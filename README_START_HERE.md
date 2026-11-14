# Vibe Coding Reference — dossier de lancement Codex

> **Document historique de cadrage.** Le prototype existe désormais : pour le découvrir et l’essayer, consulter le [README actuel](README.md). Pour l’avancement et les limites vérifiées, voir [IMPLEMENTATION_STATUS.md](docs/IMPLEMENTATION_STATUS.md). Les instructions de création ci-dessous décrivent le lancement initial du projet.

**Version :** brief prototype P0.1 · **Date de consolidation :** 14 novembre 2026  
**Nature :** spécification et plan d'implémentation, **pas** un logiciel déjà développé.

## Objectif en une phrase

Créer un dépôt open source **local-first** qui permet à une personne développant avec Codex/Claude Code de **bien démarrer (START), auditer et réparer sans risque (RESCUE), et faire remonter des possibilités d'amélioration (IMPROVE)**, tout en réduisant les dépenses de contexte et de tokens lorsque cela ne nuit pas à la réussite.

## D'abord lire ces fichiers — cet ordre est volontaire

1. `prompts/01_CODEX_BOOTSTRAP.md` : prompt prêt à donner à Codex ; définit sa mission et ses restrictions.
2. `docs/01_VISION_ET_DECISIONS.md` : vision, périmètre, exigences et arbitrages.
3. `docs/02_ARCHITECTURE_ET_CONTRATS.md` : architecture cible, formats de données, sécurité et UX.
4. `plans/03_BACKLOG_ET_LIVRAISON.md` : séquence de développement, cas d'acceptation, conditions de livraison.
5. `docs/04_RECHERCHE_ET_SOURCES.md` : publications scientifiques, dépôts, preuves, limites et liens exacts.
6. `docs/05_PROJETS_EXTERNES_ET_SKILLS.md` : comment évaluer et intégrer **sans recopier** des outils tiers.
7. `docs/06_PLAYBOOKS_ET_AUDITS.md` : scénarios complets START, RESCUE, IMPROVE, TOKEN EFFICIENCY.
8. `reference/RESEARCH_AND_DESIGN_v0.2.md` : document historique complet (1673 lignes), **référence de fond**, à consulter à la demande ; ne pas injecter en entier dans chaque tâche.
9. `reference/RESEARCH_AND_DESIGN_v0.1.md` : historique de cadrage, si une décision doit être retracée.

Les anciens documents v0.1/v0.2 ne sont **pas** des instructions d'implémentation exécutables. En cas de contradiction, privilégier **le présent dossier daté du 14/11/2026**, puis demander confirmation si la décision implique un risque réel.

## Les quatre modes visibles par l'utilisateur

| Mode | Ce que l'utilisateur doit comprendre | Travail réel de l'agent | Risque par défaut |
|---|---|---|---|
| START | « Aide-moi à choisir et préparer mon projet » | questionnaire court, proposition conditionnelle, configuration minimale, critères métier | Conseil seulement |
| RESCUE | « Analyse mon application et montre-moi les vrais problèmes » | collecte de preuves, exécution bornée de contrôles autorisés, rapport avec gravité et correctifs | Lecture/analyse sans modification du dépôt cible |
| IMPROVE | « Repère ce qui rend les prochaines sessions IA difficiles » | constats de répétitions, dette de contexte, documentation, outils, propositions avec risques | Proposition uniquement, jamais auto-mutation |
| TOKEN EFFICIENCY | « Où sont mes gaspillages et comment les corriger ? » | analyse de traces fournies volontairement, distinction coût/tokens/quota, pistes priorisées | Aucune surveillance implicite |

`TOKEN EFFICIENCY` peut être un onglet d'IMPROVE ; ce n'est **pas** un service de facturation ni une promesse d'économies.

## La stratégie pour un premier prototype « complet » mais réaliste

**Un parcours vertical de bout en bout fonctionnel avant d'ajouter 20 intégrations.** Le prototype doit pouvoir :

- analyser un dépôt **TypeScript/Next.js ou Python**, avec dégradation propre si le framework est inconnu ;
- produire une sortie **Markdown + JSON + éventuellement un HTML statique local** ;
- montrer des **preuves contrôlables** (fichier, ligne, commande, extraits anonymisés si nécessaire) ;
- séparer `confirmed`, `suspected`, `not_checked` et `not_applicable` ;
- transformer les conclusions en **actions proposées** que l'utilisateur peut accepter/rejeter ;
- afficher les règles de prudence : jamais de réécriture automatique, aucun secret dans les rapports, aucune publication sans accord ;
- se lancer avec un **point d'entrée local simple**, un mode interactif en terminal ou des prompts prêts à coller dans Codex ;
- avoir des **tests fonctionnels sur dépôts fixtures** et une documentation utilisateur en français ;
- pouvoir expliquer clairement quelles détections sont automatiques et quelles conclusions nécessitent l'IA ;
- fonctionner **sans modèle/API ajouté** : on utilise le Codex/Claude Code déjà en place ; aucun envoi externe par le logiciel lui-même en mode de base.

## Instructions d'utilisation immédiate avec Codex

1. Créer un dépôt local vide, par exemple `vibe-coding-reference`.
2. Placer **tout le contenu de ce dossier** dans le dépôt. Ne pas confondre ce dossier documentaire avec le petit prototype ZIP précédent.
3. Ouvrir ce nouveau dépôt dans Codex.
4. Copier le contenu de `prompts/01_CODEX_BOOTSTRAP.md` dans une **session neuve**.
5. Demander à Codex de commencer par le **lot 0** puis le **lot 1** du backlog ; poursuivre dans de nouvelles sessions en s'appuyant sur le journal d'avancement. Ne pas envoyer aveuglément l'intégralité de la bibliographie au contexte à chaque tour.

## Points non négociables

- **Pas de benchmark maison de performance/tokens** : seulement des tests fonctionnels du prototype et la synthèse critique d'études existantes.
- **Pas de nouveau modèle ni nouvel agent de code** : utiliser les agents déjà présents.
- **Pas de création d'un catalogue de skills maison** : sélectionner, référencer et vérifier des skills existants. Les prompts de workflow de VCR ne sont pas présentés comme des « skills validés ».
- **Pas d'intégration automatique de Google Harness², RAG, LangGraph, TokenEconomizer, Serena ou autres**, malgré leur intérêt : plugins optionnels avec contrôle de compatibilité et de permissions.
- **Aucune modification non approuvée** de la base auditée ; aucune suppression de fonctionnalités métier sans accord.
- **Ne jamais déclarer un gain de tokens ou une amélioration de fiabilité sans l'attribuer au protocole exact d'une source publiée.**

## Définition de réussite de la première version

Une personne non développeuse doit pouvoir analyser un dépôt exemple, comprendre les 3 à 5 vrais constats importants, retrouver leur preuve et décider quoi faire ensuite **sans lire le code de l'outil VCR**. Une personne expérimentée doit pouvoir inspecter les vérificateurs, enrichir les règles, reproduire les résultats et désactiver chaque mécanisme. Le tout sans service permanent ni infrastructure cloud obligatoire.
