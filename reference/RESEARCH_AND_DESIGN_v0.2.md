---
title: "Vibe Coding Reference — Research & Design Reference"
subtitle: "Décisions, recherches 2026, START, RESCUE, skills, qualité et efficacité tokens"
version: "0.2"
date: "2026-11-12"
status: "Référence documentaire consolidée — aucune implémentation lancée"
language: "fr"
---

# Vibe Coding Reference

**Research & Design Reference — v0.2**  
**Date de consolidation et revue des sources : 12 novembre 2026**  
**Statut :** document de référence v0.2 (recherche, décisions et guides réutilisables), **pas** une application, un outil installé ni un benchmark original.

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


### Nouveautés majeures de la v0.2

Cette version **conserve l'ensemble des décisions de la v0.1** et ajoute :

- trois revues de littérature : **architecture et navigation**, **gestion du contexte**, **vérification du logiciel produit** ;
- un chapitre consacré aux **besoins métier et critères d'acceptation**, particulièrement pour les non-développeurs ;
- une politique rigoureuse de **skills existants**, documentés selon la preuve disponible, la provenance, la version et la sécurité ;
- un domaine transversal **TOKEN EFFICIENCY** distinguant nombre de tokens, coût API, cache et quotas d'abonnements ;
- un **guide de déploiement gradué** : *par défaut / selon le contexte / documentation avancée* ;
- des fiches pratiques, des modèles de documents et un registre des **corrections de recherche** ;
- des références **[N01] à [N31]** ajoutées aux **[S01]–[S47]** historiques, sans supprimer ces dernières.

### Règle éditoriale supplémentaire — séparer cinq niveaux

1. **Fait de source** : résultat explicitement rapporté par une étude ou documentation ; sa validité est limitée au protocole.
2. **Interprétation** : mécanisme plausible ou généralisation prudente, signalée comme telle.
3. **Décision de produit** : choix retenu pour ce dépôt, qui ne prétend pas être scientifiquement optimal.
4. **Configuration conseillée** : variante *conditionnelle*, dépendant du projet, du modèle et de l'agent.
5. **Point non vérifié** : référence recensée, lien ouvert sans validation complète, version ou comparaison à reprendre.

**Avertissement quantitatif :** un pourcentage trouvé dans une étude ne peut être extrapolé à la réduction de coût d'un projet individuel. Les comparaisons doivent, au minimum, identifier modèle, agent, type de tâches, base de coût, échantillon et vérification du succès. Aucun benchmark maison n'est demandé ou prévu pour étayer cette bibliothèque.

### Pour qui ? Trois parcours de lecture

| Lecteur | Commencer par | Ne pas installer par défaut |
|---|---|---|
| Débutant / non-développeur | START et fiches de vérification métier | orchestration multi-agent, RAG, graphe de code, linter architectural custom |
| Projet existant fragile | RESCUE, risques de données et tests, plan de réparation | réécriture globale et nettoyage automatique sans validation |
| Projet de grande taille / usage intensif d'IA | architecture, navigation, TOKEN EFFICIENCY | compresseur et plugin coût sans revue de compatibilité |

---

# Partie I — Décisions de cadrage

## 1. Vision et cible

**RETENU —** Construire un **dépôt GitHub open source de référence** pour les personnes qui développent et maintiennent des applications largement, voire intégralement, avec des agents de code (Codex, Claude Code, etc.). Le dépôt doit aider à prendre de meilleures décisions techniques, initialiser un projet proprement, récupérer un projet devenu difficile à maintenir et fournir des configurations, skills, outils et procédures éprouvés ou solidement documentés.

Le dépôt est une **ressource structurée** : guides, fiches de sélection, références scientifiques, configurations et starter packs réutilisables. Il ne s'agit pas actuellement d'un nouvel agent, d'un SaaS ni d'un système automatisé complet de création d'applications.

### Objectifs prioritaires

1. Démarrer un projet avec une stack, une infrastructure et une architecture proportionnées aux besoins.
2. Préserver la maintenabilité sur plusieurs mois ou années, y compris lorsque le code reste produit à 100 % par IA.
3. Identifier la dette technique, les bugs, les risques, les doublons et la surcomplexité sans alarmisme.
4. Réduire le coût de **compréhension, localisation et modification** du code pour les agents, en s’appuyant sur des travaux publiés et sans promettre un gain universel en tokens.
5. Installer **sélectivement** les bibliothèques, linters, tests, contrôles, skills et outils utiles.
6. Documenter de manière vivante les décisions métiers et techniques ; automatiser les index déterministes lorsque pertinent.
7. Distinguer recommandations étayées, bonnes pratiques contextuelles et simples préférences.
8. Rendre le catalogue multi-agents, multi-stacks et peu dépendant des modes du moment.
9. Mesurer conceptuellement les choix à l’aune du **coût par tâche correctement achevée**, non du seul nombre de tokens.
10. Accompagner l’utilisateur non-développeur dans l’expression du besoin et la vérification du produit livré.

### Public cible

- Vibe coders débutants ne maîtrisant pas tous les métiers du développement.
- Profils techniques non spécialistes du full-stack qui automatisent déjà beaucoup avec l'IA.
- Développeurs confirmés cherchant une sélection sourcée d'outils et de workflows IA.
- Personnes possédant des applications existantes qui sont devenues fragiles ou coûteuses à modifier.

### Principe éditorial

> **Ne pas confondre richesse du catalogue et surcharge du projet.** Le dépôt peut répertorier beaucoup de ressources ; chaque application ne doit recevoir que les composants réellement justifiés.

## 2. Périmètre et exclusions

### RETENU
