# Épreuve fonctionnelle et préparation GitHub

- Date : 2026-11-14 ; statut : décidé, CI distante vérifiée sur le commit indiqué ci-dessous.
- Question : le parcours local est-il reproductible et que reste-t-il à vérifier avant diffusion ?
- Sources : [backlog lot 7](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [parcours](../tests/test_journey.py), [CI](../.github/workflows/ci.yml), [état d'avancement](../docs/IMPLEMENTATION_STATUS.md).

## Résultats

- **Confirmé sur fixture** : le parcours START → deux RESCUE → IMPROVE → TOKENS → SOURCES fonctionne et préserve les fichiers et le statut Git du projet fictif. Le test bloque les sockets Python ; il ne constitue pas une preuve générale d'isolation réseau du système.
- **Confirmé** : le plafond d'inventaire pouvait masquer une collecte tronquée ; il est désormais signalé `not_checked`, avec test de non-régression.
- **Confirmé sur macOS/Python 3.12** : `pip install .`, la CLI et la ressource catalogue, puis `pip uninstall`, ont fonctionné dans un environnement virtuel temporaire. Une wheel distincte a également été construite et installée. Des dépendances de construction ont été téléchargées uniquement dans l'environnement temporaire.
- **Confirmé localement** : les commandes d'exemple du README fonctionnent sur un projet artificiel ; les 4 combinaisons de CI sont syntaxiquement décrites et les modèles d'issues possèdent les champs attendus.
- **Confirmé en CI** : [exécution 43602137084](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602137084) réussie sur le commit `200c0763ded987241c7dbed3da1399f27c481f00` pour Ubuntu/Python 3.11–3.13 et macOS/Python 3.12.
- **Non vérifié** : Windows, installation editable, ergonomie par un utilisateur extérieur ; la validation JSON Schema de VCR reste partielle.

## Options et décision

- Tests `unittest` et vérification syntaxique par bibliothèque standard : aucune dépendance de test ; moins d'analyse statique qu'un outillage dédié.
- Ajouter des frameworks de lint et de tests : règles supplémentaires possibles ; installation et maintenance à justifier. Non retenu pour cette étape.
- Décision : CI légère sur Python 3.11–3.13 sous Ubuntu et 3.12 sous macOS ; aucune garantie de sécurité exhaustive.
