import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_rescue import ENV, snapshot


class ImproveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vcr improve ')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'projet avec espaces'
        self.project.mkdir()
        (self.project / 'main.py').write_text('pass\n')
        self.before = snapshot(self.project)

    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'vcr', *map(str, args)], env=ENV, text=True, capture_output=True)

    def rescue(self, name):
        output = self.base / name
        result = self.cli('rescue', '--repo', self.project, '--out', output)
        self.assertEqual(result.returncode, 0, result.stderr)
        return output / 'run.json'

    def improve(self, output, *args):
        return self.cli('improve', '--project', self.project, '--out', output, *args)

    def test_two_real_runs_and_single_run(self):
        first, second = self.rescue('run1'), self.rescue('run2')
        single = self.base / 'single'
        result = self.improve(single, '--from', first)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads((single / 'proposals.json').read_text()), [])
        self.assertIn('Aucune récurrence déduite', (single / 'report.md').read_text())
        out = self.base / 'double'
        result = self.improve(out, '--from', first, '--from', second)
        self.assertEqual(result.returncode, 0, result.stderr)
        proposal = next(x for x in json.loads((out / 'proposals.json').read_text()) if x['id'] == 'tests-unknown')
        self.assertEqual(len(proposal['sources']), 2)
        self.assertEqual({x['source'] for x in proposal['sources']}, {str(first.resolve()), str(second.resolve())})
        self.assertTrue(all(x['status'] == 'suspected' for x in proposal['sources']))
        self.assertIn('ne prouvent ni deux incidents indépendants', (out / 'report.md').read_text())
        self.assertEqual(snapshot(self.project), self.before)

    def test_two_confirmed_and_registry_reuse(self):
        reports = [self.rescue('a'), self.rescue('b')]
        for index, report in enumerate(reports):
            data = json.loads(report.read_text())
            data['findings'] = [{'id': 'test-failure', 'status': 'confirmed', 'evidence': [{'kind': 'log', 'summary': f'échec fixture {index}'}]}]
            report.write_text(json.dumps(data))
        one, two = self.base / 'one', self.base / 'two'
        self.assertEqual(self.improve(one, '--from', reports[0]).returncode, 0)
        self.assertEqual(self.improve(two, '--registry', one / 'registry.json', '--from', reports[1]).returncode, 0)
        proposals = json.loads((two / 'proposals.json').read_text())
        self.assertEqual(len(proposals), 1)
        self.assertEqual(proposals[0]['id'], 'test-failure')
        self.assertEqual(len(proposals[0]['sources']), 2)
        self.assertTrue(all(x['status'] == 'confirmed' for x in proposals[0]['sources']))
        self.assertNotIn('échec fixture', (two / 'report.md').read_text())
        self.assertEqual(snapshot(self.project), self.before)

    def test_duplicate_run_and_excluded_feedback(self):
        first = self.rescue('one')
        feedback = first.parent / 'feedback.json'
        data = json.loads(first.read_text())
        feedback.write_text(json.dumps({'run_id': data['run_id'], 'decisions': {'tests-unknown': {'status': 'false_positive'}}}))
        out = self.base / 'out'
        result = self.improve(out, '--from', first, '--from', first)
        self.assertEqual(result.returncode, 0, result.stderr)
        registry = json.loads((out / 'registry.json').read_text())
        self.assertNotIn('tests-unknown', registry['entries'])
        self.assertEqual(json.loads((out / 'proposals.json').read_text()), [])
        self.assertIn('même run_id', (out / 'report.md').read_text())

    def test_project_mismatch_and_internal_output_refused(self):
        report = self.rescue('report')
        other = self.base / 'autre'
        other.mkdir()
        out = self.base / 'wrong'
        result = self.cli('improve', '--project', other, '--out', out, '--from', report)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(out.exists())
        result = self.improve(self.project / 'bad', '--from', report)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.project / 'bad').exists())
        self.assertEqual(snapshot(self.project), self.before)


if __name__ == '__main__':
    unittest.main()
