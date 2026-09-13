# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:2",
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
{"branch_registry":[{"boundary":"Dal, insanın boyun eğen ve sakinleşen durumuyla sınırlıdır; arazi, gök cisimleri, deve hörgücü ve göğüsten salgı çıkarma anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000412/B001","candidate_links":[{"candidate_id":"cand_aab903d68bd44ea162f0","lane":"micro"},{"candidate_id":"cand_1c1584454305238ffa05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","surface_ar":"خَٰشِعَةٌ"}],"gloss":"boyun eğip dinginleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi kendini alçaltan bir tutumla boyun eğer ve dinginleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başın, göğsün veya bakışın aşağı indirilmesi bu tutumun bedensel görünümüdür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Seslere uygulandığında seslerin kesilmesini, durulmasını ve alçalmasını bildirir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İçteki yakarış ve boyun eğiş, organların sakin ve alçalmış duruşunda dışa vurabilir."}}],"root_ar":"خ ش ع","root_id":"root_000412","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanın kendini alçaltan iç ve dış tutumunu, bedensel sakinlikle birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, insanın boyun eğen ve sakinleşen durumuyla sınırlıdır; arazi, gök cisimleri, deve hörgücü ve göğüsten salgı çıkarma anlamlarını kapsamaz.","branch_image_ar":"تطامن وخضوع","concept_gloss":"boyun eğip dinginleşme","contextual_glosses":[{"applicability":"Başın ya da bakışın yere yöneltildiği bedensel görünüm için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aşağı yönelen baş ve bakış hareketini açıkça korur."},"facet_ids":["F002"],"text":"başını ve bakışını indirmek","usage_role":"contextual"},{"applicability":"Seslerin kesildiği, sakinleştiği ve işitilirliğinin azaldığı yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin durulması ve alçalması sonucunu birlikte korur."},"facet_ids":["F003"],"text":"sesler dinip alçalmak","usage_role":"contextual"},{"applicability":"İçteki boyun eğişin organların sakin duruşunda görünür olduğu bağlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İç durum ile organların görünür duruşu arasındaki bağı korur."},"facet_ids":["F004"],"text":"yakarışın bedene yansıması","usage_role":"explanatory"}],"definition":"Kişinin boyun eğerek başını, bedenini veya bakışını aşağı indirmesi ve dingin bir tutum almasıdır. Bu iç yöneliş, belirli yapılarda sesin alçalması ya da organların sakinleşmiş duruşuyla görünür olur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi kendini alçaltan bir tutumla boyun eğer ve dinginleşir."},{"facet_id":"F002","role":"specialization","statement":"Başın, göğsün veya bakışın aşağı indirilmesi bu tutumun bedensel görünümüdür."},{"facet_id":"F003","role":"extension","statement":"Seslere uygulandığında seslerin kesilmesini, durulmasını ve alçalmasını bildirir."},{"facet_id":"F004","role":"associated_use","statement":"İçteki yakarış ve boyun eğiş, organların sakin ve alçalmış duruşunda dışa vurabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Sıradan konuşmayı kesme anlamıyla kolayca karışır.","fit":"narrowing","loses":"Boyun eğme, bedensel alçalma, bakış ve organlarla ilgili çekirdeği siler.","preserves":"Sesin kesilmesiyle ilgili sınırlı görünümü korur."},"text":"susmak"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Boyun eğme, dinginleşme ve beden, bakış ya da sesteki görünür belirtileri eksiltir.","preserves":"Kendini üstün görmeme ve alçaltma yönünü korur."},"text":"alçakgönüllülük"}],"identity_rationale":"Toplu tanıklık, insanın başını, bedenini ya da bakışını aşağı indirerek boyun eğmesini temel alır; bu durum sesin durulmasına ve içteki yakarışın organlara yansımasına da uzanır. Verilen çerçeve bu bedensel, davranışsal ve sessel görünümleri aynı alçalma ve boyun eğme çekirdeğinde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"boyun eğip başını ya da bedenini alçaltmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"beden, ses, bakış ve organlarda beliren boyun eğiş ve dinginlik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boyun eğen, kendini alçaltan; kimi kullanımda eğilerek duran"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"göğsünü eğip alçakgönüllü bir tutum almak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"boyun eğişi zorlayarak sergilemek veya öyle görünmeye çalışmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yalvararak boyun eğen ve kendini alçaltan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"alçakgönüllü görünerek başını eğmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bakışını kısmak veya yere indirmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"seslerin dinip alçalması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"içteki yakarışın organların sakin duruşuna yansıması"}],"lexicalization_note":"Yalın biçimler genel boyun eğme ve alçalma durumunu verir; bakışın indirilmesi, seslerin dinmesi ve organların etkilenmesi yalnız kendi yapıları içinde yorumlanır.","neighbor_coverage_note":"İnsanın boyun eğişiyle doğrudan karışabilecek üç aday seçildi. Koşma, diz çökme ve belirli el ya da baş işaretleri ayrı hareket çekirdeklerine sahipti; öteki adaylar ya korku ve uysallık gibi daha dar durumları veriyor ya da yalnız aynı kökün fiziksel alçalma dallarını temsil ediyordu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, boyun eğişin baş, beden, bakış, ses ve organlarda beliren dingin görünümünü kapsar. Komşu dal ise boyun eğmeyi özellikle sinmiş ve güçsüz bir durumda kalma yönüyle sınırlar.","focus_only":"Bedene, sese ve bakışa yayılan sakinleşmiş alçalma görünümü vardır.","gloss":"dingin boyun eğiş / sinerek boyun eğiş","neighbor_only":"Sinmişlik ve güçsüzce boyun eğme vurgusu daha belirgindir.","neighbor_ref":"root_001332/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendini alçaltıp boyun eğmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin genel tutumunu ve bunun bakış, ses ve organlardaki belirtilerini anlatır. Komşu dalın çekirdeği ise doğrudan eğilme hareketidir; bu yüzden sıradan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Belirli bir hareket olmadan da sürebilen dingin ve alçalmış durumdur.","gloss":"boyun eğmiş duruş / eğilme hareketi","neighbor_only":"Eğilme hareketini hem tapınmada hem başka durumlarda kullanabilir.","neighbor_ref":"root_000594/B003","relation_type":"near_neighbor","shared_zone":"İkisinde de bedenin aşağı yönelmesi kendini alçaltma anlamı taşır."},{"boundary_match":"partial","distinction":"Odak dalın gerçekleşmesi için alnın yere konması gerekmez; dinginlik ve bakışın ya da sesin alçalması yeterli olabilir. Komşu dal ise yere kapanmanın belirli bedensel hareketini ve bu hareketle bildirilen boyun eğmeyi merkez alır.","focus_only":"Baş, bakış veya sesin alçalmasıyla da gerçekleşebilen geniş bir durumdur.","gloss":"dingin boyun eğiş / yere kapanma","neighbor_only":"Alnı yere koymaya kadar varan belirli bir yere kapanma hareketini içerir.","neighbor_ref":"root_000675/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bedenin alçalması boyun eğmenin görünür belirtisidir."}],"source_phrase_ar":"أصل واحد يدل على التطامن؛ تطامن وطأطا رأسه؛ الخاشع المستكين والراكع (maqayis)؛ الخشوع رميك ببصرك إلى الأرض؛ متخشع متضرع؛ خشعت الأصوات أي سكنت (ayn)؛ الخاشع المستكين؛ الخاشع الراكع؛ خشع ببصره إذا غضه (jamhara)؛ الخشوع الخضوع؛ التخشع تكلف الخشوع (sihah)؛ التخشع لله الإخبات والتذلل؛ خشع الرجل إذا رمى ببصره إلى الأرض؛ الخشوع في البدن والصوت والبصر (tahdhib)؛ الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح (mufradat)","source_summary":"Tanıklıklar alçalma, boyun eğme ve dinginlik çekirdeğinde birleşir; baş, göğüs, bakış, ses ve organlar bu çekirdeğin farklı görünüm alanlarıdır. Kimi kullanımlarda eğilerek durma, kimi kullanımlarda ise böyle görünmeye çalışma ayrıca belirtilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه خشوع الرجل والمتخشع والضراعة والإخبات والتذلل وطأطأة الرأس وغض البصر وسكون الصوت وخشوع الجوارح والركوع","what_is_not_ar":"الأرض والأكمة والبلدة والسنام والكواكب وخراشي الصدر"},"support_links":["sup_b7b23173f29798f89aa3","sup_c2d5125f6d52cde6f3a8"]},{"boundary":"Yere yakın arazi adı dalın yalın çekirdeğidir; kuruluk, tozluluk ve duvarın çökmesi yalnız ilgili adlarla kurulan yapılara aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000412/B002","candidate_links":[{"candidate_id":"cand_2068f0e21657d8add22b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","surface_ar":"خَٰشِعَةٌ"}],"gloss":"yere yakın arazi parçası","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yere yakın duran arazi parçası, sırt veya küçük yükselti yalın adın çekirdeğidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi parçası kimi tanıklıkta düzleşmiş ve kolay geçilir, kiminde pürüzlü olarak betimlenir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yöre veya yer için kullanıldığında tozlu ve yerleşimsiz olmayı bildirir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Toprak için kullanıldığında yağmursuz kalıp kurumuş, bitkisiz ve cansız duruma gelmeyi bildirir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Duvar için kullanıldığında çöküp yüksekliğini yitirerek yer düzeyine inmeyi bildirir."}}],"root_ar":"خ ش ع","root_id":"root_000412","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın adın arazi parçası, sırt veya küçük yükselti bildiren ortak çekirdeği için kullanılır.","boundary_detail":"Yere yakın arazi adı dalın yalın çekirdeğidir; kuruluk, tozluluk ve duvarın çökmesi yalnız ilgili adlarla kurulan yapılara aittir.","branch_image_ar":"أرض لاطئة هامدة","concept_gloss":"yere yakın arazi parçası","contextual_glosses":[{"applicability":"Bir yöre veya yerleşim alanının tozlu ve üzerinde ev bulunmayan durumunu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozlu ve yerleşimsiz yöre niteliğini birlikte korur."},"facet_ids":["F003"],"text":"tozlu ve yerleşimsiz olmak","usage_role":"contextual"},{"applicability":"Yağmur almayan toprağın kuruduğu ve üzerinde yeşillik kalmadığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuruma, bitkisizleşme ve cansızlaşma sonucunu korur."},"facet_ids":["F004"],"text":"kuruyup cansızlaşmak","usage_role":"contextual"},{"applicability":"Bir duvarın yüksekliğini yitirerek yere yaklaşması veya yer düzeyine inmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duvarın çökmesi ve yüksekliğini yitirmesi sonucunu korur."},"facet_ids":["F005"],"text":"çöküp yerle bir olmak","usage_role":"contextual"}],"definition":"Yalın kullanımda yere yakın duran bir arazi parçasını, sırtı veya küçük yükseltiyi belirtir; tanıklıklar yüzeyin düzleşmiş ya da pürüzlü oluşunda ayrışır. Belirli yapılarda bu alçalma görüntüsü tozlu ve yerleşimsiz yöreye, kuruyup cansızlaşmış toprağa veya çökerek yerle bir olan duvara uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yere yakın duran arazi parçası, sırt veya küçük yükselti yalın adın çekirdeğidir."},{"facet_id":"F002","role":"source_variant","statement":"Arazi parçası kimi tanıklıkta düzleşmiş ve kolay geçilir, kiminde pürüzlü olarak betimlenir."},{"facet_id":"F003","role":"specialization","statement":"Yöre veya yer için kullanıldığında tozlu ve yerleşimsiz olmayı bildirir."},{"facet_id":"F004","role":"extension","statement":"Toprak için kullanıldığında yağmursuz kalıp kurumuş, bitkisiz ve cansız duruma gelmeyi bildirir."},{"facet_id":"F005","role":"extension","statement":"Duvar için kullanıldığında çöküp yüksekliğini yitirerek yer düzeyine inmeyi bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Toprağın verimsizliğiyle sınırlı ayrı bir kavramı çağrıştırır.","fit":"narrowing","loses":"Yere yakın arazi adını, tozlu yöreyi ve çökmüş duvar kullanımını dışarıda bırakır.","preserves":"Kurumuş ve bitkisiz toprak görünümünü korur."},"text":"çoraklık"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Pürüzlü arazi değişkesini ve yere yakın küçük yükseltiyi eksiltir.","preserves":"Bazı tanıklıklardaki düzleşmiş arazi görünümünü korur."},"text":"düzlük"}],"identity_rationale":"Yetkili tanıklık yalnız cansız ve kuru toprağı değil, yere yakın bir arazi parçasını veya küçük yükseltiyi; ayrıca yapıya bağlı olarak tozlu yöreyi, kurumuş toprağı ve çöküp yere yaklaşan duvarı kapsar. Bu nedenle dal korunabilir, ancak onu yalnızca alçak ve cansız arazi diye sunan görüntü daha geniş ve katmanlı bir tanımla düzeltilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yere yakın arazi parçası veya küçük yükselti"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yere yakın, basık sırt veya yükselti"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"tozlu ve yerleşimsiz yöre"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kurumuş, bitkisiz ve cansız toprak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çöküp yerle bir olmuş duvar"}],"lexicalization_note":"Yalın ad, yere yakın arazi parçasını veya küçük yükseltiyi belirtir; yöre, toprak ve duvarla kurulan kullanımların tozluluk, kuruluk ve çökme anlamları bu ada genellenmez.","neighbor_coverage_note":"Doğrudan arazi biçimi veya bitkisizlik kesişimi bulunan üç aday seçildi. Yüksek arazi, verimli çukur, dağlara giriş ve kumluk gibi öteki alan kartları yalnız aynı çevreyi paylaşır; insan, gök cismi ve hörgüç dallarıysa fiziksel alçalma imgesine rağmen ayrı çekirdeklere sahiptir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın yalın adı yere yakın bir arazi parçası ya da küçük yükselti olabilir ve yüzey her zaman pürüzsüz değildir. Komşu dal ise özellikle düz, pürüzsüz geniş alanı merkez alır; bitkisizlik onun olası bir niteliğidir.","focus_only":"Yere yakın küçük yükseltiyi, tozlu yöreyi ve çökmüş duvarı da kapsar.","gloss":"yere yakın arazi / dümdüz alan","neighbor_only":"Özellikle dümdüz, pürüzsüz ve bazen bitkisiz geniş alanı belirtir.","neighbor_ref":"root_000871/B005","relation_type":"near_synonym","shared_zone":"Her iki dal düzleşmiş veya bitkisiz görünen araziyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalda bitkisizlik yalnız toprağa bağlı uzantılardan biridir; yalın çekirdek yere yakın arazi biçimidir. Komşu dalın çekirdeği ise bitki örtüsünün ortadan kalkmasıdır ve arazinin alçak olmasını gerektirmez.","focus_only":"Yere yakın arazi biçimini ve çökmüş duvar gibi başka alçalmış görünümleri kapsar.","gloss":"alçak arazi / bitkisi kesilmiş toprak","neighbor_only":"Bitkinin yağmursuzluk, yenme veya başka nedenle kesilmiş olmasını merkez alır.","neighbor_ref":"root_000236/B002","relation_type":"near_neighbor","shared_zone":"İki dal da kurumuş ve üzerinde bitki kalmamış toprağı anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal yere yakınlık çevresinde farklı arazi biçimlerini ve yapıya bağlı uzantıları toplar. Komşu dal ise engebeli arazinin karşıtı olan kolay geçilir düzlüğü merkez alır.","focus_only":"Küçük yükselti, pürüzlü parça, kuru toprak ve çökmüş duvar görünümlerine uzanır.","gloss":"yere yakın parça / kolay geçilen düzlük","neighbor_only":"Kolay geçilen düz araziyi ve böyle bir araziye inmeyi anlatır.","neighbor_ref":"root_000753/B001","relation_type":"near_neighbor","shared_zone":"İkisinde de düzleşmiş ve alçak görünen arazi bulunabilir."}],"source_phrase_ar":"الخشعة قطعة من الأرض قف قد غلبت عليه السهولة؛ قف خاشع لاطئ بالأرض؛ بلدة خاشعة مغبرة (maqayis)؛ الخشعة قف غلبت عليه السهولة؛ أكمة خاشعة لاطئة بالأرض (ayn)؛ الخشعة قطعة من الأرض تغلظ؛ الخاشع المطمئن من الأرض (jamhara)؛ بلدة خاشعة مغبرة؛ مكان خاشع؛ الخشعة أكمة متواضعة (sihah)؛ الحثمة اللاطئة بالأرض هي الخشعة؛ الخشعة الأكمة؛ إذا يبست الأرض ولم تمطر قيل قد خشعت؛ أرض خاشعة هامدة؛ جدار خاشع (tahdhib)","source_summary":"Tanıklıklar yere yakınlık ve alçalmış görünüm çevresinde birleşir. Bunun yanında arazi parçasının düz ya da pürüzlü oluşunda ayrışır; tozlu ve boş yöre, yağmursuz kalmış bitkisiz toprak ve çökmüş duvar kullanımları da aynı toplu iddiada yer alır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الخشعة من الأرض والقف الخاشع والأكمة المتواضعة والبلدة المغبرة والمكان الخاشع والأرض الخاشعة الهامدة والجدار المتداعي","what_is_not_ar":"خشوع الإنسان والصوت والبصر والسنام والكواكب وخراشي الصدر"},"support_links":["sup_5989c8d9b09f6867699d"]},{"boundary":"Bu anlam yalnız verilen güneş ve yıldız yapılarında geçerlidir; genel bir kararma, düşme veya batma anlamı olarak genişletilemez.","branch_kind":"collocation","branch_ref":"root_000412/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","surface_ar":"خَٰشِعَةٌ"}],"gloss":"görünürlüğü azalıp kaybolmaya yaklaşma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gök cisminin görünürlüğü ya kararma ya da ufka iniş yoluyla azalır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneşle kurulan yapıda tutulma, kararma ve görünürlüğün azalması anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yıldızlarla kurulan yapıda ufka iniş ve batmaya yaklaşma anlatılır."}}],"root_ar":"خ ش ع","root_id":"root_000412","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız güneş tutulması ile yıldızların ufka inişini birlikte kapsayan üst anlatım olarak kullanılır.","boundary_detail":"Bu anlam yalnız verilen güneş ve yıldız yapılarında geçerlidir; genel bir kararma, düşme veya batma anlamı olarak genişletilemez.","branch_image_ar":"كوكب يغور","concept_gloss":"görünürlüğü azalıp kaybolmaya yaklaşma","contextual_glosses":[{"applicability":"Güneşin tutulduğu veya bu olayda kararıp görünürlüğünün azaldığı yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin tutulması ve kararması olayını açıkça korur."},"facet_ids":["F002"],"text":"güneş tutulup kararmak","usage_role":"contextual"},{"applicability":"Yıldızların ufka inip gözden kaybolmaya yaklaştığı yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıldızların ufka inişini ve batmaya yaklaşmasını korur."},"facet_ids":["F003"],"text":"yıldızlar batmaya yüz tutmak","usage_role":"contextual"}],"definition":"Yalnız gök cisimleriyle kurulan yapılarda, güneşin tutulup kararmasını veya yıldızların ufka inerek gözden kaybolmaya yaklaşmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gök cisminin görünürlüğü ya kararma ya da ufka iniş yoluyla azalır."},{"facet_id":"F002","role":"specialization","statement":"Güneşle kurulan yapıda tutulma, kararma ve görünürlüğün azalması anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Yıldızlarla kurulan yapıda ufka iniş ve batmaya yaklaşma anlatılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin ufka iniş olmadan tutulup kararması anlamını dışarıda bırakır.","preserves":"Yıldızların ufka inip gözden kaybolması yönünü korur."},"text":"batmak"},{"category":"confusable","error_profile":{"adds":"Işık kaynağının bütünüyle çalışmaz duruma geldiği izlenimini ekler.","collision":"Ateşin veya yapay bir ışığın sönmesiyle karışır.","fit":"displacement","loses":"Güneş tutulması ile yıldızın ufka inişi arasındaki iki ayrı süreci siler.","preserves":"Işığın görünürlükten çekilmesi sonucunu kısmen korur."},"text":"sönmek"}],"identity_rationale":"Tanıklık iki göksel yapıyı birlikte verir: güneş söz konusu olduğunda tutulma veya kararma, yıldızlar söz konusu olduğunda ufka inip gözden kaybolmaya yaklaşma. Yıldızın batışını öne çıkaran dal görüntüsü kullanılabilir, ancak güneş tutulmasını aynı olaymış gibi göstermemek için iki yapı açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"güneşin tutulup kararması"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yıldızların ufka inip batmaya yaklaşması"}],"lexicalization_note":"Dal yalnız güneşin tutulmasını ve yıldızların ufka inmesini bildiren iki göksel yapıyla sınırlıdır; bunlardan yalın bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Görünmezleşme sonucunu taşıyıp süreç farkını açıklayan üç aday seçildi. Doğuş, ateş ışığı, gezegenlerin geri hareketi ve güneşin gökteki başka konum değişimleri farklı çekirdeklere sahipti; kardeş dallar ise yalnız alçalma imgesi üzerinden uzaktan bağlantılıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda güneşin görünürlüğü tutulma nedeniyle azalır; ayrıca yıldızların ufka inişi de bu dala bağlıdır. Komşu dal ise güneşin ufukta batıp kaybolmasını merkez alır.","focus_only":"Güneş tutulmasını ve yıldızların batmaya yaklaşmasını birlikte kapsar.","gloss":"göksel görünürlük kaybı / güneşin batışı","neighbor_only":"Güneşin ufukta gerçekleşen olağan batışını doğrudan belirtir.","neighbor_ref":"root_001112/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal güneşin görünürlüğünün azalabildiği bir durumu anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız iki belirli göksel yapıda tutulma veya ufka iniş bildirir. Komşu dalın çekirdeği daha genel gözden yitme ve batmadır; bu yüzden gök dışındaki varlıklara da uzanabilir.","focus_only":"Güneş tutulması ve yıldızların batmaya yaklaşmasıyla sınırlı iki yapı vardır.","gloss":"yapıya bağlı kaybolma / genel gözden yitme","neighbor_only":"Herhangi bir şeyin yokluğa çekilmesini ve çeşitli ışıklı gök cisimlerinin batışını kapsar.","neighbor_ref":"root_000042/B001","relation_type":"near_neighbor","shared_zone":"İki dal da güneş veya yıldızın görünmez duruma gelmesini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dalın süreçleri güneş tutulması ve yıldızların ufka hareketidir. Komşu dal ise ayın aylık evresinde ışıklı bölümünün küçülmesini anlatır; ortak sonuç benzer olsa da süreç ve gök cismi farklıdır.","focus_only":"Güneş tutulmasını veya yıldızların ufka inmesini bildirir.","gloss":"tutulma ya da batış / ayın küçülerek görünmezleşmesi","neighbor_only":"Ayın evre sonunda ışığının giderek azalmasıyla görünmezleşmesini bildirir.","neighbor_ref":"root_001401/B002","relation_type":"same_field","shared_zone":"Her iki dal göksel bir ışığın görünürlüğünün azalması alanındadır."}],"source_phrase_ar":"خشعت الشمس وكسفت وخسفت بمعنى واحد؛ خشوع الكواكب إذا غارت فكادت تغيب في مغيبها؛ خشعت الكواكب إذا دنت من المغيب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, güneş için tutulmayı; yıldızlar için ufka yaklaşarak gözden kaybolmayı bildirir."}],"source_summary":"Bu dalın bütün verisi tek bir tanıklık kümesinde iki ayrı göksel yapıya ayrılır; güneş için tutulma, yıldızlar için ufka yaklaşarak gözden kaybolma bildirilir.","sources":["TA"],"what_is_ar":"يدخل فيه خشوع الشمس إذا كسفت أو خسفت وخشوع الكواكب إذا غارت أو دنت من المغيب","what_is_not_ar":"خشوع الإنسان والأرض والسنام وخراشي الصدر"},"support_links":[]},{"boundary":"Anlam yalnız devenin hörgücüyle kurulan yapıya aittir; genel zayıflama, kesme veya yüksekliğini yitirme anlamına genişletilemez.","branch_kind":"collocation","branch_ref":"root_000412/B004","candidate_links":[{"candidate_id":"cand_2068f0e21657d8add22b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","surface_ar":"خَٰشِعَةٌ"}],"gloss":"hörgücün yağını yitirip çökmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin hörgücündeki yağ tükenir ve hörgüçten yalnız az bir bölüm kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yağ kaybının sonucu olarak hörgücün tepesi belirginliğini yitirip aşağı çöker."}}],"root_ar":"خ ش ع","root_id":"root_000412","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin hörgücündeki yağ kaybını ve bunun sonucundaki biçim değişikliğini birlikte anlatır.","boundary_detail":"Anlam yalnız devenin hörgücüyle kurulan yapıya aittir; genel zayıflama, kesme veya yüksekliğini yitirme anlamına genişletilemez.","branch_image_ar":"سنام ذاهب الشرف","concept_gloss":"hörgücün yağını yitirip çökmesi","contextual_glosses":[{"applicability":"Bir devenin hörgücü yağını yitirip geriye çok azı kaldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hörgücün erimesini ve aşağı çökmesini birlikte korur."},"facet_ids":["F001","F002"],"text":"hörgücü eriyip çökmek","usage_role":"contextual"}],"definition":"Devenin hörgücünün yağını yitirip büyük ölçüde erimesi ve tepesinin aşağı çökmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin hörgücündeki yağ tükenir ve hörgüçten yalnız az bir bölüm kalır."},{"facet_id":"F002","role":"extension","statement":"Yağ kaybının sonucu olarak hörgücün tepesi belirginliğini yitirip aşağı çöker."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bütün bedenin veya herhangi bir varlığın güç ve ağırlık kaybetmesi anlamını ekler.","collision":"Hayvanın genel olarak zayıflamasıyla karışır.","fit":"broadening","loses":"Deve hörgücünün tepesinin çökmesi sonucunu açıkça göstermez.","preserves":"Yağ kaybı ve küçülme yönünü genel olarak korur."},"text":"zayıflamak"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu sonucu doğuran yağ tükenmesini ve hörgücün büyük ölçüde erimesini eksiltir.","preserves":"Hörgüç tepesinin aşağı yönelmesi sonucunu korur."},"text":"hörgücü düşmek"}],"identity_rationale":"Tanıklıklar devenin hörgücündeki yağın tükenmesini, geriye çok az bölüm kalmasını ve tepenin aşağı çökmesini birlikte bildirir. Verilen dal görüntüsü hem süreci hem de ortaya çıkan biçim değişikliğini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"devenin hörgücünün yağını yitirip çökmesi"}],"lexicalization_note":"Dal yalnız devenin hörgücündeki yağ kaybını ve buna bağlı çökmeyi bildiren yapıyla sınırlıdır; yalın bir zayıflama anlamı kurulmaz.","neighbor_coverage_note":"Yağ kaybı, karşıt dolgunluk ve aynı beden bölümündeki kesme işlemini ayıran üç aday seçildi. Yükseklik, hörgücün anatomik adı, kemik iliği ve hayvan besleme kartları aynı alanı paylaşsa da doğrudan anlam karışıklığı yaratmıyordu; kardeş dallar farklı varlık ve süreçlere bağlıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız deve hörgücünün yağını yitirip çökmesini bildirir. Komşu dal bütün bedenin zayıflamasını merkez alır; hörgücün özel biçim değişikliğini gerektirmez.","focus_only":"Yağ kaybını özellikle deve hörgücünde ve tepenin çökmesi sonucuyla anlatır.","gloss":"hörgücün çökmesi / bedenin zayıflaması","neighbor_only":"Hayvanın veya bedenin genel olarak yağını ve dolgunluğunu yitirmesini anlatır.","neighbor_ref":"root_001589/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda yağ kaybı görünür bir küçülmeye yol açar."},{"boundary_match":"opposed","distinction":"Odak dal dolgunluğun kaybı ve çökmeyle sonuçlanan eksilme kutbundadır. Komşu dal ise etle dolma ve sıkılaşma kutbundadır; kapsamları tam örtüşmese de aynı doluluk ekseninde karşı karşıya gelirler.","focus_only":"Hörgücün yağını yitirerek küçülmesini ve aşağı çökmesini bildirir.","gloss":"yağı tükenmiş hörgüç / dolgun beden","neighbor_only":"Devenin etle dolmasını ve bedenin ya da hörgücün dolgunlaşmasını bildirir.","neighbor_ref":"root_001230/B007","relation_type":"polarity_pair","shared_zone":"İki dal devenin beden veya hörgücündeki dolgunluk derecesini karşıt yönlerden ele alır."},{"boundary_match":"field_only","distinction":"Odak dal besisel tükenme sonucu oluşan erime ve çökmeyi anlatır. Komşu dalın çekirdeği dışarıdan yapılan kesme işlemidir; ortak beden bölümü, işlemleri eş anlamlı kılmaz.","focus_only":"Hörgüç kendiliğinden yağını yitirir ve tepesi çöker.","gloss":"hörgücün erimesi / hörgücün kesilmesi","neighbor_only":"Hörgücün bir parçasının dışarıdan kesilmesini veya kesilmiş parçayı bildirir.","neighbor_ref":"root_000572/B003","relation_type":"same_field","shared_zone":"Her iki dal aynı beden bölümündeki küçülme veya eksilmeyle ilgilidir."}],"source_phrase_ar":"خشع سنام البعير إذا ذهب إلا أقله (maqayis)؛ خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه (tahdhib)","source_summary":"Tanıklıklar hörgücün büyük ölçüde erimesinde birleşir; daha ayrıntılı anlatım yağın tükenmesini ve hörgüç tepesinin aşağı çökmesini aynı sürecin aşamaları olarak açıklar.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه خشوع سنام البعير إذا ذهب شحمه أو لم يبق منه إلا القليل وتطأطأ شرفه","what_is_not_ar":"خشوع الإنسان والأرض والكواكب وخراشي الصدر"},"support_links":["sup_5989c8d9b09f6867699d"]},{"boundary":"Anlam yalnız göğüsten gelen yapışkan salgının çıkarılmasını bildiren eski söz öbeğine aittir; genel tükürme, öksürme veya kusma anlamı taşımaz.","branch_kind":"collocation","branch_ref":"root_000412/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","surface_ar":"خَٰشِعَةٌ"}],"gloss":"göğüsten yapışkan salgı çıkarmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi göğsünden gelen bir salgıyı çıkarıp dışarı atar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çıkarılan göğüs salgısının yapışkan olduğu özellikle belirtilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir aktarım, kullanımı nesne alan ve başka yerde işitilmemiş sınırlı bir yapı olarak kaydeder."}}],"root_ar":"خ ش ع","root_id":"root_000412","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göğüsten gelen yapışkan salgının ağız yoluyla çıkarılıp dışarı atılmasını anlatır.","boundary_detail":"Anlam yalnız göğüsten gelen yapışkan salgının çıkarılmasını bildiren eski söz öbeğine aittir; genel tükürme, öksürme veya kusma anlamı taşımaz.","branch_image_ar":"رمي خراشي الصدر","concept_gloss":"göğüsten yapışkan salgı çıkarmak","contextual_glosses":[{"applicability":"Kişinin göğsünden ağzına gelen koyu salgıyı çıkarıp attığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynak bölgeyi, salgının niteliğini ve atma eylemini korur."},"facet_ids":["F001","F002"],"text":"yapışkan göğüs salgısını dışarı atmak","usage_role":"contextual"}],"definition":"Göğüsten gelen yapışkan salgıyı çıkarıp ağız yoluyla dışarı atmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi göğsünden gelen bir salgıyı çıkarıp dışarı atar."},{"facet_id":"F002","role":"specialization","statement":"Çıkarılan göğüs salgısının yapışkan olduğu özellikle belirtilir."},{"facet_id":"F003","role":"source_variant","statement":"Bir aktarım, kullanımı nesne alan ve başka yerde işitilmemiş sınırlı bir yapı olarak kaydeder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ağızda oluşan sıradan tükürüğü atma anlamını ekler.","collision":"Sıradan tükürme eylemiyle doğrudan karışır.","fit":"displacement","loses":"Salgının göğüsten gelmesini ve yapışkan niteliğini dışarıda bırakır.","preserves":"Bir sıvıyı ağız yoluyla dışarı atma hareketini korur."},"text":"tükürmek"},{"category":"confusable","error_profile":{"adds":"Salgı bulunmadan gerçekleşebilen her türlü öksürme olayını ekler.","collision":"Salgı çıkarılmayan kuru öksürükle karışır.","fit":"broadening","loses":"Yapışkan salgının gerçekten çıkarılıp dışarı atılması sonucunu zorunlu kılmaz.","preserves":"Göğüs ve ağız yolunu içeren bedensel hareket alanını korur."},"text":"öksürmek"}],"identity_rationale":"Tanıklıklar kişinin göğsünden gelen yapışkan bir salgıyı çıkarıp dışarı atması üzerinde birleşir. Bir aktarım, fiilin bu yapıda nesne alan ve başka yerde duyulmamış bir kullanım olduğunu ayrıca belirtir; bu kayıt dalın bağımsız bir genel anlam değil, sınırlı bir söz öbeği olduğunu doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"göğüsten gelen yapışkan salgıyı çıkarıp atmak"}],"lexicalization_note":"Dal yalnız göğüsten gelen yapışkan salgıyı dışarı atmayı bildiren söz öbeğiyle sınırlıdır; fiile yalın bir çıkarma veya tükürme anlamı verilmez.","neighbor_coverage_note":"Göğüsten çıkarma, sıradan tükürme ve kusma ile doğrudan karışabilecek üç aday seçildi. Bağırsak boşaltma, nezle, beden çıkışları, irinli akıntı ve göğüs eti kartları yalnız geniş beden alanını paylaşır; kardeş dalların anlam çekirdekleri ayrıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapışkan bir beden salgısının gerçekten çıkarılmasını bildiren sınırlı bir yapıdır. Komşu dal göğüstekini dışarı atma olayını daha genel verir ve bunu sözün ya da sıkıntının açığa vurulmasına taşıyan atasözü kullanımına sahiptir.","focus_only":"Çıkarılan göğüs salgısının yapışkanlığı ve sınırlı söz öbeği açıkça belirtilir.","gloss":"yapışkan salgı çıkarmak / göğüstekini dışa vurmak","neighbor_only":"Göğüste biriken şeyi dışa vurmayı atasözüne uzanan daha genel bir anlatımla verir.","neighbor_ref":"root_001527/B003","relation_type":"near_synonym","shared_zone":"Her iki dal göğüste bulunan bir şeyin ağız yoluyla dışarı çıkarılmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın maddesi göğüsten gelir ve yapışkandır. Komşu dal ağızdaki tükürüğü ve onu dışarı atma eylemini anlatır; göğüs kaynağı veya koyu kıvam gerektirmez.","focus_only":"Salgının göğüsten gelmesini ve yapışkan olmasını gerektirir.","gloss":"göğüs salgısı çıkarmak / tükürmek","neighbor_only":"Ağızda bulunan sıradan tükürüğün dışarı atılmasını bildirir.","neighbor_ref":"root_000117/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir ağız salgısı dışarı atılır."},{"boundary_match":"field_only","distinction":"Odak dal göğüs kaynaklı yapışkan salgının bilinçli biçimde atılmasını anlatır. Komşu dalın maddesi mide içeriğidir ve temel olay kusmadır; kaynak organ ile çıkarılan madde farklıdır.","focus_only":"Göğüsten gelen yapışkan salgının ağız yoluyla çıkarılmasını bildirir.","gloss":"göğüs salgısı çıkarma / kusma","neighbor_only":"Mide içeriğinin kusma yoluyla yukarı çıkmasını bildirir.","neighbor_ref":"root_000945/B011","relation_type":"same_field","shared_zone":"Her iki dal beden içindeki bir maddenin ağızdan dışarı çıkması alanındadır."}],"source_phrase_ar":"خشع خراشي صدره إذا ألقى بزاقا لزجا (maqayis)؛ خشع الإنسان خراشي صدره إذا ألقى من صدره بزاقا لزجا (jamhara)؛ خشع الرجل خراشي صدره إذا رمى بها؛ جعل خشع واقعا ولم أسمعه لغيره (tahdhib)","source_summary":"Tanıklıklar göğüsten yapışkan bir salgı çıkarıp atma anlamında birleşir. Toplu iddia ayrıca fiilin nesne aldığı ve kullanımın seyrek ya da belirli bir aktarımla sınırlı görüldüğü yönünde bir dil bilgisi kaydı içerir.","sources":["MQ","JA","TA"],"what_is_ar":"يدخل فيه قولهم خشع خراشي صدره إذا ألقى من صدره بزاقا لزجا","what_is_not_ar":"خشوع الإنسان والبصر والأرض والسنام والكواكب"},"support_links":[]},{"boundary":"Bu dal yön, toplumsal itibar veya günün başlangıcı anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B001","candidate_links":[{"candidate_id":"cand_aab903d68bd44ea162f0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüz ve bir şeyin öne bakan yanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlılarda yüz denen organı ve yüz bölgesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin bakana dönük önünü veya görünen dış yanını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı yüzünü ve nesnelerin bakana dönük ön ya da dış yanını birlikte karşılayan genel açıklamadır.","boundary_detail":"Bu dal yön, toplumsal itibar veya günün başlangıcı anlamlarını içermez.","branch_image_ar":"الوجه والمستقبل","concept_gloss":"yüz ve bir şeyin öne bakan yanı","contextual_glosses":[{"applicability":"İnsan veya başka bir canlının yüz bölgesinden söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının yüz organı anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"yüz","usage_role":"general"},{"applicability":"Bir nesnenin bakana dönük görünen yanı kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin karşıya dönük ön yanı anlamını korur."},"facet_ids":["F002"],"text":"ön yüz","usage_role":"contextual"}],"definition":"İnsanın ya da başka bir varlığın yüzü; daha genel olarak bir şeyin bakana dönük, önde bulunan veya dışarıdan görünen yanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlılarda yüz denen organı ve yüz bölgesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir nesnenin bakana dönük önünü veya görünen dış yanını belirtir."}],"identity_rationale":"Kaynak ifadesi, insanın ve başka varlıkların yüzünü, ayrıca bir şeyin bakana dönük ön veya dış yanını ortak bir karşıya dönüklük çekirdeğinde birleştirir. Verilen dal kimliği bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yüz; bir şeyin öne bakan veya görünen yanı"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kötü bir yüz ifadesiyle bakmak"}],"lexicalization_note":"Tanım, biçimin yüz ve ön yan anlamını kapsar; kötü bakış bildiren kalıp yalnız kendi sözlüksel karşılığında tutulur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; insan yüzü ve yön dalları sınırı en çok aydınlatan iki karşılaştırma olduğu için diğerleri yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal insan yüzüyle sınırlıdır; odak dal ise aynı karşıya dönüklük ilişkisini başka canlılara ve nesnelerin ön yüzüne de taşır.","focus_only":"Nesnelerin öne bakan veya görünen yanı da bu dalın kapsamındadır.","gloss":"insan yüzü","neighbor_only":null,"neighbor_ref":"root_000383/B012","relation_type":"near_synonym","shared_zone":"İki dal da insanın yüz bölgesini adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal bir varlığın yüzünü ya da ön yanını adlandırır; komşu dal ise uzamsal yönü, hedefi ve yönelme işlemini anlatır.","focus_only":"Karşıdan görülen somut yüz veya ön yan bu dala özgüdür.","gloss":"ön yüz ile yön","neighbor_only":"Gidilecek yön, hedef ve bir şeyi o yöne sevk etme komşu dala özgüdür.","neighbor_ref":"root_001630/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da karşıya veya ileriye dönüklük ilişkisi bulunur."}],"source_phrase_ar":"الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)","source_summary":"Kaynaklar yüz organında ve bir şeyin karşıya dönük ön yanında birleşir; nesneye genişleyen kullanım, bakana dönük olma ilişkisini korur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجارحة؛ وجه الإنسان وغيره؛ مستقبل الشيء وظاهره وما يقابل الناظر","what_is_not_ar":"ليس الجهة المقصودة ولا الجاه ولا صدر النهار"},"support_links":["sup_c2d5125f6d52cde6f3a8"]},{"boundary":"Yüz yüze karşılaşma ve toplumsal mevki bu yön ve hedef dalının dışında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B002","candidate_links":[{"candidate_id":"cand_1c1584454305238ffa05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yön ve hedef; o yöne sevk etme veya yolu belli etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönülen veya gidilen yönü, tarafı ve hedefi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi tek bir yöne çevirmeyi, göndermeyi veya o yöne gitmeyi belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli kalıplarda çakılın rüzgarla sürülmesini ve yolun yürünerek belirginleşmesini anlatır."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yön adını, yönelme eylemini ve kaynakta belirtilen yapı bağımlı işlemleri birlikte özetler.","boundary_detail":"Yüz yüze karşılaşma ve toplumsal mevki bu yön ve hedef dalının dışında kalır.","branch_image_ar":"الجهة والوجهة","concept_gloss":"yön ve hedef; o yöne sevk etme veya yolu belli etme","contextual_glosses":[{"applicability":"Bir yerin, tarafın veya ulaşılmak istenen hedefin adı olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yön ve hedef olma çekirdeğini korur."},"facet_ids":["F001"],"text":"yönelinen yön veya hedef","usage_role":"general"},{"applicability":"Bir şeyi belirli bir tarafa çevirmek veya göndermek söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi belirli bir yöne sevk etme işlemini korur."},"facet_ids":["F002"],"text":"yöneltmek","usage_role":"contextual"}],"definition":"Bir şeyin dönüldüğü yön, taraf veya hedef ile bir şeyi o yöne çevirmek ya da göndermektir. Belirli kuruluşlarda rüzgarın çakılı sürmesini ve bir yolu yürüyerek izini görünür kılmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönülen veya gidilen yönü, tarafı ve hedefi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi tek bir yöne çevirmeyi, göndermeyi veya o yöne gitmeyi belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli kalıplarda çakılın rüzgarla sürülmesini ve yolun yürünerek belirginleşmesini anlatır."}],"identity_rationale":"Kaynak ifadesi yön ve hedef adlarını, bir şeyi belirli bir yöne gönderme veya çevirme eylemini, rüzgarın çakılı sürmesini ve yürüyerek yolu belli etme kullanımını birlikte verir. Dal çerçevesi bu çekirdek ile yapı bağımlı uzantıları doğru ayırmaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yön, taraf"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yönelinen yön veya hedef"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi belirli bir yöne çevirmek veya göndermek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tek bir yöne çevrilmiş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye doğru yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"rüzgarın çakılı bir yöne sürüklemesi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yolu yürüyerek izini belirginleştirmek"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak"}],"lexicalization_note":"Yön ve hedef çekirdeği ile gönderme, sürükleme ve yolu belirginleştirme gibi belirli kuruluşlara bağlı kullanımlar ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yönelme ve özel ibadet yönü, dalın kapsamını en açık biçimde sınırlayan komşulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yönün ve hedefin kendisini de adlandırır ve bazı özel sevk etme kalıplarını içerir; komşu dal esas olarak bir şeyi amaçlayıp ona gitmeyi anlatır.","focus_only":"Durağan yön adı, nesneyi sevk etme ve yolu yürüyerek belli etme kapsamı vardır.","gloss":"yön ile yönelme","neighbor_only":"Bir şeyi amaçlayıp ona gitme eylemi komşu dalda daha merkezi ve geneldir.","neighbor_ref":"root_001230/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir hedefe doğru dönme veya gitme durumunu kapsar."},{"boundary_match":"partial","distinction":"Odak dal genel yön ve hedef kavramıdır; komşu dal bunu belirli bir ibadet yerleşimine özgü ad olarak sınırlar.","focus_only":"Her türlü yön, hedef ve yöneltme işlemi bu dalda yer alabilir.","gloss":"genel yön ile ibadet yönü","neighbor_only":"İbadet sırasında dönülen özel yön komşu dalın belirleyici sınırıdır.","neighbor_ref":"root_001198/B005","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin dönüp karşısına aldığı yönü belirtebilir."}],"source_phrase_ar":"الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)","source_summary":"Kaynaklar yön, hedef ve yönelme çekirdeğinde birleşir; gönderme, rüzgarla sürükleme ve yolun yürünerek belli edilmesi bu çekirdeğe bağlı özel gerçekleşmelerdir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجهة والنحو والقبلة والمقصد؛ جعل الشيء أو السير على جهة؛ سوق الشيء في طريق؛ بيان الطريق بالسلوك","what_is_not_ar":"ليس مجرد مقابلة الوجه للوجه ولا منزلة الجاه"},"support_links":["sup_b7b23173f29798f89aa3"]},{"boundary":"Bu dal yalnızca yön bildirmez; iki tarafın karşılıklı konumunu veya doğrudan karşılaşmasını gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B003","candidate_links":[{"candidate_id":"cand_1c1584454305238ffa05","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"karşı karşıya gelme ve doğrudan yüzüne söyleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki tarafın birbirinin karşısına gelmesini veya karşılıklı durmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye iyi ya da kötü bir sözü doğrudan yüzüne söylemeyi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel karşılıklı konumu ve bunun sözlü karşılaşmaya uzanan özel kullanımını birlikte karşılar.","boundary_detail":"Bu dal yalnızca yön bildirmez; iki tarafın karşılıklı konumunu veya doğrudan karşılaşmasını gerektirir.","branch_image_ar":"المواجهة والتقابل","concept_gloss":"karşı karşıya gelme ve doğrudan yüzüne söyleme","contextual_glosses":[{"applicability":"Kişilerin veya şeylerin karşılıklı konuma gelmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki tarafın karşılıklı konumlanmasını korur."},"facet_ids":["F001"],"text":"yüz yüze gelmek","usage_role":"general"},{"applicability":"Bir sözün kişiye doğrudan ve karşısında söylenmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlü karşılaşma ve doğrudanlık koşulunu korur."},"facet_ids":["F002"],"text":"yüzüne söylemek","usage_role":"contextual"}],"definition":"İki kişi veya şeyin birbirinin karşısında bulunması ya da yüz yüze gelmesidir; bir kişiye sözü doğrudan yüzüne söylemek de bu karşılaşmanın özel bir biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki tarafın birbirinin karşısına gelmesini veya karşılıklı durmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye iyi ya da kötü bir sözü doğrudan yüzüne söylemeyi belirtir."}],"identity_rationale":"Kaynak ifadesi iki yüzün veya iki şeyin birbirinin karşısına gelmesini, bir kişinin karşılanmasını ve sözle doğrudan karşı karşıya gelmeyi açıkça bir arada verir. Dalın karşılaşma ve karşılıklı konumlanma çerçevesi bu içeriğe uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkmak, onunla yüz yüze gelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"karşılaşma, yüzleşme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"karşında, tam karşı tarafta"}],"lexicalization_note":"Karşılıklı konum çekirdeği korunur; yüz yüze gelme ve sözle karşısına çıkma, ilgili biçim ve kalıplara bağlı anlatılır.","neighbor_coverage_note":"Tüm adaylar incelendi; geniş karşıt konum alanı ile karşılıklı görünme dalı, fiziksel ve sözlü karşılaşma sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iki tarafın doğrudan karşılaşmasını ve iletişimsel yüzleşmeyi öne çıkarır; komşu dal karşı, ön ve yön ilişkilerini daha geniş uzamsal kapsamda işler.","focus_only":"Yüz yüze gelme ve sözü doğrudan birinin yüzüne söyleme belirgindir.","gloss":"yüz yüze karşılaşma","neighbor_only":"Ön ve arka karşıtlığı ile dağ veya arazi yüzü gibi daha geniş uzamsal kapsam vardır.","neighbor_ref":"root_001198/B001","relation_type":"near_neighbor","shared_zone":"İki dal da şeylerin birbirine karşı konumlanmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yüz yüze gelmeyi kişiler arası sözlü karşılaşmaya kadar taşır; komşu dal karşılıklı görünür olma durumuna odaklanır.","focus_only":"Sözlü yüzleşme ve bir kişiye doğrudan hitap etme kapsamı vardır.","gloss":"karşılıklı görünme","neighbor_only":"Toplulukların, evlerin veya ateşlerin birbirini görecek konumda olması özellikle belirtilir.","neighbor_ref":"root_000531/B004","relation_type":"near_synonym","shared_zone":"İki dal da iki tarafın birbirini görecek biçimde karşılaşmasını anlatır."}],"source_phrase_ar":"واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)","source_summary":"Kaynaklar karşılıklı konumlanma ve yüz yüze gelme üzerinde birleşir; sözle doğrudan karşılaşma bu temel ilişkinin iletişim alanındaki özel kullanımıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"مقابلة وجه بوجه؛ استقبال الشخص أو الشيء؛ الوجاه والتجاه وما يكون قبالة غيره؛ المواجهة بالكلام","what_is_not_ar":"ليس مطلق الجهة ولا القصد الباطن"},"support_links":["sup_b7b23173f29798f89aa3"]},{"boundary":"Burada yüz, varlığın kendisini temsil eden aktarmalı bir anlatımdır; bağımsız ve kesin bir yalın anlam varsayılmaz.","branch_kind":"unresolved","branch_ref":"root_001630/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüzün varlığın kendisini temsil etmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzün, yorum yoluyla varlığın kendisi veya bütün kişi yerine kullanılmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yüz sözünün bağlama göre bütün kişi veya varlık yerine yorumlandığı kullanımlarda geçerlidir.","boundary_detail":"Burada yüz, varlığın kendisini temsil eden aktarmalı bir anlatımdır; bağımsız ve kesin bir yalın anlam varsayılmaz.","branch_image_ar":"الوجه عن الذات","concept_gloss":"yüzün varlığın kendisini temsil etmesi","contextual_glosses":[{"applicability":"Yüzün bütün kişiyi temsil ettiği kabul edilen bağlamı açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzden bütün kişiye kurulan temsil ilişkisini bağlam içinde korur."},"facet_ids":["F001"],"text":"kişinin kendisi","usage_role":"explanatory"}],"definition":"Yüz sözünün, bazı bağlamlarda bir varlığın kendisini veya kişiyi bütünüyle temsil edecek biçimde kullanılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzün, yorum yoluyla varlığın kendisi veya bütün kişi yerine kullanılmasını belirtir."}],"identity_rationale":"Kaynak ifadesi yüzün bazen bir varlığın kendisi yerine kullanılabildiğini bildirir, ancak bunu kesin ve bağımsız bir temel anlam olarak değil, aktarıma dayalı bir yorum olarak sunar. Dal korunabilir, fakat bu yorum niteliği tanımın sınırı olmalıdır.","lexicalization_note":"Sözlüksel birim türü çözülmemiştir; tanım yalnız kaynakta ihtiyatla verilen yüzün varlığın kendisini temsil etmesi yorumuyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan varlığın kendisini adlandıran dal, bu yorumun aktarmalı sınırını göstermek için yeterlidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bu anlamı yüzün bütünü temsil etmesi yoluyla ve ihtiyatlı bir yorum olarak kurar; komşu dal ise varlığın kendisini doğrudan adlandırır.","focus_only":"Yüz sözünden bütün varlığa giden aktarmalı ve yoruma bağlı kullanım vardır.","gloss":"varlığın kendisi","neighbor_only":"Varlığın kendisini doğrudan adlandırma ve pekiştirme kullanımları vardır.","neighbor_ref":"root_001533/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya şeyin bütün varlığını gösterebilir."}],"source_phrase_ar":"ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)","source_summary":"Kaynaklar yüzün varlığın kendisi yerine yorumlanabileceğini aktarır; anlatımın aktarmalı ve ihtiyatlı niteliği bağımsız bir temel anlam kurulmasını engeller.","sources":["MQ","MU"],"what_is_ar":"التعبير بالوجه عن الذات أو الشخص نفسه عند من يفسره بذلك","what_is_not_ar":"ليس الجارحة وحدها ولا طلب الجاه"},"support_links":[]},{"boundary":"Mekansal yön adı bu dalın çekirdeği değildir; esas olan bir hedefi amaç edinip ona yönelmektir.","branch_kind":"unresolved","branch_ref":"root_001630/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"amaç edinip yönelme; ibadette içtenlikle bağlanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefi amaç edinip ona yönelmeyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İbadet bağlamında amacı yalnız yaratıcıya yöneltmeyi ve içten bağlılığı belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel amaçlı yönelişi ve ibadet bağlamındaki yalnızca yaratıcıya dönük içten yönelişi birlikte açıklar.","boundary_detail":"Mekansal yön adı bu dalın çekirdeği değildir; esas olan bir hedefi amaç edinip ona yönelmektir.","branch_image_ar":"القصد والتوجه","concept_gloss":"amaç edinip yönelme; ibadette içtenlikle bağlanma","contextual_glosses":[{"applicability":"Bir hedefin bilinçli olarak seçilip ona doğru yönelinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedef seçme ve ona yönelme ilişkisini korur."},"facet_ids":["F001"],"text":"amaç edinip yönelmek","usage_role":"general"},{"applicability":"İbadetin yalnız yaratıcıya yöneltilmesi ve içten bağlılık vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İbadette tek hedefe yönelme ve içtenlik koşulunu korur."},"facet_ids":["F002"],"text":"kendini içtenlikle adamak","usage_role":"contextual"}],"definition":"Bir şeyi amaç edinmek ve ona yönelmek; ibadet bağlamında ise yönelişi yalnız yaratıcıya ayırıp içtenlikle ona bağlanmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefi amaç edinip ona yönelmeyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"İbadet bağlamında amacı yalnız yaratıcıya yöneltmeyi ve içten bağlılığı belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeye doğru yönelme ve amacı kaybetme örneklerini, ayrıca ibadeti yalnız yaratıcıya yöneltme ve bunu amaç edinme anlatımlarını verir. Dalın niyet ve yöneliş çerçevesi bu ortak amaç çekirdeğini korur.","lexicalization_note":"Birim türü çözülmemiştir; tanım, kaynakta verilen amaç edinme ve bağlama bağlı içten yöneliş anlamlarıyla sınırlı tutulur.","neighbor_coverage_note":"Adayların tamamı incelendi; genel amaçlama dalı ile aynı kökün yön dalı, niyet ve mekan ayrımını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin hedefini ve niyetli yönelişini anlatır; komşu dal ise yönü, hedef yerini ve yöneltme işlemini adlandırır.","focus_only":"Niyet, amaç edinme ve içten yöneliş bu dala özgüdür.","gloss":"amaç ile yön","neighbor_only":"Yönün veya tarafın kendisi ile nesneyi o yöne sevk etme komşu dala özgüdür.","neighbor_ref":"root_001630/B002","relation_type":"near_neighbor","shared_zone":"Bir hedefe doğru dönme düşüncesi iki dalın kesiştiği alandır."}],"source_phrase_ar":"وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)","source_summary":"Kaynaklar amaç edinme ve yönelme çekirdeğini paylaşır; ibadet anlatımları bu yönelişi yalnız yaratıcıya ayırma ve içtenlik koşuluyla özelleştirir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"القصد والمقصد؛ التوجه إلى الشيء أو إلى الله؛ إسلام الوجه وإقامته وإرادة وجه الله على تفسير الإخلاص والتوجه","what_is_not_ar":"ليس الذات على تفسيرها ولا الجاه بين الناس"},"support_links":[]},{"boundary":"Buradaki önde olma fiziksel ön yüz değil, toplumsal mevki, saygınlık ve önderliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B006","candidate_links":[{"candidate_id":"cand_2068f0e21657d8add22b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"toplumsal itibar, yüksek mevki ve önde gelen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin başkaları yanındaki toplumsal mevki, değer ve saygınlığını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir topluluğun önderini veya bir yerin seçkin ve önde gelen kişilerini belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin saygın konumunu hem de topluluğun önder veya ileri gelenlerini kapsayan açıklamadır.","boundary_detail":"Buradaki önde olma fiziksel ön yüz değil, toplumsal mevki, saygınlık ve önderliktir.","branch_image_ar":"الوجاهة والجاه","concept_gloss":"toplumsal itibar, yüksek mevki ve önde gelen kişi","contextual_glosses":[{"applicability":"Bir kişinin toplumsal konumu ve başkaları yanındaki değeri anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişisel saygınlık ve yüksek mevki anlamını korur."},"facet_ids":["F001"],"text":"itibarlı ve yüksek mevkili","usage_role":"general"},{"applicability":"Bir topluluğun veya yerleşimin önde gelen seçkin kişileri anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk içinde önder ve seçkin kişiler anlamını korur."},"facet_ids":["F002"],"text":"ileri gelenler","usage_role":"contextual"}],"definition":"Bir kişinin topluluk içinde sahip olduğu yüksek mevki, değer ve saygınlıktır; ayrıca bir topluluğun önderini veya bir yerin önde gelen kişilerini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin başkaları yanındaki toplumsal mevki, değer ve saygınlığını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir topluluğun önderini veya bir yerin seçkin ve önde gelen kişilerini belirtir."}],"identity_rationale":"Kaynak ifadesi kişinin toplulukta veya yönetici yanında sahip olduğu mevki ve değeri, ayrıca topluluğun ya da yerleşimin önde gelenlerini açıkça birlikte verir. Dalın itibar ve önderlik çerçevesi bu toplumsal kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"topluluğun önderi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yerleşimin ileri gelenleri"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"itibarlı, yüksek mevkili"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"toplumsal itibar ve mevki"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"itibarlı ve yüksek mevkili olmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"onu itibarlı ve yüksek mevkili kılmak"}],"lexicalization_note":"Toplumsal mevki çekirdeği ile önde gelen kişi ve topluluk ileri gelenleri bildiren kalıplar ayrı ama bağlantılı biçimde tanımlanır.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel yücelik ile yakınlıktan doğan mevki, toplumsal itibarın iki temel sınırını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal toplumsal mevkiyi ve bu mevkiyi taşıyan önder kişileri adlandırır; komşu dal daha genel yücelik ve şeref alanını kapsar.","focus_only":"Topluluk önderi ve bir yerin ileri gelenleri gibi kişi adlandırmaları vardır.","gloss":"itibar ve yücelik","neighbor_only":"Genel yücelik, şeref ve derece yüksekliği daha geniş biçimde yer alır.","neighbor_ref":"root_001042/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin yüksek değeri ve şerefli konumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal toplum içindeki itibar ve önderliği anlatır; komşu dal birine yakın bulunmaktan doğan derece ve gözde olma ilişkisini öne çıkarır.","focus_only":"Önderlik, seçkinlik ve yüksek toplumsal değer bu dala özgüdür.","gloss":"mevki ile yakınlık","neighbor_only":"Bir başkasına yakınlık, onun yanındaki derece ve gözde olma komşu dala özgüdür.","neighbor_ref":"root_000639/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişinin başkaları yanındaki değerli konumunu gösterebilir."}],"source_phrase_ar":"وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)","source_summary":"Kaynaklar toplumsal mevki ve değer anlamında birleşir; önder ve ileri gelenler anlatımı bu mevkinin kişiler veya topluluk içindeki taşıyıcılarını adlandırır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"الوجاهة؛ الجاه والمنزلة والقدر؛ وجه القوم ووجوه البلد أي أشرافهم وسادتهم","what_is_not_ar":"ليس الجارحة ولا الجهة المكانية"},"support_links":["sup_5989c8d9b09f6867699d"]},{"boundary":"Anlam yalnız günün ilk bölümüyle ilgilidir; genel başlangıç veya üstünlük anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001630/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"günün başı, ilk saatleri","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günün başlangıcını ve ilk bölümünü belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız günün başlangıcını bildiren kaynakta verilen zaman kalıbı için geçerlidir.","boundary_detail":"Anlam yalnız günün ilk bölümüyle ilgilidir; genel başlangıç veya üstünlük anlamına genişletilmez.","branch_image_ar":"وجه النهار وصدره","concept_gloss":"günün başı, ilk saatleri","contextual_glosses":[{"applicability":"Bir olayın günün başlangıcında gerçekleştiğini doğal akışta belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün başlangıcındaki zaman konumunu korur."},"facet_ids":["F001"],"text":"günün erken saatlerinde","usage_role":"contextual"}],"definition":"Günün ilk bölümü, yani günün başlangıcıdır; anlam yalnız bu zaman bildiren kuruluş içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günün başlangıcını ve ilk bölümünü belirtir."}],"identity_rationale":"Kaynak ifadesi yalnız günün başını ve ilk bölümünü bildiren belirli bir kalıbı destekler. Geçici çerçevedeki her şeyin başlangıcı veya en değerli görünen yanı biçimindeki genelleme kaynak ifadesinde yer almadığından dal bu kalıpla sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"günün başı, ilk saatleri"}],"lexicalization_note":"Tanım yalnız günün başlangıcını bildiren sabit kuruluşa bağlıdır ve yalın bir kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar incelendi; sabah vakti ve genel başlangıç dalları, kalıbın zamanla sınırlı kapsamını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kuruluşla günün başını adlandırır; komşu dal sabah vaktini ve o vakitte yapılan erken hareketleri daha geniş biçimde kapsar.","focus_only":"Belirli bir kalıp yalnız günün ilk bölümünü adlandırır.","gloss":"günün başı ile sabah","neighbor_only":"Sabah vakti yanında erken çıkma, erken yol alma ve bir işe çabuk davranma eylemleri de vardır.","neighbor_ref":"root_000143/B001","relation_type":"near_synonym","shared_zone":"İki dal da günün erken bölümünü zaman olarak gösterebilir."},{"boundary_match":"partial","distinction":"Odak dal günün başıyla sınırlı bir zaman kalıbıdır; komşu dal başlangıç anlamını farklı varlık ve süreçlere geneller.","focus_only":"Yalnız günün başlangıcına bağlı zaman anlamı vardır.","gloss":"günün başı ile genel başlangıç","neighbor_only":"Herhangi bir şeyin başlangıcı ile bitki ve ayın ilk görünümü de kapsanır.","neighbor_ref":"root_001078/B005","relation_type":"near_neighbor","shared_zone":"Günün ilk bölümü, genel başlangıç düşüncesiyle kesişir."}],"source_phrase_ar":"وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)","source_summary":"Kaynaklar belirli zaman kalıbını günün başı veya ilk bölümü olarak açıklar ve daha genel bir başlangıç anlamı vermez.","sources":["JA","TA","MU"],"what_is_ar":"وجه النهار؛ صدر النهار وأوله؛ مبدأ الشيء وأشرف ظاهره","what_is_not_ar":"ليس جهة السير ولا مقابلة الأشخاص"},"support_links":[]},{"boundary":"Dal, fiziksel yüzü veya salt uzamsal yönü değil, söz ve işte uygun yol ile doğruluğu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"sözün veya işin doğru yönü ve ona uygun düzenleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözün amaçlanan yönünü ve görüşün doğru biçimini belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi olması gerektiği gibi düzenlemeyi veya doğru yolundan saptırmayı belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıpta genel beceriksizliği, bir aktarımda ise tuvaletini yapmayı bile becerememeyi anlatır."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözün kastını, görüşün doğruluğunu ve işin gereken biçimde yürütülmesini karşılayan çekirdek açıklamadır.","boundary_detail":"Dal, fiziksel yüzü veya salt uzamsal yönü değil, söz ve işte uygun yol ile doğruluğu anlatır.","branch_image_ar":"وجه الأمر وصوابه","concept_gloss":"sözün veya işin doğru yönü ve ona uygun düzenleme","contextual_glosses":[{"applicability":"Bir görüşün veya işin uygun ve doğru yolu kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğru yol ve uygunluk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"doğru yaklaşım","usage_role":"general"},{"applicability":"Kaynakta verilen özel kalıpta kişinin genel beceriksizliği anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel kalıbın işlerini doğru yürütemeyen kişi anlamını korur."},"facet_ids":["F003"],"text":"hiçbir işi doğru dürüst yapamayan","usage_role":"contextual"}],"definition":"Bir sözün amaçlanan yönü veya bir işin olması gereken doğru yolu ve bu yola uygun düzenlenmesidir. Özel bir kuruluşta, hiçbir işi doğru yürütemeyen beceriksiz kişiyi anlatır ve bir aktarımda bu beceriksizlik tuvaletini yapmaya kadar daraltılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözün amaçlanan yönünü ve görüşün doğru biçimini belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bir işi olması gerektiği gibi düzenlemeyi veya doğru yolundan saptırmayı belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Özel bir kalıpta genel beceriksizliği, bir aktarımda ise tuvaletini yapmayı bile becerememeyi anlatır."}],"identity_rationale":"Kaynak ifadesi sözün amaçlanan yönünü, görüşün doğru biçimini, bir işi olması gerektiği gibi düzenlemeyi ve bu doğrultudan sapmayı verir. Beceriksiz kişiye ilişkin kalıp da işini doğru yürütememe çekirdeğine bağlı özel bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sözün amaçlanan yönü"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"doğru görüş"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"aklına bir görüş gelmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir şeyi doğru yolundan saptırmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"işi gerektiği gibi düzenleyip her şeyi yerine koymak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi"}],"lexicalization_note":"Söz ve işte uygun yol çekirdeği, görüş ve düzenleme kalıpları ile beceriksizlik bildiren özel kuruluş birbirine karıştırılmadan korunur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; doğru davranış yolunu bulma ve genel amaca uygunluk dalları, odak anlamın sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal söz ve görüşün yönünü, işi gereken biçimde düzenlemeyi ve bunun olumsuz kalıbını içerir; komşu dal kişinin doğru davranış yolunu bulmasına odaklanır.","focus_only":"Sözün kastı, görüşün yönü ve özel beceriksizlik kalıbı bu dalda yer alır.","gloss":"işin doğrusunu bulma","neighbor_only":"Kişinin işin doğru tarafını bulması ve davranışında olgunluk göstermesi komşu dalda öne çıkar.","neighbor_ref":"root_000565/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir işte doğru yaklaşımı bulup uygun davranmayı kapsar."},{"boundary_match":"partial","distinction":"Odak dal doğru yön ve gereken düzenleme imgesini korur; komşu dal amaca isabet ve düzgünlük anlamını daha geniş eylem alanlarına taşır.","focus_only":"Sözün amaçlanan yönü ve belirli kuruluşlara bağlı beceriksizlik anlatımı vardır.","gloss":"doğruluk ve uygunluk","neighbor_only":"Söz, eylem, atış ve yönetimde hedefe uygunluk ile doğru çizgide olma daha genel kapsamlıdır.","neighbor_ref":"root_000687/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir söz veya işin doğru ve amaca uygun olmasını anlatır."}],"source_phrase_ar":"وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)","source_summary":"Kaynaklar söz, görüş ve işte amaçlanan doğru yol çekirdeğini paylaşır. Beceriksizlik kalıbı genel olarak hiçbir işi doğru yürütememe, daha dar bir aktarımda ise tuvaletini yapmayı becerememe biçiminde açıklanır.","sources":["JA","SI","TA","MU"],"what_is_ar":"الوجه في الرأي والكلام والأمر؛ السنن والصواب والتدبير الحسن؛ استقامة الأمر أو عدمها","what_is_not_ar":"ليس الوجه العضوي ولا الجهة المحضة"},"support_links":[]},{"boundary":"Anlam yalnız yaşlı kişiyi konu alan özel eylem kuruluşunda geçerlidir; genel yönelme anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_001630/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yaşlanıp ömrünün son dönemine girmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yaşlı kişinin daha ileri yaşa geçmesini ve ömrünün son dönemine yaklaşmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yaşlı kişinin ileri yaşa geçmesini bildiren kaynakta verilen özel kuruluş için geçerlidir.","boundary_detail":"Anlam yalnız yaşlı kişiyi konu alan özel eylem kuruluşunda geçerlidir; genel yönelme anlamı değildir.","branch_image_ar":"توجه الشيخ","concept_gloss":"yaşlanıp ömrünün son dönemine girmek","contextual_glosses":[{"applicability":"Bir yaşlının ileri yaşa ulaşıp hayatının son dönemine girmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İleri yaşa geçiş anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"iyice yaşlanmak","usage_role":"contextual"}],"definition":"Yaşlı bir kişinin yaşının ilerlemesi, ömrünün son dönemine girmesi ve gençlikten uzaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yaşlı kişinin daha ileri yaşa geçmesini ve ömrünün son dönemine yaklaşmasını belirtir."}],"identity_rationale":"Kaynak ifadesi yaşlı kişinin ömründe ileri gidip gençlikten uzaklaşmasını, yaşının büyümesini ve hayatın son dönemine yönelmesini aynı özel kuruluşla açıklar. Dalın yaşlanma ve ömrün gerileme dönemi çerçevesi buna uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yaşlanıp ömrünün son dönemine girmek"}],"lexicalization_note":"Tanım yaşlı kişinin ileri yaşa geçmesini bildiren özel sözlüksel kuruluşla sınırlıdır ve yalın anlama genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel yaşlılık ve zihinsel düşüşlü aşırı yaşlılık, özel kuruluşun sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel bir kuruluşla yaşın ilerleyip ömrün son dönemine girmesini anlatır; komşu dal yaşlı kişiyi ve yaşlılık halini genel olarak adlandırır.","focus_only":"Belirli bir eylem kuruluşu yaşlı kişinin daha da ilerleyen yaşa geçişini vurgular.","gloss":"ileri yaşa geçmek","neighbor_only":"Yaşlı erkek ve kadın adları ile yaşlılık durumu genel olarak kapsanır.","neighbor_ref":"root_000834/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin yaşlanmasını ve yaşlılık durumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız yaşın ilerlemesini bildirir; komşu dal ise aşırı yaşlılığın getirdiği zihinsel düşüşü zorunlu olarak içerir.","focus_only":"İleri yaşa geçiş vardır, zihinsel yeti kaybı zorunlu değildir.","gloss":"yaşlanma ile düşkünlük","neighbor_only":"Aşırı yaşlılıkta bilinç ve bilgi yetilerinin bozulması belirleyici koşuldur.","neighbor_ref":"root_000559/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da insan ömrünün ileri ve gerileyen dönemleriyle ilgilidir."}],"source_phrase_ar":"توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)","source_summary":"Kaynaklar özel kuruluşu yaşlı kişinin yaşının ilerlemesi ve ömrünün geriye kalan son dönemine girmesi olarak ortak biçimde açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"كبر السن والإدبار في العمر؛ توجه الشيخ إذا ولى وكبر","what_is_not_ar":"ليس التوجه إلى جهة ولا الجاه"},"support_links":[]},{"boundary":"Anlam, doğumda ellerin veya ön ayakların önce çıkması koşuluna bağlıdır; genel doğum ya da toplumsal itibar değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"doğumda ellerin veya ön ayakların önce çıkması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yavrunun doğumda ellerinin veya ön ayaklarının önce çıkmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Annenin yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yavrunun sunumunu ve annenin bu sunumla doğurmasını birlikte açıklayan özel doğum terimidir.","boundary_detail":"Anlam, doğumda ellerin veya ön ayakların önce çıkması koşuluna bağlıdır; genel doğum ya da toplumsal itibar değildir.","branch_image_ar":"الولادة باليدين أولا","concept_gloss":"doğumda ellerin veya ön ayakların önce çıkması","contextual_glosses":[{"applicability":"İnsan yavrusunun elleri önce çıkacak biçimde doğması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan doğumunda ellerin önce çıkması koşulunu korur."},"facet_ids":["F001"],"text":"elleri önde doğmak","usage_role":"contextual"},{"applicability":"Hayvan yavrusunun ön ayakları önce çıkacak biçimde doğması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan doğumunda ön ayakların önce çıkması koşulunu korur."},"facet_ids":["F001"],"text":"ön ayakları önde doğmak","usage_role":"contextual"}],"definition":"Doğum sırasında bir yavrunun ellerinin veya ön ayaklarının bedeninin öteki bölümlerinden önce çıkması ve annenin yavruyu bu biçimde doğurmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yavrunun doğumda ellerinin veya ön ayaklarının önce çıkmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Annenin yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmasını belirtir."}],"identity_rationale":"Kaynak ifadesi doğum sırasında yavrunun ellerinin veya ön ayaklarının rahimden önce çıkmasını ve annenin onu bu biçimde doğurmasını açıkça verir. Dalın doğum sunumuna ilişkin çerçevesi bu koşulu tam korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"elleri veya ön ayakları önce çıkan yavru"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak"}],"lexicalization_note":"Önce elleri çıkan yavruyu bildiren biçim ile annenin bu biçimde doğurmasını bildiren kalıp ayrı sözlüksel gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Tüm adaylar incelendi; ayakların önce çıktığı karşı sunum ile yavruyu karşılayan kişi, doğum olayındaki en açıklayıcı iki sınırı verir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal ellerin veya ön ayakların önce çıkmasını, komşu dal ise ayakların baştan önce çıkmasını belirtir; ayrım doğumda öne gelen uzuv üzerindedir.","focus_only":"Doğumda ellerin veya ön ayakların önce çıkması vardır.","gloss":"önde çıkan uzuv","neighbor_only":"Doğumda ayakların baştan önce çıkması vardır.","neighbor_ref":"root_001551/B002","relation_type":"polarity_pair","shared_zone":"İki dal da yavrunun olağan dışı bir uzuv sunumuyla doğmasını anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal yavrunun çıkış biçimini niteler; komşu dal ise çıkan yavruyu karşılayan kişinin eylemini veya görevini anlatır.","focus_only":"Yavrunun doğumda hangi uzvunun önce çıktığını niteleyen sunum biçimidir.","gloss":"doğum sunumu ve doğumu karşılama","neighbor_only":"Doğum sırasında yavruyu karşılayıp alan kişinin görevidir.","neighbor_ref":"root_001198/B007","relation_type":"thematic","shared_zone":"İki dal da doğum olayının katılımcıları ve aşamalarıyla ilgilidir."}],"source_phrase_ar":"للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)","source_summary":"Kaynaklar yavrunun doğum kanalından elleri veya ön ayakları önce çıkması koşulunda birleşir; adlandırma hem yavruya hem de annenin doğurma eylemine uygulanır.","sources":["MQ","SI","TA"],"what_is_ar":"الوجيه من المولود إذا خرجت يداه قبل غيرهما؛ أوجهت به أمه إذا ولدته كذلك","what_is_not_ar":"ليس وجاهة المنزلة ولا الوجه العضوي العام"},"support_links":[]},{"boundary":"Bu, uyak düzenindeki belirli bir harftir; genel yöneltme eylemi veya bağımsız bir hareket adı değildir.","branch_kind":"bare","branch_ref":"root_001630/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harfi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız klasik şiirin uyak yapısındaki bu belirli konumu adlandıran teknik kullanım için geçerlidir.","boundary_detail":"Bu, uyak düzenindeki belirli bir harftir; genel yöneltme eylemi veya bağımsız bir hareket adı değildir.","branch_image_ar":"توجيه القافية","concept_gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf","contextual_glosses":[{"applicability":"Teknik uyak çözümlemesinde harfin konumunu kısa ve anlaşılır biçimde açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki belirli uyak öğesi arasında bulunma özelliğini bağlam içinde korur."},"facet_ids":["F001"],"text":"aradaki uyak harfi","usage_role":"explanatory"}],"definition":"Klasik uyak düzeninde kurucu uzun ünlü ile şiirin ana uyak harfi arasında bulunan harftir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harfi belirtir."}],"identity_rationale":"Kaynak ifadelerinin tümü şiirde kurucu uzun ünlü ile ana uyak harfi arasında bulunan harfi tanımlar. Geçici çerçevedeki hareket seçeneği kaynak ifadesiyle desteklenmediğinden tanım yalnız aradaki harf olarak düzeltilmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kurucu uzun ünlü ile ana uyak harfi arasındaki harf"}],"lexicalization_note":"Dal, teknik şiir teriminin yalın biçimini tanımlar; başka yöneltme kalıpları bu teknik anlama taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kurucu uzun ünlü ve ana uyak harfi, teknik terimin iki yanındaki konumu doğrudan gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal iki öğe arasındaki harfi, komşu dal ise bu düzeni kuran uzun ünlünün kendisini belirtir.","focus_only":"Kurucu uzun ünlü ile ana uyak harfi arasındaki harftir.","gloss":"iki ayrı uyak öğesi","neighbor_only":"Uyakta kalıcı olan ve ana uyak harfinden bir harf uzakta duran kurucu uzun ünlüdür.","neighbor_ref":"root_000031/B004","relation_type":"same_field","shared_zone":"İki dal da aynı klasik uyak dizisinin bitişik öğelerini adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal ana uyak harfinden önceki belirli ara konumu, komşu dal ise dizelerin bağlandığı ana uyak harfini gösterir.","focus_only":"Kurucu uzun ünlü ile ana uyak harfi arasındaki ara harftir.","gloss":"ara harf ile ana uyak harfi","neighbor_only":"Şiir boyunca birliği sağlayan ana uyak harfinin kendisidir.","neighbor_ref":"root_000615/B013","relation_type":"same_field","shared_zone":"İki dal da şiirin uyak örgüsündeki harf konumlarını adlandırır."}],"source_phrase_ar":"التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)","source_summary":"Kaynaklar teknik terimi, kurucu uzun ünlü ile ana uyak harfi arasındaki harf olarak ortak biçimde tanımlar.","sources":["SI","TA","MU"],"what_is_ar":"التوجيه في الشعر والقافية؛ الحرف أو الحركة بين ألف التأسيس والروي","what_is_not_ar":"ليس جهة السير ولا إرشاد الشيء"},"support_links":[]},{"boundary":"Anlam yalnız bu özel yetiştirme işlemidir; bir şeyi genel olarak yöneltme anlamına genişletilmez.","branch_kind":"bare","branch_ref":"root_001630/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"hıyar veya kavunun altını kazıp yana yatırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hıyar veya kavunun altını kazma ve sonra onu yana yatırma aşamalarını birlikte belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta anlatılan iki aşamalı bitki yetiştirme işlemi için geçerlidir.","boundary_detail":"Anlam yalnız bu özel yetiştirme işlemidir; bir şeyi genel olarak yöneltme anlamına genişletilmez.","branch_image_ar":"توجيه النبات","concept_gloss":"hıyar veya kavunun altını kazıp yana yatırma","contextual_glosses":[{"applicability":"Hıyar veya kavun yetiştirirken iki aşamalı işlemi eylem olarak anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazma ve ardından yana yatırma sırasını korur."},"facet_ids":["F001"],"text":"altını kazıp yana yatırmak","usage_role":"contextual"}],"definition":"Hıyarın veya kavunun altındaki toprağı kazıp ardından bitkiyi yana yatırma işlemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hıyar veya kavunun altını kazma ve sonra onu yana yatırma aşamalarını birlikte belirtir."}],"identity_rationale":"Tek kaynak ifadesi, hıyar veya kavunun altını kazdıktan sonra bitkiyi yana yatırma işlemini açık ve aşamalı biçimde verir. Dal çerçevesi hem nesneleri hem de işlem sırasını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"hıyar veya kavunun altını kazıp yana yatırma"}],"lexicalization_note":"Yalın biçim teknik bir bitki yetiştirme işlemini adlandırır; genel yön verme anlamı tanıma alınmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; genel yetiştirme ve bitkinin desteğe sarılması, özel insan müdahalesini en iyi sınırlayan iki alandır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal iki belirli bitkiye uygulanan sıralı bir bakım tekniğidir; komşu dal ekme ve yetiştirmeyi genel olarak kapsar.","focus_only":"Hıyar veya kavunun altını kazıp bitkiyi yana yatırma işlemi vardır.","gloss":"özel bakım ile genel yetiştirme","neighbor_only":"Tohum ekme, bitki yetiştirme, ekin ve ekili yer gibi geniş bir tarım alanı vardır.","neighbor_ref":"root_000630/B001","relation_type":"same_field","shared_zone":"İki dal da bitki yetiştirme ve tarımsal işlem alanında yer alır."},{"boundary_match":"field_only","distinction":"Odak dal yetiştiricinin yaptığı kazma ve yatırma işlemidir; komşu dal bitkinin kıvrılıp bir desteğe tutunma biçimidir.","focus_only":"Bitkinin altını kazdıktan sonra onu yana yatıran insan işlemi vardır.","gloss":"yana yatırma ile sarılma","neighbor_only":"Sarmaşık benzeri bitkinin kendiliğinden kıvrılıp çubuklara tutunması vardır.","neighbor_ref":"root_000350/B006","relation_type":"same_field","shared_zone":"İki dal da bitkinin büyürken aldığı yön ve konumla ilgilidir."}],"source_phrase_ar":"التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu özel yetiştirme işlemi tek kaynakta, önce altını kazma sonra bitkiyi yana yatırma sırasıyla aktarılır."}],"source_summary":"Anlam, hıyar veya kavunun altını kazma ve ardından bitkiyi yana yatırma sırasından oluşan özel yetiştirme işlemidir.","sources":["MQ"],"what_is_ar":"التوجيه في القثاءة أو البطيخة؛ حفر ما تحتها ثم إضجاعها","what_is_not_ar":"ليس توجيه الشيء إلى جهة عامة"},"support_links":[]},{"boundary":"Bu dalda vurmanın hedefi özellikle yüzdür; genel vurma veya sözlü yüzleşme anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001630/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yüzüne vurma ve yüzüne vurulmuş olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin yüzünü hedef alarak vurmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yüzüne vurulmuş kişiyi sonuç durumuyla niteler."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Vurmanın özellikle yüzü hedef aldığı eylem ve sonuç durumu için geçerlidir.","boundary_detail":"Bu dalda vurmanın hedefi özellikle yüzdür; genel vurma veya sözlü yüzleşme anlamı değildir.","branch_image_ar":"ضرب الوجه","concept_gloss":"yüzüne vurma ve yüzüne vurulmuş olma","contextual_glosses":[{"applicability":"Eylemin bir kişinin yüzünü hedef aldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vurma eylemi ile yüz hedefini korur."},"facet_ids":["F001"],"text":"yüzüne vurmak","usage_role":"general"},{"applicability":"Kişinin eylemden etkilenmiş sonuç durumu nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzüne vurulmuş olma sonucunu korur."},"facet_ids":["F002"],"text":"yüzüne vurulmuş","usage_role":"contextual"}],"definition":"Bir kişinin yüzüne vurmak ve bu eylemin sonucu olarak kişinin yüzüne vurulmuş olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin yüzünü hedef alarak vurmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Yüzüne vurulmuş kişiyi sonuç durumuyla niteler."}],"identity_rationale":"Tek kaynak ifadesi eylemi bir kişinin yüzüne vurmak, sonuç sıfatını da yüzüne vurulmuş olmak biçiminde açıkça tanımlar. Dal kimliği hedef bölge ile sonuç durumunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"birinin yüzüne vurmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yüzüne vurulmuş"}],"lexicalization_note":"Yüze vurma eylemi ile yüzüne vurulmuş kişiyi bildiren biçim ayrı tutulur ve genel vurma anlamına genişletilmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel tokatlama ile özel çene darbesi, yüz hedefinin hem geniş hem dar komşu sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüz hedefini zorunlu kılar; komşu dal vurma ve tokatlamayı farklı hedeflere ve başka çarpma eylemlerine genişletir.","focus_only":"Vurmanın hedefi özellikle yüzdür ve sonuç sıfatı da bu hedefi korur.","gloss":"yüze vurma","neighbor_only":"Tokatlama, genel dövüşme ve kuşun kanat çarpması gibi daha geniş eylemler vardır.","neighbor_ref":"root_000713/B004","relation_type":"near_synonym","shared_zone":"İki dal da birine vurma veya tokatlama eylemini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal hedefi genel olarak yüz diye belirler; komşu dal darbeyi veya itmeyi çene bölgesiyle sınırlar.","focus_only":"Yüzün herhangi bir bölümüne vurma ve vurulmuş yüz sonucu vardır.","gloss":"yüz ile çene hedefi","neighbor_only":"Çene veya çene bağlantısına vurma ya da itme özellikle belirlenmiştir.","neighbor_ref":"root_000515/B003","relation_type":"near_neighbor","shared_zone":"İki dal da başın ön bölümüne yönelen fiziksel darbeyi kapsar."}],"source_phrase_ar":"وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak hem yüzüne vurma eylemini hem de yüzüne vurulmuş kişiyi bildiren sonuç biçimini aktarır."}],"source_summary":"Anlam, yüzü hedef alan vurma eylemini ve bu eylemden etkilenen kişinin sonuç durumunu birlikte kapsar.","sources":["TA"],"what_is_ar":"ضرب وجه الشخص؛ موجوه لمن ضرب وجهه","what_is_not_ar":"ليس المواجهة بالكلام ولا الوجه بمعنى الجاه"},"support_links":[]},{"boundary":"Bu anlam, gelen kişiyi geri çevirme koşuluna bağlıdır; genel engelleme veya bir yöne sevk etme değildir.","branch_kind":"non_bare","branch_ref":"root_001630/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"yanına gelen kişiyi geri çevirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birinin yanına gelmiş kişiyi kabul etmeyerek geri göndermeyi belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin gelmiş olması ve muhatabın onu geri göndermesi koşullarını birlikte taşıyan özel kullanım için geçerlidir.","boundary_detail":"Bu anlam, gelen kişiyi geri çevirme koşuluna bağlıdır; genel engelleme veya bir yöne sevk etme değildir.","branch_image_ar":"الرد عن الوجه","concept_gloss":"yanına gelen kişiyi geri çevirmek","contextual_glosses":[{"applicability":"Birinin yanına kadar gelen kişinin kabul edilmeyip gönderilmesini doğal bağlamda anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelmiş kişiyi kabul etmeyip geri gönderme durumunu korur."},"facet_ids":["F001"],"text":"kapısından geri çevirmek","usage_role":"contextual"}],"definition":"Bir kişinin yanına gelen kimseyi kabul etmeyip geri çevirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birinin yanına gelmiş kişiyi kabul etmeyerek geri göndermeyi belirtir."}],"identity_rationale":"Tek kaynak ifadesi bir kişinin başka birinin yanına gelmesinden sonra geri çevrilmesini açıkça bildirir. Dal kimliği gelişin önce, geri çevirmenin sonra gerçekleştiği katılımcı ve aşama düzenini korur.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yanına gelen kişiyi geri çevirmek"}],"lexicalization_note":"Tanım yalnız birinin yanına gelen kişiyi geri çevirmeyi bildiren özel sözlüksel birimle sınırlıdır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; istekte bulunanı geri çevirme ve genel reddetme, geliş koşulunun sınırını en iyi belirleyen iki komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yanına gelmiş kişiyi geri gönderme koşuluyla sınırlıdır; komşu dal ise özellikle istekte bulunan kişiyi yüz çevirerek reddetmeyi anlatır.","focus_only":"Kişinin muhatabın yanına gelmiş olması yeterlidir; bir istekte bulunması şart değildir.","gloss":"geleni veya isteyeni geri çevirmek","neighbor_only":"Geri çevrilen kişinin bir istekte bulunması ve muhatabın ondan yüz çevirmesi özellikle belirtilir.","neighbor_ref":"root_000867/B009","relation_type":"near_synonym","shared_zone":"İki dal da karşıya gelen kişinin kabul edilmeyip geri çevrilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal gelen kişi ve geliş olayıyla sınırlıdır; komşu dal reddetmeyi sözlere, nesnelere ve yanlış ya da geçersiz içeriklere genişletir.","focus_only":"Geri çevrilen katılımcı, birinin yanına gelmiş kişidir.","gloss":"kişiyi geri çevirme ile reddetme","neighbor_only":"Nesne, söz, hata veya geçersiz para gibi insan dışı içerikleri kabul etmeme kapsamı vardır.","neighbor_ref":"root_000555/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şeyi kabul etmeyip geri gönderme sonucu bulunur."}],"source_phrase_ar":"أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, yanına gelen kişiyi kabul etmeyip geri çevirme anlamını aktarır."}],"source_summary":"Anlam, kişinin önce bir başkasının yanına gelmesi ve ardından o kişi tarafından geri çevrilmesi aşamalarından oluşur.","sources":["TA"],"what_is_ar":"إتيان الرجل ثم رده؛ أوجهه إذا رده","what_is_not_ar":"ليس التوجيه إلى جهة ولا المواجهة"},"support_links":[]},{"boundary":"Anlam yalnız iki yüzlü nesne ve içiyle dışı uyuşmayan kişi kalıplarına bağlıdır; genel yüz veya itibar anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001630/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","surface_ar":"وُجُوهٌ"}],"gloss":"iki yüzlü nesne; içiyle dışı uyuşmayan kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kumaşın iki ayrı yüzünün bulunmasını belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin içinden geçenden farklı bir yüzle karşısına çıkıp tutarsız davranmasını belirtir."}}],"root_ar":"و ج ه","root_id":"root_001630","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta verilen fiziksel kumaş ve davranışsal kişi kalıplarını birlikte özetler.","boundary_detail":"Anlam yalnız iki yüzlü nesne ve içiyle dışı uyuşmayan kişi kalıplarına bağlıdır; genel yüz veya itibar anlamı değildir.","branch_image_ar":"ذو وجهين","concept_gloss":"iki yüzlü nesne; içiyle dışı uyuşmayan kişi","contextual_glosses":[{"applicability":"Kumaşın fiziksel olarak iki ayrı yüzünün bulunması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kumaşın iki fiziksel yüzü bulunması anlamını korur."},"facet_ids":["F001"],"text":"iki yüzü de kullanılabilen kumaş","usage_role":"explanatory"},{"applicability":"Kişinin karşısındakine içinden geçenden farklı görünerek davranması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin içiyle dışı arasındaki davranışsal uyuşmazlığı korur."},"facet_ids":["F002"],"text":"iki yüzlü kimse","usage_role":"contextual"}],"definition":"Bir kumaşın iki yüzünün bulunmasıdır; kişiye uygulanan ayrı bir kalıpta ise karşısındakine kalbinde olandan farklı görünerek davranmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kumaşın iki ayrı yüzünün bulunmasını belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin içinden geçenden farklı bir yüzle karşısına çıkıp tutarsız davranmasını belirtir."}],"identity_rationale":"Tek kaynak ifadesi iki ayrı kalıbı açıkça verir: iki yüzü bulunan kumaş ve karşısındakine içindekinden farklı davranan kişi. Dal kimliği fiziksel iki yanlılık ile bundan kurulan davranışsal uzantıyı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"iki yüzü bulunan kumaş"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"içiyle dışı uyuşmayan iki yüzlü kimse"}],"lexicalization_note":"Fiziksel olarak iki yüzlü kumaş ile davranışta iki yüzlü kişi, kendi kalıpları içinde ayrı facetler olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel aldatıcı görünüş ile gizli karşıt bağlılık, kişi kalıbının davranışsal sınırlarını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli kişi kalıbının yanında fiziksel iki yüzlü kumaşı da kapsar; komşu dal ise aldatıcı davranışı yöntem ve bağlam bakımından daha geniş işler.","focus_only":"İki yüzü bulunan kumaş anlamı ve kişi için belirli iki yüzlü kalıbı vardır.","gloss":"iki yüzlülük ve aldatma","neighbor_only":"Hile, savaş aldatmacası ve gizlediğinden farklı huy veya görüş gösterme gibi daha geniş davranışlar vardır.","neighbor_ref":"root_000396/B001","relation_type":"near_neighbor","shared_zone":"Kişi kullanımında iki dal da içte olanı gizleyip dışarıya farklı görünmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal kişiler arası iki yüzlü davranışı ve fiziksel kumaş anlamını taşır; komşu dal dıştan bağlı görünüp gizlice karşıt durumda olmayı özel bir inanç ve bağlılık bağlamında sınırlar.","focus_only":"Fiziksel iki yüzlü kumaş ve kişiler arası tutarsız görünüş kalıbı vardır.","gloss":"iki yüzlülük ile gizli karşıtlık","neighbor_only":"İnanç veya toplumsal bağlılıkta dışarıdan kabul gösterip gizlice karşıt yönde çıkma özel koşulu vardır.","neighbor_ref":"root_001537/B004","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin dışarıda gösterdiğiyle içinde taşıdığının farklı olmasını içerir."}],"source_phrase_ar":"كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak hem iki yüzlü kumaş kalıbını hem de içiyle dışı uyuşmayan kişi kalıbını birlikte aktarır."}],"source_summary":"Anlam, kumaşın fiziksel olarak iki yüzlü olması ile kişinin içinden geçenden farklı görünmesi arasındaki biçimsel benzerliği iki ayrı kalıpta kurar.","sources":["JA"],"what_is_ar":"ما له وجهان حسيا؛ ومن يلقى بخلاف ما في قلبه","what_is_not_ar":"ليس الوجاهة ولا مقابلة الوجوه"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_d395846438edde65c362","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:indefinite-face-subject","source_type":"word_analysis","support_ids":["sup_38f0e140be7d473c2c49","sup_b4c6020130872edf66c2"],"title":"indefinite faces carry the predication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:1","qac_refs":["88:2:1:1"],"status":"accepted"}},{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_1fccde59a476e6562d26","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:opening-sound-cadence","source_type":"word_analysis","support_ids":["sup_2d8b3b692606b0e69c24","sup_38f0e140be7d473c2c49"],"title":"rounded opening and tanwīn cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:1","qac_refs":["88:2:1:1"],"status":"accepted"}},{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_32219936bda264fc9697","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:paired-face-day-taxonomy","source_type":"word_analysis","support_ids":["sup_38f0e140be7d473c2c49","sup_9c39e09e32b592c6a12c"],"title":"paired face frame in 88:2 and 88:8","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:1","qac_refs":["88:2:1:1"],"status":"accepted"}},{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_8e80b22bdcaa71fb199e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:visible-identity-face-field","source_type":"word_analysis","support_ids":["sup_38f0e140be7d473c2c49","sup_c85cca4eabfc7b3ce99d"],"title":"faces become public identity surfaces","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:1","qac_refs":["88:2:1:1"],"status":"accepted"}},{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_c0bd6660f4eeb235854f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:visual-scene-transition","source_type":"word_analysis","support_ids":["sup_045e67fa807b3927bac5","sup_38f0e140be7d473c2c49"],"title":"question report becomes visible scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:1","qac_refs":["88:2:1:1"],"status":"accepted"}},{"anchor_refs":["88:2:2"],"branch_refs":[],"candidate_id":"cand_4806c0acfd5f44ae6d2f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:2:2:decisive-disclosure-day","source_type":"word_analysis","support_ids":["sup_031cf7ea8b4f2e538561","sup_5027fd6bb45dc405147f"],"title":"day becomes disclosure occasion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:2","qac_refs":["88:2:2:1"],"status":"accepted"}},{"anchor_refs":["88:2:2"],"branch_refs":[],"candidate_id":"cand_215205da904b54db8706","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:2:2:deictic-event-time-compound","source_type":"word_analysis","support_ids":["sup_031cf7ea8b4f2e538561","sup_3f1ad530eb3f1b8520f1"],"title":"fused event-time points back to 88:1","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:2","qac_refs":["88:2:2:1"],"status":"accepted"}},{"anchor_refs":["88:2:2"],"branch_refs":[],"candidate_id":"cand_8dde749384d00e902fff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:2:2:face-day-scene-frame","source_type":"word_analysis","support_ids":["sup_031cf7ea8b4f2e538561","sup_db8d2e209fcae4be66ed"],"title":"same Day-frame divides outcomes in 88:2 and 88:8","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:2","qac_refs":["88:2:2:1"],"status":"accepted"}},{"anchor_refs":["88:2:2"],"branch_refs":[],"candidate_id":"cand_6fa39957c02b2e77e9dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:2:2:hamza-cadence-interruption","source_type":"word_analysis","support_ids":["sup_031cf7ea8b4f2e538561","sup_bb7dec901e662e433d76"],"title":"glottal catch marks the inserted time","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:2","qac_refs":["88:2:2:1"],"status":"accepted"}},{"anchor_refs":["88:2:2"],"branch_refs":[],"candidate_id":"cand_7feff11b278e9a64ec00","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:2:2:medial-pressure-point","source_type":"word_analysis","support_ids":["sup_031cf7ea8b4f2e538561","sup_b13a5a9de182d9f773dd"],"title":"middle word delays the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:2","qac_refs":["88:2:2:1"],"status":"accepted"}},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_487d82cbc55af0e00b5f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:closure-forward-explanation","source_type":"word_analysis","support_ids":["sup_83d6ae409b784c795fe8","sup_bbcfc95566c19364e35c"],"title":"final predicate becomes the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:3","qac_refs":["88:2:3:1"],"status":"accepted"}},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_55696000e26f2dfe30d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:durative-visible-abasement","source_type":"word_analysis","support_ids":["sup_83d6ae409b784c795fe8","sup_bac4af911103bd0a69ba"],"title":"participle makes abasement a worn state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:3","qac_refs":["88:2:3:1"],"status":"accepted"}},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_eb34ef02479198a2770c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:hushed-closing-sound","source_type":"word_analysis","support_ids":["sup_28ef8e9b8159e3c2f1b4","sup_83d6ae409b784c795fe8"],"title":"softened guttural closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:3","qac_refs":["88:2:3:1"],"status":"accepted"}},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_795e3ff259c68dfba0bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:predicate-agreement-class","source_type":"word_analysis","support_ids":["sup_415f7ff5d64050e4e679","sup_83d6ae409b784c795fe8"],"title":"predicate gathers faces into one class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:3","qac_refs":["88:2:3:1"],"status":"accepted"}},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_a4e787173335e7e30f39","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:root-echoes-on-organs","source_type":"word_analysis","support_ids":["sup_2de6c77ed50b1055715d","sup_83d6ae409b784c795fe8"],"title":"lowered eyes, voices, and hearts meet on the face","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:2:3","qac_refs":["88:2:3:1"],"status":"accepted"}},{"anchor_refs":["88:2:1"],"branch_refs":[],"candidate_id":"cand_96b8b025e63ff12ee1bb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001630"],"scope":"focus_ayah","source_local_id":"88:2:1:1","source_type":"qac_morpheme","support_ids":["sup_95b4bd38e334fb6ec328"],"title":"QAC root occurrence: و ج ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:2:3"],"branch_refs":[],"candidate_id":"cand_9953aa8be00e319779d1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000412"],"scope":"focus_ayah","source_local_id":"88:2:3:1","source_type":"qac_morpheme","support_ids":["sup_99cd2c1050b6af2fdbcf"],"title":"QAC root occurrence: خ ش ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:2","branch_refs":["root_000412/B001","root_001630/B001"],"candidate_id":"cand_aab903d68bd44ea162f0","commentary_obligation":"review","hft_ref":"hft_813d4f4f23b307d45150","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_public_bodily_lowering","source_type":"hft","support_ids":["sup_c2d5125f6d52cde6f3a8"],"title":"baseline_public_bodily_lowering","trust":"legacy_unbound"},{"anchor_refs":["88:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:2","branch_refs":["root_000412/B001","root_001630/B002","root_001630/B003"],"candidate_id":"cand_1c1584454305238ffa05","commentary_obligation":"review","hft_ref":"hft_a713fe6d39f725c1c3dd","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_defeated_orientation","source_type":"hft","support_ids":["sup_b7b23173f29798f89aa3"],"title":"baseline_defeated_orientation","trust":"legacy_unbound"},{"anchor_refs":["88:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:2","branch_refs":["root_000412/B002","root_000412/B004","root_001630/B006"],"candidate_id":"cand_2068f0e21657d8add22b","commentary_obligation":"review","hft_ref":"hft_14e095e59655342334f2","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_prominence_collapsed","source_type":"hft","support_ids":["sup_5989c8d9b09f6867699d"],"title":"baseline_prominence_collapsed","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","qac_morphemes":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","root_ar":"و ج ه","surface_ar":"وُجُوهٌ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"88:2:2:1","qac_word_ref":"88:2:2","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","root_ar":"خ ش ع","surface_ar":"خَٰشِعَةٌ"}],"word_analysis_qac_refs":[["88:2:1:1"],["88:2:2:1"],["88:2:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:2:1","88:2:2","88:2:3"]},"focus_surface_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","qac_morphemes":[{"lemma_ar":"وَجْه","morph_features":"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:1:1","qac_word_ref":"88:2:1","root_ar":"و ج ه","surface_ar":"وُجُوهٌ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"88:2:2:1","qac_word_ref":"88:2:2","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"خَاشِع","morph_features":"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:2:3:1","qac_word_ref":"88:2:3","root_ar":"خ ش ع","surface_ar":"خَٰشِعَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:2:1:1"],["88:2:2:1"],["88:2:3:1"]],"word_analysis_refs":["88:2:1","88:2:2","88:2:3"],"word_rows":[{"analysis_record_ref":"88:2:1","analytic_gloss_range_en":"indefinite broken plural faces as the nominative subject of the nominal clause; locally physical countenances carrying visible identity, not every branch of the root","analytic_root_gloss_range_en":"root range includes face and front, direction and orientation, confrontation, self or essence by face, directed intention, social standing, forepart, proper aspect, and other specialized branches; this ayah selects visible faces with public identity and orientation pressure","qac_refs":["88:2:1:1"],"root":{"arabic":"و ج ه","transliteration":"w-j-h"},"surface":{"arabic":"وُجُوهٌۭ","transliteration":"wujūhun"}},{"analysis_record_ref":"88:2:2","analytic_gloss_range_en":"compound temporal adverb meaning on that Day or at that event-time, with the deictic element pointing back to the evoked overwhelming event","analytic_root_gloss_range_en":"root range includes ordinary day, an open time span, event-day or severe occasion, marked divine days, and the yawm-idh construction; this ayah selects a deictic event-time rather than a neutral calendar date","qac_refs":["88:2:2:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"88:2:3","analytic_gloss_range_en":"feminine singular active participle used as the predicate of the face-subject; locally visible humbled abasement under judgment rather than voluntary devotional softness alone","analytic_root_gloss_range_en":"root range includes low humble submission, low desolate ground, sinking or darkened heavenly bodies, a depleted hump, and a reviewed sputum expression; this ayah selects the low humble submission branch as a visible state on faces","qac_refs":["88:2:3:1"],"root":{"arabic":"خ ش ع","transliteration":"kh-sh-ʿ"},"surface":{"arabic":"خَٰشِعَةٌ","transliteration":"khāshiʿatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:2"],"branch_refs":["root_000412/B001","root_001630/B001"],"candidate_id":"cand_aab903d68bd44ea162f0","evidence_scope":"focus_ayah","hft_ref":"hft_813d4f4f23b307d45150","item_id":"baseline_public_bodily_lowering","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_public_bodily_lowering","support_id":"sup_c2d5125f6d52cde6f3a8"},{"anchor_refs":["88:2"],"branch_refs":["root_000412/B001","root_001630/B002","root_001630/B003"],"candidate_id":"cand_1c1584454305238ffa05","evidence_scope":"focus_ayah","hft_ref":"hft_a713fe6d39f725c1c3dd","item_id":"baseline_defeated_orientation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_defeated_orientation","support_id":"sup_b7b23173f29798f89aa3"},{"anchor_refs":["88:2"],"branch_refs":["root_000412/B002","root_000412/B004","root_001630/B006"],"candidate_id":"cand_2068f0e21657d8add22b","evidence_scope":"focus_ayah","hft_ref":"hft_14e095e59655342334f2","item_id":"baseline_prominence_collapsed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_prominence_collapsed","support_id":"sup_5989c8d9b09f6867699d"}],"diagnostics":[],"lane_counts":{"global":18,"macro":4,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"88:2","lane":"micro","linguistic_source_ref":"88:2","surface_ref":"88:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:2","target_tokens":[["O",["88:2:2"]],["gün",["88:2:2"]],["yüzler",["88:2:1"]],["boyun",["88:2:3"]],["eğmiştir",["88:2:3"]]],"text":"O gün yüzler boyun eğmiştir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2","source_type":"word_analysis","support_id":"sup_031cf7ea8b4f2e538561","text":"{\"gloss_range\":\"compound temporal adverb meaning on that Day or at that event-time, with the deictic element pointing back to the evoked overwhelming event\",\"prose\":\"{{ar:يَوْمَئِذٍ}} ({{tr:yawmaʾidhin}}) stands in the middle of the clause as a fused time-marker: the day noun is bound to a deictic pointer, and the compensatory tanwīn keeps the overwhelming event named in 88:1 active without restating it. The word therefore frames the whole face-state predication, not merely a loose circumstance around the final predicate. Its day-field is narrowed by the local compound: it is a decisive event-window of disclosure and accountability, not a bare calendar date. Because it is inserted between subject and predicate, the Day becomes the pressure point through which exposed faces are read as humbled; even its hamza and tanwīn cadence make that insertion audible inside the three-word tableau. The same marker also holds the constant time axis for the opposite face outcome in 88:8, while face-plus-Day scenes such as 75:22, 75:24, and 80:38 show why this compact phrase functions as a recognizable judgment-scene frame.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"root range includes ordinary day, an open time span, event-day or severe occasion, marked divine days, and the yawm-idh construction; this ayah selects a deictic event-time rather than a neutral calendar date\",\"surface_display\":\"{{ar:يَوْمَئِذٍ}} ({{tr:yawmaʾidhin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1:visual-scene-transition","source_type":"word_analysis","support_id":"sup_045e67fa807b3927bac5","text":"{\"blocking_evidence\":null,\"headline\":\"question report becomes visible scene\",\"reader_payoff\":\"The reader notices the movement from the report about the overwhelming event in 88:1 into a direct image inside that event in 88:2.\",\"reason\":\"The local nominal clause begins without a conjunction after 88:1, and the first word supplies the visual payload of the event just named.\",\"representative_source_ids\":[\"QT-a1e5c4ef\",\"QB-d5687717\",\"QY-38d62377\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3:hushed-closing-sound","source_type":"word_analysis","support_id":"sup_28ef8e9b8159e3c2f1b4","text":"{\"blocking_evidence\":null,\"headline\":\"softened guttural closure\",\"reader_payoff\":\"The reader notices that the predicate's sound texture helps the ayah close in a subdued, lowered cadence.\",\"reason\":\"The phonetic rows are compatible with the surface form and are retained as secondary recitational texture.\",\"representative_source_ids\":[\"QP-ec2e5329\",\"QP-efc5aef1\",\"MP-faf7772d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1:opening-sound-cadence","source_type":"word_analysis","support_id":"sup_2d8b3b692606b0e69c24","text":"{\"blocking_evidence\":null,\"headline\":\"rounded opening and tanwīn cadence\",\"reader_payoff\":\"The reader notices that the word's rounded opening and indefinite nasal ending make the face-class sound broad before the clause tightens.\",\"reason\":\"The phonetic rows are not contradicted by grammar; they are retained as recitational texture secondary to the syntactic and lexical topics.\",\"representative_source_ids\":[\"QP-38276804\",\"QP-c21df036\",\"MP-b4d86ad2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3:root-echoes-on-organs","source_type":"word_analysis","support_id":"sup_2de6c77ed50b1055715d","text":"{\"blocking_evidence\":null,\"headline\":\"lowered eyes, voices, and hearts meet on the face\",\"reader_payoff\":\"The reader notices that the facial predicate gathers a wider lowered-body field, with eyes in 68:43 and 79:9 and voice and heart in 20:108 and 57:16 converging on visible identity.\",\"reason\":\"The CRITICAL intertext rows provide concrete references for lowered eyes, voices, and hearts; these parallels illuminate the local face predicate without governing its parse.\",\"representative_source_ids\":[\"QI-eae39714\",\"MI-3c261c90\",\"QS-c86cfa0a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1","source_type":"word_analysis","support_id":"sup_38f0e140be7d473c2c49","text":"{\"gloss_range\":\"indefinite broken plural faces as the nominative subject of the nominal clause; locally physical countenances carrying visible identity, not every branch of the root\",\"prose\":\"{{ar:وُجُوهٌۭ}} ({{tr:wujūhun}}) opens the scene with exposed countenances before the Day or the predicate is named. Its nominative, indefinite broken plural makes the faces the grammatical carrier of the whole nominal tableau, while leaving the group classified rather than totalized; this matters because the same face-frame later receives the opposite predicate in 88:8 and belongs to the wider radiant/grim face taxonomy visible in 75:22 and 75:24. The root's face/front sense is the selected local sense, but the wider field of orientation, public aspect, and rank makes these faces more than anatomy: visible identity is being turned into the surface of judgment. The word also takes the report of the overwhelming event from 88:1 and converts it into the first direct image inside that event, ready to carry the participial description that follows in 88:3. Sound and form help bind the tableau: the rounded opening and tanwīn cadence carry the open face-class into the following time marker.\",\"root_display\":\"{{ar:و ج ه}} ({{tr:w-j-h}})\",\"root_gloss_range\":\"root range includes face and front, direction and orientation, confrontation, self or essence by face, directed intention, social standing, forepart, proper aspect, and other specialized branches; this ayah selects visible faces with public identity and orientation pressure\",\"surface_display\":\"{{ar:وُجُوهٌۭ}} ({{tr:wujūhun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2:deictic-event-time-compound","source_type":"word_analysis","support_id":"sup_3f1ad530eb3f1b8520f1","text":"{\"blocking_evidence\":null,\"headline\":\"fused event-time points back to 88:1\",\"reader_payoff\":\"The reader notices that the time marker silently carries the event from 88:1 into 88:2 instead of naming a free-standing date.\",\"reason\":\"QAC identifies a yawm-plus-idh compound with compensatory tanwīn, and attachment evidence links the deictic element back to the event named in 88:1.\",\"representative_source_ids\":[\"QG-5d89e1fd\",\"QG-9a254239\",\"QF-a4047c7d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3:predicate-agreement-class","source_type":"word_analysis","support_id":"sup_415f7ff5d64050e4e679","text":"{\"blocking_evidence\":null,\"headline\":\"predicate gathers faces into one class\",\"reader_payoff\":\"The reader notices that humbledness is the main assertion about the faces, and the plural faces are treated as one visible class.\",\"reason\":\"QAC and attachment evidence identify a nominative feminine singular active participle used predicatively and agreeing with the non-rational broken plural subject.\",\"representative_source_ids\":[\"QG-43f0398e\",\"QG-9da51ea2\",\"MG-e92b8e55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2:decisive-disclosure-day","source_type":"word_analysis","support_id":"sup_5027fd6bb45dc405147f","text":"{\"blocking_evidence\":null,\"headline\":\"day becomes disclosure occasion\",\"reader_payoff\":\"The reader notices that time itself functions as an event-window where hidden status becomes visible, while the compound blocks a merely ordinary date reading.\",\"reason\":\"V4 allows ordinary day and broader period senses, but the yawm-idh construction and judgment context select event-day disclosure and accountability pressure.\",\"representative_source_ids\":[\"QS-b5fdbcf9\",\"QS-a37baf56\",\"MS-1070a171\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3","source_type":"word_analysis","support_id":"sup_83d6ae409b784c795fe8","text":"{\"gloss_range\":\"feminine singular active participle used as the predicate of the face-subject; locally visible humbled abasement under judgment rather than voluntary devotional softness alone\",\"prose\":\"{{ar:خَٰشِعَةٌ}} ({{tr:khāshiʿatun}}) is the clause's predicate, not an incidental circumstance: the final word states what those faces are. Its feminine singular agreement gathers the broken plural faces into one visible class, and that link holds across the inserted time marker. As an active participle, it presents abasement as a sustained displayed condition rather than a narrated instant or an explicitly caused action. The root's lowly submission field is locally narrowed by the face-Day scene: this is downcast public abasement under judgment, not simply chosen devotional reverence. Echoes where eyes are lowered in 68:43 and 79:9, and where voices and hearts are humbled in 20:108 and 57:16, help the face become the surface where posture, voice, and inner claim collapse together. Its long first syllable and softened-to-guttural close give the lowered state a hushed recitational weight. Because the predicate lands last, it closes the tableau as the verdict that 88:3-7 will unfold.\",\"root_display\":\"{{ar:خ ش ع}} ({{tr:kh-sh-ʿ}})\",\"root_gloss_range\":\"root range includes low humble submission, low desolate ground, sinking or darkened heavenly bodies, a depleted hump, and a reviewed sputum expression; this ayah selects the low humble submission branch as a visible state on faces\",\"surface_display\":\"{{ar:خَٰشِعَةٌ}} ({{tr:khāshiʿatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:2:1:1","source_type":"qac_morpheme","support_id":"sup_95b4bd38e334fb6ec328","text":"{\"lemma_ar\":\"وَجْه\",\"morph_features\":\"STEM|POS:N|LEM:wajoh|ROOT:wjh|MP|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:2:1:1\",\"qac_word_ref\":\"88:2:1\",\"root_ar\":\"و ج ه\",\"surface_ar\":\"وُجُوهٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:2:3:1","source_type":"qac_morpheme","support_id":"sup_99cd2c1050b6af2fdbcf","text":"{\"lemma_ar\":\"خَاشِع\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:xaA$iE|ROOT:x$E|FS|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:2:3:1\",\"qac_word_ref\":\"88:2:3\",\"root_ar\":\"خ ش ع\",\"surface_ar\":\"خَٰشِعَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1:paired-face-day-taxonomy","source_type":"word_analysis","support_id":"sup_9c39e09e32b592c6a12c","text":"{\"blocking_evidence\":null,\"headline\":\"paired face frame in 88:2 and 88:8\",\"reader_payoff\":\"The reader notices that 88:2 begins one half of a visible outcome taxonomy, answered by the matching face-frame in 88:8.\",\"reason\":\"The same-surah reprise in 88:8 and wider face-outcome scenes such as 75:22 and 75:24 support the local sorting function without replacing the immediate grammar.\",\"representative_source_ids\":[\"QI-cdabb136\",\"QE-7a027f69\",\"QY-74996cc6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2:medial-pressure-point","source_type":"word_analysis","support_id":"sup_b13a5a9de182d9f773dd","text":"{\"blocking_evidence\":null,\"headline\":\"middle word delays the verdict\",\"reader_payoff\":\"The reader notices the clause order: faces are shown first, then the Day intervenes, and only then does the humbled predicate land.\",\"reason\":\"Attachment evidence places the adverbial between the subject and predicate inside one nominal clause, so its medial position can be retained as a structural topic.\",\"representative_source_ids\":[\"QT-13d3b617\",\"QT-cc58b2fa\",\"MT-a60bfbb5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1:indefinite-face-subject","source_type":"word_analysis","support_id":"sup_b4c6020130872edf66c2","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite faces carry the predication\",\"reader_payoff\":\"The reader notices that the ayah begins with an open class of faces as the subject, not with named people or a totalized group.\",\"reason\":\"QAC and attachment evidence mark the word as an indefinite nominative broken plural subject of the nominal predication, with the feminine singular predicate agreeing across the time marker.\",\"representative_source_ids\":[\"QG-334185bc\",\"QG-7fa8a2d3\",\"QF-007f95ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3:durative-visible-abasement","source_type":"word_analysis","support_id":"sup_bac4af911103bd0a69ba","text":"{\"blocking_evidence\":null,\"headline\":\"participle makes abasement a worn state\",\"reader_payoff\":\"The reader notices that the faces wear a sustained visible condition of abasement, while local context narrows the root away from generic reverence or unrelated low-place branches.\",\"reason\":\"V4 supports low humble submission and other lowness branches, but the local facial predicate in a judgment-time scene selects visible humbled abasement rather than desolate ground, sinking stars, or devotional softness alone.\",\"representative_source_ids\":[\"QS-b45fa84c\",\"QF-618ec07e\",\"MF-342be1fd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2:hamza-cadence-interruption","source_type":"word_analysis","support_id":"sup_bb7dec901e662e433d76","text":"{\"blocking_evidence\":null,\"headline\":\"glottal catch marks the inserted time\",\"reader_payoff\":\"The reader notices that the word's hamza and tanwīn cadence make the time insertion audible inside the three-word tableau.\",\"reason\":\"The phonetic claim is consistent with the surface form and is kept as secondary recitational texture.\",\"representative_source_ids\":[\"QP-33f0383f\",\"QP-d9fde39d\",\"MP-a16fa17b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:3:closure-forward-explanation","source_type":"word_analysis","support_id":"sup_bbcfc95566c19364e35c","text":"{\"blocking_evidence\":null,\"headline\":\"final predicate becomes the verdict\",\"reader_payoff\":\"The reader notices that the humbled state lands as the ayah's closing verdict and becomes the condition unpacked by 88:3-7.\",\"reason\":\"The predicate is delayed until after the temporal insertion and closes the nominal tableau, while the following ayahs continue with participial explanation.\",\"representative_source_ids\":[\"QT-3bdd09bd\",\"QT-a09be05b\",\"QY-b0d3a070\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:1:visible-identity-face-field","source_type":"word_analysis","support_id":"sup_c85cca4eabfc7b3ce99d","text":"{\"blocking_evidence\":null,\"headline\":\"faces become public identity surfaces\",\"reader_payoff\":\"The reader notices that judgment is first made legible on the public front of the self, while local grammar still selects physical faces rather than every root branch.\",\"reason\":\"V4 supports face/front, orientation, aspect, and social-standing branches, but the local plural noun and predication select countenances as visible identity surfaces, not unrelated specialized branches.\",\"representative_source_ids\":[\"QS-f7bdf708\",\"QS-96c64867\",\"MS-42f18a10\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:2:2:face-day-scene-frame","source_type":"word_analysis","support_id":"sup_db8d2e209fcae4be66ed","text":"{\"blocking_evidence\":null,\"headline\":\"same Day-frame divides outcomes in 88:2 and 88:8\",\"reader_payoff\":\"The reader notices that one event-time holds both the humbled faces in 88:2 and the blissful faces in 88:8, making the predicates carry the division.\",\"reason\":\"The repeated marker in 88:8 and face-Day scenes such as 75:22, 75:24, and 80:38 support the formulaic judgment-frame payoff.\",\"representative_source_ids\":[\"QI-1f3cde94\",\"QE-a1543cc8\",\"ME-f5ff3b03\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000412/B001","root_001630/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001630","role":"The face as the outward front supplies the visible surface on which the condition appears.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000412","role":"Bodily lowering, downcast sight, quiet voice, and still limbs turn khushu into an observable posture.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"changed_reading":{"after":"Their public bodily fronts visibly sink and quiet on that day; the verse stages exposure, not an invisible feeling alone.","before":"People are inwardly humble on that day."},"confidence":"strong","focus_anchor":"The plural faces are directly predicated as khashi'a on that day.","mechanism":"The exposed fronts of persons carry a whole bodily lowering: head, gaze, voice, and limbs settle downward, making an otherwise inward condition publicly legible.","model_id":"baseline_public_bodily_lowering"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_public_bodily_lowering","source_type":"hft","support_id":"sup_c2d5125f6d52cde6f3a8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000412/B001","root_001630/B002","root_001630/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001630","role":"Direction and destination convert each face into an oriented front.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001630","role":"Face-to-face confrontation supplies the encounter toward which those fronts are exposed.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000412","role":"Lowering and downcast gaze bend the oriented front away from an upright confrontation.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"changed_reading":{"after":"The fronts that should meet what approaches are directionally defeated or redirected downward.","before":"The faces wear an expression of humility."},"confidence":"medium","focus_anchor":"Wujuh can mark oriented fronts and confrontation, while khashi'a supplies their downward disposition.","mechanism":"A face is not only an expression-bearing surface but a vector aimed toward a destination or encounter. Predicating khushu of these fronts makes their orientation appear checked, lowered, or unable to hold itself in confrontation.","model_id":"baseline_defeated_orientation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_defeated_orientation","source_type":"hft","support_id":"sup_b7b23173f29798f89aa3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000412/B002","root_000412/B004","root_001630/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001630","role":"Eminence and leading people allow the faces to be socially prominent persons, not only anatomical faces.","root":"و ج ه","source_ref":"88:2","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000412","role":"A hump depleted until its prominence droops supplies a material model for lost rank.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000412","role":"Low, dormant ground extends the collapse from bodily profile into topography.","root":"خ ش ع","source_ref":"88:2","source_word_indices":["3"]}],"changed_reading":{"after":"The once-prominent public figures have lost the very contour by which they stood above others.","before":"An anonymous multitude looks bowed."},"confidence":"exploratory","focus_anchor":"The plural wujuh can denote eminent representatives, and khushu can describe either low dormant ground or a hump whose high profile has wasted away.","mechanism":"Social height is rendered as physical profile. Those who functioned as the prominent faces of a group are shown with their projection gone, reduced toward a low, inert contour.","model_id":"baseline_prominence_collapsed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_prominence_collapsed","source_type":"hft","support_id":"sup_5989c8d9b09f6867699d","trust":"legacy_unbound"}]}
</lane_packet_json>
