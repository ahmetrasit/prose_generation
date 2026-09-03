# Commentary v4 editorial handoff

Continue as the same live canonical writer for **@@AYAH_REF@@**. Revise the
exact four first-pass files below under the unchanged editorial instructions
embedded verbatim in this handoff.

The explicit destination map below overrides the filename-location example in
the embedded instructions. Write exactly the four editorial files listed here
and modify nothing else.

## Semantic invariants

- Improve cadence, continuity, clarity, and repetition without deleting,
  combining, weakening, or genericizing any finding.
- Preserve every finding's top-level semantic `prose_statement` verbatim and
  exactly once. Its editorial landing-map `prose_quote` must equal that exact
  sentence, not merely point to nearby generic prose.
- Preserve every branch-activation sentence listed in the first-pass index's
  landing map verbatim and exactly once in editorial reader prose. Integrate
  these sentences fluently; they explain which carrier/root meaning meets which
  trigger and why the resulting reading becomes active.
- Keep internal root/branch IDs, finding IDs, evidence IDs, lane names, and
  QAC/analysis coordinates out of reader prose. They remain in the apparatus.
- Preserve each finding's context refs, evidence boundary, concrete semantic
  details, counter-readings, and epistemic qualification.
- Preserve each finding's exact single-line provenance-ledger JSON object from
  the first-pass evidence and index exactly once in each editorial apparatus
  file. Do not edit, reserialize, or duplicate it, and make each landing-map
  apparatus quote encompass the complete object.
- Replace the first-pass landing map with exactly one final fenced
  `commentary-v4-landing-map` JSON block at the end of the editorial findings
  index. Use schema `@@LANDING_MAP_SCHEMA_VERSION@@`, ayah `@@AYAH_REF@@`, and
  phase `editorial`. Keep the same finding order and exact activation quote
  arrays. Repeat each finding's exact semantic `prose_quote`; update its unique
  `evidence_quote` and `index_quote` to point to the editorial files. Evidence
  and index quotes must contain the exact finding ref and exact provenance
  ledger. Quotes for different findings may not overlap or contain one another.
  Write no text after the block.

## First-pass inputs

- prose (`sha256:@@PROSE_INPUT_SHA256@@`): `@@PROSE_INPUT_PATH@@`
- evidence (`sha256:@@EVIDENCE_INPUT_SHA256@@`): `@@EVIDENCE_INPUT_PATH@@`
- findings index (`sha256:@@INDEX_INPUT_SHA256@@`): `@@INDEX_INPUT_PATH@@`
- friction (`sha256:@@FRICTION_INPUT_SHA256@@`): `@@FRICTION_INPUT_PATH@@`

## Editorial outputs

- prose: `@@PROSE_OUTPUT_PATH@@`
- evidence: `@@EVIDENCE_OUTPUT_PATH@@`
- findings index: `@@INDEX_OUTPUT_PATH@@`
- friction: `@@FRICTION_OUTPUT_PATH@@`

## Unchanged editorial instructions - verbatim

<editorial_instructions>
@@EDITORIAL_INSTRUCTIONS@@
</editorial_instructions>
