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

- Deux parcours principaux : **START** et **RESCUE**.
- Cinq domaines transversaux : **ARCHITECTURE**, **AGENT CONTEXT**, **QUALITY**, **TOKEN EFFICIENCY** et **RESEARCH**.
- Des comparatifs techniques **conditionnels**, jamais un classement universel de frameworks.
- Des processus **en trois niveaux** : immédiat, optionnel, avancé/documentaire.
- La conservation de **sources contradictoires** et la revue des versions révisées de prépublications.
- Le domaine transversal **TOKEN EFFICIENCY** et la distinction explicite tokens/coût/cache/quota.
- Des fiches d'outils précisant usage, dépendances, limites, sécurité, alternatives, sources et statut de maintenance.
- Un processus de contrôle des skills tiers avant leur adoption (scripts, provenance, licence, permissions, mises à jour).
- Une philosophie « configuration minimale suffisante » et « simplicité avant sophistication ».

### ÉCARTÉ / REPORTÉ

- Création d'un outil SaaS ou d'une interface web autour de la bibliothèque : **pas pour le moment**.
- CLI complexe, assistant d'installation propriétaire et nouvel agent de codage : **hors priorité**.
- Création d'un framework IA ou d'une architecture « AI-native » maison sans nécessité démontrée.
- Création d’une bibliothèque de skills maison : **écartée** ; sélectionner les skills publics existants, même si leur efficacité n’est pas automatiquement établie.
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

## 4.5 Nouveau pilier START — spécifier le besoin avant le code

**RETENU (v0.2).** Les agents modernes peuvent écrire beaucoup de code, mais ne peuvent pas deviner des choix de produit non exprimés. *SWE-Journey* [N06] compare des interactions simulées avec des profils différents : dans ce protocole, la proportion de tests de fonctionnalité réussis dépasse 75 % avec des profils architectes logiciels et tombe sous 25 % avec des profils non-développeurs. Ce sont des résultats liés au benchmark, **pas** une probabilité de réussite personnelle. L'étude distingue notamment « demander juste », « trouver juste » et « corriger juste ».

**Vocabulaire accessible :**

- **Besoin** = résultat observable attendu pour l'utilisateur (« je peux importer ce relevé et retrouver mes opérations »).
- **Règle métier** = contrainte de fond (« deux opérations portant le même identifiant ne doivent pas être comptées deux fois »).
- **Critère d'acceptation** = essai concret qui permet de décider si la demande est terminée.
- **Invariants** = choses qui doivent rester vraies après un changement (total, accès, confidentialité, soldes, etc.).
- **Hors périmètre** = comportement à ne pas développer maintenant.

### Flux minimal de spécification

1. Décrire **qui** utilise l'application et **quelle tâche** il veut accomplir.
2. Décrire les **entrées**, **sorties**, **cas limites** et données à protéger.
3. Écrire **2–6 critères d'acceptation observables** pour une demande normale ; davantage uniquement si un flux complexe l'exige. Ceci est un *ordre de grandeur de rédaction*, pas un seuil empirique.
4. Faire reformuler à l'agent **ce qu'il doit préserver** et **ce qu'il ne doit pas faire**.
5. Lancer l'implémentation ; demander la **preuve d'exécution** des contrôles prévus.
6. Faire vérifier l'usage réel à l'écran ou via un exemple d'entrée/sortie, surtout pour les flux critiques.

**Mini-exemple (import de données)** : « Lorsque j'importe deux fois le même fichier, aucune opération n'est dupliquée ; si une ligne est incorrecte, elle est signalée sans supprimer les lignes valides ; je peux retrouver et contrôler les montants importés. » Un test qui vérifie seulement que la route renvoie HTTP 200 est insuffisant.

### Priorité à l'invariant plutôt qu'au jargon

On ne demande pas à un non-développeur de choisir entre *CQRS, DDD, ports/adapters* ou *vertical slices*. On lui demande de décrire ce qui doit marcher ; la sélection technique doit être argumentée par l'agent, puis reliée à des contrôles vérifiables. Les formalismes avancés restent documentaires [N06, S01, S05].

## 4.6 Les trois niveaux d'adoption

| Niveau | Critère | Exemples | Décision |
|---|---|---|---|
| **A. Prêt à l'emploi** | compréhensible, peu de configuration, contrôlable | Git/README, `.env.example`, tests pertinents, lint, build, consignes courtes, sauvegardes si données | proposé normalement |
| **B. Conditionnel** | besoin identifié et bénéfice plausible | Playwright, vérification d'imports entre modules, analyse de code mort, skills Vercel sur Next.js | activer sur justification |
| **C. Avancé / étude** | installation lourde, risques ou avantage incertain | RAG, base vectorielle, graphe persistant, microservices, système multi-agent autonome, proxy de compression, custom lint | garder dans la recherche et l'annuaire |

Un élément peut changer de niveau selon le projet : Playwright est facultatif pour une page statique et pertinent pour une application dont des utilisateurs effectuent des opérations critiques.

## 4.7 Décision de stack — filtres plutôt que palmarès

**L'ordre de sélection demeure** : produit → exploitation → données/sécurité → langage/framework → architecture → outils. Les comparatifs de la section 4.3 sont **candidats**, non gagnants.

| Situation | Candidats plausibles | Questions éliminatoires |
|---|---|---|
| Site principalement éditorial / vitrine | HTML/CSS/JS, Astro, parfois WordPress selon administration | faut-il de l'authentification, une rédaction non-technique, un CMS ? |
| Outil interne simple avec formulaires | Django, Rails, parfois Next.js | faut-il Python scientifique ? une interface JS riche ? |
| Tableau analytique personnel | Streamlit, Dash/équivalent, Next.js + calculs adaptés | quantité d'interactions complexes, autonomie hors réseau, format des données ? |
| App web riche, frontend et backend intégrés | Next.js, SvelteKit, Rails/Django selon équipe | frontière données/client, SEO, compétences d'exploitation ? |
| API et algorithmes Python essentiels | FastAPI, Django, parfois frontend séparé | est-il réellement nécessaire de maintenir deux serveurs ? |
| Script/automatisation ciblée | Python simple, CLI, job planifié | une interface web est-elle indispensable ? |

**Règle anti-surarchitecture** : ne pas ajouter de serveur, couche, bus, base ou orchestrateur pour un besoin seulement hypothétique. En revanche, ne pas économiser sur la sécurité, la persistance et les sauvegardes de données réelles. L'absence d'étude comparative agent/framework est une limite **explicitement maintenue** [N02, S36].

## 4.8 Contrat de fin d'une fonctionnalité

La demande n'est pas « terminée » au seul motif que le modèle déclare la modification effectuée. Un compte-rendu doit mentionner : **fichiers concernés, comportement livré, critères vérifiés, commandes effectivement exécutées, résultats, vérification manuelle si applicable, limites restantes**. « Non testé » est une réponse acceptable si honnête ; « testé » sans exécution n'en est pas une.

Pour une modification minime, éviter un cérémonial disproportionné : la profondeur de contrôle doit refléter le risque de l'opération. Pour un changement de données, d'authentification ou de calcul financier, le niveau de preuve requis augmente.

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

