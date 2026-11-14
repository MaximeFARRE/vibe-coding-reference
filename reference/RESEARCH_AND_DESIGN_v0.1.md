---
title: "Vibe Coding Reference — Research & Design Reference"
subtitle: "Décisions, hypothèses, architecture documentaire et bibliographie"
version: "0.1"
date: "2026-11-12"
status: "Document fondateur de travail — aucune implémentation lancée"
language: "fr"
---

# Vibe Coding Reference

**Research & Design Reference — v0.1**  
**Date de consolidation : 12 novembre 2026**  
**Statut : document de cadrage et de recherche, pas une spécification logicielle finale.**

> **But de ce document.** Conserver les décisions prises au fil de nos échanges, les idées encore à examiner, les limites explicites du projet et l'ensemble des sources identifiées. Il est destiné à être versionné dans le futur dépôt GitHub et révisé lorsque des publications nouvelles justifient une évolution.

## 0. Comment lire ce document

Les affirmations sont classées en quatre statuts :

- **RETENU** — décision de produit ou méthode explicitement acceptée.
- **HYPOTHÈSE** — option plausible à documenter, non démontrée comme optimale.
- **À ÉTUDIER** — piste ou source répertoriée, sans conclusion ferme.
- **ÉCARTÉ / REPORTÉ** — hors périmètre actuel ou refusé comme défaut.

**Échelle documentaire** : **A** = étude empirique dont on examine la méthodologie ; **B** = retour d'expérience technique détaillé ; **C** = spécification ou documentation officielle ; **D** = dépôt, méthode ou opinion à examiner. Les lettres indiquent la nature de la preuve, **pas une note de vérité**. Une étude expérimentale peut elle-même avoir un périmètre limité.

**État de vérification des liens** : « ouvert » indique qu'une page source a été consultée dans cette consolidation ; « recensé » signifie que le lien provient de nos recherches précédentes et doit encore faire l'objet d'une lecture critique. L'existence d'un lien ne valide pas toutes les promesses de son auteur.

---

# Partie I — Décisions de cadrage

## 1. Vision et cible

**RETENU —** Construire un **dépôt GitHub open source de référence** pour les personnes qui développent et maintiennent des applications largement, voire intégralement, avec des agents de code (Codex, Claude Code, etc.). Le dépôt doit aider à prendre de meilleures décisions techniques, initialiser un projet proprement, récupérer un projet devenu difficile à maintenir et fournir des configurations, skills, outils et procédures éprouvés ou solidement documentés.

Le dépôt est une **ressource structurée** : guides, fiches de sélection, références scientifiques, configurations et starter packs réutilisables. Il ne s'agit pas actuellement d'un nouvel agent, d'un SaaS ni d'un système automatisé complet de création d'applications.

### Objectifs prioritaires

1. Démarrer un projet avec une stack, une infrastructure et une architecture proportionnées aux besoins.
2. Préserver la maintenabilité sur plusieurs mois ou années, y compris lorsque le code reste produit à 100 % par IA.
3. Identifier la dette technique, les bugs, les risques, les doublons et la surcomplexité sans alarmisme.
4. Réduire le coût de **compréhension et de modification** du code pour les agents, sans prétendre à des gains en tokens non publiés.
5. Installer **sélectivement** les bibliothèques, linters, tests, contrôles, skills et outils utiles.
6. Documenter de manière vivante les décisions métiers et techniques ; automatiser les index déterministes lorsque pertinent.
7. Distinguer recommandations étayées, bonnes pratiques contextuelles et simples préférences.
8. Rendre le catalogue multi-agents, multi-stacks et peu dépendant des modes du moment.

### Public cible

- Vibe coders débutants ne maîtrisant pas tous les métiers du développement.
- Profils techniques non spécialistes du full-stack qui automatisent déjà beaucoup avec l'IA.
- Développeurs confirmés cherchant une sélection sourcée d'outils et de workflows IA.
- Personnes possédant des applications existantes qui sont devenues fragiles ou coûteuses à modifier.

### Principe éditorial

> **Ne pas confondre richesse du catalogue et surcharge du projet.** Le dépôt peut répertorier beaucoup de ressources ; chaque application ne doit recevoir que les composants réellement justifiés.

## 2. Périmètre et exclusions

### RETENU

- Deux parcours principaux : **START** et **RESCUE**.
- Quatre domaines transversaux : **ARCHITECTURE**, **AGENT CONTEXT**, **QUALITY** et **RESEARCH**.
- Des comparatifs techniques **conditionnels**, jamais un classement universel de frameworks.
- Des fiches d'outils précisant usage, dépendances, limites, sécurité, alternatives, sources et statut de maintenance.
- Un processus de contrôle des skills tiers avant leur adoption (scripts, provenance, licence, permissions, mises à jour).
- Une philosophie « configuration minimale suffisante » et « simplicité avant sophistication ».

### ÉCARTÉ / REPORTÉ

- Création d'un outil SaaS ou d'une interface web autour de la bibliothèque : **pas pour le moment**.
- CLI complexe, assistant d'installation propriétaire et nouvel agent de codage : **hors priorité**.
- Création d'un framework IA ou d'une architecture « AI-native » maison sans nécessité démontrée.
- Benchmarks personnels des architectures, coûts en tokens ou performances des agents : **écartés explicitement**.
- Installation de tous les skills, MCP, outils et packages dans chaque dépôt.
- Doctrine unique imposant Next.js, Python, FSD, microservices ou un monolithe particulier à tous les projets.
- Réécriture par défaut des projets existants.
- Seuils rigides de lignes de code comme critère universel de qualité.
- Documentation longue lue entièrement avant chaque modification.

### Non tranché

Nom public, licence précise, gouvernance des contributions, première sélection de starter packs, format de distribution, politique de version des configurations, granularité des fiches et éventuelle CLI future.

## 3. Principes non négociables

1. **La preuve avant l'affirmation** : étayer les constats techniques et ne pas surestimer les bénéfices.
2. **Les besoins avant le framework** : architecture et infrastructure découlent du produit.
3. **La simplicité avant la « pureté » architecturale** : pas de couche abstraite sans valeur démontrable.
4. **La sécurité et l'intégrité des données avant les refactorings cosmétiques**.
5. **La fonctionnalité métier avant la suppression de code** : un élément complexe peut être indispensable.
6. **L'architecture doit être vérifiable** : préférer des frontières contrôlables par lint/tests aux injonctions vagues.
7. **La documentation doit être utile à la navigation**, ciblée et à jour.
8. **Ne pas imposer d'effort inutile aux modèles récents** : revisiter prompts et skills quand les capacités changent [S02].
9. **Multi-agent / multi-stack**, avec des adaptations propres à chaque environnement plutôt qu'un faux standard universel.
10. **Pas de conclusions quantitatives non fondées** : ni économies de tokens ni supériorité statistique d'une stack sans littérature pertinente.

---

# Partie II — Parcours START

## 4. Ce que START doit couvrir

**Question d'entrée :** « Quel environnement faut-il pour créer proprement ce projet, avec le minimum de complexité raisonnable ? »

### 4.1 Choisir dans le bon ordre

1. **Produit** : usage, opérations critiques, données, utilisateurs, SEO, niveau d'interactivité.
2. **Exploitation** : local, intranet ou public ; hébergement, sauvegardes, observabilité, maintenance.
3. **Données et sécurité** : persistance, multi-utilisateur, droits d'accès, migrations, secrets.
4. **Stack** : langage, framework(s), base de données, runtime.
5. **Architecture interne** : découpage par responsabilités, modules, flux, règles de dépendances.
6. **Outillage initial** : tests, lint, typage, CI, documentation, instructions agent, skills.

**Important :** TypeScript/Python sont des langages ; Next.js/FastAPI des frameworks ; monolithe modulaire/vertical slice des architectures ; Vercel/VPS/local des choix d'exploitation. Leurs comparaisons doivent rester séparées.

### 4.2 Questions à documenter dans les guides START

- Application locale, web publique, intranet, outil desktop, script ou API ?
- Utilisateur unique, petite équipe, clients externes ?
- Besoin d'authentification, autorisations, comptes et partage de données ?
- Données sensibles, contraintes réglementaires, restauration et sauvegarde ?
- Une base locale suffit-elle ou faut-il une base accessible à plusieurs processus ?
- Frontend statique, interaction riche, rendu serveur, SEO ?
- Algorithmes, calculs ou écosystème Python indispensables ?
- Coûts d'infrastructure, fréquence de maintenance et compétence d'exploitation ?
- Besoins futurs confirmés ou simplement hypothétiques ?
- Peut-on éviter un second serveur, un framework, un orchestrateur ou une base supplémentaire ?

### 4.3 Stacks candidates — pas de gagnant déclaré

| Stack | Cas à examiner | Risque de surcomplexité à surveiller |
|---|---|---|
| HTML / CSS / JavaScript | site statique ou outil très simple | accumulation de scripts sans structure |
| Astro | contenu, site vitrine, documentation | usage excessif pour une application lourde en interaction |
| React + Vite + TypeScript | interface riche et frontend séparé | multiplication des services lorsqu'un backend apparaît |
| Next.js + TypeScript | application web full-stack | frontières serveur/client, conventions et dépendances |
| SvelteKit | application web full-stack | conventions et expertise de l'écosystème |
| Django + HTMX | gestion, formulaires, CRUD | interactions riches et états UI complexes |
| FastAPI + React | backend Python central | maintien de deux applications et d'un contrat API |
| Streamlit + Python | analytique, démonstration et outil interne | limites des interfaces applicatives complexes |
| Ruby on Rails | application de gestion fortement conventionnée | adoption de Ruby et des conventions Rails |

**HYPOTHÈSE :** pour de nombreuses petites et moyennes applications, un monolithe simple ou modulaire peut limiter l'exploitation et les changements transversaux. Ce n'est pas une conclusion expérimentale sur la performance des agents [S36].

### 4.4 Inventaire de départ d'un projet propre

- Structure de dépôt et commandes reproductibles de lancement/test/build.
- Git, `.gitignore`, README court et modèle `.env.example` sans secret.
- Dépendances verrouillées et stratégie raisonnable de mises à jour.
- Formatage, lint, typage et tests pertinents à la stack.
- GitHub Actions ou autre CI si le dépôt est partagé ou déployé.
- Audit de dépendances et détection de secrets.
- Tests de frontières architecturales **si** ces frontières existent.
- Documentation courte : `AGENTS.md`, carte des fonctionnalités quand le projet grossit, décisions importantes.
- Migrations de base, sauvegarde et restauration lorsque les données sont persistantes.
- Skills spécialisés chargés à la demande, après examen de leur provenance.
- Déploiement documenté, avec configuration minimale et rollback possible.

**Non-obligation :** Playwright, Docker, Redis, PostgreSQL, monitoring distribué, RAG et MCP ne sont pas des dépendances de base universelles.

---

# Partie III — Parcours RESCUE

## 5. Objectif et philosophie

**RESCUE** est le parcours le plus différenciant : remettre sur des rails un dépôt construit rapidement avec l'IA, devenu difficile à comprendre, maintenir ou faire évoluer.

Un audit sérieux doit pouvoir conclure : « l'existant est sain », « répare ces quelques frontières », « reconstruis uniquement tel sous-système » ou « la reconstruction générale est mieux justifiée ». **Il ne doit pas chercher à produire artificiellement une longue liste d'erreurs.**

## 6. Méthode de diagnostic

### Phase A — Audit non destructif

- Inventaire du produit, des parcours, de l'architecture et des contraintes de déploiement.
- État Git et présence de modifications non sauvegardées ; ne pas les écraser.
- Vérifications passives : lint, typage, tests, build, versions de dépendances.
- Cartographie des modules, points d'entrée, imports, chemins de données, API.
- Analyse du code mort, duplication, dépendances trop fortes et abstractions inutiles.
- Revue de la sécurité : secrets, origines, permissions, validations, uploads, vulnérabilités.
- Revue des bases : migrations, transactions, intégrité, restauration et accès concurrents.
- Revue des parcours fonctionnels : redondances, complexité UX, fonctionnalités difficiles à justifier.
- Revue de la documentation et du contexte agent : erreurs, obsolescence, recherches répétitives.
- Limites explicites : pas de pentest, de test destructif ni d'accès à de vraies données sans autorisation.

### Phase B — Décision formalisée

| Verdict | Sens | Exemple |
|---|---|---|
| **KEEP** | fondations saines, petites corrections | documenter et verrouiller quelques conventions |
| **REFACTOR** | réorganisation ciblée sans changer le produit | scinder un workflow complexe, éliminer un N+1 |
| **PARTIAL REBUILD** | reconstruire une zone précisément délimitée | import fragilisé dont la frontière est claire |
| **REBUILD** | reconstruction globale mieux justifiée | architecture inadaptée + coût/risque de réparation supérieurs |

Chaque verdict doit traiter au minimum : preuves, comportements à préserver, données, tests disponibles, coût de transition, régressions probables, sécurité, bénéfice attendu et incertitudes. **Pas de score arbitraire « 3/10 donc à réécrire ».**

### Phase C — Recovery contrôlé, après validation humaine

1. Préserver les données et créer une branche distincte.
2. Établir des tests/fixtures de référence sur les comportements critiques.
3. Corriger d'abord les risques de sécurité ou d'intégrité confirmés.
4. Retirer les dépendances et chemins morts **confirmés**.
5. Réparer les problèmes de persistance et les frontières API.
6. Simplifier le produit et les workflows sans perte métier décidée implicitement.
7. Refactorer une zone cohérente à la fois, avec vérifications et commits séparés.
8. Mettre à jour documents, cartes et commandes de tests.
9. Signaler les risques non résolus et ce qui n'a pas pu être testé.

### 6.1 Les dix axes minimaux d'audit

Architecture ; code ; fonctionnalité et UX ; dépendances ; sécurité ; fiabilité/tests ; données/migrations ; performances ; infrastructure ; documentation/maintenabilité IA.

### 6.2 Exemples de mauvaises conclusions à éviter

- « 1 500 lignes = code mauvais » : la taille seule est un signal.
- « Aucun import trouvé = fonctionnalité inutilisée » : présence possible d'appels dynamiques ou externes.
- « Plus de patterns = architecture meilleure » : les abstractions peuvent masquer le flux réel.
- « Framework récent = reconstruction rentable » : migration et régression peuvent dépasser les bénéfices.
- « Les tests passent = l'UX fonctionne » : un parcours complet peut manquer de couverture.
- « L'IA veut dix documents supplémentaires » : leur maintenance peut coûter plus que leur usage.

### 6.3 Le cas Patrimoine : enseignements à conserver

Un audit de l'application Next.js/SQLite de référence a fait ressortir une stack globalement cohérente mais des difficultés localisées : dépendances vulnérables, 28 appels à une routine de migration depuis des lectures, gros composants orchestrateurs, import Trade Republic complexe et maintenu pour des raisons fonctionnelles, risques de routes POST locales, trous de tests API/migrations et documentation périmée. Les parcours Portefeuille et Projections ont été réorganisés conceptuellement en **essentiel + avancé**, sans suppression de calculs. Le bon verdict dans ce cas était **REFACTOR**, pas **REBUILD**.

**Leçon transférable :** une architecture globalement saine peut devenir difficile à maintenir par accumulation locale ; mieux vaut retirer la complexité réelle plutôt que réécrire la stack.

---

# Partie IV — Architecture et agents

## 7. Architectures à documenter

| Architecture | Atout possible | Limite / contexte |
|---|---|---|
| Monolithe simple | peu d'infrastructure, découverte facile | risques de couplage en grandissant |
| Monolithe modulaire | domaines séparés, un déploiement | règles de dépendances à faire respecter |
| Feature-first / vertical slices | parcours cohérent dans peu de modules | duplication possible ; découpage fin à surveiller |
| Clean / hexagonale | ports explicites, logique métier isolée | peut multiplier interfaces et couches |
| Feature-Sliced Design | conventions frontend et règles d'import | surdimensionnement possible pour petit projet [S33–S34] |
| Microservices | autonomie d'équipes et services | réseau, déploiements et opérations supplémentaires |

**HYPOTHÈSE DE TRAVAIL :** « monolithe modulaire + organisation par fonctionnalités + règles d'import » peut être un bon point de départ pour beaucoup d'applications. Cette hypothèse est inspirée de pratiques et de retours techniques, **pas d'une étude comparative démontrant une supériorité pour les IA** [S01, S33, S36].

### 7.1 Principes structurants

- Collocaliser les éléments d'un même workflow lorsque cela réduit la recherche et les changements en cascade.
- Séparer les calculs métier des I/O lorsque les tests et la pérennité y gagnent.
- Créer une abstraction partagée seulement après un besoin récurrent et réellement identique.
- Conserver des frontières de données, API et sécurité explicites.
- Prohiber les dépendances entre domaines seulement lorsqu'elles sont réellement interdites ; documenter les exceptions.
- Chercher une architecture **lisible et vérifiable**, pas un maximum de petits fichiers.
- Couvrir les frontières importantes par linters ou tests structurels lorsque la stack le permet.

### 7.2 Contrôles techniques d'architecture

- JS/TS : [Dependency Cruiser](https://github.com/sverweij/dependency-cruiser), [ESLint Plugin Boundaries](https://github.com/javierbrea/eslint-plugin-boundaries).
- Python : [Import Linter](https://import-linter.readthedocs.io/en/stable/).
- FSD : examiner le linter officiel et les skills [S34].

Ces outils sont des **candidats** : vérifier leur compatibilité avec la stack et éviter de superposer des outils de même fonction sans valeur ajoutée.

### 7.3 Ce qu'OpenAI montre, et ce qu'OpenAI ne prouve pas

Le retour *Harness Engineering* décrit un dépôt produit par Codex, une documentation servant de source de connaissance, des frontières architecturales explicites et des contrôles automatisés [S01]. Cela justifie une **piste forte de conception**. Il ne démontre ni la supériorité universelle de Next.js, ni une économie de tokens quantifiée pour toute architecture.

---

# Partie V — Documentation vivante et contexte IA

## 8. Les quatre couches de connaissance

1. **Règles et orientation** — `AGENTS.md` court : commandes, invariants, limites, chemins vers les docs pertinentes.
2. **Carte fonctionnelle** — fonctionnalité → module, point d'entrée, tests, flux importants.
3. **Index structurel** — symboles, imports, appels, routes, références, éventuellement un graphe régénérable.
4. **Intentions et décisions** — règles métier, architecture decision records, arbitrages et raisons des exceptions.

**La distinction clé :** un index peut découvrir où est une fonction ; il ne peut pas nécessairement retrouver pourquoi un calcul ou une règle métier existe.

### 8.1 Règles retenues

- Ne pas faire lire toute la documentation avant chaque action [S02, S04].
- Utiliser une divulgation progressive et des skills à déclenchement clair [S02, S40].
- Documenter le bon chemin vers les sources, plutôt que paraphraser toutes les fonctions.
- Adapter la découverte de `AGENTS.md` aux agents réels : Codex et Claude Code ne chargent pas forcément les fichiers de la même manière [S41–S42].
- Ne pas créer d'index complexe pour un dépôt qui tient déjà facilement en contexte.
- Préférer les connaissances persistantes réellement utiles aux instructions répétitives.

### 8.2 Mise à jour : événements plutôt que régénération générale

| Déclencheur | Réponse documentaire souhaitée |
|---|---|
| Fichier déplacé ou renommé | réparation des références/index automatiques |
| Fonction/signature modifiée | réindexation déterministe de la zone concernée |
| API/route ajoutée | inventaire des routes mis à jour |
| Module découpé | révision ciblée de la carte des fonctionnalités |
| Règle métier changée | revue humaine/agent de la décision documentée |
| Pull request | contrôle de dérive docs-code, proposition révisable |
| Échéance périodique | contrôle de cohérence, non réécriture intégrale |

Indexation des symboles et imports : **outil déterministe** de préférence. Explication du sens des changements : **IA ciblée** si nécessaire. Les modifications proposées par agent devraient passer par une PR relisible, à l'image de [S31].

### 8.3 Outils de contexte à suivre

- **Serena** [S26] : navigation à base de symboles et références.
- **Aider Repository Map** [S27] : carte compacte et sélection d'éléments importants.
- **Codebase Memory MCP** [S28] : graphe/index local persistant ; claims de performance à ne pas reprendre sans étude indépendante.
- **Google Code Wiki** [S29] : référence de documentation structurée mise à jour avec les dépôts.
- **RepoAgent** [S30] : génération/mise à jour de documentation, fonctionnement et portée à approfondir.
- **GitHub Agentic Workflows Docs Updater** [S31] : proposition de PR documentaire.
- **Repomix** [S32] : export compact ponctuel, différent d'un système de connaissance vivant.

### 8.4 Question de recherche ouverte

Quelles publications établissent, à périmètre comparable, l'effet des **cartes de code**, de la **recherche symbolique**, du **chargement progressif** et des **instructions de dépôt** sur la réussite d'un agent ? [S04, S09] sont des points d'entrée ; elles ne règlent pas toutes les comparaisons.

---

# Partie VI — Outillage et Quality Gates

## 9. Politique générale

**RETENU :** une règle importante doit autant que possible être contrôlée par un outil reproductible. Une consigne vague dans `AGENTS.md` ne suffit pas lorsqu'un linter ou un test peut vérifier le comportement.

### 9.1 Catalogue initial d'outils (non prescriptif)

| Besoin | JavaScript / TypeScript | Python / transversal |
|---|---|---|
| Paquets / verrouillage | npm ou pnpm | uv |
| Format et lint | Biome ou ESLint/Prettier | Ruff |
| Typage | TypeScript strict | Pyright |
| Tests | Vitest | pytest |
| Tests navigateur | Playwright si parcours critiques | Playwright si application web |
| Code inutilisé | Knip | Vulture / Deptry selon besoin |
| Audit dépendances | npm audit / OSV-Scanner | pip-audit / OSV-Scanner |
| Secrets | Gitleaks | Gitleaks |
| Contrats modules | Dependency Cruiser / Boundaries | Import Linter |
| CI | GitHub Actions | GitHub Actions |
| Dépendances à jour | Dependabot / Renovate | Dependabot / Renovate |

### 9.2 Politique des contrôles

- Format, lint, typage, tests et build : peuvent être bloquants lorsqu'ils sont applicables et stables.
- Sécurité : bloquer en cas de secret exposé ou risque grave confirmé ; examiner les exceptions.
- Complexité cognitive, duplication et gros fichiers : **signalement contextualisé**, pas suppression mécanique.
- Contrôle du schéma et sauvegarde : renforcés pour applications manipulant des données précieuses.
- End-to-end : commencer par les parcours à risque réel ; éviter de multiplier les tests fragiles pour une page statique.
- Contrôles d'architecture : uniquement pour des frontières choisies et documentées.

Les seuils de 400 lignes/fichier et 80 lignes/fonction, évoqués au cours de la recherche, sont **des exemples pédagogiques, non des normes validées**. Aucun seuil fixe n'est adopté.

## 10. Skills et agents

### Bibliothèque fonctionnelle envisagée

- START : `choose-stack`, `initialize-project`, `implement-feature`, `fix-bug`, `review-code`, `deploy`.
- RESCUE : `audit-existing-project`, `audit-architecture`, `audit-dependencies`, `audit-security`, `audit-tests`, `audit-maintainability`, `audit-performance`, `simplify-project`, `recovery-plan`, `safe-refactoring`, `evaluate-rebuild`.
- CONTEXTE : `map-codebase`, `find-relevant-code`, `update-documentation`, `audit-documentation`.

**Ces noms décrivent des capacités recherchées, pas des skills déjà créés.** Réutiliser d'abord les skills existants après audit de qualité, licence et compatibilité. Le format [Agent Skills](https://agentskills.io/specification) est une base d'interopérabilité, non la preuve que tous les agents interprètent un skill exactement de la même manière [S40].

### Pratiques retenues

- Des descriptions très courtes et précises pour déclencher les skills [S02, S17].
- Chargement des références détaillées seulement à la demande.
- Pas de double installation du même skill ou de douze compétences quasi identiques.
- Scripts reproductibles pour opérations déterministes.
- Vérifier les effets et droits des scripts tiers avant installation.
- Révision périodique des skills anciens, particulièrement après un changement de modèle [S02, S05].
- Pour tâches longues/risquées : contrat de résultat et revue indépendante, sans imposer par défaut un dispositif multi-agents coûteux [S05, S07].

---

# Partie VII — Doctrine de recherche

## 11. Politique de preuve

**Décision explicite : pas de benchmarks maison.** La bibliothèque s'appuie sur la littérature existante et les sources techniques originales. Si une question n'a pas de preuve, l'indiquer plutôt que créer un classement intuitif.

### Hiérarchie pratique

- **A — Étude empirique** : protocole, groupe(s), conditions, résultats et limites disponibles. L'effet observé n'est valable que pour ce périmètre.
- **B — Retour industriel détaillé** : OpenAI, Anthropic, Google, etc. Contexte concret, apprentissages précieux mais possible biais de sélection.
- **C — Documentation/spécification officielle** : description de comportements et d'interfaces, non preuve de productivité.
- **D — Dépôt/pratique personnelle/opinion** : excellente source d'idées ; conclusions à confirmer indépendamment.

### Sources prioritaires

OpenAI et les équipes Codex ; Anthropic et Claude Code ; DeepSeek ; Google DeepMind et Google ; publications scientifiques sur agents de code, génie logiciel et interfaces ; organismes indépendants comme METR ; auteurs identifiés (Andrej Karpathy, Matt Pocock, Peter Steinberger) pour leurs pratiques, **pas comme garantie scientifique**.

### Règles d'édition pour une recommandation

Chaque fiche devra préciser : (1) problème visé ; (2) contexte applicable ; (3) recommandation ; (4) contre-exemples ; (5) sources primaires ; (6) type de preuve ; (7) limites ; (8) date de dernière revue ; (9) décision retenue/à tester/écartée ; (10) changement depuis version précédente.

### Précautions essentielles

- Un papier de performance de modèle ne prouve pas une supériorité de framework.
- Un repo très populaire n'est pas une preuve de gain en tokens.
- Un retour de production d'OpenAI ne s'applique pas automatiquement à un petit projet individuel.
- Une étude sur les modèles 2024–2025 peut perdre de sa pertinence avec les modèles 2026.
- Une publication d'éditeur peut avoir un biais commercial : comparer avec des résultats indépendants.
- On doit laisser les conclusions ouvertes si les preuves sont insuffisantes.

## 12. Résultats publiés déjà utiles, sans extrapolation excessive

- OpenAI montre l'intérêt d'un **environnement agent lisible**, des garde-fous et d'une documentation utilisée comme source de référence dans un projet Codex [S01]. **Nature B**.
- OpenAI recommande de réduire les descriptions de skills inutiles et de ne charger les documents que lorsque la tâche le demande [S02]. **Nature B**.
- Anthropic décrit le contexte comme une ressource finie et recommande un contenu à forte valeur informationnelle [S04]. **Nature B**.
- Anthropic rapporte que la revue séparée, l'évaluation active et les artefacts de transmission peuvent aider des tâches de génération longues, avec un coût et une complexité supplémentaires [S05]. **Nature B**.
- SWE-agent étudie expérimentalement l'influence de l'interface agent-ordinateur pour manipuler un dépôt et exécuter les outils [S09]. **Nature A**.
- METR trouve que, dans ses conditions expérimentales du début 2025, les développeurs expérimentés ont mis en moyenne **19 % de temps en plus** avec IA, malgré une perception inverse ; le résultat n'est pas transposable tel quel aux modèles actuels [S11]. **Nature A**.
- METR explique que des biais de participation rendent sa mise à jour de 2026 difficile à utiliser pour quantifier les gains récents [S12]. **Nature A/B**.
- Google Code Wiki illustre un système de documentation rattachée à des références de code ; c'est une annonce produit et non une validation indépendante de gain de productivité [S29]. **Nature C/B**.

---

# Partie VIII — Décisions, pistes et priorités

## 13. Registre consolidé des décisions

| ID | Sujet | Statut | Décision / raison |
|---|---|---|---|
| D01 | Type de produit | **RETENU** | référentiel GitHub, pas une app |
| D02 | Piliers | **RETENU** | START + RESCUE, contexte/architecture/qualité transverses |
| D03 | Usage RESCUE | **RETENU** | audit lecture seule avant toute réparation |
| D04 | Verdicts RESCUE | **RETENU** | KEEP / REFACTOR / PARTIAL REBUILD / REBUILD |
| D05 | Rebuild | **RETENU** | possible mais exceptionnel et argumenté |
| D06 | Supprimer des fonctions | **RETENU** | jamais sans validation du besoin métier |
| D07 | Choix d'architecture | **RETENU** | contextualisé, sans dogme |
| D08 | Monolithe modulaire/feature-first | **HYPOTHÈSE** | candidat de départ, pas vérité scientifique |
| D09 | Documentation IA | **RETENU** | quatre niveaux, chargement progressif |
| D10 | Maintenance des docs | **RETENU** | événements et révision ciblée, contrôle de dérive |
| D11 | Skills | **RETENU** | catalogue large, installation sélective |
| D12 | Quality gates | **RETENU** | tests, lint, sécurité, frontières vérifiables |
| D13 | Seuils de lignes | **ÉCARTÉ** | pas de critère universel automatique |
| D14 | Benchmarks propres | **ÉCARTÉ** | s'appuyer sur les études existantes |
| D15 | Sources primaires | **RETENU** | industrie + science + documentation, avec limites |
| D16 | Nouvelle CLI | **REPORTÉ** | non nécessaire au référentiel initial |
| D17 | SaaS / application de guidance | **ÉCARTÉ maintenant** | bibliothèque avant produit |
| D18 | Propre framework/agent | **ÉCARTÉ** | privilégier les outils existants |
| D19 | Tous les outils au premier commit | **ÉCARTÉ** | installation minimale adaptée |
| D20 | Réécriture par défaut | **ÉCARTÉ** | vérifier le coût et la valeur de l'existant |

## 14. Questions de recherche non résolues

1. Quelles études comparent véritablement les architectures sous des agents de code récents ?
2. Quelles preuves quantifient la valeur des frontières de modules pour localiser et corriger les bugs ?
3. Quels effets documentés de repo maps, recherche symbolique et index persistants sur la réussite des agents ?
4. Comment détecter automatiquement une dérive de documentation sans créer de bruit ou de faux positifs ?
5. Quelles études sérieuses abordent les critères *rebuild vs refactor* et l'économie de la dette technique ?
6. Quels contrôles sont effectivement indispensables selon le profil de projet ?
7. Comment les comportements de lecture `AGENTS.md` et des skills diffèrent-ils entre agents et versions ?
8. Quels comparatifs officiels/indépendants permettent de recommander des stacks sans surinterpréter ?
9. Quel niveau de standardisation des starter packs reste acceptable sans sacrifier le minimalisme ?
10. Comment maintenir la bibliographie, les liens, les versions et les avertissements de sécurité à jour ?

## 15. Priorité des recherches suivantes

1. **Architecture pour agents** : modularité, barrières automatiques, compréhension du code.
2. **Contexte et documentation** : navigation, indexation, recouvrement docs/code, versionnement.
3. **RESCUE / dette technique** : diagnostic, migration, refactoring ou reconstruction.
4. **Quality gates** : tests, sécurité, vérification des agents, limitations de l'auto-review.
5. **Stack et infrastructure** : recommandations conditionnelles, systèmes et coûts d'exploitation.

À chaque étape : partir des sources primaires, noter les résultats contradictoires et séparer les faits des décisions de conception.

## 16. Arborescence conceptuelle, NON implémentée

```text
vibe-coding-reference/
├── README.md
├── RESEARCH_AND_DESIGN_REFERENCE.md
├── research/
│   ├── evidence-reviews/
│   ├── source-index/
│   ├── industry-publications/
│   └── scientific-papers/
├── start/
│   ├── choosing-stack/
│   ├── choosing-infrastructure/
│   ├── project-initialization/
│   └── starter-packs/
├── rescue/
│   ├── audit/
│   ├── architecture-assessment/
│   ├── rebuild-vs-refactor/
│   └── recovery-process/
├── architecture/
│   ├── patterns/
│   ├── stack-guides/
│   └── architecture-controls/
├── agent-context/
│   ├── documentation/
│   ├── code-navigation/
