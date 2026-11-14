# Validation des preuves et rapport de décision

- Date : 2026-11-14 ; statut : décidé pour le lot 2.
- Question : rendre les constats vérifiables et permettre une décision sans modifier le projet audité.
- Sources : [backlog, lot 2](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md) ; [schéma Finding](../schemas/finding.schema.json) ; [normalisation](../src/vcr/normalize.py) ; [tests](../tests/test_normalize.py) et [parcours de décision](../tests/test_decisions.py).

## Résultats

- **Confirmé par tests fonctionnels** : une ligne inexistante dégrade le statut et la confiance ; les doublons sont écartés seulement lorsque règle, cause et localisation concordent. Les décisions utilisateur sont enregistrées hors cible pour les fixtures testées.
- **Limite** : la validation interne couvre les champs utilisés par le prototype ; les tests contrôlent un sous-ensemble des mots-clés des schémas, pas une conformité JSON Schema exhaustive. Les fichiers d'environnement ne sont pas lus pour vérifier des lignes.
- **Non vérifié** : Windows et comportement face à un acteur modifiant simultanément les fichiers et liens pendant l'opération.

## Options et décision

- Validation Python simple : aucune dépendance nouvelle, règles lisibles et contrôle ciblé ; couverture JSON Schema incomplète et maintenance manuelle des règles.
- Validateur JSON Schema complet : contrat standard plus large ; dépendance supplémentaire à installer et à maintenir. Non retenu pour ce lot local sans installation.
- Rapport Markdown : inspectable sans infrastructure ; navigation et présentation variables selon le lecteur. HTML statique non nécessaire à ce stade.
- Décision utilisateur dans le dossier de rapport : la cible reste intacte ; un déplacement du rapport nécessite de conserver `run.json` et `feedback.json` ensemble.

## Suite

- Envisager une validation JSON Schema complète lors du lot de qualité si une dépendance devient acceptable ; tester sur Windows et poursuivre le lot 3 START.
