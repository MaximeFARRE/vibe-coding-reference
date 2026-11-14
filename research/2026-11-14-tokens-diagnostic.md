# TOKENS: diagnosis and declared data

- Date: 2026-11-14; status: decided for batch 5.
- Question: make context-related options understandable without inventing quotas, costs or savings.
- Sources: [batch 5 backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [TOKENS playbook](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/06_PLAYBOOKS_ET_AUDITS.md), [import format](../docs/TOKEN_TRACE_FORMAT.md), [calculations](../src/vcr/tokens_analysis.py), [tests](../tests/test_tokens.py) and [validation](../tests/test_tokens_trace.py).

## Findings and limitations

- **Confirmed on fixtures:** without a trace the diagnosis is descriptive; missing cache or cost fields are `unavailable`, with no invented monetary value. Cumulative counters and calculated sums are distinguished; no subscription quota is inferred.
- **Confirmed on fixtures:** partial traces, mixed currencies, unknown formats, duplicate fields and invalid values are handled explicitly; dummy identifiers, fingerprints and sensitive contents are not copied.
- **Limitation:** measurements and costs are declared by the importer, not verified against billing; the format requires one request per record. Source filenames are not stored: retain the trace to check references.
- **Not checked:** conversion of native Codex/Claude traces, outside usability and Windows. No evidence of VCR-specific token or performance gains.

## Options and decision

- Diagnosis without a trace: immediately usable without monitoring; does not measure actual usage.
- Explicit VCR format with optional fields: stable semantics and distinction between missing fields; other formats require manual conversion with importer error risk.
- Multi-provider native parser: more direct for some users; variable formats and interpretations, maintenance and private-data risks. Not selected until actual formats and permissions are investigated.
- Decision: voluntary, bounded and documented JSON; no telemetry or fixed pricing. Statuses are `measured` for declared values, `estimated` for derived calculations or declared estimated costs, and `unavailable` when not calculable.

## Update of 2026-11-14 — public sources authorized

- The former limitation that all provider formats require manual conversion is partially superseded: explicit imports of one OpenAI Responses API or Anthropic Messages API response are supported, without automatic access to accounts or private logs.
- [OpenAI — observability and usage](https://developers.openai.com/api/docs/guides/agents-api/observability): cache reads are included in input; reasoning in output; usage counters can be missing and are not equivalent to a bill.
- [Anthropic — prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching): ordinary input, cache-read and cache-creation counters are distinct; the total is calculated only when all three are available.
- **Confirmed on fixtures:** one-response import, missing partial fields, no fictional private content copied; see [tests](../tests/test_tokens_native.py). **Not checked:** native Codex/Claude Code session logs, conversion of multiple responses or a real production trace.
