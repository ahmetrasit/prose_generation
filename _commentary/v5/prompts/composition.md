# Commentary v5 scope prose

Continue as the **@@LANE@@** scope agent for **@@AYAH_REF@@**. This is the
planned second turn for your lane. Use your first-turn discovery work and the
discovery JSON at `@@DISCOVERY_OUTPUT_PATH@@` as the finding boundary. Do not
reopen evidence selection, add new findings, drop findings, or rewrite another
lane.

Write exactly one nonempty Turkish Markdown prose file and one non-prose landing
ledger, then modify nothing else except for the validation and monitor lifecycle
commands supplied below:

- prose: `@@SCOPE_PROSE_OUTPUT_PATH@@`
- ledger: `@@SCOPE_LEDGER_OUTPUT_PATH@@`

## Scope Prose Contract

- Write fluent Turkish scope prose, not JSON, a checklist, or a lane report.
- Every resonance must preserve the ordinary reading intact and keep it
  recoverable in the same explanation; a latent reading cannot replace it.
- Preserve every retained finding from your discovery work. Each finding's
  carrier, independent trigger, contact, changed reading, concrete semantic
  detail, and boundary must be visible to a reader.
- Recheck grammatical, morphological, and lexical wording against the supplied
  lane evidence, exact QAC alignment, and discovery branch-activation fields
  already in this conversation. Correct accidental classification errors while
  preserving the supported finding.
- A single discovery finding may contain multiple distinct claims, images,
  branch activations, or interpretive movements. Treat each distinct movement as
  a mandatory prose landing.
- Explain activation in ordinary language: which Arabic surface, root meaning,
  or ordinary meaning is carried by the focus; what independent word, image, or
  context triggers it; why they make contact; how the focus reading changes; and
  where the inference stops.
- Preserve concrete details. Do not flatten a pathology, material image,
  repeated action, spatial relation, before/after shift, or secondary branch
  into a general theme.
- For each retained lexical resonance, explain its source in the same paragraph
  as the resulting image: name the Arabic word and its ordinary meaning,
  identify the supplied lexical use and any form restriction, and explain
  which separate contextual word or passage activates it here. Distinguish
  the lexical source from the contextual trigger. Consult the supplied lane
  evidence when discovery leaves this connection implicit. If the reader
  cannot tell where the image comes from and why it applies here, revise the
  paragraph. Mentioning the image alone does not preserve the finding.
- Use the project display tag syntax when an Arabic word, phrase, carrier, or
  anchor does interpretive work in a paragraph:
  `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`.
- Tags are paragraph-local. If the same Arabic item does interpretive work again
  in a later paragraph, repeat the full tag there. Do not add QAC IDs or invent
  another tag shape.
- Do not expose internal root IDs, branch IDs, candidate IDs, support IDs, QAC
  coordinates, or lane machinery in reader prose.
- Translate English source language naturally. Arabic and transliteration may
  remain in the established notation.
- Keep uncertainty, limits, and counter-readings attached to the interpretation
  they bound.

Before finishing, check that every retained finding and every distinct retained
landing from your discovery appears explicitly in the scope prose. Write the
landing ledger only after the prose is complete.

## Landing Ledger

The ledger is accountability metadata, not reader prose. Return exactly these
top-level fields in `@@SCOPE_LEDGER_OUTPUT_PATH@@`:

```json
{
  "schema_version": "commentary-v5-scope-landing-ledger-v1",
  "ayah_ref": "@@AYAH_REF@@",
  "lane": "@@LANE@@",
  "findings": [
    {
      "finding_ref": "exact discovery finding ref",
      "landings": [
        {
          "movement_refs": ["one or more required movement refs"],
          "paragraph": 1,
          "anchor": "short exact passage unique in that prose paragraph"
        }
      ]
    }
  ]
}
```

Return one ledger row for every discovery finding in exact order. Within each
finding, map these required movement refs exactly once and in this order:

1. `discovery:claim`, `discovery:mechanism`, `discovery:reader_payoff`, and
   `discovery:containment`;
2. each `semantic_obligation_ref` as `obligation:<exact ref>`;
3. each branch activation in discovery order as `activation:<zero-based index>`;
4. each `connection_ref` as `connection:<exact ref>`;
5. each `context_ref` as `context:<exact ref>`.

One substantive passage may carry several compatible movement refs; group those
refs in one landing. `paragraph` is the one-based position of the nonempty
Markdown block containing the passage. `anchor` must be a short exact passage
that occurs once in the complete prose and once in that paragraph. Keep internal
IDs in the ledger only.

Run this validator after writing both files:

```text
python3 _commentary/v5/validate_scope_ledger.py \
  --discovery @@DISCOVERY_OUTPUT_PATH@@ \
  --prose @@SCOPE_PROSE_OUTPUT_PATH@@ \
  --ledger @@SCOPE_LEDGER_OUTPUT_PATH@@
```

If validation fails, repair the prose or ledger and rerun it. Do not change the
discovery finding set. Finish only after validation reports `ok`, then run the
terminal monitor lifecycle command supplied by the orchestrator.
