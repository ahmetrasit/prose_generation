# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:1",
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
{"branch_registry":[{"boundary":"Anlam, sabah aydınlığını, ahlaki sapmayı ve eli açıklığı değil; fiziksel açılma ile dışarı akışı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B001","candidate_links":[{"candidate_id":"cand_540b0af0ae55b647efca","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"genişçe yarılma ve içinden suyun akıp çıkması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey genişçe yarılarak içinde bir açıklık oluşturulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özellikle su, açılan yerden dışarı çıkıp akmaya başlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Suyun açılıp çıktığı ağızlar ve vadi boşaltımları sonuç ya da yer bildiren kullanımlardır."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel açılma, suyun dışarı akması ve bu akışın çıkış yerleri birlikte kastedildiğinde en kapsamlı karşılıktır.","boundary_detail":"Anlam, sabah aydınlığını, ahlaki sapmayı ve eli açıklığı değil; fiziksel açılma ile dışarı akışı kapsar.","branch_image_ar":"انشقاق واسع وانبعاث","concept_gloss":"genişçe yarılma ve içinden suyun akıp çıkması","contextual_glosses":[{"applicability":"Bir su kaynağının ya da birikmiş suyun açılan yerden güçlü biçimde çıkışını anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yarma eylemini ve çıkış yeri ya da güzergah bildiren kullanımları dışarıda bırakır.","preserves":"Açılma sonucunda suyun dışarı çıkıp akmasını açıkça korur."},"facet_ids":["F002"],"text":"su yarılan yerden fışkırıp aktı","usage_role":"contextual"}],"definition":"Bir şeyi genişçe yararak açmak ya da böyle bir açıklıktan özellikle suyun akıp çıkmasıdır. Suyun çıktığı ağız, alçak alan ve akış yolu bu sürecin yer bildiren özelleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey genişçe yarılarak içinde bir açıklık oluşturulur."},{"facet_id":"F002","role":"core","statement":"Özellikle su, açılan yerden dışarı çıkıp akmaya başlar."},{"facet_id":"F003","role":"specialization","statement":"Suyun açılıp çıktığı ağızlar ve vadi boşaltımları sonuç ya da yer bildiren kullanımlardır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin genişçe yarılmasını ve özellikle suyun açılan yerden akıp çıkmasını aynı çekirdekte birleştirir. Suyun çıktığı ağızlar ve vadi boşaltım yerleri bu açılma ve akışın yer bildiren özelleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"suyu yarıp akıtma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"su açılıp akmaya başladı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"suyu yarıp dışarı akıttı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çokça açılıp fışkırdı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"suyun açılıp çıktığı yer"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suyun çıktığı ağız"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"suların ve vadilerin açılıp çıktığı alçak alan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"vadinin su boşaltım ağızları"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kum içindeki yol"}],"lexicalization_note":"Tanım hem genişçe yarılma çekirdeğini hem de suyla, çıkış yeriyle veya güzergahla sınırlı kullanımları ayrı katmanlar halinde korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma genel açılma, yerden su çıkışı ve doğal su yolu sınırlarını en yararlı biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yarma, akıtma, kendiliğinden akış ve çıkış yerlerini daha geniş biçimde kapsarken komşu dal suyun özellikle yerden pınar olarak çıkışını adlandırır.","focus_only":"Odak dal, geniş yarma eylemini ve suyun çıktığı ağızlarla akış yollarını da kapsar.","gloss":"yerden pınarların açılıp çıkması","neighbor_only":"Komşu dal, yeryüzünün pınarlar halinde açılıp su vermesine özgüdür.","neighbor_ref":"root_001150/B005","relation_type":"near_synonym","shared_zone":"İki dalda da yerin açılması ve suyun bu açıklıktan dışarı çıkması bulunur."},{"boundary_match":"partial","distinction":"Komşu dal genel çatlama ve açılmayı öne çıkarır; odak dal ise geniş yarılmayı suyun çıkışı, akışı ve akış yerleriyle bütünleştirir.","focus_only":"Odak dalda geniş yarılmadan sonra özellikle suyun akıp çıkması kurucu bir sonuçtur.","gloss":"bir şeyin çatlayıp açılması","neighbor_only":"Komşu dal deri, yer, dağ, diş ve sabah gibi çok farklı şeylerin çatlayıp açılmasını kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal fiziksel bütünlüğün bozulup bir açıklık oluşmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal bir yarılma ve dışarı çıkma sürecinden hareket eder; komşu dal ise arazi üzerindeki geçit ya da ayırıcı hattı başlı başına adlandırır.","focus_only":"Odak dalın çekirdeği açıklığın oluşması ve suyun oradan çıkıp akmasıdır.","gloss":"dağ ya da kum arasındaki su geçidi","neighbor_only":"Komşu dal dağlar veya kum arasındaki mevcut geçidi ve suyun izlediği arazi çizgisini adlandırır.","neighbor_ref":"root_001159/B006","relation_type":"same_field","shared_zone":"İki dal suyun geçtiği arazi açıklıkları ve doğal akış yolları alanında buluşur."}],"source_phrase_ar":"التفتح في الشيء (maqayis)؛ انفجر الماء انفجارا تفتح (maqayis)؛ الفجر تفجيرك الماء (ayn;tahdhib)؛ وانفجر الماء وغيره انفجارا إذا انبعث سائلا (jamhara)؛ فجرت الماء فانفجر أي بجسته فانبجس (sihah)؛ شق الشيء شقا واسعا (mufradat)؛ المفجر الموضع الذي ينفجر منه الماء (ayn;tahdhib)؛ الفجرة موضع تفتح الماء (maqayis;sihah)؛ مفاجر الوادي مرافضه (maqayis;sihah)","source_summary":"Kaynaklar genişçe yarılma ile suyun açılıp akmasını ortak çekirdek olarak verir; su çıkışları ve vadi boşaltım yerleri de bu çekirdeğin yer uzantılarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه شق الشيء شقا واسعا وتفجير الماء وانفجاره وتفجره ومواضع انفتاح الماء ومجاريه","what_is_not_ar":"ليس ضوء الصبح ولا الفجور ولا الجود"},"support_links":["sup_cd9f725fc7cb7a8c7509"]},{"boundary":"Bu dal fiziksel su çıkışından değil, gecenin sonunda sabah ışığının ortaya çıkmasından söz eder.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B002","candidate_links":[{"candidate_id":"cand_d11c71d0cae823a45de1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"sabah aydınlığının gece karanlığını yararak belirmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabah aydınlığı, gecenin sonundaki karanlığın içinden belirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu aydınlığın birbirinden ayrılan iki tan görünümü bulunur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ışık ve zaman çekirdeği, ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan ayrımında korunur."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tan vaktini yalnız bir saat aralığı olarak değil, ışığın geceden açılıp görünmesi olarak anlatan en kapsamlı karşılıktır.","boundary_detail":"Bu dal fiziksel su çıkışından değil, gecenin sonunda sabah ışığının ortaya çıkmasından söz eder.","branch_image_ar":"انبلاج الصبح من الليل","concept_gloss":"sabah aydınlığının gece karanlığını yararak belirmesi","contextual_glosses":[{"applicability":"Gecenin sona erip sabah aydınlığının görünmeye başladığı doğal bağlamlarda kısa ve akıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karanlığın yarılması imgesini, iki tan görünümünü ve vakte girme kullanımını açıkça söylemez.","preserves":"Sabah ışığının gecenin ardından görünmeye başlamasını doğal biçimde korur."},"facet_ids":["F001"],"text":"tan söktü","usage_role":"general"}],"definition":"Gecenin sonunda karanlığın açılmasıyla sabah aydınlığının belirmesidir. Ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan, bu belirişin ayırt edilen iki görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabah aydınlığı, gecenin sonundaki karanlığın içinden belirir."},{"facet_id":"F002","role":"specialization","statement":"Bu aydınlığın birbirinden ayrılan iki tan görünümü bulunur."},{"facet_id":"F003","role":"associated_use","statement":"Aynı ışık ve zaman çekirdeği, ufukta yayılan gerçek tan ile dikey görünüp dağılan yalancı tan ayrımında korunur."}],"identity_rationale":"Kaynak ifadesi, gecenin sonundaki karanlığın açılmasıyla sabah aydınlığının belirmesini doğrudan anlatır. İki ayrı tan görünümü bu zaman ve ışık çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tan aydınlığı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ufka yayılan gerçek tan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"dikey görünüp dağılan yalancı tan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"tan vaktine girdik"}],"lexicalization_note":"Tanım sabah aydınlığı çekirdeğini korur; iki tan türünü bu çekirdek içinde, başka kullanımları ise kendi sözlüksel birimleriyle sınırlı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar sabahın açılmasıyla güçlü örtüşmeyi ve yalnız zaman bildiren komşu anlamdan farkı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Doğal sabah bağlamında anlamlar büyük ölçüde örtüşür; odak dal tanın iki görünümünü ayırırken komşu dal açıklık imgesini gerçeğin belirginleşmesine kadar genişletir.","focus_only":"Odak dal sabah aydınlığının iki ayrı tan görünümünü de kapsar.","gloss":"sabahın açılması ve belirginleşmesi","neighbor_only":"Komşu dal sabahın açılmasını, karışık bir konudan sonra gerçeğin belirginleşmesine de aktarır.","neighbor_ref":"root_001176/B002","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği sabah ışığının gecenin karanlığından açılarak görünmesidir."},{"boundary_match":"partial","distinction":"Komşu dal görünürlük ve aydınlanma durumunu öne çıkarır; odak dal ise bu belirişi gecenin sonundaki tan vakti ve tan türleriyle sınırlar.","focus_only":"Odak dal gecenin sonundaki vakti ve birbirinden ayrılan iki tan görünümünü içerir.","gloss":"sabahın karanlıkta belirip aydınlanması","neighbor_only":"Komşu dalın odağı sabahın karanlık içinde görünür, aydınlık ve seçilir hale gelmesidir.","neighbor_ref":"root_001161/B002","relation_type":"near_synonym","shared_zone":"Her iki dal sabah ışığının gece karanlığı içinde görünmeye başlamasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal kurucu olarak bir ışık belirişidir; komşu dal ise aynı döneme yakın bir gece vaktinin adıdır ve aydınlanma gerektirmez.","focus_only":"Odak dal sabah ışığının karanlığı açarak görünmesini bildirir.","gloss":"gecenin sabah öncesi son vakti","neighbor_only":"Komşu dal ışığın belirmesini değil, gecenin sabah öncesindeki son zaman bölümünü bildirir.","neighbor_ref":"root_000682/B004","relation_type":"same_field","shared_zone":"İki dal gecenin sonu ile sabahın başlangıcı arasındaki zaman alanında buluşur."}],"source_phrase_ar":"الفجر انفجار الظلمة عن الصبح (maqayis)؛ الفجر ضوء الصباح والفجر الصبح (ayn)؛ الفجر حمرة الشمس في سواد الليل وهما فجران (jamhara)؛ الفجر في آخر الليل كالشفق في أوله (sihah)؛ الفجر ضوء الصبح وقد انفجر الصبح (tahdhib)؛ قيل للصبح فجر لكونه فجر الليل (mufradat)","source_summary":"Kaynaklar sabah ışığının gecenin sonundaki karanlığı açarak görünmesini ortak anlam olarak verir; iki tan görünümü de bu çekirdeğe bağlıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الفجر بمعنى ضوء الصبح وآخر الليل والصبح الصادق والكاذب","what_is_not_ar":"ليس تفجير الماء ولا الفجور ولا الجود"},"support_links":["sup_c7e4a1fc4896d6bd969d"]},{"boundary":"Dal her türlü sürprizi değil, insanların veya belaların çokluk halinde birilerinin üzerine gelmesini anlatır.","branch_kind":"collocation","branch_ref":"root_001132/B003","candidate_links":[{"candidate_id":"cand_37be0e5fbdaf07719fce","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"kalabalığın ya da çok sayıda belanın ansızın üzerlerine gelmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk halinde bulunan bir küme, etkilenen topluluğun üzerine beklenmedik biçimde gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gelen küme kalabalık bir insan topluluğu ya da art arda gelen çok sayıda bela olabilir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirtilen üzerine gelme kuruluşunda hem insan kalabalığını hem de çok sayıdaki belayı kapsayan eksiksiz karşılıktır.","boundary_detail":"Dal her türlü sürprizi değil, insanların veya belaların çokluk halinde birilerinin üzerine gelmesini anlatır.","branch_image_ar":"اندفاع الكثير بغتة","concept_gloss":"kalabalığın ya da çok sayıda belanın ansızın üzerlerine gelmesi","contextual_glosses":[{"applicability":"Çok sayıda insanın bir topluluğa beklenmedik biçimde yöneldiği anlatılarda doğal bir cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı kuruluşun çok sayıda bela için kullanılabilmesini dışarıda bırakır.","preserves":"Kalabalığın birilerinin üzerine ansızın ve topluca gelişini korur."},"facet_ids":["F001","F002"],"text":"kalabalık ansızın üzerlerine üşüştü","usage_role":"contextual"}],"definition":"Çok sayıda insanın ya da çok sayıda belanın bir topluluğun üzerine ansızın gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk halinde bulunan bir küme, etkilenen topluluğun üzerine beklenmedik biçimde gelir."},{"facet_id":"F002","role":"specialization","statement":"Gelen küme kalabalık bir insan topluluğu ya da art arda gelen çok sayıda bela olabilir."}],"identity_rationale":"Kaynak ifadesi, çok sayıda insanın ya da belanın bir topluluğun üzerine ansızın gelmesini açıkça kurar. Miktar, beklenmedik geliş ve etkilenen topluluk birlikte korunması gereken anlam bileşenleridir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalabalık ansızın üzerlerine geldi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çok sayıda bela ansızın başlarına geldi"}],"lexicalization_note":"Tanım yalnız belirtilen üzerine gelme kuruluşuna bağlıdır; bu anlam tek başına genel bir gelme ya da patlama anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen üç ilişki genel sürpriz, ani varış ve bastırıcı toplu geliş arasındaki temel sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel sürpriz oluşu anlatır; odak dal ise sürprize ek olarak çokluğu ve insanların ya da belaların birilerinin üzerine yönelmesini gerektirir.","focus_only":"Odak dal çok sayıda insanı veya belayı ve bunların bir topluluğun üzerine gelişini şart koşar.","gloss":"beklenmedik anda karşısına çıkma","neighbor_only":"Komşu dal herhangi bir şeyin beklenmedik gelişini kapsar; çokluk ya da belirli bir etkilenen taraf gerektirmez.","neighbor_ref":"root_000135/B001","relation_type":"near_synonym","shared_zone":"İki dalda da önceden beklenmeyen, ansızın gerçekleşen bir karşılaşma veya geliş vardır."},{"boundary_match":"partial","distinction":"Komşu dalın öznesi ve sahnesi geniştir; odak dal ise çokluk halindeki insanların veya belaların bir topluluğun üzerine gelmesiyle sınırlıdır.","focus_only":"Odak dal, insan kalabalığına veya çok sayıdaki belaya ve bunlardan etkilenen topluluğa bağlıdır.","gloss":"bir şeyin ansızın ortaya çıkıp gelmesi","neighbor_only":"Komşu dal tek bir kişinin, uzaktan gelen selin ya da bir gök cisminin ansızın görünmesini de kapsar.","neighbor_ref":"root_000466/B004","relation_type":"near_synonym","shared_zone":"Her iki dal beklenmedik bir ortaya çıkış veya varış hareketi taşır."},{"boundary_match":"partial","distinction":"Odak dal beklenmedik varış anına odaklanır; komşu dal ise gelen şeyin topluluğu kaplaması, yayılması ve baskın etkisini öne çıkarır.","focus_only":"Odak dalda ansızın geliş ve çok sayıda insan ya da bela bulunması kurucu koşuldur.","gloss":"kalabalığın ya da ağır bir olayın bastırması","neighbor_only":"Komşu dal atların, insanların ya da ağır bir olayın bir topluluğu kaplayıp bastırmasını ve yayılmasını öne çıkarır.","neighbor_ref":"root_000496/B003","relation_type":"near_neighbor","shared_zone":"İki dal bir topluluğun dışarıdan gelen çokluk veya ağır bir olay karşısında baskı altında kalmasını anlatabilir."}],"source_phrase_ar":"انفجر عليهم القوم وانفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة (ayn)؛ انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغته (tahdhib)","source_summary":"Kaynaklar, kalabalık bir insan topluluğunun veya çok sayıda belanın birilerinin üzerine beklenmedik biçimde gelmesinde birleşir; çokluk ve ansızın geliş birlikte zorunludur.","sources":["AY","TA"],"what_is_ar":"يدخل فيه مجيء القوم أو الدواهي الكثيرة بغتة على قوم","what_is_not_ar":"ليس انفجار الماء حقيقة ولا الفجور"},"support_links":["sup_b770d0100d87afdf838c"]},{"boundary":"Dalın çekirdeği ahlaki ve inançsal sınırları çiğnemektir; fiziksel eğrilik yalnız ilgili söz öbeğinin ayrı sözlüksel karşılığında kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B004","candidate_links":[{"candidate_id":"cand_c1d148df135a86297d56","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"doğruluk sınırını çiğneyerek kötülüğe sapma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi doğruluk ve inanç sınırlarını çiğneyerek doğru yoldan sapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yalan söylemek, kötülüklere dalmak, başkaldırmak, inancı reddetmek ve cinsel sınırı çiğnemek bu sapmanın özel görünümleridir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalan ve başkaldırı gibi özel eylemlerin bağlı olduğu geniş ahlaki sapma çekirdeği kastedildiğinde kullanılır.","boundary_detail":"Dalın çekirdeği ahlaki ve inançsal sınırları çiğnemektir; fiziksel eğrilik yalnız ilgili söz öbeğinin ayrı sözlüksel karşılığında kalır.","branch_image_ar":"انحراف عن الحق وخرق الستر","concept_gloss":"doğruluk sınırını çiğneyerek kötülüğe sapma","contextual_glosses":[{"applicability":"Bir kişinin geniş ve belirgin ahlaki sapmasını doğal bir yüklemle anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalan, inancı reddetme, başkaldırı ve cinsel sınır çiğneme gibi özel görünümleri tek tek belirtmez.","preserves":"Doğruluktan ayrılma ve kötülüklere yönelme çekirdeğini korur."},"facet_ids":["F001"],"text":"doğru yoldan sapıp kötülüğe daldı","usage_role":"general"}],"definition":"Doğruluk ve inanç sınırlarını yarıp kötülüklere yönelmek, böylece doğru yoldan belirgin biçimde sapmaktır. Yalan, taşkın kötülük, başkaldırı, inancı reddetme ve cinsel sınır çiğneme bunun özel görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi doğruluk ve inanç sınırlarını çiğneyerek doğru yoldan sapar."},{"facet_id":"F002","role":"specialization","statement":"Yalan söylemek, kötülüklere dalmak, başkaldırmak, inancı reddetmek ve cinsel sınırı çiğnemek bu sapmanın özel görünümleridir."}],"identity_rationale":"Kaynak ifadesi, doğruluktan sapıp kötülüklere açılmayı; yalanı, başkaldırıyı, inancı reddetmeyi ve cinsel sınır çiğnemeyi bunun görünümleri olarak destekler. Geçici çerçevedeki fiziksel yana yatma ise dalın kurucu ahlaki anlamı değil, ayrı bir söz öbeğinde görülen sınırlı bir uzantıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"taşkın kötülük, başkaldırı ve yalan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"doğru yoldan sapıp kötülüklere daldı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yalan söyledi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yalan söyledi, cinsel sınırı çiğnedi ya da inancı reddetti"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"doğru yoldan sapmış kimse"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"terkin oturma yeri yana yatıktır"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kötülük, kuşku ve yalan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ey doğru yoldan sapmış kadın"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"sana yalan söyleyen, karşı gelen ya da sözünden çıkan kişi"}],"lexicalization_note":"Tanım ahlaki sapma çekirdeğini verir; yalan, başkaldırı ve benzeri kullanımlar ile fiziksel eğiklik bildiren söz öbeği birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler genel suç, yalan, hükümde eğrilik ve başkasını saptırma ile olan temel kapsam ve katılımcı farklarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal geniş ahlaki taşkınlığı ve belirli ağır görünümleri kapsar; komşu dal ise özellikle karar, yöneliş ve hükümdeki eğriliği öne çıkarır.","focus_only":"Odak dal kötülüklere dalmayı, yalanı, başkaldırıyı ve inancı reddetmeyi geniş bir sapma alanında toplar.","gloss":"hükümde ve amaçta doğruluktan eğilme","neighbor_only":"Komşu dal özellikle hüküm, niyet ve işte doğruluktan yana eğilmeyi veya haksızlığa yönelmeyi kapsar.","neighbor_ref":"root_000265/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak çekirdeği doğruluktan ayrılma ve yanlış yöne eğilmedir."},{"boundary_match":"partial","distinction":"Komşu dal işlenen yanlışı suç veya kusur olarak adlandırır; odak dal ise kişinin doğruluktan kopup kötülüğe yönelme durumunu ve bunun çeşitli görünümlerini öne çıkarır.","focus_only":"Odak dal yalanı, inançtan uzaklaşmayı ve kötülüklere açılmayı da kapsar.","gloss":"yanlış davranış ve suç işleme","neighbor_only":"Komşu dal yanlış fiili suç, saldırı veya sorumluluk doğuran edim yönüyle adlandırır.","neighbor_ref":"root_000239/B004","relation_type":"near_synonym","shared_zone":"İki dal da kişinin kınanan bir yanlış yapmasını ve doğru sınırı aşmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan yalan ve gerçek dışılığı adlandırır; odak dalda yalan daha geniş bir doğruluktan sapma ve kötülüğe açılma bütününün yalnız bir parçasıdır.","focus_only":"Odak dal yalanın yanı sıra başkaldırı, kötülük, inancı reddetme ve başka sınır çiğnemelerini kapsar.","gloss":"yalan ve gerçek dışı söz","neighbor_only":"Komşu dal yalan söz, yalancı tanıklık ve gerçek dışı sayılan şeylere özgüdür.","neighbor_ref":"root_000654/B002","relation_type":"near_neighbor","shared_zone":"Yalan söylemek odak daldaki geniş ahlaki sapmanın açıkça belirtilen bir görünümüdür."},{"boundary_match":"partial","distinction":"Odak dal sapan kişinin durumunu ve davranışını kurar; komşu dal ise katılımcı rolünü değiştirerek sapmaya yol açan kişi veya etkiyi kurucu hale getirir.","focus_only":"Odak dal kişinin kendisinin doğru yoldan sapmasını ve sınırları çiğnemesini anlatır.","gloss":"başkasını doğru yoldan uzaklaştırma","neighbor_only":"Komşu dal başka birini doğru yoldan uzaklaştıran, kandıran veya yanlış davranışı çekici gösteren etkene odaklanır.","neighbor_ref":"root_001128/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru yoldan ayrılma ve yanlış yöne dönme senaryosuna bağlıdır."}],"source_phrase_ar":"الانبعاث والتفتح في المعاصي فجورا (maqayis)؛ سمي الكذب فجورا (maqayis)؛ كل مائل عن الحق فاجر (maqayis)؛ الفجور الريبة والكذب (ayn;tahdhib)؛ انبعاثه في المعاصي (jamhara)؛ فجر فجورا أي فسق وفجر أي كذب وأصله الميل (sihah)؛ الفجور شق ستر الديانة (mufradat)؛ سمي الكاذب فاجرا لكون الكذب بعض الفجور (mufradat)؛ أفجر إذا كذب وأفجر إذا عصى بفرجه وأفجر إذا كفر (tahdhib)","source_summary":"Kaynaklar doğruluktan sapma ve inanç sınırını çiğneme çekirdeğinde birleşir; yalan, kötülüklere dalma, başkaldırı, inancı reddetme ve cinsel yanlış bu geniş sapmanın belirtilen görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الفجور والفسق والمعاصي والريبة والكذب والكفر والعصيان والميل عن الحق وما لحق به من ميل حسي","what_is_not_ar":"ليس الفجر الصباحي ولا تفجير الماء ولا الجود"},"support_links":["sup_55b164c21413fe63b462"]},{"boundary":"Bu dal fiziksel su akışını ya da ahlaki sapmayı değil, iyilik ve vermedeki geniş bolluğu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001132/B005","candidate_links":[{"candidate_id":"cand_5bc6865a43df854baca8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"taşarcasına bol iyilik ve eli açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyilik ve verme, taşarcasına geniş ve bol biçimde gerçekleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin yaptığı yardımın çokluğu ve çokça varlık getirmesi bu bolluğun özel görünümleridir."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geniş verme eğilimi ile iyiliğin bolluğunu aynı anda anlatmak için en kapsamlı doğal karşılıktır.","boundary_detail":"Bu dal fiziksel su akışını ya da ahlaki sapmayı değil, iyilik ve vermedeki geniş bolluğu anlatır.","branch_image_ar":"جود متفجر واسع","concept_gloss":"taşarcasına bol iyilik ve eli açıklık","contextual_glosses":[{"applicability":"Bir kişinin sürekli ve bol yardımını doğal bir kişi betimlemesi içinde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çokça varlık getirme kullanımını ve iyiliğin taşarak yayılması imgesini açıkça belirtmez.","preserves":"Eli açıklığı ve kişiden gelen iyiliğin bolluğunu doğal biçimde korur."},"facet_ids":["F001"],"text":"eli açık, yaptığı iyilik de boldur","usage_role":"general"}],"definition":"İyiliğin taşarcasına bol olması ve kişinin geniş bir eli açıklıkla vermesidir. Yapılan yardımın çokluğu ve kişinin çokça varlık getirmesi bu bolluğun belirtilen görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyilik ve verme, taşarcasına geniş ve bol biçimde gerçekleşir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin yaptığı yardımın çokluğu ve çokça varlık getirmesi bu bolluğun özel görünümleridir."}],"identity_rationale":"Kaynak ifadesi eli açıklığı, geniş ve taşarcasına bol iyiliği, yapılan yardımı ve çokça varlık getirmeyi aynı bolluk çekirdeği çevresinde toplar. Geçici dal çerçevesi bu olumlu taşma ve verme yönünü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bol iyilik ve eli açıklık"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iyiliği ve yardımı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iyiliği taşarcasına bol kimse"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"iyiliğin taşıp yayılması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"çokça varlık getirdi"}],"lexicalization_note":"Tanım eli açıklık çekirdeğini verir; kişinin iyiliğinin bolluğu ve çokça varlık getirmesi yalnız belirtilen yapılara bağlı özelleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel eli açıklık, karşılıksız verme, sırf çokluk ve esirgeme karşıtlığıyla olan sınırları kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal verme eyleminin nesnelerini daha açık ve genel biçimde kapsar; odak dal ise iyiliğin içeriden taşarcasına bol oluşu imgesini ve belirli bolluk kullanımlarını öne çıkarır.","focus_only":"Odak dal iyiliğin taşarcasına yayılmasını, yapılan yardımın çokluğunu ve çokça varlık getirmeyi içerir.","gloss":"eli açıklık ve çokça verme","neighbor_only":"Komşu dal para ya da bilgi vermeyi ve kişiyi veren kimse olarak nitelemeyi açıkça kapsar.","neighbor_ref":"root_000274/B001","relation_type":"near_synonym","shared_zone":"İki dal da eli açıklığı, yardım etmeyi ve çokça vermeyi olumlu bir özellik olarak anlatır."},{"boundary_match":"partial","distinction":"Odak dal taşma ve geniş iyilik imgesine dayanır; komşu dal ise vermenin serbest ve karşılıksız oluşunu, bazı kullanımlarda sözü de içine alacak biçimde öne çıkarır.","focus_only":"Odak dal yapılan iyiliğin ve yardımın taşarcasına bolluğunu, ayrıca çokça varlık getirmeyi kapsar.","gloss":"karşılıksız ve bol verme","neighbor_only":"Komşu dal karşılıksız ve kısıtsız genel vermeyi, hatta engellenmeden söylenen sözü de kapsar.","neighbor_ref":"root_000677/B003","relation_type":"near_synonym","shared_zone":"İki dalda da iyiliğin ve vermenin bol, açık ve kısıtlanmamış oluşu bulunur."},{"boundary_match":"opposed","distinction":"Odak dal aynı eksenin bolca verme ucunu, komşu dal ise vermeme ve esirgeme ucunu kurar; bu nedenle yönleri doğrudan karşıttır.","focus_only":"Odak dal iyiliği bolca verme, yardım etme ve eli açık olma yönündedir.","gloss":"vermeyi kesme ve iyiliği esirgeme","neighbor_only":"Komşu dal vermeyi durdurma, iyiliği esirgeme ve eli sıkı davranma yönündedir.","neighbor_ref":"root_001448/B001","relation_type":"antonym","shared_zone":"İki dal kişinin elindeki iyiliği veya varlığı başkasına verip vermemesi ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği taşarcasına iyilik ve eli açıklıktır; komşu dalın çekirdeği daha genel çokluk olup bol verme bunun yalnız bir uygulamasıdır.","focus_only":"Odak dal bolluğu özellikle iyilik, yardım ve eli açıklıkla sınırlar.","gloss":"çokluk ve bol verme","neighbor_only":"Komşu dal yükün veya herhangi bir şeyin çokluğunu da kapsar ve yalnız bol verme anlamına bağlı değildir.","neighbor_ref":"root_001624/B003","relation_type":"near_synonym","shared_zone":"Bol ve çokça verme bağlamında iki dal güçlü biçimde örtüşür."}],"source_phrase_ar":"الفجر وهو الكرم والتفجر بالخير (maqayis)؛ وما أكثر فجره أي معروفه (ayn)؛ رجل ذو فجر إذا كان يتفجر بالخير (jamhara)؛ الفجر الكرم والتفجر في الخير (sihah)؛ الفجر الجود الواسع والكرم (tahdhib)؛ أفجر الرجل إذا جاء بالفجر وهو المال الكثير (tahdhib)","source_summary":"Kaynaklar geniş eli açıklık, taşarcasına bol iyilik ve yapılan yardımın çokluğu üzerinde birleşir; çokça varlık getirme de bu bolluğun özel bir eylem görünümüdür.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الكرم والجود الواسع والمعروف والمال الكثير والتفجر بالخير","what_is_not_ar":"ليس الفجور ولا الفجر الصباحي ولا تفجير الماء"},"support_links":["sup_64f6e00e3b37403cdc66"]},{"boundary":"Dal, dokunulmazlığın çiğnendiği belirli savaş günlerinin yerleşik adlandırmasıyla sınırlıdır.","branch_kind":"non_bare","branch_ref":"root_001132/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","surface_ar":"فَجْرِ"}],"gloss":"dokunulmazlığın çiğnenmesiyle adlandırılan belirli savaş günleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli savaş olayları, birlikte anılan yerleşik bir tarihsel günler kümesini oluşturur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu savaşların ortak adı, dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesine dayanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yerleşik adlandırma, birbiriyle bağlantılı dört ayrı çatışma olayını kapsar."}}],"root_ar":"ف ج ر","root_id":"root_001132","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız bu yerleşik tarihsel savaş günleri kümesini, adlandırılma gerekçesiyle birlikte belirtmek için kullanılır.","boundary_detail":"Dal, dokunulmazlığın çiğnendiği belirli savaş günlerinin yerleşik adlandırmasıyla sınırlıdır.","branch_image_ar":"وقائع الفجار لانتهاك الحرمة","concept_gloss":"dokunulmazlığın çiğnenmesiyle adlandırılan belirli savaş günleri","contextual_glosses":[{"applicability":"Yerleşik savaş adı okura açıklanırken, olayların ayırt edici gerekçesini kısa biçimde vermek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bunların dört bağlantılı olaydan oluşan yerleşik ve sınırlı bir adlandırma olduğunu açıkça söylemez.","preserves":"Savaş günleri ile dokunulmazlığın çiğnenmesi arasındaki bağı korur."},"facet_ids":["F001","F002"],"text":"dokunulmazlığın çiğnendiği savaş günleri","usage_role":"explanatory"}],"definition":"Dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesi nedeniyle ortak bir adla anılan belirli savaş günleridir. Bunlar birbiriyle bağlantılı dört ayrı çatışma olayı olarak aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli savaş olayları, birlikte anılan yerleşik bir tarihsel günler kümesini oluşturur."},{"facet_id":"F002","role":"core","statement":"Bu savaşların ortak adı, dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesine dayanır."},{"facet_id":"F003","role":"specialization","statement":"Yerleşik adlandırma, birbiriyle bağlantılı dört ayrı çatışma olayını kapsar."}],"identity_rationale":"Kaynak ifadesi, belirli eski savaş olaylarını ve bunların dokunulmaz sayılan zaman ve sınırların çiğnenmesi nedeniyle ortak bir adla anılmasını açıkça destekler. Bu nedenle anlam ne her savaşa ne de her türlü sınır çiğnemeye genellenebilir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"dokunulmazlığın çiğnendiği belirli savaş günleri"}],"lexicalization_note":"Tanım yalnız belirli savaş günlerini bildiren yerleşik birime bağlıdır; yalın biçime genel savaş ya da kötülük anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen ilişkiler şiddetli savaş, yinelenen savaş, adlandırılmış başka bir savaş günü ve yanlış davranışla olan sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal yerleşik bir tarihsel olaylar kümesinin adıdır ve ayırt edici ölçütü dokunulmazlık ihlalidir; komşu dal ise savaşın şiddet derecesini niteler.","focus_only":"Odak dal dokunulmazlığın çiğnenmesiyle adlandırılan belirli ve sınırlı savaş olaylarını bildirir.","gloss":"çok şiddetli ve öldürücü savaş","neighbor_only":"Komşu dal, daha önceki bir çatışmaya bağlı olmaksızın çok şiddetli ve öldürücü herhangi bir savaşı anlatır.","neighbor_ref":"root_001037/B005","relation_type":"same_field","shared_zone":"İki dal savaş, çatışma ve yoğun şiddet alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dal dört belirli olayı ortak ad ve ihlal gerekçesiyle birleştirir; komşu dal ise herhangi bir savaşın ilk olmayıp yinelenmiş olmasını anlatır.","focus_only":"Odak dalın kimliği belirli olaylara ve dokunulmazlığın çiğnenmesine bağlıdır.","gloss":"daha önce de yapılmış yinelenen savaş","neighbor_only":"Komşu dal daha önce de savaşılmış olmasını, yani çatışmanın yinelenmesini kurucu özellik yapar.","neighbor_ref":"root_001064/B003","relation_type":"same_field","shared_zone":"Her iki dal birden fazla çatışmayla ilişkilendirilebilen savaş anlatılarıdır."},{"boundary_match":"thematic_only","distinction":"Aralarında kurucu anlam ortaklığı yoktur; odak dal ihlal gerekçesiyle birleşen olaylar kümesini, komşu dal ise başka bir yer ve ona bağlı günü bildirir.","focus_only":"Odak dal dokunulmazlığın çiğnendiği dört bağlantılı savaş olayının yerleşik adıdır.","gloss":"belirli bir yer ve ona bağlı savaş günü","neighbor_only":"Komşu dal belirli bir yer adını ve o yere bağlı tek bir savaş gününü adlandırır.","neighbor_ref":"root_000040/B009","relation_type":"thematic","shared_zone":"İki dal eski toplulukların belirli ve adlandırılmış savaş günleri senaryosunda buluşur."},{"boundary_match":"thematic_only","distinction":"Komşu dal yanlış davranışın kendisini adlandırır; odak dal ise bu yanlışın gerçekleştiği belirli savaş günlerinin yerleşik adıdır.","focus_only":"Odak dal belirli savaş olaylarını ve bunların ortak tarihsel adını bildirir.","gloss":"yanlış davranış ve suçluluk","neighbor_only":"Komşu dal doğrudan yanlış davranış, suçluluk ve kişinin sakındığı kötülüğü bildirir.","neighbor_ref":"root_000365/B001","relation_type":"thematic","shared_zone":"Dokunulmazlığın çiğnenmesi, odak daldaki savaşların adlandırılma gerekçesi olarak yanlış davranış alanına bağlanır."}],"source_phrase_ar":"يوم الفجار يوم للعرب استحلت فيه الحرمة (maqayis)؛ انفجار من وقعات العرب بعكاظ (ayn)؛ أيام الفجار أربعة أفجرة (jamhara;sihah)؛ وإنما سمت قريش هذه الحرب فجارا لأنها كانت في الأشهر الحرم (sihah)؛ أيام الفجار أيام وقائع كانت بعكاظ واستحلوا الحرمات (tahdhib)؛ أيام الفجار وقائع اشتدت بين العرب (mufradat)","source_summary":"Kaynaklar, belirli savaş günlerinin dokunulmaz sayılan aylarda ve yerde sınırların çiğnenmesi nedeniyle adlandırıldığını ve dört bağlantılı olay olarak anıldığını birlikte bildirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم أيام الفجار ووقائعها بين العرب وتسميتها بما وقع فيها من استحلال الحرمات","what_is_not_ar":"ليس كل فجور ولا كل حرب"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_70b9f2c8ca5d507e4a18","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:1:1:connective-oath-sequence","source_type":"word_analysis","support_ids":["sup_519cd2bcfa99f6e0d9a7","sup_61a19027ed2a9c969d42"],"title":"oath force also launches a sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:1","qac_refs":["89:1:1:1"],"status":"accepted"}},{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_66c6adcae5640a80cd4f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:1:1:delayed-oath-answer","source_type":"word_analysis","support_ids":["sup_61a19027ed2a9c969d42","sup_84b4f03b9bfbf1d49fb3"],"title":"evidence accumulates before verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:1","qac_refs":["89:1:1:1"],"status":"accepted"}},{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_14cf6f6b357471ab0f7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:1:1:fused-proclitic-delivery","source_type":"word_analysis","support_ids":["sup_5ca02e54d04d958ca84e","sup_61a19027ed2a9c969d42"],"title":"particle and noun arrive as one compact beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:1","qac_refs":["89:1:1:1"],"status":"accepted"}},{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_3742ec2ccaba4a11af74","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:1:1:oath-governance","source_type":"word_analysis","support_ids":["sup_0f49748dda24e625a59b","sup_61a19027ed2a9c969d42"],"title":"particle makes dawn sworn evidence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:1","qac_refs":["89:1:1:1"],"status":"accepted"}},{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_2df84b4b00272bead060","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:1:1:opening-threshold","source_type":"word_analysis","support_ids":["sup_2e1168bc97c77eb4efb5","sup_61a19027ed2a9c969d42"],"title":"threshold force survives under oath grammar","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:1","qac_refs":["89:1:1:1"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_0cb0019e4db02e56039c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:clipped-sound","source_type":"word_analysis","support_ids":["sup_615a96fb614d16ed5ac0","sup_64bce48426603561eeae"],"title":"clipped sound matches sudden threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_2ec71d75343abdaac70e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:definite-recognized-threshold","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_f356f557507aab5662b7"],"title":"the article presents known daybreak","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_15c8461f0cb562be07ca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:disclosure-before-verdict","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_985619be52d2c80bc6fc"],"title":"dawn image anticipates later disclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_860ff884cb65e28657da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:genitive-oath-object","source_type":"word_analysis","support_ids":["sup_0e2c6a3667818a04e1e3","sup_64bce48426603561eeae"],"title":"dawn is the sworn-by object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_c9e692026d06352b0b97","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:moral-breach-shadow","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_68ad9e0ccd0dfe079570"],"title":"physical rupture can shadow moral breach","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_2065673df5db1c5bf5cf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:nominal-compression","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_a10bb765fbfe60540941"],"title":"a dynamic root is stabilized as a noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_753bcc19be49a139569a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:opening-temporal-sequence","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_76c90d406f0f72ad143a"],"title":"singular dawn opens plural time signs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_54eec7a7790452d3cefc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:rupture-release-pressure","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_ecc45297c6340290ac68"],"title":"dawn is felt as release through concealment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_cc45a14090ab0e5079f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:surface-binding","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_d120bf5c011416206166"],"title":"sound and script bind the noun to the oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_7f1ee5b1c932ddf2a0b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:variant-apparatus","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_7d34ed8920975b1a901b"],"title":"variants test texture without replacing the reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:2"],"branch_refs":[],"candidate_id":"cand_33214c88f5ce4883bbf8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:2:water-burst-reference","source_type":"word_analysis","support_ids":["sup_64bce48426603561eeae","sup_7aff033cfc1498add8b0"],"title":"water-burst recurrence sharpens release","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:1:2","qac_refs":["89:1:1:2","89:1:1:3"],"status":"accepted"}},{"anchor_refs":["89:1:1"],"branch_refs":[],"candidate_id":"cand_b5841231ca5c5f206dc4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001132"],"scope":"focus_ayah","source_local_id":"89:1:1:3","source_type":"qac_morpheme","support_ids":["sup_524bcafe8c267530b194"],"title":"QAC root occurrence: ف ج ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:1","branch_refs":["root_001132/B002"],"candidate_id":"cand_d11c71d0cae823a45de1","commentary_obligation":"review","hft_ref":"hft_6add3b93824826a70dd1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_threshold_discrimination","source_type":"hft","support_ids":["sup_c7e4a1fc4896d6bd969d"],"title":"base_threshold_discrimination","trust":"legacy_unbound"},{"anchor_refs":["89:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:1","branch_refs":["root_001132/B001"],"candidate_id":"cand_540b0af0ae55b647efca","commentary_obligation":"review","hft_ref":"hft_e7a76273cc6800687337","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_material_rupture","source_type":"hft","support_ids":["sup_cd9f725fc7cb7a8c7509"],"title":"base_material_rupture","trust":"legacy_unbound"},{"anchor_refs":["89:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:1","branch_refs":["root_001132/B003"],"candidate_id":"cand_37be0e5fbdaf07719fce","commentary_obligation":"review","hft_ref":"hft_1372dc209d7dc91523a8","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_sudden_collective_inrush","source_type":"hft","support_ids":["sup_b770d0100d87afdf838c"],"title":"base_sudden_collective_inrush","trust":"legacy_unbound"},{"anchor_refs":["89:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:1","branch_refs":["root_001132/B004"],"candidate_id":"cand_c1d148df135a86297d56","commentary_obligation":"review","hft_ref":"hft_73d1336ba5d7009e65c1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_ethical_breach","source_type":"hft","support_ids":["sup_55b164c21413fe63b462"],"title":"base_ethical_breach","trust":"legacy_unbound"},{"anchor_refs":["89:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:1","branch_refs":["root_001132/B005"],"candidate_id":"cand_5bc6865a43df854baca8","commentary_obligation":"review","hft_ref":"hft_92040f0a628e37b90562","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_overflowing_good","source_type":"hft","support_ids":["sup_64f6e00e3b37403cdc66"],"title":"base_overflowing_good","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلْفَجْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:1:1:1","qac_word_ref":"89:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:1:1:2","qac_word_ref":"89:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","root_ar":"ف ج ر","surface_ar":"فَجْرِ"}],"word_analysis_qac_refs":[["89:1:1:1"],["89:1:1:2","89:1:1:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:1:1","89:1:2"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلْفَجْرِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:1:1:1","qac_word_ref":"89:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:1:1:2","qac_word_ref":"89:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"فَجْر","morph_features":"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:1:1:3","qac_word_ref":"89:1:1","root_ar":"ف ج ر","surface_ar":"فَجْرِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:1:1:1"],["89:1:1:2","89:1:1:3"]],"word_analysis_refs":["89:1:1","89:1:2"],"word_rows":[{"analysis_record_ref":"89:1:1","analytic_gloss_range_en":"opening oath particle with connective force; locally it governs the following genitive dawn noun and launches a coordinated oath sequence rather than functioning as ordinary coordination alone","analytic_root_gloss_range_en":null,"qac_refs":["89:1:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:1:2","analytic_gloss_range_en":"definite singular dawn or daybreak as genitive sworn object; locally the recognizable first-light threshold functions as witness, with rupture and disclosure pressure from the root but without replacing the selected dawn sense","analytic_root_gloss_range_en":"broad root range including dawn breaking from night, physical splitting and outflow, sudden bursting-in, moral breach, overflowing generosity, and named battle-days; the local noun selects dawn while allowing rupture and disclosure pressure to remain audible","qac_refs":["89:1:1:2","89:1:1:3"],"root":{"arabic":"ف ج ر","transliteration":"f-j-r"},"surface":{"arabic":"ٱلْفَجْرِ","transliteration":"al-fajri"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["89:1"],"branch_refs":["root_001132/B002"],"candidate_id":"cand_d11c71d0cae823a45de1","evidence_scope":"focus_ayah","hft_ref":"hft_6add3b93824826a70dd1","item_id":"base_threshold_discrimination","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_threshold_discrimination","support_id":"sup_c7e4a1fc4896d6bd969d"},{"anchor_refs":["89:1"],"branch_refs":["root_001132/B001"],"candidate_id":"cand_540b0af0ae55b647efca","evidence_scope":"focus_ayah","hft_ref":"hft_e7a76273cc6800687337","item_id":"base_material_rupture","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_material_rupture","support_id":"sup_cd9f725fc7cb7a8c7509"},{"anchor_refs":["89:1"],"branch_refs":["root_001132/B003"],"candidate_id":"cand_37be0e5fbdaf07719fce","evidence_scope":"focus_ayah","hft_ref":"hft_1372dc209d7dc91523a8","item_id":"base_sudden_collective_inrush","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_sudden_collective_inrush","support_id":"sup_b770d0100d87afdf838c"},{"anchor_refs":["89:1"],"branch_refs":["root_001132/B004"],"candidate_id":"cand_c1d148df135a86297d56","evidence_scope":"focus_ayah","hft_ref":"hft_73d1336ba5d7009e65c1","item_id":"base_ethical_breach","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_ethical_breach","support_id":"sup_55b164c21413fe63b462"},{"anchor_refs":["89:1"],"branch_refs":["root_001132/B005"],"candidate_id":"cand_5bc6865a43df854baca8","evidence_scope":"focus_ayah","hft_ref":"hft_92040f0a628e37b90562","item_id":"base_overflowing_good","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_overflowing_good","support_id":"sup_64f6e00e3b37403cdc66"}],"diagnostics":[],"lane_counts":{"global":16,"macro":4,"micro":5},"packet_summary":{"ayah_count":30,"focus_ref":"89:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"89:1","lane":"micro","linguistic_source_ref":"89:1","surface_ref":"89:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:1","target_tokens":[["Tan",["89:1:1"]],["vaktine",["89:1:1"]],["andolsun",["89:1:1"]]],"text":"Tan vaktine andolsun!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:genitive-oath-object","source_type":"word_analysis","support_id":"sup_0e2c6a3667818a04e1e3","text":"{\"blocking_evidence\":null,\"headline\":\"dawn is the sworn-by object\",\"reader_payoff\":\"The reader notices that dawn is not merely when the scene occurs; grammar makes it the object of testimony.\",\"reason\":\"QAC and attachment evidence parse {{ar:ٱلْفَجْرِ}} ({{tr:al-fajri}}) as a genitive noun governed by the oath particle, with a compressed oath predicate and possible delayed answer.\",\"representative_source_ids\":[\"QG-01aa62b0\",\"QG-f4748a37\",\"MG-47d5405b\",\"QI-5cb11ee4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1:oath-governance","source_type":"word_analysis","support_id":"sup_0f49748dda24e625a59b","text":"{\"blocking_evidence\":null,\"headline\":\"particle makes dawn sworn evidence\",\"reader_payoff\":\"The reader notices that the first word changes dawn from a named time into sworn evidence before the surah states its claim.\",\"reason\":\"QAC and attachment evidence identify {{ar:وَ}} ({{tr:wa}}) as the oath particle governing {{ar:ٱلْفَجْرِ}} ({{tr:al-fajri}}), with a formulaically omitted oath predicate.\",\"representative_source_ids\":[\"QG-5618d112\",\"MG-1bc0b8b0\",\"QI-c366fb6f\",\"QT-c0652a55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1:opening-threshold","source_type":"word_analysis","support_id":"sup_2e1168bc97c77eb4efb5","text":"{\"blocking_evidence\":null,\"headline\":\"threshold force survives under oath grammar\",\"reader_payoff\":\"The reader notices that the very first word sets relation and testimony before any content noun or narrative action appears.\",\"reason\":\"The opening-threshold effect survives, but local attachment fixes the particle primarily as oath governance rather than a free circumstantial or resumptive frame.\",\"representative_source_ids\":[\"QG-2304cca4\",\"QT-b7cd8c84\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1:connective-oath-sequence","source_type":"word_analysis","support_id":"sup_519cd2bcfa99f6e0d9a7","text":"{\"blocking_evidence\":null,\"headline\":\"oath force also launches a sequence\",\"reader_payoff\":\"The reader notices that the opening particle both solemnizes the first sign and leans forward into the repeated oath chain that continues at 89:2.\",\"reason\":\"The local grammar gives oath force, while the CRITICAL rows and the following repeated particle support the same opener as the first member of a coordinated oath inventory (89:2).\",\"representative_source_ids\":[\"QG-3896c2e1\",\"QS-57f08430\",\"MT-6b44d4d1\",\"QB-8bc78794\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:1:1:3","source_type":"qac_morpheme","support_id":"sup_524bcafe8c267530b194","text":"{\"lemma_ar\":\"فَجْر\",\"morph_features\":\"STEM|POS:N|LEM:fajor|ROOT:fjr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:1:1:3\",\"qac_word_ref\":\"89:1:1\",\"root_ar\":\"ف ج ر\",\"surface_ar\":\"فَجْرِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1:fused-proclitic-delivery","source_type":"word_analysis","support_id":"sup_5ca02e54d04d958ca84e","text":"{\"blocking_evidence\":null,\"headline\":\"particle and noun arrive as one compact beat\",\"reader_payoff\":\"The reader notices that the oath relation is not mediated by an overt verb; the particle is attached directly into the sound and script of its governed noun.\",\"reason\":\"The bundle segmentation separates the morpheme analytically, but the surface phrase {{ar:وَٱلْفَجْرِ}} ({{tr:wa-l-fajri}}) still delivers the particle directly into the article-bearing noun.\",\"representative_source_ids\":[\"QF-70e89aff\",\"QF-8768ed9b\",\"QF-bf10f956\",\"QP-78f90ecf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:clipped-sound","source_type":"word_analysis","support_id":"sup_615a96fb614d16ed5ac0","text":"{\"blocking_evidence\":null,\"headline\":\"clipped sound matches sudden threshold\",\"reader_payoff\":\"The reader notices that the short final sound gives the first image an abrupt, crack-like closure rather than a slow descriptive unfolding.\",\"reason\":\"The compact consonant shape of the displayed noun supports the CRITICAL sound observation without creating a separate lexical sense.\",\"representative_source_ids\":[\"QP-f637665c\",\"MP-12a48352\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1","source_type":"word_analysis","support_id":"sup_61a19027ed2a9c969d42","text":"{\"gloss_range\":\"opening oath particle with connective force; locally it governs the following genitive dawn noun and launches a coordinated oath sequence rather than functioning as ordinary coordination alone\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not let the surah begin with a detached scene-word. As an oath particle, it governs {{ar:ٱلْفَجْرِ}} ({{tr:al-fajri}}) as the sworn-by object, so dawn is made evidentiary before any explicit claim is spoken. The same one-letter opening keeps connective force: the oath is not exhausted in this ayah, because the repeated opening particle in the next item (89:2) confirms a coordinated oath sequence. Since the oath answer can remain suppressed until the possible verdict at 89:14, the listener first receives accumulated witnesses rather than an immediate assertion. In the surface phrase {{ar:وَٱلْفَجْرِ}} ({{tr:wa-l-fajri}}), the particle is visibly and audibly fused to the noun it governs, so the grammar of testimony is compressed into the surah's first beat; because the prefixed particle remains analytically separable, that same compact beat can carry oath, connective, and opening-threshold force at once.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2","source_type":"word_analysis","support_id":"sup_64bce48426603561eeae","text":"{\"gloss_range\":\"definite singular dawn or daybreak as genitive sworn object; locally the recognizable first-light threshold functions as witness, with rupture and disclosure pressure from the root but without replacing the selected dawn sense\",\"prose\":\"{{ar:ٱلْفَجْرِ}} ({{tr:al-fajri}}) is not a free time-setting at the start of the surah; its genitive case places it under {{ar:وَ}} ({{tr:wa}}) as the sworn-by object. The definite singular makes dawn a recognizable threshold, not an anonymous morning, and the variant apparatus sharpens that by contrast: an indefinitizing ending would weaken public recognizability, while an internal-vowel shift would change texture without undoing genitive oath governance. The later plural nights in 89:2 expand from this first concentrated sign. Its root, {{ar:ف ج ر}} ({{tr:f-j-r}}), keeps the image of breaking open inside the selected dawn sense: light appears as release through concealment, while the local noun remains dawn rather than a verbal bursting event. That rupture field can also move elsewhere into water bursting from rock (2:60) and moral breach (91:8), so the opening begins with physical disclosure before later judgment language takes over. The compact noun also compresses action: instead of narrating something being burst open, naming an agent, or casting dawn as a patient, the ayah presents the resulting threshold as witness. The clipped sound and visible article bind this known dawn tightly into the oath beat, and the delayed answer at 89:14 lets its disclosure image stand before the verdict becomes explicit.\",\"root_display\":\"{{ar:ف ج ر}} ({{tr:f-j-r}})\",\"root_gloss_range\":\"broad root range including dawn breaking from night, physical splitting and outflow, sudden bursting-in, moral breach, overflowing generosity, and named battle-days; the local noun selects dawn while allowing rupture and disclosure pressure to remain audible\",\"surface_display\":\"{{ar:ٱلْفَجْرِ}} ({{tr:al-fajri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:moral-breach-shadow","source_type":"word_analysis","support_id":"sup_68ad9e0ccd0dfe079570","text":"{\"blocking_evidence\":null,\"headline\":\"physical rupture can shadow moral breach\",\"reader_payoff\":\"The reader notices that the root field can move from physical breaking to moral breach (91:8), so the dawn's break prepares a moral register without making moral breach the local sense.\",\"reason\":\"V4 keeps moral breach as a separate accepted branch of {{ar:ف ج ر}} ({{tr:f-j-r}}), while the local word remains the dawn noun rather than an agent or abstract moral form; the concrete inter-ayah row points to moral breach at 91:8.\",\"representative_source_ids\":[\"QS-b98ee660\",\"QI-030810ee\",\"QI-0bed49d5\",\"MI-394dcfc5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:opening-temporal-sequence","source_type":"word_analysis","support_id":"sup_76c90d406f0f72ad143a","text":"{\"blocking_evidence\":null,\"headline\":\"singular dawn opens plural time signs\",\"reader_payoff\":\"The reader notices that one concentrated dawn threshold opens into the counted nights of the next oath item (89:2).\",\"reason\":\"The dawn noun is the first lexical image of the surah, and the next ayah expands the oath sequence into plural counted nights (89:2).\",\"representative_source_ids\":[\"QF-4704abf6\",\"QT-fbbe3e4b\",\"QE-0cae1467\",\"QB-2b6951ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:water-burst-reference","source_type":"word_analysis","support_id":"sup_7aff033cfc1498add8b0","text":"{\"blocking_evidence\":null,\"headline\":\"water-burst recurrence sharpens release\",\"reader_payoff\":\"The reader notices that the same root field describes water bursting from rock (2:60), sharpening dawn as visible release while the local noun still names daybreak.\",\"reason\":\"The concrete recurrence at 2:60 supports release imagery for the root field, but local grammar selects the dawn noun rather than the water-bursting verbal construction.\",\"representative_source_ids\":[\"QI-cb768b26\",\"MI-63d68d33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:variant-apparatus","source_type":"word_analysis","support_id":"sup_7d34ed8920975b1a901b","text":"{\"blocking_evidence\":null,\"headline\":\"variants test texture without replacing the reading\",\"reader_payoff\":\"The reader notices that indefinitizing or internal-vowel variants expose what the received definite genitive form is doing, without taking control of the local parse.\",\"reason\":\"The variant rows are useful as contrastive apparatus, but the aligned local surface remains the definite genitive noun governed by the oath particle.\",\"representative_source_ids\":[\"QF-2a4be0cc\",\"QF-883f7918\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:1:delayed-oath-answer","source_type":"word_analysis","support_id":"sup_84b4f03b9bfbf1d49fb3","text":"{\"blocking_evidence\":null,\"headline\":\"evidence accumulates before verdict\",\"reader_payoff\":\"The reader notices that the oath begins before its answer is explicit, allowing the signs to gather force before the possible answer at 89:14.\",\"reason\":\"Attachment evidence licenses a compressed oath predicate, and the CRITICAL row ties the suspended opening to a possible later oath answer at 89:14.\",\"representative_source_ids\":[\"QT-6a218191\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:disclosure-before-verdict","source_type":"word_analysis","support_id":"sup_985619be52d2c80bc6fc","text":"{\"blocking_evidence\":null,\"headline\":\"dawn image anticipates later disclosure\",\"reader_payoff\":\"The reader notices that the first image of visibility after concealment prepares the delayed explicit verdict at 89:14 without turning dawn into abstraction.\",\"reason\":\"The concrete dawn noun is the first content word, and the oath answer can remain delayed until 89:14, so the disclosure payoff is locally motivated by position and oath structure.\",\"representative_source_ids\":[\"QS-088be17a\",\"QS-da89de75\",\"QE-79e6255a\",\"QY-5fcfd18c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:nominal-compression","source_type":"word_analysis","support_id":"sup_a10bb765fbfe60540941","text":"{\"blocking_evidence\":null,\"headline\":\"a dynamic root is stabilized as a noun\",\"reader_payoff\":\"The reader notices that the ayah presents the result-threshold as witness instead of narrating a process of bursting open.\",\"reason\":\"The local form is a noun in a two-word oath phrase, while V4 and the CRITICAL rows show verbal and process branches that are compressed rather than syntactically selected here.\",\"representative_source_ids\":[\"QF-136a444e\",\"QF-dded59b8\",\"MF-a53cb902\",\"QT-fc793fef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:surface-binding","source_type":"word_analysis","support_id":"sup_d120bf5c011416206166","text":"{\"blocking_evidence\":null,\"headline\":\"sound and script bind the noun to the oath\",\"reader_payoff\":\"The reader notices that the known dawn noun is not given a fresh independent onset; it is drawn directly into the compact oath phrase.\",\"reason\":\"The article-bearing noun follows the prefixed particle without an independent onset, matching the licensed particle-complement relation in {{ar:وَٱلْفَجْرِ}} ({{tr:wa-l-fajri}}).\",\"representative_source_ids\":[\"QF-1e797704\",\"QF-20893fc1\",\"QP-40affba8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:rupture-release-pressure","source_type":"word_analysis","support_id":"sup_ecc45297c6340290ac68","text":"{\"blocking_evidence\":null,\"headline\":\"dawn is felt as release through concealment\",\"reader_payoff\":\"The reader notices dawn as a breaking-open and release of light through darkness, while the local word still names dawn rather than an independent bursting verb.\",\"reason\":\"V4 accepts both the dawn branch and the physical splitting or outflow branch for {{ar:ف ج ر}} ({{tr:f-j-r}}), but the local surface is a definite noun, so the root pressure survives as image rather than as a local verbal event.\",\"representative_source_ids\":[\"QS-294b75a1\",\"QS-712cac28\",\"QS-d6286136\",\"MS-9377e1d0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:1:2:definite-recognized-threshold","source_type":"word_analysis","support_id":"sup_f356f557507aab5662b7","text":"{\"blocking_evidence\":null,\"headline\":\"the article presents known daybreak\",\"reader_payoff\":\"The reader notices that the oath invokes the recognizable phenomenon of daybreak, not generic light or an indefinite morning event.\",\"reason\":\"The local noun is definite and singular, V4 includes the dawn branch for this expression, and the article remains audible before the moon letter.\",\"representative_source_ids\":[\"QG-db65c5f8\",\"QG-ec3e6b99\",\"QS-9483e161\",\"QP-29001b4b\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001132","role":"Morning light breaking from night, including the true/false dawn distinction, supplies both the threshold and its epistemic ambiguity.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"The break at which light begins to separate night while genuine emergence must still be distinguished from a deceptive signal.","before":"A generic label for early morning."},"confidence":"strong","focus_anchor":"The sole focus noun at word 1 and its ف ج ر root.","mechanism":"The focus names a luminous threshold in which night is broken, but its branch scope also preserves a distinction between a true and a false first light. Dawn is therefore an event of emergence and an initially uncertain act of discrimination.","model_id":"base_threshold_discrimination"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_threshold_discrimination","source_type":"hft","support_id":"sup_c7e4a1fc4896d6bd969d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001132","role":"Broad splitting with outflow turns dawn from a clock label into an opening that releases what had been held behind a boundary.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"A pressured boundary opening wide enough for a stored light, water-like flow, or other latent content to issue out.","before":"The appearance of daylight."},"confidence":"strong","focus_anchor":"The ف ج ر root of the focus noun at word 1.","mechanism":"The root makes dawn spatial and material: pressure finds or makes a broad fissure, then what was contained issues through it. Light is one realization of a more general breach-and-release process.","model_id":"base_material_rupture"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_material_rupture","source_type":"hft","support_id":"sup_cd9f725fc7cb7a8c7509","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001132","role":"The sudden inrush of a multitude or calamities makes the focus capable of naming an overwhelming arrival as well as a gradual brightening.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"A threshold suddenly overrun by many arrivals, with dawn felt as impact rather than merely illumination.","before":"A gradual natural transition."},"confidence":"exploratory","focus_anchor":"The same ف ج ر root carried by the focus noun.","mechanism":"A branch in which many people or calamities burst upon a group gives the apparently quiet dawn an abrupt collective vector. The opening can be experienced from the receiving side as an arrival that cannot be contained.","model_id":"base_sudden_collective_inrush"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_sudden_collective_inrush","source_type":"hft","support_id":"sup_b770d0100d87afdf838c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001132","role":"Departure from right and rupture of restraint inserts a moral tear into the natural image of daybreak.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"An opening whose light may disclose, answer, or itself echo a prior violation of limits.","before":"A morally neutral natural opening."},"confidence":"medium","focus_anchor":"The focus noun's ف ج ر root at word 1.","mechanism":"The physical breach has an ethical polarity: the same root can figure departure from right and the tearing of restraint. Dawn can expose a breach, but the word can also carry the breach it exposes.","model_id":"base_ethical_breach"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_ethical_breach","source_type":"hft","support_id":"sup_55b164c21413fe63b462","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلْفَجْرِ","ayah_ref":"89:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001132/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001132","role":"Abundant generosity and good flowing outward give the rupture a distributive, beneficent direction.","root":"ف ج ر","source_ref":"89:1","source_word_indices":["1"]}],"changed_reading":{"after":"Good released across a boundary, with daybreak functioning as an image of abundance that refuses enclosure.","before":"Light made visible at a boundary."},"confidence":"exploratory","focus_anchor":"The ف ج ر lexical field activated by the focus noun.","mechanism":"The root also supports expansive generosity and good that wells outward. On this branch, dawn is not only exposure but benefaction: what opens gives beyond itself.","model_id":"base_overflowing_good"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_overflowing_good","source_type":"hft","support_id":"sup_64f6e00e3b37403cdc66","trust":"legacy_unbound"}]}
</lane_packet_json>
