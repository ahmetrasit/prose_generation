# Empirical Resonance Contract

This contract describes the shape of a hermetic input packet and the required
output. Field names are provisional but should stay stable once scripts consume
them.

## Input Packet

```json
{
  "run_id": "empirical_resonance_s096_015_v1",
  "scope": {
    "mode": "ayah|window|pericope",
    "primary_refs": ["96:15"],
    "context_refs": ["96:13", "96:14", "96:16"]
  },
  "ayat": [
    {
      "ref": "96:15",
      "arabic": "...",
      "translation_tr": "...",
      "tokens": [
        {
          "token_ref": "96:15:3",
          "surface_ar": "...",
          "gloss_tr": "...",
          "root_id": "root_...",
          "branch_refs": ["root_...:B001"]
        }
      ]
    }
  ],
  "layer2": {
    "available": true,
    "prose_tr": "...",
    "evidence_tr": "...",
    "findings": []
  },
  "candidate_hooks": [
    {
      "hook_id": "h01",
      "ayah_ref": "96:15",
      "text_anchor": "forelock / forehead",
      "domain": "neuroscience",
      "why_candidate": "Concrete body-part mention connected to moral agency."
    }
  ],
  "research_sources": [
    {
      "source_id": "src01",
      "type": "review|meta_analysis|textbook|primary_study|official_report|classical_context|other",
      "title": "...",
      "authors": ["..."],
      "year": 2021,
      "venue": "...",
      "doi": "...",
      "url": "...",
      "abstract_or_note": "...",
      "relevant_claims": [
        {
          "claim_id": "src01_c01",
          "claim": "...",
          "population_or_scope": "...",
          "limitations": "..."
        }
      ]
    }
  ],
  "exclusions": [
    {
      "topic": "...",
      "reason": "No supplied source / too speculative / not anchored in the ayah."
    }
  ]
}
```

## Output Shape

The output is Markdown with these sections in this order:

```text
## Empirical Resonance

Reader-facing prose, without source-bracket clutter in every sentence. Use short
reference markers only where needed, such as [src01].

## Findings

| id | ayah hook | domain | strength | claim | sources | limits |
| --- | --- | --- | --- | --- | --- | --- |

## Source Gaps

Claims or hooks that look relevant but cannot be responsibly stated from the
provided packet.

## References

Full citations for every source ID used in the prose or findings table.
```

## Strength Labels

Use exactly one label per finding.

| label | meaning |
| --- | --- |
| `established` | Supported by broad expert consensus, convergent reviews, or textbook-level knowledge. |
| `well_supported` | Supported by multiple good sources, but with normal domain limits or live qualifications. |
| `plausible` | Coherent and sourced, but indirect, context-dependent, or based on a limited evidence base. |
| `contested` | Serious support exists, but interpretation or generalization is actively disputed. |
| `speculative` | Interesting but weak, indirect, or too preliminary for reader-facing prose; normally mention only in Source Gaps. |
| `unsupported` | Not usable from the supplied packet. |

Strength is not theological rank and not a claim that the ayah depends on the
empirical material. It is a reading aid.

## Finding Rules

Each finding must satisfy all of these:

- It is anchored in an explicit ayah word, phrase, legal instruction, social
  scene, body part, natural phenomenon, or repeated action.
- It uses supplied source material only.
- It says what the evidence can support and what it cannot support.
- It avoids proving-language: no "the ayah predicted", "science confirms", or
  "this is why Allah said".
- It remains reversible: if the empirical finding were later revised, the ayah
  commentary would still stand.

## Citation Rules

Use source IDs in prose and the findings table. A source ID must resolve to a
full entry in `research_sources` and must appear in the output `References`
section.

Prefer source types in this order when assigning strength:

1. systematic review, meta-analysis, consensus statement, textbook, or official
   statistics;
2. multiple independent primary studies with compatible results;
3. single primary study;
4. expert interpretation or historical-context note;
5. unsourced claim, which must not enter prose.

For social-science findings, name the population, period, and context whenever
the packet provides them. Do not universalize a result beyond the source's scope.

## Reference Format

References may use any consistent compact format, but each entry should preserve:

- source ID;
- authors or responsible institution;
- year;
- title;
- venue or publisher when available;
- DOI or URL when available.
