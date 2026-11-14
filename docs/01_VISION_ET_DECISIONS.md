# 01 — Vision, objectifs produit et décisions de conception

**Document normatif pour le prototype.** Il met à jour la référence documentaire v0.2 créée le 12 novembre 2026 : ce qui était auparavant « hors périmètre : application / CLI » devient **un très petit outil local optionnel** pour rendre les procédures accessibles, **pas** un SaaS, un nouvel agent ou une grosse plateforme. Conserver la distinction.

## 1. Problème utilisateur

Les développeurs débutants ou « vibe coders » capables de générer une application complète par IA ne savent pas toujours :

- si le produit respecte réellement son besoin métier ;
- si le dépôt est sûr, maintenable, évolutif et testable ;
- où se trouvent les problèmes qui feront consommer inutilement des tokens aux agents futurs ;
- quelles corrections méritent d'être faites, dans quel ordre, avec quels risques ;
- si une recommandation vient d'une étude empirique, d'un retour industriel ou d'une simple préférence ;
- comment installer seulement les outils appropriés, sans transformer un projet simple en usine à gaz.

**Promesse :** « L'agent rend visibles les problèmes importants, leurs preuves et les décisions possibles, sans ajouter de complexité gratuite. »

**Différenciation :** ce n'est ni un cours généraliste de Harness Engineering (Walking Labs existe), ni un wrapper de Codex, ni un moteur de recherche de code concurrent de Serena, ni un nouveau framework multi-agent. C'est un **dispositif d'orientation, de diagnostic et d'amélioration contrôlée**, agnostique du modèle et de la stack, étayé par la recherche.

## 2. Utilisateurs et situations

**U1 Débutant** — souhaite lancer une application. Fournit un descriptif simple. Reçoit questions essentielles, choix de stack conditionnels, risques évidents, critères d'acceptation compréhensibles, setup minimal reproductible.

**U2 Développeur amateur intensif en IA** — possède un projet de 100 à 1 000 fichiers, devenu difficile à modifier. Reçoit carte fonctionnelle et audit RESCUE ; voit preuves, gravité, stratégie de réparation et limites ; ne reçoit pas un « score de qualité 3/10 » arbitraire.

**U3 Mainteneur** — veut un audit ciblé sécurité, tests, migration ou performance. Peut configurer domaines, outils et chemins ; reçoit JSON structuré + Markdown + vérificateurs reproductibles.

**U4 Usage intensif de Codex** — veut expliquer l'inflation de contexte. Reçoit suggestions sur sessions, navigation, sorties de commandes, outils/plugins, cache et étapes échouées, sans chiffres inventés.

**U5 Créateur d'un harness** — veut une amélioration continue : lit un journal d'incidents et approuve les propositions de modification d'instructions, de tests ou de cartes. Aucune boucle d'auto-édition incontrôlée.

## 3. Capacités à exposer

### START
- Accepter une description en langage courant, puis poser uniquement les questions qui changent matériellement le design.
- Séparer *produit / données et sécurité / exploitation / stack / architecture / contrôles*. Ne jamais comparer « Python » à « Next.js » comme s'il s'agissait du même niveau.
- Fournir 1 à 3 options de stack lorsque pertinent, avec avantages, inconvénients, coût opérationnel et hypothèses.
- Générer une **spécification d'intention** et une **checklist de validation métier** ; ne pas déployer.
- Proposer des fichiers de démarrage minimaux sans imposer Docker, Postgres, Redis, Playwright ou RAG.

### RESCUE
- Audit d'abord **non destructif**. Reconnaître que certains outils supposés « lecture seule » peuvent créer des caches/logs ; utiliser un répertoire isolé ou demander l'accord avant ces outils.
- Scanner : git/sauvegardes ; configuration ; structure ; imports ; tests ; build ; dépendances ; sécurité ; API ; données ; documentation ; UX métier si observable ; exploitabilité.
- Séparer signaux heuristiques de constats confirmés. Ne jamais déduire l'inutilité fonctionnelle d'un simple import absent.
- Retourner KEEP, REFACTOR, PARTIAL REBUILD ou REBUILD sur des **preuves**, sans forcer une reconstruction.
- Aucun patch automatique en RESCUE : créer ensuite une **proposition de réparation** et laisser une session d'implémentation approuvée agir sur une branche.

### IMPROVE
- Recueillir les anomalies **spécifiquement choisies** par l'utilisateur : recherches répétitives, échecs des tests, navigation coûteuse, duplication, instructions obsolètes, longues séquences de prompts, risques de sécurité, migrations à chaque lecture, fichiers-centres, etc.
- Recevoir en entrée un rapport RESCUE, des résultats de contrôles, ou des traces de sessions **volontairement importées**.
- Générer un registre des problèmes récurrents et un **plan d'amélioration du harness** : preuve → hypothèse de cause → solutions alternatives → coût de maintenance → risque → geste d'approbation.
- Proposer éventuellement un diff de documentation/AGENTS/CI, mais **jamais appliquer automatiquement** dans P0.1.
- Les recommandations nouvelles doivent pouvoir être **ignorées** ou marquées `false_positive` ; l'agent n'a pas pour objectif de remplir le rapport artificiellement.

### TOKEN EFFICIENCY
- Ne pas confondre volume de tokens, prix API, tokens cache read/write, coût par issue résolue ni quota d'abonnement.
- Diagnostiquer par symptômes : trop de fichiers lus ; commandes très bavardes ; contextes réutilisés hors sujet ; prompts récurrents ; boucles d'échec ; trop de plugins ; retours de résultats complets ; documentation chargée d'office.
- Distinguer les **mesures** présentes dans un journal importé des suppositions fondées sur le dépôt.
- Priorité à la réduction des explorations et des outils inutiles, sans sacrifier les preuves nécessaires.
- Aucune télémétrie distante ni accès automatique aux historiques privés de Codex/Claude.

### RESEARCH / CATALOGUE
- Index de ressources : études, GitHub, standards, guides, avec dates, niveau de preuve, applicabilité, limites, mainteneur, licence, version et revue.
- Les sources référencées ne sont pas garanties sûres ni meilleures par leur popularité.
- Ne télécharger, cloner ou installer aucun code tiers simplement parce qu'il figure au catalogue.

## 4. Niveaux de complexité

| Niveau | Livré et activé | Exemple |
|---|---|---|
| **A — Base** | Oui, en P0.1 si applicable | git, lecture ciblée, rapports, garde-fous, tests légers, docs courtes |
| **B — Optionnel** | Seulement sur validation et compatibilité | Dependency Cruiser, lint frontières, Serena, Playwright ciblé, TokenEconomizer |
| **C — Recherche** | Documenté, expérimentation isolée possible | graphes persistants, embeddings/RAG, orchestration LangGraph, Harness², auto-optimisation |

**Règle d'architecture :** la complexité peut être importante *en arrière-plan* si elle produit un bénéfice réellement utile ; les éléments non prouvés ou potentiellement risqués restent derrière un interrupteur et un guide de décision.

## 5. Principes impératifs

1. **Local-first et offline-first** : la V0 ne doit pas envoyer de code ni de données vers un nouveau service. L'agent déjà utilisé par l'utilisateur conserve ses propres conditions d'accès au modèle.
2. **Non-destructif** : distinguer `inspect`, `propose`, `apply` ; seul `apply` (P1+) peut modifier après validation. Interdire toute action susceptible de détruire des données ou modifier le dépôt cible en analyse par défaut.
3. **Traçabilité** : chaque finding cite sa provenance, ses preuves, les vérifications exécutées et les limites ; aucune « hallucination de ligne ».
4. **Mêmes faits, plusieurs rendus** : le JSON est l'artefact machine ; Markdown/HTML en sont des vues. Ne pas coder séparément deux diagnostics.
5. **Économie de contexte** : `AGENTS.md` court, guides à la demande, commandes courtes, aucun chargement obligatoire des documents historiques complets.
6. **Reproductibilité** : exécuter les tests fonctionnels sur fixtures ; stocker versions et commandes des outils ; pas de chiffres de gains auto-déclarés.
7. **Compatibilité progressive** : TS/JS et Python d'abord, règles de fallback pour les autres stacks ; pas de garantie de couverture universelle.
8. **Risque d'outil tiers** : provenance, licence, code, permissions, dépendances, version compatible et politique de rollback avant installation.
9. **Prendre au sérieux le métier** : préserver imports complexes, règles de calcul, killswitches, fonctions de secours et données même lorsque leur code semble « mort ».
10. **Droit de ne rien changer** : un bon rapport peut conclure KEEP et zéro problème critique.

## 6. NON-OBJECTIFS en P0.1

- Construire un chat, un nouveau modèle, un agent planificateur universel ou un service cloud.
- Refaire Next.js, FastAPI, Serena, Aider, LangGraph, Harness², RepoAgent ou des skills communautaires.
- Analyser automatiquement des conversations privées ou des historiques de sessions sans autorisation explicite.
- Faire tourner un agent la nuit, lancer un cron, surveiller les comptes GitHub ou publier des PR sans accord.
- Réécrire un projet existant ou supprimer des « fichiers inutiles » automatiquement.
- Publier des chiffres de performance de notre propre méthode : **pas de benchmarks de productivité/tokens maison** ; les tests produits sont autorisés pour vérifier qu'ils fonctionnent.

## 7. Décisions éditoriales et statut

