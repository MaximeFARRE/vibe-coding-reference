import os
import socket
import subprocess
import sys
import tempfile
import unittest
import zipfile
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from test_rescue import ENV, ROOT
from vcr.catalog import load_catalog, normalize_catalog, render, search, valid_url
from vcr.cli import main


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = load_catalog()

    def test_tokens_query_has_dated_sources_and_separate_status(self):
        result = subprocess.run([sys.executable, '-m', 'vcr', 'sources', '--topic', 'tokens'], env=ENV, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('2026-11-14', result.stdout)
        self.assertIn('TokenEconomizer', result.stdout)
        self.assertIn('https://github.com/microsoft/TokenEconomizer', result.stdout)
        self.assertIn('Niveau de complexité :** B', result.stdout)
        self.assertIn('Statut de preuve :** unverified', result.stdout)
        self.assertIn('Accès au lien officiel :** verified', result.stdout)
        self.assertIn('licence', result.stdout.lower())
        self.assertNotIn('meilleur skill', result.stdout.lower())

    def test_t015_missing_url_and_maintenance_is_unverified(self):
        data = {'version': 1, 'review_date': '2026-11-14', 'entries': [{'id': 'missing', 'name': 'Incomplet', 'kind': 'tool', 'topics': ['tokens'], 'level': 'B', 'evidence_status': 'verified'}]}
        item = normalize_catalog(data)['entries'][0]
        self.assertEqual(item['evidence_status'], 'unverified')
        self.assertEqual(item['maintenance_status'], 'unverified')
        self.assertEqual(item['link_status'], 'unverified')
        self.assertIsNone(item['official_url'])
        self.assertFalse(item['recommended_by_default'])
        output = render(normalize_catalog(data), 'tokens')
        self.assertIn('URL invalide', output)
        self.assertIn('non recommandée', output)

    def test_each_tool_has_safety_fields_and_no_auto_recommendation(self):
        for item in self.catalog['entries']:
            with self.subTest(id=item['id']):
                for field in ('problem', 'incompatibilities', 'hidden_costs', 'permissions', 'license', 'verification', 'rollback', 'maintainer', 'version'):
                    self.assertTrue(item[field])
                self.assertIn(item['level'], ('A', 'B', 'C'))
                self.assertEqual(item['evidence_status'], 'unverified')
                self.assertEqual(item['maintenance_status'], 'verified' if item['kind'] == 'tool' else 'unverified')
                self.assertEqual(item['link_status'], 'verified')
                self.assertFalse(item['recommended_by_default'])
                self.assertTrue(valid_url(item['official_url']))

    def test_verified_state_requires_provenance_and_complete_fields(self):
        item = dict(self.catalog['entries'][0])
        item.update(evidence_status='verified', maintenance_status='verified', maintainer='fixture', version='1', license='fixture')
        data = {'version': 1, 'review_date': '2026-11-14', 'entries': [item]}
        self.assertEqual(normalize_catalog(data)['entries'][0]['evidence_status'], 'unverified')
        item.update(evidence_verified_at='2026-11-14', verification_source='https://example.com/evidence', maintenance_verified_at='2026-11-14', maintenance_source='https://example.com/maintenance', maintenance_detail='Métadonnée de fixture')
        result = normalize_catalog(data)['entries'][0]
        self.assertEqual(result['evidence_status'], 'verified')
        self.assertEqual(result['maintenance_status'], 'verified')
        self.assertFalse(result['recommended_by_default'])
        self.assertIn('https://example.com/evidence', render(normalize_catalog(data)))

    def test_filter_unknown_urls_and_duplicate_id(self):
        self.assertEqual(search(self.catalog, ' TOKENS '), search(self.catalog, 'tokens'))
        self.assertIn('Aucun résultat', render(self.catalog, 'inexistant'))
        self.assertFalse(valid_url('javascript:alert(1)'))
        self.assertFalse(valid_url('https://user:password@example.com'))
        item = self.catalog['entries'][0]
        with self.assertRaises(ValueError):
            normalize_catalog({'version': 1, 'entries': [item, item]})

    def test_menu_and_local_read_do_not_open_network(self):
        with patch.object(socket, 'socket', side_effect=AssertionError('network')), patch('sys.stdin.isatty', return_value=True), patch('builtins.input', side_effect=['5', 'navigation']), patch('sys.stdout', new_callable=StringIO) as output:
            self.assertEqual(main([]), 0)
        self.assertIn('Serena', output.getvalue())
        self.assertNotIn('TokenEconomizer —', output.getvalue())

    def test_catalog_resource_loads_from_zipped_package(self):
        with tempfile.TemporaryDirectory(prefix='vcr catalog ') as tmp:
            archive = Path(tmp) / 'vcr.zip'
            with zipfile.ZipFile(archive, 'w') as z:
                for name in ('__init__.py', 'catalog.py', 'catalog.json'):
                    z.write(ROOT / 'src' / 'vcr' / name, 'vcr/' + name)
            env = dict(os.environ, PYTHONPATH=str(archive), PYTHONDONTWRITEBYTECODE='1')
            result = subprocess.run([sys.executable, '-c', 'from vcr.catalog import load_catalog; print(len(load_catalog()["entries"]))'], cwd=tmp, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(int(result.stdout), len(self.catalog['entries']))


if __name__ == '__main__':
    unittest.main()
