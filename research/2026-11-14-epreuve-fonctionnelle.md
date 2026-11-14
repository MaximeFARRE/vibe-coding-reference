# Épreuve fonctionnelle et préparation GitHub

- Date : 2026-11-14 ; statut : ouvert jusqu'à vérification de la CI distante.
- Question : le parcours local est-il reproductible et que reste-t-il à vérifier avant diffusion ?
- Sources : [backlog lot 7](../plans/03_BACKLOG_ET_LIVRAISON.md), [parcours](../tests/test_journey.py), [CI](../.github/workflows/ci.yml), [état d'avancement](../docs/IMPLEMENTATION_STATUS.md).

## Résultats

- **Confirmé sur fixture** : le parcours START → deux RESCUE → IMPROVE → TOKENS → SOURCES fonctionne et préserve les fichiers et le statut Git du projet fictif. Le test bloque les sockets Python ; il ne constitue pas une preuve générale d'isolation réseau du système.
- **Confirmé** : le plafond d'inventaire pouvait masquer une collecte tronquée ; il est désormais signalé `not_checked`, avec test de non-régression.
- **Confirmé sur macOS/Python 3.12** : `pip install .`, la CLI et la ressource catalogue, puis `pip uninstall`, ont fonctionné dans un environnement virtuel temporaire. Une wheel distincte a également été construite et installée. Des dépendances de construction ont été téléchargées uniquement dans l'environnement temporaire.
- **Confirmé localement** : les commandes d'exemple du README fonctionnent sur un projet artificiel ; les 4 combinaisons de CI sont syntaxiquement décrites et les modèles d'issues possèdent les champs attendus.
- **Non vérifié** : CI GitHub, Linux, Windows, installation editable, ergonomie par un utilisateur extérieur ; la validation JSON Schema de VCR reste partielle.

## Options et décision

- Tests `unittest` et vérification syntaxique par bibliothèque standard : aucune dépendance de test ; moins d'analyse statique qu'un outillage dédié.
- Ajouter des frameworks de lint et de tests : règles supplémentaires possibles ; installation et maintenance à justifier. Non retenu pour cette étape.
- Décision : CI légère proposée sur Python 3.11–3.13 sous Ubuntu et 3.12 sous macOS ; les résultats distants ne seront connus qu'après exécution sur GitHub. Pas de garantie de sécurité exhaustive.
