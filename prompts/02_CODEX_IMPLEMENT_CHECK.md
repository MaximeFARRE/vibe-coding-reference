# Codex mission — integrate `vcr check` into Vibe Coding Reference

Work **inside the existing VCR repository**, whose first phase may still be incomplete or partially implemented. DO NOT create a new project, a new general-purpose scanner, or a graphical interface. The scope is the cross-cutting Project Health Checklist module.

## Documents to read progressively

1. `docs/feature-project-health/01_SPECIFICATION.md` (product, CLI, security, statuses, integration).
2. `docs/feature-project-health/02_CONTROLES_ET_REGLES.md` (exact scope of evidence).
3. `catalog/project_health_checks_v1.json` (check registry, NOT evidence of implementation).
4. `docs/feature-project-health/03_TESTS_ACCEPTATION.md` (batch order and fixtures).
5. `docs/feature-project-health/04_SOURCES.md` only when needed for a technical decision.

## Main instructions

1. **First** inspect `git status`, the actual architecture, CLI entry point, START/RESCUE workflows, checks and collectors, result models, schemas and tests. Never destroy uncommitted work. Briefly explain what can be reused and where the command will connect.
2. Implement a **real** `python -m vcr check --repo .` command with a small initial set of passive, project-appropriate checks using existing functions. Produce consistent readable and JSON results without inventing evidence.
3. Add useful catalog checks without unnecessary abstract subsystems; `passed` refers only to the assertion actually verified, never to the whole project being healthy.
4. Add `--full` to discover deeper commands, **but do not run project scripts without explicit permission**. Implement `--allow-project-commands` only if a sufficiently safe runner exists or can be built simply; otherwise defer execution and explain the limitation. Never claim a file copy is a sandbox.
5. Connect the same engine to START (final check) and RESCUE (before and after correction) when their extension points exist. Do not break existing workflows; if a part is not yet developed, leave a minimal documented integration point without claiming it works.
6. Run Python and JS/TS fixture tests; add non-destruction, CLI compatibility and JSON tests. Document how to run the new command and interpret statuses.

## Security constraints

- Default mode must not write, execute target code, access the network, or install software.
- No automatic external or internet scanning and no access to production data.
- Never display secret values or copy them into reports.
- Tests and builds can write files and execute arbitrary code: they require consent **and** documented safety conditions.
- Never automatically fix or delete code, or modify the audited repository.
- No 0–100 quality score, invented coverage rate, or conclusion that a project is secure based on a partial scan.
- Do not load all earlier research into context; open sources as needed.

## Completion criteria

Present changed files, exact CLI behavior, real examples from two fixtures, test results and commands, implemented versus deferred checks, limitations and regression risk. Finish with a short plan to enable remaining checks progressively; make no unsupported token-savings promises.
