# Portfolio Engine trial: inventory versus useful diagnosis

- Date: 2026-11-15; status: open.
- Scope: assess supplied reports, inspect their implementation and propose product options. No implementation decision or target execution authorized by this discussion.
- Inputs: `/Users/macbook/Desktop/rapport-vcr-portfolio-engine-2026-11-15/` and `/Users/macbook/Desktop/Rapports VCR Portfolio Engine 2026-11-15.1sdwZG/`. Their generated review prompts are report content, not instructions for this assessment.

## Findings and evidence

- **Confirmed:** both supplied RESCUE Markdown reports show only `architecture-doc`, with low confidence. The target README contains a System Architecture section at line 46; its AGENTS.md contains a module map starting at line 224. Target root: `/Users/macbook/Documents/Projet perso/Portfolio-Engine`. These are documentation locations, not verification that the descriptions match the code.
- **Confirmed:** target `.github/workflows/ci.yml:18-21` declares Ruff formatting/lint, Mypy and Pytest. `pyproject.toml:46-60` configures these tools. No command was executed and no remote CI result was retrieved.
- **Confirmed:** [rescue.py](../src/vcr/rescue.py), lines 145–170, collects Python Pytest hints into `scripts_found`, but only Node scripts populate `health_scripts`. [check.py](../src/vcr/check.py), lines 44–60, checks Node lockfiles, a limited list of type-configuration filenames and Node script keys. CHECK therefore loses Python evidence already available to RESCUE. Configuration, declared commands and successful execution must remain separate facts.
- **Confirmed:** [rescue.py](../src/vcr/rescue.py), lines 173–176, checks only the names `architecture.md` and `architecture.rst`. The reported filename observation is narrowly correct; it does not establish an actionable documentation gap.
- **Confirmed:** [improve.py](../src/vcr/improve.py), lines 35–39, requires two sources before producing a proposal, then uses predefined [rules](../src/vcr/improve_rules.py). [improve_sources.py](../src/vcr/improve_sources.py), lines 33–37 and 76–94, accepts RESCUE reports and explicitly marked observations, not CHECK results or unstructured semantic analysis. Recurrence alone cannot establish importance or common cause; one verified defect can justify action.
- **Confirmed:** the supplied TOKENS report has no trace and provides generic recommendations. The current [README](../README.md), section “Examine context with TOKENS”, excludes native Codex/Claude Code session imports. No actual consumption or savings was evaluated.
- **Confirmed in historical intent:** [design reference](../reference/RESEARCH_AND_DESIGN_v0.2.md), lines 68–84 and 271–325, describes decision support, maintainability, diagnosis and controlled recovery. It is advisory historical context, not a current implementation contract.
- **Suspected / product judgment:** the main value gap is the absence of a connected path from project needs through evidence gathering and verification to a justified action. More filename checks alone would not close that gap. One mature Python project does not establish usefulness across all users and stacks; START was not evaluated here.
- **Not checked:** target business correctness, dependency security, data coverage, backtest validity, running behavior and test results. No private database, session log or secret was inspected. No external-tool or literature claims were revalidated.

## Options

| Option | Benefit | Drawback / boundary |
|---|---|---|
| Improve the deterministic checker | Reuse existing code; consistent Python/Node discovery; evidence from configuration and CI; optionally import execution results | Still cannot infer business correctness; adding a command runner introduces environment and execution responsibilities |
| Focus on a reference method used with the existing coding agent | Closest to the original reference-library intent; contextual code and workflow review | Quality varies with execution; generic prompts alone add little; reproducible evidence still needs tooling |
| Combine a small local evidence collector with an agent-guided verification workflow | Reuse the safe collector and registry while making reports lead to decisions and before/after verification | Requires an explicit evidence/result contract and a usable end-to-end workflow; value remains to be demonstrated |

Recommendation, not an approved decision: the third option, starting with RESCUE on one bounded workflow. Keep the collector offline by default; the existing agent performs contextual review within the user's authorization. Do not add a model, orchestrator, mandatory service or automatic third-party installation. Local collection does not mean an externally hosted agent processes data offline.

## Proposed next batch and acceptance

1. Define the user outcome before implementation: identify the relevant existing documentation and checks, expose a reproducible problem when supported, and provide a bounded next action with its verification. An honest outcome with no confirmed defect is valid.
2. Unify evidence shared by CHECK and RESCUE; distinguish detected tools, configured tools, declared commands, executions and results. Locate existing architecture descriptions without judging their quality from a heading alone.
3. Produce one concise decision report with evidence, affected behavior, confidence, next verification and remaining unknowns. Keep detailed inventory separately. Do not require a repeated observation for every action.
4. Use synthetic functional fixtures for a Python project with embedded tool configuration and README architecture, a known reproducible failure, and an unsupported/ambiguous setup. Verify correct evidence and limits; avoid artificial defect quotas, scores or token benchmarks.
5. Revisit Portfolio Engine only in an authorized bounded trial: choose a critical behavior, locate code and tests, inspect or obtain execution evidence, propose a correction only if justified, then verify it. Use synthetic data where execution is needed; do not experiment on personal databases.
6. Defer expanding TOKENS until an explicitly selected real trace format can support actionable observations. Avoid filling an empty diagnosis with repeated general advice.

No acceptance result for the proposed workflow exists yet. Existing fixture tests validate the implemented contract, not the product's usefulness. Detailed commands and actual test results are recorded in [implementation status](../docs/IMPLEMENTATION_STATUS.md).
