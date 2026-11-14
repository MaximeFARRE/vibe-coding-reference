# Functional exercise and GitHub preparation

- Date: 2026-11-14; status: decided; remote CI verified on the commit identified below.
- Question: is the local workflow reproducible and what remains to check before distribution?
- Sources: [batch 7 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [journey](../tests/test_journey.py), [CI](../.github/workflows/ci.yml), [implementation status](../docs/IMPLEMENTATION_STATUS.md).

## Findings

- **Confirmed on a fixture:** START → two RESCUE runs → IMPROVE → TOKENS → SOURCES works and preserves the fictional project's files and Git status. The test blocks Python sockets; it does not establish general system network isolation.
- **Confirmed:** the inventory limit could hide truncated collection; it is now reported as `not_checked`, with a regression test.
- **Confirmed on macOS/Python 3.12:** `pip install .`, the CLI and catalog resource, followed by `pip uninstall`, worked in a temporary virtual environment. A separate wheel was also built and installed. Build dependencies were downloaded only into the temporary environment.
- **Confirmed locally:** README examples work on an artificial project; the four CI combinations are syntactically described and issue templates have the expected fields.
- **Confirmed in CI:** [run 43602137084](https://github.com/MaximeFARRE/vibe-coding-reference/actions/runs/43602137084) succeeded on commit `200c0763ded987241c7dbed3da1399f27c481f00` for Ubuntu/Python 3.11–3.13 and macOS/Python 3.12.
- **Not checked:** Windows, editable installation, usability by an outsider; VCR's JSON Schema validation remains partial.

## Options and decision

- `unittest` and standard-library syntax checks: no test dependency; less static analysis than dedicated tools.
- Add lint and test frameworks: potentially more rules; installation and maintenance need justification. Not selected for this batch.
- Decision: lightweight CI on Python 3.11–3.13 on Ubuntu and 3.12 on macOS; no comprehensive security guarantee.
