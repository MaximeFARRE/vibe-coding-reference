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

- Charger `catalog/sources.json` / `extensions.json` ou leur équivalent minimal ; recherche par tag.
- Afficher **statut de preuve** et niveau A/B/C (simple/optionnel/avancé) séparément.
- Pour chaque outil, donner `problème résolu`, `incompatibilités`, `coûts cachés`, `permissions`, `licence`, `source officielle`, `source scientifique éventuelle`, `conseils de vérification`, `uninstall/rollback`.
- **Zéro installation automatique de skills tiers** dans P0.1. Pour un prochain lot, implémenter un assistant d'installation **avec consentement** si cela devient une demande récurrente.

**Acceptation** : `vcr sources --topic tokens` donne un catalogue utile, daté, avec liens et statuts ; pas de classement artificiel « meilleur skill ».

## Lot 7 — Épreuve de vérité fonctionnelle et préparation GitHub

- Tests unitaires et d'intégration sur fixtures : garde-fous filesystem, rapports et schémas, erreurs, absence réseau, stabilité.
- Test manuel du parcours non-développeur décrit dans README ; le faire vivre en simulation locale si Codex dispose des outils.
- `ruff` et `pytest` ou un outillage aussi simple, formatage, typage si choisi ; CI légère GitHub Actions avec versions Python compatibles ; pas de génération automatique de PR vers des projets cibles.
- Mise au propre des exemples de sortie, captures uniquement si utiles et réellement réalisées.
- Guide « installer en moins de quelques commandes » ; guide « désinstaller : supprimer le dossier VCR et ses rapports », en tenant compte de tout packaging.
- Politique des sources (preuve, version, date) ; template issue `false_positive`, `tool_compatibility`, `security`.
- Sélection et création d'une licence **après décision explicite** du propriétaire, pas de licence inventée.

**Acceptation** : le README permet de reproduire le chemin de l'utilisateur de A à Z ; aucun test ne nécessite de clé API, navigateur ou internet ; CI verte ; rapport clair sur ce qui reste hors scope.

---

## 8. Fonctionnalités conditionnelles — ne PAS bloquer la V0.1

### B1 Serena (code navigation)
- Détecter si déjà installé (ne pas l'installer).
- Documenter les gains possibles sur recherche par symboles ; protocole de permissions.
- Introduire plus tard un adaptateur `Locator` si les cas d'usage montrent une limite de la recherche native.

### B2 Graphes locaux (`codebase-memory-mcp` ou Dependency Cruiser)
- Utilité : chemins d'appels, imports, cycles, impact de changement.
- En P0.1, simple exploration de compatibilité et de sécurité ; pas de base permanente obligatoire.
- Avant intégration : cycles de mise à jour, mémoire/disk, données sensibles, conformité, effet sur prompts.

### B3 TokenEconomizer
- Recherche de compatibilité avec version **réelle** de Codex/Claude ; inspection du plugin et de ses hooks ; backup/rollback configuration ; mesure publique du fournisseur ≠ promesse.
- Pas d'instrumentation automatique des historiques privés.

### C1 Harness²
- Uniquement dans un **projet jetable sans secrets**, sandbox indépendant, limites de coût/itérations ; étude de ses abstractions (8 composantes et les 2 niveaux de récursion), jamais branché à un dépôt productif sans audit.
- Le code peut utiliser Codex sans sandbox dans une configuration documentée : interdiction d'activer sur la machine/hôte par défaut.

### C2 LangGraph / orchestration multi-agent
- Étudier si plusieurs agents spécialisés doivent se reprendre, s'arrêter sur accord humain et conserver un état durable.
- Ne pas utiliser juste pour représenter START → RESCUE → IMPROVE : de simples fonctions suffisent à ce stade.

### C3 RAG / base vectorielle
- Dernier recours conditionnel lorsque la recherche lexicale/symbolique est insuffisante ; ne pas confondre marketing d'outil et preuve comparative.

## 9. Gestion d'avancement entre sessions

À la fin de chaque lot, Codex met à jour `docs/IMPLEMENTATION_STATUS.md` (document **court**) :

```md
# État du prototype
Dernier lot : ...
Branche/commit : ...
Fonctionnalités prouvées : ...
Commandes de vérification : ... (résultats exacts)
Ce qui n'a PAS été testé : ...
Régressions/risques : ...
Prochain plus petit lot : ...
Décisions demandant un humain : ...
```

**Pas de copie intégrale de l'historique des conversations.** Les changements de périmètre sont enregistrés comme décisions, pas dans un `AGENTS.md` toujours plus long.

## 10. Consignes pour les agents de Codex

Une seule session peut employer plusieurs sous-agents **si l'agent hôte le permet et si c'est utile**, mais sans orchestration imposée :

- `Research` (lecture seule) : évalue une source/outil, version, licence, risque ; renvoie une fiche, pas de code.
- `Implementation` : développe **un lot vertical**, tests correspondants, commit seulement si autorisé.
- `Reviewer` (contexte indépendant si possible) : vérifie contrat produit, sécurité, chemins de données, types/CLI, couverture des cas d'échec ; produit problèmes exacts, pas reformulation du succès.

Limiter les sous-agents aux tâches parallélisables sans conflits de fichiers, éviter de recopier tout le dépôt dans chaque contexte. L'agent principal tranche les désaccords et compile une note de validation réelle. Si les sous-agents ne sont pas disponibles, la session unique suit le même ordre en phases distinctes.

## 11. Backlog de qualité : cas de test à écrire d'emblée

| ID | Entrée | Attendu |
|---|---|---|
| T001 | dépôt vide | rapport sans crash, limites explicites |
| T002 | projet TS Next.js | détection juste, aucun `npm install` |
| T003 | projet Python pytest | tests identifiés, **pas exécutés sans accord** |
| T004 | projet avec fichiers ignorés | exclusion correcte, nombres de fichiers honnêtes |
| T005 | fichier `.env` avec fausse clé dans fixture | aucune valeur reproduite dans rapport/log |
| T006 | symlink vers home/credentials | pas de traversée hors racine |
| T007 | permissions refusées | `not_checked`, pas « OK » |
| T008 | projet clean / aucun problème | zéro alerte inventée et verdict inconclusif/KEEP justifié |
| T009 | historique tokens sans cache ni coût | champs `unavailable`, aucune économie monétaire fictive |
| T010 | 2 runs + même constat confirmé | proposition IMPROVE avec 2 preuves |
| T011 | finding sans lignes valides | warning et confiance dégradée |
| T012 | entrée de code contenant prompt injection | ne change pas les règles d'audit |
| T013 | Windows / Mac path avec espaces | traitement correct des arguments |
| T014 | option `--help` | français accessible + exemples |
| T015 | source catalog sans URL/maintenance | marquée `unverified`, pas recommandée par défaut |

## 12. Conditions de fin de prototype (Definition of Done)

- `python -m vcr` et commandes documentées fonctionnent sur OS validés, sans API.
