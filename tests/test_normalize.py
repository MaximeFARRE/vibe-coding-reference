import tempfile
import unittest
from pathlib import Path

from vcr.models import CheckResult, Evidence, Finding, Run
from vcr.normalize import normalize
from vcr.report import render


class NormalizationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / 'code.py').write_text('first\nsecond\n')
        self.run = Run('0.1', 'run', '2026-11-14T00:00:00Z', 'rescue', {'path': str(self.repo), 'mode': 'read_only'}, [], [], [], [])

    def finding(self, id, evidence, **kwargs):
        return Finding(id, 'Titre', 'code', 'P2', 'confirmed', 'high', 'static_check', 'Résumé', evidence, ['Action'], **kwargs)


    def test_check_validation_rejects_invalid_evidence_and_duplicate_ids(self):
        self.run.workflow = 'check'
        self.run.checks = [CheckResult('A', 'passed', 'Fichier présent', [Evidence('file', 'Présent', path='code.py')], 'inventaire', 'Tous')]
        self.assertEqual(normalize(self.run, self.repo).checks[0].status, 'passed')
        for evidence in (None, [Evidence('bogus', 'Présent')], [Evidence('file', 'Présent', redacted='oui')], [Evidence('file', 'Présent', line_start=1)], [Evidence('file', 'Présent', path='../outside')]):
            with self.subTest(evidence=evidence):
                self.run.checks[0].evidence = evidence
                with self.assertRaises(ValueError):
                    normalize(self.run, self.repo)
        self.run.checks[0].evidence = [Evidence('file', 'Présent')]
        self.run.checks.append(CheckResult('A', 'not_checked', 'Inconnu'))
        with self.assertRaisesRegex(ValueError, 'double'):
            normalize(self.run, self.repo)

    def test_optional_fields_keep_older_rescue_checks_compatible(self):
        self.run.checks = [CheckResult('legacy', 'passed', 'Réalisé')]
        self.assertEqual(normalize(self.run, self.repo).checks[0].id, 'legacy')
        self.run.checks[0].source_method = 12
        with self.assertRaises(ValueError):
            normalize(self.run, self.repo)

    def test_invalid_line_degrades_confidence_and_status(self):
        self.run.findings = [self.finding('x', [Evidence('file', 'Indice', path='code.py', line_start=8)])]
        result = normalize(self.run, self.repo).findings[0]
        self.assertEqual((result.status, result.confidence), ('suspected', 'low'))
        self.assertIsNone(result.evidence[0].line_start)
        self.assertIn('localisation invalide', result.limitations[0])
        self.assertEqual(self.run.findings[0].evidence[0].line_start, 8)

    def test_valid_line_and_invalid_enum(self):
        self.run.findings = [self.finding('x', [Evidence('file', 'Indice', path='code.py', line_start=2)])]
        self.assertEqual(normalize(self.run, self.repo).findings[0].status, 'confirmed')
        self.run.findings[0].status = 'verified'
        with self.assertRaisesRegex(ValueError, 'énumération'):
            normalize(self.run, self.repo)

    def test_render_links_to_validated_file_and_line(self):
        self.run.findings = [self.finding('x', [Evidence('file', 'Indice', path='code.py', line_start=2)])]
        report = render(normalize(self.run, self.repo))
        self.assertIn('[code.py:2](', report)
        self.assertIn('/code.py)', report)
        self.assertIn('ligne 2', report)

    def test_only_same_rule_cause_and_location_deduplicates(self):
        def item(id, cause='cause', line=1, rule='rule'):
            return self.finding(id, [Evidence('file', 'Indice', path='code.py', line_start=line)], rule_id=rule, cause=cause)
        self.run.findings = [item('a'), item('b'), item('c', cause='autre'), item('d', line=2), item('e', rule=None), item('f', rule=None)]
        result = normalize(self.run, self.repo)
        self.assertEqual([f.id for f in result.findings], ['a', 'c', 'd', 'e', 'f'])
        self.assertIn('dupliqué', result.limitations[-1])

    def test_escape_and_symlink_are_rejected(self):
        (self.repo / 'link').symlink_to(self.repo / 'code.py')
        self.run.findings = [self.finding('a', [Evidence('file', 'Indice', path='link', line_start=1)]), self.finding('b', [Evidence('file', 'Indice', path='../outside', line_start=1)])]
        result = normalize(self.run, self.repo)
        self.assertTrue(all(f.status == 'suspected' and f.evidence[0].path is None for f in result.findings))

    def test_empty_evidence_and_bad_target(self):
        self.run.findings = [self.finding('a', [])]
        self.assertEqual(normalize(self.run, self.repo).findings[0].confidence, 'low')
        self.run.target['git_dirty'] = 'yes'
        with self.assertRaisesRegex(ValueError, 'Git'):
            normalize(self.run, self.repo)


if __name__ == '__main__':
    unittest.main()
