# Catalogue local : liens, preuves et maintenance

- Date : 2026-11-14 ; statut : décidé pour le lot 6.
- Question : rendre les sources et outils consultables sans installation ni classement artificiel.
- Sources : [backlog lot 6](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [catalogue](../src/vcr/catalog.json), [chargeur](../src/vcr/catalog.py), [tests](../tests/test_catalog.py).

## Résultats et limites

- **Confirmé par consultation publique** : les neuf liens officiels et les deux liens scientifiques renseignés ont été ouverts le 2026-11-14. Une page accessible ne valide ni sa sécurité, ni ses résultats, ni une compatibilité locale.
- **Confirmé par métadonnées publiques GitHub** : huit dépôts ne sont pas archivés et leur date de dernier push est conservée dans les fiches, avec source et date de consultation. Ce signal ne prouve pas la qualité du support.
- **Confirmé par documentation officielle** : les licences affichées dans les huit dépôts ont été relevées, notamment [Serena](https://github.com/oraios/serena) : application GPL-3.0-or-later, composant SolidLSP MIT. Les licences réelles peuvent changer selon version et composants.
- **Confirmé sur fixtures** : filtre par thème, séparation lien / maintenance / preuve, refus d'URL incomplète et absence de recommandation par défaut. Le catalogue est chargé hors ligne, y compris depuis un paquet ZIP de fixture.
- **Non vérifié** : sécurité du code, compatibilité avec les versions locales, installation, retrait effectif et efficacité indépendante. Toutes les évaluations de preuve restent `unverified` ; aucun outil installé.

## Options et décision

- JSON embarqué et recherche par tags : simple, hors ligne, inspectable et sans API ; les fiches nécessitent une revue manuelle datée.
- Annuaire distant dynamique : données potentiellement plus actuelles ; réseau, permissions, confiance et maintenance supplémentaires. Non retenu : VCR demeure hors ligne par défaut.
- Décision : date et provenance explicites ; ne pas confondre ouverture d'un lien, activité GitHub et preuve de résultats. Réexaminer avant tout essai ou ajout d'outil.
