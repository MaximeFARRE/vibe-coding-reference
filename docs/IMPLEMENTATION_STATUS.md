# État du prototype

Dernier lot : 6, catalogue SOURCES fonctionnel et compléments TOKENS après autorisation de consultation publique. Branche locale `feat/initial-publication` ; notes de recherche et lots 2–6 non poussés. Python 3.12.9 sur macOS ; `pytest`, `setuptools` et `wheel` absents de cet environnement. Installation editable, construction d'une wheel et Windows non vérifiés.

Fonctionnalités : START cadre une idée ; RESCUE réalise un audit passif ; IMPROVE propose des pistes supervisées ; TOKENS accepte une trace VCR ou une réponse API individuelle OpenAI/Anthropic sélectionnée ; SOURCES filtre neuf fiches locales par thème. VCR ne contacte aucun service et n'installe rien. La consultation réseau de sources publiques par les agents est désormais autorisée ; aucune donnée privée n'a été envoyée pour cette recherche.

Vérification exécutée : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 57 tests réussis. Démonstrations : `python3 -m vcr sources --topic tokens` retourne quatre fiches ; `python3 -m vcr tokens --format anthropic-messages --from ...` sur fixture indique une entrée calculée de 130 et un quota indisponible. Test d'une ressource de catalogue dans un paquet ZIP artificiel ; ce n'est pas un test d'installation ou de wheel. Pas de données personnelles ni benchmark de performance/tokens.

Sources : neuf liens officiels et deux liens scientifiques ouverts le 2026-11-14 ; licences des huit dépôts et métadonnées publiques de maintenance consultées. Ces contrôles ne prouvent ni sécurité ni efficacité ; toutes les évaluations de preuve restent `unverified`. Version, compatibilité et retrait doivent être vérifiés avant essai. Aucune installation tierce effectuée.

Limites TOKENS : les imports API ne couvrent qu'une réponse individuelle explicitement choisie, pas les journaux natifs de session Codex ou Claude Code ; pas d'import automatique d'historiques. Les compteurs sont déclaratifs, sans facture ni quota déduit ; les champs absents restent indisponibles. START stocke les réponses en clair ; RESCUE vérifie partiellement les schémas et monorepos ; IMPROVE utilise des règles explicites sans prouver une cause commune. Pas de validation d'ergonomie externe, HTML ni tri automatique.

Cas du backlog : T001–T015 couverts ; T007 simulé et T013 testé seulement sur macOS avec espaces. Prochain lot : épreuve de vérité et préparation GitHub (lot 7). Licence MIT choisie par le propriétaire.
