# 04 — Revue critique de la recherche et des publications techniques

**Revue complémentaire : 14 novembre 2026.** Ce document condense les sources nécessaires aux **décisions d'implémentation**. Pour l'intégralité des références identifiées depuis le début du projet, voir `reference/BIBLIOGRAPHIE_HISTORIQUE_v0.2.md` et `reference/RESEARCH_AND_DESIGN_v0.2.md`. Les deux niveaux sont volontairement séparés pour éviter d'injecter 80 sources au contexte de Codex à chaque modification.

## 1. Politique de preuve et lecture critique

- **E — Étude empirique** : protocole, tâche, modèles et limites explicités. Une prépublication arXiv n'est pas nécessairement évaluée par les pairs.
- **I — Retour industriel** : forte valeur pratique, mais environnement particulier, biais commerciaux/échantillonnage possibles.
- **O — Documentation officielle** : preuve qu'une interface ou fonctionnalité existe, **pas** preuve qu'elle améliore les performances.
- **G — Dépôt GitHub/pratique** : source de code ou d'idée ; sa popularité/étoiles ne mesure pas un gain de qualité/tokens.

**Aucune généralisation abusive :** qualité par tâches résolues, coût par résolution et régressions ont priorité sur un simple « -X % de tokens ». Maintenir l'incertitude et la date de révision. Les gains de performance ne sont pas promis aux utilisateurs de VCR.

## 2. Les études structurantes : architecture et harness

**[R01] OpenAI — Harness engineering: leveraging Codex in an agent-first world** (11 fév. 2026, I).  
URL : https://openai.com/index/harness-engineering/  
**Constat source :** produit développé par Codex, forte importance du dépôt comme source de connaissance, architecture contrôlée, validation automatisée, lisibilité du code, boucles de feedback et suppression de complexité. L'équipe annonce une très forte productivité dans son contexte.  
**Transposition VCR :** `AGENTS.md` sommaire ; règles importantes exécutables ; trace de preuves ; architecture observée ; maintenance continue ; rapport contrôlé.  
**Limite :** retour d'une équipe particulière avec des moyens spécifiques, **aucune supériorité démontrée de Next.js/TS**.

**[R02] OpenAI — Maintaining software with the GPT-6 family** (14 oct. 2026, I).  
URL : https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family  
**Constat source :** opérations de nettoyage de code à grande échelle avec vérification d'usage réel, exclusions métier, projets de PR et relectures ; attention aux faux positifs, flags et mécanismes de sécurité. Plusieurs améliorations mesurées de CI, mais dans leur infrastructure.  
**Transposition :** RESCUE doit recueillir une preuve **avant** toute suppression ; exclure killswitches, usages dynamiques ; proposer de petites corrections et non un big-bang.

**[R03] OpenAI — Rethinking skills and prompts for GPT-6 Astra** (11 sept. 2026, I/O).  
URL : https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra  
**Constat :** les modèles récents peuvent moins nécessiter certaines instructions anciennes ; des skills trop génériques et des prompts trop chargés peuvent être contre-productifs.  
**Transposition :** revue régulière d'AGENTS/skills ; pas de surcharge documentaire.

**[R04] Barbaste et al. — Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems** (arXiv 2609.00006, juil. 2026, E descriptive).  
URL : https://arxiv.org/abs/2609.00006  
**Constat source :** analyse du code de onze harness (Claude Code, Codex, Gemini CLI, Aider, OpenHands, OpenCode, etc.), sept sous-systèmes et 29 patterns. Dans cet échantillon de production, la recherche de code ne reposait pas sur des embeddings vectoriels ; les boucles et la navigation étaient principalement déterministes.  
**Transposition :** ne pas construire un RAG par réflexe, séparer exécution/outils/contexte/état/sécurité/évaluation ; préférer un adaptateur simple.  
**Limite :** photographie des systèmes étudiés à une date donnée ; ne prouve pas qu'un RAG ne serait jamais bénéfique.

**[R05] Martin Fowler — Monolith First** (essai technique, I/opinion).  
URL : https://martinfowler.com/bliki/MonolithFirst.html  
**Transposition :** monolithe simple/modulaire comme candidature conditionnelle, pas dogme ou comparaison expérimentale agentique.

**[R06] ESEM 2026 — On Coding Agent Issue Localization Accuracy: An Exploratory Study** (conférence, E).  
URL : https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.59  
**Constat :** difficulté accrue à localiser la bonne méthode précise, même quand une zone générale est identifiée.  
**Transposition :** réduire le nombre de trajets entre modules et fournir des points d'entrée vérifiables.

## 3. Acquisition de contexte et navigation

**[R07] Qin & Xie — Agent Retrieval Bench** (arXiv 2607.24882, juil. 2026, E).  
URL : https://arxiv.org/abs/2607.24882  
**Résultats :** 427 cas, 25 dépôts ; aucune famille de récupération n'est meilleure partout. RepoMap obtient le meilleur rendement du contexte parmi les options comparées avec budget 8k tokens ; les méthodes vectorielles gagnent sur d'autres métriques ; les trajectoires observées peuvent manquer tous les fichiers pertinents dans 27–35 % des cas.  
**Transposition :** recherche lexicale/symbolique d'abord, maps compactes optionnelles, embeddings seulement avec problème de rappel documenté.  
**Limite :** récupération de contexte != réussite finale de correction.

**[R08] Chen et al. — CodeGrep** (ACL REALM 2026, étude atelier).  
URL : https://aclanthology.org/2026.realm-1.80/  
**Résultats :** −19 % de tokens et −15 % de tours sur instances résolues dans le protocole, sans dégradation significative de réussite.  
**Transposition :** dépenser moins à localiser le bon fichier ; nous ne reproduisons pas l'agent spécialisé RL de recherche dans P0.1.

**[R09] Zhang et al. — SWE-Explore** (arXiv 2606.07297, E prépublication).  
URL : https://arxiv.org/abs/2606.07297  
**Transposition :** la recherche de code mérite un statut de première classe dans l'audit de maintenabilité IA.

**[R10] Gloaguen et al. — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?** (arXiv 2602.11988, E).  
URL : https://arxiv.org/abs/2602.11988  
**Résultats :** coût d'inférence >20 % supérieur et tendance à une baisse de réussite dans les protocoles étudiés avec fichiers contextuels surchargés.  
**Transposition :** instructions minimales utiles et liens vers les docs, pas encyclopédie.  
**Limite :** ce travail n'invalide pas toutes les consignes spécifiques.

**[R11] Khatri — Do Context Files Help Coding Agents? A Two-Agent Ablation Study** (REALM 2026, E atelier).  
URL : https://aclanthology.org/volumes/2026.realm-1/  
**Constat :** pas de gain mesurable de réussite sous le protocole publié ; contribue à la controverse AGENTS.md.  
**Transposition :** garder les hypothèses ouvertes ; préférer des instructions strictement opérationnelles.

**[R12] Anthropic — Effective context engineering for AI agents** (2025, I).  
URL : https://www.anthropic.com/research/effective-context-engineering-for-ai-agents  
**Transposition :** contexte comme ressource limitée, documents chargés à la demande, pertinence > quantité.

**[R13] Aider — Repository Map** (O/G).  
URL : https://aider.chat/docs/repomap.html  
**Transposition :** exemple de carte de symboles compacte ; pas d'obligation d'adopter l'outil Aider lui-même.

## 4. Définition du besoin, tests et risque d'erreur

**[R14] SWE-Journey** (arXiv 2610.11559, oct. 2026, E).  
URL : https://arxiv.org/abs/2610.11559  
**Constat :** sur tâches de développement prolongées, les interactions avec un utilisateur capable de spécifier clairement les besoins sont beaucoup plus efficaces que celles où l'intention reste vague.  
**Transposition :** START doit produire critères métier et exigences testables en langage ordinaire, sans noyer le débutant dans le jargon.

**[R15] Sun et al. — SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering?** (Findings of ACL 2026, juillet 2026, E conférence).  
URL : https://aclanthology.org/2026.findings-acl.1976/  
Code : https://github.com/Sunny4Coding/SWE-Mutation  
**Constat :** 2 636 variantes mutées construites sur 800 instances ; les tests générés par modèle peuvent laisser passer des implémentations volontairement erronées.  
**Transposition :** ne pas considérer « tests verts » comme preuve suffisante de couverture des chemins critiques ; juger le pouvoir discriminant des assertions. Les taux expérimentaux ne constituent pas le taux d’erreur moyen de tous les tests IA.

**[R16] Banik et al. — All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code** (arXiv 2606.18168, E prépublication).  
URL : https://arxiv.org/abs/2606.18168  
**Constat :** beaucoup de modifications de tests générées par agent portent des signaux de vérification faibles ou absents selon la classification de l'étude.  
**Transposition :** demander « quel bug ce test détecterait-il ? », pas seulement « est-ce qu'il passe ? ».

