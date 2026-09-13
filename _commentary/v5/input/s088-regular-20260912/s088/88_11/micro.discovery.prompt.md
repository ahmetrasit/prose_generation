# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:11",
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
{"branch_registry":[{"boundary":"Dal, kulağın kendisini, ün kazanmayı ve şarkı söylemeyi değil, sesin işitsel olarak algılanmasını kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000741/B001","candidate_links":[{"candidate_id":"cand_4f483aec6bdd1ef3809d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"duymak ve dikkatle dinlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ses, kulak aracılığıyla fark edilir ve işitsel algıya dönüşür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dikkat sese çevrildiğinde eylem, edilgin duymadan amaçlı dinlemeye geçer."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kalıplar dinlemeye çağrı bildirir veya çokça dinleyen kişiyi niteler."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sesin kulakla algılanmasını ve dikkat sese yöneltildiğinde ortaya çıkan amaçlı dinlemeyi birlikte anlatır.","boundary_detail":"Dal, kulağın kendisini, ün kazanmayı ve şarkı söylemeyi değil, sesin işitsel olarak algılanmasını kapsar.","branch_image_ar":"إدراك الأصوات بالأذن","concept_gloss":"duymak ve dikkatle dinlemek","contextual_glosses":[{"applicability":"Bir sesin herhangi bir özel dikkat vurgusu olmadan kulakla algılandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Amaçlı ve dikkatli dinleme yönünü tek başına belirtmez.","preserves":"Sesin kulakla algılanması çekirdeğini korur."},"facet_ids":["F001"],"text":"duymak","usage_role":"general"},{"applicability":"Kişinin dikkatini söze veya sese bilerek verdiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden gerçekleşen yalın duyma durumunu dışarıda bırakır.","preserves":"Dikkatin sese yöneltilmesi özelliğini korur."},"facet_ids":["F002"],"text":"dinlemek","usage_role":"contextual"}],"definition":"Bir sesi kulak yoluyla algılamak veya dikkati o sese yönelterek dinlemektir; bazı biçimler birini dinlemeye çağırır ya da çokça dinleyen kişiyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ses, kulak aracılığıyla fark edilir ve işitsel algıya dönüşür."},{"facet_id":"F002","role":"specialization","statement":"Dikkat sese çevrildiğinde eylem, edilgin duymadan amaçlı dinlemeye geçer."},{"facet_id":"F003","role":"associated_use","statement":"Bazı kalıplar dinlemeye çağrı bildirir veya çokça dinleyen kişiyi niteler."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eylem yerine işitme organını gösterir.","collision":"Aynı kökün kulak ve kulak açıklığı dalıyla karışır.","fit":"displacement","loses":"Sesin algılanması ve dikkatle dinleme eylemlerini kaybeder.","preserves":"İşitmeyle bağlantılı beden alanını çağrıştırır."},"text":"kulak"}],"identity_rationale":"Kaynak sözü, sesin kulakla algılanmasını temel alır; bunun yanında dikkatle dinleme ve dinlemeye çağırma kullanımlarını da açıkça içerir. Bu nedenle dalın duyma ve dinleme çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sesi kulakla algılamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"işitme gücü veya duyma eylemi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"duyma eylemi veya duyulan şey"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"dikkatle dinlemek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"duymaya çalışarak kulak vermek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"beni dinle ve söylediklerime kulak ver"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dinle"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"söylenenleri çokça dinleyen kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"işiten kimse"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"kendi kulağımla duydum; görmeyle ilgili aktarılmış yorum kaynakta reddedilir"}],"lexicalization_note":"Tanım yalın duyma çekirdeğini korur; dikkatle dinleme, dinlemeye çağırma ve çok dinleyen kişi anlamları yalnızca ilgili biçim ve söz öbeklerine bağlıdır.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; işitme eylemiyle en kolay karışan organ, anlama ve hoş ses dalları yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal işitsel algı ve dinleme aşamasındadır; komşu dal ise algılanan sözün anlaşılması, kabulü veya davranışa geçirilmesi sonucunu anlatır.","focus_only":"Sesin kulağa ulaşması ve dikkatle dinlenmesi yeterlidir.","gloss":"duymak ile anlayıp uymak","neighbor_only":"Sözü anlamak, kabul etmek veya ona uymak gerekir.","neighbor_ref":"root_000741/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da işitilen sözün kişi tarafından alınması sürecinde yer alır."},{"boundary_match":"field_only","distinction":"Bu dal sesin algılanmasını anlatırken komşu dal algıyı gerçekleştiren organı veya onun açıklığını adlandırır.","focus_only":"Duyma ve dinleme birer algı eylemidir.","gloss":"işitme ile kulak","neighbor_only":"Kulak ve kulak açıklığı bedensel yapılardır.","neighbor_ref":"root_000741/B002","relation_type":"same_field","shared_zone":"İki dal işitme alanını ve kulağın bu süreçteki rolünü paylaşır."},{"boundary_match":"partial","distinction":"Bu dal genel işitsel algıdır; komşu dal yalnızca hoş bulunan ya da şarkı niteliği taşıyan ses ve onun icracısıyla ilgilidir.","focus_only":"Hoşluk veya ezgi şartı olmadan her tür ses algılanabilir.","gloss":"dinlemek ile ezgili ses","neighbor_only":"Hoş bulunan ses, şarkı veya şarkıcı özellikle öne çıkar.","neighbor_ref":"root_000741/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da kulağa ulaşan ses ve onu dinleme deneyimiyle ilgilidir."}],"source_phrase_ar":"إيناس الشيء بالأذن (maqayis)؛ سمعت الشيء سمعا (maqayis;sihah;mufradat)؛ الاستماع الإصغاء (sihah;mufradat)؛ سماع أي اسمع (maqayis;sihah)؛ السمع سمع الإنسان وغيره (tahdhib)","source_summary":"Kaynaklar sesin kulakla algılanması çekirdeğinde birleşir; dikkatle dinleme ve dinlemeye yönelten söyleyişler bu çekirdeğin özel gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إدراك الصوت بالأذن وفعل السماع والاستماع والإصغاء والنداء إلى السماع","what_is_not_ar":"ليس الأذن نفسها ولا الشهرة بين الناس ولا الغناء"},"support_links":["sup_7a4cc0ca2df710cba60d"]},{"boundary":"Bu dal işitme eylemini değil, kulağı ve özellikle sesin alındığı kulak açıklığını adlandırır.","branch_kind":"bare","branch_ref":"root_000741/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"kulak ve kulak açıklığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, işitme organı olarak kulağı kapsar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Daha dar kullanımda kulağın sesi alan açıklığı veya işitme yeri belirtilir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem işitme organının bütünü hem de sesin alındığı açıklık birlikte kastedildiğinde kapsamı eksiksiz verir.","boundary_detail":"Bu dal işitme eylemini değil, kulağı ve özellikle sesin alındığı kulak açıklığını adlandırır.","branch_image_ar":"الأذن وموضع السمع","concept_gloss":"kulak ve kulak açıklığı","contextual_glosses":[{"applicability":"Söz organın bütününü gösterdiğinde kullanılan en doğal genel karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kulak açıklığına özgü dar kullanım ayrıca belirtilmez.","preserves":"İşitme organı gönderimini tam olarak korur."},"facet_ids":["F001"],"text":"kulak","usage_role":"general"},{"applicability":"Kaynak biçim kulağın ses aldığı deliği veya işitme yerini gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Organın bütününü kapsayan daha geniş kullanımı dışarıda bırakır.","preserves":"Kulağın ses alan açıklığına yapılan gönderimi korur."},"facet_ids":["F002"],"text":"kulak açıklığı","usage_role":"contextual"}],"definition":"İşitmeyi sağlayan kulak veya sesin içeri girdiği kulak açıklığıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, işitme organı olarak kulağı kapsar."},{"facet_id":"F002","role":"specialization","statement":"Daha dar kullanımda kulağın sesi alan açıklığı veya işitme yeri belirtilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bedensel yapı yerine algı eylemini anlatır.","collision":"Sesin kulakla algılanması dalıyla karışır.","fit":"displacement","loses":"Organ ve organ açıklığı gönderimlerini kaybeder.","preserves":"Kulağın temel işleviyle bağlantıyı korur."},"text":"işitme"}],"identity_rationale":"Kaynak sözü hem kulağın kendisini hem de kulağın ses alan açıklığını adlandırır. Dal çerçevesi bu iki bedensel gönderimi korur ve kova sapı gibi benzetmeli araç anlamını dışarıda bırakır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kulak veya işitme yeri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kulak veya kulak açıklığı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kulak açıklığı veya işitme yeri"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kulak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iki kulak veya iki işitme yeri"}],"lexicalization_note":"Tanım yalın organ anlamıyla sınırlıdır; aynı biçimin kova, yük kabı veya bağlama aracındaki benzetmeli kullanımları bu dala taşınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel kulak dalı ile aynı kökün duyma dalı sınırı açıklamada en yararlı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kulağı özellikle işitme yeri ve açıklığıyla birlikte ele alır; komşu dal genel kulak adını, kulak biçimli nesneleri ve kulağa yönelik eylemleri de kapsar.","focus_only":"Kulak açıklığı ve işitme yeri ayrıca adlandırılabilir.","gloss":"kulak ve işitme açıklığı","neighbor_only":"Kulak biçimli kap sapı ve kulağa uygulanan eylemler de kapsama girebilir.","neighbor_ref":"root_000022/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği insan veya hayvan kulağıdır."},{"boundary_match":"field_only","distinction":"Bu dal araç olan organı adlandırır; komşu dal o organ aracılığıyla gerçekleşen algı ve dinleme sürecini anlatır.","focus_only":"Gönderim beden parçasına veya onun açıklığına yönelir.","gloss":"kulak ile duyma","neighbor_only":"Gönderim sesin algılanması ya da dikkatle dinlenmesi eylemine yönelir.","neighbor_ref":"root_000741/B001","relation_type":"same_field","shared_zone":"İki dal kulağın işitmedeki işlevi nedeniyle aynı deneyim alanında buluşur."}],"source_phrase_ar":"السمع الأذن وهي المسمعة (ayn;tahdhib)؛ المسمعة خرقها (ayn)؛ المسمع خرق الأذن (tahdhib;mufradat)؛ السامعة الأذن (sihah)؛ المسمعان الأذنان (sihah;tahdhib)","source_summary":"Kaynaklar kulağı temel gönderim olarak verir ve bazı biçimlerde bu gönderimi kulağın açıklığına ya da işitme yerine daraltır.","sources":["AY","SI","TA","MU"],"what_is_ar":"الأذن وخرق الأذن والموضع الذي يقع به السمع وما يسمى سامعة أو مسمعا","what_is_not_ar":"ليس فعل السماع ولا عروة الدلو المسماة مسمعا"},"support_links":[]},{"boundary":"Yalın ses algısı yeterli değildir; işitilen sözün anlaşılması, kabul edilmesi veya ona uyulması gerekir.","branch_kind":"bare","branch_ref":"root_000741/B003","candidate_links":[{"candidate_id":"cand_14d8928c037ce80960e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"anlayıp kabul etmek ve uymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşitilen sözün anlamı kavranır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlama, sözü kabul etme ve ona uygun davranma sonucuna uzanabilir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşitilen sözün kavranmasından kabulüne ve gereğinin yapılmasına kadar uzanan çekirdeği birlikte karşılar.","boundary_detail":"Yalın ses algısı yeterli değildir; işitilen sözün anlaşılması, kabul edilmesi veya ona uyulması gerekir.","branch_image_ar":"الفهم والامتثال","concept_gloss":"anlayıp kabul etmek ve uymak","contextual_glosses":[{"applicability":"Birinin söylediğini anlayıp kabul etme veya öğüdüne uyma bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözü kavrama, kabul etme ve ona uyma yönlerini bağlam içinde korur."},"facet_ids":["F001","F002"],"text":"sözünü dinlemek","usage_role":"contextual"}],"definition":"İşitilen sözü anlamak ve bağlama göre onu kabul ederek gereğini yerine getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşitilen sözün anlamı kavranır."},{"facet_id":"F002","role":"extension","statement":"Anlama, sözü kabul etme ve ona uygun davranma sonucuna uzanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalın işitsel algı dalıyla kolayca karışır.","fit":"narrowing","loses":"Anlama, kabul etme ve gereğini yerine getirme sonuçlarını kaybeder.","preserves":"Sözün kişi tarafından işitilmiş olmasını korur."},"text":"duymak"}],"identity_rationale":"Kaynak sözü işitmeyi yalnızca ses almak olarak değil, sözü anlamak ve ardından kabul edip uymak olarak açıklar. Dalın anlama ve yerine getirme çerçevesi bu katmanlı anlamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sözü anlayıp kabul etmek ve ona uymak"}],"lexicalization_note":"Tanım yalın biçimin anlam ve davranış sonucuna uzanan kullanımını verir; yalnız belirli bir söz öbeğine bağlı ek kapsam yüklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; kabul ederek dinleme ve yalın işitme, bu dalın sınırını en doğrudan açıklayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal anlama ile başlayıp uyma sonucuna varır; komşu dal dinleme, sessizce kulak verme ve kabul etme tutumunu daha geniş biçimde kapsar.","focus_only":"Sözü kavramanın yanında ona uyma sonucu açıkça bulunur.","gloss":"dinleyip kabul etmek","neighbor_only":"Her konuşanı dinleme ve söyleneni kabul etme eğilimi ayrıca kapsanır.","neighbor_ref":"root_000022/B002","relation_type":"near_synonym","shared_zone":"Her iki dal dikkatle dinlenen sözün kabul edilmesine uzanabilir."},{"boundary_match":"partial","distinction":"Komşu dal işitsel algıda tamamlanabilir; bu dal için sözün bilişsel olarak kavranması ve kimi bağlamlarda davranışa yön vermesi gerekir.","focus_only":"Sözün anlamı kavranır ve kabul ya da uyma gerçekleşebilir.","gloss":"duymak ile anlamak","neighbor_only":"Anlama gerçekleşmeden de ses kulakla algılanabilir.","neighbor_ref":"root_000741/B001","relation_type":"near_neighbor","shared_zone":"İki dal, sözün kulağa ulaşmasından sonraki iletişim sürecinde art arda yer alır."}],"source_phrase_ar":"تارة عن الفهم وتارة عن الطاعة (mufradat)؛ فهمنا وارتسمنا (mufradat)؛ فهمنا وهم لا يفهمون (mufradat)؛ لم يستعملوا هذه الحواس استعمالا يجدي عليهم (tahdhib)","source_summary":"Kaynaklar işitmeyi bilişsel ve davranışsal bir sonuçla açıklar: söz anlaşılır, ardından kabul veya uyma gerçekleşebilir.","sources":["MU","TA"],"what_is_ar":"السمع بمعنى فهم القول أو قبوله والعمل بموجبه والطاعة بعد الفهم","what_is_not_ar":"ليس مجرد وصول الصوت إلى الأذن ولا إعلان الشيء بين الناس"},"support_links":["sup_ed169584d7a5e4698a8a"]},{"boundary":"Bu dal iletiyi yaygınlaştırmayı değil, belirli bir alıcının sesi duymasını veya sözü anlamasını sağlamayı anlatır.","branch_kind":"bare","branch_ref":"root_000741/B004","candidate_links":[{"candidate_id":"cand_e2ad12629184a76caed3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"duyurmak veya kavratmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, başka bir kişinin sesi işitmesine neden olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgenlik, yalnız sesi ulaştırmaktan sözü karşı tarafa kavratmaya uzanabilir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir başkasının sesi işitmesini sağlama ile sözü ona anlatıp kavratma sonuçlarını birlikte kapsar.","boundary_detail":"Bu dal iletiyi yaygınlaştırmayı değil, belirli bir alıcının sesi duymasını veya sözü anlamasını sağlamayı anlatır.","branch_image_ar":"إسماع الغير","concept_gloss":"duyurmak veya kavratmak","contextual_glosses":[{"applicability":"Amaç bir sesin ya da sözün belirli bir kişinin kulağına ulaşmasını sağlamak olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözü karşı tarafa kavratma sonucunu zorunlu olarak belirtmez.","preserves":"Başkasının işitmesini sağlama çekirdeğini korur."},"facet_ids":["F001"],"text":"duyurmak","usage_role":"general"},{"applicability":"Ettirgen biçim yalnız işittirmeyi değil, söyleneni karşı tarafa anlaşılıp benimsenir kılmayı belirttiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Salt ses ulaştırma düzeyindeki kullanımı dışarıda bırakır.","preserves":"Karşı tarafın sözü anlamasını sağlama sonucunu korur."},"facet_ids":["F002"],"text":"anlatıp kavratmak","usage_role":"contextual"}],"definition":"Bir sesin başkasına ulaşmasını sağlayarak onu duyurmak veya sözü ona kavratmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, başka bir kişinin sesi işitmesine neden olur."},{"facet_id":"F002","role":"extension","statement":"Ettirgenlik, yalnız sesi ulaştırmaktan sözü karşı tarafa kavratmaya uzanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kamuya açıklama ve geniş bir topluluğa yayma anlamını ekler.","collision":"Ün ve insanlar arasında yayılma dalıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Bir sözün başkalarına ulaşması yönünü korur."},"text":"ilan etmek"}],"identity_rationale":"Kaynak sözü bir başkasının sesi duymasını sağlama ile sözü ona anlatıp kavratma kullanımlarını birlikte verir. Dalın başkasına duyurma ve anlatma çerçevesi bu iki sonucu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"duymasını sağlamak veya kavratmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"başkasına duyuran kimse"}],"lexicalization_note":"Tanım yalın ettirgen kullanımı kapsar; şetme veya herkese duyurarak ün kazandırma gibi kalıba bağlı anlamlar eklenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; mesaj iletme ve seslenme dalları, ettirgen duyurma sonucunun araç ve kapsam sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal alıcının duyması veya anlaması sonucuna odaklanır; komşu dal ise mesajın hedefe erişmesini, kullanılan algı yolundan bağımsız olarak anlatır.","focus_only":"Alıcının sesi işitmesi veya sözü kavraması ettirgen sonucun parçasıdır.","gloss":"duyurmak ile iletmek","neighbor_only":"İletinin hedefe ulaşması, işitme yoluna bağlı olmadan yeterlidir.","neighbor_ref":"root_000151/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir içeriğin göndericiden alıcıya ulaşmasını konu edinir."},{"boundary_match":"partial","distinction":"Bu dal ulaşılan işitsel veya bilişsel sonucu anlatır; komşu dal çağrı yapma ve sesi yükseltme biçimini anlatır.","focus_only":"Sesin alıcı tarafından işitilmesi veya anlaşılması gerekir.","gloss":"duyurmak ile seslenmek","neighbor_only":"Ses yükseltme ve çağrıda bulunma eylemin kendisini oluşturur.","neighbor_ref":"root_001487/B001","relation_type":"near_neighbor","shared_zone":"Ses yükseltmek bir başkasına duyurmanın olağan araçlarından biri olabilir."}],"source_phrase_ar":"سمعه الصوت وأسمعه (sihah)؛ السميع المسمع (sihah;tahdhib)؛ أسمعهم أي أفهمهم (mufradat)؛ فعلت ذلك تسمعتك وتسمعة لك أي لتسمعه (tahdhib)","source_summary":"Kaynaklar ettirgen çekirdeği paylaşır: ses başkasına ulaştırılır; bazı kullanımlarda beklenen sonuç karşı tarafın sözü anlamasıdır.","sources":["SI","TA","MU"],"what_is_ar":"إبلاغ الصوت أو الحديث إلى غيره والتسبب في سماعه أو إفهامه","what_is_not_ar":"ليس الشتم ولا التشهير ولا الصيت"},"support_links":["sup_17623535f2c99623da25"]},{"boundary":"Ün veya yaygın söz edilme çekirdektir; haberi yayma, birini öne çıkarma ve duyulsun diye gösteriş yapma ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000741/B005","candidate_links":[{"candidate_id":"cand_24b485fa16f9a1ed8405","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"adı yayılıp tanınmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey hakkında söz geniş bir çevrede dolaşır ve tanınmışlık doğurur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ün, özellikle güzel ad ve olumlu anılma olarak gerçekleşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanımda bir haber yayılır veya bir kişinin adı öne çıkarılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir iş, insanlar duysun ve yapan tanınsın diye gösteriş amacıyla yapılabilir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanlar arasında söz edilme yoluyla tanınmışlık veya ün oluşmasını en kısa doğal biçimde karşılar.","boundary_detail":"Ün veya yaygın söz edilme çekirdektir; haberi yayma, birini öne çıkarma ve duyulsun diye gösteriş yapma ayrı kullanımlardır.","branch_image_ar":"الصيت والشيوع بين الناس","concept_gloss":"adı yayılıp tanınmak","contextual_glosses":[{"applicability":"Bir kişinin adının insanlar arasında özellikle olumlu biçimde yayılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz yayılmayı, haberi yayma eylemini ve gösteriş amacını dışarıda bırakır.","preserves":"Yaygın tanınma ve güzel ad kazanma yönünü korur."},"facet_ids":["F001","F002"],"text":"ün salmak","usage_role":"general"},{"applicability":"Bir haberin veya kişinin adının konuşularak geniş çevreye taşındığı ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yayılmanın doğurduğu ünü ve gösteriş amacıyla yapılan işi tek başına vermez.","preserves":"Sözü insanlar arasında yayma eylemini korur."},"facet_ids":["F003"],"text":"dilden dile yaymak","usage_role":"contextual"},{"applicability":"Bir işin iç değerinden çok başkalarının onu duyması ve yapanı tanıması için gerçekleştirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel ün ve haber yayma kullanımlarını kapsamaz.","preserves":"Başkalarının duymasını amaçlayan gösteriş yönünü korur."},"facet_ids":["F004"],"text":"duyulsun diye gösteriş yapmak","usage_role":"explanatory"}],"definition":"Bir kişi veya şey hakkında sözün insanlar arasında yayılmasıyla tanınmışlık ya da ün oluşmasıdır. Bazı biçimler haberi yayma, birini övgüyle anılır kılma veya yapılan işi başkaları duysun diye sergileme eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey hakkında söz geniş bir çevrede dolaşır ve tanınmışlık doğurur."},{"facet_id":"F002","role":"source_variant","statement":"Ün, özellikle güzel ad ve olumlu anılma olarak gerçekleşebilir."},{"facet_id":"F003","role":"extension","statement":"Ettirgen kullanımda bir haber yayılır veya bir kişinin adı öne çıkarılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir iş, insanlar duysun ve yapan tanınsın diye gösteriş amacıyla yapılabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Yalın işitsel algı dalıyla karışır.","fit":"narrowing","loses":"Sözün topluluk içinde yayılması ve ün doğurması sonucunu kaybeder.","preserves":"Bilginin bir kişiye ulaştığı ilk aşamayı korur."},"text":"duymak"}],"identity_rationale":"Kaynak sözü güzel ünü, bir haberin insanlar arasında yayılmasını, birini tanınır kılmayı ve başkaları duysun diye gösteriş yapmayı aynı dalda toplar. Dal kullanılabilir, ancak ün sonucu ile yayma eylemi ve gösteriş amacı tek bir eşanlamlı çekirdek gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yaymak, tanınır kılmak veya adını öne çıkarmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"güzel ün ve iyi ad"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"duyulup yayılan ve konuşulan şey"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"insanlar duysun diye yapılan gösteriş"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"insanların haberi birbirinden duyup yayması"}],"lexicalization_note":"Yalın ün ve yaygın söz edilme anlamı, bir şeyi yayma eyleminden ve insanların duyması amacıyla yapılan gösterişi bildiren söz öbeklerinden ayrı tutulur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; genel tanınmışlık, yalnız iyi ün ve haber yayma dalları bu çok parçalı dalın temel sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal söz edilme ve duyulma yoluyla ün oluşmasına odaklanır; komşu dal görünürlük ve açıklığı da kapsayan daha geniş bir tanınmışlık alanına sahiptir.","focus_only":"Ün, güzel ad, haberi yayma ve duyulsun diye gösteriş yapma kullanımları birlikte bulunur.","gloss":"ün ve yaygın tanınma","neighbor_only":"Bir durumun açık ve görünür hâle gelmesi, kişilerce anılma olmadan da kapsanır.","neighbor_ref":"root_000823/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin insanlar arasında bilinir ve tanınır duruma gelmesini kapsar."},{"boundary_match":"partial","distinction":"Komşu dal yalnız olumlu ünü anlatır; bu dal güzel adın yanında her tür yayılmayı, birini tanınır kılmayı ve duyulsun diye yapılan gösterişi de kapsar.","focus_only":"Olumlu veya olumsuz yayılma, yayma eylemi ve gösteriş amacı da yer alabilir.","gloss":"iyi ün ile genel ün","neighbor_only":"Ün yalnızca iyi yöndeki ses ve tanınmışlıkla sınırlıdır.","neighbor_ref":"root_000745/B008","relation_type":"near_synonym","shared_zone":"İki dal kişinin insanlar arasında iyi adla tanınmasını kapsar."},{"boundary_match":"partial","distinction":"Bu dal yayılmanın kişi veya şey hakkında ün ve söz edilme doğurmasına odaklanır; komşu dal ise bilginin açığa çıkarılıp dağıtılması eylemini anlatır.","focus_only":"Yayılan sözün doğurduğu tanınmışlık ve gösteriş amacı önemlidir.","gloss":"ün salmak ile haber yaymak","neighbor_only":"Herhangi bir haberin açığa vurulup yayılması tek başına yeterlidir.","neighbor_ref":"root_000528/B001","relation_type":"near_neighbor","shared_zone":"Bir haberin insanlar arasında yayılması iki dalda da gerçekleşebilir."}],"source_phrase_ar":"السمع الذكر الجميل (maqayis;sihah)؛ السماع ما سمعت به فشاع (ayn;tahdhib)؛ سمعت بالشيء إذا أشعته (maqayis)؛ فعله رياء وسمعة (ayn;sihah)؛ سمع به أي شهره (sihah)؛ سمعت بفلان في الناس إذا نوهت بذكره (tahdhib)","source_summary":"Toplu kanıt, insanlar arasında yayılan sözden doğan ünü; haberi yayma, birini anılır kılma ve başkaları duysun diye gösteriş yapma kullanımlarıyla birlikte verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الذكر والصيت وما يذاع أو يشاع ليسمعه الناس والسمعة والرياء والتشهير","what_is_not_ar":"ليس إدراك الصوت نفسه ولا الغناء ولا الشتم المحض"},"support_links":["sup_cbdb00cc01191c440820"]},{"boundary":"Sövme, kötü söz işittirme, kınayıp rezil etme ve duymamaya yönelik beddua yalnızca tanıklanan kalıplarda geçerlidir.","branch_kind":"collocation","branch_ref":"root_000741/B006","candidate_links":[{"candidate_id":"cand_e2ad12629184a76caed3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"kötü söz işittirip sövmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişiye işitmekten hoşlanmayacağı kötü ve aşağılayıcı sözler yöneltilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kötüleme, kişiyi kınayıp insanlar önünde rezil etmeye uzanabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanıklanan bir beddua kalıbı, kişinin işitme yetisini yitirmesini dile getirir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanıklanan söz öbeklerinde kişiye incitici söz yöneltme ve onu sözle kötüleme çekirdeğini karşılar.","boundary_detail":"Sövme, kötü söz işittirme, kınayıp rezil etme ve duymamaya yönelik beddua yalnızca tanıklanan kalıplarda geçerlidir.","branch_image_ar":"إسماع القبيح والشتم","concept_gloss":"kötü söz işittirip sövmek","contextual_glosses":[{"applicability":"Kişinin yüzüne hoşlanmayacağı, aşağılayıcı veya incitici sözler söylendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kınayarak rezil etme ve beddua kullanımlarını tam vermez.","preserves":"Kötü sözü doğrudan hedefe yöneltme özelliğini korur."},"facet_ids":["F001"],"text":"ağır sözler söylemek","usage_role":"contextual"},{"applicability":"Söyleyiş kişinin işitme yetisini yitirmesini dileyen özel beddua kalıbı olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sövme ve rezil etme kullanımlarını dışarıda bırakır.","preserves":"İşitme kaybını dileyen beddua anlamını korur."},"facet_ids":["F003"],"text":"duymaz olasın diye beddua etmek","usage_role":"explanatory"}],"definition":"Belirli söz öbeklerinde birine kötü söz söyleyip onu incitmek, sövmek veya kınayarak rezil etmektir; bir başka kalıp da kişinin duyamaz hâle gelmesini dileyen beddua bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişiye işitmekten hoşlanmayacağı kötü ve aşağılayıcı sözler yöneltilir."},{"facet_id":"F002","role":"extension","statement":"Kötüleme, kişiyi kınayıp insanlar önünde rezil etmeye uzanabilir."},{"facet_id":"F003","role":"associated_use","statement":"Tanıklanan bir beddua kalıbı, kişinin işitme yetisini yitirmesini dile getirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kötüleme içermeyen her türlü sesi ulaştırma anlamını ekler.","collision":"Başkasına ses işittirme dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Sözün hedef kişinin kulağına ulaşmasını korur."},"text":"duyurmak"}],"identity_rationale":"Kaynak sözü belirli söyleyişlerde birine kötü söz işittirmenin sövme anlamına gelmesini, birini kınayıp rezil etmeyi ve duymaması yönünde beddua etmeyi bir araya getirir. Dal doğrudur, ancak bunlar yalın ettirgen duyurma anlamı değil, kalıba bağlı kötüleyici kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sövmek ve hoşlanmayacağı sözleri yüzüne söylemek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"sövmek veya duymaz olmasını dilemek"}],"lexicalization_note":"Tanım yalnız verilen söz öbeklerindeki kötüleyici ve beddua niteliğindeki anlamı açıklar; kökün yalın biçimine genel sövme anlamı yüklemez.","neighbor_coverage_note":"Tüm adaylar incelendi; genel sövme ile tarafsız duyurma dalları, bu kalıba bağlı kötüleyici kullanımın iki temel sınırını verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal işittirme yapısına bağlı belirli kötüleyici kalıplardır; komşu dal sözlü saldırının genel adını ve daha geniş türlerini kapsar.","focus_only":"Kötü sözün hedefe işittirilmesi, rezil etme ve özel beddua kalıbı birlikte bulunur.","gloss":"sövmek ve kötü söz işittirmek","neighbor_only":"Genel sövme, karşılıklı sövüşme, ayıplama ve sövme konusu olan utanç daha geniş biçimde kapsanır.","neighbor_ref":"root_000664/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişiye aşağılayıcı ve incitici söz yöneltmeyi kapsar."},{"boundary_match":"partial","distinction":"Komşu dal tarafsız ettirgen duyurmadır; bu dal yalnız tanıklanan kalıplarda kötü söz, kınama, rezil etme veya beddua işlevi taşır.","focus_only":"İşittirilen içerik kötüleyici, incitici veya beddua niteliğindedir.","gloss":"duyurmak ile kötü söz işittirmek","neighbor_only":"Herhangi bir sesin duyurulması veya sözün kavratılması yeterlidir.","neighbor_ref":"root_000741/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir sözün başka bir kişinin kulağına ulaşması sağlanır."}],"source_phrase_ar":"أسمعه الحديث وسمعه أي شتمه (sihah)؛ أسمعت فلانا إذا سببته (mufradat)؛ أسمعك الله أي جعلك الله أصم (mufradat)؛ سمعت بالرجل تسميعا إذا نددت به وشهرته وفضحته (tahdhib)؛ أسمعته القبيح وشتمته (tahdhib)","source_summary":"Toplu kanıt, kötü söz işittirerek sövme ve kişiyi kınayıp rezil etme kullanımlarını, duymamaya yönelik bir beddua kalıbıyla birlikte verir.","sources":["SI","TA","MU"],"what_is_ar":"إسماع القبيح والسب والشتم والتنديد والفضيحة والدعاء بعدم السماع","what_is_not_ar":"ليس مجرد إسماع الصوت ولا الشهرة المحمودة"},"support_links":["sup_17623535f2c99623da25"]},{"boundary":"Her türlü ses veya duyma değil, kulağa hoş gelen ezgili ses, şarkı ve bunu söyleyen kadın icracı kapsanır.","branch_kind":"bare","branch_ref":"root_000741/B007","candidate_links":[{"candidate_id":"cand_4f483aec6bdd1ef3809d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"kulağa hoş gelen ezgili ses","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ses, kulağa hoş gelir ve estetik bir dinleme deneyimi oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hoş ses, ezgili söyleyiş veya şarkı olarak gerçekleşebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi bildiren biçim, şarkıyı söyleyen kadın icracıyı gösterir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hoşluk, işitsel nitelik ve şarkıya dönüşebilme özelliklerini birlikte karşılayan genel kavram sözüdür.","boundary_detail":"Her türlü ses veya duyma değil, kulağa hoş gelen ezgili ses, şarkı ve bunu söyleyen kadın icracı kapsanır.","branch_image_ar":"السماع المستلذ والغناء","concept_gloss":"kulağa hoş gelen ezgili ses","contextual_glosses":[{"applicability":"Söz belirli bir ezgili ses ürününü veya söylenen parçayı gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şarkı sayılmayan hoş sesi ve kadın icracı anlamını dışarıda bırakır.","preserves":"Ezgili ve hoş sesin şarkı olarak gerçekleşmesini korur."},"facet_ids":["F002"],"text":"şarkı","usage_role":"general"},{"applicability":"Kişi bildiren biçim hoş sesi veya şarkıyı söyleyen kadın icracıyı gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sesin veya şarkının kendisini gösteren kullanımları dışarıda bırakır.","preserves":"Kadın icracı gönderimini açıkça korur."},"facet_ids":["F003"],"text":"kadın şarkıcı","usage_role":"contextual"}],"definition":"Kulağa hoş gelen güzel ve çoğu kez ezgili ses ya da şarkıdır; kişi bildiren biçim ise bunu söyleyen kadın icracıyı adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ses, kulağa hoş gelir ve estetik bir dinleme deneyimi oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Hoş ses, ezgili söyleyiş veya şarkı olarak gerçekleşebilir."},{"facet_id":"F003","role":"associated_use","statement":"Kişi bildiren biçim, şarkıyı söyleyen kadın icracıyı gösterir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Hoşluk ve ezgi şartı olmayan bütün işitsel algıları ekler.","collision":"Genel duyma ve dikkatle dinleme dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Sesin kulakla alınması bağlantısını korur."},"text":"dinleme"}],"identity_rationale":"Kaynak sözü hem şarkıyı ve kulağa hoş gelen güzel sesi hem de bunu icra eden kadın şarkıcıyı verir. Dal çerçevesi hoş işitsel ürün ile icracı arasındaki ayrımı koruduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"şarkı veya kulağa hoş gelen güzel ses"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kadın şarkıcı"}],"lexicalization_note":"Tanım yalın biçimlerde tanıklanan hoş ses, şarkı ve kadın şarkıcı anlamlarını verir; genel dinleme anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; daha geniş şarkı alanı ile genel işitme dalı, hoş ve ezgili ses çekirdeğini en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hoş ses ve kadın icracı odağındadır; komşu dal şarkının yanında ezgili okuma, ses süsleme ve dinleme etkinliğine de uzanır.","focus_only":"Kulağa hoş gelen sesin yanında kadın şarkıcı adı da yer alır.","gloss":"şarkı ve hoş ses","neighbor_only":"Okumayı hüzünlü veya yumuşak sesle yapma ve dinleme etkinliği daha geniş biçimde kapsanır.","neighbor_ref":"root_001110/B003","relation_type":"near_synonym","shared_zone":"İki dal şarkıyı, ezgili sesi ve kulağa hoş gelen işitsel ürünü kapsar."},{"boundary_match":"partial","distinction":"Komşu dal algılama eylemini anlatır; bu dal algılanan sesin hoş ve çoğunlukla ezgili niteliğini ya da onu söyleyen icracıyı anlatır.","focus_only":"Sesin hoş veya ezgili olması ya da şarkı niteliği taşıması gerekir.","gloss":"hoş ses ile genel işitme","neighbor_only":"Hoşluk şartı olmadan herhangi bir sesin duyulması veya dinlenmesi yeterlidir.","neighbor_ref":"root_000741/B001","relation_type":"near_neighbor","shared_zone":"Hoş ses ve şarkı da kulakla algılanıp dinlenir."}],"source_phrase_ar":"المسمعة المغنية (maqayis;sihah)؛ السماع الغناء (ayn)؛ السماع اسم ما استلذت الأذن من صوت حسن (tahdhib)؛ المسمعة القينة المغنية (ayn)","source_summary":"Kaynaklar şarkı ve kulağa hoş gelen güzel ses anlamını, bu sesi icra eden kadın şarkıcı adıyla birlikte sunar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الغناء والصوت الحسن المستلذ وما يقوم به المغني أو القينة","what_is_not_ar":"ليس مطلق السماع ولا الصيت بين الناس"},"support_links":["sup_7a4cc0ca2df710cba60d"]},{"boundary":"Temel gönderim kova veya su kabındaki taşıma ve dengeleme parçasıdır; yan, uzantı ve sepet tahtası kullanımları ayrı türlerdir.","branch_kind":"mixed_non_bare","branch_ref":"root_000741/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"taşıma kabının sap veya denge parçası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Parça bir taşıma kabını tutmaya, bağlamaya veya yükünü dengelemeye yarar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Parça halka, iç sap, kabın yanı, sapın kaba uzanan bölümü veya sepet tahtası olarak tanımlanabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen söz öbeği kovaya bu parçayı eklemeyi veya saplarını yükü hafifletecek biçimde düzenlemeyi bildirir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kova, büyük su kabı ve yük sepetindeki farklı parça türlerini ortak taşıma ve dengeleme işlevi altında toplar.","boundary_detail":"Temel gönderim kova veya su kabındaki taşıma ve dengeleme parçasıdır; yan, uzantı ve sepet tahtası kullanımları ayrı türlerdir.","branch_image_ar":"مِسمع الدلو والغرب","concept_gloss":"taşıma kabının sap veya denge parçası","contextual_glosses":[{"applicability":"Parça kovanın tutulduğu halka veya iç taraftaki sap olduğunda en doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su kabının yanı, sap uzantısı ve sepet tahtası türlerini dışarıda bırakır.","preserves":"Kovayı tutmaya yarayan sap veya halka işlevini korur."},"facet_ids":["F001","F002"],"text":"kova sapı","usage_role":"general"},{"applicability":"Ettirgen söz öbeği kovaya taşıma parçası eklemeyi veya saplarını bağlamayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçanın ad olarak kullanıldığı ve yalnız bağlama bildiren örnekleri tam kapsamaz.","preserves":"Kovaya işlevsel taşıma parçası ekleme eylemini korur."},"facet_ids":["F003"],"text":"kovaya sap takmak","usage_role":"contextual"}],"definition":"Kova, büyük su kabı veya benzeri bir taşıma kabında tutma, bağlama ya da yükü dengeleme işlevi gören halka, sap, yan parça veya tahta elemandır. Yapma bildiren söz öbeği, kovaya böyle bir parça eklemeyi ya da saplarını yükü hafifletecek biçimde bağlamayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Parça bir taşıma kabını tutmaya, bağlamaya veya yükünü dengelemeye yarar."},{"facet_id":"F002","role":"source_variant","statement":"Parça halka, iç sap, kabın yanı, sapın kaba uzanan bölümü veya sepet tahtası olarak tanımlanabilir."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen söz öbeği kovaya bu parçayı eklemeyi veya saplarını yükü hafifletecek biçimde düzenlemeyi bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Canlı bedenindeki işitme organı anlamını ekler.","collision":"Kulak ve kulak açıklığı dalıyla karışır.","fit":"displacement","loses":"Taşıma, bağlama ve yük dengeleme işlevlerini kaybeder.","preserves":"Parçanın kulağa benzetilen biçimini çağrıştırır."},"text":"kulak"}],"identity_rationale":"Kaynak sözü kova ve büyük su kabındaki halka ya da sapı temel alırken, aynı adın kabın yanları, sapın kaba uzanan bölümü ve yük sepetindeki iki tahta için de kullanıldığını gösterir. Dal doğrudur, ancak bütün parçalar tek bir biçimsel parça sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kova veya su kabının yükü dengeleyen sapı ya da halkası"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"büyük su kabının iki yanı veya yük sepetinin iki taşıyıcı tahtası"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kovaya sap takmak veya saplarını yükü hafifletecek biçimde bağlamak"}],"lexicalization_note":"Yalın parça adları ile kovaya bu parçayı takmayı veya saplarını bağlamayı bildiren söz öbeği ayrılır; anlam kulağa genellenmez.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; tek saplı kova ile büyük su kabı, parça ve bütün ayrımını en açık gösteren komşulardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal kabın bir parçasını adlandırır; komşu dal ise bir sap özelliğiyle tanımlanan kova türünün bütününü adlandırır.","focus_only":"Gönderim kovanın sapına, halkasına veya yükü dengeleyen parçasına yönelir.","gloss":"kova sapı ile tek saplı kova","neighbor_only":"Gönderim tek saplı belirli bir kova türüne yönelir.","neighbor_ref":"root_000737/B011","relation_type":"same_field","shared_zone":"İki dal kova ve onu taşımaya yarayan sap düzeni alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal tutma ve dengeleme işlevli parçaya, komşu dal ise bu parçayı taşıyan büyük kabın kendisine gönderimde bulunur.","focus_only":"Kap üzerindeki sap, halka, yan veya taşıyıcı tahta gösterilir.","gloss":"kap parçası ile büyük su kabı","neighbor_only":"Büyük ve tam kova ya da su taşıma kabının bütünü gösterilir.","neighbor_ref":"root_001077/B002","relation_type":"same_field","shared_zone":"İki dal büyük su kabı ve onun taşınması bağlamını paylaşır."}],"source_phrase_ar":"المسمع كالأذن للغرب (maqayis)؛ مسمع الدلو والغرب عروة في وسطه (ayn;sihah)؛ المسمع من المزادة ما جاوز خرت العروة إلى الظرف (ayn)؛ المسمعان جانبا الغرب (tahdhib)؛ المسمع عروة في داخل الدلو (tahdhib)؛ حلقة مسمع الغرب (mufradat)","source_summary":"Kaynaklar taşıma kabındaki halka veya sapı ortak merkez olarak verir; yan parça, sap uzantısı ve sepet tahtası tanımları bu araçsal parçanın değişik gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العروة أو الجانب أو الخشبة في الدلو أو الغرب أو المزادة أو الزبيل مما يعدل أو يخفف الحمل","what_is_not_ar":"ليس الأذن ولا خرق الأذن وإن شبه بها"},"support_links":[]},{"boundary":"Dal, kişiyi bağlayan ayak bağı veya bağı anlatır; aynı biçimli kova parçası ve kulak anlamları bunun dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000741/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"ayak bağı veya hareket kısıtlayıcı bağ","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç kişinin hareketini sınırlayan bir bağ veya ayak bağıdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkili biçim, boyun bağıyla birlikte kullanılan kalıpta bağlanmış kişiyi betimler."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi fiziksel olarak bağlayıp hareketini sınırlayan araç çekirdeğini eksiksiz karşılar.","boundary_detail":"Dal, kişiyi bağlayan ayak bağı veya bağı anlatır; aynı biçimli kova parçası ve kulak anlamları bunun dışındadır.","branch_image_ar":"المِسمع قيد والقيد مسمعان","concept_gloss":"ayak bağı veya hareket kısıtlayıcı bağ","contextual_glosses":[{"applicability":"İki bağ ile boyna geçirilen tahta bağın birlikte anıldığı kalıpta kişinin durumunu açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayak bağlarıyla boyun bağının birlikte oluşturduğu bağlanmışlık durumunu korur."},"facet_ids":["F001","F002"],"text":"bağlanmış ve boyunduruklanmış","usage_role":"explanatory"}],"definition":"Bir kişiyi hareket edemez hâle getirmek için kullanılan ayak bağı veya bağdır; ikili biçimi boyna geçirilen tahta bağla birlikte kişinin bağlanmış durumunu anlatan bir kalıpta geçer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç kişinin hareketini sınırlayan bir bağ veya ayak bağıdır."},{"facet_id":"F002","role":"associated_use","statement":"İkili biçim, boyun bağıyla birlikte kullanılan kalıpta bağlanmış kişiyi betimler."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Su kabını tutma ve dengeleme işlevini ekler.","collision":"Taşıma kabının sap veya denge parçası dalıyla karışır.","fit":"displacement","loses":"Kişiyi bağlama ve hareketini kısıtlama işlevini kaybeder.","preserves":"Aynı biçimli araç parçası adını çağrıştırır."},"text":"kova sapı"}],"identity_rationale":"Kaynak sözü ilgili adı doğrudan bir bağ ve ayak bağı adı olarak verir; ikili biçimin boyun bağıyla birlikte kullanılması da kişinin bağlanmış olduğunu gösterir. Dal çerçevesi bu araç ve durum ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayak bağı veya bağlama aracı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki ayak bağı ve bir boyun bağıyla bağlanmış"}],"lexicalization_note":"Yalın bağ adı ile iki bağın boyun bağıyla birlikte geçtiği kalıp ayrı tutulur; araç adı genel olarak her tür engelleme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; boyun bağı ile daha genel halka biçimli bağ, bu dar araç adının en yakın ve öğretici karşılıklarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bağı veya ayak bağını adlandırır; komşu dal boyna geçirilen tahta bağı ve onunla bağlanmış kişiyi adlandırır.","focus_only":"Özellikle ayak bağı ve bunun ikili biçimi öne çıkar.","gloss":"ayak bağı ile boyun bağı","neighbor_only":"Boyna geçirilen tahta bağın kendisi ve onu taşıyan kişi öne çıkar.","neighbor_ref":"root_000643/B007","relation_type":"near_synonym","shared_zone":"Her iki dal insanı fiziksel olarak bağlayıp hareketini sınırlayan araçları kapsar."},{"boundary_match":"partial","distinction":"Bu dal dar bir bağ adıdır; komşu dal halka biçimli bağın malzemesini, bedendeki yerini ve benzetmeli engelleme kullanımlarını daha geniş biçimde kapsar.","focus_only":"Tanıklık, bağ adı ile iki bağ ve boyun bağı kalıbına özgüdür.","gloss":"bağ ile halka biçimli bağ","neighbor_only":"Demir veya kayıştan halka, eli boyna bağlama ve benzetmeli engelleme anlamları da kapsanır.","neighbor_ref":"root_001102/B006","relation_type":"near_synonym","shared_zone":"İki dal bedeni bağlayarak hareketi engelleyen fiziksel araçları kapsar."}],"source_phrase_ar":"من أسماء القيد المسمع؛ ولي مسمعان وزمارة؛ مسمعا مزمرا أي مقيدا مسوجرا","source_summary":"Tek kaynaklı kanıt, sözcüğü bir bağ adı olarak verir ve ikili biçimini boyun bağıyla birlikte bağlanmışlık bildiren bir söyleyişte kullanır.","sources":["TA"],"what_is_ar":"القيد وما يقيد به الرجل ويقرن بالساجور في التعبير","what_is_not_ar":"ليس مِسمع الدلو ولا الأذن"},"support_links":[]},{"boundary":"Tarihsel ad, kurt ile sırtlan arasında tasarlanan yırtıcıyı gösterir; keskin işitme üzerine söz yalnız bu hayvana bağlı kalıptır.","branch_kind":"mixed_non_bare","branch_ref":"root_000741/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"kurt ile sırtlan arasında sayılan yırtıcı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvan kurt ve sırtlanla ilişkilendirilen birleşik veya ara bir yırtıcı olarak tanımlanır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tanım onu özellikle kurdun sırtlandan olan yavrusu sayar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın adı, keskin işitmeyi anlatan bir karşılaştırma kalıbında kullanılır."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarihsel kaynaklardaki melez veya yavru tanımlarını kesin tür iddiasına dönüştürmeden ortak çekirdekte toplar.","boundary_detail":"Tarihsel ad, kurt ile sırtlan arasında tasarlanan yırtıcıyı gösterir; keskin işitme üzerine söz yalnız bu hayvana bağlı kalıptır.","branch_image_ar":"السَّمْع ولد الذئب والضبع","concept_gloss":"kurt ile sırtlan arasında sayılan yırtıcı","contextual_glosses":[{"applicability":"Kaynak anlatımı hayvanı özellikle kurt ile sırtlanın birleşmesinden doğan yavru olarak verdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca ikisi arasında bir yırtıcı sayıldığı daha genel tanımı dışarıda bırakır.","preserves":"Kurt ve sırtlan arasında yavru bağı kuran tanımı korur."},"facet_ids":["F002"],"text":"kurt ile sırtlanın yavrusu sayılan hayvan","usage_role":"explanatory"},{"applicability":"Hayvanın adıyla kurulan karşılaştırma sözü olağanüstü güçlü işitmeyi nitelediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın kendisini adlandıran yalın kullanımı dışarıda bırakır.","preserves":"Karşılaştırma kalıbındaki keskin işitme özelliğini korur."},"facet_ids":["F003"],"text":"çok keskin işiten","usage_role":"contextual"}],"definition":"Tarihsel anlatımda kurt ile sırtlan arasında bir yırtıcı ya da kurdun sırtlandan olan yavrusu sayılan hayvandır. Bu hayvana bağlı bir karşılaştırma sözü, çok keskin işitmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvan kurt ve sırtlanla ilişkilendirilen birleşik veya ara bir yırtıcı olarak tanımlanır."},{"facet_id":"F002","role":"source_variant","statement":"Bir tanım onu özellikle kurdun sırtlandan olan yavrusu sayar."},{"facet_id":"F003","role":"associated_use","statement":"Hayvanın adı, keskin işitmeyi anlatan bir karşılaştırma kalıbında kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnız kurdu adlandıran komşu dallarla karışır.","fit":"narrowing","loses":"Sırtlanla kurulan ara tür veya yavru ilişkisini kaybeder.","preserves":"Hayvanın ilişkilendirildiği yırtıcılardan birini korur."},"text":"kurt"}],"identity_rationale":"Kaynak sözü hayvanı kimi yerde kurt ile sırtlan arasında bir yırtıcı veya melez, kimi yerde kurdun sırtlandan olan yavrusu diye tanımlar. Dal korunabilir, ancak bu tanımlar tek ve kesin bir çağdaş hayvan sınıflandırması gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"kurt ile sırtlan arasında sayılan yırtıcı veya onların yavrusu"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"o yırtıcıdan bile daha keskin işiten"}],"lexicalization_note":"Yalın hayvan adı ile onun keskin işitmesini örnek veren karşılaştırma kalıbı ayrılır; kalıp genel işitme anlamına dönüştürülmez.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel yırtıcı sınıfı ile doğrudan kurt adı, tarihsel hayvanın kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli ve tarihsel olarak kurt ile sırtlana bağlanan bir hayvan adıdır; komşu dal birçok türü kapsayan genel yırtıcı sınıfıdır.","focus_only":"Kurt ve sırtlan arasında sayılan belirli tarihsel hayvan adı gösterilir.","gloss":"belirli melez yırtıcı ile yırtıcı hayvan","neighbor_only":"Aslan, kurt, kaplan ve benzerlerinin tümünü kapsayan genel yırtıcı hayvan sınıfı gösterilir.","neighbor_ref":"root_000669/B002","relation_type":"near_neighbor","shared_zone":"Bu dalın gösterdiği hayvan da genel yırtıcı hayvan alanına yerleştirilir."},{"boundary_match":"field_only","distinction":"Bu dal kurtla sırtlan arasında ayrı bir hayvanı anlatır; komşu dal ise belirli bir dil kullanımında yalnız kurdun başka adıdır.","focus_only":"Ad kurt ile sırtlan arasında düşünülen yırtıcıya veya yavruya verilir.","gloss":"ara yırtıcı ile kurt adı","neighbor_only":"Ad bazı ağızlarda doğrudan kurda verilir.","neighbor_ref":"root_000190/B003","relation_type":"same_field","shared_zone":"İki dal kurtla ilişkilendirilen tarihsel hayvan adlarını içerir."}],"source_phrase_ar":"السمع ولد الذئب من الضبع (maqayis;tahdhib)؛ السمع سبع بين الذئب والضبع (ayn)؛ السمع سبع مركب (sihah)؛ أسمع من السمع الأزل (sihah)","source_summary":"Kaynaklar adı kurt ile sırtlan arasında düşünülen bir yırtıcıya verir; tanım melez hayvan ile kurdun sırtlandan yavrusu anlatımları arasında değişir ve keskin işitme sözü buna eklenir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"السَّمْع سبع مركب أو ولد الذئب من الضبع وما يضرب به المثل في شدة السمع","what_is_not_ar":"ليس السمع الحاسة ولا الشهرة"},"support_links":[]},{"boundary":"Anlam yalnız bu kalıptaki kötü haber dileğine bağlıdır; genel işitme, ün veya haber bildirme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_000741/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"duyulsun ama bana ulaşmasın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü veya istenmeyen haberin varlığı işitme yoluyla kabul edilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dilek, haberin konuşana ulaşmaması ve onu bulmaması yönündedir."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İstenmeyen haberin işitilmesi ile konuşana erişmemesi dileğini aynı anda doğal Türkçeyle verir.","boundary_detail":"Anlam yalnız bu kalıptaki kötü haber dileğine bağlıdır; genel işitme, ün veya haber bildirme anlamına genişletilemez.","branch_image_ar":"سَمْع لا بَلَغ","concept_gloss":"duyulsun ama bana ulaşmasın","contextual_glosses":[{"applicability":"Bir felaket veya istenmeyen olay haberi karşısında, onun uzakta kalmasını dileyen söz olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kötü haber, duyulma ve konuşana ulaşmama dileğini birlikte korur."},"facet_ids":["F001","F002"],"text":"kötü haber duyulsun da beni bulmasın","usage_role":"explanatory"}],"definition":"Hoşa gitmeyen bir haberin duyulmasını, fakat konuşana kadar ulaşıp onu etkilememesini dileyen kalıp sözdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü veya istenmeyen haberin varlığı işitme yoluyla kabul edilir."},{"facet_id":"F002","role":"core","statement":"Dilek, haberin konuşana ulaşmaması ve onu bulmaması yönündedir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Haberin kendisiyle ona karşı söylenen dileği birbirine karıştırır.","fit":"narrowing","loses":"Haberin duyulup konuşana ulaşmamasını dileyen söz edimini kaybeder.","preserves":"Söyleyişin ortaya çıktığı olumsuz haber bağlamını korur."},"text":"kötü haber"}],"identity_rationale":"Kaynak sözü, hoş karşılanmayan bir haber için onun işitilmesini fakat konuşana ulaşmamasını dileyen kalıbı açıkça verir. Dal çerçevesi bu dilek ve haber aktarımı sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"duyulsun ama bana ulaşmasın"}],"lexicalization_note":"Tanım yalnız sabit söyleyişin bütününe aittir; parçalarından yalın kök için yeni bir duyma veya ulaşma anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; aynı kalıbı veren eşanlamlı dal ve genel haber dalı, söyleyişin kimliğini ve sınırını yeterince açıklar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek, koşul ve sözün kullanım sınırı bakımından anlamlı bir ayrım bulunmaz.","focus_only":null,"gloss":"duyulsun ama ulaşmasın dileği","neighbor_only":null,"neighbor_ref":"root_000151/B009","relation_type":"synonym","shared_zone":"İki dal da hoşa gitmeyen haberin duyulup konuşana ulaşmamasını dileyen aynı kalıp sözü anlatır."},{"boundary_match":"partial","distinction":"Bu dal habere karşı söylenen korunma dileğidir; komşu dal haberin kendisini ve onun aktarılmasını anlatır.","focus_only":"Kötü haberin konuşana ulaşmamasını dileyen kalıp söz bulunur.","gloss":"haber dileği ile haber","neighbor_only":"Önemli veya yararlı bilgi taşıyan haberin kendisi ve onu bildirme eylemleri bulunur.","neighbor_ref":"root_001464/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir haberin kişiden kişiye ulaşması alanında buluşur."}],"source_phrase_ar":"اللهم سمعا لا بلغا (sihah)؛ سمع لا بلغ معناه يسمع ولا يبلغ (tahdhib)؛ أسمع بالدواهي ولا تبلغني (tahdhib)","source_summary":"Kaynaklar kalıbı, kötü haberin duyulup yine de söyleyene ulaşmamasını dileyen korunma sözü olarak ortak biçimde açıklar.","sources":["SI","TA"],"what_is_ar":"الدعاء أو القول في الخبر المكروه أن يسمع به ولا يبلغ صاحبه","what_is_not_ar":"ليس الصيت العام ولا السماع الحسي وحده"},"support_links":[]},{"boundary":"Küçük başlılık, ince uzun yapı, atılgan çeviklik ve kötülük kaynakta yan yana gelen ayrı niteleme türleridir.","branch_kind":"bare","branch_ref":"root_000741/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"küçük başlı, ince uzun veya çevik atılgan kimse","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Fiziksel nitelemede kişinin başı küçük veya bedeni ince ve uzundur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Davranışsal nitelemede kişi çevik, atılgan ve işe hızla girişen biridir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir kullanım aynı sözü kötü bir varlığın adı olarak verir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözcüğün kadın için kullanılan ayrı bir biçimi de tanıklanmıştır."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan betimlemelerindeki fiziksel ve davranışsal türleri birbirine zorunlu bağlamadan birlikte gösterir.","boundary_detail":"Küçük başlılık, ince uzun yapı, atılgan çeviklik ve kötülük kaynakta yan yana gelen ayrı niteleme türleridir.","branch_image_ar":"سَمْعَمَع في الهيئة والخبث","concept_gloss":"küçük başlı, ince uzun veya çevik atılgan kimse","contextual_glosses":[{"applicability":"Söz bir insanın baş veya beden yapısını betimlediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çevik atılganlık ve kötü varlık kullanımlarını dışarıda bırakır.","preserves":"Tanıklanan fiziksel görünüş özelliklerini korur."},"facet_ids":["F001","F004"],"text":"küçük başlı veya ince uzun","usage_role":"contextual"},{"applicability":"Söz kişinin davranışını, hızla işe girişmesini ve kararlı ilerleyişini nitelediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel görünüş ve kötü varlık kullanımlarını dışarıda bırakır.","preserves":"Davranışsal çeviklik ve atılganlık yönünü korur."},"facet_ids":["F002"],"text":"çevik ve atılgan","usage_role":"contextual"},{"applicability":"Sözcük insan görünüşünü değil, kötülüğüyle nitelenen insan dışı bir varlığı adlandırdığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların fiziksel ve davranışsal niteliklerini dışarıda bırakır.","preserves":"Kötü varlık adı olarak tanıklanan kullanımı korur."},"facet_ids":["F003"],"text":"kötü varlık","usage_role":"explanatory"}],"definition":"Bir insanı küçük başlı veya ince uzun yapılı, kimi kullanımda da çevik ve atılgan diye niteleyen sözdür; ayrı bir kullanımda kötü bir varlığı adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Fiziksel nitelemede kişinin başı küçük veya bedeni ince ve uzundur."},{"facet_id":"F002","role":"source_variant","statement":"Davranışsal nitelemede kişi çevik, atılgan ve işe hızla girişen biridir."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir kullanım aynı sözü kötü bir varlığın adı olarak verir."},{"facet_id":"F004","role":"associated_use","statement":"Sözcüğün kadın için kullanılan ayrı bir biçimi de tanıklanmıştır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynağın vermediği genel boy kısalığını ekler.","collision":"Kısa veya küçük bedenli kişileri anlatan komşu dallarla karışır.","fit":"displacement","loses":"Küçük baş, ince uzun yapı, çeviklik ve kötülük özelliklerini kaybeder.","preserves":"Beden ölçüsüne ilişkin bir niteleme olmasını korur."},"text":"kısa boylu"}],"identity_rationale":"Kaynak sözü aynı niteleme biçimini küçük başlı, ince uzun, çevik ve atılgan erkek, kadın biçimi ve kötü yaratık gibi farklı betimlemelerle verir. Dal korunabilir, ancak bu nitelikler tek bir zorunlu fiziksel ve ahlaki özellik kümesi gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"küçük başlı, ince uzun, çevik atılgan veya kötü"}],"lexicalization_note":"Tanım tanıklanan niteleme biçiminin ayrı fiziksel ve davranışsal kullanımlarını korur; kökün genel işitme anlamından açıklama türetmez.","neighbor_coverage_note":"Tüm adaylar incelendi; ince beden ve küçük beden nitelemeleri, kaynakta yan yana gelen fiziksel özelliklerin gerçek sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal inceliği küçük başlılık ve davranışsal atılganlık gibi ayrı kullanımlarla birlikte verir; komşu dal doğrudan beden inceliği ve hafifliğine odaklanır.","focus_only":"Küçük başlılık, çevik atılganlık ve kötü varlık kullanımları da bulunur.","gloss":"ince yapı ile çok yönlü niteleme","neighbor_only":"Hafif beden yapısı, kısa boy ve yetersiz beslenmeden doğan incelik ayrıntıları bulunur.","neighbor_ref":"root_000642/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir insanın ince veya narin beden yapısını betimleyebilir."},{"boundary_match":"partial","distinction":"Bu dal başın küçüklüğünü veya bedenin ince uzunluğunu anlatır; komşu dal genel beden kısalığına ya da küçüklüğüne yönelir.","focus_only":"Küçük baş, ince uzun yapı ve çevik atılganlık gösterilebilir.","gloss":"küçük baş ile küçük beden","neighbor_only":"Kısa veya küçük beden ve devenin zayıflığı gösterilir.","neighbor_ref":"root_000286/B010","relation_type":"near_neighbor","shared_zone":"İki dal insanın küçük görünen bir fiziksel özelliğini niteleyebilir."}],"source_phrase_ar":"السمعمع الصغير الرأس (sihah;tahdhib)؛ السمعمع من الرجال المنكمش الماضي (tahdhib)؛ الشيطان الخبيث يقال له سمعمع (tahdhib)؛ السمعمع من الرجال الدقيق الطويل (tahdhib)؛ امرأة سمعمعة (tahdhib)","source_summary":"Toplu kanıt aynı niteleme sözünü küçük başlılık, ince uzun yapı, çevik atılganlık ve kötülük için verir; bunlar tek bir birleşik özellik değil, yan yana tanıklanan kullanımlardır.","sources":["SI","TA"],"what_is_ar":"صفة سمعمع وسمعمعة في صغر الرأس أو الدقة والطول أو الانكماش والمضاء أو الخبث","what_is_not_ar":"ليس السمع الحاسة ولا ولد الذئب والضبع"},"support_links":[]},{"boundary":"Anlam yalnız kadın için kullanılan bu birleşik nitelemeye bağlıdır; genel dinleme, bakma veya tahminde bulunma anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000741/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"bakıp dinlediği hâlde göremeyince tahmin eden kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın bilgi edinmek için dinler veya çevresine bakar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Algı girişimi belirgin bir nesne veya kanıt sağlamaz."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kesin görgü bulunmayınca sonuç tahmin yoluyla kurulur."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın gönderimini, algı girişimini, sonuçsuzluğu ve tahmine geçişi eksiksiz biçimde korur.","boundary_detail":"Anlam yalnız kadın için kullanılan bu birleşik nitelemeye bağlıdır; genel dinleme, bakma veya tahminde bulunma anlamı değildir.","branch_image_ar":"سَمْعَنَة نَظَرْنَة في التظنّي","concept_gloss":"bakıp dinlediği hâlde göremeyince tahmin eden kadın","contextual_glosses":[{"applicability":"Birleşik niteleme, araştırdığı hâlde açık kanıt bulamayıp tahmine yönelen kadını açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinleme ve bakma yollarını ayrı ayrı açıkça söylemez.","preserves":"Sonuçsuz araştırmadan tahmine geçişi ve kadın gönderimini korur."},"facet_ids":["F002","F003"],"text":"bir iz bulamayınca varsayımla hareket eden kadın","usage_role":"explanatory"}],"definition":"Dinleyip çevresine bakmasına karşın belirgin bir şey göremediğinde, kesin bilgi yerine tahmine göre hareket eden kadını niteleyen birleşik sözdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın bilgi edinmek için dinler veya çevresine bakar."},{"facet_id":"F002","role":"core","statement":"Algı girişimi belirgin bir nesne veya kanıt sağlamaz."},{"facet_id":"F003","role":"core","statement":"Kesin görgü bulunmayınca sonuç tahmin yoluyla kurulur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Sürekli kuşku duyan bir kişilik özelliği ekler.","collision":"Genel kuşku ve zayıf inanış dallarıyla karışır.","fit":"displacement","loses":"Dinleme, bakma, görememe ve ardından tahmine geçme sürecini kaybeder.","preserves":"Kesin bilgi bulunmayan zihinsel durumu çağrıştırır."},"text":"kuşkucu kadın"}],"identity_rationale":"Kaynak sözü kadın için kullanılan birleşik nitelemeyi ve onun dinleyip bakmasına rağmen bir şey göremeyince varsayımla hareket etmesini açıkça verir. Dal çerçevesi algı girişimi, sonuçsuzluk ve tahmin aşamalarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"dinleyip baktığı hâlde bir şey göremeyince tahmin eden kadın"}],"lexicalization_note":"Tanım birleşik nitelemenin bütününe ve kadın gönderimine bağlıdır; parçalarından yalın kök için genel tahmin anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kuşku ile genel tahmin dalları, bu birleşik ve koşula bağlı kadın nitelemesinin sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir kadın nitelemesi ve sonuçsuz algı süreci içerir; komşu dal ise genel kuşku veya zayıf inanışı anlatır.","focus_only":"Kadın için kullanılan birleşik niteleme, dinleme veya bakma girişimi ve görememe koşuluna bağlıdır.","gloss":"koşullu tahmin ile genel kuşku","neighbor_only":"Zayıf belirtiye dayanan genel ve kesin olmayan inanış herhangi bir kişi veya algı sırasıyla sınırlı değildir.","neighbor_ref":"root_000969/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da kesin bilgi bulunmaz ve kişi zayıf dayanakla bir sonuca yönelir."},{"boundary_match":"partial","distinction":"Bu dal özel bir algı sırasına ve kadın nitelemesine bağlıdır; komşu dal koşul ve kişi sınırlaması olmayan genel tahmini anlatır.","focus_only":"Tahmin, dinleyip baktıktan sonra hiçbir şey görememe koşulunda ortaya çıkar.","gloss":"sonuçsuz gözlemden tahmine geçmek","neighbor_only":"Bir şeyi zihinde yaklaşık değerlendirme veya kesin olmayan beklenti genel biçimde kapsanır.","neighbor_ref":"root_000318/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kesinlik taşımayan bir zihinsel değerlendirme içerir."}],"source_phrase_ar":"امرأة سمعنة نظرنة (sihah;tahdhib)؛ إذا تسمعت أو تبصرت فلم تر شيئا تظنته تظنيا (sihah)؛ إذا سمعت أو تبصرت فلم تر شيئا تظنت تظنيا (tahdhib)","source_summary":"Kaynaklar birleşik nitelemeyi, dinleme veya bakma girişiminden sonuç alamayıp kesin bilgi yerine tahminde bulunan kadın için ortak biçimde verir.","sources":["SI","TA"],"what_is_ar":"المرأة التي تسمع أو تبصر ثم لا ترى شيئا فتعمل بالظن","what_is_not_ar":"ليس مطلق الاستماع ولا الفهم"},"support_links":[]},{"boundary":"Anlam boş arazinin kendisinden çok, orada kişiyi duyacak veya görecek başka hiç kimsenin bulunmaması koşuludur.","branch_kind":"collocation","branch_ref":"root_000741/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"kimsenin görüp duymadığı boş arazide","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olay açık veya boş bir arazi ortamında gerçekleşir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çevrede kişiyi görecek veya sözünü duyacak başka hiç kimse yoktur."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıp, bu arazide yürüyen veya orada karşılaşılan kişi için kullanılır."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer, insan yokluğu ve kişinin görülüp duyulmaması koşullarını söz öbeğine bağlı biçimde birlikte karşılar.","boundary_detail":"Anlam boş arazinin kendisinden çok, orada kişiyi duyacak veya görecek başka hiç kimsenin bulunmaması koşuludur.","branch_image_ar":"بين سمع الأرض وبصرها","concept_gloss":"kimsenin görüp duymadığı boş arazide","contextual_glosses":[{"applicability":"Kişinin çevresinde onu görecek veya duyacak hiç kimse olmadan yürümesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görülmeme ve duyulmama koşullarını ayrı ayrı açıkça söylemez.","preserves":"Issız yer ve çevrede başka insan bulunmaması durumunu korur."},"facet_ids":["F001","F002","F003"],"text":"ıssız arazide tek başına","usage_role":"contextual"}],"definition":"Kişinin, kendisini duyacak veya görecek hiç kimsenin bulunmadığı boş ve ıssız arazide yürümesi ya da orada karşılaşılması durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olay açık veya boş bir arazi ortamında gerçekleşir."},{"facet_id":"F002","role":"core","statement":"Çevrede kişiyi görecek veya sözünü duyacak başka hiç kimse yoktur."},{"facet_id":"F003","role":"example","statement":"Kalıp, bu arazide yürüyen veya orada karşılaşılan kişi için kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Belirli bir iklim ve arazi türü anlamı ekler.","collision":"Genel çorak veya bitkisiz arazi dallarıyla karışır.","fit":"narrowing","loses":"Çevrede kişiyi görecek veya duyacak hiç kimse bulunmaması koşulunu kaybeder.","preserves":"Boş ve açık arazi görünümünü kısmen korur."},"text":"çöl"}],"identity_rationale":"Kaynak sözü, çevrede konuşanı duyacak veya görecek hiç kimse bulunmayan boş arazide yürüme ya da karşılaşma durumunu açıklar. Dalın araziyi gerçek anlamda duyan bir varlık saymayan kalıpsal yorumu kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kimsenin görüp duymadığı boş arazide"}],"lexicalization_note":"Tanım yalnız verilen yer bildiren söz öbeğine bağlıdır; kökün yalın biçimine arazi, boşluk veya yalnızlık anlamı yüklenmez.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel insansız arazi ve herhangi bir yerde insan yokluğu, söz öbeğinin olay ve tanıksızlık sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir söz öbeği içinde kişinin ıssız arazideki hareketini ve tanıksızlığını anlatır; komşu dal yalnız toprağın insanlardan boş olma durumudur.","focus_only":"Boş arazide yürüme veya karşılaşma ve kişinin görülüp duyulmaması kalıba bağlıdır.","gloss":"ıssız arazide görünmeden yürümek","neighbor_only":"Toprağın insanlardan boş olması, verimli veya verimsiz oluşundan bağımsız genel bir durumdur.","neighbor_ref":"root_001006/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal insan bulunmayan bir araziyi kapsar."},{"boundary_match":"partial","distinction":"Bu dal hareket eden kişiyi ve algılayacak tanık bulunmamasını içerir; komşu dal yerin insansızlığını olay veya algı koşulu olmadan söyler.","focus_only":"Açık arazideki kişi ve onu görecek ya da duyacak kimse bulunmaması anlatılır.","gloss":"tanıksız yürüyüş ile insan yokluğu","neighbor_only":"Herhangi bir yerde insan veya oturan bulunmadığı genel bir yokluk kalıbıyla belirtilir.","neighbor_ref":"root_000503/B002","relation_type":"near_neighbor","shared_zone":"İki dal belirli bir yerde başka insan bulunmamasını bildirir."}],"source_phrase_ar":"تخرج بين سمع الأرض وبصرها؛ ليس معها أحد يسمع كلامها أو يبصرها إلا الأرض القفر؛ لقيته يمشي بين سمع الأرض وبصرها أي بأرض خلاء ما بها أحد","source_summary":"Tek kaynaklı kanıt, söz öbeğini kimsenin bulunmadığı boş arazide yürüme veya karşılaşma durumu olarak açıklar; görme ve duyma yokluğu çevredeki insanların yokluğudur.","sources":["TA"],"what_is_ar":"الخروج أو المشي في أرض خلاء لا أحد فيها يسمع أو يبصر","what_is_not_ar":"ليس السمع الحقيقي للأرض على ظاهره"},"support_links":[]},{"boundary":"Gönderim herhangi bir değneğe değil, iki öküzün bağlandığı tarım düzeneğindeki iki uzun çubuğa özgüdür.","branch_kind":"bare","branch_ref":"root_000741/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"öküz koşumundaki iki uzun çubuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Araç iki adet uzun çubuktan oluşur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çubuklar iki öküzü birbirine bağlayan tarım düzeneğinin parçalarıdır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Düzenek toprağı sürme işinde kullanılır."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaların sayısını, biçimini, koşumdaki yerini ve tarımsal bağlamını kısa ve açık biçimde karşılar.","boundary_detail":"Gönderim herhangi bir değneğe değil, iki öküzün bağlandığı tarım düzeneğindeki iki uzun çubuğa özgüdür.","branch_image_ar":"السميعان من أدوات الحراثين","concept_gloss":"öküz koşumundaki iki uzun çubuk","contextual_glosses":[{"applicability":"Tarımsal düzeneğin parçaları uzman olmayan okuyucuya açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çift öküz, koşum, uzunluk ve çoğul parça özelliklerini korur."},"facet_ids":["F001","F002","F003"],"text":"çift öküz koşumunun uzun çubukları","usage_role":"explanatory"}],"definition":"Toprağı sürerken iki öküzü birlikte bağlayan düzeneğin içinde yer alan iki uzun çubuktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Araç iki adet uzun çubuktan oluşur."},{"facet_id":"F002","role":"core","statement":"Çubuklar iki öküzü birbirine bağlayan tarım düzeneğinin parçalarıdır."},{"facet_id":"F003","role":"core","statement":"Düzenek toprağı sürme işinde kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her amaçla kullanılabilen tek bir genel çubuk anlamını ekler.","collision":"Genel sopa ve değnek adlarıyla karışır.","fit":"broadening","loses":null,"preserves":"Uzun ve sert bir çubuk olma özelliğini korur."},"text":"sopa"}],"identity_rationale":"Kaynak sözü, toprağı sürmek için iki öküzü birbirine bağlayan düzenekte bulunan iki uzun değneği açıkça tanımlar. Dal çerçevesi parça sayısını, biçimini, yerini ve tarımsal işlevini eksiksiz korur.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"toprak sürmek için iki öküzün bağlandığı düzenekteki iki uzun çubuk"}],"lexicalization_note":"Tanım yalın araç adını yalnız tanıklanan tarım düzeneğine bağlar; genel değnek, mızrak veya kesme aracı anlamlarına genişletmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel değnek ile başka bir tarım aracı, biçim benzerliğine rağmen sayıyı, yeri ve işlevi açıkça ayırır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal sayısı, yeri ve tarımsal işlevi belirlenmiş iki araç parçasıdır; komşu dal yalnız genel bir değnek adıdır.","focus_only":"İki uzun çubuk, öküz koşumunun parçasıdır ve toprak sürmede kullanılır.","gloss":"koşum çubuğu ile değnek","neighbor_only":"Tek bir genel değnek adı verilir; tarımsal düzenek ve çift olma şartı yoktur.","neighbor_ref":"root_001223/B011","relation_type":"same_field","shared_zone":"İki dal uzun ve sert bir çubuk biçimindeki nesneleri adlandırır."},{"boundary_match":"field_only","distinction":"Bu dal öküzleri toprağı sürmek için bağlayan düzeneğin parçasıdır; komşu dal ürün yığınını işlemek için kullanılan demirli araçtır.","focus_only":"Çubuklar öküzleri bağlayan koşum düzeninde yer alır.","gloss":"sürme koşumu ile harman aracı","neighbor_only":"Demir parçalı araç harman yığınını dövmek veya çiğnetmek için kullanılır.","neighbor_ref":"root_000373/B015","relation_type":"same_field","shared_zone":"İki dal tarım işlerinde kullanılan uzun parçalı araçları anlatır."}],"source_phrase_ar":"السميعان من أدوات الحراثين؛ عودان طويلان في المقرن الذي يقرن به الثوران لحراثة الأرض","source_summary":"Tek kaynaklı kanıt, terimi iki öküzü toprağı sürmek için bağlayan düzeneğin içindeki iki uzun çubuk olarak tanımlar.","sources":["TA"],"what_is_ar":"عودان طويلان في المقرن الذي يقرن به الثوران للحراثة","what_is_not_ar":"ليس المسمعين بمعنى الأذنين ولا مسمعي القيد"},"support_links":[]},{"boundary":"Anlam yalnız bu birleşik adlarda beyindir; kulak, işitme gücü veya kulağın açıklığı bu dalın gönderimi değildir.","branch_kind":"non_bare","branch_ref":"root_000741/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","surface_ar":"تَسْمَعُ"}],"gloss":"beyin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim başın içindeki beyin organıdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak benzetmesinde başın delinerek beyne ulaşması görüntüsü kullanılır."}}],"root_ar":"س م ع","root_id":"root_000741","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birleşik ad başın içindeki organı gösterdiğinde doğrudan ve eksiksiz Türkçe karşılıktır.","boundary_detail":"Anlam yalnız bu birleşik adlarda beyindir; kulak, işitme gücü veya kulağın açıklığı bu dalın gönderimi değildir.","branch_image_ar":"أم السمع الدماغ","concept_gloss":"beyin","contextual_glosses":[{"applicability":"Birleşik adın yapısı veya başı delme benzetmesi açıklanırken organın yerini belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Organı ve baş içindeki konumunu açıkça korur."},"facet_ids":["F001","F002"],"text":"başın içindeki beyin","usage_role":"explanatory"}],"definition":"Belirli birleşik adlarda başın içinde bulunan beyni gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim başın içindeki beyin organıdır."},{"facet_id":"F002","role":"example","statement":"Kaynak benzetmesinde başın delinerek beyne ulaşması görüntüsü kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dış işitme organı anlamını ekler.","collision":"Kulak ve kulak açıklığı dalıyla karışır.","fit":"displacement","loses":"Başın içindeki beyin organı gönderimini kaybeder.","preserves":"İşitmeyle ilgili birleşik ad çağrışımını korur."},"text":"kulak"}],"identity_rationale":"Kaynak sözü iki yakın söz öbeğini doğrudan beyin anlamında verir ve başın delinmesi benzetmesinde aynı gönderimi sürdürür. Dalın beyin olarak yorumlanması kaynakla tam uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"beyin"}],"lexicalization_note":"Tanım yalnız birleşik beden parçası adının bütününe aittir; yalın köke genel beyin veya baş anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; beyin ve işitme yeri dalı ile beyne ulaşan yara dalı, organ adının kapsamını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnız birleşik adın beyin anlamıdır; komşu dal beynin kendisiyle birlikte işitmenin beyindeki yeri yorumunu da kapsar.","focus_only":"Gönderim birleşik ad içinde doğrudan beynin kendisidir.","gloss":"beyin ve işitme yeri","neighbor_only":"Beynin yanında işitmenin yerleştirildiği beyin bölgesi de gösterilebilir.","neighbor_ref":"root_000853/B002","relation_type":"near_synonym","shared_zone":"Her iki dal baş içindeki beyin organını gösterebilir."},{"boundary_match":"partial","distinction":"Bu dal organın adıdır; komşu dal organı çevreleyen bölgeyi ve ona kadar ulaşan yaralanma ile ilgili kişi ve araçları anlatır.","focus_only":"Birleşik ad doğrudan sağlam veya genel beyin organını gösterir.","gloss":"beyin ile beyne ulaşan yara","neighbor_only":"Beyni örten bölüm, ona ulaşan baş yarası, yaralı kişi ve başı ezen araç da kapsanır.","neighbor_ref":"root_000053/B003","relation_type":"near_neighbor","shared_zone":"İki dal başın içindeki beyin ve ona fiziksel erişim alanında buluşur."}],"source_phrase_ar":"أم السمع وأم السميع الدماغ؛ نقبن الحرة السوداء عنهم كنقب الرأس عن أم السميع","source_summary":"Tek kaynaklı kanıt birleşik adları doğrudan beyin diye açıklar ve başı delip beyne ulaşma görüntüsü taşıyan bir benzetmeyle kullanımı gösterir.","sources":["TA"],"what_is_ar":"أم السمع أو أم السميع بمعنى الدماغ","what_is_not_ar":"ليس الأذن ولا قوة السمع"},"support_links":[]},{"boundary":"Dal, sözün çirkinliğini veya sesin yüksekliğini değil, bir şeyin dikkate alınmamasını ya da geçersiz kılınmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001361/B001","candidate_links":[{"candidate_id":"cand_14d8928c037ce80960e8","lane":"micro"},{"candidate_id":"cand_24b485fa16f9a1ed8405","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"dikkate alınmayan veya geçersiz kılınan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey değersiz, gereksiz veya geçersiz görülür ve bu nedenle dikkate alınmaz, hesaba katılmaz ya da işlemden çıkarılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yemin bağlamında söz, kişinin içten ve kesin bir bağlanması bulunmadığı için bağlayıcı sayılmaz."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kan bedeli hesabında bazı deve yavruları sayıma alınmayan kalemler olarak değerlendirilir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir atın koşusu ciddi ve amaçlı bir koşu değilse bu niteleme kullanılabilir."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin değersiz sayılarak hesaba katılmaması veya etkin biçimde geçersiz kılınması çekirdeğini birlikte karşılar.","boundary_detail":"Dal, sözün çirkinliğini veya sesin yüksekliğini değil, bir şeyin dikkate alınmamasını ya da geçersiz kılınmasını anlatır.","branch_image_ar":"الشيء المطروح الذي لا يعتد به","concept_gloss":"dikkate alınmayan veya geçersiz kılınan şey","contextual_glosses":[{"applicability":"Sayı, hesap veya kan bedeli içinde bir kalemin değerlendirme dışı bırakıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etkin biçimde geçersiz kılma ve bağlayıcı olmayan yemin kapsamını dışarıda bırakır.","preserves":"Bir kalemin değerlendirme ve hesap dışında kalmasını korur."},"facet_ids":["F001","F003"],"text":"hesaba katılmayan","usage_role":"contextual"},{"applicability":"Kişinin içten ve kesin bir bağlanma kurmadan söylediği yemin için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeminin içten bağlanma bulunmadığı için bağlayıcı sayılmamasını korur."},"facet_ids":["F002"],"text":"bağlayıcı olmayan yemin","usage_role":"contextual"}],"definition":"Bir şeyi değersiz, gereksiz veya geçersiz sayarak dikkate ya da hesaba almama ve gerektiğinde onu bir sayıdan veya işlemden çıkarma anlamıdır. Bağlayıcı olmayan yemin, kan bedelinde sayılmayan kalem ve ciddi olmayan koşu bu çekirdeğin özel kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey değersiz, gereksiz veya geçersiz görülür ve bu nedenle dikkate alınmaz, hesaba katılmaz ya da işlemden çıkarılır."},{"facet_id":"F002","role":"specialization","statement":"Yemin bağlamında söz, kişinin içten ve kesin bir bağlanması bulunmadığı için bağlayıcı sayılmaz."},{"facet_id":"F003","role":"specialization","statement":"Kan bedeli hesabında bazı deve yavruları sayıma alınmayan kalemler olarak değerlendirilir."},{"facet_id":"F004","role":"example","statement":"Bir atın koşusu ciddi ve amaçlı bir koşu değilse bu niteleme kullanılabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi değersiz veya geçersiz sayarak dikkate almama çekirdeğini açıkça destekler. Yemin, kan bedeli hesabı, sayıdan çıkarma ve ciddi olmayan koşu bunun belirli yapılardaki gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dikkate alınmayan, hesaba katılmayan şey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"içten bağlanılmamış, bağlayıcı olmayan yemin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kan bedelinin hesabına katılmayan deve yavruları"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi geçersiz kılmak veya bir sözü boş ve gereksiz saymak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onu sayıdan çıkarmak ve hesaba katmamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"içten bağlanmadan yemin etmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ciddi ve amaçlı olmayan koşu"}],"lexicalization_note":"Tanım ortak değerlendirme çekirdeğini verir; yemin, kan bedeli, sayı ve koşu anlamları yalnızca tanıklanan yapılara bağlı tutulur.","neighbor_coverage_note":"Adaylar içinden, sözün değersizliğiyle karışabilecek kötü söz dalı ve sonuç bakımından yaklaşan ihmal dalı sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği değerlendirme dışı bırakmadır; komşu dalın çekirdeği ise sözün içeriğine veya niteliğine ilişkin olumsuz hükümdür.","focus_only":"Söz dışındaki şeyleri de hesaptan çıkarma, değersiz sayma ve geçersiz kılmayı kapsar.","gloss":"dikkate almama ile kötü söz","neighbor_only":"Sözün batıl, çirkin, açık saçık veya günahlı oluşunu anlatır.","neighbor_ref":"root_001361/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir sözün değer taşımadığı düşünülebilir."},{"boundary_match":"partial","distinction":"Bu dalda dışarıda kalma bir değer ya da geçerlilik hükmünün sonucudur; komşuda ise temel anlam bırakma, savsaklama veya unutmadır.","focus_only":"Değersiz sayma, hesaptan çıkarma ve hukuken bağlayıcı kabul etmeme değerlendirmesini taşır.","gloss":"geçersiz sayma ile ihmal","neighbor_only":"Bir işi eksik yapma, ihmal etme, unutma veya geride bırakma eylemini taşır.","neighbor_ref":"root_001145/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir şeyin fiilî işlem veya ilgi dışında kalmasıyla sonuçlanabilir."}],"source_phrase_ar":"اللغو ما لا يعتد به من أولاد الإبل في الدية (maqayis;sihah;mufradat)؛ لغو الأيمان ما لم تعقدوه بقلوبكم وما لا عقد عليه (maqayis;sihah;tahdhib;mufradat)؛ ألغيت هذه الكلمة أي رأيتها باطلا وفضلا وحشوا وما يلغى من الحساب (ayn;tahdhib)؛ ألغيت الشيء: أبطلته وألغاه من العدد: ألقاه منه (sihah;tahdhib)؛ فرسك لملاغي الجري إذا كان جريه غير جري جد (tahdhib)","source_summary":"Tanıklıklar, değersiz veya fazla görülerek dikkate alınmayan şeyi; bağlayıcı olmayan yemini; hesaptan çıkarılan kalemi; geçersiz kılma işlemini ve ciddi olmayan koşuyu aynı değerlendirme çekirdeği çevresinde toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ما لا يعتد به أو يطرح من الحساب أو العدد، ولغو اليمين غير المعقود بالقلب، وما لا يحسب في الدية، والإبطال والإلغاء، وما كان غير جد.","what_is_not_ar":"ليس الكلام القبيح لذاته، ولا رفع الصوت للتشويش، ولا اللهج باللغة أو الولوع بالشيء."},"support_links":["sup_cbdb00cc01191c440820","sup_ed169584d7a5e4698a8a"]},{"boundary":"Çekirdek batıl veya çirkin sözdür; ibadet konuşması sırasındaki sıradan söz söyleme anlamı yalnızca o belirli bağlamın uzantısıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001361/B002","candidate_links":[{"candidate_id":"cand_4f483aec6bdd1ef3809d","lane":"micro"},{"candidate_id":"cand_e2ad12629184a76caed3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"batıl veya çirkin söz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz batıl, çirkin, açık saçık, sövgü niteliğinde veya günaha yol açan içerik taşır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başkasını batıl veya çirkin söze katılmaya yöneltebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Haftalık toplu ibadet konuşması sürerken söz söylemek, içeriği ayrıca kötülenmeden bu adla nitelenir."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün gerçek dışı, çirkin, açık saçık, sövgü niteliğinde ya da günaha yol açan olumsuz içeriğini karşılar.","boundary_detail":"Çekirdek batıl veya çirkin sözdür; ibadet konuşması sırasındaki sıradan söz söyleme anlamı yalnızca o belirli bağlamın uzantısıdır.","branch_image_ar":"الكلام الباطل القبيح","concept_gloss":"batıl veya çirkin söz","contextual_glosses":[{"applicability":"Bir kişinin batıl, çirkin veya sövgü niteliğinde söz söylediği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkası üzerinde yöneltme etkisini ve ibadet bağlamına bağlı nötr konuşma uzantısını kapsamaz.","preserves":"Söz söyleme eylemini ve sözün olumsuz niteliğini korur."},"facet_ids":["F001"],"text":"boş ve kötü konuşmak","usage_role":"contextual"},{"applicability":"Yalnızca haftalık toplu ibadette yetkili kişinin konuşması sürerken araya sözle girme bağlamını açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli ibadet konuşması sürerken söz söyleme eylemini eksiksiz korur."},"facet_ids":["F003"],"text":"konuşma sürerken söz söylemek","usage_role":"explanatory"}],"definition":"Batıl, çirkin, açık saçık, sövgü niteliğinde veya günaha yol açan söz söylemedir. Başkasını böyle bir söze yöneltme ve haftalık toplu ibadet konuşması sürerken söz söyleme, belirli yapılara bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz batıl, çirkin, açık saçık, sövgü niteliğinde veya günaha yol açan içerik taşır."},{"facet_id":"F002","role":"associated_use","statement":"Bir kişi başkasını batıl veya çirkin söze katılmaya yöneltebilir."},{"facet_id":"F003","role":"extension","statement":"Haftalık toplu ibadet konuşması sürerken söz söylemek, içeriği ayrıca kötülenmeden bu adla nitelenir."}],"identity_rationale":"Kaynak ifadesinin büyük bölümü batıl, çirkin, açık saçık, sövgü veya günah niteliğindeki sözü destekler. Ancak haftalık toplu ibadet konuşması sırasında söz söyleme tanıklığı, sözün içeriği kötü olmasa da bu dala bağlanan yapı ile sınırlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"batıl veya çirkin söz"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çirkin ya da açık saçık söz"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onu batıl veya çirkin söze yöneltmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"haftalık toplu ibadet konuşması sırasında söz söylemek"}],"lexicalization_note":"Bare söz niteliği ile belirli ibadet bağlamındaki konuşma ve başkasını kötü söze yöneltme kullanımları ayrı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar, değersiz sayma sonucunu, ses olayını ve özellikle ağır çirkin söz alanını birbirinden ayıran üç adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sözün içeriğini ve niteliğini sınıflandırır; komşu dal ise içeriği ne olursa olsun bir şeyi dikkate almama veya geçersiz kılma sonucuna odaklanır.","focus_only":"Sözün batıl, çirkin, açık saçık, sövgü veya günah niteliğinde olmasını bildirir.","gloss":"kötü söz ile değersiz sayma","neighbor_only":"Bir şeyi değersiz veya geçersiz sayarak hesaba katmama işlemini söz dışına da yayar.","neighbor_ref":"root_001361/B001","relation_type":"near_neighbor","shared_zone":"Olumsuz değerlendirilen bir söz her iki dalın kullanım alanına yaklaşabilir."},{"boundary_match":"partial","distinction":"Bu dalda belirleyici olan sözün içeriği veya ahlaki niteliğidir; komşu dalda ise işitsel olay ve sesin yükseltilmesi belirleyicidir.","focus_only":"Sözün batıl, çirkin veya günahlı oluşunu temel alır.","gloss":"kötü içerik ile gürültü","neighbor_only":"Sesi, gürültüyü, hayvan seslerini ve şaşırtmak için sesi yükseltmeyi temel alır.","neighbor_ref":"root_001361/B003","relation_type":"near_neighbor","shared_zone":"Yüksek ve karışık bir konuşma hem rahatsız edici ses hem de kötü söz içerebilir."},{"boundary_match":"partial","distinction":"Komşu dal ağır ve kasıtlı çirkin sözde yoğunlaşır; bu dalın kapsamı batıl söze ve belirli yapılardaki konuşma eylemlerine kadar genişler.","focus_only":"Batıl söz, başkasını böyle söze yöneltme ve belirli ibadet bağlamında konuşma uzantılarını da içerir.","gloss":"çirkin söz","neighbor_only":"Kasıtlı biçimde söylenen ağır, utanç verici ve terk edilmesi gereken çirkin söze odaklanır.","neighbor_ref":"root_001578/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da çirkin ve açık saçık söz alanını doğrudan kapsar."}],"source_phrase_ar":"لغا يلغو لغوا يعني اختلاط الكلام في الباطل (ayn;tahdhib)؛ لغا يلغو لغوا أي قال باطلا (sihah)؛ كل كلام قبيح لغوا (mufradat)؛ لاغية كلمة قبيحة أو فاحشة (ayn;tahdhib)؛ قال قتادة باطلا ومأثما وقال مجاهد شتما (tahdhib)؛ استلغوني أرادوني على اللغو (tahdhib)","source_summary":"Tanıklıklar batıl ve çirkin söz çekirdeğinde birleşir; açık saçık söz, sövgü ve günahlı konuşma bu alanı özelleştirir. Başkasını böyle konuşmaya yöneltme ile toplu ibadet konuşması sırasındaki söz söyleme de yapıya bağlı kullanımlar olarak aktarılır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اختلاط الكلام بالباطل، والكلام القبيح أو الفاحش أو الشتم أو المأثم، والخوض في اللغو أو إرادة غيره عليه.","what_is_not_ar":"ليس لغو اليمين من جهة عدم العقد إلا إذا أريد قبح الكلام، وليس مجرد الصوت أو اللهجة ولا الإلغاء من الحساب."},"support_links":["sup_17623535f2c99623da25","sup_7a4cc0ca2df710cba60d"]},{"boundary":"Dal genel ses ve gürültü olarak tanımlanmalı; karışıklık ve yanıltıcı yüksek konuşma yalnızca özel bir gerçekleşme sayılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001361/B003","candidate_links":[{"candidate_id":"cand_4f483aec6bdd1ef3809d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"ses ve gürültü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvandan çıkan işitilebilir ses ve gürültü bu dalın ortak çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Konuşma sesi, dinleyenleri şaşırtmak ve algılarını bozmak amacıyla yükseltilebilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Köpek havlaması, kuşların ve özellikle küçük kuşların sesleri bu ses alanına örnek verilir."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan konuşmasından hayvan seslerine uzanan ortak işitsel çekirdeği, her örneği karışık veya yüksek saymadan karşılar.","boundary_detail":"Dal genel ses ve gürültü olarak tanımlanmalı; karışıklık ve yanıltıcı yüksek konuşma yalnızca özel bir gerçekleşme sayılmalıdır.","branch_image_ar":"ضجيج الصوت المختلط","concept_gloss":"ses ve gürültü","contextual_glosses":[{"applicability":"Konuşma sesinin dinleyenlerin algısını bozmak amacıyla özellikle yükseltildiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem ses yükseltme eylemini hem de dinleyeni şaşırtma amacını korur."},"facet_ids":["F002"],"text":"şaşırtmak için sesi yükseltmek","usage_role":"contextual"},{"applicability":"Kuşların toplu veya tekil seslerinden söz edilen hayvan sesi bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuşlardan çıkan sesleri doğal ve doğrudan biçimde karşılar."},"facet_ids":["F003"],"text":"kuş sesleri","usage_role":"contextual"}],"definition":"İnsan veya hayvan kaynaklı ses ve gürültü alanıdır. Konuşma sesini başkalarını şaşırtmak için yükseltme bunun amaçlı bir gerçekleşmesi, köpek havlaması ile kuş sesleri ise hayvan sesi örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvandan çıkan işitilebilir ses ve gürültü bu dalın ortak çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Konuşma sesi, dinleyenleri şaşırtmak ve algılarını bozmak amacıyla yükseltilebilir."},{"facet_id":"F003","role":"example","statement":"Köpek havlaması, kuşların ve özellikle küçük kuşların sesleri bu ses alanına örnek verilir."}],"identity_rationale":"Kaynak ifadesi yalnızca karışık gürültüyü değil, genel sesi, köpek havlamasını ve kuş seslerini de kapsar. Şaşırtmak amacıyla konuşma sesini yükseltme desteklenir, fakat bu özellik dalın bütün örnekleri için zorunlu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"konuşma sesini yükselterek şaşırtmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ses ve gürültü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"köpek havlaması"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kuş sesleri"}],"lexicalization_note":"Genel ses adı ile şaşırtıcı yüksek konuşma, köpek havlaması ve kuş sesi yapıları birbirine genellenmeden ayrı gösterilir.","neighbor_coverage_note":"Adaylar arasından kötü söz dalı içerik ile sesi ayırır; yüksek ses ve gürültü adayı ise en geniş gerçek anlam örtüşmesini gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal işitilebilir sesi ve kimi zaman yükseltme amacını anlatır; komşu dal sözün içeriği hakkında olumsuz bir değerlendirme yapar.","focus_only":"Sözün içeriğinden bağımsız olarak ses, gürültü ve hayvan seslerini kapsar.","gloss":"gürültü ile kötü söz","neighbor_only":"Sözün batıl, çirkin, açık saçık veya günahlı niteliğini temel alır.","neighbor_ref":"root_001361/B002","relation_type":"near_neighbor","shared_zone":"Yüksek ve karışık konuşma her iki dalın alanına aynı olay içinde yaklaşabilir."},{"boundary_match":"partial","distinction":"Komşu dal yüksek ve toplu gürültüye daha sıkı bağlıdır; bu dal sıradan hayvan seslerine ve özel bir yanıltma amaçlı konuşma kullanımına da uzanır.","focus_only":"Genel ses, kuş sesi ve yanıltma amacıyla yükseltilen konuşmayı da kapsar.","gloss":"yüksek ses ve gürültü","neighbor_only":"Bağırma, feryat, topluluk gürültüsü ve av hayvanlarının seslerinde yoğunlaşır.","neighbor_ref":"root_001664/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da yüksek insan sesini, topluluk gürültüsünü ve bazı hayvan seslerini kapsar."}],"source_phrase_ar":"والغوا فيه يعني رفع الصوت بالكلام ليغلطوا المسلمين (ayn)؛ اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا (sihah)؛ لغوى الطير أصواتها (tahdhib)؛ اللغا صوت العصافير ونحوها من الطيور (mufradat)","source_summary":"Tanıklıklar genel ses ve gürültüyü, şaşırtmak amacıyla yükseltilen konuşmayı, köpek havlamasını ve çeşitli kuş seslerini tek bir işitsel alan içinde sunar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه رفع الصوت بالكلام للتشويش والتغليط، ومطلق الصوت أو اللغا، ونباح الكلب، وأصوات الطير والعصافير.","what_is_not_ar":"ليس الحكم على الكلام بأنه باطل أو قبيح، ولا الإلغاء والإسقاط من العدد، ولا معنى اللغة بوصفها لسان جماعة."},"support_links":["sup_7a4cc0ca2df710cba60d"]},{"boundary":"Bir şeye düşkünlük çekirdek olarak, çok tüketme özelleşme olarak, topluluk dili ise ayrı bir sözlü iletişim uzantısı olarak tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001361/B004","candidate_links":[{"candidate_id":"cand_24b485fa16f9a1ed8405","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"bir şeye düşkün olup onunla sürekli meşgul olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir şeye düşkün olur, ona bağlanır ve onunla sürekli meşgul olur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçecek veya su söz konusu olduğunda eylem, onu sık ve çok tüketme anlamı kazanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun sürekli kullandığı söz düzeni ve aynı anlamı başka sözlerle anlatma biçimi, yerleşmiş dil anlamını oluşturur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluğun konuşmasını soru sormadan dinleyerek onların dil kullanımı öğrenilebilir."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi ile yöneldiği şey arasındaki sürekli ilgi, bağlanma ve meşguliyet çekirdeğini karşılar.","boundary_detail":"Bir şeye düşkünlük çekirdek olarak, çok tüketme özelleşme olarak, topluluk dili ise ayrı bir sözlü iletişim uzantısı olarak tutulmalıdır.","branch_image_ar":"اللهج بالشيء ولسان الجماعة","concept_gloss":"bir şeye düşkün olup onunla sürekli meşgul olma","contextual_glosses":[{"applicability":"Bir içecek veya suyun sık ve fazla miktarda tüketildiği bağlamlarda doğal eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir içeceği sık ve fazla kullanıp tüketme anlamını korur."},"facet_ids":["F002"],"text":"çok tüketmek","usage_role":"contextual"},{"applicability":"Bir topluluğun kullandığı söz düzeni veya aynı anlamı kendine özgü sözlerle anlatma biçimi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğa bağlı söz düzenini ve anlatım farklılığını birlikte korur."},"facet_ids":["F003"],"text":"topluluğun dili","usage_role":"contextual"}],"definition":"Bir şeye düşkün olup onunla sürekli meşgul olma veya onu çok kullanıp tüketme anlamıdır. Topluluğun alışkanlıkla kullandığı söz düzeni ve aynı anlamı farklı sözlerle anlatma biçimi olan dil, bu çekirdekle türetim bağı kurulan yerleşmiş bir uzantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir şeye düşkün olur, ona bağlanır ve onunla sürekli meşgul olur."},{"facet_id":"F002","role":"specialization","statement":"İçecek veya su söz konusu olduğunda eylem, onu sık ve çok tüketme anlamı kazanır."},{"facet_id":"F003","role":"extension","statement":"Bir topluluğun sürekli kullandığı söz düzeni ve aynı anlamı başka sözlerle anlatma biçimi, yerleşmiş dil anlamını oluşturur."},{"facet_id":"F004","role":"associated_use","statement":"Bir topluluğun konuşmasını soru sormadan dinleyerek onların dil kullanımı öğrenilebilir."}],"identity_rationale":"Kaynak ifadesi bir şeye sürekli düşkün olmayı, onu çok tüketmeyi ve topluluğun dili anlamını birlikte tanıklar. Bununla birlikte dil anlamı, düşkünlük çekirdeğinin doğrudan eş anlamlısı değil, açıklanan türetim bağına dayalı yerleşmiş bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir şeye düşkün olmak ve onunla sürekli meşgul olmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir içeceği çok tüketmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bir topluluğun dili veya aynı anlamı farklı sözlerle anlatma biçimi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kendilerine sormadan konuşmalarını dinleyip dil kullanımlarını öğrenmek"}],"lexicalization_note":"Bir şeye düşkün olma, bir içeceği çok tüketme, topluluk dili ve konuşmayı dinleyerek öğrenme kullanımları ayrı kapsamlarla verilir.","neighbor_coverage_note":"Düşkünlük alanındaki en yakın aday ile topluluk dili alanındaki en yakın aday, dalın iki temel sınırını gereksiz tekrar olmadan gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal duygusal tutku ve bağlılığı öne çıkarır; bu dal sürekli meşguliyete dayanır ve tüketim ile dil alanlarına ayrıca uzanır.","focus_only":"Sürekli meşguliyet yanında çok tüketme ve topluluk dili uzantılarını da kapsar.","gloss":"düşkünlük ve güçlü bağlanma","neighbor_only":"Yoğun sevgi, tutku ve kişiye yönelik güçlü duygusal bağlanmada yoğunlaşır.","neighbor_ref":"root_001314/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeye veya kişiye güçlü biçimde yönelip bağlanmayı anlatır."},{"boundary_match":"partial","distinction":"Bu dalda topluluk dili daha geniş ve türemiş bir anlamdır; komşu dal doğrudan topluluğa özgü söyleyiş biçimini merkeze alır.","focus_only":"Düşkünlük ve çok tüketme çekirdeği yanında genel dil ve anlatım farklılığı anlamını taşır.","gloss":"dil ile topluluğa özgü söyleyiş","neighbor_only":"Özellikle bir kişinin veya topluluğun kendine özgü söyleyişine ve lehçesine odaklanır.","neighbor_ref":"root_001349/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir topluluğun kendine özgü konuşma biçimini adlandırabilir."}],"source_phrase_ar":"لغى بالأمر إذا لهج به ويقال إن اشتقاق اللغة منه (maqayis)؛ اللغة واللغات اختلاف الكلام في معنى واحد (ayn;tahdhib)؛ لغي به أي لهج به ولغي بالشراب أكثر منه واللغة أصلها لغى أو لغو (sihah)؛ لغي فلان بفلان إذا أولع به ولغي فلان بالماء إذا أكثر منه واستلغهم اسمع من لغاتهم (tahdhib)؛ لغي بكذا أي لهج به ومنه قيل للكلام الذي يلهج به فرقة فرقة لغة (mufradat)","source_summary":"Tanıklıklar bir şeye düşkün olma ve içeceği çok tüketme anlamlarını verir; dil anlamını bir topluluğun sürekli kullandığı sözlerle ve aynı anlamın farklı sözlerle anlatılmasıyla açıklar. Ayrıca konuşmayı doğrudan dinleyerek dil kullanımını edinme eylemi aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اللهج بالشيء والولوع به أو الإكثار منه، ومنه اللغة واللغات بوصفها كلاما تلهج به جماعة أو اختلاف الكلام في معنى واحد.","what_is_not_ar":"ليس الكلام الباطل أو القبيح، ولا مجرد الضجيج، ولا ما يلغى لأنه لا يعتد به."},"support_links":["sup_cbdb00cc01191c440820"]},{"boundary":"Dal, doğruluk ölçütünden ayrılmayı anlatan belirli yapıyla sınırlıdır; genel yanlışlık veya her türlü yön değişimi değildir.","branch_kind":"non_bare","branch_ref":"root_001361/B005","candidate_links":[{"candidate_id":"cand_14d8928c037ce80960e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"doğru olandan sapmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi doğru kabul edilen çizgiden ayrılır ve başka bir yöne yönelir."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin doğruluk ölçütünden ayrılarak başka bir yöne yöneldiği tanıklanmış yapı için tam karşılıktır.","boundary_detail":"Dal, doğruluk ölçütünden ayrılmayı anlatan belirli yapıyla sınırlıdır; genel yanlışlık veya her türlü yön değişimi değildir.","branch_image_ar":"الميل عن الصواب","concept_gloss":"doğru olandan sapmak","contextual_glosses":[{"applicability":"Yönelimin fiziksel bir yoldan çok doğru kabul edilen görüş veya davranış çizgisinden ayrılma olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğru kabul edilen çizgiden ayrılma ilişkisini açık biçimde korur."},"facet_ids":["F001"],"text":"doğruluktan ayrılmak","usage_role":"general"}],"definition":"Bir kişinin doğru olandan ayrılması, doğruluk çizgisinden başka yana yönelmesi anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi doğru kabul edilen çizgiden ayrılır ve başka bir yöne yönelir."}],"identity_rationale":"Kaynak ifadesi kişinin doğru olandan yana sapıp ayrılmasını doğrudan bildirir. Anlam yalnızca bu edatlı yapıda tanıklandığı için genel bir eğilme veya bütün yalın kullanımlara yayılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"doğru olandan sapmak"}],"lexicalization_note":"Tanım yalnızca doğru olandan sapmayı bildiren tanıklanmış yapıya bağlıdır ve yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Yanlış yapma adayı anlam yakınlığını, doğruluk ve düzgünlük adayı ise aynı eksendeki açık karşıtlığı en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir doğruluk çizgisinden ayrılma yönelimidir; komşu dal ise yönelim yanında kasıtsız eylemi ve hedefi tutturamama sonucunu da içerir.","focus_only":"Yalnızca doğru olandan yana sapmayı bildiren belirli yapıya bağlıdır.","gloss":"doğrudan sapma ile yanlış yapma","neighbor_only":"Hedefi tutturamama, istemeden yanlış yapma ve eylemin amaçlanandan farklı sonuçlanmasını da kapsar.","neighbor_ref":"root_000420/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da doğru sonuca veya doğru çizgiye ulaşamamayı anlatabilir."},{"boundary_match":"opposed","distinction":"Bu dal ölçütten uzaklaşmayı, komşu dal ise ölçüye uygun ve doğru çizgide olmayı anlatır.","focus_only":"Doğru çizgiden ayrılma ve başka yana yönelme durumunu bildirir.","gloss":"sapma ile doğruluk","neighbor_only":"Doğru çizgide kalma, düzgünlük, denge ve yerindelik durumunu bildirir.","neighbor_ref":"root_001273/B008","relation_type":"polarity_pair","shared_zone":"İki dal aynı doğruluk ve düzgünlük eksenini karşıt yönlerden değerlendirir."}],"source_phrase_ar":"لغا فلان عن الصواب أي مال عنه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu kullanım, kişinin doğru olandan sapmasını bildiren tekil bir tanıklıktır."}],"source_summary":"Bu dal için birden çok kaynağın paylaştığı ayrı bir özet bulunmaz.","sources":["TA"],"what_is_ar":"يدخل فيه قولهم لغا عن الصواب بمعنى مال عنه.","what_is_not_ar":"ليس البطلان العام للكلام ولا الضجيج ولا معنى اللغة."},"support_links":["sup_ed169584d7a5e4698a8a"]},{"boundary":"Kendiliğinden başarısız kalma ile başkasını başarısızlığa uğratma katılımcı yönleri ayrı korunmalı; sayıdan çıkarma anlamıyla birleştirilmemelidir.","branch_kind":"non_bare","branch_ref":"root_001361/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","surface_ar":"لَٰغِيَةً"}],"gloss":"umduğunu bulamama veya birini başarısızlığa uğratma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi beklediği sonucu elde edemez ve başarısız kalır; toplu ibadet konuşması sırasında söz söyleme bu sonuca bağlanan özel durumdur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başka birini beklediği sonuçtan yoksun bırakır ve başarısızlığa uğratır."}}],"root_ar":"ل غ و","root_id":"root_001361","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin beklediği sonuca ulaşamamasını hem de başka bir kişinin bu sonuca ulaşmasını engelleyen ettirici yönü karşılar.","boundary_detail":"Kendiliğinden başarısız kalma ile başkasını başarısızlığa uğratma katılımcı yönleri ayrı korunmalı; sayıdan çıkarma anlamıyla birleştirilmemelidir.","branch_image_ar":"الخيبة وإيقاعها بالفشل","concept_gloss":"umduğunu bulamama veya birini başarısızlığa uğratma","contextual_glosses":[{"applicability":"Öznenin beklediği sonucu elde edemediği ve başarısız kaldığı geçişsiz kullanım için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beklenen sonucun elde edilememesini ve öznenin başarısız kalmasını korur."},"facet_ids":["F001"],"text":"umduğunu bulamamak","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini beklediği sonuçtan yoksun bıraktığı ettirici kullanım için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir kişide başarısızlık sonucu doğuran ettirici ilişkiyi korur."},"facet_ids":["F002"],"text":"başarısızlığa uğratmak","usage_role":"contextual"}],"definition":"Bir kişinin umduğunu bulamayıp başarısız kalması veya bir başkasının umduğunu bulmasını engelleyerek onu başarısızlığa uğratması anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi beklediği sonucu elde edemez ve başarısız kalır; toplu ibadet konuşması sırasında söz söyleme bu sonuca bağlanan özel durumdur."},{"facet_id":"F002","role":"core","statement":"Bir kişi başka birini beklediği sonuçtan yoksun bırakır ve başarısızlığa uğratır."}],"identity_rationale":"Kaynak ifadesi hem kişinin umduğunu bulamayıp başarısız kalmasını hem de bir başkasını bu sonuca uğratmayı açıkça verir. Haftalık toplu ibadet konuşması sırasındaki söz söyleme, ilk yönün belirli bağlamdaki örneğidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"haftalık toplu ibadet konuşması sırasında konuşup umduğunu bulamamak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onu umduğundan yoksun bırakıp başarısızlığa uğratmak"}],"lexicalization_note":"İki anlam yalnızca tanıklanmış başarısız kalma ve başkasını başarısızlığa uğratma yapıları içinde tanımlanır.","neighbor_coverage_note":"Genel başarısızlık adayı çekirdeğe en yakın eşleşmeyi, eli boş dönme adayı ise olay yapısındaki ek koşulu açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel başarısızlık ve yoksun kalma alanıdır; bu dal aynı çekirdeği belirli yapılar ve özel bir ibadet bağlamıyla tanıklar.","focus_only":"Belirli ibadet konuşması bağlamındaki başarısız kalma kullanımını da içerir.","gloss":"umduğunu bulamama","neighbor_only":"Bir isteğe ulaşamama, iyi sonuçtan yoksun kalma ve kazanç elde edememe alanını daha genel biçimde kapsar.","neighbor_ref":"root_000451/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin aradığı veya beklediği sonucu elde edememesini ve bunun ettirici yönünü kapsar."},{"boundary_match":"partial","distinction":"Komşu dal geri dönüş ve kazançsızlık koşuluna bağlıdır; bu dalda geri dönüş gerekmez ve ettirici bir kullanım da bulunur.","focus_only":"Başarısız kalmanın yanında bir başkasını başarısızlığa uğratma yönünü de taşır.","gloss":"başarısız kalma ile eli boş dönme","neighbor_only":"Bir amaçtan eli boş ve kazançsız dönme hareketini zorunlu kılar.","neighbor_ref":"root_000816/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da amaçlanan sonucun elde edilememesi yüzünden düş kırıklığına uğramayı anlatır."}],"source_phrase_ar":"من تكلم يوم الجمعة والإمام يخطب فقد لغا أي خاب؛ وألغيته أي خيبته (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tekil tanıklık, toplu ibadet konuşması sırasında söz söyleyip başarısız kalma ile bir başkasını başarısızlığa uğratma yönlerini birlikte verir."}],"source_summary":"Bu dal için birden çok kaynağın paylaştığı ayrı bir özet bulunmaz.","sources":["TA"],"what_is_ar":"يدخل فيه تفسير لغا بمعنى خاب، وألغاه بمعنى خيبه.","what_is_not_ar":"ليس مجرد التكلم في خطبة الجمعة إلا من جهة هذا التفسير، ولا الإلغاء بمعنى الإسقاط من العدد."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:11:1"],"branch_refs":[],"candidate_id":"cand_e9a052470bf172efeb0a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:1:bounded-class-scope","source_type":"word_analysis","support_ids":["sup_1a1a0f1248e8c96faabf","sup_ab9680fb4ac0967be3ea"],"title":"bounded class-wide negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:1","qac_refs":["88:11:1:1"],"status":"accepted"}},{"anchor_refs":["88:11:1"],"branch_refs":[],"candidate_id":"cand_346ee0d5fb0cd3c1b1bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:1:descriptive-negation","source_type":"word_analysis","support_ids":["sup_0727422c9c9d38563842","sup_ab9680fb4ac0967be3ea"],"title":"descriptive absence, not prohibition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:1","qac_refs":["88:11:1:1"],"status":"accepted"}},{"anchor_refs":["88:11:1"],"branch_refs":[],"candidate_id":"cand_f8f1903e81d5588b7db3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:1:opening-and-sound-binding","source_type":"word_analysis","support_ids":["sup_56731116471477df25b7","sup_ab9680fb4ac0967be3ea"],"title":"negation heard before content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:1","qac_refs":["88:11:1:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_0890ab5c0090850cdb38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:inter-ayah-hearing-problem","source_type":"word_analysis","support_ids":["sup_9a874a03359c127e567e","sup_ff01468d5ae18b377c39"],"title":"heard vain talk removed before response (17:36; 28:55)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:2","qac_refs":["88:11:2:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_174f03d168c1ff639dbe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:perceptual-scene-order","source_type":"word_analysis","support_ids":["sup_387bc9f459bf0488b6f4","sup_9a874a03359c127e567e"],"title":"perception staged before content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:2","qac_refs":["88:11:2:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_668517c7525609c738c1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:reception-range","source_type":"word_analysis","support_ids":["sup_109681ef787c7b1ec5c7","sup_9a874a03359c127e567e"],"title":"hearing as purified reception","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:2","qac_refs":["88:11:2:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_555e54bc28ba428a46c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:t-prefix-and-form","source_type":"word_analysis","support_ids":["sup_13f9e60069db2c23599d","sup_9a874a03359c127e567e"],"title":"active imperfect with controlled subject ambiguity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:2","qac_refs":["88:11:2:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_1e0833af55232f442b4a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:voice-variants","source_type":"word_analysis","support_ids":["sup_201e43f7541f1a8c2fa3","sup_9a874a03359c127e567e"],"title":"active and passive readings redistribute the soundscape","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:2","qac_refs":["88:11:2:1"],"status":"accepted"}},{"anchor_refs":["88:11:3"],"branch_refs":[],"candidate_id":"cand_39b89d1bc30f26937abf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:3:bounded-interior","source_type":"word_analysis","support_ids":["sup_1240a79a8693b958e0c7","sup_1e602077f128c2b8671d"],"title":"garden interior as scope boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:3","qac_refs":["88:11:3:1","88:11:3:2"],"status":"accepted"}},{"anchor_refs":["88:11:3"],"branch_refs":[],"candidate_id":"cand_f4bbf2800e4c95b2ed3b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:3:locative-hinge","source_type":"word_analysis","support_ids":["sup_1240a79a8693b958e0c7","sup_919f809b8bf104673c9f"],"title":"place mediates hearing and excluded speech","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:3","qac_refs":["88:11:3:1","88:11:3:2"],"status":"accepted"}},{"anchor_refs":["88:11:3"],"branch_refs":[],"candidate_id":"cand_fc3c79b48dc356449df0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:3:pronoun-backlink","source_type":"word_analysis","support_ids":["sup_05d4c9057f67fe31bd42","sup_1240a79a8693b958e0c7"],"title":"suffix resumes the prior garden (88:10)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:3","qac_refs":["88:11:3:1","88:11:3:2"],"status":"accepted"}},{"anchor_refs":["88:11:3"],"branch_refs":[],"candidate_id":"cand_3fb491fe642216bdfecf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:11:3:sequence-reprise","source_type":"word_analysis","support_ids":["sup_1240a79a8693b958e0c7","sup_1e89fcd367162508117c"],"title":"interior carries exclusion into provision (88:12)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:3","qac_refs":["88:11:3:1","88:11:3:2"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_6605f19d6a71c6bd7fb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:case-and-voice-alternation","source_type":"word_analysis","support_ids":["sup_5e518818f04a96143edb","sup_aefc683525780858669d"],"title":"object or subject, still excluded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_73bbd966704c601285ba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:indefinite-negated-object","source_type":"word_analysis","support_ids":["sup_64c2eb429369c0f4c0fc","sup_aefc683525780858669d"],"title":"any vain utterance excluded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_60ab0fdbf8da90603ee9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:inter-ayah-soundscape-contrasts","source_type":"word_analysis","support_ids":["sup_4c88247efdb2b1a95e86","sup_aefc683525780858669d"],"title":"vain talk contrasted with peace and turning away (19:62; 28:55; 78:35)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_8462dd499e5aaa316213","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:participial-rare-shape","source_type":"word_analysis","support_ids":["sup_aefc683525780858669d","sup_b05e1bebd4b2c1859578"],"title":"participial utterance-quality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_893925a9fa803e85cd9f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:phonetic-texture","source_type":"word_analysis","support_ids":["sup_aefc683525780858669d","sup_f9c8438b2d09c2695f36"],"title":"rough loose-speech texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_8446959a018656a6171b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:scene-closure-and-forward-reversal","source_type":"word_analysis","support_ids":["sup_aefc683525780858669d","sup_c6977982f8d3856e3541"],"title":"absence closes the scene before provision (88:12)","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_c986561bf914c57a0a2d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:semantic-field-narrowed-to-audible","source_type":"word_analysis","support_ids":["sup_5183e94bcd831d11bab0","sup_aefc683525780858669d"],"title":"nullity and noise narrowed to heard communication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:11:4","qac_refs":["88:11:4:1"],"status":"accepted"}},{"anchor_refs":["88:11:2"],"branch_refs":[],"candidate_id":"cand_ee2deb743541091590bd","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000741"],"scope":"focus_ayah","source_local_id":"88:11:2:1","source_type":"qac_morpheme","support_ids":["sup_ba990c0168c0f918dfa0"],"title":"QAC root occurrence: س م ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:11:4"],"branch_refs":[],"candidate_id":"cand_853d8408b899c5d8a263","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001361"],"scope":"focus_ayah","source_local_id":"88:11:4:1","source_type":"qac_morpheme","support_ids":["sup_bde327f6ad1fe3a2d3a1"],"title":"QAC root occurrence: ل غ و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:11","branch_refs":["root_000741/B001","root_000741/B007","root_001361/B002","root_001361/B003"],"candidate_id":"cand_4f483aec6bdd1ef3809d","commentary_obligation":"review","hft_ref":"hft_1828fbe7f4e16e712dc3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_selective_soundscape","source_type":"hft","support_ids":["sup_7a4cc0ca2df710cba60d"],"title":"base_selective_soundscape","trust":"legacy_unbound"},{"anchor_refs":["88:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:11","branch_refs":["root_000741/B003","root_001361/B001","root_001361/B005"],"candidate_id":"cand_14d8928c037ce80960e8","commentary_obligation":"review","hft_ref":"hft_a33bf80f8cedfadf962e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_no_null_uptake","source_type":"hft","support_ids":["sup_ed169584d7a5e4698a8a"],"title":"base_no_null_uptake","trust":"legacy_unbound"},{"anchor_refs":["88:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:11","branch_refs":["root_000741/B005","root_001361/B001","root_001361/B004"],"candidate_id":"cand_24b485fa16f9a1ed8405","commentary_obligation":"review","hft_ref":"hft_69dff78b4d5135a92447","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_no_empty_public_circulation","source_type":"hft","support_ids":["sup_cbdb00cc01191c440820"],"title":"base_no_empty_public_circulation","trust":"legacy_unbound"},{"anchor_refs":["88:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:11","branch_refs":["root_000741/B004","root_000741/B006","root_001361/B002"],"candidate_id":"cand_e2ad12629184a76caed3","commentary_obligation":"review","hft_ref":"hft_7022d95b575585e69425","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_no_abusive_transmission","source_type":"hft","support_ids":["sup_17623535f2c99623da25"],"title":"base_no_abusive_transmission","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:11:1:1","qac_word_ref":"88:11:1","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","root_ar":"س م ع","surface_ar":"تَسْمَعُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:11:3:1","qac_word_ref":"88:11:3","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:11:3:2","qac_word_ref":"88:11:3","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","root_ar":"ل غ و","surface_ar":"لَٰغِيَةً"}],"word_analysis_qac_refs":[["88:11:1:1"],["88:11:2:1"],["88:11:3:1","88:11:3:2"],["88:11:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:11:1","88:11:2","88:11:3","88:11:4"]},"focus_surface_evidence":{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:11:1:1","qac_word_ref":"88:11:1","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"سَمِعَ","morph_features":"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:11:2:1","qac_word_ref":"88:11:2","root_ar":"س م ع","surface_ar":"تَسْمَعُ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:11:3:1","qac_word_ref":"88:11:3","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:11:3:2","qac_word_ref":"88:11:3","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"لَٰغِيَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:11:4:1","qac_word_ref":"88:11:4","root_ar":"ل غ و","surface_ar":"لَٰغِيَةً"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:11:1:1"],["88:11:2:1"],["88:11:3:1","88:11:3:2"],["88:11:4:1"]],"word_analysis_refs":["88:11:1","88:11:2","88:11:3","88:11:4"],"word_rows":[{"analysis_record_ref":"88:11:1","analytic_gloss_range_en":"simple descriptive negation over a hearing clause; not a prohibition","analytic_root_gloss_range_en":null,"qac_refs":["88:11:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَّا","transliteration":"lā"}},{"analysis_record_ref":"88:11:2","analytic_gloss_range_en":"hear, receive, or take in speech within a negated locative field; not a local causative 'make hear' sense","analytic_root_gloss_range_en":"broad hearing root spanning ear-hearing, attentive listening, report, acceptance, reputation, insult, and other lexical branches; the local clause selects reception/hearing of speech","qac_refs":["88:11:2:1"],"root":{"arabic":"س م ع","transliteration":"s-m-ʿ"},"surface":{"arabic":"تَسْمَعُ","transliteration":"tasmaʿu"}},{"analysis_record_ref":"88:11:3","analytic_gloss_range_en":"in it, within that feminine garden-domain; a locative hinge in the negated hearing clause","analytic_root_gloss_range_en":null,"qac_refs":["88:11:3:1","88:11:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِيهَا","transliteration":"fīhā"}},{"analysis_record_ref":"88:11:4","analytic_gloss_range_en":"any vain, false, futile, morally weightless, or null utterance as the excluded heard item","analytic_root_gloss_range_en":"root field spanning what does not count, vain or false speech, clamor, absorption, deviation, and failure; local hearing syntax narrows it to excluded audible communication with null or invalid weight","qac_refs":["88:11:4:1"],"root":{"arabic":"ل غ و","transliteration":"l-gh-w"},"surface":{"arabic":"لَٰغِيَةًۭ","transliteration":"lāghiyatan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:11"],"branch_refs":["root_000741/B001","root_000741/B007","root_001361/B002","root_001361/B003"],"candidate_id":"cand_4f483aec6bdd1ef3809d","evidence_scope":"focus_ayah","hft_ref":"hft_1828fbe7f4e16e712dc3","item_id":"base_selective_soundscape","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_selective_soundscape","support_id":"sup_7a4cc0ca2df710cba60d"},{"anchor_refs":["88:11"],"branch_refs":["root_000741/B003","root_001361/B001","root_001361/B005"],"candidate_id":"cand_14d8928c037ce80960e8","evidence_scope":"focus_ayah","hft_ref":"hft_a33bf80f8cedfadf962e","item_id":"base_no_null_uptake","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_no_null_uptake","support_id":"sup_ed169584d7a5e4698a8a"},{"anchor_refs":["88:11"],"branch_refs":["root_000741/B005","root_001361/B001","root_001361/B004"],"candidate_id":"cand_24b485fa16f9a1ed8405","evidence_scope":"focus_ayah","hft_ref":"hft_69dff78b4d5135a92447","item_id":"base_no_empty_public_circulation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_no_empty_public_circulation","support_id":"sup_cbdb00cc01191c440820"},{"anchor_refs":["88:11"],"branch_refs":["root_000741/B004","root_000741/B006","root_001361/B002"],"candidate_id":"cand_e2ad12629184a76caed3","evidence_scope":"focus_ayah","hft_ref":"hft_7022d95b575585e69425","item_id":"base_no_abusive_transmission","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_no_abusive_transmission","support_id":"sup_17623535f2c99623da25"}],"diagnostics":[],"lane_counts":{"global":13,"macro":6,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:11","lane":"micro","linguistic_source_ref":"88:11","surface_ref":"88:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:11","target_tokens":[["Orada",["88:11:3"]],["boş",["88:11:4"]],["söz",["88:11:4"]],["duymazsın",["88:11:1","88:11:2"]]],"text":"Orada boş söz duymazsın."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:3:pronoun-backlink","source_type":"word_analysis","support_id":"sup_05d4c9057f67fe31bd42","text":"{\"blocking_evidence\":null,\"headline\":\"suffix resumes the prior garden (88:10)\",\"reader_payoff\":\"The reader keeps the auditory purification tied to the already named high garden (88:10) rather than letting the phrase float as a generic heavenly claim.\",\"reason\":\"The attachment evidence marks the feminine suffix as resuming the feminine locative antecedent from the prior discourse (88:10).\",\"representative_source_ids\":[\"QG-32379b8c\",\"MG-5a8ee383\",\"QB-be38a775\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:1:descriptive-negation","source_type":"word_analysis","support_id":"sup_0727422c9c9d38563842","text":"{\"blocking_evidence\":null,\"headline\":\"descriptive absence, not prohibition\",\"reader_payoff\":\"The reader notices that the garden is described as already free of vain speech, rather than being regulated by a command to avoid it.\",\"reason\":\"The input marks {{ar:لَّا}} ({{tr:lā}}) as a simple negation particle governing an indicative imperfect, so the CRITICAL claim about description rather than prohibition is locally licensed.\",\"representative_source_ids\":[\"QG-4dd60ae7\",\"QG-d9004c7f\",\"MG-25f3e24b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2:reception-range","source_type":"word_analysis","support_id":"sup_109681ef787c7b1ec5c7","text":"{\"blocking_evidence\":null,\"headline\":\"hearing as purified reception\",\"reader_payoff\":\"The reader notices that the reward protects the whole reception channel, from heard sound to communicative uptake, while the local object keeps the sense tied to speech.\",\"reason\":\"The speech object and locative field license hearing/reception and accountable uptake, but block unrelated branches such as bodily ear, reputation, insult, or causative delivery as local senses.\",\"representative_source_ids\":[\"QS-52c1f598\",\"QS-5a26d70c\",\"MS-79f5e54f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:3","source_type":"word_analysis","support_id":"sup_1240a79a8693b958e0c7","text":"{\"gloss_range\":\"in it, within that feminine garden-domain; a locative hinge in the negated hearing clause\",\"prose\":\"{{ar:فِيهَا}} ({{tr:fīhā}}) is not a loose setting note. The preposition and 3fs suffix make the prior garden-domain (88:10) the bounded interior where the negated hearing event is evaluated, spatially inside the garden and conceptually within its order. Because the word stands between {{ar:تَسْمَعُ}} ({{tr:tasmaʿu}}) and {{ar:لَٰغِيَةًۭ}} ({{tr:lāghiyatan}}), place mediates the relation between reception and excluded speech: the garden is both where hearing would occur and the domain from which futility is absent. That makes the interior an acoustic shield, not merely a pleasant location. The same interior then becomes a forward hinge when the next ayah repeats it and fills the purified field with a flowing spring (88:12).\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِيهَا}} ({{tr:fīhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2:t-prefix-and-form","source_type":"word_analysis","support_id":"sup_13f9e60069db2c23599d","text":"{\"blocking_evidence\":null,\"headline\":\"active imperfect with controlled subject ambiguity\",\"reader_payoff\":\"The reader notices that one compact t-prefix can describe either the hearer's protected experience or the feminine garden-domain's inability to host vain sound.\",\"reason\":\"The attachment evidence explicitly preserves 2ms_or_3fs ambiguity; the Form I/not-causative point is retained as local reception sense rather than a claim that unrelated root branches are active.\",\"representative_source_ids\":[\"QG-4b0fc6a8\",\"MG-b43f4ee0\",\"QF-bac8c47d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:1:bounded-class-scope","source_type":"word_analysis","support_id":"sup_1a1a0f1248e8c96faabf","text":"{\"blocking_evidence\":null,\"headline\":\"bounded class-wide negation\",\"reader_payoff\":\"The reader sees that the negation is not universal silence; it is a garden-bounded exclusion of any speech that falls into the futile or invalid class.\",\"reason\":\"The locative phrase bounds the negated event, while the later indefinite object under negation supports class-wide exclusion inside that bounded field.\",\"representative_source_ids\":[\"QG-536a3bc7\",\"QG-9dae739a\",\"QS-ac0f32e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:3:bounded-interior","source_type":"word_analysis","support_id":"sup_1e602077f128c2b8671d","text":"{\"blocking_evidence\":null,\"headline\":\"garden interior as scope boundary\",\"reader_payoff\":\"The reader notices that the promise is a domain claim about what can be encountered inside the garden, not an abstract statement about silence everywhere.\",\"reason\":\"The prepositional phrase is syntactically forced as a locative complement of the hearing verb and bounds the negated event.\",\"representative_source_ids\":[\"QG-1bfe43d6\",\"QG-fd71759f\",\"QS-8e51f12b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:3:sequence-reprise","source_type":"word_analysis","support_id":"sup_1e89fcd367162508117c","text":"{\"blocking_evidence\":null,\"headline\":\"interior carries exclusion into provision (88:12)\",\"reader_payoff\":\"The reader sees the repeated interior as a sequence-builder: the place first excludes futile speech, then discloses flowing provision (88:12).\",\"reason\":\"The CRITICAL rows explicitly connect this interior with the next ayah (88:12), and the attachment support recommends reading the locative chain across 88:10-13.\",\"representative_source_ids\":[\"QB-74d91136\",\"QY-a90d6871\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2:voice-variants","source_type":"word_analysis","support_id":"sup_201e43f7541f1a8c2fa3","text":"{\"blocking_evidence\":null,\"headline\":\"active and passive readings redistribute the soundscape\",\"reader_payoff\":\"The reader sees that accepted voice variation lets the verse speak both of a protected auditor and of a place where vain speech has no audible occurrence.\",\"reason\":\"The bundle itself notes active base syntax with passive nominative variants, so the role shift is a valid variant-reading contrast while the local base parse remains active.\",\"representative_source_ids\":[\"QG-65ac7ea1\",\"QG-d788f5be\",\"QY-b2effd1c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2:perceptual-scene-order","source_type":"word_analysis","support_id":"sup_387bc9f459bf0488b6f4","text":"{\"blocking_evidence\":null,\"headline\":\"perception staged before content\",\"reader_payoff\":\"The reader feels the verse as a lived auditory scene: negated hearing and bounded place arrive before the excluded speech is named.\",\"reason\":\"The word order and attachments support the staging; sound-texture claims are preserved only as secondary surface color.\",\"representative_source_ids\":[\"QT-7f493a16\",\"MT-956166fd\",\"QE-6de6f9ad\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:inter-ayah-soundscape-contrasts","source_type":"word_analysis","support_id":"sup_4c88247efdb2b1a95e86","text":"{\"blocking_evidence\":null,\"headline\":\"vain talk contrasted with peace and turning away (19:62; 28:55; 78:35)\",\"reader_payoff\":\"The reader sees the garden's soundscape against concrete Quranic contrasts: peace replaces vain talk (19:62), denial-linked speech is excluded (78:35), and righteous turning-away after hearing is surpassed by non-occurrence (28:55).\",\"reason\":\"The CRITICAL rows provide concrete references and coherent contrasts; they are used as inter-ayah payoff, not as replacement for the local syntax.\",\"representative_source_ids\":[\"QI-630b2e2b\",\"MI-4f2d6c0d\",\"ME-390a5a45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:semantic-field-narrowed-to-audible","source_type":"word_analysis","support_id":"sup_5183e94bcd831d11bab0","text":"{\"blocking_evidence\":null,\"headline\":\"nullity and noise narrowed to heard communication\",\"reader_payoff\":\"The reader hears the excluded item as more than casual chatter: it is false, empty, noisy, or morally non-counting communication, locally narrowed to what could be heard.\",\"reason\":\"V4 supports nullity, vain/false speech, and clamor branches, while the local object-of-hearing relation keeps the active sense on audible communication rather than legal nullity alone.\",\"representative_source_ids\":[\"QS-89b78171\",\"QS-da1b5cfb\",\"MS-0a7dba25\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:1:opening-and-sound-binding","source_type":"word_analysis","support_id":"sup_56731116471477df25b7","text":"{\"blocking_evidence\":null,\"headline\":\"negation heard before content\",\"reader_payoff\":\"The reader notices the ayah first creates an experience of withheld sound, then only afterward identifies what is absent.\",\"reason\":\"The word order securely places negation first; phonetic reprise with the final noun is retained as a surface observation, not as independent proof of meaning.\",\"representative_source_ids\":[\"QT-515c2b04\",\"MT-435c3b1d\",\"QY-f3aa1e9e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:case-and-voice-alternation","source_type":"word_analysis","support_id":"sup_5e518818f04a96143edb","text":"{\"blocking_evidence\":null,\"headline\":\"object or subject, still excluded\",\"reader_payoff\":\"The reader sees that variant grammar can shift the noun between heard object and passive subject without weakening the exclusion of its semantic class.\",\"reason\":\"The bundle explicitly records the accusative base reading and nominative passive variants, so the grammatical alternation survives as contrast.\",\"representative_source_ids\":[\"QG-0a09d07b\",\"QG-0be86cf9\",\"QY-9e1373d7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:indefinite-negated-object","source_type":"word_analysis","support_id":"sup_64c2eb429369c0f4c0fc","text":"{\"blocking_evidence\":null,\"headline\":\"any vain utterance excluded\",\"reader_payoff\":\"The reader notices that the ayah does not remove one offensive statement; it denies the whole class of vain utterance inside the garden.\",\"reason\":\"The base reading has a feminine singular accusative indefinite direct object under simple negation, which supports class-wide exclusion.\",\"representative_source_ids\":[\"QG-08f72e3f\",\"QG-97b690cc\",\"MG-a3215c8c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:3:locative-hinge","source_type":"word_analysis","support_id":"sup_919f809b8bf104673c9f","text":"{\"blocking_evidence\":null,\"headline\":\"place mediates hearing and excluded speech\",\"reader_payoff\":\"The reader notices that the garden is not merely where the action happens; its interior mediates what can and cannot reach the ear.\",\"reason\":\"The local order places the locative phrase between the hearing verb and the excluded object, and attachment evidence links it to the hearing event.\",\"representative_source_ids\":[\"QG-24e9f0aa\",\"QT-aed0d253\",\"MT-e86a73c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2","source_type":"word_analysis","support_id":"sup_9a874a03359c127e567e","text":"{\"gloss_range\":\"hear, receive, or take in speech within a negated locative field; not a local causative 'make hear' sense\",\"prose\":\"{{ar:تَسْمَعُ}} ({{tr:tasmaʿu}}) is the clause's reception verb: what is negated is exposure to, report of, or uptake of futile speech inside the garden, not an act of making someone else hear or only a physical sound wave. The t-prefix leaves a controlled ambiguity between a directly addressed hearer and feminine agreement with the garden-domain, while accepted passive variants shift the scene further toward an objective claim that no vain utterance is heard there. Because the verb comes before the locative field and final object, the ayah stages a single compact auditory scene in which what can reach the listener reveals the place's moral ordering. This word therefore makes bliss auditory and relational: in contrast with accountable hearing (17:36) and passages where heard vain talk must be turned away from (28:55), this scene removes the corrupt object before reception occurs.\",\"root_display\":\"{{ar:س م ع}} ({{tr:s-m-ʿ}})\",\"root_gloss_range\":\"broad hearing root spanning ear-hearing, attentive listening, report, acceptance, reputation, insult, and other lexical branches; the local clause selects reception/hearing of speech\",\"surface_display\":\"{{ar:تَسْمَعُ}} ({{tr:tasmaʿu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:1","source_type":"word_analysis","support_id":"sup_ab9680fb4ac0967be3ea","text":"{\"gloss_range\":\"simple descriptive negation over a hearing clause; not a prohibition\",\"prose\":\"{{ar:لَّا}} ({{tr:lā}}) opens the ayah as descriptive negation: the scene is not commanding residents to avoid vain speech, because the following verb remains an indicative hearing form. Its scope is local, evaluative, and class-wide at once: inside the garden-domain, the clause denies not one named utterance but any instance of the futile, false, noisy, or morally weightless speech later named. By arriving before the verb, the place, and the object, the negation makes absence the first acoustic fact of the garden; the sound echo with the final noun can be noticed as a surface binding, while the grammar carries the claim.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4","source_type":"word_analysis","support_id":"sup_aefc683525780858669d","text":"{\"gloss_range\":\"any vain, false, futile, morally weightless, or null utterance as the excluded heard item\",\"prose\":\"{{ar:لَٰغِيَةًۭ}} ({{tr:lāghiyatan}}) is the final named absence, so the single acoustic scene closes not with an added reward but with corrupt speech removed. As an indefinite accusative object under negation in the base reading, it excludes any instance of vain utterance, not a known single remark; passive variants can make it the grammatical subject of being heard, but the same class remains denied audible existence. The root field includes chatter, false or foul speech, null signal, and speech without valid moral weight, yet the hearing frame narrows that range to receivable communication rather than speech as such. Its participial and rare shape makes futility feel like an active speech-quality barred from the garden, specifying the high garden's rank as acoustic purification. The final rough and fading sound texture can suit loose speech that has no continuing place there, while syntax and lexical sense remain the proof. The wider Quranic contrasts sharpen the payoff: no vain talk gives way to peace (19:62), denial-linked speech is absent (78:35), and what the righteous elsewhere must turn away from after hearing (28:55) never enters this soundscape before the next ayah turns the same interior toward flowing provision (88:12).\",\"root_display\":\"{{ar:ل غ و}} ({{tr:l-gh-w}})\",\"root_gloss_range\":\"root field spanning what does not count, vain or false speech, clamor, absorption, deviation, and failure; local hearing syntax narrows it to excluded audible communication with null or invalid weight\",\"surface_display\":\"{{ar:لَٰغِيَةًۭ}} ({{tr:lāghiyatan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:participial-rare-shape","source_type":"word_analysis","support_id":"sup_b05e1bebd4b2c1859578","text":"{\"blocking_evidence\":null,\"headline\":\"participial utterance-quality\",\"reader_payoff\":\"The reader notices that the ayah names not just a category of bad speech but an utterance bearing the active quality of producing futility.\",\"reason\":\"The local form is a feminine active participial noun and the contextual profile marks this exact form as low occurrence, supporting the marked-shape payoff.\",\"representative_source_ids\":[\"QS-c1533522\",\"QF-4cdd6918\",\"QH-fde7d4f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:11:2:1","source_type":"qac_morpheme","support_id":"sup_ba990c0168c0f918dfa0","text":"{\"lemma_ar\":\"سَمِعَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:samiEa|ROOT:smE|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:11:2:1\",\"qac_word_ref\":\"88:11:2\",\"root_ar\":\"س م ع\",\"surface_ar\":\"تَسْمَعُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:11:4:1","source_type":"qac_morpheme","support_id":"sup_bde327f6ad1fe3a2d3a1","text":"{\"lemma_ar\":\"لَٰغِيَة\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:la`giyap|ROOT:lgw|F|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:11:4:1\",\"qac_word_ref\":\"88:11:4\",\"root_ar\":\"ل غ و\",\"surface_ar\":\"لَٰغِيَةً\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:scene-closure-and-forward-reversal","source_type":"word_analysis","support_id":"sup_c6977982f8d3856e3541","text":"{\"blocking_evidence\":null,\"headline\":\"absence closes the scene before provision (88:12)\",\"reader_payoff\":\"The reader feels the final word close the acoustic scene with the removed corrupt sound before the next ayah turns the same garden interior toward flowing provision (88:12).\",\"reason\":\"The object arrives at the end of the clause, and the cited next-ayah contrast is concrete enough to preserve as sequence payoff.\",\"representative_source_ids\":[\"QT-84311f50\",\"QE-aede91c5\",\"QB-49c69624\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:4:phonetic-texture","source_type":"word_analysis","support_id":"sup_f9c8438b2d09c2695f36","text":"{\"blocking_evidence\":null,\"headline\":\"rough loose-speech texture\",\"reader_payoff\":\"The reader can notice how the final sound texture suits speech that lacks stable weight, while syntax and lexical sense remain the basis of the claim.\",\"reason\":\"The phonetic observations are plausible as recitational texture but are narrowed so they do not substitute for grammatical and lexical evidence.\",\"representative_source_ids\":[\"QP-3365af3b\",\"QP-62ce4da0\",\"MP-a0149ab3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:11:2:inter-ayah-hearing-problem","source_type":"word_analysis","support_id":"sup_ff01468d5ae18b377c39","text":"{\"blocking_evidence\":null,\"headline\":\"heard vain talk removed before response (17:36; 28:55)\",\"reader_payoff\":\"The reader recognizes that the garden promise intensifies earlier hearing ethics: the ear is not merely accountable (17:36) or required to turn away after hearing vain talk (28:55), but spared the encounter.\",\"reason\":\"The cited CRITICAL rows give concrete references, and no guardrail evidence contradicts using them as inter-ayah contrast rather than local parse control.\",\"representative_source_ids\":[\"QI-1b2159e8\",\"QI-e537f794\",\"ME-d3aab3d2\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000741/B001","root_000741/B007","root_001361/B002","root_001361/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000741","role":"Ear-hearing supplies the literal sensory channel that remains operative under the object-level negation.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000741","role":"Pleasing audition supplies a positive acoustic alternative, so the line need not erase sound as such.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001361","role":"Vain, false, or foul speech identifies the morally damaged content excluded from hearing.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001361","role":"Mixed raised noise identifies acoustic confusion, making the exclusion environmental as well as semantic.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"The place has a selective soundscape: hearing remains possible, while foul speech and confusing clamor do not enter it.","before":"The place is simply silent."},"confidence":"strong","focus_anchor":"The negation leaves the act of hearing in place and negates its indefinite object, لاغية.","mechanism":"Ordinary hearing is available, but vain or foul speech and mixed clamor are absent; the pleasing-audition branch keeps open the possibility of positive sound.","model_id":"base_selective_soundscape"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_selective_soundscape","source_type":"hft","support_id":"sup_7a4cc0ca2df710cba60d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000741/B003","root_001361/B001","root_001361/B005"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000741","role":"Understanding and compliance turn hearing from bare sensation into accepted or enacted communication.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001361","role":"The thing discarded from reckoning supplies the null status of the communication being refused uptake.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]},{"branch_id":"B005","mapped_root_id":"root_001361","role":"Deviation from correctness supplies the direction in which such apparently actionable speech would mislead.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"Nothing heard there asks for understanding or compliance while being null, non-counting, or off-course.","before":"No one hears idle chatter."},"confidence":"medium","focus_anchor":"تسمع can activate understanding and compliance, while لاغية can activate what does not count or departs from correctness.","mechanism":"The line excludes a communicative object that solicits cognitive uptake or obedience while being void, non-counting, or misdirected.","model_id":"base_no_null_uptake"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_no_null_uptake","source_type":"hft","support_id":"sup_ed169584d7a5e4698a8a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000741/B005","root_001361/B001","root_001361/B004"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000741","role":"Public reputation and circulated report expand hearing from an individual ear to a social transmission network.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001361","role":"What is set aside as not counting gives the circulated material its lack of worth.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001361","role":"A group's repeated speech-habit supplies the mechanism by which empty talk could otherwise become a communal norm.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"The community has no circulation economy in which empty report or reputation-performance becomes habitual speech.","before":"An individual does not happen to overhear nonsense."},"confidence":"medium","focus_anchor":"The hearing root includes public report and reputation, and لاغية names both worthless matter and a group's habitual speech.","mechanism":"The negation can govern a social circulation system: no empty report, reputation-performance, or habitual false discourse becomes common currency.","model_id":"base_no_empty_public_circulation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_no_empty_public_circulation","source_type":"hft","support_id":"sup_cbdb00cc01191c440820","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000741/B004","root_000741/B006","root_001361/B002"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000741","role":"Causing another to hear supplies an upstream speaker-to-recipient transmission relation.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000741","role":"Making someone hear abuse specifies the injurious use of that transmission relation.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001361","role":"Foul speech, insult, and sinful talk supply the harmful payload that never reaches a hearer.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"The social relation itself is non-injurious: no speaker makes another person receive abuse, falsehood, or humiliation.","before":"The hearer is protected by the accidental absence of bad words."},"confidence":"medium","focus_anchor":"The hearing inventory contains both causing another to hear and specifically making another hear abuse; لاغية includes insult and foul speech.","mechanism":"The line can describe a relation between agents, not merely a quiet recipient: no one injects verbal injury into another's hearing.","model_id":"base_no_abusive_transmission"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_no_abusive_transmission","source_type":"hft","support_id":"sup_17623535f2c99623da25","trust":"legacy_unbound"}]}
</lane_packet_json>
