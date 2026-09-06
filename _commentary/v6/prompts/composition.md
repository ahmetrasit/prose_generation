# Commentary v6 scope prose

Continue as the **@@LANE@@** scope agent for **@@AYAH_REF@@**. This is the
composition phase for your lane. Use your completed discovery work and the
discovery JSON at `@@DISCOVERY_OUTPUT_PATH@@` as the finding boundary. Do not
reopen evidence selection, add new findings, drop findings, or rewrite another
lane.

Write exactly one nonempty Turkish Markdown prose file and modify nothing else,
except for any required monitor lifecycle event command supplied by the
orchestrator:

- prose: `@@SCOPE_PROSE_OUTPUT_PATH@@`

Read the complete discovery through the supplied bounded reader, requesting
every page indicated by `page_count`:

```text
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ state --kind discovery --page N
python3 _commentary/v6/discovery.py --plan @@READING_PLAN_PATH@@ lookup --pointer /... --page N
```

Use `lookup` for any source recheck. Return each page intact, one per tool
response, with at least 32,000 output tokens on both command and outer wrapper
(`functions.exec`: `// @exec: {"max_output_tokens": 32000}`). Retry truncated
responses. After compaction, reload the relevant discovery and evidence pages.
Do not dump or project JSON files, write scripts that choose or generate
interpretations, or use other lanes or prior runs. Write your prose literally.

## Scope Prose Contract

- Write fluent Turkish scope prose, not JSON, a checklist, or a lane report.
- Every resonance must preserve the ordinary reading intact and keep it
  recoverable in the same explanation; a latent reading cannot replace it.
- Preserve every retained finding from your discovery work. Each finding's
  carrier, independent trigger, contact, changed reading, concrete semantic
  detail, and boundary must be visible to a reader.
- Recheck grammatical, morphological, and lexical wording against the
  finding's `evidence_facts` and exact branch-activation fields. Correct your
  own accidental classification errors before writing prose; preserve the
  supported finding, not an erroneous formulation of it.
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
- Preserve the attested lexical connection and form restrictions behind a
  same-root resonance, not only the resulting image.
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
landing from your discovery appears explicitly in the scope prose. If anything
is missing, revise the prose file before you report completion. Then run the
terminal monitor lifecycle command supplied by the orchestrator.
