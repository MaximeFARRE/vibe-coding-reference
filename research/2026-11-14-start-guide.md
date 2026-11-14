# START: scoping and conditional recommendations

- Date: 2026-11-14; status: decided for batch 3.
- Question: turn an idea into usable documents without a new agent or installation.
- Sources: [batch 3 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [START playbook](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/06_PLAYBOOKS_ET_AUDITS.md), [questionnaire](../src/vcr/start_questions.py), [options](../src/vcr/start_options.py), [tests](../tests/test_start.py) and [stack cases](../tests/test_start_options.py).

## Findings and limitations

- **Confirmed on fixtures:** answers are reused without repetition; missing fields are requested; supplied action and outcome appear in criteria; six profiles produce conditional options with benefits, drawbacks and qualitative costs.
- **Confirmed on fixtures:** local/public contradictions and sites with sensitive or persistent data are flagged; existing directories are not overwritten.
- **Limitation:** options are indicative rules, not a comparison study or guarantee of suitability; needs, costs and criteria require human validation. Answers are saved in plain text without a secret detector.
- **Not checked:** Windows and usability by someone outside the project.

## Options and decision

- Deterministic questionnaire and Markdown: local, inspectable and reusable; wording and rules limited to anticipated cases.
- External model: potentially richer interpretation; additional dependency, cost and data processing. Not selected under the local-first scope without a new agent.
- Decision: versioned JSON answers, Markdown documents and an optional prompt for an already chosen agent. Missing answers are stated rather than inferred.
