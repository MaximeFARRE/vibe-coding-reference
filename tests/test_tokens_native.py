import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_rescue import ENV
from vcr.tokens_analysis import analyse
from vcr.tokens_native import read_response


class NativeUsageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='vcr api fixture ')
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'response.json'

    def write(self, data):
        self.path.write_text(json.dumps(data))

    def test_openai_response_cached_input_and_private_content(self):
        self.write({'output': [{'text': 'secret_output_fixture'}], 'usage': {'input_tokens': 100, 'input_tokens_details': {'cached_tokens': 40, 'cache_write_tokens': 5}, 'output_tokens': 20, 'output_tokens_details': {'reasoning_tokens': 7}, 'total_tokens': 120}})
        records, derived = read_response(self.path, 'openai-responses')
        data = analyse(records, derived, 'openai-responses')
        self.assertEqual(data['metrics']['input_tokens']['value'], 100)
        self.assertEqual(data['metrics']['cache_read_tokens']['value'], 40)
        self.assertEqual(data['metrics']['cache_write_tokens']['value'], 5)
        self.assertEqual(data['metrics']['volume_total_tokens']['value'], 120)
        self.assertEqual(data['metrics']['uncached_input_tokens']['value'], 60)
        self.assertEqual(data['metrics']['cost_declared']['status'], 'unavailable')
        self.assertNotIn('secret_output_fixture', json.dumps(data))

    def test_anthropic_input_components_not_double_counted(self):
        self.write({'content': [{'text': 'private_fixture'}], 'usage': {'input_tokens': 10, 'cache_read_input_tokens': 100, 'cache_creation_input_tokens': 20, 'output_tokens': 5}})
        records, derived = read_response(self.path, 'anthropic-messages')
        data = analyse(records, derived, 'anthropic-messages')
        self.assertEqual(data['metrics']['input_tokens']['value'], 130)
        self.assertEqual(data['metrics']['input_tokens']['status'], 'estimated')
        self.assertEqual(data['metrics']['uncached_input_tokens']['value'], 30)
        self.assertEqual(data['metrics']['volume_total_tokens']['value'], 135)
        self.assertNotIn('private_fixture', json.dumps(data))

    def test_missing_fields_remain_unavailable(self):
        self.write({'usage': {'input_tokens': 10, 'cache_read_input_tokens': 100, 'output_tokens': 5}})
        records, derived = read_response(self.path, 'anthropic-messages')
        data = analyse(records, derived, 'anthropic-messages')
        self.assertEqual(data['metrics']['input_tokens']['status'], 'unavailable')
        self.assertEqual(data['metrics']['cache_write_tokens']['status'], 'unavailable')
        self.assertEqual(data['metrics']['volume_total_tokens']['status'], 'unavailable')
        self.write({'usage': None})
        records, derived = read_response(self.path, 'openai-responses')
        self.assertEqual(analyse(records, derived)['metrics']['input_tokens']['status'], 'unavailable')

    def test_invalid_or_ambiguous_is_rejected(self):
        for data, kind in [({'content': []}, 'openai-responses'), ({'usage': {'input_tokens': 1, 'input_tokens_details': {'cached_tokens': 2}}}, 'openai-responses'), ({'usage': {'input_tokens': -1}}, 'anthropic-messages'), ({'usage': {'output_tokens': True}}, 'openai-responses')]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.write(data)
                read_response(self.path, kind)

    def test_cli_requires_explicit_format_and_does_not_echo(self):
        self.write({'content': 'secret fixture string', 'usage': {'input_tokens': 10, 'output_tokens': 5}})
        result = subprocess.run([sys.executable, '-m', 'vcr', 'tokens', '--from', str(self.path), '--format', 'openai-responses'], env=ENV, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('openai-responses', result.stdout)
        self.assertNotIn('secret fixture string', result.stdout)
        self.assertIn('unavailable', result.stdout)
        result = subprocess.run([sys.executable, '-m', 'vcr', 'tokens', '--format', 'anthropic-messages'], env=ENV, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
