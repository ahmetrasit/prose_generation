# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:20**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_20/macro.discovery.json` and modify nothing
else, except for any required monitor lifecycle event command supplied by the
orchestrator. Remain available for a follow-up composition turn, but make this
artifact self-contained so a replacement agent can continue if the session is
lost.

## Evidence And Discovery

- The inline lane packet is the complete evidence boundary. Paths and pointers
  inside it are provenance, not permission to read other files.
- Check `focus_word_alignment` for unresolved analysis units. Their source
  readings remain available; qualify uncertain carriers rather than treating a
  missing join as evidence against a reading.
- Analysis refs and QAC refs have separate identities. Use each word candidate's
  `word_alignment` when supplied. Accepted overlaps can describe a whole
  expression and its component; shared morphemes do not make their semantic
  claims duplicates.
- Candidates are a review docket, not an accepted list, discovery limit, or
  quota. Decide every candidate exactly once. Independently inspect the full
  relevant surface, supports, connections, and available branches for
  uncandidate activations and surprise readings.
- Do not emit an exhaustive negative inventory for every available branch or
  connection. Negative accounting is required only for semantics attached to a
  supplied candidate.
- Availability is not activation. A branch reading requires a real carrier, an
  independent trigger, a mechanism, a changed reading, a reader payoff, and a
  boundary. Another word, root, image, grammatical relation, or act can be the
  trigger. Macro and global context may supply a trigger within that lane.
- `root_ids` on a word-analysis candidate are provenance normalization. They
  identify source/QAC root records but do not nominate or activate a branch.
  `root_branch_options` is the compact index of focus branches under those
  roots. Inspect it specifically for a branch that fits the candidate claim
  and meets an independent word/image/relation in the focus; nominate only a
  branch that actually passes that test.
- `accept` preserves the complete candidate. `narrow` preserves a bounded core
  and explicitly records every omitted candidate branch, branch facet, context
  ref, and semantic obligation. `represented` is only for an exact semantic
  duplicate carried by one named finding. `reject` names the failed edge and
  explicitly accounts for all attached obligations.
- For every retained finding, write `claim` and `mechanism` as the actual
  semantic relation. A statement that a supplied record or support merely
  identifies a contribution does not satisfy either field. Name the carrier,
  trigger, contact, and resulting change in meaning. If a branch otherwise
  passes the activation test, do not narrow the candidate or exclude the branch
  merely because the relation is peripheral, attributed, surprising,
  multi-step, or difficult to articulate. A form restriction justifies
  exclusion only when it is incompatible with the actual carrier; otherwise
  retain the relation with its restriction and evidence status explicit.
- Every item in a candidate's `semantic_obligations` is first-class. This
  includes candidate-specific word/channel evidence as well as HFT
  activation-trace roles, before/after changed readings, and containment; none
  may disappear behind a generic summary.
- A retained candidate context ref counts as landed only when it occurs in a
  branch activation's `carrier_refs` or `trigger_refs`. Merely listing it in
  `context_refs` does not count.
- Every candidate `branch_ref` must either land through an exact activated facet
  or be explicitly excluded. Separately account for any explicitly nominated
  `required_branch_facets`; do not expand this into all available facets. If a
  specialization/extension facet survives, at least one core facet of that
  branch must survive with it.
- `represented` means exact semantic duplication: it cannot exclude any of the
  represented candidate's branches, nominated facets, context, or obligations.
  A `narrow` decision must retain at least one semantic obligation when the
  candidate has any.
- Keep uncertainty and counter-readings visible without ranking them. Source
  trust controls qualification, not automatic acceptance or rejection.
- For a `legacy_unbound` HFT candidate, `registry: unresolved` means that no
  independent lexicon branch record is supplied; it does not by itself require
  exclusion. When its exact HFT trace names a supplied context ayah, word index,
  root, attributed role, and a contact returning to the focus, evaluate that
  trace as attributed contextual evidence. If it survives, retain it with
  `application_mode: attributed`, without inventing a branch gloss or facet.
  Exclude it when the coordinate or root does not agree with the supplied
  surface, the focus return is missing, or the inference exceeds the stated
  HFT role.

## Lane Boundary

- `micro`: local wording, syntax, morphology, sound, root pressure, and
  whole-ayah cross-root contacts.
- `macro`: what the declared pericope or host-surah context changes. Automatic
  basmala and explicitly added ayat are ordinary non-focus context members.
- `global`: a wider resonance only when a concrete wider trigger returns
  through a focus word, relation, or act and materially changes the reading.

## Lane-Specific Procedure

- Macro has no explicitly added external ayat. Assess the declared pericope or host-surah context, including any automatic host basmala, as ordinary non-focus context.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "88:20",
  "lane": "macro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["macro:stable-key"],
      "branch_exclusions": [
        {"branch_ref": "exact ref", "reason": "specific reason"}
      ],
      "facet_exclusions": [
        {"branch_ref": "exact ref", "facet_id": "F001 or null", "reason": "specific reason"}
      ],
      "context_exclusions": [
        {"context_ref": "S:A", "reason": "specific reason"}
      ],
      "semantic_obligation_exclusions": [
        {"obligation_ref": "exact ref", "reason": "specific reason"}
      ]
    }
  ],
  "findings": [
    {
      "finding_ref": "macro:stable-key",
      "origin_candidate_id": "accepted/narrowed candidate ID, or null",
      "represented_candidate_ids": ["exact duplicate candidate ID"],
      "title": "short descriptive title",
      "claim": "bounded interpretive claim",
      "mechanism": "how the cited evidence changes the reading",
      "reader_payoff": "what becomes newly perceptible",
      "containment": "limits, alternatives, and epistemic boundary",
      "epistemic": {
        "status": "grounded | qualified | exploratory",
        "source_trust": ["sorted exact trust labels from cited evidence"],
        "reason": "why this status fits"
      },
      "support_ids": ["exact support ID"],
      "branch_activations": [
        {
          "branch_ref": "exact branch ref",
          "facet_id": "exact facet ID, or null only when unresolved",
          "branch_gloss": "exact packet gloss, or null",
          "facet_statement": "exact packet statement, or null",
          "application_mode": "lexical | intrinsic_cross_root | contextual_resonance | analogical | attributed",
          "carrier_refs": ["exact focus/context occurrence ref"],
          "trigger_refs": ["exact independent grounding ref"],
          "focus_return_refs": ["exact focus word/QAC ref"],
          "carrier": "ordinary/root meaning carried by the cited form",
          "independent_trigger": "the separate activating evidence",
          "activation": "why carrier and trigger make contact",
          "resulting_reading": "the materially changed reading",
          "boundary": "what is not being claimed"
        }
      ],
      "connection_refs": ["exact connection ref"],
      "context_refs": ["S:A"],
      "semantic_obligation_refs": ["exact candidate obligation ref"]
    }
  ],
  "friction_notes": ["unresolved evidence-grounded limitation"]
}
```

Use empty arrays, not placeholders. Finding refs must be unique and begin with
`macro:`. Accepted/narrowed candidates own dedicated findings. A represented
candidate points to one exact-duplicate finding. Every cited ID/ref must exist
in the packet. Every branch activation must copy the exact gloss/facet source,
use a valid carrier occurrence, identify a distinct trigger, and return through
a focus-surface ref rather than the whole ayah. Include each non-focus ayah
used by a carrier or trigger in `context_refs`.

The texts below preserve the established v2/v3 linguistic standard. This V5
handoff controls the evidence boundary, role, response schema, and destination.

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

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Layer 2 uses
its evidence bundle; the active surah workflow uses only completed final ayah
editorials. They differ in source boundary and in what they synthesize.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

The active Layer 3 production contract is
[`_surah_commentary/v2/ORCHESTRATION.md`](_surah_commentary/v2/ORCHESTRATION.md). The
former combined Layer 3 + 2.5 overlay workflow is retired.

Status: active draft, updated 2026-09-11. The editorial-only surah contract
supersedes the legacy channel-first workflow. Mechanical validation and
semantic acceptance are separate; consult its implementation status.

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
The isolated Layer-2 writer cannot know that. The active surah workflow reads
only the completed final ayah editorials from one selected v5 analysis. It
synthesizes the readings present there, preserving their attribution, uncertainty,
and boundaries. Discovery artifacts, scope ledgers, invitations, separate
primary-floor data, and network/V11 sources do not enter this workflow. It writes
a separate surah reading and does not rewrite or overlay the ayah prose.

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
  primary instead of asking layer 3 to reconstruct that relation. Active V5
  appends a machine-readable landing map that maps each workflow-derived
  semantic ref to an exact prose passage and binds each finding to unique
  evidence and index passages. This is deterministic traceability, not a claim
  that software can judge semantic entailment. Wording may change while the
  structured semantics remain explicit. Evidence carries one compact
  workflow-derived provenance ledger per finding; the index carries only that
  ledger's source-record hash. Distinct apparatus landing spans may not
  overlap; the map is apparatus, not reader prose;
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

- **editorial snapshot** - the complete final editorial texts for one surah;
- **source-anchored outline** - the main cross-ayah movements supported by those
  texts, with each image's contribution and qualifications;
- **composition envelope** - prelude/postlude prose with exact anchors for
  each selected movement and member; semantic support requires review;
- **surah reading** — continuous reader prose emitted by the deterministic
  finalizer, not a summary or ayah catalogue;
- **publication evidence** — separate mapping from prose spans to packet
  evidence;
- **friction** — missing evidence and production limitations.

Contracts and schemas are under `_surah_commentary/v2/`.

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
remain outside reader prose. Active V5 records the exact carrier, trigger,
focus-return refs, branch facet, changed reading, and boundary in structured
discovery. Its planned scope-composition turn maps every resulting semantic ref
to exact prose passages. Canonical and editorial wording may change, but those
structured meanings must remain explicit and mapped.

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
while only exact semantic duplicates may share one. The second turn renders
the fixed finding set and maps its ordered semantic inventory to exact Turkish
passages. The canonical writer receives compact findings projections rather
than another copy of the full packets. Canonical and editorial indexes retain
the semantic passage map, one compact evidence ledger, and one index hash per
finding. The same live canonical session receives the unchanged V3 editorial
follow-up plus this preservation contract. There is no automated repair,
reconciliation, or semantic-adjudication cycle.

Layer 3 freezes only the completed final editorial prose for every numbered
ayah in one selected v5 analysis. The surah number and complete ayah count are
operator-supplied scope metadata. Missing or malformed editorial prose aborts;
no other semantic source is required or permitted. See
[`_surah_commentary/v2/ORCHESTRATION.md`](_surah_commentary/v2/ORCHESTRATION.md).

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

Status: updated 2026-09-11. New surah runs use only completed final ayah
editorials. The former channel-first source contract is historical; the active
runbook is `_surah_commentary/v2/ORCHESTRATION.md`.

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
discover or name a surah channel. The active surah workflow reads the final
editorial prose containing those local readings and writes a separate surah
reading; it does not patch channel disclosure back into the Layer-2 prose.

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

Layer 2 remains cold and states local surprise readings. The active surah
workflow freezes only the completed final editorial prose for every numbered
ayah in one selected v5 analysis. It derives an anchored outline, composes the
prelude/postlude, and edits the prose in the same composition-agent session.
Discovery artifacts, scope ledgers, invitations, separate primary-floor data,
and network/V11 sources are not inputs.

The outline selects the main cross-ayah movements supported by these editorials,
not an inventory compressing every finding. Significant distinct systems remain
separate; selection is not disambiguation. Each member image must have a clear
contribution, source anchor, and preserved qualification. Every ayah is accounted
for, including ayahs serving only as primary context.

### Layer 3 (per surah)

The prelude prepares concrete expectations; the postlude develops their
whole-surah payoff. All selected movements and members must land visibly, with
exact source and prose anchors. Mechanical validation checks coverage and
lineage; a semantic reviewer checks support, scope, and coherence. The workflow
does not rewrite Layer 2 or add overlays.

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
`_surah_commentary/v2/ORCHESTRATION.md`.

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
while designing additions to Layer 2. The active editorial-only workflow does
not write those additions; it records source-anchored movements and prose landings.

## 6. Recording

Per surah, the active workflow records:

- `surah-editorial-source-v1`: frozen final editorial texts and source hashes;
- `surah-editorial-outline-v1`: primary progression, main movements, member
  contributions and qualifications, and exact editorial anchors;
- `surah-editorial-composition-v1`: draft/editorial prelude and postlude with
  exact movement/member prose anchors;
- `surah-editorial-publication-v1`: approved publication lineage and evidence.

The active output schemas are `editorial-outline-v1.schema.json` and
`editorial-composition-v1.schema.json` under `_surah_commentary/v2/schemas/`.
Old channel/discovery schemas are historical. Follow
`_surah_commentary/v2/ORCHESTRATION.md`.

---

## 7. Open

- **Maturity remains archived.** The four-step scale and `emerging`-hint rule
  belong to the retired Layer 2.5 overlay experiment. They may be revisited
later, but the active editorial-only workflow does not depend on them.
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

<lane_packet_json>
{"branch_registry":[{"boundary":"Includes أبابيل for birds or groups arriving scattered, successive, or in separate bands","branch_kind":null,"branch_ref":"root_000006/B003","candidate_links":[{"candidate_id":"cand_c8214b1bab1fff3be362","lane":"macro"}],"focus_root_occurrences":[],"gloss":"successive or scattered groups","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الجماعات الأبابيل","image_en":"successive or scattered groups"}}],"root_ar":"ء ب ل","root_id":"root_000006","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الجماعات الأبابيل","image_en":"successive or scattered groups","scope_ar":"يدخل فيه أبابيل للطير أو الجماعات المتفرقة أو المتتابعة بعضا بعد بعض","scope_en":"Includes أبابيل for birds or groups arriving scattered, successive, or in separate bands"},"support_links":["sup_abb8d1ebf71563df9a7f"]},{"boundary":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_b7f3f963583589d7075d","lane":"macro"},{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"},{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"},{"candidate_id":"cand_044f714329608f7d322f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"yer ve yere bakan alt bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer küresi anlamını ve ona bağlı alt bölüm yönelimini birlikte özetleyen en kısa doğal karşılıktır.","boundary_detail":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_image_ar":"السفل المقابل للسماء","concept_gloss":"yer ve yere bakan alt bölüm","contextual_glosses":[{"applicability":"Üzerinde yaşanan ve göğün karşısında bulunan yer küresi söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin altı ile hayvan ayağının alt bölümüne bağlı kullanımları dışarıda bırakır.","preserves":"Üzerinde yaşanan aşağı yer ve göğe karşıt konum anlamını korur."},"facet_ids":["F001"],"text":"yeryüzü","usage_role":"contextual"}],"definition":"Göğün karşısında aşağıda bulunan, üzerinde yaşadığımız yer küresini belirtir. Belirli tamlamalarda bir şeyin yere bakan altını ve hayvanın tırnağını ya da ayağının alt bölümünü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}],"identity_rationale":"Kaynak ifadesi, göğün karşısında aşağıda bulunan ve üzerinde yaşanan yeri temel anlam olarak verir; nesnelerin yere bakan altı ile hayvan ayağının alt bölümü de buna bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yer, yeryüzü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, ülkeler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin yere bakan altı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hayvanın tırnağı veya ayaklarının altı"}],"lexicalization_note":"Tanım yalın yer anlamını kapsar; alt bölüm ve hayvan ayağı anlamlarını ise yalnız belirtilen tamlamalara bağlı yan yüzler olarak tutar.","neighbor_coverage_note":"Sağlanan bütün komşu kartları değerlendirildi; yer yüzeyiyle doğrudan karışabilecek en yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği aşağıda ve göğün karşısında bulunan yerdir; komşu dal ise yüzeyin genişliği ve düzlüğü ile serilmiş eşya fikrini öne çıkarır.","focus_only":"Göğün karşısındaki yer küresini ve tamlamalardaki alt bölüm anlamlarını kapsar.","gloss":"geniş düz yer veya yaygı","neighbor_only":"Geniş ve düz araziyi, ayrıca serilip yayılan eşyayı anlatır.","neighbor_ref":"root_000116/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da yayılmış bir yüzey olarak yer alanına dokunur."}],"source_phrase_ar":"كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)","source_summary":"Kaynaklar, anlamın merkezinde göğün karşısındaki aşağı yerin bulunduğunu; alt bölüm ve hayvan ayağı kullanımlarının bu mekansal çekirdeğe dayandığını birlikte gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","what_is_not_ar":"ليس الزكام ولا الرعدة ولا الدودة ولا البساط"},"support_links":["sup_653cc76172c0f339f13e","sup_68820d785ed9e8cc2d15","sup_73747b89a46171a56c68","sup_9ebc421e82623e106329"]},{"boundary":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B002","candidate_links":[{"candidate_id":"cand_a8b28d9c84356e01a920","lane":"macro"},{"candidate_id":"cand_0bfea26fc425c99ef016","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"yumuşak ve verimli toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oğlak yer bitkisini yer."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın toprak niteliğine dayanan çekirdeğini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_image_ar":"الأرض اللينة المنبتة","concept_gloss":"yumuşak ve verimli toprak","contextual_glosses":[{"applicability":"Bitkinin toprağa yerleşerek çoğalması anlatılan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın genel niteliğini ve oğlağın bu bitkiyle beslenmesi yüzünü dışarıda bırakır.","preserves":"Bitkinin toprağa yerleşmesi ve gelişerek çoğalması sürecini korur."},"facet_ids":["F002"],"text":"iyice köklenip çoğalmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda yumuşak, iyi, verimli ve bol bitki yetiştiren toprağı anlatır. Buna bağlı yapılarda bitkinin toprağa iyice yerleşip çoğalması veya biçilebilir olması, köklü fidan ve yer bitkisini yiyen oğlak; ayrı bir kaynak kullanımında ise semiz oğlak ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."},{"facet_id":"F002","role":"extension","statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."},{"facet_id":"F003","role":"associated_use","statement":"Oğlak yer bitkisini yer."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}],"identity_rationale":"Kaynak ifadesi yumuşak, iyi ve verimli toprağı merkez alır; bitkinin köklenip çoğalması veya biçilecek duruma gelmesi ile oğlağın bu ottan yiyip semirmesi buna bağlı gelişmelerdir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yumuşak, verimli ve bol bitkili toprak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşak tabanlı geniş çayırlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak verimlileşti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprakta kök salmış fidan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"oğlak yer bitkisini yedi veya onunla semirdi"}],"lexicalization_note":"Tanım, nitelikli toprak anlamını yalnız kanıtlanan tamlamalara; bitki, fidan ve oğlakla ilgili anlamları da kendi kanıtlanmış yapılarına bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; verimli toprak çekirdeğine en yakın olup kapsam farkı taşıyan kart seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yumuşaklık ve iyi bitkilenmeyle birlikte belirli bitki ve oğlak yapılarını taşır; komşu dal kolaylık ve hızlı yetişme niteliğine uzanır.","focus_only":"Bitkinin yerleşmesi, biçilebilir olması ve oğlağın bitkiyle beslenmesi gibi bağlı kullanımları vardır.","gloss":"kolay işlenen verimli toprak","neighbor_only":"Kolay işlenen yer ve bitkinin hızlı yetişmesi özelliklerini daha genel biçimde kapsar.","neighbor_ref":"root_000058/B004","relation_type":"near_synonym","shared_zone":"İki dal da verimli, iyi bitki yetiştiren toprağı anlatır."}],"source_phrase_ar":"أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)","source_summary":"Birleşik kanıt, verimli ve yumuşak toprağı; bu toprakta gelişen bitkiyi ve bitkiden yararlanan oğlağı aynı üretkenlik ilişkisi içinde toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض الأريضة والروضة الأريضة؛ الأرض الزاكية الحسنة النبت؛ النبات المتأرض إذا تمكن في الأرض وكثر أو أمكن جزه؛ الجدي الأريض إذا تناول نبت الأرض أو سمن","what_is_not_ar":"ليس أسفل الشيء مطلقا ولا الرعدة ولا الزكام"},"support_links":["sup_30996586adcb86125b8f","sup_9328151575867451fa13"]},{"boundary":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_kind":"collocation","branch_ref":"root_000025/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"iyiliğe yatkın ve layık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyiliğe yatkın ve ona layıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişi hakkında kurulan belirtilmiş yapıda dalın temel niteliğini karşılar.","boundary_detail":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_image_ar":"الخليق بالخير كالأرض الأريضة","concept_gloss":"iyiliğe yatkın ve layık","contextual_glosses":[{"applicability":"Bir topluluk içinden belirli işi yapmaya en uygun kişi seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğe yatkın ve alçak gönüllü kişi niteliğini dışarıda bırakır.","preserves":"Belirli eyleme başkalarından daha uygun ve layık olma karşılaştırmasını korur."},"facet_ids":["F002"],"text":"bunu yapmaya en uygunları","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişinin iyiliğe yatkın ve ona layık olmasını anlatır; bir kaynak bu niteliği alçak gönüllülükle birlikte verir. Karşılaştırmalı kullanımda ise bir işi yapmaya başkalarından daha uygun olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyiliğe yatkın ve ona layıktır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}],"identity_rationale":"Kaynak ifadesi belirli yapılarda bir kişinin iyiliğe yatkın, ona layık ve alçak gönüllü oluşunu; karşılaştırmalı yapıda ise bir işi yapmaya en uygun kişi sayılmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iyiliğe yatkın, layık ve alçak gönüllü kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu yapmaya en uygunları"}],"lexicalization_note":"Tanım bütünüyle belirtilen kişi ve eylem tamlamalarına bağlıdır; yalın biçime bağımsız bir uygunluk anlamı yüklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel layıklık alanıyla karışma olasılığı en yüksek olan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iyilik alanına ve iki belirli yapıya bağlıdır; komşu dalın uygunluk ve hazır oluş kapsamı daha geneldir.","focus_only":"İyiliğe yatkınlıkla birlikte alçak gönüllülük çağrışımı ve belirli kalıplara bağlılık taşır.","gloss":"bir şeye layık ve hazır","neighbor_only":"Herhangi bir şeye hazır, uygun veya layık olmayı daha geniş biçimde anlatır.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ile uygun görüldüğü nitelik veya eylem arasındaki yatkınlık ilişkisini bildirir."}],"source_phrase_ar":"رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)","source_summary":"Kaynaklar, iyiliğe yatkınlık ve layıklık ile belirli bir eyleme en uygun olma yargısını yapı bağımlı tek bir uygunluk alanında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الرجل الأريض للخير؛ آرض القوم أن يفعل الشيء أي أخلقهم به","what_is_not_ar":"ليس الأرض الحسية ولا الزكام ولا الرعدة"},"support_links":[]},{"boundary":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_kind":"non_bare","branch_ref":"root_000025/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan sabit adlandırmanın kişi anlamını doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_image_ar":"ابن الأرض الغريب","concept_gloss":"yabancı kimse","definition":"Belirli bir sabit adlandırmada, bulunduğu çevreye dışarıdan gelen veya oraya ait olmayan yabancı kimseyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}],"identity_rationale":"Tek kaynak ifadesi, sabit bir adlandırmanın doğrudan yabancı kimse anlamına geldiğini belirtir; yer sakini veya soy bağına ilişkin daha ayrıntılı bir koşul kurmaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yabancı kimse"}],"lexicalization_note":"Tanım yalnız kanıtlanan sabit söz birimine bağlanır; parçaların yalın anlamlarından yeni bir kişi sınıfı türetilmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel yabancı anlamına en yakın, fakat topluluk koşuluyla ayrılan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kanıtı yalnız yabancı olmayı söyler; komşu dal yabancının başka bir topluluk içinde bulunması koşulunu açıkça taşır.","focus_only":"Yabancılığı herhangi bir ek topluluk koşulu vermeden sabit bir adlandırmayla bildirir.","gloss":"başka bir topluluğa girmiş yabancı","neighbor_only":"Kişinin kendisinden olmayan bir topluluğun içine girmiş bulunmasını özellikle belirtir.","neighbor_ref":"root_000009/B006","relation_type":"near_synonym","shared_zone":"İki dal da bulunduğu insan çevresine aslen ait olmayan kişiyi anlatır."}],"source_phrase_ar":"فلان ابن أرض أي غريب (maqayis)","source_summary":"Tek kanıt, söz biriminin yabancı kimseyi belirten kısıtlı ve kalıplaşmış bir adlandırma olduğunu gösterir.","sources":["MQ"],"what_is_ar":"ابن أرض إذا أريد الغريب","what_is_not_ar":"ليس ساكن الأرض مطلقا ولا الأرض التي نحن عليها"},"support_links":[]},{"boundary":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_kind":"bare","branch_ref":"root_000025/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"kalın yün veya kıl yaygı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin türünü, belirleyici kalınlığını ve iki olası malzemesini birlikte karşılar.","boundary_detail":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_image_ar":"الإراض البساط الضخم","concept_gloss":"kalın yün veya kıl yaygı","definition":"Yünden veya hayvan kılından yapılmış kalın ve büyükçe bir yaygıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}],"identity_rationale":"Kaynak ifadesi nesneyi kalın, büyükçe bir yaygı olarak tanımlar ve malzemesini yün ya da hayvan kılıyla sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın yün veya kıl yaygı"}],"lexicalization_note":"Tanım yalın adın kanıtlanan nesne anlamıyla sınırlıdır ve komşu döşeme türlerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Sağlanan kartların tümü değerlendirildi; nesne türü bakımından en yakın fakat kapsamı daha geniş döşeme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal malzeme ve kalınlıkla tanımlanan belirli bir yaygıdır; komşu dal işlevi bakımından daha geniş bir döşeme sınıfıdır.","focus_only":"Yaygının kalın ve özellikle yün ya da hayvan kılından yapılmış olmasını gerektirir.","gloss":"döşek veya alta serilen örtü","neighbor_only":"Döşek, yatak örtüsü ve genel olarak alta serilen nesneleri kapsar.","neighbor_ref":"root_001397/B007","relation_type":"same_field","shared_zone":"Her iki dal da zemine ya da yatma yerine serilen ev eşyalarını adlandırır."}],"source_phrase_ar":"الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)","source_summary":"Kaynaklar nesnenin yaygı oluşunda, kalınlığında ve yün ya da hayvan kılından yapılmasında birleşir.","sources":["MQ","SI"],"what_is_ar":"الإراض بالكسر؛ بساط ضخم من وبر أو صوف","what_is_not_ar":"ليس الأرض ولا الأرضة ولا الأريضة"},"support_links":[]},{"boundary":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_kind":"bare","branch_ref":"root_000025/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"yere çökercesine ağırlaşıp oyalanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yerden ayrılmayarak yere bağlı kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yere bağlılık, ağırlaşma ve gecikme bileşenlerini tek bir eylem karşılığında toplar.","boundary_detail":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_image_ar":"لزوم الأرض والتثاقل إليها","concept_gloss":"yere çökercesine ağırlaşıp oyalanmak","contextual_glosses":[{"applicability":"Kişinin doğrudan yere bağlı kalması öne çıktığında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere doğru ağırlaşma ile oyalanıp gecikme görünüşlerini dışarıda bırakır.","preserves":"Yere bağlı kalma ve bulunduğu noktadan ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"yerinden ayrılmamak","usage_role":"contextual"}],"definition":"Kişinin yere bağlı kalmasını veya yere çökercesine ağırlaşmasını ve bu yüzden bir süre oyalanıp gecikmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yerden ayrılmayarak yere bağlı kalır."},{"facet_id":"F002","role":"extension","statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi kişinin yere bağlı kalmasını, yere doğru ağırlaşmasını ve bunun sonucu oyalanıp gecikmesini aynı hareket durumu içinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yere bağlı kalmak, ağırlaşıp oyalanmak"}],"lexicalization_note":"Tanım yalın eylem dalının yere bağlı kalma, ağırlaşma ve gecikme bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yere bağlı kalma çekirdeğini en doğrudan paylaşan ve kapsam farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin yere doğru ağırlaşıp gecikmesini anlatır; komşu dal farklı canlı ve nesnelerde yere yapışma ya da sabit kalma alanına daha geniş yayılır.","focus_only":"İnsan için yere doğru ağırlaşma ve bununla birlikte oyalanma anlamını taşır.","gloss":"yere yapışıp yerinde kalmak","neighbor_only":"İnsan dışında kuş ve yırtıcıları, ayrıca yuva ve yerinde ağır duran nesne örneklerini de kapsar.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dalda da yere yakın durma ve bulunulan yerden ayrılmama durumu vardır."}],"source_phrase_ar":"تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)","source_summary":"Kanıt, yere bağlı kalmayı çekirdek alır ve yere doğru ağırlaşma ile oyalanmayı bu durumun görünüşleri olarak birleştirir.","sources":["MQ","SI"],"what_is_ar":"تأرض فلان إذا لزم الأرض؛ التأرض بمعنى التثاقل والتلبث إلى الأرض","what_is_not_ar":"ليس التصدي والتعرض للغير ولا النبات المتأرض"},"support_links":[]},{"boundary":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_kind":"bare","branch_ref":"root_000025/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"karşısına çıkıp kendini ortaya koymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yönelmiş karşı duruşu ve görünür biçimde ortaya çıkmayı birlikte karşılar.","boundary_detail":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_image_ar":"التعرض والتصدي","concept_gloss":"karşısına çıkıp kendini ortaya koymak","definition":"Birine doğru yönelip onun karşısına çıkmayı, kendini ortaya koyarak ona karşı durmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}],"identity_rationale":"Tek kaynak ifadesi eylemi, birine doğru çıkıp onun karşısında kendini ortaya koymak ve ona karşı durmak biçiminde açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkıp kendini ortaya koymak"}],"lexicalization_note":"Tanım yalın eylem dalını, bir hedefe yönelme ve karşısına çıkma koşullarıyla sınırlar.","neighbor_coverage_note":"Tüm komşular değerlendirildi; yönelme ve karşıya çıkma çekirdeğini en yakından paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşıya çıkışı öne çıkarır; komşu dal bakma, gözetme ve genel yüzünü dönme kullanımlarını da kapsar.","focus_only":"Bir kişiye doğru gelerek onun karşısında kendini ortaya koyma hareketini bildirir.","gloss":"bir şeye yönelip karşısına çıkmak","neighbor_only":"Bir şeye bakmak üzere yükselme, onu gözetme veya yalnızca yüzünü ona çevirme kapsamına uzanır.","neighbor_ref":"root_000853/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe yönelme ve onun karşısında konum alma anlamını taşır."}],"source_phrase_ar":"جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)","source_summary":"Tek kanıt, eylemin hedefe yönelmiş bir karşıya çıkma ve kendini ortaya koyma hareketi olduğunu gösterir.","sources":["SI"],"what_is_ar":"جاء فلان يتأرض إلى غيره أي يتصدى ويتعرض له","what_is_not_ar":"ليس التثاقل إلى الأرض ولا لزومها"},"support_links":[]},{"boundary":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_kind":"bare","branch_ref":"root_000025/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"titreme veya ürperme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedenindeki kısa ya da süren sarsıntı durumunu doğrudan karşılar.","boundary_detail":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_image_ar":"الأَرْض الرعدة","concept_gloss":"titreme veya ürperme","definition":"Bir insanın bedeninde beliren titreme, sarsılma veya ürperme durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı insanda görülen titreme, sarsılma veya ürperme olarak açıkça tanımlar ve yer ya da hastalık anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"insanı tutan titreme veya ürperme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"titreme ve sarsılma"}],"lexicalization_note":"Tanım yalın biçimlerin insandaki titreme ve ürperme anlamıyla sınırlıdır; komşu hastalık nedenleri eklenmez.","neighbor_coverage_note":"Sağlanan bütün kartlar incelendi; genel titreme çekirdeğine en yakın ve kapsam farkı belirgin olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın bir insan titremesidir; komşu dal nedeni ve öznesi bakımından daha geniştir, ayrıca korkaklık ve gevşeklik nitelemelerine uzanır.","focus_only":"İnsan bedenindeki titreme durumunu herhangi bir özel neden belirtmeden adlandırır.","gloss":"korku veya hastalıktan sarsılma","neighbor_only":"Korku, hastalık veya gevşeklik nedeniyle insan ya da başka bir şeyin sarsılmasını ve kişilik nitelemelerini kapsar.","neighbor_ref":"root_000573/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insan bedenindeki titreme ve sarsılma alanında örtüşür."}],"source_phrase_ar":"الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)","source_summary":"Kaynaklar bu adın insanda görülen titreme ve ürperme durumunu bildirdiğinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الرعدة أو النفضة في الإنسان","what_is_not_ar":"ليس الأرض التي تقابل السماء ولا الزكام"},"support_links":[]},{"boundary":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_kind":"bare","branch_ref":"root_000025/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"soğuk algınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soğuk algınlığı durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hastalık çekirdeğini Türkçede en doğal ve ayırt edici biçimde karşılar.","boundary_detail":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_image_ar":"الأَرْض الزكام","concept_gloss":"soğuk algınlığı","contextual_glosses":[{"applicability":"Hastalığın kendisi değil, bu hastalığa tutulmuş kişi nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık adını ve birini hastalığa uğratma eylemini bağımsız olarak karşılamaz.","preserves":"Soğuk algınlığı ile kişi arasındaki etkilenme ilişkisini korur."},"facet_ids":["F002"],"text":"soğuk algınlığına yakalanmış","usage_role":"contextual"}],"definition":"Soğuk algınlığı hastalığını, bu hastalığa yakalanmış kişiyi ve birini bu hastalığa uğratma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soğuk algınlığı durumudur."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}],"identity_rationale":"Kaynak ifadesi hastalığı soğuk algınlığı olarak, etkilenen kişiyi bu hastalığa yakalanmış olarak ve ettirgen biçimi hastalığa uğratmak olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk algınlığı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına yakalanmış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına uğratmak"}],"lexicalization_note":"Tanım yalın hastalık adını ve aynı dalda kanıtlanan hasta kişi ile hastalığa uğratma türevlerini korur.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; aynı hastalık ve hasta kişi alanını en doğrudan paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın türetim dizisinde hastalığa uğratma da vardır; komşu dalın kanıtı ise bir kaynakta daha genel hastalık yorumu içerir.","focus_only":"Hastalık adı, hastaya ilişkin niteleme ve hastalığa uğratma eylemini birlikte kapsar.","gloss":"soğuk algınlığı ve hasta olma","neighbor_only":"Soğuk algınlığı yanında daha genel bir hastalık alanına açılan ayrı bir kaynak yorumunu da taşır.","neighbor_ref":"root_000916/B003","relation_type":"near_synonym","shared_zone":"Her iki dal soğuk algınlığını ve bu hastalığa yakalanmış kişiyi ifade eder."}],"source_phrase_ar":"الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)","source_summary":"Kaynaklar hastalık adı ile hasta kişi nitelemesinde birleşir; kanıt ayrıca hastalığa uğratma eylemini aynı türetim alanında gösterir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الزكمة أو الزكام؛ مأروض لمن أصابه الزكام","what_is_not_ar":"ليس الرعدة ولا الأرض الحسية"},"support_links":[]},{"boundary":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"odun yiyen küçük canlı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük canlı odunla beslenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıyı kanıtlanan boyutu ve onu ayırt eden beslenme davranışıyla kısa ve doğal biçimde karşılar.","boundary_detail":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_image_ar":"الأَرَضَة آكلة الخشب","concept_gloss":"odun yiyen küçük canlı","contextual_glosses":[{"applicability":"Bir odunun bu canlı tarafından yenerek zarar görmüş olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlının beyaz ve karıncaya benzer oluşunu bağımsız bir tanım olarak vermez.","preserves":"Odunun canlı tarafından yenmiş ve zarar görmüş olma sonucunu korur."},"facet_ids":["F002"],"text":"odun yiyen küçük canlı tarafından yenmiş","usage_role":"contextual"}],"definition":"Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük canlı odunla beslenir."},{"facet_id":"F002","role":"associated_use","statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}],"identity_rationale":"Kaynak ifadesi beyaz, karıncaya benzeyen ve odun yiyen küçük canlıyı tanımlar; ayrıca bu canlının odunu yiyerek onu zarar görmüş hale getirmesini verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"odun yiyen küçük canlı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"odunu bu canlı yedi ve zarar verdi"}],"lexicalization_note":"Tanım canlı adını yalın çekirdek olarak verir ve odunun yenmesini yalnız kanıtlanan tamlamaya bağlı sonuç yüzü olarak ayırır.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; odun yiyen canlı çekirdeğine en yakın fakat canlı ve nesne kapsamı farklı olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal odun yiyen küçük canlı ve onun oduna etkisidir; komşu dal ağaç, yaprak ve gövde üzerinde beslenen başka bir canlıya özgüdür.","focus_only":"Odun yiyen küçük canlıyı ve bu canlının yediği odunun sonucunu belirtir.","gloss":"ağacı delen ve yiyen küçük canlı","neighbor_only":"Özellikle ağaçta delik açan, yaprak veya odun yiyen başka bir küçük canlıyı ve ağacın uğradığı durumu kapsar.","neighbor_ref":"root_000699/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da odunsu bitki maddesini yiyerek zarar veren küçük canlıları anlatır."}],"source_phrase_ar":"الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)","source_summary":"Kaynaklar odun yiyen küçük canlı ile onun odunda oluşturduğu yenme ve zarar görme sonucunu aynı anlam alanında birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الأَرَضَة؛ دويبة تأكل الخشب؛ أرضت الخشبة فهي مأروضة إذا أكلتها الأرضة","what_is_not_ar":"ليس الأرض ولا الأرض الأريضة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_kind":"collocation","branch_ref":"root_000025/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"yaranın irinlenip bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yara bağlamında irin toplama ile ortaya çıkan bozulma sürecini eksiksiz karşılar.","boundary_detail":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_image_ar":"فساد القرحة بالمدة","concept_gloss":"yaranın irinlenip bozulması","definition":"Bir yaranın irin toplaması, kabarıp su toplaması ve bu irinlenme yüzünden bozulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}],"identity_rationale":"Tek kaynak ifadesi, yaranın irin toplamasıyla kabarıp bozulmasını bir süreç olarak verir; yalnız irin maddesini veya genel deri şişliğini adlandırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yara irinlenip kabardı ve bozuldu"}],"lexicalization_note":"Tanım yalnız yara öznesiyle kurulan kanıtlanmış tamlamaya bağlıdır; yalın biçime genel bozulma anlamı verilmez.","neighbor_coverage_note":"Bütün komşular incelendi; irin birikmesi çekirdeğini en yakından paylaşan ve sonuç bakımından ayrılan kart yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal irin birikimini yaranın kabarıp bozulmasına bağlar; komşu dal yalnız irin toplanması ya da dışarı çıkmasıyla yetinebilir.","focus_only":"Yaranın irinlenmeyle kabarıp bozulması sürecini zorunlu olarak içerir.","gloss":"yarada irin toplanması","neighbor_only":"İrinin yarada toplanmasını veya yaradan çıkmasını, bozulma sonucu aramadan kapsar.","neighbor_ref":"root_001664/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da yaranın içinde irin birikmesi durumunu anlatır."}],"source_phrase_ar":"أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)","source_summary":"Tek kanıt, yara içindeki irinlenme ile kabarma ve bozulmayı birbirine bağlı tek bir hastalık süreci olarak gösterir.","sources":["SI"],"what_is_ar":"أرضت القرحة إذا مجلت وفسدت بالمدة","what_is_not_ar":"ليس الزكام ولا الأرضة ولا الرعدة"},"support_links":[]},{"boundary":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_000025/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","surface_ar":"أَرْضِ"}],"gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Neden yorumunu, akıl durumunu ve belirleyici istemsiz beden hareketini birlikte açıklar.","boundary_detail":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_image_ar":"المأروض المخبول من أهل الأرض","concept_gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","contextual_glosses":[{"applicability":"Kişinin gözlenebilir beden hareketi ön plana çıkarıldığında açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl bozukluğunu ve durumun görünmez varlıkların etkisine bağlanmasını dışarıda bırakır.","preserves":"Baş ve gövdenin bilinçli amaç olmadan hareket etmesi belirtisini korur."},"facet_ids":["F002"],"text":"başıyla gövdesini istemsizce sarsan kişi","usage_role":"explanatory"}],"definition":"Yerle ilişkilendirilen görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğudur; etkilenen kişi başını ve gövdesini isteği dışında hareket ettirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."},{"facet_id":"F002","role":"specialization","statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}],"identity_rationale":"Kaynak ifadesi, görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğunu; kişinin başını ve gövdesini istemeden hareket ettirmesiyle birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi"}],"lexicalization_note":"Tanım yalın kişi nitelemesinin doğaüstü açıklama, akıl bozukluğu ve istemsiz beden hareketi bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğaüstü etkiye bağlanan akıl bozukluğu çekirdeğini en doğrudan paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kaynak ilişkilendirmesi ve istemsiz baş-gövde hareketi gerektirir; komşu dal daha genel bir doğaüstü dokunuş açıklamasıdır.","focus_only":"Yerle ilişkilendirilen görünmez varlıklar açıklamasını ve istemsiz baş-gövde hareketini birlikte taşır.","gloss":"doğaüstü dokunuşa bağlanan akıl karışıklığı","neighbor_only":"Doğaüstü bir dokunuşla açıklanan akıl karışıklığını beden hareketi koşulu olmadan daha genel verir.","neighbor_ref":"root_001423/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da akıl bozukluğunu görünmez bir varlığın etkisiyle açıklayan geleneksel anlayışta buluşur."}],"source_phrase_ar":"المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)","source_summary":"Tek kanıt, doğaüstü varlıklara bağlanan akıl karışıklığını ve istemsiz baş-gövde hareketini aynı kişi durumunun ayrılmaz parçaları olarak verir.","sources":["SI"],"what_is_ar":"المأروض الذي به خبل من الجن وأهل الأرض ويحرك رأسه وجسده على غير عمد","what_is_not_ar":"ليس المزكوم المأروض ولا الخشبة المأروضة"},"support_links":[]},{"boundary":"İnsan bedeninin yere serilmesi, özel taşıyıcılar, kaplar, kullanım yerleri ve bitki adları bu dalın genel yüzey ve düzleştirme anlamına katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000703/B001","candidate_links":[{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"},{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"},{"candidate_id":"cand_044f714329608f7d322f","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"düz üst yüzey ve yayarak düzleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin ya da yapının düz, yayvan ve üstte bulunan yüzüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi yayma, uzatma ve düzleyerek yüzey görünümüne getirme işlemidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Düzleştirme; yer, mezar ve kap içindeki yemek üzerinde uygulanabilir, ayrıca çok basık bir burun biçimini niteleyebilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyin kendiliğinden yayılıp uzaması ve hem boyuna hem enine genişlemesidir."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağımsız yüzey adını ve bir şeyi yayıp düz duruma getiren temel işlemi birlikte özetler.","boundary_detail":"İnsan bedeninin yere serilmesi, özel taşıyıcılar, kaplar, kullanım yerleri ve bitki adları bu dalın genel yüzey ve düzleştirme anlamına katılmaz.","branch_image_ar":"سطح مستو ممتد","concept_gloss":"düz üst yüzey ve yayarak düzleştirme","contextual_glosses":[{"applicability":"Bir nesnenin ya da yapının düz ve yayvan üst bölümü kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstte bulunma, düzlük ve yüzey olma özelliklerini korur."},"facet_ids":["F001"],"text":"üstteki düz yüzey","usage_role":"contextual"},{"applicability":"Bir yerin, nesnenin ya da kap içindeki yemeğin yayılıp düz duruma getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yayma işlemini ve bunun düz bir durum oluşturmasını korur."},"facet_ids":["F002","F003"],"text":"yayıp düzleştirmek","usage_role":"contextual"},{"applicability":"Bir şeyin boyuna ve enine açılarak daha geniş bir alan kapladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kendiliğinden yayılma, uzama ve genişleme sonucunu korur."},"facet_ids":["F004"],"text":"yayılıp genişlemek","usage_role":"contextual"}],"definition":"Bir nesnenin, özellikle bir yapının, düz ve yayvan üst yüzüdür; ayrıca bir şeyi yayıp uzatarak düz bir duruma getirme işlemini anlatır. Aynı biçimsel çekirdek, bir şeyin uzunlamasına ve enine yayılıp genişlemesine de uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin ya da yapının düz, yayvan ve üstte bulunan yüzüdür."},{"facet_id":"F002","role":"core","statement":"Bir şeyi yayma, uzatma ve düzleyerek yüzey görünümüne getirme işlemidir."},{"facet_id":"F003","role":"specialization","statement":"Düzleştirme; yer, mezar ve kap içindeki yemek üzerinde uygulanabilir, ayrıca çok basık bir burun biçimini niteleyebilir."},{"facet_id":"F004","role":"extension","statement":"Bir şeyin kendiliğinden yayılıp uzaması ve hem boyuna hem enine genişlemesidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin düz ve yayvan üst yüzünü, bir şeyi yayıp uzatarak düzleştirme işlemini ve aynı biçimsel çekirdeğin uzunlamasına ve enine genişleme sonucunu birlikte destekler. Verilen çerçeve bu nominal, geçişli ve kendiliğinden gerçekleşen kullanımları doğru biçimde bir arada tutmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"üstteki düz yüzey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi yayıp uzatarak düzleştirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"düzleştirme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"çok basık burun"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yayılıp uzamak ve genişlemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yemeği kabın içine yayıp düzlemek"}],"lexicalization_note":"Tanım, bağımsız üst yüzey adını; yayma ve düzleştirme eylemlerinden, özel söz öbeklerinden ve yayılıp genişleme biçiminden ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca genel yayma, yayvanlık ve düz yerle doğrudan sınır karışıklığı yaratabilecek üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yayma ve genişletme eylemine odaklanırken bu dal, düz üst yüzeyi ve yayma sonucunda düz bir yüzey oluşturmayı kendi sınırına alır.","focus_only":"Düz üst yüzeyi ve bir şeyi belirgin biçimde düz bir yüzeye dönüştürme sonucunu da kapsar.","gloss":"yayma ve uzatma","neighbor_only":"Yayma, uzatma ve genişletmeyi üst yüzey ya da düzleştirme sonucu gerektirmeden daha genel anlatır.","neighbor_ref":"root_000928/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yayılması, uzaması ve kapladığı alanın genişlemesi üzerinde buluşur."},{"boundary_match":"partial","distinction":"Bu dal üstteki düz yüzeyi ve düzleştirme işlemini anlatır; komşu dal ise yüzeyin konumundan ve yapılan işlemden bağımsız daha genel bir genişlik alanına sahiptir.","focus_only":"Üst yüzey olma ve bir şeyi işlemle düz duruma getirme özellikleri belirleyicidir.","gloss":"yayvanlık ve genişlik","neighbor_only":"Genel genişlik ile yer yüzü ve yüz derisi gibi başka yüzey türlerini de içerir.","neighbor_ref":"root_000845/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeyin yayvanlaşması ve geniş bir yüzey kaplaması bulunur."},{"boundary_match":"partial","distinction":"Komşu dal belirli bir düz yer adıdır; bu dal ise düz üst yüzey kavramını ve böyle bir yüzey oluşturma işlemini daha geniş biçimde kapsar.","focus_only":"Nesnelerin üst yüzeyini ve düzleştirme eylemini genel olarak kapsar.","gloss":"düz yer","neighbor_only":"Yalnızca düz bir taban ya da düz yer türünü adlandırır.","neighbor_ref":"root_001204/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da düz ve yatay görünen bir yer yüzeyini anlatabilir."}],"source_phrase_ar":"أصل يدل على بسط الشيء ومده (maqayis)؛ السطح البسط (ayn)؛ سطح كل شيء أعلاه (jamhara)؛ السطح من كل شيء أعلاه؛ سطح الله الأرض سطحا بسطها؛ تسطيح القبر خلاف تسنيمه؛ أنف مسطح منبسط جدا؛ اسلنطح الشيء طال وعرض (sihah)؛ السطح ظهر البيت إذا كان مستويا (tahdhib)؛ السطح أعلى البيت؛ سطحت المكان جعلته في التسوية كسطح؛ سطحت الثريدة في القصعة بسطتها (mufradat)؛ اسلنطح الشيء إذا انبسط وعرض وإنما أصله سطح وزيدت فيه اللام والنون (maqayis-v)","source_summary":"Ortak kanıt, düz üst yüzey ile yayma, uzatma ve düzleştirme işlemlerini aynı anlam çekirdeğinde birleştirir; özel örnekler bu çekirdeğin uygulamaları, yayılıp genişleme ise sonuç odaklı uzantısıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"السطح أعلى الشيء أو ظهر البيت إذا استوى، وبسط الشيء ومده وتسويته حتى يصير كالسطح، ومنه تسطيح الأرض والمكان والقبر والثريدة، واسلنطح الشيء إذا طال وعرض","what_is_not_ar":"طرح الإنسان على قفاه؛ عمود الخباء؛ الوعاء المفلطح؛ موضع تجفيف التمر؛ النبات"},"support_links":["sup_653cc76172c0f339f13e","sup_68820d785ed9e8cc2d15","sup_9ebc421e82623e106329"]},{"boundary":"Buradaki çekirdek insan bedeninin yere yatırılması ya da sırtüstü hareketsiz uzanmasıdır; genel yüzey düzlüğü ve nesne düzleştirme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000703/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"yere serme veya sırtüstü hareketsiz yatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi yere yatırıp boylu boyunca uzanır duruma getirmektir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin sırtüstü uzanması ve bu durumda hareketsiz kalmasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yere serilmiş ya da öldürülmüş kişi bu duruşun sonucu üzerinden adlandırılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bedensel engel nedeniyle sürekli yere yayılmış durumda bulunan bir kahinin adı bu duruşla ilişkilendirilir."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi yere yatıran eylem ile kişinin sırtüstü uzanıp kımıldamaması olan iki temel kullanımı birlikte karşılar.","boundary_detail":"Buradaki çekirdek insan bedeninin yere yatırılması ya da sırtüstü hareketsiz uzanmasıdır; genel yüzey düzlüğü ve nesne düzleştirme bu dala girmez.","branch_image_ar":"جسم مطروح ممتد على الأرض","concept_gloss":"yere serme veya sırtüstü hareketsiz yatma","contextual_glosses":[{"applicability":"Bir kişiyi, özellikle çatışma bağlamında, yere yatırıp uzanır duruma getiren geçişli kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kişiye yönelen yere yatırma ve uzatma eylemini korur."},"facet_ids":["F001"],"text":"yere sermek","usage_role":"contextual"},{"applicability":"Kişinin sırtı üzerinde boylu boyunca yatıp hareketsiz kaldığı durum için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sırtüstü uzanma biçimini ve hareketsiz kalma sonucunu korur."},"facet_ids":["F002"],"text":"sırtüstü uzanıp kımıldamamak","usage_role":"contextual"},{"applicability":"Yere yatırılmış ya da öldürülüp yere serilmiş kişiyi sonuç durumu üzerinden adlandırır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin yere serilmiş durumunu ve sonuç odaklı adlandırmayı korur."},"facet_ids":["F003"],"text":"yere serilmiş kişi","usage_role":"contextual"}],"definition":"Bir kişiyi yere yatırma ya da kişinin sırtüstü uzanıp hareketsiz kalmasıdır. Yere serilmiş ölü için kullanımı ve bedensel engel nedeniyle sürekli böyle yatan bir kahine verilen ad, bu beden duruşuna bağlı özel uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi yere yatırıp boylu boyunca uzanır duruma getirmektir."},{"facet_id":"F002","role":"core","statement":"Bir kişinin sırtüstü uzanması ve bu durumda hareketsiz kalmasıdır."},{"facet_id":"F003","role":"specialization","statement":"Yere serilmiş ya da öldürülmüş kişi bu duruşun sonucu üzerinden adlandırılır."},{"facet_id":"F004","role":"associated_use","statement":"Bedensel engel nedeniyle sürekli yere yayılmış durumda bulunan bir kahinin adı bu duruşla ilişkilendirilir."}],"identity_rationale":"Kaynak ifadesi hem bir kişiyi yere yatıran geçişli eylemi hem de kişinin sırtüstü uzanıp hareketsiz kalmasını açıkça verir. Yere serilmiş ölü kullanımı ve bedensel engel nedeniyle sürekli bu durumda bulunan bir kahinin adlandırılması da aynı beden duruşuna bağlı özel uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onları yere serdiler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yere serilmiş kişi veya ölü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"adam sırtüstü uzanıp hareketsiz kaldı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bedensel engeli yüzünden yere yayılmış bir kahine verilen ad"}],"lexicalization_note":"Tanım, yere serilmiş kişi adını; birini yere yatıran söz öbeğinden, sırtüstü uzanma eyleminden ve bu duruşa bağlı adlandırmadan ayrı gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; insan bedeninin yerde uzanmasıyla gerçek anlam örtüşmesi kuran iki komşu ve genel düzleşme dalı sınır açıklığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal insanın sırtüstü hareketsiz kalmasına ve yere yatırılmasına odaklanır; komşu dalın duruş, canlı türü ve yere yapışma bakımından daha geniş bir alanı vardır.","focus_only":"Özellikle insanın sırtüstü ve hareketsiz yatışını, birini yere yatırmayı ve buna bağlı kişi adlarını içerir.","gloss":"yere uzanıp yayılma","neighbor_only":"Yüzüstü kapanmayı, yere yapışmayı, hayvanların uzanmasını ve bitkinin toprağa yayılmasını da kapsar.","neighbor_ref":"root_000928/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bedenin yere yakın biçimde boylu boyunca uzanmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal vuruş ya da düşme sonrası gevşeyip yayılmaya yönelir; bu dal ise sırtüstü hareketsiz yatışı ve birini yere serme eylemini merkez alır.","focus_only":"Kasıtlı yere yatırmayı, yere serilmiş ölüyü ve bedensel engelden doğan sürekli sırtüstü duruşu kapsar.","gloss":"yere düşüp yayılma","neighbor_only":"Vuruş ya da düşme sonucunu, başın sarkmasını ve bütün bedenin gevşemesini özellikle içerir.","neighbor_ref":"root_000668/B002","relation_type":"near_synonym","shared_zone":"İki dal da insan bedeninin yerde uzanmış ve yayılmış durumda bulunmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal bir kişinin beden konumunu ve yere yatırılmasını anlatır; komşu dal ise insan duruşuna bağlı olmayan genel yüzey ve düzleştirme anlamındadır.","focus_only":"İnsan bedeninin yere yatırılması, sırtüstü uzanması ve hareketsiz kalması belirleyicidir.","gloss":"bedenin yere serilmesi","neighbor_only":"Nesnelerin düz üst yüzeyini ve bir şeyi yayıp düzleştirme işlemini anlatır.","neighbor_ref":"root_000703/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da yayılma ve düz, uzanmış bir görünüm bulunur."}],"source_phrase_ar":"سطحوهم أي أضجعوهم على الأرض؛ السطيح المسطوح وهو القتيل (ayn;tahdhib)؛ انسطح الرجل إذا امتد على قفاه فلم يتحرك؛ سمي المنبسط على قفاه من الزمانة سطيحا (jamhara;maqayis)؛ السطيح المستلقي على قفاه من الزمانة (sihah)؛ سمي سطيح الكاهن لكونه منسطحا لزمانة (mufradat)","source_summary":"Ortak kanıt, yere yatırma eylemi ile sırtüstü hareketsiz yatma durumunu birleştirir; ölü için kullanılan ad ve bir kahine verilen ad, bu temel beden konumuna dayanır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"إضجاع الشخص أو المقتول على الأرض، وانسطاح الرجل ممتدا على قفاه لعجز أو زمانة، وتسمية سطيح بذلك","what_is_not_ar":"السطح الأعلى؛ تسطيح الأرض؛ أوعية السطيحة؛ مسطح الخباء"},"support_links":[]},{"boundary":"Dal, genel üst yüzeyi ya da her türlü yapı direğini değil, örtüyü geren veya çardağı taşıyan belirli ahşap parçalarını adlandırır.","branch_kind":"bare","branch_ref":"root_000703/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"örtüyü geren veya çardağı taşıyan sırık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çadır ya da benzeri örtüyü geren ve ona üst biçim kazandıran direk veya sırktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Asma çardağını taşımak üzere enlemesine yerleştirilen ahşap parça için de kullanılır."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çadır örtüsünü geren direk ile asma çardağındaki enine taşıyıcıyı işlevleri üzerinden birlikte karşılar.","boundary_detail":"Dal, genel üst yüzeyi ya da her türlü yapı direğini değil, örtüyü geren veya çardağı taşıyan belirli ahşap parçalarını adlandırır.","branch_image_ar":"عمود يمد عليه الخباء","concept_gloss":"örtüyü geren veya çardağı taşıyan sırık","contextual_glosses":[{"applicability":"Çadır ya da barınak örtüsünü uzatıp gergin tutan taşıyıcı parça kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çadırla bağlantıyı, direk oluşunu ve örtüyü germe işlevini korur."},"facet_ids":["F001"],"text":"çadırı geren direk","usage_role":"contextual"},{"applicability":"Asma çardağını taşımak üzere yatay ve enlemesine yerleştirilen ahşap için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Enine yerleşimi ve asma çardağını taşıma görevini korur."},"facet_ids":["F002"],"text":"enine çardak taşıyıcısı","usage_role":"contextual"}],"definition":"Çadır, barınak ya da benzeri bir örtüyü gerip üst biçimini oluşturan direk veya sırık; ayrıca asma çardağını taşımak üzere enlemesine konan ahşap parçadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çadır ya da benzeri örtüyü geren ve ona üst biçim kazandıran direk veya sırktır."},{"facet_id":"F002","role":"specialization","statement":"Asma çardağını taşımak üzere enlemesine yerleştirilen ahşap parça için de kullanılır."}],"identity_rationale":"Kaynak ifadesi, çadır ya da benzeri örtüyü germeye yarayan direk veya sırık anlamını ortak çekirdek olarak verir ve enlemesine konan, asma çardağını taşıyan ahşabı aynı işlevsel çizgide ekler. Geçici çerçeve hem dikey taşıyıcıyı hem yatay taşıyıcı çeşidini açıkça sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çadırı geren direk"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"asma çardağını taşıyan enine kiriş"}],"lexicalization_note":"Tanım yalnızca bağımsız nesne adının çadır direği ve enine çardak taşıyıcısı anlamlarını içerir; ilişkili eylem veya söz öbeği anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çadır direği ve enine taşıyıcı işlevleriyle doğrudan kesişen üç yapı parçası, sınırı en açık gösteren karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel olarak dikili direğe yönelir; bu dalın sınırı örtüyü germe işleviyle çizilir ve ayrıca enine çardak ahşabına uzanır.","focus_only":"Örtüyü gerip çadıra üst biçim kazandırma işlevini ve enine çardak taşıyıcısını içerir.","gloss":"çadır direği","neighbor_only":"Genel ev ya da çadır direğini ve uzun bir deveye yapılan benzetmeyi de kapsar.","neighbor_ref":"root_000706/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çadırda kullanılan dik ve uzun bir taşıyıcıyı adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dalın enine ahşap anlamı, çadırı geren direk anlamıyla aynı ad altında bulunur; komşu dal ise enine taşıma işlevini daha genel bir yapı parçası olarak kavrar.","focus_only":"Çadır örtüsünü geren direği de içerir ve çardak kullanımında belirli bir adı taşır.","gloss":"enine taşıyıcı ahşap","neighbor_only":"Asma dallarıyla birlikte başka ahşap uçlarını da taşıyan genel enine kiriş işlevine sahiptir.","neighbor_ref":"root_000243/B007","relation_type":"near_neighbor","shared_zone":"İki dal da asma çardağında enlemesine yerleştirilen taşıyıcı bir ahşabı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal ev çatısının uçlarını taşıyan kiriştir; bu dal ise çadır örtüsünü geren direk ya da asma çardağındaki enine ahşaptır.","focus_only":"Çadır örtüsünü germe ve asma çardağını taşıma görevleriyle sınırlıdır.","gloss":"çatı taşıyıcı kirişi","neighbor_only":"Ev çatısındaki ahşap uçlarını taşıyan ana kirişe özgüdür.","neighbor_ref":"root_000276/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal da üstteki ahşap parçaları taşıyan uzun bir yapı elemanını anlatır."}],"source_phrase_ar":"المسطح عود من عيدان الخباء والفسطاط (ayn;tahdhib)؛ المسطح بكسر الميم عمود من أعمدة الخباء (jamhara;sihah)؛ المسطح عمود الخيمة الذي يجعل به لها سطحا (mufradat)؛ إنما سمي بذلك لأنه تمد الخيمة به مدا (maqayis)؛ الخشبة المعروضة تسمى المسطح (tahdhib)","source_summary":"Ortak kanıt, örtüyü gererek bir çadırın üst biçimini oluşturan taşıyıcı sırığı temel alır; enine çardak ahşabı aynı taşıma ve germe işlevinin özel bir uygulamasıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"المسطح عود أو عمود من عيدان الخباء أو الفسطاط أو الخيمة، وما يشبهه من خشبة معروضة يمد عليها العريش","what_is_not_ar":"السطح الأعلى؛ الوعاء المفلطح؛ موضع تجفيف التمر؛ النبات"},"support_links":[]},{"boundary":"Dal her türlü kap için değil, iki deriden yapılmış yassı su kabı ya da kare olmayan tek yanlı yayvan kap için kullanılır.","branch_kind":"bare","branch_ref":"root_000703/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"yayvan deri su kabı veya tek yanlı kap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki deri parçasından yapılan ve yere bırakılınca yassılaşan bir su kabıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kare biçimli olmayan, tek yanı belirgin ve yayvan testi benzeri bir kap için de kullanılır."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki deriden yapılan yassı su kabını ve tek yanı belirgin yayvan kap çeşidini alternatif biçimler olarak karşılar.","boundary_detail":"Dal her türlü kap için değil, iki deriden yapılmış yassı su kabı ya da kare olmayan tek yanlı yayvan kap için kullanılır.","branch_image_ar":"وعاء مفلطح أو ذو جنب واحد","concept_gloss":"yayvan deri su kabı veya tek yanlı kap","contextual_glosses":[{"applicability":"İki deri parçasının birleştirilmesiyle yapılan ve yere konunca yassılaşan su kabı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki deriden yapılma, su taşıma ve yassılaşma özelliklerini korur."},"facet_ids":["F001"],"text":"iki deriden yapılmış yayvan su tulumu","usage_role":"contextual"},{"applicability":"Kare olmayan, tek yanı belirgin, testi ya da yıkanma kabı benzeri kap için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabın tek yanlı, kare olmayan ve yayvan biçimini korur."},"facet_ids":["F002"],"text":"tek yanlı yayvan kap","usage_role":"contextual"}],"definition":"İki deri parçasından yapıldığı ve yere bırakılınca yayıldığı için yassı görünen su kabıdır; ayrıca kare olmayan, tek yanı belirgin ve yayvan testi benzeri bir kap için kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki deri parçasından yapılan ve yere bırakılınca yassılaşan bir su kabıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kare biçimli olmayan, tek yanı belirgin ve yayvan testi benzeri bir kap için de kullanılır."}],"identity_rationale":"Kaynak ifadesi iki bağlantılı kap biçimini destekler: iki deri parçasından yapılan ve yere bırakılınca yassılaşan su kabı ile kare olmayan, tek yanı belirgin yayvan kap. Geçici çerçeve bu biçimsel ortaklığı korurken iki yapım türünü birbirine karıştırmamaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iki deri parçasından yapılmış yayvan su tulumu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek yanlı, yayvan kap"}],"lexicalization_note":"Tanım yalnızca bağımsız kap adının iki deri su kabı ve tek yanlı yayvan kap biçimlerini kapsar; genel kap anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su tulumu yapısı ve genel kap kategorisiyle sınırı doğrudan açıklayan üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel su tulumudur; bu dal iki deriden yapılmış yassı türü merkez alır ve ayrıca tek yanlı yayvan bir kap anlamına sahiptir.","focus_only":"Yassılaşma, iki deri parçasından yapılma ve tek yanlı başka bir kap biçimini içerme özellikleri vardır.","gloss":"su tulumu","neighbor_only":"Biçim ya da iki parçalı yapım şartı olmadan genel su tulumunu anlatır.","neighbor_ref":"root_001212/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da su taşımaya yarayan deri bir kabı adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dalda iki parçalı ve yassı biçim belirleyicidir; komşu dalda ise parçaların dikilerek bir araya getirilmesi öne çıkar.","focus_only":"Özellikle iki deri parçasından yapılan yassı su kabını ve tek yanlı kap çeşidini anlatır.","gloss":"parçalardan dikilmiş su tulumu","neighbor_only":"Birden çok parçanın birbirine dikilmesiyle yapılan su tulumunu yapım tekniği üzerinden adlandırır.","neighbor_ref":"root_000214/B013","relation_type":"near_neighbor","shared_zone":"İki dal da deri parçalarının birleştirilmesiyle yapılan bir su kabını anlatır."},{"boundary_match":"field_only","distinction":"Komşu dal genel kap kategorisidir; bu dal yalnızca belirli yapım ve biçim özellikleri taşıyan kap türlerini belirtir.","focus_only":"Yassı, iki derili ya da tek yanlı belirli kap biçimleriyle sınırlıdır.","gloss":"genel kap","neighbor_only":"İçine herhangi bir şey konan kapların genel adını kapsar.","neighbor_ref":"root_000063/B004","relation_type":"same_field","shared_zone":"Her iki dal da içine bir şey konan taşınabilir kapları adlandırır."}],"source_phrase_ar":"المسطح والمسطحة شبه مطهرة ليست بمربعة؛ الكوز ذو الجنب الواحد مسطح (ayn;tahdhib)؛ السطيحة أديمان يتخذ منهما مزادة (jamhara)؛ السطيحة والسطيح المزادة (sihah)؛ السطيحة المزادة وإنما سميت بذلك لأنه إذا سقط انسطح (maqayis)؛ السطيحة من المزاد إذا كانت من جلدين (tahdhib)","source_summary":"Ortak kanıt, yassı görünüşlü kapları bir araya getirir: biri iki deriden yapılan su kabı, diğeri kare olmayan ve tek yanı belirgin kap biçimidir.","sources":["AY","JA","SI","TA","MQ"],"what_is_ar":"السطيحة والسطيح والمسطح والمسطحة في أوعية الجلد أو الكوز أو شبه المطهرة إذا كان الشكل مفلطحا أو ذا جنب واحد","what_is_not_ar":"السطح الأعلى؛ جسم منسطح؛ عمود الخباء؛ موضع تجفيف التمر؛ النبات"},"support_links":[]},{"boundary":"Üç kullanım aynı yüzey fikriyle bağlantılıdır, fakat kurutma yeri, su toplayan kaya yüzü ve hasır birbirinin yerine geçen tek bir nesne değildir.","branch_kind":"bare","branch_ref":"root_000703/B005","candidate_links":[{"candidate_id":"cand_399c1bf424860a56dd72","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"düz kurutma yeri, su toplayan kaya yüzü veya hasır","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düz ya da yayvan bir yüzeyden yararlanılan yer ve nesnelere uzanan çok anlamlı bir addır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hurmanın serilip güneşte kurutulduğu düz yerdir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çevresi taşla çevrilerek yağmur suyunun biriktirildiği geniş kaya yüzüdür."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hurma ağacı yapraklarından örülen bir hasırdır."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aynı adın üç ayrı referentini tek bir üst kategoriye indirgemeden alternatifler halinde gösterir.","boundary_detail":"Üç kullanım aynı yüzey fikriyle bağlantılıdır, fakat kurutma yeri, su toplayan kaya yüzü ve hasır birbirinin yerine geçen tek bir nesne değildir.","branch_image_ar":"موضع أو بساط مسطح ينتفع به","concept_gloss":"düz kurutma yeri, su toplayan kaya yüzü veya hasır","contextual_glosses":[{"applicability":"Hurmaların serilip güneşte kurutulduğu düz ve hazırlanmış yer kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düz yeri, hurmanın serilmesini ve kurutma amacını korur."},"facet_ids":["F002"],"text":"hurma kurutma yeri","usage_role":"contextual"},{"applicability":"Çevresi taşlarla sınırlandırılmış geniş kaya yüzünde yağmur suyu biriktiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geniş kaya yüzünü, çevre sınırını ve su biriktirme işlevini korur."},"facet_ids":["F003"],"text":"su toplayan geniş kaya yüzü","usage_role":"explanatory"},{"applicability":"Hurma ağacı yapraklarının örülmesiyle yapılan hasır kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hasır oluşunu, bitkisel malzemeyi ve örme yapımını korur."},"facet_ids":["F004"],"text":"hurma yaprağından örülmüş hasır","usage_role":"contextual"}],"definition":"Aynı ad, hurmanın serilip kurutulduğu düz yere, yağmur suyunun biriktiği çevresi taşla çevrili geniş kaya yüzüne ve hurma yaprağından örülmüş hasıra verilir; bunlar tek nesne değil, düz ya da yayvan yüzey ortaklığı taşıyan ayrı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düz ya da yayvan bir yüzeyden yararlanılan yer ve nesnelere uzanan çok anlamlı bir addır."},{"facet_id":"F002","role":"specialization","statement":"Hurmanın serilip güneşte kurutulduğu düz yerdir."},{"facet_id":"F003","role":"source_variant","statement":"Çevresi taşla çevrilerek yağmur suyunun biriktirildiği geniş kaya yüzüdür."},{"facet_id":"F004","role":"source_variant","statement":"Hurma ağacı yapraklarından örülen bir hasırdır."}],"identity_rationale":"Kaynak ifadesi tek bir nesne türünü değil, aynı adla anılan üç ayrı referenti verir: hurmanın kurutulduğu düz yer, su toplayan geniş kaya yüzü ve hurma yaprağından örülmüş hasır. Dal korunabilir, ancak bu kullanımların tek bir nesne gibi kaynaştırılmaması ve düz ya da yayvan yüzey ortaklığı altında alternatifler olarak gösterilmesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hurma kurutulan düz yer"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"suyun biriktiği geniş kaya yüzü"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hurma yaprağından örülmüş hasır"}],"lexicalization_note":"Tanım bağımsız adın üç ayrı referentini açıkça sıralar; bunları genel düz yer, genel su haznesi ya da genel hasır anlamına genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; üç referentin her biriyle doğrudan sınır karşılaştırması sağlayan düz yer, hasır, düz taban ve su biriktiren çukur adayları seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel bir açık ya da düz yerdir; bu dalın yer anlamı hurma kurutma işleviyle sınırlıdır ve ayrıca iki ayrı nesne anlamı taşır.","focus_only":"Hurma kurutma amacı ile su toplayan kaya yüzü ve örme hasır anlamlarını içerir.","gloss":"düz açık yer","neighbor_only":"Açık avlu, düz arazi ve pürüzsüz yer yüzeyi gibi genel mekanları kapsar.","neighbor_ref":"root_000854/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da düz ve açık bir yer yüzeyini adlandırabilir."},{"boundary_match":"partial","distinction":"Bu dal yalnızca belirli bitkisel malzemeden örülen hasır kullanımına sahiptir; komşu dal daha genel bir yaygı ve döşek kategorisidir.","focus_only":"Belirli biçimde hurma yaprağından örülen hasırı, ayrıca iki yer anlamını içerir.","gloss":"yaygı veya hasır","neighbor_only":"Malzemesi belirtilmeyen genel döşek, yaygı ve hasır alanını kapsar.","neighbor_ref":"root_001397/B007","relation_type":"near_neighbor","shared_zone":"İki dal da yere serilebilen bir hasır ya da yaygıyı adlandırabilir."},{"boundary_match":"partial","distinction":"Komşu dal biçimsel olarak düz yeri adlandırır; bu dalın yer anlamı belirli bir kurutma işlevine bağlıdır.","focus_only":"Düz yer kullanımını hurma kurutma amacıyla sınırlar ve kaya yüzü ile hasır anlamlarını da taşır.","gloss":"düz taban","neighbor_only":"Herhangi bir özel kullanım amacı olmadan düz taban ya da düz yer anlamındadır.","neighbor_ref":"root_001204/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da düz bir zemin ya da yer parçasını anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal kazılmış ya da çukur bir yapıdır; bu dalın su biriktirme kullanımı geniş kaya yüzünün çevresini taşla sınırlamaya dayanır.","focus_only":"Suyu geniş bir kaya yüzünde, çevresine taş dizerek biriktirir ve başka iki yüzey anlamını da içerir.","gloss":"su biriktiren oyuk","neighbor_only":"Kazılmış çukur, kuyu ve üstü örtülü yakalama çukuru biçimlerini kapsar.","neighbor_ref":"root_000078/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da suyun ya da başka bir şeyin biriktiği sınırlı bir yer oluşturabilir."}],"source_phrase_ar":"المسطح الموضع الذي يجفف ويبسط فيه التمر (jamhara;sihah;maqayis)؛ المسطح مكان مستو يجفف عليه التمر ويسمى الجرين (tahdhib)؛ المسطح الصفاة يحاط عليها بالحجارة فيجتمع فيها الماء (sihah)؛ صفيحة عريضة من الصخر يحوط عليه لماء السماء (tahdhib)؛ المسطح حصير يسف من خوص الدوم (tahdhib)","source_summary":"Toplu kanıt, aynı bağımsız ad altında üç ayrı kullanım verir: kurutma yeri, su biriktiren geniş kaya yüzü ve örme hasır. Bunlar düz ya da yayvan yüzey görünümüyle bağlantılı olsa da ayrı referentlerdir.","sources":["JA","SI","TA","MQ"],"what_is_ar":"المسطح موضع مستو يبسط عليه التمر ليجف، أو صفاة عريضة يجتمع فيها الماء، أو حصير مسفوف من خوص الدوم","what_is_not_ar":"عمود الخباء؛ الوعاء المفلطح؛ الجسم المنسطح؛ النبات"},"support_links":["sup_32dede5392b658222a5a"]},{"boundary":"Dal genel bitki ya da genel yayılma anlamı değildir; yere yayılan belirli otu ve ona bağlı kullanım bilgisini kapsar.","branch_kind":"bare","branch_ref":"root_000703/B006","candidate_links":[{"candidate_id":"cand_a8b28d9c84356e01a920","lane":"macro"},{"candidate_id":"cand_0bfea26fc425c99ef016","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","surface_ar":"سُطِحَتْ"}],"gloss":"yere yayılarak büyüyen bir ot","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak üzerinde dik yükselmek yerine yayılarak büyüyen belirli bir ot türüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanlar bu otu otlar ve yaprakları baş yıkamak için kullanılır."}}],"root_ar":"س ط ح","root_id":"root_000703","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitki adını, onu ayırt eden toprak üzerinde yayılma biçimiyle doğal Türkçe olarak karşılar.","boundary_detail":"Dal genel bitki ya da genel yayılma anlamı değildir; yere yayılan belirli otu ve ona bağlı kullanım bilgisini kapsar.","branch_image_ar":"نبت ينبسط على الأرض","concept_gloss":"yere yayılarak büyüyen bir ot","contextual_glosses":[{"applicability":"Bitkinin dik büyümek yerine toprak yüzüne yayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ot oluşunu ve yere yayılı büyüme biçimini korur."},"facet_ids":["F001"],"text":"yerde yayılan ot","usage_role":"contextual"},{"applicability":"Yere yayılan bitkinin hayvanlarca yenmesi özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yayılıcı büyümeyi ve hayvanların bu bitkiyi otlamasını korur."},"facet_ids":["F001","F002"],"text":"hayvanların otladığı yayılıcı bitki","usage_role":"explanatory"}],"definition":"Toprak üzerinde yayılıp genişleyerek büyüyen belirli bir ot türüdür. Hayvanların otlaması ve yapraklarının baş yıkamada kullanılması, bu bitkiye bağlı ikincil kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak üzerinde dik yükselmek yerine yayılarak büyüyen belirli bir ot türüdür."},{"facet_id":"F002","role":"associated_use","statement":"Hayvanlar bu otu otlar ve yaprakları baş yıkamak için kullanılır."}],"identity_rationale":"Kaynak ifadesi bu dalı yere yayılarak büyüyen belirli bir ot türü olarak tanımlar. Hayvanların onu otlaması ve yapraklarının baş yıkamada kullanılması bitkinin kimliğini değiştirmeyen, ona bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yere yayılarak büyüyen bir ot"}],"lexicalization_note":"Tanım yalnızca bağımsız bitki adının yere yayılan ot anlamını verir; genel bitki, büyüme veya düzleştirme anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ot, genel bitkisel büyüme ve kökün temel yayılma dalı, tür ile üst kategori sınırını en iyi gösteren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ot ve taze bitki kategorisidir; bu dal yere yayılan belirli bir bitki türüyle sınırlıdır.","focus_only":"Yere yayılarak büyüyen belirli bir otu ve bu ota bağlı kullanım bilgisini anlatır.","gloss":"taze yeşil ot","neighbor_only":"Ağaç olmayan taze ve yeşil bitkileri genel bir kategori olarak kapsar.","neighbor_ref":"root_000141/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağaç olmayan yeşil ve otumsu bir bitkiyi adlandırabilir."},{"boundary_match":"field_only","distinction":"Komşu dal genel bitki ve büyüme kavramıdır; bu dal ise yerde yayılan belirli bir otun adıdır.","focus_only":"Belirli bir ot türünü, yerde yayılı büyüme biçimiyle adlandırır.","gloss":"bitki ve büyüme","neighbor_only":"Ot, ekin ve ağacın topraktan çıkmasını ve genel bitkisel büyümeyi kapsar.","neighbor_ref":"root_001465/B001","relation_type":"same_field","shared_zone":"İki dal da topraktan çıkan ve büyüyen bitkiler alanındadır."},{"boundary_match":"partial","distinction":"Bu dal yayılma özelliğiyle tanınan belirli bir bitkidir; komşu dal bitkiye özgü olmayan genel yüzey ve yayılma anlamıdır.","focus_only":"Yayılma biçimini belirli bir bitki türünün kalıcı büyüme özelliği olarak taşır.","gloss":"yere yayılan bitki","neighbor_only":"Genel düz üst yüzeyi, düzleştirme işlemini ve herhangi bir şeyin genişlemesini kapsar.","neighbor_ref":"root_000703/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şeyin enine yayılarak geniş alan kaplaması düşüncesi bulunur."}],"source_phrase_ar":"السطاح ضرب من النبت (jamhara)؛ السطاح نبت الواحد سطاحة (sihah)؛ السطاحة بقلة ترعاها الماشية ويغسل بورقها الرؤوس (tahdhib)؛ السطاح نبت من نبات الأرض وذلك أنه ينبسط على الأرض (maqayis)","source_summary":"Ortak kanıt, dalı yere yayılan bir ot türü olarak tanımlar; hayvanların otlaması ve yaprakların yıkamada kullanılması bu bitkinin ayırt edici kullanım bilgisidir.","sources":["JA","SI","TA","MQ"],"what_is_ar":"السطاح أو السطاحة من النبت أو البقل المنبسط على الأرض","what_is_not_ar":"السطح الأعلى؛ تسطيح الأرض؛ الجسم المنسطح؛ أوعية السطيحة"},"support_links":["sup_30996586adcb86125b8f","sup_9328151575867451fa13"]},{"boundary":"The word السطر used for a young male goat.","branch_kind":null,"branch_ref":"root_000704/B007","candidate_links":[{"candidate_id":"cand_c8214b1bab1fff3be362","lane":"macro"}],"focus_root_occurrences":[],"gloss":"young goat named satr","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السطر العتود","image_en":"young goat named satr"}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السطر العتود","image_en":"young goat named satr","scope_ar":"السطر بمعنى العتود من الغنم","scope_en":"The word السطر used for a young male goat."},"support_links":["sup_abb8d1ebf71563df9a7f"]},{"boundary":"The sky or any upper covering/surface, with source-attested extensions to cloud, rain, vegetation from rain, and an animal's upper back.","branch_kind":null,"branch_ref":"root_000745/B004","candidate_links":[{"candidate_id":"cand_b7f3f963583589d7075d","lane":"macro"},{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"}],"focus_root_occurrences":[],"gloss":"overhead sky and cover","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السماء وما علا فأظل","image_en":"overhead sky and cover"}}],"root_ar":"س م و","root_id":"root_000745","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السماء وما علا فأظل","image_en":"overhead sky and cover","scope_ar":"يدخل فيه السماء لما علا وأظل، والسقف، والسحاب، والمطر، والنبات المنسوب إلى المطر، وظهر الفرس أو أعلى الشيء.","scope_en":"The sky or any upper covering/surface, with source-attested extensions to cloud, rain, vegetation from rain, and an animal's upper back."},"support_links":["sup_68820d785ed9e8cc2d15","sup_73747b89a46171a56c68"]},{"boundary":"It covers something or someone called عذوب/عاذب because there is no covering between it and the sky.","branch_kind":null,"branch_ref":"root_000994/B004","candidate_links":[{"candidate_id":"cand_b7f3f963583589d7075d","lane":"macro"}],"focus_root_occurrences":[],"gloss":"open to the sky","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"العذوب المكشوف للسماء","image_en":"open to the sky"}}],"root_ar":"ع ذ ب","root_id":"root_000994","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"العذوب المكشوف للسماء","image_en":"open to the sky","scope_ar":"يدخل فيه العذوب أو العاذب الذي لا ستر بينه وبين السماء.","scope_en":"It covers something or someone called عذوب/عاذب because there is no covering between it and the sky."},"support_links":["sup_73747b89a46171a56c68"]},{"boundary":"Includes the pastoral usage of separating young livestock from older animals or from their mothers.","branch_kind":null,"branch_ref":"root_001684/B015","candidate_links":[{"candidate_id":"cand_c8214b1bab1fff3be362","lane":"macro"}],"focus_root_occurrences":[],"gloss":"separating young livestock","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"موالاة صغار النعم عن كبارها","image_en":"separating young livestock"}}],"root_ar":"و ل ي","root_id":"root_001684","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"موالاة صغار النعم عن كبارها","image_en":"separating young livestock","scope_ar":"يدخل فيه والوا حواشي النعم من الجلة، أي عزل الصغار عن الكبار، وتوالي السقاب بمعنى فصالها عن الأمهات حتى تنقاد","scope_en":"Includes the pastoral usage of separating young livestock from older animals or from their mothers."},"support_links":["sup_abb8d1ebf71563df9a7f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000006/B001","candidate_links":[{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1241e4e863c50ebf294a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The camel together with its care supplies an embodied user of the habitat.","root":"ء ب ل","source_ref":"88:17","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000006","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9ebc421e82623e106329"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000217/B001","candidate_links":[{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfef87b471bccbeb7841","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A high solid aggregation supplies resistant vertical mass between sky and ground.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000217","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68820d785ed9e8cc2d15"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_399c1bf424860a56dd72","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_85c99792305e34cc2288","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting and accounting supply the operation that reads and evaluates the inscribed record.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_32dede5392b658222a5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1241e4e863c50ebf294a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measuring and proportioning supply deliberate calibration in the making process.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9ebc421e82623e106329"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B008","candidate_links":[{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1241e4e863c50ebf294a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Smoothness and evenness of a surface directly bridge creature-creation language to the focus operation.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9ebc421e82623e106329"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B008","candidate_links":[{"candidate_id":"cand_399c1bf424860a56dd72","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_85c99792305e34cc2288","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A document establishing a right supplies durable recording rather than fleeting recollection.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_32dede5392b658222a5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000516/B009","candidate_links":[{"candidate_id":"cand_044f714329608f7d322f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c1bd7c76078a3ffc8e15","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A reminder that causes recollection supplies the pedagogical function of the visible surface.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000516","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_653cc76172c0f339f13e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfef87b471bccbeb7841","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Lifting something upward supplies the operation that establishes the top member.","root":"ر ف ع","source_ref":"88:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000582","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68820d785ed9e8cc2d15"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000704/B001","candidate_links":[{"candidate_id":"cand_399c1bf424860a56dd72","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_85c99792305e34cc2288","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An aligned written line supplies ordered inscription across the flat support.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000704","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_32dede5392b658222a5a"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000704/B003","candidate_links":[{"candidate_id":"cand_044f714329608f7d322f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c1bd7c76078a3ffc8e15","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The controlling overseer supplies the coercive mode explicitly denied after the reminder.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000704","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_653cc76172c0f339f13e"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001307/B003","candidate_links":[{"candidate_id":"cand_a8b28d9c84356e01a920","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_239a1aece44bb37d2e83","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Hiding truth supplies the epistemically destructive form of covering.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001307","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_30996586adcb86125b8f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001307/B008","candidate_links":[{"candidate_id":"cand_a8b28d9c84356e01a920","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_239a1aece44bb37d2e83","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Covering seed supplies the materially productive form of the same action.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001307","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_30996586adcb86125b8f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_b47128b2e51e8a9ff6fe","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_dfef87b471bccbeb7841","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Setting something upright and prominent supplies the operation that establishes the vertical masses.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001507","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_68820d785ed9e8cc2d15"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001520/B001","candidate_links":[{"candidate_id":"cand_9b6b402765cb77b90e40","lane":"macro"},{"candidate_id":"cand_044f714329608f7d322f","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_1241e4e863c50ebf294a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Directing sight or insight supplies examination of functional fit rather than passive noticing.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]},{"hft_ref":"hft_c1bd7c76078a3ffc8e15","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Directed sight or insight supplies the observer's active engagement with the sign.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001520","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_653cc76172c0f339f13e","sup_9ebc421e82623e106329"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001650/B003","candidate_links":[{"candidate_id":"cand_0bfea26fc425c99ef016","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_60d9e3f76131b6c4452b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapping's first rain marks the earth with vegetation, supplying the initial inscription.","root":"س م و","source_ref":"88:18","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001650","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9328151575867451fa13"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B007","candidate_links":[{"candidate_id":"cand_a8b28d9c84356e01a920","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_239a1aece44bb37d2e83","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Turning away supplies the directional refusal that converts concealment into evasion.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_30996586adcb86125b8f"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001684/B010","candidate_links":[{"candidate_id":"cand_0bfea26fc425c99ef016","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_60d9e3f76131b6c4452b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Rain following the first marking rain supplies a successive layer in the surface-making process.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001684","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9328151575867451fa13"]}],"candidate_inventory":[{"anchor_refs":["88:17","88:20","88:23"],"branch_refs":["root_000006/B003","root_000704/B007","root_001684/B015"],"candidate_id":"cand_c8214b1bab1fff3be362","commentary_obligation":"review","focus_branch_refs":[],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000006/B003","root_000704/B007","root_001684/B015"],"root_ids":[],"scope":"pericope","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_ids":["sup_05033d9ef10d148b8120","sup_2e0090a494f868f4e6f6","sup_6a89d4d85836965df45a","sup_8fef3cd03c2cd8cf5941","sup_abb8d1ebf71563df9a7f"],"title":"Goat and Separated Young Stock","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:18","88:20","88:24"],"branch_refs":["root_000025/B001","root_000745/B004","root_000994/B004"],"candidate_id":"cand_b7f3f963583589d7075d","commentary_obligation":"review","focus_branch_refs":["root_000025/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000745/B004","root_000994/B004"],"root_ids":[],"scope":"pericope","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_ids":["sup_5553e96931717ea2f129","sup_6a85aef38881bb317613","sup_73747b89a46171a56c68","sup_780d4350f790faa73328","sup_f3a430146d52df343a0f"],"title":"Exposure Beneath the Sky","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:17","88:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000006/B001","root_000025/B001","root_000434/B001","root_000434/B008","root_000703/B001","root_001520/B001"],"candidate_id":"cand_9b6b402765cb77b90e40","commentary_obligation":"review","hft_ref":"hft_1241e4e863c50ebf294a","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_measured_habitat","source_type":"hft","support_ids":["sup_9ebc421e82623e106329"],"title":"delta_measured_habitat","trust":"legacy_unbound"},{"anchor_refs":["88:18","88:19","88:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000025/B001","root_000217/B001","root_000582/B001","root_000703/B001","root_000745/B004","root_001507/B001"],"candidate_id":"cand_b47128b2e51e8a9ff6fe","commentary_obligation":"review","hft_ref":"hft_dfef87b471bccbeb7841","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_vertical_architecture","source_type":"hft","support_ids":["sup_68820d785ed9e8cc2d15"],"title":"delta_vertical_architecture","trust":"legacy_unbound"},{"anchor_refs":["88:17","88:20","88:21","88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000025/B001","root_000516/B009","root_000703/B001","root_000704/B003","root_001520/B001"],"candidate_id":"cand_044f714329608f7d322f","commentary_obligation":"review","hft_ref":"hft_c1bd7c76078a3ffc8e15","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_visible_reminder","source_type":"hft","support_ids":["sup_653cc76172c0f339f13e"],"title":"delta_visible_reminder","trust":"legacy_unbound"},{"anchor_refs":["88:20","88:23"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000025/B002","root_000703/B006","root_001307/B003","root_001307/B008","root_001684/B007"],"candidate_id":"cand_a8b28d9c84356e01a920","commentary_obligation":"review","hft_ref":"hft_239a1aece44bb37d2e83","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_productive_or_occluding_cover","source_type":"hft","support_ids":["sup_30996586adcb86125b8f"],"title":"delta_productive_or_occluding_cover","trust":"legacy_unbound"},{"anchor_refs":["88:18","88:20","88:23"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000025/B002","root_000703/B006","root_001650/B003","root_001684/B010"],"candidate_id":"cand_0bfea26fc425c99ef016","commentary_obligation":"review","hft_ref":"hft_60d9e3f76131b6c4452b","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_rain_written_surface","source_type":"hft","support_ids":["sup_9328151575867451fa13"],"title":"outlier_rain_written_surface","trust":"legacy_unbound"},{"anchor_refs":["88:20","88:21","88:22","88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:20","branch_refs":["root_000318/B001","root_000516/B008","root_000703/B005","root_000704/B001"],"candidate_id":"cand_399c1bf424860a56dd72","commentary_obligation":"review","hft_ref":"hft_85c99792305e34cc2288","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_surface_as_ledger","source_type":"hft","support_ids":["sup_32dede5392b658222a5a"],"title":"outlier_surface_as_ledger","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_71bb55a61cc92828949b","connection_ref":"conn_eab357638c5f6d157773","note":"Immediate paired observation; supplies the mountain element of the same ordered scene.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_aea8def70db3dea4ef85","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:19","source_note":"Completes the adjacent earthward observation and the vertical landscape order.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:19","source_target_components":["88:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:19","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},"target_ref":"88:19"},{"connection_evidence_ref":"conn_ev_370f95391490944b1a76","connection_ref":"conn_ee6bdfa13f0725d19d66","note":"Immediate paired observation; supplies the upper counterpart to the earth below.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_ea87436d71cdadda7ecc","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:18","source_note":"Direct fourth member of the observational sequence; same interrogative and passive framing.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:18","source_target_components":["88:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:18","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},"target_ref":"88:18"},{"connection_evidence_ref":"conn_ev_8a00554ab2061f12b53d","connection_ref":"conn_841259ec07b159a8fb80","note":"Opens the immediate fourfold observational sequence culminating in 88:20.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d5c0e7bec9b70bcb5dbc","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:17","source_note":"Completes the immediate how-question series with the earth as another observable.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:17","source_target_components":["88:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:17","target_evidence":{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},"target_ref":"88:17"},{"connection_evidence_ref":"conn_ev_8582d9eb4e5f18718910","connection_ref":"conn_650991b525dfc624b523","note":"The ensuing reminder sets the function of the preceding observations, without redefining earth.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_e84666c15d389f7a42fd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:21","source_note":"The final immediate sign completes the observational material to be recalled in 88:21.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21","target_evidence":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},"target_ref":"88:21"},{"connection_evidence_ref":"conn_ev_6e0abedafb614d1e0e9c","connection_ref":"conn_491d9bedf96aa98b3723","note":"Later consequence contrasts with the focus's invitation to observe, but adds little detail.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_841d638f84dbd4a3afba","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:24","source_note":"Completes the immediate sequence of signs preceding the focus.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:24","source_target_components":["88:24"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:24","target_evidence":{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","ayah_ref":"88:24"},"target_ref":"88:24"},{"connection_evidence_ref":"conn_ev_53832c6564fce0272391","connection_ref":"conn_5475aa0269b9c06b120a","note":"Nearby refusal is consequence framing, not an added reading of earth.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_c0769ac72051ea3b78dc","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:23","source_note":"A further observation-sign, now redundant within the same immediate sequence.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:23","source_target_components":["88:23"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:23","target_evidence":{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},"target_ref":"88:23"},{"connection_evidence_ref":"conn_ev_8fc6aa76416c66c8edb1","connection_ref":"conn_7a5c8151aa3c0a98d6e5","note":"Immediate continuation limits control over listeners, only indirectly related to observation.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_1b4886c7cc743dbf142d","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:22","source_note":"The observation sequence supports f04 only as redundant context.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:22","source_target_components":["88:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:22","target_evidence":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},"target_ref":"88:22"},{"connection_evidence_ref":"conn_ev_7c8dc7f759a9d588c82f","connection_ref":"conn_eaf6859a03d6d4e2deea","note":"The focus's own later return statement directly prevents earth from being the final end.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_acfdef2665f9abea43bd","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:25","source_note":"Offers only the local observational movement before the focus.","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:25","source_target_components":["88:25"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:25","target_evidence":{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"},"target_ref":"88:25"}],"focus":{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:20:1:1","qac_word_ref":"88:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:20:1:2","qac_word_ref":"88:20:1","root_ar":"","surface_ar":"إِلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:20:2:1","qac_word_ref":"88:20:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","root_ar":"ء ر ض","surface_ar":"أَرْضِ"},{"lemma_ar":"كَيْف","morph_features":"STEM|POS:INTG|LEM:kayof|ROOT:kyf","morpheme_role":"STEM","pos":"INTG","qac_ref":"88:20:3:1","qac_word_ref":"88:20:3","root_ar":"ك ي ف","surface_ar":"كَيْفَ"},{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","root_ar":"س ط ح","surface_ar":"سُطِحَتْ"}],"word_analysis_qac_refs":[["88:20:1:1"],["88:20:1:2"],["88:20:2:1","88:20:2:2"],["88:20:3:1"],["88:20:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:20:1","88:20:2","88:20:3","88:20:4","88:20:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:20:1:1","qac_word_ref":"88:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:20:1:2","qac_word_ref":"88:20:1","root_ar":"","surface_ar":"إِلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:20:2:1","qac_word_ref":"88:20:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:20:2:2","qac_word_ref":"88:20:2","root_ar":"ء ر ض","surface_ar":"أَرْضِ"},{"lemma_ar":"كَيْف","morph_features":"STEM|POS:INTG|LEM:kayof|ROOT:kyf","morpheme_role":"STEM","pos":"INTG","qac_ref":"88:20:3:1","qac_word_ref":"88:20:3","root_ar":"ك ي ف","surface_ar":"كَيْفَ"},{"lemma_ar":"سُطِحَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:suTiHato|ROOT:sTH|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:20:4:1","qac_word_ref":"88:20:4","root_ar":"س ط ح","surface_ar":"سُطِحَتْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:20:1:1"],["88:20:1:2"],["88:20:2:1","88:20:2:2"],["88:20:3:1"],["88:20:4:1"]],"word_analysis_refs":["88:20:1","88:20:2","88:20:3","88:20:4","88:20:5"],"word_rows":[{"analysis_record_ref":"88:20:1","analytic_gloss_range_en":"local connective continuation that adds the final earth target into the ongoing observation sequence","analytic_root_gloss_range_en":null,"qac_refs":["88:20:1:1"],"root":{"note":"—"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:20:2","analytic_gloss_range_en":"directional and attentional preposition governing earth as the endpoint of looking and reflection, not a locative stance marker","analytic_root_gloss_range_en":null,"qac_refs":["88:20:1:2"],"root":{"note":"—"},"surface":{"arabic":"إِلَى","transliteration":"ilā"}},{"analysis_record_ref":"88:20:3","analytic_gloss_range_en":"the familiar earth as governed target, lower domain, contact ground, and passive patient of the surfacing question","analytic_root_gloss_range_en":"root range around earth, ground, land, soil, territory, and the terrestrial lower realm; locally the definite singular gathers those senses into one familiar surface-bearing domain","qac_refs":["88:20:2:1","88:20:2:2"],"root":{"arabic":"أ ر ض","transliteration":"ʾ-r-ḍ"},"surface":{"arabic":"ٱلْأَرْضِ","transliteration":"al-arḍi"}},{"analysis_record_ref":"88:20:4","analytic_gloss_range_en":"circumstantial manner interrogative asking how and in what configuration the earth has been surfaced","analytic_root_gloss_range_en":null,"qac_refs":["88:20:3:1"],"root":{"note":"—"},"surface":{"arabic":"كَيْفَ","transliteration":"kayfa"}},{"analysis_record_ref":"88:20:5","analytic_gloss_range_en":"completed passive surfacing of the earth into an exposed, leveled, usable plane; the agent is unexpressed and the result is made inspectable","analytic_root_gloss_range_en":"root range centered on flat extended surfaces, roof-like top faces, spreading or leveling into a surface, and related flat or spread objects; locally the earth-context selects passive surface-making rather than unrelated vessel, tent-pole, body-laid-flat, or plant branches","qac_refs":["88:20:4:1"],"root":{"arabic":"س ط ح","transliteration":"s-ṭ-ḥ"},"surface":{"arabic":"سُطِحَتْ","transliteration":"suṭiḥat"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":8,"missing_anchor_refs":[],"supplied_unique_anchor_count":8},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["88:17","88:20"],"branch_refs":["root_000006/B001","root_000025/B001","root_000434/B001","root_000434/B008","root_000703/B001","root_001520/B001"],"candidate_id":"cand_9b6b402765cb77b90e40","evidence_scope":"declared_pericope","hft_ref":"hft_1241e4e863c50ebf294a","item_id":"delta_measured_habitat","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_measured_habitat","support_id":"sup_9ebc421e82623e106329"},{"anchor_refs":["88:18","88:19","88:20"],"branch_refs":["root_000025/B001","root_000217/B001","root_000582/B001","root_000703/B001","root_000745/B004","root_001507/B001"],"candidate_id":"cand_b47128b2e51e8a9ff6fe","evidence_scope":"declared_pericope","hft_ref":"hft_dfef87b471bccbeb7841","item_id":"delta_vertical_architecture","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_vertical_architecture","support_id":"sup_68820d785ed9e8cc2d15"},{"anchor_refs":["88:17","88:20","88:21","88:22"],"branch_refs":["root_000025/B001","root_000516/B009","root_000703/B001","root_000704/B003","root_001520/B001"],"candidate_id":"cand_044f714329608f7d322f","evidence_scope":"declared_pericope","hft_ref":"hft_c1bd7c76078a3ffc8e15","item_id":"delta_visible_reminder","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_visible_reminder","support_id":"sup_653cc76172c0f339f13e"},{"anchor_refs":["88:20","88:23"],"branch_refs":["root_000025/B002","root_000703/B006","root_001307/B003","root_001307/B008","root_001684/B007"],"candidate_id":"cand_a8b28d9c84356e01a920","evidence_scope":"declared_pericope","hft_ref":"hft_239a1aece44bb37d2e83","item_id":"delta_productive_or_occluding_cover","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_productive_or_occluding_cover","support_id":"sup_30996586adcb86125b8f"},{"anchor_refs":["88:18","88:20","88:23"],"branch_refs":["root_000025/B002","root_000703/B006","root_001650/B003","root_001684/B010"],"candidate_id":"cand_0bfea26fc425c99ef016","evidence_scope":"declared_pericope","hft_ref":"hft_60d9e3f76131b6c4452b","item_id":"outlier_rain_written_surface","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_rain_written_surface","support_id":"sup_9328151575867451fa13"},{"anchor_refs":["88:20","88:21","88:22","88:26"],"branch_refs":["root_000318/B001","root_000516/B008","root_000703/B005","root_000704/B001"],"candidate_id":"cand_399c1bf424860a56dd72","evidence_scope":"declared_pericope","hft_ref":"hft_85c99792305e34cc2288","item_id":"outlier_surface_as_ledger","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_surface_as_ledger","support_id":"sup_32dede5392b658222a5a"}],"diagnostics":[],"lane_counts":{"global":14,"macro":6,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:20","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:20","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:20","lane":"macro","linguistic_source_ref":"88:20","surface_ref":"88:20","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:20","target_tokens":[["Ve",["88:20:1"]],["yere",["88:20:1","88:20:2"]],["nasıl",["88:20:3"]],["düzleştirildiğine",["88:20:4"]]],"text":"Ve yere, nasıl düzleştirildiğine?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_05033d9ef10d148b8120","text":"Age classification becomes a management practice when young stock are sorted from the larger herd.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_2e0090a494f868f4e6f6","text":"Young animals are identified, divided from the main herd, and managed as a distinct group.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_5553e96931717ea2f129","text":"A layer, enclosure, or obscurity limits access to what lies within.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_6a85aef38881bb317613","text":"An uncovered object or place stands open beneath the overhead sky.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_6a89d4d85836965df45a","text":"Animals outside ordinary domestic use are pursued, trapped, classified, or distinguished by age and form.","trust":"trusted"},{"branch_refs":["root_000025/B001","root_000745/B004","root_000994/B004"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_73747b89a46171a56c68","text":"exposed to the sky `ع ذ ب:B004/m01`; overhead expanse `س م و:B004/m01`; lower ground beneath it `ء ر ض:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_780d4350f790faa73328","text":"88:18 `السماء` (`س م و`); 88:20 `الأرض` (`ء ر ض`); 88:24 `العذاب` (`ع ذ ب`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_8fef3cd03c2cd8cf5941","text":"88:20 `سطحت` (`س ط ر`); 88:23 `تولى` (`و ل ي`); 88:17 `الإبل` (`ء ب ل`)","trust":"trusted"},{"branch_refs":["root_000006/B003","root_000704/B007","root_001684/B015"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"D:Goat and Separated Young Stock","source_type":"channel","support_id":"sup_abb8d1ebf71563df9a7f","text":"young goat `س ط ر:B007/m01`; separated young livestock `و ل ي:B015/m02`; herd group `ء ب ل:B003/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Exposure Beneath the Sky","source_type":"channel","support_id":"sup_f3a430146d52df343a0f","text":"Exposure reverses the covering relation: the lower surface remains directly open to what arches above it.","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000006/B001","root_000025/B001","root_000434/B001","root_000434/B008","root_000703/B001","root_001520/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground supplies the creature's contact and travel substrate.","root":"ء ر ض","source_ref":"88:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000703","role":"Level extension supplies the broad physical affordance to be calibrated.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001520","role":"Directing sight or insight supplies examination of functional fit rather than passive noticing.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000006","role":"The camel together with its care supplies an embodied user of the habitat.","root":"ء ب ل","source_ref":"88:17","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring and proportioning supply deliberate calibration in the making process.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]},{"branch_id":"B008","mapped_root_id":"root_000434","role":"Smoothness and evenness of a surface directly bridge creature-creation language to the focus operation.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]}],"changed_reading":{"after":"Leveling calibrates the earth as an embodied habitat, fitted to movement, care, and use.","before":"Leveling gives the earth a generic physical shape."},"confidence":"strong","mechanism":"Directed observation, an embodied creature requiring care, measured creation, and a creation-branch explicitly involving smoothness revise extension into calibrated affordance. The ground and the creature can be read as mutually fitted rather than separately displayed.","model_id":"delta_measured_habitat","reader_inference":"The packet supplies directed inspection, camel care, proportioning, and surface evenness; I infer a design relation between creature and ground. A live alternative takes each created item as an independent sign with no habitat-level coupling.","status":"revised","structural_cues":["Verses 17-20 repeat one directional, interrogative, passive frame; the branchless root ك ي ف is used only as this structural cue.","The sequence moves from creature to overhead cover, upright masses, and ground."],"trigger_roots":["ن ظ ر","ء ب ل","خ ل ق"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_measured_habitat","source_type":"hft","support_id":"sup_9ebc421e82623e106329","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000217/B001","root_000582/B001","root_000703/B001","root_000745/B004","root_001507/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground opposite the sky supplies the system's bottom member.","root":"ء ر ض","source_ref":"88:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000703","role":"Level extension supplies the horizontal operation complementary to raising and erecting.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000745","role":"What rises and shades supplies an overhead covering member.","root":"س م و","source_ref":"88:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Lifting something upward supplies the operation that establishes the top member.","root":"ر ف ع","source_ref":"88:18","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000217","role":"A high solid aggregation supplies resistant vertical mass between sky and ground.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Setting something upright and prominent supplies the operation that establishes the vertical masses.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"changed_reading":{"after":"The earth's extension is its relational job as the lower horizontal member of a raised and erected world.","before":"The earth's flatness is an isolated proposition."},"confidence":"strong","mechanism":"An overhead cover is raised, hard masses are erected, and the lower member is extended. These are complementary operations in one vertical architecture, so surfacing names the horizontal role of earth within a coordinated system.","model_id":"delta_vertical_architecture","reader_inference":"The packet supplies an overhead cover, upward lifting, solid height, upright erection, lower ground, and level extension; I assemble them into a spatial system. A live alternative reads the list as independent marvels without architectural interdependence.","status":"strengthened","structural_cues":["The same directional and passive syntax coordinates sky, mountains, and earth.","The operations differ by member: raising above, erecting vertically, and extending below."],"trigger_roots":["س م و","ر ف ع","ج ب ل","ن ص ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_vertical_architecture","source_type":"hft","support_id":"sup_68820d785ed9e8cc2d15","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000516/B009","root_000703/B001","root_000704/B003","root_001520/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000025","role":"Ordinary lower ground supplies evidence continuously available to embodied observers.","root":"ء ر ض","source_ref":"88:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000703","role":"The broad visible plane supplies the inspectable form that can prompt recollection.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001520","role":"Directed sight or insight supplies the observer's active engagement with the sign.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]},{"branch_id":"B009","mapped_root_id":"root_000516","role":"A reminder that causes recollection supplies the pedagogical function of the visible surface.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"The controlling overseer supplies the coercive mode explicitly denied after the reminder.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"The verse makes the familiar ground into an open-ended visual reminder whose process must be attended to rather than compelled as a conclusion.","before":"The verse asserts a fact about terrain."},"confidence":"medium","mechanism":"The ground's made surface is offered to directed attention, then the discourse moves to reminding while denying controlling surveillance. The focus therefore works as accessible mnemonic evidence rather than a proposition imposed by force.","model_id":"delta_visible_reminder","reader_inference":"The packet supplies observation, reminder, and denied control; I assign the visible surface a mnemonic rather than coercive function. A live alternative limits the non-control statement to the messenger and gives it no bearing on how the earth question operates.","status":"new","structural_cues":["The repeated branchless interrogative root in verses 17-20 sustains process-focused attention without supplying a branch citation.","The command to remind and denial of control immediately follow the earth question."],"trigger_roots":["ن ظ ر","ذ ك ر","س ط ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_visible_reminder","source_type":"hft","support_id":"sup_653cc76172c0f339f13e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000703/B006","root_001307/B003","root_001307/B008","root_001684/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000025","role":"Fertile ground supplies the medium in which concealment can become germination.","root":"ء ر ض","source_ref":"88:20","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000703","role":"Vegetation spreading visibly over the ground supplies the disclosed result of productive covering.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B007","mapped_root_id":"root_001684","role":"Turning away supplies the directional refusal that converts concealment into evasion.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001307","role":"Hiding truth supplies the epistemically destructive form of covering.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]},{"branch_id":"B008","mapped_root_id":"root_001307","role":"Covering seed supplies the materially productive form of the same action.","root":"ك ف ر","source_ref":"88:23","source_word_indices":["4"]}],"changed_reading":{"after":"The earth's surface dramatizes two kinds of cover: one that incubates emergence and one that suppresses recognition.","before":"The earth's surface simply lies above what is beneath it."},"confidence":"exploratory","mechanism":"The same material act of covering can hide truth or protect seed until growth emerges. Joined to fertile earth and a ground-spreading plant, this makes the surfaced earth a test case in morally and causally divergent concealment.","model_id":"delta_productive_or_occluding_cover","reader_inference":"The packet supplies fertile ground, spreading growth, turning away, truth-concealment, and seed-covering; I infer a contrast between generative and evasive concealment. A live alternative treats the agricultural branch as an etymological side image with no role in the focus.","status":"new","structural_cues":["The discourse moves directly from looking and reminding to turning away and covering.","The focus surface is both what covers depth and where buried growth becomes visible."],"trigger_roots":["و ل ي","ك ف ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_productive_or_occluding_cover","source_type":"hft","support_id":"sup_30996586adcb86125b8f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000025/B002","root_000703/B006","root_001650/B003","root_001684/B010"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000025","role":"Fertile ground supplies the receptive medium on which rain can leave living marks.","root":"ء ر ض","source_ref":"88:20","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000703","role":"A plant spreading along the ground supplies the visible inscription across the surface.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001650","role":"The non-dominant mapping's first rain marks the earth with vegetation, supplying the initial inscription.","root":"س م و","source_ref":"88:18","source_word_indices":["2"]},{"branch_id":"B010","mapped_root_id":"root_001684","role":"Rain following the first marking rain supplies a successive layer in the surface-making process.","root":"و ل ي","source_ref":"88:23","source_word_indices":["3"]}],"changed_reading":{"after":"The earth's visible face is repeatedly written into being by rain and the vegetation that follows.","before":"The earth receives a finished surface once."},"confidence":"exploratory","containment":"This is surprising because it depends on the non-dominant mapped inventory of the sky root and a later rain branch activated from turning. It remains anchored in the focus's fertile-earth and ground-spreading-plant branches, while sequential rains provide a concrete mechanism for vegetation to mark the visible plane. Downstream prose should label it a split-root, cross-domain activation rather than a direct gloss of the focus verb.","focus_anchor":"Fertile earth at word 2 and vegetation spreading along ground at word 4 can receive visible marks made by successive rains.","outlier_id":"outlier_rain_written_surface"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_rain_written_surface","source_type":"hft","support_id":"sup_9328151575867451fa13","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":4,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":4,"target_morphology_supplied":false},"branch_refs":["root_000318/B001","root_000516/B008","root_000703/B005","root_000704/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000703","role":"The flat working place supplies the material tablet on which the analogy is anchored.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]},{"branch_id":"B008","mapped_root_id":"root_000516","role":"A document establishing a right supplies durable recording rather than fleeting recollection.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_000704","role":"An aligned written line supplies ordered inscription across the flat support.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and accounting supply the operation that reads and evaluates the inscribed record.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"The earth can be imagined as a legible working surface on which action leaves ordered traces available to account.","before":"The earth is a neutral floor for action."},"confidence":"exploratory","containment":"This is surprising because writing and accounting are activated from branch-distant context roots rather than from the ordinary sense of the focus. It remains anchored in the focus branch of a flat working surface, which can materially host ordered marks, while document, line, and count form a coherent recording mechanism. Downstream prose should present it as a ledger analogy, not as a lexical translation.","focus_anchor":"The surfacing verb at word 4 has a branch for a flat working place or mat capable of bearing arranged marks.","outlier_id":"outlier_surface_as_ledger"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_surface_as_ledger","source_type":"hft","support_id":"sup_32dede5392b658222a5a","trust":"legacy_unbound"}]}
</lane_packet_json>
