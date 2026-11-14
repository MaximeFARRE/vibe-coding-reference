# 03 — Plan d'exécution Codex et backlog ordonné

**But :** un premier prototype suffisamment complet pour être utilisé, sans demander à Codex de construire une usine à gaz dans une unique réponse. Chaque lot doit produire une fonctionnalité utilisable, une validation reproductible, une note de passation et une liste d'incertitudes.

## 0. Ordre de priorité et règle de pilotage

**Priorité P0.1 : RESCUE bout en bout**, puis START, IMPROVE, TOKENS et catalogue. Le choix répond au besoin le plus différenciant du projet : rendre visibles des problèmes avec preuves et solutions. L'utilisateur non-développeur n'est jamais obligé de lire des tracebacks pour interpréter un rapport.

**Aucune estimation ferme de coûts en tokens** n'est promise. Le système lui-même ne doit pas appeler un LLM externe. Les efforts de vérification dans ce backlog sont des **tests fonctionnels d'un logiciel**, non des benchmarks comparatifs sur performances de modèles/architectures.

## Lot 0 — Préflight, décisions techniques et socle sain

**Tâches**

- Lire `README_START_HERE.md`, `docs/01_VISION_ET_DECISIONS.md` et `docs/02_ARCHITECTURE_ET_CONTRATS.md` ; pointer vers les autres docs seulement si nécessaire.
- `git status`, versions Python/OS, fichiers existants ; préserver toute modification.
- Créer un `README.md`, `AGENTS.md` court et `pyproject.toml` cohérent avec un paquet `src/` ; choisir commandes simples test/lint ; `pytest` comme dépendance dev.
- Mettre en place `python -m vcr --help` et `python -m vcr` affichant un menu accessible. Ne pas ajouter une TUI avec nombreuses dépendances.
- Créer un journal `docs/IMPLEMENTATION_STATUS.md` avec lots, décisions/écarts, commandes vérifiées et risques restants.
- Respecter `.gitignore` pour rapports, secrets, caches et fixtures générées.

**Acceptation** : le projet s'installe localement selon README, le menu s'ouvre sans connexion réseau, les tests de socle passent et `AGENTS.md` ne contient pas la bibliographie intégrale.

## Lot 1 — RESCUE vertical slice (exécutable et sûr)

**Tâches**

1. Créer des types `Run`, `Finding`, `Evidence`, `CheckResult` et sérialisation JSON. La V0.1 du format est dans `schemas/`.
2. Collecteurs passifs : `git status`, `HEAD` si disponible ; inventaire filtré ; manifests `package.json`, `pyproject.toml`, `requirements.txt`, lockfiles ; scripts de test/lint/build connus mais **non exécutés**.
3. Détecter les familles TS/JS/Python/générique sans prétendre reconnaître toutes les stacks.
4. Au minimum **six vérifications fonctionnelles** dans les fixtures : (a) dépôt Git sale ; (b) scripts de tests absents / non vérifiés ; (c) fichiers ignorés ; (d) dépendances manifestes répertoriées sans appeler des audits réseau ; (e) documentation d'architecture absente = info ; (f) présence potentielle de secrets => redaction et vérification, pas de clé reproduite.
5. Gérer les limites : absence Git, dépôt vide, permission refusée, projet monorepo, échec de commande ; les différencier de « tout va bien ».
6. Générer `run.json` + `report.md` et un prompt ciblé `ASK_CODEX_TO_REVIEW.md` pour interprétation approfondie, sans auto-appel modèle.
7. Ne rien écrire dans le dépôt cible ; sortir dans `--out` ; supprimer toute journalisation de secrets.
8. Proposer KEEP/REFACTOR/PARTIAL REBUILD/REBUILD seulement lorsque l'analyse est suffisamment étayée ; au stade purement statique, accepter `verdict: inconclusive`.

**Acceptation scénarios**

- Dépôt exemple TS : `vcr rescue --repo ...` donne rapport Markdown et JSON lisibles.
- Dépôt exemple Python : idem ; pas d'erreur sur un `pyproject` absent.
- Dépôt avec `node_modules`, `.next`, `.venv`, gros médias : exclus ; signale les exclusions.
- Dépôt contenant `.env` sensible : ne reproduit pas la valeur, ne l'envoie jamais au modèle. Un `.env.example` avec valeur fictive n'est pas déclaré secret avéré.
- Dépôt « propre » : peut sortir zéro finding important, pas de remplissage fictif.
- Aucune modification du dépôt cible (`git diff`, `git status`, empreinte des fichiers) après un audit passif. **Cette vérification doit être faite dans les tests fixtures, pas sur données privées**.

**Résultat utilisateur** : preuves concrètes + limites, lecture accessible à un non-développeur. Ne pas présenter un « audit sécurité exhaustif » : ce serait faux.

## Lot 2 — Preuves, normalisation et rapport orienté décisions

**Tâches**

- Validation de champs/énumérations et liens de preuves ; tolérance aux constats partiels avec messages d'erreur explicites ; éviter les gros framework de validation non nécessaires.
- Déduplication seulement si même cause, même emplacement et même règle, pas par simple similarité de texte.
- Ajouter `confidence`, `status` et `origin` dans le rendu ; priorité par **impact × confiance × réversibilité** expliquée en prose, pas score universel.
- Format « décision » pour chaque problème : problème, preuve, impact, solution A/B, coûts/risques, ce qu'il faut préserver, comment vérifier, humain doit-il approuver ?
- Générer éventuellement un `report.html` **statique**, accessible localement sans CDN ni JS tiers. Si cela complique beaucoup le prototype, Markdown d'abord.
- Liens locaux fiables (fichiers, lignes) si possibles ; si impossible, afficher chemin et ligne en texte.
- Modèle des retours utilisateur : `accepted`, `rejected`, `false_positive`, `deferred` ; stocké dans **le dossier de rapport**, pas dans les fichiers source.

**Acceptation** : un novice peut choisir un problème, lire une explication et copier un ordre de travail ; un expert peut inspecter les preuves, le code de règle et les limites.

## Lot 3 — START guidé (peu de questions, bons garde-fous)

**Tâches**

- Mode interactif, questions minimales : type de produit, accès public/local, utilisateurs, données sensibles, persistance, SEO/interactivité, contraintes Python, budget/maintenance. Réutiliser les réponses antérieures sans répéter.
- Séparer les propositions de langage, framework, architecture, infra, BDD.
- Cas conditionnels : site statique simple, app web full-stack, CRUD administratif, backend Python analytique, outil local, application à forte interactivité.
- Sortir `project-brief.md`, `acceptance-criteria.md`, `stack-options.md` et `START_PROMPT_FOR_CODEX.md` ; aucun déploiement, aucune config de comptes cloud.
- Ne pas présenter un « meilleur framework pour les agents » sans preuve comparative.

**Acceptation** : une idée vague devient une spécification compréhensible avec critères « quand on clique X, on observe Y » et 1–3 propositions de stack avec conditions et coûts d'exploitation.

## Lot 4 — IMPROVE supervisé (fonction phare)

**Tâches**

- Prendre un ou plusieurs `run.json`, une note de passation ou un log volontairement importé ; identifier répétitions de problèmes **vraiment présents**.
- Proposer des `ImprovementProposal` : `scope` (`agent_context`, `navigation`, `testing`, `architecture`, `workflow`, `token_efficiency`), source, cause supposée, solution A/B, risque, effort de maintenance, statut d'approbation.
- Cas prioritaires : erreurs répétées faute de tests ; absence de carte des fonctionnalités ; instructions AGENTS trompeuses ; modules difficiles à localiser ; gros retours d'outils ; conflits de conventions ; plugins inutilisés.
- Ne pas créer `AGENTS.md` automatiquement ; proposer un **diff ou texte à insérer**, puis demander validation humaine. Pas d'auto-optimiseur du harness.
- Garder un registre local par projet, possibilité de marquer faux positif ou obsolète ; horodatage et condition de réévaluation.

**Acceptation** : depuis 2 rapports fixtures montrant le même type d'échec, IMPROVE produit une proposition pertinente avec références aux 2 occurrences ; depuis 1 seul rapport, il évite d'inventer une récurrence.

## Lot 5 — TOKEN EFFICIENCY lisible et prudent

**Tâches**

- Mode diagnostique sans chiffres : checklist de sources de gaspillage, sélection de 3 recommandations immédiates, 3 conditionnelles maximum.
- Mode import des traces si format connu : parser documenté avec champs optionnels (modèle, entrée, sortie, cache read/write, coûts fournis, outils, sessions). Ne pas deviner les champs.
- Différencier `measured`, `estimated`, `unavailable`. Ne pas inférer les quotas ChatGPT/Codex à partir d'une facture API.
- Identifier les grands volumes d'entrées cachées, contexte cumulé, outils peu utilisés **si disponibles dans les journaux**, commandes longues, sessions multi-sujets, répétitions de recherche.
- Rapporter des leviers : sessions plus ciblées, recherche localisée, sorties courtes mais conservant preuves, outils désactivables, tests par paliers. Cache tarifaire : référencer fournisseur et date, ne pas figer des prix.

**Acceptation** : un journal sans coûts n'affiche jamais « € économisés » ; un journal sans cache n'affiche jamais « cache = 90% » ; la fonction marche quand aucune trace n'est fournie (diagnostic descriptif explicite).

## Lot 6 — Catalogue et guide d'intégration des outils externes

**Tâches**
