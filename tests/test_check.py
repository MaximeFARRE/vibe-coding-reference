import json
import contextlib
import io
from unittest.mock import patch
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
ENV = dict(os.environ, PYTHONPATH=str(ROOT / 'src'), PYTHONDONTWRITEBYTECODE='1')


class CheckTests(unittest.TestCase):
    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'vcr', 'check', *map(str, args)], env=ENV, text=True, capture_output=True)

    def test_python_git_sensitive_and_no_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            (repo / 'README.md').write_text('fixture')
            (repo / 'pyproject.toml').write_text('[project]\nname="fixture"\nversion="0.1"\n')
            (repo / '.env').write_text('PASSWORD=FAKE_SECRET_VALUE\n')
            subprocess.run(['git', '-C', str(repo), 'add', '.env'], check=True)
            before = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'])
            result = self.cli('--repo', repo, '--json', '--full')
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertNotIn('FAKE_SECRET_VALUE', result.stdout)
            checks = {x['id']: x['status'] for x in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['GIT-01'], 'passed')
            self.assertEqual(checks['GIT-05'], 'passed')
            self.assertEqual(checks['SEC-01'], 'failed')
            self.assertEqual(before, subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain']))

    def test_node_full_does_not_run_scripts_and_output_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / 'repo'; repo.mkdir()
            (repo / 'package.json').write_text(json.dumps({'scripts': {'test': 'touch SHOULD_NOT_EXIST'}}))
            (repo / 'package-lock.json').write_text('{}')
            result = self.cli('--repo', repo, '--json', '--full')
            self.assertEqual(result.returncode, 0, result.stderr)
            checks = {x['id']: x['status'] for x in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['ENV-03'], 'passed')
            self.assertEqual(checks['TEST-01-EXEC'], 'skipped')
            text = self.cli('--repo', repo, '--full').stdout
            for item in json.loads(result.stdout)['checks']:
                self.assertIn(item['id'] + ' [' + item['status'] + '] ' + item['reason'], text)
            self.assertFalse((repo / 'SHOULD_NOT_EXIST').exists())
            self.assertEqual(self.cli('--repo', repo, '--out', repo / 'report').returncode, 2)
            out = Path(tmp) / 'report.json'
            self.assertEqual(self.cli('--repo', repo, '--json', '--out', out).returncode, 0)
            self.assertEqual(self.cli('--repo', repo, '--json', '--out', out).returncode, 2)
            self.assertEqual(json.loads(out.read_text())['workflow'], 'check')


    def test_structured_evidence_and_targeted_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / 'README.md').write_text('fixture')
            (repo / '.env.example').write_text('SECRET=NEVER_PRINT_THIS')
            (repo / 'tsconfig.json').write_text('{}')
            (repo / 'package.json').write_text(json.dumps({'scripts': {'typecheck': 'dangerous', 'test': None}}))
            result = self.cli('--repo', repo, '--full', '--json')
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertNotIn('NEVER_PRINT_THIS', result.stdout)
            checks = {c['id']: c for c in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['GIT-05']['evidence'][0]['path'], 'README.md')
            self.assertIn('documentaire', checks['GIT-05']['applicability_reason'])
            self.assertNotIn('DATA-07', checks)
            self.assertNotIn('DEP-01', checks)
            self.assertIn('contenu', checks['GIT-05']['limitation'])
            self.assertEqual(checks['ENV-05']['status'], 'passed')
            self.assertEqual(checks['CODE-02']['status'], 'passed')
            self.assertEqual(checks['CODE-02-EXEC']['status'], 'skipped')
            self.assertEqual(checks['TEST-01']['status'], 'not_checked')
            self.assertTrue(all(c['source_method'] and c['applicability_reason'] for c in checks.values()))
            text = self.cli('--repo', repo).stdout
            self.assertIn('Contexte GIT-05 :', text)
            self.assertIn('Preuve GIT-05 :', text)
            self.assertIn('Limite GIT-05 :', text)

    def test_lockfile_in_different_subproject_does_not_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            (repo / 'one').mkdir(); (repo / 'two').mkdir()
            (repo / 'one' / 'package.json').write_text('{}')
            (repo / 'two' / 'package-lock.json').write_text('{}')
            result = self.cli('--repo', repo, '--json')
            checks = {c['id']: c for c in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['ENV-03']['status'], 'not_checked')
            (repo / 'one' / 'package-lock.json').write_text('{}')
            result = self.cli('--repo', repo, '--json')
            checks = {c['id']: c for c in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['ENV-03']['status'], 'passed')

    def test_schema_additions_and_rescue_compatibility(self):
        schema = json.loads((ROOT / 'schemas' / 'run.schema.json').read_text())
        props = schema['properties']['checks']['items']['properties']
        self.assertTrue({'evidence', 'source_method', 'applicability_reason', 'limitation'} <= props.keys())
        self.assertIn('check', schema['properties']['workflow']['enum'])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); repo = root / 'project'; repo.mkdir()
            output = root / 'rescue'
            result = subprocess.run([sys.executable, '-m', 'vcr', 'rescue', '--repo', str(repo), '--out', str(output)], env=ENV, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            run = json.loads((output / 'run.json').read_text())
            self.assertEqual(run['workflow'], 'rescue')
            self.assertTrue(all(set(c) <= {'id', 'status', 'reason'} for c in run['checks']))


    def test_invalid_internal_result_is_not_published(self):
        from vcr import cli
        from vcr.models import CheckResult, Run
        with tempfile.TemporaryDirectory() as tmp:
            run = Run('0.1', 'id', '2026-11-14T00:00:00Z', 'check',
                      {'path': tmp, 'mode': 'read_only'}, [],
                      [CheckResult('BROKEN', 'passed', 'Sans preuve')], [], [])
            stdout = io.StringIO(); stderr = io.StringIO()
            with patch.object(cli, 'run_checks', return_value=run), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                code = cli.main(['check', '--repo', tmp, '--json'])
            self.assertEqual(code, 2)
            self.assertEqual(stdout.getvalue(), '')
            self.assertIn('preuve', stderr.getvalue().lower())

    def test_invalid_target_and_external_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); repo = root / 'repo'; repo.mkdir()
            (root / 'README.md').write_text('secret')
            (repo / 'README.md').symlink_to(root / 'README.md')
            result = self.cli('--repo', repo, '--json')
            self.assertEqual(result.returncode, 0)
            checks = {x['id']: x['status'] for x in json.loads(result.stdout)['checks']}
            self.assertEqual(checks['GIT-05'], 'not_checked')
            self.assertEqual(self.cli('--repo', root / 'missing').returncode, 2)
