# Existing foundation and research

- Date: 2026-11-14; status: open.
- Question: where are the decisions, evidence and limitations predating this notes directory?
- Scope: existing project references; no new independent review of the publications.

## Findings and references

- **Confirmed in documents:** intended workflows are START, RESCUE, IMPROVE and TOKEN EFFICIENCY; RESCUE is the priority. Sources: [vision](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/01_VISION_ET_DECISIONS.md), [backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md).
- **Documented state:** the RESCUE prototype is partial; 8 fixture tests were run during its development. Coverage and limitations are in the [implementation status](../docs/IMPLEMENTATION_STATUS.md). This does not establish the state of a future version.
- **Existing research, not rechecked here:** the [critical review](../docs/04_RECHERCHE_ET_SOURCES.md) lists publications, limitations and sources; the [tool review](../docs/05_PROJETS_EXTERNES_ET_SKILLS.md) documents options and risks. Detailed historical reference: [v0.2](../reference/RESEARCH_AND_DESIGN_v0.2.md). Check primary sources and their currency before repeating a claim.
- **Documented decision:** local Python monolith and minimal dependencies; no added LLM, web service or mandatory advanced integration. Source: [architecture](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/02_ARCHITECTURE_ET_CONTRATS.md), sections 1–3.

## Preservation options

- Indexed Markdown and text search: easy to edit, read and version; the index needs maintenance and searches depend on wording.
- Structured database or vector index: potentially more sophisticated search; additional infrastructure, synchronization and maintenance. No demonstrated need at this stage.
- Decision: concise Markdown with references, without bulk copying. Reassess if actual searches fail to find relevant material.

## Uncertainties and next steps

- This note does not verify historical external sources or their present-day applicability.
- Future notes must distinguish observed findings, hypotheses and attributed conclusions, and describe rejected options when actually examined.
