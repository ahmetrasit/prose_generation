# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **94:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s094-regular-20260912/s094/94_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "94:1",
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
{"branch_registry":[{"boundary":"Bu dal etkin biçimde anlamı açıklamayı kapsar; yalnızca anlamayı, eti parçalamayı ya da içsel ferahlamayı kapsamaz.","branch_kind":"bare","branch_ref":"root_000784/B001","candidate_links":[{"candidate_id":"cand_857f6a79f82947db1dc6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"gizli anlamı açıklayıp anlaşılır kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirsiz ya da gizli anlamı açıklayıp görünür ve anlaşılır kılar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güç bir söz veya meseleyi ayrıntılandırarak yorumlar ve kapalılığını giderir."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Söz, iş ve güç meselelerdeki etkin açıklama ve anlamı açığa çıkarma çekirdeğinin tamamını karşılar.","boundary_detail":"Bu dal etkin biçimde anlamı açıklamayı kapsar; yalnızca anlamayı, eti parçalamayı ya da içsel ferahlamayı kapsamaz.","branch_image_ar":"فتح المعنى وبيانه","concept_gloss":"gizli anlamı açıklayıp anlaşılır kılma","contextual_glosses":[{"applicability":"Bir sözün, işin veya meselenin ne demek olduğunu açık ve anlaşılır biçimde ortaya koyan genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anlamı açığa çıkarma ve dinleyenin ya da okuyanın anlayacağı duruma getirme eylemini korur."},"facet_ids":["F001"],"text":"açıklamak","usage_role":"general"},{"applicability":"Kapalı veya güç bir sözün ayrıntılarının çözülerek anlamının görünür kılındığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güç içeriği ayrıntılandırma, yorumlama ve kapalılığını giderme yönlerini korur."},"facet_ids":["F002"],"text":"yorumlayıp açıklamak","usage_role":"contextual"}],"definition":"Bir sözün, işin ya da güç meselenin gizli veya belirsiz anlamını açığa çıkararak onu anlaşılır duruma getirmek; gerektiğinde ayrıntılandırıp yorumlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirsiz ya da gizli anlamı açıklayıp görünür ve anlaşılır kılar."},{"facet_id":"F002","role":"specialization","statement":"Güç bir söz veya meseleyi ayrıntılandırarak yorumlar ve kapalılığını giderir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Açıklayan kişinin eylemini, anlayan kişinin zihinsel sonucuyla karıştırır.","fit":"narrowing","loses":"Anlamı başkası için etkin biçimde açığa çıkarma ve açıklama işlemini kaybeder.","preserves":"Bir anlamın kavranması sonucunu kısmen korur."},"text":"anlamak"}],"identity_rationale":"Dalın kaynak ifadesi, sözün, bir işin ya da güç bir meselenin gizli kalan anlamını açığa çıkarıp anlaşılır kılma eylemini ortak çekirdek olarak verir. Geçici çerçevedeki açıklama, açığa çıkarma, yorumlama ve anlama unsurları bu çekirdeği doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"açıklama; gizli anlamı ortaya çıkarma"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım herhangi bir kalıba bağlı özel anlam eklemeden açıklama eylemini verir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; açıklama, kavrama ve anlamı kapatma eksenlerinde sınırı en açık gösteren üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal söz ve mesele merkezli açıklama eylemini öne çıkarır; komşu dal ise açıklanan nesne türlerini daha geniş tutar ve soru yoluyla açıklık istemeyi de kapsar.","focus_only":"Özellikle söz, iş ve güç meselenin anlamını ayrıntılandırarak açar.","gloss":"açıklama ve anlamı açığa çıkarma","neighbor_only":"Kitap, sözcük, düş ve örtülü nesne gibi daha geniş açıklama nesnelerini de kapsar.","neighbor_ref":"root_001155/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kapalı bir anlamı görünür ve anlaşılır duruma getirme çekirdeğini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal anlamı açıklayıp başkasına görünür kılan eylemdir; komşu dal ise açıklama yapılmış olsun ya da olmasın anlamı kavrama durumudur.","focus_only":"Anlamı açıklayan kişinin etkin açığa çıkarma işlemini bildirir.","gloss":"açıklama ile kavrama","neighbor_only":"Bir kişinin sözü veya bilgiyi zihninde kavramasını bildirir.","neighbor_ref":"root_001171/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sözün ya da anlamın anlaşılır olmasıyla ilgilidir."},{"boundary_match":"opposed","distinction":"Odak dal gizli anlamı açarak anlaşılmayı sağlar; komşu dal sözü bilmece gibi kapatarak anlaşılmayı zorlaştırır.","focus_only":"Kapalı anlamı açar ve anlaşılmasını kolaylaştırır.","gloss":"açıklık ile kapalılık karşıtlığı","neighbor_only":"Sözü bilerek güçleştirir ve muhatabın anlamasını engeller.","neighbor_ref":"root_001070/B005","relation_type":"polarity_pair","shared_zone":"Her iki dal da bir sözün muhatap tarafından anlaşılma derecesini düzenler."}],"source_phrase_ar":"شرحت الكلام وغيره شرحا إذا بينته (maqayis)؛ الشرح البيان اشرح أي بين (ayn)؛ شرحت لك الأمر إذا أوضحته وكشفته (jamhara)؛ شرحت الغامض إذا فسرته (sihah)؛ شرح مسألة مشكلة إذا بينها والشرح البيان والفهم (tahdhib)؛ شرح المشكل من الكلام بسطه وإظهار ما يخفى من معانيه (mufradat)","source_summary":"Kaynaklar, temel anlamı bir sözün veya meselenin kapalı yönünü açıklamak, gizli anlamını açığa çıkarmak ve anlaşılmasını sağlamak olarak birlikte sunar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه شرح الكلام والأمر والمسألة المشكلة وبيان الغامض وكشفه وتفسيره والفهم.","what_is_not_ar":"لا يدخل فيه تقطيع اللحم ولا مجرد اتساع الصدر إلا من جهة الصورة العامة للفتح والبسط."},"support_links":["sup_285ae75f1c269bd3cbb0"]},{"boundary":"Dal et üzerindeki kesme, yayma ve inceltme işlemleriyle bunların ürünlerini kapsar; anlam açıklamayı veya genel kesmeyi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000784/B002","candidate_links":[{"candidate_id":"cand_d91c42acfd3914df5c51","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"eti kesip yayarak parça veya dilim elde etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eti kemik üzerinde ya da organdan ayırarak keser, yayar veya inceltir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlem sonucundaki et parçasını, ince dilimi veya yayvan yağlı eti adlandırır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kurutulmuş durumda bütünlüğü korunarak getirilen bir ceylan parçası için de kullanılır."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Et üzerindeki kesme, ayırma, yayma ve inceltme işlemleri ile ortaya çıkan parçayı birlikte temsil eder.","boundary_detail":"Dal et üzerindeki kesme, yayma ve inceltme işlemleriyle bunların ürünlerini kapsar; anlam açıklamayı veya genel kesmeyi kapsamaz.","branch_image_ar":"بسط اللحم وتقطيعه","concept_gloss":"eti kesip yayarak parça veya dilim elde etme","contextual_glosses":[{"applicability":"Etin kemik üzerinde kesildiği veya organdan ayrılarak parçalara bölündüğü eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin kesilmesi, ayrılması ve parçalara dönüştürülmesi işlemlerini korur."},"facet_ids":["F001"],"text":"eti parçalara ayırmak","usage_role":"general"},{"applicability":"İşlem sonucunda elde edilen ince veya yayvan bir et parçasının adlandırıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Et parçası olma, inceltilme ve yayvan bir dilim biçimi kazanma özelliklerini korur."},"facet_ids":["F002"],"text":"ince et dilimi","usage_role":"contextual"}],"definition":"Eti kemik üzerinde veya organdan ayırarak kesmek, yaymak ya da inceltmek ve böylece parça, dilim veya yayvan et elde etmektir. Bazı biçimler doğrudan bu işlemin ürününü adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eti kemik üzerinde ya da organdan ayırarak keser, yayar veya inceltir."},{"facet_id":"F002","role":"specialization","statement":"İşlem sonucundaki et parçasını, ince dilimi veya yayvan yağlı eti adlandırır."},{"facet_id":"F003","role":"example","statement":"Kurutulmuş durumda bütünlüğü korunarak getirilen bir ceylan parçası için de kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Et dışındaki her türlü nesnenin kesilmesini de sınırsız biçimde kapsar.","collision":"Dala özgü yayma, inceltme ve et parçası sonucu görünmez olur.","fit":"broadening","loses":null,"preserves":"Etin parçalara ayrılması işlemini kısmen korur."},"text":"kesmek"}],"identity_rationale":"Kaynak ifadesi eti kemik üzerinde ya da organdan ayırarak kesmeyi, yaymayı ve inceltmeyi aynı maddi işlem alanında toplar; ayrıca bu işlemin ürünü olan parça ve dilim adlarını verir. Geçici çerçeve bu işlem ile sonuç arasındaki bağı doğru kurmaktadır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"eti kesme ya da yayma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"eti parçalara ayırma ya da inceltme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"et parçası"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ince et dilimi ya da et parçası"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yayvan, yağlı et parçası"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kesilmiş ya da yayılmış et"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kurutulmuş halde getirilen ceylan parçası"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kesilmiş ya da yayılmış et"}],"lexicalization_note":"Yalın işlem anlamı, et parçası bildiren biçimler ve ete bağlı kalıplar ayrı tutulur; kalıplardaki ayrıntılar bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; et kesme, küçük doğrama, kesilmiş parça ve kurutmak için serme sınırlarını gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kesmeye ek olarak eti yayma, inceltme ve ürün adlarını içerir; komşu dalın verilen sınırı yalnızca kesme eylemidir.","focus_only":"Eti yayma, inceltme ve ortaya çıkan parça adlarını da kapsar.","gloss":"eti kesme ve yayma","neighbor_only":"Yalnızca eti kesme eylemini kısa ve sınırlı biçimde bildirir.","neighbor_ref":"root_000419/B006","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği eti keserek parçalara ayırmaktır."},{"boundary_match":"partial","distinction":"Odak dalda parçaların küçük olması zorunlu değildir ve yayma ya da inceltme de bulunur; komşu dal küçük doğrama biçimiyle sınırlıdır.","focus_only":"Kemik üzerinde kesme, organdan ayırma, yayma ve dilim sonucu içerir.","gloss":"eti dilimleme ile küçük doğrama","neighbor_only":"Eti özellikle küçük parçalara doğrama koşulunu öne çıkarır.","neighbor_ref":"root_000401/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da eti keserek daha küçük parçalara dönüştürür."},{"boundary_match":"partial","distinction":"Odak dal et işleminin biçimine ve et dilimine bağlıdır; komşu dal daha genel bir kesme ve kesilmiş parça alanına yayılır.","focus_only":"Etin yayılması, inceltilmesi ve yayvan dilim biçimi kazanması bulunur.","gloss":"et dilimi ile kesilmiş parça","neighbor_only":"Et dışındaki şeyleri, yara türünü ve sürüden ayrılan kümeyi de kapsar.","neighbor_ref":"root_000123/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kesme işlemiyle ortaya çıkan bir et parçasını adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği eti kesme, yayma ve inceltmedir; komşu dalda nesne türü geniştir ve serme işleminin amacı güneşte kurutmadır.","focus_only":"Eti keserek veya incelterek parça ve dilim üretir.","gloss":"eti yayma ile kurutmak için serme","neighbor_only":"Bir şeyi özellikle güneşte kuruması için serme amacını gerektirir.","neighbor_ref":"root_000787/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da etin yüzeye yayılması mümkün bir ortak görünüş oluşturur."}],"source_phrase_ar":"اشتقاقه من تشريح اللحم (maqayis)؛ الشرح والتشريح قطع اللحم على العظام والقطعة شرحة (ayn)؛ الشريحة من اللحم القطعة المرققة وكل قطعة من اللحم شرحة وشريحة (jamhara)؛ ومنه تشريح اللحم والقطعة منه شريحة وكل سمين من اللحم ممتد فهو شريحة وشريح (sihah)؛ الشرح والتشريح قطع اللحم عن العضو وكل قطعة شرحة والتصفيف نحو من التشريح (tahdhib)؛ أصل الشرح بسط اللحم ونحوه (mufradat)","source_summary":"Kaynaklar eti kesme, kemikten veya organdan ayırma, yayma ve inceltme işlemlerini ortak bir alanda birleştirir; parça ve ince dilim adlarını da bu işlemin sonucu olarak verir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه تشريح اللحم وقطعه عن العضو أو على العظام، والشرحة والشريحة واللحم الممدد أو المرقق، وشرحة الظباء اليابسة.","what_is_not_ar":"لا يدخل فيه بيان الكلام ولا شرح الصدر إلا إذا جعلته المصادر امتدادا لصورة البسط."},"support_links":["sup_07120fc2461a63f214df"]},{"boundary":"Dal içsel genişlik ve iyiliği ya da gerçeği kabul etmeye açılmadır; açıklama eylemi veya dünyaya yönelen edinme isteği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000784/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"iyiliği ve gerçeği kabule açılan içsel ferahlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yalın biçimde genişlik, açılma ve ferahlık bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İç dünyayı iyiliği veya gerçeği kabul edecek ölçüde genişletip açar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Manevi açılmayı aydınlık ve dinginliğin iç dünyayı genişletmesiyle ilişkilendirir."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İç dünyanın genişletilmesi, kabul yeteneği kazanması ve ferahlaması çekirdeğini birlikte karşılar.","boundary_detail":"Dal içsel genişlik ve iyiliği ya da gerçeği kabul etmeye açılmadır; açıklama eylemi veya dünyaya yönelen edinme isteği değildir.","branch_image_ar":"اتساع الصدر لقبول الخير","concept_gloss":"iyiliği ve gerçeği kabule açılan içsel ferahlık","contextual_glosses":[{"applicability":"Kişinin iç dünyasının açılıp genişlediği ve iyiliği kabul etmeye elverişli hale geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçsel açılma, genişleme ve ferahlama sonucunu doğal bir anlatımla korur."},"facet_ids":["F001","F002"],"text":"içi ferahlamak","usage_role":"contextual"},{"applicability":"Gerçeği kabul etmeyi sağlayan manevi genişleme ve dinginlik yönünün açıkça belirtilmesi gereken bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İç dünyayı genişletme, gerçeği kabul etme ve manevi açılma ilişkisini korur."},"facet_ids":["F002","F003"],"text":"içini gerçeğe açmak","usage_role":"explanatory"}],"definition":"İç dünyayı iyiliği veya gerçeği kabul edebilecek biçimde genişletip açmak ve bunun sonucunda ferahlık kazanmaktır. Bu açılma aydınlık ve dinginlikle desteklenen manevi bir kabul durumu olarak da tasvir edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yalın biçimde genişlik, açılma ve ferahlık bildirir."},{"facet_id":"F002","role":"specialization","statement":"İç dünyayı iyiliği veya gerçeği kabul edecek ölçüde genişletip açar."},{"facet_id":"F003","role":"associated_use","statement":"Manevi açılmayı aydınlık ve dinginliğin iç dünyayı genişletmesiyle ilişkilendirir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü bedensel veya gündelik rahatlamayla karışabilir.","fit":"narrowing","loses":"İç dünyanın iyiliği veya gerçeği kabul edecek biçimde genişlemesi koşulunu kaybeder.","preserves":"Sıkıntının azalması ve ferahlık sonucunu korur."},"text":"rahatlama"}],"identity_rationale":"Kaynak ifadesi yalın biçimde genişlik ve ferahlığı, belirli kullanımda ise insanın iç dünyasının iyiliği veya gerçeği kabul edecek biçimde genişletilip açılmasını bildirir. Geçici çerçeve, kabul edici içsel genişleme ile aydınlık ve dinginlik tasvirini doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"genişlik ve ferahlık"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iç dünyayı iyiliği veya gerçeği kabul edecek biçimde genişletme"}],"lexicalization_note":"Yalın genişlik anlamı ile iç dünyayı kabule açan kalıba bağlı kullanım ayrılır; kalıbın manevi koşulları yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; mekânsal boşluk ve beden bölgesi adayları yalnızca uzak çağrışım taşıdığı için, sınırı açıklayan iki kök içi karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal alıcının içsel kabul kapasitesinin genişlemesidir; komşu dal ise açıklayan kişinin bir anlamı söz yoluyla açığa çıkarmasıdır.","focus_only":"İç dünyayı iyiliği veya gerçeği kabul etmeye açıp genişletir.","gloss":"içsel açılma ile anlamı açıklama","neighbor_only":"Bir sözün ya da meselenin gizli anlamını açıklayıp görünür kılar.","neighbor_ref":"root_000784/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kapalı bir şeyin açılması biçiminde ortak bir tasarıma dayanır."},{"boundary_match":"partial","distinction":"Odak dal manevi kabul ve dinginliğe açılır; komşu dal yalnızca dünya malına yönelme ve onu edinme isteğine bağlıdır.","focus_only":"İyilik veya gerçeği kabul etmeye dönük manevi ferahlık bildirir.","gloss":"kabule açılma ile dünyaya yönelme","neighbor_only":"Dünya malını geniş ölçüde edinmeye yönelen istek bildirir.","neighbor_ref":"root_000784/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin iç yönelişinin bir hedefe doğru genişlemesi tasarlanır."}],"source_phrase_ar":"الشرح السعة وشرح الله صدره للإسلام أي وسعه (ayn)؛ شرح الله صدره فانشرح إذا اتسع لقبول الخير (jamhara)؛ شرح الله صدره للاسلام فانشرح (sihah)؛ شرح الله صدره فانشرح أي وسع صدره لقبول الحق فاتسع (tahdhib)؛ شرح الصدر أي بسطه بنور إلهي وسكينة (mufradat)","source_summary":"Kaynaklar genişlik ve ferahlık çekirdeğinde birleşir; özel kullanımda bu genişleme, insanın iç dünyasının iyiliği veya gerçeği kabul etmeye açılması ve dinginlik kazanmasıdır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه شرح الله الصدر للإسلام أو للحق، وانشراحه واتساعه لقبول الخير، وبسط الصدر بنور وسكينة.","what_is_not_ar":"لا يدخل فيه شرح الكلام ولا تقطيع اللحم، ولا الرغبة في الدنيا إلا بوصفها انبساطا نفسيا مفصولا هنا."},"support_links":[]},{"boundary":"Eylem kalıpları, bekâreti bozma adı ve örtmece organ adı birbirine indirgenmeden aynı kullanım kümesinde tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000784/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"belirli biçimde cinsel birleşme, bekâreti bozma ve örtmece organ adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadını sırtüstü yatırarak ya da belirli bir biçimde onunla cinsel ilişkide bulunmayı bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bekâretin cinsel birleşme sonucunda bozulmasını adlandırır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ad biçimi kadın cinsel organını doğrudan söylemeden anlatan örtmece olarak kullanılır."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylem, sonuç ve örtmece ad düzlemlerini tek bir kullanım kümesi olarak eksiksiz belirtir.","boundary_detail":"Eylem kalıpları, bekâreti bozma adı ve örtmece organ adı birbirine indirgenmeden aynı kullanım kümesinde tutulur.","branch_image_ar":"فتح جنسي وافتضاض","concept_gloss":"belirli biçimde cinsel birleşme, bekâreti bozma ve örtmece organ adı","contextual_glosses":[{"applicability":"Kadının sırtüstü yatırılmasıyla tanımlanan belirli cinsel birleşme eyleminin açıklandığı bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadının konumunu ve ardından gerçekleşen cinsel birleşme eylemini korur."},"facet_ids":["F001"],"text":"kadını sırtüstü yatırarak onunla cinsel ilişkiye girmek","usage_role":"contextual"},{"applicability":"Eylemin belirli sonucu olarak bekâretin bozulmasının adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bekâretin cinsel birleşme sonucunda bozulması yönünü açıkça korur."},"facet_ids":["F002"],"text":"bekâreti cinsel birleşmeyle bozmak","usage_role":"contextual"},{"applicability":"Kadın cinsel organını doğrudan söylemeden anan ad biçiminin açıklanması gereken bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın cinsel organına gönderimi ve doğrudan söylemekten kaçınan örtmece niteliğini korur."},"facet_ids":["F003"],"text":"kadın cinsel organı için örtmece","usage_role":"explanatory"}],"definition":"Bu kullanım kümesi, kadını sırtüstü yatırarak veya belirli bir biçimde cinsel ilişkide bulunmayı ve bekâretin cinsel birleşmeyle bozulmasını bildirir. Ayrı bir ad biçimi de kadın cinsel organı için örtmece olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadını sırtüstü yatırarak ya da belirli bir biçimde onunla cinsel ilişkide bulunmayı bildirir."},{"facet_id":"F002","role":"specialization","statement":"Bekâretin cinsel birleşme sonucunda bozulmasını adlandırır."},{"facet_id":"F003","role":"associated_use","statement":"Bir ad biçimi kadın cinsel organını doğrudan söylemeden anlatan örtmece olarak kullanılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü cinsel ilişki biçimini ayrım yapmadan kapsar.","collision":"Belirli konumu, bekâreti bozma sonucunu ve örtmece ad kullanımını görünmez kılar.","fit":"broadening","loses":null,"preserves":"Cinsel birleşme alanındaki genel eylemi korur."},"text":"cinsel ilişki"}],"identity_rationale":"Kaynak ifadesi tek bir cinsel çekirdeğin eşdeğer anlatımlarını değil, belirli biçimde cinsel birleşme eylemini, bekâretin cinsel birleşmeyle bozulmasını ve kadın cinsel organına yönelik örtmece bir adı aynı dalda toplar. Dal korunabilir, ancak bu üç kullanım tanımda ayrı düzlemler olarak belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kadını sırtüstü yatırarak onunla cinsel ilişkiye girme"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kadınlarla belirli bir biçimde cinsel ilişkiye girme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bekâreti cinsel birleşmeyle bozma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kadın cinsel organı için örtmece ad"}],"lexicalization_note":"Cinsel birleşme bildiren kalıplar, bekâreti bozma bildiren yalın biçim ve örtmece organ adı ayrı tutulur; biri bütün dalın tek anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel cinsel birleşme, kadınla birleşme, bekâretin karşıt durumu ve örtmece organ adını ayıran dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir konum, bekâreti bozma sonucu ve kadın organına yönelik ayrı bir örtmece içerir; komşu dal cinsel birleşmenin genel adlandırma alanıdır.","focus_only":"Belirli birleşme biçimini, bekâreti bozmayı ve örtmece organ adını kapsar.","gloss":"özel cinsel kullanım ile genel birleşme","neighbor_only":"Cinsel birleşmeyi genel ve doğrudan ya da başka bir örtmece sözle bildirir.","neighbor_ref":"root_001548/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da cinsel birleşme eylemini açık veya örtük biçimde adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın eyleminde belirli bir beden konumu tanımlanır ve başka ad kullanımları da vardır; komşu dal yalnızca kadınla birleşme eylemini verir.","focus_only":"Belirli konumu ve bekâreti bozma ile örtmece organ adı yanlarını içerir.","gloss":"belirli birleşme biçimi ile kadınla birleşme","neighbor_only":"Bir kadınla cinsel ilişkiye girme anlamını tek bir kalıpla ve daha genel verir.","neighbor_ref":"root_000793/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kadınla cinsel ilişkide bulunma eylemini bildirir."},{"boundary_match":"opposed","distinction":"Odak dal eksenin bozulma ve cinsel temas ucundadır; komşu dal ise dokunulmamışlık ve bekâretin sürmesi ucundadır.","focus_only":"Bekâretin cinsel birleşmeyle bozulması sonucunu içerir.","gloss":"bekâreti bozma ile bekâretin korunması","neighbor_only":"Cinsel temasın bulunmamasını ve bekâretin korunmasını içerir.","neighbor_ref":"root_000143/B004","relation_type":"polarity_pair","shared_zone":"İki dal bekâretin cinsel temas karşısındaki durumunu aynı eksende ele alır."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir kadın organı örtmecesidir ve cinsel eylem anlamlarıyla aynı kümededir; komşu dal daha geniş bir beden bölgesi ve cinsel organ alanıdır.","focus_only":"Kadın cinsel organını örtmeceyle anan özel bir ad biçimi içerir.","gloss":"özel örtmece ile genel cinsel organ alanı","neighbor_only":"Kadın, erkek ve hayvanlarda bacak arası ile cinsel organ alanını genişçe adlandırır.","neighbor_ref":"root_001139/B003","relation_type":"same_field","shared_zone":"Her iki dal kadın cinsel organına gönderimde bulunabilen örtülü adlandırmalar içerir."}],"source_phrase_ar":"ربما سمي فرج المرأة شريحا كناية (jamhara)؛ شرح جاريته إذا سلقها على قفاها ثم غشيها ويشرحون النساء شرحا والشرح افتضاض الأبكار (tahdhib)","source_summary":"Toplu kanıt, belirli bir cinsel birleşme biçimini ve bekâretin bozulmasını eylem alanında bir araya getirirken, kadın cinsel organına yönelik örtmece adı ilişkili fakat ayrı bir ad kullanımı olarak gösterir.","sources":["JA","TA"],"what_is_ar":"يدخل فيه شرح الجارية أو النساء بمعنى هيئة الجماع، والشرح بمعنى افتضاض الأبكار، وشريح كناية عن فرج المرأة.","what_is_not_ar":"لا يدخل فيه شرح الصدر ولا بيان الكلام ولا تشريح اللحم في الاستعمال العادي."},"support_links":[]},{"boundary":"Dal yalnızca dünya malına yönelip onu geniş ölçüde edinme isteğini bildiren kalıpla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000784/B005","candidate_links":[{"candidate_id":"cand_27669bb52d6e9995c065","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"dünya malını geniş ölçüde edinme isteği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin isteği dünya malına doğru açılır ve ona güçlü biçimde yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yöneliş, dünya malını geniş ölçüde edinme isteğini içerir."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dünya malına yönelme, güçlü istek ve onu edinme hedefini taşıyan kalıba bağlı anlamı eksiksiz karşılar.","boundary_detail":"Dal yalnızca dünya malına yönelip onu geniş ölçüde edinme isteğini bildiren kalıpla sınırlıdır.","branch_image_ar":"انبساط الرغبة إلى الشيء","concept_gloss":"dünya malını geniş ölçüde edinme isteği","contextual_glosses":[{"applicability":"Kişinin dünya malını edinmeye güçlü ve geniş bir istekle yöneldiğinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dünya malını hedef alma, ona güçlü biçimde yönelme ve edinme isteğini korur."},"facet_ids":["F001","F002"],"text":"dünya malına tutkuyla yönelmek","usage_role":"contextual"}],"definition":"Dünya malına güçlü biçimde yönelmek ve onu geniş ölçüde edinmeye istek duymaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin isteği dünya malına doğru açılır ve ona güçlü biçimde yönelir."},{"facet_id":"F002","role":"specialization","statement":"Yöneliş, dünya malını geniş ölçüde edinme isteğini içerir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü nesneye ve her güçteki isteğe uygulanabilir.","collision":"Dünya malı hedefini ve geniş ölçüde edinme yönelişini siler.","fit":"broadening","loses":null,"preserves":"Bir şeye yönelik istek bulunmasını korur."},"text":"istemek"}],"identity_rationale":"Kaynak ifadesi belirli bir yönelme kalıbında kişinin dünya malına açılıp onu geniş ölçüde edinmek istemesini açıkça tanımlar. Geçici çerçeve hem hedefi hem güçlü edinme isteğini koruduğu için dal kimliği uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"dünya malına yönelip onu geniş ölçüde edinmek isteme"}],"lexicalization_note":"Tanım yalnızca dünya malına yönelmeyi bildiren kalıba bağlıdır; bu istek yalın kökün genel anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yönelme, aşırı istek ve haz arzusu ile olan sınırları en iyi gösteren üç aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın hedefi dünya malıdır ve amaç onu geniş ölçüde edinmektir; komşu dalın hedefi geneldir ve isteksizlik ile yüz çevirme yönünü de içerir.","focus_only":"Yalnızca dünya malını geniş ölçüde edinmeye dönük güçlü yönelişi bildirir.","gloss":"dünya malına yönelme ile genel istek","neighbor_only":"Herhangi bir şeye yönelmeyi veya ondan yüz çevirip vazgeçmeyi de kapsar.","neighbor_ref":"root_000575/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin bir hedefe istek ve eğilimle yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dal dünya malını geniş ölçüde edinmeye yönelir; komşu dal hedef bakımından daha geniştir ve aşırılık ile açgözlülüğü çekirdek yapar.","focus_only":"Dünya malını edinmeye bağlı belirli bir yönelme kalıbıyla sınırlıdır.","gloss":"dünya malı isteği ile aşırı istek","neighbor_only":"Yarar, doğru yol veya yaşam gibi farklı hedeflere yönelik aşırı isteği de kapsar.","neighbor_ref":"root_000308/B002","relation_type":"near_synonym","shared_zone":"İki dal da sıradan ölçüyü aşabilen güçlü istek ve elde etme eğilimi taşır."},{"boundary_match":"partial","distinction":"Odak dal dünya malını edinme amacıyla sınırlıdır; komşu dal haz veren şeylere yönelik daha genel iştah ve arzu alanındadır.","focus_only":"Dünya malını edinmeye yönelik iradi ve geniş bir yöneliş bildirir.","gloss":"edinme isteği ile haz arzusu","neighbor_only":"İştah duyulan veya haz veren nesneye yönelik bedensel ya da ruhsal arzu bildirir.","neighbor_ref":"root_000825/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin arzulanan bir hedefe doğru güçlü iç yönelişi vardır."}],"source_phrase_ar":"أكان الأنبياء يشرحون إلى الدنيا يريد كانوا ينبسطون إليها ويرغبون في اقتنائها رغبة واسعة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Belirli kalıp, dünya malına açılıp onu geniş ölçüde edinmeye güçlü istek duymayı bildirir."}],"source_summary":"Bu dal için paylaşılan çok kaynaklı bir özet yoktur; kullanım tek bir kaynak tanıklığıyla sınırlıdır.","sources":["TA"],"what_is_ar":"يدخل فيه الانبساط إلى الدنيا والرغبة الواسعة في اقتنائها.","what_is_not_ar":"لا يدخل فيه شرح الصدر لقبول الحق، ولا البيان، ولا اللحم."},"support_links":["sup_47294475791d784a05b0"]},{"boundary":"Dal koruma ve koruyan kişi çekirdeğindedir; ekin bekçiliği bunun bölgesel ve tarımsal uzmanlaşmasıdır.","branch_kind":"bare","branch_ref":"root_000784/B006","candidate_links":[{"candidate_id":"cand_d441fa0e383ad2cd97ae","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","surface_ar":"نَشْرَحْ"}],"gloss":"koruma ve koruyucu gözetimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi zarardan koruma ve gözetme eylemini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma görevini üstlenen kişiyi, özellikle ekini kuşlardan ve başka tehditlerden koruyan bekçiyi adlandırır."}}],"root_ar":"ش ر ح","root_id":"root_000784","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel koruma eylemini, koruyucu kişiyi ve ekin bekçiliği uzmanlaşmasını aynı çekirdek çevresinde karşılar.","boundary_detail":"Dal koruma ve koruyan kişi çekirdeğindedir; ekin bekçiliği bunun bölgesel ve tarımsal uzmanlaşmasıdır.","branch_image_ar":"حراسة الشيء وحفظه","concept_gloss":"koruma ve koruyucu gözetimi","contextual_glosses":[{"applicability":"Bir şeyi zarardan uzak tutmak ve güvenliğini sürekli gözetmek anlamındaki yalın kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zararı önleme, koruma ve dikkatle gözetme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"koruyup gözetmek","usage_role":"general"},{"applicability":"Ekini kuşlardan ve başka tehditlerden koruyan kişinin adlandırıldığı bölgesel tarım bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koruyucu kişiyi, korunan ekini ve kuşlara karşı gözetim görevini korur."},"facet_ids":["F002"],"text":"ekin bekçisi","usage_role":"contextual"}],"definition":"Bir şeyi zarardan korumak ve gözetmek, ayrıca bu görevi üstlenen koruyucu kişiyi adlandırmaktır. Bölgesel kullanımda koruyucu, ekini kuşlardan ve başka tehditlerden uzak tutan bekçidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi zarardan koruma ve gözetme eylemini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Koruma görevini üstlenen kişiyi, özellikle ekini kuşlardan ve başka tehditlerden koruyan bekçiyi adlandırır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her tür mekân veya kişi bekçisiyle karışabilir.","fit":"narrowing","loses":"Yalın koruma eylemini ve koruyucunun ekine bağlı özel görevini tek başına vermez.","preserves":"Koruma görevini üstlenen kişi yönünü korur."},"text":"bekçi"}],"identity_rationale":"Kaynak ifadesi yalın biçimde koruma anlamını ve koruyan kişiyi verir; bölgesel kullanımda bu kişi ekini kuşlardan ve başka tehditlerden korur. Geçici çerçeve genel çekirdek ile tarımsal uzmanlaşmayı doğru sırada sunar.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"koruma ve gözetme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"koruyucu ya da ekin bekçisi"}],"lexicalization_note":"Dalın yalın anlamı koruma ve gözetmedir; ekin bekçisi örneği çekirdeği daraltmadan uzmanlaşmış kullanım olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bekçilik, gözcülük, izleyerek koruma ve bakım sorumluluğu sınırlarını gösteren dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel koruma yanında belirli bir tarımsal koruyucu kullanım taşır; komşu dal koruma görevlileri ve kişinin kendini koruması bakımından daha geniştir.","focus_only":"Bölgesel olarak ekini kuşlardan ve başka tehditlerden koruyan kişiyi adlandırır.","gloss":"koruma ile genel bekçilik","neighbor_only":"Hükümdar muhafızı, yer bekçisi ve kişinin kendi güvenliği için önlem almasını da kapsar.","neighbor_ref":"root_000307/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeği bir şeyi tehlike ve zarardan koruyup gözetmektir."},{"boundary_match":"partial","distinction":"Odak dalda koruma ve ekin bekçiliği öndedir; komşu dal koruyucuya ek olarak gözcü ve öncü rollerini içerir.","focus_only":"Ekin ve benzeri korunacak şeylere yönelik koruma eylemini ve koruyucuyu bildirir.","gloss":"koruyucu ile gözcü","neighbor_only":"Gözcülük yapan öncü ve bir topluluk adına çevreyi izleyen kişi rollerini de kapsar.","neighbor_ref":"root_000584/B002","relation_type":"near_synonym","shared_zone":"İki dal da koruyan, gözeten ve tehlikeyi uzak tutan kişi anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal koruma sonucunu ve koruyucu kişiyi öne çıkarır; komşu dal korumayı bakma ve izleme yöntemiyle sınırlar.","focus_only":"Koruma çekirdeğinden koruyucu kişi ve ekin bekçisi adını türetir.","gloss":"koruma ile izleyerek koruma","neighbor_only":"Korumanın yöntemi olarak sürekli bakma, izleme ve göz gezdirmeyi özellikle gerektirir.","neighbor_ref":"root_001317/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da tehlikeye karşı koruma ve gözetim işlevini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal zarar ve kuşlara karşı korumayı öne çıkarır; komşu dal korumayı sürekli bakım, sorumluluk ve durumunu izleme yönleriyle genişletir.","focus_only":"Bölgesel ekin bekçiliğini ve kuşları uzak tutma görevini içerir.","gloss":"koruma ile bakım sorumluluğu","neighbor_only":"Bir şeyi gözetmenin yanında bakımını üstlenme, durumunu izleme ve sorumluluğunu taşıma anlamlarını içerir.","neighbor_ref":"root_000342/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin güvenliğini gözetme ve onu koruma çekirdeğinde birleşir."}],"source_phrase_ar":"الشارح الحافظ؛ الشرح الحفظ؛ الشارح في كلام أهل اليمن الذي يحفظ الزرع من الطيور وغيرها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Yalın biçim korumayı, kişi adı ise genel koruyucuyu ve bölgesel olarak ekini kuşlardan koruyan bekçiyi bildirir."}],"source_summary":"Bu dal için paylaşılan çok kaynaklı bir özet yoktur; genel koruma çekirdeği ile tarımsal koruyucu kullanımı tek bir kaynak tanıklığında birlikte verilir.","sources":["TA"],"what_is_ar":"يدخل فيه الشرح بمعنى الحفظ، والشارح حافظ الزرع أو صغار النخل من الطير وغيره.","what_is_not_ar":"لا يدخل فيه البيان ولا الصدر ولا اللحم، وهو استعمال لهجي أو منقول في تهذيب اللغة."},"support_links":["sup_4cfc6f76c26f3e2cf3f4"]},{"boundary":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B001","candidate_links":[{"candidate_id":"cand_857f6a79f82947db1dc6","lane":"micro"},{"candidate_id":"cand_d91c42acfd3914df5c51","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"göğüs bölgesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvan gövdesindeki temel anatomik bölgeyi karşılar; dalın öteki kullanımları bu anlamdan türemiştir.","boundary_detail":"Dalın çekirdeği göğüs bölgesidir; giysi, damga, bağ, rahatsızlık ve güçlü göğüslü aslan kullanımları bu çekirdeğe bağlıdır.","branch_image_ar":"الصدر الجارحة وما يتصل بها","concept_gloss":"göğüs bölgesi","contextual_glosses":[{"applicability":"İnsan göğsünün üstte belirginleşen özel kesiminden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğsün üstte çıkıntı yapan kesimine yönelik dar bağlamı korur."},"facet_ids":["F002"],"text":"göğsün üst çıkıntısı","usage_role":"contextual"},{"applicability":"Bir kişinin göğsünde ağrı ya da rahatsızlık bulunmasını anlatan eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Rahatsızlığın göğüs bölgesinde bulunması bilgisini korur."},"facet_ids":["F003"],"text":"göğsü ağrımak","usage_role":"contextual"},{"applicability":"Bir hayvanda yükü sabitlemek üzere göğüs çevresinden geçirilen bağ veya kemer için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin göğüste bulunmasını ve yükü sabitleme görevini korur."},"facet_ids":["F004"],"text":"göğüs bağı","usage_role":"contextual"}],"definition":"İnsan ya da hayvan gövdesinin boyun ile karın arasında kalan ön ve üst bölgesidir. Bu çekirdekten, üstte kabaran kesim, buradaki ağrı veya yaralanma, bölgeyi örten ya da bağlayan nesneler, üzerindeki damga ve güçlü göğsüyle nitelenen aslan kullanımları doğar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvan gövdesinin boyun altındaki ön bölgesini belirtir."},{"facet_id":"F002","role":"specialization","statement":"İnsanda göğsün üstte belirgin biçimde çıkıntı yapan kesimini gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Göğsün ağrıması, bu bölgeden rahatsız olma veya göğse bir şeyle vurma bu bedensel çekirdeğe bağlı kullanımlardır."},{"facet_id":"F004","role":"associated_use","statement":"Göğsü örten giysi, hayvanın göğsündeki damga ve yükü tutan göğüs bağı aynı beden bölgesine göre adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Aslana verilen ad, hayvanın güçlü göğüslü oluşuna dayanan bir nitelemedir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamansal ya da sırasal ilk olma anlamını ekler.","collision":"Aynı kökün ön, üst ve ilk kesim dalıyla karışır.","fit":"displacement","loses":"Anatomik göğüs bölgesini ve bedensel sınırını bütünüyle kaybeder.","preserves":"Önde bulunma çağrışımını dolaylı olarak koruyabilir."},"text":"başlangıç"}],"identity_rationale":"Kaynak ifadesi, insanın göğsünü temel beden bölgesi olarak verir ve hayvandaki karşılığını, göğsün üstte çıkıntılı kesimini, bu bölgedeki ağrı ya da yaralanmayı ve göğüsle ilişkili nesne ile adlandırmaları aynı dalda toplar. Geçici çerçeve bu çekirdek ile ona bağlı kullanımların sırasını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"göğüsler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göğsün üstte çıkıntılı kesimi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göğsü örten kısa giysi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"devenin göğsündeki damga"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yükü sabitleyen göğüs bağı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"göğsünden rahatsız olan kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birinin göğsüne bir şeyle vurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"göğsü ağrımak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"güçlü göğüslü aslan"}],"lexicalization_note":"Çıplak biçimin anatomik anlamı temel alınır; ağrı, yaralama, örtme, bağlama ve adlandırma anlamları yalnız kendi türemiş biçimleri içinde değerlendirilir.","neighbor_coverage_note":"Bütün adaylar anatomik kapsam ve bağımlı türetimler bakımından değerlendirildi; yalnız eşanlamlı göğüs çekirdeği ile et ve kemik sınırlarını açıklayan üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anatomik sınır bakımından anlamlı bir ayrım yoktur; odak daldaki giysi, ağrı ve benzeri türemiş örnekler eşanlamlı çekirdeği değiştirmez.","focus_only":null,"gloss":"göğüs","neighbor_only":null,"neighbor_ref":"root_001315/B007","relation_type":"synonym","shared_zone":"Her iki dalın çekirdeği de gövdenin ön üst bölümündeki göğüs bölgesidir."},{"boundary_match":"partial","distinction":"Biri beden bölgesinin kendisini, öteki ise o bölgede bulunan belirli dokuyu adlandırır; bu nedenle olağan bağlamlarda birbirinin yerine geçmez.","focus_only":"Odak dalı göğüs bölgesinin tamamını anatomik bir yer olarak belirtir.","gloss":"göğüs eti","neighbor_only":"Komşu dal yalnız göğüs ve boyun çevresindeki eti belirtir.","neighbor_ref":"root_000095/B003","relation_type":"near_neighbor","shared_zone":"İki dal da göğüs çevresindeki aynı beden alanına yönelir."},{"boundary_match":"partial","distinction":"Odak geniş bir anatomik bölgedir; komşu ise bu bölgedeki kemiklere ve belirli bir yüzey konumuna özgüdür.","focus_only":"Odak dalı kemiklerle sınırlı olmayan bütün göğüs bölgesini kapsar.","gloss":"üst göğüs kemikleri","neighbor_only":"Komşu dal köprücük kemiği çevresindeki göğüs kemiklerini ve kolye yerini belirtir.","neighbor_ref":"root_000178/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de göğsün üst bölümünü bedensel konum olarak paylaşır."}],"source_phrase_ar":"الصدر للإنسان والجمع صدور (maqayis)؛ الصدر الجارحة (mufradat)؛ الصدرة من الإنسان ما أشرف من أعلى صدره (ayn;sihah;tahdhib)؛ صدر فلان إذا وجع صدره (ayn;tahdhib)؛ المصدور الذي يشتكي صدره (maqayis;sihah)؛ الصدار ثوب يغطي الصدر (maqayis;ayn;tahdhib;mufradat)؛ الصدار سمة على صدر البعير (maqayis;sihah;mufradat)؛ المصدر الأسد (maqayis;ayn;sihah)","source_summary":"Kaynakların ortak çizgisi göğsü anatomik merkez olarak kurar; üst çıkıntı, ağrı ve yaralama ile giysi, damga ve güçlü göğüslülüğe dayalı adlandırmalar bu merkezden açıklanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صدر الإنسان والحيوان وما أشرف من أعلاه، ووجع الصدر وإصابته، وما يغطى الصدر أو يسمه أو يشد عليه، وما سمي لقوة صدره","what_is_not_ar":"صدر الأمر؛ الصدور عن الماء؛ المصدر النحوي"},"support_links":["sup_07120fc2461a63f214df","sup_285ae75f1c269bd3cbb0"]},{"boundary":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"ön, üst ya da başlangıç bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın konumsal ve sırasal çekirdeğini birlikte vermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Anatomik göğsün kendisi bu dalın çekirdeği değildir; beden bölgesinden taşınan ön, üst veya ilk konum ilişkisi belirleyicidir.","branch_image_ar":"المقدّم والأعلى والأول","concept_gloss":"ön, üst ya da başlangıç bölümü","contextual_glosses":[{"applicability":"Bir nesnenin ya da düzenlenmiş alanın öndeki kesimi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki önde bulunma ilişkisini açık biçimde korur."},"facet_ids":["F001","F002"],"text":"ön kısım","usage_role":"contextual"},{"applicability":"Bir işin, kitabın veya sözün ilk bölümü anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sırasal olarak ilk bölüm olma anlamını eksiksiz korur."},"facet_ids":["F001","F003"],"text":"başlangıç","usage_role":"contextual"},{"applicability":"Bir atın yarışta göğsünü öne çıkararak önce gelmesini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarış üstünlüğünün atın göğsünün önde bulunmasıyla belirlenmesini korur."},"facet_ids":["F004"],"text":"göğüs farkıyla öne geçmek","usage_role":"explanatory"}],"definition":"Bir şeyin önde, üstte ya da başlangıçta bulunan kesimidir. Bu konumsal ve sırasal çekirdek uzun nesnelerin ön veya üst bölümlerinde, toplantı, kitap ve sözün başlangıcında ve atın göğsüyle öne geçmesinde özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, oluş veya düzenin ön, üst ya da ilk kesimini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Mızrak benzeri uzun bir nesnenin üst kısmını ve okun ortasından ucuna uzanan ön bölümünü gösterebilir."},{"facet_id":"F003","role":"extension","statement":"Bir işin, toplantının, kitabın veya sözün ön ya da başlangıç bölümüne uygulanır."},{"facet_id":"F004","role":"associated_use","statement":"Atın göğsünü öne çıkararak rakiplerinden önce gelmesini anlatan yarış kullanımına temel olur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Aynı kökün anatomik göğüs dalıyla karışır.","fit":"narrowing","loses":"Nesnelerin, işlerin ve metinlerin ön veya ilk bölümü olma kapsamını kaybeder.","preserves":"Önde ve üstte bulunma imgesinin bedensel kaynağını korur."},"text":"göğüs"}],"identity_rationale":"Kaynak ifadesi bir şeyin ön, üst veya ilk kesimini ortak çekirdek olarak açıkça verir; uzun nesnelerin bölümleri, işin başlangıcı, toplantı, kitap ve sözün ön kısmı ile atın göğsüyle öne geçmesi bu çekirdeğin düzenli özelleşmeleridir. Geçici çerçeve bu kapsamı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ön, üst ya da başlangıç bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"mızrağın üst bölümü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"işin başlangıcı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"toplantının ön kısmı; kitabın veya sözün başlangıcı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"okun ortasından ucuna uzanan ön bölümü"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ön gövdesi kalın ok"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"göğsüyle öne çıkıp yarışı geçmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kitaba giriş bölümü koymak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"toplantının başköşesine oturmak"}],"lexicalization_note":"Çıplak biçimin ön, üst ve ilk kesim anlamı korunur; nesne, metin, toplantı ve yarış bağlamları kendi yapılarına bağlı özelleşmeler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar konum, sıra ve hareket ayrımı üzerinden değerlendirildi; ön ve ilk bölümle en yakın iki dal, öne geçme olayı ve arka yön karşıtlığı sınırı en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme ön ve ilk bölümde güçlüdür; odak dalının üstlük ve metinsel başlangıç kapsamı ile komşunun belirli beden ve nesne parçaları tam ikameyi engeller.","focus_only":"Odak dalı üst bölüm ve soyut başlangıç anlamlarını da genel çekirdeğe katar.","gloss":"ön veya ilk bölüm","neighbor_only":"Komşu dal yüz, baş, ordu, eyer, meme ve kuş tüyü gibi belirli ön parçaları ayrıca kapsar.","neighbor_ref":"root_001207/B007","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin önde bulunan ya da ilk gelen bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Komşu başlangıç ve ilk görünüş üzerinde yoğunlaşırken odak dalı ayrıca uzamsal önlük ve üstlüğü kurucu seçenekler olarak taşır.","focus_only":"Odak dalı öndeki ve üstteki somut kesimleri de başlangıçla birlikte kapsar.","gloss":"ilk bölüm","neighbor_only":"Komşu dal bitkinin başı, yeni ay ve ayın ilk günleri gibi başlangıç örneklerine özgü uzanımlara sahiptir.","neighbor_ref":"root_001078/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başlangıcını veya ilk görünen kesimini anlatır."},{"boundary_match":"partial","distinction":"Odak ön konumu veya bölümü adlandırır; komşu ise o konuma doğru ilerleme ya da üstünlük kazanma olayını anlatır.","focus_only":"Odak dalı bir şeyin sabit ön, üst veya ilk bölümünü adlandırır.","gloss":"öne geçme","neighbor_only":"Komşu dal öne doğru ilerleme ve başkasını geçme hareketini temel alır.","neighbor_ref":"root_001207/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal önde bulunma ve başkalarından önce gelme alanında buluşur."},{"boundary_match":"opposed","distinction":"Uzamsal ön ve arka anlamları doğrudan karşıttır; odak dalındaki üst ve başlangıç uzanımları bu karşıtlığın dışında kalır.","focus_only":"Odak dalı ön tarafı ve buna bağlı üst veya ilk konumu kapsar.","gloss":"ön ve arka","neighbor_only":"Komşu dal arka tarafı ve önde olanın gerisinde kalma konumunu kapsar.","neighbor_ref":"root_000433/B002","relation_type":"antonym","shared_zone":"İki dal bir nesneye göre yön ve sıra belirleyen ortak bir eksen kurar."}],"source_phrase_ar":"الصدر أعلى مقدم كل شيء (ayn;tahdhib)؛ صدر القناة أعلاها (ayn;sihah;tahdhib;mufradat)؛ صدر الأمر أوله (ayn;tahdhib)؛ صدر كل شيء أوله (sihah)؛ صدر المجلس والكتاب والكلام (mufradat)؛ صدر السهم ما فوق نصفه إلى المراش (ayn;tahdhib)؛ صدر الفرس إذا جاء قد سبق بصدره (sihah;tahdhib;mufradat)","source_summary":"Kaynaklar ön, üst ve ilk olma ilişkisini ortak anlam olarak sunar; nesne bölümleri, metin ve toplantı başlangıçları ile göğsü öne çıkararak kazanılan yarış üstünlüğü bu ilişkinin bağlama göre görünüşleridir.","sources":["AY","SI","TA","MU"],"what_is_ar":"مقدّم الشيء وأعلاه وأوله، كصدر القناة والأمر والكتاب والمجلس والكلام، ومقدّم السهم، وسبق الفرس بصدره","what_is_not_ar":"الصدر الجارحة في نفسها؛ الانصراف عن الورد؛ المصادرة على مال"},"support_links":[]},{"boundary":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000849/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"geldiği yerden ayrılıp dönme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki varış ile sonraki ayrılış aşamalarını birlikte belirtmek gereken genel bağlamlarda kullanılır.","boundary_detail":"Her ayrılma bu dala girmez; çekirdekte daha önce varılan yerden veya girilen durumdan ayrılma ve geri yönelme ilişkisi bulunur.","branch_image_ar":"الصُّدور عن المورد","concept_gloss":"geldiği yerden ayrılıp dönme","contextual_glosses":[{"applicability":"Su içmek üzere gelmiş insan veya hayvanların daha sonra su başını terk etmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su başına gelişten sonraki ayrılma aşamasını tam olarak korur."},"facet_ids":["F001","F002"],"text":"su başından ayrılmak","usage_role":"contextual"},{"applicability":"Bir başkasının geldiği yerden ayrılıp dönmesini sağlama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi başkasına yaptırma ve geri yöneltme ilişkisini korur."},"facet_ids":["F003"],"text":"geri döndürmek","usage_role":"contextual"},{"applicability":"İnsanları su başından uzaklaştırıp geri götüren yolun niteliğini açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolun su başından ayrılışa aracılık etmesi anlamını korur."},"facet_ids":["F004"],"text":"su başından dönüş yolu","usage_role":"explanatory"}],"definition":"Bir su başına, ülkeye ya da bir işe vardıktan veya girdikten sonra oradan ayrılıp geri yönelme hareketidir. Başkasını bu dönüşe yöneltme ve insanları su başından uzaklaştıran yol, bu çekirdeğe bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce varılan bir yerden veya girilen bir durumdan ayrılıp geri yönelmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Su içmek için su başına gelen insan veya hayvanların oradan ayrılması temel örnektir."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, bir başkasını geri çevirip onun dönmesini sağlama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Belirli söz öbeğinde yol, insanlarını su başından uzaklaştırıp geri götüren güzergah olarak nitelenir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Önceden varılmış bir yer ya da girilmiş bir durum bulunmayan her türlü ayrılmayı kapsama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir yerden uzaklaşma hareketini genel düzeyde korur."},"text":"ayrılma"}],"identity_rationale":"Kaynak ifadesi, su başı, ülke veya başka bir işe varıştan sonra oradan ayrılmayı temel hareket olarak verir; bir başkasını geri çevirme ve insanlarını su başından uzaklaştıran yol da bu hareketin ettirgen ve yapıya bağlı uzanımlarıdır. Geçici çerçeve bu aşamaları birbirine karıştırmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir yerden ya da durumdan ayrılış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"su başından, geldikten sonra ayrılmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"geri döndürmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"su başından dönüşü sağlayan yol"}],"lexicalization_note":"Ayrılıp dönme olayı temel alınır; başkasını döndürme yalnız ettirgen biçime, su başından uzaklaştıran yol ise verilen söz öbeğine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar önceki varış, iç-dış geçiş, geri yönelme ve yolculuk koşulları bakımından değerlendirildi; bu dört aday dalın hareket sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında varıştan sonraki dönüş kurucudur; komşu dalda genel gidiş veya hızlı uzaklaşma yeterlidir.","focus_only":"Odak dalı önceden varılan yerden ayrılıp geri yönelme aşamasını gerektirir.","gloss":"ayrılıp gitme","neighbor_only":"Komşu dal yeryüzünde gitmeyi ve bir kişiden hızla uzaklaşmayı önceki varış koşulu olmadan kapsar.","neighbor_ref":"root_000325/B007","relation_type":"near_synonym","shared_zone":"İki dal da bir yerden uzaklaşma ve orayı geride bırakma hareketini anlatır."},{"boundary_match":"partial","distinction":"Çıkış, iç-dış sınırının aşılmasına dayanır; odak ise önceki varış ve ardından dönüş düzenini gerektirir.","focus_only":"Odak dalı bir yere geldikten sonra oradan ayrılıp geri yönelmeyi içerir.","gloss":"dışarı çıkma","neighbor_only":"Komşu dal yalnız bir şeyin içinden dışarı çıkmayı bildirir.","neighbor_ref":"root_001158/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir başlangıç alanını geride bırakma hareketinde örtüşür."},{"boundary_match":"partial","distinction":"Odak, varılan yerden çıkış anını adlandırır; komşu ise geri gelişin kendisini ve daha geniş gidip gelme olaylarını kapsar.","focus_only":"Odak dalı varılan kaynaktan ayrılma evresini merkeze alır.","gloss":"geri dönme","neighbor_only":"Komşu dal geri gelme, yeniden dönme ve bazı şeylerin gidip gelmesi gibi yinelenen hareketleri kapsar.","neighbor_ref":"root_000618/B004","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı geriye yönelme ve önceki konumla yeniden ilişki kurmadır."},{"boundary_match":"thematic_only","distinction":"Odak önceki varışın ardından dönüşü, komşu ise yeni bir hedefe yönelen yolculuğu anlatır; ortaklık olay alanıyla sınırlıdır.","focus_only":"Odak dalı varıştan sonra kaynaktan veya yerden ayrılma aşamasını belirtir.","gloss":"yola çıkma","neighbor_only":"Komşu dal bir hedefe doğru yolculuğa çıkmayı ve seyahat etmeyi belirtir.","neighbor_ref":"root_000551/B001","relation_type":"thematic","shared_zone":"Her ikisi de bir yerden ayrılmayı içeren hareket senaryosunda yer alır."}],"source_phrase_ar":"صدر عن الماء وصدر عن البلاد (maqayis;sihah)؛ الصدر الانصراف عن الورد وعن كل أمر (ayn;tahdhib)؛ صدرت الإبل عن الماء (mufradat)؛ أصدرته فصدر أي رجعته فرجع (sihah)؛ طريق صادر يصدر بأهله عن الماء (ayn;sihah;tahdhib)","source_summary":"Kaynakların ortak anlamı, varılan su başından, ülkeden veya girilen bir işten ayrılıp geri yönelmektir; ettirgen dönüş ve bu ayrılışı sağlayan yol aynı hareket şemasına bağlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الانصراف عن الماء أو البلاد أو كل أمر بعد وروده، والإصدار بمعنى الإرجاع، والطريق الصادر بأهله","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء بمعنى أوله؛ المصدر النحوي"},"support_links":[]},{"boundary":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_kind":"bare","branch_ref":"root_000849/B004","candidate_links":[{"candidate_id":"cand_857f6a79f82947db1dc6","lane":"micro"},{"candidate_id":"cand_d441fa0e383ad2cd97ae","lane":"micro"},{"candidate_id":"cand_27669bb52d6e9995c065","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"eylem türetme temeli; çıkış yeri veya zamanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın dil bilgisel çekirdeğiyle yer ve zaman uzanımını birlikte göstermek gereken sözlük açıklamasında kullanılır.","boundary_detail":"Dil bilgisel temel ana kullanımdır; çıkış yeri ve çıkış zamanı, ortak çıkma ilişkisine dayanan ayrı adlandırma seçenekleridir.","branch_image_ar":"الأصل الذي تصدر عنه الأفعال","concept_gloss":"eylem türetme temeli; çıkış yeri veya zamanı","contextual_glosses":[{"applicability":"Sözcük yapısında çekimli eylemlerin dayandırıldığı temel ad biçimi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel biçim ile ondan türeyen eylem biçimleri arasındaki yönü korur."},"facet_ids":["F001"],"text":"eylemlerin türediği temel biçim","usage_role":"explanatory"},{"applicability":"Bir çıkma olayının gerçekleştiği mekanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait yer olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış yeri","usage_role":"contextual"},{"applicability":"Bir çıkma olayının gerçekleştiği zamanın adı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adlandırılan unsurun çıkma olayına ait zaman olması bilgisini korur."},"facet_ids":["F002"],"text":"çıkış zamanı","usage_role":"contextual"}],"definition":"Dil bilgisinde, çekimli eylem biçimlerinin kendisinden çıktığı kabul edilen temel sözcük biçimidir. Aynı ad, çıkma eyleminin gerçekleştiği yeri veya zamanı da gösterebilir; bu ikinci kullanım dil bilgisel temel ile özdeş değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli eylem biçimlerinin türediği kabul edilen temel sözcük biçimini belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı ad, çıkma olayının gerçekleştiği yer veya zamanı bildiren bir ad olarak da açıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Su kaynağı, bilgi belgesi ve genel köken gibi bu dala özgü olmayan çok sayıda anlamı kapsama ekler.","collision":"Genel köken ve maden ya da pınar komşularıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Başka bir şeyin kendisinden çıkması ya da doğması ilişkisini korur."},"text":"kaynak"}],"identity_rationale":"Kaynak ifadesi, çekimli eylemlerin kendisinden çıktığı kabul edilen temel sözcük biçimi ile çıkmanın gerçekleştiği yer ve zamanı aynı ad altında anar. Geçici çerçeve kullanılabilir, ancak dil bilgisel türetme temeli ile olayın yeri veya zamanı tek bir kavrammış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"eylemlerin türediği temel sözcük biçimi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"çıkış yeri ya da zamanı"}],"lexicalization_note":"Dal, ad biçiminin çıplak anlam alanını tanımlar; dil bilgisel temel ile yer ve zaman anlamları ayrılır ve başka söz öbeklerinden kapsam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar genel köken, somut kaynak, dil bilgisel işlev ve gerçek ayrılış bakımından değerlendirildi; seçilen dört karşılaştırma iki alt kullanımın sınırını doğrudan aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak teknik bir sözcük biçimine ve çıkış olayının yer-zaman adlarına bağlıdır; komşu ise alan sınırlaması olmayan genel köken kavramıdır.","focus_only":"Odak dalı dil bilgisel temel biçimi ve çıkışın yer ya da zamanını adlandırır.","gloss":"köken","neighbor_only":"Komşu dal herhangi bir şeyin, kişinin veya olayın genel kökenini kapsar.","neighbor_ref":"root_000031/B002","relation_type":"near_synonym","shared_zone":"Her iki dal başka biçimlerin veya olayların kendisinden çıktığı başlangıç noktasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dil bilgisel ve olay yapısına bağlı bir adlandırmadır; komşu somut üretim veya akış kaynağını temel alır.","focus_only":"Odak dalı dil bilgisel türetme temelini ve olayın çıkış yeri ya da zamanını kapsar.","gloss":"çıktığı yer","neighbor_only":"Komşu dal maddelerin çıkarıldığı maden veya bir şeyin doğduğu somut pınar ve menba alanını kapsar.","neighbor_ref":"root_001475/B008","relation_type":"near_neighbor","shared_zone":"İki dal bir şeyin ortaya çıktığı başlangıç yerini gösterme alanında örtüşür."},{"boundary_match":"field_only","distinction":"Biri türetme yönündeki temel biçimdir, öteki cümle içindeki durum işaretidir; çekirdek işlemleri farklıdır.","focus_only":"Odak dalı eylem biçimlerinin dayandırıldığı temel sözcük biçimini belirtir.","gloss":"dil bilgisel biçim","neighbor_only":"Komşu dal sözcüğün cümledeki durumunu gösteren belirli bir dil bilgisi işaretlemesini belirtir.","neighbor_ref":"root_000582/B012","relation_type":"same_field","shared_zone":"Her iki dal sözcüklerin dil bilgisel çözümlemesi alanında kullanılır."},{"boundary_match":"partial","distinction":"Odak bir temel biçim veya yer-zaman adıdır; komşu ise katılımcının gerçekleştirdiği hareketin kendisidir.","focus_only":"Odak dalı çıkmanın dil bilgisel temelini ve olayın yer ya da zaman adını belirtir.","gloss":"çıkış ve ayrılış","neighbor_only":"Komşu dal varılan yerden gerçekten ayrılıp geri yönelme hareketini belirtir.","neighbor_ref":"root_000849/B003","relation_type":"near_neighbor","shared_zone":"İki dal çıkma ve bir başlangıç noktasından uzaklaşma düşüncesini paylaşır."}],"source_phrase_ar":"المصدر أصل الكلمة الذي تصدر عنه الأفعال (ayn;tahdhib)؛ مصادر الأفعال (sihah)؛ المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه (mufradat)","source_summary":"Toplu kaynak anlatımı iki bağlı fakat ayrı kullanımı içerir: eylem biçimlerinin türediği dil bilgisel temel ve bir çıkma olayının yeri ya da zamanı. Ortak bağ, başka bir biçim veya olayın buradan çıkması düşüncesidir.","sources":["AY","SI","TA","MU"],"what_is_ar":"المصدر بوصفه أصل الكلمة أو الفعل، وما يلحق به من اسم الموضع والزمان في الصدور","what_is_not_ar":"الصدر الجارحة؛ صدر الشيء أوله؛ الصدور الحسي عن الماء"},"support_links":["sup_285ae75f1c269bd3cbb0","sup_47294475791d784a05b0","sup_4cfc6f76c26f3e2cf3f4"]},{"boundary":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_kind":"non_bare","branch_ref":"root_000849/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"para ödeme ve güvence yükümlülüğü koyma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yapı içinde bir kişiye ödeyeceği tutar için sorumluluk yüklendiğini açıklamak üzere kullanılır.","boundary_detail":"Anlam belirli yapılara bağlı bir ödeme ve güvence yükümlülüğüdür; malın zorla alınması tek başına bu dalı karşılamaz.","branch_image_ar":"المصادرة على مال","concept_gloss":"para ödeme ve güvence yükümlülüğü koyma","contextual_glosses":[{"applicability":"Bir kişiye belirlenmiş para tutarını ödeme ve güvenceye alma sorumluluğu verildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükümlü kılınan kişiyi, belirli tutarı ve ödeme sorumluluğunu korur."},"facet_ids":["F001"],"text":"belli bir tutarı ödemekle yükümlü kılmak","usage_role":"explanatory"},{"applicability":"Tarafların güvence altına alınacak para tutarını belirleyip ayrılması veya anlaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli para tutarı üzerinde anlaşma ve sorumluluğu üstlenme ilişkisini korur."},"facet_ids":["F002"],"text":"ödeme tutarı üzerinde hesaplaşmak","usage_role":"contextual"}],"definition":"Belirli yapılarda, bir kimseyi belirli bir parayı ödemek ve bu tutardan sorumlu olmakla yükümlü kılmayı; kimi bağlamlarda da bu yükümlülük üzerinde hesaplaşmayı anlatır. Doğrudan malına el koyma anlamı zorunlu değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye belirli bir para tutarını ödeme ve o tutarın güvencesini üstlenme yükümlülüğü konur."},{"facet_id":"F002","role":"source_variant","statement":"Yapı, kimi açıklamada tarafların güvence altındaki para tutarı üzerinde hesaplaşması veya anlaşması olarak yorumlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Malın doğrudan alınması ve mülkiyetin kişiden çıkarılması sonucunu ekler.","collision":"Çağdaş zorla alma anlamıyla karışarak kaynak sınırını değiştirir.","fit":"displacement","loses":"Belirli tutarı ödeme ve bu tutardan sorumlu olma ilişkisini kaybeder.","preserves":"Bir kişinin mal varlığına yönelen zorlayıcı mali işlem çağrışımını korur."},"text":"malına el koymak"}],"identity_rationale":"Kaynak ifadesi modern anlamdaki doğrudan mala el koymayı zorunlu kılmaz; belirli yapılarda bir kimseye ödeyeceği ve güvencesini üstleneceği bir tutar yüklenmesini, kimi açıklamada da bu tutar üzerinde hesaplaşmayı anlatır. Bu nedenle dal korunabilir, fakat geçici el koyma çerçevesi mali yükümlülük olarak düzeltilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini belli bir parayı ödemek ve güvence altına almakla yükümlü kılmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendisine para ödeme ve güvence yükümlülüğü konmak"}],"lexicalization_note":"Anlam yalnız verilen kişi ve para yapılarında geçerlidir; çıplak köke genel el koyma, vergi alma veya ödeme anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar yükümlülük kurma, hakkı ödeme, alacak isteme ve belirli mali ödeme türleri bakımından değerlendirildi; seçilen dört aday işlem ile sonuç arasındaki sınırı gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak sorumluluğun kişiye yüklenmesini, komşu ise mevcut sorumluluğun ödeme yoluyla yerine getirilmesini temel alır.","focus_only":"Odak dalı belirli tutar için ödeme ve güvence yükümlülüğünü kurar.","gloss":"ödeme yükümlülüğü ve ödeme","neighbor_only":"Komşu dal önceden var olan borç, vergi veya emanet hakkının fiilen yerine getirilmesini anlatır.","neighbor_ref":"root_000021/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir hakkın veya para borcunun ödenmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Odak yükümlülüğün kurulmasına, komşu ise kurulmuş hakkın talep ve tahsiline dayanır.","focus_only":"Odak dalı kişiyi belirli bir tutardan sorumlu kılma işlemini belirtir.","gloss":"mali sorumluluk ve alacak isteme","neighbor_only":"Komşu dal hak sahibinin mevcut alacağını sürekli istemesi ve tahsil etmeye çalışmasını belirtir.","neighbor_ref":"root_000943/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin başkasından para veya hak istemesiyle ilişkili olabilir."},{"boundary_match":"field_only","distinction":"Odak kişi üzerinde kurulan sorumluluktur; komşu ise verilen veya çıkarılan mali değerin türünü adlandırır.","focus_only":"Odak dalı kişiye ödeme ve güvence sorumluluğu yükleyen işlemi anlatır.","gloss":"mali yükümlülük","neighbor_only":"Komşu dal belirli bir yolla çıkarılan para, ürün, vergi veya payın kendisini anlatır.","neighbor_ref":"root_000400/B003","relation_type":"same_field","shared_zone":"İki dal düzenlenmiş bir mali ödeme ve belirlenmiş tutar alanını paylaşır."},{"boundary_match":"field_only","distinction":"Odak bir yükümlü kılma işlemi ve güvencedir; komşu ise belirli hukuki bağlamdaki ödeme türüdür.","focus_only":"Odak dalı herhangi bir kişiye belirli yapı içinde yüklenen para sorumluluğunu belirtir.","gloss":"yüklenen mali ödeme","neighbor_only":"Komşu dal belirli bir topluluğa hukuki statüsü nedeniyle konan özel mali ödemeyi belirtir.","neighbor_ref":"root_000244/B004","relation_type":"same_field","shared_zone":"Her iki dal bir kişinin ya da topluluğun ödemek zorunda bırakıldığı para alanındadır."}],"source_phrase_ar":"صادره على كذا (sihah)؛ صودر فلان العامل على مال يؤديه أي فورق على مال ضمنه (tahdhib)","source_summary":"Toplu kaynak anlatımı, belirli bir para için ödeme ve güvence sorumluluğu kurulmasında birleşir; anlatım bu sorumluluğun yüklenmesi ile tarafların tutar üzerinde hesaplaşması arasında değişir.","sources":["SI","TA"],"what_is_ar":"مصادرة العامل أو غيره على مال يؤديه ويضمنه","what_is_not_ar":"الصدر الجارحة؛ الصدور عن الماء؛ صدر الشيء أوله"},"support_links":[]},{"boundary":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_kind":"bare","branch_ref":"root_000849/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","surface_ar":"صَدْرَ"}],"gloss":"bir şeyin bölümü ya da kümesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}}],"root_ar":"ص د ر","root_id":"root_000849","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütünden ayrılan parçanın veya onun içindeki grubun oranı ve konumu belirtilmediğinde kullanılır.","boundary_detail":"Dal, bütünün herhangi bir bölümünü veya kümesini belirtir; ilk bölüm, beden parçası ya da sabit oran koşulu taşımaz.","branch_image_ar":"الطائفة من الشيء","concept_gloss":"bir şeyin bölümü ya da kümesi","contextual_glosses":[{"applicability":"Bir bütünün oranı belirtilmeyen kısmından söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütüne bağlı ve oranı belirtilmeyen parça anlamını korur."},"facet_ids":["F001"],"text":"bir bölüm","usage_role":"general"},{"applicability":"Bir şeyin içinden birlikte ele alınan topluluk veya grup kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bütün içindeki öğelerin birlikte bir grup oluşturması anlamını korur."},"facet_ids":["F001"],"text":"bir küme","usage_role":"contextual"}],"definition":"Bir bütünün içinden ayrılan veya onun kapsamında düşünülen bölüm ya da kümedir. Bölümün yeri, büyüklüğü ve oranı anlam tarafından belirlenmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin belirli olmayan bölümünü veya onun içindeki bir kümeyi belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bütünün dokuz eşit parçaya ayrılması koşulunu ekler.","collision":"Belirli kesir bildiren komşu dalla karışır.","fit":"narrowing","loses":"Bölümün herhangi bir büyüklükte veya küme niteliğinde olabilmesi kapsamını kaybeder.","preserves":"Bir bütünün parçası olma özelliğini korur."},"text":"dokuzda bir"}],"identity_rationale":"Kaynak ifadesi, biçimi doğrudan bir şeyin bölümü veya ondan ayrılan topluluk anlamında tanımlar. Geçici çerçeve bu kısa ve bağımsız anlamı ne bütünün başı anlamıyla ne de belirli bir kesirle karıştırır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir şeyin bölümü ya da kümesi"}],"lexicalization_note":"Çıplak biçimin bölüm veya küme anlamı tanımlanır; bölme eylemi, belirli kesirler ve başka yapılara bağlı özel anlamlar kapsama alınmaz.","neighbor_coverage_note":"Bütün adaylar genel parça, özel organ veya pay, sabit kesir ve tam bütün sınırları bakımından değerlendirildi; yayımlanan üç karşılaştırma dalın oranı belirsiz bölüm anlamını yeterince ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ad olarak bölüm anlamında büyük ölçüde örtüşürler; komşunun bölme işlemi ve bütünün kuruluşuna ilişkin kapsamı tam eşanlamlılığı engeller.","focus_only":"Odak dalı yalnız bölümün veya kümenin adını verir ve bir işlem gerektirmez.","gloss":"bölüm veya parça","neighbor_only":"Komşu dal bölme işlemini ve parçaların bütünü kuran yapısal öğeler olmasını da kapsar.","neighbor_ref":"root_000241/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün bölümü veya içindeki topluluk anlamında kullanılabilir."},{"boundary_match":"partial","distinction":"Odak belirlenmemiş bölüm ya da kümedir; komşu organ, et parçası ve pay gibi özelleşmiş parça türlerine uzanır.","focus_only":"Odak dalı cansız veya soyut bir bütün içindeki kümeyi de genel olarak kapsar.","gloss":"parça","neighbor_only":"Komşu dal beden organı, et parçası ve kişiye düşen pay gibi daha özel bölüm türlerini kapsar.","neighbor_ref":"root_000024/B003","relation_type":"near_synonym","shared_zone":"İki dal bir bütünden ayrılan bölüm anlamında birbirine yaklaşır."},{"boundary_match":"opposed","distinction":"Odak kapsamı bütünün bir kesimiyle sınırlar; komşu aynı varlığın eksiksiz tamamını kapsar.","focus_only":"Odak dalı bütünün içindeki yalnız bir bölüm veya kümeyi belirtir.","gloss":"bölüm ve bütün","neighbor_only":"Komşu dal hiçbir bölüm dışarıda kalmadan şeyin tamamını belirtir.","neighbor_ref":"root_000030/B005","relation_type":"antonym","shared_zone":"İki dal aynı şeyin ne kadarının kapsandığını belirleyen parça-bütün eksenindedir."}],"source_phrase_ar":"الصدر الطائفة من الشيء (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu bölüm veya küme anlamı, sağlanan kanıtta tek bir sözlük tarafından kaydedilmiştir."}],"source_summary":"Dal, bir bütünün belirli olmayan bölümü veya onun içindeki bir küme anlamını taşır; konum ve oran bakımından ek koşul bildirmez.","sources":["SI"],"what_is_ar":"الصدر بمعنى طائفة من الشيء","what_is_not_ar":"صدر الشيء بمعنى أوله؛ الصدر الجارحة؛ الصدور عن الماء"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["94:1:1"],"branch_refs":[],"candidate_id":"cand_fd7f520600759c7dbf01","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:1:fused-particle-jussive-control","source_type":"word_analysis","support_ids":["sup_7274bfb129c9519d358a","sup_a41021222809d7bc9941"],"title":"fused particle controls the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:1","qac_refs":["94:1:1:1","94:1:1:2"],"status":"accepted"}},{"anchor_refs":["94:1:1"],"branch_refs":[],"candidate_id":"cand_5baf3b8803196607bf13","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:1:negative-interrogative-recognition","source_type":"word_analysis","support_ids":["sup_7274bfb129c9519d358a","sup_c9850c556a5ea81f1c4b"],"title":"negative question as compelled recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:1","qac_refs":["94:1:1:1","94:1:1:2"],"status":"accepted"}},{"anchor_refs":["94:1:1"],"branch_refs":[],"candidate_id":"cand_d6132653d8518a815a45","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:1:surah-opening-sequence","source_type":"word_analysis","support_ids":["sup_7274bfb129c9519d358a","sup_bdf9f73bb7470c528de7"],"title":"surah-opening sequence stages the favor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:1","qac_refs":["94:1:1:1","94:1:1:2"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_23c71c831b0b2750e328","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:audible-throat-release","source_type":"word_analysis","support_ids":["sup_5984a4fb08c6126a38a1","sup_7054149fd2c3499dce40"],"title":"throat sound echoes opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_dac5073a0f00de7b64ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:form-one-holistic-opening","source_type":"word_analysis","support_ids":["sup_0cefa2c2c44eeca7a5e1","sup_5984a4fb08c6126a38a1"],"title":"Form I holistic opening, not repeated dissection","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_0eb23d5076f06167c0c8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:implicit-divine-agent-and-open-purpose","source_type":"word_analysis","support_ids":["sup_547e9311e5a04f2870b5","sup_5984a4fb08c6126a38a1"],"title":"divine agency with open enabled capacity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_fe3c45871b95511cfd9e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:lam-governed-jussive","source_type":"word_analysis","support_ids":["sup_5984a4fb08c6126a38a1","sup_c25d56279f144b04919d"],"title":"lam-governed jussive verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_46d247b201d101ed9cc3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:opened-chest-semantic-convergence","source_type":"word_analysis","support_ids":["sup_5984a4fb08c6126a38a1","sup_94da82b36901f1ea228f"],"title":"opening, clarification, and receptivity converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_17215e45f2a549574c75","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:root-pair-formula","source_type":"word_analysis","support_ids":["sup_0a0034f7b41393bd3b27","sup_5984a4fb08c6126a38a1"],"title":"formulaic pairing with the chest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:2","qac_refs":["94:1:2:1"],"status":"accepted"}},{"anchor_refs":["94:1:3"],"branch_refs":[],"candidate_id":"cand_41f606d5a5fded51610f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:3:benefactive-recipient-not-patient","source_type":"word_analysis","support_ids":["sup_f33f819a80ab2a699854","sup_fb693d4930290942ef5b"],"title":"beneficiary before patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:3","qac_refs":["94:1:3:1","94:1:3:2"],"status":"accepted"}},{"anchor_refs":["94:1:3"],"branch_refs":[],"candidate_id":"cand_ee33dbf10d24c0627629","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:3:fused-address-benefit","source_type":"word_analysis","support_ids":["sup_4c8d1cf21241709f66b7","sup_fb693d4930290942ef5b"],"title":"address and benefit fused","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:3","qac_refs":["94:1:3:1","94:1:3:2"],"status":"accepted"}},{"anchor_refs":["94:1:3"],"branch_refs":[],"candidate_id":"cand_b150323bee7002c07771","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:1:3:interposed-benefactive-focus","source_type":"word_analysis","support_ids":["sup_3f6f4790bc501019240f","sup_fb693d4930290942ef5b"],"title":"interposed benefactive focus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:3","qac_refs":["94:1:3:1","94:1:3:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_de2f9fd6ff25165956d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:accusative-direct-object","source_type":"word_analysis","support_ids":["sup_0a1f72e13d0021b7f664","sup_4eb299ae9bf0697a1627"],"title":"singular direct object opened","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_5218fbcf4fb14ccc5da9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:bodily-inner-cognition","source_type":"word_analysis","support_ids":["sup_4eb299ae9bf0697a1627","sup_8ca2a6b36bb017dca515"],"title":"body term as inner faculty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_b070299d076f3711f9aa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:closing-transformation-site","source_type":"word_analysis","support_ids":["sup_4eb299ae9bf0697a1627","sup_b6040a8ad4113fb818c1"],"title":"closing word concentrates transformation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_c30a7e1cd5060cafc93c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:formulaic-sharh-sadr-echo","source_type":"word_analysis","support_ids":["sup_4eb299ae9bf0697a1627","sup_96a6e8745bc88b211777"],"title":"formulaic chest-opening echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_4ec9bc3d520f99951712","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:possessed-personal-locus","source_type":"word_analysis","support_ids":["sup_26cc77dc397d594031a2","sup_4eb299ae9bf0697a1627"],"title":"possessed object personalizes the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_b2edca046390ad757ffe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:source-and-front-origin","source_type":"word_analysis","support_ids":["sup_4eb299ae9bf0697a1627","sup_ac54246b32f2e19f192d"],"title":"opened patient becomes source-point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:1:4","qac_refs":["94:1:4:1","94:1:4:2"],"status":"accepted"}},{"anchor_refs":["94:1:2"],"branch_refs":[],"candidate_id":"cand_9a324016890157f2a66e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000784"],"scope":"focus_ayah","source_local_id":"94:1:2:1","source_type":"qac_morpheme","support_ids":["sup_68efa5d1da95ab73e5a0"],"title":"QAC root occurrence: ش ر ح","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:1:4"],"branch_refs":[],"candidate_id":"cand_c3ff539b71ce3bac27f8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000849"],"scope":"focus_ayah","source_local_id":"94:1:4:1","source_type":"qac_morpheme","support_ids":["sup_95bec948040107d81271"],"title":"QAC root occurrence: ص د ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:1","branch_refs":["root_000784/B001","root_000849/B001","root_000849/B004"],"candidate_id":"cand_857f6a79f82947db1dc6","commentary_obligation":"review","hft_ref":"hft_ad26c09bf4da9c29d164","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_clarified_inner_source","source_type":"hft","support_ids":["sup_285ae75f1c269bd3cbb0"],"title":"baseline_clarified_inner_source","trust":"legacy_unbound"},{"anchor_refs":["94:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:1","branch_refs":["root_000784/B002","root_000849/B001"],"candidate_id":"cand_d91c42acfd3914df5c51","commentary_obligation":"review","hft_ref":"hft_2d32809e0164400452e7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_material_unfolding","source_type":"hft","support_ids":["sup_07120fc2461a63f214df"],"title":"baseline_material_unfolding","trust":"legacy_unbound"},{"anchor_refs":["94:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:1","branch_refs":["root_000784/B006","root_000849/B004"],"candidate_id":"cand_d441fa0e383ad2cd97ae","commentary_obligation":"review","hft_ref":"hft_cbd981ba5fe5f5f9a15e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_guarded_capacity","source_type":"hft","support_ids":["sup_4cfc6f76c26f3e2cf3f4"],"title":"baseline_guarded_capacity","trust":"legacy_unbound"},{"anchor_refs":["94:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:1","branch_refs":["root_000784/B005","root_000849/B004"],"candidate_id":"cand_27669bb52d6e9995c065","commentary_obligation":"review","hft_ref":"hft_d1419366d87cf22a793b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_expanded_desire","source_type":"hft","support_ids":["sup_47294475791d784a05b0"],"title":"baseline_expanded_desire","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"94:1:1:1","qac_word_ref":"94:1:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"94:1:1:2","qac_word_ref":"94:1:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","root_ar":"ش ر ح","surface_ar":"نَشْرَحْ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"94:1:3:1","qac_word_ref":"94:1:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"94:1:3:2","qac_word_ref":"94:1:3","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","root_ar":"ص د ر","surface_ar":"صَدْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:1:4:2","qac_word_ref":"94:1:4","root_ar":"","surface_ar":"كَ"}],"word_analysis_qac_refs":[["94:1:1:1","94:1:1:2"],["94:1:2:1"],["94:1:3:1","94:1:3:2"],["94:1:4:1","94:1:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["94:1:1","94:1:2","94:1:3","94:1:4"]},"focus_surface_evidence":{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|A:INTG+","morpheme_role":"PREFIX","pos":"INTG","qac_ref":"94:1:1:1","qac_word_ref":"94:1:1","root_ar":"","surface_ar":"أَ"},{"lemma_ar":"لَم","morph_features":"STEM|POS:NEG|LEM:lam","morpheme_role":"STEM","pos":"NEG","qac_ref":"94:1:1:2","qac_word_ref":"94:1:1","root_ar":"","surface_ar":"لَمْ"},{"lemma_ar":"شَرَحَ","morph_features":"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS","morpheme_role":"STEM","pos":"V","qac_ref":"94:1:2:1","qac_word_ref":"94:1:2","root_ar":"ش ر ح","surface_ar":"نَشْرَحْ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"94:1:3:1","qac_word_ref":"94:1:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"94:1:3:2","qac_word_ref":"94:1:3","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"صَدْر","morph_features":"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:1:4:1","qac_word_ref":"94:1:4","root_ar":"ص د ر","surface_ar":"صَدْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:1:4:2","qac_word_ref":"94:1:4","root_ar":"","surface_ar":"كَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["94:1:1:1","94:1:1:2"],["94:1:2:1"],["94:1:3:1","94:1:3:2"],["94:1:4:1","94:1:4:2"]],"word_analysis_refs":["94:1:1","94:1:2","94:1:3","94:1:4"],"word_rows":[{"analysis_record_ref":"94:1:1","analytic_gloss_range_en":"fused interrogative plus lam-negation that frames the following jussive predicate as a recognition-demand, not a flat denial","analytic_root_gloss_range_en":null,"qac_refs":["94:1:1:1","94:1:1:2"],"root":{},"surface":{"arabic":"أَلَمْ","transliteration":"ʾa-lam"}},{"analysis_record_ref":"94:1:2","analytic_gloss_range_en":"lam-governed Form I opening or widening of the addressee's chest, carrying physical opening, clarification, receptivity, and relief while excluding unrelated root branches","analytic_root_gloss_range_en":"broad root range includes clarifying, cutting or spreading, opening the chest to receive good, euphemistic sexual uses, expansive inclination, and guarding; the local verb selects the chest-opening and clarification field, with the cutting-open image only as constrained pressure","qac_refs":["94:1:2:1"],"root":{"arabic":"ش ر ح","transliteration":"sh-r-ḥ"},"surface":{"arabic":"نَشْرَحْ","transliteration":"nashraḥ"}},{"analysis_record_ref":"94:1:3","analytic_gloss_range_en":"benefactive prepositional phrase with a second-person masculine singular suffix, marking the addressee as recipient-beneficiary before the direct object appears","analytic_root_gloss_range_en":null,"qac_refs":["94:1:3:1","94:1:3:2"],"root":{},"surface":{"arabic":"لَكَ","transliteration":"laka"}},{"analysis_record_ref":"94:1:4","analytic_gloss_range_en":"the addressee's singular possessed chest as direct object: a bodily front, inner faculty, and source-like locus opened by the verb","analytic_root_gloss_range_en":"broad root range includes chest or bodily front, foremost part, departing from water, source from which forms issue, liability settlement, and portion; the local noun selects chest/front and source-like inner locus, not the unrelated financial or departure branches","qac_refs":["94:1:4:1","94:1:4:2"],"root":{"arabic":"ص د ر","transliteration":"ṣ-d-r"},"surface":{"arabic":"صَدْرَكَ","transliteration":"ṣadraka"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["94:1"],"branch_refs":["root_000784/B001","root_000849/B001","root_000849/B004"],"candidate_id":"cand_857f6a79f82947db1dc6","evidence_scope":"focus_ayah","hft_ref":"hft_ad26c09bf4da9c29d164","item_id":"baseline_clarified_inner_source","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_clarified_inner_source","support_id":"sup_285ae75f1c269bd3cbb0"},{"anchor_refs":["94:1"],"branch_refs":["root_000784/B002","root_000849/B001"],"candidate_id":"cand_d91c42acfd3914df5c51","evidence_scope":"focus_ayah","hft_ref":"hft_2d32809e0164400452e7","item_id":"baseline_material_unfolding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_material_unfolding","support_id":"sup_07120fc2461a63f214df"},{"anchor_refs":["94:1"],"branch_refs":["root_000784/B006","root_000849/B004"],"candidate_id":"cand_d441fa0e383ad2cd97ae","evidence_scope":"focus_ayah","hft_ref":"hft_cbd981ba5fe5f5f9a15e","item_id":"baseline_guarded_capacity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_guarded_capacity","support_id":"sup_4cfc6f76c26f3e2cf3f4"},{"anchor_refs":["94:1"],"branch_refs":["root_000784/B005","root_000849/B004"],"candidate_id":"cand_27669bb52d6e9995c065","evidence_scope":"focus_ayah","hft_ref":"hft_d1419366d87cf22a793b","item_id":"baseline_expanded_desire","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_expanded_desire","support_id":"sup_47294475791d784a05b0"}],"diagnostics":[],"lane_counts":{"global":9,"macro":9,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"94:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ز ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001643","furuq_root_norm":"و ز ر","furuq_source_root_norm":"و ز ر","is_dominant":true,"target_occurrences":24,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000654","furuq_root_norm":"ز و ر","furuq_source_root_norm":"ز و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"94:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"94:1","lane":"micro","linguistic_source_ref":"94:1","surface_ref":"94:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"94:1","target_tokens":[["Senin",["94:1:3","94:1:4"]],["için",["94:1:3"]],["göğsünü",["94:1:4"]],["açmadık",["94:1:1","94:1:2"]],["mı",["94:1:1"]]],"text":"Senin için göğsünü açmadık mı?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s094-p01-001-008","label":"Whole surah","number":1,"refs":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:root-pair-formula","source_type":"word_analysis","support_id":"sup_0a0034f7b41393bd3b27","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic pairing with the chest\",\"reader_payoff\":\"The reader notices that this opening verb is bound to the chest-object formula across the Quran, including request and guidance contexts.\",\"reason\":\"The CRITICAL rows give concrete comparanda at 6:125, 20:25, 39:22, and 16:106, and the contextual profile keeps {{ar:ش ر ح}} ({{tr:sh-r-ḥ}}) low-occurrence with {{ar:لـ}} ({{tr:li-}}) and explicit object frames.\",\"representative_source_ids\":[\"QI-43311aef\",\"MI-126042c4\",\"ME-7f31dade\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:accusative-direct-object","source_type":"word_analysis","support_id":"sup_0a1f72e13d0021b7f664","text":"{\"blocking_evidence\":null,\"headline\":\"singular direct object opened\",\"reader_payoff\":\"The reader notices that the chest is the acted-upon object, not the agent, location, or a distributed plural field.\",\"reason\":\"QAC marks {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) as accusative, and attachment evidence makes it the explicit direct object of {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}).\",\"representative_source_ids\":[\"QG-d4d9f4e1\",\"MG-543ce9bc\",\"QF-30440cea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:form-one-holistic-opening","source_type":"word_analysis","support_id":"sup_0cefa2c2c44eeca7a5e1","text":"{\"blocking_evidence\":null,\"headline\":\"Form I holistic opening, not repeated dissection\",\"reader_payoff\":\"The reader notices that the selected stem presents a single active divine opening rather than iterative clinical dissection or reflexive self-opening.\",\"reason\":\"The local form is Form I and active; V4 shows wider family material, but formal matching alone does not activate other stems as local senses.\",\"representative_source_ids\":[\"QF-9dfe3695\",\"QF-cd9f01d7\",\"MF-19847074\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:possessed-personal-locus","source_type":"word_analysis","support_id":"sup_26cc77dc397d594031a2","text":"{\"blocking_evidence\":null,\"headline\":\"possessed object personalizes the opening\",\"reader_payoff\":\"The reader notices that the opened object is not a generic chest; it is the addressee's own singular inner locus.\",\"reason\":\"The noun is parsed with a second-person possessive suffix, and cross-reference evidence ties that suffix to the same single addressee marked by {{ar:لَكَ}} ({{tr:laka}}).\",\"representative_source_ids\":[\"QG-0e6f98de\",\"QG-48e7c317\",\"QF-eabcaef5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:3:interposed-benefactive-focus","source_type":"word_analysis","support_id":"sup_3f6f4790bc501019240f","text":"{\"blocking_evidence\":null,\"headline\":\"interposed benefactive focus\",\"reader_payoff\":\"The reader notices that the clause routes attention to the recipient before naming the opened object.\",\"reason\":\"The local word order is {{ar:نَشْرَحْ لَكَ صَدْرَكَ}} ({{tr:nashraḥ laka ṣadraka}}), with the benefactive prepositional phrase placed between verb and direct object.\",\"representative_source_ids\":[\"QT-ea0e4f05\",\"MT-05c37ba6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:3:fused-address-benefit","source_type":"word_analysis","support_id":"sup_4c8d1cf21241709f66b7","text":"{\"blocking_evidence\":null,\"headline\":\"address and benefit fused\",\"reader_payoff\":\"The reader notices that the same second-person addressee is heard first as beneficiary and then as possessor, not as two separate participants.\",\"reason\":\"Cross-reference evidence resolves the suffix in {{ar:لَكَ}} ({{tr:laka}}) and the suffix in {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) to the same single addressee.\",\"representative_source_ids\":[\"QG-1a02df1f\",\"QS-28f43c55\",\"QF-f3ca1757\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4","source_type":"word_analysis","support_id":"sup_4eb299ae9bf0697a1627","text":"{\"gloss_range\":\"the addressee's singular possessed chest as direct object: a bodily front, inner faculty, and source-like locus opened by the verb\",\"prose\":\"{{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) is the final landing point of the ayah and the direct object of {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}). Its accusative singular form makes one possessed locus the thing opened, while the suffix {{ar:كَ}} ({{tr:-ka}}) makes that locus personal and definite, tying it to the same addressee already marked in {{ar:لَكَ}} ({{tr:laka}}). The noun keeps the concrete chest in view, but its Quranic and lexical field also makes the chest an inner site of understanding, intention, and resolve. The {{ar:ص د ر}} ({{tr:ṣ-d-r}}) field adds frontness and issuing-forth force, so the opened patient becomes a source from which breath, voice, response, and action can proceed. As the fixed partner of {{ar:ش ر ح}} ({{tr:sh-r-ḥ}}), it echoes the request of 20:25 by declaring accomplished what is asked there, and it carries the expansion-or-constriction field of 6:125, 39:22, and 16:106 while the local grammar keeps the focus on this addressee's opened interior. The closing position also lets the God-and-knowledge co-occurrence pressure remain visible: the transformed interior is where divine awareness and human knowing intersect.\",\"root_display\":\"{{ar:ص د ر}} ({{tr:ṣ-d-r}})\",\"root_gloss_range\":\"broad root range includes chest or bodily front, foremost part, departing from water, source from which forms issue, liability settlement, and portion; the local noun selects chest/front and source-like inner locus, not the unrelated financial or departure branches\",\"surface_display\":\"{{ar:صَدْرَكَ}} ({{tr:ṣadraka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:implicit-divine-agent-and-open-purpose","source_type":"word_analysis","support_id":"sup_547e9311e5a04f2870b5","text":"{\"blocking_evidence\":null,\"headline\":\"divine agency with open enabled capacity\",\"reader_payoff\":\"The reader notices that agency, benefit, and patienthood are all packed into the verb frame, while the purpose or content of the opened capacity remains unstated.\",\"reason\":\"The verb instance has prodrop first-person plural subject agreement, a benefactive {{ar:لـ}} ({{tr:li-}}) complement, and the explicit object {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}), with no separate complement naming what the expansion is for.\",\"representative_source_ids\":[\"QG-1a6f0503\",\"QG-e813b584\",\"QS-e5b90d54\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2","source_type":"word_analysis","support_id":"sup_5984a4fb08c6126a38a1","text":"{\"gloss_range\":\"lam-governed Form I opening or widening of the addressee's chest, carrying physical opening, clarification, receptivity, and relief while excluding unrelated root branches\",\"prose\":\"{{ar:نَشْرَحْ}} ({{tr:nashraḥ}}) is the clause's action-node: {{ar:أَلَمْ}} ({{tr:ʾa-lam}}) governs it as a jussive, the initial {{ar:نـ}} ({{tr:n-}}) carries the first-person plural speaker inside the verb, {{ar:لَكَ}} ({{tr:laka}}) marks the beneficiary, and {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) supplies the opened object. Its final sukūn makes the lam-governed apocopation audible, and the reported final-fatḥa variant marks exactly where that jussive dependence is tested. Its root lets opening, widening, clarification, and gladdening converge, because the object is a chest that is also an inner faculty; the meat-cutting branch remains only an image of laying open what was closed so it becomes visible and intelligible, while unrelated sexual, worldly-inclination, and guarding branches are not local senses. The Form I stem presents one comprehensive divine opening rather than repeated anatomical dissection or a chest opening itself. The terminal {{ar:ح}} ({{tr:ḥāʾ}}) gives the opening verb a constricted throat release, so the sound texture mirrors the movement from constriction toward opening. The root-pair with {{ar:صَدْر}} ({{tr:ṣadr}}) also links this word to the wider formula seen in 6:125, 20:25, 39:22, and 16:106: 20:25 asks for chest-opening, 94:1 declares it accomplished, and 6:125 sets expansion against constriction.\",\"root_display\":\"{{ar:ش ر ح}} ({{tr:sh-r-ḥ}})\",\"root_gloss_range\":\"broad root range includes clarifying, cutting or spreading, opening the chest to receive good, euphemistic sexual uses, expansive inclination, and guarding; the local verb selects the chest-opening and clarification field, with the cutting-open image only as constrained pressure\",\"surface_display\":\"{{ar:نَشْرَحْ}} ({{tr:nashraḥ}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:1:2:1","source_type":"qac_morpheme","support_id":"sup_68efa5d1da95ab73e5a0","text":"{\"lemma_ar\":\"شَرَحَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:$araHa|ROOT:$rH|1P|MOOD:JUS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"94:1:2:1\",\"qac_word_ref\":\"94:1:2\",\"root_ar\":\"ش ر ح\",\"surface_ar\":\"نَشْرَحْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:audible-throat-release","source_type":"word_analysis","support_id":"sup_7054149fd2c3499dce40","text":"{\"blocking_evidence\":null,\"headline\":\"throat sound echoes opening\",\"reader_payoff\":\"The reader notices a sound-level fit: the word for opening ends with a constricted throat consonant, making release audible in the recitation.\",\"reason\":\"No guardrail evidence contradicts the phonetic observation, so it survives as a sound-texture payoff rather than a claim about lexical sense.\",\"representative_source_ids\":[\"QP-b4622ee9\",\"MP-914726e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:1","source_type":"word_analysis","support_id":"sup_7274bfb129c9519d358a","text":"{\"gloss_range\":\"fused interrogative plus lam-negation that frames the following jussive predicate as a recognition-demand, not a flat denial\",\"prose\":\"{{ar:أَلَمْ}} ({{tr:ʾa-lam}}) opens the surah by making the completed favor something the addressee is pressed to acknowledge. The hamza gives the clause question-shape, while {{ar:لَمْ}} ({{tr:lam}}) negates the following jussive predicate; together they produce an affirmative recognition rather than a simple report. The fused particle also controls the form of {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}), so the opening word is not separate from the verb it governs. In the four-word sequence, the reader moves from question-frame to divine act, then to {{ar:لَكَ}} ({{tr:laka}}) and {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}), where the repeated addressee-marking binds benefit and possession inside one compact address.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَلَمْ}} ({{tr:ʾa-lam}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:bodily-inner-cognition","source_type":"word_analysis","support_id":"sup_8ca2a6b36bb017dca515","text":"{\"blocking_evidence\":null,\"headline\":\"body term as inner faculty\",\"reader_payoff\":\"The reader notices that the noun holds concrete chest imagery together with understanding, intention, and resolve.\",\"reason\":\"V4 supports the bodily chest and front-part branches for {{ar:ص د ر}} ({{tr:ṣ-d-r}}), while contextual evidence shows the noun moving across concrete and abstract uses; local syntax narrows that range to the possessed chest as inner locus.\",\"representative_source_ids\":[\"QS-0dc38765\",\"QS-23fe00a4\",\"QS-7ce61ed2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:opened-chest-semantic-convergence","source_type":"word_analysis","support_id":"sup_94da82b36901f1ea228f","text":"{\"blocking_evidence\":null,\"headline\":\"opening, clarification, and receptivity converge\",\"reader_payoff\":\"The reader notices that the verb does not reduce to a flat emotional relief; it opens an inner chest in a way that is bodily, cognitive, and receptive.\",\"reason\":\"V4 supports clarification, cutting/opening imagery, and chest-opening branches for {{ar:ش ر ح}} ({{tr:sh-r-ḥ}}), but the local object and grammar narrow the active sense to opening or widening the addressee's {{ar:صَدْر}} ({{tr:ṣadr}}), not every dictionary branch.\",\"representative_source_ids\":[\"QS-59c9731d\",\"QS-73b1d1d2\",\"MS-3ced0442\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:1:4:1","source_type":"qac_morpheme","support_id":"sup_95bec948040107d81271","text":"{\"lemma_ar\":\"صَدْر\",\"morph_features\":\"STEM|POS:N|LEM:Sador|ROOT:Sdr|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"94:1:4:1\",\"qac_word_ref\":\"94:1:4\",\"root_ar\":\"ص د ر\",\"surface_ar\":\"صَدْرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:formulaic-sharh-sadr-echo","source_type":"word_analysis","support_id":"sup_96a6e8745bc88b211777","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic chest-opening echo\",\"reader_payoff\":\"The reader notices that the final noun is the fixed partner of the opening verb in a wider Quranic field of expansion, request, and constriction.\",\"reason\":\"The CRITICAL rows give concrete cross-surah comparanda at 20:25, 39:22, 16:106, and 6:125, and the local attachment confirms {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) as the object paired with {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}).\",\"representative_source_ids\":[\"QI-bfc212c2\",\"MI-612563e6\",\"QE-bd84dd7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:1:fused-particle-jussive-control","source_type":"word_analysis","support_id":"sup_a41021222809d7bc9941","text":"{\"blocking_evidence\":null,\"headline\":\"fused particle controls the verb\",\"reader_payoff\":\"The reader notices that the first word is a compact form-control unit whose negating particle shapes the mood of the following verb.\",\"reason\":\"Attachment evidence makes {{ar:أَلَمْ}} ({{tr:ʾa-lam}}) the particle complement governing the apocopated verb {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}).\",\"representative_source_ids\":[\"QF-023da2c8\",\"QF-3ca21e9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:source-and-front-origin","source_type":"word_analysis","support_id":"sup_ac54246b32f2e19f192d","text":"{\"blocking_evidence\":null,\"headline\":\"opened patient becomes source-point\",\"reader_payoff\":\"The reader notices that the opened chest is not only a container receiving relief but also a front or source from which response can issue.\",\"reason\":\"V4 includes front/beginning and source-from-which-forms-issue branches, but the local noun does not activate unrelated departure, liability, or portion senses.\",\"representative_source_ids\":[\"QS-146bf938\",\"QS-36491f47\",\"MS-45515a68\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:4:closing-transformation-site","source_type":"word_analysis","support_id":"sup_b6040a8ad4113fb818c1","text":"{\"blocking_evidence\":null,\"headline\":\"closing word concentrates transformation\",\"reader_payoff\":\"The reader notices that the ayah lands on the opened interior, where object grammar, possession, knowledge, formula, and closure converge.\",\"reason\":\"The word closes the single clause, and the retained rows connect its grammar and co-occurrence profile to the ayah's concentrated transformation site.\",\"representative_source_ids\":[\"QT-62def9bc\",\"ME-934ad674\",\"QY-7416a3f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:1:surah-opening-sequence","source_type":"word_analysis","support_id":"sup_bdf9f73bb7470c528de7","text":"{\"blocking_evidence\":null,\"headline\":\"surah-opening sequence stages the favor\",\"reader_payoff\":\"The reader notices the whole opening beat unfold in order: recognition-frame, act, beneficiary, and finally the possessed inner object.\",\"reason\":\"The single local clause runs from {{ar:أَلَمْ}} ({{tr:ʾa-lam}}) through {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}), and cross-reference evidence keeps the two second-person suffixes tied to the same addressee.\",\"representative_source_ids\":[\"QT-33f1220b\",\"QT-e1c1c049\",\"QE-cf632fdf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:2:lam-governed-jussive","source_type":"word_analysis","support_id":"sup_c25d56279f144b04919d","text":"{\"blocking_evidence\":null,\"headline\":\"lam-governed jussive verb\",\"reader_payoff\":\"The reader notices that the opening act sits inside the first word's negated-question control rather than appearing as an independent indicative statement.\",\"reason\":\"QAC and attachment both parse {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}) as governed by {{ar:لَمْ}} ({{tr:lam}}), with final jussive apocopation visible in the local form.\",\"representative_source_ids\":[\"QG-18f2ba3e\",\"MG-948fd53d\",\"QF-01f73ced\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:1:negative-interrogative-recognition","source_type":"word_analysis","support_id":"sup_c9850c556a5ea81f1c4b","text":"{\"blocking_evidence\":null,\"headline\":\"negative question as compelled recognition\",\"reader_payoff\":\"The reader notices that the ayah is not merely denying a non-action; it uses a negative question to make the completed opening something the addressee must acknowledge.\",\"reason\":\"QAC parses {{ar:أَلَمْ}} ({{tr:ʾa-lam}}) as interrogative hamza plus jussive {{ar:لَمْ}} ({{tr:lam}}), and attachment support warns against flattening the form into a simple denial.\",\"representative_source_ids\":[\"QG-a4b89444\",\"MG-89107258\",\"QI-b53191e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:3:benefactive-recipient-not-patient","source_type":"word_analysis","support_id":"sup_f33f819a80ab2a699854","text":"{\"blocking_evidence\":null,\"headline\":\"beneficiary before patient\",\"reader_payoff\":\"The reader notices that the act is done for the addressee, while the chest, not the addressee directly, is the grammatical object opened.\",\"reason\":\"Attachment evidence links {{ar:لَكَ}} ({{tr:laka}}) as a prepositional complement of {{ar:نَشْرَحْ}} ({{tr:nashraḥ}}), while {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) is the direct object.\",\"representative_source_ids\":[\"QG-75aae6f7\",\"QG-eb87b569\",\"MG-629d965d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:1:3","source_type":"word_analysis","support_id":"sup_fb693d4930290942ef5b","text":"{\"gloss_range\":\"benefactive prepositional phrase with a second-person masculine singular suffix, marking the addressee as recipient-beneficiary before the direct object appears\",\"prose\":\"{{ar:لَكَ}} ({{tr:laka}}) makes the expansion explicitly for the addressee before the chest is named as the thing opened. The {{ar:لـ}} ({{tr:li-}}) complement marks benefit, purpose, and dative recipienthood, so the addressee is not the grammatical patient; {{ar:صَدْرَكَ}} ({{tr:ṣadraka}}) will fill that role. Because the preposition and {{ar:كَ}} ({{tr:-ka}}) are fused in one word, direct address and benefit arrive together, and the same addressee then reappears as the possessor of the object. Its position between verb and object foregrounds the recipient before the affected inner locus.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَكَ}} ({{tr:laka}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000784/B001","root_000849/B001","root_000849/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000784","role":"Opening a hidden meaning into clarity supplies the operation: an opaque interior is rendered intelligible.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The bodily chest fixes that clarified interior in an embodied site rather than an abstract faculty.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"A source from which actions issue turns the chest into the generative interior being clarified.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"changed_reading":{"after":"A claim that the inward source of response was opened into intelligibility, so action can issue from a clarified interior.","before":"A generic reassurance that the chest was made broad."},"confidence":"strong","focus_anchor":"نَشْرَحْ acts on صَدْرَكَ: an opening or explication is applied to the chest, which can also image an originating source.","mechanism":"The chest is construed as the inward source from which speech and action issue. شرح opens what is hidden until it becomes intelligible, so the intervention makes that source both spacious and legible.","model_id":"baseline_clarified_inner_source"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_clarified_inner_source","source_type":"hft","support_id":"sup_285ae75f1c269bd3cbb0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000784/B002","root_000849/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000784","role":"Spreading and slicing flesh contributes a material operation of opening surface and redistributing thickness.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000849","role":"The anatomical chest supplies the bodily material and load-bearing front on which that operation is imagined.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"changed_reading":{"after":"An embodied unbinding or spreading of the bodily front, with relief imagined as altered material geometry.","before":"An idiom for inward comfort with no specified mechanics."},"confidence":"medium","focus_anchor":"The same verb-root can image flesh being spread or sliced, while its object names the bodily front.","mechanism":"The construction permits an embodied geometry: constricted material at the front of the torso is spread, thinned, or unfolded. Relief is therefore not only a mental state but a change in how pressure occupies the body.","model_id":"baseline_material_unfolding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_material_unfolding","source_type":"hft","support_id":"sup_07120fc2461a63f214df","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000784/B006","root_000849/B004"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000784","role":"Guarding crops or young palms contributes preservation as the way newly available capacity is kept viable.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The originating source supplies the protected generative center whose future acts are being preserved.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"changed_reading":{"after":"Opening establishes protected capacity: the source becomes usable without being abandoned to exposure.","before":"Opening removes boundaries and exposes what was inside."},"confidence":"exploratory","focus_anchor":"A branch of شرح means guarding young growth, and صدر can denote the source from which acts issue.","mechanism":"Opening need not mean leaving the interior exposed. It can establish a protected generative enclosure: capacity is made usable while what is young or vulnerable within it is kept from loss.","model_id":"baseline_guarded_capacity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_guarded_capacity","source_type":"hft","support_id":"sup_4cfc6f76c26f3e2cf3f4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ","ayah_ref":"94:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000784/B005","root_000849/B004"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000784","role":"Expansive inclination toward something supplies a widening of desire rather than only a widening of space.","root":"ش ر ح","source_ref":"94:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000849","role":"The source from which acts issue makes expanded inclination operational: desire can become conduct.","root":"ص د ر","source_ref":"94:1","source_word_indices":["4"]}],"changed_reading":{"after":"The motivational source gains a larger capacity to incline and act, without yet specifying where that desire should point.","before":"The chest receives passive emotional relief."},"confidence":"medium","focus_anchor":"شرح can name an inward expansion of inclination, and the chest can be the source of ensuing action.","mechanism":"The opening enlarges motivational range. The chest is not merely calmed; its power to incline, choose, and send action outward is expanded, although the focus ayah alone leaves the desired object unspecified.","model_id":"baseline_expanded_desire"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_expanded_desire","source_type":"hft","support_id":"sup_47294475791d784a05b0","trust":"legacy_unbound"}]}
</lane_packet_json>
