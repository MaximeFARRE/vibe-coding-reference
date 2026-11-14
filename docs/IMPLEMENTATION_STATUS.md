# État du prototype

Dernier lot : 7, vérifications locales et CI GitHub réalisées sur `feat/initial-publication` ; branche principale non fusionnée. Python 3.12.9 sur macOS ; Linux vérifié en CI, Windows non vérifié. Licence MIT choisie par le propriétaire.

Fonctionnalités : START cadre une idée ; RESCUE réalise un audit passif ; IMPROVE propose des pistes supervisées ; TOKENS accepte une trace VCR ou une réponse API individuelle OpenAI/Anthropic sélectionnée ; SOURCES filtre neuf fiches locales par thème. VCR ne contacte aucun service et n'installe rien. La consultation réseau de sources publiques par les agents est autorisée.

Vérification : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis sur macOS/Python 3.12. Vérification syntaxique par `ast.parse` et lecture YAML locale de la CI et des trois modèles d'issues. Le parcours complet sur fixture bloque les sockets Python, vérifie les sorties et préserve les fichiers et le statut Git ; les commandes d'exemple README ont été exécutées. Le plafond d'inventaire est désormais signalé incomplet lorsqu'il est atteint.

Installation : wheel construite et installée, puis `python -m pip install .` et `python -m pip uninstall vibe-coding-reference` vérifiés dans des environnements virtuels temporaires sur macOS/Python 3.12 ; CLI, catalogue embarqué et RESCUE testés sur fixture. Des dépendances de construction ont été téléchargées dans l'environnement temporaire ; aucun paquet système modifié. Installation editable et Windows non vérifiés.

CI : [exécution GitHub 43602137084](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602137084) réussie sur le commit `200c0763ded987241c7dbed3da1399f27c481f00` : Python 3.11–3.13 sur Ubuntu et 3.12 sur macOS, sans dépendance de test. Le YAML et les modèles d'issues ont aussi été lus localement. Pas de données personnelles ni benchmark de performance/tokens.

Limites : TOKENS ne lit pas les journaux natifs de session Codex/Claude Code ; les compteurs et coûts sont déclaratifs. Les neuf liens du catalogue et des métadonnées ont été consultés le 2026-11-14, sans audit de sécurité ni preuve générale d'efficacité. START stocke les réponses en clair ; RESCUE vérifie partiellement les schémas et monorepos ; IMPROVE n'établit pas de cause commune. Pas de validation d'ergonomie par une personne extérieure, HTML ni tri automatique.

Cas du backlog : T001–T015 couverts ; T007 simulé et T013 testé avec espaces sur macOS et Ubuntu, pas Windows. Prochaine étape : revue de la branche et décision de fusion ; ensuite, prioriser les limites réelles selon les retours utilisateurs.

## Présentation GitHub — 14 novembre 2026

README réorganisé autour des cinq parcours, du statut de prototype et d'un clonage explicite de `feat/initial-publication` ; le dossier de lancement initial est signalé comme historique. Le README est préparé pour la branche par défaut après fusion.

Vérifications de ce lot sur macOS/Python 3.12.9 : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis. L'exemple README RESCUE (deux rapports), IMPROVE, `tokens` et `sources --topic tokens` a été exécuté sur un projet fictif temporaire ; les deux rapports Markdown attendus existent. `git diff --check` : aucune erreur. Le clone présenté et le parcours interactif START n'ont pas été rejoués dans ce lot ; Windows et l'installation editable restent non vérifiés.

GitHub consulté en lecture seule : `main` est la branche par défaut ; `feat/initial-publication` est 91 commits en avance et 0 en retard au moment de la consultation. La CI [43602244697](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602244697), sur `c41ce65`, a réussi ses quatre configurations. Ces observations ont précédé les changements de publication ci-dessous.

## Préparation de la publication

README bilingue d'accueil avec badges CI, Python et licence, schéma des parcours et guide français détaillé. Ajout de consignes de contribution, code de conduite, modèle de pull request et de signalement de bug, journal des changements et feuille de route. Les retours de personnes extérieures, Windows et l'installation editable restent à vérifier.

Vérification locale : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis sur macOS/Python 3.12.9. La [pull request #1](https://github.com/MaximeFARRE/vibe-coding-reference/pull/1) a été fusionnée après réussite de ses quatre configurations CI ; le signalement privé des vulnérabilités est activé. Prochaines étapes : première préversion, essais par des personnes extérieures et traitement des retours.

## README anglais et français

Le README principal est intégralement en anglais ; le guide français est conservé dans `README.fr.md` et relié dans les deux sens. Les rapports et le menu de VCR restent en français. Les documents publics de contribution, sécurité, conduite, feuille de route et changelog sont également en anglais ; les documents historiques, techniques et notes de recherche restent en français.

Vérifications : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis sur macOS/Python 3.12.9 ; exemple fictif RESCUE, IMPROVE, TOKENS et SOURCES exécuté ; liens locaux des deux README vérifiés et `git diff --check` sans erreur. Traduction du reste de la documentation technique et essais par des lecteurs anglophones restent à faire.

## Nettoyage du dépôt

Retrait du brief initial fusionné, du prompt initial dupliqué et du manifeste SHA-256 du kit documentaire historique. Leurs copies locales sont conservées dans `.vcr-local-archive/`, ignoré par Git ; elles sont identiques aux fichiers de `origin/main` au moment du nettoyage. Les notes de recherche et leurs sources liées, le backlog, les consignes et le prompt de lancement référencé restent en place. Les fichiers retirés restent accessibles dans l'historique Git ; l'archive locale n'est pas distribuée aux nouveaux clones.

Vérifications sur macOS/Python 3.12.9 : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis ; comparaison `git show ... | cmp` des trois copies locales : identiques ; `git check-ignore` confirme l'exclusion ; `git diff origin/main --check` sans erreur. Prochaine étape : vérifier la CI de la pull request et les retours des utilisateurs ; ne pas supprimer les sources historiques référencées sans traiter leurs liens.

## Retrait du kit initial de construction

Retrait du README de lancement, du backlog de livraison initial, du prompt de bootstrap et des anciens documents de vision, d'architecture cible et de playbooks. Leurs copies sont dans `.vcr-local-archive/`, ignoré par Git et absent des nouveaux clones. Les notes de recherche restent en place ; leurs liens vers les documents retirés pointent désormais vers le commit GitHub `c8d94cb14c27270f430277034d4b280431001d3f` et demandent donc une connexion. Les notes et références de recherche, y compris les corrections et décisions historiques, sont conservées. AGENTS.md utilise les points d'entrée actuels.

Vérifications sur macOS/Python 3.12.9 : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 59 tests réussis ; les six copies locales correspondent aux fichiers de `origin/main` par `git show ... | cmp` ; `git diff origin/main --check` sans erreur. Prochaine étape : revue et CI avant intégration ; évaluer séparément les documents de recherche si leur organisation doit évoluer.

## Project Health Check — November 14, 2026

`python3 -m vcr check` reuses RESCUE's bounded inventory, script detection and passive Git commands. It offers text or JSON output, optional `--repo`, a non-executing `--full` mode and exclusive `--out` creation outside the target. The existing `Run` model and 0.1 schema now accept the `check` workflow and optional evidence, method, applicability and limitation fields. Existing RESCUE reports remain compatible. The new catalog is documentation, not runtime configuration.

Partial checks cover GIT-01, GIT-02, GIT-03, GIT-05, ENV-01, ENV-03, ENV-05, CODE-01, CODE-02, TEST-01, BUILD-01, CI-01, CTX-03 and SEC-01. They examine limited conventions and the filtered inventory. ENV-03 associates a Node manifest and lockfile in the same directory but does not validate their contents or compatibility. SEC-01 looks only for tracked `.env` names. ENV-05 checks example filenames without reading them; CODE-02 checks configuration filenames without executing a type checker. No check establishes security, CI success, secret absence, restoration or business correctness. DATA-02, DATA-06 and AGT-06 are not implemented. DATA-07 and DEP-01 are not in the check list; restoration and dependency vulnerabilities are listed as unverified limitations.

In `--full` mode, detected nonempty Node `lint`, `typecheck`, `test` and `build` scripts are marked `skipped`; they are not executed. Before output, internal validation checks IDs, statuses, optional fields and evidence types and paths, and requires evidence for conclusive check results. Invalid results produce exit code 2 without publishing JSON. This is not a complete JSON Schema validator. Evidence may omit nested paths, and applicability can remain uncertain. Ignored, excluded and oversized files are not examined; monorepo coverage is partial.

START does not create a project and RESCUE does not repair code, so final START and pre/post-repair RESCUE integration remain deferred. IMPROVE does not consume check outputs. There is no project-command runner or `--allow-project-commands` option. The checks are local deterministic rules: no AI, network, installation or target scripts are used.

Earlier local verification: 62 tests passed after the first slice, 65 after structured evidence, and 68 after validation. Python/Git and Node fixtures demonstrated README and Git detection, Node lockfile detection, and skipped test execution; fixture tests cover masking, evidence, separate subprojects and RESCUE compatibility. Windows and complete manifest interpretation remain unverified.

## Release preparation — November 14, 2026

The English README and changelog document the new passive `check` command and its limitations. The feature was tested on macOS/Python 3.12.9 with `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q`: 68 tests passed. No tag, push or release has been created. The project still contains French documentation, including historical references and research; translating and reviewing it is required before the requested English-only documentation is complete. The CLI and reports remain in French. The feature branch also contains earlier repository-cleanup commits and should be reviewed before merging.
