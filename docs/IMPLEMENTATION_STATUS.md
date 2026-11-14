# État du prototype

Dernier lot : 7, vérifications locales et préparation GitHub réalisées ; CI distante à exécuter. Branche `feat/initial-publication` ; lots 2–7 en attente de publication. Python 3.12.9 sur macOS ; Windows et Linux non vérifiés localement. Licence MIT choisie par le propriétaire.

Fonctionnalités : START cadre une idée ; RESCUE réalise un audit passif ; IMPROVE propose des pistes supervisées ; TOKENS accepte une trace VCR ou une réponse API individuelle OpenAI/Anthropic sélectionnée ; SOURCES filtre neuf fiches locales par thème. VCR ne contacte aucun service et n'installe rien. La consultation réseau de sources publiques par les agents est autorisée.

Vérification : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis sur macOS/Python 3.12. Vérification syntaxique par `ast.parse` et lecture YAML locale de la CI et des trois modèles d'issues. Le parcours complet sur fixture bloque les sockets Python, vérifie les sorties et préserve les fichiers et le statut Git ; les commandes d'exemple README ont été exécutées. Le plafond d'inventaire est désormais signalé incomplet lorsqu'il est atteint.

Installation : wheel construite et installée, puis `python -m pip install .` et `python -m pip uninstall vibe-coding-reference` vérifiés dans des environnements virtuels temporaires sur macOS/Python 3.12 ; CLI, catalogue embarqué et RESCUE testés sur fixture. Des dépendances de construction ont été téléchargées dans l'environnement temporaire ; aucun paquet système modifié. Installation editable et Windows non vérifiés.

CI : workflow GitHub préparé pour Python 3.11–3.13 sur Ubuntu et 3.12 sur macOS, sans dépendance de test. Son YAML a été lu localement ; aucune exécution GitHub vérifiée à ce stade, donc pas de CI déclarée verte. Pas de données personnelles ni benchmark de performance/tokens.

Limites : TOKENS ne lit pas les journaux natifs de session Codex/Claude Code ; les compteurs et coûts sont déclaratifs. Les neuf liens du catalogue et des métadonnées ont été consultés le 2026-11-14, sans audit de sécurité ni preuve générale d'efficacité. START stocke les réponses en clair ; RESCUE vérifie partiellement les schémas et monorepos ; IMPROVE n'établit pas de cause commune. Pas de validation d'ergonomie par une personne extérieure, HTML ni tri automatique.

Cas du backlog : T001–T015 couverts ; T007 simulé et T013 testé seulement sur macOS avec espaces. Prochaine étape : exécuter la CI distante et vérifier ses résultats ; ensuite, prioriser les limites réelles selon les retours utilisateurs.
