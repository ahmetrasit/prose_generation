# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **103:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s103-regular-20260911/s103/103_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "103:1",
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
{"analysis_context":{"analysis_id":"s103-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"103:1","host_surah":103,"lane_context_refs":[],"ordered_context_refs":["103:0","103:2","103:3","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Zaman çekirdeği ile yalnız belirli biçimlerde görülen ikindi, ibadet ve deyim kullanımları birbirine karıştırılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B001","candidate_links":[{"candidate_id":"cand_57e4ad124fd696d5bc0e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"devir, vakit ve günün geç bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, devir, süre veya belirli bir vakit olarak zamandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkili biçim gece-gündüzü ya da sabah-akşamı, tekil biçim ise ikindiyi ve o vakitteki ibadeti gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kalıplar geç gelme, uygun geliş vaktinde gelmeme veya neredeyse hiç uyumama bildirir."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zaman çekirdeğini ve gün içindeki başlıca uzmanlaşmayı birlikte veren en kısa doğal karşılıktır.","boundary_detail":"Zaman çekirdeği ile yalnız belirli biçimlerde görülen ikindi, ibadet ve deyim kullanımları birbirine karıştırılmamalıdır.","branch_image_ar":"دهر ووقت متعاقب","concept_gloss":"devir, vakit ve günün geç bölümü","contextual_glosses":[{"applicability":"Gelişin yavaşlığını ya da beklenen zamanın kaçırıldığını bildiren kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıba bağlı gecikme ve uygunsuz zaman anlamını korur."},"facet_ids":["F003"],"text":"geç veya vaktinin dışında geldi","usage_role":"contextual"}],"definition":"Bir devir, vakit ya da günün geç bölümü; ikili kullanımda gece ile gündüzü veya sabah ile akşamı karşılar. Belirli kalıplarda geç gelmeyi, geliş vaktini kaçırmayı ya da neredeyse hiç uyumamayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, devir, süre veya belirli bir vakit olarak zamandır."},{"facet_id":"F002","role":"specialization","statement":"İkili biçim gece-gündüzü ya da sabah-akşamı, tekil biçim ise ikindiyi ve o vakitteki ibadeti gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Bazı kalıplar geç gelme, uygun geliş vaktinde gelmeme veya neredeyse hiç uyumama bildirir."}],"identity_rationale":"Kaynak ifadesi dalı devir, vakit ve günün geç bölümü çevresinde kurar; ikili zaman adlarını ve belirli deyimlerdeki gecikme ya da güçlük anlamlarını da açıkça kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"devir, çağ veya vakit"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gece ile gündüz veya sabah ile akşam"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ikindi ve günün akşama yakın bölümü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ikindi namazı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geç veya geliş vaktinin dışında geldi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"neredeyse hiç uyumadı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir zaman dilimi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir kez"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ömrüm ve yaşlılığım"}],"lexicalization_note":"Tanım, genel zaman anlamını biçim ve kalıba bağlı ikili zaman, ikindi ve deyim anlamlarından ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zaman sınırını en iyi açıklayan devir komşusu yayımlandı, diğerleri yalnız aynı senaryoyu paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalın odağı devir veya zaman parçasıdır; bu dal ise buna ek olarak gece-gündüz, sabah-akşam ve ikindi gibi gün içi ayrımları taşır.","focus_only":"Bu dal gün bölümlerini ve zamanla ilgili özel kalıpları da kapsar.","gloss":"devir ve vakit","neighbor_only":"Komşu dal özellikle uzun bir devir veya o devrin bir parçası olarak süreyi adlandırır.","neighbor_ref":"root_000665/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da sınırlı ya da geniş bir zaman kesitini gösterebilir."}],"source_phrase_ar":"العصر الدهر (ayn;sihah;tahdhib)؛ العصران الليل والنهار (ayn;sihah;tahdhib;maqayis)؛ العصران الغداة والعشي (sihah;tahdhib;maqayis)؛ العصر العشي (ayn;tahdhib)؛ صلاة العصر (sihah;tahdhib;maqayis)؛ العصار الحين (tahdhib)؛ جاءني فلان عصرا أي بطيئا (sihah)؛ نام وما نام لعصر (tahdhib)","source_summary":"Kaynaklar zaman çekirdeğinde ve günün bölümlerine ilişkin kullanımlarda birleşir; deyimsel kullanımlar bu çekirdeğe bağlı özel anlamlardır.","sources":["AY","SI","TA","MQ"],"what_is_ar":"يدخل فيه العصر بمعنى الدهر والحين واليوم والليلة، والعصران لليل والنهار أو للغداة والعشي، والعشي وصلاة العصر، وما جاء في البطء أو المجيء في غير حينه.","what_is_not_ar":"ليس هو عصر العنب والزيت، ولا الإعصار والغبار، ولا الملجأ والمنجاة."},"support_links":["sup_f3f25600e6d4c151d6c4"]},{"boundary":"Yağmur, sığınma ve malı geri alma anlamları bu mekanik sıkma dalına alınmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B002","candidate_links":[{"candidate_id":"cand_aeeec94145555ecea4c7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"sıkarak sıvısını çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek işlem, bir şeyi bastırıp sıkarak içindeki sıvıyı dışarı çıkarmaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemden çıkan sıvı, öz veya geride kalan posa sonuç adı olarak kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üzümün sıkıldığı yer ile içine konup sıkıldığı araç da işlem üzerinden adlandırılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşlemin basınç, sıkma ve sıvının çıkması aşamalarını eksiksiz biçimde özetler.","boundary_detail":"Yağmur, sığınma ve malı geri alma anlamları bu mekanik sıkma dalına alınmamalıdır.","branch_image_ar":"ضغط حتى يتحلب","concept_gloss":"sıkarak sıvısını çıkarma","contextual_glosses":[{"applicability":"İşlemin sonucunda akan sıvı veya özün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıkma işlemiyle elde edilen sıvı sonucu korur."},"facet_ids":["F002"],"text":"sıkılarak elde edilen özsu","usage_role":"contextual"}],"definition":"Bir şeyi basınç uygulayarak içindeki sıvı çıkıncaya kadar sıkmak; çıkan sıvı veya posa ile sıkmanın yapıldığı yer ve araç da bu işlemin sonuç ve araçlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek işlem, bir şeyi bastırıp sıkarak içindeki sıvıyı dışarı çıkarmaktır."},{"facet_id":"F002","role":"extension","statement":"İşlemden çıkan sıvı, öz veya geride kalan posa sonuç adı olarak kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Üzümün sıkıldığı yer ile içine konup sıkıldığı araç da işlem üzerinden adlandırılır."}],"identity_rationale":"Kaynak ifadesi bir şeyi sıvısı çıkıncaya kadar basınçla sıkmayı, çıkan sıvıyı ve bu işlemde kullanılan yer ya da aracı açıkça aynı dalda toplar.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"üzümü sıkarak suyunu çıkardı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"üzümü kendisi için sıktı veya suyunu hazırladı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"suyu sıkılmış şey veya sıkılarak çıkan sıvı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sıkılarak çıkan öz veya geride kalan posa"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"üzüm sıkılan yer veya düzenek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"içine üzüm konup sıkılan torba benzeri araç"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sıkılmış veya suyu çıkarılmış şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"üzüm ve zeytin sıkarlar"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sonsuza dek"}],"lexicalization_note":"Genel sıkma işlemi korunur; üzüm, yağ, araç, ürün ve kalıp anlamları kendi biçimlerine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çıkan özle karışma olasılığı en yüksek komşu yayımlandı, ürün ve tahıl adayları yalnız alan ortaklığı taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği basınçla çıkarma işlemidir; komşu dal işlem türünü şart koşmadan dökülen ya da çıkan sıvıya odaklanır.","focus_only":"Bu dal sıvıyı çıkarmak için uygulanan sıkma işlemini ve araçlarını içerir.","gloss":"sıkma ve çıkan öz","neighbor_only":"Komşu dal çeşitli maddelerden dökülen kırmızımsı sıvı veya özün kendisini adlandırır.","neighbor_ref":"root_000838/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir maddeden çıkan sıvı veya öz söz konusudur."}],"source_phrase_ar":"ضغط شيء حتى يتحلب (maqayis)؛ عصرت العنب واعتصرته (sihah)؛ عصرت العنب وعصرته إذا وليت عصره بنفسك (tahdhib)؛ يعصرون الأعناب والزيت (tahdhib)؛ العصارة ما سال عن العصر (sihah)؛ العصارة ما تحلب من شيء تعصره (tahdhib)؛ كل شيء عصر ماؤه فهو عصير (tahdhib)؛ المعصرة ما يعصر فيه العنب (sihah)؛ المعصار شيء كالمخلاة يجعل فيه العنب ويعصر (maqayis)؛ العصر مصدر عصرت والمعصور الشيء العصير (mufradat)","source_summary":"Kaynaklar basınçla sıvı çıkarma işlemini ortak çekirdek sayar; ürün, posa, yer ve araç adları bu işlemin çevresinde düzenlenir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه عصر العنب والزيت ونحوهما، والعصير، والعصارة، والمعصرة والمعصار، وما يستخرج بالضغط أو يتخذ من المعصور، وصورة قوله يعصرون على معنى يعصرون الأعناب والزيت.","what_is_not_ar":"ليس هو المطر والسحاب إلا من جهة اشتقاقه، ولا الملجأ، ولا أخذ المال من جهة الحق أو الرجوع."},"support_links":["sup_07abbe7d9d7ffa9abe85"]},{"boundary":"Dalın çekirdeği yağmur taşıyan bulut ve yağmurun gelişiyle sınırlıdır; rüzgar yorumu yalnız ilgili söz biriminde belirtilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B003","candidate_links":[{"candidate_id":"cand_36b4f292edc9ca347330","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"yağmur yüklü bulut ve yağmurun gelişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmur taşıyan ve yağışını boşaltmaya hazır bulut temel görüntüdür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğa yağmurun gelmesi veya insanların yağmura kavuşması olay olarak anlatılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem taşıyıcı bulutunu hem de topluluğa ulaşan yağışı birlikte karşılar.","boundary_detail":"Dalın çekirdeği yağmur taşıyan bulut ve yağmurun gelişiyle sınırlıdır; rüzgar yorumu yalnız ilgili söz biriminde belirtilir.","branch_image_ar":"سحاب يمطر ومطر يعصر","concept_gloss":"yağmur yüklü bulut ve yağmurun gelişi","contextual_glosses":[{"applicability":"Bir topluluğun yağmura kavuştuğunu bildiren fiil veya okuma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmurun topluluğa ulaşması olayını tam olarak korur."},"facet_ids":["F002"],"text":"onlara yağmur geldi","usage_role":"contextual"}],"definition":"Yağmurla dolu bulutun yağışı getirmesi veya bir topluluğun yağmura kavuşması; belirli bir okumada da insanlara yağmur gelmesini bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmur taşıyan ve yağışını boşaltmaya hazır bulut temel görüntüdür."},{"facet_id":"F002","role":"extension","statement":"Bir topluluğa yağmurun gelmesi veya insanların yağmura kavuşması olay olarak anlatılır."}],"identity_rationale":"Yetkili dal ifadesi yağmur yüklü bulutları ve bir topluluğa yağmur gelmesini destekler; rüzgar yorumu yalnız ayrı bir söz biriminde görüldüğünden dal çekirdeğine genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yağmur yüklü bulutlar veya yağmuru taşıyan rüzgarlar"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"topluluğa yağmur geldi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"orada yağmura kavuşurlar"}],"lexicalization_note":"Bulut ve yağmur çekirdeği korunur; topluluğa yağmur gelmesi ve özel okuma yalnız kendi kalıplarında verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yağmur dalı temel sınırı en iyi gösterdi, öteki adaylar yağışın yoğunluğu, belirtisi veya düşüş yeridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği düşen yağmur suyudur; bu dal ise yağmuru taşıyan bulutu ve bir topluluğun yağmura kavuşmasını öne çıkarır.","focus_only":"Bu dal yağmuru taşıyan bulutu ve yağmurun bir topluluğa gelişini birlikte içerir.","gloss":"yağmur yüklü bulut","neighbor_only":"Komşu dal gökten dökülen suyu, tek bir yağışı ve yağmurlu gün ya da vadiyi kapsar.","neighbor_ref":"root_001431/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı gökten gelen yağmur ve yağış olayıdır."}],"source_phrase_ar":"المعصرات السحائب تعتصر بالمطر (sihah)؛ المعصرات سحائب تجيء بمطر (maqayis)؛ السحابة المعصر التي تتحلب بالمطر (tahdhib)؛ أعصر القوم إذا أتاهم المطر (maqayis)؛ عصر القوم أي مطروا (sihah)؛ قرئت وفيه يعصرون أي يأتيهم المطر (maqayis)؛ تعصرون بضم التاء أي تمطرون (tahdhib)","source_summary":"Kaynaklar yağmur yüklü bulut ile yağmurun insanlara gelişi çevresinde birleşir; özel okuma da yağış anlamını sürdürür.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه المعصرات من السحاب أو الرياح إذا حملت المطر، وأعصر القوم أو عصروا إذا أتاهم المطر، وقراءة يعصرون على معنى يمطرون.","what_is_not_ar":"ليس هو نفس عصر العنب والزيت، ولا الإعصار الترابي المستدير الخالي من المطر."},"support_links":["sup_52ae367498bfb9de1eaa"]},{"boundary":"Döner toz sütunu çekirdektir; giysi ardından yayılan toz veya koku yalnız benzetmeli ve kalıba bağlı bir uzantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B004","candidate_links":[{"candidate_id":"cand_36b4f292edc9ca347330","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"sütun gibi yükselen döner toz rüzgarı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rüzgarın kaldırdığı, dönen ve sütun gibi yükselen toz temel anlamdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Giysi eteğinin ardından yükselen toz veya güzel kokunun yayılışı aynı görüntüyle anlatılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Rüzgarı, tozun dönmesini ve sütun biçiminde yükselmesini birlikte korur.","boundary_detail":"Döner toz sütunu çekirdektir; giysi ardından yayılan toz veya koku yalnız benzetmeli ve kalıba bağlı bir uzantıdır.","branch_image_ar":"إعصار وغبار مستدير","concept_gloss":"sütun gibi yükselen döner toz rüzgarı","contextual_glosses":[{"applicability":"Kokulu giysinin eteği ardından yükselen koku dalgasını anlatan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Giysi ardından yükselip yayılan güzel koku görüntüsünü korur."},"facet_ids":["F002"],"text":"eteğin ardından yayılan güzel koku","usage_role":"contextual"}],"definition":"Rüzgarın toprağı kaldırıp göğe doğru sütun gibi ve dönerek yükselttiği toz oluşumu. Giysi eteğinin ardından yükselen toz veya güzel kokunun yayılması da buna bağlı bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rüzgarın kaldırdığı, dönen ve sütun gibi yükselen toz temel anlamdır."},{"facet_id":"F002","role":"associated_use","statement":"Giysi eteğinin ardından yükselen toz veya güzel kokunun yayılışı aynı görüntüyle anlatılır."}],"identity_rationale":"Kaynak ifadesi sütun gibi yükselen döner tozu oluşturan rüzgarı çekirdek yapar ve giysi ardından yükselen toz ya da güzel koku yayılımını ilişkili kullanım olarak ayrıca verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tozu sütun gibi yükselten döner rüzgar veya döner toz"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"toz sütunları ve döner rüzgarlar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"eteğin ardından yükselen toz veya güzel koku"}],"lexicalization_note":"Rüzgar ve döner toz anlamı, giysi eteğine bağlı koku ya da toz yayılımından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; döner sütun sınırına en yakın toz bulutu adayı yayımlandı, diğerleri genel rüzgar, savrulma veya iz silinmesidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yükselen toz bulutu için daha geniştir; bu dalın belirleyici sınırı dönme ve sütun gibi dik yükselmedir.","focus_only":"Bu dal tozun dönmesini ve sütun biçiminde göğe yükselmesini şart koşar.","gloss":"döner toz sütunu","neighbor_only":"Komşu dal gökte yükselen bir toz bulutunu daha genel biçimde adlandırır.","neighbor_ref":"root_001258/B008","relation_type":"near_synonym","shared_zone":"Her iki dal rüzgarla yükselen yoğun bir toz oluşumunu anlatır."}],"source_phrase_ar":"الإعصار ريح تهب تثير الغبار فيرتفع إلى السماء كأنه عمود (sihah)؛ الإعصار الغبار الذي يسطع مستديرا والجمع الأعاصير (maqayis)؛ الإعصار الريح التي تهب من الأرض كالعمود الساطع نحو السماء (tahdhib)؛ إعصار وعصار وهو أن تهيج الريح التراب فترفعه (tahdhib)؛ مرت امرأة متطيبة لذيلها عصر (sihah)؛ لذيلها عصرة تكون العصرة من فوح الطيب وهيجه (tahdhib)","source_summary":"Kaynaklar döner ve sütun biçiminde yükselen toz ile onu kaldıran rüzgarı ortak çekirdek sayar; koku yayılımı bağlı bir uzantıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه الإعصار والأعاصير، والريح التي تثير الغبار فيرتفع كعمود، والغبار أو فوح الطيب الذي يثور وراء الذيل.","what_is_not_ar":"ليس هو السحاب الماطر إلا إذا ذكرت المجاورة، ولا الدهر، ولا عصر العنب."},"support_links":["sup_52ae367498bfb9de1eaa"]},{"boundary":"Sığınma ve kurtuluş çekirdeği, mekanik sıkma veya malı alıkoyma anlamlarıyla birleştirilmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B005","candidate_links":[{"candidate_id":"cand_8ac68e84bce74f717e19","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"tutunarak sığınma ve kurtuluş arama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeye tutunma ve onu güvenlik dayanağı edinme anlamın çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sığınılan kişi veya yer, sığınak ve kurtuluş yolu olarak adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki kişi arasındaki sevgi veya akrabalık bağı aynı tutunma ilişkisiyle anlatılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tutunma ilişkisini, sığınma hareketini ve kurtuluş amacını birlikte verir.","boundary_detail":"Sığınma ve kurtuluş çekirdeği, mekanik sıkma veya malı alıkoyma anlamlarıyla birleştirilmemelidir.","branch_image_ar":"ملجأ ومنجاة واعتصام","concept_gloss":"tutunarak sığınma ve kurtuluş arama","contextual_glosses":[{"applicability":"İki kişi arasında yakınlık bulunmadığını bildiren olumsuz kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sevgi ve akrabalık bağının yokluğunu açıkça korur."},"facet_ids":["F003"],"text":"aralarında sevgi veya akrabalık bağı yok","usage_role":"contextual"}],"definition":"Bir şeye tutunarak sığınmak ve kurtuluş aramak; sığınılan kişi veya yer de sığınak sayılır. İki kişi arasındaki sevgi ya da akrabalık bağı bu tutunma görüntüsünün ilişkili kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeye tutunma ve onu güvenlik dayanağı edinme anlamın çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Sığınılan kişi veya yer, sığınak ve kurtuluş yolu olarak adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"İki kişi arasındaki sevgi veya akrabalık bağı aynı tutunma ilişkisiyle anlatılır."}],"identity_rationale":"Kaynak ifadesi bir şeye tutunma ve onunla bağ kurma çekirdeğinden sığınak, kurtuluş, bir kişiye ya da yere sığınma ve iki kişi arasındaki yakınlık anlamlarını açıkça türetir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sığınak veya kurtuluş yolu"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"sığınak ve kurtuluş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"o kişiye veya o yere sığındı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"aralarında sevgi veya akrabalık bağı yok"}],"lexicalization_note":"Sığınak adı ile bir kişiye ya da yere sığınma ve yakınlık bildiren kalıplar ayrı fakat ortak tutunma çekirdeğine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sığınma ve kurtuluş dalı yayımlandı, diğerleri korunak türü, savunucu veya destekleyici kişidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal güvenli yere yönelmeyi anlatır; bu dal sığınılan dayanağa tutunmayı ve bundan doğan bağ ilişkisini de içerir.","focus_only":"Bu dal tutunma çekirdeğini ve kişiler arasındaki yakınlık bağını da kapsar.","gloss":"sığınma ve kurtulma","neighbor_only":"Komşu dal güvenli yere yönelme, korunma yerine gitme ve kurtulma hareketini öne çıkarır.","neighbor_ref":"root_001616/B002","relation_type":"near_synonym","shared_zone":"Her iki dal güvenlik arama, sığınak bulma ve tehlikeden kurtulma alanındadır."}],"source_phrase_ar":"تعلق بشيء وامتساك به (maqayis)؛ العصر الملجأ (sihah;maqayis)؛ العصر المنجاة والعصرة والمعتصر والمعصر (tahdhib)؛ اعتصرت بفلان وتعصرت أي التجأت إليه (sihah)؛ اعتصر بالمكان إذا التجأ إليه (maqayis)؛ الاعتصار الالتجاء (tahdhib)؛ عصرة المنجود (sihah;tahdhib;maqayis)؛ ما بينهما عصر ولا يصر أي ما بينهما مودة ولا قرابة (tahdhib)","source_summary":"Kaynaklar tutunma, sığınma ve kurtuluş anlamlarında birleşir; kişiler arasındaki sevgi veya akrabalık bağı bu çekirdeğin ilişkili uzantısıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه العصر والعصرة بمعنى الملجأ والمنجاة، والاعتصار أو التعصر بمعنى الالتجاء، وما بين الشيئين من مودة أو قرابة على جهة التعلق والامتساك.","what_is_not_ar":"ليس هو استخراج العصارة، ولا حبس المال ومنعه، ولا الدهر."},"support_links":["sup_c815c5c9175925de329b"]},{"boundary":"Başlangıçta verme anlamı bu dala ait değildir; burada malın tutulması, alınması veya geri çevrilmesi söz konusudur.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B006","candidate_links":[{"candidate_id":"cand_8ac68e84bce74f717e19","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"alıkoyma, malı alma veya geri alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi engelleme, tutma veya hak sahibinden alıkoyma çekirdek anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin malını elinden alma, geri alma veya önceki bağıştan dönme özel uygulamalardır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eli sıkı ve iyiliği az kişi, elindekini tutması üzerinden nitelenir."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel engellemeyi ve mala ilişkin başlıca işlem türlerini birlikte karşılar.","boundary_detail":"Başlangıçta verme anlamı bu dala ait değildir; burada malın tutulması, alınması veya geri çevrilmesi söz konusudur.","branch_image_ar":"حبس ومنع واسترجاع","concept_gloss":"alıkoyma, malı alma veya geri alma","contextual_glosses":[{"applicability":"Daha önce verilmiş bir şeyden dönüp onu yeniden alma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce verme ve ardından geri alma sırasını korur."},"facet_ids":["F002"],"text":"verdiği bağışı geri aldı","usage_role":"contextual"}],"definition":"Bir şeyi engellemek veya birinden alıkoymak; özellikle birinin malını elinden almak, geri almak ya da verilmiş bir bağıştan dönmek. Eli sıkı ve iyiliği az kişi de bu tutma davranışıyla nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi engelleme, tutma veya hak sahibinden alıkoyma çekirdek anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Birinin malını elinden alma, geri alma veya önceki bağıştan dönme özel uygulamalardır."},{"facet_id":"F003","role":"extension","statement":"Eli sıkı ve iyiliği az kişi, elindekini tutması üzerinden nitelenir."}],"identity_rationale":"Kaynak ifadesi engelleme ve alıkoyma çekirdeğini, malı birinin elinden çıkarma, geri alma veya verilmiş bağıştan dönme işlemlerini ve eli sıkı kişiyi aynı dalda açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"alıkoyma veya engelleme"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"malını elinden çıkardı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"baba çocuğunun malını alıkoydu veya geri aldı"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"verdiği bağıştan döndü ve onu geri aldı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"eli sıkı, iyiliği az kimse"}],"lexicalization_note":"Genel engelleme çekirdeği ile malı çıkarma, geri alma ve eli sıkılık bildiren biçimler ayrı kapsamlarla verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel alıkoyma sınırını en iyi gösteren komşu yayımlandı, ötekiler hak, pay veya karşılık alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kapatma ve yoksun bırakmayı öne çıkarır; bu dal özellikle malın elden alınması ve önceki işlemin geri çevrilmesini içerir.","focus_only":"Bu dal malı elden çıkarma, geri alma ve verilmiş bağıştan dönmeyi de kapsar.","gloss":"alıkoyma ve engelleme","neighbor_only":"Komşu dal kişi ya da hayvanı kapatma ve onu yem, otlak veya iyilikten yoksun bırakma bağlamlarına uzanır.","neighbor_ref":"root_000231/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir varlığı veya yararı başkasından esirgeme ve tutma anlamını paylaşır."}],"source_phrase_ar":"العصر الحبس (tahdhib)؛ تعصر أي تعسر (tahdhib)؛ ما عصرك أي ما منعك (tahdhib)؛ اعتصرت ماله إذا استخرجته من يده (sihah)؛ يعتصر الوالد على ولده في ماله أي يمنعه إياه ويحبسه عنه (sihah)؛ يعتصر يسترجع (tahdhib)؛ أعطيت فلانا عطية فاعتصرتها أي رجعت فيها (tahdhib)؛ المعتصر الذي يأخذ من الشيء يصيب منه (maqayis)؛ فلان عاصر إذا كان ممسكا (tahdhib)","source_summary":"Kaynaklar engelleme ve alıkoyma çekirdeğini malı çıkarma, geri alma ve bağıştan dönme işlemleriyle ilişkilendirir; eli sıkılık bunun kişiye aktarımıdır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه العصر بمعنى الحبس أو المنع، واعتصر مال غيره إذا استخرجه أو حبسه، واعتصر الوالد مال ولده أو رجع في عطية، والعاصر الممسك قليل الخير.","what_is_not_ar":"ليس هو العطاء ابتداء، ولا عصر العنب، ولا الملجأ."},"support_links":["sup_c815c5c9175925de329b"]},{"boundary":"Bu dal verme ve elde edilen ürünü kapsar; verileni geri alma ya da alıkoyma karşıt yöndeki başka bir daldır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B007","candidate_links":[{"candidate_id":"cand_aeeec94145555ecea4c7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"bağış, iyilik veya elde edilen ürün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birine ulaşan bağış, iyilik veya yarar dalın verme yönünü oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyden alınan pay, ürün, tarımsal gelir veya başka kazanç elde etme yönünü oluşturur."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen yarar ile bir kaynaktan çıkan ürün veya geliri birlikte temsil eder.","boundary_detail":"Bu dal verme ve elde edilen ürünü kapsar; verileni geri alma ya da alıkoyma karşıt yöndeki başka bir daldır.","branch_image_ar":"عطاء وغلة مستخرجة","concept_gloss":"bağış, iyilik veya elde edilen ürün","contextual_glosses":[{"applicability":"Arazinin işletilmesiyle ürün veya gelir kazanılmasını bildiren özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi kaynağından ürün ve gelir elde etmeyi korur."},"facet_ids":["F002"],"text":"topraklarından ürün ve gelir elde ederler","usage_role":"contextual"}],"definition":"Birine verilen bağış veya iyilik ile bir kaynaktan elde edilen ürün, pay ya da gelir. Bir şeyden yarar elde eden kişi de bu elde etme ilişkisiyle adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birine ulaşan bağış, iyilik veya yarar dalın verme yönünü oluşturur."},{"facet_id":"F002","role":"extension","statement":"Bir şeyden alınan pay, ürün, tarımsal gelir veya başka kazanç elde etme yönünü oluşturur."}],"identity_rationale":"Kaynak ifadesi bağış ve iyilik ile bir şeyden elde edilen pay, ürün veya geliri birlikte verir; elde etme görüntüsü iki kullanım alanını bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"bağış veya armağan"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"bize bağışta bulunur veya iyilik eder"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"iyiliği ve bağışı bol"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"ürün veya gelir"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"topraklarından ürün ve gelir elde ederler"}],"lexicalization_note":"Bağış, iyilik ve ürün anlamları biçim veya kalıba göre ayrılır; arazi geliri bütün köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iyilik ile ürün yönlerini birlikte sınayan komşu yayımlandı, ötekiler yalnız bağış miktarı, meyve veya hasat işlemidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel iyilik ve yarar ilişkisidir; bu dal ayrıca kaynaktan elde edilen ürün ya da gelir görüntüsünü yapısal olarak taşır.","focus_only":"Bu dal iyiliğin yanı sıra bir kaynaktan çıkarılan ürün, pay ve arazi gelirini içerir.","gloss":"iyilik ve ürün","neighbor_only":"Komşu dal yarar, geçim ve yakınlarla bağı sürdürme gibi daha geniş iyilik ilişkilerini kapsar.","neighbor_ref":"root_000152/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bağış, yarar ve başkasına ulaşan iyilik alanında kesişir."}],"source_phrase_ar":"العصر العطية (tahdhib)؛ يعصر فينا كالذي تعصر أي تعطي (maqayis;tahdhib)؛ العرب تجعل العصارة والمعتصر مثلا للخير والعطاء (maqayis)؛ المعتصر الذي يصيب من الشيء ويأخذ منه (sihah)؛ العصارة الغلة (tahdhib)؛ يعصرون قال يستغلون بأرضيهم (maqayis)؛ وفيه تعصرون أي تستغلون (tahdhib)","source_summary":"Kaynaklar bağış ve iyiliği, bir şeyden pay alma ve araziden ürün ya da gelir elde etme anlamlarıyla birlikte sunar.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه العصر بمعنى العطية، ويعصر فينا بمعنى يعطي، والعصارة أو المعتصر مثلا للخير والعطاء، والغلة والاستغلال.","what_is_not_ar":"ليس هو الرجوع في العطية أو حبسها، ولا الملجأ، ولا المطر إلا إذا فسر يعصرون بالمطر."},"support_links":["sup_07abbe7d9d7ffa9abe85"]},{"boundary":"Az içme tek başına yeterli değildir; yiyeceğin boğaza takılması ve onu geçirme amacı kurucu koşullardır.","branch_kind":"non_bare","branch_ref":"root_001019/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"boğaza takılan yiyeceği küçük yudumlarla geçirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yiyeceğin boğaza takılması üzerine onu geçirmek amacıyla su küçük yudumlarla içilir."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koşulu, küçük yudumlarla içme biçimini ve yiyeceği geçirme amacını eksiksiz verir.","boundary_detail":"Az içme tek başına yeterli değildir; yiyeceğin boğaza takılması ve onu geçirme amacı kurucu koşullardır.","branch_image_ar":"شرب قليل لإساغة الغصة","concept_gloss":"boğaza takılan yiyeceği küçük yudumlarla geçirme","contextual_glosses":[{"applicability":"Boğaza takılan lokmanın küçük su yudumlarıyla geçirildiği gerçek olay bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçme biçimini ve lokmayı geçirme amacını korur."},"facet_ids":["F001"],"text":"yiyeceği geçirmek için suyu azar azar içti","usage_role":"contextual"}],"definition":"Yiyecek boğaza takıldığında onu geçirmek için suyu azar azar içmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yiyeceğin boğaza takılması üzerine onu geçirmek amacıyla su küçük yudumlarla içilir."}],"identity_rationale":"Kaynak ifadesi yiyecek boğaza takıldığında onu geçirmek amacıyla suyu azar azar içme durumunu bütün koşul, işlem ve amaçlarıyla açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"boğaza takılan yiyeceği geçirmek için suyu azar azar içti"}],"lexicalization_note":"Anlam yalnız yiyecek boğaza takıldığında suyu azar azar içme biçimine aittir ve genel içme anlamına genişletilemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; küçük yudumlarla içme komşusu yayımlandı, diğerleri genel yutma, az su, boğaz rahatsızlığı veya ıslaklıktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yudumlama ve yutmadır; bu dal yalnız yiyecek takılması üzerine onu geçirmek için yapılan amaçlı içmedir.","focus_only":"Bu dal boğaza takılmış yiyeceği geçirme amacını ve suyu azar azar içmeyi şart koşar.","gloss":"küçük yudumlarla geçirme","neighbor_only":"Komşu dal genel yutmayı, tek veya art arda yudumları ve istemeden içmeyi de kapsar.","neighbor_ref":"root_000237/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal suyun küçük miktarlar halinde boğazdan geçirilmesini içerebilir."}],"source_phrase_ar":"الاعتصار أن يغص الإنسان بالطعام فيعتصر بالماء وهو أن يشربه قليلا قليلا ليسيغه (sihah)؛ لو بغير الماء حلقي شرق كنت كالغصان بالماء اعتصاري (tahdhib)","source_summary":"Kaynaklar boğaza takılan yiyecek, azar azar su içme işlemi ve yiyeceği geçirme amacı üzerinde birleşir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الاعتصار إذا غص الإنسان بالطعام فشرب الماء قليلا قليلا ليسيغه.","what_is_not_ar":"ليس هو الالتجاء العام، ولا عصر الشيء لاستخراج مائه."},"support_links":[]},{"boundary":"Tanım tek bir kesin ana indirgenmez; aybaşına yaklaşma, ilk aybaşı ve belirgin gençlik gelişimi kaynaklar arasındaki eşik aralığıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B009","candidate_links":[{"candidate_id":"cand_92acfc78e23f28655524","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"genç kızın ergenlik eşiğine ulaşması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Genç kızın çocukluktan ergenlik dönemine geçiş eşiğine varması ortak çekirdektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşik, aybaşına yaklaşma, ilk aybaşı veya gençlik gelişiminin belirgin artışı olarak farklı biçimlerde belirlenir."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların farklı ölçütlerini tek bir kesin ana zorlamadan ortak geçişi karşılar.","boundary_detail":"Tanım tek bir kesin ana indirgenmez; aybaşına yaklaşma, ilk aybaşı ve belirgin gençlik gelişimi kaynaklar arasındaki eşik aralığıdır.","branch_image_ar":"بلوغ الجارية عصر شبابها","concept_gloss":"genç kızın ergenlik eşiğine ulaşması","contextual_glosses":[{"applicability":"Kaynakların yaklaşma ve gerçekleşme ölçütlerini birlikte görünür kılmak gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaklaşma ile ilk gerçekleşme arasındaki kaynak farkını korur."},"facet_ids":["F001","F002"],"text":"ergenliğe yaklaştı veya ilk aybaşını gördü","usage_role":"explanatory"}],"definition":"Genç kızın ergenlik eşiğine varması: gençlik gelişiminin belirginleşmesi, aybaşına yaklaşması veya ilk kez aybaşı olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Genç kızın çocukluktan ergenlik dönemine geçiş eşiğine varması ortak çekirdektir."},{"facet_id":"F002","role":"source_variant","statement":"Eşik, aybaşına yaklaşma, ilk aybaşı veya gençlik gelişiminin belirgin artışı olarak farklı biçimlerde belirlenir."}],"identity_rationale":"Kaynak ifadesi genç kızın ergenlik eşiğine ulaşmasını ortaklaştırır, ancak bazı anlatımlar ilk aybaşını, bazıları ona yaklaşmayı veya gençlik gelişiminin belirginleşmesini ölçüt alır.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"ergenliğe ulaşan veya aybaşına yaklaşan genç kız"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"genç kız ergenliğe ulaştı veya aybaşına yaklaştı"}],"lexicalization_note":"Ergenlik eşiği biçime bağlıdır; aybaşına yaklaşma ile gerçekleşmiş ilk aybaşı arasındaki kaynak farkı korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çocukluktan çıkış sınırına en yakın komşu yayımlandı, diğerleri genel gençlik, beden belirtisi, hizmet yaşı veya aybaşı olayıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal toplumsal yaş ve giyim eşiğine odaklanır; bu dalın belirleyici sınırı bedensel gelişim ve aybaşı eşiğidir.","focus_only":"Bu dal ergenlik eşiğini özellikle aybaşı ve gençlik gelişimi belirtileriyle sınırlar.","gloss":"ergenliğe ulaşan genç kız","neighbor_only":"Komşu dal çocukluktan çıkmış, örtünme yaşına gelmiş fakat evlenmemiş genç kız durumunu öne çıkarır.","neighbor_ref":"root_000979/B005","relation_type":"near_synonym","shared_zone":"Her iki dal genç kızın çocukluktan çıkıp yeni bir yaş evresine girmesini anlatır."}],"source_phrase_ar":"الجارية أول ما أدركت وحاضت يقال قد أعصرت (sihah)؛ التي قاربت الحيض (sihah)؛ بلغت عصر شبابها وإدراكها (tahdhib)؛ إذا رأت في نفسها زيادة الشباب فقد أعصرت وهي معصر (maqayis)؛ إذا بلغت الجارية وقربت من حيضها فهي معصر (maqayis)؛ المعصر ساعة تطمث أي تحيض لأنها تحبس في البيت يجعل لها عصرا (tahdhib)","source_summary":"Kaynaklar genç kızın ergenlik eşiğinde birleşir; eşiğin yaklaşan aybaşı mı, ilk aybaşı mı yoksa belirgin gençlik gelişimi mi olduğu farklı anlatılır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه المعصر من الجواري إذا أدركت أو قاربت الحيض أو بلغت زيادة الشباب وعصر الشباب.","what_is_not_ar":"ليس هو السحاب المعصر، ولا معصرة العنب، ولا الحبس العام إلا في تفسير خاص."},"support_links":["sup_7f0b3a089c65fe8ff40a"]},{"boundary":"Anlam yalnız ekinin başak kılıflarına girme evresidir; genel kap, kılıf veya sıkma anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_001019/B010","candidate_links":[{"candidate_id":"cand_92acfc78e23f28655524","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"ekinin başak kılıflarına girip korunması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ekin, başağın kılıfları belirginleşince onların içine girip korunur."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkiyi, gelişim aşamasını, kılıfa girmeyi ve korunma sonucunu birlikte verir.","boundary_detail":"Anlam yalnız ekinin başak kılıflarına girme evresidir; genel kap, kılıf veya sıkma anlamına genişletilemez.","branch_image_ar":"زرع يتحرز في أكمامه","concept_gloss":"ekinin başak kılıflarına girip korunması","contextual_glosses":[{"applicability":"Ekinin kılıflarının yeni belirginleştiği gelişim aşamasını anlatan cümlede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ekinin gelişim aşamasını ve kılıfa girişini korur."},"facet_ids":["F001"],"text":"ekin başak kılıflarına girdi","usage_role":"contextual"}],"definition":"Ekinin başak kılıfları belirginleşerek onların içine girmesi ve bu örtüler içinde korunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ekin, başağın kılıfları belirginleşince onların içine girip korunur."}],"identity_rationale":"Kaynak ifadesi ekinin kılıfları belirginleşip başağı çevrelediği gelişim evresini ve bitkinin bu kılıflarda korunmasını açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"ekin başak kılıflarına girdi ve örtüleri içinde korundu"}],"lexicalization_note":"Tanım yalnız ekinle kurulan ve başak kılıflarının belirmesini anlatan kalıba bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başak oluşum evresini en iyi karşılaştıran komşu yayımlandı, diğerleri genel kap, bitki örtüsü veya hurma gelişimidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal başağın oluşup uzamasına odaklanır; bu dal ise başak kılıflarının belirginleşmesi ve koruyucu örtü işlevini öne çıkarır.","focus_only":"Bu dal kılıfların belirmesini ve ekinin onların içinde korunmasını şart koşar.","gloss":"başak kılıfına girme","neighbor_only":"Komşu dal ekinin başak vermesini ve başağın uzayıp ortaya çıkmasını daha genel biçimde anlatır.","neighbor_ref":"root_000672/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal ekinin başak oluşturduğu gelişim evresine ilişkindir."}],"source_phrase_ar":"عصر الزرع صار في أكمامه (tahdhib)؛ إذا تبينت أكمام السنبل قيل قد عصر الزرع (tahdhib)؛ مأخوذ من العصر وهو الحرز أي تحرز في غلفه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Ekinin başak kılıfları belirginleşip örtüleri içinde korunduğu gelişim evresi bu kaynakta tek başına tanıklanır."}],"source_summary":"Kanıt, ekinin başak kılıflarına girdiği ve bu örtüler içinde korunduğu gelişim evresini tek başına bildirir.","sources":["TA"],"what_is_ar":"يدخل فيه عصر الزرع إذا صار في أكمامه وتحرز في غلفه وأوعيته.","what_is_not_ar":"ليس هو عصر الماء من الشيء، ولا المطر، ولا الجارية المعصر."},"support_links":["sup_7f0b3a089c65fe8ff40a"]},{"boundary":"Soy kökü çekirdektir; sorulduğunda cömertlik bildiren kalıp ayrı tutulur ve sığınak anlamı yalnız köken açıklamasındaki benzetmeli bağlantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001019/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"soy kökü ve kökene bağlı soyluluk","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin soyunun döndüğü kök ve köken temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kökenin seçkinliği, soylu bir soya sahip olma niteliğiyle ifade edilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir kalıp, soy yerine kişinin kendisinden istenen şeye cömertçe karşılık vermesini anlatır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın baskın köken ve soy çekirdeğini doğal biçimde karşılar; cömertlik kalıbı ayrıca verilir.","boundary_detail":"Soy kökü çekirdektir; sorulduğunda cömertlik bildiren kalıp ayrı tutulur ve sığınak anlamı yalnız köken açıklamasındaki benzetmeli bağlantıdır.","branch_image_ar":"أصل وحسب ونسب","concept_gloss":"soy kökü ve kökene bağlı soyluluk","contextual_glosses":[{"applicability":"Kişinin soyunu değil, bir istek karşısındaki cömertliğini bildiren özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İstek üzerine cömertçe karşılık verme niteliğini korur."},"facet_ids":["F003"],"text":"kendisine başvurulduğunda cömert davranan","usage_role":"contextual"}],"definition":"Bir kişinin soyunun dayandığı kök, köken ve bu kökene bağlı soyluluk. Ayrı bir kalıpta ise kişinin kendisinden bir şey istendiğinde cömert davranması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin soyunun döndüğü kök ve köken temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Kökenin seçkinliği, soylu bir soya sahip olma niteliğiyle ifade edilir."},{"facet_id":"F003","role":"source_variant","statement":"Belirli bir kalıp, soy yerine kişinin kendisinden istenen şeye cömertçe karşılık vermesini anlatır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü kişinin soy kökü ve kökenini destekler, ancak sorulduğunda cömert olmayı bildiren ayrı bir kalıp soy anlamına indirgenemez ve bağımlı bir kaynak çeşidi olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"soy kökü ve köken"},{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"soyu seçkin"},{"lexical_unit_id":"lu_045","rendering_kind":"ordinary","target_gloss":"kendisine başvurulduğunda cömert"}],"lexicalization_note":"Köken bildiren biçim ile soyluluk ve sorulduğunda cömertlik bildiren kalıplar birbirinden ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; köken ve soy sınırına en yakın komşu yayımlandı, ötekiler aşiret, araştırılmış köken, soy eğilimi veya toplumsal değer uzantılarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal köken ile toplumsal konumu birleştirir; bu dal soyun döndüğü kökü öne çıkarır ve ayrıca cömertlik bildiren özel bir kalıp taşır.","focus_only":"Bu dal kökenin yanında soyluluğu ve ayrı bir kalıpta istek karşısındaki cömertliği de taşır.","gloss":"soy kökü ve köken","neighbor_only":"Komşu dal kişinin yetiştiği kökü, soy başlangıcını ve toplumsal konumunu birlikte adlandırır.","neighbor_ref":"root_000589/B008","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin geldiği soy kökünü ve bu köke bağlı değeri anlatır."}],"source_phrase_ar":"العنصر والعنصر الأصل والحسب (sihah)؛ كريم المعصر أي كريم عند المسألة (sihah)؛ فلان كريم العصير أي كريم النسب (tahdhib)؛ العنصر أصل الحسب ومما زيدت فيه النون وهو في الأصل العصر وهو الملجأ (maqayis)؛ كلا يئل في الانتساب إلى أصله الذي هو منه (maqayis)","source_summary":"Kaynaklar köken ve soy anlamını destekler; bunun yanında tek bir kalıp sorulduğunda cömert davranma yönüyle ayrı bir açıklama taşır.","sources":["SI","TA","MQ"],"what_is_ar":"يدخل فيه العنصر بمعنى أصل الحسب مع زيادة النون، وكريم المعصر أو العصير في النسب، وما يرجع فيه المنتسب إلى أصله.","what_is_not_ar":"ليس هو الملجأ الحسي إلا من جهة تعليل رجوع النسب إلى أصله، ولا الدنية في الموالي."},"support_links":[]},{"boundary":"Genel değersizlik değil, bağlılık ilişkisi içindeki göreli alt konum bu dalın sınırıdır.","branch_kind":"bare","branch_ref":"root_001019/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"bağlılar arasındaki alt konumlu kesim","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlı kimseler arasında başkalarından daha aşağı sayılan kesim ve göreli mevki anlatılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlılık ilişkisini ve başkalarına göre daha düşük konumu birlikte belirtir.","boundary_detail":"Genel değersizlik değil, bağlılık ilişkisi içindeki göreli alt konum bu dalın sınırıdır.","branch_image_ar":"دنية في الموالاة","concept_gloss":"bağlılar arasındaki alt konumlu kesim","contextual_glosses":[{"applicability":"Bir grubun kendisine bağlı kimseler arasında daha düşük saydığı kesimi gösterirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşana bağlı olmayı ve alt konumu birlikte korur."},"facet_ids":["F001"],"text":"bizim alt konumdaki bağlılarımız","usage_role":"contextual"}],"definition":"Bir bağlılık ilişkisi içindeki kimselerin, aynı ilişki içindeki başkalarına göre daha aşağı konumda olan kesimi veya bu göreli düşük mevki.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlı kimseler arasında başkalarından daha aşağı sayılan kesim ve göreli mevki anlatılır."}],"identity_rationale":"Kaynak ifadesi bağlı kimseler arasında ötekilere göre daha aşağı konumda sayılan kesimi ve bu düşük mevkiyi açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_046","rendering_kind":"ordinary","target_gloss":"bağlılar arasındaki alt konumlu kesim"}],"lexicalization_note":"Tanım çıplak biçimin bağlılar arasındaki düşük mevki anlamıyla sınırlıdır ve komşu genel aşağılık anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel mevki düşüklüğü en yakın karşılaştırma olarak yayımlandı, diğerleri uzaklık, yardımcılık, değersizlik veya güçsüzlük alanındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel düşüklük ve boyun eğmeyi içerir; bu dal yalnız bağlılar arasındaki göreli alt sınıfı adlandırır.","focus_only":"Bu dal düşük konumu özellikle bağlılık ilişkisi içindeki bir kesime sınırlar.","gloss":"alt konum ve düşüklük","neighbor_only":"Komşu dal genel mevki düşüklüğünü ve kişinin kendini alçaltmasını da kapsar.","neighbor_ref":"root_001657/B005","relation_type":"near_synonym","shared_zone":"Her iki dal toplumsal ya da kişisel mevkinin düşük olmasını anlatır."}],"source_phrase_ar":"العصرة أيضا الدنية (sihah)؛ هؤلاء موالينا عصرة أي دنية دون من سواهم (sihah)؛ هؤلاء موالينا عصرة أي دنية دون من سواهم (tahdhib)","source_summary":"Kaynaklar anlamı bağlılık ilişkisi içindeki göreli düşük mevki ve bu mevkideki kesim olarak ortak biçimde verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العصرة بالضم أو موالينا عصرة بمعنى الدنية دون غيرهم.","what_is_not_ar":"ليس هو كريم النسب، ولا الملجأ، ولا العصر بمعنى الدهر."},"support_links":[]},{"boundary":"Kanıt yalnız ağaç olduğunu gösterir; tür, görünüş, meyve veya kullanım özelliği eklenemez.","branch_kind":"bare","branch_ref":"root_001019/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"bir ağaç türü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, ek bir tür veya görünüş bilgisi olmadan bir ağacı adlandırır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtın izin verdiği tek sınıflandırmayı verir ve bilinmeyen tür özelliği eklemez.","boundary_detail":"Kanıt yalnız ağaç olduğunu gösterir; tür, görünüş, meyve veya kullanım özelliği eklenemez.","branch_image_ar":"العصرة شجرة","concept_gloss":"bir ağaç türü","definition":"Kaynakta türü ve özellikleri belirtilmeden adı verilen bir ağaç.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, ek bir tür veya görünüş bilgisi olmadan bir ağacı adlandırır."}],"identity_rationale":"Kaynak ifadesi sözcüğü herhangi bir tür, görünüş veya kullanım ayrıntısı vermeden doğrudan bir ağaç adı olarak tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_047","rendering_kind":"ordinary","target_gloss":"bir ağaç türü"}],"lexicalization_note":"Tanım çıplak biçimin yalnız bir ağaç adı olma anlamını taşır ve başka bitki dallarından özellik almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kanıt ağacın kimliğini ve özelliklerini vermediği için başka özel bitki adlarıyla güvenilir bir sınır karşılaştırması kurulamadı.","source_phrase_ar":"العصرة شجرة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcüğün bir ağaç adı olduğu bilgisi bu kaynakta tek başına ve başka nitelik verilmeden tanıklanır."}],"source_summary":"Kanıt yalnız sözcüğün bir ağaç adı olduğunu bildirir; ağacın türü veya özellikleri hakkında ek bilgi vermez.","sources":["TA"],"what_is_ar":"يدخل فيه العصرة اسما لشجرة.","what_is_not_ar":"ليس هو العصفر، ولا عصر النبات في أكمامه، ولا عصر الماء من الشيء."},"support_links":[]},{"boundary":"Kuruyan dil sonuç durumudur; genel susama, boğaz ağrısı veya sıkılmış nesne anlamı değildir.","branch_kind":"bare","branch_ref":"root_001019/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"susuzluktan kurumuş dil","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Susuzluk dili kurutur; adlandırılan şey susuzluk değil, kurumuş dilin kendisidir."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Etkilenen organı, nedeni ve ortaya çıkan kuruluk durumunu birlikte karşılar.","boundary_detail":"Kuruyan dil sonuç durumudur; genel susama, boğaz ağrısı veya sıkılmış nesne anlamı değildir.","branch_image_ar":"لسان معصور من العطش","concept_gloss":"susuzluktan kurumuş dil","definition":"Susuzluk yüzünden kurumuş ve nemini yitirmiş dil.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Susuzluk dili kurutur; adlandırılan şey susuzluk değil, kurumuş dilin kendisidir."}],"identity_rationale":"Kaynak ifadesi genel susuzluk durumunu değil, susuzluğun doğrudan sonucu olarak kuruyup nemini yitirmiş dili adlandırır.","lexical_glosses":[{"lexical_unit_id":"lu_048","rendering_kind":"ordinary","target_gloss":"susuzluktan kurumuş dil"}],"lexicalization_note":"Tanım çıplak biçimin susuzluktan kuruyan dil anlamıyla sınırlıdır ve genel susuzluk alanına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel susuzluk dalı neden-sonuç sınırını en iyi gösterdi, diğerleri susuzluk türü, ısı, öksürük veya boğaz ağrısıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal durumun kendisidir; bu dal ise o durumun belirli sonucu olarak kuruyan dili adlandırır.","focus_only":"Bu dal susuzluğun belirli bedensel sonucu olan kurumuş dili adlandırır.","gloss":"susuzluk ve kuruyan dil","neighbor_only":"Komşu dal susuzluk durumunu, susamayı ve susuz bırakmayı genel olarak kapsar.","neighbor_ref":"root_000968/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal susuzluk durumuyla ve onun bedendeki etkisiyle ilgilidir."}],"source_phrase_ar":"المعصور اللسان اليابس عطشا (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Susuzluk nedeniyle kurumuş dil anlamı bu kaynakta tek başına tanıklanır."}],"source_summary":"Kanıt, susuzluğun etkisiyle kuruyan dili sonuç durumu olarak tek başına tanımlar.","sources":["TA"],"what_is_ar":"يدخل فيه المعصور بمعنى اللسان اليابس عطشا.","what_is_not_ar":"ليس هو الشيء العصير المعصور، ولا الإعصار والغبار."},"support_links":[]},{"boundary":"Anlam döner rüzgar, koku algılama veya genel karın rahatsızlığı değil, bağırsak gazı çıkarmadır.","branch_kind":"bare","branch_ref":"root_001019/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"bağırsak gazı çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağırsak gazının bedenden çıkması ve çıkan gazın kendisi anlatılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel olayı doğal ve doğrudan biçimde karşılar.","boundary_detail":"Anlam döner rüzgar, koku algılama veya genel karın rahatsızlığı değil, bağırsak gazı çıkarmadır.","branch_image_ar":"العصار ريح البطن","concept_gloss":"bağırsak gazı çıkarma","definition":"Bağırsak gazının bedenden çıkarılması veya çıkan gaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağırsak gazının bedenden çıkması ve çıkan gazın kendisi anlatılır."}],"identity_rationale":"Kaynak ifadesi sözcüğü doğrudan bağırsak gazı çıkarma olayı veya bu olayda çıkan gaz olarak tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_049","rendering_kind":"ordinary","target_gloss":"bağırsak gazı çıkarma"}],"lexicalization_note":"Tanım çıplak biçimin bağırsak gazı çıkarma anlamıyla sınırlıdır ve genel rüzgar ya da koku alanına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı olayın fiil biçimi yayımlandı, öteki adaylar koku alma, rahatsızlık, kaba adlandırma veya genel bedensel durumdur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Olay çekirdeği ortaktır; bu dal isim olarak olay ya da gazı, komşu dal ise eylemin gerçekleşmesini bildirir.","focus_only":"Bu dal olay adı veya çıkan gazı adlandıran isim kullanımıdır.","gloss":"bağırsak gazı çıkarma","neighbor_only":"Komşu dal aynı bedensel olayın gerçekleşmesini bildiren fiil kullanımıdır.","neighbor_ref":"root_001400/B006","relation_type":"near_synonym","shared_zone":"Her iki dal aynı bedensel gaz çıkarma olayını anlatır."}],"source_phrase_ar":"العصار الفساء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bağırsak gazı çıkarma anlamı bu kaynakta tek başına tanıklanır."}],"source_summary":"Kanıt, bağırsak gazı çıkarma olayını ve çıkan gazı tek başına adlandırır.","sources":["TA"],"what_is_ar":"يدخل فيه العصار بمعنى الفساء.","what_is_not_ar":"ليس هو الإعصار، ولا الحين، ولا العصر بمعنى الحبس."},"support_links":[]},{"boundary":"Giysi kimliği kaynak içinde tartışmalıdır; zırh tercih edilse de baş sargısı ve siyah giysi seçenekleri görünür kalmalıdır.","branch_kind":"unresolved","branch_ref":"root_001019/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","surface_ar":"عَصْرِ"}],"gloss":"zırh, baş sargısı ya da siyah giysi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha güçlü açıklama, adı giyeni sıkan zırhlara bağlar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad için baş sargıları ve siyah giysiler seçenekleri de aktarılır."}}],"root_ar":"ع ص ر","root_id":"root_001019","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynak içindeki üç açıklamayı korur; zırhın daha güçlü görüş olduğu tanımda belirtilir.","boundary_detail":"Giysi kimliği kaynak içinde tartışmalıdır; zırh tercih edilse de baş sargısı ve siyah giysi seçenekleri görünür kalmalıdır.","branch_image_ar":"معاصر تلبس وتعصر","concept_gloss":"zırh, baş sargısı ya da siyah giysi","contextual_glosses":[{"applicability":"Kaynağın daha güçlü saydığı zırh yorumunun özellikle belirtilmesi gereken bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baş sargısı ve siyah giysi biçimindeki iki alternatif açıklamayı dışarıda bırakır.","preserves":"Tercih edilen zırh yorumunu ve sıkma gerekçesini korur."},"facet_ids":["F001"],"text":"giyeni sıkan zırhlar","usage_role":"explanatory"}],"definition":"Kimliği tartışmalı bir giysi adı: baş sargıları veya siyah giysiler diye açıklanmış, daha güçlü görüşte ise giyeni sıkan zırhlar olarak yorumlanmıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha güçlü açıklama, adı giyeni sıkan zırhlara bağlar."},{"facet_id":"F002","role":"source_variant","statement":"Aynı ad için baş sargıları ve siyah giysiler seçenekleri de aktarılır."}],"identity_rationale":"Tek kaynak aynı biçim için baş sargıları, siyah giysiler ve daha güçlü tercih olarak giyeni sıkan zırh açıklamalarını verir; dal korunabilir ancak tek bir giysi türü kesinmiş gibi sunulamaz.","lexicalization_note":"Söz birimi kaydı bulunmadığından çıplak veya kalıba bağlı kapsam varsayılmaz; yalnız kaynakta tartışılan çoğul giysi adı açıklanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel giysi dalı alan sınırını göstermek için yayımlandı, diğerleri belirli giyme eylemleri veya özel giysi türleridir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu dal genel giysi adıdır; bu dal ise baş sargısı, siyah giysi veya zırh diye çözümlenen tartışmalı özel bir addır.","focus_only":"Bu dal kimliği tartışmalı özel bir çoğul giysi adını ve zırh yorumunu taşır.","gloss":"özel giysi adı","neighbor_only":"Komşu dal türü ne olursa olsun genel giysi ve gömlek adını, giydirme ve giyinme eylemlerini kapsar.","neighbor_ref":"root_000692/B001","relation_type":"same_field","shared_zone":"Her iki dal insanın giydiği bir nesneyi adlandırma alanındadır."}],"source_phrase_ar":"المعاصر العمائم (maqayis)؛ قالوا هي ثياب سود (maqayis)؛ الصحيح من ذلك أن المعاصر الدروع مأخوذ من العصر لأنه يعصر بها (maqayis)","source_qualifications":[{"kind":"disagreement","summary":"Tek tanıklık baş sargısı, siyah giysi ve tercih edilen zırh açıklamalarını bir arada aktarır."}],"source_summary":"Kanıt tek bir giysi adını üç farklı açıklamayla verir ve zırh yorumunu daha güçlü sayar; kapsam bu anlaşmazlık nedeniyle çözümlenmemiştir.","sources":["MQ"],"what_is_ar":"يدخل فيه المعاصر في القول الذي يجعلها الدروع، مع ذكر الأقوال الأخرى في العمائم أو الثياب السود.","what_is_not_ar":"ليس هو معاصر العنب، ولا السحاب المعصر، ولا الجارية المعصر."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["103:1:1"],"branch_refs":[],"candidate_id":"cand_f6c172602983ed476c16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:1:1:compressed-oath-verb","source_type":"word_analysis","support_ids":["sup_1cb35e932cee7f6cec99","sup_fcadbbc7205ddee31d02"],"title":"suppressed oath verb compresses the formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:1","qac_refs":["103:1:1:1"],"status":"accepted"}},{"anchor_refs":["103:1:1"],"branch_refs":[],"candidate_id":"cand_c7dfbd17c573925fc886","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:1:1:deferred-oath-frame","source_type":"word_analysis","support_ids":["sup_1cb35e932cee7f6cec99","sup_3c0a93ecb9edfc8c23b3"],"title":"opening particle delays the sworn answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:1","qac_refs":["103:1:1:1"],"status":"accepted"}},{"anchor_refs":["103:1:1"],"branch_refs":[],"candidate_id":"cand_776ddf0dd0f6df4a9c1b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:1:1:oath-particle-scope","source_type":"word_analysis","support_ids":["sup_1cb35e932cee7f6cec99","sup_76866130b227fdd5e382"],"title":"oath particle governs the next noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:1","qac_refs":["103:1:1:1"],"status":"accepted"}},{"anchor_refs":["103:1:1"],"branch_refs":[],"candidate_id":"cand_2aac5d667b4e1181526e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:1:1:proclitic-audible-fusion","source_type":"word_analysis","support_ids":["sup_1cb35e932cee7f6cec99","sup_acb659acf10bd5b993d6"],"title":"bound particle fuses with the oath noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:1","qac_refs":["103:1:1:1"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_832b4598c38388a22f34","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:abstract-totalized-form","source_type":"word_analysis","support_ids":["sup_6f95654e08eebac6b2ff","sup_bbfd79b78cee56e86285"],"title":"singular abstract form gathers time into one field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_820cd93ba5e40b90ffe4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:bond-variant-apparatus","source_type":"word_analysis","support_ids":["sup_530eaccbc895843f0471","sup_bbfd79b78cee56e86285"],"title":"vowel variant exposes a bond path","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_ee8c32540bd94f37d901","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:compressed-sound-texture","source_type":"word_analysis","support_ids":["sup_96b60c13faf86d74b614","sup_bbfd79b78cee56e86285"],"title":"tight root cluster makes compression audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_25af9ca928d22033d706","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:convergent-oath-force","source_type":"word_analysis","support_ids":["sup_bbd9666b7cae983b2dc6","sup_bbfd79b78cee56e86285"],"title":"grammar, form, root, and sound converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_d882096250b28dd1348e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:definite-genitive-witness","source_type":"word_analysis","support_ids":["sup_83139b50d2d6690c60ca","sup_bbfd79b78cee56e86285"],"title":"definite genitive noun becomes the oath witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_f7488be0328ae2d5b2c1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:derivational-family-pressure","source_type":"word_analysis","support_ids":["sup_bbfd79b78cee56e86285","sup_c6b7024980e18b74ddae"],"title":"root relatives add pressure without controlling the parse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_32c414dcbc2a2682e09c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:final-one-noun-landing","source_type":"word_analysis","support_ids":["sup_3b0ad47c86862d09bc81","sup_bbfd79b78cee56e86285"],"title":"single noun carries the ayah landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_fbfa0c2fe639ff594e3c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:rare-abstract-distribution","source_type":"word_analysis","support_ids":["sup_b43766012100d199e0ce","sup_bbfd79b78cee56e86285"],"title":"rare abstract root use marks the oath choice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_25e58e2b7140347c49eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:shawadhdh-calamity-expansion","source_type":"word_analysis","support_ids":["sup_8437c692c18b3b5aa19d","sup_bbfd79b78cee56e86285"],"title":"expanded reading makes time's shocks explicit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:2"],"branch_refs":[],"candidate_id":"cand_d7f6ba2be38f9aa8f44e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:2:temporal-sense-with-pressure","source_type":"word_analysis","support_ids":["sup_4faa9f1830823bc89cca","sup_bbfd79b78cee56e86285"],"title":"time remains primary while pressing colors it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:1:2","qac_refs":["103:1:1:2","103:1:1:3"],"status":"accepted"}},{"anchor_refs":["103:1:1"],"branch_refs":[],"candidate_id":"cand_023f365b1bc0f10d78cb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001019"],"scope":"focus_ayah","source_local_id":"103:1:1:3","source_type":"qac_morpheme","support_ids":["sup_9edc117efd40b328d2bf"],"title":"QAC root occurrence: ع ص ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["103:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:1","branch_refs":["root_001019/B001"],"candidate_id":"cand_57e4ad124fd696d5bc0e","commentary_obligation":"review","hft_ref":"hft_8ba1a3746556da57d606","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-recurring-witness","source_type":"hft","support_ids":["sup_f3f25600e6d4c151d6c4"],"title":"baseline-recurring-witness","trust":"legacy_unbound"},{"anchor_refs":["103:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:1","branch_refs":["root_001019/B002","root_001019/B007"],"candidate_id":"cand_aeeec94145555ecea4c7","commentary_obligation":"review","hft_ref":"hft_e19f6ff3a88bef639080","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-pressure-extraction","source_type":"hft","support_ids":["sup_07abbe7d9d7ffa9abe85"],"title":"baseline-pressure-extraction","trust":"legacy_unbound"},{"anchor_refs":["103:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:1","branch_refs":["root_001019/B005","root_001019/B006"],"candidate_id":"cand_8ac68e84bce74f717e19","commentary_obligation":"review","hft_ref":"hft_17d4b85571ea0f04b7a7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-constraining-refuge","source_type":"hft","support_ids":["sup_c815c5c9175925de329b"],"title":"baseline-constraining-refuge","trust":"legacy_unbound"},{"anchor_refs":["103:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:1","branch_refs":["root_001019/B009","root_001019/B010"],"candidate_id":"cand_92acfc78e23f28655524","commentary_obligation":"review","hft_ref":"hft_f3f83c6507d6cdae5935","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-enclosed-maturation","source_type":"hft","support_ids":["sup_7f0b3a089c65fe8ff40a"],"title":"baseline-enclosed-maturation","trust":"legacy_unbound"},{"anchor_refs":["103:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:1","branch_refs":["root_001019/B003","root_001019/B004"],"candidate_id":"cand_36b4f292edc9ca347330","commentary_obligation":"review","hft_ref":"hft_1da5a8752e8b68522dfb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-atmospheric-release","source_type":"hft","support_ids":["sup_52ae367498bfb9de1eaa"],"title":"baseline-atmospheric-release","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلْعَصْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"103:1:1:1","qac_word_ref":"103:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"103:1:1:2","qac_word_ref":"103:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","root_ar":"ع ص ر","surface_ar":"عَصْرِ"}],"word_analysis_qac_refs":[["103:1:1:1"],["103:1:1:2","103:1:1:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["103:1:1","103:1:2"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلْعَصْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"103:1:1:1","qac_word_ref":"103:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"103:1:1:2","qac_word_ref":"103:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَصْر","morph_features":"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:1:1:3","qac_word_ref":"103:1:1","root_ar":"ع ص ر","surface_ar":"عَصْرِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["103:1:1:1"],["103:1:1:2","103:1:1:3"]],"word_analysis_refs":["103:1:1","103:1:2"],"word_rows":[{"analysis_record_ref":"103:1:1","analytic_gloss_range_en":"oath particle at surah onset, not ordinary coordination; it governs the following genitive noun and opens a deferred oath frame","analytic_root_gloss_range_en":null,"qac_refs":["103:1:1:1"],"root":{"note":"no root (particle)"},"surface":{"arabic":"وَ","transliteration":"wa-"}},{"analysis_record_ref":"103:1:2","analytic_gloss_range_en":"definite singular abstract oath-object, locally selecting time, era, or afternoon as a totalized witness while allowing narrowed pressure imagery from the root","analytic_root_gloss_range_en":"broad root range includes age or recurring time, pressing and extraction, rain-pressure, whirlwind, refuge, withholding, yield, and other branch-specific senses; the local form selects the temporal oath branch, with pressure-family effects retained only as narrowed resonance","qac_refs":["103:1:1:2","103:1:1:3"],"root":{"arabic":"ع ص ر","transliteration":"ʿ-ṣ-r"},"surface":{"arabic":"ٱلْعَصْرِ","transliteration":"al-ʿaṣr"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["103:1"],"branch_refs":["root_001019/B001"],"candidate_id":"cand_57e4ad124fd696d5bc0e","evidence_scope":"focus_ayah","hft_ref":"hft_8ba1a3746556da57d606","item_id":"baseline-recurring-witness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-recurring-witness","support_id":"sup_f3f25600e6d4c151d6c4"},{"anchor_refs":["103:1"],"branch_refs":["root_001019/B002","root_001019/B007"],"candidate_id":"cand_aeeec94145555ecea4c7","evidence_scope":"focus_ayah","hft_ref":"hft_e19f6ff3a88bef639080","item_id":"baseline-pressure-extraction","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-pressure-extraction","support_id":"sup_07abbe7d9d7ffa9abe85"},{"anchor_refs":["103:1"],"branch_refs":["root_001019/B005","root_001019/B006"],"candidate_id":"cand_8ac68e84bce74f717e19","evidence_scope":"focus_ayah","hft_ref":"hft_17d4b85571ea0f04b7a7","item_id":"baseline-constraining-refuge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-constraining-refuge","support_id":"sup_c815c5c9175925de329b"},{"anchor_refs":["103:1"],"branch_refs":["root_001019/B009","root_001019/B010"],"candidate_id":"cand_92acfc78e23f28655524","evidence_scope":"focus_ayah","hft_ref":"hft_f3f83c6507d6cdae5935","item_id":"baseline-enclosed-maturation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-enclosed-maturation","support_id":"sup_7f0b3a089c65fe8ff40a"},{"anchor_refs":["103:1"],"branch_refs":["root_001019/B003","root_001019/B004"],"candidate_id":"cand_36b4f292edc9ca347330","evidence_scope":"focus_ayah","hft_ref":"hft_1da5a8752e8b68522dfb","item_id":"baseline-atmospheric-release","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-atmospheric-release","support_id":"sup_52ae367498bfb9de1eaa"}],"diagnostics":[],"lane_counts":{"global":9,"macro":9,"micro":5},"packet_summary":{"ayah_count":3,"focus_ref":"103:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[],"window":["103:1","103:2","103:3"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"103:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"103:1","lane":"micro","linguistic_source_ref":"103:1","surface_ref":"103:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"103:1","target_tokens":[["Zamana",["103:1:1"]],["yemin",["103:1:1"]],["olsun",["103:1:1"]]],"text":"Zamana yemin olsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":3,"id":"s103-p01-001-003","label":"Whole surah","number":1,"refs":["103:1","103:2","103:3"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:1","source_type":"word_analysis","support_id":"sup_1cb35e932cee7f6cec99","text":"{\"gloss_range\":\"oath particle at surah onset, not ordinary coordination; it governs the following genitive noun and opens a deferred oath frame\",\"prose\":\"{{ar:وَ}} ({{tr:wa-}}) is not functioning here as a simple connective. At the opening of the surah, before any prior clause exists to join, it acts as the initiated oath particle and makes the following noun its genitive sworn-by object; this is the surah-opening oath use of {{ar:وَ}} ({{tr:wa-}}), not a continuing oath link or an oath introduced by another particle. That first particle therefore sets the discourse mode before any lexical predicate appears: the listener enters an oath-frame and waits for the answer in 103:2. The oath act itself remains compressed; Arabic leaves the swearing verb unspoken and gives only particle plus governed noun. Because the particle is a bound proclitic and runs into the hamzat wasl of {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}), the dependency is also seen and heard as one compact opening unit.\",\"root_display\":\"no root (particle)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:final-one-noun-landing","source_type":"word_analysis","support_id":"sup_3b0ad47c86862d09bc81","text":"{\"blocking_evidence\":null,\"headline\":\"single noun carries the ayah landing\",\"reader_payoff\":\"The reader feels the first ayah close on one unexplained oath noun and carry its force across the boundary into 103:2.\",\"reason\":\"The word is the only lexical noun of the ayah and attachment support identifies the oath response as following in 103:2. This preserves the CRITICAL structural payoff of delayed explanation and concentrated closure.\",\"representative_source_ids\":[\"QT-3960ac7b\",\"QT-cd033487\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:1:deferred-oath-frame","source_type":"word_analysis","support_id":"sup_3c0a93ecb9edfc8c23b3","text":"{\"blocking_evidence\":null,\"headline\":\"opening particle delays the sworn answer\",\"reader_payoff\":\"The reader sees that the first word launches a sworn frame whose assertion arrives only with the verdict in 103:2.\",\"reason\":\"Attachment translation support warns that a one-ayah rendering can leave the oath without its response, and identifies the assertion as completed by the following clause. The CRITICAL rows' discourse claim is therefore locally supported.\",\"representative_source_ids\":[\"QI-977c8604\",\"QT-068580b6\",\"QT-6f4a0da4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:temporal-sense-with-pressure","source_type":"word_analysis","support_id":"sup_4faa9f1830823bc89cca","text":"{\"blocking_evidence\":null,\"headline\":\"time remains primary while pressing colors it\",\"reader_payoff\":\"The reader senses time as an invoked field that compresses, extracts, and tests, while still reading the local noun as temporal.\",\"reason\":\"V4 accepts both time and pressing branches for the root, and QAC selects a definite abstract noun of time governed as the oath object. The pressure image survives as narrowed semantic coloring, not as replacement of the temporal sense.\",\"representative_source_ids\":[\"QS-0ab39284\",\"QS-61caf1f8\",\"QS-77e663ef\",\"QS-fc91b54a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:bond-variant-apparatus","source_type":"word_analysis","support_id":"sup_530eaccbc895843f0471","text":"{\"blocking_evidence\":null,\"headline\":\"vowel variant exposes a bond path\",\"reader_payoff\":\"The reader sees that the irregular {{ar:وَالْعِصْرِ}} ({{tr:wa-l-ʿiṣri}}) can expose a rope or covenant sense, while the received local form remains the temporal oath noun.\",\"reason\":\"Variant evidence can survive as apparatus, but QAC alignment is to {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) with the canonical vowel pattern. The bond reading therefore contrasts with, rather than governs, the local parse.\",\"representative_source_ids\":[\"QF-474bd888\",\"QE-0b48c572\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:abstract-totalized-form","source_type":"word_analysis","support_id":"sup_6f95654e08eebac6b2ff","text":"{\"blocking_evidence\":null,\"headline\":\"singular abstract form gathers time into one field\",\"reader_payoff\":\"The reader sees the noun's article, singularity, and abstract form gather the temporal field as one sworn domain before the answer in 103:2.\",\"reason\":\"The local word is tagged as a definite singular NOUN_ABSTRACT, and V4 local form observations place it in the noun class. This supports the CRITICAL claim that the selected shape totalizes rather than individuates episodes.\",\"representative_source_ids\":[\"QF-39d994d0\",\"QI-71798483\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:1:oath-particle-scope","source_type":"word_analysis","support_id":"sup_76866130b227fdd5e382","text":"{\"blocking_evidence\":null,\"headline\":\"oath particle governs the next noun\",\"reader_payoff\":\"The reader notices that {{ar:وَ}} ({{tr:wa-}}) is the initiated surah-opening oath particle here, not ordinary joining or a continuing oath link, so {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) is invoked as the sworn-by object.\",\"reason\":\"QAC identifies the particle as the oath particle at surah onset, and attachment evidence marks a syntactically forced particle-complement relation with the following genitive noun. This supports the CRITICAL claim that the local reading is oath, not coordination.\",\"representative_source_ids\":[\"QG-f47f9c67\",\"MG-742efa9d\",\"QS-c4d23ee8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:definite-genitive-witness","source_type":"word_analysis","support_id":"sup_83139b50d2d6690c60ca","text":"{\"blocking_evidence\":null,\"headline\":\"definite genitive noun becomes the oath witness\",\"reader_payoff\":\"The reader notices that {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) is the definite sworn-by witness, not an indefinite time or a temporal adverb.\",\"reason\":\"QAC and attachment evidence identify a definite masculine singular genitive noun governed by the oath particle. Contextual evidence marks the exact root-form as scoped by oath, supporting witness-role rather than adverbial timing.\",\"representative_source_ids\":[\"QG-46a698cb\",\"QG-9fa6aa4c\",\"QG-e4cd5380\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:shawadhdh-calamity-expansion","source_type":"word_analysis","support_id":"sup_8437c692c18b3b5aa19d","text":"{\"blocking_evidence\":null,\"headline\":\"expanded reading makes time's shocks explicit\",\"reader_payoff\":\"The reader sees that expanded shawadhdh wording spells out calamities of time, while the received oath keeps that temporal pressure folded into one noun.\",\"reason\":\"The expansion is useful contrast for the pressure point, but it is anomalous and cannot govern the canonical local text. The topic is preserved only as apparatus for what the received form leaves compressed.\",\"representative_source_ids\":[\"QF-b21bb9ca\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:compressed-sound-texture","source_type":"word_analysis","support_id":"sup_96b60c13faf86d74b614","text":"{\"blocking_evidence\":null,\"headline\":\"tight root cluster makes compression audible\",\"reader_payoff\":\"The reader hears the tight root cluster as acoustic compression, with irregular phonetic readings showing how a small vowel can loosen that compactness.\",\"reason\":\"The local canonical form contains the compact consonant cluster, while the cited phonetic variants alter pacing without changing the canonical lexical identity. The sound payoff is retained but narrowed to acoustic reinforcement.\",\"representative_source_ids\":[\"QP-418ac561\",\"QP-9211aa6d\",\"QP-9c79e498\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"103:1:1:3","source_type":"qac_morpheme","support_id":"sup_9edc117efd40b328d2bf","text":"{\"lemma_ar\":\"عَصْر\",\"morph_features\":\"STEM|POS:N|LEM:EaSor|ROOT:ESr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"103:1:1:3\",\"qac_word_ref\":\"103:1:1\",\"root_ar\":\"ع ص ر\",\"surface_ar\":\"عَصْرِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:1:proclitic-audible-fusion","source_type":"word_analysis","support_id":"sup_acb659acf10bd5b993d6","text":"{\"blocking_evidence\":null,\"headline\":\"bound particle fuses with the oath noun\",\"reader_payoff\":\"The reader hears and sees the oath relation immediately because the bound {{ar:وَ}} ({{tr:wa-}}) clings to the noun it governs.\",\"reason\":\"The local surface is a proclitic particle attached to the following noun, and the syntactic relation is forced by the oath construction. The phonetic liaison claim is a surface payoff rather than a separate syntactic parse.\",\"representative_source_ids\":[\"QF-d0951acd\",\"QP-381e2eff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:rare-abstract-distribution","source_type":"word_analysis","support_id":"sup_b43766012100d199e0ce","text":"{\"blocking_evidence\":null,\"headline\":\"rare abstract root use marks the oath choice\",\"reader_payoff\":\"The reader notices that the oath uses the root in a rare abstract noun slot rather than in the concrete or process-like forms supplied elsewhere.\",\"reason\":\"Contextual profiles mark the exact root-form as low occurrence, and QAC identifies the local form as NOUN_ABSTRACT. The CRITICAL distributional claim is therefore preserved as markedness, not as proof that every branch is locally active.\",\"representative_source_ids\":[\"QI-22090cb2\",\"QI-f482a733\",\"QH-3e818e8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:convergent-oath-force","source_type":"word_analysis","support_id":"sup_bbd9666b7cae983b2dc6","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, form, root, and sound converge\",\"reader_payoff\":\"The reader notices the opening's combined force: witness grammar, totalizing form, pressure-root memory, and compressed sound all meet in the single noun.\",\"reason\":\"The synthesis row is not a new independent sense; it accurately gathers already retained grammatical, formal, lexical, and phonetic payoffs into the ayah's concentrated oath opening.\",\"representative_source_ids\":[\"QY-0f8e408d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2","source_type":"word_analysis","support_id":"sup_bbfd79b78cee56e86285","text":"{\"gloss_range\":\"definite singular abstract oath-object, locally selecting time, era, or afternoon as a totalized witness while allowing narrowed pressure imagery from the root\",\"prose\":\"{{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) is the genitive sworn-by noun governed by the opening oath particle, not a temporal adverb telling when something happens. Its article, singular shape, and abstract noun form gather the referent as the time, era, or afternoon invoked as witness, and the oath waits for its answer in 103:2. The root field keeps more than a neutral clock-word in view: accepted dictionary branches include time and pressing, so the local temporal sense is primary while the pressure and extraction image makes the sworn field feel compressive and testing. That pressure is not allowed to replace the local meaning with a concrete press, juice, storm, or action in progress; the selected form is a stable oath-object. The root's rare Quranic distribution strengthens the markedness of the choice, since this abstract noun is set beside other supplied uses involving pressing, rain-production, whirlwind, and related concrete or process forms (12:36, 12:49, 2:266, 78:14). Variant evidence remains apparatus: the irregular {{ar:وَالْعِصْرِ}} ({{tr:wa-l-ʿiṣri}}) opens a bond or covenant path, and expanded shawadhdh wording makes calamities of time explicit, but the received form keeps the oath compressed in the definite temporal noun. The final position also matters: the ayah lands on this one noun with no adjective or explanation, while the tight root cluster makes the compression audible and irregular helping-vowel readings show how that compact -ṣr- pacing can be loosened without changing the canonical sense.\",\"root_display\":\"{{ar:ع ص ر}} ({{tr:ʿ-ṣ-r}})\",\"root_gloss_range\":\"broad root range includes age or recurring time, pressing and extraction, rain-pressure, whirlwind, refuge, withholding, yield, and other branch-specific senses; the local form selects the temporal oath branch, with pressure-family effects retained only as narrowed resonance\",\"surface_display\":\"{{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:2:derivational-family-pressure","source_type":"word_analysis","support_id":"sup_c6b7024980e18b74ddae","text":"{\"blocking_evidence\":null,\"headline\":\"root relatives add pressure without controlling the parse\",\"reader_payoff\":\"The reader can connect the oath noun to root-family pressure in pressing, rain-production, and whirlwind scenes (12:36, 12:49, 2:266, 78:14), while the local form stays an abstract noun.\",\"reason\":\"The CRITICAL rows supply concrete Quranic references for related root-family pressure. V4 confirms accepted pressure, rain, and whirlwind branches, but the local QAC form is not Form IV, not a concrete press, and not a process verb, so the relation must be narrowed.\",\"representative_source_ids\":[\"QS-f19a05cb\",\"QF-755caa1e\",\"QE-4a0e9ef5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:1:1:compressed-oath-verb","source_type":"word_analysis","support_id":"sup_fcadbbc7205ddee31d02","text":"{\"blocking_evidence\":null,\"headline\":\"suppressed oath verb compresses the formula\",\"reader_payoff\":\"The reader notices that the oath is compressed into particle plus genitive noun, with the act of swearing left unlexicalized.\",\"reason\":\"The attachment ellipsis profile explicitly marks a strongly licensed formulaic omitted oath verb, matching the CRITICAL row's compression claim.\",\"representative_source_ids\":[\"QT-a73ff21f\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْعَصْرِ","ayah_ref":"103:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001019/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001019","role":"The literal range of age and recurring time supplies the successive temporal field and gives that field an evidentiary role in the oath.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]}],"changed_reading":{"after":"The oath calls recurring succession itself as witness: alternation and return make temporal passage an active field of disclosure.","before":"The phrase is a bare oath by an unspecified unit of time."},"confidence":"strong","focus_anchor":"The noun عَصْر and the oath construction وَٱلْعَصْرِ.","mechanism":"The named span is not inert chronology: recurrence, alternation, and the arrival of phases let temporal succession function as a witness that repeatedly exposes what occupies it.","model_id":"baseline-recurring-witness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-recurring-witness","source_type":"hft","support_id":"sup_f3f25600e6d4c151d6c4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْعَصْرِ","ayah_ref":"103:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001019/B002","root_001019/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001019","role":"The literal press that makes liquid run supplies the pressure-to-extraction mechanism for the temporal span.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_001019","role":"The literal image of bestowed or extracted yield identifies the possible output of the temporal press as gain rather than mere depletion.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]}],"changed_reading":{"after":"The named span presses what it contains until its hidden yield or lack of yield becomes manifest.","before":"Time merely passes over its contents."},"confidence":"medium","focus_anchor":"The root ع ص ر in عَصْر.","mechanism":"A span can be imagined as a press: sustained enclosure and force draw out a latent liquid, residue, gain, or yield. The oath therefore foregrounds what duration extracts from what it contains.","model_id":"baseline-pressure-extraction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-pressure-extraction","source_type":"hft","support_id":"sup_07abbe7d9d7ffa9abe85","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْعَصْرِ","ayah_ref":"103:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001019/B005","root_001019/B006"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001019","role":"The literal refuge, rescue, and attachment image supplies a mode of survival by holding fast within the root's field.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001019","role":"The literal withholding and reclamation image supplies the opposing grip that makes refuge necessary and keeps the model internally tense.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]}],"changed_reading":{"after":"Al-ʿaṣr can be the constraining grip and, simultaneously, the field in which attachment becomes refuge.","before":"Time is only an external threat from which rescue must come elsewhere."},"confidence":"exploratory","focus_anchor":"The lexical field of ع ص ر carried by the sole focus noun.","mechanism":"The same root can organize a polarity: pressure withholds and reclaims, yet attachment provides refuge and rescue. The oath can name a constraining medium whose grip is dangerous but within which clinging is also possible.","model_id":"baseline-constraining-refuge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-constraining-refuge","source_type":"hft","support_id":"sup_c815c5c9175925de329b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْعَصْرِ","ayah_ref":"103:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001019/B009","root_001019/B010"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_001019","role":"The literal arrival at youthful maturity supplies development toward a threshold as one function of the named span.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_001019","role":"The literal grain enclosed in its sheaths supplies protective containment as the spatial mechanism of maturation.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]}],"changed_reading":{"after":"The oath can invoke an enclosing phase that brings contents to ripeness while sheltering what is still forming.","before":"Aging means only that time consumes what lives in it."},"confidence":"exploratory","focus_anchor":"The form عَصْر as a phase or condition within the root's inventory.","mechanism":"Temporal enclosure need not mean attrition. Reaching youth and grain entering protective sheaths make a span into a maturation chamber in which vulnerability, ripeness, and preservation coexist.","model_id":"baseline-enclosed-maturation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-enclosed-maturation","source_type":"hft","support_id":"sup_7f0b3a089c65fe8ff40a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْعَصْرِ","ayah_ref":"103:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001019/B003","root_001019/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001019","role":"The literal rain-bearing compression supplies accumulation followed by release as a temporal mechanism.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_001019","role":"The literal whirlwind and rising column supply circulation and visible turbulence rather than simple linear passage.","root":"ع ص ر","source_ref":"103:1","source_word_indices":["1"]}],"changed_reading":{"after":"The oath can evoke a gathering temporal force whose compression, circulation, and eventual release reveal its contents.","before":"The oath points to a fixed time-marker."},"confidence":"exploratory","focus_anchor":"The root ع ص ر in the focus noun, through its meteorological branches.","mechanism":"The span gathers force like a weather system: cloud is compressed toward rain while wind curls matter into a visible column. Time becomes accumulated pressure approaching release, not a flat line.","model_id":"baseline-atmospheric-release"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-atmospheric-release","source_type":"hft","support_id":"sup_52ae367498bfb9de1eaa","trust":"legacy_unbound"}]}
</lane_packet_json>
