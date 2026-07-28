# Combined Surah Commentary and Channel Integration

## 1. Task

Write Layer 3 and design Layer 2.5 in one pass.

You receive:

- a lean bundle containing reviewed surah channels, exact Quran anchors, the
  Arabic text, and the canonical primary floor;
- the unchanged Layer-2 prose for every ayah, written in isolation.

Produce the whole-surah argument and surprising channel reading, then place
maturity-bounded channel additions into the existing ayah sequence. Do not
rewrite or flatten Layer 2. Its local surprise readings remain intact.

Use only the inlined task, governing excerpts, schemas, bundle, and Layer-2
prose. Paths are provenance and insertion identities, never permission to read
another file.

## 2. Authority and Identity

`reviewedChannels` is already reviewed with root and branch identities. Do not
send it through another admission pass and do not downgrade it to a list of
network nominations. Layer 3 may integrate related reviewed subchannels into the
smallest coherent reader-facing systems, but it may not silently discard their
evidence.

Each citation in `active_motifs`, such as `خ ل ق:B002/m01`, joins by exact
root/branch/motif keys to `motifAnchorMap`; its `anchorIds` then resolve to
`anchorInventory`. Never guess a QAC occurrence or root ID. An `ambiguous` or
`unmatched` mapping remains apparatus and cannot become an exact member.

`ambiguous` means one thing: the root string resolves to several
`candidateRootIds` and nothing chooses between them. A root appearing at several
morphemes is **not** ambiguous — those anchors are `exact` and carry
`recurrenceRefs`, which is the recurrence a channel is made of. Take every
occurrence as an anchor of one member rather than choosing among them.

`mNN` is review-local detail. Stable downstream member identity is:

`qacMorphemeRef + rootId + branchId`

## 3. Two Axes

Keep the surah argument and channels distinct.

- The **argument** says what the surah does as an assembly. It must survive with
  every secondary channel removed.
- A **channel** is a recurring secondary image or working system. It must change
  the reading of its participating ayahs and the whole surah in a way no local
  reading alone could produce.

For each channel state whether it `supports-primary` or `shifts-primary` at the
whole-surah level and at every disclosed focus ayah. The primary reading remains
recoverable in either relation.

Integrate rather than catalogue. Several subchannels or branches may be facets
of one system. The finding is the image that makes them explain one another.
Do not emit one prose section per upstream parent or subchannel.

## 4. Surprising Channel Prose

The channel prose must make a secondary reading happen. It should let a reviewed
image recolour, attach, or reorganize the primary reading while preserving it.
Do not list roots, branch IDs, channel names, or events as a substitute for that
shift.

Use the reviewed `synthesis`, `semantic_invariant`, and `surprising_reach` as
meaning already established upstream. Use Layer-2 prose to learn the reader's
current ground and the local surprise turns already spoken. Do not copy either
source mechanically.

The whole-surah prose should make the completed image feel like recognition
after the Layer-2.5 additions, not like a new apparatus-heavy reveal.

## 5. Maturity and Layer 2.5

Derive each accepted channel's `maturityByAyah` from its exact members in reading
order:

- `latent`: only one member is available; write no insertion;
- `emerging`: at least two encountered members have a statable relation; add one
  restrained hint;
- `mature`: the system's shape is recognizable; state the resulting local shift;
- `complete`: all accepted members have appeared; add what the last member
  completes instead of retelling the channel.

At every visible point:

1. Enter through a word already present in that ayah and through ground the base
   prose has laid.
2. Recall only members encountered earlier.
3. Say only what has matured at this point.
4. Do not import the surah thesis into the ayah.
5. Prefer one well-placed paragraph to several fragments.

An insertion is story-building prose, not an evidence dump. Technical identities
belong in JSON, never in `prose_tr`.

The original Layer-2 files remain canonical and unchanged. Every insertion names
its exact `baseProse`, paragraph, and optional stable phrase. The preview is a
review surface, not replacement prose.

## 6. Structured Plan

Write `{S}.surah.channels.reviewed.json` conforming to the channel-plan schema:

- `sourceLane: "combined"`;
- `reviewState: "reviewed"`;
- every rendered system has `reviewDecision: "accepted"` and
  `maturityStatus: "reviewed"`;
- `primaryFloorBasis` records the bundle's authored floor, or
  `writer-primary-inference` when only Arabic is available;
- members use only exact anchor mappings;
- source candidates preserve the upstream parent/subchannel keys;
- maturity introduces every member at its ayah and never runs backward.

`sourceCoverage` must account for every reviewed source key exactly once.
Subchannels use `Pnn/key`; standalone parents use `Pnn`. Mark each source
`integrated` with the reader-facing channel IDs that carry it, or
`apparatus-only` with a concise reason. Apparatus-only is a rendering decision,
not rejection of the reviewed source.

The top-level `review` records the upstream reviewed source named in bundle
coverage. It is provenance, not a new adjudication claim.

Write `{S}.ayah-channel-overlays.json` conforming to the overlay schema and
consistent with that reviewed plan. Every eligible visible arrival is either
inserted or explicitly omitted with a reason.

## 7. Output

Write exactly:

1. `{S}.surah.prose.md` - continuous reader prose containing the
   primary-grounded argument and the surprising completed channel reading;
2. `{S}.surah.thesis.md` - the primary-grounded thesis in one sentence;
3. `{S}.surah.channels.reviewed.json` - reviewed channel systems, exact members,
   effects, and maturity;
4. `{S}.ayah-channel-overlays.json` - Layer-2.5 additions and placements;
5. `{S}.ayah-channel-overlays.preview.md` - the ayah sequence with additions
   visibly delimited for human review;
6. `{S}.surah.exclusions.md` - Layer-2 readings the selected argument does not
   carry; channels are not exclusions merely because they are a separate axis;
7. `{S}.surah.evidence.md` - phrase-to-source mapping and coverage, with
   structural inferences marked;
8. `{S}.channel.friction.md` - instruction or evidence failures, never surah
   claims.

## 8. Failure Modes

- **Dry catalogue:** evidence or events are listed but no reading shifts.
- **Argument/channel conflation:** a secondary image becomes the primary thesis,
  or the thesis suppresses the channel.
- **Upstream re-adjudication:** reviewed material is needlessly accepted again.
- **Premature disclosure:** the completed image appears before its members.
- **Layer-2 capture:** local prose is rewritten into slices of the surah thesis.
- **Repeated definition:** every ayah restates the channel from the beginning.
- **Identity guessing:** an ambiguous or unmatched mapping becomes a member.
- **Apparatus leakage:** roots, IDs, stages, or schema language enter reader
  prose.
