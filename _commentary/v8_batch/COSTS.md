# V8 Batch cost projection

V8 changes only discovery from standard processing to OpenAI Batch. The saved
discovery prompt is unchanged, Luna remains at `max`, and composition plus all
later prose stages remain regular. OpenAI documents a 50% Batch discount and a
24-hour completion window. A Batch input file can contain up to 50,000 requests
and 200 MB, so the builder shards below that byte limit.

GPT-5.6 Luna standard text prices are $0.20/M input and $1.20/M output. For a
request above 272K input tokens, the whole request is billed at $0.40/M input
and $1.80/M output. Batch halves those rates. The collector uses each response's
actual token usage and applies that threshold per request; it also accounts for
reported cached-input tokens.

Official references:

- [OpenAI Batch API](https://developers.openai.com/api/reference/resources/batches)
- [OpenAI file upload limits](https://developers.openai.com/api/reference/typescript/resources/files/methods/create)
- [GPT-5.6 Luna model and pricing](https://developers.openai.com/api/docs/models/gpt-5.6-luna)

## S12 projection

This uses the previously measured S12 V5 token projection, including 12:0. The
displayed stage costs are rounded, so their sum can differ from the unrounded
grand total by one cent.

| Stage | Standard plan | V8 plan | V8 saving |
|---|---:|---:|---:|
| Discovery: 81.866M input, 7.411M output | $34.50 | $17.25 | $17.25 |
| Composition: 89.875M input, 3.709M output | $33.62 | $33.62 | $0.00 |
| Consolidation + editorial | $6.49 | $6.49 | $0.00 |
| Summary / invitation | $0.26 | $0.26 | $0.00 |
| Middle layer | $2.23 | $2.23 | $0.00 |
| **Whole workflow** | **$77.11** | **$59.86** | **$17.25 (22.4%)** |

Keeping composition regular leaves $16.81 of additional S12 Batch savings
unused. That is deliberate: composition is the second turn of discovery and
needs repository file writes plus its validator/repair loop. Batching it would
require a second asynchronous transport and would create a larger behavioral
change than the requested discovery-only plan.

## Whole-Quran extrapolation

The prior 6,236-ayah all-Luna estimate was $3,506.17. Its measured scope total
was $3,022.07, but discovery and composition were not separately regressed at
whole-Quran scale. Applying S12's measured 50.646% discovery share to that scope
cost gives this explicitly approximate comparison:

| Plan | Projected total | Saving vs standard |
|---|---:|---:|
| All regular | $3,506.17 | $0.00 |
| Discovery Batch; everything else regular | $2,740.89 | $765.28 (21.8%) |
| Discovery and composition both Batch | $1,995.14 | $1,511.03 (43.1%) |

The discovery-only plan therefore retains about $745.76 of projected
composition cost that a hypothetical two-stage Batch design could save. This is
an opportunity cost, not a regression against V5: compared with the all-regular
workflow, V8 still saves about $765.28.

S12's projected 81.866M discovery input tokens also require enough Luna Batch
queue capacity. The current published limits are 5M at Tier 1, 20M at Tier 2,
40M at Tier 3, 1B at Tier 4, and 15B at Tier 5. A one-wave S12 submission
therefore needs Tier 4 or higher. At a lower tier, prepare smaller named ayah
groups and submit the next group only after the prior group leaves the queue;
this changes transport scheduling, not prompt contents or the 50% token price.

## Non-dollar tradeoffs

- Discovery can take up to 24 hours rather than returning interactively.
- Batch does not retain the original live agent session for composition. V8
  uses the replacement-agent path already required by the unchanged discovery
  prompt and replays the exact prompt, frozen JSON, and exact composition prompt
  in order through a generated path-only handoff.
- There is no automated retry. Any failed or malformed response stops
  all-or-nothing collection before discovery files are written.
