# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:13**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_13/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:13",
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
{"branch_registry":[{"boundary":"Dal fiziksel yükseltme çekirdeğini kapsar; saygınlık, haber yayma ve özel yürüyüş anlamları bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_79fae44bab9eac278634","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"bir şeyi yukarı kaldırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi bulunduğu konumdan yukarı taşımak ve böylece yüksekliğini artırmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapıyı daha yüksek olacak biçimde uzatmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin bulunduğu yerden daha yüksek bir konuma taşındığı genel fiziksel kullanım için uygundur.","boundary_detail":"Dal fiziksel yükseltme çekirdeğini kapsar; saygınlık, haber yayma ve özel yürüyüş anlamları bu sınıra girmez.","branch_image_ar":"إعلاء الشيء","concept_gloss":"bir şeyi yukarı kaldırmak","contextual_glosses":[{"applicability":"Bir binanın boyunun artırıldığı yapı bağlamındaki özel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapının yüksekliğini artırma ve uzatma sonucunu korur."},"facet_ids":["F002"],"text":"yapıyı yükseltmek","usage_role":"contextual"}],"definition":"Bir şeyi bulunduğu yerden daha yukarı bir konuma taşımak, aşağı indirme yönünün tersine hareket ettirmektir. Yapı bağlamında bu çekirdek, yapıyı yükseltip uzatma biçiminde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi bulunduğu konumdan yukarı taşımak ve böylece yüksekliğini artırmak."},{"facet_id":"F002","role":"specialization","statement":"Yapıyı daha yüksek olacak biçimde uzatmak."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca kendiliğinden gerçekleşen bir hareket gibi anlaşılabilir.","fit":"narrowing","loses":"Bir etkileyenin nesneyi yukarı taşıması ve yapı yükseltme ayrıntısını kaybeder.","preserves":"Daha yüksek bir konuma geçme yönünü korur."},"text":"yükselmek"}],"identity_rationale":"Kaynak ifadesi, bir şeyi bulunduğu yerden yukarı taşımayı aşağı indirmenin karşıtı olarak verir; yapı söz konusu olduğunda yükseltip uzatmayı da bu çekirdeğe bağlı özel bir kullanım olarak gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bulunduğu yerden yukarı kaldırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendiliğinden yükselmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yapıyı yükseltip uzatmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"üst üste serilmiş döşekler"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu göğe çıkarmak veya onurlandırmak"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"bir şeyi eliyle kaldırmak"}],"lexicalization_note":"Çıplak kullanım fiziksel olarak yukarı kaldırmayı anlatır; yapı, döşek ve başka kalıplara bağlı kullanımlar bu çekirdeğin özel gerçekleşmeleri olarak ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; düşey hareketin karşıtı, genel yükselme ve üstte bulunma ile sınırı en açık gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal konumu yukarı doğru değiştirirken komşu dal nesneyi elden yere veya daha aşağı, kararlaştırılmış bir konuma bırakır.","focus_only":"Nesneyi daha yüksek bir konuma taşır.","gloss":"yukarı kaldırmak ve aşağı bırakmak","neighbor_only":"Nesneyi daha alçak ya da belirlenmiş bir yere bırakır.","neighbor_ref":"root_001657/B001","relation_type":"antonym","shared_zone":"İki dal da bir nesnenin düşey konumunu değiştiren hareketleri anlatır."},{"boundary_match":"partial","distinction":"Odak dal özellikle fiziksel bir nesnenin yukarı alınmasına dayanır; komşu dal ise ettirgenlik aramadan genel yükselme ve yücelmeyi daha geniş biçimde kapsar.","focus_only":"Bir nesneyi yerinden yukarı taşıma eylemini ve yapı yükseltmeyi belirginleştirir.","gloss":"kaldırmak ve yükselmek","neighbor_only":"Bulutun yükselmesi gibi daha geniş kendiliğinden yükselme ve yücelme durumlarını da kapsar.","neighbor_ref":"root_001502/B001","relation_type":"near_synonym","shared_zone":"Her ikisinin çekirdeğinde daha yüksek bir konuma geçiş veya geçirme bulunur."},{"boundary_match":"partial","distinction":"Odak dal bir konum değişikliği eylemidir; komşu dal ise hareket gerektirmeyen bir yer ve yön ilişkisini belirtir.","focus_only":"Daha yüksek konuma götüren hareketi anlatır.","gloss":"yukarı kaldırmak ve üstte olmak","neighbor_only":"Bir şeyin üstte veya yukarı yönde bulunma ilişkisini anlatır.","neighbor_ref":"root_001188/B001","relation_type":"near_neighbor","shared_zone":"İki dal da düşey yükseklik ve üst-alt eksenini paylaşır."}],"source_phrase_ar":"رفعت الشيء رفعا وهو خلاف الخفض (maqayis;ayn); الرفع ضد الخفض (tahdhib); الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها (mufradat); في البناء إذا طولته (mufradat)","source_summary":"Kanıtlar fiziksel yukarı taşıma ile aşağı indirme arasındaki karşıtlıkta birleşir ve yapı yükseltmeyi bu yönlü değişimin özel bir uygulaması olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إعلاء الأجسام أو البناء وإزالة الشيء عن موضعه إلى علو","what_is_not_ar":"ليس رفع القدر ولا الإبلاغ ولا السير الخاص"},"support_links":["sup_4e77e557afef2f9be10a"]},{"boundary":"Dal toplumsal veya simgesel değerin yükselmesini kapsar; fiziksel taşıma ve yalnızca ün kazanma bu çekirdeğin yerini tutmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B002","candidate_links":[{"candidate_id":"cand_e40a587395ace4f2290b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"saygınlığı yüksek olmak veya yükseltmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yüksek saygınlığa ve onurlu bir konuma sahip olması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin, anılışın veya konumun saygınlığını artırıp onu yüceltmek."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem onurlu ve yüksek konumlu olma durumunu hem de birine ya da bir şeye bu değeri kazandırmayı kapsar.","boundary_detail":"Dal toplumsal veya simgesel değerin yükselmesini kapsar; fiziksel taşıma ve yalnızca ün kazanma bu çekirdeğin yerini tutmaz.","branch_image_ar":"علو القدر","concept_gloss":"saygınlığı yüksek olmak veya yükseltmek","contextual_glosses":[{"applicability":"Bir kişinin sahip olduğu saygın konumu niteleyen durum kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin saygınlığını ve yüksek toplumsal değerini korur."},"facet_ids":["F001"],"text":"onurlu ve yüksek konumlu","usage_role":"contextual"},{"applicability":"Bir kişinin, anılışın, belgenin veya yerin saygınlığının artırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değeri ve saygınlığı etkin biçimde artırma yönünü korur."},"facet_ids":["F002"],"text":"değerini yüceltmek","usage_role":"contextual"}],"definition":"Bir kişinin, anılışın veya konumun değer ve saygınlık bakımından yüksek olması ya da bu yüksek konuma çıkarılmasıdır. Aşağılanmanın karşıtıdır ve fiziksel yükseklik bildirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yüksek saygınlığa ve onurlu bir konuma sahip olması."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin, anılışın veya konumun saygınlığını artırıp onu yüceltmek."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Saygınlık gerektirmeyen sıradan tanınmışlık anlamını ekler.","collision":"Kötü bir nedenle tanınmış kişi de ünlü olabilir.","fit":"displacement","loses":"Onur, yüksek değer ve aşağılanmaya karşıt saygınlık çekirdeğini kaybeder.","preserves":"Bir kişinin başkalarınca tanınması ihtimalini korur."},"text":"ünlü olmak"}],"identity_rationale":"Kaynak ifadesi kişinin onurlu ve yüksek konumlu oluşunu, aşağılanmanın karşıtı olan saygınlığı ve bir anılışın ya da konumun yüceltilmesini aynı değer ekseninde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"değerli ve onurlu döşekler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"anılışını yüceltmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"konumunu ve saygınlığını yükseltmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"saygın ve yüksek konumlu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yüksek saygınlık ve onur"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir topluluğu alçaltıp diğerini yükselten"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu göğe çıkarmak veya onurlandırmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"değerli ve onurlandırılmış sayfalar"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"evleri onurlandırıp yüceltmek"}],"lexicalization_note":"Çıplak biçimler yüksek saygınlık durumunu anlatır; anılışı, konumu, belgeleri veya yapıları yüceltmeye bağlı kalıplar ayrı bağlamsal gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; onur alanındaki en yakın komşu, karşıt değer yönü ve iyi ünle karışma riski sınırı açıklayan üç ilişki olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem yüksek saygınlık durumunu hem de onu artırma eylemini işler; komşu dal yüksek onur alanını ve seçkinlik adlarını daha geniş biçimde kapsar.","focus_only":"Saygınlığı artıran eylemi ve anılış ya da konum gibi nesnelerin yüceltilmesini de kapsar.","gloss":"saygınlığı yükseltmek ve yüksek onur","neighbor_only":"Yüksek toplumsal tabakayı ve seçkin kişileri adlandıran daha geniş kullanımları kapsar.","neighbor_ref":"root_001042/B002","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde yüksek değer, onur ve saygınlık bulunur."},{"boundary_match":"opposed","distinction":"Odak dal değer ve onur kazandırırken komşu dal bunları azaltan küçümseme yönünde işler.","focus_only":"Kişinin veya konumun değerini ve saygınlığını yükseltir.","gloss":"yüceltmek ve küçümsemek","neighbor_only":"Kişiyi küçümseyip değerini düşürür.","neighbor_ref":"root_000414/B006","relation_type":"antonym","shared_zone":"İki dal da bir kişiye verilen toplumsal değerin yönünü belirler."},{"boundary_match":"partial","distinction":"Odak dal kişinin değer ve onur düzeyine ilişkindir; komşu dal ise bu değerin toplumda yayılmış iyi bir ün olarak görünmesine odaklanır.","focus_only":"Saygınlığın kendisini ve onu yükseltme eylemini anlatır.","gloss":"yüksek saygınlık ve iyi ün","neighbor_only":"İnsanlar arasında yayılan iyi ünü ve olumlu tanınmışlığı anlatır.","neighbor_ref":"root_000890/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olumlu toplumsal değerlendirme alanında buluşur."}],"source_phrase_ar":"رفع الرجل يرفع رفاعة فهو رفيع إذا شرف (ayn;tahdhib); رجل رفيع أي شريف (sihah); الرفعة نقيض الذلة (tahdhib); في الذكر إذا نوهته (mufradat); في المنزلة إذا شرفتها (mufradat)","source_summary":"Kanıtlar yüksek saygınlık ile aşağılanma arasındaki karşıtlığı temel alır; kişinin onurlu oluşunu ve anılış ya da konumun yüceltilmesini bu temel çevresinde birleştirir.","sources":["AY","SI","TA","MU"],"what_is_ar":"تشريف الشخص أو الذكر أو المنزلة وعلو القدر","what_is_not_ar":"ليس النقل الحسي ولا رفع الزرع ولا رفع الخبر"},"support_links":["sup_90014bef26d3d87ae120"]},{"boundary":"Dal genel hız kavramı değil, binek hayvanının belirli yoğunluk ve aralıkta gerçekleşen yürüyüş biçimidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"bineğin orta-üst hızda ilerlemesi veya ilerletilmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Binek hayvanının ağır yürüyüş ile tam koşu arasında güçlü ve hızlı ilerlemesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bineğin yürüyüşünü olağandan daha güçlü ve hızlı hale getirmek."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Binek hayvanının ağır yürüyüş ile tam koşu arasındaki güçlü gidişini ve bu gidişe yöneltilmesini birlikte anlatır.","boundary_detail":"Dal genel hız kavramı değil, binek hayvanının belirli yoğunluk ve aralıkta gerçekleşen yürüyüş biçimidir.","branch_image_ar":"رفع السير","concept_gloss":"bineğin orta-üst hızda ilerlemesi veya ilerletilmesi","contextual_glosses":[{"applicability":"Hayvanın gidiş biçiminin anlatıldığı, tam koşuya varmayan hızlı yürüyüş bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hızın ağır yürüyüş ile tam koşu arasındaki özel yerini açıkça belirtmez.","preserves":"İlerleyişin güçlü ve hızlı niteliğini korur."},"facet_ids":["F001"],"text":"güçlü ve hızlı ilerlemek","usage_role":"contextual"}],"definition":"Bir binek hayvanının ağır yürüyüşten hızlı, tam koşudan daha düşük bir hızla güçlü biçimde ilerlemesidir. Aynı alan, hayvanın yürüyüşünü bu yoğunluğa çıkarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Binek hayvanının ağır yürüyüş ile tam koşu arasında güçlü ve hızlı ilerlemesi."},{"facet_id":"F002","role":"specialization","statement":"Bineğin yürüyüşünü olağandan daha güçlü ve hızlı hale getirmek."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tam koşuyu ve binek dışındaki her türlü koşuyu sınırsız biçimde kapsar.","collision":"Kaynakta belirtilen ara yürüyüş düzeyini en üst hızla karıştırır.","fit":"broadening","loses":null,"preserves":"Hızlı ilerleme yönünü korur."},"text":"koşmak"}],"identity_rationale":"Kaynak ifadesi, bineğin ağır yürüyüşten daha hızlı fakat tam koşudan daha düşük bir gidişini ve hayvanın yürüyüşünü belirgin biçimde hızlandırmayı birlikte gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"devenin yürüyüşünü hızlandırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ağır yürüyüşle tam koşu arasında hızlı gidiş"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hızı yer yer artan koşu"}],"lexicalization_note":"Biçim birimleri belirli bir yürüyüş türünü adlandırır; kalıba bağlı kullanım ise bineğin yürüyüşünü bu düzeye çıkarma eylemini ayrı tutar.","neighbor_coverage_note":"Bütün aday yürüyüş kartları karşılaştırıldı; hız aralığı, deveye özgü atılganlık ve beden duruşu bakımından en açıklayıcı üç sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hızın alt ve üst sınırını belirli bir aralıkta tutar; komşu dal ise belirli bir aralık şartı olmadan hızlı binek yürüyüşlerini kapsar.","focus_only":"Ağır yürüyüş ile tam koşu arasında belirli bir hız düzeyi kurar.","gloss":"ara hızlı yürüyüş ve hızlı binek gidişi","neighbor_only":"Binek hayvanının çeşitli hızlı yürüyüşlerini ve onu genel olarak hızlandırmayı kapsar.","neighbor_ref":"root_001628/B001","relation_type":"near_synonym","shared_zone":"İki dal da binek hayvanının hızlı ilerlemesi ve sürücünün onu hızlandırmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal hız derecesini ağır yürüyüş ile tam koşu arasında tanımlar; komşu dal develerin peş peşe atılgan ilerleyiş biçimine odaklanır.","focus_only":"Binek türleri arasında kullanılabilen ve tam koşunun altında kalan bir hız düzeyidir.","gloss":"güçlü binek yürüyüşü ve atılgan deve gidişi","neighbor_only":"Özellikle develerin ardışık ve atılgan ilerleyişini öne çıkarır.","neighbor_ref":"root_000676/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da devenin olağandan hızlı ve güçlü yürüyüşünü anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü hız derecesidir; komşu dalın ayırıcı yönü ise hızlı gidişe eşlik eden alçak boyun duruşudur.","focus_only":"Yürüyüşü hız aralığıyla tanımlar.","gloss":"hız derecesi ve boyun alçaltarak gidiş","neighbor_only":"Boyunların alçaltılması gibi belirli bir beden duruşunu ve ciddi gidişi şart koşar.","neighbor_ref":"root_000419/B004","relation_type":"near_neighbor","shared_zone":"İki dal da binek hayvanlarının güçlü ve hızlı ilerleyişini betimler."}],"source_phrase_ar":"مرفوع الناقة في سيرها خلاف الموضوع (maqayis); المرفوع من حضر الفرس والبرذون دون الحضر وفوق الموضوع (ayn;tahdhib); رفع البعير في السير أي بالغ (sihah); مرفوع السير شديدة (mufradat)","source_summary":"Kanıtlar bu yürüyüşü ağır gidişin üstünde, tam koşunun altında konumlandırır; bazı ifadeler hız aralığını, bazıları ise yürüyüşü artırma eylemini öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اشتداد سير الدابة بين البطء والحضر ورفع البعير في سيره","what_is_not_ar":"ليس علو المنزلة ولا حمل الزرع"},"support_links":[]},{"boundary":"Dal bir şeyi yaklaştırma veya yetkili önüne sunma eylemidir; haberin kamuya yayılması ayrı bir anlamdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B004","candidate_links":[{"candidate_id":"cand_fb7373c014385562acde","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"yaklaştırmak veya yetkili önüne sunmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bulunduğu yere göre yakına getirmek veya öne almak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiyi, davayı veya anlatılan işi karar verecek yetkilinin önüne sunmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem genel öne getirme eylemini hem de kişi ya da işin karar verecek makama sunulmasını kapsar.","boundary_detail":"Dal bir şeyi yaklaştırma veya yetkili önüne sunma eylemidir; haberin kamuya yayılması ayrı bir anlamdır.","branch_image_ar":"التقريب والتقديم","concept_gloss":"yaklaştırmak veya yetkili önüne sunmak","contextual_glosses":[{"applicability":"Bir kişi veya işin yönetici ya da yargıç tarafından görülmek üzere sunulduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yetkiliye doğru yaklaştırma ve değerlendirmeye sunma işlemini korur."},"facet_ids":["F002"],"text":"önüne getirmek","usage_role":"contextual"}],"definition":"Bir şeyi daha yakına getirmek veya öne almaktır. Yönetim ve yargı bağlamında kişi, dava ya da anlatılan iş yetkili önüne çıkarılarak değerlendirmeye sunulur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bulunduğu yere göre yakına getirmek veya öne almak."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiyi, davayı veya anlatılan işi karar verecek yetkilinin önüne sunmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnızca sözlü ya da yazılı bilgi verme anlamını ekler.","collision":"Haber yayma dalıyla kolayca karışır.","fit":"displacement","loses":"Kişiyi veya işi yaklaştırıp yetkili önüne çıkarma işlemini kaybeder.","preserves":"Bir işin yetkiliye ulaşması sonucunu kısmen korur."},"text":"bildirmek"}],"identity_rationale":"Kaynak ifadesi genel yaklaştırma çekirdeğini açıkça verir ve kişi ya da anlatılan bir işi yönetici veya yargı yetkisi olan kimsenin önüne getirmeyi bunun kurumsal özel kullanımı olarak gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kullanacaklara yaklaştırılmış döşekler"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yaklaştırma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yönetici veya yargıç önüne sunmak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yargılanması için yetkili önüne çıkarmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dilekçesini veya şikayetini sunmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onu iki perdenin bulunduğu yere kadar ilerletmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir topluluğu savaşta öne sürmek"}],"lexicalization_note":"Çıplak biçim yaklaştırmayı anlatır; kişiyi, davayı veya anlatılan işi bir yetkilinin önüne sunan kalıplar bu çekirdeğin kurumsal özel kullanımlarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; haber yayma, genel yakınlık ve bir sonuca araçla ulaşma dalları sunma eyleminin sınırını en iyi gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın hedefi karar verecek belirli bir yetkilidir ve sunma işlemi öne çıkar; komşu dalın çekirdeği ise haberin görünür ve yaygın hale gelmesidir.","focus_only":"Kişi veya işi belirli bir yetkilinin önüne getirir.","gloss":"yetkiliye sunmak ve haberi yaymak","neighbor_only":"Haberi belirli bir karar makamıyla sınırlamadan açığa çıkarıp yayar.","neighbor_ref":"root_000582/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bir içeriğin başka kişilere ulaştırılması görülebilir."},{"boundary_match":"partial","distinction":"Odak dal genel yaklaştırmaya ek olarak kurumsal sunmayı içerir; komşu dal ise fiziksel ve ilişkisel yakınlığın daha geniş alanına yayılır.","focus_only":"Yetkili önüne kişi, dava veya anlatılan iş sunma kullanımını içerir.","gloss":"yaklaştırmak ve yakın olmak","neighbor_only":"Yakınlık, akrabalık ve iki şey arasında yakınlaşma gibi daha geniş ilişkileri kapsar.","neighbor_ref":"root_000493/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyi daha yakın konuma getirme anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal sunulan kişi ya da işin yetkiliye yaklaştırılmasına dayanır; komşu dal ise sonuca götüren bir aracın veya dayanağın kullanılmasına dayanır.","focus_only":"Kişiyi veya işi bizzat yetkilinin önüne çıkarır.","gloss":"yetkili önüne sunmak ve araç ileri sürmek","neighbor_only":"Bir sonuca ulaşmak için kanıt, hak, mal veya aracı ileri sürer.","neighbor_ref":"root_000485/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bir hüküm veya istenen sonuç karşısında bir şeyi öne getirmeyi içerir."}],"source_phrase_ar":"الرفع تقريب الشيء (maqayis;sihah); رفعته للسلطان (maqayis); رفعته إلى السلطان (sihah); رفعت فلانا إلى الحاكم أي قدمته إليه (tahdhib); رفعت قصتي قدمتها (tahdhib)","source_summary":"Kanıtlar genel yaklaştırma ile yönetici ya da yargıç önüne sunmayı aynı öne getirme yönünde birleştirir; kurumsal örnek çekirdeği bütünüyle daraltmaz.","sources":["MQ","SI","TA"],"what_is_ar":"تقريب الشيء أو تقديم الشخص أو القصة إلى سلطان أو حاكم","what_is_not_ar":"ليس إذاعة الخبر ولا علو المكان"},"support_links":["sup_048710b7584aad032ae4"]},{"boundary":"Dal haberin görünür ve yaygın hale gelmesini gerektirir; yalnızca bir yetkiliye sunmak veya haber istemek yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B005","candidate_links":[{"candidate_id":"cand_f2dc90488c5856ca37b4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"haberi açığa çıkarıp yaymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir haberi açığa çıkarıp insanlar arasında yaymak."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aktardığı haberi başkalarına ulaştırıp yayan topluluk."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir haberin gizli veya dar çevrede kalmaktan çıkıp başkalarına duyurulduğu bağlamlarda uygundur.","boundary_detail":"Dal haberin görünür ve yaygın hale gelmesini gerektirir; yalnızca bir yetkiliye sunmak veya haber istemek yeterli değildir.","branch_image_ar":"إذاعة الخبر","concept_gloss":"haberi açığa çıkarıp yaymak","contextual_glosses":[{"applicability":"Haberin bir topluluk aracılığıyla birçok kişiye ulaştırıldığı akıcı metin bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Daha önce gizli olan içeriği açığa çıkarma ayrıntısını açıkça söylemez.","preserves":"Haberi başkalarına ulaştırma ve yayma işlemini korur."},"facet_ids":["F001","F002"],"text":"duyurup yaymak","usage_role":"contextual"}],"definition":"Bir haberi gizli veya sınırlı kaldığı durumdan çıkararak başkalarının bilgisine açmak ve yaymaktır. Haberi taşıyıp duyuran topluluk bu eyleme bağlı bir kullanım oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir haberi açığa çıkarıp insanlar arasında yaymak."},{"facet_id":"F002","role":"associated_use","statement":"Aktardığı haberi başkalarına ulaştırıp yayan topluluk."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tek kişiye özel ve yayılmayan her türlü bilgilendirmeyi de kapsar.","collision":"Açığa çıkarma ve yayma koşulları görünmez hale gelir.","fit":"broadening","loses":null,"preserves":"Bir içeriği başkasının bilgisine ulaştırmayı korur."},"text":"haber vermek"}],"identity_rationale":"Kaynak ifadesi bir şeyi, özellikle gizli kalmış bir haberi açığa çıkarıp yaymayı ve bunu aktaran bir topluluğu açıkça aynı duyurma alanında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"açığa çıkarıp yayma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinin yönetici hakkındaki haberini yaymak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iletileni duyurup yayan topluluk"}],"lexicalization_note":"Çıplak biçim açığa çıkarıp yaymayı anlatır; belirli kişi ve yönetici ilişkisine bağlı kalıp ile haber taşıyan topluluk adı ayrı gerçekleşmeler olarak korunur.","neighbor_coverage_note":"Bütün aday haber ve iletişim kartları değerlendirildi; yayılma durumu, haberin kendisi ve yetkiliye sunma eylemi en yararlı üç sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal duyuran kişinin veya topluluğun etkin yayma eylemine dayanır; komşu dal ise haberin yaygınlaşma durumunu ve konuşmanın genişlemesini de kapsar.","focus_only":"Bir haberi etkin biçimde açığa çıkarıp yaymayı anlatır.","gloss":"haberi yaymak ve haberin yayılması","neighbor_only":"Sözün veya haberin taşarcasına kendiliğinden yayılmasını ve konuşmaya dalmayı da kapsar.","neighbor_ref":"root_001192/B003","relation_type":"near_synonym","shared_zone":"İki dalda da haberin başlangıçtaki dar çevresinin dışına çıkması bulunur."},{"boundary_match":"partial","distinction":"Odak dal içeriğin yaygın hale getirilmesine odaklanır; komşu dal ise haber türündeki içeriği ve bildirme ilişkisini, yayılma şartı olmadan kapsar.","focus_only":"Haberin açığa çıkarılıp yayılma sürecini anlatır.","gloss":"haberi yaymak ve haber","neighbor_only":"Haberin kendisini ve onu bildirme ya da öğrenme ilişkilerini anlatır.","neighbor_ref":"root_001464/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal haberin kişiler arasında bilgi olarak aktarılması alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda amaç haberin görünür ve yaygın olmasıdır; komşu dalda amaç belirli kişi veya işin yetkili tarafından değerlendirilmesidir.","focus_only":"Haberi geniş bir çevrenin bilgisine açar.","gloss":"haberi yaymak ve yetkiliye sunmak","neighbor_only":"Kişi veya işi karar verecek belirli bir yetkili önüne getirir.","neighbor_ref":"root_000582/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir içerik ilk sahibinden başka bir alıcıya ulaştırılır."}],"source_phrase_ar":"الرفع إذاعة الشيء وإظهاره (maqayis); كل رافعة رفعت علينا من البلاغ (maqayis;sihah;tahdhib); رفع فلان على العامل إذا أذاع خبره (maqayis;tahdhib); أذاع خبر ما احتجبه (mufradat)","source_summary":"Kanıtlar haberin gizlilikten çıkarılıp yayılmasında birleşir; haberi duyuran topluluk, temel yayma eyleminin katılımcısı olarak ayrıca belirtilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"إظهار الخبر وإشاعته والتبليغ عن القائل","what_is_not_ar":"ليس مجرد تقديم الخصومة إلى الحاكم"},"support_links":["sup_3407c64c6d39b6f528e1"]},{"boundary":"Dal hasat sonrası taşıma aşamasına bağlıdır; ekini biçme, ürünün kendisi veya genel kaldırma anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"hasat ürününü harman yerine taşımak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hasat edilmiş ürünü harman yerine taşımak."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ürünün harman yerine taşındığı zamanı veya bu taşıma işini adlandırmak."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçilmiş ürünün hasattan sonra tarladan harman yerine götürüldüğü tarımsal aşama için uygundur.","boundary_detail":"Dal hasat sonrası taşıma aşamasına bağlıdır; ekini biçme, ürünün kendisi veya genel kaldırma anlamına genişletilmez.","branch_image_ar":"رفع الزرع","concept_gloss":"hasat ürününü harman yerine taşımak","contextual_glosses":[{"applicability":"İşlemin kendisinden çok hasat ürününün harman yerine taşındığı zaman diliminin adlandırıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli tarımsal işlemin gerçekleştiği zaman dilimini korur."},"facet_ids":["F002"],"text":"ürün taşıma dönemi","usage_role":"contextual"}],"definition":"Hasat edilen ürünü tarladan alıp harman yerine taşımaktır. Aynı kullanım bu taşıma işinin yapıldığı dönemi de adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hasat edilmiş ürünü harman yerine taşımak."},{"facet_id":"F002","role":"extension","statement":"Ürünün harman yerine taşındığı zamanı veya bu taşıma işini adlandırmak."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ürünü kesip toplama biçimindeki önceki aşamayı ekler.","collision":"Taşıma işlemini biçme işlemiyle karıştırır.","fit":"displacement","loses":"Biçilmiş ürünü harman yerine taşıma aşamasını kaybeder.","preserves":"Aynı tarımsal üretim çevrimini korur."},"text":"hasat etmek"}],"identity_rationale":"Kaynak ifadesi, ürünü hasattan sonra harman yerine taşıma işlemini açıkça tanımlar ve aynı adın bu işin yapıldığı dönem için de kullanıldığını gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"hasat edilen ürünü harman yerine taşımak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ürünün harman yerine taşındığı dönem veya bu iş"}],"lexicalization_note":"Kalıba bağlı kullanım hasat edilmiş ürünü harman yerine taşımayı anlatır; biçim birimi ise bu işlemle onun zamanını adlandırır ve genel fiziksel kaldırma anlamına açılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; biçme aşaması, taşımanın varış yeri ve genel fiziksel kaldırma bu tarımsal kullanımın sınırlarını en açık gösteren ilişkilerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ürünü tarlada kesme aşamasıdır; odak dal ise kesilmiş ürünü bundan sonra harman yerine götürme aşamasıdır.","focus_only":"Biçilmiş ürünü harman yerine taşır.","gloss":"ürünü taşımak ve ürünü biçmek","neighbor_only":"Tarladaki ürünü kesip hasat eder ve hasat zamanını da kapsar.","neighbor_ref":"root_000327/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı hasat sürecinin art arda gelen aşamalarını anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dal bir işlem ve dönemdir; komşu dal bu işlemin ulaştığı, ürünün biriktirildiği veya işlendiği mekandır.","focus_only":"Ürünü belirli yere götüren taşıma işlemini anlatır.","gloss":"harman yerine taşımak ve harman yeri","neighbor_only":"Ürünün toplandığı veya dövüldüğü yerin kendisini anlatır.","neighbor_ref":"root_000093/B007","relation_type":"thematic","shared_zone":"Harman yeri odak daldaki taşımanın varış noktasıdır."},{"boundary_match":"partial","distinction":"Odak dalda yönün yukarı olması gerekmez; tarımsal nesne, hasat sonrası zaman ve harman yeri zorunludur. Komşu dalda ise ayırıcı unsur yukarı yöndür.","focus_only":"Hasat edilmiş ürünü harman yerine götürme aşamasına bağlıdır.","gloss":"ürünü harman yerine taşımak ve yukarı kaldırmak","neighbor_only":"Herhangi bir fiziksel nesneyi daha yüksek konuma taşımayı anlatır.","neighbor_ref":"root_000582/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal fiziksel bir nesnenin bulunduğu yerden taşınmasını içerebilir."}],"source_phrase_ar":"رفع الزرع أن يحمل بعد الحصاد إلى البيدر (maqayis;sihah); جاء زمن الرفاع إذا رفع الزرع (tahdhib); الرفاع أن يحصد الزرع ويرفع (tahdhib)","source_summary":"Kanıtlar hasattan sonraki ürün taşıma aşamasında birleşir; işlem ile bu işlemin zamanı aynı tarımsal çevrim içinde birbirine bağlı iki görünüm olarak sunulur.","sources":["MQ","SI","TA"],"what_is_ar":"حمل الزرع بعد حصاده إلى البيدر وزمن ذلك","what_is_not_ar":"ليس رفع الجسم مطلقا ولا رفع القدر"},"support_links":[]},{"boundary":"Dal yalnızca dişi devenin sütü memede tutması ve süt vermemesi kalıbına bağlıdır; genel süt birikmesi veya sağım anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000582/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"dişi devenin sütünü memesinde tutması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi devenin memedeki sütü tutup sağım sırasında vermemesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin sütü bulunduğu halde onu vermediği özel hayvancılık bağlamı için uygundur.","boundary_detail":"Dal yalnızca dişi devenin sütü memede tutması ve süt vermemesi kalıbına bağlıdır; genel süt birikmesi veya sağım anlamı değildir.","branch_image_ar":"رفع اللبن في الضرع","concept_gloss":"dişi devenin sütünü memesinde tutması","contextual_glosses":[{"applicability":"Özne dişi deve ve bağlam memedeki sütün tutulması olduğunu zaten açıkça gösterdiğinde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün memede tutulması işlemini ve ilk süt ayrıntısını açıkça söylemez.","preserves":"Sağımda sütün verilmemesi sonucunu korur."},"facet_ids":["F001"],"text":"sütünü vermemek","usage_role":"contextual"}],"definition":"Dişi devenin sütünü veya doğumdan sonraki ilk sütünü memesinde tutması ve bu nedenle süt vermemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi devenin memedeki sütü tutup sağım sırasında vermemesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sütün tutulmadığı ve olağan biçimde sağılabildiği her türlü doluluğu da kapsar.","collision":"Etkin biçimde süt vermeme sınırını sıradan dolulukla karıştırır.","fit":"broadening","loses":null,"preserves":"Sütün memede bulunması durumunu korur."},"text":"sütü birikmek"}],"identity_rationale":"Kaynak ifadesi, dişi devenin sütünü veya doğumdan sonraki ilk sütünü memesinde tutup vermemesini açıkça tanımlar; geçici doluluk tek başına yeterli değildir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve"}],"lexicalization_note":"Tanım yalnızca sütünü veya ilk sütünü memesinde tutup vermeyen dişi deve kalıbına bağlıdır ve çıplak kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sütü salma karşıtlığı, uyarı gerektiren sağım ve ilk sütün koyulaşması dalın sınırını en açık gösteren üç karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal sütün tutulduğu uçtadır; komşu dal ise sütün herhangi bir sağım olmadan dışarı çıktığı karşı uçtadır.","focus_only":"Sütü memede tutar ve dışarı vermemeyi belirtir.","gloss":"sütü tutmak ve sütün kendiliğinden çıkması","neighbor_only":"Sütün sağım olmadan kendiliğinden dışarı çıkmasını belirtir.","neighbor_ref":"root_001528/B005","relation_type":"polarity_pair","shared_zone":"İki dal memedeki sütün dışarı çıkıp çıkmaması eksenini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal memedeki sütü tutma durumuna dayanır; komşu dal ise süt akışını başlatmak için gereken özel burun uyarısını ayırıcı özellik yapar.","focus_only":"Sütü memede tutma durumunu doğrudan adlandırır.","gloss":"sütü tutan deve ve uyarılınca süt veren deve","neighbor_only":"Süt vermesi için burnuna dokunulması gereken özel bir dişi deve türünü anlatır.","neighbor_ref":"root_001482/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal sütü olağan sağımda hemen vermeyen dişi deveyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal sütün dışarı verilmemesine ilişkindir; komşu dal ise sütün kıvamındaki değişimi anlatır ve süt vermeme davranışını zorunlu kılmaz.","focus_only":"Hayvanın sütü vermemesi davranışını belirtir.","gloss":"sütü tutmak ve ilk sütün koyulaşması","neighbor_only":"İlk sütün memede koyulaşıp bağlanmasını belirtir.","neighbor_ref":"root_001625/B010","relation_type":"near_neighbor","shared_zone":"İki dal da dişi devenin memesindeki ilk sütle ilgili bir durumu anlatır."}],"source_phrase_ar":"ناقة رافع إذا رفعت اللبأ في ضرعها (maqayis;sihah); التي رفعت لبنها فلم تدر رافع (tahdhib)","source_summary":"Kanıtlar memedeki sütün, özellikle ilk sütün tutulması ile hayvanın süt vermemesi sonucunu aynı yapı içinde birleştirir.","sources":["MQ","SI","TA"],"what_is_ar":"حبس الناقة لبنها أو لبأها في ضرعها فلا تدر","what_is_not_ar":"ليس دفع اللبأ في الضرع"},"support_links":[]},{"boundary":"Dal kalçayı büyük gösterme amacıyla kullanılan dolgu nesnesidir; genel giysi astarı veya beden niteliği değildir.","branch_kind":"bare","branch_ref":"root_000582/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"kalçayı büyük gösteren dolgu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının kalçasını daha büyük göstermek amacıyla kullanılan dolgu nesnesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Giysi altında kullanılarak kadının kalçasını daha büyük göstermeye yarayan nesneyi adlandırır.","boundary_detail":"Dal kalçayı büyük gösterme amacıyla kullanılan dolgu nesnesidir; genel giysi astarı veya beden niteliği değildir.","branch_image_ar":"الرِفاعة للمرأة","concept_gloss":"kalçayı büyük gösteren dolgu","contextual_glosses":[{"applicability":"Nesnenin giysi altındaki işlevini açıkça belirtmek gereken açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalçayı daha büyük gösteren destek nesnesi işlevini korur."},"facet_ids":["F001"],"text":"beden biçimlendirici kalça dolgusu","usage_role":"explanatory"}],"definition":"Bir kadının kalçasını gerçekte olduğundan daha büyük göstermek için giysisinin altında kullandığı dolgu veya destek nesnesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının kalçasını daha büyük göstermek amacıyla kullanılan dolgu nesnesi."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Giysinin iç yüzünü kaplayan her türlü astar işlevini ekler.","collision":"Yapısal giysi parçasıyla görünüm değiştirici dolguyu karıştırır.","fit":"displacement","loses":"Kalçayı daha büyük gösterme işlevini ve beden bölgesini kaybeder.","preserves":"Giysinin altında yer alan bir malzeme olabilmesini korur."},"text":"giysi astarı"}],"identity_rationale":"Kaynak ifadesi, bir kadının kalçasını daha büyük göstermek için kullandığı nesneyi doğrudan tanımlar ve bu işlevi nesnenin kurucu özelliği yapar.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"kadının kalçasını büyük göstermek için kullandığı dolgu"}],"lexicalization_note":"Dal, tek başına adlandırılan beden biçimlendirici nesneyi tanımlar; başka kalıplardan anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; tam eşleşen beden dolgusu ile yalnızca yer bakımından yakın olan giysi astarı yayıma değer iki sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kartlarda görülen çekirdek, kullanıcı, beden bölgesi ve amaç bakımından aynıdır; olağan kullanımda birbirlerinin yerine geçebilirler.","focus_only":null,"gloss":"kalçayı büyük gösteren dolgu","neighbor_only":null,"neighbor_ref":"root_001029/B008","relation_type":"synonym","shared_zone":"İki dal da kadının kalçasını daha büyük göstermek için yastık benzeri bir destek nesnesi kullanmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalın zorunlu işlevi beden görünümünü değiştirmektir; komşu dal ise giysiyi içten kaplar ve kalçayı büyütme amacı taşımaz.","focus_only":"Kalçanın görünümünü büyütmek için belirli bir yere yerleştirilir.","gloss":"kalça dolgusu ve giysi astarı","neighbor_only":"Giysinin veya örtünün iç yüzünü kaplayan genel bir katmandır.","neighbor_ref":"root_000128/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal giysinin dış katmanının altında bulunan bir malzemeyi anlatabilir."}],"source_phrase_ar":"الرفاعة ما تتعظم به المرأة الرسحاء (sihah); الرفاعة شيء تعظم به المرأة عجيزتها (tahdhib); الرفاعة ما ترفع به المرأة عجيزتها (mufradat)","source_summary":"Kanıtlar nesnenin kim tarafından ve hangi beden bölgesini büyük göstermek için kullanıldığı konusunda birleşir; biçimlendirme işlevi tanımın merkezindedir.","sources":["SI","TA","MU"],"what_is_ar":"الرِفاعة التي تعظم بها المرأة عجيزتها","what_is_not_ar":"ليس حبل القيد ولا رفعة القدر"},"support_links":[]},{"boundary":"Dal bağın kendisi değil, bağlı kişinin o bağı yukarı kaldırmasına yarayan yardımcı iptir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"bağı yukarı çekmeye yarayan ip","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlı kişinin bağını eline doğru yukarı kaldırmasını sağlayan ip."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bağlı kişinin kendi bağını eline doğru kaldırmak için kullandığı özel yardımcı ipi adlandırır.","boundary_detail":"Dal bağın kendisi değil, bağlı kişinin o bağı yukarı kaldırmasına yarayan yardımcı iptir.","branch_image_ar":"رِفاع القيد","concept_gloss":"bağı yukarı çekmeye yarayan ip","contextual_glosses":[{"applicability":"Kullanıcının bağlı olduğu ve ipin bağın ağırlığını yukarı almak için kullanıldığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İpin bağ kaldırma işlevini kısa biçimde korur."},"facet_ids":["F001"],"text":"bağ kaldırma ipi","usage_role":"contextual"}],"definition":"Bağlı bir kişinin elinde tutup ayağındaki veya bedenindeki bağı kendine doğru yukarı çekmek için kullandığı yardımcı iptir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlı kişinin bağını eline doğru yukarı kaldırmasını sağlayan ip."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişiyi doğrudan kısıtlayan asıl bağ veya demir halka anlamını ekler.","collision":"Yardımcı ipi kaldırdığı bağın kendisiyle karıştırır.","fit":"displacement","loses":"Bağı yukarı çekmeye yarayan yardımcı ip işlevini kaybeder.","preserves":"Bağlı kişinin kısıtlanmasıyla ilgili nesne alanını korur."},"text":"pranga"}],"identity_rationale":"Kaynak ifadesi, bağlı kişinin elinde tutarak bağını veya prangasını kendine doğru yukarı çektiği ipi açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"bağlı kişinin bağını yukarı çekmekte kullandığı ip"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bağlı kişinin elinde tutup bağını kaldırdığı ip"}],"lexicalization_note":"Biçim birimi yardımcı ipi adlandırır; bağlı kişiye özgü kalıp aynı nesnenin kullanımını açıklar ve genel ip ya da bağ anlamına genişletilmez.","neighbor_coverage_note":"Bütün bağ ve ip adayları karşılaştırıldı; asıl bağ, yapısıyla tanımlanan deri bağ ve bağlama eylemi yardımcı ipin işlevsel sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kısıtlamayı kurmaz, asıl bağın taşınmasını kolaylaştırır; komşu dal ise doğrudan bağlama ve kısıtlama aracıdır.","focus_only":"Var olan bağı yukarı çekmeye yarayan yardımcı iptir.","gloss":"bağ kaldırma ipi ve bağ","neighbor_only":"Hayvanı veya başka bir varlığı doğrudan kısıtlayan bağın kendisidir.","neighbor_ref":"root_000813/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bağlama düzeninde kullanılan ip veya kordon türü nesnelerle ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yönü kullanım işlevidir; komşu dalın ayırıcı yönü ise doğrudan bağ oluşu ile deri ve sıkı büküm özellikleridir.","focus_only":"Bağlı kişinin kendi bağını eline doğru kaldırma işleviyle tanımlanır.","gloss":"yardımcı kaldırma ipi ve deri bağ","neighbor_only":"Deriden yapılmış kısa ve sıkı bükümlü bir bağ türü olarak malzemesi ve yapısıyla tanımlanır.","neighbor_ref":"root_000946/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal kısıtlama düzeninde kullanılan kısa ip veya bağ nesnelerini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal mevcut kısıtlama içindeki yardımcı bir nesnedir; komşu dal ise kısıtlamayı kuran bağlama eylemi ve araçlarına odaklanır.","focus_only":"Bağlı kişinin hareketini kolaylaştırmak için bağı yukarı alır.","gloss":"bağı kaldıran ip ve bağlayıp kısıtlama","neighbor_only":"Esiri bağlayıp hareketini sınırlama eylemini ve bağlama araçlarını anlatır.","neighbor_ref":"root_000868/B002","relation_type":"same_field","shared_zone":"İki dal bağlı kişi, bağ ve kısıtlama düzeni alanını paylaşır."}],"source_phrase_ar":"رفاعة المقيد خيط يرفع به قيده إليه (sihah); الرفاع حبل القيد يأخذه المقيد بيده يرفعه إليه (tahdhib)","source_summary":"Kanıtlar ipin bağlı kişi tarafından elde tutulması ve bağın yukarı çekilmesini sağlaması konusunda birleşir; nesne doğrudan bağın kendisi olarak tanımlanmaz.","sources":["SI","TA"],"what_is_ar":"حبل أو خيط يرفع به المقيد قيده","what_is_not_ar":"ليس رِفاعة المرأة ولا رفع الحصاد"},"support_links":[]},{"boundary":"Dal yalnızca sesin yüksekliğini adlandıran kalıba bağlıdır; genel ses, konuşma ve toplumsal yücelik anlamlarını kapsamaz.","branch_kind":"collocation","branch_ref":"root_000582/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"sesin yüksekliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sesin güçlü ve yüksek düzeyde işitilmesi niteliği."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir sesin işitilebilir güç düzeyinin yüksek oluşunu adlandıran bağlam için uygundur.","boundary_detail":"Dal yalnızca sesin yüksekliğini adlandıran kalıba bağlıdır; genel ses, konuşma ve toplumsal yücelik anlamlarını kapsamaz.","branch_image_ar":"رِفاعة الصوت","concept_gloss":"sesin yüksekliği","contextual_glosses":[{"applicability":"Sesin belirgin ve güçlü işitildiği niteliği daha doğal bir sıfatlaştırmayla vermek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yükseklik derecesini doğrudan adlandırmak yerine sesin dolgunluğunu öne çıkarabilir.","preserves":"Sesin güçlü ve belirgin işitilmesini korur."},"facet_ids":["F001"],"text":"gür seslilik","usage_role":"contextual"}],"definition":"Bir sesin işitilebilir güç bakımından yüksek olma niteliğidir; ses çıkarma eyleminden çok ses düzeyini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sesin güçlü ve yüksek düzeyde işitilmesi niteliği."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İstemli bir ses çıkarma eylemini ve çoğu kez öfke ya da çağrı bağlamını ekler.","collision":"Ses düzeyi niteliğini belirli bir insan eylemiyle karıştırır.","fit":"broadening","loses":null,"preserves":"Yüksek ses çıkarılabilmesini korur."},"text":"bağırma"}],"identity_rationale":"Kaynak ifadesi bu dalı sesin yüksek olması niteliğiyle sınırlar; bağırma eylemi veya belirli bir çağrı türü tanımın zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"sesin yüksekliği"}],"lexicalization_note":"Tanım sesin yüksekliğini belirten kalıba bağlı tutulur ve çıplak biçime ya da her türlü yüksekliğe genellenmez.","neighbor_coverage_note":"Bütün ses adayları değerlendirildi; bağırma, çağrıda sesi yükseltme ve sesin gövdeli oluşu yüksek ses niteliğinin üç yararlı sınırı olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ses düzeyinin niteliğidir; komşu dal ise yüksek sesin çıkarıldığı bağırma ve seslenme eylemlerine kadar uzanır.","focus_only":"Sesin yüksek olma niteliğini eylemden bağımsız adlandırır.","gloss":"yüksek ses ve bağırma","neighbor_only":"Bağırma, haykırma ve karşılıklı seslenme eylemlerini de kapsar.","neighbor_ref":"root_000895/B001","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü ve yüksek işitilen ses alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal bağlamdan bağımsız bir ses niteliğidir; komşu dal ise çağrı amacı ve sesi yükseltme eylemiyle sınırlıdır.","focus_only":"Herhangi bir sesin yüksekliğini belirtir.","gloss":"ses yüksekliği ve yüksek sesle çağırma","neighbor_only":"Özellikle çağrı sırasında sesi yükseltme ve abartılı seslenme eylemini belirtir.","neighbor_ref":"root_001484/B004","relation_type":"near_synonym","shared_zone":"İki dal da sesin olağandan yüksek düzeye çıkmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca yükseklik derecesine dayanır; komşu dal sesin gövdesi ya da çıkışı gibi farklı ve daha tartışmalı bir niteliğe dayanır.","focus_only":"Sesin yüksek işitilme derecesini güvenli biçimde anlatır.","gloss":"ses yüksekliği ve sesin gövdesi","neighbor_only":"Sesin gövdeli oluşunu veya dışarı çıkmasını, kaynakların çekincesi bulunan özel bir kullanımla anlatır.","neighbor_ref":"root_000239/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal sesin belirgin ve güçlü algılanan yönüyle ilgilidir."}],"source_phrase_ar":"في صوته رفاعة ورفاعة (sihah;tahdhib); إذا كان رفيع الصوت (tahdhib)","source_summary":"Kanıtlar kullanımın sesle kurulan özel bir kalıba bağlı olduğu ve yüksek ses niteliğini anlattığı konusunda birleşir.","sources":["SI","TA"],"what_is_ar":"علو الصوت المسمى رِفاعة أو رَفاعة","what_is_not_ar":"ليس رفعة القدر ولا إعلاء الجسم"},"support_links":[]},{"boundary":"Dal toplulukların ülke içinde ilerlemesini anlatan özel seyahat kullanımıdır; binek yürüyüşü ve genel fiziksel kaldırma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000582/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"toplulukça ülke içinde ilerlemek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun ülke içinde yola koyulup ilerlemesi."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun ülke içinde yola koyulup ilerlediği özel kullanım için uygundur.","boundary_detail":"Dal toplulukların ülke içinde ilerlemesini anlatan özel seyahat kullanımıdır; binek yürüyüşü ve genel fiziksel kaldırma değildir.","branch_image_ar":"الإصعاد في البلاد","concept_gloss":"toplulukça ülke içinde ilerlemek","contextual_glosses":[{"applicability":"Toplulukların ülke içinde yola koyulmasını açıkça belirtmek gereken açıklayıcı veya sözlük bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun yola çıkmasını ve ülke içindeki ilerleyişini korur."},"facet_ids":["F001"],"text":"toplulukça ülke içinde yola koyulmak","usage_role":"explanatory"}],"definition":"Bir topluluğun ülke içinde yola koyulup ilerlemesidir. Kullanım her türlü yolculuğa genişletilmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun ülke içinde yola koyulup ilerlemesi."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tek kişinin yolculuğunu, her yönü ve her türlü seyahat amacını sınırsız biçimde kapsar.","collision":"Topluluk ve özel yön çerçevesi görünmez olur.","fit":"broadening","loses":null,"preserves":"Bir yerden başka yere hareket etme alanını korur."},"text":"seyahat etmek"}],"identity_rationale":"Kaynak ifadesi toplulukların ülke içinde yola koyulup ilerlemesini yukarı yönelme sözüyle anlatır; bunu her türlü yolculuğa veya zorunlu bir yükseklik kazanımına yaymak kanıtı aşar.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"topluluğun ülke içinde yola koyulup ilerlemesi"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"yolculukta ilerleyenler"}],"lexicalization_note":"Topluluğa bağlı kalıp ülke içinde yola koyulmayı anlatır; biçim birimi bu ilerleyen topluluğu adlandırır ve anlam genel seyahate genişletilmez.","neighbor_coverage_note":"Bütün yolculuk adayları değerlendirildi; genel yola çıkma, binek yürüyüşü ve ufuklarda dolaşma bu özel topluluk kullanımının sınırlarını en açık gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal topluluk öznesiyle ülke içindeki ilerlemeyi anlatır; komşu dal ise özne, yolculuğa başlama ve güzergah bakımından daha genel bir hareket alanına sahiptir.","focus_only":"Topluluk öznesine ve ülke içindeki ilerlemeye bağlı özel kullanımdır.","gloss":"toplulukça ilerlemek ve yolculuğa çıkmak","neighbor_only":"Tekil veya çoğul yolcuları, yolculuğa başlama ve ülke ya da vadi içinde her yönde ilerlemeyi daha geniş biçimde kapsar.","neighbor_ref":"root_000862/B002","relation_type":"near_synonym","shared_zone":"İki dal ülke içinde yola koyulma ve ilerleme anlamında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği topluluğun yer değiştirmesidir; komşu dalın çekirdeği ise binek hayvanının yürüyüş hızı ve biçimidir.","focus_only":"Toplulukların ülke içindeki yolculuğunu anlatır.","gloss":"ülkede ilerlemek ve bineği hızlı yürütmek","neighbor_only":"Binek hayvanının ağır yürüyüş ile tam koşu arasındaki belirli hız biçimini anlatır.","neighbor_ref":"root_000582/B003","relation_type":"near_neighbor","shared_zone":"İki dal yolculuk ve ilerleme sahnesinde görülebilir."},{"boundary_match":"partial","distinction":"Odak dal topluluk öznesiyle ülke içindeki ilerleyişe bağlıdır; komşu dal ise uzaklık, dolaşma ve kazanç amacı gibi geniş yolculuk kullanımlarını içerir.","focus_only":"Toplulukların ülke içinde ilerlemesini anlatır.","gloss":"ülke içinde ilerlemek ve uzaklarda dolaşmak","neighbor_only":"Ufuklara yayılma, kazanç için dolaşma ve uzak yerlerden gelip gitme gibi daha geniş amaçları kapsar.","neighbor_ref":"root_000040/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal ülke içinde veya ülkeler arasında yol alma alanındadır."}],"source_phrase_ar":"رفع القوم فهم رافعون إذا أصعدوا في البلاد (tahdhib); الروافع إذا رفعوا في سيرهم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, ülke içinde yola koyulan toplulukları ve yolculuktaki ilerleyişlerini adlandırır."}],"source_summary":"Kanıt, toplulukların ülke içinde veya yolculukta ilerlemesini anlatan özel bir kullanım sunar; anlam her türlü seyahate genişletilmemelidir.","sources":["TA"],"what_is_ar":"إصعاد القوم في البلاد أو في السير","what_is_not_ar":"ليس سير الدابة الخاص ولا رفع الشيء باليد"},"support_links":[]},{"boundary":"Dal yalnızca dil bilgisel çekim durumudur; fiziksel yükseltme veya toplumsal yücelik anlamı taşımaz.","branch_kind":"non_bare","branch_ref":"root_000582/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","surface_ar":"مَّرْفُوعَةٌ"}],"gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunması."}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir sözcüğün çekim düzenindeki bu özel dil bilgisel durumu doğal Türkçe ile adlandırmak için uygundur.","boundary_detail":"Dal yalnızca dil bilgisel çekim durumudur; fiziksel yükseltme veya toplumsal yücelik anlamı taşımaz.","branch_image_ar":"الرفع في الإعراب","concept_gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu","contextual_glosses":[{"applicability":"Terimin sözcük çekimindeki yerini ve sabit biçimlerdeki ötreyle karşılığını açıklayan öğretici bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcük çekimi ile sabit biçimlerdeki ötre arasındaki karşılığı korur."},"facet_ids":["F001"],"text":"çekimde ötreye karşılık gelen durum","usage_role":"explanatory"}],"definition":"Çekimli bir sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcüğün, sabit biçimlerdeki ötreye karşılık gelen dil bilgisel çekim durumunda bulunması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel veya toplumsal bir şeyi daha yüksek hale getirme eylemini ekler.","collision":"Dil bilgisi dalını fiziksel kaldırma dalıyla karıştırır.","fit":"displacement","loses":"Dil bilgisel çekim durumu ve uzmanlık terimi olma niteliğini kaybeder.","preserves":"Kaynak kavramdaki yukarı yönlü adlandırma çağrışımını korur."},"text":"yükseltme"}],"identity_rationale":"Kaynak ifadesi dalı dil bilgisi uzmanlarının koyduğu çekim terimi olarak açıkça sınırlar ve çekimli sözcüklerdeki bu durumu sabit biçimlerdeki belirli son ses işaretiyle karşılaştırır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"dil bilgisinde ötreye karşılık gelen çekim durumu"}],"lexicalization_note":"Anlam yalnızca dil bilgisi terimi olan özel sözlük birimine bağlıdır ve çıplak kökün fiziksel ya da değer bildiren anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün dil bilgisi adayları incelendi; karşı çekim durumu, çekime açıklık ve tümce ögeleri terimin yerini en açık gösteren üç komşu olarak seçildi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal sabit biçimlerdeki ötreye karşılık gelen çekim durumudur; komşu dal ise üstünle ilişkilendirilen karşıt çekim durumunu anlatır.","focus_only":"Sözcüğün ötreyle ilişkilendirilen çekim durumunu belirtir.","gloss":"ötreye ve üstüne karşılık gelen çekim durumları","neighbor_only":"Sözcüğün üstünle ilişkilendirilen karşı çekim durumunu belirtir.","neighbor_ref":"root_001507/B007","relation_type":"antonym","shared_zone":"İki dal aynı dil bilgisel çekim düzeninde birbirine karşıt konumları belirtir."},{"boundary_match":"field_only","distinction":"Odak dal çekim içindeki tek bir konumdur; komşu dal ise sözcüğün böyle konum değişikliklerini alabilme yeteneğini sınıflandırır.","focus_only":"Çekimli sözcüğün belirli bir durumunu adlandırır.","gloss":"belirli çekim durumu ve çekime açıklık","neighbor_only":"Bir adın genel olarak çekime açık, değişebilir veya sabit olma özelliğini adlandırır.","neighbor_ref":"root_001439/B006","relation_type":"same_field","shared_zone":"İki dal adların çekim düzenindeki davranışını konu edinir."},{"boundary_match":"field_only","distinction":"Odak dal biçimsel bir çekim konumudur; komşu dal ise anlam ve görev bakımından farklı nesne türlerini sayar.","focus_only":"Sözcük biçiminin çekim durumunu belirtir.","gloss":"çekim durumu ve tümce ögeleri","neighbor_only":"Tümcede eyleme çeşitli yönlerden bağlanan nesne ve tamamlayıcı türlerini sınıflandırır.","neighbor_ref":"root_001167/B007","relation_type":"same_field","shared_zone":"İki dal dil bilgisinde sözcüklerin tümce içindeki görevleriyle ilgilidir."}],"source_phrase_ar":"الرفع في الإعراب كالضم في البناء (sihah); وهو من أوضاع النحويين (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı tanıklık, terimin uzmanlarca konduğunu ve çekim durumu ile sabit son ses işareti arasında karşılık kurduğunu belirtir."}],"source_summary":"Kanıt bu anlamı uzmanların belirlediği bir çekim terimi olarak sunar ve çekimli sözcükteki durum ile sabit biçimdeki son ses işareti arasında karşılaştırma kurar.","sources":["SI"],"what_is_ar":"الرفع النحوي في الإعراب كالضم في البناء","what_is_not_ar":"ليس الرفع اللغوي للأجسام ولا رفع المنزلة"},"support_links":[]},{"boundary":"Anlam hem saklı içerik ve iç durumları hem de kişiler arasındaki gizli konuşmayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B001","candidate_links":[{"candidate_id":"cand_f2dc90488c5856ca37b4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"saklama ve gizli paylaşım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bilgi, söz, iş veya iç durum başkalarının bilgisine kapalı tutulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz, bir kişiye gizlice söylenir veya kişiler kendi aralarında gizli konuşur."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Saklı içerik ile kişiler arasındaki gizli söz alışverişini birlikte karşılayan genel kavram anlatımıdır.","boundary_detail":"Anlam hem saklı içerik ve iç durumları hem de kişiler arasındaki gizli konuşmayı kapsar.","branch_image_ar":"إخفاء الشيء في الباطن","concept_gloss":"saklama ve gizli paylaşım","contextual_glosses":[{"applicability":"İki veya daha çok kişinin başkalarından saklı biçimde konuştuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Konuşma dışındaki saklı bilgi, iş ve iç durum anlamlarını karşılamaz.","preserves":"Gizli söz alışverişini ve açıklamama koşulunu korur."},"facet_ids":["F002"],"text":"gizlice konuşmak","usage_role":"contextual"}],"definition":"Bir bilgi, söz, iş veya iç durumun başkalarına açıklanmadan saklanmasıdır; ayrıca bu tür bir sözün bir kişiye gizlice iletilmesini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bilgi, söz, iş veya iç durum başkalarının bilgisine kapalı tutulur."},{"facet_id":"F002","role":"specialization","statement":"Söz, bir kişiye gizlice söylenir veya kişiler kendi aralarında gizli konuşur."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkalarından saklama durumunu ve birine sözü gizlice iletme eylemini birlikte açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gizlenen bilgi veya durum"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin gizli iç durumu veya gizlice yaptığı iş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi gizleyip saklamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"birine bir sözü gizlice açmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kulağına gizlice söylemek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kendi aralarında gizlice konuşmak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"gizlice konuşmaya yarayan tomar benzeri araç"}],"lexicalization_note":"Tanım, yalın biçimlerin giz ve iç durum anlamıyla türemiş eylemlerin saklama ve gizli konuşma anlamlarını ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın karışma alanını gizli konuşma dalı açıklamaktadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal gizli konuşmaya odaklanırken bu dal daha geniş biçimde saklı içerik, iç durum ve saklama eylemini de içerir.","focus_only":"Saklı bilgi, iç durum ve tek başına gizleme eylemi de kapsama girer.","gloss":"gizli konuşma","neighbor_only":"Özel konuşma, bir kişiyi gizli söz için ayırma çerçevesinde belirginleşir.","neighbor_ref":"root_001476/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da başkalarından saklanan sözün kişiler arasında iletilmesini kapsar."}],"source_phrase_ar":"السر خلاف الإعلان (maqayis)؛ السر ما أسررت والسريرة عمل السر (ayn)؛ السر الذي يكتم والسريرة مثله (sihah)؛ الإسرار خلاف الإعلان والسر هو الحديث المكتم في النفس (mufradat)؛ ساره في أذنه وتساروا (sihah)","source_summary":"Tanıklıklar saklamayı açıklamanın karşıtı olarak verir; içte tutulan söz, gizli durum ve özel konuşma bu çekirdeğin görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السر والإسرار والسريرة والمناجاة والمسارة وما يفضى به في خفية","what_is_not_ar":"الإعلان؛ النكاح؛ السرور؛ السرار القمري"},"support_links":["sup_3407c64c6d39b6f528e1"]},{"boundary":"Bu, yerleşik saklama anlamının karşıtı olan tartışmalı bir kullanım olarak sunulmalıdır.","branch_kind":"unresolved","branch_ref":"root_000697/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"açığa vurma, tartışmalı kullanım","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem bazı tanıklıklarda bir şeyi açıklamak veya görünür kılmak anlamında verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı okuma başka değerlendirmelerde yanlış, işitilmemiş veya güvenilmez sayılır."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynaklarda aktarılıp aynı zamanda eleştirilen karşıt anlamı ihtiyatla göstermek için uygundur.","boundary_detail":"Bu, yerleşik saklama anlamının karşıtı olan tartışmalı bir kullanım olarak sunulmalıdır.","branch_image_ar":"إظهار ما قيل فيه أسر","concept_gloss":"açığa vurma, tartışmalı kullanım","contextual_glosses":[{"applicability":"Anlamın doğrudan onaylanmadığı, yalnızca eski bir yorum olarak aktarıldığı açıklamalarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açıklama iddiasını kesin hüküm vermeden aktarır ve tartışmalı niteliği sezdirir."},"facet_ids":["F001","F002"],"text":"açıkladığı ileri sürülmek","usage_role":"explanatory"}],"definition":"Tartışmalı bir kullanımda, saklamak beklenen eylemin bir şeyi açıklamak veya görünür kılmak anlamına gelmesidir; bu okumanın güvenilirliğine bazı kaynak değerlendirmelerinde itiraz edilmiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem bazı tanıklıklarda bir şeyi açıklamak veya görünür kılmak anlamında verilir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı okuma başka değerlendirmelerde yanlış, işitilmemiş veya güvenilmez sayılır."}],"identity_rationale":"Kaynak ifadesi açıklama anlamındaki kullanımı bildirir, ancak aynı toplu tanıklık bu okumanın yanlış veya tekil sayıldığını da kaydeder.","lexicalization_note":"Yalın ya da belirli bir yapıya bağlı olduğu kanıtlanmadığından tanım kullanımın biçimsel kapsamını varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ortaya çıkma dalı tartışmalı kullanımın sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ortaya çıkmayı anlatır; bu dal ise belirli bir sözcüğe atfedilen ve güvenilirliği tartışılan karşıt anlam kaydıdır.","focus_only":"Açıklama anlamı, normalde saklama bildiren bir eyleme yüklenen tartışmalı karşıt okumadır.","gloss":"gizlinin ortaya çıkması","neighbor_only":"Bir şeyin gizlilikten çıkıp görünür olması veya doğrudan ortaya çıkarılması genel ve yerleşik anlamdır.","neighbor_ref":"root_000105/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gizli veya görünmez olan bir şeyin bilinir ve görünür hale gelmesi vardır."}],"source_phrase_ar":"أسررته أعلنته (maqayis)؛ أسررت الشيء أظهرته وكتمته أيضا (jamhara)؛ أسررت الشيء كتمته وأعلنته أيضا (sihah)؛ قال الفراء أخطأ أبو عبيدة (maqayis)؛ لم أسمع ذلك لغيره (tahdhib)","source_summary":"Toplu tanıklık hem açıklama anlamını aktarır hem de bu anlamın güvenilirliğine yönelik açık itirazı korur; bu nedenle kullanım kesinleştirilemez.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"استعمال أسررت بمعنى أعلنت أو أظهرت مع كونه موضع خلاف في المصادر","what_is_not_ar":"الإسرار المستقر بمعنى الكتمان؛ أشررت بالشين"},"support_links":[]},{"boundary":"Dal genel gizli konuşma değildir; evlilik ve cinsellikle ilgili örtülü kullanımla sınırlıdır.","branch_kind":"unresolved","branch_ref":"root_000697/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"gizli tutulan evlilik veya cinsel ilişki","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evlilik veya cinsel birleşme, gizli tutulan bir ilişki olarak örtülü biçimde adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım evlilik dışı ilişkiye veya bekleme süresindeki kadına evlenme önerisine uzanabilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik ve cinsel birlikteliği gizlilik bağıyla birlikte veren en geniş doğal karşılıktır.","boundary_detail":"Dal genel gizli konuşma değildir; evlilik ve cinsellikle ilgili örtülü kullanımla sınırlıdır.","branch_image_ar":"سر النكاح المستور","concept_gloss":"gizli tutulan evlilik veya cinsel ilişki","contextual_glosses":[{"applicability":"Sözün özellikle cinsel birleşmeyi dolaylı ve gizlilik vurgusuyla anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evlilik, evlenme önerisi ve evlilik dışı ilişki arasındaki geniş kapsamı daraltır.","preserves":"Cinsel birliktelik ve örtülü adlandırma bağını korur."},"facet_ids":["F001"],"text":"örtülü biçimde cinsel birliktelik","usage_role":"contextual"}],"definition":"Evlilik veya cinsel birleşmenin, genellikle gizli tutulması nedeniyle örtülü biçimde adlandırılmasıdır; kimi kullanımlarda evlilik dışı ilişkiyi ya da bekleme süresindeki kadına evlenme önerisini de belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evlilik veya cinsel birleşme, gizli tutulan bir ilişki olarak örtülü biçimde adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Kullanım evlilik dışı ilişkiye veya bekleme süresindeki kadına evlenme önerisine uzanabilir."}],"identity_rationale":"Kaynak ifadesi evlilik ve cinsel birleşmeyi gizlilik üzerinden adlandırır; evlilik dışı ilişki ve bekleme süresindeki kadına evlenme önerisi de kapsam uzantılarıdır.","lexicalization_note":"Belirli bir yalın veya yapıya bağlı dağılım kanıtlanmadığı için tanım yalnızca aktarılan cinsel ve evlilik alanını korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan cinsel birleşme dalı örtülü kullanımın sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan birleşme eylemine odaklanır; bu dal gizlilikten doğan örtülü adlandırmayı ve evlilik alanındaki uzantıları korur.","focus_only":"Evlilik, evlilik dışı ilişki ve belirli evlenme önerileri gizlilik bağıyla kapsama girebilir.","gloss":"cinsel birleşme","neighbor_only":"Cinsel birleşme ve çiftleşme eylemi doğrudan anlam çekirdeğidir.","neighbor_ref":"root_000259/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da cinsel birleşmeyi veya evlilik içindeki cinsel birlikteliği anlatabilir."}],"source_phrase_ar":"السر وهو النكاح (maqayis)؛ السر الجماع والسر الذكر (sihah)؛ السر النكاح والزنى وخطبة المعتدة (tahdhib)؛ كني عن النكاح بالسر من حيث إنه يخفى (mufradat)","source_summary":"Tanıklıklar evlilik ve cinsel birleşme çekirdeğinde birleşir; toplu ifade, örtülü adlandırmanın evlilik dışı ilişki ve belirli evlenme önerilerine uzandığını da gösterir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السر بمعنى النكاح والجماع وما يتصل به من الزنى أو خطبة المعتدة والسريّة في اختلاف المصادر","what_is_not_ar":"المناجاة العامة؛ خالص النسب؛ السرور"},"support_links":[]},{"boundary":"Anlam ay sonundaki görünmezlik zamanına bağlıdır ve genel gizlenme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"ayın görünmediği ay sonu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hilalin ay sonunda görünmez olduğu son gün, gece veya kısa dönem adlandırılır."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hilalin kaybolduğu ay sonu zamanını gün ve gece ayrıntılarını zorlamadan karşılar.","boundary_detail":"Anlam ay sonundaki görünmezlik zamanına bağlıdır ve genel gizlenme anlamına genişletilmez.","branch_image_ar":"استتار الهلال آخر الشهر","concept_gloss":"ayın görünmediği ay sonu","contextual_glosses":[{"applicability":"Kaynak bağlamı özellikle ayın son gecesini işaret ettiğinde doğal bir zaman karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Son gün veya iki gecelik dönem olarak verilen kapsamı dışarıda bırakır.","preserves":"Ay sonundaki görünmezlik ve gece zamanını korur."},"facet_ids":["F001"],"text":"ayın son görünmez gecesi","usage_role":"contextual"}],"definition":"Ayın sonunda hilalin görünmediği son gün, son gece veya bir iki gecelik kısa dönemdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hilalin ay sonunda görünmez olduğu son gün, gece veya kısa dönem adlandırılır."}],"identity_rationale":"Kaynak ifadesi ayın sonunda hilalin görünmez olduğu son gün, gece veya iki gecelik dönemi tutarlı biçimde tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ayın sonunda hilalin görünmediği bir veya iki günlük dönem"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ayın son gecesi"}],"lexicalization_note":"Tanım hem dönem adını hem de ayın son gecesini bildiren yapıya bağlı kullanımı ayırmadan ama aynı zaman sınırında tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayın sönümlenmesi dalı zaman ile olay arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ışığın azalması ve görünmezleşme olayına, bu dal ise o olayla belirlenen son gün veya geceye odaklanır.","focus_only":"Ayın görünmediği son gün veya geceyi bir zaman dilimi olarak adlandırır.","gloss":"ayın sönümlenmesi","neighbor_only":"Ay ışığının azalması ve ayın görünmez hale gelmesi sürecini anlatır.","neighbor_ref":"root_001401/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal ayın sonunda hilalin görünmez olması çevresinde buluşur."}],"source_phrase_ar":"السرار ليلة يستسر الهلال (maqayis)؛ السرار يوم يستسر فيه الهلال آخر يوم من الشهر (ayn)؛ سرر الشهر آخر ليلة منه وكذلك سراره (sihah)؛ السرار اليوم الذي يستتر فيه القمر آخر الشهر (mufradat)","source_summary":"Tanıklıklar ay sonundaki görünmezlikte birleşir; süreyi son gün, son gece veya bir iki gece olarak ifade edebilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"السرار وسرر الشهر لآخر الشهر حين يستتر الهلال ليلة أو ليلتين","what_is_not_ar":"سر الإنسان؛ السرور؛ سر الوادي"},"support_links":[]},{"boundary":"Anlam yalnızca verilen tamlamalarda ortaya çıkar; yalın köke genel bir öz anlamı yüklenmez.","branch_kind":"collocation","branch_ref":"root_000697/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"bir şeyin arı özü veya en seçkin bölümü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin katkısız, arı özü veya niteliğinin en yoğun bölümü belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk, soy, vadi veya yaşam içinde en seçkin, merkezi ya da elverişli bölüm belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca belirtilen yapılar içinde arılık ile üstün veya merkezi bölüm değerini birlikte taşır.","boundary_detail":"Anlam yalnızca verilen tamlamalarda ortaya çıkar; yalın köke genel bir öz anlamı yüklenmez.","branch_image_ar":"خالص الشيء وأكرم موضعه","concept_gloss":"bir şeyin arı özü veya en seçkin bölümü","contextual_glosses":[{"applicability":"Yapının vadiyi belirttiği ve toprağın ya da konumun üstünlüğünün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arı öz, seçkin topluluk, soy ve iyi yaşam kullanımlarını dışarıda bırakır.","preserves":"Bir bütün içindeki en iyi ve elverişli bölümü korur."},"facet_ids":["F002"],"text":"vadinin en iyi yeri","usage_role":"contextual"}],"definition":"Belirli yapılarda bir şeyin katkısız özü ya da bir topluluğun, soyun, yerin veya yaşamın en seçkin, merkezi ve elverişli bölümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin katkısız, arı özü veya niteliğinin en yoğun bölümü belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Topluluk, soy, vadi veya yaşam içinde en seçkin, merkezi ya da elverişli bölüm belirtilir."}],"identity_rationale":"Kaynak ifadesi bir şeyin arı özü ile bir topluluğun veya yerin en seçkin, orta ya da elverişli bölümünü yapı içinde tutarlı biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bir şeyin katkısız özü"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"topluluğunun merkezindeki en seçkin kesim"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"soyun katkısız ve en seçkin kolu"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"vadinin toprağı en iyi veya en elverişli yeri"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir şeyin özü ve üstün niteliğinin çekirdeği"}],"lexicalization_note":"Tanım yalnızca şey, topluluk, soy, vadi ve yaşam gibi belirtilen yapılar içindeki arı veya en iyi bölüm anlamına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel arı öz dalı yapıya bağlı kapsamın sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel öz ve çekirdek anlamına sahiptir; bu dal yalnızca belirli yapılarda yer, soy, topluluk ve yaşamın en iyi bölümünü de belirtir.","focus_only":"Topluluk, soy, vadi ve yaşam gibi belirli yapılarda merkezilik ve elverişlilik de ifade edilir.","gloss":"bir şeyin arı özü","neighbor_only":"Bir şeyin özü ve en arı bölümü yapıdan bağımsız, genel bir adlandırma olarak verilir.","neighbor_ref":"root_001248/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir bütünün katkısız, seçkin veya çekirdek bölümünü gösterebilir."}],"source_phrase_ar":"السر خالص الشيء وسر النسب (maqayis)؛ سر كل شيء خالصه وسر الوادي وسراره أطيبه ترابا (jamhara)؛ في سر قومه أي في أوسطهم وسر الوادي أفضل موضع (sihah)؛ استعير للخالص ومنه سر الوادي وسرارته (mufradat)","source_summary":"Tanıklıklar katkısız öz anlamında birleşir; toplulukta seçkin veya orta kesim, vadide en iyi yer ve yaşamda en iyi durum bu yapıya bağlı görünümlerdir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"سر الشيء وسر النسب وسر القوم وسر الوادي وسرارته وسرارة الفضل والعيش","what_is_not_ar":"الكتمان المجرد؛ السرة؛ السرير"},"support_links":[]},{"boundary":"Anlam hem bedendeki kalıcı yeri hem de doğum sırasında kesilen parçayı içerir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"göbek ve kesilen göbek bağı parçası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göbek bağının kesilmesinden sonra karnın ortasında kalan yer belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bebekten kesilen göbek bağı parçası ve bu parçayı kesme eylemi belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedendeki kalıcı yer ile doğumda kesilen parçayı birlikte karşılayan açıklayıcı üst karşılıktır.","boundary_detail":"Anlam hem bedendeki kalıcı yeri hem de doğum sırasında kesilen parçayı içerir.","branch_image_ar":"سرة البطن وما يقطع منها","concept_gloss":"göbek ve kesilen göbek bağı parçası","contextual_glosses":[{"applicability":"Eylem biçiminin doğumdan sonra göbek bağı parçasını kesmeyi anlattığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karında kalan göbek yerini adlandırma anlamını karşılamaz.","preserves":"Kesilen göbek bağı parçasını ve kesme eylemini korur."},"facet_ids":["F002"],"text":"bebeğin göbek bağını kesmek","usage_role":"contextual"}],"definition":"Karnın ortasında göbek bağının kesilmesinden sonra kalan yer ile doğum sırasında bebekten kesilen göbek bağı parçasıdır; ayrıca bu parçayı kesme eylemini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göbek bağının kesilmesinden sonra karnın ortasında kalan yer belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Bebekten kesilen göbek bağı parçası ve bu parçayı kesme eylemi belirtilir."}],"identity_rationale":"Kaynak ifadesi karındaki göbek yerini, doğumdan sonra kalan bölümü ve bebekten kesilen göbek bağı parçasını açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"göbek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bebekten kesilen göbek bağı parçası"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bebeğin göbek bağı parçasını kesmek"}],"lexicalization_note":"Tanım ad biçimlerindeki göbek ve kesilen parça anlamlarını, kesme eylemini bildiren türemiş kullanımdan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yenidoğan örtüsü dalı göbek bağı parçasıyla karışabilecek doğum dokusunu ayırır.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Komşu dal bebeğin üzerindeki geçici deri örtüsünü, bu dal ise karında kalan göbeği ve kesilen göbek bağı parçasını adlandırır.","focus_only":"Göbek yeri, kesilen göbek bağı parçası ve bu parçanın kesilmesi temel kapsamdadır.","gloss":"yenidoğan üzerindeki deri örtüsü","neighbor_only":"Doğum sırasında bebeğin başı ve elleri üzerinde bulunan ince deri örtüsü anlatılır.","neighbor_ref":"root_001424/B010","relation_type":"thematic","shared_zone":"Her iki dal doğum sırasında bebekle birlikte görülen bedensel bir parçaya ilişkindir."}],"source_phrase_ar":"السرة سرة الإنسان (maqayis)؛ السرة في البطن موضع السرر الذي يقطع من الصبي (jamhara)؛ السر ما تقطعه القابلة من سرة الصبي (sihah)؛ سرة البطن ما يبقى بعد القطع والسر والسرر لما يقطع منها (mufradat)","source_summary":"Tanıklıklar göbekte kalan yer ile bebekten kesilen parçayı birbirinden ayırır ve ilgili kesme eylemini aynı beden alanına bağlar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السرة والسر والسرر لما يبقى أو يقطع من سرة الصبي وموضع السرة في البطن","what_is_not_ar":"سر النسب؛ أسرار الكف؛ سرر الشهر"},"support_links":[]},{"boundary":"Hastalığın deveye özgü olduğu korunmalı, kesin anatomik yeri tek bir bölgeye indirgenmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"devede gövde içi ağrı hastalığı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve veya dişi deveyi etkileyen bir ağrı ya da hastalık belirtilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalığın yeri göbek, göğüs veya göğsün altındaki yastıksı bölüm olarak değişik biçimde verilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deveye özgü hastalığı korur ve tartışmalı anatomik yeri gereksiz biçimde kesinleştirmez.","boundary_detail":"Hastalığın deveye özgü olduğu korunmalı, kesin anatomik yeri tek bir bölgeye indirgenmemelidir.","branch_image_ar":"وجع البعير في باطنه","concept_gloss":"devede gövde içi ağrı hastalığı","contextual_glosses":[{"applicability":"Bağlam rahatsızlığı göğsün altındaki yastıksı bölgeye yerleştirdiğinde hayvanı nitelemek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göbek veya göğüs konumunu veren diğer tanıklıkları dışarıda bırakır.","preserves":"Deveye özgü rahatsızlığı ve gövde içindeki ağrı yerini korur."},"facet_ids":["F001","F002"],"text":"göğüs altı ağrısı bulunan deve","usage_role":"contextual"}],"definition":"Deve veya dişi devede göbek, göğüs ya da göğsün altındaki yastıksı bölüm çevresinde görüldüğü aktarılan bir ağrı veya hastalıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve veya dişi deveyi etkileyen bir ağrı ya da hastalık belirtilir."},{"facet_id":"F002","role":"source_variant","statement":"Hastalığın yeri göbek, göğüs veya göğsün altındaki yastıksı bölüm olarak değişik biçimde verilir."}],"identity_rationale":"Kaynak ifadesi develerde bir hastalık veya ağrıda birleşir, fakat yerini göbek, göğüs ya da göğüs altındaki yastıksı bölüm olarak farklı verir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"devede göbek, göğüs veya göğüs altı ağrısı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bu gövde ağrısına tutulmuş deve"}],"lexicalization_note":"Tanım hastalık adını ve bu hastalığa tutulmuş deveyi bildiren yapıya bağlı kullanımı birbirinden ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli uzuv hastalığı anatomik belirsizliği en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal gövdenin iç veya alt bölgelerindeki değişken bir ağrıyı, komşu dal ise belirli biçimde üst ön bacak hastalığını anlatır.","focus_only":"Rahatsızlık göbek, göğüs veya göğüs altındaki yastıksı bölüm çevresine yerleştirilir.","gloss":"devede üst ön bacak hastalığı","neighbor_only":"Rahatsızlık özellikle devenin üst ön bacak bölümünü etkiler.","neighbor_ref":"root_001023/B007","relation_type":"same_field","shared_zone":"Her iki dal develerde görülen, beden bölümüne bağlanan bir hastalık adıdır."}],"source_phrase_ar":"السرر داء يأخذ البعير في سرته (maqayis)؛ السرر داء يصيب الإبل في صدورها (jamhara)؛ بعير أسر وناقة سراء (sihah)؛ وجع يأخذ في الكركرة (tahdhib)","source_summary":"Tanıklıklar deve hastalığı çekirdeğinde birleşir, ancak rahatsızlığın anatomik yerini göbek, göğüs veya göğüs altı olarak farklılaştırır.","sources":["MQ","JA","SI","TA"],"what_is_ar":"السرر داء أو وجع في البعير أو الناقة مع اختلاف موضعه بين السرة والصدر والكركرة","what_is_not_ar":"السرة المقطوعة؛ التجويف؛ خطوط الكف"},"support_links":[]},{"boundary":"Genel iç bölüm değil, içi boş nesne veya beden ile oyuğa çubuk yerleştirme işlemidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"içi oyuk olma ve oyuğa çubuk yerleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateş çubuğu, boru biçimli çubuk veya insan içi oyuk olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ateş yakma amacıyla oyuk çubuğun içine başka bir çubuk parçası yerleştirilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem oyukluk niteliğini hem de ateş çubuğuna özgü yerleştirme işlemini eksiksiz karşılar.","boundary_detail":"Genel iç bölüm değil, içi boş nesne veya beden ile oyuğa çubuk yerleştirme işlemidir.","branch_image_ar":"جوف الزند والقناة","concept_gloss":"içi oyuk olma ve oyuğa çubuk yerleştirme","contextual_glosses":[{"applicability":"Nitelemenin kamış veya boru biçimli bir çubuğun iç boşluğuna yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan için oyukluk nitelemesini ve oyuğa parça yerleştirme işlemini dışarıda bırakır.","preserves":"İçi oyuk olma niteliğini ve çubuk biçimli nesneyi korur."},"facet_ids":["F001"],"text":"içi oyuk boru biçimli çubuk","usage_role":"contextual"}],"definition":"Bir ateş çubuğunun, boru biçimli çubuğun ya da kişinin içinin oyuk olmasıdır; ayrıca ateş yakmak için çubuğun oyuğuna başka bir parça yerleştirme işlemini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateş çubuğu, boru biçimli çubuk veya insan içi oyuk olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Ateş yakma amacıyla oyuk çubuğun içine başka bir çubuk parçası yerleştirilir."}],"identity_rationale":"Kaynak ifadesi içi oyuk olma niteliğini ateş çubuğu, kamış benzeri boru ve insan için; oyuğa çubuk yerleştirme işlemini de ilgili eylem için destekler.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ateş çubuğunun oyuğuna tutuşturma çubuğu yerleştirmek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"içi oyuk boru biçimli çubuk"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"içi oyuk kişi"}],"lexicalization_note":"Tanım, yapıya bağlı içi oyuk nitelemeleri ile ateş çubuğunun oyuğuna parça yerleştiren eylemi ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel iç boşluk dalı nitelik ile özel işlem sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel iç ve boşluk kavramıdır; bu dal belirli oyuk nitelemeleriyle ateş çubuğuna özgü yerleştirme işlemini birleştirir.","focus_only":"Belirli nesne ve kişilerin oyukluğu ile ateş çubuğunun oyuğuna parça yerleştirme işlemi vardır.","gloss":"bir şeyin içi ve boşluğu","neighbor_only":"Her tür şeyin içi, dibi, karın bölgesi ve iç hacmin genişliği genel olarak adlandırılır.","neighbor_ref":"root_000279/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir nesne veya bedenin iç boşluğu ve oyuk yapısıyla ilgilidir."}],"source_phrase_ar":"سررت الزند وذلك أن يبقى أسر أي أجوف (maqayis)؛ قناة سراء أي جوفاء (maqayis)؛ سر زندك فإنه أسر أي أجوف (sihah)؛ رجل أسر إذا كان أجوف (tahdhib)","source_summary":"Tanıklıklar içi oyuk olma niteliğinde birleşir ve ateş yakma aracında bu oyuğa bir çubuk yerleştirme işlemini aynı çekirdeğe bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"سر الزند إذا جعل في جوفه عود وقدح به والقناة السراء والرجل الأسر بمعنى الأجوف","what_is_not_ar":"السرة؛ السرور؛ السرار القمري"},"support_links":[]},{"boundary":"Anlam avuç ve alın yüzeyindeki doğal çizgilerle sınırlıdır; gizli bilgi anlamına geçmez.","branch_kind":"bare","branch_ref":"root_000697/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"avuç ve alın çizgileri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avuç içinde veya alın ve yüzde görülen doğal çizgi ve kırışıklıklar belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki anatomik yüzeydeki doğal çizgi ve kırışıklıkları kısa ve eksiksiz biçimde karşılar.","boundary_detail":"Anlam avuç ve alın yüzeyindeki doğal çizgilerle sınırlıdır; gizli bilgi anlamına geçmez.","branch_image_ar":"خطوط الكف والجبهة","concept_gloss":"avuç ve alın çizgileri","contextual_glosses":[{"applicability":"Bağlam çizgileri özellikle alın veya yüz yüzeyinde gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Avuç içindeki çizgileri adlandıran kullanımı dışarıda bırakır.","preserves":"Alın ve yüzdeki çizgi veya kırışıklık anlamını korur."},"facet_ids":["F001"],"text":"alın kırışıklıkları","usage_role":"contextual"}],"definition":"Avuç içinin doğal çizgileri ile alın veya yüzde görülen çizgi ve kırışıklıklardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avuç içinde veya alın ve yüzde görülen doğal çizgi ve kırışıklıklar belirtilir."}],"identity_rationale":"Kaynak ifadesi avuç içindeki çizgileri ve alındaki çizgi ya da kırışıklıkları ortak bir beden yüzeyi izi olarak açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"avuç içi çizgileri"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"alın veya yüz çizgileri ve kırışıklıkları"}],"lexicalization_note":"Tanım yalın biçimlerin doğrudan beden çizgisi anlamını verir ve yapıya bağlı başka okumalar eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kat izi dalı doğal beden çizgisi ile oluşmuş yüzey izi ayrımını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal katlama ve kırılmanın nesne yüzeyindeki izidir; bu dal avuç ve alındaki doğal beden çizgileridir.","focus_only":"Çizgiler avuç içi, alın veya yüzün doğal anatomik izleridir.","gloss":"kat ve kırılma izi","neighbor_only":"İz kumaş veya deri gibi bir yüzeyde kırılma ve ilk katlama sonucunda oluşur.","neighbor_ref":"root_001078/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yüzeyde görülen çizgisel kırılma veya kat izini anlatabilir."}],"source_phrase_ar":"الأسرار خطوط باطن الراحة (maqayis)؛ السر والسرار والجميع الأسرار خطوط راحة الكف (ayn)؛ السرر واحد أسرار الكف والجبهة (sihah)؛ أسرة الراحة وأسارير الجبهة (mufradat)","source_summary":"Tanıklıklar avuç içi çizgileri ve alın kırışıklıklarını aynı beden yüzeyi izi alanında birleştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"أسرار الكف وأسراره وأسارير الجبهة وخطوط باطن الراحة والكسور في الجبهة","what_is_not_ar":"السر المكتوم؛ السرة؛ السرر القمري"},"support_links":[]},{"boundary":"Duygusal sevinç ile iyi ve rahat yaşam durumu ayrı görünümler olarak korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B010","candidate_links":[{"candidate_id":"cand_e40a587395ace4f2290b","lane":"micro"},{"candidate_id":"cand_f2dc90488c5856ca37b4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"sevinç ve gönence","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üzüntüden uzak, içte duyulan sevinç ve birini sevindirme durumu belirtilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumu belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal sevinç ile sıkıntının karşıtı olan rahat ve bolluk içindeki durumu birlikte karşılar.","boundary_detail":"Duygusal sevinç ile iyi ve rahat yaşam durumu ayrı görünümler olarak korunmalıdır.","branch_image_ar":"فرح خفي ورخاء","concept_gloss":"sevinç ve gönence","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişide sevinç doğurduğu eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rahatlık, bolluk ve iyi yaşam durumu anlamlarını karşılamaz.","preserves":"Sevinç duygusunu ve bu duygunun bir başkasınca oluşturulmasını korur."},"facet_ids":["F001"],"text":"onu sevindirdi","usage_role":"contextual"}],"definition":"Üzüntünün bulunmadığı, içte duyulan sevinçtir; ayrıca sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumunu belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üzüntüden uzak, içte duyulan sevinç ve birini sevindirme durumu belirtilir."},{"facet_id":"F002","role":"extension","statement":"Sıkıntı ve darlığın karşıtı olan rahatlık, bolluk ve iyi yaşam durumu belirtilir."}],"identity_rationale":"Kaynak ifadesi üzüntüden uzak sevinç ile sıkıntının karşıtı olan gönenceyi aynı dalda açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"üzüntüden uzak iç sevinci"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"beni sevindirdi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"rahatlık, bolluk ve gönence"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"iyilik eden ve sevindiren kişi"}],"lexicalization_note":"Tanım yalın sevinç ve gönence biçimlerini, sevindirme eylemini ve kişiyi niteleyen yapıya bağlı kullanımı ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel sevinç dalı duyguyla gönence arasındaki ek kapsamı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel sevinçtir; bu dal içte duyulan sevinç yanında darlığın karşıtı rahatlık ve bolluk durumunu da taşır.","focus_only":"Sıkıntının karşıtı olan rahatlık, bolluk ve iyi yaşam durumu da kapsanır.","gloss":"sevinç ve coşku","neighbor_only":"Genel sevinç ve coşku, içte kalma veya gönence koşulu olmadan ifade edilir.","neighbor_ref":"root_000158/B002","relation_type":"near_synonym","shared_zone":"Her iki dal üzüntünün karşıtı olan sevinç ve mutlu olma durumunu kapsar."}],"source_phrase_ar":"السرور أمر خال من الحزن (maqayis)؛ السر ضد الضر وقال قوم السر والسرور واحد (jamhara)؛ السراء الرخاء نقيض الضراء (sihah)؛ السرور ما ينكتم من الفرح (mufradat)","source_summary":"Tanıklıklar sevinci üzüntüden uzak bir iç durum olarak verir ve aynı alanı sıkıntının karşıtı olan rahat yaşam ile genişletir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"السرور والمسرة والسراء والسر بمعنى ضد الضر أو موضع الفرح والرخاء","what_is_not_ar":"السر المكتوم؛ النكاح؛ السرير"},"support_links":["sup_3407c64c6d39b6f528e1","sup_90014bef26d3d87ae120"]},{"boundary":"Somut yatak çekirdeği, başın dayanağı ve yaşamın rahat düzeni gibi yapıya bağlı uzantılardan ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000697/B011","candidate_links":[{"candidate_id":"cand_79fae44bab9eac278634","lane":"micro"},{"candidate_id":"cand_e40a587395ace4f2290b","lane":"micro"},{"candidate_id":"cand_fb7373c014385562acde","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"oturma, yaslanma veya dinlenme yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın oturduğu, yaslandığı veya dinlendiği yatak ya da destekli yer belirtilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başın dayandığı yer veya yaşamın yerleşik rahatlığı yapıya bağlı uzantılar olarak belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut yatağı ve dayanak işlevini korurken yapıya bağlı yerleşme uzantılarına temel sağlar.","boundary_detail":"Somut yatak çekirdeği, başın dayanağı ve yaşamın rahat düzeni gibi yapıya bağlı uzantılardan ayrılmalıdır.","branch_image_ar":"موضع الاستقرار والاتكاء","concept_gloss":"oturma, yaslanma veya dinlenme yeri","contextual_glosses":[{"applicability":"Yapı doğrudan başın oturduğu veya dayandığı bölgeyi anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yatak, oturma yeri ve rahat yaşam düzeni anlamlarını dışarıda bırakır.","preserves":"Dayanma ve yerleşme ilişkisini baş bölgesi için korur."},"facet_ids":["F002"],"text":"başın dayandığı yer","usage_role":"contextual"}],"definition":"Oturmak, yaslanmak veya dinlenmek için kullanılan yatak ya da destekli yerdir; yapıya bağlı kullanımlarda başın dayandığı yeri veya yaşamın yerleşik rahatlığını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın oturduğu, yaslandığı veya dinlendiği yatak ya da destekli yer belirtilir."},{"facet_id":"F002","role":"extension","statement":"Başın dayandığı yer veya yaşamın yerleşik rahatlığı yapıya bağlı uzantılar olarak belirtilir."}],"identity_rationale":"Kaynak ifadesi oturulan veya yaslanılan yatağı, başın dayandığı yeri ve yaşamın yerleşik rahatlığını ortak bir dayanma ve yerleşme ilişkisiyle destekler.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturulan, yaslanılan veya yatılan yer"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"başın dayandığı yer"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"yaşamın yerleşik rahatlığı ve dinginliği"}],"lexicalization_note":"Tanım yalın yatak ve oturma desteğini, başın dayandığı yer ile yaşamın yerleşik rahatlığını bildiren yapılardan ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel döşenmiş yatak dalı genel nesne ile özel tür ayrımını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal döşenmiş ve örtülü yerdeki özel yatağa bağlıdır; bu dal daha genel destekli yeri ve mecazlaşmış dayanak uzantılarını içerir.","focus_only":"Genel yatak ve oturma desteği yanında başın dayanağı ve yaşamın rahat düzeni uzantıları vardır.","gloss":"örtülü yerde süslü yatak","neighbor_only":"Özellikle örtülü bir bölmede bulunan döşenmiş ve süslü oturma yatağı belirtilir.","neighbor_ref":"root_000026/B004","relation_type":"near_synonym","shared_zone":"Her iki dal oturmak, yaslanmak veya dinlenmek için hazırlanmış bir yatak türünü kapsar."}],"source_phrase_ar":"السرير وجمعه سرر وأسرة (maqayis)؛ سرير الرأس مستقره (maqayis)؛ السرير معروف والعدد أسرة والجميع السرر (tahdhib)؛ السرير الذي يجلس عليه من السرور (mufradat)","source_summary":"Tanıklıklar oturulan ya da dinlenilen destekli yer çekirdeğinde birleşir; başın dayanağı ve rahat yaşam düzeni bu çekirdeğin yapıya bağlı uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"السرير والسرر والأسرة وسرير الرأس وسرير العيش وما يستقر عليه أو عنده","what_is_not_ar":"سر النسب؛ السرة؛ السرار القمري"},"support_links":["sup_048710b7584aad032ae4","sup_4e77e557afef2f9be10a","sup_90014bef26d3d87ae120"]},{"boundary":"Anlam bitkinin nemli üst bölümleridir; bütün bitkiyi veya yalnızca tek bir ucu anlatmaz.","branch_kind":"collocation","branch_ref":"root_000697/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"bitkinin nemli üst bölümleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitkinin uç veya üst gövde bölümündeki taze ve nemli kısımlar belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Uçlar ile gövdenin üst yarısını ortak tazelik ve nemlilik özelliği altında karşılar.","boundary_detail":"Anlam bitkinin nemli üst bölümleridir; bütün bitkiyi veya yalnızca tek bir ucu anlatmaz.","branch_image_ar":"غضارة أطراف النبات","concept_gloss":"bitkinin nemli üst bölümleri","contextual_glosses":[{"applicability":"Bağlam özellikle hoş kokulu otların en taze uçlarını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bitkilerin gövde üst yarılarını kapsayan daha geniş kullanımı dışarıda bırakır.","preserves":"Bitkinin üst, taze ve nemli kısmını korur."},"facet_ids":["F001"],"text":"hoş kokulu otların nemli uçları","usage_role":"contextual"}],"definition":"Bitkiyi belirten yapıda, hoş kokulu otların en nemli uçları veya bitki gövdelerinin üst yarılarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitkinin uç veya üst gövde bölümündeki taze ve nemli kısımlar belirtilir."}],"identity_rationale":"Kaynak ifadesi bitkinin en nemli uçlarını ve gövdelerin üst yarılarını birlikte verir; geçici dal imgesi yalnızca uçlarla sınırlandırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bitkilerin nemli uçları veya gövdelerinin üst yarıları"}],"lexicalization_note":"Tanım yalnızca bitkiyi belirten yapıda üst, taze ve nemli bölümler anlamını taşır; yalın anlama genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; taze otsu bitki dalı bütün ile üst bölüm arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal otsu bitkinin bütününü, bu dal ise belirli yapı içinde yalnızca üst ve nemli bölümlerini adlandırır.","focus_only":"Bitkinin yalnızca nemli uçları veya gövdesinin üst yarıları belirtilir.","gloss":"taze otsu bitki","neighbor_only":"Ağaç sayılmayan yeşil ve taze otsu bitkinin bütünü adlandırılır.","neighbor_ref":"root_000141/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal yeşil, taze ve nemli bitki dokusuyla ilgilidir."}],"source_phrase_ar":"أطراف الريحان تسمى سرورا لأنها أرطب شيء فيه (maqayis)؛ السرور من النبات أنصاف سوقها العلى (tahdhib)","source_summary":"Tanıklıklar bitkinin üst ve nemli bölümünde birleşir; biri özellikle hoş kokulu otların uçlarını, diğeri gövdelerin üst yarılarını öne çıkarır.","sources":["MQ","TA"],"what_is_ar":"سرور النبات وأطراف الرياحين أو أنصاف سوق النبات العليا الرطبة","what_is_not_ar":"سرور الفرح؛ سرير العيش؛ قشور الكمأة"},"support_links":[]},{"boundary":"Anlam yer mantarının kendisi değil, onun yüzeyine yapışmış kabuk ve toprak örtüsüdür.","branch_kind":"collocation","branch_ref":"root_000697/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"yer mantarı üzerindeki kabuk ve toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer mantarının üzerinde kabuk, çamur veya topraktan oluşan bir yüzey örtüsü bulunur."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mantarın kendisiyle yüzeyine yapışan kabuklu toprak örtüsünü açıkça ayırır.","boundary_detail":"Anlam yer mantarının kendisi değil, onun yüzeyine yapışmış kabuk ve toprak örtüsüdür.","branch_image_ar":"قشور الكمأة وترابها","concept_gloss":"yer mantarı üzerindeki kabuk ve toprak","contextual_glosses":[{"applicability":"Bağlam yüzey örtüsünü mantara yapışmış kabuk ve toprak olarak betimlediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mantar yüzeyi, yapışma, kabuk ve toprak unsurlarının tümünü korur."},"facet_ids":["F001"],"text":"yer mantarına yapışmış topraklı kabuk","usage_role":"contextual"}],"definition":"Yer mantarının yüzeyinde bulunan veya ona yapışan kabuk, çamur ve toprak örtüsüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer mantarının üzerinde kabuk, çamur veya topraktan oluşan bir yüzey örtüsü bulunur."}],"identity_rationale":"Kaynak ifadesi yer mantarının üzerinde bulunan kabuk, çamur ve toprak örtüsünü doğrudan ve tutarlı biçimde tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yer mantarı üzerindeki kabuk, çamur ve toprak"}],"lexicalization_note":"Tanım yalnızca yer mantarını belirten yapıda yüzey kabuğu, çamur ve toprak anlamını taşır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuruyan yer kabuğu dalı mantar yüzeyi ile çevre zemin arasındaki sınırı açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kuruyup ayrılan zemin kabuğunu daha geniş biçimde anlatır; bu dal yalnızca mantarın kendi yüzeyindeki yapışık örtüdür.","focus_only":"Örtü doğrudan yer mantarının üzerinde bulunan kabuk, çamur ve topraktır.","gloss":"kuruyup ayrılan yer kabuğu","neighbor_only":"Kuruyup çatlayan yer veya çamur kabuğu ve yer mantarının üstündeki yükselmiş zemin kabuğu da kapsanır.","neighbor_ref":"root_001250/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal yer mantarı çevresindeki kabuklu toprak oluşumuna değinebilir."}],"source_phrase_ar":"السرر ما على الكمأة من القشور والطين (sihah)؛ السرار ما على الكمأة من القشور والتراب (tahdhib)","source_summary":"Tanıklıklar yer mantarının üzerindeki kabuklu ve topraklı örtüde birleşir; örtünün maddesi çamur veya toprak olarak değişebilir.","sources":["SI","TA"],"what_is_ar":"سرر الكمأة وأسرارها لما عليها من القشور والطين أو التراب","what_is_not_ar":"خطوط الكف؛ سرر الشهر؛ سرر الصبي"},"support_links":[]},{"boundary":"Uzman ve kavrayışlı kişi çekirdeği, yakın ve sevilen kişi anlamıyla özdeşleştirilmemelidir.","branch_kind":"bare","branch_ref":"root_000697/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"işlerin inceliğini bilen becerikli kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir işin inceliklerini bilir, güçlü kavrayış gösterir ve o işe ustalıkla girer."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir kullanım aynı biçim ailesini sevilen veya çok yakın kişi için kullanır."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın baskın uzmanlık ve kavrayış çekirdeğini doğal biçimde karşılar; yakın kişi kullanımı ayrıca gösterilir.","boundary_detail":"Uzman ve kavrayışlı kişi çekirdeği, yakın ve sevilen kişi anlamıyla özdeşleştirilmemelidir.","branch_image_ar":"نفاذ إلى خفايا الأمور","concept_gloss":"işlerin inceliğini bilen becerikli kişi","contextual_glosses":[{"applicability":"Bir kişinin belirli bir işte bilgili, kavrayışlı ve deneyimli olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sevilen veya yakın kişi anlamını ve genel kişi adlandırmasını dışarıda bırakır.","preserves":"Belirli bir işi derinden bilme ve o alanda kavrayışlı olma yönünü korur."},"facet_ids":["F001"],"text":"bu işin bütün inceliklerini bilir","usage_role":"contextual"},{"applicability":"Biçimin bilgi ve uzmanlık değil, sevgi ve yakınlık bildiren hitap olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgili, kavrayışlı ve işlere ustalıkla giren kişi çekirdeğini karşılamaz.","preserves":"Sevilen ve yakın kişi için kullanılan özel hitap değerini korur."},"facet_ids":["F002"],"text":"sevdiğim yakın kişi","usage_role":"contextual"}],"definition":"Bir işin inceliklerini bilen, kavrayışlı ve o işin içine ustalıkla girebilen kişidir; ayrı bir kullanımda sevilen veya çok yakın kişi için söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir işin inceliklerini bilir, güçlü kavrayış gösterir ve o işe ustalıkla girer."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir kullanım aynı biçim ailesini sevilen veya çok yakın kişi için kullanır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü işleri derinden bilen becerikli kişiyi destekler; aynı biçim ailesindeki sevgili veya yakın kişi kullanımı ayrı bir kaynak uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"işlerin inceliğini bilen kavrayışlı kişi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"sevdiğim ve çok yakın bulduğum kişi"}],"lexicalization_note":"Tanım yalın biçimlerdeki bilgili ve becerikli kişi anlamını verir, ayrı sevgi hitabını yalnızca kaynak uzantısı olarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; derin kavrayış dalı yeti ile bu yetiyi taşıyan kişi arasındaki sınırı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bilme ve iç görüş yetisine odaklanır; bu dal bu yetiye sahip becerikli kişiyi adlandırır ve ayrı bir yakınlık kullanımı taşır.","focus_only":"Bilgi bir kişiyi işlerin içine ustalıkla giren uzman olarak niteler ve ayrı yakınlık kullanımı taşır.","gloss":"derin kavrayış","neighbor_only":"Bilme, doğrulama, düşünsel kavrayış ve kanıta dayalı iç görüş bir yeti veya durum olarak anlatılır.","neighbor_ref":"root_000121/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzeyin ötesine geçen bilgi, kavrayış ve bir konuyu derinden anlama alanındadır."}],"source_phrase_ar":"السرسور العالم الفطن (maqayis)؛ السرسور العالم الفطن الدخال في الأمور (sihah)؛ سرسور هذا الأمر إذا كان عالما به (tahdhib)؛ سرسوري وسرسورتي أي حبيبي وخاصتي (tahdhib)","source_summary":"Tanıklıklar bilgili, kavrayışlı ve işlere nüfuz eden kişi çekirdeğinde birleşir; toplu ifade ayrıca sevilen veya yakın kişi kullanımını korur.","sources":["MQ","SI","TA"],"what_is_ar":"السرسور العالم الفطن الدخال في الأمور ومن يقوم على المال أو يكون خاصة وحبيبا","what_is_not_ar":"السرور؛ السرير؛ السرار القمري"},"support_links":[]},{"boundary":"Anlam yükseltinin kendisi değil, onun üzerinde yer alan kumdur.","branch_kind":"bare","branch_ref":"root_000697/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","surface_ar":"سُرُرٌ"}],"gloss":"tepecik üzerindeki kum tabakası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kum, küçük bir tepe veya yükseltinin üzerinde yer alan tabaka olarak belirtilir."}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kumun türünden çok küçük bir yükselti üzerindeki konumunu eksiksiz biçimde belirtir.","boundary_detail":"Anlam yükseltinin kendisi değil, onun üzerinde yer alan kumdur.","branch_image_ar":"رمل على الأكمة","concept_gloss":"tepecik üzerindeki kum tabakası","contextual_glosses":[{"applicability":"Bir metinde küçük yükseltinin üstünü kaplayan kumdan söz edildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kum ile tepe üzerindeki konum ilişkisini tam olarak korur."},"facet_ids":["F001"],"text":"tepenin üstündeki kum","usage_role":"contextual"}],"definition":"Küçük bir tepe veya yükseltinin üzerinde bulunan kum tabakasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kum, küçük bir tepe veya yükseltinin üzerinde yer alan tabaka olarak belirtilir."}],"identity_rationale":"Tek kaynak ifadesi, küçük bir yükseltinin üzerinde bulunan kumu doğrudan ve herhangi bir ek koşul olmadan tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"küçük bir tepenin üzerindeki kum"}],"lexicalization_note":"Tanım yalın biçimin doğrudan küçük yükselti üzerindeki kum anlamını verir ve başka kum oluşumlarını eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüksek kum tepesi dalı taşıyıcı yükselti ile kum oluşumu ayrımını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kumdan oluşan yükseltiyi, bu dal ise önceden var olan küçük yükseltinin üzerindeki kumu adlandırır.","focus_only":"Kum, başka bir küçük yükseltinin üzerinde bulunan tabaka olarak tanımlanır.","gloss":"yüksek kum tepesi","neighbor_only":"Kumun kendisi yükselmiş ve uzaktan belirgin bir kum tepesi oluşturur.","neighbor_ref":"root_001607/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal yükselti ve kumun bir arada bulunduğu yer biçimini anlatır."}],"source_phrase_ar":"السري ما على الأكمة من الرمل (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Küçük bir tepe veya yükselti üzerinde bulunan kum olarak tanıklanır."}],"source_summary":"Bu anlam yalnızca tek sözlük tanıklığına dayanır ve küçük yükselti üzerindeki kumu bildirir.","sources":["MQ"],"what_is_ar":"السري لما يكون على الأكمة من الرمل","what_is_not_ar":"سر الوادي؛ سرار الشهر؛ السرير"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:13:1"],"branch_refs":[],"candidate_id":"cand_fe7123d6e256bfc08bf3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:13:1:container-to-furnishing-sound","source_type":"word_analysis","support_ids":["sup_1b68e2c8bc87923599b9","sup_dc57f0684ec4436b19ec"],"title":"cadence moves from container to furniture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:1","qac_refs":["88:13:1:1","88:13:1:2"],"status":"accepted"}},{"anchor_refs":["88:13:1"],"branch_refs":[],"candidate_id":"cand_28719442b4a93de38f37","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:13:1:feminine-pronoun-resumption","source_type":"word_analysis","support_ids":["sup_2a4f5fb81eb1840c7757","sup_dc57f0684ec4436b19ec"],"title":"pronoun resumes the garden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:1","qac_refs":["88:13:1:1","88:13:1:2"],"status":"accepted"}},{"anchor_refs":["88:13:1"],"branch_refs":[],"candidate_id":"cand_87d71438612d8837a100","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:13:1:fronted-locative-domain","source_type":"word_analysis","support_ids":["sup_070d537d9459c6073a09","sup_dc57f0684ec4436b19ec"],"title":"location first as predicate frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:1","qac_refs":["88:13:1:1","88:13:1:2"],"status":"accepted"}},{"anchor_refs":["88:13:1"],"branch_refs":[],"candidate_id":"cand_8566a124b3f396b9af46","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:13:1:inventory-refrain","source_type":"word_analysis","support_ids":["sup_7f0872121375ddb52129","sup_dc57f0684ec4436b19ec"],"title":"repeated interior catalogue marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:1","qac_refs":["88:13:1:1","88:13:1:2"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_6a06326ac9d765cbba9e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:couch-joy-honor-branch","source_type":"word_analysis","support_ids":["sup_1188ed0109f952f6a9cc","sup_1714db504e561a0e79ea"],"title":"concrete seating with joy pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:2","qac_refs":["88:13:2:1"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_bfc179f8ee95e603482b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:couch-scene-contrasts","source_type":"word_analysis","support_ids":["sup_1188ed0109f952f6a9cc","sup_658e7413368de8c4e734"],"title":"other couch scenes clarify emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:2","qac_refs":["88:13:2:1"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_e14b623788cd838f22fd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:delayed-indefinite-subject","source_type":"word_analysis","support_ids":["sup_1188ed0109f952f6a9cc","sup_38d5aeed48da6bfeee65"],"title":"newly disclosed collective subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:2","qac_refs":["88:13:2:1"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_6576614cb2766eaa2a70","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:inventory-hospitality-progression","source_type":"word_analysis","support_ids":["sup_1188ed0109f952f6a9cc","sup_893b8003ddcf378ed5fe"],"title":"garden becomes furnished rest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:2","qac_refs":["88:13:2:1"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_926b16ff4315c2bcef67","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:liaison-cadence","source_type":"word_analysis","support_ids":["sup_1188ed0109f952f6a9cc","sup_7c6641b39ba7062a28b1"],"title":"sound binds noun to adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:2","qac_refs":["88:13:2:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_4b4d55d2d172f22a417c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:bound-collective-adjective","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_5e523243888b3f3a4727"],"title":"adjective bound to the couch phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_dd0bb0ace77c75c06fb1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:closing-vertical-transformation","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_9751aebb1840f3c05648"],"title":"final word lands on elevation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_fe9dda3a023cd54cbb2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:completed-hospitality-sequence","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_bacf836507d336be7e10"],"title":"prepared rest joins arranged hospitality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_1dcaa90ad8759c7acea2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:height-and-rank","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_9fc06549ff1cd15c1bb5"],"title":"physical height carries dignity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_0b81f6fc89222c3542a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:inter-ayah-elevation-field","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_2b95cbe2746d4564797f"],"title":"elevation field across references","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_3f04a4545561e039c037","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:passive-result-state","source_type":"word_analysis","support_ids":["sup_259fe29a9874f8c214d2","sup_d28b351b555ef1281580"],"title":"received elevation as achieved state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_d1a5e1134bb01a77f78c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:raised-sound-cadence","source_type":"word_analysis","support_ids":["sup_1aa1ae81753919ab8dff","sup_259fe29a9874f8c214d2"],"title":"sound expands into raisedness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:13:3","qac_refs":["88:13:3:1"],"status":"accepted"}},{"anchor_refs":["88:13:2"],"branch_refs":[],"candidate_id":"cand_fab99e76cce6bd16426f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000697"],"scope":"focus_ayah","source_local_id":"88:13:2:1","source_type":"qac_morpheme","support_ids":["sup_d2952785f3f944066387"],"title":"QAC root occurrence: س ر ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:13:3"],"branch_refs":[],"candidate_id":"cand_f30585ad8ac5167e5358","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000582"],"scope":"focus_ayah","source_local_id":"88:13:3:1","source_type":"qac_morpheme","support_ids":["sup_7a4fcb079aba61bc8194"],"title":"QAC root occurrence: ر ف ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:13","branch_refs":["root_000582/B001","root_000697/B011"],"candidate_id":"cand_79fae44bab9eac278634","commentary_obligation":"review","hft_ref":"hft_bde8e96b79a91458c26b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-elevated-settled-support","source_type":"hft","support_ids":["sup_4e77e557afef2f9be10a"],"title":"baseline-elevated-settled-support","trust":"legacy_unbound"},{"anchor_refs":["88:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:13","branch_refs":["root_000582/B002","root_000697/B010","root_000697/B011"],"candidate_id":"cand_e40a587395ace4f2290b","commentary_obligation":"review","hft_ref":"hft_2c382a36f7bdbf401258","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-honored-repose","source_type":"hft","support_ids":["sup_90014bef26d3d87ae120"],"title":"baseline-honored-repose","trust":"legacy_unbound"},{"anchor_refs":["88:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:13","branch_refs":["root_000582/B004","root_000697/B011"],"candidate_id":"cand_fb7373c014385562acde","commentary_obligation":"review","hft_ref":"hft_f11b4d009f09c1378e83","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-presented-hospitality","source_type":"hft","support_ids":["sup_048710b7584aad032ae4"],"title":"baseline-presented-hospitality","trust":"legacy_unbound"},{"anchor_refs":["88:13"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:13","branch_refs":["root_000582/B005","root_000697/B001","root_000697/B010"],"candidate_id":"cand_f2dc90488c5856ca37b4","commentary_obligation":"review","hft_ref":"hft_2159ae9910f0f716615a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-inward-ease-made-public","source_type":"hft","support_ids":["sup_3407c64c6d39b6f528e1"],"title":"baseline-inward-ease-made-public","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:13:1:1","qac_word_ref":"88:13:1","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:13:1:2","qac_word_ref":"88:13:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","root_ar":"س ر ر","surface_ar":"سُرُرٌ"},{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","root_ar":"ر ف ع","surface_ar":"مَّرْفُوعَةٌ"}],"word_analysis_qac_refs":[["88:13:1:1","88:13:1:2"],["88:13:2:1"],["88:13:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:13:1","88:13:2","88:13:3"]},"focus_surface_evidence":{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:13:1:1","qac_word_ref":"88:13:1","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:13:1:2","qac_word_ref":"88:13:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"سُرُر","morph_features":"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:13:2:1","qac_word_ref":"88:13:2","root_ar":"س ر ر","surface_ar":"سُرُرٌ"},{"lemma_ar":"مَّرْفُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:13:3:1","qac_word_ref":"88:13:3","root_ar":"ر ف ع","surface_ar":"مَّرْفُوعَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:13:1:1","88:13:1:2"],["88:13:2:1"],["88:13:3:1"]],"word_analysis_refs":["88:13:1","88:13:2","88:13:3"],"word_rows":[{"analysis_record_ref":"88:13:1","analytic_gloss_range_en":"locative in-it/therein opening that resumes the feminine garden as the interior domain for the disclosed furnishings","analytic_root_gloss_range_en":null,"qac_refs":["88:13:1:1","88:13:1:2"],"root":{},"surface":{"arabic":"فِيهَا","transliteration":"fīhā"}},{"analysis_record_ref":"88:13:2","analytic_gloss_range_en":"indefinite plural couches or honor-seats, locally concrete furniture that also carries prepared repose, joy, and status pressure through its root field and raised qualifier","analytic_root_gloss_range_en":"broad range around inward secrecy, inner joy, ease, and couch or throne seating; the local noun selects the concrete furnishing branch while joy and inward-repose pressure survive as coloring","qac_refs":["88:13:2:1"],"root":{"arabic":"س ر ر","transliteration":"s-r-r"},"surface":{"arabic":"سُرُرٌۭ","transliteration":"sururun"}},{"analysis_record_ref":"88:13:3","analytic_gloss_range_en":"passive participial raised/elevated adjective marking the couches as collectively installed in a received state of physical height and dignity","analytic_root_gloss_range_en":"broad range of lifting, physical height, exalted rank, presentation, public raising of voice or report, and other specialized branches; the local form selects received elevation of the couches, with rank pressure surviving through visible height","qac_refs":["88:13:3:1"],"root":{"arabic":"ر ف ع","transliteration":"r-f-ʿ"},"surface":{"arabic":"مَّرْفُوعَةٌۭ","transliteration":"marfūʿatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:13"],"branch_refs":["root_000582/B001","root_000697/B011"],"candidate_id":"cand_79fae44bab9eac278634","evidence_scope":"focus_ayah","hft_ref":"hft_bde8e96b79a91458c26b","item_id":"baseline-elevated-settled-support","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-elevated-settled-support","support_id":"sup_4e77e557afef2f9be10a"},{"anchor_refs":["88:13"],"branch_refs":["root_000582/B002","root_000697/B010","root_000697/B011"],"candidate_id":"cand_e40a587395ace4f2290b","evidence_scope":"focus_ayah","hft_ref":"hft_2c382a36f7bdbf401258","item_id":"baseline-honored-repose","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-honored-repose","support_id":"sup_90014bef26d3d87ae120"},{"anchor_refs":["88:13"],"branch_refs":["root_000582/B004","root_000697/B011"],"candidate_id":"cand_fb7373c014385562acde","evidence_scope":"focus_ayah","hft_ref":"hft_f11b4d009f09c1378e83","item_id":"baseline-presented-hospitality","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-presented-hospitality","support_id":"sup_048710b7584aad032ae4"},{"anchor_refs":["88:13"],"branch_refs":["root_000582/B005","root_000697/B001","root_000697/B010"],"candidate_id":"cand_f2dc90488c5856ca37b4","evidence_scope":"focus_ayah","hft_ref":"hft_2159ae9910f0f716615a","item_id":"baseline-inward-ease-made-public","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-inward-ease-made-public","support_id":"sup_3407c64c6d39b6f528e1"}],"diagnostics":[],"lane_counts":{"global":15,"macro":9,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:13","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:13","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"88:13","lane":"micro","linguistic_source_ref":"88:13","surface_ref":"88:13","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:13","target_tokens":[["Orada",["88:13:1"]],["yükseltilmiş",["88:13:3"]],["sedirler",["88:13:2"]],["vardır",["88:13:1","88:13:2"]]],"text":"Orada yükseltilmiş sedirler vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:1:fronted-locative-domain","source_type":"word_analysis","support_id":"sup_070d537d9459c6073a09","text":"{\"blocking_evidence\":null,\"headline\":\"location first as predicate frame\",\"reader_payoff\":\"The reader notices that the ayah first reopens the garden interior and only then discloses what is found there.\",\"reason\":\"The QAC and attachment evidence parse the opening phrase as a fronted locative predicate for the delayed subject, so the location-first discovery reading is locally licensed.\",\"representative_source_ids\":[\"QG-0d94bc28\",\"QG-8c75b47c\",\"QT-44a1ecf1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2","source_type":"word_analysis","support_id":"sup_1188ed0109f952f6a9cc","text":"{\"gloss_range\":\"indefinite plural couches or honor-seats, locally concrete furniture that also carries prepared repose, joy, and status pressure through its root field and raised qualifier\",\"prose\":\"{{ar:سُرُرٌۭ}} ({{tr:sururun}}) is not the object of the preposition; it is the delayed subject disclosed after {{ar:فِيهَا}} ({{tr:fīhā}}), so the garden interior yields a newly encountered class of furnishings. The plural gives abundance without making each couch the focus, and {{ar:مَّرْفُوعَةٌۭ}} ({{tr:marfūʿatun}}) immediately frames that furniture as dignified seating, not mere comfort; the tanwīn-to-mīm join also makes the noun flow audibly into its raised qualifier. The root field is broader than furniture, with joy and inwardness nearby, but the local form selects couches or honor-seats; that means the joy pressure is materialized as prepared repose rather than stated as an abstract emotion. The word also turns the inventory from flowing provision into usable hospitality, opening a sequence of arranged objects that continues with vessels set in place (88:14). Other couch scenes sharpen the local emphasis: 15:47 stresses facing one another, 56:15 stresses woven luxury, while 88:13 stresses elevated dignity.\",\"root_display\":\"{{ar:س ر ر}} ({{tr:s-r-r}})\",\"root_gloss_range\":\"broad range around inward secrecy, inner joy, ease, and couch or throne seating; the local noun selects the concrete furnishing branch while joy and inward-repose pressure survive as coloring\",\"surface_display\":\"{{ar:سُرُرٌۭ}} ({{tr:sururun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2:couch-joy-honor-branch","source_type":"word_analysis","support_id":"sup_1714db504e561a0e79ea","text":"{\"blocking_evidence\":null,\"headline\":\"concrete seating with joy pressure\",\"reader_payoff\":\"The reader notices that the word means concrete couches or honor-seats while still letting the root's joy and inward-repose field color the furniture.\",\"reason\":\"The local noun form and raised adjective select the concrete couch/throne branch, while the broader root field supports joy and inward-repose pressure without replacing the local furniture sense.\",\"representative_source_ids\":[\"QS-1a63c7ff\",\"QS-ae58b7a9\",\"QF-04b5bf44\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:raised-sound-cadence","source_type":"word_analysis","support_id":"sup_1aa1ae81753919ab8dff","text":"{\"blocking_evidence\":null,\"headline\":\"sound expands into raisedness\",\"reader_payoff\":\"The reader notices the final descriptor stretching and weighing the line as the furniture is lifted in description.\",\"reason\":\"The sound rows are tied to the actual final adjective and support the same closing elevation payoff without creating a separate lexical sense.\",\"representative_source_ids\":[\"QP-4565aabe\",\"QP-840d3604\",\"MP-ce95990c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:1:container-to-furnishing-sound","source_type":"word_analysis","support_id":"sup_1b68e2c8bc87923599b9","text":"{\"blocking_evidence\":null,\"headline\":\"cadence moves from container to furniture\",\"reader_payoff\":\"The reader notices that the sound and boundary allow the location to stand before the compact plural furniture arrives.\",\"reason\":\"The sound rows are modest but coherent with the same location-first syntax; they add an audible version of the container-to-contained movement.\",\"representative_source_ids\":[\"QP-a4d834b9\",\"QP-dbe49151\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3","source_type":"word_analysis","support_id":"sup_259fe29a9874f8c214d2","text":"{\"gloss_range\":\"passive participial raised/elevated adjective marking the couches as collectively installed in a received state of physical height and dignity\",\"prose\":\"{{ar:مَّرْفُوعَةٌۭ}} ({{tr:marfūʿatun}}) closes the ayah by making elevation the final impression of the furnished scene. As a passive participial adjective, it presents the couches as already raised, with the raiser left outside the clause and the achieved state placed before the reader; the feminine singular agreement gathers the many couches under one shared raised quality. The word does not force a choice between height and honor: the furniture is spatially lifted and dignified by that visible height. The echo with the high garden (88:10) brings elevation down into the furnishings, while the later question about the raised sky (88:18) keeps the same root field alive at a larger scale. Parallels such as raised bedding (56:34) and elevated mention (94:4) clarify the range, but here the local grammar keeps the focus on couches bearing a completed, received elevation. The heavier final descriptor stretches the line into raisedness, and the passive completed arrangement anticipates the cups set in place next (88:14).\",\"root_display\":\"{{ar:ر ف ع}} ({{tr:r-f-ʿ}})\",\"root_gloss_range\":\"broad range of lifting, physical height, exalted rank, presentation, public raising of voice or report, and other specialized branches; the local form selects received elevation of the couches, with rank pressure surviving through visible height\",\"surface_display\":\"{{ar:مَّرْفُوعَةٌۭ}} ({{tr:marfūʿatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:1:feminine-pronoun-resumption","source_type":"word_analysis","support_id":"sup_2a4f5fb81eb1840c7757","text":"{\"blocking_evidence\":null,\"headline\":\"pronoun resumes the garden\",\"reader_payoff\":\"The reader notices that the furnishings remain dependent on the same feminine garden frame introduced earlier rather than floating as a separate reward image.\",\"reason\":\"The attachment evidence strongly licenses the suffix as continuing the feminine garden reference, especially the garden named in 88:10.\",\"representative_source_ids\":[\"QG-a33e0568\",\"MT-5604aefb\",\"QB-862272a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:inter-ayah-elevation-field","source_type":"word_analysis","support_id":"sup_2b95cbe2746d4564797f","text":"{\"blocking_evidence\":null,\"headline\":\"elevation field across references\",\"reader_payoff\":\"The reader notices that the same elevation root can link reward furniture with high garden, raised sky, raised bedding, and elevated mention, while the local phrase remains about couches.\",\"reason\":\"The inter-ayah rows name concrete references, but they serve as range and echo evidence; local grammar keeps the selected sense as the raised state of couches in 88:13.\",\"representative_source_ids\":[\"QI-79ec934e\",\"MI-d3fa99b2\",\"MI-505478f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2:delayed-indefinite-subject","source_type":"word_analysis","support_id":"sup_38d5aeed48da6bfeee65","text":"{\"blocking_evidence\":null,\"headline\":\"newly disclosed collective subject\",\"reader_payoff\":\"The reader notices the couches as newly disclosed contents inside the garden, not as the governed object of the opening preposition.\",\"reason\":\"The word is nominative and functions as the delayed subject of the fronted locative predicate; its indefiniteness and plural form make the furniture newly disclosed and class-like.\",\"representative_source_ids\":[\"QG-7cf99d3d\",\"QG-99c555b3\",\"QG-beabaff3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:bound-collective-adjective","source_type":"word_analysis","support_id":"sup_5e523243888b3f3a4727","text":"{\"blocking_evidence\":null,\"headline\":\"adjective bound to the couch phrase\",\"reader_payoff\":\"The reader notices that raisedness belongs to the couches collectively as their qualifier, not as a separate comment on the garden.\",\"reason\":\"QAC and attachment evidence identify the word as an indefinite feminine singular nominative adjective modifying the nonhuman broken plural couch noun.\",\"representative_source_ids\":[\"QG-549c4b99\",\"QG-b0483e8d\",\"QF-e636f7b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2:couch-scene-contrasts","source_type":"word_analysis","support_id":"sup_658e7413368de8c4e734","text":"{\"blocking_evidence\":null,\"headline\":\"other couch scenes clarify emphasis\",\"reader_payoff\":\"The reader notices that this couch scene is shaped by elevation, whereas other couch scenes highlight social facing (15:47) or woven luxury (56:15).\",\"reason\":\"The concrete inter-ayah rows name valid couch-scene contrasts; they clarify local emphasis without controlling the grammar of 88:13.\",\"representative_source_ids\":[\"MI-149af95d\",\"MI-5bf20fac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:13:3:1","source_type":"qac_morpheme","support_id":"sup_7a4fcb079aba61bc8194","text":"{\"lemma_ar\":\"مَّرْفُوعَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|LEM:m~arofuwEap|ROOT:rfE|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"88:13:3:1\",\"qac_word_ref\":\"88:13:3\",\"root_ar\":\"ر ف ع\",\"surface_ar\":\"مَّرْفُوعَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2:liaison-cadence","source_type":"word_analysis","support_id":"sup_7c6641b39ba7062a28b1","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds noun to adjective\",\"reader_payoff\":\"The reader notices that the plural couch noun flows audibly into its raised adjective instead of standing alone.\",\"reason\":\"The sound observations are tied to the actual noun-adjective junction and reinforce the grammatical dependence already established by agreement.\",\"representative_source_ids\":[\"QF-8e8426bb\",\"QP-98024bcb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:1:inventory-refrain","source_type":"word_analysis","support_id":"sup_7f0872121375ddb52129","text":"{\"blocking_evidence\":null,\"headline\":\"repeated interior catalogue marker\",\"reader_payoff\":\"The reader notices the repeated locative opener as a catalogue device that changes the item while preserving one interior garden sphere.\",\"reason\":\"The contextual attachment notes identify the repeated formula as part of the garden-inventory refrain, and the CRITICAL rows give the concrete comparison with the spring in 88:12.\",\"representative_source_ids\":[\"QE-dc36f035\",\"QB-28fe798c\",\"QY-613826d2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:2:inventory-hospitality-progression","source_type":"word_analysis","support_id":"sup_893b8003ddcf378ed5fe","text":"{\"blocking_evidence\":null,\"headline\":\"garden becomes furnished rest\",\"reader_payoff\":\"The reader notices the ayah's movement from contained place to usable hospitality, with rest answering the prior provision and opening the next arranged objects.\",\"reason\":\"The row family follows the local sequence from locative frame to furniture to raised qualifier, and it coheres with the surrounding inventory movement from the spring in 88:12 toward positioned vessels in 88:14.\",\"representative_source_ids\":[\"QS-c7955659\",\"QT-def8473b\",\"QB-59e5b4f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:closing-vertical-transformation","source_type":"word_analysis","support_id":"sup_9751aebb1840f3c05648","text":"{\"blocking_evidence\":null,\"headline\":\"final word lands on elevation\",\"reader_payoff\":\"The reader notices the ayah's sequence ending with elevation: interior, furniture, then the lifted state as the final visual transformation.\",\"reason\":\"The word is the final adjective of the nominal clause, so it completes the local movement from garden interior to furniture to visible raisedness.\",\"representative_source_ids\":[\"QT-69fe9ac1\",\"QT-7e427e4d\",\"QY-6830038d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:height-and-rank","source_type":"word_analysis","support_id":"sup_9fc06549ff1cd15c1bb5","text":"{\"blocking_evidence\":null,\"headline\":\"physical height carries dignity\",\"reader_payoff\":\"The reader notices that the couches are not merely tall objects or abstractly honored seats; physical height and rank reinforce each other.\",\"reason\":\"The root range supports both physical lifting and exalted status, and the local furniture context lets visible height carry dignitary force without leaving the concrete couch scene.\",\"representative_source_ids\":[\"QS-1313e74c\",\"QS-44ee1f06\",\"MS-0b1b1dc6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:completed-hospitality-sequence","source_type":"word_analysis","support_id":"sup_bacf836507d336be7e10","text":"{\"blocking_evidence\":null,\"headline\":\"prepared rest joins arranged hospitality\",\"reader_payoff\":\"The reader notices the shift from active provision to completed arrangement, with raised couches anticipating cups set in place (88:14).\",\"reason\":\"The boundary rows connect the passive completed state of the couches with the surrounding inventory, including the next arranged hospitality item in 88:14.\",\"representative_source_ids\":[\"QB-cfa5f0c3\",\"QB-df25caa1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:3:passive-result-state","source_type":"word_analysis","support_id":"sup_d28b351b555ef1281580","text":"{\"blocking_evidence\":null,\"headline\":\"received elevation as achieved state\",\"reader_payoff\":\"The reader notices an installed result: the couches stand raised, while the act and agent of raising are withheld.\",\"reason\":\"The surface is a passive participial adjective, not a finite passive verb, active participle, or intransitive rising form, so the local payoff is achieved received elevation.\",\"representative_source_ids\":[\"QS-d63dbd5a\",\"QF-ed975341\",\"MF-791ec4d8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:13:2:1","source_type":"qac_morpheme","support_id":"sup_d2952785f3f944066387","text":"{\"lemma_ar\":\"سُرُر\",\"morph_features\":\"STEM|POS:N|LEM:surur|ROOT:srr|MP|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:13:2:1\",\"qac_word_ref\":\"88:13:2\",\"root_ar\":\"س ر ر\",\"surface_ar\":\"سُرُرٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:13:1","source_type":"word_analysis","support_id":"sup_dc57f0684ec4436b19ec","text":"{\"gloss_range\":\"locative in-it/therein opening that resumes the feminine garden as the interior domain for the disclosed furnishings\",\"prose\":\"{{ar:فِيهَا}} ({{tr:fīhā}}) puts the garden interior first, so the couches are discovered inside an already opened domain rather than introduced as detached objects. The suffix keeps the scene tied to the same high garden already named (88:10), and the repeated locative formula from the spring scene (88:12) turns the passage into an accumulating inventory: provision is followed by elevated rest. Even the location-first order matters; the pause-capable boundary lets the container stand first, and the long opening sound releases into the compact plural rhythm of the furnishing.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِيهَا}} ({{tr:fīhā}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000582/B001","root_000697/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_000697","role":"The settled-support image supplies couches as stable places of repose.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Physical upward displacement makes height a concrete property of those supports.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]}],"changed_reading":{"after":"There are stable supports deliberately lifted into an upper position, so their height belongs to the scene's spatial design.","before":"There are couches in the scene."},"confidence":"strong","focus_anchor":"The noun سُرُرٌ and its adjective مَّرْفُوعَةٌ form a compact object-plus-state construction.","mechanism":"The settled-support branch of س ر ر combines with physical upward displacement in ر ف ع: the objects are couches or throne-like supports whose elevation is materially part of their arrangement.","model_id":"baseline-elevated-settled-support"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-elevated-settled-support","source_type":"hft","support_id":"sup_4e77e557afef2f9be10a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000582/B002","root_000697/B010","root_000697/B011"],"payload":{"activation_trace":[{"branch_id":"B010","mapped_root_id":"root_000697","role":"Joy and ease give the couch an affective function beyond furnishing.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B011","mapped_root_id":"root_000697","role":"Settled support keeps the reading anchored in the actual couch noun.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000582","role":"High rank converts elevation into honor and elevated standing.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]}],"changed_reading":{"after":"The couches confer honored, ease-filled station: their elevation is social and affective as well as spatial.","before":"The couches are physically high."},"confidence":"medium","focus_anchor":"The same noun-adjective pair can carry affective and social elevation without losing the couch as its material anchor.","mechanism":"A couch is a place of settled ease; the joy and prosperity branch of س ر ر colors its use, while the rank branch of ر ف ع turns being raised into dignified station rather than geometry alone.","model_id":"baseline-honored-repose"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-honored-repose","source_type":"hft","support_id":"sup_90014bef26d3d87ae120","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000582/B004","root_000697/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_000697","role":"The couch branch supplies the concrete support offered to a recipient.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000582","role":"Bringing near or presenting turns the raised state into prepared availability.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]}],"changed_reading":{"after":"The couches are already presented for reception, with elevation carrying readiness and approach as well as height.","before":"The couches simply occupy a high location."},"confidence":"medium","focus_anchor":"مَّرْفُوعَةٌ modifies the settled supports and can activate presentation or bringing-near within the focus root inventory.","mechanism":"The couches remain places of support, but ر ف ع contributes presentation and approach: they read as prepared supports brought into availability for reception.","model_id":"baseline-presented-hospitality"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-presented-hospitality","source_type":"hft","support_id":"sup_048710b7584aad032ae4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000582/B005","root_000697/B001","root_000697/B010"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000697","role":"Hidden inwardness supplies the concealed interior pole of the reading.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B010","mapped_root_id":"root_000697","role":"Joy and ease identify what the concealed interior can contain.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000582","role":"Announcing or making a report public supplies outward manifestation.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]}],"changed_reading":{"after":"The visible raised couches can be carried as the public form of an inward, previously concealed ease.","before":"The verse names visible furniture and nothing more."},"confidence":"exploratory","focus_anchor":"The lexical breadth of س ر ر and ر ف ع remains attached to the two overt focus words even when it exceeds their immediate furniture sense.","mechanism":"س ر ر holds inward concealment beside joy and ease; ر ف ع can announce or publicize. Their conjunction permits the raised couches to externalize an inward delight that had been hidden.","model_id":"baseline-inward-ease-made-public"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-inward-ease-made-public","source_type":"hft","support_id":"sup_3407c64c6d39b6f528e1","trust":"legacy_unbound"}]}
</lane_packet_json>
