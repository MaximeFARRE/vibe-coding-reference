# État du prototype

Dernier lot : 5, TOKEN EFFICIENCY opérationnel avec réserves ci-dessous. Branche locale `feat/initial-publication` ; notes de recherche et lots 2–5 non poussés. Python 3.12.9 sur macOS ; `pytest` absent, tests `unittest` sans dépendance. Installation editable et Windows non vérifiés.

Fonctionnalités : START génère un cadrage ; RESCUE réalise un audit passif ; IMPROVE propose des pistes supervisées à partir de sources choisies ; TOKENS propose un diagnostic descriptif et importe volontairement le format documenté `vcr-token-trace-v1`. Les compteurs complets sont déclaratifs, les valeurs dérivées identifiées, les absences `unavailable` et le quota non déduit. Aucun accès réseau, historique privé automatique, test ou modification automatique du projet.

Vérification exécutée : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 45 tests réussis. Démonstration sur trace artificielle : `python3 -m vcr tokens --from ... --out ... --project ...` ; somme entrée/sortie 120, cache, coût et quota `unavailable`, trois fichiers de sortie vérifiés. Tests : sans trace, T009 sans coût/cache, champs partiels, cache inclus dans entrée, coûts déclarés et devises mixtes, doublons JSON, confidentialité des métadonnées fictives, protection du projet et précision décimale. Pas de données personnelles ni benchmark de performance/tokens.

Limites TOKENS : aucun format natif Codex/Claude pris en charge ; conversion manuelle explicite nécessaire et sémantique sous responsabilité de l'importateur. Les mesures/coûts déclarés ne sont pas vérifiés sur une facture ; les entrées cumulées ne sont pas du contexte unique. Pas de calcul de quota, de prix tarifaire, d'économie ou de réussite par coût. Les références renvoient aux enregistrements de la trace sélectionnée, dont le chemin n'est pas mémorisé ; la conserver. Si `--out` est utilisé sans `--project`, l'utilisateur choisit un chemin extérieur au projet.

Limites existantes : START stocke les réponses en clair ; RESCUE vérifie partiellement les schémas et les monorepos ; IMPROVE utilise des règles explicites et des sources déclaratives, sans prouver incidents ni causes communes. Pas de validation d'ergonomie externe, HTML ni tri automatique.

Cas du backlog : T001–T014 couverts ; T007 simulé et T013 testé seulement sur macOS avec espaces. T015 attend le catalogue. Prochain lot : catalogue des sources (lot 6), puis épreuve de vérité (lot 7). Licence MIT choisie par le propriétaire.
