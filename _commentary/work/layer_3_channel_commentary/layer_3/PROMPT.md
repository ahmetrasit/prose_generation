# Layer 3 Surah Channel Commentary and Layer 2.5 Integration

## 1. Task

Write Layer 3 and design its Layer 2.5 handoff in one pass.

The channel material in `reviewedChannels` has already been reviewed together
with its root and branch identities. Accept it as settled source evidence. Do
not admit, reject, rank, score, or review channels again.

You receive:

- a compact bundle of reviewed channels, Quran occurrences, Arabic text, a
  canonical primary translation floor, and primary-branch identities;
- the unchanged Layer-2 prose for every ayah, including its local surprise
  readings.

Produce a surprising whole-surah secondary reading from the reviewed recurring
channels. Then design additions that let the same image become visible gradually
through the existing ayah prose. Preserve the primary reading and all local
Layer-2 surprise turns.

## 2. Distinct Layers

Keep three functions separate:

- **Layer 2:** the focus ayah's primary reading and local surprise readings. It
  remains canonical and unchanged.
- **Layer 3:** the whole-surah argument plus recurring secondary images that
  make participating ayahs and the assembled surah newly legible.
- **Layer 2.5:** short story-building additions that disclose a Layer-3 image
  only as its members become available in reading order.

A local surprise is not automatically a surah channel. A surah channel recurs
through non-primary branch resonances and becomes a coherent secondary image,
like the traveler image gradually becoming visible across al-Fatihah.

## 3. Source Authority and Identity

`reviewedChannels` is authoritative input. Layer 3 may combine related reviewed
subchannels into the smallest coherent reader-facing image, but this is prose
composition, not a new review decision.

Every `active_motifs` citation joins through `motifAnchorMap` to
`anchorInventory`. A `resolved` occurrence may become a member.
`ambiguous-root` and `unmatched` mappings remain apparatus; never guess their
QAC occurrence or root ID.

Repeated Quran occurrences of one resolved root are recurrence evidence, not
ambiguity. Stable member identity is:

`qacMorphemeRef + rootId + branchId`

`primaryBranchMap` determines `primaryStatus` mechanically:

- cited branch in `primaryBranchIds`: `primary`;
- resolved same QAC occurrence and root, different branch: `non-primary`;
- no primary entry for that occurrence/root: `unknown`.

## 4. Surprising Reading

Do not produce a catalogue of events, roots, or channel labels. Make the
secondary reading happen in prose:

1. Establish the surah's primary-grounded argument.
2. Let recurring secondary details attach to one another.
3. Name the image or working system only when the accumulated evidence makes it
   recognizable.
4. Show precisely how it supports or shifts the primary reading without
   replacing it.

Use reviewed `synthesis`, `semantic_invariant`, and `surprising_reach` as
established meaning. Use Layer-2 prose as the reader's current ground. Do not
copy either source mechanically.

Related reviewed sources may form one image. Do not emit one prose section per
source channel. Conversely, do not combine sources merely to reduce their
number; the combination must increase explanatory force.

## 5. Maturity and Layer 2.5

Derive each rendered image's `maturityByAyah` from its resolved members:

- `latent`: only one member is available, or the relation cannot yet be stated;
  write no insertion;
- `emerging`: at least two encountered members form a statable relation; add a
  restrained hint;
- `mature`: the image's working shape is recognizable; state its local effect;
- `complete`: every member has appeared; add what the last member completes
  instead of retelling the image.

At each visible arrival:

1. Enter through a word already present in the ayah and ground already laid by
   its Layer-2 prose.
2. Recall only members encountered earlier.
3. Say only what has matured at this point.
4. Do not import the completed surah thesis prematurely.
5. Prefer one well-placed paragraph to several fragments.

Layer-2 files remain unchanged. Each insertion records the exact base prose
path and SHA-256, paragraph number, and optional phrase inside that paragraph.
`afterPhrase` is an integrity anchor; insertion still occurs after the selected
paragraph.

## 6. Integration Contract

Write `{S}.surah.channels.integrated.json` conforming to
`surah-channel-integration-v1`:

- `sourceLane: "combined-layer3-layer2.5"`;
- `sourceBundle` and `sourceBundleSha256` identify the exact compiled bundle;
- `maturityStatus: "derived"` because maturity is produced here, not reviewed
  upstream;
- `sourceChannels` names the reviewed `Pnn/key` or standalone `Pnn` sources
  composed into each reader-facing image;
- members use only `resolved` bundle mappings;
- maturity introduces members at their ayahs and never runs backward.

`sourceCoverage` accounts for every reviewed source exactly once. Use:

- `integrated` when the source contributes to one or more rendered images;
- `apparatus-only` when it remains valid reviewed evidence but cannot be
  rendered coherently in this prose pass. Give a concise reason.

`apparatus-only` is not rejection or downgrading.

Write `{S}.ayah-channel-overlays.json` conforming to the overlay schema. It must
hash-bind the integration plan and every base Layer-2 prose file. Every eligible
visible arrival is inserted or explicitly omitted with a reason.

## 7. Output

Write exactly seven authored artifacts:

1. `{S}.surah.prose.md` - continuous primary-grounded surah prose whose
   recurring secondary image produces a surprising reading shift;
2. `{S}.surah.thesis.md` - the primary-grounded thesis in one sentence;
3. `{S}.surah.channels.integrated.json` - composition and derived maturity of
   the already-reviewed channels;
4. `{S}.ayah-channel-overlays.json` - Layer-2.5 additions and placements;
5. `{S}.surah.exclusions.md` - Layer-2 readings not carried by the selected
   primary argument;
6. `{S}.surah.evidence.md` - phrase-to-source coverage with structural
   inferences marked;
7. `{S}.channel.friction.md` - input or instruction failures, never surah
   claims.

Do not author a merged preview. The workflow renders it deterministically from
validated overlay JSON and unchanged Layer-2 prose.

## 8. Failure Modes

- **Second review:** channel evidence is admitted, rejected, scored, or ranked.
- **Dry catalogue:** evidence or events are listed but no reading shifts.
- **Argument/channel conflation:** a secondary image replaces the primary
  thesis.
- **Premature disclosure:** the completed image appears before its members.
- **Layer-2 capture:** local prose is rewritten into pieces of the surah thesis.
- **Repeated definition:** every ayah restates the image from the beginning.
- **Identity guessing:** unresolved evidence becomes an exact member.
- **Apparatus leakage:** roots, IDs, stages, or schema terms enter reader prose.
