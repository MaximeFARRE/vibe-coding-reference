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

## 6.4 Actualisation RESCUE — preuves et priorités

**RETENU (v0.2).** Chaque constat d'audit doit séparer : **preuve observée**, **risque plausible**, **impact métier**, **recommandation**, **conditions de correction**, **incertitude** et **moyen de contrôler la correction**. Une conclusion peut être « pas assez de preuves pour supprimer ceci ». L'audit **ne confond jamais code volumineux et code inutile**, ni test vert et absence de bug.

### Format minimal d'une fiche de constat

| Champ | Exemple |
|---|---|
| Constat | Une migration de base est déclenchée à chaque requête de lecture |
| Preuve | Fonctions/chemins et appels vérifiés dans le dépôt, commandes exécutées |
| Impact | latence, contention ou risque d'échec selon l'implémentation réelle |
| Incertitude | faut-il mesurer la fréquence et les transactions avant de conclure ? |
| Correction proposée | migration explicite, versionnée, effectuée à l'initialisation/déploiement |
| Sécurité du changement | sauvegarde, migration réversible si possible, tests sur copie |
| Critère d'acceptation | lectures sans appel de migration, données intactes, démarrage vérifié |

### Séquence pratique d'audit, sans modification destructive

1. **Préserver le travail** : vérifier les changements non commités, l'état des branches, les secrets et l'emplacement des sauvegardes. Ne pas forcer de reset Git.
2. **Comprendre le produit** : quelles fonctions comptent, quelles données ne peuvent être perdues, quels utilisateurs et intégrations ?
3. **Relever les contrôles disponibles** : `lint`, typage, build, tests, sécurité des dépendances, sauvegarde/restauration.
4. **Établir la carte réelle** : routes/endpoints, modules, fichiers centraux, DB, bibliothèques, chemins de déploiement ; distinguer ce qui est inspecté de ce qui est supposé.
5. **Examiner les zones à risque** : accès et permissions, validation à la frontière, migrations, transactions, import/export, jobs planifiés, appels externes.
6. **Chercher les anomalies fonctionnelles** : comportements redondants, calculs sans test, données incohérentes, tests ne reproduisant pas l'usage.
7. **Proposer des corrections limitées** : classées par risque et valeur, avec verdict KEEP / REFACTOR / PARTIAL REBUILD / REBUILD.
8. **Faire valider la direction** avant toute transformation de données, suppression de fonctionnalité ou reconstruction.

### Règle pour les modèles capables de relire le code mais non l'usage

Les modèles peuvent produire une explication plausible d'une application dont ils n'ont jamais testé le parcours réel. Le diagnostic doit signaler si une conclusion vient de la lecture du code, d'une reproduction locale, d'un test automatisé ou d'un contrôle utilisateur. Le retour d'Anthropic sur le harness long [N18] montre précisément des applications convaincantes en apparence dont des interactions fondamentales ne fonctionnaient pas.

## 6.5 Risque de reproduction de défauts par les agents

L'étude *Coding Agents Propagate Vulnerabilities in Code Bases* [N09], publiée le 8 novembre 2026, constate que le contexte de code vulnérable peut pousser l'agent à produire des vulnérabilités analogues. Dans son sous-ensemble C/C++ mémoire-sûre, l'écart moyen entre contextes sûrs et vulnérables atteint **35,4 points**, un chiffre **non transposable** aux applications Next.js ou Python sans étude complémentaire.

**Ajout à RESCUE :** repérer les patterns existants qui ne doivent **pas** devenir des modèles de génération (routes sans contrôle d'accès, désérialisation trop permissive, transactions absentes, secrets en dur, bypass de validation). Les corriger à la source quand c'est pertinent, et faire appliquer des tests/linters pour prévenir leur réintroduction. Ne pas compter exclusivement sur une phrase « fais attention à la sécurité ».

## 6.6 REBUILD : l'exception doit rester étayée

Le coût d'une réécriture inclut les fonctionnalités invisibles, cas limites, migrations de données, processus métier, intégrations, déploiement, pertes de connaissances et risque de nouvelles failles. Un nouveau framework ne supprime pas ces coûts.

**Motifs envisageables** : architecture réellement incompatible avec une contrainte confirmée ; socle abandonné et non maintenable ; coût/risque d'une réparation localisée manifestement supérieur ; système sans chemins de migration raisonnables. **Contre-motifs** : gros fichier, code « laid », version non récente ou désir de changer de technologie.

Quand la preuve est insuffisante, proposer un **spike réversible ciblé** uniquement si le commanditaire accepte une expérimentation locale ; notre référentiel ne prescrit pas de benchmark maison pour construire ses conclusions générales.

## 6.7 Qualité des tests dans un projet RESCUE

Trois travaux de 2026 justifient cette rubrique :

- *All Smoke, No Alarm* [N07] : 86 156 patchs de fichiers de tests provenant de 33 596 PR d'agents ; **80,2 %** ont des signaux syntaxiques d'« oracle » (affirmations vérifiables) faibles ou absents. Ce n'est **pas** le taux de tests incorrects.
- *Test Coverage Analysis of Agentic Pull Requests* [N08] : sur les échantillons étudiés, les tests existants couvrent **61,5 % des lignes modifiées exécutables en Java** et **27 % en Python** ; la couverture ne prouve pas qu'un test détecte les mauvaises valeurs.
- *SWE-Journey* [N06] : l'expression du besoin et l'interaction utilisateur influent fortement sur la réussite dans ce protocole.

**Conséquence opérationnelle** : pendant RESCUE, prioriser les tests des comportements critiques et de l'intégrité des données, vérifier les assertions, puis contrôler les cas limites. Les outils de mutation testing et la revue indépendante sont **options avancées**, pas exigences universelles.

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

## 7.4 Revue approfondie 2026 — architecture adaptée aux agents

**Question posée :** existe-t-il une architecture démontrée plus facile à maintenir par Codex/Claude Code qu'une autre ? **Réponse : pas de classement général probant identifié dans les sources de cette consolidation.** La question doit être décomposée en localisation du code, couplage, risque de régression, effort de test et charge d'exploitation.

| Source | Résultat attesté | Ce qu'elle ne démontre pas |
|---|---|---|
| *On Coding Agent Issue Localization Accuracy* (ESEM, octobre 2026) [N02] | 2 441 corrections dans 10 projets Java ; localisation globalement meilleure au niveau package qu'aux niveaux classe et méthode | supériorité du monolithe modulaire, de Java ou d'un framework web |
| *SWE-Explore* (juin 2026) [N10] | 848 problèmes, 203 dépôts et 10 langages ; la précision aux lignes et l'efficacité du contexte restent des difficultés | classement universel des méthodes de navigation dans des projets réels |
| *Agent Retrieval Bench* (juillet 2026) [N01] | 427 exemples, 25 dépôts ; aucune famille de retrieval ne domine tout ; RepoMap a un bon rendement au budget 8K | économie directe garantie en coût API/quotas |
| OpenAI *Harness Engineering* (février 2026) [N19] | retour industriel de forte activité agentique, contraintes structurales testables, documentation repo locale, nettoyage continu | causalité isolée d'une organisation de dossiers ; transposabilité au solo developer |
| Martin Fowler *Monolith First* [S36] | argumentation d'architecture pour un démarrage monolithique dans certaines situations | expérimentation récente spécifique aux agents de code |

### Hypothèses de travail révisées

1. **Cohésion fonctionnelle.** Quand les changements d'une fonctionnalité peuvent se comprendre dans un nombre limité de modules, on s'attend à moins d'allers-retours exploratoires. **Hypothèse**, non économie de tokens chiffrée.
2. **Frontières contraignantes.** Les invariants vérifiés par l'outillage résistent mieux à la dérive que les simples interdictions en langage naturel. **Pratique industrielle** [N19], non résultat universel.
3. **Coût marginal de modification.** L'indicateur conceptuel pertinent est l'effort pour changer un comportement sans casser les autres, pas le nombre brut de fichiers, couches ou LOC.
4. **Complexité totale.** Un microservice peut réduire un couplage local mais augmenter réseau, permissions, déploiement, monitoring et traçage. L'analyse doit considérer **tous** ces coûts.
5. **Mauvais précédents.** Le code existant sert de modèle au code futur ; lorsqu'il contient des vulnérabilités, elles peuvent être propagées [N09].

### Garde-fous raisonnables selon la taille

- **Petit dépôt** : conventions simples, fonctions cohérentes, quelques tests métier, aucun outillage architectural spécial.
- **Dépôt grandissant** : routes claires, séparation I/O et calculs sensibles, carte des fonctionnalités, contrôle d'import si des frontières stables existent.
- **Grand dépôt** : dépendances explicites, analyse de cycles, contrôles structuraux en CI, ownership fonctionnel, logs vérifiables, documentation orientée parcours.

**Interdiction éditoriale** : affirmer « architecture X = −Y % de tokens » sans étude directement pertinente et comparable. Des gains observés pour un système de recherche ne peuvent être attribués à une architecture de dossiers.

## 7.5 Recommandation conditionnelle pour un grand projet JS/TS

La structure `features/<domaine>/` peut rassembler pages/queries/actions/services, avec `lib/domain/` pour la logique métier pure, `lib/db/` pour accès et migrations, `components/` pour les composants réellement transversaux, `app/` pour assembler les routes. Ce **schéma illustratif** doit être adapté à chaque framework ; ce n'est ni une norme scientifique ni une réécriture imposée.

**Critères de contrôle** : chemins d'import autorisés, présence de tests des règles métier, accès aux données centralisé quand nécessaire, validation aux frontières et absence de logique critique dupliquée. Les dépendances entre domaines ne sont interdites que si une règle métier justifie cette interdiction.

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
