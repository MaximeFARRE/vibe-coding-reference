"""Parcours complet local sur fixture, sans connexion Python au réseau."""
import json
import socket
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from test_rescue import snapshot
from vcr.cli import main


class UserJourneyTests(unittest.TestCase):
    def test_full_local_journey_preserves_fixture(self):
        with tempfile.TemporaryDirectory(prefix='vcr parcours ') as tmp:
            root = Path(tmp)
            repo = root / 'projet fictif'
            repo.mkdir()
            (repo / 'package.json').write_text('{"dependencies":{"next":"fixture"}}')
            (repo / '.env').write_text('PASSWORD=faux_secret_parcours_439')
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            before = snapshot(repo)
            before_status = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain'])
            report1, report2 = root / 'rapport 1', root / 'rapport 2'
            start, improved = root / 'cadrage', root / 'améliorations'
            questions = iter(['1', str(start), 'Gérer une liste', 'Cliquer sur Ajouter', 'Voir l’élément', '3', 'une équipe', '2', 'libellés fictifs', '2', '1', '2', '1', '2', 'simple'])
            stdout, stderr = StringIO(), StringIO()
            with patch.object(socket, 'socket', side_effect=AssertionError('Accès réseau interdit dans ce test')), redirect_stdout(stdout), redirect_stderr(stderr):
                with patch('sys.stdin.isatty', return_value=True), patch('builtins.input', side_effect=lambda _: next(questions)):
                    self.assertEqual(main([]), 0)
                for output in (report1, report2):
                    self.assertEqual(main(['rescue', '--repo', str(repo), '--out', str(output)]), 0)
                self.assertEqual(main(['feedback', '--report', str(report1), '--finding', 'tests-unknown', '--decision', 'deferred']), 0)
                self.assertEqual(main(['improve', '--project', str(repo), '--from', str(report1 / 'run.json'), '--from', str(report2 / 'run.json'), '--out', str(improved)]), 0)
                self.assertEqual(main(['improve-feedback', '--registry', str(improved / 'registry.json'), '--proposal', 'tests-unknown', '--decision', 'deferred']), 0)
                self.assertEqual(main(['tokens']), 0)
                self.assertEqual(main(['sources', '--topic', 'tokens']), 0)
            self.assertEqual(stderr.getvalue(), '')
            self.assertIn('Voir l’élément', (start / 'acceptance-criteria.md').read_text())
            self.assertIn('Aucune trace fournie', stdout.getvalue())
            self.assertIn('TokenEconomizer', stdout.getvalue())
            proposals = json.loads((improved / 'proposals.json').read_text())
            finding = next(p for p in proposals if p['id'] == 'tests-unknown')
            self.assertEqual(len(finding['sources']), 2)
            registry = json.loads((improved / 'registry.json').read_text())
            self.assertEqual(registry['entries']['tests-unknown']['approval_status'], 'deferred')
            for folder in (start, report1, report2, improved):
                for file in folder.iterdir():
                    self.assertNotIn('faux_secret_parcours_439', file.read_text())
            self.assertEqual(snapshot(repo), before)
            self.assertEqual(subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain']), before_status)


if __name__ == '__main__':
    unittest.main()
