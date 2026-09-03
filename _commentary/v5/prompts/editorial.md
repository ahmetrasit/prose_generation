# Commentary v5 editorial handoff

Continue as the same live canonical writer for **@@AYAH_REF@@**. Revise the
four first-pass files under the editorial instructions embedded below and write
the four editorial outputs. Modify nothing else.

## Editorial Contract

- Improve cadence, continuity, clarity, proportion, and repetition while
  preserving every validated finding's claim, mechanism, changed reading,
  branch activation, concrete detail, context, payoff, and qualification.
- No scope sentence is verbatim-immutable. Rewrite any sentence that is
  awkward, repetitive, malformed, or not Turkish. Semantic discovery fields
  and provenance are authoritative; prior wording is not.
- Reader-facing prose must be Turkish. Translate English phrases and analytic
  terminology rather than copying them. Internal IDs, lane names, and QAC or
  analysis coordinates stay out of reader prose.
- Compatible findings may share a fluent passage, but none may become implicit
  or disappear. Preserve explicit carrier-trigger-contact-result-boundary
  explanations without turning the prose into a technical ledger.
- Preserve each exact compact single-line provenance-ledger JSON object from
  first-pass evidence exactly once in editorial evidence. Preserve only its
  exact provenance hash in the editorial findings-index row. Do not copy full
  packets, candidate audits, focus-surface JSON, semantic payloads, or the
  compact ledger into the findings index.
- Replace the first-pass landing map with exactly one final fenced
  `commentary-v5-landing-map` block at the end of the editorial findings index.
  Use schema `@@LANDING_MAP_SCHEMA_VERSION@@`, ayah `@@AYAH_REF@@`, phase
  `editorial`, and the same finding order. Rebuild each `semantic_landings`
  list against the editorial prose while preserving every semantic ref exactly
  once and in order. Source hashes remain workflow-bound and are not echoed.
  Related records may share a passage
  only when it expresses all of them. Evidence/index quotes must be unique and
  non-overlapping; the evidence quote contains the exact compact ledger, while
  the index quote contains the finding ref and provenance hash. Preserve
  `provenance_sha256`. Write no text after the block.

## First-Pass Inputs

- prose (`sha256:@@PROSE_INPUT_SHA256@@`): `@@PROSE_INPUT_PATH@@`
- evidence (`sha256:@@EVIDENCE_INPUT_SHA256@@`): `@@EVIDENCE_INPUT_PATH@@`
- findings index (`sha256:@@INDEX_INPUT_SHA256@@`): `@@INDEX_INPUT_PATH@@`
- friction (`sha256:@@FRICTION_INPUT_SHA256@@`): `@@FRICTION_INPUT_PATH@@`

## Editorial Outputs

- prose: `@@PROSE_OUTPUT_PATH@@`
- evidence: `@@EVIDENCE_OUTPUT_PATH@@`
- findings index: `@@INDEX_OUTPUT_PATH@@`
- friction: `@@FRICTION_OUTPUT_PATH@@`

<editorial_instructions>
@@EDITORIAL_INSTRUCTIONS@@
</editorial_instructions>
