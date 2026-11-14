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
