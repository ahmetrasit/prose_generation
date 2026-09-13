# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:22**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_22/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:22",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği düzenli sıra ve sıra sıra yazmadır; adın bulunduğu yazı sırasını aşma anlamındaki özel söz kalıbı çıplak anlama genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000704/B001","candidate_links":[{"candidate_id":"cand_27df44c919fb7f068c31","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"düzenli sıra oluşturma ve yazıyı sıra sıra kayda geçirme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yazı öğeleri, dikili ağaçlar veya ayakta duran insanlar düzenli bir sıra oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yazı, birbirini izleyen düzenli sıralar halinde yazılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yazılmış içerik bir kayda geçirilmiş, sabitlenmiş ve korunmuş olur."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesne sırası ile yazma ve yazılı içeriği sabitleme çekirdeğinin birlikte anlatılması gerektiğinde kullanılır.","boundary_detail":"Dalın çekirdeği düzenli sıra ve sıra sıra yazmadır; adın bulunduğu yazı sırasını aşma anlamındaki özel söz kalıbı çıplak anlama genellenmez.","branch_image_ar":"السطر المصطف المكتوب","concept_gloss":"düzenli sıra oluşturma ve yazıyı sıra sıra kayda geçirme","contextual_glosses":[{"applicability":"Yazı öğeleri, ağaçlar, insanlar veya başka nesnelerin yan yana dizilişi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öğelerin düzenli biçimde birbirini izleyen bir sıra oluşturmasını korur."},"facet_ids":["F001"],"text":"düzenli sıra","usage_role":"general"},{"applicability":"Bir içeriğin birbirini izleyen yazı sıraları halinde yazılması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazma eylemini ve yazının düzenli sıralar halinde kurulmasını korur."},"facet_ids":["F002"],"text":"sıra sıra yazmak","usage_role":"contextual"},{"applicability":"Bir bilginin yazılı kayıtta sabitlenmiş ve saklanmış olduğu vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçeriğin yazılmış, sabitlenmiş ve korunmuş olmasını eksiksiz biçimde korur."},"facet_ids":["F003"],"text":"yazıya geçirilmiş ve korunmuş","usage_role":"explanatory"}],"definition":"Nesnelerin, özellikle yazı öğelerinin, dikili ağaçların veya ayakta duran insanların düzenli bir sıra oluşturmasıdır. Ayrıca yazıyı sıra sıra yazma ve yazılmış olanı kayda geçirip koruma eylemlerini kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yazı öğeleri, dikili ağaçlar veya ayakta duran insanlar düzenli bir sıra oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Yazı, birbirini izleyen düzenli sıralar halinde yazılır."},{"facet_id":"F003","role":"extension","statement":"Yazılmış içerik bir kayda geçirilmiş, sabitlenmiş ve korunmuş olur."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Türkçede et doğrama bıçağı anlamıyla aynı biçimde kullanıldığı için başka dalla karışabilir.","fit":"narrowing","loses":"Ağaç ve insan sıralarını, yazma eylemini ve yazılı içeriğin sabitlenmesini tek başına anlatmaz.","preserves":"Yazıdaki tek bir düzenli çizgi anlamını doğal biçimde korur."},"text":"satır"}],"identity_rationale":"Kaynak ifadesi yalnız yazıdaki çizgiyi değil, kitap yazısının, dikili ağaçların ve ayakta duran insanların oluşturduğu düzenli sıraları da kapsar. Ayrıca yazıyı sıra sıra yazma ile yazılmış olanı kayıtta sabitleme anlamlarını içerir; bu nedenle dalın yazı ağırlıklı ilk çerçevesi daha geniş sıra anlamıyla tamamlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"nesne sırası; yazı sırası veya yazı çizgisi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yazmak; sıra sıra yazıya geçirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yazmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yazılmış, kayda geçirilmiş ve korunmuş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"adımın bulunduğu yazı sırasını geçti"}],"lexicalization_note":"Çıplak biçimlerin sıra ve yazı anlamları ile özel söz kalıbının bir yazı sırasını aşma anlamı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnız yazma, işaretleme ve düzenli yerleştirme sınırını gerçekten keskinleştiren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yazı, daha genel bir düzenli sıra çekirdeğinin özel görünümüdür; komşu dal ise yazma ve yazılı belge alanını sıra koşuluna bağlı olmadan genişletir.","focus_only":"Yazı dışındaki ağaç ve insan sıralarını ve genel sıra düzenini de kapsar.","gloss":"yazı sırası ile genel yazma alanı","neighbor_only":"Yazma, çoğaltma, yazdırma ve yazılı belge adlandırmalarını daha geniş biçimde kapsar.","neighbor_ref":"root_001283/B002","relation_type":"near_synonym","shared_zone":"Her iki dal yazma eylemini ve yazılı bir ürünün ortaya çıkmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dalın belirleyici özelliği öğelerin sıra oluşturmasıdır; komşu dal çeşitli yazma ve işaretleme işlemlerini sıra şartı olmadan kapsar.","focus_only":"Ağaç ve insan sıraları ile içeriği sıra sıra yazma çekirdeğini içerir.","gloss":"düzenli yazı sırası ile işaretleme","neighbor_only":"Harfleri noktalama, belgeyi mühürleme, kumaşı damgalama ve kayıtları numaralama gibi işlemleri içerir.","neighbor_ref":"root_000587/B001","relation_type":"near_synonym","shared_zone":"İki dal yazı çizgisi, yazılı kayıt ve yazma işlemi çevresinde kesişir."},{"boundary_match":"partial","distinction":"Odak dalda öğeler bir sıra boyunca dizilir ve yazı alanına uzanır; komşu dalda temel işlem şeyleri birbirine eklemek veya üst üste koymaktır.","focus_only":"Yazı sırası kurmayı, yazmayı ve yazılı içeriği sabitlemeyi kapsar.","gloss":"sıra oluşturma ile düzenli yığma","neighbor_only":"Eşya veya başka nesneleri birbirine ekleyerek ya da üst üste koyarak düzenler.","neighbor_ref":"root_001515/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal birden çok öğenin düzenli ve uyumlu biçimde yerleştirilmesini anlatır."}],"source_phrase_ar":"أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر (maqayis)؛ السطر سطر من كتب وسطر من شجر مغروس (ayn;tahdhib)؛ السطر الصف من الشيء والخط والكتابة (sihah)؛ السطر والسطر الصف من الكتابة ومن الشجر المغروس ومن القوم الوقوف (mufradat)؛ سطر يسطر إذا كتب (ayn;sihah;tahdhib)؛ كتاب مسطور ومسطورا أي مثبتا محفوظا (mufradat)","source_summary":"Kaynakların ortak anlatımı düzenli sıra fikrini yazı, dikili ağaç ve ayakta duran insan örnekleriyle açıklar; yazma eylemini ve yazılmış içeriğin kayıtta sabitlenmesini de aynı dalda toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صفوف الأشياء وخصوصا أسطر الكتابة والشجر والقوم، وما يكتب سطرا سطرا وما يثبت في كتاب","what_is_not_ar":"أباطيل الأساطير؛ تسلط المسيطر؛ الضرب والقطع؛ المسطار؛ الإخطاء؛ العتود"},"support_links":["sup_89e2d383652e3ed12df4"]},{"boundary":"Dal, asılsız veya düzensiz anlatılar ile temelsiz söz uydurma kullanımını kapsar; genel olarak her kurmaca anlatıya genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000704/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"asılsız veya düzensiz anlatı ve temelsiz söz uydurma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlatı veya söz gerçeğe dayanmaz ve asılsızdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı anlatılar, iç düzeni ve tutarlı kuruluşu bulunmamasıyla nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi hiçbir temeli olmayan söz veya anlatılar üretip ileri sürer."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anlatıların niteliği ile hiçbir temeli olmayan anlatılar üretme eylemi birlikte özetlendiğinde kullanılır.","boundary_detail":"Dal, asılsız veya düzensiz anlatılar ile temelsiz söz uydurma kullanımını kapsar; genel olarak her kurmaca anlatıya genişletilmez.","branch_image_ar":"أساطير الباطل","concept_gloss":"asılsız veya düzensiz anlatı ve temelsiz söz uydurma","contextual_glosses":[{"applicability":"Gerçeğe dayanmayan veya doğruymuş gibi ileri sürülen anlatılar topluca adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anlatıların gerçeğe dayanmayan ve asılsız olma niteliğini korur."},"facet_ids":["F001"],"text":"asılsız anlatılar","usage_role":"general"},{"applicability":"Anlatıların yalanlığından çok iç düzenlerinin bulunmadığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anlatının düzenli ve tutarlı bir kuruluş taşımaması özelliğini korur."},"facet_ids":["F002"],"text":"düzensiz anlatılar","usage_role":"contextual"},{"applicability":"Bir kişinin hiçbir gerçek dayanağı olmayan anlatılar üretmesi veya ileri sürmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temeli olmayan sözleri üretme ve başkalarına ileri sürme eylemini korur."},"facet_ids":["F003"],"text":"temelsiz sözler uydurmak","usage_role":"contextual"}],"definition":"Gerçeğe dayanmayan, asılsız ya da düzenli bir kuruluşu bulunmayan anlatılar ve sözlerdir. Bunun eylem yönü, hiçbir temeli olmayan anlatılar üretip ileri sürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlatı veya söz gerçeğe dayanmaz ve asılsızdır."},{"facet_id":"F002","role":"source_variant","statement":"Bazı anlatılar, iç düzeni ve tutarlı kuruluşu bulunmamasıyla nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Kişi hiçbir temeli olmayan söz veya anlatılar üretip ileri sürer."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kasıtlı aldatma taşımayan ve düzenli kurulmuş edebi anlatıları da kapsar.","collision":"Edebi yaratım alanıyla karışarak asılsızlık yargısını belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Gerçekte yaşanmamış bir anlatı üretme yönünü kısmen korur."},"text":"kurmaca"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anlatı niteliğini, düzen eksikliği seçeneğini ve temelsiz anlatı üretme eylemini eksik bırakır.","preserves":"Gerçeğe aykırılık ve asılsızlık çekirdeğini güçlü biçimde korur."},"text":"yalan"}],"identity_rationale":"Kaynak ifadesi yalnız gerçeğe aykırı anlatıları değil, düzeni bulunmayan anlatıları ve hiçbir temeli olmayan sözler uydurma eylemini de kapsar. Bu unsurlar birbirine yakın olsa da her düzensiz anlatının mutlaka yalan olduğu varsayılmamalı, eylem anlamı da ad anlamından ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz anlatılar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz bir anlatı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz bir anlatı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz bir anlatı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz bir anlatı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"asılsız veya düzensiz bir anlatı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bize gerçeğe aykırı anlatılar getirdi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"hiçbir temeli olmayan şeyler uydurur"}],"lexicalization_note":"Anlatı adları ile temelsiz söz getirme veya uydurma bildiren söz kalıpları ayrıştırılarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yalan, söz uydurma ve daha geniş ürün uydurma alanlarıyla en açıklayıcı üç sınır karşılaştırması seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal anlatı yapısını ve anlatı üretimini öne çıkarır; komşu dal genel yalanı, yalancıyı ve yalanın büyüklüğünü anlatı koşulu olmadan kapsar.","focus_only":"Düzensiz anlatıları ve temelsiz anlatı üretme kullanımını ayrıca kapsar.","gloss":"asılsız anlatı ile genel yalan","neighbor_only":"Kişinin yalancılığı ile çok büyük bir yalanı anlatı biçimine bağlı olmadan kapsar.","neighbor_ref":"root_000041/B002","relation_type":"near_synonym","shared_zone":"İki dal gerçeğe aykırı, asılsız söz ve anlatılar alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal hem ürün olan anlatıları hem üretme kullanımını taşır; komşu dalın çekirdeği ise kişinin yalan bir söz veya anlatı uydurmasıdır.","focus_only":"Ortaya çıkan asılsız veya düzensiz anlatıların adlandırılmasını da kapsar.","gloss":"temelsiz anlatı ile söz uydurma","neighbor_only":"Söz ya da anlatıyı bilerek üretip gerçeğe aykırı biçimde ileri sürme eylemine odaklanır.","neighbor_ref":"root_001450/B013","relation_type":"near_synonym","shared_zone":"Her iki dal hiçbir gerçek dayanağı olmayan bir söz veya anlatının üretilmesini kapsar."},{"boundary_match":"partial","distinction":"Odak dal anlatı ve sözlerle sınırlıdır; komşu dal uydurma eylemini şiir, ezgi ve başka ürünlere kadar genişletir.","focus_only":"Düzeni bulunmayan anlatı çeşidini ve bu anlatıların adını içerir.","gloss":"asılsız anlatı ile geniş kapsamlı uydurma","neighbor_only":"Söz, şiir, ezgi ve başka ürünlerin önceden örneği olmadan kurulmasını daha geniş biçimde kapsar.","neighbor_ref":"root_001167/B004","relation_type":"near_synonym","shared_zone":"Her iki dal yalan veya temelsiz bir içeriğin kurulup ortaya çıkarılması alanında kesişir."}],"source_phrase_ar":"الأساطير أشياء كتبت من الباطل (maqayis)؛ أحاديث تشبه الباطل (ayn;tahdhib)؛ أحاديث لا نظام لها بشيء (ayn)؛ الأساطير الأباطيل (sihah)؛ يسطر ما لا أصل له أي يؤلف (ayn;tahdhib)","source_summary":"Ortak anlatım, gerçeğe dayanmayan anlatıları merkeze alır; bunun yanında düzeni bulunmayan anlatıları ve temelsiz sözler üretme eylemini de aynı anlam alanında gösterir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الأساطير والأحاديث الباطلة أو التي لا نظام لها، وما يؤلف مما لا أصل له","what_is_not_ar":"السطر الحقيقي والكتابة المثبتة؛ السيطرة؛ القطع والضرب؛ المسطار"},"support_links":[]},{"boundary":"Yetki, gözetim, koruma ve sorumluluk birlikte bulunur; yalnız bakma, yalnız koruma veya salt egemenlik bu dalın bütününü karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000704/B003","candidate_links":[{"candidate_id":"cand_651fc01eba55ccdf2d29","lane":"micro"},{"candidate_id":"cand_27df44c919fb7f068c31","lane":"micro"},{"candidate_id":"cand_093b88f38c87580e505e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"gözeten, koruyan ve hesap tutan yetkili denetleyici","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, gözettiği şeyin sorumluluğunu üstlenen yetkili bir denetleyicidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gözetilen şeyi korur, durumlarını izler ve onun üzerinde denetim yetkisi kullanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözetimi altındaki kişilerin yaptıkları işleri yazılı olarak kaydedebilir."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sorumluluk, koruyucu gözetim, denetim yetkisi ve işlerin hesabını tutma birlikte anlatıldığında kullanılır.","boundary_detail":"Yetki, gözetim, koruma ve sorumluluk birlikte bulunur; yalnız bakma, yalnız koruma veya salt egemenlik bu dalın bütününü karşılamaz.","branch_image_ar":"سيطرة الرقيب المتسلط","concept_gloss":"gözeten, koruyan ve hesap tutan yetkili denetleyici","contextual_glosses":[{"applicability":"Bir şeyin sorumluluğunu üstlenmiş, onu koruyup durumlarını izleyen kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin yetkili, sorumlu ve sürekli gözetim yapan konumunu korur."},"facet_ids":["F001","F002"],"text":"yetkili gözetmen","usage_role":"general"},{"applicability":"Bir kişinin topluluk üzerinde denetim kurması ve onların durumlarını izlemesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluk üzerinde yetki kullanma ve gözetim kurma eylemlerini birlikte korur."},"facet_ids":["F001","F002"],"text":"üzerimizde yetki kurup bizi gözetti","usage_role":"contextual"},{"applicability":"Gözetim altındaki kişilerin yaptıklarının yazılı hesabını tutma görevi vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözetlenen kişilerin işlerini yazılı biçimde izleme ve kaydetme görevini korur."},"facet_ids":["F003"],"text":"yapılan işleri kayda geçirmek","usage_role":"explanatory"}],"definition":"Bir şeyin sorumluluğunu üstlenerek onu koruyan, durumlarını gözeten ve üzerinde yetkiyle denetim kuran kişidir. Yapılan işleri kaydetmek, bu gözetim ve hesap sorma görevinin özel bir parçası olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, gözettiği şeyin sorumluluğunu üstlenen yetkili bir denetleyicidir."},{"facet_id":"F002","role":"core","statement":"Gözetilen şeyi korur, durumlarını izler ve onun üzerinde denetim yetkisi kullanır."},{"facet_id":"F003","role":"specialization","statement":"Gözetimi altındaki kişilerin yaptıkları işleri yazılı olarak kaydedebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koruma sorumluluğunu, sürekli gözetimi, durumları izlemeyi ve işlerin hesabını tutmayı kaybeder.","preserves":"Başkaları üzerinde yetki kullanma ve üstün konumda olma yönünü korur."},"text":"egemenlik"}],"identity_rationale":"Kaynak ifadesi, bir şeyin sorumluluğunu üstlenen, onu koruyup gözeten, durumlarını izleyen ve üzerinde yetki kullanan denetleyiciyi anlatır. Gerektiğinde yapılan işleri kaydetmesi bu gözetim görevinin özel bir gerçekleşmesidir; verilen dal çerçevesi bu bileşenleri doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"koruyup gözeten, sorumluluğunu üstlenen yetkili denetleyici"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"durumları izlemekle görevli yetkili gözetmen"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yetkili gözetim, koruma ve denetim"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"üzerimizde yetki kurup durumlarımızı gözetti"}],"lexicalization_note":"Denetleyici kişi ve gözetim adı ile bir topluluk üzerinde yetki kurmayı bildiren söz kalıbı kendi kapsamlarında tutulur.","neighbor_coverage_note":"Bütün adaylar incelendi; koruma, bekçilik ve egemenlik alanlarıyla sınırı en açık gösteren üç ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korumayı yetkili denetim ve hesap sorma konumuyla birleştirir; komşu dalın koruma ve bakım alanı böyle bir üstün yetki gerektirmez.","focus_only":"Gözetilen şey üzerinde denetim yetkisi kullanmayı ve yapılan işleri kaydetmeyi içerir.","gloss":"yetkili denetim ile genel koruma","neighbor_only":"Yetki veya hesap kaydı gerektirmeden genel koruma, bakım, bekçilik ve emanet sorumluluğunu kapsar.","neighbor_ref":"root_000342/B001","relation_type":"near_synonym","shared_zone":"İki dal bir şeyi gözetme, koruma ve onun sorumluluğunu üstlenme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yönetimsel yetki ve sorumluluğa dayanır; komşu dalın çekirdeği tehlikeyi gözlemek ve koruma nöbeti tutmaktır.","focus_only":"Sorumluluk üstlenme, durumları yönetme ve gözetilen üzerinde yetki kullanma öğelerini taşır.","gloss":"denetleyici gözetmen ile bekçi","neighbor_only":"Bekçilik, nöbetçilik ve topluluk adına çevreyi gözleyen öncü görevlerini kapsar.","neighbor_ref":"root_000584/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal koruma amacıyla sürekli dikkat gösteren bir gözetleyiciyi anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir şeyin gözetim ve denetim sorumluluğudur; komşu dal siyasal hükümranlık ve yönetim gücü çevresinde kurulur.","focus_only":"Koruyucu gözetim, durumları izleme ve yapılan işleri kaydetme görevini içerir.","gloss":"denetim görevi ile hükümdarlık","neighbor_only":"Hükümdarlığı, yönetim gücünü ve bu gücün yararlı ya da zararlı sonuçlarını kapsar.","neighbor_ref":"root_001633/B008","relation_type":"same_field","shared_zone":"İki dal başkaları üzerinde yetki ve üstün konum kullanılması alanını paylaşır."}],"source_phrase_ar":"المسيطر المتعهد للشيء المتسلط عليه (maqayis)؛ السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء (ayn;tahdhib)؛ المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله (sihah)؛ المسيطرون الأرباب المسلطون (tahdhib)","source_summary":"Kaynaklar, sorumluluk üstlenen koruyucu gözetleyici ile yetki kullanan denetleyiciyi aynı çekirdekte birleştirir; işlerin yazılı kaydı bu görevin özel bir görünümü olarak sunulur.","sources":["MQ","AY","SI","TA"],"what_is_ar":"المسيطر والمصيطر والرقيب الحافظ المتعهد للشيء والمتسلط عليه، وما يتصل بسيطر وتصيطر","what_is_not_ar":"السطر بمعنى الصف والكتابة؛ الأساطير؛ الضرب والقطع؛ المسطار"},"support_links":["sup_89e2d383652e3ed12df4","sup_b391ed5074b32f3f0e18","sup_ed9ed0a627162755ad22"]},{"boundary":"Çekirdek yere serme veya kılıçla kesmedir; et doğrama bıçağı ve bu işi yapan kişi çekirdeğin türevleridir, bağımsız eylemler değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000704/B004","candidate_links":[{"candidate_id":"cand_567009e631ec6d7e9959","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"yere serme veya kılıçla düz bir iz gibi kesme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi vurularak yere serilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi kılıçla, çizilmiş düz bir iz gibi kesilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Et doğramada kullanılan kesici araç, bu kesme eylemine bağlı olarak adlandırılır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Et doğrayan kişi için de aynı kesme eylemine bağlı adlar kullanılır."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki çekirdek eylemi olan yere serme ve kılıçla çizgi görünümünde kesme birlikte anlatıldığında kullanılır.","boundary_detail":"Çekirdek yere serme veya kılıçla kesmedir; et doğrama bıçağı ve bu işi yapan kişi çekirdeğin türevleridir, bağımsız eylemler değildir.","branch_image_ar":"خط الضرب والقطع","concept_gloss":"yere serme veya kılıçla düz bir iz gibi kesme","contextual_glosses":[{"applicability":"Bir kişinin vurma sonucunda düşürülüp yere serilmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin hedef kişiyi düşürerek yere serme sonucunu eksiksiz korur."},"facet_ids":["F001"],"text":"onu yere serdi","usage_role":"contextual"},{"applicability":"Bir kişinin kılıçla düz bir çizgi görünümünde kesilmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kılıç kullanımını, hedef kişiyi kesmeyi ve düz iz görünümünü korur."},"facet_ids":["F002"],"text":"onu kılıçla boydan boya kesti","usage_role":"contextual"},{"applicability":"Et doğrayan kişinin kullandığı özel kesici araç adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın et doğrama işlevini ve kesici bıçak oluşunu açıkça korur."},"facet_ids":["F003"],"text":"et doğrama bıçağı","usage_role":"contextual"},{"applicability":"Mesleği gereği et kesip doğrayan kişi için kullanılan ad açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin belirleyici işi olan eti kesme ve doğrama görevini korur."},"facet_ids":["F004"],"text":"et doğrayan kişi","usage_role":"contextual"}],"definition":"Birini yere sermek veya kılıçla, çizilmiş düz bir iz bırakır gibi kesmektir. Et doğrama bıçağı ve et doğrayan kişi için verilen adlar, bu kesme imgesine bağlı özel türevlerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi vurularak yere serilir."},{"facet_id":"F002","role":"core","statement":"Bir kişi kılıçla, çizilmiş düz bir iz gibi kesilir."},{"facet_id":"F003","role":"specialization","statement":"Et doğramada kullanılan kesici araç, bu kesme eylemine bağlı olarak adlandırılır."},{"facet_id":"F004","role":"extension","statement":"Et doğrayan kişi için de aynı kesme eylemine bağlı adlar kullanılır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Yazı çizgisi anlamıyla aynı biçimde kullanıldığı için kökün yazı dalıyla karışabilir.","fit":"narrowing","loses":"Yere serme ve kılıçla kesme eylemlerini, ayrıca işi yapan kişi adlarını karşılamaz.","preserves":"Et doğramada kullanılan ağır kesici araç anlamını doğal biçimde korur."},"text":"satır"}],"identity_rationale":"Kaynak ifadesi birini yere serme ve kılıçla, çizilmiş bir çizgiyi andıracak biçimde kesme eylemlerini açıkça bir arada verir. Et doğrayan kişinin bıçağı ile bu işi yapan kişi için kullanılan adlar, kesme eylemine bağlı özel türevlerdir ve dal çerçevesinde bağımlı öğeler olarak tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"onu yere serdi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"onu kılıçla düz bir iz gibi kesti"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"et doğrama bıçağı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"et doğrayan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"et doğrayan kişi"}],"lexicalization_note":"Yere serme biçimi, kılıçla kesme söz kalıbı ve bunlara bağlı araç ile kişi adları ayrı yüzler olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; hedef bölge, kesme biçimi ve kılıcın niteliği bakımından sınırı en iyi gösteren üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düz iz benzerliğine dayanan daha genel kesişi ve yere sermeyi içerir; komşu dal hedeflenen beden bölgesini sınırlar.","focus_only":"Yere sermeyi, çizgi gibi genel kılıç kesişini ve araç ile kişi türevlerini kapsar.","gloss":"genel kılıç kesişi ile boyun vuruşu","neighbor_only":"Vuruşu özellikle sırtın üst bölümüne veya boyna yöneltir.","neighbor_ref":"root_000312/B004","relation_type":"near_synonym","shared_zone":"İki dal bir kişiye kılıçla vurma ve bedeni kesme eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın sınırı çizgi benzerliği ve yere serme ile kurulur; komşu dal kesilen yerin orta bölüm olmasını belirleyici kılar.","focus_only":"Yere serme sonucunu ve kesme eyleminden doğan araç ile kişi adlarını içerir.","gloss":"çizgi gibi kesme ile ortadan kesme","neighbor_only":"Kesişi bedenin ya da nesnenin ortasına ve kimi kullanımlarda yalnız ete yöneltir.","neighbor_ref":"root_000290/B004","relation_type":"near_synonym","shared_zone":"Her iki dal kılıçla vurup kesme ve kesilen yerde belirgin bir iz bırakma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal kişi üzerinde gerçekleşen eylem ve sonucudur; komşu dal ise eylemi yapan kılıcın keskinlik ve geçiş niteliğidir.","focus_only":"Bir kişiyi yere serme veya kılıçla kesme eylemini ve buna bağlı türevleri anlatır.","gloss":"kesme eylemi ile keskin kılıç niteliği","neighbor_only":"Keskin kılıcın vuruş sırasında akıp geçme niteliğini anlatır.","neighbor_ref":"root_001456/B008","relation_type":"near_neighbor","shared_zone":"İki dal kılıcın güçlü ve etkili bir kesme vuruşunda kullanılmasını paylaşır."}],"source_phrase_ar":"سطره أي صرعه (sihah)؛ سطر فلان فلانا بالسيف سطرا إذا قطعه به كأنه سطر مسطور ومنه قيل لسيف القصاب ساطور (tahdhib)؛ يقال للقصاب ساطر وسطار (tahdhib)","source_summary":"Kaynak anlatımı yere serme ile kılıçla kesmeyi çekirdekte birleştirir; et doğrama bıçağı ve et doğrayan kişi adlarını kesme eyleminden doğan özel kullanımlar olarak ekler.","sources":["SI","TA"],"what_is_ar":"سطره بمعنى صرعه، وسطر فلانا بالسيف إذا قطعه به كأنه سطر مسطور، وما يتصل بساطور القصاب وساطر وسطار","what_is_not_ar":"السطر المكتوب؛ الأساطير؛ السيطرة؛ المسطار؛ الإخطاء"},"support_links":["sup_8989cdd0b3c8141782d7"]},{"boundary":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_kind":"unresolved","branch_ref":"root_000704/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir açıklamada söz, içinde ekşilik bulunan bir içecek türünü gösterir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir açıklamada söz, göğe doğru yükselen tozu gösterir ve biçimin başka bir sözcükten gelmiş olabileceği belirtilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üçüncü açıklama hayvanlarla ilgili bir söz verir, ancak sağlanan bağlam anlamı güvenle belirlemeye yetmez."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki dağınık veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu dalın öğeleri genel kök anlamı gibi genişletilmemeli, birbirinin yerine geçebilen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtta verilen biçim veya bağlam sınırı içinde tutulmalıdır.","branch_image_ar":"مسطار مختلف فيه","concept_gloss":"biçime bağlı adlandırmalar","contextual_glosses":[{"applicability":"Yalnız içeceğin tadında belirgin bir ekşilik bulunduğunu söyleyen kaynak açıklaması için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir içecek türünü ve bu içeceğin belirgin ekşilik taşımasını korur."},"facet_ids":["F001"],"text":"ekşimsi bir içecek","usage_role":"contextual"},{"applicability":"Yalnız havaya yükselip gökte görünen toz açıklaması için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toz maddesini ve onun havaya doğru yükselme hareketini korur."},"facet_ids":["F002"],"text":"göğe yükselen toz","usage_role":"contextual"},{"applicability":"Yalnız sağlanan sözün hayvanlarla bağlantısını gösterip kesin anlam çıkarmaktan kaçınmak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanlarla bağlantıyı ve ifadenin anlam bakımından çözülememiş oluşunu korur."},"facet_ids":["F003"],"text":"hayvanlarla ilgili anlamı belirsiz kullanım","usage_role":"explanatory"}],"definition":"Bu dal, ortak anlam çekirdeği doğrulanmamış üç açıklamayı geçici olarak bir arada tutar: ekşimsi bir içecek, göğe yükselen toz ve hayvanlarla ilgili anlamı belirsiz bir söz. Bunlar yapısal inceleme olmadan tek bir sözlük anlamında birleştirilemez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir açıklamada söz, içinde ekşilik bulunan bir içecek türünü gösterir."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir açıklamada söz, göğe doğru yükselen tozu gösterir ve biçimin başka bir sözcükten gelmiş olabileceği belirtilir."},{"facet_id":"F003","role":"source_variant","statement":"Üçüncü açıklama hayvanlarla ilgili bir söz verir, ancak sağlanan bağlam anlamı güvenle belirlemeye yetmez."}],"identity_rationale":"Bu dal packet düzeyinde inceleme statüsünde tutulmuş sınır-riskli malzemeyi taşır. Kanıt, tek bir yalın kök imgesinden çok biçime veya özel kullanıma bağlı dağınık adlandırmaları gösterdiği için dal yapısal bölme şartı koşmadan sınırlı bir adlandırma kümesi olarak okunmalıdır.","lexicalization_note":"Kapsam verilen biçim veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"المسطار بكسر الميم ضرب من الشراب فيه حموضة (sihah)؛ المسطار هو الغبار المرتفع في السماء وقيل كان في الأصل مستطارا (tahdhib)؛ مسطار ماشية لم يعد أن عصرا (tahdhib)","source_summary":"İnceleme statüsündeki kanıt, tek bir birleşik anlamdan çok biçime veya özel bağlama bağlı sınırlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA"],"what_is_ar":"المسطار في قول بمعنى شراب فيه حموضة، وفي قول بمعنى غبار مرتفع أو شراب من ماشية","what_is_not_ar":"ليس من السطر المكتوب ولا من السيطرة؛ وقيل أصله مستطار"},"support_links":[]},{"boundary":"Dal genel yanlış yapma anlamını taşır, ancak söz kalıbındaki kullanım özellikle kişinin yanılmasını dolaylı biçimde bildirmeye bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000704/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"yanlış yapma ve bunu dolaylı yoldan söyleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yanlış yapar ve bu durum belirli bir sözle dolaylı biçimde bildirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem adı, yanlış yapma veya yanılma durumunu doğrudan adlandırır."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yanılma eylemi ile bu eylemi belirli bir söz aracılığıyla örtük biçimde bildirme birlikte özetlendiğinde kullanılır.","boundary_detail":"Dal genel yanlış yapma anlamını taşır, ancak söz kalıbındaki kullanım özellikle kişinin yanılmasını dolaylı biçimde bildirmeye bağlıdır.","branch_image_ar":"الإسْطار في الخطأ","concept_gloss":"yanlış yapma ve bunu dolaylı yoldan söyleme","contextual_glosses":[{"applicability":"Bir kişinin o gün yanıldığını dolaylı bir sözün doğal Türkçe karşılığıyla bildirmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin belirli günde yanlış yapmış olduğu bildirimini korur."},"facet_ids":["F001"],"text":"bugün yanlış yaptı","usage_role":"contextual"},{"applicability":"Eylem adının doğrudan bir yanılma veya doğru sonucu bulamama durumunu göstermesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yanılma ve doğru olandan saparak yanlış bir iş yapma anlamını korur."},"facet_ids":["F002"],"text":"yanlış yapma","usage_role":"general"}],"definition":"Bir kişinin yanlış yapması ve bu yanılmanın belirli bir sözle doğrudan söylenmeden, dolaylı biçimde bildirilmesidir. Aynı dalda bulunan eylem adı doğrudan yanlış yapmayı gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yanlış yapar ve bu durum belirli bir sözle dolaylı biçimde bildirilir."},{"facet_id":"F002","role":"specialization","statement":"Eylem adı, yanlış yapma veya yanılma durumunu doğrudan adlandırır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Hayrete düşme ve beklenmedik bir durum karşısında afallama anlamlarını da getirir.","collision":"Güncel Türkçede hayret duyma anlamı daha baskın olduğu için yanlış yapma çekirdeği bulanıklaşır.","fit":"broadening","loses":null,"preserves":"Doğru yoldan veya doğru düşünceden sapma yönünü kısmen korur."},"text":"şaşırma"}],"identity_rationale":"Kaynak ifadesi, birinin yanlış yaptığını doğrudan söylemek yerine belirli bir sözle dolaylı biçimde anlatmayı ve buna bağlı adın yanlış yapma anlamını açıkça verir. Dal çerçevesi hem söz kalıbının örtük anlatım işlevini hem de eylem adını doğru biçimde sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bugün yanlış yaptı; yanılması dolaylı biçimde söylendi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yanlış yapma, yanılma"}],"lexicalization_note":"Dolaylı anlatım sağlayan söz kalıbı ile yanlış yapmayı adlandıran biçim ayrılır; kalıbın örtük işlevi her kullanıma yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yanılma ile sürçme ve eksiltme alanları, özel dolaylı söyleyişin sınırını en iyi gösteren iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel yanlış yapma anlamının yanında özel bir dolaylı söyleyiş taşır; komşu dal yanılmayı çok daha geniş eylem ve sonuç bağlamlarında anlatır.","focus_only":"Yanlışın belirli bir söz kalıbıyla dolaylı biçimde bildirilmesini içerir.","gloss":"dolaylı yanlış bildirimi ile genel yanılma","neighbor_only":"Yönü şaşırma, istemeden yanlış sonuç doğurma ve kötülüğün kişiyi ıskalamasını dileme gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000420/B001","relation_type":"near_synonym","shared_zone":"İki dal bir kişinin doğru sonuca ulaşamaması ve yanlış yapması çekirdeğinde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalda ayırt edici unsur dolaylı bildirimdir; komşu dal sürçme, düşme ve özellikle yazıdaki eksiltme türlerini ayrıca kapsar.","focus_only":"Birinin yanlışını örtük biçimde haber veren belirli söyleyişe sahiptir.","gloss":"dolaylı yanılma ile sürçme ve eksiltme","neighbor_only":"Söz, yazı veya hesapta sürçme ile harf ya da sözcük düşürme ve çıkarma sonuçlarını kapsar.","neighbor_ref":"root_000719/B003","relation_type":"near_synonym","shared_zone":"Her iki dal sözde, eylemde veya başka bir işte yapılan yanlışı anlatabilir."}],"source_phrase_ar":"يقولون للرجل إذا أخطأ فكنوا عن خطئه أسطر فلان اليوم وهو الإسطار بمعنى الإخطاء (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bir kişinin o gün yanlış yaptığı dolaylı bir sözle bildirilir; buna bağlı eylem adı yanlış yapma anlamındadır."}],"source_summary":"Bu anlam tek bir tanıklıkla sınırlıdır ve hem dolaylı bildirim sağlayan söz kalıbını hem de yanlış yapmayı adlandıran biçimi içerir.","sources":["TA"],"what_is_ar":"قولهم أسطر فلان اليوم، والإسْطار بمعنى الإخطاء","what_is_not_ar":"ليس كتابة السطر ولا أساطير الباطل ولا السيطرة"},"support_links":[]},{"boundary":"Dal yalnız küçükbaş hayvanlardan genç erkek yavruyu adlandırır; türün tamamına, dişi yavruya veya genel hayvan adına genişletilmez.","branch_kind":"bare","branch_ref":"root_000704/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","surface_ar":"مُصَيْطِرٍ"}],"gloss":"genç erkek küçükbaş hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, küçükbaş hayvanlar içinde genç ve erkek bir yavrudur."}}],"root_ar":"س ط ر","root_id":"root_000704","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın küçükbaş oluşu ile gençlik ve erkeklik özelliklerinin birlikte belirtilmesi gerektiğinde kullanılır.","boundary_detail":"Dal yalnız küçükbaş hayvanlardan genç erkek yavruyu adlandırır; türün tamamına, dişi yavruya veya genel hayvan adına genişletilmez.","branch_image_ar":"السطر العتود","concept_gloss":"genç erkek küçükbaş hayvan","contextual_glosses":[{"applicability":"Küçükbaş sürüsündeki genç erkek hayvanı kısa ve doğal biçimde adlandırmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın küçükbaş, genç ve erkek oluşunu açık biçimde korur."},"facet_ids":["F001"],"text":"genç erkek küçükbaş","usage_role":"general"}],"definition":"Küçükbaş hayvanlardan genç erkek bir yavruyu adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, küçükbaş hayvanlar içinde genç ve erkek bir yavrudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Erkeklik koşulunu belirtmeden dişi yavruları da kapsayabilir ve hayvanı yalnız keçi türüne daraltabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Genç bir küçükbaş yavruyu doğal ve kısa biçimde adlandırır."},"text":"oğlak"}],"identity_rationale":"Kaynak ifadesi sözü doğrudan küçükbaş hayvanlardan genç erkek bir hayvanın adı olarak tanımlar. Verilen dal çerçevesi bu tek ve yalın adlandırmayı doğru biçimde yansıtır; yazı, anlatı, denetim veya kesme dallarından herhangi bir anlam buraya taşınmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"genç erkek küçükbaş hayvan"}],"lexicalization_note":"Çıplak biçim genç erkek küçükbaş hayvanı adlandırır ve herhangi bir söz kalıbına bağlı anlam içermeden tanımlanır.","neighbor_coverage_note":"Bütün adaylar incelendi; dişi yavru karşıtı ile keçi ve koyun tür adları, yaş, cinsiyet ve tür sınırlarını en açık gösteren üç ilişkidir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal erkek yavruyu, komşu dal ise dişi yavruyu adlandırır; temel karşıtlık aynı yaş ve hayvan alanındaki cinsiyettir.","focus_only":"Küçükbaş yavrunun erkek olması odak dalın ayırt edici özelliğidir.","gloss":"genç erkek ile genç dişi küçükbaş","neighbor_only":"Küçükbaş yavrunun dişi olması komşu dalın ayırt edici özelliğidir.","neighbor_ref":"root_001053/B010","relation_type":"polarity_pair","shared_zone":"İki dal küçükbaş hayvanların genç yavrularını yaş ve hayvan sınıfı bakımından paylaşır."},{"boundary_match":"field_only","distinction":"Odak dal yaş ve cinsiyetçe sınırlı bir yavru adıdır; komşu dal keçi türünün genel adı ve çeşitli üyelerini kapsayan geniş bir sınıftır.","focus_only":"Gençlik evresi ile erkek cinsiyetini birlikte zorunlu kılar.","gloss":"genç erkek yavru ile keçi türü","neighbor_only":"Keçi türünü, erkeği ve dişiyi, tekili ve topluluğu yaş koşulu olmadan genel olarak kapsar.","neighbor_ref":"root_001433/B001","relation_type":"same_field","shared_zone":"İki dal küçükbaş hayvan ve özellikle keçi alanında aynı canlı grubuna gönderimde bulunabilir."},{"boundary_match":"field_only","distinction":"Odak dal belirli yaş ve cinsiyetteki bireydir; komşu dal yaş ve cinsiyet ayrımı yapmadan koyun türünün genel adlandırmasını verir.","focus_only":"Tek bir genç erkek küçükbaş yavruyu yaş ve cinsiyet özellikleriyle belirtir.","gloss":"genç erkek yavru ile koyun türü","neighbor_only":"Koyun türünü, erkek ve dişi üyeleriyle ve çeşitli çoğul biçimleriyle genel olarak adlandırır.","neighbor_ref":"root_000900/B001","relation_type":"same_field","shared_zone":"İki dal küçükbaş hayvanların koyun çevresindeki adlandırma alanında kesişebilir."}],"source_phrase_ar":"السطر العتود من الغنم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Söz, küçükbaş hayvanlardan genç erkek bir yavrunun adı olarak verilir."}],"source_summary":"Bu hayvan adı tek bir tanıklıkla sınırlı olup küçükbaş hayvanlardan genç erkek bir yavruyu gösterir.","sources":["TA"],"what_is_ar":"السطر بمعنى العتود من الغنم","what_is_not_ar":"ليس السطر المكتوب ولا الأساطير ولا السيطرة ولا المسطار"},"support_links":[]},{"boundary":"Bu dal yalnızca yüklemli olumsuzluk işlevini kapsar; istisna, bağlama olumsuzluğu ve kişi nitelikleri ayrı dallardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B001","candidate_links":[{"candidate_id":"cand_651fc01eba55ccdf2d29","lane":"micro"},{"candidate_id":"cand_567009e631ec6d7e9959","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum ya da niteliğin özne için geçerli olmadığını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Biçimce geçmiş zamanlı ve değişmez bir eylemdir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özneyi yalın durumda, yüklem öğesini belirtme durumunda kullanır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın olumsuzluk, biçim ve söz dizimi özelliklerinin birlikte açıklanması gereken genel kullanımına uygundur.","boundary_detail":"Bu dal yalnızca yüklemli olumsuzluk işlevini kapsar; istisna, bağlama olumsuzluğu ve kişi nitelikleri ayrı dallardır.","branch_image_ar":"ليس جحود ينفي الحال كفعل جامد","concept_gloss":"özneyi yalın, yüklemi belirtme durumunda tutan geçmiş biçimli olumsuzluk eylemi","contextual_glosses":[{"applicability":"Bir özneye yüklenen durum ya da niteliği doğal Türkçe bir cümlede olumsuzlamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynak biçimin geçmiş zaman görünümünü ve öğelerin durumunu yöneten eylem niteliğini açıkça göstermez.","preserves":"Yüklemli olumsuzluk işlevini doğal bir Türkçe karşılıkla korur."},"facet_ids":["F001"],"text":"değildir","usage_role":"contextual"}],"definition":"Biçimce geçmiş zamanlı ve değişmez bir eylem olarak yüklemli olumsuzluk bildirir; özneyi yalın durumda, yüklem öğesini belirtme durumunda tutar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum ya da niteliğin özne için geçerli olmadığını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Biçimce geçmiş zamanlı ve değişmez bir eylemdir."},{"facet_id":"F003","role":"specialization","statement":"Özneyi yalın durumda, yüklem öğesini belirtme durumunda kullanır."}],"identity_rationale":"Kaynak ifadesi bu dalı olumsuzluk bildiren, biçimce geçmiş zamanlı olan ve özne ile yüklem öğesini belirli durumlara sokan değişmez bir eylem olarak kurar. Geçici dal çerçevesi bu dilbilgisel çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"özneyi yalın, yüklem öğesini belirtme durumunda kullanarak olumsuzluk bildiren geçmiş biçimli eylem"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bulunduğu ya da bulunmadığı yerden"}],"lexicalization_note":"Tanım temel dilbilgisel işlevi verir; özel söz öbeğinin bağlama bağlı anlamı bu çekirdeğe genellenmeden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca yüklemli olumsuzluğu istisnadan, özel olumsuzluk kullanımından ve bilinçli inkârdan ayıran üç karşılaştırma sınırı belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bir cümlenin yüklemli olumsuzluğunu eylem gibi kurar; komşu dal ise başka olumsuzluk araçlarının bağlama ya da tümel yokluk işlevinde kullanılır.","focus_only":"Yüklemli olumsuzluk kurar ve özne ile yüklem öğesinin dilbilgisel durumunu yönetir.","gloss":"yüklemli olumsuzluk ile özel olumsuzluk ayrımı","neighbor_only":"Bağlama olumsuzluğu veya bir türün bütünüyle yokluğunu bildiren özel kullanımın yerini tutar.","neighbor_ref":"root_001390/B003","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzluk bildirir ve aynı biçim ailesine dayanır."},{"boundary_match":"partial","distinction":"Bu dal yüklemi olumsuzlar; komşu dal ise ardından gelen öğeyi istisna eder ve olumsuz yüklem kurmak zorunda değildir.","focus_only":"Bir durumun özne için geçerli olmadığını yüklem düzeyinde bildirir.","gloss":"olumsuzlama ile dışarıda bırakma ayrımı","neighbor_only":"Bir öğeyi anılan topluluğun ya da hükmün dışında bırakır.","neighbor_ref":"root_001390/B002","relation_type":"near_neighbor","shared_zone":"İki kullanım aynı dilbilgisel biçimi kullanır ve cümlede bir sınırlandırma etkisi oluşturur."},{"boundary_match":"field_only","distinction":"Bu dalın çekirdeği cümle kuran dilbilgisel olumsuzluktur; komşu dal bilgiye rağmen yapılan iradeli inkârdır.","focus_only":"Tarafsız bir dilbilgisel olumsuzluk işlemi bildirir.","gloss":"dilbilgisel olumsuzluk ile bilinçli inkâr","neighbor_only":"Doğru olduğunu bildiği bir şeyi bilinçli biçimde inkâr eden kişinin tutumunu bildirir.","neighbor_ref":"root_000224/B001","relation_type":"same_field","shared_zone":"Her ikisi de bir içeriği geçersiz sayma ya da reddetme alanıyla ilişkilidir."}],"source_phrase_ar":"ليس كلمة جحود ... معناه لا أيس (ayn;tahdhib)؛ ليس: كلمة نفي، وهو فعل ماض (sihah)؛ تكون بمنزلة كان، ترفع الاسم وتنصب الخبر (tahdhib)","source_summary":"Kaynaklar, bu biçimin olumsuzluk bildirdiği, geçmiş zaman görünümünde olduğu ve özne ile yüklem öğesinin durumunu belirleyen bir eylem gibi işlediği konusunda birleşir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه ليس كلمة جحود أو نفي، وعملها عمل كان فترفع الاسم وتنصب الخبر، وتصريفها بلفظ الماضي دون المستقبل، ودخول الباء في خبرها لتأكيد النفي.","what_is_not_ar":"لا يدخل فيه الاستثناء بليس، ولا ليس بمعنى لا النسقية أو لا التبرئة، ولا أوصاف الأليس."},"support_links":["sup_8989cdd0b3c8141782d7","sup_b391ed5074b32f3f0e18"]},{"boundary":"Dal, yalnızca öğeyi dışarıda bırakan özel dilbilgisel yapıyı kapsar; genel olumsuzluk veya bağımsız bir dışlama kavramı değildir.","branch_kind":"non_bare","branch_ref":"root_001390/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ardından gelen öğeyi daha önce anılan kapsamın dışında bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dışarıda bırakılan öğe belirtme durumunda kullanılır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem dışlama işlemini hem de özel söz dizimsel davranışını birlikte belirtmek gereken yerlerde uygundur.","boundary_detail":"Dal, yalnızca öğeyi dışarıda bırakan özel dilbilgisel yapıyı kapsar; genel olumsuzluk veya bağımsız bir dışlama kavramı değildir.","branch_image_ar":"ليس استثناء يخرج المذكور","concept_gloss":"ardından gelen öğeyi belirtme durumunda dışarıda bırakan istisna yapısı","contextual_glosses":[{"applicability":"Bir topluluktan ya da hükümden tek bir öğeyi doğal Türkçede ayırmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dışarıda bırakılan öğenin kaynak yapıdaki belirtme durumu özelliğini göstermez.","preserves":"Öğeyi verilen kapsamın dışında bırakma işlevini korur."},"facet_ids":["F001"],"text":"dışında","usage_role":"contextual"}],"definition":"Belirli bir söz dizimsel yapıda ardından gelen öğeyi anılan topluluğun ya da hükmün dışında bırakır ve bu öğeyi belirtme durumunda kullanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ardından gelen öğeyi daha önce anılan kapsamın dışında bırakır."},{"facet_id":"F002","role":"specialization","statement":"Dışarıda bırakılan öğe belirtme durumunda kullanılır."}],"identity_rationale":"Kaynak ifadesi, bu kullanımda ardından gelen öğenin dışarıda bırakıldığını ve belirtme durumunda bulunduğunu açıkça belirtir. Geçici çerçeve bu özel istisna işlevini yüklemli olumsuzluktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ardından gelen adı belirtme durumunda kullanarak dışarıda bırakan istisna yapısı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"senin dışında"}],"lexicalization_note":"Tanım, biçimin yalnızca istisna kurduğu özel söz dizimsel kullanıma bağlıdır ve yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel istisna kavramı, başka bir özel istisna aracı ve aynı biçimin yüklemli olumsuzluğu en yararlı sınırları verdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal tek bir özel söz dizimsel aracın istisna işlevidir; komşu dal ise istisna etmenin çeşitli biçim ve alanlarını kapsayan daha geniş kavramdır.","focus_only":"Belirli bir dilbilgisel biçimle kurulur ve dışarıda bırakılan öğeyi belirtme durumunda kullanır.","gloss":"özel istisna yapısı ile genel istisna","neighbor_only":"İstisna işlemini ad, söz, yemin ve alışveriş gibi daha geniş yapılarda kapsar.","neighbor_ref":"root_000208/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bir öğeyi genel kapsamın hükmünden çıkarır."},{"boundary_match":"partial","distinction":"İşlevleri bazı bağlamlarda yaklaşsa da kullanılan araç ve söz dizimsel sınırları ayrıdır; komşu kullanım ayrıca başka bir bağıntı yorumuna açıktır.","focus_only":"Dışarıda bırakılan öğenin belirtme durumunda kullanıldığı bir eylem biçimine bağlıdır.","gloss":"iki özel istisna aracının ayrımı","neighbor_only":"Başka bir özel araçla kurulur ve kaynak yorumuna göre dışlama dışında farklı bir bağıntı da bildirebilir.","neighbor_ref":"root_000167/B003","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir dilbilgisel araçla dışarıda bırakma anlamı verebilir."},{"boundary_match":"partial","distinction":"Bu dal öğeyi kapsam dışında bırakır; komşu dal ise özne ile yüklem arasında olumsuz bir yargı kurar.","focus_only":"Bir öğeyi anılan kapsamdan çıkarır.","gloss":"istisna ile yüklemli olumsuzluk","neighbor_only":"Bir özneye yüklenen durum ya da niteliği olumsuzlar.","neighbor_ref":"root_001390/B001","relation_type":"near_neighbor","shared_zone":"İki dal aynı biçim ailesini ve sınırlandırıcı bir dilbilgisel etkiyi paylaşır."}],"source_phrase_ar":"وقد يستثنى بها، تقول: جاءني القوم ليس زيدا (sihah)؛ يكون استثناء، ينصب به ... بمعنى ما عدا زيدا ... بمعنى إلا زيدا (tahdhib)","source_summary":"Kaynaklar, yapının istisna bildirdiği, ardından gelen öğeyi kapsam dışında bıraktığı ve bu öğeyi belirtme durumunda kullandığı konusunda birleşir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه استعمال ليس للاستثناء بمعنى إلا أو ما عدا، مثل نصب الاسم بعدها في جاءني القوم ليس زيدا.","what_is_not_ar":"لا يدخل فيه نفي الجملة على عمل كان، ولا لا النسقية، ولا أوصاف الأليس."},"support_links":[]},{"boundary":"Bu dal yalnızca belirtilen iki özel dilbilgisel ikameyi kapsar; yüklemli olumsuzluk ve istisna işlevleri dışarıda kalır.","branch_kind":"non_bare","branch_ref":"root_001390/B003","candidate_links":[{"candidate_id":"cand_27df44c919fb7f068c31","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bağlama yapısında sonraki öğeye olumsuzluk yükleyen aracın yerini tutar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir türün hiçbir üyesinin bulunmadığını bildiren genel olumsuzluk aracının yerini tutar."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ayrı özel dilbilgisel çevresini tek üst ifadede göstermek gereken açıklamalarda uygundur.","boundary_detail":"Bu dal yalnızca belirtilen iki özel dilbilgisel ikameyi kapsar; yüklemli olumsuzluk ve istisna işlevleri dışarıda kalır.","branch_image_ar":"ليس تقوم مقام لا في النسق والتبرئة","concept_gloss":"bağlama ya da tümel yokluk bildiren özel olumsuzluk kullanımı","contextual_glosses":[{"applicability":"Bağlanan ikinci öğeyi doğal Türkçede olumsuzlamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir türün bütün üyelerini yok sayan genel olumsuzluk kullanımını kapsamaz.","preserves":"Bağlama yapısındaki olumsuzluk işlevini korur."},"facet_ids":["F001"],"text":"ne de","usage_role":"contextual"},{"applicability":"Bir türün hiçbir üyesinin bulunmadığını doğal Türkçede bildirmek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağlanan ikinci öğeyi olumsuzlama işlevini kapsamaz.","preserves":"Türün bütünüyle yokluğunu bildiren genel olumsuzluğu korur."},"facet_ids":["F002"],"text":"hiçbir","usage_role":"contextual"}],"definition":"Özel dilbilgisel çevrelerde ya bağlanan bir öğeyi olumsuzlar ya da adı geçen türün bütünüyle bulunmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bağlama yapısında sonraki öğeye olumsuzluk yükleyen aracın yerini tutar."},{"facet_id":"F002","role":"specialization","statement":"Bir türün hiçbir üyesinin bulunmadığını bildiren genel olumsuzluk aracının yerini tutar."}],"identity_rationale":"Kaynak ifadesi iki özel işlevi birlikte verir: bağlama sırasında olumsuzluk kurma ve bir türün tamamını yok sayan genel olumsuzluk. Geçici dal çerçevesi bu iki işlevi olağan yüklemli olumsuzluktan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bağlanan öğeyi olumsuzlayan ya da bir türün bütünüyle bulunmadığını bildiren söz"}],"lexicalization_note":"Tanım iki özel dilbilgisel çevreyle sınırlıdır; bunlar biçimin genel ve bağlamdan bağımsız anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel yüklemli olumsuzluk, daha geniş başkalık alanı ve olumsuzluğu bozan cevap aracı bu özel kullanımların sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal iki özel ikame çevresine bağlıdır; komşu dal ise özne ve yüklem ilişkisini doğrudan olumsuzlayan temel kullanımdır.","focus_only":"Bağlama olumsuzluğu ya da bir türün bütünüyle yokluğu için başka bir aracın yerini tutar.","gloss":"özel olumsuzluk ile yüklemli olumsuzluk","neighbor_only":"Özne ile yüklem arasında olumsuz yargı kuran eylem gibi davranır.","neighbor_ref":"root_001390/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir içeriğin geçerli olmadığını dilbilgisel olarak bildirir."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği belirli olumsuzluk görevleridir; komşu dalın çekirdeği başkalık ve ayrılıktır, olumsuzluk bunun yalnızca bir uzantısıdır.","focus_only":"Bağlama ya da tümel yokluk bildiren iki belirli dilbilgisel işleve bağlıdır.","gloss":"özel olumsuzluk ile başkalık alanı","neighbor_only":"Başkalık, karşıtlık, istisna ve olumsuzluğu daha geniş bir anlam alanında birleştirir.","neighbor_ref":"root_001119/B005","relation_type":"near_neighbor","shared_zone":"İki dal da olumsuzluk veya bir öğenin kapsam dışında kalmasıyla ilişkilidir."},{"boundary_match":"thematic_only","distinction":"Bu dal olumsuzluk kurar; komşu dal ise var olan olumsuzluğa cevap vererek onu tersine çevirir.","focus_only":"Bir öğeyi ya da türü olumsuzlar.","gloss":"olumsuzluk ile olumsuzu bozma","neighbor_only":"Önceden kurulmuş olumsuzluğu yanıt içinde bozup olumlu hükmü geri getirir.","neighbor_ref":"root_000154/B010","relation_type":"thematic","shared_zone":"İki dal da olumsuz bir ifadenin dilbilgisel yönetiminde rol oynar."}],"source_phrase_ar":"ربما جاءت ليس بمعنى لا التي ينسق بها؛ وربما جاءت ليس بمعنى لا التبرئة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimin hem bağlama olumsuzluğu hem de bir türü bütünüyle yok sayan genel olumsuzluk işlevinde kullanılabildiğini bildirir."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; iki özel dilbilgisel işlev tek tanıklıkla sınırlıdır.","sources":["TA"],"what_is_ar":"يدخل فيه مجيء ليس بمعنى لا التي ينسق بها، ومجيئها بمعنى لا التبرئة.","what_is_not_ar":"لا يدخل فيه ليس العاملة عمل كان، ولا الاستثناء بليس، ولا أوصاف الأليس."},"support_links":["sup_89e2d383652e3ed12df4"]},{"boundary":"Dal savaşta korkusuz ve rakibine karşı sebatlı kişiyi kapsar; yerinde kalma, yumuşak huyluluk, zayıf yargı ve yergi anlamları ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"savaşta korkmayan ve rakibini bırakmayan yiğit","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Savaş karşısında korkuya kapılmayan yiğit kişiyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşısındaki rakibi bırakmadan mücadelede sebat eder."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu nitelikteki kişi için övgü sözü olarak kullanılabilir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın savaş korkusuzluğu ile rakip karşısındaki sebatını birlikte aktarmak gereken genel açıklamalarda uygundur.","boundary_detail":"Dal savaşta korkusuz ve rakibine karşı sebatlı kişiyi kapsar; yerinde kalma, yumuşak huyluluk, zayıf yargı ve yergi anlamları ayrıdır.","branch_image_ar":"الأليس شجاع لا تروعه الحرب","concept_gloss":"savaşta korkmayan ve rakibini bırakmayan yiğit","contextual_glosses":[{"applicability":"Savaşta korkusuzluk özelliğini doğal ve kısa bir Türkçe ifadeyle öne çıkarmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rakibinden ayrılmama ve mücadeleyi sürdürme koşulunu açıkça belirtmez.","preserves":"Savaş bağlamındaki yiğitlik ve korkusuzluğu korur."},"facet_ids":["F001"],"text":"gözü pek savaşçı","usage_role":"contextual"}],"definition":"Savaşın korkutmadığı ve karşısındaki rakipten ayrılmadan mücadeleyi sürdüren yiğit kişidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Savaş karşısında korkuya kapılmayan yiğit kişiyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Karşısındaki rakibi bırakmadan mücadelede sebat eder."},{"facet_id":"F003","role":"associated_use","statement":"Bu nitelikteki kişi için övgü sözü olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi kişiyi savaşın korkutmadığı, rakibinden ayrılmadığı ve bu nedenle yiğit sayıldığı özelliklerle tanımlar. Geçici çerçeve savaş bağlamındaki korkusuzluk ile sebatı doğru biçimde bir arada tutar.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"savaş karşısında yılmayan yiğitlik"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"savaştan korkmayan ve rakibini bırakmayan yiğit"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz"}],"lexicalization_note":"Tanım savaşta korkusuzluk ve rakibi bırakmama çekirdeğini korur; övgü sözü bu çekirdeğe bağlı özel bir gerçekleşimdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çatışmadan ayrılmayan kişi, genel kahraman ve aynı kökteki yerinden ayrılmama dalı savaşçı yiğitliğin sınırını en iyi belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal korkusuzluğu ve rakip karşısındaki yiğitliği tanımın çekirdeğine alır; komşu dal daha çok çatışma alanından ayrılmama davranışına odaklanır.","focus_only":"Savaşın korkutmaması ve belirli rakibi bırakmama özelliklerini birlikte taşır.","gloss":"korkusuz yiğit ile çatışmadan ayrılmayan kişi","neighbor_only":"Doğrudan çatışma alanından ayrılmama ve savaşa bağlı kalma davranışını öne çıkarır.","neighbor_ref":"root_000304/B012","relation_type":"near_synonym","shared_zone":"Her iki dal da savaşta sebat eden ve çatışmayı bırakmayan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Bu dal savaş ve rakip karşısındaki belirli davranışlarla tanımlanır; komşu dal kahramanlığı daha genel ve tehlikeye atılma yönüyle anlatır.","focus_only":"Savaşın korkutmaması ve rakipten ayrılmama koşullarıyla sınırlıdır.","gloss":"sebatlı savaşçı ile genel kahraman","neighbor_only":"Tehlikeye atılan kahramanı ve yiğitliği savaş dışına da uzanan daha geniş bir çerçevede kapsar.","neighbor_ref":"root_000127/B004","relation_type":"near_synonym","shared_zone":"İki dal da tehlike karşısında cesaret gösteren yiğit kişiyi belirtir."},{"boundary_match":"partial","distinction":"Bu dalda ayrılmama savaşçı sebatıdır; komşu dalda fiziksel bir yerde kalma ve kimi zaman ağır bulunma söz konusudur.","focus_only":"Rakip karşısında savaşmayı sürdürmek olumlu bir yiğitlik niteliğidir.","gloss":"mücadelede sebat ile yerinden ayrılmama","neighbor_only":"Bir yerden ya da evden ayrılmamak ağırlık veya yergi taşıyabilir ve savaş gerektirmez.","neighbor_ref":"root_001390/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bir konumdan ya da karşı karşıya olunan şeyden ayrılmama öğesi vardır."}],"source_phrase_ar":"الأليس وهو الشجاع الذي لا يروعه الحرب (ayn;tahdhib)؛ ورجل أليس، أي شجاع بين الليس (sihah)؛ الأليس الذي لا يبارح قرنه؛ يقال للرجل الشجاع: أهيس أليس (tahdhib)","source_summary":"Kaynaklar savaşın korkutmadığı yiğit kişi çekirdeğinde birleşir; ayrıca rakibi bırakmama ve bu niteliği övgüyle anma ayrıntıları verilir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الأليس والرجل الأليس بمعنى الشجاع الذي لا تروعه الحرب، ولا يبارح قرنه، وما جاء في المدح مثل أهيس أليس إذا أريد به الشجاع.","what_is_not_ar":"لا يدخل فيه الثقل ولزوم البيت أو الحوض، ولا ضعف الرأي، ولا الديوثي الذي لا يغار، ولا استعمال ليس النحوي."},"support_links":[]},{"boundary":"Dal fiziksel bir yerde kalmayı kapsar; savaşta sebat, güçlüğe katlanma ve yumuşak huyluluk bu anlamın parçası değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bulunduğu yerden ayrılmayıp orada kalmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi için yerinden veya evinden ayrılmayan ağır kimseyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develer için su başında kalıp oradan ayrılmamayı anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Evinden ayrılmayan kişi hakkında yergi olarak kullanılabilir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ile hayvan uygulamalarını ortak kalma çekirdeği altında birlikte göstermek gereken genel açıklamalarda uygundur.","boundary_detail":"Dal fiziksel bir yerde kalmayı kapsar; savaşta sebat, güçlüğe katlanma ve yumuşak huyluluk bu anlamın parçası değildir.","branch_image_ar":"الأليس ملازم لا يبرح مكانه","concept_gloss":"yerinden ayrılmayan ağır kişi veya bulunduğu yerde kalan hayvan","contextual_glosses":[{"applicability":"Bir kişinin bulunduğu yerden ya da evinden ayrılmamasını doğal Türkçede anlatmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Develerin su başında kalması uzantısını kapsamaz.","preserves":"Kişinin bir yerde kalıp ayrılmaması özelliğini korur."},"facet_ids":["F001","F002"],"text":"yerinden kımıldamayan kimse","usage_role":"contextual"}],"definition":"Bir kişinin yerinden ya da evinden, develerin ise su başından ayrılmayıp orada kalmasıdır; kişi için ağırlık ve yergi çağrışımı taşıyabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bulunduğu yerden ayrılmayıp orada kalmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Kişi için yerinden veya evinden ayrılmayan ağır kimseyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Develer için su başında kalıp oradan ayrılmamayı anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Evinden ayrılmayan kişi hakkında yergi olarak kullanılabilir."}],"identity_rationale":"Kaynak ifadesi çekirdeği bir yerden ayrılmama olarak kurar ve bunu evinden çıkmayan ağır kişi ile su başında kalan develere uygular. Geçici çerçeve kişi, hayvan ve yergi boyutlarını aynı kalma çekirdeğine bağlı tutar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yerinden ya da evinden ayrılmayan ağır kimse"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"övgüde gözü pek kişi, yergide evinden ayrılmayan kimse için söylenen söz"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"su başında kalıp oradan ayrılmayan develer"}],"lexicalization_note":"Kişinin yerinden ayrılmaması temel nitelik olarak, ev ve su başı kullanımları ise kendi varlık ve yapı sınırları içinde ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabit duran kişi, genel yerleşip kalma, savaşta sebat ve uğraşa devam karşılaştırmaları mekânsal kalma çekirdeğini en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi uygulamasında çekirdekler çok yakındır; bu dal hayvan uzantısı ve değerlendirme taşırken komşu dal hareket etmeme karşıtlığını ayrıca içerir.","focus_only":"Kişide ağırlık veya yergi, ayrıca develerin su başında kalması kapsamını taşır.","gloss":"yerinden ayrılmayan varlık ile sabit duran kişi","neighbor_only":"Yalnızca yerinde duran kişi anlamını, hareket etmemeyi olumsuzlayan ayrı bir kullanımla birlikte verir.","neighbor_ref":"root_000599/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da bulunduğu yerden ayrılmayan kişiyi anlatır."},{"boundary_match":"partial","distinction":"Bu dalın kapsamı belirli kişi ve su başı kullanımlarıyla, kimi zaman yergiyle sınırlıdır; komşu dal genel yerleşip kalma anlamını taşır.","focus_only":"Evinden ayrılmayan ağır kişi ve su başında kalan develer gibi belirli uygulamalara sahiptir.","gloss":"belirli yerde kalma ile genel yerleşip kalma","neighbor_only":"Bir yerde kalmayı kişi, deve ve otlak bağlamlarında daha genel olarak kapsar.","neighbor_ref":"root_000026/B003","relation_type":"near_synonym","shared_zone":"İki dalın çekirdeği kişi ya da hayvanın bulunduğu yerde kalıp ayrılmamasıdır."},{"boundary_match":"partial","distinction":"Bu dal mekânsal kalıcılıktır; komşu dal savaşçı kişinin rakibi bırakmayan olumlu sebatıdır.","focus_only":"Fiziksel bir yerde kalmayı ve kimi zaman ağır bulunmayı bildirir.","gloss":"yerinde kalma ile savaşta sebat","neighbor_only":"Savaşta rakipten ayrılmamayı yiğitlik olarak bildirir.","neighbor_ref":"root_001390/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir yerden ya da karşı karşıya olunan şeyden ayrılmama öğesi bulunur."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği mekânsal olarak ayrılmamaktır; komşu dal yönelme, uğraş ve düzenli devamı da içine alan daha geniş sürekliliktir.","focus_only":"Bir fiziksel yerden ayrılmama durumunu belirtir.","gloss":"mekânda kalma ile uğraşa devam","neighbor_only":"Bir işe veya şeye yönelip onu sürekli sürdürmeyi de kapsar.","neighbor_ref":"root_001038/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeye bağlı kalma ve süreklilik alanındadır."}],"source_phrase_ar":"الأليس الرجل الثقيل الذي لا يبرح مكانه (ayn)؛ الأليس: الذي لا يبرح بيته؛ إبل ليس على الحوض: إذا أقامت عليه فلم تبرحه؛ وبالأليس الذي لا يبرح بيته، وهذا ذم (tahdhib)","source_summary":"Kaynaklar bir yerden ayrılmama çekirdeğinde birleşir; kişi için ağırlık veya evden çıkmama, develer için su başında kalma ve kişi kullanımında yergi ayrıntıları bu çekirdeğe bağlanır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الأليس بمعنى الرجل الثقيل أو الملازم الذي لا يبرح مكانه أو بيته، وإبل ليس على الحوض إذا أقامت عليه فلم تبرحه، وما ذم به من لا يبرح بيته.","what_is_not_ar":"لا يدخل فيه ثبات الشجاع في الحرب، ولا تحمل الخلق والتغاضي، ولا ضعف الرأي، ولا ليس النحوية."},"support_links":[]},{"boundary":"Fiziksel yük taşıma, insanda güçlüğe katlanma, yumuşak huyluluk ve görmezden gelme birlikte kapsanır; bunlar yerinde kalma veya savaşçı cesareti değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B006","candidate_links":[{"candidate_id":"cand_093b88f38c87580e505e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin üzerine yüklenen her şeyi taşıyabilmesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin güçlüğe katlanan ve yumuşak huylu biri olmasını belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Rahatsız edici bir şeyi görmezden gelip üzerinde durmamayı belirtir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yumuşak huylu kişiyi niteleyen özel bir söz öbeğinde kullanılır."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel taşıma ile insana özgü katlanma ve hoşgörülü aşma uzantılarını birlikte göstermek gereken genel açıklamada uygundur.","boundary_detail":"Fiziksel yük taşıma, insanda güçlüğe katlanma, yumuşak huyluluk ve görmezden gelme birlikte kapsanır; bunlar yerinde kalma veya savaşçı cesareti değildir.","branch_image_ar":"تلايس احتمال وتغاض حسن الخلق","concept_gloss":"yük taşıma, güçlüğe katlanma ve rahatsızlığı görmezden gelme","contextual_glosses":[{"applicability":"Kişinin güç bir duruma katlanması veya rahatsız edici bir şeyi büyütmeden geçmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Devenin fiziksel olarak her yükü taşıması anlamını kapsamaz.","preserves":"İnsana özgü katlanma ve görmezden gelme yönlerini korur."},"facet_ids":["F002","F003"],"text":"hoşgörüyle karşılamak","usage_role":"contextual"}],"definition":"Yüklenen şeyi taşıma çekirdeğinden, kişinin güçlüğe katlanıp yumuşak huylu davranmasına ve rahatsız edici bir şeyi görmezden gelerek aşmasına uzanan kullanımları kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin üzerine yüklenen her şeyi taşıyabilmesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Kişinin güçlüğe katlanan ve yumuşak huylu biri olmasını belirtir."},{"facet_id":"F003","role":"extension","statement":"Rahatsız edici bir şeyi görmezden gelip üzerinde durmamayı belirtir."},{"facet_id":"F004","role":"associated_use","statement":"Yumuşak huylu kişiyi niteleyen özel bir söz öbeğinde kullanılır."}],"identity_rationale":"Kaynak ifadesi yalnızca insanın yumuşak huylu oluşunu ve görmezden gelmesini değil, devenin yüklenen her şeyi taşımasını da içerir. Dal korunabilir, ancak fiziksel yük taşıma ile insandaki güçlüğe katlanma ve hoşgörülü davranma aynı üst dayanma ilişkisine bağlı farklı gerçekleşimler olarak ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"üzerine yüklenen her yükü taşıyan deve"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güçlüğe katlanan ve yumuşak huylu olmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"görmezden gelip üzerinde durmamak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yumuşak huylu"}],"lexicalization_note":"Devenin yük taşıması temel fiziksel gerçekleşim, insandaki katlanma ile görmezden gelme ise kendi yapılara bağlı insani gerçekleşimler olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tartışmayı bırakma, sabır, bağışlama ve öfke denetimi karşılaştırmaları yük taşıma ile hoşgörülü katlanma arasındaki özgül bağı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görmezden gelmeyi daha geniş taşıma ve yumuşak huyluluk alanına bağlar; komşu dal doğrudan tartışmayı ve kuşkuyu bırakmaya yönelten bir sözdür.","focus_only":"Fiziksel yük taşıma ile yumuşak huylu katlanmayı da kapsar.","gloss":"görmezden gelme ile tartışmayı bırakma","neighbor_only":"Tartışmayı bırakma, kuşkudan uzaklaşma ve karşıdakini hoş görme yönlendirmesi taşır.","neighbor_ref":"root_000769/B007","relation_type":"near_neighbor","shared_zone":"İki dal da rahatsız edici bir şeyi büyütmeden geçme ve katlanma davranışında buluşur."},{"boundary_match":"partial","distinction":"Bu dal yükü üstlenme ve hoşgörülü geçme eksenindedir; komşu dal kişinin kaygı ve yakınma tepkisini dizginlemesine odaklanır.","focus_only":"Yük taşıma ve rahatsızlığı görmezden gelme uzantılarını içerir.","gloss":"katlanma ile kendini tutma","neighbor_only":"Sarsıntı ve yakınma karşısında kişinin kendini tutmasını, akıl veya değer ölçüsüne bağlı sabrı anlatır.","neighbor_ref":"root_000840/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da güçlük karşısında dayanma ve taşkın tepki vermeme alanındadır."},{"boundary_match":"partial","distinction":"Bu dalda görmezden gelme katlanma davranışıdır; komşu dalda asıl işlem kusuru bağışlamak ve kınamayı bırakmaktır.","focus_only":"Katlanma, yumuşak huyluluk ve yük taşıma anlam alanını birlikte kapsar.","gloss":"görmezden gelme ile bağışlama","neighbor_only":"Bir kusuru bağışlayıp kınamaktan vazgeçmeyi ve ondan yüz çevirmeyi belirtir.","neighbor_ref":"root_000867/B002","relation_type":"near_neighbor","shared_zone":"İki dal da rahatsız edici bir davranışın üzerinde durmamayı içerebilir."},{"boundary_match":"field_only","distinction":"Bu dal yük ve güçlüğü taşıma üzerinden kurulur; komşu dalın çekirdeği öfke ve taşkınlığı akılla denetlemektir.","focus_only":"Fiziksel yük taşıma ile bir şeyi görmezden gelmeye kadar uzanır.","gloss":"yumuşak huyluluk ile öfke denetimi","neighbor_only":"Öfke kabarmasını denetleyen ağırbaşlılık ve akla dayalı özdenetimi anlatır.","neighbor_ref":"root_000352/B001","relation_type":"same_field","shared_zone":"İki dal da yumuşak davranma, sabır ve sert tepkiyi önleme alanında buluşur."}],"source_phrase_ar":"الأليس: البعير يحمل كل ما حمل (sihah)؛ تلايس الرجل: إذا كان حمولا حسن الخلق؛ وتلايست عن كذا وكذا: أي غمضت عنه؛ وفلان أليس دهثم: أي حسن الخلق (tahdhib)","source_summary":"Toplu kanıt fiziksel yük taşıma ile insanın güçlüğe katlanması, yumuşak huylu olması ve bir şeyi görmezden gelmesi arasında uzanan bir anlam alanı verir; ayrıntılar tek kaynaklara bölünebilecek ayrı iddialar halinde sunulmamıştır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه تلايس الرجل إذا كان حمولا حسن الخلق، وتلايست عن كذا إذا غمضت عنه، وفلان أليس دهثم أي حسن الخلق، ومعه الأليس من الإبل الذي يحمل كل ما حمل.","what_is_not_ar":"لا يدخل فيه نفي ليس، ولا الاستثناء، ولا الشجاعة، ولا لزوم المكان، ولا ضعف الرأي."},"support_links":["sup_ed9ed0a627162755ad22"]},{"boundary":"Dal yalnızca görüşü zayıf kişiyi kapsar; genel akıl eksikliği, budalalık veya kararsızlık ancak ayrıca kanıtlanırsa bu sınıra girer.","branch_kind":"bare","branch_ref":"root_001390/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"görüşü ve yargısı zayıf kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin görüş ve yargı gücünün zayıf olmasını belirtir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın ve tek çekirdekli kişi niteliğini doğrudan karşılamak için uygundur.","boundary_detail":"Dal yalnızca görüşü zayıf kişiyi kapsar; genel akıl eksikliği, budalalık veya kararsızlık ancak ayrıca kanıtlanırsa bu sınıra girer.","branch_image_ar":"الأليس ضعيف الرأي","concept_gloss":"görüşü ve yargısı zayıf kişi","contextual_glosses":[{"applicability":"Görüş zayıflığının ileriyi sağlıklı değerlendirememe olarak belirdiği bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görüş zayıflığının öngörü dışındaki bütün biçimlerini kapsamaz.","preserves":"Sağlam değerlendirme yapamama yönünü korur."},"facet_ids":["F001"],"text":"öngörüsüz","usage_role":"contextual"}],"definition":"Sağlam değerlendirme yapamayan, görüşü ve yargısı zayıf kişiyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin görüş ve yargı gücünün zayıf olmasını belirtir."}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan görüş ve yargı zayıflığıyla sınırlar. Geçici çerçeve bu kısa ve yalın kişi niteliğini cesaret, yerinde kalma ve dilbilgisel kullanımlardan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"görüşü zayıf kimse"}],"lexicalization_note":"Tanım, herhangi bir özel söz öbeğinden anlam aktarmadan yalın biçimin görüş zayıflığı anlamıyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sezgi zayıflığına, daha geniş eksikliğe ve budalalığa uzanan yakın anlamlar ile sağlam görüş karşıtlığı dal sınırını en açık biçimde belirledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal görüş zayıflığıyla sınırlıdır; komşu dal sezgi ve kestirim yetisinin zayıflığını veya yanılmasını da içerir.","focus_only":"Yalnızca görüş ve yargı zayıflığını bildirir.","gloss":"görüş zayıflığı ile sezgi zayıflığı","neighbor_only":"Görüşün yanında sezgi zayıflığı ve yanılmasını da kapsar.","neighbor_ref":"root_001193/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin doğru değerlendirme gücündeki eksikliği anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca görüş gücünü niteler; komşu dal akıl ve değer alanına uzanan daha geniş bir eksiklik çerçevesi taşır.","focus_only":"Görüş zayıflığını tek başına kişi niteliği olarak verir.","gloss":"zayıf görüş ile daha geniş eksiklik","neighbor_only":"Görüş kusurunu akıl veya değer alanındaki eksikliklere kadar genişletir.","neighbor_ref":"root_001072/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da görüşün zayıf ve yetersiz olmasını kapsar."},{"boundary_match":"partial","distinction":"Bu dalın kanıtı görüş zayıflığıyla sınırlıdır; komşu dal daha ağır bir zihinsel yetersizlik yargısı ekler.","focus_only":"Budalalık yargısı eklemeden görüşün zayıflığını belirtir.","gloss":"zayıf görüş ile budalalık","neighbor_only":"Görüş zayıflığını budalalıkla birlikte veya onun eşdeğeri olarak sunar.","neighbor_ref":"root_001360/B003","relation_type":"near_synonym","shared_zone":"İki dal da görüşü zayıf kişiyi ifade edebilir."},{"boundary_match":"opposed","distinction":"Bu dal değerlendirme gücünün olumsuz ucunu, komşu dal ise sağlam ve iyi görüşten oluşan olumlu ucunu temsil eder.","focus_only":"Görüşün zayıf ve güvenilmez olmasını bildirir.","gloss":"zayıf görüş ile sağlam görüş","neighbor_only":"Görüşün sağlam, dengeli ve iyi olmasını bildirir.","neighbor_ref":"root_000599/B008","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin görüş ve değerlendirme niteliğini aynı eksende belirler."}],"source_phrase_ar":"الأليس الضعيف الرأي (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, biçimi görüşü ve yargısı zayıf kişi olarak açıklar."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; görüş zayıflığı anlamı tek tanıklıkla sınırlıdır.","sources":["AY"],"what_is_ar":"يدخل فيه الأليس بمعنى ضعيف الرأي.","what_is_not_ar":"لا يدخل فيه الشجاع الأليس، ولا الملازم الذي لا يبرح، ولا ليس النحوية."},"support_links":[]},{"boundary":"Dal, koruyucu kıskançlık göstermeyen erkeğe yönelik yergi ve alayı kapsar; aynı biçimin yiğitlik övgüsü bu dala alınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001390/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","surface_ar":"لَّسْ"}],"gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde niteler."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu nitelikteki kişiye yönelik alaycı ve yergili bir sözde kullanılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçimin başka bir dalda övgü bildirebilmesi, buradaki yergi anlamının bağlamsal sınırını gösterir."}}],"root_ar":"ل ي س","root_id":"root_001390","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişideki eksikliği ve bu eksikliğin aşağılayıcı, alaycı değerlendirilmesini birlikte aktarmak gereken genel açıklamada uygundur.","boundary_detail":"Dal, koruyucu kıskançlık göstermeyen erkeğe yönelik yergi ve alayı kapsar; aynı biçimin yiğitlik övgüsü bu dala alınmaz.","branch_image_ar":"الأليس ذم لمن لا يغار","concept_gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeğe yönelik alaycı yergi","contextual_glosses":[{"applicability":"Kişiye yüklenen olumsuz niteliği açık ve doğal Türkçeyle anlatmak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözün alaycı kalıbını ve açık yergi tonunu tam olarak taşımaz.","preserves":"Erkeğin ailesine karşı koruyucu kıskançlık göstermemesi niteliğini korur."},"facet_ids":["F001"],"text":"ailesini kıskanıp korumayan adam","usage_role":"explanatory"}],"definition":"Ailesini kıskanıp koruma duyarlılığı göstermeyen erkeği aşağılayarak niteler ve bu kişiye yönelik alaycı bir yergi sözü kurar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde niteler."},{"facet_id":"F002","role":"associated_use","statement":"Bu nitelikteki kişiye yönelik alaycı ve yergili bir sözde kullanılır."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçimin başka bir dalda övgü bildirebilmesi, buradaki yergi anlamının bağlamsal sınırını gösterir."}],"identity_rationale":"Kaynak ifadesi bu dalda ailesini kıskanıp koruma duyarlılığı göstermeyen erkeğe yöneltilen alaycı yergiyi açıkça verir. Aynı ifade biçimin övgü ve yergi anlamlarına girebildiğini de not eder; bu dal yalnızca yergi tarafını temsil etmeli, övgüdeki yiğitlik ayrı dalda kalmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ailesine karşı koruyucu kıskançlık göstermediği için alay edilen erkek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ailesine karşı koruyucu kıskançlık göstermeyen erkeği alaya alan yergi sözü"}],"lexicalization_note":"Kişiye yüklenen olumsuz nitelik temel anlam, alaycı yergi sözü ise yalnızca kendi söz öbeğine bağlı kullanım olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eş anlamlı kişi niteliği, koruyucu kıskançlık karşıtı ve iki genel yergi alanı bu özel aşağılamanın sınırını en iyi belirledi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek kişi niteliği ve değerlendirme sınırı aynıdır; bu daldaki alaycı söz yalnızca kullanım örneğidir ve eş anlamlılığı bozmaz.","focus_only":null,"gloss":"koruyucu kıskançlığı olmayan erkek","neighbor_only":null,"neighbor_ref":"root_001450/B014","relation_type":"synonym","shared_zone":"İki dal da ailesine karşı koruyucu kıskançlık göstermeyen erkeği aşağılayıcı biçimde belirtir."},{"boundary_match":"opposed","distinction":"Bu dal niteliğin yokluğunu aşağılayıcı biçimde bildirir; komşu dal aynı niteliğin varlığını ve bunu taşıyan kişiyi belirtir.","focus_only":"Ailesine karşı koruyucu kıskançlık göstermeyen erkeği yerer.","gloss":"koruyucu kıskançlık eksikliği ile varlığı","neighbor_only":"Ailesine karşı koruyucu kıskançlık gösteren kişiyi niteler.","neighbor_ref":"root_001119/B004","relation_type":"polarity_pair","shared_zone":"İki dal da kişinin ailesine yönelik koruyucu kıskançlık niteliğini aynı eksende değerlendirir."},{"boundary_match":"field_only","distinction":"Bu dal yerginin hedefini koruyucu kıskançlık eksikliğiyle sınırlar; komşu dal herhangi bir kusura yönelen genel ayıplamadır.","focus_only":"Belirli bir ailevi tutum eksikliğini hedef alan yergidir.","gloss":"özel yergi ile genel ayıplama","neighbor_only":"Kusurun türünü sınırlamadan ayıplama, yerme ve utandırma eylemlerini genel olarak kapsar.","neighbor_ref":"root_001066/B012","relation_type":"same_field","shared_zone":"Her iki dal da kişiyi kusuru nedeniyle aşağılayıp yerme alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal belirli davranış eksikliğini ve alaycı hitabı anlatır; komşu dal kusurun kendisini ve doğurduğu genel yerilmeyi daha geniş biçimde kapsar.","focus_only":"Belirli bir erkeği ailevi tutumu nedeniyle alaya alır.","gloss":"belirli alaycı yergi ile genel kusur","neighbor_only":"Kişiye utanç ve küçümsenme getiren kusur ile genel yerme sonucunu kapsar.","neighbor_ref":"root_000506/B001","relation_type":"same_field","shared_zone":"İki dal da kusur, yerme ve küçümseme alanında buluşur."}],"source_phrase_ar":"الأليس: الديوثي الذي لا يغار ويتهزأ به؛ فيقال: هو أليس بورك فيه؛ فالليس يدخل في المعنيين: في المدح والذم (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, ailesine karşı koruyucu kıskançlık göstermeyen erkeğin alayla yerildiğini ve aynı biçimin başka bağlamda övgü de taşıyabildiğini bildirir."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaştırılacak ayrı bir anlatım yoktur; aşağılayıcı kişi niteliği ve alaycı söz tek tanıklıkla sınırlıdır.","sources":["TA"],"what_is_ar":"يدخل فيه قول بعض الأعراب الأليس الديوثي الذي لا يغار، وما يتصل بالتهزؤ والذم في قولهم هو أليس بورك فيه.","what_is_not_ar":"لا يدخل فيه الشجاع الممدوح، ولا الملازم للمكان إلا إذا أريد ذمه من جهة لزوم البيت، ولا استعمال ليس النحوي."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_38b0718346bc848198e8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:272-outcome-boundary","source_type":"word_analysis","support_ids":["sup_463f67e73d0e979008d8","sup_485039aca73fe8bdb3e2"],"title":"laysa-framed address also denies outcome ownership","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_ba361ff3b67976c5f85a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:addressee-continuity","source_type":"word_analysis","support_ids":["sup_485039aca73fe8bdb3e2","sup_d3b58248631499e4a591"],"title":"same addressee carried inside the negator","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_7c46c5f955c8c636c382","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:clipped-negation-sound","source_type":"word_analysis","support_ids":["sup_485039aca73fe8bdb3e2","sup_a054e4cee6a110235adf"],"title":"short opening sound makes the denial decisive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_3acd2912af8ea144e01e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:exception-preparation","source_type":"word_analysis","support_ids":["sup_2eb8eb81a1431f755b4c","sup_485039aca73fe8bdb3e2"],"title":"negation prepares the marked refuser without weakening non-control","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_102dcf31b4492aa3b6e8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:immediate-mission-boundary","source_type":"word_analysis","support_ids":["sup_485039aca73fe8bdb3e2","sup_63ad5f8d3305c602a98d"],"title":"positive role statement pivots into direct exclusion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_e28e86bfa3b6a2ad0e4b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:negation-scope","source_type":"word_analysis","support_ids":["sup_091f02f9269e3cc91da4","sup_485039aca73fe8bdb3e2"],"title":"opening negation governs domain and predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_3b7168ccfa992f9e2bfb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:role-negation-not-ban","source_type":"word_analysis","support_ids":["sup_403e4fb105c3efee3f61","sup_485039aca73fe8bdb3e2"],"title":"copular negation excludes a role, not one act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_eb85ab3b97fc97cf5657","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:surah-local-negation-return","source_type":"word_analysis","support_ids":["sup_485039aca73fe8bdb3e2","sup_b8962d10f3a8df2134c3"],"title":"surah reuses negation for failed functions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:1","qac_refs":["88:22:1:1","88:22:1:2"],"status":"accepted"}},{"anchor_refs":["88:22:2"],"branch_refs":[],"candidate_id":"cand_a4d69d9b0b7ceee3848b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:2:authority-domain","source_type":"word_analysis","support_ids":["sup_e5fffa4bf180f52e04d6","sup_ea51d1b70ef8f2266bf6"],"title":"over-them marks a denied authority domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:2","qac_refs":["88:22:2:1","88:22:2:2"],"status":"accepted"}},{"anchor_refs":["88:22:2"],"branch_refs":[],"candidate_id":"cand_92ea4658b6898bec09b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:2:nasal-link","source_type":"word_analysis","support_ids":["sup_01ceef725cd841416304","sup_e5fffa4bf180f52e04d6"],"title":"sound binds the domain to the denied title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:2","qac_refs":["88:22:2:1","88:22:2:2"],"status":"accepted"}},{"anchor_refs":["88:22:2"],"branch_refs":[],"candidate_id":"cand_5f7bb3958714c64c5ff9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:2:plural-to-refuser","source_type":"word_analysis","support_ids":["sup_e5fffa4bf180f52e04d6","sup_ebd21249fab73e2e5a02"],"title":"plural domain narrows into a marked refuser","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:2","qac_refs":["88:22:2:1","88:22:2:2"],"status":"accepted"}},{"anchor_refs":["88:22:2"],"branch_refs":[],"candidate_id":"cand_44995041d5c4895ab180","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:2:responsibility-shift","source_type":"word_analysis","support_ids":["sup_0ff8357cd57687a19e4a","sup_e5fffa4bf180f52e04d6"],"title":"over-them is answered by upon-Us","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:2","qac_refs":["88:22:2:1","88:22:2:2"],"status":"accepted"}},{"anchor_refs":["88:22:3"],"branch_refs":[],"candidate_id":"cand_35465019517ca31593f3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:3:fused-attachment","source_type":"word_analysis","support_ids":["sup_5c81984b9420a013880b","sup_8cc1c48fcd73adb0b374"],"title":"written and heard fusion fastens the denied title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:3","qac_refs":["88:22:3:1"],"status":"accepted"}},{"anchor_refs":["88:22:3"],"branch_refs":[],"candidate_id":"cand_53407e24d7955e9e95fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:3:hinge-to-final-title","source_type":"word_analysis","support_ids":["sup_5a3f98c9e0a33d08202d","sup_5c81984b9420a013880b"],"title":"particle pivots from domain to excluded title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:3","qac_refs":["88:22:3:1"],"status":"accepted"}},{"anchor_refs":["88:22:3"],"branch_refs":[],"candidate_id":"cand_32cb48d576c37b9c563d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:22:3:reinforcing-predicate-ba","source_type":"word_analysis","support_ids":["sup_2b61dd919f9b3bea2697","sup_5c81984b9420a013880b"],"title":"bāʾ reinforces the negated predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:3","qac_refs":["88:22:3:1"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_8dd26cbfc01a15e0116e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:5045-parallel","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_41976129c5774d77e8b6"],"title":"parallel shifts from force to supervisory control","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_61ae102bb503926e303d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:5237-control-claim","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_c7051d1f9970f33e54c1"],"title":"rare title is paired with cosmic control-claims","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_1ea2d9259e03a56c5844","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:8826-accounting","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_e00fcf1353771146a47b"],"title":"denied control is answered by divine reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_aca4a639bf4b372d3a44","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:active-role-predicate","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_1bffbeaed5c886925f55"],"title":"active indefinite role noun over a plural domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_7b9e41ca783ec7868459","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:controller-cadence","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_37a470ad5c4d0659d9c3"],"title":"sound gives the denied title final weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_7a260c9390302af52f66","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:final-excluded-title","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_5f982ff2e1f02e8570dc"],"title":"final word lands as the excluded model","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_769fe2f8486ddbc95dab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:forward-accountability","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_338d85ffb93bb2f8aa1c"],"title":"non-control permits refusal but leaves consequence elsewhere","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_18a0b1a683268db7ab37","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:line-order-imagery","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_38ee2481139c3881b555"],"title":"line and record field colors control as imposed order","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_a869aeffc0a354e0c418","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:rare-active-title","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_7f0a29ad46c92be47a21"],"title":"active controller title is distributionally marked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_3d25f9fd6cc3cb92d0a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:reminder-vs-control","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_ecbe12369aef67c81dd0"],"title":"controller is the rival mission role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:4"],"branch_refs":[],"candidate_id":"cand_2b2ba2743b00ebcfd8df","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:4:variant-pressure","source_type":"word_analysis","support_ids":["sup_1222b9a8a7ae50ad7cdc","sup_e9b567cd5a45ea6fd873"],"title":"variant pressure tests sound, case, and agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:22:4","qac_refs":["88:22:3:2"],"status":"accepted"}},{"anchor_refs":["88:22:1"],"branch_refs":[],"candidate_id":"cand_16c7c67f9f0d7724ff1a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001390"],"scope":"focus_ayah","source_local_id":"88:22:1:1","source_type":"qac_morpheme","support_ids":["sup_75dc6acdc7cc81dd5558"],"title":"QAC root occurrence: ل ي س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:22:3"],"branch_refs":[],"candidate_id":"cand_5292eae14da30bea03ed","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000704"],"scope":"focus_ayah","source_local_id":"88:22:3:2","source_type":"qac_morpheme","support_ids":["sup_4f3be4c442636937d278"],"title":"QAC root occurrence: س ط ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:22","branch_refs":["root_000704/B003","root_001390/B001"],"candidate_id":"cand_651fc01eba55ccdf2d29","commentary_obligation":"review","hft_ref":"hft_677282e60b60c83acc14","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_present_jurisdiction","source_type":"hft","support_ids":["sup_b391ed5074b32f3f0e18"],"title":"baseline_present_jurisdiction","trust":"legacy_unbound"},{"anchor_refs":["88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:22","branch_refs":["root_000704/B001","root_000704/B003","root_001390/B003"],"candidate_id":"cand_27df44c919fb7f068c31","commentary_obligation":"review","hft_ref":"hft_d0788e261e107f5cd5a5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_not_line_inscriber","source_type":"hft","support_ids":["sup_89e2d383652e3ed12df4"],"title":"baseline_not_line_inscriber","trust":"legacy_unbound"},{"anchor_refs":["88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:22","branch_refs":["root_000704/B004","root_001390/B001"],"candidate_id":"cand_567009e631ec6d7e9959","commentary_obligation":"review","hft_ref":"hft_1f78c351611eba8edd97","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_cutting_people_into_line","source_type":"hft","support_ids":["sup_8989cdd0b3c8141782d7"],"title":"outlier_cutting_people_into_line","trust":"legacy_unbound"},{"anchor_refs":["88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:22","branch_refs":["root_000704/B003","root_001390/B006"],"candidate_id":"cand_093b88f38c87580e505e","commentary_obligation":"review","hft_ref":"hft_5000309427c9d02c35c0","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_forbearing_noncontrol","source_type":"hft","support_ids":["sup_ed9ed0a627162755ad22"],"title":"outlier_forbearing_noncontrol","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","qac_morphemes":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","root_ar":"ل ي س","surface_ar":"لَّسْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:22:1:2","qac_word_ref":"88:22:1","root_ar":"","surface_ar":"تَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:22:2:1","qac_word_ref":"88:22:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:22:2:2","qac_word_ref":"88:22:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"88:22:3:1","qac_word_ref":"88:22:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","root_ar":"س ط ر","surface_ar":"مُصَيْطِرٍ"}],"word_analysis_qac_refs":[["88:22:1:1","88:22:1:2"],["88:22:2:1","88:22:2:2"],["88:22:3:1"],["88:22:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:22:1","88:22:2","88:22:3","88:22:4"]},"focus_surface_evidence":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","qac_morphemes":[{"lemma_ar":"لَّيْسَ","morph_features":"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:22:1:1","qac_word_ref":"88:22:1","root_ar":"ل ي س","surface_ar":"لَّسْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:22:1:2","qac_word_ref":"88:22:1","root_ar":"","surface_ar":"تَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:22:2:1","qac_word_ref":"88:22:2","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:22:2:2","qac_word_ref":"88:22:2","root_ar":"","surface_ar":"هِم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"88:22:3:1","qac_word_ref":"88:22:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"مُصَيْطِر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:22:3:2","qac_word_ref":"88:22:3","root_ar":"س ط ر","surface_ar":"مُصَيْطِرٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:22:1:1","88:22:1:2"],["88:22:2:1","88:22:2:2"],["88:22:3:1"],["88:22:3:2"]],"word_analysis_refs":["88:22:1","88:22:2","88:22:3","88:22:4"],"word_rows":[{"analysis_record_ref":"88:22:1","analytic_gloss_range_en":"laysa-type present-state negation with a second-person masculine singular subject; locally denies role-status rather than a single act","analytic_root_gloss_range_en":"fixed negating-verb range centered on laysa-type predication and exclusion; unrelated nominal branches are not locally active here","qac_refs":["88:22:1:1","88:22:1:2"],"root":{"arabic":"ل ي س","transliteration":"l-y-s"},"surface":{"arabic":"لَّسْتَ","transliteration":"lasta"}},{"analysis_record_ref":"88:22:2","analytic_gloss_range_en":"over them, upon them, or against them as a governed authority domain; locally the domain over which control is denied","analytic_root_gloss_range_en":null,"qac_refs":["88:22:2:1","88:22:2:2"],"root":{},"surface":{"arabic":"عَلَيْهِم","transliteration":"ʿalayhim"}},{"analysis_record_ref":"88:22:3","analytic_gloss_range_en":"prefixed bāʾ on the negated predicate; locally reinforces exclusion and governs the following role noun rather than marking an independent instrument","analytic_root_gloss_range_en":null,"qac_refs":["88:22:3:1"],"root":{},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"88:22:4","analytic_gloss_range_en":"active controller or dominating overseer role over a human domain; locally denied as a standing office, with line-order and record imagery coloring but not replacing the selected control sense","analytic_root_gloss_range_en":"root range includes lines, rows, writing or records, false written tales, and a specialized control branch; local grammar selects the control branch while allowing written-order pressure as image coloring","qac_refs":["88:22:3:2"],"root":{"arabic":"س ط ر","transliteration":"s-ṭ-r"},"surface":{"arabic":"مُصَيْطِرٍ","transliteration":"muṣayṭirin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:22"],"branch_refs":["root_000704/B003","root_001390/B001"],"candidate_id":"cand_651fc01eba55ccdf2d29","evidence_scope":"focus_ayah","hft_ref":"hft_677282e60b60c83acc14","item_id":"baseline_present_jurisdiction","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_present_jurisdiction","support_id":"sup_b391ed5074b32f3f0e18"},{"anchor_refs":["88:22"],"branch_refs":["root_000704/B001","root_000704/B003","root_001390/B003"],"candidate_id":"cand_27df44c919fb7f068c31","evidence_scope":"focus_ayah","hft_ref":"hft_d0788e261e107f5cd5a5","item_id":"baseline_not_line_inscriber","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_not_line_inscriber","support_id":"sup_89e2d383652e3ed12df4"},{"anchor_refs":["88:22"],"branch_refs":["root_000704/B004","root_001390/B001"],"candidate_id":"cand_567009e631ec6d7e9959","evidence_scope":"focus_ayah","hft_ref":"hft_1f78c351611eba8edd97","item_id":"outlier_cutting_people_into_line","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_cutting_people_into_line","support_id":"sup_8989cdd0b3c8141782d7"},{"anchor_refs":["88:22"],"branch_refs":["root_000704/B003","root_001390/B006"],"candidate_id":"cand_093b88f38c87580e505e","evidence_scope":"focus_ayah","hft_ref":"hft_5000309427c9d02c35c0","item_id":"outlier_forbearing_noncontrol","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_forbearing_noncontrol","support_id":"sup_ed9ed0a627162755ad22"}],"diagnostics":[],"lane_counts":{"global":16,"macro":4,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:22","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:22","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"88:22","lane":"micro","linguistic_source_ref":"88:22","surface_ref":"88:22","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:22","target_tokens":[["Onlar",["88:22:2"]],["üzerinde",["88:22:2"]],["bir",["88:22:3"]],["denetleyici",["88:22:3"]],["değilsin",["88:22:1"]]],"text":"Onlar üzerinde bir denetleyici değilsin."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:2:nasal-link","source_type":"word_analysis","support_id":"sup_01ceef725cd841416304","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds the domain to the denied title\",\"reader_payoff\":\"The reader notices that the heard ending of the domain runs straight into the final predicate phrase.\",\"reason\":\"The phonetic point is limited to recitation texture: the final sound of {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) links into {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}) without changing the syntactic separation.\",\"representative_source_ids\":[\"QP-15c22eb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:negation-scope","source_type":"word_analysis","support_id":"sup_091f02f9269e3cc91da4","text":"{\"blocking_evidence\":null,\"headline\":\"opening negation governs domain and predicate\",\"reader_payoff\":\"The reader notices that the denial reaches the whole relation, not just an isolated title or an isolated prepositional phrase.\",\"reason\":\"Attachment evidence makes {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}) the predicate under {{ar:لَّسْتَ}} ({{tr:lasta}}), while {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) supplies the domain governed by that denied role.\",\"representative_source_ids\":[\"QG-d53dedb0\",\"QT-4f085feb\",\"QY-0bea434c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:2:responsibility-shift","source_type":"word_analysis","support_id":"sup_0ff8357cd57687a19e4a","text":"{\"blocking_evidence\":null,\"headline\":\"over-them is answered by upon-Us\",\"reader_payoff\":\"The reader notices a responsibility switch: the people are not placed under prophetic control, and reckoning is later placed upon Us in 88:26.\",\"reason\":\"The row-level links are concrete: {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) is denied as a control-domain in 88:22, {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) assigns reckoning in 88:26, and 42:48 limits the messenger's burden to conveyance.\",\"representative_source_ids\":[\"QI-6811c8a0\",\"QE-13378843\",\"QI-927e5e73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4","source_type":"word_analysis","support_id":"sup_1222b9a8a7ae50ad7cdc","text":"{\"gloss_range\":\"active controller or dominating overseer role over a human domain; locally denied as a standing office, with line-order and record imagery coloring but not replacing the selected control sense\",\"prose\":\"{{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}) is the final title the clause has been excluding, withheld until the close so the rejected model can land with full weight. Its active participial form makes the addressee the possible role-holder, its indefiniteness broadens the denial to any such controller-role, and {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) keeps the people as the domain over which that role would operate. The selected sense is coercive authority-over, not neutral supervision, because 88:21 has just affirmed the reminder role and this word names the rival office. The {{ar:س ط ر}} ({{tr:s-ṭ-r}}) field narrows locally to control, yet its line, record, and written-order branches still color the denied authority as arranging or fixing people into an imposed order. Variant pressures at the final word test sound, case, and active/passive direction, but the canonical form remains the active controller-title being denied; its sibilant-emphatic cadence gives the title a heavy controlling texture before the denial releases it. The same rare active title is marked against the field's record and writtenness uses, paired with control-claims in 52:37, contrasted with force-language in 50:45, and answered inside the surah by the accounting assignment in 88:26: control is refused to the messenger, reckoning is reserved elsewhere. The next movement can mark the refuser in 88:23 and divine consequence in 88:24 without converting that consequence into prophetic control.\",\"root_display\":\"{{ar:س ط ر}} ({{tr:s-ṭ-r}})\",\"root_gloss_range\":\"root range includes lines, rows, writing or records, false written tales, and a specialized control branch; local grammar selects the control branch while allowing written-order pressure as image coloring\",\"surface_display\":\"{{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:active-role-predicate","source_type":"word_analysis","support_id":"sup_1bffbeaed5c886925f55","text":"{\"blocking_evidence\":null,\"headline\":\"active indefinite role noun over a plural domain\",\"reader_payoff\":\"The reader notices that the final word names a standing role-holder assigned to the singular addressee, while the plural group remains the domain over which that role is denied.\",\"reason\":\"The local form is an active participial predicate governed by {{ar:بِ}} ({{tr:bi}}), indefinite under negation, and connected to {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) as its authority domain.\",\"representative_source_ids\":[\"QG-c47676ab\",\"QG-79f4f637\",\"QG-dabf636f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:3:reinforcing-predicate-ba","source_type":"word_analysis","support_id":"sup_2b61dd919f9b3bea2697","text":"{\"blocking_evidence\":null,\"headline\":\"bāʾ reinforces the negated predicate\",\"reader_payoff\":\"The reader notices that the tiny particle strengthens the exclusion of the controller-role rather than functioning as an instrument.\",\"reason\":\"After {{ar:لَّسْتَ}} ({{tr:lasta}}), {{ar:بِ}} ({{tr:bi}}) governs the predicate noun and reinforces the negation; local attachment evidence blocks an instrumental reading.\",\"representative_source_ids\":[\"QG-4296ebdf\",\"QG-6899f1b3\",\"MG-0603858e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:exception-preparation","source_type":"word_analysis","support_id":"sup_2eb8eb81a1431f755b4c","text":"{\"blocking_evidence\":null,\"headline\":\"negation prepares the marked refuser without weakening non-control\",\"reader_payoff\":\"The reader notices that the following exception in 88:23 can mark refusal while the denial of control remains intact.\",\"reason\":\"The next ayah begins an exception/adversative turn (88:23), but this row preserves only the forward rhetorical setup; it does not alter the local parse of {{ar:لَّسْتَ}} ({{tr:lasta}}).\",\"representative_source_ids\":[\"QB-9007b0f8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:forward-accountability","source_type":"word_analysis","support_id":"sup_338d85ffb93bb2f8aa1c","text":"{\"blocking_evidence\":null,\"headline\":\"non-control permits refusal but leaves consequence elsewhere\",\"reader_payoff\":\"The reader notices that the next movement can mark refusal and divine consequence without converting the messenger into a controller.\",\"reason\":\"The forward context is concrete: 88:23 marks the refuser, and 88:24 assigns consequence to {{ar:ٱللَّهُ}} ({{tr:Allāhu}}), preserving non-control while maintaining accountability.\",\"representative_source_ids\":[\"QB-96e2d2a3\",\"QB-bf64b260\",\"QB-deea6c9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:controller-cadence","source_type":"word_analysis","support_id":"sup_37a470ad5c4d0659d9c3","text":"{\"blocking_evidence\":null,\"headline\":\"sound gives the denied title final weight\",\"reader_payoff\":\"The reader notices that the sound and cadence make the excluded title feel weighty before releasing it as denied.\",\"reason\":\"The phonetic rows are local sound payoffs: {{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}) carries the final sibilant-emphatic texture and nasal close, while the grammar remains the active predicate under negation.\",\"representative_source_ids\":[\"QP-3a7811e1\",\"QP-aa3d718c\",\"QP-feb41335\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:line-order-imagery","source_type":"word_analysis","support_id":"sup_38ee2481139c3881b555","text":"{\"blocking_evidence\":null,\"headline\":\"line and record field colors control as imposed order\",\"reader_payoff\":\"The reader notices that the denied control feels like arranging, registering, and fixing people into an imposed order, while the selected local role remains controller.\",\"reason\":\"V4 separates written-line and false-record branches from the control branch, so the writing and record field should color the selected controller-role as image-pressure rather than replace it with literal writing or fabricated tales.\",\"representative_source_ids\":[\"QS-4a77bf71\",\"QS-c582f67b\",\"QY-3b8eac28\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:role-negation-not-ban","source_type":"word_analysis","support_id":"sup_403e4fb105c3efee3f61","text":"{\"blocking_evidence\":null,\"headline\":\"copular negation excludes a role, not one act\",\"reader_payoff\":\"The reader notices that the clause removes controller-status itself rather than merely forbidding a particular controlling action.\",\"reason\":\"The local construction is a laysa-type copular negation with a predicate, so {{ar:لَّسْتَ}} ({{tr:lasta}}) denies identity with the predicate role rather than narrating or prohibiting an event.\",\"representative_source_ids\":[\"QG-812bb621\",\"QG-82290b6b\",\"MG-21ce4b82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:5045-parallel","source_type":"word_analysis","support_id":"sup_41976129c5774d77e8b6","text":"{\"blocking_evidence\":null,\"headline\":\"parallel shifts from force to supervisory control\",\"reader_payoff\":\"The reader notices that 50:45 denies overpowering force, while 88:22 denies supervisory control, sharpening the type of authority excluded here.\",\"reason\":\"The parallel is concrete: 50:45 uses {{ar:بِجَبَّارٍ}} ({{tr:bi-jabbārin}}) over them, while 88:22 uses {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}), both under negation but with different role-nouns.\",\"representative_source_ids\":[\"QI-85df7de3\",\"MI-d2de09d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:272-outcome-boundary","source_type":"word_analysis","support_id":"sup_463f67e73d0e979008d8","text":"{\"blocking_evidence\":null,\"headline\":\"laysa-framed address also denies outcome ownership\",\"reader_payoff\":\"The reader notices a Quranic pattern where laysa-framed address sets the messenger outside both outcome ownership and coercive authority.\",\"reason\":\"The parallel is concrete: {{ar:لَيْسَ عَلَيْكَ هُدَاهُمْ}} ({{tr:laysa ʿalayka hudāhum}}) denies guidance-burden in 2:272, while {{ar:لَّسْتَ}} ({{tr:lasta}}) denies controller-status in 88:22.\",\"representative_source_ids\":[\"QI-778c55c1\",\"MI-f5eeee3f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1","source_type":"word_analysis","support_id":"sup_485039aca73fe8bdb3e2","text":"{\"gloss_range\":\"laysa-type present-state negation with a second-person masculine singular subject; locally denies role-status rather than a single act\",\"prose\":\"{{ar:لَّسْتَ}} ({{tr:lasta}}) carries the same addressed figure from the reminder-role in 88:21 into a direct denial of controller-status. Because it is laysa-type copular negation, the clause is not simply saying not to perform one act; it says the addressee is not constituted as the role named at the end. The opening negation governs the whole relation, so {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) and {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}) are heard inside one boundary: reminder remains assigned, coercive authority over response does not. This also fits the wider laysa-framed boundary in 2:272, where outcome-burden is denied, and the surah-local return from failed nourishment in 88:6 to denied control in 88:22 makes negation mark what cannot perform the imagined function. The compact sound of {{ar:لَّسْتَ}} ({{tr:lasta}}) makes non-control the first frame heard before the title is named, while the next exception in 88:23 can mark refusal without making refusal a failure of prophetic control.\",\"root_display\":\"{{ar:ل ي س}} ({{tr:l-y-s}})\",\"root_gloss_range\":\"fixed negating-verb range centered on laysa-type predication and exclusion; unrelated nominal branches are not locally active here\",\"surface_display\":\"{{ar:لَّسْتَ}} ({{tr:lasta}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:22:3:2","source_type":"qac_morpheme","support_id":"sup_4f3be4c442636937d278","text":"{\"lemma_ar\":\"مُصَيْطِر\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|(II)|LEM:muSayoTir|ROOT:sTr|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:22:3:2\",\"qac_word_ref\":\"88:22:3\",\"root_ar\":\"س ط ر\",\"surface_ar\":\"مُصَيْطِرٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:3:hinge-to-final-title","source_type":"word_analysis","support_id":"sup_5a3f98c9e0a33d08202d","text":"{\"blocking_evidence\":null,\"headline\":\"particle pivots from domain to excluded title\",\"reader_payoff\":\"The reader notices that the particle is the hinge that turns over-them into the final denied office.\",\"reason\":\"In local order, {{ar:بِ}} ({{tr:bi}}) introduces the final predicate after {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}); the same bāʾ-marked negated-role pattern is visible in {{ar:بِجَبَّارٍ}} ({{tr:bi-jabbārin}}) at 50:45, and the following turn in 88:23 does not undo the exclusion.\",\"representative_source_ids\":[\"QT-12b22191\",\"MT-b6d8365e\",\"QI-3dd885b6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:3","source_type":"word_analysis","support_id":"sup_5c81984b9420a013880b","text":"{\"gloss_range\":\"prefixed bāʾ on the negated predicate; locally reinforces exclusion and governs the following role noun rather than marking an independent instrument\",\"prose\":\"{{ar:بِ}} ({{tr:bi}}) is small but not ornamental. After {{ar:لَّسْتَ}} ({{tr:lasta}}), it governs the final predicate and strengthens the denial, so the role is excluded with emphatic syntax rather than treated as an instrument. The particle is split in analysis but fused in the heard and written phrase {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}), making reinforcement and title arrive together at the clause's end as if the role is fastened to the clause only to be rejected. It also acts as the hinge from {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) to the excluded role, a structurally barred alternative that resonates with the bāʾ-marked non-compulsion formula in 50:45.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:final-excluded-title","source_type":"word_analysis","support_id":"sup_5f982ff2e1f02e8570dc","text":"{\"blocking_evidence\":null,\"headline\":\"final word lands as the excluded model\",\"reader_payoff\":\"The reader notices that the clause withholds the title until the final word can land as the exact model being rejected.\",\"reason\":\"The word order places {{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}) at the close of the clause, so the final position carries the denied mission-model.\",\"representative_source_ids\":[\"QT-a102f221\",\"MT-e2ca339a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:immediate-mission-boundary","source_type":"word_analysis","support_id":"sup_63ad5f8d3305c602a98d","text":"{\"blocking_evidence\":null,\"headline\":\"positive role statement pivots into direct exclusion\",\"reader_payoff\":\"The reader notices that 88:22 immediately qualifies the reminder command of 88:21 by naming what the mission is not.\",\"reason\":\"The ayah opens directly with {{ar:لَّسْتَ}} ({{tr:lasta}}), so the negation functions as an immediate boundary after the role statement in 88:21 rather than as a detached new theme.\",\"representative_source_ids\":[\"QT-4998cdfc\",\"QT-7a946564\",\"QB-734a7d3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:22:1:1","source_type":"qac_morpheme","support_id":"sup_75dc6acdc7cc81dd5558","text":"{\"lemma_ar\":\"لَّيْسَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:l~ayosa|ROOT:lys|SP:kaAn|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:22:1:1\",\"qac_word_ref\":\"88:22:1\",\"root_ar\":\"ل ي س\",\"surface_ar\":\"لَّسْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:rare-active-title","source_type":"word_analysis","support_id":"sup_7f0a29ad46c92be47a21","text":"{\"blocking_evidence\":null,\"headline\":\"active controller title is distributionally marked\",\"reader_payoff\":\"The reader notices that this is not ordinary authority vocabulary but a marked active controller title within a field more often tied to records and writtenness.\",\"reason\":\"The contextual profile marks the root and active participial title as low-occurrence, supporting the CRITICAL claim that the role-word stands out without making other root branches literally local.\",\"representative_source_ids\":[\"QI-f323676b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:3:fused-attachment","source_type":"word_analysis","support_id":"sup_8cc1c48fcd73adb0b374","text":"{\"blocking_evidence\":null,\"headline\":\"written and heard fusion fastens the denied title\",\"reader_payoff\":\"The reader notices that the particle and title arrive as one close unit, as if the role is attached only to be rejected.\",\"reason\":\"The bundle analytically separates {{ar:بِ}} ({{tr:bi}}), but the surface and recitation bind it to {{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}); this supports attachment and reinforcement, not a separate lexical object.\",\"representative_source_ids\":[\"QS-bc1509aa\",\"QF-04266186\",\"QP-a5386e8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:clipped-negation-sound","source_type":"word_analysis","support_id":"sup_a054e4cee6a110235adf","text":"{\"blocking_evidence\":null,\"headline\":\"short opening sound makes the denial decisive\",\"reader_payoff\":\"The reader notices the compact sound of the first word before the longer predicate phrase unfolds.\",\"reason\":\"The sound observation is local and limited: the compact onset of {{ar:لَّسْتَ}} ({{tr:lasta}}) gives the role boundary an abrupt opening without changing the grammar.\",\"representative_source_ids\":[\"QP-9d2fb657\",\"QP-aa3040bb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:surah-local-negation-return","source_type":"word_analysis","support_id":"sup_b8962d10f3a8df2134c3","text":"{\"blocking_evidence\":null,\"headline\":\"surah reuses negation for failed functions\",\"reader_payoff\":\"The reader notices that the surah reuses negation to mark what does not fulfill an imagined function, from food in 88:6 to control in 88:22.\",\"reason\":\"The echo stays at the level of recurring negation: 88:6 denies nourishing function, and 88:22 denies controller-status through {{ar:لَّسْتَ}} ({{tr:lasta}}).\",\"representative_source_ids\":[\"QE-a585ee46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:5237-control-claim","source_type":"word_analysis","support_id":"sup_c7051d1f9970f33e54c1","text":"{\"blocking_evidence\":null,\"headline\":\"rare title is paired with cosmic control-claims\",\"reader_payoff\":\"The reader notices that the rare controller title is alien both to opponent claims in 52:37 and to the messenger's mission in 88:22.\",\"reason\":\"The concrete pair is 52:37, where {{ar:ٱلْمُصَيْطِرُونَ}} ({{tr:al-muṣayṭirūn}}) mocks control-claims, and 88:22, where {{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}) is denied to the addressee.\",\"representative_source_ids\":[\"QI-ef23a492\",\"MI-32fbf7b4\",\"QH-afe9029d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:1:addressee-continuity","source_type":"word_analysis","support_id":"sup_d3b58248631499e4a591","text":"{\"blocking_evidence\":null,\"headline\":\"same addressee carried inside the negator\",\"reader_payoff\":\"The reader notices that the one commanded to remind in 88:21 is the same second-person figure whose controller-role is denied here.\",\"reason\":\"The second-person masculine singular suffix in {{ar:لَّسْتَ}} ({{tr:lasta}}) is the surface subject and matches the addressee of the prior reminder command (88:21).\",\"representative_source_ids\":[\"QG-040deee5\",\"QG-6ff4bbe5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:8826-accounting","source_type":"word_analysis","support_id":"sup_e00fcf1353771146a47b","text":"{\"blocking_evidence\":null,\"headline\":\"denied control is answered by divine reckoning\",\"reader_payoff\":\"The reader notices that control over them is not handed to the messenger because account over them is assigned to Us in 88:26.\",\"reason\":\"The same closing unit contrasts {{ar:بِمُصَيْطِرٍ}} ({{tr:bi-muṣayṭirin}}) in 88:22 with {{ar:عَلَيْنَا حِسَابَهُم}} ({{tr:ʿalaynā ḥisābahum}}) in 88:26, relocating final authority from control to reckoning.\",\"representative_source_ids\":[\"MI-8e92976a\",\"QE-d1164139\",\"QE-f5699948\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:2","source_type":"word_analysis","support_id":"sup_e5fffa4bf180f52e04d6","text":"{\"gloss_range\":\"over them, upon them, or against them as a governed authority domain; locally the domain over which control is denied\",\"prose\":\"{{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) turns the denial into a relation over a human domain. The preposition {{ar:عَلَى}} ({{tr:ʿalā}}) does not make them a direct object; it makes control sound like a posture of authority above them, the very posture refused. Its placement before the final title lets the audience-domain appear before the controller-role is named, and the heard ending runs straight into the following predicate phrase, audibly tying that domain to the title being denied. The same prepositional pressure becomes a responsibility switch in the passage: 88:22 denies control over them, while 88:26 places reckoning upon Us, and 42:48 limits the messenger's burden to conveyance. The group can then narrow into the marked refuser in 88:23, so non-control over the plural domain does not erase individual accountability.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْهِم}} ({{tr:ʿalayhim}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:variant-pressure","source_type":"word_analysis","support_id":"sup_e9b567cd5a45ea6fd873","text":"{\"blocking_evidence\":null,\"headline\":\"variant pressure tests sound, case, and agency\",\"reader_payoff\":\"The reader notices that variant pressures gather at the final title, but the canonical reading keeps the addressee as the active role-holder being denied.\",\"reason\":\"The sibilant variants affect acoustic color, and the passive-like or case-disrupting reports expose role-direction and government pressure; they do not overturn the canonical active participial predicate {{ar:مُصَيْطِرٍ}} ({{tr:muṣayṭirin}}).\",\"representative_source_ids\":[\"QF-5e33cf3e\",\"QS-a9245f68\",\"QY-17259510\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:2:authority-domain","source_type":"word_analysis","support_id":"sup_ea51d1b70ef8f2266bf6","text":"{\"blocking_evidence\":null,\"headline\":\"over-them marks a denied authority domain\",\"reader_payoff\":\"The reader notices that the people are not direct objects of control but the domain over which authority is refused.\",\"reason\":\"The preposition {{ar:عَلَى}} ({{tr:ʿalā}}) with the 3mp suffix forms {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}), the domain complement of the denied controller predicate, so the local relation is authority-over rather than speech-to.\",\"representative_source_ids\":[\"QG-0f49c43f\",\"QG-4ee00dd2\",\"MG-a33ecafe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:2:plural-to-refuser","source_type":"word_analysis","support_id":"sup_ebd21249fab73e2e5a02","text":"{\"blocking_evidence\":null,\"headline\":\"plural domain narrows into a marked refuser\",\"reader_payoff\":\"The reader notices that non-control over the group does not erase individual accountability in the next ayah.\",\"reason\":\"The next ayah isolates {{ar:مَن}} ({{tr:man}}) in 88:23 from the plural domain of {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}), so the forward relation preserves accountability without making it prophetic control.\",\"representative_source_ids\":[\"QB-4c35be27\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:22:4:reminder-vs-control","source_type":"word_analysis","support_id":"sup_ecbe12369aef67c81dd0","text":"{\"blocking_evidence\":null,\"headline\":\"controller is the rival mission role\",\"reader_payoff\":\"The reader notices that the final title defines the mission by contrast: reminder is affirmed in 88:21, coercive mastery is excluded in 88:22.\",\"reason\":\"The predicate selects coercive authority-over rather than neutral supervision because it follows the reminder command in 88:21 and is denied as the counter-role to {{ar:مُذَكِّرٌ}} ({{tr:mudhakkirun}}).\",\"representative_source_ids\":[\"QS-22831523\",\"QI-a2b5a8d3\",\"QT-c271ea4b\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000704/B003","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001390","role":"The fixed present-state negation, reinforced in the predicate construction, denies that this supervisory relation presently holds.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"Overseeing, preserving, and controlling authority supplies the office that is being denied.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"You are emphatically not installed over them as their guardian-controller; the line limits jurisdiction, not simply effectiveness.","before":"You cannot make them believe."},"confidence":"strong","focus_anchor":"The whole predication in lَsta alayhim bi-musaytir joins emphatic negation to a relational position over them.","mechanism":"The clause denies a presently holding office, and the denied office bundles oversight, preservation, and domination. It therefore marks a jurisdictional boundary rather than merely predicting that persuasion will fail.","model_id":"baseline_present_jurisdiction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_present_jurisdiction","source_type":"hft","support_id":"sup_b391ed5074b32f3f0e18","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000704/B001","root_000704/B003","root_001390/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001390","role":"Categorical negation excludes the addressee from the class of totalizing arrangers.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000704","role":"The aligned written row turns abstract control into fixing people as ordered entries.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"The supervisory branch links that row image back to the actual predicate of authority.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"You are not the registrar-arranger who fixes their places, responses, or outcomes into a humanly controlled row.","before":"You are not a ruler over them."},"confidence":"medium","focus_anchor":"Musaytir carries the same focus root whose inventory includes both control and the aligned written row.","mechanism":"Control can be pictured as fixing persons into a legible line or record. Categorical negation blocks the speaker from becoming the one who writes, ranks, or fixes their responses into such an order.","model_id":"baseline_not_line_inscriber"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_not_line_inscriber","source_type":"hft","support_id":"sup_89e2d383652e3ed12df4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000704/B004","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001390","role":"Present-state negation blocks the violent line-making action from becoming the addressee's current office.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000704","role":"A striking or cutting line materializes coercion as bringing bodies into line by force.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"Metaphorically, he is not the one who strikes, cuts, or disciplines people into a compliant line.","before":"He must not coerce them."},"confidence":"exploratory","containment":"The striking or cutting line is a peripheral branch, so this cannot replace the ordinary control sense. It remains valid as an exact focus-root activation that gives coercion a material mechanism; downstream prose should mark it explicitly as metaphorical.","focus_anchor":"The negated musaytir bears a focus-root branch in which a blow or cut produces a line.","outlier_id":"outlier_cutting_people_into_line"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_cutting_people_into_line","source_type":"hft","support_id":"sup_8989cdd0b3c8141782d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000704/B003","root_001390/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001390","role":"Forbearing load-bearing and good-natured overlooking supplies a positive manner for inhabiting the negation of control.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"The denied supervisory office is the pressure against which patient non-control becomes ethically legible.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"As a contained ethical echo, the removal of control opens a mode of patient bearing and overlooking while reminder continues.","before":"The verse only removes authority."},"confidence":"exploratory","containment":"The forbearance branch belongs to collateral alis and talayasa material rather than the grammatical sense of laysa, making this the most form-distant activation retained. It is still rooted in the focus occurrence and yields a coherent posture opposite control; render it only as an ethical halo, never as the clause's lexical translation.","focus_anchor":"The focus negation and denied supervisory role meet within a root inventory that also carries patient bearing and overlooking.","outlier_id":"outlier_forbearing_noncontrol"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_forbearing_noncontrol","source_type":"hft","support_id":"sup_ed9ed0a627162755ad22","trust":"legacy_unbound"}]}
</lane_packet_json>
