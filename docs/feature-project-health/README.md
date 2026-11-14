# Vibe Coding Reference — Project Health Check add-on

**Proposed batch: `vcr check` — November 14, 2026.** Specification to integrate into the **existing VCR repository**, not a parallel project or standalone application.

## Place these files in the repository

Copy the files **without overwriting** existing files:

- `docs/feature-project-health/01_SPECIFICATION.md`: behavior, CLI, architecture and integration.
- `docs/feature-project-health/02_CONTROLES_ET_REGLES.md`: check selection and priority decisions.
- `docs/feature-project-health/03_TESTS_ACCEPTATION.md`: test cases and acceptance conditions.
- `docs/feature-project-health/04_SOURCES.md`: standards and references.
- `catalog/project_health_checks_v1.json`: initial **documentary** catalog, not executed until adapters are implemented.
- `prompts/02_CODEX_IMPLEMENT_CHECK.md`: mission prompt to copy into Codex.

Launch Codex in the existing VCR repository and provide the contents of `prompts/02_CODEX_IMPLEMENT_CHECK.md`.

**Important:** this kit is not a working tool. Codex must write the code, integrations with existing modules and tests. Do not present the JSON checks as already available.

## Documentation precedence

The **actual** architecture and contracts in the current repository take precedence over the illustrative structure of this kit. This add-on updates the product scope (a `vcr check` entry point) but must not break existing schemas or commands. Document differences between the specification and existing code before implementation.

## User goal

```bash
python -m vcr check --repo .          # quick, mostly passive, console output
python -m vcr check --repo . --json   # same result, machine-readable stdout
python -m vcr check --repo . --full   # full inventory; no project scripts without consent
```

START uses it as a final check; RESCUE uses it before and after correction; the user can run it manually. **One implementation of the checks.**
