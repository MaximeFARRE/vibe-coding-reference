# Initial catalog: simple checks, evidence scope and priorities

`catalog/project_health_checks_v1.json` provides metadata and stable identifiers. **It does not assert that implementations exist.** Inspect the current VCR code before connecting each check.

## Principle: broad catalog, few checks run by default

- **Passive MVP (17 cataloged checks; start with 5–8):** Git inventory, README, `.gitignore`, manifests, lockfiles, validation and CI scripts, agent configuration, tracked sensitive paths. A *presence* check does not validate the mechanism.
- **Deeper MVP (4 checks):** run lint, type checking, tests and build **only** with consent and within the specification's security limits.
- **MVP signals (within passive and deferred checks):** migrations, backup/restore and vulnerabilities; use `not_checked` or report configuration presence only when behavior is not verified.
- **After MVP:** authentication, authorization, OWASP ASVS, mutation testing, SAST, GitHub Scorecard, restore tests, recurring agent errors and token cost. These topics are already covered by RESCUE or advanced documentation and must not be artificially converted into automatic checks.

## Detailed selection matrix

| ID | Assertion actually checkable | MVP method | Limitations and false positives |
|---|---|---|---|
| GIT-01 | Path is inside a usable Git repository | `git rev-parse` without writing | Says nothing about commit quality |
| GIT-02 | A `.gitignore` exists | Passive read | Does not prove all sensitive files are excluded |
| GIT-03 | A Git remote is configured | `git remote` | Remote ≠ working remote backup or GitHub publication |
| GIT-05 | A README exists | File scan | Does not prove commands are correct |
| ENV-01 | Runtime/dependency manifests are detectable | Known files | Some stacks use other formats; do not invent actual versions |
| ENV-03 | A relevant lockfile exists | Manifests/lockfiles | Does not guarantee complete reproducibility |
| ENV-05 | An environment example exists **if** variables are declared | Detect an explicit reference and example | Never print secret variables or the actual `.env` |
| CODE-01 | A linter is configured; optionally its execution succeeds | Passive discovery; consented execution | Configured ≠ executed; linters do not guarantee business quality |
| CODE-02 | Type checking is configured; optionally it succeeds | Same | JavaScript without TS can be legitimate |
| TEST-01 | A test command is defined; optionally tests succeed | Same | Existing/passing tests ≠ exhaustive behavior validation |
| BUILD-01 | A build command exists when applicable; optionally it succeeds | Same | Python scripts and static sites do not necessarily need builds |
| CI-01 | A known CI configuration exists | YAML/workflow files | Presence ≠ successful execution or safe permissions |
| CTX-03 | Agent instructions exist (informational only) | Read `AGENTS.md`, `CLAUDE.md` as appropriate | Absence is not a universal failure; size ≠ quality |
| SEC-01 | Git tracks potentially secret **filenames** | `git ls-files` without showing contents | Cannot establish that no secrets exist |
| DATA-02 | A migration mechanism is **detected** when persistence is established | Passive configuration/directory scan | Does not prove ordering, safety or rollback |
| DATA-06 | An identifiable backup strategy exists for persistent data | Declared docs/scripts | Presence ≠ effective backup; otherwise `not_checked` |
| DATA-07 | An explicit piece of evidence demonstrates restoration | Manual only in MVP | `not_checked` by default; never restore automatically |
| DEP-01 | A vulnerability scanner exists, then a scan is authorized | OSV-Scanner if present | Qualify alerts; no implicit network scan; missing tool ≠ no risk |
| AGT-06 | MCP or external-tool declarations exist | Detect without secrets | Permissions still need separate review |

**Status clarification:** a successful presence assertion establishes presence only. To answer whether tests pass, the engine needs a **separate** result or explicit execution evidence. A detected but unrun command is `skipped`, not `passed`. Ambiguous cases are `not_checked`, not `failed`.

## Applicability and severity rules

- Missing Git may be `failed` for an explicitly version-controlled software workflow, but must not block file analysis: degrade gracefully.
- Missing lockfiles are failures only for ecosystems and management modes that require them. For unlocked `requirements.txt`, suggest an appropriate tool and avoid automatically declaring a critical defect.
- Missing CI for a personal local script is generally `not_applicable` or advice, not P0.
- Missing `AGENTS.md` is not an error by default. Do not create one merely to pass a check.
- Migrations and backup depend on genuinely important persistent data; a `data/` directory is insufficient evidence.
- A P0 check must correspond only to a **confirmed critical-impact failure**, not merely a missing tool. P0/P1/P2 are resolution priorities where applicable, distinct from check statuses.

## What remains in RESCUE (not in the MVP automation)

Modular architecture, duplication, test quality, per-route/API security, access to other people's data, business rules, rewrite versus refactoring, documentation quality, token optimization, safe migrations, actual restoration and end-to-end tests. VCR may **indicate** they were not checked and suggest a RESCUE audit; do not claim to measure them by inspecting one file.

## Example user output

```text
Project Health Check — /my/project
Passive checks: 9 passed · 1 problem · 3 not checked · 2 not applicable

✓ GIT-01  Git repository detected
✓ GIT-05  README present (contents not checked)
! ENV-03  No lockfile identified for this Node project
? DATA-07 Data restoration not checked
– CI-01   CI not applicable to the local script profile

Priority: choose appropriate dependency locking.
No test or build commands were run. No comprehensive security conclusion is possible.
```

**Important:** this is a fictional example, not an actual run.
