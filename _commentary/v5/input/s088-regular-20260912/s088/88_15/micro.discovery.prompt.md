# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:15**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_15/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:15",
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
{"branch_registry":[{"boundary":"Çekirdek, yalnızca bir araya gelmeyi değil, düz bir çizgi üzerinde yan yana düzenlenmeyi gerektirir.","branch_kind":"bare","branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_35fdda236bc8e6e95e1f","lane":"micro"},{"candidate_id":"cand_d26efbb329c83556e5be","lane":"micro"},{"candidate_id":"cand_1e0be5affd1ab279bc4f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"düz bir sıra oluşturma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok ögeyi düz bir çizgi üzerinde yan yana yerleştirme ya da bu biçimde düzenlenmiş olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanların, özellikle savaş bağlamında, yan yana bir çizgi düzeninde durması ve bu düzenin kurulduğu mevki."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşların kanatlarını açıp kıpırdatmadan durması veya kesilecek hayvanların yan yana dizilmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ögeleri yan yana düz bir çizgide düzenleme ve bu düzende bulunma çekirdeğini doğal ve kısa biçimde karşılar.","boundary_detail":"Çekirdek, yalnızca bir araya gelmeyi değil, düz bir çizgi üzerinde yan yana düzenlenmeyi gerektirir.","branch_image_ar":"الاصطفاف على خط مستو","concept_gloss":"düz bir sıra oluşturma","contextual_glosses":[{"applicability":"Bir topluluğun ya da nesne kümesinin kendi üzerinde gerçekleşen düzenlenmeyi anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yan yana bir çizgi düzenine girme ve sonuçta o düzende bulunma korunur."},"facet_ids":["F001","F002"],"text":"sıraya dizilmek","usage_role":"contextual"},{"applicability":"Kuşların uçuş sırasında kanatlarını yanlara açıp hareket ettirmeden tuttuğu özel bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş bağlamındaki açılmış kanatların düzenli ve hareketsiz tutulması korunur."},"facet_ids":["F003"],"text":"kanatlarını açıp sabit tutmak","usage_role":"explanatory"}],"definition":"Nesneleri ya da bir topluluğu düz bir çizgi üzerinde yan yana dizmek veya kişilerin ve varlıkların böyle bir düzen içinde durmasıdır. Savaş düzeni ile kanatlarını açıp sabit tutan kuşlar gibi kullanımlar bu temel uzamsal düzenin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok ögeyi düz bir çizgi üzerinde yan yana yerleştirme ya da bu biçimde düzenlenmiş olma."},{"facet_id":"F002","role":"specialization","statement":"İnsanların, özellikle savaş bağlamında, yan yana bir çizgi düzeninde durması ve bu düzenin kurulduğu mevki."},{"facet_id":"F003","role":"example","statement":"Kuşların kanatlarını açıp kıpırdatmadan durması veya kesilecek hayvanların yan yana dizilmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Düz çizgi ve yan yanalık bulunmadan gerçekleşen her türlü bir araya gelmeyi de kapsar.","collision":"Su başında toplanma dalıyla kolayca karışır.","fit":"broadening","loses":null,"preserves":"Birden çok kişinin ya da ögenin birlikte bulunması korunur."},"text":"toplanma"}],"identity_rationale":"Kaynak ifadesi, nesneleri ya da kişileri düz bir çizgi üzerinde yan yana yerleştirme ve bu düzende durma çekirdeğini açıkça destekler. Savaşta durulan yer, hareketsiz açılmış kanatlarla duran kuşlar ve kesim için yan yana duran hayvanlar bu çekirdeğin bağlama özgü gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"düz çizgi üzerinde yan yana duran ögelerden oluşan sıra"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yan yana sıraya dizmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yan yana sıraya girmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sıra halinde duran; kanatlarını açıp sabit tutan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"savaş sırasının kurulduğu mevki"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sıra halinde dizilmiş"}],"lexicalization_note":"Dal yalın kullanımlarla tanıklanmıştır; tanım herhangi bir özel tamlamaya ya da tek bir bağlama bağlanmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çizgisel düzeni topluluk adı, sıra içi hareket ve su başında toplanmadan ayıran üç karşılaştırma sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düzenleme eylemi ile çizgisel sonucu temel alır; komşu dal ise belirli bir topluluk ya da düzenli küme türünü adlandırır.","focus_only":"Düz çizgi üzerinde yan yana dizme eylemini ve bu düzende durmayı genel olarak kapsar.","gloss":"düzenli bir sıra ya da bölük","neighbor_only":"İnsan bölüğü, asker topluluğu veya aynı düzen üzerinde sıralanmış evler gibi belirli kümeleri ve bunların birbirine geçişli örgüsünü adlandırır.","neighbor_ref":"root_000812/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da çok sayıda ögenin yan yana ve düzenli biçimde yerleşmesi vardır."},{"boundary_match":"field_only","distinction":"Odak dal sıranın kendisini kurar veya adlandırır; komşu dal mevcut sıra içindeki konumları ileri geri değiştirir.","focus_only":"Sıranın kurulmasını ve çizgi üzerindeki düzenli duruşu bildirir.","gloss":"savaş sırasında yer değiştirme","neighbor_only":"Kurulmuş savaş sıralarında bazı kişileri öne, bazılarını geriye kaydırarak düzenleme yapmayı bildirir.","neighbor_ref":"root_000316/B011","relation_type":"same_field","shared_zone":"İki dal da savaş sıralarının mekânsal düzeniyle ilgilidir."},{"boundary_match":"partial","distinction":"Su başında toplanmak çizgisel bir düzen gerektirmez; odak dalın ayırıcı özelliği düz sıra biçimidir.","focus_only":"Bir çizgi üzerinde yan yana düzenlenmeyi zorunlu kılar.","gloss":"su başında toplanma","neighbor_only":"Yalnızca su başında bir araya gelmeyi bildiren kalıpla sınırlıdır.","neighbor_ref":"root_000871/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda da birden çok katılımcının aynı yerde bulunması söz konusudur."}],"source_phrase_ar":"الصف معروف (ayn;tahdhib); الصف أن تجعل الشيء على خط مستو (mufradat); صففت القوم فاصطفوا (ayn;sihah;tahdhib); المصف الموقف والجمع المصاف (ayn;sihah;tahdhib); الصافات صفا يعني الملائكة (mufradat;tahdhib); الطير الصواف التي تصف أجنحتها فلا تحركها (ayn;tahdhib); البدن الصواف التي تصفف ثم تنحر (ayn;tahdhib)","source_summary":"Kaynaklar, düz çizgi üzerinde yan yana düzenlenme çekirdeğinde birleşir ve insan, savaş, kuş ve kesim hayvanı bağlamlarını bu çekirdeğe bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"جعل الشيء أو الجماعة صفا على خط مستو، ووقوف القوم والملائكة والخيل والطير والبدن مصطفة، والمصف في الحرب","what_is_not_ar":"ليس ناقة الصفوف ولا الصفيف من اللحم ولا الصفصف من الأرض"},"support_links":["sup_1cb7537c91d559c6abab","sup_4b7a5a5dcce7a39a8b7f","sup_51fdc70e6969b0515821"]},{"boundary":"Çokluk, tek sağımda kullanılan süt kaplarına ilişkindir; ikinci kullanım ise süt miktarından bağımsız bir ayak duruşudur.","branch_kind":"bare","branch_ref":"root_000871/B002","candidate_links":[{"candidate_id":"cand_0e1529d859ecaeb2ca16","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin tek bir sağımda iki ya da daha çok süt kabını doldurması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi devenin sağım sırasında ön ayaklarını yan yana hizalayarak durması."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kap sayısına dayalı ana kullanımını ve sağım sırasındaki duruş varyantını birlikte belirtmek gerektiğinde kullanılır.","boundary_detail":"Çokluk, tek sağımda kullanılan süt kaplarına ilişkindir; ikinci kullanım ise süt miktarından bağımsız bir ayak duruşudur.","branch_image_ar":"ناقة تجمع محالبها","concept_gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve","contextual_glosses":[{"applicability":"Süt bolluğu ve tek sağımda doldurulan kap sayısı öne çıktığında kullanılan doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi deve, tek sağım ve birden çok kabı dolduracak süt verme özellikleri korunur."},"facet_ids":["F001"],"text":"bir sağımda birkaç kap süt veren dişi deve","usage_role":"contextual"},{"applicability":"Kaynaklardaki duruşa dayalı kullanımın özellikle anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi devenin sağım anındaki ön ayaklarını yan yana getirme duruşu korunur."},"facet_ids":["F002"],"text":"sağılırken ön ayaklarını hizalayan dişi deve","usage_role":"explanatory"}],"definition":"Tek bir sağımda iki ya da daha çok kabı sütle dolduran dişi deve veya sağılırken ön ayaklarını yan yana hizalayan dişi devedir. İlk kullanım süt bolluğuna ve kap sayısına, ikincisi ise hayvanın duruşuna dayanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin tek bir sağımda iki ya da daha çok süt kabını doldurması."},{"facet_id":"F002","role":"source_variant","statement":"Dişi devenin sağım sırasında ön ayaklarını yan yana hizalayarak durması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kap sayısıyla ölçülmeyen her türlü süt bolluğunu da kapsar.","collision":"Genel süt bolluğunu bildiren komşu dalla karışır.","fit":"broadening","loses":null,"preserves":"Süt bolluğu ve deve niteliği korunur."},"text":"bol sütlü deve"}],"identity_rationale":"Kaynak ifadesi iki bağlı fakat farklı betimlemeyi aynı dalda toplar: dişi devenin tek sağımda iki veya daha çok kabı doldurması ve sağılırken ön ayaklarını yan yana hizalaması. Dal korunabilir, ancak kapları doldurma ile ayrı sağımları birleştirme birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dişi deveyi tek sağımda iki veya üç kaba sağma"}],"lexicalization_note":"Dalın iki yalın biçimi vardır; tanım hem çok kap doldurma niteliğini hem de sağım sırasındaki ayak duruşunu ayrı tutar.","neighbor_coverage_note":"Adayların tümü incelendi; iki kaplık yakın karşılık, üçlü sağım niteliği ve genel süt bolluğu dalın kap sayısı ile duruş sınırlarını yeterince belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal iki kapla sınırlı daha dar bir karşılıktır; odak dal iki veya daha çok kabı ve ayrıca ayak duruşu varyantını içerir.","focus_only":"İki kabın ötesine çıkabilmeyi ve sağımda ön ayakları hizalama varyantını da kapsar.","gloss":"tek sağımda iki kap dolduran dişi deve","neighbor_only":"Özellikle iki kaplık sütün tek sağımda bir araya getirilmesini adlandırır.","neighbor_ref":"root_000802/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da dişi devenin tek sağımda birden çok kabı sütle doldurmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın eşiği iki kaptır ve ayak duruşu varyantı bulunur; komşu dal üç sayısına ve farklı meme durumlarına bağlıdır.","focus_only":"İki ya da daha çok kap doldurmayı genel olarak veya ön ayakların hizalanmasını bildirir.","gloss":"üçlü sağım özelliği taşıyan dişi deve","neighbor_only":"Üç kap doldurma yanında üç meme ucundan sağılma, üçünün kuruması ya da bağlanması gibi başka üçlü özellikleri de kapsar.","neighbor_ref":"root_000203/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da dişi devenin sağımı ve kap sayısı üzerinden nitelenmesi vardır."},{"boundary_match":"field_only","distinction":"Komşu dal genel ve karşılaştırmalı bolluğu, odak dal ise tek sağımda doldurulan kapları ve ayrıca ayak duruşunu temel alır.","focus_only":"Süt bolluğunu doldurulan kap sayısıyla somutlaştırır ve bir duruş varyantı içerir.","gloss":"çok bol sütlü dişi deve","neighbor_only":"Sütün başka bol sütlü develerle karşılaştırıldığında daha da bol oluşunu bildirir.","neighbor_ref":"root_000200/B005","relation_type":"same_field","shared_zone":"İki dal da dişi devenin süt veriminin yüksekliğini konu edinir."}],"source_phrase_ar":"الصفوف الناقة التي تجمع بين محلبين في حلبة (maqayis;tahdhib); الصف أن تحلب الناقة في محلبين أو ثلاثة تصف بينها (sihah); ناقة صفوف للتي تصف أقداحا من لبنها (sihah); الصفوف ناقة تصف بين محلبين فصاعدا لغزارتها (mufradat); الصفوف أيضا التي تصف يديها عند الحلب (maqayis;sihah;tahdhib)","source_summary":"Kaynaklar, aynı adlandırma altında hem tek sağımda birden çok kap dolduran sütlü dişi deveyi hem de sağılırken ön ayaklarını hizalayan dişi deveyi aktarır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الناقة الصفوف التي تجمع بين محلبين أو ثلاثة في حلبة، أو تصف يديها عند الحلب","what_is_not_ar":"ليس صف القوم ولا صفيف اللحم ولا صفة البناء"},"support_links":["sup_4796e6a8ef57323c2950"]},{"boundary":"Güneşte kurutma, közde pişirme, yolculuk eti ve inceltici dilimleme tek bir zorunlu süreç gibi birleştirilmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000871/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"kurutmak ya da közlemek için sıra sıra serilmiş et","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Etin şeritlere ayrılıp güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi ve böyle hazırlanmış et."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolculukta pişmiş ya da kızartılmış olarak taşınan, ancak tam pişmemiş kalan et."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir et parçasını genişletip inceltecek biçimde dilimleme."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın et şeritlerini düzenli biçimde serme ve güneş ya da közle hazırlama çekirdeğini karşılar.","boundary_detail":"Güneşte kurutma, közde pişirme, yolculuk eti ve inceltici dilimleme tek bir zorunlu süreç gibi birleştirilmemelidir.","branch_image_ar":"الصَّفيف من اللحم","concept_gloss":"kurutmak ya da közlemek için sıra sıra serilmiş et","contextual_glosses":[{"applicability":"Güneşte kurutmaya yönelik et hazırlama eyleminin anlatıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin şeritlenmesi, sıra sıra serilmesi ve kurutma amacı korunur."},"facet_ids":["F001"],"text":"eti şeritler halinde serip kurutmak","usage_role":"contextual"},{"applicability":"Yolculukta taşınan pişmiş ya da kızartılmış etin içinin tam pişmemiş kaldığı kaynak varyantına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolculukta taşınma, et olma ve tam pişmeme özellikleri korunur."},"facet_ids":["F002"],"text":"tam pişmemiş yolculuk eti","usage_role":"explanatory"},{"applicability":"Et parçasını genişletip incelten dilimleme kullanımını açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin kesilmesi ve kesim sonucunda incelmesi korunur."},"facet_ids":["F003"],"text":"eti inceltecek biçimde dilimlemek","usage_role":"explanatory"}],"definition":"Etin şeritlenerek güneşte kurutulmak ya da köz üzerinde pişirilmek üzere sıra sıra serilmesi ve bu biçimde hazırlanmış ettir. Bunun yanında yolculukta taşınan fakat tam pişmemiş et ile eti inceltecek biçimde dilimleme de kaynakta ilişkili kullanımlar olarak yer alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Etin şeritlere ayrılıp güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi ve böyle hazırlanmış et."},{"facet_id":"F002","role":"source_variant","statement":"Yolculukta pişmiş ya da kızartılmış olarak taşınan, ancak tam pişmemiş kalan et."},{"facet_id":"F003","role":"extension","statement":"Bir et parçasını genişletip inceltecek biçimde dilimleme."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etin sıra sıra serilmesini, közde pişirme kullanımını ve işlem yönünü siler.","preserves":"Etin güneşte hazırlanmış bir ürün olabilmesi korunur."},"text":"kurutulmuş et"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel pişirme ve kızartma dallarıyla karışır.","fit":"narrowing","loses":"Şeritlere ayırıp sıra sıra serme ile güneşte kurutma seçeneklerini kaybeder.","preserves":"Etin ateş ısısıyla hazırlanması korunur."},"text":"ızgara et"}],"identity_rationale":"Kaynak ifadesi tek bir işlemden çok, etin şeritlenip güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmesi çevresindeki kullanımları toplar. Yolculukta taşınan fakat tam pişmemiş et ve eti inceltecek biçimde dilimleme, bu çekirdekle ilişkili fakat ondan ayrı varyantlardır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmiş et"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"eti şeritlere ayırıp sıra sıra sermek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"eti genişletip inceltecek biçimde dilimleme"}],"lexicalization_note":"Dal hem yalın adları hem de ete bağlı bir kalıbı içerir; yalın et adı, eti sıra sıra serme kalıbı ve inceltici dilimleme ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; dilimleme, kurutup saklama ve kor üzerinde pişirme dalları, odak dalın sıra sıra serme ile çoklu hazırlama yöntemlerini en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kesme biçimini temel alır; odak dalın çekirdeğinde kesilen etin kurutma veya közleme için düzenli biçimde serilmesi vardır.","focus_only":"Dilimlenen eti güneşte veya közde hazırlamak üzere sıra sıra sermeyi içerir.","gloss":"eti kesip yayvan dilimlere ayırma","neighbor_only":"Eti uzuvdan ya da kemik üzerinden ayırma ve genel olarak yayvan ya da ince parçalara kesme işlemlerini kapsar.","neighbor_ref":"root_000784/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da etin kesilerek ince veya yayvan parçalara dönüştürülmesini içerebilir."},{"boundary_match":"partial","distinction":"Odak dal düzenli serme biçimine bağlıdır ve köz kullanımına uzanır; komşu dal kurutma ve saklama sürecini daha geniş ürün alanında ele alır.","focus_only":"Et şeritlerinin sıra sıra serilmesini ve közde pişirme seçeneğini de kapsar.","gloss":"eti veya hurmayı kurutup saklama","neighbor_only":"Et yanında hurmanın kurutulması ve genel kurutma ya da saklama işlemlerini kapsar.","neighbor_ref":"root_000187/B002","relation_type":"near_neighbor","shared_zone":"İki dal etin kesilip kurutularak hazırlanması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal ısıyla pişirme yöntemidir; odak dal ise sıra sıra serilen etin hem kurutma hem közleme yoluyla hazırlanmasını adlandırır.","focus_only":"Etin sıra sıra serilmesini ve güneşte kurutulmasını da içerir.","gloss":"eti kor üzerinde pişirme","neighbor_only":"Etin doğrudan kor üzerine konmasını ve pişmesi için ısının yeniden yemeğe yöneltilmesini temel alır.","neighbor_ref":"root_000321/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda etin közle temas ederek pişirilmesi bulunabilir."}],"source_phrase_ar":"الصفيف قال قوم هو القديد (maqayis); اللحم يحمل في الأسفار طبيخا أو شواء فلا ينضج (maqayis); الصفيف القديد اذا شر في الشمس (ayn;tahdhib); الصفيف ما صف من اللحم على الجمر لينشوي (sihah); صففت اللحم قددته وألقيته صفا صفا (mufradat); التصفيف نحو التشريح (tahdhib)","source_summary":"Kaynaklar etin şeritlenmesi, sıra sıra serilmesi ve güneş ya da közle hazırlanması çevresinde birleşir; tam pişmemiş yolculuk eti ve inceltici dilimleme de ilişkili varyantlar olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصَّفيف، وهو اللحم المشرر أو المصفوف في الشمس أو على الجمر، واللحم المحمول في السفر طبيخا أو شواء فلا ينضج","what_is_not_ar":"ليس الصف المعروف ولا الصُّفَّة من البناء ولا الصفصف من الأرض"},"support_links":[]},{"boundary":"Yapıdaki bölüm ile eyer düzeneği aynı ad altında yer alır, fakat kanıt bunların biçimsel ayrıntılarını belirtmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000871/B004","candidate_links":[{"candidate_id":"cand_d26efbb329c83556e5be","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"yapı ya da eyer bölümü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yapıda veya eyerde bulunan özel bir bölüm ya da düzenek."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir hayvan için söz konusu eyer düzeneğini yapma."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynağın fiziksel biçimini belirtmediği yalın adın iki kullanım alanını ihtiyatlı biçimde karşılar.","boundary_detail":"Yapıdaki bölüm ile eyer düzeneği aynı ad altında yer alır, fakat kanıt bunların biçimsel ayrıntılarını belirtmez.","branch_image_ar":"الصُّفَّة في البناء والسرج","concept_gloss":"yapı ya da eyer bölümü","contextual_glosses":[{"applicability":"Yalnızca hayvan için ilgili parçanın yapıldığını bildiren kalıp kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan, eyer düzeneği ve bunu yapma eylemi korunur."},"facet_ids":["F002"],"text":"hayvan için eyer düzeneği yapmak","usage_role":"explanatory"}],"definition":"Bir yapıda ya da eyerde bulunan, biçimi kaynakta ayrıntılandırılmamış bölüm veya düzenektir. Hayvan için bu tür bir eyer düzeneği yapma eylemi de yalnızca ilgili kalıp içinde bu dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yapıda veya eyerde bulunan özel bir bölüm ya da düzenek."},{"facet_id":"F002","role":"associated_use","statement":"Bir hayvan için söz konusu eyer düzeneğini yapma."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Kaynağın belirtmediği belirli bir mimari biçimi varsayar.","fit":"narrowing","loses":"Eyer kullanımını ve hayvan için düzenek yapma kalıbını bütünüyle kaybeder.","preserves":"Bir yapı bölümü olma olasılığını korur."},"text":"sundurma"}],"identity_rationale":"Kaynak ifadesi bir yapıda ve eyerde bulunan bölüm ya da düzenek ile hayvan için böyle bir eyer düzeneği yapma kullanımını destekler. Ancak parçanın fiziksel biçimi kaynak ifadesinde açıklanmadığından, tanım onu belirli bir mimari tür veya belirli bir eyer parçasıyla özdeşleştirmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yapıda ya da eyerde bulunan bölüm veya düzenek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hayvan için eyer düzeneği yapmak"}],"lexicalization_note":"Yalın ad yapı ve eyer alanlarına uzanırken, kalıp yalnızca hayvan için ilgili eyer düzeneğini yapma eylemini bildirir.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; destek parçası, belirli semer biçimi ve bütün binek takımı karşılaştırmaları kanıtta biçimi belirsiz kalan bölümün sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal parçayı destek işleviyle tanımlar; odak dalın kanıtı ise işlevi ve biçimi ayrıntılandırmadan yapı veya eyer bölümünü adlandırır.","focus_only":"Yapı veya eyer üzerindeki adlandırılmış bölümü ve onun hayvan için yapılmasını kapsar.","gloss":"taşıyıcı destek parçası","neighbor_only":"Duvar, çatı, yara ve eyer gibi şeylere destek ya da dayanak olarak eklenen yardımcı parçaların genel alanını kapsar.","neighbor_ref":"root_000580/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da eyer veya yapı üzerinde bulunan işlevsel bir parça söz konusu olabilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli biçimdeki bir semeri adlandırır; odak dal biçimi belirsiz bir eyer bölümünü ve ayrıca yapıdaki kullanımı kapsar.","focus_only":"Yapı alanına da uzanır ve hayvan için ilgili düzeneği yapma eylemini içerir.","gloss":"yayılmış ve ayrılmamış semer","neighbor_only":"Özellikle yayılmış, ayrılmamış bir semer türünü ve onun belirli yapısını adlandırır.","neighbor_ref":"root_000116/B013","relation_type":"near_neighbor","shared_zone":"İki dal hayvanın sırtında kullanılan eyer veya semer donanımı alanında buluşur."},{"boundary_match":"field_only","distinction":"Komşu dal bütün binek takımını, odak dal ise eyer üzerindeki bir bölüm veya düzeneği belirtir.","focus_only":"Eyerin bir bölümünü veya düzeneğini ve bunun yapılmasını bildirir.","gloss":"deve binek takımı","neighbor_only":"Devenin sırtına konan bütün binek takımını adlandırır.","neighbor_ref":"root_000551/B002","relation_type":"same_field","shared_zone":"Her iki dal da hayvanın sırtındaki binme donanımıyla ilgilidir."}],"source_phrase_ar":"الصفة من البنيان والسرج ايضا (ayn); صفة الدار والسرج واحدة الصفف (sihah); صفة السرج (tahdhib); صففت للدابة صفة أي عملتها له (tahdhib); الصفة من البنيان وصفة السرج (mufradat)","source_summary":"Kaynaklar, yapıdaki bölüm ile eyer üzerindeki düzeneği aynı yalın ad altında verir ve hayvan için bu düzeneği yapma eylemini ayrı bir kalıpla tanıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"الصُّفَّة من البنيان، وصُفَّة السرج، وما يعمل للدابة من ذلك","what_is_not_ar":"ليست صفة الوصف ولا صف القوم ولا الصفيف"},"support_links":["sup_1cb7537c91d559c6abab"]},{"boundary":"Düzlük ve pürüzsüzlük çekirdektir; bitkisizlik ise tanıklanmış fakat zorunlu olmayan bir varyanttır.","branch_kind":"bare","branch_ref":"root_000871/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"düz ve pürüzsüz arazi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzeyi düz ve pürüzsüz olan arazi ya da geniş düzlük."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki örtüsü bulunmayan, çıplak düz arazi."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzeyin tek bir sıra gibi kesintisiz ve aynı düzeyde görünmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bütün tanıklardaki ortak arazi ve yüzey çekirdeğini en kısa doğal biçimde karşılar.","boundary_detail":"Düzlük ve pürüzsüzlük çekirdektir; bitkisizlik ise tanıklanmış fakat zorunlu olmayan bir varyanttır.","branch_image_ar":"الأرض الصفصف","concept_gloss":"düz ve pürüzsüz arazi","contextual_glosses":[{"applicability":"Bitki örtüsünün bulunmadığının ayrıca belirtildiği kaynak varyantı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi, düzlük, pürüzsüzlük ve bitkisizlik özellikleri birlikte korunur."},"facet_ids":["F001","F002"],"text":"bitkisiz, düz ve pürüzsüz arazi","usage_role":"contextual"},{"applicability":"Arazinin tek bir sıra gibi aynı düzeyde uzanması benzetmesini öne çıkaran bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arazi yüzeyinin aynı düzeyde ve kesintisiz görünmesi korunur."},"facet_ids":["F003"],"text":"kesintisiz düzlük","usage_role":"explanatory"}],"definition":"Yüzeyi düz ve pürüzsüz olan arazi veya geniş düzlük alanıdır. Bazı kullanımlarda bu arazinin bitkisiz ve çıplak olduğu da özellikle belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzeyi düz ve pürüzsüz olan arazi ya da geniş düzlük."},{"facet_id":"F002","role":"source_variant","statement":"Bitki örtüsü bulunmayan, çıplak düz arazi."},{"facet_id":"F003","role":"extension","statement":"Yüzeyin tek bir sıra gibi kesintisiz ve aynı düzeyde görünmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"İklimsel bir arazi türünü gereksiz yere varsayar.","fit":"narrowing","loses":"Düzlük ve pürüzsüzlük çekirdeğini zorunlu olarak taşımaz, bitkili olabilen çekirdek kullanımları dışarıda bırakır.","preserves":"Geniş ve bitkisiz arazi olabilme özelliği korunur."},"text":"çöl"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği arazinin düz, pürüzsüz ve geniş bir düzlük olmasıdır. Bitkisizlik ve çıplaklık bazı tanımlarda eklenen bir yüzey niteliğidir; her düz ve pürüzsüz arazi için zorunlu koşul gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz, kimi kullanımda bitkisiz arazi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"düz ve pürüzsüz araziler"}],"lexicalization_note":"Dal yalın arazi adlarıyla tanıklanır; tanım başka bir tamlamaya dayanmaz ve yüzey özelliklerini arazi çekirdeğine bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; tam eşdeğer arazi dalı ile çakıllı, beyaz ve genel düz yer komşuları pürüzsüzlük, bitkisizlik ve ek yüzey niteliklerini ayırır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; tek sıra görünümü veya bitkisizlik gibi betimlemeler aynı arazi kavramının bağımlı özellikleridir.","focus_only":null,"gloss":"düz ve pürüzsüz arazi","neighbor_only":null,"neighbor_ref":"root_000870/B001","relation_type":"synonym","shared_zone":"Her iki dalın çekirdeği düz, pürüzsüz ve geniş arazi yüzeyidir."},{"boundary_match":"partial","distinction":"Komşu dal çakıllı yüzey ve belirli arazi türlerini ekler; odak dalın çekirdeği yalnızca düzlük ile pürüzsüzlüktür.","focus_only":"Çakıllı olmayı gerektirmeden düz ve pürüzsüz araziyi adlandırır.","gloss":"çıplak ve çakıllı düzlük","neighbor_only":"Bozkır veya geçit alanını çıplak ve özellikle çakıllı olabilen yüzeyiyle niteler.","neighbor_ref":"root_001420/B009","relation_type":"near_synonym","shared_zone":"İki dal da düz, çıplak ve geniş arazi için kullanılabilir."},{"boundary_match":"partial","distinction":"Komşu dal beyazlık ve adlandırılmış yer kapsamını ekler; odak dal düz yüzey yapısıyla sınırlıdır.","focus_only":"Beyazlık veya kum niteliği olmadan düz ve pürüzsüz araziyi karşılar.","gloss":"beyaz ve pürüzsüz arazi","neighbor_only":"Beyazlık, kum tepesi ve yer adı kullanımlarını da kapsar.","neighbor_ref":"root_000168/B013","relation_type":"near_synonym","shared_zone":"Her iki dal bitkisiz ve pürüzsüz bir araziyi adlandırabilir."},{"boundary_match":"partial","distinction":"Odak dal yüzeyin pürüzsüzlüğünü çekirdeğe alır; komşu dal daha genel bir düz yer adıdır.","focus_only":"Pürüzsüz yüzeyi ve kimi kullanımlarda bitkisizliği özellikle taşır.","gloss":"düz tabanlı yer","neighbor_only":"Genel olarak düz bir tabanı veya düz yeri adlandırır, pürüzsüzlük koşulu taşımaz.","neighbor_ref":"root_001204/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalın referansı düz bir arazi veya yer olabilir."}],"source_phrase_ar":"الصفصف وهو المستوي من الأرض (maqayis); الصفصف الفلاة المستوية الملساء (ayn); الصفصف المستوى من الأرض (sihah); الصفصف الذي لا نبات فيه (tahdhib); الصفصف القرعاء (tahdhib); الصفصف المستوي الأملس (tahdhib); الصفصف المستوي من الأرض كأنه على صف واحد (mufradat)","source_summary":"Kaynaklar düz ve pürüzsüz arazi çekirdeğinde birleşir; bitkisizlik, çıplaklık ve tek bir sıra gibi aynı düzeyde görünme bu yüzeyin ek betimlemeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الصَّفْصَف والقاع المستوي الأملس من الأرض، وما لا نبات فيه أو القرعاء","what_is_not_ar":"ليس صف القوم ولا الصفيف ولا شجر الصفصاف"},"support_links":[]},{"boundary":"Bu dal yalnızca söğüt ağacını adlandırır; düz ve pürüzsüz arazi anlamını içermez.","branch_kind":"bare","branch_ref":"root_000871/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"söğüt ağacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söğüt ağacı türünün adı."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek ve doğrudan botanik referansını doğal Türkçe ağaç adıyla eksiksiz karşılar.","boundary_detail":"Bu dal yalnızca söğüt ağacını adlandırır; düz ve pürüzsüz arazi anlamını içermez.","branch_image_ar":"الصفصاف شجر الخلاف","concept_gloss":"söğüt ağacı","definition":"Söğüt ağacını adlandıran yalın bir bitki adıdır. Benzer sesli arazi adından bağımsız bir botanik referansa sahiptir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söğüt ağacı türünün adı."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bitki yerine arazi yüzeyi anlamı ekler.","collision":"Düz ve pürüzsüz arazi dalıyla doğrudan karışır.","fit":"displacement","loses":"Ağaç türü olma ve söğüt kimliğini bütünüyle kaybeder.","preserves":"Benzer sesli başka bir dalın yüzeyle ilgili referansını taşır."},"text":"düz arazi"}],"identity_rationale":"Kaynak ifadesi dalı açık ve tutarlı biçimde belirli bir ağaç türü olarak tanımlar. Arazi adıyla yazılış benzerliği bulunsa da referans ağaçtır ve düz arazi dalından ayrı tutulması gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"söğüt ağacı"}],"lexicalization_note":"Dal tek bir yalın ağaç adıyla tanıklanmıştır; tanım herhangi bir kalıp ya da mecazi uzantı eklemez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; aynı ağaç türünü adlandıran tam eşdeğer dal yararlı tek doğrudan karşılaştırmadır, öteki adaylar yalnızca genel bitki alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kavramsal çekirdek ve kapsam bakımından bir ayrım yoktur; iki dal aynı ağaç referansında örtüşür.","focus_only":null,"gloss":"söğüt ağacı","neighbor_only":null,"neighbor_ref":"root_000870/B002","relation_type":"synonym","shared_zone":"Her iki dal da aynı söğüt ağacı türünü doğrudan adlandırır."}],"source_phrase_ar":"الصفصف شجر الخلاف الواحدة بالهاء (ayn); الصفصاف شجر الخلاف (sihah;mufradat); الصفصاف الخلاف (tahdhib); هو شجر الخلاف بلغة أهل الشام (tahdhib)","source_summary":"Kaynaklar, yalın adın söğüt ağacını gösterdiğinde birleşir; bölgesel kullanım bilgisi kavramın ağaç türü sınırını değiştirmez.","sources":["AY","SI","TA","MU"],"what_is_ar":"الصَّفصاف شجر الخلاف","what_is_not_ar":"ليس الصفصف من الأرض ولا الصف المعروف"},"support_links":[]},{"boundary":"Anlam genel toplanma değil, yalnızca suyla kurulan belirtilmiş kalıp içindeki bir araya gelmedir.","branch_kind":"collocation","branch_ref":"root_000871/B007","candidate_links":[{"candidate_id":"cand_1e0be5affd1ab279bc4f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","surface_ar":"مَصْفُوفَةٌ"}],"gloss":"su başında toplanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun su başında bir araya gelmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı su başında toplanma anlamının iki ayrı fiil biçimiyle ifade edilmesi."}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca topluluğun su çevresinde bir araya geldiği tanıklı kalıpların ortak kavramını karşılar.","boundary_detail":"Anlam genel toplanma değil, yalnızca suyla kurulan belirtilmiş kalıp içindeki bir araya gelmedir.","branch_image_ar":"التصافّ على الماء","concept_gloss":"su başında toplanma","contextual_glosses":[{"applicability":"İki tanıklı kalıbın da cümle içinde doğal Türkçe karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcıların su başında aynı yere gelmesi ve kalıbın suyla sınırlı oluşu korunur."},"facet_ids":["F001","F002"],"text":"suyun başında bir araya gelmek","usage_role":"contextual"}],"definition":"Bir topluluğun su başında bir araya gelmesidir. Anlam, suyu tamamlayıcı olarak alan iki eşdeğer kalıpla sınırlıdır ve düz sıra oluşturmayı gerektirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun su başında bir araya gelmesi."},{"facet_id":"F002","role":"source_variant","statement":"Aynı su başında toplanma anlamının iki ayrı fiil biçimiyle ifade edilmesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta bulunmayan çizgisel yan yanalık ve sıra düzeni ekler.","collision":"Düz çizgi üzerinde sıralanma dalıyla doğrudan karışır.","fit":"displacement","loses":"Su başında bir araya gelme koşulunu kaybeder.","preserves":"Bir topluluğun ortak bir yerde bulunmasını korur."},"text":"sıraya girmek"},{"category":"alternative","error_profile":{"adds":"Suyla bağlantısı olmayan her türlü toplanmayı da kapsar.","collision":"Genel toplanma komşularıyla sınırı belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Birden çok katılımcının bir araya gelmesi korunur."},"text":"toplanmak"}],"identity_rationale":"Kaynak ifadesi iki fiil biçimini aynı anlamda verir ve kullanımı su başında bir araya gelme durumuyla açıkça sınırlar. Çizgi halinde dizilme anlamı bu tanıklığın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"su başında toplanmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"su başında toplanmak"}],"lexicalization_note":"Dal yalnızca suyla kurulan iki tanıklı kalıpta geçer; buradan yalın fiile genel bir toplanma anlamı aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nesne çevresinde genel toplanma, tek yerde toplanma ve çizgisel sıralanma karşılaştırmaları suya bağlı kalıbın sınırını açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın odak noktası zorunlu olarak sudur; komşu dal farklı nesneler çevresindeki toplanmayı ve yönelmeyi daha genel biçimde kapsar.","focus_only":"Toplanmayı özellikle su başına bağlayan tanıklı iki kalıpla sınırlıdır.","gloss":"bir şeyin çevresinde toplanma","neighbor_only":"İnsan veya hayvanların herhangi bir şeyin çevresinde ya da üzerinde durup ona yönelmesini genel olarak kapsar.","neighbor_ref":"root_001038/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda bir topluluk belirli bir odak noktasının çevresinde bir araya gelir."},{"boundary_match":"partial","distinction":"Komşu dal genel yer birliğini anlatır; odak dal yalnızca su başındaki toplanmanın kalıplaşmış ifadesidir.","focus_only":"Su tamamlayıcısıyla kurulan belirli söz dizimsel kalıba bağlıdır.","gloss":"tek bir yerde toplanma","neighbor_only":"Özellikle develer başta olmak üzere şeylerin tek bir yere toplanmasını su koşulu olmadan bildirir.","neighbor_ref":"root_001616/B001","relation_type":"near_synonym","shared_zone":"İki dal da birden çok katılımcının aynı yerde bir araya gelmesini ifade eder."},{"boundary_match":"partial","distinction":"Odak dal suya bağlı toplanmadır; komşu dalın belirleyici özelliği su değil, düz çizgi üzerindeki yan yanalıktır.","focus_only":"Su başında bir araya gelmeyi gerektirir, çizgisel düzen istemez.","gloss":"düz bir sıra oluşturma","neighbor_only":"Ögelerin düz bir çizgi üzerinde yan yana sıralanmasını gerektirir, su koşulu taşımaz.","neighbor_ref":"root_000871/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir topluluğun ortak bir mekânsal düzen içinde bulunmasını anlatabilir."}],"source_phrase_ar":"تضافوا على الماء وتصافوا عليه بمعنى واحد إذا اجتمعوا عليه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, iki fiil biçiminin su başında toplanma anlamında eşdeğer kullanıldığını bildirir."}],"source_summary":"Kanıt, anlamı su başında bir araya gelme kalıbıyla sınırlar ve iki fiil biçimini bu sınırlı kullanımda eşdeğer gösterir.","sources":["TA"],"what_is_ar":"تصافوا على الماء، أي اجتمعوا عليه","what_is_not_ar":"ليس الاصطفاف في صف للحرب أو الصلاة، ولا صفيف اللحم"},"support_links":["sup_4b7a5a5dcce7a39a8b7f"]}],"candidate_inventory":[{"anchor_refs":["88:15:1"],"branch_refs":[],"candidate_id":"cand_bf6afc5f5635d6837c62","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:1:catalog-coordination","source_type":"word_analysis","support_ids":["sup_b70fa5f2817459de7e02","sup_dc0d815224da541aa535"],"title":"catalog coordination rather than restart","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:1","qac_refs":["88:15:1:1"],"status":"accepted"}},{"anchor_refs":["88:15:1"],"branch_refs":[],"candidate_id":"cand_5df90ec1896a4790e6c7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:1:compressed-locative-frame","source_type":"word_analysis","support_ids":["sup_64abf0bd1c622f243d5d","sup_b70fa5f2817459de7e02"],"title":"compressed carried locative frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:1","qac_refs":["88:15:1:1"],"status":"accepted"}},{"anchor_refs":["88:15:1"],"branch_refs":[],"candidate_id":"cand_0bf50485921cb22fa28b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:1:rhythmic-pickup","source_type":"word_analysis","support_ids":["sup_85941bc070bfe582cc63","sup_b70fa5f2817459de7e02"],"title":"light recited pickup into the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:1","qac_refs":["88:15:1:1"],"status":"accepted"}},{"anchor_refs":["88:15:1"],"branch_refs":[],"candidate_id":"cand_8c1a5789915dcd29af9d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:1:serial-additive-chain","source_type":"word_analysis","support_ids":["sup_a78c22bf61f9582203d0","sup_b70fa5f2817459de7e02"],"title":"serial additive chain across furnishings","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:1","qac_refs":["88:15:1:1"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_c57d4251117bd6c6fa29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:collective-modifier-licensing","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_ffd9c79b3ba1db3eb365"],"title":"plural head handled as collective set","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_4a3c029c676d00450933","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:furnishing-sequence-slot","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_40d3f5af23a39946faf0"],"title":"bodily support slot in the sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_fbdfb2ee216395583295","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:hapax-concrete-anchor","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_d89694a9b419e95491cc"],"title":"hapax concrete furnishing term","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_1f9f6b4f021fa30ce84b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:present-inventory-item","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_86a5303b7433b9cd7c47"],"title":"nominative present furnishing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_fac24204b0b82e33edf5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:sound-closure-before-order","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_a896bdc3b4280950169a"],"title":"soft furnishing word closes firmly","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_360b5bb7e45df4223c0b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:support-plus-display","source_type":"word_analysis","support_ids":["sup_29ff4e9baee90a72e07e","sup_2f2e4d988901489a0e5d"],"title":"support object before ordered display","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_dab01bf33371ae067af1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:tactile-support-object","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_9f786e58954e3850c8df"],"title":"material support rather than abstract ease","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_b0dc8c762627e8e32722","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:15:2:uncounted-plural-abundance","source_type":"word_analysis","support_ids":["sup_2f2e4d988901489a0e5d","sup_37b2ed15f26a92612cc2"],"title":"uncounted plural abundance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:2","qac_refs":["88:15:1:2"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_d531883ea39e37ab702e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:bound-modifier-case","source_type":"word_analysis","support_ids":["sup_10e91420685e34f64ea4","sup_e485c0c7da8b8de6cbec"],"title":"orderedness bound to the head noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_0a4aff37c2f685f18b83","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:boundary-spatial-handoff","source_type":"word_analysis","support_ids":["sup_33b7ac10ede54326c3c3","sup_e485c0c7da8b8de6cbec"],"title":"from placement to formation to spread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_c7ad10dac433edffb021","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:collective-agreement","source_type":"word_analysis","support_ids":["sup_d2fdde5094ee2fb78cd7","sup_e485c0c7da8b8de6cbec"],"title":"many cushions gathered as one array","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_511edfb07fd99298ff87","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:implicit-arranger","source_type":"word_analysis","support_ids":["sup_2a3125d9eedba136c56a","sup_e485c0c7da8b8de6cbec"],"title":"arranger withheld while order appears","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_93b7c2c864b27bb52978","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:inter-ayah-alignment-echoes","source_type":"word_analysis","support_ids":["sup_20288bda5aa1d366716b","sup_e485c0c7da8b8de6cbec"],"title":"alignment echoes from ranks and furnished scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_89215f939691fbfb6469","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:passive-result-state","source_type":"word_analysis","support_ids":["sup_71dfdab09fa9f34af4ef","sup_e485c0c7da8b8de6cbec"],"title":"already arrayed result state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_c6bafeef28a72280105c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:phrase-progression-and-closure","source_type":"word_analysis","support_ids":["sup_0e91a20d3a964165a05a","sup_e485c0c7da8b8de6cbec"],"title":"the ayah closes on ordered state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_01ad24f5e9929c776ab8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:rank-field-narrowed-to-furnishing","source_type":"word_analysis","support_ids":["sup_5640dcd113d290677925","sup_e485c0c7da8b8de6cbec"],"title":"rank field quieted into furnishing order","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_375a24a9fbf6542d5a27","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:row-alignment-root-pressure","source_type":"word_analysis","support_ids":["sup_39c39fff89df5f5a38a3","sup_e485c0c7da8b8de6cbec"],"title":"row alignment beyond mere presence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:3"],"branch_refs":[],"candidate_id":"cand_47a3fa9c993f71ef6d0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:3:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_62588f62a86ac6676d9f","sup_e485c0c7da8b8de6cbec"],"title":"compressed sound suits rowed repetition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:15:3","qac_refs":["88:15:2:1"],"status":"accepted"}},{"anchor_refs":["88:15:2"],"branch_refs":[],"candidate_id":"cand_762ab67a543d9f78a612","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000871"],"scope":"focus_ayah","source_local_id":"88:15:2:1","source_type":"qac_morpheme","support_ids":["sup_1f09ae9c9e9095058c73"],"title":"QAC root occurrence: ص ف ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000871/B001"],"candidate_id":"cand_35fdda236bc8e6e95e1f","commentary_obligation":"review","hft_ref":"hft_faf209c363d5f5164a3e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_linear_seating_order","source_type":"hft","support_ids":["sup_51fdc70e6969b0515821"],"title":"base_linear_seating_order","trust":"legacy_unbound"},{"anchor_refs":["88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000871/B001","root_000871/B004"],"candidate_id":"cand_d26efbb329c83556e5be","commentary_obligation":"review","hft_ref":"hft_f9dfc2c435142b66f3f4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_fitted_rest_interface","source_type":"hft","support_ids":["sup_1cb7537c91d559c6abab"],"title":"base_fitted_rest_interface","trust":"legacy_unbound"},{"anchor_refs":["88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000871/B001","root_000871/B007"],"candidate_id":"cand_1e0be5affd1ab279bc4f","commentary_obligation":"review","hft_ref":"hft_33841798141e44ac0efb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_convergent_gathering","source_type":"hft","support_ids":["sup_4b7a5a5dcce7a39a8b7f"],"title":"base_convergent_gathering","trust":"legacy_unbound"},{"anchor_refs":["88:15"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:15","branch_refs":["root_000871/B002"],"candidate_id":"cand_0e1529d859ecaeb2ca16","commentary_obligation":"review","hft_ref":"hft_c55d0581a7f6470f7954","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_serial_abundance","source_type":"hft","support_ids":["sup_4796e6a8ef57323c2950"],"title":"base_serial_abundance","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:15:1:1","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَمَارِق","morph_features":"STEM|POS:N|LEM:namaAriq|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:15:1:2","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"نَمَارِقُ"},{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","root_ar":"ص ف ف","surface_ar":"مَصْفُوفَةٌ"}],"word_analysis_qac_refs":[["88:15:1:1"],["88:15:1:2"],["88:15:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:15:1","88:15:2","88:15:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:15:1:1","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"نَمَارِق","morph_features":"STEM|POS:N|LEM:namaAriq|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:15:1:2","qac_word_ref":"88:15:1","root_ar":"","surface_ar":"نَمَارِقُ"},{"lemma_ar":"مَصْفُوفَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:15:2:1","qac_word_ref":"88:15:2","root_ar":"ص ف ف","surface_ar":"مَصْفُوفَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:15:1:1"],["88:15:1:2"],["88:15:2:1"]],"word_analysis_refs":["88:15:1","88:15:2","88:15:3"],"word_rows":[{"analysis_record_ref":"88:15:1","analytic_gloss_range_en":"additive coordination that carries the already established garden-inventory frame forward into another furnishing item","analytic_root_gloss_range_en":null,"qac_refs":["88:15:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:15:2","analytic_gloss_range_en":"indefinite plural cushion-supports, materially present in the garden inventory and then gathered by the following ordering adjective","analytic_root_gloss_range_en":"tight concrete object field for a small cushion, pad, bolster, or saddle-cover; the local noun selects the cushion-support branch","qac_refs":["88:15:1:2"],"root":{"arabic":"ن م ر ق","transliteration":"n-m-r-q"},"surface":{"arabic":"نَمَارِقُ","transliteration":"namāriq"}},{"analysis_record_ref":"88:15:3","analytic_gloss_range_en":"rowed or arranged as a completed collective state modifying the cushion group","analytic_root_gloss_range_en":"root range centered on lining up or arranging side by side in rows, ranks, or formations; other lexical branches exist, but the local adjective selects ordered alignment","qac_refs":["88:15:2:1"],"root":{"arabic":"ص ف ف","transliteration":"ṣ-f-f"},"surface":{"arabic":"مَصْفُوفَةٌۭ","transliteration":"maṣfūfatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:15"],"branch_refs":["root_000871/B001"],"candidate_id":"cand_35fdda236bc8e6e95e1f","evidence_scope":"focus_ayah","hft_ref":"hft_faf209c363d5f5164a3e","item_id":"base_linear_seating_order","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_linear_seating_order","support_id":"sup_51fdc70e6969b0515821"},{"anchor_refs":["88:15"],"branch_refs":["root_000871/B001","root_000871/B004"],"candidate_id":"cand_d26efbb329c83556e5be","evidence_scope":"focus_ayah","hft_ref":"hft_f9dfc2c435142b66f3f4","item_id":"base_fitted_rest_interface","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_fitted_rest_interface","support_id":"sup_1cb7537c91d559c6abab"},{"anchor_refs":["88:15"],"branch_refs":["root_000871/B001","root_000871/B007"],"candidate_id":"cand_1e0be5affd1ab279bc4f","evidence_scope":"focus_ayah","hft_ref":"hft_33841798141e44ac0efb","item_id":"base_convergent_gathering","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_convergent_gathering","support_id":"sup_4b7a5a5dcce7a39a8b7f"},{"anchor_refs":["88:15"],"branch_refs":["root_000871/B002"],"candidate_id":"cand_0e1529d859ecaeb2ca16","evidence_scope":"focus_ayah","hft_ref":"hft_c55d0581a7f6470f7954","item_id":"base_serial_abundance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_serial_abundance","support_id":"sup_4796e6a8ef57323c2950"}],"diagnostics":[],"lane_counts":{"global":14,"macro":6,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:15","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:15","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:15","lane":"micro","linguistic_source_ref":"88:15","surface_ref":"88:15","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:15","target_tokens":[["Dizilmiş",["88:15:2"]],["yastıklar",["88:15:1"]],["da",["88:15:1"]],["vardır",["88:15:1"]]],"text":"Dizilmiş yastıklar da vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:phrase-progression-and-closure","source_type":"word_analysis","support_id":"sup_0e91a20d3a964165a05a","text":"{\"blocking_evidence\":null,\"headline\":\"the ayah closes on ordered state\",\"reader_payoff\":\"The reader notices the two-word phrase moving from many cushions to one ordered state, with order as the ayah's closing perception.\",\"reason\":\"The adjective follows the cushion noun and stands at the end of the ayah, making the arranged state the final local quality.\",\"representative_source_ids\":[\"QT-03766894\",\"QT-e61c4145\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:bound-modifier-case","source_type":"word_analysis","support_id":"sup_10e91420685e34f64ea4","text":"{\"blocking_evidence\":null,\"headline\":\"orderedness bound to the head noun\",\"reader_payoff\":\"The reader notices orderedness as a quality of the cushion group, not as an independent predicate floating away from it.\",\"reason\":\"The nominative adjective follows and modifies the nominative cushion head in the local noun phrase.\",\"representative_source_ids\":[\"QG-dcb897b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:15:2:1","source_type":"qac_morpheme","support_id":"sup_1f09ae9c9e9095058c73","text":"{\"lemma_ar\":\"مَصْفُوفَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|LEM:maSofuwfap|ROOT:Sff|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"88:15:2:1\",\"qac_word_ref\":\"88:15:2\",\"root_ar\":\"ص ف ف\",\"surface_ar\":\"مَصْفُوفَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:inter-ayah-alignment-echoes","source_type":"word_analysis","support_id":"sup_20288bda5aa1d366716b","text":"{\"blocking_evidence\":null,\"headline\":\"alignment echoes from ranks and furnished scenes\",\"reader_payoff\":\"The reader notices that the same alignment field can appear in collective struggle (61:4), intensified arrival rows (89:22), and furnished paradise scenes (52:20), while 88:15 applies it quietly to cushions.\",\"reason\":\"The concrete references support an echo or contrast in the alignment field, but they do not replace the local furnishing parse in 88:15.\",\"representative_source_ids\":[\"MI-482ba5be\",\"MI-db4b79bc\",\"QE-c252f6f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:support-plus-display","source_type":"word_analysis","support_id":"sup_29ff4e9baee90a72e07e","text":"{\"blocking_evidence\":null,\"headline\":\"support object before ordered display\",\"reader_payoff\":\"The reader notices the phrase staging provision before arrangement: first many support objects, then the adjective turns them into an array.\",\"reason\":\"The head noun precedes its strongly licensed adjective, so the phrase locally moves from object to ordered state.\",\"representative_source_ids\":[\"QS-507f8beb\",\"QF-634c3402\",\"QT-bcaedd3e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:implicit-arranger","source_type":"word_analysis","support_id":"sup_2a3125d9eedba136c56a","text":"{\"blocking_evidence\":null,\"headline\":\"arranger withheld while order appears\",\"reader_payoff\":\"The reader notices prepared order without attention shifting to a named arranger or an explicit ordering verb.\",\"reason\":\"The participial surface marks the cushions as bearing the result of arrangement while the local phrase has no finite arranging verb.\",\"representative_source_ids\":[\"QG-74ea520b\",\"MG-d4f011ec\",\"QS-1bb50641\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2","source_type":"word_analysis","support_id":"sup_2f2e4d988901489a0e5d","text":"{\"gloss_range\":\"indefinite plural cushion-supports, materially present in the garden inventory and then gathered by the following ordering adjective\",\"prose\":\"{{ar:نَمَارِقُ}} ({{tr:namāriq}}) names concrete cushion-supports, so the garden's ease becomes bodily and usable rather than abstract comfort. Its indefinite broken plural opens an uncounted abundance of support objects, while the nominative case keeps them present inside the recovered garden frame rather than making them objects of a hidden action. As a one-time Quranic furnishing term, it stays close to its immediate anchors: many support objects that the following feminine singular modifier can gather as one collective set. The noun comes before {{ar:مَصْفُوفَةٌ}} ({{tr:maṣfūfatun}}), so the listener first registers many cushions and then sees that multiplicity organized into an ordered display. In the 88:13-16 sequence, the cushions fill the bodily-support slot between raised couches, placed cups, and spread carpets, and the soft furnishing word closes on qāf before the ordering adjective arrives.\",\"root_display\":\"{{ar:ن م ر ق}} ({{tr:n-m-r-q}})\",\"root_gloss_range\":\"tight concrete object field for a small cushion, pad, bolster, or saddle-cover; the local noun selects the cushion-support branch\",\"surface_display\":\"{{ar:نَمَارِقُ}} ({{tr:namāriq}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:boundary-spatial-handoff","source_type":"word_analysis","support_id":"sup_33b7ac10ede54326c3c3","text":"{\"blocking_evidence\":null,\"headline\":\"from placement to formation to spread\",\"reader_payoff\":\"The reader notices the catalog's spatial logic widening from placed cups in 88:14 to aligned cushions in 88:15 and spread carpets in 88:16.\",\"reason\":\"The adjective belongs to the same serial furnishing inventory and naturally marks the transition from individual placement to collective formation.\",\"representative_source_ids\":[\"QB-702761ba\",\"QB-7c3552db\",\"QB-bca0edfc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:uncounted-plural-abundance","source_type":"word_analysis","support_id":"sup_37b2ed15f26a92612cc2","text":"{\"blocking_evidence\":null,\"headline\":\"uncounted plural abundance\",\"reader_payoff\":\"The reader notices abundance without a measured count: many cushion units are disclosed as a class of provision.\",\"reason\":\"The noun is an indefinite plural, and V4 keeps the root in a concrete cushion-object branch rather than an abstract field.\",\"representative_source_ids\":[\"QG-75f11d09\",\"QF-349b2e1a\",\"QF-6531acab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:row-alignment-root-pressure","source_type":"word_analysis","support_id":"sup_39c39fff89df5f5a38a3","text":"{\"blocking_evidence\":null,\"headline\":\"row alignment beyond mere presence\",\"reader_payoff\":\"The reader sees the cushions not merely available for use but visibly aligned, so comfort is joined to disciplined spatial order.\",\"reason\":\"V4's accepted local root branch centers on arranging things side by side in rows, and the local adjective selects that alignment field.\",\"representative_source_ids\":[\"QS-3803256e\",\"QS-3ba5af4b\",\"MS-eea16cdd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:furnishing-sequence-slot","source_type":"word_analysis","support_id":"sup_40d3f5af23a39946faf0","text":"{\"blocking_evidence\":null,\"headline\":\"bodily support slot in the sequence\",\"reader_payoff\":\"The reader notices the cushions filling the bodily-support place between raised couches, placed cups, and spread carpets in 88:13-16.\",\"reason\":\"The local noun remains inside the same coordinated furnishing inventory and contributes a distinct support function in that sequence.\",\"representative_source_ids\":[\"QT-1384094e\",\"MT-0f280cb4\",\"QB-216f8add\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:rank-field-narrowed-to-furnishing","source_type":"word_analysis","support_id":"sup_5640dcd113d290677925","text":"{\"blocking_evidence\":null,\"headline\":\"rank field quieted into furnishing order\",\"reader_payoff\":\"The reader notices row-and-rank pressure entering a paradise-furnishing scene, while local syntax keeps it to arranged cushions rather than battle or angelic formation.\",\"reason\":\"The root field supports rows and ranks, but the local head noun is a furnishing item, so the rank pressure survives as ordered layout rather than controlling the referent.\",\"representative_source_ids\":[\"QS-26150882\",\"QS-f364a040\",\"QI-fc04ca6d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:sound-and-cadence","source_type":"word_analysis","support_id":"sup_62588f62a86ac6676d9f","text":"{\"blocking_evidence\":null,\"headline\":\"compressed sound suits rowed repetition\",\"reader_payoff\":\"The reader hears firm, repeated consonantal pressure and indefinite cadence reinforcing the sense of side-by-side ordered repetition.\",\"reason\":\"The sound rows are local to the surface form and reinforce, without replacing, the row-alignment meaning.\",\"representative_source_ids\":[\"QP-40a1403c\",\"QP-656d40cb\",\"QP-768fddbd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:1:compressed-locative-frame","source_type":"word_analysis","support_id":"sup_64abf0bd1c622f243d5d","text":"{\"blocking_evidence\":null,\"headline\":\"compressed carried locative frame\",\"reader_payoff\":\"The reader notices the ayah's compression: the garden-location frame is recoverable without being restated before the new furnishing noun.\",\"reason\":\"Attachment evidence marks an omitted locative predicate for the cushion noun, supporting a carried frame rather than a new explicit clause.\",\"representative_source_ids\":[\"QT-086bfafb\",\"QT-abb6c75d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:passive-result-state","source_type":"word_analysis","support_id":"sup_71dfdab09fa9f34af4ef","text":"{\"blocking_evidence\":null,\"headline\":\"already arrayed result state\",\"reader_payoff\":\"The reader notices arrangement as a settled quality the cushions already bear, not as a narrated act of arranging.\",\"reason\":\"The local word is a passive participial adjective, and the attachment evidence binds it to the cushion noun rather than to a finite verbal event.\",\"representative_source_ids\":[\"QG-0b529dbc\",\"QF-02ad3a8c\",\"MF-ae19a61a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:1:rhythmic-pickup","source_type":"word_analysis","support_id":"sup_85941bc070bfe582cc63","text":"{\"blocking_evidence\":null,\"headline\":\"light recited pickup into the phrase\",\"reader_payoff\":\"The reader hears the short particle as a light pickup before the longer cushion-and-order phrase.\",\"reason\":\"The one-syllable particle immediately precedes the longer two-word furnishing phrase, giving the line a small audible launch.\",\"representative_source_ids\":[\"QP-1dcd14fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:present-inventory-item","source_type":"word_analysis","support_id":"sup_86a5303b7433b9cd7c47","text":"{\"blocking_evidence\":null,\"headline\":\"nominative present furnishing\",\"reader_payoff\":\"The reader notices the cushions as already present within the garden inventory, not as objects being acted upon by an unstated verb.\",\"reason\":\"The noun is nominative and attachment evidence strongly licenses a carried locative predicate for the ongoing inventory.\",\"representative_source_ids\":[\"QG-758a946f\",\"QG-c106c64c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:tactile-support-object","source_type":"word_analysis","support_id":"sup_9f786e58954e3850c8df","text":"{\"blocking_evidence\":null,\"headline\":\"material support rather than abstract ease\",\"reader_payoff\":\"The reader notices comfort made material through objects shaped for bodily support, not merely through a general word for rest.\",\"reason\":\"V4 supplies a tight accepted branch for small cushion or padded cover, and no local evidence expands the noun into an abstract rest term.\",\"representative_source_ids\":[\"QS-6f6f8887\",\"QS-f761d4c0\",\"MS-c9d1072d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:1:serial-additive-chain","source_type":"word_analysis","support_id":"sup_a78c22bf61f9582203d0","text":"{\"blocking_evidence\":null,\"headline\":\"serial additive chain across furnishings\",\"reader_payoff\":\"The reader notices 88:14-16 as a linked furnishing sequence whose repeated additive onset accumulates the scene item by item.\",\"reason\":\"The same coordinating onset is locally consistent with the surrounding short inventory lines and does not require a discourse reset.\",\"representative_source_ids\":[\"QE-8b1522b0\",\"QB-734792f5\",\"QB-8a249641\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:sound-closure-before-order","source_type":"word_analysis","support_id":"sup_a896bdc3b4280950169a","text":"{\"blocking_evidence\":null,\"headline\":\"soft furnishing word closes firmly\",\"reader_payoff\":\"The reader hears a soft furnishing word land with a firm closure before the following adjective organizes it.\",\"reason\":\"The sound observation is local to the displayed word and aligns with the transition into the ordering adjective without changing the lexical sense.\",\"representative_source_ids\":[\"QP-cb9fb7c5\",\"MP-6eda2661\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:1","source_type":"word_analysis","support_id":"sup_b70fa5f2817459de7e02","text":"{\"gloss_range\":\"additive coordination that carries the already established garden-inventory frame forward into another furnishing item\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the cushion phrase arrive as another item in the same furnished garden inventory, not as a fresh scene. Because the phrase has no overt verb or repeated locative, the particle helps carry the catalog frame forward from the previous furnishing line while letting {{ar:نَمَارِقُ مَصْفُوفَةٌ}} ({{tr:namāriqu maṣfūfatun}}) appear immediately. Its brief recited pickup also keeps 88:14-16 moving by recurrence: placed cups, rowed cushions, then spread carpets.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3:collective-agreement","source_type":"word_analysis","support_id":"sup_d2fdde5094ee2fb78cd7","text":"{\"blocking_evidence\":null,\"headline\":\"many cushions gathered as one array\",\"reader_payoff\":\"The reader notices grammar itself gathering multiple cushions into a single collective arranged set.\",\"reason\":\"The feminine singular nominative adjective is strongly licensed as a modifier of the nonhuman plural cushion head.\",\"representative_source_ids\":[\"QG-bed7ee50\",\"MG-400adecb\",\"QF-f49b80ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:hapax-concrete-anchor","source_type":"word_analysis","support_id":"sup_d89694a9b419e95491cc","text":"{\"blocking_evidence\":null,\"headline\":\"hapax concrete furnishing term\",\"reader_payoff\":\"The reader notices that this one-time Quranic furnishing term should stay close to its immediate cushion-support anchors.\",\"reason\":\"The contextual profile marks a single exact-root form instance, and V4 constrains the root to the cushion or padded-cover object field.\",\"representative_source_ids\":[\"QH-1cf1508d\",\"MH-fcdebe8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:1:catalog-coordination","source_type":"word_analysis","support_id":"sup_dc0d815224da541aa535","text":"{\"blocking_evidence\":null,\"headline\":\"catalog coordination rather than restart\",\"reader_payoff\":\"The reader notices that the cushion phrase is added into one co-present furnished scene rather than opened as an isolated nominal display.\",\"reason\":\"The prefixed conjunction and the strongly licensed omitted locative predicate keep the line attached to the surrounding inventory.\",\"representative_source_ids\":[\"QG-5a7906d9\",\"QS-68fb75bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:3","source_type":"word_analysis","support_id":"sup_e485c0c7da8b8de6cbec","text":"{\"gloss_range\":\"rowed or arranged as a completed collective state modifying the cushion group\",\"prose\":\"{{ar:مَصْفُوفَةٌۭ}} ({{tr:maṣfūfatun}}) makes order the final perceived quality of the cushion phrase, binding orderedness to the cushion group rather than leaving it as a free predicate. As a passive participial adjective, it presents the cushions as already arrayed while withholding the arranging act and arranger. Its feminine singular agreement gathers the many {{ar:نَمَارِقُ}} ({{tr:namāriq}}) into one collective display, and the root's row-and-rank field makes the comfort disciplined rather than loose. The same alignment field can carry collective rank elsewhere (61:4), intensified rows (89:22), and a furnished paradise setting near couches (52:20), but here it quiets into prepared cushion order. Its firm repeated consonantal feel and indefinite cadence reinforce side-by-side repetition, while the catalog's spatial logic widens from placed cups in 88:14 to aligned cushions in 88:15 and spread carpets in 88:16.\",\"root_display\":\"{{ar:ص ف ف}} ({{tr:ṣ-f-f}})\",\"root_gloss_range\":\"root range centered on lining up or arranging side by side in rows, ranks, or formations; other lexical branches exist, but the local adjective selects ordered alignment\",\"surface_display\":\"{{ar:مَصْفُوفَةٌۭ}} ({{tr:maṣfūfatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:15:2:collective-modifier-licensing","source_type":"word_analysis","support_id":"sup_ffd9c79b3ba1db3eb365","text":"{\"blocking_evidence\":null,\"headline\":\"plural head handled as collective set\",\"reader_payoff\":\"The reader notices that the many cushions can be grammatically treated as one collective set by the following feminine singular modifier.\",\"reason\":\"The adjective attachment is strongly licensed, and the grammar identifies collective feminine singular agreement with a nonhuman plural head.\",\"representative_source_ids\":[\"QG-5e0743f6\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000871/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000871","role":"The straight-row image supplies the literal alignment and makes repeated cushions function as one ordered line.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"changed_reading":{"after":"The cushions have been deliberately repeated into an even, readable seating order with a place-by-place rhythm.","before":"Several decorative cushions happen to be present."},"confidence":"strong","focus_anchor":"The passive adjective on the plural cushions is anchored in ص ف ف as even-row placement.","mechanism":"Parallel repetition turns separate cushions into a legible seating line: each item remains distinct, but equal spacing makes the plurality operate as one prepared order.","model_id":"base_linear_seating_order"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_linear_seating_order","source_type":"hft","support_id":"sup_51fdc70e6969b0515821","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000871/B001","root_000871/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000871","role":"The bench-or-pad branch makes the aligned cushions an installed bodily interface rather than loose decoration.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"The row branch extends the fitted surface serially across multiple resting positions.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"changed_reading":{"after":"It describes rest as built into the environment through a continuous series of fitted supports.","before":"The verse inventories a luxury object."},"confidence":"medium","focus_anchor":"The cushions are modified by ص ف ف, whose building-and-saddle branch treats padding as a fitted structural surface.","mechanism":"The row is not only ornamental. It forms a continuous soft interface between bodies and a supporting structure, like an installed bench facing or a fitted pad.","model_id":"base_fitted_rest_interface"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_fitted_rest_interface","source_type":"hft","support_id":"sup_1cb7537c91d559c6abab","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000871/B001","root_000871/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000871","role":"The gathering-at-water branch turns alignment into infrastructure for shared access and assembly.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"The even row preserves a distinct place for each participant within the convergence.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"changed_reading":{"after":"The row is gathering infrastructure that coordinates plural access to a shared setting.","before":"The row is a purely visual pattern."},"confidence":"medium","focus_anchor":"The same focus root has a branch in which alignment is a gathering around water.","mechanism":"A row can coordinate convergence: it gives a plurality of arrivals distinct positions around a shared center without dissolving them into a crowd.","model_id":"base_convergent_gathering"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_convergent_gathering","source_type":"hft","support_id":"sup_4b7a5a5dcce7a39a8b7f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000871/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000871","role":"The multiple-vessel camel image supplies abundance distributed across parallel receivers and a stabilizing aligned posture.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"changed_reading":{"after":"Multiplicity becomes serial capacity: a common abundance has been converted into many ready receptacles for rest.","before":"Multiplicity means only that there are many cushions."},"confidence":"exploratory","focus_anchor":"A form-distant ص ف ف branch links ordered posture with one camel filling several vessels.","mechanism":"The branch activates a distributive image: one abundant provision is received through several parallel receptacles. By analogy, the cushion row multiplies a single condition of rest into many available places.","model_id":"base_serial_abundance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_serial_abundance","source_type":"hft","support_id":"sup_4796e6a8ef57323c2950","trust":"legacy_unbound"}]}
</lane_packet_json>
