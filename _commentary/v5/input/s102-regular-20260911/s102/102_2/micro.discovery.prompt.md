# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **102:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s102-regular-20260911/s102/102_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "102:2",
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
{"analysis_context":{"analysis_id":"s102-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"102:2","host_surah":102,"lane_context_refs":[],"ordered_context_refs":["102:0","102:1","102:3","102:4","102:5","102:6","102:7","102:8","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal genel eğilme ve yönünden ayrılmadır; yalan, ziyaret, göğüs veya yöneticilik anlamlarını kendi kapsamına almaz.","branch_kind":"bare","branch_ref":"root_000654/B001","candidate_links":[{"candidate_id":"cand_87cb3e8a864dcce27623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"yönünden sapma ve yana eğilme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Amaçlanan yön, yol veya duruştan yana doğru ayrılma ve başka tarafa dönme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin biçiminde, bir canlının duruşunda veya bakışında fiziksel yana eğrilik bulunması."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolundan uzaklaşmış arazi, dibi uzak kuyu, eğri kap ve yay bu yönelme biçiminin örnekleridir."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem amaçlanan doğrultudan ayrılmayı hem de fiziksel yana eğrilik gösteren yalın kullanımları birlikte karşılar.","boundary_detail":"Bu dal genel eğilme ve yönünden ayrılmadır; yalan, ziyaret, göğüs veya yöneticilik anlamlarını kendi kapsamına almaz.","branch_image_ar":"الميل والعدول","concept_gloss":"yönünden sapma ve yana eğilme","contextual_glosses":[{"applicability":"Nesne, gövde veya bakışın fiziksel olarak bir yana kaydığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Fiziksel yana kayma ve eğrilik anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"yana eğilmek","usage_role":"contextual"},{"applicability":"Bir şeyin amaçlanan rota veya doğrultudan ayrıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Amaçlanan yönden ayrılma ve başka yana dönme anlamını korur."},"facet_ids":["F001"],"text":"yolundan sapmak","usage_role":"contextual"}],"definition":"Bir şeyin amaçlanan doğrultudan ayrılması, başka yana dönmesi veya fiziksel olarak yana eğilmesidir. Bu çekirdek, eğri biçimli nesnelere ve bakış ya da duruştaki yana kaymaya uygulanabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Amaçlanan yön, yol veya duruştan yana doğru ayrılma ve başka tarafa dönme."},{"facet_id":"F002","role":"specialization","statement":"Bir nesnenin biçiminde, bir canlının duruşunda veya bakışında fiziksel yana eğrilik bulunması."},{"facet_id":"F003","role":"example","statement":"Yolundan uzaklaşmış arazi, dibi uzak kuyu, eğri kap ve yay bu yönelme biçiminin örnekleridir."}],"identity_rationale":"Kaynak ifadesi, anlamın çekirdeğini bir doğrultudan yana eğilme, amaçlanan yönden ayrılma ve başka yana dönme olarak açıkça kurar. Çöl, kuyu, kap ve yay örnekleri bu çekirdeğin farklı fiziksel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yönünden sapma, yana eğilme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyden yana dönüp uzaklaşmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyden yana sapıp yönünü değiştirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"doğrultusundan sapmış veya yana eğri"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bakışı veya duruşu yana eğik"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım herhangi bir özel söz öbeğine bağlı olmayan eğilme ve yön değiştirme çekirdeğiyle sınırlıdır.","neighbor_coverage_note":"Verilen bütün komşu adayları değerlendirildi; en yakın iki eğilme dalı sınırı belirginleştirdiği için yayımlandı, yalnızca aynı senaryoyu paylaşan veya başka anlam dallarına ait adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; ancak komşu dalın destek amacıyla birine yönelme ve geniş yapısal eğrilik alanı odak dalın sınırını aşar.","focus_only":"Odak dal, belirli bir amaç veya yön çizgisinden ayrılmayı ve bunun adlandırdığı çeşitli eğri biçimleri öne çıkarır.","gloss":"yana sapma","neighbor_only":"Komşu dal, orta çizgiden ayrılmanın yanında bir kişiye destek için yönelmeyi ve çok çeşitli yapısal eğrilikleri de kapsar.","neighbor_ref":"root_001462/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyin düz veya beklenen çizgiden yana ayrılması bulunur."},{"boundary_match":"partial","distinction":"Odak dalda ayrılınan doğrultu belirleyicidir; komşu dalda ise başka bir şeye doğru yönelme veya dayanma ilişkisi belirginleşir.","focus_only":"Odak dal, amaçlanan yön veya doğrultudan sapmayı bağımsız bir çekirdek olarak taşır.","gloss":"başka yana eğilme","neighbor_only":"Komşu dal, bir şeyi başka bir şeye dayama ve güneşin batışa yönelmesi gibi hedefe doğru eğilmeleri kapsar.","neighbor_ref":"root_000924/B001","relation_type":"near_synonym","shared_zone":"İki dal da yön değiştirme ve bir yana eğilme alanında buluşur."}],"source_phrase_ar":"أصل واحد يدل على الميل والعدول (maqayis)؛ الزور الميل (maqayis)؛ مفازة زوراء أي مائلة عن القصد والسمت (ayn)؛ الزور بالتحريك الميل وهو الصعر (sihah)؛ تزاور عنه تزاورا كله بمعنى عدل عنه وانحرف (sihah)؛ الزوراء البئر البعيدة العقر (sihah)؛ الزوراء القدح (sihah)؛ القوس زوراء لميلها (sihah)؛ تتزاور عن كهفهم أي تميل (mufradat)","source_summary":"Kaynaklar, yön veya amaç çizgisinden ayrılma ile fiziksel yana eğilmeyi ortak çekirdek olarak verir; nesne ve duruş örnekleri bu çekirdeği somutlaştırır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الميل عن القصد والسمت والازورار والتزاور وما سمي زوراء لميله كالمفازة والبئر والقدح والقوس","what_is_not_ar":"الكذب؛ الزيارة؛ الصدر؛ التزوير؛ الزعامة"},"support_links":["sup_7e3e381c016bca983319"]},{"boundary":"Dal yalan ve gerçekten sapmış batıl şeylerle sınırlıdır; ziyaret, fiziksel eğilme ve sözü konuşmadan önce düzenleme bu dalın çekirdeği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000654/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"gerçekten sapmış yalan veya batıl nesne","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gerçekle uyuşmayan, doğruluktan ayrılmış yalan veya batıl içerik."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğru olmayan söz ve yalancı tanıklık biçimindeki söz öbeğine bağlı kullanım."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gerçek tanrılık niteliği taşımadığı halde tanrılaştırılıp tapınılan nesne."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın yalan anlamını, doğru olmayan söz kullanımını ve batıl tapınma nesnesine uzanan anlamı birlikte gösterir.","boundary_detail":"Dal yalan ve gerçekten sapmış batıl şeylerle sınırlıdır; ziyaret, fiziksel eğilme ve sözü konuşmadan önce düzenleme bu dalın çekirdeği değildir.","branch_image_ar":"الزور كذب وباطل","concept_gloss":"gerçekten sapmış yalan veya batıl nesne","contextual_glosses":[{"applicability":"Bir sözün veya tanıklığın gerçekle uyuşmadığını bildiren bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlü içeriğin gerçekten ayrılmış ve doğru olmayan niteliğini korur."},"facet_ids":["F002"],"text":"yalan söz","usage_role":"contextual"},{"applicability":"Hak etmediği halde tapınma konusu yapılan nesnenin açıklanmasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin gerçek tanrılık niteliği taşımadan tapınma konusu yapılmasını korur."},"facet_ids":["F003"],"text":"tanrılaştırılan batıl nesne","usage_role":"explanatory"}],"definition":"Gerçekten ve doğrudan ayrılmış söz, hüküm veya tanıklıktır. Bu sapma düşüncesi, hak etmediği halde tanrılaştırılıp tapınılan nesnenin adlandırılmasına da genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gerçekle uyuşmayan, doğruluktan ayrılmış yalan veya batıl içerik."},{"facet_id":"F002","role":"specialization","statement":"Doğru olmayan söz ve yalancı tanıklık biçimindeki söz öbeğine bağlı kullanım."},{"facet_id":"F003","role":"extension","statement":"Gerçek tanrılık niteliği taşımadığı halde tanrılaştırılıp tapınılan nesne."}],"identity_rationale":"Kaynak ifadesi, gerçekten ayrılmış söz anlamındaki yalanı ve buna bağlı olarak doğru kabul edilmemesi gereken tapınma nesnesini birlikte tanıklar. Yalancı tanıklık ve doğru olmayan söz, yalan çekirdeğinin belirli kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yalan ve batıl"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yalan söz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"tanrılaştırılıp tapınılan batıl nesne"}],"lexicalization_note":"Dal hem yalın yalan ve batıl nesne anlamlarını hem de doğru olmayan söz kalıbını içerir; söz kalıbının kapsamı yalın biçimin bütün anlamlarına yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; en yakın iki genel yalan dalı yayımlandı, yalnız belirli yalan türlerini, günahı veya söz süslemesini anlatan adaylar daha uzak kaldığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalan çekirdeği örtüşse de odak dal batıl tapınma nesnesine uzanır; komşu dal ise yalan eylemi ile yalancı kişiye ilişkin daha geniş bir kullanım alanı taşır.","focus_only":"Odak dal, yalancı tanıklığı ve gerçekten sapma gerekçesiyle batıl tapınma nesnesini de kapsar.","gloss":"yalan ve doğruluk karşıtlığı","neighbor_only":"Komşu dal, sözün yanı sıra eylemde yalanı ve yalancının çeşitli nitelendirmelerini daha açık biçimde kapsar.","neighbor_ref":"root_001290/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde gerçeğe aykırı olma ve doğruyu söylememe bulunur."},{"boundary_match":"partial","distinction":"Komşu dalda gerçeğin tersine çevrilmesi ve başkalarını saptıran yalancı öne çıkarken odak dalda yalancı tanıklık ile batıl nesne uzantısı belirleyicidir.","focus_only":"Odak dal, yalancı tanıklığı ve tanrılaştırılmış batıl nesneyi doğruluktan sapma altında birleştirir.","gloss":"gerçekten çevrilmiş yalan","neighbor_only":"Komşu dal, ağır yalanı ve insanları batılla gerçekten uzaklaştıran yalancı kişiyi özellikle adlandırır.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal da doğrudan uzaklaşmış yalan ve batıl içerik alanını paylaşır."}],"source_phrase_ar":"الزور الكذب لأنه مائل عن طريقة الحق (maqayis)؛ الصنم زور (maqayis)؛ الزور قول الكذب وشهادة الباطل (ayn)؛ الزور الكذب (sihah)؛ الزور أيضا الزون وهو كل شيء يتخذ ربا ويعبد من دون الله (sihah)؛ قيل للكذب زور لكونه مائلا عن جهته (mufradat)؛ يسمى الصنم زورا (mufradat)","source_summary":"Kaynaklar yalanı doğruluk yolundan sapma olarak açıklar, yalancı tanıklığı bunun sözlü gerçekleşmesi sayar ve aynı adlandırmayı batıl tapınma nesnesine genişletir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الكذب وشهادة الباطل وقول الزور وما سمي زورا من الصنم أو المعبود الباطل لميله عن الحق","what_is_not_ar":"الزيارة؛ الميل الحسي؛ الصدر؛ تقويم الكلام قبل النطق"},"support_links":[]},{"boundary":"Dal birini görmek üzere ona yönelme ve bunun katılımcılarıyla sınırlıdır; konukluk, yalın yönelme veya tel ve keten anlamları bu çekirdeğe katılmaz.","branch_kind":"bare","branch_ref":"root_000654/B003","candidate_links":[{"candidate_id":"cand_606b2c685d8bd0489f94","lane":"micro"},{"candidate_id":"cand_87cb3e8a864dcce27623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"birini görmek için yanına gitme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi görmek veya onunla buluşmak için yanına gitme ve ona yönelme."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görmeye giden kişi ile bu kişilerden oluşan topluluğun adlandırılması."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Görmeye gelen kişiyi iyi karşılayıp ağırlama."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kadınların yanına sık gidip onlarla görüşmeyi ve sohbet etmeyi seven erkek."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylemin temel yönelme ve buluşma amacını verir; kişi, topluluk ve özel uzantılar bu çekirdeğe bağlıdır.","boundary_detail":"Dal birini görmek üzere ona yönelme ve bunun katılımcılarıyla sınırlıdır; konukluk, yalın yönelme veya tel ve keten anlamları bu çekirdeğe katılmaz.","branch_image_ar":"زيارة وقصد الزائر","concept_gloss":"birini görmek için yanına gitme","contextual_glosses":[{"applicability":"Bir kimseyi görmeye gelen tek kişi için doğal adlandırmadır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görmek ve buluşmak amacıyla gelen kişi rolünü korur."},"facet_ids":["F002"],"text":"ziyaretçi","usage_role":"contextual"},{"applicability":"Görmeye gelen kişiye iyi davranma ve onu ağırlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelen kişiyi iyi karşılayıp ağırlama eylemini korur."},"facet_ids":["F003"],"text":"ziyaretçiyi ağırlamak","usage_role":"contextual"}],"definition":"Bir kimseyi görmek veya onunla buluşmak amacıyla yanına gitmek ve ona yönelmektir; bu eylemi yapan kişi ya da topluluk da aynı anlam alanındadır. Ziyaretçiyi ağırlama ve kadınlarla sık görüşüp sohbet eden erkek anlamları özel kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi görmek veya onunla buluşmak için yanına gitme ve ona yönelme."},{"facet_id":"F002","role":"extension","statement":"Görmeye giden kişi ile bu kişilerden oluşan topluluğun adlandırılması."},{"facet_id":"F003","role":"associated_use","statement":"Görmeye gelen kişiyi iyi karşılayıp ağırlama."},{"facet_id":"F004","role":"specialization","statement":"Kadınların yanına sık gidip onlarla görüşmeyi ve sohbet etmeyi seven erkek."}],"identity_rationale":"Kaynak ifadesi bir kişiye yönelip onu görmeye gitme eylemini, bu eylemi yapan kişiyi ve topluluğu açıkça tanıklar. Ziyaretçiyi ağırlama ile kadınlarla sık görüşen erkek anlamları, aynı alandaki özel ve bağımlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birini görmeye gitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ziyaretçi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ziyaretçiler veya ziyaretçi topluluğu"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ziyaret"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ziyaret ettirmek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ziyarete çağırmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birbirini ziyaret etmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ziyaret veya ziyaret yeri"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ziyaretçiyi ağırlama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kadınlarla sık görüşüp sohbet eden erkek"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım görmeye gitme eylemini temel alır ve özel kişi ya da ağırlama kullanımlarını bu çekirdeğe bağımlı tutar.","neighbor_coverage_note":"Tüm adaylar incelendi; konukluk ve hedefe yönelme dalları en yararlı iki sınırı verdi, haber öğrenme, sabah gelme ve çağırma gibi yalnızca aynı olay alanındaki adaylar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ziyaret kısa ya da amaçlı bir görmeye gitme eylemidir; konukluk ise bir topluluğun yanına inme ve ağırlanma ilişkisini kurar.","focus_only":"Odak dal, bir kişiyi görmek için yanına gitme eylemini ve ziyaretçi rolünü merkez alır.","gloss":"ziyaret ile konukluk","neighbor_only":"Komşu dal, bir topluluğun yanına konuk olarak inme, barınma, ağırlanma ve konuk isteme ilişkilerini kapsar.","neighbor_ref":"root_000924/B002","relation_type":"same_field","shared_zone":"İki dalda da bir kişinin başka kişilerin yanına gelmesi ve toplumsal karşılanma durumu vardır."},{"boundary_match":"partial","distinction":"Odak dal kişiler arası görmeye gitmeyle sınırlıdır; komşu dalın hedefi kişi olmak zorunda değildir ve dinsel gidişi de kapsar.","focus_only":"Odak dalın hedefi görülecek bir kişidir ve ziyaretçi rolünü de adlandırır.","gloss":"bir hedefe yönelip gitme","neighbor_only":"Komşu dal, önemli bir şeye yönelmeyi ve dinsel amaçlı gidişi de kapsayan daha geniş bir hedefleme alanına sahiptir.","neighbor_ref":"root_000295/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da belirli bir hedefe yönelme ve onun bulunduğu yere gitme vardır."}],"source_phrase_ar":"الزائر لأنه إذ زارك فقد عدل عن غيرك (maqayis)؛ التزوير كرامة الزائر (maqayis)؛ الزور الذي يزورك واحدا كان أو جميعا (ayn)؛ زرته أزوره زورا وزيارة وزوارة (sihah)؛ التزوير كرامة الزائر (sihah)؛ الزير من الرجال الذي يحب محادثة النساء ومجالستهن سمي بذلك لكثرة زيادته لهن (sihah)؛ زرت فلانا تلقيته بزوري أو قصدت زوره (mufradat)؛ رجل زائر وقوم زور (mufradat)","source_summary":"Kaynaklar, görmeye gitme eylemi ile ziyaretçi ve ziyaretçi topluluğunu ortak biçimde tanıklar; ağırlama ve kadınlarla sık görüşen erkek kullanımları bu alanın özel uzantılarıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الزيارة والزائر والزور بمعنى الزوار وإكرام الزائر وكثرة قصد النساء ومحادثتهن في لفظ الزير عند الصحاح","what_is_not_ar":"الكذب؛ الصدر؛ الزير بمعنى الوتر أو الكتان؛ الميل المجرد"},"support_links":["sup_7e3e381c016bca983319","sup_967469edc9c7278cc1ee"]},{"boundary":"Tanım göğüs bölgesi ve buradaki eğrilik çekirdeğini korur; araç adlarını ve güçlü kişi kullanımını çekirdekle eşitlemez.","branch_kind":"bare","branch_ref":"root_000654/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"göğsün üst veya orta bölümü ve buradaki eğrilik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvanda göğsün üst ya da orta bölümü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göğüs yapısının bir yanında içe, öbür yanında dışa doğru beliren eğrilik veya biçim bozukluğu."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin göğsüne bağlanan kayış veya bir hayvanın ağzını çevirmeye yarayan araç."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göğsün gücüyle ilişkilendirilerek güçlü ve sert kişi için verilen sıra dışı kullanım."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan göğsünün belirtilen bölümünü ve bu bölümdeki yapısal eğriliği birlikte karşılar.","boundary_detail":"Tanım göğüs bölgesi ve buradaki eğrilik çekirdeğini korur; araç adlarını ve güçlü kişi kullanımını çekirdekle eşitlemez.","branch_image_ar":"زَوْر الصدر وميله","concept_gloss":"göğsün üst veya orta bölümü ve buradaki eğrilik","contextual_glosses":[{"applicability":"Bir insan veya hayvanın göğüs yapısındaki yana eğriliği anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğüs bölgesindeki yapısal eğrilik ve biçim bozukluğunu korur."},"facet_ids":["F002"],"text":"göğsü eğri","usage_role":"contextual"},{"applicability":"Devenin göğsüne bağlanan kayış ile hayvanın ağzını çevirmede kullanılan aracı açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın göğse bağlanma veya hayvanın ağzını çevirme işlevini korur."},"facet_ids":["F003"],"text":"göğüs kayışı veya ağız çevirme aracı","usage_role":"explanatory"}],"definition":"Göğsün üst veya orta bölümü ile bu bölgede görülen yana eğriliktir. Göğse bağlanan araçlar ilişkili adlandırmalar, güçlü ve sert kişi anlamı ise olağan çekirdeğin dışındaki bir uzantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvanda göğsün üst ya da orta bölümü."},{"facet_id":"F002","role":"specialization","statement":"Göğüs yapısının bir yanında içe, öbür yanında dışa doğru beliren eğrilik veya biçim bozukluğu."},{"facet_id":"F003","role":"associated_use","statement":"Devenin göğsüne bağlanan kayış veya bir hayvanın ağzını çevirmeye yarayan araç."},{"facet_id":"F004","role":"source_variant","statement":"Göğsün gücüyle ilişkilendirilerek güçlü ve sert kişi için verilen sıra dışı kullanım."}],"identity_rationale":"Kaynak ifadesi göğsün üst veya orta bölümünü ve bu bölümdeki eğriliği doğrudan tanıklar. Göğse bağlanan kayış ile hayvanın ağzını çevirmeye yarayan araç ilişkili kullanımlardır; güçlü kişi anlamı ise kaynağın olağan çekirdeğin dışında saydığı ayrı bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"göğsün üst veya orta bölümü"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"göğsü eğri"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"göğsü eğri olduğu için düzeltilen deve"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"devenin göğsüne bağlanan kayış veya hayvanın ağzını çevirmeye yarayan araç"}],"lexicalization_note":"Dal yalın göğüs bölgesi ve göğüsteki eğrilik anlamına dayanır; araç ve kişi kullanımları bu yalın çekirdeğin bağımlı uzantıları olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; göğsün belirli ön bölgesi ile kaburga dalı anatomik sınırı en iyi gösterdi, burun, kol, ayrılma ve beden iriliği adayları yalnızca uzak benzerlik taşıdığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha geniş bir üst veya orta göğüs bölgesini ve eğriliği taşırken komşu dal daha belirli bir göğüs yüzeyiyle sınırlıdır.","focus_only":"Odak dal göğsün üst veya orta bölümünü, bu bölümün eğriliğini ve onunla ilişkili araçları kapsar.","gloss":"göğüs bölgesi","neighbor_only":"Komşu dal göğüsteki belirli bir ön bölgeyi ve kayışın göğüs üzerinde geçtiği yeri adlandırır.","neighbor_ref":"root_001342/B005","relation_type":"near_neighbor","shared_zone":"İki dal da göğsün ön tarafındaki anatomik alanı adlandırır."},{"boundary_match":"field_only","distinction":"Biri göğsün bölgesini ve biçimini, diğeri ise bu bölgeyi oluşturan kaburga kemiklerini adlandırır; olağan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal göğsün üst veya orta yüzeyini ve bu yüzeydeki eğriliği anlatır.","gloss":"göğüs yüzeyi ve kaburgalar","neighbor_only":"Komşu dal göğüs boşluğunu çevreleyen ve orta göğüste birleşen kaburgaları adlandırır.","neighbor_ref":"root_000263/B005","relation_type":"same_field","shared_zone":"Her iki dal göğüs anatomisinin birbirine yakın bölümleriyle ilgilidir."}],"source_phrase_ar":"الزور وسط الصدر (ayn)؛ الزور ميل في وسط الصدر (ayn)؛ كلب أزور استدق جوشن زوره (ayn)؛ الزيار سفاف يشد به الرحل إلى صدر البعير (ayn)؛ الزور أعلى الصدر (sihah)؛ الزور في صدر الفرس دخول إحدى الفهدتين وخروج الأخرى (sihah)؛ الزيار ما يزير به البيطار الدابة (sihah)؛ الزور أعلى الصدر (mufradat)؛ الزور ميل في الزور (mufradat)؛ الزور القوي الشديد من الزور وهو أعلى الصدر شاذ عن الأصل (maqayis)","source_summary":"Kaynaklar göğsün üst veya orta bölümünde ve buradaki eğrilikte birleşir; göğse bağlanan araçlar ilişki yoluyla, güçlü kişi anlamı ise sıra dışı bir uzantı olarak verilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه أعلى الصدر أو وسطه وميل الصدر في الإنسان والحيوان وما شد إلى صدر البعير أو عولج به الفم واللحي وما ألحقه ابن فارس من القوي الشديد","what_is_not_ar":"الكذب؛ الزيارة؛ الميل المعنوي؛ الزعامة"},"support_links":[]},{"boundary":"Yöneticilik yalın kişi adıdır; görüş veya başvuru dayanağının yokluğu yalnız verilen olumsuz söz kalıbına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000654/B005","candidate_links":[{"candidate_id":"cand_f7db2d1097b9125b14d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"başvurulan önder veya dayanak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluğun işini yöneten, üyelerin kendisine başvurduğu önder."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli olumsuz söz kalıbında dayanılacak görüşün veya başvurulacak bir merciin bulunmaması."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimde topluluğun önderini, özel olumsuz kalıpta ise görüş ve başvuru dayanağını karşılar.","boundary_detail":"Yöneticilik yalın kişi adıdır; görüş veya başvuru dayanağının yokluğu yalnız verilen olumsuz söz kalıbına bağlıdır.","branch_image_ar":"مرجع وزعامة يمال إليها","concept_gloss":"başvurulan önder veya dayanak","contextual_glosses":[{"applicability":"Bir topluluğun işini yöneten ve üyelerin kendisine başvurduğu kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yöneticilik ve başvurulan kişi olma özelliklerini birlikte korur."},"facet_ids":["F001"],"text":"topluluğun önderi","usage_role":"contextual"},{"applicability":"Kişinin geri döneceği sağlam bir görüş veya başvuracağı dayanak bulunmadığını söyleyen özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüş ve başvuru dayanağının bulunmaması anlamını korur."},"facet_ids":["F002"],"text":"dayanacağı görüşü yok","usage_role":"contextual"}],"definition":"Bir topluluğun işlerini yöneten, insanların kendisine başvurduğu önderdir. Özel olumsuz söz kalıbında ise kişinin dayanacağı bir görüşünün veya başvuracağı bir merciinin bulunmamasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluğun işini yöneten, üyelerin kendisine başvurduğu önder."},{"facet_id":"F002","role":"specialization","statement":"Belirli olumsuz söz kalıbında dayanılacak görüşün veya başvurulacak bir merciin bulunmaması."}],"identity_rationale":"Kaynak ifadesi, topluluğun işlerini yöneten ve başvurulan kişiyi tanıklar; ayrıca kişinin geri döneceği görüş veya dayanak bulunmamasını belirli bir söz kalıbında verir. Bu iki kullanım başvuru noktası olma ilişkisiyle bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"topluluğun önderi veya işlerini yöneten kişi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"dayanacağı görüşü veya başvuracağı mercii yok"}],"lexicalization_note":"Dal yalın yönetici adını ve özel olumsuz söz kalıbını ayrı tutar; söz kalıbındaki görüş veya dayanak anlamı yalın biçime genellenmez.","neighbor_coverage_note":"Bütün komşular incelendi; baş olma ve topluluk adına önderlik etme dalları en yakın sınırları sağladı, yalnız efendilik, danışma topluluğu veya yönetici atama anlamları daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda insanların yöneldiği başvuru noktası olma belirgindir; komşu dalda önde gelme ve bir grubun başı sayılma kapsamı daha geniştir.","focus_only":"Odak dal, önderi topluluğun işlerinde başvurulan kişi olarak kurar ve görüş dayanağına ilişkin özel bir kullanım taşır.","gloss":"başvurulan topluluk önderi","neighbor_only":"Komşu dal, önde bulunmayı ve güçlü ya da kalabalık bir topluluğun baş sayılmasını da kapsar.","neighbor_ref":"root_000529/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da topluluğun önünde bulunan ve onu yöneten kişi vardır."},{"boundary_match":"partial","distinction":"Odak dalın sınırı başvuru noktası olan yöneticiye dayanır; komşu dal yöneticiliği soyluluk, temsil ve pay üstünlüğüyle genişletir.","focus_only":"Odak dal, topluluk işlerinde başvurulan önderi ve görüş dayanağına ilişkin özel olumsuz kullanımı içerir.","gloss":"topluluğun yöneticisi","neighbor_only":"Komşu dal, soyluluk, üstün pay ve topluluk adına konuşma görevini yöneticilikle birlikte kapsar.","neighbor_ref":"root_000633/B004","relation_type":"near_synonym","shared_zone":"İki dal topluluğu yöneten ve onun adına ağırlık taşıyan kişi anlamında örtüşür."}],"source_phrase_ar":"لرئيس القوم وصاحب أمرهم الزوير وذلك أنهم يعدلون عن كل أحد إليه (maqayis)؛ رجل ليس له زور أي ليس له صيور يرجع إليه (maqayis)؛ ماله زور ولا صيور أي رأي يرجع إليه (sihah)؛ الزوير زعيم القوم (sihah)","source_summary":"Kaynaklar topluluğun yöneticisini herkesin yöneldiği kişi olarak tanıklar ve özel olumsuz kullanımda başvurulacak görüş ya da dayanak bulunmamasını bildirir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه الزوير رئيس القوم وصاحب أمرهم وما يرجع إليه من رأي أو صيور","what_is_not_ar":"الكذب؛ الزيارة؛ الصدر؛ الميل المكاني"},"support_links":["sup_3140071eceb5acbeecd7"]},{"boundary":"Dal hazırlama, düzeltme ve süsleme işlemini anlatır; ortaya çıkan yalanı veya batıl içeriği kendi başına adlandırmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000654/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"önceden hazırlayıp düzeltme ve süsleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi ortaya çıkarmadan önce zihinde hazırlama, düzeltme ve biçimlendirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söylenecek sözü konuşmadan önce düşünüp düzgün bir biçime getirme."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi iyileştirip güzelleştirme veya yalanı inandırıcı görünecek biçimde süsleme."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözü düzenleme kullanımının yalanın kendisinden değil, sözü içte hazırlama düşüncesinden türetildiği açıklaması."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel hazırlamayı, sözün önceden düzenlenmesini ve bir şeyin iyi ya da aldatıcı biçimde süslenmesini birlikte karşılar.","boundary_detail":"Dal hazırlama, düzeltme ve süsleme işlemini anlatır; ortaya çıkan yalanı veya batıl içeriği kendi başına adlandırmaz.","branch_image_ar":"تزوير الكلام وتقويمه","concept_gloss":"önceden hazırlayıp düzeltme ve süsleme","contextual_glosses":[{"applicability":"Bir kişinin söyleyeceği sözü konuşmadan önce düşünüp biçimlendirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün konuşulmadan önce zihinde hazırlanıp düzeltilmesini korur."},"facet_ids":["F002"],"text":"sözü önceden düzenlemek","usage_role":"contextual"},{"applicability":"Yalanın daha çekici veya inandırıcı görünmesi için biçimlendirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yalanı aldatıcı biçimde güzelleştirme ve süsleme işlemini korur."},"facet_ids":["F003"],"text":"yalanı süslemek","usage_role":"contextual"}],"definition":"Bir şeyi ortaya koymadan önce zihinde hazırlamak veya onu düzeltip daha iyi bir biçime getirmektir. Söz için konuşmadan önce düzenlemeyi, yalan içinse aldatıcı biçimde süslemeyi anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi ortaya çıkarmadan önce zihinde hazırlama, düzeltme ve biçimlendirme."},{"facet_id":"F002","role":"specialization","statement":"Söylenecek sözü konuşmadan önce düşünüp düzgün bir biçime getirme."},{"facet_id":"F003","role":"extension","statement":"Bir şeyi iyileştirip güzelleştirme veya yalanı inandırıcı görünecek biçimde süsleme."},{"facet_id":"F004","role":"source_variant","statement":"Sözü düzenleme kullanımının yalanın kendisinden değil, sözü içte hazırlama düşüncesinden türetildiği açıklaması."}],"identity_rationale":"Kaynak ifadesi zihinde hazırlama, sözü konuşmadan önce düzeltip düzenleme ve bir şeyi iyileştirme anlamlarını tanıklar. Yalanı süsleme bunun özel ve olumsuz bir gerçekleşmesidir; sözü hazırlama anlamı yalanın kendisiyle özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir şeyi zihninde hazırlamak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"sözü konuşmadan önce düzeltip düzenlemek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bir şeyi düzeltip güzelleştirme veya yalanı süsleme"}],"lexicalization_note":"Dal yalın iyileştirme ve zihinde hazırlama kullanımlarıyla sözü önceden düzenleme kalıbını ayırır; kalıba bağlı konuşma anlamı bütün dala yayılmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; aldatıcı süslü söz ve sözü etkileyici kılma dalları en yakın karşılaştırmaları verdi, şiir, genel hazırlık, dil bükme ve salt ekleme adayları daha dolaylı kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal nötr hazırlama ve düzeltmeyi de kapsayan bir işlemdir; komşu dalın çekirdeği ise süslü görünüş yoluyla aldatıcı söz üretmektir.","focus_only":"Odak dal, yalanla sınırlı olmayan zihinsel hazırlama, düzeltme ve önceden söz kurma işlemlerini kapsar.","gloss":"sözü süsleme ve düzenleme","neighbor_only":"Komşu dal, dışarıdan güzel görünen fakat yalanla aldatmayı amaçlayan süslü sözü doğrudan adlandırır.","neighbor_ref":"root_000628/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sözün etkili görünmesi için biçimlendirilmesi ve süslenmesi bulunur."},{"boundary_match":"partial","distinction":"Odak dal hazırlama ve düzeltme aşamasına dayanır; komşu dal ekleme ve dinleyeni etkileme sonucuna odaklanır.","focus_only":"Odak dal sözün konuşulmadan önce zihinde hazırlanmasını ve bir şeyin düzeltilmesini içerir.","gloss":"sözü çekici biçime getirme","neighbor_only":"Komşu dal söze sonradan ekleme yaparak dinleyenin kulağını veya gönlünü ona yöneltme etkisini öne çıkarır.","neighbor_ref":"root_000860/B006","relation_type":"near_neighbor","shared_zone":"İki dal da sözün daha etkili veya güzel görünmesi için işlenmesini kapsar."}],"source_phrase_ar":"زور الشيء في نفسه هيأه (maqayis)؛ الإنسان يزور كلاما أي يقومه قبل أن يتكلم به (ayn)؛ لم يشتق تزوير الكلام منه ولكن من تزوير الصدر (ayn)؛ التزوير تزيين الكذب (sihah)؛ زورت الشيء حسنته وقومته (sihah)","source_summary":"Kaynaklar zihinde hazırlama, sözü konuşmadan önce düzenleme ve bir şeyi düzeltip güzelleştirme işlemlerini verir; yalanı süsleme bu işlemin olumsuz özel uygulamasıdır.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه تهيئة الشيء في النفس وتقويم الكلام قبل النطق وتحسين الشيء أو تزيين الكذب في لفظ التزوير","what_is_not_ar":"الزور بمعنى الكذب نفسه؛ التزوير بمعنى كرامة الزائر؛ الصدر"},"support_links":[]},{"boundary":"Dal şiddetli yol alışla sınırlıdır; genel hız, kesintisiz sürme, koşu veya baş eğerek ilerleme gibi ek koşullar yüklenmez.","branch_kind":"bare","branch_ref":"root_000654/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"şiddetli yol alış","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güçlü, yoğun ve şiddetli biçimde yol alma."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin hangi araçla veya ne kadar sürdüğü belirtilmeden, yalnız yoğun ve güçlü oluşunu karşılar.","boundary_detail":"Dal şiddetli yol alışla sınırlıdır; genel hız, kesintisiz sürme, koşu veya baş eğerek ilerleme gibi ek koşullar yüklenmez.","branch_image_ar":"سير شديد","concept_gloss":"şiddetli yol alış","contextual_glosses":[{"applicability":"Yol almanın yoğun ve güçlü gerçekleştiği hareket bağlamlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlerlemenin güçlü ve yoğun gerçekleşmesi anlamını korur."},"facet_ids":["F001"],"text":"güçlü biçimde ilerlemek","usage_role":"contextual"}],"definition":"Yol almanın güçlü, yoğun ve şiddetli biçimde gerçekleşmesidir; süreklilik, belirli bir taşıt veya özel beden duruşu zorunlu değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güçlü, yoğun ve şiddetli biçimde yol alma."}],"identity_rationale":"Kaynak ifadesi bu dalı doğrudan şiddetli ve güçlü yol alış olarak tanıklar. Başka bir katılımcı, sonuç veya özel bağlam belirtilmediği için tanım yalnız hareketin yoğunluğunu korur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"şiddetli yol alış"}],"lexicalization_note":"Dal yalın kullanıma dayanır ve yalnız şiddetli yol alış anlamını taşır; komşu hareket türlerinin ek koşulları tanıma alınmaz.","neighbor_coverage_note":"Bütün hareket adayları incelendi; hız ve kesintisizliği açıkça ekleyen iki dal sınırı en iyi gösterdi, koşu, araziye yayılma, boyun indirme ve yalnız ilerleme adayları daha özel kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda şiddet belirleyicidir; komşu dalda ise hız ve duraksamadan ilerleme ayrıca anlamın parçasıdır.","focus_only":"Odak dal hareketin güçlü ve şiddetli oluşunu bildirir, açıkça hız veya kesintisizlik koşulu koymaz.","gloss":"şiddetli ve hızlı yol alış","neighbor_only":"Komşu dal hız, acelecilik ve gevşemeden sürme özelliklerini açıkça taşır.","neighbor_ref":"root_000293/B002","relation_type":"near_synonym","shared_zone":"İki dal da sıradan hareketten daha yoğun bir ilerleyişi anlatır."},{"boundary_match":"partial","distinction":"Şiddetli yol alış kısa süreli de olabilir; komşu dalın çekirdeğinde ise hızla birlikte kesintisiz devam etme vardır.","focus_only":"Odak dal yalnız yol alışın şiddetini bildirir ve uzun süre devam etme gerektirmez.","gloss":"durmaksızın hızlı ilerleme","neighbor_only":"Komşu dal hareketin hızlı olmasını ve duraklama ya da gevşeme göstermeden sürmesini gerektirir.","neighbor_ref":"root_001223/B008","relation_type":"near_synonym","shared_zone":"Her iki dalda da yoğun bir yol alma biçimi bulunur."}],"source_phrase_ar":"الزور مثال الهجف السير الشديد (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Sözcük, güçlü ve şiddetli biçimde yol alma anlamıyla tek başına tanıklanır."}],"source_summary":"Paylaşılan çok kaynaklı bir özet yoktur; anlam tekil bir tanıklıkta şiddetli yol alış olarak verilir.","sources":["SI"],"what_is_ar":"يدخل فيه الزور بمعنى السير الشديد","what_is_not_ar":"الكذب؛ الميل؛ الزيارة؛ الصدر"},"support_links":[]},{"boundary":"Dal iki ayrı nesne adını korur; bunlardan genel iplik, ağaç parçası veya bağlama aracı anlamı çıkarılmaz.","branch_kind":"unresolved","branch_ref":"root_000654/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","surface_ar":"زُرْ"}],"gloss":"ince tel veya kiriş; ayrıca keten","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnce bir tel veya kiriş için kullanılan nesne adı."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçimin keten için verilen ayrı nesne adı."}}],"root_ar":"ز و ر","root_id":"root_000654","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirine indirgenmeyen iki tanıklı nesne adını aralarında açıklanmamış bir bağ kurmadan birlikte gösterir.","boundary_detail":"Dal iki ayrı nesne adını korur; bunlardan genel iplik, ağaç parçası veya bağlama aracı anlamı çıkarılmaz.","branch_image_ar":"الزِّير الوتر والكتان","concept_gloss":"ince tel veya kiriş; ayrıca keten","contextual_glosses":[{"applicability":"Nesnenin ince bir tel ya da gerilmiş kiriş olarak adlandırıldığı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin tel veya kiriş türünden ve ince oluşunu korur."},"facet_ids":["F001"],"text":"ince tel veya kiriş","usage_role":"explanatory"},{"applicability":"Biçimin doğrudan keten bitkisi veya keten maddesi için kullanıldığı bağlama aittir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynakta ayrı olarak verilen keten nesnesini doğrudan karşılar."},"facet_ids":["F002"],"text":"keten","usage_role":"contextual"}],"definition":"Bir kullanımda ince bir tel veya kiriş, başka bir kullanımda ise keten için verilen addır. İki nesne arasında ortak bir anlam ilişkisi kurulmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnce bir tel veya kiriş için kullanılan nesne adı."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçimin keten için verilen ayrı nesne adı."}],"identity_rationale":"Kaynak ifadesi aynı biçim için iki ayrı adlandırma verir: ince bir tel veya kiriş ve keten. Bunlar ortak bir nesne sınıfıymış gibi birleştirilemez; dal ancak iki tanıklı anlamı yan yana ve aralarında ilişki varsaymadan korursa kullanılabilir.","lexicalization_note":"Yalınlık durumu çözümlenmemiştir; tanım yalnız kaynakta verilen ince tel veya kiriş ile keten adlarını kaydeder ve biçimin kapsamını genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ince iplik ile gevşek bükümlü iplik dalları sınırı en iyi gösterdi, ağaç parçası, kayış, hayvansal kiriş ve halat bükümü adayları daha özel nesneler olduğu için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tel veya kiriş anlamı daha dar bir nesne adıdır ve ayrıca keten anlamı vardır; komşu dal ise genel ince iplik ve tel alanına uzanır.","focus_only":"Odak dal ince tel veya kiriş anlamının yanında ayrı bir keten anlamı da taşır.","gloss":"ince tel veya iplik","neighbor_only":"Komşu dal genel olarak uzanan ince ipliği ve ince teli kapsar, fakat keten adını taşımaz.","neighbor_ref":"root_000453/B001","relation_type":"near_neighbor","shared_zone":"İki dal ince ve uzun bir tel ya da iplik benzeri nesne alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dal yalnız ince tel veya kiriş adını verir; komşu dal ise ipliğin gevşek bükümünü ya da tek katlı oluşunu zorunlu özellik sayar.","focus_only":"Odak dal ince tel veya kiriş ile ayrı olarak keteni adlandırır.","gloss":"ince kiriş ve gevşek iplik","neighbor_only":"Komşu dal gevşek bükülmüş veya tek katlı iplik, ip ya da halatı yapısal niteliğiyle adlandırır.","neighbor_ref":"root_000684/B007","relation_type":"same_field","shared_zone":"Her iki dal iplik veya tel benzeri uzun ve ince nesnelerle ilişkilidir."}],"source_phrase_ar":"الزير من الأوتار الدقيق؛ والزير الكتان (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Aynı biçim, ince tel veya kiriş ve ayrıca keten için tek başına tanıklanır."}],"source_summary":"Paylaşılan çok kaynaklı bir özet yoktur; tekil tanıklık ince tel veya kiriş ile keten adlarını ayrı anlamlar olarak verir.","sources":["SI"],"what_is_ar":"يدخل فيه الزِّير للوتر الدقيق والكتان على رواية الصحاح","what_is_not_ar":"زيارة النساء؛ الزائر؛ الكذب؛ الميل؛ الصدر"},"support_links":[]},{"boundary":"Dal, kuş adını, burunla ilgili kullanımları ve alçak ya da gizli şeylere ilişkin ayrı anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B001","candidate_links":[{"candidate_id":"cand_606b2c685d8bd0489f94","lane":"micro"},{"candidate_id":"cand_f7db2d1097b9125b14d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","surface_ar":"مَقَابِرَ"}],"gloss":"ölüyü gömme, ona gömü yeri sağlama ve gömü yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gömüt, ölünün gömüldüğü ve kalacağı yerdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem olarak ölüyü gömmek, onu gömü yerine koymaktır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, ölüye gömü yeri sağlama, onu gömülecek duruma getirme veya gömülmesine izin verme ayrımını taşır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yer adı, gömütlerin bir arada bulunduğu alanı da belirtir."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, doğrudan gömme, gömülmeyi sağlama ve toplu gömü alanı yönlerini birlikte temsil eder.","boundary_detail":"Dal, kuş adını, burunla ilgili kullanımları ve alçak ya da gizli şeylere ilişkin ayrı anlamları kapsamaz.","branch_image_ar":"مواراة الميت في القبر","concept_gloss":"ölüyü gömme, ona gömü yeri sağlama ve gömü yeri","contextual_glosses":[{"applicability":"Ölüyü doğrudan gömü yerine koyma eyleminin geçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğrudan gömme eylemini ve ölü katılımcısını eksiksiz korur."},"facet_ids":["F002"],"text":"ölüyü gömmek","usage_role":"general"},{"applicability":"Kişinin ölüyü kendi eliyle gömmesinden çok, onun gömülmesini mümkün kıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gömme eylemi ile gömülmeyi sağlama arasındaki katılımcı farkını korur."},"facet_ids":["F003"],"text":"ölüye gömü yeri sağlamak","usage_role":"explanatory"},{"applicability":"Birden çok gömütün yer aldığı toplu gömü alanı kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek gömüt ile toplu gömü alanı arasındaki kapsam ayrımını korur."},"facet_ids":["F004"],"text":"gömütlerin bulunduğu alan","usage_role":"contextual"}],"definition":"Ölünün konulduğu gömü yerini ve ölüyü bu yere koyma eylemini; ayrıca ölüye böyle bir yer sağlama, gömülmesine izin verme ve gömütlerin bulunduğu yeri anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gömüt, ölünün gömüldüğü ve kalacağı yerdir."},{"facet_id":"F002","role":"core","statement":"Eylem olarak ölüyü gömmek, onu gömü yerine koymaktır."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, ölüye gömü yeri sağlama, onu gömülecek duruma getirme veya gömülmesine izin verme ayrımını taşır."},{"facet_id":"F004","role":"extension","statement":"Yer adı, gömütlerin bir arada bulunduğu alanı da belirtir."}],"identity_rationale":"Kaynak ifadesi bu dalı ölünün gömüldüğü yer, ölüyü oraya koyma eylemi, ölüye gömü yeri sağlama ya da gömme izni verme ve gömütlerin toplandığı yer çevresinde açıkça kurar. Geçişli gömme eylemi ile birine gömü yeri sağlama anlamı aynı sayılmamalı, dal içinde ayrı yönler olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ölünün gömüldüğü yer; gömüt"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ölüyü gömmek ve gömü yerine koymak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ölüyü gömü yerine koyma işi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ölüye gömü yeri sağlamak, gömülmesine izin vermek veya onu gömülecek duruma getirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ölü için gömü yeri hazırlama ve onu gömülmeye layık sayılanlar arasına koyma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu gömmemize izin ver"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ölüyü kendi eliyle gömen kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gömütlerin bulunduğu yer; mezarlık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gömüt yeri veya gömütlerin bulunduğu yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gömme işi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ölüye gömü yeri veren"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gömütler; mezarlıklar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"mezarlığa veya gömüt yerine ilişkin"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gömüt kazısında sana yardım eden kişi"}],"lexicalization_note":"Tanım yalın ad ve eylem çekirdeğini kapsar; gömme izni isteyen kalıplaşmış söz ile türemiş yer ve kişi adlarını kendi özel kapsamlarında tutar.","neighbor_coverage_note":"Listelenen bütün komşu kartları incelendi; gömme eylemi, örtüp gizleme, genel gizleme ve gömütün özel bölümüyle en açıklayıcı sınırları kuran dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gömme eyleminin gözden kaybolma sonucuna odaklanırken odak dal yer adlarını ve gömülmeyi sağlama ya da buna izin verme katılımcı ayrımını da korur.","focus_only":"Odak dal gömüt adını, toplu gömü alanını ve ölüye gömü yeri sağlama ayrımını da içerir.","gloss":"ölüyü gömerek gözden kaldırmak","neighbor_only":null,"neighbor_ref":"root_001117/B009","relation_type":"near_synonym","shared_zone":"Her iki dal da ölünün bir gömü yerine konulması eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği gömü yeri ve ölüyü oraya koymaktır; komşu dalın çekirdeği ise daha genel olarak ölüyü örtüp gizlemektir.","focus_only":"Odak dal gömüt, toplu gömü alanı ve gömülmeye yer ya da izin sağlama anlamlarını taşır.","gloss":"ölüyü örtüp gizlemek","neighbor_only":"Komşu dal ölüyü örtüp gizleme alanına kefeni ve başka örtünme adlarını da katar.","neighbor_ref":"root_000266/B009","relation_type":"near_neighbor","shared_zone":"İki dal ölünün gömülerek görünmez kılındığı cenaze işlemi alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal nesne ve yöntem bakımından geneldir; odak dal ise ölünün belirli bir gömü yerine konulması ve bu yerin sağlanması çevresinde uzmanlaşır.","focus_only":"Odak dal özellikle ölüyü, onun gömü yerini ve gömülmesine ilişkin rolleri konu eder.","gloss":"bir şeyi altına sokarak gizlemek","neighbor_only":"Komşu dal insan dışındaki herhangi bir şeyin toprakta veya başka bir şeyin altında gizlenmesini kapsar.","neighbor_ref":"root_000475/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı toprağın altında görünmez kılma durumu bulunabilir."},{"boundary_match":"field_only","distinction":"Odak dal genel gömü yeri ve gömme eylemidir; komşu dal bu yerin içindeki belirli bir mimari bölümle sınırlıdır.","focus_only":"Odak dal gömütün bütününü, gömme eylemini ve gömütlerin bulunduğu alanı kapsar.","gloss":"gömütün yanındaki özel oyuk","neighbor_only":"Komşu dal gömütün yan tarafında açılan özel oyuğu ve ölünün oraya yerleştirilmesini belirtir.","neighbor_ref":"root_001345/B002","relation_type":"same_field","shared_zone":"İki dal aynı gömme düzeninin yerlerini ve işlemlerini konu eder."}],"source_phrase_ar":"القبر قبر الميت (maqayis)؛ القبر مدفن الإنسان (tahdhib)؛ القبر مقر الميت (mufradat)؛ قبرت الميت أي دفنته (jamhara;sihah;tahdhib)؛ أقبرته جعلت له مكانا يقبر فيه (maqayis;mufradat)؛ المقبرة موضع القبور (ayn;jamhara;tahdhib;mufradat)","source_summary":"Kaynakların ortak anlatımı ölünün gömüldüğü yeri, ölüyü gömme eylemini, ona gömü yeri sağlama veya gömme izni verme ayrımını ve gömütlerin bulunduğu alanı birlikte destekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه القبر مدفن الميت ومقره، وقبر الميت أي دفنه وجعله في القبر، وأقبره أي جعل له قبرا أو أذن في قبره أو صيره ذا قبر، والمقبرة موضع القبور","what_is_not_ar":"ليس القُبَّرة الطائر ولا طرف الأنف ولا غموض الأرض والنخل إلا من جهة الأصل العام"},"support_links":["sup_3140071eceb5acbeecd7","sup_967469edc9c7278cc1ee"]},{"boundary":"Genel çekirdek gizli, içe gömülü veya alçakta kalma durumudur; özel bitki, arazi ve doğum kullanımları bu çekirdeğin yerine geçmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B002","candidate_links":[{"candidate_id":"cand_87cb3e8a864dcce27623","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","surface_ar":"مَقَابِرَ"}],"gloss":"gizli, alçakta veya içe gömülü kalma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirsiz, gizli, alçalmış veya içe çekilmiş durumda bulunması temel anlam alanını oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi için kullanım, çukurda kalan ve kolay seçilmeyen yeri anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hurma ağacı için kullanım, ürünün yaprakların arasında saklı kalmasını belirtir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hoş kokulu ağacın içinde aşınmış ve gevşemiş oyuk bölüm bu adla anılır."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Yeni doğan için kullanım, bedenin yarıksız ve deliksiz kapalı bir zarla çevrili olmasını anlatır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel durum çekirdeğini ve özel kullanımları birbirine karıştırmadan ortaklaştırır.","boundary_detail":"Genel çekirdek gizli, içe gömülü veya alçakta kalma durumudur; özel bitki, arazi ve doğum kullanımları bu çekirdeğin yerine geçmez.","branch_image_ar":"غموض الشيء وتطامنه","concept_gloss":"gizli, alçakta veya içe gömülü kalma","contextual_glosses":[{"applicability":"Araziyi niteleyen söz öbeğinde hem alçaklığı hem de kolay seçilmemeyi anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araziye bağlı alçaklık ve belirsizlik özelliklerini birlikte korur."},"facet_ids":["F002"],"text":"çukurda ve gözden ırak arazi","usage_role":"contextual"},{"applicability":"Yalnızca ürünün ağacın yaprakları arasında kaldığını anlatan bitki kullanımına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ürünün yapraklar arasında saklı kalması koşulunu tam olarak korur."},"facet_ids":["F003"],"text":"ürünü yapraklarında saklı hurma ağacı","usage_role":"explanatory"},{"applicability":"Yeni doğanın üzerinde yarık ya da delik bulunmayan bütün bir zar olduğu bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yeni doğanı çevreleyen zarın kapalı ve kesintisiz olma koşulunu korur."},"facet_ids":["F005"],"text":"kapalı bir zar içinde doğmuş çocuk","usage_role":"explanatory"}],"definition":"Bir şeyin belirgin olmaması, alçakta ya da içe gömülü kalması çekirdektir. Arazi çukurluğu, ürünün yapraklar arasında saklı kalması, ağacın içindeki gevşek oyuk ve kapalı bir zar içindeki yeni doğan bu çekirdeğin ayrı, sözcüksel olarak sınırlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirsiz, gizli, alçalmış veya içe çekilmiş durumda bulunması temel anlam alanını oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Arazi için kullanım, çukurda kalan ve kolay seçilmeyen yeri anlatır."},{"facet_id":"F003","role":"specialization","statement":"Hurma ağacı için kullanım, ürünün yaprakların arasında saklı kalmasını belirtir."},{"facet_id":"F004","role":"specialization","statement":"Hoş kokulu ağacın içinde aşınmış ve gevşemiş oyuk bölüm bu adla anılır."},{"facet_id":"F005","role":"specialization","statement":"Yeni doğan için kullanım, bedenin yarıksız ve deliksiz kapalı bir zarla çevrili olmasını anlatır."}],"identity_rationale":"Kaynak ifadesi dalın çekirdeğini bir şeyde belirsizlik, gizlilik ve alçalma olarak verir; arazi, hurma ağacı, hoş kokulu ağacın içi ve kapalı zarla doğan çocuk bunun farklı gerçekleşmeleridir. Bu örnekler tek bir yalın anlam gibi birleştirilemez; her biri kendi ad veya söz kalıbına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çukurda ve gözden ırak arazi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ürünü yapraklarının arasında saklı duran hurma ağacı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hoş kokulu ağacın içinde gevşeyip aşınmış oyuk bölüm"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"üzerinde yarıksız ve deliksiz kapalı bir zarla doğan çocuk"}],"lexicalization_note":"Yalın çekirdek ile arazi, hurma ağacı ve yeni doğan için kullanılan söz öbekleri ayrılır; söz öbeklerinin özel anlamları yalın köke genellenmez.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; alçalma, çukur arazi, derinleşme ve etkin gizleme ile sınırı en iyi gösteren dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği fiziksel alçalma ve içe girmedir; odak dal ise buna kolay seçilmeme ve çeşitli nesnelerde saklı kalma boyutunu ekler.","focus_only":"Odak dal belirsizlik ve gizliliği, ayrıca bitki, ağaç içi ve doğum kullanımlarını da kapsar.","gloss":"alçalmak ve içe girmek","neighbor_only":"Komşu dal evin geride kalması ile bacak ve ayaktaki çukur bölümler gibi başka içe girme örneklerini içerir.","neighbor_ref":"root_001107/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da alçalma, çukurlaşma veya dış yüzeyden içe çekilme görünümü vardır."},{"boundary_match":"partial","distinction":"Arazi bağlamında yakın karşılık olsalar da odak dalın kapsamı gizlilik çekirdeğine bağlı başka sözcüksel kullanımlara uzanır.","focus_only":"Odak dal belirsizliği ve arazi dışındaki yaprak, ağaç içi ve kapalı zar kullanımlarını da taşır.","gloss":"arazinin çukur iç bölümü","neighbor_only":"Komşu dal yer, vadi ve özel yer adları olarak kullanılan toprak içi çukurla sınırlıdır.","neighbor_ref":"root_000279/B004","relation_type":"near_synonym","shared_zone":"İki dal arazideki alçak ve içe çökmüş yer anlamında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal derinlik eksenine dayanır; odak dal için derinlik zorunlu değildir, belirgin olmama ve çevre içinde saklı kalma da yeterlidir.","focus_only":"Odak dal görünmezlik, ürünün yapraklarda saklanması ve kapalı zarla çevrilme gibi durumları içerir.","gloss":"derine inmek","neighbor_only":"Komşu dal suyun derinliği ile göz, yağ ve yaranın içeri girmesi gibi doğrudan derinleşme örneklerini içerir.","neighbor_ref":"root_001112/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzeyden aşağıda veya içeride bulunma durumunu paylaşır."},{"boundary_match":"partial","distinction":"Odak dal bir durum ve nitelik alanıdır; komşu dal ise bir nesneyi etkin biçimde gizleme işlemini anlatır.","focus_only":"Odak dal çoğunlukla bir şeyin kendiliğinden alçak, içte veya kapalı durumda olmasını bildirir.","gloss":"altına sokarak gizlemek","neighbor_only":"Komşu dal bir failin nesneyi başka bir şeyin altına sokup gizlemesi eylemini gerektirir.","neighbor_ref":"root_000475/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın sonucunda söz konusu şey görünmez veya zor seçilir duruma gelebilir."}],"source_phrase_ar":"أصل صحيح يدل على غموض في شيء وتطامن (maqayis)؛ أرض قبور غامضة (maqayis;jamhara;tahdhib)؛ نخلة قبور وكبوس يكون حملها في سعفها (maqayis;jamhara;tahdhib)؛ القبر موضع متأكل مسترخى في العود الذي يتطيب به وهو جوفه (ayn)؛ ولد مقبورا لأن عليه جلدة مصمتة ليس فيها شق ولا ثقب (tahdhib)","source_summary":"Kaynaklar belirsizlik ve alçalma çekirdeğini, çukur araziyi ve ürünü yapraklar arasında kalan hurma ağacını birlikte destekler; ayrıca ağaç içindeki gevşek oyuk ile kapalı zarla doğan çocuk özel örnekler olarak aktarılır.","sources":["MQ","AY","JA","TA"],"what_is_ar":"يدخل فيه الغموض والتطامن في الشيء، والأرض القبور الغامضة، والنخلة القبور التي يكون حملها في سعفها، وجوف عود الطيب المتأكل، والمقبور المحصور في جلدة مصمتة","what_is_not_ar":"ليس دفن الميت في القبر ولا المقبرة موضع القبور ولا القُبَّرة الطائر"},"support_links":["sup_7e3e381c016bca983319"]},{"boundary":"Dal yalnızca kuş adını ve onun dil biçimlerini kapsar; gömü, alçalma veya burun anlamlarıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","surface_ar":"مَقَابِرَ"}],"gloss":"belirli bir kuş türünün adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim belirli bir kuş türüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar aynı kuş adının birbiriyle bağlantılı tekil, çoğul ve söyleniş biçimlerini aktarır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtın türü daha dar biçimde tanımlamadığı bu kuş adı dalının tamamı için uygundur.","boundary_detail":"Dal yalnızca kuş adını ve onun dil biçimlerini kapsar; gömü, alçalma veya burun anlamlarıyla birleştirilmez.","branch_image_ar":"القُبَّرة الطائر","concept_gloss":"belirli bir kuş türünün adı","contextual_glosses":[{"applicability":"Ad biçimleri arasındaki ayrım önemli değilken kuş gönderimini doğal cümle içinde verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı türüne yapılan kuş gönderimini herhangi bir ek tür iddiası olmadan korur."},"facet_ids":["F001"],"text":"bir kuş türü","usage_role":"general"},{"applicability":"Bir biçimin aynı kuşu adlandıran dilsel bir değişke olduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ad biçimleri arasındaki değişke ilişkisini ve aynı gönderimi korur."},"facet_ids":["F002"],"text":"aynı kuş adının başka bir biçimi","usage_role":"explanatory"}],"definition":"Belirli bir kuş türü için kullanılan bir ad ile bu adın tekil, çoğul veya değişik söyleniş olarak aktarılan bağlantılı biçimlerini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim belirli bir kuş türüdür."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar aynı kuş adının birbiriyle bağlantılı tekil, çoğul ve söyleniş biçimlerini aktarır."}],"identity_rationale":"Kaynak ifadesi bu dalı belirli bir kuşun adı ve aynı adın birbiriyle ilişkili dil biçimleri olarak sınırlar. Kanıt kuşun daha dar tür kimliğini açıklamadığından, tanım kuş adı olmanın ötesinde tür belirlemez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"belirli bir kuş türünün tekil adı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aynı kuşun adı veya çoğul biçimi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"aynı kuş adının değişik söylenişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"aynı kuş için kullanılan başka bir ad biçimi"}],"lexicalization_note":"Dal, kuş için kullanılan ayrı ad biçimlerini kapsar; bu biçimler tek bir yalın kök anlamı varmış gibi genellenmez.","neighbor_coverage_note":"Adayların tümü ayrı hayvan veya kuş adları olarak denetlendi; tür özdeşliği göstermeyen kartlardan alan ortaklığını en açık gösteren üçü seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan yalnızca kuş adlandırmasıdır; kartlar farklı kuş adlarını verir ve aralarında tür özdeşliği kurulamaz.","focus_only":"Odak dal kendi kuş adını ve o adın bağlantılı dil biçimlerini belirtir.","gloss":"başka bir küçük kuş adı","neighbor_only":"Komşu dal serçegillerden olduğu söylenen başka bir kuşun özel adıdır.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"Her iki dal da bir kuş türünü adlandıran söz varlığına aittir."},{"boundary_match":"field_only","distinction":"Komşu kart görünüş ve bölge bilgisiyle başka bir kuşu tanımlar; odak kartta bu özellikler yoktur ve adlar birbirinin yerine geçmez.","focus_only":"Odak dal türü daha dar tanımlanmayan ayrı bir kuş adını ve biçimlerini kapsar.","gloss":"güvercine benzeyen kuş","neighbor_only":"Komşu dal güvercine benzeyen ve belirli bir bölgeyle ilişkilendirilen başka bir kuşu anlatır.","neighbor_ref":"root_001066/B009","relation_type":"same_field","shared_zone":"İki dal da kuş türü adları alanında yer alır."},{"boundary_match":"field_only","distinction":"Ad biçimlerinin bulunması yapısal bir benzerliktir; gönderilen kuş türleri farklı olduğundan anlam örtüşmesi yoktur.","focus_only":"Odak dal farklı biçimleri bulunan ayrı bir kuş adıdır.","gloss":"toy kuşu","neighbor_only":"Komşu dal toy kuşunu ve onunla bağlantılı ad biçimlerini belirtir.","neighbor_ref":"root_000287/B008","relation_type":"same_field","shared_zone":"Her iki dal kuş adlarını ve bu adlarla bağlantılı biçimleri içerir."}],"source_phrase_ar":"القبرة واحدة القبر وهو ضرب من الطير (sihah)؛ القنبراء لغة فيها (sihah)؛ يقال للقنبرة قبرة وقبر (tahdhib)","source_summary":"Kaynaklar aynı kuşun iki temel ad biçimini birlikte destekler; bunlardan biri diğerinin tekili olarak açıklanır ve kuş adı için ek bir söyleniş biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه القُبَّرة والقُبَّر اسما لطائر، وما يتصل بهما من لغة القنبرة والقنبراء","what_is_not_ar":"ليس القبر مدفن الإنسان ولا غموض الأرض والنخل ولا طرف الأنف"},"support_links":[]},{"boundary":"Burun ucu adları yalın anatomik kullanımlardır; öfkeli geliş anlamı ise yalnızca verilen söz kalıplarına bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","surface_ar":"مَقَابِرَ"}],"gloss":"burun ucu ve öfkeli gelişte burnun belirginleşmesi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalın anatomik kullanım burun ucunu adlandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Küçültme biçimi, çıkıntılı burnun baş kısmı için kullanılan ayrı bir addır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir söz kalıbı, burnu öne çıkmış görünerek öfkeli biçimde gelmeyi anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İkinci söz kalıbı da aynı biçimde öfkeli gelişi anlatan eş yapılı bir kullanımdır."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik adları ve yalnızca özel söz kalıplarında bulunan öfkeli geliş anlamını birlikte, fakat ayrımlı biçimde temsil eder.","boundary_detail":"Burun ucu adları yalın anatomik kullanımlardır; öfkeli geliş anlamı ise yalnızca verilen söz kalıplarına bağlıdır.","branch_image_ar":"طرف الأنف في الغضب","concept_gloss":"burun ucu ve öfkeli gelişte burnun belirginleşmesi","contextual_glosses":[{"applicability":"Öfke anlamı bulunmadan yalnızca anatomik bölüm adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yalın anatomik gönderimi herhangi bir öfke anlamı eklemeden korur."},"facet_ids":["F001"],"text":"burun ucu","usage_role":"general"},{"applicability":"Kişinin öfkeli gelişini burnunun belirgin görünümüyle anlatan ilk söz kalıbına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geliş eylemini, öfke durumunu ve burnun belirgin görünümünü birlikte korur."},"facet_ids":["F003"],"text":"burnu öne çıkmış biçimde öfkeli gelmek","usage_role":"contextual"},{"applicability":"İlk öfke ifadesine denk gösterilen ikinci söz kalıbını doğal Türkçeyle karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İkinci kalıbın öfkeli geliş ve belirgin burun görünümü yönlerini korur."},"facet_ids":["F004"],"text":"burnu kabarmış halde öfkeli gelmek","usage_role":"contextual"}],"definition":"Burun ucuna ve çıkıntılı burnun baş kısmına verilen adları kapsar. İki özel söz kalıbında ise burnun öne çıkmış ya da kabarmış görünümü, kişinin öfkeli gelişiyle ilişkilendirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalın anatomik kullanım burun ucunu adlandırır."},{"facet_id":"F002","role":"specialization","statement":"Küçültme biçimi, çıkıntılı burnun baş kısmı için kullanılan ayrı bir addır."},{"facet_id":"F003","role":"associated_use","statement":"Bir söz kalıbı, burnu öne çıkmış görünerek öfkeli biçimde gelmeyi anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İkinci söz kalıbı da aynı biçimde öfkeli gelişi anlatan eş yapılı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi yalnızca öfke anındaki burun ucunu değil, burun ucuna verilen adları ve burnun belirginleştiği öfkeli gelişi anlatan iki kalıplaşmış sözü birlikte verir. Bu nedenle dal, anatomik ad ile öfke ifadesini ayıran biçimde yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"burun ucu"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çıkıntılı burnun baş kısmı için kullanılan küçültme biçimi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"burnu öne çıkmış biçimde öfkeli gelmek"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"burnu kabarmış halde öfkeli gelmek"}],"lexicalization_note":"Yalın burun ucu adları ile öfkeli gelişi bildiren iki kalıplaşmış söz ayrı tutulur; öfke anlamı anatomik adın geneline yayılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; genel öfke izi, öfkeden yüzün alevlenmesi, burun organı ve burnun rüzgârı karşılamasıyla sınırı gösteren dört komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirtiyi burun ucuna ve iki geliş kalıbına bağlar; komşu dal ise yüzün genelindeki öfke izini anlatır.","focus_only":"Odak dal burun ucunun adını ve öfkeli gelişte burnun belirgin görünmesini içerir.","gloss":"öfkenin yüzdeki izi","neighbor_only":"Komşu dal öfkenin yüzdeki herhangi bir görünür izini organ ve hareket belirtmeden kapsar.","neighbor_ref":"root_000198/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal öfkenin yüzde dışarıdan görülen bir belirti kazanmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal burun biçimi ve geliş eylemiyle sınırlıdır; komşu dal bütün yüzün ısınma ve alevlenme görünümüne dayanır.","focus_only":"Odak dal burnun öne çıkması veya kabarmasıyla birlikte kişinin gelişini bildirir.","gloss":"yüzün öfkeden alevlenmesi","neighbor_only":"Komşu dal yüzün öfkeden alevlenmesini ve iç sıcaklığın yükselmesini ateş benzetmesiyle anlatır.","neighbor_ref":"root_000225/B004","relation_type":"near_neighbor","shared_zone":"İki dal da öfkeyi yüzde beliren bedensel bir görünüm aracılığıyla ifade eder."},{"boundary_match":"field_only","distinction":"Komşu dal organın genel adıdır; odak dal yalnızca ucuna verilen adları ve belirli öfke kalıplarını içerir.","focus_only":"Odak dal burun ucunu ve burun görünümüyle kurulan iki öfke ifadesini kapsar.","gloss":"burun organı","neighbor_only":"Komşu dal burun organının bütünü, büyüklüğü, kokusu, yaralanması ve işlevleri gibi geniş bir alanı kapsar.","neighbor_ref":"root_000060/B002","relation_type":"same_field","shared_zone":"Her iki dal insan veya hayvan burnuyla ilgili söz varlığı alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal öfke ifadesidir; komşu dal yönelme ve rüzgârı karşılama eylemidir, öfke içermez.","focus_only":"Odak dal öfke sırasında burnun görünümünü ve kişinin gelişini anlatır.","gloss":"rüzgârı burunla karşılamak","neighbor_only":"Komşu dal insanın veya atın burnuyla rüzgâra yönelip onu karşılaması eylemini anlatır.","neighbor_ref":"root_001405/B002","relation_type":"same_field","shared_zone":"İki dalda da burun belirli bir görünüm veya eylemin merkezindedir."}],"source_phrase_ar":"جاء فلان رامعا قبراه ورامعا أنفه إذا جاء مغضبا (tahdhib)؛ جاءنا فخا قبراه (tahdhib)؛ القبراة أيضا طرف الأنف (tahdhib)؛ القبيرة تصغير القبرة وهي رأس القنفاء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Burun ucu ve çıkıntılı burnun baş kısmı için iki ad, burnun belirgin görünümüyle öfkeli gelişi anlatan iki söz kalıbıyla birlikte aktarılır."}],"source_summary":"Bu dalda birden çok kaynağın ortak katmanı yoktur; anatomik adlar ile öfkeli gelişi bildiren iki söz kalıbının tamamı tek kaynaklı bir tanıklıkta toplanır.","sources":["TA"],"what_is_ar":"يدخل فيه القبراة طرف الأنف، والقبيرة رأس القنفاء، وقولهم جاء رامعا قبراه أو فخا قبراه في الغضبان","what_is_not_ar":"ليس القبر مدفن الإنسان ولا القُبَّرة الطائر ولا الغموض العام"},"support_links":[]},{"boundary":"Dal gerçek gömü yerini adlandırmaz; ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölüler hükmünde olma yönlerini mecazi kullanımlarla sınırlar.","branch_kind":"mixed_non_bare","branch_ref":"root_001195/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","surface_ar":"مَقَابِرَ"}],"gloss":"gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gömü alanına varma sözü ölümün dolaylı anlatımı olabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gömülerde olanın çıkarılması, diriliş durumunu veya gizli sırların açığa çıkmasını anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanın dünyadaki durumları, henüz açığa çıkmadıkları için gömülmüşçesine gizli sayılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kâfir ile cahil, dünyadayken gömülmüş diye nitelenir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bazı kişiler ölüler hükmünde anlatılabilir."}}],"root_ar":"ق ب ر","root_id":"root_001195","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ölüm, saklılık, açığa çıkma ve dirilikten yoksun sayılma yönlerini ortak gömülme imgesi altında toplar.","boundary_detail":"Dal gerçek gömü yerini adlandırmaz; ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölüler hükmünde olma yönlerini mecazi kullanımlarla sınırlar.","branch_image_ar":"استعارة القبر للموت والاستتار","concept_gloss":"gömülme üzerinden ölüm, gizlilik ve ölü hükmünde olma","contextual_glosses":[{"applicability":"Gömü alanına varmanın ölümü dolaylı biçimde anlattığı bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dolaylı sözün bağlam içinde ulaştığı ölüm anlamını tam olarak korur."},"facet_ids":["F001"],"text":"ölmek","usage_role":"contextual"},{"applicability":"Gömülü olanın dirilişte ortaya çıkarılması veya sırların açığa dökülmesi bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önce gizli olanın daha sonra ortaya çıkarılması yönünü korur."},"facet_ids":["F002"],"text":"gizli olanların açığa çıkarılması","usage_role":"explanatory"},{"applicability":"Bilgisiz kişinin dünyadayken gizlenmiş ve işlevsiz kalmış sayıldığı mecazi nitelemeye özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgisizliği çevreleyen ve kişiyi etkisiz bırakan bir durum olarak korur."},"facet_ids":["F004"],"text":"bilgisizliğe gömülmüş","usage_role":"contextual"},{"applicability":"Gerçekte canlı olup etkisizlik veya algısızlık bakımından ölü sayılan kişiler için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerçek ölüm ile mecazi olarak ölü sayılma arasındaki hüküm farkını korur."},"facet_ids":["F005"],"text":"ölü hükmünde olanlar","usage_role":"contextual"}],"definition":"Gömü ve gömülme imgesi, ölümün dolaylı anlatımı, gizli durumların gömülmüş sayılması, gömülü olanın dirilişte ya da sırlar açığa çıktığında ortaya çıkarılması, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesi ve bazı kişilerin ölüler hükmünde görülmesi için mecazen kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gömü alanına varma sözü ölümün dolaylı anlatımı olabilir."},{"facet_id":"F002","role":"extension","statement":"Gömülerde olanın çıkarılması, diriliş durumunu veya gizli sırların açığa çıkmasını anlatır."},{"facet_id":"F003","role":"extension","statement":"İnsanın dünyadaki durumları, henüz açığa çıkmadıkları için gömülmüşçesine gizli sayılır."},{"facet_id":"F004","role":"extension","statement":"Kâfir ile cahil, dünyadayken gömülmüş diye nitelenir."},{"facet_id":"F005","role":"extension","statement":"Bazı kişiler ölüler hükmünde anlatılabilir."}],"identity_rationale":"Kaynak ifadesi gömü alanı üzerinden ölümü anlatma, gömülü olanın dirilişte veya sırların açığa çıkışında ortaya çıkarılması, insanın durumlarının gizli sayılması, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesi ve bazı kişilerin ölüler hükmünde görülmesi gibi birkaç mecazi yön verir. Bunlar tek bir 'gizlenme' anlamına indirgenmemeli, gömülme imgesine bağlı ayrı aktarımlar olarak korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ölmek"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gömülerde saklı olanların dirilişte veya sırlar açığa çıkarken ortaya çıkarılması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gömülmüşçesine gizli"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bilgisizliğe gömülmüş"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ölü hükmünde olanlar"}],"lexicalization_note":"Mecazi anlamlar belirli söz kalıpları ve türemiş biçimlere bağlıdır; ölüm veya gizlilik anlamı yalın gömü adı için genel anlam sayılmaz.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; gerçek gömme dalı, gömütün eş adlı karşılığı ve gömütü ev sayan aktarım mecazi sınırı en yararlı biçimde açıkladığı için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal fiziksel yer ve işlemdir; odak dal bu alanı ölüm, saklılık, gömülmüş sayılma ve ölü hükmünde olma gibi mecazi durumlara taşır.","focus_only":"Odak dal ölüm, gizlilik, açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde olma için mecazi aktarımlar içerir.","gloss":"gerçek gömü yeri ve gömme","neighbor_only":"Komşu dal gerçek gömü yerini, ölüyü oraya koymayı ve gömülmesine yer ya da izin sağlamayı anlatır.","neighbor_ref":"root_001195/B001","relation_type":"near_neighbor","shared_zone":"Mecazi kullanımların tümü gerçek gömü ve gömülme tasarımından yararlanır."},{"boundary_match":"field_only","distinction":"Komşu dal doğrudan fiziksel yeri adlandırır; odak dal ise fiziksel adı mecazi bir anlatım aracı olarak kullanır.","focus_only":"Odak dal gömü fikrini ölüm, gizlilik, gömülmüş sayılma ve ölü hükmünde olma gibi mecazi anlatımlarda kullanır.","gloss":"gömütün başka bir adı","neighbor_only":"Komşu dal gerçek gömütün başka bir adını ve o yerin yapılmasını belirtir.","neighbor_ref":"root_000226/B001","relation_type":"same_field","shared_zone":"Her iki dal gömü yeri düşüncesi çevresinde yer alır."},{"boundary_match":"partial","distinction":"Komşu dal gömütü ev olarak kavramlaştırır; odak dal gömülmeyi ölüm, saklılık, gömülmüş sayılma ve ölü hükmünde olma durumlarına genişletir.","focus_only":"Odak dal gizlilik, dirilişte açığa çıkma, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde sayılma yönlerine uzanır.","gloss":"gömütü ölünün evi saymak","neighbor_only":"Komşu dal gömütü ölünün evi veya kaldığı yer olarak yeniden adlandırır.","neighbor_ref":"root_000166/B007","relation_type":"near_neighbor","shared_zone":"İki dal gerçek gömü yerinden hareketle ölüm hakkında aktarmalı bir anlatım kurar."}],"source_phrase_ar":"حتى زرتم المقابر كناية عن الموت (mufradat)؛ إذا بعثر ما في القبور إشارة إلى حال البعث (mufradat)؛ أحوال الإنسان ما دام في الدنيا مستورة كأنها مقبورة (mufradat)؛ الكافر والجاهل ما دام في الدنيا فهو مقبور (mufradat)؛ من في القبور أي الذين هم في حكم الأموات (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Gömülme imgesi ölümün dolaylı anlatımına, gizlinin açığa çıkmasına, insan durumlarının saklılığına, kâfir ile cahilin dünyadayken gömülmüş diye nitelenmesine ve ölüler hükmünde olanlara yapılan ayrı gönderime genişletilir."}],"source_summary":"Bu dalda birden çok kaynağın ortak katmanı yoktur; ölüm, dirilişte açığa çıkma, gizli durumlar, kâfir ile cahilin gömülmüş diye nitelenmesi ve ölü hükmünde sayılma yönleri tek kaynaklı bir açıklamada toplanır.","sources":["MU"],"what_is_ar":"يدخل فيه استعمال المقابر كناية عن الموت، والقبور إشارة إلى كشف المستور، والمقبور استعارة للمستور أو الجاهل أو من في حكم الأموات","what_is_not_ar":"ليس المدفن الحسي نفسه ولا اسم الطائر ولا طرف الأنف"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["102:2:1"],"branch_refs":[],"candidate_id":"cand_bacb9621899767789634","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:2:1:boundary-pivot","source_type":"word_analysis","support_ids":["sup_24f1e95b72863b966ae9","sup_3b40f96e76c38d6a5aba"],"title":"ayah opens as a hinge to one fixed end","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:1","qac_refs":["102:2:1:1"],"status":"accepted"}},{"anchor_refs":["102:2:1"],"branch_refs":[],"candidate_id":"cand_e1614cfa2671179efa97","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:2:1:endpoint-and-result-pressure","source_type":"word_analysis","support_ids":["sup_3b40f96e76c38d6a5aba","sup_4b2e89b242821fce5e59"],"title":"endpoint force also carries result pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:1","qac_refs":["102:2:1:1"],"status":"accepted"}},{"anchor_refs":["102:2:1"],"branch_refs":[],"candidate_id":"cand_d2996e0ed2bb00353744","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:2:1:limit-dependency","source_type":"word_analysis","support_ids":["sup_2af676dfaa226b7cf9b6","sup_3b40f96e76c38d6a5aba"],"title":"limit particle carries the prior clause forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:1","qac_refs":["102:2:1:1"],"status":"accepted"}},{"anchor_refs":["102:2:1"],"branch_refs":[],"candidate_id":"cand_6317549247860e138b44","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"102:2:1:sound-of-limit","source_type":"word_analysis","support_ids":["sup_028ababeb39b6a6d1b92","sup_3b40f96e76c38d6a5aba"],"title":"recited texture presses the boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:1","qac_refs":["102:2:1:1"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_ad0ba757a93b8422a352","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:cadence-clipped-verb","source_type":"word_analysis","support_ids":["sup_3ecf471730dd789ff289","sup_45c8d8523249d481112d"],"title":"short verb hands attention to the grave noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_b5c49fe1d6215c5cd2dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:compressed-route","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_b7434e553162156fb2db"],"title":"rivalry narrows into one spare action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_ab1f5f08c7ea34a9d7c1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:form-i-rarity-and-direction","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_f5a50ec9d069bd8d46ab"],"title":"plain Form I visit stands out against other root-family forms","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_e03dcc573d9755907585","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:forward-knowing-threshold","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_5536259dcf0c797c1015"],"title":"completed visit opens into future knowing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_a09d639418bfba5d7022","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:perfect-certainty","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_ce42b958e08b84777d4b"],"title":"perfect tense makes the endpoint accomplished","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_4c7286716a8ba61ef692","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:pronoun-continuity-role-shift","source_type":"word_analysis","support_ids":["sup_001c69495f48f0dd19c3","sup_45c8d8523249d481112d"],"title":"same addressees become the arriving subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_7b2707295339ebe49338","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:rare-finite-against-abstract-field","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_8725ea6b6731076bcbb6"],"title":"finite act emerges from an abstract root field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_f03c44dd3a83f22189fd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:root-turning-falsehood-pressure","source_type":"word_analysis","support_ids":["sup_11257f6397e851863628","sup_45c8d8523249d481112d"],"title":"turning and falsehood pressure shadows the visit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_d9314a68cd2acc15b62a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:subordinate-endpoint-verb","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_7391c44961f399b70eb0"],"title":"verb completes the cross-ayah dependency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_739bf28fd7cdda78c87f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:visit-death-euphemism","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_6a3c861bb5416c79c02b"],"title":"grave object keeps visit and death together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_f942dc9432133a199699","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:architecture-destination-dominates","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_6913eedf7ebe686da78d"],"title":"bare verb-object clause ends in destination","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_2d7e6c6329a1faf95de6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:burial-concealment-reversal","source_type":"word_analysis","support_ids":["sup_1b13a7a5451d32ff036f","sup_2d91f66ffc66b99a5011"],"title":"burial place hides public display","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_7fb8b43f82110f526319","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:death-disclosure-horizon","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_9c36e4f4fd6b6c859ab5"],"title":"concealed graves point toward disclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_634160b7a7f5c0681d73","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:definite-collective-destination","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_d12ddd9591fcdf12457a"],"title":"definite plural makes the graveyard shared","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_930fd948283d8fcd8ed6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:direct-object-endpoint","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_ae2b6845f25ceb4ff0d3"],"title":"accusative object is the thing reached","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_20fd1aee3083e2bd1981","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:grave-form-echo","source_type":"word_analysis","support_ids":["sup_04765a756c6fb8435ba8","sup_2d91f66ffc66b99a5011"],"title":"related grave forms shift from container to place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_60bd2c15682fff17b455","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:literal-euphemistic-threshold","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_cfcfceb919185e3c98a6"],"title":"graveyard remains both endpoint and visit-place","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_764998c6f699dcab8d6c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:place-noun-institution","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_4c06f3c96e5d1606fb1e"],"title":"place noun names a cemetery-domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_f0bf430675fe335468ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:rare-closing-root","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_aa11579e49b0e630291b"],"title":"uncommon root carries the closing burden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_a5fd67574a1bfa4058de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:scene-shift","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_3cfe588469418a22f36e"],"title":"social arena collapses into cemetery","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_79e78a9c7bfab080a476","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:sound-weight","source_type":"word_analysis","support_ids":["sup_2d91f66ffc66b99a5011","sup_37ee4d835026768501c6"],"title":"grave noun sounds heavier than the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:3","qac_refs":["102:2:3:1","102:2:3:2"],"status":"accepted"}},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_81a656310ff152a0d9b4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:1","source_type":"qac_morpheme","support_ids":["sup_677c5fb5a122def9bd55"],"title":"QAC root occurrence: ز و ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:2:3"],"branch_refs":[],"candidate_id":"cand_1d9b5a36c97cc2de12c4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001195"],"scope":"focus_ayah","source_local_id":"102:2:3:2","source_type":"qac_morpheme","support_ids":["sup_7b87dd1b02c40f88bc89"],"title":"QAC root occurrence: ق ب ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["102:2:2"],"branch_refs":[],"candidate_id":"cand_243ec0b80d0e53c50fad","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000654"],"scope":"focus_ayah","source_local_id":"102:2:2:overbroad-burden-partner","source_type":"word_analysis","support_ids":["sup_45c8d8523249d481112d","sup_d431a4a12408da208330"],"title":"burden and laterness are not locally activated partners","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"102:2:2","qac_refs":["102:2:2:1","102:2:2:2"],"status":"accepted"}},{"anchor_refs":["102:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:2","branch_refs":["root_000654/B003","root_001195/B001"],"candidate_id":"cand_606b2c685d8bd0489f94","commentary_obligation":"review","hft_ref":"hft_ee8ea238611a69abfcc0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_temporary_grave_visit","source_type":"hft","support_ids":["sup_967469edc9c7278cc1ee"],"title":"baseline_temporary_grave_visit","trust":"legacy_unbound"},{"anchor_refs":["102:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:2","branch_refs":["root_000654/B001","root_000654/B003","root_001195/B002"],"candidate_id":"cand_87cb3e8a864dcce27623","commentary_obligation":"review","hft_ref":"hft_a77bc0d072fb7f4d8669","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_bent_descent_into_hiddenness","source_type":"hft","support_ids":["sup_7e3e381c016bca983319"],"title":"baseline_bent_descent_into_hiddenness","trust":"legacy_unbound"},{"anchor_refs":["102:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"102:2","branch_refs":["root_000654/B005","root_001195/B001"],"candidate_id":"cand_f7db2d1097b9125b14d0","commentary_obligation":"review","hft_ref":"hft_0d452d6a34453d2092e9","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_buried_recourse","source_type":"hft","support_ids":["sup_3140071eceb5acbeecd7"],"title":"baseline_buried_recourse","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","qac_morphemes":[{"lemma_ar":"حَتَّىٰ","morph_features":"STEM|POS:INC|LEM:Hat~aY`","morpheme_role":"STEM","pos":"INC","qac_ref":"102:2:1:1","qac_word_ref":"102:2:1","root_ar":"","surface_ar":"حَتَّىٰ"},{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","root_ar":"ز و ر","surface_ar":"زُرْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:2:2:2","qac_word_ref":"102:2:2","root_ar":"","surface_ar":"تُمُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:2:3:1","qac_word_ref":"102:2:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","root_ar":"ق ب ر","surface_ar":"مَقَابِرَ"}],"word_analysis_qac_refs":[["102:2:1:1"],["102:2:2:1","102:2:2:2"],["102:2:3:1","102:2:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["102:2:1","102:2:2","102:2:3"]},"focus_surface_evidence":{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","qac_morphemes":[{"lemma_ar":"حَتَّىٰ","morph_features":"STEM|POS:INC|LEM:Hat~aY`","morpheme_role":"STEM","pos":"INC","qac_ref":"102:2:1:1","qac_word_ref":"102:2:1","root_ar":"","surface_ar":"حَتَّىٰ"},{"lemma_ar":"زُرْ","morph_features":"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"102:2:2:1","qac_word_ref":"102:2:2","root_ar":"ز و ر","surface_ar":"زُرْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"102:2:2:2","qac_word_ref":"102:2:2","root_ar":"","surface_ar":"تُمُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"102:2:3:1","qac_word_ref":"102:2:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَقَابِر","morph_features":"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"102:2:3:2","qac_word_ref":"102:2:3","root_ar":"ق ب ر","surface_ar":"مَقَابِرَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["102:2:1:1"],["102:2:2:1","102:2:2:2"],["102:2:3:1","102:2:3:2"]],"word_analysis_refs":["102:2:1","102:2:2","102:2:3"],"word_rows":[{"analysis_record_ref":"102:2:1","analytic_gloss_range_en":"temporal limit particle marking the endpoint of the previous diversion, with a consequential/result nuance surviving as a qualified pressure","analytic_root_gloss_range_en":null,"qac_refs":["102:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"حَتَّىٰ","transliteration":"ḥattā"}},{"analysis_record_ref":"102:2:2","analytic_gloss_range_en":"Form I perfect second-person plural visiting/arrival directed to the graves; locally euphemistic for death while preserving the visitor wording and certainty of completed arrival","analytic_root_gloss_range_en":"root range includes visiting and turning toward, turning aside or deviation, falsehood by deviation from truth, and other remote branches; the local Form I verb selects visiting/arrival while deviation and falsehood remain only controlled pressure","qac_refs":["102:2:2:1","102:2:2:2"],"root":{"arabic":"ز و ر","transliteration":"z-w-r"},"surface":{"arabic":"زُرْتُمُ","transliteration":"zurtumu"}},{"analysis_record_ref":"102:2:3","analytic_gloss_range_en":"definite plural place noun naming the graveyard or cemetery-domain as the direct object and endpoint of the visit, with literal graveyard and euphemistic death readings held together","analytic_root_gloss_range_en":"root range centers on grave, burial, placing the dead in a grave, and concealment or inward hiddenness; local wording selects the cemetery/place-domain, not unrelated branches such as bird or anger idioms","qac_refs":["102:2:3:1","102:2:3:2"],"root":{"arabic":"ق ب ر","transliteration":"q-b-r"},"surface":{"arabic":"ٱلْمَقَابِرَ","transliteration":"al-maqābira"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["102:2"],"branch_refs":["root_000654/B003","root_001195/B001"],"candidate_id":"cand_606b2c685d8bd0489f94","evidence_scope":"focus_ayah","hft_ref":"hft_ee8ea238611a69abfcc0","item_id":"baseline_temporary_grave_visit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_temporary_grave_visit","support_id":"sup_967469edc9c7278cc1ee"},{"anchor_refs":["102:2"],"branch_refs":["root_000654/B001","root_000654/B003","root_001195/B002"],"candidate_id":"cand_87cb3e8a864dcce27623","evidence_scope":"focus_ayah","hft_ref":"hft_a77bc0d072fb7f4d8669","item_id":"baseline_bent_descent_into_hiddenness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_bent_descent_into_hiddenness","support_id":"sup_7e3e381c016bca983319"},{"anchor_refs":["102:2"],"branch_refs":["root_000654/B005","root_001195/B001"],"candidate_id":"cand_f7db2d1097b9125b14d0","evidence_scope":"focus_ayah","hft_ref":"hft_0d452d6a34453d2092e9","item_id":"baseline_buried_recourse","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_buried_recourse","support_id":"sup_3140071eceb5acbeecd7"}],"diagnostics":[],"lane_counts":{"global":9,"macro":7,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"102:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"102:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"102:2","lane":"micro","linguistic_source_ref":"102:2","surface_ref":"102:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"102:2","target_tokens":[["Mezarları",["102:2:3"]],["ziyaret",["102:2:2"]],["edinceye",["102:2:1","102:2:2"]],["kadar",["102:2:1"]]],"text":"Mezarları ziyaret edinceye kadar."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s102-p01-001-008","label":"Whole surah","number":1,"refs":["102:1","102:2","102:3","102:4","102:5","102:6","102:7","102:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:pronoun-continuity-role-shift","source_type":"word_analysis","support_id":"sup_001c69495f48f0dd19c3","text":"{\"blocking_evidence\":null,\"headline\":\"same addressees become the arriving subject\",\"reader_payoff\":\"The reader notices that the same second-person plural audience crosses the ayah boundary, moving from being distracted to performing the graveward arrival.\",\"reason\":\"The verb has a syntactically forced 2mp implicit subject, and the CRITICAL boundary rows tie that subject to the prior second-person audience.\",\"representative_source_ids\":[\"QG-abc616d6\",\"QS-30ec8018\",\"QF-1733ba32\",\"QB-15b2e681\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:1:sound-of-limit","source_type":"word_analysis","support_id":"sup_028ababeb39b6a6d1b92","text":"{\"blocking_evidence\":null,\"headline\":\"recited texture presses the boundary\",\"reader_payoff\":\"The reader hears the small particle as a hard, lingering boundary marker rather than a weightless connective.\",\"reason\":\"The written and recited form includes a doubled consonantal pressure and final long vowel, matching the CRITICAL sound rows without adding an independent lexical meaning.\",\"representative_source_ids\":[\"QF-60921eac\",\"QP-3af1ba11\",\"QP-7244bca7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:grave-form-echo","source_type":"word_analysis","support_id":"sup_04765a756c6fb8435ba8","text":"{\"blocking_evidence\":null,\"headline\":\"related grave forms shift from container to place\",\"reader_payoff\":\"The reader notices the visible root-family shift from individual grave language to the collective place form selected here.\",\"reason\":\"The CRITICAL echo remains valid as a form contrast: the local word is the place-noun plural, not the simpler individual grave noun.\",\"representative_source_ids\":[\"QE-abac71a8\",\"QI-2f0270a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:root-turning-falsehood-pressure","source_type":"word_analysis","support_id":"sup_11257f6397e851863628","text":"{\"blocking_evidence\":null,\"headline\":\"turning and falsehood pressure shadows the visit\",\"reader_payoff\":\"The reader notices that the local visit toward the graves also exposes the previous life-route as misdirected, while visiting remains the selected sense.\",\"reason\":\"V4 accepts branches for turning aside/deviation, falsehood, and visiting, but the local Form I verb with a grave object selects visiting; the other branches survive only as controlled image-pressure.\",\"representative_source_ids\":[\"QS-8cdcaa06\",\"QS-b020a310\",\"QE-8ffe1653\",\"QY-3a219cd4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:burial-concealment-reversal","source_type":"word_analysis","support_id":"sup_1b13a7a5451d32ff036f","text":"{\"blocking_evidence\":null,\"headline\":\"burial place hides public display\",\"reader_payoff\":\"The reader notices the reversal from public accumulation to the burial domain where bodies and status disappear from view.\",\"reason\":\"V4 supports grave, burial, and hiddenness branches for {{ar:ق ب ر}} ({{tr:q-b-r}}), while local grammar selects the cemetery place noun; concealment therefore survives as root image rather than a separate local act.\",\"representative_source_ids\":[\"QS-1c9edcbf\",\"QS-951daed3\",\"QB-f19e01a1\",\"QY-84277b0b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:1:boundary-pivot","source_type":"word_analysis","support_id":"sup_24f1e95b72863b966ae9","text":"{\"blocking_evidence\":null,\"headline\":\"ayah opens as a hinge to one fixed end\",\"reader_payoff\":\"The reader notices that the first word after the ayah break turns open-ended rivalry into a path with a named terminal destination.\",\"reason\":\"The particle begins the ayah and governs the following grave-clause, so its boundary position is a structural hinge between the previous diversion and the present endpoint.\",\"representative_source_ids\":[\"QT-7ddcc3c9\",\"QT-9d9940f8\",\"QY-10b5d01f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:1:limit-dependency","source_type":"word_analysis","support_id":"sup_2af676dfaa226b7cf9b6","text":"{\"blocking_evidence\":null,\"headline\":\"limit particle carries the prior clause forward\",\"reader_payoff\":\"The reader notices that the ayah begins inside the grammar of 102:1, so grave-visiting is the limit of the prior diversion rather than a detached new scene.\",\"reason\":\"QAC and attachment evidence identify {{ar:حَتَّىٰ}} ({{tr:ḥattā}}) as introducing a temporal limit clause whose complement is the verbal span {{ar:زُرْتُمُ ٱلْمَقَابِرَ}} ({{tr:zurtumu l-maqābira}}).\",\"representative_source_ids\":[\"QG-7e78da11\",\"QG-d2a1c530\",\"QT-cd7bdc12\",\"QB-6fc2d6e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3","source_type":"word_analysis","support_id":"sup_2d91f66ffc66b99a5011","text":"{\"gloss_range\":\"definite plural place noun naming the graveyard or cemetery-domain as the direct object and endpoint of the visit, with literal graveyard and euphemistic death readings held together\",\"prose\":\"{{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) is not a loose background setting; it is the accusative direct object of {{ar:زُرْتُمُ}} ({{tr:zurtumu}}), so the clause lands on the graveyard as the thing reached. Its definite plural form makes the destination feel shared and already known, while the place-noun pattern names a cemetery-domain rather than one individual grave container. That form matters after {{ar:ٱلتَّكَاثُرُ}} ({{tr:al-takāthuru}}): a public multiplication is answered by a collective place where bodies are buried and hidden. The object relation keeps literal grave-visiting and euphemistic death open together, and the visitor verb keeps the graveyard from being simple final silence. Later grave-disclosure scenes (82:4; 100:9) show the same root horizon moving from concealment toward exposure, and the next ayah's rebuke (102:3) likewise reopens what this final noun seems to close. As the last word, longer and heavier than the verb, {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) absorbs the action into the destination.\",\"root_display\":\"{{ar:ق ب ر}} ({{tr:q-b-r}})\",\"root_gloss_range\":\"root range centers on grave, burial, placing the dead in a grave, and concealment or inward hiddenness; local wording selects the cemetery/place-domain, not unrelated branches such as bird or anger idioms\",\"surface_display\":\"{{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:sound-weight","source_type":"word_analysis","support_id":"sup_37ee4d835026768501c6","text":"{\"blocking_evidence\":null,\"headline\":\"grave noun sounds heavier than the verb\",\"reader_payoff\":\"The reader hears the final object as a longer, weightier landing after the clipped verb.\",\"reason\":\"The sound rows describe the local recited surface, including the article boundary and the heavier consonantal texture of the final noun.\",\"representative_source_ids\":[\"QP-4f4ffe75\",\"QP-c54052e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:1","source_type":"word_analysis","support_id":"sup_3b40f96e76c38d6a5aba","text":"{\"gloss_range\":\"temporal limit particle marking the endpoint of the previous diversion, with a consequential/result nuance surviving as a qualified pressure\",\"prose\":\"{{ar:حَتَّىٰ}} ({{tr:ḥattā}}) keeps 102:2 from sounding like a fresh, independent report. It opens with dependency, carrying the previous verb {{ar:أَلْهَاكُمُ}} ({{tr:alhākumu}}) into the current ayah and making {{ar:زُرْتُمُ ٱلْمَقَابِرَ}} ({{tr:zurtumu l-maqābira}}) the endpoint of that diversion. The strongest local grammar is temporal limit: the competitive absorption lasts until the grave-arrival. The result nuance also survives, but only as qualified pressure, because the same wording can make the diversion feel as though it issues in that arrival rather than merely continuing up to it. Placed first after the ayah break, the particle turns the break into continuation, and its doubled stop plus final long sound make the small boundary word feel audibly weighty before the verb names the arrival.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:حَتَّىٰ}} ({{tr:ḥattā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:scene-shift","source_type":"word_analysis","support_id":"sup_3cfe588469418a22f36e","text":"{\"blocking_evidence\":null,\"headline\":\"social arena collapses into cemetery\",\"reader_payoff\":\"The reader notices the concrete spatial shift from public competition to the burial ground.\",\"reason\":\"The boundary row coherently links the previous social rivalry to the final cemetery object without changing the local noun sense.\",\"representative_source_ids\":[\"QB-bcf4246c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:cadence-clipped-verb","source_type":"word_analysis","support_id":"sup_3ecf471730dd789ff289","text":"{\"blocking_evidence\":null,\"headline\":\"short verb hands attention to the grave noun\",\"reader_payoff\":\"The reader hears the verb as a compact beat that quickly yields to the heavier graveyard object.\",\"reason\":\"The sound rows describe a local cadence effect between the short verb and the longer object; this is compatible with the surface sequence and does not create a new lexical sense.\",\"representative_source_ids\":[\"QP-a8b2bad3\",\"QP-cabd43c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2","source_type":"word_analysis","support_id":"sup_45c8d8523249d481112d","text":"{\"gloss_range\":\"Form I perfect second-person plural visiting/arrival directed to the graves; locally euphemistic for death while preserving the visitor wording and certainty of completed arrival\",\"prose\":\"{{ar:زُرْتُمُ}} ({{tr:zurtumu}}) is a perfect verb inside the scope of {{ar:حَتَّىٰ}} ({{tr:ḥattā}}), so the graveward action is subordinated to the distraction named in 102:1. Its past form makes the endpoint sound already accomplished, collapsing the distance between present rivalry and future death. The attached second-person plural ending keeps the same accused audience in view: the ones affected by distraction become the ones who arrive. Because the object is {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}), the ordinary visit sense is selected, yet the pairing with graves lets the wording remain euphemistic, so death is spoken as a visit and not as a blunt death verb. The spare verb-object beat reduces the wide motion of {{ar:ٱلتَّكَاثُرُ}} ({{tr:al-takāthuru}}) to one action and one destination, with no intervening clause for delay. The broader {{ar:ز و ر}} ({{tr:z-w-r}}) field can involve turning aside and falsehood; here those branches do not replace visiting, but they make the visit expose the prior life of {{ar:ٱلتَّكَاثُرُ}} ({{tr:al-takāthuru}}) as a misdirected route. The Form I simplicity also matters: against swerving language elsewhere (18:17), this word moves directly toward the graveyard, and the next ayah's rebuke and future knowing (102:3) keep the completed arrival from becoming silence.\",\"root_display\":\"{{ar:ز و ر}} ({{tr:z-w-r}})\",\"root_gloss_range\":\"root range includes visiting and turning toward, turning aside or deviation, falsehood by deviation from truth, and other remote branches; the local Form I verb selects visiting/arrival while deviation and falsehood remain only controlled pressure\",\"surface_display\":\"{{ar:زُرْتُمُ}} ({{tr:zurtumu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:1:endpoint-and-result-pressure","source_type":"word_analysis","support_id":"sup_4b2e89b242821fce5e59","text":"{\"blocking_evidence\":null,\"headline\":\"endpoint force also carries result pressure\",\"reader_payoff\":\"The reader notices both duration and consequence: the distraction runs up to the graves and is made to feel as though it drives toward them.\",\"reason\":\"The local attachment strongly licenses the temporal-limit reading, while the CRITICAL particle rows preserve a consequential nuance as rhetorical pressure without replacing the grammatical endpoint function.\",\"representative_source_ids\":[\"QG-a16260ac\",\"QS-12b0b7d6\",\"MG-a54305e5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:place-noun-institution","source_type":"word_analysis","support_id":"sup_4c06f3c96e5d1606fb1e","text":"{\"blocking_evidence\":null,\"headline\":\"place noun names a cemetery-domain\",\"reader_payoff\":\"The reader notices that the ayah chooses the cemetery as an institutional place of burial, not merely a count of individual graves.\",\"reason\":\"QAC identifies {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) as a place/time noun plural, supporting the CRITICAL distinction between cemetery-domain and individual grave containers.\",\"representative_source_ids\":[\"QS-c40640f9\",\"QF-5bf9f604\",\"QF-bd423ac3\",\"MF-8ec46842\",\"QI-2f0270a4\",\"QH-ce448d72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:forward-knowing-threshold","source_type":"word_analysis","support_id":"sup_5536259dcf0c797c1015","text":"{\"blocking_evidence\":null,\"headline\":\"completed visit opens into future knowing\",\"reader_payoff\":\"The reader notices that the grave-arrival is not the end of discourse; the next ayah turns it into the threshold for rebuke and future knowing (102:3).\",\"reason\":\"The CRITICAL rows provide the concrete forward reference to 102:3, and nothing in the local grammar blocks reading the completed visit as a threshold for the next ayah.\",\"representative_source_ids\":[\"QE-ea3cc88c\",\"QB-787105ea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"102:2:2:1","source_type":"qac_morpheme","support_id":"sup_677c5fb5a122def9bd55","text":"{\"lemma_ar\":\"زُرْ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:zuro|ROOT:zwr|2MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"102:2:2:1\",\"qac_word_ref\":\"102:2:2\",\"root_ar\":\"ز و ر\",\"surface_ar\":\"زُرْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:architecture-destination-dominates","source_type":"word_analysis","support_id":"sup_6913eedf7ebe686da78d","text":"{\"blocking_evidence\":null,\"headline\":\"bare verb-object clause ends in destination\",\"reader_payoff\":\"The reader notices that the clause offers no modifier after the graveyard noun, so the destination itself becomes the structural close.\",\"reason\":\"The local clause is a compact limit clause with verb plus explicit direct object and no post-object elaboration.\",\"representative_source_ids\":[\"QT-c69cabc1\",\"QY-9df93f44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:visit-death-euphemism","source_type":"word_analysis","support_id":"sup_6a3c861bb5416c79c02b","text":"{\"blocking_evidence\":null,\"headline\":\"grave object keeps visit and death together\",\"reader_payoff\":\"The reader notices that death is voiced through the softer grammar of visiting, preserving both actual grave-going and euphemistic arrival at death.\",\"reason\":\"The direct object {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) selects the visiting-to-graves frame while allowing the euphemistic death reading pressed by the CRITICAL rows.\",\"representative_source_ids\":[\"QS-50a71bf4\",\"QS-7f277c44\",\"MF-b4e0ab71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:subordinate-endpoint-verb","source_type":"word_analysis","support_id":"sup_7391c44961f399b70eb0","text":"{\"blocking_evidence\":null,\"headline\":\"verb completes the cross-ayah dependency\",\"reader_payoff\":\"The reader notices that the verb is not free-standing; it is the action that completes the limit clause begun by {{ar:حَتَّىٰ}} ({{tr:ḥattā}}).\",\"reason\":\"Attachment evidence identifies {{ar:زُرْتُمُ ٱلْمَقَابِرَ}} ({{tr:zurtumu l-maqābira}}) as the verbal span governed by the limit particle.\",\"representative_source_ids\":[\"QG-354065ff\",\"QT-193068c0\",\"QT-4b2c8d8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"102:2:3:2","source_type":"qac_morpheme","support_id":"sup_7b87dd1b02c40f88bc89","text":"{\"lemma_ar\":\"مَقَابِر\",\"morph_features\":\"STEM|POS:N|LEM:maqaAbir|ROOT:qbr|MP|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"102:2:3:2\",\"qac_word_ref\":\"102:2:3\",\"root_ar\":\"ق ب ر\",\"surface_ar\":\"مَقَابِرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:rare-finite-against-abstract-field","source_type":"word_analysis","support_id":"sup_8725ea6b6731076bcbb6","text":"{\"blocking_evidence\":null,\"headline\":\"finite act emerges from an abstract root field\",\"reader_payoff\":\"The reader notices the finite graveward action standing out against a root field that elsewhere includes abstract falsehood and deviation language.\",\"reason\":\"The CRITICAL distributional rows are coherent when kept as contrast: the local word is a finite visiting act, not an abstract noun or a derived swerving form.\",\"representative_source_ids\":[\"QH-2df9b0bb\",\"QI-d8427bec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:death-disclosure-horizon","source_type":"word_analysis","support_id":"sup_9c36e4f4fd6b6c859ab5","text":"{\"blocking_evidence\":null,\"headline\":\"concealed graves point toward disclosure\",\"reader_payoff\":\"The reader notices that the graveyard's concealment is not the final horizon, because related scenes move toward grave-opening and exposure (82:4; 100:9).\",\"reason\":\"The CRITICAL rows supply concrete references to grave-disclosure contexts (82:4; 100:9), and the local noun's burial/concealment sense makes the contrast meaningful.\",\"representative_source_ids\":[\"QI-4336c88f\",\"QE-d153a0ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:rare-closing-root","source_type":"word_analysis","support_id":"sup_aa11579e49b0e630291b","text":"{\"blocking_evidence\":null,\"headline\":\"uncommon root carries the closing burden\",\"reader_payoff\":\"The reader notices that an uncommon grave-root form is placed at the ayah's end, making it carry the weight of the surah's opening trajectory.\",\"reason\":\"The contextual profile marks the exact root/form as low occurrence, and the word's final position makes that rarity locally salient.\",\"representative_source_ids\":[\"QI-d97299c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:direct-object-endpoint","source_type":"word_analysis","support_id":"sup_ae2b6845f25ceb4ff0d3","text":"{\"blocking_evidence\":null,\"headline\":\"accusative object is the thing reached\",\"reader_payoff\":\"The reader notices that the graves are not scenery around the action; they are the direct endpoint into which the action is pulled.\",\"reason\":\"Attachment evidence marks {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) as the explicit direct object of {{ar:زُرْتُمُ}} ({{tr:zurtumu}}).\",\"representative_source_ids\":[\"QG-95cebcff\",\"QT-25f00eac\",\"QT-eadb8a0b\",\"QY-9df93f44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:compressed-route","source_type":"word_analysis","support_id":"sup_b7434e553162156fb2db","text":"{\"blocking_evidence\":null,\"headline\":\"rivalry narrows into one spare action\",\"reader_payoff\":\"The reader notices the movement from expansive social rivalry to a stripped-down verb-object clause with no room for delay.\",\"reason\":\"The clause has a compact verb-object architecture, and the boundary rows connect it to the prior {{ar:ٱلتَّكَاثُرُ}} ({{tr:al-takāthuru}}).\",\"representative_source_ids\":[\"QB-418b3d05\",\"QT-4b2c8d8d\",\"QY-3a219cd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:perfect-certainty","source_type":"word_analysis","support_id":"sup_ce42b958e08b84777d4b","text":"{\"blocking_evidence\":null,\"headline\":\"perfect tense makes the endpoint accomplished\",\"reader_payoff\":\"The reader notices that the future grave-arrival is worded as already completed, making death feel grammatically certain rather than merely predicted.\",\"reason\":\"QAC marks {{ar:زُرْتُمُ}} ({{tr:zurtumu}}) as a Form I perfect verb and explicitly allows prophetic-perfect force or literal past narration.\",\"representative_source_ids\":[\"QG-16498a29\",\"QB-c874d87e\",\"QY-44bf98fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:literal-euphemistic-threshold","source_type":"word_analysis","support_id":"sup_cfcfceb919185e3c98a6","text":"{\"blocking_evidence\":null,\"headline\":\"graveyard remains both endpoint and visit-place\",\"reader_payoff\":\"The reader notices that the direct object stabilizes the graveyard phrase while leaving literal grave-visiting and death-euphemism active together.\",\"reason\":\"The syntax fixes the object relation, but the visit verb plus grave object allows both literal graveyard-going and euphemistic death without changing the noun's concrete sense.\",\"representative_source_ids\":[\"QG-80b996a2\",\"QS-403adff5\",\"QB-caaf7b96\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:3:definite-collective-destination","source_type":"word_analysis","support_id":"sup_d12ddd9591fcdf12457a","text":"{\"blocking_evidence\":null,\"headline\":\"definite plural makes the graveyard shared\",\"reader_payoff\":\"The reader notices that the clause ends at the recognizable graves, not at an unspecified burial place.\",\"reason\":\"QAC marks the noun as definite and plural, and the CRITICAL rows correctly treat definiteness as part of the final destination's force.\",\"representative_source_ids\":[\"QG-39260377\",\"QF-76b42de5\",\"QF-b1ef554d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:overbroad-burden-partner","source_type":"word_analysis","support_id":"sup_d431a4a12408da208330","text":"{\"blocking_evidence\":\"The local frame has {{ar:ٱلْمَقَابِرَ}} ({{tr:al-maqābira}}) as the direct object, and V4 branch evidence for {{ar:ز و ر}} ({{tr:z-w-r}}) does not license a burden sense or a free partner-field activation here.\",\"headline\":\"burden and laterness are not locally activated partners\",\"reader_payoff\":null,\"reason\":\"The row imports distributional neighbors without a local co-occurrence or construction; the grave object licenses visiting, not a burden/laterness collocation.\",\"representative_source_ids\":[\"QI-e2a3b6d9\"],\"status\":\"rejected\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"102:2:2:form-i-rarity-and-direction","source_type":"word_analysis","support_id":"sup_f5a50ec9d069bd8d46ab","text":"{\"blocking_evidence\":null,\"headline\":\"plain Form I visit stands out against other root-family forms\",\"reader_payoff\":\"The reader notices that a simple finite visiting form is reserved here for the graves, so ordinary visiting becomes extraordinary by its destination.\",\"reason\":\"The local word is Form I perfect; broader root-family distribution and the swerving contrast (18:17) are useful contrasts, but they do not change the local visit sense.\",\"representative_source_ids\":[\"QF-f3badefc\",\"QF-f7f94a07\",\"QI-d8427bec\",\"QI-edc01d80\",\"QH-fb18a3a9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","ayah_ref":"102:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000654/B003","root_001195/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000654","role":"Visiting and turning toward someone supplies a purposeful arrival whose visitor relation remains temporary.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001195","role":"Burial and the place of graves fix the destination as actual mortuary space rather than an abstract limit.","root":"ق ب ر","source_ref":"102:2","source_word_indices":["3"]}],"changed_reading":{"after":"You crossed the limit into burial, yet the verb casts even that arrival as a visit: the grave is a reached station whose permanence the wording pointedly withholds.","before":"You continued until you reached the graves and died."},"confidence":"strong","focus_anchor":"The limit particle حَتَّى, the perfect second-person plural زُرْتُم, and the plural destination ٱلْمَقَابِرَ.","mechanism":"Ordinary visitation supplies arrival without lexical ownership of the destination, while the burial-place branch identifies that destination as the resting place of the dead. The limit construction therefore reaches death while retaining a live asymmetry: those buried are described as visitors, so the grave is a terminal boundary in the sentence but not securely a permanent home in the visitor image.","model_id":"baseline_temporary_grave_visit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_temporary_grave_visit","source_type":"hft","support_id":"sup_967469edc9c7278cc1ee","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","ayah_ref":"102:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000654/B001","root_000654/B003","root_001195/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000654","role":"The ordinary visit keeps the model attached to the clause's actual directed motion.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000654","role":"Turning aside and deviation bend the visitor's route away from an intended course.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001195","role":"Hiddenness, inward sinking, and sealed enclosure give the route a downward and occluding terminus.","root":"ق ب ر","source_ref":"102:2","source_word_indices":["3"]}],"changed_reading":{"after":"The verse images a trajectory permitted to bend all the way into hidden, sunken enclosure: the cemetery is the geometry of a completed diversion.","before":"The verse reports a neutral visit to a cemetery."},"confidence":"medium","focus_anchor":"The motion in زُرْتُم directed toward the plural ٱلْمَقَابِرَ can activate side branches of both focus roots.","mechanism":"The visit remains the overt event, but the same motion root also carries turning aside, and the grave root carries hiddenness, depression, and enclosure. Together they spatialize the clause as a course that bends away and sinks inward; حَتَّى measures not merely elapsed time but the full extent of that diversion.","model_id":"baseline_bent_descent_into_hiddenness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_bent_descent_into_hiddenness","source_type":"hft","support_id":"sup_7e3e381c016bca983319","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ","ayah_ref":"102:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000654/B005","root_001195/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000654","role":"A point of recourse or leadership supplies the social topology of a group inclining toward an authority.","root":"ز و ر","source_ref":"102:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001195","role":"The burial-place image locates that possible recourse among the dead.","root":"ق ب ر","source_ref":"102:2","source_word_indices":["3"]}],"changed_reading":{"after":"The living may also be turning toward the buried as collective reference points; the graveyard becomes a social archive of authority as well as a destination.","before":"A group physically arrives at burial grounds."},"confidence":"exploratory","focus_anchor":"The collective subject turns toward plural graves through a verb whose root also contains a social point-of-recourse branch.","mechanism":"Alongside physical visitation, the root can organize people around a chief or reference point toward which they incline. Coupled with burial places, this leaves a social reading in which the living turn toward the buried dead not only as destinations but as sources of standing, precedent, or orientation.","model_id":"baseline_buried_recourse"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_buried_recourse","source_type":"hft","support_id":"sup_3140071eceb5acbeecd7","trust":"legacy_unbound"}]}
</lane_packet_json>
