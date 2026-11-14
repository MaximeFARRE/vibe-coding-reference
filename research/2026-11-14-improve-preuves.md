# IMPROVE: recurrence and supervised registry

- Date: 2026-11-14; status: decided for batch 4.
- Question: propose improvements from selected sources without inventing recurrence or modifying the project.
- Sources: [batch 4 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [collection](../src/vcr/improve_sources.py), [registry](../src/vcr/improve_registry.py), [report tests](../tests/test_improve.py), [note tests](../tests/test_improve_notes.py).

## Findings

- **Confirmed on fixtures:** two RESCUE reports for the same project and rule produce one proposal and two references; a single source remains to be monitored. The same `run_id` or copied text does not create a second occurrence.
- **Confirmed on fixtures:** human decisions persist when resumed; a RESCUE false positive is removed from the registry when its report is reimported. Text sources without an explicit marker are not interpreted or copied.
- **Limitation:** two observations can reflect one persistent state, without repeated incidents or a common cause. Statuses and evidence are declared by provided sources, not independently confirmed.
- **Not checked:** semantic analysis of logs or instructions; Windows compatibility; usability by an outsider.

## Options and decision

- Explicit rules and text markers: simple and inspectable; limited recognition, manual marking required for notes and logs.
- Automatic semantic analysis: potentially richer interpretation; risk of invented conclusions, sensitive data and an additional dependency. Not selected for this prototype without an added model.
- Decision: use only selected sources; timestamped registry outside the target, reversible proposals for human review and no automatic application. RESCUE feedback is synchronized only when reports are reimported.
