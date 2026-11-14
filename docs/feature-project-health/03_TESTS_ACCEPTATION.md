# Implementation and acceptance plan — `vcr check`

## Step A — Audit existing work (required before writing)

1. Inspect Git status and uncommitted changes; overwrite nothing.
2. Identify the actual CLI entry point, existing collectors and checks, `Run`/`CheckResult`/`Finding` types, JSON schemas and renderers.
3. Record reusable functions and gaps. **Do not create a second runtime catalog or report format.**
4. Confirm test conventions, packaging, Python versions and runner safety. This package's product requirements must be adapted to the actual contracts.

## Step B — First vertical slice (deliver first)

1. Register `check` in the existing CLI (`--repo`, `--json`, `--format`, `--out`).
2. Connect existing collectors and produce 5–8 passive checks: Git, README, `.gitignore`, manifest, lockfile, lint/test configuration, without requiring every project to have these tools.
3. Normalize results to the existing `CheckResult` with evidence and reasons; record the profile and limitations.
4. Display French results and JSON conforming to the existing model. JSON stdout must remain one parseable value.
5. Verify non-destruction by comparing repository state before and after.

**Delivery criterion A:** the command actually works on Python and JS/TS fixtures without running target scripts, with appropriate `passed/failed/not_checked/not_applicable/skipped` statuses.

## Step C — Extend basic checks

Add useful passive catalog checks (CI, environment, tracked sensitive paths, migration/backup declarations with limitations, possible MCP). Do not multiply failures for optional checks. Select according to the detected profile. Explain what was not checked.

**Delivery criterion B:** no catalog check **claimed as supported** consists only of a TODO; others are explicitly marked documentation or not implemented.

## Step D — Full mode, consent and isolation

1. `--full` must recognize relevant commands and report that they were not run without consent; **no scripts run**.
2. Reuse an existing safe project runner, if available; otherwise add a minimal runner **only with explicit `--allow-project-commands`**, timeout, bounded output, cleanup and no installation.
3. Refuse or clearly warn if the repository is untrusted, the environment contains sensitive secrets, a sandbox is unavailable, or commands trigger indirect scripts.
4. Do not promise sandboxing without real isolation; consent does not replace isolation. If this is too complex for the MVP, **document and defer execution** rather than create an unsafe runner.

**Delivery criterion C:** automated tests demonstrate that commands are blocked without consent and that runner errors and timeouts are reported correctly.

## Step E — Connect START and RESCUE

- START: at the end of initialization, run the **same service** passively on the created directory; do not require production checks for a local script.
- RESCUE: use the service initially and after an approved repair; keep business-review findings distinct and do not duplicate findings.
- Do not change previous commands. If directory acquisition is still under development, provide a ready-to-call integration instead of simulating a result.
- IMPROVE: may consume `check` outputs **saved by the user**; no automatic monitoring in the MVP.

## Required test scenarios

| Test ID | Fixture / operation | Expected result |
|---|---|---|
| T01 | Python project with README and Git | Git and README checks `passed` with evidence |
| T02 | Node project with `package.json` and consistent lockfile | Lockfile `passed` (scope: verified presence and compatibility) |
| T03 | Node project without a lockfile | Warning/failure only if applicable, never an invented P0 |
| T04 | Static repository without a database | DATA-02/DATA-07 `not_applicable` if absence of persistence is established |
| T05 | Project with possible but uncertain persistence | `not_checked`, not a confirmed missing backup |
| T06 | Git-tracked `.env` in a fixture with dummy values | Tracked sensitive-file signal, **no values displayed** |
| T07 | No linter or pytest installed | `not_checked` or `skipped`, never a fabricated success |
| T08 | `--full` without `--allow-project-commands` | No script launched; non-execution clearly stated |
| T09 | `--json` | Valid JSON without stray logging, compatible with the agreed schema |
| T10 | No `--out` requested | No report written inside the target repository |
| T11 | Symlink pointing outside the repository | Do not follow the link or read its external target |
| T12 | Dirty Git state before `check` | No file or Git-state change after a quick check |
| T13 | A check fails internally | Degraded result or explicit error; other checks continue |
| T14 | Nonexistent `--repo` | Error exit code and actionable message |
| T15 | Final START and initial RESCUE on the same fixture | Same checks and statuses reused, without duplicate analyzers |
| T16 | Fixture stdout/stderr contains fake secrets | Redact before display/report; never copy source files |
| T17 | A tool hangs | Controlled timeout, no orphan command |
| T18 | Existing RESCUE test or CLI | No regression in existing contracts |

## Codex validation and delivery evidence

- Provide an implemented/partial/deferred table for each JSON catalog check.
- Run actually available tests and report commands and exit codes.
- Show **real** examples from Python and JS fixtures, with sanitized JSON/text excerpts.
- Summarize new files and changes to existing modules.
- Identify checks still requiring human review and safety limitations.
- Do not claim a complete security scan, validated restoration or token savings without evidence.
