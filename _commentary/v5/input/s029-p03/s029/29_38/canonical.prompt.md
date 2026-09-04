# Commentary v5 consolidator

You are the fresh consolidator for **29:38**. Three independent scope
agents have written micro, macro, and global scope prose. Merge those inputs
into one coherent first-pass commentary.

This is a consolidation and writing task, not a new evidence-selection stage.
Do not add, reject, split, or silently merge away findings.

This V5 consolidator writes prose only. Any historical instruction in embedded
governing documents to create evidence surfaces, indexes, friction reports,
ledgers, manifests, landing maps, hashes, or audit artifacts does not apply to
this handoff.

## Coverage Contract

Treat every retained finding from the micro, macro, and global inputs as
mandatory. Before drafting, identify each finding's:

- carrier;
- independent trigger;
- contact between carrier and trigger;
- changed reading;
- concrete semantic detail;
- boundary.

Preserve every part explicitly in the reader-facing text. Do not replace a
concrete image, pathology, secondary branch, repeated action, spatial relation,
or before/after shift with a general theme.

Boundaries must stay attached to the interpretations they limit. Saying that a
word is not being translated literally in one way does not authorize deleting
the related contextual resonance.

A single scope paragraph may contain multiple retained findings or branches.
Treat each distinct claim, image, branch activation, or interpretive movement as
a separate mandatory landing, even when the scope agent expressed several of
them in one paragraph.

Each retained landing must be explicit in the prose, but explicit does not mean
one paragraph or one sentence per landing. Write composed v2-style commentary,
not a checklist. Compatible landings may share a paragraph when every landing's
carrier, trigger, contact, changed reading, concrete detail, and boundary remain
visible there. Avoid duplicate restatement, but do not compress a landing until
it becomes implicit.

Coverage is checked inside the prose itself. Every retained finding and every
distinct retained landing from the three scope inputs must become visible to a
reader in the consolidated commentary without requiring a separate ledger.

## Writing Contract

- Write fluent Turkish reader prose, not a lane report or technical ledger.
- Preserve the project display tag syntax when naming an Arabic word doing
  interpretive work: `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`.
  Do not drop the tag, convert it to plain Arabic only, or invent another tag
  shape. Use tags sparingly at real anchor points; do not tag every repeated
  mention of the same word.
- Explain activation in ordinary language: which Arabic surface, root meaning,
  or ordinary meaning is carried by the focus; what independent word, image, or
  context triggers it; why they make contact; how the focus reading changes;
  and where the inference stops.
- Do not expose internal root IDs, branch IDs, support IDs, QAC coordinates, or
  lane machinery in reader prose.
- Scope prose is source material, not immutable wording. Rewrite, group, and
  reorder for cadence and coherence while preserving semantic coverage. Do not
  turn micro findings into a sequential word-by-word catalogue unless the ayah's
  own movement requires it.
- Translate English source language naturally. Arabic and transliteration may
  remain in the established notation.
- Automatic basmala and explicitly added ayat are ordinary non-focus context
  members. Contextual resonance must not be presented as lexical meaning.
- Keep counter-readings visible without verdict or rank. Do not turn lane order
  into evidentiary rank.

## Output

Write exactly one nonempty file and modify nothing else:

- prose: `_commentary/v5/raw/s029-p03/s029/29_38/29_38.prose.tr.md`

Before finishing, check that every input finding and every distinct retained
landing appears once as an explicit prose landing. If any retained landing is
missing, revise before you consider the unit complete.

After writing the prose file, remain in this conversation for the editorial
follow-up.

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

Status: active draft, updated 2026-09-02. Layer 2 V5 and Layer 3 v3 workflow
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
network/V11 evidence. It reads the complete Layer-2 findings index and preserved
boundaries. Legacy Layer-2 runs may also contain local `surprise:<id>` resonance
rows, but simplified V5 commentary does not require those rows, a landing map,
or provenance-ledger apparatus. Layer 3 writes a separate surah reading and does
not rewrite or overlay the ayah prose.

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
- **legacy evidence surface** — separate, addressable per phrase, holding refs,
  branch IDs, counter-evidence, coverage, and an explicit mark on every claim
  that is inference rather than bundle-traceable. Simplified V5 consolidation and
  editorial handoffs do not write this artifact;
- **legacy findings index** — *ayah level only.* A flat list of every reading the
  prose carries, one line per reading, each under its bundle ref, with
  `[inference]` marking the writer's own readings. Legacy Layer-2 runs may add
  `surprise:<id>` synthesis rows for local resonances, but simplified V5 does not
  require surprise rows, a machine-readable landing map, or provenance-ledger/hash
  apparatus. V5 traceability is prose-level: each retained finding and each
  distinct retained landing must remain explicit in reader prose;
- **legacy friction** — ambiguity, contradiction, missing evidence, or production
  limitations. Simplified V5 consolidation and editorial handoffs do not write a
  friction file.

The prose must be readable end to end on its own. Legacy evidence surfaces, when
present, are supporting apparatus rather than required reader context.
Mandatory coverage does not license checklist prose. Findings may be woven,
grouped, and reordered into composed commentary when every retained landing
remains recoverable and its boundary remains attached.

Ayah prose makes its surprise turn explicit in reader language. It first gives a
recoverable primary floor, then enters through a local word, states the
secondary resonance, and makes clear what that resonance newly supports or
shifts. This is part of the continuous prose, not a section headed "surprise" and
not an apparatus label. When no secondary material survives grounding and
containment, the writer leaves it out rather than inventing a turn. Legacy
workflows may record the omission in evidence or friction; simplified V5 does
not require that apparatus.

Arabic lexical items in authored prose should use structured surface spans so one
text can render for both reading and listening editions:

```text
{ar:ٱلْقَلَمِ, tr:el-kalem, gloss:kalem}
```

Use the span at first mention of an ayah word, and again when the prose returns
to that word after moving to another word or another paragraph. A renderer may
collapse repeated fields later; the authored source should preserve `ar`, `tr`,
and `gloss` whenever the word is doing fresh interpretive work. Active V5
consolidation and editorial passes must preserve this exact tag shape at Arabic
anchor points. They may reduce repeated tags after the anchor is established,
but they must not drop the anchor tag, convert it to plain Arabic only, or
invent another tag format.

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
auditable source. Active V5 derives its focus docket and lane packets from that
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

An activated branch must become an explicit reader-facing semantic movement,
not merely an apparatus reference. In fluent prose, state which word or image
carries the relevant root meaning, which independent word, relation, or context
detail activates its exact branch facet, why the contact changes the reading,
and where the inference stops. Root IDs, branch IDs, and analysis coordinates
remain outside reader prose. Active V5 scope and consolidation instructions
preserve the exact carrier, trigger, contact, changed reading, concrete
semantic detail, and boundary for every retained finding. Canonical and
editorial wording may change, but those meanings must remain explicit.

### 6.1 Unit identity and prefatory basmala

Every current bundle declares `unit_kind`, `surface_ref`, and
`linguistic_source_ref`. For a `numbered_ayah`, all identities resolve to the
numbered ayah itself. For `prefatory_basmala`, the surface is the target surah's
`S:0` Quran-text row and the linguistic source is canonical `1:1`. The builder
must prove normalized surface equivalence before aliasing. QAC, word-analysis,
and morpheme-span references remain `1:1:*`; it is forbidden to manufacture
`S:0:*` linguistic identities. When `S:0` is the focus, those `1:1` coordinates
remain its focus surface and may not be classified or routed as external
context.

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
included zero; V5 adds `S:0` once to the macro packet at ordinary non-focus
context depth.

### 6.2 Explicit ordered context

Canonical unit bundles remain context-independent. V5 may prepare an analysis
composition containing one or more ordered, discontinuous, and cross-surah
segments, with one or more declared focus units. Each focus is authored one at
a time; every other selected unit becomes context. This supports, without
changing the canonical source bundles:

- a basmala focus with a selected surah as context;
- each numbered ayah as focus with its surah's basmala automatically present;
- each ayah of one surah as focus under an ordered Fatiha or other recitation
  lens;
- arbitrary explicit additions such as one external ayah outside a pericope.

For every numbered focus in S2-S8 and S10-S114, V5 automatically and mandatorily
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

Before lane prompts are written, V5 extracts candidate and support Quran refs
from structured fields, serialized JSON, Quran coordinates, and same-surah
ranges. Evidence is routed to the widest lane those exact refs require. This
inference cannot move automatic host-basmala or explicit external-member
evidence out of macro: their membership is defined by the host analysis, while
their linguistic and source identities remain intact.

The complete selected bundle remains the hash-bound provenance source but is
not embedded as model-visible context. Context projection must exclude the
unit's standalone-focus word commentary, full QAC rows, morpheme spans,
coverage report, full root dictionaries/glosses, prior HFT run, reader walks,
cross-run publication, inter-ayah rows, whole-surah reading, and channel
material. Those fields remain available only when that unit itself is the
focus. This boundary prevents automatic basmala and `--add-ayat` members from
becoming larger or semantically privileged relative to ordinary context ayat.

One narrow enrichment affects an evidence descriptor, not the context-depth
boundary. If a supplied candidate cites an unresolved branch and its
branch-specific trace names exact context refs whose canonical bundles contain
that branch, V5 may hydrate only that branch's semantic detail, review facets,
and all matching root occurrences from those refs. Those branch refs participate
in lane routing before hydration, and source-to-carrier bindings remain separate
per candidate when several candidates use the same branch. Divergent source
semantics fail closed. It must not import neighboring branches or standalone-focus
payloads. Every auxiliary source path, byte count, raw SHA-256, canonical
SHA-256, unit identity, source pointer, and projected branch field is persisted
and revalidated.

An analysis ID namespaces `input/`, `raw/`, and `editorial/` paths so native and
custom readings of the same focus cannot collide. The composition JSON, every
selected bundle hash, deterministic context-projection hash, projected lane
packets, and output identities are snapshotted in the unit manifest. Multiple
focus units may be prepared and orchestrated in parallel. V5 preserves the
established V2/V3 interpretive and prose standard while separating each of the
micro, macro, and global lanes into a discovery turn and a planned composition
follow-up to the same agent. Historical stage, role, and file-writing
instructions in embedded governing texts do not override V5. Discovery must
account for every candidate, supplied branch facet, connection, and named
semantic obligation; accepted and narrowed candidates own dedicated findings,
while only exact semantic duplicates may share one. The second turn renders the
fixed finding set into Turkish scope prose. The V5 consolidator then receives
the three scope prose files and writes only a consolidated prose file; the same
live consolidator writes only the editorial prose file. No V5 consolidation or
editorial handoff creates evidence files, indexes, friction files, ledgers,
landing maps, manifests, hashes, or audit artifacts. There is no automated
repair, reconciliation, or semantic-adjudication cycle.

Layer 3 builds a separate hermetic source packet from Quran text, the typed
primary floor, the completed four-file Layer-2 v2 artifact set for every
numbered ayah, and whatever network-v3/V11 sources are available. Missing
optional source families are warnings, not build failures. Missing Quran text,
typed primary floor, or complete Layer-2 artifacts aborts. See
[`_channel/layer3/ORCHESTRATION.md`](_channel/layer3/ORCHESTRATION.md).

</commentary_spec>

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
- composition into a prose envelope whose evidence map mechanically maps every
  admitted channel and hinge to reader-visible language.

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

<focus_context_brief>
{
  "focus_ref": "29:38",
  "analysis_id": "s029-p03",
  "context_refs": [
    "29:28",
    "29:29",
    "29:30",
    "29:31",
    "29:32",
    "29:33",
    "29:34",
    "29:35",
    "29:36",
    "29:37",
    "29:39",
    "29:40",
    "29:41",
    "29:42",
    "29:43",
    "29:44"
  ],
  "automatic_host_basmala_ref": "29:0",
  "external_ayat_refs": []
}
</focus_context_brief>

<micro_scope_prose>
{
  "schema_version": "commentary-v5-scope-composition-v1",
  "ayah_ref": "29:38",
  "lane": "micro",
  "findings": [
    {
      "finding_ref": "micro:dwelling-stillness",
      "prose": "مَّسَٰكِنِهِمْ, yerleşip yaşanan yer anlamını taşırken, yıkımdan sonra hareketsiz kalmış yurt görüntüsüyle temas eder. Çoğul yer adı biçimi bu anlamı yalnız geçmişte yaşanmış bir mekân olmaktan çıkarıp görünür bir tanıklık yüzüne dönüştürür; sahipleri yokken kalan yer, olanı kendisi gösterir. Böylece okur yurtları sahne dekoru değil, okunabilen tanık olarak görür. Temel anlam yerleşilen yerdir; durma ve tanıklık bu yerel temasın basıncıdır, iç dinginlik veya başka anlam alanları ileri sürülmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:dwelling-stillness:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مَّسَٰكِنِهِمْ, yerleşip yaşanan yer anlamını taşırken, yıkımdan sonra hareketsiz kalmış yurt görüntüsüyle temas eder. Çoğul yer adı biçimi bu anlamı yalnız geçmişte yaşanmış bir mekân olmaktan çıkarıp görünür bir tanıklık yüzüne dönüştürür; sahipleri yokken kalan yer, olanı kendisi gösterir. Böylece okur yurtları sahne dekoru değil, okunabilen tanık olarak görür. Temel anlam yerleşilen yerdir; durma ve tanıklık bu yerel temasın basıncıdır, iç dinginlik veya başka anlam alanları ileri sürülmez."
        }
      ]
    },
    {
      "finding_ref": "micro:source-governed-dwellings",
      "prose": "مَّسَٰكِنِهِمْ temel çözümlemede mecrûr bir kaynak olarak okunur ve bunu açıkça مِنْ kaynak edatı tetikler: açıklık yurtlardan gelir. Yalın özne hâliyle duyulan varyant ise aynı yurtların açıklığı taşıyan etkin bir yüzey gibi algılanmasını güçlendirir. Okur böylece temel kaynak ilişkisini korurken varyantın kanıtlayıcı etkiyi neden artırdığını fark eder. Varyant ana çözümlemenin yerine geçirilmez; yurtlardan bağımsız bir fail kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:source-governed-dwellings:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مَّسَٰكِنِهِمْ temel çözümlemede mecrûr bir kaynak olarak okunur ve bunu açıkça مِنْ kaynak edatı tetikler: açıklık yurtlardan gelir. Yalın özne hâliyle duyulan varyant ise aynı yurtların açıklığı taşıyan etkin bir yüzey gibi algılanmasını güçlendirir. Okur böylece temel kaynak ilişkisini korurken varyantın kanıtlayıcı etkiyi neden artırdığını fark eder. Varyant ana çözümlemenin yerine geçirilmez; yurtlardan bağımsız bir fail kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:surviving-ruin-witness",
      "prose": "مَّسَٰكِنِهِمْ yalnız bir zamanlar yaşanan yerlerin adını taşımaz; yıkımdan sonra geride kalan okunabilir tanıklık da bu yurt anlamını etkinleştirir. Yurt sözcüğü kalıntı olarak görünen mekân imgesiyle buluşunca yer, tarihsel olayın arkasında kalan bir açıklama yüzüne dönüşür. Okur, geçmişten geriye kalan yerin kendisinin ne olduğunu anlattığını görür. Bu tanıklık odaktaki yurt ifadesiyle sınırlıdır; buradan genel bir yıkım düzeni çıkarılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:surviving-ruin-witness:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مَّسَٰكِنِهِمْ yalnız bir zamanlar yaşanan yerlerin adını taşımaz; yıkımdan sonra geride kalan okunabilir tanıklık da bu yurt anlamını etkinleştirir. Yurt sözcüğü kalıntı olarak görünen mekân imgesiyle buluşunca yer, tarihsel olayın arkasında kalan bir açıklama yüzüne dönüşür. Okur, geçmişten geriye kalan yerin kendisinin ne olduğunu anlattığını görür. Bu tanıklık odaktaki yurt ifadesiyle sınırlıdır; buradan genel bir yıkım düzeni çıkarılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:resumptive-conjunction",
      "prose": "Kanıt cümleciğinden sonra gelen وَ, bağlama ve yeniden başlatma anlamını taşır; bağımsız tetikleyici, yurtlardan gelen görünür delil ile hemen ardından yürüyen eylem dizisinin yan yana gelişidir. Bağlaç bu kısa kanıt aralığını kapatıp sonraki fiili önceki yıkım akışına geri bağlar. Böylece okur yurtların tanıklığı ile saptırmayı iki kopuk bilgi değil, aynı hareketin ardışık vuruşları olarak duyar. İşlev yerel yeniden bağlanmayla sınırlıdır; daha geniş bir anlatı tezi yüklenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:resumptive-conjunction:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "Kanıt cümleciğinden sonra gelen وَ, bağlama ve yeniden başlatma anlamını taşır; bağımsız tetikleyici, yurtlardan gelen görünür delil ile hemen ardından yürüyen eylem dizisinin yan yana gelişidir. Bağlaç bu kısa kanıt aralığını kapatıp sonraki fiili önceki yıkım akışına geri bağlar. Böylece okur yurtların tanıklığı ile saptırmayı iki kopuk bilgi değil, aynı hareketin ardışık vuruşları olarak duyar. İşlev yerel yeniden bağlanmayla sınırlıdır; daha geniş bir anlatı tezi yüklenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:active-valency",
      "prose": "زَيَّنَ etken ikinci kalıp olarak güzelleştiren faili, لَهُمُ ile gösterilen alıcı topluluğu ve أَعْمَالَهُمْ ile gösterilen doğrudan nesneyi ayrı ayrı görünür kılar. Fiilin etkenliği, alıcı edatı ve nesne ilişkisi birlikte çalışarak fail, muhatap ve işlenmiş yüzey arasındaki temasın bağımsız dayanaklarını verir. Okur saptırmayı belirsiz bir kötülük değil, belirli kişilere ve belirli eylemlere yönelen bir işlem olarak görür. Bulgu yerel etkenlik ve tümleç rolleriyle sınırlıdır; bundan daha geniş bir fail veya sonuç çıkarılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:active-valency:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "زَيَّنَ etken ikinci kalıp olarak güzelleştiren faili, لَهُمُ ile gösterilen alıcı topluluğu ve أَعْمَالَهُمْ ile gösterilen doğrudan nesneyi ayrı ayrı görünür kılar. Fiilin etkenliği, alıcı edatı ve nesne ilişkisi birlikte çalışarak fail, muhatap ve işlenmiş yüzey arasındaki temasın bağımsız dayanaklarını verir. Okur saptırmayı belirsiz bir kötülük değil, belirli kişilere ve belirli eylemlere yönelen bir işlem olarak görür. Bulgu yerel etkenlik ve tümleç rolleriyle sınırlıdır; bundan daha geniş bir fail veya sonuç çıkarılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:worked-over-surface",
      "prose": "زَيَّنَ içindeki güzelleştirme anlamı, yalnız bir şeyi güzel bulmayı değil, onu işleyerek çekici bir yüzey hâline getirmeyi taşır. Bu anlamı fiilin etkin ikinci kalıbı taşır; bağımsız tetikleyici, güzelleştirmenin nesnesi olan أَعْمَالَهُمْ ve ardından gelen yol engellemesidir. Temas, düşüşün kaba kuvvetten önce eylemlerin görünüşüne verilen yönlendirmeyle başladığını gösterir. Güzelleştirme burada yerel eylem nesnesiyle sınırlıdır; her güzellik veya süs aynı işlem sayılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:worked-over-surface:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "زَيَّنَ içindeki güzelleştirme anlamı, yalnız bir şeyi güzel bulmayı değil, onu işleyerek çekici bir yüzey hâline getirmeyi taşır. Bu anlamı fiilin etkin ikinci kalıbı taşır; bağımsız tetikleyici, güzelleştirmenin nesnesi olan أَعْمَالَهُمْ ve ardından gelen yol engellemesidir. Temas, düşüşün kaba kuvvetten önce eylemlerin görünüşüne verilen yönlendirmeyle başladığını gösterir. Güzelleştirme burada yerel eylem nesnesiyle sınırlıdır; her güzellik veya süs aynı işlem sayılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:beautification-obstruction-formula",
      "prose": "زَيَّنَ ile فَصَدَّ arasındaki sonuç sırası, güzelleştirme anlamını yolun önünü kesen tekrarlanabilir bir aldatma düzenine taşır. İlk fiilin çekici gösterme işlemi, sonuç bağlacı ve alıkoyma fiiliyle temas edince yön kaybının hazırlayıcı adımı olarak duyulur; yakın tekrar izleri bu okumayı destekler. Okur başarısızlığı çekici sunumdan yön kaybına geçen bir işlem olarak izler. Bu destek ayetteki yerel mekanizmayla sınırlıdır; sure geneline yayılan tek bir açıklama kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:beautification-obstruction-formula:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "زَيَّنَ ile فَصَدَّ arasındaki sonuç sırası, güzelleştirme anlamını yolun önünü kesen tekrarlanabilir bir aldatma düzenine taşır. İlk fiilin çekici gösterme işlemi, sonuç bağlacı ve alıkoyma fiiliyle temas edince yön kaybının hazırlayıcı adımı olarak duyulur; yakın tekrar izleri bu okumayı destekler. Okur başarısızlığı çekici sunumdan yön kaybına geçen bir işlem olarak izler. Bu destek ayetteki yerel mekanizmayla sınırlıdır; sure geneline yayılan tek bir açıklama kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:harmful-affectedness",
      "prose": "لَهُمُ, güzelleştirmenin alıcılarını gösteren “onlar için” yönünü taşır; bunu bağımsız olarak tetikleyen doğrudan nesne أَعْمَالَهُمْ ve sonrasındaki فَصَدَّ ilişkisidir. Alıcı konumu, eylemlerin onlara yöneltildiğini gösterirken, aynı eylemlerin sonunda onların aleyhine işlemesiyle gerilim kazanır. Okur, “onlar için” gibi duyulan ilişkinin neden koruyucu değil, etkileyici ve zararlı bir yön taşıyabildiğini fark eder. Yorum lāmın yerel alıcı ve etkilenme işleviyle sınırlıdır; edat tek başına iyilik hükmü kurmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:harmful-affectedness:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "لَهُمُ, güzelleştirmenin alıcılarını gösteren “onlar için” yönünü taşır; bunu bağımsız olarak tetikleyen doğrudan nesne أَعْمَالَهُمْ ve sonrasındaki فَصَدَّ ilişkisidir. Alıcı konumu, eylemlerin onlara yöneltildiğini gösterirken, aynı eylemlerin sonunda onların aleyhine işlemesiyle gerilim kazanır. Okur, “onlar için” gibi duyulan ilişkinin neden koruyucu değil, etkileyici ve zararlı bir yön taşıyabildiğini fark eder. Yorum lāmın yerel alıcı ve etkilenme işleviyle sınırlıdır; edat tek başına iyilik hükmü kurmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:plural-pronoun-thread",
      "prose": "هُمُ ile taşınan çoğul gönderim, başlangıçta anılan topluluğu yurtların sahibi, güzelleştirmenin alıcısı, eylemlerin sahibi ve yoldan çevrilen taraf olarak korur. Bağımsız tetikleyici, bu ekin مَّسَٰكِنِهِمْ, أَعْمَالَهُمْ ve صَدَّهُمْ içindeki tekrarlarıdır; aynı biçim farklı roller arasında gönderimi dağıtmaz. Böylece okur farklı görevlerde görünen kişilerin ayrı örnekler değil aynı topluluk olduğunu hisseder. Bu yalnız yerel gönderim sürekliliğidir; grup içi yapı veya sure geneli kimliği ileri sürülmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:plural-pronoun-thread:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "هُمُ ile taşınan çoğul gönderim, başlangıçta anılan topluluğu yurtların sahibi, güzelleştirmenin alıcısı, eylemlerin sahibi ve yoldan çevrilen taraf olarak korur. Bağımsız tetikleyici, bu ekin مَّسَٰكِنِهِمْ, أَعْمَالَهُمْ ve صَدَّهُمْ içindeki tekrarlarıdır; aynı biçim farklı roller arasında gönderimi dağıtmaz. Böylece okur farklı görevlerde görünen kişilerin ayrı örnekler değil aynı topluluk olduğunu hisseder. Bu yalnız yerel gönderim sürekliliğidir; grup içi yapı veya sure geneli kimliği ileri sürülmez."
        }
      ]
    },
    {
      "finding_ref": "micro:adversarial-formula-agent",
      "prose": "ٱلشَّيْطَانُ, adı konmuş karşıt varlık anlamını taşır; onu etkinleştiren bağımsız temas زَيَّنَ ile güzelleştirilen eylemler ve hemen sonraki فَصَدَّ sonucudur. Belirli fail, eylemlerin görünüşünü değiştirip yolu kapatan düzenin içine yerleşince aldatma anonim bir atmosfer olmaktan çıkar, işlem yapan bir faille ilişkilendirilir. Okur bu yüzden Şeytanı değerlendirmeyi yöneten ve yön kaybına bağlayan fail olarak görür. Yakın tekrarlar yalnız bu yerel fail-işlem bağını destekler; sure geneline yayılan bir kanal ilan edilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:adversarial-formula-agent:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلشَّيْطَانُ, adı konmuş karşıt varlık anlamını taşır; onu etkinleştiren bağımsız temas زَيَّنَ ile güzelleştirilen eylemler ve hemen sonraki فَصَدَّ sonucudur. Belirli fail, eylemlerin görünüşünü değiştirip yolu kapatan düzenin içine yerleşince aldatma anonim bir atmosfer olmaktan çıkar, işlem yapan bir faille ilişkilendirilir. Okur bu yüzden Şeytanı değerlendirmeyi yöneten ve yön kaybına bağlayan fail olarak görür. Yakın tekrarlar yalnız bu yerel fail-işlem bağını destekler; sure geneline yayılan bir kanal ilan edilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:known-adversarial-agent",
      "prose": "ٱلشَّيْطَانُ belirli ve özne hâlindeki biçimiyle güzelleştirme işinin bilinen karşıt failini taşır. Bu anlamı bağımsız olarak tetikleyen etken fiil زَيَّنَ ve onun açıkça kurduğu fail-işlem ilişkidir; belirlilik ile özne hâli, mekanizmanın isimsiz bir kuvvet tarafından işletilmediğini gösterir. Okur ayetin sorumluluğu belirsiz bir etkiye dağıtmadığını fark eder. Bulgu yerel özne belirliğiyle sınırlıdır; alternatif türetimler ana yapıya eklenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:known-adversarial-agent:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلشَّيْطَانُ belirli ve özne hâlindeki biçimiyle güzelleştirme işinin bilinen karşıt failini taşır. Bu anlamı bağımsız olarak tetikleyen etken fiil زَيَّنَ ve onun açıkça kurduğu fail-işlem ilişkidir; belirlilik ile özne hâli, mekanizmanın isimsiz bir kuvvet tarafından işletilmediğini gösterir. Okur ayetin sorumluluğu belirsiz bir etkiye dağıtmadığını fark eder. Bulgu yerel özne belirliğiyle sınırlıdır; alternatif türetimler ana yapıya eklenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:remoteness-distance-pressure",
      "prose": "ٱلشَّيْطَانُ adında bulunan uzaklık ve yabancılaşma basıncı, yoldan uzaklaştırma anlamıyla sınırlı bir temas kurar. Bağımsız tetikleyici صَدَّ ... عَنِ ٱلسَّبِيلِ yapısındaki ayrılma yönüdür; adın çağrışımı bu yönle birleşince uzaklaştırma hareketine hafif bir renk verir. Okur Şeytan adının ayetteki uzaklaşma yönüyle neden uyum kazandığını anlar. Ancak taşıyıcı yerel olarak bilinen varlık adıdır; ateş türetimi etkinleştirilmez ve uzaklık ayrı bir fiile dönüştürülmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:remoteness-distance-pressure:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلشَّيْطَانُ adında bulunan uzaklık ve yabancılaşma basıncı, yoldan uzaklaştırma anlamıyla sınırlı bir temas kurar. Bağımsız tetikleyici صَدَّ ... عَنِ ٱلسَّبِيلِ yapısındaki ayrılma yönüdür; adın çağrışımı bu yönle birleşince uzaklaştırma hareketine hafif bir renk verir. Okur Şeytan adının ayetteki uzaklaşma yönüyle neden uyum kazandığını anlar. Ancak taşıyıcı yerel olarak bilinen varlık adıdır; ateş türetimi etkinleştirilmez ve uzaklık ayrı bir fiile dönüştürülmez."
        }
      ]
    },
    {
      "finding_ref": "micro:neutral-action-field",
      "prose": "أَعْمَالَهُمْ, iş ve bilerek yapılan eylem anlamını nötr biçimde korur; bu anlamı dönüştüren bağımsız temas زَيَّنَ ile ardından gelen صَدَّ fiilidir. Tehlike eylem adının kendisinden değil, eylemlerin nasıl gösterildiği ve nereye yöneltildiğinden doğar. Okur ayetin bütün işleri baştan kötü ilan etmediğini, değerlendirme düzeninin eylem alanını tehlikeli hâle getirdiğini görür. Eylem sözcüğüne bu yerel ilişki dışında her iş için hüküm yüklenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:neutral-action-field:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "أَعْمَالَهُمْ, iş ve bilerek yapılan eylem anlamını nötr biçimde korur; bu anlamı dönüştüren bağımsız temas زَيَّنَ ile ardından gelen صَدَّ fiilidir. Tehlike eylem adının kendisinden değil, eylemlerin nasıl gösterildiği ve nereye yöneltildiğinden doğar. Okur ayetin bütün işleri baştan kötü ilan etmediğini, değerlendirme düzeninin eylem alanını tehlikeli hâle getirdiğini görür. Eylem sözcüğüne bu yerel ilişki dışında her iş için hüküm yüklenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:owned-practice-field",
      "prose": "أَعْمَالَهُمْ çoğul ve iyelikli nesne olarak tek bir davranışı değil, topluluğun sahiplenilmiş eylemler ve uygulamalar alanını taşır. Bağımsız tetikleyici زَيَّنَ fiilidir; çoğul yapı ve üçüncü çoğul iyelik eki, güzelleştirmenin tek bir seçime değil toplanmış bir pratik bütüne yöneldiğini gösterir. Okur saptırmanın bir anlık hatadan önce bütün eylem alanının çekici gösterilmesiyle kurulduğunu görür. Kapsam yerel eylem alanıyla sınırlıdır; topluluğun bütün hayatı hakkında otomatik hüküm verilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:owned-practice-field:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "أَعْمَالَهُمْ çoğul ve iyelikli nesne olarak tek bir davranışı değil, topluluğun sahiplenilmiş eylemler ve uygulamalar alanını taşır. Bağımsız tetikleyici زَيَّنَ fiilidir; çoğul yapı ve üçüncü çoğul iyelik eki, güzelleştirmenin tek bir seçime değil toplanmış bir pratik bütüne yöneldiğini gösterir. Okur saptırmanın bir anlık hatadan önce bütün eylem alanının çekici gösterilmesiyle kurulduğunu görür. Kapsam yerel eylem alanıyla sınırlıdır; topluluğun bütün hayatı hakkında otomatik hüküm verilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:beautified-deeds-pivot",
      "prose": "أَعْمَالَهُمْ önce زَيَّنَ fiilinin doğrudan nesnesi olarak güzelleştirilen yüzeyi taşır, sonra فَ ile başlayan sonuçta yol saptırmasının dönüm noktasına dönüşür. Bağımsız tetikleyici bu sonuç bağlacıdır; eylem nesnesini görünüşten yön kaybına geçen bağlantı hâline getirir. Okur yolun kesilmesini ayrı bir olay değil, eylemlerin çekici gösterilmesinden doğan dönüş olarak izler. Bu dönüm noktası yerel cümle sırasına aittir; eylemlerin değişmez biçimde kötü olduğu söylenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:beautified-deeds-pivot:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "أَعْمَالَهُمْ önce زَيَّنَ fiilinin doğrudan nesnesi olarak güzelleştirilen yüzeyi taşır, sonra فَ ile başlayan sonuçta yol saptırmasının dönüm noktasına dönüşür. Bağımsız tetikleyici bu sonuç bağlacıdır; eylem nesnesini görünüşten yön kaybına geçen bağlantı hâline getirir. Okur yolun kesilmesini ayrı bir olay değil, eylemlerin çekici gösterilmesinden doğan dönüş olarak izler. Bu dönüm noktası yerel cümle sırasına aittir; eylemlerin değişmez biçimde kötü olduğu söylenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:beautification-consequence",
      "prose": "فَ, ardışık sonuç ve yakınlık anlamını taşır; önündeki زَيَّنَ ile sonrasındaki صَدَّ bu anlamı doğrudan tetikler. Güzelleştirme ile alıkoyma arasındaki bağ, gevşek bir olay sırası değil hemen doğan bir sonuç ilişkisi olarak duyulur. Okur “güzel gösterdi ve alıkoydu” ifadesindeki sıkı geçişi fark eder. Bağlaç yalnız yerel sonuç ve zaman yakınlığını gösterir; nedenselliğin bütün ayrıntıları buradan türetilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:beautification-consequence:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "فَ, ardışık sonuç ve yakınlık anlamını taşır; önündeki زَيَّنَ ile sonrasındaki صَدَّ bu anlamı doğrudan tetikler. Güzelleştirme ile alıkoyma arasındaki bağ, gevşek bir olay sırası değil hemen doğan bir sonuç ilişkisi olarak duyulur. Okur “güzel gösterdi ve alıkoydu” ifadesindeki sıkı geçişi fark eder. Bağlaç yalnız yerel sonuç ve zaman yakınlığını gösterir; nedenselliğin bütün ayrıntıları buradan türetilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:acted-upon-peoples",
      "prose": "صَدَّهُمْ, geçişli alıkoyma anlamını ve ekindeki topluluğu doğrudan nesne yapan yapıyı taşır. Bağımsız tetikleyici, son niteliği kuran مُسْتَبْصِرِينَ ile aynı topluluğun anlayabilecek durumda olduğunun bildirilmesidir; zamir bu topluluğu gerçekleşmiş saptırmanın hedefi olarak fiilin içine alır. Okur kavrayış imkânı bulunan kişilerin fiilen alıkonduğunu görür. Nesne oluşu topluluğun her türlü edilgenliğini değil, yalnız bu eylemdeki rolünü gösterir.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:acted-upon-peoples:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "صَدَّهُمْ, geçişli alıkoyma anlamını ve ekindeki topluluğu doğrudan nesne yapan yapıyı taşır. Bağımsız tetikleyici, son niteliği kuran مُسْتَبْصِرِينَ ile aynı topluluğun anlayabilecek durumda olduğunun bildirilmesidir; zamir bu topluluğu gerçekleşmiş saptırmanın hedefi olarak fiilin içine alır. Okur kavrayış imkânı bulunan kişilerin fiilen alıkonduğunu görür. Nesne oluşu topluluğun her türlü edilgenliğini değil, yalnız bu eylemdeki rolünü gösterir."
        }
      ]
    },
    {
      "finding_ref": "micro:obstruction-formula",
      "prose": "فَ sonucu, صَدَّ fiili ve ٱلسَّبِيلِ yol adı birlikte çalışınca güzelleştirme genel bir başarısızlıkta kalmaz, yol hedefli belirli bir alıkoyma düzenine dönüşür. Bağımsız tetikleyici, sonuç bağlacının engelleme fiilini tanınan yol ile birleştirmesidir; bu temas saptırmayı soyut bir yön kaybından erişimi kesilen bir güzergâha çevirir. Okur son hareketi belirli bir yolun engellenmesi olarak görür. Formül niteliği yerel birleşim ve yakın karşılaştırmayla sınırlıdır; her benzer yapı için tek açıklama ilan edilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:obstruction-formula:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "فَ sonucu, صَدَّ fiili ve ٱلسَّبِيلِ yol adı birlikte çalışınca güzelleştirme genel bir başarısızlıkta kalmaz, yol hedefli belirli bir alıkoyma düzenine dönüşür. Bağımsız tetikleyici, sonuç bağlacının engelleme fiilini tanınan yol ile birleştirmesidir; bu temas saptırmayı soyut bir yön kaybından erişimi kesilen bir güzergâha çevirir. Okur son hareketi belirli bir yolun engellenmesi olarak görür. Formül niteliği yerel birleşim ve yakın karşılaştırmayla sınırlıdır; her benzer yapı için tek açıklama ilan edilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:path-access-blocked",
      "prose": "صَدَّهُمْ عَنِ ٱلسَّبِيلِ, yolu ortadan kaldırmadan insanları ondan uzaklaştıran tamamlanmış bir engellemeyi taşır. Fiilin insanları nesne yapması ve عَنِ ile yönetilen belirli yol, bağımsız tetikleyici olarak değişenin yolun varlığı değil erişim ve yöneliş olduğunu gösterir. Okur felaketin yolun yok olması değil, yol dururken topluluğun ondan çevrilmesi olduğunu fark eder. Yolun korunması bu yerel söz diziminin sonucudur; evrensel erişim veya son hüküm iddiası kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:path-access-blocked:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "صَدَّهُمْ عَنِ ٱلسَّبِيلِ, yolu ortadan kaldırmadan insanları ondan uzaklaştıran tamamlanmış bir engellemeyi taşır. Fiilin insanları nesne yapması ve عَنِ ile yönetilen belirli yol, bağımsız tetikleyici olarak değişenin yolun varlığı değil erişim ve yöneliş olduğunu gösterir. Okur felaketin yolun yok olması değil, yol dururken topluluğun ondan çevrilmesi olduğunu fark eder. Yolun korunması bu yerel söz diziminin sonucudur; evrensel erişim veya son hüküm iddiası kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:away-from-target",
      "prose": "عَنِ, alıkoymanın uzaklaştırma yönünü taşır; bunu tamamlayan bağımsız temas صَدَّ fiili ile onun hedefi olan ٱلسَّبِيلِ'dir. Ayrılma edatı fiilin açık bıraktığı yön yuvasını belirli bir yolla doldurunca alıkoyma yalnız bir engel değil, belirli rotadan koparılma hareketi olur. Okur yön ilişkisinin “yoldan” ifadesinde nasıl tamamlandığını görür. Bu anlam yerel yol tümleciyle sınırlıdır; edatın bütün mekânsal ayrılık kullanımları etkinleştirilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:away-from-target:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "عَنِ, alıkoymanın uzaklaştırma yönünü taşır; bunu tamamlayan bağımsız temas صَدَّ fiili ile onun hedefi olan ٱلسَّبِيلِ'dir. Ayrılma edatı fiilin açık bıraktığı yön yuvasını belirli bir yolla doldurunca alıkoyma yalnız bir engel değil, belirli rotadan koparılma hareketi olur. Okur yön ilişkisinin “yoldan” ifadesinde nasıl tamamlandığını görür. Bu anlam yerel yol tümleciyle sınırlıdır; edatın bütün mekânsal ayrılık kullanımları etkinleştirilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:carried-opening",
      "prose": "İlk وَ, bağlama ve önceki yönetimi sürdürme anlamını taşır; bağımsız tetikleyici, Âd ve Semûd adlarının önceki yıkım anlatısının devamı olarak taşınmasıdır. Bağlaç ad dizisini sıfırdan başlatmak yerine önceki olay çerçevesine ekler ve tamamlanması okuyucuya bırakılan yönetici fiil hissini korur. Okur ilk kelimeden itibaren süren hüküm ve önceki sahneyle bağlılık duyar. Önceki yönetim yalnız bu yerel devamlılık basıncıdır; gizli fiil tek bir kesin biçimde kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:carried-opening:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "İlk وَ, bağlama ve önceki yönetimi sürdürme anlamını taşır; bağımsız tetikleyici, Âd ve Semûd adlarının önceki yıkım anlatısının devamı olarak taşınmasıdır. Bağlaç ad dizisini sıfırdan başlatmak yerine önceki olay çerçevesine ekler ve tamamlanması okuyucuya bırakılan yönetici fiil hissini korur. Okur ilk kelimeden itibaren süren hüküm ve önceki sahneyle bağlılık duyar. Önceki yönetim yalnız bu yerel devamlılık basıncıdır; gizli fiil tek bir kesin biçimde kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:course-pressure",
      "prose": "ٱلسَّبِيلِ yerel olarak “yol” anlamını taşırken, صَدَّ fiilinin müdahalesiyle akışı kesilen ve üzerinde ilerlenen bir rota gibi de duyulur. Bağımsız tetikleyici engelleme fiilidir; fiziksel rota ile amaca götüren yol arasındaki temas, alıkoymayı ilerleyen bir seyirden koparılma olarak hissettirir. Okur yolun önünün kesilmesini hareket hâlindeki bir rotaya müdahale gibi algılar. Yerel isim anlamı korunur; dökülme veya serbest akma bağımsız anlam olarak etkinleştirilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:course-pressure:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلسَّبِيلِ yerel olarak “yol” anlamını taşırken, صَدَّ fiilinin müdahalesiyle akışı kesilen ve üzerinde ilerlenen bir rota gibi de duyulur. Bağımsız tetikleyici engelleme fiilidir; fiziksel rota ile amaca götüren yol arasındaki temas, alıkoymayı ilerleyen bir seyirden koparılma olarak hissettirir. Okur yolun önünün kesilmesini hareket hâlindeki bir rotaya müdahale gibi algılar. Yerel isim anlamı korunur; dökülme veya serbest akma bağımsız anlam olarak etkinleştirilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:recognized-way",
      "prose": "ٱلسَّبِيلِ belirli ve tekil biçimiyle rastgele bir rotayı değil, ortakça tanınan yolu taşır. Bağımsız tetikleyici عَنِ tarafından kurulan hedef ilişkisi ve yolu belirli kılan artikel biçimidir; bu temas “yol”u seçeneklerden biri olmaktan çıkarıp zaten bilinen güzergâh olarak duyurur. Okur alıkoymanın tanınmayan bir yoldan değil, yönelinen ortak yoldan çevrilme olduğunu fark eder. Tanınırlık yerel biçim ve bağlanmayla sınırlıdır; tek bir mezhep veya geniş bir anlatı tezi seçilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:recognized-way:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلسَّبِيلِ belirli ve tekil biçimiyle rastgele bir rotayı değil, ortakça tanınan yolu taşır. Bağımsız tetikleyici عَنِ tarafından kurulan hedef ilişkisi ve yolu belirli kılan artikel biçimidir; bu temas “yol”u seçeneklerden biri olmaktan çıkarıp zaten bilinen güzergâh olarak duyurur. Okur alıkoymanın tanınmayan bir yoldan değil, yönelinen ortak yoldan çevrilme olduğunu fark eder. Tanınırlık yerel biçim ve bağlanmayla sınırlıdır; tek bir mezhep veya geniş bir anlatı tezi seçilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:governed-path-target",
      "prose": "ٱلسَّبِيلِ mecrûr biçimiyle عَنِ tarafından yönetilen ve alıkoymanın tam hedefini taşıyan isimdir. Bağımsız tetikleyici edatın ayrılma çerçevesidir; genitif hâl yolu bağımsız bir konu olmaktan çıkarıp alıkoymanın “-den” tamamlayıcısına kilitler. Okur yön ilişkisinin “yoldan” sözünde nasıl tamamlandığını görür. Bu yalnız yerel yönetim ve hedefi açıklar; hâlden yeni bir fail veya yol niteliği türetilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:governed-path-target:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلسَّبِيلِ mecrûr biçimiyle عَنِ tarafından yönetilen ve alıkoymanın tam hedefini taşıyan isimdir. Bağımsız tetikleyici edatın ayrılma çerçevesidir; genitif hâl yolu bağımsız bir konu olmaktan çıkarıp alıkoymanın “-den” tamamlayıcısına kilitler. Okur yön ilişkisinin “yoldan” sözünde nasıl tamamlandığını görür. Bu yalnız yerel yönetim ve hedefi açıklar; hâlden yeni bir fail veya yol niteliği türetilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:path-obstruction-collocation",
      "prose": "ٱلسَّبِيلِ ile صَدَّ birlikte duyulduğunda yol, alıkoymanın tanınan hedefini taşır. Bağımsız tetikleyici yol adıyla birleşen engelleme fiilidir; ikisi sonucu genel başarısızlık değil, belirli bir yol erişiminin kesilmesi olarak çerçeveler. Okur son hareketi soyut sapma değil yol hedefli engelleme kalıbı olarak tanır. Bu kolokasyon yerel cümle ve sunulan yol kanıtıyla sınırlıdır; her benzer yapıya otomatik taşınmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:path-obstruction-collocation:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ٱلسَّبِيلِ ile صَدَّ birlikte duyulduğunda yol, alıkoymanın tanınan hedefini taşır. Bağımsız tetikleyici yol adıyla birleşen engelleme fiilidir; ikisi sonucu genel başarısızlık değil, belirli bir yol erişiminin kesilmesi olarak çerçeveler. Okur son hareketi soyut sapma değil yol hedefli engelleme kalıbı olarak tanır. Bu kolokasyon yerel cümle ve sunulan yol kanıtıyla sınırlıdır; her benzer yapıya otomatik taşınmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:concessive-closure",
      "prose": "Son وَ, kapanıştaki anlayış durumunu önceki alıkoymaya ekleyen bağlama anlamını taşır; bağımsız tetikleyici كَانُوا ... مُسْتَبْصِرِينَ ile gerçekleşmiş صَدَّهُمْ arasındaki yan yanalıktır. Bağlı kapanış, içgörü durumunu saptırmayla aynı çerçevede tutunca “buna rağmen” etkisi doğar. Okur anlayışla nitelenen topluluğun çevrilmesindeki gerilimi fark eder. Ödünleme yerel ilişkidir; bağlaç tek başına bütün neden-sonuç düzenini yeniden yazmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:concessive-closure:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "Son وَ, kapanıştaki anlayış durumunu önceki alıkoymaya ekleyen bağlama anlamını taşır; bağımsız tetikleyici كَانُوا ... مُسْتَبْصِرِينَ ile gerçekleşmiş صَدَّهُمْ arasındaki yan yanalıktır. Bağlı kapanış, içgörü durumunu saptırmayla aynı çerçevede tutunca “buna rağmen” etkisi doğar. Okur anlayışla nitelenen topluluğun çevrilmesindeki gerilimi fark eder. Ödünleme yerel ilişkidir; bağlaç tek başına bütün neden-sonuç düzenini yeniden yazmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:established-insight-state",
      "prose": "كَانُوا, ardından gelen مُسْتَبْصِرِينَ niteliğini anlık bir fark ediş değil, alıkoyma anında zaten taşınan yerleşik bir durum olarak kurar. Bağımsız tetikleyici, yardımcı fiilin geçmiş çerçevesi ile partisipin birlikte kullanılmasıdır; anlayış saptırmadan sonra doğan geç bir ışık değil, onunla yan yana duran hâl olur. Okur içgörünün olaydan önce mevcut olduğunu görür. Kurulan durum ayetin geçmiş çerçevesiyle sınırlıdır; sonraki sonuçlar buradan belirlenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:established-insight-state:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "كَانُوا, ardından gelen مُسْتَبْصِرِينَ niteliğini anlık bir fark ediş değil, alıkoyma anında zaten taşınan yerleşik bir durum olarak kurar. Bağımsız tetikleyici, yardımcı fiilin geçmiş çerçevesi ile partisipin birlikte kullanılmasıdır; anlayış saptırmadan sonra doğan geç bir ışık değil, onunla yan yana duran hâl olur. Okur içgörünün olaydan önce mevcut olduğunu görür. Kurulan durum ayetin geçmiş çerçevesiyle sınırlıdır; sonraki sonuçlar buradan belirlenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:next-ayah-echo",
      "prose": "كَانُوا ile مُسْتَبْصِرِينَ arasındaki yardımcı fiil-partisip kuruluşu, kapanıştaki yerleşik hâli hemen sonraki ayette yeniden görülen yakın biçimsel yankıyla taşır. Bağımsız tetikleyici bu yakın tekrarın aynı kuruluşu korumasıdır; son kelime kopuk bir sıfat olmaktan çıkar ve sonraki ayete açılan devamlılık hissi verir. Okur kapanışın biçimsel olarak asılı kalmadığını fark eder. Yankı yalnız yakın karşılaştırmayla sınırlıdır; sonraki ayet burada yeniden yorumlanmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:next-ayah-echo:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "كَانُوا ile مُسْتَبْصِرِينَ arasındaki yardımcı fiil-partisip kuruluşu, kapanıştaki yerleşik hâli hemen sonraki ayette yeniden görülen yakın biçimsel yankıyla taşır. Bağımsız tetikleyici bu yakın tekrarın aynı kuruluşu korumasıdır; son kelime kopuk bir sıfat olmaktan çıkar ve sonraki ayete açılan devamlılık hissi verir. Okur kapanışın biçimsel olarak asılı kalmadığını fark eder. Yankı yalnız yakın karşılaştırmayla sınırlıdır; sonraki ayet burada yeniden yorumlanmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:plural-doublet-continuity",
      "prose": "كَانُوا, başta birlikte anılan Âd ve Semûd'u yeniden adlandırmadan tek bir çoğul özne olarak taşır. Bağımsız tetikleyici açılıştaki iki ad ve bunların ardından gelen ortak nitelemedir; çoğul yardımcı fiil gönderimi kapanışa kadar etkin tutar. Okur son niteliğin iki topluluğa birlikte yöneldiğini görür. Bu yalnız yerel özne devamlılığıdır; iki halkın bütün tarihi hakkında genelleme yapılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:plural-doublet-continuity:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "كَانُوا, başta birlikte anılan Âd ve Semûd'u yeniden adlandırmadan tek bir çoğul özne olarak taşır. Bağımsız tetikleyici açılıştaki iki ad ve bunların ardından gelen ortak nitelemedir; çoğul yardımcı fiil gönderimi kapanışa kadar etkin tutar. Okur son niteliğin iki topluluğa birlikte yöneldiğini görür. Bu yalnız yerel özne devamlılığıdır; iki halkın bütün tarihi hakkında genelleme yapılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:body-mind-contrast",
      "prose": "مُسْتَبْصِرِينَ içgörü ve kavrayış anlamını taşır; bağımsız tetikleyici, topluluğun yıkımla karşı karşıya kalan bedensel sonucu ile bu bilişsel nitelemenin aynı sahnede buluşmasıdır. Bedensel çöküş ile algısal yeterlik arasındaki mesafe, kapanıştaki ironiyi daha görünür kılar: bedenler düşmüş olsa da kavrayış dili hâlâ vardır. Okur gerilimi beden ile zihin arasındaki mesafede de görür. Bu karşıtlık sunulan sınırla sınırlıdır; bağımsız bir beden veya zihin öğretisi kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:body-mind-contrast:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مُسْتَبْصِرِينَ içgörü ve kavrayış anlamını taşır; bağımsız tetikleyici, topluluğun yıkımla karşı karşıya kalan bedensel sonucu ile bu bilişsel nitelemenin aynı sahnede buluşmasıdır. Bedensel çöküş ile algısal yeterlik arasındaki mesafe, kapanıştaki ironiyi daha görünür kılar: bedenler düşmüş olsa da kavrayış dili hâlâ vardır. Okur gerilimi beden ile zihin arasındaki mesafede de görür. Bu karşıtlık sunulan sınırla sınırlıdır; bağımsız bir beden veya zihin öğretisi kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:heightened-insight-range",
      "prose": "مُسْتَبْصِرِينَ onuncu kalıbın yoğunlaştırdığı algı ve içgörü anlamını taşır; bağımsız tetikleyici kelimenin kendi kalıp yapısı ve içindeki anlam aralığıdır. Bu aralık görmeyi, yükseltilmiş kavrayışı, bir niteliğe sahip olmayı veya böyle bir niteliği ileri sürmeyi açık tutar; dolayısıyla son sözcük yalnız bedensel görmeye indirgenmez. Okur burada yüksek kavrayış kapasitesinin veya iddiasının bulunduğunu fark eder. Yerel alan budur; en yüksek kesinlik, yalnız fiziksel görme ya da tek bir içgörü yorumu seçilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:heightened-insight-range:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مُسْتَبْصِرِينَ onuncu kalıbın yoğunlaştırdığı algı ve içgörü anlamını taşır; bağımsız tetikleyici kelimenin kendi kalıp yapısı ve içindeki anlam aralığıdır. Bu aralık görmeyi, yükseltilmiş kavrayışı, bir niteliğe sahip olmayı veya böyle bir niteliği ileri sürmeyi açık tutar; dolayısıyla son sözcük yalnız bedensel görmeye indirgenmez. Okur burada yüksek kavrayış kapasitesinin veya iddiasının bulunduğunu fark eder. Yerel alan budur; en yüksek kesinlik, yalnız fiziksel görme ya da tek bir içgörü yorumu seçilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:inverse-insight-echo",
      "prose": "مُسْتَبْصِرِينَ, önceki Şeytan karşılaşmasının tersine dönen bir yankısını taşır: orada temas algıyı açarken burada içgörü dili saptırmayı durdurmaz. Bağımsız tetikleyici, Şeytanın güzelleştirme ve alıkoyma işlemi ile kapanıştaki kavrayış niteliğinin karşılaştırılmasıdır; bu temas algının kendiliğinden kurtarıcı olmadığını gösterir. Okur içgörü sözcüğünün sonucu değiştirmediği için daha keskin bir terslik taşıdığını görür. Karşılaştırma sunulan tekil yankıyla sınırlıdır; dışarıya yayılan bir kanal veya yeni bir ayet yorumu kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:inverse-insight-echo:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مُسْتَبْصِرِينَ, önceki Şeytan karşılaşmasının tersine dönen bir yankısını taşır: orada temas algıyı açarken burada içgörü dili saptırmayı durdurmaz. Bağımsız tetikleyici, Şeytanın güzelleştirme ve alıkoyma işlemi ile kapanıştaki kavrayış niteliğinin karşılaştırılmasıdır; bu temas algının kendiliğinden kurtarıcı olmadığını gösterir. Okur içgörü sözcüğünün sonucu değiştirmediği için daha keskin bir terslik taşıdığını görür. Karşılaştırma sunulan tekil yankıyla sınırlıdır; dışarıya yayılan bir kanal veya yeni bir ayet yorumu kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:shared-perceptual-state",
      "prose": "مُسْتَبْصِرِينَ, iki topluluğu كَانُوا yardımcı fiilinin mansup haberi olarak ortak algı ve kavrayış hâliyle adlandırır. Bağımsız tetikleyici yardımcı fiilin çoğul öznesi ve açılışta birlikte anılan iki addır; mansup partisip niteliği kişilere değil ortak topluluğa yayar. Okur son sözcüğü tek tek kişilerin değil iki halkın birlikte taşıdığı durum olarak okur. Ortaklık yerel çoğul ve haber ilişkisine aittir; bütün bireylerin aynı kesinlikte olduğu seçilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:shared-perceptual-state:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مُسْتَبْصِرِينَ, iki topluluğu كَانُوا yardımcı fiilinin mansup haberi olarak ortak algı ve kavrayış hâliyle adlandırır. Bağımsız tetikleyici yardımcı fiilin çoğul öznesi ve açılışta birlikte anılan iki addır; mansup partisip niteliği kişilere değil ortak topluluğa yayar. Okur son sözcüğü tek tek kişilerin değil iki halkın birlikte taşıdığı durum olarak okur. Ortaklık yerel çoğul ve haber ilişkisine aittir; bütün bireylerin aynı kesinlikte olduğu seçilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:clarity-insight-envelope",
      "prose": "Ayet, dış açıklığı تَبَيَّنَ ile açılışta belirginleştirir ve topluluğu مُسْتَبْصِرِينَ ile kapanışta içgörü sahibi diye adlandırır; aradaki فَصَدَّ bu iki ucu davranışta karşılaştırır. Bağımsız tetikleyici, açılıştaki yurt kanıtı ile kapanıştaki algı niteliğinin aynı alıkoyma ilişkisine bağlanmasıdır. Böylece okur gerilimin bilgi eksikliğinden çok açıklığın davranışı yönetmemesi olduğunu fark eder. Bu ayet içi sentezdir; içgörü derecesi veya daha geniş bir tez ayrıca seçilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:clarity-insight-envelope:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "Ayet, dış açıklığı تَبَيَّنَ ile açılışta belirginleştirir ve topluluğu مُسْتَبْصِرِينَ ile kapanışta içgörü sahibi diye adlandırır; aradaki فَصَدَّ bu iki ucu davranışta karşılaştırır. Bağımsız tetikleyici, açılıştaki yurt kanıtı ile kapanıştaki algı niteliğinin aynı alıkoyma ilişkisine bağlanmasıdır. Böylece okur gerilimin bilgi eksikliğinden çok açıklığın davranışı yönetmemesi olduğunu fark eder. Bu ayet içi sentezdir; içgörü derecesi veya daha geniş bir tez ayrıca seçilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:accusative-name-frame",
      "prose": "عَادًا tenvinli mansup biçimiyle önceki yönetim altında taşınan adı ve yanındaki özel adla aynı çerçeveyi taşır. Bağımsız tetikleyici, açıkça söylenmeyen yönetici fiil hissi ile hemen ardından gelen ثَمُودَ adıdır; mansup hâl ve tenvin, açılışı basit bir ad listesi olmaktan çıkarıp bağlamla tamamlanan nesne dizisine dönüştürür. Okur iki adın anlatı içinde taşınan öğeler olduğunu fark eder. Elipsli yönetim bu yerel sınırda tutulur; tenvinden yeni bir fiil veya tarihsel anlam çıkarılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:accusative-name-frame:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "عَادًا tenvinli mansup biçimiyle önceki yönetim altında taşınan adı ve yanındaki özel adla aynı çerçeveyi taşır. Bağımsız tetikleyici, açıkça söylenmeyen yönetici fiil hissi ile hemen ardından gelen ثَمُودَ adıdır; mansup hâl ve tenvin, açılışı basit bir ad listesi olmaktan çıkarıp bağlamla tamamlanan nesne dizisine dönüştürür. Okur iki adın anlatı içinde taşınan öğeler olduğunu fark eder. Elipsli yönetim bu yerel sınırda tutulur; tenvinden yeni bir fiil veya tarihsel anlam çıkarılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:ruined-peoples-doublet",
      "prose": "عَادًا ve ثَمُودَ, aynı yönetim altında yan yana gelerek yıkım ve geride kalan kanıt sahnesinde birlikte duyulan bir ad çifti oluşturur. Bağımsız tetikleyici, iki adı bağlayan وَ ile hemen ardından gelen yurtların kalıntı olarak görünmesidir; koordinasyon onları aynı olay çerçevesinde toplar. Okur iki ismi bağımsız örnekler değil, aynı hükmü taşıyan çift olarak görür. Çiftlenme yerel koordinasyon ve sunulan karşılaştırmayla sınırlıdır; tarihsel ayrıntılar genişletilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:ruined-peoples-doublet:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "عَادًا ve ثَمُودَ, aynı yönetim altında yan yana gelerek yıkım ve geride kalan kanıt sahnesinde birlikte duyulan bir ad çifti oluşturur. Bağımsız tetikleyici, iki adı bağlayan وَ ile hemen ardından gelen yurtların kalıntı olarak görünmesidir; koordinasyon onları aynı olay çerçevesinde toplar. Okur iki ismi bağımsız örnekler değil, aynı hükmü taşıyan çift olarak görür. Çiftlenme yerel koordinasyon ve sunulan karşılaştırmayla sınırlıdır; tarihsel ayrıntılar genişletilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:return-name-irony",
      "prose": "عَادًا özel ad olarak kalırken, dönüş ve yinelemeyle ilişkilendirilen kök basıncı yıkım ve hakikate dönememe sahnesine hafif bir ironi taşır. Bağımsız tetikleyici, geri dönülmez sonuç ile tekrarlanan hata çevresidir; adın çağrışımı bu çevreye dokunur fakat fiile dönüşmez. Okur dönüş çağrışımının dönüşsüz sahnede neden ince bir gerilim oluşturduğunu fark eder. Dönüş basıncı arka plandadır; Âd yeni bir dönüş eylemi diye çevrilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:return-name-irony:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "عَادًا özel ad olarak kalırken, dönüş ve yinelemeyle ilişkilendirilen kök basıncı yıkım ve hakikate dönememe sahnesine hafif bir ironi taşır. Bağımsız tetikleyici, geri dönülmez sonuç ile tekrarlanan hata çevresidir; adın çağrışımı bu çevreye dokunur fakat fiile dönüşmez. Okur dönüş çağrışımının dönüşsüz sahnede neden ince bir gerilim oluşturduğunu fark eder. Dönüş basıncı arka plandadır; Âd yeni bir dönüş eylemi diye çevrilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:name-pair-lock",
      "prose": "İkinci وَ, ثَمُودَ adını önceki عَادًا adına aynı taşınmış yönetim altında bağlayan koordinasyon anlamını taşır. Bağımsız tetikleyici ilk adın nesne rolü ve ikinci adın aynı hâl çerçevesine girmesidir; biçimsel farklılıklar korunurken olay çerçevesi ortak kalır. Okur ortak hüküm ile biçimsel asimetriyi aynı anda duyar. Bağlama ve ritmik kilitleme yerel açılışla sınırlıdır; iki halk özdeşleştirilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:name-pair-lock:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "İkinci وَ, ثَمُودَ adını önceki عَادًا adına aynı taşınmış yönetim altında bağlayan koordinasyon anlamını taşır. Bağımsız tetikleyici ilk adın nesne rolü ve ikinci adın aynı hâl çerçevesine girmesidir; biçimsel farklılıklar korunurken olay çerçevesi ortak kalır. Okur ortak hüküm ile biçimsel asimetriyi aynı anda duyar. Bağlama ve ritmik kilitleme yerel açılışla sınırlıdır; iki halk özdeşleştirilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:depletion-name-pressure",
      "prose": "ثَمُودَ özel ad işlevini korurken, tükenme ve eksilmiş kaynak basıncı yurtların geride kalan kalıntı oluşuyla sınırlı bir renk kazanır. Bağımsız tetikleyici مِنْ مَّسَٰكِنِهِمْ ifadesinin görünür yurtları kaynak ve kanıt olarak getirmesidir; adın bu hizası yerleşimleri kaynakları tükenmiş bir sahne gibi de duyurur. Okur adın çağrışımı ile sessizleşmiş yurtların neden birlikte bir tükeniş resmi oluşturduğunu anlar. Tükenme arka plan basıncıdır; özel adın yerini almaz ve kesin etimoloji kurulmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:depletion-name-pressure:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ثَمُودَ özel ad işlevini korurken, tükenme ve eksilmiş kaynak basıncı yurtların geride kalan kalıntı oluşuyla sınırlı bir renk kazanır. Bağımsız tetikleyici مِنْ مَّسَٰكِنِهِمْ ifadesinin görünür yurtları kaynak ve kanıt olarak getirmesidir; adın bu hizası yerleşimleri kaynakları tükenmiş bir sahne gibi de duyurur. Okur adın çağrışımı ile sessizleşmiş yurtların neden birlikte bir tükeniş resmi oluşturduğunu anlar. Tükenme arka plan basıncıdır; özel adın yerini almaz ve kesin etimoloji kurulmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:diptote-asymmetry",
      "prose": "ثَمُودَ, عَادًا ile aynı taşınmış nesne görevini paylaşırken tenvin almayan çekim yüzeyiyle biçimsel bir asimetri taşır. Bağımsız tetikleyici, iki adın aynı yönetim içinde yan yana durmasıdır; ortak yıkım çerçevesi içinde farklı çekim davranışı duyulur. Okur iki halkın birlikte anılmasının tekdüze bir dilbilgisel kalıp olmadığını fark eder. Bu yalnız biçimsel karşılaştırmadır; çekim farkından halkların değeri çıkarılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:diptote-asymmetry:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ثَمُودَ, عَادًا ile aynı taşınmış nesne görevini paylaşırken tenvin almayan çekim yüzeyiyle biçimsel bir asimetri taşır. Bağımsız tetikleyici, iki adın aynı yönetim içinde yan yana durmasıdır; ortak yıkım çerçevesi içinde farklı çekim davranışı duyulur. Okur iki halkın birlikte anılmasının tekdüze bir dilbilgisel kalıp olmadığını fark eder. Bu yalnız biçimsel karşılaştırmadır; çekim farkından halkların değeri çıkarılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:thamud-dwelling-field",
      "prose": "ثَمُودَ, مِنْ مَّسَٰكِنِهِمْ ile birleştiğinde yalnız bir kavim adını değil, görünür yurtlar ve geride kalan yerleşimler alanını taşır. Bağımsız tetikleyici, özel adı yurtların kaynağına bağlayan مِنْ edatıdır; bu temas topluluğu okunabilir kalıntıya ve oradan belli olan tarihe bağlar. Okur Semûd adının neden hemen ardından gelen yurtlardan belli oluş cümlesiyle somutlaştığını görür. Bağ yerel yurt kanıtı ve sunulan karşılaştırmayla sınırlıdır; açık olmayan geleneksel ayrıntılar eklenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:thamud-dwelling-field:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "ثَمُودَ, مِنْ مَّسَٰكِنِهِمْ ile birleştiğinde yalnız bir kavim adını değil, görünür yurtlar ve geride kalan yerleşimler alanını taşır. Bağımsız tetikleyici, özel adı yurtların kaynağına bağlayan مِنْ edatıdır; bu temas topluluğu okunabilir kalıntıya ve oradan belli olan tarihe bağlar. Okur Semûd adının neden hemen ardından gelen yurtlardan belli oluş cümlesiyle somutlaştığını görür. Bağ yerel yurt kanıtı ve sunulan karşılaştırmayla sınırlıdır; açık olmayan geleneksel ayrıntılar eklenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:evidence-parenthesis",
      "prose": "İkinci kanıt cümleciğini açan وَ, taşınmış kavim adları arasına muhatabı doğrudan sokan bir kanıt parantezi kurar. Bağımsız tetikleyici قَدْ تَبَيَّنَ لَكُمْ ifadesidir; bağlaç ad listesinin akışını kısa süreliğine durdurup yıkıntıyı anlatılan tarihten muhatabın gördüğü delile çevirir. Okur ayetin yalnız geçmiş halklardan söz etmediğini, kanıtı kendisine gösterdiğini fark eder. Parantez etkisi yerel söylem düzeni ve ikinci kişi dönüşüyle sınırlıdır.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:evidence-parenthesis:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "İkinci kanıt cümleciğini açan وَ, taşınmış kavim adları arasına muhatabı doğrudan sokan bir kanıt parantezi kurar. Bağımsız tetikleyici قَدْ تَبَيَّنَ لَكُمْ ifadesidir; bağlaç ad listesinin akışını kısa süreliğine durdurup yıkıntıyı anlatılan tarihten muhatabın gördüğü delile çevirir. Okur ayetin yalnız geçmiş halklardan söz etmediğini, kanıtı kendisine gösterdiğini fark eder. Parantez etkisi yerel söylem düzeni ve ikinci kişi dönüşüyle sınırlıdır."
        }
      ]
    },
    {
      "finding_ref": "micro:certified-clarity",
      "prose": "قَدْ, ardından gelen perfect fiilin tamamlanmışlığını öne çıkaran gerçekleşmişlik anlamını taşır; bağımsız tetikleyici hemen arkasındaki تَبَيَّنَ fiilidir. Parçacık fiilden önce gelerek açıklığın ihtimal değil, kurulmuş ve hazır bir olgu olduğunu duyurur. Okur kanıt cümlesindeki açıklığın sonradan yapılacak bir yorum değil, zaten mevcut gerçeklik olduğunu hisseder. Kesinlik açıklık olayının gerçekleşmiş oluşuna aittir; muhatabın bu sonucu kabul ettiği iddia edilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:certified-clarity:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "قَدْ, ardından gelen perfect fiilin tamamlanmışlığını öne çıkaran gerçekleşmişlik anlamını taşır; bağımsız tetikleyici hemen arkasındaki تَبَيَّنَ fiilidir. Parçacık fiilden önce gelerek açıklığın ihtimal değil, kurulmuş ve hazır bir olgu olduğunu duyurur. Okur kanıt cümlesindeki açıklığın sonradan yapılacak bir yorum değil, zaten mevcut gerçeklik olduğunu hisseder. Kesinlik açıklık olayının gerçekleşmiş oluşuna aittir; muhatabın bu sonucu kabul ettiği iddia edilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:completed-clarity",
      "prose": "تَبَيَّنَ, yurtlardan gelen kanıtın muhatap için zaten açığa çıkmış ve anlaşılır olduğunu taşır. Bağımsız tetikleyici مِنْ مَّسَٰكِنِهِمْ kaynak ilişkisidir; tamamlanmış fiil, açıklığı görünür yurt kalıntılarına bağlayarak “belli olmuştur” sözünü somutlaştırır. Okur açıklığın yurtlardan okunabildiğini görür. Açıklığın kapsamı bu yurt kanıtıdır; her belirsizliğin giderildiği sonucu çıkarılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:completed-clarity:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "تَبَيَّنَ, yurtlardan gelen kanıtın muhatap için zaten açığa çıkmış ve anlaşılır olduğunu taşır. Bağımsız tetikleyici مِنْ مَّسَٰكِنِهِمْ kaynak ilişkisidir; tamamlanmış fiil, açıklığı görünür yurt kalıntılarına bağlayarak “belli olmuştur” sözünü somutlaştırır. Okur açıklığın yurtlardan okunabildiğini görür. Açıklığın kapsamı bu yurt kanıtıdır; her belirsizliğin giderildiği sonucu çıkarılmaz."
        }
      ]
    },
    {
      "finding_ref": "micro:audience-perception-frame",
      "prose": "تَبَيَّنَ لَكُمْ dış açıklığı muhatabın önüne yerleştirirken مُسْتَبْصِرِينَ içgörü niteliğini yıkılmış topluluğa verir; bağımsız tetikleyici aradaki فَصَدَّ alıkoymasıdır. Dış kanıt, muhataba ulaşan açıklık ve topluluğun iç kavrayışı aynı ayet çerçevesinde buluşunca sorun kanıtın yokluğu değil, açık kanıt ve içgörü varken yönelişin değişmesidir. Okur bu karşıtlığı fark eder. Bu ayet içi algı çerçevesidir; muhatapların her şeyi kavradığı veya tek bir kesinlik derecesi olduğu söylenmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:audience-perception-frame:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "تَبَيَّنَ لَكُمْ dış açıklığı muhatabın önüne yerleştirirken مُسْتَبْصِرِينَ içgörü niteliğini yıkılmış topluluğa verir; bağımsız tetikleyici aradaki فَصَدَّ alıkoymasıdır. Dış kanıt, muhataba ulaşan açıklık ve topluluğun iç kavrayışı aynı ayet çerçevesinde buluşunca sorun kanıtın yokluğu değil, açık kanıt ve içgörü varken yönelişin değişmesidir. Okur bu karşıtlığı fark eder. Bu ayet içi algı çerçevesidir; muhatapların her şeyi kavradığı veya tek bir kesinlik derecesi olduğu söylenmez."
        }
      ]
    },
    {
      "finding_ref": "micro:self-manifesting-clarity",
      "prose": "تَبَيَّنَ beşinci kalıbın kendiliğinden belirginleşme anlamını taşır; bağımsız tetikleyici مِنْ ile bağlanan yurt kanıtıdır. Oluş bildiren yapı açıklığı yapan bir açıklayıcıyı öne çıkarmadan, kanıtın kendi görünür yüzünden belirginleşmesini kurar. Okur harabeleri yalnız anlatılan delil değil, kendilerini açıklığa çıkaran yüz olarak fark eder. Kendiliğinden belirginleşme yerel biçim ve kaynak ilişkisiyle sınırlıdır; harabelere bilinç verilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:self-manifesting-clarity:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "تَبَيَّنَ beşinci kalıbın kendiliğinden belirginleşme anlamını taşır; bağımsız tetikleyici مِنْ ile bağlanan yurt kanıtıdır. Oluş bildiren yapı açıklığı yapan bir açıklayıcıyı öne çıkarmadan, kanıtın kendi görünür yüzünden belirginleşmesini kurar. Okur harabeleri yalnız anlatılan delil değil, kendilerini açıklığa çıkaran yüz olarak fark eder. Kendiliğinden belirginleşme yerel biçim ve kaynak ilişkisiyle sınırlıdır; harabelere bilinç verilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:accountable-witnesses",
      "prose": "لَكُمْ, açıklığın yöneldiği ikinci çoğul muhatabı yurtlardan gelen kanıtın alıcısı ve tanığı olarak cümleye yerleştirir. Bağımsız tetikleyici تَبَيَّنَ olayının bu dative alıcıya bağlanması ve مِنْ مَّسَٰكِنِهِمْ ile kanıt kaynağının gösterilmesidir; görünür kanıt muhatabın önüne gelir. Okur “size belli olmuştur” denirken kendisinin kanıtın sorumluluğu içine alındığını fark eder. Tanık etkisi alıcı rolünden çıkan sınırlı yorumdur; muhatabın fiili ayrıca seçilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:accountable-witnesses:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "لَكُمْ, açıklığın yöneldiği ikinci çoğul muhatabı yurtlardan gelen kanıtın alıcısı ve tanığı olarak cümleye yerleştirir. Bağımsız tetikleyici تَبَيَّنَ olayının bu dative alıcıya bağlanması ve مِنْ مَّسَٰكِنِهِمْ ile kanıt kaynağının gösterilmesidir; görünür kanıt muhatabın önüne gelir. Okur “size belli olmuştur” denirken kendisinin kanıtın sorumluluğu içine alındığını fark eder. Tanık etkisi alıcı rolünden çıkan sınırlı yorumdur; muhatabın fiili ayrıca seçilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:source-attachment-ambiguity",
      "prose": "مِنْ مَّسَٰكِنِهِمْ temel olarak açıklığın kaynağını taşır; bağımsız tetikleyici, edatın تَبَيَّنَ fiiline bağlanması ve genitif yurt adıdır. Bu kaynak-fiil ilişkisi öncelikliyken, kalıntıların halkları tanımlayan bir iz gibi okunması kontrollü bir yan duyum olarak açık kalır. Okur yurtların hem “nereden belli oldu” hem de “kim oldukları nasıl belli oldu” sorularına yaklaşabildiğini görür. Tanımlayıcı yan duyum temel kaynak çözümlemesinin yerine geçirilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:source-attachment-ambiguity:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مِنْ مَّسَٰكِنِهِمْ temel olarak açıklığın kaynağını taşır; bağımsız tetikleyici, edatın تَبَيَّنَ fiiline bağlanması ve genitif yurt adıdır. Bu kaynak-fiil ilişkisi öncelikliyken, kalıntıların halkları tanımlayan bir iz gibi okunması kontrollü bir yan duyum olarak açık kalır. Okur yurtların hem “nereden belli oldu” hem de “kim oldukları nasıl belli oldu” sorularına yaklaşabildiğini görür. Tanımlayıcı yan duyum temel kaynak çözümlemesinin yerine geçirilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:dwellings-as-evidence",
      "prose": "مِنْ, yan yana duran bir mekânı değil, açıklığın içinden çıktığı kaynağı ve kanıt mecrasını taşır. Bağımsız tetikleyici مَّسَٰكِنِهِمْ yurt adı ile تَبَيَّنَ açıklık fiilinin birleşimidir; edat yurtları açıklığın yanında duran dekor olmaktan çıkarıp delilin çıktığı yüzeye dönüştürür. Okur yıkıntıların kanıtı taşıyan etkin yüzey olarak cümledeki yerini fark eder. Mecra etkisi yerel edat-yurt birleşimidir; mekâna bilinç veya fail atfedilmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:dwellings-as-evidence:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مِنْ, yan yana duran bir mekânı değil, açıklığın içinden çıktığı kaynağı ve kanıt mecrasını taşır. Bağımsız tetikleyici مَّسَٰكِنِهِمْ yurt adı ile تَبَيَّنَ açıklık fiilinin birleşimidir; edat yurtları açıklığın yanında duran dekor olmaktan çıkarıp delilin çıktığı yüzeye dönüştürür. Okur yıkıntıların kanıtı taşıyan etkin yüzey olarak cümledeki yerini fark eder. Mecra etkisi yerel edat-yurt birleşimidir; mekâna bilinç veya fail atfedilmez."
        }
      ]
    },
    {
      "finding_ref": "micro:evidence-insight-gap",
      "prose": "تَّبَيَّنَ içindeki açığa çıkma anlamı, yurtlardan gelen kanıtın görünür ve anlaşılır olmasını taşır; bağımsız tetikleyici مَّسَٰكِنِهِمْ, yerleşilmiş yurtları açıklığın somut kaynağı olarak getirir. Bu iki anlam temas edince yurtlar saptırılmadan önce zaten dışarıdan okunabilir bir açıklık sunar. Ardından صَدَّهُمْ ile taşınan alıkoyma, مُسْتَبْصِرِينَ ile taşınan iç kavrayışa rağmen bu açıklığın davranışı yönetmediğini gösterir. Böylece başlangıçtaki “gerçeği göremedikleri için saptılar” okuması, dış kanıt ve iç kavrayış mevcutken bağlılığın harekete dönüşmemesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; temel alıkoyma anlamını değiştirmez, dış kanıtı ayrıca bir fail iddiasına dönüştürmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:evidence-insight-gap:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "تَّبَيَّنَ içindeki açığa çıkma anlamı, yurtlardan gelen kanıtın görünür ve anlaşılır olmasını taşır; bağımsız tetikleyici مَّسَٰكِنِهِمْ, yerleşilmiş yurtları açıklığın somut kaynağı olarak getirir. Bu iki anlam temas edince yurtlar saptırılmadan önce zaten dışarıdan okunabilir bir açıklık sunar. Ardından صَدَّهُمْ ile taşınan alıkoyma, مُسْتَبْصِرِينَ ile taşınan iç kavrayışa rağmen bu açıklığın davranışı yönetmediğini gösterir. Böylece başlangıçtaki “gerçeği göremedikleri için saptılar” okuması, dış kanıt ve iç kavrayış mevcutken bağlılığın harekete dönüşmemesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; temel alıkoyma anlamını değiştirmez, dış kanıtı ayrıca bir fail iddiasına dönüştürmez."
        }
      ]
    },
    {
      "finding_ref": "micro:valuation-capture",
      "prose": "زَيَّنَ içindeki güzelleştirme anlamı, bağımsız tetikleyici أَعْمَالَهُمْ ile temas edince eylemlerin değerini ve görünüşünü yeniden sunan bir işleme dönüşür. ٱلشَّيْطَانُ, azgın ve karşıt varlık anlamını taşıyan adıyla, زَيَّنَ fiilinin faili olarak bu yeniden değerlendirmeyi anonim bir etki olmaktan çıkarır. أَعْمَالَهُمْ içindeki bilerek yapılan iş anlamı, aynı fiilin tetiklemesiyle korunur: kişiler eylemeye devam ederken eylemlerinin değerlendirme yüzeyi yönlendirilir. صَدَّهُمْ anlamı, bağımsız tetikleyici ٱلسَّبِيلِ ile buluşunca soyut bir başarısızlığı değil, belirli bir yoldan çevrilmeyi taşır; ٱلسَّبِيلِ de bu alıkoyma ile yürünebilir ve amaca götüren yol olarak kalır. Böylece başlangıçtaki “dışarıdan gelen tempter görünmeyen bir yolu kapattı” okuması, kişinin kendi amaçlı eylemlerinin çekici biçimde yeniden değerlendirilmesi ve eylem sürerken yönün değiştirilmesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; eylemlerin sahipliğini, failin varlığını veya yolun gerçekliğini silmez.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:valuation-capture:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "زَيَّنَ içindeki güzelleştirme anlamı, bağımsız tetikleyici أَعْمَالَهُمْ ile temas edince eylemlerin değerini ve görünüşünü yeniden sunan bir işleme dönüşür. ٱلشَّيْطَانُ, azgın ve karşıt varlık anlamını taşıyan adıyla, زَيَّنَ fiilinin faili olarak bu yeniden değerlendirmeyi anonim bir etki olmaktan çıkarır. أَعْمَالَهُمْ içindeki bilerek yapılan iş anlamı, aynı fiilin tetiklemesiyle korunur: kişiler eylemeye devam ederken eylemlerinin değerlendirme yüzeyi yönlendirilir. صَدَّهُمْ anlamı, bağımsız tetikleyici ٱلسَّبِيلِ ile buluşunca soyut bir başarısızlığı değil, belirli bir yoldan çevrilmeyi taşır; ٱلسَّبِيلِ de bu alıkoyma ile yürünebilir ve amaca götüren yol olarak kalır. Böylece başlangıçtaki “dışarıdan gelen tempter görünmeyen bir yolu kapattı” okuması, kişinin kendi amaçlı eylemlerinin çekici biçimde yeniden değerlendirilmesi ve eylem sürerken yönün değiştirilmesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; eylemlerin sahipliğini, failin varlığını veya yolun gerçekliğini silmez."
        }
      ]
    },
    {
      "finding_ref": "micro:settlement-reversal",
      "prose": "مَّسَٰكِنِهِمْ içindeki yerleşme ve sabit kalma anlamı, bağımsız tetikleyici تَّبَيَّنَ ile buluşunca hareketi sona ermiş yurt yüzeyinin okunabilir tanıklığına dönüşür. Yerleşim için kurulmuş ve artık hareketsiz kalan yer, açıklık fiili sayesinde sahiplerinin yokluğunu saklamaz, açığa çıkarır. Aynı yurt sözcüğü sabit yer ve alışılmış düzen anlamını da taşır; yine تَّبَيَّنَ ile tetiklenince bu düzenin araçları sahipleri yokken düzenin sonucunu gösteren kanıta dönüşür. تَّبَيَّنَ içindeki belirginleşme anlamı, bağımsız tetikleyici olarak bu hayatta kalan yurtlarla temas edince kalıcılık iddiasını tersine çevirir: yurtların sürmesi topluluğun dayanıklılığını değil yok oluşunu açık eder. Böylece başlangıçtaki “yurtlar yalnızca halkların yaşadığı yerleri gösterir” okuması, yerleşme araçlarının sahiplerinden uzun yaşayarak kalıcılık iddiasına karşı tanıklık etmesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; yurtlara irade verilmez ve tek bir açıklama dayatılmaz.",
      "semantic_landings": [
        {
          "semantic_refs": [
            "micro:settlement-reversal:claim-mechanism-payoff-boundary"
          ],
          "prose_quote": "مَّسَٰكِنِهِمْ içindeki yerleşme ve sabit kalma anlamı, bağımsız tetikleyici تَّبَيَّنَ ile buluşunca hareketi sona ermiş yurt yüzeyinin okunabilir tanıklığına dönüşür. Yerleşim için kurulmuş ve artık hareketsiz kalan yer, açıklık fiili sayesinde sahiplerinin yokluğunu saklamaz, açığa çıkarır. Aynı yurt sözcüğü sabit yer ve alışılmış düzen anlamını da taşır; yine تَّبَيَّنَ ile tetiklenince bu düzenin araçları sahipleri yokken düzenin sonucunu gösteren kanıta dönüşür. تَّبَيَّنَ içindeki belirginleşme anlamı, bağımsız tetikleyici olarak bu hayatta kalan yurtlarla temas edince kalıcılık iddiasını tersine çevirir: yurtların sürmesi topluluğun dayanıklılığını değil yok oluşunu açık eder. Böylece başlangıçtaki “yurtlar yalnızca halkların yaşadığı yerleri gösterir” okuması, yerleşme araçlarının sahiplerinden uzun yaşayarak kalıcılık iddiasına karşı tanıklık etmesi yönünde genişler. Bu, kaynağın okuyucuya bağlanmamış olması ve kapsamının belirtilen çevreden geniş tutulması nedeniyle nitelikli bir ek okumadır; yurtlara irade verilmez ve tek bir açıklama dayatılmaz."
        }
      ]
    }
  ],
  "friction_notes": [
    "Bağlantı kayıtları ve seçilmiş bağlam birimleri bulunmadığından prose içinde bağlantı veya ek bağlam rezonansı kurulmadı.",
    "Üç nitelikli ek okuma, okuyucu kimliği ve kapsam sınırlılığı nedeniyle temel sözlüksel okumaların yerine geçirilmeden sunuldu.",
    "Bütün aktivasyonlar odak yüzeyindeki taşıyıcılarla sınırlı tutuldu; kaynakta bulunmayan daha geniş bir kanıt alanı eklenmedi."
  ]
}

</micro_scope_prose>

<macro_scope_prose>
Âd ve Semûd'un da yok edildiği bildirilir; onların yurtlarının kalıntıları, yaşananların açıkça görülebilen izi olarak kalmıştır. Aynı bağlam, Şeytan'ın kendi yaptıklarını onlara güzel gösterdiğini ve anlayabilecek durumda oldukları hâlde onları yoldan alıkoyduğunu söyler. Bu doğrudan anlam, bütün çağrışımların zemininde kalır: görünür tarihî kalıntı ile insanı tanınan yoldan uzaklaştıran yanıltıcı güzelleştirme birlikte düşünülür.

Buradaki “yol” diye karşılanan es-Sebîl, temel olarak insanların üzerinde ilerlediği ve bir amaca ulaştıran güzergâh anlamını taşır. 29:29'da aynı kelimenin yol kesme ilişkisi içinde, yanında yolda bulunan erkeklerle anılması, odaktaki yolu üzerinde yürünüp kullanılan işlek bir güzergâh olarak belirginleştirir. Odaktaki sadda fiilinin “yüz çevirmek, alıkoymak” yönü, bu kesme sahnesiyle temas edince basit bir sapmadan çok geçişi fiilen kapatan bir yönlendirmeye dönüşür. A'mâl kelimesinin olağan “yapılan işler” anlamı da aynı yol kelimesiyle birleşerek, tekrar tekrar kullanılarak işlek hâle gelmiş bir yol imgesini destekler; a'mâl burada yol diye çevrilmez. 29:29'daki erkekler, yolda yaya hareket eden bedenleri sahneye getirir; böylece alıkoyma, hem yolu hem ona bağlı yolcuları etkileyen bir engel gibi duyulur. Yolun kesilmesi, umuda veya varılacak yere doğru ilerlemenin önünde kalma ve geçişin zorla kapatılması duygusunu da taşır. Ancak bu yerel görüntü su yolunu, özel bir geçidi, kaybolmuş bir bineği ya da ayrıca kurulmuş bir soygun olayını ileri sürmez; ana anlam, Şeytan'ın insanları yoldan çevirmesi olarak kalır.

Mesâkin kelimesinin yerleşilmiş mesken anlamı, 29:37'de kendi yurtlarında yere çakılıp kalan bedenlerin sahnesiyle karşılaşınca hareketin dinip durması yönünü de açar. Böylece yurtlar yalnızca geçmişi kanıtlayan görülebilir yerler değil, hareketin sona erdiği ve geride kalanların orada sabitlendiği mekânlar olarak duyulur. Bu, mesâkin'i doğrudan “yıkım” veya “hareketsizlik” diye çevirmek değildir; olağan mesken anlamının içine, bağlamın tetiklediği yerel bir son-durma görüntüsü eklenir.

Yurtlar, yalnızca hatırlanan tarihî yerler değil, parçaları birbirine bağlanarak ayakta duran yapılar olarak da incelenebilir. Odaktaki müstebsirîn kelimesi öncelikle gören ve anlayan kimseleri anlatırken, 29:41'de örümcek ağı ile evin birlikte anılması, kelimenin ek yeri ve birleşim kenarı yönünü yapısal bir temas noktası olarak öne çıkarır. Böylece bir evin güveni, parçalarının nasıl birleştiği ve yükü nasıl taşıdığı üzerinden düşünülür. 29:41'deki beyt, açık bir barınak ve konut imgesiyle meskenleri bu küçük yapısal örneğe bağlar; 29:44'teki hakk kelimesinin yerindelik ve tam yerine oturma yönü, her parçanın kendi yuvasına uygun düşmesi fikrini güçlendirir. 29:31'deki yerleşim sözüyle birlikte duyulan, çadır direğinin başını taşıyan ahşap çerçeve imgesi ile 29:28'de topluluğu anlatan kelimenin yanında beliren dikey taşıyıcı imgesi de yerleşimi ayakta tutan görünmeyen iskeleti hissettirir. Bu son yapısal görüntüler, odaktaki kelimeleri teknik bina terimlerine çevirmeden, kalıntıların nasıl kurulmuş ve nasıl taşınmış olabileceği sorusunu açar; yurtların tarihî delil olarak görünürlüğü ise birincil anlam olarak kalır.

Odaktaki tebeyyene fiilinin “açığa çıkıp belirginleşme” yönü, 29:35'te geride bırakılan apaçık işaretle karşılaşınca, anlamı olay geçtikten sonra da açılan bir iz görüntüsü kazanır. Müstebsirîn'in görme ve iç kavrayış yönü, aynı ayetteki “anlayıp kavrayanlar” ifadesiyle birleşir; böylece görmek yalnızca yüzeyde bir şey seçmek değil, görülen kalıntının ne anlama geldiğini kavramaktır. 29:28'deki ayırt edici alamet çağrışımı, 29:35'teki açık işaret ve odaktaki yol ilişkisiyle birleştiğinde, yurtlar geçmişi gösteren sabit izler olmanın yanında tanımayı belli bir yöne sevk eden işaretler gibi çalışır. 29:35'teki “geride bırakma” fiili de etkinin olayla birlikte silinmediğini, kalıntının tanıklığı sürdürdüğünü düşündürür. Bu, tarihî görünürlük ve içgörü iddiasını koruyan yerel bir okumadır; sûrenin tamamına yayılan bir işaret sistemi kurmaz, kalıntıyı ayrıca sözlü açıklama yapan bir metin gibi sunmaz ve odaktaki tarihî iddianın yerini almaz.

Mesâkin'in yerleşim ve mesken anlamı, içinde yaşayanları ve bir yeri yaşanır kılan sükûneti de bağlama açar. 29:31'deki ahl sözü, ev halkı ve bir yere ait olanlar anlamıyla, kimlerin o mekâna dâhil edildiği ve kimlerin kabul edilmeye uygun görüldüğü sorusunu getirir; aynı ayetteki köy ve yerleşim bağlamı bu soruyu somut bir topluluğa bağlar. 29:41'deki beyt ise ev ile ev halkı veya aileyi birlikte duyurarak fizikî konut ile sosyal aidiyet arasında bir köprü kurar. 29:31'de gelenlerle ve müjdeyle birlikte kurulan sahne, meskeni yalnız barınma yeri değil, karşılama ve kabul ilişkilerinin gerçekleştiği yer olarak hissettirir. Bununla birlikte odak hâlâ geçmişi açıkça gösteren yurtları anlatır; burada genel bir aile anlamı, odakta bulunmayan yemek veya ikram ayrıntıları ya da bu tarihî yurtların güvenli ve onaylanmış olduğu sonucu eklenmez.

Odaktaki zeyyene fiili, bir şeyi güzelleştirme ve güzelliğini görünür kılma anlamını taşır. 29:41'de adı açıkça konan ev ile hemen onun zayıflığını belirten ifade bir araya geldiğinde, görünüş ile taşıma gücü arasındaki farkı somutlaştıran yerel bir karşıtlık oluşur. Bu temas, yapılan işlerin çekici ve yerleşik görünen bir yüzeyle sunulup alttaki yetersizliği gizleyebilmesini düşündürür; güzelleştirme, yapının gerçekten taşıyıp taşımadığını fark etmeyi geciktiren bir sunum hâline gelir. Yine de zeyyene fiili zayıflık demek değildir: temel anlam, Şeytan'ın onların işlerini güzel göstererek onları yoldan çevirmesidir; kırılgan barınak karşılaştırması yalnızca bu bağlamda açılır.

Bunun yanında, ihtiyat payı korunarak tutulması gereken başka bir okuma daha belirir. Mesâkin'in sabitlenmiş yer ve yerleşim yönü ile tebeyyene'nin açıkça görünür olmayı bildiren yönü, 29:37'deki yerleşim sonrası manzara, 29:39'daki açık delillere rağmen sergilenen kibir, 29:40'ta suça bağlanan farklı sonuçlar ve 29:41-43'teki kendine dayanak ve koruyucu seçme, zayıf ev, benzetme ve akıl-bilgi silsilesiyle birlikte düşünülür. Bu dizilim, odaktaki yurtları yalnızca geçmiş felaketin izlerini koruyan yerler olmaktan çıkarıp, güvenliği tasarlanmış görünen fakat kendisine emanet edilen hayatı taşıyamayan bir düzenek olarak yeniden görmeye izin verir. Burada mesele, yerleşim, görünür kanıt, kibir, sorumluluğa bağlanan sonuç ve seçilmiş dayanakların gerçekten taşıyıcı olup olmadığıdır. Bu, her belirsiz kelime için yeni bir sözlük karşılığı ileri süren kesin bir çeviri değil, bağlamın kurduğu ihtiyatlı bir yapısal benzetmedir. 29:41'deki örneğin yıkıntılardan bağımsız biçimde aidiyet veya ittifak ilişkisini anlatıyor olabileceği ihtimali de korunur; iki açıklamadan biri kesinleştirilmez ve bu okuma sûrenin tamamına yayılan bir ana teze dönüştürülmez.

Daha şaşırtıcı ve keşif niteliğinde bir benzetmede, odaktaki es-Sebîl'in olağan yol anlamı ile müstebsirîn'in görme ve fark etme yönü, 29:41'deki örümcek ağı ve zayıflık imgesiyle karşılaşır. Bu temas, yolu gözün üzerine serilmiş ince, ağsı bir perde gibi hayal ettirir: ayırt etme yetisi tamamen yok olmaz, zayıf örtünün altında sürer. Böylece alıkoyma, yalnızca dışarıdan konan güçlü bir engel değil, güzelleştirilmiş görünüşün görüş alanını örten ve görüntüsünden daha büyük bir etki bırakan ince bir tabaka olarak da hissedilir. Bu, es-Sebîl'i göz perdesi diye çevirmek değildir; birincil anlam, insanların anlayabilecek durumda oldukları hâlde yoldan çevrilmesi olarak kalır. Örümcek ağı ve onun zayıflığı burada benzetmeyi tetikleyen bağımsız bağlam unsurlarıdır; gerçek bir göz hastalığı veya kelimenin doğrudan böyle bir nesneyi adlandırdığı ileri sürülmez.

Son olarak, Âd ve Semûd adları ile odaktaki tebeyyene'nin açıklık yönü, 29:40'taki “her biri” ve suça bağlanan sonuç ifadeleriyle birlikte, keşif niteliğinde bir kayıt veya vaka çizelgesi benzetmesi açabilir. Âd ve Semûd yine öncelikle iki topluluğun özel adlarıdır; fakat her adın, görünür bir yurt izi ve ona bağlanan sonuçla birlikte ayrı bir vaka gibi okunabilmesi mümkündür. Tebeyyene'nin belirginlik anlamı, bu vakaların dağınık bir isimler listesi değil, görülebilen ve sorumluluğu ilişkilendirilebilen kayıtlar gibi durmasını sağlar. Bu sayma ve toplam içine katma çağrışımı, Âd adının etimolojisi ya da çeviri karşılığı değildir; özel adların olağan niteliği korunarak, 29:40'taki “her biri” ve suç imgesiyle açılan sınırlı, ihtiyatlı bir benzetme olarak kalır.

</macro_scope_prose>

<global_scope_prose>
## Süslenmiş eylem, kavrayış ile yol arasına engel koyabilir

Odak ayetindeki “sadda” fiili, yüz çevirme ve alıkoyma anlamını taşır. 27:24’te amellerin güzelleştirilmesinin ardından yoldan çevirme gelmesi, bu fiilin taşıdığı engelleme işlevini bağımsız bir daha geniş ilişkiyle görünür kılar. Böylece süslenmiş eylem, mevcut iç kavrayış ile yol arasında kurulmuş somut bir engel gibi okunabilir. Bu bağlantı, dağ anlamını devreye sokmaz; ayrıca 27:24’teki hedef ifadenin biçimbilgisel çözümlemesi verilmediği için nedensel işleyiş kesinleştirilemez.

## Görünür kanıt, yola bağlılığı garanti etmez

Odak ayetindeki “tebeyyene” açığa çıkıp belirginleşme, “mesâkin” yerleşilip yaşanan yerler, “müstabsırîn” ise iç kavrayış anlamını taşır. 29:35’teki geride kalan açık iz, bu üç taşıyıcıyı maddi bir kanıt sahnesinde buluşturur: yerleşim kalıntıları incelenebilir bir dış kanıta dönüşürken kavrayış, yönelmeyi kendiliğinden güvenceye bağlamaz. Böylece açık kanıt ile içsel anlama kapasitesinin, yoldan sapma ihtimali ortadan kalkmadan birlikte bulunabileceği görülür. Bu, geniş okuma yürüyüşü içindeki sınırlı bir yankıdır; görme ile kavrayış arasında bir hiyerarşi kurmaz, bütün sureyi açıklayan bir tez ileri sürmez ve kavrayış kelimesinin tüm sözlük alanını belirlemez. Yola bağlılığın kırılganlığı da burada kesin hüküm değil, yorumlayıcı bir çıkarımdır.

## Güzelleştirilmiş eylemler rakip bir yola yöneltebilir

Odak ayetinde “zeyyene” güzelleştirme ve güzelliği görünür kılma, “a‘mâl” bilerek ortaya konan eylem, “sadda” yüz çevirme ve alıkoyma, “sebîl” ise üzerinde ilerlenen ve amaca götüren yol anlamında işler. “Şeytan” adlandırması da bu dizide yönünden ayıran, karşıtlık kuran bir işlevle okunur. 27:24, bu beş yüzeyi aynı Arapça kuruluş içinde yeniden bir araya getirerek güzelleştirmenin yoldan çevirme işleminden önce geldiğini gösterir. Odak okuması böylece yalnızca engellenmiş bir yol görüntüsü olmaktan çıkar; eylemlerin çekici biçimde sunulmasının yön kaymasına aracılık edebileceği bir sürece dönüşür. Bununla birlikte eylemler nesnel olarak iyi hale gelmiş sayılmaz, başka şeytan imgeleri bu okumaya eklenmez ve ilişkinin nedensel mi, retorik mi, yoksa ikisi birden mi olduğu kesinleştirilmez. 27:24’ün biçimbilgisel çözümlemesi sunulmadığı için bu tekrar ihtiyatlı bir dayanak olarak kalır.

## İç kavrayış davranış sınamasına konur

Odak ayetindeki “müstabsırîn” ifadesi, bilme, kalbe nüfuz eden kavrayış ve doğrulanmış anlayış kapasitesini taşır. 29:2-4’te sınanma, doğruluğun yoklanması, bilerek yapılan iş ve hüküm verme art arda gelerek bu kapasiteyi davranış içinde sınayan bağımsız bir çerçeve kurar. Odak ayetindeki güzelleştirilmiş eylemler bu çerçeveye döndüğünde, kavrayışın yokluğundan çok eylemi yönetip yönetemediği sorusu öne çıkar. Bu okuma, içgörüyü başarısızlık ihtimali taşıyan ama mevcut bir yeti olarak gösterir. Olağan iç kavrayış anlamı korunur; kelimenin dünyevi yeterliği de kapsayıp kapsamadığı karara bağlanmaz ve davranışa yapılan aktarım ihtiyatlı, yorumlayıcı bir çıkarım olarak kalır.

## Saptırma, rakip bir yola katılım sağlayabilir

Odak ayetindeki “sadda” yüz çevirme ve alıkoyma, “sebîl” ise tanınan bir yol ve amaca ulaştıran güzergâh anlamını taşır. 29:12’de başka bir yolu izlemeye çağrı, 29:13’te ise sonuçların ve yüklerin başkalarınca taşınacağı güvencesi, bu iki taşıyıcıyı toplumsal bir yönlendirme sahnesine bağlar. Böylece yoldan çevirme yalnızca yön kaybı değil, bedeli başkasına devredilmiş gibi sunulan rakip bir güzergâha katılım olarak da okunabilir. Odak ayetindeki tanınan yoldan yüz çevirme anlamı korunur; davet, takip ve yük aktarımı ise sınırlı bir genişletmedir, evrensel bir model olarak ileri sürülmez. Katılım ve yük devri arasındaki bağın bir bölümü yorumlayıcı kaldığından sonuç kesin bir nedensellik iddiası değildir.

## Güzelleştirme toplumsal bir engele dönüşebilir

Odak ayetindeki “zeyyene” güzelliği görünür kılma, “a‘mâl” bilinçli eylem, “sebîl” ise insanların üzerinde ilerlediği yol anlamını taşır. 29:17’deki uydurma değer, 29:25’teki bağ kurma ve toplu görünürlük, 29:29’daki yolu kesme görüntüsüyle birleşerek bağımsız bir toplumsal yayılım zinciri kurar. Bu zincir odak ayetine döndüğünde, çekici yüzeyin özel bir değerlendirme olmaktan çıkıp ortaklaşa sürdürülen bir davranışa dönüşebileceği görülür: bilinçli eylem, ortak değeri kamusal bir olguya taşır ve yol başkaları için de kapanır. Bu, güzelleştirmenin engeli sabitleyip yeniden üretebileceğine dair sınırlı bir yayılım varsayımıdır; her grup bağının aldatıcı olduğu söylenmez. Uydurma, toplanma, bağlanma ve yol kesme alanlarının tümü odak kelimelerinin sözlük anlamı olarak kurulmaz.

## Yerleşimler bir gözlem ve kanıt alanı oluşturur

Odak ayetindeki “tebeyyene” açıklığa kavuşma, “mesâkin” ise yerleşilmiş ve sabit bir mekân anlamını taşır. 29:19-20’de hareket etme ve yönelmiş biçimde inceleme, 29:35’te de geride kalmış açık bir iz bulunması, bu iki taşıyıcıya maddi bir işleyiş kazandırır. Hareket eden gözlemci sabit yerleşimlere gider, onları inceler ve orada kalan sonucu okur; böylece meskenler yalnızca miras alınmış hatırlatıcılar değil, yeniden gözlemlenebilir kanıt noktaları haline gelir. Bu, çağdaş anlamda bir arkeoloji talimatı değil, metinler arası işaretlerden çıkarılan sınırlı bir gözlem düzenidir. Yerleşim, hane veya başka özel kullanımların tümü bu odak okumasına eklenmez.

## Uygulama, çekici görünen eyleme karşı bir denetim sağlayabilir

Odak ayetindeki “zeyyene” güzelleştirme ve güzelliği görünür kılma, “a‘mâl” ise bilerek ortaya konan iş veya eylem anlamını taşır. 29:45’te tekrarlanan uygulamanın çirkin ve sakıncalı eylemden alıkoyucu bir ilişki içinde kurulması ve insanların yaptıklarına dönmesi, aynı davranış düzeyinde bağımsız bir karşı kuvvet oluşturur. Böylece odak ayetindeki güzelleştirme, eylemi çekici gösteren bir işlem olarak kalırken uygulama, bu çekiciliğin davranışa dönüşmesini sınayabilecek bir denetim noktası olarak okunur. Bu, bir karşı ilişki önerisidir; odak kelimelerinin yeni bir sözlük anlamı veya uygulamanın her durumda sonuç vereceğine dair mekanik bir güvence değildir.

## Bilgi, bağlayıcı olmadan da mevcut kalabilir

Odak ayetindeki “müstabsırîn” iç kavrayış, “sadda” ise yüz çevirme ve alıkoyma anlamını taşır. 29:47-49’da içteki işaretler ve bilgi inkârla yan yana getirilir; 29:61-63’te doğru cevaplar, yüz çevirme ve düşünsel başarısızlıkla birlikte görünür. Bu daha geniş düzenek, kavrayışın gerçekliğini korurken onun bağlılık, çıkarım veya davranış üzerindeki gücünün kesilebileceğini gösterir. Böylece odaktaki içgörü terimi ironik olmak zorunda kalmaz: biliş mevcut olabilir, fakat eylemi bağlamayabilir. Olağan kavrayış anlamı korunur; sonraki bütün cevapların istikrarlı bir bilişi ifade ettiği veya tek bir psikolojik model oluşturduğu ileri sürülmez.

## Hangi bağlılığın eylemi yönettiği duruma göre değişebilir

Odak ayetindeki “zeyyene” güzelleştirmeyi, “kânû” ise bir hâlin gerçekten mevcut oluşunu bildirir; böylece kavrayışlı olma hâli gerçek bir durum olarak cümlede yer alır. 29:64-65’te oyalanma ve amaçsız hareket, sıkıntı anında tek bir sığınak arama, kurtuluş ve ardından eski bağlara dönme sıralanır. Bu bağımsız durum dizisi, odak ayetindeki güzelleştirilmiş eylemin davranışı her koşulda aynı biçimde yönetmeyebileceğini düşündürür: kavrayış mevcut kalabilir, kriz anında etkinleşebilir, olağan dikkat ve bağlılık düzeni geri döndüğünde denetimini yitirebilir. Buradaki oluş bildiren yapı dikkat çekiciliğinin eş anlamlısı değildir; kriz de tek etkinleştirici olarak sunulmaz. Dikkatin öne çıkması ile davranış denetimi arasındaki model, metinler arası karşılaştırmadan çıkan sınırlı ve yorumlayıcı bir çıkarımdır.

## Kavrayış ile güvenin yöneldiği nesne ayrışabilir

Odak ayetindeki “müstabsırîn” iç kavrayış ve kanıtı kavrama kapasitesini taşır. 29:67’de görme, güvenli bir sığınak, çevreden gelen kuşatıcı tehdit ve asılsız olana inanma aynı karşılaştırma içinde bulunur. Bu daha geniş ilişki, kişinin şartları doğru algılayabildiği halde yerleşik güvenini yanlış bir nesneye verebileceğini gösterir; odak okuması böylece yalnızca algı sorununa değil, güvenin nereye tahsis edildiğine yönelir. Kelimeler arasındaki biçimsel ortaklık tek başına nedensellik kanıtı değildir ve güvenin yer değiştirmesine dair sonuç ihtiyatlı kalır.

## Bağlı çaba yolları açabilir

Odak ayetindeki “sadda” yüz çevirme ve alıkoyma, “sebîl” ise üzerinde ilerlenen ve bir amaca ulaştıran yol anlamını taşır. 29:69’da çabanın rehberlikle buluşması ve yolların çoğul biçimde açılması, odaktaki kapalı güzergâha bağımsız bir karşı ilişki sunar. Böylece algının tek başına eylemsiz kalabildiği yerde, fiilen ortaya konan bağlılık engellenmiş hareketi tersine çevirebilen bir dönüştürücü olarak okunabilir; rehberlik, yolları geçilebilir hale getirir. Odak ayetindeki tanınan yoldan yüz çevirme anlamı korunur. Çaba rehberliği mekanik olarak hak ettirmez ve çaba ile rehberlik kelimelerinin çözümlenmemiş diğer anlam alanları bu okumanın içine alınmaz.

</global_scope_prose>
