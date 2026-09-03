# Commentary v4 canonical merge writer

You are the fresh canonical writer for **29:0**. Three independent
one-pass scope authors have already made the micro, macro, and global evidence
decisions and supplied prose-ready Turkish movements. Their validated
contributions and the focus-surface record are inlined below.

Your job is composition, not adjudication. Merge the supplied movements into a
single commentary with the established v2/v3 quality and then write the four
first-pass files. Do not reopen candidate decisions, inspect lane packets,
invent new findings, request repairs, or run a reconciliation stage.

## Merge contract

- Preserve every supplied finding exactly once in the prose and apparatus. A
  finding may share a prose movement only with findings that genuinely perform
  the same mechanism and reader payoff.
- Preserve each finding's carrier, mechanism, concrete image, containment,
  epistemic status, and reader payoff. Do not turn a specific discovery into a
  generic theme.
- Preserve exact macro and global `context_refs` in the evidence and findings
  index, and retain their concrete contextual movement in prose. Contextual
  pressure must never be rewritten as lexical meaning.
- Let micro, macro, and global material interact around the ayah's acts,
  relations, images, and tensions. Do not concatenate three lane reports and do
  not expose lane names, finding IDs, packet IDs, or analysis coordinates in
  reader prose.
- Keep countervailing findings without verdict or rank. Carry unresolved scope
  limitations into evidence and friction without fabricating a resolution.
- Use the focus-surface record only to preserve exact Arabic, transliteration,
  morphology, and analytic gloss boundaries. Render Arabic in the canonical
  single-span syntax with a natural Turkish gloss. QAC coordinates stay out of
  prose.
- The first pass should reveal before it compresses. Avoid catalogues, generic
  summaries, and commentary about the workflow itself.

## Output

Write exactly these four nonempty first-pass files and modify nothing else:

- prose: `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.prose.tr.md`
- evidence: `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.evidence.tr.md`
- findings index: `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.index.tr.md`
- friction: `_commentary/v4/raw/s029-basmala-full/s029/29_0/29_0.friction.tr.md`

The evidence file and findings index must make every supplied `finding_ref`
recoverable, including its cited evidence and context refs. After writing all
four files, remain in this same conversation for the unchanged editorial
follow-up.

The governing texts below are already inlined. Filenames and relative paths
inside them are in-document references, not permission to read other files.
This V4 handoff controls the evidence boundary, merge-only role, workflow stage,
and output destinations. Any older candidate-review, lane, reconciliation,
workflow, or file-writing instruction in the embedded texts is historical and
superseded by this merge contract.

## Governing principles - verbatim

<principles>
# Principles

Rules that govern every layer. Layer-specific rules live in
[`COMMENTARY_SPEC.md`](COMMENTARY_SPEC.md) and in each output family's own
directory; nothing there may contradict this file.

---

## 1. Evidence before prose

Every user-facing claim traces to typed evidence in the input bundle. Prose
renders accepted claims; it is not where claims first become true.

**A true claim from outside the bundle is still a violation.** If a reading needs
55:9, then 55:9 must be in the bundle. Correctness does not substitute for
provenance, because the reader's trust in the unusual claims depends entirely on
the ordinary ones being checkable.

## 2. Candidate systems nominate; review establishes

Semantic networks, embeddings, retrieval ranks, activation runs, and inter-ayah
similarity can nominate evidence. They do not independently establish a word
sense, an ayah relation, a channel, a theological claim, or publishable prose.

## 3. No disambiguation

The reader is never told which reading is correct, because the readings are not
in competition. This is the constraint the whole architecture is built to
satisfy, and it is expensive: it is why there are separate levels, why depth is
not confidence, and why nothing is ranked.

Classical exegesis buys depth by selecting — *the correct view is*. That trade is
refused here.

Two consequences:

- **Readings at the same depth coexist.** If two activated readings do not
  reconcile, both are said. Neither is adjudicated away.
- **Ranking is disambiguation under another name.** A ranked list has a winner,
  and a winner is a selection. Order for reading flow; never to imply truth.

The guarantee lives physically at ayah level, which does not select. See
`COMMENTARY_SPEC.md` §2.

## 4. Containment

Every latent reading must be expressible in a sentence that **contains the
primary reading intact**.

```
PASS   "By time — as the pressure through which what is latent becomes yield."
FAIL   "Not by time, but by pressing."
```

If a reading can only be written as *not X but Y*, it is a disambiguation claim
wearing different clothes; reject or downgrade it. This is checkable at review.

Containment must be achieved in the prose voice, not by a label. Do not write a
section headed "this does not replace the primary meaning." Write sentences that
add rather than substitute.

## 5. Grounding

Containment is a logical guarantee: the latent reading does not displace the
primary one. **Grounding is a reader-state guarantee**, and it is a separate
axis. A perfectly contained reading still unmoors a reader with no Arabic if it
arrives without preparation.

Three requirements:

1. **The way back is always open.** At any point the reader can recover the
   primary reading of what they are looking at. It is never left behind.
2. **New material arrives from ground already laid.** A resonance enters through
   a word the reader has already met, in a form they have already been given.
   Nothing is announced from above.
3. **Channel disclosure is paced by maturity, not by availability.** That a
   branch is present in the bundle is not a reason to announce the eventual
   surah-wide image. This does not suppress a locally grounded surprise reading:
   layer 2 still states what a secondary resonance does to the primary reading
   here. See [`docs/CHANNELS.md`](docs/CHANNELS.md).

The failure this prevents is real and was observed: prose that is entirely true,
fully traceable, and leaves the reader less certain of what the ayah says than
before they read it.

## 6. Exclusions are handed forward, never dropped

Each layer makes rejections. A rejection recorded nowhere is evidence destroyed.

| layer | selects | rejections go to |
| --- | --- | --- |
| 1 — spine | one branch per rooted stem | layers 2 and 3 |
| 3 — surah | one thesis | the exclusion artifact; Layer 2's full field already preserves them |
| reviewed channel source | recurring systems and members | compiled plan provenance |
| combined 3 + 2.5 | thesis and disclosure points, not local readings | exclusions and overlay omissions |
| 2 — ayah | nothing | — |

Layer 2 does not select, so it is the terminus: it is obliged to carry what the
others could not. It is not rerun with knowledge of the later thesis; that would
break the isolation Layer 3 depends on.

The concrete case: layer 1 selects `B003` (created beings, worlds) for
`عَٰلَمِينَ`; if `B002` (sign, landmark) is genuinely activated as the branch
the Fātiḥa path channel runs on, it belongs in `primary-anchors.json` as an
explicit root-scoped resonance. Branches that are merely inapplicable remain
implicit exclusions.

## 7. Preserve uncertainty and rejection

Rejected senses, weak alternatives, collisions, omissions, additions, and review
notes are part of the production record. They are not discarded because the
default reader surface is concise.

**Report gaps rather than filling them.** If a v12 run recorded no reader
responses, say so. Do not infer what it would have said. Every bundle carries a
coverage block naming what is present and what is missing, per source, per ayah.

## 8. Integration, not aggregation

Placing readings next to each other is not integration. Integration is letting
one reading **explain** another.

If N activated readings become N sections, the output has been reformatted, not
written. Multiple branches of one root are usually facets of a single concept.
Find the concept.

In S103, eight `ع ص ر` branches — press, rain-cloud, husk, choking throat,
withholding, refuge, yield — are one idea: *retention under compression*. That
collapse is what made `خسر` legible as leakage and made the surah's ending on
`صبر` structurally necessary rather than a pious sign-off.

The collapse is the finding. The list is not. Ask constantly: do these images
explain each other, or merely sit next to each other? If a paragraph could be
moved elsewhere without damage, it is sitting.

## 9. Retrieval labels order; they never filter

The inter-ayah `strong`/`medium`/`weak` axis measures a row's **marginal
contribution to the focus ayah**, not whether a connection is real.

Measured on S103: root-overlap is 55.6% for `strong` and 41.4% for `weak`, and
for focus 103:3 the order inverts. Weak-dense clusters carry *distributed*
findings — the S103 oath-genre cluster is 22 rows, 86% weak, zero strong, and no
single row states the finding.

Filtering at `strong` deletes such findings silently. Use the axis for ordering.
Never for inclusion.

`no value` is categorically different (10% root overlap; notes read "no clear
contribution"). Treat it as a retrieval artifact: retain, do not render.

**Counter-evidence is retained and rendered.** 45:24 for S103 is contrary
evidence for a temporal-agent reading and must survive into output at ayah level.

## 10. Analyze once, render per language

Arabic-side analysis is language-neutral wherever possible. What is shared:

- QAC morpheme, word, and ayah identities;
- root and branch identities;
- shared branch selection (`primary-anchors.json`) and its recorded resonances.

The shared selection may use an independently authored ordinary Turkish
baseline as non-authoritative assistance. Arabic morphology, context, and
branch boundaries remain controlling.

What each target language authors for itself:

- occurrence and card glosses;
- the fluent line;
- target-token-to-QAC-morpheme mapping;
- language policy.

A Turkish token mapping cannot be reused for English or German. A branch
selection can, and must be — if two languages disagree about which branch is
primary, one of them is wrong, and the shared file is what makes that
impossible.

## 11. Stable identities

- `ayahRef` — `S:A`
- `qacWordRef` — `S:A:W`
- `qacMorphemeRef` — `S:A:W:M`
- word analysis — `(releaseId, ayahRef, analysisIndex)`
- lexicon — `rootId`, and `branchId` scoped to its root

QAC words, QAC morphemes, and word-analysis records are different layers.
Similar-looking records must not be merged by position or surface form.
Cross-layer joins require explicit, versioned crosswalks. Branch IDs are
per-root, not global: `B002` means nothing without its root.

**One identity is in use upstream but not in this list.** The channel review
cites motifs as `root:branch/mNN` — e.g. `ع ب د:B005/m01`. That `mNN`
morpheme-sense level is finer than `branchId` and joins to nothing here. Until
it is either promoted with a crosswalk or dropped, channel members are recorded
at branch granularity and the `mNN` distinction is treated as prose, not as a
reference.

## 12. Prose and apparatus never mix

Two artifacts per output, always separate:

- **prose** — continuous, single voice, no provenance markers, no headers named
  after evidence layers;
- **evidence surface** — addressable per phrase, holding refs, branch IDs,
  counter-evidence, and coverage.

The prose must be readable end to end with the evidence surface closed. The
reader is never shown which layer a claim came from, how many readers converged,
confidence labels, ablation records, or row counts. That apparatus is how the
prose earned the right to speak. It is not what it says.

</principles>

## Commentary specification - verbatim

<commentary_spec>
# Commentary Specification

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Both consume
the same input bundle and obey the same evidence rules; they differ in what
question they answer and in whether they are allowed to select.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

The active Layer 3 production contract is
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md). The
former combined Layer 3 + 2.5 overlay workflow is retired.

Status: active draft, updated 2026-08-18. Layer 2 V4 and Layer 3 v3 workflow
contracts are implemented and locally validated; production Layer 3 semantic
passes have not yet been run.

---

## 1. What commentary is for

The reader understands the ayah better after reading the prose than before.
Nothing else is a success criterion.

The reader must never be shown which layer a claim came from, how many readers
converged, confidence labels, ablation records, row counts, branch identifiers,
or schema names. That apparatus belongs in the evidence surface
(`PRINCIPLES.md` §12).

The reader must also not be *destabilised*. A latent reading that is true,
contained, and fully traceable can still leave the reader less certain of what
the ayah says than before — that is a failure, and grounding
(`PRINCIPLES.md` §5) is what prevents it.

---

## 2. The two levels

|  | layer 3 — surah | layer 2 — ayah |
| --- | --- | --- |
| question | what is this surah's argument, and what runs through it? | what happens in this ayah, on its own? |
| selection | **must select what qualifies**; admitted channels coexist without ranking or disambiguation | **must not select**; carries the full local field |
| time | none; the whole is present at once | **has a before and an after** |
| pass condition | says something no ayah-by-ayah reading could produce | holds what the surah thesis had to drop |

These are not two sizes of one output. A surah reading that decomposes back into
its ayahs has failed. An ayah reading that is a slice of the surah thesis has
failed.

The split is also where no-disambiguation is structurally guaranteed. Layer 3
does make an admission decision: not every local resonance becomes a surah-wide
channel. But once channels are admitted, it does not choose one as the correct
reading, rank them, or collapse incompatible channels into a single winner. With
two levels, the primary-grounded surah argument can be stated, admitted channels
can coexist, and the full local field still survives at ayah level.

### 2.1 The surah argument rests on the primary reading

An argument that holds only under latent readings is not yet an argument. State
it from the primary reading first; latent readings then perturb, deepen, or
recolour it. If removing every latent reading collapses the thesis, the thesis is
not ready.

This does not demote channels — see `docs/CHANNELS.md` §4. The argument and the
channels are separate outputs on separate axes, and for some surahs (S100) the
channel is the more valuable finding.

### 2.2 Local surprise is not a surah-wide system

Layer 2 states the **local surprise reading** made visible by this ayah's own
words: the secondary resonance, what it does to the recoverable primary reading,
and what becomes newly legible. This requires no claim that the image recurs
elsewhere.

A **surah-wide system** is different. It says how recurring semantic operations
make several ayahs explain one another and change the reading of the assembly.
The isolated Layer-2 writer cannot know that. Layer 3 consumes the unchanged
Layer-2 v2 artifacts alongside the typed Layer-1 primary floor and available
network/V11 evidence. It reads the complete Layer-2 findings index, local
`surprise:<id>` resonance rows, and preserved boundaries. It hashes Layer-2
prose and friction for lineage, but does not use their prose as the primary
floor or as semantic input. It writes a separate surah reading and does not
rewrite or overlay the ayah prose.

Layer 2 may **not** carry the surah's architecture or name a recurring
surah-wide system. The distinction is testable: a local surprise is fully
anchored in this ayah; a Layer-3 system depends on explanatory recurrence across
multiple ayahs.

---

## 3. Depth model (build-time only)

Evidence enters at six depths. **Depths never appear in output.** They govern
what may be written and keep the primary reading structurally protected.

```
D0  what the grammar forces           QAC + attachments
D1  what the local form selects       word_analysis `used`      ← the primary reading
D2  what colors it                    word_analysis `narrowed`
D3  what activates under context      v12 models + trajectory
D4  what corroborates                 inter-ayah clusters
D5  apparatus                         variants, shawādhdh, sound
```

Depth is distance from the grammatical floor — not confidence, not rank. Ranking
readings forces a winner, which is disambiguation under another name
(`PRINCIPLES.md` §3). Two readings at the same depth coexist; nothing at D3 can
displace D1, because they are not on the same axis.

Depth does inform **grounding**: material further from the floor needs more
ground laid before it can be spoken.

---

## 4. Known failure modes

Observed during S103 development. Each produced output that was rejected.

| failure | symptom |
| --- | --- |
| aggregation-as-synthesis | clustering ayah readings, naming the cluster, calling it surah commentary |
| provenance-as-structure | sections titled by which layer they came from |
| list reformatting | N source readings become N prose sections in a different language |
| decorated primary | one latent branch used as seasoning; the rest of the latent field unused |
| latent-only thesis | a surah argument that collapses if the latent layer is removed |
| imported citation | a correct reference the writer knew but the bundle did not contain |
| sample-as-whole | reading one of eighteen word records, then writing as if from all |
| ungrounded reveal | a contained, traceable reading delivered before the reader had ground for it |

---

## 5. Output contract

Per ayah and per surah:

- **prose** — continuous, single voice, no provenance markers, no headers named
  after evidence layers, and no wrapper labels such as `=== THE PROSE ===` when
  the prose is written to its own file;
- **evidence surface** — separate, addressable per phrase, holding refs, branch
  IDs, counter-evidence, coverage, and an explicit mark on every claim that is
  inference rather than bundle-traceable;
- **findings index** — *ayah level only.* A flat list of every reading the prose
  carries, one line per reading, each under its bundle ref, with `[inference]`
  marking the writer's own readings. It compresses how each reading is said and
  never how many there are: every `must_integrate` topic appears exactly once,
  `ledger_only` topics are excluded, and no line may name a reading the prose does
  not carry. It is a table of contents for the field, not a summary. Layer 3 does
  not emit one — it selects, so its analogue is the exclusion list. Each
  coherent local surprise carried by the prose gets an additional
  `surprise:<id>` synthesis row marked `[supports-primary]` or
  `[shifts-primary]`; these rows expose how secondary readings relate to the
  primary instead of asking layer 3 to reconstruct that relation;
- **friction** — every point where the instructions were ambiguous,
  contradictory, unsatisfiable, or silent. Profile-specific style audits may be
  included here when a prompt profile asks for them, but they must be labelled as
  style audit rather than friction.

The prose must be readable end to end with the evidence surface closed.

Ayah prose makes its surprise turn explicit in reader language. It first gives a
recoverable primary floor, then enters through a local word, states the
secondary resonance, and makes clear what that resonance newly supports or
shifts. This is part of the continuous prose, not a section headed "surprise" and
not an apparatus label. When no secondary material survives grounding and
containment, the writer records that in evidence/friction rather than inventing
a turn.

Arabic lexical items in authored prose should use structured surface spans so one
text can render for both reading and listening editions:

```text
{ar:ٱلْقَلَمِ, tr:el-kalem, gloss:kalem}
```

Use the span at first mention of an ayah word, and again when the prose returns
to that word after moving to another word or another paragraph. A renderer may
collapse repeated fields later; the authored source should preserve `ar`, `tr`,
and `gloss` whenever the word is doing fresh interpretive work.

For reader display, render transliteration first, with Arabic in parentheses and
the gloss nearby. For TTS, render the Arabic surface form. For Turkish-only
display, render the gloss. Raw root skeletons, branch IDs, and letter-by-letter
root transliterations belong in the evidence surface, not in reader prose.

Prose should begin from reader meaning, then bring in grammar: say what the ayah
or the word does in plain target language, then name the construction that does
it, within the same sentence. It should not make the reader cross a technical
threshold before knowing what is happening.

Layer 3 emits:

- **discovery hypotheses** — blind cross-ayah possibilities opened from the
  typed primary floor and activation cards, not reader prose;
- **channel briefs** — reviewed operations, stable hinges, safe claim forms,
  prohibited rejected predications, and explicit before/after reader shifts;
- **composition envelope** — the publishable prose plus an evidence map proving
  that every admitted channel and hinge landed visibly, with complete evidence
  refs and distinct reader-visible spans;
- **surah reading** — continuous reader prose emitted by the deterministic
  finalizer, not a summary or ayah catalogue;
- **publication evidence** — separate mapping from prose spans to packet
  evidence;
- **friction** — missing evidence and production limitations.

Contracts and schemas are under `_channel/layer3/`.

---

## 6. Input bundle

Layer 2 uses one canonical bundle per Quran analysis unit. A unit is either a
numbered ayah or a prefatory basmala. `scripts/build_bundle.py` creates the full,
auditable source. Active V4 derives its focus docket and lane packets from that
source, while selected non-focus units receive the uniform lean projection
defined below. The retired direct prompt-instantiation path instead runs
`scripts/tier_branch_payloads.py` before `scripts/instantiate.py`; that tierer
may project only `root_lexicon` dictionary/gloss branch payloads and must
preserve every root target, branch identity, and non-branch field.

Branch payload tiers are transport projections, not finding ranks or prose
budgets. Layer 2 has no root, paragraph, or word-count quota. It must state every
materially distinct, anchored latent activation or surprise with a significant
reader payoff, including one supported by a compact branch; it must also avoid
repetition, filler, and available branches that do not change understanding.
The admission threshold is density-invariant: a finding receives the same test
in a three-root and a twenty-six-root ayah. Findings may share prose only when
their mechanism and payoff are the same and every admitted ref still has an
identifiable landing.

### 6.1 Unit identity and prefatory basmala

Every current bundle declares `unit_kind`, `surface_ref`, and
`linguistic_source_ref`. For a `numbered_ayah`, all identities resolve to the
numbered ayah itself. For `prefatory_basmala`, the surface is the target surah's
`S:0` Quran-text row and the linguistic source is canonical `1:1`. The builder
must prove normalized surface equivalence before aliasing. QAC, word-analysis,
and morpheme-span references remain `1:1:*`; it is forbidden to manufacture
`S:0:*` linguistic identities.

S1 has no separate `1:0` bundle because its basmala is numbered `1:1`. S9 has
no prefatory basmala. Every other surah emits `S:0` before numbered units. The
surah bundle keeps `ayah_refs` / `ayah_bundle_files` numbered-only and exposes
the complete ordered list separately as `bundle_unit_refs` /
`bundle_unit_files`.

The standalone prefatory unit bundle carries all intrinsic `1:1` semantic
evidence plus available target-surah reader walks, wide walks, cross-run
publication, whole-surah line, and channel material. That full depth is used
when `S:0` is the focus. Native HFT, inter-ayah completeness, and pericope
membership are `not_applicable`: those protocols are defined on numbered focus
ayahs. Existing numbered HFT source runs are not rewritten to claim that they
included zero; V4 adds `S:0` once to the macro packet at ordinary non-focus
context depth.

### 6.2 Explicit ordered context

Canonical unit bundles remain context-independent. V4 may prepare an analysis
composition containing one or more ordered, discontinuous, and cross-surah
segments, with one or more declared focus units. Each focus is authored one at
a time; every other selected unit becomes context. This supports, without
changing the canonical source bundles:

- a basmala focus with a selected surah as context;
- each numbered ayah as focus with its surah's basmala automatically present;
- each ayah of one surah as focus under an ordered Fatiha or other recitation
  lens;
- arbitrary explicit additions such as one external ayah outside a pericope.

For every numbered focus in S2-S8 and S10-S114, V4 automatically and mandatorily
adds the host surah's `S:0` bundle once to macro as first-class, ordinary
surah-preface context. An explicitly declared host `S:0` is normalized to the
same macro route and is not duplicated. S1 and S9 retain the exceptions above.
A dedicated basmala analysis instead makes `S:0` the host focus and selects its
complete numbered host surah as ordinary macro context.

External ayat use explicit context membership. Every ref must be enumerated;
comma-separated lists are allowed but ranges and whole-surah shortcuts are not.
These members retain their original Quran identities, enter macro once, and are
never focus-eligible. The declared host surah, not an external ayah's source
surah, determines the automatic prefatory basmala.

For ordinary ordered segments, selection order is evidence. Same-surah units in
the focus's own segment enter the macro packet; cross-segment or cross-surah
units enter the global packet; micro remains focus-local. Every selected context
unit, whether native, automatic basmala, or explicit external ayah, is projected
at HFT non-focus depth: one lean ayah record (`text_ar`, root sequence, and root
occurrences) plus compact `branch_image_ar` cues grouped under every mapped root
target. A context root already represented by the current focus inventory does
not duplicate that inventory.

The complete selected bundle remains the hash-bound provenance source but is
not embedded as model-visible context. Context projection must exclude the
unit's standalone-focus word commentary, full QAC rows, morpheme spans,
coverage report, full root dictionaries/glosses, prior HFT run, reader walks,
cross-run publication, inter-ayah rows, whole-surah reading, and channel
material. Those fields remain available only when that unit itself is the
focus. This boundary prevents automatic basmala and `--add-ayat` members from
becoming larger or semantically privileged relative to ordinary context ayat.

An analysis ID namespaces `input/`, `raw/`, and `editorial/` paths so native and
custom readings of the same focus cannot collide. The composition JSON, every
selected bundle hash, deterministic context-projection hash, projected lane
packets, and output identities are snapshotted in the unit manifest. Multiple
focus units may be prepared and orchestrated in parallel. V4 wraps the
established V2/V3 interpretive and prose standard in one-pass micro, macro, and
global contribution prompts; historical stage, role, and file-writing
instructions in those governing texts do not control V4. The canonical writer
merges the three completed contributions, and its same live session receives
the unchanged V3 editorial follow-up.

Layer 3 builds a separate hermetic source packet from Quran text, the typed
primary floor, the completed four-file Layer-2 v2 artifact set for every
numbered ayah, and whatever network-v3/V11 sources are available. Missing
optional source families are warnings, not build failures. Missing Quran text,
typed primary floor, or complete Layer-2 artifacts aborts. See
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).

</commentary_spec>

## Channel definitions - verbatim

<channel_definitions>
# Channels

A **channel** is a coherent secondary image or system that runs across a surah,
assembled substantially from branches the primary reading does not select.

Channels are the main vehicle for the surprise this project exists to deliver,
and they are also the main disorientation risk. This document defines what a
channel is, when it may be spoken, and how layers 2 and 3 divide the active
work. The old Layer 2.5 overlay lane is retained only as a historical
experiment.

Status: active specification, updated 2026-08-18. The Layer 3 v3 workflow is
implemented and locally validated; a production semantic surah run has not yet
been completed.

---

## 1. What a channel is

Ayah commentary also carries **local surprise readings**: secondary resonances
that shift or deepen one ayah without necessarily recurring across the surah.
They are valuable, and they are not channels merely because they are surprising.
The distinction is recurrence and system:

- a local surprise makes this ayah newly legible;
- a channel makes both participating ayahs and the assembled surah newly
  legible through one recurring image.

Channel membership requires:

1. **Lexical anchor.** Each member is a specific branch of a specific root at a
   specific `qacMorphemeRef`.
2. **Non-primary contribution.** The system depends substantially on branches
   layer 1 did not select. Primary members may support it, but a system made only
   from primary branches is a paraphrase of the translation.
3. **Cross-ayah recurrence.** The image has members in more than one ayah. One
   dense local synthesis remains an ayah reading.
4. **Coherence.** The members explain one another rather than merely sharing a
   topic. Rain, water collection, grass, a well, and a pulley form a working
   irrigation system. Five unrelated words that mention water form a topic.
5. **Explanatory yield.** The channel changes the reading of its focus ayahs and
   the whole surah: an unattached opening attaches, a flat sequence becomes one
   scene, or a closing turn becomes structurally necessary.

A coherent cluster without distinct yield is a **motif**. Motifs are recorded
and not rendered as channels.

Every accepted channel records how it relates to the primary reading at two
levels:

- **focus-ayah effect** — what the image makes newly visible in each member ayah;
- **whole-surah effect** — what changes in the assembled reading.

Both may be `supports-primary` or `shifts-primary`. These are relations, not
confidence grades. The primary remains recoverable in either case.

### The Fātiḥa water channel

Non-primary branches across the surah give rain, water collection, grass, a
well, and the crossbeam-and-pulley used to draw water. Together they are a
provisioning system, and `Rabb` — nurturer, sustainer — is the right name for
its agent because the surah has already named him that way. What the channel
yields: `الْعَالَمِينَ` stops being an abstract "worlds" and becomes the full extent
of what is provisioned; sustenance stops being asserted and becomes depicted.

### The Fātiḥa path channel

`na'budu` carries `mu'abbad` — a road that exists *because* it has been walked
over and over. `الْعَالَمِينَ` carries sign, landmark — waymarks. `صراط` carries a road
that does not merely run straight but takes its traveler into itself and moves
him along it. `أنعمت` carries the station where a traveler is received. `ضالين`
carries the ownerless animal that has strayed with no keeper, and being buried
and lost.

What the channel yields: the surah's second half stops being a sequence of
requests and becomes one picture — a traveler who can only move if helped, a
guide who goes ahead, signs made legible, a road made by a community's repeated
walking, and at the end the precise danger being prayed against.

### S100

Under the primary reading the running horses of the opening oath have nothing to
do with the rest of the surah. The channel is what attaches them — and because
the attachment is not visible without it, S100 is the case that makes layer 3
non-optional.

---

## 2. Maturity

A channel is not available for use the moment it is detectable. It has a
**maturity** at each point in the reading, determined by how much of it the
reader has actually been given.

| maturity | state | may be spoken |
| --- | --- | --- |
| `latent` | one member placed | no |
| `emerging` | two or more members placed and their relation is statable in one sentence | yes, as a *hint*, entered through this ayah's word |
| `mature` | enough members placed that the system's shape is visible | yes, as a *reading* |
| `complete` | all members placed | layer 3 |

Maturity is a property of a channel **at a position in the surah**, not of the
channel. The same channel is `latent` at 1:2 and `mature` at 1:7. It is computed
over the reading order, not over the evidence.

Two rules follow:

- **Availability is not permission.** That a branch is in the bundle at 1:1 does
  not license announcing the channel at 1:1. The evidence exists all at once;
  the reader does not.
- **Maturity never runs backwards.** A channel that reached `mature` at 1:6 is
  not re-hinted at 1:7. It is extended.

Maturity does not gate local surprise readings. Those arise from the ayah's own
evidence and remain part of layer 2 whether or not a surah channel exists.

---

## 3. Disclosure protocol

### Layer 2 (per ayah)

The isolated layer-2 writer produces local surprise readings and does not
discover or name a surah channel. In the active workflow, Layer 3 consumes those
local surprise rows later and writes a separate surah reading; it does not patch
channel disclosure back into the Layer-2 prose.

The following maturity protocol belongs to the retired Layer 2.5 overlay
experiment. Keep it as design history, not as active production instruction.

The overlay lane may mention a channel only at `emerging` or above, and then under three
constraints:

1. **Enter through this ayah's own word.** The channel is reached from a lexical
   item present here, never announced from outside. "Bu âyette yol imgesi
   sürüyor" is an announcement. "`na'budu`nun çağrıştırdığı `mu'abbad`…" is an
   entry.
2. **Say only what has matured.** Not the channel's eventual shape — its shape
   *as of here*. Withholding the rest is not a loss; it is the mechanism.
3. **Do not state the surah's thesis.** A channel increment is anchored in this
   ayah's lexis and bounded by maturity. A thesis is neither. Carrying an
   increment is permitted; carrying the thesis is the forbidden move
   (`COMMENTARY_SPEC.md` §2).

Worked example — the path channel across 1:6–1:7.

At 1:6, `emerging`. Two members are placed and their relation is one sentence:

> Yol imgesi, `na'budu` kelimesinin çağrıştırdığı `mu'abbad` — yani üzerinde
> tekrar tekrar yürüne yürüne meydana gelen yol — ile daha önce geçen yol
> işaretlerinin (`âlemîn`) birleşmesinden doğar: bir yol ve onun yolcusu
> görünür olur.

At 1:7, `mature`. `أنعمت` adds the station where the traveler is received, and
only now is the whole configuration sayable:

> `En'amte`, yolcunun vardığı ve karşılandığı konak anlamını da taşır. Böylece
> ancak yardımla yürüyebilen bir yolcuya yaratıcının önden giderek yol
> göstermesi (`mâlik`), yol işaretlerinin belirginliği (`âlemîn`), yolun bir
> topluluk tarafından yürüne yürüne açılması (`na'budu`) ve yolun yalnızca
> dosdoğru değil, yolcusunu içine alıp ilerleten bir yol oluşu (`sırât`) tek bir
> görüntüde toplanır. `Dâllîn` ise sahibi olmayan, yolunu kaybetmiş hayvan ve
> toprağa gömülüp kaybolma imgeleriyle yolcunun en büyük tehlikesini öne çıkarır
> ve duayı, neyden korunmak istendiğiyle tamamlar.

Note what the 1:7 passage does *not* do: it does not state a thesis about the
Fātiḥa, and every element it names is a word the reader has already met.

### 3.1 Active production

Layer 2 remains cold and states local surprise readings. Layer 3 v3 consumes the
unchanged Layer-2 v2 artifact set, especially the findings index and
`surprise:<id>` local resonance rows, alongside the typed primary floor and
available network/V11 evidence.

Layer 3 then performs three separate semantic passes:

- blind discovery of possible cross-ayah recognitions;
- review into channel briefs, with stable hinges, claim policies, and complete
  accounting for every discovery hypothesis and local resonance;
- composition into a prose envelope whose evidence map proves that every
  admitted channel and hinge landed in reader-visible language.

This is not disambiguation. Review decides whether something qualifies as a
surah-wide channel, but admitted channels are not ranked and incompatible
channels may coexist.

| | layer 2 | layer 3 v3 |
| --- | --- | --- |
| states local surprise readings | yes | consumes them as local resonances |
| establishes cross-ayah systems | no | yes |
| uses Layer-2 prose as semantic input | no | no; prose is hashed for lineage |
| writes the completed channel reading | no | yes |
| writes ayah overlays | no | no |

### Layer 3 (per surah)

Receives channels at the surah level. States the whole: the operations they
form, their relation to the primary-grounded surah argument, and how each
admitted hinge changes the reader's understanding.

Layer 3 v3 writes the complete channel reading and a publication evidence map.
It does not rewrite Layer 2 and does not add Layer-2.5 increments. The evidence
map checks that every admitted channel and hinge appears in the prose exactly
enough to be visible to a regular reader.

---

## 4. Channels and the argument are different outputs

A channel is the secondary image running through a surah. The argument is what
the surah does as an assembly. **Both are real and they are different axes.**
Neither may stand in for the other.

The argument must rest on the primary reading: state it such that it holds with
every latent reading removed, then let channels deepen and recolour it. If
deleting the channels collapses the thesis, the thesis is not ready. This rule
exists because it was violated — a first S103 attempt built the surah level
entirely out of latent readings and explained nothing to a reader who already
knew the surah.

The inverse error is to let the argument suppress the channel. For S100 the
channel *is* the finding; a surah reading that reports only the argument has
withheld the thing worth knowing.

Layer 3 therefore emits both, distinctly. See
`_channel/layer3/ORCHESTRATION.md`.

---

## 5. What exists upstream

Channels are **not** discovered in this repository. `latent_activation/network/v3`
does it deterministically — a branch-level top-k graph mined from the surah-local
SLM affinity matrix, with Qnet labels attached only *after* clustering, so the
candidates are discovery rather than classification. Generation is complete:
89,199 dense candidates and 4.16M sparse paths across 111 eligible surahs.

A blind review pass then turns candidates into readable channels, one markdown
report per surah, structured as parent channel → subchannel with `Semantic
invariant`, `Surprising reach`, `Active motifs`, `Ayah anchors`, and `Synthesis`.
110 surahs have one; S108, S110, S113, S114 do not.

**The quality is there.** Both reference channels in §1 were recovered by this
pipeline for S1, at finer resolution than the hand sketch:

> **Habitation, Water, and the Living Landscape** → *Water-Secured Encampment and
> Livelihood*: abundant fresh water `ر ب ب:B013`, water-rich well `ع ل م:B005`,
> water that secures command of camp `م ل ك:B007`, irrigation of land and people
> `غ ي ر:B001/m02` → *Sky, Rain, Wind, and Enduring Growth*

> **Movement/course** → landmark and boundary `ع ل م:B002/m02`, middle of the road
> or valley `م ل ك:B006/m01`, **paved or trodden road `ع ب د:B005/m01`**, leading
> animal followed by the group `م ل ك:B008` → swallowing `ص ر ط:B002`, burial
> `ض ل ل:B002` → *Disorientation, Forgetting, and the Stray*

The only member of the water channel not found anywhere in the corpus is the
pulley/crossbeam; `غ ي ر:B001/m02` "irrigation of land and people" is the nearest.

### 5.1 Reviewed source and compiled ledger

The channel reports are the reviewed source for parent/subchannel membership,
root/branch motifs, synthesis, and surprising reach. The commentary workflow
does not repeat that review.

They are prose artifacts rather than downstream ledgers, so the bundle compiler
adds the missing machine join:

- every `root:branch/mNN` citation is normalized;
- `motifAnchorMap` resolves it to typed Quran anchors;
- each anchor carries `qacMorphemeRef` and `rootId`;
- downstream stable membership drops review-local `mNN` and uses
  `qacMorphemeRef + rootId + branchId`.

Maturity is intentionally absent upstream because it is a reader-order property,
not a discovery or review property. The retired combined pass tried to derive it
while designing additions to Layer 2. The active Layer 3 v3 workflow does not
write those additions; it records channel hinges and reader-visible prose
landings instead.

## 6. Recording

Per surah, active Layer 3 v3 records:

- `discovery-hypotheses-v3` for blind concrete image-system candidates and exact
  activation-card coverage;
- `channel-briefs-v3` for admitted channels, member landings, hinges, claim
  policies, and non-channel dispositions, with exact accounting for every
  discovery hypothesis and local resonance;
- `surah-composition-v2` for draft/editorial prelude and postlude surfaces plus
  span-level evidence maps;
- `surah-reading-evidence-v2` for the finalized publication evidence.

The schemas live under `_channel/layer3/schemas/`. For active v3 runs use only
the schema versions listed here; older schema files are archival. The runbook is
`_channel/layer3/ORCHESTRATION.md`.

---

## 7. Open

- **Maturity remains archived.** The four-step scale and `emerging`-hint rule
  belong to the retired Layer 2.5 overlay experiment. They may be revisited
  later, but the active Layer 3 v3 workflow does not depend on them.
- **Motif identity now joins only through its stable portion.** The compiler
  resolves `root:branch/mNN` citations to typed Quran anchors. `mNN` remains
  review-local detail; downstream member identity is recorded at branch
  granularity as `qacMorphemeRef + rootId + branchId`.
- **The surah argument remains inference.** Reviewed channels establish the
  recurring secondary systems, but nothing upstream evidences what the surah
  does as a primary-grounded assembly.
- **Four surahs have no review**: S108, S110, S113, S114.
- **Cross-surah channels** are out of scope. Whether an image running across
  surahs is the same object as a channel is unresolved.
- Whether branches with lexicon `status='review'` (e.g. `ع ص ر` B016) may serve
  as channel members is unresolved; they are currently invisible to every
  consumer.

</channel_definitions>

## Canonical v2 authoring standard - verbatim

<canonical_prompt_v2>
# Ayah Commentary Prompt — layer 2 (v2)

Read `../../PRINCIPLES.md` and `../../COMMENTARY_SPEC.md` first. They govern.
This file is the task.

---

## Task

You are given the input bundle for one ayah. Write commentary that makes a
reader understand **this ayah, on its own terms**.

An ayah is a unit people meet alone. It gets memorised, quoted, written on a
wall, encountered without its neighbours. Your reader may have no intention of
reading the whole surah. Write for that person.

Your reader has almost no Arabic grammar and reaches Arabic words through Turkish
loanwords that have shifted, narrowed, or lost their meaning. Assume nothing is
obvious. Assume also that they are not fragile — they want the real thing, and
they want to keep their footing while getting it.

## The question you answer

**What happens here?**

Not "what does the surah argue" — that is layer 3's job, and if you answer it you
have written the wrong document. Concretely, ayah level covers:

- what this ayah *does* as an act: asserts, suspends, answers, excepts, swears;
- what its grammar forces before any lexical content is weighed;
- **what each word contributes to building the ayah**, including everything the
  reader's languages cannot render — Turkish has no definite article, English
  cannot double one, and `الصِّرَاطَ الْمُسْتَقِيمَ` has two. That doubling is invisible
  in every translation your reader will ever see, and it is doing work;
- what its form selects, and what that selection excludes;
- what its sound does, if the bundle records it;
- what genre or pattern the reader recognises before understanding it;
- what it holds that a whole-surah reading has no room for.

## Your reader does not know how Arabic words work

This is the single most important thing about your audience. Your reader does
not know that an Arabic surface word belongs to a family of related meanings,
some of which may become relevant when this ayah and its supplied evidence
activate them. The local form and context still establish the recoverable
primary reading. A translation usually renders that local sense, but it cannot
also show every grounded pressure that related meanings place on the ayah.

Do not teach the false rule that every dictionary meaning of a root is active at
once. Availability is not activation. Show only the meanings that the bundle
anchors here, while making clear how one word can legitimately carry more than
the translation had room to display.

**You must teach this as you go.** Not with terminology — not "polysemy," not
"branch," not "root field." Show the reader that this word carries more than
what the translation gave them. Show them what opens when that second meaning is
heard. Show them what changes in the ayah when two words' secondary meanings
meet.

If you mention a secondary reading without first making the reader understand
that the word has this capacity, the reading will feel like decorative ambiguity
— strange pressure with no payoff. The reader will think you are being poetic
rather than revealing something real.

A materially distinct activated reading may not be dropped because it is hard to
explain. Make it intelligible without displacing the primary reading. If the
available evidence does not let you do that, report the unresolved problem in
evidence and friction; do not silently omit the reading or decorate the prose
with an unexplained hint.

## Composition

Before writing, identify the ayah's **resonance set**: zero or more materially
distinct, locally grounded secondary images or shifts that emerge when one or
more of this ayah's words are heard with their activated meanings. Look for
nominations in `channel_subchannels_anchored_here`,
`v12_focus_trace_hermetic` (especially `context_deltas` and
`surprising_valid_outliers`), and `v12_reader_walks` (especially
`retrospective_surprises`). These sources may corroborate one another, but
source count is not rank and convergence does not choose a winner.

Carry every resonance that survives grounding, containment, and the reader-payoff
test. If two resonances support different pictures, both remain live. Do not
merge them merely to give the commentary one elegant center, and do not make the
most vivid resonance the ayah's hidden "real meaning."

Not every ayah has a resonance worth surfacing. Some ayahs' main contribution is
a grammatical force, a form selection, a sound pattern, or a single dense word.
When there is no coherent secondary image, the composition still works — the
word-built development becomes the center and the closing consolidates what the
ayah does. No resonance is not no depth. Do not force a surprise that is not
there, and do not shorten an ayah merely because it is not part of a channel.

The movements below are a planning model, not a fixed section template. Let the
ayah determine paragraph count and proportion.

### 1. Opening — what the ayah plainly says

Establish the ordinary scene and the reader's first footing. What does a
competent translation already give? Say it compactly. No technical apparatus
and normally no secondary meanings yet. This movement is grounding: when the
resonances arrive later, the reader can still recover what the ayah plainly
says.

### 2. Word-built development — complete in coverage, proportionate in development

Account for every surface word and meaningful morpheme, but do not give every
word equal architecture. Before drafting, silently map each word to one of three
reader-facing treatments:

- **develop it explicitly** when it has a distinct grammatical, lexical, formal,
  sound, or resonance payoff;
- **integrate it into another sentence or phrase movement** when its work is
  supportive rather than independent;
- **carry it transparently in the plain reading** when the bundle supplies no
  distinct payoff beyond what that reading already makes visible.

Every word is therefore accounted for. Not every word receives its own paragraph,
root excursion, or technical label. Prose space follows explanatory need, not
truth rank. A longer treatment does not make one word or reading more correct.
A significant finding receives enough space to make its mechanism and reader
payoff clear. Never compress such a finding into a passing clause merely to
shorten the commentary; compact treatment is for supportive work with no
independent payoff.

Sustained word development should do at least one of three things:

- **ground the primary reading** — make the reader feel the ayah's plain
  meaning more precisely than a translation could;
- **create tension** — show the reader that a word carries more than what they
  heard, that the translation chose one meaning and set others aside;
- **prepare one or more resonances** — lay the ground so each later surprise
  feels earned, not announced.

`must_integrate` topics from `word_analysis` must all appear in the commentary.
But appearing does not mean getting a dedicated paragraph — a `must_integrate`
topic can land in a sentence within a paragraph organized around something else.
What matters is that the reading is present and the `reader_payoff` is
delivered, not that each topic gets equal architectural weight.

When you introduce a word's secondary meaning, **first show the reader that
the word has this capacity**. Not "bu kelimenin bağlı olduğu alan da X'i
taşır" — that is analyst's shorthand the reader cannot use. Instead, begin with
the translated sense, show the related meaning that is actually activated here,
and explain the change it makes in this sentence. Show the word opening without
turning its entire dictionary family into the ayah's meaning.

### 3. Local resonances — what the words reveal together

This is the payoff. For each member of the resonance set, say what image,
operation, or shift emerges and what it changes. Every materially distinct
resonance gets an identifiable prose landing. Resonances may share a paragraph
only when they share the same mechanism and reader payoff.

Do not present this as a separate "channel section" or label it as a secondary
reading. It is part of the continuous prose. Enter through one of the ayah's own
words that the reader has already met in the development section. Show how this
word's activated meaning meets another word or reorients the ayah, and what
picture emerges here.

Then say what changed. What can the reader now see that a flat translation hid?
What does this ayah do that was invisible before?

If a resonance supports the primary reading, say so: the ayah's plain meaning
is not replaced but deepened. If it shifts it, say what shifts: the reader's
understanding of what the ayah is doing has changed direction.

These relations are not grades. A resonance that supports the primary and one
that shifts its frame can coexist. If two resonances cannot be reconciled, give
the reader both without a verdict.

**What you must not do:**

- Name the image as an established surah-wide system. Not "bu sûrede bir yol
  imgesi sürüyor." You are writing in isolation; you do not know whether this
  image recurs. Keep it local.
- Assert maturity or channel status. No maturity has been adjudicated.
- State the surah's thesis.
- Call one resonance the strongest, deepest, governing, central, or real one.

### 4. Closing — what the reader now sees

Consolidate what the ayah does — both its plain sense and everything the
word-built reading made newly visible. Return to the primary reading without
collapsing the resonance set into a verdict. The reader should finish knowing
what the ayah plainly says and all the distinct ways its grounded resonances now
remain live.

### When there is no resonance

Some ayahs will not have a coherent secondary image worth surfacing. The
channel material may be sparse, the HFT may show no grounded outliers, or the
secondary branches may not form a coherent picture.

In that case, skip movement 3. Give full attention to the ayah's act, grammar,
syntax, form selection, semantic precision, sound, genre, and relations among
its words. The commentary is still valuable: a strong primary reading with
precise, connected word analysis is better than a forced surprise. Record in the
evidence coverage and friction that no coherent secondary resonance survived
grounding and containment.

## What counts as an activated reading

The bundle's `word_analysis` topics carry `commentary_obligation`:

- **`must_integrate`** — obligatory. Every one appears in your commentary.
- **`candidate`** — review every one. Carry every candidate that is anchored,
  materially distinct, and has a significant reader payoff not already
  expressed. Omit only repetition, availability without changed understanding,
  or material that fails grounding and containment. Candidate status is not a
  rank and resonance fit is not an admission test. Record every omission and
  its reason in the evidence surface; conflict with another live reading is
  never a reason to omit.
- **`ledger_only`** — apparatus, not reader prose. Retain it in evidence when it
  explains a boundary or rejection; do not create a findings-index obligation
  from it.

Beyond `word_analysis`, these bundle fields carry activated readings:

- **`v12_reader_responses`** — retired strict staged focus responses, when
  present. They are the truer record of what appeared before and after context.
- **`v12_focus_trace_hermetic`** — a reconstructed, not strictly staged,
  before/after signal. Use `baseline_models`, `context_deltas`, and
  `surprising_valid_outliers`; never call them `stage_00` or `stage_01`.
  Outliers are not errors by default, especially when they preserve an anchored
  secondary split-root activation.
- **`v12_reader_walks`** and **`v12_reader_walks_wide`** — retrospective
  surprises are the highest-value material at this level. They are literally
  the shape of understanding arriving late.
- **`v12_cross_run_publication`** — compact coverage/priority check. Do not
  copy as prose; use as a coverage audit.
- **`channel_subchannels_anchored_here`** — first-pass, single-reader channel
  review material anchored at this ayah. It has no accept/reject decision, no
  second reader, and no maturity. It may nominate a local connection among this
  ayah's words; it does not establish a recurring channel. Mark a
  channel-informed synthesis as the writer's inference in the evidence surface.
- **`channel_generated_outputs`** — lists external quran-data files (candidate
  graphs, family inventories, path families). If your run gives file access,
  read only the exact listed files and only when channel detail is necessary.
  Do not browse the repository generally. If the files are not accessible or
  inlined, treat the manifest as awareness and do not invent their contents.
  These are candidate/family/path evidence, not an adjudicated channel ledger.
- **Branch inventories** — support explanations; they create no standalone
  prose obligation.

Branch availability, source repetition, and reader convergence do not by
themselves activate a prose reading. Activation requires an anchored mechanism
and a changed understanding for the reader.

## You must not select

This is the defining constraint of this level.

Layer 3 is allowed — required — to build a thesis, and a thesis excludes. You are
the opposite. **You carry the full field.** Every activated reading in the bundle
that survives review appears here, including ones no surah thesis could use.
Including ones that pull in different directions.

If two activated readings do not reconcile, say both. Do not adjudicate, do not
rank, do not pick. Readings at the same depth coexist.

Completeness governs findings; proportion governs exposition. You may give one
reading more sentences because it takes more work to explain, but never because
you have chosen it as more correct. Ordering is for reader comprehension, not
authority. The resonance set may contain several independent or countervailing
lines, and the prose must leave all of them recoverable.

This is where the no-disambiguation guarantee actually lives. If you select, the
guarantee is gone and nothing else in the system restores it.

## Integrate without collapsing

Your reader already has the catalogue. They cannot use it — assembling activated
readings into something that means anything is exactly the work that requires
the Arabic they do not have.

Connect readings that share a mechanism and reader payoff. Keep readings
separate when their mechanisms, payoffs, or directions differ. Do not force the
whole resonance set into one master image for elegance. One section per source
reading is aggregation; one winning synthesis that absorbs distinct live
readings is selection. Both fail.

## Keep the reader's feet on the ground

Grounding (`PRINCIPLES.md` §5) is a hard constraint here, not a matter of tone.

- The primary reading stays reachable at every point. The reader must never lose
  track of what the ayah plainly says.
- Every resonance enters through a word already in front of the reader, in a form
  they have already been given. Nothing is announced from above.
- Containment is at sentence level: `X — as Y`, never `not X but Y`.

An ungrounded reveal is a rejected output even when every claim in it is true and
traceable.

## Before and after

Ayah level has something surah level cannot have: **the ayah existed before its
neighbours did.**

If the bundle contains `v12_reader_responses`, use the staged responses for what
the ayah yielded in isolation and how that changed as context was revealed,
including any `changed_reading{before, after}` movement.

If the bundle contains `v12_focus_trace_hermetic`, use it as a reconstructed
replacement signal: `baseline_models` for what the ayah can yield alone,
`context_deltas` for what later context activates, sharpens, weakens, or revises,
and `surprising_valid_outliers` for what remains anchored but unexpected. It is
not a strict staged reveal, so do not call it `stage_00` or `stage_01`.

When both source families exist, staged responses remain the truer reveal
record. Preserve any live tension between them in evidence rather than making
their agreement a confidence vote.

Render this as reading experience, not as measurement:

> Bu âyet tek başına gösterildiğinde … Sonra hüsran açıldı, sonra istisna — ve
> iki okuma da yerine oturdu.

Never as: *"three readers at exploratory confidence converged on two models."*

If the reader walks record *retrospective surprises* — readings that only became
visible after a later ayah — those are the highest-value material at this level.

**If both staged reader responses and Hermetic Focus Trace are absent, say so in
the evidence coverage and friction, never in reader prose.** Do not infer what
they would have contained.

## What earlier selection dropped

You are the terminus for every upstream exclusion actually supplied to this
ayah (`PRINCIPLES.md` §6).

- If the bundle contains Layer 1 `consideredNotPrimary` readings, carry every one
  that is activated and grounded here.
- Do not infer an exclusion artifact that is absent. Record the coverage gap.
- Do not look for later Layer 3 exclusions. Canonical Layer 2 is not rerun with
  knowledge of a later thesis.

They are not errors and not leftovers. They are readings that a selection had no
room for.

## Voice — say what the word does

Write in positive predication. State what a word does and let what it does not do
be inferred.

Containment (`PRINCIPLES.md` §4) is phrased as a prohibition, so it is tempting
to discharge it by narrating what is *not* happening. And the `reader_payoff`
fields in the bundle are themselves written as analyst's shorthand. Do not
inherit that register.

In Turkish, stacked `-maz / -mez / değildir / yoktur` constructions read as
hedging and break the flow. Turkish carries contrast through `zaten`, `hem… hem`,
`-ken`, `ayrıca`, and through simple juxtaposition.

| instead of | write |
| --- | --- |
| Bu âyet bir şey bildirmez, bir şey ister. | Bu âyet bir istektir. |
| Türkçede bunun karşılığı yoktur. | Türkçe burada tek bir "ilet" ile yetinir. |
| Âyet yolun düz olduğunu ileri sürmüyor; hangi yol olduğunu söylüyor. | Âyet hangi yol olduğunu söyler: o yol, o bilinen dosdoğru olan. |

Use an explicit negative only to correct a likely misconception, protect the
primary sense from replacement, or preserve live counter-evidence. If no
explicit negative is needed, say in the friction report that there was no live
misconception requiring one.

## Arabic word surfaces

Mark Arabic lexical items with a structured span when the Arabic word matters:

```text
{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar}
```

`ar` is the Arabic surface form for TTS, `tr` is the Turkish-readable
transliteration, `gloss` is the target-language meaning.

Use the span at first mention of an ayah word, and again when the prose returns
to that word after another word or another paragraph. Inside one short local
sequence, a Turkish label or transliteration is enough.

Do not display roots as spaced Arabic letters or letter-by-letter transliteration
in prose. Anchor root discussion to the surface word:
`{ar:ٱلْعَادِيَاتِ, tr:el-âdiyât, gloss:koşup atılanlar} kelimesinin bağlı
olduğu kök alanı...`, not `ʿ-d-w kökü...`. Raw roots, branch IDs, and root
skeletons belong in the evidence surface.

## Structure notes

Section headers named after evidence layers are forbidden. Let the ayah's shape
decide. A single-word ayah and a twelve-word ayah do not have the same shape.
The four composition movements are an internal drafting sequence, not four
mandatory prose headings or four fixed-size paragraphs.

Organize paragraphs around acts, relations, and reader payoffs rather than
around a serial list of words. A phrase may carry several words together, but a
word with distinct work must still have an identifiable landing. Likewise,
several resonances may form one movement without becoming one adjudicated
reading.

Do not open a paragraph with "isim cümlesi", "edat", "tamlama başı", "yalın
hâl", or similar technical scaffolding unless the same sentence has already
given the reader a concrete meaning to hold. Prefer: "Âyet önce hamdi Allah'a
verir; bunu fiille değil, sabit bir ad cümlesiyle yapar."

**There is no length limit.** Write what the ayah's own work takes. Length is a
consequence, never a target, and it is never a reason to leave something out —
carrying the full field outranks brevity at this level.

Absence goes in the coverage note, never in the prose. If a source is missing,
the reader does not learn that; the reviewer does.

## Failure modes

- **Slicing the surah thesis.** If your ayah commentary reads as one third of the
  surah reading, you have produced nothing new.
- **Selecting.** Choosing the most interesting activated reading and dropping the
  rest. This is the one unrecoverable error.
- **Cataloguing.** Correct, complete, unconnected. The reader is exactly where
  they started.
- **Ungrounded reveal.** True, contained, traceable, and delivered before the
  reader had ground for it.
- **Reporting the measurement.** Reader ids, stage numbers, confidence words,
  convergence counts. Render the experience; suppress the instrument.
- **Skipping an available walk.** Reader walks are where much of the latent
  material actually is. When present, review them; when absent, record the gap
  rather than inventing their contribution.
- **Burying the surprise in word analysis.** A channel-informed nomination or
  HFT outlier identifies a coherent secondary image. The prose spends twelve
  paragraphs on word-by-word grammar, then mentions the image in passing. The
  finding was present but not organized around.
- **Decorative ambiguity.** A secondary branch is mentioned in passing — the
  reader does not know why it matters, does not know the word carries multiple
  meaning families, and cannot tell whether the author is revealing something
  real or being poetic. Strange pressure with no payoff. This is a failure of
  pedagogy, not of content.
- **Resonance monopoly.** One vivid resonance becomes the organizing truth and
  absorbs or displaces other grounded lines. A memorable reading is still a
  selection if competing live readings disappear.
- **Equal-paragraph completeness.** Every word receives the same amount of prose
  merely to prove coverage. Coverage is complete; development is proportionate.
- **Thin no-resonance commentary.** No channel-like image appears, so grammar,
  form, sound, and word relations are rushed. Absence of resonance changes the
  center of depth, not the required depth.
- **Lexical overactivation.** Every available dictionary branch is presented as
  live. The bundle must activate a meaning; root membership alone does not.

## Pass condition

Someone who already knows this ayah well reads your text and learns something
they could not have got from a translation plus a dictionary — the thing they
learn does not depend on having read the rest of the surah — and at no point are
they unsure what the ayah says.

A secondary condition: a reader who does *not* know this ayah well finishes the
text understanding both what the ayah plainly says and why certain words carry
more than the translation showed. They should not feel confused by unexplained
secondary meanings or wonder why the author mentioned something strange.

The output also passes only if every surface word is accounted for, every
required or admitted finding has a prose landing, and every materially distinct
grounded resonance remains recoverable without being ranked or collapsed into a
winner.

## Output

Produce four separate artifacts:

1. **Prose** — continuous prose in the target language, single voice, no
   provenance markers, evidence-layer headings, or wrapper label when written to
   its own file.
2. **Evidence surface** — addressable per prose phrase, mapping every claim to
   bundle refs, retaining counter-evidence, marking the writer's inference
   distinctly, and ending with a coverage note stating what was missing.
3. **Findings index** — one line per reading the prose carries, under its bundle
   ref, with `[inference]` on the writer's own readings. Every `must_integrate`
   topic appears exactly once, `ledger_only` topics are excluded, and no line
   names a reading absent from prose. Add one `surprise:<id>` synthesis row for
   every member of the resonance set, marked `[supports-primary]` or
   `[shifts-primary]`. These are relations, not ranks.
4. **Friction** — headed exactly `=== PROMPT FRICTION ===`, reporting ambiguity,
   contradiction, missing evidence, or invented rules. End with a `Density audit`
   recording counts for `must_integrate` topics, admitted candidates, distinct
   resonances, prose landings, and any shared landing with its justification.

Never interleave prose and apparatus. If an orchestrator requests separate
files, the paths supply the artifact names; do not add wrapper labels to prose
or evidence.

</canonical_prompt_v2>

## Focus-surface evidence

<focus_surface_json sha256="5dc21507b283022f04af7dbb4144cf9f72d928589464c014569cdecf9304eabc">
{"arabic_uthmani":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"1:1:1:1","qac_word_ref":"1:1:1","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"ٱسْم","morph_features":"STEM|POS:N|LEM:{som|ROOT:smw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"1:1:1:2","qac_word_ref":"1:1:1","root_ar":"س م و","surface_ar":"سْمِ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"1:1:2:1","qac_word_ref":"1:1:2","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:1:3:1","qac_word_ref":"1:1:3","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:1:3:2","qac_word_ref":"1:1:3","root_ar":"ر ح م","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:1:4:1","qac_word_ref":"1:1:4","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:1:4:2","qac_word_ref":"1:1:4","root_ar":"ر ح م","surface_ar":"رَّحِيمِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["1:1:1:1"],["1:1:1:2"],["1:1:2:1"],["1:1:3:1","1:1:3:2"],["1:1:4:1","1:1:4:2"]],"word_analysis_refs":["1:1:1","1:1:2","1:1:3","1:1:4","1:1:5"],"word_rows":[{"analysis_record_ref":"1:1:1","analytic_gloss_range_en":"bound opening preposition; locally governs the following name noun and leaves the governing act compressed","analytic_root_gloss_range_en":null,"qac_refs":["1:1:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"1:1:2","analytic_gloss_range_en":"name or designation in construct, governed by the opening preposition and bound to the divine proper name","analytic_root_gloss_range_en":"broad root field of rising, height, sky, raised designation, hunting, rivalry, and good repute; the local word selects name as raised designation","qac_refs":["1:1:1:2"],"root":{"arabic":"س م و","transliteration":"s-m-w"},"surface":{"arabic":"سْمِ","transliteration":"ismi"}},{"analysis_record_ref":"1:1:3","analytic_gloss_range_en":"definite divine proper name in genitive construct relation, anchoring the following mercy epithets","analytic_root_gloss_range_en":"deity and worship field, with reported longing or bewilderment pressure; local form is the proper name rather than an indefinite class term","qac_refs":["1:1:2:1"],"root":{"arabic":"أ ل ه","transliteration":"'-l-h"},"surface":{"arabic":"ٱللَّهِ","transliteration":"Allahi"}},{"analysis_record_ref":"1:1:4","analytic_gloss_range_en":"first definite mercy epithet in genitive apposition, expansive in force and attached to the divine proper name","analytic_root_gloss_range_en":"mercy and tenderness field with kinship and womb branches; local epithet selects mercy while allowing protective root imagery as pressure","qac_refs":["1:1:3:1","1:1:3:2"],"root":{"arabic":"ر ح م","transliteration":"r-h-m"},"surface":{"arabic":"ٱلرَّحْمَٰنِ","transliteration":"al-rahmani"}},{"analysis_record_ref":"1:1:5","analytic_gloss_range_en":"second definite mercy epithet in genitive apposition, landing the formula on durable enacted mercy","analytic_root_gloss_range_en":"mercy and tenderness field with kinship and womb branches; local epithet selects stable enacted mercy while retaining protective pressure","qac_refs":["1:1:4:1","1:1:4:2"],"root":{"arabic":"ر ح م","transliteration":"r-h-m"},"surface":{"arabic":"ٱلرَّحِيمِ","transliteration":"al-rahimi"}}]}
</focus_surface_json>

## Micro contribution

<micro_contribution_json>
{"ayah_ref":"29:0","candidate_decisions":[{"candidate_id":"cand_1c46d52273a24776b639","decision":"accept","finding_refs":["micro:opening-bound-act"],"reason":"sup_0269958b2367af9c5e43 ve sup_86c91a923c49bc88a942, بِ parçasını sonraki ada bağlanan formülün ilk vuruşu ve eylemi sıkıştıran yapı olarak birlikte temellendiriyor."},{"candidate_id":"cand_ba2e80731a21e085717f","decision":"narrow","finding_refs":["micro:opening-bound-act"],"reason":"sup_a9711d331c8ab9ebfd32 edatın araç, beraberlik ve içinden geçme duyumlarını destekliyor; sup_86c91a923c49bc88a942 yerel yönetimin bunları dört ayrı önerme değil tek bağlı yapı olarak tuttuğunu gösteriyor."},{"candidate_id":"cand_d9c0b1b4fdb4684a48d0","decision":"accept","finding_refs":["micro:opening-bound-act"],"reason":"sup_db7bbf7d31cf15bf9543, بِ'nin açıkça söylenmeyen başlama, okuma veya anma eylemini ada yönelterek formülü tamamlayan sıkıştırılmış çerçeve olduğunu doğrudan taşıyor."},{"candidate_id":"cand_3de911178ef87a39e8e3","decision":"narrow","finding_refs":["micro:name-as-mediated-designation"],"reason":"sup_46da0fbbee759728567b yükseltilmiş ya da işaretlenmiş belirginlik tonunu destekliyor; sup_0d8b07eb431a21708089 yerel biçimin etkin anlamını ad olarak tuttuğu için bu ton sınırlandırılarak taşındı."},{"candidate_id":"cand_39aa3d63b7af231e1d7f","decision":"accept","finding_refs":["micro:name-as-mediated-designation"],"reason":"sup_ba54357b33ac2f1cbc46 ve sup_0d8b07eb431a21708089, isim kelimesinin soldan بِ tarafından yönetilip sağdan Allah'ın özel adına tamlama ile bağlandığını açıkça gösteriyor."},{"candidate_id":"cand_a73536c6f1f30d661198","decision":"accept","finding_refs":["micro:name-as-mediated-designation"],"reason":"sup_4a6a06dc50a4443bda26, ismi açılış edatından Allah adına ve oradan merhamet sıfatlarına geçiren yapısal menteşe olarak temellendiriyor."},{"candidate_id":"cand_231d00f4806e5125e785","decision":"narrow","finding_refs":["micro:name-as-mediated-designation"],"reason":"sup_8e572e4e186ddeacaa5c, s-m-w anlam çevresindeki somut gök ve yükselme kullanımlarıyla soyut adlandırma arasındaki karşıtlığı veriyor; sup_0d8b07eb431a21708089 yalnız ad dalının yerel olarak seçildiğini koruyor."},{"candidate_id":"cand_cf4f3a926ca2139c97f4","decision":"narrow","finding_refs":["micro:name-as-mediated-designation"],"reason":"sup_3904c7864e7ec72fc6b8, alternatif kök yönlendirmesini yalnızca adlandırma anlamını keskinleştiren karşıtlık olarak sınırlıyor; sup_0d8b07eb431a21708089 yerel kök hizasını koruyor."},{"candidate_id":"cand_94927b25c0fed4865f58","decision":"accept","finding_refs":["micro:divine-name-anchor"],"reason":"sup_02991ac40aeaac854e72 ve sup_f7725957d9a8549cb393, iki merhamet sıfatının bağımsız bir niteliğe değil Allah'ın belirli adına bağlandığını ve zinciri oradan aldığını gösteriyor."},{"candidate_id":"cand_4b0304416b7855a41e73","decision":"accept","finding_refs":["micro:divine-name-anchor"],"reason":"sup_106108c5d58aa80ed91f, Allah adının tamlama içinde sesçe yoğunlaştığını ve ardından hamd ilişkisine dayanak olarak döndüğünü bildiriyor; bu ayrı ses ve bağlanma getirisi korunuyor."},{"candidate_id":"cand_fa521af54ad04516cae8","decision":"accept","finding_refs":["micro:divine-name-anchor"],"reason":"sup_9616286c79c43182bed8 ve sup_f7725957d9a8549cb393, Allah kelimesini genitif tamlamaya ulaşan belirli ve tekil özel ad olarak doğrudan destekliyor."},{"candidate_id":"cand_3a84a87d7339e33a9ee4","decision":"narrow","finding_refs":["micro:divine-name-worship-pressure"],"reason":"sup_ce242bd892b0c6e51152 tapınma ve özlem ya da hayranlık basıncını anlamlı bir karşıtlık olarak veriyor, fakat aynı kayıt Allah kelimesi için V4 satırı bulunmadığını ve yerel biçimin özel ad kaldığını belirtiyor."},{"candidate_id":"cand_3f864ad15356ff2ac1aa","decision":"narrow","finding_refs":["micro:variant-syntactic-pressure"],"reason":"sup_6ead5cbdfb87cc7d1f19 varyant irabların sıfat çiftini yüklem veya nesne gibi yeniden duyurabilecek canlı bir basınç taşıdığını söylüyor; aynı kayıt yerel genitif sıfat zincirini koruyor."},{"candidate_id":"cand_2189a4173d3d3e00fd4b","decision":"accept","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_1675ff53e3dda1fc6912 ve sup_4f18b826f6b812c5f5c8, ilk merhamet sıfatının belirli ve genitif bir niteleme olarak Allah adına bağlandığını doğrudan temellendiriyor."},{"candidate_id":"cand_846cad2f7d38c7dae4f1","decision":"accept","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_990bff7b47282b7f417a ve sup_4f18b826f6b812c5f5c8, ilk merhamet biçiminin genişletici niteliğini ve hemen ardından gelen aynı anlam ailesiyle farklandırıldığını destekliyor."},{"candidate_id":"cand_9685004bc52b37b5f3cb","decision":"accept","finding_refs":["micro:mercy-cadence-and-return"],"reason":"sup_5e4026cbb17c38d001fa, belirli takı, yinelenen başlangıç ve ritmin ilk merhamet sıfatını ikili sonun bağlı üyesi olarak işittirdiğini gösteriyor."},{"candidate_id":"cand_15645155a921e968fbc4","decision":"accept","finding_refs":["micro:mercy-cadence-and-return"],"reason":"sup_ba63014c1294abaed965, ilk merhamet çizgisinin 1:3'te yeniden duyulmasını ve 1:2'deki hamd ilişkisiyle ayrımını somut bir aynı-surah yankısı olarak veriyor."},{"candidate_id":"cand_0d92dd869e87a9099286","decision":"narrow","finding_refs":["micro:protective-mercy-pressure"],"reason":"sup_dbb3006e444c60b8325c merhamet ve döl yatağı dallarının birlikte koruyucu-kuşatıcı basınç verebildiğini, fakat yerel sıfatın merhamet anlamını seçtiğini belirtiyor."},{"candidate_id":"cand_2d0978cd3ad4a24e0f20","decision":"accept","finding_refs":["micro:mercy-cadence-and-return"],"reason":"sup_6ef75f06d3884729980a, kapanış kelimesinin ikili ritmi mühürlediğini ve aynı son çizgisinin 1:3'te döndüğünü açıkça taşıyor."},{"candidate_id":"cand_4d462bc2882a3f01451d","decision":"accept","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_a0459e602e39b3c6f314 ve sup_696cad80b84a282418b4, son kelimenin önceki sıfatı tamamlayıp aynı Allah adına bağlı zinciri kapattığını destekliyor."},{"candidate_id":"cand_505f30bd726b25681f68","decision":"accept","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_5a2186ca53d4a45fa108, aynı anlam ailesinin ikinci kez dönmesini biçim farkıyla daralan bir inceltme olarak kuruyor; tekrarın düz eşanlamlılık olmadığını gösteriyor."},{"candidate_id":"cand_69fbec494e02bcd3e720","decision":"narrow","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_59953667b2f192780589 son merhamet biçiminin insan hakkında gerçekleşen merhameti de niteleyebildiğini gösteriyor; sup_696cad80b84a282418b4 yerel genitif bağın onu burada Allah'a ait sıfat tuttuğunu sınırlandırıyor."},{"candidate_id":"cand_e74130c63d851de1a020","decision":"accept","finding_refs":["micro:paired-mercy-attributes"],"reason":"sup_5a43ccd2baac6c45ad04 ve sup_696cad80b84a282418b4, final sıfatın formülü dayanıklı ve gerçekleşen merhamet niteliğinde sonlandırdığını destekliyor."},{"candidate_id":"cand_d37a7bc52f828cc7df3e","decision":"narrow","finding_refs":["micro:variant-syntactic-pressure"],"reason":"sup_f5a6078ed810bdf095da, irab ve durak varyantlarının son sıfatı 1:2'ye geçiş eşiği gibi duyurabileceğini bildiriyor; yerel biçim yine genitif kapanış olduğundan yalnızca bu sentaktik ve tilavetsel basınç taşındı."},{"candidate_id":"cand_353c6d0b915f11c20788","decision":"reject","finding_refs":[],"reason":"sup_7522ff51600da0a209ed yalnızca س م و kökünün QAC yüzey koordinatını kaydeden ledger_only bir oluşumdur; bağımsız okuyucu anlamı sağlamaz ve adlandırma bulgusunun yerine geçmez."},{"candidate_id":"cand_59d76ebb0fb3cf746c5e","decision":"reject","finding_refs":[],"reason":"sup_701f6be1a818d6d1c994 yalnızca ء ل ه kökünün QAC morfem kaydıdır; ledger_only olduğu için özel ad ve tapınma basıncına ayrıca yeni bir okuyucu bulgusu eklemez."},{"candidate_id":"cand_2e4a10b0c79321d62da2","decision":"reject","finding_refs":[],"reason":"sup_3d9db17a6b2ee32b24cc yalnızca ر ح م kökünün QAC morfem kaydını verir; ledger_only kayıt olarak merhamet sıfatı bulgusuna ek, bağımsız bir anlam taşımaz."}],"coverage_complete":true,"findings":[{"branch_refs":[],"candidate_ids":["cand_1c46d52273a24776b639","cand_ba2e80731a21e085717f","cand_d9c0b1b4fdb4684a48d0"],"claim":"بِ, başlama, okuma veya anma eylemini kendinden sonraki ada bağlayan bağlı bir başlangıç hareketi kurar; eylem açıkça söylenmeden okuyanın edimi için yer bırakır.","connection_refs":[],"containment":"Birincil okuma 'Allah'ın adıyla' olarak korunur. Araç, beraberlik ve yöneliş duyumları birbirinin yerine geçen dört önerme değil, aynı bağlı yapının sınırlı tonlarıdır.","context_refs":[],"epistemic_status":"Yerel edat yönetimi ve tamlama yapısından doğrudan okunan, eylem elipsini sınırlı biçimde içeren bulgu.","finding_ref":"micro:opening-bound-act","mechanism":"Açılış edatı sonraki isim kelimesini yönetir ve formülün ilk vuruşu olarak duyulur. Edatın araç, beraberlik ve içinden geçme yönleri tek bir yönetilen tamlama içinde toplanır; ardından gelen eylem dilbilgisel olarak sıkıştırılmış kalır.","reader_payoff":"Okur, Türkçedeki tek bir 'adıyla' karşılığının arkasında bir hükümden önce kurulan ilişkiyi ve kendi başlama ya da okuma ediminin bu ilişkiye nasıl yerleştiğini fark eder.","support_ids":["sup_0269958b2367af9c5e43","sup_86c91a923c49bc88a942","sup_a9711d331c8ab9ebfd32","sup_db7bbf7d31cf15bf9543"],"title":"Bağlı başlangıç ve sıkıştırılmış eylem"},{"branch_refs":["root_000745/B004","root_000745/B005"],"candidate_ids":["cand_3de911178ef87a39e8e3","cand_39aa3d63b7af231e1d7f","cand_a73536c6f1f30d661198","cand_231d00f4806e5125e785","cand_cf4f3a926ca2139c97f4"],"claim":"سْمِ, soldan بِ tarafından yönetilen ve sağdan Allah'ın özel adına tamlama ile bağlanan bir adlandırmadır; bağlı olduğu anlam çevresindeki yükselme ve belirginleşme basıncı, adı anılanı öne çıkaran bir tona dönüştürür.","connection_refs":[],"containment":"Yerel anlam ad ve adlandırmadır. Gök, yükselme ve karşıt kök yönlendirmeleri yalnızca bu seçimi keskinleştiren sınır bilgisi olarak kalır; ayet somut gök, av, yarış veya başka bir kök anlamına çevrilmez.","context_refs":[],"epistemic_status":"Yerel tamlama ilişkisiyle sağlamlaşan ve yükselme-belirginlik tonunu sınırlı sözcük çağrışımı olarak taşıyan bulgu.","finding_ref":"micro:name-as-mediated-designation","mechanism":"İsim kelimesi ne bağımsız bir etiket olarak kalır ne de kök çevresindeki somut gök ve yükselme görüntülerine kayar. Yönetim ve tamlama ilişkisi onu açılış hareketinin aracısı yaparken, adlandırma dalı yükseltilmiş ya da işaretlenmiş belirginliği sınırlı bir renk olarak taşır.","reader_payoff":"Okur, 'ad' kelimesinin burada yalnızca bir isim bildirmediğini; başlangıç edimini belirli bir ada ulaştırıp o adı görünür ve ayırt edilir kılan bir iş yaptığını görür.","support_ids":["sup_0d8b07eb431a21708089","sup_46da0fbbee759728567b","sup_4a6a06dc50a4443bda26","sup_8e572e4e186ddeacaa5c","sup_ba54357b33ac2f1cbc46","sup_7522ff51600da0a209ed"],"title":"Adın aracılı ve belirginleştirici kuruluşu"},{"branch_refs":["root_000047/B002"],"candidate_ids":["cand_94927b25c0fed4865f58","cand_4b0304416b7855a41e73","cand_fa521af54ad04516cae8"],"claim":"ٱللَّهِ, isim tamlamasının genitif konumundaki belirli ve tekil özel ad olarak, ardından gelen iki merhamet sıfatını kendisine bağlar ve tamlamayı sesçe yoğun bir birlik halinde taşır.","connection_refs":[],"containment":"Allah kelimesi yerel olarak özel addır; ses yoğunluğu ve sonraki hamd ilişkisi bu adın bağımsız bir yüklem ya da genel tür adı olduğu anlamına gelmez.","context_refs":[],"epistemic_status":"Genitif özel ad yapısı, sıfat bağlanması ve supplied ses-yankı kanıtlarıyla desteklenen yerel bulgu.","finding_ref":"micro:divine-name-anchor","mechanism":"QAC biçimi ve yerel bağlanma, Allah adını soldaki isim tarafından ulaşılan referent, sağdaki sıfatların da onun genitif nitelemeleri olarak kurar. Aynı adın hamd ilişkisine doğru yeniden dayanak olması, bu yapısal bağın ses ve geçişte de sürmesini sağlar.","reader_payoff":"Merhamet artık Allah'ın adından kopuk iki özellik gibi görünmez; okur, adın açılıştaki yönelişi merhamet zincirine taşıyan merkezî bağ olduğunu işitir.","support_ids":["sup_02991ac40aeaac854e72","sup_106108c5d58aa80ed91f","sup_701f6be1a818d6d1c994","sup_9616286c79c43182bed8","sup_f7725957d9a8549cb393"],"title":"Özel adın merhamet zincirini taşıması"},{"branch_refs":["root_000047/B001","root_000047/B002"],"candidate_ids":["cand_3a84a87d7339e33a9ee4"],"claim":"Allah adının bağlı olduğu anlam çevresi, yerel özel ad okumasının içinde tapınmaya yöneliş ve hayranlık ya da özlem basıncını arka planda toplar.","connection_refs":[],"containment":"Paket bu kök için V4 satırı bulunmadığını bildirir; bu nedenle tapınma ve hayranlık/özlem basıncı etimolojik ve karşılaştırmalı bir renktir. Yerel okuma belirli özel ad olarak korunur, genel bir ilah türüne genişletilmez.","context_refs":[],"epistemic_status":"Kök anlam çevresinden gelen, V4 kapsamı sınırlı olduğu için özel ad biçimiyle çerçevelenmiş ikincil basınç.","finding_ref":"micro:divine-name-worship-pressure","mechanism":"ء ل ه alanındaki tapınma ve yöneliş anlamı, Allah adının belirli referentiyle birlikte okunduğunda 'Allah'ın adıyla' başlangıcına nötr bir etiketin ötesinde kulluk yönü verir. Yerel biçim bu basıncı özel adın etrafında tutar.","reader_payoff":"Okur, ada yönelmenin yalnızca bir ismi anmak olmadığını; başlangıç hareketinin tapınmaya yönelen bir muhataba doğru ağırlık kazandığını fark eder.","support_ids":["sup_ce242bd892b0c6e51152","sup_f7725957d9a8549cb393"],"title":"Özel adda tapınma yönelişinin basıncı"},{"branch_refs":["root_000552/B001"],"candidate_ids":["cand_2189a4173d3d3e00fd4b","cand_846cad2f7d38c7dae4f1","cand_4d462bc2882a3f01451d","cand_505f30bd726b25681f68","cand_69fbec494e02bcd3e720","cand_e74130c63d851de1a020"],"claim":"İlk merhamet sıfatı Allah adına bağlı, belirli ve genişletici bir niteleme açar; aynı anlam ailesinden gelen son sıfat bu alanı gerçekleşen ve süreklilik kazanan merhamet niteliğiyle inceltir, formülü yine Allah adına bağlı olarak tamamlar.","connection_refs":[],"containment":"Birincil okuma Allah'ın sınırsız merhamet sahibi ve merhamet eden oluşudur. Aynı anlam ailesindeki soy bağı ya da döl yatağı görüntüleri bu bulguda literal bir organ veya soy iddiası değildir; son biçimin başka kişilerde kullanılabilmesi de bu ayetteki ilahî genitif bağını değiştirmez.","context_refs":[],"epistemic_status":"Yerel biçim, genitif sıfat zinciri ve aynı anlam ailesindeki biçim farkıyla desteklenen; ikinci merhamet formunu bir inceltme olarak okuyan bulgu.","finding_ref":"micro:paired-mercy-attributes","mechanism":"Her iki sıfatın belirli takısı ve genitif biçimi onları Allah adına bağlar. İlk biçimin genişlik kuvveti, hemen yanındaki biçim değişikliğiyle düz tekrar olmaktan çıkar; son kelime önceki sıfatı belirleyip aynı niteleme zincirini kapatır. Son biçimin insan hakkında gerçekleşen merhameti de niteleyebilmesi, bu eylemde görünen kaliteyi karşılaştırmalı olarak belirginleştirir.","reader_payoff":"Çeviride yan yana duran iki 'merhamet' kelimesi, Arapçada önce kuşatan bir alanı açıp sonra o alanı süreklilik taşıyan iyilikte sabitleyen bir hareket olarak görünür.","support_ids":["sup_1675ff53e3dda1fc6912","sup_3d9db17a6b2ee32b24cc","sup_4f18b826f6b812c5f5c8","sup_5a2186ca53d4a45fa108","sup_5a43ccd2baac6c45ad04","sup_59953667b2f192780589","sup_696cad80b84a282418b4","sup_990bff7b47282b7f417a","sup_a0459e602e39b3c6f314"],"title":"Genişleyen ve gerçekleşen merhamet çifti"},{"branch_refs":["root_000552/B001","root_000552/B002","root_000552/B003"],"candidate_ids":["cand_0d92dd869e87a9099286"],"claim":"Merhamet kelimesi, seçtiği merhamet anlamını korurken yakınlık, içinde taşıma ve koruyucu kuşatıcılık duyumuyla zenginleşir.","connection_refs":[],"containment":"Yerel kelime merhamettir. Soy bağı veya döl yatağı burada doğrudan anlatılan varlıklar değildir; yalnızca koruyucu ve içinde taşıyıcı basınç olarak merhamete renk verir.","context_refs":[],"epistemic_status":"Merhamet anlamının seçildiği yerel sıfata, aynı anlam çevresinden gelen sınırlı ve mecazî bir koruyucu basınç ekleyen bulgu.","finding_ref":"micro:protective-mercy-pressure","mechanism":"Aynı anlam çevresindeki soy bağı ve döl yatağı kullanımları, merhameti yalnızca soyut bir duygu değil, canlıyı gözeten ve içinde taşıyan bir esirgeme basıncı olarak renklendirir. Yerel sıfatın Allah adına bağlı oluşu bu rengi kapsayıcı merhamet yönünde tutar.","reader_payoff":"Okur, 'merhamet' kelimesini uzak bir iyi niyet etiketi olarak değil, koruyan ve kuşatan bir yakınlık olarak duyabilir; bu, ilk sıfatın genişlik kuvvetini bedensel bir sezgiyle görünür kılar.","support_ids":["sup_4f18b826f6b812c5f5c8","sup_696cad80b84a282418b4","sup_dbb3006e444c60b8325c"],"title":"Merhametin koruyucu yakınlık rengi"},{"branch_refs":["root_000552/B001"],"candidate_ids":["cand_9685004bc52b37b5f3cb","cand_15645155a921e968fbc4","cand_2d0978cd3ad4a24e0f20"],"claim":"İki belirli merhamet sıfatının yinelenen başlangıcı ve benzer kapanışı, ilk sıfatı bağlı bir çiftin üyesi, son sıfatı ise ayeti mühürleyen ses olarak duyurur; bu merhamet sonu 1:3'te yeniden yankılanır.","connection_refs":[],"containment":"1:3'teki dönüş, bu ayetin yerel ses ve biçim hareketini destekleyen bir yankıdır; prefatory ifadenin yerine geçen bir surah tezi ya da tek doğru okuma ilanı değildir.","context_refs":[],"epistemic_status":"Yerel ses, biçim ve aynı-surah yankı kayıtlarıyla desteklenen, anlamı sıralamayan akustik ve yapısal bulgu.","finding_ref":"micro:mercy-cadence-and-return","mechanism":"Belirli takıların yinelenmesi, aynı anlam ailesinin iki biçimi ve ritmik yakınlık ilk kelimenin tek başına kapanmayıp ikinci kelimeye akmasını sağlar. Sonraki aynı-surah dönüşü, burada kurulan merhamet kapanışını hamd çerçevesiyle birlikte yeniden işittirir.","reader_payoff":"Okur, son iki kelimeyi yalnızca art arda gelen eş anlamlılar olarak değil, biri alanı açan diğeri sesi ve niteliği mühürleyen bağlı bir çift olarak duyar.","support_ids":["sup_106108c5d58aa80ed91f","sup_5e4026cbb17c38d001fa","sup_6ef75f06d3884729980a","sup_696cad80b84a282418b4","sup_ba63014c1294abaed965"],"title":"İkili ses kapanışı ve merhamet yankısı"},{"branch_refs":[],"candidate_ids":["cand_3f864ad15356ff2ac1aa","cand_d37a7bc52f828cc7df3e"],"claim":"Aktarılan irab ve durak varyantları, merhamet çiftinin yüklem ya da nesne gibi yeniden duyulabileceğini ve son kelimenin 1:2'ye doğru bir geçiş eşiği kurabileceğini görünür kılar; mevcut yapı ise iki sıfatı Allah adına bağlı genitif kapanışta tutar.","connection_refs":[],"containment":"Varyantlar canlı bir sentaktik ve tilavetsel basınç olarak korunur. Bu basınç mevcut genitif nitelemeyi ortadan kaldırmaz ve alternatif bir hüküm seçtirmez.","context_refs":[],"epistemic_status":"Varyant ve durak aparatına dayanan, yerel genitif çözümlemeyle açıkça sınırlandırılmış bulgu.","finding_ref":"micro:variant-syntactic-pressure","mechanism":"Varyant kayıtları sıfatların cümledeki hareket alanını ve durakla sonraki hamd cümlesine bağlanma ihtimalini açar. Yerel uyumlu biçim, bu basıncı genitif sıfat zinciri içinde sınırlar ve kapanışın nasıl kurulduğunu belirginleştirir.","reader_payoff":"Okur, okunuş ve irabın yalnızca son ek ayrıntısı olmadığını; son kelimenin hem bir formülü kapatıp hem de sonraki cümleye geçiş hissi taşıyabildiğini fark eder.","support_ids":["sup_4f18b826f6b812c5f5c8","sup_6ead5cbdfb87cc7d1f19","sup_696cad80b84a282418b4","sup_f5a6078ed810bdf095da"],"title":"Varyantlarda açığa çıkan sentaktik eşik"}],"friction_notes":["HFT payloadı yok; hft_evidence.source_present=false, assigned_record_count=0 ve anchor kapsamı sıfırdır. Bu nedenle baseline/context delta/outlier, aşamalı okuyucu yanıtı veya reader-walk değişimi üzerinden ek bir before/after okuması yazılmadı.","Bağlantı kaydı ve lane context sunulmamış durumda: connection_count=0, authored_connection_count=0 ve selected_context_units=0. Bulgular yalnızca 1:1 yüzey, word-analysis kayıtları ve bunlara bağlı focus-root dallarıyla sınırlandı.","33 focus-root dalının yüzeyde bulunması tek başına etkinlik kanıtı sayılmadı; aday bağlantısı ve bağımsız dilsel taşıyıcı olmayan dallar okuyucu bulgusu yapılmadı. Üç ledger_only QAC oluşumu da bu nedenle ayrı bir karar ile reddedildi."],"identity":{"authoring_request_sha256":"3c3d406858a239787abc17f891461645a49366ad7e6524328ba5d8590e6e76ae","ayah_ref":"29:0","lane":"micro","lane_packet_sha256":"189d1a92c4d4565153c9420b118d0c6142eb40b2bec423cfb126137e326e1df0"},"lane":"micro","movements":[{"draft_prose":"Bu kısa ifade, 'Merhameti sınırsız, merhamet eden Allah'ın adıyla' diyerek başlanılan işi Allah'ın adıyla ilişkilendirir. İlk parça olan {ar:بِ, tr:bi, gloss:ile / adıyla}, Türkçedeki tek bir 'ile'den daha sıkı bir bağ kurar: başlama, okuma ya da anma eylemi kendinden sonra gelen adın içinden ve onunla birlikte yürür. {ar:سْمِ, tr:ismi, gloss:adı} kelimesi bu edatın yönetiminde olduğu için ifade eylemi uzun bir cümle halinde açıklamaz; okuyan kişi başlıyorum, okuyorum veya anıyorum gibi edimleri bu ada bağlayarak cümleyi tamamlar. Böylece söz, bir hüküm bildirmekten önce ilişki kuran bir başlangıç hareketi olarak duyulur.","finding_refs":["micro:opening-bound-act"],"movement_key":"opening-act"},{"draft_prose":"Bu adın iki yönlü bağlanışı, ifadenin taşıyıcı eksenidir. {ar:سْمِ, tr:ismi, gloss:adı} soldan بِ tarafından yönetilir, sağdan {ar:ٱللَّهِ, tr:Allahi, gloss:Allah'ın} ile tamlamaya girer. Bu yüzden 'ad' soyut ve başıboş bir etiket gibi kalmaz; başlangıç hareketini Allah'ın belirli adına ulaştıran bir aracı olur. Adlandırmanın anlam çevresinde yükselme ve belirginleşme duyumu da vardır. Aynı kelime ailesindeki gök ve yükselme görüntüleri burada somut bir göğe dönüşmez; adın anılanı görünür ve ayırt edilir kılan işlevine hafif bir yükseklik tonu verir. Böylece Türkçede 'adıyla' diye geçen kelime, yalnızca isim bildirmez; adı öne çıkaran bir yöneliş de kurar.\n\n{ar:ٱللَّهِ, tr:Allahi, gloss:Allah'ın} burada belirli ve tekil özel ad olarak tamlamanın ulaştığı noktadır; ardından gelen iki merhamet sıfatı bu ada bağlanır. Ad, merhameti kendi başına duran bir nitelik gibi değil, Allah'ın adı içinde açılan bir niteleme zinciri halinde taşır. Ses bakımından da bu tamlama sıkışık bir birlik gibi işitilir; Allah adı, sonraki hamd ilişkisine doğru bu birliği taşıyan dayanak olur. Adın bağlı olduğu anlam çevresinde tapınmaya yöneliş ve hayranlık ya da özlem basıncı da bulunur. Bu basınç, 'Allah'ın adıyla' deyişini nötr bir etiket olmaktan çıkarıp yöneliş ve kulluk duygusu taşıyan bir başlangıç haline getirir; kelime yine belirli Allah adıdır.","finding_refs":["micro:name-as-mediated-designation","micro:divine-name-anchor","micro:divine-name-worship-pressure"],"movement_key":"name-and-anchor"},{"draft_prose":"Allah adından sonra gelen ilk sıfat, {ar:الرَّحْمَٰنِ, tr:er-Rahmân, gloss:merhameti sınırsız} kelimesidir. Başındaki belirli takı ve genitif biçimi, onu Allah adına bağlı bir niteleme yapar; anlamı ise merhameti geniş ve kuşatıcı bir alan olarak açar. Bunun ardından {ar:الرَّحِيمِ, tr:er-Rahîm, gloss:merhamet eden} gelir. Aynı anlam ailesinin ikinci biçimi, ilk kelimeyi düz bir tekrar olarak bırakmaz: genişleyen merhamet, burada gerçekleşen ve süreklilik taşıyan iyilik niteliğinde incelir. Son kelime önceki sıfatı belirleyerek aynı Allah adına bağlı zinciri tamamlar. Bu biçimin insan hakkında gerçekleşen merhameti de niteleyebilmesi, merhameti eylemde görünen bir kalite olarak duyurur; bu ifadede ise genitif bağ onu Allah'a ait sıfat olarak tutar.\n\nMerhamet sözcüğünün anlam çevresinde soy bağı ve döl yatağı gibi yakınlık ve içinde taşıma görüntüleri de bulunur. Bunlar burada doğrudan organ veya soy anlatımı kurmaz; merhameti koruyan, kuşatan ve canlıya ulaşan bir esirgeme basıncı olarak renk verir. Böylece ilk sıfatın genişliği yalnız soyut bir sınırsızlık değil, koruyucu bir yakınlık sezgisiyle birlikte duyulur.","finding_refs":["micro:paired-mercy-attributes","micro:protective-mercy-pressure"],"movement_key":"mercy-pair"},{"draft_prose":"İki belirli merhamet sıfatının yinelenen başlangıcı ve benzer kapanışı, ilk kelimeyi bağlı bir çiftin üyesi, son kelimeyi ise ifadeyi mühürleyen ses olarak duyurur. İlk merhamet çizgisi Fâtiha'nın 1:3'ünde yeniden işitilir; bu dönüş, burada kurulan merhamet kapanışının hamd çerçevesine geçerken de tanınmasını sağlar.\n\nAktarılan irab ve durak biçimleri, bu sıfatların bazı okunuşlarda yüklem ya da nesne gibi yeniden duyulabileceğini, son kelimenin de 1:2'ye doğru bir geçiş eşiği kurabileceğini gösterir. Uyumlu yerel yapı ise iki sıfatı Allah adına bağlı genitif nitelemeler olarak kapatır. Böylece ifade, önce adıyla başlayan eylemi Allah'ın belirli adına bağlar; ardından merhameti genişletir, onu gerçekleşen bir iyilikte sabitler ve son sesiyle tamamlanır. Her iki merhamet okuması da bu açık birincil anlamın içinde yerini korur.","finding_refs":["micro:mercy-cadence-and-return","micro:variant-syntactic-pressure"],"movement_key":"closing-and-variants"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</micro_contribution_json>

## Macro contribution

<macro_contribution_json>
{"ayah_ref":"29:0","candidate_decisions":[{"candidate_id":"cand_ctx_418f81af22bc0cf6a95a","decision":"reject","finding_refs":[],"reason":"الٓمٓ için packet, 29:0’daki Allah adı ve iki merhamet sıfatının okumasını değiştiren somut bir taşıyıcı veya mekanizma sunmuyor; köksüz işaret dizisi olarak kalıyor."},{"candidate_id":"cand_ctx_5aacd4ac1ae35b3db6c9","decision":"accept","finding_refs":["macro:trial-tests-faith"],"reason":"29:2, iman iddiasını sınanma ilişkisine bağlayarak merhamet sıfatlarının host-surah içindeki ilk gerilimini ve belirgin okur dönüşünü sağlar."},{"candidate_id":"cand_ctx_a4b4760cb31d9ed39002","decision":"accept","finding_refs":["macro:trial-tests-faith"],"reason":"29:3 sınamanın doğruluk ile yalanı görünür kıldığını açıkça söyler; focus’taki merhameti sınavdan kaçış değil, hakikati açığa çıkaran eşlik olarak okumaya taşıyan doğrudan kanıttır."},{"candidate_id":"cand_ctx_698b29caf4584fa6cb9f","decision":"narrow","finding_refs":["macro:trial-tests-faith"],"reason":"Yalnız “bizi geçeceklerini sanmak” ve kötü eylem hesabı bölümü, merhametin sorumluluğu askıya almayan bağlamını destekler; ayetin geri kalan ayrıntıları yeni bir focus kazanımı üretmiyor."},{"candidate_id":"cand_ctx_ecc3a42e1dddeabe191d","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Allah’a kavuşma umudu ve belirlenmiş vaktin gelişi, merhameti nihai karşılaşma ufkuna bağlayan sınırlı bir bağlam baskısı sağlar."},{"candidate_id":"cand_ctx_235a159d1a2b2b37dc4c","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Çabanın kişiye dönmesi ve Allah’ın âlemlerden müstağni oluşu, merhametin insan ihtiyacını gözeten fakat Allah’ı insan çabasına bağımlı kılmayan görünümünü verir."},{"candidate_id":"cand_ctx_57042ca2e111c2232e99","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"İman, iyi işler, kusurların örtülmesi ve daha iyi karşılık aynı ayette birleşir; merhametin eylem ve karşılık üzerinden somutlaştığı ayrı bir taşıyıcıdır."},{"candidate_id":"cand_ctx_539f2a28b25ca480f647","decision":"reject","finding_refs":[],"reason":"Ebeveyn baskısı ve itaat ayrıntısı, Allah’ın adı ve merhametinin host-surah okumasında 29:2-7’den farklı bir mekanizma veya belirgin okur kazanımı kurmuyor."},{"candidate_id":"cand_ctx_067f50c3f5ce8d96af3e","decision":"represented","finding_refs":["macro:mercy-enacted-in-return"],"reason":"İman ve iyi işler karşılığında salihler arasına alınma, 29:7’deki eylem-karşılık hareketini yeni bir mekanizma eklemeden tekrar ediyor; f2’de temsil edildi."},{"candidate_id":"cand_ctx_4cb786d6dd70ea5d7743","decision":"narrow","finding_refs":["macro:trial-tests-faith"],"reason":"Sıkıntıyı Allah’ın azabıyla ölçen ve menfaat gelince bağlılık iddia eden kişi, merhameti insanın anlık rahatlığıyla özdeşleştirmeyen sınav karşı-basıncını taşır."},{"candidate_id":"cand_ctx_1a108673f87b0562ba24","decision":"represented","finding_refs":["macro:trial-tests-faith"],"reason":"İman edenlerle münafıkların ayrılması, 29:3’teki doğruluk/yalan açığa çıkışıyla aynı okur işini yapıyor; f1’de temsil edildi."},{"candidate_id":"cand_ctx_f4996472b4fca6efb8b0","decision":"narrow","finding_refs":["macro:mercy-and-accountability"],"reason":"Başkalarının günahını üstlenme vaadinin reddi, merhametin sorumluluğu başkasına devreden bir kaçış olmadığını gösteren sınırlı bir karşı-örnektir."},{"candidate_id":"cand_ctx_f477c25cd0fe296abf08","decision":"accept","finding_refs":["macro:mercy-and-accountability"],"reason":"Taşınan yüklerin çoğalması ve kıyamette sorgu, bağlamın merhamet temasını hesap ve kişisel sorumlulukla birlikte tutan somut bir taşıyıcıdır."},{"candidate_id":"cand_ctx_52b3bc453c3d903eabab","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Nuh’un uzun süreli elçilik süresi ve tufan, merhametin bekleme ve kurtuluşla birlikte okunmasına yarayan bağlam parçasıdır; tarihsel ayrıntıların tamamı ayrıca gerekli değildir."},{"candidate_id":"cand_ctx_f8f59bcc871477f2de7a","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Nuh ve gemi arkadaşlarının kurtarılması ve bunun âlemlere ayet kılınması, merhametin korunma ve hatırlatıcı işaret olarak görünür hale geldiği doğrudan sahnedir."},{"candidate_id":"cand_ctx_12dd72808ab31c342106","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"“Allah’a kulluk edin ve O’na karşı sakının” çağrısı, Allah’ın adıyla başlamayı host-surah içinde yönelme ve kulluk eylemine bağlayan açık bir taşıyıcıdır."},{"candidate_id":"cand_ctx_43b16b4a544fa0ebb5f9","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"Sahte mabutların rızık vermemesi, rızkın Allah yanında aranması, kulluk ve şükür emirleri focus’taki Allah adının yöneldiği ilişkiyi somutlaştırır."},{"candidate_id":"cand_ctx_fd5802f9bbe46371b65e","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Elçinin yalnız açık tebliğle yükümlü oluşu ve önceki ümmetlerin inkârı, f4’teki inkâr-sorumluluk karşı-basıncını yeni bir focus kazanımı eklemeden tekrarlar."},{"candidate_id":"cand_ctx_6267a4166b32ba327cbc","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Yaratılışın başlatılması ve yeniden edilmesi, Allah adını yaratma ve dönüş ufkuna taşıyan sınırlı bir bağlam değişimidir."},{"candidate_id":"cand_ctx_d649d905a90e43b8f98c","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Yeryüzünde dolaşıp yaratılışa bakma çağrısı ile son yaratılışın Allah’a nispeti, f2’deki yeniden kurma ve yönlendirme hareketini destekleyen seçili bölümdür."},{"candidate_id":"cand_ctx_fa801a0f7765408ade0f","decision":"accept","finding_refs":["macro:mercy-and-accountability"],"reason":"Aynı ayette azap ve merhametin, ardından dönüşün anılması, Rahmân/Rahîm’i bağlamın gerçek karşı-basıncıyla birlikte tutan doğrudan kanıttır."},{"candidate_id":"cand_ctx_295f5c73288177984f42","decision":"narrow","finding_refs":["macro:mercy-and-accountability"],"reason":"Yeryüzü ve gökte kaçış imkânının, Allah dışında veli ve yardımcı bulunmadığının söylenmesi, merhameti sonuçlardan kaçış güvencesi saymayan sınırlı karşı-baskıdır."},{"candidate_id":"cand_ctx_829059baab9167e2d9c3","decision":"accept","finding_refs":["macro:mercy-and-accountability"],"reason":"Allah’ın ayetlerini ve O’na kavuşmayı inkâr edenlerin rahmetten ümit kesmesi, focus’taki rahmet kelimesini host-surah içinde açıkça adlandıran ve sorumlulukla karşılaştıran doğrudan kanıttır."},{"candidate_id":"cand_ctx_2bd03aab9339712f29bf","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"İbrahim’in ateşten Allah tarafından kurtarılması ve olayın inananlar için ayet oluşu, merhametin kurtarıcı ve açıklayıcı eylem olarak görünmesidir."},{"candidate_id":"cand_ctx_7b0f896859513353d3e9","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Dünya hayatındaki sahte bağlılıkların kıyamette çözülmesi, Allah’la kurulan adlandırılmış ilişkinin geçici insan bağlarından ayrışmasını gösteren sınırlı bölümdür."},{"candidate_id":"cand_ctx_3521d8297ba03de7a89b","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"İbrahim’in Rabbine hicreti, focus’taki Allah adına yönelme fikrini bir hareket ve güven ilişkisi olarak somutlaştırır; ayetin diğer isimlendirmeleri ek payoff üretmez."},{"candidate_id":"cand_ctx_2fe91ff2e11e403f9f57","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"İbrahim’e nesil, nübüvvet, kitap ve iki dünyada karşılık verilmesi, merhametin süreklilik ve karşılık biçimindeki somut etkisini taşır."},{"candidate_id":"cand_ctx_4ce3703dbfbfbea7d186","decision":"reject","finding_refs":[],"reason":"Lût kavminin belirli fiillerine ilişkin ayrıntı, focus’taki Allah adı ve merhamet okuması için ayrı bir taşıyıcı ya da yeni bir okur kazanımı kurmuyor."},{"candidate_id":"cand_ctx_22eab1c325918409908f","decision":"reject","finding_refs":[],"reason":"Aynı kıssanın davranış ve azap talebi ayrıntıları, 29:21-23 ve 29:40’taki sorumluluk karşı-basıncını aşan, focus’a özgü yeni bir mekanizma sunmuyor."},{"candidate_id":"cand_ctx_608ab17a9a1ada08d654","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"“Rabbim, bana yardım et” yakarışı, bismillah’taki sıkıştırılmış eylemin dua ve yardım talebi olarak açılmasını sağlar; diğer ayrıntılar bu lane için tali."},{"candidate_id":"cand_ctx_6880f31ed5eea4593b25","decision":"narrow","finding_refs":["macro:mercy-and-accountability"],"reason":"Elçilerin iyi haber ile yıkımı aynı gelişte taşıması, merhamet ve hükmün birlikte görünmesi bakımından f4’e sınırlı kanıt verir."},{"candidate_id":"cand_ctx_89a15f8f0df6441683d0","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Lût’un kurtarılacağına dair seçik vaat, f2’deki kurtuluş hareketini doğrudan destekler; ayetin bilgi alışverişinin tamamı gerekli değildir."},{"candidate_id":"cand_ctx_e1135f10776227c4cffb","decision":"represented","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Korkuya verilen “korkma, üzülme” ve kurtuluş vaadi, 29:32’deki aynı kurtuluş mekanizmasını yeni bir okur kazanımı eklemeden yineler."},{"candidate_id":"cand_ctx_046ba434febc812c6bd3","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Gökten indirilen azap, f4’teki yargı ve sonuç karşı-basıncının bir başka örneğidir; focus okumasını ayrıca değiştiren taşıyıcı değil, tekrar niteliğindedir."},{"candidate_id":"cand_ctx_2003174e55317e691eae","decision":"narrow","finding_refs":["macro:revelation-as-mercy"],"reason":"Geride bırakılan açık ayet, bağlamdaki olayların yalnız geçmiş ceza değil, düşünmeye çağıran kalıcı bir işaret olduğunu gösterir; bu, f5’in hatırlatma boyutuyla sınırlı biçimde kullanılır."},{"candidate_id":"cand_ctx_888a224b5163e404ab3e","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"Şuayb kıssasındaki kulluk, son günü umma ve yeryüzünde bozgunculuk yapmama çağrısı, Allah’ın adıyla başlamayı ibadet, umut ve davranış yönüyle açar."},{"candidate_id":"cand_ctx_88231751876f9c718c94","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Yalanlamanın ardından gelen sarsıntı, f4’te zaten taşınan inkâr ve sonuç ilişkisinin tekrarıdır."},{"candidate_id":"cand_ctx_c4b39e9f61c14bd6b1ea","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Şeytanın işleri süslemesi ve yoldan alıkoyması, f3’teki doğru yöneliş/sahte yöneliş ayrımını yeni bir focus kazanımı üretmeden tekrarlar."},{"candidate_id":"cand_ctx_c13ef7186cb06427e974","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Musa’nın açık kanıtlarına rağmen büyüklük taslama, f4’teki açık kanıtı reddetme ve sonuç ilişkisini yineler."},{"candidate_id":"cand_ctx_7936016d0ec928791a9c","decision":"accept","finding_refs":["macro:mercy-and-accountability"],"reason":"Farklı topluluklara farklı sonuçların uygulanması ve Allah’ın zulmetmediğinin özellikle belirtilmesi, merhameti ilahî haksızlık varsayımına indirgemeden hesapla birlikte okutan güçlü bir karşı kanıttır."},{"candidate_id":"cand_ctx_e06f1033a4bddb03b3ca","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Örümcek evinin zayıflığı, Allah dışındaki koruyucuların güven vermeyen dayanaklar oluşunu görünür kılar; bu, Allah’ın adıyla yönelmenin karşıtını somutlaştırır."},{"candidate_id":"cand_ctx_d99f2acd06af656870fb","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Allah’ın çağrılan şeyleri bildiğinin söylenmesi, adın yöneldiği muhatabı bilgi ve hüküm sahibi olarak çerçeveler; benzetmenin diğer unsurları focus kazanımı eklemez."},{"candidate_id":"cand_ctx_8149f884b3bf0966c7ed","decision":"reject","finding_refs":[],"reason":"Mesellerin yalnız bilenlerce kavranması genel bir anlama ilkesi sunuyor; packet, bunu 29:0’ın Allah ve merhamet ifadelerini değiştiren somut bir mekanizmaya bağlamıyor."},{"candidate_id":"cand_ctx_9d29d35d86fbb83c3b0d","decision":"represented","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Göklerin ve yerin Allah tarafından hak ile yaratılması, 29:19-20’deki yaratma ve ayet hareketini yeni bir okur kazanımı eklemeden tekrarlar."},{"candidate_id":"cand_ctx_19292c4b43d75e6638d0","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"Vahyin okunması, namazın kurulması ve Allah’ı anmanın büyüklüğü, focus’taki adın anılmasını okuma, ibadet ve hatırlama eylemleriyle somutlaştırır."},{"candidate_id":"cand_ctx_9d89e15fc27400e542ff","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"En güzel biçimde konuşma ve “ilahımız da ilahınız da birdir” diyerek teslim olma, Allah’ın adının ayrıştırıcı bir slogan değil ortak muhataba yönelen bir ilişki olduğunu gösterir."},{"candidate_id":"cand_ctx_293bd5892f174fe9a834","decision":"narrow","finding_refs":["macro:revelation-as-mercy"],"reason":"Kitabın indirilmesi ve farklı insanların ona iman etmesi, f5’teki vahyin merhamet/hatırlatma taşıyıcısına sınırlı destek verir."},{"candidate_id":"cand_ctx_07eb59b34b7137ec03e4","decision":"reject","finding_refs":[],"reason":"Peygamberin önce kitap okumamış ve yazmamış oluşuna dair kanıt, vahyin niteliğini savunur; ancak focus’taki rahmet okumasına değişmiş bir okur kazanımı sağlamaz."},{"candidate_id":"cand_ctx_dd3b140d5b8525577b03","decision":"narrow","finding_refs":["macro:revelation-as-mercy"],"reason":"Ayetlerin bilenlerin göğüslerinde açık oluşu, merhamet ve hatırlatmanın içte taşınan bir bilgiye dönüşmesini f5 içinde sınırlar; inkârın tekrar kısmı ayrıca yeni değildir."},{"candidate_id":"cand_ctx_c5e98f2467f20f7af2c2","decision":"narrow","finding_refs":["macro:revelation-as-mercy"],"reason":"İşaret talebi ile Allah katındaki ayetler arasındaki ayrım, f5’teki vahyin hazır bulunan bir merhamet ve uyarı olarak okunmasına sınırlı zemin sağlar."},{"candidate_id":"cand_ctx_c6e5b6f8c3fedc08e8f9","decision":"accept","finding_refs":["macro:revelation-as-mercy"],"reason":"Kitabın doğrudan “rahmet ve hatırlatma” diye nitelenmesi, focus’taki Rahmân/Rahîm’i host-surah içinde aynı sözcük ailesiyle değiştiren en doğrudan bağlam kanıtıdır."},{"candidate_id":"cand_ctx_9aadaadd523e83282427","decision":"narrow","finding_refs":["macro:mercy-and-accountability"],"reason":"Allah’ın şahit ve göklerle yerin bilgisine sahip oluşu, merhamet temasını kapsamlı bilme ve hesap çerçevesine taşıyan sınırlı destek verir."},{"candidate_id":"cand_ctx_c001da308f1aa4809e1e","decision":"narrow","finding_refs":["macro:mercy-and-accountability"],"reason":"Azabın belirlenmiş vakit nedeniyle ertelenmesi, bağlamdaki merhamet/hesap gerilimine zaman ve mühlet boyutu ekler."},{"candidate_id":"cand_ctx_1088e10d939537b0a0be","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Cehennemin inkârcıları kuşatması, f4’teki sonuç ve kaçışsızlık karşı-basıncını tekrarlar."},{"candidate_id":"cand_ctx_1fdba7778e516eb8e7ab","decision":"represented","finding_refs":["macro:mercy-and-accountability"],"reason":"Azabın üstten ve alttan kuşatması ile yapılanların tadılması, 29:54’teki sonuç çerçevesini yeni bir focus mekanizması olmadan yineler."},{"candidate_id":"cand_ctx_bd41acb81f97521520bb","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"“Ey kullarım” hitabı, geniş yeryüzü ve yalnız Allah’a kulluk emriyle Allah adını yakın hitap, hareket alanı ve ibadet çağrısı içinde açar."},{"candidate_id":"cand_ctx_ac73526a3b41d7112700","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Her nefsin ölümü tatması ve Allah’a dönüş, f2’deki dönüş ufkunu destekler; ayetin ölüm genellemesi ayrı bir merhamet dalı kurmaz."},{"candidate_id":"cand_ctx_412b57cf22e7bd61c531","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"İman ve salih amel sahiplerine kalıcı yurt, nehirler ve iyi iş yapanların karşılığı verilmesi, merhametin ödül ve yerleştirme olarak somutlaşmasını taşır."},{"candidate_id":"cand_ctx_3775af9c2f5a3d9e90a2","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Sabır ve Rabbe dayanma, f2’deki merhametin sınav aralığında sürdürülen bir güven ve sebatla karşılandığını gösteren ayrı bir taşıyıcıdır."},{"candidate_id":"cand_ctx_f5532b8752be15476d45","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Rızkını taşıyamayan canlıların Allah tarafından rızıklandırılması, merhameti canlıların ihtiyacına ulaşan somut bir ihsan olarak gösterir."},{"candidate_id":"cand_ctx_c163ea876a928efa0ab9","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Gökleri, yeri, güneşi ve ayı yaratanın Allah olduğu kabulü, Allah adını yaratıcı ve düzenleyici muhatap olarak f3 içinde sınırlar; inkârın son dönüşü ayrıca f4’e taşınmaz."},{"candidate_id":"cand_ctx_9e15ff1f99e6016ab686","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Allah’ın rızkı açıp daraltması ve her şeyi bilmesi, f2’deki etkin merhamet/provision hareketini doğrudan güçlendirir."},{"candidate_id":"cand_ctx_e1cf2238f59206779918","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Gökten su indirip ölü toprağı diriltme ve ardından hamd, merhametin hayat verici ve şükre açılan eylem olarak görünmesidir."},{"candidate_id":"cand_ctx_b0c364173775d3034fe2","decision":"narrow","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Dünya hayatının geçiciliği ve gerçek hayatın ahirette oluşu, f2’deki karşılık ufkunu genişletir; merhameti yalnız bu hayatın rahatına bağlamaz."},{"candidate_id":"cand_ctx_c6c31abdb67606c03db0","decision":"accept","finding_refs":["macro:name-as-orientation"],"reason":"Denizde Allah’a içtenlikle yönelip kurtulunca ortak koşmaya dönülmesi, bismillah’taki yönelişin kriz anına mahsus değil, kurtuluş sonrasında da korunması gereken bir ilişki olduğunu gösterir."},{"candidate_id":"cand_ctx_51e6c2d7da9e2623bc7b","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Verilen nimetle yetinip eğlenme ve ileride bilecek olma karşıtlığı, f3’teki şükür/yöneliş çağrısına sınırlı bir karşı-örnek sağlar."},{"candidate_id":"cand_ctx_0b270eecc2b36c26853c","decision":"narrow","finding_refs":["macro:name-as-orientation"],"reason":"Kutsal ve güvenli kılınmış yer ile çevredeki kapılma tehlikesi, Allah’ın nimeti ve güvenliğini tanıyıp inkâr etme karşıtlığını f3 içinde somutlaştırır."},{"candidate_id":"cand_ctx_b94e5486188ff4f5a128","decision":"accept","finding_refs":["macro:mercy-and-accountability"],"reason":"Allah adına yalan uydurmak veya hak geldiğinde onu yalanlamak, merhamet adını keyfî bir iddiaya dönüştürmenin karşısına doğruluk ve hesap sınırı koyar."},{"candidate_id":"cand_ctx_f80ef0f59b65d6128ea4","decision":"accept","finding_refs":["macro:mercy-enacted-in-return"],"reason":"Gayret edenlere yolların gösterilmesi ve Allah’ın iyilik yapanlarla beraber olduğunun söylenmesi, f2’deki etkin merhameti yönlendirme ve yakınlık olarak kapanışta görünür kılar."}],"coverage_complete":true,"findings":[{"branch_refs":["root_000047/B002","root_000552/B001"],"candidate_ids":["cand_ctx_5aacd4ac1ae35b3db6c9","cand_ctx_a4b4760cb31d9ed39002","cand_ctx_698b29caf4584fa6cb9f","cand_ctx_4cb786d6dd70ea5d7743","cand_ctx_1a108673f87b0562ba24"],"claim":"29:0 tek başına merhamet sahibi Allah’ın adıyla başlamayı kurarken, host-surah bağlamı bu merhameti iman iddiasını sınayan ve doğruluğu görünür kılan bir eşlik olarak çerçeveler.","connection_refs":[],"containment":"Bu bağlam sınavın kendisini merhametin tanımı yapmaz ve merhametin birincil genişliğini daraltmaz; yalnızca host-surah’ın ilk hareketinin merhamet ile sınamayı aynı okuma içinde tuttuğunu gösterir.","context_refs":["29:2","29:3","29:4","29:10","29:11"],"epistemic_status":"Seçilmiş host-surah ayetlerine ve focus yüzeyine dayanan, sınırları belirtilmiş makro sentez.","finding_ref":"macro:trial-tests-faith","mechanism":"29:2-4’teki sınanma, geçmiş toplulukların denenmesi ve doğruluk ile yalanın açığa çıkması; 29:10-11’deki sıkıntı, bağlılık iddiası ve iman edenlerle münafıkların ayrılması, focus’taki Rahmân/Rahîm adlarını sınavın yokluğu yerine sınav boyunca işleyen bir ilişki içinde okutur.","reader_payoff":"Okur, başlangıçtaki merhameti yalnızca rahatlık vaadi olarak değil, sözü yaşayışa taşıyan ve hakikati görünür kılan bir yakınlık olarak duyabilir.","support_ids":["sup_ctx_f599f164d802447eff34","sup_ctx_98a5159d0126ec0fb2c5","sup_ctx_eedda422cf28379d9e1b","sup_ctx_34a8e266e22998ba530d","sup_ctx_edb3c44c34223813deb7"],"title":"Merhametin sınav içinde duyulması"},{"branch_refs":["root_000552/B001"],"candidate_ids":["cand_ctx_ecc3a42e1dddeabe191d","cand_ctx_235a159d1a2b2b37dc4c","cand_ctx_57042ca2e111c2232e99","cand_ctx_067f50c3f5ce8d96af3e","cand_ctx_52b3bc453c3d903eabab","cand_ctx_f8f59bcc871477f2de7a","cand_ctx_6267a4166b32ba327cbc","cand_ctx_d649d905a90e43b8f98c","cand_ctx_2bd03aab9339712f29bf","cand_ctx_2fe91ff2e11e403f9f57","cand_ctx_89a15f8f0df6441683d0","cand_ctx_e1135f10776227c4cffb","cand_ctx_9d29d35d86fbb83c3b0d","cand_ctx_ac73526a3b41d7112700","cand_ctx_412b57cf22e7bd61c531","cand_ctx_3775af9c2f5a3d9e90a2","cand_ctx_f5532b8752be15476d45","cand_ctx_9e15ff1f99e6016ab686","cand_ctx_e1cf2238f59206779918","cand_ctx_b0c364173775d3034fe2","cand_ctx_f80ef0f59b65d6128ea4"],"claim":"29:0’daki merhamet, host-surah bağlamında insanın dönüşü, kurtuluşu, rızkı ve hidayeti içinde eylemle görünür hale gelir.","connection_refs":[],"containment":"Bu sahneler merhametin sözlük tanımını tüketmez ve bütün bağlamı tek bir yardım imgesine indirgemez; farklı olaylarda görülen kurtuluş, karşılık, rızık ve yönlendirme örneklerini bir arada tutar.","context_refs":["29:5","29:6","29:7","29:9","29:14","29:15","29:19","29:20","29:24","29:27","29:32","29:33","29:44","29:57","29:58","29:59","29:60","29:62","29:63","29:64","29:69"],"epistemic_status":"Birden çok doğrudan bağlam ayetinin ortak eylem çizgisinden çıkarılan, açıkça sınırlanmış makro yorum.","finding_ref":"macro:mercy-enacted-in-return","mechanism":"29:5-7’de karşılaşma, kişiye dönen çaba, kusurların örtülmesi ve iyi karşılık; kıssa ve yaratılış sahnelerinde kurtarılma, yeniden kurulma ve işaret; 29:58-63’te ödül, sabır, rızık ve ölü toprağın dirilmesi; 29:69’da yolların gösterilmesi aynı focus merhametini olaylar ve karşılıklar içinde görünür kılar.","reader_payoff":"Okur, “merhamet eden” adının yalnızca bir nitelik bildirmediğini, dönüşe, korunmaya, beslenmeye ve yol bulmaya değen somut hareketler içinde çalıştığını kavrar.","support_ids":["sup_ctx_366ac95007ae5a78f1c4","sup_ctx_f2d3bc2bd53df90627ea","sup_ctx_66dcd2ea19454b766a11","sup_ctx_a5082e137958913476d2","sup_ctx_2bb46b410a10d51ce61f","sup_ctx_1a97f2c95fa2e6b33c61","sup_ctx_55c8810cdf42a71a8d38","sup_ctx_1655746be4f4a3555b83","sup_ctx_a2eee77377507874e47e","sup_ctx_42ec3ad2a2aa044202ee","sup_ctx_c6711897d1f0a9fa3ce9","sup_ctx_bae7cc65f6b57c51728f","sup_ctx_f1aee54d57cd768fcc3a","sup_ctx_82a8bb2f306c56e39b36","sup_ctx_a7a07f1c43063342c68f","sup_ctx_06dae7466fe95a24d639","sup_ctx_723d457b273cf4782800","sup_ctx_7df2e347fd8b5a16545b","sup_ctx_bef0c3f3569dafff5e13","sup_ctx_fc3bf1642dcda741e228","sup_ctx_f1200e54c99c96711bdf"],"title":"Merhametin dönüşte ve eylemde görünmesi"},{"branch_refs":["root_000047/B002","root_000745/B005"],"candidate_ids":["cand_ctx_12dd72808ab31c342106","cand_ctx_43b16b4a544fa0ebb5f9","cand_ctx_7b0f896859513353d3e9","cand_ctx_3521d8297ba03de7a89b","cand_ctx_608ab17a9a1ada08d654","cand_ctx_888a224b5163e404ab3e","cand_ctx_e06f1033a4bddb03b3ca","cand_ctx_d99f2acd06af656870fb","cand_ctx_19292c4b43d75e6638d0","cand_ctx_9d89e15fc27400e542ff","cand_ctx_bd41acb81f97521520bb","cand_ctx_c163ea876a928efa0ab9","cand_ctx_c6c31abdb67606c03db0","cand_ctx_51e6c2d7da9e2623bc7b","cand_ctx_0b270eecc2b36c26853c"],"claim":"29:0’daki “Allah’ın adıyla” başlangıcı, host-surah’ın kulluk, dua, şükür, rızık arayışı ve teslimiyet eylemleriyle belirli bir yöneliş kazanır.","connection_refs":[],"containment":"Bağlam, kısa başlangıç formülünü başka bir cümleye çevirmediği gibi onun hakkında bağımsız bir hukuk hükmü de kurmaz; yalnızca focus’taki adlandırılmış yönelişin bu host-surah’da hangi eylemlerle göründüğünü gösterir.","context_refs":["29:16","29:17","29:25","29:26","29:30","29:36","29:41","29:42","29:45","29:46","29:56","29:61","29:65","29:66","29:67"],"epistemic_status":"Focus morfolojisi ile host-surah eylemlerini birleştiren yazar sentezi; sözlük eşleştirmesi olarak sunulmuyor.","finding_ref":"macro:name-as-orientation","mechanism":"Focus’taki {ar:بِ, tr:bi, gloss:ile} ile {ar:ٱسْمِ, tr:ismi, gloss:adı} arasındaki bağda başlanılan iş açıkça söylenmez; 29:16-17, 29:36, 29:45-46, 29:56 ve 29:61-67’deki kulluk, arayış, dua, anma, şükür, teslimiyet ve nimet karşısındaki cevaplar bu sıkışmış eylemin host-surah’daki yönünü gösterir.","reader_payoff":"Okur, bismillah’ı yalnız söylenen bir başlangıç değil, Allah’a yönelme, O’na kulluk etme ve verilen nimeti tanıma hareketine açılan bir söz olarak okuyabilir.","support_ids":["sup_ctx_a3e3a8513ebbcbc523b2","sup_ctx_f45b176eacb4cf83215d","sup_ctx_ee4fcc5b9c982b070d05","sup_ctx_668c526b63881448a3e7","sup_ctx_a2eccdab769648c1d5d3","sup_ctx_467d02efafcb4c2ce972","sup_ctx_4c87091b02621288d5a5","sup_ctx_dd3ba2364b3629db57a4","sup_ctx_83d82123e73e2edb7e45","sup_ctx_5413f347f125ee46ab79","sup_ctx_4b3255df3ee47b952d54","sup_ctx_ea699b023bcc743851df","sup_ctx_33317da7d3c11cab91cb","sup_ctx_eff666058b238d57942e","sup_ctx_e38752653d9c0a0ee17d"],"title":"Allah’ın adının yönelişe açılması"},{"branch_refs":["root_000047/B002","root_000552/B001"],"candidate_ids":["cand_ctx_f4996472b4fca6efb8b0","cand_ctx_f477c25cd0fe296abf08","cand_ctx_fd5802f9bbe46371b65e","cand_ctx_fa801a0f7765408ade0f","cand_ctx_295f5c73288177984f42","cand_ctx_829059baab9167e2d9c3","cand_ctx_6880f31ed5eea4593b25","cand_ctx_046ba434febc812c6bd3","cand_ctx_88231751876f9c718c94","cand_ctx_c4b39e9f61c14bd6b1ea","cand_ctx_c13ef7186cb06427e974","cand_ctx_7936016d0ec928791a9c","cand_ctx_9aadaadd523e83282427","cand_ctx_c001da308f1aa4809e1e","cand_ctx_1088e10d939537b0a0be","cand_ctx_1fdba7778e516eb8e7ab","cand_ctx_b94e5486188ff4f5a128"],"claim":"Host-surah, 29:0’ın merhamet adını azap, hesap, inkâr ve insan sorumluluğuyla aynı alan içinde tutarak otomatik kaçış anlamına kapanmasını engeller.","connection_refs":[],"containment":"Bu karşı-basınç birincil merhamet okumasını iptal etmez ve azap ile merhamet arasında bir kazanan sıralamaz; bağlamdaki farklı sonuçları, insan cevabını ve ilahî adalet iddiasını aynı anda canlı tutar.","context_refs":["29:12","29:13","29:18","29:21","29:22","29:23","29:31","29:34","29:37","29:38","29:39","29:40","29:52","29:53","29:54","29:55","29:68"],"epistemic_status":"Doğrudan karşıt bağlam kanıtlarına dayanan, birincil okumayı koruyan sınırlama sentezi.","finding_ref":"macro:mercy-and-accountability","mechanism":"29:12-13’te başkasının yükünü üstlenme vaadi reddedilir; 29:21-23’te azap, merhamet, dönüş ve rahmetten ümit kesme yan yana gelir; kıssalarda ve 29:40’ta sonuçlar ile Allah’ın zulmetmediği açıkça belirtilir; 29:53-55 ve 29:68’de mühlet, kuşatıcı azap ve Allah adına yalanın hesabı sürdürülür.","reader_payoff":"Okur, Rahmân/Rahîm adlarının bağlam içinde sonuçları silen otomatik bir güvenceye dönüşmediğini, merhamet ile sorumluluk ve hesap geriliminin birlikte taşındığını görür.","support_ids":["sup_ctx_5b8fcdc081028c453919","sup_ctx_c33ae20529d5036864e8","sup_ctx_8c3a6a9e6d4bfb87b270","sup_ctx_b7f6728413efe4840071","sup_ctx_54a898dd7e54a4887f4f","sup_ctx_b260be450683e5a6938f","sup_ctx_377513d687688d4dd0d8","sup_ctx_ad77b9a69a66f0641407","sup_ctx_daba41faf318f9bae51b","sup_ctx_2307bb2811738060a5f2","sup_ctx_9894d5945f09e4ce2ba6","sup_ctx_28bf6775d8f1852f75dc","sup_ctx_0daf185e66f60e5c884d","sup_ctx_4fe817cdf089ff164a17","sup_ctx_1a56b78443bd922fb059","sup_ctx_966a7c872274c5a563b7","sup_ctx_8adf98c8e212ba8cd41e"],"title":"Merhametin hesapla birlikte tutulması"},{"branch_refs":["root_000552/B001"],"candidate_ids":["cand_ctx_2003174e55317e691eae","cand_ctx_293bd5892f174fe9a834","cand_ctx_dd3b140d5b8525577b03","cand_ctx_c5e98f2467f20f7af2c2","cand_ctx_c6e5b6f8c3fedc08e8f9"],"claim":"29:0’ın merhameti, 29:35 ve 29:47-51 bağlamında indirilen kitabın rahmet ve hatırlatma oluşunda, insanın duyup içte taşıdığı bir erişim olarak da görünür.","connection_refs":[],"containment":"Bu bağlam vahyi merhamet diye adlandırır ama bütün insan tepkilerini aynılaştırmaz; iman, inkâr ve ayetleri taşıma biçimleri ayrı kalır ve birincil merhamet anlamı korunur.","context_refs":["29:35","29:47","29:49","29:50","29:51"],"epistemic_status":"29:51’de açıkça adlandırılan rahmet ve hatırlatmadan hareket eden, komşu ayetlerle desteklenmiş bağlam sentezi.","finding_ref":"macro:revelation-as-mercy","mechanism":"Açık bırakılan ayet, indirilen kitap, göğüslerde taşınan açık ayetler ve ayet talebine verilen cevap, 29:51’deki “rahmet ve hatırlatma” nitelemesine bağlanır; böylece focus’taki merhamet yalnız olaylarda gerçekleşen yardım değil, karşılaşılabilir ve hatırlanabilir bir söz olarak da host-surah’da görünür.","reader_payoff":"Okur, başlangıçtaki merhameti yalnız dışarıdan gelen koruma olarak değil, kitabın okunması ve hatırlanmasıyla insana ulaşan bir açıklık olarak da fark eder.","support_ids":["sup_ctx_19cacb5449190e7ab8c0","sup_ctx_e072a7c1088ae7ce8692","sup_ctx_6160da2f30dc28ba72ac","sup_ctx_56b1081e9b9f3c44b8f5","sup_ctx_75f0c4779c946d239f46"],"title":"Rahmetin hatırlatma olarak ulaşması"}],"friction_notes":["Bu lane packetinde HFT yükü ve aşamalı okuyucu yanıtı bulunmuyor; before/after hareketi, focus’ın tek başına bir başlangıç cümlesi oluşu ile 29:1-69’un doğrudan host-surah baskısı arasındaki farktan kuruldu.","Bağlam ayetlerinin çoğu aynı sorumluluk, kurtuluş veya yöneliş çizgisini tekrar ediyor; tekrarlar temsil edildi, yalnızca yeni taşıyıcı ve okur kazanımı sağlayan bölümler ayrı karar olarak korundu."],"identity":{"authoring_request_sha256":"9c6b1d8694e9d0a0632f020ac8f0b700fd83c8383e2f2dc7142b7c07bd9715f7","ayah_ref":"29:0","lane":"macro","lane_packet_sha256":"bd5c4048ce7c2558a501825b721a3e405d29a65cc461238886117d29c952ed52"},"lane":"macro","movements":[{"draft_prose":"Tek başına bu başlangıç, {ar:بِسْمِ, tr:bismillâhi, gloss:Allah’ın adıyla} diyerek merhameti geniş ve sürekli olan Allah’ın adıyla yola çıkmayı söyler. Burada {ar:ٱلرَّحْمَٰنِ, tr:er-Rahmân, gloss:merhameti kuşatan} ile {ar:ٱلرَّحِيمِ, tr:er-Rahîm, gloss:merhameti eylemde sürdüren} aynı ada bağlanır; söz, merhameti önceleyen bir giriş olarak durur.\n\nSûrenin yanına gelince bu girişin önüne bir sınav sahnesi açılır: “inandık” demekle bırakılmayan insanlar denenir, daha önce yaşayanlar da denenmiş ve doğru söz ile yalan açığa çıkarılmıştır. Böylece başlangıçtaki merhamet, sınavın yokluğu şeklinde değil, sözü yaşayışa taşıyıp hakikati görünür kılan bir eşlik olarak derinleşir. Sınavın kendisi merhametin tanımı değildir; bağlam, ikisini aynı yürüyüşte tutar.","finding_refs":["macro:trial-tests-faith"],"movement_key":"movement-trial-tests-faith"},{"draft_prose":"Tek başına söz, Allah’ın adını anarak O’nun merhametini çağırır. Sûre ilerledikçe merhametin nasıl işlediği görünür: Allah’a kavuşmayı bekleyen için belirlenmiş vakit gelir; kişinin çabası kendisine döner; iman ve iyi işler kusurların örtülmesiyle ve güzel karşılıkla karşılanır. Nuh’un ve gemi arkadaşlarının kurtarılması bir işaret olur; İbrahim’e verilen nesil ve karşılık, ateşten kurtuluş ve Lût’un kurtarılacağına dair vaat, merhametin soyut bir sıfat olmaktan çıkıp korunma ve karşılık şeklinde görünmesini sağlar.\n\nYaratılışın başlaması ve yeniden kurulması, her canlının rızkının verilmesi, rızkın açılıp daraltılması, ölü toprağın suyla diriltilmesi ve gayret edenlere yolların gösterilmesi de bu hareketi farklı sahnelerde sürdürür. Böylece tek başına “merhamet eden” diye duyulan ad, bağlam içinde dönüşe, rızka, kurtuluşa ve hidayete dokunan etkin bir iyilik olarak okunur. Bu sahneler merhametin sözlük tanımını tüketmez; yalnızca bu sûrede onun hangi eylemlerle görünür olduğunu gösterir.","finding_refs":["macro:mercy-enacted-in-return"],"movement_key":"movement-mercy-enacted-in-return"},{"draft_prose":"Tek başına {ar:بِ, tr:bi, gloss:ile} ile {ar:ٱسْمِ, tr:ismi, gloss:adı} arasındaki bağda başlanılan iş açıkça söylenmez; okur “Allah’ın adıyla” der ve eylem sıkıştırılmış kalır. Ev sahibi sûre bu yönü kendi emir ve yakarışlarıyla belirginleştirir: Allah’a kulluk etmek, O’na karşı sakınmak, rızkı O’nun yanında aramak, şükretmek, O’na yönelmek ve teslim olmak.\n\nTehlikede Allah’a içtenlikle yalvarıp kurtulunca ortak koşmaya dönülen sahne, ismi anmanın yalnız bir söz değil, süreklilik isteyen bir yöneliş olduğunu da gösterir. Aynı bağlam Allah’ı yaratıcı ve rızık verici olarak tanıyan fakat bunun gereğini bozan kişileri yan yana tutar. Bu, başlangıçtaki ifadeyi başka bir cümleye dönüştürmez; sadece “adıyla başlamak”ın sûrenin içindeki karşılığını yönelme, kulluk ve şükür hareketleriyle görünür kılar.","finding_refs":["macro:name-as-orientation"],"movement_key":"movement-name-as-orientation"},{"draft_prose":"Tek başına {ar:ٱلرَّحْمَٰنِ ٱلرَّحِيمِ, tr:er-Rahmâni er-Rahîm, gloss:merhameti kuşatan ve eylemde sürdüren} Allah’ın merhametini öne çıkarır. Sûrenin karşı basıncı bu merhameti otomatik bir kaçış güvencesine indirgemez: “azap eder ve merhamet eder” denir; rahmetten ümit kesme, hesap, farklı azap örnekleri ve “Allah onlara zulmetmedi, onlar kendilerine zulmetti” açıklaması aynı bağlamda yer alır. Sonra gerçeği Allah’a karşı uydurmak ve geldiğinde hakkı yalanlamak ağır bir sorumluluk olarak gösterilir.\n\nBu sahneler başlangıçtaki merhameti geri almaz; onu sonuçları ve insanın cevabını silmeyen, hüküm ve dönüş ufkuyla birlikte duran bir iyilik olarak çerçeveler. Azap ile rahmetin nasıl dağıtıldığına dair burada bir sıralama kurulmaz; iki yönün de bağlamda canlı kalması, başlangıcın tek renkli okunmasını engeller.","finding_refs":["macro:mercy-and-accountability"],"movement_key":"movement-mercy-and-accountability"},{"draft_prose":"Başlangıçta merhamet Allah’ın adıyla duyulur; bağlamda bu merhamet bir sözün ve kitabın insana ulaşmasında da adlandırılır: indirilen kitap, “rahmet ve hatırlatma” diye nitelenir. Önceki ayetlerde geride bırakılan açık ayetler, indirilen kitabın farklı insanlarca karşılanması ve bilenlerin göğüslerinde açık olan ayetler bu hatırlatmanın zeminini kurar.\n\nBöylece bismillah’ın merhameti yalnızca dışarıdan verilen yardım değil, insanın duyup hatırlaması ve doğruyu seçmesi için açılan bir erişim olarak da görünür. Yine de vahyi merhamet diye anmak bütün tepkileri aynılaştırmaz: inananlar, inkârcılar ve ayetleri taşıma biçimleri bağlamda ayrı ayrı kalır.","finding_refs":["macro:revelation-as-mercy"],"movement_key":"movement-revelation-as-mercy"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</macro_contribution_json>

## Global contribution

<global_contribution_json>
{"ayah_ref":"29:0","candidate_decisions":[{"candidate_id":"cand_basmala_1ea05fc79f88cd5284d5","decision":"accept","finding_refs":["global:ad-yetki-cercevesi","global:merhamet-sinama-zemini"],"reason":"Paket, بِسْمِ içindeki adlandırma taşıyıcısını ve Allah'ın özel adıyla ilişkisini, 29:2-6 ile 29:51 ve 29:53'teki daha geniş tetikleyicileri, focus ayetine dönüş yolunu ve okuyucu kazanımını birlikte veriyor. Bu nedenle aday, birbirinden farklı mekanizmaları koruyan iki sınırlandırılmış global bulgu olarak kabul edildi."}],"coverage_complete":true,"findings":[{"branch_refs":["root_000745/B005","root_000047/B002"],"candidate_ids":["cand_basmala_1ea05fc79f88cd5284d5"],"claim":"29:0'daki adlandırma, surenin sınama, kurtuluş ve dönüş anlatılarını Allah'ın yetkisi altında okutan bir üst başlık gibi işler; bu geniş yankı, بِسْمِ ile Allah'ın özel adı arasındaki ilişki üzerinden focus ayetine geri döner.","connection_refs":[],"containment":"Bu okuma, 'Merhameti sınırsız, merhamet eden Allah'ın adıyla' birincil anlamını ve adla başlama bildirimini korur. Üst başlık ve hesap verebilirlik etkisi, kelimenin bu yerde duruşu ile paketteki geniş tetikleyicilerden çıkan bir yankıdır; ayeti bütün sura tezine indirgemez ve adın sözlük anlamının yerine geçmez.","context_refs":["29:2","29:3","29:4","29:5","29:6","29:53"],"epistemic_status":"Paketin kanonik desteğiyle taşınan, odak ifadenin yerleşimi ve sonraki tetikleyicilerden çıkarılan sınırlı bir geniş-bağlam yorumudur.","finding_ref":"global:ad-yetki-cercevesi","mechanism":"Paketin geniş okuyuşunda adlandırma, insanların söylediklerinin sınama, bilgi ve emek tarafından açığa çıkarıldığı ilk diziye yerleştirilir; 29:53'te belirlenmiş bir adlandırma yeniden görünerek aynı ad baskısını tetikler. Böylece başlangıçtaki ad, yalnızca bir giriş işareti değil, söz ve eylemin hangi yetki altında sorumluluk kazanacağını belirleyen bir çerçeve olarak okunur.","reader_payoff":"Okur, basmalayı süslenmiş bir önsöz olarak bırakmadan, ilerideki iddia ve eylemlerin kimin adıyla okunacağını baştan belirleyen bir başlangıç eylemi olarak kavrar.","support_ids":["sup_basmala_b9fdfc10b909918af5b8"],"title":"Adın geniş bağlamı taşıyan çerçevesi"},{"branch_refs":["root_000552/B001"],"candidate_ids":["cand_basmala_1ea05fc79f88cd5284d5"],"claim":"Başlangıçtaki iki merhamet nitelemesi, daha geniş dizideki sınamayı ilahî terk ediliş olarak değil, açığa çıkaran ve düzelten bir ilişki içinde okumaya elverişli bir zemin kurar; merhamet burada sınamanın bildirilen sebebi değil, onun okunuşunu çevreleyen çerçevedir.","connection_refs":[],"containment":"Bu bulgu, 'Merhameti sınırsız, merhamet eden Allah'ın adıyla' sözündeki birincil merhamet bildirimini taşır ve ona geniş bağlamdan gelen bir ilişki çerçevesi ekler. Paket merhametin sınamaya neden olduğunu söylemediği için nedensellik kurulmaz; alışılmadık kök ve bağlam yankıları, açık merhamet okumasını bastırmadan ihtiyatla tutulur.","context_refs":["29:2","29:3","29:5","29:6","29:51"],"epistemic_status":"Paket içindeki zayıf çapraz-run bulgusu ile geniş okuyuşun verdiği bağlardan çıkarılan, nedensellik iddiası taşımayan ihtiyatlı bir rezonanstır.","finding_ref":"global:merhamet-sinama-zemini","mechanism":"29:2-3'te sınama fiilinin tekrarı ve 29:5-6'da belirlenmiş buluşma ile çabanın Allah'ın işitmesi, bilmesi ve kendine yeter oluşu içinde anılması, focus ayetindeki merhamet kökünü sonraki açığa çıkma hareketine bağlar. 29:51'de merhametin sürekli okunan bir kitapta işleyen bir hitap biçimi olarak görünmesi, bu başlangıç zeminine daha sonraki bir taşıyıcı da verir.","reader_payoff":"Okur, sınanmayı otomatik olarak ilahî terk ediliş diye okumak zorunda kalmaz; iddianın açığa çıkması ve biçimlenmesi, eşikte duyulan merhametle birlikte düşünülebilir.","support_ids":["sup_basmala_b9fdfc10b909918af5b8"],"title":"Merhametin sınamayı çevreleyen zemini"}],"friction_notes":["Bu prefatory birimde yerel HFT, inter-ayah ve ayrı bağlantı kayıtları uygulanabilir değildir; geniş okumalar yalnızca aynı destek demetindeki çapraz-run ve okuyucu yürüyüşünün verdiği tetikleyicilerle sınırlı tutuldu."],"identity":{"authoring_request_sha256":"9ce020e6de69bf9dd327352c22bb0e0d526a8af7dc624b0a543ee9c599d7d547","ayah_ref":"29:0","lane":"global","lane_packet_sha256":"b87171824e80905503148fdfa1708d9b9e6825aa0688dea54466124c82ea9ffb"},"lane":"global","movements":[{"draft_prose":"Merhameti sınırsız, merhamet eden Allah'ın adıyla. Bu sözde ad, yalnızca başlangıçta anılan bir isim olarak kalmaz. Sözün hemen ardından insanın söyledikleri sınanıp yaptıklarıyla açığa çıktığında, başlangıçtaki adlandırma bütün bu yürüyüşün hangi yetki altında okunacağını belirleyen yüksek bir başlık gibi duyulur. Böylece basmala, ilerideki iddia ve eylemleri kendi başına sahiplenmez; onları Allah'ın adıyla sorumluluk alanına yerleştirir. Daha sonra belirlenmiş bir adlandırmanın yeniden görünmesi de bu yankıyı güçlendirir: ad vermek, yalnızca anmak değil, sözün ve eylemin sınırını görünür kılmak anlamına gelebilir. Bu, ayetin açıkça söylediği tek anlamın yerine geçen bir hüküm değil, başlangıçtaki yerleşimle geniş bağlamın birlikte açtığı sınırlı bir imkandır.","finding_refs":["global:ad-yetki-cercevesi"],"movement_key":"ad-yetki-cercevesi"},{"draft_prose":"Merhameti sınırsız, merhamet eden Allah'ın adıyla sözü, eşiğe iki merhamet niteliği yerleştirir. Sonraki akışta sınanmanın tekrarlanması, belirlenmiş buluşmanın ve çabanın ilahî işitme, bilme ve kendine yeter oluşla birlikte anılması, bu merhameti sınamanın karşısına dikilen bir duygu değil, sınamanın nasıl okunacağını çevreleyen bir ilişki olarak geri getirir. Sınanma böylece ilahî terk ediliş olarak değil, iddianın açığa çıkması ve düzelmeye yönelmesiyle birlikte düşünülebilir; yine de merhametin sınamaya sebep olduğu söylenmez. Daha ileride merhametin sürekli okunan kitapta işleyen bir hitap biçimine dönüşmesi, eşikteki iki niteliğin yalnızca duygusal bir önsöz değil, düzeltici açıklığın taşıyıcı zemini olabileceğini hissettirir.","finding_refs":["global:merhamet-sinama-zemini"],"movement_key":"merhamet-sinama-zemini"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</global_contribution_json>
