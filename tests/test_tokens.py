import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from test_rescue import ENV, snapshot
from vcr.cli import main


class TokenTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='vcr tokens ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = self.root / 'projet avec espaces'
        self.project.mkdir()
        (self.project / 'main.py').write_text('pass\n')
        self.before = snapshot(self.project)
        self.trace = self.root / 'trace.json'
        self.output = self.root / 'rapport'

    def cli(self, *args):
        return subprocess.run([sys.executable, '-m', 'vcr', *map(str, args)], env=ENV, capture_output=True, text=True)

    def write_trace(self, records):
        self.trace.write_text(json.dumps({'format': 'vcr-token-trace-v1', 'records': records}))

    def test_no_trace_diagnostic(self):
        result = self.cli('tokens')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Aucune trace fournie', result.stdout)
        self.assertIn('Quota d’abonnement — unavailable', result.stdout)
        self.assertNotIn('€', result.stdout)
        self.assertNotIn('cache =', result.stdout)
        self.assertEqual(snapshot(self.project), self.before)

    def test_t009_without_cache_or_cost(self):
        self.write_trace([{'input_tokens': 100, 'output_tokens': 20}])
        result = self.cli('tokens', '--from', self.trace, '--out', self.output, '--project', self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads((self.output / 'tokens.json').read_text())
        self.assertEqual(data['metrics']['cache_read_tokens']['status'], 'unavailable')
        self.assertEqual(data['metrics']['cost_declared']['status'], 'unavailable')
        self.assertEqual(data['metrics']['subscription_quota']['status'], 'unavailable')
        self.assertEqual(data['metrics']['volume_total_tokens']['value'], 120)
        text = (self.output / 'report.md').read_text()
        self.assertNotIn('€', text)
        self.assertNotIn('cache =', text)
        self.assertNotIn('économisés', text)
        self.assertEqual(snapshot(self.project), self.before)

    def test_cache_cost_and_signals_without_private_content(self):
        def cost(amount):
            return {'amount': amount, 'currency': 'EUR', 'kind': 'actual', 'provider': 'secret_provider_fixture', 'date': '2026-11-14'}
        records = [
            {'input_tokens': 100, 'output_tokens': 10, 'cache_read_tokens': 30, 'cache_write_tokens': 9, 'cost': cost(0.1), 'session_id': 'secret_session_fixture', 'model': 'secret_model_fixture', 'tool': 'secret_tool_fixture', 'search_fingerprint': 'a' * 64, 'topic_count': 2, 'command_chars': 1200},
            {'input_tokens': 200, 'output_tokens': 20, 'cache_read_tokens': 20, 'cache_write_tokens': 8, 'cost': cost(0.2), 'session_id': 'secret_session_fixture', 'tool': 'secret_tool_fixture', 'search_fingerprint': 'a' * 64},
        ]
        self.write_trace(records)
        result = self.cli('tokens', '--from', self.trace, '--out', self.output, '--project', self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads((self.output / 'tokens.json').read_text())
        metrics = data['metrics']
        self.assertEqual(metrics['volume_total_tokens']['value'], 330)
        self.assertEqual(metrics['uncached_input_tokens']['value'], 250)
        self.assertEqual(metrics['cache_write_tokens']['value'], 17)
        self.assertEqual(metrics['cost_declared']['value'], '0.3')
        self.assertEqual(metrics['subscription_quota']['status'], 'unavailable')
        self.assertEqual(data['signals']['repeated_searches'][0]['record_refs'], [1, 2])
        self.assertEqual(data['signals']['multi_topic_sessions'], 1)
        self.assertEqual(data['signals']['long_command_count'], 1)
        output = ''.join(p.read_text() for p in self.output.iterdir())
        for forbidden in ('secret_provider_fixture', 'secret_session_fixture', 'secret_model_fixture', 'secret_tool_fixture', 'a' * 64):
            self.assertNotIn(forbidden, output)
        self.assertEqual(snapshot(self.project), self.before)

    def test_partial_data_and_output_safety(self):
        self.write_trace([{'input_tokens': 100}, {'output_tokens': 20}])
        result = self.cli('tokens', '--from', self.trace, '--out', self.output, '--project', self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        metrics = json.loads((self.output / 'tokens.json').read_text())['metrics']
        self.assertEqual(metrics['input_tokens']['status'], 'unavailable')
        self.assertEqual(metrics['volume_total_tokens']['status'], 'unavailable')
        result = self.cli('tokens', '--from', self.trace, '--out', self.project / 'tokens', '--project', self.project)
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.project / 'tokens').exists())
        result = self.cli('tokens', '--out', self.output)
        self.assertEqual(result.returncode, 2)

    def test_menu_diagnostic(self):
        from io import StringIO
        with patch('sys.stdin.isatty', return_value=True), patch('builtins.input', side_effect=['4', '', '']), patch('sys.stdout', new_callable=StringIO) as output:
            self.assertEqual(main([]), 0)
        self.assertIn('Aucune trace fournie', output.getvalue())


if __name__ == '__main__':
    unittest.main()
