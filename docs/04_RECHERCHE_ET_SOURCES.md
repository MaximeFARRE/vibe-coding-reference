# 04 — Critical review of research and technical publications

**Supplementary review: November 14, 2026.** This document condenses sources needed for **implementation decisions**. For all references identified since the project began, see `reference/BIBLIOGRAPHIE_HISTORIQUE_v0.2.md` and `reference/RESEARCH_AND_DESIGN_v0.2.md`. The levels are deliberately separate to avoid injecting 80 sources into Codex context for every change.

## 1. Evidence policy and critical reading

- **E — Empirical study:** protocol, task, models and limitations stated. An arXiv preprint is not necessarily peer reviewed.
- **I — Industrial experience:** strong practical value, but a specific environment and possible commercial/sampling bias.
- **O — Official documentation:** evidence that an interface or feature exists, **not** that it improves performance.
- **G — GitHub repository/practice:** source of code or ideas; popularity/stars do not measure quality or token gains.

**No unwarranted generalization:** task success, cost per resolution and regressions matter more than a simple “−X% tokens”. Preserve uncertainty and review dates. VCR users are not promised performance gains.

## 2. Foundational studies: architecture and harnesses

**[R01] OpenAI — Harness engineering: leveraging Codex in an agent-first world** (February 11, 2026, I).<br>
URL: https://openai.com/index/harness-engineering/<br>
**Source finding:** product developed by Codex; emphasis on the repository as a knowledge source, controlled architecture, automated validation, code readability, feedback loops and removal of complexity. The team reports very high productivity in its context.<br>
**VCR application:** concise `AGENTS.md`; executable important rules; evidence trail; observed architecture; ongoing maintenance; controlled report.<br>
**Limitation:** one team with specific resources; **no demonstrated superiority of Next.js/TS**.

**[R02] OpenAI — Maintaining software with the GPT-6 family** (October 14, 2026, I).<br>
URL: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family<br>
**Source finding:** large-scale code cleanup with actual-usage checks, business exclusions, draft PRs and reviews; attention to false positives, flags and safety mechanisms. Several CI improvements were measured in their infrastructure.<br>
**Application:** RESCUE must gather evidence **before** deletion; exclude kill switches and dynamic usage; propose small fixes rather than a big bang.

**[R03] OpenAI — Rethinking skills and prompts for GPT-6 Astra** (September 11, 2026, I/O).<br>
URL: https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra<br>
**Finding:** recent models may need fewer older instructions; overly generic skills and overloaded prompts can be counterproductive.<br>
**Application:** review AGENTS/skills regularly; avoid documentation overload.

**[R04] Barbaste et al. — Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems** (arXiv 2609.00006, July 2026, descriptive E).<br>
URL: https://arxiv.org/abs/2609.00006<br>
**Source finding:** code analysis of eleven harnesses (Claude Code, Codex, Gemini CLI, Aider, OpenHands, OpenCode, etc.), seven subsystems and 29 patterns. In this production sample, code search did not rely on vector embeddings; loops and navigation were mainly deterministic.<br>
**Application:** do not build RAG reflexively; separate execution/tools/context/state/security/evaluation; prefer a simple adapter.<br>
**Limitation:** snapshot of studied systems at one date; does not prove RAG could never help.

**[R05] Martin Fowler — Monolith First** (technical essay, I/opinion).<br>
URL: https://martinfowler.com/bliki/MonolithFirst.html<br>
**Application:** simple/modular monolith as a conditional candidate, not dogma or an experimental agent comparison.

**[R06] ESEM 2026 — On Coding Agent Issue Localization Accuracy: An Exploratory Study** (conference, E).<br>
URL: https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.59<br>
**Finding:** greater difficulty locating the precise method even when the general area is identified.<br>
**Application:** reduce trips between modules and provide verifiable entry points.

## 3. Context acquisition and navigation

**[R07] Qin & Xie — Agent Retrieval Bench** (arXiv 2607.24882, July 2026, E).<br>
URL: https://arxiv.org/abs/2607.24882<br>
**Results:** 427 cases, 25 repositories; no retrieval family is best everywhere. RepoMap has the best context efficiency among compared options with an 8k-token budget; vector methods win on other metrics; observed trajectories may miss all relevant files in 27–35% of cases.<br>
**Application:** lexical/symbolic search first, optional compact maps, embeddings only for a documented recall problem.<br>
**Limitation:** context retrieval != eventual repair success.

**[R08] Chen et al. — CodeGrep** (ACL REALM 2026, workshop study).<br>
URL: https://aclanthology.org/2026.realm-1.80/<br>
**Results:** −19% tokens and −15% turns on solved instances in the protocol, without significant success degradation.<br>
**Application:** spend less finding the right file; P0.1 does not reproduce the specialized RL search agent.

**[R09] Zhang et al. — SWE-Explore** (arXiv 2606.07297, E preprint).<br>
URL: https://arxiv.org/abs/2606.07297<br>
**Application:** treat code search as a first-class concern in AI-maintainability audits.

**[R10] Gloaguen et al. — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?** (arXiv 2602.11988, E).<br>
URL: https://arxiv.org/abs/2602.11988<br>
**Results:** inference cost over 20% higher and a tendency toward lower success in studied protocols with overloaded context files.<br>
**Application:** minimal useful instructions and links to docs, not an encyclopedia.<br>
**Limitation:** this does not invalidate every specific instruction.

**[R11] Khatri — Do Context Files Help Coding Agents? A Two-Agent Ablation Study** (REALM 2026, E workshop).<br>
URL: https://aclanthology.org/volumes/2026.realm-1/<br>
**Finding:** no measurable success gain under the published protocol; contributes to the AGENTS.md controversy.<br>
**Application:** keep hypotheses open; prefer strictly operational instructions.

**[R12] Anthropic — Effective context engineering for AI agents** (2025, I).<br>
URL: https://www.anthropic.com/research/effective-context-engineering-for-ai-agents<br>
**Application:** context as a limited resource, documents loaded on demand, relevance over volume.

**[R13] Aider — Repository Map** (O/G).<br>
URL: https://aider.chat/docs/repomap.html<br>
**Application:** example of a compact symbol map; no obligation to adopt Aider itself.

## 4. Requirements, tests and error risk

**[R14] SWE-Journey** (arXiv 2610.11559, October 2026, E).<br>
URL: https://arxiv.org/abs/2610.11559<br>
**Finding:** for extended development tasks, interactions with a user who can clearly specify needs are much more effective than those with vague intent.<br>
**Application:** START should produce business criteria and testable requirements in plain language without overwhelming beginners with jargon.

**[R15] Sun et al. — SWE-Mutation: Can LLMs Generate Reliable Test Suites in Software Engineering?** (Findings of ACL 2026, July 2026, E conference).<br>
URL: https://aclanthology.org/2026.findings-acl.1976/<br>
Code: https://github.com/Sunny4Coding/SWE-Mutation<br>
**Finding:** 2,636 mutated variants built on 800 instances; model-generated tests can let intentionally incorrect implementations pass.<br>
**Application:** green tests alone do not prove critical-path coverage; assess whether assertions discriminate. Experimental rates are not the average error rate of all AI tests.

**[R16] Banik et al. — All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code** (arXiv 2606.18168, E preprint).<br>
URL: https://arxiv.org/abs/2606.18168<br>
**Finding:** many agent-generated test changes have weak or absent verification signals according to the study's classification.<br>
**Application:** ask “what bug would this test catch?”, not just “does it pass?”.

**[R17] Test Coverage Analysis of Agentic Pull Requests** (arXiv 2607.18057, E).<br>
URL: https://arxiv.org/abs/2607.18057<br>
**Application:** flag test gaps in APIs, transactions and changed code; coverage alone is not a safety score.

**[R18] Sun et al. — Coding Agents Propagate Vulnerabilities in Code Bases** (arXiv 2611.11455, November 8, 2026, E).<br>
URL: https://arxiv.org/abs/2611.11455<br>
**Finding:** agents can reproduce nearby vulnerabilities even with general security guidance.<br>
**Application:** a harness should check inherited bad conventions through explicit tests and rules. Results are limited to the study's tasks/frameworks.

**[R19] Anthropic — Harness design for long-running application development** (March 24, 2026, I).<br>
URL: https://www.anthropic.com/research/harness-design-long-running-apps<br>
**Application:** plans, independent validation and handoff states can help long tasks; do not impose its multi-agent cost on every project.

**[R20] OpenAI — Iterating Development Workflows with Codex** (August 3, 2026, O/recipe).<br>
URL: https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex<br>
**Application:** per-phase contract and log files are optional conventions; the user must approve secret, infrastructure, commit, push, deployment and branch-switching changes.

## 5. Skills: benefits, non-benefits and security

**[R21] SkillsBench** (arXiv 2602.12670, E).<br>
URL: https://arxiv.org/abs/2602.12670<br>
**Results from the version consulted in v0.2:** positive average gain over varied tasks, more modest in software development.<br>
**Application:** specialized skills are plausible; no universal gain.

**[R22] SWE-Skills-Bench v2** (arXiv 2603.15401v2, revised October 27, 2026, E).<br>
URL: https://arxiv.org/html/2603.15401v2<br>
**Results:** 98 skills studied; 92 without statistically significant effect, 4 beneficial and 2 harmful under the evaluated conditions; variation across models. Figures from the first March version **must no longer be presented as current results**.<br>
**Application:** catalog existing skills with source/version and **individual** evidence; popularity != effectiveness. The benchmark does not establish that all nonsignificant skills are useless.

**[R23] USENIX Security — “Do Not Mention This to the User”: Detecting and Understanding Malicious Agent Skills in the Wild** (2026, E conference).<br>
URL: https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi<br>
**Reported results:** 157 confirmed malicious skills among 98,380 studied.<br>
**Application:** review scripts, permissions and provenance before installation; never “install all skills”.

**[R24] Agent Skills Specification** (O).<br>
URL: https://agentskills.io/specification<br>
**Application:** common packaging format, not evidence that all agents activate skills identically.

## 6. Token consumption and actual costs

**[R25] Microsoft Research — TokenEconomizer** (October 2026, E/I).<br>
Publication: https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/<br>
Code: https://github.com/microsoft/TokenEconomizer<br>
**Results:** 18.4–30.9% reduction in mean cost across five studied agent-model combinations, with at least comparable resolution effectiveness in the study; mechanisms include small persistent information, unused-tool removal and intervention in failure loops.<br>
**Application:** document and potentially offer the plugin **optionally**, depending on versions/hook permissions; P0.1 runs no third-party hooks.

**[R26] Bai et al. — How Do AI Agents Spend Your Money?** (arXiv 2604.22750, E).<br>
URL: https://arxiv.org/abs/2604.22750<br>
**Finding:** trajectories vary widely; more tokens do not guarantee a better answer.<br>
**Application:** look for repetition and exploration before aggressive compression.

**[R27] Weinberger & Hozez — Token Reduction Is Not Cost Reduction** (arXiv 2607.12161, E).<br>
URL: https://arxiv.org/abs/2607.12161<br>
**Results:** among 2,848 runs, compression removing ~38% of raw tool-output tokens resulted in ~6.8% more billed cost in one arm; context reduction can remove necessary evidence.<br>
**Application:** VCR separates masked output, cache, total cost and success; no “universal compressor”.

**[R28] An Empirical Cost Attribution of Context-Compression Gateways in Multi-Turn Coding Agents** (arXiv 2609.22114, E).<br>
URL: https://arxiv.org/abs/2609.22114<br>
**Application:** avoid unnecessary tool descriptions and check the actual cost of filtering.

**[R29] CliffCompaction** (arXiv 2609.26779, E).<br>
URL: https://arxiv.org/abs/2609.26779<br>
**Application:** advanced option; reported cost gains do not make systematic compression safe.

**[R30] OpenAI — Prompt Caching** (O, evolving prices/version).<br>
URL: https://developers.openai.com/api/docs/guides/prompt-caching<br>
**Application:** stable prefixes and tools can optimize **API billing**; ChatGPT/Codex subscription quotas cannot be inferred from this pricing. Do not estimate missing `cached_tokens`.

**[R31] METR — Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity** (July 10, 2025, E).<br>
URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/<br>
**[R32] METR — We are Changing our Developer Productivity Experiment Design** (February 24, 2026, E/I).<br>
URL: https://metr.org/blog/2026-02-24-uplift-update/<br>
**Application:** agent effectiveness is difficult to evaluate; selection and perception bias matter; **do not treat latency or token reduction as business-productivity gain without evidence**.

## 7. Advanced research on harness self-improvement

**[R33] Google Research — Harness²: Recursive Agent Harnessing for an Open World** (arXiv 2610.14224, E preprint + G).<br>
Paper: https://arxiv.org/abs/2610.14224<br>
Code: https://github.com/google-research/harness2<br>
Setup: https://github.com/google-research/harness2/blob/main/docs/SETUP.md<br>
**Precise description:** two recursion levels: (a) `Propose–Probe–Compose` applied to the task harness using run comparisons; (b) persistent improvement memory across tasks. Eight editable components: system prompt, safeguards, memory, tool instructions, subagents, skills, scripts and plugins. Authors report gains on three benchmarks and several configurations, **not** universal superiority.<br>
**Operational risk:** Codex setup indicates execution with sandbox disabled under some conditions. VCR must treat this as **advanced research** only; no installation/execution commands on real projects.<br>
**Idea to adapt without the complexity:** IMPROVE turns incidents into **reversible, evaluable proposals subject to human approval**.

**[R34] Meta-Harness: End-to-End Optimization of Model Harnesses** (found as related work, but not equated with the social image without evidence).<br>
Contextual reference: https://ishwarj.com/papers/meta-harness/read/<br>
**Status:** explanatory source verified; locate and read the original study before quantitative citation.<br>
**Warning:** the image circulating under “The End of Harness Engineering” and a “4B editor” model has **no identifiable primary link in the screenshot**. Do not present it as validated research or evidence that human engineering is disappearing. Keep `UNVERIFIED_SOCIAL_CLAIM`.

**[R35] TrishamBP — Harness Engineering, reference harness** (G, educational diagram).<br>
URL: https://github.com/TrishamBP/harness-engineering<br>
**Description:** demonstrative stdlib Python implementation (loop, typed tools, permissions, logs, compaction, verification, coordination) and diagrams inspired by a code study; neither industrial-agent code nor proof of superiority.<br>
**Application:** good interface-architecture example, not a reason to rewrite an LLM loop in P0.1.

## 8. Contradictions and what VCR MUST state

| Question | Conflicting evidence | Defensible decision |
|---|---|---|
| Is `AGENTS.md` useful? | Favorable industry practices; neutral/negative evaluations on some tasks | Keep a **short index** with commands, invariants and linked docs; avoid over-prescription |
| Skills = gains? | Favorable general benchmark; SWE-Skills-Bench v2 has few significant gains | Select **individual** skills; never copy a huge pack by default |
| Compression = savings? | Observable token reductions; sometimes higher API cost and failures | Preserve evidence and cache; measure/attribute actual cost when available |
| Are vectors essential? | Some recall gains; not dominant everywhere; absent from the 11 studied harnesses | Native/symbolic first; vectors optional |
| Is multi-agent better? | Benefits for some tasks; coordination costs and failures | One lead agent by default; delegate only when useful |
| Rewrite a project's architecture? | Changing fashions; regression and data risks | KEEP/REFACTOR often preferable; REBUILD only with justification |
| Self-improve rules? | Research feasibility; overfitting and drift risks | **Human proposals** first, isolated recursive experiment later |

## 9. Knowledge maintenance rules

Each entry must include `id`, `title`, `url`, `authors/owner`, `date`, `last_checked`, `source_type`, `evidence_scope`, `limitations`, `relevance`, `recommendation_tier`, `license_if_repo`, `review_required`. A source not read in full may be `catalogued`, not `verified`. arXiv studies must include their **version**. GitHub projects change quickly: installation instructions and skill names must be revalidated at use time.

**This research is dated November 14, 2026.** External sources must be refreshed before official publication of the reference.
