import unittest

from vcr.start_options import suggest


class StackOptionsTests(unittest.TestCase):
    def base(self, **changes):
        data = {'kind': 'unknown', 'access': 'unknown', 'persistence': 'unknown', 'sensitive': 'unknown', 'interaction': 'unknown', 'python': 'unknown', 'seo': 'unknown'}
        data.update(changes)
        return data

    def test_profiles_choose_conditional_families(self):
        scenarios = [
            ({'kind': 'site', 'access': 'public', 'persistence': 'no', 'sensitive': 'no'}, 'Site statique'),
            ({'kind': 'fullstack', 'access': 'public'}, 'Application web intégrée'),
            ({'kind': 'crud', 'access': 'private'}, 'Application de gestion côté serveur'),
            ({'kind': 'python', 'access': 'public'}, 'Backend Python avec pages simples'),
            ({'kind': 'local', 'access': 'local'}, 'Utilitaire local'),
            ({'kind': 'interactive', 'interaction': 'rich'}, 'Application web intégrée'),
        ]
        for inputs, expected in scenarios:
            with self.subTest(profile=inputs):
                options, _ = suggest(self.base(**inputs))
                self.assertEqual(options[0]['name'], expected)
                self.assertTrue(1 <= len(options) <= 3)
                for option in options:
                    for field in ('language', 'framework', 'architecture', 'infrastructure', 'database', 'advantage', 'drawback', 'condition', 'cost'):
                        self.assertTrue(option[field])

    def test_contradictions_and_unknowns_remain_explicit(self):
        options, warnings = suggest(self.base(kind='site', access='public', persistence='yes', sensitive='yes'))
        self.assertNotEqual(options[0]['name'], 'Site statique')
        self.assertTrue(any('site vitrine' in w for w in warnings))
        _, warnings = suggest(self.base(kind='local', access='public'))
        self.assertTrue(any('contradictoires' in w for w in warnings))
        options, _ = suggest(self.base(kind='python', persistence='yes'))
        self.assertIn('À déterminer', options[0]['database'])
        options, _ = suggest(self.base(kind='local', access='local', persistence='no'))
        self.assertIn('Aucune base', options[0]['database'])


if __name__ == '__main__':
    unittest.main()
