import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from vcr.cli import main
from vcr.start_options import suggest
from vcr.start_questions import ask
from test_rescue import ENV


class StartTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='vcr start ')
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.out = self.base / 'résultat avec espaces'

    def cli(self, args, answers=''):
        return subprocess.run([sys.executable, '-m', 'vcr', *map(str, args)], input=answers, env=ENV, text=True, capture_output=True)

    def test_full_interactive_workflow_and_resume(self):
        responses = '\n'.join(['Présenter des activités locales', 'Cliquer sur Activités', 'Voir la liste des activités', '1', 'visiteurs', '3', 'texte public', '2', '2', '1', '1', '2', 'petit budget']) + '\n'
        result = self.cli(['start', '--interactive', '--out', self.out], responses)
        self.assertEqual(result.returncode, 0, result.stderr)
        expected = {'answers.json', 'project-brief.md', 'acceptance-criteria.md', 'stack-options.md', 'START_PROMPT_FOR_CODEX.md'}
        self.assertEqual({p.name for p in self.out.iterdir()}, expected)
        brief = (self.out / 'project-brief.md').read_text()
        criteria = (self.out / 'acceptance-criteria.md').read_text()
        stack = (self.out / 'stack-options.md').read_text()
        self.assertIn('Présenter des activités locales', brief)
        self.assertIn('Cliquer sur Activités', criteria)
        self.assertIn('Voir la liste des activités', criteria)
        self.assertIn('Site statique', stack)
        self.assertIn('Aucune base requise', stack)
        self.assertIn('Hébergement public', stack)
        resumed = self.base / 'reprise'
        result = self.cli(['start', '--from', self.out / 'answers.json', '--out', resumed])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('Que doit permettre', result.stdout)
        self.assertEqual(json.loads((self.out / 'answers.json').read_text()), json.loads((resumed / 'answers.json').read_text()))

    def test_partial_resume_asks_only_missing_answers(self):
        previous = self.base / 'partial.json'
        previous.write_text(json.dumps({'version': 1, 'answers': {'goal': 'Consulter des dossiers', 'action': 'Ouvrir un dossier', 'outcome': 'Voir son contenu', 'kind': 'crud'}}))
        answers = '\n'.join(['une équipe', '2', 'des dossiers fictifs', '1', '1', '2', '1', '2', 'budget limité']) + '\n'
        result = self.cli(['start', '--out', self.out, '--from', previous], answers)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn('Que doit permettre', result.stdout)
        self.assertNotIn('Type :', result.stdout)
        self.assertIn('Qui utilisera', result.stdout)
        self.assertIn('gestion côté serveur', (self.out / 'stack-options.md').read_text())
        self.assertIn('quand une donnée est enregistrée', (self.out / 'acceptance-criteria.md').read_text())

    def test_missing_invalid_and_no_overwrite(self):
        self.out.mkdir()
        (self.out / 'keep').write_text('keep')
        result = self.cli(['start', '--out', self.out])
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.out / 'keep').read_text(), 'keep')
        destination = self.base / 'absent'
        result = self.cli(['start', '--out', destination], 'idée\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(destination.exists())
        invalid = self.base / 'invalid.json'
        invalid.write_text('{"version":1,"answers":{"access":"bad"}}')
        result = self.cli(['start', '--out', destination, '--from', invalid])
        self.assertEqual(result.returncode, 2)
        self.assertFalse(destination.exists())

    def test_choices_and_unknown_answers(self):
        values = iter(['idée', '', '', '9', '0', '', '', '', '', '', '', '', '', ''])
        output = []
        answers = ask(input_fn=lambda _: next(values), print_fn=output.append)
        self.assertEqual(answers['kind'], 'unknown')
        self.assertIn('Choisissez un numéro indiqué.', output)
        options, warnings = suggest(answers)
        self.assertEqual(len(options), 1)
        self.assertTrue(warnings)
        self.assertIn('À déterminer', options[0]['database'])

    def test_menu_start_uses_same_workflow(self):
        responses = iter(['1', str(self.out), 'idée', 'Ouvrir', 'Voir', '5', 'moi', '1', '', '2', '2', '2', '1', '2', ''])
        with patch('sys.stdin.isatty', return_value=True), patch('builtins.input', side_effect=lambda _: next(responses)):
            self.assertEqual(main([]), 0)
        self.assertTrue((self.out / 'project-brief.md').exists())


if __name__ == '__main__':
    unittest.main()
