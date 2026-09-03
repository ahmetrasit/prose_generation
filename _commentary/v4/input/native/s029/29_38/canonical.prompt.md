# Commentary v4 canonical merge writer

You are the fresh canonical writer for **29:38**. Three independent
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

- prose: `_commentary/v4/raw/native/s029/29_38/29_38.prose.tr.md`
- evidence: `_commentary/v4/raw/native/s029/29_38/29_38.evidence.tr.md`
- findings index: `_commentary/v4/raw/native/s029/29_38/29_38.index.tr.md`
- friction: `_commentary/v4/raw/native/s029/29_38/29_38.friction.tr.md`

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

<focus_surface_json sha256="e52d6fa99ae313a3c08d32fde1cd57a9632042058358a824ab6e33ce50a884a8">
{"arabic_uthmani":"وَعَادًۭا وَثَمُودَا۟ وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ ۖ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ وَكَانُوا۟ مُسْتَبْصِرِينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:1:1","qac_word_ref":"29:38:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَاد2","morph_features":"STEM|POS:PN|LEM:EaAd2|ROOT:Ewd|ACC","morpheme_role":"STEM","pos":"PN","qac_ref":"29:38:1:2","qac_word_ref":"29:38:1","root_ar":"ع و د","surface_ar":"عَادًا"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:2:1","qac_word_ref":"29:38:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ثَمُود","morph_features":"STEM|POS:PN|LEM:vamuwd|ACC","morpheme_role":"STEM","pos":"PN","qac_ref":"29:38:2:2","qac_word_ref":"29:38:2","root_ar":"","surface_ar":"ثَمُودَا۟"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:3:1","qac_word_ref":"29:38:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"29:38:3:2","qac_word_ref":"29:38:3","root_ar":"","surface_ar":"قَد"},{"lemma_ar":"تَبَيَّنَ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tabay~ana|ROOT:byn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"29:38:4:1","qac_word_ref":"29:38:4","root_ar":"ب ي ن","surface_ar":"تَّبَيَّنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"29:38:5:1","qac_word_ref":"29:38:5","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"29:38:5:2","qac_word_ref":"29:38:5","root_ar":"","surface_ar":"كُم"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"29:38:6:1","qac_word_ref":"29:38:6","root_ar":"","surface_ar":"مِّن"},{"lemma_ar":"مَسْكَن","morph_features":"STEM|POS:N|LEM:masokan|ROOT:skn|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"29:38:7:1","qac_word_ref":"29:38:7","root_ar":"س ك ن","surface_ar":"مَّسَٰكِنِ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"29:38:7:2","qac_word_ref":"29:38:7","root_ar":"","surface_ar":"هِمْ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:8:1","qac_word_ref":"29:38:8","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"زَيَّنَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:zay~ana|ROOT:zyn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"29:38:8:2","qac_word_ref":"29:38:8","root_ar":"ز ي ن","surface_ar":"زَيَّنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"29:38:9:1","qac_word_ref":"29:38:9","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"29:38:9:2","qac_word_ref":"29:38:9","root_ar":"","surface_ar":"هُمُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"29:38:10:1","qac_word_ref":"29:38:10","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"شَيْطَٰن","morph_features":"STEM|POS:PN|LEM:$ayoTa`n|ROOT:$Tn|M|NOM","morpheme_role":"STEM","pos":"PN","qac_ref":"29:38:10:2","qac_word_ref":"29:38:10","root_ar":"ش ط ن","surface_ar":"شَّيْطَٰنُ"},{"lemma_ar":"عَمَل","morph_features":"STEM|POS:N|LEM:Eamal|ROOT:Eml|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"29:38:11:1","qac_word_ref":"29:38:11","root_ar":"ع م ل","surface_ar":"أَعْمَٰلَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"29:38:11:2","qac_word_ref":"29:38:11","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:12:1","qac_word_ref":"29:38:12","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"صَدَّ","morph_features":"STEM|POS:V|PERF|LEM:Sad~a|ROOT:Sdd|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"29:38:12:2","qac_word_ref":"29:38:12","root_ar":"ص د د","surface_ar":"صَدَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"29:38:12:3","qac_word_ref":"29:38:12","root_ar":"","surface_ar":"هُمْ"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"29:38:13:1","qac_word_ref":"29:38:13","root_ar":"","surface_ar":"عَنِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"29:38:14:1","qac_word_ref":"29:38:14","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"سَبِيل","morph_features":"STEM|POS:N|LEM:sabiyl|ROOT:sbl|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"29:38:14:2","qac_word_ref":"29:38:14","root_ar":"س ب ل","surface_ar":"سَّبِيلِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"29:38:15:1","qac_word_ref":"29:38:15","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"كَانَ","morph_features":"STEM|POS:V|PERF|LEM:kaAna|ROOT:kwn|SP:kaAn|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"29:38:15:2","qac_word_ref":"29:38:15","root_ar":"ك و ن","surface_ar":"كَانُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"29:38:15:3","qac_word_ref":"29:38:15","root_ar":"","surface_ar":"وا۟"},{"lemma_ar":"مُسْتَبْصِرِين","morph_features":"STEM|POS:N|ACT|PCPL|(X)|LEM:musotaboSiriyn|ROOT:bSr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"29:38:16:1","qac_word_ref":"29:38:16","root_ar":"ب ص ر","surface_ar":"مُسْتَبْصِرِينَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["29:38:1:1"],["29:38:1:2"],["29:38:2:1"],[],["29:38:3:1"],["29:38:3:2"],["29:38:4:1"],["29:38:5:1","29:38:5:2"],["29:38:6:1"],[],["29:38:8:1"],["29:38:8:2"],["29:38:9:1","29:38:9:2"],[],[],[],[],[],[],[],[],[],[]],"word_analysis_refs":["29:38:1","29:38:2","29:38:3","29:38:4","29:38:5","29:38:6","29:38:7","29:38:8","29:38:9","29:38:10","29:38:11","29:38:12","29:38:13","29:38:14","29:38:15","29:38:16","29:38:17","29:38:18","29:38:19","29:38:20","29:38:21","29:38:22","29:38:23"],"word_rows":[{"analysis_record_ref":"29:38:1","analytic_gloss_range_en":"opening conjunction that carries the named peoples into an already-running destruction frame","analytic_root_gloss_range_en":null,"qac_refs":["29:38:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"29:38:2","analytic_gloss_range_en":"proper name for the people of ʿAd as an accusative carried object; tanwin keeps it fully declinable beside its paired name","analytic_root_gloss_range_en":"return, recurrence, or coming back; here only background pressure on a proper name, not a free local verb sense","qac_refs":["29:38:1:2"],"root":{"arabic":"ع و د","transliteration":"ʿ-w-d"},"surface":{"arabic":"عَادًۭا","transliteration":"ʿĀdan"}},{"analysis_record_ref":"29:38:3","analytic_gloss_range_en":"coordinating conjunction that binds Thamud to ʿAd under the same recovered governance","analytic_root_gloss_range_en":null,"qac_refs":["29:38:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"29:38:4","analytic_gloss_range_en":"proper name for Thamud as an accusative paired object; base diptote shape remains visible beside a leveling tanwin variant","analytic_root_gloss_range_en":"Thamud-name root field with depletion or exhausted-water pressure in some evidence; locally a proper name with cautious root coloring only","qac_refs":[],"root":{"arabic":"ث م و د","transliteration":"th-m-w-d"},"surface":{"arabic":"ثَمُودَ","transliteration":"Thamūda"}},{"analysis_record_ref":"29:38:5","analytic_gloss_range_en":"connector introducing the certified evidence parenthesis and the shift toward direct address","analytic_root_gloss_range_en":null,"qac_refs":["29:38:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"29:38:6","analytic_gloss_range_en":"certification particle before a perfect verb, marking the clarity as established rather than tentative","analytic_root_gloss_range_en":null,"qac_refs":["29:38:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"29:38:7","analytic_gloss_range_en":"Form V perfect of becoming clear or distinct; the evidence has self-manifested to the audience from the ruins","analytic_root_gloss_range_en":"separation, distinction, clarification, and evidentness; local Form V selects self-manifesting clarity","qac_refs":["29:38:4:1"],"root":{"arabic":"ب ي ن","transliteration":"b-y-n"},"surface":{"arabic":"تَبَيَّنَ","transliteration":"tabayyana"}},{"analysis_record_ref":"29:38:8","analytic_gloss_range_en":"prepositional phrase routing the manifest evidence to the addressed audience as witnesses","analytic_root_gloss_range_en":null,"qac_refs":["29:38:5:1","29:38:5:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَكُمْ","transliteration":"lakum"}},{"analysis_record_ref":"29:38:9","analytic_gloss_range_en":"source preposition that makes the dwellings the origin, medium, or sample of the evidential clarity","analytic_root_gloss_range_en":null,"qac_refs":["29:38:6:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"مِنْ","transliteration":"min"}},{"analysis_record_ref":"29:38:10","analytic_gloss_range_en":"possessed plural dwelling-places governed by the source phrase; ruined habitation becomes visible evidence","analytic_root_gloss_range_en":"dwelling, settling, repose, and stillness; the ruin context lets habitation and final stillness overlap","qac_refs":[],"root":{"arabic":"س ك ن","transliteration":"s-k-n"},"surface":{"arabic":"مَسَاكِنِهِمْ","transliteration":"masākinihim"}},{"analysis_record_ref":"29:38:11","analytic_gloss_range_en":"resumptive conjunction returning from the evidence parenthesis to the causal narrative","analytic_root_gloss_range_en":null,"qac_refs":["29:38:8:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"29:38:12","analytic_gloss_range_en":"Form II active beautifying or adorning of deeds, with recipient and object separated and the agent named","analytic_root_gloss_range_en":"beauty, adornment, attractive presentation, and making something seem fair; local Form II selects active beautification of deeds","qac_refs":["29:38:8:2"],"root":{"arabic":"ز ي ن","transliteration":"z-y-n"},"surface":{"arabic":"زَيَّنَ","transliteration":"zayyana"}},{"analysis_record_ref":"29:38:13","analytic_gloss_range_en":"prepositional recipient phrase for beautification, ironically marking the harmed group as those for whom the deeds were made attractive","analytic_root_gloss_range_en":null,"qac_refs":["29:38:9:1","29:38:9:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَهُمُ","transliteration":"lahumu"}},{"analysis_record_ref":"29:38:14","analytic_gloss_range_en":"bound plural pronoun carrying the named peoples forward as one affected group","analytic_root_gloss_range_en":null,"qac_refs":[],"root":{"note":"no lexical root"},"surface":{"arabic":"هُمُ","transliteration":"humu"}},{"analysis_record_ref":"29:38:15","analytic_gloss_range_en":"definite nominative adversarial agent who beautifies the deeds; remoteness pressure fits the later separation from the path","analytic_root_gloss_range_en":"remoteness and estrangement, with an alternative fire derivation only as background; locally the known adversarial agent is selected","qac_refs":[],"root":{"arabic":"ش ط ن","transliteration":"sh-ṭ-n"},"surface":{"arabic":"ٱلشَّيْطَانُ","transliteration":"al-shayṭānu"}},{"analysis_record_ref":"29:38:16","analytic_gloss_range_en":"their collected deeds or works as the object made attractive and the hinge toward diversion","analytic_root_gloss_range_en":"work, action, deed, practice, and agency; local plural construct selects their owned body of deeds","qac_refs":[],"root":{"arabic":"ع م ل","transliteration":"ʿ-m-l"},"surface":{"arabic":"أَعْمَالَهُمْ","transliteration":"aʿmālahum"}},{"analysis_record_ref":"29:38:17","analytic_gloss_range_en":"causal-sequential particle making the obstruction follow from the beautification","analytic_root_gloss_range_en":null,"qac_refs":[],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"29:38:18","analytic_gloss_range_en":"completed transitive obstruction or turning-away of the named peoples from the path, without erasing the path itself","analytic_root_gloss_range_en":"turning away, barring, hindering, aversion, and obstruction; local frame selects transitive diversion away from the path","qac_refs":[],"root":{"arabic":"ص د د","transliteration":"ṣ-d-d"},"surface":{"arabic":"صَدَّهُمْ","transliteration":"ṣaddahum"}},{"analysis_record_ref":"29:38:19","analytic_gloss_range_en":"separation preposition completing the obstruction frame by marking what they are turned away from","analytic_root_gloss_range_en":null,"qac_refs":[],"root":{"note":"no lexical root"},"surface":{"arabic":"عَنِ","transliteration":"ʿani"}},{"analysis_record_ref":"29:38:20","analytic_gloss_range_en":"the definite singular way or proper course, governed after the separation preposition and targeted by obstruction","analytic_root_gloss_range_en":"path, way, course, means, and flowing or let-fall imagery; local definite noun selects the recognized proper route","qac_refs":[],"root":{"arabic":"س ب ل","transliteration":"s-b-l"},"surface":{"arabic":"ٱلسَّبِيلِ","transliteration":"al-sabīli"}},{"analysis_record_ref":"29:38:21","analytic_gloss_range_en":"final conjunction that adds the closing state and, in context, makes it concessive","analytic_root_gloss_range_en":null,"qac_refs":[],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"29:38:22","analytic_gloss_range_en":"past auxiliary/copular verb establishing the plural subjects in an already-held state of insight","analytic_root_gloss_range_en":"being, existing, occurring, or becoming; local perfect plus participle selects an established past state","qac_refs":[],"root":{"arabic":"ك و ن","transliteration":"k-w-n"},"surface":{"arabic":"كَانُوا","transliteration":"kānū"}},{"analysis_record_ref":"29:38:23","analytic_gloss_range_en":"Form X masculine plural active participle of insight, seeking, possessing, or claiming clear perception in the ayah closing","analytic_root_gloss_range_en":"sight, perception, discernment, insight, and reflective seeing; local Form X participle selects heightened perceptual status with qualified range","qac_refs":[],"root":{"arabic":"ب ص ر","transliteration":"b-ṣ-r"},"surface":{"arabic":"مُسْتَبْصِرِينَ","transliteration":"mustabṣirīna"}}]}
</focus_surface_json>

## Micro contribution

<micro_contribution_json>
{"ayah_ref":"29:38","candidate_decisions":[{"candidate_id":"cand_e323a9c554dc9aba40bc","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Odak yurt adının yerleşme ve durulma baskısı, yıkıntıyı geçmiş yerleşimin hâlâ okunabilen tanığı olarak kuruyor."},{"candidate_id":"cand_0c15fbcb88b8e8245fe7","decision":"narrow","finding_refs":["micro:ruins-as-disclosure"],"reason":"Temel i'rabda yurtlar مِنْ altında açıklığın kaynağıdır; nominatif varyant yalnızca yurtların açıklayıcı fail gibi duyulması yönündeki sınırlı baskıyı koruyor."},{"candidate_id":"cand_ffee06c640990df3c516","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Yurtlar yer bildiren bir ayrıntı olmaktan çıkıp yıkımdan sonra kalan okunabilir tanık olarak somut bir okuyucu kazanımı sağlıyor."},{"candidate_id":"cand_f43b2cc89a130d809690","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Parantezdeki kanıt cümlesinden sonra gelen bağlaç, ana nedensel anlatıyı yeniden bağlayan belirgin bir yüzey taşıyıcısıdır."},{"candidate_id":"cand_ff3a5016bef1d71bf5df","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Aktif fiilin özne, alıcı ve doğrudan nesne ayrımı, güzelleştirme mekanizmasındaki failliği ve etkilenen grubu ayrı ayrı görünür kılıyor."},{"candidate_id":"cand_84a995280049207af00f","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Form II ve fiilin doğrudan nesnesi, düşüşü kaba zorlamadan önce eylemlerin işlenmiş bir yüzey üzerinden çekici kılınması olarak kuruyor."},{"candidate_id":"cand_054980ab7c0d77bfbc88","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Güzelleştirme ile sonraki yoldan alıkoyma odak ayette aynı yerel sonuç zincirinde birleşiyor ve bu zincir somut bir okuma değişikliği taşıyor."},{"candidate_id":"cand_d6ced223d4cd6d60e59f","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"لَهُمُ yapısı güzelleştirmenin onlar için yönünü kurarken, sonraki sonuç bu yönelişin onlar üzerinde zararlı bir etki olarak çalıştığını gösteriyor."},{"candidate_id":"cand_5872748bed52504cf252","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Bağlı çoğul zamir, iki adı yurtların sahipleri, güzelleştirmenin alıcıları ve alıkoymanın nesneleri olarak aynı toplulukta tutuyor."},{"candidate_id":"cand_1c213b841c05b56c10c3","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Adı verilmiş fail, güzelleştirme ve yol engelleme sırasını odak ayette tamamlanan tanıdık bir aldatma kuruluşu olarak taşıyor."},{"candidate_id":"cand_1e3c429893bf6697184f","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Belirli ve nominatif Şeytan sözcüğü, güzelleştirme fiilinin faili olarak açıkça case-marked ve tanınabilir durumdadır."},{"candidate_id":"cand_a347d8a6ca09628c9c0e","decision":"narrow","finding_refs":["micro:beautified-agency"],"reason":"Uzaklık ve yabancılaşma kök baskısı, adın yerel özel ad işlevini değiştirmeden yol ile mesafe okumasını renklendiriyor."},{"candidate_id":"cand_408da59ed8fd20865222","decision":"narrow","finding_refs":["micro:beautified-agency"],"reason":"عمل adının temel anlamı geniş ve nötr eylem alanıdır; tehlike, adın kendisinden değil güzelleştirme ve alıkoyma ilişkisine girmesinden doğuyor."},{"candidate_id":"cand_1739fd740095bd3bb688","decision":"accept","finding_refs":["micro:beautified-agency"],"reason":"Çoğul iyelikli nesne, tek bir davranış yerine topluluğun sahip olduğu bütün eylem alanının çekici gösterildiğini açıkça taşıyor."},{"candidate_id":"cand_a2143ee4515fa5ccc24f","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Yerel sıra, güzelleştirilen eylemleri sonraki yoldan sapmanın dönüm noktası olarak kuruyor."},{"candidate_id":"cand_de7d6532945c99b6729d","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"فَ bağlacı, alıkoymayı güzelleştirmenin ayrı bir sonucu değil, onun hemen ardından gelen sonucu olarak bağlıyor."},{"candidate_id":"cand_e3d1f86386623532996f","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Ekli çoğul nesne, içgörü sahibi topluluğu tamamlanmış alıkoyma eyleminin doğrudan etkileneni yapıyor."},{"candidate_id":"cand_8a6ae59b1623ea2eda3b","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Fa-sonuç zinciri ile yol birlikteliği, güzelleştirme ardından yoldan alıkoymayı yerel ve formülleşmiş bir mekanizma olarak görünür kılıyor."},{"candidate_id":"cand_afc77cd415ae33d518f5","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Alıkoyma fiili yolu ortadan kaldırmadan topluluğun ona erişimini ve yönelişini kesiyor; bu, fiilin geçişli yapısıyla destekleniyor."},{"candidate_id":"cand_6c1355508afd4e996ab6","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"عَنِ edatı, alıkoymanın hedefini belirli bir yoldan uzaklaşma olarak tamamlıyor."},{"candidate_id":"cand_4b45ddfcc0cd19d71516","decision":"accept","finding_refs":["micro:carried-name-pair"],"reason":"Başlangıç bağlacı adları yeni bir sahneye sıfırdan başlatmak yerine taşınmış yıkım yönetimi içine alıyor."},{"candidate_id":"cand_512bcfaef105c02addba","decision":"narrow","finding_refs":["micro:way-obstruction"],"reason":"Yol adındaki akış ve kurs baskısı, yerel isim anlamı olan yolun üzerine yalnızca engellenen doğal güzergâh imgesi olarak ekleniyor."},{"candidate_id":"cand_ff3eff4a90fe4affe9e0","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Belirli tekil yol biçimi, alıkoymanın herhangi bir rotayı değil tanınan yolu hedeflediğini gösteriyor."},{"candidate_id":"cand_2e7fc0ab34afb5981112","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Genitif yol adı, عَنِ edatının yönettiği ayrılma tamamlayıcısı olarak alıkoymanın kesin hedefini kuruyor."},{"candidate_id":"cand_6e59a114678378ea1967","decision":"accept","finding_refs":["micro:way-obstruction"],"reason":"Alıkoyma ile yolun birlikte kullanımı, hedefin tanınabilir ve erişilebilir bir güzergâh olduğunu somutlaştırıyor."},{"candidate_id":"cand_b098221ea6f4e615894a","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Son bağlaç, içgörü durumunu önceki alıkoyma eylemine ekleyerek cümleyi bağlanmış bir rağmen ilişkisine keskinleştiriyor."},{"candidate_id":"cand_e5f244a301dd8d6ab533","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"كَانُوا ile participle birleşimi, iki topluluğun içgörü durumunu o anda ortaya çıkan geçici bir parıltı değil, elde edilmiş bir hâl olarak kuruyor."},{"candidate_id":"cand_a45180e0e5f9c6fd5389","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Aynı yardımcı fiil ve participle düzeninin hemen sonraki 29:39'da yankılanması, mevcut kapanışın yakın metinsel devamını somutlaştırıyor."},{"candidate_id":"cand_71d9e52aacf218d9b477","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Çoğul fiil, açılıştaki iki adı yeniden adlandırmadan kapanışın öznesi olarak etkin tutuyor."},{"candidate_id":"cand_73a0e61259ed838a47b3","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Yakın önceki bedensel yıkım ile kapanıştaki algı dili arasındaki sınır karşılaştırması, içgörüye rağmen süren düşüşü belirginleştiriyor."},{"candidate_id":"cand_88e2a7e96b3fe305240d","decision":"narrow","finding_refs":["micro:insight-paradox"],"reason":"Form X, kapanışta yükseltilmiş algı ve içgörü aralığını destekliyor; bunu tek ve azami kesinlik anlamına indirgemeden taşıyoruz."},{"candidate_id":"cand_aa2e52e4810029adf4f6","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Nadir kapanış biçimi, packetta verilen Şeytan temasıyla ilgili ters yönlü hatırlama ve görme karşılaştırmasını somut bir yankı olarak taşıyor."},{"candidate_id":"cand_a04953e45bcb84196b81","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Akkusatif participle, iki topluluğu kapanışta ortak ve süreklilik kazanmış bir algı durumu ile sınıflandırıyor."},{"candidate_id":"cand_95ce80f2b2ff35ca4c7a","decision":"accept","finding_refs":["micro:insight-paradox"],"reason":"Kapanıştaki algı sözcüğü, baştaki açıkça belirginleşen kanıtı geri çağırarak açıklık ile eyleme yön vermeyen içgörüyü aynı zarf içinde tutuyor."},{"candidate_id":"cand_7cca21b3f9eca4ae2318","decision":"accept","finding_refs":["micro:carried-name-pair"],"reason":"Âd adındaki akkusatif tenvin, adı geri kazanılan bir fiil çerçevesinin taşınan nesnesi olarak biçimsel biçimde görünür kılıyor."},{"candidate_id":"cand_978705f2205fc3f2af92","decision":"accept","finding_refs":["micro:carried-name-pair"],"reason":"Âd ve Semûd'un eşleştirilmesi, iki özel adı aynı yıkılmış topluluklar çerçevesinde birlikte okunabilir kılıyor."},{"candidate_id":"cand_53366c02cc7c3847de7d","decision":"narrow","finding_refs":["micro:carried-name-pair"],"reason":"Âd adındaki geri dönüş ve yinelenme baskısı yalnızca ihtiyatlı bir arka plan rengidir; özel ad ve yıkım çerçevesinin yerini almıyor."},{"candidate_id":"cand_1f67288f6ed9468431b5","decision":"accept","finding_refs":["micro:carried-name-pair"],"reason":"İkinci bağlaç Semûd'u ilk adla aynı taşınmış yönetim altında pair-locking yapan yerel bir bağlantı kuruyor."},{"candidate_id":"cand_9b2e1495f3506b53ad42","decision":"narrow","finding_refs":["micro:carried-name-pair"],"reason":"Semûd adındaki tükenme ve su kaybı imgesi, özel adın temel işlevini koruyan ihtiyatlı bir arka plan baskısı olarak kalıyor."},{"candidate_id":"cand_004018374ba52e83e7e2","decision":"accept","finding_refs":["micro:carried-name-pair"],"reason":"Semûd'un temel diptot yüzeyi, Âd ile aynı akkusatif nesne rolünü paylaşırken tenvin bakımından işitilen bir asimetri taşıyor; varyant bu farkı canlı bırakıyor."},{"candidate_id":"cand_500e1a8d4f85d358b695","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Semûd özel adı, hemen açılan yurtlar ilişkisiyle birlikte görünür yerleşim ve yıkım tanıklığına bağlanıyor."},{"candidate_id":"cand_81f534a9acef9d6d8dfd","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Bağlaç, ad listesinden muhataba yönelen ve kanıt çerçevesini açan belirgin bir söylem parantezi başlatıyor."},{"candidate_id":"cand_7c26229fcf5f7dad6c7e","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"قَدْ parçacığı, ardından gelen tamamlanmış fiilin bildirdiği açıklığı ihtimal değil gerçekleşmiş durum olarak sertifikalandırıyor."},{"candidate_id":"cand_c07edaa35ae6f2196915","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Tamamlanmış Form V fiil ve geniş özne, yurtlardan çıkarılan açıklığın zaten gerçekleşmiş olduğunu kuruyor."},{"candidate_id":"cand_c11f60e149f7af43c726","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Muhataba açık kesinlik ile kapanıştaki başarısız içgörü aynı yerel algı zarfında karşılaştırılabilir hâle geliyor."},{"candidate_id":"cand_7df2310ac6a31d357e4f","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Form V açıklığı dışarıdan açıklayan bir failden çok yurtların içinden kendiliğinden belirginleşen kanıt olarak kuruyor."},{"candidate_id":"cand_8c62b9e942c58dff7f4f","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"Dative yönlendirme, açıklığın yalnızca tarihsel bir yerde bulunmadığını, mevcut muhatabın tanıklığına sunulduğunu gösteriyor."},{"candidate_id":"cand_25433f08078575a63312","decision":"narrow","finding_refs":["micro:ruins-as-disclosure"],"reason":"Yerel sözdizimi kaynak okumasını güçlü biçimde koruyor; yurtların açıklığı doğrudan açığa çıkaran fail gibi duyulması yalnızca kontrollü varyant baskısı olarak tutuluyor."},{"candidate_id":"cand_96cb0de1117b69a664c2","decision":"accept","finding_refs":["micro:ruins-as-disclosure"],"reason":"مِنْ edatı yurtları açıklığın yalnızca çevresindeki yer değil, açıklığın çıktığı ve kanıtı taşıdığı kanal yapıyor."},{"candidate_id":"cand_796e9198fd0ee9ef1e22","decision":"reject","finding_refs":[],"reason":"Packet bu QAC satırını yalnızca odak kökü oluşumu olarak ledger_only veriyor; bağımsız taşıyıcı, mekanizma, değişmiş okuma ve okuyucu getirisi sağlamıyor."},{"candidate_id":"cand_4c9611bd8ec70c845819","decision":"reject","finding_refs":[],"reason":"Bu QAC oluşum satırı yalnızca ع م ل yüzey oluşumunu kaydediyor; anlam değişimini kuran kanıt word_analysis bulgusunda ve ledger_only satırın kendisinde bulunmuyor."},{"candidate_id":"cand_c38e267d9b824c8313f1","decision":"reject","finding_refs":[],"reason":"Bu ledger_only QAC satırı ص د د oluşumunu bildiriyor ancak ayrı bir mekanizma veya okuyucuya yeni bir kavrayış taşımıyor."},{"candidate_id":"cand_c3e200e1b61f55a03d28","decision":"reject","finding_refs":[],"reason":"س ب ل QAC oluşumu yüzey taşıyıcısını doğruluyor, fakat tek başına değişmiş okuma ve containment sağlayan bağımsız bir bulgu değil."},{"candidate_id":"cand_b32b2ea0743e06c5cf3b","decision":"reject","finding_refs":[],"reason":"ك و ن QAC satırı yalnızca odak morfemini listeliyor; standing-state anlamını kuran destek word_analysis kaydında taşınıyor."},{"candidate_id":"cand_d2e6083dbd766aae9e7f","decision":"reject","finding_refs":[],"reason":"ب ص ر QAC occurrence kaydı kök temasını gösteriyor ama iç kavrayış için bağımsız aktivasyon, mekanizma ve okuyucu payı sunmuyor."},{"candidate_id":"cand_fc97f435d1b4937007bb","decision":"reject","finding_refs":[],"reason":"ع و د QAC kaydı özel ad oluşumunu listeliyor; ihtiyatlı geri dönüş rengi word_analysis adayında, occurrence satırında değil."},{"candidate_id":"cand_d6d163f7fb18e357b666","decision":"reject","finding_refs":[],"reason":"ب ي ن QAC occurrence yalnızca yüzey fiilini kaydediyor; kendiliğinden belirginleşme mekanizması word_analysis kanıtında zaten sınırlandırılmış."},{"candidate_id":"cand_7146b5f73a75581b23e2","decision":"reject","finding_refs":[],"reason":"س ك ن QAC occurrence yurt adının kök temasını gösteriyor, fakat stillness ve tanıklık değişmiş okumasını tek başına kurmuyor."},{"candidate_id":"cand_c7113683973b5712cf82","decision":"reject","finding_refs":[],"reason":"ز ي ن QAC occurrence yalnızca güzelleştirme fiilinin yüzey kökünü kaydediyor; mekanizma ve okuyucu getirisi word_analysis bulgularında taşınıyor."},{"candidate_id":"cand_3f625a6ab7cb1baa0be8","decision":"narrow","finding_refs":["micro:insight-paradox"],"reason":"HFT kaydı odak sözcükleri, üç branch taşıyıcısı ve açık bir before/after mekanizması sağlıyor; legacy_unbound provenance nedeniyle yalnız dış kanıt ile iç kavrayış arasındaki sınırlı yerel gerilimi koruyoruz."},{"candidate_id":"cand_8b0d61bba9d137dceab5","decision":"narrow","finding_refs":["micro:beautified-agency"],"reason":"HFT kaydı güzelleştirme, eylem ve yol ilişkisini odak yüzeyiyle somut biçimde taşıyor; legacy_unbound kaynağı nedeniyle tam model sonucu yerine bu sınırlı değer-değişimi katkısı tutuluyor."},{"candidate_id":"cand_b9aaf2952dc6d967271f","decision":"narrow","finding_refs":["micro:ruins-as-disclosure"],"reason":"HFT kaydı yurt, durulma ve açığa çıkma branch'lerini odak ifadesine bağlıyor; legacy_unbound provenance nedeniyle yalnız yurtların yerleşimi aşan tanıklık dönüşü korunuyor."}],"coverage_complete":true,"findings":[{"branch_refs":[],"candidate_ids":["cand_4b45ddfcc0cd19d71516","cand_7cca21b3f9eca4ae2318","cand_978705f2205fc3f2af92","cand_53366c02cc7c3847de7d","cand_1f67288f6ed9468431b5","cand_9b2e1495f3506b53ad42","cand_004018374ba52e83e7e2"],"claim":"Başlangıçtaki bağlaç, Âd ile Semûd adlarını geri kazanılan yıkım çerçevesine taşır; ortak nesne rolü içinde tenvin ve diptot yüzeylerinin farkı, iki adı hem birlikte hem de ayrı işitilir kılar.","connection_refs":[],"containment":"Âd ve Semûd yerel okumada özel ad olarak kalır; geri dönüş ve tükenme çağrışımları bu ad işlevine eklenir. Varyant, temel diptot çözümünü silmeden yalnızca alternatif biçim baskısını açık tutar.","context_refs":[],"epistemic_status":"Odak ayetin sözdizimi ve güvenilir word_analysis kayıtlarıyla doğrudan temellenen okuma; özel ad kök renkleri ve varyant etkisi açıkça sınırlandırılmıştır.","finding_ref":"micro:carried-name-pair","mechanism":"İlk وَ bağlacı süreklilik kurar, Âd'ın akkusatif tenvini taşınan nesne çerçevesini duyurur, ikinci وَ ad çiftini kilitler ve Semûd'un temel diptot biçimi ile canlı tenvin varyantı biçimsel asimetriyi korur. Özel ad köklerindeki geri dönüş ve tükenme baskıları bu sahneye yalnızca ihtiyatlı bir arka plan rengi verir.","reader_payoff":"Okur, iki adı çıplak bir liste olarak değil, aynı yıkım hükmüne bağlı bir çift ve biçimsel farkı işitilen iki ayrı yüzey olarak algılar.","support_ids":["sup_5995424bc3d409951b73","sup_c4f5224f8d7df57e56d2","sup_df0aa5d3a60869d9e658","sup_3e2c16c7947ec9b1ba73","sup_8b2964925237c64a4e53","sup_19c610c7fab85798337c","sup_631548b1eaedc46d1175","sup_80e29439989f89b33a51","sup_f4525684e125d6460f6b","sup_f969f73aeab0fad1034d"],"title":"Taşınmış ad çifti ve biçimsel asimetri"},{"branch_refs":["root_000170/B004","root_000726/B001","root_000726/B009"],"candidate_ids":["cand_e323a9c554dc9aba40bc","cand_0c15fbcb88b8e8245fe7","cand_ffee06c640990df3c516","cand_500e1a8d4f85d358b695","cand_81f534a9acef9d6d8dfd","cand_7c26229fcf5f7dad6c7e","cand_c07edaa35ae6f2196915","cand_c11f60e149f7af43c726","cand_7df2310ac6a31d357e4f","cand_8c62b9e942c58dff7f4f","cand_25433f08078575a63312","cand_96cb0de1117b69a664c2","cand_b9aaf2952dc6d967271f"],"claim":"Kanıt parantezi, yurtları yalnızca geçmiş yerleşim noktaları olarak değil, muhataba açıkça ulaşan ve yıkımın kendisini okunabilir kılan bir açıklık kanalı olarak kurar.","connection_refs":[],"containment":"Temel okuma açıklığın yurtlardan geldiğini korur; yurtların doğrudan açıklayıcı fail gibi duyulması sınırlı varyant baskısıdır. Semûd adı bu yerleşim tanıklığına bağlanır, fakat özel ad işlevi korunur.","context_refs":[],"epistemic_status":"Sözdizimi, biçim ve kelime kayıtlarıyla doğrudan desteklenen yerel okuma; yerleşim dönüşünü taşıyan HFT katkısı legacy_unbound olduğu için nitelikli bir ek olarak tutulmuştur.","finding_ref":"micro:ruins-as-disclosure","mechanism":"Kanıtı açan وَ, قَدْ ve tamamlanmış Form V تَبَيَّنَ ile açıklığın zaten gerçekleştiğini bildirir; لَكُمْ onu muhatabın tanıklığına yöneltir, مِنْ ve temel genitif مَسَاكِنِهِمْ ise açıklığın yurtlardan çıktığını gösterir. Yerleşme ve durulma baskısı, sakinlerin yokluğunda yurtların durmuş kalıntı olarak tanıklık etmesini sağlar. Alternatif i'rab bu kalıntıları açıklığı taşıyan failler gibi duyurabilir, fakat temel kaynak ilişkisini kaldırmaz.","reader_payoff":"Okur, görünür yurtların dekor değil kanıtın taşıyıcısı olduğunu ve açıklığın uzak bir anlatımdan çok muhataba sunulmuş bir karşılaşma olarak kurulduğunu görür.","support_ids":["sup_60d19ed2804d00cbedf3","sup_dfa9f47d9eb57ca243b6","sup_bdf53680b8e05540ad93","sup_ab69484f61a806f0f4eb","sup_a77f6ac1b8053c154d84","sup_f4525684e125d6460f6b","sup_624ae183161e3c00b578","sup_b843a6065422f594e330","sup_978e84f2b967f07f85b6","sup_d176b8f45421e5a2ad21","sup_1e2a7b6dd69b3815b31c","sup_c00c0ef0e0a8e5837571","sup_0dd659ad808f6e373a23","sup_33c0e1a90b3368c319c0","sup_778fc51a2f25126608dc","sup_97226ac3686446cfeb44","sup_2a916727f8ec83c31339","sup_af2b0cb03b21d691d74e","sup_e6dad31dd3ba0b1a4106","sup_15b705015e215d3c1e0d"],"title":"Yurtların açıklığa dönüşen tanıklığı"},{"branch_refs":["root_000660/B002","root_000672/B001","root_000796/B004","root_000848/B001","root_001046/B001"],"candidate_ids":["cand_f43b2cc89a130d809690","cand_ff3a5016bef1d71bf5df","cand_84a995280049207af00f","cand_d6ced223d4cd6d60e59f","cand_5872748bed52504cf252","cand_1c213b841c05b56c10c3","cand_1e3c429893bf6697184f","cand_a347d8a6ca09628c9c0e","cand_408da59ed8fd20865222","cand_1739fd740095bd3bb688","cand_8b0d61bba9d137dceab5"],"claim":"Kanıt parantezinden sonra ayet, adı belirli Şeytan'ın onların bütün eylem alanını kendileri için çekici kılmasıyla faillik zincirini görünür kılar; eylem sürerken değerlendirme yönü değişir.","connection_refs":[],"containment":"Şeytan ayetin adlandırılmış faili, eylemler de güzelleştirmenin nesnesi olarak kalır; zarar gören alıcı ve eylem sürerken yönün değişmesi bu temel yapıya eklenir. Uzaklık kökü yalnızca arka plan baskısıdır, eylem kökü ise kendiliğinden kötülük anlamına daraltılmaz.","context_refs":[],"epistemic_status":"Fiil valansı, zamir zinciri ve word_analysis kayıtlarıyla doğrudan temellenen okuma; branch tabanlı valuation katkısı legacy_unbound HFT kaynağı nedeniyle sınırlandırılmıştır.","finding_ref":"micro:beautified-agency","mechanism":"Resumptive وَ anlatıyı geri bağlar; aktif Form II زَيَّنَ fiili faili, لَهُمُ ile etkilenen topluluğu ve أَعْمَالَهُمْ ile çoğul sahiplik içindeki eylemleri ayırır. Şeytan'ın nominatif ve belirli oluşu failin adını açık eder, bağlı zamir aynı topluluğu zincir boyunca taşır ve iş eylem alanının nötr genişliği güzelleştirme altında tehlikeli bir değerlendirme yüzeyine dönüşür.","reader_payoff":"Okur, aldatmayı belirsiz bir dış baskı değil, onların kendi eylemlerinin çekici gösterilmesi üzerinden çalışan ve onları eylemde tutarken yönlerini değiştiren bir işlem olarak fark eder.","support_ids":["sup_071c9e3868cfdc70508f","sup_3685ed4eda1288dae095","sup_0c3a75e9d24aa5bc5068","sup_ce7c593332e5681d5954","sup_aa94557924e00dc8475f","sup_00edb74e09104fbb8cac","sup_1141acf1a43c0d262ec2","sup_643c19cb5bb02d3f89ac","sup_733c35216c52323498cf","sup_0b0d79691242755a9e0c","sup_17dda1ebeeac73cac0b2","sup_01cea74d4e224839bd80","sup_9b56678ed36238a26c4a","sup_4ef731f586f311d5faa4","sup_b9955b33be6fdef9a4f9","sup_11bdd4ef32479b945e28","sup_850fd7762f8a652a0825"],"title":"Güzelleştirme içinde yön değiştiren faillik"},{"branch_refs":[],"candidate_ids":["cand_054980ab7c0d77bfbc88","cand_a2143ee4515fa5ccc24f","cand_de7d6532945c99b6729d","cand_e3d1f86386623532996f","cand_8a6ae59b1623ea2eda3b","cand_afc77cd415ae33d518f5","cand_6c1355508afd4e996ab6","cand_512bcfaef105c02addba","cand_ff3eff4a90fe4affe9e0","cand_2e7fc0ab34afb5981112","cand_6e59a114678378ea1967"],"claim":"فَ ile başlayan sonuç zinciri, onların güzelleştirilen eylemleri ardından tanınan yoldan tamamlanmış biçimde alıkonulmasını bildirir; yol yerinde kalırken erişim ve yöneliş kesilir.","connection_refs":[],"containment":"Temel okuma onların Şeytan tarafından yoldan alıkonulmasıdır; yolun korunmuş olması, kurs imgesi ve engellemenin erişim yönü bu okumayı derinleştirir. Akış kökü yol adını serbest bir dökme fiiline dönüştürmez.","context_refs":[],"epistemic_status":"Yerel bağlaç, geçişlilik, edat ve isim biçimleriyle doğrudan desteklenen sözdizimsel ve kavramsal okuma; kök akış baskısı açıkça daraltılmıştır.","finding_ref":"micro:way-obstruction","mechanism":"فَ güzelleştirmeyi yakın sonuçla bağlar, صَدَّهُمْ topluluğu tamamlanmış geçişli eylemin nesnesi yapar ve عَنِ ٱلسَّبِيلِ ayrılmanın hedefini belirli tekil yol olarak tamamlar. Yol adı fiziksel güzergâh ve amaçlı rota basıncını taşır; akış veya kurs imgesi yalnızca bu temel yol anlamını keskinleştiren sınırlı bir renktir.","reader_payoff":"Okur, ayetin genel bir ahlaki başarısızlıktan söz etmediğini; işlenmiş eylem değerlendirmesinin belirli ve mevcut bir yola erişimi nasıl engellediğini görür.","support_ids":["sup_5adebdef1a7f88d7bd02","sup_ce7c593332e5681d5954","sup_06dbb8004c4a0edf035a","sup_b9955b33be6fdef9a4f9","sup_82dbfa3ce6f74169ac67","sup_de3434e17dd4ac0ab2ea","sup_101f76c0e9fad2176807","sup_25a025134ac7dee7668e","sup_1151621b4b0822e67da4","sup_6e708332349fbd3a342f","sup_32055bb37e6479a36c68","sup_3b91a13afb0ae693b18b","sup_521d97888300a8fc2f36","sup_c810b3a70373f57cb5a0","sup_880cc77a90295f75052c","sup_bd1c16d24586fa2d5347","sup_83babc76fa8951d73ffe"],"title":"Güzelleştirmeden tanınan yoldan uzaklaşmaya"},{"branch_refs":["root_000121/B002","root_000170/B004","root_000726/B002"],"candidate_ids":["cand_b098221ea6f4e615894a","cand_e5f244a301dd8d6ab533","cand_a45180e0e5f9c6fd5389","cand_71d9e52aacf218d9b477","cand_73a0e61259ed838a47b3","cand_88e2a7e96b3fe305240d","cand_aa2e52e4810029adf4f6","cand_a04953e45bcb84196b81","cand_95ce80f2b2ff35ca4c7a","cand_3f625a6ab7cb1baa0be8"],"claim":"Kapanış, Âd ve Semûd'u zaten algı ve kavrayış durumuna sahip bir topluluk olarak adlandırırken, aynı topluluğun yoldan alıkonulmuş olmasını korur; böylece açık dış kanıt ile eyleme yön vermeyen içgörü yan yana kalır.","connection_refs":[],"containment":"Ayetin temel sonucu değişmez: bu topluluklar içgörü sahibi oldukları hâlde yoldan alıkonulmuştur. Form X tek bir azami kesinlik anlamına seçilmez; dış açıklık-iç kavrayış gerilimi, 29:39 yankısı ve ters Şeytan karşılaştırması birbirinin yerine geçirilmeyen ek okumalar olarak kalır.","context_refs":["29:37","29:39"],"epistemic_status":"Kapanışın sözdizimi ve participle çözümlemesi doğrudan packet kanıtıyla desteklenir; HFT'nin iç kavrayış sentezi legacy_unbound bir adaydır ve bu nedenle yerel, nitelikli katkı olarak sunulmuştur. Yakın ayet yankısı packet içindeki pericope referanslarıyla sınırlanmıştır.","finding_ref":"micro:insight-paradox","mechanism":"Son وَ önceki fiile bağlanır; كَانُوا ve akkusatif Form X مُسْتَبْصِرِينَ ortak özneyi elde edilmiş, yükseltilmiş ama anlam aralığı açık bir algı durumunda tutar. Başlangıçtaki تَبَيَّنَ ile kapanıştaki içgörü arasında bir algı zarfı oluşur. HFT'nin odaklı branch katkısı, yurtlardan dış açıklık ve iç kavrayışın mevcut olduğu hâlde görmenin yön verici bir bağlılığa dönüşmemesi gerilimini bu yerel yapı içinde görünür kılar. Önceki 29:37'deki bedensel düşüşle karşılaştırma ve hemen sonraki 29:39'daki yardımcı fiil-participle yankısı bu kapanışın farklı yönlerini açık tutar; packetta verilen ters Şeytan teması da aynı algı alanına karşıt bir yön ekler.","reader_payoff":"Okur, son kelimeyi yalnızca görme yeteneği olarak değil, bilme, arama, sahip olma veya içgörü iddiası aralığını taşıyan bir hâl olarak duyar; sorun bilgiye erişimin yokluğu değil, mevcut kavrayışın hareketi yönetmemesidir.","support_ids":["sup_2bea6964aaa743a336e7","sup_5554e8dd7170847aeef2","sup_2dc9308e4a48584e10df","sup_bcdc904d2f4e99fc5789","sup_4da2d052e572bcd76d0a","sup_817cfe53987a7f759c2b","sup_8118c110735dee93b86c","sup_82c011242f54b6d2ac3e","sup_4d642aa41188c2f2d3f2","sup_027daf4f1ae6253477d8","sup_fd46f44f3ce5c2eb14b8","sup_d103e3976ebe2743182d","sup_ef7feaea18c97da4d0c0"],"title":"Elde edilmiş içgörü içindeki alıkonulma"}],"friction_notes":["Atanan üç HFT kaydı odak yüzeyi, changed-reading, mekanizma ve branch sınırları sağlıyor; ancak legacy_unbound provenance nedeniyle katkıları tam bir sözlük anlamı değil, açıkça nitelenmiş yerel rezonanslar olarak tutuldu.","Connection registry boş ve packet içinde bağlantı kanıtı yok; bu nedenle hiçbir bulguya connection_ref eklenmedi ve bütün hareketler odak sözcükleri ile doğrudan branch kanıtlarına bağlandı.","Bazı kök ve i'rab seçenekleri taşıyıcıya temas etse de bağımsız okuyucu getirisi üretmiyor; bunlar ledger-only olarak elendi veya temel anlamı değiştirmeyen daraltılmış baskılar olarak kayda alındı."],"identity":{"authoring_request_sha256":"c24e105ebe815c4a3b14f7822c4083a83d66dbf089d8389767b82cc297d947f6","ayah_ref":"29:38","lane":"micro","lane_packet_sha256":"4de2e08920717f8d996565f51697db0449f036aff369a692cbc6e7efba1dccf3"},"lane":"micro","movements":[{"draft_prose":"Âyet, {ar:وَعَادًۭا, tr:ve Âden, gloss:Âd'ı} ile {ar:وَثَمُودَا۟, tr:ve Semûde, gloss:Semûd'u} adlarını yeni bir liste gibi değil, taşınmış bir yıkım çerçevesi içinde yan yana getirir. İlk bağlaç anlatının zaten sürmekte olduğunu hissettirir; Âd adındaki akkusatif tenvin de adın geri kazanılan bir hükmün taşıdığı nesne olduğunu duyurur. İkinci bağlaç {ar:ثَمُودَ, tr:Semûde, gloss:Semûd'u} aynı çerçeveye kilitler.\n\nBu eşleşmede küçük bir biçim farkı da iş görür: Âd tenvinini açıkça taşırken Semûd temel okumada diptot yüzeyiyle kalır. Tenvinli düzleştirme varyantının bulunması, farkı sözdizimin tek mümkün sonucu olmaktan çıkarıp işitilen bir yüzey baskısı olarak canlı tutar. Âd adında geri dönüş ve yinelenme, Semûd adında tükenme çağrışımı arka planda hafifçe renk verir; iki adın özel isim ve yıkım içindeki temel işlevi bu renklerle birlikte yerinde kalır.","finding_refs":["micro:carried-name-pair"],"movement_key":"opening-name-pair"},{"draft_prose":"Ardından {ar:وَقَدْ, tr:ve kad, gloss:ve gerçekten} ile açılan kısa kanıt parantezi gelir: {ar:تَّبَيَّنَ, tr:tebeyyene, gloss:açığa çıktı} sözcüğü açıklığı sonradan biri açıklıyormuş gibi değil, zaten belirginleşmiş bir olay gibi kurar. {ar:لَكُمْ, tr:lekum, gloss:size} bu açıklığı muhatabın tanıklığına yöneltir; {ar:مِّنْ, tr:min, gloss:-den} ise onun kaynağını hemen ardından gelen yurtlara bağlar. {ar:مَّسَٰكِنِهِمْ, tr:mesâkinuhum, gloss:onların yurtları} yalnızca geçmişte yaşanan yerleri göstermez. Yerleşme ve durulma hissi, sakinleri kalmasa da durmuş hâlde kalan yapıların yıkım hakkında konuşmasını sağlar. Semûd adı da bu yakın ilişki içinde, salt bir etiket olmaktan çıkıp görünür yerleşim tanıklığına açılır.\n\nTemel kuruluşta yurtlar açıklığın kaynağıdır; farklı i'rab baskısı onları açıklığı kendiliğinden açığa çıkaran görünen failler gibi de duyurabilir. İki yön aynı kalıntıda buluşur: açıklık yurtlardan gelir ve yurtlar bu açıklığı taşıyan bir tanık gibi görünür. Böylece muhataba sunulan kanıt, uzaktan anlatılan bir geçmiş değil, kalıntının kendisinden okunabilen bir açıklık olur.","finding_refs":["micro:ruins-as-disclosure"],"movement_key":"evidence-from-dwellings"},{"draft_prose":"Kanıt parantezinden sonra gelen bağlaç anlatıyı yeniden nedensel harekete bağlar. {ar:زَيَّنَ, tr:zeyyene, gloss:güzelleştirdi} aktif bir fiildir; {ar:ٱلشَّيْطَٰنُ, tr:eş-şeytânu, gloss:Şeytan} belirli ve nominatif fail olarak açıkça öne çıkar, {ar:لَهُمُ, tr:lehumu, gloss:onlar için} güzelleştirmenin yöneldiği topluluğu bildirir, {ar:أَعْمَٰلَهُمْ, tr:a'mâlehum, gloss:onların eylemleri} ise fiilin doğrudan nesnesi olur. Cümle böylece faili, alıcıyı ve çekici gösterilen şeyi birbirine karıştırmaz.\n\nOnlar için yapılmış gibi akan güzelleştirme, devamındaki alıkoyma ile birlikte okunduğunda onlar üzerinde işleyen zararlı bir etki kazanır. Aynı çoğul zamir iki adı yurtların sahipleri, güzelleştirmenin alıcıları, eylemlerin sahipleri ve sonraki fiilin nesneleri olarak birbirine bağlar. Eylem sözcüğü kendi başına kötülük taşıyan dar bir ad değildir; tehlike, onların bütün pratik alanının güzel gösterilerek değerlendirme yönünün değiştirilmesindedir. Bu yerel birleşim, onları eylemsiz kuklalara çevirmeden, kendi işlerini sürdürürken yönlerinin başka bir değerlendirme üzerinden değişmesini görünür kılar.","finding_refs":["micro:beautified-agency"],"movement_key":"beautification-and-agency"},{"draft_prose":"Ardından gelen {ar:فَ, tr:fe, gloss:derken} küçücük bağlaç, güzelleştirme ile sonucu birbirine yaklaştırır. {ar:صَدَّهُمْ, tr:saddehum, gloss:onları alıkoydu} tamamlanmış ve geçişli bir fiildir; topluluk bu eylemin doğrudan nesnesi olur. {ar:عَنِ, tr:ani, gloss:-den uzaklaştırarak} ayrılmanın yönünü verir ve {ar:ٱلسَّبِيلِ, tr:es-sebîli, gloss:bilinen yol} belirli, tekil ve tanınan güzergâhı hedef olarak tamamlar.\n\nBu kuruluşta yol ortadan kalkmaz; değişen, onların o yola erişimi ve yönelişidir. Yol kelimesinin kurs ve akışa yakın baskısı, engellenen güzergâhı fiziksel bir rota gibi hissettirir; yine de yerel anlam yol ve amaçlı geçiş olarak kalır. Böylece güzelleştirilen eylemler, genel bir başarısızlık cümlesinde erimez: yakın sonuç zinciri içinde belirli bir yoldan uzaklaşmaya dönüşür.","finding_refs":["micro:way-obstruction"],"movement_key":"path-obstruction"},{"draft_prose":"Son bağlaç, kapanıştaki hâli alıkoyma eylemine ekler: {ar:وَكَانُوا, tr:ve kânû, gloss:ve onlar idiler} ile {ar:مُسْتَبْصِرِينَ, tr:mustabsirîne, gloss:algı ve kavrayış sahibi} birlikte, iki topluluğu o anda parlayan geçici bir fark edişten çok elde edilmiş bir algı durumunda tutar. Form X biçimi burada yükseltilmiş görme, arama, sahip olma veya içgörü iddiası aralığını açık bırakır. Başlangıçtaki yurtlardan açıkça belirginleşen kanıt ile sondaki kavrayış dili aynı cümlede karşılaşır: dış kanıtın ve iç kavrayış imkânının bulunduğu hâlde görmenin yön verici bir bağlılığa dönüşmemesi, alıkonulmayı bilgi yokluğuna bağlamayan yerel bir okuma açar.\n\nBu kapanış, bir önceki 29:37'deki bedensel düşüşün ardından algı sahibi zihni öne çıkarır; hemen sonraki ayetteki yardımcı fiil ve participle düzeninin yankılanması, durumu yakın akışta sürdürür. Nadir biçim, Şeytan temasına verilen hatırlama ve görme karşılığının ters yönünü düşündürür: burada içgörü dili, yoldan alıkonulmanın içinde kalır. Bu karşılaşmalar temel cümleyi değiştirmez; ayet hâlâ içgörü sahibi oldukları hâlde yoldan alıkonulan bir topluluğu anlatır. Fakat son kelime, açıklık ile eyleme yön vermeyen kavrayış arasındaki gerilimi okuyucunun önünde canlı bırakır.","finding_refs":["micro:insight-paradox"],"movement_key":"insight-and-diversion"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</micro_contribution_json>

## Macro contribution

<macro_contribution_json>
{"ayah_ref":"29:38","candidate_decisions":[{"candidate_id":"cand_df9c356bacb77a20794a","decision":"accept","finding_refs":["macro:road-cutting-mobility"],"reason":"29:29'daki açık yol kesme bağlamı, odaktaki yoldan alıkoyma fiilini işlek güzergâh, yolcular ve hareketin kesilmesiyle ilişkilendiriyor; paket somut taşıyıcı, mekanizma, before/after değişimi ve okur getirisi sağlıyor."},{"candidate_id":"cand_ff11b4ba64ec617517d0","decision":"accept","finding_refs":["macro:fitted-dwelling-structure"],"reason":"29:38'deki meskenlerle 29:41'deki örümcek evi arasında, barınağı yalnız bir kabuk değil destek, ek yeri ve yük taşıyan bir düzenek olarak okutan ayrı bir bağlam mekanizması ve açık bir okur getirisi var."},{"candidate_id":"cand_b0cdc9c11beba468f9e4","decision":"accept","finding_refs":["macro:ruin-as-landmark"],"reason":"Odaktaki açıkça belli olma ve görerek kavrama dili, 29:35'te geride bırakılan açık işaret ve akledenler ifadesiyle doğrudan bağlanıyor; kalıntının olay sonrasında yön gösteren bir kanıta dönüşmesi somut biçimde destekleniyor."},{"candidate_id":"cand_7b6ec7ef851717481779","decision":"accept","finding_refs":["macro:shelter-as-belonging"],"reason":"29:31-32'de ev halkı ve istisna, 29:41'de ise seçilmiş dayanaklar birlikte veriliyor; odaktaki meskeni fiziksel yer anlamını koruyarak aidiyet, kabul ve koruyucu ilişki açısından değiştiren ayrı bir okuma kurulabiliyor."},{"candidate_id":"cand_64952ac6dfd1c0b90cf4","decision":"accept","finding_refs":["macro:stability-test"],"reason":"29:37-41 ve 29:43'teki açık ayet metinleri, yerleşik beden, görünür kanıt, kibir, suç ve zayıf dayanak sırasını taşıyor; legacy_unbound niteliği görünürlüğü kaldırmıyor, yalnızca bu birleşik mimari okumasının epistemik sınırını zorunlu kılıyor."},{"candidate_id":"cand_258d68d6010581d8496e","decision":"accept","finding_refs":["macro:webbed-sight"],"reason":"Odaktaki yol ve görme kelimeleri 29:41'deki örümcek ağına benzeyen zayıf perdeyle aynı somut yüzeyde buluşuyor; HFT kaydı bunun sözlük çevirisi değil, açıkça sınırlandırılmış keşifsel bir benzetme olduğunu belirtiyor."},{"candidate_id":"cand_5b8e47a462dbae9cfa6e","decision":"accept","finding_refs":["macro:case-ledger"],"reason":"29:38'deki Âd adı, görünür kılma dili ve 29:40'taki her birini suçuyla yakalama sırası, adları incelenebilir vakalar gibi okutan paket içi bir before/after hareketi sağlıyor; sayma bağlantısı etimoloji değil, HFT'nin açıkça sınırladığı biçimsel bir yankı olarak korunuyor."},{"candidate_id":"cand_ctx_2289dc1b718a5197ff13","decision":"reject","finding_refs":[],"reason":"29:0 yalnızca otomatik prefatory basmala üyeliğini ve yüzey metnini sağlıyor; 29:38 için somut taşıyıcı, bağlamsal mekanizma, değişen okuma veya ayrı bir okur getirisi vermiyor."}],"coverage_complete":true,"findings":[{"branch_refs":["root_000546/B003","root_000672/B001","root_000672/B002","root_000848/B001","root_000848/B004","root_001046/B011","root_001240/B003","root_001240/B006","root_001240/B023"],"candidate_ids":["cand_df9c356bacb77a20794a"],"claim":"29:38'in Şeytan'ın güzel gösterilen işlerin ardından insanları yoldan alıkoyduğu yönündeki temel okuması, 29:29'un yolu kesme bağlamıyla birlikte başkalarının geçişini ve kaynaklara ulaşmasını bozan etkin bir engelleme olarak görünür.","connection_refs":["conn_630722c657bccfedcdf6"],"containment":"Âyetin olağan anlamı olan bilinen yoldan uzaklaştırılma korunur. Kamusal yol kesme görüntüsü 29:29'un sağladığı bağlamsal basınçtır; 29:38'in yoldan alıkoymasını tek başına fiziksel yol soygunu diye çevirmeyi gerektirmez.","context_refs":["29:29"],"epistemic_status":"Güvenilir kanal kanıtı ve açık perikope bağlamıyla desteklenen yerel bağlamsal sentez.","finding_ref":"macro:road-cutting-mobility","mechanism":"Odaktaki yol, alıkoyma ve işler birlikte durur; 29:29 ise yolu kesmeyi, işlek güzergâhı ve yolcuların hareketinin kesilmesini açıkça kurar. Yakın bağlam bu yüzden alıkoymayı yalnız içsel bir sapma değil, kullanılabilir bir geçiş düzenine yönelen dışa dönük eylem olarak genişletir.","reader_payoff":"Okur, yoldan alıkoyma sözünde yalnız yön kaybını değil, insanların ilerleyişini ve kaynaklara erişimini kesen somut bir hareketi de seçebilir.","support_ids":["sup_4c86cbda457fc090a75c","sup_4cebd27a45ce2e4abf32","sup_9589b8f04f9d3592eb22","sup_aa7da8a5224fd30fbff3","sup_b188a312e38482aaafb1"],"title":"Yoldan alıkoymanın kamusal kesintiye açılması"},{"branch_refs":["root_000121/B006","root_000166/B001","root_000347/B011","root_000726/B002","root_001222/B008","root_001273/B012"],"candidate_ids":["cand_ff11b4ba64ec617517d0"],"claim":"29:38'deki meskenler, 29:41'deki örümcek eviyle birlikte okunduğunda yalnız geçmişin görünen kalıntıları değil, barınak adının gerçekten destek ve birleşimlerle iş görüp görmediğini sınayan yapılar olarak belirir.","connection_refs":["conn_314ac0eed46265bb9f9e"],"containment":"29:38'in tarihi yurtları açık kanıt olarak sunan yüzeyi yerinde kalır. Destek ve ek yeri görüntüsü 29:41'deki zayıf evden ve paket içi yapı malzemesinden gelir; mesken kelimesinin tek başına bütün bu teknik ayrıntıları söylediği ileri sürülmez.","context_refs":["29:41"],"epistemic_status":"Güvenilir kanal kanıtına ve 29:41'in doğrudan ev karşılaştırmasına dayanan, birleştirilmiş yerel okuma.","finding_ref":"macro:fitted-dwelling-structure","mechanism":"Odaktaki mesken yerleşilmiş yeri görünür kanıt haline getirir; 29:41'de ev, örümceğin zayıf eviyle karşılaştırılır. Paket bu karşılaştırmayı dik duran destek, uygun ek yeri, çapraz parçalar ve birleşen yüzeylerin yük taşıması üzerinden kurar; böylece görünüş ile taşıma işlevi ayrışır.","reader_payoff":"Okur, yurtları yalnız manzaradaki harabe olarak değil, bir barınağın adını taşıyabilmesi için hangi birleşik işlevleri yerine getirmesi gerektiğini gösteren bir sınama olarak görür.","support_ids":["sup_0fe4b9ad036326e1a854","sup_3420e6e4734474286ad5","sup_9356307ac18b9b5d6571","sup_a18f9587bf0cab400ef8","sup_eef53953103112527e89"],"title":"Meskenin taşıyıcı bir düzenek olarak sınanması"},{"branch_refs":["root_000074/B003","root_000121/B002","root_000170/B004","root_000170/B005","root_000180/B002","root_001040/B002"],"candidate_ids":["cand_b0cdc9c11beba468f9e4"],"claim":"29:38'de yurtlardan açıkça belli olan şey, 29:35'in açık işaret ve akledenler diliyle birlikte, olay geçtikten sonra da görmeyi anlamaya ve iç kanıta yönlendiren korunmuş bir iz olarak görünür.","connection_refs":["conn_9be925dbfa8ea3474562"],"containment":"Bedenî görünürlük ve yurtların tanıklığı temel okumanın içinde kalır. İç kavrayış ve yön gösteren işaret, 29:35'in bağlamsal katkısıdır; odaktaki görme ifadesi yalnızca soyut bilgiye indirgenmez.","context_refs":["29:35"],"epistemic_status":"Güvenilir kanal desteği ve 29:35'in açık işaret bağlantısıyla temellendirilmiş bağlamsal okuma.","finding_ref":"macro:ruin-as-landmark","mechanism":"Odaktaki açığa çıkma fiili kanıtı doğrudan yurtlara bağlar ve son söz görerek kavramaya elverişli bir durum taşır. 29:35, yıkılmış kentten akledenler için açık bir işaret bırakıldığını söyleyerek aynı izi önce göze çarpan, sonra anlam açan, daha sonra içten doğrulayan bir harekete dönüştürür.","reader_payoff":"Harabe, olayın dekoru olmaktan çıkar; ayrılmış bir olayın ardından yönü ve anlamı koruyan bir işaret olarak okunur. Görmek ile kavramak arasındaki geçiş görünür hale gelir.","support_ids":["sup_16efca038eea03d64af6","sup_75174c86656e229a8ae6","sup_782eb4659a15f0af3da0","sup_7f527b731eb1e4e431f6","sup_e4e46767a633960cd763"],"title":"Kalıntının yön gösteren işarete dönüşmesi"},{"branch_refs":["root_000064/B001","root_000064/B003","root_000064/B004","root_000166/B002","root_000726/B003","root_000726/B004","root_001222/B001","root_001222/B003"],"candidate_ids":["cand_7b6ec7ef851717481779"],"claim":"29:38'deki meskenler, yakın bağlamdaki ev halkı ve seçilmiş koruyucularla birlikte, fiziksel yer olmanın yanında kimin içeride sayıldığı, kimin kabul edildiği ve hangi ilişkinin koruma sağladığı sorusunu da görünür kılar.","connection_refs":["conn_7957232d88bd0996251f","conn_314ac0eed46265bb9f9e"],"containment":"Meskenin fiziksel yer ve kalıntı anlamı korunur. Ev halkı, kabul ve koruyucu ilişki okumaları bağlamdan doğar; mesken kelimesi doğrudan kan bağı veya her tür topluluk anlamına genişletilmez.","context_refs":["29:31","29:32","29:41"],"epistemic_status":"Güvenilir kanal malzemesiyle, 29:31-32 ve 29:41'in yakın bağlamından çıkarılan ayrı bir sosyal barınak okuması.","finding_ref":"macro:shelter-as-belonging","mechanism":"Odaktaki yerleşim alanı, 29:31-32'de kent halkı, Lut ve ailesi üzerinden aidiyet ve istisna ilişkileriyle; 29:41'de ise Allah'tan başka edinilen koruyucuların ev benzetmesiyle çevrelenir. Böylece mesken, yaşayanlarını tanıyan ve koruyan bir ilişki düzeni olarak ikinci bir bağlam kazanır.","reader_payoff":"Okur, yurtların yalnız nerede yaşandığını değil, bir yerin veya ilişkinin gerçekten koruyucu sayılmasını hangi aidiyet ve kabul biçimlerinin mümkün kıldığını da görür.","support_ids":["sup_364e76cfc81601c6cf58","sup_748070bde56b5942dc55","sup_9d31931c52ebea1e09e9","sup_ded21f511c4f2aa8b1ae","sup_e0335dc4a16875673f98"],"title":"Barınağın aidiyet ve koruma ilişkisi"},{"branch_refs":["root_000166/B001","root_000170/B004","root_000222/B001","root_000499/B007","root_000521/B001","root_000726/B009","root_001036/B001","root_001054/B001","root_001281/B006","root_001397/B011","root_001684/B004","root_001687/B001"],"candidate_ids":["cand_64952ac6dfd1c0b90cf4"],"claim":"Yakın ayet dizisi, 29:38'in görünen yurtlarını geçmiş bir yıkımın izinden, yerleşik bedenleri, açık kanıtı, kibri ve suça bağlanan sonuçları sonunda zayıf bir koruyucu eve bağlayan başarısız bir güven düzeni olarak okumaya açar.","connection_refs":["conn_0f85d375955afae49954","conn_0df16f85c8c3d44467a1","conn_ffac51a6c5eb11e72aa0","conn_314ac0eed46265bb9f9e","conn_72e2690863f0e69d1ef1"],"containment":"Âyetin Âd ve Semûd'un yurtlarından görülen tarihsel kanıtı, Şeytan'ın işleri güzel göstermesi ve yoldan alıkoyması temel anlam olarak korunur. Birleşik güven mimarisi okuması legacy_unbound HFT kaydının yazar çıkarımıdır; 29:41'deki benzetmenin yalnızca yıkıntıların açıklaması olabileceği canlı alternatifi yerinde kalır.","context_refs":["29:37","29:39","29:40","29:41","29:43"],"epistemic_status":"Açık ayet metinleriyle temas eden, fakat legacy_unbound HFT sentezi nedeniyle temkinli ve çıkarımsal tutulmuş makro okuma.","finding_ref":"macro:stability-test","mechanism":"29:37 bedenleri kendi yurtlarında yere sabitler; odak ayet yurtlardan açıkça belli olan izi, işleri güzelleştirmeyi ve yoldan alıkoymayı verir; 29:39 açık kanıta rağmen büyüklük taslamayı, 29:40 her topluluğu suçu ile karşılayan sonuçları, 29:41 ise seçilmiş koruyucuları en zayıf evle karşılaştırır. 29:43'ün akledenler vurgusu bu zinciri okunabilir bir yapı sınamasına bağlar.","reader_payoff":"Okur, görünür bir yerleşim veya seçilmiş bir dayanağın yalnızca var görünmesinin yeterli olmadığını; kanıt karşısında yön verip hayatı taşıyıp taşıyamadığının sınandığını fark eder.","support_ids":["sup_01afe80fc3ba4dcd6405"],"title":"Yerleşik görünümün taşıma sınavı"},{"branch_refs":["root_000121/B001","root_000672/B010","root_001054/B001","root_001687/B001"],"candidate_ids":["cand_258d68d6010581d8496e"],"claim":"Keşifsel ve sınırlı bir maddi benzetme olarak, odaktaki yol ile görme ifadeleri 29:41'deki örümcek ve zayıflık görüntüsüyle buluştuğunda, güzelleştirmenin görme alanına ince bir ağ perdesi serdiği ve ayırt etmenin bu narin engelin altında sürdüğü düşünülebilir.","connection_refs":["conn_314ac0eed46265bb9f9e"],"containment":"Odaktaki yolun olağan güzergâh anlamı yerinde kalır; ağsı göz perdesi ilgili dalın uzak ve keşifsel maddi benzetmesidir, ٱلسَّبِيلِ için sözlük çevirisi değildir. 29:41 doğrudan örümcek ve zayıf ev yüzeyini sağlar; HFT'nin hedef morfolojisi ve çözülmemiş dal atıfları nedeniyle bu görüntü kesinleştirilmez.","context_refs":["29:41"],"epistemic_status":"Legacy_unbound HFT kaydından gelen, açıkça keşifsel ve sözlük anlamı olarak kullanılmayan sınırlı maddi analoji.","finding_ref":"macro:webbed-sight","mechanism":"Odaktaki yol olağan güzergâh anlamını taşırken son ifade görme yetisini öne çıkarır. 29:41'de örümceğin dokuduğu ev ve zayıflık birlikte verildiğinde, aynı yüzey teması yolu kapatan güçlü bir duvar yerine görüşü örtebilen hafif bir ağ görüntüsü üretir.","reader_payoff":"Okur, görebilen ve kavrayabilecek durumda olan insanların yine de yönlerinin değişebilmesini, engelin gücünden çok görüş alanını biçimlendiren aldatıcı bir örtü üzerinden de tasavvur edebilir.","support_ids":["sup_39e089abad690f68c898"],"title":"Görüş alanına serilen narin perde"},{"branch_refs":["root_000170/B004","root_000521/B001","root_000989/B001","root_001315/B003"],"candidate_ids":["cand_5b8e47a462dbae9cfa6e"],"claim":"Âd ve Semûd adları, 29:38'in görünür kılınma dili ve 29:40'ta her bir topluluğun suçu ile karşılanmasıyla birlikte, yalnız hatırlanan halk adları değil, her biri kendi izi ve sonucu incelenebilen vakalar gibi okunabilir.","connection_refs":["conn_ffac51a6c5eb11e72aa0"],"containment":"Âd ve Semûd'un topluluk adları olarak olağan kimliği korunur. Sayma bağlantısı Âd adının etimolojisi veya çevirisi değildir; 29:40'taki her biri ve suçla ilişkilenen sonuç, legacy_unbound HFT kaydının sınırlı biçimsel yankısını taşır.","context_refs":["29:40"],"epistemic_status":"Legacy_unbound HFT kaydına dayanan, bölünmüş kök çağrışımını kesin etimolojiye çevirmeyen keşifsel bağlamsal okuma.","finding_ref":"macro:case-ledger","mechanism":"HFT kaydı Âd özel adının içindeki sayma çağrışımını, odaktaki açığa çıkma dilini ve sonraki her biri ifadesini 29:40'taki suç-sonuç bağlantısıyla birleştirir. Böylece isimler, yurtlardan görülen izleri ve ayrı ayrı karşılanan sonuçları taşıyan bir kayıt düzeninin başlıkları gibi iş görür.","reader_payoff":"Okur, isimlerin peş peşe anılmasını genel bir tarih listesi olarak bırakmayıp her örneği görünür kanıt ve kendine ait sonuçla birlikte okunabilen bir dosya düzeni olarak kavrayabilir.","support_ids":["sup_c02306ffdaee4fc8e150"],"title":"Adların incelenebilir vakalara açılması"}],"friction_notes":["Üç HFT kaydında hedef morfolojisi sunulmuyor; dal, kök ve kelime konumu bilgileri paket tarafından atıflı ve kısmen çözülmemiş olarak nitelendiriliyor. Bu nedenle HFT bulguları görünür tutuldu, fakat keşifsel veya temkinli statü ve açık containment ile sınırlandı.","Bağlantı satırlarında hedef ayetlerin Arapça yüzeyi mevcut olsa da hedef morfolojisi ve bağımsız sözlük çözümlemesi yok; bağlantılar yalnızca verilen ilişki mekanizmaları kadar kullanıldı.","Paket, aşamalı okuyucu yanıtlarının veya okuyucu yürüyüşlerinin içeriklerini sunmuyor; bu kaynakların sağlayacağı okuyucu-durumu değişimi hakkında çıkarım yapılmadı.","29:0 prefatory basmala olarak otomatik bağlam üyesi; odak ayet için ayrı bir taşıyıcı, mekanizma veya okuma değişimi vermediği için bulguya dönüştürülmedi."],"identity":{"authoring_request_sha256":"6268415ea13c3de76d82be5e05bdd0458b84363e15e7a535f785108e4449e62b","ayah_ref":"29:38","lane":"macro","lane_packet_sha256":"1f0888d7dd1f1d3aa7ad6dfb5ff07f1597b3ec70fdb3d67efc24a15f370c7b7b"},"lane":"macro","movements":[{"draft_prose":"Âyet ilk bakışta Âd ile Semûd'un yok oluşunu, yurtlarından geriye kalan açık izi ve Şeytan'ın onların yaptıklarını güzel göstererek onları yoldan alıkoymasını anlatır. Sıra önemlidir: geride duran yurtlar tanıklık eder; ardından cazip gösterilen işler, onların anlayabilecek durumda oldukları halde yoldan ayrılmasına dönüşür. {ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:bilinen yol} bu temel anlamı taşır.\n\nYol kesme anlatısının hemen önceki bağlamda belirginleşmesiyle alıkoyma, insanların ve kaynaklara ulaşmanın sürdürdüğü işlek güzergâhı bozan somut bir eylem olarak da duyulur. Yol yalnız varılacak yön değildir; başkalarının ilerleyebilmesini sağlayan geçiştir. Böylece güzel gösterilen işler, içeride hoş görünen fakat dışarıda başkalarının yolunu kesebilen eylemler olarak görünür. Bu ek görüntü temel anlamı değiştirmez; yoldan alıkoymanın dışa dönük etkisini belirginleştirir.","finding_refs":["macro:road-cutting-mobility"],"movement_key":"road-mobility"},{"draft_prose":"{ar:مَّسَٰكِنِهِمْ, tr:mesâkin, gloss:yurtları} sözü, tek başına, yok olmuş bir topluluğun geride kalan meskenlerini ve bu meskenlerden görülen açık kanıtı gösterir. Yakınındaki örümcek evi benzetmesiyle birlikte düşünüldüğünde ev, yalnız üstü örten bir kabuk değil, dik duran destekleri, uygun ek yerleri ve yükü dağıtan parçaları bulunan bir düzenek olarak görünür.\n\nBu bakış yurtları geriye dönük olarak bir yapı sınamasına çevirir: bir şeyin barınak diye görünmesi ile gerçekten taşıması aynı şey değildir. Örümceğin evi, ev adını korurken zayıflığı açığa çıkarır; yurtlardan kalan iz de geçmişi göstermekle birlikte, bir yerleşimin hayatı güvenle taşıyıp taşımadığını düşündürür. Tarihsel kanıt yerinde kalır, ona yapının işleyişini sınayan ikinci bir görüntü eklenir.","finding_refs":["macro:fitted-dwelling-structure"],"movement_key":"fitted-dwelling"},{"draft_prose":"Âyet kanıtı uzakta verilmiş bir haber olarak değil, yurtların içinden açığa çıkan bir açıklık olarak kurar: size belli olan şey, geride duran meskenlerden görülür. Sonra aynı yakın bağlamda yıkılmış kentten akledenler için açık bir işaret bırakıldığı söylenir. Böylece kalıntı önce göze çarpar, sonra yön gösterir, ardından olay artık geride kalmışken anlamı koruyan bir iç kanıta dönüşür.\n\n{ar:تَّبَيَّنَ, tr:tebeyyene, gloss:açığa çıkmak} ile {ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:görerek kavrayanlar} birlikte okunduğunda görme ve kavrama birbirinden kopmaz. Yurtların görünür tanıklığı, insanların anlayabilecek durumda olmalarıyla birleşir; açık iz, bakışın içinden geçen bir anlama yolu açar.","finding_refs":["macro:ruin-as-landmark"],"movement_key":"ruin-landmark"},{"draft_prose":"Yurtlar fiziksel yer olarak kalır; fakat yakın bağlam bu yerin kimleri içine aldığı sorusunu da açar. Kentin halkı, Lut ve ailesi, ardından bir başkasını Allah'tan ayrı koruyucu edinme benzetmesi, barınmanın yalnız duvarla kurulmadığını gösteren bir dizi oluşturur. Bir ev halkı, yalnız aynı yerde bulunan kişiler değil, tanınan, kabul edilen ve korunması beklenen kimselerdir.\n\nBu yüzden mesken, hem yaşanan yer hem de güven veren bir aidiyet ilişkisi gibi duyulur. Örümcek evinin zayıflığı bu toplumsal görüntüyü keskinleştirir: koruyucu adı taşıyan bir ilişki, gerçekten koruyup korumadığıyla sınanır. Fiziksel yurtların bıraktığı tarihsel iz korunur; ona, kimin içeride sayıldığı ve hangi bağın barınak işlevi gördüğü sorusu eklenir.","finding_refs":["macro:shelter-as-belonging"],"movement_key":"shelter-belonging"},{"draft_prose":"Âyet tek başına Âd ve Semûd'un yurtlarından görünen kanıtı, Şeytan'ın işleri güzel göstermesini ve anlayabilecek durumda oldukları halde onları yoldan alıkoymasını söyler. Yakın ayetlerde önce insanların kendi yurtlarında yere kapanmış halde kalması, sonra açık kanıta rağmen büyüklük taslamaları, ardından her topluluğun kendi suçu ile karşılaşması ve sonunda seçilmiş koruyucuların en zayıf eve benzetilmesi gelir.\n\nBu sıra, yurtların yalnız geçmişteki yıkımın izleri olmasının ötesinde, yerleşik görünen bir düzenin gerçekten taşıyıcı olup olmadığını soran bir sınama gibi okunabilir. Görünürlük, kibir ve seçilmiş dayanak aynı düzlemde buluşur: bir düzenin var görünmesi, açık kanıt karşısında yön vermesi veya hayatı taşıması anlamına gelmez. Âyetin tarihsel bildirimi burada yerini korurken, yakın dizi güvenli sanılan yapının içindeki kırılganlığı da görünür kılar.","finding_refs":["macro:stability-test"],"movement_key":"stability-test"},{"draft_prose":"{ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:yol} sözü burada bilinen güzergâhı gösterir; sonundaki görme ifadesiyle birlikte, aynı sözün uzak bir maddi görüntüsü de duyulabilir. Örümcek evinin zayıflığıyla yan yana geldiğinde güzelleştirme, görme alanının üzerine serilen ince ve ağsı bir perde gibi tasavvur edilir: ayırt etme yetisi sürer, fakat yönü narin bir örtü biçimlendirir.\n\nBu görüntü yol kelimesinin olağan çevirisinin yerine geçmez. Yoldan alıkoymanın yanında, gören ve kavrayabilecek durumda olan bir topluluğun önüne, gücü büyük görünmeyen fakat bakışın yönünü değiştiren bir perde konabileceğini düşündüren keşifsel bir benzetme olarak kalır.","finding_refs":["macro:webbed-sight"],"movement_key":"webbed-sight"},{"draft_prose":"Âyetin başındaki Âd ve Semûd adları, yurtlardan görülen açık iz ile birlikte anılır. Yakınındaki devam cümlesi her topluluğu kendi suçu ile karşılanan ayrı bir sonuç içinde ele alınca, adlar yalnız geçmişten hatırlanan halkların başlıkları olarak kalmaz; her biri kendi izi ve karşılığı bulunan incelenebilir vakalara açılır.\n\nÂd adında beliren sayma çağrışımı bu düzeni keşifsel olarak destekler; onu bir etimoloji veya çeviri diye almak gerekmez. Böylece isim, görünür yurt ve ayrı sonuç aynı kayıt hareketinde buluşur: tarihsel örnekler topluca anılırken her birinin kendi eylemi ve karşılığı da görünür kalır.","finding_refs":["macro:case-ledger"],"movement_key":"case-ledger"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</macro_contribution_json>

## Global contribution

<global_contribution_json>
{"ayah_ref":"29:38","candidate_decisions":[{"candidate_id":"cand_3bc56997b4f3d1787b11","decision":"accept","finding_refs":["global:adorned-evaluation-blocks"],"reason":"Güvenilir çapraz-çalışma kaydı, 29:38'in görünür yurt, içgörü, süsleme ve alıkoyma ilişkisini aynı odak ankrajlarında birlikte veriyor; bu ilişki F1'de korunuyor."},{"candidate_id":"cand_029f6cac1f2d21898055","decision":"represented","finding_refs":["global:adorned-evaluation-blocks"],"reason":"Süslenmiş görme üzerinden engel kurulması, F1'de 29:38'in aynı صَدَّ ve زَيَّنَ ilişkisiyle aynen taşınıyor."},{"candidate_id":"cand_92731051cd9e27e99bcf","decision":"narrow","finding_refs":["global:trace-to-guidance"],"reason":"29:41-43'te görünür kanıtın kavranmış bir benzetme içinde yön kazanması anlamlıdır; ancak kayıt yapılandırılmış dal ankrajı vermediği için yalnız kanıttan rehberliğe geçişle sınırlanıyor."},{"candidate_id":"cand_05ceb0391bfa78b1bd57","decision":"represented","finding_refs":["global:trace-to-guidance"],"reason":"Yurtların açık delil, içgörünün mevcut kapasite, yönün ise yine de kaybedilebilir oluşu F2'nin aynı bulgusudur."},{"candidate_id":"cand_012aa490468209c9ba9f","decision":"represented","finding_refs":["global:adorned-evaluation-blocks"],"reason":"Süslenmiş işin değerlendirmeyi ele geçirip yolu kapatması F1'in taşıdığı aynı mekanizmadır."},{"candidate_id":"cand_ffbcbe8292074b9be873","decision":"represented","finding_refs":["global:knowledge-without-conversion"],"reason":"29:61'de doğru yöneliş ile insanların çevrilmesi üzerinden kurulan kozmik karşılaştırma, F3'te içgörünün yön ve eyleme bağlanmaması olarak zaten taşınıyor."},{"candidate_id":"cand_164728c5d0819990bd37","decision":"narrow","finding_refs":["global:knowledge-without-conversion"],"reason":"Müstebsirîn'in ahlaki basiret, dünyevi kavrayış veya ikisini taşıyabilmesi açık bir sınırdır; kayıtsız özet bağımsız global mekanizma olarak değil F3'ün sınırlandırmasında tutuluyor."},{"candidate_id":"cand_a09ff26fc7469fadf112","decision":"narrow","finding_refs":["global:socialized-obstruction"],"reason":"Sosyal yayılımın aşamalarının her biri ankrajlı olsa da tek bir nedensel ok olarak okunması okuyucu çıkarımıdır; F6'da bu sınırlama korunuyor."},{"candidate_id":"cand_49c0ee7683fa531b82a5","decision":"reject","finding_refs":[],"reason":"Kayıt, ağsı yol ve sayılmış defter imgelerini yalnız dal yankısı olarak sınırlıyor; odak kelimesine bağımsız değişen okuma ve somut taşıyıcı sunmuyor."},{"candidate_id":"cand_b9670a0364a325c0bdc3","decision":"represented","finding_refs":["global:knowledge-without-conversion"],"reason":"Cehaletten bilgi ve doğru sözle birlikte süren yön kaymasına geçiş, F3'teki 29:47, 29:49, 29:61 ve 29:63 ankrajlı bulguyla aynen taşınıyor."},{"candidate_id":"cand_8e5bb7c83a6252372acc","decision":"narrow","finding_refs":["global:rival-route-burden","global:socialized-obstruction"],"reason":"Özet iki ayrı packet-grounded mekanizmayı, rakip yol ve yük devri ile toplumsallaşmış engeli, tek bir doğrusal iddia gibi birleştiriyor; bu iki sınırlı bulguya ayrıldı."},{"candidate_id":"cand_a109ebb6dd938c02de4d","decision":"narrow","finding_refs":["global:trace-to-guidance","global:security-belief-allocation"],"reason":"Meskenlerin saha kanıtı ve güvenlik görünüşünün kırılganlığı F2 ve F9'a bölündü; yapılandırılmamış zayıf-ev eşlemesi ayrıca ileri sürülmedi."},{"candidate_id":"cand_da1e3a1dbde3882b4cb7","decision":"narrow","finding_refs":["global:state-dependent-salience","global:embodied-inhibition","global:effort-opens-paths"],"reason":"Eylem düzeyindeki üç karşılık, durum-değişen çekicilik, bedenleşmiş fren ve gayretle açılan yollar, F7, F8 ve F10'a ayrı mekanizmalar olarak dağıtıldı."},{"candidate_id":"cand_23dbd9d5b8a7d6b9a45c","decision":"reject","finding_refs":[],"reason":"Bu, somut odak dönüşü ve ayrı mekanizma vermeyen meta düzey bir bütün-sûre özeti; split-root uyarısı da bağımsız bir bulgu taşıyıcısı değil."},{"candidate_id":"cand_2eba703117e453f48de4","decision":"accept","finding_refs":["global:discernment-under-assay"],"reason":"29:2-4 ile 29:38 arasında açık odak ankrajı, sınama mekanizması, değişen okuma, canlı alternatif ve HFT kanıt zinciri sağlıyor; F4'te sınırlı çıkarım olarak korunuyor."},{"candidate_id":"cand_3da929e6a62922e844d9","decision":"accept","finding_refs":["global:rival-route-burden"],"reason":"29:12-13'teki rakip yol ve yük devri, صَدَّ ve ٱلسَّبِيلِ ilişkisine somut dönüş ve okuyucu payı sağlıyor; alternatif polemik okuması containment'ta tutuluyor."},{"candidate_id":"cand_c8da6ae730c2e7bb770d","decision":"accept","finding_refs":["global:socialized-obstruction"],"reason":"29:17, 29:25 ve 29:29, üretimden bağa, toplantıya ve yol kesmeye uzanan açık aşamalarla odaktaki süsleme-alıkoymayı değiştiriyor; nedensel zincir nitelendiriliyor."},{"candidate_id":"cand_0d0a8651cf8736a990ff","decision":"accept","finding_refs":["global:trace-to-guidance"],"reason":"29:19, 29:20 ve 29:35 ile odak meskeni arasında seyahat, bakış, bırakılmış iz ve akılla okuma mekanizması açıkça bağlanıyor; F2'de korunuyor."},{"candidate_id":"cand_18fd8cc8b4fefc8c9168","decision":"accept","finding_refs":["global:embodied-inhibition"],"reason":"29:45, odaktaki güzel gösterilmiş işlere karşı tekrarlı ve eylem düzeyinde bir alıkoyma ilişkisi veriyor; F8'de alternatif statü korunuyor."},{"candidate_id":"cand_eff6f2741bc0415655e9","decision":"accept","finding_refs":["global:knowledge-without-conversion"],"reason":"29:47, 29:49, 29:61 ve 29:63 açık Arapça yüzeyleri, iç bilgi ve doğru sözle birlikte süren inkâr ve yön kaymasını odak müstebsirîn'e geri bağlıyor."},{"candidate_id":"cand_2e491022b5747ed267d7","decision":"accept","finding_refs":["global:state-dependent-salience"],"reason":"29:64-65'te oyalanma, kriz anında arınma ve kurtuluş sonrası geri dönüş, zeyyene'nin durum-bağımlı dikkat okuması için tam trigger ve return path sağlıyor."},{"candidate_id":"cand_21f509a01c539ee2988d","decision":"accept","finding_refs":["global:security-belief-allocation"],"reason":"29:67'de görme, güvenlik, çevredeki kapılma ve yanlış olana inanma aynı açık sahnede birleşiyor; odak içgörüsüne dönüş ve canlı kök alternatifi korunuyor."},{"candidate_id":"cand_f2ec08c088717523861f","decision":"accept","finding_refs":["global:effort-opens-paths"],"reason":"29:69'da gayret, hidayet ve çoğul yollar, odaktaki alıkonmuş tekil yolu ters yönde aydınlatan açık bir karşı-sequence kuruyor."}],"coverage_complete":true,"findings":[{"branch_refs":["root_000121/B002","root_000170/B004","root_000660/B002","root_000672/B001","root_000796/B003","root_000848/B001","root_000848/B005","root_001046/B001"],"candidate_ids":["cand_3bc56997b4f3d1787b11","cand_029f6cac1f2d21898055","cand_012aa490468209c9ba9f"],"claim":"Görünür yurtlar ve iç kavrayış mevcutken, yapılan işleri çekici gösteren değerlendirme kanıt ile tanınan yol arasına bir engel koyabilir.","connection_refs":["conn_e32caea43e40d93f2f99","conn_b7e144562c65ebed7d06","conn_d91329795dd8bcbddbfc"],"containment":"Âyetin açık okuması, Şeytanın onların işlerini güzel gösterip onları bilinen yoldan alıkoymasıdır; değerlendirmenin araya giren mekanizma oluşu bu okumanın içine eklenir. Dağ ve engel imgeleri ile zihinsel ara adım, sınırlandırılmış yorum imkânları olarak kalır.","context_refs":["27:24","16:63","47:14"],"epistemic_status":"Odak kelimeleri ve doğrudan paralel ayet yüzeyleriyle desteklenen, değerlendirme ile yön arasındaki ara adımı yazar çıkarımı olarak koruyan bulgu.","finding_ref":"global:adorned-evaluation-blocks","mechanism":"Odaktaki زَيَّنَ ve صَدَّ ilişkisi, daha geniş ayetlerde aynı süsleme-yoldan çevirme dizisiyle ve süslenmiş kötü işin açık kanıtın karşısına konmasıyla birlikte okunuyor. Böylece alıkoyma, kanıtın yokluğundan değil, eylemin görünüşünü değerlendiren ara hareketten doğan bir yön kayması olarak beliriyor.","reader_payoff":"Okur, yıkıntıların verdiği dış kanıt ile مُسْتَبْصِرِينَ kelimesinin taşıdığı iç kavrayışın gerçekten mevcut kaldığını, buna rağmen yapılan işlerin değerlendirilmesi üzerinden yolun kapanabildiğini görür.","support_ids":["sup_3e1351fa35815a1bbc9f","sup_a77d2794b80076f119e6","sup_8ddab411dc46fedd646f"],"title":"Süslenen değerlendirme ile yol arasındaki engel"},{"branch_refs":["root_000074/B003","root_000121/B002","root_000170/B004","root_000180/B002","root_000531/B001","root_000726/B002","root_000726/B009","root_000769/B001","root_001036/B001","root_001520/B001"],"candidate_ids":["cand_92731051cd9e27e99bcf","cand_05ceb0391bfa78b1bd57","cand_a109ebb6dd938c02de4d","cand_0d0a8651cf8736a990ff"],"claim":"Meskenler geçmişten kalan sabit bir hatırlatma olmanın yanında, dolaşma, bakma ve ilişki kuran kavrayış yoluyla davranışı uyaran okunabilir bir saha kanıtına dönüşür.","connection_refs":["conn_f82a1f53698aaf8960e0","conn_21cac76e314863ec4004","conn_4d8cc3a36b75a1c48133"],"containment":"Âyetin yurtları görünür bir kanıt olarak göstermesi korunur. Seyahat buyruğunun her durumda doğrudan bu harabelere yöneldiği söylenmez; sonraki benzetmenin de kanıta yön veren tek açıklama olduğu ileri sürülmez.","context_refs":["29:19","29:20","29:35","29:41","29:42","29:43"],"epistemic_status":"Seyahat, görünür iz ve kavrayış ankrajlarını birleştiren bağlam çıkarımı; seyahat buyruğunun bu meskenlere doğrudan yönelip yönelmediği ve benzetme bağının kapsamı açık tutuluyor.","finding_ref":"global:trace-to-guidance","mechanism":"Yeryüzünde dolaşma ve yönelmiş bakış, bırakılmış açık iz ve odaktaki meskenlerle birleşiyor; sonraki benzetme de görünen kanıtın kavranmış bir ilişki içinde yön kazanmasını istiyor. Bu dönüş, مُسْتَبْصِرِينَ ile taşınan iç kapasitenin tek başına rota üretmediğini, görünür iz ile kavrayışın birlikte işlenmesi gerektiğini açıyor.","reader_payoff":"Okur, yurtları yalnızca geçmiş bir yıkımın kalıntısı olarak değil, incelenebilen, bağlama yerleştirildiğinde uyarıya dönüşen bir kanıt alanı olarak görür; görme ile yön bulma arasındaki fark belirginleşir.","support_ids":["sup_4ab71827ffe71251d705","sup_b38252d24f40c2eaccc8","sup_d11bec9f45ff2c5c6a9b","sup_517a678fb16d212c1d73"],"title":"Yurtların okunabilir saha kanıtına dönüşmesi"},{"branch_refs":["root_000041/B001","root_000074/B003","root_000121/B002","root_000224/B001","root_000848/B001","root_000849/B004","root_001036/B001","root_001040/B001","root_001272/B001"],"candidate_ids":["cand_ffbcbe8292074b9be873","cand_164728c5d0819990bd37","cand_b9670a0364a325c0bdc3","cand_eff6f2741bc0415655e9"],"claim":"Müstebsirîn nitelemesi tam anlamıyla gerçek olabilir: içte taşınan işaretler, bilgi ve doğru söz, inkârın, çıkarım hatasının veya yön kaymasının sona ermesini kendiliğinden sağlamaz.","connection_refs":["conn_45e309b5224a32e5e954","conn_f39581c33e507316db5a","conn_65160f791a23b683567f"],"containment":"Âyet onları kavrayış sahibi sayarken alıkonulduklarını söylemeye devam eder; bu okuma onları aslında kör ilan etmez. İçgörünün ahlaki basiret, dünyevi beceri veya ikisinin kesişimi olması seçilmez; doğru sözlerin polemik itiraflar olarak okunması da canlı kalır.","context_refs":["29:47","29:49","29:61","29:63"],"epistemic_status":"Odak ve sonraki ayet yüzeyleriyle desteklenen, içgörünün eyleme bağlanmamasını öneren içerilmiş yorum; müstebsirîn'in ahlaki ve pratik aralığı açık bırakılıyor.","finding_ref":"global:knowledge-without-conversion","mechanism":"İçlerinde açık ayetler bulunan ve bilgi verilen kişilerle bilerek inkârın yan yana getirilmesi, ardından doğru cevabın hemen sonrasında yönün tersine çevrilmesi ve düşünmeyi sağlayan imkânın işlememesi, kavrayış ile bağlılık arasındaki kopukluğu görünür kılıyor. Aynı bağlamda güneş ve ayın düzenli yönelişi ile insanların doğru yönden çevrilmesi de algı ile yönelişin ayrı haritalarda kalabileceğini gösteriyor.","reader_payoff":"Okur, yoldan alıkonulmayı yalnızca bilgisizlik veya görme eksikliği olarak okumak zorunda kalmaz; insanın görüp bilmesi, hatta doğru konuşması ile bunu kararına ve işine bağlaması arasında ayrı bir eşik olduğunu fark eder.","support_ids":["sup_b34bc56e34672031ec9e","sup_9e3741af381d493b97d0","sup_424d4235f249d65ec733","sup_386ea38831259af5594e"],"title":"Bilginin eyleme bağlanmaması"},{"branch_refs":["root_000121/B002","root_000348/B003","root_000852/B004","root_001046/B001","root_001128/B001"],"candidate_ids":["cand_2eba703117e453f48de4"],"claim":"İçgörü, yalnızca elde bulunan bir yetenek değil, yapılan iş ve hüküm içinde sınanan bir kapasite olarak da belirir; süslenmiş işler bu kapasitenin değerlendirmeden eyleme geçişteki sınırını görünür kılar.","connection_refs":[],"containment":"29:2-4'ün sınama düzeni, odaktaki kelimeye davranışta ölçülen bir imkân baskısı ekler; müstebsirîn'in yalnız dünyevi beceri veya yalnız ahlaki nitelik olması dışlanmaz.","context_refs":["29:2","29:3","29:4"],"epistemic_status":"29:2-4 ile 29:38 arasındaki HFT bağlam farkından türeyen, sınama mekanizmasını yazar çıkarımı olarak sunan sınırlı bulgu.","finding_ref":"global:discernment-under-assay","mechanism":"Açılıştaki sınama, doğruluğun yapılan işte görünür olması ve kötü işin bozuk hükümle yan yana gelmesi, 29:38'in sonundaki kavrayış nitelemesine bir davranış ölçüsü ekliyor. Böylece süsleme, yalnızca algıyı değiştiren bir görüntü değil, kavrayışın eylemi yönetip yönetmediğini ortaya çıkaran bir sınama ortamı oluyor.","reader_payoff":"Okur, kavrayışın değerini daha fazla bilgi biriktirmekte değil, hükmün harekete dönüşmesinde izleyebileceği bir ölçü olarak görür; âyetin son kelimesi önceki eylem zincirine geri bağlanır.","support_ids":["sup_cff11748f7e10c72e06a"],"title":"Kavrayışın davranışta sınanması"},{"branch_refs":["root_000175/B001","root_000202/B007","root_000357/B003","root_000672/B001","root_000848/B001"],"candidate_ids":["cand_8e5bb7c83a6252372acc","cand_3da929e6a62922e844d9"],"claim":"Yoldan alıkoyma, yolu ortadan kaldırmaktan çok, izlenmesi kolay bir rakip güzergâhı ve sonuçlarını başkasına yükleme vaadini birlikte kurarak da işleyebilir.","connection_refs":[],"containment":"Odaktaki fiil gerçek bir yoldan alıkoymayı anlatır; rakip yol ve yük devri, bu alıkoymanın bağlam içinde nasıl işleyebileceğine dair ek resimdir. 29:12-13'teki yük polemiğinin tek mekanizma olduğu söylenmez.","context_refs":["29:12","29:13"],"epistemic_status":"Açık ayet ankrajlarıyla desteklenen toplumsal davet ve yük devri okuması; yük aktarımı ile odaktaki saptırmanın bağı yorum düzeyinde tutuluyor.","finding_ref":"global:rival-route-burden","mechanism":"Başka bir yerdeki bizden yana yolu izleme çağrısı, yanlışların yükünü başkasının taşıyacağı sözüyle birleştiriliyor; hemen sonraki ayet bu sözün kişisel ve ek yükleri çoğalttığını açıyor. Bu dizi, odaktaki صَدَّ ve ٱلسَّبِيلِ ilişkisini toplumsal bir davet ve sahte güven üzerinden somutlaştırıyor.","reader_payoff":"Okur, alıkonmayı yalnızca kişinin içinde oluşan bir yön şaşması olarak değil, sosyal güven veren bir anlatının insanı başka bir yola sokması olarak da görür; sorumluluğun devredilebileceği vaadinin yolu nasıl çekici kıldığı belirginleşir.","support_ids":["sup_39a2d31694bc95cd1f3e","sup_0843c8dd4c0817b7ca59"],"title":"Rakip yol ve devredilen yük"},{"branch_refs":["root_000041/B002","root_000434/B007","root_000660/B002","root_000672/B001","root_001046/B001","root_001240/B023","root_001487/B003","root_001550/B006","root_001634/B001"],"candidate_ids":["cand_a09ff26fc7469fadf112","cand_8e5bb7c83a6252372acc","cand_c8da6ae730c2e7bb770d"],"claim":"Süsleme, tek tek kişilerin iç değerlendirmesinde kapanmayıp üretilmiş bir değeri ortak bağa, kamusal kabule ve sonunda başkalarının yolunu kesen davranışa dönüştürebilir.","connection_refs":[],"containment":"Odaktaki güzel gösterme ve yoldan alıkoyma korunur; üretim, sevgi, toplantı ve yol kesmenin tek bir nedensel zincir olması yazar çıkarımıdır. Bu sahneler birbirinden bağımsız özellikler olarak da okunabilir.","context_refs":["29:17","29:25","29:29"],"epistemic_status":"Birden çok açık ayet yüzeyini bir araya getiren HFT çıkarımı; aşamaların tek bir yayılım zinciri olarak okunması kesinleştirilmiyor.","finding_ref":"global:socialized-obstruction","mechanism":"Yanlışın üretilmesi, insanlar arasında karşılıklı bağ kurulması, topluluk önünde sergilenmesi ve yol kesme eylemi ayrı ayetlerde görünür hale geliyor. Odaktaki güzel gösterilmiş işler böylece yalnızca kişinin kendi yaptığı şeyler değil, paylaşılan ve tekrarlanan bir yönlendirme düzeni olarak okunabiliyor.","reader_payoff":"Okur, alıkoymanın toplumsal biçimini görür: çekici gösterilen iş insanları birbirine bağlar, ortak bir norm gibi sergilenir ve bu norm başkalarının geçeceği yolu da kapatabilir.","support_ids":["sup_061959718e9b87881e21","sup_39a2d31694bc95cd1f3e","sup_2731278a47385c012147"],"title":"Süslemenin toplumsal engel oluşu"},{"branch_refs":["root_000430/B004","root_000660/B002","root_000791/B002","root_001332/B001","root_001358/B001","root_001382/B001","root_001476/B001"],"candidate_ids":["cand_da1e3a1dbde3882b4cb7","cand_2e491022b5747ed267d7"],"claim":"Süslenmiş işlerin etkisi kalıcı bir körlükten çok, hangi çekiciliğin davranışı yönettiğini değiştiren durum-bağımlı bir dikkat düzeni olarak da okunabilir.","connection_refs":[],"containment":"Süsleme ve sapma âyetteki asli anlatıdır; dikkat rejiminin krizle değişmesi buna eklenir. Bu okuma, yalnızca edebî tutarsızlık veya kalıcı körlük açıklamalarından birini seçmez.","context_refs":["29:64","29:65"],"epistemic_status":"29:64-65 sırasına dayanan durum-bağımlı dikkat okuması; metinsel durum değişiminin psikolojik yasa olduğu ileri sürülmüyor.","finding_ref":"global:state-dependent-salience","mechanism":"Oyalanma ve amaçsız eylem tasvirinden sonra tehlike, rakip dayanakları ayıklayıp özel bir yönelişi görünür kılıyor; kurtuluşun ardından eski ortaklaştırma geri dönüyor. Bu sıra, odaktaki زَيَّنَ fiilini kavrayışın varlığını silen sabit bir durum yerine, eylem üzerindeki dikkat değişimiyle ilişkilendiriyor.","reader_payoff":"Okur, bir insanın bildiğini bir anda kaybetmesi ile bildiğinin farklı şartlarda farklı bir çekicilik tarafından yönetilmesi arasındaki farkı görür; kriz anındaki arınma ve sonrasındaki geri dönüş aynı sahnede belirir.","support_ids":["sup_43f9d1d609f0ab5d773b","sup_891d2200b6fc717ec68b"],"title":"Değişen dikkat ve çekicilik düzeni"},{"branch_refs":["root_000660/B002","root_000879/B003","root_000885/B001","root_001046/B001","root_001560/B001"],"candidate_ids":["cand_da1e3a1dbde3882b4cb7","cand_18fd8cc8b4fefc8c9168"],"claim":"Kavrayışın yönetime dönüşmesi, çekici gösterilen işe karşı tekrarlanan ve bedensel bir yönelişin eylem düzeyinde fren oluşturmasıyla da açıklanabilir.","connection_refs":[],"containment":"Odaktaki işleri güzel gösterme ve alıkoyma korunur; ibadetin eylem düzeyinde fren oluşturması kesin bir psikolojik yasa değil, metinler arası bir karşı mekanizma okumasıdır. Bu bağın normatif bir vaat olarak okunması da canlıdır.","context_refs":["29:45"],"epistemic_status":"29:45'teki eylem düzeyi ilişkiyi odaktaki süsleme ile buluşturan, sınırları açık bir bağlam çıkarımı.","finding_ref":"global:embodied-inhibition","mechanism":"Daha sonraki ayet, tekrarlanan ibadet pratiğini çirkin eylemden alıkoyma ilişkisi içinde kuruyor ve dikkati insanların ürettiği işlere geri getiriyor. Bu, odaktaki süsleme ile alıkoyma arasına yalnızca daha fazla bilgi değil, davranışta çalışan bir karşı düzenek yerleştiriyor.","reader_payoff":"Okur, içgörünün tek başına yeterli sayılmadığı yerde, tekrar edilen yönelişin değerlendirmeyi eylemden önce durdurabilecek bir alışkanlık alanı açtığını görür.","support_ids":["sup_43f9d1d609f0ab5d773b","sup_90522d6b1c956355c011"],"title":"Eylemde tekrarlanan fren"},{"branch_refs":["root_000054/B001","root_000121/B002","root_000127/B001","root_000423/B001","root_000531/B001"],"candidate_ids":["cand_a109ebb6dd938c02de4d","cand_21f509a01c539ee2988d"],"claim":"Görme, güvenlik ve inanma aynı sahnede buluştuğunda, güvenli alanı doğru seçmek ile güveni doğru nesneye bağlamak birbirinden ayrılabilir.","connection_refs":[],"containment":"Odaktaki kavrayış imkânı ve yoldan alıkoyma korunur; güvenlik ile inanmanın aynı kökte bağlanmasının nedensel kuvveti açık bir alternatif olarak bırakılır. Görünen güvenli alanın bütün anlamı belirlediği sonucuna gidilmez.","context_refs":["29:67"],"epistemic_status":"29:67'nin açık sahnesi ve odaktaki içgörü ankrajıyla desteklenen yorum; ortak kök ile güven tahsisi arasındaki kuvvet yazar çıkarımı olarak tutuluyor.","finding_ref":"global:security-belief-allocation","mechanism":"Güvenli bir alan ile çevresindeki insanların kapılıp götürülmesi birlikte görülüyor; ardından güvenlik ve inanma dilini bağlayan aynı kök, güvenin yanlış olana yönelmesiyle karşılaşıyor. Bu sahne, odaktaki içgörüyü koruyarak kanıtın ayrıştırılması ile aidiyet ve güven tahsisinin farklı işlemler olduğunu açıyor.","reader_payoff":"Okur, kişinin gerçeği hiç seçemediğini varsaymadan, gördüğü ayrım ile bağlandığı nesnenin farklı olabileceğini fark eder; maddi güvence ve ona yüklenen inanç arasındaki çatlak görünür olur.","support_ids":["sup_d11bec9f45ff2c5c6a9b","sup_a9f84032e1d82087f211"],"title":"Görülen güvenlik ile bağlanılan nesne"},{"branch_refs":["root_000268/B001","root_000672/B001","root_000848/B001","root_001583/B001"],"candidate_ids":["cand_da1e3a1dbde3882b4cb7","cand_f2ec08c088717523861f"],"claim":"Kavrayışın yola dönüşmesi, yalnızca daha iyi görmekten değil, gayretin yönlendirmeyle karşılaşıp yeni geçiş yolları açmasından da okunabilir.","connection_refs":[],"containment":"Odaktaki tekil bilinen yoldan alıkoyma korunur; gayretin çoğul yollarla karşılık bulması, tekil ve çoğul biçimler arasındaki farkın yalnızca üslup olabileceğini dışlamayan ek bir okumadır.","context_refs":["29:69"],"epistemic_status":"29:69 ile odaktaki yol fiilini karşılaştıran, gayret-yol dönüşümünü yazar çıkarımı olarak nitelendiren bulgu.","finding_ref":"global:effort-opens-paths","mechanism":"Son ayet gayreti, hidayeti ve çoğul yolları aynı hareket içinde birleştiriyor. Odaktaki ٱلسَّبِيلِ tekil ve tanınan yolun önündeki alıkonmayı taşırken, sonraki çoğul yollar, bağlılığın eyleme dönüşmesinin yönlendirmeye cevap veren bir hareket olduğunu düşündürüyor.","reader_payoff":"Okur, odaktaki sapmayı korurken, algının tek başına yeterli olmadığı ve yürüyüşe dönüşen bağlılığın yolu yeniden açabildiği karşı hareketi de görür.","support_ids":["sup_43f9d1d609f0ab5d773b","sup_a42ebf8ea764ccd4776f"],"title":"Gayretle açılan yollar"}],"friction_notes":["HFT ankrajlarının Arapça yüzeyi ve ayet referansları eksiksizdir; buna karşılık wider branch kayıtlarının bir bölümü çözülmemiş olduğundan bu dallar bağımsız sözlük kesinliği gibi kullanılmadı.","HFT okuyucu kimliği legacy_unbound, bazı okuyucu yürüyüşleri citable false durumundadır; bu kayıtlar yalnızca sınırlı çıkarım ve containment malzemesi olarak taşındı, önceki etiketler karar sayılmadı.","Sosyal yayılım, krizle değişen dikkat ve gayretin yolu açması için ayet aşamaları mevcut olsa da tek nedensel bağlar yazar çıkarımıdır; her bulguda canlı alternatifler korunmuştur.","Webbed-path ve counted-ledger imgeleri paket tarafından yalnız dal yankısı olarak sınırlandırılmıştır; lexical gloss veya bağımsız bulgu yapılmadı."],"identity":{"authoring_request_sha256":"35df040354d22037a55497cf6b226573e74c056cb26ac96efcb43f43088cfabd","ayah_ref":"29:38","lane":"global","lane_packet_sha256":"7df1717bf2d163e3cc4b8d004256fb1fa2062925cb6240a9fdc04e6e3bb9c999"},"lane":"global","movements":[{"draft_prose":"{ar:مَّسَٰكِنِهِمْ, tr:mesâkinuhum, gloss:onların yurtları} sözü, geride kalmış birkaç ev görüntüsünü taşır; daha geniş akışta yeryüzünde dolaşma, bakma ve düşünme çağrılarıyla birlikte bu görüntü okunabilir bir saha kanıtına dönüşür. {ar:تَّبَيَّنَ, tr:tebeyyene, gloss:açığa çıkıp belirginleşti} onun içinden belirginleşir: iz, yalnızca görülüp geçilen bir harabe değildir. Kavrayış ilişki kurduğunda görünen sonuç davranışı sınırlayan bir uyarıya dönüşür. Sonraki benzetmede kalıntının bir ilişki içinde kavranması vurgulanır; böylece kanıtın yön göstermesi, gözün önünde bulunmasından onu doğru bağa yerleştirmeye geçer. Bu okuma, âyetin tarihsel bildirimini korurken yurtların okuyucuya açık bir inceleme alanı olarak iş görmesini görünür kılar.","finding_refs":["global:trace-to-guidance"],"movement_key":"global:trace-to-guidance"},{"draft_prose":"Âyetin önündeki sahnede yurtların bıraktığı iz ve iç kavrayış birlikte dururken, {ar:زَيَّنَ, tr:zeyyene, gloss:güzel gösterdi} fiili yapılan işlerin değerlendirmesini değiştirir. Daha geniş ayet çevresinde aynı süsleme ile yoldan çevirme art arda gelir; böylece {ar:صَدَّ, tr:sadde, gloss:yoldan alıkoydu} ve {ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:bilinen yol} birlikte düşünüldüğünde görünüşün yol ile gören kişi arasına girebildiği bir engel belirir. {ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:kavrayış sahibi olanlar} nitelemesi bu sahneyi keskinleştirir: kanıtın ve kavrayışın bulunması, yapılan işin nasıl değerlendirildiğini kendiliğinden düzeltmez. Bu okuma âyetin açık bildirimini, Şeytanın onların işlerini güzel gösterip onları bilinen yoldan alıkoymasını korur; sadece alıkoymanın körlükten önce değerlendirmeye yerleşebilen bir ara hareketini görünür kılar.","finding_refs":["global:adorned-evaluation-blocks"],"movement_key":"global:adorned-evaluation"},{"draft_prose":"Açılıştaki sınanma dili, {ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:kavrayış sahibi olanlar} nitelemesini bir unvan olmaktan çıkarıp davranışta ölçülen bir imkân gibi yeniden duyurur. İddia sınamadan geçer, doğruluk yapılan işte görünür, kötü iş bozuk hükümle yan yana gelir; bu akışta süslenen ameller, kavrayışın değerlendirmeden eyleme geçişinde ortaya çıkan arızayı görünür kılar. Okur böylece kavrayışın değerini yalnız bilgi biriktirmekte değil, hükmün harekete dönüşmesinde izleyebilir. Bu sınama, son kelimenin önceki eylem zincirine geri bağlandığı bir okuma açar; müstebsirîn'in ahlaki basiret, dünyevi beceri veya ikisinin kesişimi olması açık kalır. Ayetin sonundaki {ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:kavrayış sahibi olanlar} sözü, sonraki örneklerle birlikte okunduğunda yalnızca alaycı bir etiket olarak kapanmaz. İçlerinde açık ayetler bulunan ve bilgi verilen kişilerden söz edilirken inkârın da bilerek sürebildiği; güneş ve ayın düzenli yönelişi ile insanların doğru yönden çevrilmesinin yan yana getirildiği; doğru cevabın hemen ardından yönün tersine çevrilebildiği gösterilir. Böylece burada söz konusu olan kavrayış, dış kanıtın yokluğundan önce gelen bir imkân olarak kalır: insan görür, bilir, hatta doğru konuşur; karar, çıkarım ve iş aynı doğrultuya bağlanmayabilir. Bu, yoldan alıkonulmanın gerçek oluşunu korur; yalnızca engelin körlükten ibaret olmadığını açar.","finding_refs":["global:discernment-under-assay","global:knowledge-without-conversion"],"movement_key":"global:discernment-action"},{"draft_prose":"Yoldan alıkoyma yalnız kişinin içinde oluşan bir yön şaşması olarak kalmaz. Başka bir yerde bizden yana yolu izleme çağrısı, yükü başkasına devretme vaadiyle birleşir; hemen sonraki cevap bu vaadin yükleri çoğalttığını açığa çıkarır. Bu sıra, {ar:صَدَّ, tr:sadde, gloss:yoldan alıkoydu} fiilini somutlaştırır: yol silinmez, onun yerine güven verici sözlerle rakip bir güzergâh kurulabilir. Böylece süslenmiş iş yalnız güzel görünmez; izlenmesi kolay bir hikâye ve paylaşılmış bir sorumluluk duygusu da üretir. Başka bir genişleme, süslemenin tek tek kişilerin zihninde kapanmadığını gösterir. Üretilmiş yanlış, insanlar arasında bağ kuran bir değere, toplantıda sergilenen ortak bir kabule ve sonunda başkalarının yolunu kesen bir eyleme dönüşebilir. Odaktaki {ar:أَعْمَٰلَهُمْ, tr:a'mâlehum, gloss:yaptıkları işler} bu yüzden yalnızca yaptıkları işlerin listesini değil, paylaşılan ve tekrarlanan bir üretimi de düşündürür; {ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:bilinen yol} başkasının geçişini etkileyen ortak bir alan haline gelir. Zincirin aşamaları metin içinde ayrı ayrı görünür; bunların tek bir nedensel yayılım oluşturması yorum düzeyindedir, bağımsız sahnelerin okumaları da açık kalır.","finding_refs":["global:rival-route-burden","global:socialized-obstruction"],"movement_key":"global:rival-routes"},{"draft_prose":"Yolun önündeki süsleme sabit bir körlük resmi de kurmaz. Dünya hayatının oyalanma ve amaçsız meşguliyet olarak tasvir edildiği bölümde, tehlike anı rakip dayanakları birden ayıklar; kurtuluşla birlikte eski ortaklaştırmalar geri döner. Böylece {ar:زَيَّنَ, tr:zeyyene, gloss:güzel gösterdi} fiili, insanın bildiğini her durumda aynı kuvvetle uyguladığı bir hâli değil, hangi çekiciliğin eylemi yönettiğini değiştiren bir dikkat düzenini de açar. Bu hareket, odaktaki içgörüyü korur; onun etkisinin durumlara göre görünür olup geri çekilebileceğini gösterir. Bu baskıya karşı metin, yalnızca daha çok bilme düzeyinde kalmayan bir karşılık da sunar. Tekrarlanan bir ibadet pratiğinin çirkin eylemden alıkoyması, süslenmiş işlerin çekiciliğine davranış düzeyinde bir fren getirir. Böylece kavrayışın yönetime dönüşmesi bedende tekrarlanan bir yönelişle birlikte düşünülür; bu bağın doğrudan bir psikoloji yasası mı, yoksa normatif bir vaat mi olduğu açık kalırken, odaktaki işlerin fiilî niteliği korunur.","finding_refs":["global:state-dependent-salience","global:embodied-inhibition"],"movement_key":"global:changing-salience"},{"draft_prose":"Başka bir karşılaşmada görme, güven ve inanma aynı sahnede buluşur: güvenli alan ile çevresindeki insanların kapılıp götürülmesi birlikte görülür, ardından güven yanlış olana bağlanır. Bu, odaktaki {ar:مُسْتَبْصِرِينَ, tr:müstebsirîn, gloss:kavrayış sahibi olanlar} kelimesini gerçeği hiç seçememe şeklinde daraltmaz; seçilen ayrım ile bağlanılan nesnenin aynı olması gerekmediğini gösterir. İçgörü imkânı açık kalırken, aidiyet ve güven başka bir haritaya kayabilir. Son ayetteki karşı hareket, tek başına algıyı artırmaktan başka bir yol gösterir: gayret, yönlendirme ve çoğul yollar birlikte anılır. Odaktaki {ar:ٱلسَّبِيلِ, tr:es-sebîl, gloss:bilinen yol} tekil ve tanınan güzergâhın önünde gerçekleşen alıkonmayı taşırken, sonradan açılan yollar çabanın yönlendirmeye karşılık veren bir hareket olduğunu düşündürür. Böylece daha çok görmek yeterdi biçimindeki dar okuma genişler; odaktaki sapma korunur, fakat yürüyüşe dönüşen bağlılığın yolu yeniden açabildiği başka bir okuma da canlı kalır.","finding_refs":["global:security-belief-allocation","global:effort-opens-paths"],"movement_key":"global:trust-and-effort"}],"schema_version":"commentary-v4-scope-contribution-v1"}
</global_contribution_json>
