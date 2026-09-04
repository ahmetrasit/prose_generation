# Commentary v5 editorial handoff

Continue as the same live consolidator for **29:38**. Revise the
first-pass prose under the editorial instructions below and write the editorial
prose output. Modify nothing else.

This V5 editorial handoff modifies prose only. Any historical instruction in
embedded governing documents to create evidence surfaces, indexes, friction
reports, ledgers, manifests, landing maps, hashes, or audit artifacts does not
apply to this handoff. You may run the mechanical validator command named below;
that command is a prose-file format check, not an audit artifact.

## Editorial Contract

The editorial version must preserve the complete semantic coverage of the raw
version while changing only wording, cadence, clarity, proportion, repetition,
and Turkish fluency.

- Preserve every retained finding's carrier, independent trigger, contact,
  changed reading, concrete semantic detail, and boundary.
- Preserve useful section subtitles, or add short Turkish section subtitles
  when they make the editorial prose easier to follow. Subtitles are reader
  prose, not wrappers; do not use generic labels such as `# PROSE`,
  `=== PROSE ===`, or XML-style prose wrappers.
- Preserve concrete images and secondary branches. Do not flatten a pathology,
  material image, repeated action, spatial relation, or before/after shift into
  a general theme.
- Keep each boundary attached to the interpretation it limits. A warning
  against literal translation does not authorize deleting the contextual
  resonance being bounded.
- No first-pass sentence is verbatim-immutable. Rewrite awkward, repetitive,
  malformed, or English-leaking sentences freely, but keep the underlying
  finding coverage.
- Preserve the project display tag syntax at Arabic anchor points:
  `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`. Tags are
  paragraph-local. A tag in an earlier paragraph does not cover a later
  paragraph. Repeated tags are required when the same Arabic item does
  interpretive work again in a new paragraph, because downstream TTS and reader
  masking depend on paragraph-local tags. Do not remove, deduplicate, reduce, or
  merge tags; do not convert tagged anchors to plain Arabic/transliteration, add
  QAC IDs, or invent another tag shape.
- Reader-facing prose must be Turkish. Translate English phrases and analytic
  terminology rather than copying them. Internal IDs, lane names, and QAC or
  analysis coordinates stay out of reader prose.
- Compatible findings may share a fluent passage, but none may become implicit
  or disappear.
- A single raw paragraph may contain multiple retained findings or branches.
  Treat each distinct claim, image, branch activation, or interpretive movement
  as a separate mandatory landing. Each one must remain explicit in editorial
  prose.

Before finishing, compare the editorial prose against the raw prose and confirm
that every raw finding and every distinct retained landing still appears once
as an explicit substantive landing. Also confirm that every paragraph-local
Arabic anchor still uses the project tag syntax. If any retained landing is
missing or any tag syntax is damaged, revise before you consider the unit
complete.

## First-Pass Inputs

- prose: `_commentary/v5/raw/s029-p03/s029/29_38/29_38.prose.tr.md`

## Editorial Outputs

- prose: `_commentary/v5/editorial/s029-p03/s029/29_38/29_38.prose.editorial.tr.md`

## Mechanical Validation

After writing the editorial prose file, run this validator on the editorial
prose file only:

```bash
python3 _commentary/v5/validate_prose.py _commentary/v5/editorial/s029-p03/s029/29_38/29_38.prose.editorial.tr.md
```

If the validator returns nonzero, repair only the reported mechanical
file-contract issues in the editorial prose file, then rerun the validator.
You may do at most two repair/rerun cycles. After two cycles, accept the
editorial prose as-is and report the remaining validator findings in this
conversation. Mechanical repairs include tag syntax, unsupported or duplicate
tag fields, unresolved placeholders, wrapper labels, empty/non-renderable prose
wrappers, malformed braces, and Arabic script outside valid paragraph-local
tags. The validator lists every detected issue, including every Arabic-outside
span, in compact line-oriented output. Do not use validator failures to add new
evidence, drop findings, reopen evidence selection, create ledgers, create
hashes, write a separate validation report, validate scope prose, validate
first-pass prose, or launch another agent.

<editorial_instructions>
No additional unit-specific instructions.
</editorial_instructions>
