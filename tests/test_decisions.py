import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_rescue import ENV, ROOT, snapshot


class DecisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='vcr décision ')
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.repo = self.base / 'projet'
        self.repo.mkdir()
        self.out = self.base / 'rapport'
        (self.repo / '.env').write_text('PASSWORD=secret_fixture_decision')
        self.before = snapshot(self.repo)
        result = self.cli('rescue', '--repo', self.repo, '--out', self.out)
        self.assertEqual(result.returncode, 0, result.stderr)

    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'vcr', *map(str, args)], env=ENV, capture_output=True, text=True)

    def test_report_contains_decision_proof_and_shared_fields(self):
        data = json.loads((self.out / 'run.json').read_text())
        report = (self.out / 'report.md').read_text()
        finding = next(f for f in data['findings'] if f['id'] == 'env-present')
        for key in ('impact', 'alternatives', 'risks_of_fix', 'invariants_to_preserve', 'verification_plan'):
            self.assertTrue(finding[key])
        for fragment in ('env-present', 'suspected', 'low', 'static_check', 'Solution A', 'Solution B', 'Approbation humaine', 'Ordre de revue à copier', '.env'):
            self.assertIn(fragment, report)
        self.assertEqual(finding['evidence'][0]['path'], '.env')
        self.assertNotIn('secret_fixture_decision', report)
        self.assertEqual(snapshot(self.repo), self.before)

    def test_feedback_choices_update_only_report(self):
        for decision in ('accepted', 'rejected', 'false_positive', 'deferred'):
            result = self.cli('feedback', '--report', self.out, '--finding', 'env-present', '--decision', decision)
            self.assertEqual(result.returncode, 0, result.stderr)
            feedback = json.loads((self.out / 'feedback.json').read_text())
            self.assertEqual(feedback['decisions']['env-present']['status'], decision)
        bad = self.cli('feedback', '--report', self.out, '--finding', 'unknown', '--decision', 'accepted')
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(json.loads((self.out / 'feedback.json').read_text())['decisions']['env-present']['status'], 'deferred')
        self.assertEqual(snapshot(self.repo), self.before)

    def test_feedback_symlink_and_target_report_refused(self):
        (self.out / 'feedback.json').symlink_to(self.repo / '.env')
        result = self.cli('feedback', '--report', self.out, '--finding', 'env-present', '--decision', 'accepted')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(snapshot(self.repo), self.before)
        (self.repo / 'run.json').write_text((self.out / 'run.json').read_text())
        result = self.cli('feedback', '--report', self.repo, '--finding', 'env-present', '--decision', 'accepted')
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.repo / 'feedback.json').exists())

    def test_run_matches_documented_schema_subset(self):
        schemas = {name: json.loads((ROOT / 'schemas' / name).read_text()) for name in ('run.schema.json', 'finding.schema.json')}
        types = {'object': dict, 'array': list, 'string': str, 'integer': int, 'boolean': bool, 'null': type(None)}
        def validate(value, schema):
            if '$ref' in schema:
                return validate(value, schemas[schema['$ref']])
            expected = schema.get('type')
            if expected:
                allowed = expected if isinstance(expected, list) else [expected]
                self.assertTrue(any(type(value) is types[k] for k in allowed), (value, allowed))
            if 'enum' in schema: self.assertIn(value, schema['enum'])
            if 'const' in schema: self.assertEqual(value, schema['const'])
            if isinstance(value, dict):
                for key in schema.get('required', []): self.assertIn(key, value)
                props = schema.get('properties', {})
                if schema.get('additionalProperties') is False: self.assertFalse(set(value) - set(props))
                for key, child in value.items():
                    if key in props: validate(child, props[key])
            if isinstance(value, list) and 'items' in schema:
                for item in value: validate(item, schema['items'])
            if isinstance(value, int) and 'minimum' in schema: self.assertGreaterEqual(value, schema['minimum'])
            if isinstance(value, str) and 'minLength' in schema: self.assertGreaterEqual(len(value), schema['minLength'])
        validate(json.loads((self.out / 'run.json').read_text()), schemas['run.schema.json'])


if __name__ == '__main__':
    unittest.main()
