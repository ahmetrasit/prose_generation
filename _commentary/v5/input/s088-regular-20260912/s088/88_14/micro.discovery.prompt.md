# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:14**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_14/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:14",
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
{"branch_registry":[{"boundary":"Dal yalnızca kulpsuz ya da kulaksız içme kabını kapsar; çalgı, oyun, içme eylemi ve beden özelliği anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_001328/B001","candidate_links":[{"candidate_id":"cand_a8d8da7c689c96398dbe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"kulpsuz içme kabı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir içeceğin konduğu ve içildiği kap türüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın tutma kulpu ya da yan kulağı bulunmaz."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kap, bardak, testi veya dökme kabı türleriyle açıklanabilir; bir anlatım yuvarlak başlı oluşunu da belirtir."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın içme kabı olma işlevini ve kulp ya da kulak taşımama sınırını birlikte veren genel karşılıktır.","boundary_detail":"Dal yalnızca kulpsuz ya da kulaksız içme kabını kapsar; çalgı, oyun, içme eylemi ve beden özelliği anlamlarını kapsamaz.","branch_image_ar":"الكوب بلا عروة","concept_gloss":"kulpsuz içme kabı","contextual_glosses":[{"applicability":"Kabın özellikle bardak türünde düşünüldüğü bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Testi veya dökme kabı olarak açıklanan öteki kap görünümlerini dışarıda bırakır.","preserves":"İçme kabı olmayı ve kulpsuzluk özelliğini korur."},"facet_ids":["F001","F002","F003"],"text":"kulpsuz bardak","usage_role":"contextual"},{"applicability":"Yuvarlak başlı ve yan kulağı bulunmayan kap betiminin öne çıktığı özel bağlamda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yuvarlak başlılık belirtmeyen genel kulpsuz içme kabı kapsamını daraltır.","preserves":"Kulaksız olma sınırını ve kap niteliğini korur."},"facet_ids":["F001","F002","F003"],"text":"kulaksız yuvarlak kap","usage_role":"explanatory"}],"definition":"İçecek koymak ve içmek için kullanılan, kulpu ya da kulağı bulunmayan kaptır. Kaynaklarda kap türü değişik biçimlerde açıklansa da kulpsuzluk ortak sınırdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir içeceğin konduğu ve içildiği kap türüdür."},{"facet_id":"F002","role":"core","statement":"Kabın tutma kulpu ya da yan kulağı bulunmaz."},{"facet_id":"F003","role":"source_variant","statement":"Kap, bardak, testi veya dökme kabı türleriyle açıklanabilir; bir anlatım yuvarlak başlı oluşunu da belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kulplu bardakları da kapsayabildiği için dalın kulpsuzluk sınırını aşar.","collision":null,"fit":"broadening","loses":null,"preserves":"İçecek koymaya ve içmeye yarayan kap olma yönünü korur."},"text":"bardak"}],"identity_rationale":"Kaynak ifadesi, bu dalı kulpu ya da kulağı bulunmayan bir içme kabı olarak açıkça sınırlar. Kap türüne ilişkin bardak, testi ve dökme kabı gibi anlatımlar ile yuvarlak başlı olma ayrıntısı, aynı kulpsuz kap çekirdeğinin değişik kaynak görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kulpu ya da kulağı olmayan içme kabı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kulpu ya da kulağı olmayan içme kapları"}],"lexicalization_note":"Tanım yalın biçimin kap anlamıyla sınırlıdır ve başka dallardaki eylem ya da özel kullanım anlamlarını bu dala taşımaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; kulpsuzluk, içerikle adlandırma ve ölçme işlevi sınırlarını en açık gösteren üç karşılaştırma seçildi. Öteki adaylar yalnız genel kap alanını paylaştığı veya bu dalın eşsesli diğer anlamları olduğu için ayrıca yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kulpsuzluk tanımın kurucu sınırıdır; komşu dalda bu biçim şartı yoktur ve kapsam ölçü işlevi ile o kaptan içme eylemine uzanabilir.","focus_only":"Bu dal, içme kabının kulpu ya da kulağı bulunmamasını zorunlu kılar.","gloss":"bardak ve ölçü kabı","neighbor_only":"Komşu dal, kabı belirli bir topluluğun bardağı veya bir ölçü kabı olarak ele alır ve onunla içme eylemine de uzanır.","neighbor_ref":"root_001130/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da içmek için kullanılan kapları adlandırır."},{"boundary_match":"partial","distinction":"Odak dalı biçimsel olarak kulpsuz bir kabı adlandırır; komşu dalın sınırı ise kap ile içeriğinin birlikte veya birbirinin yerine anılmasına dayanır.","focus_only":"Kulpu ya da kulağı olmayan kabın kendisini gösterir.","gloss":"içeceğiyle birlikte kap","neighbor_only":"Kabın içindeki içecekle birlikte düşünülmesine, yalnız kaba veya yalnız içeceğe aktarılmasına izin verir.","neighbor_ref":"root_001277/B001","relation_type":"near_neighbor","shared_zone":"İki dal da içecek sunmaya yarayan bir kap çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dalının ayırıcı yanı kulpsuzluk iken komşu dalın ayırıcı yanı ölçü kabı olarak da iş görmesi ve ölçü değeridir.","focus_only":"İçme amacı ve kulpsuzluk birlikte zorunludur.","gloss":"içme ve ölçme kabı","neighbor_only":"Komşu kap hem içme hem ölçme işlevi görebilir ve belirli bir ölçü değerine bağlanır.","neighbor_ref":"root_000892/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de içmede kullanılabilen kap türleridir."}],"source_phrase_ar":"الكوب القدح لا عروة له (maqayis;mufradat)؛ الكوب كوز لا عروة له (ayn;sihah)؛ الكوب الإبريق بلا عروة (jamhara)؛ الكوب الكوز المستدير الرأس الذي لا أذن له (tahdhib)","source_summary":"Kaynaklar kulpu ya da kulağı olmayan içme kabı çekirdeğinde birleşir. Kabın bardak, testi veya dökme kabı olarak betimlenmesi ve yuvarlak başlılık ayrıntısı, ortak sınırı değiştirmeyen anlatım çeşitleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الكوب والقدح والكوز والإبريق إذا كان إناء للشرب بلا عروة أو بلا أذن","what_is_not_ar":"ليس الكوبة الطبل ولا الشطرنجة ولا الشرب بالكوب ولا دقة العنق وعظم الرأس"},"support_links":["sup_a119917d3222eece4e04"]},{"boundary":"Dal, birbirine alternatif çalgı türlerini kapsayan bir adlandırmadır; bütün özellikleri aynı araçta birleştirmez.","branch_kind":"bare","branch_ref":"root_001328/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eğlence amacıyla çalınan bir araçtır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Vurmalı çalgı görünümü davul ya da küçük ve ortası dar bir davuldur."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir görünüm, uzun saplı telli bir çalgıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Üflemeli görünüm, bir deri parçasına birleştirilen ve içine üflenen borulardan oluşur."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alternatif araç türlerini tek bir birleşik yapı gibi göstermeden dalın bütün kaynak kapsamını veren açıklayıcı karşılıktır.","boundary_detail":"Dal, birbirine alternatif çalgı türlerini kapsayan bir adlandırmadır; bütün özellikleri aynı araçta birleştirmez.","branch_image_ar":"الكوبة آلة لهو","concept_gloss":"davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı","contextual_glosses":[{"applicability":"Vurmalı çalgı görünümünün söz konusu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun saplı telli çalgı ile deriye birleştirilmiş üfleme boruları görünümlerini dışarıda bırakır.","preserves":"Eğlence için çalınan vurmalı araç görünümünü korur."},"facet_ids":["F001","F002"],"text":"davul","usage_role":"contextual"},{"applicability":"Telli araç görünümünün açıkça kastedildiği bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davul ve deriye birleştirilmiş üfleme boruları görünümlerini dışarıda bırakır.","preserves":"Eğlence çalgısı olmayı ve telli araç görünümünü korur."},"facet_ids":["F001","F003"],"text":"uzun saplı telli çalgı","usage_role":"contextual"},{"applicability":"Deri parçasında birleştirilen boruların üflenerek çalındığı araç görünümünü açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davul ve uzun saplı telli çalgı görünümlerini dışarıda bırakır.","preserves":"Üfleme borularını, deri içinde birleşmelerini ve çalınma biçimini korur."},"facet_ids":["F001","F004"],"text":"deriye geçirilmiş üfleme boruları","usage_role":"explanatory"}],"definition":"Eğlence amacıyla çalınan bir çalgıyı adlandırır. Kaynaklara göre bu çalgı bir davul, küçük ve ortası dar bir davul, uzun saplı telli bir çalgı veya deriye birleştirilmiş ve üflenerek çalınan borular olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eğlence amacıyla çalınan bir araçtır."},{"facet_id":"F002","role":"source_variant","statement":"Vurmalı çalgı görünümü davul ya da küçük ve ortası dar bir davuldur."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir görünüm, uzun saplı telli bir çalgıdır."},{"facet_id":"F004","role":"source_variant","statement":"Üflemeli görünüm, bir deri parçasına birleştirilen ve içine üflenen borulardan oluşur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Eğlence amacıyla ilişkilendirilmeyen ve kaynakta verilen türlerden olmayan bütün çalgıları da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Çalınan bir araç olma yönünü korur."},"text":"çalgı"}],"identity_rationale":"Kaynak ifadesi bu adı eğlence için çalınan bir araçla ilişkilendirir; ancak tek bir araç yapısı vermez. Davul ve küçük, ortası dar davul anlatımlarının yanında uzun saplı telli bir çalgı ile deriye birleştirilmiş üfleme boruları da yer alır. Bu nedenle dal korunabilir, fakat bu araçların özellikleri tek bir birleşik çalgının parçaları gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"davul veya küçük, ortası dar davul"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"uzun saplı telli çalgı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"deri parçasına birleştirilip üflenerek çalınan borular"}],"lexicalization_note":"Tanım yalın biçimin çalgı anlamını verir; belirli bir araç türünü bütün dalın tek anlamı saymaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; davul, telli çalgı ve üfleme boruları görünümlerinin sınırlarını keskinleştiren üç aday seçildi. Ses, deri ve şarkı alanındaki öteki adaylar aracın kendisiyle yeterli anlam örtüşmesi taşımadığından yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tek yüzlü belirli bir davula bağlıdır; odak dalında davul yalnızca alternatiflerden biridir ve tek yüzlülük koşulu bulunmaz.","focus_only":"Davul dışında uzun saplı telli çalgı ve deriye birleştirilmiş üfleme boruları görünümlerini de kapsar.","gloss":"tek yüzlü davul","neighbor_only":"Belirli olarak tek yüzlü bir davul türünü gösterir.","neighbor_ref":"root_001281/B012","relation_type":"near_synonym","shared_zone":"İki dal da bir davul türünü adlandırabildiği ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalındaki üflemeli araç birden çok borunun deride birleşmesiyle tanımlanır; komşu dal tek kamıştan yapılan çoban aracıdır.","focus_only":"Bir deri parçasında birleştirilmiş birden çok üfleme borusu görünümünü içerir ve başka çalgı türlerine de uzanır.","gloss":"çoban borusu","neighbor_only":"Çobanın üflediği tek bir kamış boru türünü gösterir.","neighbor_ref":"root_001586/B010","relation_type":"near_neighbor","shared_zone":"Her iki dalın bir görünümünde üflenerek çalınan boru biçimli araç vardır."},{"boundary_match":"partial","distinction":"Odak dalındaki telli görünüm daha genel bir uzun saplı çalgıdır ve dal başka araç türlerini de kapsar; komşu dal belirli bir telli aracın vurularak çalınmasına bağlıdır.","focus_only":"Vurmalı ve üflemeli araçlara da uzanan birden çok alternatif çalgı görünümü vardır.","gloss":"vurularak çalınan telli çalgı","neighbor_only":"Vurularak çalınan belirli bir telli çalgıyı gösterir.","neighbor_ref":"root_000650/B006","relation_type":"near_neighbor","shared_zone":"İki dal da telli bir çalgıyı gösterebilir."}],"source_phrase_ar":"الكوبة الطبل للعب (maqayis)؛ الكوبة الطبل الذي يلعب به (mufradat)؛ الكوبة الطبل (jamhara)؛ الطبل والطنبور (jamhara)؛ الكوبة الطبل الصغير المخصر (sihah)؛ الكوبة قصبات تجمع في قطعة أديم ويزمر فيها (ayn)","source_summary":"Kanıt, eğlence için çalınan araç çekirdeğini ortaklaştırırken aracın türünü değişik biçimlerde verir: davul ve küçük, ortası dar davul; uzun saplı telli çalgı; deriye birleştirilmiş üfleme boruları. Bunlar tek bir aracın birleşik özellikleri değil, adın alternatif göndergeleridir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الكوبة للطبل والطبل الصغير المخصر والطبل الذي يلعب به والطنبور والقصبات المجموعة في أديم يزمر فيها","what_is_not_ar":"ليس الكوب إناء الشرب ولا الشطرنجة ولا إلصاق بعض الشيء ببعض"},"support_links":[]},{"boundary":"Dal yalnızca satranç oyununu adlandırır; aynı biçimle ilişkilendirilen çalgı anlamı bu dalın dışında kalır.","branch_kind":"bare","branch_ref":"root_001328/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"satranç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir tahta oyunu olan satrancı adlandırır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta verilen belirli oyunun Türkçedeki doğal ve eksiksiz adıdır.","boundary_detail":"Dal yalnızca satranç oyununu adlandırır; aynı biçimle ilişkilendirilen çalgı anlamı bu dalın dışında kalır.","branch_image_ar":"الكوبة الشطرنجة","concept_gloss":"satranç","contextual_glosses":[{"applicability":"Oyun niteliğinin açıkça belirtilmesinin yararlı olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyunun kimliğini ve oyun türünde oluşunu açıkça korur."},"facet_ids":["F001"],"text":"satranç oyunu","usage_role":"explanatory"}],"definition":"Karşılıklı oyuncuların taşları kurallı biçimde hareket ettirdiği satranç adlı tahta oyununu adlandıran kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir tahta oyunu olan satrancı adlandırır."}],"identity_rationale":"Kaynak ifadesi bu biçimi doğrudan satranç oyunuyla özdeşleştirir. Provisional dal çerçevesi bu açık oyun adını doğru yansıtır ve başka bir araç, kap veya eylem anlamını içeri almaz.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"satranç"}],"lexicalization_note":"Tanım yalın biçimin oyun adını verir ve aynı söz biçiminin başka dallardaki anlamlarını buna katmaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi. Adayların hiçbiri satrançla ikame edilebilir bir anlam ya da dal sınırını açıklayan yeterli bir örtüşme sunmadığı için komşu ayrımı yayımlanmadı; aynı söz biçiminin öteki anlamları yalnız eşseslidir.","source_phrase_ar":"الكوبة الشطرنجة (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, bu biçimin satranç oyununu adlandırdığını bildirir."}],"source_summary":"Bu dal için kanıt tek bir açık oyun anlamı verir ve kap, çalgı ya da eylem anlamlarına ilişkin bir genişleme bildirmez.","sources":["AY"],"what_is_ar":"الكوبة إذا أريد بها الشطرنجة","what_is_not_ar":"ليس الكوب إناء الشرب ولا الكوبة الطبل والطنبور والقصبات"},"support_links":[]},{"boundary":"Anlam, parçaları birbirinin üzerine getirip yapıştıran özel söyleyişle sınırlıdır; genel toplama veya bağlama anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_001328/B004","candidate_links":[{"candidate_id":"cand_1bfb14a66d613e571bc2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"üst üste getirip yapıştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bazı parçalar başka parçaların üzerine getirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst üste getirilen parçalar birbirine yapıştırılır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaların hem konum ilişkisini hem de yapışma sonucunu birlikte veren tam karşılıktır.","boundary_detail":"Anlam, parçaları birbirinin üzerine getirip yapıştıran özel söyleyişle sınırlıdır; genel toplama veya bağlama anlamı değildir.","branch_image_ar":"كُوب بعضه على بعض","concept_gloss":"üst üste getirip yapıştırmak","contextual_glosses":[{"applicability":"Nesne parçalarının karşılıklı konumu bağlamdan belli olduğunda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların birbirinin üzerinde olmasını ve yapışmasını birlikte korur."},"facet_ids":["F001","F002"],"text":"birbirinin üzerine yapıştırmak","usage_role":"contextual"}],"definition":"Bir şeyin bazı parçalarını öteki parçaların üzerine getirerek birbirine yapıştırmaktır. Üst üste yerleştirme ilişkisi ve parçaların tutunması birlikte kurucudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bazı parçalar başka parçaların üzerine getirilir."},{"facet_id":"F002","role":"core","statement":"Üst üste getirilen parçalar birbirine yapıştırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Üst üste getirme ve yapıştırma bulunmayan her türlü birleştirmeyi de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Ayrı parçalar arasında bağlantı kurulması yönünü korur."},"text":"birleştirmek"}],"identity_rationale":"Kaynak ifadesi, bazı parçaların birbirinin üzerine getirilerek birbirine yapıştırılmasını bildirir. Dal çerçevesi hem parçalar arasındaki üst üste gelme ilişkisini hem de bunun sonucundaki yapışmayı korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"parçalarını birbirinin üzerine getirip yapıştırmak"}],"lexicalization_note":"Tanım yalnızca parçaların birbirinin üzerine getirilmesini belirten tedarikli söyleyişe bağlıdır ve bunu yalın kökün genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; genel bağlantı, yana yapıştırma ve toplama anlamlarıyla kurulan üç karşılaştırma dalın konum ve sonuç sınırını yeterince gösterir. Öteki adaylar bu ayrımları tekrar ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı üst üste konmuş parçaların yapıştırılmasına bağlıdır; komşu dal konum ve yapıştırma şartı olmadan çok daha genel bağlantı ve birleşmeyi kapsar.","focus_only":"Parçaların birbirinin üzerine getirilmesi ve yapışması birlikte zorunludur.","gloss":"bağlamak ve birleştirmek","neighbor_only":"Somut ve soyut şeyler arasında genel bağlantı, süreklilik veya birleşme kurulmasına uzanır.","neighbor_ref":"root_001655/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ayrı şeylerin birbirine tutunması veya bağlanması sonucunu içerebilir."},{"boundary_match":"partial","distinction":"Odak dalının konum sınırı parçaların üst üste gelmesidir; komşu dalda yapışma özellikle yan tarafa yönelir.","focus_only":"Bir şeyin parçalarını birbirinin üzerine getirerek yapıştırır.","gloss":"yana yapıştırmak","neighbor_only":"Bir şeyi özellikle yana yapıştırmayı ve bu yana çekip yakın tutmayı anlatır.","neighbor_ref":"root_001356/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi başka bir yüzeye yapıştırma eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği genel toplama ve eklemedir; odak dalı ise bu işlemin üst üste konum ve yapışma yoluyla yapılmasına bağlıdır.","focus_only":"Üst üste getirme ve yapıştırarak tutturma sonucunu şart koşar.","gloss":"toplamak ve eklemek","neighbor_only":"Toplama, bir araya getirme, dikme ve çeşitli kapatma eylemlerine kadar uzanır.","neighbor_ref":"root_001283/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda ayrı parçalar bir araya getirilebilir."}],"source_phrase_ar":"بعضها كُوب على بعض أي ألزق (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, parçaları birbirinin üzerine getirip yapıştırma eylemini bildirir."}],"source_summary":"Kanıt, parçaların yalnız yan yana toplanmasını değil, birbirinin üzerine getirilip birbirine yapıştırılmasını anlatan sınırlı bir eylem anlamı verir.","sources":["AY"],"what_is_ar":"ما كان بمعنى ألصق بعضه على بعض","what_is_not_ar":"ليس الكوب إناء الشرب ولا الكوبة آلة اللهو"},"support_links":["sup_2d48a4347de983e702c4"]},{"boundary":"Dal kabın kendisini değil, o kap kullanılarak gerçekleştirilen içme eylemini gösterir.","branch_kind":"bare","branch_ref":"root_001328/B005","candidate_links":[{"candidate_id":"cand_60cb7a8c462fbfce811f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"kulpsuz içme kabından içmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir içeceği içme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçme eylemi kulpsuz bir içme kabı kullanılarak yapılır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçme eylemini ve bu eylemde kullanılan özel kap türünü birlikte veren karşılıktır.","boundary_detail":"Dal kabın kendisini değil, o kap kullanılarak gerçekleştirilen içme eylemini gösterir.","branch_image_ar":"الشرب بالكوب","concept_gloss":"kulpsuz içme kabından içmek","contextual_glosses":[{"applicability":"Söz konusu kabın içme kabı olduğu bağlamdan açıkça anlaşıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçme eylemini ve kulpsuz kabın kullanımını korur."},"facet_ids":["F001","F002"],"text":"kulpsuz kaptan içmek","usage_role":"contextual"}],"definition":"Bir içeceği kulpu bulunmayan içme kabını kullanarak içmektir. İçme eylemi çekirdek, kullanılan kap ise eylemi sınırlandıran araçtır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir içeceği içme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"İçme eylemi kulpsuz bir içme kabı kullanılarak yapılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kulpsuz içme kabı dışında başka yollarla gerçekleştirilen bütün içme eylemlerini de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"İçeceği alma eylemini korur."},"text":"içmek"}],"identity_rationale":"Kaynak ifadesi eylemi, içeceği belirli türde bir içme kabı kullanarak içmek biçiminde açıklar. Dal çerçevesi kabın kendisiyle içme eylemini birbirine karıştırmadan araç koşulunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kulpsuz içme kabından içmek"}],"lexicalization_note":"Tanım yalın eylem biçiminin kap kullanarak içme anlamını verir; kap adını eylemin yerine geçirmez.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; aşırı içme, sabah içme ve kullanılan kabın kendisiyle yapılan karşılaştırmalar araç koşulunu en açık biçimde ayırır. Yutma, yudum ve başka kap adları aynı sınırı daha az doğrudan gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı miktar veya doyma bildirmez, yalnız aracı belirler; komşu dal kullanılan kaptan bağımsız olarak aşırılık ve doymama bildirir.","focus_only":"İçme eylemini kullanılan kulpsuz kapla sınırlar.","gloss":"çok içip doymamak","neighbor_only":"Çok içme, doymama ve aralıklarla içmeyi sürdürme koşullarını taşır.","neighbor_ref":"root_000717/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalın çekirdeğinde bir içeceği içme eylemi vardır."},{"boundary_match":"partial","distinction":"Odak dalındaki koşul kullanılan kap, komşu daldaki koşul ise günün sabah vaktidir; komşu ayrıca yeme ve sunmaya uzanır.","focus_only":"İçmeyi kulpsuz bir kabın kullanımına bağlar.","gloss":"sabah içmek","neighbor_only":"İçme, yeme veya sunma eylemini sabah vaktine bağlar.","neighbor_ref":"root_000839/B003","relation_type":"near_neighbor","shared_zone":"İki dal da belirli bir koşulla sınırlandırılmış içme eylemini içerebilir."},{"boundary_match":"thematic_only","distinction":"Odak dalı bir içme eylemidir; komşu dal ise o eylemde araç olabilen nesnedir, bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Kulpsuz kabı kullanarak yapılan eylemi gösterir.","gloss":"kulpsuz içme kabı","neighbor_only":"Eylemde kullanılan kulpsuz içme kabının kendisini gösterir.","neighbor_ref":"root_001328/B001","relation_type":"thematic","shared_zone":"Aynı içme olayında biri eylemi, öteki kullanılan aracı adlandırır."}],"source_phrase_ar":"كاب يكوب إذا شرب بالكوب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, eylemi kulpsuz içme kabını kullanarak içmek biçiminde açıklar."}],"source_summary":"Kanıt, genel içme eylemini kullanılan araç bakımından sınırlar: içecek, kulpsuz bir içme kabı aracılığıyla içilir.","sources":["TA"],"what_is_ar":"الفعل كاب يكوب إذا شرب بالكوب","what_is_not_ar":"ليس الكوب نفس إناء الشرب ولا الكوبة آلة اللهو"},"support_links":["sup_00919c056b1504d612bc"]},{"boundary":"Dal, ince boyun ve büyük baş özelliklerinin birleşimidir; boynun yalnız uzun, eğik veya uzatılmış olması yeterli değildir.","branch_kind":"bare","branch_ref":"root_001328/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"ince boyunluluk ve iri başlılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boyun ince yapıdadır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baş büyük yapıdadır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birleşik beden özelliğinin iki zorunlu parçasını da açıkça veren genel karşılıktır.","boundary_detail":"Dal, ince boyun ve büyük baş özelliklerinin birleşimidir; boynun yalnız uzun, eğik veya uzatılmış olması yeterli değildir.","branch_image_ar":"دقة العنق وعظم الرأس","concept_gloss":"ince boyunluluk ve iri başlılık","contextual_glosses":[{"applicability":"Beden görünümünün tam bir söz öbeğiyle açıklanmasının gerektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnce boyun ve iri baş özelliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"ince boyunlu ve iri başlı olma","usage_role":"explanatory"}],"definition":"Boynun ince, başın ise büyük olmasıyla oluşan birleşik beden yapısıdır. Her iki oransal özellik de tanımın zorunlu parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boyun ince yapıdadır."},{"facet_id":"F002","role":"core","statement":"Baş büyük yapıdadır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başın büyük olması biçimindeki ikinci zorunlu özelliği düşürür.","preserves":"Boynun ince olması özelliğini korur."},"text":"ince boyunluluk"}],"identity_rationale":"Kaynak ifadesi boynun inceliği ile başın büyüklüğünü birlikte veren bir beden özelliğini açıkça bildirir. Dal çerçevesi iki özelliği de korur ve yalnız boyun inceliğine ya da yalnız baş büyüklüğüne indirgemez.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"boynun inceliği ve başın büyüklüğü"}],"lexicalization_note":"Tanım yalın biçimin birleşik beden özelliğini verir ve boyunla ilgili başka hareket ya da biçim anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; boyun uzunluğu ve genel beden inceliğiyle ilgili üç aday, odak dalındaki ince boyun ile büyük baş birleşimini en iyi sınırlar. Boyun hareketi, boyun yanı ve kısa boy gibi adaylar daha uzak kaldığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı incelik ve büyük baş oranına dayanır; komşu dal uzunluk, uzatma ve yükseltmeye dayanır, dolayısıyla iki betim birbirinin yerine geçmez.","focus_only":"İnce boyunla birlikte büyük baş özelliğini zorunlu kılar.","gloss":"uzun ve uzatılmış boyun","neighbor_only":"Boynun uzunluğu, uzatılması veya başın yukarı kaldırılması özelliklerini içerir.","neighbor_ref":"root_000706/B002","relation_type":"same_field","shared_zone":"Her iki dal da boynun görünüşüne ilişkin bir beden özelliğini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalında uzunluk şartı yoktur ve büyük baş zorunludur; komşu dal uzunluğu öne çıkarır ve baş büyüklüğü bildirmez.","focus_only":"Boynun inceliğini başın büyüklüğüyle birlikte betimler.","gloss":"uzun kişi veya uzun boyun","neighbor_only":"Kişinin veya boynun uzun olmasını betimler.","neighbor_ref":"root_001405/B007","relation_type":"same_field","shared_zone":"İki dal da kişinin boyun ve beden oranlarıyla ilgili görünüşünü betimler."},{"boundary_match":"field_only","distinction":"Odak dalı iki belirli beden bölümünün karşıt oranını tanımlar; komşu dal bütün bedenin ince ve sıkı yapısını anlatır.","focus_only":"İnce boyun ile büyük baş arasındaki özel oranı gösterir.","gloss":"ince ve sıkı yapılı beden","neighbor_only":"Bedenin bütünüyle sıkı, kıvrak veya ip gibi ince görünmesini gösterir.","neighbor_ref":"root_001422/B002","relation_type":"same_field","shared_zone":"Her iki dal insan bedeninin ince veya narin görünümüyle ilişkilidir."}],"source_phrase_ar":"الكَوَب دقة العنق وعظم الرأس (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, ince boyun ile büyük başın birlikte bulunduğu beden özelliğini bildirir."}],"source_summary":"Kanıt, boyun inceliği ile baş büyüklüğünü tek bir birleşik beden betimi içinde verir; iki özellikten biri çıkarıldığında dalın anlamı eksik kalır.","sources":["TA"],"what_is_ar":"الكَوَب في وصف دقة العنق وعظم الرأس","what_is_not_ar":"ليس الكوب إناء الشرب ولا الفعل كاب يكوب في الشرب"},"support_links":[]},{"boundary":"Çekirdek, nesneyi yerine indirme ve konduğu yerle sınırlıdır; kalıp kullanımlar ayrı render edilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B001","candidate_links":[{"candidate_id":"cand_a8d8da7c689c96398dbe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"bir şeyi indirip yerine koyma; konduğu yer","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne kaldırmanın karşıtı olarak aşağı indirilir ya da elden bırakılıp yerine konur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem alanından nesnenin konduğu yer veya konum adı gelişir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kanıt, kimi yerde indirmeyi öne çıkarır, kimi yerde daha geniş bir yerine koyma işini kapsar."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın dal için nesnenin indirilip belirli yere konmasını ve bundan çıkan yer adını kapsar.","boundary_detail":"Çekirdek, nesneyi yerine indirme ve konduğu yerle sınırlıdır; kalıp kullanımlar ayrı render edilir.","concept_gloss":"bir şeyi indirip yerine koyma; konduğu yer","contextual_glosses":[{"applicability":"Nesnenin elden bırakılıp veya indirilip belirli bir yere konduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneye yapılan koyma işini korur."},"facet_ids":["F001"],"text":"yerine koymak","usage_role":"contextual"},{"applicability":"Eylemin sonucunda ortaya çıkan yer veya konum adı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer adını ve konma ilişkisini korur."},"facet_ids":["F002"],"text":"konduğu yer","usage_role":"contextual"}],"definition":"Bir şeyi eldeki ya da yüksek konumdan indirip belirli bir yere koyma; aynı alan, nesnenin konduğu yeri de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne kaldırmanın karşıtı olarak aşağı indirilir ya da elden bırakılıp yerine konur."},{"facet_id":"F002","role":"extension","statement":"Eylem alanından nesnenin konduğu yer veya konum adı gelişir."},{"facet_id":"F003","role":"source_variant","statement":"Kanıt, kimi yerde indirmeyi öne çıkarır, kimi yerde daha geniş bir yerine koyma işini kapsar."}],"identity_rationale":"Kaynak ifadesi bu dalın çekirdeğini bir şeyi aşağı indirme, elden bırakma ya da kaldırmanın karşıtı olarak yerine koyma anlamında kurar. Yapı kurma ve kayıt ortaya çıkarma gibi kullanımlar ancak ayrı kalıplar olarak korunmalıdır; yalın dalın genel anlamı bunlara genişletilmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yerine koymak veya elden bırakmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yer, konum"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yerine konmuş şey"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ev yapmak veya kurmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yazılı kayıtları ortaya çıkarmak"}],"lexicalization_note":"mixed_non_bare olduğu için yalın koyma ve yer anlamı, kalıp bağlı yapı kurma ya da kayıt gösterme kullanımlarından ayrı tutulur.","neighbor_coverage_note":"Listelenen adayların tamamı değerlendirildi; yayımlananlar okuyucunun en kolay karıştırabileceği dikey hareket, sabitlenme ve deve boynu alçaltma sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalda hareket aşağıya veya belirlenmiş yere doğrudur; komşuda hareket yukarıya ve yükseltmeye doğrudur.","focus_only":"Odak dal nesneyi aşağı indirip yerine koyar.","gloss":"indirme ile yükseltme","neighbor_only":"Komşu dal nesneyi yukarı kaldırma ve yüksek konuma çıkarma yönündedir.","neighbor_ref":"root_000582/B001","relation_type":"antonym","shared_zone":"İkisi de nesnenin dikey konumunu değiştirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici olan nesnenin konmasıdır; komşuda belirleyici olan nesnenin orada kalıcı biçimde tutunmasıdır.","focus_only":"Odak dal nesneyi bir yere koyma eylemini de içerir.","gloss":"koyma ile sabit kalma","neighbor_only":"Komşu dal yerinde sabit kalma, yapışma veya sağlamlaştırma sonucunu öne çıkarır.","neighbor_ref":"root_000562/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir yerle bağlantı kuran nesneyi düşünür."},{"boundary_match":"partial","distinction":"Odak dal genel yerleştirme anlamındadır; komşu dal yalnızca binicinin binmesini sağlayan hayvan duruşunu anlatır.","focus_only":"Odak dal her tür nesneyi yerine koyma ve konulan yeri kapsar.","gloss":"genel indirme ile binme için alçaltma","neighbor_only":"Komşu dal devenin başını veya boynunu binme amacıyla alçaltmasına bağlıdır.","neighbor_ref":"root_001657/B013","relation_type":"near_neighbor","shared_zone":"İkisi de aşağı yönlü bir hareketi kullanır."}],"source_summary":"Ortak kanıt, anlamı bir nesneyi aşağı indirme, elden bırakma veya kaldırmanın karşıtı olarak belirli bir yere koyma ekseninde toplar. Aynı kanıt bu eylemden konulan yer adının da çıktığını gösterir."},"support_links":["sup_a119917d3222eece4e04"]},{"boundary":"Doğum çekirdektir; özel gebe kalma zamanı aynı dalda ayrı bir sınırlı facet olarak kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"doğumla yükü bırakma ve özel gebe kalma zamanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın çocuğunu veya taşıdığı gebelik yükünü doğumla bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı malzeme, gebeliğin adetin hemen öncesindeki temizlik sonunda başlamasını özel olarak adlandırır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğum çekirdeğini ve adet döngüsü sınırındaki özel gebelik zamanı kullanımını birlikte temsil eder.","boundary_detail":"Doğum çekirdektir; özel gebe kalma zamanı aynı dalda ayrı bir sınırlı facet olarak kalır.","concept_gloss":"doğumla yükü bırakma ve özel gebe kalma zamanı","contextual_glosses":[{"applicability":"Kadın öznesinin çocuğunu dünyaya getirdiği gerçek doğum bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın öznesi ve doğumla bırakma anlamını korur."},"facet_ids":["F001"],"text":"çocuğunu doğurmak","usage_role":"contextual"},{"applicability":"Gebeliğin temizlik süresinin sonunda ve adetin hemen öncesinde başladığını anlatan özel ad için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Döngü sınırındaki gebelik zamanı bilgisini korur."},"facet_ids":["F002"],"text":"adet öncesi gebelik başlangıcı","usage_role":"explanatory"}],"definition":"Kadının gebelik yükünü doğumla bırakmasını anlatır; ayrıca adetin hemen öncesindeki temizlik sonunda oluşan gebelik için özel bir ad kullanımını içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın çocuğunu veya taşıdığı gebelik yükünü doğumla bırakır."},{"facet_id":"F002","role":"specialization","statement":"Aynı malzeme, gebeliğin adetin hemen öncesindeki temizlik sonunda başlamasını özel olarak adlandırır."}],"identity_rationale":"Kaynak ifadesi kadının çocuğunu veya gebelik yükünü doğumla bırakmasını açıkça verir, fakat aynı dalda adetin hemen öncesindeki temizlik sonunda oluşan gebelik için özel bir kullanım da yer alır. Bu yüzden dal doğum olarak kullanılabilir, ancak gebelik zamanına ait yan kullanımı gizlenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının çocuğunu doğurması"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"adet öncesi temizlik sonunda gebe kalma"}],"lexicalization_note":"mixed_non_bare olduğu için kadınla kurulan doğum kalıbı ile yalın zaman adı birbirine karıştırılmaz.","neighbor_coverage_note":"Tüm adaylar kontrol edildi; yayımlanan ayrımlar doğum, doğum sancısı ve tamamlanmamış düşme sınırlarını özellikle netleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Doğum bağlamında çok yakındırlar, fakat odak dalın özel zaman adı komşuda çekirdek değildir.","focus_only":"Odak dal doğumun yanında adet döngüsüne bağlı özel gebelik zamanı adını da taşır.","gloss":"doğum","neighbor_only":"Komşu dal doğum olayını ve doğum zamanının gelmesini daha genel biçimde kapsar.","neighbor_ref":"root_001683/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de çocuğun dünyaya gelmesi ve gebelikten çıkış alanındadır."},{"boundary_match":"partial","distinction":"Odak dal sonuçlanan doğumu veya gebelik zamanını adlandırır; komşu dal doğuma yaklaşan bedensel süreçleri adlandırır.","focus_only":"Odak dal doğumun gerçekleşmesini veya özel gebe kalma zamanını anlatır.","gloss":"doğum ile doğum sancısı","neighbor_only":"Komşu dal doğum sancısı, yakın doğum ve rahimdeki hareket alanındadır.","neighbor_ref":"root_001406/B002","relation_type":"near_neighbor","shared_zone":"İkisi de gebeliğin son evreleri ve doğum çevresindedir."},{"boundary_match":"partial","distinction":"Odak dal doğumu esas alır; komşu dal tamamlanmamış gebelikten düşme sınırına sahiptir.","focus_only":"Odak dal normal doğurma anlamını taşır.","gloss":"doğum ile düşük","neighbor_only":"Komşu dal tamamlanmadan düşen çocuk veya düşük olayına bağlıdır.","neighbor_ref":"root_000719/B004","relation_type":"near_neighbor","shared_zone":"İkisi de rahimdeki çocuğun anneden ayrılması alanındadır."}],"source_summary":"Ortak kanıt, kadın öznesiyle doğum yapma ve gebelik yükünü bırakma anlamını verir. Aynı toplu kanıt, gebeliğin belirli bir adet döngüsü sınırında başlamasıyla ilgili daha dar bir ad kullanımını da korur."},"support_links":[]},{"boundary":"Kapsam hayvan yürüyüşü ve onu hızlandırma ile sınırlıdır; genel acelecilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"hayvanın hızlı ya da özel yürüyüşle ilerlemesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvan veya binek yol içinde belirli bir yürüyüşle ilerler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıtın bir kısmı yürüyüşü hızlı koşu, bir kısmı daha kolay ve alçak bir gidiş olarak sınırlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Binici hayvanı bu yürüyüşe veya hıza zorlayabilir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan yürüyüşü, hızlandırma ve kaynaklarda görülen kolay gidiş sınırı için uygundur.","boundary_detail":"Kapsam hayvan yürüyüşü ve onu hızlandırma ile sınırlıdır; genel acelecilik değildir.","concept_gloss":"hayvanın hızlı ya da özel yürüyüşle ilerlemesi","contextual_glosses":[{"applicability":"Binek veya hayvanın hızlı yürüdüğü ya da koştuğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yol içinde hızlanmasını korur."},"facet_ids":["F001","F002"],"text":"hızla gitmek","usage_role":"contextual"},{"applicability":"Sürücü veya binici hayvanı bu gidişe sevk ettiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcıyı ve hızlandırma işini korur."},"facet_ids":["F003"],"text":"bineği hızlandırmak","usage_role":"contextual"}],"definition":"Binek ya da hayvanın yolda özel bir yürüyüşle hızlı veya rahat biçimde ilerlemesi; binici de onu bu gidişe sevk edebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvan veya binek yol içinde belirli bir yürüyüşle ilerler."},{"facet_id":"F002","role":"source_variant","statement":"Kanıtın bir kısmı yürüyüşü hızlı koşu, bir kısmı daha kolay ve alçak bir gidiş olarak sınırlar."},{"facet_id":"F003","role":"specialization","statement":"Binici hayvanı bu yürüyüşe veya hıza zorlayabilir."}],"identity_rationale":"Kaynak ifadesi hayvanın yolda hızlı gitmesini ve binicinin onu hızlandırmasını güçlü biçimde destekler; ancak bazı kanıtlar bunu sadece koşu değil, daha alçak veya kolay bir yürüyüş türü olarak da verir. Bu nedenle dal hız anlamıyla kullanılabilir, fakat her bağlamda en şiddetli koşu gibi okunmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bineğin hızlı gitmesi veya koşması"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sürücünün bineği hızlandırması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bu yürüyüşü güzel olan"}],"lexicalization_note":"mixed_non_bare olduğu için hayvanın kendi yürüyüşü, binicinin hızlandırması ve kalıp halindeki yürüyüş niteliği ayrı tutulur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar hız, koşu derecesi ve binek duruşu arasındaki başlıca sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hız bağlamında çok yakındırlar; odak dalın kaynak aralığı sadece yüksek hız değil, özel yürüyüş biçimini de içerir.","focus_only":"Odak dalda bazı kanıtlar daha kolay veya alçak yürüyüşü de korur.","gloss":"bineğin hızla gitmesi","neighbor_only":"Komşu dal bineklerde hızlı gidiş ve bu hıza sevk etmeyi daha genel biçimde kapsar.","neighbor_ref":"root_001628/B001","relation_type":"near_synonym","shared_zone":"İkisi de binek veya hayvanın yol içinde hızlanması alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal yürüyüş türü ve hızlandırma çevresindedir; komşu dal çok sert koşu derecesini adlandırır.","focus_only":"Odak dal hızla birlikte kolay veya düşük yürüyüş varyantını da taşıyabilir.","gloss":"özel gidiş ile sert koşu","neighbor_only":"Komşu dal devenin en şiddetli koşusu ve ayak vuruşu üzerine kuruludur.","neighbor_ref":"root_000536/B012","relation_type":"same_field","shared_zone":"Her ikisi de deve veya binek koşusu alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal yol içi gidişi anlatır; komşu dal binicinin üzerine çıkmasını sağlayan duruşu anlatır.","focus_only":"Odak dal hayvanın yolda ilerleyişidir.","gloss":"yürüme ile binmeye hazırlanma","neighbor_only":"Komşu dal hayvanın binilsin diye boynunu alçaltmasıdır.","neighbor_ref":"root_001657/B013","relation_type":"same_field","shared_zone":"İkisi de binek hayvanın hareket veya duruşuna bağlıdır."}],"source_summary":"Ortak kanıt, dalı hayvanın yolda belirli bir gidişle ilerlemesi ve kişinin onu bu gidişe sevk etmesi etrafında toplar. Toplu anlatımda hız, koşu ve daha kolay bir yürüyüş niteliği birlikte bulunduğundan tanım bu aralığı açık tutar."},"support_links":[]},{"boundary":"Dal ticaret ve sermaye eksilmesiyle sınırlıdır; sosyal düşüklük veya fiziksel koyma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"ticarette zarar ve sermaye indirimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ticaret yapan kişi zarar eder veya sermayesi beklenen tutarın altına düşer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eksilen veya indirilen pay sermayeden düşülen tutar olarak adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinden fiyat veya alacakta indirim isteme kullanımı aynı eksiltme alanına bağlıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ticari zarar, sermayeden düşme ve indirim isteme alanlarını kapsar.","boundary_detail":"Dal ticaret ve sermaye eksilmesiyle sınırlıdır; sosyal düşüklük veya fiziksel koyma değildir.","concept_gloss":"ticarette zarar ve sermaye indirimi","contextual_glosses":[{"applicability":"Kişinin ticaretinde kardan değil kayıptan söz edildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ticari kayıp sonucunu korur."},"facet_ids":["F001"],"text":"zarar etmek","usage_role":"contextual"},{"applicability":"Kayıp veya indirim tutarının sermaye üzerinden adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sermayeden eksilen tutarı korur."},"facet_ids":["F002"],"text":"sermayeden düşülen pay","usage_role":"explanatory"}],"definition":"Ticarette zarar etme ya da sermaye tutarından bir kısmın düşmesi; kişi karda değil eksilmede kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ticaret yapan kişi zarar eder veya sermayesi beklenen tutarın altına düşer."},{"facet_id":"F002","role":"specialization","statement":"Eksilen veya indirilen pay sermayeden düşülen tutar olarak adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Birinden fiyat veya alacakta indirim isteme kullanımı aynı eksiltme alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi ticarette zarar etmeyi ve sermayeden düşülen kısmı aynı ekonomik düşüş alanında açıkça birleştirir. Provisional çerçeve sermaye kaybı, indirim ve zarar sınırlarını doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ticarette zarar etmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sermayeden düşülen indirim veya eksilti"}],"lexicalization_note":"mixed_non_bare olduğu için ticarette zarar etme kalıbı ile sermayeden düşülen pay adı ayrı ama aynı ekonomik alanda tutulur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlanan ayrımlar ticari zarar, genel eksilme ve kar karşıtlığı sınırlarını kapsar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sınırları örtüşür; ikisi de ticari zarar ve sermaye eksiltisi alanında aynı çekirdeği verir.","focus_only":null,"gloss":"ticarette zarar","neighbor_only":null,"neighbor_ref":"root_000409/B002","relation_type":"synonym","shared_zone":"İkisi de ticarette sermaye veya satış sonucunda kardan değil kayıptan söz eder."},{"boundary_match":"partial","distinction":"Odak dal ticari zarar koşulunu ister; komşu dal bu koşul olmadan genel azalmayı anlatır.","focus_only":"Odak dal eksilmeyi özellikle ticaret ve sermaye bağlamına bağlar.","gloss":"sermaye kaybı ile genel eksilme","neighbor_only":"Komşu dal her tür azalmanın ve eksilmenin genel alanını kapsar.","neighbor_ref":"root_001542/B001","relation_type":"near_synonym","shared_zone":"İkisi de bir miktarın azalması anlamını paylaşır."},{"boundary_match":"opposed","distinction":"Odak dal negatif ekonomik sonuçtur; komşu dal pozitif artış veya kazanç yönünü taşır.","focus_only":"Odak dal ticarette kayıp ve sermaye düşmesini anlatır.","gloss":"zarar ile kar","neighbor_only":"Komşu dal alışverişte artış, ürün veya kar elde etme yönündedir.","neighbor_ref":"root_000533/B001","relation_type":"antonym","shared_zone":"İkisi de ticari sonuç ve sermaye hareketi alanındadır."}],"source_summary":"Ortak kanıt, dalı ticarette zarar etmek ve sermayeden düşülen eksilti olarak verir. Aynı toplu malzeme bu eksiltinin talep edilen indirim biçimine de uzandığını gösterir."},"support_links":[]},{"boundary":"Dal toplumsal ya da davranışsal alçalma alanındadır; para kaybı veya fiziksel yerleştirme değildir.","branch_kind":"bare","branch_ref":"root_001657/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"düşük konum ve kendini alçaltma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi toplumsal konum veya soy bakımından düşük ve itibarsız görülür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıt, bu düşüklüğü yüksek veya soylu olmanın karşıtı olarak belirler."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kendini alçaltarak boyun eğme tavrı aynı anlam alanına bağlıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplumsal düşük sayılma ile davranışsal boyun eğme alanlarını birlikte kapsar.","boundary_detail":"Dal toplumsal ya da davranışsal alçalma alanındadır; para kaybı veya fiziksel yerleştirme değildir.","concept_gloss":"düşük konum ve kendini alçaltma","contextual_glosses":[{"applicability":"Kişinin soy, onur veya toplumdaki yeri bakımından aşağı sayıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplumsal düşük konum anlamını korur."},"facet_ids":["F001","F002"],"text":"düşük konumlu","usage_role":"contextual"},{"applicability":"Kişinin tavır olarak kendini aşağı çektiği veya boyun eğdiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Davranışsal alçalmayı ve boyun eğmeyi korur."},"facet_ids":["F003"],"text":"kendini alçaltarak boyun eğmek","usage_role":"explanatory"}],"definition":"Kişinin soy, konum veya davranış bakımından aşağı ve itibarsız sayılması; ayrıca kendini alçaltarak boyun eğme tavrını içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi toplumsal konum veya soy bakımından düşük ve itibarsız görülür."},{"facet_id":"F002","role":"source_variant","statement":"Kanıt, bu düşüklüğü yüksek veya soylu olmanın karşıtı olarak belirler."},{"facet_id":"F003","role":"extension","statement":"Kendini alçaltarak boyun eğme tavrı aynı anlam alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi kişiyi soyluluk veya yüksek konumun karşıtı olarak düşük ve itibarsız sayar; ayrıca kişinin kendini alçaltarak boyun eğmesini aynı düşüklük alanına bağlar. Provisional çerçeve sosyal konum ve alçalma ayrımını doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"düşük konumlu kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aşağı konum, düşüklük"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini alçaltarak boyun eğme"}],"lexicalization_note":"bare olduğu için tanım yalın sosyal düşüklük ve kendini alçaltma alanında kalır; kalıp bağlı anlam içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar sosyal düşüklük, boyun eğme ve kibir karşıtlığındaki başlıca karışma alanlarını kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha çok kişinin konum veya soydaki düşüklüğünü adlandırır; komşu dal aşağı düşürme sürecini daha geniş tutar.","focus_only":"Odak dal kişinin düşük ve itibarsız sayılmasına ad olur.","gloss":"düşük konum","neighbor_only":"Komşu dal yüksek bir halden düşürülme, mal veya iyi durum kaybı gibi daha geniş bir alçalışı kapsar.","neighbor_ref":"root_001575/B002","relation_type":"near_synonym","shared_zone":"İkisi de insanın yüksek durumdan aşağı görülmesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal kişinin değer veya statüsündeki düşüklüğü korur; komşu dal daha çok huşu ve bedensel uysallıktır.","focus_only":"Odak dal sosyal itibarsızlık ve düşük konumu içerir.","gloss":"düşüklük ile boyun eğme","neighbor_only":"Komşu dal baş eğme, ses kısma ve organların sükuneti gibi boyun eğen beden tavrını öne çıkarır.","neighbor_ref":"root_000412/B001","relation_type":"near_neighbor","shared_zone":"İkisi de kendini aşağı çekme ve alçak durma alanına yaklaşır."},{"boundary_match":"opposed","distinction":"Odak dal aşağılık veya alçak duruşu anlatır; komşu dal üstünlük gösteren yükselişi anlatır.","focus_only":"Odak dal aşağı görülme ve kendini alçaltma yönündedir.","gloss":"alçalma ile kibirlenme","neighbor_only":"Komşu dal burnunu veya başını kaldırarak kibirlenme yönündedir.","neighbor_ref":"root_000817/B002","relation_type":"antonym","shared_zone":"İkisi de kişinin kendini toplum içinde nasıl konumladığıyla ilgilidir."}],"source_summary":"Ortak kanıt, dalı kişide düşük konum, soyluluk karşıtı olma ve itibarsızlık olarak toplar. Aynı kanıt kendini alçaltma ve boyun eğme tavrını da bu düşüklük alanına bağlar."},"support_links":[]},{"boundary":"Dal, yerleştirilmiş topluluklar, kayıtlı askerler ve yüklerdir; ticari indirim anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001657/B006","candidate_links":[{"candidate_id":"cand_1bfb14a66d613e571bc2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"yerleştirilmiş topluluk, kayıtlı asker ya da yük","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk eski yerinden alınıp başka bir yerde oturtulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Askerlerden oluşan bir grup belirli bir bölgenin kaydına bağlanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad alanında topluluğun taşıdığı ağır eşyalar da anılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer değiştirmiş topluluk, bölge kaydına bağlı asker ve topluluk yükü kullanımlarını kapsar.","boundary_detail":"Dal, yerleştirilmiş topluluklar, kayıtlı askerler ve yüklerdir; ticari indirim anlamı dışarıda kalır.","concept_gloss":"yerleştirilmiş topluluk, kayıtlı asker ya da yük","contextual_glosses":[{"applicability":"Bir halk veya grup yerinden alınıp başka bir yerde oturtulduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun yer değiştirilip oturtulmasını korur."},"facet_ids":["F001"],"text":"başka yere yerleştirilen topluluk","usage_role":"contextual"},{"applicability":"Asker adlarının belirli bir bölge kaydına yazıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Asker grubunu ve bölge kaydına bağlanmayı korur."},"facet_ids":["F002"],"text":"bölgeye kaydedilmiş askerler","usage_role":"contextual"},{"applicability":"Adın bir topluluğa ait ağır eşya veya yükler için kullanıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşınan yük anlamını korur."},"facet_ids":["F003"],"text":"topluluğun yükleri","usage_role":"contextual"}],"definition":"Yerinden alınıp başka yere yerleştirilen toplulukları, bir bölge kaydına bağlanan askerleri ve topluluğun taşınan yüklerini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk eski yerinden alınıp başka bir yerde oturtulur."},{"facet_id":"F002","role":"specialization","statement":"Askerlerden oluşan bir grup belirli bir bölgenin kaydına bağlanabilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad alanında topluluğun taşıdığı ağır eşyalar da anılır."}],"identity_rationale":"Kaynak ifadesi başka yere taşınıp yerleştirilen toplulukları, bir bölge kaydına bağlanan askerleri ve topluluğun yüklerini birlikte verir. Bunlar tek bir basit nesne koyma anlamı değildir; ancak yerleştirilmiş veya kayıt altına konmuş kişi ve yükler başlığı altında korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"başka bir yere taşınıp yerleştirilen topluluklar"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bölgeye kaydedilen askerler veya topluluğun yükleri"}],"lexicalization_note":"bare olduğu için tanım bu ad grubunun kendi sınırında kalır; ticaret veya genel koyma kalıplarından anlam taşımaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar yerinden edilme, grup adı ve yük anlamı çevresindeki en yararlı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sonuçtaki yerleşmiş grubu adlandırır; komşu dal ayrılma ve sürülme hareketini adlandırır.","focus_only":"Odak dal başka yerde oturtulan topluluk adını verir.","gloss":"yerleştirilen topluluk ile yurttan çıkarma","neighbor_only":"Komşu dal yurtlardan çıkma veya çıkarılma eylemini anlatır.","neighbor_ref":"root_000256/B004","relation_type":"near_neighbor","shared_zone":"İkisi de bir grubun yurdundan ayrılması veya ayrılmaya zorlanması alanındadır."},{"boundary_match":"field_only","distinction":"Odak dalın belirleyici yönü yerleştirilme veya kayıt bağlamıdır; komşuda belirleyici yön karışık ve bölük bölük topluluktur.","focus_only":"Odak dal yer değiştirilmiş veya kayda geçirilmiş gruba bağlıdır.","gloss":"yerleştirilmiş grup ile karışık grup","neighbor_only":"Komşu dal farklı kabilelerden veya kesimlerden oluşan karışık toplulukları anlatır.","neighbor_ref":"root_001667/B002","relation_type":"same_field","shared_zone":"İkisi de insan gruplarını adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda yük anlamı aynı ad grubunun özel bir kullanımıdır; komşu dal yük kavramını çekirdek anlam yapar.","focus_only":"Odak dal yük anlamını topluluk adının bir varyantı olarak taşır.","gloss":"topluluk yükü ile genel yük","neighbor_only":"Komşu dal yük, ağırlık ve taşınan şeyler alanını genel olarak kapsar.","neighbor_ref":"root_000644/B001","relation_type":"near_neighbor","shared_zone":"İkisi de taşınan ağır eşya veya yük kavramına dokunur."}],"source_summary":"Toplu kanıt, dalı başka yere taşınıp yerleştirilen topluluklar ve kayıt altına alınan askerler etrafında kurar. Aynı toplu kanıt, adın topluluğa ait yükler için de kullanıldığını bildirir."},"support_links":["sup_2d48a4347de983e702c4"]},{"boundary":"Dal deve otlaması ve belirli otlak bitkisiyle sınırlıdır; hızlı yürüyüş anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001657/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"devenin tuzcul otu otlaması ve orada konaklaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develer belirli otlak bitkisini yer veya onun üzerinde kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, develerin üzerinde kaldığı bitki veya otlak alanına da aktarılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve sürüsü, belirli otlak bitkisi ve bu bitki alanında kalma bağlamlarında uygundur.","boundary_detail":"Dal deve otlaması ve belirli otlak bitkisiyle sınırlıdır; hızlı yürüyüş anlamı dışarıda kalır.","concept_gloss":"devenin tuzcul otu otlaması ve orada konaklaması","contextual_glosses":[{"applicability":"Tek bir devenin bu bitkiyle beslenmesi veya yanında kalması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deveyi ve özel otlama nesnesini korur."},"facet_ids":["F001"],"text":"tuzcul otu otlayan deve","usage_role":"contextual"},{"applicability":"Ad bitkinin kendisine veya bu bitkinin bulunduğu otlak alanına geçtiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitki ve otlak alanı anlamını korur."},"facet_ids":["F002"],"text":"tuzcul otlak bitkisi","usage_role":"contextual"}],"definition":"Develerin belirli tuzcul veya sert otlak bitkisini yemesi ya da onun bulunduğu yerde konaklaması; aynı ad bitki veya otlak alanı için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develer belirli otlak bitkisini yer veya onun üzerinde kalır."},{"facet_id":"F002","role":"extension","statement":"Ad, develerin üzerinde kaldığı bitki veya otlak alanına da aktarılır."}],"identity_rationale":"Kaynak ifadesi develerin belirli meralık bitkiyi yemesi veya o bitki alanında konaklaması ile bitkinin kendisine verilen adı birlikte gösterir. Provisional çerçeve otlama, konaklama ve bitki adı ilişkisini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tuzcul otu otlayan veya yanında konaklayan dişi deve"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tuzcul bitkiyi otlayan develer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tuzcul yemlik bitki veya develerin kaldığı otlak"}],"lexicalization_note":"bare olduğu için tanım bu otlama ve bitki alanına bağlı yalın kullanımları verir; başka deve hareketleri içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar genel mera, otlatma eylemi ve alanda kalma anlamlarıyla karışmayı sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve ve belirli bitki türüyle sınırlıdır; komşu dal genel ot ve mera adıdır.","focus_only":"Odak dal develeri ve belirli tuzcul otlak bitkisini ister.","gloss":"özel deve otlağı ile genel mera","neighbor_only":"Komşu dal hayvanların yediği ot ve merayı genel biçimde kapsar.","neighbor_ref":"root_000003/B001","relation_type":"near_neighbor","shared_zone":"İkisi de hayvanların yediği bitki ve otlak alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal hayvanın yediği özel bitki ve konaklama yeridir; komşu dal otlatma izni ve serbest bırakma eylemidir.","focus_only":"Odak dal belirli bitkiyi yeme ve yanında kalma durumunu adlandırır.","gloss":"özel otlama ile meraya salma","neighbor_only":"Komşu dal hayvanı meraya salma ve serbest otlatma eylemini anlatır.","neighbor_ref":"root_000764/B003","relation_type":"same_field","shared_zone":"İkisi de sürü hayvanlarının otlaması alanındadır."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı koşulu özel bitki adıdır; komşuda ayırıcı koşul hayvanın bir yanda kalması veya sürü niteliğidir.","focus_only":"Odak dal özel otlak bitkisi ve deve kullanımını korur.","gloss":"deve otlağı ile yana bağlı otlama","neighbor_only":"Komşu dal belirli bir yana bağlı kalarak otlayan veya çok sayıda olan hayvan grubunu anlatır.","neighbor_ref":"root_000902/B006","relation_type":"near_neighbor","shared_zone":"İkisi de hayvanın belli bir otlama alanında kalmasına ilişir."}],"source_summary":"Ortak kanıt, dalı develerin belirli otlak bitkisini yemesi ve onun bulunduğu yerde kalması olarak verir. Aynı kanıt adın bitkiye veya bu bitkinin bulunduğu yere de geçtiğini gösterir."},"support_links":[]},{"boundary":"Dal terzilikte kumaşa pamuk serme ve ardından dikme işlemidir; genel koyma anlamı değildir.","branch_kind":"bare","branch_ref":"root_001657/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"kumaşa pamuk serip dikme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Pamuk kumaşın üzerine düzgünce serilir veya konur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Pamuk yerleştirildikten sonra giysinin dikilmesi bu teknik işin parçasıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Pamuk yerleştirme ve sonrasındaki giysi dikme işlemini birlikte anlatır.","boundary_detail":"Dal terzilikte kumaşa pamuk serme ve ardından dikme işlemidir; genel koyma anlamı değildir.","concept_gloss":"kumaşa pamuk serip dikme","contextual_glosses":[{"applicability":"Terzinin pamuğu kumaş üzerine yerleştirdiği aşama için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Pamuk yerleştirme aşamasını korur."},"facet_ids":["F001"],"text":"kumaşa pamuk sermek","usage_role":"contextual"},{"applicability":"Giysinin pamuk yerleştirmesinden sonra dikildiği teknik bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süreç sırasını ve dikme aşamasını korur."},"facet_ids":["F002"],"text":"pamuk serildikten sonra dikmek","usage_role":"explanatory"}],"definition":"Terzinin pamuğu kumaş üzerine sermesi ve bu yerleştirmeden sonra pamuklu giysiyi dikmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Pamuk kumaşın üzerine düzgünce serilir veya konur."},{"facet_id":"F002","role":"specialization","statement":"Pamuk yerleştirildikten sonra giysinin dikilmesi bu teknik işin parçasıdır."}],"identity_rationale":"Kaynak ifadesi terzinin pamuğu kumaş üzerine sermesini ve pamuk konduktan sonra giysiyi dikmesini aynı el işi sürecinde verir. Provisional çerçeve bu teknik kullanımın sınırını doğru gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kumaşa pamuk koyma veya sonra giysiyi dikme"}],"lexicalization_note":"bare olduğu için tanım bu teknik el işi adında kalır; genel yerleştirme veya karşılıklı anlaşma anlamı içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar dikiş, astar ve pamuk hazırlama alanlarıyla en yakın karışmaları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal pamuk serme aşamasına bağlıdır; komşu dal bu özel hazırlık olmadan genel dikiştir.","focus_only":"Odak dal dikmeden önce kumaşa pamuk yerleştirme aşamasını ister.","gloss":"pamuklu dikim ile genel dikiş","neighbor_only":"Komşu dal dikiş, dikilmiş şey ve dikme aracı alanını genel biçimde kapsar.","neighbor_ref":"root_000453/B006","relation_type":"near_neighbor","shared_zone":"İkisi de kumaş işleme ve dikme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal teknik işlemdir; komşu dal giysideki iç katman veya astar sonucudur.","focus_only":"Odak dal pamuğun kumaş üzerine serilmesi ve ardından dikilmesidir.","gloss":"pamuk serme ile astar","neighbor_only":"Komşu dal elbisenin iç yüzü veya astarını adlandırır.","neighbor_ref":"root_000128/B003","relation_type":"near_neighbor","shared_zone":"İkisi de giysinin iç yapısı ve katmanlarıyla ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal lifli malzemeyi kumaşa koyar; komşu dal lifli malzemenin hacmini açar ve dağıtır.","focus_only":"Odak dal pamuğu kumaşa yerleştirir.","gloss":"yerleştirme ile kabartma","neighbor_only":"Komşu dal pamuk veya yünün kabartılıp dağıtılmasını anlatır.","neighbor_ref":"root_001534/B001","relation_type":"same_field","shared_zone":"İkisi de pamuk veya yün gibi lifli malzemeyle çalışır."}],"source_summary":"Ortak kanıt, dalı terzilikte pamuğun kumaşa serilmesi ve bundan sonra pamuklu giysinin dikilmesi olarak toplar. Bu kullanım genel koyma değil, belirli bir el işi sürecidir."},"support_links":[]},{"boundary":"Dal yalnızca kadın ve baş örtüsü kalıbına bağlıdır; genel soyunma veya doğum değildir.","branch_kind":"collocation","branch_ref":"root_001657/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"baş örtüsünü çıkarıp baş örtüsüz kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın baş örtüsünü çıkarır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonuçta kadın baş örtüsüz olarak nitelenir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın öznesi ve baş örtüsü kalıbı bulunduğunda tam uygulanır.","boundary_detail":"Dal yalnızca kadın ve baş örtüsü kalıbına bağlıdır; genel soyunma veya doğum değildir.","concept_gloss":"baş örtüsünü çıkarıp baş örtüsüz kalma","contextual_glosses":[{"applicability":"Kadının baş örtüsünü çıkarmış olmasından doğan durum nitelenirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sonuçtaki örtüsüzlük durumunu korur."},"facet_ids":["F002"],"text":"baş örtüsüz kadın","usage_role":"contextual"},{"applicability":"Eylemin kendisi, yani örtünün çıkarılması öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baş örtüsünün çıkarılmasını korur."},"facet_ids":["F001"],"text":"baş örtüsünü çıkarmak","usage_role":"contextual"}],"definition":"Kadının baş örtüsünü çıkarıp üzerinde baş örtüsü bulunmaması durumunu anlatan kalıp kullanım.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın baş örtüsünü çıkarır."},{"facet_id":"F002","role":"extension","statement":"Sonuçta kadın baş örtüsüz olarak nitelenir."}],"identity_rationale":"Kaynak ifadesi kadın için baş örtüsünü çıkarmayı ve bu yüzden üzerinde baş örtüsü bulunmamasını doğrudan verir. Provisional çerçeve doğum veya genel koyma anlamına kaymadan bu kalıp sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"baş örtüsünü çıkardığı için baş örtüsüz kadın"}],"lexicalization_note":"collocation olduğu için tanım kadın baş örtüsü kalıbına bağlıdır; yalın köke genel çıkarma anlamı verilmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar genel açma, kadın örtüsü ve örtülü-örtüsüz karşıtlığını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal baş örtüsüz kadın sonucunu ister; komşu dal bu sonucu gerektirmeyen genel örtü kaldırmadır.","focus_only":"Odak dal kadın baş örtüsüne bağlı özel kalıptır.","gloss":"baş örtüsünü çıkarma ile genel açma","neighbor_only":"Komşu dal her türlü örtüyü kaldırma, açma ve temizleme kullanımlarını kapsar.","neighbor_ref":"root_000712/B001","relation_type":"near_synonym","shared_zone":"İkisi de örtü veya kapatan şeyin kaldırılması alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal örtünün kaldırıldığı sonucu anlatır; komşu dal örtünün sağladığı saklanma yönündedir.","focus_only":"Odak dal baş örtüsünün çıkarılması ve baş örtüsüz kalmadır.","gloss":"örtüsüz kalma ile örtünme","neighbor_only":"Komşu dal kadının örtünmesini sağlayan şeyle ilgilidir.","neighbor_ref":"root_000848/B012","relation_type":"polarity_pair","shared_zone":"İkisi de kadının örtüsü ve örtülü olma durumu alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal örtünün yokluğuna gider; komşu dal örtünün kendisini ve kapatma işlevini adlandırır.","focus_only":"Odak dal baş örtüsünün çıkarılmasıyla oluşan örtüsüzlüğü anlatır.","gloss":"örtüyü çıkarma ile örtü","neighbor_only":"Komşu dal bedeni veya baş ve göğsü örten dış örtüyü adlandırır.","neighbor_ref":"root_000252/B004","relation_type":"polarity_pair","shared_zone":"İkisi de kadın örtüsü ve bedenin örtülmesi çevresindedir."}],"source_summary":"Ortak kanıt, dalı kadının baş örtüsünü çıkarması ve bu yüzden baş örtüsüz olması olarak verir. Kullanım kalıp bağlıdır ve genel koyma anlamına genişletilmez."},"support_links":[]},{"boundary":"Dal yalnızca bir şeyi başkasına saklatmak üzere bırakma kalıbıdır.","branch_kind":"collocation","branch_ref":"root_001657/B010","candidate_links":[{"candidate_id":"cand_60cb7a8c462fbfce811f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"saklaması için birine bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahip, bir şeyi saklaması için başka bir kişinin yanına bırakır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bırakılan şey, saklanmak üzere başkasına teslim edilen mal olarak anlaşılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin korunması için başka kişinin yanına bırakıldığı kalıp bağlamlarda uygundur.","boundary_detail":"Dal yalnızca bir şeyi başkasına saklatmak üzere bırakma kalıbıdır.","concept_gloss":"saklaması için birine bırakma","contextual_glosses":[{"applicability":"Bir kişi malını başka birinin yanında korunsun diye bıraktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saklama amacını ve başkasına bırakmayı korur."},"facet_ids":["F001"],"text":"saklatmak üzere bırakmak","usage_role":"contextual"}],"definition":"Bir malı veya şeyi korunup saklanması için başka bir kişinin yanında bırakma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahip, bir şeyi saklaması için başka bir kişinin yanına bırakır."},{"facet_id":"F002","role":"associated_use","statement":"Bırakılan şey, saklanmak üzere başkasına teslim edilen mal olarak anlaşılır."}],"identity_rationale":"Kaynak ifadesi bir şeyi bir kişinin yanında saklatma anlamındaki kalıbı doğrudan verir. Provisional çerçeve ticari indirim veya genel koyma anlamına kaymadan saklanması için bırakma ilişkisini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir şeyi saklaması için birinin yanına bırakmak"}],"lexicalization_note":"collocation olduğu için tanım kişinin yanında saklatma kalıbına bağlı kalır; yalın köke genel bırakma anlamı yüklenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar saklatma, koruma ve güvence olarak tutma arasındaki temel sınırları kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıp bağlıdır; komşu dal aynı ilişkiyi daha geniş ad ve fiil ağıyla taşır.","focus_only":"Odak dal belirli bırakma kalıbıyla sınırlıdır.","gloss":"saklatmak için bırakma","neighbor_only":"Komşu dal saklanmak üzere bırakılan şey, bırakma eylemi, kabul etme ve bırakılan yer gibi alanları daha geniş kapsar.","neighbor_ref":"root_001635/B005","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyi korunması için başkasına bırakma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal saklama için teslim etme anını anlatır; komşu dal koruma işinin kendisini anlatır.","focus_only":"Odak dal bir şeyi başkasına bırakma teslimini içerir.","gloss":"bırakma ile koruma","neighbor_only":"Komşu dal koruma, gözetme ve bekçilik işini genel olarak anlatır.","neighbor_ref":"root_000342/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin güvenle tutulması amacına bağlanır."},{"boundary_match":"partial","distinction":"Odak dal saklama ve geri alma güvenine dayanır; komşu dal borç ilişkisine bağlı güvence işlevidir.","focus_only":"Odak dal korunsun diye bırakılan maldır.","gloss":"saklatılan şey ile güvence","neighbor_only":"Komşu dal borca güvence olarak tutulan şeyi anlatır.","neighbor_ref":"root_000607/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bir malın başka elde tutulmasına ilişir."}],"source_summary":"Ortak kanıt, dalı bir şeyi başkasının yanında saklatmak üzere bırakma kalıbı olarak verir. Bırakılan şey, korunması için o kişiye teslim edilen maldır."},"support_links":["sup_00919c056b1504d612bc"]},{"boundary":"Çekirdek karşılıklı anlaşma ve görüşmedir; işlem türleri buna bağlı özel kullanımlardır.","branch_kind":"bare","branch_ref":"root_001657/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"karşılıklı anlaşma ve görüşme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi veya taraf bir iş üzerinde karşılıklı anlaşır ve onu görüşür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılıklı para koymalı sözleşme aynı ad alanında özel bir işlem kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Satıştan karşılıklı vazgeçme de bu karşılıklı işlem alanına bağlanır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana çekirdeği verir; işlem türleri bağlamda gerektiğinde ayrıca açıklanır.","boundary_detail":"Çekirdek karşılıklı anlaşma ve görüşmedir; işlem türleri buna bağlı özel kullanımlardır.","concept_gloss":"karşılıklı anlaşma ve görüşme","contextual_glosses":[{"applicability":"Tarafların bir işi karşılıklı kabul ettiği ve görüştüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı anlaşma çekirdeğini korur."},"facet_ids":["F001"],"text":"bir konuda anlaşmak","usage_role":"contextual"},{"applicability":"İki tarafın satış işlemini bırakması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satışı karşılıklı bırakma kullanımını korur."},"facet_ids":["F003"],"text":"satıştan karşılıklı vazgeçme","usage_role":"contextual"},{"applicability":"Tarafların sonuç için karşılıklı para veya değer bağladığı işlem kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlem ve değer bağlama anlamını korur."},"facet_ids":["F002"],"text":"karşılıklı para koymalı sözleşme","usage_role":"explanatory"}],"definition":"İki tarafın bir işi karşılıklı olarak ortaya koyup üzerinde anlaşması veya görüşmesi; buna bağlı olarak para koymalı sözleşme ve satıştan karşılıklı vazgeçme gibi işlem kullanımları da bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi veya taraf bir iş üzerinde karşılıklı anlaşır ve onu görüşür."},{"facet_id":"F002","role":"associated_use","statement":"Karşılıklı para koymalı sözleşme aynı ad alanında özel bir işlem kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Satıştan karşılıklı vazgeçme de bu karşılıklı işlem alanına bağlanır."}],"identity_rationale":"Kaynak ifadesi iki tarafın bir iş üzerinde karşılıklı anlaşmasını ve onu görüşmesini ana çekirdek olarak verir. Aynı toplu kanıt bahisleşme ve satıştan karşılıklı vazgeçme gibi işlem kullanımlarını da içerdiğinden tanım yalnızca genel anlaşma diye düzleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir işte karşılıklı anlaşmak ve onu görüşmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"karşılıklı para koymalı sözleşme veya satışı bırakma"}],"lexicalization_note":"bare olduğu için tanım karşılıklı anlaşma adının kendi yalın alanında kalır; fiziksel koyma anlamı içeri alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar anlaşma, razı olma ve karşılıklı bırakma alanlarındaki başlıca sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal karşılıklı görüşme ve işlem bağını korur; komşu dal daha genel uyum ve denkliği anlatır.","focus_only":"Odak dal iki tarafın bir işi görüşmesini ve bazı işlem uzantılarını içerir.","gloss":"karşılıklı anlaşma ile uygunluk","neighbor_only":"Komşu dal uygunluk, denk düşme ve söz birliği alanını daha genel biçimde kapsar.","neighbor_ref":"root_000927/B003","relation_type":"near_synonym","shared_zone":"İkisi de uyuşma ve anlaşma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal işin konuşulup karara bağlanmasını öne çıkarır; komşu dal iç kabul ve hoşnutluk yönünü öne çıkarır.","focus_only":"Odak dal görüşme, karşılıklı sözleşme ve satıştan vazgeçme kullanımlarını içerir.","gloss":"anlaşma ile karşılıklı razı olma","neighbor_only":"Komşu dal tarafların birbirinden hoşnut olup razı olması yönündedir.","neighbor_ref":"root_000569/B003","relation_type":"near_neighbor","shared_zone":"İkisi de iki taraflı kabul alanındadır."},{"boundary_match":"partial","distinction":"Satıştan vazgeçme bağlamında yaklaşırlar; odak dalın ana çekirdeği daha geniş karşılıklı görüşme ve anlaşmadır.","focus_only":"Odak dal satıştan vazgeçmenin yanında genel görüşme ve anlaşmayı da taşır.","gloss":"satıştan vazgeçme","neighbor_only":"Komşu dal iki taraf arasında bırakma veya ayrılmayı çekirdek yapar.","neighbor_ref":"root_000180/B005","relation_type":"near_synonym","shared_zone":"İkisi de karşılıklı bırakma kullanımıyla kesişir."}],"source_summary":"Ortak kanıt, dalı bir konuda karşılıklı anlaşma ve görüşme olarak toplar. Aynı toplu kanıt, karşılıklı para koymalı sözleşme ve satıştan vazgeçme gibi işlem uzantılarını da tek branch claim altında verir."},"support_links":[]},{"boundary":"Dal sağlamlık eksikliği, kadınsı sayılan yumuşama ve at kusurunu kapsar; sosyal düşüklükle aynı değildir.","branch_kind":"bare","branch_ref":"root_001657/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"sağlamlık eksikliği ve kusurlu yumuşama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin işi, yapısı veya yaratılışı sağlam ve toparlanmış değildir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Konuşma veya kişide kadın konuşmasına benzetilen yumuşama ve kadınsı sayılan tavır anılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"At için alt bacağın yayılıp üst kısmın ardından gelmesi biçimindeki yürüyüş kusuru örneklenir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sağlam olmaması, kadınsı sayılan yumuşama ve at yürüyüş kusurunu açıklayıcı biçimde kapsar.","boundary_detail":"Dal sağlamlık eksikliği, kadınsı sayılan yumuşama ve at kusurunu kapsar; sosyal düşüklükle aynı değildir.","concept_gloss":"sağlamlık eksikliği ve kusurlu yumuşama","contextual_glosses":[{"applicability":"Kişinin işi, yapısı veya karakteri toparlanmış ve sağlam görülmediğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişideki sağlamlık eksikliğini korur."},"facet_ids":["F001"],"text":"sağlam olmayan kişi","usage_role":"contextual"},{"applicability":"Kaynakların konuşmayı kadın konuşmasına benzeterek nitelediği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmadaki kadınsı sayılan yumuşama bilgisini korur."},"facet_ids":["F002"],"text":"kadınsı sayılan konuşma","usage_role":"contextual"},{"applicability":"Atın bacak hareketindeki kusur özel olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"At öznesini ve yürüyüş kusurunu korur."},"facet_ids":["F003"],"text":"yürüyüş kusurlu at","usage_role":"contextual"}],"definition":"İnsanda işin, yapının veya tavrın sağlam olmaması; konuşma ya da kişide kadınsı sayılan yumuşama ve atta belirli bir yürüyüş kusuru için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin işi, yapısı veya yaratılışı sağlam ve toparlanmış değildir."},{"facet_id":"F002","role":"extension","statement":"Konuşma veya kişide kadın konuşmasına benzetilen yumuşama ve kadınsı sayılan tavır anılır."},{"facet_id":"F003","role":"example","statement":"At için alt bacağın yayılıp üst kısmın ardından gelmesi biçimindeki yürüyüş kusuru örneklenir."}],"identity_rationale":"Kaynak ifadesi sağlam olmayan kişi veya yaratılış, kadın konuşmasına benzetilen yumuşama, kişide kadınsı sayılan tavır ve attaki yürüyüş kusurunu aynı dalda verir. Bu malzeme tek bir düz anlamdan çok sağlamlık eksikliği ve kusurlu yumuşama çevresinde tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işi veya yapısı sağlam olmayan, kadınsı sayılan kişi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kadın konuşmasına benzetilen yumuşama"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"alt bacağını yayarak yürüyen kusurlu at"}],"lexicalization_note":"bare olduğu için tanım bu yalın nitelik alanında kalır; sosyal düşüklük veya ticari eksilme buraya alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar kişisel sağlamlık, bedensel gevşeklik ve genel bozulma alanlarındaki en yakın sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapısal sağlamlık ve belirli at kusurunu da kapsar; komşu dal akıl ve tavır gevşekliği çevresindedir.","focus_only":"Odak dal sağlam olmayan kişi, kadınsı sayılan tavır ve at kusurunu birlikte taşır.","gloss":"sağlamlık eksikliği ile gevşeklik","neighbor_only":"Komşu dal akıl eksikliği, görüşte gevşeklik ve hafiflik alanına daha çok yönelir.","neighbor_ref":"root_001173/B006","relation_type":"near_neighbor","shared_zone":"İkisi de kişide toparlanmışlık eksikliği ve yumuşaklık alanına yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal sosyal veya tavırsal nitelemeye de açılır; komşu dal daha çok organ ve eklem gevşekliğidir.","focus_only":"Odak dal insan niteliği ve at yürüyüş kusurunu aynı ad altında tutar.","gloss":"sağlam olmayan yapı ile gevşek eklem","neighbor_only":"Komşu dal eklemlerin gevşemesi ve bedenin parçalanmış gibi olması alanındadır.","neighbor_ref":"root_000432/B008","relation_type":"near_neighbor","shared_zone":"İkisi de bedensel veya yapısal gevşeklik alanındadır."},{"boundary_match":"partial","distinction":"Odak dal kişisel yapı ve belirli kusurlara bağlıdır; komşu dal işin veya düzenin bozulmasına bağlıdır.","focus_only":"Odak dal kişide sağlamlık eksikliği ve konuşma yumuşamasını anlatır.","gloss":"sağlamlık eksikliği ile bozulma","neighbor_only":"Komşu dal iş, savaş veya görüşte bozulma ve zayıflamayı anlatır.","neighbor_ref":"root_000435/B010","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin güçlü ve düzgün olmamasını paylaşır."}],"source_summary":"Toplu kanıt, dalı insanda sağlamlık ve toparlanmışlık eksikliği çevresinde verir. Aynı kanıt konuşma ve kişide kadınsı sayılan yumuşama ile atta belirli bir yürüyüş kusurunu da bu gevşeklik alanına bağlar."},"support_links":[]},{"boundary":"Dal binme amacıyla deve başı veya boynunun alçaltılmasıdır; yol hızı değildir.","branch_kind":"bare","branch_ref":"root_001657/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"binmek için devenin boynunu alçaltma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin başı veya boynu aşağı indirilir ya da deve bunu yapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alçaltmanın amacı binicinin ayağını boyna koyarak deveye binmesidir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve ayaktayken binicinin ayağını boyna koyup binmesi için yapılan alçaltma bağlamında uygundur.","boundary_detail":"Dal binme amacıyla deve başı veya boynunun alçaltılmasıdır; yol hızı değildir.","concept_gloss":"binmek için devenin boynunu alçaltma","contextual_glosses":[{"applicability":"Binmek için hayvanın boynu veya başı aşağı alındığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyun veya baş indirme eylemini korur."},"facet_ids":["F001"],"text":"devenin boynunu indirmek","usage_role":"contextual"},{"applicability":"Devenin biniciye çıkış kolaylığı sağladığı duruş açıklanırken uygundur.","error_profile":{"adds":"Çöker gibi ifadesi diz çökme çağrışımı ekleyebilir; kaynak çekirdeği baş ve boyun alçaltmadır.","collision":null,"fit":"broadening","loses":null,"preserves":"Binme amacını ve aşağı eğilme yönünü korur."},"facet_ids":["F001","F002"],"text":"binmek için çöker gibi eğilmek","usage_role":"explanatory"}],"definition":"Devenin ayaktayken başını veya boynunu alçaltması ya da alçalttırılması; binici ayağını boyna koyup binebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin başı veya boynu aşağı indirilir ya da deve bunu yapar."},{"facet_id":"F002","role":"specialization","statement":"Alçaltmanın amacı binicinin ayağını boyna koyarak deveye binmesidir."}],"identity_rationale":"Kaynak ifadesi devenin ayaktayken başını veya boynunu alçaltmasını, binicinin ayağını boyna koyup binebilmesi amacıyla açıkça verir. Provisional çerçeve bu amaçlı hayvan duruşunu doğru temsil eder ve hızlı yürüme anlamına kaymaz.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"binmek için devenin boynunu veya başını alçaltması"}],"lexicalization_note":"bare olduğu için tanım bu deve duruşunun yalın kullanımında kalır; genel koyma veya hızlı yürüyüş anlamı alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar aynı deve duruşu, yorgunluk duruşu ve karşıt baş yönüyle en önemli ayrımları verir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sınırları örtüşür; iki dal da aynı amaçlı deve duruşunu verir.","focus_only":null,"gloss":"binmek için deve başını alçaltma","neighbor_only":null,"neighbor_ref":"root_000426/B005","relation_type":"synonym","shared_zone":"İkisi de devenin başını veya boynunu binici binsin diye aşağı almasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal yardımcı ve amaçlı bir binme duruşudur; komşu dal yorgunluk belirtisidir.","focus_only":"Odak dal alçaltmayı binme amacıyla yapar.","gloss":"binme için alçaltma ile yorgun boyun uzatma","neighbor_only":"Komşu dal devenin yorgunluktan boynunu uzatması ve ses çıkarmasıdır.","neighbor_ref":"root_000814/B007","relation_type":"near_neighbor","shared_zone":"İkisi de devenin boyun duruşuna bağlıdır."},{"boundary_match":"opposed","distinction":"Odak dal aşağı yönlü ve binmeye yardımcıdır; komşu dal yukarı yönlü bir baş hareketidir.","focus_only":"Odak dal binmek için baş veya boynu aşağı alır.","gloss":"baş indirme ile baş kaldırma","neighbor_only":"Komşu dal yüklenirken başın yukarı kaldırılmasını anlatır.","neighbor_ref":"root_001000/B009","relation_type":"polarity_pair","shared_zone":"İkisi de yüklenme veya binme çevresinde hayvan başının yönüyle ilgilidir."}],"source_summary":"Ortak kanıt, dalı devenin başını veya boynunu binme amacıyla alçaltması olarak verir. Eylem, hayvanın yol içi hızı değil, biniciye çıkış kolaylığı sağlayan duruştur."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_46290cd58ae0b583d8c6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:14:1:connective-range-narrowed","source_type":"word_analysis","support_ids":["sup_1a6fb55c9a823a5cb6e8","sup_589ec0f9241cba666d60"],"title":"broad connective values resolved locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:1","qac_refs":["88:14:1:1"],"status":"accepted"}},{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_6abd599ce34f23d29b9d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:14:1:inventory-continuation","source_type":"word_analysis","support_ids":["sup_1a6fb55c9a823a5cb6e8","sup_1f454ce89c538ccaf6c1"],"title":"connector continues the garden inventory","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:1","qac_refs":["88:14:1:1"],"status":"accepted"}},{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_8f30906824a9d3d3e743","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:14:1:locative-ellipsis","source_type":"word_analysis","support_ids":["sup_1a6fb55c9a823a5cb6e8","sup_6c7a1d49ac377c0a5845"],"title":"connector carries omitted locative frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:1","qac_refs":["88:14:1:1"],"status":"accepted"}},{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_3efe0aefd54071d555f5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:14:1:repeated-list-rhythm","source_type":"word_analysis","support_ids":["sup_1a6fb55c9a823a5cb6e8","sup_99ba2a9070b613cce1c8"],"title":"repeated connector builds list rhythm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:1","qac_refs":["88:14:1:1"],"status":"accepted"}},{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_1029ed4c980e8ca2935d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:14:1:tight-surface-join","source_type":"word_analysis","support_ids":["sup_057bcfd8d00c8d9a46d7","sup_1a6fb55c9a823a5cb6e8"],"title":"clitic join makes coordination audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:1","qac_refs":["88:14:1:1"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_96adcbcf7762d2d05915","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:catalogue-service-transition","source_type":"word_analysis","support_ids":["sup_039ef4a4c3bc12ad65a8","sup_12c9f86d10a0e767ba4e"],"title":"catalogue shifts from repose to service","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_ef8528f1e0d85a6bb7ab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:concrete-service-vessel","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_3a2249ae3ba4ae6efd52"],"title":"cup branch selected as service equipment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_d8f0adda3d2f60c8c29b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:contained-cadence","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_c025d362d4a0d347a37f"],"title":"sound supports contained vessel image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_e9e8987347c863d38a6d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:coordinated-plural-head","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_5be5675d213bf692c913"],"title":"plural cup noun as inventory head","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_7c010f981f25bb917b18","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:indefinite-availability","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_9b75f81b9d8d0c9b0c33"],"title":"indefinite vessels as available class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_b344f8805c2d25362795","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:placed-readiness-pair","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_9793f51cc9c1f6804bab"],"title":"cups named to be shown placed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_fddc0c6186881351da9c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:2:service-scene-contrasts","source_type":"word_analysis","support_ids":["sup_12c9f86d10a0e767ba4e","sup_8d60a85f397313a33222"],"title":"settled cups versus circulated service","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:2","qac_refs":["88:14:1:2"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_f22301000fc12d0ac0c2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:completed-passive-state","source_type":"word_analysis","support_ids":["sup_74e08d826c681b87d72e","sup_bd81df3348f88eaf38bd"],"title":"passive participle freezes placement as result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_a180d852fcbcafa3677d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:dependent-collective-adjective","source_type":"word_analysis","support_ids":["sup_bd81df3348f88eaf38bd","sup_e5530c8dcaf1dfca2b3d"],"title":"collective adjective binds the cups","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_8a57d86fb24d5be37f6f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:participial-chain","source_type":"word_analysis","support_ids":["sup_6ee51ccc1ce3a3646caa","sup_bd81df3348f88eaf38bd"],"title":"placed state joins furnishing chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_67dc128d44de7631c90e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:placement-access-assignment","source_type":"word_analysis","support_ids":["sup_5879fe0fd2961481bf58","sup_bd81df3348f88eaf38bd"],"title":"setting-down becomes accessible service","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_115195167c5b67724416","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:raised-placed-vertical-logic","source_type":"word_analysis","support_ids":["sup_56643802e332af0aa52a","sup_bd81df3348f88eaf38bd"],"title":"raised honor answered by placed service","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_e4588ebd70e08797960f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:root-echoes-narrowed","source_type":"word_analysis","support_ids":["sup_bd81df3348f88eaf38bd","sup_f409b003f247878bb5d7"],"title":"root echoes ordered setting and relieved rest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_b3076b6caedf398e94cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:settled-cadence","source_type":"word_analysis","support_ids":["sup_0a1da1aec04584f4a4b7","sup_bd81df3348f88eaf38bd"],"title":"sound slows into settled state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:3"],"branch_refs":[],"candidate_id":"cand_9696004ba2baed1d5bde","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:3:verbless-tableau","source_type":"word_analysis","support_ids":["sup_1edfbad6db8d08e96c7e","sup_bd81df3348f88eaf38bd"],"title":"verbless inventory becomes still tableau","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:14:3","qac_refs":["88:14:2:1"],"status":"accepted"}},{"anchor_refs":["88:14:1"],"branch_refs":[],"candidate_id":"cand_3fdf512a7ee07d58f980","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001328"],"scope":"focus_ayah","source_local_id":"88:14:1:2","source_type":"qac_morpheme","support_ids":["sup_9f2ced43f21e26fc129f"],"title":"QAC root occurrence: ك و ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:14:2"],"branch_refs":[],"candidate_id":"cand_b6c12670585aab777d4e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001657"],"scope":"focus_ayah","source_local_id":"88:14:2:1","source_type":"qac_morpheme","support_ids":["sup_35dea9d46af8069eb82f"],"title":"QAC root occurrence: و ض ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_001328/B001","root_001657/B001"],"candidate_id":"cand_a8d8da7c689c96398dbe","commentary_obligation":"review","hft_ref":"hft_d19a5a99b5e9941f8348","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-ready-drinking-stations","source_type":"hft","support_ids":["sup_a119917d3222eece4e04"],"title":"baseline-ready-drinking-stations","trust":"legacy_unbound"},{"anchor_refs":["88:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_001328/B004","root_001657/B006"],"candidate_id":"cand_1bfb14a66d613e571bc2","commentary_obligation":"review","hft_ref":"hft_edf84de0dce37ffc0d81","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-configured-service-array","source_type":"hft","support_ids":["sup_2d48a4347de983e702c4"],"title":"baseline-configured-service-array","trust":"legacy_unbound"},{"anchor_refs":["88:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_001328/B005","root_001657/B010"],"candidate_id":"cand_60cb7a8c462fbfce811f","commentary_obligation":"review","hft_ref":"hft_03fa4804d5e05ec804f3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-entrusted-hospitality","source_type":"hft","support_ids":["sup_00919c056b1504d612bc"],"title":"baseline-entrusted-hospitality","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:14:1:1","qac_word_ref":"88:14:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","root_ar":"ك و ب","surface_ar":"أَكْوَابٌ"},{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","root_ar":"و ض ع","surface_ar":"مَّوْضُوعَةٌ"}],"word_analysis_qac_refs":[["88:14:1:1"],["88:14:1:2"],["88:14:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:14:1","88:14:2","88:14:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:14:1:1","qac_word_ref":"88:14:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","root_ar":"ك و ب","surface_ar":"أَكْوَابٌ"},{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","root_ar":"و ض ع","surface_ar":"مَّوْضُوعَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:14:1:1"],["88:14:1:2"],["88:14:2:1"]],"word_analysis_refs":["88:14:1","88:14:2","88:14:3"],"word_rows":[{"analysis_record_ref":"88:14:1","analytic_gloss_range_en":"prefixed connector adding the cups to the ongoing garden inventory while preserving the compressed locative frame","analytic_root_gloss_range_en":null,"qac_refs":["88:14:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:14:2","analytic_gloss_range_en":"indefinite plural cups or drinking vessels, foregrounded as ready service equipment rather than beverage or pouring apparatus","analytic_root_gloss_range_en":"cup-vessel language is the locally selected branch; broader lexical branches include instrument, game-object, attachment, drinking-from-a-cup, and body-shape senses that are not activated by this surface","qac_refs":["88:14:1:2"],"root":{"arabic":"ك و ب","transliteration":"k-w-b"},"surface":{"arabic":"أَكْوَابٌۭ","transliteration":"akwābun"}},{"analysis_record_ref":"88:14:3","analytic_gloss_range_en":"passive participial placed-state adjective: the cups are set, positioned, and ready as a collective service arrangement","analytic_root_gloss_range_en":"setting down, putting in place, locating, assigning, lowering, reducing, depositing, and other branch-specific uses; local grammar selects completed placed-state with access and assignment pressure","qac_refs":["88:14:2:1"],"root":{"arabic":"و ض ع","transliteration":"w-ḍ-ʿ"},"surface":{"arabic":"مَّوْضُوعَةٌۭ","transliteration":"mawḍūʿatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:14"],"branch_refs":["root_001328/B001","root_001657/B001"],"candidate_id":"cand_a8d8da7c689c96398dbe","evidence_scope":"focus_ayah","hft_ref":"hft_d19a5a99b5e9941f8348","item_id":"baseline-ready-drinking-stations","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-ready-drinking-stations","support_id":"sup_a119917d3222eece4e04"},{"anchor_refs":["88:14"],"branch_refs":["root_001328/B004","root_001657/B006"],"candidate_id":"cand_1bfb14a66d613e571bc2","evidence_scope":"focus_ayah","hft_ref":"hft_edf84de0dce37ffc0d81","item_id":"baseline-configured-service-array","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-configured-service-array","support_id":"sup_2d48a4347de983e702c4"},{"anchor_refs":["88:14"],"branch_refs":["root_001328/B005","root_001657/B010"],"candidate_id":"cand_60cb7a8c462fbfce811f","evidence_scope":"focus_ayah","hft_ref":"hft_03fa4804d5e05ec804f3","item_id":"baseline-entrusted-hospitality","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-entrusted-hospitality","support_id":"sup_00919c056b1504d612bc"}],"diagnostics":[],"lane_counts":{"global":11,"macro":5,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:14","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:14","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"88:14","lane":"micro","linguistic_source_ref":"88:14","surface_ref":"88:14","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:14","target_tokens":[["Konulmuş",["88:14:2"]],["kadehler",["88:14:1"]],["de",["88:14:1"]],["vardır",["88:14:1"]]],"text":"Konulmuş kadehler de vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:catalogue-service-transition","source_type":"word_analysis","support_id":"sup_039ef4a4c3bc12ad65a8","text":"{\"blocking_evidence\":null,\"headline\":\"catalogue shifts from repose to service\",\"reader_payoff\":\"The reader feels the inventory move from where the recipient reclines to what is placed within reach for hosted reception.\",\"reason\":\"After the connector, this is the ayah's first content-bearing noun and it follows the prior raised couches within the same inventory sequence.\",\"representative_source_ids\":[\"QT-85d12732\",\"MT-1165a11c\",\"QB-dd28a435\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1:tight-surface-join","source_type":"word_analysis","support_id":"sup_057bcfd8d00c8d9a46d7","text":"{\"blocking_evidence\":null,\"headline\":\"clitic join makes coordination audible\",\"reader_payoff\":\"The reader hears the connector and object head arrive together, so the new furnishing is joined at the moment it appears.\",\"reason\":\"Although alignment separates the particle as word 1, the surface form is prefixed to the following noun.\",\"representative_source_ids\":[\"QF-503ffd77\",\"QP-6af786e1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:settled-cadence","source_type":"word_analysis","support_id":"sup_0a1da1aec04584f4a4b7","text":"{\"blocking_evidence\":null,\"headline\":\"sound slows into settled state\",\"reader_payoff\":\"The reader can hear the final word's weight and length support the stillness of things set down, while sound remains a secondary cue.\",\"reason\":\"The surface sound and final position can reinforce the settled-state effect, but lexical and grammatical evidence carry the main claim.\",\"representative_source_ids\":[\"QP-238ea998\",\"QP-29424d75\",\"MP-f951ec1e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2","source_type":"word_analysis","support_id":"sup_12c9f86d10a0e767ba4e","text":"{\"gloss_range\":\"indefinite plural cups or drinking vessels, foregrounded as ready service equipment rather than beverage or pouring apparatus\",\"prose\":\"{{ar:أَكْوَابٌۭ}} ({{tr:akwābun}}) is the first content word of the ayah, so this line of the catalogue moves from raised places of repose into drink-service within reach. The noun is an indefinite broken plural: not one assigned cup, and not a named set, but available vessels appearing as part of the garden's furnished abundance. Its local sense is concrete cup or drinking vessel, not the drink itself and not a pouring apparatus; the following {{ar:مَّوْضُوعَةٌۭ}} ({{tr:mawḍūʿatun}}) immediately makes those vessels read as already arranged for use. That makes the rare cup lexeme feel like specialized service equipment: abundance becomes reachable as multiple receiving vessels set out at the point of use. The service field is sharpened by contrast: vessels are circulated in 76:15, and cups stand with pitchers in 56:18, while 88:14 isolates cups and fixes attention on placed readiness. Even the cadence opens into the vessel name and closes before the heavier placed-state adjective, supporting the contained-cup image without making sound carry the proof.\",\"root_display\":\"{{ar:ك و ب}} ({{tr:k-w-b}})\",\"root_gloss_range\":\"cup-vessel language is the locally selected branch; broader lexical branches include instrument, game-object, attachment, drinking-from-a-cup, and body-shape senses that are not activated by this surface\",\"surface_display\":\"{{ar:أَكْوَابٌۭ}} ({{tr:akwābun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1","source_type":"word_analysis","support_id":"sup_1a6fb55c9a823a5cb6e8","text":"{\"gloss_range\":\"prefixed connector adding the cups to the ongoing garden inventory while preserving the compressed locative frame\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the ayah begin as continuation rather than reset: the cups enter the same garden catalogue already moving through the surrounding verses. The connector also lets {{ar:أَكْوَابٌۭ}} ({{tr:akwābun}}) inherit the earlier locative frame, so the Arabic can keep the inventory compressed instead of restating where the objects are. Its local force is addition within a nominal furnishing list, not oath or independent circumstance. Beginning here, the repeated connector projects the list rhythm forward into the following furnishings, while its quick attachment to the noun makes the next object arrive as another placed item in the same ordered scene.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:verbless-tableau","source_type":"word_analysis","support_id":"sup_1edfbad6db8d08e96c7e","text":"{\"blocking_evidence\":null,\"headline\":\"verbless inventory becomes still tableau\",\"reader_payoff\":\"The reader sees a completed scene of readiness rather than a story about someone arranging cups.\",\"reason\":\"The clause has no finite verb, and the final passive participle supplies completed action as an adjectival state.\",\"representative_source_ids\":[\"QT-2b77b4e2\",\"QT-a030f557\",\"QY-8eff6cf2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1:inventory-continuation","source_type":"word_analysis","support_id":"sup_1f454ce89c538ccaf6c1","text":"{\"blocking_evidence\":null,\"headline\":\"connector continues the garden inventory\",\"reader_payoff\":\"The reader receives the cups as another item inside the active garden catalogue, not as a new isolated luxury image.\",\"reason\":\"QAC identifies a prefixed coordinating particle before the cup noun, and attachment evidence treats the following noun as continuing the prior inventory.\",\"representative_source_ids\":[\"QG-91143a0d\",\"QT-c357ef74\",\"MT-a9a42e72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:14:2:1","source_type":"qac_morpheme","support_id":"sup_35dea9d46af8069eb82f","text":"{\"lemma_ar\":\"مَّوْضُوعَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"88:14:2:1\",\"qac_word_ref\":\"88:14:2\",\"root_ar\":\"و ض ع\",\"surface_ar\":\"مَّوْضُوعَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:concrete-service-vessel","source_type":"word_analysis","support_id":"sup_3a2249ae3ba4ae6efd52","text":"{\"blocking_evidence\":null,\"headline\":\"cup branch selected as service equipment\",\"reader_payoff\":\"The reader imagines drink made reachable through concrete receiving vessels, while the word does not name the beverage itself.\",\"reason\":\"V4 supports the cup-vessel branch for the local surface, while other listed branches for the root are not licensed by the local concrete plural noun.\",\"representative_source_ids\":[\"QS-e96e8960\",\"MS-c718d2ae\",\"QF-7990b3e7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:raised-placed-vertical-logic","source_type":"word_analysis","support_id":"sup_56643802e332af0aa52a","text":"{\"blocking_evidence\":null,\"headline\":\"raised honor answered by placed service\",\"reader_payoff\":\"The reader notices a vertical design: couches are raised for honor, while cups are set down for access within one ordered environment.\",\"reason\":\"The CRITICAL rows tie the word to the prior raised-state adjective in 88:13, and the local passive-adjectival form makes the contrast grammatically parallel.\",\"representative_source_ids\":[\"QS-b8e291f6\",\"ME-3e466583\",\"QB-e6c38729\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:placement-access-assignment","source_type":"word_analysis","support_id":"sup_5879fe0fd2961481bf58","text":"{\"blocking_evidence\":null,\"headline\":\"setting-down becomes accessible service\",\"reader_payoff\":\"The reader feels the cups as both physically near and functionally appointed for service, while broader root branches stay locally limited.\",\"reason\":\"V4 supports setting down, putting in place, and assignment-related branches, but local grammar selects a passive object-state of cups positioned for use.\",\"representative_source_ids\":[\"QS-091d3f47\",\"QS-bb6c2a21\",\"MS-a19df4d8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1:connective-range-narrowed","source_type":"word_analysis","support_id":"sup_589ec0f9241cba666d60","text":"{\"blocking_evidence\":null,\"headline\":\"broad connective values resolved locally\",\"reader_payoff\":\"The reader can hear ordinary addition here without importing oath, event-sequencing, or a separate circumstantial aside.\",\"reason\":\"The following nominative concrete noun selects inventory coordination, while broader connective possibilities remain outside this local frame.\",\"representative_source_ids\":[\"QS-9b331c29\",\"QG-eb8c6eb1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:coordinated-plural-head","source_type":"word_analysis","support_id":"sup_5be5675d213bf692c913","text":"{\"blocking_evidence\":null,\"headline\":\"plural cup noun as inventory head\",\"reader_payoff\":\"The reader sees the cups as the grammatical center of this inventory item and as a collective plural set that receives one placed-state modifier.\",\"reason\":\"QAC marks the word as an indefinite broken-plural nominative concrete noun, and attachment evidence links the following passive participle as its adjective.\",\"representative_source_ids\":[\"QG-085e4f3c\",\"QG-3598e6c3\",\"QF-b1bdaafd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1:locative-ellipsis","source_type":"word_analysis","support_id":"sup_6c7a1d49ac377c0a5845","text":"{\"blocking_evidence\":null,\"headline\":\"connector carries omitted locative frame\",\"reader_payoff\":\"The reader notices that the compact phrase still belongs inside the same garden setting even though the locative predicate is not repeated.\",\"reason\":\"Attachment evidence explicitly licenses recovery of the omitted locative predicate for the coordinated cup noun.\",\"representative_source_ids\":[\"QG-cf9a74d3\",\"QB-6770db84\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:participial-chain","source_type":"word_analysis","support_id":"sup_6ee51ccc1ce3a3646caa","text":"{\"blocking_evidence\":null,\"headline\":\"placed state joins furnishing chain\",\"reader_payoff\":\"The reader hears placed cups as one member of a broader chain of completed furnishing states.\",\"reason\":\"The CRITICAL rows connect the placed-state adjective with adjacent passive-participial furnishing descriptions before and after this ayah.\",\"representative_source_ids\":[\"QE-b0e6d6d3\",\"QB-74e32b1b\",\"QB-bcf36e51\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:completed-passive-state","source_type":"word_analysis","support_id":"sup_74e08d826c681b87d72e","text":"{\"blocking_evidence\":null,\"headline\":\"passive participle freezes placement as result\",\"reader_payoff\":\"The reader arrives after the ordering has already been completed, so the scene is readiness rather than action.\",\"reason\":\"The local form is a passive participle adjective, and the contextual profile shows this exact passive-participial deployment as rare and static.\",\"representative_source_ids\":[\"MG-f9efaa10\",\"QF-6e887d61\",\"MF-0f0c6ea1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:service-scene-contrasts","source_type":"word_analysis","support_id":"sup_8d60a85f397313a33222","text":"{\"blocking_evidence\":null,\"headline\":\"settled cups versus circulated service\",\"reader_payoff\":\"The reader notices that 88:14 focuses on cups already at hand, unlike scenes where vessels move or where pitchers share the service frame.\",\"reason\":\"The CRITICAL rows give concrete comparisons: vessels are circulated in 76:15, and 56:18 pairs cups with pitchers, while this ayah names cups with a placed-state adjective.\",\"representative_source_ids\":[\"QI-0aeb4c61\",\"QI-37035dbd\",\"MI-83f2e290\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:placed-readiness-pair","source_type":"word_analysis","support_id":"sup_9793f51cc9c1f6804bab","text":"{\"blocking_evidence\":null,\"headline\":\"cups named to be shown placed\",\"reader_payoff\":\"The reader does not stop at vessels as objects; the word is immediately drawn into an image of arranged readiness.\",\"reason\":\"The following passive participle modifies the cup noun directly, making object and state one local service pair.\",\"representative_source_ids\":[\"QS-7242907b\",\"QE-8243af6e\",\"QH-df3dd72e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:1:repeated-list-rhythm","source_type":"word_analysis","support_id":"sup_99ba2a9070b613cce1c8","text":"{\"blocking_evidence\":null,\"headline\":\"repeated connector builds list rhythm\",\"reader_payoff\":\"The reader feels each furnishing arrive as another bead in the same repeated catalogue rhythm.\",\"reason\":\"The ayah opens with the connector and the surrounding inventory continues by adding coordinated furnishing nouns.\",\"representative_source_ids\":[\"QE-aca85e29\",\"QB-d015668b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:indefinite-availability","source_type":"word_analysis","support_id":"sup_9b75f81b9d8d0c9b0c33","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite vessels as available class\",\"reader_payoff\":\"The reader notices availability and abundance without limiting the scene to one owner, one vessel, or one counted set.\",\"reason\":\"The noun is indefinite, plural, and unpossessed, so the vessels appear as furnishings of the environment rather than property assigned to a named recipient.\",\"representative_source_ids\":[\"QG-9cbbe926\",\"QG-dadec485\",\"MG-05aac955\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:14:1:2","source_type":"qac_morpheme","support_id":"sup_9f2ced43f21e26fc129f","text":"{\"lemma_ar\":\"أَكْوَاب\",\"morph_features\":\"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:14:1:2\",\"qac_word_ref\":\"88:14:1\",\"root_ar\":\"ك و ب\",\"surface_ar\":\"أَكْوَابٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3","source_type":"word_analysis","support_id":"sup_bd81df3348f88eaf38bd","text":"{\"gloss_range\":\"passive participial placed-state adjective: the cups are set, positioned, and ready as a collective service arrangement\",\"prose\":\"{{ar:مَّوْضُوعَةٌۭ}} ({{tr:mawḍūʿatun}}) turns the cups into a finished state: they are not being placed in a narrated action, but are met as already set out. No arranger is named, so the listener encounters prepared order rather than the labor that produced it. As a feminine singular adjective for the nonhuman broken plural {{ar:أَكْوَابٌۭ}} ({{tr:akwābun}}), it treats many vessels as one arranged furnishing. The root's setting-down field makes service feel physically accessible, while assignment pressure lets the cups seem put in their proper places; broader lowering or motion branches are held to that positive local function, not to disgrace or movement. The word also answers the raised couches of 88:13 through the parallel passive-adjectival form: honor is high, service is set near. Its placed-state participates in the surrounding chain of completed furnishing states, so the garden reads as prepared before any inhabitant acts. Wider echoes keep the scale in view: 55:7 uses the root for ordered setting, and 94:2 uses it for laying down a burden, while 88:14 miniaturizes that order into rested hospitality. The weighted onset and lengthened cadence make the ayah settle on stillness, while grammar and root sense remain the basis of the claim.\",\"root_display\":\"{{ar:و ض ع}} ({{tr:w-ḍ-ʿ}})\",\"root_gloss_range\":\"setting down, putting in place, locating, assigning, lowering, reducing, depositing, and other branch-specific uses; local grammar selects completed placed-state with access and assignment pressure\",\"surface_display\":\"{{ar:مَّوْضُوعَةٌۭ}} ({{tr:mawḍūʿatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:2:contained-cadence","source_type":"word_analysis","support_id":"sup_c025d362d4a0d347a37f","text":"{\"blocking_evidence\":null,\"headline\":\"sound supports contained vessel image\",\"reader_payoff\":\"The reader can hear the word's opening and closure support the contained-vessel image, while sound remains secondary to grammar and sense.\",\"reason\":\"The surface sound can reinforce the cup image and the move into the following settled adjective, but it does not independently establish lexical sense.\",\"representative_source_ids\":[\"QP-794f1330\",\"QP-9d410cc6\",\"MP-13cceb4f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:dependent-collective-adjective","source_type":"word_analysis","support_id":"sup_e5530c8dcaf1dfca2b3d","text":"{\"blocking_evidence\":null,\"headline\":\"collective adjective binds the cups\",\"reader_payoff\":\"The reader sees many cups gathered into one arranged furnishing rather than scattered individual objects.\",\"reason\":\"QAC and attachment evidence mark the word as a feminine singular nominative adjective modifying the nonhuman broken-plural cup noun.\",\"representative_source_ids\":[\"QG-ad7fd505\",\"QG-cbe0c59b\",\"MG-2bf881df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:14:3:root-echoes-narrowed","source_type":"word_analysis","support_id":"sup_f409b003f247878bb5d7","text":"{\"blocking_evidence\":null,\"headline\":\"root echoes ordered setting and relieved rest\",\"reader_payoff\":\"The reader can connect the local placement of cups to wider root scenes of ordered setting and burden laid down, without letting those scenes control the local parse.\",\"reason\":\"The concrete references in 55:7 and 94:2 share the root field, while the local passive participle remains a cup-modifying placed-state adjective.\",\"representative_source_ids\":[\"QI-b501fbc9\",\"QI-d35d3fd6\",\"MI-0843eda9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001328/B001","root_001657/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001328","role":"The handleless drinking-vessel image identifies an object meant for direct access and use.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Setting something down in its determined place supplies the completed preparation that makes the cups ready.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]}],"changed_reading":{"after":"Handleless drinking vessels have already been stationed where use can begin without retrieval or further preparation.","before":"Cups are simply present."},"confidence":"strong","focus_anchor":"The plural أَكْوَابٌ and passive participle مَّوْضُوعَةٌ join drinking vessels to a completed act of deliberate placement.","mechanism":"Handleless cups require direct bodily approach, while setting each object in a determined place removes fetching and preparation from the drinker's side. The line depicts readiness for use rather than a still-life inventory.","model_id":"baseline-ready-drinking-stations"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-ready-drinking-stations","source_type":"hft","support_id":"sup_a119917d3222eece4e04","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001328/B004","root_001657/B006"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001328","role":"Attaching one part upon another makes the vessel plurality available as a coordinated configuration.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001657","role":"Loads or persons assigned to a fixed place supply the functional image of each cup occupying a service station.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]}],"changed_reading":{"after":"The cups form a deliberately configured plurality in which placement assigns each vessel a role within an accessible array.","before":"Several cups have been put somewhere."},"confidence":"medium","focus_anchor":"The plural vessel noun is qualified by a placement participle, allowing plurality to be read as a configured arrangement.","mechanism":"The attachment image in ك و ب makes the many units compositional, and the assigned-place image in و ض ع gives each unit a station. Together they support a service array rather than an accidental heap.","model_id":"baseline-configured-service-array"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-configured-service-array","source_type":"hft","support_id":"sup_2d48a4347de983e702c4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001328/B005","root_001657/B010"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001328","role":"Drinking by means of the cup turns the displayed noun toward the act it enables.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B010","mapped_root_id":"root_001657","role":"Depositing something with another recasts completed placement as a transfer of usable provision.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]}],"changed_reading":{"after":"The cups are provision deliberately relinquished into the beneficiary's reach, making hospitality a transfer rather than a display.","before":"The cups belong to the decor of the scene."},"confidence":"exploratory","focus_anchor":"The vessel root can foreground drinking as an act, while the placement root can carry the image of leaving a deposit with another.","mechanism":"The objects are not only prepared but handed over: placement transfers drinking capacity into another's reach or keeping. Hospitality is therefore rendered as relinquished control over a usable provision.","model_id":"baseline-entrusted-hospitality"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-entrusted-hospitality","source_type":"hft","support_id":"sup_00919c056b1504d612bc","trust":"legacy_unbound"}]}
</lane_packet_json>
