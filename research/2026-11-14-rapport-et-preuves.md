# Evidence validation and decision report

- Date: 2026-11-14; status: decided for batch 2.
- Question: make findings verifiable and enable decisions without modifying the audited project.
- Sources: [batch 2 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md); [Finding schema](../schemas/finding.schema.json); [normalization](../src/vcr/normalize.py); [tests](../tests/test_normalize.py) and [decision workflow](../tests/test_decisions.py).

## Findings

- **Confirmed by functional tests:** a nonexistent line lowers status and confidence; duplicates are removed only when rule, cause and location agree. User decisions are stored outside the target for tested fixtures.
- **Limitation:** internal validation covers fields used by the prototype; tests check a subset of schema keywords, not full JSON Schema compliance. Environment files are not read to validate lines.
- **Not checked:** Windows and behavior when an actor simultaneously changes files and links during the operation.

## Options and decision

- Simple Python validation: no new dependency, readable rules and targeted checks; incomplete JSON Schema coverage and manual rule maintenance.
- Complete JSON Schema validator: broader standard contract; an additional dependency to install and maintain. Not chosen for this local batch without installation.
- Markdown report: inspectable without infrastructure; navigation and appearance depend on the reader. Static HTML is not needed at this stage.
- User decision in the report directory: target remains intact; moving the report requires keeping `run.json` and `feedback.json` together.

## Next

- Consider full JSON Schema validation in a quality batch if a dependency becomes acceptable; test on Windows and continue batch 3 START.
