# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **110:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s110-regular-20260911/s110/110_1/micro.discovery.json` and modify nothing
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

- No additional lane-specific procedure.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "110:1",
  "lane": "micro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["micro:stable-key"],
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
      "finding_ref": "micro:stable-key",
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
`micro:`. Accepted/narrowed candidates own dedicated findings. A represented
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
{"analysis_context":{"analysis_id":"s110-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"110:1","host_surah":110,"lane_context_refs":[],"ordered_context_refs":["110:0","110:2","110:3","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_30ab58e43c0fc20a78bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"110:1:4:1","qac_word_ref":"110:1:4","surface_ar":"ٱللَّهِ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":["sup_9efe16c4be1033ee5e3e"]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[{"candidate_id":"cand_08161fcc24c8918b349e","lane":"micro"},{"candidate_id":"cand_9eeb8452160d3ed27d2b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"110:1:4:1","qac_word_ref":"110:1:4","surface_ar":"ٱللَّهِ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":["sup_a2a6a26c6812ccce6e70","sup_de5d80415ab6704241b1"]},{"boundary":"Bu dal fiziksel açma, açılma ve açıklıkla sınırlıdır; başlangıç, yargı, zafer, araç veya saklama yeri anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B001","candidate_links":[{"candidate_id":"cand_08161fcc24c8918b349e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"fiziksel açma, açılma ve geniş açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kapalı olanın engelini kaldırıp içeriye ya da ardındakine erişim sağlama eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin üzerindekinden sıyrılarak görünür olması ve bitkinin açılması bu çekirdeğin kendiliğinden gerçekleşen görünümüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kapı, şişe ağzı, gedik veya beden geçidi gibi bir bölümün geniş ve açık oluşunu da anlatır."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kapalı bir şeyi açma, kendiliğinden açılıp görünme ve belirli bir girişin geniş açık oluşunu birlikte temsil eder.","boundary_detail":"Bu dal fiziksel açma, açılma ve açıklıkla sınırlıdır; başlangıç, yargı, zafer, araç veya saklama yeri anlamlarını içermez.","branch_image_ar":"انفراج المغلق واتساع المدخل","concept_gloss":"fiziksel açma, açılma ve geniş açıklık","contextual_glosses":[{"applicability":"Kapı, kilit veya kapalı eşya üzerindeki engelin kaldırıldığı eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kapalı olanın engelini kaldırıp erişim sağlama eylemini tam olarak korur."},"facet_ids":["F001"],"text":"açmak","usage_role":"general"},{"applicability":"Bir şey görünür duruma geldiğinde veya bir çiçek açtığında doğal bir metin içi karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kendiliğinden açılıp görünür olma değişimini eksiksiz biçimde korur."},"facet_ids":["F002"],"text":"açılmak","usage_role":"contextual"},{"applicability":"Kapı, kap ağzı, gedik veya beden geçidinin geniş açık oluşunun adlandırıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir girişin ya da ağzın geniş ve açık olma durumunu tam olarak korur."},"facet_ids":["F003"],"text":"geniş açıklık","usage_role":"explanatory"}],"definition":"Kapalı bir şeyi açarak erişilebilir duruma getirme, bir şeyin üzerindekinden sıyrılıp görünür olması veya bir girişin ya da ağzın geniş ve açık bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kapalı olanın engelini kaldırıp içeriye ya da ardındakine erişim sağlama eylemidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin üzerindekinden sıyrılarak görünür olması ve bitkinin açılması bu çekirdeğin kendiliğinden gerçekleşen görünümüdür."},{"facet_id":"F003","role":"specialization","statement":"Kapı, şişe ağzı, gedik veya beden geçidi gibi bir bölümün geniş ve açık oluşunu da anlatır."}],"identity_rationale":"Kaynak ifadesi kapanmanın karşıtı olan fiziksel açmayı, bir şeyin üzerindekinden sıyrılıp görünmesini ve giriş ya da ağız gibi bölümlerin geniş açıklığını birlikte gösterir. Verilen çerçeve bu çekirdeği ve ona bağlı durumları doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"fiziksel açma ve kapalılığı giderme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kapıyı, kilidi veya kapalı eşyayı açmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"açılmak; çiçeğin açması"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"geniş ve açık kapı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ağzı geniş, tıpasız ve kılıfsız şişe"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"açıklık veya gedik"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"idrar yolu geniş dişi deve"}],"lexicalization_note":"Bağımsız fiziksel açılma çekirdeği ile yalnız kapı, şişe ağzı ve benzeri yapılarda görülen özel genişlik anlamları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar fiziksel açma, açıklık, kenar, geçit ve öteki kök içi dallar bakımından değerlendirildi; sınırı en doğrudan keskinleştiren kapı açma komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kapı açma eylemine özgüdür; odak dal ise fiziksel kapalılığın giderilmesini ve bunun durum ya da genişlik sonuçlarını daha geniş biçimde kapsar.","focus_only":"Bu dal kilit ve eşya açmayı, görünür hale gelmeyi ve geniş açıklık durumunu da kapsar.","gloss":"kapıyı açma","neighbor_only":"Komşu dal yalnız kapıyı açmayı bildiren özel bir eylem anlatımıdır.","neighbor_ref":"root_000249/B006","relation_type":"near_synonym","shared_zone":"İki dal da kapalı bir kapının açılması eyleminde örtüşür."}],"source_phrase_ar":"خلاف الإغلاق ونقيض الإغلاق (maqayis;ayn;jamhara;sihah;tahdhib;mufradat)؛ فتحت الباب وغيره فتحا (maqayis;sihah)؛ كل شيء انكشف عن شيء فقد انفتح عنه ومنه تفتح النور (jamhara)؛ باب فتح أي واسع مفتوح (maqayis;ayn;sihah;tahdhib;mufradat)؛ قارورة فتح واسعة الرأس والفتحة الفرجة والفتوح الناقة الواسعة الإحليل (sihah;tahdhib)","source_summary":"Kaynaklar kapanmanın karşıtı olan açma üzerinde birleşir; kapı ve kilit gibi kapalı şeylerin açılmasını, üzeri örtülü olanın görünmesini ve belirli giriş ya da ağızların açık bulunmasını bu anlam alanında toplar. Camhara çiçeğin açmasını bu kendiliğinden açılma alanında kaydeder; Sıhah ve Tehzib geniş ağızlı şişe ve geniş beden geçidi örneklerini açıklık alanına bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه فتح الباب والقفل والمتاع، وانكشاف الشيء عن الشيء، واتساع الباب أو فم القارورة أو الفرجة أو مجرى الجسد.","what_is_not_ar":"ليس هو الحكم بين الخصوم، ولا النصر، ولا الابتداء، ولا المفتاح أو الخزانة."},"support_links":["sup_a2a6a26c6812ccce6e70"]},{"boundary":"Bu dal başlangıç ve açılışla ilgilidir; fiziksel açma, yargılama veya zafer anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"sonrasını başlatan ilk bölüm veya eylem","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünün ilk bölümü ya da sonraki süreci başlatan ilk eylemdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kitabın açılış bölümü ve kutsal metindeki bölümlerin başlangıçları bu anlamın metinsel uzmanlaşmalarıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İbadeti başlatan ilk yüceltme sözü, başlangıç işlevinin törensel bir örneğidir."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir bütünün başlangıç bölümünü hem de bir süreci başlatan ilk eylemi kapsayan genel karşılıktır.","boundary_detail":"Bu dal başlangıç ve açılışla ilgilidir; fiziksel açma, yargılama veya zafer anlamına genişletilmez.","branch_image_ar":"فاتحة الشيء ومبدؤه الذي يفتح ما بعده","concept_gloss":"sonrasını başlatan ilk bölüm veya eylem","contextual_glosses":[{"applicability":"Bir işin ilk anı veya bir bütünün ilk bölümü öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin ilk bölümünü veya ilk aşamasını doğal ve açık biçimde korur."},"facet_ids":["F001"],"text":"başlangıç","usage_role":"general"},{"applicability":"Bir kitabın ya da metinsel bölümün kendisinden sonrasını başlatan ilk kısmı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Metnin ilk kısmını ve sonraki içeriği başlatma işlevini tam olarak korur."},"facet_ids":["F002"],"text":"açılış bölümü","usage_role":"contextual"}],"definition":"Bir şeyin kendisinden sonrasını başlatan ilk bölümü veya bir işe girişme eylemidir; metinlerin ve ibadetin belirlenmiş açılışları bunun özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünün ilk bölümü ya da sonraki süreci başlatan ilk eylemdir."},{"facet_id":"F002","role":"specialization","statement":"Bir kitabın açılış bölümü ve kutsal metindeki bölümlerin başlangıçları bu anlamın metinsel uzmanlaşmalarıdır."},{"facet_id":"F003","role":"example","statement":"İbadeti başlatan ilk yüceltme sözü, başlangıç işlevinin törensel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi bir şeyin ilk bölümünü, kendisinden sonrasını başlatan açılışı ve bir işe başlama eylemini açıkça bir araya getirir. Kitap bölümleri ile ibadetin ilk sözü bu çekirdeğin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyin başlangıcı ve ilk bölümü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kitabın açılış bölümü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kutsal metindeki bölümlerin başlangıçları"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ibadeti başlatan ilk yüceltme sözü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir şeye başlamak ve girişmek"}],"lexicalization_note":"Genel başlangıç çekirdeği korunur; kitap, bölüm ve ibadet başlangıçlarına ait özel kullanımlar bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar genel başlama, ilk bölüm, süreklilik, bitiş ve diğer kök içi dallar açısından değerlendirildi; genel başlangıç komşusu en yararlı sınırı verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, sonrasını başlatan ilk bölüm ya da açılış işleviyle sınırlanır; komşu dal ise başlangıcı daha genel bir olay ve yaratma süreci olarak da kapsar.","focus_only":"Bu dal ilk bölümün kendisinden sonrasını açma işlevini ve belirlenmiş açılış bölümlerini öne çıkarır.","gloss":"başlama ve başlangıç","neighbor_only":"Komşu dal yaratılışın başlaması dahil daha genel başlama ve yeniden başlatma alanına uzanır.","neighbor_ref":"root_000091/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin veya sürecin ilk anını anlatabilir."}],"source_phrase_ar":"فواتح القرآن أوائل السور (maqayis;ayn;tahdhib)؛ كل ما بدأت به فقد استفتحته وبه سميت الحمد فاتحة الكتاب (jamhara)؛ فاتحة الشيء أوله (sihah)؛ فاتحة كل شيء مبدؤه الذي يفتح به ما بعده وافتتح فلان كذا إذا ابتدأ به (mufradat)؛ افتتاح الصلاة التكبيرة الأولى (ayn)","source_summary":"Kaynaklar bu anlamı bir şeyin ilki ve sonrasını açan başlangıcı olarak verir; işe başlama eylemini, kitabın açılışını ve metin bölümlerinin ilk kısımlarını aynı çekirdeğe bağlar. Ayn, ibadetin ilk tekbirle açılmasını başlangıç kullanımının özel örneği olarak açıklar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه ابتداء الشيء، وفاتحة الكتاب، وفواتح السور، وافتتاح الصلاة بالتكبيرة الأولى.","what_is_not_ar":"ليس هو فتح الباب حسيا، ولا الحكم، ولا النصر."},"support_links":[]},{"boundary":"Bu dal taraflar arasındaki uyuşmazlığı kararla ayırır; askeri zafer veya yalnız yardım isteme anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B003","candidate_links":[{"candidate_id":"cand_9eeb8452160d3ed27d2b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"uyuşmazlığı hükümle çözüme bağlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Uyuşmazlık içindeki taraflar arasında hüküm verip anlaşmazlığı sonuçlandırmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir davadaki kapalı noktaları ayırıp doğru karar yerini belirginleştirmek yargısal çözümün sonucudur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hüküm, yargı işi ve bu işi yapan yargıç için kullanılan adlar eylem çekirdeğine bağlı kullanımlardır."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Taraflar arasında yargısal karar verilerek anlaşmazlığın sonuçlandırıldığı çekirdeği temsil eder.","boundary_detail":"Bu dal taraflar arasındaki uyuşmazlığı kararla ayırır; askeri zafer veya yalnız yardım isteme anlamı değildir.","branch_image_ar":"فصل الإغلاق بالحكم والقضاء","concept_gloss":"uyuşmazlığı hükümle çözüme bağlama","contextual_glosses":[{"applicability":"Bir yargı merciinin çekişen tarafların uyuşmazlığı hakkında karar verdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çekişen taraflar arasında hüküm verme eylemini eksiksiz olarak korur."},"facet_ids":["F001"],"text":"aralarında hüküm vermek","usage_role":"general"},{"applicability":"Belirsiz bir yargı işinin ayrıştırılıp kesin bir sonuca ulaştırılması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Davadaki belirsizliği giderme ve işi kararla sonuçlandırma aşamalarını korur."},"facet_ids":["F002"],"text":"davayı karara bağlamak","usage_role":"contextual"}],"definition":"Çekişen taraflar arasındaki uyuşmazlığı hüküm vererek ayırma, davayı karara bağlama ve belirsizliği giderme eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Uyuşmazlık içindeki taraflar arasında hüküm verip anlaşmazlığı sonuçlandırmaktır."},{"facet_id":"F002","role":"specialization","statement":"Bir davadaki kapalı noktaları ayırıp doğru karar yerini belirginleştirmek yargısal çözümün sonucudur."},{"facet_id":"F003","role":"associated_use","statement":"Hüküm, yargı işi ve bu işi yapan yargıç için kullanılan adlar eylem çekirdeğine bağlı kullanımlardır."}],"identity_rationale":"Kaynak ifadesi çekişen taraflar arasında hüküm vermeyi, davayı sonuçlandırmayı ve doğru karar yerini açığa çıkarmayı aynı yargısal çekirdekte toplar. Hükmeden kişi için kullanılan adlar bu eyleme bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çekişen taraflar arasında hüküm vermek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"hüküm ve yargı işi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hükmeden ve karar veren"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hükmeden yargıç"}],"lexicalization_note":"Yargıyla çözme çekirdeği korunur; taraflar arasında hüküm verme yapısı ile yargıç ve karar adları ayrı uzmanlaşmalar olarak ele alınır.","neighbor_coverage_note":"Bütün adaylar yargı, hesap, adaletsizlik, kanıt, dava açma ve diğer kök içi dallar bakımından değerlendirildi; ayırıcı yargı komşusu en yakın sınırı gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal taraflar arasında hüküm verme sürecini ve yargı görevini öne çıkarır; komşu dal ise kararın doğru ile yanlışı ayıran kesinliğini öne çıkarır.","focus_only":"Bu dal uyuşmazlığı çözme eyleminin yanı sıra hüküm ve yargıç adlarını da kapsar.","gloss":"ayırıcı yargı","neighbor_only":"Komşu dal kararın doğruyu yanlıştan kesin biçimde ayırması ve sözün belirleyici niteliği üzerinde durur.","neighbor_ref":"root_001159/B002","relation_type":"near_synonym","shared_zone":"İki dal da yargısal bir kararla uyuşmazlığı kesin biçimde sonuçlandırır."}],"source_phrase_ar":"الفتح والفتاحة الحكم والله الفاتح أي الحاكم (maqayis)؛ الفتح أن تحكم بين قوم يختصمون إليك والفتاح الحاكم (ayn)؛ فتح فلان بين بني فلان إذا حكم بينهم والفتاح العليم (jamhara)؛ افتح بيننا أي احكم والفتاحة الحكم (sihah)؛ الفتاح الحكومة والقاضي لأنه يفتح مواضع الحق (tahdhib)؛ فتح القضية فتاحا فصل الأمر فيها وأزال الإغلاق عنها (mufradat)","source_summary":"Kaynaklar çekişen kişiler arasında hüküm verme ve davayı ayırıp sonuçlandırma üzerinde birleşir. Karar verme işi ile hükmeden veya yargıç olan kişi için kullanılan adları da bu yargısal işleve bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحكم بين المختصمين، القضاء، الفتاحة بمعنى الحكومة، والفتاح بمعنى الحاكم أو القاضي.","what_is_not_ar":"ليس هو النصر العسكري أو طلب الظفر إلا حيث تنص المصادر على احتمال الحكم في اللفظ نفسه."},"support_links":["sup_de5d80415ab6704241b1"]},{"boundary":"Bu dal üstün gelme ve zafer alanındadır; taraflar arasında hüküm verme anlamı bağlamdan bağımsız olarak buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"üstün gelerek zafere ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rakibe üstün gelerek zafer kazanmak veya bir tarafın kazanmasını sağlamaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaşta düşman ülkesini ele geçirmek, zafer çekirdeğinin askeri uzmanlaşmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir rakibe karşı üstünlük ve zafer istemek, sonucun kendisi değil o sonuca yönelen yardım talebidir."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Rakibin yenildiği ve üstünlüğün zafer sonucuna ulaştığı temel anlam için kullanılır.","boundary_detail":"Bu dal üstün gelme ve zafer alanındadır; taraflar arasında hüküm verme anlamı bağlamdan bağımsız olarak buraya taşınmaz.","branch_image_ar":"انفتاح الغلبة والظفر","concept_gloss":"üstün gelerek zafere ulaşma","contextual_glosses":[{"applicability":"Bir rakibe karşı üstün gelmenin başarı sonucuyla anlatıldığı genel bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün gelmenin ulaştığı zafer sonucunu doğal biçimde ve eksiksiz korur."},"facet_ids":["F001"],"text":"zafer kazanmak","usage_role":"general"},{"applicability":"Zaferin askeri olarak bir ülkenin denetimini alma biçiminde gerçekleştiği bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Askeri üstünlüğü ve ülkenin denetimini ele geçirme sonucunu birlikte korur."},"facet_ids":["F002"],"text":"düşman ülkesini ele geçirmek","usage_role":"contextual"},{"applicability":"Bir rakibe karşı üstün gelmek için yüce bir güçten yardım istendiği yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zafer sonucunun kendisini değil, o sonuca yönelik yardım talebini korur."},"facet_ids":["F003"],"text":"zafer dilemek","usage_role":"contextual"}],"definition":"Bir rakibe üstün gelerek zafer kazanma veya bir tarafı zafere ulaştırmadır; düşman ülkesini ele geçirme ve birine karşı yardım isteyerek zafer arama bunun özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rakibe üstün gelerek zafer kazanmak veya bir tarafın kazanmasını sağlamaktır."},{"facet_id":"F002","role":"specialization","statement":"Savaşta düşman ülkesini ele geçirmek, zafer çekirdeğinin askeri uzmanlaşmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bir rakibe karşı üstünlük ve zafer istemek, sonucun kendisi değil o sonuca yönelen yardım talebidir."}],"identity_rationale":"Kaynak ifadesi zafer kazanmayı, bir tarafı üstün kılmayı, savaş ülkesini ele geçirmeyi ve üstünlük istemeyi açıkça aynı başarı çekirdeğinde toplar. Yargı ihtimali yalnız bağlamın ayrıca gerektirdiği yerde düşünülmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"zafer, üstün gelme veya savaşta ele geçirme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"düşman ülkesini yenerek ele geçirmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"Tanrı'dan birine karşı zafer istemek"}],"lexicalization_note":"Genel zafer çekirdeği ile askeri ele geçirme ve birine karşı zafer isteme yapıları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar genel üstünlük, baskıyla yenme, özel yarışma kullanımları, savaş eylemleri ve diğer kök içi dallar açısından değerlendirildi; genel yenip kazanma komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zafer sonucunu ve ona bağlı askeri ya da isteme yapılarını taşır; komşu dal ise baskın gelme yoluyla herhangi bir şeyi kazanmayı daha genel anlatır.","focus_only":"Bu dal askeri ele geçirmeyi, bir tarafı zafere ulaştırmayı ve zafer istemeyi de kapsar.","gloss":"yenip kazanma","neighbor_only":"Komşu dal bir şeyi kazanma ve rakibi baskıyla yenme alanını daha genel biçimde kapsar.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"İki dal da rakibe üstün gelerek başarıya ulaşma çekirdeğinde örtüşür."}],"source_phrase_ar":"الفتح النصر والإظفار واستفتحت استنصرت (maqayis)؛ الفتح افتتاح دار الحرب والفتح النصرة واستفتحت الله سألته النصر (ayn)؛ الاستفتاح الاستنصار والفتح النصر (sihah)؛ إن تستنصروا فقد جاءكم النصر (tahdhib)؛ يحتمل النصرة والظفر والاستفتاح طلب الفتح أو الفتاح وطلب الظفر (mufradat)","source_summary":"Kaynaklar zafer, üstün gelme ve bir tarafı kazandırma anlamlarında birleşir; savaş ülkesinin ele geçirilmesini ve bir rakibe karşı zafer istenmesini de bu çekirdeğe bağlı kullanımlar olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النصر، الإظفار، فتح دار الحرب، والاستفتاح بمعنى طلب النصر أو الظفر.","what_is_not_ar":"ليس هو الحكم القضائي إلا في الألفاظ التي صرحت المصادر بترددها بين القضاء والنصر."},"support_links":[]},{"boundary":"Çekirdek çıkan veya akan sudur; sulanan ürün ve ilk yağmur adları bağımlı kullanımlardır, çekirdeğin zorunlu parçaları değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B005","candidate_links":[{"candidate_id":"cand_12b070938f64dc090076","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"kaynaktan çıkıp akan su","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir gözeden ya da başka bir çıkış yerinden dışarı çıkan sudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Akarsu yatağında ilerleyen su ve nehrin kendisi, çıkan su çekirdeğinin akış alanına uzanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Nehir suyunun ulaşıp suladığı ekin veya hurmalık, suyun kendisi değil ona bağlı tarımsal kullanımdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Mevsim yağmurlarının ilki için kullanılan özel ad, akan su çekirdeğine bağlı ayrı bir adlandırmadır."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir çıkış yerinden doğan ve akış halinde ilerleyen su çekirdeğini temsil eder.","boundary_detail":"Çekirdek çıkan veya akan sudur; sulanan ürün ve ilk yağmur adları bağımlı kullanımlardır, çekirdeğin zorunlu parçaları değildir.","branch_image_ar":"انبعاث الماء من منفذه","concept_gloss":"kaynaktan çıkıp akan su","contextual_glosses":[{"applicability":"Suyun bir gözeden ya da başka bir çıkıştan doğup aktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun kaynaktan çıkma ve akma özelliklerini doğal bir karşılıkla korur."},"facet_ids":["F001","F002"],"text":"akan kaynak suyu","usage_role":"general"},{"applicability":"Suyun kendisinin değil, nehir suyunun ulaştırıldığı ekin veya hurmalığın anlatıldığı yapıya özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tarımsal ürünü ve bu ürünün nehir suyuyla sulanması koşulunu birlikte korur."},"facet_ids":["F003"],"text":"nehir suyuyla sulanan ekin","usage_role":"explanatory"},{"applicability":"Yılın belirli mevsiminde gelen yağmurların ilkini adlandıran özel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmurun belirli mevsime ait olmasını ve o dizide ilk gelmesini korur."},"facet_ids":["F004"],"text":"mevsimin ilk yağmuru","usage_role":"contextual"}],"definition":"Bir kaynaktan çıkan veya akarsu yatağında ilerleyen sudur. Aynı ad, nehir suyuyla sulanan ekinlere ve mevsimin ilk yağmuruna bağlı olarak da kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir gözeden ya da başka bir çıkış yerinden dışarı çıkan sudur."},{"facet_id":"F002","role":"extension","statement":"Akarsu yatağında ilerleyen su ve nehrin kendisi, çıkan su çekirdeğinin akış alanına uzanır."},{"facet_id":"F003","role":"associated_use","statement":"Nehir suyunun ulaşıp suladığı ekin veya hurmalık, suyun kendisi değil ona bağlı tarımsal kullanımdır."},{"facet_id":"F004","role":"source_variant","statement":"Mevsim yağmurlarının ilki için kullanılan özel ad, akan su çekirdeğine bağlı ayrı bir adlandırmadır."}],"identity_rationale":"Kaynak ifadesi bir kaynaktan çıkan ya da akarsuda ilerleyen suyu çekirdek olarak verir; nehir suyuyla sulanan ürünler ile mevsimin ilk yağmuru aynı adın bağlı kullanımlarıdır. Bu nedenle suyun çıkışı çerçevesi geçerlidir, ancak bütün kullanımları tek bir çıkış olayı saymamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kaynaktan çıkan veya akarsuda ilerleyen su"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"nehir suyuyla sulanan ekin veya hurmalık"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"mevsim yağmurlarının ilki"}],"lexicalization_note":"Çıkan ve akan su anlamı, nehir suyuyla sulanan ürün yapısından ve ilk mevsim yağmurunun özel adından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar kaynak, akış, yağmur, nem, kesilme, sıcak su ve diğer kök içi dallar açısından değerlendirildi; yerden kaynayan su en yakın çekirdek karşılaştırmasını sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal çıkan suyu akarsu akışına ve bağlı adlandırmalara uzatır; komşu dal ise yerden kaynama olayını, kaynağı ve kaynaktan oluşan su yolunu öne çıkarır.","focus_only":"Bu dal akarsuda ilerleyen suyu ve sulanan ürün ile ilk yağmur adlarını da kapsar.","gloss":"yerden kaynayan su","neighbor_only":"Komşu dal özellikle suyun yerden veya gözeden kaynamasını, kaynağı ve bol sulu küçük akarsuyu kapsar.","neighbor_ref":"root_001469/B001","relation_type":"near_synonym","shared_zone":"İki dal da suyun bir kaynaktan çıkıp görünür hale gelmesinde örtüşür."}],"source_phrase_ar":"الفتح الماء يخرج من عين أو غيرها (maqayis)؛ الفتح الماء يجري من عين أو غيرها (sihah)؛ الفتح النهر وما جرى في الأنهار من الماء وما سقي فتحا وأول مطر الوسمي الفتوح (tahdhib)","source_summary":"Kaynaklar bir gözeden veya başka bir yerden çıkan ve akarsularda ilerleyen suyu verir; çekirdek, çıkan veya akan su üzerindedir. Tehzib nehir suyuyla sulanan ekin ve hurmalıkları ve mevsim yağmurlarının ilkini aynı su alanındaki özel kullanımlar olarak kaydeder.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الماء الخارج من عين أو غيرها، ماء النهر أو ما جرى في الأنهار، وما فتح إليه ماء النهر من الزروع والنخيل، وأول مطر الوسمي المسمى الفتوح.","what_is_not_ar":"ليس هو فتح الباب، ولا النصر، ولا الحكم، ولا الخزانة."},"support_links":["sup_082364b131bcf399f88b"]},{"boundary":"Bu dal erişim sağlayan araç veya yoldur; servetin saklandığı yer ya da saklanan servetin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001124/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"kapalıyı açan araç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kapıyı, kilidi veya başka bir kapalı şeyi açmaya yarayan somut araçtır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bilinmeyen bir alana erişmeyi mümkün kılan bilgi veya yol, açma aracının düşünsel uzantısıdır."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kapı, kilit veya başka bir kapalı nesne üzerinde doğrudan kullanılan somut araç için uygundur.","boundary_detail":"Bu dal erişim sağlayan araç veya yoldur; servetin saklandığı yer ya da saklanan servetin kendisi değildir.","branch_image_ar":"آلة الوصول إلى المغلق","concept_gloss":"kapalıyı açan araç","contextual_glosses":[{"applicability":"Kapı, kilit veya benzeri kapalı bir düzeni açan somut araçtan söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kapalı bir düzeni açmaya yarayan somut araç anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"anahtar","usage_role":"general"},{"applicability":"Bilinmeyen bir konuya ulaşmayı sağlayan bilgi veya yöntemin anlatıldığı özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilinmeyen alana eriştiren araçsal yolu düşünsel düzeyde korur."},"facet_ids":["F002"],"text":"gizliye erişme yolu","usage_role":"explanatory"}],"definition":"Kapı, kilit veya başka bir kapalı şeyi açarak erişim sağlayan araçtır; bilinmeyene ulaşmayı mümkün kılan yol da buna bağlı düşünsel bir uzantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kapıyı, kilidi veya başka bir kapalı şeyi açmaya yarayan somut araçtır."},{"facet_id":"F002","role":"extension","statement":"Bilinmeyen bir alana erişmeyi mümkün kılan bilgi veya yol, açma aracının düşünsel uzantısıdır."}],"identity_rationale":"Kaynak ifadesi kapı, kilit veya başka kapalı şeyleri açmaya yarayan aracı temel anlam olarak verir ve bilinmeyene eriştiren şeyi bunun düşünsel uzantısı sayar. Araç ile açılan yerin kendisi birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kapıyı, kilidi veya başka bir kapalı şeyi açan anahtar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kilitli olanı açmaya yarayan araç"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bilinmeyene erişmeyi sağlayan yollar"}],"lexicalization_note":"Somut açma aracı çekirdeği korunur; bilinmeyene erişme yapısındaki düşünsel uzantı yalnız kendi bağlamında ele alınır.","neighbor_coverage_note":"Bütün adaylar genel araç, anahtar, kapıcı, örtü, koruyucu nesne, açma eylemi ve diğer kök içi dallar bakımından değerlendirildi; anahtar ile saklama yerini birleştiren komşu en keskin sınırı verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği açma aracıdır ve soyut erişim yoluna uzanır; komşu dal ise aynı araç alanını saklama yeri ve koruma düzeniyle birlikte kapsar.","focus_only":"Bu dal her türlü kapalı şeyi açan aracı ve bilinmeyene eriştiren düşünsel yolu kapsar.","gloss":"anahtar ve saklama yeri","neighbor_only":"Komşu dal anahtarın yanında saklama yerlerini ve onların koruyucu çevresini de kapsar.","neighbor_ref":"root_001249/B006","relation_type":"near_synonym","shared_zone":"İki dal da bir kilidi açarak korunan şeye erişim sağlayan araçta örtüşür."}],"source_phrase_ar":"المفاتيح جمع المفتاح الذي يفتح به المغلاق (ayn)؛ المفتاح معروف (jamhara)؛ المفتاح مفتاح الباب وكل مستغلق (sihah)؛ الذي يفتح به المغلاق مفتح بكسر الميم ومفتاح (tahdhib)؛ المفتح والمفتاح ما يفتح به ومفاتح الغيب ما يتوصل به إلى غيبه (mufradat)","source_summary":"Kaynaklar kapı, kilit ve her türlü kapalı şeyi açmaya yarayan somut araç üzerinde birleşir. Müfredat, bilinmeyene eriştiren şeyi aynı araç düşüncesinin soyut uzantısı olarak açıklar.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المفتاح والمفتح بكسر الميم، أي ما يفتح به الباب أو المغلاق أو كل مستغلق، وما يتوصل به إلى الغيب في استعمال المفردات.","what_is_not_ar":"ليس هو الخزانة أو الكنز نفسه حيث تفسر المفاتح بالخزائن، ولا هو الفاتحة بمعنى البداية."},"support_links":[]},{"boundary":"Bu dal saklama yeri veya içindeki servettir; o yeri açan araç anlamı ayrı tutulur.","branch_kind":"bare","branch_ref":"root_001124/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"servet saklanan yer veya içindeki servet","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Değerli malların korunduğu saklama yeri veya bu yerlerin bütünü anlamına gelir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalar yeri değil, gömüyü, servet türlerini veya saklama yerlerindeki malı öne çıkarır."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların yer ile içerik arasında değişen açıklamalarını tek bir tarafı zorunlu kılmadan temsil eder.","boundary_detail":"Bu dal saklama yeri veya içindeki servettir; o yeri açan araç anlamı ayrı tutulur.","branch_image_ar":"الخزانة المنفتحة على ما فيها","concept_gloss":"servet saklanan yer veya içindeki servet","contextual_glosses":[{"applicability":"Değerli malların korunduğu yer veya bu yerlerin çoğulu öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Servetin korunaklı bir yerde saklanması ve yer anlamının öne çıkmasını korur."},"facet_ids":["F001"],"text":"servet deposu","usage_role":"general"},{"applicability":"Saklama yerinden çok içindeki değerli mal ya da biriktirilmiş servet kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerin içeriği olan değerli malı ve biriktirilmiş servet seçeneğini korur."},"facet_ids":["F002"],"text":"gömü veya biriktirilmiş servet","usage_role":"contextual"}],"definition":"Servetin saklandığı korunaklı yer, biriktirilmiş değerli mal veya bu yerde bulunan servettir; kaynaklardaki açıklamalar yer ile içeriği farklı biçimlerde öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Değerli malların korunduğu saklama yeri veya bu yerlerin bütünü anlamına gelir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalar yeri değil, gömüyü, servet türlerini veya saklama yerlerindeki malı öne çıkarır."}],"identity_rationale":"Kaynak ifadesi açılmış bir yer tasviri kurmaktan çok servetin saklandığı yeri, gömüyü, bu yerlerin çoğulunu veya içlerindeki malı adlandırır. Dal korunabilir, ancak tanımın varsayılan açılma imgesini değil bu yer ve içerik seçeneklerini öne çıkarması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"servet saklanan yer veya gömü"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"servet depoları, gömüler veya bunlardaki mallar"}],"lexicalization_note":"Bağımsız yer ve içerik anlamı tanımlanır; anahtar anlamı veya yalnız belirli bir söz öbeğine bağlı okuma içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar biriktirilmiş mal, gömü, edinme, koruma, değerli eşya, anahtar ve diğer kök içi dallar açısından değerlendirildi; yer ile anahtarı birleştiren komşu en yararlı ayrımı sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ile içerik arasındaki adlandırmaya yoğunlaşır; komşu dal ise saklama yerini ona eriştiren anahtar ve çevresel koruma düzeniyle aynı alanda toplar.","focus_only":"Bu dal saklama yerinin kendisini veya içindeki serveti anlatır ve açma aracını çekirdeğe katmaz.","gloss":"anahtarlar ve depolar","neighbor_only":"Komşu dal anahtarı, saklama yerini ve koruma ya da kuşatma ilişkisini daha geniş biçimde birleştirir.","neighbor_ref":"root_001249/B006","relation_type":"near_synonym","shared_zone":"İki dal da değerli şeylerin korunduğu saklama yerleri alanında örtüşür."}],"source_phrase_ar":"المفتح الخزانة ومفاتحه الكنوز وصنوف أمواله (ayn)؛ المفتح الكنز ومفاتحه كنوزه (jamhara)؛ المفتح الخزانة ومفاتحه كنوزه وخزائنه وما في الخزائن من مال (tahdhib)؛ مفاتح خزائنه وقيل الخزائن أنفسها (mufradat)","source_summary":"Kaynaklar bu kullanımı servet saklanan yer ile onun içeriği arasında açıklar. Açıklamalar korunaklı depo, gömü, bu yerlerin çoğulu, servet türleri ve bu yerlerdeki mal seçeneklerini birlikte kaydeder.","sources":["AY","JA","TA","MU"],"what_is_ar":"يدخل فيه المفتح بمعنى الخزانة أو الكنز، وتفسير مفاتحه في آية قارون بالكنوز أو الخزائن أو المال الذي في الخزائن.","what_is_not_ar":"ليس هو المفتاح الآلة إذا كان المراد ما يفتح به المغلاق."},"support_links":[]},{"boundary":"Anlam yalnız kanıtlanan yapılarda güçlük giderme, bilgi açma ve okuma desteğidir; genel bir soyut açma anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001124/B008","candidate_links":[{"candidate_id":"cand_30ab58e43c0fc20a78bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"güçlüğü giderme ve bilgiyi erişilir kılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kanıtlanan yapılarda çözülmesi güç bir durumu giderip kişiye rahatlık veya erişim sağlama işlemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkıntıyı hafifletme ve maddi yoksunluğu bağışla giderme, güçlük çözmenin duygusal ve maddi gerçekleşmeleridir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Anlaşılması güç bilgiyi açıklama veya bir kişiye bir şeyi bildirip kavratma, bilgiye erişim sağlayan gerçekleşmelerdir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Okuyan kişiye takıldığı sözü hatırlatmak, bilgiye erişim çekirdeğine bağlı özel bir yardım eylemidir."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan söz öbeklerinde fiziksel olmayan engelin giderildiği genel ilişkiyi temsil eder.","boundary_detail":"Anlam yalnız kanıtlanan yapılarda güçlük giderme, bilgi açma ve okuma desteğidir; genel bir soyut açma anlamına genişletilmez.","branch_image_ar":"انكشاف الانغلاق المعنوي بالبصيرة أو التفريج","concept_gloss":"güçlüğü giderme ve bilgiyi erişilir kılma","contextual_glosses":[{"applicability":"Kaygı veya bunaltının hafifletilip kişiye rahatlık sağlandığı özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duygusal güçlüğün kaldırılmasını ve rahatlama sonucunu birlikte korur."},"facet_ids":["F002"],"text":"sıkıntıyı gidermek","usage_role":"contextual"},{"applicability":"Bir kişiye bilinmeyen veya anlaşılması güç bir konu öğretilip kavratıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgiyi kişiye ulaştırma ve anlaşılır hale getirme işlemlerini birlikte korur."},"facet_ids":["F003"],"text":"bir şeyi bildirip açıklamak","usage_role":"contextual"},{"applicability":"Okuma sırasında duraklayan kişiye sonraki sözü hatırlatarak yardım etme bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Okuyan kişinin takılmasını ve ona gerekli sözü vererek yardım edilmesini korur."},"facet_ids":["F004"],"text":"okuyana takıldığı yeri söylemek","usage_role":"explanatory"}],"definition":"Yalnız belirtilen söz öbeklerinde, zihinsel, duygusal veya maddi bir güçlüğü gidermek ya da bilgiyi erişilebilir kılmaktır. Buna sıkıntıyı hafifletme, yoksunluğu giderme, bilgiyi açıklama ve okuyana takıldığı yeri söyleme dahildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kanıtlanan yapılarda çözülmesi güç bir durumu giderip kişiye rahatlık veya erişim sağlama işlemidir."},{"facet_id":"F002","role":"specialization","statement":"Sıkıntıyı hafifletme ve maddi yoksunluğu bağışla giderme, güçlük çözmenin duygusal ve maddi gerçekleşmeleridir."},{"facet_id":"F003","role":"specialization","statement":"Anlaşılması güç bilgiyi açıklama veya bir kişiye bir şeyi bildirip kavratma, bilgiye erişim sağlayan gerçekleşmelerdir."},{"facet_id":"F004","role":"associated_use","statement":"Okuyan kişiye takıldığı sözü hatırlatmak, bilgiye erişim çekirdeğine bağlı özel bir yardım eylemidir."}],"identity_rationale":"Kaynak ifadesi sıkıntı ve yoksunluğu giderme, anlaşılması güç bilgiyi açıklama, birine bilgi verme ve okuyana takıldığı yerde yardımcı olma kullanımlarını destekler. Ancak bunlar bağımsız, sınırsız bir soyut anlam değil, belirtilen yapılara bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kaygıyı veya sıkıntıyı gidermek"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir şeyi bildirip kavratmak"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"anlaşılması güç bir bilgi alanını açıklığa kavuşturmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"okuyan kişiye takıldığı yeri söylemek"}],"lexicalization_note":"Tanım yalnız sıkıntı giderme, bilgi açıklama, bildirme ve okuyana yardım etme yapılarıyla sınırlıdır; bağımsız kök anlamı varsayılmaz.","neighbor_coverage_note":"Bütün adaylar bilgi, görünürlük, şaşkınlık, kaygı, soruşturma, dayanıklılık ve diğer kök içi dallar bakımından değerlendirildi; belirginleşme komşusu işlem ile durum ayrımını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir güçlüğü gideren veya bilgiyi açan nedensel bir işlemdir; komşu dal ise öncelikle bir şeyin görünür ya da belirgin olma durumunu anlatır.","focus_only":"Bu dal belirli yapılarda bir güçlüğü etkin biçimde giderir, bilgi verir veya okuyana yardım eder.","gloss":"belirginleşme ve görünürlük","neighbor_only":"Komşu dal bir şeyin görünür ve belirgin olma durumunu, ayrıca yol ve kılavuz işlevini kapsar.","neighbor_ref":"root_001473/B002","relation_type":"near_neighbor","shared_zone":"İki dal da belirsiz olanın anlaşılır ve erişilebilir hale gelmesi alanında buluşur."}],"source_phrase_ar":"الفتح أن تفتح على من يستقرئك (ayn)؛ إزالة الإغلاق والإشكال وما يدرك بالبصيرة كفتح الهم وإزالة الغم وفقر يزال بإعطاء المال وفتح المستغلق من العلوم وفتح عليه كذا إذا أعلمه ووقفه عليه (mufradat)","source_summary":"Kaynaklar, kanıtlanan yapılarda fiziksel olmayan bir engelin kaldırılması ilişkisiyle birleşen yardım, giderme ve açıklama kullanımlarını bildirir. Ayn, okuyana takıldığı yerde yardım etmeyi bu alana bağlar; Müfredat sıkıntıyı veya maddi yoksunluğu giderme, anlaşılması güç bilgiyi açıklama ve birine bilgi verme kullanımlarını kaydeder.","sources":["AY","MU"],"what_is_ar":"يدخل فيه إزالة الإشكال أو الهم، تفريج الغم، إزالة الفقر بالعطاء، إقبال الخيرات، فتح العلم والهداية، وفتح الشيء على الإنسان بمعنى إعلامه وإيقافه عليه.","what_is_not_ar":"ليس هو الفتح الحسي للباب، ولا الحكم، ولا النصر إلا إذا صرحت الصيغة بطلب الظفر أو القضاء."},"support_links":["sup_9efe16c4be1033ee5e3e"]},{"boundary":"Bu dal servet veya bilgi göstererek böbürlenmedir; fiziksel açıklık anlamındaki aynı sesli biçimle karıştırılmaz.","branch_kind":"bare","branch_ref":"root_001124/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","surface_ar":"فَتْحُ"}],"gloss":"serveti veya bilgisiyle böbürlenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahip olunan bir üstünlüğü dışa vurarak başkalarından daha yüksek görünmeye çalışmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Böbürlenmenin dayanağı özellikle servet, bilgi veya toplumsal görgü olabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir aktarım, bu adlandırmanın dilin daha sonraki bir döneminde türemiş olabileceğini belirtir."}}],"root_ar":"ف ت ح","root_id":"root_001124","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sahip olduklarını sergileyerek başkalarına üstünlük tasladığı temel tutumu temsil eder.","boundary_detail":"Bu dal servet veya bilgi göstererek böbürlenmedir; fiziksel açıklık anlamındaki aynı sesli biçimle karıştırılmaz.","branch_image_ar":"تفتح المتطاول بما يظهره من مال أو أدب","concept_gloss":"serveti veya bilgisiyle böbürlenme","contextual_glosses":[{"applicability":"Kişinin sahip olduğu nitelikleri göstererek kendini başkalarından üstün sunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Böbürlenmenin özellikle servet, bilgi veya görgüye dayanması tek sözcükte belirtilmez.","preserves":"Başkalarına üstünlük taslama ve bunu dışa vurma tutumunu doğal biçimde korur."},"facet_ids":["F001"],"text":"böbürlenmek","usage_role":"general"},{"applicability":"Böbürlenmenin dayanağının servet ve bilgi olduğu açıkça belirtilmek istendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sahip olunan malı ve bilgiyi göstererek başkalarına üstünlük taslama anlamını tam korur."},"facet_ids":["F001","F002"],"text":"malı ve bilgisiyle üstünlük taslamak","usage_role":"explanatory"}],"definition":"Kişinin sahip olduğu serveti, bilgiyi veya görgüyü sergileyerek başkalarına üstünlük taslaması ve böbürlenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahip olunan bir üstünlüğü dışa vurarak başkalarından daha yüksek görünmeye çalışmaktır."},{"facet_id":"F002","role":"specialization","statement":"Böbürlenmenin dayanağı özellikle servet, bilgi veya toplumsal görgü olabilir."},{"facet_id":"F003","role":"source_variant","statement":"Bir aktarım, bu adlandırmanın dilin daha sonraki bir döneminde türemiş olabileceğini belirtir."}],"identity_rationale":"Kaynak ifadesi kişinin servetini, bilgisini veya görgüsünü öne sürerek başkalarına üstünlük taslamasını açıkça anlatır. Genel kibirden farklı olarak böbürlenmenin dayanağını ve dışa vurulan karşılaştırmalı üstünlüğü belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"serveti veya bilgisiyle böbürlenme"}],"lexicalization_note":"Bağımsız böbürlenme anlamı tanımlanır; fiziksel açıklık veya başka dallara ait söz öbeği anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar kibir, kendini beğenme, övünme, soy ve başarıyla böbürlenme, sayı üstünlüğü ve diğer kök içi dallar bakımından değerlendirildi; genel övünme komşusu en yakın sınırı verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin mevcut serveti veya bilgisiyle böbürlenmesine özgüdür; komşu dal geçmiş başarıları, soyu ve karşılıklı övünme davranışını daha geniş kapsar.","focus_only":"Bu dal üstünlük taslamayı özellikle servet, bilgi veya görgünün gösterilmesine bağlar.","gloss":"övünme ve böbürlenme","neighbor_only":"Komşu dal eski başarıları saymayı, soyla övünmeyi ve karşılıklı övünme yarışını da kapsar.","neighbor_ref":"root_001135/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin sahip olduklarını öne çıkararak başkalarına üstünlük göstermesinde örtüşür."}],"source_phrase_ar":"الفتحة تفتح الإنسان بما عنده من أموال أو أدب يتطاول به (ayn)؛ الفتحة التيه والتكبر وأحسبها مولدة (jamhara)؛ الفتحة تفتح الإنسان بما عنده من ملك أو أدب يتطاول به (tahdhib)","source_summary":"Kaynaklar kişinin servetini, bilgisini veya görgüsünü göstererek başkalarına üstünlük taslaması ve böbürlenmesi anlamını verir. Camhara, bu adlandırmanın daha sonraki dönemde türemiş olabileceği tarihsel ihtiyatını ekler.","sources":["AY","JA","TA"],"what_is_ar":"يدخل فيه الفتحة بمعنى التيه أو التكبر أو تطاول الإنسان بما عنده من مال أو أدب.","what_is_not_ar":"ليس هو الفتحة بمعنى الفرجة في الشيء، ولا فتح الباب."},"support_links":[]},{"boundary":"Dal, haksızlığa uğrayanın kendi hakkını almasını değil, ona yardım eden tarafın sağladığı desteği anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001510/B001","candidate_links":[{"candidate_id":"cand_08161fcc24c8918b349e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"yardım edip üstün gelmesini sağlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasına, özellikle haksızlığa uğramış olana yardım ve destek sağlama çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yardımın düşmana karşı üstünlük ve başarı sağlaması, çekirdeğin çatışma ortamındaki belirginleşmiş biçimidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karşılıklı kullanımda birden çok tarafın birbirine yardım etmesi ve iş birliği yapması anlatılır."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yardım çekirdeğini ve düşmana karşı üstünlük sağlama sonucunu birlikte veren en kapsamlı kısa karşılıktır.","boundary_detail":"Dal, haksızlığa uğrayanın kendi hakkını almasını değil, ona yardım eden tarafın sağladığı desteği anlatır.","branch_image_ar":"النصرة عون وإظهار","concept_gloss":"yardım edip üstün gelmesini sağlama","contextual_glosses":[{"applicability":"Karşılaşma sonucunun öne çıkmadığı, bir kişiye ya da topluluğa destek verildiği genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşmana karşı üstünlük sağlama sonucunu ve karşılıklı yardımlaşma biçimini söylemez.","preserves":"Bir başkasına destek verme biçimindeki temel eylemi açıkça korur."},"facet_ids":["F001"],"text":"yardım etmek","usage_role":"general"},{"applicability":"Bir tarafın aldığı yardımla düşmanı yenmesi ya da onun karşısında üstün duruma gelmesi anlatılırken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çatışma dışındaki genel yardımı ve tarafların karşılıklı desteğini kapsamaz.","preserves":"Yardımın çatışmadaki üstünlük ve başarı doğuran sonucunu korur."},"facet_ids":["F002"],"text":"üstün gelmesini sağlamak","usage_role":"contextual"},{"applicability":"Tarafların tek yönlü yardım yerine karşılıklı olarak birbirini güçlendirdiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek yönlü yardımı ve düşmana karşı üstün getirme sonucunu dışarıda bırakır.","preserves":"Karşılıklı yardım ve iş birliği düzenini doğal Türkçeyle korur."},"facet_ids":["F003"],"text":"birbirine destek olmak","usage_role":"contextual"}],"definition":"Bir kişiye ya da topluluğa yardım ederek onu güçlendirmek ve özellikle bir düşman karşısında üstün duruma gelmesini sağlamaktır; karşılıklı biçiminde taraflar birbirine yardım eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasına, özellikle haksızlığa uğramış olana yardım ve destek sağlama çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Yardımın düşmana karşı üstünlük ve başarı sağlaması, çekirdeğin çatışma ortamındaki belirginleşmiş biçimidir."},{"facet_id":"F003","role":"extension","statement":"Karşılıklı kullanımda birden çok tarafın birbirine yardım etmesi ve iş birliği yapması anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yardımdan bağımsız biçimde kazanılmış her türlü başarıyla karışabilir.","fit":"narrowing","loses":"Bu sonucu doğuran yardım eylemini ve sonuçsuz kalabilen genel desteği siler.","preserves":"Düşmana karşı elde edilen başarılı sonucu belirgin biçimde korur."},"text":"zafer"}],"identity_rationale":"Kaynak ifadesi, temel anlamı birine yardım etme olarak verir; düşmana karşı üstünlük kazandırmayı bunun belirgin bir sonucu, karşılıklı yardımlaşmayı da katılımcıların birbirine yöneldiği biçim olarak gösterir. Verilen dal çerçevesi bu çekirdeği ve başlıca kapsamını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yardım etti ve düşmana karşı üstün gelmesini sağladı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yardım, destek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iyi ve etkili yardım"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yardımcı, destekçi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yardımcı, destekçi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yardımcılar, destekçiler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"düşmanına karşı kendisine yardım etmesini istedi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birbirlerine yardım ettiler, dayanıştılar"}],"lexicalization_note":"Tanım genel yardım çekirdeğini, düşmana karşı üstün getirme kullanımını ve yardım isteme ya da karşılıklı yardımlaşma gibi türemiş yapıları birbirine karıştırmadan kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma yardım, kişisel karşılık verme ve daha geniş güç alanıyla en yararlı sınırları gösterir. Diğer adaylar ya bu ayrımları tekrarlar ya da yalnızca aynı çatışma çevresinde uzaktan ilişki kurar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, yardım alan tarafın özellikle bir rakip karşısında üstün duruma gelmesine yönelebilir; komşu dal ise dayanak olmayı nesne ve yapı desteğine kadar genişletir.","focus_only":"Düşmana karşı üstünlük kazandırma ve karşılıklı yardımlaşma bu dalda açıkça yer alır.","gloss":"yardım ve dayanak olma","neighbor_only":"Bir şeyi dayanak veya güç kılma ve duvarı destekleme gibi cansız nesnelere uzanan kullanımlar vardır.","neighbor_ref":"root_000554/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir başkasına güç kazandıran yardım ve destek alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal bir tarafın diğerine verdiği yardımı anlatır; komşu dal ise mağdurun haksızlık yapan kişiye karşı kendi tepkisini ve hakkını geri almasını anlatır.","focus_only":"Yardımı sağlayan dış taraf ve onun başkasını güçlendiren eylemi merkezdedir.","gloss":"yardım ile hakkını alma","neighbor_only":"Haksızlığa uğrayanın zalime karşı koyması, hakkını alması veya öcünü alması merkezdedir.","neighbor_ref":"root_001510/B002","relation_type":"near_neighbor","shared_zone":"İki dal da baskı veya çatışma karşısında güç kazanma senaryosunda buluşabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yardım ilişkisidir; komşu dal ise yardımın yanında cesaret ve kuvvet gibi kişinin kendi niteliğini de bağımsız anlamlar olarak kapsar.","focus_only":"Yardım ve yardımla üstün getirme, cesaret veya bedensel güç gerektirmeden de gerçekleşebilir.","gloss":"yardım, güç ve üstünlük","neighbor_only":"Cesaret, sert güç, hastalıktan sonra kuvvetlenme ve yardım isteme gibi daha geniş kuvvet alanları bulunur.","neighbor_ref":"root_001473/B003","relation_type":"near_neighbor","shared_zone":"Yardım görme, güç kazanma ve düşmana karşı üstünlük iki dalın kesiştiği alandır."}],"source_phrase_ar":"النصر والنصرة العون (mufradat)؛ عون المظلوم (ayn;tahdhib)؛ نصره الله على عدوه ينصره نصرا (sihah)؛ آتاهم الظفر على عدوهم (maqayis)؛ النصير الناصر (ayn;sihah;tahdhib)؛ التناصر التعاون (mufradat)","source_summary":"Kaynakların ortak çizgisi yardım etme, yardımla güç kazandırma ve düşman karşısında üstünlük sağlamadır; karşılıklı biçim bu çekirdeği iş birliğine genişletir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العون، والنصرة، والناصر والنصير، والأنصار، والاستنصار والتناصر حين تدور على المعونة والإظهار على العدو","what_is_not_ar":"ليس الدخول في النصرانية؛ وليس مطر الأرض؛ وليس إتيان المكان؛ وليس العطاء المجرد"},"support_links":["sup_a2a6a26c6812ccce6e70"]},{"boundary":"Buradaki tepki, herhangi bir cezalandırma değil, kişinin kendisine yönelmiş haksızlık veya baskıdan sonra karşı koymasıdır.","branch_kind":"bare","branch_ref":"root_001510/B002","candidate_links":[{"candidate_id":"cand_9eeb8452160d3ed27d2b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"zulmedene karşı koyup hakkını alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mağdurun haksızlık yapan kişiden hakkını veya yapılan kötülüğün karşılığını almasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılık alma sonucundan önce ya da onun yerine, zalimin baskısına direnip kendini koruma anlamı da bulunur."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Direnme ile haksızlığın karşılığını alma aşamalarını birlikte ifade ettiği için dalın bütün çekirdeğine uygundur.","boundary_detail":"Buradaki tepki, herhangi bir cezalandırma değil, kişinin kendisine yönelmiş haksızlık veya baskıdan sonra karşı koymasıdır.","branch_image_ar":"انتصاف المظلوم","concept_gloss":"zulmedene karşı koyup hakkını alma","contextual_glosses":[{"applicability":"Haksızlığa uğrayan kişinin kötülük yapan kişiye karşı cezalandırıcı bir karşılık verdiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşı saldırı olmadan direnme ve yalnızca hakkını geri alma biçimlerini kapsamaz.","preserves":"Kötülük yapan kişiye karşılık verme ve ondan öç alma yönünü korur."},"facet_ids":["F001"],"text":"öcünü almak","usage_role":"contextual"},{"applicability":"Vurgu cezalandırmadan çok yitirilen hakkın geri kazanılmasındaysa doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskıya direnme aşamasını ve öç alma biçimindeki cezalandırıcı karşılığı dışarıda bırakır.","preserves":"Mağdurun kendisine ait hakkı yeniden elde etmesi sonucunu korur."},"facet_ids":["F001"],"text":"hakkını almak","usage_role":"contextual"},{"applicability":"Mağdurun baskıyı kabul etmeyip kendini savunduğu, fakat henüz bir karşılık almadığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hakkı geri kazanma veya yapılan kötülüğün karşılığını alma sonucunu söylemez.","preserves":"Zalimin baskısına direnme ve kendini koruma yönünü açıkça korur."},"facet_ids":["F002"],"text":"zulme karşı koymak","usage_role":"contextual"}],"definition":"Haksızlık yapan kişiye karşı koymak, onun baskısını savuşturmak ve ondan hakkını ya da yapılan kötülüğün karşılığını almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mağdurun haksızlık yapan kişiden hakkını veya yapılan kötülüğün karşılığını almasıdır."},{"facet_id":"F002","role":"extension","statement":"Karşılık alma sonucundan önce ya da onun yerine, zalimin baskısına direnip kendini koruma anlamı da bulunur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kişisel haksızlıkla ilgisi bulunmayan her türlü yaptırımı ve yetkili cezasını da kapsar.","collision":"Yargısal veya kurumsal ceza verme anlamıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Kötülük yapan kişiye olumsuz bir karşılık verme yönünü kısmen korur."},"text":"cezalandırmak"}],"identity_rationale":"Kaynak ifadesi, haksızlık yapan kişiden karşılık alma ve hakkını elde etmenin yanında onun baskısına direnme anlamını da açıkça taşır. Dal çerçevesi bu tepki alanını tek bir mağdur-merkezli anlam kümesi olarak doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zulmeden kişiden hakkını aldı, öcünü aldı"}],"lexicalization_note":"Tanım, çıplak dalın haksızlık yapan kişiye karşı koyma ve ondan hakkını alma kapsamıyla sınırlıdır; yardım isteme yapısı buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu öç alma, adalet, yetkiliden yardım isteme ve dışarıdan destek alma sınırlarını ayrı ayrı açıklar. Kalan adaylar genel ceza, savunma veya husumet alanlarını daha uzaktan paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal mağdurun kendisine zulmedene karşı direnişini ve hak almasını içerir; komşu dal cezalandırıcı karşılığı, mağdurun kendi hakkını geri alması şartına bağlamaz.","focus_only":"Mağdurun baskıya direnmesi ve kendi hakkını doğrudan geri alması da kapsam içindedir.","gloss":"öç alma ve cezalandırma","neighbor_only":"Bir kötülüğü kınadıktan sonra suçluya ceza verme ve yaptırım uygulama daha geniştir.","neighbor_ref":"root_001545/B002","relation_type":"near_synonym","shared_zone":"İki dal da yapılan kötülüğe karşı olumsuz bir karşılık verme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal belirli bir zulümden sonra mağdurun tepkisini anlatır; komşu dal ise haksızlık öncesinde de geçerli olan genel adalet ve eşit davranma düzenini kapsar.","focus_only":"Öç alma ve zalimin baskısını savuşturma gibi çatışmalı tepki biçimleri vardır.","gloss":"hakkını alma ve adalet","neighbor_only":"Taraflar arasında eşitlik, hakkı verme ve adil davranma gibi karşılıklı düzen ilkeleri vardır.","neighbor_ref":"root_001511/B003","relation_type":"near_neighbor","shared_zone":"Kişinin hakkına kavuşması ve haksızlığın giderilmesi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal kişinin kendi direnişini ve karşılığını merkeze alır; komşu dal üçüncü bir yetkiliden yardım istemeyi kurucu unsur yapar.","focus_only":"Mağdurun zalime bizzat karşı koyması veya ondan doğrudan karşılık alması anlatılır.","gloss":"doğrudan karşılık ve yardım isteme","neighbor_only":"Bir yöneticiye ya da yargıca başvurup zalime karşı yardım ve yaptırım isteme anlatılır.","neighbor_ref":"root_000993/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da haksızlığa uğrayan kişinin zalime karşı hakkını aramasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal mağdurun zalime yönelen tepkisidir; komşu dal ise yardımcı bir tarafın mağdura veya savaşan tarafa yönelttiği destektir.","focus_only":"Haksızlığa uğrayan kişinin kendi direnişi, hak alması ve öç alması merkezdedir.","gloss":"karşı koyma ve yardım","neighbor_only":"Başka bir tarafın mağdura yardım etmesi ve onu düşman karşısında üstün getirmesi merkezdedir.","neighbor_ref":"root_001510/B001","relation_type":"near_neighbor","shared_zone":"İki dal da haksızlık veya düşmanlık karşısında güç kazanma senaryosuna katılır."}],"source_phrase_ar":"انتصر انتقم وهو منه (maqayis)؛ انتصر الرجل انتقم من ظالمه (ayn)؛ وانتصر منه انتقم (sihah)؛ انتصر الرجل إذا امتنع من ظالمه (tahdhib)؛ الانتصاف والانتقام منه (tahdhib)؛ إذا أصابهم البغي هم ينتصرون (mufradat)","source_summary":"Kaynaklar, haksızlık yapan kişiden öç veya hak alma çizgisini onun baskısına direnme ve kendini koruma çizgisiyle birlikte sunar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الانتصار من الظالم، والامتناع منه، والانتصاف والانتقام بعد ظلم","what_is_not_ar":"ليس طلب النصرة العام إلا إذا صار انتصارا من ظالم؛ وليس العون المتبادل المجرد"},"support_links":["sup_de5d80415ab6704241b1"]},{"boundary":"Anlam genel bir çıplak eylem olarak değil, ülke veya toprağı nesne alan belirli kullanım içinde geçerlidir.","branch_kind":"collocation","branch_ref":"root_001510/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"bir ülkeye veya toprağa gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ülke veya toprakla kurulan sınırlı yapıda, adı verilen yere gelme anlamı taşır."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer türünü ve varış hareketini birlikte koruduğu için yalnızca kanıtlanan sınırlı yapıya uygundur.","boundary_detail":"Anlam genel bir çıplak eylem olarak değil, ülke veya toprağı nesne alan belirli kullanım içinde geçerlidir.","branch_image_ar":"إتيان البلد","concept_gloss":"bir ülkeye veya toprağa gelmek","contextual_glosses":[{"applicability":"Hedefin daha önce anıldığı ve bir ülke olduğu akıcı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli ülke hedefini ve konuşana ya da bakış noktasına doğru varışı korur."},"facet_ids":["F001"],"text":"o ülkeye gelmek","usage_role":"contextual"},{"applicability":"Nesnenin ülke yerine bir topluluğun toprağı veya yurdu olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli toprağı hedef alan hareketi ve hedefe ulaşma sonucunu korur."},"facet_ids":["F001"],"text":"o toprağa varmak","usage_role":"contextual"}],"definition":"Bir ülke veya toprağın doğrudan nesne olduğu belirli yapıda, o yere gelmek ya da oraya varmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ülke veya toprakla kurulan sınırlı yapıda, adı verilen yere gelme anlamı taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir yararlanan taraf ve ona destek verme ilişkisi ekler.","collision":"Aynı kökün yardım dalıyla doğrudan karışır.","fit":"displacement","loses":"Ülke veya toprağı hedef alan gelme hareketini bütünüyle ortadan kaldırır.","preserves":"Aynı kökün başka bir dalındaki yaygın eylem çağrışımını taşır."},"text":"yardım etmek"}],"identity_rationale":"Kaynak ifadesi yalnızca belirli bir ülke ya da toprağın nesne olduğu kullanımda oraya gelme anlamını bildirir. Dal çerçevesi bu yer-yönelimli ve kalıba bağlı anlamı doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"belirtilen ülkeye veya toprağa geldim"}],"lexicalization_note":"Tanım yalnızca ülke ya da toprak adıyla kurulan yapıya bağlıdır; buradan genel bir gelmek veya gitmek anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel gelme, kişiye ihtiyaç için gelme ve yüce bir hedefe yönelme ile olan sınırları gösterir. Öteki adaylar yolculuk, sabah gelme veya ülkede dolaşma gibi daha uzak hareket türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnızca ülke veya toprağı nesne alan özel yapıdır; komşu dal hedef türüyle sınırlanmayan genel gelme anlamına sahiptir.","focus_only":"Hedefin ülke veya toprak olması ve anlamın belirli nesneli yapıya bağlı kalması gerekir.","gloss":"belirli yere gelme","neighbor_only":"Genel gelme eylemi ve çok gelerek üstünlük kurma gibi daha geniş hareket kullanımları bulunur.","neighbor_ref":"root_000282/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe doğru gelme ve o hedefe ulaşma hareketini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın hedefi ülke veya topraktır; komşu dalın hedefi bir kişi ya da onun çevresi olup ihtiyaç ve konukluk amacı belirginleşir.","focus_only":"Bir ülkeye veya toprağa gelmek için ihtiyaç arama ya da konuk olma amacı aranmaz.","gloss":"yere veya kişiye gelme","neighbor_only":"Bir kişinin yanına ihtiyaç istemek için gelme veya konukların ona gelmesi kurucu kapsam içindedir.","neighbor_ref":"root_001005/B002","relation_type":"near_neighbor","shared_zone":"İki dal da belirli bir hedefe yönelip onun yanına ya da alanına gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnızca hedef yer türüyle sınırlıdır; komşu dal ise hedefin önemini ve ona yönelme amacını anlamın merkezine alır.","focus_only":"Herhangi bir ülke veya toprağa gelme, hedefin yüceltilmiş olmasını gerektirmez.","gloss":"gelme ve amaçlı yönelme","neighbor_only":"Yüce sayılan bir hedefe yönelme ve dinsel ziyaret amacı taşıyan gelişler bulunur.","neighbor_ref":"root_000295/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bir yere yönelme ve o yere varma olayını içerebilir."}],"source_phrase_ar":"نصرت بلد كذا إذا أتيته (maqayis)؛ نصرت أرض بني فلان أي أتيتها (tahdhib)","source_summary":"Kaynaklar, ülke ya da toprağı nesne alan bu özel yapıyı o yere gelmek anlamında ortak biçimde açıklar.","sources":["MQ","TA"],"what_is_ar":"نصر البلد أو الأرض بمعنى أتاها","what_is_not_ar":"ليس نصرة المظلوم؛ وليس المطر الذي يروي الأرض؛ وليس العطاء"},"support_links":[]},{"boundary":"Dal, suyun aktığı yatağı değil, yağan yağmuru ve onun toprakla insanlar üzerindeki yararlı etkisini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001510/B004","candidate_links":[{"candidate_id":"cand_12b070938f64dc090076","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"toprağı sulayıp yeşerten, insanları ferahlatan yağmur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmurun adı ve özellikle eksiksiz, yeterli bir yağış oluşu bu dalın adlandırma çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yağmurun ülkeyi veya toprağı sulaması ve bitki çıkarması, yararlı etkinin başlıca gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toprağın yağmur almış duruma gelmesi, olayın etkilenen yer açısından kurulan biçimidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluğun yağmura kavuşarak kuraklık veya susuzluktan kurtulması, etkinin insanlar açısından kurulan biçimidir."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmur adını ve onun toprakla insanlar üzerindeki iki temel yararlı sonucunu birlikte temsil eder.","boundary_detail":"Dal, suyun aktığı yatağı değil, yağan yağmuru ve onun toprakla insanlar üzerindeki yararlı etkisini anlatır.","branch_image_ar":"النصر مطر وإغاثة","concept_gloss":"toprağı sulayıp yeşerten, insanları ferahlatan yağmur","contextual_glosses":[{"applicability":"Sözcüğün doğrudan yağışı adlandırdığı ve etkinin ayrıca belirtilmediği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yağışın yeterliliğini, toprağı yeşertmesini ve insanları rahatlatmasını açıkça söylemez.","preserves":"Dalın doğrudan yağışı adlandıran temel isim yönünü korur."},"facet_ids":["F001"],"text":"yağmur","usage_role":"general"},{"applicability":"Yağışın eksiksiz ve ihtiyacı karşılayacak ölçüde oluşunun vurgulandığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın yağmur alması ile sulama, yeşertme ve toplumsal rahatlama yapılarını ayrı ayrı vermez.","preserves":"Yağmurun tam, yeterli ve yarar sağlayan bir yağış oluşunu korur."},"facet_ids":["F001"],"text":"doyurucu yağmur","usage_role":"contextual"},{"applicability":"Yağmurun etkileyen, toprağın ise sulanan veya bitki çıkaran taraf olduğu cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yağmurun ad olarak kullanımını ve insanların yağmurla rahatlamasını kapsamaz.","preserves":"Yağmurun toprağa su vermesi ve bitki çıkarması sonuçlarını açıkça korur."},"facet_ids":["F002"],"text":"yağmur toprağı suladı ve yeşertti","usage_role":"contextual"},{"applicability":"Bir topluluğun ihtiyaç duyduğu yağmuru alarak sıkıntıdan kurtulduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yağmurun adı ile toprağın sulanması ve yeşermesi yönlerini dışarıda bırakır.","preserves":"İnsanların yağmurla rahatlaması ve ihtiyaçlarının karşılanması sonucunu korur."},"facet_ids":["F004"],"text":"halk yağmura kavuştu","usage_role":"contextual"}],"definition":"Yağmurun kendisini, özellikle yeterli ve yararlı bir yağışı adlandırır. İlgili yapılarda yağmurun toprağı sulayıp yeşertmesi, toprağın yağmur alması ve insanların yağmurla sıkıntıdan kurtulması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmurun adı ve özellikle eksiksiz, yeterli bir yağış oluşu bu dalın adlandırma çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Yağmurun ülkeyi veya toprağı sulaması ve bitki çıkarması, yararlı etkinin başlıca gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Toprağın yağmur almış duruma gelmesi, olayın etkilenen yer açısından kurulan biçimidir."},{"facet_id":"F004","role":"extension","statement":"Bir topluluğun yağmura kavuşarak kuraklık veya susuzluktan kurtulması, etkinin insanlar açısından kurulan biçimidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Suyun içinden aktığı kalıcı veya geçici bir yer biçimini ekler.","collision":"Aynı kökün uzaktan gelen su yataklarını anlatan dalıyla karışır.","fit":"displacement","loses":"Yağış olayını ve yağmurun sulama, yeşertme, rahatlatma etkilerini siler.","preserves":"Su ve toprağa ilişkin genel alan çağrışımını korur."},"text":"su yolu"}],"identity_rationale":"Kaynak ifadesi hem yağmurun adı ve tam bir yağış oluşunu hem de yağmurun toprağı sulaması, yeşertmesi ve insanları sıkıntıdan kurtarmasını birlikte bildirir. Verilen dal çerçevesi yağış ile onun yararlı sonucunu doğru bir bütünlük içinde tutar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yağmur"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"eksiksiz ve doyurucu yağmur"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yağmur ülkeyi suladı veya yeşertti"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"toprağa yağmur yağdı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"halk yağmura kavuşup rahatladı"}],"lexicalization_note":"Tanım, yağmur adını ve tam yağış biçimini; toprağın yağmur alması, yağmurun sulayıp yeşertmesi ve insanların yağmurla ferahlaması yapılarından ayrı gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen dört komşu yağışın gerçekleşmesi, bol yağmur, yağmur sonrası bitkilenme ve su yatağı sınırlarını gösterir. Kalanlar sulama araçları, yağış zamanları veya susuz tarım gibi daha dolaylı alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yağmuru yararlı etkisiyle birlikte kavrar; komşu dal yağışın oluşuna ve düştüğü yerlere odaklanır, rahatlatıcı sonucu şart koşmaz.","focus_only":"Yağmurun toprağı sulayıp yeşertmesi ve insanları sıkıntıdan kurtarması belirgindir.","gloss":"yağmur ve yağışın gerçekleşmesi","neighbor_only":"Yağışın gerçekleştiği yerler ve suyun gökten düştüğü noktalar bağımsız olarak adlandırılır.","neighbor_ref":"root_001675/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da yağmurun yağmasını ve belirli bir toprağın yağış almasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal yararlı etkiyi ve rahatlamayı öne çıkarır; komşu dal ise yağmurun miktar ve bolluk niteliğini merkeze alır.","focus_only":"Sulama, yeşertme ve insanları rahatlatma sonucu, yalnız yağış miktarına bağlı olmadan kapsam içindedir.","gloss":"yararlı ve bol yağmur","neighbor_only":"Yağmurun özellikle bol ve yoğun oluşu tanımın belirleyici koşuludur.","neighbor_ref":"root_000213/B003","relation_type":"near_synonym","shared_zone":"İki dal da güçlü, ihtiyacı karşılayan bir yağmuru adlandırmak için kullanılabilir."},{"boundary_match":"partial","distinction":"Odak dal yağışı ve onun etkisini adlandırır; komşu dal ise yağıştan sonra hızlı gelişen toprağın veya bitkinin niteliğini anlatır.","focus_only":"Etkileyen yağmur ve onun toprağı sulaması bu dalda merkezdedir.","gloss":"yağmur ve yağmur sonrası bitki","neighbor_only":"Yağmurdan sonra hızla bitki çıkaran toprağın veya ürünün yatkınlığı merkezdedir.","neighbor_ref":"root_001412/B006","relation_type":"near_neighbor","shared_zone":"Yağmurdan sonra toprağın yeşermesi iki dalın aynı olay içinde kesiştiği noktadır."},{"boundary_match":"field_only","distinction":"Bu dal suyun yağış olarak düşmesini ve yarar sağlamasını anlatır; komşu dal yağmış veya akmış suyun izlediği yer biçimini anlatır.","focus_only":"Gökten düşen yağış ve onun sulama ya da rahatlatma etkisi anlatılır.","gloss":"yağmur ve su yatağı","neighbor_only":"Uzaktan gelen suyu vadiye veya su toplanma yerine taşıyan yatak ya da yarıntı anlatılır.","neighbor_ref":"root_001510/B007","relation_type":"same_field","shared_zone":"İki dal suyun toprağa ulaşması ve bir yerde toplanmasıyla ilgili doğal çevre alanını paylaşır."}],"source_phrase_ar":"يسمى المطر نصرا (maqayis)؛ نصر الغيث البلاد أرواها (ayn)؛ نصر الغيث الأرض أي غاثها (sihah)؛ النصرة المطرة التامة (tahdhib)؛ نصر الغيث البلاد إذا أنبتها (tahdhib)؛ نصر القوم إذا أغيثوا (tahdhib)","source_summary":"Kaynaklar yağmur adını, yeterli yağışı, toprağın yağmur almasını ve yağmurun sulama, yeşertme ve insanları rahatlatma sonuçlarını aynı anlam alanında birleştirir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"المطر المسمى نصرا، ونصر الغيث البلاد بإروائها أو إنباتها، والأرض المنصورة إذا مطرت، وإغاثة القوم بالغيث","what_is_not_ar":"ليس نصرة المظلوم؛ وليس النصر بمعنى العطاء؛ وليس النواصر مسايل المياه"},"support_links":["sup_082364b131bcf399f88b"]},{"boundary":"Dal, birine destek olmanın her türünü değil, iyi bir şeyi ona verme veya ulaştırma eylemini anlatır.","branch_kind":"bare","branch_ref":"root_001510/B005","candidate_links":[{"candidate_id":"cand_30ab58e43c0fc20a78bf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"iyilik veya armağan verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye armağan ya da yararlı bir şey verme anlamı dalın doğrudan çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Verilen şeyin maddi bir armağanla sınırlı kalmayıp genel olarak iyilik ulaştırması da kapsanır."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi armağanı ve daha genel iyi bir şey ulaştırmayı birlikte kapsayan kısa karşılıktır.","boundary_detail":"Dal, birine destek olmanın her türünü değil, iyi bir şeyi ona verme veya ulaştırma eylemini anlatır.","branch_image_ar":"النصر عطاء","concept_gloss":"iyilik veya armağan verme","contextual_glosses":[{"applicability":"Verilen iyi şeyin somut bir bağış veya armağan olarak düşünüldüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut armağan sayılmayan daha genel iyilik ulaştırma biçimlerini kapsamaz.","preserves":"Birine değerli veya yararlı bir şeyi karşılıksız verme eylemini korur."},"facet_ids":["F001"],"text":"armağan vermek","usage_role":"contextual"},{"applicability":"Verilen şeyin türü belirtilmediğinde ve yararlı sonuç öne çıkarıldığında kullanılabilir.","error_profile":{"adds":"Bir şey verme içermeyen yararlı davranışları da olağan kullanımda kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir başkasına iyi ve yararlı bir sonuç sağlama yönünü korur."},"facet_ids":["F002"],"text":"iyilikte bulunmak","usage_role":"explanatory"}],"definition":"Birine armağan, yarar veya başka bir iyi şey vermek ve böylece iyiliği ona ulaştırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye armağan ya da yararlı bir şey verme anlamı dalın doğrudan çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Verilen şeyin maddi bir armağanla sınırlı kalmayıp genel olarak iyilik ulaştırması da kapsanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir şey verme içermeyen koruma, destek ve birlikte çalışma biçimlerini de kapsar.","collision":"Aynı kökün yardım ve üstünlük sağlama dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Bir başkasına yarar sağlama yönünü genel düzeyde korur."},"text":"yardım"}],"identity_rationale":"Kaynak ifadesi doğrudan verme ve armağan anlamını, daha genel biçimde de iyi bir şeyi ulaştırma veya sunma düşüncesini bildirir. Verilen çerçeve bu iki yönü yardım ve yağmur dallarına taşırmadan doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"armağan, veriş"}],"lexicalization_note":"Tanım, çıplak dalın armağan ve iyilik verme kapsamını korur; yağmur veya belirli bir yardım yapısı bu anlama eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma cömertlik, maddi verme ve ödül niteliğindeki armağan sınırlarını gösterir. Diğer adaylar aynı verme alanını benzer biçimde tekrarlar veya kazanç ve akrabalık bağı gibi ek kapsamlar taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal verilen iyiliği ve verme olayını anlatır; komşu dal bunların yanında vericinin cömert niteliğini ve çok verme eğilimini de içerir.","focus_only":"Tek bir verme olayı veya verilen armağanın adı, vericinin sürekli cömert olmasını gerektirmez.","gloss":"armağan ve cömertlik","neighbor_only":"Cömertlik, eli açıklık ve çok veren kişinin yerleşik niteliği kapsam içindedir.","neighbor_ref":"root_001487/B008","relation_type":"near_synonym","shared_zone":"Birine iyilik veya armağan verme iki dalın doğrudan kesiştiği alandır."},{"boundary_match":"partial","distinction":"Odak dal iyi bir şeyi ulaştırma bakımından daha genel kalır; komşu dal mal ve somut bağış verme görünümünü daha belirgin taşır.","focus_only":"İyiliğin maddi mal dışındaki yararlı bir şey olarak verilmesine de izin verir.","gloss":"iyilik veya mal verme","neighbor_only":"Mal veya belirli bir şey vermek ve art arda yapılan iyilikler daha belirgin kapsamdır.","neighbor_ref":"root_001528/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiye karşılıksız olarak yararlı bir şey verme eylemini anlatır."},{"boundary_match":"partial","distinction":"Odak dal herhangi bir iyi şeyi verme kapsamına sahiptir; komşu dal verilen şeyi ödül veya özel armağan niteliğiyle sınırlar.","focus_only":"Verilen şeyin ödül veya resmî armağan olması gerekmez; genel iyilik de kapsanır.","gloss":"armağan ve ödül","neighbor_only":"İnsanlara verilen ödül veya değerli armağan niteliğindeki sunular öne çıkar.","neighbor_ref":"root_000276/B010","relation_type":"near_synonym","shared_zone":"Karşılıksız verilen armağan iki dalın doğal olarak birbirinin yerine yaklaşabildiği alandır."}],"source_phrase_ar":"النصر العطاء (maqayis;sihah)؛ أصل صحيح يدل على إتيان خير وإيتائه (maqayis)","source_summary":"Kaynaklar doğrudan armağan verme anlamında birleşir ve bunu daha genel olarak birine iyi bir şey ulaştırma düşüncesiyle ilişkilendirir.","sources":["MQ","SI"],"what_is_ar":"النصر بمعنى العطاء وإيتاء الخير","what_is_not_ar":"ليس النصرة بمعنى العون؛ وليس المطر؛ وليس إتيان المكان"},"support_links":["sup_9efe16c4be1033ee5e3e"]},{"boundary":"Adın yardımcılar düşüncesiyle ilişkilendirilmesi, bu dalı yardım anlamına dönüştürmez; din ve bağlılık çekirdeği korunur.","branch_kind":"bare","branch_ref":"root_001510/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"Hristiyanlık ve Hristiyan olma ya da yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hristiyanlık ve bu dine bağlılık, dalın din ve kimlik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin Hristiyanlığı benimseyip bu dine girmesi, bağlılığın oluşma sürecidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başkasını Hristiyan yapmak, sürecin dışarıdan bir etkileyenle kurulan ettirgen biçimidir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Dine bağlı erkek, kadın ve topluluk için kullanılan adlar aynı kimlik alanını kişi ve grup düzeyinde kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Adlandırmanın kökeni bir açıklamada Tanrı'nın yardımcıları olma çağrısına, diğerinde bir yer adına bağlanır."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dini, ona bağlanma sürecini ve birini o dine sokma sürecini birlikte gösteren kapsamlı kısa karşılıktır.","boundary_detail":"Adın yardımcılar düşüncesiyle ilişkilendirilmesi, bu dalı yardım anlamına dönüştürmez; din ve bağlılık çekirdeği korunur.","branch_image_ar":"النصرانية نسبة وملة","concept_gloss":"Hristiyanlık ve Hristiyan olma ya da yapma","contextual_glosses":[{"applicability":"Din veya bağlılık alanının kendisi adlandırıldığında, kişi ve süreçler ayrıca belirtilmediğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dine girme, birini dine sokma ve bağlı kişileri adlandırma süreçlerini söylemez.","preserves":"Belirli dini ve ona bağlı kimlik alanını doğrudan korur."},"facet_ids":["F001"],"text":"Hristiyanlık","usage_role":"general"},{"applicability":"Bir kişinin Hristiyanlığı benimseyerek bu dine girdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinin adını, başkasını dine sokmayı ve bağlı topluluğun adlandırılmasını kapsamaz.","preserves":"Kişinin Hristiyan kimliğini edinmesi ve dine girmesi sürecini korur."},"facet_ids":["F002"],"text":"Hristiyan olmak","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini Hristiyanlığa soktuğu ettirgen bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendiliğinden dine girmesini, dinin adını ve topluluk adını kapsamaz.","preserves":"Başka bir kişiye Hristiyan kimliği kazandırma sürecini açıkça korur."},"facet_ids":["F003"],"text":"Hristiyan yapmak","usage_role":"contextual"},{"applicability":"Hristiyanlığa bağlı topluluğun bir bütün olarak adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dine girme ve dine sokma süreçleriyle dinin soyut adını dışarıda bırakır.","preserves":"Belirli dine bağlı insan topluluğunu doğal Türkçe çoğul adla korur."},"facet_ids":["F004"],"text":"Hristiyanlar","usage_role":"contextual"}],"definition":"Hristiyanlığı, bu dine bağlı olmayı, bu dine girmeyi veya birini bu dine sokmayı ve bağlı kişi ya da topluluğu adlandıran anlam alanıdır. Adın kökeni için Tanrı'nın yardımcıları olma çağrısına ve bir yer adına bağlanan iki açıklama aktarılır; bunlar temel anlamı belirlemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hristiyanlık ve bu dine bağlılık, dalın din ve kimlik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin Hristiyanlığı benimseyip bu dine girmesi, bağlılığın oluşma sürecidir."},{"facet_id":"F003","role":"extension","statement":"Bir başkasını Hristiyan yapmak, sürecin dışarıdan bir etkileyenle kurulan ettirgen biçimidir."},{"facet_id":"F004","role":"specialization","statement":"Dine bağlı erkek, kadın ve topluluk için kullanılan adlar aynı kimlik alanını kişi ve grup düzeyinde kurar."},{"facet_id":"F005","role":"source_variant","statement":"Adlandırmanın kökeni bir açıklamada Tanrı'nın yardımcıları olma çağrısına, diğerinde bir yer adına bağlanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Herhangi bir dinden bağımsız yardım eden kişiler anlamını öne çıkarır.","collision":"Aynı kökün yardım ve destek dalıyla karışır.","fit":"displacement","loses":"Hristiyanlık dinini, dine bağlılığı ve bu bağlılığı edinme ya da kazandırma süreçlerini siler.","preserves":"Adlandırmanın kökeni için aktarılan açıklamalardan birini korur."},"text":"Tanrı'nın yardımcıları"},{"category":"alternative","error_profile":{"adds":"Hristiyanlık dışındaki bütün dinleri ve bunlara bağlı kimlikleri de kapsar.","collision":"Genel din kavramıyla belirli Hristiyan kimliği arasındaki ayrımı kaldırır.","fit":"broadening","loses":null,"preserves":"İnanç ve bağlılık alanının genel türünü korur."},"text":"din"}],"identity_rationale":"Kaynak ifadesi Hristiyanlığı, bu dine girme ve birini bu dine sokma eylemlerini, bağlı kişi ile topluluğun adlarını ve adlandırmanın kökenine dair iki açıklamayı birlikte verir. Dal çerçevesi temel din ve bağlılık alanını doğru kurar; köken açıklamaları anlamın kendisi değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"Hristiyan oldu, Hristiyanlığı benimsedi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"onu Hristiyan yaptı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"Hristiyan erkek, Hristiyan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"Hristiyan kadın"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Hristiyanlar"}],"lexicalization_note":"Tanım, Hristiyanlık alanındaki din, bağlılık, dine girme ve dine sokma biçimlerini kapsar; adın kökenine ilişkin açıklamalar yalnızca ikincil bilgi olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler iki başka dinin paralel adlandırma alanını ve din değiştirme sürecini gösterir. Genel din, topluluk ve mezhep adayları bu ayrımları daha geniş veya daha uzak düzeyde tekrarlar; yardım dalıyla bağ yalnızca köken açıklamasındadır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Yapısal benzerliğe rağmen dallar farklı dinleri ve farklı topluluk kimliklerini gösterir; olağan bağlamda birbirinin yerine geçmez.","focus_only":"Hristiyanlık, Hristiyan olma ve Hristiyan yapma süreçleri bu dala özgüdür.","gloss":"iki ayrı din ve bağlılık","neighbor_only":"Yahudilik, Yahudi olma ve o yolun izlenmesi komşu dala özgüdür.","neighbor_ref":"root_001605/B002","relation_type":"same_field","shared_zone":"İki dal da belirli bir dini, o dine bağlı kişileri ve dine yönelme sürecini adlandırır."},{"boundary_match":"field_only","distinction":"Anlamsal yapı paraleldir, fakat gönderimde bulunulan din ve topluluk bütünüyle farklıdır; ilişki eş anlamlılık değil aynı alanda bulunmadır.","focus_only":"Hristiyan dini, bu dine girme ve birini bu dine sokma alanıdır.","gloss":"din ve dine bağlanma","neighbor_only":"Mecusi dini, bu dine girme ve birini bu din içinde yetiştirme alanıdır.","neighbor_ref":"root_001399/B001","relation_type":"same_field","shared_zone":"Her iki dal da belirli bir dinin adını, mensubunu ve dine geçiş ya da geçirme süreçlerini kapsar."},{"boundary_match":"partial","distinction":"Odak dal Hristiyanlığa özgü din ve kimlik alanıdır; komşu dal din değiştirme hareketini ve başka bir belirli dini merkeze alır.","focus_only":"Hristiyan kimliğini ve bu kimliğe özgü kişi ile topluluk adlarını kurar.","gloss":"belirli dine girme","neighbor_only":"Bir dinden çıkıp başka bir dine geçme genel sürecini ve özellikle Sabiilik kimliğini kurar.","neighbor_ref":"root_000837/B002","relation_type":"near_neighbor","shared_zone":"Bir kişinin önceki dinî durumundan ayrılıp belirli bir dine bağlanması iki dalda kesişebilir."}],"source_phrase_ar":"تنصر دخل في النصرانية (ayn;tahdhib)؛ نصره جعله نصرانيا (sihah)؛ رجل نصراني وامرأة نصرانية (sihah)؛ النصارى قيل سموا بذلك لقوله كونوا أنصار الله (mufradat)؛ انتسابا إلى قرية يقال لها نصرانة (mufradat)","source_summary":"Ortak anlam alanı Hristiyanlık, bu dine girme veya sokma ve bağlı kişileri adlandırmadır. Adın kökeni için Tanrı'nın yardımcıları düşüncesine ve bir yer adına dayanan iki farklı açıklama aktarılır.","sources":["AY","SI","TA","MU"],"what_is_ar":"النصرانية، والتنصر، والنصراني والنصرانية والنصارى بوصفها ملة أو نسبة","what_is_not_ar":"ليس نصرة المظلوم إلا على قول الاشتقاق من أنصار الله؛ وليس قرية نصرونة وحدها"},"support_links":[]},{"boundary":"Uzak bir başlangıçtan su toplanma yerine uzanan yatak veya yarıntı belirleyicidir; yalnız suyun akması yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001510/B007","candidate_links":[{"candidate_id":"cand_12b070938f64dc090076","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","surface_ar":"نَصْرُ"}],"gloss":"uzaktan gelip su toplanma yerine ulaşan su yatağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su yatağı veya yarıntı uzaktaki bir yerden gelir ve vadiye ya da su toplanma yerine ulaşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma, suyun aktığı yatak ile bu yatağı oluşturan doğal yarıntı görünümünü birlikte kapsayabilir."}}],"root_ar":"ن ص ر","root_id":"root_001510","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başlangıç uzaklığını, izlenen doğal yatağı ve suyun vardığı toplanma yerini birlikte korur.","boundary_detail":"Uzak bir başlangıçtan su toplanma yerine uzanan yatak veya yarıntı belirleyicidir; yalnız suyun akması yeterli değildir.","branch_image_ar":"ناصرة الماء","concept_gloss":"uzaktan gelip su toplanma yerine ulaşan su yatağı","contextual_glosses":[{"applicability":"Doğal yarıntının ana vadiye uzaktan katılan bir dere kolu olarak görüldüğü coğrafi bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her kullanımda açık bir dere bulunmayabileceğini ve hedefin genel bir su toplanma yeri olabileceğini daraltır.","preserves":"Uzak başlangıçtan ana su alanına uzanan doğal kol görünümünü korur."},"facet_ids":["F001"],"text":"uzaktan gelen dere kolu","usage_role":"contextual"},{"applicability":"Yatak biçimi ile suyun ulaştığı son noktanın açıklanması gerektiği bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolun uzak bir yerden başlaması koşulunu açıkça belirtmez.","preserves":"Suyu taşıyan yolu ve yolun su toplanma yerine bağlanmasını korur."},"facet_ids":["F001","F002"],"text":"su toplanma yerine açılan akış yolu","usage_role":"explanatory"}],"definition":"Uzak bir yerden başlayıp vadiye veya suyun biriktiği yere ulaşan doğal yarıntı, dere kolu ya da su yatağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su yatağı veya yarıntı uzaktaki bir yerden gelir ve vadiye ya da su toplanma yerine ulaşır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırma, suyun aktığı yatak ile bu yatağı oluşturan doğal yarıntı görünümünü birlikte kapsayabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gökten düşen su olayını ve yağış anlamını ekler.","collision":"Aynı kökün yağmur ve yağmurla ferahlama dalıyla karışır.","fit":"displacement","loses":"Suyu taşıyan yarıntıyı, uzak başlangıcı ve toplanma yerine ulaşma sınırını siler.","preserves":"Doğal su ve arazi alanıyla olan genel ilişkiyi korur."},"text":"yağmur"}],"identity_rationale":"Kaynak ifadesi, uzaktaki bir yerden gelip vadiye veya suyun toplandığı yere ulaşan yarıntı ve su yataklarını açıkça tanımlar. Dal çerçevesi bu yer biçimini yağmurun kendisinden ve genel su akışından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"uzaktan gelip su toplanma yerine ulaşan su yatakları"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bu tür su yatağı için olası tekil ad"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu tür su yatağı için diğer olası tekil ad"}],"lexicalization_note":"Tanım kanıtlanan çoğul su yatağı adını esas alır ve incelemede tutulan iki olası tekil biçimi yalnız kendi sözlüksel satırlarında gösterir; çıplak köke genel su yolu anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş karşılaştırma genel su yatağı, dökülme yeri, vadi ucu, yönlendirilmiş kanal ve akış olayıyla sınırları açıklar. Kalan adaylar kıyı, sulama kolu veya sürüklenme izi gibi daha uzak yer biçimleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal güzergâhın uzaktan başlayıp bir toplama alanına bağlanmasını şart koşar; komşu dal genel su yataklarını bu rota sınırı olmadan kapsar.","focus_only":"Su yolunun uzaktan gelmesi ve vadiye ya da su toplanma yerine ulaşması gerekir.","gloss":"su yatağı","neighbor_only":"Suyun herhangi bir akış yatağı, uzak başlangıç ve belirli bir son nokta aranmadan adlandırılabilir.","neighbor_ref":"root_000546/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da suyun içinden aktığı doğal yatak veya küçük akış yolunu adlandırır."},{"boundary_match":"partial","distinction":"Odak dal uzaktan gelen yolun toplama alanına girişini anlatır; komşu dal özellikle suyun döküldüğü, dağıldığı veya aşağıya itildiği yerleri kapsar.","focus_only":"Yatak uzaktaki kaynaktan vadiye veya suyun toplandığı yere doğru gelir.","gloss":"su yolu ve dökülme yeri","neighbor_only":"Suyun aşağıda döküldüğü, itildiği veya kollara ayrıldığı çıkış ve boşalma yerleri de kapsanır.","neighbor_ref":"root_000480/B006","relation_type":"near_synonym","shared_zone":"İki dal doğal su yollarını ve suyun başka bir alana ulaştığı yatakları adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal yolu başlangıç ve varış ilişkisiyle tanımlar; komşu dal ise vadinin veya tepenin aşağı ucu ve kuyruk biçimine odaklanır.","focus_only":"Uzak başlangıçtan su toplanma yerine geliş rotası tanımın zorunlu parçasıdır.","gloss":"vadi kolu ve aşağı uç","neighbor_only":"Tepe ve vadilerin kuyruk, uç ve aşağı kesimleri ile buralardaki su yolları öne çıkar.","neighbor_ref":"root_000521/B004","relation_type":"near_synonym","shared_zone":"Vadiye bağlanan küçük su yolları ve arazi içindeki akış yatakları iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal doğal ve uzak kaynaklı yataktır; komşu dal suyu yönlendiren kanal ile akışı açma veya engelleme işlemlerini de kapsar.","focus_only":"Doğal yarıntının uzaktan gelip su birikim alanına ulaşması belirleyicidir.","gloss":"doğal yatak ve yönlendirilmiş kanal","neighbor_only":"Suyu havuza yönlendiren kanal, akışı kolaylaştırma ve akışı engelleyen nesne gibi işlevsel kullanımlar vardır.","neighbor_ref":"root_000009/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da suyu bir toplama yerine ulaştıran kanal veya akış yolu görünümünü paylaşır."},{"boundary_match":"partial","distinction":"Odak dal suyun izlediği belirli arazi biçimidir; komşu dal ise akma olayını, akan suyu ve akıtma eylemini daha genel biçimde anlatır.","focus_only":"Belirli uzak başlangıç ile vadi veya toplanma yeri arasındaki yatak adlandırılır.","gloss":"su yatağı ve akış","neighbor_only":"Suyun veya başka bir şeyin akma olayı, akıtılması ve akan suyun kendisi merkezdedir.","neighbor_ref":"root_000770/B001","relation_type":"near_neighbor","shared_zone":"Su, doğal yatağı içinde ilerlerken yer biçimi ile akış olayı aynı sahnede buluşur."}],"source_phrase_ar":"النواصر من الشعاب ما جاء من مكان بعيد إلى الوادي؛ النواصر مسايل المياه واحدها ناصرة؛ تجيء من مكان بعيد حتى تقع في مجتمع الماء","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kullanım yalnız bir kaynakta, uzaktan gelip vadideki su toplanma yerine ulaşan yarıntı ve su yolları olarak tanıklanır."}],"source_summary":"Dal, uzaktan gelen suyu vadiye veya su toplanma yerine taşıyan doğal yatak ve yarıntıların sınırlı adlandırmasını temsil eder.","sources":["TA"],"what_is_ar":"النواصر من الشعاب أو المسايل التي تجيء من بعيد حتى تقع في مجتمع الماء","what_is_not_ar":"ليس المطر نفسه؛ وليس عون المظلوم؛ وليس إتيان الأرض بمعنى قصدها"},"support_links":["sup_082364b131bcf399f88b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B001","candidate_links":[{"candidate_id":"cand_08161fcc24c8918b349e","lane":"micro"},{"candidate_id":"cand_9eeb8452160d3ed27d2b","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e94f4440a7d228fe6ae6","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Coming and arrival supply the threshold at which aid becomes present rather than remaining a static possession.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]},{"hft_ref":"hft_b6ff2642a166f03ce444","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Arrival supplies the moment at which a previously pending settlement takes effect.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a2a6a26c6812ccce6e70","sup_de5d80415ab6704241b1"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B003","candidate_links":[{"candidate_id":"cand_12b070938f64dc090076","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_7109c1201dc86721333e","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"A hollow where water gathers supplies the receiving basin of the material mechanism.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_082364b131bcf399f88b"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000281/B004","candidate_links":[{"candidate_id":"cand_30ab58e43c0fc20a78bf","lane":"micro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_b2ab1aaf96b1c9fae0a1","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Bringing or presenting something lets the arrival be heard as the presentation of an effective good.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000281","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_9efe16c4be1033ee5e3e"]}],"candidate_inventory":[{"anchor_refs":["110:1:1"],"branch_refs":[],"candidate_id":"cand_723abe55751a93e25900","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:1:future-certain-condition","source_type":"word_analysis","support_ids":["sup_a9d7fff2da1062a42c91","sup_e4fd7469cbe5c470d277"],"title":"condition is certain, not hypothetical","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:1","qac_refs":["110:1:1:1"],"status":"accepted"}},{"anchor_refs":["110:1:1"],"branch_refs":[],"candidate_id":"cand_b3fa0c1b8a45a4c2e348","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:1:surah-opening-protasis","source_type":"word_analysis","support_ids":["sup_6f255380f7653399b85d","sup_e4fd7469cbe5c470d277"],"title":"surah begins with an unfinished setup","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:1","qac_refs":["110:1:1:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_65afc60613b0c1c06151","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:arrival-as-realization","source_type":"word_analysis","support_ids":["sup_233d4652c0624f301cef","sup_2a8188d6585519208a50"],"title":"arrival turns abstractions into events","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_4c4c7dd23721647252c3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:arrival-pairing-and-reversal-echoes","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_7fb0cd998a46f75a9971"],"title":"arrival joins aid and opening fields","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_48aaa479d30ed1fc2a57","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:form-i-arrival-not-causation","source_type":"word_analysis","support_ids":["sup_049cc396f12dab299c12","sup_2a8188d6585519208a50"],"title":"simple form foregrounds arrival","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_c7b82e29060188715137","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:intransitive-arrival-subjects","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_88a4586cfad83c922a92"],"title":"aid and opening are the arriving subjects","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_a29a6fe9674e93fecf6e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:perfect-under-condition","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_82ba896d06992eb9bfc2"],"title":"perfect form carries future certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_b3de02e0c9b1b5cf88bd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:singular-agreement-before-expansion","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_332cbb81e3b7e178729c"],"title":"singular verb precedes compound subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_32f3eba2998b133ff798","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:source-marked-arrival","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_f5b744a09ceef6beee4d"],"title":"arrival is routed through the divine-source phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_68224c7996b150cea665","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:2:stretched-then-arrested-sound","source_type":"word_analysis","support_ids":["sup_2a8188d6585519208a50","sup_bb0c01ea69f3cbe7a84b"],"title":"sound stretches arrival then closes it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:2","qac_refs":["110:1:2:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_648303d525048f0102e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:aid-victory-support-range","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_d259b3e8aefc4314b1ab"],"title":"aid carries victory and stabilizing support","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_30807dcf51aed565724c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:derivational-contrast","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_59c3f75574b84669861f"],"title":"maṣdar differs from helper and self-redress forms","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_3b7bb2ca3d1cebd906d8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:first-subject-maṣdar-arrival","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_216a20f0a321d64d2679"],"title":"aid arrives as the first bounded subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_ed1f50086cdc561c3593","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:genitive-role-pressure","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_206f3c7f356f92176ba3"],"title":"objective genitive remains secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_ec6ab364d2a41de8ac89","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:local-order-before-opening","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_95804015acb3a2feb13d"],"title":"source-bound aid is named before opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_a48bd7cc453570f69a57","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:recurrence-and-forward-response","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_b74ade42408ff3cb6296"],"title":"aid joins opening and demands response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_d127f8add62b48f01d61","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:release-and-opening-color","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_79822c68a1e670fff641"],"title":"release image touches the aid-opening pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_926323a320c0205664ab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:source-bound-construct-aid","source_type":"word_analysis","support_ids":["sup_087e3c094ed9d2a50c18","sup_75222553db0459eb5764"],"title":"construct binds aid to divine source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:3","qac_refs":["110:1:3:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_9262cc7ab0bf30a1ce6b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:compressed-name-form","source_type":"word_analysis","support_ids":["sup_1afcde5530c0944d5199","sup_8b17c824da607da0e4a3"],"title":"assimilated name compresses the source term","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_012a28e1cbb0cd5d6c38","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:construct-closure-before-wa","source_type":"word_analysis","support_ids":["sup_19659c58c6d77cc21512","sup_8b17c824da607da0e4a3"],"title":"genitive closes the first subject unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_9fc6f722b52e0518533b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:derivational-pressure-without-reparse","source_type":"word_analysis","support_ids":["sup_8b17c824da607da0e4a3","sup_dd5ec37996809d95dde4"],"title":"refuge and exaltation color the proper name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_37fd21320c38207aba65","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:divine-name-recurrence","source_type":"word_analysis","support_ids":["sup_8b17c824da607da0e4a3","sup_d819142d26336f3a4432"],"title":"same name links aid to religion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_6d0194ec3c8150eb0f93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:genitive-proper-name-source","source_type":"word_analysis","support_ids":["sup_473e7cfdf446e118d920","sup_8b17c824da607da0e4a3"],"title":"proper name completes the aid-source construct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_b30dd4f5ffbaa301349a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:4:qiraat-attachment-contrast","source_type":"word_analysis","support_ids":["sup_8b17c824da607da0e4a3","sup_951f1fb29ae6f4c7660c"],"title":"variant exposes the standard attachment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:4","qac_refs":["110:1:4:1"],"status":"accepted"}},{"anchor_refs":["110:1:5"],"branch_refs":[],"candidate_id":"cand_9bad9e4ca8aec1a5754c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:5:coordination-not-resumption","source_type":"word_analysis","support_ids":["sup_11a8183c0dafcd24e25c","sup_f6f3b52b6caaf3f433a4"],"title":"conjunction keeps two subjects under one verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:5","qac_refs":["110:1:5:1"],"status":"accepted"}},{"anchor_refs":["110:1:5"],"branch_refs":[],"candidate_id":"cand_01a14998f9edabae4c98","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:5:post-construct-pivot","source_type":"word_analysis","support_ids":["sup_f6f3b52b6caaf3f433a4","sup_fc08bf04c73e43403dd0"],"title":"particle separates construct aid from definite opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:5","qac_refs":["110:1:5:1"],"status":"accepted"}},{"anchor_refs":["110:1:5"],"branch_refs":[],"candidate_id":"cand_bfc2954aab1305f03829","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"110:1:5:recited-fusion-with-fatḥ","source_type":"word_analysis","support_ids":["sup_dedcfae43156d9502294","sup_f6f3b52b6caaf3f433a4"],"title":"connector binds audibly to the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:5","qac_refs":["110:1:5:1"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_414766b0a0c2a8844ecc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:access-water-derivative-color","source_type":"word_analysis","support_ids":["sup_385dd5c02104da156ac8","sup_76314189650e9587bbb5"],"title":"keys and water add access-release color","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_8dc8aaf7fec581a630eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:arrival-versus-seeking","source_type":"word_analysis","support_ids":["sup_385dd5c02104da156ac8","sup_b6b8aad379c8899a098f"],"title":"no seeker governs the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_4992583512158eb4ea64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:coordinated-arriving-subject","source_type":"word_analysis","support_ids":["sup_00d9986e6187ab6245d5","sup_385dd5c02104da156ac8"],"title":"opening arrives as second subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_be3b94580a46b083506b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:final-landing-and-forward-response","source_type":"word_analysis","support_ids":["sup_297f9ab095934144bf41","sup_385dd5c02104da156ac8"],"title":"final noun lands the condition and triggers response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_e2261a1bd056ab7af452","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:independent-definiteness-asymmetry","source_type":"word_analysis","support_ids":["sup_385dd5c02104da156ac8","sup_c52f05865888f22b296d"],"title":"article makes the opening identifiable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_7601558d1a2f407da37c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:opening-victory-judgment-polysemy","source_type":"word_analysis","support_ids":["sup_359344bff160639fa44a","sup_385dd5c02104da156ac8"],"title":"opening includes victory and judgment pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_5079a3a27189f023941c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:recurrence-definiteness-shift","source_type":"word_analysis","support_ids":["sup_385dd5c02104da156ac8","sup_9a83c8e0956f37e3bfed"],"title":"known opening contrasts with earlier near opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:6"],"branch_refs":[],"candidate_id":"cand_636aad829375c07201e8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:6:sound-pairing-and-throat-opening","source_type":"word_analysis","support_ids":["sup_1305ee0cdab860ad1c4b","sup_385dd5c02104da156ac8"],"title":"sound reinforces the paired subjects","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"110:1:6","qac_refs":["110:1:5:2","110:1:5:3"],"status":"accepted"}},{"anchor_refs":["110:1:2"],"branch_refs":[],"candidate_id":"cand_0bb10fa073d7b27336df","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000281"],"scope":"focus_ayah","source_local_id":"110:1:2:1","source_type":"qac_morpheme","support_ids":["sup_5637abd49e484631a0a7"],"title":"QAC root occurrence: ج ي ء","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["110:1:3"],"branch_refs":[],"candidate_id":"cand_6b5d015c407e9428142b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001510"],"scope":"focus_ayah","source_local_id":"110:1:3:1","source_type":"qac_morpheme","support_ids":["sup_7ba34438a88d622396c7"],"title":"QAC root occurrence: ن ص ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["110:1:4"],"branch_refs":[],"candidate_id":"cand_e2554dbae24eee19c9e5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"110:1:4:1","source_type":"qac_morpheme","support_ids":["sup_63e6453c1f129a5eaef6"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["110:1:5"],"branch_refs":[],"candidate_id":"cand_6a77936314db34938025","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001124"],"scope":"focus_ayah","source_local_id":"110:1:5:3","source_type":"qac_morpheme","support_ids":["sup_9cfb715b077aa0d75460"],"title":"QAC root occurrence: ف ت ح","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["110:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"110:1","branch_refs":["root_000047/B002","root_000281/B001","root_001124/B001","root_001510/B001"],"candidate_id":"cand_08161fcc24c8918b349e","commentary_obligation":"review","hft_ref":"hft_e94f4440a7d228fe6ae6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_arrival_aperture","source_type":"hft","support_ids":["sup_a2a6a26c6812ccce6e70"],"title":"baseline_arrival_aperture","trust":"legacy_unbound"},{"anchor_refs":["110:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"110:1","branch_refs":["root_000047/B002","root_000281/B001","root_001124/B003","root_001510/B002"],"candidate_id":"cand_9eeb8452160d3ed27d2b","commentary_obligation":"review","hft_ref":"hft_b6ff2642a166f03ce444","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_adjudicated_redress","source_type":"hft","support_ids":["sup_de5d80415ab6704241b1"],"title":"baseline_adjudicated_redress","trust":"legacy_unbound"},{"anchor_refs":["110:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"110:1","branch_refs":["root_000047/B001","root_000281/B004","root_001124/B008","root_001510/B005"],"candidate_id":"cand_30ab58e43c0fc20a78bf","commentary_obligation":"review","hft_ref":"hft_b2ab1aaf96b1c9fae0a1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_gifted_inner_opening","source_type":"hft","support_ids":["sup_9efe16c4be1033ee5e3e"],"title":"baseline_gifted_inner_opening","trust":"legacy_unbound"},{"anchor_refs":["110:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"110:1","branch_refs":["root_000281/B003","root_001124/B005","root_001510/B004","root_001510/B007"],"candidate_id":"cand_12b070938f64dc090076","commentary_obligation":"review","hft_ref":"hft_7109c1201dc86721333e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_hydraulic_relief","source_type":"hft","support_ids":["sup_082364b131bcf399f88b"],"title":"baseline_hydraulic_relief","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","qac_morphemes":[{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"110:1:1:1","qac_word_ref":"110:1:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"110:1:2:1","qac_word_ref":"110:1:2","root_ar":"ج ي ء","surface_ar":"جَآءَ"},{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","root_ar":"ن ص ر","surface_ar":"نَصْرُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"110:1:4:1","qac_word_ref":"110:1:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"110:1:5:1","qac_word_ref":"110:1:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"110:1:5:2","qac_word_ref":"110:1:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","root_ar":"ف ت ح","surface_ar":"فَتْحُ"}],"word_analysis_qac_refs":[["110:1:1:1"],["110:1:2:1"],["110:1:3:1"],["110:1:4:1"],["110:1:5:1"],["110:1:5:2","110:1:5:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["110:1:1","110:1:2","110:1:3","110:1:4","110:1:5","110:1:6"]},"focus_surface_evidence":{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","qac_morphemes":[{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"110:1:1:1","qac_word_ref":"110:1:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"جَآءَ","morph_features":"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"110:1:2:1","qac_word_ref":"110:1:2","root_ar":"ج ي ء","surface_ar":"جَآءَ"},{"lemma_ar":"نَصْر","morph_features":"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:3:1","qac_word_ref":"110:1:3","root_ar":"ن ص ر","surface_ar":"نَصْرُ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"110:1:4:1","qac_word_ref":"110:1:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"110:1:5:1","qac_word_ref":"110:1:5","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"110:1:5:2","qac_word_ref":"110:1:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَتْح","morph_features":"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"110:1:5:3","qac_word_ref":"110:1:5","root_ar":"ف ت ح","surface_ar":"فَتْحُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["110:1:1:1"],["110:1:2:1"],["110:1:3:1"],["110:1:4:1"],["110:1:5:1"],["110:1:5:2","110:1:5:3"]],"word_analysis_refs":["110:1:1","110:1:2","110:1:3","110:1:4","110:1:5","110:1:6"],"word_rows":[{"analysis_record_ref":"110:1:1","analytic_gloss_range_en":"temporal-conditional particle introducing a certain future event as the condition for the later response","analytic_root_gloss_range_en":null,"qac_refs":["110:1:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"110:1:2","analytic_gloss_range_en":"intransitive arrival of the following compound subject, with perfect form under the temporal condition carrying future certainty","analytic_root_gloss_range_en":"broad coming and bringing range; local absence of an object and nominative subjects select arrival or occurrence, not bringing or committing","qac_refs":["110:1:2:1"],"root":{"arabic":"ج ي أ","transliteration":"j-y-ʾ"},"surface":{"arabic":"جَآءَ","transliteration":"jāʾa"}},{"analysis_record_ref":"110:1:3","analytic_gloss_range_en":"source-bound aid, support, victory, and vindication as the first arriving subject","analytic_root_gloss_range_en":"broad range including aid that makes prevail, redress, rain-relief, gift, watercourse imagery, and unrelated affiliation branches; local construct and pairing select divine-source aid with victory and support pressure","qac_refs":["110:1:3:1"],"root":{"arabic":"ن ص ر","transliteration":"n-ṣ-r"},"surface":{"arabic":"نَصْرُ","transliteration":"naṣru"}},{"analysis_record_ref":"110:1:4","analytic_gloss_range_en":"genitive divine proper name completing the construct and marking the aid as source-bound","analytic_root_gloss_range_en":"proper divine name with derivational discussions around deity, refuge, and exaltation; local grammar selects the proper name as genitive source, not a generic deity phrase","qac_refs":["110:1:4:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهِ","transliteration":"allāhi"}},{"analysis_record_ref":"110:1:5","analytic_gloss_range_en":"coordinating conjunction joining the independently definite opening as second subject under the same arrival verb","analytic_root_gloss_range_en":null,"qac_refs":["110:1:5:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"110:1:6","analytic_gloss_range_en":"the identifiable opening, victory, and decisive settlement as the coordinated second subject that arrives","analytic_root_gloss_range_en":"broad opening field including physical opening, beginning, judgment, victory or conquest, water release, keys or access, treasuries, disclosure, and review-only marginal senses; local definiteness, coordination, and maṣdar subjecthood select decisive identifiable opening-victory with judgment pressure","qac_refs":["110:1:5:2","110:1:5:3"],"root":{"arabic":"ف ت ح","transliteration":"f-t-ḥ"},"surface":{"arabic":"ٱلْفَتْحُ","transliteration":"al-fatḥu"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["110:1"],"branch_refs":["root_000047/B002","root_000281/B001","root_001124/B001","root_001510/B001"],"candidate_id":"cand_08161fcc24c8918b349e","evidence_scope":"focus_ayah","hft_ref":"hft_e94f4440a7d228fe6ae6","item_id":"baseline_arrival_aperture","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_arrival_aperture","support_id":"sup_a2a6a26c6812ccce6e70"},{"anchor_refs":["110:1"],"branch_refs":["root_000047/B002","root_000281/B001","root_001124/B003","root_001510/B002"],"candidate_id":"cand_9eeb8452160d3ed27d2b","evidence_scope":"focus_ayah","hft_ref":"hft_b6ff2642a166f03ce444","item_id":"baseline_adjudicated_redress","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_adjudicated_redress","support_id":"sup_de5d80415ab6704241b1"},{"anchor_refs":["110:1"],"branch_refs":["root_000047/B001","root_000281/B004","root_001124/B008","root_001510/B005"],"candidate_id":"cand_30ab58e43c0fc20a78bf","evidence_scope":"focus_ayah","hft_ref":"hft_b2ab1aaf96b1c9fae0a1","item_id":"baseline_gifted_inner_opening","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_gifted_inner_opening","support_id":"sup_9efe16c4be1033ee5e3e"},{"anchor_refs":["110:1"],"branch_refs":["root_000281/B003","root_001124/B005","root_001510/B004","root_001510/B007"],"candidate_id":"cand_12b070938f64dc090076","evidence_scope":"focus_ayah","hft_ref":"hft_7109c1201dc86721333e","item_id":"baseline_hydraulic_relief","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_hydraulic_relief","support_id":"sup_082364b131bcf399f88b"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":4},"packet_summary":{"ayah_count":3,"focus_ref":"110:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ت و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000189","furuq_root_norm":"ت و ب","furuq_source_root_norm":"ت و ب","is_dominant":true,"target_occurrences":68,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000172","furuq_root_norm":"ت ب ب","furuq_source_root_norm":"ت ب ب","is_dominant":false,"target_occurrences":5,"target_rank":2}]}],"window":["110:1","110:2","110:3"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"110:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"110:1","lane":"micro","linguistic_source_ref":"110:1","surface_ref":"110:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"110:1","target_tokens":[["Allah'ın",["110:1:4"]],["yardımı",["110:1:3","110:1:4"]],["ve",["110:1:5"]],["zafer",["110:1:5"]],["geldiğinde",["110:1:1","110:1:2"]]],"text":"Allah'ın yardımı ve zafer geldiğinde,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":3,"id":"s110-p01-001-003","label":"Whole surah","number":1,"refs":["110:1","110:2","110:3"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:coordinated-arriving-subject","source_type":"word_analysis","support_id":"sup_00d9986e6187ab6245d5","text":"{\"blocking_evidence\":null,\"headline\":\"opening arrives as second subject\",\"reader_payoff\":\"The reader notices that opening itself arrives under the shared verb, rather than being something performed on an unstated object.\",\"reason\":\"QAC and attachment evidence mark {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) as nominative and coordinated with {{ar:نَصْرُ}} ({{tr:naṣru}}) under {{ar:جَآءَ}} ({{tr:jāʾa}}).\",\"representative_source_ids\":[\"QG-73a6a1ff\",\"QG-f6930ca0\",\"QF-aa2d4ff2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:form-i-arrival-not-causation","source_type":"word_analysis","support_id":"sup_049cc396f12dab299c12","text":"{\"blocking_evidence\":null,\"headline\":\"simple form foregrounds arrival\",\"reader_payoff\":\"The reader notices that the chosen simple verb foregrounds the event arriving, while local grammar blocks shifting the focus to a causative bringing construction.\",\"reason\":\"The surface is Form I perfect, and the local frame is intransitive; the contrast with causation is useful only as a boundary, not as an activated alternate construction.\",\"representative_source_ids\":[\"QF-5b1ac89e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3","source_type":"word_analysis","support_id":"sup_087e3c094ed9d2a50c18","text":"{\"gloss_range\":\"source-bound aid, support, victory, and vindication as the first arriving subject\",\"prose\":\"{{ar:نَصْرُ}} ({{tr:naṣru}}) is the first arriving subject, and its construct with {{ar:ٱللَّهِ}} ({{tr:allāhi}}) makes the aid definite and source-bound. A maṣdar construct can allow more than one genitive relation, so aid for God's cause remains a secondary pressure, but the local arrival clause favors aid from God before any human recipient is named. The noun form turns helping into one bounded event that can arrive alongside {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}), naming the support itself rather than a helper class, self-redress, or responder motion. Its root range keeps aid, support, victory, vindication, and rescue in view; the rain and watering images make the support feel life-giving, the standing-firm image makes it stabilizing, and the release image lets it touch the opening field without replacing the aid sense. The exact noun choice is sharper than a generic helper or verb form, and its first-subject position foregrounds source-bound aid before the ayah lands on opening. The pairing with opening recalls the aid-and-opening field of 61:13, while delayed aid-arrival formulas at 12:110 and 6:34 keep the arrival pressure visible; this received aid prepares the response of glorification and seeking forgiveness in 110:3.\",\"root_display\":\"{{ar:ن ص ر}} ({{tr:n-ṣ-r}})\",\"root_gloss_range\":\"broad range including aid that makes prevail, redress, rain-relief, gift, watercourse imagery, and unrelated affiliation branches; local construct and pairing select divine-source aid with victory and support pressure\",\"surface_display\":\"{{ar:نَصْرُ}} ({{tr:naṣru}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:5:coordination-not-resumption","source_type":"word_analysis","support_id":"sup_11a8183c0dafcd24e25c","text":"{\"blocking_evidence\":null,\"headline\":\"conjunction keeps two subjects under one verb\",\"reader_payoff\":\"The reader notices that the opening belongs to the same arrival event as God's aid, not to a new sentence or background circumstance.\",\"reason\":\"QAC and attachment evidence identify the particle as coordination linking {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) to {{ar:نَصْرُ ٱللَّهِ}} ({{tr:naṣru llāhi}}) as co-subjects of {{ar:جَآءَ}} ({{tr:jāʾa}}).\",\"representative_source_ids\":[\"QG-75f0292c\",\"QS-f0ed1ca6\",\"QT-7a7ee82d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:sound-pairing-and-throat-opening","source_type":"word_analysis","support_id":"sup_1305ee0cdab860ad1c4b","text":"{\"blocking_evidence\":null,\"headline\":\"sound reinforces the paired subjects\",\"reader_payoff\":\"The reader notices that the final throat consonant and repeated nominative cadence give the opening word an audible aperture while tying it to the aid noun.\",\"reason\":\"The phonetic observation is compatible with the root's final consonant and with the shared nominative subject cadence of {{ar:نَصْرُ}} ({{tr:naṣru}}) and {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}).\",\"representative_source_ids\":[\"QP-a85c9a7a\",\"QP-ecb06ed7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:construct-closure-before-wa","source_type":"word_analysis","support_id":"sup_19659c58c6d77cc21512","text":"{\"blocking_evidence\":null,\"headline\":\"genitive closes the first subject unit\",\"reader_payoff\":\"The reader notices that the divine genitive completes the first subject before the conjunction introduces a distinct second subject.\",\"reason\":\"Attachment evidence identifies the iḍāfa relation between words 3 and 4 and the coordination of word 6 after word 5.\",\"representative_source_ids\":[\"QT-0d38557f\",\"QT-5d7d5007\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:compressed-name-form","source_type":"word_analysis","support_id":"sup_1afcde5530c0944d5199","text":"{\"blocking_evidence\":null,\"headline\":\"assimilated name compresses the source term\",\"reader_payoff\":\"The reader notices the divine source as a compact, acoustically weighted proper-name surface rather than an expanded analytic title.\",\"reason\":\"QAC reports the al-plus-ilāh analysis with hamza elision and lām assimilation as one analysis; the local payoff is surface compression and sound weight, not a replacement of proper-name status.\",\"representative_source_ids\":[\"QF-80fee827\",\"QF-f53ebd2f\",\"QP-b17829b6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:genitive-role-pressure","source_type":"word_analysis","support_id":"sup_206f3c7f356f92176ba3","text":"{\"blocking_evidence\":null,\"headline\":\"objective genitive remains secondary\",\"reader_payoff\":\"The reader notices that the construct can also suggest aid for God's cause, while the local arrival frame keeps source as the stronger reading.\",\"reason\":\"The maṣdar construct can bear objective pressure, but the immediate grammar identifies God as the genitive source of the arriving aid.\",\"representative_source_ids\":[\"QG-0f80f74d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:first-subject-maṣdar-arrival","source_type":"word_analysis","support_id":"sup_216a20f0a321d64d2679","text":"{\"blocking_evidence\":null,\"headline\":\"aid arrives as the first bounded subject\",\"reader_payoff\":\"The reader notices that helping is nominalized into one source-bound arrival before the coordinated opening is added.\",\"reason\":\"QAC marks {{ar:نَصْرُ}} ({{tr:naṣru}}) as nominative subject and construct head, and attachment evidence makes it the first subject of {{ar:جَآءَ}} ({{tr:jāʾa}}).\",\"representative_source_ids\":[\"QG-c99b2e4a\",\"QF-b961c6a1\",\"QF-d3f42aaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:arrival-as-realization","source_type":"word_analysis","support_id":"sup_233d4652c0624f301cef","text":"{\"blocking_evidence\":null,\"headline\":\"arrival turns abstractions into events\",\"reader_payoff\":\"The reader notices that aid and opening are not static labels; the verb makes them cross into the scene as realized happenings.\",\"reason\":\"The local intransitive frame licenses event-arrival, so the broader coming field is realized as movement into presence rather than as transitive bringing.\",\"representative_source_ids\":[\"QS-c8c0cd25\",\"QS-c8d197cc\",\"QS-dea071b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:final-landing-and-forward-response","source_type":"word_analysis","support_id":"sup_297f9ab095934144bf41","text":"{\"blocking_evidence\":null,\"headline\":\"final noun lands the condition and triggers response\",\"reader_payoff\":\"The reader notices that the ayah closes on the opening as the audible endpoint of the condition, which then leads to the command response in 110:3.\",\"reason\":\"The word is the final term of 110:1 and attachment support links the temporal condition to the imperative sequence in 110:3.\",\"representative_source_ids\":[\"MI-36e3019f\",\"QT-76e05492\",\"QT-87f01959\",\"QT-c31670d1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2","source_type":"word_analysis","support_id":"sup_2a8188d6585519208a50","text":"{\"gloss_range\":\"intransitive arrival of the following compound subject, with perfect form under the temporal condition carrying future certainty\",\"prose\":\"{{ar:جَآءَ}} ({{tr:jāʾa}}) turns the condition into an arrival scene. The verb is perfect in form, but under {{ar:إِذَا}} ({{tr:idhā}}) it points to a future event treated as already sure. Locally it is intransitive: {{ar:نَصْرُ ٱللَّهِ}} ({{tr:naṣru llāhi}}) and {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) are the arriving subjects, not objects brought by an unstated agent. The simple Form I shape foregrounds the event arriving rather than a causative bringing. The singular verb first agrees with the masculine singular aid-phrase, then the subject expands by coordination. This makes aid and opening enter the scene as realized turning points, with aid marked as an arriving reversal point in recurrence fields such as 30:47 and 29:10. The echoes with seeking an opening in 8:19 and with gates opening after arrival in 39:71 and 39:73 sharpen the local reversal, because here the opening itself is one of the things that comes.\",\"root_display\":\"{{ar:ج ي أ}} ({{tr:j-y-ʾ}})\",\"root_gloss_range\":\"broad coming and bringing range; local absence of an object and nominative subjects select arrival or occurrence, not bringing or committing\",\"surface_display\":\"{{ar:جَآءَ}} ({{tr:jāʾa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:singular-agreement-before-expansion","source_type":"word_analysis","support_id":"sup_332cbb81e3b7e178729c","text":"{\"blocking_evidence\":null,\"headline\":\"singular verb precedes compound subject\",\"reader_payoff\":\"The reader notices the grammar lock onto the first subject before the wording expands to include the coordinated opening.\",\"reason\":\"QAC marks the verb as third masculine singular and explains that it agrees with the first masculine singular element of the compound subject.\",\"representative_source_ids\":[\"QG-1b76f062\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:opening-victory-judgment-polysemy","source_type":"word_analysis","support_id":"sup_359344bff160639fa44a","text":"{\"blocking_evidence\":null,\"headline\":\"opening includes victory and judgment pressure\",\"reader_payoff\":\"The reader notices that the final word is not a flat victory label; it carries barrier-removal, conquest, judgment, disclosure, and decisive settlement together.\",\"reason\":\"V4 accepts physical opening, judgment, victory, disclosure, and related branches for {{ar:ف ت ح}} ({{tr:f-t-ḥ}}); local definiteness and pairing with aid select decisive opening-victory with judgment pressure, not every branch as a separate local sense.\",\"representative_source_ids\":[\"QS-76cdf89f\",\"QS-cf2b0f7f\",\"QS-df76672d\",\"QS-ffaea9e4\",\"QY-468515da\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6","source_type":"word_analysis","support_id":"sup_385dd5c02104da156ac8","text":"{\"gloss_range\":\"the identifiable opening, victory, and decisive settlement as the coordinated second subject that arrives\",\"prose\":\"{{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) completes the compound subject as the ayah's final landing. It is nominative and coordinated, so the opening arrives with the aid rather than being the object of an unspoken opener. Its article makes it independently definite: not an indefinite opening and not, in the standard reading, a second construct governed by {{ar:ٱللَّهِ}} ({{tr:allāhi}}). The root field lets opening, conquest, victory, judgment, disclosure, access, and release press together, while local grammar keeps the selected sense as the recognizable decisive opening-victory; the judgment sense keeps dispute-resolution pressure visible through 26:118 and 7:89. Key and water imagery make the event feel access-controlled and release-like without taking over the parse. The contrast with the indefinite near opening of 61:13, the seeking-and-coming pattern of 8:19, and the opening-victory passages at 48:1, 48:18, and 48:27 make this final noun feel like a known arrival rather than a vague success. It also drives forward to the response in 110:3, where victory leads to glorification and seeking forgiveness rather than celebration. Its final pharyngeal ḥ gives the word an open-throat aperture, and its nominative -u repeats the aid noun's subject cadence.\",\"root_display\":\"{{ar:ف ت ح}} ({{tr:f-t-ḥ}})\",\"root_gloss_range\":\"broad opening field including physical opening, beginning, judgment, victory or conquest, water release, keys or access, treasuries, disclosure, and review-only marginal senses; local definiteness, coordination, and maṣdar subjecthood select decisive identifiable opening-victory with judgment pressure\",\"surface_display\":\"{{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:genitive-proper-name-source","source_type":"word_analysis","support_id":"sup_473e7cfdf446e118d920","text":"{\"blocking_evidence\":null,\"headline\":\"proper name completes the aid-source construct\",\"reader_payoff\":\"The reader notices that the aid is specified by the divine proper name as source, not left as generic agency or possession.\",\"reason\":\"QAC marks {{ar:ٱللَّهِ}} ({{tr:allāhi}}) as a genitive proper noun and attachment evidence forces it as the muḍāf ilayh of {{ar:نَصْرُ}} ({{tr:naṣru}}).\",\"representative_source_ids\":[\"QG-338573d1\",\"QG-671435be\",\"QS-9c6734e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"110:1:2:1","source_type":"qac_morpheme","support_id":"sup_5637abd49e484631a0a7","text":"{\"lemma_ar\":\"جَآءَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:jaA^'a|ROOT:jyA|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"110:1:2:1\",\"qac_word_ref\":\"110:1:2\",\"root_ar\":\"ج ي ء\",\"surface_ar\":\"جَآءَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:derivational-contrast","source_type":"word_analysis","support_id":"sup_59c3f75574b84669861f","text":"{\"blocking_evidence\":null,\"headline\":\"maṣdar differs from helper and self-redress forms\",\"reader_payoff\":\"The reader notices that the ayah names the support itself, not a helper class, a self-vindicating actor, or someone moving in response to a plea.\",\"reason\":\"The wider derivational family is real, but the local surface is a singular maṣdar subject, so related forms function as contrast rather than active parses.\",\"representative_source_ids\":[\"QS-8e2e9032\",\"QF-578cab33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"110:1:4:1","source_type":"qac_morpheme","support_id":"sup_63e6453c1f129a5eaef6","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"110:1:4:1\",\"qac_word_ref\":\"110:1:4\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:1:surah-opening-protasis","source_type":"word_analysis","support_id":"sup_6f255380f7653399b85d","text":"{\"blocking_evidence\":null,\"headline\":\"surah begins with an unfinished setup\",\"reader_payoff\":\"The reader notices that the first ayah opens grammatical dependency that is completed only by the later imperative response in 110:3.\",\"reason\":\"Attachment support treats 110:1 as the protasis and links the consequent to the imperative sequence in 110:3.\",\"representative_source_ids\":[\"QT-21132964\",\"QT-7ee60e7b\",\"QT-c4baad97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:source-bound-construct-aid","source_type":"word_analysis","support_id":"sup_75222553db0459eb5764","text":"{\"blocking_evidence\":null,\"headline\":\"construct binds aid to divine source\",\"reader_payoff\":\"The reader notices that the aid is not generic help; the construct makes it definite and sourced from God, while only secondarily allowing aid directed toward God's cause.\",\"reason\":\"QAC and attachment evidence force the iḍāfa with {{ar:ٱللَّهِ}} ({{tr:allāhi}}); the source reading is locally favored by the phrase serving as the arriving subject, though maṣdar construct pressure leaves an objective nuance available.\",\"representative_source_ids\":[\"QG-aa92eed7\",\"QG-d12fb775\",\"QS-bee075c1\",\"QY-1f24e4c0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:access-water-derivative-color","source_type":"word_analysis","support_id":"sup_76314189650e9587bbb5","text":"{\"blocking_evidence\":null,\"headline\":\"keys and water add access-release color\",\"reader_payoff\":\"The reader notices that the opening feels access-controlled and release-like, with key and water imagery coloring the decisive event.\",\"reason\":\"V4 supports key, access, and water-release branches, but the local word is the gerund {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}), so these branches enrich the image without becoming the selected gloss.\",\"representative_source_ids\":[\"QS-2a7eae9a\",\"QS-7fb3750f\",\"QS-e2e5e0b7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:release-and-opening-color","source_type":"word_analysis","support_id":"sup_79822c68a1e670fff641","text":"{\"blocking_evidence\":null,\"headline\":\"release image touches the aid-opening pair\",\"reader_payoff\":\"The reader notices that aid and opening are not merely adjacent synonyms; they share a release-and-arrival pressure reinforced by their paired nominative cadence.\",\"reason\":\"The release image is lexically attested but secondary; local coordination with {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) lets it color the pair without replacing the aid sense.\",\"representative_source_ids\":[\"QS-ae95f766\",\"QI-5e9f54b9\",\"QP-9f19a0e6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"110:1:3:1","source_type":"qac_morpheme","support_id":"sup_7ba34438a88d622396c7","text":"{\"lemma_ar\":\"نَصْر\",\"morph_features\":\"STEM|POS:N|LEM:naSor|ROOT:nSr|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"110:1:3:1\",\"qac_word_ref\":\"110:1:3\",\"root_ar\":\"ن ص ر\",\"surface_ar\":\"نَصْرُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:arrival-pairing-and-reversal-echoes","source_type":"word_analysis","support_id":"sup_7fb0cd998a46f75a9971","text":"{\"blocking_evidence\":null,\"headline\":\"arrival joins aid and opening fields\",\"reader_payoff\":\"The reader notices that the arrival verb binds aid, opening, and divine-source language into a turning-point formula, with the opening itself arriving rather than merely following someone else's arrival.\",\"reason\":\"The supplied co-occurrence and echo rows cite concrete parallels such as 8:19, 39:71, and 39:73, while the local grammar confirms that {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) is a subject of {{ar:جَآءَ}} ({{tr:jāʾa}}).\",\"representative_source_ids\":[\"QI-9b7e5d97\",\"QI-9ca3ff40\",\"QE-902c5958\",\"QE-fa734fe5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:perfect-under-condition","source_type":"word_analysis","support_id":"sup_82ba896d06992eb9bfc2","text":"{\"blocking_evidence\":null,\"headline\":\"perfect form carries future certainty\",\"reader_payoff\":\"The reader notices that the verb is not an ordinary past report; the conditional particle makes the future event sound completed and sure.\",\"reason\":\"QAC states that the perfect verb after {{ar:إِذَا}} ({{tr:idhā}}) expresses future certainty, and the attachment evidence keeps the verb inside that temporal protasis.\",\"representative_source_ids\":[\"QG-d9570f0b\",\"QG-fe0809c5\",\"QI-906e5d50\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:intransitive-arrival-subjects","source_type":"word_analysis","support_id":"sup_88a4586cfad83c922a92","text":"{\"blocking_evidence\":null,\"headline\":\"aid and opening are the arriving subjects\",\"reader_payoff\":\"The reader notices that aid and opening are made to arrive in their own right, rather than being objects carried by an unnamed actor.\",\"reason\":\"The local verb instance has no object, and QAC identifies {{ar:نَصْرُ}} ({{tr:naṣru}}) with the coordinated {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) as subject.\",\"representative_source_ids\":[\"QG-33d0463b\",\"QS-d04bf0ff\",\"MI-ee23a085\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4","source_type":"word_analysis","support_id":"sup_8b17c824da607da0e4a3","text":"{\"gloss_range\":\"genitive divine proper name completing the construct and marking the aid as source-bound\",\"prose\":\"{{ar:ٱللَّهِ}} ({{tr:allāhi}}) completes the construct {{ar:نَصْرُ ٱللَّهِ}} ({{tr:naṣru llāhi}}), so the aid is heard as source-bound before the ayah turns to the independently definite opening. The word is a proper name in the genitive, not a generic agent label. Its compressed surface, from the al-plus-ilāh analysis with assimilation, makes that source term dense and singular; the documented derivational pressures of refuge and exaltation enrich the name without displacing the proper-name reading. The accepted variant that attaches the divine name to opening shows that a different genitive distribution was available, which makes the standard reading's attachment to aid more visible. Familiar source-formula anchors such as 61:13, 29:10, and 2:214 concentrate in this compact genitive phrase. The name then recurs in 110:2 with the religion-domain, binding the arrival of aid to the later entry into God's religion.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"proper divine name with derivational discussions around deity, refuge, and exaltation; local grammar selects the proper name as genitive source, not a generic deity phrase\",\"surface_display\":\"{{ar:ٱللَّهِ}} ({{tr:allāhi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:qiraat-attachment-contrast","source_type":"word_analysis","support_id":"sup_951f1fb29ae6f4c7660c","text":"{\"blocking_evidence\":null,\"headline\":\"variant exposes the standard attachment\",\"reader_payoff\":\"The reader notices that the standard reading deliberately attaches the divine name to aid even though an opening-linked divine construct is visible in the variant and recurrence field.\",\"reason\":\"The variant can illuminate contrast, but canonical local syntax attaches {{ar:ٱللَّهِ}} ({{tr:allāhi}}) to {{ar:نَصْرُ}} ({{tr:naṣru}}), not to {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}).\",\"representative_source_ids\":[\"QF-e6463827\",\"QI-b7ca04cf\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:local-order-before-opening","source_type":"word_analysis","support_id":"sup_95804015acb3a2feb13d","text":"{\"blocking_evidence\":null,\"headline\":\"source-bound aid is named before opening\",\"reader_payoff\":\"The reader notices that the exact noun choice and first-subject position foreground aid before the ayah lands on opening.\",\"reason\":\"The noun is a small exact-form group in the contextual profile and stands as the first subject before coordination introduces the second subject.\",\"representative_source_ids\":[\"QT-34d83120\",\"QT-c3501130\",\"QI-34420fc0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:recurrence-definiteness-shift","source_type":"word_analysis","support_id":"sup_9a83c8e0956f37e3bfed","text":"{\"blocking_evidence\":null,\"headline\":\"known opening contrasts with earlier near opening\",\"reader_payoff\":\"The reader notices that this definite opening stands inside a Quranic opening-victory field, especially against the indefinite near opening and aid-from-God pairing of 61:13.\",\"reason\":\"The recurrence rows cite 61:13 and opening-victory passages at 48:1, 48:18, and 48:27, while the local form is independently definite and coordinated with source-bound aid.\",\"representative_source_ids\":[\"QF-a5acb423\",\"QI-a812fd56\",\"QI-e98793b2\",\"QE-c6205efb\",\"QE-e3b13398\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"110:1:5:3","source_type":"qac_morpheme","support_id":"sup_9cfb715b077aa0d75460","text":"{\"lemma_ar\":\"فَتْح\",\"morph_features\":\"STEM|POS:N|LEM:fatoH|ROOT:ftH|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"110:1:5:3\",\"qac_word_ref\":\"110:1:5\",\"root_ar\":\"ف ت ح\",\"surface_ar\":\"فَتْحُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:1:future-certain-condition","source_type":"word_analysis","support_id":"sup_a9d7fff2da1062a42c91","text":"{\"blocking_evidence\":null,\"headline\":\"condition is certain, not hypothetical\",\"reader_payoff\":\"The reader notices that the opening word frames the event as a trusted when, not a doubtful if.\",\"reason\":\"QAC and attachment evidence identify {{ar:إِذَا}} ({{tr:idhā}}) as the temporal-conditional particle governing the clause, and QAC explicitly distinguishes its confident future force from a doubtful conditional.\",\"representative_source_ids\":[\"QG-0e1d681f\",\"MG-38d17acd\",\"QS-7e6ccd50\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:arrival-versus-seeking","source_type":"word_analysis","support_id":"sup_b6b8aad379c8899a098f","text":"{\"blocking_evidence\":null,\"headline\":\"no seeker governs the opening\",\"reader_payoff\":\"The reader notices that the opening is not requested in this ayah; it arrives as the subject, reversing the seeking-and-coming pattern visible in 8:19.\",\"reason\":\"The local maṣdar is subject of {{ar:جَآءَ}} ({{tr:jāʾa}}), while the supplied 8:19 echo supplies a contrast where opening or decision is sought and comes to seekers.\",\"representative_source_ids\":[\"QF-daf4a765\",\"QI-bb28ea14\",\"QE-4eab3882\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:recurrence-and-forward-response","source_type":"word_analysis","support_id":"sup_b74ade42408ff3cb6296","text":"{\"blocking_evidence\":null,\"headline\":\"aid joins opening and demands response\",\"reader_payoff\":\"The reader notices that source-bound aid belongs to a recurring aid-arrival field and, in this surah, leads forward to the commands of 110:3.\",\"reason\":\"The supplied rows cite concrete recurrence anchors including 61:13 and link the conditional setup of 110:1 to the imperative response in 110:3.\",\"representative_source_ids\":[\"QI-0d17781a\",\"MI-24f58dfe\",\"QE-7d5cb44b\",\"QE-ff48420c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:stretched-then-arrested-sound","source_type":"word_analysis","support_id":"sup_bb0c01ea69f3cbe7a84b","text":"{\"blocking_evidence\":null,\"headline\":\"sound stretches arrival then closes it\",\"reader_payoff\":\"The reader notices that the long vowel followed by final hamza gives the arrival word an audible stretch and stop.\",\"reason\":\"The written and recited shape of {{ar:جَآءَ}} ({{tr:jāʾa}}) supports the phonetic observation without changing the grammatical analysis.\",\"representative_source_ids\":[\"QF-92d92c31\",\"QP-b71af348\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:6:independent-definiteness-asymmetry","source_type":"word_analysis","support_id":"sup_c52f05865888f22b296d","text":"{\"blocking_evidence\":null,\"headline\":\"article makes the opening identifiable\",\"reader_payoff\":\"The reader notices that the opening is definite in its own right, standing beside but not grammatically possessed by the divine name in the standard reading.\",\"reason\":\"The word carries the definite article and no genitive complement; the available variant with divine genitive functions as contrast while standard syntax keeps independent definiteness.\",\"representative_source_ids\":[\"QG-8a4c4d15\",\"QG-cd20e667\",\"MG-5c5052a4\",\"QF-ef134f98\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:3:aid-victory-support-range","source_type":"word_analysis","support_id":"sup_d259b3e8aefc4314b1ab","text":"{\"blocking_evidence\":null,\"headline\":\"aid carries victory and stabilizing support\",\"reader_payoff\":\"The reader notices that the word's aid is not thin assistance; it carries triumph, vindication, stabilizing support, and even reviving provision as concrete pressure.\",\"reason\":\"V4 supports aid that makes prevail and rain-relief branches for {{ar:ن ص ر}} ({{tr:n-ṣ-r}}), while the local construct selects source-backed aid rather than turning the word into a literal rain term.\",\"representative_source_ids\":[\"QS-33419fea\",\"QS-6f10cd04\",\"QS-789990de\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:divine-name-recurrence","source_type":"word_analysis","support_id":"sup_d819142d26336f3a4432","text":"{\"blocking_evidence\":null,\"headline\":\"same name links aid to religion\",\"reader_payoff\":\"The reader notices that the divine name concentrates familiar source formulas in 110:1 and then recurs with the religion-domain in 110:2.\",\"reason\":\"The supplied rows cite divine-name pairing with aid and identify the same-surah recurrence from the aid-source phrase in 110:1 to the religion phrase in 110:2.\",\"representative_source_ids\":[\"MI-d42cce59\",\"QE-fac70902\",\"QI-b9f6fb86\",\"QE-1495ad0d\",\"QI-a6c89e9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:4:derivational-pressure-without-reparse","source_type":"word_analysis","support_id":"sup_dd5ec37996809d95dde4","text":"{\"blocking_evidence\":null,\"headline\":\"refuge and exaltation color the proper name\",\"reader_payoff\":\"The reader notices that refuge and exaltation pressures can enrich the divine name while the local grammar keeps it functioning as the proper name.\",\"reason\":\"The derivational dispute around {{ar:أ ل ه}} ({{tr:ʾ-l-h}}) and {{ar:و ل ه}} ({{tr:w-l-h}}) is interpretive pressure only; QAC and contextual evidence keep the local token as the dominant divine proper noun.\",\"representative_source_ids\":[\"QS-281189de\",\"QS-7b251e50\",\"QS-eb0e1ff3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:5:recited-fusion-with-fatḥ","source_type":"word_analysis","support_id":"sup_dedcfae43156d9502294","text":"{\"blocking_evidence\":null,\"headline\":\"connector binds audibly to the opening\",\"reader_payoff\":\"The reader notices that the connector is not only grammatical; its recited liaison makes the bond to the opening immediate.\",\"reason\":\"The particle precedes a hamzat-waṣl definite noun, so the recitation binds {{ar:وَ}} ({{tr:wa}}) directly to {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}).\",\"representative_source_ids\":[\"QF-066c635c\",\"QP-d1f18bec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:1","source_type":"word_analysis","support_id":"sup_e4fd7469cbe5c470d277","text":"{\"gloss_range\":\"temporal-conditional particle introducing a certain future event as the condition for the later response\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) opens the surah by making the first ayah a condition rather than a self-contained report. Its force is temporal and conditional: when the arrival happens, the response will be required. Because it stands before a perfect verb, the event is future in the discourse but treated as certain, not left as a doubtful possibility. The clause therefore waits structurally for its answer in 110:3, where the command sequence supplies the response.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:2:source-marked-arrival","source_type":"word_analysis","support_id":"sup_f5b744a09ceef6beee4d","text":"{\"blocking_evidence\":null,\"headline\":\"arrival is routed through the divine-source phrase\",\"reader_payoff\":\"The reader notices that the verb stands as the pivot from the condition into a compound subject whose first element is source-marked as God's aid.\",\"reason\":\"The verb governs the subject phrase beginning with {{ar:نَصْرُ ٱللَّهِ}} ({{tr:naṣru llāhi}}), so the arrival is immediately specified by a divine-source construct.\",\"representative_source_ids\":[\"QI-b848201c\",\"QT-cbd17b34\",\"QT-e0f5fa0a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:5","source_type":"word_analysis","support_id":"sup_f6f3b52b6caaf3f433a4","text":"{\"gloss_range\":\"coordinating conjunction joining the independently definite opening as second subject under the same arrival verb\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is the small hinge that keeps the ayah from collapsing into a single noun pile. It follows the completed construct {{ar:نَصْرُ ٱللَّهِ}} ({{tr:naṣru llāhi}}) and coordinates {{ar:ٱلْفَتْحُ}} ({{tr:al-fatḥu}}) as a second subject under the same verb {{ar:جَآءَ}} ({{tr:jāʾa}}). That selects conjunction over circumstantial, oath, or resumptive uses: the opening co-arrives with the aid rather than beginning a new clause or serving as background. In recitation the connector fuses immediately into the following definite noun, making the syntactic bond audible.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"110:1:5:post-construct-pivot","source_type":"word_analysis","support_id":"sup_fc08bf04c73e43403dd0","text":"{\"blocking_evidence\":null,\"headline\":\"particle separates construct aid from definite opening\",\"reader_payoff\":\"The reader notices that the conjunction stands after construct closure, preserving the asymmetry between source-bound aid and independently definite opening.\",\"reason\":\"The iḍāfa closes at word 4 before {{ar:وَ}} ({{tr:wa}}), and word 6 is then coordinated as a separate nominative subject.\",\"representative_source_ids\":[\"QG-591b2a03\",\"QT-638fb871\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","ayah_ref":"110:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000281/B001","root_001124/B001","root_001510/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000281","role":"Coming and arrival supply the threshold at which aid becomes present rather than remaining a static possession.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001510","role":"Aid that makes someone prevail supplies the enabling force of the event.","root":"ن ص ر","source_ref":"110:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name identifies the aid's source and prevents an unnamed human actor from absorbing that role.","root":"ء ل ه","source_ref":"110:1","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001124","role":"Opening a closure and widening an aperture supply the changed state paired with the arriving aid.","root":"ف ت ح","source_ref":"110:1","source_word_indices":["5"]}],"changed_reading":{"after":"A threshold mechanism in which enabling aid becomes present and a blocked field becomes traversably open.","before":"A compact promise that divine victory will happen."},"confidence":"strong","focus_anchor":"The conditional إذا, the arrival verb جاء, and the coordinated nouns نصر الله and الفتح make the ayah an event threshold.","mechanism":"Aid becomes present, then a formerly closed state is rendered open. The coordination keeps enabling support and opened outcome distinguishable rather than reducing both nouns to one generic victory label.","model_id":"baseline_arrival_aperture"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_arrival_aperture","source_type":"hft","support_id":"sup_a2a6a26c6812ccce6e70","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","ayah_ref":"110:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B002","root_000281/B001","root_001124/B003","root_001510/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000281","role":"Arrival supplies the moment at which a previously pending settlement takes effect.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001510","role":"Redress after oppression recasts aid as the restoration of a wronged party.","root":"ن ص ر","source_ref":"110:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000047","role":"The fixed divine name locates the authority of the redress beyond the disputants.","root":"ء ل ه","source_ref":"110:1","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001124","role":"Judgment that resolves a closed dispute supplies the decisive settlement paired with redress.","root":"ف ت ح","source_ref":"110:1","source_word_indices":["5"]}],"changed_reading":{"after":"Victory can also be a divinely authorized redress that closes oppression by settling what had remained judicially locked.","before":"Victory is chiefly the defeat of an opposing force."},"confidence":"medium","focus_anchor":"نصر can image redress after oppression while الفتح can image judgment that settles a closed dispute.","mechanism":"The paired nouns can describe a juridical event: divine redress arrives and an unresolved conflict is decisively opened by adjudication. This coexists with, rather than cancels, the military-prevailing reading.","model_id":"baseline_adjudicated_redress"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_adjudicated_redress","source_type":"hft","support_id":"sup_de5d80415ab6704241b1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","ayah_ref":"110:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000281/B004","root_001124/B008","root_001510/B005"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000281","role":"Bringing or presenting something lets the arrival be heard as the presentation of an effective good.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001510","role":"Granting a gift supplies the beneficent substance of the arriving aid.","root":"ن ص ر","source_ref":"110:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"Worship and the worshipped one keep the gift relationally directed toward devotion rather than mere advantage.","root":"ء ل ه","source_ref":"110:1","source_word_indices":["4"]},{"branch_id":"B008","mapped_root_id":"root_001124","role":"Relief, insight, and disclosure supply the inward effect of the granted aid.","root":"ف ت ح","source_ref":"110:1","source_word_indices":["5"]}],"changed_reading":{"after":"Aid may arrive as a divine gift that relieves an inward closure and makes knowledge, guidance, or possibility accessible.","before":"Aid arrives as external power and conquest."},"confidence":"medium","focus_anchor":"The cluster جاء، نصر، الفتح permits brought good to culminate in relief, disclosure, or guidance.","mechanism":"Aid is not only force against an opponent; it can arrive as a presented gift whose effect is to remove an inward obstruction and disclose a way forward.","model_id":"baseline_gifted_inner_opening"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_gifted_inner_opening","source_type":"hft","support_id":"sup_9efe16c4be1033ee5e3e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا جَآءَ نَصْرُ ٱللَّهِ وَٱلْفَتْحُ","ayah_ref":"110:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000281/B003","root_001124/B005","root_001510/B004","root_001510/B007"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000281","role":"A hollow where water gathers supplies the receiving basin of the material mechanism.","root":"ج ي ء","source_ref":"110:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001510","role":"Rain that relieves and makes land grow supplies aid as life-giving water.","root":"ن ص ر","source_ref":"110:1","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001510","role":"Tributary channels arriving from afar supply the conveyance that gathers relief at the threshold.","root":"ن ص ر","source_ref":"110:1","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001124","role":"Water released from an outlet supplies the transition from gathered potential to distributed effect.","root":"ف ت ح","source_ref":"110:1","source_word_indices":["5"]}],"changed_reading":{"after":"Exploratorily, divine aid behaves like relieving water: it arrives through tributaries, gathers, and becomes effective when an outlet is opened.","before":"The ayah names an abstract or military victory."},"confidence":"exploratory","focus_anchor":"All three event roots carry a coherent water constellation: gathering, rain-relief or tributary flow, and release through an opening.","mechanism":"As a material analogy, distant channels bring relieving rain into a gathering place and an opened outlet releases it. The coherence across جاء، نصر، and فتح makes this more than a free-standing water theme, though it remains branch-distant from the surface construction.","model_id":"baseline_hydraulic_relief"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_hydraulic_relief","source_type":"hft","support_id":"sup_082364b131bcf399f88b","trust":"legacy_unbound"}]}
</lane_packet_json>
