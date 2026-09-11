# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **108:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s108-regular-20260911/s108/108_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "108:1",
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
{"analysis_context":{"analysis_id":"s108-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"108:1","host_surah":108,"lane_context_refs":[],"ordered_context_refs":["108:0","108:2","108:3","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal verme, birinden isteme veya birinin işini görme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"elle uzanıp alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneye elle uzanıp onu alma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ceylanın yapraklara erişmek için ön ayaklarını kaldırıp ağaca uzanmasını anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin el ile erişilip alındığı temel kullanım için uygundur.","boundary_detail":"Bu dal verme, birinden isteme veya birinin işini görme anlamlarını kapsamaz.","branch_image_ar":"الأخذ والتناول باليد","concept_gloss":"elle uzanıp alma","contextual_glosses":[{"applicability":"Ceylanın ön ayaklarını kaldırarak ağaç yapraklarına uzandığı betimleme için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yükselme amacını ve yaprağa doğru uzanmasını korur."},"facet_ids":["F002"],"text":"yapraklara erişmek için uzanma","usage_role":"contextual"}],"definition":"Temel anlam, bir nesneye elle uzanıp onu almaktır. Hayvanı anlatan özel kullanımda ceylan, ağacın yapraklarına erişmek için ön ayaklarını kaldırıp uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneye elle uzanıp onu alma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Ceylanın yapraklara erişmek için ön ayaklarını kaldırıp ağaca uzanmasını anlatır."}],"identity_rationale":"Kaynak anlatımı, temel olarak bir şeyi elle almayı; özel hayvan betimlemesinde ise ceylanın ağacın yapraklarına erişmek için ön ayaklarını kaldırmasını bildirir. Bu iki kullanım, alma ve erişmek için uzanma odağında tutarlı biçimde birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"elle alma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi elle alma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yapraklara erişmek için ön ayaklarını kaldıran ceylan"}],"lexicalization_note":"Tanım, elle alma çekirdeğini hayvanı anlatan özel kalıptan ayırır; ceylan betimlemesi bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan dört ilişki elle alma sınırını en açık biçimde gösterir, öteki adaylar yalnızca uzak konu ortaklığı taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda erişip alma belirleyiciyken komşu dalda avucu kapatıp nesneyi bütünüyle kavrama belirleyicidir.","focus_only":"Erişmek için elle uzanmayı ve ceylanın yaprağa uzanmasını da kapsar.","gloss":"elle uzanma ile avuçlayarak alma","neighbor_only":"Nesneyi bütün avuçla kavrama ve avuçta tutma biçimini öne çıkarır.","neighbor_ref":"root_001197/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir nesneyi el kullanarak almayı anlatır."},{"boundary_match":"partial","distinction":"Odak dal elle uzanıp almaya bağlıdır; komşu dal ise elde bulundurma, toplama ve daha geniş alma kullanımlarını içerir.","focus_only":"Elle uzanma biçimini ve yaprağa uzanan ceylan betimlemesini taşır.","gloss":"elle alma ile genel alıp edinme","neighbor_only":"Alınanı elde bulundurma, toplama ve söz gibi soyut nesneleri alma alanına da uzanır.","neighbor_ref":"root_000018/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi alma ve ona erişme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalın sınırı elle alma üzerindedir; komşu dal uzaklıktan erişme, güçlü tutma ve soyut kullanımlara kadar genişler.","focus_only":"Elle alma çekirdeği yanında ceylanın ön ayaklarını kaldırdığı özel betimlemeyi içerir.","gloss":"elle alma ile uzaktan erişip tutma","neighbor_only":"Uzak bir şeye erişmeyi, soyut uzanımları ve baştan ya da sakaldan tutmayı da kapsar.","neighbor_ref":"root_001565/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da uzanarak bir şeye erişme ve onu alma vardır."},{"boundary_match":"partial","distinction":"Odak dal hareketi alan kişinin yönünden kurar; komşu dal veren kişinin nesneyi başkasına geçirmesini ve ortaya çıkan verilmiş şeyi anlatır.","focus_only":"Nesneyi alan kişinin elle erişip kendine doğru almasını anlatır.","gloss":"alma ile verme yönleri","neighbor_only":"Nesneyi başkasına verme, elden uzatma ve verilen şeyi adlandırma yönünü taşır.","neighbor_ref":"root_001028/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin el aracılığıyla yer değiştirmesine ilişkindir."}],"source_phrase_ar":"العطو التناول باليد (maqayis;ayn;tahdhib)؛ عطوت الشيء تناولته باليد (sihah)؛ الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق (ayn)؛ الظباء تتطالل إذا رفعت أيديها لتتناول ورق الشجر (tahdhib)","source_summary":"Kaynaklar elle alma çekirdeğinde birleşir ve ceylanın yaprağa erişmek için ön ayaklarını kaldırmasını bu çekirdeğin özel bir görünümü olarak verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه التناول باليد ورفع اليدين إلى الورق وتناول الشيء","what_is_not_ar":"ليس الإعطاء ولا اسم العطية ولا طلبها ولا خدمة الإنسان لغيره"},"support_links":[]},{"boundary":"Dal, alma yönünü veya verme isteğini değil, veren yönündeki aktarımı ve verilen şeyi kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B002","candidate_links":[{"candidate_id":"cand_7338a33768b1a5f7fba1","lane":"micro"},{"candidate_id":"cand_0427a50dab18afbdf9d0","lane":"micro"},{"candidate_id":"cand_23ef5df9ade66d1b1480","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"verme, karşılıklı elden geçirme ve verilen şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi başkasına verme veya elden uzatma eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir nesnenin iki kişi arasında karşılıklı olarak el değiştirmesini anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Verilen nesnenin kendisini ve bunun tekil ya da çoğul adlandırılışını gösterir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İki kişinin bir kılıcı birbirine verip bir süre sırayla tutması veya sallaması karşılıklı el değiştirmeye örnektir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın eylem, karşılıklı aktarım ve aktarılmış nesne katmanlarını birlikte göstermek için uygundur.","boundary_detail":"Dal, alma yönünü veya verme isteğini değil, veren yönündeki aktarımı ve verilen şeyi kapsar.","branch_image_ar":"المناولة والإعطاء","concept_gloss":"verme, karşılıklı elden geçirme ve verilen şey","contextual_glosses":[{"applicability":"Bir nesnenin veren kişiden başka bir kişiye geçirildiği düz kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vereni, verilen nesneyi ve alıcıya doğru aktarımı korur."},"facet_ids":["F001"],"text":"bir şeyi başkasına vermek","usage_role":"general"},{"applicability":"Aynı nesnenin iki kişi arasında el değiştirerek sırayla kullanıldığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı vermeyi ve nesnenin sırayla kullanılmasını korur."},"facet_ids":["F002","F004"],"text":"sırayla birbirine vermek","usage_role":"contextual"},{"applicability":"Eylemin kendisi değil, birine verilmiş nesne adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Verme sonunda alıcıya geçen nesne sonucunu açıkça korur."},"facet_ids":["F003"],"text":"verilen şey","usage_role":"contextual"}],"definition":"Bir şeyi başkasına verme veya elden uzatma; karşılıklı kullanımda aynı şeyi iki kişinin birbirine vermesi veya elden geçirmesidir. Adlaşmış kullanım ise verilen şeyi ve onun birden çok oluşunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi başkasına verme veya elden uzatma eylemidir."},{"facet_id":"F002","role":"extension","statement":"Bir nesnenin iki kişi arasında karşılıklı olarak el değiştirmesini anlatır."},{"facet_id":"F003","role":"extension","statement":"Verilen nesnenin kendisini ve bunun tekil ya da çoğul adlandırılışını gösterir."},{"facet_id":"F004","role":"example","statement":"İki kişinin bir kılıcı birbirine verip bir süre sırayla tutması veya sallaması karşılıklı el değiştirmeye örnektir."}],"identity_rationale":"Kaynak anlatımı bir şeyi başkasına verme ve elden uzatma eylemini, iki kişi arasındaki karşılıklı el değiştirmeyi ve verilen şeyin adını birlikte bildirir. Kılıcın sırayla elde tutulması, karşılıklı el değiştirme yönünü açıklayan özel bir örnektir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"verme, elden uzatma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı elden verme veya el değiştirme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kılıcı sırayla birbirine verip elde tutma veya sallama"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"verilen şey"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birine verilen şey"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"birine verilen şeyler"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"verilen şeylerin çoğul adı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çok veren kimse"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"malı ne çok veriyor!"}],"lexicalization_note":"Tanım, verme çekirdeğini karşılıklı el değiştirme, verilen şeyin adı ve özel söyleyişlerden ayrı katmanlar halinde tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş karşılaştırma verme dalını alma, isteme, getirme, iyeliğe geçirme ve isteyene karşılık verme sınırlarında açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aktarımı veren kişinin yönünden kurar; komşu dal nesneye erişip onu alan kişinin yönünden kurar.","focus_only":"Nesneyi veren kişiden alıcıya geçirme ve verilen şeyi adlandırma yönünü taşır.","gloss":"verme ile alma yönleri","neighbor_only":"Nesneye elle erişip onu alan kişinin yönünü ve ceylanın uzanışını taşır.","neighbor_ref":"root_001028/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin el aracılığıyla yer değiştirmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalda nesne verenden alıcıya geçer; komşu dalda isteyen kişi böyle bir geçişin yapılmasını başkalarından ister.","focus_only":"Bir şeyi gerçekten verme, elden uzatma ve verilen nesneyi adlandırma vardır.","gloss":"verme ile verilmesini isteme","neighbor_only":"Henüz verilmemiş bir şeyi başkalarından isteme eylemi vardır.","neighbor_ref":"root_001028/B005","relation_type":"same_field","shared_zone":"İki dal aynı olası aktarımın veren ve isteyen taraflarıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal karşılıklı elden geçirme ve verilen nesneye kadar genişler; komşu dal ise verme yanında getirip hazır etme yönünü taşır.","focus_only":"Karşılıklı el değiştirmeyi ve verilen nesnenin adını ayrıca kapsar.","gloss":"verme ile getirip verme","neighbor_only":"Bir şeyi başka bir şeyle birlikte getirme veya hazır etme yönüne de uzanır.","neighbor_ref":"root_000009/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği bir şeyi başkasına vermektir."},{"boundary_match":"partial","distinction":"Odak dalda elden uzatma yeterli olabilir; komşu dalda verme, alıcının o varlık üzerinde iyelik kazanmasıyla sınırlandırılır.","focus_only":"Elden uzatma, karşılıklı geçirme ve yalnızca verilen şeyi adlandırma kullanımlarını kapsar.","gloss":"verme ile iyeliğe geçirme","neighbor_only":"Verilen malın alıcının iyeliğine geçirilmesini belirgin bir koşul olarak taşır.","neighbor_ref":"root_000448/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın başkasına verilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal alıcının önceden istemesini gerektirmez; komşu dal ise vermeyi açıkça bir isteyen kişiye yöneltir.","focus_only":"İstek bulunmadan yapılan vermeyi, karşılıklı geçirmeyi ve verilen nesneyi de kapsar.","gloss":"genel verme ile isteyene verme","neighbor_only":"Verme eylemini, kendisinden bir şey isteyen kişiye karşılık verme durumuna bağlar.","neighbor_ref":"root_001403/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye bir nesne vermeyi anlatır."}],"source_phrase_ar":"منه اشتق الإعطاء والمعاطاة المناولة والعطاء اسم لما يعطى وهي العطية (maqayis)؛ العطاء اسم لما يعطى وأعطية وأعطيات (ayn)؛ أعطاه مالا يعطيه إعطاء والاسم العطاء والعطية الشيء المعطى (sihah)؛ الإعطاء مأخوذ من هذا والمعاطاة المناولة والعطاء اسم لما يعطى (tahdhib)؛ المعاطاة أن يستقبل رجل رجلا ومعه سيف فيقول أرني سيفك فيعطيه فيهزه هذا ساعة وهذا ساعة (tahdhib)","source_summary":"Kaynaklar verme, elden uzatma ve verilen şey anlamlarını birlikte destekler; karşılıklı verme, bir kılıcın iki kişi arasında sırayla kullanılmasıyla örneklenir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الإعطاء والمناولة والمعاطاة والعطاء والعطية والشيء المعطى وجمعه","what_is_not_ar":"ليس مجرد تناول الشيء لنفسه ولا طلب العطاء من الناس"},"support_links":["sup_876e7255b1214818ae98","sup_961914d8688ce357ed7c","sup_cd12a1b3acdc8e6a1985"]},{"boundary":"Dal genel vermeyi değil, belirli bir kişinin işini görme ve ona bakma ilişkisini anlatır.","branch_kind":"non_bare","branch_ref":"root_001028/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"birinin işini görüp istediğini uzatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasının işini görme ve bakımını üstlenme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bakılan kişinin istediği nesneleri ona uzatmak, işini görmenin bir parçasıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir çocuğun yakınları için çalışıp onların istediklerini uzatması bu kullanımı örnekler."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye bakma ile onun istediği nesneleri uzatmanın birlikte anlatıldığı kullanım için uygundur.","boundary_detail":"Dal genel vermeyi değil, belirli bir kişinin işini görme ve ona bakma ilişkisini anlatır.","branch_image_ar":"الخدمة والمناولة للأهل","concept_gloss":"birinin işini görüp istediğini uzatma","contextual_glosses":[{"applicability":"Bir çocuğun kendi yakınları için çalışıp onların gereksinimlerini karşıladığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çocuğun yakınları adına çalışmasını ve işlerini görmesini korur."},"facet_ids":["F001","F003"],"text":"yakınlarının işini görmek","usage_role":"contextual"}],"definition":"Bir kişinin işini görmek, bakımını üstlenmek ve istediği şeyleri ona uzatmaktır; çocukla ilgili özel kullanımda bu işler kendi yakınları için yapılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasının işini görme ve bakımını üstlenme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Bakılan kişinin istediği nesneleri ona uzatmak, işini görmenin bir parçasıdır."},{"facet_id":"F003","role":"example","statement":"Bir çocuğun yakınları için çalışıp onların istediklerini uzatması bu kullanımı örnekler."}],"identity_rationale":"Kaynak anlatımı bir kişinin, özellikle bir çocuğun, yakınlarının işini görmesini, istediklerini onlara uzatmasını ve genel olarak bir başkasının bakımını üstlenmesini bildirir. Verme bu dalda bağımsız amaç değil, birinin işini görmenin parçasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çocuğun yakınlarının işini görüp istediklerini uzatması"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"onun işini görüp bakımını üstlenme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"işimi görüyor"}],"lexicalization_note":"Anlam yalnızca belirtilen kişi ve yapı bağı içinde verilir; kökün yalın anlamına ya da bütün verme kullanımlarına yayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen dört ilişki iş görme çekirdeğini verme, iş gören kişi, hasta bakımı ve yol yardımı alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda uzatma, kişinin işini görme ilişkisinin bir parçasıdır; komşu dalda nesnenin verilmesi başlı başına çekirdektir.","focus_only":"Bir kişinin işini sürekli görme ve istediğini ona uzatma ilişkisini taşır.","gloss":"işini görme ile nesne verme","neighbor_only":"Bir nesneyi başkasına aktarma ve verilmiş nesneyi adlandırma çekirdeğini taşır.","neighbor_ref":"root_001028/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir kişiye istediği bir nesnenin uzatılması bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal yapılan işi anlatır; komşu dal ise bu işi yapan yardımcıları ve kimi yakınlık kümelerini adlandırır.","focus_only":"Birinin işini görme eylemini ve istediği nesneyi ona uzatmayı bildirir.","gloss":"iş görme ile iş gören kişiler","neighbor_only":"Yardımcı ya da iş gören kişileri, yakınlık bağlarıyla birlikte bir insan kümesi olarak adlandırır.","neighbor_ref":"root_000340/B002","relation_type":"near_neighbor","shared_zone":"İki dal da başkası için çalışma ve onun gereksinimini karşılama alanındadır."},{"boundary_match":"partial","distinction":"Odak dal genel bir iş görme ilişkisidir; komşu dal hastanın bakımına ve iyileşmesine yönelik daha dar bir alandır.","focus_only":"Sağlık koşulu aramadan bir kişinin işini görmeyi ve istediğini uzatmayı kapsar.","gloss":"genel iş görme ile hasta bakımı","neighbor_only":"Bakımı yalnızca hastalık durumuna ve hastayı iyileştirmeye yönelik gözetmeye bağlar.","neighbor_ref":"root_001415/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da başka bir kişinin gereksinimleriyle ilgilenme vardır."},{"boundary_match":"field_only","distinction":"Odak dal kişiye yönelik genel iş görmedir; komşu dal yalnızca yolculuk ve binek gereksinimi çevresinde kurulur.","focus_only":"Bir kişinin gündelik işini görme ve istediği nesneyi ona uzatma ilişkisini anlatır.","gloss":"iş görme ile yol yardımı","neighbor_only":"Yolculuğa yardım etme, binek sağlama veya yol yardımı isteme durumuna bağlıdır.","neighbor_ref":"root_000551/B008","relation_type":"same_field","shared_zone":"İki dal da bir başkasının gereksinimini karşılayarak ona destek olmayı içerir."}],"source_phrase_ar":"عاطى الصبي أهله إذا عمل وناول ما أرادوا (maqayis)؛ هو يعطيني ويعاطيني إذا كان يخدمك (sihah)؛ عطيته وعاطيته أي خدمته وقمت بأمره ومن يعطيك أي من يتولى خدمتك (tahdhib)","source_summary":"Kaynaklar birinin işini görme ve bakımını üstlenme çekirdeğinde birleşir; çocuğun yakınları için çalışıp istediklerini uzatması bu çekirdeği somutlaştırır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه خدمة الإنسان والقيام بأمره ومناولته ما يريد","what_is_not_ar":"ليس العطاء العام ولا طلب العطاء ولا مجرد تناول الشيء باليد"},"support_links":[]},{"boundary":"Dal olağan nesne verme veya alma değil, sınırı aşan ya da gözü pek bir işe el atma üzerindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"hakkı olmadan el uzatma ve gözü pekçe işe girişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hakkı olmayan veya alınması uygun görülmeyen bir şeye el uzatmayı anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işe girip onunla uğraşmayı, özellikle yüksek ya da çirkin görülen işlere yönelmeyi anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözü pekçe eyleme geçip amaçlanan işi sonuna vardırmayı bildirir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yeterli aracı, dayanağı veya erişme olanağı olmadan gücünü aşan bir işe kalkışmayı anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uygunsuz alma ile sınırı aşan bir işe gözü pekçe kalkışma yönlerini birlikte anlatmak için uygundur.","boundary_detail":"Dal olağan nesne verme veya alma değil, sınırı aşan ya da gözü pek bir işe el atma üzerindedir.","branch_image_ar":"التعاطي والخوض فيما يبلغه","concept_gloss":"hakkı olmadan el uzatma ve gözü pekçe işe girişme","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işe yönelip onu yapmaya başladığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşe yönelmeyi, başlamayı ve onunla etkin biçimde uğraşmayı korur."},"facet_ids":["F002"],"text":"bir işe girip onunla uğraşmak","usage_role":"general"},{"applicability":"Yeterli araç, dayanak veya bilgi olmadan erişilmez görülen bir işe yönelme için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araçsızlığı, dayanaksızlığı ve erişilmez işe kalkışmayı korur."},"facet_ids":["F004"],"text":"dayanaksızca gücünü aşan işe kalkışmak","usage_role":"explanatory"}],"definition":"Bir kimsenin hakkı olmayan ya da el atması uygun görülmeyen bir şeye uzanması ve bir işe gözü pek biçimde girişmesidir. Kimi kullanımlarda yeterli araç veya dayanak olmadan yüksek ya da erişilmez bir işe kalkışmayı ve girişilen eylemi sonuna vardırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hakkı olmayan veya alınması uygun görülmeyen bir şeye el uzatmayı anlatır."},{"facet_id":"F002","role":"extension","statement":"Bir işe girip onunla uğraşmayı, özellikle yüksek ya da çirkin görülen işlere yönelmeyi anlatır."},{"facet_id":"F003","role":"specialization","statement":"Gözü pekçe eyleme geçip amaçlanan işi sonuna vardırmayı bildirir."},{"facet_id":"F004","role":"specialization","statement":"Yeterli aracı, dayanağı veya erişme olanağı olmadan gücünü aşan bir işe kalkışmayı anlatır."}],"identity_rationale":"Kaynak anlatımı, hakkı olmayan veya yapılması uygun görülmeyen bir şeye el uzatmayı; bir işe girip onunla uğraşmayı; yüksek, çirkin ya da erişilmez bir işe gözü pek biçimde kalkışmayı birlikte verir. Eylemi sonuna vardırma ve araçsız kalkışma, bu girişme çekirdeğinin ayrı görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hakkı olmayan veya alınması uygun görülmeyen şeye el uzatma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir işe girip onunla uğraşma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"gözü pekçe eyleme girişip deveyi yaralama"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aracı, dayanağı veya yeterliği olmadan erişilmez işe kalkışma"}],"lexicalization_note":"Tanım, genel el atma yönünü belirli yapılardaki uygunsuz alma, gözü pek girişme ve araçsız kalkışma görünümlerinden ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen beş ilişki dalı gerçek alma, nötr işe girme, düşünmeden atılma, yaklaşma ve çekişmede yenme alanlarından ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bu görüntüyü uygunsuz veya gözü pek bir girişime taşır; komşu dal ise gerçek bir nesnenin elle alınmasını anlatır.","focus_only":"Hakkı aşma, uygunsuzluk veya gözü pek biçimde bir işe girişme yönünü taşır.","gloss":"işe el atma ile elle alma","neighbor_only":"Bir nesneye elle erişip onu alma ve ceylanın yaprağa uzanmasıyla sınırlıdır.","neighbor_ref":"root_001028/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeye uzanıp onu ele alma görüntüsü bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla uygunsuzluk, hak aşımı veya gözü peklik bildirir; komşu dal nötr biçimde işe girmeyi anlatır.","focus_only":"Haksız veya uygunsuz şeye uzanma, gözü peklik ve araçsız kalkışma sınırlarını taşır.","gloss":"sınır aşan girişme ile işe başlama","neighbor_only":"Bir işe girme ve onunla uğraşmayı değer yargısı ya da gözü peklik koşulu olmadan anlatır.","neighbor_ref":"root_000789/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işe girme ve onunla uğraşmaya başlama alanındadır."},{"boundary_match":"partial","distinction":"Odak dal hak aşımı ve yetersiz araçla kalkışmayı öne çıkarır; komşu dal korkutucu duruma düşünmeden atılmayı öne çıkarır.","focus_only":"Hakkı olmayan şeye uzanmayı, yüksek işe araçsız kalkışmayı ve sonuca varmayı da kapsar.","gloss":"gözü pek girişme ile düşünmeden atılma","neighbor_only":"Korkutucu veya çetin bir duruma düşünmeden atılmayı ve başkasını da oraya sokmayı kapsar.","neighbor_ref":"root_001202/B001","relation_type":"near_synonym","shared_zone":"İki dal da güç veya tehlike taşıyan bir işe çekinmeden girme yönünü paylaşır."},{"boundary_match":"partial","distinction":"Odak dal etkin bir girişim ve uğraş gerektirir; komşu dal yalnız yaklaşma veya sınırda bulunmayla gerçekleşebilir.","focus_only":"Bir işi üstlenip etkin biçimde girişmeyi ve kimi zaman onu sonuna vardırmayı anlatır.","gloss":"işe girişme ile sınırına yaklaşma","neighbor_only":"Bir şeye yaklaşma, onun sınırına gelme ve yasaklanan şeye yakın durma alanını taşır.","neighbor_ref":"root_001212/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin bir şeyle yakın ilişkiye girmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal girişimin kendisini ve sınırlarını anlatır; komşu dal karşılıklı uğraşın yalnızca üstün gelme sonucunu anlatır.","focus_only":"Uygunsuz şeye el uzatma ve tek başına bir işe gözü pekçe girişme yönünü taşır.","gloss":"işe girişme ile çekişmede yenme","neighbor_only":"Karşılıklı çekişmenin sonunda öteki kişiyi yenme sonucuna bağlıdır.","neighbor_ref":"root_001028/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişinin etkin bir uğraşa girmesini gerektiren bir olay alanındadır."}],"source_phrase_ar":"التعاطي تناول ما ليس له بحق ويتعاطى ظلم فلان وفتعاطى فعقر وعاط بغير أنواط (maqayis)؛ تعاطاه تناوله وفلان يتعاطى كذا أي يخوض فيه وفتعاطى فعقر (sihah)؛ التعاطي تناول ما لا يجوز تناوله وفتعاطى الشقي عقر الناقة فبلغ ما أراد وتعاطيه جرأته ويتعاطى معالي الأمور ورفيعها ويتعاطى أمرا قبيحا (tahdhib)","source_summary":"Kaynaklar uygunsuz bir şeye el uzatma ile bir işe girip uğraşma yönlerini bir arada verir; gözü pekçe sonuca gitme ve araçsız biçimde erişilmez işe kalkışma bu alanın özel görünümleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه تعاطي ما لا حق له به أو ما لا يجوز والخوض في الأمر والتطلع إلى الرفيع بلا آلة وبلوغ الفعل بجرأة","what_is_not_ar":"ليس المناولة المشروعة ولا العطاء ولا طلب العطاء"},"support_links":[]},{"boundary":"Dal veren kişiyi değil, başkalarından kendisine bir şey verilmesini isteyen kişiyi odaklar.","branch_kind":"bare","branch_ref":"root_001028/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"insanlardan bir şey isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başkalarından kendisine bir şey vermelerini isteme eylemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İsteyen kişinin avucunu insanlara doğru uzatması bu isteğe eşlik edebilir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin başkalarından kendisine bir şey vermelerini istediği temel kullanım için uygundur.","boundary_detail":"Dal veren kişiyi değil, başkalarından kendisine bir şey verilmesini isteyen kişiyi odaklar.","branch_image_ar":"استعطاء الناس","concept_gloss":"insanlardan bir şey isteme","contextual_glosses":[{"applicability":"İsteğin avuç uzatma hareketiyle birlikte açıkça gösterildiği bağlam için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şey istemeyi ve buna eşlik eden avuç uzatma hareketini korur."},"facet_ids":["F001","F002"],"text":"el açıp istemek","usage_role":"contextual"}],"definition":"İnsanlardan kendisine bir şey verilmesini istemektir. Bu istek, avuç uzatma hareketiyle açıkça gösterilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başkalarından kendisine bir şey vermelerini isteme eylemidir."},{"facet_id":"F002","role":"associated_use","statement":"İsteyen kişinin avucunu insanlara doğru uzatması bu isteğe eşlik edebilir."}],"identity_rationale":"Kaynak anlatımı, insanlardan bir şey verilmesini istemeyi açıkça bildirir ve bu isteğin avuç uzatılarak gösterilebildiğini ekler. Eylemin çekirdeği istemektir; verme eylemi veya verilen nesne bu dalın kendisi değildir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir şey verilmesini isteme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şey verilmesini isteme"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"insanlardan bir şey isteme"}],"lexicalization_note":"Tanım yalnızca başkalarından bir şey isteme çekirdeğini verir ve bunu el uzatma örneğine ya da başka bir yapıya bağımlı kılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen beş ilişki yalın istemeyi el hareketi, boyun bükme, bağış, diretme ve gerçekleşmiş verme sınırlarında açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği istemektir ve el hareketi zorunlu değildir; komşu dal doğrudan avucu uzatma görünümüne bağlıdır.","focus_only":"İsteğin el hareketi olmadan sözle veya başka yolla bildirilmesini de kapsar.","gloss":"genel isteme ile avuç uzatma","neighbor_only":"Avucun insanlara doğru uzatılmasını eylemin belirleyici görünümü yapar.","neighbor_ref":"root_001308/B009","relation_type":"near_synonym","shared_zone":"İki dal da insanlardan bir şey isterken el açma durumunu kapsar."},{"boundary_match":"partial","distinction":"Odak dal yalın istemedir; komşu dal bu isteğe boyun bükme, başkasının fazlasını arama ve verileni kabul etme yönlerini ekler.","focus_only":"Başkasından verilmesini istemeyi boyun bükme veya verilenle yetinme koşulu olmadan anlatır.","gloss":"isteme ile boyun bükerek isteme","neighbor_only":"İsterken boyun bükmeyi, başkasının fazlasını aramayı ve verileni kabul etmeyi de kapsar.","neighbor_ref":"root_001263/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak çekirdeği başkasından bir şey istemektir."},{"boundary_match":"partial","distinction":"Odak dal isteme eylemiyle sınırlıdır; komşu dal bağışın kabul edilmesini ve karşılıklı verilmesini de aynı alana katar.","focus_only":"İstenen şeyin bağış niteliğinde olmasını zorunlu kılmadan insanlardan verilmesini istemeyi anlatır.","gloss":"genel isteme ile bağış isteme","neighbor_only":"Bağış istemenin yanında bağışı kabul etmeyi ve kişilerin birbirine bağış vermesini de kapsar.","neighbor_ref":"root_001685/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiden karşılıksız bir şey verilmesini istemeyi kapsayabilir."},{"boundary_match":"partial","distinction":"Odak dal ısrar gerektirmez; komşu dal isteğin yinelenmesini ve istenen kişiyi bunaltacak ölçüde sürdürülmesini gerektirir.","focus_only":"İsteğin bir kez ve ısrar göstermeden yapılabildiği nötr alanı kapsar.","gloss":"isteme ile diretici isteme","neighbor_only":"İsteği yineleyip karşı tarafı bunaltacak ölçüde diretme koşulunu taşır.","neighbor_ref":"root_001346/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiden bir şey isteme eylemini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalda aktarım istenir ama gerçekleşmiş olmak zorunda değildir; komşu dalda verme veya elden geçirme gerçekleşir.","focus_only":"İsteyen kişinin henüz gerçekleşmemiş bir verme eylemini başkasından beklemesini anlatır.","gloss":"isteme ile verme","neighbor_only":"Veren kişinin nesneyi gerçekten aktarmasını ve aktarılmış nesnenin kendisini anlatır.","neighbor_ref":"root_001028/B002","relation_type":"same_field","shared_zone":"İki dal aynı olası aktarımın isteyen ve veren yönleriyle ilgilidir."}],"source_phrase_ar":"استعطى وتعطى سأل العطاء (sihah)؛ يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم (tahdhib)","source_summary":"Kaynaklar başkalarından bir şey verilmesini isteme çekirdeğinde birleşir; avuç uzatma, bu isteği dışa vuran eşlikçi hareket olarak belirtilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه سؤال العطاء وطلبه من الناس","what_is_not_ar":"ليس نفس الإعطاء ولا العطية المعطاة ولا خدمة المعطي"},"support_links":[]},{"boundary":"Dal verme anlamına değil, canlıdaki dirençsizlik ile nesnedeki kolay bükülme ortaklığına dayanır.","branch_kind":"mixed_non_bare","branch_ref":"root_001028/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"direnmeden uyma ve kolay bükülme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin direnmeyip kendisini yönlendiren kişiye uymasını anlatır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yayın sert ve direngen olmayıp kolayca bükülmesini ve gerilmesini anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bineğin yönlendirmeye uyarak başını biniciye doğru çevirmesini bildirir."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıdaki yönlendirmeye uyma ile nesnedeki kolay bükülme katmanlarını birlikte göstermek için uygundur.","boundary_detail":"Dal verme anlamına değil, canlıdaki dirençsizlik ile nesnedeki kolay bükülme ortaklığına dayanır.","branch_image_ar":"اللين والانقياد والمطاوعة","concept_gloss":"direnmeden uyma ve kolay bükülme","contextual_glosses":[{"applicability":"Deve veya bineğin kendisini yönlendiren kişiye karşı koymadığı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının direnmemesini ve yönlendiren kişiye uymasını korur."},"facet_ids":["F001","F003"],"text":"direnmeyip yönlendirmeye uyma","usage_role":"contextual"},{"applicability":"Yayın sertçe karşı koymadan kolayca bükülüp gerildiği kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yayın yumuşaklığını, kolay bükülmesini ve gerilmeye karşı koymamasını korur."},"facet_ids":["F002"],"text":"kolay bükülen yay","usage_role":"contextual"}],"definition":"Canlı varlıkta direnmeyip yönlendirmeye uymayı, nesnede ise sertçe karşı koymadan kolayca bükülmeyi anlatır. Deve veya binek başını biniciye çevirir; yay da kolay gerilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin direnmeyip kendisini yönlendiren kişiye uymasını anlatır."},{"facet_id":"F002","role":"core","statement":"Yayın sert ve direngen olmayıp kolayca bükülmesini ve gerilmesini anlatır."},{"facet_id":"F003","role":"specialization","statement":"Bineğin yönlendirmeye uyarak başını biniciye doğru çevirmesini bildirir."}],"identity_rationale":"Kaynak anlatımı canlı varlıkta direnmeyip yönlendirmeye uymayı, yayda ise sertçe karşı koymadan kolay bükülmeyi bildirir. Bineğin başını biniciye çevirmesi, canlıdaki uyma yönünün somut sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"devenin direnmeyip yönlendirmeye uyması"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kolay bükülen yumuşak yay"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gerilirken direnmeyen yumuşak yay"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"boyun eğip başını biniciye çevir"}],"lexicalization_note":"Tanım, deve ve binek için yönlendirmeye uymayı yay için kolay bükülmeden ayırır; bu özel kullanımlar yalın verme anlamına taşınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; seçilen beş ilişki canlıdaki uyma ile nesnedeki bükülmeyi genel boyun eğme, çeviklik, yumuşaklık, eğme ve yumuşak davranıştan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve ve binekteki uyumu nesnedeki bükülmeyle bağlar; komşu dal insanı da kapsayan daha genel bir boyun eğme alanına yayılır.","focus_only":"Yayın kolay bükülmesini ve bineğin başını biniciye çevirmesini de kapsar.","gloss":"direnmeden uyma ile boyun eğme","neighbor_only":"İnsanların boyun eğmesini, alçak gönüllü uyumu ve buyruğa hızlı karşılık vermeyi de kapsar.","neighbor_ref":"root_000514/B001","relation_type":"near_synonym","shared_zone":"İki dal da canlı varlığın direnmeyip yönlendirmeye uymasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal direnç göstermeme ve bükülme üzerindedir; komşu dal buna hareket hafifliği ve adımların çevik aktarımını ekler.","focus_only":"Yayın bükülmesini ve bineğin başını sürücüye çevirmesini kapsar.","gloss":"uyma ile çevikçe izleme","neighbor_only":"İnsan veya atta hızlı izlemeyi, hafif bacakları ve düzgün adım aktarımını kapsar.","neighbor_ref":"root_001694/B005","relation_type":"near_synonym","shared_zone":"Her iki dal canlıda yumuşaklık ve yönlendirmeyi kolayca izleme yönünü paylaşır."},{"boundary_match":"partial","distinction":"Odak dal yumuşaklığı yaydaki bükülme ve canlıdaki uyma üzerinden belirler; komşu dal her türlü şeydeki genel yumuşaklıktır.","focus_only":"Canlının yönlendirmeye uymasını ve yayın gerilirken karşı koymamasını birlikte kapsar.","gloss":"kolay bükülme ile genel yumuşaklık","neighbor_only":"Yumuşaklığı belirli bir canlıya, nesneye veya yönlendirme ilişkisine bağlamadan geneller.","neighbor_ref":"root_001403/B008","relation_type":"near_neighbor","shared_zone":"İki dal da nesnede sertliğin karşıtı olan yumuşaklık yönünü taşır."},{"boundary_match":"partial","distinction":"Odak dal kolay bükülmeyi nesnenin niteliği olarak verir; komşu dal o şeyi koparmadan eğme eylemini öne çıkarır.","focus_only":"Canlıdaki yönlendirmeye uymayı ve yayın gerilmeye elverişli olmasını kapsar.","gloss":"bükülgenlik ile koparmadan eğme","neighbor_only":"Yumuşak bir dalı ya da deve boynunu koparmadan eğme eylemini anlatır.","neighbor_ref":"root_000417/B001","relation_type":"near_neighbor","shared_zone":"İki dal da yumuşak bir şeyin kırılmadan eğilebilmesini içerir."},{"boundary_match":"partial","distinction":"Odak dal hayvanın yönlendirilmesi ve yayın bükülmesiyle sınırlıdır; komşu dal insanın özenli ve yumuşak davranış niteliğidir.","focus_only":"Deve ve binekte dirençsiz uyumu, yayda ise somut bükülgenliği anlatır.","gloss":"dirençsiz uyma ile yumuşak davranma","neighbor_only":"İnsanın başkalarına karşı yumuşak, ölçülü ve aşağılanmadan uyumlu davranmasını anlatır.","neighbor_ref":"root_000519/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sertçe karşı koymama ve yumuşak uyum gösterme alanındadır."}],"source_phrase_ar":"أعطى البعير إذا انقاد ولم يستعصب (sihah)؛ قوس عطوى مواتية سهلة (sihah)؛ قوس معطية لينة ليست بكزة ولا ممتنعة (tahdhib)؛ أعط فيعوج رأسه إلى راكبه (tahdhib)","source_summary":"Kaynaklar direnmeden uyma ve kolay bükülme ortaklığını deve, binek ve yay üzerinden verir; başın biniciye çevrilmesi, yönlendirmeye uymanın görünür sonucudur.","sources":["SI","TA"],"what_is_ar":"يدخل فيه انقياد البعير ولين القوس ومطاوعتها وانعطاف الراحلة لصاحبها","what_is_not_ar":"ليس الإعطاء المالي ولا التناول باليد ولا طلب العطاء"},"support_links":[]},{"boundary":"Dal genel uğraşmayı değil, karşılıklı çekişmede öteki kişiye üstün gelme sonucunu anlatır.","branch_kind":"non_bare","branch_ref":"root_001028/B007","candidate_links":[{"candidate_id":"cand_0427a50dab18afbdf9d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","surface_ar":"أَعْطَيْ"}],"gloss":"karşılıklı çekişmede yenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karşılıklı çekişmenin sonunda öteki kişiye üstün gelip onu yenmeyi anlatır."}}],"root_ar":"ع ط و","root_id":"root_001028","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kişinin aynı uğraşta karşı karşıya geldiği ve birinin ötekini yendiği yapı için uygundur.","boundary_detail":"Dal genel uğraşmayı değil, karşılıklı çekişmede öteki kişiye üstün gelme sonucunu anlatır.","branch_image_ar":"الغلبة في التعاطي","concept_gloss":"karşılıklı çekişmede yenme","contextual_glosses":[{"applicability":"Konuşanın karşılıklı uğraşı ve kendi üstün gelme sonucunu birlikte aktardığı cümle için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı çekişmeyi, konuşanı ve onun yenme sonucunu korur."},"facet_ids":["F001"],"text":"çekiştik ve onu yendim","usage_role":"contextual"}],"definition":"İki kişinin karşılıklı bir çekişmeye girmesi ve birinin bu çekişmede ötekini yenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karşılıklı çekişmenin sonunda öteki kişiye üstün gelip onu yenmeyi anlatır."}],"identity_rationale":"Tek kaynak anlatımı, iki kişinin karşılıklı bir uğraşa girmesinden sonra konuşanın ötekini yenmesini bildirir. Bu nedenle dal genel üstünlükten çok, karşılıklı çekişme içindeki yenme sonucuna bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"karşılıklı çekişmede onu yenme"}],"lexicalization_note":"Anlam yalnızca karşılıklı çekişme ve ardından yenme bildiren yapıya bağlı tutulur; yalın köke genel yenme anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen beş ilişki bir tam eşdeğeri ve çekişme türü ya da sonuç genişliği bakımından en açıklayıcı dört yakın dalı gösterir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği ve yapı sınırı örtüşür; iki dal bu kullanımda birbirinin yerine geçebilecek eşdeğer açıklamalar sunar.","focus_only":null,"gloss":"karşılıklı çekişmede üstün gelme","neighbor_only":null,"neighbor_ref":"root_000569/B005","relation_type":"synonym","shared_zone":"İki dal da karşılıklı çekişmeye girip öteki kişiyi yenmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal çekişmenin türünü açık bırakır; komşu dal üstün gelmeyi özellikle karşı çıkma ve uyuşmazlık alanına sınırlar.","focus_only":"Karşılıklı uğraşın türünü belirlemeden öteki kişiyi yenme sonucuna bağlanır.","gloss":"genel çekişmede yenme ile karşı çıkışta yenme","neighbor_only":"Yenmeyi özellikle karşı çıkma ve çekişmeli uyuşmazlık alanındaki yarışmaya bağlar.","neighbor_ref":"root_000808/B003","relation_type":"near_synonym","shared_zone":"İki dal da karşılıklı çekişmede rakibe üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel bir karşılıklı uğraşa bağlıdır; komşu dal yarışmayı özellikle gelişlerin çokluğu üzerinden kurar.","focus_only":"Yarışın veya çekişmenin türünü sık gelme koşuluna bağlamadan yenmeyi anlatır.","gloss":"çekişmede yenme ile geliş sayısında yenme","neighbor_only":"Karşılıklı yarışmayı çok kez gelme ve bu sıklıkta ötekini geçme durumuna bağlar.","neighbor_ref":"root_000281/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da iki kişinin aynı davranışta yarışması ve birinin üstün gelmesi vardır."},{"boundary_match":"partial","distinction":"Odak dal yarışın niteliğini belirlemez; komşu dal onu böbürlenme ve büyüklük taslayarak karşı koyma biçimine bağlar.","focus_only":"Çekişmenin böbürlenme veya büyüklük taslama niteliği taşımasını gerektirmez.","gloss":"çekişmede yenme ile böbürlenme yarışında yenme","neighbor_only":"Yarışmayı böbürlenerek karşı koyma ve büyüklük taslama biçiminde kurar.","neighbor_ref":"root_001281/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir rakiple karşılıklı yarışıp ona üstün gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal karşılıklı çekişme yapısına bağlıdır; komşu dal ise genel zafer, baskınlık ve bir şeyi kazanma alanına yayılır.","focus_only":"Yenmeyi belirli bir karşılıklı çekişme yapısının sonucu olarak bildirir.","gloss":"çekişmede yenme ile genel üstün gelme","neighbor_only":"Genel zaferi, baskıyla boyun eğdirmeyi, bir şeyi kazanmayı ve üstün kılmayı da kapsar.","neighbor_ref":"root_000965/B001","relation_type":"near_synonym","shared_zone":"İki dal da rakibe üstün gelme ve onu yenme sonucunda buluşur."}],"source_phrase_ar":"تعاطينا فعطوته أي غلبته (sihah)","source_summary":"Tek tanıklık, karşılıklı çekişmenin sonunda konuşanın öteki kişiye üstün gelerek onu yenmesini bildirir.","sources":["SI"],"what_is_ar":"يدخل فيه قولهم تعاطينا فعطوته أي غلبته","what_is_not_ar":"ليس العطاء ولا الاستعطاء ولا الانقياد ولا مطلق الخوض في الأمر"},"support_links":["sup_cd12a1b3acdc8e6a1985"]},{"boundary":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B001","candidate_links":[{"candidate_id":"cand_7338a33768b1a5f7fba1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"çokluk ve sayıca artma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin çok bulunmasını ve sayısının artmasını birlikte anlatan genel çekirdek için uygundur.","boundary_detail":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_image_ar":"الكثرة ونماء العدد","concept_gloss":"çokluk ve sayıca artma","contextual_glosses":[{"applicability":"Bir şeyin kendiliğinden ya da süreç içinde sayıca çok duruma gelmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin çok duruma gelme sürecini korur."},"facet_ids":["F002"],"text":"çoğalmak","usage_role":"contextual"},{"applicability":"Bir kişinin ya da etkenin bir şeyi çok duruma getirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dışarıdan yapılan çoklaştırma işlemini korur."},"facet_ids":["F002"],"text":"çoğaltmak","usage_role":"contextual"},{"applicability":"Malın veya bir durumun az ve çok miktarlarını birlikte karşılayan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşıt iki miktarın birlikte anılmasını korur."},"facet_ids":["F003"],"text":"azı ve çoğu","usage_role":"contextual"}],"definition":"Bir şeyin ya da ayrık bir niceliğin az olmayacak ölçüde bulunması veya sayıca artmasıdır. Buna bir şeyi çok duruma getirme ve ondan çokça edinme gibi bu çekirdekten türeyen işlemler de bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."},{"facet_id":"F003","role":"associated_use","statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}],"identity_rationale":"Kaynak ifadesi, çokluğu azlığın karşıtı ve sayının artması olarak kurar; ayrıca bir şeyin çok duruma gelmesini, çok duruma getirilmesini ve ondan çokça edinilmesini de açıkça kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"çokluk; sayının artması ve azlığın karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şey çoğaldı, sayısı arttı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok, sayıca fazla"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi çoğaltmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeyden çokça edinmek veya onu çok saymak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"malın ya da durumun azı ve çoğu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"pek çok, çok büyük sayıda"}],"lexicalization_note":"Tanım yalın çokluk çekirdeğini öne alır; artırma, çokça edinme ve azıyla çoğunu birlikte anan kalıp ayrı bağımlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel artış, çokluk yarışı ve koyuna özgü çoğalma, çekirdek sınırı en açık biçimde gösterdikleri için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Artış bir miktara eklenme işlemini öne çıkarırken odak dal, herhangi bir karşılaştırmalı ekleme gerektirmeden çok olma durumunu da anlatır.","focus_only":"Odak dal, bir şeyin çok bulunmasını ve azlığın karşıtı olan durumu da kapsar.","gloss":"artış ve çokluk","neighbor_only":"Komşu dal, var olan ölçünün üzerine belirli bir ekleme yapılmasını çekirdek edinir.","neighbor_ref":"root_000558/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da sayının veya miktarın başlangıçtakinden daha yüksek olabildiği durumlarda buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalın çokluk ve çoğalmadır; komşu dal ise çokluğu taraflar arasındaki yarışın ve üstün gelmenin ölçüsü yapar.","focus_only":"Odak dalda başka bir tarafı geçme ya da övünme koşulu bulunmaz.","gloss":"çokluk ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluk bakımından yarışmasını, övünmesini veya birinin ötekini geçmesini gerektirir.","neighbor_ref":"root_001286/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sayının, malın veya başka bir varlığın çokluğu belirleyici olabilir."},{"boundary_match":"partial","distinction":"Komşu dalın kapsamı koyunla sınırlıyken odak dal nesne türüne bağlı olmayan genel çokluk çekirdeğidir.","focus_only":"Odak dal her tür sayılabilir varlıkta ve nicelikte genel çokluğu kapsar.","gloss":"genel çokluk ve koyun çokluğu","neighbor_only":"Komşu dal yalnız koyun sürüsünün çoğalmasına bağlı özel bir kullanımdır.","neighbor_ref":"root_000900/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir varlıkların sayıca çok olmasını anlatabilir."}],"source_phrase_ar":"الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)","source_summary":"Kaynaklar çokluğu azlığın karşıtı, sayının artması ve bir şeyin çok olması diye ortaklaştırır; ayrıca çoklaştırma, çokça edinme ve çokluk bildiren niteleme biçimlerini aynı anlam alanına bağlar.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كثرة الشيء والعدد والمال، وضد القلة، والوصف بكثير وكثار وكاثر، وجعل الشيء كثيرا أو الاستكثار منه.","what_is_not_ar":"ليس هو التفاخر أو الغلبة بالكثرة من حيث هي منافسة، ولا كوثر النهر أو الخير الكثير بوصفه اسما مخصوصا، ولا جمار النخل."},"support_links":["sup_876e7255b1214818ae98"]},{"boundary":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B002","candidate_links":[{"candidate_id":"cand_0427a50dab18afbdf9d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"çokluk yarışı ve çoklukla üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarafların çokluğu yarıştırdığı, bununla övündüğü veya birinin daha çok olarak ötekini geçtiği bağlamlar için uygundur.","boundary_detail":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_image_ar":"المكاثرة والغلبة بالعدد","concept_gloss":"çokluk yarışı ve çoklukla üstün gelme","contextual_glosses":[{"applicability":"Bir topluluğun öteki topluluktan daha çok olduğu ve onu bu bakımdan geçtiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayı karşılaştırmasını ve üstün gelen tarafı korur."},"facet_ids":["F002"],"text":"sayıca geçmek","usage_role":"contextual"},{"applicability":"Mal, sayı veya saygınlık gücü üzerinden karşılıklı övünme ve yarışma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarışma alanlarını ve övünme yönünü korur."},"facet_ids":["F001","F003"],"text":"çoklukla övünme yarışı","usage_role":"contextual"}],"definition":"İki tarafın sayı, mal veya saygınlık sağlayan güç bakımından çokluk yarıştırması, bununla övünmesi ya da bir tarafın daha çok olarak ötekini geçmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."},{"facet_id":"F002","role":"specialization","statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."},{"facet_id":"F003","role":"extension","statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi iki tarafın sayı, mal veya güç sayılan bir üstünlük alanında yarışmasını ve bir tarafın çoklukla ötekini geçmesini açıkça bildirir; yenilen tarafı adlandıran biçim de aynı karşıt ilişkiyi doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onlarla çokluk yarışına girdik ve onları sayıca geçtik"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"mal, sayı veya güç bakımından çokluk yarışı ve övünme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çokluk yarışında yenilmiş"}],"lexicalization_note":"Tanım, yarışma ve üstün gelme bildiren yapılara bağlıdır; yalın çokluk anlamı bu yapılardan bağımsız biçimde dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalın çokluk, cömertlik yarışı ve genel övünme, bu dalın çokluk ölçüsüne bağlı yarış sınırını en iyi gösteren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda çokluk karşılaştırmalı bir yarışın aracıdır; komşu dalda ise kendi başına bir nicelik durumu veya artma sürecidir.","focus_only":"Odak dal, taraflar arasında yarışma veya üstün gelme ilişkisini zorunlu kılar.","gloss":"çokluk yarışı ve yalın çokluk","neighbor_only":"Komşu dal, başka bir taraf bulunmadan yalın çokluğu ve çoğalmayı da kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sayının, malın veya başka bir ölçünün çok olmasına dayanır."},{"boundary_match":"partial","distinction":"İlişki düzeni benzese de üstünlüğün ölçüsü ayrıdır: odak dal çokluğu, komşu dal cömertliği temel alır.","focus_only":"Odak dalın yarış ölçüsü sayı, mal veya toplumsal güç gibi çokluk alanlarıdır.","gloss":"çoklukta ve cömertlikte yarış","neighbor_only":"Komşu dalın yarış ölçüsü cömertlik ve eli açıklıktır.","neighbor_ref":"root_001294/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal karşılıklı övünme ve bir tarafın belirli bir ölçütte ötekini geçmesi düzenini taşır."},{"boundary_match":"partial","distinction":"Odak dal, üstünlük iddiasını sayı veya mal gibi çoğaltılabilir değerlere bağlarken komşu dal daha genel bir övünme üstünlüğüdür.","focus_only":"Odak dal övünmeyi özellikle çokluk ölçüsüne bağlar.","gloss":"çoklukla övünmek ve genel övünme","neighbor_only":"Komşu dal övünme alanını belirli bir çokluk ölçüsüyle sınırlamaz.","neighbor_ref":"root_001135/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da karşılıklı övünme ve bir tarafın üstün sayılması bulunabilir."}],"source_phrase_ar":"كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)","source_summary":"Kaynaklar, çokluk bakımından karşılıklı yarışmayı sayıca geçme ve üstün gelme sonucuyla birlikte verir; yarışın mal ve toplumsal güç üzerinden övünmeye uzanabildiğini de belirtir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كاثرناهم فكثرناهم، ومكاثرة القوم إذا غلبوا غيرهم بالعدد، والتكاثر والتفاخر أو التباري بكثرة العدد والمال والعز.","what_is_not_ar":"ليس هو مجرد كون الشيء كثيرا بلا مقابلة أو مفاخرة، ولا المكثر بمعنى كثير المال وحده."},"support_links":["sup_cd12a1b3acdc8e6a1985"]},{"boundary":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_kind":"collocation","branch_ref":"root_001286/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"kişiye bağlı çokluk nitelemeleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız mal, konuşma, istem veya hak çokluğunu belirli kişi kalıplarında toplayan üst açıklama olarak uygundur.","boundary_detail":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_image_ar":"كثرة في صاحب أو كلام أو مطالب","concept_gloss":"kişiye bağlı çokluk nitelemeleri","contextual_glosses":[{"applicability":"Bir kişinin varlığının ve malının çok olduğunu bildiren kişi kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen mal çokluğunu korur."},"facet_ids":["F001"],"text":"malı çok kişi","usage_role":"contextual"},{"applicability":"Kadın veya erkek için sözün çokluğunu bildiren niteleme kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmanın çokluğu ve kişi niteliğini korur."},"facet_ids":["F002"],"text":"çok konuşan kişi","usage_role":"contextual"},{"applicability":"Kendisinden iyilik isteyenlerin veya üzerindeki hakların çok olduğu kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çok sayıda isteyen veya hak sahibinin kişiye yönelmesini korur."},"facet_ids":["F003"],"text":"istek ve hak yükü altında","usage_role":"explanatory"},{"applicability":"Kişinin kendisine ait olmayan mala dayanarak çok malı varmış gibi görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malın başkasına ait oluşunu ve görünüş yaratmayı korur."},"facet_ids":["F004"],"text":"başkasının malıyla varlıklı görünmek","usage_role":"contextual"}],"definition":"Belirli kalıplarda bir kişinin malının ya da sözünün çok olması, kendisinden iyilik isteyenlerin veya üzerindeki hakların çoğalması yahut başkasının malıyla kendini varlıklı göstermesidir. Bu kullanımlar yalnız bağlı oldukları kalıp içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."},{"facet_id":"F002","role":"specialization","statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."},{"facet_id":"F003","role":"specialization","statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."},{"facet_id":"F004","role":"associated_use","statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlamdan çok, belirli kişi ve durum kalıplarında malı veya sözü çok olma, üzerinde çok sayıda istek ya da hak bulunma ve başkasının malıyla çok görünme kullanımlarını toplar. Dal korunabilir, ancak bu kullanımlar ortak bir yalın kök anlamı gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"malı çok kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çok konuşan kadın veya erkek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"başkasının malıyla kendini varlıklı göstermek"}],"lexicalization_note":"Tanım yalnız verilen kişi ve durum kalıplarının anlam alanını düzenler; bunlardan bağımsız bir yalın çokluk anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; genel çokluk, hak isteme ve çokluk yarışı, kalıba bağlı kişi nitelemelerinin sınırını en belirgin biçimde açığa çıkarır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal, çokluk öğesini farklı kalıpların kişi nitelemelerine dağıtır; komşu dal ise çokluğu kendi başına tanımlar.","focus_only":"Odak dalda her anlam belirli bir kişi veya durum kalıbına bağlıdır.","gloss":"kalıba bağlı ve genel çokluk","neighbor_only":"Komşu dal, kalıptan bağımsız yalın çokluğu ve sayıca artmayı kapsar.","neighbor_ref":"root_001286/B001","relation_type":"same_field","shared_zone":"Her iki dalın kullanımlarında da bir varlığın, sözün, malın veya istemin çokluğu bulunur."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici olan isteyenlerin ya da hakların çokluğudur; komşu dalda ise tek bir istem bile olsa hakkın peşine düşme ilişkisidir.","focus_only":"Odak dal, istem veya hak sahiplerinin çokluğunu ve bunların bir kişinin üzerinde birikmesini bildirir.","gloss":"çok sayıda istem ve hak isteme","neighbor_only":"Komşu dal, istemin sayısından bağımsız olarak bir hakkı veya alacağı isteme eylemini çekirdek edinir.","neighbor_ref":"root_000175/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye yönelen hak veya iyilik istemleri bağlamında buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dalın kişi nitelemeleri karşılıklı yarışma gerektirmez; komşu dalın çekirdeği karşılaştırma ve üstün gelmedir.","focus_only":"Odak dal kişide bulunan mal, söz veya yük çokluğunu kalıplaşmış biçimde niteler.","gloss":"çokluk niteliği ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluğu yarıştırmasını ve birinin üstün gelmesini anlatır.","neighbor_ref":"root_001286/B002","relation_type":"same_field","shared_zone":"Her iki dalda mal veya sayı gibi çokluk ölçüleri kişilere bağlanabilir."}],"source_phrase_ar":"رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)","source_summary":"Kaynaklar, kalıba göre mal çokluğu, çok konuşma, iyilik isteyenlerin veya hak sahiplerinin çoğalması ve başkasının malıyla varlıklı görünme anlamlarını verir; bunlar ortak çokluk öğesine rağmen ayrı kullanımlardır. Bir açıklamada hakların çoğalmasına kişinin elindekinin tükenmesi eşlik eder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه مكثر أو كاثر بمعنى كثير المال، ومكثار في كثرة الكلام، ومكثور عليه لكثرة طالبي المعروف أو الحقوق عليه، ويتكثر بمال غيره.","what_is_not_ar":"ليس هو المكاثرة بين جماعتين، ولا كوثر بمعنى السيد الكثير الخير أو النهر."},"support_links":[]},{"boundary":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"özel ırmak veya bol iyilik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biriminin iki temel açıklamasını birlikte gösterir; kişi nitelemesi ayrıca bağlama bağlıdır.","boundary_detail":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_image_ar":"الكوثر: خير كثير وفيض مخصوص","concept_gloss":"özel ırmak veya bol iyilik","contextual_glosses":[{"applicability":"Başka ırmakların kendisinden ayrıldığı bildirilen cennet ırmağı anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Irmak oluşunu ve cennete özgü gönderimi korur."},"facet_ids":["F001"],"text":"cennetteki özel ırmak","usage_role":"contextual"},{"applicability":"Birine verilmiş çok geniş ve büyük iyiliği anlatan açıklamada kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliğin hem bolluğunu hem büyüklüğünü korur."},"facet_ids":["F002"],"text":"bol ve büyük iyilik","usage_role":"contextual"},{"applicability":"Cömertliği, iyiliği ve çok bağışta bulunmasıyla öne çıkan erkek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin cömertliğini, önderliğini ve bağış bolluğunu korur."},"facet_ids":["F003"],"text":"iyiliği ve bağışı bol önder","usage_role":"contextual"}],"definition":"Olağanüstü bolluk bildiren özel bir sözlük birimi, cennetteki bir ırmağı veya bol ve büyük iyiliği adlandırır; kişi kalıbında ise iyiliği ve bağışı bol, cömert bir önderi niteler.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."},{"facet_id":"F002","role":"core","statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."},{"facet_id":"F003","role":"extension","statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}],"identity_rationale":"Kaynak ifadesi aynı sözlük birimini cennetteki özel ırmak, bol ve büyük iyilik, ayrıca iyiliği ve bağışı bol cömert önder için kullanır. Dal bu sözlüksel çokanlamlılık olarak korunabilir; bu üç gönderim tek bir varlık tanımıymış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"cennetteki özel ırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bol veya büyük iyilik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iyiliği ve bağışı bol, cömert önder"}],"lexicalization_note":"Tanım, yalın bir çokluk anlamı kurmak yerine verilen sözcük ve kişi kalıbına bağlı üç özel kullanımı ayrı tutar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel çokluk, aynı kökteki yoğun toz kullanımı ve bastıran çokluk, özel bolluk anlamlarının sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bolluğu belirli bir ırmak, iyilik veya cömert kişi adı ve nitelemesi içinde özelleştirir; komşu dal genel nicelik çekirdeğidir.","focus_only":"Odak dal belirli bir sözlük biriminin ırmak, bol iyilik ve cömert kişi kullanımlarına bağlıdır.","gloss":"özel bolluk kullanımı ve genel çokluk","neighbor_only":"Komşu dal varlık türünden bağımsız yalın çokluğu ve sayıca artmayı anlatır.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da azlığın karşıtı olan bolluk düşüncesini taşıyabilir."},{"boundary_match":"field_only","distinction":"Ortak bolluk bağına karşın gönderimler ayrıdır: odak dal iyilik, ırmak ve kişiyi; komşu dal tozu ve aşırı çoğalmayı anlatır.","focus_only":"Odak dal ırmak, iyilik ve cömert kişiyle ilgili özel kullanımları kapsar.","gloss":"bol iyilik ve yoğun toz","neighbor_only":"Komşu dal kabarıp yükselen yoğun tozu ve bir şeyin aşırı derecede çoğalmasını kapsar.","neighbor_ref":"root_001286/B005","relation_type":"same_field","shared_zone":"İki dalın sözlük birimleri olağanüstü çokluk ve bolluk düşüncesiyle açıklanır."},{"boundary_match":"partial","distinction":"Odak dalda baskın gelme koşulu yoktur; komşu dalda çokluğun yükselerek başka şeyleri örtmesi veya yenmesi belirleyicidir.","focus_only":"Odak dalda bolluk özel olarak iyilik, bağış, kişi veya ırmakla sözlükselleşir.","gloss":"bolluk ve bastıran çokluk","neighbor_only":"Komşu dal çokluğun yükselip çevresindekileri bastırmasını çekirdek edinir.","neighbor_ref":"root_000952/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olağan ölçüyü aşan bir çokluğu anlatabilir."}],"source_phrase_ar":"الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)","source_summary":"Kaynaklar özel sözlük birimini cennetteki bir ırmak ve bol ya da büyük iyilik olarak açıklar; kişi için kullanıldığında cömertliği, önderliği, iyilik ve bağış bolluğunu bildirir. Bir açıklamada cennet ırmaklarının çoğunun ondan ayrıldığı, bir diğerinde ise bol iyiliğin Peygamber'e verildiği belirtilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر بوصفه نهر الجنة، أو الخير الكثير العظيم، أو الرجل السيد السخي الكثير الخير والعطاء، وكل ذلك من فوعل الكثرة.","what_is_not_ar":"ليس هو مطلق الكثرة العددية، ولا جمار النخل، ولا غبار الكوثر إلا من جهة صيغة المبالغة في الكثرة."},"support_links":[]},{"boundary":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"kabarıp yükselen yoğun toz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görüntü bakımından belirgin toz çekirdeğini karşılar; genel aşırı çoğalma ayrıca bağlama göre çevrilir.","boundary_detail":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_image_ar":"كوثر الغبار وتكوثره","concept_gloss":"kabarıp yükselen yoğun toz","contextual_glosses":[{"applicability":"Çok miktarda tozun kabarıp havada görünür duruma geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun çokluğunu ve havada toplanmış görünümünü korur."},"facet_ids":["F001","F003"],"text":"yoğun toz bulutu","usage_role":"contextual"},{"applicability":"Tozla sınırlı olmayan biçimde bir şeyin aşırı ölçüde çok duruma gelmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğalmanın aşırı dereceye varmasını korur."},"facet_ids":["F002"],"text":"son derece çoğalmak","usage_role":"contextual"}],"definition":"Toz kalıbında, çok olup kabaran veya havada belirgin biçimde yükselen yoğun tozu anlatır. Ayrı bir biçimde ise herhangi bir şeyin son derece çoğalmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."},{"facet_id":"F002","role":"extension","statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."},{"facet_id":"F003","role":"example","statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}],"identity_rationale":"Kaynak ifadesi yoğunlaşıp yükselen tozu adlandıran özel kullanımla bir şeyin son derece çoğalmasını bildiren biçimi birlikte verir. Ortak aşırı çokluk bağı dalı korur, ancak toz görüntüsü genel çoğalma anlamının zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kabarıp yükselen yoğun toz"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"son derece çoğalmak"}],"lexicalization_note":"Tanım, toza bağlı kalıbı ve genel aşırı çoğalma biçimini ayrı yüzler olarak tutar; toz özelliğini yalın çoğalma anlamına taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükselmiş toz, havadaki görünür toz ve genel çokluk, dalın yoğunluk, kabarma ve aşırılık sınırlarını en açık biçimde karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Toz bağlamında anlamlar büyük ölçüde örtüşür; odak dal çokluk ve kabarmayı belirginleştirir ve ayrıca toz dışı aşırı çoğalma kullanımına sahiptir.","focus_only":"Odak dal, yoğun toz yanında bir şeyin aşırı çoğalmasını bildiren ayrı bir biçimi de kapsar.","gloss":"yoğun kabaran toz ve yükselmiş toz","neighbor_only":"Komşu dal tozu genel olarak, özellikle kaldırılmış veya yükselmiş toz olarak adlandırır.","neighbor_ref":"root_001544/B004","relation_type":"near_synonym","shared_zone":"İki dal da havaya kalkmış, görünür ve yoğun tozu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde yoğunluk ve çokluk vardır; komşu dal görünürlük ve havada uçuşan toz görüntüsüne daha geniş yer verir.","focus_only":"Odak dal tozun çokluğunu ve kabarmasını, ayrıca genel aşırı çoğalmayı bildirir.","gloss":"kabarık yoğun toz ve havadaki toz","neighbor_only":"Komşu dal havada parlayan veya ışıkta belirginleşen ince toz parçalarını da kapsar.","neighbor_ref":"root_001576/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da tozun havaya yükselip görünür olması bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal çokluğun son dereceye ulaşmasını veya yoğun toz olarak görünmesini gerektirirken komşu dal derece bakımından nötrdür.","focus_only":"Odak dal aşırı çoğalmayı ve toza özgü kabarıp yükselme görüntüsünü taşır.","gloss":"aşırı çoğalma ve genel çokluk","neighbor_only":"Komşu dal herhangi bir aşırılık ya da toz görüntüsü gerektirmeyen genel çokluktur.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin çok olması veya çoğalması durumunu anlatabilir."}],"source_phrase_ar":"الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)","source_summary":"Kaynaklar, çokluğu yüzünden kabarıp yükselen yoğun tozu ve bir şeyin son derece çoğalmasını aynı aşırılık alanında birleştirir; kabaran ölüm tozu bu kullanıma örnek verilir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر من الغبار إذا كثر وثار أو سطع، وتكوثر الشيء إذا كثر كثرة متناهية.","what_is_not_ar":"ليس هو الكوثر بمعنى نهر الجنة أو الخير العظيم، ولا مطلق كثير بلا صورة ثوران أو إفراط."},"support_links":[]},{"boundary":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B006","candidate_links":[{"candidate_id":"cand_23ef5df9ade66d1b1480","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"hurma ağacının iç göbeği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların ortak temel gönderimini, hurma ağacının yumuşak iç bölümü olarak karşılar.","boundary_detail":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_image_ar":"الكثر جمار النخل","concept_gloss":"hurma ağacının iç göbeği","contextual_glosses":[{"applicability":"Ağacın tepe kısmından çıkarılan yumuşak iç göbek yiyecek olarak söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurmaya ait oluşu, iç konumu ve yenilebilirliği korur."},"facet_ids":["F001"],"text":"hurmanın yenilebilir iç bölümü","usage_role":"explanatory"},{"applicability":"Adın hurma ağacındaki çiçek salkımının ilk oluşumu için kullanıldığı açıklamaya uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurma ağacını ve çiçeklenmenin ilk oluşumunu korur."},"facet_ids":["F002"],"text":"hurmanın ilk çiçek sürgünü","usage_role":"contextual"}],"definition":"Hurma ağacının tepe bölümündeki yumuşak ve yenilebilir iç göbeğini adlandırır; bazı açıklamalarda çiçek salkımının ilk oluşumuna da uzanır. Aynı birim belirli bir ceza sözünde meyveyle birlikte anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."},{"facet_id":"F003","role":"associated_use","statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}],"identity_rationale":"Kaynak ifadesinin ortak ağırlığı hurma ağacının yenilebilir iç göbeğindedir; bazı açıklamalar bunu ağacın çekilen öz bölümü veya çiçek salkımının ilk oluşumu olarak genişletir. Dal korunabilir, fakat bu ikinci açıklama kesin eşdeğer gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"meyve veya hurma göbeği için el kesme cezası yoktur"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hurma ağacı çiçek sürgünü verdi"}],"lexicalization_note":"Tanım, bitki adını çekirdek alır; söz içindeki kullanım ve ağacın çiçeklenmesini bildiren biçim ayrı bağlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel ağaç göbeği, hurma salkımı ve zararlı sert sürgün, bitkinin aynı bölgesindeki karışabilecek gönderimleri en iyi ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hurma göbeği bağlamında büyük ölçüde örtüşürler; odak dalın bitki kapsamı daha dar, çiçek sürgünü açıklaması ise ona özgüdür.","focus_only":"Odak dal hurma ağacına özgüdür ve bazı açıklamalarda ilk çiçek sürgününe uzanır.","gloss":"hurma göbeği ve ağaç göbeği","neighbor_only":"Komşu dal hurma yanında başka ağaçların yumuşak iç göbeklerini de kapsar.","neighbor_ref":"root_001248/B003","relation_type":"near_synonym","shared_zone":"İki dal da hurma ağacının tepesindeki yumuşak iç bölümü adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak iç dokuya veya ilk sürgüne, komşu dal ise gelişmiş meyveleri taşıyan salkıma gönderir.","focus_only":"Odak dal ağacın iç göbeğini ve bazı açıklamalarda ilk çiçek oluşumunu anlatır.","gloss":"hurma göbeği ve meyve salkımı","neighbor_only":"Komşu dal hurmanın üzerinde meyveler bulunan bütün salkımını adlandırır.","neighbor_ref":"root_001264/B004","relation_type":"same_field","shared_zone":"İki dal da hurma ağacının tepe ve ürün oluşumu alanıyla ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak ve yenilebilir iç bölümü öne çıkarır; komşu dal sertliği ve ağaca zarar verme sonucuyla ayrılır.","focus_only":"Odak dal yenilebilir iç göbeği veya ilk çiçek sürgününü adlandırır.","gloss":"yumuşak göbek ve zararlı sert sürgün","neighbor_only":"Komşu dal bırakıldığında ağaca zarar veren uzun ve sert bir sürgünü anlatır.","neighbor_ref":"root_000489/B003","relation_type":"same_field","shared_zone":"Her iki dal hurma ağacının kalbinden veya tepesinden çıkan bir oluşumla ilgilidir."}],"source_phrase_ar":"الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)","source_summary":"Kaynaklar adı çoğunlukla hurma ağacının iç göbeği ve çekilen öz bölümü için verir; bir açıklama çiçek salkımının ilk oluşumunu da kapsar ve yaygın bir sözde meyveyle birlikte anılır. Ad için kaynaklarda birden fazla harekeleme ve okunuş biçimi de aktarılır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الكثر أو الكثر بمعنى جمار النخل، والجذب، وطلع النخل عند بعض المصادر، وما ورد في لا قطع في ثمر ولا كثر.","what_is_not_ar":"ليس هو الكثرة العددية، ولا الكوثر، ولا المال الكثير."},"support_links":["sup_961914d8688ce357ed7c"]},{"boundary":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_kind":"bare","branch_ref":"root_001286/B007","candidate_links":[{"candidate_id":"cand_23ef5df9ade66d1b1480","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","surface_ar":"كَوْثَرَ"}],"gloss":"bir araya toplanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin öğelerinin birleşerek toplu duruma gelmesini anlatan yalın anlam için uygundur.","boundary_detail":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_image_ar":"الكمثرة اجتماع الشيء","concept_gloss":"bir araya toplanma","contextual_glosses":[{"applicability":"Bir şeyin ayrı öğelerinin aynı yerde veya bütün içinde birleşmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı öğelerin birleşme sürecini korur."},"facet_ids":["F001"],"text":"toplanıp bir araya gelmek","usage_role":"contextual"}],"definition":"Bir şeyin parçalarının veya öğelerinin bir araya gelerek toplanmasıdır; sözlük biriminin yapısındaki ek ses, bu anlamın çokluk ailesiyle bağlantısı olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."},{"facet_id":"F002","role":"associated_use","statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}],"identity_rationale":"Tek kaynak ifadesi, bir şeyin bir araya toplanması anlamını doğrudan verir ve sözcük yapısındaki ek sesin çokluk ailesiyle bağlantısını ayrıca belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir"}],"lexicalization_note":"Tanım, kanıtta verilen yalın sözlük biriminin bir araya toplanma anlamıyla sınırlıdır ve herhangi bir kalıp anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel toplama, yönlerden bir araya getirme ve doluluk yaratan birikme, bu yalın toplanma anlamının kapsamını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak çekirdek güçlüdür; komşu dalın eylem, katılımcı ve kullanım kapsamı odak daldan daha geniştir.","focus_only":"Odak dal yalnız bir şeyin öğelerinin bir araya toplanmasını bildirir.","gloss":"bir araya toplanma ve genel toplama","neighbor_only":"Komşu dal hem toplama eylemini hem insanların, suyun, yemeğin ve başka varlıkların çeşitli birleşme biçimlerini kapsar.","neighbor_ref":"root_001210/B001","relation_type":"near_synonym","shared_zone":"İki dal da ayrı öğelerin birleşerek toplu duruma gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal sonuçlanan bir araya gelişi bildirirken komşu dal toplama işlemini, yön çeşitliliğini ve türemiş kullanımları daha geniş biçimde taşır.","focus_only":"Odak dal yalın biçimde bir şeyin bir araya toplanmasını anlatır.","gloss":"toplanma ve yönlerden toplama","neighbor_only":"Komşu dal farklı yönlerden toplama, birbirine katma ve bundan türetilen adlandırmaları da kapsar.","neighbor_ref":"root_001216/B001","relation_type":"near_synonym","shared_zone":"İki dalda da dağınık öğelerin bir araya gelmesi temel görüntüdür."},{"boundary_match":"partial","distinction":"Odak dal nicelik derecesi belirtmez; komşu dal birikimin çok ve doluluk yaratacak ölçüde olmasını çekirdek edinir.","focus_only":"Odak dal için öğelerin bir araya gelmesi yeterlidir; çokluk veya doluluk zorunlu değildir.","gloss":"toplanma ve dolacak kadar birikme","neighbor_only":"Komşu dal toplanmanın yanında çokluğu ve dolacak ölçüde birikmeyi gerektirir.","neighbor_ref":"root_000261/B001","relation_type":"near_neighbor","shared_zone":"İki dal da öğelerin aynı yerde birikmesi veya birleşmesi durumunda buluşur."}],"source_phrase_ar":"الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)","source_summary":"Tek kaynak, sözlük birimini bir şeyin bir araya toplanması diye açıklar ve yapısına eklenen m sesiyle birlikte onu çokluk anlam ailesine bağlar.","sources":["MQ"],"what_is_ar":"يدخل فيه الكمثرة بمعنى اجتماع الشيء، مع تصريح Maqāyīs بأن الميم زائدة وأنه من الكثرة.","what_is_not_ar":"ليس هو استعمالا عاديا للثلاثي كثر، ولا الجمار أو الكوثر."},"support_links":["sup_961914d8688ce357ed7c"]}],"candidate_inventory":[{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_a86191960184d2563141","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:divine-plural-singular-recipient","source_type":"word_analysis","support_ids":["sup_c50acf14f18f35228890","sup_e9240a8073921884bf07"],"title":"plural divine speaker faces one addressee","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_b6572c64a221feab1ae3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:emphatic-divine-assertion","source_type":"word_analysis","support_ids":["sup_92aaf22e424fcd72d3c5","sup_c50acf14f18f35228890"],"title":"emphatic divine assertion governs the gift clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_db6bc0dd7661afded1a0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:fused-pronoun-and-sound","source_type":"word_analysis","support_ids":["sup_79ca2c395fec0ad5e393","sup_c50acf14f18f35228890"],"title":"fused form makes speaker and assertion inseparable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_29f7852cb8e884c47ef7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:na-reprise-into-verb","source_type":"word_analysis","support_ids":["sup_76a96097de9a82716e3b","sup_c50acf14f18f35228890"],"title":"repeated {{ar:نَا}} ({{tr:nā}}) carries agency into the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_d16e03d69cae3556ac87","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:surah-launch-and-response-arc","source_type":"word_analysis","support_ids":["sup_c50acf14f18f35228890","sup_d21a808ace598f1e3a15"],"title":"opening assertion launches gift before response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_c3169c7de0fcbd469008","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:completed-active-grant","source_type":"word_analysis","support_ids":["sup_dd9edcee0c013b02b7f9","sup_f83d90ee8ccc896ad323"],"title":"active perfect presents completed divine giving","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_4f6a7ed20c4bfac87ae9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:deictic-pivot","source_type":"word_analysis","support_ids":["sup_04067f8055aedc306c69","sup_dd9edcee0c013b02b7f9"],"title":"verb pivots from speaker to recipient to gift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_c798458ee6956feba02a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:distribution-and-echo","source_type":"word_analysis","support_ids":["sup_dd9edcee0c013b02b7f9","sup_e72c900b18661f8b7601"],"title":"rare Form IV giving contrasts future giving in 93:5","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_8a95f9fb75c21492eb06","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:double-object-transfer","source_type":"word_analysis","support_ids":["sup_93bae7179daa5b4aac9b","sup_dd9edcee0c013b02b7f9"],"title":"one verb distinguishes recipient and gift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_2aef57037a0f1582e5c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:form-iv-caused-possession","source_type":"word_analysis","support_ids":["sup_7dc711aa8c4160abe485","sup_dd9edcee0c013b02b7f9"],"title":"Form IV gives as conferred possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_cfb0b663765d3c8e03c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:forward-command-premise","source_type":"word_analysis","support_ids":["sup_00197af232e1b1974aa9","sup_dd9edcee0c013b02b7f9"],"title":"completed grant grounds the response command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_86abb7f4774982b91872","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:lexical-image-pressure","source_type":"word_analysis","support_ids":["sup_dd9edcee0c013b02b7f9","sup_ff2f0ab2daa1dd35fda4"],"title":"yielding and reaching color the grant","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_3ce1ee1ee54bc80b2ca0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:na-reprise","source_type":"word_analysis","support_ids":["sup_7d5c54d9e01edd06b353","sup_dd9edcee0c013b02b7f9"],"title":"second {{ar:نَا}} ({{tr:nā}}) reprises the opener","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_865fba7f1f08c80b3609","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:performative-report","source_type":"word_analysis","support_ids":["sup_75efb3bc9150ea04f6be","sup_dd9edcee0c013b02b7f9"],"title":"declaration carries performative force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:2","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_c9066aeef85954a6ddb0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:clause-final-landing","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_2d4f0985dd3fa18b0424"],"title":"final position lands the clause on abundance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_90b5c1ee71ef7acca948","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:definite-hapax-identifiability","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_985b3f574c01556537a8"],"title":"definite article makes a unique lexeme identifiable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_ecf9eee7c67db210e2e8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:form-level-rarity","source_type":"word_analysis","support_ids":["sup_0c1ba0cf1584a7544e04","sup_294620b017cff7e41065"],"title":"rarity is form-level, not root-level","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_767864bd89fef34d2c44","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:generosity-field","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_50718cf6d3ba8b8400d2"],"title":"giver-quality field makes the gift generative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_320398157237fad55e12","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:gift-object-grammar","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_549f461581ed3eabc53c"],"title":"accusative noun is the given thing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_0ffaea460dd0cbe35167","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:intensive-fawal-superabundance","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_fc2b3741534e66d69bd6"],"title":"faʿwal form intensifies abundance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_75e28441f4e9eb50a773","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:overflow-contained-in-one-noun","source_type":"word_analysis","support_ids":["sup_22fca59db98e020c2b90","sup_294620b017cff7e41065"],"title":"unbounded abundance is packaged as one gift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_bb559b46a3b91b700071","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:phonetic-and-fawasil-texture","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_bf6c3a68ff80e89c0cc7"],"title":"sound gives the gift a full landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_e7e10ade104da3d4f253","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:received-not-rivalrous-abundance","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_9634eafad184e25c269d"],"title":"abundance is received, not multiplied or contested","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_39dad363190e1ef8ff78","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:referential-openness","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_d6469a1da04f84dde08e"],"title":"river and abundant-good readings remain locally possible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_5fa209a8270a03447a2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:root-family-compression","source_type":"word_analysis","support_ids":["sup_294620b017cff7e41065","sup_e46d41b249a4eaefd0e2"],"title":"common root field crystallizes into one rare form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_97c80149a6c1e45e3267","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:same-surah-forward-echoes","source_type":"word_analysis","support_ids":["sup_26ad8b709625c2425af6","sup_294620b017cff7e41065"],"title":"gift anticipates response and cutoff contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:3","qac_refs":["108:1:3:1","108:1:3:2"],"status":"accepted"}},{"anchor_refs":["108:1:2"],"branch_refs":[],"candidate_id":"cand_a57c4c88b01dd5d51904","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001028"],"scope":"focus_ayah","source_local_id":"108:1:2:1","source_type":"qac_morpheme","support_ids":["sup_5bde672996fab35890f9"],"title":"QAC root occurrence: ع ط و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["108:1:3"],"branch_refs":[],"candidate_id":"cand_f422188acf953c9bbbfd","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"108:1:3:2","source_type":"qac_morpheme","support_ids":["sup_dbd8457319a724878f4b"],"title":"QAC root occurrence: ك ث ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["108:1:1"],"branch_refs":[],"candidate_id":"cand_a3b0b5b16d43f89c1ca7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"108:1:1:generosity-theology-synthesis","source_type":"word_analysis","support_ids":["sup_b865aa060dc9f5a6a0db","sup_c50acf14f18f35228890"],"title":"broad theological synthesis repeats retained payoffs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"108:1:1","qac_refs":["108:1:1:1","108:1:1:2"],"status":"accepted"}},{"anchor_refs":["108:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:1","branch_refs":["root_001028/B002","root_001286/B001"],"candidate_id":"cand_7338a33768b1a5f7fba1","commentary_obligation":"review","hft_ref":"hft_d62e75081262ca7a3d72","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_transferred_plenitude","source_type":"hft","support_ids":["sup_876e7255b1214818ae98"],"title":"base_transferred_plenitude","trust":"legacy_unbound"},{"anchor_refs":["108:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:1","branch_refs":["root_001028/B002","root_001028/B007","root_001286/B002"],"candidate_id":"cand_0427a50dab18afbdf9d0","commentary_obligation":"review","hft_ref":"hft_2888215eed5e30eebdaa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_comparative_preponderance","source_type":"hft","support_ids":["sup_cd12a1b3acdc8e6a1985"],"title":"base_comparative_preponderance","trust":"legacy_unbound"},{"anchor_refs":["108:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"108:1","branch_refs":["root_001028/B002","root_001286/B006","root_001286/B007"],"candidate_id":"cand_23ef5df9ade66d1b1480","commentary_obligation":"review","hft_ref":"hft_d37af64ecf020ed3d8fb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_concentrated_fecundity","source_type":"hft","support_ids":["sup_961914d8688ce357ed7c"],"title":"base_concentrated_fecundity","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"108:1:1:1","qac_word_ref":"108:1:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:1:2","qac_word_ref":"108:1:1","root_ar":"","surface_ar":"آ"},{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","root_ar":"ع ط و","surface_ar":"أَعْطَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:2:2","qac_word_ref":"108:1:2","root_ar":"","surface_ar":"نَٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:2:3","qac_word_ref":"108:1:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"108:1:3:1","qac_word_ref":"108:1:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","root_ar":"ك ث ر","surface_ar":"كَوْثَرَ"}],"word_analysis_qac_refs":[["108:1:1:1","108:1:1:2"],["108:1:2:1","108:1:2:2","108:1:2:3"],["108:1:3:1","108:1:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["108:1:1","108:1:2","108:1:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"108:1:1:1","qac_word_ref":"108:1:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:1:2","qac_word_ref":"108:1:1","root_ar":"","surface_ar":"آ"},{"lemma_ar":"أَعْطَىٰ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P","morpheme_role":"STEM","pos":"V","qac_ref":"108:1:2:1","qac_word_ref":"108:1:2","root_ar":"ع ط و","surface_ar":"أَعْطَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:2:2","qac_word_ref":"108:1:2","root_ar":"","surface_ar":"نَٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"108:1:2:3","qac_word_ref":"108:1:2","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"108:1:3:1","qac_word_ref":"108:1:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"كَوْثَر","morph_features":"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"108:1:3:2","qac_word_ref":"108:1:3","root_ar":"ك ث ر","surface_ar":"كَوْثَرَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["108:1:1:1","108:1:1:2"],["108:1:2:1","108:1:2:2","108:1:2:3"],["108:1:3:1","108:1:3:2"]],"word_analysis_refs":["108:1:1","108:1:2","108:1:3"],"word_rows":[{"analysis_record_ref":"108:1:1","analytic_gloss_range_en":"emphatic divine self-reference that asserts the whole giving clause as established fact","analytic_root_gloss_range_en":null,"qac_refs":["108:1:1:1","108:1:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّا","transliteration":"innā"}},{"analysis_record_ref":"108:1:2","analytic_gloss_range_en":"completed active Form IV granting that causes the addressed recipient to have the named gift","analytic_root_gloss_range_en":"giving, handing over, causing possession, productive yielding, reaching toward, asking for a gift, compliant yielding, and overreaching; the local Form IV double-object frame selects divine granting and conferred possession","qac_refs":["108:1:2:1","108:1:2:2","108:1:2:3"],"root":{"arabic":"ع ط و","transliteration":"ʿ-ṭ-w"},"surface":{"arabic":"أَعْطَيْنَٰكَ","transliteration":"aʿṭaynāka"}},{"analysis_record_ref":"108:1:3","analytic_gloss_range_en":"the definite intensive gift: a unique named or quintessential abundance, locally the second object granted to the addressee","analytic_root_gloss_range_en":"abundance, manyness, increase, outnumbering, rivalry in abundance, much speech or claim, and fruitful plentifulness; the local faʿwal definite noun gathers the abundance field into one gift rather than a rivalry or multiplying act","qac_refs":["108:1:3:1","108:1:3:2"],"root":{"arabic":"ك ث ر","transliteration":"k-th-r"},"surface":{"arabic":"ٱلْكَوْثَرَ","transliteration":"al-kawthar"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["108:1"],"branch_refs":["root_001028/B002","root_001286/B001"],"candidate_id":"cand_7338a33768b1a5f7fba1","evidence_scope":"focus_ayah","hft_ref":"hft_d62e75081262ca7a3d72","item_id":"base_transferred_plenitude","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_transferred_plenitude","support_id":"sup_876e7255b1214818ae98"},{"anchor_refs":["108:1"],"branch_refs":["root_001028/B002","root_001028/B007","root_001286/B002"],"candidate_id":"cand_0427a50dab18afbdf9d0","evidence_scope":"focus_ayah","hft_ref":"hft_2888215eed5e30eebdaa","item_id":"base_comparative_preponderance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_comparative_preponderance","support_id":"sup_cd12a1b3acdc8e6a1985"},{"anchor_refs":["108:1"],"branch_refs":["root_001028/B002","root_001286/B006","root_001286/B007"],"candidate_id":"cand_23ef5df9ade66d1b1480","evidence_scope":"focus_ayah","hft_ref":"hft_d37af64ecf020ed3d8fb","item_id":"base_concentrated_fecundity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_concentrated_fecundity","support_id":"sup_961914d8688ce357ed7c"}],"diagnostics":[],"lane_counts":{"global":7,"macro":8,"micro":3},"packet_summary":{"ayah_count":3,"focus_ref":"108:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["108:1","108:2","108:3"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"108:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"108:1","lane":"micro","linguistic_source_ref":"108:1","surface_ref":"108:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"108:1","target_tokens":[["Kuşkusuz",["108:1:1"]],["biz",["108:1:1","108:1:2"]],["sana",["108:1:2"]],["bolluk",["108:1:3"]],["verdik",["108:1:2"]]],"text":"Kuşkusuz biz sana bolluk verdik."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":3,"id":"s108-p01-001-003","label":"Whole surah","number":1,"refs":["108:1","108:2","108:3"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:forward-command-premise","source_type":"word_analysis","support_id":"sup_00197af232e1b1974aa9","text":"{\"blocking_evidence\":null,\"headline\":\"completed grant grounds the response command\",\"reader_payoff\":\"The reader notices that the verb functions as the premise for the following worship command in 108:2 rather than as an isolated report.\",\"reason\":\"The CRITICAL rows tie the completed grant to the concrete next-ayah response, and the local syntax supports the gift statement as the surah's opening premise.\",\"representative_source_ids\":[\"QS-dd2289fb\",\"QY-6223ff07\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:deictic-pivot","source_type":"word_analysis","support_id":"sup_04067f8055aedc306c69","text":"{\"blocking_evidence\":null,\"headline\":\"verb pivots from speaker to recipient to gift\",\"reader_payoff\":\"The reader notices that the middle word converts divine self-identification into an action directed to one addressee and awaiting its gift object.\",\"reason\":\"The verbal clause is the predicate of the opening emphatic particle, and the suffix marks a second-person singular addressee before the explicit gift object.\",\"representative_source_ids\":[\"QI-1b879bf3\",\"QT-58932631\",\"QT-7afd3fb2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:form-level-rarity","source_type":"word_analysis","support_id":"sup_0c1ba0cf1584a7544e04","text":"{\"blocking_evidence\":null,\"headline\":\"rarity is form-level, not root-level\",\"reader_payoff\":\"The reader notices that the marked feature is not an obscure root but the special local form chosen from a familiar abundance field.\",\"reason\":\"The bundle's distribution rows distinguish the unique local lexeme from the broader root field, matching the QAC note that this is a specific intensive nominal form.\",\"representative_source_ids\":[\"QI-900f2c81\",\"QH-15532679\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:overflow-contained-in-one-noun","source_type":"word_analysis","support_id":"sup_22fca59db98e020c2b90","text":"{\"blocking_evidence\":null,\"headline\":\"unbounded abundance is packaged as one gift\",\"reader_payoff\":\"The reader notices the tension between excess beyond containment and the grammar that gathers it into one definite object.\",\"reason\":\"The root branch supports abundance and increase, while the local surface is a singular definite noun in the object slot.\",\"representative_source_ids\":[\"QS-6e660c12\",\"QF-6c349d23\",\"QF-9d8ef245\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:same-surah-forward-echoes","source_type":"word_analysis","support_id":"sup_26ad8b709625c2425af6","text":"{\"blocking_evidence\":null,\"headline\":\"gift anticipates response and cutoff contrast\",\"reader_payoff\":\"The reader notices that the named gift in 108:1 grounds the worship response in 108:2 and sets the abundance-versus-cutoff contrast in 108:3.\",\"reason\":\"The rows give concrete same-surah relations, and the local gift-object grammar supports a forward gift-to-response and abundance-to-deprivation arc.\",\"representative_source_ids\":[\"QE-421ff585\",\"QE-f96526a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3","source_type":"word_analysis","support_id":"sup_294620b017cff7e41065","text":"{\"gloss_range\":\"the definite intensive gift: a unique named or quintessential abundance, locally the second object granted to the addressee\",\"prose\":\"{{ar:ٱلْكَوْثَرَ}} ({{tr:al-kawthar}}) is the gift on which the ayah lands. Grammar keeps it distinct from the recipient: {{ar:أَعْطَيْنَٰكَ}} ({{tr:aʿṭaynāka}}) marks the addressee in the verb and then gives this definite accusative noun as the second object. The article and singular noun shape make a unique or quintessential abundance identifiable even though the lexeme occurs only here. Its intensive faʿwal form turns the root's many-ness into superabundance, not merely an adjective meaning much, a comparative, or a verbal act of multiplying. That is why the word can hold both concrete named-gift and abundant-good readings without syntax forcing a single referent; the local frame only requires a definite gift. The abundance also has a bounded-unbounded pressure: a vast field is packed into one grammatical object. A generosity field makes the gift feel generative rather than passive, while grammar keeps it as the object given. Within the surah, this final gift makes the worship response in 108:2 intelligible and sets the abundance pole answered by the cut-off one in 108:3, while the same root field can contrast received abundance here with rivalry in abundance at 102:1. Its broad aw, interdental th, and final r give the close a full rolling texture; the -ar ending opens the short surah's fawāṣil chain, and recitation links the verb's final recipient directly into the gift noun.\",\"root_display\":\"{{ar:ك ث ر}} ({{tr:k-th-r}})\",\"root_gloss_range\":\"abundance, manyness, increase, outnumbering, rivalry in abundance, much speech or claim, and fruitful plentifulness; the local faʿwal definite noun gathers the abundance field into one gift rather than a rivalry or multiplying act\",\"surface_display\":\"{{ar:ٱلْكَوْثَرَ}} ({{tr:al-kawthar}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:clause-final-landing","source_type":"word_analysis","support_id":"sup_2d4f0985dd3fa18b0424","text":"{\"blocking_evidence\":null,\"headline\":\"final position lands the clause on abundance\",\"reader_payoff\":\"The reader notices that speaker and action create expectation until the final word names the gift and completes the clause.\",\"reason\":\"The object completes the verbal predicate after the opening subject and giving verb, so the final noun is structurally the landing point.\",\"representative_source_ids\":[\"QT-3668564d\",\"QT-793c8259\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:generosity-field","source_type":"word_analysis","support_id":"sup_50718cf6d3ba8b8400d2","text":"{\"blocking_evidence\":null,\"headline\":\"giver-quality field makes the gift generative\",\"reader_payoff\":\"The reader notices that the lexeme's generosity field can make the gift feel generative, while grammar keeps it as the object given.\",\"reason\":\"The row's giver-quality pressure is preserved as lexical coloring, but local syntax identifies the word as the given object rather than a person described as generous.\",\"representative_source_ids\":[\"QS-62795ded\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:gift-object-grammar","source_type":"word_analysis","support_id":"sup_549f461581ed3eabc53c","text":"{\"blocking_evidence\":null,\"headline\":\"accusative noun is the given thing\",\"reader_payoff\":\"The reader notices that the final noun is the gift itself, not a descriptor of the addressee or a detached topic.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلْكَوْثَرَ}} ({{tr:al-kawthar}}) as the explicit accusative object governed by the double-transitive giving verb.\",\"representative_source_ids\":[\"QG-3e3f92d6\",\"QG-d29d1123\",\"QT-793c8259\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"108:1:2:1","source_type":"qac_morpheme","support_id":"sup_5bde672996fab35890f9","text":"{\"lemma_ar\":\"أَعْطَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>aEoTaY`|ROOT:ETw|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"108:1:2:1\",\"qac_word_ref\":\"108:1:2\",\"root_ar\":\"ع ط و\",\"surface_ar\":\"أَعْطَيْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:performative-report","source_type":"word_analysis","support_id":"sup_75efb3bc9150ea04f6be","text":"{\"blocking_evidence\":null,\"headline\":\"declaration carries performative force\",\"reader_payoff\":\"The reader notices that the opening declaration can be heard as enacting the bestowal it reports, while grammar still presents a perfect verbal statement.\",\"reason\":\"The performative reading is preserved as discourse force of the emphatic opening statement, not as a change to the perfect verb's grammar.\",\"representative_source_ids\":[\"QI-ebe93fef\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:na-reprise-into-verb","source_type":"word_analysis","support_id":"sup_76a96097de9a82716e3b","text":"{\"blocking_evidence\":null,\"headline\":\"repeated {{ar:نَا}} ({{tr:nā}}) carries agency into the verb\",\"reader_payoff\":\"The reader notices that the same first-person plural sound and pronoun moves from the opening assertion into the completed act of giving.\",\"reason\":\"The verb's first-person plural subject agreement is syntactically controlled by the opening divine subject, preserving the local reprise as both grammar and sound.\",\"representative_source_ids\":[\"QE-bda547d2\",\"QP-effb7d03\",\"QY-ccac0aaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:fused-pronoun-and-sound","source_type":"word_analysis","support_id":"sup_79ca2c395fec0ad5e393","text":"{\"blocking_evidence\":null,\"headline\":\"fused form makes speaker and assertion inseparable\",\"reader_payoff\":\"The reader notices that the surface word lets emphatic certainty and the divine pronoun arrive as one sustained opening sound.\",\"reason\":\"The QAC grammar identifies the contracted particle-pronoun form, and the acoustic rows preserve a real surface payoff without changing the parse.\",\"representative_source_ids\":[\"QF-419a9d23\",\"QF-c5714d2c\",\"QP-48fd5d20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:na-reprise","source_type":"word_analysis","support_id":"sup_7d5c54d9e01edd06b353","text":"{\"blocking_evidence\":null,\"headline\":\"second {{ar:نَا}} ({{tr:nā}}) reprises the opener\",\"reader_payoff\":\"The reader notices the same divine subject first as asserting speaker and then as acting giver.\",\"reason\":\"The verb carries first-person plural subject agreement syntactically controlled by the opening subject, matching the CRITICAL sound-pronoun reprise.\",\"representative_source_ids\":[\"QE-6aabb3f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:form-iv-caused-possession","source_type":"word_analysis","support_id":"sup_7dc711aa8c4160abe485","text":"{\"blocking_evidence\":null,\"headline\":\"Form IV gives as conferred possession\",\"reader_payoff\":\"The reader notices that the morphology makes the addressee not just touched by an action but installed as holder of the named abundance.\",\"reason\":\"The local Form IV and double-object frame select causing-to-have or granting from the giving branch of {{ar:ع ط و}} ({{tr:ʿ-ṭ-w}}).\",\"representative_source_ids\":[\"QS-642423ce\",\"QS-7656610f\",\"QF-8fe242fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:emphatic-divine-assertion","source_type":"word_analysis","support_id":"sup_92aaf22e424fcd72d3c5","text":"{\"blocking_evidence\":null,\"headline\":\"emphatic divine assertion governs the gift clause\",\"reader_payoff\":\"The reader notices that the ayah begins by assigning certainty and agency to the divine speaker before any gift is named.\",\"reason\":\"QAC and attachment evidence confirm an emphatic particle with attached first-person plural governed subject whose predicate is the full giving statement.\",\"representative_source_ids\":[\"QG-a87a2149\",\"QG-c8ee1d5e\",\"QS-4c01796b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:double-object-transfer","source_type":"word_analysis","support_id":"sup_93bae7179daa5b4aac9b","text":"{\"blocking_evidence\":null,\"headline\":\"one verb distinguishes recipient and gift\",\"reader_payoff\":\"The reader notices that the word itself contains the recipient while still governing the named gift as a separate object.\",\"reason\":\"Attachment evidence marks the object suffix as one direct object and {{ar:ٱلْكَوْثَرَ}} ({{tr:al-kawthar}}) as the explicit object, so the transfer relation is locally forced.\",\"representative_source_ids\":[\"QG-886555f6\",\"QG-f782f7ae\",\"QF-c96897bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:received-not-rivalrous-abundance","source_type":"word_analysis","support_id":"sup_9634eafad184e25c269d","text":"{\"blocking_evidence\":null,\"headline\":\"abundance is received, not multiplied or contested\",\"reader_payoff\":\"The reader notices that this abundance is given as a noun, contrasting with making-many or rivalry in abundance, including the warning field of 102:1.\",\"reason\":\"The local form is not a Form II multiplying verb or Form VI rivalry form; those branches survive as contrast that sharpens the received-gift sense.\",\"representative_source_ids\":[\"QS-dbd17092\",\"QF-5735f66d\",\"QI-1fd2d29d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:definite-hapax-identifiability","source_type":"word_analysis","support_id":"sup_985b3f574c01556537a8","text":"{\"blocking_evidence\":null,\"headline\":\"definite article makes a unique lexeme identifiable\",\"reader_payoff\":\"The reader notices that the article lets a one-time word arrive as the known or quintessential gift instead of an undefined kind of abundance.\",\"reason\":\"The noun is definite and corpus-unique in the supplied data; local grammar makes it identifiable through article, object role, and intensive form rather than repeated Quranic usage.\",\"representative_source_ids\":[\"QG-9fd76e3d\",\"QG-eb167374\",\"QH-5ba6c870\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:generosity-theology-synthesis","source_type":"word_analysis","support_id":"sup_b865aa060dc9f5a6a0db","text":"{\"blocking_evidence\":null,\"headline\":\"broad theological synthesis repeats retained payoffs\",\"reader_payoff\":null,\"reason\":\"The useful claims about emphatic launch, divine plural, and completed giving are already preserved in more specific topics; the remaining theological expansion adds no separate word-level payoff.\",\"representative_source_ids\":[\"MG-98d6f5e6\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:phonetic-and-fawasil-texture","source_type":"word_analysis","support_id":"sup_bf6c3a68ff80e89c0cc7","text":"{\"blocking_evidence\":null,\"headline\":\"sound gives the gift a full landing\",\"reader_payoff\":\"The reader notices that the closing sound gives the gift acoustic weight and starts the short surah's matching end-rhyme channel.\",\"reason\":\"The phonetic rows describe surface recitation and same-surah endings without altering the local grammar or lexical sense.\",\"representative_source_ids\":[\"QP-39f9e8dc\",\"QP-712d5603\",\"QP-9ed0111b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1","source_type":"word_analysis","support_id":"sup_c50acf14f18f35228890","text":"{\"gloss_range\":\"emphatic divine self-reference that asserts the whole giving clause as established fact\",\"prose\":\"{{ar:إِنَّا}} ({{tr:innā}}) opens the surah by fusing emphatic assertion with the divine speaker. The attached first-person plural is not an impersonal marker; it is the governed subject of the emphatic particle, so agency is fixed before the giving verb begins. Its doubled nūn tightens the assertion, and the long final ā lets the divine pronoun linger rather than sounding clipped. Its certainty scopes over the whole clause, making the gift a declared fact rather than a tentative report. The plural divine speaker is then aimed at the singular recipient in {{ar:أَعْطَيْنَٰكَ}} ({{tr:aʿṭaynāka}}), and the repeated {{ar:نَا}} ({{tr:nā}}) carries the same agency from assertion into action. The opening therefore supplies the surah's first premise: divine certainty, divine speaker, and completed gift stand together before the response commanded in 108:2 and the adversary reversal in 108:3.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّا}} ({{tr:innā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:surah-launch-and-response-arc","source_type":"word_analysis","support_id":"sup_d21a808ace598f1e3a15","text":"{\"blocking_evidence\":null,\"headline\":\"opening assertion launches gift before response\",\"reader_payoff\":\"The reader notices that the surah starts from declared gift, then moves to commanded response in 108:2 and adversary reversal in 108:3.\",\"reason\":\"The emphatic clause is syntactically forced as the opening statement, and the CRITICAL rows give a concrete same-surah sequence from 108:1 to 108:2 and 108:3.\",\"representative_source_ids\":[\"QT-189608e1\",\"MI-7885ab8d\",\"MT-801d3919\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:referential-openness","source_type":"word_analysis","support_id":"sup_d6469a1da04f84dde08e","text":"{\"blocking_evidence\":null,\"headline\":\"river and abundant-good readings remain locally possible\",\"reader_payoff\":\"The reader notices that a concrete named gift and broader abundant good can remain in play because syntax only requires a definite object of giving.\",\"reason\":\"The local grammar does not force a single referent beyond definite gift-object status; broad lists of possible referents are therefore narrowed to the river or abundant-good range actually pressed by the CRITICAL rows.\",\"representative_source_ids\":[\"QS-629ec952\",\"QS-cfb15fd9\",\"MH-43579e51\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"108:1:3:2","source_type":"qac_morpheme","support_id":"sup_dbd8457319a724878f4b","text":"{\"lemma_ar\":\"كَوْثَر\",\"morph_features\":\"STEM|POS:N|LEM:kawovar|ROOT:kvr|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"108:1:3:2\",\"qac_word_ref\":\"108:1:3\",\"root_ar\":\"ك ث ر\",\"surface_ar\":\"كَوْثَرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2","source_type":"word_analysis","support_id":"sup_dd9edcee0c013b02b7f9","text":"{\"gloss_range\":\"completed active Form IV granting that causes the addressed recipient to have the named gift\",\"prose\":\"{{ar:أَعْطَيْنَٰكَ}} ({{tr:aʿṭaynāka}}) is the clause's hinge: the emphatic divine speaker of {{ar:إِنَّا}} ({{tr:innā}}) becomes the active giver, and the singular addressee is marked inside the same word. Its perfect aspect presents the grant as accomplished before any response is commanded. Form IV makes the giving causative, so the verb does more than report transfer; it causes the addressed recipient to have {{ar:ٱلْكَوْثَرَ}} ({{tr:al-kawthar}}). The double-object frame keeps the recipient and the gift distinct, while the affixes compress subject, action, and recipient into one verbal form. The same first-person plural marker heard in the opener appears again here, first as asserting speaker and now as acting giver. Lexical pressure from yielding or reaching makes the grant feel like productive outflow from a source that generates abundance rather than losing a finite object, and like a gift actively extended toward the -ka recipient; local grammar still keeps grant or bestowal as the selected sense. In the surah's opening speech event, the declaration can be heard as enacting the bestowal it reports. The verb also points forward: the completed gift becomes the premise for the worship command in 108:2, and its Form IV recurrence contrasts with the future promise of giving in 93:5.\",\"root_display\":\"{{ar:ع ط و}} ({{tr:ʿ-ṭ-w}})\",\"root_gloss_range\":\"giving, handing over, causing possession, productive yielding, reaching toward, asking for a gift, compliant yielding, and overreaching; the local Form IV double-object frame selects divine granting and conferred possession\",\"surface_display\":\"{{ar:أَعْطَيْنَٰكَ}} ({{tr:aʿṭaynāka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:root-family-compression","source_type":"word_analysis","support_id":"sup_e46d41b249a4eaefd0e2","text":"{\"blocking_evidence\":null,\"headline\":\"common root field crystallizes into one rare form\",\"reader_payoff\":\"The reader notices that a widely distributed abundance root is concentrated into a single unrepeated intensive gift name.\",\"reason\":\"The contextual profile marks the local noun as low-occurrence while CRITICAL distribution rows contrast that unique form with the broader {{ar:ك ث ر}} ({{tr:k-th-r}}) family.\",\"representative_source_ids\":[\"QS-d3e8c580\",\"QI-23ed809b\",\"QY-6e065b88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:distribution-and-echo","source_type":"word_analysis","support_id":"sup_e72c900b18661f8b7601","text":"{\"blocking_evidence\":null,\"headline\":\"rare Form IV giving contrasts future giving in 93:5\",\"reader_payoff\":\"The reader notices that this giving form is a marked local selection and that its completed aspect sharpens against the promised future giving in 93:5.\",\"reason\":\"Contextual profiles show low occurrence for this exact root-form and support aspect/frame comparison, while the echo remains contrastive rather than controlling the local parse.\",\"representative_source_ids\":[\"QI-dcdd736c\",\"QE-ce1f53fa\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:1:divine-plural-singular-recipient","source_type":"word_analysis","support_id":"sup_e9240a8073921884bf07","text":"{\"blocking_evidence\":null,\"headline\":\"plural divine speaker faces one addressee\",\"reader_payoff\":\"The reader notices the asymmetry between expansive divine self-reference and the singular addressed recipient, while the local grammar keeps the plural as divine speaker morphology.\",\"reason\":\"The local evidence supports majestic first-person plural and second-person singular recipient; broader speculation about plural agency is not needed for the local parse.\",\"representative_source_ids\":[\"MG-78abceaa\",\"QI-4aa0abce\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:completed-active-grant","source_type":"word_analysis","support_id":"sup_f83d90ee8ccc896ad323","text":"{\"blocking_evidence\":null,\"headline\":\"active perfect presents completed divine giving\",\"reader_payoff\":\"The reader notices that the grant is grammatically complete and actively assigned to the divine giver, not merely received or promised.\",\"reason\":\"QAC and attachment evidence confirm a perfect active Form IV verb with first-person plural subject agreement and no passive suppression of the giver.\",\"representative_source_ids\":[\"QG-533ce2b7\",\"QG-fd4c0518\",\"QF-a07c8736\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:3:intensive-fawal-superabundance","source_type":"word_analysis","support_id":"sup_fc2b3741534e66d69bd6","text":"{\"blocking_evidence\":null,\"headline\":\"faʿwal form intensifies abundance\",\"reader_payoff\":\"The reader notices that the word turns abundance itself into the named object given, not an ordinary adjective or comparison.\",\"reason\":\"QAC identifies the faʿwal intensive nominal pattern from {{ar:ك ث ر}} ({{tr:k-th-r}}), and the local noun has no following head noun.\",\"representative_source_ids\":[\"QS-3c680e9c\",\"QF-05706964\",\"QF-e14855c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"108:1:2:lexical-image-pressure","source_type":"word_analysis","support_id":"sup_ff2f0ab2daa1dd35fda4","text":"{\"blocking_evidence\":null,\"headline\":\"yielding and reaching color the grant\",\"reader_payoff\":\"The reader notices the grant as productive outflow and directed extension, while the local frame still selects bestowal rather than a free taking or reaching sense.\",\"reason\":\"V4 separates taking, giving, serving, asking, yielding, and overreaching branches; the local Form IV double-object grant licenses giving while allowing compatible yield and directed-transfer pressure as image, not replacement sense.\",\"representative_source_ids\":[\"QS-523d03f4\",\"QS-79e08bc9\",\"QS-973795ce\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001028/B002","root_001286/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Literal handing-over supplies a completed donor-to-recipient transfer and makes the plenty recipient-directed.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001286","role":"Abundance and numerical increase supply content that can keep multiplying rather than a merely honorific object.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"changed_reading":{"after":"A multiplying plenitude has been decisively placed with the addressee.","before":"A large or excellent good is announced."},"confidence":"strong","focus_anchor":"The completed first-person-plural giving construction and its definite direct object.","mechanism":"Handing-over combines with numerical increase so that the focus does not merely announce that much good exists: it presents multiplying plenty as already transferred into the addressee's reach.","model_id":"base_transferred_plenitude"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_transferred_plenitude","source_type":"hft","support_id":"sup_876e7255b1214818ae98","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001028/B002","root_001028/B007","root_001286/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Giving keeps the advantage bestowed rather than seized by the recipient.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_001028","role":"Outdoing in reciprocal dealing supplies one side of a contest whose balance can be reversed.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001286","role":"Outnumbering and rivalry in abundance turn quantity into comparative social force.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"changed_reading":{"after":"The gift creates bestowed preponderance in contests of number, wealth, speech, or standing.","before":"The gift is quantitatively large."},"confidence":"medium","focus_anchor":"The same giving event and the abundance noun, read through their shared competitive branch potential.","mechanism":"The focus roots both contain outdoing images: one in mutual dealing and the other through number, wealth, or standing. Their conjunction makes the gift an intervention in a comparative field, granting preponderance rather than only adding possessions.","model_id":"base_comparative_preponderance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_comparative_preponderance","source_type":"hft","support_id":"sup_cd12a1b3acdc8e6a1985","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّآ أَعْطَيْنَٰكَ ٱلْكَوْثَرَ","ayah_ref":"108:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001028/B002","root_001286/B006","root_001286/B007"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001028","role":"Handing-over makes the compact source itself the bestowed object.","root":"ع ط و","source_ref":"108:1","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001286","role":"Palm pith or inflorescence supplies a small fertile structure carrying future proliferation.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001286","role":"Clustering supplies concentrated gathering as the organization of the latent abundance.","root":"ك ث ر","source_ref":"108:1","source_word_indices":["3"]}],"changed_reading":{"after":"The object can be a concentrated fertile source whose compact gathering unfolds into abundance.","before":"The object names an already expanded quantity."},"confidence":"exploratory","focus_anchor":"The transferred object as named by the abundance root's palm-growth and clustering branches.","mechanism":"Palm pith or inflorescence and clustering recast abundance as a compact generative node. What is handed over need not be an already expanded heap; it can be a concentrated source from which plurality unfolds.","model_id":"base_concentrated_fecundity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_concentrated_fecundity","source_type":"hft","support_id":"sup_961914d8688ce357ed7c","trust":"legacy_unbound"}]}
</lane_packet_json>
