# Vibe Coding Reference

[![English](https://img.shields.io/badge/language-English-3776AB)](README.md)

VCR aide à cadrer et examiner un projet quand on développe avec des agents existants comme Codex ou Claude Code. Ce prototype Python fonctionne localement, sans clé API et sans créer de nouvel agent ou modèle. Ses rapports sont en français.

> **Prototype :** les résultats sont partiels et demandent une validation humaine. RESCUE ne garantit pas qu'un projet est sûr ou exempt de bugs ; il ne remplace ni ses tests ni une revue de sécurité.

| Parcours | Pour quoi faire ? | Résultat ou limite principale |
|---|---|---|
| **START** | Transformer une idée en cadrage | Brief, critères et pistes de stack à valider |
| **RESCUE** | Inspecter passivement un projet | Rapport avec preuves et limites, sans modifier la cible |
| **IMPROVE** | Examiner des rapports ou notes choisis | Pistes supervisées, sans appliquer de changement |
| **TOKENS** | Examiner le contexte ou une trace fournie volontairement | Diagnostic descriptif, sans calcul de quota ou d'économies |
| **SOURCES** | Consulter des ressources par thème | Catalogue local, sans installation automatique |

Les [notes de recherche destinées aux agents](research/README.md) conservent les observations, sources, décisions et limites du projet.

## Démarrage sans installation

Il faut **Python 3.11 ou supérieur** et Git pour le clonage. Sur macOS ou Linux, dans un terminal :

```sh
git clone https://github.com/MaximeFARRE/vibe-coding-reference.git
cd vibe-coding-reference
python3 --version
export PYTHONPATH="$PWD/src"
python3 -m vcr --help
python3 -m vcr
```

Le menu permet de découvrir les commandes. VCR ne contacte aucun service pendant son utilisation ; le clonage, lui, nécessite une connexion. Aucun paquet n'est nécessaire pour cette utilisation avec `PYTHONPATH`.

Sous Windows PowerShell, remplacer l'export par `$env:PYTHONPATH = "$PWD/src"` et utiliser `python` si nécessaire ; **Windows n'a pas été vérifié**.

Pour un premier essai sans projet personnel, suivre l'exemple fictif ci-dessous. Pour une idée personnelle, utiliser `python3 -m vcr start --interactive --out "/chemin/vers/nouveau-cadrage"` ; pour un projet existant, utiliser `python3 -m vcr rescue --repo "/chemin/du/projet" --out "/chemin/vers/nouveau-rapport"`. Les dossiers de sortie doivent être nouveaux ; pour RESCUE et IMPROVE, ils doivent aussi être extérieurs au projet.

### Essayer sur un projet fictif

Sur macOS ou Linux, après l'`export PYTHONPATH` ci-dessus :

```sh
VCR_DEMO_DIR="$(mktemp -d)"
mkdir "$VCR_DEMO_DIR/projet"
printf '{"dependencies":{"next":"fixture"}}\n' > "$VCR_DEMO_DIR/projet/package.json"
python3 -m vcr rescue --repo "$VCR_DEMO_DIR/projet" --out "$VCR_DEMO_DIR/rapport-1"
python3 -m vcr rescue --repo "$VCR_DEMO_DIR/projet" --out "$VCR_DEMO_DIR/rapport-2"
python3 -m vcr improve --project "$VCR_DEMO_DIR/projet" --from "$VCR_DEMO_DIR/rapport-1/run.json" --from "$VCR_DEMO_DIR/rapport-2/run.json" --out "$VCR_DEMO_DIR/ameliorations"
python3 -m vcr tokens
python3 -m vcr sources --topic tokens
printf 'Rapports locaux : %s\n' "$VCR_DEMO_DIR"
```

Ouvrir `rapport-1/report.md` puis `ameliorations/report.md` dans le dossier affiché. Le projet et les rapports sont fictifs ; le dossier temporaire reste disponible jusqu'à sa suppression par l'utilisateur. Pour essayer START, lancer `python3 -m vcr start --interactive --out "$VCR_DEMO_DIR/cadrage"` et répondre avec des données fictives.

### Installer ou retirer le paquet

L'utilisation sans installation ci-dessus est la plus courte. Pour installer dans un environnement virtuel dédié sur macOS/Linux : `python3 -m venv .venv`, puis `. .venv/bin/activate` et `python -m pip install .`. La préparation du paquet peut télécharger les outils de construction Python ; installation et désinstallation ont été vérifiées dans un environnement temporaire sous macOS/Python 3.12. L'installation editable et Windows restent non vérifiés. Une fois installé, `vcr --help` fonctionne depuis l'environnement activé.

Pour retirer une installation, activer le même environnement puis exécuter `python -m pip uninstall vibe-coding-reference`. Supprimer éventuellement l'environnement virtuel uniquement s'il est dédié à VCR ; les rapports créés ailleurs sont à supprimer séparément si souhaité. Sans installation, supprimer le dossier VCR et ses rapports séparés suffit.

## Cadrer une idée avec START

Le questionnaire demande le besoin, une action et son résultat visible, les utilisateurs, données et contraintes. Une réponse vide indique « à préciser ». Il produit un brief, des critères à valider, des options de stack et un prompt Codex, ainsi que `answers.json` pour reprendre les réponses. Aucune infrastructure ni compte n'est créé.

Pour reprendre un cadrage dans un **nouveau** dossier :

```sh
python3 -m vcr start --interactive --from "/chemin/vers/nouveau-cadrage/answers.json" --out "/chemin/vers/autre-cadrage"
```

Les réponses déjà enregistrées, y compris « à préciser », ne sont pas redemandées. Pour les changer, recommencer sans `--from`. Les documents contiennent vos réponses en clair : ne saisissez pas de secret ni de donnée personnelle et vérifiez-les avant partage. Les choix de stack et les critères restent des hypothèses à confirmer avec le propriétaire ; ils ne remplacent pas une analyse de sécurité ou de faisabilité.

## Analyser un projet avec RESCUE

Le dossier `--out` doit être nouveau, extérieur au projet, et ne pas contenir le projet. Ouvrir `report.md` ; `run.json` contient les mêmes constats structurés et `ASK_CODEX_TO_REVIEW.md` un prompt facultatif.

Chaque constat présente ses preuves, son niveau de confiance, deux options et un ordre de revue à copier. Pour enregistrer une décision, utiliser l'identifiant affiché dans le rapport :

```sh
python3 -m vcr feedback --report "/chemin/vers/nouveau-rapport" --finding tests-unknown --decision deferred
```

Les décisions possibles sont `accepted` (accepté), `rejected` (rejeté), `false_positive` (faux positif) et `deferred` (reporté). Le dernier choix par constat est stocké dans `feedback.json` à côté du rapport, sans modifier le projet audité. Cette décision ne lance aucune correction. Les liens vers des fichiers ordinaires sont locaux ; les fichiers sensibles sont affichés sans lien cliquable.

## Examiner des améliorations avec IMPROVE

Sélectionner explicitement des rapports du **même projet** et un nouveau dossier extérieur à celui-ci :

```sh
python3 -m vcr improve --project "/chemin/projet" --from "/chemin/rapport-1/run.json" --from "/chemin/rapport-2/run.json" --out "/chemin/nouvel-improve"
```

Le rapport distingue une observation isolée de deux observations d'une même règle. Deux rapports peuvent décrire le même état : ils ne prouvent pas deux incidents ni une cause commune. Les statuts et preuves sont ceux déclarés par les sources, à vérifier ; les constats RESCUE marqués `false_positive` ou `rejected` dans leur `feedback.json` sont ignorés. `report.md`, `proposals.json` et `registry.json` restent dans le dossier de sortie. Aucune modification n'est appliquée.

Pour enregistrer une décision et reprendre le registre plus tard :

```sh
python3 -m vcr improve-feedback --registry "/chemin/nouvel-improve/registry.json" --proposal tests-unknown --decision false_positive
python3 -m vcr improve --project "/chemin/projet" --registry "/chemin/nouvel-improve/registry.json" --from "/chemin/rapport-3/run.json" --out "/chemin/improve-suivant"
```

Décisions : `accepted`, `rejected`, `deferred`, `false_positive`, `obsolete`. La décision modifie seulement le registre sélectionné ; pour actualiser le Markdown et les propositions, relancer `improve` avec ce registre et un nouveau dossier. Lorsqu'un rapport est réimporté, son feedback actuel peut retirer du registre une observation rejetée ; les rapports non réimportés ne sont pas revérifiés automatiquement. Les chemins des sources figurent dans les sorties : les examiner avant partage.

Les options répétables `--note` et `--log` importent des fichiers texte choisis volontairement. Le texte libre n'est pas interprété ni recopié. Pour signaler explicitement une observation, placer seule sur une ligne, par exemple, `VCR_OBSERVATION test-failure confirmed` ou `VCR_OBSERVATION agents-conflict suspected` ; les statuts sont des déclarations de l'utilisateur, non des vérifications automatiques. Règles reconnues : `tests-unknown`, `test-failure`, `architecture-doc`, `git-dirty`, `env-present`, `agents-conflict`, `navigation-difficulty`, `large-tool-output`, `convention-conflict`, `unused-plugin`. Une même note copiée ne compte qu'une fois. Ne pas importer d'historique privé sans choix explicite ; les fichiers sont limités à 1 Mio et les liens symboliques directs refusés.

