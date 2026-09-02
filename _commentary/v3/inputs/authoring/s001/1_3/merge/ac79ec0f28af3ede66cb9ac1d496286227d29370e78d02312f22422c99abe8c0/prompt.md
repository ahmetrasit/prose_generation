# Commentary v3 canonical prose merge

You are the fresh final writer for **1:3**. Write the four declared
first-pass Layer-2 files from the reconciled findings and the three independently
prepared scope drafts.

The canonical governing documents and Layer-2 prompt are inlined below
verbatim. This file is self-contained: every filename mentioned by those texts
is an in-document reference to material below, not an instruction to read the
repository. They govern composition, pedagogy, voice, Arabic spans,
completeness, and output. This v3 wrapper changes only the staging and
filenames:

- the finding decisions are already reconciled and locked;
- the three scope drafts are source work to recompose, never sections to
  concatenate;
- you may reorganize and proportion the exposition, but you may not reject,
  add, rank, or collapse a locked finding;
- scope names, candidate identities, and analysis instruments stay out of the
  reader prose;
- any `before`/`after` movement names reader-disclosure order in the supplied
  analysis, not historical revelation order, textual chronology, or a claim
  that the ayah once existed without its neighbors;
- use the supplied focus-surface packet for exact Arabic and transliteration
  values, analytic gloss boundaries, and morphology; render Arabic in the
  canonical single-span syntax with a natural Turkish gloss, never by copying
  raw wrappers or internal coordinates;
- write exactly the four declared first-pass files and modify nothing else;
- after writing them, remain in this same conversation for the canonical
  editorial follow-up.

Micro gives the local footing, macro gives pericope-bounded changes, and global
gives grounded wider discoveries. Recompose them by the ayah's acts, relations,
images, tensions, and reader payoffs. Findings from different scopes may share
a paragraph when they genuinely work together, but each distinct mechanism and
payoff must remain recoverable.

The first-pass prose should reveal before it compresses. Do not replace a
concrete lexical or contextual image with a generic summary, and do not hide an
exploratory or noncanonical finding merely because it needs a short boundary.
Every locked surprise must let the reader see the carrier, the image or
relation, and what changes in the reading. Compatible findings may cooperate in
one movement, but related conclusions do not erase distinct mechanisms.

## Declared first-pass files

- prose: `_commentary/v3/outputs/authoring/s001/1_3/merge/ac79ec0f28af3ede66cb9ac1d496286227d29370e78d02312f22422c99abe8c0/1_3.prose.tr.md`
- evidence: `_commentary/v3/outputs/authoring/s001/1_3/merge/ac79ec0f28af3ede66cb9ac1d496286227d29370e78d02312f22422c99abe8c0/1_3.evidence.tr.md`
- findings index: `_commentary/v3/outputs/authoring/s001/1_3/merge/ac79ec0f28af3ede66cb9ac1d496286227d29370e78d02312f22422c99abe8c0/1_3.index.tr.md`
- friction: `_commentary/v3/outputs/authoring/s001/1_3/merge/ac79ec0f28af3ede66cb9ac1d496286227d29370e78d02312f22422c99abe8c0/1_3.friction.tr.md`

## Governing principles — verbatim

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

## Commentary specification — verbatim

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

Status: active draft, updated 2026-08-18. Layer 2 v2 and Layer 3 v3 workflow
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

Layer 2 continues to use one bundle per ayah. The production bundle is the
output of `scripts/tier_branch_payloads.py`, run against the full ayah bundle
from `scripts/build_bundle.py` before `scripts/instantiate.py`. The tierer may
project only `root_lexicon` dictionary/gloss branch payloads and its recorded
branch policy. It must preserve every root target, every dictionary branch
identity, and every non-branch field. Its required-source, malformed-citation,
and semantic-payload checks fail loudly; it never falls back to dictionary
source files.

Branch payload tiers are transport projections, not finding ranks or prose
budgets. Layer 2 has no root, paragraph, or word-count quota. It must state every
materially distinct, anchored latent activation or surprise with a significant
reader payoff, including one supported by a compact branch; it must also avoid
repetition, filler, and available branches that do not change understanding.
The admission threshold is density-invariant: a finding receives the same test
in a three-root and a twenty-six-root ayah. Findings may share prose only when
their mechanism and payoff are the same and every admitted ref still has an
identifiable landing.

Layer 3 builds a separate hermetic source packet from Quran text, the typed
primary floor, the completed four-file Layer-2 v2 artifact set for every
numbered ayah, and whatever network-v3/V11 sources are available. Missing
optional source families are warnings, not build failures. Missing Quran text,
typed primary floor, or complete Layer-2 artifacts aborts. See
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).

</commentary_spec>

## Channel definitions — verbatim

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

## Canonical Layer-2 prompt — verbatim

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

## Locked finding ledger

<reconciled_findings_json>
{"ayah_ref":"1:3","coverage":{"global":{"accepted":23,"decided":26,"disputed":0,"locked":11,"new":4,"rejected":3,"supplied":26},"macro":{"accepted":20,"decided":20,"disputed":0,"locked":20,"new":0,"rejected":0,"supplied":20},"micro":{"accepted":16,"decided":17,"disputed":0,"locked":12,"new":0,"rejected":1,"supplied":17}},"disputed_decisions":[],"friction_notes":[{"lane":"micro","note":"Üç assigned HFT kaydı görünür tutuldu. Her birinde exact Arabic yalnızca yüzey temasını doğrular; HFT'nin segmentation, word index, root, branch ve role iddiaları bağımsız paket kanıtı gibi sunulmadı. Legacy_unbound statüsü, destek ve analoji sınırları kabul edilen bulguların containment alanında korundu.","type":"hft_provenance"},{"lane":"micro","note":"B002 ve B003 temasları gerçek fakat keşifsel imge düzeyindedir. Soy bağı, döl yatağı, gebelik veya doğum anlamları doğrudan çeviri olarak değil, yinelenen kök ile yerel biçim/sözdizimi düzeninin taşıdığı sınırlı analojiler olarak bırakıldı.","type":"secondary_lexical_pressure"},{"lane":"micro","note":"B001 F003 ve F004 için karşılıklılık ya da esenlik dileme kalıbı yoktur. B002 F002/F003 için organ aktarımı veya bağ sürdürme-koparma eylemi yoktur. B004'ün üç facet'i için de tıbbi, hayvansal veya doğum sonrası bağımsız bağlam yoktur.","type":"unactivated_facets"},{"lane":"micro","note":"1:1 basmala dönüşü ve 55:1 başlık yankısı mikro düzeyde tekrar kanıtı olarak tutuldu. 55:1 bulgusu 1:3'ün genitif-ilahî ad işlevini yönetmez; daha geniş sure yapısı iddiasına çevrilmedi.","type":"recurrence_scope"},{"lane":"micro","note":"cand_a8883dc9a7a282d88748 yalnızca ر ح م kök taşıyıcısını kaydeder. Yüzey kapsaması diğer gerçek bulgularla tamamlandı, fakat ledger_only kaydı kendisi bağımsız finding olarak yayımlanmadı.","type":"ledger_only"},{"lane":"micro","note":"'Merhameti sınırsızdır, merhamet edendir.' plain footing korunur; genişlik, etkin iyilik, zincir, ses, tekrar ve sınırlı kök imgeleri bu önermenin yerine geçirilmeden üzerine eklenir.","type":"primary_floor"},{"lane":"micro","note":"Packet'ta connection_registry boş olduğundan connection_refs tüm bulgularda boştur; bu, yerel word-analysis ve branch temaslarını silmez.","type":"connections"},{"lane":"macro","note":"Tüm connection target'larında exact Arabic surface evidence supplied, ancak target morphology ve lexical analysis supplied değil; connection claims yalnızca notun bildirdiği relation ve yüzey bağlamıyla sınırlı tutuldu.","type":"lane_friction"},{"lane":"macro","note":"On altı HFT branch citation'ı branch registry'de bağımsız review_facet olmadan geldi. Bunlar candidate ve atlas coverage'da görünür bırakıldı; accepted findings yalnızca kayıtlı facet'i olan dalları branch_contributions'a aldı.","type":"lane_friction"},{"lane":"macro","note":"HFT kayıtlarının legacy-unbound provenance'ı ve confidence/alternative boundary'leri containment içinde korundu; provenance hiçbir kaydı görünmez kılmadı.","type":"lane_friction"},{"lane":"macro","note":"Name-disclosure ile visible-mark, accounting-frame ile ledger-kinship, petition-aid ile dependent-service ve gestation ile womb-pathway ayrı tutuldu; aynı focus carrier'a dönseler de mechanism, direction veya reader payoff'ları tam duplicate değildir.","type":"lane_friction"},{"lane":"macro","note":"Unresolved branch'lerin dışlanması rejection değil, bağımsız facet yokluğu nedeniyle daraltmadır; HFT raw support ID'leri ve aday kararları korunmuştur.","type":"lane_friction"},{"lane":"global","note":"Target morphology and target lexical analysis were not supplied. Connection judgments use only the exact target Arabic, supplied source notes, and bounded focus-side relations; no missing morphology is invented.","type":"lane_friction"},{"lane":"global","note":"The four B004 facets are not all activated: only F001 has a bounded contact. F002 and F003 remain no_independent_trigger, while the accepted B004 finding is explicitly analogical and narrow.","type":"lane_friction"},{"lane":"global","note":"The foster/step-family and stagewise-nurture branches are cross-root or source-image carriers. Their contributions remain visible, but they are not lexical identities with the focus r-ḥ-m forms.","type":"lane_friction"},{"lane":"global","note":"Reciprocal nominations and reciprocal counterevidence were judged separately. Counterevidence at 8:75, 19:87, 33:6 and 60:3 remains visible; where exact target wording exposed a bounded relation, the result was narrowed rather than treated as a veto.","type":"lane_friction"},{"lane":"global","note":"Repeated formula targets such as the 26:104 family and 17:110 are represented only where the same mechanism and payoff are already covered; generic naming-only rows without a changed reading are rejected.","type":"lane_friction"},{"lane":"global","note":"The unanchored HFT items retain their support in candidate and support ledgers when narrowed, but their source qualifications prevent them from becoming an uncontained surah thesis.","type":"lane_friction"}],"identity":{"authoring_request_sha256":"2af3a6aeabcaeab8d9cbeb18bd6ec684929e3646d2fd6da46b93e873a36c9dc8","ayah_ref":"1:3"},"locked_findings":[{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_2fb12f95b6f9a1077b6e"],"claim":"1:3'teki ilk ad, 1:1'deki basmala merhamet çiftiyle yeniden görünür; böylece 1:2'deki övgü ve rablık bildirimi iki merhamet adının kurduğu bir çerçeve içinde kalır.","connection_refs":[],"contact_refs":[],"containment":"Bu, yerel tekrar ve halka etkisidir; 55:1'in eşik yankısını bu bulguya katmaz ve sonraki ayetler hakkında kapsamlı bir yapı iddiası kurmaz.","epistemic_status":"established","lane":"micro","locked_finding_ref":"locked:micro:finding-basmala-ring","mechanism":"1:1 ile 1:3 arasında aynı iki adın somut tekrarı vardır; yerel genitif zincir ve bitişik çiftlenme bu dönüşü bağımsız bir formül yankısı olarak taşır.","member_finding_refs":["micro:finding-basmala-ring"],"proposal_keys":[],"reader_payoff":"Okur, 1:2'deki övgü ve rablığı merhametten kopuk bir bildirim olarak değil, merhametle çevrelenmiş bir zincir olarak okur.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-basmala-ring"}],"support_ids":["sup_272c858fee96121a92cf","sup_d9badd7741765a383942"],"title":"Basmala çiftinin merhamet halkası olarak dönüşü"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_18d73edde943787b4080","cand_2658d4ef92298f73e244"],"claim":"ٱلرَّحْمَٰنِ ile ٱلرَّحِيمِ bağlaçsız ve bitişik bir çift oluşturur: yinelenen kesin başlangıç, r-h-m sessiz çerçevesi ve ortak genitif kapanışı çifti bağlarken uzun ünlü farkı biçimsel ayrımı duyurur.","connection_refs":[],"contact_refs":[],"containment":"Ses ve biçim, tek başına sözlükte bulunmayan yeni bir anlam icat etmez; yalnızca iki yerel adın birlik ve farkını görünür kılar.","epistemic_status":"established","lane":"micro","locked_finding_ref":"locked:micro:finding-mercy-pair-sound","mechanism":"İki sözcük aynı kökü ve ses çerçevesini paylaşır; ilk ve son konumları, uzun ünlülerin farklı dağılımı ve kapanıştaki ortaklıkla açılış-kapanış dengesi kurar.","member_finding_refs":["micro:finding-mercy-pair-sound"],"proposal_keys":[],"reader_payoff":"Okur, ikinci adı ilkini mekanikçe yineleyen bir etiket olarak değil, aynı merhamet alanını farklı biçimle tamamlayan ikinci yarı olarak duyar.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-mercy-pair-sound"}],"support_ids":["sup_272c858fee96121a92cf","sup_75eb074a3ef5fea3ca41","sup_02816da6adce33fc2739","sup_d834754f4a5016ec8ba2"],"title":"İki merhamet adının ses ve biçimle dengelenmesi"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_52d721bf55fbc6055858"],"claim":"İlk sözcüğün kesin ve özel ad kaydı, onu yeni tanıtılan belirsiz bir sıfat olmaktan çıkarıp 1:1'den beri etkin olan tanınmış ilahî ad olarak kurar.","connection_refs":[],"contact_refs":[],"containment":"İlk sözcüğün yerel kesin-ad kaydıyla sınırlıdır; ikinci adın kapanışını veya 55:1'deki eşik işlevini bu bulguya yüklemez.","epistemic_status":"established","lane":"micro","locked_finding_ref":"locked:micro:finding-divine-title-register","mechanism":"Kesinlik, özel ad işlevi ve ilahî gönderge; sıradan insanî niteleme yerine süreklilik taşıyan ilahî ad okumasını destekler.","member_finding_refs":["micro:finding-divine-title-register"],"proposal_keys":[],"reader_payoff":"Okur, ilk adı yalnızca 'merhametli' diye eklenmiş bir açıklama değil, ilahî ad zincirinin tanınan bir üyesi olarak algılar.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-divine-title-register"}],"support_ids":["sup_272c858fee96121a92cf","sup_c8e3357a8bd067782315"],"title":"İlk adın kesin ilahî ad kaydı"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_acb38a75be04ec0aa63a","cand_025e40150412f75173b9"],"claim":"Her iki kesin genitif ad da 1:2'deki ilahî gönderge zincirine bağlıdır; 1:3, yeni ve bağımsız bir cümle başlatmak yerine önceki bildirimi iki merhamet adıyla niteler.","connection_refs":[],"contact_refs":[],"containment":"Yerel genitif bağlanma ve uygulama olasılığıyla sınırlıdır; tüm sentaktik tartışmayı tek bir zorunlu çözüm diye kapatmaz.","epistemic_status":"established","lane":"micro","locked_finding_ref":"locked:micro:finding-genitive-chain","mechanism":"İki sözcüğün genitif oluşu, kesinlikleri ve aralarında bağlaç bulunmadan aynı çiftte yer almaları; ilk adın önceki zinciri taşımasını, ikincinin de aynı zincire bağlı kapanış olarak kalmasını sağlar.","member_finding_refs":["micro:finding-genitive-chain"],"proposal_keys":[],"reader_payoff":"Okur, iki adı gevşek bir sonradan eklenmiş sıfat dizisi olarak değil, rablık bildirimini içeriden sürdüren bağlı bir ad çifti olarak okur.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-genitive-chain"}],"support_ids":["sup_272c858fee96121a92cf","sup_724702948b5a584f3539","sup_02816da6adce33fc2739","sup_4fa5e3e0018a25417f1f"],"title":"İki genitif adın 1:2 zincirini sürdürmesi"},{"branch_contributions":[{"boundary":"Belirli insanî muhatap, acı durumu veya insan tarzı duygulanım doğrudan ayete eklenmez.","branch_ref":"root_000552/B001","contribution":"B001'in yumuşaklık ve iç yakınlık çekirdeği, ilahî adların soyut bir etiketten çok yönelmiş merhamet tonu taşımasına katkı verir.","distinctive_facet":"Bir başkasının durumu karşısında yüreğin yumuşaması ve içten yakınlık","facet_id":"F001","independent_anchor":"İki kesin ilahî merhamet adının aynı genitif zincirinde ve aynı göndergeye bağlı tek çift olarak kurulması","surface_carrier":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_985bed732d2b34730bfb"],"claim":"İki ilahî merhamet adı, merhameti yalnızca sonuç bildiren bir etiket değil, muhataba yönelen yumuşaklık ve iç yakınlık tonu olarak da duyurur.","connection_refs":[],"contact_refs":["micro:contact-b001-tenderness"],"containment":"Tanrısal kullanımda insanî duygulanım veya belirli bir acı çeken muhatap varsayılmaz; bulgu B001 F001'in yönelmiş yumuşaklık basıncıyla sınırlıdır.","epistemic_status":"qualified","lane":"micro","locked_finding_ref":"locked:micro:finding-mercy-tenderness","mechanism":"Yinelenen kökün aynı ilahî ad çiftinde taşınması ve çiftin önceki rablık bildirimine bağlı oluşu, acıma-yumuşaklık çekirdeğini yerel ad işlevi içinde görünür kılar.","member_finding_refs":["micro:finding-mercy-tenderness"],"proposal_keys":[],"reader_payoff":"Okur, 'merhamet' karşılığının içinde yönelmiş şefkat ve yakınlık bulunduğunu fark eder.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-mercy-tenderness"}],"support_ids":["sup_272c858fee96121a92cf","sup_fbeb59f860e5554e459c"],"title":"Merhamet adının yumuşaklık ve iç yakınlık yönü"},{"branch_contributions":[{"boundary":"Bu ilahî adın 1:3'teki yerel uzmanlaşmasıdır; genel bir insanî merhamet veya kalıplaşmış dilek eylemi değildir.","branch_ref":"root_000552/B001","contribution":"B001 F005, geniş merhamet adının rablığı çıplak hükümden kuşatıcı gözetme ve iyilik yönüne çekmesini sağlar.","distinctive_facet":"Tanrı hakkında esirgemenin genişliği ve iyiliğin yaratılmışlara ulaşması","facet_id":"F005","independent_anchor":"İlk kesin ilahî adın genitif biçimde 1:2'deki rablık zincirine bağlanması","surface_carrier":"ٱلرَّحْمَٰنِ"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_985bed732d2b34730bfb"],"claim":"1:2'deki rablık zinciri, 1:3'teki ٱلرَّحْمَٰنِ ile salt sahiplik veya hüküm olarak değil, yaratılmışlara kuşatıcı iyilik ulaştıran gözetici bakım olarak belirginleşir.","connection_refs":[],"contact_refs":["micro:contact-b001-divine-specialization"],"containment":"Bu yerel ad-zinciri etkisidir; bağımsız bir doktrin özeti, tüm sonraki ayetlere yayılmış bir hüküm veya B001'in karşılıklılık/dilek kullanımı değildir.","epistemic_status":"qualified","lane":"micro","locked_finding_ref":"locked:micro:finding-lordship-as-care","mechanism":"İlk adın kesin ilahî ad oluşu, genitif uygulamayla önceki rablık bildirimini sürdürmesi ve genişlik taşıyan biçimsel basınç, rablığı merhamet çerçevesinde yeniden niteler.","member_finding_refs":["micro:finding-lordship-as-care"],"proposal_keys":[],"reader_payoff":"Okur, rablık bildirimini merhametle yumuşamış ve yaratılmışlara iyilik ulaştıran bir gözetme olarak okur.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-lordship-as-care"}],"support_ids":["sup_272c858fee96121a92cf","sup_fbeb59f860e5554e459c"],"title":"Geniş merhametin rablığı bakım olarak belirlemesi"},{"branch_contributions":[{"boundary":"Bu, biçim ve sıra üzerinden kurulan niteliksel karşıtlıktır; kesin zaman kipleri, zorunlu kronoloji veya iki ayrı sözlük anlamı iddia edilmez.","branch_ref":"root_000552/B001","contribution":"B001 F002, merhametin yalnızca içsel bir tutum değil, genişçe ulaşan ve ardından süreklilik taşıyan etkin esirgeme olarak okunmasına katkı verir.","distinctive_facet":"İç yönelişin acınanı esirgeyip ona iyilikte bulunma sonucuna taşınması","facet_id":"F002","independent_anchor":"Aynı kökün bitişik iki farklı biçimde yinelenmesi ve biçim karşıtlığının ilk genişlik ile ikinci süreklilik arasında yerel bir düzen kurması","surface_carrier":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_e0a7f8e4a3ea54e06ebb","cand_c2784c118726435c48fa","cand_cd0ae7737ec400621108"],"claim":"Aynı kökün iki biçimi bir merhameti iki kayıtsız tekrar olarak değil, ilkinde genişçe ulaşan, ikincisinde ise kalıcı ve yönelmiş biçimde işleyen bir iyilik olarak kademelendirir.","connection_refs":[],"contact_refs":["micro:contact-b001-beneficent-care"],"containment":"Biçim farkı iki zorunlu zaman kipi veya kesin bir kronoloji değildir; B001 F002'nin etkin esirgeme ve iyilik sonucunu destekleyen niteliksel bir okuma olarak tutulur. İkinci adın yakın uygulama çifti ya da aynı göndergeye doğrudan niteleme olarak bağlanabilmesi açık bırakılır. HFT desteği exact Arabic yüzey çapası, legacy_unbound kaynak ve aday model sınırları içinde korunur; HFT'nin bölümleme, indeks, kök, dal ve rol iddiaları bağımsız kanıt sayılmaz.","epistemic_status":"exploratory","lane":"micro","locked_finding_ref":"locked:micro:finding-breadth-to-continuance","mechanism":"Bitişik aynı kök, biçim farkı ve ikinci adın son konumu; ilk adın taşan genişliği ile ikinci adın yerleşik ve sürdürülen bakımını aynı çift içinde karşılaştırır.","member_finding_refs":["micro:finding-breadth-to-continuance"],"proposal_keys":[],"reader_payoff":"Okur, ٱلرَّحْمَٰنِ ve ٱلرَّحِيمِ adlarının 'Tanrı merhametlidir' önermesini mekanikçe yinelemediğini, merhametin ulaşma alanı ile sürekliliğini birlikte kurduğunu görür.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-breadth-to-continuance"}],"support_ids":["sup_02816da6adce33fc2739","sup_c232b085604e158cfceb","sup_2fafa89b7c69dfe85821","sup_20bee313d3d1fd1fd1a1"],"title":"Genişlikten sürekliliğe inen merhamet çifti"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_fab3dcd67cb9c46e7fbe"],"claim":"ٱلرَّحِيمِ, paylaşılabilir bir sıfat alanıyla merhameti ilişkisel olarak anlaşılır kılabilir; fakat kesinlik, özel ad kaydı ve genitif zincir yerel işlevi ilahî ad olarak korur.","connection_refs":[],"contact_refs":[],"containment":"Bu yalnızca seçilebilir sıfat alanının lexical pressure'ıdır; 1:3'teki sözcük sıradan bir insan sıfatı olarak yeniden sınıflandırılmaz.","epistemic_status":"qualified","lane":"micro","locked_finding_ref":"locked:micro:finding-adjective-pressure","mechanism":"Sıfat alanına açık sözlük basıncı, yerel kesin ilahî ad ve zincire bağlılıkla birlikte çalışır; bu gerilim ilişkisel anlaşılabilirliği korurken sıradan sıfata dönüşmeyi engeller.","member_finding_refs":["micro:finding-adjective-pressure"],"proposal_keys":[],"reader_payoff":"Okur, ikinci adın insanî ilişkilerde anlaşılabilir bir merhamet yönü taşıdığını sezer, fakat ayetteki ilahî ad işlevini kaybetmez.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-adjective-pressure"}],"support_ids":["sup_02816da6adce33fc2739","sup_4dd33d41bdd71e1ff6cd","sup_4fa5e3e0018a25417f1f"],"title":"İkinci adın paylaşılabilir sıfat basıncı"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_5515309fc1e575afa1d7"],"claim":"ٱلرَّحِيمِ, iki sözcüklü ayetin sonundaki konumuyla aynı kökü yineleyen çiftin dengeli kapanış ve iniş noktası olur; kapanış farklı bir sıfatla değil, merhamet kökünün ikinci biçimiyle yapılır.","connection_refs":[],"contact_refs":[],"containment":"Kapanış etkisi bu iki sözcüklü ayetin yerel ses ve sıra düzenine aittir; sonraki söylem hakkında otomatik sonuç çıkarmaz.","epistemic_status":"established","lane":"micro","locked_finding_ref":"locked:micro:finding-closure-epithet","mechanism":"Son konum, yinelenen kök, ortak ses çerçevesi ve kapanış epiteli profili, ilk genişlikten sonra süreklilik taşıyan merhameti son duyulan nitelik yapar.","member_finding_refs":["micro:finding-closure-epithet"],"proposal_keys":[],"reader_payoff":"Okur, ayetin sonunu genel bir merhamet bildirimiyle değil, devam eden ve yönelmiş bakımın landing point'iyle kapatır.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-closure-epithet"}],"support_ids":["sup_02816da6adce33fc2739","sup_61326fbf176c211565b2"],"title":"İkinci adın kapanışta merhameti indirmesi"},{"branch_contributions":[],"branch_refs":[],"candidate_ids":["cand_635c2435c34747828997"],"claim":"İlk adın 55:1'deki sure açılışı kullanımı, 1:3'teki aynı başlığa daha geniş bir Kur'anî eşik yankısı verir; ancak yerel sözcük 1:2'ye bağlı ilahî ad olarak kalır.","connection_refs":[],"contact_refs":[],"containment":"55:1 yalnızca yankı ve başlık bağlamıdır; 1:3'ün yerel sözdizimini yönetmez ve bu bulgu makro bir sure yapısı iddiasına genişletilmez.","epistemic_status":"qualified","lane":"micro","locked_finding_ref":"locked:micro:finding-title-threshold","mechanism":"Aynı başlığın 55:1'de sure açılışında bulunması, 1:3'teki başlık işlevine tekrar ve eşik basıncı ekler; yerel genitif uygulama bu yankının anlamı devralmasını sınırlar.","member_finding_refs":["micro:finding-title-threshold"],"proposal_keys":[],"reader_payoff":"Okur, 1:3'teki ilk adı yalnızca yerel bir niteleme değil, sure açılışlarında eşik kurabilen tanınmış bir başlık olarak da duyabilir.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-title-threshold"}],"support_ids":["sup_0ed1d956d711789d667e","sup_272c858fee96121a92cf"],"title":"55:1'deki başlık ve eşik yankısı"},{"branch_contributions":[{"boundary":"Bu doğrudan akrabalık veya soy anlamı değildir; B002 F002 ve F003'teki organ aktarımı ile bağ sürdürme/koparma eylemleri etkinleştirilmez.","branch_ref":"root_000552/B002","contribution":"B002 F001, rahmeti uzak bir iyilik değil, yakınlığı kuran ve koruyan bir yöneliş gibi imgeleştirmeye katkı verir.","distinctive_facet":"Ortak soydan gelmenin kurduğu yakın ve kalıcı ilişki","facet_id":"F001","independent_anchor":"Aynı kökün iki komşu kesin genitif adında yinelenmesi ve çiftin aynı ilahî göndergeye bağlı tek ilişki olarak kurulması","surface_carrier":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"branch_refs":["root_000552/B002"],"candidate_ids":["cand_90e67649f941ab2b06ef","cand_fe32ac952ea4fa4a9c2d"],"claim":"Yinelenen merhamet kökü ve tek bağlı ad çifti, merhameti ayrı bir alıcıya verilen iyilikten öte, yakınlığı kuran ve sürdüren bir yöneliş olarak imgesel biçimde duyurabilir.","connection_refs":[],"contact_refs":["micro:contact-b002-nearness"],"containment":"Bu, B002'nin yalnızca F001 çekirdeğini taşıyan keşifsel bir image-pressure'dır. Ortak ata, gerçek soy bağı, bağ sürdürme/koparma fiili veya doğrudan 'yakın soy bağı' çevirisi ileri sürülmez. HFT desteği sup_7599367ac31807367809 ile taşınır; exact Arabic yalnızca yüzey temasını doğrular ve legacy_unbound kaynak niteliği korunur.","epistemic_status":"exploratory","lane":"micro","locked_finding_ref":"locked:micro:finding-kinship-pressure","mechanism":"B002 F001'in ortak-soy kaynaklı yakın bağ imgesi, gerçek soy veya akrabalık bağlamından değil; iki adın aynı kökü paylaşması ve aynı ilahî göndergeye bağlı tek çift halinde kurulmasından gelen ilişkisel yerellikten beslenir.","member_finding_refs":["micro:finding-kinship-pressure"],"proposal_keys":[],"reader_payoff":"Okur, merhametin ilişki kuran ve kopmamayı gözeten bir yakınlık basıncı taşıdığını sezebilir.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-kinship-pressure"}],"support_ids":["sup_272c858fee96121a92cf","sup_5cd2ebcd0e3899a1084e","sup_7599367ac31807367809"],"title":"Merhamet kökünün yakınlık imgesi"},{"branch_contributions":[{"boundary":"Organın kendisi veya gebelik olayı ayetin sözlük anlamı değildir; yalnızca sınırlı bir imge basıncı korunur.","branch_ref":"root_000552/B003","contribution":"B003 F001, rahmetin kuşatan ve besleyerek sürdüren bir ortam olarak düşünülmesine maddi bir analoji sağlar.","distinctive_facet":"Dişi bedenindeki iç organın yavrunun oluşup geliştiği kuşatıcı kap olması","facet_id":"F001","independent_anchor":"Aynı kökteki iki biçimin genişlikten sürekliliğe inen yerel karşıtlığı","surface_carrier":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"}],"branch_refs":["root_000552/B003"],"candidate_ids":["cand_90e67649f941ab2b06ef","cand_c5e46909163d28966a09"],"claim":"İlk biçimin geniş kuşatıcılığı ile ikinci biçimin süreklilik taşıyan yönü, merhameti oluşmayı ve dayanmayı mümkün kılan kuşatıcı-besleyici bir ortam olarak keşifsel biçimde imgeselleştirebilir.","connection_refs":[],"contact_refs":["micro:contact-b003-enclosing-sustaining"],"containment":"Bu yalnızca B003 F001'e bağlı keşifsel bir analojidir; döl yatağı, gebelik, doğum veya organ sözlük anlamı 1:3'e yüklenmez. HFT desteği sup_bc9f3e0dd94d781c05aa ile taşınır; exact Arabic yüzey çapası, atfedilmiş HFT bölümlemesi ve legacy_unbound statüsü birbirine karıştırılmaz.","epistemic_status":"exploratory","lane":"micro","locked_finding_ref":"locked:micro:finding-womb-pressure","mechanism":"B003 F001'in iç kap ve taşıma imgesi, döl yatağına ilişkin bir yüzey bağlamından değil; aynı kökün iki biçimindeki genişlik-süreklilik karşıtlığının kuşatma ve sürdürme yönleriyle analojik olarak buluşmasından doğar.","member_finding_refs":["micro:finding-womb-pressure"],"proposal_keys":[],"reader_payoff":"Okur, rahmeti dışarıdan gelen tekil yardımın yanında varlığı içinde tutan, oluşmasını ve sürmesini sağlayan bir ortam gibi düşünebilir.","referral_payloads":[],"scope_movements":[{"lane":"micro","member_finding_ref":"micro:finding-womb-pressure"}],"support_ids":["sup_272c858fee96121a92cf","sup_5cd2ebcd0e3899a1084e","sup_2fafa89b7c69dfe85821","sup_c232b085604e158cfceb","sup_bc9f3e0dd94d781c05aa"],"title":"Merhametin kuşatan ve sürdüren ortam imgesi"},{"branch_contributions":[{"actual_contribution":"Bakımı tek seferlik iyilikten aşamalı yetiştirme ve tamamlama işine çevirir.","boundary":"Aşamalı bakım imgesidir; odak sıfatının literal lordluk anlamı değildir.","branch_ref":"root_000532/B002","carrier":"1:2'deki lordluk bağlamı","distinctive_facet":"Onarım, yetiştirme ve tamamlanma","facet_id":"SOURCE_IMAGE","independent_anchor":"A'nın aşamalı nurture ve guardianship statement'ları"},{"actual_contribution":"Odak merhametini iç durumdan koruyan etkin iyiliğe taşır.","boundary":"Etkin sonuç facet'idir; tüm bakım dallarının lexical gloss'u değildir.","branch_ref":"root_000552/B001","carrier":"1:3'teki ٱلرَّحْمَٰنِ / ٱلرَّحِيمِ","distinctive_facet":"Acımanın esirgemeye ve iyiliğe etkin sonucu","facet_id":"F002","independent_anchor":"A'nın compassion-to-care statement'ı"},{"actual_contribution":"Merhametin bağımlıya ulaşan pratik destek olarak görünmesini sağlar.","boundary":"Destek imgesidir; yardım fiilinin odak ayette bulunduğu söylenmez.","branch_ref":"root_001064/B001","carrier":"1:5'teki yardım isteme çerçevesi","distinctive_facet":"Yardım ve destek","facet_id":"SOURCE_IMAGE","independent_anchor":"A'nın practical aid statement'ı"},{"actual_contribution":"Bakımı geçindirme ve bozulmuş şeyi düzeltme hareketiyle somutlaştırır.","boundary":"Bağlam dalıdır; odak köküne غ ي ر sözlüğü yüklenmez.","branch_ref":"root_001119/B001","carrier":"A'nın provision/repair bağlamı","distinctive_facet":"Tedarik ve onarım yoluyla yarar","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9a4dbaccf30a303287f1"},{"actual_contribution":"Merhametin iyi durumu koruyan devamlı gözetim olmasını sağlar.","boundary":"Muhafaza imgesidir; target morphology çıkarımı değildir.","branch_ref":"root_001273/B004","carrier":"1:6'daki doğru yolda tutulma çerçevesi","distinctive_facet":"Koruma, gözetim ve muhafaza","facet_id":"SOURCE_IMAGE","independent_anchor":"A'nın guardianship statement'ı"},{"actual_contribution":"Bakımın alıcıda iyi durumda sabitlenen sonucunu görünür kılar.","boundary":"Sonuç facet'idir; nimet kelimesinin odak anlamı olduğu söylenmez.","branch_ref":"root_001525/B001","carrier":"1:7'deki bağışlanmış iyilik çerçevesi","distinctive_facet":"Hoş iyi durum ve bağışlanmış lütuf","facet_id":"SOURCE_IMAGE","independent_anchor":"A'nın blessing outcome statement'ı"}],"branch_refs":["root_000532/B002","root_000552/B001","root_001064/B001","root_001119/B001","root_001273/B004","root_001525/B001"],"candidate_ids":["cand_5b88b90247e67bc584ad"],"claim":"1:3'teki merhamet, 1:2'nin lordluk çerçevesi ve 1:5-1:7'nin yardım, doğru yol ve bağışlanmış iyilik sahnesiyle birlikte okunduğunda somut bakım ve tedarik emeğine açılır.","connection_refs":["conn_1c69a6b55c466048a176","conn_3420a48ccdcd3a0cd4d3","conn_05a542581545271f3a76","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-compassionate-provision"],"containment":"Komşu bağlamın etkinleştirdiği bakım imgesidir; odak sıfatlarının bütün bu dalların sözlük eşanlamı olduğu ileri sürülmez.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-compassionate-provision","mechanism":"İç yumuşaklık etkin iyiliğe dönüşür; yetiştirme, koruma, yardım, tedarik ve iyi durumda tutma facetleri bu dönüşümü aşamalı bir bakım zinciri yapar.","member_finding_refs":["macro:finding-compassionate-provision"],"proposal_keys":[],"reader_payoff":"Merhamet soyut duygu olmaktan çıkıp bağımlının yaşayabilirliğini sürdüren pratik bir iş olarak görünür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, bağımlının iyi durumda kalması için zaman içinde koruyan, yardım eden, onaran ve besleyen etkin düzen olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-compassionate-provision"}],"support_ids":["sup_0b6a58a3663ce0d84403","sup_92a1564168faaa40d410","sup_9a4dbaccf30a303287f1","sup_a3ce45741c308af66c48","sup_badc0ed91c1df4c8595a"],"title":"Merhametin bakım ve geçindirme işine dönüşmesi"},{"branch_contributions":[{"actual_contribution":"Yakınlığı sürdürmek için devamlı yetiştirme emeği sağlar.","boundary":"Bakım imgesidir; ربّ kelimesinin odak ayette yeniden okunması değildir.","branch_ref":"root_000532/B002","carrier":"1:2'deki رَبِّ bağlamı","distinctive_facet":"Onarım, yetiştirme ve tamamlanma","facet_id":"SOURCE_IMAGE","independent_anchor":"Kinship channel'ın progressive nurture statement'ı"},{"actual_contribution":"Kan bağı dışındaki edinilmiş yakınlığın da bakım sorumluluğu doğurabileceğini gösterir.","boundary":"Foster imgesidir; odak ayete literal step-parent hükmü eklemez.","branch_ref":"root_000532/B005","carrier":"Kinship channel'ın fosterage statement'ı","distinctive_facet":"Foster çocuk ve step-family ilişkisi","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_c838dec722ec4550f156"},{"actual_contribution":"Merhameti kalıcı yakınlık olarak ilişkilendirir.","boundary":"Yakınlık facet'idir; organ veya foster anlamı değildir.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Ortak soydan gelen yakın ve kalıcı ilişki","facet_id":"F001","independent_anchor":"Kinship channel'ın close-kinship statement'ı"},{"actual_contribution":"Merhametin ilişkiyi yalnızca adlandırmayıp onu tutan eylemli süreklilik taşıdığını gösterir.","boundary":"Eylemli tutum facet'idir; kalıp biçim ayrıntısı icat edilmez.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Bağı sürdürme veya koparma eylemi","facet_id":"F003","independent_anchor":"Continuing-care ve protection statements"},{"actual_contribution":"Yakınlık bağını koruyup ayakta tutan bakım mekanizması verir.","boundary":"Guardianship imgesidir; hedef kelimede morfolojik çözüm değildir.","branch_ref":"root_001273/B004","carrier":"1:6'daki sürdürme çerçevesi","distinctive_facet":"Koruma, gözetim ve muhafaza","facet_id":"SOURCE_IMAGE","independent_anchor":"Kinship channel'ın guardianship statement'ı"}],"branch_refs":["root_000532/B002","root_000532/B005","root_000552/B002","root_001273/B004"],"candidate_ids":["cand_34338f60da8afee4a1eb"],"claim":"Komşu kinship, fosterage ve continuing-care imgeleri, 1:3'teki merhameti geçici acımadan kalıcı ve sorumluluk taşıyan ilişkiye dönüştürür.","connection_refs":["conn_1c69a6b55c466048a176","conn_05a542581545271f3a76"],"contact_refs":["macro:contact-kinship-care"],"containment":"Aile ve foster imgeleri contextual activation'dır; literal soy, step-family veya hukuk kuralı değildir.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-kinship-care","mechanism":"Yakın soy bağı, foster çocuk, bakım veren ve koruma facetleri formal ilişkiyi zaman içinde yaşayan bakıma çevirir.","member_finding_refs":["macro:finding-kinship-care"],"proposal_keys":[],"reader_payoff":"Merhametin birini yalnızca acınacak nesne değil, korunması ve ilişki içinde tutulması gereken yakın olarak kurduğu görülür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, yakın soy veya edinilmiş akrabalık içinde sürdürülen bakım ve koruma sorumluluğu olarak keskinleşir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-kinship-care"}],"support_ids":["sup_0c16b3048ffd31f794c3","sup_a485a4d0f43bfd09f80f","sup_c30e01766ab7b13c05de","sup_c838dec722ec4550f156","sup_fca3b9677c041a2f83af"],"title":"Merhametin kalıcı yakınlık ve bakım bağına açılması"},{"branch_contributions":[{"actual_contribution":"Oluşumun başarıyla ortaya çıkmış fakat hâlâ yeni ve bağımlı aşamasını verir.","boundary":"Hayvan ve tazelik imgesidir; focus root'un doğrudan anlamı değildir.","branch_ref":"root_000532/B009","carrier":"B channel'ın recently delivered ewe statement'ı","distinctive_facet":"Yeni doğmuş hayvan ve tazelik","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_46b756e88e7b81d3cebe"},{"actual_contribution":"Merhameti oluşumu içeride taşıyan koruyucu alan olarak somutlaştırır.","boundary":"Sağlıklı döl yatağı facet'idir; soy bağı veya ağrı anlamı değildir.","branch_ref":"root_000552/B003","carrier":"1:3'teki ر ح م","distinctive_facet":"Yavrunun oluşup geliştiği iç kap","facet_id":"F001","independent_anchor":"B channel'ın womb-as-organ/seedbed statement'ı"},{"actual_contribution":"Oluşumun sonrasında bedensel maliyet ve kırılganlık bulunduğunu ekler.","boundary":"Döl yatağına özgü pathology facet'idir; genel acı anlamı değildir.","branch_ref":"root_000552/B004","carrier":"1:3'teki ر ح م","distinctive_facet":"Döl yatağının ağrıması veya hastalanması","facet_id":"F001","independent_anchor":"Postpartum vulnerability statement'ı"}],"branch_refs":["root_000532/B009","root_000552/B003","root_000552/B004"],"candidate_ids":["cand_9493f045c48261bf02cb"],"claim":"Gestation, recent birth ve postpartum context, 1:3'teki rḥm womb/pathology facetlerini statik sığınaktan oluşumun maliyetini üstlenen korumaya doğru daraltır.","connection_refs":["conn_1c69a6b55c466048a176"],"contact_refs":["macro:contact-gestation-postpartum"],"containment":"Keşifsel maddi analojidir; döl yatağı dalı genel beden, literal biyoloji veya odak ayetin tek anlamı yapılmaz.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-gestation-postpartum","mechanism":"Döl yatağının kap olması, yeni doğmuş koyun ve doğum sonrası ağrının ardışık imgeleri, bakımın taşıma, ortaya çıkarma ve sonrasını gözetme aşamalarını kurar.","member_finding_refs":["macro:finding-gestation-postpartum"],"proposal_keys":[],"reader_payoff":"Merhamet, yeni hayatı korurken geçişin acısını ve savunmasızlığını da taşıyan bir süreç olarak görülür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, yaşamı taşıyan koruyucu oluşum ve doğumdan sonra süren bedensel kırılganlıkla birlikte düşünülen süreç olur.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-gestation-postpartum"}],"support_ids":["sup_08349ff0361b238a7939","sup_46b756e88e7b81d3cebe","sup_74db88f266c232f1be76","sup_792005d7d142f6d2633c","sup_d69cf276554e0b01306e"],"title":"Merhametin oluşum ve doğum sonrası kırılganlıkla birlikte görünmesi"},{"branch_contributions":[{"actual_contribution":"Merhamet imgesini korunması gereken ama incinebilen canlı bedene bağlar.","boundary":"Özgül womb pathology'dir; genel merhamet karşılığı değildir.","branch_ref":"root_000552/B004","carrier":"1:3'teki ر ح م","distinctive_facet":"Döl yatağına özgü ağrı ve hastalık","facet_id":"F001","independent_anchor":"B channel'ın localized pain statement'ı"},{"actual_contribution":"Hasarın görünür bir işaret olarak okunmasını sağlar.","boundary":"Cleft imgesidir; focus word'e morfolojik anlam yüklenmez.","branch_ref":"root_001040/B004","carrier":"B channel'ın visible-lesion statement'ı","distinctive_facet":"Üst dudakta görünür yarık","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_168d9400c5af506b5bc2"},{"actual_contribution":"Lokalize bedensel baskı ve şişlik karşı-imajını ekler.","boundary":"Eye-related swelling facet'idir; öfke anlamı taşınmaz.","branch_ref":"root_001092/B006","carrier":"B channel'ın swelling statement'ı","distinctive_facet":"Göz çevresinde şişme","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_168d9400c5af506b5bc2"},{"actual_contribution":"Acının bütün bedene yayılmayıp belirli bir taşıyıcıda tutulduğunu gösterir.","boundary":"Pain source image'ıdır; focus ayetinde ağrı iddiası değildir.","branch_ref":"root_001273/B019","carrier":"B channel'ın localized pain statement'ı","distinctive_facet":"Bir organa yerleşen ağrı","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_3913fa8eb456f456e646"}],"branch_refs":["root_000552/B004","root_001040/B004","root_001092/B006","root_001273/B019"],"candidate_ids":["cand_a153169990a2c1c4d63b"],"claim":"Lesion channel, focus rḥm'nin döl yatağı hastalığı facet'iyle birleşerek merhametin pürüzsüz yumuşaklık değil, hasar ihtimali altında koruma olduğunu düşündürür.","connection_refs":["conn_05a542581545271f3a76","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-bodily-vulnerability"],"containment":"Daraltılmış exploratory counter-image'dır; odak merhameti lezyon veya hastalıkla eşitlenmez.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-bodily-vulnerability","mechanism":"Görünür yarık, göz çevresi şişliği ve lokal ağrı, döl yatağı pathology facet'ini canlı bedenin teşhis ve acı sahasına bağlar.","member_finding_refs":["macro:finding-bodily-vulnerability"],"proposal_keys":[],"reader_payoff":"Merhametin karşıtını sertlikten önce korunmaya muhtaç ve acı çeken bedende fark etmek mümkün olur.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, lezyon, şişme ve organa yerleşen ağrı karşısında korunması gereken kırılganlığı hesaba katan maliyetli bakım olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-bodily-vulnerability"}],"support_ids":["sup_0a2fb0374bdac7441218","sup_168d9400c5af506b5bc2","sup_3913fa8eb456f456e646","sup_ade4ded86699d8508f5c","sup_ae9d05391286ddec14a8"],"title":"Merhametin ağrı ve bedensel hasar karşısında sınanması"},{"branch_contributions":[{"actual_contribution":"Sosyal aktarımın sonunda kurulan bağı yakınlık olarak okutur.","boundary":"Yakınlık facet'idir; evlilik sözleşmesiyle özdeş değildir.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Yakın ve kalıcı soy ilişkisi","facet_id":"F001","independent_anchor":"Marriage channel'ın kinship statement'ı"},{"actual_contribution":"İlişkinin kurulmasını formel bir geçiş olarak çerçeveler.","boundary":"Marriage image'ıdır; focus ayetine hukuk aktarılmaz.","branch_ref":"root_001444/B004","carrier":"Marriage channel'ın contract statement'ı","distinctive_facet":"Evlilik sözleşmesi","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_de7d9718c9ea56199acc"},{"actual_contribution":"İlişki kurucu aktarımın şefkatli jest boyutunu verir.","boundary":"Gift imgesidir; reciprocal obligation kurulmaz.","branch_ref":"root_001583/B004","carrier":"Marriage channel'ın affectionate gift statement'ı","distinctive_facet":"Yakına gönderilen lütuf hediyesi","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_de7d9718c9ea56199acc"},{"actual_contribution":"Yakınlığın yeni bir hane ve ilişki alanına geçişini görünür kılar.","boundary":"Conveyance imgesidir; focus ayetinde literal gelin yoktur.","branch_ref":"root_001583/B006","carrier":"Marriage channel'ın bride-conveyance statement'ı","distinctive_facet":"Gelinin eşine götürülmesi","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_de7d9718c9ea56199acc"}],"branch_refs":["root_000552/B002","root_001444/B004","root_001583/B004","root_001583/B006"],"candidate_ids":["cand_f15b548d35c708feeb81"],"claim":"Marriage and bride-conveyance context, rḥm yakınlık facetini sözleşme, hediye ve bir haneye götürülme imgeleriyle ilişki kuran geçişe açar.","connection_refs":["conn_146cb43f16e8ce98ae2d","conn_05a542581545271f3a76"],"contact_refs":["macro:contact-marriage-conveyance"],"containment":"Keşifsel sosyal analojidir; marriage, ownership veya conveyance odak ayete hukuki hüküm olarak aktarılmaz.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-marriage-conveyance","mechanism":"Yakınlık, evlilik sözleşmesi, yakına gönderilen hediye ve gelinin eşine götürülmesi sosyal ilişkinin kurulma ve taşınma aşamalarını sağlar.","member_finding_refs":["macro:finding-marriage-conveyance"],"proposal_keys":[],"reader_payoff":"Merhametin yaşam düzenini değiştiren, tarafları birbirine bağlayan bir hareket olabileceği görülür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, bir bağı kuran, tarafları yeni bir ilişki alanına taşıyan ve yakınlık içinde hediyeleşen aktarım hareketi olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-marriage-conveyance"}],"support_ids":["sup_6680b39df3eabd0fb288","sup_8dd6db431a8f7aa0a5c1","sup_95abda0eb57d0d0b8d16","sup_de7d9718c9ea56199acc","sup_e2afbf0a30dc60a45f40"],"title":"Merhametin ilişki kuran sosyal aktarım olarak görünmesi"},{"branch_contributions":[{"actual_contribution":"Merhametin yardım talebine cevap veren iyilik olarak çalışmasını sağlar.","boundary":"Active beneficence facet'idir; yardım kelimesiyle aynılaştırılmaz.","branch_ref":"root_000552/B001","carrier":"1:3'teki merhamet çifti","distinctive_facet":"Esirgeme ve iyiliğe etkin sonuç","facet_id":"F002","independent_anchor":"Petition channel'ın benefaction statement'ı"},{"actual_contribution":"Merhamet bağının karşılık üreten, fakat asimetrik ilişki olarak okunmasını sağlar.","boundary":"Karşılıklılık imgesidir; tarafların eşitliği değildir.","branch_ref":"root_000552/B001","carrier":"1:5'teki hizmet ve yardım talebi","distinctive_facet":"Karşılıklı kuruluş","facet_id":"F003","independent_anchor":"Petition channel'ın request-response statement'ı"},{"actual_contribution":"Merhameti yalnızca sahip olunan nitelik değil, talep edilen ilişki alanı yapar.","boundary":"Söz eylemi facet'idir; target grammar icat edilmez.","branch_ref":"root_000552/B001","carrier":"1:5-1:6'daki doğrudan talep","distinctive_facet":"Merhamete erişmeyi dileme söz eylemi","facet_id":"F004","independent_anchor":"Petition channel'ın petition statement'ı"},{"actual_contribution":"Yardımın yalnızca rahatlatma değil, yönlendirilmiş bir varış taşıdığını gösterir.","boundary":"Path image'ıdır; merhamet kelimesinin yol anlamı değildir.","branch_ref":"root_000858/B001","carrier":"1:6-1:7'deki yol dizisi","distinctive_facet":"Doğru yol","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d4bed164651e2e21ccf"},{"actual_contribution":"Bağımlının açıkça talep edebildiği pratik cevap hareketini verir.","boundary":"Aid image'ıdır; odak ayetinde ayrı bir yardım fiili yoktur.","branch_ref":"root_001064/B001","carrier":"1:5'teki yardım isteme","distinctive_facet":"Yardım ve destek","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d4bed164651e2e21ccf"},{"actual_contribution":"Yardımın hedefini dengeli ve doğru bir yaşam durumu olarak belirler.","boundary":"Uprightness image'ıdır; target morphology supplied değildir.","branch_ref":"root_001273/B008","carrier":"1:6'daki المستقيم için supplied context","distinctive_facet":"Doğruluk ve diklik","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d4bed164651e2e21ccf"},{"actual_contribution":"Merhametin talebe yol gösteren cevap biçimini verir.","boundary":"Guidance image'ıdır; lexical identity odak köküne taşınmaz.","branch_ref":"root_001583/B001","carrier":"1:6'daki rehberlik talebi","distinctive_facet":"Nazik rehberlik","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d4bed164651e2e21ccf"}],"branch_refs":["root_000552/B001","root_000858/B001","root_001064/B001","root_001273/B008","root_001583/B001"],"candidate_ids":["cand_a28000043e01afdbe93d"],"claim":"1:5'teki ibadet ve yardım isteme ile 1:6'daki rehberlik talebi, 1:3 merhametini salt ihsan değil, talebe cevap veren ve doğru yola yönelten ilişki yapar.","connection_refs":["conn_3420a48ccdcd3a0cd4d3","conn_05a542581545271f3a76","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-petition-aid"],"containment":"Karşılıklılık eşitlik anlamında değildir; prayer and guidance context odak kökünün lexical gloss'u yapılmadan kullanılır.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-petition-aid","mechanism":"Etkin iyilik, yardım, rehberlik, yol ve doğruluk facetleri doğrudan hitap içindeki request-response hareketinde birleşir.","member_finding_refs":["macro:finding-petition-aid"],"proposal_keys":[],"reader_payoff":"Okur merhameti alıcıyı pasifleştiren bir iyilik değil, onun hizmet edip yardım isteyebildiği canlı bağ olarak görür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, hizmet eden ve yardım isteyen bağımlının yön, yol ve doğruluk talebine cevap veren asimetrik ilişki olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-petition-aid"}],"support_ids":["sup_3c847633d3a35d55128d","sup_6e9f76a8691310275aad","sup_9d4bed164651e2e21ccf","sup_d0188fb732bba5681532","sup_f9f2f1abea78531af803"],"title":"Merhametin yardım isteyen bağımlıya yön veren ilişki olması"},{"branch_contributions":[{"actual_contribution":"Aktarımın merhametten doğan etkin iyilik olduğunu belirler.","boundary":"Benefaction facet'idir; gift kelimesinin odak anlamı değildir.","branch_ref":"root_000552/B001","carrier":"1:3'teki merhamet çifti","distinctive_facet":"Acımanın etkin iyiliği","facet_id":"F002","independent_anchor":"Gift channel'ın benefaction statement'ı"},{"actual_contribution":"İyiliğin alıcıya geçerek onun elinde sonuçlanması için aktarım ekseni verir.","boundary":"Ownership image'ıdır; focus ayetinde mülkiyet hükmü değildir.","branch_ref":"root_001444/B002","carrier":"1:4'teki sahiplik çerçevesi","distinctive_facet":"Sahiplik ve tasarruf","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d8a20e8685ebe54855a"},{"actual_contribution":"Aktarımın hedefindeki alıcı yararını görünür kılar.","boundary":"Outcome image'ıdır; odak sıfatlarının doğrudan nimet anlamı değildir.","branch_ref":"root_001525/B001","carrier":"1:7'deki bağışlanmış iyi durum","distinctive_facet":"Hoş iyi durum ve bağış","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d8a20e8685ebe54855a"},{"actual_contribution":"Merhametin sosyal motivasyonunu sevilen alıcıya yönelen jest olarak verir.","boundary":"Gift image'ıdır; reciprocal exchange zorunluluğu yoktur.","branch_ref":"root_001583/B004","carrier":"Gift channel'ın affectionate transfer statement'ı","distinctive_facet":"Yakına gönderilen şefkatli hediye","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_9d8a20e8685ebe54855a"}],"branch_refs":["root_000552/B001","root_001444/B002","root_001525/B001","root_001583/B004"],"candidate_ids":["cand_283ae4ce88fbadd5fabe"],"claim":"Gift, ownership, benefit ve affectionate transfer context'i, 1:3 merhametini alıcıya ulaşan ve onda iyi durum oluşturan sosyal ihsan olarak etkinleştirir.","connection_refs":["conn_146cb43f16e8ce98ae2d","conn_05a542581545271f3a76","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-beneficent-transfer"],"containment":"Aktarım analojisi korunur; hukukî sahiplik veya karşılık zorunluluğu focus reading yapılmaz.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-beneficent-transfer","mechanism":"Etkin merhamet, yakına gönderilen hediye, mülkiyete geçiş ve hoş iyi durum facetleriyle motive, nesne ve sonuç sırasını kazanır.","member_finding_refs":["macro:finding-beneficent-transfer"],"proposal_keys":[],"reader_payoff":"Merhametin değerini, alıcının yaşamında meydana getirdiği ulaşılabilir sonuçta görmek mümkün olur.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, verenin içinde kalan tutum değil, hediye ve yarar olarak başka birinin durumuna geçen aktarım olur.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-beneficent-transfer"}],"support_ids":["sup_0ac065c59d768eca536c","sup_1271a83061eedcf7f13e","sup_1502eb0ec3fee382bd9e","sup_6475c2dae1eb4ee46954","sup_9d8a20e8685ebe54855a"],"title":"Merhametin alıcıya ulaşan ihsan olması"},{"branch_contributions":[{"actual_contribution":"Enclosure'dan çıkmış, yeni ve hâlâ korunmaya muhtaç canlıyı verir.","boundary":"Animal/freshness image'ıdır; literal odak anlamı değildir.","branch_ref":"root_000532/B009","carrier":"C'nin recently delivered ewe statement'ı","distinctive_facet":"Yeni doğmuş hayvan ve tazelik","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_09ee6a9bd52ee1774afb"},{"actual_contribution":"Açık alana çıkışın öncesindeki koruyucu oluşum alanını sağlar.","boundary":"Womb organ facet'idir; kinship veya pain değildir.","branch_ref":"root_000552/B003","carrier":"1:3'teki ر ح م","distinctive_facet":"Üreme ve oluşum kabı","facet_id":"F001","independent_anchor":"C'nin womb-as-generative-vessel statement'ı"},{"actual_contribution":"Enclosure sonrasında sahip ve koruma kaybı riskini somutlaştırır.","boundary":"Stray animal image'ıdır; dalın focus word anlamı değildir.","branch_ref":"root_000913/B005","carrier":"C'nin stray statement'ı","distinctive_facet":"Issız yerde sahipsiz hayvan","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_09ee6a9bd52ee1774afb"},{"actual_contribution":"Dışarıdaki yaşamın avcı baskısı altında olduğunu gösterir.","boundary":"Raptor image'ıdır; focus ayette hayvan adı aranmaz.","branch_ref":"root_001040/B006","carrier":"C'nin open-field predator statement'ı","distinctive_facet":"Raptor","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_09ee6a9bd52ee1774afb"},{"actual_contribution":"Exposure sahnesindeki yırtıcı çeşitliliğini tamamlar.","boundary":"Hyena image'ıdır; lexical equation değildir.","branch_ref":"root_001040/B007","carrier":"C'nin predator-class statement'ı","distinctive_facet":"Erkek sırtlan","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_09ee6a9bd52ee1774afb"},{"actual_contribution":"Koruyucu kap dışındaki geniş ve sınıflanmış canlı alanını verir.","boundary":"Bird image'ıdır; focus mercy'ye hayvan anlamı eklemez.","branch_ref":"root_001525/B006","carrier":"C'nin open-field bird statement'ı","distinctive_facet":"Ostrich ve açık alan kuşu","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_09ee6a9bd52ee1774afb"}],"branch_refs":["root_000532/B009","root_000552/B003","root_000913/B005","root_001040/B006","root_001040/B007","root_001525/B006"],"candidate_ids":["cand_383ee35cdc1c7e377a1a"],"claim":"Wildlife context, focus womb facetini yakın korumadan açık alanda savunmasız kalmaya geçişle sınar ve merhametin koruma sınırını görünür kılar.","connection_refs":["conn_1c69a6b55c466048a176","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-wildlife-exposure"],"containment":"Keşifsel hayvan karşı-imajıdır; zoolojik anlam veya dalların odak sıfatlarının sözlük karşılığı yapılmaz.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-wildlife-exposure","mechanism":"Yeni doğum ve döl yatağı, ostrich, raptor, hyena ve sahipsiz hayvan imgeleriyle enclosure-to-exposure dizisine bağlanır.","member_finding_refs":["macro:finding-wildlife-exposure"],"proposal_keys":[],"reader_payoff":"Merhametin yalnızca hayatı başlatmak değil, hayatın dışarı çıktığında kaybolmaması ve tutulması sorununu da taşıdığı görülür.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, canlıyı oluşturan kapalı koruma ile onun dışarı çıktıktan sonra kaybolma ve yırtıcılarla karşılaşma riskini aynı sahnede görünür kılar.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-wildlife-exposure"}],"support_ids":["sup_04ad32c8de2cd90457eb","sup_09ee6a9bd52ee1774afb","sup_0c06b90004769a6afa1f","sup_5d9b73f828a78ff3b650","sup_9c79f5c6153cc7c49ace"],"title":"Merhametin koruyucu oluşumdan açık dünyadaki exposure'a uzanması"},{"branch_contributions":[{"actual_contribution":"Gelişimsel sürecin iç oluşum alanını verir.","boundary":"Healthy womb facet'idir; maturity'nin kendisi değildir.","branch_ref":"root_000552/B003","carrier":"1:3'teki ر ح م","distinctive_facet":"Yavrunun oluşup geliştiği kap","facet_id":"F001","independent_anchor":"D'nin reproductive-capacity statement'ı"},{"actual_contribution":"Olgunlaşmanın dışarıdan okunabilir olmasını sağlar.","boundary":"Mark image'ıdır; mercy'nin etimolojisi değildir.","branch_ref":"root_001040/B002","carrier":"D'nin bodily-mark statement'ı","distinctive_facet":"Ayırt edici görünür işaret","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_4ed5dd498ada03082146"},{"actual_contribution":"Gelişimi tek an değil, yaş içinde yerleşen ara süreç olarak gösterir.","boundary":"Middle-age image'ıdır; focus ayetinde yaş iddiası yoktur.","branch_ref":"root_001064/B002","carrier":"D'nin life-stage statement'ı","distinctive_facet":"İki yaş arasındaki orta dönem","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_4ed5dd498ada03082146"},{"actual_contribution":"Bakımın hedefindeki dengeli ve dayanıklı durumu verir.","boundary":"Strength image'ıdır; odak merhametinin kuvvet anlamı değildir.","branch_ref":"root_001064/B005","carrier":"D'nin mature-strength statement'ı","distinctive_facet":"Yerleşmiş yapı ve yetişmiş güç","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_4ed5dd498ada03082146"},{"actual_contribution":"Yaşam evresinin bedende görünür bir belirtiyle işaretlenmesini sağlar.","boundary":"Pubis-hair image'ıdır; focus reading'e biyoloji yüklenmez.","branch_ref":"root_001064/B007","carrier":"D'nin visible-marker statement'ı","distinctive_facet":"Bedensel kıl işareti","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_4ed5dd498ada03082146"}],"branch_refs":["root_000552/B003","root_001040/B002","root_001064/B002","root_001064/B005","root_001064/B007"],"candidate_ids":["cand_08a44d9fc1f1fba015e7"],"claim":"Bodily-markers context, rḥm womb facetini biçim, işlev ve yaş üzerinden izlenebilen oluşum ve olgunlaşma sürecine bağlar.","connection_refs":["conn_1c69a6b55c466048a176","conn_3420a48ccdcd3a0cd4d3"],"contact_refs":["macro:contact-maturity-markers"],"containment":"Keşifsel development image'dır; odak sıfatları biyolojik terim veya sınıflandırma etiketi değildir.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-maturity-markers","mechanism":"Womb, distinguishing mark, middle age, settled build and pubic-hair facetleri, gelişimi görünür ve sınıflanabilir bir yaşam evresi olarak kurar.","member_finding_refs":["macro:finding-maturity-markers"],"proposal_keys":[],"reader_payoff":"Bakımın sonucunu, bağımlının zaman içinde olgunlaşıp kendi durumu okunabilir hale gelmesinde izlemek mümkün olur.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, yaşamı üreten ve onu görünür işaretlerle ayırt edilebilir, orta yaşa ulaşmış ve dengeli güçlü bir duruma getiren gelişim süreci olarak okunur.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-maturity-markers"}],"support_ids":["sup_4ed5dd498ada03082146","sup_5702158d961a910169cd","sup_733f128f0d80cd20182d","sup_958596083ea6172e9a22","sup_e6f47a8718362ba7cc4c"],"title":"Merhametin gelişim ve okunabilir olgunluk süreci olması"},{"branch_contributions":[{"actual_contribution":"Savunulan çevrenin neden yakınlıkla kurulduğunu verir.","boundary":"Kinship facet'idir; jealousy anlamı değildir.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Yakın ve kalıcı ilişki","facet_id":"F001","independent_anchor":"E'nin protected-circle statement'ı"},{"actual_contribution":"Koruyucu sınırın bedensel kapasitesini verir.","boundary":"Strength image'ıdır; worship branch'i değildir.","branch_ref":"root_000973/B007","carrier":"E'nin bodily-firmness statement'ı","distinctive_facet":"Güç ve sağlamlık","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_cf440c927cdd0f701434"},{"actual_contribution":"Dışarıya yönelen savunucu sertliği görünür kılar.","boundary":"Irritability image'ıdır; merhamete doğrudan anlam yapılmaz.","branch_ref":"root_001092/B007","carrier":"E'nin frown/anger statement'ı","distinctive_facet":"Surly ve irritabl yaratık","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_cf440c927cdd0f701434"},{"actual_contribution":"Yakın çevrenin ihlal edilmesine karşı seçici sınır kurar.","boundary":"Protective-jealousy image'ıdır; merhametle eşanlamlı değildir.","branch_ref":"root_001119/B004","carrier":"E'nin threatened-boundary statement'ı","distinctive_facet":"Aileye yönelik koruyucu kıskançlık","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_cf440c927cdd0f701434"},{"actual_contribution":"Korumanın bireyden topluluğa genişleyen sosyal alanını verir.","boundary":"Group image'ıdır; target morphology çıkarımı değildir.","branch_ref":"root_001273/B001","carrier":"E'nin protected-group statement'ı","distinctive_facet":"İnsanlar/topluluk grubu","facet_id":"SOURCE_IMAGE","independent_anchor":"sup_cf440c927cdd0f701434"}],"branch_refs":["root_000552/B002","root_000973/B007","root_001092/B007","root_001119/B004","root_001273/B001"],"candidate_ids":["cand_78a8987e305928719aaf"],"claim":"Protective-jealousy context, rḥm yakınlık facetini yumuşaklığın karşısına değil, yumuşaklığın koruduğu çevreyi savunan seçici bir kuvvete taşır.","connection_refs":["conn_3420a48ccdcd3a0cd4d3","conn_05a542581545271f3a76","conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-household-defense"],"containment":"Savunma ve öfke karşı-imajdır; merhamet öfke, kıskançlık veya sertlikle eşanlamlı yapılmaz.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-household-defense","mechanism":"Yakınlık, topluluk, bedensel sağlamlık, koruyucu kıskançlık ve kaş çatma imgeleri içeride bakım, dışarıda direnç dizisi kurar.","member_finding_refs":["macro:finding-household-defense"],"proposal_keys":[],"reader_payoff":"Merhametin sınırsız gevşeklik değil, koruduğu kişileri olduğu için sınır çizen bakım olduğunu görmek mümkün olur.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, bağlı olunan çevreyi içeriden koruyan ve dışarıdan gelen ihlale karşı sınır ve savunma kapasitesi oluşturan bağ olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-household-defense"}],"support_ids":["sup_5b1a4e5380d4ee99f54b","sup_5dffcebbf5e2e9068992","sup_b0db5747f99cb89dba16","sup_cf440c927cdd0f701434","sup_f74563a0a9b410bc19d2"],"title":"Merhametin korunan çevre ve savunma sınırı kurması"},{"branch_contributions":[{"actual_contribution":"Merhamet içeriğini adı anılan ilahî varlığa yaklaşmanın tanınabilir eşiği olarak çerçeveler.","boundary":"Divine-use facet'inin contextual activation'ıdır; name branch'i lexical olarak doğrulanmaz.","branch_ref":"root_000552/B001","carrier":"1:3'teki ilahî merhamet çifti","distinctive_facet":"Tanrı hakkında kullanıldığında merhametin genişliği ve yaratılmışlara ulaşması","facet_id":"F005","independent_anchor":"1:1'deki adlandırma ve exact repetition"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_003064899e643c5d38b5"],"claim":"1:1 ve 1:3'teki aynı merhamet çifti, sıfatların yalnızca niteleme değil, adlandırılmış ilahî varlığa merhamet üzerinden yaklaşmayı açan tekrar olduğunu önerebilir.","connection_refs":["conn_cffcad30e81c6cd03957"],"contact_refs":["macro:contact-name-disclosure"],"containment":"HFT raw payload'daki medium confidence ve legacy-unbound qualification korunur; kayıtlı olmayan name/mark dalları dropped, bu nedenle bulgu etimoloji değil contextual activation'dır.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-name-disclosure","mechanism":"Adlandırma kuruluşu, focus pair'in exact recurrence'ı ve direct invocation relation'ı merhameti betimlemeden erişim işlevine taşır.","member_finding_refs":["macro:finding-name-disclosure"],"proposal_keys":[],"reader_payoff":"Okur merhamet adlarının kimliği açıklayan ve hitabı mümkün kılan bir kapı olarak işleyebileceğini fark eder.","referral_payloads":[],"scope_movements":[{"context_after":"1:1'deki adlandırma kuruluşu ve tam tekrar, merhamet çiftini adı anılan varlığa yaklaşmanın çağrılmış eşiği olarak görmeyi mümkün kılar.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-name-disclosure"}],"support_ids":["sup_d5abba186182302551bb"],"title":"Tekrarın merhameti adlandırılmış erişim eşiği yapması"},{"branch_contributions":[{"actual_contribution":"Kozmik nurturing claim için oluşum ve korunma modelini sağlar.","boundary":"Womb analogy'dir; bütün cosmology'nin lexical temeli değildir.","branch_ref":"root_000552/B003","carrier":"1:3'teki ر ح م","distinctive_facet":"Koruyucu oluşum kabı","facet_id":"F001","independent_anchor":"HFT payload'ındaki womb-as-matrix role"},{"actual_contribution":"Oluşum modeline aşamalı yönetim ve tamamlanma yönü ekler.","boundary":"Registered repair/nurture image'ıdır; unresolved praise/growth branches yerine geçmez.","branch_ref":"root_000532/B002","carrier":"1:2'deki رَبِّ ve worlds frame","distinctive_facet":"Onarım, yetiştirme ve tamamlanma","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT payload'ındaki repair/upbringing/completion role"}],"branch_refs":["root_000552/B003","root_000532/B002"],"candidate_ids":["cand_b390918e7f1298c4c4c4"],"claim":"Odak döl yatağı facet'i, 1:2'deki lordluk ve praise context'iyle birleşince tekil sığınaktan çoklu alanları oluşturan nurturing rule imgesine açılır.","connection_refs":["conn_1c69a6b55c466048a176"],"contact_refs":["macro:contact-nurturing-rule"],"containment":"HFT medium ve legacy-unbound provenance korunmuştur; üç facet'siz HFT branch finding'e alınmamıştır, bu nedenle kozmolojik claim exploratory'dir.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-nurturing-rule","mechanism":"Koruyucu oluşum, onarım-yetiştirme-tamamlama ve çoğul âlemler arasında gelişim yönü kurulur.","member_finding_refs":["macro:finding-nurturing-rule"],"proposal_keys":[],"reader_payoff":"Merhamet hazır bir sonuç değil, dünyaları oluşmuş ve övgüye değer hale getiren sürekli yönetim olarak görülebilir.","referral_payloads":[],"scope_movements":[{"context_after":"1:2'nin hemen önceki lordluk ve çoğul âlemler çerçevesinde merhamet, bağımlı varlık alanlarını besleyip onarımla tamamlayan kozmolojik gelişim emeği olarak genişler.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-nurturing-rule"}],"support_ids":["sup_4187ef5005ba2a115156"],"title":"Merhametin kozmolojik yetiştirme emeği olması"},{"branch_contributions":[{"actual_contribution":"Hesap sahnesinin nasıl tutulduğuna dair olumlu yönetici tarz sağlar.","boundary":"Disposition activation'ıdır; mercy'nin leniency veya judgment ile özdeşliği değildir.","branch_ref":"root_000552/B001","carrier":"1:3'teki merhamet çifti","distinctive_facet":"Merhametin etkin iyiliği","facet_id":"F002","independent_anchor":"1:4'teki following accountability frame"},{"actual_contribution":"Hesaplamanın bir idare ve tasarruf sahibi tarafından tutulduğu çerçeveyi verir.","boundary":"Ownership image'ıdır; target morphology supplied değildir.","branch_ref":"root_001444/B002","carrier":"1:4 supplied exact Arabic","distinctive_facet":"Sahiplik ve tasarruf","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT ownership/disposal role"}],"branch_refs":["root_000552/B001","root_001444/B002"],"candidate_ids":["cand_d93273b590a8f5ba2db7"],"claim":"Merhamet çifti, hemen sonraki hesap çerçevesiyle birlikte okunduğunda yargıyı silmeyen, onun idare edilme tarzını belirleyen öncül disposition olur.","connection_refs":["conn_146cb43f16e8ce98ae2d"],"contact_refs":["macro:contact-accounting-frame"],"containment":"HFT exact target Arabic yalnızca surface contact sağlar; target morphology ve hukukî doktrin çıkarılmamıştır. Unresolved accounting/time branches dışarıdadır.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-accounting-frame","mechanism":"Odak merhameti, 1:4'teki ownership/disposal facet'iyle birleşerek bounded accountability context'ini yönetir.","member_finding_refs":["macro:finding-accounting-frame"],"proposal_keys":[],"reader_payoff":"Merhamet ve hesap arasındaki gerilim, birinin diğerini yok etmesi yerine hesap verme tarzının belirlenmesi olarak okunur.","referral_payloads":[],"scope_movements":[{"context_after":"1:4'ün sahiplik ve hesap verme sahnesi, merhameti yargının karşıtı değil, hesabın nasıl tutulduğunu önceleyen idare edici nitelik olarak gösterir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-accounting-frame"}],"support_ids":["sup_c7425ce963b46a526fed"],"title":"Merhametin hesap sahnesini çerçeveleyen yönetici tutum olması"},{"branch_contributions":[{"actual_contribution":"Merhameti hizmet ve yardım talebiyle işleyen devamlı bağa çevirir.","boundary":"Relational action facet'idir; worship anlamı değildir.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Bağı sürdürme veya koparma eylemi","facet_id":"F003","independent_anchor":"HFT maintained-kinship role ve 1:5 response frame"},{"actual_contribution":"Bağımlının talebine cevap veren etkin destek hareketini sağlar.","boundary":"Aid image'ıdır; odak ayette ayrı lexical gloss olarak sunulmaz.","branch_ref":"root_001064/B001","carrier":"1:5 supplied exact Arabic","distinctive_facet":"Yardım ve destek","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT assistance role"}],"branch_refs":["root_000552/B002","root_001064/B001"],"candidate_ids":["cand_5f45719f597ab4cd1c17"],"claim":"Yakınlık facet'i ile 1:5'in ibadet ve yardım hareketi birleşerek merhameti pasif alıcıya tek yönlü iyilik olmaktan çıkarır.","connection_refs":["conn_3420a48ccdcd3a0cd4d3"],"contact_refs":["macro:contact-dependent-service"],"containment":"HFT medium, legacy-unbound nomination; worship branch'i kayıtlı facet olmadığı için çıkarılmış, target morphology icat edilmemiştir.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-dependent-service","mechanism":"Sürdürülen bağ hizmeti cevap olarak, yardım istemeyi de bağımlılığın açık ifadesi olarak yerleştirir.","member_finding_refs":["macro:finding-dependent-service"],"proposal_keys":[],"reader_payoff":"Okur merhametin karşılık bekleyen eşit değişim değil, cevap ve talep üreten asimetrik yakınlık olduğunu görür.","referral_payloads":[],"scope_movements":[{"context_after":"1:5'teki hizmet ve yardım isteme, merhameti bağımlının cevap verip yardım talep ettiği asimetrik ilişki olarak görünür kılar.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-dependent-service"}],"support_ids":["sup_15feb6ca8f1c877fea0b"],"title":"Merhametin hizmet ve yardım talebine cevap alanı açması"},{"branch_contributions":[{"actual_contribution":"Yönlendirmenin şefkatli ve koruyucu tarzını verir.","boundary":"Mercy action facet'idir; guidance kelimesi değildir.","branch_ref":"root_000552/B001","carrier":"1:3'teki merhamet çifti","distinctive_facet":"Etkin esirgeme ve iyilik","facet_id":"F002","independent_anchor":"HFT gentle-care role"},{"actual_contribution":"Yönün üzerinde yaşanabilir bir süreklilik alanı sağlar.","boundary":"Road image'ıdır; mercy'nin path anlamı değildir.","branch_ref":"root_000858/B001","carrier":"1:6 supplied exact Arabic","distinctive_facet":"Doğru yol","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT traversable-road role"},{"actual_contribution":"Yolcunun seyir boyunca tutulmasını ve korunmasını sağlar.","boundary":"Care image'ıdır; target morphology supplied değildir.","branch_ref":"root_001273/B004","carrier":"1:6 supplied exact Arabic","distinctive_facet":"Koruma ve muhafaza","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT guardianship role"},{"actual_contribution":"Sürdürülen yönün yalnız hareket değil, dengeli durum olduğunu belirler.","boundary":"Uprightness image'ıdır; odak kökünün literal anlamı değildir.","branch_ref":"root_001273/B008","carrier":"1:6 supplied exact Arabic","distinctive_facet":"Diklik ve dengelilik","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT upright-alignment role"},{"actual_contribution":"Merhametin yön gösteren işlemini doğrudan sağlar.","boundary":"Guidance image'ıdır; target morphology çıkarımı değildir.","branch_ref":"root_001583/B001","carrier":"1:6 supplied exact Arabic","distinctive_facet":"Nazik rehberlik","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT guidance role"}],"branch_refs":["root_000552/B001","root_000858/B001","root_001273/B004","root_001273/B008","root_001583/B001"],"candidate_ids":["cand_e2c66f9808c72c10c0da"],"claim":"Merhamet, 1:6'daki rehberlik, yol, koruma ve doğruluk facetleriyle birlikte okunduğunda hem istikamet gösteren hem de seyri sürdüren bir bakım düzenidir.","connection_refs":["conn_05a542581545271f3a76"],"contact_refs":["macro:contact-guides-maintains"],"containment":"HFT strong confidence atfı taşımakla birlikte source qualifications korunmuş, hedef morfolojisi çıkarılmamış ve finding contextual activation olarak tutulmuştur.","epistemic_status":"medium","lane":"macro","locked_finding_ref":"locked:macro:finding-guides-maintains","mechanism":"Gentle guidance path'i gösterir; care/preservation ve uprightness facetleri yolcuyu ve yolu çökmeden tutar.","member_finding_refs":["macro:finding-guides-maintains"],"proposal_keys":[],"reader_payoff":"Okur merhametin yalnızca nereye gidileceğini söylemediğini, oraya giderken ayakta kalmayı da mümkün kıldığını görür.","referral_payloads":[],"scope_movements":[{"context_after":"1:6'nın yol ve doğruluk talebiyle merhamet, yön gösteren ve yolcuyu dengede tutan sürekli altyapı olarak görünür.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-guides-maintains"}],"support_ids":["sup_7b77ad317da0460b83a0"],"title":"Merhametin yönlendiren ve yolda tutan altyapı olması"},{"branch_contributions":[{"actual_contribution":"Merhametin sertleşme ve kaybolma karşısındaki olumlu hassasiyetini verir.","boundary":"Tenderness activation'ıdır; unresolved hardness/loss branches yerine geçmez.","branch_ref":"root_000552/B001","carrier":"1:3'teki merhamet çifti","distinctive_facet":"İç yumuşaklık ve şefkat","facet_id":"F001","independent_anchor":"1:7'nin supplied positive/negative path contrast'ı"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_e5dfa31680dd1fbb7937"],"claim":"1:7'nin supplied contrast'ı, merhametin yalnızca olumlu nitelik olmadığını; yönlendirilebilirliği ve tutulabilirliği koruyan karşıt-sonuç önleyici bir kuvvet olduğunu düşündürür.","connection_refs":["conn_195e867089f8a8d93226"],"contact_refs":["macro:contact-softens-loss"],"containment":"HFT medium ve legacy-unbound kaynaklı exploratory narrowing'dir; kayıtlı olmayan dört context branch'i finding branch listesine alınmamıştır.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-softens-loss","mechanism":"Olumlu iyi durum ile dışlama, sertlik ve kaybolma rollerinin yan yana gelişi merhametin outcome field'ini tanımlar.","member_finding_refs":["macro:finding-softens-loss"],"proposal_keys":[],"reader_payoff":"Okur merhametin neye karşı çalıştığını ve canlıyı nasıl yumuşak, görünür ve yolda tuttuğunu görebilir.","referral_payloads":[],"scope_movements":[{"context_after":"1:7'deki bağış ve dışlanan sonuçlar, merhameti yumuşaklığı koruyan, sertleşme ve yolunu kaybetmeye karşı tutan ortam olarak gösterir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-softens-loss"}],"support_ids":["sup_1fa463d9d97262620ced"],"title":"Merhametin sertleşme ve kaybolma karşısında tutması"},{"branch_contributions":[{"actual_contribution":"Merhamet içeriğini ilahî eylemde tanınabilir kılan context frame'i sağlar.","boundary":"Divine-use facet'inin activation'ıdır; mark branch'i bağımsız doğrulanmamıştır.","branch_ref":"root_000552/B001","carrier":"1:3'teki ٱلرَّحْمَٰنِ / ٱلرَّحِيمِ","distinctive_facet":"İlahî kullanımda geniş merhamet","facet_id":"F005","independent_anchor":"1:1 name construction ve complete repetition"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_55e092bfe3d85d6e3717"],"claim":"Odak çiftinin exact recurrence'ı, merhamet içeriğinin aksi halde belirsiz eylemlerde tanınabilir bir trace olarak görünmesi ihtimalini açar.","connection_refs":["conn_cffcad30e81c6cd03957"],"contact_refs":["macro:contact-visible-mark"],"containment":"HFT exploratory outlier'dır; non-dominant split mapping ve kayıtlı olmayan mark branch'i nedeniyle etimoloji veya lexical gloss değildir.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-visible-mark","mechanism":"Adlandırma ve tekrar, nitelik ile tanınabilir iz arasında form-distant bir activation kurar.","member_finding_refs":["macro:finding-visible-mark"],"proposal_keys":[],"reader_payoff":"Okur merhameti yalnızca söylenen bir nitelik değil, eylemlerde aranıp fark edilebilen bir belirti gibi düşünebilir.","referral_payloads":[],"scope_movements":[{"context_after":"1:1'deki adlandırma ve tekrar, merhametin eylem ve ilişkilerde tanınabilir bir ilahî imza olarak okunmasını önerebilir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-visible-mark"}],"support_ids":["sup_19ec4bc3c090ebb82827"],"title":"Merhametin tanınabilir bir iz olarak görünmesi"},{"branch_contributions":[{"actual_contribution":"Hesapta önem kazanabilecek kalıcı ilişkisel bağ modelini verir.","boundary":"Kinship analogy'sidir; debt branch'i veya hukukî yükümlülük değildir.","branch_ref":"root_000552/B002","carrier":"1:3'teki ر ح م","distinctive_facet":"Yakın ve kalıcı soy ilişkisi","facet_id":"F001","independent_anchor":"1:4'ün supplied accounting frame"}],"branch_refs":["root_000552/B002"],"candidate_ids":["cand_f7c3470e5afab564dec4"],"claim":"Rḥm yakınlık facet'i ile 1:4'ün supplied accountability context'i, merhameti iz bırakmayan gönüllü yarardan ilişkisel sonuç taşıyan bağa doğru daraltır.","connection_refs":["conn_146cb43f16e8ce98ae2d"],"contact_refs":["macro:contact-ledger-kinship"],"containment":"HFT exploratory cross-domain analogy'dir; unresolved financial-debt branch çıkarılmış, hukukî borç doktrini ve target morphology kurulmamıştır.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-ledger-kinship","mechanism":"Yakın ve sürdürülebilir ilişki, hesap ve idare sahnesine girerek bağın korunması/kopmasının önemini görünür kılar.","member_finding_refs":["macro:finding-ledger-kinship"],"proposal_keys":[],"reader_payoff":"Okur merhametin ilişki kurduğu yerde bir sorumluluk ve devamlılık iddiası ürettiğini düşünebilir.","referral_payloads":[],"scope_movements":[{"context_after":"1:4'ün hesap çerçevesinde merhamet, korunması veya kopması sonuç doğurabilecek yakınlık benzeri kalıcı bir bağ olarak okunabilir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-ledger-kinship"}],"support_ids":["sup_abd42bc7c3c1a704516a"],"title":"Merhametin hesapta önem kazanan yakınlık iddiası olması"},{"branch_contributions":[{"actual_contribution":"Geçişin öncesindeki koruyucu oluşum alanını verir.","boundary":"Womb image'ıdır; literal path anlamı değildir.","branch_ref":"root_000552/B003","carrier":"1:3'teki ر ح م","distinctive_facet":"Koruyucu oluşum kabı","facet_id":"F001","independent_anchor":"HFT enclosure/formation role"},{"actual_contribution":"Geçişin bedelsiz olmadığını ve oluşumun sonrasında maliyet bulunduğunu ekler.","boundary":"Womb pathology image'ıdır; genel suffering claim'i değildir.","branch_ref":"root_000552/B004","carrier":"1:3'teki ر ح م","distinctive_facet":"Doğum sonrası ağrı ve bozukluk","facet_id":"F001","independent_anchor":"HFT costly-aftermath role"},{"actual_contribution":"Geçişin hedefini dengeli ve ayakta bir durum olarak verir.","boundary":"Uprightness image'ıdır; unresolved path split'i temsil etmez.","branch_ref":"root_001273/B008","carrier":"1:6 supplied exact Arabic","distinctive_facet":"Diklik ve dengeli varış","facet_id":"SOURCE_IMAGE","independent_anchor":"HFT upright-arrival role"}],"branch_refs":["root_000552/B003","root_000552/B004","root_001273/B008"],"candidate_ids":["cand_2b7bb295ca61885c598e"],"claim":"Womb and postpartum facets, 1:6'nın supplied path/uprightness surface'iyle birleşerek merhameti statik shelter değil, oluşumdan bağımsız duruşa geçiş modeli olarak açar.","connection_refs":["conn_05a542581545271f3a76"],"contact_refs":["macro:contact-womb-pathway"],"containment":"HFT exploratory material analogy'dir; unresolved constrained-transit branch ve target morphology dışarıda tutulmuştur.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-womb-pathway","mechanism":"İç kap, doğum sonrası ağrı, yol ve uprightness facetleri korunma, baskı, geçiş ve varış sırası kurar.","member_finding_refs":["macro:finding-womb-pathway"],"proposal_keys":[],"reader_payoff":"Okur koruyucu merhametin bağımlıyı içeride tutmakla bitmeyip zor geçişte taşıyarak ayakta durmasına yardım ettiğini görebilir.","referral_payloads":[],"scope_movements":[{"context_after":"Merhamet, hayatı koruyup oluşturan ve sonra onu maliyetli bir geçitten geçirerek dengeli, dik bir duruma ulaştıran süreç olarak tasarlanabilir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-womb-pathway"}],"support_ids":["sup_0023a2a8f387b62d16ca"],"title":"Merhametin oluşumdan maliyetli geçişe taşıması"},{"branch_contributions":[{"actual_contribution":"Tekrarın güven ve yatışma ihtimalini taşıyacağı duygu içeriğini sağlar.","boundary":"Tenderness facet'inin performative activation'ıdır; soothing root mapping'i bağımsız doğrulanmaz.","branch_ref":"root_000552/B001","carrier":"1:3'teki ritmik çift","distinctive_facet":"İç yumuşaklık ve şefkat","facet_id":"F001","independent_anchor":"1:6 öncesindeki exact doubled utterance ve guidance request"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_6cf571b8d9eb297813e0"],"claim":"Merhamet çifti, ardındaki yön talebiyle birlikte, merhameti yalnızca bildirmeyip talepte bulunma güveni veren performatif bir tekrar olarak önerebilir.","connection_refs":["conn_05a542581545271f3a76"],"contact_refs":["macro:contact-soothing-performance"],"containment":"HFT exploratory outlier'dır; non-dominant soothing branch'i çıkarılmış, bu nedenle claim performative possibility ve lexical gloss dışı tutulmuştur.","epistemic_status":"exploratory","lane":"macro","locked_finding_ref":"locked:macro:finding-soothing-performance","mechanism":"Çiftin audible doubling'i ile hemen sonraki rehberlik talebi arasında ritimden güvene, güvenden isteğe uzanan bir okuma hareketi kurulur.","member_finding_refs":["macro:finding-soothing-performance"],"proposal_keys":[],"reader_payoff":"Okur metnin merhamet hakkında konuşurken konuşanı da merhamet istemeye hazırlayabileceğini deneyimleyebilir.","referral_payloads":[],"scope_movements":[{"context_after":"Çiftin ritmik tekrarı, 1:6'daki rehberlik talebinden önce bağımlı konuşanı güven içinde istemeye hazırlayan yatıştırıcı edim olarak düşünülebilir.","lane":"macro","local_before":"Merhameti sınırsızdır, merhamet edendir.","member_finding_ref":"macro:finding-soothing-performance"}],"support_ids":["sup_dbeeae29a11769bae1c1"],"title":"Tekrarın merhameti yatıştıran bir edim gibi gerçekleştirmesi"},{"branch_contributions":[{"actual_contribution":"Rahmeti, bakım ile hesap arasındaki etkin iyilik ve koruma kipine bağlar.","boundary":"Bu bağlam işlevi, F002 çekirdeğine eklenen wider bir roldür; rahmet kelimesi hesap veya egemenlik ile eşanlamlı değildir.","branch_ref":"root_000552/B001","carrier":"odaktaki iki rahmet adı","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"1:2-1:4 yerleşimi ve 20:5/21:112/18:58 hüküm-izin sahneleri"},{"actual_contribution":"Tanrı hakkında kullanımdaki geniş ulaşan iyiliği, yönetimin niteliği olarak görünür kılar.","boundary":"İlahi genişlik, her belirli sonucun garanti edildiği anlamına gelmez.","branch_ref":"root_000552/B001","carrier":"odaktaki ilahi adlandırma","distinctive_facet":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir.","facet_id":"F005","independent_anchor":"20:5 ve 78:37'de الرحمن'in egemenlik çevresinde görünmesi"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_df7eb8162594427ef66a","cand_f41046bd39da0f0e7582","cand_d3bb76453ebc7313184e","cand_2f4695857ae2a081f6bf","cand_60a51d4abf428220434f","cand_3f8acc60e66adecbce5d"],"claim":"Odaktaki yinelenen rahmet adları, bakım veren rablik ile hesap sahibi egemenlik arasında merhametin işleyişini kurar.","connection_refs":["conn_acf267774e6d5b4c0ac4","conn_ae93daa6102640eb7e15","conn_a8fb51af6f60dd69be6f","conn_b5cabf1ec07a8c8a9e29","conn_b41d96f3484f8c27f09f","conn_30ef4219b8e01868ec3c","conn_4b557722b09c4f8fb6ca","conn_a99d4c6d2be0e95af325","conn_0d2ce4caa518fa7ddff4","conn_217bb5a646f550e99766","conn_92252985df09648fd7d7","conn_a9a7852c4ce01ecc20ab","conn_264341e7151f9039bb28","conn_e7771d175b3bf8b5b52b","conn_f11fecfe0c19616cf078","conn_824615e2d0cc2de2132e","conn_fe21e0e2d6fcc3be8633","conn_34fcbe78f4150d3fa14b","conn_237008137d0db0470db0","conn_8f736312f26fbc8fff4e","conn_71a006e8d4d7d2c3f418","conn_0ed3389c75db1239c81d","conn_2accdf9c9eaa5bdf2353"],"contact_refs":["global:contact:connection-001","global:contact:connection-009","global:contact:connection-012","global:contact:connection-018","global:contact:connection-021","global:contact:connection-032","global:contact:connection-050","global:contact:connection-052","global:contact:connection-064","global:contact:connection-113","global:contact:connection-120","global:contact:connection-130","global:contact:connection-145","global:contact:connection-184","global:contact:connection-189","global:contact:connection-202"],"containment":"Bu, komşu ayetlerin etkinleştirdiği yapısal bir okumadır; Arapça dilbilgisi merhametin hukuki sonucu olduğunu tek başına iddia etmez.","epistemic_status":"supported_structural","lane":"global","locked_finding_ref":"locked:global:finding:governing-mercy","mechanism":"Ayetler arası yerleşim ve ilahi adın farklı hüküm sahnelerinde taşıyıcı olarak yeniden görünmesi, rahmeti hükmün karşıtı değil hükmün niteliği haline getirir.","member_finding_refs":["global:finding:governing-mercy"],"proposal_keys":[],"reader_payoff":"Okur, 1:3'ü yalnızca iki sıfatın tekrarı olarak değil, surenin övgüden hesap düzenine geçişini taşıyan bir yönetim ilkesi olarak görür.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, iki ilahi merhamet adını öne çıkarır; bu adlar genel bir iyilik ve yakınlık bildirimi olarak kalabilir.","lane":"global","member_finding_ref":"global:finding:governing-mercy","wider_after":"1:2'deki rablik/bakım ile 1:4'teki hesap ve hüküm yan yana düşünülünce merhamet, yönetimi yumuşatan değil yönetimin nasıl icra edildiğini belirleyen ara kip olarak görünür.","wider_trigger":"1:2-1:4 geçişi; özellikle 20:5, 21:112, 18:58, 44:6 ve 78:38 gibi rablik, hüküm, izin ve gecikmiş hesap sahneleri."}],"support_ids":["sup_33bf02bc7dc7c085ec7a","sup_508af9abd6c2644e61a0","sup_9a3d6c2de50a13858501","sup_c0a8cb84b2bf462fd8d9","sup_b007ebab928cba9b42d5","sup_b87a1855ee68ffff42db"],"title":"Merhamet yönetimin işleyişini belirleyen menteşedir"},{"branch_contributions":[{"actual_contribution":"Etkin iyilik çekirdeğini bağımlının korunması ve desteklenmesi olarak açar.","boundary":"Yardım ve koruma wider bağlamın katkısıdır; odak adlarına r-b-b veya ʿ-w-n biçimi yüklenmez.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"12:64, 18:16, 22:65 ve 67:19 koruma/yardım sahneleri"},{"actual_contribution":"Rahmi, gelişimin gerçekleştiği koruyucu kap imgesi olarak taşır.","boundary":"Bu maddi kap imgesi ilahi adın literal bedensel anlamı değildir.","branch_ref":"root_000552/B003","carrier":"odaktaki rahmet adları","distinctive_facet":"Dişi bedenindeki bu iç organ, yavrunun oluşup geliştiği yer ve onu karın içinde taşıyan kap işlevindedir.","facet_id":"F001","independent_anchor":"3:6 ve 4:1'de rahimlerde oluşum; 18:82'de çocukların olgunluğa erişmesi"},{"actual_contribution":"Aşama aşama yetiştirme ve tamamlama imgesini rahmetin devamlı bakımına bağlar.","boundary":"ر ب ب ile ر ح م farklı kök alanlarıdır; ilişki analojik taşıyıcı düzeyindedir.","branch_ref":"root_000532/B002","carrier":"odaktaki rahmet adları","distinctive_facet":"repair, nurture, and completion","facet_id":"SOURCE_IMAGE","independent_anchor":"4:2 yetimlerin malları, 17:24 çocuklukta yetiştirilme ve 18:82 aşamalı erişim"},{"actual_contribution":"Rahmetin bağımlının yol ve kriz içinde desteklenmesine açılan yardım imgesini sağlar.","boundary":"Yardım dalı odak kökünün morfolojik çözümlemesi değildir.","branch_ref":"root_001064/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"helping and backing","facet_id":"SOURCE_IMAGE","independent_anchor":"12:18'de yardım arayışı ve 30:5'te yardım/güç çevresi"}],"branch_refs":["root_000532/B002","root_000552/B001","root_000552/B003","root_001064/B001"],"candidate_ids":["cand_8050d6bbbdca90dbcbda","cand_a1ab0115c7eb70b04040","cand_95c34b28045c08acc4d8","cand_a7c789addacd8c868cee"],"claim":"Yinelenen rahmet adları, bağımlı varlığın hem korunmuş bir kapta oluşmasını hem de gelişim boyunca yardım almasını görünür kılar.","connection_refs":["conn_fb513320989435208138","conn_3c9ad2c97962624ade39","conn_cab668f1daf8b3022289","conn_a68bb10addaadc7edb9c","conn_b976dfb04c36d4ebe075","conn_d29cf8cb5f25e2604ec0","conn_42dd4d6fe6c3f4779eb7","conn_d423dc237bfe5a56b168","conn_24dc04997c45b295a85f","conn_a9a0bff222bede971112","conn_30c12d5379babfbbf95a","conn_f798ecf4b91f30e7c301","conn_7efb928341db7d4464a9","conn_e734d72e386921b0f23c","conn_b7ba13769877e67ad414","conn_9a81691b863ec59ae9a9","conn_2e7a8d19d243073fd242","conn_949e85179324861172ac","conn_f28c67ef4aa384c33c8f","conn_c29c56fc9d462c79be3a","conn_06ad8beba9c4ae216de2","conn_c493c5adcb9c2227919c","conn_b56ad7611674b51a2f39","conn_d3935cb22f7ea524ecee","conn_edc0f731e91e1fa38560"],"contact_refs":["global:contact:connection-019","global:contact:connection-025","global:contact:connection-037","global:contact:connection-068","global:contact:connection-084","global:contact:connection-085","global:contact:connection-090","global:contact:connection-092","global:contact:connection-105","global:contact:connection-106","global:contact:connection-110","global:contact:connection-125","global:contact:connection-136","global:contact:connection-146","global:contact:connection-160","global:contact:connection-166","global:contact:connection-167","global:contact:connection-168","global:contact:connection-171","global:contact:connection-172","global:contact:connection-174","global:contact:connection-177","global:contact:connection-204","global:contact:connection-235"],"containment":"Döl yatağı ve r-b-b/ʿ-w-n imleri bağlamsal ve analojik taşıyıcılardır; odaktaki r-ḥ-m adlarına hedef morfolojisi veya tek bir sözlük anlamı icat edilmez.","epistemic_status":"supported_bounded","lane":"global","locked_finding_ref":"locked:global:finding:protected-formation","mechanism":"Aynı okuma, rahim imgesini mekânsal kuşatma; rablik, yardım ve yetiştirmeyi ise zamana yayılan bakım olarak birleştirir, fakat bunları odak kelimelerinin literal morfolojisi saymaz.","member_finding_refs":["global:finding:protected-formation"],"proposal_keys":[],"reader_payoff":"Rahmet, soyut bir duygu olmaktan çıkarak kırılgan oluşumu taşıyan ve yol boyunca destekleyen etkin bir bakım düzeni olarak okunur.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhameti ilahi bir nitelik olarak bildirir; koruma, oluşum ve devamlı destek süreçleri açıkça adlandırılmaz.","lane":"global","member_finding_ref":"global:finding:protected-formation","wider_after":"Döl yatağı, yetim ve küçüklerin bakımı, taşınan yük, korunma ve aşamalı büyüme imgeleriyle merhamet bağımlıyı içine alan ve hareketi boyunca destekleyen bir oluşum alanına dönüşür.","wider_trigger":"3:6, 4:2, 12:18, 12:56, 12:64, 16:7, 17:24, 18:16, 18:82, 22:65 ve 55:3 çevresindeki koruma ve gelişme sahneleri."}],"support_ids":["sup_1c4085b648f2357542f9","sup_e76643a9ca3019e16e68","sup_f9ef2aef6a92810cf352","sup_6772772b6fe1a53ff2fa"],"title":"Merhamet korunan oluşum ve sürdürülen destek olarak görünür"},{"branch_contributions":[{"actual_contribution":"Yakın ve kalıcı ilişki çekirdeğini dua edenlerle önceki yolcular arasında topluluk aidiyetine dönüştürür.","boundary":"Bu, bağlamsal topluluk sürekliliğidir; odak ayeti tek başına belirli bir soy iddiası kurmaz.","branch_ref":"root_000552/B002","carrier":"odaktaki yinelenen adlar","distinctive_facet":"Ortak soydan gelme, kişiler arasında yakın ve kalıcı bir soy ilişkisi kurar.","facet_id":"F001","independent_anchor":"1:5-1:7'de çoğul dua, yol ve daha önce nimet görmüşler; 59:10"},{"actual_contribution":"Bağın yalnızca mevcut değil, korunması veya kopması mümkün olan eylemli bir ilişki olduğunu sınır olarak gösterir.","boundary":"F003 ilişkideki eylemi anlatır; akrabalık varlığını veya kurtuluş garantisini tek başına anlatmaz.","branch_ref":"root_000552/B002","carrier":"odaktaki yinelenen adlar","distinctive_facet":"Soy bağını sürdürmek veya koparmak, ilişkinin kendisini değil ona karşı takınılan eylemli tutumu anlatır.","facet_id":"F003","independent_anchor":"47:22 ve 60:3'te bağların kesilmesi/hesap gününde bağın kurtarmaması"},{"actual_contribution":"Topluluk bağının soyut yakınlıktan önce paylaşılan oluşum ve korunma imgesi taşıdığını gösterir.","boundary":"Organ veya soy anlamı odak adlarının literal anlamı olarak aktarılmaz.","branch_ref":"root_000552/B003","carrier":"odaktaki rahmet adları","distinctive_facet":"Dişi bedenindeki bu iç organ, yavrunun oluşup geliştiği yer ve onu karın içinde taşıyan kap işlevindedir.","facet_id":"F001","independent_anchor":"3:6 ve 4:1'de ortak doğum kaynağı ve rahim çevresi"},{"actual_contribution":"Korunan aidiyetin üvey aile ve bakıcı ilişkisini de kapsayabileceğini sınırlar.","boundary":"ر ب ب ve ر ح م özdeş değildir; bu yalnızca korunan ilişki analojisidir.","branch_ref":"root_000532/B005","carrier":"odaktaki rahmet adları","distinctive_facet":"fostered child and step-family relation","facet_id":"SOURCE_IMAGE","independent_anchor":"4:23'te ربائبكم ve 64:14'te aile ilişkisi içinde uyarı/bağışlama"}],"branch_refs":["root_000552/B002","root_000552/B003","root_000532/B005"],"candidate_ids":["cand_28a32ae835f16a29a899","cand_15f35ad48f6eee8e4f23","cand_fde51af1fd07d0c4ae80","cand_e261524b56547c4087cf","cand_f8629fced418f893f6ef","cand_53c6add6fc2594672c97"],"claim":"Rahmet, birlikte dua edenleri daha önce yol almış ve iyilik görmüş kişilerle ilişkilendiren topluluk kurucu bir bağ olarak görünür.","connection_refs":["conn_e7c17d789e7c510d3abb","conn_057d3ff5c9574ba8b787","conn_08d53cc7edbac12a1d7b","conn_5f97fac6ffae4d977a11","conn_f2522d204fcf01485c8d","conn_29e7503e3b570c8fd76d","conn_7cf1b86194aa25c86950","conn_ee00532e32c840c3b5f6","conn_00bbe8bacfcca2c11b24","conn_4ee34db02897f470b199","conn_c953478cc5d9a4785e56","conn_73a17ca300d4e9503cfb","conn_745e2faf63effba0ffaa","conn_adceff5c035b1c64a2b5","conn_8935cb60b57b29fbe3cc","conn_6381e04a442955fef25a","conn_ed50885662c79aa996f0","conn_7c691617ada0b0534710"],"contact_refs":["global:contact:connection-003","global:contact:connection-017","global:contact:connection-035","global:contact:connection-040","global:contact:connection-041","global:contact:connection-046","global:contact:connection-054","global:contact:connection-062","global:contact:connection-067","global:contact:connection-074","global:contact:connection-078","global:contact:connection-087","global:contact:connection-116","global:contact:connection-155","global:contact:connection-178","global:contact:connection-203","global:contact:connection-224","global:contact:connection-233"],"containment":"Yakın soy ve üvey aile bağlantıları farklı kök ve kullanım alanlarıdır; bunlar odaktaki r-ḥ-m için literal eşanlamlı veya otomatik soy iddiası değildir.","epistemic_status":"exploratory_relational","lane":"global","locked_finding_ref":"locked:global:finding:community-bond","mechanism":"Rahim/soy ilişkisi, üvey aile ve karşılıklı dua, odaktaki adları kolektif bir bağımlılık ve bakım ağına döndürür; bağın kopabileceği de aynı geniş okumada korunur.","member_finding_refs":["global:finding:community-bond"],"proposal_keys":[],"reader_payoff":"“Biz”in yol istemesi bireysel bir talep değil, önceki yolcularla ilişki içinde konuşan bir topluluğun talebi olarak belirginleşir.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhamet adlarını söyler; konuşanların birbirleriyle veya daha önce iyilik görmüş kişilerle nasıl bağlandığını belirtmez.","lane":"global","member_finding_ref":"global:finding:community-bond","wider_after":"1:5-1:7'deki biz, ibadet, yol talebi ve iyilik görmüşler dizisi; soy, rahim, üvey aile ve topluluk duası imgeleriyle korunan bir aidiyet sürekliliği kazanır.","wider_trigger":"4:1, 4:23, 7:151, 8:75, 23:109, 47:22, 49:10, 59:10 ve 60:3 gibi soy, kardeşlik, bakım, uzlaşma ve bağın kopması sahneleri."}],"support_ids":["sup_2dde0b803f410fe142b1","sup_38b677bedfb7cb3c721c","sup_8ae647e5614106c3a243","sup_96f1019255dfb30db631","sup_b31a34cf08b5479103be","sup_bb79d1becda69e351bfd"],"title":"Merhamet dua eden topluluk ile önceki yolcular arasında bağ kurar"},{"branch_contributions":[{"actual_contribution":"İç yumuşama ve yakınlık çekirdeğini sertlik, sapma ve rahmetten kesilme karşısında görünür kılar.","boundary":"Öfke, sapma ve nankörlük odak kelimelerine eklenmez; bunlar wider karşıt tetikleyicilerdir.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bir başkasının durumu karşısında yüreğin yumuşaması, ona acıma ve içten yakınlık duyma çekirdeği oluşturur.","facet_id":"F001","independent_anchor":"23:75-76, 17:100, 19:69 ve 29:23 karşıtlıkları"},{"actual_contribution":"Etkin iyiliğin alıcıyı koruyabileceğini, fakat onun yönelişini zorunlu olarak düzeltmediğini gösterir.","boundary":"Fayda ve dönüş ihtimali koşulsuz bağışlanma olarak sunulmaz.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"7:57, 10:21 ve 41:50'de rahmetten sonra yenilenen fakat bozulabilen durum"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_2522d078ac888a274b5f","cand_d6f1e3a2070c71c46eb6","cand_789e827787980cc54422"],"claim":"Merhamet, yolu yalnızca sert bir hüküm yüzeyine dönüşmekten koruyan bir yumuşaklık sağlar, fakat sorumluluğu ve sapma ihtimalini ortadan kaldırmaz.","connection_refs":["conn_ef746f89a987bb0167b5","conn_f50ee4a5d8304f0472b5","conn_fa5d98ee42fec8d9af8c","conn_ffbd3a1a2f2e2f9affcb","conn_5bd3614c92da58f847f1","conn_dc03226bad0c36035c5e","conn_828d72fa8a924f739de1","conn_dcbf873354b16e36fa3f","conn_d515f2e5585c5dc42a0b","conn_59eea067ffefb6a20ca8","conn_4094302be4abe7f3273e","conn_ae174614af4adf76d388","conn_6cdf19d1de366c9d6698","conn_04fe70e29b7f90e52f28","conn_0e51f7c64bac59fbe0af","conn_0f5f008338e349877194","conn_b0b751813a9736c5b544","conn_8a41baf2f45d1862ccfc","conn_ac61cdab571fb5aa97da","conn_487c650147bce55884a0","conn_d4b5de3754c5890d7749","conn_74b058ecfa915b654643","conn_1ad38dd5d22be6f34872"],"contact_refs":["global:contact:connection-031","global:contact:connection-034","global:contact:connection-086","global:contact:connection-088","global:contact:connection-103","global:contact:connection-104","global:contact:connection-121","global:contact:connection-129","global:contact:connection-157","global:contact:connection-163","global:contact:connection-164","global:contact:connection-169","global:contact:connection-175","global:contact:connection-176","global:contact:connection-196","global:contact:connection-199","global:contact:connection-206","global:contact:connection-208","global:contact:connection-216","global:contact:connection-217","global:contact:connection-220","global:contact:connection-225","global:contact:connection-232","global:contact:connection-236"],"containment":"Bu bulgu karşıtlık ve sonuç örüntüsüdür; odak ayetinin kelimelerine öfke, sapma veya maddi yumuşaklık anlamı eklenmez.","epistemic_status":"supported_counterpattern","lane":"global","locked_finding_ref":"locked:global:finding:softening-boundary","mechanism":"Yumuşaklık/sertlik ve merhamet/sapma karşıtlıkları aynı geniş okumada tutulur; olumlu etkinin alıcı tarafından bozulabilmesi, rahmeti koşulsuz sonuçla özdeşleştirmeyi engeller.","member_finding_refs":["global:finding:softening-boundary"],"proposal_keys":[],"reader_payoff":"Okur, merhameti ne yalnızca duygu ne de garantili bağışlanma sayar; merhamet, sertleşmeyi önleyen fakat alıcının yönelişini sınamaya devam eden bir atmosfer olur.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhameti olumlu bir ilahi nitelik olarak sunar; bunun sertlik, sapma veya nankörlükle karşıtlığı görünmezdir.","lane":"global","member_finding_ref":"global:finding:softening-boundary","wider_after":"Sonraki kayıtlar merhameti sert kalp, öfke, sapma ve nankörlük karşısında koruyucu bir yumuşaklık olarak gösterirken, merhamet görmenin iç yönelişi otomatik olarak düzeltmediğini de açığa çıkarır.","wider_trigger":"1:7'deki öfke ve sapma karşıtlığı; ayrıca 23:75-76, 7:57, 10:21, 17:100, 19:69, 29:23, 41:50 ve 42:48 gibi rahatlama sonrası direnç sahneleri."}],"support_ids":["sup_1b35e99c2fb5e1a76a56","sup_7828b6bec44e8748ee2a","sup_0cef6af8e0fcd1a119d8"],"title":"Merhamet sertleşmeye karşı yumuşatıcı fakat otomatik olmayan bir koşuldur"},{"branch_contributions":[{"actual_contribution":"Rahmi özgü ağrı/hastalık dalını, başlangıç sonrasında kırılgan olanın onarılması için sınırlı bir analojiye bağlar.","boundary":"Doğum sonrası hastalık odak adlarının sözlük glossu değildir; morfoloji ve klinik ayrıntı genişletilmez.","branch_ref":"root_000552/B004","carrier":"odaktaki rahmet adları","distinctive_facet":"Dişi hayvan veya kadında döl yatağının ağrıması ya da hastalanması temel durumdur; özellikle bazı kullanımlarda bu durum doğum sonrasında görülür.","facet_id":"F001","independent_anchor":"3:6'daki rahimlerde biçimlenme ile 1:2-1:6 bağımlılık geçişi"}],"branch_refs":["root_000552/B004"],"candidate_ids":["cand_8c31bfb181ac9c2bb048"],"claim":"Odaktaki rahmet adları, literal sözlük anlamı olarak değil, kırılgan oluşumun başlangıç sonrasında onarılması için keşifsel bir bakım analojisini taşıyabilir.","connection_refs":["conn_ce528e0dd4cbd865ab59"],"contact_refs":["global:contact:connection-044"],"containment":"Bu en dar ve analojik bulgudur; B004 hastalık dalları odak adlarının literal karşılığı değildir, hedef morfolojisi de varsayılmaz.","epistemic_status":"exploratory_analogical","lane":"global","locked_finding_ref":"locked:global:finding:fragile-emergence","mechanism":"Aynı kök alanındaki rahim ve gelişme imgesi, doğum sonrası zayıflığı bir yaşam döngüsü eşiği olarak odak ayetine geri bağlar.","member_finding_refs":["global:finding:fragile-emergence"],"proposal_keys":[],"reader_payoff":"Merhamet, yalnızca baştan verilen iyilik değil, bağımlının ortaya çıktıktan sonra da ayakta kalmasına yardım eden onarıcı bakım olarak görünür.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, doğum sonrası hastalık veya yeni ortaya çıkanın kırılganlığı hakkında bir şey söylemez.","lane":"global","member_finding_ref":"global:finding:fragile-emergence","wider_after":"Rahim ve yetiştirme çevresindeki kayıtlarla birlikte düşünüldüğünde merhamet, yeni bir başlangıçtan sonra henüz sağlamlaşmamış olanı onaran sınırlı bir bakım imgesine taşınabilir.","wider_trigger":"3:6'daki rahimlerde biçimlenme sahnesi ve 1:2-1:6 arasındaki bağımlılık/gelişme dizisi; okuyucu kaydındaki destekli geçiş önerisi."}],"support_ids":["sup_1c9b76b0644df6382e0f"],"title":"Merhamet kırılgan bir başlangıç sonrasındaki bakıma da açılabilir"},{"branch_contributions":[{"actual_contribution":"İlahi kullanımın geniş ulaşmasını, çift adın süreklilik okumasıyla birlikte tutar.","boundary":"Bu ayrım keşifsel analitik bir okumadır; supplied olmayan sarfî fark kesinleştirilmez.","branch_ref":"root_000552/B001","carrier":"odaktaki iki ilahi rahmet adı","distinctive_facet":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir.","facet_id":"F005","independent_anchor":"packet analitik glossundaki geniş/taşan ve devam eden/yönelmiş ayrımı; 57:28"}],"branch_refs":["root_000552/B001"],"candidate_ids":["cand_18cdd96248c72855b8df","cand_951b9270445ea3ae0c49"],"claim":"İki rahmet adının yan yana gelişi, yalnızca tekrar değil, kapsam ile sürekliliği birlikte taşıyan çift kutuplu bir okuma fırsatı verir.","connection_refs":["conn_b96942a1393a43c3b85c","conn_872e87ccb38e756aefdb","conn_44108b6102526a25c139"],"contact_refs":["global:contact:connection-138"],"containment":"Bu, packet analitik glossu ve geniş okuma üzerine kurulu keşifsel bir ayrımdır; supplied olmayan morfoloji veya kesin anlam dağılımı iddia edilmez.","epistemic_status":"exploratory_analytic","lane":"global","locked_finding_ref":"locked:global:finding:breadth-continuance","mechanism":"Analitik yüzey açıklamasındaki geniş/taşan ve devam eden/yönelmiş ayrımı, sonraki kapsam ve ışık sahneleriyle ilişkilendirilir; bu ayrım sarfî bir hüküm olarak ileri sürülmez.","member_finding_refs":["global:finding:breadth-continuance"],"proposal_keys":[],"reader_payoff":"Çift adlandırma, iki eşanlamlıyı üst üste koymaktan daha fazlası olarak, rahmetin hem kuşatmasını hem devam eden etkisini düşündürür.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, iki adın tekrarı nedeniyle yoğunlaştırılmış bir niteleme gibi okunabilir.","lane":"global","member_finding_ref":"global:finding:breadth-continuance","wider_after":"Genişleyen rahmet, ilahi yönetim ve iki pay rahmet ile ışık gibi sonraki bağlamlar, çifti kapsamın genişliği ile ulaşmaya devam eden yönelimin birlikte tutulduğu bir düzen olarak düşündürür.","wider_trigger":"57:28'deki iki pay rahmet ve yürüyen ışık; 7:156'daki her şeyi kuşatan ama düzenlenen rahmet; 17:110'daki adlandırma ve dua dengesi."}],"support_ids":["sup_1ff8925c0fe04cf8f389","sup_6c9122b4b3ec44fbe286"],"title":"Yinelenen çift genişlik ve süreklilik olarak birlikte tutulabilir"},{"branch_contributions":[{"actual_contribution":"Etkin iyiliği doğru istikamete yöneltme ve orada destekleme olarak açar.","boundary":"Hidayet, odak kelimelerinin literal glossu değil, wider eylem sonucudur.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"18:10, 4:175, 27:63 ve 57:28'de rahmet ile yol/ışık/hidayet"},{"actual_contribution":"Rahmetin, yön arayan bağımlı topluluğun dilek ve yönelişinde gerçekleşen bir söz eylemi olduğunu gösterir.","boundary":"Dua formülü çekirdek anlamdan doğan bağlamsal eylemdir; her kullanımın aynı sonucu verdiği söylenmez.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bir kimsenin Tanrı'nın esirgemesine erişmesini dilemek, çekirdek anlamdan doğan kalıplaşmış bir söz eylemidir.","facet_id":"F004","independent_anchor":"18:10 ve 3:8'de rahmetin doğrudan istenmesi"},{"actual_contribution":"Yakın olana gönderilen armağan imgesini yol gösteren rahmet talebine bağlar.","boundary":"Armağan imgesi, rahmetin literal kök çözümlemesi değildir.","branch_ref":"root_001583/B004","carrier":"odaktaki rahmet adları","distinctive_facet":"a gracious gift sent to someone close","facet_id":"SOURCE_IMAGE","independent_anchor":"3:8'de “bize rahmet bağışla” ve 57:28'de rahmet/ışık"}],"branch_refs":["root_000552/B001","root_001583/B004"],"candidate_ids":["cand_f9fd1dc644020b8a1f57"],"claim":"Rahmet, rehberliğin yalnızca verilmesi değil, bağımlı kişinin doğru istikamete yöneltilip orada tutulması olarak görünür.","connection_refs":["conn_18f94899336a79c21045","conn_62a9510338570e545d73","conn_253eb415f1302b14cf82","conn_feb2c1feb893a9fbc8e4","conn_6fc7482092cf550c491e","conn_410e78d39a67704a77af","conn_0627424d1aa164f906b0","conn_471b9342450c30b56f27","conn_2c0d76d4fdbf13b54ed6","conn_bc3b55c45dadfbd486af","conn_623f22113a1d8b93f40c","conn_ae6448e56d49ccdfa00a","conn_c226d09fb4bfe6cca9a6","conn_465ab8eadb98dfe7b6ff","conn_d2fe6b575eade2570f25","conn_509cac5c14d43bceda4c"],"contact_refs":["global:contact:connection-000","global:contact:connection-005","global:contact:connection-010","global:contact:connection-016","global:contact:connection-022","global:contact:connection-028","global:contact:connection-057","global:contact:connection-094","global:contact:connection-124","global:contact:connection-128","global:contact:connection-143","global:contact:connection-154","global:contact:connection-185","global:contact:connection-187","global:contact:connection-193","global:contact:connection-201"],"containment":"Hidayet ve yol sahneleri bağlamsal etkinleştiricilerdir; odak kelimelerine doğrudan “hidayet” sözlük anlamı yüklenmez.","epistemic_status":"supported_structural","lane":"global","locked_finding_ref":"locked:global:finding:merciful-guidance","mechanism":"Merhamet talebi veya rahmetin sonucu, doğru yol ve ışık fiilleriyle yan yana gelir; ilişki, ilahi sıfatın rehberlik eylemiyle bağlamda işletildiğini gösterir.","member_finding_refs":["global:finding:merciful-guidance"],"proposal_keys":[],"reader_payoff":"“Merhamet edendir” ifadesi, okurda pasif bir iyilik beklentisi değil, yol bulmayı ve yolda kalmayı mümkün kılan bir destek beklentisi oluşturur.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhamet ile yol, doğru istikamet veya ışık arasındaki işlevsel bağlantıyı kurmaz.","lane":"global","member_finding_ref":"global:finding:merciful-guidance","wider_after":"Rahmetin hidayet, doğru yol, sözün iyisi, ışık ve kalplerin sabitlenmesiyle birlikte görünmesi, merhameti yön veren ve yönelişi sürdüren etkin yardım olarak açar.","wider_trigger":"18:10, 22:24, 3:101, 4:175, 3:8, 27:63, 33:43, 57:28 ve 7:204 çevresindeki yol, ışık, dinleme ve kalp istikrarı sahneleri."}],"support_ids":["sup_aa8e63cba4b79c75afe5"],"title":"Merhamet yönlendirmeyi ve yolda kalmayı işler hale getirir"},{"branch_contributions":[{"actual_contribution":"Etkin iyiliğin kaybı veya sıkıntıyı gidererek yeniden kuran yönünü görünür kılar.","boundary":"Yenilenme sahneleri bağlamsal pay-off'tur; odak adlarına “yağmur” veya “diriltme” literal anlamı verilmez.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"7:57, 21:84, 30:50 ve 42:28'de yağmur, sıkıntının kaldırılması ve canlanma"}],"branch_refs":["root_000552/B001"],"candidate_ids":[],"claim":"Daha geniş kayıt, odaktaki rahmeti başlangıçta verilmiş bir nitelik değil, kayıp veya sıkıntıdan sonra hayatı yeniden açan etkin bir yenileme olarak da görünür kılar.","connection_refs":["conn_e8b8843f524b845556c4","conn_5f32642b580f31e911ba","conn_282deddc2409c5cebf7a","conn_e737281b8d901e59e130","conn_e735b48613d5286abfc1","conn_bb47b5cad2131a75e793","conn_79363463eb6143946115","conn_57156362fa28713566d9","conn_783e3fcb39706b737cee"],"contact_refs":["global:contact:connection-080","global:contact:connection-115","global:contact:connection-127","global:contact:connection-132","global:contact:connection-186","global:contact:connection-190","global:contact:connection-200","global:contact:connection-210","global:contact:connection-212"],"containment":"Yağmur, diriltme ve aile iadesi odak adlarının maddi sözlük anlamı değildir; bunlar rahmetin wider-result örnekleridir.","epistemic_status":"supported_contextual","lane":"global","locked_finding_ref":"locked:global:finding:restorative-renewal","mechanism":"Aynı rahmet taşıyıcısı, umutsuzluk/ölüm/zarar öncesi ve yenilenme sonrası düzenek içinde okunur; sonuç, odak için maddi bir literal anlam değil bağlamsal bir eylem imgesidir.","member_finding_refs":["global:finding:restorative-renewal"],"proposal_keys":["global:proposal:restorative-renewal"],"reader_payoff":"Merhamet, durumu değiştirmeyen soyut bir iyi niyet değil, kapanmış görünen bir imkânı yeniden açabilen bir fiil olarak belirginleşir.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhametin yağmur, diriltme, iyileşme veya kaybın geri verilmesi gibi somut sonuçlarını belirtmez.","lane":"global","member_finding_ref":"global:finding:restorative-renewal","wider_after":"Kuraklık ve umutsuzluk sonrası yağmur, ölü toprağın canlanması, sıkıntının kaldırılması ve ailenin geri verilmesi; rahmeti yenileyen ve yeniden kuran etkin bir sonuç olarak görünür kılar.","wider_trigger":"7:57, 21:84, 30:46, 30:50, 36:52, 38:43 ve 42:28'deki yağmur, diriltme, sıkıntıdan çıkış ve aileyi geri verme sahneleri."}],"support_ids":[],"title":"Merhamet sıkıntı sonrasında yenileyen bir eylem olarak görünür"},{"branch_contributions":[{"actual_contribution":"Etkin iyilik çekirdeğini bilgi ve yönlendirme taşıyan gönderim olarak açar.","boundary":"Vahiy ve öğretim wider sonuçlardır; odak adlarının sözlük glossu değildir.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"41:2, 16:64, 17:82 ve 55:2-4'te indirme, kitap, şifa, öğretim ve beyan"},{"actual_contribution":"İlahi kullanımda rahmetin yaratılmışlara anlam ve uyarı ulaştıran geniş erişimini gösterir.","boundary":"İlahi genişlik, her alıcının aynı tepkiyi verdiğini veya odak cümlesinin vahiy kelimesi taşıdığını göstermez.","branch_ref":"root_000552/B001","carrier":"odaktaki ilahi adlandırma","distinctive_facet":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir.","facet_id":"F005","independent_anchor":"46:12, 28:46, 28:86 ve 45:20'de kitap/uyarı/hidayet/rahmet"}],"branch_refs":["root_000552/B001"],"candidate_ids":[],"claim":"Odaktaki rahmet, sonraki wider reading içinde vahiy, kitap, öğretim ve anlamlı iletişim aracılığıyla ulaştırılan yönlendirici bir iyilik olarak görünür.","connection_refs":["conn_1a0842d9dcdf5ddb9528","conn_6a6fd79e3b33b4c38b9e","conn_2551ccb0812d234c0cf3","conn_1deb5b2b7ba62849cb91","conn_74d6fcab81c7b06accd7","conn_1480242e7315e7c0f395","conn_0235530afcbd8bca7037","conn_7d581a5b835e2c8b9e9e","conn_ca0de6200c4a59f901e3","conn_0a8eb0686a1b7899358f","conn_3b13f9b5cc9a1db6bb41","conn_55c8d7ed29ae761e02a2","conn_acabd5796f9cf04fcda0","conn_08536d4e00f6a9029f04","conn_05586a2860effe85b7c8","conn_0c58085eb93d8c8522be","conn_ab7c700881b2afb9b266","conn_918d6e532b3d82fcc94a","conn_f1291952df00662267d6","conn_689e413536bb79362829","conn_8aeac00bba2e32574233","conn_abc0377c8cc263e3802f"],"contact_refs":["global:contact:connection-002","global:contact:connection-013","global:contact:connection-014","global:contact:connection-020","global:contact:connection-056","global:contact:connection-070","global:contact:connection-082","global:contact:connection-091","global:contact:connection-096","global:contact:connection-109","global:contact:connection-111","global:contact:connection-135","global:contact:connection-137","global:contact:connection-151","global:contact:connection-153","global:contact:connection-162","global:contact:connection-188","global:contact:connection-191","global:contact:connection-194","global:contact:connection-197","global:contact:connection-215","global:contact:connection-222"],"containment":"Kitap ve öğretim sahneleri bağlamsal sonuçlardır; odak adlarının literal anlamı “vahiy” veya “öğretim” değildir.","epistemic_status":"supported_contextual","lane":"global","locked_finding_ref":"locked:global:finding:mercy-as-revelation","mechanism":"Rahmet adının indirme, açıklama, hidayet, şifa ve beyan eylemleriyle birlikte tekrar edilmesi; rahmetin bilgiye erişim ve uyarı düzenindeki işlevini açar.","member_finding_refs":["global:finding:mercy-as-revelation"],"proposal_keys":["global:proposal:mercy-as-revelation"],"reader_payoff":"Okur, rahmeti yalnızca alıcıya karşı bir tutum olarak değil, alıcının anlayabilmesi ve yön bulabilmesi için gönderilen bir içerik/eylem olarak da okur.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, iki rahmet adını bir kitap, öğretim, iletişim veya uyarının verilmesiyle bağlamaz.","lane":"global","member_finding_ref":"global:finding:mercy-as-revelation","wider_after":"Kitabın indirilmesi, açıklaması, öğretmesi, iletişim kapasitesi ve şifa olarak inmesi; rahmeti insanlara bilgi ve yön verecek bir gönderim olarak görünür kılar.","wider_trigger":"41:2, 46:12, 16:64, 17:82, 17:87, 18:65, 28:43, 28:46, 28:86, 29:51, 41:32, 45:20 ve 55:2-4 kayıtları."}],"support_ids":[],"title":"Merhamet vahiy ve öğretim yoluyla ulaştırılan iyilik olarak görünür"},{"branch_contributions":[{"actual_contribution":"Etkin iyiliği korunan kabul, dönüş ve sonuç üreten bir işlem olarak görünür kılar.","boundary":"Kabul ve arınma wider bağlamdadır; odak ayeti tek başına şartlı hukuk formülü değildir.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bu iç yöneliş, acınan kişiyi esirgemeyi ve ona iyilikte bulunmayı gerektiren etkin bir sonuç taşır.","facet_id":"F002","independent_anchor":"4:175, 6:54, 9:21 ve 45:30'da rahmete giriş; 24:10-21'de koruma ve arınma"},{"actual_contribution":"İlahi rahmetin genişliğini egemenlik ve izin düzeniyle birlikte tutar.","boundary":"“Her şeyi kuşatma” sonucu sınırsız veya sorumluluksuz kabul anlamına getirilmez.","branch_ref":"root_000552/B001","carrier":"odaktaki ilahi adlandırma","distinctive_facet":"Tanrı hakkında kullanıldığında esirgemenin genişliği ve yaratılmışlara iyilik olarak ulaşması belirginleşir.","facet_id":"F005","independent_anchor":"7:156, 35:2, 40:7 ve 76:31'de kuşatıcılık, açma/kapama ve yönetilmiş giriş"},{"actual_contribution":"Nimet ve iyi hal dalını, rahmete girişin bağlamsal yolu olarak görünür kılar.","boundary":"Nimet dalı odak kökünün literal eşdeğeri değildir.","branch_ref":"root_001525/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"pleasant well-being and bestowed favor","facet_id":"SOURCE_IMAGE","independent_anchor":"9:99'da nimet, yakınlık ve rahmete giriş"}],"branch_refs":["root_000552/B001","root_001525/B001"],"candidate_ids":[],"claim":"Merhamet kuşatıcıdır, fakat sorumluluk ve hesap düzenini askıya almayan, kime ve nasıl ulaşacağı yönetilen bir kabuldür.","connection_refs":["conn_95f2a3bbd953befd070a","conn_a77a4c2d445a6dca6ee4","conn_ffd80800795798a394ce","conn_6ec9e5023a1bf0c8eb54","conn_430b5a2a3dfad27c872a","conn_73cf9d3d5886cb5e3441","conn_57275f19b09db7e24705","conn_0a5707d7dbba5b64b169","conn_bf080fa472e93e429168","conn_5fcd13f4904aab192f1e","conn_caee61a8570aea8a8128","conn_8ca248083d868640c4ac","conn_b732acc5afb3cffe4c10","conn_b8a838b9545b59375eab","conn_66010a04278a8410aa4c","conn_38172160be2d2eae840d","conn_4b2523ca890de34edc3c","conn_67f1c59a3e866c95c518","conn_eab1843240e5be131cc2","conn_d1475e54a557097278d3","conn_b473e323254829719498","conn_daf9c074d54fcc47746e","conn_5c3814b929f345f0d17b","conn_017641324dc4327730fa","conn_dc4a4aee65328e89f8a2","conn_5abc4d3463f157c9fdba","conn_c6ea9262867fad4ec185","conn_f2626e60f3838425daa2","conn_52519e30cac35909e557","conn_c34188d682fd7359b782","conn_0e55d2d77a8a1f7f2318","conn_1bd7c5f5fc78d2acaf6d","conn_1df4affd2c85bf86fc8d","conn_1ba017527cde4213a369","conn_ca5f9d85c1655735227b","conn_47acfab587892ba35657","conn_8d5cd627a0b934d015a2","conn_6f154855d7040b0cc5f0","conn_e316d24d103eb288585d","conn_f7ee39b38b8bc77c0f0f","conn_ca73f24d1c6eb81a77ef","conn_52b00fba3510090385c0"],"contact_refs":["global:contact:connection-008","global:contact:connection-015","global:contact:connection-023","global:contact:connection-047","global:contact:connection-063","global:contact:connection-066","global:contact:connection-069","global:contact:connection-071","global:contact:connection-072","global:contact:connection-073","global:contact:connection-075","global:contact:connection-097","global:contact:connection-098","global:contact:connection-099","global:contact:connection-100","global:contact:connection-101","global:contact:connection-102","global:contact:connection-108","global:contact:connection-114","global:contact:connection-117","global:contact:connection-118","global:contact:connection-123","global:contact:connection-131","global:contact:connection-133","global:contact:connection-134","global:contact:connection-139","global:contact:connection-141","global:contact:connection-142","global:contact:connection-148","global:contact:connection-149","global:contact:connection-150","global:contact:connection-159","global:contact:connection-173","global:contact:connection-180","global:contact:connection-181","global:contact:connection-195","global:contact:connection-205","global:contact:connection-207","global:contact:connection-211","global:contact:connection-213","global:contact:connection-214","global:contact:connection-219"],"containment":"Bu bulgu bağlamsal düzen ve sonuç örüntüsüdür; odak ayetinin iki adından tek başına kapsam/izin hukukunu çıkardığını söylemez.","epistemic_status":"supported_ordered","lane":"global","locked_finding_ref":"locked:global:finding:ordered-admission","mechanism":"Kabul/rahmet, izin, seçme, dönüş, hesap ve ceza karşıtlıkları aynı wider record içinde birlikte tutulur; “geniş” ifadesi sınırsız sonuç garantisine çevrilmez.","member_finding_refs":["global:finding:ordered-admission"],"proposal_keys":["global:proposal:ordered-admission"],"reader_payoff":"Okur, 1:3'teki rahmeti ne salt ceza ne de cezasızlık olarak görür; rahmet, egemenliğin hesap verebilir ama koruyucu çalışma tarzıdır.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhametin kapsamlı olması ile seçme, izin, sonuç ve hesap arasındaki düzeni açıklamaz.","lane":"global","member_finding_ref":"global:finding:ordered-admission","wider_after":"Rahmetin her şeyi kuşattığı söylenirken kabul, giriş, şefaat, bağışlama ve koruma sahneleri izne, yönelişe veya sonuç düzenine bağlanır; böylece merhamet hükmün alternatifi değil düzenlenmiş kabul biçimidir.","wider_trigger":"6:12, 6:54, 6:147, 7:49, 7:156, 9:21, 9:99, 17:57, 18:98, 20:109, 24:10, 29:21, 35:2, 40:9, 42:8, 45:30, 48:25 ve 76:31."}],"support_ids":[],"title":"Geniş merhamet seçme, izin ve hesap düzeni içinde işler"},{"branch_contributions":[{"actual_contribution":"İç yakınlık çekirdeğini ilişki içinde yumuşak söz ve huzur olarak somutlaştırır.","boundary":"Toplumsal davranış, odak sıfatlarının doğrudan sözlük karşılığı değildir.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Bir başkasının durumu karşısında yüreğin yumuşaması, ona acıma ve içten yakınlık duyma çekirdeği oluşturur.","facet_id":"F001","independent_anchor":"3:159, 17:28, 30:21 ve 36:58'de yumuşaklık, sükûn ve barış sözü"},{"actual_contribution":"Karşılıklılık çekirdeğini topluluğun birbirine bakım ve sabır göstermesi olarak açar.","boundary":"Karşılıklı kullanımın bağlamsal uygulaması, ilahi adların karşılıklı olduğu iddiası değildir.","branch_ref":"root_000552/B001","carrier":"odaktaki rahmet adları","distinctive_facet":"Topluluğun bireylerinin birbirine acıyıp birbirini esirgemesi, çekirdeğin karşılıklı bir kuruluşta gerçekleşmesidir.","facet_id":"F003","independent_anchor":"49:10, 59:10, 90:17 ve 57:27'de karşılıklı merhamet, uzlaşma ve bakım"}],"branch_refs":["root_000552/B001"],"candidate_ids":[],"claim":"Wider reading, odaktaki merhameti yalnızca ilahi nitelik olarak değil, söz ve ilişki düzeninde yumuşaklık, uzlaşma ve karşılıklı bakım üreten bir eksen olarak görünür kılar.","connection_refs":["conn_0236a53760f37ab64132","conn_444cb24f95566f5cd4d2","conn_2078d925db0dcf890d92","conn_acb133f8c9df54702e16","conn_d499c03480a83fc248bf","conn_b228eaa60e8482da1ab2","conn_7fe286e79384b912f559","conn_41b00da64e07352c6218","conn_3f94bbb01f9698ada1ba","conn_f1408f50d59637ad547a","conn_a209948c9fc3d8101d31","conn_0be4e4de80d6e5afcf02"],"contact_refs":["global:contact:connection-089","global:contact:connection-093","global:contact:connection-095","global:contact:connection-107","global:contact:connection-112","global:contact:connection-119","global:contact:connection-122","global:contact:connection-126","global:contact:connection-156","global:contact:connection-158","global:contact:connection-161","global:contact:connection-234"],"containment":"Eşlik ve toplumsal davranış, odak kelimelerinin literal anlamı değil bağlamın ürettiği uygulama ve taşıma alanıdır.","epistemic_status":"supported_contextual","lane":"global","locked_finding_ref":"locked:global:finding:embodied-mercy","mechanism":"Rahmetin adı, sert kalp/ayrılık/zarar ihtimali bulunan sahnelerde yumuşak söz, bağışlama, istişare ve birbirine merhamet eylemleriyle birlikte çalışır.","member_finding_refs":["global:finding:embodied-mercy"],"proposal_keys":["global:proposal:embodied-mercy"],"reader_payoff":"İki rahmet adı, insan topluluğunun birbirine nasıl davranması gerektiğini doğrudan emir vermeden, sonraki uygulama sahneleriyle somutlaştırır.","referral_payloads":[],"scope_movements":[{"isolated_before":"Tek başına ayet, merhamet adlarının insanlar arası söz, uzlaşma, eşlik veya ortak dayanışmaya nasıl dönüştüğünü göstermez.","lane":"global","member_finding_ref":"global:finding:embodied-mercy","wider_after":"Kardeşleri barıştırma, yumuşak konuşma, istişare, eşler arasındaki rahmet, toplu sabır ve karşılıklı merhamet; ilahi rahmetin toplumsal davranışta bir karşılık bulduğunu gösterir.","wider_trigger":"3:159, 9:61, 9:128, 11:90, 17:28, 24:21, 25:63, 30:21, 36:58, 57:27, 59:10 ve 60:12."}],"support_ids":[],"title":"Merhamet davranışta yumuşak söz ve karşılıklı bakım olur"}],"ready_for_prose":true,"rejections":[{"branch_exclusion_reasons":[],"branch_refs":[],"candidate_id":"cand_a8883dc9a7a282d88748","duplicate_of":null,"excluded_branch_refs":[],"failed_edge":"Bağımsız tetikleyici ve değişmiş okuma/okuyucu getirisi yok; kayıt yalnızca kök taşıyıcısı ve provenans bilgisidir.","lane":"micro","reason":"Bu kayıt gerçek yüzey taşıyıcısını doğrular, fakat ledger_only yükümlülüğü nedeniyle tek başına yeni bir okuma veya okuyucu getirisi oluşturamaz.","support_ids":["sup_8680094eccf25d2dee9a"]},{"branch_exclusion_reasons":[],"branch_refs":["root_000552/B004"],"candidate_id":"cand_d2ca13e8f29400bdb7ed","duplicate_of":null,"excluded_branch_refs":[],"failed_edge":"Bağımsız wider trigger ve ayet-yerel return path yok; citable satır yalnızca desteklenmemiş bir iddia sunuyor.","lane":"global","reason":"B004 doğum sonrası bakım iddiası, bu kaydın kendi içinde bağımsız wider tetikleyici ve odak-yanıt dönüşü göstermediği için kabul edilmedi; daha açık reader kaydı ayrı ve dar bir bulgu olarak korundu.","support_ids":["sup_ca792553b569d4b2c64d"]},{"branch_exclusion_reasons":[],"branch_refs":[],"candidate_id":"cand_50a56c59f80710567f19","duplicate_of":null,"excluded_branch_refs":[],"failed_edge":"Exact anchor, branch, wider trigger ve bounded return path yok; kayıt bu nedenle contained bir finding değil.","lane":"global","reason":"Görünür iz, borç, doğum geçidi ve yatıştırma modellerini tek bir anchorsız HFT envanterinde topluyor; bunlardan hiçbiri packet içinde yeterli taşıyıcı-trigger-relation-payoff zinciri kurmuyor.","support_ids":["sup_88ee58635b26b6a753f8"]},{"branch_exclusion_reasons":[],"branch_refs":[],"candidate_id":"cand_0f07e3f47c7370e0935d","duplicate_of":null,"excluded_branch_refs":[],"failed_edge":"Ayrı bir changed reading/payoff ve ayet-yerel dönüş yolu yok.","lane":"global","reason":"Birden çok modelin meta-özetidir; yeni ve ayrı bir taşıyıcı, wider trigger veya okur getirisi sunmadığı için bağımsız finding değildir.","support_ids":["sup_2ff016a5213d12e0341d"]}],"repair_requests":{"global":[],"macro":[],"micro":[]},"resolved_referrals":[],"schema_version":"commentary-v3-reconciled-findings-v2","scope_assignments":{"global":["locked:global:finding:governing-mercy","locked:global:finding:protected-formation","locked:global:finding:community-bond","locked:global:finding:softening-boundary","locked:global:finding:fragile-emergence","locked:global:finding:breadth-continuance","locked:global:finding:merciful-guidance","locked:global:finding:restorative-renewal","locked:global:finding:mercy-as-revelation","locked:global:finding:ordered-admission","locked:global:finding:embodied-mercy"],"macro":["locked:macro:finding-compassionate-provision","locked:macro:finding-kinship-care","locked:macro:finding-gestation-postpartum","locked:macro:finding-bodily-vulnerability","locked:macro:finding-marriage-conveyance","locked:macro:finding-petition-aid","locked:macro:finding-beneficent-transfer","locked:macro:finding-wildlife-exposure","locked:macro:finding-maturity-markers","locked:macro:finding-household-defense","locked:macro:finding-name-disclosure","locked:macro:finding-nurturing-rule","locked:macro:finding-accounting-frame","locked:macro:finding-dependent-service","locked:macro:finding-guides-maintains","locked:macro:finding-softens-loss","locked:macro:finding-visible-mark","locked:macro:finding-ledger-kinship","locked:macro:finding-womb-pathway","locked:macro:finding-soothing-performance"],"micro":["locked:micro:finding-basmala-ring","locked:micro:finding-mercy-pair-sound","locked:micro:finding-divine-title-register","locked:micro:finding-genitive-chain","locked:micro:finding-mercy-tenderness","locked:micro:finding-lordship-as-care","locked:micro:finding-breadth-to-continuance","locked:micro:finding-adjective-pressure","locked:micro:finding-closure-epithet","locked:micro:finding-title-threshold","locked:micro:finding-kinship-pressure","locked:micro:finding-womb-pressure"]},"unresolved_referrals":[]}
</reconciled_findings_json>

## Exact focus-surface evidence

This packet is a writing-accuracy aid, not permission to add or remove a
finding. Preserve supplied Arabic and transliteration values when used, but
translate analytic English gloss ranges naturally into Turkish and use the
canonical single-span syntax. Never expose analysis/QAC coordinates. Do not
force every row into the prose.

<focus_surface_evidence_json>
{"arabic_uthmani":"ٱلرَّحْمَٰنِ ٱلرَّحِيمِ","primary_floor":{"source_ref":"1:3","target_tokens":[["Merhameti",["1:3:1"]],["sınırsızdır",["1:3:1"]],["merhamet",["1:3:2"]],["edendir",["1:3:2"]]],"text":"Merhameti sınırsızdır, merhamet edendir."},"qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:1:1","qac_word_ref":"1:3:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحْمَٰن","morph_features":"STEM|POS:ADJ|LEM:r~aHoma`n|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:1:2","qac_word_ref":"1:3:1","root_ar":"ر ح م","surface_ar":"رَّحْمَٰنِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"1:3:2:1","qac_word_ref":"1:3:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"رَّحِيم","morph_features":"STEM|POS:ADJ|LEM:r~aHiym|ROOT:rHm|MS|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"1:3:2:2","qac_word_ref":"1:3:2","root_ar":"ر ح م","surface_ar":"رَّحِيمِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["1:3:1:1","1:3:1:2"],["1:3:2:1","1:3:2:2"]],"word_analysis_refs":["1:3:1","1:3:2"],"word_rows":[{"analysis_record_ref":"1:3:1","analytic_gloss_range_en":"definite divine mercy-name in genitive apposition, carrying broad overflowing mercy and continuing the praise-lordship chain from 1:2","analytic_root_gloss_range_en":"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local divine name selects mercy while allowing generative-care image pressure","qac_refs":["1:3:1:1","1:3:1:2"],"root":{"arabic":"ر ح م","transliteration":"r-ḥ-m"},"surface":{"arabic":"ٱلرَّحْمَٰنِ","transliteration":"ar-raḥmāni"}},{"analysis_record_ref":"1:3:2","analytic_gloss_range_en":"definite divine mercy-name in the same genitive pair, carrying enduring and directed mercy as the closing counterpart to the prior breadth","analytic_root_gloss_range_en":"root range centered on mercy, tenderness, and compassion, with related kinship and womb branches; the local second epithet selects sustained mercy within the paired divine-name frame","qac_refs":["1:3:2:1","1:3:2:2"],"root":{"arabic":"ر ح م","transliteration":"r-ḥ-m"},"surface":{"arabic":"ٱلرَّحِيمِ","transliteration":"ar-raḥīmi"}}]}
</focus_surface_evidence_json>

## Micro prose-ready source work

<micro_scope_draft_json>
{"ayah_ref":"1:3","coverage_complete":true,"finding_landings":[{"finding_ref":"locked:micro:finding-basmala-ring","movement_key":"micro:movement-recurrence"},{"finding_ref":"locked:micro:finding-mercy-pair-sound","movement_key":"micro:movement-pair-shape"},{"finding_ref":"locked:micro:finding-divine-title-register","movement_key":"micro:movement-plain-chain"},{"finding_ref":"locked:micro:finding-genitive-chain","movement_key":"micro:movement-plain-chain"},{"finding_ref":"locked:micro:finding-mercy-tenderness","movement_key":"micro:movement-mercy-care"},{"finding_ref":"locked:micro:finding-lordship-as-care","movement_key":"micro:movement-mercy-care"},{"finding_ref":"locked:micro:finding-breadth-to-continuance","movement_key":"micro:movement-pair-shape"},{"finding_ref":"locked:micro:finding-adjective-pressure","movement_key":"micro:movement-plain-chain"},{"finding_ref":"locked:micro:finding-closure-epithet","movement_key":"micro:movement-pair-shape"},{"finding_ref":"locked:micro:finding-title-threshold","movement_key":"micro:movement-recurrence"},{"finding_ref":"locked:micro:finding-kinship-pressure","movement_key":"micro:movement-root-images"},{"finding_ref":"locked:micro:finding-womb-pressure","movement_key":"micro:movement-root-images"}],"friction_notes":[{"note":"Ekli Arapça ifade, iki adın yüzeyde bulunduğunu doğrular; atfedilmiş bölümleme, sözcük konumu, kök, dal ve rol bilgileri tek başına doğrulanmış sayılmaz. Yerel biçim ve sözdizimi kanıtı bunlardan ayrı tutuldu; uygulama çifti ile doğrudan niteleme olasılıkları açık bırakıldı.","type":"hft_boundary"},{"note":"“Merhameti sınırsızdır, merhamet edendir.” temel okuma olarak erişilebilir tutuldu. Genişlik, süreklilik, bakım, ses, tekrar ve kök imgeleri bu önermenin yerine geçirilmeden onun üzerine işlendi.","type":"primary_floor"},{"note":"Yakınlık ve kuşatıcı kap imgeleri keşifsel analojilerdir; “soy bağı” ve “döl yatağı” doğrudan sözlük karşılığı değildir. Organ, gebelik, doğum, ortak ata veya bağ koparma/sürdürme bağlamı ayete eklenmemelidir.","type":"exploratory_boundaries"},{"note":"Her iki yüzey sözcüğü ve kilitli on iki bulgu hareketlere indirildi; etkinleştirilmemiş karşılıklılık, dilek ve tıbbi dal baskıları prose içine taşınmadı.","type":"coverage"}],"identity":{"authoring_request_sha256":"9f5e846a04ba48b7f3fd1bfba4a8b8c8f284d00d5aad34903e5edc469788586e","ayah_ref":"1:3","lane":"micro","reconciled_sha256":"2a68d960df454bd53d7692cca9b5d2c63f5a562fb075d62a75d1c6fafc6dce7f"},"lane":"micro","movements":[{"draft_prose":"Yüzeydeki temel önerme açıktır: “Merhameti sınırsızdır, merhamet edendir.” Fakat bu karşılık, iki adın birbirine nasıl bağlandığını tek başına göstermez. ٱلرَّحْمَٰنِ (ar-raḥmāni; merhameti kuşatan) ile ٱلرَّحِيمِ (ar-raḥīmi; merhamet eden), başlarındaki belirli tanımlık ve genitif biçimleriyle aynı ilahî ad zincirinde 1:2'deki rablık bildirimine bağlanır. Bu nedenle 1:3 yeni ve bağımsız bir cümle gibi başlamaz; önceki bildirimi içeriden niteler. İlk adın kesin ve tanınmış ilahî ad oluşu, onu belirsiz bir sıfat olmaktan çıkarır. İkinci ad ise insan ilişkilerinde de anlaşılabilecek bir merhamet yakınlığı sezdirse bile, bu zincirde sıradan bir insan sıfatına dönüşmez.","finding_refs":["locked:micro:finding-divine-title-register","locked:micro:finding-genitive-chain","locked:micro:finding-adjective-pressure"],"movement_key":"micro:movement-plain-chain"},{"draft_prose":"Bu bağlılık kulakta da duyulur: iki adın aynı kök ses çerçevesini taşıyan başlangıcı, ortak genitif sonlanışı ve yinelenen kesinlik sesi çifti birbirine bağlar; uzun ünlülerin farkı ise iki yarının aynı olmadığını duyurur. Böylece aynı kök tekdüze bir tekrar değil, açılış ve kapanış dengesi kurar. İlk adın genişçe ulaşan merhamet basıncından sonra ikinci adın kalıcı ve yönelmiş bakım olarak gelmesi, merhametin etkin bir esirgemeye ve iyiliğe dönüştüğünü hissettirir. Son konum, bu sürekliliği ayetin iniş noktası yapar. Bu, iki kesin zaman kipi ya da zorunlu bir kronoloji değildir; ikinci adın yakın bir uygulama çifti olarak veya aynı göndergeyi doğrudan niteleyen ad olarak bağlanabilmesi açık kalır.","finding_refs":["locked:micro:finding-mercy-pair-sound","locked:micro:finding-breadth-to-continuance","locked:micro:finding-closure-epithet"],"movement_key":"micro:movement-pair-shape"},{"draft_prose":"Bu ad çifti, “merhamet”i yalnızca soyut bir sonuç olarak bırakmaz: yumuşaklık, karşısındaki varlığa yönelen bir iç yakınlık tonu kazanır. Burada Tanrı'ya insanî duygulanım veya belirli bir acı çeken kişi yüklenmez; öne çıkan, merhametin gözetmeye ve iyilik ulaştırmaya yönelen sonucudur. Bu yüzden 1:2'deki rablık, çıplak sahiplik ya da hüküm olarak değil, yaratılmışlara ulaşan kuşatıcı bakım olarak duyulur. “Merhameti sınırsızdır” sözü kapsamı, “merhamet edendir” sözü ise bu bakımın yerleşik ve etkin oluşunu birlikte taşır.","finding_refs":["locked:micro:finding-mercy-tenderness","locked:micro:finding-lordship-as-care"],"movement_key":"micro:movement-mercy-care"},{"draft_prose":"İki adın bu sıkı dizilişi, 1:1'deki basmala merhamet çiftini de yeniden duyurur. Böylece 1:2'deki övgü ve rablık bildirimi merhametten kopuk bir ara cümle gibi kalmaz; merhametin kurduğu bir halka içinde yer alır. Aynı ilk adın 55:1'de sure açılışında eşik kurması, burada daha geniş bir Kur'anî başlık yankısı hissettirebilir. Ancak bu yankı yalnızca tekrar ve başlık etkisidir: 1:3'ün 1:2'ye bağlı genitif işlevini yönetmez ve daha geniş bir sure yapısı iddiasına dönüşmez.","finding_refs":["locked:micro:finding-basmala-ring","locked:micro:finding-title-threshold"],"movement_key":"micro:movement-recurrence"},{"draft_prose":"Aynı kökün iki ad içinde yinelenmesi, merhameti ayrı ve uzak bir alıcıya verilen iyilikten öte, yakınlığı kurup sürdüren bir bağ gibi sezdiren keşifsel bir basınç da taşır. Burada ortak ata veya gerçek soy bağı söylenmez; bağı sürdürme ya da koparma eylemi de ayette yoktur. Aynı biçim karşıtlığı daha maddi bir imgeye açılabilir: merhamet, canlıyı içinde oluşturan, taşıyan ve besleyen kuşatıcı bir kap gibi, varlığın oluşup dayanmasını mümkün kılan bir ortam olarak düşünülebilir. Bu, “soy bağı” veya “döl yatağı”nı doğrudan çeviri yapmak değildir; organ, gebelik ve doğum bağlamı bulunmadığı için yalnızca yerel biçim düzeninin açtığı sınırlı bir analojidir.","finding_refs":["locked:micro:finding-kinship-pressure","locked:micro:finding-womb-pressure"],"movement_key":"micro:movement-root-images"}],"schema_version":"commentary-v3-scope-prose-draft-v1"}
</micro_scope_draft_json>

## Macro prose-ready source work

<macro_scope_draft_json>
{"ayah_ref":"1:3","coverage_complete":true,"finding_landings":[{"finding_ref":"locked:macro:finding-compassionate-provision","movement_key":"macro:movement_compassionate_provision"},{"finding_ref":"locked:macro:finding-kinship-care","movement_key":"macro:movement_kinship_care"},{"finding_ref":"locked:macro:finding-gestation-postpartum","movement_key":"macro:movement_gestation_postpartum"},{"finding_ref":"locked:macro:finding-bodily-vulnerability","movement_key":"macro:movement_bodily_vulnerability"},{"finding_ref":"locked:macro:finding-marriage-conveyance","movement_key":"macro:movement_marriage_conveyance"},{"finding_ref":"locked:macro:finding-petition-aid","movement_key":"macro:movement_petition_aid"},{"finding_ref":"locked:macro:finding-beneficent-transfer","movement_key":"macro:movement_beneficent_transfer"},{"finding_ref":"locked:macro:finding-wildlife-exposure","movement_key":"macro:movement_wildlife_exposure"},{"finding_ref":"locked:macro:finding-maturity-markers","movement_key":"macro:movement_maturity_markers"},{"finding_ref":"locked:macro:finding-household-defense","movement_key":"macro:movement_household_defense"},{"finding_ref":"locked:macro:finding-name-disclosure","movement_key":"macro:movement_name_disclosure"},{"finding_ref":"locked:macro:finding-nurturing-rule","movement_key":"macro:movement_nurturing_rule"},{"finding_ref":"locked:macro:finding-accounting-frame","movement_key":"macro:movement_accounting_frame"},{"finding_ref":"locked:macro:finding-dependent-service","movement_key":"macro:movement_dependent_service"},{"finding_ref":"locked:macro:finding-guides-maintains","movement_key":"macro:movement_guides_maintains"},{"finding_ref":"locked:macro:finding-softens-loss","movement_key":"macro:movement_softens_loss"},{"finding_ref":"locked:macro:finding-visible-mark","movement_key":"macro:movement_visible_mark"},{"finding_ref":"locked:macro:finding-ledger-kinship","movement_key":"macro:movement_ledger_kinship"},{"finding_ref":"locked:macro:finding-womb-pathway","movement_key":"macro:movement_womb_pathway"},{"finding_ref":"locked:macro:finding-soothing-performance","movement_key":"macro:movement_soothing_performance"}],"friction_notes":[{"note":"HFT kaynaklı adlandırma, kozmolojik yetiştirme, hesap, hizmet, rehberlik, karşıt-sonuç, görünür iz, hesapta yakınlık, geçiş ve yatıştırıcı tekrar okumaları görünür tutuldu. Bunlar yüzey Arapçasının temasından hareket eden, nitelikli bağlam etkinleştirmeleridir; ikincil biçim, kök, dal, rol veya kelime anlamı yüzeyden ayrıca doğrulanmış sayılmaz. Her biri için daha basit tekrar, bağımsız görev, sınıflandırıcı karşıtlık veya yalnızca ritim gibi canlı alternatifler korunur.","note_ref":"macro:friction:hft-boundaries","refs":["locked:macro:finding-name-disclosure","locked:macro:finding-nurturing-rule","locked:macro:finding-accounting-frame","locked:macro:finding-dependent-service","locked:macro:finding-guides-maintains","locked:macro:finding-softens-loss","locked:macro:finding-visible-mark","locked:macro:finding-ledger-kinship","locked:macro:finding-womb-pathway","locked:macro:finding-soothing-performance"],"source_lane":"macro"},{"note":"Döl yatağı, doğum sonrası ağrı, lezyon, hayvanlar, evlilik aktarımı, sahiplik ve hane savunması gibi sahneler somut mekanizma ve karşı-imaj olarak korundu. Bu imgeler odak merhametini doğrudan biyolojiye, zoolojiye, hukuka, sahipliğe veya öfkeye çevirmeden okuma alanını daraltır.","note_ref":"macro:friction:bounded-material-and-social-analogies","refs":["locked:macro:finding-gestation-postpartum","locked:macro:finding-bodily-vulnerability","locked:macro:finding-marriage-conveyance","locked:macro:finding-beneficent-transfer","locked:macro:finding-wildlife-exposure","locked:macro:finding-maturity-markers","locked:macro:finding-household-defense","locked:macro:finding-womb-pathway"],"source_lane":"macro"},{"note":"Bakım, yakınlık ve iyilik hareketleri ile doğum sonrası ağrı, bedensel hasar, açık alanda maruz kalma, savunma, sertleşme ve kaybolma karşı-imajları aynı makro okumada birlikte bırakıldı. Karşıt sahneler merhametin sınırını belirginleştirir; hiçbiri odak çiftinin tek sözlük tanımı haline getirilmedi.","note_ref":"macro:friction:countervailing-outcomes","refs":["locked:macro:finding-compassionate-provision","locked:macro:finding-kinship-care","locked:macro:finding-gestation-postpartum","locked:macro:finding-bodily-vulnerability","locked:macro:finding-wildlife-exposure","locked:macro:finding-household-defense","locked:macro:finding-softens-loss"],"source_lane":"macro"}],"identity":{"authoring_request_sha256":"e14eb18eda21d8ebbf68d09ee9522a11e3942130e3b9372f5282a28e48a2c277","ayah_ref":"1:3","lane":"macro","reconciled_sha256":"2a68d960df454bd53d7692cca9b5d2c63f5a562fb075d62a75d1c6fafc6dce7f"},"lane":"macro","movements":[{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına şu yalın okumayı verir: “Merhameti sınırsızdır, merhamet edendir.” 1:2'nin Rabb çerçevesi, 1:5'teki yardım isteme ve 1:7'deki bağışlanmış iyi oluş, bu merhameti soyut bir duygudan somut bir bakım sahnesine taşır. Bakım verenin bağımlıyı zaman içinde gözetmesi, eksileni onarması, yiyecek ve araç sağlaması ve onu iyi durumda tutması aynı zincirin farklı halkalarıdır. Böylece “Merhamet, bağımlının iyi durumda kalması için zaman içinde koruyan, yardım eden, onaran ve besleyen etkin düzen olarak görünür.” Bu, komşu bağlamın etkinleştirdiği bir bakım imgesidir; odak çiftinin bu dalların tümü için sözlük eşanlamı olduğu ileri sürülmez.","finding_refs":["locked:macro:finding-compassionate-provision"],"movement_key":"macro:movement_compassionate_provision"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:1 ve 1:3'teki merhamet adları; yakın soy, edinilmiş akrabalık, foster çocuk ve bakım veren sahneleriyle birlikte okunduğunda, geçici acımadan uzun süre taşınan bir ilişkiye açılır. Bir çocuğun bir bağ ağına ait olması, bu bağı sürdüren kişinin onu yetiştirme ve koruma sorumluluğunu üstlenmesiyle canlı bir bakıma dönüşür. Böylece “Merhamet, yakın soy veya edinilmiş akrabalık içinde sürdürülen bakım ve koruma sorumluluğu olarak keskinleşir.” Aile ve foster imgeleri bağlamsal etkinleştirmedir; burada literal soy, üvey aile düzeni veya bir hukuk kuralı kurulmaz.","finding_refs":["locked:macro:finding-kinship-care"],"movement_key":"macro:movement_kinship_care"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü taşır. Döl yatağının koruyucu bir kap olması, yeni doğmuş bir koyunun ortaya çıkışı ve doğum sonrasında süren ağrı sahnesi, merhameti yalnızca içeride saklayan bir sığınak olmaktan çıkarır. Taşıma, dünyaya getirme ve geçişten sonra kalan kırılganlığı gözetme aynı sürecin birbirini izleyen aşamalarıdır. Böylece “Merhamet, yaşamı taşıyan koruyucu oluşum ve doğumdan sonra süren bedensel kırılganlıkla birlikte düşünülen süreç olur.” Bu, keşifsel bir maddi analojidir; döl yatağı dalı genel beden, literal biyoloji veya odak ayetin tek anlamı yapılmaz.","finding_refs":["locked:macro:finding-gestation-postpartum"],"movement_key":"macro:movement_gestation_postpartum"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. Döl yatağına ilişkin hastalık ve ağrı imgesi, üst dudaktaki görünür yarık, göz çevresindeki şişlik ve organa yerleşen ağrıyla yan yana geldiğinde merhametin pürüzsüz bir yumuşaklık olmadığını gösterir. Koruma, hasarın teşhis edilebildiği ve acının bedende bir yere yerleştiği yerde maliyet kazanır. Böylece “Merhamet, lezyon, şişme ve organa yerleşen ağrı karşısında korunması gereken kırılganlığı hesaba katan maliyetli bakım olarak görünür.” Bu daraltılmış, keşifsel bir karşı-imajdır; odak merhameti lezyon veya hastalıkla eşitlenmez.","finding_refs":["locked:macro:finding-bodily-vulnerability"],"movement_key":"macro:movement_bodily_vulnerability"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü kurar. Evlilik sözleşmesi, yakına gönderilen hediye ve gelinin eşine götürülmesi sahneleri, yakınlığı yalnızca duyulan bir his değil, tarafları yeni bir ilişki alanına taşıyan bir hareket olarak görünür kılar. Bağ kurulur, bir taraf diğerine doğru iletilir ve hediyenin sıcaklığı bu geçişi ilişki içinde anlamlı kılar. Böylece “Merhamet, bir bağı kuran, tarafları yeni bir ilişki alanına taşıyan ve yakınlık içinde hediyeleşen aktarım hareketi olarak görünür.” Bu keşifsel bir sosyal analojidir; marriage, ownership veya conveyance odak ayete hukuki hüküm olarak aktarılmaz.","finding_refs":["locked:macro:finding-marriage-conveyance"],"movement_key":"macro:movement_marriage_conveyance"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:5'teki إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ (yalnız sana kulluk eder ve yalnız senden yardım isteriz) ile 1:6'daki ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ (bizi dosdoğru yola ilet) birlikte düşünüldüğünde, merhamet talebe cevap veren bir ilişki içinde belirir. Hizmet eden bağımlı yardım ister; rehberlik yönü, yol geçişi ve doğruluk ise yardımın nereye vardığını gösterir. Böylece “Merhamet, hizmet eden ve yardım isteyen bağımlının yön, yol ve doğruluk talebine cevap veren asimetrik ilişki olarak görünür.” Buradaki karşılıklılık eşitlik veya eşit değişim değildir; dua ve rehberlik bağlamı odak kökünün sözlük karşılığı yapılmadan kullanılır.","finding_refs":["locked:macro:finding-petition-aid"],"movement_key":"macro:movement_petition_aid"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü bildirir. 1:4'teki sahiplik, 1:6'daki yön ve 1:7'deki bağışlanmış iyi durum, merhametin verende kalan bir niyet değil, bir alıcıya ulaşan bir iyilik olduğunu görünür kılar. Yakına gönderilen hediye, başka birinin yararına geçen değer ve alıcının durumundaki iyileşme, veren, aktarım ve sonuç sırasını kurar. Böylece “Merhamet, verenin içinde kalan tutum değil, hediye ve yarar olarak başka birinin durumuna geçen aktarım olur.” Aktarım burada bir analojidir; hukuki sahiplik veya zorunlu karşılık odağa taşınmaz.","finding_refs":["locked:macro:finding-beneficent-transfer"],"movement_key":"macro:movement_beneficent_transfer"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. Döl yatağı ve yeni doğum, devekuşu gibi açık alan hayvanları, yırtıcı kuş ve erkek sırtlan ile sahipsiz hayvan görüntüsü yan yana geldiğinde kapalı koruma ile açık dünyanın riski aynı sahneye girer. Canlı önce korunan bir oluşum içinde meydana gelir; dışarı çıktığında sınıflanma, kaybolma ve av olma ihtimaliyle karşılaşır. Böylece “Merhamet, canlıyı oluşturan kapalı koruma ile onun dışarı çıktıktan sonra kaybolma ve yırtıcılarla karşılaşma riskini aynı sahnede görünür kılar.” Bu, keşifsel bir hayvan karşı-imajıdır; zoolojik anlam veya bu dalların odak sıfatlarının sözlük karşılığı yapılmaz.","finding_refs":["locked:macro:finding-wildlife-exposure"],"movement_key":"macro:movement_wildlife_exposure"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü verir. Döl yatağı, bedendeki ayırt edici işaret, orta yaş, yerleşmiş güç ve bedensel kıl gibi sahneler, oluşumu tek bir başlangıç anı değil, biçim, işlev ve yaş üzerinden izlenebilen bir gelişim olarak kurar. Bakımın sonucu, bağımlının zaman içinde olgunlaşması ve durumunun dışarıdan okunabilir hale gelmesidir. Böylece “Merhamet, yaşamı üreten ve onu görünür işaretlerle ayırt edilebilir, orta yaşa ulaşmış ve dengeli güçlü bir duruma getiren gelişim süreci olarak okunur.” Bu keşifsel bir gelişim imgesidir; odak sıfatları biyolojik terim veya sınıflandırma etiketi değildir.","finding_refs":["locked:macro:finding-maturity-markers"],"movement_key":"macro:movement_maturity_markers"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. Yakın soy ve topluluk, aileye yönelik koruyucu kıskançlık, bedensel sağlamlık ve kaş çatma sahneleri merhametin içeride tuttuğu bağ ile dışarıya karşı çizdiği sınırı birlikte gösterir. Bir çevreyi korumak, yalnızca yumuşak davranmak değil, ihlal karşısında direnç gösterecek bir kapasite oluşturmaktır. Böylece “Merhamet, bağlı olunan çevreyi içeriden koruyan ve dışarıdan gelen ihlale karşı sınır ve savunma kapasitesi oluşturan bağ olarak görünür.” Savunma ve öfke burada karşı-imajdır; merhamet öfke, kıskançlık veya sertlikle eşanlamlı yapılmaz.","finding_refs":["locked:macro:finding-household-defense"],"movement_key":"macro:movement_household_defense"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü söyler. 1:1'deki بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (Allah'ın adıyla, çok merhametli ve merhamet eden) adlandırma kuruluşu ve 1:3'teki tam tekrar birlikte okunduğunda, iki sıfat yalnızca bir niteliği bildirmekle kalmaz. Adı anılan varlığa yaklaşma, merhamet çiftinin yeniden çağrılmasıyla mümkün olan bir eşik gibi duyulur. Böylece “1:1'deki adlandırma kuruluşu ve tam tekrar, merhamet çiftini adı anılan varlığa yaklaşmanın çağrılmış eşiği olarak görmeyi mümkün kılar.” Bu keşifsel öneri, basit bir litürjik vurgu veya tekrar etkisi olarak da okunabilir; metnin Arapça yüzeyi tekrar temasını sağlar, fakat ikincil ad/işaret dallarını, hedef biçimini veya etimolojiyi ayrıca kanıtlamaz.","finding_refs":["locked:macro:finding-name-disclosure"],"movement_key":"macro:movement_name_disclosure"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:2'nin hemen önceki lordluk ve çoğul âlemler çerçevesi, döl yatağının koruyucu oluşumunu tekil bir sığınaktan çok, varlık alanlarını besleyen ve onarımla tamamlayan bir emeğe doğru genişletir. Gelişme, bakım ve tamamlanma hazır bir sonuca değil, sürdürülmesi gereken kozmolojik bir işe işaret eder. Böylece “1:2'nin hemen önceki lordluk ve çoğul âlemler çerçevesinde merhamet, bağımlı varlık alanlarını besleyip onarımla tamamlayan kozmolojik gelişim emeği olarak genişler.” Bu okuma orta güvenli, keşifsel bir bağlam etkinleştirmesidir; odak çiftinin döl yatağı imgesi bütün HFT dallarının veya biyolojik bir sürecin sözlük karşılığı değildir ve Arapça yüzey ikincil biçimsel rolleri tek başına doğrulamaz.","finding_refs":["locked:macro:finding-nurturing-rule"],"movement_key":"macro:movement_nurturing_rule"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü kurar. Hemen ardından gelen مَٰلِكِ يَوْمِ ٱلدِّينِ (hesap gününün sahibi) sahiplik ve hesap verme sahnesini açtığında, merhamet yargının silinmesi olarak değil, hesabın nasıl idare edildiğini belirleyen önceki tutum olarak duyulur. Hesap vardır; fakat onu tutan elin niteliği de önceki merhamet çiftiyle çerçevelenir. Böylece “1:4'ün sahiplik ve hesap verme sahnesi, merhameti yargının karşıtı değil, hesabın nasıl tutulduğunu önceleyen idare edici nitelik olarak gösterir.” Bu hareket bir yönetim okumasıdır, hukuk doktrini değildir; Arapça yüzey teması hedef morfolojisini bağımsız olarak kanıtlamaz ve çözümlenmemiş zaman ya da muhasebe dalları buraya eklenmez.","finding_refs":["locked:macro:finding-accounting-frame"],"movement_key":"macro:movement_accounting_frame"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:5'teki إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ (yalnız sana kulluk eder ve yalnız senden yardım isteriz), yakınlık imgesini hizmet ve açık yardım talebiyle birleştirir. Bağımlı yalnızca iyiliğin pasif alıcısı değildir; cevap verir, hizmet eder ve ihtiyacını bağın sahibine yöneltir. Böylece “1:5'teki hizmet ve yardım isteme, merhameti bağımlının cevap verip yardım talep ettiği asimetrik ilişki olarak görünür kılar.” Bu karşılıklılık eşit bir alışveriş değildir; hizmet ve yardım bağımsız görevler olarak da okunabilir, ayrıca bu yüzey temasından hedef biçimi veya odak kökünün sözlük anlamı çıkarılamaz.","finding_refs":["locked:macro:finding-dependent-service"],"movement_key":"macro:movement_dependent_service"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü verir. 1:6'daki ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ (bizi dosdoğru yola ilet) yön gösteren rehberliği, geçilebilir yolu ve dengeli doğruluğu aynı talepte toplar. Merhamet burada tek seferlik bir yumuşaklık değil, yolcuyu nereye gideceği konusunda yönlendiren ve ilerlerken dağılmasını önleyen sürekli bir bakım altyapısıdır. Böylece “1:6'nın yol ve doğruluk talebiyle merhamet, yön gösteren ve yolcuyu dengede tutan sürekli altyapı olarak görünür.” Bu, kaynak nitelemesi güçlü olsa da bağlamın kurduğu bir etkinleştirmedir; Arapça yüzey teması hedef morfolojisini, ikincil kökleri veya dalların rollerini tek başına doğrulamaz ve ifade sözlükte “yol” demek değildir.","finding_refs":["locked:macro:finding-guides-maintains"],"movement_key":"macro:movement_guides_maintains"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:7'deki bağışlanmış iyi durum ile dışlanan sonuçların, sertliğin ve yolunu kaybetmenin aynı yol kuruluşunda yan yana gelmesi merhametin karşıtını görünür kılar. Merhamet yalnız olumlu bir nitelik değil, canlıyı yumuşak, yönlendirilebilir ve tutulabilir halde bırakan bir ortamdır. Böylece “1:7'deki bağış ve dışlanan sonuçlar, merhameti yumuşaklığı koruyan, sertleşme ve yolunu kaybetmeye karşı tutan ortam olarak gösterir.” Bu, orta güvenli ve keşifsel bir daraltmadır; karşıtlık yalnız sınıflandırıcı bir ayrım olarak da okunabilir, bu yüzden merhamet sertlik veya kaybolma karşıtlarının sözlük karşılığı yapılmaz.","finding_refs":["locked:macro:finding-softens-loss"],"movement_key":"macro:movement_softens_loss"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü bildirir. 1:1'deki adlandırma ve 1:3'teki eksiksiz tekrar, bu merhamet içeriğinin ilişkilerde ve eylemlerde tanınabilir bir iz bırakabileceğini düşündürür. Okur böylece niteliği yalnızca duyulan bir söz olarak değil, bir işin kimden ve hangi tarzda geldiğini sezdiren görünür bir imza olarak arayabilir. Böylece “1:1'deki adlandırma ve tekrar, merhametin eylem ve ilişkilerde tanınabilir bir ilahî imza olarak okunmasını önerebilir.” Bu, adlandırma içindeki baskın olmayan bir işaret analojisinden doğan keşifsel bir olasılıktır; basit tekrar veya litürjik vurgu alternatifi açıktır ve bu okuma etimoloji ya da sözlük karşılığı değildir.","finding_refs":["locked:macro:finding-visible-mark"],"movement_key":"macro:movement_visible_mark"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. 1:4'ün sahiplik ve hesap çerçevesi, yakınlık imgesini iz bırakmayan gönüllü bir yarardan, korunması veya kopması önem taşıyan kalıcı bir bağa doğru daraltır. Yakınlık bir ilişki kurduğu anda devamlılık ve sorumluluk iddiası üretir; hesabın sahnesi bu ilişkinin sonucunu görünür kılar. Böylece “1:4'ün hesap çerçevesinde merhamet, korunması veya kopması sonuç doğurabilecek yakınlık benzeri kalıcı bir bağ olarak okunabilir.” Bu, kinship ile hesap arasında keşifsel ve alanlar arası bir analojidir; finansal borç doktrini, hukukî yükümlülük veya hedef morfolojisi kurulmaz, çözülmemiş borç dalı da bu okumaya eklenmez.","finding_refs":["locked:macro:finding-ledger-kinship"],"movement_key":"macro:movement_ledger_kinship"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” hükmünü taşır. Döl yatağının yaşamı içeride oluşturması ve doğum sonrası ağrının bu oluşuma bir maliyet yüklemesi, 1:6'daki ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ (bizi dosdoğru yola ilet) yol ve diklik yüzeyiyle birleşir. Koruma, geçiş ve varış arasında bir sıra kurulur: bağımlı içeride tutulur, zor bir eşikten geçirilir ve sonunda dengeli duruşa taşınır. Böylece “Merhamet, hayatı koruyup oluşturan ve sonra onu maliyetli bir geçitten geçirerek dengeli, dik bir duruma ulaştıran süreç olarak tasarlanabilir.” Bu keşifsel bir maddi analojidir; sınırlı geçişe dair çözülmemiş dal ve hedef morfolojisi dışarıda tutulur, merhamet “yol” veya biyolojik oluşumla özdeşleştirilmez.","finding_refs":["locked:macro:finding-womb-pathway"],"movement_key":"macro:movement_womb_pathway"},{"draft_prose":"Bu ayetteki ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (ar-raḥmāni ar-raḥīmi; çok merhametli ve merhamet eden) çifti tek başına “Merhameti sınırsızdır, merhamet edendir.” der. İki adın sesli tekrarı, hemen ardından gelen 1:6'daki rehberlik talebinden önce konuşanın yön istemeye hazırlanmasını sağlayan bir ritim gibi duyulabilir. Merhamet hakkında konuşulmaz yalnızca; bu tekrar, bağımlı konuşanı güven içinde istemeye taşıyan bir zemin de kurabilir. Böylece “Çiftin ritmik tekrarı, 1:6'daki rehberlik talebinden önce bağımlı konuşanı güven içinde istemeye hazırlayan yatıştırıcı edim olarak düşünülebilir.” Bu keşifsel bir performatif olasılıktır; tekrar yalnızca ritmik veya litürjik vurgu olarak da anlaşılabilir, bu nedenle odak çiftinin sözlük gloss'u veya rehberlik kökünün biçimsel çözümlemesi değildir.","finding_refs":["locked:macro:finding-soothing-performance"],"movement_key":"macro:movement_soothing_performance"}],"schema_version":"commentary-v3-scope-prose-draft-v1"}
</macro_scope_draft_json>

## Global prose-ready source work

<global_scope_draft_json>
{"ayah_ref":"1:3","coverage_complete":true,"finding_landings":[{"finding_ref":"locked:global:finding:governing-mercy","movement_key":"global:movement:governing-mercy"},{"finding_ref":"locked:global:finding:protected-formation","movement_key":"global:movement:protected-formation"},{"finding_ref":"locked:global:finding:community-bond","movement_key":"global:movement:community-bond"},{"finding_ref":"locked:global:finding:softening-boundary","movement_key":"global:movement:softening-boundary"},{"finding_ref":"locked:global:finding:fragile-emergence","movement_key":"global:movement:fragile-emergence"},{"finding_ref":"locked:global:finding:breadth-continuance","movement_key":"global:movement:breadth-continuance"},{"finding_ref":"locked:global:finding:merciful-guidance","movement_key":"global:movement:merciful-guidance"},{"finding_ref":"locked:global:finding:restorative-renewal","movement_key":"global:movement:restorative-renewal"},{"finding_ref":"locked:global:finding:mercy-as-revelation","movement_key":"global:movement:mercy-as-revelation"},{"finding_ref":"locked:global:finding:ordered-admission","movement_key":"global:movement:ordered-admission"},{"finding_ref":"locked:global:finding:embodied-mercy","movement_key":"global:movement:embodied-mercy"}],"friction_notes":[{"note":"Target morphology and target lexical analysis were not supplied. Connection judgments use only the exact target Arabic, supplied source notes, and bounded focus-side relations; no missing morphology is invented.","source_lane":"global"},{"note":"The four B004 facets are not all activated: only F001 has a bounded contact. F002 and F003 remain no_independent_trigger, while the accepted B004 finding is explicitly analogical and narrow.","source_lane":"global"},{"note":"The foster/step-family and stagewise-nurture branches are cross-root or source-image carriers. Their contributions remain visible, but they are not lexical identities with the focus r-ḥ-m forms.","source_lane":"global"},{"note":"Reciprocal nominations and reciprocal counterevidence were judged separately. Counterevidence at 8:75, 19:87, 33:6 and 60:3 remains visible; where exact target wording exposed a bounded relation, the result was narrowed rather than treated as a veto.","source_lane":"global"},{"note":"Repeated formula targets such as the 26:104 family and 17:110 are represented only where the same mechanism and payoff are already covered; generic naming-only rows without a changed reading are rejected.","source_lane":"global"},{"note":"The unanchored HFT items retain their support in candidate and support ledgers when narrowed, but their source qualifications prevent them from becoming an uncontained surah thesis.","source_lane":"global"}],"identity":{"authoring_request_sha256":"1b254155c6c0edd2f327b03b97e6c8b4decec8d01f3a9405feaecaa68532486f","ayah_ref":"1:3","lane":"global","reconciled_sha256":"2a68d960df454bd53d7692cca9b5d2c63f5a562fb075d62a75d1c6fafc6dce7f"},"lane":"global","movements":[{"draft_prose":"Ayet tek başına okunduğunda iki ilahi merhamet adı, genel bir iyilik ve yakınlık bildirimi olarak kalabilir. Fakat 1:2'deki rablik ve bakım ile 1:4'teki hesap ve hüküm yan yana düşünülünce, 20:5, 21:112, 18:58, 44:6 ve 78:38'deki rablik, hüküm, izin ve gecikmiş hesap sahneleri bu iki adın yerini açıklığa kavuşturur. Merhamet burada yönetimi yalnızca yumuşatan bir ek değil, bakımın egemenlik ve hesapla nasıl birlikte işlediğini belirleyen ara kip olarak görünür; böylece 1:3'teki adlar övgüden hesap düzenine geçişte hükmün karşıtı olmayan bir menteşe olur.","finding_refs":["locked:global:finding:governing-mercy"],"movement_key":"global:movement:governing-mercy"},{"draft_prose":"Tek başına ayet, merhameti ilahi bir nitelik olarak bildirir; koruma, oluşum ve devamlı destek süreçleri açıkça adlandırılmaz. 3:6, 4:2, 12:18, 12:56, 12:64, 16:7, 17:24, 18:16, 18:82, 22:65 ve 55:3 çevresindeki döl yatağı, yetim ve küçüklerin bakımı, taşınan yük ve aşama aşama gelişme imgeleri bir araya gelince merhamet, bağımlı oluşumu içine alan ve hareketi boyunca destekleyen bir bakım alanına dönüşür. Bu, rahmet adlarının döl yatağı anlamına geldiği yönünde literal bir iddia değildir; rablik ve yardım alanları yalnızca analojik taşıyıcılardır. Yine de iki adın etkin iyilik yönü, korunmuş bir kap ile sürdürülen desteği birlikte düşünmeyi mümkün kılar.","finding_refs":["locked:global:finding:protected-formation"],"movement_key":"global:movement:protected-formation"},{"draft_prose":"Tek başına ayet, merhamet adlarını söyler; konuşanların birbirleriyle veya daha önce iyilik görmüş kişilerle nasıl bağlandığını belirtmez. 1:5-1:7'deki biz, ibadet, yol talebi ve iyilik görmüşler dizisi; 4:1, 4:23, 7:151, 8:75, 23:109, 47:22, 49:10, 59:10 ve 60:3'teki soy, rahim, üvey aile, kardeşlik, bakım ve topluluk duası sahneleriyle birlikte korunan bir aidiyet sürekliliği kazanır. Böylece rahmet, yol isteyen topluluğu daha önce yol almış kişilerle ilişkilendiren bir bağ gibi okunur. Soy ve rahim imgeleri burada odak adlarının literal anlamı ya da belirli bir soy garantisi değildir; bağın korunabileceği gibi kesilebileceği de görünür. Bu sınırlama içinde iki ad, ayetin tekil bir övgüsünü ortak bir yöneliş içinde konuşan bir biz'e açar.","finding_refs":["locked:global:finding:community-bond"],"movement_key":"global:movement:community-bond"},{"draft_prose":"Tek başına ayet, merhameti olumlu bir ilahi nitelik olarak sunar; bunun sertlik, sapma veya nankörlükle karşıtlığı görünmezdir. 1:7'deki öfke ve sapma karşıtlığı ile 23:75-76, 7:57, 10:21, 17:100, 19:69, 29:23, 41:50 ve 42:48'deki rahatlama sonrasında bozulan durumlar, merhameti sertleşmeye ve kayba karşı koruyucu bir yumuşaklık olarak gösterir. Bu yumuşaklık yolu yalnızca sert bir hüküm yüzeyine dönüşmekten korur, fakat merhamet gören kişinin yönelişini zorla düzeltmez ve sonucu otomatik bir bağışlanmaya çevirmez. Öfke, sapma ve nankörlük odak adlarının sözlük anlamına eklenmez; bunlar iki adın daha geniş karşıtlık içinde neyi görünür kıldığını açıklayan tetikleyicilerdir.","finding_refs":["locked:global:finding:softening-boundary"],"movement_key":"global:movement:softening-boundary"},{"draft_prose":"Tek başına ayet, doğum sonrası hastalık veya yeni ortaya çıkanın kırılganlığı hakkında bir şey söylemez. 3:6'daki rahimlerde biçimlenme sahnesi, 1:2-1:6 arasındaki bağımlılık ve gelişme geçişiyle birlikte düşünüldüğünde, merhamet yeni bir başlangıçtan sonra henüz sağlamlaşmamış olanı onaran sınırlı bir bakım imgesine taşınabilir. Bu, döl yatağı hastalığını rahmet adlarının sözlük karşılığı yapmak değildir; morfoloji ve klinik ayrıntı buradan çıkarılamaz. Keşifsel analoji, yalnızca yön arayan ve desteğe ihtiyaç duyan bir varlığın başlangıç sonrasındaki kırılganlığını ayetin iki adındaki etkin esirgeme ile yan yana getirir.","finding_refs":["locked:global:finding:fragile-emergence"],"movement_key":"global:movement:fragile-emergence"},{"draft_prose":"Tek başına ayet, iki adın tekrarı nedeniyle yoğunlaştırılmış bir niteleme gibi okunabilir. 57:28'deki iki pay rahmet ve yürüyen ışık, 7:156'daki her şeyi kuşatan fakat düzenlenen rahmet ve 17:110'daki adlandırma ile dua dengesi, bu tekrarı yalnızca yinelenen bir betimleme olmaktan çıkarır: rahmet hem genişler hem de ulaştığı yerde sürer. Böylece çift ad, kapsamın genişliği ile devam eden ve yönelen iyiliğin birlikte tutulduğu bir düzeni düşündürür. Bu, biçimlerin zorunlu ve teknik bir sarf ayrımı değildir; ayrım keşifsel bir analitik imkân olarak korunur, ayetin iki adını tek başına kesin bir morfolojik teoriye dönüştürmez.","finding_refs":["locked:global:finding:breadth-continuance"],"movement_key":"global:movement:breadth-continuance"},{"draft_prose":"Tek başına ayet, merhamet ile yol, doğru istikamet veya ışık arasındaki işlevsel bağlantıyı kurmaz. 18:10, 22:24, 3:101, 4:175, 3:8, 27:63, 33:43, 57:28 ve 7:204 çevresindeki hidayet, doğru yol, iyi söz, ışık, dinleme ve kalplerin sabitlenmesi sahneleri, rahmeti yön arayana yalnızca bir imkân vermek değil, onu doğru istikamete yöneltip orada desteklemek olarak görünür kılar. Bu dönüş, 1:5-1:6'daki kulluk, yardım ve yol dileğinde yeniden ayetin içine döner; rahmet, yön arayan bağımlı topluluğun dileğinde işleyen bir yardım olur. Yine de bu nedensellik ayetin gramerinin doğrudan söylediği bir sözlük anlamı değildir; geniş bağlamdan çıkarılan yorumlayıcı bir sonuçtur ve armağan imgesi de yalnızca analojik bir taşıyıcıdır.","finding_refs":["locked:global:finding:merciful-guidance"],"movement_key":"global:movement:merciful-guidance"},{"draft_prose":"Tek başına ayet, merhametin yağmur, diriltme, iyileşme veya kaybın geri verilmesi gibi somut sonuçlarını belirtmez. 7:57, 21:84, 30:46, 30:50, 36:52, 38:43 ve 42:28'deki yağmur, ölü toprağın canlanması, sıkıntının kaldırılması ve ailenin geri verilmesi sahneleri, rahmeti başlangıçta verilmiş bir nitelik olmanın ötesinde, kayıp veya sıkıntıdan sonra hayatı yeniden açan etkin bir yenileme olarak görünür kılar. Bu sahneler iki adın acınan kişiye iyilik ulaştıran yönüne geri döner; yağmur ve diriltme ise odak adlarının literal anlamı değil, daha geniş bağlamdaki sonuç imgeleridir. Okuma böylece merhametin yeniden kurucu hareketini görünür kılar, fakat onu ayetin tek başına söylediği bir doğa yasasına dönüştürmez.","finding_refs":["locked:global:finding:restorative-renewal"],"movement_key":"global:movement:restorative-renewal"},{"draft_prose":"Tek başına ayet, iki rahmet adını bir kitap, öğretim, iletişim veya uyarının verilmesiyle bağlamaz. 41:2, 46:12, 16:64, 17:82, 17:87, 18:65, 28:43, 28:46, 28:86, 29:51, 41:32, 45:20 ve 55:2-4'te kitabın indirilmesi, açıklanması, öğretilmesi, şifa ve beyan olarak ulaştırılması, rahmeti insanlara bilgi ve yön veren bir gönderim biçimi olarak görünür kılar. Böylece ayetteki iki adın etkin iyilik yönü, anlamın ve uyarının ulaştırılması üzerinden yeniden okunur. Vahiy ve öğretim burada daha geniş bağlamın sonuçlarıdır; odak adlarının sözlük karşılığı değildir ve her alıcının aynı tepkiyi vereceği anlamına gelmez.","finding_refs":["locked:global:finding:mercy-as-revelation"],"movement_key":"global:movement:mercy-as-revelation"},{"draft_prose":"Tek başına ayet, merhametin kapsamlı olması ile seçme, izin, sonuç ve hesap arasındaki düzeni açıklamaz. 6:12, 6:54, 6:147, 7:49, 7:156, 9:21, 9:99, 17:57, 18:98, 20:109, 24:10, 29:21, 35:2, 40:9, 42:8, 45:30, 48:25 ve 76:31'deki kabul, giriş, şefaat, bağışlama ve koruma sahneleri, rahmetin izin, yöneliş veya sonuç düzeni içinde işlediğini gösterir. Böylece her şeyi kuşatan rahmet, sorumluluğu askıya alan sınırsız bir kabul değil, kime ve nasıl ulaşacağı yönetilen bir giriş biçimi olur. 1:3'teki iki adın bakım ile hesap arasındaki konumu bu okumaya geri döner: merhamet hükmün alternatifi değil, hüküm ve egemenliğin nasıl icra edildiğini belirleyen bir kip olarak görünür.","finding_refs":["locked:global:finding:ordered-admission"],"movement_key":"global:movement:ordered-admission"},{"draft_prose":"Tek başına ayet, merhamet adlarının insanlar arası söz, uzlaşma, eşlik veya ortak dayanışmaya nasıl dönüştüğünü göstermez. 3:159, 9:61, 9:128, 11:90, 17:28, 24:21, 25:63, 30:21, 36:58, 57:27, 59:10 ve 60:12'de kardeşleri barıştırma, yumuşak konuşma, istişare, eşler arasındaki sükûn, toplu sabır ve karşılıklı merhamet sahneleri, ilahi rahmetin toplumsal davranışta bir karşılık bulabileceğini açar. Böylece 1:3'teki iki ad, yalnızca yukarıdan bildirilen bir nitelik değil, söz ve ilişki düzeninde yumuşaklık, uzlaşma ve karşılıklı bakım üreten bir eksen olarak yeniden duyulur. Bu toplumsal davranış odak sıfatlarının doğrudan sözlük karşılığı değildir; karşılıklı kullanım da ilahi adların karşılıklı olduğu iddiası değil, daha geniş bağlamda kurulan sınırlı bir uygulamadır.","finding_refs":["locked:global:finding:embodied-mercy"],"movement_key":"global:movement:embodied-mercy"}],"schema_version":"commentary-v3-scope-prose-draft-v1"}
</global_scope_draft_json>
