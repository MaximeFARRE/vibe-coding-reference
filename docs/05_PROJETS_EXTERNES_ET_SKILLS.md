# 05 — Prioritized catalog of GitHub repositories, tools, skills and experiments

**Public-page review: November 14, 2026.** This is an **options registry**, not an installation list. Versions change; every installation requires review of the current repository. `recommended` means “worth studying in this context”, **not** “current-version effectiveness proven”.

## 1. Four adoption categories

- **A — Reference and documentation:** useful for decisions; no component installed in the user's project.
- **B — Optional integration:** targeted tool enabled only when needed, with maintenance and compatibility checked.
- **C — Isolated laboratory:** advanced research on a disposable machine/container, without secrets or access to real repositories.
- **D — Watch only:** interesting potential but insufficient evidence or compatibility to recommend.

Tools may be powerful **behind the interface** if their value justifies it. No category B/C tool should appear as a mandatory requirement in the startup assistant.

## 2. Architecture and harness research

### [G01] Google Research — Harness²

**URL:** https://github.com/google-research/harness2<br>
**Paper:** https://arxiv.org/abs/2610.14224<br>
**Setup:** https://github.com/google-research/harness2/blob/main/docs/SETUP.md<br>
**Category: C** — research on harness self-improvement.

The system treats the harness as editable components around the model, with two levels of recursive improvement, comparison of execution behavior and persistence of validated lessons. Takeaways: (1) separate agent behavior from rules/tools; (2) each harness change should address an observable failure; (3) prevent unverified changes from spreading to other tasks.

**Study plan for Codex:** read README and setup; document components, assumptions, API and sandbox requirements and ability to reproduce an experiment on fixtures; **do not install or run automatically**. Setup describes a Codex configuration that may run without a sandbox. Risks: unisolated execution, unbounded costs, script/plugin editing, data leakage and evaluation overfitting. P0.1: simple entry plus supervised IMPROVE proposals.

### [G02] Walking Labs — Learn Harness Engineering

**URL:** https://github.com/walkinglabs/learn-harness-engineering<br>
**Category: A** — reference course with 14 lessons and practical projects according to its README at review time. Covers AGENTS, verification, session resumption, loop engineering, graph engineering and comparative analysis of Claude Code/Codex/Pi/DeepSeek. Closely related to our domain.

**Reusable ideas:** minimal persistent state, *plan → act → verify → hand off* loop, description of a “graph” as explicit routing. **Do not copy** its templates, exercises or `harness-creator` skill by default: assess license, maintenance, quality and conflict with our “no custom skills” policy. VCR helps users choose and **audit**, not recreate the course.

### [G03] TrishamBP — Harness Engineering

**URL:** https://github.com/TrishamBP/harness-engineering<br>
**Category: A/C** — diagrams and stdlib Python reference harness (loop, typed tools, permissions, logs, context, checks, coordination). Useful for understanding complex runtime interfaces.

**For Codex:** read its design and compare our safety obligations; do not take the entire codebase as a dependency or build an alternative runtime in P0.1. Its code is an original study-inspired illustration, not production code from the analyzed agents.

### [G04] Gloriaameng — Awesome Agent Harness

**URL:** https://github.com/Gloriaameng/Awesome-Agent-Harness<br>
**Category: A** — directory and matrix comparing loop, tools, context, state, hooks and evaluation. Useful to expand our catalog; may contain dated product descriptions and unverified information.

**For Codex:** extract only relevant entries and cross-check each claim against first-party project documentation. Never treat its ranking as a benchmark.

### [G05] LangGraph

**Repository:** https://github.com/langchain-ai/langgraph<br>
**Persistence:** https://docs.langchain.com/oss/python/langgraph/persistence<br>
**Category: C/future B** — stateful execution-graph engine with checkpoints, interruption/approval, resumption, routing and fan-out/fan-in. Interesting if VCR orchestrates multiple autonomous agents in long distributed audits.

**Introduction criterion:** actual need for crash recovery, N-agent coordination and mid-execution approval points. In P0.1, a simple Python workflow is enough: **no LangGraph**.

## 3. Navigation, maps and code search

### [G06] Serena

**URL:** https://github.com/oraios/serena<br>
**Category: B** — structured symbol/reference search and agent tool integration. May make large codebases easier to navigate.

**Investigate:** actually supported languages, installation, LSP startup, MCP security, output quotas and logs, search commands, JS/TS and Python limitations. Simple alternatives: `rg`, `git grep`, import analysis and file overview. Do not make Serena mandatory or assume every agent uses it automatically.

### [G07] Aider RepoMap

**Documentation:** https://aider.chat/docs/repomap.html<br>
**Repository:** https://github.com/Aider-AI/aider<br>
**Category: A/B** — symbol-ranking and compact-presentation algorithm. Useful for learning budgeted context. Agent Retrieval Bench reports interesting relative context efficiency at 8k tokens.

**Investigate:** actual reuse without forking all of Aider; license, stable API and compatibility. If standalone use is complex, keep the method as documentation.

### [G08] DeusData — Codebase Memory MCP

**URL:** https://github.com/DeusData/codebase-memory-mcp<br>
**Category: B/C** — local code graph/index, MCP tools, dependency and flow graphs; the current tool also includes semantic/vector search and optional UI. **A serious advanced-layer candidate**, not a core dependency.

**Investigate:** installation and footprint, version/features, storage, secret indexing, update mechanisms, network, file access, result granularity, license and revocation. Its “120× fewer tokens” claims are **vendor claims**, not independently verified gains. Comparisons must not become VCR promises.

### [G09] RepoAgent

**URL:** https://github.com/OpenBMB/RepoAgent<br>
**Category: D** — AST/LLM-based code-documentation generation and updates with change detection. Useful for research, but exhaustive documentation can be costly and stale; some integrations require a model/API and language coverage may be limited. **Document**, do not install.

### [G10] Repomix

**URL:** https://repomix.com/<br>
**Category: B** — one-off context export for review, not living memory. Large exports and secrets are risks; check `.gitignore` and excluded files before sending output to a model.

### [G11] Dependency Cruiser / ESLint Boundaries / Import Linter

- **Dependency Cruiser:** https://github.com/sverweij/dependency-cruiser (B, JS/TS, import rules and graphs).
- **ESLint Plugin Boundaries:** https://github.com/javierbrea/eslint-plugin-boundaries (B, JS/TS, lint-enforced boundaries).
- **Import Linter:** https://import-linter.readthedocs.io/en/stable/ (B, Python, dependency contracts).

Select **one** appropriate mechanism when boundary needs are established. Indirect imports, dynamic paths and business elements need further diagnosis.

## 4. Existing public engineering skills and workflows

### [G12] Matt Pocock — Skills for Real Engineers

**URL:** https://github.com/mattpocock/skills<br>
**Category: B (manual selection of individual skills)**. Scoping, architecture, audit, TDD and handoff skills. At review time the repository described `grill-with-docs`, `to-spec`, `improve-codebase-architecture`, `retro`, `diagnosing-bugs`, `code-review` and `to-tickets`, among others.

**Assessment:** particularly relevant to IMPROVE (`retro`) and specification preparation; verify **the exact name and content of the installed version**. Existence and popularity do not establish individual comparative gains. Do not install the whole setup in every repository.

### [G13] Jesse Vincent / obra — Superpowers

**URL:** https://github.com/obra/superpowers<br>
**Category: B**. Systematic debugging, testing, completion verification and planning workflows. May impose heavy steps unsuited to micro-tasks; examine `systematic-debugging`, `verification-before-completion` and actual trigger rules.

### [G14] Vercel — Agent Skills

**URL:** https://github.com/vercel-labs/agent-skills<br>
**Category: B**. React, Next.js and web UX best-practice skills; useful for START when the stack fits. An official source for framework practices; **no independent evidence of the exact skill's marginal benefit** in our corpus. Review scripts, version and triggers before use.

### [G15] GitHub — Spec Kit

**URL:** https://github.com/github/spec-kit<br>
**Category: B/A**. Specification → planning → implementation → verification. Best practices to adapt for START and requirements; introduce only a proportional subset. Do not default to a 30-document specification system.

### [G16] Every — Compound Engineering Plugin

**URL:** https://github.com/EveryInc/compound-engineering-plugin<br>
**Category: B/C**. Brainstorm/plan/build/review/compound loop, multiple skills and sometimes subagents; the version reviewed claims Codex compatibility (recheck at installation). Close to IMPROVE; watch context costs, permissions, automatic behavior and whole-suite installation. **Study selected mechanisms; do not install the whole suite** for P0.1.

### [G17] Peter Steinberger — Agent Scripts

**URL:** https://github.com/steipete/agent-scripts<br>
**Category: A/B**. Short instructions, script-synchronized skills, hooks and utilities. Useful for governance and instruction format; many decisions depend on the author's personal environment. Do not copy paths, models or permissions.

### [G18] Anthropic — Public Skills

**URL:** https://github.com/anthropics/skills<br>
**Category: A/B**. Official examples of skills and formats; useful sources, not all suitable or guaranteed for production. Retain individual selection and review.

### [G19] khasky — Awesome Agent Skills

**URL:** https://github.com/khasky/awesome-agent-skills<br>
**Category: D/B for an individual skill**. Audit, debugging and quality skill catalog; very broad global bulk-install instructions. **Do not use the README's install-all-skills approach**; select only after reviewing code, license and value.

### [G20] SWE-Skills-Bench (benchmark and corpus)

**Code:** https://github.com/ControllableModel/SWE-Skills-Bench<br>
**Revised paper:** https://arxiv.org/html/2603.15401v2<br>
**Category: A (research)**. Helps distinguish “known” from “evaluated”. The protocol's four positive skills are not a universal production shortlist; some tasks use ecosystems outside VCR's target (Go/Java). Pin the exact commit when discussing the tested version.

## 5. Token and cost optimization

### [G21] Microsoft — TokenEconomizer

**URL:** https://github.com/microsoft/TokenEconomizer<br>
**Publication:** https://www.microsoft.com/en-us/research/publication/tokeneconomizer-experience-driven-black-box-cost-control-for-coding-agents/<br>
**Category: B/C**. Agent cost-control plugin using micro-facts, tool filtering and failure-loop guards. Interesting research, but its hooks act on a runtime, configuration files and potentially local traces. The README table gives **specific supported version ranges**; Codex can change quickly. Never install automatically or promise a constant percentage.

**Before use:** actual Codex/Claude version; dependencies; hooks and commands; local files affected; extra model/judge; recorded data; network access; undo instructions; consent. First test in an isolated Codex profile and disposable repository, not personal projects.

## 6. Skill supply-chain security

USENIX Security 2026 study: https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi<br>
Specification: https://agentskills.io/specification

**Required entry before recommending a skill for installation:**

```text
ID and exact name:
Official link and maintainer:
Reviewed tag/commit:
License and redistribution:
Date of last commit/release:
Useful domain and target model(s):
Evidence of benefit (specific study / experience / none):
SKILL.md and script contents:
Dangerous actions / network / permissions / secrets:
Context cost and dependencies:
Overlap with installed skills:
Codex / Claude / version compatibility:
Minimal installation:
Uninstall and rollback:
Status: unverified / documented / reviewed / optional / discouraged
```

**Rule:** a very popular repository is still **G**, not **E**. Evidence that it works does not prove it significantly improves success.

## 7. Applied research program — no homemade performance benchmarks

**Priority work for Codex on demonstration repositories:**

| Research | Specific question | Documentary deliverable | Integration |
|---|---|---|---|
| Serena | TS/Python symbol navigation without overload? | Installation/risk/usage entry, fixture result capture | Future B |
| Codebase Memory MCP | Useful local call graph for a complex module? | Architecture/permissions/limitations entry; no token claims carried over | B/C |
| TokenEconomizer | Hooks compatible with the local version? Can configuration be isolated? | Version/rollback/risk entry | B/C |
| Harness² | Generalizable abstractions without autonomous recursion? | Eight components, two loops and security entry | C only |
| LangGraph | What concrete recovery/coordination problem justifies a graph? | Single-agent versus graph decision matrix | C |
| Pocock / Vercel / Superpowers skills | Which specific nonduplicative skills for which stacks? | Selection and provenance entry | B |

Prototype “proof of operation” includes **compatibility/functional tests** on fixtures. Do not call these a study proving token savings or publish comparative performance benchmarks, in accordance with the user's decision.

## 8. Additional relevant sources retained in the historical catalog

Serena, Aider RepoMap, Google Code Wiki, RepoAgent, Repomix, Feature-Sliced Design and its skill catalog, T3 stack, Astro, Django/HTMX, FastAPI, Ruby on Rails, RUFF/uv/pytest/Playwright, Gitleaks, OSV, GitHub Actions, Dependabot/Renovate, ESEM 2026, SWE-agent, METR and Anthropic context engineering. **Historical links and notes are preserved** in `reference/BIBLIOGRAPHIE_HISTORIQUE_v0.2.md`; do not copy everything into `AGENTS.md`.

## 9. What is not “proven” and must not be sold as such

- “Google Harness² is X% better than Codex” without a protocol; Harness² **uses** executors including Codex, and comparisons depend on baselines.
- “A graph + RAG costs fewer tokens”: no universal evidence.
- “The best model is X, the best framework is Y”: no stable ranking for our task profiles.
- “A course's 24,000 stars prove effectiveness”: adoption ≠ experimentation.
- “Fewer prompts = fewer euros/quota”: cached tokens, reruns and failures change the bill.
- “The loop rewrites itself, humans have no work”: defining evaluations, permissions, risks and goals remains critical.
