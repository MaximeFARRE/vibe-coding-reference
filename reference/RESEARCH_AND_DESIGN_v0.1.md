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
