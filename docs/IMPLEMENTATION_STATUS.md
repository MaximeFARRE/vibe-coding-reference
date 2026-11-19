# Prototype status

## Cleanup — November 19, 2026

Removed the obsolete seven-file CHECK implementation kit and documentary catalog. Its historical material remains in Git at `d53401d`. Fixed CHECK quick mode and added a regression assertion. Existing research changes were preserved.

Verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q` passed 68 tests. `git diff --check` passed. Next: evaluate the product value and consumers of IMPROVE, TOKENS and SOURCES before changing their commands or stored formats. External use remains unknown.

## VCR self-audit — November 19, 2026

Audited the local VCR tree at `d53401d`. The [audit note](../research/2026-11-19-vcr-self-audit.md) records the inventory, traced maintenance scenarios, duplicated evidence and decision paths, and candidates for retirement. Only audit documentation was added or updated.

Verification on macOS with Python 3.12.9: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q` passed 68 tests. Git inventory and history commands, `rg` and `wc -l` supported the source review. Temporary fixtures exercised `python3 -m vcr check`, `rescue` and `improve`, reproducing the Node and Python evidence differences, unintended full-mode rows, and the two-report proposal gate. No fixture scripts ran. Downstream users, Windows and remote CI were not checked.

Next proposed batch: consolidate passive test evidence for CHECK and RESCUE, fix quick/full behavior and verify a useful next action from one scan. Keep existing CLI and report contracts while assessing which secondary features and obsolete instructions can be retired.

## Portfolio Engine trial review — November 15, 2026

Reviewed the two supplied report directories, the VCR implementation, relevant research/design sections, and the target's README, AGENTS.md, Python configuration and CI declarations in read-only mode. Recorded confirmed detection gaps, the broader product-value hypothesis, three options and proposed functional acceptance criteria in [the research note](../research/2026-11-15-portfolio-trial-product-gap.md). No product code, target files, commits, installations or deployments were changed. The existing untracked `.DS_Store` was preserved.

Checks: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q` passed 68 existing fixture tests. Reads used `rg`, `cat`, `nl -ba` and `sed`; `git status --short` identified pre-existing work. These tests confirm the existing implementation contract, not useful diagnosis on a real project. No Portfolio Engine scripts were run, no private database or session trace was read, and remote CI, dependency security and business correctness were not checked.

Next proposed batch, pending product direction: define one useful end-to-end RESCUE outcome, unify Python/Node evidence across CHECK and RESCUE, and validate a bounded evidence-to-action workflow with synthetic functional fixtures. The recommendation is discussion material, not an approved refactor.

Latest initial batch: 7, with local checks and GitHub CI on `feat/initial-publication`; the main branch had not yet been merged at that point. Python 3.12.9 on macOS; Linux checked in CI, Windows not checked. The owner chose the MIT license.

Features: START scopes an idea; RESCUE performs a passive audit; IMPROVE offers supervised proposals; TOKENS accepts a VCR trace or one selected OpenAI/Anthropic API response; SOURCES filters nine local entries by topic. VCR contacts no service and installs nothing. Agents may consult useful public sources over the network.

Verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed on macOS/Python 3.12. Syntax was checked with `ast.parse` and the CI and three issue templates were read as YAML locally. The full fixture journey blocks Python sockets, verifies outputs and preserves files and Git status; README examples were run. The inventory limit is now reported as incomplete when reached.

Installation: a wheel was built and installed; `python -m pip install .` and `python -m pip uninstall vibe-coding-reference` were verified in temporary macOS/Python 3.12 virtual environments; CLI, packaged catalog and RESCUE were tested on a fixture. Build dependencies were downloaded into the temporary environment; no system package was modified. Editable installation and Windows were not verified.

CI: [GitHub run 43602137084](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602137084) succeeded on commit `200c0763ded987241c7dbed3da1399f27c481f00`: Python 3.11–3.13 on Ubuntu and 3.12 on macOS, without a test dependency. The YAML and issue templates were also read locally. No personal data or performance/token benchmark was used.

Limitations: TOKENS does not read native Codex/Claude Code session logs; counters and costs are declarations. The nine catalog links and metadata were consulted on 2026-11-14, without a security audit or general proof of effectiveness. START stores answers in plain text; RESCUE only partially checks schemas and monorepos; IMPROVE does not establish common causes. No external usability validation, HTML or automatic sorting.

Backlog cases T001–T015 were covered; T007 was simulated and T013 tested with spaces on macOS and Ubuntu, not Windows. The then-next step was branch review and a merge decision, followed by prioritizing actual limitations from user feedback.

## GitHub presentation — November 14, 2026

The README was reorganized around the five workflows, prototype status and an explicit `feat/initial-publication` clone; the initial launch folder was marked historical. The README was prepared for the default branch after merging.

Checks for this batch on macOS/Python 3.12.9: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed. The README RESCUE example (two reports), IMPROVE, `tokens` and `sources --topic tokens` were run on a temporary fictional project; both expected Markdown reports existed. `git diff --check` reported no errors. The displayed clone and interactive START journey were not replayed in this batch; Windows and editable installation remained unverified.

GitHub was consulted read-only: `main` was the default branch; `feat/initial-publication` was 91 commits ahead and 0 behind at that time. [CI run 43602244697](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602244697), on `c41ce65`, passed its four configurations. These observations preceded the publication changes below.

## Publication preparation

A bilingual landing README was prepared with CI, Python and license badges, a workflow diagram and a detailed French guide. Contribution guidelines, a code of conduct, pull request and bug-report templates, changelog and roadmap were added. Outside feedback, Windows and editable installation remained to be verified.

Local verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed on macOS/Python 3.12.9. [Pull request #1](https://github.com/MaximeFARRE/vibe-coding-reference/pull/1) was merged after all four CI configurations passed; private vulnerability reporting was enabled. Next steps were the first prerelease, outside trials and feedback handling.

## English and French READMEs

The main README was made fully English; the French guide remains in `README.fr.md`, with links both ways. VCR reports and menu remain in French. Public contribution, security, conduct, roadmap and changelog documents are also English; historical and technical documents and research notes remained French at that stage.

Verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed on macOS/Python 3.12.9; fictional RESCUE, IMPROVE, TOKENS and SOURCES examples were run; local links in both READMEs and `git diff --check` were verified. Translation of remaining technical documentation and review by English-speaking readers remained open.

## Repository cleanup

The merged initial brief, duplicate initial prompt and SHA-256 manifest for the historical documentation kit were removed. Local copies are kept in `.vcr-local-archive/`, ignored by Git; they matched `origin/main` at cleanup time. Research notes and their linked sources, backlog, instructions and referenced launch prompt remained. Removed files remain in Git history; the local archive is not distributed in new clones.

Verification on macOS/Python 3.12.9: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed; `git show ... | cmp` confirmed the three local copies were identical; `git check-ignore` confirmed exclusion; `git diff origin/main --check` reported no errors. The next step was PR CI and user feedback review; do not remove referenced historical sources without addressing their links.

## Retirement of the initial construction kit

The launch README, initial delivery backlog, bootstrap prompt and old vision, target architecture and playbook documents were removed. Their copies are in `.vcr-local-archive/`, ignored by Git and absent from new clones. Research notes remain; their links to removed documents now point to GitHub commit `c8d94cb14c27270f430277034d4b280431001d3f` and require a connection. Research notes and references, including historical corrections and decisions, are preserved. AGENTS.md uses current entry points.

Verification on macOS/Python 3.12.9: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v`: 59 tests passed; the six local copies matched `origin/main` via `git show ... | cmp`; `git diff origin/main --check` reported no errors. The next step was review and CI before integration; assess research-document organization separately.

## Project Health Check — November 14, 2026

`python3 -m vcr check` reuses RESCUE's bounded inventory, script detection and passive Git commands. It offers text or JSON output, optional `--repo`, a non-executing `--full` mode and exclusive `--out` creation outside the target. The existing `Run` model and 0.1 schema now accept the `check` workflow and optional evidence, method, applicability and limitation fields. Existing RESCUE reports remain compatible. The new catalog is documentation, not runtime configuration.

Partial checks cover GIT-01, GIT-02, GIT-03, GIT-05, ENV-01, ENV-03, ENV-05, CODE-01, CODE-02, TEST-01, BUILD-01, CI-01, CTX-03 and SEC-01. They examine limited conventions and the filtered inventory. ENV-03 associates a Node manifest and lockfile in the same directory but does not validate their contents or compatibility. SEC-01 looks only for tracked `.env` names. ENV-05 checks example filenames without reading them; CODE-02 checks configuration filenames without executing a type checker. No check establishes security, CI success, secret absence, restoration or business correctness. DATA-02, DATA-06 and AGT-06 are not implemented. DATA-07 and DEP-01 are not in the check list; restoration and dependency vulnerabilities are listed as unverified limitations.

In `--full` mode, detected nonempty Node `lint`, `typecheck`, `test` and `build` scripts are marked `skipped`; they are not executed. Before output, internal validation checks IDs, statuses, optional fields and evidence types and paths, and requires evidence for conclusive check results. Invalid results produce exit code 2 without publishing JSON. This is not a complete JSON Schema validator. Evidence may omit nested paths, and applicability can remain uncertain. Ignored, excluded and oversized files are not examined; monorepo coverage is partial.

START does not create a project and RESCUE does not repair code, so final START and pre/post-repair RESCUE integration remain deferred. IMPROVE does not consume check outputs. There is no project-command runner or `--allow-project-commands` option. The checks are local deterministic rules: no AI, network, installation or target scripts are used.

Earlier local verification: 62 tests passed after the first slice, 65 after structured evidence, and 68 after validation. Python/Git and Node fixtures demonstrated README and Git detection, Node lockfile detection, and skipped test execution; fixture tests cover masking, evidence, separate subprojects and RESCUE compatibility. Windows and complete manifest interpretation remain unverified.

## Release preparation — November 14, 2026

The English README and changelog document the new passive `check` command and its limitations. The feature was tested on macOS/Python 3.12.9 with `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q`: 68 tests passed. No tag, push or release has been created. The project still contains French documentation, including historical references and research; translating and reviewing it is required before the requested English-only documentation is complete. The CLI and reports remain in French. The feature branch contains earlier repository-cleanup commits, which the owner explicitly requested to include.

The README `check` JSON stdout and external-file examples were also executed on a temporary Node fixture: both returned 0, detected the colocated lockfile, and `--full` reported the test script as skipped. `git diff --check` reported no errors. `AGENTS.md` was translated while preserving its existing instructions. The owner requested English documentation and inclusion of the earlier cleanup commits. The health-check catalog, specifications and implementation prompt have since been translated and committed; translation and review of other French documentation remains pending. The pre-existing `.DS_Store` remains untracked.

## English documentation — November 14, 2026

The health-check specification, check rules, acceptance plan, sources, kit README, implementation prompt and documentary catalog were translated into English and committed. The implementation history, research index and three workflow research notes were also translated. Historical references, other research and technical documents, and `README.fr.md` remain in French. The catalog remains specification-only and is not executed. No release, tag or push was created.

Verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q`: 68 tests passed on macOS/Python 3.12.9. `python3 -m json.tool catalog/project_health_checks_v1.json` parsed the translated catalog. Next: complete and review the remaining translations, then verify links and the whole release branch.

The owner clarified that `README.fr.md` is the French translation of the main README and must remain in French. The catalog and functional-verification research notes were translated; historical references, other technical documents and remaining research still need English translations. Documentation-only changes were checked with `git diff --check`; the 68-test run above remains the latest code verification. Next: continue the remaining translations while preserving the French README.

## English documentation — research and technical references

Translated the remaining two research notes, critical research review, external tools/skills catalog, revisions and open decisions, and TOKENS trace format. All Markdown link targets and external URLs in these six files match their prior versions; the JSON and shell examples in the trace-format document are unchanged. The notes preserve dated research and do not establish current findings. `README.fr.md` remains intentionally French and has pre-existing uncommitted additions. The three documents in `reference/` remain to be translated and reviewed; they are historical source material, not current implementation claims.

Verification: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q`: 68 tests passed on macOS/Python 3.12.9. A local Python comparison checked the six files' Markdown targets and URLs and the trace document's fenced JSON/shell blocks; `git diff --check` passed. Next: translate the remaining historical references without losing citations, caveats or links; recheck documentation links before release.

## Stable release preparation — November 14, 2026

Prepared version `0.1.0` (the package already declares that version), updated the changelog and French guide, and retained the three historical references and `README.fr.md` in French as requested. The existing `v0.1.0-rc.1` prerelease remains historical. The product remains a prototype with partial passive checks and the limitations above.

Verification on macOS/Python 3.12.9: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -q` passed 68 tests. A temporary virtual environment built a wheel with `python -m pip wheel .`, installed it using `python -m pip install --no-index --find-links <wheel-directory> vibe-coding-reference==0.1.0`, confirmed the installed version, and ran installed `vcr check --json` on a temporary directory. Build dependencies were downloaded into the isolated build environment. Windows and editable installation remain unverified. GitHub CI and publication are checked separately after this preparation.
