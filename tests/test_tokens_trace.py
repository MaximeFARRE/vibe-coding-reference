import json
import tempfile
import unittest
from pathlib import Path

from vcr.tokens_analysis import analyse
from vcr.tokens_trace import load_trace


class TraceValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.file = Path(self.tmp.name) / 'trace.json'

    def trace(self, data):
        self.file.write_text(json.dumps(data))
        return load_trace(self.file)

    def test_rejects_unknown_and_invalid_values(self):
        bad_records = [
            {'input_tokens': -1}, {'input_tokens': True}, {'output_tokens': 1.2},
            {'input_tokens': 1, 'cache_read_tokens': 2}, {'prompt': 'secret'},
            {'search_fingerprint': 'not-a-hash'}, {'cost': {'amount': 1}},
            {'cost': {'amount': True, 'currency': 'EUR', 'kind': 'actual', 'provider': 'x', 'date': '2026-11-14'}},
            {'cost': {'amount': -1, 'currency': 'EUR', 'kind': 'actual', 'provider': 'x', 'date': '2026-11-14'}},
            {'cost': {'amount': 1, 'currency': 'EUR', 'kind': 'actual', 'provider': 'x', 'date': '2026-02-30'}},
        ]
        for record in bad_records:
            with self.subTest(record=record), self.assertRaises(ValueError):
                self.trace({'format': 'vcr-token-trace-v1', 'records': [record]})
        with self.assertRaises(ValueError):
            self.trace({'format': 'unknown', 'records': []})
        self.file.write_text('{"format":"vcr-token-trace-v1","records":[{"input_tokens":NaN}]}')
        with self.assertRaises(ValueError):
            load_trace(self.file)
        self.file.write_text('{"format":"vcr-token-trace-v1","records":[{"input_tokens":1,"input_tokens":2}]}')
        with self.assertRaises(ValueError):
            load_trace(self.file)

    def test_mixed_currency_or_missing_cost_is_unavailable(self):
        def cost(currency, kind='actual'):
            return {'amount': 1, 'currency': currency, 'kind': kind, 'provider': 'fixture', 'date': '2026-11-14'}
        for records in ([{'cost': cost('EUR')}, {'cost': cost('USD')}], [{'cost': cost('EUR')}, {}], [{'cost': cost('EUR')}, {'cost': cost('EUR', 'estimated')} ]):
            data = analyse(self.trace({'format': 'vcr-token-trace-v1', 'records': records}))
            self.assertEqual(data['metrics']['cost_declared']['status'], 'unavailable')
            self.assertIsNone(data['metrics']['cost_declared']['value'])

    def test_estimated_cost_and_empty_trace(self):
        data = self.trace({'format': 'vcr-token-trace-v1', 'records': [{'cost': {'amount': 1, 'currency': 'USD', 'kind': 'estimated', 'provider': 'fixture', 'date': '2026-11-14'}}]})
        self.assertEqual(analyse(data)['metrics']['cost_declared']['status'], 'estimated')
        empty = analyse(self.trace({'format': 'vcr-token-trace-v1', 'records': []}))
        self.assertTrue(empty['trace_supplied'])
        self.assertEqual(empty['record_count'], 0)
        self.assertEqual(empty['metrics']['input_tokens']['status'], 'unavailable')
        self.assertIsNone(empty['signals']['long_command_count'])

    def test_decimal_precision_limit_and_symlink(self):
        self.file.write_text('{"format":"vcr-token-trace-v1","records":[{"cost":{"amount":0.0000000000000000001,"currency":"EUR","kind":"actual","provider":"x","date":"2026-11-14"}}]}')
        with self.assertRaises(ValueError):
            load_trace(self.file)
        link = self.file.parent / 'link'
        link.symlink_to(self.file)
        with self.assertRaises(ValueError):
            load_trace(link)


if __name__ == '__main__':
    unittest.main()
