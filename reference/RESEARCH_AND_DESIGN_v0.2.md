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

## 8.5 Revue approfondie — récupération de contexte et navigation

Les références [N01], [N10] et [N11] établissent qu'une part importante du travail de l'agent consiste à **localiser le code**, et pas seulement à écrire un correctif.

- **Agent Retrieval Bench** [N01] : 427 exemples, 25 dépôts, 345 positifs + 50 cas sans cible + 32 contrôles négatifs. Dans les trajectoires journalisées, les agents manquent *tous* les fichiers de référence pour **27 à 35 % des exemples**. C'est un taux propre à ce jeu de données ; ce n'est pas la part de temps perdu en production. Il n'existe **pas de méthode dominante** : les embeddings et RepoMap gagnent sur des métriques différentes, RepoMap sur le rendement sous 8 000 tokens.
- **SWE-Explore** [N10] : forte capacité de certains systèmes à localiser un fichier, précision encore plus difficile au niveau ligne et sous budget contraint.
- **CodeGrep**, publié à l'atelier REALM d'EMNLP 2026 [N11] : sur SWE-bench Verified, un récupérateur spécialisé ramène les tours de résolution de **15 %** et les tokens de **19 %** sur les instances résolues ; taux de résolution de **25,8 % à 27,0 %**, différence qui ne justifie pas à elle seule une revendication générale de performance. Le système entraîne un retriever RL 14B ; le recommander comme outil léger serait trompeur.

### Décision de navigation, niveau A

1. Partir de la demande fonctionnelle et des chemins d'entrée connus (route/page, CLI, tâche planifiée, API, test).
2. Utiliser l'index/recherche fournis par le dépôt et l'agent (`rg`, recherche de symboles, références d'IDE/LSP, historique Git) avant d'ouvrir des fichiers entiers.
3. Lire les **portions pertinentes**, puis les fichiers adjacents quand le flux l'exige ; ne pas masquer les portions nécessaires à une modification sûre.
4. Exécuter d'abord les tests **ciblés** si les dépendances sont connues, puis les contrôles plus larges en fin de changement selon le risque.
5. Mettre à jour une **carte de fonctionnalités courte** seulement lorsque les changements la rendent incorrecte.

Il ne s'agit pas de prescrire toujours moins de lecture : une modification de sécurité, de migrations ou de flux financiers exige parfois une exploration large. Le bon critère est la **pertinence du contexte**.

### Sélection d'outils existants

| Outil | Avantage plausible | Coût d'adoption / limite | Niveau |
|---|---|---|---|
| `rg` / Git / IDE/LSP natifs | instantané, contrôlable, généralement déjà disponibles | indices symboliques variables suivant l'environnement | A |
| Aider RepoMap [S27] | carte compacte des symboles ; exemple de réduction de contexte | intégration à l'agent courant à examiner, pas universelle | B |
| Serena [S26] | recherche par symboles et références, navigation LSP | serveur/installation/configuration ; vérifier langues et protocole | B/C |
| Repomix [S32] | export de sous-ensemble reproductible | peut saturer le contexte si export total | B |
| Graphes de code/MCP spécialisés [S28] | mémoire de dépendances persistante | synchronisation, confidentialité, qualité de l'index non garanties | C |
| RAG/embeddings custom | recherche sémantique | coût d'index, maintenance, fausses localisations | C |

**Principe** : une carte générée automatiquement est une *aide de navigation*, pas une vérité sur le sens métier du code. La source de vérité du comportement reste le code et les critères métier ; la documentation mémorise les intentions et les exceptions.

## 8.6 Controverse : `AGENTS.md` peut aider ou gêner

- [N03] *Evaluating AGENTS.md* (février 2026) observe, dans son protocole, une **baisse moyenne de réussite** et **plus de 20 % de coût d'inférence supplémentaire** avec des fichiers de contexte par rapport à leur absence. Les fichiers encouragent une exploration plus large et l'exécution d'instructions pas toujours utiles.
- [S01]/[N19] OpenAI rapporte qu'une documentation locale utile et des invariants mécanisés soutiennent une équipe agentique, mais il s'agit d'un **retour de production** et non d'une comparaison isolant la taille de `AGENTS.md`.
- [S02]/[N20] OpenAI recommande en septembre 2026 de **raccourcir les descriptions de skills**, **ne pas lire toutes les docs avant chaque changement** et réviser les instructions après changement de modèle.

**Conclusion retenue** : garder un `AGENTS.md` succinct contenant uniquement les commandes utiles, les contraintes spécifiques et les chemins vers les documents pertinents ; le reste est disponible *à la demande*. L'effet causal exact dépend du type de fichier, de l'agent, du modèle et des tâches. Aucun quota fixe de mots/tokens n'est établi.

### La mémoire entre sessions n'est pas la reprise intégrale de l'historique

Un nouveau fil cohérent peut éviter la répétition de résultats d'outils et de décisions périmées, mais peut aussi faire perdre une contrainte importante. Le moyen le plus simple est un **handoff minimal** : tâche, état Git, fichiers concernés, contraintes métier, tests effectués et restant, prochaine action. Pour des tâches longues, Anthropic [N18] a décrit le rôle de tels artefacts, tout en expliquant que la nécessité des resets de contexte change lorsque les modèles progressent. La remise à zéro systématique est **une pratique contextuelle, pas une règle**.

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

## 10.1 Politique v0.2 — sélectionner des skills EXISTANTS

**Décision utilisateur explicite :** le projet ne vise **pas** à inventer une nouvelle collection de skills. Il sélectionne et documente des skills déjà publiés, idéalement **officiels, reconnus, maintenus et bénéficiant d'une preuve expérimentale**. On peut écrire une courte **fiche de sélection** ou une configuration pour guider leur utilisation, mais pas présenter cette fiche comme un nouveau skill original.

Trois attributs doivent rester distincts :

1. **Officiel / crédible** : maintenu par l'éditeur d'une technologie ou une personne reconnue.
2. **Populaire / utilisé** : téléchargements, étoiles, exemples publics ; la popularité ne prouve ni l'efficacité ni la sécurité.
3. **Mesuré** : gain marginal identifié par une étude contrôlée sur certains agent–modèle–tâches ; l'effet ne se transfère pas nécessairement.

### Résultats scientifiques révisés — attention aux versions

**SkillsBench [N04]** : 86 tâches dans 11 domaines, 7 configurations agent/modèle et 7 308 trajectoires d'après l'abstrait consulté. Gain moyen de **+16,2 points de réussite** avec skills sélectionnés, mais **+4,5 points** pour le domaine *software engineering* ; 16 tâches sur 84 voient un delta négatif. Les skills générés par le modèle n'aident pas en moyenne. Ce benchmark multi-domaines ne mesure pas un catalogue général de skills de programmation.

**SWE-Skills-Bench [N05], version 2 datée du 27 octobre 2026** : **98 skills**, **3 920 évaluations appariées** sur quatre configurations et dix exigences par skill ; **92/98 n'ont pas d'effet statistiquement significatif**, **4 ont un effet positif** global, **2 négatif** global. Taux de réussite moyen **76,6 % sans skill contre 76,9 % avec skill** (**+0,3 point**, non +1,2 point). Les chiffres **49 skills / 39 sans amélioration / +1,2 %** appartiennent à **la version 1 de mars 2026** et ne doivent plus être présentés comme les résultats actuels de cet article.

Les résultats significatifs (effet **en points de pourcentage du taux de réussite** dans le protocole) :

| Skill étudié | Delta global | Interprétation et restriction |
|---|---:|---|
| `viper-configuration` | +17,69 pts | aide à employer correctement `spf13/viper` en Go ; pas pertinent hors projet Go/Viper |
| `go-testify-patterns` | +4,88 pts | tests Go, bénéfice modéré selon le benchmark |
| `junit5-testing` | +3,90 pts | tests Java JUnit 5, effet dépendant du contexte |
| `fastapi-patterns` | +3,23 pts | FastAPI ; dispersion des résultats selon configuration |
| `asyncio-patterns` | −16,96 pts | *négatif*, templates pouvant contredire la tâche |
| `grafana-dashboards` | −2,96 pts | *négatif* dans le protocole, pas interdiction générale |

L'étude rapporte aussi, pour `vitest-unit-testing`, **+41,34 points avec Codex/GPT-5.4-mini**, mais **pas** de gain global significatif. Ce cas illustre qu'un skill peut corriger une omission d'environnement dans une configuration et être inutile ailleurs. **Ne pas transformer un résultat de protocole en label permanent « prouvé pour toutes versions de Codex ».**

### Méthode de sélection sans benchmark maison

Pour chaque skill candidat, rédiger une **fiche documentaire** :

| Champ | Question à résoudre |
|---|---|
| Identité | auteur, dépôt officiel, chemin exact du `SKILL.md`, licence, version/commit revu |
| Portée | outil, langage, tâches déclenchantes, prérequis |
| Reconnaissance | auteur mainteneur, usage connu, activité du dépôt (avec date) |
| Preuves | étude indépendante, retour industriel, cas public, ou aucune donnée comparative |
| Compatibilité | Codex/Claude Code/autres, versions testées, mécanisme d'invocation |
| Surface de risque | scripts, hooks, commandes shell, réseau, lecture de secrets, packages installés |
| Coût de contexte | description chargée, ressources lues à la demande, conflits avec autres skills |
| Maintenance | dernière vérification, risques d'obsolescence et changements de version |
| Verdict | **référencer / recommander conditionnellement / étude seulement / exclure** |

**Seuil d'inclusion au catalogue** : source et utilité identifiable ; **seuil de recommandation directe** : adéquation à la stack, prérequis maîtrisés, absence de risque disproportionné et preuve ou retour technique cohérent. Si un skill est controversé ou sans preuve, il peut être **catalogué** sans être **activé**.

## 10.2 Candidats concrets déjà publics

| Source / skill existant | À quoi il sert | Nature de la preuve | Position v0.2 |
|---|---|---|---|
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) — `vercel-react-best-practices` [N24] | conventions et optimisation React/Next.js | officiellement maintenu, règles techniques ; pas de preuve indépendante de gain marginal retrouvée | **recommandable conditionnellement** sur React/Next.js |
| Vercel — `web-design-guidelines` [S20] | qualité de conception UI | source éditeur et règles, efficacité non isolée | à référencer pour les tâches UI |
| [Matt Pocock — Skills](https://github.com/mattpocock/skills) [N25] — `to-spec`, `grill-with-docs`, `improve-codebase-architecture`, `handoff` | clarification des besoins, docs métier, architecture, passation | pratiques mainteneur reconnu, pas test indépendant positif établi | catalogue / installation sélective ; certains workflows sont exigeants |
| [obra/Superpowers](https://github.com/obra/superpowers) [N26] — `systematic-debugging`, `verification-before-completion`, `test-driven-development` | diagnostic de cause, preuve avant conclusion, discipline de test | méthodes explicites et adoption open source ; effet causal de ce skill non démontré ici | référencer les skills ciblés, **ne pas activer tout le framework** |
| [anthropics/skills](https://github.com/anthropics/skills) [S47] | skills officiels d'usage de documents et workflows | provenance officielle, fiabilité dépend de chaque skill | annuaire officiel, au cas par cas |
| [Peter Steinberger — agent-scripts](https://github.com/steipete/agent-scripts) [S17] | scripts, instructions légères, automatisation d'environnement | pratique d'expert, pas une étude | référence de minimalisme, évaluer scripts individuellement |
| [Every — compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) [S24] | workflow planifier/coder/revoir/capitaliser | témoignage et code publics ; orchestration plus lourde | étude avancée, pas base START |
| [GitHub Spec Kit](https://github.com/github/spec-kit) [S21] | spécification structurée | outil existant, pas gain universel documenté | option pour gros besoins, pas défaut |
| Skills expérimentaux Golden de [N05] | configurations Go/Java/FastAPI ciblées | expérience appariée positive dans protocole identifié | recommander **uniquement** si la version exacte et la tâche concordent |

**Point de vigilance de version :** dans les dépôts vivants, les noms et contenus peuvent évoluer. Ex. le dépôt `mattpocock/skills` documente désormais des compétences `grilling` et des règles d'invocation **user-invoked** vs **model-invoked** ; un ancien prompt qui suppose `/grill-me` automatiquement déclenché serait erroné. Les fiches doivent citer un chemin et une date de revue, non seulement un nom de dépôt [N25].

## 10.3 Sécurité de la chaîne de distribution des skills

La recherche USENIX Security 2026 [N17] étudie **98 380 skills** collectés auprès de registres et identifie **157 skills malveillants confirmés**. Cela établit un risque tangible, pas un taux de danger applicable à toutes les sources.

**Checklist de provenance (simple mais obligatoire avant installation) :**

1. Ouvrir le dépôt **original**, pas un miroir anonyme ; vérifier auteur et licence.
2. Lire le `SKILL.md`, les scripts, hooks, installations et commandes déclenchées.
3. Repérer accès au réseau, secrets, shell, chemins personnels, écriture de fichiers et commandes à privilèges.
4. Vérifier que la version est compatible et que le skill ne remplace pas la demande métier par ses templates.
5. Ne pas accorder par défaut les permissions « tout autoriser » sans comprendre les conséquences.
6. Conserver un **pointeur versionné** vers l'origine ; revoir les modifications importantes et correctifs de sécurité.
7. Ne pas copier un skill dans le dépôt utilisateur sans savoir comment il recevra les mises à jour.

*How Agent Skills Evolve* [N31] analyse **84 200 skills / 750 898 commits** en novembre 2026 et souligne les difficultés de maintenance, duplication et changements liés à la sécurité. Cela justifie de **préférer des liens vers la source et une installation maîtrisée**, plutôt que de figer à jamais des copies. L'étude n'établit pas qu'une source officielle soit invulnérable.

## 10.4 Gouvernance des recommandations de skills

- **Référencer** de nombreux candidats : oui ; **en installer beaucoup** dans un projet individuel : non.
- Réexaminer les descriptions et conditions de déclenchement après mise à jour des modèles [N20].
- Éviter plusieurs skills qui contrôlent le même workflow ou imposent des instructions contradictoires.
- Privilégier un skill de domaine vérifié à un « guide universel du bon code » trop général.
- Si un outil officiel fait déjà nativement une tâche, le skill doit montrer une valeur ajoutée claire ; sinon il reste optionnel.
- **Aucun « score d'efficacité » fictif** fondé sur des étoiles GitHub ou le nombre de téléchargements.

---


# Partie VI bis — TOKEN EFFICIENCY : efficacité sans dégrader la qualité

## 10.5 Objet et définition

**RETENU (v0.2).** Ajouter **TOKEN EFFICIENCY** comme domaine transversal aux deux parcours START et RESCUE, sans créer un système de facturation ni un optimiseur propriétaire. L'enjeu est d'éviter du **travail inutile** plutôt que de sacrifier les lectures, validations ou raisonnements nécessaires.

On doit distinguer **cinq métriques** :

| Métrique | Définition | Ce qu'elle ne dit pas |
|---|---|---|
| **Tokens d'entrée bruts** | total effectivement fourni au modèle, y compris une grande partie du contexte et des résultats d'outils | ni le prix réellement payé ni la pertinence du contenu |
| **Tokens d'entrée en cache** | portion réutilisée à un tarif spécifique selon le fournisseur/API | ce n'est pas zéro token, ni nécessairement zéro quota |
| **Tokens de sortie / raisonnement** | générations et éventuels tokens de réflexion comptabilisés | ne correspondent pas directement au nombre de lignes de code produites |
| **Coût API facturé** | somme des catégories aux tarifs réels (entrées, cache read/write, sorties, options) | ne représente pas une limite d'abonnement Codex/Claude Code |
| **Coût par tâche correcte** | coût total des tentatives nécessaires pour obtenir un résultat qui passe les contrôles métier | nécessite un succès défini ; un taux de compression seul ne suffit pas |

**Sixième notion distincte** : le **quota/usage d'abonnement** (notamment Codex avec ChatGPT, ou Claude Code) dépend des règles internes et de la charge des tâches. Une économie API ne prouve **pas** une réduction proportionnelle de consommation de quota. Éviter le vocabulaire « 30 % de tokens économisés = 30 % de sessions supplémentaires » tant que le fournisseur ne le documente pas.

## 10.6 Ce que disent les études — chiffres et contextes

| Source | Protocole et résultat | Limite d'interprétation |
|---|---|---|
| *How Do AI Agents Spend Your Money?* [N13] | 8 modèles, tâches SWE-bench Verified ; variabilité jusqu'à **30×** entre exécutions d'une même tâche ; fort poids de l'entrée ; plus de tokens ne garantit pas plus de réussite | ne quantifie pas l'économie d'une configuration locale pour une application donnée |
| *TokenEconomizer* Microsoft Research [N12] | Codex, Claude Code, Copilot CLI ; contrôle black-box ; **−18,4 à −30,9 % de coût moyen en tokens** dans les configurations étudiées avec réussite comparable | plugin et résultats dépendants de versions, repos et tâches ; mécanismes expérimentaux |
| *CodeGrep* REALM 2026 [N11] | sur instances résolues SWE-bench Verified : **−19 % tokens**, **−15 % tours** avec retriever spécialisé | n'est pas un simple script à installer ; effet de sélection « instances résolues » |
| *Token Reduction Is Not Cost Reduction* [N14] | **2 848** exécutions appariées analysées ; bras à **−38 % de tokens bruts de sortie d'outils** et **+6,8 % de coût réellement facturé** | campagne sur Claude Code et modèles étudiés ; prouve la possibilité d'un contre-effet, pas l'inutilité de toute réduction |
| *An Empirical Cost Attribution of Context-Compression Gateways* [N15] | distingue filtrage de schémas d'outils, compression et résumé ; filtrage de **21K–57K tokens sur certains tours** dans leurs configurations | tokens retirés d'un prompt ≠ dollars économisés ; méthode de passerelle complexe |
| *CliffCompaction* [N16] | jusqu'à **50 % de coût en moins** sous certaines conditions de contextes longs dans Terminal-Bench et autres protocoles | prépublication et proxy sophistiqué, pas standard START |
| *Evaluating AGENTS.md* [N03] | **>20 % de coût d'inférence supplémentaire** en moyenne dans son protocole | ne condamne pas toute instruction projet minimale |

**Conclusion de recherche :** aucun gain en pourcentage ne doit être annoncé comme applicable à tous les dépôts. L'optimisation est une hiérarchie **plausible** fondée sur la théorie des outils, des études et du coût d'adoption, pas un palmarès causal sur les projets du lecteur.

## 10.7 Les coûts évitables courants dans un gros dépôt

1. **Lecture trop large** : ouvrir des fichiers entiers, générer l'arborescence complète, exporter tout le repo alors que seules quelques zones sont pertinentes.
2. **Navigation répétitive** : rechercher plusieurs fois la même relation route → service → DB à cause d'une carte de fonctionnalités absente ou inexacte.
3. **Historique de session devenu inutile** : résultats de build, logs, anciennes erreurs, code rendu obsolète par les correctifs ultérieurs.
4. **Sorties d'outils trop verboses** : tests, lint, diff ou logs retournant des milliers de lignes sans signal utile.
5. **Descriptions de skills/MCP chargées inutilement** : beaucoup d'outils et de descriptions disponibles, parfois redondantes.
6. **Boucles de correction inefficaces** : même erreur, mêmes commandes, essais successifs sans nouvelle hypothèse ni preuve.
7. **Vérifications trop larges trop tôt** : relancer l'ensemble des tests après chaque micro-édition au lieu de vérifier ciblé puis global avant livraison.
8. **Contexte difficile à transmettre** : nouvelle session sans état utile, impliquant de tout redécouvrir.
9. **Spécifications instables** : l'agent implémente le mauvais comportement, puis doit en réécrire de grandes portions.
10. **Mauvais choix de modèle/effort** : surcoût pour les tâches simples ou, inversement, échec répété avec un modèle trop faible.

Le **coût de compréhension initiale** n'est pas automatiquement du gaspillage : explorer le code peut éviter une régression. On cherche la meilleure exploration, pas un minimum dogmatique.

## 10.8 Mesures immédiatement recommandées (niveau A)

### A1. Une tâche cohérente par session — règle souple

Avant un changement de sujet important, une nouvelle conversation peut éviter de réinjecter un historique sans rapport. **Ne pas imposer** de nouveau fil pour chaque petite modification : les caches et l'état accumulé ont aussi de la valeur. Pour poursuivre un chantier interrompu, conserver un petit document de passation contenant les informations qui ne peuvent être redécouvertes facilement. Anthropic [N18] a utilisé des resets avec artefacts de transmission dans un harness long, puis les a parfois retirés avec des modèles plus capables.

**Exemple** : finir un bug d'authentification puis commencer une refonte d'export CSV = deux tâches distinctes ; corriger trois assertions du même import = une tâche cohérente.

### A2. Recherche ciblée avant lecture massive

Commencer par points d'entrée, recherche de symboles, références, tests et historique. Développer l'exploration lorsque les dépendances le justifient. Exemples de commandes illustratives si l'environnement les permet :

```bash
rg -n 'calculatePortfolio|importTransactions' src tests
rg --files | rg '(portfolio|transactions|import|test)'
git log --oneline -10 -- path/to/relevant/module
```

Ne pas intégrer les résultats d'un `rg` sur tout le dépôt comme preuve de non-utilisation : imports dynamiques, conventions de framework et appels externes existent. Voir [N01], [N10], [N11].

### A3. Réduire le bruit, préserver les preuves

Des commandes peuvent écrire leur journal complet **sur disque** et ne retourner au modèle qu'un résumé et les erreurs pertinentes. Le journal doit rester consultable, et il ne faut pas supprimer silencieusement une erreur de sécurité ou un message nécessaire à une correction.

Exemples de **stratégie** (non commandes universelles) : option quiet de pytest, affichage des tests échoués, filtrage des avertissements connus seulement après justification, sortie `--json` parsable pour certains linters ; pas de `| tail -20` comme méthode qui pourrait masquer un code retour si le shell est mal configuré.

### A4. Vérifications par étages

- Après une modification locale : test ciblé correspondant au comportement modifié.
- Avant déclaration de fin : suite plus large selon le risque et les scripts du dépôt.
- Avant migration de données ou déploiement : sauvegarde, vérification d'intégrité, plan de rollback et contrôle humain si applicable.

C'est une règle de **séquencement**, pas une autorisation de ne jamais tester le reste du projet. L'agent doit mentionner les vérifications réellement effectuées.

### A5. Instructions et skills courts

Réserver `AGENTS.md` aux chemins, commandes et exceptions ; les skills pertinents ne doivent être chargés qu'à la demande. Supprimer les instructions périmées, contradictoires et « lire tous les docs avant toute action ». Les nouveaux modèles peuvent déjà appliquer les comportements qu'un vieux prompt leur imposait [N20].

### A6. Sortir d'une boucle d'échecs par la preuve

Après plusieurs tentatives infructueuses, demander explicitement une **nouvelle hypothèse testable**, identifier ce qui a changé et arrêter les modifications aléatoires. Un protocole simple : « Reproduis, isole l'origine, propose une cause, teste-la sur une zone limitée, puis corrige ». Un nombre fixe de tentatives est une heuristique d'usage, pas une règle scientifiquement universelle.

## 10.9 Mesures conditionnelles (niveau B)

### B1. Cartes de fonctionnalités et repo maps

Pour un gros dépôt, un document court « fonctionnalité → point d'entrée → modules → tests → données » peut éviter de reproduire des recherches récurrentes. On privilégie des **index déterministes** pour les symboles et imports. Aider RepoMap et Serena sont des outils publics à examiner, pas des dépendances obligatoires [S26-S27, N01].

### B2. Désactiver les MCP/plugins réellement inutilisés

Une description d'outil peut devenir une partie répétée du préfixe du modèle. Réduire les intégrations inutiles est raisonnable, à condition de ne pas retirer un outil critique et de comprendre l'effet sur le **cache** (modification des outils = possible changement de préfixe et coût d'écriture). Le chiffre de 21K–57K de [N15] dépend fortement d'une configuration chargée de schémas.

### B3. Choix raisonné du modèle et de l'effort

Les modèles plus coûteux ne sont pas systématiquement meilleurs par dollar pour tous les travaux. Le retour OpenAI *Maintaining Software* [N21] compare différentes configurations sur un nettoyage précis et illustre un arbitrage. **Néanmoins :** choisir un modèle moins cher qui échoue deux fois peut coûter davantage qu'un modèle robuste qui réussit du premier coup. Le coût d'une tâche correcte prime sur le tarif par token.

### B4. États/handoffs réutilisables

Conserver les règles et décisions métier stables dans les documents du dépôt ; utiliser des notes de transmission sur les longues tâches, plutôt qu'un historique intégral. Éviter un système de mémoire automatique qui invente des « faits » ou oublie de supprimer une décision périmée.

## 10.10 Optimisations avancées / expérimentales (niveau C)

- **TokenEconomizer** [N12, N27] : plugin Microsoft existant ; apprend des micro-faits de dépôt, écarte les outils historiquement inutiles, repère certains cycles improductifs. **N'est pas un skill**. Compatible uniquement avec les versions d'agents listées et testées par son dépôt ; inspecter les hooks, scripts, paramètres et permissions avant usage. Les fonctionnalités ont des activations différentes ; ne pas interpréter la fourchette de publication comme un gain garanti sous un abonnement.
- **Compression automatique / proxy** [N14-N16] : gains possibles, mais risque d'effacer un détail exact indispensable (identifiants, lignes d'édition, messages d'erreur). La compression d'un log ne doit jamais déformer une chaîne servant d'ancre à un patch.
- **Routage sémantique/RAG/graphe** : potentiel sur dépôts massifs, coût d'indexation, maintenance, fausses localisations et confidentialité ; **aucun déploiement automatique** prévu.
- **Multi-agents spécialisés** : revue indépendante et séparation planification/exécution utile pour tâches longues mais parfois très chère ; Anthropic [N18] rapporte un harness qualitatif nettement plus coûteux qu'une exécution solo. Ce n'est pas un scénario général de réduction des coûts.

## 10.11 Cache API : bénéfices, contre-effets et contrat de preuve

La documentation OpenAI sur le prompt caching [N28], consultée pour cette version, précise que le cache réutilise un **préfixe identique** et peut réduire considérablement la facture des entrées mises en cache. Sur certains modèles GPT-5.6 et ultérieurs, la lecture peut être facturée à **0,1× le prix d'entrée normal**, voire **0,05×** sur des modèles énumérés, tandis que la première écriture de cache selon la durée choisie peut être facturée **1,25× ou 2,5×** en API. Ces **paramètres changent selon le modèle et la date** ; vérifier la page officielle avant toute recommandation chiffrée.

**Conséquence contre-intuitive :** compresser un historique déjà fortement caché peut réduire le nombre de tokens bruts tout en réinitialisant une partie du cache ; l'effet monétaire peut être négatif [N14, N28]. Les modèles/harness et les API ne gèrent pas tous le caching de la même manière.

### Règles API conditionnelles

1. Stabiliser les instructions et schémas communs au début du contexte quand l'API le permet.
2. Ajouter les entrées dynamiques après les éléments stables ; éviter de réécrire sans cesse un long préfixe.
3. Utiliser les compteurs réels (`cached_tokens`, éventuels `cache_write_tokens`, tarification de sortie) au lieu de déduire le coût du seul volume d'entrée.
4. Ne pas promettre qu'un cache hit est toujours garanti : modèle, paramètres, expiration et routage peuvent changer.
5. Tester l'effet financier d'une compaction **sur la métrique facturée** publiée ; ne pas utiliser une étude sur les tokens bruts pour prédire des dollars.

**Formule de principe** : `coût ≈ (entrée non cachée × prix entrée) + (lecture cache × prix lecture) + (écriture cache × prix écriture) + (sortie × prix sortie) + coûts d'outils`. Les catégories exactes sont propres au provider, et certaines API n'ont pas de tarification explicite d'écriture de cache.

### Quotas des applications / abonnements

Le fournisseur peut utiliser une allocation, des plafonds dynamiques, un compteur de messages ou une tarification interne des tâches qui n'est **pas identique** au coût API. À défaut de formule officielle publique détaillée, on ne prédit pas combien « une économie de 20 % en tokens API » ajoute de tâches Codex par semaine. On privilégie les bonnes pratiques qui **réduisent aussi le travail total** (navigation pertinente, moins de boucles d'échecs) ; c'est une hypothèse raisonnable d'amélioration du quota, pas une conversion chiffrée.

## 10.12 Ordre d'action recommandé par valeur/difficulté

| Ordre de lecture | Action | Adoption | Effet présumé | Risque principal |
|---|---|---|---|---|
| 1 | Définir clairement la tâche et les critères métier | A | éviter réécritures | sous-spécifier les cas limites |
| 2 | Recherche ciblée puis élargissement prudent | A | moins d'exploration inutile | manquer une dépendance indirecte |
| 3 | Sorties de tests synthétiques + logs complets conservés | A | contexte moins encombré | masquer une erreur si filtrage brut |
| 4 | Session cohérente + passation courte quand nécessaire | A | éviter répétition et histoire obsolète | perdre un invariant sans handoff |
| 5 | AGENTS.md/skills pertinents, pas de lecture obligatoire globale | A | moins de surcharge et contradictions | supprimer une vraie contrainte |
| 6 | Outils/MCP inventoriés et désactivés si inutiles | B | préfixe et outils plus légers | casser une fonction, perturber cache |
| 7 | Index, RepoMap, recherche symbolique complémentaire | B | gains de localisation sur gros projets | coût d'installation ou index périmé |
| 8 | TokenEconomizer / routage avancé | C | gains publiés sur certains agents | hooks, compatibilité, réversibilité |
| 9 | Compression intelligente et proxies | C | potentiel selon cache/tâches | dégradation des correctifs et facture |

Ce classement est **une proposition éditoriale qualitative**, pas le résultat d'un essai contrôlé comparant les neuf lignes.

## 10.13 Auditer la consommation de tokens sans créer de benchmark

Dans RESCUE, un audit peut être **purement descriptif** et non expérimental : inventorier le `AGENTS.md`, les skills activés, les outils MCP, les scripts bavards, les patterns de navigation, les sessions longues et les journaux d'erreur répétitifs. Il ne nécessite ni dispositif scientifique, ni collecte nouvelle de données privées, ni instrumentation complexe.

**Sortie attendue :**

- **Observation** : « la tâche lance un build complet 11 fois avant une correction locale », uniquement si une trace accessible le montre ; sinon « à vérifier ».
- **Conséquence possible** : volume de contexte/temps supplémentaire, sans conversion monétaire inventée.
- **Action simple** : exécuter un test ciblé en boucle puis le build final.
- **Risques** : test ciblé insuffisant sur changements transversaux.
- **Preuve de correction** : commandes réellement exécutées, tests verts, critères métier contrôlés.

Aucune obligation de produire des métriques personnelles ni de chronométrer des agents. **Les études externes demeurent la seule base pour les bénéfices quantitatifs généraux.**

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

# Partie VII bis — Revues croisées de la recherche (novembre 2026)

## 12.1 Dossier de recherche A — Maintenabilité et architecture des logiciels générés par agents

**Question :** une organisation logicielle réduit-elle les erreurs et les coûts de maintenance des agents sans augmenter excessivement la complexité ?

**Éléments de preuve** : [N02] mesure la localisation des changements sur des projets Java ; [N10] et [N01] examinent le repérage du contexte ; [N19] rapporte la pratique industrielle d'un dépôt agent-first ; [N09] documente la propagation de défauts existants. Ces quatre types de travaux ne mesurent **pas le même résultat**. Les regrouper en une prétendue preuve « monolithe + feature-first gagne » serait une erreur.

**Convergences plausibles :** rendre les points d'entrée faciles à identifier ; fixer les frontières qu'un agent peut enfreindre par des contrôles reproductibles ; garder le code métier isolable et testable ; éviter l'accumulation de doublons et de routes d'accès à la donnée. Une architecture conçue pour être navigable n'est pas forcément plus courte.

**Résultats contradictoires ou lacunes :** aucune comparaison robuste trouvée entre Next.js, Rails, Django, FastAPI+React et SvelteKit sur des tâches homogènes avec des agents récents. Les différences de stack, compétences humaines, cadre de tests et taille de projet créent des confusions. L'exemple OpenAI représente un investissement organisationnel sans commune mesure avec un site de petite entreprise.

**Décision** : conserver *monolithe simple/modulaire + regroupement par fonctionnalité* comme **hypothèse de départ** sous conditions, **pas** dogme. Passer aux contrôles d'architecture lorsque des dépendances mal maîtrisées apparaissent. Pour RESCUE, réparer en priorité les limites dangereuses plutôt que changer de framework.

**Ce qui invaliderait la recommandation** : une publication multi-repos comparative démontrant, à complexité et qualité comparables, une meilleure maintenabilité IA d'un autre découpage ou un contre-exemple concret où la configuration proposée complique inutilement le projet.

## 12.2 Dossier de recherche B — Contexte, documentation et localisation

**Question :** quels artefacts persistent d'une session à l'autre sans créer du contexte inutile ?

**Éléments de preuve** : [N03] montre que des fichiers de contexte peuvent augmenter coût et exploration sans améliorer la réussite ; [N20] recommande de réduire les descriptions de skills ; [N01] observe les échecs de récupération de bons fichiers ; [N11] montre qu'un retriever spécialisé peut réduire des explorations dans un benchmark ; [N28] établit qu'un historique stable peut bénéficier d'un cache API.

**Tension centrale :** *moins de contexte brut* peut réduire la charge d'un modèle, mais *un contexte mieux organisé* peut prévenir les erreurs. Le cache peut aussi rendre une répétition moins chère qu'une compression imprécise. Il faut donc distinguer :

- **Navigation** : où se trouve le code ? → index/symboles/repomap.
- **Intentions** : pourquoi cette règle existe ? → documentation métier/ADR.
- **Contraintes globales** : quelles commandes et interdictions sont constantes ? → `AGENTS.md` court.
- **État temporaire** : quelle tâche et quels tests restent ? → handoff ciblé.

**Décision** : quatre couches documentaires de la v0.1 maintenues, avec lecture progressive. Les cartes sont révisées lors de modifications pertinentes et les index techniques sont de préférence régénérés par des outils déterministes.

**Limite** : un dépôt très petit n'a pas besoin d'un inventaire des symboles, encore moins d'une base de recherche vectorielle. Une documentation obsolète peut être pire que son absence lorsqu'un agent la traite comme source de vérité.

## 12.3 Dossier de recherche C — Vérification, QA et confiance

**Question :** comment détecter les erreurs produites par des agents lorsque l'utilisateur ne lit pas toutes les lignes de code ?

Les sources [N07], [N08], [N06] et [N18] traitent des **dimensions différentes** : qualité syntaxique des assertions, couverture de modifications, interaction de spécification, capacité d'un évaluateur à exercer l'application. Elles convergent sur une faiblesse pratique : une implémentation peut sembler satisfaisante sans avoir prouvé qu'elle réalise le bon comportement.

**Doctrine en trois preuves :**

1. **Preuve d'intention** : ce que l'utilisateur veut, les données et invariants concernés, les critères observables.
2. **Preuve technique** : tests, lint, typage, build, revue de configuration ou de dépendances réellement exécutés.
3. **Preuve d'usage** : parcours réel (manuel ou Playwright si justifié) et comparaison des sorties/états aux critères métier.

**Limite des tests générés** : le modèle peut écrire une implémentation et un test contenant la même hypothèse incorrecte. Si le test est conçu pour valider seulement le comportement du code qu'il vient d'écrire, il ne garantit pas l'exigence originale. Pour les systèmes à risque, demander au moins un contrôle à partir d'exemples métier établis indépendamment.

**Moyens optionnels** : tests de mutation, fuzzing ciblé, revue indépendante, snapshots explicites, Playwright, audit de sécurité spécialisé. **Pas d'obligation par défaut** de monter un second agent critique ou un harness multi-étapes ; [N18] rappelle le coût important de ces dispositifs.

**Critère final** : réussite métier, intégrité des données, sécurité et limites résiduelles explicitement rapportées — pas simple pourcentage de couverture ou compteur de tests verts.

## 12.4 Dossier de recherche D — Économie des tokens, coûts et cache

**Question :** économise-t-on de l'argent en réduisant le texte envoyé à un agent de code ?

**État des preuves** : [N13] démontre la variabilité de la consommation et l'absence de lien monotone entre volume et exactitude. [N12] présente un contrôleur externe capable de faire baisser les coûts dans plusieurs configurations. [N11] relie une récupération de fichiers ciblée à des gains de tokens *sur les instances résolues*. [N14] montre au contraire qu'une compression de sorties peut augmenter la facture. [N28] explique la logique et les tarifs de cache.

**Leçon de méthode** : les coûts *par trajectoire* et surtout *par tâche correcte* sont plus pertinents que le pourcentage de caractères supprimés. Une compaction, un routeur ou un second modèle peuvent eux-mêmes consommer des tokens. Les gains publiés doivent inclure ces frais quand l'étude les mesure.

**Décision** : adopter les pratiques « low-tech » immédiatement (tâches claires, navigation ciblée, sorties de commandes maîtrisées, contexte utile, lutte contre les boucles) ; n'activer plugins ou proxies de réduction que sur version compatible et compréhension des limites. Le référentiel ne promet **aucune économie forfaitaire**.

## 12.5 Dossier de recherche E — Skills utiles versus skills populaires

**Question :** faut-il accroître le nombre de skills installés pour accroître la réussite des agents ?

**Réponse du corpus étudié : non, pas de relation universelle démontrée.** [N04] constate des gains appréciables pour des skills sélectionnés multi-domaines, mais plus faibles en software engineering. [N05] v2 rapporte 92/98 skills sans effet statistiquement significatif sur ses tâches. [N17] documente les risques de distribution malveillante ; [N31] examine l'évolution et la redondance.

**Décision** : cataloguer les meilleurs skills **existants** et évaluer leurs preuves sans les réécrire. Le projet peut être très riche comme **bibliothèque de choix**, mais chaque projet utilisateur reste léger.

## 12.6 Pièges de lecture des publications — obligatoire dans les fiches

- **Corrélation / causalité** : un dépôt avec AGENTS.md n'a pas nécessairement de meilleures performances *à cause* du fichier.
- **Prépublication / version révisée** : utiliser la version datée effectivement lue (exemple [N05] v2 du 27/10/2026).
- **Succès observé / succès attribué** : une hausse de 1,2 point sur un benchmark n'est pas automatiquement statistiquement établie.
- **Score / comportement utile** : précision de localisation, qualité des tests, réussite finale et coût ne se remplacent pas.
- **Sous-groupe** : « tokens sur les instances résolues » ne dit pas le coût de toutes les tentatives.
- **Tokens comptés / prix** : entrée cachée, sortie et écriture de cache peuvent suivre des tarifs différents.
- **Versions changeantes** : un skill ou plugin peut évoluer après l'étude et devenir inefficace, dangereux ou incompatible.
- **Étude de laboratoire / usage produit** : un protocole sur GitHub public ne se transporte pas directement à une application locale avec données sensibles.
