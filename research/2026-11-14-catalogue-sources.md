# Local catalog: links, evidence and maintenance

- Date: 2026-11-14; status: decided for batch 6.
- Question: make sources and tools browsable without installation or artificial ranking.
- Sources: [batch 6 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [catalog](../src/vcr/catalog.json), [loader](../src/vcr/catalog.py), [tests](../tests/test_catalog.py).

## Findings and limitations

- **Confirmed by public consultation:** the nine official links and two listed scientific links were opened on 2026-11-14. An accessible page validates neither security, results nor local compatibility.
- **Confirmed by public GitHub metadata:** eight repositories were not archived, and their last-push dates are recorded in the entries with source and consultation date. This signal does not establish support quality.
- **Confirmed by official documentation:** licenses shown in the eight repositories were recorded, including [Serena](https://github.com/oraios/serena): GPL-3.0-or-later application, MIT SolidLSP component. Actual licenses may vary by version and component.
- **Confirmed on fixtures:** topic filtering, separation of link/maintenance/evidence, rejection of incomplete URLs and no default recommendation. The catalog loads offline, including from a fixture ZIP package.
- **Not checked:** code security, compatibility with local versions, installation, actual removal and independent effectiveness. All evidence ratings remain `unverified`; no tool was installed.

## Options and decision

- Packaged JSON and tag search: simple, offline, inspectable and API-free; entries require dated manual review.
- Dynamic remote directory: potentially more current data; additional network, permissions, trust and maintenance. Rejected: VCR stays offline by default.
- Decision: explicit date and provenance; do not confuse opening a link, GitHub activity and evidence of results. Reassess before trying or adding a tool.
