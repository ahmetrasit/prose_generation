# Layer 3 Channel Workflow Status

Status as of 2026-08-19: **the Layer 3 workflow has been revised after the S1
v3 regression diagnosis. The implementation and structural tests are complete;
a fresh semantic S1 run has not yet been performed.**

## Revised Contract

- Layer 3 has one channel model and two reader surfaces:
  - a pre-surah prelude that plants concrete image expectations without
    explaining their payoff;
  - a post-surah postlude that reconnects the image system, its distributed
    members, and its surprising whole-surah yield.
- Discovery is channel-first and blind to Layer 2. A hypothesis must name a
  concrete image system, its boundary, at least two distributed signals, its
  proposed operation, and its expected reader shift.
- Discovery must account exactly for every Network activation card. It cannot
  satisfy the contract with an abstract theme that would survive deletion of
  the named images.
- Review tests secondary dependence and whole-surah yield. It preserves each
  admitted ayah's distinct contribution as a member landing and records the
  hinges that make those members operate together.
- Review may merge candidates only when they share both the same image system
  and the same reader payoff. Broad moral similarity is not a merge rule.
- Layer 2 prose is withheld from discovery and review. After review admits a
  channel, only the selected ayahs' editorial Layer 2 prose is projected into
  composition.
- Composition is a two-pass operation by the same agent:
  - `compose` produces an expansive draft;
  - `edit` removes repetition while preserving every channel, member, hinge,
    and distinct prelude/postlude function.
- Finalization accepts only an editorial composition and publishes separate
  prelude and postlude Markdown files plus their evidence and friction files.

## Active Artifacts

- `_surah_commentary/v2/schemas/discovery-hypotheses-v3.schema.json`
- `_surah_commentary/v2/schemas/channel-briefs-v3.schema.json`
- `_surah_commentary/v2/schemas/surah-composition-v2.schema.json`
- `_surah_commentary/v2/schemas/surah-reading-evidence-v2.schema.json`
- `_surah_commentary/v2/prompts/01-discover.md`
- `_surah_commentary/v2/prompts/02-review.md`
- `_surah_commentary/v2/prompts/03-compose.md`
- `_surah_commentary/v2/prompts/04-edit.md`

Older discovery, brief, composition, and publication schemas remain only for
archived run readability. They are not used by the active instantiator.

## Enforced Invariants

- Every selected Layer 2 artifact set is explicitly labeled `editorial`.
- Every discovery activation card is accounted for exactly once in the
  coverage ledger, with all hypothesis links declared.
- Every admitted channel has at least two member ayahs and every member is
  connected through a hinge.
- Every admitted local resonance retains its exact Layer 2 finding pair.
- Every prelude channel promise and every postlude channel, member, and hinge
  landing has a distinct prose span and evidence coverage.
- Prelude and postlude prose cannot be identical, contain workflow apparatus,
  or collapse to duplicated paragraphs.
- Finalization rejects draft-phase compositions.

## Validation Completed

- `python3 -B -m unittest tests.test_layer3_channel_workflow` passes 13 tests.
- All Layer 3 JSON schemas parse successfully.
- Scoped `git diff --check` passes for Layer 3 and its workflow tests.
- Prompt instantiation tests verify discovery blindness, selected editorial
  prose projection at compose time, same-agent edit input, and dual-surface
  publication hashes.
- A real S1 packet smoke build succeeded against the updated
  `editorial.tr` Layer 2 set with 33 registered sources. Grounded and inferred
  local resonances both survive the handoff; only the known partial V11 warning
  remains.
- A real S1 discovery prompt instantiated successfully from that packet and
  includes the concrete-image, image-deletion, and exact activation-card
  coverage requirements.
- The cold-agent runbook now requires an explicit primary-floor path, captures
  every emitted packet/prompt/output path, passes prior-stage artifacts
  explicitly, validates each semantic stage, and archives failed attempts
  before retrying.
- The composition validator CLI accepts `--phase draft` and
  `--phase editorial`, so orchestration can enforce the compose/edit boundary
  before advancing.

## Not Yet Completed

- No new semantic S1 discovery, review, compose, or edit pass has been run with
  the revised prompts.
- The current archived S1 v3 output remains diagnostic evidence of the old
  workflow; it has not been overwritten.
- The first revised S1 run still requires manual semantic review for image
  specificity, genuine multi-ayah interaction, anticipatory restraint in the
  prelude, and complete reinforcing payoff in the postlude.
