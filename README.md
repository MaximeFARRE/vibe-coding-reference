# Vibe Coding Reference — prototype local

START aide à cadrer une idée et propose des options techniques conditionnelles. RESCUE inspecte passivement un dossier et produit un rapport en français, un fichier JSON et un prompt de revue. IMPROVE propose des pistes à partir de sources choisies. Aucun ne lance de test du projet, ne contacte de service ou ne modifie le projet analysé. Python 3.11 ou supérieur est requis. TOKENS et SOURCES ne sont pas encore disponibles.

> **Prototype en cours de développement.** L'analyse est partielle et ne remplace ni les tests du projet ni une revue de sécurité.

**English:** VCR is a local-first prototype for project scoping, passive repository inspection and supervised improvement proposals. START, RESCUE and IMPROVE generate French documents locally without an API. Other workflows are planned.

Les recherches et décisions sont conservées dans les [notes destinées aux agents](research/README.md), avec leurs sources et limites.

## Démarrage sans installation

Dans ce dossier, sur macOS ou Linux :

```sh
export PYTHONPATH="$PWD/src"
python3 -m vcr --help
python3 -m vcr
python3 -m vcr start --interactive --out "/chemin/vers/nouveau-cadrage"
python3 -m vcr rescue --repo "/chemin/du/projet" --out "/chemin/vers/nouveau-rapport"
```

Sous Windows PowerShell, remplacer la première ligne par `$env:PYTHONPATH = "$PWD/src"` et utiliser `python` si nécessaire. Il est aussi possible d'installer le paquet localement avec `python -m pip install --no-build-isolation -e .` si `pip` et les outils de construction sont déjà disponibles ; cette installation n'a pas été vérifiée dans cette session. Aucun téléchargement n'est nécessaire pour l'utilisation avec `PYTHONPATH`.

## Cadrer une idée avec START

Le questionnaire demande le besoin, une action et son résultat visible, les utilisateurs, données et contraintes. Une réponse vide indique « à préciser ». Il produit un brief, des critères à valider, des options de stack et un prompt Codex, ainsi que `answers.json` pour reprendre les réponses. Aucune infrastructure ni compte n'est créé.

Pour reprendre un cadrage dans un **nouveau** dossier :

```sh
python3 -m vcr start --interactive --from "/chemin/vers/nouveau-cadrage/answers.json" --out "/chemin/vers/autre-cadrage"
```

Les réponses déjà enregistrées, y compris « à préciser », ne sont pas redemandées. Pour les changer, recommencer sans `--from`. Les documents contiennent vos réponses en clair : ne saisissez pas de secret ni de donnée personnelle et vérifiez-les avant partage. Les choix de stack et les critères restent des hypothèses à confirmer avec le propriétaire ; ils ne remplacent pas une analyse de sécurité ou de faisabilité.

## Analyser un projet avec RESCUE

Le dossier `--out` doit être nouveau, extérieur au projet, et ne pas contenir le projet. Ouvrir `report.md` ; `run.json` contient les mêmes constats structurés et `ASK_CODEX_TO_REVIEW.md` un prompt facultatif. Pour supprimer l'outil utilisé sans installation, supprimer son dossier et les rapports créés séparément. Si le paquet a été installé, utiliser aussi `python -m pip uninstall vibe-coding-reference`.

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

## Ce qui est examiné

Inventaire limité, filtres de dossiers, règles Git ignore lorsque Git fonctionne, statut et HEAD Git, manifestes courants, indices de scripts test/lint/build, noms de documentation d'architecture et fichiers `.env` non exclus. Les commandes et valeurs de manifestes ne sont pas recopiées. Les fichiers `.env` ne sont jamais lus ; leur présence n'établit pas qu'un secret existe. Les fichiers ignorés ne sont pas inspectés. Les dépendances sont comptées partiellement, sans analyse de vulnérabilités.

Un constat `confirmed` correspond à un fait observé ; `suspected` demande vérification. Les contrôles `not_checked` n'ont pas été établis ; `not_applicable` signifie non applicable. L'absence d'alerte ne prouve ni sécurité ni bon fonctionnement. Le verdict reste inconclusif. L'analyse ne couvre ni le métier ni l'exécution. Les noms et chemins du dossier ciblé, le hash Git et les observations figurent dans les rapports : vérifiez-les avant partage. Ne copiez pas de données sensibles dans un agent sans les examiner.

Les champs et énumérations produits sont vérifiés avant rendu ; une preuve sans localisation valide entraîne un avertissement et une confiance diminuée. Cette validation interne ne remplace pas un validateur JSON Schema complet. Un tri automatique par priorité et un rapport HTML ne sont pas fournis.

L'inventaire exclut les liens symboliques et les fichiers de plus de 1 Mio ; il est limité à 10 000 fichiers. Un dépôt modifié simultanément peut changer pendant l'analyse : ne pas auditer une arborescence contrôlée activement par un tiers hostile. Les erreurs de lecture et les règles Git non disponibles sont indiquées. Les règles de fichiers ignorés ne sont pas évaluées hors Git ; plusieurs manifestes sont relevés, sans interprétation complète des monorepos.

## Tests locaux

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Les tests créent des projets artificiels temporaires et ne nécessitent ni réseau ni données privées. `pytest` est proposé en dépendance de développement facultative, mais n'est pas nécessaire à cette commande. Voir [l'état d'avancement](docs/IMPLEMENTATION_STATUS.md) pour les cas couverts et les limites.

## Licence

Ce projet est distribué sous [licence MIT](LICENSE).
