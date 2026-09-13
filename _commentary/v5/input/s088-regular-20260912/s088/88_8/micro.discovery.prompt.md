# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:8",
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
{"branch_registry":[{"boundary":"Bu kol övgü, olumlu cevap, hayvan adı ve kuş adı olan ayrı kollardan uzak tutulur.","branch_kind":"bare","branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_cff8a4865edae7f185d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"iyi yaşam durumu ve başkasına ulaştırılan iyilik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Rahatlık, geçim genişliği ve iyi oluşla belirlenen elverişli yaşam durumu."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birine verilen bağış, yapılan iyilik veya yararın o kişiye ulaştırılması."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kolun hem elverişli durum hem verilen ya da iletilen yarar yönlerini birlikte karşılar.","boundary_detail":"Bu kol övgü, olumlu cevap, hayvan adı ve kuş adı olan ayrı kollardan uzak tutulur.","branch_image_ar":"حسن الحال والنعمة","concept_gloss":"iyi yaşam durumu ve başkasına ulaştırılan iyilik","contextual_glosses":[{"applicability":"Kişinin iyi ve rahat yaşam durumunun anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağışın veya iyiliğin başka birine ulaştırılması yönünü karşılamaz.","preserves":"Elverişli yaşam ve rahatlık yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"esenlik ve bolluk","usage_role":"contextual"},{"applicability":"Bir yararın bir kişiye verilmesi veya ulaştırılması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin içinde bulunduğu rahat yaşam durumunu tek başına anlatmaz.","preserves":"Verilen yarar ile iyiliğin başkasına ulaştırılması yönünü korur."},"facet_ids":["F002"],"text":"bağış ve iyilik sunma","usage_role":"contextual"}],"definition":"Kişinin rahat, iyi ve elverişli bir yaşam durumunda bulunması; ayrıca bir yararın bağış, yardım ya da iyilik olarak ona ulaşması veya başkasına ulaştırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Rahatlık, geçim genişliği ve iyi oluşla belirlenen elverişli yaşam durumu."},{"facet_id":"F002","role":"extension","statement":"Birine verilen bağış, yapılan iyilik veya yararın o kişiye ulaştırılması."}],"identity_rationale":"Kaynak ifadesi iyi ve rahat yaşama durumunu, kişiye ulaşan bağış ve iyiliği ve iyiliğin başkasına ulaştırılması eylemini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bağış, iyilik veya elverişli yaşam durumu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"iyi durum ve esenlik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bolluk ve rahatlık"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bol ve rahat yaşam"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyiliği başkasına ulaştırma"}],"lexicalization_note":"Tanım yalın kola aittir; başka kollardaki kalıplaşmış kullanımlardan anlam aktarılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; iyi yaşam ile yarar aktarımının sınırını en açık gösteren iki karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol iyi durum ile verilen yararı kavramlaştırır; komşu kol ise yumuşaklık niteliğini ve rahat yaşama sürecini öne çıkarır.","focus_only":"İyi durumun yanı sıra bağış ve iyiliğin bir başkasına ulaştırılmasını içerir.","gloss":"yumuşaklık ve rahat yaşama","neighbor_only":"Nesnenin yumuşaması ile kişinin rahat yaşaması veya yaşatılması yönlerini içerir.","neighbor_ref":"root_001525/B002","relation_type":"near_neighbor","shared_zone":"Her iki kol da rahat ve elverişli yaşama durumuna değebilir."},{"boundary_match":"partial","distinction":"Komşu kol karşılıksız verme ve bağış üzerinde yoğunlaşırken bu kol ayrıca yararın sonucundaki iyi yaşam durumunu da kapsar.","focus_only":"Yarar aktarımının yanında kişinin iyi ve rahat yaşam durumunu da kapsar.","gloss":"karşılıksız iyilik ve bağış","neighbor_only":"Özellikle yükümlülük dışı bağış, karşılıksız verme ve iyilik bolluğunu öne çıkarır.","neighbor_ref":"root_001163/B003","relation_type":"near_synonym","shared_zone":"İki kol da bir kişiye yarar sağlayan bağış ve iyilik alanında örtüşür."}],"source_phrase_ar":"أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)","source_summary":"Ortak kanıt, iyi ve rahat yaşam durumunu bunun kişiye verilen yarar ve başkasına ulaştırılan iyilik yönleriyle bir arada gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النعمة والنعمى والنعماء والنعيم والإنعام، بمعنى حسن الحال وطيب العيش والمن والعطاء والإحسان الموصل إلى غيره.","what_is_not_ar":"ليس هو نعم المدح، ولا نعم الجواب، ولا اسم الأنعام، ولا النعامة والطائر وما شبه بها."},"support_links":["sup_2b6d1ab8539602b9597e"]},{"boundary":"Yumuşaklık çekirdeği ile rahat yaşam ve rahat yaşatma kullanımları ayrı yüzler olarak korunur.","branch_kind":"mixed_non_bare","branch_ref":"root_001525/B002","candidate_links":[{"candidate_id":"cand_5ad5c2ade7ac3211c70d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"yumuşamak, rahat yaşamak veya rahat yaşatmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin yumuşak nitelik kazanması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin rahatlık, bolluk ve incelik içinde yaşaması."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başkasını rahatlık ve bolluk içinde yaşatmak."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın nitelik ile yapıya bağlı yaşam ve ettirme yönlerinin tamamını kapsar.","boundary_detail":"Yumuşaklık çekirdeği ile rahat yaşam ve rahat yaşatma kullanımları ayrı yüzler olarak korunur.","branch_image_ar":"اللين والنعومة ورفاه العيش","concept_gloss":"yumuşamak, rahat yaşamak veya rahat yaşatmak","contextual_glosses":[{"applicability":"Bir nesnenin fiziksel niteliğinin yumuşadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rahat yaşama ve bir başkasını rahat yaşatma yönlerini dışarıda bırakır.","preserves":"Fiziksel yumuşama çekirdeğini korur."},"facet_ids":["F001"],"text":"yumuşamak","usage_role":"contextual"},{"applicability":"Kişinin rahat ve varlıklı yaşamı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel yumuşama ile başkasını rahat yaşatma yönlerini karşılamaz.","preserves":"Rahatlık ve bolluk içindeki yaşam yönünü korur."},"facet_ids":["F002"],"text":"bolluk içinde yaşamak","usage_role":"contextual"}],"definition":"Bir şeyin yumuşak duruma gelmesidir. Belirli kullanımlarda kişinin rahat ve bolluk içinde yaşamasını ya da bir başkasını böyle yaşatmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin yumuşak nitelik kazanması."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin rahatlık, bolluk ve incelik içinde yaşaması."},{"facet_id":"F003","role":"associated_use","statement":"Bir başkasını rahatlık ve bolluk içinde yaşatmak."}],"identity_rationale":"Kaynak ifadesi fiziksel yumuşama ile rahat ve bolluk içindeki yaşamı, ayrıca birini böyle yaşatma eylemini açıkça birlikte verir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşamak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yumuşak; rahat yaşayan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"rahat ve bolluk içinde yaşayan kadın"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çocuklarını bolluk içinde yaşattı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"rahat ve bolluk içindeki yaşam"}],"lexicalization_note":"Yalın yumuşaklık anlamı ile belirli yapılardaki rahat yaşama ve yaşatma anlamları birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; fiziksel yumuşaklık ile rahat yaşam sınırını en iyi açan iki yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol yumuşaklıktan rahat yaşama ve yaşatmaya uzanır; komşu kol ise kolaylık ve davranış yumuşaklığına kadar genişler.","focus_only":"Rahat ve bolluk içinde yaşama ile başkasını böyle yaşatma kullanımlarını içerir.","gloss":"yumuşaklık ve sertliğin giderilmesi","neighbor_only":"Kolaylık, hoşgörü ve insanlarla yumuşak davranma gibi toplumsal yönlere uzanır.","neighbor_ref":"root_000753/B002","relation_type":"near_synonym","shared_zone":"Her iki kol fiziksel yumuşaklık ve sertliğin azalması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu kol nitelik bildiren yumuşaklık ve gürlüğe odaklanır; bu kol ayrıca durum değişmesini ve rahat yaşama sürecini anlatır.","focus_only":"Yumuşama sürecini ve birini rahat yaşam koşullarına kavuşturmayı kapsar.","gloss":"yumuşak ve gür nitelik","neighbor_only":"Yumuşaklıkla birlikte gürlük ve verimlilik niteliğini öne çıkarır.","neighbor_ref":"root_001075/B002","relation_type":"near_synonym","shared_zone":"İki kol da yumuşaklık ve rahatlık çağrışımında belirgin biçimde örtüşür."}],"source_phrase_ar":"نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)","source_summary":"Kanıt, yumuşaklık niteliğini rahat yaşamla ilişkilendirir ve bu durumu bir başkasına sağlama eylemini de ayrı bir kullanım olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه نعم الشيء إذا لان، والناعم والمنعم والمناعم، والتنعم وطيب العيش والترف، والطعام أو الشخص الموصوف بالنعومة أو الرفاه.","what_is_not_ar":"لا يدخل فيه مجرد العطاء والمن إذا كان المقصود الإحسان لا صفة اللين والترف، ولا نعم الجواب والمدح."},"support_links":["sup_cd28e438ad3004719364"]},{"boundary":"Övgü işlevi, aynı biçimin olumlu cevap verme işlevinden kesin olarak ayrılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001525/B003","candidate_links":[{"candidate_id":"cand_9ae64b59e50857e0b0f3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"övgü ve beğeni bildirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, şey veya davranış hakkında övgü ve beğeni bildirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Övgüyü belirli söz dizimsel kalıplarla dile getirme."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek başına veya özel yapılarda kullanılan övgü işlevinin tamamına uygundur.","boundary_detail":"Övgü işlevi, aynı biçimin olumlu cevap verme işlevinden kesin olarak ayrılır.","branch_image_ar":"مدح الشيء بنعم","concept_gloss":"övgü ve beğeni bildirmek","contextual_glosses":[{"applicability":"Bir şeyin doğrudan beğenilip övüldüğü cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her özel övgü yapısının söz dizimsel biçimini tek başına göstermez.","preserves":"Doğrudan beğeni ve övgü bildirme işlevini korur."},"facet_ids":["F001"],"text":"ne güzel","usage_role":"contextual"}],"definition":"Bir şeyi iyi, güzel veya yerinde bularak onu özel bir söz ya da kalıpla övmek ve beğeniyi bildirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, şey veya davranış hakkında övgü ve beğeni bildirme."},{"facet_id":"F002","role":"specialization","statement":"Övgüyü belirli söz dizimsel kalıplarla dile getirme."}],"identity_rationale":"Kaynak ifadesi bu kolu yerginin karşısında duran, bir şeyi beğenip öven özel söz ve yapılar olarak açıkça belirler.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ne güzel; övgü bildirir"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu ne güzel"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"öyleyse ne güzel, yerinde olur"}],"lexicalization_note":"Tek başına övgü bildiren biçim ile belirli övgü kalıpları birlikte gösterilir, cevap anlamına genişletilmez.","neighbor_coverage_note":"Tüm adaylar incelendi; karşıt yergi kutbu ile en yakın övgü sözü sınırı okuyucu için en yararlı iki ayrımdır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu kol olumlu değerlendirme ve övgü verir; komşu kol aynı eksenin karşı kutbunda olumsuz değerlendirme ve yergi verir.","focus_only":"Bir şeyi iyi ve beğenilir gösteren övgü kutbunu bildirir.","gloss":"yergi ve kötüleme bildirmek","neighbor_only":"Bir şeyi kötü ve yerilir gösteren yergi kutbunu bildirir.","neighbor_ref":"root_000079/B004","relation_type":"antonym","shared_zone":"İki kol da bir şey hakkında değer yargısını özel bir sözle bildirir."},{"boundary_match":"partial","distinction":"Bu kolun çekirdeği yalın övgüdür; komşu kol ise övgüden güçlü istek ve sevgi bildirimine de geçebilir.","focus_only":"Yerginin karşıtı olan genel övgü işlevini ve ona özgü yapıları taşır.","gloss":"övgü ve güçlü beğeni sözü","neighbor_only":"Övgünün yanında güçlü istek ve sevgi derecesini bildiren kullanımlara da uzanır.","neighbor_ref":"root_000286/B003","relation_type":"near_synonym","shared_zone":"Her iki kol doğrudan beğeni ve övgü bildiren sözlerde örtüşür."}],"source_phrase_ar":"نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)","source_summary":"Ortak kanıt, biçimi yergi bildiren karşıtının karşısına yerleştirir ve hem tek başına hem belirli yapılarda övgü işlevi taşıdığını gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نعم المقابلة لبئس، ونعم الشيء، ونعما، وفبها ونعمت، حيث تكون اللفظة فعلا أو صيغة مدح واستحسان.","what_is_not_ar":"لا يدخل فيه نعم التي تجيب السؤال أو تصدق الخبر، ولا النعمة بمعنى العطاء."},"support_links":["sup_104a96babe00c0572e21"]},{"boundary":"Bu cevap işlevi övgü bildiren eş biçimli koldan ve genel doğruluk inancından ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001525/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"evet diyerek onaylamak veya söz vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soruya veya önermeye olumlu cevap verip onu doğrulama."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gelecekte yapılacak bir iş için olumlu söz veya güvence verme."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumlu cevap, doğrulama ve olumlu güvence verme işlevlerini birlikte karşılar.","boundary_detail":"Bu cevap işlevi övgü bildiren eş biçimli koldan ve genel doğruluk inancından ayrıdır.","branch_image_ar":"الجواب بنعم والتصديق","concept_gloss":"evet diyerek onaylamak veya söz vermek","contextual_glosses":[{"applicability":"Olumlu cevap verilen veya bir önermenin doğrulandığı konuşmalarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gelecekte yapılacak iş için açıkça söz verme yönünü zorunlu olarak göstermez.","preserves":"Olumlu cevap ve doğrulama işlevini doğrudan korur."},"facet_ids":["F001"],"text":"evet","usage_role":"contextual"},{"applicability":"Bir isteğe olumlu karşılık verilip geleceğe dönük güvence sunulduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir önermeyi yalnızca doğru diye onaylama işlevini kapsamaz.","preserves":"Olumlu söz ve işi yapma güvencesi yönünü korur."},"facet_ids":["F002"],"text":"olur, yaparım","usage_role":"contextual"}],"definition":"Bir soruya olumlu cevap vermek, söylenen bir şeyi doğru diye onaylamak veya istenen bir iş için olumlu söz vermektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soruya veya önermeye olumlu cevap verip onu doğrulama."},{"facet_id":"F002","role":"extension","statement":"Gelecekte yapılacak bir iş için olumlu söz veya güvence verme."}],"identity_rationale":"Kaynak ifadesi olumlu cevap, söyleneni doğrulama ve geleceğe dönük söz verme işlevlerini aynı cevap kolunda açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"evet; doğru; olur"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ona evet dedi"}],"lexicalization_note":"Tek başına kullanılan olumlu cevap ile birine olumlu cevap verme yapısı korunur, övgü anlamı içeri alınmaz.","neighbor_coverage_note":"Adayların hepsi değerlendirildi; genel olumlu cevap ile doğrulayıcı ve olumsuzluğu bozan cevap türleri arasındaki iki sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol doğrulayıcı cevapta yoğunlaşır; bu kol ise genel olumlu yanıtın yanında söz verme işlevine de sahiptir.","focus_only":"Soru yanıtlamanın yanında olumlu söz ve güvence verme işlevini de kapsar.","gloss":"doğrulayan olumlu cevap","neighbor_only":"Özellikle geleceğe ilişkin bir bildirimi doğru diye kabul eden cevap sözüdür.","neighbor_ref":"root_000016/B003","relation_type":"near_synonym","shared_zone":"İki kol da konuşmada söyleneni doğru sayan olumlu cevap verir."},{"boundary_match":"partial","distinction":"Bu kol genel onay ve olumlu yanıt verir; komşu kol özellikle önceki olumsuzluğu bozup tersini doğrular.","focus_only":"Olumlu soruyu veya bildirimi onaylar ve gerektiğinde söz verme işlevi taşır.","gloss":"olumsuz sözü düzelten olumlu cevap","neighbor_only":"Olumsuz kurulmuş sözü geri çevirerek karşıt olumlu hükmü doğrular.","neighbor_ref":"root_000153/B006","relation_type":"near_neighbor","shared_zone":"Her iki kol da konuşmada olumlu hüküm kuran kısa cevap sözleridir."}],"source_phrase_ar":"نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)","source_summary":"Kanıt, bu cevap sözünün olumsuz cevabın karşıtı olduğunu ve soru yanıtlama, doğrulama ve söz verme işlevlerinde kullanıldığını ortak biçimde gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نعم حرفا أو كلمة جواب، للتصديق والإيجاب والعدة، وما اتصل بذلك مثل أنعم له أي قال له نعم.","what_is_not_ar":"لا يدخل فيه نعم المدحية المقابلة لبئس، ولا النعمة بمعنى الإحسان."},"support_links":[]},{"boundary":"Deveye özgü dar kapsam ile daha geniş otlayan evcil hayvan topluluğu aynı düzeyde genellenmemelidir.","branch_kind":"bare","branch_ref":"root_001525/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"develer ve geniş anlamda otlayan evcil hayvanlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dar ve belirgin kullanımda develer veya deve malı."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geniş topluluk adında deve, sığır ve koyunu kapsayan otlayan evcil hayvanlar."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deveye özgü dar kullanım ile daha geniş hayvan topluluğu kullanımını ayırarak karşılar.","boundary_detail":"Deveye özgü dar kapsam ile daha geniş otlayan evcil hayvan topluluğu aynı düzeyde genellenmemelidir.","branch_image_ar":"مال الأنعام والإبل","concept_gloss":"develer ve geniş anlamda otlayan evcil hayvanlar","contextual_glosses":[{"applicability":"Dar adın özellikle deve varlığını gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geniş adın sığır ve koyunu da kapsayan topluluk yönünü dışarıda bırakır.","preserves":"Dar kapsamdaki deveye özgü hayvan adını korur."},"facet_ids":["F001"],"text":"develer","usage_role":"contextual"},{"applicability":"Deve, sığır ve koyunun birlikte kapsandığı geniş kullanımlarda uygundur.","error_profile":{"adds":"Bağlam sınırlandırılmazsa kaynak kapsamı dışındaki başka otlayan evcil türleri de düşündürebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Geniş topluluk kapsamını ve hayvanların otlayan evcil türler oluşunu korur."},"facet_ids":["F002"],"text":"otlayan evcil hayvanlar","usage_role":"contextual"}],"definition":"Dar kullanımda develeri, daha geniş topluluk adında ise deve, sığır ve koyun gibi otlayan evcil hayvanları gösteren hayvan varlığıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dar ve belirgin kullanımda develer veya deve malı."},{"facet_id":"F002","role":"extension","statement":"Geniş topluluk adında deve, sığır ve koyunu kapsayan otlayan evcil hayvanlar."}],"identity_rationale":"Kaynak ifadesi tekil kullanımın özellikle develeri gösterdiğini, çoğul kapsamın ise deve, sığır ve koyun gibi otlayan evcil hayvanlara genişlediğini belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"develer; deve varlığı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"deve, sığır ve koyun topluluğu"}],"lexicalization_note":"Tanım yalın hayvan adlarını kapsar ve başka kollardaki kuş ya da bağış anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar tarandı; deve merkezli dar kapsam ile sürü ve küçükbaş topluluğu arasındaki iki karşılaştırma sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol dar adla deveyi, geniş adla birkaç evcil hayvan türünü kapsar; komşu kol devenin cinsiyet, erginlik ve sürü ayrıntılarına odaklanır.","focus_only":"Geniş kullanımda sığır ve koyunu da deveyle aynı hayvan topluluğuna katar.","gloss":"deve ve deve sürüsü","neighbor_only":"Ergin erkek deveyi, devenin eşini ve develerin sahipleriyle birlikte oluşturduğu sürüyü ayrıntılandırır.","neighbor_ref":"root_000260/B001","relation_type":"near_synonym","shared_zone":"İki kol da develeri ve deve varlığını doğrudan adlandırır."},{"boundary_match":"field_only","distinction":"Bu kol deve merkezli olup daha geniş bir tür dizisine açılır; komşu kol küçükbaş hayvanlarla sınırlıdır.","focus_only":"Deveyi merkez alır ve geniş kullanımda sığır ile koyunu birlikte kapsar.","gloss":"küçükbaş hayvan topluluğu","neighbor_only":"Yalnız koyun ve keçi türünden küçükbaş hayvan topluluğunu cinsiyet ayrımı yapmadan gösterir.","neighbor_ref":"root_001109/B001","relation_type":"same_field","shared_zone":"Her iki kol evcil ve otlayan hayvanların topluluk adları alanındadır."}],"source_phrase_ar":"النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)","source_summary":"Ortak kanıt, dar adın deveye özgü veya ağırlıklı olduğunu; geniş adın ise deve, sığır ve koyunla birlikte otlayan evcil hayvanları kapsadığını gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النعم والأنعام، خصوصا الإبل، وبالتوسيع الإبل والبقر والغنم والبهائم الراعية حيث نصت المصادر على ذلك.","what_is_not_ar":"لا يدخل فيه النعمة بمعنى العطاء، ولا النعام الطائر، ولا النعامة المشبهة."},"support_links":[]},{"boundary":"Tür kimliği sabittir, fakat tekil biçimin cinsiyet kapsamı kaynaklardaki farklı kullanımlara göre belirtilmelidir.","branch_kind":"bare","branch_ref":"root_001525/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"devekuşu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğrudan devekuşu türü ve bu türün bireyi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil ve topluluk adlarının erkek, dişi veya tür geneli için kullanılabilmesi."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş türünün kendisini karşılar; cinsiyet ayrımı gerektiğinde bağlamla belirlenir.","boundary_detail":"Tür kimliği sabittir, fakat tekil biçimin cinsiyet kapsamı kaynaklardaki farklı kullanımlara göre belirtilmelidir.","branch_image_ar":"النعام والنعامة الطائر","concept_gloss":"devekuşu","contextual_glosses":[{"applicability":"Tek bir cinsiyetten çok kuş türünün bütünü kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bazı kullanımlardaki özel erkek veya dişi birey ayrımını belirtmez.","preserves":"Kuşun tür kimliğini açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"devekuşu türü","usage_role":"explanatory"}],"definition":"Devekuşu türüdür; kullanılan biçime ve kaynağa göre türün bütünü, erkek veya dişi birey gösterilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğrudan devekuşu türü ve bu türün bireyi."},{"facet_id":"F002","role":"source_variant","statement":"Tekil ve topluluk adlarının erkek, dişi veya tür geneli için kullanılabilmesi."}],"identity_rationale":"Kaynak ifadesi kuş türünde birleşir; ancak tekil ve topluluk adlarının erkek, dişi veya türün bütünü için kullanılışı konusunda kapsam farkı bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"devekuşu; erkek veya dişi birey"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"devekuşu türü veya topluluğu"}],"lexicalization_note":"Tanım doğrudan kuş türüne aittir; benzetmeyle adlandırılan nesneler ve deyimler bu kola katılmaz.","neighbor_coverage_note":"Tüm aday kuş ve kuşla ilişkili adlar değerlendirildi; gerçek türü aktarmalı adlardan ve sürü adından ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol gerçek kuşu adlandırır; komşu kol kuşun görünüşünden hareketle başka varlıklara aktarılmış adları toplar.","focus_only":"Canlı kuş türünü ve onun erkek ya da dişi bireylerini doğrudan gösterir.","gloss":"devekuşuna benzetilen adlar","neighbor_only":"Kuşa benzetilerek aynı adın verildiği nesne, beden bölümü, yol ve gök konumlarını gösterir.","neighbor_ref":"root_001525/B007","relation_type":"near_neighbor","shared_zone":"Komşu koldaki aktarmalı adlandırmaların benzetme kaynağı bu kuşun görünüşüdür."},{"boundary_match":"partial","distinction":"Bu kol tür ve birey düzeyindedir; komşu kol ise yalnız birden çok bireyin oluşturduğu sürü düzeyindedir.","focus_only":"Türü veya tek bir erkek ya da dişi bireyi adlandırır.","gloss":"devekuşu sürüsü","neighbor_only":"Bir arada bulunan devekuşlarının oluşturduğu sürüyü özel bir topluluk adıyla gösterir.","neighbor_ref":"root_000453/B007","relation_type":"near_neighbor","shared_zone":"Her iki kolun canlı katılımcısı aynı kuş türüdür."}],"source_phrase_ar":"النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)","source_summary":"Kanıt kuş türünde birleşir; ayrım, tekil ve topluluk biçimlerinin tür geneli ile erkek veya dişi bireye nasıl dağıtıldığı noktadadır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النعامة والنعام للطائر المعروف، ذكرا أو أنثى، وما يذكر من جنسه وصفاته المباشرة.","what_is_not_ar":"لا يدخل فيه النعم الإبل، ولا الأجسام أو الأمثال المسماة نعامة بالتشبيه إلا إذا كان الطائر نفسه مقصودا."},"support_links":[]},{"boundary":"Benzetme ilişkisi korunmalı, listedeki nesnelerden bağımsız ve üretken bir genel anlam çıkarılmamalıdır.","branch_kind":"bare","branch_ref":"root_001525/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"devekuşuna benzetilerek ad verilen şeyler","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devekuşuna benzerlik yoluyla başka bir varlığa aktarılan ad."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu kirişi, dağ gölgeliği, ayak veya bacak bölümü ve yol için kullanılan aktarmalı adlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ay'ın konak yerlerinden biri veya bu adla anılan yıldız kümesi."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak benzetme kaynağını koruyarak farklı aktarmalı adların tümüne uygulanır.","boundary_detail":"Benzetme ilişkisi korunmalı, listedeki nesnelerden bağımsız ve üretken bir genel anlam çıkarılmamalıdır.","branch_image_ar":"ما سمي نعامة تشبيها بالهيئة","concept_gloss":"devekuşuna benzetilerek ad verilen şeyler","contextual_glosses":[{"applicability":"Kuyu, dağ, beden veya yol üzerindeki somut benzetme açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ay'ın konak yeri olarak kullanılan özel gökbilim adını açıkça kapsamaz.","preserves":"Görünüş benzerliğine dayalı somut ad aktarımını korur."},"facet_ids":["F001","F002"],"text":"devekuşu biçimli adlandırma","usage_role":"explanatory"}],"definition":"Devekuşunun görünüşüne veya belirgin bir özelliğine benzetilerek aynı adın verildiği kuyu kirişi, dağ gölgeliği, ayak ya da bacak bölümü, yol ve Ay'ın konak yerleri gibi varlıklardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devekuşuna benzerlik yoluyla başka bir varlığa aktarılan ad."},{"facet_id":"F002","role":"example","statement":"Kuyu kirişi, dağ gölgeliği, ayak veya bacak bölümü ve yol için kullanılan aktarmalı adlar."},{"facet_id":"F003","role":"specialization","statement":"Ay'ın konak yerlerinden biri veya bu adla anılan yıldız kümesi."}],"identity_rationale":"Kaynak ifadesi devekuşuna benzetilerek aynı adın verildiği çeşitli varlıkları destekler; bunlar tek bir nesne türü değil, ortak adlandırma yoluyla bağlı bir kümedir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Ay'ın konak yerlerinden biri"}],"lexicalization_note":"Yalın biçimlerin aktarmalı adları tanımlanır; gerçek kuş ve kuşlu deyimler bu kapsama alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; gerçek kuşla sınır ve başka bir benzetmeli ad kümesiyle yöntem farkı en yararlı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol benzerlik yoluyla başka varlıklara verilen adlardan oluşur; komşu kol ise benzetme kaynağı olan canlı türün kendisidir.","focus_only":"Kuşun adıyla anılan kuyu, dağ, beden, yol ve gök konumu gibi aktarmalı varlıkları kapsar.","gloss":"gerçek devekuşu","neighbor_only":"Canlı devekuşu türünü ve onun bireylerini doğrudan adlandırır.","neighbor_ref":"root_001525/B006","relation_type":"near_neighbor","shared_zone":"Aktarmalı adların ortak benzetme kaynağı komşu koldaki gerçek kuştur."},{"boundary_match":"partial","distinction":"Adlandırma yöntemi benzerdir, fakat benzetme kaynağı ve ad verilen nesneler bütünüyle ayrıdır.","focus_only":"Ad aktarımında kaynak görüntü olarak devekuşunu kullanır ve gök konumuna kadar uzanır.","gloss":"böbrek biçiminden aktarılan adlar","neighbor_only":"Ad aktarımında kaynak görüntü olarak böbreğin biçimini kullanır ve kap, yay ile bulut parçalarına yönelir.","neighbor_ref":"root_001317/B006","relation_type":"near_neighbor","shared_zone":"Her iki kol bir varlığın görünüşünü başka nesnelere ad olarak aktarma yolunu kullanır."}],"source_phrase_ar":"على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)","source_summary":"Ortak kanıt, kuşun görünüşünden doğan ad aktarımını kuyu ve dağ yapıları, beden bölümleri, yol ve gök konumu gibi farklı somut örneklerle gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه المسميات المشبهة بالنعامة في الهيئة أو البعد أو السرعة، مثل خشبة البئر والظلة على رأس الجبل وباطن القدم أو عرق الرجل أو الساق والمحجة والنعائم من منازل القمر.","what_is_not_ar":"لا يدخل فيه الطائر نفسه، ولا الإبل والأنعام، ولا نعم الجواب والمدح."},"support_links":[]},{"boundary":"Anlam yalnız verilen söz kalıplarına aittir; kuşun tek başına taşıdığı yalın bir dağılma anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001525/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"bir topluluğun dağılıp gücünü yitirmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun bir arada kalamayarak dağılıp ayrılması veya yola çıkması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun ortak sözünü, gücünü veya saygınlığını yitirmesi."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan kuş imgeli sözlerdeki dağılma, ayrılma ve güç kaybı alanını karşılar.","boundary_detail":"Anlam yalnız verilen söz kalıplarına aittir; kuşun tek başına taşıdığı yalın bir dağılma anlamı değildir.","branch_image_ar":"طيران النعامة وتفرق القوم","concept_gloss":"bir topluluğun dağılıp gücünü yitirmesi","contextual_glosses":[{"applicability":"Topluluğun birliğini kaybedip farklı yönlere ayrıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hızlı yol alma kullanımını zorunlu olarak belirtmez.","preserves":"Topluluğun dağılması ve ortaklığının bozulması yönünü korur."},"facet_ids":["F001","F002"],"text":"dört bir yana dağıldılar","usage_role":"contextual"}],"definition":"Belirli kuş imgeli sözlerde bir topluluğun hızla dağılıp ayrılması, yol alması veya birliğini ya da gücünü yitirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun bir arada kalamayarak dağılıp ayrılması veya yola çıkması."},{"facet_id":"F002","role":"extension","statement":"Topluluğun ortak sözünü, gücünü veya saygınlığını yitirmesi."}],"identity_rationale":"Kaynak ifadesi belirli kuş imgeli sözlerin topluluğun dağılması, hızla ayrılması, yol alması, birliğini ya da gücünü yitirmesi için kullanıldığını destekler.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"dağıldılar, ayrıldılar veya güçlerini yitirdiler"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hızla yola koyulup gittiler"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yenilip dağıldılar"}],"lexicalization_note":"Tanım yalnız kanıtlanan söz kalıplarına bağlanır ve yalın kuş adına dağılma ya da yenilme anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; farklı yönlere dağılma karşılaştırması kalıbın ayrılma ve güç kaybı sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol yönlere saçılma üzerinde yoğunlaşır; bu kol ise belirli kuş imgeli yapılarda ayrılma ve güç kaybını da kapsar.","focus_only":"Dağılmanın yanında ayrılma, hızla yol alma ve güç kaybı sonuçlarını taşıyabilir.","gloss":"farklı yönlere dağılıp gitmek","neighbor_only":"Özellikle insanların birbirinden farklı yönlere saçılmasını tek bir tarihsel benzetmeyle anlatır.","neighbor_ref":"root_000663/B007","relation_type":"near_synonym","shared_zone":"İki kol da bir topluluğun birlikten çıkıp farklı yönlere dağılmasını anlatır."}],"source_phrase_ar":"شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)","source_summary":"Kanıt, kalıplaşmış kuş imgesini toplu ayrılma ve dağılma çekirdeğine bağlar; hızla yol alma, ortaklığın bozulması ve güç kaybı bu çekirdeğin bağlamsal sonuçlarıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه شالت نعامتهم وخفت نعامتهم وأضحوا نعاما ونحوها، حيث يدل التعبير على الارتحال أو التفرق أو ذهاب العز أو الهزيمة.","what_is_not_ar":"لا يدخل فيه النعامة الطائر إذا لم تكن في مثل أو كناية، ولا أسماء الأجسام المسماة نعامة."},"support_links":[]},{"boundary":"Yumuşak esiş tek başına yeterli değildir; güney yönü ve nemlilik bu kolun belirleyici sınırlarıdır.","branch_kind":"bare","branch_ref":"root_001525/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"yumuşak esen nemli güney rüzgarı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güney yönünden esen belirli bir rüzgar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Esişi yumuşak, havası nemli ve ıslaklık taşıyan rüzgar niteliği."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yön, esiş biçimi ve nemlilik koşullarının üçünü de açıkça karşılar.","boundary_detail":"Yumuşak esiş tek başına yeterli değildir; güney yönü ve nemlilik bu kolun belirleyici sınırlarıdır.","branch_image_ar":"النعامى ريح لينة","concept_gloss":"yumuşak esen nemli güney rüzgarı","contextual_glosses":[{"applicability":"Rüzgarın yönü ile yumuşak ve nemli hissi birlikte anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güney yönünü ve yumuşak, nemli esiş niteliğini korur."},"facet_ids":["F001","F002"],"text":"yumuşak ve nemli güney yeli","usage_role":"contextual"}],"definition":"Güneyden esen, esişi yumuşak ve taşıdığı hava nemli olan rüzgardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güney yönünden esen belirli bir rüzgar."},{"facet_id":"F002","role":"specialization","statement":"Esişi yumuşak, havası nemli ve ıslaklık taşıyan rüzgar niteliği."}],"identity_rationale":"Kaynak ifadesi bu adı güneyden esen, yumuşak, nemli ve öteki rüzgarlara göre daha ıslak bir yel için ortak biçimde kullanır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yumuşak esen nemli güney rüzgarı"}],"lexicalization_note":"Tanım yalın rüzgar adına aittir ve genel yumuşaklık ya da kuş anlamına genişletilmez.","neighbor_coverage_note":"Tüm rüzgar ve nem adayları incelendi; genel güney rüzgarı ile yönsüz yumuşak esiş arasındaki iki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol genel güney rüzgarının yumuşak ve nemli bir türüdür; komşu kol yönü koruyup esiş niteliğini sınırlamaz.","focus_only":"Güney rüzgarının yumuşak esişini ve belirgin nemliliğini zorunlu özellik olarak taşır.","gloss":"genel güney rüzgarı","neighbor_only":"Güney rüzgarının esmesi, kişiye ulaşması ve onunla ilişkili bulut gibi daha geniş olayları kapsar.","neighbor_ref":"root_000262/B006","relation_type":"near_synonym","shared_zone":"İki kol da güney yönünden gelen rüzgarı doğrudan gösterir."},{"boundary_match":"partial","distinction":"Bu kol yönü ve nemi belirli bir rüzgardır; komşu kol yönsüz yumuşak esiş ile hafif yağmuru aynı alanda toplar.","focus_only":"Güney yönünü ve nemli hava niteliğini belirleyici koşul olarak içerir.","gloss":"hafif yağmur ve yumuşak yel","neighbor_only":"Hafif yağmuru da kapsar ve rüzgar için belirli bir yön şartı koymaz.","neighbor_ref":"root_001602/B007","relation_type":"near_neighbor","shared_zone":"Her iki kol yumuşak ve hafif esen rüzgar niteliğinde buluşur."}],"source_phrase_ar":"النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)","source_summary":"Ortak kanıt rüzgarın güney yönünü, yumuşak esişini ve belirgin nemliliğini aynı hava olayı içinde birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النعامى، وهي ريح الجنوب اللينة أو الأرطب والأبل في الهبوب.","what_is_not_ar":"لا يدخل فيه النعمة العامة ولا النعامة الطائر إلا من جهة الاشتقاق أو التشبيه الذي تذكره المصادر."},"support_links":[]},{"boundary":"Bu kol, başkasına iyilik ulaştırma kolundan ayrıdır; burada belirleyici işlem miktar veya derece artışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001525/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"daha da artırmak veya ileri dereceye götürmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Var olan miktarın üzerine daha fazlasını eklemek."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir eylemi daha ileri dereceye götürüp yoğunlaştırmak."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir maddeyi daha çok işleyerek daha ince öğütmek."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem nicelik artışını hem bir eylemin yoğunluk derecesinin yükseltilmesini kapsar.","boundary_detail":"Bu kol, başkasına iyilik ulaştırma kolundan ayrıdır; burada belirleyici işlem miktar veya derece artışıdır.","branch_image_ar":"زاد وأنعم في الفعل","concept_gloss":"daha da artırmak veya ileri dereceye götürmek","contextual_glosses":[{"applicability":"Sayı, miktar, söz veya yapılan iş üzerine fazlalık eklendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eylemin niteliğini veya incelik derecesini yükseltme yönünü açıkça göstermez.","preserves":"Var olan miktarın üzerine daha fazlasını ekleme yönünü korur."},"facet_ids":["F001"],"text":"biraz daha artırmak","usage_role":"contextual"},{"applicability":"Öğütme işleminin artırılıp maddenin daha ince hale getirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğütme dışındaki genel nicelik ve derece artışlarını dışarıda bırakır.","preserves":"İşlemi yoğunlaştırma ve daha ince sonuç elde etme yönünü korur."},"facet_ids":["F002","F003"],"text":"iyice ince öğütmek","usage_role":"contextual"}],"definition":"Bir miktara daha fazlasını eklemek veya bir işi önceki derecesinin ötesine götürerek daha yoğun ve ileri yapmak demektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Var olan miktarın üzerine daha fazlasını eklemek."},{"facet_id":"F002","role":"specialization","statement":"Bir eylemi daha ileri dereceye götürüp yoğunlaştırmak."},{"facet_id":"F003","role":"example","statement":"Bir maddeyi daha çok işleyerek daha ince öğütmek."}],"identity_rationale":"Kaynak ifadesi bir miktarın üzerine çıkma, bir işi daha ileri dereceye götürme ve özellikle öğütmeyi artırma anlamlarını aynı artış çekirdeğinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"artırdı; daha ileri götürdü"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"onu iyice ince öğüttü"}],"lexicalization_note":"Genel artırma biçimi ile belirli eylem yapısındaki dereceyi yükseltme kullanımı ayrı tutulur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; genel miktar artışı ile sınırı aşan artışa ilişkin iki yakın komşu bu kolun derece yönünü açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol genel fazlalıkta yoğunlaşır; bu kol ise artışın yanında eylemi daha ileri dereceye götürme işlevi taşır.","focus_only":"Bir eylemin derecesini yükseltme ve işi daha yoğun yapma yönünü de kapsar.","gloss":"miktar üzerine ekleme","neighbor_only":"Artışı sayı, bağış veya söz gibi ad alanlarında doğrudan bir fazlalık olarak gösterebilir.","neighbor_ref":"root_000558/B005","relation_type":"near_synonym","shared_zone":"Her iki kol var olan miktar veya düzey üzerine bir fazlalık eklemeyi anlatır."},{"boundary_match":"partial","distinction":"Bu kol bir işi daha ileri yapma kullanımını öne çıkarır; komşu kol ise sınırı aşan veya mali nitelikli fazlalığa uzanır.","focus_only":"Artırmayı bir eylemin uygulanma derecesine ve yoğunluğuna taşıyabilir.","gloss":"artışla sınırı aşma","neighbor_only":"Artışı bir sınırı aşan fazlalık ve belirli mali fazlalık türü olarak da kapsar.","neighbor_ref":"root_000603/B002","relation_type":"near_synonym","shared_zone":"İki kol da bir sayı, miktar veya düzeyin üstüne çıkma çekirdeğinde örtüşür."}],"source_phrase_ar":"فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)","source_summary":"Kanıt, nicelikte fazlalık ekleme ile eylemin derecesini yükseltmeyi aynı artış altında toplar ve daha ince öğütmeyi bunun somut örneği olarak verir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه فعل كذا وأنعم بمعنى زاد، وأنعم في الدق أو الإحسان بمعنى بالغ وزاد، وأنعما في الخبر بمعنى زادا على ذلك.","what_is_not_ar":"لا يدخل فيه الإنعام بمعنى إيصال الإحسان إلا إذا نص السياق على الزيادة والمبالغة."},"support_links":[]},{"boundary":"Yalnız kalma değil, yerin kişiye uygun gelmesi ve bunun ardından orada bulunmayı sürdürme birlikte korunur.","branch_kind":"collocation","branch_ref":"root_001525/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"bir yeri kendine uygun bulup orada kalmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gelinen yerin kişinin durumuna ve isteğine uygun düşmesi."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uygun bulunan yerde kalmak ve yerleşmeyi sürdürmek."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan yer yapısında uygunluk ile kalma sonucunu birlikte karşılar.","boundary_detail":"Yalnız kalma değil, yerin kişiye uygun gelmesi ve bunun ardından orada bulunmayı sürdürme birlikte korunur.","branch_image_ar":"موافقة المكان وطيب المقام","concept_gloss":"bir yeri kendine uygun bulup orada kalmak","contextual_glosses":[{"applicability":"Bir yerin kişiye uygun gelmesi ve kişinin orada kalması birlikte anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerin uygun gelmesini ve bunun ardından orada kalmayı eksiksiz korur."},"facet_ids":["F001","F002"],"text":"orası bana uydu, yerleştim","usage_role":"contextual"}],"definition":"Bir yere geldikten sonra o yeri kendine uygun ve hoş bulup orada kalmak veya yerleşmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gelinen yerin kişinin durumuna ve isteğine uygun düşmesi."},{"facet_id":"F002","role":"associated_use","statement":"Uygun bulunan yerde kalmak ve yerleşmeyi sürdürmek."}],"identity_rationale":"Kaynak ifadesi bir yere gelme, o yerin kişiye uygun düşmesi ve kişinin orada kalması aşamalarını aynı yerleşme olayında açıkça bağlar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir yere geldi, orayı uygun bulup kaldı"}],"lexicalization_note":"Tanım yalnız kişinin bir yere gelmesiyle kurulan yapıya aittir ve yalın köke genel yerleşme anlamı yüklemez.","neighbor_coverage_note":"Bütün yer ve kalış adayları değerlendirildi; uygunluk koşulunu genel ve yalın kalma anlamlarından ayıran iki karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol kalmayı yerin kişiye uygun gelmesine bağlar; komşu kol ise uygunluk aramadan kalışın süresini ve türlerini anlatır.","focus_only":"Kalınan yerin kişiye uygun ve hoş gelmesi koşulunu içerir.","gloss":"bir yerde kalıp yerleşmek","neighbor_only":"Uzun süre kalmayı, yabancının ikametini ve bazı özel kalma durumlarını uygunluk şartı olmadan kapsar.","neighbor_ref":"root_000211/B001","relation_type":"near_synonym","shared_zone":"İki kol da kişinin bir yerde bulunmayı sürdürmesi ve orada yerleşmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu kol yalnız kalma sonucunu verir; bu kol ise önce yerin uygun gelmesini, sonra orada kalmayı anlatır.","focus_only":"Yere gelme ve o yeri kendine uygun bulma aşamalarını zorunlu kılar.","gloss":"bir yerde kalmak","neighbor_only":"Bir yerde bulunmayı sürdürmeyi özel bir fiille doğrudan anlatır, uygunluk değerlendirmesi taşımaz.","neighbor_ref":"root_000168/B016","relation_type":"near_synonym","shared_zone":"Her iki kol kişinin belirli bir yerde kalması sonucunda örtüşür."}],"source_phrase_ar":"أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)","source_summary":"Kanıt, kişinin bir yere varmasını, yerin ona uygun gelmesini ve bu uygunluğun sonucu olarak orada kalmasını tek bir yapıya bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أتيت أرضا فتنعمتني أو فنعمتني، إذا وافقت الشخص وأقام بها أو طاب له النزول.","what_is_not_ar":"لا يدخل فيه النعمة العامة إلا إن كان المقصود طيب المقام بهذا التعبير، ولا المشي على القدم إلى شخص."},"support_links":[]},{"boundary":"Bineksiz yönelme, ayakların kullanılması ve hafif yürüme aynı kalıbın tek bir zorunlu sonucu gibi birleştirilmemelidir.","branch_kind":"collocation","branch_ref":"root_001525/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"birine yaya gitmek ve ayakları yürüyerek kullanmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye bineğe binmeden, kendi ayaklarıyla gitmek veya onu aramak."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayakları yürüyüşte kullanarak yormak veya eskitmek."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hafif ve yumuşak adımlarla yürümek."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan yapılarda bineksiz yönelme ile ayakları işletme çekirdeğini karşılar.","boundary_detail":"Bineksiz yönelme, ayakların kullanılması ve hafif yürüme aynı kalıbın tek bir zorunlu sonucu gibi birleştirilmemelidir.","branch_image_ar":"المشي على القدم وابتذالها","concept_gloss":"birine yaya gitmek ve ayakları yürüyerek kullanmak","contextual_glosses":[{"applicability":"Bir kişiye bineksiz gidildiği veya o kişi yürüyerek arandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ayakları eskitme ve hafif yürüme kullanımlarını dışarıda bırakır.","preserves":"Bir kişiye kendi ayaklarıyla yönelme ve onu arama yönünü korur."},"facet_ids":["F001"],"text":"onu yaya gidip aradı","usage_role":"contextual"},{"applicability":"Uzun veya sık yürüyüşle ayakların kullanılıp yıpratılması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişiye yaya yönelme ve hafif adımlarla yürüme yönlerini dışarıda bırakır.","preserves":"Ayakları yürüyüşte kullanma ve eskitme yönünü korur."},"facet_ids":["F002"],"text":"ayaklarını yürümekle eskitti","usage_role":"contextual"}],"definition":"Belirli yapılarda birine bineksiz olarak yaya gitmek veya onu yürüyerek aramak; ayrıca ayakları yürümekle kullanıp eskitmek ya da hafif adımlarla yürümektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye bineğe binmeden, kendi ayaklarıyla gitmek veya onu aramak."},{"facet_id":"F002","role":"associated_use","statement":"Ayakları yürüyüşte kullanarak yormak veya eskitmek."},{"facet_id":"F003","role":"source_variant","statement":"Hafif ve yumuşak adımlarla yürümek."}],"identity_rationale":"Kaynak ifadesi birine bineksiz gitme ile ayakları yürüyüşte kullanıp eskitme yönünü açıkça destekler; hafif yürüme ise buna bağlı fakat daha dar bir kullanım olarak verilir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"ona yaya gitti veya onu yürüyerek aradı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayaklarını yürümekle eskitti; hafif yürüdü"}],"lexicalization_note":"Tanım yalnız yaya gitme ve ayakları kullanma yapılarıyla sınırlıdır; yalın biçime genel yürüyüş anlamı verilmez.","neighbor_coverage_note":"Adayların tamamı incelendi; genel yaya olma ile yürüyüşün ayakta doğurduğu aşınma bu kalıpların sınırını en açık gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu kol belirli yapılarda hedef kişiye yaya yönelir ve ayak kullanımını öne çıkarır; komşu kol yaya olma durumunu genel olarak adlandırır.","focus_only":"Belirli bir kişiye yönelme veya onu arama ve ayakları kullanıp eskitme yapılarını içerir.","gloss":"bineksiz olarak yürümek","neighbor_only":"Yayanın binici karşıtı oluşunu, bineksiz kalmayı ve yürümeye dayanıklılığı genel adlarla kapsar.","neighbor_ref":"root_000546/B003","relation_type":"near_synonym","shared_zone":"İki kol da bir taşıta binmeden kendi ayakları üzerinde yol almayı anlatır."},{"boundary_match":"partial","distinction":"Bu kol yürüme ve ayakları işletme eylemine odaklanır; komşu kol bu eylemin bedensel aşınma sonucunu adlandırır.","focus_only":"Yürüme eylemini, hedef kişiye yönelmeyi ve ayakları bilinçli biçimde kullanmayı anlatır.","gloss":"çok yürümekten ayağın aşınması","neighbor_only":"Çok yürümekten ayağın, toynağın veya tabanın incelip aşınmış sonucunu anlatır.","neighbor_ref":"root_000344/B006","relation_type":"near_neighbor","shared_zone":"Her iki kol yürüyüşün ayak üzerinde oluşturduğu kullanım ve yıpranma alanında buluşur."}],"source_phrase_ar":"تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)","source_summary":"Kanıt, bir kişiye yaya yönelmeyi ayakların işletilmesi düşüncesiyle açıklar; ayakları eskitme ve hafif yürüme bunun ayrı kullanımları olarak yer alır.","sources":["MQ","TA","MU"],"what_is_ar":"يدخل فيه تنعمت فلانا إذا أتيته على غير دابة أو طلبته ماشيا، وتنعم القدمين أي ابتذلهما، وما قرب منه من المشي الخفيف.","what_is_not_ar":"لا يدخل فيه موافقة الأرض للشخص، ولا نعومة العيش إلا إذا كان النص عن المشي أو القدم."},"support_links":[]},{"boundary":"Göz sevinci yapısı genel mutluluk sözünden ve sıradan bağış anlamından ayrı, yapıya bağlı bir iyi dilektir.","branch_kind":"collocation","branch_ref":"root_001525/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","surface_ar":"نَّاعِمَةٌ"}],"gloss":"birini göz sevinci saymak veya bunun için dua etmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin görülmesinden doğan göz sevinci, dinginlik ve hoşnutluk."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin gözlere sevinç vermesi için söylenen dua, iyi dilek veya onurlandırma sözü."}}],"root_ar":"ن ع م","root_id":"root_001525","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız göz sözüyle kurulan sevinç, hoşnutluk ve iyi dilek yapılarını karşılar.","boundary_detail":"Göz sevinci yapısı genel mutluluk sözünden ve sıradan bağış anlamından ayrı, yapıya bağlı bir iyi dilektir.","branch_image_ar":"نعم الله بك عينا وقرة العين","concept_gloss":"birini göz sevinci saymak veya bunun için dua etmek","contextual_glosses":[{"applicability":"Bir kişinin görülmesinden doğan sevincin ve hoşnutluğun adlandırıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu durumun dua veya iyi dilek olarak söylenmesi işlevini karşılamaz.","preserves":"Kişinin göz için sevinç ve hoşnutluk kaynağı oluşunu korur."},"facet_ids":["F001"],"text":"gözümün sevinci","usage_role":"contextual"},{"applicability":"Bir kişi için göz hoşnutluğu ve sevinç dilenen dua veya iyi dilek bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen göz sevinci dileğini ve dua işlevini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"gözlere sevinç versin","usage_role":"contextual"}],"definition":"Birini göz için sevinç, dinginlik ve hoşnutluk kaynağı saymak veya onun böyle bir sevinç vermesi için dua ve iyi dilekte bulunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin görülmesinden doğan göz sevinci, dinginlik ve hoşnutluk."},{"facet_id":"F002","role":"associated_use","statement":"Bir kişinin gözlere sevinç vermesi için söylenen dua, iyi dilek veya onurlandırma sözü."}],"identity_rationale":"Kaynak ifadesi bir kişinin göz için sevinç ve hoşnutluk kaynağı sayılmasını, ayrıca bunun dua veya iyi dilek olarak söylenmesini ortak biçimde destekler.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"Tanrı seni gözlere sevinç kaynağı kılsın"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"göz sevinci ve hoşnutluğu"}],"lexicalization_note":"Tanım yalnız göz sözüyle kurulan kanıtlanmış yapılara aittir ve yalın köke genel sevinç anlamı yüklemez.","neighbor_coverage_note":"Tüm sevinç ve iyi dilek adayları değerlendirildi; göz dinginliğiyle en yakın anlam ve olay üzerine kutlama arasındaki iki sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu kol gözün sevinme durumunu genel olarak verir; bu kol ise aynı durumu belirli bir kişi için dua ve iyi dilek yapısına bağlar.","focus_only":"Belirli bir kişiyi göz sevinci sayan çeşitli iyi dilek ve onurlandırma yapılarını kapsar.","gloss":"gözün sevinip dinginleşmesi","neighbor_only":"Gözün sakinleşmesini ve gözyaşının dinmesini genel bir sevinme durumu olarak anlatır.","neighbor_ref":"root_001215/B002","relation_type":"near_synonym","shared_zone":"İki kol da gözün bir kişi veya durum karşısında sevinç ve dinginlik bulmasını anlatır."},{"boundary_match":"partial","distinction":"Bu kol göz hoşnutluğu imgesiyle kişiyi sevinç kaynağı sayar; komşu kol belirli bir iyi olay üzerine kutlama yapar.","focus_only":"Bir kişinin kendisini göz sevinci ve hoşnutluk kaynağı olarak sunar.","gloss":"iyilik karşısında kutlama ve iyi dilek","neighbor_only":"Yeni bir iyilik veya göreve kavuşan kişiye doğrudan kutlama sözü ve esenlik dileği yöneltir.","neighbor_ref":"root_001604/B005","relation_type":"near_neighbor","shared_zone":"Her iki kol bir kişiye yönelik sevinç, değer verme ve iyi dilek sözleri alanındadır."}],"source_phrase_ar":"نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)","source_summary":"Ortak kanıt, gözün hoşnut olup sevinmesini temel alır ve bu durumu bir kişi için dua, iyi dilek ve değer verme sözüne dönüştüren yapıları birlikte gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نعم الله بك عينا، ونعمك عينا، ونعمى عين، ونعمة عين، ونعم عين، ونعام عين، بمعنى قرة العين والإكرام أو الدعاء بذلك.","what_is_not_ar":"لا يدخل فيه نعم الجواب، ولا نعم المدح، ولا النعمة العامة إلا إذا وردت في صيغة العين."},"support_links":[]},{"boundary":"Bu dal yön, toplumsal itibar veya günün başlangıcı anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B001","candidate_links":[{"candidate_id":"cand_5ad5c2ade7ac3211c70d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüz ve bir şeyin öne bakan yanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlılarda yüz denen organı ve yüz bölgesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin bakana dönük önünü veya görünen dış yanını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı yüzünü ve nesnelerin bakana dönük ön ya da dış yanını birlikte karşılayan genel açıklamadır.","boundary_detail":"Bu dal yön, toplumsal itibar veya günün başlangıcı anlamlarını içermez.","branch_image_ar":"الوجه والمستقبل","concept_gloss":"yüz ve bir şeyin öne bakan yanı","contextual_glosses":[{"applicability":"İnsan veya başka bir canlının yüz bölgesinden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının yüz organı anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"yüz","usage_role":"general"},{"applicability":"Bir nesnenin bakana dönük görünen yanı kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin karşıya dönük ön yanı anlamını korur."},"facet_ids":["F002"],"text":"ön yüz","usage_role":"contextual"}],"definition":"İnsanın ya da başka bir varlığın yüzü; daha genel olarak bir şeyin bakana dönük, önde bulunan veya dışarıdan görünen yanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlılarda yüz denen organı ve yüz bölgesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir nesnenin bakana dönük önünü veya görünen dış yanını belirtir."}],"identity_rationale":"Kaynak ifadesi, insanın ve başka varlıkların yüzünü, ayrıca bir şeyin bakana dönük ön veya dış yanını ortak bir karşıya dönüklük çekirdeğinde birleştirir. Verilen dal kimliği bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yüz; bir şeyin öne bakan veya görünen yanı"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kötü bir yüz ifadesiyle bakmak"}],"lexicalization_note":"Tanım, biçimin yüz ve ön yan anlamını kapsar; kötü bakış bildiren kalıp yalnız kendi sözlüksel karşılığında tutulur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; insan yüzü ve yön dalları sınırı en çok aydınlatan iki karşılaştırma olduğu için diğerleri yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal insan yüzüyle sınırlıdır; odak dal ise aynı karşıya dönüklük ilişkisini başka canlılara ve nesnelerin ön yüzüne de taşır.","focus_only":"Nesnelerin öne bakan veya görünen yanı da bu dalın kapsamındadır.","gloss":"insan yüzü","neighbor_only":null,"neighbor_ref":"root_000383/B012","relation_type":"near_synonym","shared_zone":"İki dal da insanın yüz bölgesini adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal bir varlığın yüzünü ya da ön yanını adlandırır; komşu dal ise uzamsal yönü, hedefi ve yönelme işlemini anlatır.","focus_only":"Karşıdan görülen somut yüz veya ön yan bu dala özgüdür.","gloss":"ön yüz ile yön","neighbor_only":"Gidilecek yön, hedef ve bir şeyi o yöne sevk etme komşu dala özgüdür.","neighbor_ref":"root_001630/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da karşıya veya ileriye dönüklük ilişkisi bulunur."}],"source_phrase_ar":"الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)","source_summary":"Kaynaklar yüz organında ve bir şeyin karşıya dönük ön yanında birleşir; nesneye genişleyen kullanım, bakana dönük olma ilişkisini korur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجارحة؛ وجه الإنسان وغيره؛ مستقبل الشيء وظاهره وما يقابل الناظر","what_is_not_ar":"ليس الجهة المقصودة ولا الجاه ولا صدر النهار"},"support_links":["sup_cd28e438ad3004719364"]},{"boundary":"Yüz yüze karşılaşma ve toplumsal mevki bu yön ve hedef dalının dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B002","candidate_links":[{"candidate_id":"cand_9ae64b59e50857e0b0f3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yön ve hedef; o yöne sevk etme veya yolu belli etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönülen veya gidilen yönü, tarafı ve hedefi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi tek bir yöne çevirmeyi, göndermeyi veya o yöne gitmeyi belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli kalıplarda çakılın rüzgarla sürülmesini ve yolun yürünerek belirginleşmesini anlatır."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yön adını, yönelme eylemini ve kaynakta belirtilen yapı bağımlı işlemleri birlikte özetler.","boundary_detail":"Yüz yüze karşılaşma ve toplumsal mevki bu yön ve hedef dalının dışında kalır.","branch_image_ar":"الجهة والوجهة","concept_gloss":"yön ve hedef; o yöne sevk etme veya yolu belli etme","contextual_glosses":[{"applicability":"Bir yerin, tarafın veya ulaşılmak istenen hedefin adı olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yön ve hedef olma çekirdeğini korur."},"facet_ids":["F001"],"text":"yönelinen yön veya hedef","usage_role":"general"},{"applicability":"Bir şeyi belirli bir tarafa çevirmek veya göndermek söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi belirli bir yöne sevk etme işlemini korur."},"facet_ids":["F002"],"text":"yöneltmek","usage_role":"contextual"}],"definition":"Bir şeyin dönüldüğü yön, taraf veya hedef ile bir şeyi o yöne çevirmek ya da göndermektir. Belirli kuruluşlarda rüzgarın çakılı sürmesini ve bir yolu yürüyerek izini görünür kılmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönülen veya gidilen yönü, tarafı ve hedefi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi tek bir yöne çevirmeyi, göndermeyi veya o yöne gitmeyi belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli kalıplarda çakılın rüzgarla sürülmesini ve yolun yürünerek belirginleşmesini anlatır."}],"identity_rationale":"Kaynak ifadesi yön ve hedef adlarını, bir şeyi belirli bir yöne gönderme veya çevirme eylemini, rüzgarın çakılı sürmesini ve yürüyerek yolu belli etme kullanımını birlikte verir. Dal çerçevesi bu çekirdek ile yapı bağımlı uzantıları doğru ayırmaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yön, taraf"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yönelinen yön veya hedef"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir yöne çevirmek veya göndermek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tek bir yöne çevrilmiş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye doğru yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"rüzgarın çakılı bir yöne sürüklemesi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yolu yürüyerek izini belirginleştirmek"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak"}],"lexicalization_note":"Yön ve hedef çekirdeği ile gönderme, sürükleme ve yolu belirginleştirme gibi belirli kuruluşlara bağlı kullanımlar ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yönelme ve özel ibadet yönü, dalın kapsamını en açık biçimde sınırlayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yönün ve hedefin kendisini de adlandırır ve bazı özel sevk etme kalıplarını içerir; komşu dal esas olarak bir şeyi amaçlayıp ona gitmeyi anlatır.","focus_only":"Durağan yön adı, nesneyi sevk etme ve yolu yürüyerek belli etme kapsamı vardır.","gloss":"yön ile yönelme","neighbor_only":"Bir şeyi amaçlayıp ona gitme eylemi komşu dalda daha merkezi ve geneldir.","neighbor_ref":"root_001230/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir hedefe doğru dönme veya gitme durumunu kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel yön ve hedef kavramıdır; komşu dal bunu belirli bir ibadet yerleşimine özgü ad olarak sınırlar.","focus_only":"Her türlü yön, hedef ve yöneltme işlemi bu dalda yer alabilir.","gloss":"genel yön ile ibadet yönü","neighbor_only":"İbadet sırasında dönülen özel yön komşu dalın belirleyici sınırıdır.","neighbor_ref":"root_001198/B005","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin dönüp karşısına aldığı yönü belirtebilir."}],"source_phrase_ar":"الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)","source_summary":"Kaynaklar yön, hedef ve yönelme çekirdeğinde birleşir; gönderme, rüzgarla sürükleme ve yolun yürünerek belli edilmesi bu çekirdeğe bağlı özel gerçekleşmelerdir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجهة والنحو والقبلة والمقصد؛ جعل الشيء أو السير على جهة؛ سوق الشيء في طريق؛ بيان الطريق بالسلوك","what_is_not_ar":"ليس مجرد مقابلة الوجه للوجه ولا منزلة الجاه"},"support_links":["sup_104a96babe00c0572e21"]},{"boundary":"Bu dal yalnızca yön bildirmez; iki tarafın karşılıklı konumunu veya doğrudan karşılaşmasını gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"karşı karşıya gelme ve doğrudan yüzüne söyleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki tarafın birbirinin karşısına gelmesini veya karşılıklı durmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye iyi ya da kötü bir sözü doğrudan yüzüne söylemeyi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel karşılıklı konumu ve bunun sözlü karşılaşmaya uzanan özel kullanımını birlikte karşılar.","boundary_detail":"Bu dal yalnızca yön bildirmez; iki tarafın karşılıklı konumunu veya doğrudan karşılaşmasını gerektirir.","branch_image_ar":"المواجهة والتقابل","concept_gloss":"karşı karşıya gelme ve doğrudan yüzüne söyleme","contextual_glosses":[{"applicability":"Kişilerin veya şeylerin karşılıklı konuma gelmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafın karşılıklı konumlanmasını korur."},"facet_ids":["F001"],"text":"yüz yüze gelmek","usage_role":"general"},{"applicability":"Bir sözün kişiye doğrudan ve karşısında söylenmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlü karşılaşma ve doğrudanlık koşulunu korur."},"facet_ids":["F002"],"text":"yüzüne söylemek","usage_role":"contextual"}],"definition":"İki kişi veya şeyin birbirinin karşısında bulunması ya da yüz yüze gelmesidir; bir kişiye sözü doğrudan yüzüne söylemek de bu karşılaşmanın özel bir biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki tarafın birbirinin karşısına gelmesini veya karşılıklı durmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye iyi ya da kötü bir sözü doğrudan yüzüne söylemeyi belirtir."}],"identity_rationale":"Kaynak ifadesi iki yüzün veya iki şeyin birbirinin karşısına gelmesini, bir kişinin karşılanmasını ve sözle doğrudan karşı karşıya gelmeyi açıkça bir arada verir. Dalın karşılaşma ve karşılıklı konumlanma çerçevesi bu içeriğe uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkmak, onunla yüz yüze gelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"karşılaşma, yüzleşme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"karşında, tam karşı tarafta"}],"lexicalization_note":"Karşılıklı konum çekirdeği korunur; yüz yüze gelme ve sözle karşısına çıkma, ilgili biçim ve kalıplara bağlı anlatılır.","neighbor_coverage_note":"Tüm adaylar incelendi; geniş karşıt konum alanı ile karşılıklı görünme dalı, fiziksel ve sözlü karşılaşma sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iki tarafın doğrudan karşılaşmasını ve iletişimsel yüzleşmeyi öne çıkarır; komşu dal karşı, ön ve yön ilişkilerini daha geniş uzamsal kapsamda işler.","focus_only":"Yüz yüze gelme ve sözü doğrudan birinin yüzüne söyleme belirgindir.","gloss":"yüz yüze karşılaşma","neighbor_only":"Ön ve arka karşıtlığı ile dağ veya arazi yüzü gibi daha geniş uzamsal kapsam vardır.","neighbor_ref":"root_001198/B001","relation_type":"near_neighbor","shared_zone":"İki dal da şeylerin birbirine karşı konumlanmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yüz yüze gelmeyi kişiler arası sözlü karşılaşmaya kadar taşır; komşu dal karşılıklı görünür olma durumuna odaklanır.","focus_only":"Sözlü yüzleşme ve bir kişiye doğrudan hitap etme kapsamı vardır.","gloss":"karşılıklı görünme","neighbor_only":"Toplulukların, evlerin veya ateşlerin birbirini görecek konumda olması özellikle belirtilir.","neighbor_ref":"root_000531/B004","relation_type":"near_synonym","shared_zone":"İki dal da iki tarafın birbirini görecek biçimde karşılaşmasını anlatır."}],"source_phrase_ar":"واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)","source_summary":"Kaynaklar karşılıklı konumlanma ve yüz yüze gelme üzerinde birleşir; sözle doğrudan karşılaşma bu temel ilişkinin iletişim alanındaki özel kullanımıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"مقابلة وجه بوجه؛ استقبال الشخص أو الشيء؛ الوجاه والتجاه وما يكون قبالة غيره؛ المواجهة بالكلام","what_is_not_ar":"ليس مطلق الجهة ولا القصد الباطن"},"support_links":[]},{"boundary":"Burada yüz, varlığın kendisini temsil eden aktarmalı bir anlatımdır; bağımsız ve kesin bir yalın anlam varsayılmaz.","branch_kind":"unresolved","branch_ref":"root_001630/B004","candidate_links":[{"candidate_id":"cand_cff8a4865edae7f185d4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüzün varlığın kendisini temsil etmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzün, yorum yoluyla varlığın kendisi veya bütün kişi yerine kullanılmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yüz sözünün bağlama göre bütün kişi veya varlık yerine yorumlandığı kullanımlarda geçerlidir.","boundary_detail":"Burada yüz, varlığın kendisini temsil eden aktarmalı bir anlatımdır; bağımsız ve kesin bir yalın anlam varsayılmaz.","branch_image_ar":"الوجه عن الذات","concept_gloss":"yüzün varlığın kendisini temsil etmesi","contextual_glosses":[{"applicability":"Yüzün bütün kişiyi temsil ettiği kabul edilen bağlamı açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzden bütün kişiye kurulan temsil ilişkisini bağlam içinde korur."},"facet_ids":["F001"],"text":"kişinin kendisi","usage_role":"explanatory"}],"definition":"Yüz sözünün, bazı bağlamlarda bir varlığın kendisini veya kişiyi bütünüyle temsil edecek biçimde kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzün, yorum yoluyla varlığın kendisi veya bütün kişi yerine kullanılmasını belirtir."}],"identity_rationale":"Kaynak ifadesi yüzün bazen bir varlığın kendisi yerine kullanılabildiğini bildirir, ancak bunu kesin ve bağımsız bir temel anlam olarak değil, aktarıma dayalı bir yorum olarak sunar. Dal korunabilir, fakat bu yorum niteliği tanımın sınırı olmalıdır.","lexicalization_note":"Sözlüksel birim türü çözülmemiştir; tanım yalnız kaynakta ihtiyatla verilen yüzün varlığın kendisini temsil etmesi yorumuyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan varlığın kendisini adlandıran dal, bu yorumun aktarmalı sınırını göstermek için yeterlidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bu anlamı yüzün bütünü temsil etmesi yoluyla ve ihtiyatlı bir yorum olarak kurar; komşu dal ise varlığın kendisini doğrudan adlandırır.","focus_only":"Yüz sözünden bütün varlığa giden aktarmalı ve yoruma bağlı kullanım vardır.","gloss":"varlığın kendisi","neighbor_only":"Varlığın kendisini doğrudan adlandırma ve pekiştirme kullanımları vardır.","neighbor_ref":"root_001533/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya şeyin bütün varlığını gösterebilir."}],"source_phrase_ar":"ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)","source_summary":"Kaynaklar yüzün varlığın kendisi yerine yorumlanabileceğini aktarır; anlatımın aktarmalı ve ihtiyatlı niteliği bağımsız bir temel anlam kurulmasını engeller.","sources":["MQ","MU"],"what_is_ar":"التعبير بالوجه عن الذات أو الشخص نفسه عند من يفسره بذلك","what_is_not_ar":"ليس الجارحة وحدها ولا طلب الجاه"},"support_links":["sup_2b6d1ab8539602b9597e"]},{"boundary":"Mekansal yön adı bu dalın çekirdeği değildir; esas olan bir hedefi amaç edinip ona yönelmektir.","branch_kind":"unresolved","branch_ref":"root_001630/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"amaç edinip yönelme; ibadette içtenlikle bağlanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefi amaç edinip ona yönelmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İbadet bağlamında amacı yalnız yaratıcıya yöneltmeyi ve içten bağlılığı belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel amaçlı yönelişi ve ibadet bağlamındaki yalnızca yaratıcıya dönük içten yönelişi birlikte açıklar.","boundary_detail":"Mekansal yön adı bu dalın çekirdeği değildir; esas olan bir hedefi amaç edinip ona yönelmektir.","branch_image_ar":"القصد والتوجه","concept_gloss":"amaç edinip yönelme; ibadette içtenlikle bağlanma","contextual_glosses":[{"applicability":"Bir hedefin bilinçli olarak seçilip ona doğru yönelinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedef seçme ve ona yönelme ilişkisini korur."},"facet_ids":["F001"],"text":"amaç edinip yönelmek","usage_role":"general"},{"applicability":"İbadetin yalnız yaratıcıya yöneltilmesi ve içten bağlılık vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İbadette tek hedefe yönelme ve içtenlik koşulunu korur."},"facet_ids":["F002"],"text":"kendini içtenlikle adamak","usage_role":"contextual"}],"definition":"Bir şeyi amaç edinmek ve ona yönelmek; ibadet bağlamında ise yönelişi yalnız yaratıcıya ayırıp içtenlikle ona bağlanmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefi amaç edinip ona yönelmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"İbadet bağlamında amacı yalnız yaratıcıya yöneltmeyi ve içten bağlılığı belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeye doğru yönelme ve amacı kaybetme örneklerini, ayrıca ibadeti yalnız yaratıcıya yöneltme ve bunu amaç edinme anlatımlarını verir. Dalın niyet ve yöneliş çerçevesi bu ortak amaç çekirdeğini korur.","lexicalization_note":"Birim türü çözülmemiştir; tanım, kaynakta verilen amaç edinme ve bağlama bağlı içten yöneliş anlamlarıyla sınırlı tutulur.","neighbor_coverage_note":"Adayların tamamı incelendi; genel amaçlama dalı ile aynı kökün yön dalı, niyet ve mekan ayrımını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin hedefini ve niyetli yönelişini anlatır; komşu dal ise yönü, hedef yerini ve yöneltme işlemini adlandırır.","focus_only":"Niyet, amaç edinme ve içten yöneliş bu dala özgüdür.","gloss":"amaç ile yön","neighbor_only":"Yönün veya tarafın kendisi ile nesneyi o yöne sevk etme komşu dala özgüdür.","neighbor_ref":"root_001630/B002","relation_type":"near_neighbor","shared_zone":"Bir hedefe doğru dönme düşüncesi iki dalın kesiştiği alandır."}],"source_phrase_ar":"وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)","source_summary":"Kaynaklar amaç edinme ve yönelme çekirdeğini paylaşır; ibadet anlatımları bu yönelişi yalnız yaratıcıya ayırma ve içtenlik koşuluyla özelleştirir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"القصد والمقصد؛ التوجه إلى الشيء أو إلى الله؛ إسلام الوجه وإقامته وإرادة وجه الله على تفسير الإخلاص والتوجه","what_is_not_ar":"ليس الذات على تفسيرها ولا الجاه بين الناس"},"support_links":[]},{"boundary":"Buradaki önde olma fiziksel ön yüz değil, toplumsal mevki, saygınlık ve önderliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"toplumsal itibar, yüksek mevki ve önde gelen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin başkaları yanındaki toplumsal mevki, değer ve saygınlığını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun önderini veya bir yerin seçkin ve önde gelen kişilerini belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin saygın konumunu hem de topluluğun önder veya ileri gelenlerini kapsayan açıklamadır.","boundary_detail":"Buradaki önde olma fiziksel ön yüz değil, toplumsal mevki, saygınlık ve önderliktir.","branch_image_ar":"الوجاهة والجاه","concept_gloss":"toplumsal itibar, yüksek mevki ve önde gelen kişi","contextual_glosses":[{"applicability":"Bir kişinin toplumsal konumu ve başkaları yanındaki değeri anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişisel saygınlık ve yüksek mevki anlamını korur."},"facet_ids":["F001"],"text":"itibarlı ve yüksek mevkili","usage_role":"general"},{"applicability":"Bir topluluğun veya yerleşimin önde gelen seçkin kişileri anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk içinde önder ve seçkin kişiler anlamını korur."},"facet_ids":["F002"],"text":"ileri gelenler","usage_role":"contextual"}],"definition":"Bir kişinin topluluk içinde sahip olduğu yüksek mevki, değer ve saygınlıktır; ayrıca bir topluluğun önderini veya bir yerin önde gelen kişilerini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin başkaları yanındaki toplumsal mevki, değer ve saygınlığını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun önderini veya bir yerin seçkin ve önde gelen kişilerini belirtir."}],"identity_rationale":"Kaynak ifadesi kişinin toplulukta veya yönetici yanında sahip olduğu mevki ve değeri, ayrıca topluluğun ya da yerleşimin önde gelenlerini açıkça birlikte verir. Dalın itibar ve önderlik çerçevesi bu toplumsal kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"topluluğun önderi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yerleşimin ileri gelenleri"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"itibarlı, yüksek mevkili"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"toplumsal itibar ve mevki"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"itibarlı ve yüksek mevkili olmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu itibarlı ve yüksek mevkili kılmak"}],"lexicalization_note":"Toplumsal mevki çekirdeği ile önde gelen kişi ve topluluk ileri gelenleri bildiren kalıplar ayrı ama bağlantılı biçimde tanımlanır.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel yücelik ile yakınlıktan doğan mevki, toplumsal itibarın iki temel sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal toplumsal mevkiyi ve bu mevkiyi taşıyan önder kişileri adlandırır; komşu dal daha genel yücelik ve şeref alanını kapsar.","focus_only":"Topluluk önderi ve bir yerin ileri gelenleri gibi kişi adlandırmaları vardır.","gloss":"itibar ve yücelik","neighbor_only":"Genel yücelik, şeref ve derece yüksekliği daha geniş biçimde yer alır.","neighbor_ref":"root_001042/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin yüksek değeri ve şerefli konumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal toplum içindeki itibar ve önderliği anlatır; komşu dal birine yakın bulunmaktan doğan derece ve gözde olma ilişkisini öne çıkarır.","focus_only":"Önderlik, seçkinlik ve yüksek toplumsal değer bu dala özgüdür.","gloss":"mevki ile yakınlık","neighbor_only":"Bir başkasına yakınlık, onun yanındaki derece ve gözde olma komşu dala özgüdür.","neighbor_ref":"root_000639/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişinin başkaları yanındaki değerli konumunu gösterebilir."}],"source_phrase_ar":"وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)","source_summary":"Kaynaklar toplumsal mevki ve değer anlamında birleşir; önder ve ileri gelenler anlatımı bu mevkinin kişiler veya topluluk içindeki taşıyıcılarını adlandırır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الوجاهة؛ الجاه والمنزلة والقدر؛ وجه القوم ووجوه البلد أي أشرافهم وسادتهم","what_is_not_ar":"ليس الجارحة ولا الجهة المكانية"},"support_links":[]},{"boundary":"Anlam yalnız günün ilk bölümüyle ilgilidir; genel başlangıç veya üstünlük anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001630/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"günün başı, ilk saatleri","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günün başlangıcını ve ilk bölümünü belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız günün başlangıcını bildiren kaynakta verilen zaman kalıbı için geçerlidir.","boundary_detail":"Anlam yalnız günün ilk bölümüyle ilgilidir; genel başlangıç veya üstünlük anlamına genişletilmez.","branch_image_ar":"وجه النهار وصدره","concept_gloss":"günün başı, ilk saatleri","contextual_glosses":[{"applicability":"Bir olayın günün başlangıcında gerçekleştiğini doğal akışta belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün başlangıcındaki zaman konumunu korur."},"facet_ids":["F001"],"text":"günün erken saatlerinde","usage_role":"contextual"}],"definition":"Günün ilk bölümü, yani günün başlangıcıdır; anlam yalnız bu zaman bildiren kuruluş içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günün başlangıcını ve ilk bölümünü belirtir."}],"identity_rationale":"Kaynak ifadesi yalnız günün başını ve ilk bölümünü bildiren belirli bir kalıbı destekler. Geçici çerçevedeki her şeyin başlangıcı veya en değerli görünen yanı biçimindeki genelleme kaynak ifadesinde yer almadığından dal bu kalıpla sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"günün başı, ilk saatleri"}],"lexicalization_note":"Tanım yalnız günün başlangıcını bildiren sabit kuruluşa bağlıdır ve yalın bir kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar incelendi; sabah vakti ve genel başlangıç dalları, kalıbın zamanla sınırlı kapsamını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kuruluşla günün başını adlandırır; komşu dal sabah vaktini ve o vakitte yapılan erken hareketleri daha geniş biçimde kapsar.","focus_only":"Belirli bir kalıp yalnız günün ilk bölümünü adlandırır.","gloss":"günün başı ile sabah","neighbor_only":"Sabah vakti yanında erken çıkma, erken yol alma ve bir işe çabuk davranma eylemleri de vardır.","neighbor_ref":"root_000143/B001","relation_type":"near_synonym","shared_zone":"İki dal da günün erken bölümünü zaman olarak gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal günün başıyla sınırlı bir zaman kalıbıdır; komşu dal başlangıç anlamını farklı varlık ve süreçlere geneller.","focus_only":"Yalnız günün başlangıcına bağlı zaman anlamı vardır.","gloss":"günün başı ile genel başlangıç","neighbor_only":"Herhangi bir şeyin başlangıcı ile bitki ve ayın ilk görünümü de kapsanır.","neighbor_ref":"root_001078/B005","relation_type":"near_neighbor","shared_zone":"Günün ilk bölümü, genel başlangıç düşüncesiyle kesişir."}],"source_phrase_ar":"وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)","source_summary":"Kaynaklar belirli zaman kalıbını günün başı veya ilk bölümü olarak açıklar ve daha genel bir başlangıç anlamı vermez.","sources":["JA","TA","MU"],"what_is_ar":"وجه النهار؛ صدر النهار وأوله؛ مبدأ الشيء وأشرف ظاهره","what_is_not_ar":"ليس جهة السير ولا مقابلة الأشخاص"},"support_links":[]},{"boundary":"Dal, fiziksel yüzü veya salt uzamsal yönü değil, söz ve işte uygun yol ile doğruluğu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B008","candidate_links":[{"candidate_id":"cand_9ae64b59e50857e0b0f3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"sözün veya işin doğru yönü ve ona uygun düzenleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözün amaçlanan yönünü ve görüşün doğru biçimini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi olması gerektiği gibi düzenlemeyi veya doğru yolundan saptırmayı belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıpta genel beceriksizliği, bir aktarımda ise tuvaletini yapmayı bile becerememeyi anlatır."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün kastını, görüşün doğruluğunu ve işin gereken biçimde yürütülmesini karşılayan çekirdek açıklamadır.","boundary_detail":"Dal, fiziksel yüzü veya salt uzamsal yönü değil, söz ve işte uygun yol ile doğruluğu anlatır.","branch_image_ar":"وجه الأمر وصوابه","concept_gloss":"sözün veya işin doğru yönü ve ona uygun düzenleme","contextual_glosses":[{"applicability":"Bir görüşün veya işin uygun ve doğru yolu kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğru yol ve uygunluk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"doğru yaklaşım","usage_role":"general"},{"applicability":"Kaynakta verilen özel kalıpta kişinin genel beceriksizliği anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel kalıbın işlerini doğru yürütemeyen kişi anlamını korur."},"facet_ids":["F003"],"text":"hiçbir işi doğru dürüst yapamayan","usage_role":"contextual"}],"definition":"Bir sözün amaçlanan yönü veya bir işin olması gereken doğru yolu ve bu yola uygun düzenlenmesidir. Özel bir kuruluşta, hiçbir işi doğru yürütemeyen beceriksiz kişiyi anlatır ve bir aktarımda bu beceriksizlik tuvaletini yapmaya kadar daraltılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözün amaçlanan yönünü ve görüşün doğru biçimini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir işi olması gerektiği gibi düzenlemeyi veya doğru yolundan saptırmayı belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Özel bir kalıpta genel beceriksizliği, bir aktarımda ise tuvaletini yapmayı bile becerememeyi anlatır."}],"identity_rationale":"Kaynak ifadesi sözün amaçlanan yönünü, görüşün doğru biçimini, bir işi olması gerektiği gibi düzenlemeyi ve bu doğrultudan sapmayı verir. Beceriksiz kişiye ilişkin kalıp da işini doğru yürütememe çekirdeğine bağlı özel bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sözün amaçlanan yönü"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"doğru görüş"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"aklına bir görüş gelmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir şeyi doğru yolundan saptırmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"işi gerektiği gibi düzenleyip her şeyi yerine koymak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi"}],"lexicalization_note":"Söz ve işte uygun yol çekirdeği, görüş ve düzenleme kalıpları ile beceriksizlik bildiren özel kuruluş birbirine karıştırılmadan korunur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; doğru davranış yolunu bulma ve genel amaca uygunluk dalları, odak anlamın sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal söz ve görüşün yönünü, işi gereken biçimde düzenlemeyi ve bunun olumsuz kalıbını içerir; komşu dal kişinin doğru davranış yolunu bulmasına odaklanır.","focus_only":"Sözün kastı, görüşün yönü ve özel beceriksizlik kalıbı bu dalda yer alır.","gloss":"işin doğrusunu bulma","neighbor_only":"Kişinin işin doğru tarafını bulması ve davranışında olgunluk göstermesi komşu dalda öne çıkar.","neighbor_ref":"root_000565/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir işte doğru yaklaşımı bulup uygun davranmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal doğru yön ve gereken düzenleme imgesini korur; komşu dal amaca isabet ve düzgünlük anlamını daha geniş eylem alanlarına taşır.","focus_only":"Sözün amaçlanan yönü ve belirli kuruluşlara bağlı beceriksizlik anlatımı vardır.","gloss":"doğruluk ve uygunluk","neighbor_only":"Söz, eylem, atış ve yönetimde hedefe uygunluk ile doğru çizgide olma daha genel kapsamlıdır.","neighbor_ref":"root_000687/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir söz veya işin doğru ve amaca uygun olmasını anlatır."}],"source_phrase_ar":"وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)","source_summary":"Kaynaklar söz, görüş ve işte amaçlanan doğru yol çekirdeğini paylaşır. Beceriksizlik kalıbı genel olarak hiçbir işi doğru yürütememe, daha dar bir aktarımda ise tuvaletini yapmayı becerememe biçiminde açıklanır.","sources":["JA","SI","TA","MU"],"what_is_ar":"الوجه في الرأي والكلام والأمر؛ السنن والصواب والتدبير الحسن؛ استقامة الأمر أو عدمها","what_is_not_ar":"ليس الوجه العضوي ولا الجهة المحضة"},"support_links":["sup_104a96babe00c0572e21"]},{"boundary":"Anlam yalnız yaşlı kişiyi konu alan özel eylem kuruluşunda geçerlidir; genel yönelme anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_001630/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yaşlanıp ömrünün son dönemine girmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaşlı kişinin daha ileri yaşa geçmesini ve ömrünün son dönemine yaklaşmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yaşlı kişinin ileri yaşa geçmesini bildiren kaynakta verilen özel kuruluş için geçerlidir.","boundary_detail":"Anlam yalnız yaşlı kişiyi konu alan özel eylem kuruluşunda geçerlidir; genel yönelme anlamı değildir.","branch_image_ar":"توجه الشيخ","concept_gloss":"yaşlanıp ömrünün son dönemine girmek","contextual_glosses":[{"applicability":"Bir yaşlının ileri yaşa ulaşıp hayatının son dönemine girmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İleri yaşa geçiş anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"iyice yaşlanmak","usage_role":"contextual"}],"definition":"Yaşlı bir kişinin yaşının ilerlemesi, ömrünün son dönemine girmesi ve gençlikten uzaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaşlı kişinin daha ileri yaşa geçmesini ve ömrünün son dönemine yaklaşmasını belirtir."}],"identity_rationale":"Kaynak ifadesi yaşlı kişinin ömründe ileri gidip gençlikten uzaklaşmasını, yaşının büyümesini ve hayatın son dönemine yönelmesini aynı özel kuruluşla açıklar. Dalın yaşlanma ve ömrün gerileme dönemi çerçevesi buna uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yaşlanıp ömrünün son dönemine girmek"}],"lexicalization_note":"Tanım yaşlı kişinin ileri yaşa geçmesini bildiren özel sözlüksel kuruluşla sınırlıdır ve yalın anlama genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yaşlılık ve zihinsel düşüşlü aşırı yaşlılık, özel kuruluşun sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel bir kuruluşla yaşın ilerleyip ömrün son dönemine girmesini anlatır; komşu dal yaşlı kişiyi ve yaşlılık halini genel olarak adlandırır.","focus_only":"Belirli bir eylem kuruluşu yaşlı kişinin daha da ilerleyen yaşa geçişini vurgular.","gloss":"ileri yaşa geçmek","neighbor_only":"Yaşlı erkek ve kadın adları ile yaşlılık durumu genel olarak kapsanır.","neighbor_ref":"root_000834/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin yaşlanmasını ve yaşlılık durumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız yaşın ilerlemesini bildirir; komşu dal ise aşırı yaşlılığın getirdiği zihinsel düşüşü zorunlu olarak içerir.","focus_only":"İleri yaşa geçiş vardır, zihinsel yeti kaybı zorunlu değildir.","gloss":"yaşlanma ile düşkünlük","neighbor_only":"Aşırı yaşlılıkta bilinç ve bilgi yetilerinin bozulması belirleyici koşuldur.","neighbor_ref":"root_000559/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da insan ömrünün ileri ve gerileyen dönemleriyle ilgilidir."}],"source_phrase_ar":"توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)","source_summary":"Kaynaklar özel kuruluşu yaşlı kişinin yaşının ilerlemesi ve ömrünün geriye kalan son dönemine girmesi olarak ortak biçimde açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"كبر السن والإدبار في العمر؛ توجه الشيخ إذا ولى وكبر","what_is_not_ar":"ليس التوجه إلى جهة ولا الجاه"},"support_links":[]},{"boundary":"Anlam, doğumda ellerin veya ön ayakların önce çıkması koşuluna bağlıdır; genel doğum ya da toplumsal itibar değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"doğumda ellerin veya ön ayakların önce çıkması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yavrunun doğumda ellerinin veya ön ayaklarının önce çıkmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Annenin yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yavrunun sunumunu ve annenin bu sunumla doğurmasını birlikte açıklayan özel doğum terimidir.","boundary_detail":"Anlam, doğumda ellerin veya ön ayakların önce çıkması koşuluna bağlıdır; genel doğum ya da toplumsal itibar değildir.","branch_image_ar":"الولادة باليدين أولا","concept_gloss":"doğumda ellerin veya ön ayakların önce çıkması","contextual_glosses":[{"applicability":"İnsan yavrusunun elleri önce çıkacak biçimde doğması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan doğumunda ellerin önce çıkması koşulunu korur."},"facet_ids":["F001"],"text":"elleri önde doğmak","usage_role":"contextual"},{"applicability":"Hayvan yavrusunun ön ayakları önce çıkacak biçimde doğması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan doğumunda ön ayakların önce çıkması koşulunu korur."},"facet_ids":["F001"],"text":"ön ayakları önde doğmak","usage_role":"contextual"}],"definition":"Doğum sırasında bir yavrunun ellerinin veya ön ayaklarının bedeninin öteki bölümlerinden önce çıkması ve annenin yavruyu bu biçimde doğurmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yavrunun doğumda ellerinin veya ön ayaklarının önce çıkmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Annenin yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmasını belirtir."}],"identity_rationale":"Kaynak ifadesi doğum sırasında yavrunun ellerinin veya ön ayaklarının rahimden önce çıkmasını ve annenin onu bu biçimde doğurmasını açıkça verir. Dalın doğum sunumuna ilişkin çerçevesi bu koşulu tam korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"elleri veya ön ayakları önce çıkan yavru"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak"}],"lexicalization_note":"Önce elleri çıkan yavruyu bildiren biçim ile annenin bu biçimde doğurmasını bildiren kalıp ayrı sözlüksel gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Tüm adaylar incelendi; ayakların önce çıktığı karşı sunum ile yavruyu karşılayan kişi, doğum olayındaki en açıklayıcı iki sınırı verir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal ellerin veya ön ayakların önce çıkmasını, komşu dal ise ayakların baştan önce çıkmasını belirtir; ayrım doğumda öne gelen uzuv üzerindedir.","focus_only":"Doğumda ellerin veya ön ayakların önce çıkması vardır.","gloss":"önde çıkan uzuv","neighbor_only":"Doğumda ayakların baştan önce çıkması vardır.","neighbor_ref":"root_001551/B002","relation_type":"polarity_pair","shared_zone":"İki dal da yavrunun olağan dışı bir uzuv sunumuyla doğmasını anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal yavrunun çıkış biçimini niteler; komşu dal ise çıkan yavruyu karşılayan kişinin eylemini veya görevini anlatır.","focus_only":"Yavrunun doğumda hangi uzvunun önce çıktığını niteleyen sunum biçimidir.","gloss":"doğum sunumu ve doğumu karşılama","neighbor_only":"Doğum sırasında yavruyu karşılayıp alan kişinin görevidir.","neighbor_ref":"root_001198/B007","relation_type":"thematic","shared_zone":"İki dal da doğum olayının katılımcıları ve aşamalarıyla ilgilidir."}],"source_phrase_ar":"للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)","source_summary":"Kaynaklar yavrunun doğum kanalından elleri veya ön ayakları önce çıkması koşulunda birleşir; adlandırma hem yavruya hem de annenin doğurma eylemine uygulanır.","sources":["MQ","SI","TA"],"what_is_ar":"الوجيه من المولود إذا خرجت يداه قبل غيرهما؛ أوجهت به أمه إذا ولدته كذلك","what_is_not_ar":"ليس وجاهة المنزلة ولا الوجه العضوي العام"},"support_links":[]},{"boundary":"Bu, uyak düzenindeki belirli bir harftir; genel yöneltme eylemi veya bağımsız bir hareket adı değildir.","branch_kind":"bare","branch_ref":"root_001630/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harfi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız klasik şiirin uyak yapısındaki bu belirli konumu adlandıran teknik kullanım için geçerlidir.","boundary_detail":"Bu, uyak düzenindeki belirli bir harftir; genel yöneltme eylemi veya bağımsız bir hareket adı değildir.","branch_image_ar":"توجيه القافية","concept_gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf","contextual_glosses":[{"applicability":"Teknik uyak çözümlemesinde harfin konumunu kısa ve anlaşılır biçimde açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki belirli uyak öğesi arasında bulunma özelliğini bağlam içinde korur."},"facet_ids":["F001"],"text":"aradaki uyak harfi","usage_role":"explanatory"}],"definition":"Klasik uyak düzeninde kurucu uzun ünlü ile şiirin ana uyak harfi arasında bulunan harftir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harfi belirtir."}],"identity_rationale":"Kaynak ifadelerinin tümü şiirde kurucu uzun ünlü ile ana uyak harfi arasında bulunan harfi tanımlar. Geçici çerçevedeki hareket seçeneği kaynak ifadesiyle desteklenmediğinden tanım yalnız aradaki harf olarak düzeltilmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf"}],"lexicalization_note":"Dal, teknik şiir teriminin yalın biçimini tanımlar; başka yöneltme kalıpları bu teknik anlama taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kurucu uzun ünlü ve ana uyak harfi, teknik terimin iki yanındaki konumu doğrudan gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal iki öğe arasındaki harfi, komşu dal ise bu düzeni kuran uzun ünlünün kendisini belirtir.","focus_only":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harftir.","gloss":"iki ayrı uyak öğesi","neighbor_only":"Uyakta kalıcı olan ve ana uyak harfinden bir harf uzakta duran kurucu uzun ünlüdür.","neighbor_ref":"root_000031/B004","relation_type":"same_field","shared_zone":"İki dal da aynı klasik uyak dizisinin bitişik öğelerini adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal ana uyak harfinden önceki belirli ara konumu, komşu dal ise dizelerin bağlandığı ana uyak harfini gösterir.","focus_only":"Kurucu uzun ünlü ile ana uyak harfi arasındaki ara harftir.","gloss":"ara harf ile ana uyak harfi","neighbor_only":"Şiir boyunca birliği sağlayan ana uyak harfinin kendisidir.","neighbor_ref":"root_000615/B013","relation_type":"same_field","shared_zone":"İki dal da şiirin uyak örgüsündeki harf konumlarını adlandırır."}],"source_phrase_ar":"التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)","source_summary":"Kaynaklar teknik terimi, kurucu uzun ünlü ile ana uyak harfi arasındaki harf olarak ortak biçimde tanımlar.","sources":["SI","TA","MU"],"what_is_ar":"التوجيه في الشعر والقافية؛ الحرف أو الحركة بين ألف التأسيس والروي","what_is_not_ar":"ليس جهة السير ولا إرشاد الشيء"},"support_links":[]},{"boundary":"Anlam yalnız bu özel yetiştirme işlemidir; bir şeyi genel olarak yöneltme anlamına genişletilmez.","branch_kind":"bare","branch_ref":"root_001630/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"hıyar veya kavunun altını kazıp yana yatırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hıyar veya kavunun altını kazma ve sonra onu yana yatırma aşamalarını birlikte belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta anlatılan iki aşamalı bitki yetiştirme işlemi için geçerlidir.","boundary_detail":"Anlam yalnız bu özel yetiştirme işlemidir; bir şeyi genel olarak yöneltme anlamına genişletilmez.","branch_image_ar":"توجيه النبات","concept_gloss":"hıyar veya kavunun altını kazıp yana yatırma","contextual_glosses":[{"applicability":"Hıyar veya kavun yetiştirirken iki aşamalı işlemi eylem olarak anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazma ve ardından yana yatırma sırasını korur."},"facet_ids":["F001"],"text":"altını kazıp yana yatırmak","usage_role":"contextual"}],"definition":"Hıyarın veya kavunun altındaki toprağı kazıp ardından bitkiyi yana yatırma işlemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hıyar veya kavunun altını kazma ve sonra onu yana yatırma aşamalarını birlikte belirtir."}],"identity_rationale":"Tek kaynak ifadesi, hıyar veya kavunun altını kazdıktan sonra bitkiyi yana yatırma işlemini açık ve aşamalı biçimde verir. Dal çerçevesi hem nesneleri hem de işlem sırasını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"hıyar veya kavunun altını kazıp yana yatırma"}],"lexicalization_note":"Yalın biçim teknik bir bitki yetiştirme işlemini adlandırır; genel yön verme anlamı tanıma alınmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; genel yetiştirme ve bitkinin desteğe sarılması, özel insan müdahalesini en iyi sınırlayan iki alandır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal iki belirli bitkiye uygulanan sıralı bir bakım tekniğidir; komşu dal ekme ve yetiştirmeyi genel olarak kapsar.","focus_only":"Hıyar veya kavunun altını kazıp bitkiyi yana yatırma işlemi vardır.","gloss":"özel bakım ile genel yetiştirme","neighbor_only":"Tohum ekme, bitki yetiştirme, ekin ve ekili yer gibi geniş bir tarım alanı vardır.","neighbor_ref":"root_000630/B001","relation_type":"same_field","shared_zone":"İki dal da bitki yetiştirme ve tarımsal işlem alanında yer alır."},{"boundary_match":"field_only","distinction":"Odak dal yetiştiricinin yaptığı kazma ve yatırma işlemidir; komşu dal bitkinin kıvrılıp bir desteğe tutunma biçimidir.","focus_only":"Bitkinin altını kazdıktan sonra onu yana yatıran insan işlemi vardır.","gloss":"yana yatırma ile sarılma","neighbor_only":"Sarmaşık benzeri bitkinin kendiliğinden kıvrılıp çubuklara tutunması vardır.","neighbor_ref":"root_000350/B006","relation_type":"same_field","shared_zone":"İki dal da bitkinin büyürken aldığı yön ve konumla ilgilidir."}],"source_phrase_ar":"التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu özel yetiştirme işlemi tek kaynakta, önce altını kazma sonra bitkiyi yana yatırma sırasıyla aktarılır."}],"source_summary":"Anlam, hıyar veya kavunun altını kazma ve ardından bitkiyi yana yatırma sırasından oluşan özel yetiştirme işlemidir.","sources":["MQ"],"what_is_ar":"التوجيه في القثاءة أو البطيخة؛ حفر ما تحتها ثم إضجاعها","what_is_not_ar":"ليس توجيه الشيء إلى جهة عامة"},"support_links":[]},{"boundary":"Bu dalda vurmanın hedefi özellikle yüzdür; genel vurma veya sözlü yüzleşme anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüzüne vurma ve yüzüne vurulmuş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin yüzünü hedef alarak vurmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yüzüne vurulmuş kişiyi sonuç durumuyla niteler."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Vurmanın özellikle yüzü hedef aldığı eylem ve sonuç durumu için geçerlidir.","boundary_detail":"Bu dalda vurmanın hedefi özellikle yüzdür; genel vurma veya sözlü yüzleşme anlamı değildir.","branch_image_ar":"ضرب الوجه","concept_gloss":"yüzüne vurma ve yüzüne vurulmuş olma","contextual_glosses":[{"applicability":"Eylemin bir kişinin yüzünü hedef aldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vurma eylemi ile yüz hedefini korur."},"facet_ids":["F001"],"text":"yüzüne vurmak","usage_role":"general"},{"applicability":"Kişinin eylemden etkilenmiş sonuç durumu nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzüne vurulmuş olma sonucunu korur."},"facet_ids":["F002"],"text":"yüzüne vurulmuş","usage_role":"contextual"}],"definition":"Bir kişinin yüzüne vurmak ve bu eylemin sonucu olarak kişinin yüzüne vurulmuş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin yüzünü hedef alarak vurmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Yüzüne vurulmuş kişiyi sonuç durumuyla niteler."}],"identity_rationale":"Tek kaynak ifadesi eylemi bir kişinin yüzüne vurmak, sonuç sıfatını da yüzüne vurulmuş olmak biçiminde açıkça tanımlar. Dal kimliği hedef bölge ile sonuç durumunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"birinin yüzüne vurmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yüzüne vurulmuş"}],"lexicalization_note":"Yüze vurma eylemi ile yüzüne vurulmuş kişiyi bildiren biçim ayrı tutulur ve genel vurma anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel tokatlama ile özel çene darbesi, yüz hedefinin hem geniş hem dar komşu sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüz hedefini zorunlu kılar; komşu dal vurma ve tokatlamayı farklı hedeflere ve başka çarpma eylemlerine genişletir.","focus_only":"Vurmanın hedefi özellikle yüzdür ve sonuç sıfatı da bu hedefi korur.","gloss":"yüze vurma","neighbor_only":"Tokatlama, genel dövüşme ve kuşun kanat çarpması gibi daha geniş eylemler vardır.","neighbor_ref":"root_000713/B004","relation_type":"near_synonym","shared_zone":"İki dal da birine vurma veya tokatlama eylemini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal hedefi genel olarak yüz diye belirler; komşu dal darbeyi veya itmeyi çene bölgesiyle sınırlar.","focus_only":"Yüzün herhangi bir bölümüne vurma ve vurulmuş yüz sonucu vardır.","gloss":"yüz ile çene hedefi","neighbor_only":"Çene veya çene bağlantısına vurma ya da itme özellikle belirlenmiştir.","neighbor_ref":"root_000515/B003","relation_type":"near_neighbor","shared_zone":"İki dal da başın ön bölümüne yönelen fiziksel darbeyi kapsar."}],"source_phrase_ar":"وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak hem yüzüne vurma eylemini hem de yüzüne vurulmuş kişiyi bildiren sonuç biçimini aktarır."}],"source_summary":"Anlam, yüzü hedef alan vurma eylemini ve bu eylemden etkilenen kişinin sonuç durumunu birlikte kapsar.","sources":["TA"],"what_is_ar":"ضرب وجه الشخص؛ موجوه لمن ضرب وجهه","what_is_not_ar":"ليس المواجهة بالكلام ولا الوجه بمعنى الجاه"},"support_links":[]},{"boundary":"Bu anlam, gelen kişiyi geri çevirme koşuluna bağlıdır; genel engelleme veya bir yöne sevk etme değildir.","branch_kind":"non_bare","branch_ref":"root_001630/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"yanına gelen kişiyi geri çevirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birinin yanına gelmiş kişiyi kabul etmeyerek geri göndermeyi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin gelmiş olması ve muhatabın onu geri göndermesi koşullarını birlikte taşıyan özel kullanım için geçerlidir.","boundary_detail":"Bu anlam, gelen kişiyi geri çevirme koşuluna bağlıdır; genel engelleme veya bir yöne sevk etme değildir.","branch_image_ar":"الرد عن الوجه","concept_gloss":"yanına gelen kişiyi geri çevirmek","contextual_glosses":[{"applicability":"Birinin yanına kadar gelen kişinin kabul edilmeyip gönderilmesini doğal bağlamda anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelmiş kişiyi kabul etmeyip geri gönderme durumunu korur."},"facet_ids":["F001"],"text":"kapısından geri çevirmek","usage_role":"contextual"}],"definition":"Bir kişinin yanına gelen kimseyi kabul etmeyip geri çevirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birinin yanına gelmiş kişiyi kabul etmeyerek geri göndermeyi belirtir."}],"identity_rationale":"Tek kaynak ifadesi bir kişinin başka birinin yanına gelmesinden sonra geri çevrilmesini açıkça bildirir. Dal kimliği gelişin önce, geri çevirmenin sonra gerçekleştiği katılımcı ve aşama düzenini korur.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yanına gelen kişiyi geri çevirmek"}],"lexicalization_note":"Tanım yalnız birinin yanına gelen kişiyi geri çevirmeyi bildiren özel sözlüksel birimle sınırlıdır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; istekte bulunanı geri çevirme ve genel reddetme, geliş koşulunun sınırını en iyi belirleyen iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yanına gelmiş kişiyi geri gönderme koşuluyla sınırlıdır; komşu dal ise özellikle istekte bulunan kişiyi yüz çevirerek reddetmeyi anlatır.","focus_only":"Kişinin muhatabın yanına gelmiş olması yeterlidir; bir istekte bulunması şart değildir.","gloss":"geleni veya isteyeni geri çevirmek","neighbor_only":"Geri çevrilen kişinin bir istekte bulunması ve muhatabın ondan yüz çevirmesi özellikle belirtilir.","neighbor_ref":"root_000867/B009","relation_type":"near_synonym","shared_zone":"İki dal da karşıya gelen kişinin kabul edilmeyip geri çevrilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelen kişi ve geliş olayıyla sınırlıdır; komşu dal reddetmeyi sözlere, nesnelere ve yanlış ya da geçersiz içeriklere genişletir.","focus_only":"Geri çevrilen katılımcı, birinin yanına gelmiş kişidir.","gloss":"kişiyi geri çevirme ile reddetme","neighbor_only":"Nesne, söz, hata veya geçersiz para gibi insan dışı içerikleri kabul etmeme kapsamı vardır.","neighbor_ref":"root_000555/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şeyi kabul etmeyip geri gönderme sonucu bulunur."}],"source_phrase_ar":"أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, yanına gelen kişiyi kabul etmeyip geri çevirme anlamını aktarır."}],"source_summary":"Anlam, kişinin önce bir başkasının yanına gelmesi ve ardından o kişi tarafından geri çevrilmesi aşamalarından oluşur.","sources":["TA"],"what_is_ar":"إتيان الرجل ثم رده؛ أوجهه إذا رده","what_is_not_ar":"ليس التوجيه إلى جهة ولا المواجهة"},"support_links":[]},{"boundary":"Anlam yalnız iki yüzlü nesne ve içiyle dışı uyuşmayan kişi kalıplarına bağlıdır; genel yüz veya itibar anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001630/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","surface_ar":"وُجُوهٌ"}],"gloss":"iki yüzlü nesne; içiyle dışı uyuşmayan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kumaşın iki ayrı yüzünün bulunmasını belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin içinden geçenden farklı bir yüzle karşısına çıkıp tutarsız davranmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta verilen fiziksel kumaş ve davranışsal kişi kalıplarını birlikte özetler.","boundary_detail":"Anlam yalnız iki yüzlü nesne ve içiyle dışı uyuşmayan kişi kalıplarına bağlıdır; genel yüz veya itibar anlamı değildir.","branch_image_ar":"ذو وجهين","concept_gloss":"iki yüzlü nesne; içiyle dışı uyuşmayan kişi","contextual_glosses":[{"applicability":"Kumaşın fiziksel olarak iki ayrı yüzünün bulunması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kumaşın iki fiziksel yüzü bulunması anlamını korur."},"facet_ids":["F001"],"text":"iki yüzü de kullanılabilen kumaş","usage_role":"explanatory"},{"applicability":"Kişinin karşısındakine içinden geçenden farklı görünerek davranması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin içiyle dışı arasındaki davranışsal uyuşmazlığı korur."},"facet_ids":["F002"],"text":"iki yüzlü kimse","usage_role":"contextual"}],"definition":"Bir kumaşın iki yüzünün bulunmasıdır; kişiye uygulanan ayrı bir kalıpta ise karşısındakine kalbinde olandan farklı görünerek davranmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kumaşın iki ayrı yüzünün bulunmasını belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin içinden geçenden farklı bir yüzle karşısına çıkıp tutarsız davranmasını belirtir."}],"identity_rationale":"Tek kaynak ifadesi iki ayrı kalıbı açıkça verir: iki yüzü bulunan kumaş ve karşısındakine içindekinden farklı davranan kişi. Dal kimliği fiziksel iki yanlılık ile bundan kurulan davranışsal uzantıyı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"iki yüzü bulunan kumaş"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"içiyle dışı uyuşmayan iki yüzlü kimse"}],"lexicalization_note":"Fiziksel olarak iki yüzlü kumaş ile davranışta iki yüzlü kişi, kendi kalıpları içinde ayrı facetler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aldatıcı görünüş ile gizli karşıt bağlılık, kişi kalıbının davranışsal sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kişi kalıbının yanında fiziksel iki yüzlü kumaşı da kapsar; komşu dal ise aldatıcı davranışı yöntem ve bağlam bakımından daha geniş işler.","focus_only":"İki yüzü bulunan kumaş anlamı ve kişi için belirli iki yüzlü kalıbı vardır.","gloss":"iki yüzlülük ve aldatma","neighbor_only":"Hile, savaş aldatmacası ve gizlediğinden farklı huy veya görüş gösterme gibi daha geniş davranışlar vardır.","neighbor_ref":"root_000396/B001","relation_type":"near_neighbor","shared_zone":"Kişi kullanımında iki dal da içte olanı gizleyip dışarıya farklı görünmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal kişiler arası iki yüzlü davranışı ve fiziksel kumaş anlamını taşır; komşu dal dıştan bağlı görünüp gizlice karşıt durumda olmayı özel bir inanç ve bağlılık bağlamında sınırlar.","focus_only":"Fiziksel iki yüzlü kumaş ve kişiler arası tutarsız görünüş kalıbı vardır.","gloss":"iki yüzlülük ile gizli karşıtlık","neighbor_only":"İnanç veya toplumsal bağlılıkta dışarıdan kabul gösterip gizlice karşıt yönde çıkma özel koşulu vardır.","neighbor_ref":"root_001537/B004","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin dışarıda gösterdiğiyle içinde taşıdığının farklı olmasını içerir."}],"source_phrase_ar":"كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak hem iki yüzlü kumaş kalıbını hem de içiyle dışı uyuşmayan kişi kalıbını birlikte aktarır."}],"source_summary":"Anlam, kumaşın fiziksel olarak iki yüzlü olması ile kişinin içinden geçenden farklı görünmesi arasındaki biçimsel benzerliği iki ayrı kalıpta kurar.","sources":["JA"],"what_is_ar":"ما له وجهان حسيا؛ ومن يلقى بخلاف ما في قلبه","what_is_not_ar":"ليس الوجاهة ولا مقابلة الوجوه"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_6ea05bf19e327b1964d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:face-day-reversal","source_type":"word_analysis","support_ids":["sup_877bec6dcf65f62218cb","sup_a6530e9ec8096fbf1743"],"title":"same face-Day frame reversed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_52aa8b6dbc55ee4c6392","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:indefinite-visible-subject","source_type":"word_analysis","support_ids":["sup_a6530e9ec8096fbf1743","sup_bd96908baa70d4a7e86d"],"title":"indefinite faces as fresh subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_471796db515bf9c15546","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:nasal-open-form","source_type":"word_analysis","support_ids":["sup_405ec6babe7e4e1ab289","sup_a6530e9ec8096fbf1743"],"title":"open plural carried into event-time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_2ac567fe0648092540af","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:orientation-status-pressure","source_type":"word_analysis","support_ids":["sup_a6530e9ec8096fbf1743","sup_b0b0facee77e0b3658bd"],"title":"front-facing and status pressure kept local","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_ace8bfb0eed73d39982c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:public-countenance-metonymy","source_type":"word_analysis","support_ids":["sup_8e18a925d3e1d4d4e13b","sup_a6530e9ec8096fbf1743"],"title":"countenance as public manifestation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_a79a79c6455592a8fb76","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:three-word-tableau-boundary","source_type":"word_analysis","support_ids":["sup_46f9d62ab2360f324229","sup_a6530e9ec8096fbf1743"],"title":"visible entry into the blessed tableau","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:1","qac_refs":["88:8:1:1"],"status":"accepted"}},{"anchor_refs":["88:8:2"],"branch_refs":[],"candidate_id":"cand_7a71ac4b8ef5df68ad19","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:8:2:audible-deictic-compression","source_type":"word_analysis","support_ids":["sup_10bc159f1ce55e11aa8b","sup_ca18583eefc7c8c19012"],"title":"hamza and nunation mark the compact turn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:2","qac_refs":["88:8:2:1"],"status":"accepted"}},{"anchor_refs":["88:8:2"],"branch_refs":[],"candidate_id":"cand_d7ce898ae000b8501257","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:8:2:decisive-day-not-duration","source_type":"word_analysis","support_ids":["sup_4a47caf94cc5e4a6904b","sup_ca18583eefc7c8c19012"],"title":"broad day range narrowed to decisive occasion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:2","qac_refs":["88:8:2:1"],"status":"accepted"}},{"anchor_refs":["88:8:2"],"branch_refs":[],"candidate_id":"cand_2d14963f89990a2dff9e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:8:2:deictic-event-compound","source_type":"word_analysis","support_ids":["sup_1c47b65aad5712f52487","sup_ca18583eefc7c8c19012"],"title":"that-Day compound retrieves the event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:2","qac_refs":["88:8:2:1"],"status":"accepted"}},{"anchor_refs":["88:8:2"],"branch_refs":[],"candidate_id":"cand_a018230a4b9034dd6f7b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:8:2:medial-hinge","source_type":"word_analysis","support_ids":["sup_91bb5465ac77638d3d95","sup_ca18583eefc7c8c19012"],"title":"time inserted between face and state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:2","qac_refs":["88:8:2:1"],"status":"accepted"}},{"anchor_refs":["88:8:2"],"branch_refs":[],"candidate_id":"cand_b3814509a734f6086f7f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:8:2:same-frame-two-outcomes","source_type":"word_analysis","support_ids":["sup_af4f6f70871fb0d02036","sup_ca18583eefc7c8c19012"],"title":"one Day-frame holds opposed faces","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:2","qac_refs":["88:8:2:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_36d81eea9842be65ed49","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:boundary-from-deficit-to-ease","source_type":"word_analysis","support_ids":["sup_4dc9d0adf706ea6e60e4","sup_cf893a319161951edb49"],"title":"failed sufficiency becomes manifested ease","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_4cf0742d22af57ac35a8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:opposite-predicate-slot","source_type":"word_analysis","support_ids":["sup_30fabb682bd69bb55d90","sup_4dc9d0adf706ea6e60e4"],"title":"eased predicate reverses 88:2","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_db4796ceef0032e3b731","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:participial-visible-state","source_type":"word_analysis","support_ids":["sup_4dc9d0adf706ea6e60e4","sup_7c2327d56f066b7da00e"],"title":"abiding visible state, not event verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_f11f48116db451974871","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:predicate-collective-verdict","source_type":"word_analysis","support_ids":["sup_19f65e1248ce914ecf2a","sup_4dc9d0adf706ea6e60e4"],"title":"collective predicate verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_aefee63399bacc3c35b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:soft-emphatic-arrival","source_type":"word_analysis","support_ids":["sup_4dc9d0adf706ea6e60e4","sup_7dc3b84509d3ff8c45bb"],"title":"softened emphatic arrival","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_0e831a3311fe2952ed19","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:softness-bounty-visible","source_type":"word_analysis","support_ids":["sup_4dc9d0adf706ea6e60e4","sup_f6199249c87161911b7c"],"title":"softness and bounty made visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:8:3","qac_refs":["88:8:3:1"],"status":"accepted"}},{"anchor_refs":["88:8:1"],"branch_refs":[],"candidate_id":"cand_e4c905ebd16463036b90","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:8:1:1","source_type":"qac_morpheme","support_ids":["sup_918434dcee8756d7fb04"],"title":"QAC root occurrence: و ج ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:8:3"],"branch_refs":[],"candidate_id":"cand_7fb3ee64ba34a87a8c9c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001525"],"scope":"focus_ayah","source_local_id":"88:8:3:1","source_type":"qac_morpheme","support_ids":["sup_6f571ec0425fda9667a2"],"title":"QAC root occurrence: ن ع م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:8","branch_refs":["root_001525/B002","root_001630/B001"],"candidate_id":"cand_5ad5c2ade7ac3211c70d","commentary_obligation":"review","hft_ref":"hft_1c15f78c348982afe943","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_visible_ease","source_type":"hft","support_ids":["sup_cd28e438ad3004719364"],"title":"baseline_visible_ease","trust":"legacy_unbound"},{"anchor_refs":["88:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:8","branch_refs":["root_001525/B001","root_001630/B004"],"candidate_id":"cand_cff8a4865edae7f185d4","commentary_obligation":"review","hft_ref":"hft_df0581ba08a571a1b78b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_whole_person_flourishing","source_type":"hft","support_ids":["sup_2b6d1ab8539602b9597e"],"title":"baseline_whole_person_flourishing","trust":"legacy_unbound"},{"anchor_refs":["88:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:8","branch_refs":["root_001525/B003","root_001630/B002","root_001630/B008"],"candidate_id":"cand_9ae64b59e50857e0b0f3","commentary_obligation":"review","hft_ref":"hft_4666b90d05a715001b57","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_approved_orientation","source_type":"hft","support_ids":["sup_104a96babe00c0572e21"],"title":"baseline_approved_orientation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","qac_morphemes":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","root_ar":"و ج ه","surface_ar":"وُجُوهٌ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"88:8:2:1","qac_word_ref":"88:8:2","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","root_ar":"ن ع م","surface_ar":"نَّاعِمَةٌ"}],"word_analysis_qac_refs":[["88:8:1:1"],["88:8:2:1"],["88:8:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:8:1","88:8:2","88:8:3"]},"focus_surface_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","qac_morphemes":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:1:1","qac_word_ref":"88:8:1","root_ar":"و ج ه","surface_ar":"وُجُوهٌ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"88:8:2:1","qac_word_ref":"88:8:2","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"نَّاعِمَة","morph_features":"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:8:3:1","qac_word_ref":"88:8:3","root_ar":"ن ع م","surface_ar":"نَّاعِمَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:8:1:1"],["88:8:2:1"],["88:8:3:1"]],"word_analysis_refs":["88:8:1","88:8:2","88:8:3"],"word_rows":[{"analysis_record_ref":"88:8:1","analytic_gloss_range_en":"indefinite broken-plural faces as the visible subject of the nominal scene","analytic_root_gloss_range_en":"face, front, outward aspect, orientation, confrontation, and status; the local noun selects concrete countenances while allowing public-facing and status-bearing pressure","qac_refs":["88:8:1:1"],"root":{"arabic":"و ج ه","transliteration":"w-j-h"},"surface":{"arabic":"وُجُوهٌۭ","transliteration":"wujūhun"}},{"analysis_record_ref":"88:8:2","analytic_gloss_range_en":"deictic temporal adverbial compound meaning on that Day, at the already evoked event-time","analytic_root_gloss_range_en":"ordinary day, open time span, event-day, marked divine days, and the yawm-idh construction; the local compound selects a singular deictic event-frame","qac_refs":["88:8:2:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍۢ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"88:8:3","analytic_gloss_range_en":"feminine singular active-participle predicate naming visible ease, flourishing, and softened wellbeing on the face-class","analytic_root_gloss_range_en":"pleasant well-being, bestowed favor, softness, easeful living, praise, affirmation, livestock, and other lexical branches; the local predicate selects ease, softness, comfort, and favor-pressure while excluding unrelated branches","qac_refs":["88:8:3:1"],"root":{"arabic":"ن ع م","transliteration":"n-ʿ-m"},"surface":{"arabic":"نَّاعِمَةٌۭ","transliteration":"nāʿimatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:8"],"branch_refs":["root_001525/B002","root_001630/B001"],"candidate_id":"cand_5ad5c2ade7ac3211c70d","evidence_scope":"focus_ayah","hft_ref":"hft_1c15f78c348982afe943","item_id":"baseline_visible_ease","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_visible_ease","support_id":"sup_cd28e438ad3004719364"},{"anchor_refs":["88:8"],"branch_refs":["root_001525/B001","root_001630/B004"],"candidate_id":"cand_cff8a4865edae7f185d4","evidence_scope":"focus_ayah","hft_ref":"hft_df0581ba08a571a1b78b","item_id":"baseline_whole_person_flourishing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_whole_person_flourishing","support_id":"sup_2b6d1ab8539602b9597e"},{"anchor_refs":["88:8"],"branch_refs":["root_001525/B003","root_001630/B002","root_001630/B008"],"candidate_id":"cand_9ae64b59e50857e0b0f3","evidence_scope":"focus_ayah","hft_ref":"hft_4666b90d05a715001b57","item_id":"baseline_approved_orientation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_approved_orientation","support_id":"sup_104a96babe00c0572e21"}],"diagnostics":[],"lane_counts":{"global":13,"macro":8,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:8","lane":"micro","linguistic_source_ref":"88:8","surface_ref":"88:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:8","target_tokens":[["O",["88:8:2"]],["gün",["88:8:2"]],["yüzler",["88:8:1"]],["rahattır",["88:8:3"]]],"text":"O gün yüzler rahattır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2:audible-deictic-compression","source_type":"word_analysis","support_id":"sup_10bc159f1ce55e11aa8b","text":"{\"blocking_evidence\":null,\"headline\":\"hamza and nunation mark the compact turn\",\"reader_payoff\":\"The reader hears the compact time-marker as a caught deictic insertion rather than a smooth generic time noun.\",\"reason\":\"The orthographic-recited compound includes the internal hamza and final nunation while occupying the medial position.\",\"representative_source_ids\":[\"QF-3eeffe5c\",\"QF-68219a27\",\"QP-f84c563b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:predicate-collective-verdict","source_type":"word_analysis","support_id":"sup_19f65e1248ce914ecf2a","text":"{\"blocking_evidence\":null,\"headline\":\"collective predicate verdict\",\"reader_payoff\":\"The reader notices that ease is the clause's predicate verdict for a whole visible class of faces.\",\"reason\":\"QAC marks the word as a feminine singular nominative active participle, and attachment evidence makes it the predicate of the broken-plural subject.\",\"representative_source_ids\":[\"QG-25292281\",\"QG-e62150bf\",\"MG-c0de4522\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2:deictic-event-compound","source_type":"word_analysis","support_id":"sup_1c47b65aad5712f52487","text":"{\"blocking_evidence\":null,\"headline\":\"that-Day compound retrieves the event\",\"reader_payoff\":\"The reader notices that the time phrase silently carries the already evoked overwhelming event into the positive scene.\",\"reason\":\"Attachment evidence links the deictic element back to the event noun in 88:1, and V4 recognizes the yawm-idh construction as a contextual time reference.\",\"representative_source_ids\":[\"QG-7e4d5732\",\"QG-aedb5bee\",\"MT-f63e2656\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:opposite-predicate-slot","source_type":"word_analysis","support_id":"sup_30fabb682bd69bb55d90","text":"{\"blocking_evidence\":null,\"headline\":\"eased predicate reverses 88:2\",\"reader_payoff\":\"The reader recognizes the final word as the positive counter-state that completes the paired face-Day taxonomy from 88:2.\",\"reason\":\"The critical rows identify the same face-Day-predicate frame as 88:2, while the local predicate supplies the opposite semantic value.\",\"representative_source_ids\":[\"MT-77898ea4\",\"QE-d2c446f3\",\"QY-4de07048\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:nasal-open-form","source_type":"word_analysis","support_id":"sup_405ec6babe7e4e1ab289","text":"{\"blocking_evidence\":null,\"headline\":\"open plural carried into event-time\",\"reader_payoff\":\"The reader hears the indefinite face-class move directly into the Day-marker before the verdict is named.\",\"reason\":\"The form is indefinite with final nunation and is immediately followed by the temporal compound.\",\"representative_source_ids\":[\"QF-546f845a\",\"QP-54e56edf\",\"MP-22129cc3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:three-word-tableau-boundary","source_type":"word_analysis","support_id":"sup_46f9d62ab2360f324229","text":"{\"blocking_evidence\":null,\"headline\":\"visible entry into the blessed tableau\",\"reader_payoff\":\"The reader feels the discourse boundary move from failed sustenance to a still human tableau before the blessed sequence unfolds.\",\"reason\":\"The clause begins a new nominal scene with this subject, and no attachment evidence carries the prior food-chain syntax across the boundary.\",\"representative_source_ids\":[\"QT-11a970c0\",\"QT-809100d7\",\"QB-24820964\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2:decisive-day-not-duration","source_type":"word_analysis","support_id":"sup_4a47caf94cc5e4a6904b","text":"{\"blocking_evidence\":null,\"headline\":\"broad day range narrowed to decisive occasion\",\"reader_payoff\":\"The reader takes the word as a decisive occasion of disclosure, not a neutral calendar span.\",\"reason\":\"V4 allows ordinary day, broad span, and event-day branches, while the local deictic compound and adverbial syntax select the event-day reading.\",\"representative_source_ids\":[\"QS-5d48ae8d\",\"QS-e1129504\",\"QI-817465fd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3","source_type":"word_analysis","support_id":"sup_4dc9d0adf706ea6e60e4","text":"{\"gloss_range\":\"feminine singular active-participle predicate naming visible ease, flourishing, and softened wellbeing on the face-class\",\"prose\":\"{{ar:نَّاعِمَةٌۭ}} ({{tr:nāʿimatun}}) is the final predicate and the clause's positive verdict. Its feminine singular form agrees with the non-rational broken plural {{ar:وُجُوهٌۭ}} ({{tr:wujūhun}}), gathering many faces into one visible class rather than scattering the scene into private reactions. As an active participle in a verbless clause, it names a carried condition already visible in the tableau, not a finite reward event or a causative act of making comfortable. The root field lets softness, pleasant living, delight, bounty, and bestowed favor converge on the face: the blessed outcome is felt as smooth composure and sufficiency made public. That range is still narrowed by the local predicate, so praise-formula, affirmation, livestock, and other remote branches do not become local senses. The word also seals the reversal of 88:2: the same face-Day-predicate frame now answers humbled faces with eased, flourishing faces. Its arrival is audible too: the assimilated nasal opening and long vowel give the predicate a softened but emphatic landing. After the failed sufficiency of 88:7, the boundary turns from lack into stable nominal ease, and 88:9 will continue the blessed sequence with satisfaction.\",\"root_display\":\"{{ar:ن ع م}} ({{tr:n-ʿ-m}})\",\"root_gloss_range\":\"pleasant well-being, bestowed favor, softness, easeful living, praise, affirmation, livestock, and other lexical branches; the local predicate selects ease, softness, comfort, and favor-pressure while excluding unrelated branches\",\"surface_display\":\"{{ar:نَّاعِمَةٌۭ}} ({{tr:nāʿimatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:8:3:1","source_type":"qac_morpheme","support_id":"sup_6f571ec0425fda9667a2","text":"{\"lemma_ar\":\"نَّاعِمَة\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:n~aAEimap|ROOT:nEm|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:8:3:1\",\"qac_word_ref\":\"88:8:3\",\"root_ar\":\"ن ع م\",\"surface_ar\":\"نَّاعِمَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:participial-visible-state","source_type":"word_analysis","support_id":"sup_7c2327d56f066b7da00e","text":"{\"blocking_evidence\":null,\"headline\":\"abiding visible state, not event verb\",\"reader_payoff\":\"The reader sees ease as an already carried display-state on the faces, not as a narrated action after the fact.\",\"reason\":\"The local form is an active participial noun serving as predicate, with no finite verb or causative form in the surface.\",\"representative_source_ids\":[\"QG-bfa1a0ea\",\"QF-a2b9c205\",\"MF-715b644f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:soft-emphatic-arrival","source_type":"word_analysis","support_id":"sup_7dc3b84509d3ff8c45bb","text":"{\"blocking_evidence\":null,\"headline\":\"softened emphatic arrival\",\"reader_payoff\":\"The reader hears the predicate arrive with sound texture that suits softness while still landing emphatically.\",\"reason\":\"The recited sequence brings tanwin assimilation into the doubled initial consonant of the predicate and a long vowel inside the word.\",\"representative_source_ids\":[\"QP-01d23a74\",\"QP-360562f2\",\"MP-df96db71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:face-day-reversal","source_type":"word_analysis","support_id":"sup_877bec6dcf65f62218cb","text":"{\"blocking_evidence\":null,\"headline\":\"same face-Day frame reversed\",\"reader_payoff\":\"The reader recognizes 88:8 as the matched positive half of the face-Day sorting opened in 88:2.\",\"reason\":\"The row evidence ties the opener to 88:2 and to face-verdict scenes such as 3:106 and 75:22; attachment evidence also confirms the repeated event-time frame.\",\"representative_source_ids\":[\"MI-23de2877\",\"MT-9d2f458d\",\"QE-14993b98\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:public-countenance-metonymy","source_type":"word_analysis","support_id":"sup_8e18a925d3e1d4d4e13b","text":"{\"blocking_evidence\":null,\"headline\":\"countenance as public manifestation\",\"reader_payoff\":\"The reader sees final condition made legible on the public human surface rather than reported as hidden inward feeling.\",\"reason\":\"The accepted V4 face/front branch supports concrete countenance, and the local predicate makes that countenance carry the persons' condition.\",\"representative_source_ids\":[\"QS-2f64ddde\",\"QS-8742d6bd\",\"MS-9beca740\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:8:1:1","source_type":"qac_morpheme","support_id":"sup_918434dcee8756d7fb04","text":"{\"lemma_ar\":\"وَجْه\",\"morph_features\":\"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:8:1:1\",\"qac_word_ref\":\"88:8:1\",\"root_ar\":\"و ج ه\",\"surface_ar\":\"وُجُوهٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2:medial-hinge","source_type":"word_analysis","support_id":"sup_91bb5465ac77638d3d95","text":"{\"blocking_evidence\":null,\"headline\":\"time inserted between face and state\",\"reader_payoff\":\"The reader sees the Day stand between visible subject and final ease, making the state event-bound rather than timeless.\",\"reason\":\"Attachment evidence makes the word an adverbial for the predicate, and word order places it between subject and predicate.\",\"representative_source_ids\":[\"QT-2fc20481\",\"QT-559d3a31\",\"QY-03fef36b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1","source_type":"word_analysis","support_id":"sup_a6530e9ec8096fbf1743","text":"{\"gloss_range\":\"indefinite broken-plural faces as the visible subject of the nominal scene\",\"prose\":\"{{ar:وُجُوهٌۭ}} ({{tr:wujūhun}}) opens the positive scene with indefinite broken-plural faces, not with a named people or a carried-over food-chain pronoun. As a nominative subject in a verbless clause, the word makes visible countenances the bearers of the state that will land at the end of the ayah. The face is both literal surface and public manifestation: the persons are read through the front by which they are encountered, while the wider root pressure of orientation, confrontation, and standing remains narrowed to what concrete faces can display. The reprise of the face-Day opener from 88:2 puts these faces under the same judgment tableau, but the predicate reverses the outcome; related face-verdict scenes such as 3:106 and 75:22 show why countenances are a natural public surface for disclosed status. Even the sound and form keep the group open and event-bound: the final nunation of the indefinite plural carries into {{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) before the predicate names their ease.\",\"root_display\":\"{{ar:و ج ه}} ({{tr:w-j-h}})\",\"root_gloss_range\":\"face, front, outward aspect, orientation, confrontation, and status; the local noun selects concrete countenances while allowing public-facing and status-bearing pressure\",\"surface_display\":\"{{ar:وُجُوهٌۭ}} ({{tr:wujūhun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2:same-frame-two-outcomes","source_type":"word_analysis","support_id":"sup_af4f6f70871fb0d02036","text":"{\"blocking_evidence\":null,\"headline\":\"one Day-frame holds opposed faces\",\"reader_payoff\":\"The reader keeps the humbled and eased groups under one event-time, so contrast comes from the predicates rather than from different timelines.\",\"reason\":\"The same deictic time-marker appears in 88:2 and 88:8, and the critical rows link the repeated frame to face-disclosure scenes such as 75:22.\",\"representative_source_ids\":[\"QE-6694f979\",\"ME-ef2b9be9\",\"QY-217402b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:orientation-status-pressure","source_type":"word_analysis","support_id":"sup_b0b0facee77e0b3658bd","text":"{\"blocking_evidence\":null,\"headline\":\"front-facing and status pressure kept local\",\"reader_payoff\":\"The reader notices that the faces are exposed fronts under encounter and public standing, while the word still means faces here.\",\"reason\":\"V4 lists orientation, facing, and status branches for the root, but QAC marks the local surface as a concrete noun, so those branches qualify the image without replacing the face sense.\",\"representative_source_ids\":[\"QS-3012f0b9\",\"QS-803559b5\",\"QS-912f7785\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:1:indefinite-visible-subject","source_type":"word_analysis","support_id":"sup_bd96908baa70d4a7e86d","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite faces as fresh subject\",\"reader_payoff\":\"The reader notices a newly introduced visible class of persons, not a named group or a continuation of the prior food scene.\",\"reason\":\"QAC and attachment evidence identify the word as an indefinite nominative broken-plural subject of a nominal clause, with the predicate supplied by {{ar:نَّاعِمَةٌۭ}} ({{tr:nāʿimatun}}).\",\"representative_source_ids\":[\"QG-a020b9ee\",\"QG-917e902b\",\"MG-d8e91720\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:2","source_type":"word_analysis","support_id":"sup_ca18583eefc7c8c19012","text":"{\"gloss_range\":\"deictic temporal adverbial compound meaning on that Day, at the already evoked event-time\",\"prose\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) is the middle word and the event-frame of the clause. Grammatically it functions as a temporal adverbial for the state in {{ar:نَّاعِمَةٌۭ}} ({{tr:nāʿimatun}}), but its compound form does more than mark ordinary duration: {{ar:يَوْمَ}} ({{tr:yawma}}) is fused with the deictic {{ar:إِذٍ}} ({{tr:idhin}}), so the Day points back to the overwhelming event already opened in 88:1 and repeated in 88:2. The root's broad day and occasion range is therefore narrowed to a singular decisive disclosure-time. Its placement between faces and ease makes the Day the hinge through which visible identity becomes verdict, and the repeated frame keeps the blessed faces in the same event as the humbled faces of 88:2. That also lets a wider face-Day pattern, including 75:22, stand behind the local scene without displacing the local syntax. The hamza and final nunation keep the deictic compression audible inside the three-word tableau.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"ordinary day, open time span, event-day, marked divine days, and the yawm-idh construction; the local compound selects a singular deictic event-frame\",\"surface_display\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:boundary-from-deficit-to-ease","source_type":"word_analysis","support_id":"sup_cf893a319161951edb49","text":"{\"blocking_evidence\":null,\"headline\":\"failed sufficiency becomes manifested ease\",\"reader_payoff\":\"The reader feels the scene turn from unreleased hunger and failed benefit into a stable visible condition of comfort.\",\"reason\":\"The word follows the prior condemned-provision unit and opens the blessed sequence as a nominal predicate before the satisfaction of 88:9.\",\"representative_source_ids\":[\"QB-06cce4c3\",\"QB-62d46f8b\",\"QB-c837c82a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:8:3:softness-bounty-visible","source_type":"word_analysis","support_id":"sup_f6199249c87161911b7c","text":"{\"blocking_evidence\":null,\"headline\":\"softness and bounty made visible\",\"reader_payoff\":\"The reader feels the blessed condition as visible smooth composure, delight, and bestowed sufficiency on the face.\",\"reason\":\"V4 supports pleasant well-being, favor, softness, and easeful living branches; local predication on faces selects those pressures while excluding remote root branches.\",\"representative_source_ids\":[\"QS-5754f75c\",\"QS-db23f18a\",\"MS-79601afe\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001525/B002","root_001630/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001630","role":"The bodily face and outward front provide the visible surface on which the state appears.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001525","role":"Softness and easeful living supply a state that is simultaneously material, bodily, and experiential.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"changed_reading":{"after":"The faces visibly carry softened, unstrained ease; bodily appearance and lived condition coincide.","before":"Some faces look pleasant."},"confidence":"strong","focus_anchor":"وجوه at word 1 is the observer-facing surface, while ناعمة at word 3 carries softness and easeful living.","mechanism":"The predicate transfers both tactile softness and an unstrained mode of life onto the visible front, making condition legible as countenance.","model_id":"baseline_visible_ease"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_visible_ease","source_type":"hft","support_id":"sup_cd28e438ad3004719364","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001525/B001","root_001630/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001630","role":"Face as self makes the visible countenance a compact reference to the whole person.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"Bounty and good condition extend the predicate from appearance to the person's total flourishing.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"changed_reading":{"after":"Whole persons, shown through their faces, stand in a condition of received bounty and flourishing.","before":"The adjective describes facial texture or expression alone."},"confidence":"strong","focus_anchor":"The face at word 1 can stand for the person, and ناعمة at word 3 can denote bounty and good condition.","mechanism":"Face-for-self expands the adjective beyond skin or expression: the whole person is presented through the part that meets others, while bounty names the person's encompassing condition.","model_id":"baseline_whole_person_flourishing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_whole_person_flourishing","source_type":"hft","support_id":"sup_2b6d1ab8539602b9597e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001525/B003","root_001630/B002","root_001630/B008"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001630","role":"Orientation and destination turn the plural faces into plural ways of facing or proceeding.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B008","mapped_root_id":"root_001630","role":"The proper aspect or sound course gives the orientation a normative rather than merely spatial value.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001525","role":"The praise branch supplies approval, allowing the predicate to commend how these faces are directed.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"changed_reading":{"after":"Their very facing or course is excellent and rightly ordered, with comfort as one consequence of that orientation.","before":"Faces merely display comfort."},"confidence":"exploratory","focus_anchor":"وجوه at word 1 can be directions or proper courses, while the root of ناعمة at word 3 can perform praise.","mechanism":"The clause can carry a directional layer in which the subjects' facings are not only comfortable but commendable and sound.","model_id":"baseline_approved_orientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_approved_orientation","source_type":"hft","support_id":"sup_104a96babe00c0572e21","trust":"legacy_unbound"}]}
</lane_packet_json>
