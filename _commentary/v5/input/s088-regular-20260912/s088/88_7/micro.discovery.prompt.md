# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:7",
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
{"branch_registry":[{"boundary":"Dal bireyin bedensel açlık durumuyla sınırlıdır; toplu açlık zamanı, aç bırakma eylemi ve aktarmalı kullanımlar bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_000278/B001","candidate_links":[{"candidate_id":"cand_3e86a0948c7a25692d1e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","surface_ar":"جُوعٍ"}],"gloss":"midenin boş kalmasından doğan açlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tokluğun karşıtı olan ve midenin yiyeceksiz kalmasıyla canlıda rahatsızlık ya da ağrı doğuran bedensel durumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durumun tek bir kez yaşanması ayrıca adlandırılabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sürekli aç görünen ya da sık aralıklarla azar azar yiyen kişi için türemiş bir ad kullanılır."}}],"root_ar":"ج و ع","root_id":"root_000278","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel yoksunluğu, mideyle bağlantısını ve tokluğa karşıt durum oluşunu birlikte anlatan dal geneli karşılıktır.","boundary_detail":"Dal bireyin bedensel açlık durumuyla sınırlıdır; toplu açlık zamanı, aç bırakma eylemi ve aktarmalı kullanımlar bu sınıra girmez.","branch_image_ar":"خلو البطن من الطعام","concept_gloss":"midenin boş kalmasından doğan açlık","contextual_glosses":[{"applicability":"Midenin boş kalması bağlamdan zaten anlaşıldığında doğal ve kısa bir karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":"Bağlam dışında güçlü istek gibi aktarmalı anlamlarla karışabilir.","fit":"narrowing","loses":"Midenin yiyeceksiz kalmasıyla doğan rahatsızlık bağını açıkça söylemez.","preserves":"Tokluğa karşıt olan bedensel yiyecek gereksinimini korur."},"facet_ids":["F001"],"text":"açlık","usage_role":"general"},{"applicability":"Açlığın tek bir yaşanışını sayılan bir olay olarak anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açlık durumunun tek seferlik yaşanmasını eksiksiz korur."},"facet_ids":["F002"],"text":"bir kez açlık çekme","usage_role":"contextual"},{"applicability":"Açlığı sürekli görünen ya da sık sık azar azar yiyen kişiyi açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sık aralıklarla azar azar yeme seçeneğini tek başına belirtmez.","preserves":"Kişide sürekli görülen açlık izlenimini korur."},"facet_ids":["F003"],"text":"sürekli aç görünen kimse","usage_role":"explanatory"}],"definition":"Midenin yiyeceksiz kalmasıyla canlıda rahatsızlık ya da ağrı doğuran ve tokluğun karşısında yer alan bedensel durumdur. Bunun tek seferlik yaşanması ile sürekli aç görünen ya da sık aralıklarla azar azar yiyen kişinin adlandırılması çekirdeğe bağlı özel kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tokluğun karşıtı olan ve midenin yiyeceksiz kalmasıyla canlıda rahatsızlık ya da ağrı doğuran bedensel durumdur."},{"facet_id":"F002","role":"specialization","statement":"Bu durumun tek bir kez yaşanması ayrıca adlandırılabilir."},{"facet_id":"F003","role":"associated_use","statement":"Sürekli aç görünen ya da sık aralıklarla azar azar yiyen kişi için türemiş bir ad kullanılır."}],"identity_rationale":"Kaynak ifadesi, tokluğun karşıtı olan açlığı midenin yiyeceksiz kalmasından doğan bedensel rahatsızlıkla açıkça birleştirir. Bir kez yaşanan açlık ve sürekli aç görünen ya da sık sık azar azar yiyen kişi, bu çekirdeğin bağımlı adlandırmalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"açlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"acıkmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"aç kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"aç kadın"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çok aç kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"aç kadın"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"aç kimseler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"açlar"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir kez açlık çekme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sürekli aç görünen ya da sık sık azar azar yiyen kimse"}],"lexicalization_note":"Dalın yalın anlamı tanımlanır; türemiş kişi ve tek sefer adları çekirdeğe bağlı kalır, başka dallardaki söz öbeği anlamları buraya taşınmaz.","neighbor_coverage_note":"Bütün aday komşular gözden geçirildi; sınırı en iyi açıklayan beş karşılaştırma yayımlandı, yalnız benzer sahneyi paylaşan veya doğrudan ayrım sağlamayan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal açlığı bütün bedensel durum olarak kurarken komşu dal karın boşluğu ve içe çekilme görüntüsüne daha sıkı bağlıdır; bu yüzden her bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal tokluğun karşıtı olan genel bedensel durumu, tek seferlik yaşanışı ve kişi adlandırmasını kapsar.","gloss":"açlık ve karın boşluğu","neighbor_only":"Komşu dal karın boşluğunu ve karnın açlıktan içe çekilmesini özellikle öne çıkarır.","neighbor_ref":"root_000440/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yiyeceksiz kalan karınla bağlantılı açlık durumunu anlatır."},{"boundary_match":"partial","distinction":"Açlık, boşluğun canlıda doğurduğu duyum ve durumdur; komşu ise bu duyum bulunsun ya da bulunmasın karnın boş olmasını veya boşaltılmasını anlatabilir.","focus_only":"Odak dal yiyecek yoksunluğunun doğurduğu açlık ve rahatsızlığı merkez alır.","gloss":"açlık ve midenin boşluğu","neighbor_only":"Komşu dal karnın ya da midenin boşaltılmasını, sağaltım amacıyla yapılan boşaltma dahil, merkez alır.","neighbor_ref":"root_001632/B004","relation_type":"near_neighbor","shared_zone":"İki dal da midenin yiyeceksiz kalması durumunda kesişir."},{"boundary_match":"field_only","distinction":"Biri canlıdaki bedensel durumun, diğeri ise yaygın açlığın yaşandığı zamanın adıdır.","focus_only":"Odak dal tek bir canlının bedensel açlık durumudur.","gloss":"bireysel açlık ve açlık dönemi","neighbor_only":"Komşu dal açlığın topluma yayıldığı yılı ya da dönemi bildirir.","neighbor_ref":"root_000278/B002","relation_type":"same_field","shared_zone":"Her ikisinin ortak alanı yiyecek yoksunluğu ve açlıktır."},{"boundary_match":"partial","distinction":"Odak bir durumdur; komşu ise bu duruma neden olan geçişli eylemi veya durumu bilinçli biçimde seçmeyi kodlar.","focus_only":"Odak dal açlığın kendisini ve aç kişinin durumunu anlatır.","gloss":"açlık ve aç bırakma","neighbor_only":"Komşu dal birini aç bırakma eylemini veya kişinin bilerek aç kalmasını anlatır.","neighbor_ref":"root_000278/B003","relation_type":"near_neighbor","shared_zone":"Eylemin sonucu ya da amacı odak daldaki açlık durumudur."},{"boundary_match":"field_only","distinction":"Ortak üst alanlarına karşın biri yiyeceğe, diğeri suya yönelir; aynı duyumu ya da aynı gereksinimi adlandırmazlar.","focus_only":"Odak dal yiyecek yoksunluğundan doğan açlıktır.","gloss":"açlık ve susuzluk","neighbor_only":"Komşu dal su yoksunluğundan doğan yoğun susuzluktur.","neighbor_ref":"root_001380/B002","relation_type":"same_field","shared_zone":"İkisi de bedensel bir gereksinimin karşılanmamasından doğan yoksunluk duyumudur."}],"source_phrase_ar":"الجوع ضد الشبع (maqayis;jamhara;sihah)؛ الجوع اسم جامع للمخمصة (ayn)؛ الجوع اسم للمخمصة (tahdhib)؛ الألم الذي ينال الحيوان من خلو المعدة من الطعام (mufradat)؛ الجوعة المرة من الجوع (jamhara;sihah;tahdhib)؛ المستجيع الذي يأكل كل ساعة الشيء بعد الشيء (tahdhib)","source_summary":"Kaynaklar açlığı tokluğun karşıtı ve yiyeceksiz midenin canlıda doğurduğu bedensel sıkıntı olarak ortaklaştırır; ayrıca tek seferlik açlığı ve açlığı sürekli görünen kişinin adını kaydeder.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الجوع ضد الشبع، والمخمصة، وألم خلو المعدة، وحال الجائع والجوعان والجياع، والمرة الواحدة من الجوع، والمستجيع الذي يظهر عليه دوام الجوع أو تكرار الأكل.","what_is_not_ar":"لا يدخل فيه عام المجاعة بوصفه زمانا، ولا أفعال الإجاعة والتجويع والتجوع، ولا الأسماء الموضعية أو القبلية."},"support_links":["sup_4115f3d79c0e6aca9aa1"]},{"boundary":"Dal yaygın açlığın yaşandığı zamanla sınırlıdır; tek kişinin açlığı ya da yalnız yağışsızlık durumu tek başına bu kimliği karşılamaz.","branch_kind":"bare","branch_ref":"root_000278/B002","candidate_links":[{"candidate_id":"cand_7a78400a7dfe63137f2e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","surface_ar":"جُوعٍ"}],"gloss":"yaygın açlık dönemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Açlığın bir toplulukta yaygın biçimde yaşandığı yıl ya da dönemdir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu dönem, kaynak anlatımında kuraklığın yaşandığı zaman olarak da sınırlandırılır."}}],"root_ar":"ج و ع","root_id":"root_000278","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplum çapındaki açlığı, bunun tek bir kişideki duyum değil bir zaman dilimi oluşunu birlikte koruyan dal geneli karşılıktır.","boundary_detail":"Dal yaygın açlığın yaşandığı zamanla sınırlıdır; tek kişinin açlığı ya da yalnız yağışsızlık durumu tek başına bu kimliği karşılamaz.","branch_image_ar":"زمن يعم فيه الجوع","concept_gloss":"yaygın açlık dönemi","contextual_glosses":[{"applicability":"Söz konusu zaman açıkça tek bir yıl olduğunda kısa ve doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıl boyunca yaygın açlık yaşanması anlamını korur."},"facet_ids":["F001"],"text":"açlık yılı","usage_role":"contextual"},{"applicability":"Kaynak bağlamı dönemin hem kurak hem de yaygın açlıkla belirlenmiş olduğunu vurguladığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kurak zaman ile yaygın açlık zamanı arasındaki açık bağlantıyı korur."},"facet_ids":["F001","F002"],"text":"kuraklık ve açlık dönemi","usage_role":"explanatory"}],"definition":"Bir toplulukta açlığın yaygınlaştığı yıl ya da dönemdir. Kaynakta kuraklık zamanıyla ilişkilendirilen bu zaman anlamı, bireyin açlık duyumundan ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Açlığın bir toplulukta yaygın biçimde yaşandığı yıl ya da dönemdir."},{"facet_id":"F002","role":"source_variant","statement":"Bu dönem, kaynak anlatımında kuraklığın yaşandığı zaman olarak da sınırlandırılır."}],"identity_rationale":"Kaynak ifadesi dalı, yaygın açlığın yaşandığı yıl ya da zaman olarak açıkça kurar ve bunu kurak dönemle ilişkilendirir. Bu, bireyin açlık duyumundan ve birini aç bırakma eyleminden ayrı bir zaman adıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yaygın açlık dönemi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"açlık yılı"}],"lexicalization_note":"Yalın dal, yaygın açlığın yaşandığı yıl veya dönem olarak tanımlanır; bireysel durum ve neden olan eylemler bu kapsama eklenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; zaman, kuraklık, genel güçlük ve bireysel duyum sınırlarını en açık gösteren dört komşu seçildi, geri kalanlar bu ayrımları yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak için belirleyici ölçüt yaygın açlıktır; komşu için yağışsızlık ve toprağın durumu belirleyicidir, bu nedenle sonuçları kesişse de sınırları aynı değildir.","focus_only":"Odak dal yılı yaygın açlığın yaşanmasıyla tanımlar.","gloss":"açlık yılı ve kurak yıl","neighbor_only":"Komşu dal yılı yağışsızlıkla ve kimi anlatımlarda hem bolluk hem kuraklık taşımasıyla tanımlar.","neighbor_ref":"root_000140/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da geçim sıkıntısı doğuran ağır bir yılı anlatabilir."},{"boundary_match":"partial","distinction":"Odak sonuç ve zaman bakımından açlığı adlandırır; komşu ise çevresel koşulu adlandırır ve açlık ortaya çıkmadan da kullanılabilir.","focus_only":"Odak dal yaygın açlığın yaşandığı zaman dilimidir.","gloss":"açlık dönemi ve kuraklık","neighbor_only":"Komşu dal yağmurun kesilmesi, toprağın kuruması ve otlakların azalması durumudur.","neighbor_ref":"root_001402/B001","relation_type":"near_neighbor","shared_zone":"Kuraklık yaygın açlığa yol açabildiği için iki alan sıkça aynı olayda buluşur."},{"boundary_match":"partial","distinction":"Odak yalnız zamanın yaygın açlık niteliğini merkez alır; komşu daha geniş bir güçlük alanını ve açlığın kimi sonuçlarını da kapsar.","focus_only":"Odak dal doğrudan yaygın açlık yaşanan zamanı gösterir.","gloss":"açlık dönemi ve ağır geçim sıkıntısı","neighbor_only":"Komşu dal zamanın sertliğini, yiyecek sıkıntısını ve bunların bedensel ya da hayvansal sonuçlarını birlikte taşır.","neighbor_ref":"root_000252/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da yaygın açlık ve zor zaman alanında kesişir."},{"boundary_match":"field_only","distinction":"Odak zamana ve toplumsal yaygınlığa, komşu ise bireyin bedensel durumuna gönderme yapar.","focus_only":"Odak dal yaygın açlığın yaşandığı yıl ya da dönemdir.","gloss":"açlık dönemi ve bireysel açlık","neighbor_only":"Komşu dal tek bir canlının midesinde duyduğu açlık durumudur.","neighbor_ref":"root_000278/B001","relation_type":"same_field","shared_zone":"Her ikisi de yiyecek yoksunluğu ve açlık alanına bağlıdır."}],"source_phrase_ar":"عام مجاعة ومجوعة (maqayis;sihah)؛ المجاعة عام فيه جوع (ayn;tahdhib)؛ المجاعة عبارة عن زمان الجدب (mufradat)","source_summary":"Kaynaklar, yaygın açlığın yaşandığı yılı veya dönemi ortak anlam olarak verir; bazı anlatımlar zamanın kuraklık niteliğini de öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العام أو الزمان الذي يقع فيه الجوع العام: مجاعة ومجوعة، وزمان الجدب.","what_is_not_ar":"لا يدخل فيه جوع الفرد نفسه ولا فعل جعل غيره جائعا."},"support_links":["sup_a4cff254ebf451c7f80b"]},{"boundary":"Bir başkasını aç bırakma ile bilerek aç kalma birbirine karıştırılmaz; sağaltım için doyuncaya kadar yememe yalnız ikinci yüzün söz öbeğine bağlı özel biçimidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000278/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","surface_ar":"جُوعٍ"}],"gloss":"aç bırakma ya da bilerek aç kalma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının aç duruma gelmesine neden olan geçişli eylemdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bilinçli olarak aç kalmayı seçmesi ve yemeğini kısmasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sağaltım amacıyla doyuncaya kadar yememek, bilinçli aç kalmanın yapıya bağlı özel uygulamasıdır."}}],"root_ar":"ج و ع","root_id":"root_000278","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ayrı eylem yönünü birlikte gösteren üst karşılıktır; tek bir geçişlilik kalıbı varmış izlenimi vermez.","boundary_detail":"Bir başkasını aç bırakma ile bilerek aç kalma birbirine karıştırılmaz; sağaltım için doyuncaya kadar yememe yalnız ikinci yüzün söz öbeğine bağlı özel biçimidir.","branch_image_ar":"إحداث الجوع أو قصده","concept_gloss":"aç bırakma ya da bilerek aç kalma","contextual_glosses":[{"applicability":"Bir öznenin başka bir kişiyi aç duruma getirdiği geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyen ile aç kalan kişinin ayrı katılımcılar olmasını korur."},"facet_ids":["F001"],"text":"birini aç bırakmak","usage_role":"contextual"},{"applicability":"Kişinin açlığı kendi isteğiyle ve bilinçli biçimde seçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aç kalan ile kararı veren kişinin aynı olmasını ve niyeti korur."},"facet_ids":["F002"],"text":"bilerek aç kalmak","usage_role":"contextual"},{"applicability":"Amaç sağaltım olduğunda ve kişi yemeği tümüyle bırakmak yerine doymadan kestiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sağaltım amacını ve yemeği tam doymadan kesme koşulunu korur."},"facet_ids":["F003"],"text":"sağaltım için doyuncaya kadar yememek","usage_role":"explanatory"}],"definition":"Bir başkasının aç duruma gelmesine neden olmayı veya kişinin bilinçli biçimde kendini aç tutmasını anlatır. Sağaltım amacıyla doyuncaya kadar yememek, yalnız bilinçli öz-kısıtlama yüzünün yapıya bağlı özel biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının aç duruma gelmesine neden olan geçişli eylemdir."},{"facet_id":"F002","role":"core","statement":"Kişinin bilinçli olarak aç kalmayı seçmesi ve yemeğini kısmasıdır."},{"facet_id":"F003","role":"specialization","statement":"Sağaltım amacıyla doyuncaya kadar yememek, bilinçli aç kalmanın yapıya bağlı özel uygulamasıdır."}],"identity_rationale":"Kaynak ifadesi hem bir başkasını aç bırakmayı hem de kişinin bilerek aç kalmasını bildirir; bunlar aynı eylem yönüne sahip değildir. Dal korunabilir, ancak dışarıya yönelen neden olma ile kişinin kendi yemeğini bilinçli olarak kısması ayrı çekirdek yüzler olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"onu aç bıraktı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu aç bıraktı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başkasını aç bırakma"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini aç bırakma"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bilerek aç kalmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sağaltım için doyuncaya kadar yememek"}],"lexicalization_note":"Dal, başkasını aç bırakan geçişli biçimleri, bilerek aç kalma biçimini ve sağaltım amacı taşıyan yapıya bağlı özel kullanımı ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bilinçli yeme kısıtlaması, açlıkla incelme ve ortaya çıkan açlık durumu arasındaki sınırları açıklayan üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnız bilerek aç kalma yüzündedir; odak dal başkasını aç bırakmaya da uzanırken komşu karın inceliği ve genel açlık durumlarına uzanır.","focus_only":"Odak dal ayrıca bir başkasını aç bırakma yönünü ve sağaltım için yemeyi kısma özel kullanımını kapsar.","gloss":"bilerek aç kalma ve açlıkla incelme","neighbor_only":"Komşu dal açlıkla birlikte karnın içe çekilmesini ve doğuştan ince karınlı olmayı da kapsar.","neighbor_ref":"root_000960/B008","relation_type":"near_synonym","shared_zone":"İki dal kişinin açlığı bilinçli biçimde sürdürmesi yüzünde örtüşür."},{"boundary_match":"partial","distinction":"Odakta açlık amaçlanan ya da meydana getirilen sonuçtur; komşuda belirleyici olan yemekten geri durmadır ve bunun açlık amacı taşıması gerekmez.","focus_only":"Odak dal aç kalmayı amaçlamayı veya başkasını aç bırakmayı içerir.","gloss":"bilerek aç kalma ve yemekten kaçınma","neighbor_only":"Komşu dal iştah bulunsa bile yemekten kaçınmayı, az yemeyi ya da yemeği bırakmayı içerir.","neighbor_ref":"root_000986/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda kişi kendi yemeğini bilinçli olarak sınırlandırabilir."},{"boundary_match":"partial","distinction":"Biri neden olma veya niyet taşıyan eylemi, diğeri ise eylemden bağımsız olarak bulunabilen bedensel sonucu adlandırır.","focus_only":"Odak dal açlığa neden olan veya açlığı bilinçli seçen eylemdir.","gloss":"aç bırakma ve açlık","neighbor_only":"Komşu dal midenin yiyeceksiz kalmasından doğan bedensel durumdur.","neighbor_ref":"root_000278/B001","relation_type":"near_neighbor","shared_zone":"Odak daldaki eylemin sonucu ya da amacı komşu daldaki açlık durumudur."}],"source_phrase_ar":"أجعته وجوعته فجاع يجوع (ayn;tahdhib)؛ المتعدي الإجاعة والتجويع (ayn)؛ أجاعه وجوعه (sihah)؛ تجوع أي تعمد الجوع (sihah)؛ تجوع للدواء أي لا تستوف الطعام (tahdhib)","source_summary":"Kaynakların toplu anlatımı, başkasını aç bırakma ile bilerek aç kalmayı ayırır; yemeği sağaltım amacıyla tam yememe, ikinci yönün özel ve yapıya bağlı bir uygulamasıdır.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه أجاعه وجوعه، والإجاعة والتجويع، وتعمد الجوع، وترك استيفاء الطعام للدواء.","what_is_not_ar":"لا يدخل فيه مجرد كون الشخص جائعا من غير تسبب أو قصد."},"support_links":[]},{"boundary":"Bu üç aktarım yalnız kendi yapılarında geçerlidir; bedensel açlığın yalın anlamına veya birbirlerinin bağlamlarına genellenemez.","branch_kind":"collocation","branch_ref":"root_000278/B004","candidate_links":[{"candidate_id":"cand_ddb2d7736cab346a83e6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","surface_ar":"جُوعٍ"}],"gloss":"yapıya göre özlem, kap boşluğu ya da karın inceliği","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Açlık görüntüsü yalnız belirli söz yapıları içinde, yapının belirlediği aktarmalı bir anlama taşınır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kabın aç diye nitelenmesi, kabın dolu olmadığını bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kadının kuşağının aç diye nitelenmesi, kadının karnının ince olduğunu bildirir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Buluşmaya yönelik açlık anlatımı, o buluşmaya duyulan güçlü özlemi bildirir."}}],"root_ar":"ج و ع","root_id":"root_000278","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üç kullanımı tek bir yalın karşılığa indirmeden dalın tüm kapsamını gösteren açıklayıcı üst karşılıktır.","boundary_detail":"Bu üç aktarım yalnız kendi yapılarında geçerlidir; bedensel açlığın yalın anlamına veya birbirlerinin bağlamlarına genellenemez.","branch_image_ar":"استعارة الخلو والنحول","concept_gloss":"yapıya göre özlem, kap boşluğu ya da karın inceliği","contextual_glosses":[{"applicability":"Açlık görüntüsü bir kişiyle buluşmaya duyulan güçlü özlemi anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buluşmaya yönelen güçlü özlem duygusunu korur."},"facet_ids":["F004"],"text":"seninle buluşmayı çok özledim","usage_role":"contextual"},{"applicability":"Niteleme bir kabın içinin dolu olmadığını bildirdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabın dolu olmaması durumunu doğrudan korur."},"facet_ids":["F002"],"text":"kabı dolu değil","usage_role":"contextual"},{"applicability":"Yapı bir kadının karın bölgesinin ince oluşunu betimlediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadının karnının ince oluşunu doğrudan korur."},"facet_ids":["F003"],"text":"karnı ince kadın","usage_role":"contextual"}],"definition":"Belirli söz yapılarında açlık görüntüsünü buluşmaya duyulan güçlü özleme, bir kabın dolu olmamasına veya bir kadının karnının ince oluşuna aktaran kullanımlar kümesidir. Her anlam yalnız kendisini kuran yapı içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Açlık görüntüsü yalnız belirli söz yapıları içinde, yapının belirlediği aktarmalı bir anlama taşınır."},{"facet_id":"F002","role":"source_variant","statement":"Bir kabın aç diye nitelenmesi, kabın dolu olmadığını bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kadının kuşağının aç diye nitelenmesi, kadının karnının ince olduğunu bildirir."},{"facet_id":"F004","role":"source_variant","statement":"Buluşmaya yönelik açlık anlatımı, o buluşmaya duyulan güçlü özlemi bildirir."}],"identity_rationale":"Kaynak ifadesi tek bir boşluk ve incelik anlamı vermez; belirli yapılarda buluşmaya güçlü özlem, kabın dolu olmaması ve kadının karnının ince olması şeklinde üç ayrı aktarım sunar. Dal korunur, ancak yalın bir anlam gibi değil, yapıya göre değişen kullanımlar kümesi olarak tanımlanır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"seninle buluşmayı çok özledim"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kabı dolu değil"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"karnı ince kadın"}],"lexicalization_note":"Dal bütünüyle belirli söz yapılarıyla sınırlıdır; özlem, dolu olmayan kap ve ince karın anlamları yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar incelendi; yapıya bağlı karın inceliğini doğrudan beden inceliğinden ve gerçek açlığı aktarmalı kullanımdan ayıran dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odaktaki incelik, belirli bir söz yapısının aktarmalı sonucudur; komşudaki incelik ise doğrudan beden niteliğidir ve aynı yapıya bağlı değildir.","focus_only":"Odak dal ince karın anlamını yalnız belirli bir kadın betimlemesi içinde taşır ve ayrıca iki başka aktarımı kapsar.","gloss":"yapıya bağlı ince karın ve doğrudan incelik","neighbor_only":"Komşu dal karın inceliğini ve ince beli kişi için doğrudan bir beden özelliği olarak adlandırır.","neighbor_ref":"root_000440/B001","relation_type":"near_neighbor","shared_zone":"İki dal karın bölgesinin ince görünmesi yüzünde kesişir."},{"boundary_match":"partial","distinction":"Odak belirli yapıda genel inceliği bildirir; komşu ise etin çekilmiş gibi görünmesini temel alan daha somut bir beden biçimini anlatır.","focus_only":"Odak dal ince karın yüzünü belirli bir kadın betimlemesinde verir ve özlem ile boş kap yüzlerini de içerir.","gloss":"ince karın ve içe çekilmiş karın","neighbor_only":"Komşu dal karnın içe çekilmiş ya da eti alınmış gibi ince görünmesini doğrudan anlatır.","neighbor_ref":"root_000423/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda karın bölgesinin ince ya da çekilmiş görünmesi anlatılır."},{"boundary_match":"partial","distinction":"Odak dalda gerçek yiyecek gereksinimi kurucu değildir; komşu dalda ise midenin yiyeceksizliği ve bunun doğurduğu durum anlamın çekirdeğidir.","focus_only":"Odak dal açlık görüntüsünü özlem, dolu olmayan kap ve ince karın anlamlarına aktarır.","gloss":"aktarmalı açlık ve bedensel açlık","neighbor_only":"Komşu dal midenin yiyeceksiz kalmasından doğan gerçek bedensel açlığı anlatır.","neighbor_ref":"root_000278/B001","relation_type":"near_neighbor","shared_zone":"Odaktaki kullanımlar görüntü ve anlatım gücünü bedensel açlık alanından alır."},{"boundary_match":"field_only","distinction":"Odak belirli bir beden bölgesine ve söz yapısına bağlıdır; komşu ise bütün bedenin yapısını doğrudan niteler.","focus_only":"Odak dal kadın için yalnız karın inceliğini belirli bir yapı içinde bildirir.","gloss":"ince karın ve ince biçimli beden","neighbor_only":"Komşu dal bütün bedenin ip gibi düzgün, ince ve biçimli oluşunu anlatır.","neighbor_ref":"root_001422/B002","relation_type":"same_field","shared_zone":"İki dal insan bedenindeki incelik ve biçim alanını paylaşır."}],"source_phrase_ar":"جعت إلى لقائك وعطشت إلى لقائك؛ جائع القدر إذا لم تكن قدره ملأى؛ امرأة جائعة الوشاح إذا كانت ضامرة البطن","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, buluşmaya güçlü özlem duyma, kabın dolu olmaması ve kadının karnının ince olması için üç ayrı yapıya bağlı kullanım verir."}],"source_summary":"Dal, yalın bir anlamdan çok, açlık görüntüsünü farklı sonuçlara taşıyan ve anlamı kullanılan yapıya göre belirlenen bir aktarım kümesidir.","sources":["TA"],"what_is_ar":"يدخل فيه العبارات المجازية أو الاصطلاحية: جعت إلى لقائك، وجائع القدر إذا لم تكن قدره ملأى، وجائعة الوشاح للمرأة الضامرة البطن.","what_is_not_ar":"لا يدخل فيه الجوع الحسي المباشر ولا المجاعة العامة."},"support_links":["sup_608eab685989d1373326"]},{"boundary":"Dal, yenilen yağ ürününü, soğutma anlamını ve aynı yazı ailesindeki kuş, topluluk, yer, boya ya da bölüşüm adlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000744/B001","candidate_links":[{"candidate_id":"cand_3e86a0948c7a25692d1e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"şişmanlık ve şişmanlaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedensel şişmanlık, zayıflık ve cılızlığın karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geçişli kullanım, bir kişi ya da şeyi şişman duruma getirmeyi bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir adlandırma, kadınlara kilo aldırmak amacıyla kullanılan ilacı gösterir."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel durum ile bu duruma getirme eylemini birlikte anlatan genel ve kısa karşılıktır.","boundary_detail":"Dal, yenilen yağ ürününü, soğutma anlamını ve aynı yazı ailesindeki kuş, topluluk, yer, boya ya da bölüşüm adlarını kapsamaz.","branch_image_ar":"السِّمَن ونقيض الهزال","concept_gloss":"şişmanlık ve şişmanlaştırma","contextual_glosses":[{"applicability":"Kadınlara kilo aldırmak için kullanılan özel ilaç adlandırmasının geçtiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel şişmanlık durumu ile sıradan şişmanlaştırma eylemini kapsamaz.","preserves":"İlaçla kilo aldırma işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"kilo aldırıcı ilaç","usage_role":"contextual"}],"definition":"Bir bedenin zayıf ya da cılız olmayıp yağlı ve dolgun olmasıdır; ayrıca birini bu duruma getirmeyi ve özellikle kadınlara kilo aldırmak için kullanılan bir ilacı kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedensel şişmanlık, zayıflık ve cılızlığın karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Geçişli kullanım, bir kişi ya da şeyi şişman duruma getirmeyi bildirir."},{"facet_id":"F003","role":"specialization","statement":"Özel bir adlandırma, kadınlara kilo aldırmak amacıyla kullanılan ilacı gösterir."}],"identity_rationale":"Kaynak ifadesi, bedensel şişmanlığı zayıflık ve cılızlığın karşıtı olarak verir; ayrıca birini şişmanlatma eylemini ve kadınlara kilo aldırmakta kullanılan ilacı açıkça bu dala bağlar. Geçici çerçeve bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"şişmanlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"şişmanlamak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"şişman"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"şişmanlaştırma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kadınlara kilo aldıran ilaç"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu şişman bulmak ya da saymak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"şişman bir şeyi satın almak, edinmek ya da başkasına vermek"}],"lexicalization_note":"Tanım, yalın şişmanlık durumunu çekirdek tutar; şişmanlatma, kilo aldırıcı ilaç, şişman bulma ve şişman bir şeyi edinme gibi türemiş kullanımları ayrı kapsamlar olarak korur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnızca karşıtlık, aşırı derece ve beden iriliği üzerinden sınırı keskinleştiren üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal bu eksenin şişman ve dolgun ucunu, komşu dal ise zayıf ve çökmüş ucunu gösterir.","focus_only":"Odak dal bedensel yağlılık ve dolgunluğu bildirir.","gloss":"cılızlaşma","neighbor_only":"Komşu dal bedenin cılızlaşıp hacmini yitirmesini bildirir.","neighbor_ref":"root_001347/B004","relation_type":"antonym","shared_zone":"İki dal da bedenin dolgunluk derecesini aynı eksende değerlendirir."},{"boundary_match":"partial","distinction":"Komşu dal hayvanlarla ve şişmanlığın en ileri derecesiyle sınırlıdır; odak dalın kapsamı daha genel ve türetimce daha geniştir.","focus_only":"Odak dal her derecedeki şişmanlığı, şişmanlaştırmayı ve özel ilaç kullanımını kapsar.","gloss":"aşırı şişmanlık","neighbor_only":"Komşu dal özellikle dişi deve ya da kesimlik hayvanın aşırı şişmanlığına ulaşmasını anlatır.","neighbor_ref":"root_001560/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bedensel şişmanlık durumunu adlandırır."},{"boundary_match":"partial","distinction":"Odak dal yağlılık durumunu zayıflığın karşıtı olarak kurar; komşu dal ise beden hacmi ve iriliği yönünü daha belirgin taşır.","focus_only":"Odak dal şişmanlatma eylemi ile kilo aldırıcı ilaç kullanımını da içerir.","gloss":"iri ve tıknaz olma","neighbor_only":"Komşu dal bedenin iriliğini, hacimliliğini ve tıknazlığını öne çıkarır.","neighbor_ref":"root_000096/B004","relation_type":"near_synonym","shared_zone":"Her ikisi de bedensel dolgunluk ve şişmanlık alanında örtüşür."}],"source_phrase_ar":"السمن نقيض الهزال (ayn;tahdhib;mufradat)؛ خلاف الضمر والهزال (maqayis)؛ السمين خلاف المهزول (sihah)؛ أسمنته وسمنته جعلته سمينا (mufradat)؛ السمنة دواء تسمن به النساء (ayn;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar şişmanlığı zayıflığın karşıtı sayma, birini şişmanlatma ve kilo aldırıcı ilaç anlamlarında birleşir. Böylece durum anlamı çekirdeği, ettirgen eylem ve ilaç kullanımı ise ona bağlı kapsamları oluşturur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السِّمَن والسَّمين والسِّمان والتسمين بمعنى جعل الشيء سمينا والسُّمْنة الدواء واستسمانه وجدان السمن فيه","what_is_not_ar":"لا يدخل فيه السَّمْن المأكول ولا التبريد ولا الطائر ولا أسماء الفرق والمواضع"},"support_links":["sup_4115f3d79c0e6aca9aa1"]},{"boundary":"Dal bedensel şişmanlığı değil, yenilebilir süt yağı ürününü ve yalnızca bu ürüne bağlı eylemleri kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000744/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"arıtılmış tereyağı ve kullanımları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, özellikle inek sütünden ve kimi kullanımlarda keçi sütünden elde edilen yenilebilir arıtılmış yağdır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ürün yemeğe katılabilir ya da onunla karıştırılarak yemek hazırlanabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş kullanımlar topluluğa bu yağdan azık vermeyi, armağan istemeyi ve ürünü satan kişiyi bildirir."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ürünün kendisini ve kanıtlanan yiyecek, azık, armağan ve satış kullanımlarını birlikte temsil eder.","boundary_detail":"Dal bedensel şişmanlığı değil, yenilebilir süt yağı ürününü ve yalnızca bu ürüne bağlı eylemleri kapsar.","branch_image_ar":"السَّمْن وسلاء اللبن","concept_gloss":"arıtılmış tereyağı ve kullanımları","contextual_glosses":[{"applicability":"Yiyeceğin bu yağla hazırlanması ya da karıştırılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ürün adı ile azık, armağan ve satış kullanımlarını dışarıda bırakır.","preserves":"Yağın yiyeceğe katılması işlemini eksiksiz korur."},"facet_ids":["F002"],"text":"yemeğe arıtılmış tereyağı katmak","usage_role":"contextual"},{"applicability":"Bir topluluğa bu üründen yol azığı ya da erzak sağlama bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ürünün yalın adını ve öteki bağlı eylemleri kapsamaz.","preserves":"Topluluğa yağ ürünü sağlama işlemini korur."},"facet_ids":["F003"],"text":"arıtılmış tereyağı azığı vermek","usage_role":"contextual"}],"definition":"Sütten elde edilen yenilebilir arıtılmış yağdır; bu yağın yemeğe katılması, topluluğa azık olarak verilmesi, armağan edilmesinin istenmesi ve satılması da dala bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, özellikle inek sütünden ve kimi kullanımlarda keçi sütünden elde edilen yenilebilir arıtılmış yağdır."},{"facet_id":"F002","role":"associated_use","statement":"Ürün yemeğe katılabilir ya da onunla karıştırılarak yemek hazırlanabilir."},{"facet_id":"F003","role":"extension","statement":"Türemiş kullanımlar topluluğa bu yağdan azık vermeyi, armağan istemeyi ve ürünü satan kişiyi bildirir."}],"identity_rationale":"Kaynak ifadesi, sütten elde edilen yenilebilir arıtılmış yağı çekirdek yapar ve yemeğe katma, topluluğa azık verme, armağan isteme ve satma kullanımlarını açıkça sıralar. Geçici çerçeve ürün ile ona bağlı işlemleri doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"arıtılmış tereyağı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yemeğe arıtılmış tereyağı katmak ya da onunla karıştırmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"topluluğa arıtılmış tereyağı azığı vermek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"arıtılmış tereyağının armağan edilmesini istemek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"arıtılmış tereyağı satıcısı"}],"lexicalization_note":"Yalın ürün adı çekirdektir; yemeğe katma, azık verme, armağan isteme ve satıcılık anlamları yalnızca kendi kalıplaşmış ya da türemiş kullanımları içinde geçerlidir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; ürün türünü, üretim aşamasını, benzer kullanım örüntüsünü ve bedensel durumdan ayrımı açıklayan dört karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal süt kökenli belirli bir üründür; komşu dal farklı kaynaklardan gelen yağları ve tencere yüzeyindeki yağı da içine alan daha geniş bir sınıftır.","focus_only":"Odak dal özellikle sütten elde edilen arıtılmış yenilebilir yağı gösterir.","gloss":"eritilmiş yemeklik yağlar","neighbor_only":"Komşu dal kuyruk yağı, iç yağı, hayvansal yağ ya da bitkisel yağ gibi daha geniş bir yağlı yiyecek kümesini kapsar.","neighbor_ref":"root_000064/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi de yiyeceğe eşlik eden yenilebilir yağ maddelerini kapsar."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan tereyağı aşamasında kalırken odak dal arıtılmış ürün kimliğini ve bu ürüne bağlı eylemleri taşır.","focus_only":"Odak dal ayrıştırılmış ve yenilen süt yağı ürününü bildirir.","gloss":"tereyağı","neighbor_only":"Komşu dal sütün çalkalanmasıyla oluşan tereyağını bildirir.","neighbor_ref":"root_000336/B009","relation_type":"near_neighbor","shared_zone":"İki dal da sütten elde edilen yağlı yiyecek ürünleridir."},{"boundary_match":"partial","distinction":"İşlem örüntüsü benzerdir, fakat odak dalın maddesi süt yağı, komşu dalın maddesi bitkisel yağdır.","focus_only":"Odak dal süt yağını yiyeceğe katma, azık verme, isteme ve satma kapsamlarına sahiptir.","gloss":"bitkisel yağı yiyecek ve azık olarak kullanma","neighbor_only":"Komşu dal aynı tür eylemleri bitkisel yağ üzerinden kurar.","neighbor_ref":"root_000656/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalda yağlı bir ürün yiyeceğe katılır, azık yapılır ya da armağan olarak istenir."},{"boundary_match":"partial","distinction":"Birinde gönderge yiyecek olan yağ ürünüdür, ötekinde ise bedenin durumu ya da bu duruma getirilmesidir.","focus_only":"Odak dal yenilebilir bir süt yağı ürününü ve bu ürüne bağlı işlemleri gösterir.","gloss":"şişmanlık","neighbor_only":"Komşu dal bedenin şişmanlık durumunu ve şişmanlaştırmayı gösterir.","neighbor_ref":"root_000744/B001","relation_type":"near_neighbor","shared_zone":"İki dal yağlılık düşüncesi çevresinde tarihsel bir anlam yakınlığı taşır."}],"source_phrase_ar":"والسمن من هذا (maqayis)؛ السمن سلاء اللبن (ayn;tahdhib)؛ السمن للبقر وقد يكون للمعزى (sihah)؛ سمنت الطعام إذا جعلت فيه السمن (tahdhib)؛ سمنت لهم الطعام إذا لتته بالسمن (sihah)؛ سمنت القوم تسمينا زودتهم السمن (sihah;tahdhib)؛ جاءوا يستسمنون أي يطلبون أن يوهب لهم السمن (sihah;tahdhib)؛ السمان بائع السمن (sihah)","source_summary":"Kaynakların ortak çizgisi, süt kökenli yenilebilir arıtılmış yağ ve bu ürünün yiyecekte, azık vermede, armağan istemede ve ticarette kullanılmasıdır. Ürüne ilişkin eylemler yalın anlamın yerine geçmez.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السَّمْن المأكول وسلاء اللبن وإدام الطعام بالسَّمْن وزود القوم بالسَّمْن وطلب هبته وبيع السَّمْن","what_is_not_ar":"لا يدخل فيه السِّمَن البدني ولا التبريد ولا السَّمّ"},"support_links":[]},{"boundary":"Bu dal yalnızca soğutma anlamındaki kullanımları kapsar; bedensel şişmanlık, süt yağı ürünü ya da yiyecek hazırlama anlamı buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000744/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"soğutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne alan kullanım, bir şeyin sıcaklığını düşürmek anlamındadır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem adı biçimi doğrudan soğutma işlemini adlandırır."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin sıcaklığını düşürme çekirdeğini en kısa ve doğal biçimde karşılar.","boundary_detail":"Bu dal yalnızca soğutma anlamındaki kullanımları kapsar; bedensel şişmanlık, süt yağı ürünü ya da yiyecek hazırlama anlamı buraya taşınmaz.","branch_image_ar":"التبريد الشاذ","concept_gloss":"soğutma","contextual_glosses":[{"applicability":"Eylemin açık bir nesne aldığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin sıcaklığını düşürme işlemini tam olarak korur."},"facet_ids":["F001"],"text":"bir şeyi soğutmak","usage_role":"general"}],"definition":"Bir şeyi soğutmak, yani sıcaklığını düşürmek eylemidir; aynı anlam eylem adı olarak da kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne alan kullanım, bir şeyin sıcaklığını düşürmek anlamındadır."},{"facet_id":"F002","role":"source_variant","statement":"Eylem adı biçimi doğrudan soğutma işlemini adlandırır."}],"identity_rationale":"Kaynak ifadesi hem bir şeyi soğutma eylemini hem de eylem adının soğutma anlamını açıkça verir. Geçici çerçevenin sıra dışı olarak nitelediği kullanım, kaynak çekirdeğiyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir şeyi soğutmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"soğutma"}],"lexicalization_note":"Soğutma anlamı hem bir nesne alan kalıp içinde hem de eylem adı biçiminde kanıtlanır; tanım bu iki kapsamı ayırarak korur.","neighbor_coverage_note":"Bütün adaylar incelendi; kurutma, pişirme ve benzeri süreçler çekirdekle örtüşmediği için yalnızca genel soğukluk alanı ve soğuk su karşılaştırmaları tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dar bir ettirgen soğutma anlamıdır; komşu dal soğukluk çevresindeki durum, süreç, araç ve doğa olaylarını daha geniş biçimde kapsar.","focus_only":"Odak dal belirli söz biçimlerinde yalnızca soğutma işlemini bildirir.","gloss":"soğukluk ve soğuma","neighbor_only":"Komşu dal soğukluk durumunu, soğuklaşmayı, soğutan şeyleri, yağışı ve başka bağlı kullanımları da kapsar.","neighbor_ref":"root_000103/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı bir şeyin sıcaklığının düşmesi ya da düşürülmesidir."},{"boundary_match":"partial","distinction":"Odak dal değiştirici bir eylemdir; komşu dal ise soğuk niteliği taşıyan bir maddeyi adlandırır.","focus_only":"Odak dal bir şeyi soğutma işlemini gösterir.","gloss":"soğuk su","neighbor_only":"Komşu dal yalnızca soğuk nitelikli belirli bir su adlandırmasını gösterir.","neighbor_ref":"root_000403/B006","relation_type":"near_neighbor","shared_zone":"İki dal sıcaklığın düşük olmasıyla ilişkilidir."}],"source_phrase_ar":"سمنت الشيء إذا بردته (maqayis)؛ التسمين التبريد (maqayis;tahdhib)؛ سمنها أي بردها (maqayis;sihah;tahdhib)","source_summary":"Kaynaklar, dalın belirli biçimlerinde soğutma anlamını ortaklaşa doğrular. Nesne alan eylem ile eylem adı aynı çekirdeğe bağlıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه سمنت الشيء بمعنى بردته والتسمين بمعنى التبريد وأمر تبريد السمكة","what_is_not_ar":"لا يدخل فيه السِّمَن ولا السَّمْن ولا إدام الطعام"},"support_links":[]},{"boundary":"Çekirdek, tavuk yavrusuna benzetilen kuştur; başka bir kuşla özdeşlik olası ve tartışmalı bir kaynak görüşüdür.","branch_kind":"bare","branch_ref":"root_000744/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"tavuk yavrusuna benzeyen, kimliği tartışmalı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, tavuk yavrusuna benzetilen bir kuş adını gösterir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı aktarımlar kuşu başka bir kuş adıyla özdeşleştirir, ancak görüş kesinleştirilmez."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş oluşunu, verilen benzetmeyi ve tür özdeşliğindeki belirsizliği birlikte koruyan açıklayıcı karşılıktır.","boundary_detail":"Çekirdek, tavuk yavrusuna benzetilen kuştur; başka bir kuşla özdeşlik olası ve tartışmalı bir kaynak görüşüdür.","branch_image_ar":"طائر السُّمانى","concept_gloss":"tavuk yavrusuna benzeyen, kimliği tartışmalı kuş","definition":"Tavuk yavrusuna benzediği belirtilen bir kuştur; bazı aktarımlar onu başka bir kuş adıyla özdeşleştirse de bu eşitlik ortak ve kesin değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, tavuk yavrusuna benzetilen bir kuş adını gösterir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı aktarımlar kuşu başka bir kuş adıyla özdeşleştirir, ancak görüş kesinleştirilmez."}],"identity_rationale":"Kaynak ifadesi adı verilen bir kuşu ve tekil biçimini kesin olarak bildirir, fakat kuşun başka bir kuş adıyla özdeşliği yalnızca bazı aktarımlarda ileri sürülür. Bu nedenle dal korunur, ancak tür eşitliği kesin bilgi gibi sunulmaz.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"tavuk yavrusuna benzeyen, başka bir kuşla da özdeşleştirilen kuş"}],"lexicalization_note":"Tanım yalnızca yalın kuş adını kapsar; aynı yazı ailesindeki bedensel durum, yiyecek, topluluk ya da yer anlamlarını içermez.","neighbor_coverage_note":"Tüm kuş ve hayvan adayları incelendi; yalnızca doğrudan benzerlik ve olası özdeşlik bildiren kuş dalı anlam sınırını keskinleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme güçlüdür, fakat eldeki kanıt özdeşliği kesinleştirmediğinden tam eş anlamlılık kurulamaz.","focus_only":"Odak dal tavuk yavrusuna benzetilir ve iki adın özdeşliği yalnızca olası bir görüş olarak verilir.","gloss":"benzer ya da aynı sayılan kuş","neighbor_only":"Komşu dal benzer kuşu ayrı bir yalın ad ve onun tekil biçimiyle sunar.","neighbor_ref":"root_000738/B004","relation_type":"near_synonym","shared_zone":"Kaynak kartları iki kuşu birbirine benzetir ve bazı aktarımlar onları aynı sayar."}],"source_phrase_ar":"السمانى طائر شبه الفروجة الواحدة سماناة وقيل إنه السلوى (ayn)؛ السماني طائر ولا يقال سمانى بالتشديد (sihah)؛ السمانى طائر وبعضهم يقول إنه السلوى (tahdhib)؛ السمانى طائر (mufradat)","source_summary":"Kaynaklar bunun bir kuş adı olduğu konusunda birleşir. Tavuk yavrusuna benzerliği ve başka bir kuşla aynı sayılması ise bütün kaynakların aynı kesinlikle paylaştığı özellikler değildir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الطائر المسمى السُّمانى والواحدة سماناة وما قيل إنه السلوى","what_is_not_ar":"لا يدخل فيه السِّمَن ولا السَّمْن ولا السُّمَنيّة"},"support_links":[]},{"boundary":"Dal bir kuşu, bedensel şişmanlığı ya da yenilebilir yağı değil, kaynaklarda farklı biçimlerde nitelenen tarihsel bir inanç topluluğunu gösterir.","branch_kind":"bare","branch_ref":"root_000744/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"Hindistanlı tarihsel inanç topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, Hindistan'dan ve kendine özgü inancı olan bir topluluk kimliğidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak nitelemeleri materyalistlik, putperestlik ve ruh göçü inancı arasında değişir."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Topluluk kimliğini kaynakların tartışmalı inanç nitelemelerinden daha kısa ve yansız biçimde temsil eder.","boundary_detail":"Dal bir kuşu, bedensel şişmanlığı ya da yenilebilir yağı değil, kaynaklarda farklı biçimlerde nitelenen tarihsel bir inanç topluluğunu gösterir.","branch_image_ar":"السُّمَنيّة فرقة من الهند","concept_gloss":"Hindistanlı tarihsel inanç topluluğu","contextual_glosses":[{"applicability":"Tarihsel kaynakların topluluğa yüklediği farklı inanç nitelemelerinin açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kökeni, topluluk kimliğini ve değişen kaynak nitelemelerini korur."},"facet_ids":["F001","F002"],"text":"kaynaklarda materyalist ya da putperest diye nitelenen Hindistanlı topluluk","usage_role":"explanatory"}],"definition":"Hindistan'dan, kendine özgü bir inancı bulunan ve kaynaklarda materyalist ya da putperest diye nitelenen bir topluluktur; bir aktarım ayrıca ruh göçüne inandıklarını söyler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, Hindistan'dan ve kendine özgü inancı olan bir topluluk kimliğidir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak nitelemeleri materyalistlik, putperestlik ve ruh göçü inancı arasında değişir."}],"identity_rationale":"Kaynak ifadesi Hindistan'dan ayrı inançlı bir topluluğu bildirir; aktarımlar topluluğu materyalist ya da putperest olarak niteler ve bir aktarım ruh göçü inancını ekler. Geçici çerçeve bu tarihsel kaynak nitelemelerini yeterince yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"Hindistanlı, ayrı inançlı ve kaynaklarda materyalist ya da putperest diye nitelenen topluluk"}],"lexicalization_note":"Tanım yalnızca yalın topluluk adının kanıtlanan tarihsel kullanımını kapsar ve kaynak nitelemelerini çağdaş öz tanım gibi genelleştirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca başka bir Hindistanlı topluluk ile topluluk-inanç düzeni ayrımını gösteren iki alan ilişkisi yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak coğrafi ve dinsel alan kimlik eşitliği doğurmaz; topluluklar ve onlara yüklenen öğretiler ayrıdır.","focus_only":"Odak dal kaynaklarda materyalistlik, putperestlik ve ruh göçüyle nitelenen ayrı bir Hindistanlı topluluktur.","gloss":"başka bir Hindistanlı inanç topluluğu","neighbor_only":"Komşu dal elçilerin gönderilmesine ilişkin görüşüyle tanıtılan başka bir topluluğu gösterir.","neighbor_ref":"root_000111/B004","relation_type":"same_field","shared_zone":"Her iki dal da Hindistan bağlantılı tarihsel inanç topluluklarını adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal insan topluluğudur; komşu dal ise bir topluluğun ya da kişinin izlediği inanç düzenidir.","focus_only":"Odak dal belirli bir tarihsel topluluğu adlandırır.","gloss":"benimsenen inanç düzeni","neighbor_only":"Komşu dal benimsenen din ya da öğreti kavramını genel olarak adlandırır.","neighbor_ref":"root_001445/B003","relation_type":"same_field","shared_zone":"Topluluk kimliği ile benimsenen inanç düzeni aynı dinsel alanda ilişkilidir."}],"source_phrase_ar":"السمنية قوم من أهل الهند لهم دين على حدة دهريون (ayn)؛ السمنية فرقة من عبدة الاصنام تقول بالتناسخ (sihah)؛ السمنية قوم من الهند دهريون (tahdhib)","source_summary":"Kaynaklar topluluğun Hindistan kökenli ve ayrı bir inanca sahip olduğu çizgisinde buluşur. İnancın materyalistlik, putperestlik ya da ruh göçü üzerinden açıklanması kaynak nitelemelerindeki çeşitliliği gösterir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السُّمَنيّة قوم من الهند وفرقة من عبدة الأصنام أو الدهريين","what_is_not_ar":"لا يدخل فيه طائر السُّمانى ولا السِّمَن ولا السَّمْن"},"support_links":[]},{"boundary":"Dal genel olarak her boya ya da boyama eylemini değil, bezemek için kullanılan boya maddelerini gösterir.","branch_kind":"bare","branch_ref":"root_000744/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"bezeme boyaları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, bezeme amacıyla kullanılan boya maddeleridir."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Boya maddelerini ve onların bezeme amacını birlikte belirten doğal karşılıktır.","boundary_detail":"Dal genel olarak her boya ya da boyama eylemini değil, bezemek için kullanılan boya maddelerini gösterir.","branch_image_ar":"السَّمان أصباغ الزخرفة","concept_gloss":"bezeme boyaları","definition":"Bir yüzeyi ya da nesneyi bezemek için kullanılan boya maddeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, bezeme amacıyla kullanılan boya maddeleridir."}],"identity_rationale":"Tek kaynaklı ifade doğrudan bezemede kullanılan boyaları tanımlar. Geçici çerçeve bu dar araç ve kullanım ilişkisini ekleme yapmadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bezeme boyaları"}],"lexicalization_note":"Tanım yalın boya adını, kanıtlanan bezeme işleviyle sınırlı tutar; satıcı ya da başka eşsesli anlamları içeri almaz.","neighbor_coverage_note":"Adayların tümü tarandı; genel boyama alanı ile belirli boya türleri arasından dalın bezeme amacı sınırını açıklayan üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bezeme amaçlı maddeyle sınırlıdır; komşu dal işlem, madde, meslek ve yer anlamlarını kapsayan daha geniş bir alandır.","focus_only":"Odak dal yalnızca bezemede kullanılan boya maddelerini adlandırır.","gloss":"boyama ve boya","neighbor_only":"Komşu dal boyama eylemini, boya maddesini, boyacılık işini ve boyama yerini birlikte kapsar.","neighbor_ref":"root_000842/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak bölgesi renk vermekte kullanılan boya maddesidir."},{"boundary_match":"partial","distinction":"Odak dal işlevsel bir boya kümesidir; komşu dal belirli boya maddesi ile onun uygulanmasını kapsar.","focus_only":"Odak dal bezemeye yarayan boyaları tür belirtmeden topluca adlandırır.","gloss":"toprak boyasıyla boyama","neighbor_only":"Komşu dal belirli bir toprak boyasını ve onunla boyanma eylemini bildirir.","neighbor_ref":"root_001438/B004","relation_type":"near_neighbor","shared_zone":"İki dal renk verici madde ve süsleme amacı çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal kullanım amacına göre, komşu dal ise renk türü ve boyanmış nesneye uzanan kapsamıyla ayrılır.","focus_only":"Odak dal bezemede kullanılan boya maddelerini genel bırakır.","gloss":"kırmızı ya da sarı boya","neighbor_only":"Komşu dal özellikle kırmızı ya da sarı, yoğun renk veren boya ve boyanmış nesne anlamlarını taşır.","neighbor_ref":"root_000245/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal somut renk verici maddeleri kapsar."}],"source_phrase_ar":"السمان هذه الأصباغ التي يزخرف بها (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, bu adı bezemede kullanılan boya maddeleri olarak açıklar."}],"source_summary":"Çoklu kaynak ortaklığı yoktur; kanıt, dalı bezemede kullanılan boya maddeleriyle sınırlayan tek bir aktarımdan gelir.","sources":["AY"],"what_is_ar":"يدخل فيه السَّمان بمعنى الأصباغ التي يزخرف بها","what_is_not_ar":"لا يدخل فيه بائع السَّمْن ولا السَّمّ"},"support_links":[]},{"boundary":"Dal yalnızca belirli bir yer adıdır; genel yer, çöl, kasaba ya da yükseklik kavramı değildir.","branch_kind":"non_bare","branch_ref":"root_000744/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"kasaba ya da çöldeki yer adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, belirli bir coğrafi yeri adlandıran özel addır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yer türü bir aktarımda kasaba, diğerinde çöldeki yer olarak sınıflandırılır."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın yazımını üretmeden, iki kaynakta verilen coğrafi sınıflandırmayı yansıtır.","boundary_detail":"Dal yalnızca belirli bir yer adıdır; genel yer, çöl, kasaba ya da yükseklik kavramı değildir.","branch_image_ar":"سَمْنان الموضع","concept_gloss":"kasaba ya da çöldeki yer adı","definition":"Bir kaynakta kasaba, başka bir kaynakta çöldeki bir yer olarak tanımlanan özel yer adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, belirli bir coğrafi yeri adlandıran özel addır."},{"facet_id":"F002","role":"source_variant","statement":"Yer türü bir aktarımda kasaba, diğerinde çöldeki yer olarak sınıflandırılır."}],"identity_rationale":"Kaynak ifadesi aynı adı bir aktarımda kasaba, diğerinde çöldeki bir yer olarak verir. Geçici çerçeve bu iki coğrafi sınıflandırmayı kesin bir yer türüne zorlamadan korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir kasabanın ya da çöldeki bir yerin adı"}],"lexicalization_note":"Tanım, yalnızca kanıtlanan özel yer adı kullanımına bağlıdır ve kökün yalın ya da başka türemiş anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar başka yer adları ya da genel coğrafi kavramlardır; odak yerin kimliğini veya kasaba-çöl sınıflandırmasını daha fazla açıklayan güvenilir bir anlam ilişkisi yoktur.","source_phrase_ar":"سمنان بلدة (ayn)؛ سمنان موضع في البادية (tahdhib)","source_summary":"Kaynaklar belirli bir yer adından söz eder; yerin kasaba mı yoksa çölde bir mevki mi olduğu konusunda farklı sınıflandırmalar sunar.","sources":["AY","TA"],"what_is_ar":"يدخل فيه سَمْنان اسم بلدة أو موضع في البادية","what_is_not_ar":"لا يدخل فيه السِّمَن ولا السَّمْن ولا السُّمانى"},"support_links":[]},{"boundary":"Dal sıradan bölüşümden daha dardır: ortaklar, eşitsiz paylar, fazla alan ile eksik kalan arasındaki geri verme işlemi birlikte bulunmalıdır.","branch_kind":"bare","branch_ref":"root_000744/B008","candidate_links":[{"candidate_id":"cand_7a78400a7dfe63137f2e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"fazlayı geri vererek ortaklık paylarını denkleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey ortaklar arasında paylaştırılır ve paylardan biri ötekinden fazla çıkar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fazlayı elinde tutan ortak, kaybı olan ortağa geri vererek payları eşitler."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortakları, başlangıçtaki pay eşitsizliğini, geri verme işlemini ve eşitleme sonucunu birlikte korur.","boundary_detail":"Dal sıradan bölüşümden daha dardır: ortaklar, eşitsiz paylar, fazla alan ile eksik kalan arasındaki geri verme işlemi birlikte bulunmalıdır.","branch_image_ar":"التسمين بين الشركاء","concept_gloss":"fazlayı geri vererek ortaklık paylarını denkleştirme","contextual_glosses":[{"applicability":"Geri verme işleminin bağlamdan açıkça anlaşıldığı bölüşüm anlatılarında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fazla alanın eksik kalana geri verme işlemini açıkça söylemez.","preserves":"Ortaklar arasındaki pay eşitsizliğini giderme sonucunu korur."},"facet_ids":["F001","F002"],"text":"ortakların pay farkını giderme","usage_role":"contextual"}],"definition":"Ortaklar arasındaki bölüşümde paylar eşit çıkmadığında, fazla pay alanın bu fazlayı payı eksik kalana geri vererek payları denkleştirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey ortaklar arasında paylaştırılır ve paylardan biri ötekinden fazla çıkar."},{"facet_id":"F002","role":"core","statement":"Fazlayı elinde tutan ortak, kaybı olan ortağa geri vererek payları eşitler."}],"identity_rationale":"Kaynak ifadesi, ortaklar arasındaki bölüşümde paylardan birinin fazla kalması üzerine fazlayı elinde tutanın kaybeden ortağa geri vermesini kurucu işlem olarak belirtir. Geçici çerçeve hem bölüşümü hem denkleştirme sonucunu doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"fazla pay alanın eksik kalana geri vererek ortaklık paylarını denkleştirmesi"}],"lexicalization_note":"Tanım bu yalın terimi ortaklık bölüşümündeki denkleştirme işlemiyle sınırlar; şişmanlaştırma ya da soğutma anlamlarına genişletmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel ortaklık paylaşımı, payların ayrılması ve haksız bölüşüm karşıtlığı dalın kurucu geri verme işlemini en iyi açıklayan ilişkilerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir eşitsizlik ve düzeltici geri verme düzenine bağlıdır; komşu dal bu işlemleri zorunlu kılmayan genel bir ortaklık çözümüdür.","focus_only":"Odak dal, fazla pay alanın eksik kalana geri vermesiyle payların eşitlenmesini zorunlu kılar.","gloss":"ortakla paylaşma ve hesaplaşma","neighbor_only":"Komşu dal ortakların ayrılması, paylaşması ya da aralarında genel bir hesaplaşma yapması anlamlarını daha geniş tutar.","neighbor_ref":"root_001159/B014","relation_type":"near_synonym","shared_zone":"İki dal da ortaklar arasındaki bir şeyi paylaşma ve hesapları düzenleme alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal ayrılma ve paylaştırma sürecine, odak dal ise pay farkını düzeltme mekanizmasına odaklanır.","focus_only":"Odak dal bölüşümden sonra ortaya çıkan fazlayı geri vererek payları eşitler.","gloss":"ortakların paylarını ayırması","neighbor_only":"Komşu dal ortakların ya da mirasçıların paylaşımdan çıkarak paylarını ayırmasını anlatır.","neighbor_ref":"root_000400/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal ortaklar veya hak sahipleri arasındaki paylaştırmayı düzenler."},{"boundary_match":"opposed","distinction":"Odak dal eşitsizliği onaran işlemi, komşu dal ise eşitsizlik üreten veya hakkı eksilten bölüşümü gösterir.","focus_only":"Odak dal pay eşitsizliğini geri verme yoluyla giderir.","gloss":"haksız ve eksik bölüşüm","neighbor_only":"Komşu dal hakkı eksilten ya da haksızlaştıran kusurlu bölüşümü bildirir.","neighbor_ref":"root_000922/B001","relation_type":"polarity_pair","shared_zone":"İki dal bölüşümün hak ve eşitlik eksenindeki sonucunu değerlendirir."}],"source_phrase_ar":"التسمين أن تقسم شيئا بين الشركاء فيكون في الأنصباء فضل لبعضهما على بعض فيرد كل من في يده فضل على الذي خسر نصيبه (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, fazla pay alan ortağın eksik kalana geri vererek payları denkleştirdiği bölüşümü anlatır."}],"source_summary":"Çoklu kaynak ortaklığı yoktur; tek aktarım, ortaklık bölüşümündeki pay farkının fazlayı geri verme yoluyla giderilmesini bütün aşamalarıyla tanımlar.","sources":["AY"],"what_is_ar":"يدخل فيه التسمين في قسمة الشيء بين الشركاء ورد الفضل حتى تستوي الأنصباء","what_is_not_ar":"لا يدخل فيه التسمين بمعنى جعل الشيء سمينا ولا التسمين بمعنى التبريد"},"support_links":["sup_a4cff254ebf451c7f80b"]},{"boundary":"Dal bütün eski giysileri değil, özellikle eskimiş bel örtülerini gösterir; boya, yağ ya da bedensel durum anlamı içermez.","branch_kind":"bare","branch_ref":"root_000744/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"eskimiş bel örtüleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, bel çevresine sarılan örtülerdir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu örtüler eski ve yıpranmış olma niteliği taşır."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Giysi türünü, çoğulluğu ve yıpranmışlık koşulunu eksiksiz taşıyan doğal karşılıktır.","boundary_detail":"Dal bütün eski giysileri değil, özellikle eskimiş bel örtülerini gösterir; boya, yağ ya da bedensel durum anlamı içermez.","branch_image_ar":"الأسمان الأزر الخلقان","concept_gloss":"eskimiş bel örtüleri","definition":"Eskimiş ve yıpranmış bel örtülerini topluca adlandıran bir giysi terimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, bel çevresine sarılan örtülerdir."},{"facet_id":"F002","role":"core","statement":"Bu örtüler eski ve yıpranmış olma niteliği taşır."}],"identity_rationale":"Tek kaynaklı ifade, söz konusu çoğul biçimi eskimiş bel örtüleriyle açıkça eşler. Geçici çerçeve hem giysi türünü hem yıpranmışlık niteliğini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"eskimiş bel örtüleri"}],"lexicalization_note":"Tanım yalın çoğul giysi adını, bel örtüsü olma ve eskimişlik koşullarıyla birlikte korur.","neighbor_coverage_note":"Bütün giysi adayları karşılaştırıldı; geniş eski giysi sınıfı, parçalanmış giysi ve genel bel örtüsü dalları odak sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal giysi türü bakımından bel örtüsüyle sınırlıdır; komşu dalın nesne kapsamı daha geniştir.","focus_only":"Odak dal yalnızca eskimiş bel örtülerini çoğul olarak adlandırır.","gloss":"eskimiş dokuma ve giysi","neighbor_only":"Komşu dal giysi, yaygı ve benzeri birçok yıpranmış dokumayı kapsar.","neighbor_ref":"root_000470/B003","relation_type":"near_synonym","shared_zone":"İki dal eskiyip yıpranmış giysileri adlandırır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir giysi türünü, komşu dal ise giysinin parçalanma durumunu ayırt edici özellik yapar.","focus_only":"Odak dal bel örtüsü türünü ve eskiliği zorunlu kılar.","gloss":"parçalanmış eski giysi","neighbor_only":"Komşu dal giysinin parçalara ayrılmış ya da yırtılmış olmasını öne çıkarır.","neighbor_ref":"root_000786/B003","relation_type":"near_synonym","shared_zone":"Her iki dal yıpranmış ve kullanılamazlaşmaya yaklaşmış giysiler alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yıpranmış çoğul nesneleri adlandırır; komşu dal nesnenin genel adını ve giyilme eylemini kapsar.","focus_only":"Odak dal bel örtülerinin eski ve yıpranmış olmasını gerektirir.","gloss":"bel örtüsü ve onu sarınma","neighbor_only":"Komşu dal bel örtüsünün kendisini ve onu giyme ya da bağlama eylemini eskilik koşulu olmadan kapsar.","neighbor_ref":"root_000027/B003","relation_type":"near_neighbor","shared_zone":"İki dalın ortak gönderge alanı bel çevresine sarılan giysidir."}],"source_phrase_ar":"الأسمال والأسمان الأزر الخلقان (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek aktarım, bu çoğul adı eskimiş bel örtüleri olarak tanımlar."}],"source_summary":"Çoklu kaynak ortaklığı yoktur; tek aktarım hem giysi türünü hem de eskimişlik niteliğini birlikte verir.","sources":["TA"],"what_is_ar":"يدخل فيه الأسمان بمعنى الأزر الخلقان","what_is_not_ar":"لا يدخل فيه السِّمَن ولا السَّمْن ولا الأصباغ"},"support_links":[]},{"boundary":"Tanım, yalnızca kanıtlanan çoğul eylem biçimine bağlıdır ve asılsız övünme, toplumsal yükselme amaçlı mal biriktirme ile çok yeme yorumlarını ayrı tutar.","branch_kind":"non_bare","branch_ref":"root_000744/B010","candidate_links":[{"candidate_id":"cand_ddb2d7736cab346a83e6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","surface_ar":"يُسْمِنُ"}],"gloss":"sahip olmadığı iyilik ve saygınlıkla övünme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başlıca yorum, kişide bulunmayan iyilik ve saygınlığı varmış gibi göstererek bunlarla övünmesidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İkinci yorum, seçkin ve saygın kişilerin düzeyine erişmek amacıyla mal biriktirmedir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başka bağlamlandırma, çok yeme ve bunun kınanmasıyla bağlantı kurar."}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın ilk ve en açık açıklamasını doğal Türkçeyle verir; öteki iki yorumu tek karşılığa zorlamaz.","boundary_detail":"Tanım, yalnızca kanıtlanan çoğul eylem biçimine bağlıdır ve asılsız övünme, toplumsal yükselme amaçlı mal biriktirme ile çok yeme yorumlarını ayrı tutar.","branch_image_ar":"التكثّر بما ليس للمرء","concept_gloss":"sahip olmadığı iyilik ve saygınlıkla övünme","contextual_glosses":[{"applicability":"Toplumsal düzeyini yükseltmek amacıyla mal toplama yorumunun izlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Asılsız övünme ve çok yeme yorumlarını kapsamaz.","preserves":"Servet biriktirme amacını ve hedeflenen toplumsal yükselmeyi korur."},"facet_ids":["F002"],"text":"seçkinlere yetişmek için servet biriktirmek","usage_role":"contextual"},{"applicability":"Biçimin çok yeme ve bunun kınanmasıyla ilişkilendirildiği alternatif açıklamada kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Asılsız övünme ve servet biriktirme yorumlarını kapsamaz.","preserves":"Çok yeme ve bedensel irileşme bağlantısını korur."},"facet_ids":["F003"],"text":"çok yiyip irileşmek","usage_role":"contextual"}],"definition":"Bir yoruma göre kişinin kendinde bulunmayan iyilik ve saygınlığı varmış gibi gösterip bunlarla övünmesidir; başka açıklamalar seçkinlere yetişmek için mal biriktirmeyi ya da kınanan çok yeme davranışını öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başlıca yorum, kişide bulunmayan iyilik ve saygınlığı varmış gibi göstererek bunlarla övünmesidir."},{"facet_id":"F002","role":"source_variant","statement":"İkinci yorum, seçkin ve saygın kişilerin düzeyine erişmek amacıyla mal biriktirmedir."},{"facet_id":"F003","role":"source_variant","statement":"Bir başka bağlamlandırma, çok yeme ve bunun kınanmasıyla bağlantı kurar."}],"identity_rationale":"Tek kaynak, aynı kullanım için kendinde bulunmayan iyilik ve saygınlıkla övünme, seçkinlere yetişmek amacıyla mal biriktirme ve çok yeme bağlamı olmak üzere birden çok açıklama verir. Dal korunabilir, ancak bu açıklamalar tek bir kesin anlammış gibi birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kendilerinde bulunmayan iyilik ve saygınlıkla övünmek ya da seçkinlere yetişmek için mal biriktirmek"}],"lexicalization_note":"Anlam yalnızca kanıtlanan çoğul eylem biçiminde geçerlidir; kökün yalın şişmanlık anlamına ya da bütün övünme ve servet biriktirme eylemlerine genellenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel asılsız iddia, karşılıksız gösteriş ve gerçek saygınlık dayanakları, ana yorumun sınırını en iyi açıklayan üç ilişkidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal övünme ve toplumsal saygınlık alanına bağlıdır; komşu dalın yalan ya da geçersiz iddia kapsamı daha geneldir.","focus_only":"Odak dal özellikle kişide bulunmayan iyilik ve saygınlığı kendine mal ederek övünmeyi bildirir.","gloss":"asılsız iddiada bulunma","neighbor_only":"Komşu dal gerçek dışı bir şeyi ileri sürmeyi ve doğru olmayan söz söylemeyi genel olarak kapsar.","neighbor_ref":"root_000127/B003","relation_type":"near_synonym","shared_zone":"Her iki dal gerçekte bulunmayan bir niteliğin ya da durumun varlığını ileri sürer."},{"boundary_match":"partial","distinction":"Odak dal kişinin toplumsal öz sunumuna bağlıdır; komşu dal insan davranışı dışındaki aldatıcı belirtilere de uzanır.","focus_only":"Odak dal kişinin kendinde olmayan erdem ve saygınlıkla övünmesini öne çıkarır.","gloss":"karşılığı olmayan gösteriş","neighbor_only":"Komşu dal karşılığı bulunmayan herhangi bir işaret, vaat ya da görüntüyü de kapsar.","neighbor_ref":"root_000108/B004","relation_type":"near_synonym","shared_zone":"İki dal da dışarıya sunulan görünüş ile gerçek durum arasındaki uyumsuzluğu içerir."},{"boundary_match":"partial","distinction":"Komşu dal gerçek dayanakları adlandırır; odak dal bu dayanaklar bulunmadığı hâlde onları kendine mal etme davranışıdır.","focus_only":"Odak dal iyilik ve saygınlığın gerçekte bulunmadığı hâlde sahiplenilmesini bildirir.","gloss":"gerçek saygınlık ve övünç değerleri","neighbor_only":"Komşu dal gerçekten var olan soy saygınlığı, erdemler, varlık ve övünç kaynaklarını adlandırır.","neighbor_ref":"root_000318/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal kişinin saygınlık ve övünç iddiasında dayandığı niteliklerle ilgilidir."}],"source_phrase_ar":"يتسمنون أي يتكثرون بما ليس فيهم من الخير ويدعون ما ليس لهم من الشرف (tahdhib)؛ وقيل معناه جمعهم المال ليلحقوا بذوي الشرف (tahdhib)؛ باب كثرة الأكل وما يذم منه (tahdhib)","source_qualifications":[{"kind":"disagreement","summary":"Tek kaynaktaki açıklamalar, asılsız iyilik ve saygınlık iddiası, seçkinlere yetişmek için mal biriktirme ve çok yeme bağlamı arasında ayrılır."}],"source_summary":"Çoklu kaynak ortaklığı yoktur; tek kaynak aynı biçimi asılsız üstünlük gösterisi, toplumsal yükselme amaçlı servet biriktirme ve kınanan çok yeme üzerinden alternatif biçimlerde açıklar.","sources":["TA"],"what_is_ar":"يدخل فيه يتسمنون بمعنى يتكثرون بما ليس فيهم من الخير ويدعون ما ليس لهم من الشرف أو يجمعون المال ليلحقوا بذوي الشرف","what_is_not_ar":"لا يدخل فيه السِّمَن الحقيقي إلا على قول من جعله في باب كثرة الأكل"},"support_links":["sup_608eab685989d1373326"]},{"boundary":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B001","candidate_links":[{"candidate_id":"cand_ddb2d7736cab346a83e6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi varlık ile ihtiyaç duymama çekirdeğini birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_image_ar":"الغنى والاستغناء","concept_gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","contextual_glosses":[{"applicability":"Bağlam yalnızca para, mal ve maddi bolluk durumunu öne çıkardığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ile bir şey sayesinde yetinme ilişkisini tek başına açıkça vermez.","preserves":"Maddi varlık ve bolluk yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"zenginlik","usage_role":"contextual"},{"applicability":"Kişinin bir şeye ihtiyaç duymaması veya elindekiyle yetinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi servet ve çok sayıda mala sahip olma yönünü zorunlu olarak taşımaz.","preserves":"İhtiyaçtan bağımsızlık ve bir şeyle yetinme yönünü korur."},"facet_ids":["F002","F003"],"text":"kendine yetmek","usage_role":"contextual"}],"definition":"Maddi varlığa ve bolluğa sahip olma, ihtiyaç duymama ya da az ihtiyaç duyma durumudur. Bağıntılı kullanımlarda kişi bir şey sayesinde yetinir veya başka bir şeye gerek duymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."},{"facet_id":"F002","role":"core","statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ve bir şeyle yetinme yönlerini karşılamaz.","preserves":"Maddi mala ve bolluğa sahip olma yönünü korur."},"text":"varlıklılık"},{"category":"confusable","error_profile":{"adds":"Bir şeyin başkası için yeterli olma işlevini çağrıştırır.","collision":"Başkası için yeterli olma dalıyla karışır.","fit":"displacement","loses":"Maddi bolluk ve kişinin ihtiyaçtan bağımsız olma durumunu silikleştirir.","preserves":"İhtiyacın karşılanmış olmasıyla ilgili sınırlı bir yakınlığı korur."},"text":"yeterlilik"}],"identity_rationale":"Kaynak sözü, maddi varlık ve bolluğun yanı sıra ihtiyaç duymama ya da az ihtiyaç duyma durumunu açıkça birlikte verir. Bir şey sayesinde yetinme ve bir şeye gerek duymama anlatımları da bu çekirdeğin bağıntılı kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"maddi zenginlik, bolluk ve ihtiyaçsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"varlıklı, zengin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona ihtiyaç duymamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onunla yetinip başka bir şeye ihtiyaç duymamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye ihtiyaç duymama durumu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"zenginlik ve bolluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gönül tokluğu ve az şeye ihtiyaç duyma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zengin etmek veya yoksunluğunu gidermek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"Kur'an'la yetinip başka bir şeye ihtiyaç duymamak"}],"lexicalization_note":"Yalın biçimler maddi bolluk ve ihtiyaçsızlık durumunu adlandırırken bağıntılı yapılar bir şeyle yetinmeyi veya bir şeye gerek duymamayı belirtir; bu iki kapsam tanımda ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; maddi bolluk, yeterlik ve sonradan zenginleşme sınırlarını en açık gösteren dört karşılaştırma seçildi, yalnızca dar örnek veya uzak alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir sahibin varlık ve ihtiyaçsızlık durumunu anlatır; komşu dal ise bir unsurun başka biri için yeterli olma ve onun işini görme ilişkisini anlatır.","focus_only":"Kişinin maddi bolluğu ve kendisinin ihtiyaçtan bağımsız oluşu bu dala özgüdür.","gloss":"kendine yeterlik ve başkasına yetme","neighbor_only":"Bir şeyin veya kişinin başkası için yeterli olması, yarar sağlaması ve onun yerini tutması komşuya özgüdür.","neighbor_ref":"root_001110/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir ihtiyacın ortadan kalkması veya karşılanması çevresinde buluşur."},{"boundary_match":"partial","distinction":"Komşu dal genişlik ve refahı öne çıkarırken odak dal bunu ihtiyaçların yokluğu veya azalması ve bağımsızlıkla daha sıkı bağlar.","focus_only":"Az ihtiyaç duyma, çok mala sahip olma ve bir şeyle yetinme bağıntıları odakta açıkça yer alır.","gloss":"bolluk ve refah","neighbor_only":"Genel genişlik ve ferahlık anlatımı komşu dalda daha belirgindir.","neighbor_ref":"root_001694/B003","relation_type":"near_synonym","shared_zone":"İki dal da maddi genişlik, refah ve yoksunluktan çıkma durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal zenginliği ihtiyaçtan bağımsızlıkla tanımlar; komşu dal ise birikmiş malın veya başka şeylerin çokluğuna kadar genişleyebilir.","focus_only":"İhtiyaç duymama veya bir şeyle yetinme odak dalın kurucu sınırıdır.","gloss":"zenginlik ve mal çokluğu","neighbor_only":"Her tür çokluk ve malı iyi yönetme anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000459/B001","relation_type":"near_synonym","shared_zone":"Her iki dal maddi varlığın çokluğunu ve zenginliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel ve sürebilen bir zenginlik durumudur; komşu dal aynı sonucu özellikle önceki yoksulluktan sonraki değişim olarak sınırlar.","focus_only":"Öncesinde yoksulluk bulunması gerekmeksizin varlıklı ve ihtiyaçsız olmayı kapsar.","gloss":"zenginlik ve sonradan zenginleşme","neighbor_only":"Yoksulluktan sonra zenginleşme geçişi komşu dalın zorunlu koşuludur.","neighbor_ref":"root_000406/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin zengin duruma gelmesini veya zengin olmasını içerir."}],"source_phrase_ar":"الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)","source_summary":"Kaynakların ortak çerçevesi maddi zenginliği, bolluğu ve ihtiyaçların yokluğunu ya da azalmasını bir araya getirir; ayrıca bir şeyle yetinip başkasına ihtiyaç duymama kullanımını destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغنى في المال والوفر وعدم الحاجة أو قلتها وكثرة القنيات والاستغناء بالشيء أو عنه وتغنى وتغانى بمعنى استغنى","what_is_not_ar":"ليس إجزاء الشيء عن غيره ولا الغناء بالصوت ولا المقام بالمكان"},"support_links":["sup_608eab685989d1373326"]},{"boundary":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_3e86a0948c7a25692d1e","lane":"micro"},{"candidate_id":"cand_7a78400a7dfe63137f2e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir unsurun başkası için hem yeterli hem yararlı olması ve gerektiğinde başka bir unsurun işlevini üstlenmesi için kullanılır.","boundary_detail":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_image_ar":"الغَناء والكفاية","concept_gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","contextual_glosses":[{"applicability":"Bir şeyin miktar veya işlev bakımından ihtiyacı karşılaması öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarar sağlama ve başka bir unsurun yerini tutma yönlerini açıkça belirtmez.","preserves":"Yeterli olma ve ihtiyacı karşılama çekirdeğini korur."},"facet_ids":["F001"],"text":"yetmek","usage_role":"contextual"},{"applicability":"Bir unsurun beklenen yararı sağlaması veya başka bir unsur yerine kullanılabilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yeterlik ile ihtiyacın bütünüyle karşılanmasını zorunlu olarak anlatmaz.","preserves":"Yarar sağlama ve beklenen işlevi yerine getirme yönünü korur."},"facet_ids":["F002","F003"],"text":"işini görmek","usage_role":"contextual"}],"definition":"Bir şeyin ya da kişinin başkası için yeterli olması, onun ihtiyacını karşılaması ve yarar sağlamasıdır; bağlama göre başka bir unsurun işini görüp onun yerini de tutabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."},{"facet_id":"F002","role":"core","statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."},{"facet_id":"F003","role":"extension","statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeterli olma, ihtiyacı karşılama ve başkasının yerini tutma ilişkilerini vermez.","preserves":"Olumlu sonuç ve işe yarama yönünü korur."},"text":"yarar"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel değiştirme ve takas alanıyla karışabilir.","fit":"narrowing","loses":"Yer değiştirme bulunmayan yeterlik ve yarar kullanımlarını dışarıda bırakır.","preserves":"Bir unsurun başka bir unsurun işlevini üstlenmesi yönünü korur."},"text":"yerine geçme"}],"identity_rationale":"Kaynak sözü, bir şeyin ya da kişinin başkası için yeterli olmasını, ihtiyacı karşılamasını, yarar sağlamasını ve gerektiğinde başka bir unsurun yerini tutmasını birlikte verir. Bu nedenle dalın çekirdeği, sahibin zenginliği değil, iki katılımcı arasındaki yeterlik ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yeterlilik, ihtiyacı karşılama ve yarar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu sana yetmez ve yarar sağlamaz"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yeterli ve ihtiyacı karşılayan"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin yerini tutan yeterlilik ve işlev"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"zararını benden uzak tut"}],"lexicalization_note":"Yalın biçimler yeterlik ve yararı adlandırır; bağıntılı yapılar kimin için yeterli olunduğunu, neyin yerini tuttuğunu veya hangi zararın uzak tutulduğunu açıklar.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik, bir şeyle yetinme, başkası adına iş görme ve gerçek değiştirme arasındaki sınırları gösteren dört aday seçildi, daha uzak alan ortaklıkları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir unsurun başkası için yeterli ve yararlı oluşuna dayanır; komşu dal ise işi üstlenip sürdürerek açığı kapatma ve sonuca ulaştırma sürecini öne çıkarır.","focus_only":"Yarar sağlama ve bir kişi ya da şeyin yerini tutma ilişkileri odakta açıkça bulunur.","gloss":"yetme ve işi tamamlayarak yetme","neighbor_only":"Bir işi yürütüp açığı kapatarak amaca ulaşma süreci komşu dalda daha belirgindir.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir ihtiyacın karşılanması ve yeterli sonucun elde edilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel yeterlik ve yararı da içerir; komşu dal yerini tutma ve özellikle bir yükümlülüğü başkası adına yerine getirme ilişkisine daha sıkı bağlıdır.","focus_only":"Bir şeyin yalnızca yeterli veya yararlı olması, yer değiştirme gerçekleşmeden de bu dala girebilir.","gloss":"yetme ve başkasının yerine ödeme","neighbor_only":"Hak, borç veya bağış gibi yükümlülükleri başkası adına yerine getirme komşu dalın ek alanıdır.","neighbor_ref":"root_000244/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir unsurun başka birinin yerini tutup onun adına yeterli olmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yeterli unsur ile yararlanan katılımcı arasındaki ilişkiyi kurar; komşu dal eldeki şeyle yetinme ve başkasından vazgeçebilme sonucunu öne çıkarır.","focus_only":"Bir kişinin ya da şeyin başkası için yararlı ve yeterli olup onun yerini tutması odakta belirgindir.","gloss":"ihtiyacı karşılama ve bir şeyle yetinme","neighbor_only":"Bir şeyle yetinip başka bir şeye gerek duymama sonucu komşu dalda çekirdeğe daha yakındır.","neighbor_ref":"root_000241/B001","relation_type":"near_synonym","shared_zone":"Her iki dal, eldeki bir unsurun ihtiyacı karşılayarak başka bir gereği ortadan kaldırmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal işlev bakımından yetmeyi anlatır; komşu dal ise bir unsurun yerine diğerini koyma veya onları değiştirme işlemini anlatır.","focus_only":"Yeterli olma ve yarar sağlama, gerçek bir değiştirme işlemi olmadan da gerçekleşebilir.","gloss":"işlevsel yeterlik ve değiştirme","neighbor_only":"Bir unsurun çıkarılıp yerine başka bir unsurun konması ve karşılıklı değiştirme komşu dala özgüdür.","neighbor_ref":"root_000095/B001","relation_type":"near_neighbor","shared_zone":"Bir unsurun başka bir unsurun konumunu veya işlevini üstlenmesi iki dalda da görülebilir."}],"source_phrase_ar":"الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)","source_summary":"Kaynaklar yeterli olma, ihtiyacı karşılama, yarar sağlama ve başkasının yerini tutma yönlerinde birleşir; olumsuz yapılarda aynı ilişki yetersizlik veya yararsızlık olarak görünür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يكفي الشيء أو الشخص غيره ويجزئ عنه وينفعه ويقوم مقامه","what_is_not_ar":"ليس اليسار والوفر ولا الغناء بالصوت ولا سكنى المكان"},"support_links":["sup_4115f3d79c0e6aca9aa1","sup_a4cff254ebf451c7f80b"]},{"boundary":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ses üretme, dinleme ve özel metin okuma yönlerini birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_image_ar":"الغِناء والصوت","concept_gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","contextual_glosses":[{"applicability":"İnsan sesiyle ezgili bir parça seslendirme eylemi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinleme ile metni hüzünlü ve yumuşak sesle okuma yönlerini dışarıda bırakır.","preserves":"Sesle ezgi üretme ve ezgili parça yönlerini korur."},"facet_ids":["F001","F002"],"text":"şarkı söylemek","usage_role":"contextual"},{"applicability":"Bir metnin sesi yumuşatıp duygulandırarak ezgili biçimde okunması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel şarkı söyleme, ezgili parça ve dinleme alanlarını kapsamaz.","preserves":"Okuyuşta ezgi, hüzün ve ses yumuşaklığı yönünü korur."},"facet_ids":["F003"],"text":"ezgili okumak","usage_role":"contextual"}],"definition":"Sesle ezgi söyleme, söylenen ezgili parça ve bunu dinleme alanıdır. Okuyuşu ezgili, hüzünlü ve yumuşak bir sesle gerçekleştirme bunun özel bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."},{"facet_id":"F003","role":"specialization","statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İnsan sesi bulunmayan çalgısal üretim ve düzenleme alanlarını da kapsar.","collision":"Çalgı müziğiyle gereksiz bir kapsam çakışması doğurur.","fit":"broadening","loses":null,"preserves":"Ezgi ve işitsel sanat alanıyla olan bağı korur."},"text":"müzik"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söyleme ve dinleme etkinliğiyle özel ezgili okuma kullanımını tek başına karşılamaz.","preserves":"Ezgili söylenen parça yönünü güçlü biçimde korur."},"text":"şarkı"}],"identity_rationale":"Kaynak sözü sesle ezgi söylemeyi, söylenen ezgili parçayı ve dinlemeyi açıkça bu dalda toplar. Okuyuşu ezgili, hüzünlü ve yumuşak seslendirme ise aynı ses kullanımının özel bir uygulamasıdır, dalın bütününü tek başına tanımlamaz.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarkı söyleme, ezgili seslendirme ve dinleti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"şarkı; ezgili söylenen parça"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"şarkı söylemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"şarkı söylemek veya sesi ezgili ve duygulu kullanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak"}],"lexicalization_note":"Yalın biçimler şarkı söyleme, ezgili parça ve dinletiyi adlandırır; belirli metni ezgili okuma anlamı yalnızca ilgili bağıntılı yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hoş insan sesi, özel yolcu ezgisi, ses yineleme ve çalgı sesiyle sınırı en iyi gösteren dört aday seçildi, yalnızca yüksek ses veya uzak konu ortaklığı sunanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şarkı söyleme, parça, dinleme ve özel okuma kullanımını toplar; komşu dal özellikle hoş işitilen ses niteliği ve bunu üreten kişiye yönelir.","focus_only":"Ezgili parça ile metni hüzünlü ve yumuşak sesle okuma kullanımı odakta açıkça bulunur.","gloss":"şarkı ve hoş ezgili ses","neighbor_only":"Sesin hoş ve zevk verici niteliği ile icracıyı adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_000741/B007","relation_type":"near_synonym","shared_zone":"İki dal da insan sesiyle üretilen hoş ezgiyi ve şarkı söylemeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal geniş sesli ezgi alanını anlatır; komşu dal bunu yüksek sesli ve yolculukla ilişkili belirli bir söyleyiş türüyle sınırlar.","focus_only":"Genel şarkı söyleme, ezgili parça, dinleme ve yumuşak okuyuş odak dalda yer alır.","gloss":"genel şarkı ve yolcu ezgisi","neighbor_only":"Yolcuların yüksek sesle söylediği çağrı ve belirli ezgi türü komşuya özgüdür.","neighbor_ref":"root_001507/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal insan sesiyle ezgili söyleme etkinliğine girer."},{"boundary_match":"partial","distinction":"Odak dal ezgi üretimi ve dinlemeyi tanımlar; komşu dal sesin yinelenmesi veya geri döndürülmesi biçimine dayanır ve ezgi gerektirmez.","focus_only":"Ezgili parça ve şarkı söyleme etkinliği odak dalın merkezindedir.","gloss":"ezgili söyleme ve ses yineleme","neighbor_only":"Çağrı, gök gürültüsü ve başka seslerde yineleme veya yankılanma komşu dalın ek kapsamıdır.","neighbor_ref":"root_000544/B007","relation_type":"near_neighbor","shared_zone":"Şarkı ve okuma sırasında sesin düzenli biçimde çevrilmesi iki dalda kesişebilir."},{"boundary_match":"field_only","distinction":"Odak dal insan sesi ve şarkıya dayanır; komşu dalın çekirdeği üflemeli çalgıdan çıkan sestir ve insan sesi zorunlu değildir.","focus_only":"İnsan sesiyle şarkı söyleme ve metni ezgili okuma odak dalın çekirdeğidir.","gloss":"insan sesi ve çalgı sesi","neighbor_only":"Üflemeli çalgıyla ses üretme ve aynı sözcüğün bazı hayvan seslerine uygulanması komşuya özgüdür.","neighbor_ref":"root_000643/B002","relation_type":"same_field","shared_zone":"İki dal ezgili veya hoş işitilebilen ses üretimi alanında buluşur."}],"source_phrase_ar":"الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)","source_summary":"Kaynaklar insan sesiyle ezgi söyleme, ezgili parça ve dinleme anlamlarında birleşir; ayrıca okuyuştaki ezgili, hüzünlü ve yumuşak seslendirmeyi özel bir kullanım olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغناء بالصوت والأغنية والسماع والتطريب وتحزين القراءة وترقيقها","what_is_not_ar":"ليس الغنى في المال ولا الغَناء بمعنى الكفاية ولا المقام بالمكان"},"support_links":[]},{"boundary":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"bir yerde uzun süre kalıp yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, süre ve yaşama katılımlarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_image_ar":"الغنى بالمكان","concept_gloss":"bir yerde uzun süre kalıp yaşama","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun belirli bir yeri yaşama yeri edinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süre kalma vurgusunu ve bundan doğan yer adlarını açıkça vermez.","preserves":"Belirli bir yerde yaşama ve yerle bağ kurma yönünü korur."},"facet_ids":["F001"],"text":"bir yerde oturmak","usage_role":"contextual"},{"applicability":"Kalınan yer ile kalış süresinin öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Orada yaşama ile ev veya yer adı türetme yönlerini zorunlu olarak taşımaz.","preserves":"Belirli yerde kalma ve süreklilik yönünü korur."},"facet_ids":["F001"],"text":"uzun süre kalmak","usage_role":"contextual"},{"applicability":"Geçmişte bir yerde bulunmuş ve yaşamış olmanın sonradan yokluğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel uzun süre kalma çekirdeği ile konut ve eylem adlarını kapsamaz.","preserves":"Geçmişte o yerde yaşama veya bulunma yönünü korur."},"facet_ids":["F002"],"text":"orada yaşamış olmak","usage_role":"contextual"}],"definition":"Bir yerde oturmak, orada uzun süre kalmak ve yaşamak anlamıdır. Geçmişte orada bulunmuş olma anlatımı ile bir topluluğun oturduğu evleri, kalma eylemini veya kalınan yeri bildiren adlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süreli oturma, yaşama ve o yerin ev sayılması yönlerini zayıflatır.","preserves":"Belirli bir yerde kalma yönünü korur."},"text":"konaklamak"},{"category":"alternative","error_profile":{"adds":"Başlangıçtaki taşınma ve kalıcı düzen kurma olayını öne çıkarır.","collision":"Yer edinme eylemiyle kalış durumunu birbirine yaklaştırır.","fit":"displacement","loses":"Geçmişte bulunmuş olma ve yalnızca uzun süre kalma kullanımlarını daraltır.","preserves":"Bir yeri yaşama yeri edinme yönünü korur."},"text":"yerleşmek"}],"identity_rationale":"Kaynak sözü bir yerde oturup uzun süre kalmayı çekirdek olarak verir; orada yaşamış veya bulunmuş olma anlatımı ile oturulan ev ve yer adları bu çekirdekten doğan kullanımlardır. Bu nedenle geçici bulunma ile konut adı aynı düzeyde tek anlam sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturmak ve uzun süre kalmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sanki daha dün orada hiç yaşamamıştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir topluluğun oturduğu evler ve yurtlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturma eylemi veya oturulan yer"}],"lexicalization_note":"Bir yerde uzun kalma ve geçmişte orada yaşama anlamları belirli bağıntılı yapılarda görünür; yalın ad biçimleri ise kalma eylemini veya oturulan yeri gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; uzun kalış, genel kalma, konut edinme ve oturma duruşu arasındaki sınırı gösteren beş aday seçildi, yalnızca yer adı veya uzaktan alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama, geçmişte bulunma ve konut adlarına uzanır; komşu dal ise yerleşik kalmayı farklı kişi durumlarına ve özel kalış bağlamlarına genişletir.","focus_only":"Topluluğun evleri ile kalma eylemini veya yerini adlandıran biçimler odakta bulunur.","gloss":"uzun süre yaşama ve yerleşik kalma","neighbor_only":"Yabancının kalışı, kutsal yerde komşuluk, hapiste kalma ve öldürülmüş kişi kullanımları komşuya özgüdür.","neighbor_ref":"root_000211/B001","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir yerde oturma, kalma ve özellikle uzun süren yerleşikliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal uzun yaşama ile bundan doğan ev ve yer adlarını toplar; komşu dal aynı alanı durma, bekleme ve soyut yerleşiklik kullanımlarına taşır.","focus_only":"Geçmişte orada yaşamış olma ve topluluğun evlerini adlandırma odakta belirgindir.","gloss":"oturma ve yerleşik kalma","neighbor_only":"Durma, ağırdan alma ve eskiden beri yerleşmiş bir iş anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000536/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir yerde oturma, ev ve yerleşik kalma alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreyi, yaşamayı ve bağlı yer adlarını içerir; komşu dal ise süre veya konut sonucu belirtmeden bir yerde kalma eylemiyle sınırlıdır.","focus_only":"Uzun süre yaşama, geçmişte bulunma ve oturulan evleri adlandırma odakta yer alır.","gloss":"uzun süre yaşama ve bir yerde kalma","neighbor_only":"Komşu dal yalnızca bir yerde kalmayı bildiren daha dar bir eylem çerçevesidir.","neighbor_ref":"root_000168/B016","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin belirli bir yerde kalmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sürmekte olan kalış ve yaşam durumunu anlatır; komşu dal ise yeri konut seçme ya da başkasına konut sağlama işlemini öne çıkarır.","focus_only":"Bir yerde fiilen uzun süre yaşama ve geçmişte orada bulunmuş olma odak dalın merkezidir.","gloss":"orada yaşama ve konut edinme","neighbor_only":"Bir yeri konut edinme veya birini bir yere yerleştirme işlemi komşu dalda belirgindir.","neighbor_ref":"root_000162/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişi ile yaşadığı yer arasında kalıcı veya uzun süreli bir bağ kurar."},{"boundary_match":"partial","distinction":"Odak dal yaşama yeri ve uzun kalışla ilgilidir; komşu dal bedenin oturma duruşunu ve bu duruş çevresindeki birlikteliği anlatır.","focus_only":"Yerde uzun süre yaşama ve o yeri konut edinme odak dala özgüdür.","gloss":"bir yerde yaşama ve oturma duruşu","neighbor_only":"İnsan bedeninin oturma duruşu, oturum ve birlikte oturma komşu dalın çekirdeğidir.","neighbor_ref":"root_000254/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda kişi bir yerde bulunur ve o yere bağlı bir süreklilik gösterebilir."}],"source_phrase_ar":"غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)","source_summary":"Kaynaklar bir yerde oturma ve uzun süre kalma çekirdeğinde birleşir; geçmişte orada yaşama anlatımını, topluluğun evlerini ve hem eylemi hem yeri gösterebilen adları da bu alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإقامة وطول المقام في الدار أو المحلة والمغاني منازل القوم والمغنى للمصدر أو المكان وما يقرب من العيش والكون السابق","what_is_not_ar":"ليس الغنى في المال ولا الكفاية ولا الغناء بالصوت"},"support_links":[]},{"boundary":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_kind":"bare","branch_ref":"root_001110/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana açıklama ile kaynaklarda görülen daha geniş kadın nitelemelerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_image_ar":"الغانية المستغنية","concept_gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","contextual_glosses":[{"applicability":"Nitelemenin kadının kendi güzelliği sayesinde süslenmeye gerek duymaması açıklamasına dayandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde bağımsızlık ile yalnız gençlik, evlilik veya genel kadın kullanımını dışarıda bırakır.","preserves":"Güzellik nedeniyle süsten bağımsız sayılma yönünü açıkça korur."},"facet_ids":["F001"],"text":"güzelliğiyle süse ihtiyaç duymayan kadın","usage_role":"explanatory"},{"applicability":"Kaynak sınırının gençlik ve güzellik özelliklerine dayandığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş veya güzellik sayesinde süsten bağımsız olma açıklamasını ve genel kadın kullanımını vermez.","preserves":"Gençlik ve güzellik temelli kaynak çeşidini korur."},"facet_ids":["F002"],"text":"genç ve güzel kadın","usage_role":"contextual"},{"applicability":"Nitelemenin yalnızca evlilik durumuna göre sınırlandığı kaynak kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güzellik, gençlik, süsten bağımsızlık ve evli olmayan kadın kullanımlarını dışarıda bırakır.","preserves":"Evlilik koşuluna dayanan dar kaynak çeşidini korur."},"facet_ids":["F002"],"text":"evli kadın","usage_role":"contextual"}],"definition":"Eşi sayesinde takıya gerek duymadığı veya güzelliği nedeniyle süslenmeye ihtiyaç duymadığı düşünülen kadını anlatan bir nitelemedir. Kullanım sınırı bazı kaynaklarda genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın olacak kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."},{"facet_id":"F003","role":"source_variant","statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde süsten bağımsızlık, evlilik, gençlik ve koşulsuz kadın kullanımlarını dışarıda bırakır.","preserves":"Güzellik özelliğine dayanan kullanımı korur."},"text":"güzel kadın"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evli olmayan güzel kadın, süsten bağımsız kadın ve genel kadın kullanımlarını kapsamaz.","preserves":"Gençlik ile evliliği birlikte arayan dar kaynak çeşidini korur."},"text":"evli genç kadın"}],"identity_rationale":"Kaynak sözü, eşi veya güzelliği sayesinde takı ve süslenmeye ihtiyaç duymadığı düşünülen kadın açıklamasını güçlü biçimde destekler; ancak bütün tanımlar bu sınırı korumaz. Bazı kullanımlar genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın düzeyine kadar genişler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar"}],"lexicalization_note":"Tanım yalın kadın nitelemesine bağlıdır; eşi, güzelliği, gençliği veya evliliği anlatan sınır çeşitleri korunur ve başka dallardaki evlenme olayına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ihtiyaçsızlık, genç ve güzel kadın, süs eşyası ve evlilik durumu ile sınırı gösteren dört aday seçildi, yalnızca aynı toplumsal sahneyi paylaşan daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli ve sınırları değişken bir kadın adıdır; komşu dal ise cinsiyet veya niteleme sınırlaması olmadan zenginlik ve ihtiyaçsızlık durumunu anlatır.","focus_only":"Belirli bir kadın nitelemesi ve bunun gençlik, güzellik veya evlilik sınırları odak dala özgüdür.","gloss":"kadın nitelemesi ve genel ihtiyaçsızlık","neighbor_only":"Genel maddi bolluk, mal çokluğu ve herhangi bir kişinin ihtiyaçtan bağımsızlığı komşu dalın kapsamıdır.","neighbor_ref":"root_001110/B001","relation_type":"near_neighbor","shared_zone":"Kadının eşi veya güzelliği sayesinde süse ihtiyaç duymadığı açıklaması, ihtiyaçtan bağımsızlık düşüncesiyle kesişir."},{"boundary_match":"partial","distinction":"Odak dalın ana açıklaması eş veya güzellik sayesinde süsten bağımsızlıktır ve sınırı değişkendir; komşu dal doğrudan gençlik ve güzelliği bildirir.","focus_only":"Eş veya güzellik sayesinde süse ihtiyaç duymama ve evlilik sınırı odakta bulunabilir.","gloss":"süsten bağımsız kadın ve genç güzel kız","neighbor_only":"Genç ve güzel kız olma, başka bir gerekçe aranmadan komşu dalın doğrudan çekirdeğidir.","neighbor_ref":"root_000610/B008","relation_type":"near_neighbor","shared_zone":"İki dal da genç ve güzel bir kadını nitelemek için kullanılabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal bir kadını süse gerek duymama veya başka özelliklerle niteler; komşu dal ise süs eşyasını ve süslenme eylemini anlatır.","focus_only":"Süse ihtiyaç duymadığı düşünülen kadının kendisi odak dalda adlandırılır.","gloss":"süsten bağımsız kadın ve süs eşyası","neighbor_only":"Takı ve süs eşyasının kendisi ile bunları takma eylemi komşu dalda adlandırılır.","neighbor_ref":"root_000353/B001","relation_type":"thematic","shared_zone":"Her iki dal kadın, takı ve süslenme durumunun aynı sahnesinde yer alır."},{"boundary_match":"field_only","distinction":"Odakta evlilik yalnızca değişken sınırlardan biridir; komşu dal ise önceki evlilik veya birleşme sonrasındaki medeni durumu doğrudan tanımlar.","focus_only":"Güzellik, gençlik veya eş sayesinde süsten bağımsızlıkla kurulan kadın nitelemesi odakta yer alır.","gloss":"kadın nitelemesi ve önceki evlilik durumu","neighbor_only":"Evlilik ilişkisinin sona ermesi ya da evlilikte cinsel birleşme sonrası kazanılan durum komşuya özgüdür.","neighbor_ref":"root_000209/B005","relation_type":"same_field","shared_zone":"Her iki dal bir kadını evlilik durumu üzerinden niteleyebilir."}],"source_phrase_ar":"الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)","source_summary":"Kaynaklar kadın nitelemesinde birleşir, fakat sınırı farklı kurar: eşi veya güzelliği nedeniyle süse ihtiyaç duymama ana açıklamadır; gençlik, güzellik, evlilik ve koşulsuz kadın kullanımları daha geniş çeşitlerdir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغانية والغواني على اختلاف تفسيرها بالمتزوجة أو الشابة أو الحسناء أو من استغنت بزوجها أو حسنها عن الزينة","what_is_not_ar":"ليس الغناء بالصوت ولا مطلق الغنى في المال ولا التزويج نفسه"},"support_links":[]},{"boundary":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_kind":"bare","branch_ref":"root_001110/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","surface_ar":"يُغْنِى"}],"gloss":"evlenme ve evlendirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik bağının kurulmasını hem kişinin kendisi hem de bir başkasını evlendiren katılımcı açısından kapsar.","boundary_detail":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_image_ar":"الغنى والتزويج","concept_gloss":"evlenme ve evlendirme","contextual_glosses":[{"applicability":"Kişinin evlenmesi veya evlilik durumuna girmesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını evlendirme ve evliliği koruyucu sayma yönlerini dışarıda bırakır.","preserves":"Kişinin evlenmesi ve evlilik bağının kurulması yönünü korur."},"facet_ids":["F001"],"text":"evlilik bağı kurmak","usage_role":"contextual"},{"applicability":"Ettirgen kullanımda bir gelin için evlilik bağı kurulması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi evlenmesini ve evliliğin koruyucu sayılmasını kapsamaz.","preserves":"Bir başkasını, özellikle gelini, evlendirme yönünü korur."},"facet_ids":["F002"],"text":"bir gelini evlendirmek","usage_role":"contextual"}],"definition":"Evlilik bağı kurma veya birini, özellikle bir gelini, evlendirme anlamıdır. Evlilik ayrıca bekâr kişiyi koruyan bir güvence olarak tasarlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."},{"facet_id":"F003","role":"associated_use","statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kutlama ve tören olayını zorunluymuş gibi öne çıkarır.","collision":"Evlilik bağı ile düğün törenini birbirine karıştırır.","fit":"displacement","loses":"Evlilik bağını kurma ve birini evlendirme işlemlerini hukuki ve ilişkisel yönleriyle vermez.","preserves":"Evlilik çevresindeki toplumsal olaya gönderme yapar."},"text":"düğün"}],"identity_rationale":"Kaynak sözü evlenmeyi, gelinleri evlendirmeyi ve evliliğin bekâr kişi için koruyucu bir durum sayılmasını aynı dalda açıkça verir. Kadın nitelemesi, maddi zenginlik ve sesle ezgi anlamları bu çekirdeğin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"evlenme; bekâr kişi için koruyucu sayılan evlilik"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gelinleri evlendirme"}],"lexicalization_note":"Tanım yalın ad ve ettirgen biçimlerin evlenme ile evlendirme anlamlarını kapsar; düğün töreni, eşin kendisi veya evliliğin sonraki aşamaları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; evlilik sözleşmesi, eş edinme, birlikte yaşama aşaması, örtülü evlilik anlatımı ve kadın nitelemesiyle sınırı gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal evlenme ile başkasını evlendirmeyi birlikte kapsar; komşu dal özellikle evlilik sözleşmesini ve bu sözleşmeyle evlenmeyi öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği bekâr için koruyucu sayma yönleri odakta bulunur.","gloss":"evlenme ve evlilik sözleşmesi","neighbor_only":"Evlilik sözleşmesinin kendisini doğrudan adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_001548/B002","relation_type":"near_synonym","shared_zone":"Her iki dal evlilik bağının kurulmasını ve kişinin evlenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal evlilik bağını kurma ve kurdurma olayını anlatır; komşu dal eş ve aile edinme sonucunu öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği koruyucu bir güvence sayma odak dala özgüdür.","gloss":"evlenme ve eş edinme","neighbor_only":"Eş edinerek aile sahibi olma ve kişiye bir eş verilmesi komşu dalda daha belirgindir.","neighbor_ref":"root_000064/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin evlenerek bir eş ve aile bağı edinmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bağın kurulmasını anlatır; komşu dal ise kurulmuş evliliğin ardından eşlerin bir araya gelmesi ve ortak yaşama geçmesi aşamasına yönelir.","focus_only":"Evlilik bağını kurma ve bir başkasını evlendirme odak dalın çekirdeğidir.","gloss":"evlenme ve eşlerin birleşmesi","neighbor_only":"Evliliğin ardından eşlerin birlikte yaşamaya başlaması ve gelinin eve getirilmesi komşuya özgüdür.","neighbor_ref":"root_000156/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal evlilik sürecinin birbirine yakın aşamalarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan evlenme ve evlendirme anlamındadır; komşu dal örtülü bir anlatımla evlilikten cinsel birleşmeye kadar genişleyebilir.","focus_only":"Bir başkasını evlendirme ve koruyucu evlilik düşüncesi odak dalda açıkça yer alır.","gloss":"evlilik bağı ve evlilik için örtülü anlatım","neighbor_only":"Evlilik yanında cinsel birleşmeye kadar uzanan örtülü kullanım komşu dalın ek kapsamıdır.","neighbor_ref":"root_000161/B005","relation_type":"near_neighbor","shared_zone":"İki dal da evlenme anlamını veya evliliğe gönderme yapan bir kullanımı kapsar."},{"boundary_match":"field_only","distinction":"Odak dal bir olay ve ilişki kurma sürecidir; komşu dal ise evli olabilen veya başka özelliklerle tanımlanan bir kadın adıdır.","focus_only":"Evlilik bağını kurma veya birini evlendirme olayı odak dala özgüdür.","gloss":"evlenme olayı ve kadın nitelemesi","neighbor_only":"Evlilik, güzellik veya gençlik üzerinden tanımlanan kadın nitelemesi komşu dala özgüdür.","neighbor_ref":"root_001110/B005","relation_type":"same_field","shared_zone":"Her iki dal evlilik ve kadınla ilgili aynı toplumsal alan içinde yer alabilir."}],"source_phrase_ar":"الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kullanım, evlenmeyi ve gelinleri evlendirmeyi anlatır; evliliği de bekâr kişi için koruyucu bir güvence sayar."}],"source_summary":"Bu dalda ad ve ettirgen biçim, evlilik bağı kurma çevresinde birleşir; koruma düşüncesi evlenmenin sonucu olarak sunulur.","sources":["TA"],"what_is_ar":"يدخل فيه الغنى بمعنى التزويج والأغناء بمعنى إملاكات العرائس وجعل التزويج حصنا للعزب","what_is_not_ar":"ليس الغانية نفسها ولا الغناء بالصوت ولا الغنى في المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:7:1"],"branch_refs":[],"candidate_id":"cand_cc21272b0a6a00dce322","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:1:audible-and-boundary-weight","source_type":"word_analysis","support_ids":["sup_05b0c6a655f483cdf635","sup_419000ac1a90f0342a04"],"title":"weighted refusal after food naming","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:1","qac_refs":["88:7:1:1"],"status":"accepted"}},{"anchor_refs":["88:7:1"],"branch_refs":[],"candidate_id":"cand_fb7d64686c2c452f277b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:1:opening-local-negation","source_type":"word_analysis","support_ids":["sup_05b0c6a655f483cdf635","sup_f5c1ce34895e1e9b6101"],"title":"first predicate denied as fact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:1","qac_refs":["88:7:1:1"],"status":"accepted"}},{"anchor_refs":["88:7:1"],"branch_refs":[],"candidate_id":"cand_ea47bbe2330daa21684d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:1:paired-negation-frame","source_type":"word_analysis","support_ids":["sup_05b0c6a655f483cdf635","sup_12ec4a3d131ad9f7e9d0"],"title":"first beat of twofold denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:1","qac_refs":["88:7:1:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_b1eebd850e326e9238e0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:bodily-reserve-root-image","source_type":"word_analysis","support_ids":["sup_380d9b40a417f4b642d6","sup_8953a580aa2590ae175b"],"title":"fatness field narrowed to nutritive reserve","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_ada22271052a5e12aeac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:implicit-food-subject","source_type":"word_analysis","support_ids":["sup_380d9b40a417f4b642d6","sup_8d816aec9b845621133f"],"title":"subject carried from prior food phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_9a23db4878fed72b0f81","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:objectless-causative-negated","source_type":"word_analysis","support_ids":["sup_380d9b40a417f4b642d6","sup_4bd1ba9ee0a0c02de377"],"title":"objectless causative nourishment denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_1a90d135f39b208ce71b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:paired-effect-sequence","source_type":"word_analysis","support_ids":["sup_0dff004caba88754b2b6","sup_380d9b40a417f4b642d6"],"title":"first concrete effect before sufficiency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_8db840968faf9804db1d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:rare-abundance-contrast","source_type":"word_analysis","support_ids":["sup_380d9b40a417f4b642d6","sup_d69ea32afe425fee8f83"],"title":"rare verbal abundance test","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_1249428f5e19d592d3ed","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:soft-cadence-before-hard-failure","source_type":"word_analysis","support_ids":["sup_380d9b40a417f4b642d6","sup_fd86db2a3f7995e4e2d6"],"title":"smooth verbal cadence still blocked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:2","qac_refs":["88:7:2:1"],"status":"accepted"}},{"anchor_refs":["88:7:3"],"branch_refs":[],"candidate_id":"cand_e392c37a09fcdbea63bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:3:boundary-after-exception","source_type":"word_analysis","support_ids":["sup_5d03b5f8db5febf4ef25","sup_b4234cbe27e5ae910a92"],"title":"available food becomes nonfunctional","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:3","qac_refs":["88:7:3:1"],"status":"accepted"}},{"anchor_refs":["88:7:3"],"branch_refs":[],"candidate_id":"cand_e4e283044aa2eba0caf6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:3:cumulative-coordination","source_type":"word_analysis","support_ids":["sup_2b56f491ce95b9179898","sup_5d03b5f8db5febf4ef25"],"title":"second failure added, not folded in","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:3","qac_refs":["88:7:3:1"],"status":"accepted"}},{"anchor_refs":["88:7:3"],"branch_refs":[],"candidate_id":"cand_87e88f0956826a35311e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:3:segmented-sound-bridge","source_type":"word_analysis","support_ids":["sup_5b1c70b9edb102bd9c6c","sup_5d03b5f8db5febf4ef25"],"title":"separate particle, tight recited bridge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:3","qac_refs":["88:7:3:1"],"status":"accepted"}},{"anchor_refs":["88:7:4"],"branch_refs":[],"candidate_id":"cand_c3fee3a4f38b00d36e4e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:4:independent-second-negation","source_type":"word_analysis","support_ids":["sup_1a71cbc4fb1a6f213406","sup_3ed128583f28eae1e06c"],"title":"sufficiency receives its own denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:4","qac_refs":["88:7:3:2"],"status":"accepted"}},{"anchor_refs":["88:7:4"],"branch_refs":[],"candidate_id":"cand_f198027b76127c08d0f8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:4:neither-nor-symmetry","source_type":"word_analysis","support_ids":["sup_1a71cbc4fb1a6f213406","sup_819ff01220c36367ab86"],"title":"balanced repeated denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:4","qac_refs":["88:7:3:2"],"status":"accepted"}},{"anchor_refs":["88:7:4"],"branch_refs":[],"candidate_id":"cand_f0ce7955addcd77aaeef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:4:particle-cadence","source_type":"word_analysis","support_ids":["sup_1a71cbc4fb1a6f213406","sup_44f4a138699198460c77"],"title":"short stops before hunger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:4","qac_refs":["88:7:3:2"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_35041f25d32380d87316","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:delayed-deficit-escalation","source_type":"word_analysis","support_ids":["sup_2bf00743406dfcf16dad","sup_569705da61edec51ba3e"],"title":"failed rescue before named hunger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_78e3ab76c6387c5585e4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:denied-avail-intertexts","source_type":"word_analysis","support_ids":["sup_1f10e21142be2480b132","sup_569705da61edec51ba3e"],"title":"failed resources across concrete parallels","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_5902ce921141054e7f29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:guttural-second-predicate","source_type":"word_analysis","support_ids":["sup_569705da61edec51ba3e","sup_69f431089d473deeff7d"],"title":"heavier second verb texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_93e3e8c4873e3d00141a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:independent-sufficiency-test","source_type":"word_analysis","support_ids":["sup_06a5de708e3f9bd457f8","sup_569705da61edec51ba3e"],"title":"second causative effect tested separately","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_ea2b03e3cee2044f4ce8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:omitted-beneficiary-min-domain","source_type":"word_analysis","support_ids":["sup_041eec6ec60eacc981b5","sup_569705da61edec51ba3e"],"title":"beneficiary omitted, hunger domain visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:5"],"branch_refs":[],"candidate_id":"cand_e557546ba9e7f241fd77","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:5:root-sufficiency-narrowed-to-hunger","source_type":"word_analysis","support_ids":["sup_569705da61edec51ba3e","sup_67e91327744e0dc00ccc"],"title":"broad sufficiency field narrowed to hunger relief","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:5","qac_refs":["88:7:4:1"],"status":"accepted"}},{"anchor_refs":["88:7:6"],"branch_refs":[],"candidate_id":"cand_6d662d5802a7df5cd28a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:6:delayed-boundary-shift","source_type":"word_analysis","support_ids":["sup_ac837427d2d969e55b61","sup_e28fc8c712088c56292b"],"title":"late phrase shifts from existence to efficacy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:6","qac_refs":["88:7:5:1"],"status":"accepted"}},{"anchor_refs":["88:7:6"],"branch_refs":[],"candidate_id":"cand_9afb26fce636f6f95150","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:6:relief-from-domain","source_type":"word_analysis","support_ids":["sup_ac837427d2d969e55b61","sup_af1847a084f925dc78e4"],"title":"hunger as release-domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:6","qac_refs":["88:7:5:1"],"status":"accepted"}},{"anchor_refs":["88:7:6"],"branch_refs":[],"candidate_id":"cand_cc507ef900cb25c36ca6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:6:second-predicate-attachment","source_type":"word_analysis","support_ids":["sup_7c5d6f8fa700330d4f7e","sup_ac837427d2d969e55b61"],"title":"phrase belongs to the second denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:6","qac_refs":["88:7:5:1"],"status":"accepted"}},{"anchor_refs":["88:7:6"],"branch_refs":[],"candidate_id":"cand_545814aa4e52ffe65ecc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:7:6:sound-closure-link","source_type":"word_analysis","support_ids":["sup_a322a54a8a42f7c1482a","sup_ac837427d2d969e55b61"],"title":"small preposition compressed into final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:6","qac_refs":["88:7:5:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_a6aae6e93ecf14034ee6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:feeding-formula-reversed","source_type":"word_analysis","support_ids":["sup_483d138eb95831a0732d","sup_d95ea714542c6f6c9915"],"title":"relief formula inverted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_ace9d7b3ea4414e5d040","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:genitive-prep-object","source_type":"word_analysis","support_ids":["sup_08195138fd59add65bb7","sup_d95ea714542c6f6c9915"],"title":"hunger fixed as prepositional domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_e172ed0d9bd74cd6eb2b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:hunger-as-food-function-standard","source_type":"word_analysis","support_ids":["sup_39f07e31c3f3333911e2","sup_d95ea714542c6f6c9915"],"title":"final noun gathers both failed functions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_2a95f87316338eba69d2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:noun-condition-not-agent","source_type":"word_analysis","support_ids":["sup_521bb3f9e5268a752ccd","sup_d95ea714542c6f6c9915"],"title":"condition named, cause and sufferer withheld","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_489ab3907f6687044d8f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:open-ended-deficit-state","source_type":"word_analysis","support_ids":["sup_1858ab1734dd27a4e3d4","sup_d95ea714542c6f6c9915"],"title":"indefinite hunger as unresolved condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_a127eb48de2eac506c7d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:passage-boundary-contrast","source_type":"word_analysis","support_ids":["sup_d95ea714542c6f6c9915","sup_e25ed464af5666bf5a65"],"title":"deprivation before ease contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:7"],"branch_refs":[],"candidate_id":"cand_b9258cf677a41ff0da0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:7:rare-final-sound-closure","source_type":"word_analysis","support_ids":["sup_423d2776f9a829c3877d","sup_d95ea714542c6f6c9915"],"title":"rare hunger root closes hard","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:7:7","qac_refs":["88:7:6:1"],"status":"accepted"}},{"anchor_refs":["88:7:2"],"branch_refs":[],"candidate_id":"cand_6ec8edb1d971f54987c7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000744"],"scope":"focus_ayah","source_local_id":"88:7:2:1","source_type":"qac_morpheme","support_ids":["sup_99a044a2a943e2c4d644"],"title":"QAC root occurrence: س م ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:7:4"],"branch_refs":[],"candidate_id":"cand_b6a53e7c5ba6100e3fc3","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"88:7:4:1","source_type":"qac_morpheme","support_ids":["sup_d686343748088cb930e8"],"title":"QAC root occurrence: غ ن ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:7:6"],"branch_refs":[],"candidate_id":"cand_daa9038076a062f2c34b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000278"],"scope":"focus_ayah","source_local_id":"88:7:6:1","source_type":"qac_morpheme","support_ids":["sup_b377016487608d293155"],"title":"QAC root occurrence: ج و ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:7","branch_refs":["root_000278/B001","root_000744/B001","root_001110/B002"],"candidate_id":"cand_3e86a0948c7a25692d1e","commentary_obligation":"review","hft_ref":"hft_d9466424a846cf697d3d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_two_stage_nutritional_failure","source_type":"hft","support_ids":["sup_4115f3d79c0e6aca9aa1"],"title":"base_two_stage_nutritional_failure","trust":"legacy_unbound"},{"anchor_refs":["88:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:7","branch_refs":["root_000278/B004","root_000744/B010","root_001110/B001"],"candidate_id":"cand_ddb2d7736cab346a83e6","commentary_obligation":"review","hft_ref":"hft_d93eaed657b28169bb30","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_hollow_surplus","source_type":"hft","support_ids":["sup_608eab685989d1373326"],"title":"base_hollow_surplus","trust":"legacy_unbound"},{"anchor_refs":["88:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:7","branch_refs":["root_000278/B002","root_000744/B008","root_001110/B002"],"candidate_id":"cand_7a78400a7dfe63137f2e","commentary_obligation":"review","hft_ref":"hft_bf76ac13299662713c9f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_failed_scarcity_settlement","source_type":"hft","support_ids":["sup_a4cff254ebf451c7f80b"],"title":"base_failed_scarcity_settlement","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:7:1:1","qac_word_ref":"88:7:1","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","root_ar":"س م ن","surface_ar":"يُسْمِنُ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:7:3:1","qac_word_ref":"88:7:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:7:3:2","qac_word_ref":"88:7:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","root_ar":"غ ن ي","surface_ar":"يُغْنِى"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"88:7:5:1","qac_word_ref":"88:7:5","root_ar":"","surface_ar":"مِن"},{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","root_ar":"ج و ع","surface_ar":"جُوعٍ"}],"word_analysis_qac_refs":[["88:7:1:1"],["88:7:2:1"],["88:7:3:1"],["88:7:3:2"],["88:7:4:1"],["88:7:5:1"],["88:7:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:7:1","88:7:2","88:7:3","88:7:4","88:7:5","88:7:6","88:7:7"]},"focus_surface_evidence":{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","qac_morphemes":[{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:7:1:1","qac_word_ref":"88:7:1","root_ar":"","surface_ar":"لَّا"},{"lemma_ar":"يُسْمِنُ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:2:1","qac_word_ref":"88:7:2","root_ar":"س م ن","surface_ar":"يُسْمِنُ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:7:3:1","qac_word_ref":"88:7:3","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"88:7:3:2","qac_word_ref":"88:7:3","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:7:4:1","qac_word_ref":"88:7:4","root_ar":"غ ن ي","surface_ar":"يُغْنِى"},{"lemma_ar":"مِن","morph_features":"STEM|POS:P|LEM:min","morpheme_role":"STEM","pos":"P","qac_ref":"88:7:5:1","qac_word_ref":"88:7:5","root_ar":"","surface_ar":"مِن"},{"lemma_ar":"جُوع","morph_features":"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:7:6:1","qac_word_ref":"88:7:6","root_ar":"ج و ع","surface_ar":"جُوعٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:7:1:1"],["88:7:2:1"],["88:7:3:1"],["88:7:3:2"],["88:7:4:1"],["88:7:5:1"],["88:7:6:1"]],"word_analysis_refs":["88:7:1","88:7:2","88:7:3","88:7:4","88:7:5","88:7:6","88:7:7"],"word_rows":[{"analysis_record_ref":"88:7:1","analytic_gloss_range_en":"negative particle opening the first denied imperfect predicate and preparing the repeated neither-nor frame","analytic_root_gloss_range_en":null,"qac_refs":["88:7:1:1"],"root":{},"surface":{"arabic":"لَّا","transliteration":"lā"}},{"analysis_record_ref":"88:7:2","analytic_gloss_range_en":"Form IV imperfect causative for producing fatness or bodily reserve, here denied and left without an expressed beneficiary object","analytic_root_gloss_range_en":"fatness, bodily fullness, edible fat or clarified butter, and several unrelated lexical branches; local grammar selects caused bodily reserve and blocks the unrelated branches","qac_refs":["88:7:2:1"],"root":{"arabic":"س م ن","transliteration":"s-m-n"},"surface":{"arabic":"يُسْمِنُ","transliteration":"yusminu"}},{"analysis_record_ref":"88:7:3","analytic_gloss_range_en":"conjunction segment coordinating the second negated predicate with the first and making the second failure cumulative","analytic_root_gloss_range_en":null,"qac_refs":["88:7:3:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:7:4","analytic_gloss_range_en":"second negative particle independently negating the sufficiency predicate in the coordinated frame","analytic_root_gloss_range_en":null,"qac_refs":["88:7:3:2"],"root":{},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"88:7:5","analytic_gloss_range_en":"Form IV imperfect causative for availing, sufficing, or making need unnecessary, here denied with a following hunger-domain phrase","analytic_root_gloss_range_en":"wealth, self-sufficiency, availing, replacing, song, dwelling, and other branches; local Form IV plus the following phrase narrows the active sense to hunger-specific sufficing or availing","qac_refs":["88:7:4:1"],"root":{"arabic":"غ ن ي","transliteration":"gh-n-y"},"surface":{"arabic":"يُغْنِى","transliteration":"yughni"}},{"analysis_record_ref":"88:7:6","analytic_gloss_range_en":"preposition governing the final hunger noun and marking the respect or separation domain in which availing fails","analytic_root_gloss_range_en":null,"qac_refs":["88:7:5:1"],"root":{},"surface":{"arabic":"مِن","transliteration":"min"}},{"analysis_record_ref":"88:7:7","analytic_gloss_range_en":"indefinite genitive verbal noun naming hunger as the final domain and unresolved deficit of the clause","analytic_root_gloss_range_en":"hunger, empty-stomach need, hunger-season, caused hunger, chosen hunger, and idiomatic lack or leanness; local noun selects the experienced deficit-state without narrating a cause","qac_refs":["88:7:6:1"],"root":{"arabic":"ج و ع","transliteration":"j-w-ʿ"},"surface":{"arabic":"جُوعٍۢ","transliteration":"jūʿin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:7"],"branch_refs":["root_000278/B001","root_000744/B001","root_001110/B002"],"candidate_id":"cand_3e86a0948c7a25692d1e","evidence_scope":"focus_ayah","hft_ref":"hft_d9466424a846cf697d3d","item_id":"base_two_stage_nutritional_failure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_two_stage_nutritional_failure","support_id":"sup_4115f3d79c0e6aca9aa1"},{"anchor_refs":["88:7"],"branch_refs":["root_000278/B004","root_000744/B010","root_001110/B001"],"candidate_id":"cand_ddb2d7736cab346a83e6","evidence_scope":"focus_ayah","hft_ref":"hft_d93eaed657b28169bb30","item_id":"base_hollow_surplus","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_hollow_surplus","support_id":"sup_608eab685989d1373326"},{"anchor_refs":["88:7"],"branch_refs":["root_000278/B002","root_000744/B008","root_001110/B002"],"candidate_id":"cand_7a78400a7dfe63137f2e","evidence_scope":"focus_ayah","hft_ref":"hft_bf76ac13299662713c9f","item_id":"base_failed_scarcity_settlement","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_failed_scarcity_settlement","support_id":"sup_a4cff254ebf451c7f80b"}],"diagnostics":[],"lane_counts":{"global":14,"macro":6,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"88:7","lane":"micro","linguistic_source_ref":"88:7","surface_ref":"88:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:7","target_tokens":[["O",["88:7:2","88:7:4"]],["ne",["88:7:1"]],["besler",["88:7:2"]],["ne",["88:7:3"]],["de",["88:7:3"]],["açlığı",["88:7:5","88:7:6"]],["giderir",["88:7:4"]]],"text":"O ne besler ne de açlığı giderir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:omitted-beneficiary-min-domain","source_type":"word_analysis","support_id":"sup_041eec6ec60eacc981b5","text":"{\"blocking_evidence\":null,\"headline\":\"beneficiary omitted, hunger domain visible\",\"reader_payoff\":\"The reader supplies the eater mentally while the ayah keeps hunger, not the sufferer, as the pronounced complement.\",\"reason\":\"Attachment evidence records no direct object and a following prepositional complement, with the exact form commonly appearing under negation and with prepositions.\",\"representative_source_ids\":[\"QG-840ea8b4\",\"QG-c624fc90\",\"MG-1821afaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:1","source_type":"word_analysis","support_id":"sup_05b0c6a655f483cdf635","text":"{\"gloss_range\":\"negative particle opening the first denied imperfect predicate and preparing the repeated neither-nor frame\",\"prose\":\"{{ar:لَّا}} ({{tr:lā}}) makes denial the ayah's first operation. It governs only the first imperfect at this point, so the food's bodily effect is blocked before the wider failure of relief is named. The particle is declarative, not prohibitive: the line reports that the named food cannot nourish, rather than commanding anyone not to nourish. Because a second negator follows, this first one also starts a two-beat frame in which each expected food function receives its own denial. Its doubled onset gives the opening refusal audible weight, and the shift from the prior food naming into this verbal-effect negation turns mere availability into functional deprivation.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَّا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:independent-sufficiency-test","source_type":"word_analysis","support_id":"sup_06a5de708e3f9bd457f8","text":"{\"blocking_evidence\":null,\"headline\":\"second causative effect tested separately\",\"reader_payoff\":\"The reader notices that sufficing is a second explicit food-function test, not a loose explanation of failed nourishment.\",\"reason\":\"The verb is a coordinated Form IV imperfect under its own negative particle, matching the first verb's finite shape while adding a broader effect.\",\"representative_source_ids\":[\"QG-186104d1\",\"QF-87966107\",\"MT-a6e7017e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:genitive-prep-object","source_type":"word_analysis","support_id":"sup_08195138fd59add65bb7","text":"{\"blocking_evidence\":null,\"headline\":\"hunger fixed as prepositional domain\",\"reader_payoff\":\"The reader sees hunger framed as the domain of failed relief, not as an object directly acted upon.\",\"reason\":\"QAC marks the noun as genitive after the preposition, and attachment evidence assigns it as the object of that preposition.\",\"representative_source_ids\":[\"QG-171379d3\",\"QG-1e85dcef\",\"MG-8147f70c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:paired-effect-sequence","source_type":"word_analysis","support_id":"sup_0dff004caba88754b2b6","text":"{\"blocking_evidence\":null,\"headline\":\"first concrete effect before sufficiency\",\"reader_payoff\":\"The reader sees the ayah move from bodily increase to broader need-removal in a paired causative test.\",\"reason\":\"The first Form IV imperfect is conjoined with the second, and both sit under separately articulated negation.\",\"representative_source_ids\":[\"QT-bec9ac3a\",\"QE-9f72fc93\",\"QY-4808831b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:1:paired-negation-frame","source_type":"word_analysis","support_id":"sup_12ec4a3d131ad9f7e9d0","text":"{\"blocking_evidence\":null,\"headline\":\"first beat of twofold denial\",\"reader_payoff\":\"The reader hears the first denial as the start of a structured effects-test, not as one broad negative statement.\",\"reason\":\"The second negated predicate is coordinated later in the ayah, so the first particle both negates locally and prepares the repeated frame.\",\"representative_source_ids\":[\"QS-7a5c2053\",\"QT-7df780b3\",\"MT-59611c39\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:open-ended-deficit-state","source_type":"word_analysis","support_id":"sup_1858ab1734dd27a4e3d4","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite hunger as unresolved condition\",\"reader_payoff\":\"The reader feels hunger as a continuing bodily deficit, not a passing appetite or isolated episode.\",\"reason\":\"The local noun is indefinite and the accepted V4 branch centers hunger as empty-stomach need.\",\"representative_source_ids\":[\"QG-52eb4d26\",\"QS-90cfa691\",\"MS-5d6a2e27\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:4","source_type":"word_analysis","support_id":"sup_1a71cbc4fb1a6f213406","text":"{\"gloss_range\":\"second negative particle independently negating the sufficiency predicate in the coordinated frame\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) gives the second predicate its own denial. Relief from hunger is not left as an implication of failed fattening; it is asserted as a separate failure with equal grammatical weight. The analytical split from {{ar:وَ}} ({{tr:wa}}) keeps coordination and negation visible as two steps: the line adds another test, then blocks it. The repeated short particle also creates the ayah's clipped rhythm, turning denial into a small refrain and stopping each expected benefit before the final hunger noun arrives.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:denied-avail-intertexts","source_type":"word_analysis","support_id":"sup_1f10e21142be2480b132","text":"{\"blocking_evidence\":null,\"headline\":\"failed resources across concrete parallels\",\"reader_payoff\":\"The reader recognizes a wider Quranic pattern of failed sufficiency while keeping the local resource and need concrete.\",\"reason\":\"The cited rows give concrete references, but local grammar keeps them as parallels or contrasts rather than controlling the parse.\",\"representative_source_ids\":[\"QI-3ed936df\",\"MI-276f1ccf\",\"MI-8c1f0c40\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:3:cumulative-coordination","source_type":"word_analysis","support_id":"sup_2b56f491ce95b9179898","text":"{\"blocking_evidence\":null,\"headline\":\"second failure added, not folded in\",\"reader_payoff\":\"The reader notices that sufficiency is added as a distinct failed food function rather than treated as a paraphrase of fattening.\",\"reason\":\"Attachment evidence explicitly joins the second predicate to the first through coordination.\",\"representative_source_ids\":[\"QG-3c00966d\",\"MG-763bd31a\",\"MT-9a11722b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:delayed-deficit-escalation","source_type":"word_analysis","support_id":"sup_2bf00743406dfcf16dad","text":"{\"blocking_evidence\":null,\"headline\":\"failed rescue before named hunger\",\"reader_payoff\":\"The reader experiences the ayah's escalation: failed nourishment becomes failed rescue before the final deficit is disclosed.\",\"reason\":\"The verb precedes the prepositional hunger phrase and follows the first denied causative effect.\",\"representative_source_ids\":[\"QT-3b8c406a\",\"QT-9eb8aa11\",\"QY-5316239d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2","source_type":"word_analysis","support_id":"sup_380d9b40a417f4b642d6","text":"{\"gloss_range\":\"Form IV imperfect causative for producing fatness or bodily reserve, here denied and left without an expressed beneficiary object\",\"prose\":\"{{ar:يُسْمِنُ}} ({{tr:yusminu}}) is the first tested food effect: can the prior food produce bodily reserve? The Form IV imperfect keeps that as an active causal capacity, and {{ar:لَّا}} ({{tr:lā}}) denies the capacity rather than describing a completed failure. Its subject is carried from the prior food phrase in 88:6 without forcing which live masculine singular term is resumed, so the focus stays on effect rather than identity. No beneficiary object is spoken, so the denial is not limited to one named eater; anyone looking to this food for nourishment is left outside its benefit. The root field gives the test a bodily texture: fatness, flesh-fullness, and stored surplus stand behind the verb, while local Form IV and negation keep intensive, reflexive, edible-fat, and unrelated branches from becoming separate meanings here. The rare verbal use stands out beside the fat-cow abundance imagery (12:43): the abundance field remains, but here intake cannot produce it. Its place before {{ar:يُغْنِى}} ({{tr:yughni}}) makes the sequence begin with the most concrete food function before widening to sufficiency, and the paired imperfect cadence lets the smooth expectation of nourishment be heard even as it is blocked.\",\"root_display\":\"{{ar:س م ن}} ({{tr:s-m-n}})\",\"root_gloss_range\":\"fatness, bodily fullness, edible fat or clarified butter, and several unrelated lexical branches; local grammar selects caused bodily reserve and blocks the unrelated branches\",\"surface_display\":\"{{ar:يُسْمِنُ}} ({{tr:yusminu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:hunger-as-food-function-standard","source_type":"word_analysis","support_id":"sup_39f07e31c3f3333911e2","text":"{\"blocking_evidence\":null,\"headline\":\"final noun gathers both failed functions\",\"reader_payoff\":\"The reader sees hunger retroactively measure both verbs and expose the supposed food as a systematic failure.\",\"reason\":\"The final noun arrives after the two denied food effects and is governed by the second verb's preposition.\",\"representative_source_ids\":[\"QS-4d0e2ee7\",\"QS-792e683d\",\"QT-fc571a38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:4:independent-second-negation","source_type":"word_analysis","support_id":"sup_3ed128583f28eae1e06c","text":"{\"blocking_evidence\":null,\"headline\":\"sufficiency receives its own denial\",\"reader_payoff\":\"The reader sees relief from hunger denied directly, not merely inferred from the denial of nourishment.\",\"reason\":\"The second negative particle opens the coordinated predicate headed by the sufficiency verb and its hunger-domain phrase.\",\"representative_source_ids\":[\"QG-9268bb95\",\"MG-a338a900\",\"QS-3bb3cb33\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:1:audible-and-boundary-weight","source_type":"word_analysis","support_id":"sup_419000ac1a90f0342a04","text":"{\"blocking_evidence\":null,\"headline\":\"weighted refusal after food naming\",\"reader_payoff\":\"The reader notices that the opening refusal is felt as a hard turn from named food to denied function.\",\"reason\":\"The particle has its own surface position at the start of the ayah, immediately after the prior food phrase supplied the subject under evaluation.\",\"representative_source_ids\":[\"QP-2c6d76fb\",\"QB-e718c2ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:rare-final-sound-closure","source_type":"word_analysis","support_id":"sup_423d2776f9a829c3877d","text":"{\"blocking_evidence\":null,\"headline\":\"rare hunger root closes hard\",\"reader_payoff\":\"The reader hears and sees the ayah terminate on a concentrated need-word rather than on an abstract judgment.\",\"reason\":\"The contextual profile marks the root-form as low occurrence, and the CRITICAL sound rows tie the long-vowel and guttural closure to the final noun.\",\"representative_source_ids\":[\"QI-84f45311\",\"QP-dd8cadc9\",\"QY-252a8538\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:4:particle-cadence","source_type":"word_analysis","support_id":"sup_44f4a138699198460c77","text":"{\"blocking_evidence\":null,\"headline\":\"short stops before hunger\",\"reader_payoff\":\"The reader feels the repeated particles as clipped stops that delay and intensify the final need-word.\",\"reason\":\"The sequence of short particles precedes the final prepositional phrase and supports a local cadence observation.\",\"representative_source_ids\":[\"QP-aa731351\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:feeding-formula-reversed","source_type":"word_analysis","support_id":"sup_483d138eb95831a0732d","text":"{\"blocking_evidence\":null,\"headline\":\"relief formula inverted\",\"reader_payoff\":\"The reader recognizes that a familiar relief-from-hunger wording is inverted into food that leaves hunger untouched.\",\"reason\":\"The CRITICAL rows provide the concrete 106:4 parallel, while local syntax keeps 88:7 as a deprivation reversal rather than a feeding statement.\",\"representative_source_ids\":[\"QI-13854216\",\"MI-b82cbaf7\",\"QH-bd8e7c2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:objectless-causative-negated","source_type":"word_analysis","support_id":"sup_4bd1ba9ee0a0c02de377","text":"{\"blocking_evidence\":null,\"headline\":\"objectless causative nourishment denied\",\"reader_payoff\":\"The reader notices that the food is denied the power to cause bodily increase for any implied eater, not merely in one named case.\",\"reason\":\"The verb is Form IV imperfect active with no overt object, and the local frame records an absolute objectless causative use under negation.\",\"representative_source_ids\":[\"QG-d80a908a\",\"QG-fbe54e53\",\"MG-0387620f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:noun-condition-not-agent","source_type":"word_analysis","support_id":"sup_521bb3f9e5268a752ccd","text":"{\"blocking_evidence\":null,\"headline\":\"condition named, cause and sufferer withheld\",\"reader_payoff\":\"The reader notices that the verse centers the unmet state itself instead of shifting attention to who caused it or which person is hungry.\",\"reason\":\"V4 allows caused-hunger and hungry-person related branches, but the local surface is an abstract verbal noun in a prepositional phrase.\",\"representative_source_ids\":[\"QS-6e9e1d92\",\"QS-abf1a6cc\",\"QF-5fe80798\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5","source_type":"word_analysis","support_id":"sup_569705da61edec51ba3e","text":"{\"gloss_range\":\"Form IV imperfect causative for availing, sufficing, or making need unnecessary, here denied with a following hunger-domain phrase\",\"prose\":\"{{ar:يُغْنِى}} ({{tr:yughni}}) widens the test from bodily reserve to sufficiency. It has its own {{ar:لَا}} ({{tr:lā}}), so the food is not merely unfattening; it also cannot avail at the point where food should end need. Like the first verb, it carries the prior food forward as the implicit subject, while the local frame leaves the beneficiary object unspoken and makes the following phrase the visible domain of failure. The verb is Form IV and causative: it asks whether the food can make another free of need, not whether the eater imagines independence. The root field can move through wealth, self-sufficiency, availing, song, and dwelling, but {{ar:مِن جُوعٍۢ}} ({{tr:min jūʿin}}) pulls it into practical relief from bodily dependence. In that wider pattern, wealth's avail fails (69:28) and imagined self-sufficiency is exposed (96:7), but this local clause keeps the failed resource as food and the need as hunger. Because the hunger domain is delayed until after the verb, the listener first hears the possibility of rescue and only then learns the exact need it fails to answer, with the heavier guttural opening matching the move from body mass to deeper need-removal.\",\"root_display\":\"{{ar:غ ن ي}} ({{tr:gh-n-y}})\",\"root_gloss_range\":\"wealth, self-sufficiency, availing, replacing, song, dwelling, and other branches; local Form IV plus the following phrase narrows the active sense to hunger-specific sufficing or availing\",\"surface_display\":\"{{ar:يُغْنِى}} ({{tr:yughni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:3:segmented-sound-bridge","source_type":"word_analysis","support_id":"sup_5b1c70b9edb102bd9c6c","text":"{\"blocking_evidence\":null,\"headline\":\"separate particle, tight recited bridge\",\"reader_payoff\":\"The reader sees the grammar split into conjunction plus renewed negation while hearing the transition as one tight movement.\",\"reason\":\"The bundle gives the conjunction its own word slot before the second negator, supporting the distinction between syntactic segmentation and recited flow.\",\"representative_source_ids\":[\"QF-8221d01d\",\"QE-cf608c05\",\"QP-7e3aca21\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:3","source_type":"word_analysis","support_id":"sup_5d03b5f8db5febf4ef25","text":"{\"gloss_range\":\"conjunction segment coordinating the second negated predicate with the first and making the second failure cumulative\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is the hinge that prevents the second clause from being only a gloss on the first. It coordinates a second failed effect with the same implicit subject: no bodily gain, and then no release from hunger. In the negative frame it functions like 'nor' while still carrying ordinary addition, so the ayah accumulates failures rather than repeating one idea. Since the conjunction is segmented before the next {{ar:لَا}} ({{tr:lā}}), the listener can see coordination and renewed negation as separate mechanisms even though recitation binds them tightly. The exception named in 88:6 therefore does not become relief; the particle carries it straight into another functional denial.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:root-sufficiency-narrowed-to-hunger","source_type":"word_analysis","support_id":"sup_67e91327744e0dc00ccc","text":"{\"blocking_evidence\":null,\"headline\":\"broad sufficiency field narrowed to hunger relief\",\"reader_payoff\":\"The reader feels the broad force of being freed from need while seeing that the local issue is bodily hunger, not wealth or abstract independence.\",\"reason\":\"V4 shows several accepted branches, but the local Form IV and following hunger phrase select availing or sufficing with respect to hunger.\",\"representative_source_ids\":[\"QS-c1285324\",\"MS-6ab9f1eb\",\"QI-16fc2d69\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:5:guttural-second-predicate","source_type":"word_analysis","support_id":"sup_69f431089d473deeff7d","text":"{\"blocking_evidence\":null,\"headline\":\"heavier second verb texture\",\"reader_payoff\":\"The reader hears the second predicate as texturally heavier while the semantic test deepens from body mass to need-removal.\",\"reason\":\"The sound observation is supported as a local surface contrast with the preceding matched imperfect.\",\"representative_source_ids\":[\"QP-068005f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:6:second-predicate-attachment","source_type":"word_analysis","support_id":"sup_7c5d6f8fa700330d4f7e","text":"{\"blocking_evidence\":null,\"headline\":\"phrase belongs to the second denial\",\"reader_payoff\":\"The reader keeps the final phrase from retroactively flattening both verbs into one hunger-governed construction.\",\"reason\":\"The local attachment table connects the prepositional phrase to the second verb while the first and second verbs are coordinated.\",\"representative_source_ids\":[\"QG-3599d7a3\",\"MG-8fe178d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:4:neither-nor-symmetry","source_type":"word_analysis","support_id":"sup_819ff01220c36367ab86","text":"{\"blocking_evidence\":null,\"headline\":\"balanced repeated denial\",\"reader_payoff\":\"The reader hears the two food functions rejected with balanced force rather than ranked as primary and secondary.\",\"reason\":\"The repeated negator mirrors the first particle in the local parallel structure.\",\"representative_source_ids\":[\"QT-9ea1b52b\",\"MT-836a8c8d\",\"QE-64ff7e9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:bodily-reserve-root-image","source_type":"word_analysis","support_id":"sup_8953a580aa2590ae175b","text":"{\"blocking_evidence\":null,\"headline\":\"fatness field narrowed to nutritive reserve\",\"reader_payoff\":\"The reader feels the denial as anti-nutritive: the thing called food cannot become stored bodily life.\",\"reason\":\"V4 includes fatness and edible-fat branches, but the local Form IV imperfect selects caused bodily reserve; other branches remain background or are excluded locally.\",\"representative_source_ids\":[\"QS-17504fbc\",\"QS-86335d27\",\"MS-31b66c0b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:implicit-food-subject","source_type":"word_analysis","support_id":"sup_8d816aec9b845621133f","text":"{\"blocking_evidence\":null,\"headline\":\"subject carried from prior food phrase\",\"reader_payoff\":\"The reader keeps 88:7 as an evaluation of the prior named food while preserving the grammatical ambiguity of which prior masculine singular term is resumed.\",\"reason\":\"Attachment evidence marks the subject as implicit and ambiguous between prior masculine singular food terms, so the topic survives as contextual continuation without forcing one antecedent.\",\"representative_source_ids\":[\"QG-a241452c\",\"QB-2b63c52c\",\"QB-a3cb3ce5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:7:2:1","source_type":"qac_morpheme","support_id":"sup_99a044a2a943e2c4d644","text":"{\"lemma_ar\":\"يُسْمِنُ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:yusominu|ROOT:smn|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:7:2:1\",\"qac_word_ref\":\"88:7:2\",\"root_ar\":\"س م ن\",\"surface_ar\":\"يُسْمِنُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:6:sound-closure-link","source_type":"word_analysis","support_id":"sup_a322a54a8a42f7c1482a","text":"{\"blocking_evidence\":null,\"headline\":\"small preposition compressed into final noun\",\"reader_payoff\":\"The reader hears the short preposition carry the earlier verbal sound into the long final hunger word.\",\"reason\":\"The CRITICAL rows make a local sound claim tied to adjacent words and the final phrase, with no contradiction from grammar.\",\"representative_source_ids\":[\"QE-350cb8ff\",\"QP-979b330f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:6","source_type":"word_analysis","support_id":"sup_ac837427d2d969e55b61","text":"{\"gloss_range\":\"preposition governing the final hunger noun and marking the respect or separation domain in which availing fails\",\"prose\":\"{{ar:مِن}} ({{tr:min}}) makes hunger the domain from which availing would release and the respect in which the food fails. It attaches to {{ar:يُغْنِى}} ({{tr:yughni}}), not back to the first predicate, so the ayah keeps the two-part structure intact: first no bodily reserve, then no sufficiency from hunger. The preposition also delays the precise deficit until the close of the verse, turning a general-looking denial of availing into a targeted failure against bodily need. Its recurrence after the earlier source-language of the food shifts the register from what the food is from to what it cannot relieve from, and its m-n sound links the first denied bodily effect to the compressed arrival of the final hunger domain.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مِن}} ({{tr:min}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:6:relief-from-domain","source_type":"word_analysis","support_id":"sup_af1847a084f925dc78e4","text":"{\"blocking_evidence\":null,\"headline\":\"hunger as release-domain\",\"reader_payoff\":\"The reader notices that hunger is not a direct object but the state or respect from which relief should come and does not.\",\"reason\":\"Attachment evidence makes the preposition govern the final noun as a complement to the sufficiency verb.\",\"representative_source_ids\":[\"QG-0e664a13\",\"QG-e37c2784\",\"QS-161dc385\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:7:6:1","source_type":"qac_morpheme","support_id":"sup_b377016487608d293155","text":"{\"lemma_ar\":\"جُوع\",\"morph_features\":\"STEM|POS:N|LEM:juwE|ROOT:jwE|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:7:6:1\",\"qac_word_ref\":\"88:7:6\",\"root_ar\":\"ج و ع\",\"surface_ar\":\"جُوعٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:3:boundary-after-exception","source_type":"word_analysis","support_id":"sup_b4234cbe27e5ae910a92","text":"{\"blocking_evidence\":null,\"headline\":\"available food becomes nonfunctional\",\"reader_payoff\":\"The reader keeps the prior exception from sounding like relief because the conjunction carries that food into another denial of function.\",\"reason\":\"The second predicate remains coordinated with the first effect-test of the food supplied by the prior ayah.\",\"representative_source_ids\":[\"QB-f1dc6b35\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:7:4:1","source_type":"qac_morpheme","support_id":"sup_d686343748088cb930e8","text":"{\"lemma_ar\":\"أَغْنَتْ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:7:4:1\",\"qac_word_ref\":\"88:7:4\",\"root_ar\":\"غ ن ي\",\"surface_ar\":\"يُغْنِى\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:rare-abundance-contrast","source_type":"word_analysis","support_id":"sup_d69ea32afe425fee8f83","text":"{\"blocking_evidence\":null,\"headline\":\"rare verbal abundance test\",\"reader_payoff\":\"The reader notices the marked verbal use of a sparse fatness field, with abundance imagery inverted into failed nourishment.\",\"reason\":\"The contextual profile marks the exact root-form as low occurrence, and the CRITICAL intertext to 12:43 is a concrete abundance contrast rather than a governing parse.\",\"representative_source_ids\":[\"QI-68dc732b\",\"MI-580fb52f\",\"QH-b1391975\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7","source_type":"word_analysis","support_id":"sup_d95ea714542c6f6c9915","text":"{\"gloss_range\":\"indefinite genitive verbal noun naming hunger as the final domain and unresolved deficit of the clause\",\"prose\":\"{{ar:جُوعٍۢ}} ({{tr:jūʿin}}) is the final deficit word that explains why both denials matter. Governed by {{ar:مِن}} ({{tr:min}}), it is genitive and prepositional, not a direct object or construct complement; hunger is the state from which relief should come. Its indefiniteness makes the condition open-ended rather than a single episode, and the verbal noun closes on hunger itself instead of naming a hungry person or narrating someone causing hunger. The broader root family includes being hungry, being made hungry, famine-like periods, and figurative emptiness, but the local clause concentrates that range into bodily need left unreleased. This reverses the relief formula: feeding answers hunger (106:4), but here the thing called food in 88:6 relieves nothing. Hunger therefore becomes the standard that retroactively judges both verbs, while the rare root, the prior degraded food's shared final ʿayn echo, and the long-vowel guttural close make the ayah end on unresolved need. The following shift toward ease in 88:8 is sharpened by this hard closure.\",\"root_display\":\"{{ar:ج و ع}} ({{tr:j-w-ʿ}})\",\"root_gloss_range\":\"hunger, empty-stomach need, hunger-season, caused hunger, chosen hunger, and idiomatic lack or leanness; local noun selects the experienced deficit-state without narrating a cause\",\"surface_display\":\"{{ar:جُوعٍۢ}} ({{tr:jūʿin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:7:passage-boundary-contrast","source_type":"word_analysis","support_id":"sup_e25ed464af5666bf5a65","text":"{\"blocking_evidence\":null,\"headline\":\"deprivation before ease contrast\",\"reader_payoff\":\"The reader keeps the preceding food claim and following ease-scene in view as the hunger word closes one side of the passage contrast.\",\"reason\":\"The CRITICAL rows explicitly link the final noun to the food claim in 88:6 and the contrastive movement into 88:8.\",\"representative_source_ids\":[\"ME-99662a31\",\"QB-683975f5\",\"QB-965f206b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:6:delayed-boundary-shift","source_type":"word_analysis","support_id":"sup_e28fc8c712088c56292b","text":"{\"blocking_evidence\":null,\"headline\":\"late phrase shifts from existence to efficacy\",\"reader_payoff\":\"The reader feels the verse close by revealing that the available thing fails precisely as relief from need.\",\"reason\":\"The preposition appears after the second verb and before the final noun, making it a compact boundary into the closing deficit phrase.\",\"representative_source_ids\":[\"QT-5d3a28ca\",\"QB-562be876\",\"QB-836e8ee4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:1:opening-local-negation","source_type":"word_analysis","support_id":"sup_f5c1ce34895e1e9b6101","text":"{\"blocking_evidence\":null,\"headline\":\"first predicate denied as fact\",\"reader_payoff\":\"The reader notices that the ayah begins by blocking a concrete food effect before explaining the larger hunger failure.\",\"reason\":\"QAC and attachment evidence identify the particle as the local negator of the following imperfect predicate, not as a command particle.\",\"representative_source_ids\":[\"QG-41b5b658\",\"QG-4733cbab\",\"MG-ce629122\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:7:2:soft-cadence-before-hard-failure","source_type":"word_analysis","support_id":"sup_fd86db2a3f7995e4e2d6","text":"{\"blocking_evidence\":null,\"headline\":\"smooth verbal cadence still blocked\",\"reader_payoff\":\"The reader hears the smooth first verb as part of the paired cadence while its expected nourishment is still refused.\",\"reason\":\"The surface shape and its coordination with the matching second imperfect support a restrained sound-level observation.\",\"representative_source_ids\":[\"QP-34f34fa6\",\"QP-cccbfe78\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000278/B001","root_000744/B001","root_001110/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000744","role":"Bodily fatness, opposite leanness, supplies the accretion pole blocked by the first negation.","root":"س م ن","source_ref":"88:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficing, benefiting, or standing in supplies the functional-relief pole blocked by the second negation.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000278","role":"The empty stomach and its pain specify the bodily deficit that remains operative.","root":"ج و ع","source_ref":"88:7","source_word_indices":["6"]}],"changed_reading":{"after":"It fails both conversion into bodily reserve and immediate cancellation of bodily lack: intake occurs, but neither accumulation nor relief follows.","before":"It is food that neither fattens nor satisfies hunger."},"confidence":"strong","focus_anchor":"The coordinated negations attach separately to يُسْمِنُ and يُغْنِى, while مِن جُوعٍ names the deficit left unresolved.","mechanism":"The substance fails two different nutritional tests: it adds no bodily reserve and it does not functionally suffice to terminate an existing deficit. The second clause is not merely a synonym of the first; a thing might fail to fatten yet still relieve hunger, but this does neither.","model_id":"base_two_stage_nutritional_failure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_two_stage_nutritional_failure","source_type":"hft","support_id":"sup_4115f3d79c0e6aca9aa1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000278/B004","root_000744/B010","root_001110/B001"],"payload":{"activation_trace":[{"branch_id":"B010","mapped_root_id":"root_000744","role":"Self-inflating claims to unowned merit or rank supply the deceptive outward increase.","root":"س م ن","source_ref":"88:7","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001110","role":"Wealth and independence from need supply the genuine sufficiency that the apparent increase cannot create.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_000278","role":"Hunger extended to emptiness or longing lets the unresolved lack exceed a merely caloric reading.","root":"ج و ع","source_ref":"88:7","source_word_indices":["6"]}],"changed_reading":{"after":"It can also expose hollow enlargement: nothing in this intake produces real substance, independence, or an answer to inner lack.","before":"The verse denies the physical usefulness of a food."},"confidence":"exploratory","focus_anchor":"The roots of يُسْمِنُ, يُغْنِى, and جُوعٍ each carry a non-caloric branch concerning claimed surplus, independence, and inner emptiness.","mechanism":"An apparent increase can be socially or rhetorically inflated without producing real independence. The two negations puncture that false surplus: it cannot enlarge standing and cannot release the subject from an inward lack figured as hunger or longing.","model_id":"base_hollow_surplus"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_hollow_surplus","source_type":"hft","support_id":"sup_608eab685989d1373326","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000278/B002","root_000744/B008","root_001110/B002"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_000744","role":"Equalizing partners' shares by returning excess supplies a distributive correction that the first negation can withhold.","root":"س م ن","source_ref":"88:7","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficing or standing in for something supplies the standard for an adequate replacement.","root":"غ ن ي","source_ref":"88:7","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000278","role":"A famine-time expands the deficit from one stomach to a scarcity regime in which shares matter.","root":"ج و ع","source_ref":"88:7","source_word_indices":["6"]}],"changed_reading":{"after":"In a scarcity frame, the ration neither repairs a deficient share nor counts as an adequate substitute; private hunger and failed distribution coexist.","before":"One eater remains hungry after an inadequate meal."},"confidence":"exploratory","focus_anchor":"يُسْمِنُ activates a branch of restoring unequal shares, يُغْنِى names an adequate substitute, and جُوعٍ can widen from an episode to a hunger-time.","mechanism":"Under scarcity, provision has distributive as well as bodily work: it should repair a short share or substitute adequately for what is missing. The coordinated negation allows neither function, so the item leaves both the allocation and the need uncorrected.","model_id":"base_failed_scarcity_settlement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_failed_scarcity_settlement","source_type":"hft","support_id":"sup_a4cff254ebf451c7f80b","trust":"legacy_unbound"}]}
</lane_packet_json>
