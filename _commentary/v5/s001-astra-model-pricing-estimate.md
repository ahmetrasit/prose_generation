# S1 Model Pricing Estimate

Analysis ID: `s001-fresh-20260910`

This applies current base uncached text-token pricing to the same approximate
token estimates used in `s001-astra-token-usage-estimate.md`. The calculation is:

```text
(input tokens / 1,000,000 * input price) + (output tokens / 1,000,000 * output price)
```

Rates used, per OpenAI model documentation checked on 2026-09-11:

| Model | Input price / 1M tokens | Output price / 1M tokens |
|---|---:|---:|
| GPT-6 Astra | $10.00 | $50.00 |
| GPT-5.6 Sol | $4.00 | $20.00 |
| GPT-5.6 Luna | $0.20 | $1.20 |

This is a base estimate only. It does not include cached-input pricing, cache
writes, hidden system/tool overhead, or any long-prompt pricing multipliers that
may apply to individual requests.

| Ayah | Input k tok | Output k tok | Astra est. USD | Sol est. USD | Luna est. USD |
|---|---:|---:|---:|---:|---:|
| 1:1 | 1,544.6 | 297.7 | $30.33 | $12.13 | $0.67 |
| 1:2 | 1,947.8 | 372.5 | $38.10 | $15.24 | $0.84 |
| 1:3 | 1,366.2 | 261.6 | $26.74 | $10.70 | $0.59 |
| 1:4 | 2,155.4 | 465.9 | $44.85 | $17.94 | $0.99 |
| 1:5 | 1,947.9 | 381.0 | $38.53 | $15.41 | $0.85 |
| 1:6 | 2,127.7 | 457.1 | $44.13 | $17.65 | $0.97 |
| 1:7 | 2,315.9 | 519.1 | $49.11 | $19.65 | $1.09 |
| Grand | 13,405.6 | 2,754.8 | $271.80 | $108.72 | $5.99 |

Sources:

- https://developers.openai.com/api/docs/models/compare
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
