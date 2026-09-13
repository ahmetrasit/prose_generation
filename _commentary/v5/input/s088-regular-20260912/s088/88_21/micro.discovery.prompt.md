# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:21**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_21/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:21",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"erkek cinsiyet ve erkek yavru doğurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeklik karşıtlığını ve buna bağlı doğurma türetimlerini birlikte göstermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_image_ar":"الذكر خلاف الأنثى","concept_gloss":"erkek cinsiyet ve erkek yavru doğurma","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın dişinin karşıtı olan cinsiyeti belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek yavru doğurmaya ilişkin türemiş kullanım alanını dışarıda bırakır.","preserves":"Bireyin erkek cinsiyetinden olması anlamını korur."},"facet_ids":["F001","F002"],"text":"erkek","usage_role":"general"},{"applicability":"Bir dişinin doğurduğu yavrunun erkek olduğunu bildiren çekimli yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel erkek cinsiyet kategorisini ve çoğul adlandırmaları kapsamaz.","preserves":"Doğum sonucunun erkek yavru olması anlamını korur."},"facet_ids":["F003"],"text":"erkek yavru doğurmak","usage_role":"contextual"}],"definition":"Canlıların dişinin karşısında yer alan erkek cinsiyetinden olmasıdır. Bu çekirdeğe bağlı biçimler, erkek yavru dünyaya getirmeyi veya bunu alışkanlıkla yapmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."},{"facet_id":"F002","role":"extension","statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."},{"facet_id":"F003","role":"specialization","statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}],"identity_rationale":"Kaynak ifadesi dalın merkezini dişinin karşıtı olan erkek cinsiyet olarak kurar; çoğul adları ve erkek yavru doğurma anlatımları bu merkeze bağlı türetimlerdir. Ayrı sözlüksel birimlerde görülen anatomi ve erkeğe benzetme kullanımları çekirdek tanımı genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erkek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"erkek üreme organı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"erkeğin üreme organı çevresindeki organlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"erkekler veya erkeklik"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"erkek yavru doğurdu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çoğunlukla erkek yavru doğuran dişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"erkek yapılı kadın veya dişi deve"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gebe için kolay doğum ve erkek çocuk dileği"}],"lexicalization_note":"Tanım erkek cinsiyet çekirdeğini korur; doğurma, anatomi ve benzetme anlamları yalnız ilgili çekimli biçim ya da söz öbeğiyle sınırlandırılır.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; dört belirgin karşıtlık veya sınır ilişkisi seçildi, kalanlar anatomi, gelişim, bellek, söz ve belge alanlarında uzak ya da yinelenen eşleşmelerdi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı cinsiyet ekseninde doğrudan karşıttırlar; biri erkek, öteki dişi tarafını seçer.","focus_only":"Odak dalı erkek cinsiyetini ve ona bağlı erkek yavru doğurma biçimlerini anlatır.","gloss":"erkek ile dişi","neighbor_only":"Komşu dal dişi cinsiyetini ve dişiliğe bağlı biçimleri anlatır.","neighbor_ref":"root_000058/B001","relation_type":"antonym","shared_zone":"İki dal canlıların biyolojik cinsiyet ayrımının karşıt uçlarını adlandırır."},{"boundary_match":"partial","distinction":"Odak biyolojik kategoridir ve hayvanları da kapsar; komşu ise insan kişisini ve toplumsal nitelendirmeleri öne çıkarır.","focus_only":"Odak, insanlarla sınırlı olmayan erkek cinsiyet kategorisini belirtir.","gloss":"erkek cinsiyet ile erkek kişi","neighbor_only":"Komşu, yetişkin erkek kişiyi ve ona yüklenen erkekçe nitelikleri belirtir.","neighbor_ref":"root_000546/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal insan söz konusu olduğunda erkek olma alanında buluşur."},{"boundary_match":"partial","distinction":"Cinsiyet kategorisi bir bütün olarak bireyi sınıflandırır; komşu ifade yalnız belirli bir organı adlandırır.","focus_only":"Odak dalı canlı bireyin erkek cinsiyetinden olmasını temel alır.","gloss":"erkeklik ile erkek anatomisi","neighbor_only":"Komşu dal yalnız erkek üreme organı için kullanılan örtmeceli bir adı verir.","neighbor_ref":"root_000597/B007","relation_type":"near_neighbor","shared_zone":"İki dal erkek cinsiyetle ilişkili bedensel alana temas eder."},{"boundary_match":"field_only","distinction":"Birinci dal cinsiyet sınıflamasıdır; ikinci dal ise cinsiyetten bağımsız varlıklara aktarılabilen güç ve sertlik niteliğidir.","focus_only":"Odak dalı gerçek erkek cinsiyetini ve buna bağlı doğum biçimlerini anlatır.","gloss":"erkeklik ile güçlü sertlik","neighbor_only":"Komşu dal nesne, bitki, insan veya olaylara yüklenen sertlik ve güç niteliğini anlatır.","neighbor_ref":"root_000516/B002","relation_type":"same_field","shared_zone":"Aynı kökten gelen iki dal bazı niteleme biçimlerinde erkeklik çağrışımını paylaşır."}],"source_phrase_ar":"الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar erkek ile dişi arasındaki temel karşıtlıkta birleşir; ayrıca erkekler için kullanılan çoğul biçimleri ve erkek yavru doğurmaya ilişkin türetimleri aynı anlam alanına bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكر والذكورة والذكران وولادة الذكور والمذكار وما شبه بالذكر في الخلقة.","what_is_not_ar":"لا يدخل فيه مجرد التذكر أو الذكر باللسان ولا الصيت والشرف."},"support_links":[]},{"boundary":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"sert, keskin ve güçlü olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel sertlik ile kişi ve durumlara aktarılan yoğun güç anlamlarını birlikte açıklarken kullanılır.","boundary_detail":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_image_ar":"صلابة الذكر وحدته وشدته","concept_gloss":"sert, keskin ve güçlü olma","contextual_glosses":[{"applicability":"Demir, bitki veya benzeri maddi bir varlığın kuru, kalın ve dayanıklı yapısı anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıçtaki keskinliği ve kişi ya da olaylara aktarılan güç anlamını dışarıda bırakır.","preserves":"Maddi varlıktaki güçlü sertlik ve dayanıklılık niteliğini korur."},"facet_ids":["F001","F002"],"text":"çok sert ve dayanıklı","usage_role":"contextual"},{"applicability":"Kişi, gün, yol, felaket, yağmur, söz veya şiir yoğunluk ve zorluk bakımından nitelenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Metal ve bitkideki somut sertlik ile kılıçtaki keskinliği kapsamaz.","preserves":"Aktarmalı güç, şiddet ve zorluk anlamını korur."},"facet_ids":["F001","F003"],"text":"çetin ve güçlü","usage_role":"contextual"}],"definition":"Belirli varlıkların sert, kuru, keskin, güçlü veya çetin oluşunu bildiren bir nitelemedir. Metal ve bitkide fiziksel dayanıklılığı, kişi, olay, hava ve sözde ise yoğun güç ya da zorluğu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."},{"facet_id":"F002","role":"specialization","statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."},{"facet_id":"F003","role":"extension","statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}],"identity_rationale":"Kaynak ifadesi demir, kılıç ve sert bitkilerdeki somut sertlik ile insan, gün, yol, felaket, yağmur, söz ve şiire aktarılan güç ve şiddeti aynı niteleme dalında toplar. Geçici çerçeve bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"demirin en sert ve kuru türü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"keskin ve sağlam kılıç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kılıcın veya erkeğin keskinliği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kalın ve sert otlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"güçlü, yiğit ve onurlu adam"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çetin ve korkutucu gün, yol veya felaket"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"şiddetli yağmur, sağlam söz veya güçlü şiir"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova"}],"lexicalization_note":"Somut ve aktarmalı nitelikler ayrı yüzler olarak korunur; hiçbiri bağlamdan bağımsız genel bir kök anlamı gibi sunulmaz.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; en açıklayıcı beş karşıt veya yakın sınır seçildi, öteki adaylar hava, madde ve kardeş dallar bakımından daha uzak ya da yinelenendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak güçlü ve keskin ucu, komşu ise yumuşak ve zayıf ucu seçtiği için doğrudan karşıttırlar.","focus_only":"Odak dalı sertlik, keskinlik, güç ve çetinlik niteliğini taşır.","gloss":"sertlik ile yumuşaklık","neighbor_only":"Komşu dal yumuşaklık, kesmeyiş, zayıflık ve edilgenlik niteliğini taşır.","neighbor_ref":"root_000058/B002","relation_type":"antonym","shared_zone":"İki dal nesne ve kişilerin güç ile dayanıklılık eksenindeki karşıt uçlarını niteler."},{"boundary_match":"partial","distinction":"Odak keskinlik ve şiddetli durumlara daha açıktır; komşu sıkılık ve darbeye dayanma yeteneğine daha belirgin biçimde bağlıdır.","focus_only":"Odak, keskinlik ile gün, yol, yağmur, söz ve şiirdeki aktarmalı şiddeti de kapsar.","gloss":"çetin sertlik ile dayanıklılık","neighbor_only":"Komşu, darbeye dayanma ve sıkı dokulu sağlamlık gibi bedensel veya maddi dayanıklılığı öne çıkarır.","neighbor_ref":"root_000253/B002","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü, sağlam ve kolay bozulmayan bir niteliği anlatabilir."},{"boundary_match":"partial","distinction":"Komşu kılıca özgü dar bir nitelemedir; odak ise aynı özelliği daha geniş bir varlık ve durum dizisine taşır.","focus_only":"Odak metal dışındaki varlıkları ve aktarmalı güç nitelemelerini de kapsar.","gloss":"genel sertlik ile keskin kılıç","neighbor_only":"Komşu yalnız bir kılıcın keskin ve kesici olmasını niteler.","neighbor_ref":"root_000258/B009","relation_type":"near_synonym","shared_zone":"Kılıç söz konusu olduğunda iki dal keskinlik ve güçlü kesme niteliğinde buluşur."},{"boundary_match":"partial","distinction":"Odak keskin ve çetin oluşa, komşu ise gücün sürmesi ve maddi sağlamlığa doğru ayrışır.","focus_only":"Odak keskinliği ve belirli söz öbeklerindeki çetinlik nitelemesini içerir.","gloss":"sert güç ile kalıcı sağlamlık","neighbor_only":"Komşu kalıcılık, semizlik ve kumaş dayanıklılığı gibi ek gelişmeleri içerir.","neighbor_ref":"root_000973/B007","relation_type":"near_synonym","shared_zone":"Her iki dal güç, sertlik ve dayanıklılık alanında önemli ölçüde örtüşür."},{"boundary_match":"field_only","distinction":"Sertlik niteliği cinsiyet bildirmez; erkek cinsiyet dalı da tek başına güç veya keskinlik yüklemez.","focus_only":"Odak çeşitli varlıklara yüklenen sertlik, güç ve keskinliği anlatır.","gloss":"güç niteliği ile erkek cinsiyet","neighbor_only":"Komşu erkek ile dişi arasındaki biyolojik cinsiyet karşıtlığını anlatır.","neighbor_ref":"root_000516/B001","relation_type":"same_field","shared_zone":"İki dal aynı kökten gelen ve kimi tarihsel nitelemelerde ilişkilenen anlam alanlarına aittir."}],"source_phrase_ar":"سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)","source_summary":"Kaynaklar sert demir, keskin kılıç ve kalın bitki örneklerini temel alır; aynı niteliği güçlü kişiye ve şiddetli ya da çetin olay, yol, hava ve söz anlatımlarına genişletir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحديد الذكر والسيف المذكر وذكور البقل وما وصف بالشدة والقوة كالرجل الذكر واليوم والطريق والداهية والمطر.","what_is_not_ar":"لا يدخل فيه الذكر بمعنى الحفظ أو الكلام أو الكتاب."},"support_links":[]},{"boundary":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B003","candidate_links":[{"candidate_id":"cand_227730f5b2234a388bf8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"akılda tutma ve yeniden hatırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bellekte koruma durumunu hem de unutulanı etkin biçimde geri çağırma sürecini birlikte anlatır.","boundary_detail":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_image_ar":"استحضار الشيء بعد النسيان أو مع الحفظ","concept_gloss":"akılda tutma ve yeniden hatırlama","contextual_glosses":[{"applicability":"Unutulmuş veya o sırada düşünülmeyen bir şey yeniden bilince geldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgiyi sürekli akılda tutma ve ezber için çalışma yüzlerini dışarıda bırakır.","preserves":"Bilgiyi yeniden bilince getirme eylemini doğal biçimde korur."},"facet_ids":["F002"],"text":"hatırlamak","usage_role":"general"},{"applicability":"Bir bilgi ya da yükümlülüğün unutulmadan bellekte korunması istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Unutulanı etkin olarak geri çağırma ve arama sürecini kapsamaz.","preserves":"Bilginin bellekte hazır ve korunmuş bulunması anlamını korur."},"facet_ids":["F001"],"text":"aklında tutmak","usage_role":"contextual"}],"definition":"Bir şeyi unutmayacak biçimde zihinde tutmak veya unutulan bilgiyi yeniden bilince getirmektir. Buna bağlı kullanımlar, kayıp bilgiyi aramayı ve belleği korumak için çalışmayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."},{"facet_id":"F002","role":"core","statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."},{"facet_id":"F003","role":"specialization","statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}],"identity_rationale":"Kaynak ifadesi unutmanın karşıtı olarak bir şeyi zihinde tutmayı, unutulanı yeniden bilince getirmeyi ve kaybolan bilgiyi arayıp bulmayı birlikte verir. Geçici çerçeve zihinsel süreç ile korunmuş bellek durumunu doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hatırladı veya aklında tuttu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aklında"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hatırlama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ezberlemek için çalışma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Zihinsel çekirdek korunur; akılda olma, yeniden hatırlama, ezber çalışması ve iyi bellek nitelemeleri kendi yapılarına bağlı yüzlerdir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; bellek eksenini en iyi açıklayan beş ilişki seçildi, tanıma, düşünme, eski tanışıklık ve diğer kardeş dallar daha uzak veya yinelenen kaldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak bellekte varlık ve erişimi, komşu ise aynı varlık ve erişimin kaybını bildirir.","focus_only":"Odak bir bilginin bellekte bulunmasını veya yeniden bilince gelmesini anlatır.","gloss":"hatırlama ile unutma","neighbor_only":"Komşu bir bilginin bellekten kaybolmasını ve sahibince erişilememesini anlatır.","neighbor_ref":"root_000913/B004","relation_type":"antonym","shared_zone":"İki dal bilginin bellekte bulunup bulunmaması ekseninde karşı karşıya gelir."},{"boundary_match":"partial","distinction":"Komşu daha çok bilginin yerleşik korunmasına, odak ise hem korumaya hem yeniden geri çağırmaya uzanır.","focus_only":"Odak unutulan bilgiyi etkin biçimde geri çağırma sürecini de içerir.","gloss":"hatırlama ile bellekte saklama","neighbor_only":"Komşu işitilen veya öğrenilen şeyin zihinde sağlam biçimde yerleşmesini öne çıkarır.","neighbor_ref":"root_000342/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bilginin unutulmadan zihinde bulunması alanında örtüşür."},{"boundary_match":"partial","distinction":"Ezbere bilme dış kaynağa ihtiyaç duymayan yerleşik öğrenmeyi gerektirir; odak böyle bir öğrenme koşulu olmadan da hatırlamayı kapsar.","focus_only":"Odak genel olarak akılda tutmayı ve unutulanı hatırlamayı kapsar.","gloss":"hatırlama ile ezbere bilme","neighbor_only":"Komşu bir metne bakmadan ezbere bilme durumuyla sınırlıdır.","neighbor_ref":"root_000970/B019","relation_type":"near_neighbor","shared_zone":"İki dal bilginin zihinde hazır bulunması bakımından buluşur."},{"boundary_match":"partial","distinction":"Komşu bir çalışma yöntemi ve yineleme sürecidir; odak ise yönteme bağlı olmadan bellek durumu ile geri çağırmayı anlatır.","focus_only":"Odak bilginin zihinde bulunması veya geri çağrılması sonucunu içerir.","gloss":"hatırlama ile zihinsel yineleme","neighbor_only":"Komşu bir sözü belleğe yerleştirmek için içten yineleme eylemini öne çıkarır.","neighbor_ref":"root_000562/B006","relation_type":"near_neighbor","shared_zone":"İçten yineleme, bilginin hatırlanmasını ve bellekte tutulmasını destekleyebilir."},{"boundary_match":"partial","distinction":"Odak zihinsel sonuç ve süreçtir; komşu bu sonucu meydana getiren neden veya hatırlatıcıdır.","focus_only":"Odak kişinin zihninde gerçekleşen hatırlama ve akılda tutma durumudur.","gloss":"hatırlama ile hatırlatma","neighbor_only":"Komşu bir başkasında ya da kişinin kendisinde hatırlamayı doğuran uyarı, araç veya eylemdir.","neighbor_ref":"root_000516/B009","relation_type":"near_neighbor","shared_zone":"İki dal unutulan bilginin yeniden zihinde hazır olması sonucunda buluşur."}],"source_phrase_ar":"ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)","source_summary":"Kaynaklar unutmanın karşıtı olan zihinsel korumayı, unutulanı geri çağırmayı ve kaybolan bilgiyi yeniden bulma çabasını tek bir bellek alanında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحفظ والاستحضار بالقلب والتذكر والاستذكار وما يكون خلاف النسيان.","what_is_not_ar":"لا يدخل فيه مجرد جريان اللفظ على اللسان إذا لم يقصد حضور المعنى في النفس."},"support_links":["sup_5f8f0c276afcd187c3e7"]},{"boundary":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_kind":"collocation","branch_ref":"root_000516/B004","candidate_links":[{"candidate_id":"cand_74aca909adf4326c4f7d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"bir şeyi sözle anma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, nesne veya konunun dilde adlandırılması ve söz konusu edilmesi gereken yapılarda kullanılır.","boundary_detail":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_image_ar":"جريان الذكر على اللسان","concept_gloss":"bir şeyi sözle anma","contextual_glosses":[{"applicability":"Bir kişi ya da şeyin adı konuşma içinde geçirildiğinde doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü söz sayılabilen geniş kaynak açıklamasını ve özel çekiştirme kullanımını belirtmez.","preserves":"Bir şeyi söz içinde adlandırma ve söz konusu etme eylemini korur."},"facet_ids":["F001","F002"],"text":"anmak","usage_role":"general"},{"applicability":"Bir insanın eksik ve kusurlarından o yokken söz etme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tarafsız veya olumlu sözle anma çekirdeğini dışarıda bırakır.","preserves":"İnsanları kusurlarıyla anma biçimindeki olumsuz özel kullanımı korur."},"facet_ids":["F003"],"text":"arkasından kusurlarını söylemek","usage_role":"contextual"}],"definition":"Bir şeyi dil aracılığıyla söz konusu etmek, adını söylemek veya sözle görünür kılmaktır. İnsanların kusurlarını arkalarından söyleme, bu eylemin olumsuz bağlama bağlı bir türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."},{"facet_id":"F002","role":"extension","statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."},{"facet_id":"F003","role":"associated_use","statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}],"identity_rationale":"Kaynak ifadesi bir şeyin dilde söz olarak geçirilmesini merkeze alır ve kusur söyleyerek çekiştirmeyi bağlama bağlı bir alt kullanım olarak verir. Her sözün bu adla anılabileceği geniş açıklama, dalı bütün konuşma eylemleriyle özdeşleştirmeden yorumlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sözle anma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"insanların arkasından kusurlarını söyleme"}],"lexicalization_note":"Tanım açıkça sözle anma yapısına bağlı tutulur; çekiştirme anlamı yalnız insanlardan kusurlarıyla söz etme bağlamında verilir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; konuşma, övgü, yerme, hatırlama ve ünle en yararlı beş sınır seçildi, diğerleri özel konuşma türleri veya uzak kardeş anlamlardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Dile getirme genel bir konuşma eylemidir; sözle anma ise belirli bir içeriği adlandırıp konu etmeye bağlıdır.","focus_only":"Odak belirli bir kişi, nesne veya konuyu söz içinde anmayı gerektirir.","gloss":"sözle anma ile dile getirme","neighbor_only":"Komşu, belirli bir içeriği anma koşulu olmadan konuşma seslerini dışa vurmayı anlatır.","neighbor_ref":"root_001364/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal düşüncenin dil ve ses aracılığıyla dışarı çıkarılmasını içerir."},{"boundary_match":"partial","distinction":"Övme zorunlu olarak olumlu değer yükler; odak dalı ise değer yönü taşımadan yalnız söz konusu etmeyi de kapsar.","focus_only":"Odak olumlu, tarafsız veya olumsuz olabilen genel sözle anmayı kapsar.","gloss":"anma ile övme","neighbor_only":"Komşu bir kişiyi en iyi nitelikleriyle överek yüceltme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övme sırasında kişi olumlu özellikleriyle söz içinde anılır."},{"boundary_match":"partial","distinction":"Odaktaki olumsuz kullanım arkadan kusur söylemeyle sınırlıdır; komşu daha geniş yerme ve saldırı davranışlarını içerir.","focus_only":"Odak tarafsız ve olumlu sözle anmayı da kapsayan daha geniş bir eylemdir.","gloss":"kusurla anma ile yerme","neighbor_only":"Komşu kusur arama, küçümseme ve gizli ya da açık saldırı yollarını içerir.","neighbor_ref":"root_001376/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir kişiyi kusurları üzerinden söz konusu etme bağlamında örtüşebilir."},{"boundary_match":"partial","distinction":"Hatırlama zihinsel bir durum veya süreçtir; sözle anma ise dışa vurulan dilsel eylemdir.","focus_only":"Odak içeriğin dil aracılığıyla dışa vurulmasını gerektirir.","gloss":"sözle anma ile hatırlama","neighbor_only":"Komşu içerik söylenmese bile onun zihinde korunması veya geri çağrılmasıdır.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyi hatırlamak, onun daha sonra sözle anılmasına eşlik edebilir."},{"boundary_match":"partial","distinction":"Odak tekil dilsel eylemdir; komşu bu tür anmaların toplumsal sonucu olan kalıcı itibardır.","focus_only":"Odak bir kişi veya şeyden söz etme eylemini anlatır.","gloss":"anma eylemi ile iyi ün","neighbor_only":"Komşu sürekli ve olumlu anılmanın doğurduğu iyi ün, onur ve saygınlığı anlatır.","neighbor_ref":"root_000516/B007","relation_type":"near_neighbor","shared_zone":"Bir kişinin toplum içinde anılması onun ününün oluşmasına katkı sağlayabilir."}],"source_phrase_ar":"ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)","source_summary":"Kaynaklar bir şeyin dilde söz olarak geçirilmesini ortak çekirdek sayar; insanları kusurlarıyla anmayı ise bağlama bağlı olumsuz bir kullanım olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ذكر الشيء باللسان والقول والإظهار والتسمية، ومنه ذكر الناس بخير أو بسوء إذا دل السياق.","what_is_not_ar":"لا يدخل فيه الحفظ القلبي وحده ولا الشرف والصيت الناتج عن الذكر."},"support_links":["sup_794f6a786906a37b4af1"]},{"boundary":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"Tanrı'yı kulluk amacıyla anma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanrı'ya yönelen yakarış, övgü, şükür, itaat ve dinî okuma eylemlerini ortak bir kulluk kavramında toplar.","boundary_detail":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_image_ar":"ذكر الله عبادة وثناء ودعاء","concept_gloss":"Tanrı'yı kulluk amacıyla anma","contextual_glosses":[{"applicability":"Tanrı'ya bilinçli biçimde yönelen övgü, yakarış veya kulluk eylemi genel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruklara uyma ve dinî metin okuma gibi davranışsal gerçekleşmeleri açıkça belirtmez.","preserves":"Tanrı'ya yönelen bilinçli anma ve kulluk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"Tanrı'yı anmak","usage_role":"general"},{"applicability":"Kulluğun sözlü yakarış, övgü ve yüceltme yönü bağlamda baskın olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şükretme, itaat ve dinî okuma gibi öteki gerçekleşmeleri kapsamaz.","preserves":"Yakarış, övgü ve yüceltme biçimindeki kulluk eylemlerini korur."},"facet_ids":["F002"],"text":"yakarışta ve övgüde bulunmak","usage_role":"contextual"}],"definition":"Tanrı'yı kulluk amacıyla anmak; ona yönelen yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma eylemlerini yerine getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."},{"facet_id":"F003","role":"extension","statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}],"identity_rationale":"Kaynak ifadesi Tanrı'yı anmaya yönelen kulluk eylemlerini; yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma örnekleriyle açıklar. Geçici çerçeve bu ibadet odaklı kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı'yı kulluk, övgü ve yakarışla anma"}],"lexicalization_note":"Genel kulluk anlamı ile Tanrı'yı anma söz öbeği ayrılır; dinî metin okuma ancak bu kulluk yönelimi içinde değerlendirilir.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; genel anma, belirli yakarışlar ve ibadet sessizliğiyle ilgili dört ilişki seçildi, kalan adaylar aynı sahnenin daha uzak parçalarıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel sözle anma yalnız dilsel eylemdir; odak dalı ise belirli bir yöneliş ve kulluk amacı gerektirir.","focus_only":"Odak Tanrı'ya yönelmiş kulluk, yakarış, övgü ve itaat koşulunu taşır.","gloss":"kulluk amacıyla anma ile sözle anma","neighbor_only":"Komşu herhangi bir kişi, nesne veya konuyu söz içinde anmayı kapsar.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Tanrı'yı sözle anma, her iki dalın kesişebildiği bir gerçekleşmedir."},{"boundary_match":"thematic_only","distinction":"Belirli kabul dileği kendi kalıplaşmış işlevine sahiptir; odak ise tek bir söz kalıbına bağlı olmayan geniş kulluk alanıdır.","focus_only":"Odak çok sayıda sözlü ve davranışsal kulluk biçimini kapsar.","gloss":"genel kulluk ile kabul dileği","neighbor_only":"Komşu yakarışın kabulü için söylenen belirli bir karşılıkla sınırlıdır.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal yakarış ve dinsel söz eylemi bağlamında aynı sahnede yer alabilir."},{"boundary_match":"thematic_only","distinction":"Komşu isteğin konusunu su ve yağmurla sınırlar; odak ise konu sınırlaması olmayan kulluk yönelimidir.","focus_only":"Odak övgü, şükür, itaat ve farklı yakarış türlerini birlikte kapsar.","gloss":"kulluk ile yağmur dileği","neighbor_only":"Komşu özellikle su ve yağmur istemeye yönelik yakarıştır.","neighbor_ref":"root_000722/B006","relation_type":"thematic","shared_zone":"Yağmur isteme eylemi Tanrı'ya yönelen bir yakarış olarak odak alanında gerçekleşebilir."},{"boundary_match":"thematic_only","distinction":"Sessizlik ibadetin düzenleyici bir koşuludur; odak ise Tanrı'ya yönelen anma ve kulluk eyleminin kendisidir.","focus_only":"Odak anma, yakarış, övgü, okuma ve itaat gibi etkin kulluk biçimleridir.","gloss":"kulluk eylemi ile ibadet sessizliği","neighbor_only":"Komşu ibadet sırasında sıradan konuşmayı bırakıp susma davranışıdır.","neighbor_ref":"root_001260/B004","relation_type":"thematic","shared_zone":"İki dal aynı ibadet ortamında birlikte bulunabilir."}],"source_phrase_ar":"الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)","source_summary":"Kaynaklar Tanrı'yı anmayı ibadet, yakarış ve övgü ekseninde birleştirir; yüceltme, şükretme, itaat ve dinî metin okumayı bu yönelimin farklı gerçekleşmeleri sayar.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الصلاة والدعاء والثناء والتسبيح والشكر والطاعة وقراءة القرآن من حيث هي ذكر لله.","what_is_not_ar":"لا يدخل فيه كل ذكر لساني عام ولا الكتاب المسمى ذكرا إلا من جهة القراءة والعبادة."},"support_links":[]},{"boundary":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_kind":"bare","branch_ref":"root_000516/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"indirildiğine inanılan kutsal kitap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinin hükümlerini içeren peygamber kitabı genel bir tür olarak anlatılırken kullanılır.","boundary_detail":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_image_ar":"الذكر كتاب منزل أو كتاب دين","concept_gloss":"indirildiğine inanılan kutsal kitap","contextual_glosses":[{"applicability":"Bağlam kitabın dini ve vahyedilmiş niteliğini zaten açıkça gösterdiğinde doğal kısa karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Peygambere indirilme ve önceki kitapları kapsayan üst ad olma ayrıntısını açıkça belirtmez.","preserves":"Dini içerikli ve kutsal kabul edilen kitap olma çekirdeğini korur."},"facet_ids":["F001"],"text":"kutsal kitap","usage_role":"general"}],"definition":"Dinin hükümlerini ve açıklamalarını içeren, bir peygambere indirildiğine inanılan kutsal kitaptır. Kapsam hem Kur'an'ı hem de daha önceki kutsal kitapları içine alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."},{"facet_id":"F002","role":"extension","statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}],"identity_rationale":"Kaynak ifadesi dini açıklayan kitabı, peygamberlere indirildiğine inanılan kitapları, Kur'an'ı ve önceki kutsal kitapları aynı dalda toplar. Geçici çerçeve metinsel nesneyi doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dinin ayrıntılarını bildiren kutsal kitap"}],"lexicalization_note":"Tanım yalın dalın kutsal kitap anlamını verir; okuma veya ibadetle ilgili söz öbeklerinden yeni bir genel anlam aktarılmaz.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; kitap bölümü, okuma ve çalışmayla ilgili üç sınır seçildi, öteki adaylar ad, görünme, kulluk veya gizli haber alanlarında uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütün kitap veya kitap türünü, komşu ise onun çevrelenmiş bölümünü adlandırır.","focus_only":"Odak kutsal kitabın bütünü veya kutsal kitap türüdür.","gloss":"kutsal kitap ile kitap bölümü","neighbor_only":"Komşu kutsal metnin sınırları belirlenmiş bir bölümü ve ayrıca yüksek konum anlamıdır.","neighbor_ref":"root_000758/B003","relation_type":"near_neighbor","shared_zone":"Kutsal kitabın belirli bölümleri, bütün metnin yapısal parçalarıdır."},{"boundary_match":"thematic_only","distinction":"Kitap bir nesnedir; okuma ise yalnız kutsal kitaplarla sınırlı olmayan bir eylemdir.","focus_only":"Odak okunan kutsal metinsel nesnenin kendisidir.","gloss":"kutsal kitap ile okuma","neighbor_only":"Komşu metni sesli veya sessiz okuma, başkasına okutma ve birlikte çalışma eylemleridir.","neighbor_ref":"root_001210/B002","relation_type":"thematic","shared_zone":"Kutsal kitap, okuma eyleminin önemli bir nesnesi olabilir."},{"boundary_match":"thematic_only","distinction":"Odak metinsel nesnedir; komşu farklı kitaplara da uygulanabilen öğrenme etkinliğidir.","focus_only":"Odak dini içeriği taşıyan kitabın kendisini adlandırır.","gloss":"kutsal kitap ile metin çalışması","neighbor_only":"Komşu bir kitabı okuyup yineleyerek öğrenme ve belleğe yerleştirme sürecidir.","neighbor_ref":"root_000470/B002","relation_type":"thematic","shared_zone":"Kutsal kitap üzerinde okuma ve öğrenme çalışması yapılabilir."}],"source_phrase_ar":"الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)","source_summary":"Kaynaklar dini açıklayan peygamber kitaplarını ortak çekirdek olarak verir ve kapsamı Kur'an ile önceki kutsal kitaplara kadar genişletir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الكتاب الذي فيه تفصيل الدين وكل كتاب للأنبياء والقرآن والكتب المتقدمة.","what_is_not_ar":"لا يدخل فيه فعل التذكر ولا مطلق الصلاة والدعاء إلا إذا كان اللفظ يدل على الكتاب أو القرآن."},"support_links":[]},{"boundary":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"onur, iyi ün ve saygınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin olumlu tanınması ile toplumsal yüksekliğini birlikte anlatmak gereken bağlamlarda kullanılır.","boundary_detail":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_image_ar":"ذكر المرء شرف وصيت","concept_gloss":"onur, iyi ün ve saygınlık","contextual_glosses":[{"applicability":"Kişinin insanlar arasında olumlu biçimde tanınıp anılması bağlamda öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüksek konum ve onur bileşenini tek başına açıkça belirtmez.","preserves":"Olumlu tanınma ve insanlar arasında yayılan övgü yönünü korur."},"facet_ids":["F002"],"text":"iyi ün","usage_role":"general"},{"applicability":"Toplumdaki yüksek değer ve itibar, yaygın tanınmadan daha önemli olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adının yayılması ve övgüyle anılması yönünü açıkça kapsamaz.","preserves":"Kişinin yüksek toplumsal değeri ve saygınlığı anlamını korur."},"facet_ids":["F001"],"text":"onur ve saygınlık","usage_role":"contextual"}],"definition":"Bir kişinin insanlar arasında olumlu biçimde tanınmasından doğan iyi ün, onur, övgü ve yüksek saygınlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."},{"facet_id":"F002","role":"core","statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}],"identity_rationale":"Kaynak ifadesi bir kişinin toplum içindeki yüksek konumunu, iyi ününü, övgüyle anılmasını ve saygınlığını ortak bir sonuç alanında toplar. Geçici çerçeve bu toplumsal değer ve yayılmış tanınma bileşimini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"onur, iyi ün ve övgü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Yalın iyi ün ve onur anlamı korunur; kişi niteleyen söz öbeği bellek gücü ile iyi anılmayı kendi bağlamında birleştirir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; iyi ün, güzel anılma, yüce saygınlık, tanınmışlık ve övgüyle ilgili beş sınır seçildi, kalan adaylar daha dar statü türleri veya kardeş dallardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu yayılan iyi üne daha dardır; odak bu üne onur ve toplumsal yükseklik bileşenini de ekler.","focus_only":"Odak iyi üne ek olarak onur ve yüksek toplumsal konumu da kapsar.","gloss":"onurlu ün ile iyi ün","neighbor_only":"Komşu özellikle insanlar arasında yayılmış güzel ve olumlu ünle sınırlıdır.","neighbor_ref":"root_000890/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin insanlar arasında olumlu biçimde tanınıp anılmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu güzel söz ve övgü sonucuna daha yakındır; odak bunun yanında onur ve yüksek konumu da kurucu sayar.","focus_only":"Odak kişinin yüksek konumunu ve saygınlığını da içerir.","gloss":"saygınlık ile güzel anılma","neighbor_only":"Komşu kişinin insanlar arasında güzel sözle anılması ve övülmesine odaklanır.","neighbor_ref":"root_000804/B004","relation_type":"near_synonym","shared_zone":"İki dal olumlu anılma ve iyi ün alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak iyi anılma ve ünle bağlantılıdır; komşu ün bulunmasa da büyüklük ve otoriteyi ifade edebilir.","focus_only":"Odak yaygın olumlu anılma ve iyi ün bileşenini taşır.","gloss":"iyi ün ile yüce saygınlık","neighbor_only":"Komşu kutsallık, büyüklük, önderlik ve görüş üstünlüğü gibi ek toplumsal boyutlar içerir.","neighbor_ref":"root_001029/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin toplumdaki onur ve yüksek değerini anlatabilir."},{"boundary_match":"partial","distinction":"Tanınmışlık değer bakımından yansız olabilir; odak dalı ise olumlu değerlendirme ve onur taşır.","focus_only":"Odak ünün olumlu, övgüye değer ve onurlu olmasını gerektirir.","gloss":"iyi ün ile tanınmışlık","neighbor_only":"Komşu bir topluluğun veya kişinin olumlu ya da olumsuz değer belirtilmeden tanınır hale gelmesini anlatabilir.","neighbor_ref":"root_000500/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir adın insanlar arasında yayılması ve tanınması alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu bir söz eylemi, odak ise bu ve benzeri değerlendirmelerin toplumsal sonucu olan itibardır.","focus_only":"Odak kişinin kazandığı kalıcı iyi ün ve toplumsal değerdir.","gloss":"iyi ün ile övme","neighbor_only":"Komşu kişiyi iyi özellikleriyle övme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övgü eylemi kişinin iyi ününün oluşmasına veya güçlenmesine katkı verebilir."}],"source_phrase_ar":"الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)","source_summary":"Kaynaklar onur ve yüksek konumu, insanlar arasında yayılan iyi ün ve övgüyle birlikte tek bir olumlu toplumsal itibar alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الشرف والعلاء والصيت والثناء وحسن الذكر.","what_is_not_ar":"لا يدخل فيه مجرد التلفظ باسم الشيء ولا الذكر بمعنى الكتاب إلا إذا صرح بالشرف أو الصيت."},"support_links":[]},{"boundary":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000516/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"hakkı gösteren yazılı belge","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hakkın yazıyla kayda geçirildiği belgeyi veya bu belgelerin çoğulunu açıklarken kullanılır.","boundary_detail":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_image_ar":"ذكر الحق صك ووثيقة حق","concept_gloss":"hakkı gösteren yazılı belge","contextual_glosses":[{"applicability":"Bağlam belgenin yazılı olduğunu açıkça gösterdiğinde kısa ve doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yazılı olma niteliğini ve çoğul biçimin tarihsel yapısını açıkça belirtmez.","preserves":"Belgenin belirli bir hakkı gösterme ve kanıtlama işlevini korur."},"facet_ids":["F001"],"text":"hak belgesi","usage_role":"general"},{"applicability":"Birden çok hakkı veya birden çok yazılı kanıtı topluca adlandıran çoğul yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekil belge kullanımını dışarıda bırakır.","preserves":"Birden çok yazılı hak belgesinin topluca adlandırılmasını korur."},"facet_ids":["F002"],"text":"hak belgeleri","usage_role":"contextual"}],"definition":"Bir hakkın varlığını, sahibini veya koşullarını yazılı olarak gösteren belge ve bu tür belgelerin çoğul adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."},{"facet_id":"F002","role":"extension","statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}],"identity_rationale":"Kaynak ifadesi yalnız belirli hak söz öbeğinde bir hakkı kayda geçiren yazılı belgeyi ve bu belgelerin çoğulunu verir. Geçici çerçeve yapıya bağlı belge anlamını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakkı gösteren yazılı belge"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yazılı hak belgeleri"}],"lexicalization_note":"Tanım yalnız hak belgesi yapısına ve onun çoğul biçimine bağlanır; yalın köke genel belge anlamı yüklenmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; eş belge, geniş kayıt, genel yazılı kâğıt, hakkın kendisi ve vasiyetle ilgili beş sınır seçildi, kalan adaylar yazma eylemi, pay veya kardeş anlamlarda daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belgenin belirli bir hakkı göstermesini gerektirir; komşu ise bu koşul olmadan daha genel yazılı belgeleri de kapsar.","focus_only":"Odak yalnız bir hakkı gösteren yazılı belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile yazılı senet","neighbor_only":"Komşu hak bağlantısı zorunlu olmadan yazılı kitap veya senetleri kapsar.","neighbor_ref":"root_000874/B006","relation_type":"near_synonym","shared_zone":"İki dal yazılı senet veya belgeyi adlandırdıklarında örtüşür."},{"boundary_match":"partial","distinction":"Odak hak belgesine daralır; komşu belge türlerini ve resmi kayıt eylemini daha geniş biçimde kapsar.","focus_only":"Odak özellikle bir hakkı gösteren belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile resmi kayıt","neighbor_only":"Komşu kayıt defteri, yükümlülük belgesi, yazılı sayfa ve yargıcın kayda geçirmesi gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000677/B004","relation_type":"near_synonym","shared_zone":"Her iki dal hakkı veya yükümlülüğü yazılı biçimde güvence altına alan belgeyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak hak ilişkisine bağlıdır; komşu daha genel yazılı nesneyi ve belge dışındaki pay anlamını da içerir.","focus_only":"Odak belgenin belirli bir hakkı kanıtlama işlevini zorunlu kılar.","gloss":"hak belgesi ile yazılı kâğıt","neighbor_only":"Komşu yazılı belge yanında ayrılmış pay ve ödül gibi belge dışı anlamlara da uzanır.","neighbor_ref":"root_001239/B002","relation_type":"near_synonym","shared_zone":"İki dal yazılı bir belge veya kayıt nesnesini adlandırabilir."},{"boundary_match":"field_only","distinction":"Hak hukuki veya toplumsal ilişkidir; belge ise o ilişkinin varlığını gösteren ayrı bir nesnedir.","focus_only":"Odak hakkı kanıtlayan yazılı belgedir.","gloss":"hak belgesi ile hakkın kendisi","neighbor_only":"Komşu kişinin sahip olduğu hakkın veya hak iddiasının kendisidir.","neighbor_ref":"root_000347/B003","relation_type":"same_field","shared_zone":"Belge, kişinin sahip olduğu hakkı kayda geçirir ve kanıtlar."},{"boundary_match":"partial","distinction":"Odak bir hakkı kanıtlar; komşu ise bir kişiye yapılacak işi önceden bildirip emanet eder.","focus_only":"Odak mevcut bir hakkı gösteren yazılı kanıt işlevidir.","gloss":"hak belgesi ile yazılı vasiyet","neighbor_only":"Komşu gelecekte uyulması gereken buyruk veya görevi emanet eden vasiyet ve talimattır.","neighbor_ref":"root_001055/B002","relation_type":"near_neighbor","shared_zone":"İki dal yükümlülük doğurabilen ve korunması gereken yazılı belgeler alanında buluşur."}],"source_phrase_ar":"ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)","source_summary":"Kaynaklar belirli hak söz öbeğini yazılı hak belgesi olarak açıklar ve çoğul biçimin birden çok hak belgesini gösterdiğinde birleşir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه ذكر الحق بمعنى الصك وجمعه ذكور حقوق أو ذكور حق.","what_is_not_ar":"لا يدخل فيه الكتاب الديني المسمى ذكرا ولا التذكرة العامة."},"support_links":[]},{"boundary":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B009","candidate_links":[{"candidate_id":"cand_5a7686b575e0b0d422af","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hatırlamayı doğuran eylemi, buna yarayan işaret veya nesneyi ve belirli biçime bağlı sık anmayı birlikte açıklamak gereken genel bağlamlarda kullanılır.","boundary_detail":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_image_ar":"الذكرى والتذكرة ما يذكّر","concept_gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","contextual_glosses":[{"applicability":"Bir kişide unutulmuş bilginin yeniden zihne gelmesini sağlayan eylem anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatıcı nesne ve sık anma yüzlerini dışarıda bırakır.","preserves":"Hatırlamayı başka bir kişide meydana getiren geçişli eylemi korur."},"facet_ids":["F001"],"text":"hatırlatmak","usage_role":"general"},{"applicability":"Bir ihtiyaç veya bilginin unutulmamasını sağlayan not, işaret ya da nesne anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatma eylemini ve sık anma yoğunluğunu kapsamaz.","preserves":"Hatırlamaya yarayan araç ve işaret işlevini korur."},"facet_ids":["F002"],"text":"hatırlatıcı","usage_role":"contextual"},{"applicability":"Kaynakta yoğunluk bildiren belirli ad biçimi bir şeyi çok kez anmayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına hatırlatma ve hatırlatıcı araç anlamlarını dışarıda bırakır.","preserves":"Bir şeyi çok ve yinelenen biçimde anma yoğunluğunu korur."},"facet_ids":["F003"],"text":"sıkça anma","usage_role":"explanatory"}],"definition":"Bir bilginin yeniden zihinde belirmesini sağlamak veya buna yarayan bir işaret ya da araç sunmaktır. Belirli bir biçim ayrıca bir şeyi sıkça anmayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."},{"facet_id":"F002","role":"specialization","statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."},{"facet_id":"F003","role":"source_variant","statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}],"identity_rationale":"Kaynak ifadesi yalnız hatırlatan bir nesneyi değil, başkasında hatırlamayı meydana getirme eylemini, hatırlamaya yarayan aracı ve bazı biçimlerde sık anmayı birlikte verir. Dal korunabilir, ancak geçici nesne merkezli çerçeve bu süreç ve yoğunluk yüzlerini açıkça kapsayacak biçimde genişletilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"hatırlatma, öğüt alma veya sıkça anma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"hatırlatıcı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"hatırlatma"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ona o şeyi hatırlattı"}],"lexicalization_note":"Hatırlatma eylemi, hatırlatıcı araç ve sık anma ayrı yüzler olarak tutulur; bu yapıların hiçbiri yalın zihinsel hatırlamayla özdeşleştirilmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; öğüt, uyarı, dikkat çekme, hatırlama ve sözle anmayla ilgili beş sınır seçildi, kalan adaylar öğretme, aktarma, yazı veya yergi alanlarında daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu ahlaki yönlendirme ve duygusal etki taşır; odak bunları gerektirmeyen genel hatırlatma alanıdır.","focus_only":"Odak her tür bilgiyi hatırlatabilir ve bir araç ya da işaret biçiminde gerçekleşebilir.","gloss":"genel hatırlatma ile öğüt","neighbor_only":"Komşu korkutma, sakındırma ve iyi sonuca yöneltme yoluyla kalbi etkileyen öğütle sınırlıdır.","neighbor_ref":"root_001663/B001","relation_type":"near_synonym","shared_zone":"Öğüt, kişiye unuttuğu değer veya sonucu yeniden hatırlatabilir."},{"boundary_match":"partial","distinction":"Uyarma risk ve sakınma yönelimi gerektirir; hatırlatma ise böyle bir değer ve tehlike koşulu taşımaz.","focus_only":"Odak tarafsız, olumlu veya olumsuz herhangi bir bilgiyi yeniden zihne getirebilir.","gloss":"hatırlatma ile uyarma","neighbor_only":"Komşu kişide tehlikeye karşı dikkat ve sakınma meydana getirmeyi amaçlar.","neighbor_ref":"root_000301/B002","relation_type":"near_neighbor","shared_zone":"Bir tehlikeyi hatırlatmak aynı zamanda kişinin dikkatli olmasını sağlayabilir."},{"boundary_match":"partial","distinction":"Komşu soru ve bilgi isteme işlevi taşır; odak ise önceden bilinen içeriğin yeniden hatırlanmasını hedefler.","focus_only":"Odak önceden bilinen bir içeriği yeniden zihne getirmeyi sağlar.","gloss":"hatırlatma ile dikkat çekme","neighbor_only":"Komşu karşıdakinin dikkatini çekip ondan bilgi istemeye yarayan bir söyleyiş kalıbıdır.","neighbor_ref":"root_000531/B013","relation_type":"near_neighbor","shared_zone":"Dikkat çekme, dinleyiciyi belirli bir konuya zihinsel olarak yöneltebilir."},{"boundary_match":"partial","distinction":"Odak sonuç doğuran uyarıcı eylem veya araçtır; komşu ise ortaya çıkan zihinsel durum ve süreçtir.","focus_only":"Odak hatırlamayı meydana getiren dış veya geçişli neden ile aracı anlatır.","gloss":"hatırlatma ile hatırlama","neighbor_only":"Komşu kişinin zihninde bilginin korunması veya yeniden bulunması sürecidir.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"İki dal unutulmuş bilginin yeniden zihinde hazır bulunması sonucunda birleşir."},{"boundary_match":"partial","distinction":"Sözle anma dilsel biçimi gerektirir fakat hatırlatma amacı taşımaz; odak farklı araçlarla gerçekleşebilir ve hatırlama sonucu hedefler.","focus_only":"Odak sözlü olmak zorunda değildir ve temel işlevi bilgiyi yeniden zihne getirmektir.","gloss":"hatırlatma ile sözle anma","neighbor_only":"Komşu belirli bir kişi veya şeyi söz içinde adlandırıp konu etmektir.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Bir şeyi sözle anmak dinleyene o şeyi hatırlatabilir."}],"source_phrase_ar":"الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)","source_summary":"Kaynaklar hatırlatmayı başkasında hatırlama meydana getiren geçişli eylem ve hatırlamaya yarayan araç olarak verir; ayrıca belirli biçimde sık anma yoğunluğunu kaydeder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكرى والتذكير والتذكرة وما يجعل الشيء مذكورا أو يعيد حضوره.","what_is_not_ar":"لا يدخل فيه نفس الحفظ القلبي إلا من حيث النتيجة، ولا الذكر بمعنى الذكران والذكورة."},"support_links":["sup_eac07b67ab1c5672afcd"]}],"candidate_inventory":[{"anchor_refs":["88:21:1"],"branch_refs":[],"candidate_id":"cand_ea65d8f1b411ca52f572","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:1:boundary-synthesis","source_type":"word_analysis","support_ids":["sup_1f43295ed9d2a8d0a587","sup_5d8c4488884cdb0175c3"],"title":"boundary bridge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:1","qac_refs":["88:21:1:1"],"status":"accepted"}},{"anchor_refs":["88:21:1"],"branch_refs":[],"candidate_id":"cand_3b07052270308aad3090","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:1:consequence-resumption","source_type":"word_analysis","support_ids":["sup_5d8c4488884cdb0175c3","sup_de972e91bcb55a9537ca"],"title":"consequence and resumption together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:1","qac_refs":["88:21:1:1"],"status":"accepted"}},{"anchor_refs":["88:21:1"],"branch_refs":[],"candidate_id":"cand_3cb14cddc169fefa32b4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:1:fused-command-surface","source_type":"word_analysis","support_ids":["sup_48a195cf44689739f7fe","sup_5d8c4488884cdb0175c3"],"title":"fused launch into command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:1","qac_refs":["88:21:1:1"],"status":"accepted"}},{"anchor_refs":["88:21:1"],"branch_refs":[],"candidate_id":"cand_c6c0ee79588745e8c133","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:1:visual-display-to-duty","source_type":"word_analysis","support_ids":["sup_09c43a656a5f7e0f9f94","sup_5d8c4488884cdb0175c3"],"title":"display turns into duty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:1","qac_refs":["88:21:1:1"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_d7ffdb8103ad0f7cb97d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:act-to-role-echo","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_f40715b56a511e9d5d7d"],"title":"command echoed as role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_74a74b54f2043e47feed","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:bounded-office-synthesis","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_d9be88ed18206034e26b"],"title":"bounded reminder office","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_bb6de05beb305d12646f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:command-before-restriction","source_type":"word_analysis","support_ids":["sup_4b8cc072a9d44d4c61e1","sup_ac4a1b0dff6332d2556d"],"title":"duty before limit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_5f7fafe00166920c2341","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:command-sound-pressure","source_type":"word_analysis","support_ids":["sup_622d0d4c3b9d02a69e6b","sup_ac4a1b0dff6332d2556d"],"title":"crisp doubled command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_02578dd77391e0f53ed2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:common-root-local-slot","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_b040a0f56be3fe6fcb51"],"title":"common root in a narrow slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_04183a457a2cd3aaef31","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:delivery-not-uptake","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_edbe63e352c356a0dae5"],"title":"delivery not uptake","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_85f1af9c9a387c772687","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:form-ii-reminder-agency","source_type":"word_analysis","support_ids":["sup_a832c333f26398213bf2","sup_ac4a1b0dff6332d2556d"],"title":"Form II reminder agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_b8b0d7d3a358bb0e1ee6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:intertext-command-frames","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_fff0b17bde9abde693c5"],"title":"same command different frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_79c0b9767b0626ad55f2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:objectless-imperative","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_e733020a4464cf56b1bd"],"title":"objectless imperative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_94fa7879ca2c4616600f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:observation-becomes-reminder","source_type":"word_analysis","support_ids":["sup_ac4a1b0dff6332d2556d","sup_f31896238d6748695b55"],"title":"failed seeing becomes prompting","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:2"],"branch_refs":[],"candidate_id":"cand_f720729712512c6b24c2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:2:reminder-field","source_type":"word_analysis","support_ids":["sup_95f29fc3f443edc6b53c","sup_ac4a1b0dff6332d2556d"],"title":"mention and memory joined","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:2","qac_refs":["88:21:1:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_4507f5734f1c5b470014","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:action-to-role-pivot","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_f11c59c0ed356376b760"],"title":"imperative becomes role boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_802be078b050c4fb3eac","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:duty-and-limit-two-way-reading","source_type":"word_analysis","support_ids":["sup_27740e9be7fe9627cad4","sup_2f4511b98ed33aed0175"],"title":"duty and limit together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_50185aa15011a856fe13","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:echo-and-forward-negation","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_374d68176a73e9348dec"],"title":"restriction prepares denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_7da1b4e0e31582d9dd3d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:emphatic-limitation","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_e3e36da88b6c12e4fde0"],"title":"limit without devaluing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_4c3deb67625cf083a8c0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:fused-particle-reparse","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_cb469fb8e264aacf9baa"],"title":"fused restrictive token","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_b29475e5324344caebc8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:restrictive-clause-cadence","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_f726541b45adcbf6f5d0"],"title":"nasal clause binding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:3"],"branch_refs":[],"candidate_id":"cand_748ea964e07fc2bb8b5d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:3:restrictive-scope","source_type":"word_analysis","support_ids":["sup_2f4511b98ed33aed0175","sup_58dec66e9b4f39920ae5"],"title":"role under restriction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:3","qac_refs":["88:21:2:1","88:21:2:2"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_521257266a518d5d4553","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:detached-syntactic-body","source_type":"word_analysis","support_ids":["sup_9237ce534e39e41865df","sup_f3796991c2df595716e6"],"title":"separate syntactic body","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_6fd5233ba184144dadc2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:discourse-pivot","source_type":"word_analysis","support_ids":["sup_1373230b12ef7fe7d00d","sup_f3796991c2df595716e6"],"title":"observation to commission","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_6625eb7bcff4713715aa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:explicit-addressee-subject","source_type":"word_analysis","support_ids":["sup_4b3f3a61369517ea40ca","sup_f3796991c2df595716e6"],"title":"explicit addressed subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_f89cddea555b58d3c5a0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:focus-and-role-specification","source_type":"word_analysis","support_ids":["sup_b99567bece9a5f3adb4c","sup_f3796991c2df595716e6"],"title":"focused role bearer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_d9d1e07ee4d2d12d8ed7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:forward-continuity","source_type":"word_analysis","support_ids":["sup_76d1974e536aeef581fa","sup_f3796991c2df595716e6"],"title":"same person into denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_88938b1e7d24e1d7443b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:implicit-to-explicit-you","source_type":"word_analysis","support_ids":["sup_65c47e11d7f7e92dbfa5","sup_f3796991c2df595716e6"],"title":"hidden you made visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:4"],"branch_refs":[],"candidate_id":"cand_2ff71025ce926f8c8a2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:21:4:pronoun-sound-centering","source_type":"word_analysis","support_ids":["sup_01d4e683b773d386a722","sup_f3796991c2df595716e6"],"title":"sharp onset centers you","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:4","qac_refs":["88:21:3:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_7cb519b182fff21330e9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:active-not-passive-or-finite","source_type":"word_analysis","support_ids":["sup_45b5ca072d57b812c75b","sup_635e3fc399f981e6f1e3"],"title":"active role-bearer chosen","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_3916826081f0254d51d1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:agent-and-token-family","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_cb981fdb1a14a1aa5703"],"title":"agent and reminder-token family","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_c5234e8896f3e240df66","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:agent-not-controller","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_721cb0e89d5bf1677fb8"],"title":"agent not controller","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_e5661cbf25db8a2e5b41","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:command-to-role-principle","source_type":"word_analysis","support_ids":["sup_02180e75d26d7ad481f4","sup_635e3fc399f981e6f1e3"],"title":"act generalized into role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_fcb62245be35a7c6aca7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:convergent-final-mechanism","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_7f663119eca17243376d"],"title":"final mechanism gathered","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_56db3b35d1912370a235","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:final-predicate-landing","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_91ad7a03328f2718a957"],"title":"ending lands on role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_a8ec46173de36a074830","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:form-ii-active-participle","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_959fbec7dc3e797013b2"],"title":"durable causative reminder role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_7d79fccfb15d09e23a6a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:implied-recipients-not-domain","source_type":"word_analysis","support_ids":["sup_126415599b28a970172c","sup_635e3fc399f981e6f1e3"],"title":"recipients implied, not possessed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_234e9cc8e064999b8076","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:indefinite-classifying-role","source_type":"word_analysis","support_ids":["sup_1a36ab197b0271b7adf9","sup_635e3fc399f981e6f1e3"],"title":"classifying not sovereign title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_cc54f1e352fe19140cd0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:marked-role-form","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_7a7d9adf035ffaba0992"],"title":"marked role-form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_efe435d0814f0effc364","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:nasal-forward-contrast","source_type":"word_analysis","support_ids":["sup_3b3317e9e859ca1721f2","sup_635e3fc399f981e6f1e3"],"title":"nasal close into contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_c7c079a362fea5b41e91","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:positive-to-negative-boundary","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_9fba7dbdd3cc3d03d8f9"],"title":"positive role to negative exclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_620b44e68e5f9bf229d9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:predicate-of-anta","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_80b942a50d9e24ff27ac"],"title":"predicate of the addressee","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_e7b9fd1cb684f9b0f103","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:reminder-range-without-control","source_type":"word_analysis","support_ids":["sup_4da37725d76e571a3d60","sup_635e3fc399f981e6f1e3"],"title":"broad reminder, no control","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_5de949ffb1f5cde473e3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:root-echo-ring","source_type":"word_analysis","support_ids":["sup_22e083501ec8c515a2df","sup_635e3fc399f981e6f1e3"],"title":"act-to-agent root echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_464df0466f3357a3c7d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:sound-echo-closure","source_type":"word_analysis","support_ids":["sup_635e3fc399f981e6f1e3","sup_e2dec63b2ed79539fdd8"],"title":"audible sustained reminder","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:5"],"branch_refs":[],"candidate_id":"cand_8d42d311454bb050b875","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:5:tanwin-under-restriction","source_type":"word_analysis","support_ids":["sup_188d071c21225ace3eaf","sup_635e3fc399f981e6f1e3"],"title":"qualitative tanwīn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:21:5","qac_refs":["88:21:4:1"],"status":"accepted"}},{"anchor_refs":["88:21:1"],"branch_refs":[],"candidate_id":"cand_1f191110a9671e85f7cd","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000516"],"scope":"focus_ayah","source_local_id":"88:21:1:2","source_type":"qac_morpheme","support_ids":["sup_c3d23df57fde8bb8cdf3"],"title":"QAC root occurrence: ذ ك ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B003"],"candidate_id":"cand_227730f5b2234a388bf8","commentary_obligation":"review","hft_ref":"hft_1862119f38cca1d7de83","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_recall_reactivation","source_type":"hft","support_ids":["sup_5f8f0c276afcd187c3e7"],"title":"baseline_recall_reactivation","trust":"legacy_unbound"},{"anchor_refs":["88:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B004"],"candidate_id":"cand_74aca909adf4326c4f7d","commentary_obligation":"review","hft_ref":"hft_65498fdc495f7de61178","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_spoken_making_known","source_type":"hft","support_ids":["sup_794f6a786906a37b4af1"],"title":"baseline_spoken_making_known","trust":"legacy_unbound"},{"anchor_refs":["88:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B009"],"candidate_id":"cand_5a7686b575e0b0d422af","commentary_obligation":"review","hft_ref":"hft_3059ed98103f58b3eb17","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_reminder_medium","source_type":"hft","support_ids":["sup_eac07b67ab1c5672afcd"],"title":"baseline_reminder_medium","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:21:1:1","qac_word_ref":"88:21:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","root_ar":"ذ ك ر","surface_ar":"ذَكِّرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:21:2:1","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"88:21:2:2","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"88:21:3:1","qac_word_ref":"88:21:3","root_ar":"","surface_ar":"أَنتَ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","root_ar":"ذ ك ر","surface_ar":"مُذَكِّرٌ"}],"word_analysis_qac_refs":[["88:21:1:1"],["88:21:1:2"],["88:21:2:1","88:21:2:2"],["88:21:3:1"],["88:21:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:21:1","88:21:2","88:21:3","88:21:4","88:21:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:21:1:1","qac_word_ref":"88:21:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","root_ar":"ذ ك ر","surface_ar":"ذَكِّرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:21:2:1","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"88:21:2:2","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"88:21:3:1","qac_word_ref":"88:21:3","root_ar":"","surface_ar":"أَنتَ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","root_ar":"ذ ك ر","surface_ar":"مُذَكِّرٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:21:1:1"],["88:21:1:2"],["88:21:2:1","88:21:2:2"],["88:21:3:1"],["88:21:4:1"]],"word_analysis_refs":["88:21:1","88:21:2","88:21:3","88:21:4","88:21:5"],"word_rows":[{"analysis_record_ref":"88:21:1","analytic_gloss_range_en":"consequential or resumptive connector prefixed to the following command","analytic_root_gloss_range_en":null,"qac_refs":["88:21:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"88:21:2","analytic_gloss_range_en":"Form II imperative to cause reminder, with object and instrument unstated","analytic_root_gloss_range_en":"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; the local Form II command activates the reminder/admonitory speech branch","qac_refs":["88:21:1:2"],"root":{"arabic":"ذ ك ر","transliteration":"dh-k-r"},"surface":{"arabic":"ذَكِّرْ","transliteration":"dhakkir"}},{"analysis_record_ref":"88:21:3","analytic_gloss_range_en":"restrictive particle that places the following nominal clause under limitation","analytic_root_gloss_range_en":null,"qac_refs":["88:21:2:1","88:21:2:2"],"root":{},"surface":{"arabic":"إِنَّمَآ","transliteration":"innamā"}},{"analysis_record_ref":"88:21:4","analytic_gloss_range_en":"independent second-person masculine singular pronoun serving as subject of the restrictive nominal clause","analytic_root_gloss_range_en":null,"qac_refs":["88:21:3:1"],"root":{},"surface":{"arabic":"أَنتَ","transliteration":"anta"}},{"analysis_record_ref":"88:21:5","analytic_gloss_range_en":"Form II active participle: reminder-agent, predicate of the explicit addressee under restriction","analytic_root_gloss_range_en":"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; this active participle selects the reminder-agent role and excludes coercive control","qac_refs":["88:21:4:1"],"root":{"arabic":"ذ ك ر","transliteration":"dh-k-r"},"surface":{"arabic":"مُذَكِّرٌۭ","transliteration":"mudhakkirun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:21"],"branch_refs":["root_000516/B003"],"candidate_id":"cand_227730f5b2234a388bf8","evidence_scope":"focus_ayah","hft_ref":"hft_1862119f38cca1d7de83","item_id":"baseline_recall_reactivation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_recall_reactivation","support_id":"sup_5f8f0c276afcd187c3e7"},{"anchor_refs":["88:21"],"branch_refs":["root_000516/B004"],"candidate_id":"cand_74aca909adf4326c4f7d","evidence_scope":"focus_ayah","hft_ref":"hft_65498fdc495f7de61178","item_id":"baseline_spoken_making_known","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_spoken_making_known","support_id":"sup_794f6a786906a37b4af1"},{"anchor_refs":["88:21"],"branch_refs":["root_000516/B009"],"candidate_id":"cand_5a7686b575e0b0d422af","evidence_scope":"focus_ayah","hft_ref":"hft_3059ed98103f58b3eb17","item_id":"baseline_reminder_medium","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_reminder_medium","support_id":"sup_eac07b67ab1c5672afcd"}],"diagnostics":[],"lane_counts":{"global":15,"macro":6,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:21","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:21","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"88:21","lane":"micro","linguistic_source_ref":"88:21","surface_ref":"88:21","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:21","target_tokens":[["O",["88:21:1"]],["halde",["88:21:1"]],["hatırlat",["88:21:1"]],["sen",["88:21:3"]],["yalnızca",["88:21:2"]],["hatırlatansın",["88:21:4"]]],"text":"O halde hatırlat; sen yalnızca hatırlatansın."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:pronoun-sound-centering","source_type":"word_analysis","support_id":"sup_01d4e683b773d386a722","text":"{\"blocking_evidence\":null,\"headline\":\"sharp onset centers you\",\"reader_payoff\":\"The reader hears the restrictive clause catch on the addressed person before the predicate lands.\",\"reason\":\"The sound row fits the local word order: the pronoun stands between the restrictive particle and the predicate.\",\"representative_source_ids\":[\"QP-f85a39a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:command-to-role-principle","source_type":"word_analysis","support_id":"sup_02180e75d26d7ad481f4","text":"{\"blocking_evidence\":null,\"headline\":\"act generalized into role\",\"reader_payoff\":\"The reader sees the specific order become a general mission boundary at the end of the ayah.\",\"reason\":\"The final predicate closes the restrictive nominal clause that explains the preceding imperative.\",\"representative_source_ids\":[\"QT-54d29182\",\"QT-6243c4c7\",\"QT-b041fe9a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:1:visual-display-to-duty","source_type":"word_analysis","support_id":"sup_09c43a656a5f7e0f9f94","text":"{\"blocking_evidence\":null,\"headline\":\"display turns into duty\",\"reader_payoff\":\"The reader notices that the prior inspection of camel, sky, mountains, and earth becomes an obligation to remind.\",\"reason\":\"The connector opens 88:21 and attaches directly to the imperative clause, so the preceding evidentiary display can function as the command's immediate discourse ground.\",\"representative_source_ids\":[\"QT-7c818f3e\",\"QT-c0e5d251\",\"QB-907956d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:implied-recipients-not-domain","source_type":"word_analysis","support_id":"sup_126415599b28a970172c","text":"{\"blocking_evidence\":null,\"headline\":\"recipients implied, not possessed\",\"reader_payoff\":\"The reader sees those reminded as implied recipients without turning them into a domain of coercive control.\",\"reason\":\"The noun instance has no overt complement, while 88:22 names the group over whom control is denied.\",\"representative_source_ids\":[\"QG-efad9bdb\",\"QS-0509df1f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:discourse-pivot","source_type":"word_analysis","support_id":"sup_1373230b12ef7fe7d00d","text":"{\"blocking_evidence\":null,\"headline\":\"observation to commission\",\"reader_payoff\":\"The reader feels the discourse axis shift from those being asked to look to the addressee being commissioned to remind.\",\"reason\":\"The preceding sequence addresses observation, while this nominal clause explicitly centers the commissioned second-person addressee.\",\"representative_source_ids\":[\"QI-5fd96d4b\",\"QB-ac4737bd\",\"QB-bfd2772d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:tanwin-under-restriction","source_type":"word_analysis","support_id":"sup_188d071c21225ace3eaf","text":"{\"blocking_evidence\":null,\"headline\":\"qualitative tanwīn\",\"reader_payoff\":\"The reader sees the noun-form remain qualitative while exclusivity comes from the particle rather than from a named title.\",\"reason\":\"The predicate is indefinite nominative, and the restriction is supplied by {{ar:إِنَّمَآ}} ({{tr:innamā}}).\",\"representative_source_ids\":[\"QF-caa8e2ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:indefinite-classifying-role","source_type":"word_analysis","support_id":"sup_1a36ab197b0271b7adf9","text":"{\"blocking_evidence\":null,\"headline\":\"classifying not sovereign title\",\"reader_payoff\":\"The reader notices that the tanwīn classifies the addressee by reminder-function rather than installing a sovereign title.\",\"reason\":\"QAC and noun-instance evidence identify an indefinite nominative active participle predicate under {{ar:إِنَّمَآ}} ({{tr:innamā}}).\",\"representative_source_ids\":[\"QG-1bb1ddb5\",\"MG-be7bff81\",\"QF-94d189ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:1:boundary-synthesis","source_type":"word_analysis","support_id":"sup_1f43295ed9d2a8d0a587","text":"{\"blocking_evidence\":null,\"headline\":\"boundary bridge\",\"reader_payoff\":\"The reader follows the discourse boundary where observation stops being scenery and becomes addressed responsibility.\",\"reason\":\"The particle begins the new imperative clause after the inspection sequence, allowing bridge, launch, and command-prefix functions to converge.\",\"representative_source_ids\":[\"QB-832c32e0\",\"QB-9ba8f86a\",\"QY-afd1aed8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:root-echo-ring","source_type":"word_analysis","support_id":"sup_22e083501ec8c515a2df","text":"{\"blocking_evidence\":null,\"headline\":\"act-to-agent root echo\",\"reader_payoff\":\"The reader hears the command's root return as the closing agent noun, making the line explain itself by repetition with changed morphology.\",\"reason\":\"Both the imperative {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) and the predicate {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) align to {{ar:ذ ك ر}} ({{tr:dh-k-r}}), but they occupy different grammatical roles.\",\"representative_source_ids\":[\"QE-24fda77b\",\"QE-6be66608\",\"QE-8a031836\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:duty-and-limit-two-way-reading","source_type":"word_analysis","support_id":"sup_27740e9be7fe9627cad4","text":"{\"blocking_evidence\":null,\"headline\":\"duty and limit together\",\"reader_payoff\":\"The reader keeps both directions of the verse together: the command requires action, and the restriction defines its limit.\",\"reason\":\"The verbal command and the following restrictive nominal explanation are both strongly licensed in the attachment evidence.\",\"representative_source_ids\":[\"QY-e0be7fce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3","source_type":"word_analysis","support_id":"sup_2f4511b98ed33aed0175","text":"{\"gloss_range\":\"restrictive particle that places the following nominal clause under limitation\",\"prose\":\"{{ar:إِنَّمَآ}} ({{tr:innamā}}) is the ayah's boundary operator. It takes the following nominal clause, {{ar:أَنتَ مُذَكِّرٌۭ}} ({{tr:anta mudhakkirun}}), as a restricted role statement: the addressee is defined by reminder, not by control over response, and the restriction targets his function rather than denying that anyone else can remind. Its force is not to make reminder small, because {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) has already been commanded; it makes the duty emphatically limited. The fused particle prevents reading the wording as ordinary emphasis plus a separate particle, and its placement after the imperative lets the ayah move from action to authorized identity. Its nasal cadence also binds the pronoun-predicate clause as one continuous role-boundary after the sharper command. That positive restriction prepares the explicit negation of control in 88:22.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّمَآ}} ({{tr:innamā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:echo-and-forward-negation","source_type":"word_analysis","support_id":"sup_374d68176a73e9348dec","text":"{\"blocking_evidence\":null,\"headline\":\"restriction prepares denial\",\"reader_payoff\":\"The reader sees the positive role limit in 88:21 setting up the explicit denial of control in 88:22.\",\"reason\":\"{{ar:إِنَّمَآ}} ({{tr:innamā}}) restricts the repeated reminder predicate in 88:21, and the next ayah states the excluded role directly in 88:22.\",\"representative_source_ids\":[\"QE-7aeacb79\",\"QB-6b67221a\",\"QY-46c1472a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:nasal-forward-contrast","source_type":"word_analysis","support_id":"sup_3b3317e9e859ca1721f2","text":"{\"blocking_evidence\":null,\"headline\":\"nasal close into contrast\",\"reader_payoff\":\"The reader hears the indefinite close anticipate the next ayah's contrasted role ending in 88:22.\",\"reason\":\"The row gives a local sound bridge from {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) to the role denial in 88:22.\",\"representative_source_ids\":[\"QP-6a8f466e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:active-not-passive-or-finite","source_type":"word_analysis","support_id":"sup_45b5ca072d57b812c75b","text":"{\"blocking_evidence\":null,\"headline\":\"active role-bearer chosen\",\"reader_payoff\":\"The reader sees the addressee named as one who causes remembrance, not as something remembered or as merely performing an ongoing verb.\",\"reason\":\"The local form is an active participle noun, not a passive participle or finite imperfect verb.\",\"representative_source_ids\":[\"QF-cff17517\",\"QF-fb60075d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:1:fused-command-surface","source_type":"word_analysis","support_id":"sup_48a195cf44689739f7fe","text":"{\"blocking_evidence\":null,\"headline\":\"fused launch into command\",\"reader_payoff\":\"The reader hears the connector and the imperative as a compressed launch, with transition and pressure joined at the surface.\",\"reason\":\"The bundle segmentation splits the particle from the verb, while the local verb instance records the fused surface {{ar:فَذَكِّرْ}} ({{tr:fa-dhakkir}}).\",\"representative_source_ids\":[\"QF-d84f0635\",\"QP-706f442f\",\"QP-f78ac796\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:explicit-addressee-subject","source_type":"word_analysis","support_id":"sup_4b3f3a61369517ea40ca","text":"{\"blocking_evidence\":null,\"headline\":\"explicit addressed subject\",\"reader_payoff\":\"The reader sees the role boundary attached to a definite addressed person rather than floating as an abstract reminder statement.\",\"reason\":\"QAC identifies {{ar:أَنتَ}} ({{tr:anta}}) as an independent second-person masculine singular pronoun, and attachment evidence makes it the head of predication with {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}).\",\"representative_source_ids\":[\"QG-052ead94\",\"QG-4260c39e\",\"QG-44c1dc68\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:command-before-restriction","source_type":"word_analysis","support_id":"sup_4b8cc072a9d44d4c61e1","text":"{\"blocking_evidence\":null,\"headline\":\"duty before limit\",\"reader_payoff\":\"The reader hears obligation before limitation, so the role boundary does not weaken the command.\",\"reason\":\"Attachment evidence identifies the imperative verbal clause before the restrictive nominal explanation, and 88:22 supplies the explicit non-control boundary.\",\"representative_source_ids\":[\"QT-edd10908\",\"MT-b258fb15\",\"QB-b324afb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:reminder-range-without-control","source_type":"word_analysis","support_id":"sup_4da37725d76e571a3d60","text":"{\"blocking_evidence\":null,\"headline\":\"broad reminder, no control\",\"reader_payoff\":\"The reader keeps the richness of reminder, mention, admonition, and memory activation while excluding coercion.\",\"reason\":\"V4 supports reminder, mention, and memory branches, while the local restriction and 88:22 keep the agency from becoming control over response.\",\"representative_source_ids\":[\"QS-628e4f2b\",\"QS-b13bdf55\",\"QS-ec676e3f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:restrictive-scope","source_type":"word_analysis","support_id":"sup_58dec66e9b4f39920ae5","text":"{\"blocking_evidence\":null,\"headline\":\"role under restriction\",\"reader_payoff\":\"The reader sees the particle limiting the addressee's role, not claiming that no one else can ever remind.\",\"reason\":\"QAC marks {{ar:إِنَّمَآ}} ({{tr:innamā}}) as a restrictive particle before the nominal clause, and attachment evidence says it restricts {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) to {{ar:أَنتَ}} ({{tr:anta}}).\",\"representative_source_ids\":[\"QG-0d3e0c12\",\"QG-9ade81ac\",\"MG-d90fea82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:1","source_type":"word_analysis","support_id":"sup_5d8c4488884cdb0175c3","text":"{\"gloss_range\":\"consequential or resumptive connector prefixed to the following command\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes the command that follows answer what has just been displayed. It can resume the discourse, but it does not let {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) sound like a detached exhortation: the visual sequence of 88:17-20 is carried forward as warrant for direct address. Because the particle is split analytically but fused in recitation to the imperative, consequence and command arrive as one tight surface movement. The light opening also pivots from seeing to commissioned speech: what was shown is now to be made present as reminder.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:command-sound-pressure","source_type":"word_analysis","support_id":"sup_622d0d4c3b9d02a69e6b","text":"{\"blocking_evidence\":null,\"headline\":\"crisp doubled command\",\"reader_payoff\":\"The reader hears the command as compact and forceful, matching the causative intensity of the Form II shape.\",\"reason\":\"The local surface has the doubled middle consonant of the Form II imperative, and the sound rows treat that pressure as tied to the command's force.\",\"representative_source_ids\":[\"QP-736a7b63\",\"QP-dcd6abc6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5","source_type":"word_analysis","support_id":"sup_635e3fc399f981e6f1e3","text":"{\"gloss_range\":\"Form II active participle: reminder-agent, predicate of the explicit addressee under restriction\",\"prose\":\"{{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) is where the command becomes a role. Grammatically it is the predicate of {{ar:أَنتَ}} ({{tr:anta}}), masculine singular and nominative, so the reminder function is attached to the single addressed person rather than left as an abstract noun. Its indefinite active participle form classifies him as a reminder-agent; it does not name a sovereign office, a passive remembered object, or a finite ongoing action, and its tanwīn leaves the role qualitative while exclusivity comes from the restriction. The root range allows mention, admonition, reminder-token, and making memory present, and the local Form II participle keeps that family centered on the agent who communicates reminder rather than on coercive mastery. The recipients remain implied rather than possessed as a domain, which lets reminder reach them without making response belong to the reminder-agent. The word also closes the ayah by echoing {{ar:ذَكِّرْ}} ({{tr:dhakkir}}): the act commanded at the start is restated as the only authorized identity at the end, with the final role-form standing out inside a common root. Its repeated doubled sound makes the final noun feel like the sustained version of the command, and its nasal indefinite close carries the role contrast forward into 88:22. That is why 88:22 can answer immediately with the excluded counterpart, control over them.\",\"root_display\":\"{{ar:ذ ك ر}} ({{tr:dh-k-r}})\",\"root_gloss_range\":\"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; this active participle selects the reminder-agent role and excludes coercive control\",\"surface_display\":\"{{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:implicit-to-explicit-you","source_type":"word_analysis","support_id":"sup_65c47e11d7f7e92dbfa5","text":"{\"blocking_evidence\":null,\"headline\":\"hidden you made visible\",\"reader_payoff\":\"The reader notices responsibility move from an inflection inside the command to an overt subject before its scope is limited.\",\"reason\":\"Attachment evidence marks the imperative's subject as implicit 2ms and {{ar:أَنتَ}} ({{tr:anta}}) as an explicit 2ms speech-role pronoun.\",\"representative_source_ids\":[\"QG-9030d172\",\"MG-c5da5266\",\"QT-a07d0e71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:agent-not-controller","source_type":"word_analysis","support_id":"sup_721cb0e89d5bf1677fb8","text":"{\"blocking_evidence\":null,\"headline\":\"agent not controller\",\"reader_payoff\":\"The reader sees the next ayah's denial of control as the excluded counterpart to the reminder-agent role.\",\"reason\":\"The cited contrast with 88:22 shows that {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) is a bounded role, not coercive mastery.\",\"representative_source_ids\":[\"MS-03261ff2\",\"MI-3b2a40ad\",\"MI-4bba5b07\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:forward-continuity","source_type":"word_analysis","support_id":"sup_76d1974e536aeef581fa","text":"{\"blocking_evidence\":null,\"headline\":\"same person into denial\",\"reader_payoff\":\"The reader keeps the same addressed figure across the positive role statement in 88:21 and the denial of control in 88:22.\",\"reason\":\"{{ar:أَنتَ}} ({{tr:anta}}) anchors the restrictive clause's subject, and the following ayah continues the same addressee in the negated role boundary at 88:22.\",\"representative_source_ids\":[\"QB-96199a68\",\"QY-45498104\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:marked-role-form","source_type":"word_analysis","support_id":"sup_7a7d9adf035ffaba0992","text":"{\"blocking_evidence\":null,\"headline\":\"marked role-form\",\"reader_payoff\":\"The reader notices that a common root is made sharper by ending on a less common role-bearing form.\",\"reason\":\"Contextual profiles show the active participle as a distinct local form profile within the common {{ar:ذ ك ر}} ({{tr:dh-k-r}}) root.\",\"representative_source_ids\":[\"QI-9529cb54\",\"QH-0a1f989f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:convergent-final-mechanism","source_type":"word_analysis","support_id":"sup_7f663119eca17243376d","text":"{\"blocking_evidence\":null,\"headline\":\"final mechanism gathered\",\"reader_payoff\":\"The reader sees the final word gather predicate grammar, causative role-form, exclusivity, root echo, and forward denial into one closing term.\",\"reason\":\"All local constraints converge on {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) as the restricted active reminder-agent predicate that answers the command and prepares 88:22.\",\"representative_source_ids\":[\"QY-aae2b24f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:predicate-of-anta","source_type":"word_analysis","support_id":"sup_80b942a50d9e24ff27ac","text":"{\"blocking_evidence\":null,\"headline\":\"predicate of the addressee\",\"reader_payoff\":\"The reader sees reminder predicated of the addressed person as his role, not floating as an abstract quality.\",\"reason\":\"Attachment evidence marks {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) as the predicate of {{ar:أَنتَ}} ({{tr:anta}}) in the restrictive nominal clause.\",\"representative_source_ids\":[\"QG-0083183c\",\"QG-06788a78\",\"QI-46b20428\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:final-predicate-landing","source_type":"word_analysis","support_id":"sup_91ad7a03328f2718a957","text":"{\"blocking_evidence\":null,\"headline\":\"ending lands on role\",\"reader_payoff\":\"The reader notices that the ayah closes not on the command but on the role noun that governs the command's meaning.\",\"reason\":\"{{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) is the last word of the ayah and the predicate of the explanatory nominal clause.\",\"representative_source_ids\":[\"QT-864949a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:detached-syntactic-body","source_type":"word_analysis","support_id":"sup_9237ce534e39e41865df","text":"{\"blocking_evidence\":null,\"headline\":\"separate syntactic body\",\"reader_payoff\":\"The reader sees the addressee given a full clause position rather than remaining only a verbal ending.\",\"reason\":\"The imperative already contains the implicit addressee, while {{ar:أَنتَ}} ({{tr:anta}}) appears separately as the subject of the restrictive nominal clause.\",\"representative_source_ids\":[\"QF-a4a318b8\",\"MT-bdffc456\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:form-ii-active-participle","source_type":"word_analysis","support_id":"sup_959fbec7dc3e797013b2","text":"{\"blocking_evidence\":null,\"headline\":\"durable causative reminder role\",\"reader_payoff\":\"The reader sees the final word as a durable Form II reminder-agent role, not generic causation or a one-time finite action.\",\"reason\":\"The local word is a Form II active participle of {{ar:ذ ك ر}} ({{tr:dh-k-r}}); broader causative and root-family possibilities survive only as narrowed reminder-agency here.\",\"representative_source_ids\":[\"QS-3509c053\",\"QF-f8e7d9c0\",\"MF-bf6768dc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:reminder-field","source_type":"word_analysis","support_id":"sup_95f29fc3f443edc6b53c","text":"{\"blocking_evidence\":null,\"headline\":\"mention and memory joined\",\"reader_payoff\":\"The reader hears reminder as speech that reawakens heed, not as mere information transfer or private recollection.\",\"reason\":\"V4 supports branches for bringing to mind, tongue-mention, revealed reminder, and admonition; the local imperative narrows that range to commanded reminder speech.\",\"representative_source_ids\":[\"QS-27920d20\",\"QS-411958cc\",\"MS-84376c79\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:positive-to-negative-boundary","source_type":"word_analysis","support_id":"sup_9fba7dbdd3cc3d03d8f9","text":"{\"blocking_evidence\":null,\"headline\":\"positive role to negative exclusion\",\"reader_payoff\":\"The reader sees the positive definition of the messenger's role in 88:21 determine the role he is not allowed in 88:22.\",\"reason\":\"The local predicate stays broad within reminder but is immediately contrasted with control in 88:22.\",\"representative_source_ids\":[\"QB-1e7c4156\",\"QB-30677cca\",\"QY-7558bf2a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:form-ii-reminder-agency","source_type":"word_analysis","support_id":"sup_a832c333f26398213bf2","text":"{\"blocking_evidence\":null,\"headline\":\"Form II reminder agency\",\"reader_payoff\":\"The reader sees the addressee assigned outward recall-making, not private remembering or generic causation.\",\"reason\":\"The local form is a Form II imperative of {{ar:ذ ك ر}} ({{tr:dh-k-r}}); V4 shows many accepted root branches, but local grammar selects causative reminder rather than the whole root inventory.\",\"representative_source_ids\":[\"QF-193ad246\",\"QF-1e05a5aa\",\"MF-d49b5dcf\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2","source_type":"word_analysis","support_id":"sup_ac4a1b0dff6332d2556d","text":"{\"gloss_range\":\"Form II imperative to cause reminder, with object and instrument unstated\",\"prose\":\"{{ar:ذَكِّرْ}} ({{tr:dhakkir}}) is a real imperative, but it is deliberately compressed. The Form II shape makes the addressee an active cause of reminder: public mention, admonition, and awakening recollection are all in range, while unrelated root branches such as maleness, hardness, renown, or legal documents are not locally selected. The verb has no stated object, suffix, preposition, or instrument, so the command does not narrow itself to one explicit audience or one named content; it lets the prior signs and the hearers remain recoverable without being restated. That compression differs from the benefit-framed reminder of 87:9 and the Qur'an-instrument reminder of 50:45, because here the command is moving toward role-definition. The same addressee hidden in the imperative will be made explicit in {{ar:أَنتَ}} ({{tr:anta}}), and the same root will return in {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}), turning the ordered act into a bounded role. Its doubled center also makes the command sound compact and forceful, so the audible pressure matches the causative recall-making force. The command is heard before the restriction, so duty is affirmed first; 88:22 then prevents that duty from expanding into coercive control.\",\"root_display\":\"{{ar:ذ ك ر}} ({{tr:dh-k-r}})\",\"root_gloss_range\":\"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; the local Form II command activates the reminder/admonitory speech branch\",\"surface_display\":\"{{ar:ذَكِّرْ}} ({{tr:dhakkir}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:common-root-local-slot","source_type":"word_analysis","support_id":"sup_b040a0f56be3fe6fcb51","text":"{\"blocking_evidence\":null,\"headline\":\"common root in a narrow slot\",\"reader_payoff\":\"The reader sees a broad, familiar root concentrated into a specific objectless command that is then bounded by role and non-control.\",\"reason\":\"Distributional evidence shows this exact root/form as an imperative pattern, while V4 confirms the broader root range that local grammar narrows.\",\"representative_source_ids\":[\"QI-bbd49137\",\"QH-a7de71e2\",\"QY-8acc65e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4:focus-and-role-specification","source_type":"word_analysis","support_id":"sup_b99567bece9a5f3adb4c","text":"{\"blocking_evidence\":null,\"headline\":\"focused role bearer\",\"reader_payoff\":\"The reader sees the pronoun both identify and focus the addressee as the bearer of the limited role.\",\"reason\":\"The independent pronoun occupies the subject slot of the restrictive nominal clause, so focus and predication work together rather than remaining mere reference.\",\"representative_source_ids\":[\"QS-25dc56fc\",\"QS-bec8a6e6\",\"QF-46ca0f19\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:21:1:2","source_type":"qac_morpheme","support_id":"sup_c3d23df57fde8bb8cdf3","text":"{\"lemma_ar\":\"ذُكِّرَ\",\"morph_features\":\"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:21:1:2\",\"qac_word_ref\":\"88:21:1\",\"root_ar\":\"ذ ك ر\",\"surface_ar\":\"ذَكِّرْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:fused-particle-reparse","source_type":"word_analysis","support_id":"sup_cb469fb8e264aacf9baa","text":"{\"blocking_evidence\":null,\"headline\":\"fused restrictive token\",\"reader_payoff\":\"The reader sees emphasis and limitation arrive as one grammatical unit over the pronoun-predicate clause.\",\"reason\":\"QAC identifies the surface as a restrictive particle, not an ordinary {{ar:إِنَّ}} ({{tr:inna}}) clause with an independent following particle.\",\"representative_source_ids\":[\"QF-4883dd6b\",\"QF-560d7453\",\"QF-8d850fb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:agent-and-token-family","source_type":"word_analysis","support_id":"sup_cb981fdb1a14a1aa5703","text":"{\"blocking_evidence\":null,\"headline\":\"agent and reminder-token family\",\"reader_payoff\":\"The reader sees the root family include both reminder-agent and reminder-token ideas while the local word names the agent.\",\"reason\":\"V4 includes reminder-object and admonition senses, but the local form is the active participial agent {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}).\",\"representative_source_ids\":[\"QS-a460a617\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:bounded-office-synthesis","source_type":"word_analysis","support_id":"sup_d9be88ed18206034e26b","text":"{\"blocking_evidence\":null,\"headline\":\"bounded reminder office\",\"reader_payoff\":\"The reader sees the command as broad enough to cover reminder but restricted enough not to become mastery over response.\",\"reason\":\"The imperative is followed by restriction in 88:21 and explicit denial of control in 88:22, so the root recurrence is framed as office rather than outcome-ownership.\",\"representative_source_ids\":[\"QY-946c595a\",\"QY-8acc65e7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:1:consequence-resumption","source_type":"word_analysis","support_id":"sup_de972e91bcb55a9537ca","text":"{\"blocking_evidence\":null,\"headline\":\"consequence and resumption together\",\"reader_payoff\":\"The reader sees the command as both a resumed address and a consequence of the preceding signs, not as a new disconnected instruction.\",\"reason\":\"QAC identifies {{ar:فَ}} ({{tr:fa}}) as a conjunction before the imperative, and the verbal clause evidence supports a transition into command rather than an isolated clause.\",\"representative_source_ids\":[\"QG-5045b26a\",\"QG-9c1fc56f\",\"QS-afafb0bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:5:sound-echo-closure","source_type":"word_analysis","support_id":"sup_e2dec63b2ed79539fdd8","text":"{\"blocking_evidence\":null,\"headline\":\"audible sustained reminder\",\"reader_payoff\":\"The reader hears the final role noun as the sustained sound-version of the earlier command.\",\"reason\":\"The sound rows are supported by the shared root and Form II doubled consonant visible in both local forms.\",\"representative_source_ids\":[\"QP-49f7983b\",\"QP-964377fd\",\"MP-875ad2ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:emphatic-limitation","source_type":"word_analysis","support_id":"sup_e3e36da88b6c12e4fde0","text":"{\"blocking_evidence\":null,\"headline\":\"limit without devaluing\",\"reader_payoff\":\"The reader understands 'only' as a boundary on authority, not as a dismissal of the commanded reminder.\",\"reason\":\"The imperative has already established real duty, while the restriction clause prevents that duty from being inflated into control, compulsion, or outcome-ownership.\",\"representative_source_ids\":[\"QS-13dcec6f\",\"QS-2877a7a1\",\"QI-7ab510ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:objectless-imperative","source_type":"word_analysis","support_id":"sup_e733020a4464cf56b1bd","text":"{\"blocking_evidence\":null,\"headline\":\"objectless imperative\",\"reader_payoff\":\"The reader notices that the command is broad because the audience, content, and instrument of reminder are not overtly filled in.\",\"reason\":\"Attachment evidence marks {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) as a Form II imperative with frame `obj=none_absolute` and warns against adding an explicit object if the target language can preserve the compression.\",\"representative_source_ids\":[\"QG-4ed3beda\",\"QF-88ba79b8\",\"QT-a36a1ad0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:delivery-not-uptake","source_type":"word_analysis","support_id":"sup_edbe63e352c356a0dae5","text":"{\"blocking_evidence\":null,\"headline\":\"delivery not uptake\",\"reader_payoff\":\"The reader separates the messenger-side act of prompting from the audience-side act of taking heed.\",\"reason\":\"The commanded form is messenger-side Form II; receptive remembering forms are not the local imperative, and the object remains omitted.\",\"representative_source_ids\":[\"QS-dc65ca5b\",\"QS-e42d85ee\",\"QF-d5934d44\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:action-to-role-pivot","source_type":"word_analysis","support_id":"sup_f11c59c0ed356376b760","text":"{\"blocking_evidence\":null,\"headline\":\"imperative becomes role boundary\",\"reader_payoff\":\"The reader feels the ayah pivot from a commanded act to a standing role-definition.\",\"reason\":\"The restrictive nominal clause follows the verbal imperative clause and is marked as its explanation.\",\"representative_source_ids\":[\"QT-77ed9a4d\",\"QT-b71ee280\",\"MT-f6ebd0f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:observation-becomes-reminder","source_type":"word_analysis","support_id":"sup_f31896238d6748695b55","text":"{\"blocking_evidence\":null,\"headline\":\"failed seeing becomes prompting\",\"reader_payoff\":\"The reader sees the prior visible signs become the material that must be brought back into awareness.\",\"reason\":\"The imperative follows the inspection sequence beginning at 88:17, so the objectless reminder can recover the displayed signs without restating them.\",\"representative_source_ids\":[\"MI-a687f923\",\"QB-d7ad0b0a\",\"QB-f3e99011\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:4","source_type":"word_analysis","support_id":"sup_f3796991c2df595716e6","text":"{\"gloss_range\":\"independent second-person masculine singular pronoun serving as subject of the restrictive nominal clause\",\"prose\":\"{{ar:أَنتَ}} ({{tr:anta}}) is not needed merely to identify the addressee, because the imperative {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) already carries a second-person subject. Its work is to give that addressee an independent subject slot inside the restrictive nominal clause, so reference and focus land on the same role-bearer. The command's hidden 'you' becomes an explicit 'you' at the point where responsibility is being defined and limited. Its separate onset makes the clause catch on the addressed person before the predicate lands, turning a verbal ending into a visible syntactic body. This turns the prior discourse from audience-facing observation into direct commission, and it keeps the same person in view when 88:22 denies control over them.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَنتَ}} ({{tr:anta}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:act-to-role-echo","source_type":"word_analysis","support_id":"sup_f40715b56a511e9d5d7d","text":"{\"blocking_evidence\":null,\"headline\":\"command echoed as role\",\"reader_payoff\":\"The reader notices the root returning from imperative act to predicate role inside the same ayah.\",\"reason\":\"QAC aligns both {{ar:ذَكِّرْ}} ({{tr:dhakkir}}) and {{ar:مُذَكِّرٌۭ}} ({{tr:mudhakkirun}}) to {{ar:ذ ك ر}} ({{tr:dh-k-r}}), while the clause grammar changes from imperative to predicate.\",\"representative_source_ids\":[\"QE-1bebb1cf\",\"QE-86b60d04\",\"ME-2c01a871\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:3:restrictive-clause-cadence","source_type":"word_analysis","support_id":"sup_f726541b45adcbf6f5d0","text":"{\"blocking_evidence\":null,\"headline\":\"nasal clause binding\",\"reader_payoff\":\"The reader hears the restrictive clause as a continuous unit after the sharper command.\",\"reason\":\"The sound row concerns the heard continuity of the nominal restriction and is compatible with the local clause structure.\",\"representative_source_ids\":[\"QP-c915972b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:21:2:intertext-command-frames","source_type":"word_analysis","support_id":"sup_fff0b17bde9abde693c5","text":"{\"blocking_evidence\":null,\"headline\":\"same command different frame\",\"reader_payoff\":\"The reader can compare the same reminder command under different limits: benefit in 87:9, Qur'an-instrument in 50:45, and role-definition here.\",\"reason\":\"Contextual profiles show Form II imperative instances with varied complements, while the cited rows give concrete contrasts at 87:9 and 50:45.\",\"representative_source_ids\":[\"QI-03863237\",\"QI-5e8aac80\",\"MI-5b4c404a\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000516","role":"Bringing something back to mind supplies the cognitive operation performed by both the imperative and the named agent.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"changed_reading":{"after":"Actively restore an absent or neglected matter to present awareness; that restorative act defines the role.","before":"Issue a generic exhortation."},"confidence":"strong","focus_anchor":"The Form II imperative at word 1 and the agent noun at word 4 repeat ذ ك ر around the restrictive إنما.","mechanism":"The command causes an already addressable matter to become present after absence or forgetfulness, while the repeated agent noun makes that reactivation the addressee's bounded office.","model_id":"baseline_recall_reactivation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_recall_reactivation","source_type":"hft","support_id":"sup_5f8f0c276afcd187c3e7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000516","role":"Mention on the tongue makes voiced disclosure the means by which the reminder enters public awareness.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"changed_reading":{"after":"Voice, name, and make the matter known so that recollection becomes publicly available.","before":"Privately prompt someone to remember."},"confidence":"strong","focus_anchor":"The imperative ذَكِّرْ can externalize remembrance, and مُذَكِّر names the person who repeatedly performs that public act.","mechanism":"Verbal mention is the outward carrier of inward recollection: naming and making known place the matter within hearing without yet determining its reception.","model_id":"baseline_spoken_making_known"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_spoken_making_known","source_type":"hft","support_id":"sup_794f6a786906a37b4af1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000516/B009"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000516","role":"A reminder as the thing that makes a matter present casts the agent as a mnemonic medium rather than the controller of response.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]}],"changed_reading":{"after":"Supply the occasion and means of renewed presence; the restrictive identity leaves the audience's resulting response open.","before":"Make the audience remember as an achieved result."},"confidence":"medium","focus_anchor":"The sequence فَذَكِّرْ ... إِنَّمَا أَنتَ مُذَكِّرٌ pairs an act with a restrictive identity statement.","mechanism":"The addressee is not represented as owning the remembered reality or its outcome, but as the recurring occasion by which it is made present.","model_id":"baseline_reminder_medium"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_reminder_medium","source_type":"hft","support_id":"sup_eac07b67ab1c5672afcd","trust":"legacy_unbound"}]}
</lane_packet_json>
