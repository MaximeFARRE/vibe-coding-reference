# TOKENS trace format V1

The `vcr-token-trace-v1` format below is accepted by default. Two explicit imports of an individual API response are also available (see below); no Codex or Claude Code history is read automatically. The user voluntarily selects the file and must verify the meaning of its data before conversion. VCR accepts UTF-8 JSON files up to 4 MiB and 10,000 records; unknown VCR fields, invalid values, duplicate JSON keys and direct symbolic links are rejected.

Each `records` element represents **one distinct request**, not a cumulative counter or snapshot. Do not import the same request more than once. Fields are optional: absence means “unavailable”, never zero. Integers must be non-negative; booleans are not integers. Totals are calculated only when every record has the required field. Amounts are not quota or savings estimates.

```json
{
  "format": "vcr-token-trace-v1",
  "records": [
    {
      "input_tokens": 1000,
      "output_tokens": 200,
      "cache_read_tokens": 400,
      "cache_write_tokens": 50,
      "model": "modele-fictif",
      "session_id": "session-fictive",
      "tool": "outil-fictif",
      "command_chars": 1200,
      "search_fingerprint": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "topic_count": 2,
      "cost": {
        "amount": 0.001,
        "currency": "EUR",
        "kind": "actual",
        "provider": "source-fictive",
        "date": "2026-11-14"
      }
    }
  ]
}
```

The numbers and names above are **invented fixtures** describing the format; no pricing is provided or recommended.

| Field | Meaning declared by the importer |
|---|---|
| `input_tokens`, `output_tokens` | Request input and output counters. Output must already include any reasoning the provider counts there: VCR does not add it separately. |
| `cache_read_tokens` | Portion of `input_tokens` read from cache. If both fields are present, the first cannot exceed the second. |
| `cache_write_tokens` | Separately declared write counter; whether it is included in input depends on the source. VCR does not add it to input or output. |
| `model`, `session_id`, `tool` | Supplied identifiers, not copied to outputs. `tool` describes the tool associated with the record; one value per request. Without a complete tool inventory, low frequency does not demonstrate uselessness. |
| `command_chars` | Number of command characters, not the command itself. The 1,000-character display threshold is descriptive and does not prove waste. |
| `search_fingerprint` | SHA-256 fingerprint, 64 lowercase hexadecimal characters, already calculated by the importer, with no plain-text search. Comparisons also require `session_id`. Do not use confidential data to create a shareable fingerprint. |
| `topic_count` | Number of distinct topics declared for the session associated with this record. VCR does not infer topics from content. |
| `cost` | Complete object: numeric `amount`, three-letter uppercase `currency`, `kind` (`actual` or `estimated`), `provider` and ISO `YYYY-MM-DD` `date`. Nonduplicated per-request amounts, at most 18 decimal places. Provider and amounts are declarations: VCR does not verify billing. |

`measured` denotes a **declared** sum of counters or actual cost, not an independent measurement. `estimated` denotes a derived calculation (input + output or input − cache read) or a cost supplied as estimated. `unavailable` means a value is missing or units/cost types do not permit a reliable total. Currencies are never converted; if currencies or cost types differ, no total cost is calculated.

Summing inputs across requests can count reused context more than once: it is not the number of unique tokens. Total input + output must not be confused with cost. Cache reads and writes are presented separately; input excluding cache reads may include writes depending on the source. No subscription quota is inferred. No prices or percentage savings are calculated.

Free-text fields (`model`, `session_id`, `tool`, `provider`), fingerprints and raw contents are not copied into reports. `record_refs` references use positions **starting at 1** in `records`; outputs list at most ten references/groups and indicate partial coverage. The tool has no automatic collection, telemetry or external transmission. The user remains responsible for securing the imported file and reviewing outputs before sharing.

## Voluntary import of an individual API response

`--format openai-responses` accepts a JSON object containing the `usage` field of one OpenAI **Responses API** response. `input_tokens` includes cached input, including `input_tokens_details.cached_tokens`; output includes any reasoning tokens. VCR does not add them a second time. Missing or `null` values remain unavailable. References: [OpenAI — observability and usage](https://developers.openai.com/api/docs/guides/agents-api/observability) and [OpenAI — prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching).

`--format anthropic-messages` accepts a JSON object containing the `usage` field of one Anthropic **Messages API** response. Total input is calculated only if `input_tokens`, `cache_read_input_tokens` and `cache_creation_input_tokens` are all present: they are distinct according to [Anthropic — prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). If one is missing, the total is unavailable; observed cache remains separate. The sum is marked as calculated (`estimated`), and source counters as declared (`measured`).

```sh
python3 -m vcr tokens --format openai-responses --from "/chemin/reponse-openai.json"
python3 -m vcr tokens --format anthropic-messages --from "/chemin/reponse-anthropic.json"
```

The user must select **one response** from the specified API, not a session summary, list of responses or cumulative counter. A null `usage` remains unavailable. Response content and unnecessary fields are ignored and not copied; no API call is made. These formats are **not** native Codex or Claude Code session logs and do not establish their quota or subscription cost. No cost is inferred from these responses.
