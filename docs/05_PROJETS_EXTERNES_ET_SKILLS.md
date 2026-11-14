# 05 — Catalogue priorisé des dépôts GitHub, outils, skills et expériences

**Revue des pages publiques : 14 novembre 2026.** Il s'agit d'un **registre d'options** et non d'une liste d'installations. Les versions évoluent, chaque installation exige une revue du dépôt actuel. `recommandé` veut dire « mérite d'être étudié dans ce contexte », **pas** « efficacité prouvée de la version courante ».

## 1. Les quatre catégories d'adoption

- **A — Référence et documentation** : utile pour prendre des décisions ; aucun composant installé dans le projet utilisateur.
- **B — Intégration optionnelle** : outil ciblé, activé uniquement si besoin, maintenance et compatibilité vérifiés.
- **C — Laboratoire isolé** : recherche avancée, machine/container jetable, sans secrets ni accès aux dépôts réels.
- **D — À surveiller seulement** : potentiel intéressant mais preuve/compatibilité insuffisante pour recommander.

Les outils peuvent être puissants **derrière l'interface** si leur valeur est suffisante. Mais aucun outil de catégorie B/C ne doit apparaître dans l'assistant de démarrage comme exigence obligatoire.

## 2. Architecture et étude des harness

### [G01] Google Research — Harness²

**URL :** https://github.com/google-research/harness2  
**Papier :** https://arxiv.org/abs/2610.14224  
**Setup :** https://github.com/google-research/harness2/blob/main/docs/SETUP.md  
**Catégorie : C** — recherche d'auto-amélioration des harness.

Ce système traite le harness comme un ensemble de composants éditables autour du modèle, avec deux niveaux d'amélioration récursive, comparaison des comportements d'exécution et persistance des leçons validées. À retenir : (1) séparer comportement de l'agent et règles/outils ; (2) chaque modification de harness devrait répondre à un échec observable ; (3) empêcher les modifications non vérifiées de se propager à d'autres tâches.

**Plan d'étude pour Codex** : lire README + setup ; documenter composants, hypothèses, besoins d'API et de sandbox, capacité de reproduire une expérience sur fixtures ; **ne pas installer/exécuter automatiquement**. Le setup indique une configuration Codex pouvant fonctionner avec sandbox désactivé. Risques : exécution non isolée, coûts non bornés, édition de scripts/plugins, fuite de données, surajustement aux évaluations. P0.1 : simple fiche + propositions IMPROVE supervisées.

### [G02] Walking Labs — Learn Harness Engineering

**URL :** https://github.com/walkinglabs/learn-harness-engineering  
**Catégorie : A** — cours de référence, 14 leçons et projets pratiques d'après son README actuel. Couvre AGENTS, vérification, reprise de sessions, loop engineering, graph engineering, analyse comparée de Claude Code/Codex/Pi/DeepSeek. Très proche de notre domaine.

**Réutilisable comme idées** : état persistant minimal, boucle *planifier → agir → vérifier → transmettre*, description d'un « graph » comme routage explicite. **Ne pas recopier** ses templates, exercices ou skill `harness-creator` par défaut : licence, maintenance, qualité et conflit avec notre politique « pas de skills maison » à évaluer. En VCR nous aidons à choisir et **auditer**, pas à refaire le cours.

### [G03] TrishamBP — Harness Engineering

**URL :** https://github.com/TrishamBP/harness-engineering  
**Catégorie : A/C** — diagrammes et implémentation Python stdlib d'un harness de référence (boucle, outils typés, permissions, logs, contexte, contrôles, coordination). Utile pour comprendre les interfaces d'un runtime complexe.

**Pour Codex** : lire son design, comparer nos obligations de sûreté ; ne pas prendre le code entier comme dépendance et ne pas développer un runtime alternatif dans P0.1. Son code est une illustration originale inspirée d'une étude, pas le code de production des agents analysés.

### [G04] Gloriaameng — Awesome Agent Harness

**URL :** https://github.com/Gloriaameng/Awesome-Agent-Harness  
**Catégorie : A** — annuaire et grille comparant plusieurs fonctions : boucle, outils, contexte, état, hooks, évaluation. Référence utile pour enrichir notre catalogue ; peut comporter des descriptions datées de produits et des informations non vérifiées.

**Pour Codex** : extraire seulement les entrées pertinentes, croiser chaque affirmation avec la documentation première partie du projet. Ne jamais considérer son classement comme benchmark.

### [G05] LangGraph

**Repo :** https://github.com/langchain-ai/langgraph  
**Persistance :** https://docs.langchain.com/oss/python/langgraph/persistence  
**Catégorie : C/B futur** — moteur de graphes d'exécution avec état, checkpoints, interruption/approbation, reprise, routage, fan-out/fan-in. Intéressant si VCR orchestre plusieurs agents autonomes dans de longs audits distribués.

**Critère d'introduction** : apparaissent réellement des besoins de reprise après crash, de coordination de N agents et de points d'approbation au milieu d'exécutions. En P0.1, un simple workflow Python suffit, **pas de LangGraph**.

## 3. Navigation, cartes et recherche de code

### [G06] Serena

**URL :** https://github.com/oraios/serena  
**Catégorie : B** — recherche structurée par symboles/références, intégration des agents via outils. Peut rendre les grosses bases plus navigables.

**À étudier** : langages réellement pris en charge, installation, démarrage LSP, sécurité du MCP, quotas de sortie et logs, commandes de recherche, limites sur JS/TS et Python. Alternative simple : `rg`, `git grep`, analyse des imports, sommaire des fichiers. Ne pas faire de Serena un composant obligatoire ou présumer que chaque agent l'utilise automatiquement.

### [G07] Aider RepoMap

**Documentation :** https://aider.chat/docs/repomap.html  
**Repo :** https://github.com/Aider-AI/aider  
**Catégorie : A/B** — algorithme de classement de symboles et de présentation compacte. Utile pour apprendre le *budgeted context*. L'étude Agent Retrieval Bench trouve des performances relatives intéressantes sur le rendement de contexte à 8k tokens.

**À étudier** : réutilisation réelle du composant sans forker Aider entier ; licence, API stable, compatibilité. Si l'usage autonome est complexe, garder la méthode en documentation.

### [G08] DeusData — Codebase Memory MCP

**URL :** https://github.com/DeusData/codebase-memory-mcp  
**Catégorie : B/C** — code graph/index local, outils MCP, graphes de dépendance et de flot ; l'outil actuel contient aussi recherche sémantique/vectorielle et UI optionnelle. **C'est une candidature sérieuse à une couche avancée**, pas une dépendance de base.

**À étudier** : installation et empreinte, version/fonctions, stockage, indexation de secrets, mécanismes de mise à jour, réseau, accès fichiers, granularité des résultats, licence, système de révocation. Ses annonces de « 120× moins de tokens » sont des **claims fournisseur**, pas des gains indépendants vérifiés. Toute comparaison ne doit pas devenir une promesse VCR.

### [G09] RepoAgent

**URL :** https://github.com/OpenBMB/RepoAgent  
**Catégorie : D** — génération/actualisation de documentation de code via AST/LLM et détection de changements. Utile pour la recherche, mais documentation exhaustive peut être très coûteuse et se périmer ; certaines intégrations requièrent un modèle/API et le périmètre de langues peut être limité. À **documenter**, pas à installer.

### [G10] Repomix

**URL :** https://repomix.com/  
**Catégorie : B** — export ponctuel du contexte pour revue, pas une mémoire vivante. Risque de gros exports et de secrets ; vérifier `.gitignore`/fichiers exclus avant de transmettre le résultat à un modèle.

### [G11] Dependency Cruiser / ESLint Boundaries / Import Linter

- **Dependency Cruiser :** https://github.com/sverweij/dependency-cruiser (B, JS/TS, règles et graphes d'imports).
- **ESLint Plugin Boundaries :** https://github.com/javierbrea/eslint-plugin-boundaries (B, JS/TS, frontières contrôlées par lint).
- **Import Linter :** https://import-linter.readthedocs.io/en/stable/ (B, Python, contrats de dépendance).

À sélectionner **un seul** mécanisme approprié lorsque le besoin de frontières est établi. Les imports indirects, chemins dynamiques et éléments métier requièrent un diagnostic complémentaire.

## 4. Skills et workflows d'ingénierie déjà publics

### [G12] Matt Pocock — Skills for Real Engineers

**URL :** https://github.com/mattpocock/skills  
**Catégorie : B (sélection manuelle de skills individuels)**. Compétences de formalisation, architecture, audit, TDD, passation. Au moment de la revue, le dépôt décrit entre autres : `grill-with-docs`, `to-spec`, `improve-codebase-architecture`, `retro`, `diagnosing-bugs`, `code-review`, `to-tickets`.

**Avis :** particulièrement pertinent pour IMPROVE (`retro`) et préparation des spécifications ; vérifier **le nom et le contenu exact à la version installée**. Son existence et sa notoriété ne démontrent pas de gains comparatifs individuels. Ne pas installer tout son setup dans chaque repo.

### [G13] Jesse Vincent / obra — Superpowers

**URL :** https://github.com/obra/superpowers  
**Catégorie : B**. Workflows de debugging systématique, tests, vérification avant fin, planification. Peut imposer des étapes lourdes qui conviennent moins aux micro-tâches ; examiner `systematic-debugging` / `verification-before-completion` et les règles de déclenchement réelles.

### [G14] Vercel — Agent Skills

**URL :** https://github.com/vercel-labs/agent-skills  
**Catégorie : B**. Skills de bonnes pratiques React, Next.js et UX web ; utile pour START lorsqu'une stack correspond. Source officielle sur les pratiques du framework ; **pas de preuve indépendante de gain marginal du skill exact** dans notre corpus. Scanner scripts, version et déclencheurs avant usage.

### [G15] GitHub — Spec Kit

**URL :** https://github.com/github/spec-kit  
**Catégorie : B/A**. Spécification → planification → implémentation → vérification. Source de bonnes pratiques à adapter pour START et définition des besoins ; n'introduire qu'un sous-ensemble proportionné. Ne pas faire un système de spécifications de 30 documents par défaut.

### [G16] Every — Compound Engineering Plugin

**URL :** https://github.com/EveryInc/compound-engineering-plugin  
**Catégorie : B/C**. Boucle brainstorm/plan/build/review/compound, plusieurs skills et parfois sous-agents ; version actuelle compatible avec Codex selon la documentation (à vérifier lors de l'installation). Très proche de notre IMPROVE ; attention à coûts de contexte, permissions, comportements automatiques et installation de toute la suite. **Étudier certains mécanismes, ne pas l'installer en bloc** pour P0.1.

### [G17] Peter Steinberger — Agent Scripts

**URL :** https://github.com/steipete/agent-scripts  
**Catégorie : A/B**. Instructions courtes, skills synchronisés par scripts, hooks et utilitaires. Utile pour gouvernance et format d'instructions ; de nombreuses décisions sont liées à l'environnement personnel de l'auteur. Ne pas copier ses chemins, modèles ni permissions.

### [G18] Anthropic — Public Skills

**URL :** https://github.com/anthropics/skills  
**Catégorie : A/B**. Exemples officiels de skills et formats ; utiles comme source, pas tous adaptés ni garantis pour production. Nous conservons le principe de sélection et revue individuelles.

### [G19] khasky — Awesome Agent Skills

**URL :** https://github.com/khasky/awesome-agent-skills  
**Catégorie : D/B sur skill individuel**. Catalogue de skills d'audit, debugging, qualité ; instructions d'installation globales par lot très larges. **Ne pas utiliser l'installation de tous les skills** proposée dans le README ; sélectionner uniquement après revue du code, de la licence et de la valeur.

### [G20] SWE-Skills-Bench (benchmark + corpus)

**Code :** https://github.com/ControllableModel/SWE-Skills-Bench  
**Papier révisé :** https://arxiv.org/html/2603.15401v2  
**Catégorie : A (recherche)**. Référence pour différencier « connu » et « évalué ». Les quatre skills positifs du protocole ne constituent pas une shortlist universelle de production ; certaines tâches appartiennent à des écosystèmes non ciblés par VCR (Go/Java). Épingler le commit exact si l'on discute de la version testée.

## 5. Optimisation de tokens et coûts

### [G21] Microsoft — TokenEconomizer

**URL :** https://github.com/microsoft/TokenEconomizer  
**Publication :** https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/  
**Catégorie : B/C**. Plugin de contrôle de coûts sur agents, utilise micro-faits, filtrage outils et garde sur boucles d'échecs. Recherche intéressante, mais ses hooks agissent sur un runtime, ses fichiers de config et potentiellement des traces locales. La table du README donne **des plages précises de versions supportées** ; Codex peut changer rapidement. Ne jamais installer automatiquement et ne jamais promettre un pourcentage constant.

**Checklist avant usage** : version réelle de Codex/Claude ; dépendances ; hooks et commandes ; fichiers locaux touchés ; modèle/judge additionnel ; données enregistrées ; accès réseau ; instructions d'undo ; consentement. Tester d'abord dans un profil de Codex isolé et un dépôt jetable, pas les projets personnels.

## 6. Sécurité de la supply chain des skills

Étude USENIX Security 2026 : https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi  
Spécification : https://agentskills.io/specification

**Fiche obligatoire avant de recommander un skill en installation :**

```text
ID et nom exact :
Lien officiel et mainteneur :
Tag/commit de revue :
Licence et redistribution :
Date du dernier commit/release :
Domaine utile et modèle(s) ciblé(s) :
Preuve de bénéfice (étude exacte / retour / aucune) :
Contenu des SKILL.md et scripts :
Actions dangereuses / réseau / permissions / secrets :
Coût en contexte et dépendances :
Chevauchement avec les skills déjà installés :
Compatibilité Codex / Claude / versions :
Installation minimale :
Désinstallation et rollback :
Statut : non vérifié / documenté / révisé / optionnel / déconseillé
```

**Règle** : un dépôt très populaire reste une entrée **G**, pas **E**. La preuve « fonctionne » n'est pas la preuve « améliore significativement la réussite ».

## 7. Programme de recherche appliquée — sans benchmarks de performance maison

**À mener par Codex en priorité sur des dépôts de démonstration** :

| Recherche | Question précise | Livrable documentaire | Intégration |
|---|---|---|---|
| Serena | Navigation par symboles TS/Python sans surcharge ? | fiche installation/risques/usage, capture de résultat sur fixture | B futur |
| Codebase Memory MCP | Graph d'appels local pertinent pour un module complexe ? | fiche architecture/permissions/limites ; pas de claim tokens repris | B/C |
| TokenEconomizer | Hooks compatibles avec la version locale ? Peut-on isoler la config ? | fiche version/rollback/risque | B/C |
| Harness² | Quelles abstractions généralisables sans récursion autonome ? | fiche des huit composants, deux boucles et sécurité | C uniquement |
| LangGraph | Quel problème concret de reprise/coordination justifie un graph ? | matrice de décision mono-agent vs graphe | C |
| Skills Pocock / Vercel / Superpowers | Quels skills précis sans doublons, sur quelles stacks ? | fiche de sélection et provenance | B |

La « preuve de fonctionnement » du prototype inclut des **tests de compatibilité/fonctionnels** sur fixtures. Il ne faut pas les appeler étude démontrant une économie de tokens ; ne pas publier de benchmark de performance comparatif, conformément à la décision utilisateur.

## 8. Sources complémentaires pertinentes, à laisser dans le catalogue historique
