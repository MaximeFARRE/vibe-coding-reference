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

