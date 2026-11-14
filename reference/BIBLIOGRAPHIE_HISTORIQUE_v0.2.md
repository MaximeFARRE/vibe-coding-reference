# Bibliographie historique complète — v0.2 (fichier source recopié)

> Références S01–S47 et N01–N31 recensées au 12/11/2026. Certaines ne sont PAS revérifiées. Le dossier `docs/04_RECHERCHE_ET_SOURCES.md` contient la réévaluation sélective au 14/11/2026. Ne pas confondre « recensé » et « validé ».

## 17. Mode d'emploi des sources

- Les références **[S01] à [S45]** reprennent les 45 sources listées dans notre bilan précédent, dans le même ordre ; quelques intitulés et liens ont été précisés.
- Les références **[S46] et [S47]** sont des compléments officiels identifiés pendant cette consolidation.
- « Ouvert » = page vérifiée via une source consultée dans cette séance. « Recensé » = lien répertorié mais non relu complètement.
- Les articles industriels et dépôts sont des **sources primaires sur leurs propres pratiques**, pas des preuves scientifiques d'efficacité comparative.
- Les liens X peuvent changer de disponibilité ; l'archive textuelle / citation primaire est à rechercher avant d'appuyer une recommandation structurante sur un post.

### A — Recherche industrielle, agents et études (S01–S10)

**[S01] OpenAI — Harness engineering: leveraging Codex in an agent-first world.** Ryan Lopopolo, 11 févr. 2026. **B · Ouvert.** Architecture vérifiable, documentation, maintenance et environnement de Codex.  
https://openai.com/index/harness-engineering/

**[S02] OpenAI — Rethinking skills and prompts for GPT-6 Astra.** Eric Provencher, 11 sept. 2026. **B · Ouvert.** Skills, `AGENTS.md`, surcharge de contexte, révision des anciennes instructions.  
https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

**[S03] OpenAI — Maintaining software with the GPT-6 family.** Oct. 2026. **B · Ouvert.** Nettoyage raisonné du code et conservation des garde-fous métier.  
https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family

**[S04] Anthropic — Effective context engineering for AI agents.** 2025. **B · Ouvert.** Sélection d'informations utiles, contexte limité, outils chargés à la demande.  
https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

**[S05] Anthropic — Harness design for long-running application development.** 24 mars 2026. **B · Ouvert.** Agents planificateur/générateur/évaluateur, coût de l'évaluation, limites des scaffolds.  
https://www.anthropic.com/research/harness-design-long-running-apps

**[S06] Anthropic — Agentic coding and persistent returns to expertise.** 16 juin 2026. **A/B · Ouvert.** Pratiques de Claude Code et rôle de l'expertise dans l'usage des agents.  
https://www.anthropic.com/research/claude-code-expertise

**[S07] Anthropic — Building effective agents.** Déc. 2024. **B · Recensé (résumé source consulté).** Favoriser les systèmes simples ; complexifier seulement si nécessaire.  
https://www.anthropic.com/research/building-effective-agents

**[S08] Anthropic — Claude Code Best Practices.** Documentation officielle évolutive. **C · Recensé.** Sessions, instructions et contrôles.  
https://code.claude.com/docs/en/best-practices

**[S09] SWE-agent — Agent-Computer Interfaces Enable Automated Software Engineering.** Yang et al., 2024. **A · Ouvert.** Influence de l'interface outillée sur les capacités des agents.  
https://arxiv.org/abs/2405.15793

**[S10] DeepSeek-Coder-V2 — Breaking the Barrier of Closed-Source Models in Code Intelligence.** DeepSeek-AI, 2024. **A/B · Ouvert.** Modèle de code et évaluations ; aucune conclusion directe sur les frameworks web.  
https://arxiv.org/abs/2406.11931

### B — Études indépendantes et experts (S11–S14)

**[S11] METR — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.** 10 juill. 2025. **A · Ouvert.** Expérience randomisée ; +19 % de temps dans ce protocole.  
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

**[S12] METR — We are Changing our Developer Productivity Experiment Design.** 24 févr. 2026. **A/B · Ouvert.** Limites de mesure et biais de sélection des études plus récentes.  
https://metr.org/blog/2026-02-24-uplift-update/

**[S13] Andrej Karpathy — Message original sur le « vibe coding ».** Févr. 2025. **D · Recensé.** Point de départ historique ; opinion/observation personnelle.  
https://x.com/karpathy/status/1886192184808149383

**[S14] Andrej Karpathy — Publication sur « agentic engineering ».** Févr. 2026, intitulé exact et contenu à confirmer. **D · À vérifier.**  
https://x.com/karpathy/status/2026731645169185220

### C — Collections, workflows et setups d'experts (S15–S25)

**[S15] Everything Claude Code (affaan-m/ECC).** **D · Recensé.** Catalogue de skills, agents, hooks et configurations.  
https://github.com/affaan-m/ECC

**[S16] Matt Pocock — Skills for Real Engineers.** **D · Ouvert.** Skills d'ingénierie, TDD, revue, modèles de domaine, documentation pour agents.  
https://github.com/mattpocock/skills

**[S17] Peter Steinberger — Agent Scripts.** **D · Ouvert.** `AGENTS.md`, petits scripts et synchronisation légère de skills.  
https://github.com/steipete/agent-scripts

**[S18] obra — Superpowers.** **D · Recensé.** Méthodes de brainstorming, tests, refactoring et vérification.  
https://github.com/obra/superpowers

**[S19] wshobson/agents.** **D · Recensé.** Grand catalogue d'agents et de plugins spécialisés.  
https://github.com/wshobson/agents

**[S20] Vercel — Agent Skills.** **C/D · Recensé.** Skills de bonnes pratiques React/Next.js.  
https://github.com/vercel-labs/agent-skills

**[S21] GitHub — Spec Kit.** **C/D · Recensé.** Développement piloté par spécifications.  
https://github.com/github/spec-kit

**[S22] khasky — Awesome Agent Skills.** **D · Ouvert.** Skills d'audit, sécurité, tests, nettoyage et revue.  
https://github.com/khasky/awesome-agent-skills

**[S23] Vibe Coding Rules.** **D · Recensé.** Règles et structures de projets variés.  
https://github.com/yerdaulet-damir/vibe-coding-rules

**[S24] Every — Compound Engineering Plugin.** **D · Ouvert.** Boucle planifier → coder → simplifier → revoir → capitaliser.  
https://github.com/EveryInc/compound-engineering-plugin

**[S25] Cole Medin — Archon.** **D · Ouvert.** Workflows codifiés pour agents et validations.  
https://github.com/coleam00/Archon

### D — Navigation, index et documentation (S26–S32)

**[S26] Serena.** **D · Recensé.** Recherche symbolique et navigation outillée dans le code.  
https://github.com/oraios/serena

**[S27] Aider — Repository Map.** **D · Recensé.** Carte concise des classes et symboles d'un dépôt.  
https://aider.chat/docs/repomap.html

**[S28] Codebase Memory MCP.** **D · Ouvert.** Graphe/index local ; gains annoncés à valider avant citation.  
https://github.com/DeusData/codebase-memory-mcp

**[S29] Google — Introducing Code Wiki: Accelerating your code understanding.** 13 nov. 2025. **B/C · Ouvert.** Documentation vivante reliée aux définitions de code.  
https://developers.googleblog.com/introducing-code-wiki-accelerating-your-code-understanding/

**[S30] OpenBMB — RepoAgent.** **D · Ouvert.** Génération et maintenance de documentation de dépôt.  
https://github.com/OpenBMB/RepoAgent

**[S31] GitHub Agentic Workflows — Keeping documentation up to date automatically.** **C · Ouvert.** Mise à jour de docs sous forme de PR contrôlée.  
https://github.github.com/gh-aw/gallery/docs-automation/

**[S32] Repomix.** **D · Recensé.** Export ciblé du code pour agents et audits.  
https://repomix.com/

### E — Architecture et contrôles de dépendances (S33–S39)

**[S33] Feature-Sliced Design.** **C/D · Recensé.** Couches et découpages frontend ; éviter la surapplication.  
https://feature-sliced.design/

**[S34] Feature-Sliced Design — Agent Skills.** **C/D · Ouvert.** Règles d'import, croissance progressive des couches, skills FSD.  
https://github.com/feature-sliced/skills

**[S35] Create T3 App.** **D · Recensé.** Exemple de starter Next.js et sélection de technologies.  
https://github.com/t3-oss/create-t3-app

**[S36] Martin Fowler — Monolith First.** **B/D · Recensé.** Argument architectural favorable au monolithe comme point de départ dans certaines situations.  
https://martinfowler.com/bliki/MonolithFirst.html

**[S37] Dependency Cruiser.** **D · Recensé.** Cartographie et contraintes de dépendances JS/TS.  
https://github.com/sverweij/dependency-cruiser

**[S38] ESLint Plugin Boundaries.** **D · Recensé.** Règles de dépendances entre modules JS/TS.  
https://github.com/javierbrea/eslint-plugin-boundaries

**[S39] Import Linter.** **D · Recensé.** Contrats de dépendances Python.  
https://import-linter.readthedocs.io/en/stable/

### F — Standards et documentations techniques (S40–S45)

**[S40] Agent Skills — Specification.** **C · Ouvert.** Convention du `SKILL.md` et de ses références/scripts.  
https://agentskills.io/specification

**[S41] AGENTS.md — Open format.** **C · Ouvert.** Instruction de dépôt destinée aux agents de code.  
https://github.com/agentsmd/agents.md

**[S42] OpenAI — Documentation sur AGENTS.md pour Codex.** **C · À préciser.** Le lien initial de nos notes n'était pas suffisamment fiable ; voir la source complémentaire [S46].  
Lien antérieurement envisagé : https://learn.chatgpt.com/docs/agent-configuration/agents-md

**[S43] Astro — Islands Architecture.** **C · Recensé.** Architecture frontend à îlots.  
https://docs.astro.build/en/concepts/islands/

**[S44] Django — site et documentation officielle.** **C · Recensé.** Conventions backend/full-stack Python.  
https://www.djangoproject.com/

**[S45] HTMX — site et documentation officielle.** **C · Recensé.** Interactions HTML côté serveur.  
https://htmx.org/

### G — Compléments officiels identifiés pendant la consolidation (S46–S47)

**[S46] OpenAI — Codex Prompting Guide (section AGENTS.md).** **C · Ouvert.** Ordre de découverte des instructions dans les répertoires.  
https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide

**[S47] Anthropic — Public repository for Agent Skills.** **C/D · Ouvert.** Exemples de skills et conventions officielles ; les ressources du dépôt restent à examiner une par une.  
https://github.com/anthropics/skills

### H — Guides officiels à compléter dans le prochain cycle

Next.js, SvelteKit, React, Vite, FastAPI, Streamlit, Ruby on Rails, GitHub Actions, ESLint, Biome, Ruff, uv, Vitest, pytest, Playwright, Gitleaks et OSV-Scanner. Ils sont mentionnés comme outils/stacks dans notre réflexion ; une revue comparative des documentations officielles reste à mener. **Aucune conclusion sur un avantage propre aux agents ne doit être inférée de leur simple présence dans cette liste.**

---


## Compléments N01–N31

## 17 bis. Sources nouvelles vérifiées ou identifiées pour la v0.2 (N01–N31)

**Mode de lecture :** `A-prépublication` = étude expérimentale déposée avant validation éventuelle par les pairs ; `A-conférence` = article dans des actes de conférence/atelier ; `B` = retour technique industriel ; `C` = documentation éditeur ; `D` = dépôt et pratiques publiques. L'état **« source consultée »** signifie que l'abstract, la page d'actes ou la documentation liée a été accessible lors de cette consolidation, **pas** que nous avons reproduit les résultats ni audité le code de l'étude. La présence d'un article dans Google Scholar/arXiv n'établit pas sa robustesse.

### Navigation et architecture

**[N01] Qin, B. & Xie, Y. — Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents.** 27 juillet 2026. **A-prépublication, source consultée.** 427 exemples, 25 dépôts ; comparaison lexicale, embeddings, RepoMap et récupérations d'agents. Ne pas confondre métrique de retrieval et réussite d'un correctif.  
https://arxiv.org/abs/2607.24882

**[N02] Coppola, A., Esposito, M., Kazman, R. & Lenarduzzi, V. — On Coding Agent Issue Localization Accuracy: An Exploratory Study.** ESEM, 5 octobre 2026. **A-conférence, source consultée.** Étude de granularité package/classe/méthode ; 2 441 commits dans dix projets Java.  
https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.59

**[N10] Zhang, S. et al. — SWE-Explore: Benchmarking How Coding Agents Explore Repositories.** Juin 2026. **A-prépublication, source consultée.** 848 problèmes, 203 projets, dix langages ; évaluation d'exploration sous budget de lignes.  
https://arxiv.org/abs/2606.07297

**[N11] Chen, W., Yang, Y., Cao, Y. & Lin, Y. — CodeGrep: An RL-Trained Retrieval Agent for LLM Coding Agents.** REALM 2026, ACL Anthology, octobre 2026. **A-atelier, source consultée.** Code retrieval spécialisé, résultats −15 % de tours et −19 % de tokens sur instances résolues de SWE-bench Verified.  
https://aclanthology.org/2026.realm-1.80/

**[N23] Aider — Repository Map.** Documentation technique de l'outil ; **C/D, référence de documentation**. Emploi d'une carte des symboles pondérés sous budget de tokens.  
https://aider.chat/docs/repomap.html

### Instructions, besoins et skills

**[N03] Gloaguen, T. et al. — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?** 12 février 2026. **A-prépublication, source consultée.** Résultats défavorables à l'injection indiscriminée de contexte ; ne prouve pas que toute consigne minimale est inutile.  
https://arxiv.org/abs/2602.11988

**[N04] Li, X. et al. — SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks.** 13 février 2026. **A-prépublication, source consultée.** Benchmark général multi-domaines ; +16,2 points moyen, +4,5 en génie logiciel d'après la version consultée.  
https://arxiv.org/abs/2602.12670

**[N05] Han, T. et al. — SWE-Skills-Bench: Do Agent Skills Actually Help in Real-World Software Engineering?** **Version 2 du 27 octobre 2026**. **A-prépublication, texte HTML et tableau de résultats consultés.** 98 skills ; 92 sans effet significatif, quatre positifs et deux négatifs, moyenne +0,3 point. Les résultats de mars 2026 sont historiques.  
https://arxiv.org/html/2603.15401v2

**[N06] Deng, H. et al. — SWE-Journey: Towards More Realistic Evaluation of Coding Assistants through Long-Horizon, Multi-Turn Interaction.** 8 octobre 2026. **A-prépublication, source consultée.** Benchmark d'interactions prolongées avec profils utilisateurs ; fortes différences selon la capacité à préciser les besoins.  
https://arxiv.org/abs/2610.11559

**[N17] Liu, Y. et al. — “Do Not Mention This to the User”: Detecting and Understanding Malicious Agent Skills in the Wild.** USENIX Security 2026. **A-conférence, résumé consulté.** 98 380 skills étudiés, 157 malveillants confirmés dans le corpus.  
https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi

**[N24] Vercel — Agent Skills, notamment `vercel-react-best-practices`.** Dépôt officiel, **C/D, documentation consultée** ; 70 règles dans le SKILL.md consulté. Pas de preuve expérimentale indépendante de gain marginal examinée pour ce skill exact.  
https://github.com/vercel-labs/agent-skills

**[N25] Matt Pocock — Skills for Real Engineers.** Dépôt public et release notes, **D, documentation consultée**. Certains noms/invocations ont évolué ; ne pas supposer qu'un ancien nom persiste.  
https://github.com/mattpocock/skills

**[N26] Jesse Vincent / obra — Superpowers.** Dépôt et `systematic-debugging`, **D, documentation consultée**. Processus de debugging détaillé, pas une preuve d'efficacité comparative universelle.  
https://github.com/obra/superpowers

**[N30] Agent Skills — Specification.** Standard documentaire public des skills, **C, spécification identifiée**. Interopérabilité de format, pas uniformité d'interprétation des agents.  
https://agentskills.io/specification

**[N31] Huang, J. et al. — How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub.** 3 novembre 2026. **A-prépublication, source consultée.** 84 200 skills, 750 898 commits ; maintenance, redondance et évolution des connaissances.  
https://arxiv.org/abs/2611.04456

### Tests, sécurité, qualité

**[N07] Banik, D., Chowdhury, K. & Shamim, S. I. — All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code.** Juin 2026. **A-prépublication, source consultée.** 86 156 patchs de tests ; 80,2 % sans signaux d'oracle explicites forts selon la classification de l'étude.  
https://arxiv.org/abs/2606.18168

**[N08] Dipongkor, A. K., Baral, T., Lam, W. & Moran, K. — Test Coverage Analysis of Agentic Pull Requests.** 20 juillet 2026. **A-prépublication, source consultée.** Analyse de 4 882 PR ; couverture du code modifié et lacunes dans les blocs de gestion d'erreur.  
https://arxiv.org/abs/2607.18057

**[N09] Sun, C., Mündler-Sasahara, N., Vero, M. & Vechev, M. — Coding Agents Propagate Vulnerabilities in Code Bases.** 8 novembre 2026. **A-prépublication, source consultée.** Étude de la réutilisation de vulnérabilités à partir de code voisin ; résultats spécifiques aux protocoles backend et C/C++.  
https://arxiv.org/abs/2611.11455

### Tokens, cache et coût

**[N12] Li, A. J. et al. — TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents.** Microsoft Research, octobre 2026. **A-prépublication + B industriel, résumé officiel consulté.** Réduction moyenne de 18,4–30,9 % dans les configurations de l'étude.  
https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/

**[N13] Bai, L. et al. — How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks.** 24 avril 2026. **A-prépublication, source consultée.** Variabilité jusqu'à 30× selon trajectoires, saturation des gains de réussite avec plus de tokens.  
https://arxiv.org/abs/2604.22750

**[N14] Weinberger, S. & Hozez, A. — Token Reduction Is Not Cost Reduction.** 13 juillet 2026. **A-prépublication, source consultée.** 2 848 runs appariés analysés ; compression de sorties d'outils sans économie correspondante dans certains bras.  
https://arxiv.org/abs/2607.12161

**[N15] Chen, L. & Shi, J. — An Empirical Cost Attribution of Context-Compression Gateways in Multi-Turn Coding Agents.** Prépublication 2026. **A-prépublication, source consultée.** Décompose filtrage d'outils, compression et résumé.  
https://arxiv.org/abs/2609.22114

**[N16] Nguyen, T., Cho, E., Chen, B. & Dettmers, T. — CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents.** 22 septembre 2026. **A-prépublication, source consultée.** Compression conservatrice, gains jusqu'à 50 % sur certains protocoles ; système avancé.  
https://arxiv.org/abs/2609.26779

**[N27] Microsoft — TokenEconomizer, dépôt et documentation plugin.** **D/C, dépôt consulté.** Conditions de fonctionnement, hooks, versions d'agents compatibles, limites et commands d'annulation. Son existence ne remplace pas la revue de sécurité avant installation.  
https://github.com/microsoft/TokenEconomizer

**[N28] OpenAI — Prompt caching (API documentation).** **C, source officielle consultée le 12/11/2026.** Explique préfixes, cache read/write, TTL, prix et impact des modifications d'outils, modèle et compaction ; **valeurs sujettes à changement**.  
https://developers.openai.com/api/docs/guides/prompt-caching

### Retours industriels et méthodes

**[N18] Anthropic — Harness design for long-running application development.** 24 mars 2026. **B, retour détaillé consulté.** Planificateur/générateur/évaluateur, contrôle d'usage réel, budgets élevés et simplification de harness à mesure que les modèles progressent.  
https://www.anthropic.com/research/harness-design-long-running-apps

**[N19] OpenAI — Harness Engineering: Leveraging Codex in an Agent-First World.** Ryan Lopopolo, 11 février 2026. **B, retour industriel consulté.** Frontières imposées, connaissance versionnée dans le repo, nettoyage et feedback ; pas de conclusion universelle sur le framework.  
https://openai.com/index/harness-engineering/

**[N20] OpenAI — Rethinking skills and prompts for GPT-6 Astra.** Eric Provencher, 11 septembre 2026. **B/C, source consultée.** Descriptions courtes, chargement progressif, mise à jour des instructions historiques, non-imposition de lectures globales.  
https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

**[N21] OpenAI — Maintaining Software with the GPT-6 Family.** Octobre 2026. **B, source consultée.** Nettoyage avec garanties, modèle/effort/coût sur tâche spécifique et importance des exceptions métier.  
https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family

**[N22] METR — We are Changing our Developer Productivity Experiment Design.** 24 février 2026. **A/B, source consultée.** Explique biais de sélection et prudence face à l'estimation récente de gains de productivité ; garder distinct de l'étude historique de juillet 2025 [S11].  
https://metr.org/blog/2026-02-24-uplift-update/

**[N29] Anthropic — Effective context engineering for AI agents.** 2025. **B, déjà présent en [S04], rappel conceptuel.** Gestion du contexte comme ressource finie et outils/références nécessaires à la demande.  
https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

### Politique de fraîcheur

- Mettre en avant la version et le jour de la source lorsqu'une étude reçoit une mise à jour.
- Les sources [S01]–[S47] constituent l'**historique** et n'ont pas été intégralement reverifiées ici ; une fiche dédiée est nécessaire avant toute recommandation strictement dépendante de leur contenu actuel.
- Tous les chiffres précédés d'un signe « + » ou « − » renvoient au protocole cité, **jamais** à une promesse générale.
- Les fiches publiques doivent inclure un champ `last_checked` et, si nécessaire, `recheck_required`.

---


