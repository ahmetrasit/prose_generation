# Ayah Channel Integration Prompt - Layer 2.5

Read the inlined `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, and
`docs/CHANNELS.md` first. This file is the task.

## Task

Design the story-building channel additions that let a reader encounter an
accepted surah channel gradually while moving through the existing Layer-2 ayah
commentaries.

You receive:

- the original Layer-2 prose, evidence, and findings index for every ayah;
- the Layer-3 whole-surah prose;
- a reviewed channel plan whose `reviewState` is `reviewed`.

Produce:

- `{S}.ayah-channel-overlays.json`, conforming to
  `schemas/ayah-channel-overlays-v1.schema.json`;
- `{S}.ayah-channel-overlays.preview.md`, a non-canonical reading preview with
  insertions visibly delimited for review;
- `{S}.ayah-channel-overlays.friction.md`.

The original Layer-2 files remain canonical and unchanged. The JSON overlay is
the authored handoff. A renderer may merge it later.

## Preserve Layer 2

Layer 2 already contains the primary reading, grammar, word function, and local
surprise turns. Do not summarize it, correct it, suppress it, or bend it toward
the surah thesis. A channel addition has one job: connect an accepted recurring
system to the reader's current position.

Anchor every insertion to an exact base prose file and paragraph. Use
`afterPhrase` when a stable phrase gives a better join; otherwise use `null`.
The preview may show the merged sequence, but it must not be presented as a
replacement for the base files.

## Build the channel as a story

Follow the reviewed `maturityByAyah` path:

- write no insertion for `latent`;
- at `emerging`, connect the current word to previously encountered members in
  one restrained hint;
- at `mature`, let the system become recognizable and state the resulting local
  shift;
- at `complete`, add what the final member completes instead of retelling the
  channel from the beginning.

Enter through this ayah's own word. Recall only members already encountered.
Name the channel only when its reviewed disclosure makes the name earned.
Prefer one well-placed paragraph to several fragments.

The prose must make a secondary reading happen, not list evidence:

- do not enumerate roots or branch IDs;
- do not say "another channel is...";
- do not repeat the same channel definition at each ayah;
- do not dump every earlier member into every later insertion;
- do not import the whole-surah thesis into an ayah;
- do not add a channel merely because the reviewed plan contains it.

Each insertion records the exact member IDs it introduces and recalls, the
focus-ayah relation, and the shift it produces. Technical IDs stay in JSON, not
in `prose_tr`.

## Coverage

Every accepted channel must either appear in `insertedChannelIds` or have an
explicit omission for each eligible `emerging`, `mature`, or `complete` point.
Rejected and `revise` channels never enter the overlays. The validator checks
IDs, maturity, order, and coverage; the reviewer still judges whether the
prose builds recognition rather than a catalogue.
