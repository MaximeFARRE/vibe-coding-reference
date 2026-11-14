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

**[R17] Test Coverage Analysis of Agentic Pull Requests** (arXiv 2607.18057, E).  
URL : https://arxiv.org/abs/2607.18057  
**Transposition :** signaler trous de tests sur API, transactions et code modifié ; la couverture n'est pas à elle seule un score de sûreté.

**[R18] Sun et al. — Coding Agents Propagate Vulnerabilities in Code Bases** (arXiv 2611.11455, 8 nov. 2026, E).  
URL : https://arxiv.org/abs/2611.11455  
**Constat :** les agents peuvent reproduire des vulnérabilités voisines, même avec des consignes générales de sécurité.  
**Transposition :** un harness doit contrôler les mauvaises conventions héritées par des tests et règles explicites. Résultats limités aux tâches/frameworks de l'étude.

**[R19] Anthropic — Harness design for long-running application development** (24 mars 2026, I).  
URL : https://www.anthropic.com/research/harness-design-long-running-apps  
**Transposition :** plans, validations indépendantes et états de passation utiles pour tâches longues ; ne pas imposer son coût multi-agent à tous les projets.

**[R20] OpenAI — Iterating Development Workflows with Codex** (3 août 2026, O/recette).  
URL : https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex  
**Transposition :** les fichiers de contrat et de logs par phase sont des conventions optionnelles ; l'utilisateur doit approuver les changements de secrets, infra, commits, pushes, déploiements et branch switching.

## 5. Skills : bénéfices, non-bénéfices et sécurité

**[R21] SkillsBench** (arXiv 2602.12670, E).  
URL : https://arxiv.org/abs/2602.12670  
**Résultats de la version consultée en v0.2 :** gain moyen positif sur tâches variées, plus modeste sur développement logiciel.  
**Transposition :** compétences spécialisées plausibles, aucun gain universel.

**[R22] SWE-Skills-Bench v2** (arXiv 2603.15401v2, révisée 27 oct. 2026, E).  
URL : https://arxiv.org/html/2603.15401v2  
**Résultats :** 98 skills étudiés ; 92 sans effet statistiquement significatif, 4 utiles et 2 nuisibles dans les conditions évaluées ; variation selon les modèles. Les chiffres de la première version de mars **ne doivent plus être présentés comme les résultats courants**.  
**Transposition :** catalogue de skills existants avec source/version et preuves **individuelles** ; popularité != efficacité. Le benchmark n'autorise pas à dire que tous les skills non significatifs sont inutiles.

**[R23] USENIX Security — “Do Not Mention This to the User”: Detecting and Understanding Malicious Agent Skills in the Wild** (2026, E conférence).  
URL : https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi  
**Résultats rapportés :** 157 skills malveillants confirmés dans 98 380 skills étudiés.  
**Transposition :** revue des scripts, droits et provenance avant installation ; aucun « installer tous les skills ».

**[R24] Agent Skills Specification** (O).  
URL : https://agentskills.io/specification  
**Transposition :** un format de packaging commun, pas une preuve que tous les agents activent les skills à l'identique.

## 6. Consommation des tokens et coûts réels

**[R25] Microsoft Research — TokenEconomizer** (oct. 2026, E/I).  
URL publication : https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/  
URL code : https://github.com/microsoft/TokenEconomizer  
**Résultats :** réduction de 18,4 à 30,9 % du coût moyen sur cinq combinaisons agent-modèle étudiées, avec efficacité de résolution au moins comparable dans l'étude ; mécanismes = petites informations persistantes, suppression des outils non utilisés, intervention sur boucles d'échec.  
**Transposition :** documenter et potentiellement proposer **optionnellement** le plugin, selon versions/hook permissions ; P0.1 n'exécute aucun hook tiers.

**[R26] Bai et al. — How Do AI Agents Spend Your Money?** (arXiv 2604.22750, E).  
URL : https://arxiv.org/abs/2604.22750  
**Constat :** forte variabilité des trajectoires, davantage de tokens n'assure pas une meilleure réponse.  
**Transposition :** chercher les répétitions et l'exploration avant de compresser agressivement.

**[R27] Weinberger & Hozez — Token Reduction Is Not Cost Reduction** (arXiv 2607.12161, E).  
URL : https://arxiv.org/abs/2607.12161  
**Résultats :** sur 2 848 exécutions analysées, une compression retirant ~38 % de tokens bruts de sorties d'outils aboutissait à ~6,8 % de coût facturé supplémentaire dans un bras ; réduction du contexte peut supprimer les preuves nécessaires.  
**Transposition :** VCR sépare sortie masquée, cache, coût total et réussite ; n'ajoute pas de « compresseur universel ».

**[R28] An Empirical Cost Attribution of Context-Compression Gateways in Multi-Turn Coding Agents** (arXiv 2609.22114, E).  
URL : https://arxiv.org/abs/2609.22114  
**Transposition :** éviter les descriptions d'outils inutiles et vérifier le coût réel du filtrage.

**[R29] CliffCompaction** (arXiv 2609.26779, E).  
URL : https://arxiv.org/abs/2609.26779  
**Transposition :** option avancée ; les gains de coût rapportés ne rendent pas la compression systématique sûre.

**[R30] OpenAI — Prompt Caching** (O, prix/version évolutifs).  
URL : https://developers.openai.com/api/docs/guides/prompt-caching  
**Transposition :** stabilité du préfixe et des outils pour optimiser **facturation API** ; les quotas des abonnements ChatGPT/Codex ne se déduisent pas de cette grille. En cas d'absence de `cached_tokens`, ne pas estimer.

**[R31] METR — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity** (10 juil. 2025, E).  
URL : https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/  
**[R32] METR — We are Changing our Developer Productivity Experiment Design** (24 fév. 2026, E/I).  
URL : https://metr.org/blog/2026-02-24-uplift-update/  
**Transposition :** l'évaluation de l'efficacité des agents est difficile ; biais de sélection et de perception ; **ne pas prendre une réduction de latence ou de tokens pour un gain de productivité métier sans preuve**.

## 7. Recherche avancée sur auto-amélioration des harness

**[R33] Google Research — Harness²: Recursive Agent Harnessing for an Open World** (arXiv 2610.14224, E prépublication + G).  
URL papier : https://arxiv.org/abs/2610.14224  
URL code : https://github.com/google-research/harness2  
URL setup : https://github.com/google-research/harness2/blob/main/docs/SETUP.md  
**Description précise :** deux niveaux de récursion : (a) `Propose–Probe–Compose` appliqué au harness de la tâche à partir de comparaisons d'exécutions ; (b) enrichissement persistant d'une mémoire d'amélioration entre tâches. Huit composantes éditables : prompt système, garde-fous, mémoire, consignes pour outils, sous-agents, skills, scripts et plugins. Les auteurs rapportent des progrès sur trois benchmarks et plusieurs configurations, **pas** une supériorité universelle.  
**Danger opérationnel :** le setup Codex indique une exécution avec sandbox désactivé dans certaines conditions. VCR doit lire cette source comme **recherche avancée** uniquement ; aucune commande d'installation/exécution sur de vrais projets.  
**Idée à transposer sans la complexité :** IMPROVE transforme les incidents en propositions **réversibles, évaluables et soumises à validation humaine**.

**[R34] Meta-Harness: End-to-End Optimization of Model Harnesses** (publication retrouvée comme travaux liés, mais pas assimilée sans preuve au visuel social).  
Référence contextuelle : https://ishwarj.com/papers/meta-harness/read/  
**Statut :** source de vulgarisation vérifiée, étude originale à retrouver/lire avant citation quantitative.  
**Avertissement :** l'image circulant avec le titre « The End of Harness Engineering » et un modèle « 4B editor » n'a **pas de lien primaire identifiable dans la capture**. Ne pas la présenter comme un article de recherche validé ou comme une preuve de disparition de l'ingénierie humaine. Garder `UNVERIFIED_SOCIAL_CLAIM`.

**[R35] TrishamBP — Harness Engineering, reference harness** (G, schéma pédagogique).  
URL : https://github.com/TrishamBP/harness-engineering  
**Description :** implémentation Python stdlib démonstrative (boucle, outils typés, permissions, journaux, compactage, vérification, coordination) et diagrammes, inspirée d'une étude de code ; ce code n'est ni le code des agents industriels ni une preuve de supériorité.  
**Transposition :** bon exemple pour l'architecture d'interfaces, pas de raison de réécrire une boucle LLM dans P0.1.

## 8. Contradictions et ce que VCR DOIT écrire

| Question | Constat contradictoire | Décision défendable |
|---|---|---|
| `AGENTS.md` utile ? | pratiques industrielles favorables ; évaluations neutres/négatives sur certaines tâches | garder un **index court** avec commandes, invariants, docs liées ; éviter sur-prescription |
| Skills = gain ? | benchmark général favorable ; SWE-Skills-Bench v2 très peu de gains significatifs | sélectionner skills **individuels** ; jamais copier un pack énorme par défaut |
| Compression = économie ? | réductions de tokens observables ; parfois coût API + échecs en hausse | préserver preuves et cache, mesurer/attribuer coût réel si disponible |
| Vectoriel = indispensable ? | certains gains de rappel ; pas dominant partout ; absent des 11 harness étudiés | native/symbolique d'abord ; vectoriel optionnel |
| Multi-agent supérieur ? | bénéfices sur certaines tâches ; coûts et défaillances de coordination | un agent principal par défaut ; délégation seulement quand utile |
| Réécrire l'architecture d'un projet ? | mode changeant ; risques de régressions et données | KEEP/REFACTOR souvent préférable ; REBUILD seulement argumenté |
| Auto-améliorer les règles ? | faisabilité de recherche ; risques de surajustement et dérive | **propositions humaines** d'abord, expérience récursive isolée plus tard |

## 9. Règles d'entretien des connaissances

Chaque fiche doit inclure `id`, `title`, `url`, `authors/owner`, `date`, `last_checked`, `source_type`, `evidence_scope`, `limitations`, `relevance`, `recommendation_tier`, `license_if_repo`, `review_required`. Une source non lue entièrement peut être `catalogued`, non `verified`. Les études arXiv doivent porter leur **version**. Les projets GitHub évoluent vite : les instructions d'installation et noms de skills sont à revalider au moment de l'usage.

**Cette recherche est datée du 14 novembre 2026.** Une actualisation des sources externes sera nécessaire avant de publier officiellement le référentiel.
