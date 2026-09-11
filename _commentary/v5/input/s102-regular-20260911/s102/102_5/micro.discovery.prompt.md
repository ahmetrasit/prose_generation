# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **102:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s102-regular-20260911/s102/102_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "102:5",
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
{"analysis_context":{"analysis_id":"s102-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"102:5","host_surah":102,"lane_context_refs":[],"ordered_context_refs":["102:0","102:1","102:2","102:3","102:4","102:6","102:7","102:8","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B001","candidate_links":[{"candidate_id":"cand_202c86c06aff5d745f62","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"bilme ve gerçeğini kavrama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgisizliğin karşıtı olan temel zihinsel edinimi, tanımayı ve gerçeğe uygun kavrayışı birlikte karşılar.","boundary_detail":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_image_ar":"انكشاف الشيء للعارف","concept_gloss":"bilme ve gerçeğini kavrama","contextual_glosses":[{"applicability":"Bir olay veya gelişme hakkındaki haberin kişinin bilgisine ulaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin farkına varma ve ondan bilgi edinme yönünü korur."},"facet_ids":["F002"],"text":"haberinden haberdar olmak","usage_role":"contextual"},{"applicability":"Bilginin tekrar ve yönlendirmeyle bir öğrenende yerleşmesini sağlayan öğretim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin aktarılması ve öğrenende kalıcı bir sonuç oluşturması sürecini korur."},"facet_ids":["F003"],"text":"öğretmek ve öğrenmesini sağlamak","usage_role":"explanatory"},{"applicability":"İki kişi arasındaki bilgi sınamasında bir tarafın ötekini yenmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi alanındaki karşılaştırmayı ve üstün gelme sonucunu korur."},"facet_ids":["F004"],"text":"bilgide üstün gelmek","usage_role":"contextual"}],"definition":"Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}],"identity_rationale":"Dalın bilme ve bilgisizliğin karşıtı olma yönündeki çekirdeği kaynak ifadesiyle uyumludur. Ancak haberden haberdar olma, öğretme, öğrenme ve bilgi bakımından üstün gelme kullanımları bu çekirdekle aynı düzeyde değil, belirli biçimlere bağlı uzantılar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilgi; bir şeyi gerçeğiyle kavrama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek ve tanımak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haberinden haberdar olmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bildirmek, haberdar etmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öğretmek, öğrenmesini sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öğrenmek, kavramaya yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilmek; buyrukta bil ki"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bilgi yarışında yenmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilen ve bildiğine göre davranan kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bilgili, bilgi sahibi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok bilgili, çok bilen"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"son derece bilgili kişi"}],"lexicalization_note":"Tanım çıplak bilme çekirdeğini öne alır; haber, öğretim, öğrenim ve karşılıklı bilgi sınamasıyla ilgili anlamları yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bilme çekirdeğini en çok açıklayan yakın kavrayış dalı, açık karşıtı olan bilgisizlik dalı ve doğru kullanım boyutu taşıyan bilgelik dalı seçildi; öteki adaylar yalnızca uzak çağrışım veya ayrı kök içi anlam alanı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri yakın olsa da odak dalın biçime bağlı aktarım ve edinim süreçleri ile komşunun akletme ve hızlı anlama vurgusu karşılıklı değiştirilebilirliği sınırlar.","focus_only":"Odak dal, haberden haberdar etme, öğretme, öğrenme ve bilgi yarışında üstün gelme gibi biçime bağlı uzantıları da kapsar.","gloss":"bilmek ve anlamını kavramak","neighbor_only":"Komşu dal, anlamları doğrulama, akletme ve çabuk kavrama yönlerini ayrıca öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme, tanıma ve zihnen kavrama alanında büyük ölçüde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilgiye erişmeyi ve kavramayı bildirirken komşu dal bu erişimin bulunmamasını ya da gerçeğin yanlış bilinmesini bildirir.","focus_only":"Bir şeyi tanıma, gerçeğine uygun kavrama ve bilgi sahibi olma bulunur.","gloss":"bilgi ile bilgisizlik karşıtlığı","neighbor_only":"Bilginin yokluğu, durumu tanımama veya gerçeğe aykırı bir kanaat bulunur.","neighbor_ref":"root_000271/B001","relation_type":"antonym","shared_zone":"İki dal aynı zihinsel erişim ekseninin olumlu ve olumsuz uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bilmek tek başına odak dal için yeterli olabilir; komşu dal ise bilginin doğru yargı ve isabetli davranışla birleşmesini öne çıkarır.","focus_only":"Odak dalda yalın bilme ve tanıma, bilginin doğru kullanımından bağımsız olarak çekirdekte yer alabilir.","gloss":"bilgi ile bilgelik","neighbor_only":"Komşu dal doğruyu bulma, yerinde yargı ve bilgiyi isabetli kullanma niteliğini gerektirir.","neighbor_ref":"root_000348/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bilgi sahibi olmayı ve zihinsel kavrayışı paylaşır."}],"source_phrase_ar":"العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bilgiyi bilgisizliğin karşıtı sayar ve bir şeyi tanıyıp gerçeğiyle kavramayı öne çıkarır. Toplu tanıklık ayrıca haberden haberdar olmayı, bilgiyi aktarmayı, öğrenmeyi ve bilgiyle üstün gelmeyi biçime bağlı uzantılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم","what_is_not_ar":"ليس هو العلامة الحسية ولا الجبل ولا الراية ولا الشق في الشفة ولا اسم العالمين"},"support_links":["sup_5d57b721bad5d690c623"]},{"boundary":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B002","candidate_links":[{"candidate_id":"cand_f869eada5b348e9211ed","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"ayırt edici ve yol gösterici işaret","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi tanınır kılan veya ona ulaşmayı sağlayan belirgin iz ve işaretlerin ortak çekirdeğini karşılar.","boundary_detail":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_image_ar":"أثر يميز الشيء ويهدي إليه","concept_gloss":"ayırt edici ve yol gösterici işaret","contextual_glosses":[{"applicability":"Askerlerin çevresinde toplandığı bayrak ya da yol bulmayı sağlayan belirgin dağ ve iz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görünürlük ile yöneltme ve tanıtma işlevini korur."},"facet_ids":["F002"],"text":"bayrak veya uzaktan seçilen kılavuz","usage_role":"contextual"},{"applicability":"Bir savaşçıya, kumaşa veya sarığa başkalarından ayıran görünür bir belirti ekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin sonradan konmasını ve ayırt etme amacını korur."},"facet_ids":["F003"],"text":"tanıtıcı işaret koymak","usage_role":"contextual"},{"applicability":"Belirli bir son zamanın yaklaştığını haber veren gösterge bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın yakınlığını gösterme işlevini korur."},"facet_ids":["F004"],"text":"yaklaşmayı gösteren belirti","usage_role":"explanatory"}],"definition":"Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."},{"facet_id":"F003","role":"associated_use","statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasından ayıran belirgin izi dalın ortak çekirdeği olarak açıkça destekler. Bayrak, belirgin dağ, yol belirtisi, kumaş deseni ve savaş işareti gibi örnekler bu çekirdeğin farklı gerçekleşmeleridir; tanınmış kişi ve son zaman belirtisi ise benzetme veya gösterme ilişkisine bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayırt edici işaret"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bayrak, sancak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin dağ"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kumaşın kenar işareti veya deseni"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yol gösteren iz veya belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"savaşta kendine ayırt edici işaret takmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kumaşı işaretlemek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işaret olarak kullanılan kına"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sarığı tanıtıcı bir biçimde sarmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tanınmış ve öne çıkan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"son saatin yaklaştığını gösteren belirti"}],"lexicalization_note":"Ayırt edici iz çıplak çekirdektir; savaşçı, kumaş, sarık ve belirli zaman göstergesiyle kurulan anlamlar kendi kuruluşlarına bağlı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar geçmişten kalan iz, bilerek konan tanıtıcı işaret ve fiziksel damga ile yapıldı; bayrak adayı yalnızca tek bir alt gerçekleşmeyi, öteki adaylar ise daha uzak renk veya biçim belirtilerini karşılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda işaret önceden konabilir veya doğal bir kılavuz olabilir; komşu dalda iz, daha önceki bir varlık ya da olayın geride kalan sonucudur.","focus_only":"Odak dal, bilerek konan bayrak ve işaretlerin yanı sıra yön bulduran belirgin dağ gibi göstergeleri de kapsar.","gloss":"işaret ile kalıntı iz","neighbor_only":"Komşu dal, geçmişte var olmuş veya gerçekleşmiş bir şeyden geriye kalan izi özellikle gerektirir.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da görünür bir izin başka bir şeyi tanıtması veya ona kanıt olması bakımından örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği işaretleme eylemine daha sıkı bağlıdır; odak dal ise konmuş işaretlerin yanında doğal kılavuzları ve bayrağı da adlandırır.","focus_only":"Odak dal doğal dağ işaretini, bayrağı, yol belirtisini ve kumaş kenarını da içine alan daha geniş bir gösterge alanına sahiptir.","gloss":"ayırt edici işaret koyma","neighbor_only":"Komşu dal özellikle atlara, varlıklara veya nesnelere tanıtma amacıyla işaret koyma eylemini öne çıkarır.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığı başkalarından ayıracak görünür bir işaretle tanıtmayı kapsar."},{"boundary_match":"partial","distinction":"Damga bir yüzeye bilerek bırakılan fiziksel izdir; odak dalın işareti ise doğal veya yapılmış olabilir ve yön gösterme işlevi de taşıyabilir.","focus_only":"Odak dal işaret koyma dışında bayrak, dağ, yol kılavuzu ve kumaş deseni gibi bağımsız adları da kapsar.","gloss":"işaret ile damga","neighbor_only":"Komşu dal, hayvana veya nesneye yakma, kesme ya da benzeri yolla bırakılan bedensel ve maddi damgayı gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_synonym","shared_zone":"Her iki dal görünür bir belirti aracılığıyla tanıtma ve ayırt etme işlevini paylaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)","source_summary":"Kaynaklar ayırt edici izi ortak temel sayar ve bayrak, yüksek ya da belirgin dağ, yol göstergesi, kumaş kenarı, kına ve sonradan yerleştirilen tanıtıcı işaretleri bu temelde toplar. Tanınmış kişi ile yaklaşan son zamanın belirtisi de görünürlük ve gösterme işlevinden doğan uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة","what_is_not_ar":"ليس هو إدراك العلم ولا اسم الخلق ولا شق الشفة العليا"},"support_links":["sup_c26b56eae4bddea714fc"]},{"boundary":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001040/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"evren ve bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış varlıkların tümünü tek bir düzen veya bütün olarak anlatan temel kullanım için uygundur.","boundary_detail":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_image_ar":"الخلق عالم يدل على صانعه","concept_gloss":"evren ve bütün yaratılmışlar","contextual_glosses":[{"applicability":"Sözün bütün evren yerine insan, görünmeyen varlıklar veya başka bir yaratık cinsi gibi ayrı sınıflara dağıtıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her yaratık cinsinin ayrı bir bütün sayılması yönünü korur."},"facet_ids":["F002"],"text":"varlıkların her bir sınıfı","usage_role":"explanatory"}],"definition":"Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, dalı yaratılmışların bütünü, gök düzeni ve içindekiler ya da yaratıkların ayrı sınıfları olarak açıklar. Her sınıfın ve bütünün yaratıcıyı gösteren bir belirti sayılması adlandırmanın gerekçesidir; bilme eylemi veya somut işaret dalıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"evren veya yaratılmışlar bütünü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bütün yaratıklar veya varlık sınıfları"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"evrenler, varlık dünyaları"}],"lexicalization_note":"Tanım, çıplak dalın evren, yaratılmışların bütünü ve varlık sınıfları anlamlarını verir; başka kuruluşlardan anlam aktarmaz.","neighbor_coverage_note":"Adayların çoğu hayvan bedenindeki renk ve işaretleri ya da ilgisiz özel adları anlatır; aynı kökün bilme ve işaret dalları adlandırma gerekçesini açıklasa da bu dalın yaratılmışlar bütünü sınırını keskinleştirecek bir karşıtlık oluşturmaz.","source_phrase_ar":"العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)","source_summary":"Kaynaklar bu adı yaratılmışların bütünü için kullanır; kapsam bazen evren ve içindekilerin tamamı, bazen de yaratıkların her bir cinsi veya sınıfıdır. Bütünün kendi yaratıcısına işaret etmesi adlandırmayı açıklayan ortak bir düşüncedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلم بمعنى الراية أو الجبل"},"support_links":[]},{"boundary":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"üst dudak yarığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin üst dudak bölgesindeki belirgin yarığı adlandıran temel kullanım için uygundur.","boundary_detail":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_image_ar":"شق ظاهر في الشفة العليا","concept_gloss":"üst dudak yarığı","contextual_glosses":[{"applicability":"Bir insanı veya deveyi üst dudak bölgesindeki yarıkla niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özelliğin taşıyıcıda bulunmasını ve anatomik yerini korur."},"facet_ids":["F002"],"text":"üst dudağı yarık","usage_role":"contextual"},{"applicability":"Bir kişinin üst dudağında yarık oluşturma eylemini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, etkilenen kişiyi ve üst dudak sınırını korur."},"facet_ids":["F003"],"text":"üst dudağını yarmak","usage_role":"contextual"}],"definition":"İnsanın üst dudağında veya devenin üst dudak bölgesinde bulunan belirgin yarıktır. Aynı dal, bu özelliği taşıyanı niteleyen biçimi ve üst dudağı yarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı açıkça üst dudaktaki yarıkla sınırlar; insanın üst dudağının yarılmış olması, devenin üst dudak bölgesindeki aynı belirti ve üst dudağı yarma eylemi bu kimliği doğrular. Genel yarılma anlamı veya alt dudaktaki bir biçim bozukluğu bu dala dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"üst dudaktaki yarık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst dudağı yarık kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"üst dudağını yarmak"}],"lexicalization_note":"Üst dudak yarığı dalın temelidir; yarıklı kişi veya deve nitelemesi ile üst dudağı yarma eylemi ilgili biçimlere bağlı tutulur.","neighbor_coverage_note":"Genel yarılma dalı süreç ve kapsam farkını, ağız eğriliği dalı ise yakın anatomik karışmayı açıklar; öteki adaylar kırık iyileşmesi, hayvan yapısı veya daha uzak ayrılma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve sonuç bakımından üst dudağa özelleşmiş anatomik bir addır; komşu dal ise nesne ve yüzey türü bakımından geniş bir yarılma eylemidir.","focus_only":"Odak dal belirli bir anatomik yerde, üst dudakta bulunan yarığı ve bu yarıkla niteleneni bildirir.","gloss":"üst dudak yarığı ile genel yarılma","neighbor_only":"Komşu dal nesne, deri, toprak, dağ ve başka yüzeylerdeki genel yarılma ve açılma sürecini kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir yüzeyin ayrılmasıyla oluşan yarık düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Yarık, dokuda açılma veya ayrılmadır; eğrilik ise bir bölümün yana yönelmiş biçimidir ve üst dudakta bir açıklık gerektirmez.","focus_only":"Odak dalda üst dudak dokusunun yarılmış olması gerekir.","gloss":"dudak yarığı ile ağız eğriliği","neighbor_only":"Komşu dalda ağız, dudak veya gözün bir yana eğri oluşu vardır; doku yarığı gerekmez.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal yüz ve ağız çevresindeki belirgin bir yapısal özelliği adlandırır."}],"source_phrase_ar":"العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)","source_summary":"Kaynaklar yarığın yerini üst dudak olarak ortak biçimde sınırlar ve yarıklı insanı bu özellikle niteler. Toplu tanıklık, devenin üst dudak bölgesindeki karşılığını ve üst dudağı yarma eylemini de aynı dalda gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلامة الموضوعة اختيارا ولا الشق في الشفة السفلى"},"support_links":[]},{"boundary":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_kind":"bare","branch_ref":"root_001040/B005","candidate_links":[{"candidate_id":"cand_3c746652fe18d2b402c2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"deniz ya da suyu bol kuyu","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biçiminin kaynaklarda verilen iki ayrı karşılığını eksiltmeden birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_image_ar":"ماء كثير مجتمع في عيلم","concept_gloss":"deniz ya da suyu bol kuyu","contextual_glosses":[{"applicability":"Sözlük biçiminin geniş su kütlesi karşılığıyla kullanıldığı tanıklığa özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan suyu bol kuyu karşılığını dışarıda bırakır.","preserves":"Deniz karşılığını doğal ve doğrudan biçimde korur."},"facet_ids":["F002"],"text":"deniz","usage_role":"contextual"},{"applicability":"Sözlük biçiminin bol su içeren kuyu karşılığıyla kullanıldığı tanıklıklara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan deniz karşılığını dışarıda bırakır.","preserves":"Kuyu türünü ve suyunun çokluğu koşulunu korur."},"facet_ids":["F003"],"text":"suyu bol kuyu","usage_role":"contextual"}],"definition":"Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}],"identity_rationale":"Kaynak ifadesi tek bir su birikimi türü tanımlamaz; aynı sözlük biçimi için deniz ve suyu bol kuyu olmak üzere iki ayrı karşılık verir. Dal korunabilir, ancak geçici çerçevedeki ortak su kütlesi görüntüsü yerine bu açık seçeneklilik tanıma yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deniz"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu"}],"lexicalization_note":"Tanım çıplak sözlük biçiminin deniz ve suyu bol kuyu karşılıklarını ayrı ayrı korur; bunlardan genel bir su birikintisi anlamı türetmez.","neighbor_coverage_note":"Deniz karşılığını açıklayan geniş su dalı ile kuyu çevresindeki bol su dalı seçildi; diğer adaylar gölet, artık su, taşkın veya su tutan arazi gibi farklı taşıyıcı ve süreçlere bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca deniz karşılığındadır; odak dalın kuyu seçeneği komşuda bulunmaz, komşunun büyük ırmak ve genel su genişliği ise odak dalın tanımına girmez.","focus_only":"Odak dal aynı sözlük biçiminin suyu bol kuyu karşılığını da bağımsız bir seçenek olarak taşır.","gloss":"deniz ve geniş su","neighbor_only":"Komşu dal deniz yanında büyük ırmak ve farklı büyüklükte su alanlarına uzanan genel bir geniş su kapsamına sahiptir.","neighbor_ref":"root_000086/B001","relation_type":"near_synonym","shared_zone":"Odak dalın deniz karşılığı, komşu dalın geniş ve çok su çekirdeğiyle örtüşür."},{"boundary_match":"partial","distinction":"Odak dal suyu taşıyan kuyuyu niteler; komşu dal ise kuyudan dökülen suyu ve taşma sürecini merkez alır.","focus_only":"Odak dal kuyunun kendisini suyunun bol olması koşuluyla adlandırır.","gloss":"suyu bol kuyu ile kuyu suyu","neighbor_only":"Komşu dal kuyudaki kovadan dökülen veya havuza taşan suyu, kokusunu ve taşma olayını anlatır.","neighbor_ref":"root_001077/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuyu çevresinde suyun çokluğu ve görünür birikimiyle ilişkilidir."}],"source_phrase_ar":"العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)","source_summary":"Toplu tanıklık iki karşılığı yan yana verir: bir aktarım sözcüğü deniz olarak açıklar, öteki tanıklıklar ise suyu bol kuyu anlamını destekler. Kaynaklara özgü ayrı claim kimlikleri bulunmadığı için bu karşıtlık ortak özet içinde, atıf uydurulmadan korunur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء","what_is_not_ar":"ليس هو العالمين ولا العلم ولا العلامة ولا العيلم بمعنى آخر غير مائي"},"support_links":["sup_416da319492089188f91"]},{"boundary":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_kind":"bare","branch_ref":"root_001040/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"doğan veya atmaca türü yırtıcı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel kuş adını iki kaynak karşılığı arasındaki seçenekliliği koruyarak açıklamak için uygundur.","boundary_detail":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_image_ar":"طائر جارح يسمى العلام","concept_gloss":"doğan veya atmaca türü yırtıcı kuş","contextual_glosses":[{"applicability":"Kuş adından türemiş insan nitelemesinin kullanıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan oluşu ile çeviklik ve zekâ niteliklerini birlikte korur."},"facet_ids":["F002"],"text":"çevik ve zeki adam","usage_role":"contextual"}],"definition":"Doğan veya atmaca türünden bir yırtıcı kuş adıdır. Bu kuş adından türetilen bir niteleme, çevik ve zeki bir erkeği anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}],"identity_rationale":"Kaynak ifadesi temel adı doğan veya atmaca türünden yırtıcı kuş için verir ve geçici dal görüntüsünü doğrular. Çevik ve zeki erkek nitelemesi ise kuş adından türetilmiş ayrı bir biçimdir; kuşun tanımına doğrudan katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"doğan veya atmaca"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çevik ve zeki adam"}],"lexicalization_note":"Çıplak dal doğan veya atmaca türünden kuş adını tanımlar; insan nitelemesi türemiş bir sözcüksel uzantı olarak bağımlı tutulur.","neighbor_coverage_note":"Yırtıcı kuş sınıfında en yakın iki aday seçildi; diğer adaylar kanat çırpma, beslenme, farklı hayvan adları veya yalnızca uzak bir doğan ilişkisi taşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı kuş alanını paylaşsalar da komşu dal renk ve ara tür özellikleriyle daha dar bir kuşu adlandırır; odak dalın türemiş insan nitelemesi de komşuda yoktur.","focus_only":"Odak dal doğan veya atmaca karşılığı taşıyan kuş adını ve ondan türeyen insan nitelemesini içerir.","gloss":"yırtıcı kuş adları","neighbor_only":"Komşu dal mavi renkli, doğan ile atmaca arasında tanımlanan veya beyaz doğan sayılan daha özel bir kuş adıdır.","neighbor_ref":"root_000631/B002","relation_type":"same_field","shared_zone":"Her iki dal doğan ve atmaca çevresindeki avcı kuş adlandırmaları alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda zekâ kuştan türetilen insan niteliğinde belirginleşir; komşuda ise doğrudan belirli doğanların özelliğidir.","focus_only":"Odak dal doğan veya atmaca türünü genel bir adla karşılar ve bu addan insan nitelemesi türetir.","gloss":"doğan adı ile zeki doğan nitelemesi","neighbor_only":"Komşu dal özellikle zeki ve keskin bakışlı doğanlara verilen bir adı belirtir.","neighbor_ref":"root_001375/B006","relation_type":"near_neighbor","shared_zone":"İki dal doğan türünden yırtıcı kuşları adlandırır ve zekâ çağrışımını paylaşır."}],"source_phrase_ar":"العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık temel adı doğan veya atmaca türünden kuş için verir ve türemiş biçimi çevik, zeki erkek olarak açıklar."}],"source_summary":"Dal tek bir sözlük tanıklığında yırtıcı kuş adı ile bu addan türetilmiş çevik ve zeki erkek nitelemesini birlikte sunar.","sources":["TA"],"what_is_ar":"يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي","what_is_not_ar":"ليس هو العلام بمعنى الحناء ولا العلامة ولا العالم"},"support_links":[]},{"boundary":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001040/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","surface_ar":"تَعْلَمُ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","surface_ar":"عِلْمَ"}],"gloss":"erkek sırtlan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve erkek oluşunu birlikte veren bütün bağlamlarda tam karşılıktır.","boundary_detail":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_image_ar":"ذكر الضباع يسمى العيلام","concept_gloss":"erkek sırtlan","definition":"Erkek sırtlanı adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}],"identity_rationale":"Kaynak ifadesinin iki tanıklığı da sözcüğü doğrudan erkek sırtlan olarak açıklar. Geçici dal görüntüsü bu yalın hayvan adıyla tam uyumludur ve başka bir tür, özellik veya mecaz eklemeyi gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"erkek sırtlan"}],"lexicalization_note":"Tanım çıplak hayvan adını erkek sırtlanla sınırlar ve başka türlere ya da bağlı kuruluşlara genişletmez.","neighbor_coverage_note":"Erkek sırtlanı aynı sınırlarla adlandıran aday tam eş anlamlı olarak seçildi; diğer adaylar kurt, erkek domuz, aslan, kuş veya daha geniş hayvan sınıflarıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, hayvan türü ve cinsiyet sınırı aynıdır; ayrım yalnızca kullanılan sözlük biçimindedir.","focus_only":null,"gloss":"erkek sırtlan","neighbor_only":null,"neighbor_ref":"root_001068/B007","relation_type":"synonym","shared_zone":"Her iki dal da hiçbir ek koşul getirmeden erkek sırtlanı adlandırır."}],"source_phrase_ar":"العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)","source_summary":"Kaynaklar sözcüğün erkek sırtlanı adlandırdığı konusunda birleşir ve ek bir anlam ayrımı bildirmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العيلام بمعنى ذكر الضباع","what_is_not_ar":"ليس هو العيلم البئر الكثيرة الماء ولا العلامة ولا العلم"},"support_links":[]},{"boundary":"Dalın özü kesinleşmiş bilgidir; duyulanı hemen doğru sayma ve öldürmenin kesinliğini belirtme yalnızca belirli yapılara bağlı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001696/B001","candidate_links":[{"candidate_id":"cand_202c86c06aff5d745f62","lane":"micro"},{"candidate_id":"cand_f869eada5b348e9211ed","lane":"micro"},{"candidate_id":"cand_3c746652fe18d2b402c2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","surface_ar":"يَقِينِ"}],"gloss":"kuşkunun giderilmesiyle kesinleşen bilgi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşku giderilir ve ele alınan şeyin doğruluğu kesinleştirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlayış yatışır, yargı sabitlenir ve bilgi kuşkuya yer bırakmayacak biçimde yerleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çeşitli fiil biçimleri, bir şeyin doğruluğunu kesin olarak bilme veya bu kesinliğe ulaşma eylemini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Duyduğu her şeyi hiçbir kuşku duymadan doğru sayan kişi, belirli bir söz öbeğiyle nitelenir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Öldürme bağlamındaki belirli yapı, öldürme eyleminden çok o eylemin gerçekleştiğinin kesin olarak bilinmesini belirtir."}}],"root_ar":"ي ق ن","root_id":"root_001696","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın çıplak anlam çekirdeğini, hem kuşkunun kalkmasını hem de bilgi ile yargının sabitlenmesini birlikte anlatır.","boundary_detail":"Dalın özü kesinleşmiş bilgidir; duyulanı hemen doğru sayma ve öldürmenin kesinliğini belirtme yalnızca belirli yapılara bağlı kullanımlardır.","branch_image_ar":"ثبات العلم وزوال الشك","concept_gloss":"kuşkunun giderilmesiyle kesinleşen bilgi","contextual_glosses":[{"applicability":"Sonuç durumunun öne çıktığı ad kullanımlarında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuşkunun etkin biçimde giderilmesi ve doğruluğun araştırılarak belirlenmesi sürecini açıkça söylemez.","preserves":"Kuşkusuz ve sabit olma sonucunu korur."},"facet_ids":["F001","F002"],"text":"kesinlik","usage_role":"general"},{"applicability":"Fiil biçimlerinin bir şey hakkındaki kuşkunun kalkıp bilginin sabitlenmesini anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin kuşkuya yer bırakmadan doğrulanmasını ve sabitlenmesini korur."},"facet_ids":["F001","F002","F003"],"text":"kesin olarak bilmek","usage_role":"contextual"},{"applicability":"Konuşma dilinde kuşkunun sona ermesi öne çıkarıldığında uygun bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilginin ve yargının doğrulanıp sabitlenmesini açıkça belirtmez.","preserves":"Kuşkunun tümüyle ortadan kalkmasını korur."},"facet_ids":["F001"],"text":"kuşkusu kalmamak","usage_role":"contextual"},{"applicability":"Öldürme eyleminin gerçekleşip gerçekleşmediğine ilişkin kesinliğin anlatıldığı özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin kendisiyle, o eylemin gerçekleştiğine ilişkin kesin bilgiyi birbirinden ayırır."},"facet_ids":["F005"],"text":"gerçekleştiğini kesin olarak bilmek","usage_role":"explanatory"}],"definition":"Kuşkunun ortadan kalkmasıyla anlayışın yatışması, yargının sabitlenmesi ve bir şey hakkındaki bilginin değişmez biçimde kesinleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşku giderilir ve ele alınan şeyin doğruluğu kesinleştirilir."},{"facet_id":"F002","role":"core","statement":"Anlayış yatışır, yargı sabitlenir ve bilgi kuşkuya yer bırakmayacak biçimde yerleşir."},{"facet_id":"F003","role":"extension","statement":"Çeşitli fiil biçimleri, bir şeyin doğruluğunu kesin olarak bilme veya bu kesinliğe ulaşma eylemini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Duyduğu her şeyi hiçbir kuşku duymadan doğru sayan kişi, belirli bir söz öbeğiyle nitelenir."},{"facet_id":"F005","role":"associated_use","statement":"Öldürme bağlamındaki belirli yapı, öldürme eyleminden çok o eylemin gerçekleştiğinin kesin olarak bilinmesini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kesinlik düzeyi belirtilmeyen her türlü bilmeyi kapsar.","collision":"Sıradan veya değişebilir bilgiyle karışır.","fit":"broadening","loses":"Kuşkunun giderilmesini ve yargının değişmez biçimde sabitlenmesini belirtmez.","preserves":"Bir şeyin bilinmesi unsurunu korur."},"text":"bilgi"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, kuşkunun giderilmesiyle bilginin ve yargının değişmez biçimde yerleşmesidir. Verilen çerçeve bu çekirdeği doğru yansıtır; fiil biçimleri ile duyma ve öldürme bağlamlarındaki kullanımlar ise çekirdeğin ayrı gerçekleşmeleri olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kuşkunun kalkması ve bilginin kesinleşmesi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşkusuz ve sabit bilgi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kesin olarak bilmek; kuşkusu kalmamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin doğruluğunu kesin olarak bilmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kesin olarak bilme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kesinliğe varmak; kesin olarak bilmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyden kesin biçimde emin olmak; kuşkusu kalmamak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kesin olarak bilen, kuşkusu olmayan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kesin bilen; kendisine ulaşan haberi hemen doğru sayan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"duyduğu her şeyi kesin doğru sayan kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun hakkında hiçbir kuşkusu olmamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kesin bilen kimseyi bildiren küçültme biçimi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kesin bilgi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kesinliğin bilgi diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kesinliğin göz diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kesinliğin hakikat diye adlandırılan mertebesi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"öldürmenin gerçekleştiğini kesin olarak bilmek"}],"lexicalization_note":"Tanım çıplak anlam çekirdeğini verir; fiil biçimleri ve belirli söz öbekleri bu çekirdeğe bağlı ayrı yüzler olarak gösterilir ve bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kesinlik sınırını doğrudan aydınlatır, kalanlar ise yalnızca aynı bilgi alanında bulunur veya çekirdekle yeterli anlam örtüşmesi göstermez.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalda tereddüt sona erip bilgi sabitlenirken komşu dalda karşıt seçenekler dengede kalır ve kesin bir hükme ulaşılamaz.","focus_only":"Bilgi ve yargı sabitlenir, kuşku ortadan kalkar.","gloss":"kuşkunun karşıtı olan kesinlik","neighbor_only":"Karşıt olasılıklar arasında karar verilemez ve hüküm sabitlenmez.","neighbor_ref":"root_000812/B001","relation_type":"polarity_pair","shared_zone":"İki dal da bir yargının doğruluk bakımından ne ölçüde sabit olduğunu gösteren aynı eksende yer alır."},{"boundary_match":"partial","distinction":"Odak dal tam kuşkusuzluğu ve sabit bilgiyi gerektirir; komşu dal ise bir belirtiden doğan güçlü yargıyı da kapsadığı için daha düşük bir kesinlik düzeyine açık kalır.","focus_only":"Kuşkunun tümüyle giderilmesi ve bilginin sabitlenmesi için önceden bir belirtiye dayanma şartı yoktur.","gloss":"belirtiye dayalı güçlü yargı","neighbor_only":"Güçlü yargı, bir belirtiye dayanabilir ve tam kesinliğe ulaşmadan da kullanılabilir.","neighbor_ref":"root_000969/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi doğru sayan güçlü ve yerleşmiş bir bilişsel tutumu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalı ayıran ölçüt kuşkunun kalkmasıdır; komşu dalı ayıran ölçüt ise bilginin derinliği ve kişide kök salmasıdır.","focus_only":"Kuşkunun giderilerek belirli bir şeyin doğruluğunun kesinleşmesini öne çıkarır.","gloss":"kökleşmiş derin bilgi","neighbor_only":"Bilginin kişide derinleşip kökleşmesini ve güçlü bir bilgi birikimine dönüşmesini öne çıkarır.","neighbor_ref":"root_000561/B002","relation_type":"near_synonym","shared_zone":"İki dalda da bilgi geçici değildir ve bilen kişide sağlam biçimde yerleşmiştir."},{"boundary_match":"partial","distinction":"Derin kavrayış bir şeyi açıkça görme veya anlama yetisini anlatabilir; odak dal ise bunun ötesinde kuşkunun bitmiş ve hükmün sabitlenmiş olmasını şart koşar.","focus_only":"Belirli bir yargıda kuşkunun ortadan kalkmasını ve bilginin sabitlenmesini gerektirir.","gloss":"derin kavrayış ve içgörü","neighbor_only":"İçgörü, kanıttan ders çıkarma ve bir konuyu derinden kavrama gibi daha geniş bilişsel yetileri kapsar.","neighbor_ref":"root_000121/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal, yüzeysel sanının ötesine geçen doğrulayıcı bir kavrayışla ilişkilidir."}],"source_phrase_ar":"اليقن واليقين زوال الشك (maqayis)؛ اليقن اليقين وهو إزاحة الشك وتحقيق الأمر (ayn;tahdhib)؛ اليقين العلم وزوال الشك (sihah)؛ سكون الفهم مع ثبات الحكم (mufradat)؛ أيقن واستيقن وتيقن كله واحد (ayn;sihah;tahdhib)؛ رجل أذن يقن وهو الذي لا يسمع بشيء إلا أيقن به (tahdhib)؛ ما قتلوه يقينا أي ما قتلوه قتلا تيقنوه (mufradat)","source_summary":"Kaynakların birleşik anlatımı, kuşkunun giderilmesini, anlayışın yatışmasını ve yargıyla bilginin sabitlenmesini ortak çekirdek yapar. Aynı anlatım, kesin olarak bilme bildiren fiilleri ve kesinliğin duyma ya da öldürme bağlamında özel bir yapıyla dile getirildiği kullanımları da bu çekirdeğe bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اليقن واليقين؛ إزاحة الشك وتحقيق الأمر؛ العلم الثابت فوق المعرفة والدراية؛ أيقن واستيقن وتيقن؛ قتل تيقنه؛ أذن يقن يوقن بما يسمعه","what_is_not_ar":"الموقونة بمعنى الجارية المصونة المخدرة"},"support_links":["sup_416da319492089188f91","sup_5d57b721bad5d690c623","sup_c26b56eae4bddea714fc"]},{"boundary":"Anlam yalnızca örtünme veya saklanma eylemi değildir; koruma altında ve gözden uzak tutulan genç kadın kişisini belirtir.","branch_kind":"bare","branch_ref":"root_001696/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","surface_ar":"يَقِينِ"}],"gloss":"korunup gözden uzak tutulan genç kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim yapılan kişi genç bir kadındır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kişi koruma altında tutulur ve dışarıdan görülmeyecek biçimde gözden uzak yaşar."}}],"root_ar":"ي ق ن","root_id":"root_001696","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi, koruma altında bulunma ve dışarıdan görülmeme nitelikleriyle birlikte eksiksiz tanımlar.","boundary_detail":"Anlam yalnızca örtünme veya saklanma eylemi değildir; koruma altında ve gözden uzak tutulan genç kadın kişisini belirtir.","branch_image_ar":"صون الجارية وخدرها","concept_gloss":"korunup gözden uzak tutulan genç kadın","contextual_glosses":[{"applicability":"Koruma ile görünür olmama durumunun tek ve doğal bir nitelemeyle anlatılabildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korumanın fiziksel veya toplumsal kapsamını açıkça belirtmez.","preserves":"Genç kadının başkalarının gözünden uzak ve gözetilerek tutulmasını korur."},"facet_ids":["F001","F002"],"text":"gözlerden sakınılan genç kadın","usage_role":"contextual"}],"definition":"Koruma altında bulunan ve dışarıya çıkarılmayarak gözden uzak tutulan genç kadındır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim yapılan kişi genç bir kadındır."},{"facet_id":"F002","role":"core","statement":"Bu kişi koruma altında tutulur ve dışarıdan görülmeyecek biçimde gözden uzak yaşar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca giysiyle örtünmüş herhangi bir kadın anlamıyla karışır.","fit":"narrowing","loses":"Koruma altında tutulmayı, gözden uzak yaşamayı ve gençlik niteliğini belirtmez.","preserves":"Kadının dışarıdan görünmemesi yönünü kısmen korur."},"text":"örtülü kadın"}],"identity_rationale":"Kaynak ifadesi, korunan ve dışarıdan gözlenmeyecek biçimde ev içinde tutulan genç bir kadını doğrudan tanımlar. Verilen dal çerçevesi hem kişi türünü hem de koruma ile gözden uzak tutma niteliklerini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"koruma altında ve gözden uzak tutulan genç kadın"}],"lexicalization_note":"Tanım, tek başına kişi bildiren dalı kapsar; başka bir yapıya bağlı anlam veya genel bir örtme eylemi tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar kişi, saklılık, koruma ve örtü arasındaki sınırları gösterir, kalan adaylar ise yalnızca daha uzak örtme ya da kapatma durumlarını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda koruma ve dışarı çıkarmama birlikte kurucu niteliktedir; komşu dalda ise asıl ölçüt gizli bulunmadır ve koruma zorunlu değildir.","focus_only":"Genç kadının korunma amacıyla sürekli biçimde gözden uzak tutulmasını içerir.","gloss":"saklanan kadın","neighbor_only":"Bir kadının saklanması veya görünüp yeniden gizlenmesi, koruma altında bulunmadan da gerçekleşebilir.","neighbor_ref":"root_000384/B003","relation_type":"near_synonym","shared_zone":"İki dal da görünür alanda bulunmayan bir kadın kişisini anlatır."},{"boundary_match":"field_only","distinction":"Komşu dal genel bir örtme ve koruma alanıdır; odak dal ise bu işlemin sonucu sayılabilecek özel bir durumdaki belirli kişi türünü anlatır.","focus_only":"Örtme veya koruma işlemini değil, bu durumda tutulan genç kadın kişisini adlandırır.","gloss":"genel örtme ve koruma","neighbor_only":"Herhangi bir şeyi örten, kaplayan veya koruyan genel işlemi ve araçları kapsar.","neighbor_ref":"root_001096/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda dış etkiden koruma ve görünürlüğü azaltma düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Komşu dal yalnızca kişi türünü bildirir; odak dalda ise o kişinin koruma altında bulunması ve görünür alandan uzak tutulması anlamın ayrılmaz parçasıdır.","focus_only":"Genç kadını korunma ve gözden uzak tutulma durumuyla sınırlar.","gloss":"genç kadın","neighbor_only":"Genç kadın kişi türünü, korunma veya saklı yaşama şartı olmadan genel olarak belirtir.","neighbor_ref":"root_000240/B004","relation_type":"same_field","shared_zone":"Her iki dalın gönderimi genç kadın kişi alanındadır."},{"boundary_match":"thematic_only","distinction":"Yüzü örten nesne, kişinin bütünüyle gözden uzak tutulduğunu veya koruma altında bulunduğunu göstermez; odak dalın gönderimi de örtüye değil kişiyedir.","focus_only":"Bir giysi veya araç değil, korunup gözden uzak tutulan kişiyi belirtir.","gloss":"yüz örtüsü","neighbor_only":"Kadının yüzüne taktığı belirli örtüyü ve onu takma eylemini belirtir.","neighbor_ref":"root_001539/B012","relation_type":"thematic","shared_zone":"İki dal kadınların görünürlüğünü azaltma çevresinde aynı toplumsal durumda buluşabilir."}],"source_phrase_ar":"الموقونة الجارية المصونة المخدرة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu anlam, koruma altında ve gözden uzak tutulan genç kadın biçiminde tek kaynaktan aktarılır."}],"source_summary":"Dal, kişi türü ile onun içinde bulunduğu durumu tek bir anlamda birleştirir: genç kadın hem korunur hem de dışarıdan gözlenmeyecek biçimde gözden uzak tutulur.","sources":["TA"],"what_is_ar":"الموقونة بمعنى الجارية المصونة المخدرة","what_is_not_ar":"اليقين وزوال الشك وأفعال أيقن واستيقن وتيقن"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["102:5:1"],"branch_refs":[],"candidate_id":"cand_67f5437e313e61d09024","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:1:acoustic-deterrent-pressure","source_type":"word_analysis","support_ids":["sup_35a1b245755183edefce","sup_cf4a9d6602311ffb5b3d"],"title":"sound reinforces the halt","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:1","qac_refs":["102:5:1:1"],"status":"accepted"}},{"anchor_refs":["102:5:1"],"branch_refs":[],"candidate_id":"cand_f903a0459e0929cc1a21","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:1:deterrent-corrective-break","source_type":"word_analysis","support_ids":["sup_c53ef01813eb2f823ebd","sup_cf4a9d6602311ffb5b3d"],"title":"deterrent break opens correction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:1","qac_refs":["102:5:1:1"],"status":"accepted"}},{"anchor_refs":["102:5:1"],"branch_refs":[],"candidate_id":"cand_e23580c9b8a3d93b7435","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:1:opening-boundary-reset","source_type":"word_analysis","support_ids":["sup_54b5396e3628a62f2d36","sup_cf4a9d6602311ffb5b3d"],"title":"opening reset replaces sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:1","qac_refs":["102:5:1:1"],"status":"accepted"}},{"anchor_refs":["102:5:1"],"branch_refs":[],"candidate_id":"cand_6a3461995dd7a5e4e3cb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:1:third-refrain-pivot","source_type":"word_analysis","support_ids":["sup_547fce62357364be9927","sup_cf4a9d6602311ffb5b3d"],"title":"third refrain changes frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:1","qac_refs":["102:5:1:1"],"status":"accepted"}},{"anchor_refs":["102:5:2"],"branch_refs":[],"candidate_id":"cand_241fe156d79f56f5694a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:2:future-warning-to-condition","source_type":"word_analysis","support_ids":["sup_43a9500180a92a4a0469","sup_85370b7cb79fd1a832aa"],"title":"future warning becomes diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:2","qac_refs":["102:5:2:1"],"status":"accepted"}},{"anchor_refs":["102:5:2"],"branch_refs":[],"candidate_id":"cand_e9f0830f93ee8da4c529","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:2:imperfect-and-elided-answer","source_type":"word_analysis","support_ids":["sup_43a9500180a92a4a0469","sup_6c5a2aee2b8c8aa776c0"],"title":"marked tense and silence suspend the result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:2","qac_refs":["102:5:2:1"],"status":"accepted"}},{"anchor_refs":["102:5:2"],"branch_refs":[],"candidate_id":"cand_9e7eb46d594db9fdfc4d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:2:optative-lament","source_type":"word_analysis","support_ids":["sup_0a87be7c62aea8400c76","sup_43a9500180a92a4a0469"],"title":"condition carries if-only pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:2","qac_refs":["102:5:2:1"],"status":"accepted"}},{"anchor_refs":["102:5:2"],"branch_refs":[],"candidate_id":"cand_f5ae61882810ae89438b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:2:suspended-pacing-and-forward-pressure","source_type":"word_analysis","support_ids":["sup_43a9500180a92a4a0469","sup_c2fcd098a5a5ee137105"],"title":"brief particle suspends the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:2","qac_refs":["102:5:2:1"],"status":"accepted"}},{"anchor_refs":["102:5:2"],"branch_refs":[],"candidate_id":"cand_7605c5635340dc8fe6d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:5:2:unreal-conditional-scope","source_type":"word_analysis","support_ids":["sup_3ae2f15574f6d87a32d5","sup_43a9500180a92a4a0469"],"title":"unreal scope covers the knowledge phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:2","qac_refs":["102:5:2:1"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_2bf241e88e5750c72096","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:certainty-pair-narrows-knowing","source_type":"word_analysis","support_ids":["sup_83df0be46e1d73df232f","sup_a7199d10d26ae40f7b27"],"title":"certainty specializes knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_61e520daebc0658dacbb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:cognate-saturation","source_type":"word_analysis","support_ids":["sup_961656cd75a985915a66","sup_a7199d10d26ae40f7b27"],"title":"knowing receives its own measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_aaaa194402ae803dd15d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:direct-plural-address","source_type":"word_analysis","support_ids":["sup_5a383c7c5b4c6c782ce6","sup_a7199d10d26ae40f7b27"],"title":"plural addressees stay confronted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_ace85fcd47444d2afd14","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:form-i-direct-knowing","source_type":"word_analysis","support_ids":["sup_5fce24219a2905836384","sup_a7199d10d26ae40f7b27"],"title":"Form I keeps cognition direct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_6a0adbdd39d964c0dac7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:imperfect-open-ended-failure","source_type":"word_analysis","support_ids":["sup_9db8b0f8f7bf55805298","sup_a7199d10d26ae40f7b27"],"title":"imperfect keeps failure ongoing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_d9b2da36ac1d39fb6c06","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:knowledge-before-seeing","source_type":"word_analysis","support_ids":["sup_a7199d10d26ae40f7b27","sup_f72df6a03050f49f4683"],"title":"knowing precedes seeing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_195878a1f40f099c2083","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:local-root-cadence","source_type":"word_analysis","support_ids":["sup_5446e939a59fae558f9e","sup_a7199d10d26ae40f7b27"],"title":"same-root cadence makes grammar audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_c3bc2cf29c4fb79feaea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:mark-recognition-pressure","source_type":"word_analysis","support_ids":["sup_a7199d10d26ae40f7b27","sup_c033d1b707b9f7e5dbd5"],"title":"mark imagery sharpens recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_337ae9abe24eaf7ca86e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:repeated-verb-remodalized","source_type":"word_analysis","support_ids":["sup_23e69f168fc5073a9e2c","sup_a7199d10d26ae40f7b27"],"title":"same verb changes modality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_59e7f80e99eea4771079","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:verb-core-of-protasis","source_type":"word_analysis","support_ids":["sup_3efc0fc01e6b76fd0dab","sup_a7199d10d26ae40f7b27"],"title":"finite core gathers the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:3","qac_refs":["102:5:3:1","102:5:3:2"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_8234660eb7ae9d25ba7d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:accusative-role-compression","source_type":"word_analysis","support_ids":["sup_b86b71a2027b37578c13","sup_e425028876551e2b1876"],"title":"manner and known state compress","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_5ef616843753e6b7ff1f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:certainty-formula-family","source_type":"word_analysis","support_ids":["sup_5fd3e57665864d08760e","sup_e425028876551e2b1876"],"title":"construct family stages certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_83d0df4772df77eb09bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:certainty-rung-forward","source_type":"word_analysis","support_ids":["sup_74da61a20116f9f55330","sup_e425028876551e2b1876"],"title":"knowledge becomes the first certainty rung","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_a3e8180d2f7e585fc3bc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:construct-determination","source_type":"word_analysis","support_ids":["sup_7e5aef9d7b795f6161bf","sup_e425028876551e2b1876"],"title":"definite tail specifies the knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_e131f64a6ff2baa1e096","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:dual-grammar-hinge","source_type":"word_analysis","support_ids":["sup_a8a091c1098e43284b6d","sup_e425028876551e2b1876"],"title":"one noun binds backward and forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_644d173ff8ac1eeba56d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:knowledge-certainty-fusion","source_type":"word_analysis","support_ids":["sup_079ba014aabdc91c9666","sup_e425028876551e2b1876"],"title":"knowledge and certainty fuse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_7443fc62af3382871c2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:mark-recognition-noun-pressure","source_type":"word_analysis","support_ids":["sup_733307826f6c89b323c8","sup_e425028876551e2b1876"],"title":"knowledge carries recognition pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_2f3048b68ba5a06d18a2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:masdar-reifies-knowing","source_type":"word_analysis","support_ids":["sup_a5298818b750c40cb2ab","sup_e425028876551e2b1876"],"title":"maṣdar lets knowing be qualified","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_96959a19c10276fb768a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:prior-objectlessness-specified","source_type":"word_analysis","support_ids":["sup_162cfa8be56a8763aea2","sup_e425028876551e2b1876"],"title":"open knowing receives quality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_6089c6848f7c6b2a8dce","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:rare-certainty-construction","source_type":"word_analysis","support_ids":["sup_c417a5fee4bd1d759184","sup_e425028876551e2b1876"],"title":"ordinary knowledge enters a rare frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:4"],"branch_refs":[],"candidate_id":"cand_ae7ae4cdb0c9625e37dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:4:root-cadence-into-certainty","source_type":"word_analysis","support_ids":["sup_b3b464ba06a7d84717f5","sup_e425028876551e2b1876"],"title":"cadence moves from knowing to certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:4","qac_refs":["102:5:4:1"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_dd19c699f4770c955ef7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:certainty-against-denial","source_type":"word_analysis","support_ids":["sup_0041b72755d17ae8aff5","sup_1a66fb7a1a09396fb5cd"],"title":"denied certainty elsewhere is required here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_9dedf4f80e0a1c597024","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:certainty-controls-grade","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_8cfc5fef0a9b0d19a72d"],"title":"certainty grades the knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_2bc1e22b192d69278a09","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:certainty-formula-family","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_f0e8985ba296afa0c14e"],"title":"certainty joins construct formulas","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_63d6375f4a5ffb82baad","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:closing-weight","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_e920fe489618ba685fe6"],"title":"certainty closes the ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_cc8c9fcf765bd5e80914","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:death-certainty-resonance","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_68cfd00f2d438a55d6a4"],"title":"death resonance presses from the graves","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_7c4d62b8ce625768236b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:definite-genitive-qualifier","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_6ae32ad7d4bf10dbe734"],"title":"definite certainty qualifies knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_6ff3d7bee772987fd773","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:forward-certainty-tail","source_type":"word_analysis","support_ids":["sup_13505262d2b132fb15ff","sup_1a66fb7a1a09396fb5cd"],"title":"stable tail returns in seeing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_6badf3050c2a19d8f4a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:rare-certainty-crowns-knowledge","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_75190be7782d87424017"],"title":"rare certainty crowns common knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_e237b6c6277fbcfde33c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:retroactive-coloring","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_bb7abfbc3ad8d138e153"],"title":"certainty rereads prior knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_4a71582b820eab4c79fd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:sound-and-liaison-closure","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_a65de3d98f59ab1c47d2"],"title":"sound binds the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_7bd73874d0e45ebd08c8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:verified-certainty-family","source_type":"word_analysis","support_ids":["sup_1a66fb7a1a09396fb5cd","sup_8b2952eb2cb1ae494629"],"title":"certainty is verified, not mood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:5:5","qac_refs":["102:5:5:1","102:5:5:2"],"status":"accepted"}},{"anchor_refs":["102:5:3"],"branch_refs":[],"candidate_id":"cand_5af41d06dfba5e7860d7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"102:5:3:1","source_type":"qac_morpheme","support_ids":["sup_380be0b2c54f1611302c"],"title":"QAC root occurrence: ع ل م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:5:5"],"branch_refs":[],"candidate_id":"cand_f39cbe50da1c8b3ab26f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001696"],"scope":"focus_ayah","source_local_id":"102:5:5:2","source_type":"qac_morpheme","support_ids":["sup_a08fc5bdea00b7326324"],"title":"QAC root occurrence: ي ق ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B001","root_001696/B001"],"candidate_id":"cand_202c86c06aff5d745f62","commentary_obligation":"review","hft_ref":"hft_2cdd108d18ce6f6469fa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_disclosure_threshold","source_type":"hft","support_ids":["sup_5d57b721bad5d690c623"],"title":"b_disclosure_threshold","trust":"legacy_unbound"},{"anchor_refs":["102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B002","root_001696/B001"],"candidate_id":"cand_f869eada5b348e9211ed","commentary_obligation":"review","hft_ref":"hft_a2a27a6d5ca607eda9b1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_landmark_certainty","source_type":"hft","support_ids":["sup_c26b56eae4bddea714fc"],"title":"b_landmark_certainty","trust":"legacy_unbound"},{"anchor_refs":["102:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:5","branch_refs":["root_001040/B005","root_001696/B001"],"candidate_id":"cand_3c746652fe18d2b402c2","commentary_obligation":"review","hft_ref":"hft_b97d04a400b47f8a12d7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_reservoir_certainty","source_type":"hft","support_ids":["sup_416da319492089188f91"],"title":"b_reservoir_certainty","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"102:5:1:1","qac_word_ref":"102:5:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"لَو","morph_features":"STEM|POS:COND|LEM:law","morpheme_role":"STEM","pos":"COND","qac_ref":"102:5:2:1","qac_word_ref":"102:5:2","root_ar":"","surface_ar":"لَوْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","root_ar":"ع ل م","surface_ar":"تَعْلَمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:5:3:2","qac_word_ref":"102:5:3","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","root_ar":"ع ل م","surface_ar":"عِلْمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:5:5:1","qac_word_ref":"102:5:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","root_ar":"ي ق ن","surface_ar":"يَقِينِ"}],"word_analysis_qac_refs":[["102:5:1:1"],["102:5:2:1"],["102:5:3:1","102:5:3:2"],["102:5:4:1"],["102:5:5:1","102:5:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["102:5:1","102:5:2","102:5:3","102:5:4","102:5:5"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"102:5:1:1","qac_word_ref":"102:5:1","root_ar":"","surface_ar":"كَلَّا"},{"lemma_ar":"لَو","morph_features":"STEM|POS:COND|LEM:law","morpheme_role":"STEM","pos":"COND","qac_ref":"102:5:2:1","qac_word_ref":"102:5:2","root_ar":"","surface_ar":"لَوْ"},{"lemma_ar":"عَلِمَ","morph_features":"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:5:3:1","qac_word_ref":"102:5:3","root_ar":"ع ل م","surface_ar":"تَعْلَمُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:5:3:2","qac_word_ref":"102:5:3","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عِلْم","morph_features":"STEM|POS:N|LEM:Eilom|ROOT:Elm|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:4:1","qac_word_ref":"102:5:4","root_ar":"ع ل م","surface_ar":"عِلْمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:5:5:1","qac_word_ref":"102:5:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَقِين","morph_features":"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"102:5:5:2","qac_word_ref":"102:5:5","root_ar":"ي ق ن","surface_ar":"يَقِينِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["102:5:1:1"],["102:5:2:1"],["102:5:3:1","102:5:3:2"],["102:5:4:1"],["102:5:5:1","102:5:5:2"]],"word_analysis_refs":["102:5:1","102:5:2","102:5:3","102:5:4","102:5:5"],"word_rows":[{"analysis_record_ref":"102:5:1","analytic_gloss_range_en":"deterrent and corrective discourse particle that halts the preceding heedless movement and opens a new conditional frame","analytic_root_gloss_range_en":null,"qac_refs":["102:5:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَلَّا","transliteration":"kallā"}},{"analysis_record_ref":"102:5:2","analytic_gloss_range_en":"counterfactual conditional particle with optative pressure and an omitted answer","analytic_root_gloss_range_en":null,"qac_refs":["102:5:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَوْ","transliteration":"law"}},{"analysis_record_ref":"102:5:3","analytic_gloss_range_en":"second-person plural imperfect knowing, remodalized by the counterfactual particle and specified by a cognate accusative","analytic_root_gloss_range_en":"knowledge, recognition, and marking/sign branches; local sense is knowing or recognizing, with sign/mark imagery only as a narrowed root-family pressure","qac_refs":["102:5:3:1","102:5:3:2"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"تَعْلَمُونَ","transliteration":"taʿlamūna"}},{"analysis_record_ref":"102:5:4","analytic_gloss_range_en":"accusative maṣdar functioning as cognate measure of knowing and construct head qualified by certainty","analytic_root_gloss_range_en":"knowledge, recognition, and sign/mark branches; the local noun selects knowledge while mark imagery may color recognition only secondarily","qac_refs":["102:5:4:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"عِلْمَ","transliteration":"ʿilma"}},{"analysis_record_ref":"102:5:5","analytic_gloss_range_en":"definite genitive certainty that qualifies the knowledge phrase and closes the ayah","analytic_root_gloss_range_en":"settled knowledge with doubt removed; death resonance is possible as a narrowed lexical pressure in this surah because of 102:2, while unrelated nominal branches are inactive","qac_refs":["102:5:5:1","102:5:5:2"],"root":{"arabic":"ي ق ن","transliteration":"y-q-n"},"surface":{"arabic":"ٱلْيَقِينِ","transliteration":"al-yaqīn"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["102:5"],"branch_refs":["root_001040/B001","root_001696/B001"],"candidate_id":"cand_202c86c06aff5d745f62","evidence_scope":"focus_ayah","hft_ref":"hft_2cdd108d18ce6f6469fa","item_id":"b_disclosure_threshold","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_disclosure_threshold","support_id":"sup_5d57b721bad5d690c623"},{"anchor_refs":["102:5"],"branch_refs":["root_001040/B002","root_001696/B001"],"candidate_id":"cand_f869eada5b348e9211ed","evidence_scope":"focus_ayah","hft_ref":"hft_a2a27a6d5ca607eda9b1","item_id":"b_landmark_certainty","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_landmark_certainty","support_id":"sup_c26b56eae4bddea714fc"},{"anchor_refs":["102:5"],"branch_refs":["root_001040/B005","root_001696/B001"],"candidate_id":"cand_3c746652fe18d2b402c2","evidence_scope":"focus_ayah","hft_ref":"hft_b97d04a400b47f8a12d7","item_id":"b_reservoir_certainty","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_reservoir_certainty","support_id":"sup_416da319492089188f91"}],"diagnostics":[],"lane_counts":{"global":9,"macro":10,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"102:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"102:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"102:5","lane":"micro","linguistic_source_ref":"102:5","surface_ref":"102:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"102:5","target_tokens":[["Hayır",["102:5:1"]],["Kesin",["102:5:4","102:5:5"]],["olarak",["102:5:4","102:5:5"]],["bilseydiniz",["102:5:2","102:5:3"]]],"text":"Hayır! Kesin olarak bilseydiniz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s102-p01-001-008","label":"Whole surah","number":1,"refs":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:certainty-against-denial","source_type":"word_analysis","support_id":"sup_0041b72755d17ae8aff5","text":"{\"blocking_evidence\":null,\"headline\":\"denied certainty elsewhere is required here\",\"reader_payoff\":\"The reader notices that where 4:157 denies certainty in a disputed claim, 102:5 makes certainty the required qualifier of knowledge.\",\"reason\":\"The CRITICAL row gives the concrete contrast at 4:157, and the local phrase positively requires {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) as qualifier.\",\"representative_source_ids\":[\"QI-614d8705\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:knowledge-certainty-fusion","source_type":"word_analysis","support_id":"sup_079ba014aabdc91c9666","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge and certainty fuse\",\"reader_payoff\":\"The reader notices that the phrase fuses knowledge and certainty in 102:5, the opposite pressure from the denied knowledge and certainty in 4:157.\",\"reason\":\"The local construct binds {{ar:عِلْمَ}} ({{tr:ʿilma}}) to {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}), and the inter-ayah contrast is concrete at 4:157.\",\"representative_source_ids\":[\"QI-57c666ba\",\"QI-a8a7dc5e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2:optative-lament","source_type":"word_analysis","support_id":"sup_0a87be7c62aea8400c76","text":"{\"blocking_evidence\":null,\"headline\":\"condition carries if-only pressure\",\"reader_payoff\":\"The reader notices that the particle does more than pose a logical condition; it registers the ache of a missing certainty.\",\"reason\":\"The optative reading survives as tone because it complements, rather than replaces, the counterfactual force of {{ar:لَوْ}} ({{tr:law}}).\",\"representative_source_ids\":[\"QS-80993e45\",\"QI-4891410a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:forward-certainty-tail","source_type":"word_analysis","support_id":"sup_13505262d2b132fb15ff","text":"{\"blocking_evidence\":null,\"headline\":\"stable tail returns in seeing\",\"reader_payoff\":\"The reader notices that certainty is the stable tail carried from knowledge in 102:5 into seeing in 102:7.\",\"reason\":\"The CRITICAL rows give the concrete same-surah reprise of {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) in {{ar:عَيْنَ ٱلْيَقِينِ}} ({{tr:ʿayna al-yaqīn}}) at 102:7.\",\"representative_source_ids\":[\"QE-5c394ca4\",\"QE-ed791b46\",\"QB-2903ba3a\",\"QY-70e0e716\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:prior-objectlessness-specified","source_type":"word_analysis","support_id":"sup_162cfa8be56a8763aea2","text":"{\"blocking_evidence\":null,\"headline\":\"open knowing receives quality\",\"reader_payoff\":\"The reader notices that the previously open warning about knowing is now specified by a certainty-grade phrase.\",\"reason\":\"The local phrase supplies the cognate accusative quality after earlier same-surah warning formulas that left the known content unstated.\",\"representative_source_ids\":[\"QB-671f54b6\",\"QB-ac52f464\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5","source_type":"word_analysis","support_id":"sup_1a66fb7a1a09396fb5cd","text":"{\"gloss_range\":\"definite genitive certainty that qualifies the knowledge phrase and closes the ayah\",\"prose\":\"{{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) is genitive because it depends on the preceding knowledge noun, but semantically it governs the grade of the whole phrase. Its definiteness makes certainty identifiable rather than indefinite confidence, and its final position lets the ayah land on the standard of doubtless knowing rather than on the verb alone. The root's main local branch is settled, verified knowledge with doubt removed; its relative rarity lets this certainty term crown the common knowledge field, and it stands opposite the denied certainty of 4:157. The death sense can press in only as resonance after the graves of 102:2, not as a replacement for epistemic certainty. In recitation, liaison across the construct can make the phrase feel continuous, and the final sound answers the surrounding knowing endings. The same tail returns in the later seeing formula in 102:7 and belongs with the truth-of-certainty formulas in 56:95 and 69:51, so certainty is both the endpoint of this ayah, the anchor of that later formula, and the word that rereads the prior knowing warnings as more than information.\",\"root_display\":\"{{ar:ي ق ن}} ({{tr:y-q-n}})\",\"root_gloss_range\":\"settled knowledge with doubt removed; death resonance is possible as a narrowed lexical pressure in this surah because of 102:2, while unrelated nominal branches are inactive\",\"surface_display\":\"{{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:repeated-verb-remodalized","source_type":"word_analysis","support_id":"sup_23e69f168fc5073a9e2c","text":"{\"blocking_evidence\":null,\"headline\":\"same verb changes modality\",\"reader_payoff\":\"The reader notices that repetition does not mean sameness: the warning verb of 102:3-4 becomes a counterfactual diagnosis in 102:5.\",\"reason\":\"Attachment evidence makes {{ar:لَوْ}} ({{tr:law}}) the governor of {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}), supporting the modal shift in the repeated same-surah verb.\",\"representative_source_ids\":[\"QG-a5f738c0\",\"QI-167cb006\",\"MI-3832f1b4\",\"QE-9366d394\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:1:acoustic-deterrent-pressure","source_type":"word_analysis","support_id":"sup_35a1b245755183edefce","text":"{\"blocking_evidence\":null,\"headline\":\"sound reinforces the halt\",\"reader_payoff\":\"The reader notices that the compact sound shape can make the refusal feel like a held stop before the conditional opens.\",\"reason\":\"The phonetic claim is useful as recitational texture, but it is kept secondary to the particle's syntactic and discourse function.\",\"representative_source_ids\":[\"QP-0f463490\",\"QP-9b393cb7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"102:5:3:1","source_type":"qac_morpheme","support_id":"sup_380be0b2c54f1611302c","text":"{\"lemma_ar\":\"عَلِمَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:Ealima|ROOT:Elm|2MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"102:5:3:1\",\"qac_word_ref\":\"102:5:3\",\"root_ar\":\"ع ل م\",\"surface_ar\":\"تَعْلَمُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2:unreal-conditional-scope","source_type":"word_analysis","support_id":"sup_3ae2f15574f6d87a32d5","text":"{\"blocking_evidence\":null,\"headline\":\"unreal scope covers the knowledge phrase\",\"reader_payoff\":\"The reader notices that the knowledge of certainty is framed as absent and unrealized, not as a present possession.\",\"reason\":\"QAC and attachment evidence identify {{ar:لَوْ}} ({{tr:law}}) as opening a counterfactual subordinate clause spanning through {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}).\",\"representative_source_ids\":[\"QG-3d7005d4\",\"QT-b446e2b7\",\"QB-044ca82b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:verb-core-of-protasis","source_type":"word_analysis","support_id":"sup_3efc0fc01e6b76fd0dab","text":"{\"blocking_evidence\":null,\"headline\":\"finite core gathers the clause\",\"reader_payoff\":\"The reader notices that this verb is the finite center around which the particle, subject ending, and certainty phrase gather.\",\"reason\":\"Attachment evidence makes the clause headed by {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}) the complement governed by {{ar:لَوْ}} ({{tr:law}}).\",\"representative_source_ids\":[\"QI-23df9965\",\"QT-cefd68d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2","source_type":"word_analysis","support_id":"sup_43a9500180a92a4a0469","text":"{\"gloss_range\":\"counterfactual conditional particle with optative pressure and an omitted answer\",\"prose\":\"{{ar:لَوْ}} ({{tr:law}}) sets the whole span {{ar:تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ}} ({{tr:taʿlamūna ʿilma al-yaqīn}}) inside an unreal condition. The word therefore prevents the knowledge phrase from sounding achieved: the line means not that the addressees possess certainty, but that such knowledge is missing. Its optative shade makes the condition feel like an 'if only,' while the omitted answer after the phrase keeps the consequence compressed. Because the particle is so brief before the long knowledge phrase, it creates a suspended beat; the withheld result then leaves room for the next movement to turn toward seeing in 102:6-7.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَوْ}} ({{tr:law}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:local-root-cadence","source_type":"word_analysis","support_id":"sup_5446e939a59fae558f9e","text":"{\"blocking_evidence\":null,\"headline\":\"same-root cadence makes grammar audible\",\"reader_payoff\":\"The reader notices the adjacent root echo between the verb and verbal noun before analyzing it as a cognate accusative.\",\"reason\":\"The echo is real because {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}) and {{ar:عِلْمَ}} ({{tr:ʿilma}}) share the root, but the payoff is kept tied to the licensed cognate construction.\",\"representative_source_ids\":[\"QE-a1da920b\",\"QP-e4d908fd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:1:third-refrain-pivot","source_type":"word_analysis","support_id":"sup_547fce62357364be9927","text":"{\"blocking_evidence\":null,\"headline\":\"third refrain changes frame\",\"reader_payoff\":\"The reader notices that the repeated halt-word is not simple repetition; in 102:5 it turns the earlier future warning into an unrealized knowledge condition.\",\"reason\":\"The CRITICAL rows give concrete same-surah references, and the guardrail evidence confirms that {{ar:لَوْ}} ({{tr:law}}) governs the following conditional clause with no overt answer.\",\"representative_source_ids\":[\"MG-86255ea2\",\"QT-8c637789\",\"QE-f0049f10\",\"QB-0a68bb92\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:1:opening-boundary-reset","source_type":"word_analysis","support_id":"sup_54b5396e3628a62f2d36","text":"{\"blocking_evidence\":null,\"headline\":\"opening reset replaces sequence\",\"reader_payoff\":\"The reader notices that 102:5 begins as an abrupt rhetorical boundary, not as a smooth sequential continuation from 102:4.\",\"reason\":\"The ayah opens directly with {{ar:كَلَّا}} ({{tr:kallā}}), while the prior boundary in 102:4 used sequential framing; nothing in the guardrails contradicts the boundary contrast.\",\"representative_source_ids\":[\"QT-10a35362\",\"QT-7db48e5d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:direct-plural-address","source_type":"word_analysis","support_id":"sup_5a383c7c5b4c6c782ce6","text":"{\"blocking_evidence\":null,\"headline\":\"plural addressees stay confronted\",\"reader_payoff\":\"The reader notices that the audience is not renamed or distanced; the same second-person plural group remains encoded inside the verb.\",\"reason\":\"QAC marks the verb as second masculine plural, and attachment evidence identifies the subject as implicit in the agreement.\",\"representative_source_ids\":[\"QG-de3cb90d\",\"QF-fe35959f\",\"QB-d91a8869\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:form-i-direct-knowing","source_type":"word_analysis","support_id":"sup_5fce24219a2905836384","text":"{\"blocking_evidence\":null,\"headline\":\"Form I keeps cognition direct\",\"reader_payoff\":\"The reader notices that the form targets the addressees' own knowing rather than a scene of teaching or informing someone else.\",\"reason\":\"QAC identifies the local word as Form I imperfect, so causative teaching/informing branches are not the local grammatical selection.\",\"representative_source_ids\":[\"QF-1fb44655\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:certainty-formula-family","source_type":"word_analysis","support_id":"sup_5fd3e57665864d08760e","text":"{\"blocking_evidence\":null,\"headline\":\"construct family stages certainty\",\"reader_payoff\":\"The reader notices that this construct sits beside other certainty formulas, including {{ar:حَقَّ ٱلْيَقِينِ}} ({{tr:ḥaqqa al-yaqīn}}) in 56:95 and 69:51.\",\"reason\":\"The CRITICAL row gives concrete phrase-family references, and the local phrase is syntactically the same kind of construct with {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}).\",\"representative_source_ids\":[\"QE-40e861c2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:death-certainty-resonance","source_type":"word_analysis","support_id":"sup_68cfd00f2d438a55d6a4","text":"{\"blocking_evidence\":null,\"headline\":\"death resonance presses from the graves\",\"reader_payoff\":\"The reader notices that the earlier graves in 102:2 can make certainty feel like the unavoidable certainty of death, while the local phrase still means doubtless knowledge.\",\"reason\":\"The local grammar and V4 main branch keep {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) epistemic, so the death sense is retained only as a contextual resonance after 102:2.\",\"representative_source_ids\":[\"QS-503047c9\",\"MS-405f0008\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:definite-genitive-qualifier","source_type":"word_analysis","support_id":"sup_6ae32ad7d4bf10dbe734","text":"{\"blocking_evidence\":null,\"headline\":\"definite certainty qualifies knowledge\",\"reader_payoff\":\"The reader notices that certainty is a definite genitive qualifier inside the phrase, not a loose abstract noun after it.\",\"reason\":\"QAC marks {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) as definite genitive, and attachment evidence makes it the genitive dependent of {{ar:عِلْمَ}} ({{tr:ʿilma}}).\",\"representative_source_ids\":[\"QG-25b296a9\",\"QG-c63ae734\",\"QF-653df7d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2:imperfect-and-elided-answer","source_type":"word_analysis","support_id":"sup_6c5a2aee2b8c8aa776c0","text":"{\"blocking_evidence\":null,\"headline\":\"marked tense and silence suspend the result\",\"reader_payoff\":\"The reader notices that the imperfect verb after {{ar:لَوْ}} ({{tr:law}}) keeps the failed knowing open-ended, and the missing answer makes the consequence felt rather than stated.\",\"reason\":\"The bundle explicitly notes an imperfect after {{ar:لَوْ}} ({{tr:law}}) and a strongly licensed omitted apodosis; broader temporal claims are kept as open-ended pressure rather than a fixed doctrine.\",\"representative_source_ids\":[\"MG-9d25df4a\",\"QT-8bcc9382\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:mark-recognition-noun-pressure","source_type":"word_analysis","support_id":"sup_733307826f6c89b323c8","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge carries recognition pressure\",\"reader_payoff\":\"The reader notices that the noun can feel like recognition of marked reality, while the selected local sense remains knowledge.\",\"reason\":\"V4 supports both knowledge and sign/mark branches for {{ar:ع ل م}} ({{tr:ʿ-l-m}}), but the local maṣdar in this construct selects the knowledge branch.\",\"representative_source_ids\":[\"QS-6f86dbb4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:certainty-rung-forward","source_type":"word_analysis","support_id":"sup_74da61a20116f9f55330","text":"{\"blocking_evidence\":null,\"headline\":\"knowledge becomes the first certainty rung\",\"reader_payoff\":\"The reader notices that 102:5 names certainty as knowledge before 102:7 names it as seeing.\",\"reason\":\"CRITICAL rows provide the concrete same-surah link between {{ar:عِلْمَ ٱلْيَقِينِ}} ({{tr:ʿilma al-yaqīn}}) in 102:5 and {{ar:عَيْنَ ٱلْيَقِينِ}} ({{tr:ʿayna al-yaqīn}}) in 102:7.\",\"representative_source_ids\":[\"QT-8416d458\",\"MT-7dff9a74\",\"QE-3c16c6e6\",\"QY-2c6f0552\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:rare-certainty-crowns-knowledge","source_type":"word_analysis","support_id":"sup_75190be7782d87424017","text":"{\"blocking_evidence\":null,\"headline\":\"rare certainty crowns common knowledge\",\"reader_payoff\":\"The reader notices that the rarer certainty root closes over the more common knowledge field, making the phrase specialized and weighty.\",\"reason\":\"The contextual profiles show few {{ar:ي ق ن}} ({{tr:y-q-n}}) gerund instances compared with the broad {{ar:ع ل م}} ({{tr:ʿ-l-m}}) field, and the local construct binds them.\",\"representative_source_ids\":[\"QI-dcea58a6\",\"QI-e854ccd0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:construct-determination","source_type":"word_analysis","support_id":"sup_7e5aef9d7b795f6161bf","text":"{\"blocking_evidence\":null,\"headline\":\"definite tail specifies the knowledge\",\"reader_payoff\":\"The reader notices that the knowledge is not generic; the definite certainty noun fixes it as a specific certainty-grade knowing.\",\"reason\":\"QAC marks {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) as definite genitive and attachment evidence makes it the genitive dependent of {{ar:عِلْمَ}} ({{tr:ʿilma}}).\",\"representative_source_ids\":[\"QG-20cfe700\",\"QG-24691e7b\",\"QS-91346797\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:certainty-pair-narrows-knowing","source_type":"word_analysis","support_id":"sup_83df0be46e1d73df232f","text":"{\"blocking_evidence\":null,\"headline\":\"certainty specializes knowing\",\"reader_payoff\":\"The reader notices that common knowing vocabulary is tightened by the rarer certainty field, excluding weaker awareness or conjecture.\",\"reason\":\"The local phrase binds {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}) to {{ar:عِلْمَ ٱلْيَقِينِ}} ({{tr:ʿilma al-yaqīn}}), while V4 confirms the active knowledge branch for {{ar:ع ل م}} ({{tr:ʿ-l-m}}).\",\"representative_source_ids\":[\"QS-846e65ba\",\"QI-5b6f0528\",\"QI-a7113b2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2:future-warning-to-condition","source_type":"word_analysis","support_id":"sup_85370b7cb79fd1a832aa","text":"{\"blocking_evidence\":null,\"headline\":\"future warning becomes diagnosis\",\"reader_payoff\":\"The reader notices the same knowing language has moved from future inevitability in 102:3-4 into a present unreal condition in 102:5.\",\"reason\":\"The cross-ayah CRITICAL rows give the 102:3-4 contrast, and local syntax confirms that {{ar:لَوْ}} ({{tr:law}}) governs the repeated knowing verb here.\",\"representative_source_ids\":[\"QT-5232bf63\",\"QB-de779b91\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:verified-certainty-family","source_type":"word_analysis","support_id":"sup_8b2952eb2cb1ae494629","text":"{\"blocking_evidence\":null,\"headline\":\"certainty is verified, not mood\",\"reader_payoff\":\"The reader notices that certainty functions as a settled quality of knowing, not as a separate action or a passing psychological confidence.\",\"reason\":\"QAC identifies a nominal gerund, and V4 supports the root's settled-knowledge and verification field.\",\"representative_source_ids\":[\"QS-e6a6ea72\",\"QF-63594dc2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:certainty-controls-grade","source_type":"word_analysis","support_id":"sup_8cfc5fef0a9b0d19a72d","text":"{\"blocking_evidence\":null,\"headline\":\"certainty grades the knowing\",\"reader_payoff\":\"The reader notices that certainty is not being acted upon; it sets the standard by which the demanded knowing is judged.\",\"reason\":\"The local construct makes {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}) the qualifier of {{ar:عِلْمَ}} ({{tr:ʿilma}}), and V4 supports the settled-knowledge branch for {{ar:ي ق ن}} ({{tr:y-q-n}}).\",\"representative_source_ids\":[\"QG-f866c4bf\",\"QS-287414b9\",\"QS-2d87827c\",\"QT-fa2b32d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:cognate-saturation","source_type":"word_analysis","support_id":"sup_961656cd75a985915a66","text":"{\"blocking_evidence\":null,\"headline\":\"knowing receives its own measure\",\"reader_payoff\":\"The reader notices that the verb is immediately measured by its own verbal noun, turning open-ended knowing into an intensified certainty-grade demand.\",\"reason\":\"Attachment evidence strongly licenses {{ar:عِلْمَ ٱلْيَقِينِ}} ({{tr:ʿilma al-yaqīn}}) as an accusative maṣdar expression qualifying {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}).\",\"representative_source_ids\":[\"QG-d49416f7\",\"MG-637af691\",\"QE-da902447\",\"QB-319e1dd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:imperfect-open-ended-failure","source_type":"word_analysis","support_id":"sup_9db8b0f8f7bf55805298","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect keeps failure ongoing\",\"reader_payoff\":\"The reader notices that the failed knowing is not locked into a simple past counterfactual; it is left as an ongoing unreal state.\",\"reason\":\"The prompt bundle notes the marked imperfect after {{ar:لَوْ}} ({{tr:law}}); the topic is narrowed to aspectual pressure without overstating a single temporal solution.\",\"representative_source_ids\":[\"QG-feada07a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"102:5:5:2","source_type":"qac_morpheme","support_id":"sup_a08fc5bdea00b7326324","text":"{\"lemma_ar\":\"يَقِين\",\"morph_features\":\"STEM|POS:N|LEM:yaqiyn|ROOT:yqn|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"102:5:5:2\",\"qac_word_ref\":\"102:5:5\",\"root_ar\":\"ي ق ن\",\"surface_ar\":\"يَقِينِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:masdar-reifies-knowing","source_type":"word_analysis","support_id":"sup_a5298818b750c40cb2ab","text":"{\"blocking_evidence\":null,\"headline\":\"maṣdar lets knowing be qualified\",\"reader_payoff\":\"The reader notices that the verbal noun turns knowing into a compact noun that can receive certainty as its qualifier.\",\"reason\":\"QAC identifies {{ar:عِلْمَ}} ({{tr:ʿilma}}) as a verbal noun, singular accusative and construct head, matching the CRITICAL form-specific payoff.\",\"representative_source_ids\":[\"QF-52f46572\",\"QF-890f13c6\",\"QT-9ff02fa0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:sound-and-liaison-closure","source_type":"word_analysis","support_id":"sup_a65de3d98f59ab1c47d2","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds the phrase\",\"reader_payoff\":\"The reader notices that recitation can bind the construct into one continuous phrase and make the final certainty sound echo the surah's knowing endings.\",\"reason\":\"The liaison and sound claims are recitational texture, while the syntactic dependency is independently licensed by the {{ar:إِضَافَة}} ({{tr:iḍāfa}}) attachment.\",\"representative_source_ids\":[\"QP-10e4651f\",\"QP-7acb4bc6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3","source_type":"word_analysis","support_id":"sup_a7199d10d26ae40f7b27","text":"{\"gloss_range\":\"second-person plural imperfect knowing, remodalized by the counterfactual particle and specified by a cognate accusative\",\"prose\":\"{{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}) is the same knowing verb heard in the warnings of 102:3-4, but {{ar:لَوْ}} ({{tr:law}}) changes its force: the repeated word now names an unrealized condition rather than an inevitable future. Because the verb is imperfect under that condition, the failed knowing is left ongoing rather than locked into a simple past counterfactual. Its second-person plural ending keeps the confronted audience inside the verb as the frame shifts, and the finite verb gathers the particle, subject ending, and certainty phrase into one protasis. The verb is then saturated by {{ar:عِلْمَ}} ({{tr:ʿilma}}), its own same-root verbal noun, so the adjacent root echo makes the cognate measure audible while the line demands not bare awareness but a measured knowing qualified as certainty. The broad {{ar:ع ل م}} ({{tr:ʿ-l-m}}) family can add the pressure of marks and recognition, but the local Form I verb remains direct knowing, not teaching, informing, or unrelated sign nouns; that epistemic frame comes before the surah's later turn from knowing to seeing in 102:6-7.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"knowledge, recognition, and marking/sign branches; local sense is knowing or recognizing, with sign/mark imagery only as a narrowed root-family pressure\",\"surface_display\":\"{{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:dual-grammar-hinge","source_type":"word_analysis","support_id":"sup_a8a091c1098e43284b6d","text":"{\"blocking_evidence\":null,\"headline\":\"one noun binds backward and forward\",\"reader_payoff\":\"The reader notices that one noun does two jobs at once: it measures the verb behind it and governs the certainty noun ahead of it.\",\"reason\":\"Attachment evidence licenses both the cognate accusative relation to {{ar:تَعْلَمُونَ}} ({{tr:taʿlamūna}}) and the {{ar:إِضَافَة}} ({{tr:iḍāfa}}) relation to {{ar:ٱلْيَقِينِ}} ({{tr:al-yaqīn}}).\",\"representative_source_ids\":[\"MG-d7b0b5fb\",\"QS-d20e949d\",\"QT-299ed2c2\",\"QY-2c6f0552\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:root-cadence-into-certainty","source_type":"word_analysis","support_id":"sup_b3b464ba06a7d84717f5","text":"{\"blocking_evidence\":null,\"headline\":\"cadence moves from knowing to certainty\",\"reader_payoff\":\"The reader notices the sound and root reprise from the verb into the noun before the phrase resolves into certainty.\",\"reason\":\"The adjacent same-root words support the cadence claim, but it remains secondary to the grammatical cognate and construct relations.\",\"representative_source_ids\":[\"QE-4194da01\",\"QP-f67a2c10\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:accusative-role-compression","source_type":"word_analysis","support_id":"sup_b86b71a2027b37578c13","text":"{\"blocking_evidence\":null,\"headline\":\"manner and known state compress\",\"reader_payoff\":\"The reader notices that the accusative noun can be felt both as the manner of knowing and as the knowledge-state demanded.\",\"reason\":\"The local guardrail strongly treats the phrase as cognate accusative rather than an ordinary direct object, so the object reading is retained only as semantic compression.\",\"representative_source_ids\":[\"QG-25ed6132\",\"QS-5bd0b267\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:retroactive-coloring","source_type":"word_analysis","support_id":"sup_bb7abfbc3ad8d138e153","text":"{\"blocking_evidence\":null,\"headline\":\"certainty rereads prior knowing\",\"reader_payoff\":\"The reader notices that once certainty is named, the earlier knowing warnings are reread as movement toward more than information.\",\"reason\":\"The same-surah repetition of the knowing verb and the final certainty qualifier support the retroactive pressure.\",\"representative_source_ids\":[\"QB-50ed5a57\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:mark-recognition-pressure","source_type":"word_analysis","support_id":"sup_c033d1b707b9f7e5dbd5","text":"{\"blocking_evidence\":null,\"headline\":\"mark imagery sharpens recognition\",\"reader_payoff\":\"The reader notices that knowing can carry the flavor of recognizing what is marked and distinguishable, while the local sense remains cognition.\",\"reason\":\"V4 accepts a mark/sign branch for {{ar:ع ل م}} ({{tr:ʿ-l-m}}), but the local Form I verb selects knowing; sign imagery is therefore retained only as root-family pressure.\",\"representative_source_ids\":[\"QS-10877e41\",\"QS-ba396310\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:2:suspended-pacing-and-forward-pressure","source_type":"word_analysis","support_id":"sup_c2fcd098a5a5ee137105","text":"{\"blocking_evidence\":null,\"headline\":\"brief particle suspends the clause\",\"reader_payoff\":\"The reader notices a pause before the long knowledge phrase, and the withheld result leaves room for the later seeing movement in 102:6-7.\",\"reason\":\"The pacing claim is recitational and therefore secondary, while the forward-pressure claim is supported by the omitted answer and the concrete same-surah continuation.\",\"representative_source_ids\":[\"QP-939c68fa\",\"QB-52774dba\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4:rare-certainty-construction","source_type":"word_analysis","support_id":"sup_c417a5fee4bd1d759184","text":"{\"blocking_evidence\":null,\"headline\":\"ordinary knowledge enters a rare frame\",\"reader_payoff\":\"The reader notices that a common knowledge noun becomes load-bearing because it is placed in an uncommon certainty construct.\",\"reason\":\"Distributional evidence shows the {{ar:ع ل م}} ({{tr:ʿ-l-m}}) gerund is common, while the CRITICAL row's exact constructional rarity is not contradicted by the guardrails.\",\"representative_source_ids\":[\"QI-fe627fc5\",\"QH-c8419039\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:1:deterrent-corrective-break","source_type":"word_analysis","support_id":"sup_c53ef01813eb2f823ebd","text":"{\"blocking_evidence\":null,\"headline\":\"deterrent break opens correction\",\"reader_payoff\":\"The reader notices that the ayah begins by stopping the prior heedless orientation before the conditional can be heard.\",\"reason\":\"QAC identifies {{ar:كَلَّا}} ({{tr:kallā}}) as a deterrent/rejection particle, and the local clause evidence places {{ar:لَوْ}} ({{tr:law}}) immediately after it as the counterfactual opening.\",\"representative_source_ids\":[\"QG-90b4a1ae\",\"QS-d510aa75\",\"QS-ea72a084\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:1","source_type":"word_analysis","support_id":"sup_cf4a9d6602311ffb5b3d","text":"{\"gloss_range\":\"deterrent and corrective discourse particle that halts the preceding heedless movement and opens a new conditional frame\",\"prose\":\"{{ar:كَلَّا}} ({{tr:kallā}}) does not merely decorate the opening of 102:5. It halts the accumulation-and-warning sequence before it, then releases the listener into {{ar:لَوْ}} ({{tr:law}}), so the line becomes a corrective interruption rather than a neutral supposition. Because the same particle has already sounded in 102:3 and 102:4, this third occurrence is a staged escalation: the refrain is preserved, but its neighbor changes from future warning to counterfactual diagnosis. The heavy doubled sound can support the felt stop, while the grammar keeps the main payoff discourse-level: a refusal that resets the ayah into the missing knowledge of certainty.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَلَّا}} ({{tr:kallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:4","source_type":"word_analysis","support_id":"sup_e425028876551e2b1876","text":"{\"gloss_range\":\"accusative maṣdar functioning as cognate measure of knowing and construct head qualified by certainty\",\"prose\":\"{{ar:عِلْمَ}} ({{tr:ʿilma}}) is the hinge of the clause. Backward, it measures the preceding knowing verb as a cognate accusative; forward, it heads the construct with the certainty noun. That double binding makes the ayah ask for a mode of knowing that is also a determinate epistemic state, not a loose object after the verb. The noun's lack of its own article does not make the phrase indefinite, because the definite genitive transfers determination into the construct, so previously open-ended knowing is specified as certainty-grade knowledge. A common knowledge noun is therefore made load-bearing by an uncommon certainty construction: it fuses knowledge and certainty in 102:5, opposite the denied knowledge and certainty in 4:157. Its root family can still make the knowledge feel like recognition of marked reality, and the sound reprise from the verb into the noun carries the phrase toward certainty. It also prepares the same-surah shift from this knowledge-of-certainty phrase to the later vision-of-certainty formula in 102:7, while the related truth-of-certainty formulas in 56:95 and 69:51 show the wider construct family.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"knowledge, recognition, and sign/mark branches; the local noun selects knowledge while mark imagery may color recognition only secondarily\",\"surface_display\":\"{{ar:عِلْمَ}} ({{tr:ʿilma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:closing-weight","source_type":"word_analysis","support_id":"sup_e920fe489618ba685fe6","text":"{\"blocking_evidence\":null,\"headline\":\"certainty closes the ayah\",\"reader_payoff\":\"The reader notices that the ayah does not land on the verb or even the knowledge noun, but on certainty as the final concept.\",\"reason\":\"The word is the final item in the counterfactual clause, completing the span governed by {{ar:لَوْ}} ({{tr:law}}).\",\"representative_source_ids\":[\"QT-b8c6d32a\",\"QT-d6fc00d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:5:certainty-formula-family","source_type":"word_analysis","support_id":"sup_f0e8985ba296afa0c14e","text":"{\"blocking_evidence\":null,\"headline\":\"certainty joins construct formulas\",\"reader_payoff\":\"The reader notices that this tail belongs to a broader construct family, including {{ar:عَيْنَ ٱلْيَقِينِ}} ({{tr:ʿayna al-yaqīn}}) in 102:7 and {{ar:حَقَّ ٱلْيَقِينِ}} ({{tr:ḥaqqa al-yaqīn}}) in 56:95 and 69:51.\",\"reason\":\"The row supplies concrete formula references, and the local word occupies the same definite certainty-tail position.\",\"representative_source_ids\":[\"QE-aaf9e3c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:5:3:knowledge-before-seeing","source_type":"word_analysis","support_id":"sup_f72df6a03050f49f4683","text":"{\"blocking_evidence\":null,\"headline\":\"knowing precedes seeing\",\"reader_payoff\":\"The reader notices that the surah first frames the problem as knowing before the later movement to seeing in 102:6-7.\",\"reason\":\"The same-surah contrast is explicit in CRITICAL rows, and the local verb is a cognition verb from {{ar:ع ل م}} ({{tr:ʿ-l-m}}).\",\"representative_source_ids\":[\"QS-6b5ac935\",\"QT-5c908c81\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B001","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"Disclosure to a knower supplies the transition from merely lacking information to a matter becoming clear.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settled knowledge with doubt removed supplies the threshold at which disclosure becomes determinative.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]}],"changed_reading":{"after":"An unrealized epistemic threshold: were the matter to become clear and stabilize beyond doubt, an unstated consequence would follow.","before":"A generic wish that the addressees possessed more information."},"confidence":"strong","focus_anchor":"The cognate verb-noun pairing at words 3-4 and the certainty qualifier at word 5.","mechanism":"Knowing appears both as an event and as a named state: disclosure must become settled enough to remove doubt, while the conditional leaves its consequence suspended.","model_id":"b_disclosure_threshold"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_disclosure_threshold","source_type":"hft","support_id":"sup_5d57b721bad5d690c623","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"The distinguishing mark makes knowledge a guidance relation between a present sign and what it indicates.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"The removal of doubt makes successful sign-reading terminate in a stable judgment.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]}],"changed_reading":{"after":"Certainty can be the stable result of correctly reading a distinguishing landmark that points beyond what is presently seen.","before":"Certainty is simply a high degree of subjective confidence."},"confidence":"medium","focus_anchor":"The doubled root at words 3-4 permits the noun of knowing to be heard as a discriminating mark as well as an internal state.","mechanism":"A mark points beyond itself to an absent object; certainty is reached by following a reliable distinction rather than by possessing the object in immediate sight.","model_id":"b_landmark_certainty"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_landmark_certainty","source_type":"hft","support_id":"sup_c26b56eae4bddea714fc","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ","ayah_ref":"102:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B005","root_001696/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001040","role":"The gathered body of water supplies a reservoir image for knowledge accumulating into a coherent whole.","root":"ع ل م","source_ref":"102:5","source_word_indices":["3","4"]},{"branch_id":"B001","mapped_root_id":"root_001696","role":"Settledness keeps the reservoir image tied to the focus construction's demand for doubt-ending knowledge.","root":"ي ق ن","source_ref":"102:5","source_word_indices":["5"]}],"changed_reading":{"after":"Exploratorily, knowing with certainty is knowledge gathering into a settled reservoir whose accumulated weight could change conduct.","before":"Knowing is the possession of a discrete true proposition."},"confidence":"exploratory","focus_anchor":"The repeated root at words 3-4 carries a remote branch in which gathered abundant water is named from the same root.","mechanism":"Knowledge is provisionally imaged as an accumulated body rather than an isolated proposition; certainty gives that gathered content settledness.","model_id":"b_reservoir_certainty"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_reservoir_certainty","source_type":"hft","support_id":"sup_416da319492089188f91","trust":"legacy_unbound"}]}
</lane_packet_json>
