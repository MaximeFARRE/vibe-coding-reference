# Agent instructions for Vibe Coding Reference

- This repository aims to provide a simple **local-first** tool for START, RESCUE, IMPROVE and TOKEN EFFICIENCY. Codex and Claude remain the existing agents; do not build a new agent or LLM.
- Start with `README.md` and `docs/IMPLEMENTATION_STATUS.md`, then read only the documents relevant to the current task. The long reference `reference/RESEARCH_AND_DESIGN_v0.2.md` is **advisory**; do not reread it in full by default.
- For research, consult `research/README.md` and only the relevant notes. Record new findings, options, benefits, drawbacks, sources and uncertainties in a dated note, then update the index.
- Audits of third-party repositories are non-destructive. Network access to public sources useful to the project is authorized; do not transmit secrets or private content, and keep VCR offline by default.
- Do not install anything, run target scripts, migrate, delete, commit, push or deploy without authorization.
- Produce verifiable results: distinguish `confirmed`, `suspected`, `not_checked` and `not_applicable`; cite actual paths, lines and commands; state limitations and risks.
- Prefer a simple Python monolith and minimal dependencies; no RAG, multi-agent graph, web service or automatic third-party skills.
- Functional tests on fixtures are required; **no** homemade performance or token benchmarks. Never promise savings based on a third-party study without context.
- Do not invent issues or metrics to fill a report; respect business rules and existing Git changes.
- At the end of a work batch, update `docs/IMPLEMENTATION_STATUS.md` with commands and tests actually run, limitations and the next batch. If the file is missing, create a short one.
