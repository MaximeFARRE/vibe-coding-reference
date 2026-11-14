# Product and technical specification — `vcr check`

**Status: feature proposal, v1.0, November 14, 2026.** Adapt after inspecting the existing repository.

## 1. Problem and desired outcome

Codex/Claude Code users do not always know whether their projects have the necessary security, reliability and maintainability foundations. They need a repeatable, jargon-free check that distinguishes established facts from checks not performed. `vcr check` should:

1. recognize repository characteristics (Git, JS/TS, Python, persistence, CI, etc.);
2. select checks that actually apply, without a universal mandatory list;
3. run safe passive checks and, with explicit authorization, more expensive checks;
4. produce a clear text report and the same observations in structured JSON;
5. show **what was NOT checked**, limitations, evidence and suggested remediation;
6. support START and RESCUE **without duplicating their analyzers**;
7. never produce a 0–100 score, an “everything is secure” conclusion or fictional token savings.

## 2. Scope and exclusions

**MVP:** local Python, reuse of existing collectors/checks and models, simple stack detection, repository inventory, supportable statuses, JSON/text or Markdown, basic checks in `02_CONTROLES_ET_REGLES.md`, and JS/TS and Python fixture tests.

**Deferred / documentation:** GUI, persistent service, custom plugin system, database storage, scoring, RAG, knowledge graph, new AI, automatic tool installation, automatic fixes (`--fix`), mutation tests, penetration tests, complete compliance audit and automatic backup-restore verification. Deep audits remain in RESCUE.

## 3. Simple use and interfaces

The preferred command is `python -m vcr check` (`vcr check` only if an installed entry point already exists). Do not introduce a new CLI framework such as Click/Typer if `argparse` is used.

```bash
python -m vcr check --repo .
python -m vcr check --repo /path/to/project --json
python -m vcr check --repo . --full
python -m vcr check --repo . --full --allow-project-commands
python -m vcr check --repo . --out /external/path/report.json --format json
```

- `--repo`: defaults to the current directory; display and record the actual checked path.
- `--json`: JSON only on stdout, without stray logs or banners; equivalent to `--format json`.
- `--format text|json|md`: text by default. Markdown is optional if a renderer already exists.
- `--out`: explicit file path; **never write implicitly inside the checked repository**. Refuse overwriting without consent; stdout by default.
- `--full`: selects deeper checks but **does NOT** authorize scripts in the audited repository.
- `--allow-project-commands`: explicit consent to run detected and permitted commands (tests, lint, build), only under the restrictions below. Without it, use `skipped` with the reason “project command not authorized”.
- Do not add `--allow-network` by default in the MVP. Network-dependent checks are `not_checked` or `skipped` as appropriate; a future network option must specify destinations, permissions and the lack of guaranteed isolation without a sandbox.

**Suggested exit codes:** `0` when execution completes with no *confirmed* failures among applicable checks, even if `not_checked` results remain explicitly visible; `1` if an applicable check confirms a failure; `2` if the command cannot execute correctly (arguments, invalid target, crash). Do not present `not_checked` as success. Adjust only for a different documented CLI convention, and state the convention used.

## 4. Status and evidence model: respect existing code

The initial VCR brief already has `run.schema.json` and check statuses `passed`, `failed`, `skipped`, `not_checked`, `not_applicable`. **Reuse exactly these five values** where present; do not create a second enumeration. Epistemic *finding* statuses (`confirmed`, `suspected`, etc.) are a **different** concept.

| Status | Exact meaning | Example |
|---|---|---|
| `passed` | Check **performed** with positive evidence of the exact assertion | `git rev-parse` confirms the target is a Git repository |
| `failed` | Applicable assertion checked and found false | Tests ran with a nonzero exit code; required README missing |
| `skipped` | Requested check intentionally not performed | Tests found but code execution not authorized |
| `not_checked` | Insufficient evidence, missing tool or unknown mechanism | Backup presumed to exist but restoration not tested |
| `not_applicable` | Check outside scope with explicit justification | Database migrations for a static page without persistence |

**Minimum result fields:** `id`, `status`, `reason`, `evidence` (in the existing structure or a stable reference), `applicability_reason`, `source_method`, `duration_ms` when executed, command/version when used, and suggested action when relevant. Avoid breaking changes to `run.schema.json`: add optional fields while preserving consumers. The old schema permits `workflow` ∈ `start,rescue,improve,tokens`; extend it additively to `check` for the standalone command **if and only if** the code exists and consumers are adapted and tested. Preserve schema migration history when needed.

**Presence** checks never prove **operational quality**. For example, `.github/workflows` ≠ CI actually executed; a `migrations/` directory ≠ safe migrations; `AGENTS.md` ≠ useful instructions. Name assertions at the exact level supported by evidence (“configuration detected”, not “feature validated”).

Separate automatic check results from `findings` (demonstrated problems or hypotheses). An inconclusive check does not create a confirmed finding. Deduplicate with RESCUE by check ID, location and evidence without overwriting enriched audit findings.

## 5. Architecture: **reuse the current engine**

```text
START (final check) ────┐
RESCUE (pre/post) ──────┼──> shared service run_checks(repo, profile, options)
User: check ────────────┘           │
                                   ├── profile/applicability
                                   ├── EXISTING Git / manifest / file collectors
                                   ├── EXISTING checkers + minimal added checks
                                   └── structured results + evidence
                                               │
                                  CLI text/JSON; RESCUE reports; IMPROVE
```

1. Audit `src/vcr/checks`, `collectors`, `domain` and actual workflows before coding. If modules are organized differently, keep their conventions.
2. Add only CLI registration for `check` and reusable orchestration **if missing**.
3. The JSON catalog is metadata, not an interpreted rules language, plugin engine or new database; Python tests do the work.
4. Respect current JSON/Markdown renderers; **one result set, multiple outputs**.
5. Do not change existing `rescue` options; RESCUE consumes the same `CheckResult` objects.
6. START need not run every test: invoke the final quick profile, then suggest `--full` for deeper validation.
7. IMPROVE consumes explicitly provided history; do not run hidden monitoring.

## 6. Applicability conditions

- Choose profiles using reliable clues: `package.json`, `pyproject.toml`, `requirements.txt`, lockfiles, declared framework, `migrations/`, CI configuration. One file may be insufficient; document ambiguity.
- Do not require a backend for a static site, migrations for a program without a database, or public deployment for a local tool.
- Do not make GitHub mandatory: a non-GitHub Git remote is acceptable, and remaining unpublished may be an explicit choice.
- Do not impose `AGENTS.md` on small repositories. Its content should be short, but no fixed line threshold is universal.
- Do not impose an arbitrary overall coverage percentage or minimum test count.
- Justify `not_applicable`; **when applicability is uncertain, prefer `not_checked`**.

## 7. Security and non-destruction

**Quick mode:** passive filesystem and metadata inspection; read-only Git commands; no installation, repository scripts, unapproved external commands, target writes or network. Avoid symlinks outside the repository and filter sensitive paths.

**Full mode:** tests/lint/build can write caches, generate files or run arbitrary code, including through plugins. NEVER claim they are passive. `--full` alone discovers commands and reports them unrun; `--allow-project-commands` explicitly authorizes them for a **trusted** repository. Recommend a real sandbox without secrets, ideally on an isolated copy; a simple file copy is **not** a security sandbox. Without sufficient isolation, prefer asking Codex to execute in its controlled environment over creating a privileged runner. Limit time, output, CPU and memory where possible; stop cleanly on timeout. Do not install dependencies without consent.

- Do not publish secret values: redact sensitive stdout, stderr and artifacts; test redaction.
- Do not include unnecessary sensitive absolute paths or private information in shareable reports.
- Do not send the repository to an external API in the MVP; the existing host model remains the review agent.
- Do not follow symlinks outside the target or run arbitrary user-defined scripts via a shell string. Prefer an explicit allowlist of tool-built executables and arguments; project content can still be untrusted.
- Distinguish **reported** vulnerabilities from actually exploitable ones; use `osv-scanner`/`gitleaks` only when present and appropriately authorized. Never claim “0 secrets” from a simple heuristic.
- Project tests can have external effects even on a local copy: security is not guaranteed without network/process isolation and credential protection.

## 8. Completion criteria

- An executable user command: `python -m vcr check --repo <fixture>`.
- Both Python and TS/JS fixtures demonstrate all five statuses **in context**.
- JSON and text use the same data, without false positives or sensitive data.
- `--full` without authorization **does not run** project scripts.
- `--allow-project-commands` runs only what the user approved, with documented operational limits.
- START and RESCUE reuse the same checks without duplicate scanners.
- Existing RESCUE commands and schemas still pass their tests.
- User documentation in French (copy-and-paste examples), explicit limitations and a versioned catalog.
