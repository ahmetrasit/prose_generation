# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:16**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_16/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:16",
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
{"branch_registry":[{"boundary":"Bu dal, icte sakli duygu veya sirrin acilmasini degil, seylerin alana dagitilip yayilmasini anlatir.","branch_kind":"mixed_non_bare","branch_ref":"root_000083/B001","candidate_links":[{"candidate_id":"cand_53d8e396ab694477b08c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَبْثُوثَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:16:2:1","qac_word_ref":"88:16:2","surface_ar":"مَبْثُوثَةٌ"}],"gloss":"dagitip yaymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir seyi ayirip farkli yonlere veya alana dagitmaktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dagitma, nesnenin ortaya cikmasi, yayilmasi, savrulmasi veya yerinden kaldirilip hareketlendirilmesi sonucunu dogurabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atlari veya av kopeklerini salmak gibi kullanimlarda dagitma, canlilari belli bir is icin alana yaymaktir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Hurma, yemek, dosek, cekirge, kelebek veya toz gibi nesnelerde anlam daginik, serpilmis, cok veya savrulmus duruma yonelir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Yaratilmis varliklar icin kullanim, onlarin yeryuzune yayilmasini ve cogalmasini anlatir."}}],"root_ar":"ب ث ث","root_id":"root_000083","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel ya da sayilabilir bir seyin alana ayrilip yayilmasini en kisa bicimde karsilar; cogalma ve savrulma baglamlari aciklama ister.","boundary_detail":"Bu dal, icte sakli duygu veya sirrin acilmasini degil, seylerin alana dagitilip yayilmasini anlatir.","branch_image_ar":"تفريق الشيء وبثه","concept_gloss":"dagitip yaymak","contextual_glosses":[{"applicability":"At, kopek veya canli varliklarin bir alan icine gonderilip dagitildigi baglamlarda dogaldir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Cansiz nesneyi sacma veya savurma kullanimlarini kapsamaz.","preserves":"Canlilari alana gonderme ve yayma yonunu korur."},"facet_ids":["F003","F005"],"text":"salip yaymak","usage_role":"contextual"},{"applicability":"Hurma, yemek, dosek, bocek veya toz gibi nesnelerin ortaya daginik halde bulunmasi icin uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin gonderme, cogaltma veya aciga cikarma yonunu azaltir.","preserves":"Daginiklik ve alana yayilmis sonucunu korur."},"facet_ids":["F002","F004"],"text":"sacilip dagilmis","usage_role":"contextual"},{"applicability":"Toz veya benzeri hafif seyin kaldirilip yayildigi baglamlarda dogal bir karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel dagitma, canli salma ve cogalma kullanimlarini disarida birakir.","preserves":"Hareketlendirme ve havaya yayma sonucunu korur."},"facet_ids":["F002","F004"],"text":"savurmak","usage_role":"contextual"}],"definition":"Bir seyi tek yerde toplu veya gizli halde birakmayip parcalara, yonlere ya da alana dagitmak; buna bagli olarak nesnenin yayilmasi, savrulmasi, aciga cikmasi veya canlilarin yeryuzunde cogalip dagilmasi anlatilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir seyi ayirip farkli yonlere veya alana dagitmaktir."},{"facet_id":"F002","role":"extension","statement":"Dagitma, nesnenin ortaya cikmasi, yayilmasi, savrulmasi veya yerinden kaldirilip hareketlendirilmesi sonucunu dogurabilir."},{"facet_id":"F003","role":"specialization","statement":"Atlari veya av kopeklerini salmak gibi kullanimlarda dagitma, canlilari belli bir is icin alana yaymaktir."},{"facet_id":"F004","role":"specialization","statement":"Hurma, yemek, dosek, cekirge, kelebek veya toz gibi nesnelerde anlam daginik, serpilmis, cok veya savrulmus duruma yonelir."},{"facet_id":"F005","role":"extension","statement":"Yaratilmis varliklar icin kullanim, onlarin yeryuzune yayilmasini ve cogalmasini anlatir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Alana yayma, aciga cikarma, salma ve cogalma sonuclarini eksiltir.","preserves":"Birlesik halden ayrilma yonunu korur."},"text":"sadece ayirmak"},{"category":"confusable","error_profile":{"adds":"Haber veya soz iletme alanini ekler.","collision":"Bu karsilik daha cok ic icerigin veya haberin acilmasi dalina yaklasir.","fit":"displacement","loses":"Fiziksel dagitma ve alana yayilma cekirdegini kaybeder.","preserves":"Yayma fikrinin iletisim alanindaki bir benzerini tasir."},"text":"duyurmak"}],"identity_rationale":"Kaynak deyimi, bir seyi dagitma, ortaya cikararak yayma, savurma veya canlilari yeryuzune salip cogaltma ekseninde tutarlidir. Provisional cerceve bu fiziksel dagitma ve yayma cekirdegini, atlar, kopekler, cekirge, toz, yiyecek ve insanlar gibi farkli nesnelere uygulanisini dogru bicimde kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir seyi dagitip yaymak veya aciga cikarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"atlari saldiriya yaymak veya av kopeklerini ava salmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yayilip dagilmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"cok ve daginik; yayilmis veya savrulmus"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"toplanmamis, etrafa sacilmis hurma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yiyecegi veya hurmayi alt ust edip birbirinin ustune atmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yaratilmislari veya hayvanlari yeryuzune yayip cogaltmak"}],"lexicalization_note":"Ciplak kullanim dagitma ve yayma cekirdegini verir; at, av kopegi, hurma, yiyecek ve yaratilis baglamlari bu cekirdegin bagimli uygulamalaridir.","neighbor_coverage_note":"Aday komsularin hepsi degerlendirildi; avcilik, otlak veya cekirge toplulugu gibi yalniz ayni sahneye dokunan adaylar siniri keskinlestirmedigi icin yayimlanmadi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Okur icin en yakin karisim, ikisinin de dagitma sozcuguyle karsilanabilmesidir. Bu dal alana yayilmislik ve ortaya sacilma sonucuna giderken komsu dal daha cok ayirma, parcalara bolme ve birligi bozma sinirindadir.","focus_only":"Bu dalda dagitma, yayma, savurma, salma ve cogaltma sonucuyla birlikte dusunulur.","gloss":"dagitma ile ayirma","neighbor_only":"Komsu dalda ayirma, bolme, toplulugu veya sozu parcalara ayirma ve uzaklastirma daha belirgindir.","neighbor_ref":"root_001148/B002","relation_type":"near_synonym","shared_zone":"Iki dal da toplu olan seyin bolunup ayrilmasi alaninda bulusur."},{"boundary_match":"field_only","distinction":"Fiziksel dagitma ile icteki bilginin veya kederin acilmasi ayni genel disa cikma alanina ait olsa da birbirinin yerine gecmez. Birincisi nesnelerin alana yayilmasi, ikincisi sakli icerigin baskasina bildirilmesidir.","focus_only":"Bu dal somut seyleri, canlilari veya tozu alana dagitip yayar.","gloss":"yayma ile acma","neighbor_only":"Komsu dal haber, sir, keder veya icte sakli olan seyin dile getirilmesiyle ilgilidir.","neighbor_ref":"root_000083/B002","relation_type":"same_field","shared_zone":"Her ikisinde de kapali veya toplu bir durumdan disa yonelme vardir."},{"boundary_match":"partial","distinction":"Komsu dal daginik boluk veya yol gruplarini adlandiran daha durumsal bir alan verir. Bu dal ise bir seyin dagitilmasi ya da yayilmasi islemini ve onun sonucunu anlatir.","focus_only":"Bu dal dagitma eylemini, savurmayi, salmayi ve cogalmayi da kapsar.","gloss":"sacma ile daginik bolukler","neighbor_only":"Komsu dal daha cok insanlarin, seylerin veya yollarin her yonde daginik bolukler halinde bulunmasidir.","neighbor_ref":"root_000973/B010","relation_type":"near_neighbor","shared_zone":"Iki dalda da farkli yonlere dagilmislik gorulur."},{"boundary_match":"partial","distinction":"Komsu dalin siniri belirli bir kaliba baglidir ve arastirip ortaya cikarma anlamini da tasir. Bu dal ise o kalipla sinirli degil; somut dagitma, salma ve yayma cekirdegidir.","focus_only":"Bu dal ana kokun dagitma ve yayma cekirdegidir.","gloss":"genel yayma ile kalipli acma","neighbor_only":"Komsu dal yalniz belirli yinelenmis fiil kalibinda haber, is veya tozu yayma, arastirma ya da aciga cikarma kullanimidir.","neighbor_ref":"root_000083/B003","relation_type":"near_neighbor","shared_zone":"Ikisinde de haberin veya tozun yayilmasi gibi ortak gorunen uygulamalar bulunur."}],"source_phrase_ar":"تفريق الشيء وإظهاره؛ بثوا الخيل؛ بث الصياد كلابه؛ خلق الخلق وبثهم في الأرض؛ وزرابي مبثوثة؛ تمر بث؛ بثثت الطعام والتمر (maqayis)؛ بث الخيل؛ كل شيء فرقته؛ انبث الجراد؛ كالفراش المبثوث؛ تمر بث (jamhara)؛ فانبث أي انتشر؛ تمر بث؛ منثورا متفرقا؛ الغبار إذا هيجته (sihah)؛ تفريقك الأشياء؛ بثوا الخيل؛ بث الصياد كلابه؛ بثت البسط؛ مبثوثة كثيرة؛ غبارا منتشرا؛ وبث منهما رجالا كثيرا ونساء أي نشر وكثر (tahdhib)؛ التفريق وإثارة الشيء كبث الريح التراب؛ بثثته فانبث؛ وبث فيها؛ كالفراش المبثوث (mufradat)","source_summary":"Butun kanit, dalin dagitma ve yayma cekirdeginde birlestigini gosterir. Kaynaklardaki ornekler bunu kimi zaman somut esyayi sacma, kimi zaman hayvanlari salma, kimi zaman toz veya boceklerin yayilmasi, kimi zaman da insanlarin ve canlilarin yeryuzunde cogalmasi olarak uygular.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه تفريق الأشياء ونشرها وبسطها وإثارتها، وانتشار الخيل والدواب والجراد والفراش والغبار والمتاع والطعام والتمر وكثرة الخلق بعد بثهم","what_is_not_ar":"ليس حزن النفس المكبوت ولا سرها ولا تفتيش الأمر بصيغة بثبث"},"support_links":["sup_59a386babb4f3cd37cff"]},{"boundary":"Bu dal, nesnelerin yere veya alana dagitilmasi degil, sakli haberin, sirrin veya ic sikintisinin acilmasidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000083/B002","candidate_links":[{"candidate_id":"cand_173c5faaa621e6d6c43b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَبْثُوثَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:16:2:1","qac_word_ref":"88:16:2","surface_ar":"مَبْثُوثَةٌ"}],"gloss":"icindekini acip dile getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, sakli veya icte tutulan icerigi disa vurmak ve baskasina bildirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Haber ve soz baglaminda kullanim, bunlari yaymak veya duyurmak anlamina gelir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sir veya sakli bilgi baglaminda kullanim, onu birine acmak ve haberdar etmektir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Keder, gam veya sikinti baglaminda anlam, icteki agirligi sikayet ederek veya paylasarak aciga vurur."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir kaynakta gecen kapali bedensel, sevgiyle ilgili veya isleri yoklama yorumu, dalin sakli seyi anlamaya calisma kenarina temas eder."}}],"root_ar":"ب ث ث","root_id":"root_000083","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sir, haber, keder veya sikintinin sakli halden baskasina acildigi cekirdegi iyi karsilar.","boundary_detail":"Bu dal, nesnelerin yere veya alana dagitilmasi degil, sakli haberin, sirrin veya ic sikintisinin acilmasidir.","branch_image_ar":"إظهار المكتوم من النفس","concept_gloss":"icindekini acip dile getirmek","contextual_glosses":[{"applicability":"Haber veya sozun baskalarina duyuruldugu baglamlarda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sir acma ve ic kederi sikayet etme yonlerini kapsamaz.","preserves":"Iletisimsel yayma ve duyurma yonunu korur."},"facet_ids":["F002"],"text":"haberi yaymak","usage_role":"contextual"},{"applicability":"Birine sakli bilgiyi bildirme baglamlarinda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Haber yayma ve keder adini kapsamaz.","preserves":"Gizli icerigi birine acma yonunu korur."},"facet_ids":["F003"],"text":"sirrini acmak","usage_role":"contextual"},{"applicability":"Keder, gam veya sikintinin bir dosta sikayet olarak acildigi baglamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Haber ve sir baglamlarini kapsamaz.","preserves":"Ic sikintisinin baskasina acilmasi yonunu korur."},"facet_ids":["F004"],"text":"derdini dokmek","usage_role":"contextual"}],"definition":"Sakli bir haber, soz, sir veya icteki kederi kapali tutmayip baskasina acmak, yaymak ya da sikayet olarak dile getirmek; ad kullaniminda insanin icinde tasidigi keder, gam veya sikinti da bu acilabilir icerik olarak adlandirilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, sakli veya icte tutulan icerigi disa vurmak ve baskasina bildirmektir."},{"facet_id":"F002","role":"specialization","statement":"Haber ve soz baglaminda kullanim, bunlari yaymak veya duyurmak anlamina gelir."},{"facet_id":"F003","role":"specialization","statement":"Sir veya sakli bilgi baglaminda kullanim, onu birine acmak ve haberdar etmektir."},{"facet_id":"F004","role":"extension","statement":"Keder, gam veya sikinti baglaminda anlam, icteki agirligi sikayet ederek veya paylasarak aciga vurur."},{"facet_id":"F005","role":"source_variant","statement":"Bir kaynakta gecen kapali bedensel, sevgiyle ilgili veya isleri yoklama yorumu, dalin sakli seyi anlamaya calisma kenarina temas eder."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Haber yayma, sir acma ve sikayet ederek disa vurma eylemini kaybeder.","preserves":"Keder ve gam adini kismen korur."},"text":"uzuntu"},{"category":"confusable","error_profile":{"adds":"Fiziksel nesne dagitma alanini ekler.","collision":"Bu karsilik fiziksel dagitma dalina kayar.","fit":"displacement","loses":"Sakli haber, sir veya kederin iletisimsel acilisini kaybeder.","preserves":"Bir seyin disari yonelmesi fikrini dolayli olarak korur."},"text":"sacmak"}],"identity_rationale":"Kaynak deyimi, haber veya sozu yayma ile sir, keder, gam ve sikintiyi sakli halden cikarip baskasina acma alanini ayni dalda toplar. Provisional cerceve, fiziksel dagitmadan ayrilan iletisimsel ve ruhsal disa vurma sinirini dogru kurar.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"haberi veya sozu yaymak, duyurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"birine sirrini acmak ve onu haberdar etmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"insanin icinde tasidigi keder, gam veya sikinti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yoksullugunu ve duskunlugunu birine sikayet etmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gizli bir kusur, sevgi veya isin durumunu yoklayip anlamaya calisma"}],"lexicalization_note":"Dal hem adlasmis ic sikinti kullanimini hem de haber, sir ve sikayeti acma gibi bagimli yapilari kapsar; bunlar fiziksel yayma anlamina genellenmez.","neighbor_coverage_note":"Adaylarin tumu tartildi; salt hüzün sesi, kalbi yakan keder veya genel ifade araci gibi adaylar bu dalin sinirini yineleyen yahut uzaktan tematik kalan bilgiler verdigi icin secilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komsu dal sikayet etme alaninda daha dardir. Bu dal ise sikayet edilmis kederin yaninda haberin yayilmasini ve sirrin birine acilmasini da kapsar.","focus_only":"Bu dal sir, haber, ic sikinti ve kederi acma alanini birlikte tasir.","gloss":"icini acma ile sikayet","neighbor_only":"Komsu dal daha belirgin olarak kotu davranis veya incinme uzerine sikayet gostermeye yonelir.","neighbor_ref":"root_000814/B001","relation_type":"near_synonym","shared_zone":"Iki dal da kisinin icindeki sikintiyi veya haberi sozle ortaya koymasinda bulusur."},{"boundary_match":"partial","distinction":"Komsu dal genel gorunme ve ortaya cikma alanini verir. Bu dalda aciga cikma, haber, sir veya ic durumun iletisim yoluyla baskasina aktarilmasina baglidir.","focus_only":"Bu dal sakli soz, sir veya kederin birine acilmasi ve anlatilmasidir.","gloss":"dile acma ile gorunme","neighbor_only":"Komsu dal bir seyin gizlilikten sonra gorunur hale gelmesi veya gostermeye cikarilmasidir.","neighbor_ref":"root_000105/B001","relation_type":"near_neighbor","shared_zone":"Ikisinde de kapali olanin aciga cikmasi vardir."},{"boundary_match":"field_only","distinction":"Bu dalin nesnesi cogunlukla haber, sir veya ruhsal yuktur. Komsu dalin nesnesi ise somut seyler ve canlilardir; bu nedenle dogal Turkce karsiliklar ayrilir.","focus_only":"Bu dal haber, sir ve keder gibi ic veya iletisimsel icerigi aciga vurur.","gloss":"iceriği acma ile nesne yayma","neighbor_only":"Komsu dal seyleri, canlilari veya tozu fiziksel olarak dagitip yayar.","neighbor_ref":"root_000083/B001","relation_type":"same_field","shared_zone":"Her iki dalda da kapali veya toplu durumdan disa dogru bir hareket fikri vardir."},{"boundary_match":"partial","distinction":"Komsu dal daha cok acikta kalma veya gizleyememe durumunu adlandirir. Bu dalda ise icerigin birine acilmasi, anlatilmasi veya sikayet olarak dile getirilmesi esastir.","focus_only":"Bu dal sakli icerigi acma veya paylasma eylemini anlatir.","gloss":"paylasma ile acikta kalma","neighbor_only":"Komsu dal sir saklamayan kimseyi, ortunun acilmasini veya gizlenmesi gerekenin gorunmesini anlatir.","neighbor_ref":"root_001139/B007","relation_type":"near_neighbor","shared_zone":"Gizli kalmasi beklenen seyin ortaya cikmasi iki dalda da bulunur."},{"boundary_match":"field_only","distinction":"Komsu dalin ayirici yonu kalip siniri ve arastirma, yoklama, kesfetme anlamidir. Bu dal ise kisinin sakli icerigi veya ic sikintisini baskasina acmasina yonelir.","focus_only":"Bu dal sir, haber ve kederin acilmasina dayanir.","gloss":"sır acma ile arastirip acma","neighbor_only":"Komsu dal belirli yinelenmis fiil kalibinda haber veya isi yayma, arastirma ve ortaya cikarma kullanimi tasir.","neighbor_ref":"root_000083/B003","relation_type":"same_field","shared_zone":"Ikisinde de haber veya kapali bir seyin ortaya cikarilmasi gorulebilir."}],"source_phrase_ar":"بثثت الحديث أي نشرته؛ البث من الحزن؛ يشتكى ويبث ويظهر؛ أبث فلان شقوره وفقوره؛ وأبثثتك مكتومي (maqayis)؛ بثثته سري وأبثثته؛ البث ما يجده الرجل في نفسه من كرب أو غم (jamhara)؛ بث الخبر وأبثه؛ نشره؛ أبثثتك سري؛ أظهرته لك؛ البث الحال والحزن؛ أظهرت لك بثي (sihah)؛ البث الحزن الذي تفضي به إلى صاحبك؛ أبثثت فلانا سري؛ أطلعته عليه؛ لا يولج الكف ليعلم البث (tahdhib)؛ بث النفس ما انطوت عليه من الغم والسر؛ غمي الذي أبثه عن كتمان (mufradat)","source_summary":"Kanitlar haberin ve sozun yayilmasi, sirrin birine acilmasi ve kisinin icinde buldugu keder ya da sikintiyi dile getirmesi etrafinda birlesir. Tekil yorum farklari bulunan kapali ornek de sakli olanin bilinmesi veya yoklanmasi fikrini bu dalin kenarinda tutar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه بث الخبر والحديث والسر، وإبثاث المكتوم، وشكاية الحزن والكرب والغم الذي في النفس","what_is_not_ar":"ليس تفريق الأشياء في الأرض ولا نشر الخيل والدواب ولا بثبثة الأمر"},"support_links":["sup_0727bd5e706fb64231ea"]},{"boundary":"Bu dal yalniz belirli kalipli kullanimdir; genel fiziksel dagitma veya ic kederi acma anlami buraya genellenmez.","branch_kind":"collocation","branch_ref":"root_000083/B003","candidate_links":[{"candidate_id":"cand_3fed034045a414151c06","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَبْثُوثَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:16:2:1","qac_word_ref":"88:16:2","surface_ar":"مَبْثُوثَةٌ"}],"gloss":"arastirip aciga cikarmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, belirli kalipli kullanimla sinirlidir ve genel kok anlaminin tamamini temsil etmez."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Haber baglaminda anlam, haberi yaymak veya duyurmaktir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toz baglaminda anlam, tozu kaldirip savurmaktir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Is veya mesele baglaminda anlam, arastirmak, yoklamak, haberini almak ve aciga cikarmaktir."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kanit, bu kalibin ana fiilden ses degisimiyle aciklandigini da bildirir; bu bilgi anlami genel dala geri tasimaz."}}],"root_ar":"ب ث ث","root_id":"root_000083","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Is veya mesele baglamindaki kalipli kullanimi iyi karsilar; haber ve toz baglamlari icin aciklama gerekir.","boundary_detail":"Bu dal yalniz belirli kalipli kullanimdir; genel fiziksel dagitma veya ic kederi acma anlami buraya genellenmez.","branch_image_ar":"بثبثة الأمر وكشفه","concept_gloss":"arastirip aciga cikarmak","contextual_glosses":[{"applicability":"Belirli kalip haberle kullanildiginda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Is arastirma ve toz savurma kullanimlarini kapsamaz.","preserves":"Haberin yayilmasi yonunu korur."},"facet_ids":["F001","F002"],"text":"haberi yaymak","usage_role":"contextual"},{"applicability":"Belirli kalip tozla kullanildiginda tozun kaldirilip yayilmasini karsilar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Haber yayma ve is arastirma kullanimlarini kapsamaz.","preserves":"Tozu hareketlendirip yayma yonunu korur."},"facet_ids":["F001","F003"],"text":"tozu savurmak","usage_role":"contextual"},{"applicability":"Bir mesele hakkinda arastirma, haber alma ve sakli yani ortaya cikarma baglaminda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yayma ve savurma kullanimlarini kapsamaz.","preserves":"Arastirma, yoklama ve bilgi edinme yonunu korur."},"facet_ids":["F001","F004"],"text":"isi yoklayip ogrenmek","usage_role":"contextual"}],"definition":"Belirli yinelenmis fiil kalibinda bir haberi yaymak veya tozu kaldirip savurmak; is ve mesele baglaminda ise onu arastirip yoklamak ve sakli yanini aciga cikarmak anlatilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, belirli kalipli kullanimla sinirlidir ve genel kok anlaminin tamamini temsil etmez."},{"facet_id":"F002","role":"specialization","statement":"Haber baglaminda anlam, haberi yaymak veya duyurmaktir."},{"facet_id":"F003","role":"specialization","statement":"Toz baglaminda anlam, tozu kaldirip savurmaktir."},{"facet_id":"F004","role":"extension","statement":"Is veya mesele baglaminda anlam, arastirmak, yoklamak, haberini almak ve aciga cikarmaktir."},{"facet_id":"F005","role":"source_variant","statement":"Kanit, bu kalibin ana fiilden ses degisimiyle aciklandigini da bildirir; bu bilgi anlami genel dala geri tasimaz."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kalip sinirini ve arastirip aciga cikarma ozelligini silerek genel dagitma alanini ekler.","collision":"Bu karsilik birinci dalin genel yayma anlamiyla karisir.","fit":"broadening","loses":null,"preserves":"Haber veya tozun yayilmasi yonunu kismen korur."},"text":"genel olarak yaymak"},{"category":"confusable","error_profile":{"adds":"Keder veya zarar bildirimi anlamini ekler.","collision":"Bu karsilik ikinci dalin ic sikintiyi dile getirme alanina kayar.","fit":"displacement","loses":"Haber yayma, toz savurma ve isi arastirip aciga cikarma cekirdegini kaybeder.","preserves":"Kapali bir seyin sozle ortaya konmasina uzak bir benzerlik tasir."},"text":"sikayet etmek"}],"identity_rationale":"Kaynak deyimi, belirli yinelenmis fiil kalibinda haberin yayilmasi, tozun kaldirilmasi, bir isin arastirilip yoklanmasi ve aciga cikarilmasi kullanimlarini bir araya getirir. Provisional cerceve, bu dalin ana dagitma veya ic keder dalindan farkli olarak kalipla sinirli oldugunu dogru belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"haberi yaymak veya tozu kaldirip savurmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir isi arastirip yoklamak veya aciga cikarmak"}],"lexicalization_note":"Mekanik sinir collocation oldugu icin tanim, sadece haber, toz veya isin bu belirli kalipli kullanimdaki yayma, yoklama ve aciga cikarma anlamini kapsar.","neighbor_coverage_note":"Aday komsularin hepsi gozden gecirildi; kahinlik, genel acikta kalma ve iz surme gibi alanlar ya cok uzak tematik kaldi ya da secilen arastirma komsularinin verdigi siniri yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komsu dal arastirma ve haber isteme icin daha genel bir alandir. Bu dal ise sadece belirli kalipli kullanimda calisir ve haberin yayilmasi ya da tozun savrulmasi gibi ek baglamlara sahiptir.","focus_only":"Bu dal belirli kalipla sinirlidir ve haber yayma ile toz savurma kullanimlarini da tasir.","gloss":"kalipli yoklama ile haber sorma","neighbor_only":"Komsu dal genel olarak sorma, haber isteme, arastirma ve sirri kesfetme alanini verir.","neighbor_ref":"root_000085/B002","relation_type":"near_synonym","shared_zone":"Iki dalda da bir mesele hakkinda arastirip bilgi edinme ve kapali yani acma bulunur."},{"boundary_match":"partial","distinction":"Komsu dalin merkezi gizli olana vakif olma ve onu bildirmedir. Bu dalda ise kalipli arastirma-yoklama hareketi ve ayrica yayma ya da savurma kullanimi bulunur.","focus_only":"Bu dal kalipli olarak isi yoklama, haberi yayma ve tozu savurma kullanimlarini birlestirir.","gloss":"yoklayip acma ile vakif olma","neighbor_only":"Komsu dal gizli bir seye vakif olma, onun uzerine cikma veya baskasina bildirme alanindadir.","neighbor_ref":"root_000982/B001","relation_type":"near_neighbor","shared_zone":"Ikisi de gizli veya bilinmeyen seyin bilgisine ulasma ve onu aciga getirme alanina dokunur."},{"boundary_match":"partial","distinction":"Komsu dal daha genis kesif ve bakip anlama alanidir. Bu dalin kimligi ise belirli kalip ve onun haber, toz, mesele uzerindeki ozel kullanimlariyla kurulur.","focus_only":"Bu dal belirli kalipta arastirma, haber yayma ve toz savurma anlamlariyla sinirlidir.","gloss":"kalipli arastirma ile isin icine bakma","neighbor_only":"Komsu dal bir seye veya isin ic yuzune bakma, ortaya cikarma, bas gostermesi ve gorus yoklama gibi daha genis kullanimlar tasir.","neighbor_ref":"root_000945/B003","relation_type":"near_neighbor","shared_zone":"Ikisi de bir isin gizli veya ic yuzunu anlamaya yonelir."},{"boundary_match":"partial","distinction":"Komsu dal kalipsiz genel dagitma ve yayma alanidir. Bu dal, kalip siniri yuzunden daha dar ve ayrica bir meseleyi arastirip ortaya cikarma yonuyle farklidir.","focus_only":"Bu dal belirli kalipla bagli olarak yayma, savurma ve arastirip acma anlatir.","gloss":"kalipli yayma ile genel dagitma","neighbor_only":"Komsu dal ana fiziksel dagitma, yayma, salma ve cogalma cekirdegidir.","neighbor_ref":"root_000083/B001","relation_type":"near_neighbor","shared_zone":"Haber veya tozun yayilmasi noktasinda ortak gorunen bir alan vardir."},{"boundary_match":"field_only","distinction":"Komsu dalin agirligi icte tutulan icerigi paylasmadadir. Bu dal ise kalipli arastirma ve yoklama ile, bazi baglamlarda haberi yayma veya tozu savurma anlamina gider.","focus_only":"Bu dal arastirip aciga cikarma ve kalipli haber yayma kullanimidir.","gloss":"arastirip acma ile icini acma","neighbor_only":"Komsu dal sir, haber, keder veya ic sikintisini baskasina acma alanidir.","neighbor_ref":"root_000083/B002","relation_type":"same_field","shared_zone":"Ikisinde de haber veya kapali bir icerigin ortaya cikmasi gorulebilir."}],"source_phrase_ar":"بثبثت الخبر بثبثة نشرته؛ وكذلك الغبار إذا هيجته (sihah)؛ بثبثت الأمر إذا فتشت عنه وتخبرته؛ بثبثوه أي كشفوه؛ الأصل فيه بثثوه فأبدلوا (tahdhib)","source_summary":"Kanit iki hat verir: haber veya toz icin yayma ve kaldirma, is veya mesele icin arastirip yoklama ve aciga cikarma. Bu hatlar ortak bir kalip siniri altindadir; bu nedenle dal, genel dagitma veya ic keder acma anlaminin yerine gecmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه بثبثة الخبر أو الأمر بمعنى نشره أو تفتيشه أو كشفه، وإثارة الغبار بهذا اللفظ","what_is_not_ar":"ليس أصل تفريق الأشياء بلا صيغة بثبث ولا حزن النفس المسمى بثا"},"support_links":["sup_234d2dc528ca35284ccd"]}],"candidate_inventory":[{"anchor_refs":["88:16:1"],"branch_refs":[],"candidate_id":"cand_f88204f119baa49bd589","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:1:alternative-values-narrowed","source_type":"word_analysis","support_ids":["sup_d8a78c4162760377e2dc","sup_f408300454515a0774b2"],"title":"resumptive and circumstantial values limited","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:1","qac_refs":["88:16:1:1"],"status":"accepted"}},{"anchor_refs":["88:16:1"],"branch_refs":[],"candidate_id":"cand_4799a6af21e789faa12e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:1:boundary-before-turn","source_type":"word_analysis","support_ids":["sup_38b2404ee6ae7022d30e","sup_d8a78c4162760377e2dc"],"title":"catalogue boundary before 88:17","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:1","qac_refs":["88:16:1:1"],"status":"accepted"}},{"anchor_refs":["88:16:1"],"branch_refs":[],"candidate_id":"cand_26da1352f70cff366207","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:1:inventory-coordination","source_type":"word_analysis","support_ids":["sup_83553d22b604d4775ffb","sup_d8a78c4162760377e2dc"],"title":"final item coordinated into the inventory","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:1","qac_refs":["88:16:1:1"],"status":"accepted"}},{"anchor_refs":["88:16:1"],"branch_refs":[],"candidate_id":"cand_96e812d9de7ba6c9e284","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:1:prefixed-liaison-cadence","source_type":"word_analysis","support_ids":["sup_98683cccafe743b62e43","sup_d8a78c4162760377e2dc"],"title":"brief connector as audible pickup","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:1","qac_refs":["88:16:1:1"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_1a94651749e235669306","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:catalogue-culmination","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_d578bc84bd7c90e02e61"],"title":"ground-covering culmination of the furnishing list","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_8fbc0116009e9dc72f4a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:heavy-textile-cadence","source_type":"word_analysis","support_ids":["sup_003d3f3aa13e6f178119","sup_1c105429e0227e898370"],"title":"heavy textile cadence before outward release","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_869e7d1cff57e0b42e94","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:hidden-brocade-contrast","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_9bfb6c34e040e2bf32ec"],"title":"visible surface contrast with 55:54","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_196e567b79146556b0a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:nominative-indefinite-head","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_8367ded43726e131a16f"],"title":"indefinite plural head in a compressed locative frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_de9e5253bd31152d5a18","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:object-before-state","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_8a0bce62c5e7c926554b"],"title":"object named before spread-state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_9b9cb95c12322016ac0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:plural-to-collective-field","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_b53beb70277bb597e671"],"title":"plural carpets become one field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_430354a5d30c1b979ffb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:rare-local-anchor","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_4a26c4db082ec77333d8"],"title":"rare noun interpreted by local anchors","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_267aa045055cc5e5aa89","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:rowed-cushions-to-carpet-field","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_a5c94f48948626139812"],"title":"from rowed cushions in 88:15 to carpet coverage","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_324260d9d334e05a5bab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:surface-environment-luxury","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_4120ef314d43e1479396"],"title":"luxury reaches the floor surface","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_96771ec3d8cb883dd0cf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:16:2:textile-branch-selected","source_type":"word_analysis","support_ids":["sup_1c105429e0227e898370","sup_a579929ae5c5289acd65"],"title":"patterned textile branch selected","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:2","qac_refs":["88:16:1:2"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_8143fcb08fbfdb9d648d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:chaos-to-repose-contrast","source_type":"word_analysis","support_ids":["sup_b2dd24ceb51ad011933a","sup_c17dd717888614c22356"],"title":"scattering reversed into repose at 101:4 and 56:6","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_f420e5c44c3c9504ffef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:completed-display-before-looking","source_type":"word_analysis","support_ids":["sup_c17dd717888614c22356","sup_d2ec5e0de1792db58c80"],"title":"completed display before the looking question in 88:17","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_0f5888bfa268152900cb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:dependent-collective-adjective","source_type":"word_analysis","support_ids":["sup_b4a49a1e6a2ce459bdf8","sup_c17dd717888614c22356"],"title":"dependent adjective makes one collective field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_cd0fa0a82f8eb00de41e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:diffused-sound","source_type":"word_analysis","support_ids":["sup_b3b59e75618aabbed9e0","sup_c17dd717888614c22356"],"title":"sound disperses with the spread image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_a1dc96623fd65329533a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:dispersal-domesticated","source_type":"word_analysis","support_ids":["sup_c17dd717888614c22356","sup_d31eca037c36b641fd19"],"title":"dispersal turned into ordered hospitality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_e2b4f2db2c928a305d12","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:distress-and-creature-spread-echoes","source_type":"word_analysis","support_ids":["sup_c0a1ba9dd43f9c8f34ef","sup_c17dd717888614c22356"],"title":"diffusion echoes from 12:86 and 2:164","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_8c112de515003370d45e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:indefinite-condition","source_type":"word_analysis","support_ids":["sup_c17dd717888614c22356","sup_c4d14fa473c049477811"],"title":"indefinite condition of the carpet field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_0c18e9c1bcf544d811d4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:list-closure-before-88-17","source_type":"word_analysis","support_ids":["sup_9eb9a3feb6936bf4dd38","sup_c17dd717888614c22356"],"title":"final participle closes the tableau before 88:17","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_ecc8baa7d0348250e1a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:non-reflexive-non-causative-limit","source_type":"word_analysis","support_ids":["sup_c17dd717888614c22356","sup_f849eb1849ba2c0385bb"],"title":"self-dispersal and causation kept out","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_1459555f15278d18fd8e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:object-to-field-sequence","source_type":"word_analysis","support_ids":["sup_397d7156609f747c941e","sup_c17dd717888614c22356"],"title":"textile object resolves into field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_74765a4293adc6900919","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:ordered-field-boundary","source_type":"word_analysis","support_ids":["sup_1b45d9b2894e5eab82b3","sup_c17dd717888614c22356"],"title":"ordered alignment complemented by broad coverage","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_2b64a93eb8a42d5f8cbc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:outward-disclosure-pressure","source_type":"word_analysis","support_ids":["sup_711dfac50277f222f236","sup_c17dd717888614c22356"],"title":"outwardness redirected from disclosure to visible comfort","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_f4249273651babe8bb8b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:participial-cadence","source_type":"word_analysis","support_ids":["sup_852b5109a9fae846fc24","sup_c17dd717888614c22356"],"title":"indefinite participial cadence completes the endings","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_680f7d1e7f78256e7376","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:passive-result-state","source_type":"word_analysis","support_ids":["sup_b24a66c8a1a0ffeb533d","sup_c17dd717888614c22356"],"title":"completed result-state without narrated agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_aa0d6597d54f1b4c9b7c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:rare-marked-form","source_type":"word_analysis","support_ids":["sup_c17dd717888614c22356","sup_fe6f23e0898a8283888a"],"title":"limited passive-participle recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_cb77c7c961dd0299cb03","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:rowed-to-spread-handoff","source_type":"word_analysis","support_ids":["sup_6549b212c80c38e33863","sup_c17dd717888614c22356"],"title":"from rows in 88:15 to coverage in 88:16","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_3826d92a3bfa750eb706","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:variant-collective-surface","source_type":"word_analysis","support_ids":["sup_c10e0d87ef6269394fa3","sup_c17dd717888614c22356"],"title":"variant pronoun reinforces collective surface","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:3"],"branch_refs":[],"candidate_id":"cand_b8244094755466356727","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:3:variant-reclining-apparatus","source_type":"word_analysis","support_ids":["sup_c028e39d6fb5f2260960","sup_c17dd717888614c22356"],"title":"variant makes embedded use explicit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:16:3","qac_refs":["88:16:2:1"],"status":"accepted"}},{"anchor_refs":["88:16:2"],"branch_refs":[],"candidate_id":"cand_4d37e7284df4a29aa806","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000083"],"scope":"focus_ayah","source_local_id":"88:16:2:1","source_type":"qac_morpheme","support_ids":["sup_e3910ce32ec5b9382a41"],"title":"QAC root occurrence: ب ث ث","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:16","branch_refs":["root_000083/B001"],"candidate_id":"cand_53d8e396ab694477b08c","commentary_obligation":"review","hft_ref":"hft_e09db0bb250d8f87bf72","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_areal_distribution","source_type":"hft","support_ids":["sup_59a386babb4f3cd37cff"],"title":"baseline_areal_distribution","trust":"legacy_unbound"},{"anchor_refs":["88:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:16","branch_refs":["root_000083/B002"],"candidate_id":"cand_173c5faaa621e6d6c43b","commentary_obligation":"review","hft_ref":"hft_dec2e4b3b6a597bbfcff","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_disclosed_interior","source_type":"hft","support_ids":["sup_0727bd5e706fb64231ea"],"title":"baseline_disclosed_interior","trust":"legacy_unbound"},{"anchor_refs":["88:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:16","branch_refs":["root_000083/B003"],"candidate_id":"cand_3fed034045a414151c06","commentary_obligation":"review","hft_ref":"hft_adb53c8d5c4fbd4599aa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inspectable_layout","source_type":"hft","support_ids":["sup_234d2dc528ca35284ccd"],"title":"baseline_inspectable_layout","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:16:1:1","qac_word_ref":"88:16:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"زَرَابِىّ","morph_features":"STEM|POS:N|LEM:zaraAbiY~|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:16:1:2","qac_word_ref":"88:16:1","root_ar":"","surface_ar":"زَرَابِىُّ"},{"lemma_ar":"مَبْثُوثَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:16:2:1","qac_word_ref":"88:16:2","root_ar":"ب ث ث","surface_ar":"مَبْثُوثَةٌ"}],"word_analysis_qac_refs":[["88:16:1:1"],["88:16:1:2"],["88:16:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:16:1","88:16:2","88:16:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:16:1:1","qac_word_ref":"88:16:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"زَرَابِىّ","morph_features":"STEM|POS:N|LEM:zaraAbiY~|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:16:1:2","qac_word_ref":"88:16:1","root_ar":"","surface_ar":"زَرَابِىُّ"},{"lemma_ar":"مَبْثُوثَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:16:2:1","qac_word_ref":"88:16:2","root_ar":"ب ث ث","surface_ar":"مَبْثُوثَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:16:1:1"],["88:16:1:2"],["88:16:2:1"]],"word_analysis_refs":["88:16:1","88:16:2","88:16:3"],"word_rows":[{"analysis_record_ref":"88:16:1","analytic_gloss_range_en":"coordinating list-particle that carries the final furnishing item within the same compressed garden inventory","analytic_root_gloss_range_en":null,"qac_refs":["88:16:1:1"],"root":{"note":"—"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:16:2","analytic_gloss_range_en":"indefinite plural patterned carpets or rich floor-coverings, displayed as the final furnishing head and made into a spread field by the following adjective","analytic_root_gloss_range_en":"root range includes enclosed shelter meanings and patterned textile furnishings; the local plural noun selects the patterned textile branch, not the shelter branch","qac_refs":["88:16:1:2"],"root":{"arabic":"ز ر ب","transliteration":"z-r-b"},"surface":{"arabic":"زَرَابِىُّ","transliteration":"zarābiyyu"}},{"analysis_record_ref":"88:16:3","analytic_gloss_range_en":"feminine singular passive-participle adjective marking the carpets as already spread, distributed, and laid out as one collective furnishing field","analytic_root_gloss_range_en":"root range includes physical spreading, scattering, diffusion, and outward disclosure; the local passive participle narrows that dispersal field into prepared carpet coverage","qac_refs":["88:16:2:1"],"root":{"arabic":"ب ث ث","transliteration":"b-th-th"},"surface":{"arabic":"مَبْثُوثَةٌ","transliteration":"mabthūthatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:16"],"branch_refs":["root_000083/B001"],"candidate_id":"cand_53d8e396ab694477b08c","evidence_scope":"focus_ayah","hft_ref":"hft_e09db0bb250d8f87bf72","item_id":"baseline_areal_distribution","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_areal_distribution","support_id":"sup_59a386babb4f3cd37cff"},{"anchor_refs":["88:16"],"branch_refs":["root_000083/B002"],"candidate_id":"cand_173c5faaa621e6d6c43b","evidence_scope":"focus_ayah","hft_ref":"hft_dec2e4b3b6a597bbfcff","item_id":"baseline_disclosed_interior","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_disclosed_interior","support_id":"sup_0727bd5e706fb64231ea"},{"anchor_refs":["88:16"],"branch_refs":["root_000083/B003"],"candidate_id":"cand_3fed034045a414151c06","evidence_scope":"focus_ayah","hft_ref":"hft_adb53c8d5c4fbd4599aa","item_id":"baseline_inspectable_layout","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inspectable_layout","support_id":"sup_234d2dc528ca35284ccd"}],"diagnostics":[],"lane_counts":{"global":14,"macro":5,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:16","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:16","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":13,"unstructured_record_count":0},"identity":{"ayah_ref":"88:16","lane":"micro","linguistic_source_ref":"88:16","surface_ref":"88:16","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:16","target_tokens":[["Serilmiş",["88:16:2"]],["halılar",["88:16:1"]],["da",["88:16:1"]],["vardır",["88:16:1"]]],"text":"Serilmiş halılar da vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:heavy-textile-cadence","source_type":"word_analysis","support_id":"sup_003d3f3aa13e6f178119","text":"{\"blocking_evidence\":null,\"headline\":\"heavy textile cadence before outward release\",\"reader_payoff\":\"The reader hears the rare textile word slow the recitation before the final adjective opens the image outward.\",\"reason\":\"These rows describe a sound effect tied to the actual surface sequence from connector to noun to adjective.\",\"representative_source_ids\":[\"QP-ad4bb66e\",\"QP-fdb860a4\",\"MP-cbbb4008\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:ordered-field-boundary","source_type":"word_analysis","support_id":"sup_1b45d9b2894e5eab82b3","text":"{\"blocking_evidence\":null,\"headline\":\"ordered alignment complemented by broad coverage\",\"reader_payoff\":\"The reader sees the final image expand beyond ranked placement while still remaining orderly within the furnishing context.\",\"reason\":\"The local adjective supplies diffusion, but the head noun and inventory context constrain it as prepared coverage rather than disorder.\",\"representative_source_ids\":[\"QB-9fa0704e\",\"QB-d6306fd9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2","source_type":"word_analysis","support_id":"sup_1c105429e0227e898370","text":"{\"gloss_range\":\"indefinite plural patterned carpets or rich floor-coverings, displayed as the final furnishing head and made into a spread field by the following adjective\",\"prose\":\"{{ar:زَرَابِىُّ}} ({{tr:zarābiyyu}}) names the final furnishing head as indefinite plural carpets: not one counted rug, but a newly disclosed class of rich textile surfaces entering the scene. Its nominative role and the recoverable locative frame display the carpets as present within the same garden inventory, while {{ar:مَبْثُوثَةٌ}} ({{tr:mabthūthatun}}) then gathers the plural into one spread field. The ayah first lets the listener register the luxurious object, then reveals its deployed state; grammatically displayed as a head noun, the carpets are semantically the prepared patient of spreading. The dictionary range of {{ar:ز ر ب}} ({{tr:z-r-b}}) includes shelter or enclosure language, but the local noun and V4 textile branch narrow the sense to patterned furnishings and floor-coverings. That matters because the catalogue has moved through couches, cups, and rowed cushions: by 88:16 the comfort reaches the ground surface itself, shifting from arranged support points to a continuous material field. The contrast with hidden brocade bedding (55:54) sharpens the local image, since this ayah foregrounds visible spread surfaces rather than concealed lining. Because this rare noun appears only here, its meaning leans on immediate anchors: textile sense, plural abundance, catalogue-final position, and the following spread-state. The rare word also slows the cadence; after the brief connector, the long textile noun gives the listener a material pause before the adjective opens the image outward.\",\"root_display\":\"{{ar:ز ر ب}} ({{tr:z-r-b}})\",\"root_gloss_range\":\"root range includes enclosed shelter meanings and patterned textile furnishings; the local plural noun selects the patterned textile branch, not the shelter branch\",\"surface_display\":\"{{ar:زَرَابِىُّ}} ({{tr:zarābiyyu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:1:boundary-before-turn","source_type":"word_analysis","support_id":"sup_38b2404ee6ae7022d30e","text":"{\"blocking_evidence\":null,\"headline\":\"catalogue boundary before 88:17\",\"reader_payoff\":\"The reader feels the furnished scene remain continuous through its final addition just before 88:17 changes the discourse mode.\",\"reason\":\"The same connective pattern carries the omitted garden-locative frame through the final furnishing item before the next ayah's shift.\",\"representative_source_ids\":[\"QB-03f83dda\",\"QB-c75ed054\",\"QB-d0a1df94\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:object-to-field-sequence","source_type":"word_analysis","support_id":"sup_397d7156609f747c941e","text":"{\"blocking_evidence\":null,\"headline\":\"textile object resolves into field\",\"reader_payoff\":\"The reader experiences the phrase moving from named carpets to a completed field of coverage without a narrative verb.\",\"reason\":\"The local sequence places the carpet noun before the passive participial adjective inside a verbless inventory.\",\"representative_source_ids\":[\"QT-50735824\",\"QT-7ace1ac3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:surface-environment-luxury","source_type":"word_analysis","support_id":"sup_4120ef314d43e1479396","text":"{\"blocking_evidence\":null,\"headline\":\"luxury reaches the floor surface\",\"reader_payoff\":\"The reader notices that comfort is not only elevated seating; the ground-level environment itself becomes prepared and luxurious.\",\"reason\":\"The selected textile sense and the following spread-state adjective together present usable surfaces that cover the scene.\",\"representative_source_ids\":[\"QS-3414d11a\",\"QS-77845851\",\"MS-c6fcb6bb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:rare-local-anchor","source_type":"word_analysis","support_id":"sup_4a26c4db082ec77333d8","text":"{\"blocking_evidence\":null,\"headline\":\"rare noun interpreted by local anchors\",\"reader_payoff\":\"The reader treats the noun's rarity as pressure to read by immediate anchors: textile sense, plural abundance, and the following spread-state.\",\"reason\":\"The contextual profile marks the exact noun as a single occurrence, so local grammar and V4's textile sense carry the interpretation.\",\"representative_source_ids\":[\"QI-8c9ed7fe\",\"QH-ed286757\",\"MH-f597e9f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:rowed-to-spread-handoff","source_type":"word_analysis","support_id":"sup_6549b212c80c38e33863","text":"{\"blocking_evidence\":null,\"headline\":\"from rows in 88:15 to coverage in 88:16\",\"reader_payoff\":\"The reader sees the spatial grammar widen from rowed cushions in 88:15 to spread carpets in 88:16.\",\"reason\":\"The adjacent furnishing adjectives at 88:15 and 88:16 support a row-to-coverage handoff.\",\"representative_source_ids\":[\"MT-eff61fae\",\"QE-86603b67\",\"QB-0ce859e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:outward-disclosure-pressure","source_type":"word_analysis","support_id":"sup_711dfac50277f222f236","text":"{\"blocking_evidence\":null,\"headline\":\"outwardness redirected from disclosure to visible comfort\",\"reader_payoff\":\"The reader notices outward diffusion as visible comfort spread across the place, while disclosure or complaint senses do not become the local meaning.\",\"reason\":\"V4 includes outward disclosure and distress-related uses, but the local adjective modifies carpets and therefore selects visible spatial spreading.\",\"representative_source_ids\":[\"QS-a9baacf2\",\"QS-d05e7089\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:1:inventory-coordination","source_type":"word_analysis","support_id":"sup_83553d22b604d4775ffb","text":"{\"blocking_evidence\":null,\"headline\":\"final item coordinated into the inventory\",\"reader_payoff\":\"The reader notices that the ayah is still adding to the same prepared garden inventory, not opening an unrelated sentence.\",\"reason\":\"QAC marks the word as a prefixed conjunction, and attachment evidence supports an omitted locative predicate continuing the furnishing inventory.\",\"representative_source_ids\":[\"QG-08f86a36\",\"QT-27f91c1d\",\"QE-848db49d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:nominative-indefinite-head","source_type":"word_analysis","support_id":"sup_8367ded43726e131a16f","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite plural head in a compressed locative frame\",\"reader_payoff\":\"The reader sees carpets displayed as an open furnishing category within the garden, not as counted objects in a narrated act.\",\"reason\":\"QAC marks an indefinite plural nominative noun, and attachment evidence licenses the omitted locative predicate that keeps the item inside the inventory.\",\"representative_source_ids\":[\"QG-0fea047a\",\"QG-90f19a50\",\"QG-a97ff24e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:participial-cadence","source_type":"word_analysis","support_id":"sup_852b5109a9fae846fc24","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite participial cadence completes the endings\",\"reader_payoff\":\"The reader hears the final prepared-state cadence join morphology, sound, and spatial coverage at the catalogue's close.\",\"reason\":\"The final word is an indefinite passive participial adjective, and the convergent row connects that form, sound, and boundary function.\",\"representative_source_ids\":[\"QP-93687d4c\",\"QY-c68c3048\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:object-before-state","source_type":"word_analysis","support_id":"sup_8a0bce62c5e7c926554b","text":"{\"blocking_evidence\":null,\"headline\":\"object named before spread-state\",\"reader_payoff\":\"The reader first registers the luxurious object, then sees it as the patient of completed placement through the following adjective.\",\"reason\":\"The surface order places the textile noun before its adjective, and attachment evidence identifies the adjective as the noun's state.\",\"representative_source_ids\":[\"QT-47237aee\",\"QS-91b714e1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:1:prefixed-liaison-cadence","source_type":"word_analysis","support_id":"sup_98683cccafe743b62e43","text":"{\"blocking_evidence\":null,\"headline\":\"brief connector as audible pickup\",\"reader_payoff\":\"The reader hears the short connector as a pickup into the rare, heavier textile noun.\",\"reason\":\"The particle is analytically separate but orthographically prefixed to the following noun, so the sound and list function arrive together.\",\"representative_source_ids\":[\"QF-07292a58\",\"QP-96fc8813\",\"QP-ed828b4d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:hidden-brocade-contrast","source_type":"word_analysis","support_id":"sup_9bfb6c34e040e2bf32ec","text":"{\"blocking_evidence\":null,\"headline\":\"visible surface contrast with 55:54\",\"reader_payoff\":\"The reader sees 88:16 place luxury on exposed spread surfaces, unlike the hidden brocade lining emphasized in 55:54.\",\"reason\":\"The row gives a concrete contrast with 55:54, and the local phrase foregrounds a textile noun followed by a spread-state adjective.\",\"representative_source_ids\":[\"QI-e3a13b7a\",\"MI-5b591433\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:list-closure-before-88-17","source_type":"word_analysis","support_id":"sup_9eb9a3feb6936bf4dd38","text":"{\"blocking_evidence\":null,\"headline\":\"final participle closes the tableau before 88:17\",\"reader_payoff\":\"The reader feels the furnishing run land on spread coverage before 88:17 shifts into an observational question.\",\"reason\":\"The word is the final term of the no-verb furnishing sequence and stands immediately before the discourse shift at 88:17.\",\"representative_source_ids\":[\"QT-1cd40865\",\"QT-fcd7d7f9\",\"QY-7fc9ae60\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:textile-branch-selected","source_type":"word_analysis","support_id":"sup_a579929ae5c5289acd65","text":"{\"blocking_evidence\":null,\"headline\":\"patterned textile branch selected\",\"reader_payoff\":\"The reader keeps the concrete carpet image central while avoiding speculative activation of the root's shelter or enclosure branch.\",\"reason\":\"V4 separates an enclosure branch from a patterned-furnishing branch; the local plural noun and inventory setting select the furnishing branch.\",\"representative_source_ids\":[\"QS-a8a1f146\",\"QS-f30dc28d\",\"QF-3f60765c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:rowed-cushions-to-carpet-field","source_type":"word_analysis","support_id":"sup_a5c94f48948626139812","text":"{\"blocking_evidence\":null,\"headline\":\"from rowed cushions in 88:15 to carpet coverage\",\"reader_payoff\":\"The reader notices the spatial handoff from arranged support points in 88:15 to a furnished surface in 88:16.\",\"reason\":\"The CRITICAL rows name the adjacent 88:15 furnishing boundary, and the local noun supplies the ground-covering counterpart.\",\"representative_source_ids\":[\"MT-622e014b\",\"QE-b8ab782e\",\"QB-018696a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:passive-result-state","source_type":"word_analysis","support_id":"sup_b24a66c8a1a0ffeb533d","text":"{\"blocking_evidence\":null,\"headline\":\"completed result-state without narrated agency\",\"reader_payoff\":\"The reader meets the carpets as already arranged provision before any agent or spreading action is named.\",\"reason\":\"The local form is a passive participial adjective in a verbless inventory, so completed placement is foregrounded while agency recedes.\",\"representative_source_ids\":[\"QG-f28c693f\",\"MG-011ac785\",\"QF-dfe24aa9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:chaos-to-repose-contrast","source_type":"word_analysis","support_id":"sup_b2dd24ceb51ad011933a","text":"{\"blocking_evidence\":null,\"headline\":\"scattering reversed into repose at 101:4 and 56:6\",\"reader_payoff\":\"The reader sees the same passive-participle dispersal field that can mark panic or fragmentation in 101:4 and 56:6 become calm placement in 88:16.\",\"reason\":\"The CRITICAL rows give concrete contrasts at 101:4 and 56:6, while the local furnishing head reverses the effect into repose.\",\"representative_source_ids\":[\"QS-8bea3918\",\"QI-55e6b9b4\",\"MI-25b559b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:diffused-sound","source_type":"word_analysis","support_id":"sup_b3b59e75618aabbed9e0","text":"{\"blocking_evidence\":null,\"headline\":\"sound disperses with the spread image\",\"reader_payoff\":\"The reader hears repeated and airy consonantal pressure reinforce the semantic movement from gathered object to distributed field.\",\"reason\":\"The sound rows are tied to the actual surface form and the local semantic movement toward distribution.\",\"representative_source_ids\":[\"QP-33ef62c9\",\"QP-4df38bd7\",\"MP-72d7282d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:dependent-collective-adjective","source_type":"word_analysis","support_id":"sup_b4a49a1e6a2ce459bdf8","text":"{\"blocking_evidence\":null,\"headline\":\"dependent adjective makes one collective field\",\"reader_payoff\":\"The reader sees the word define the carpets' shared condition rather than introduce a separate object.\",\"reason\":\"QAC and attachment evidence identify the word as a nominative feminine singular adjective modifying the nonhuman plural carpet noun.\",\"representative_source_ids\":[\"QG-45d6beff\",\"QG-d4ca3aa8\",\"QF-d424453f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:plural-to-collective-field","source_type":"word_analysis","support_id":"sup_b53beb70277bb597e671","text":"{\"blocking_evidence\":null,\"headline\":\"plural carpets become one field\",\"reader_payoff\":\"The reader sees multiplicity become coverage because many carpets are gathered by one collective spread-state.\",\"reason\":\"The noun is plural and indefinite, while the adjective attaches with nonhuman plural collective agreement.\",\"representative_source_ids\":[\"QG-28a46f7b\",\"QF-fe218186\",\"QF-febdedfe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:variant-reclining-apparatus","source_type":"word_analysis","support_id":"sup_c028e39d6fb5f2260960","text":"{\"blocking_evidence\":null,\"headline\":\"variant makes embedded use explicit\",\"reader_payoff\":\"The reader sees that spread carpets imply usable support and ease, while the canonical wording still closes on the carpets' state.\",\"reason\":\"The variant expansion is useful as apparatus for function and posture, but it does not replace the canonical adjective's object-state focus.\",\"representative_source_ids\":[\"QF-156ed436\",\"QF-1c44d6be\",\"QF-c0aaccea\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:distress-and-creature-spread-echoes","source_type":"word_analysis","support_id":"sup_c0a1ba9dd43f9c8f34ef","text":"{\"blocking_evidence\":null,\"headline\":\"diffusion echoes from 12:86 and 2:164\",\"reader_payoff\":\"The reader notices diffusion moved from expressed distress in 12:86 and creature distribution in 2:164 into hospitable furnishing in 88:16.\",\"reason\":\"The root range supports diffusion and outward spreading, but the local carpet adjective narrows those echoes into spatial hospitality.\",\"representative_source_ids\":[\"QI-2e765fba\",\"QI-869c9170\",\"ME-468e73cd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:variant-collective-surface","source_type":"word_analysis","support_id":"sup_c10e0d87ef6269394fa3","text":"{\"blocking_evidence\":null,\"headline\":\"variant pronoun reinforces collective surface\",\"reader_payoff\":\"The reader sees the plural carpets treated as one support-surface for use, matching the collective agreement in the base phrase.\",\"reason\":\"The variant's pronoun and user participles clarify the same collective surface logic already present in the canonical adjective agreement.\",\"representative_source_ids\":[\"QG-7a0649de\",\"QG-7d831f19\",\"QS-a8990e71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3","source_type":"word_analysis","support_id":"sup_c17dd717888614c22356","text":"{\"gloss_range\":\"feminine singular passive-participle adjective marking the carpets as already spread, distributed, and laid out as one collective furnishing field\",\"prose\":\"{{ar:مَبْثُوثَةٌ}} ({{tr:mabthūthatun}}) closes the inventory by making the carpets not merely present but already spread out. Its nominative adjective role keeps the word dependent on {{ar:زَرَابِىُّ}} ({{tr:zarābiyyu}}), and its feminine singular agreement treats the plural carpets as one collective surface rather than unrelated individual rugs. Shared indefiniteness makes spread-outness the type-quality of the whole carpet field, not a later specification of a known set. The passive participle matters: no finite verb narrates someone spreading them, and no active form pulls attention to an agent; the listener meets provision as a completed result, not as self-dispersal or a cue to analyze causation. The root field of {{ar:ب ث ث}} ({{tr:b-th-th}}) can scatter, diffuse, or disclose outward, but here the furnishing context turns dispersal into ordered hospitality and visible comfort spread across the place. That reversal is sharp beside panicked or fragmenting dispersal in 101:4 and 56:6, and beside expressed distress in 12:86; even the creature-spreading logic of 2:164 is miniaturized into garden furnishing. Because this passive-participle recurrence is limited, the hospitable use stands out as marked rather than as a generic adjective. Variant expansions that mention reclining upon the carpets make explicit what the base phrase leaves embedded: spread placement implies usable support and ease, while the canonical wording still ends on object-state and still treats the plural carpets as one support-surface. After the rowed cushions of 88:15, the final participle moves the eye from linear arrangement to broad coverage, then leaves a completed tableau just before 88:17 demands observation. Its repeated and airy consonantal pressure reinforces the move from gathered object to distributed field, so the final prepared-state cadence joins morphology, sound, and spatial coverage at the catalogue's close.\",\"root_display\":\"{{ar:ب ث ث}} ({{tr:b-th-th}})\",\"root_gloss_range\":\"root range includes physical spreading, scattering, diffusion, and outward disclosure; the local passive participle narrows that dispersal field into prepared carpet coverage\",\"surface_display\":\"{{ar:مَبْثُوثَةٌ}} ({{tr:mabthūthatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:indefinite-condition","source_type":"word_analysis","support_id":"sup_c4d14fa473c049477811","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite condition of the carpet field\",\"reader_payoff\":\"The reader notices spread-outness as the type-quality of the whole carpet field, not a later note about an already identified set.\",\"reason\":\"The adjective shares the indefinite nominative noun phrase and modifies the plural head as a collective state.\",\"representative_source_ids\":[\"QG-5ee8dbf6\",\"QF-7921b9db\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:completed-display-before-looking","source_type":"word_analysis","support_id":"sup_d2ec5e0de1792db58c80","text":"{\"blocking_evidence\":null,\"headline\":\"completed display before the looking question in 88:17\",\"reader_payoff\":\"The reader sees the prepared visual tableau completed before 88:17 commands attention outward.\",\"reason\":\"The final passive participle completes the displayed furnishing scene immediately before 88:17.\",\"representative_source_ids\":[\"QB-19110dec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:dispersal-domesticated","source_type":"word_analysis","support_id":"sup_d31eca037c36b641fd19","text":"{\"blocking_evidence\":null,\"headline\":\"dispersal turned into ordered hospitality\",\"reader_payoff\":\"The reader feels the root's spreading and scattering energy converted into generous spatial coverage.\",\"reason\":\"V4 supports physical spreading and diffusion in the root range, while the local carpet head and garden inventory narrow that field into deliberate furnishing coverage.\",\"representative_source_ids\":[\"QS-1dc648e1\",\"QS-99d6ede4\",\"MS-e2dacbc4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:2:catalogue-culmination","source_type":"word_analysis","support_id":"sup_d578bc84bd7c90e02e61","text":"{\"blocking_evidence\":null,\"headline\":\"ground-covering culmination of the furnishing list\",\"reader_payoff\":\"The reader follows the inventory from discrete supports into a complete inhabited setting whose floor is also prepared.\",\"reason\":\"The word occupies the final furnishing-head position after the preceding inventory items, and attachment evidence keeps the same locative frame active.\",\"representative_source_ids\":[\"QS-03beb1e7\",\"QT-5233c9a1\",\"QY-c7faed47\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:1","source_type":"word_analysis","support_id":"sup_d8a78c4162760377e2dc","text":"{\"gloss_range\":\"coordinating list-particle that carries the final furnishing item within the same compressed garden inventory\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does quiet structural work: it carries the final furnishing noun into the same garden inventory rather than starting a detached sentence. The repeated connector onset for cups, cushions, and carpets makes 88:16 the last audible addition in one furnishing run. The following nominative carpet noun and the recoverable locative frame make additive coordination the local force, while possible resumptive or circumstantial values remain secondary. Because the particle is prefixed in writing but split for analysis, the listener hears a tight pickup into {{ar:زَرَابِىُّ}} ({{tr:zarābiyyu}}): the clipped connector releases into the heavier textile word at the same moment the final object is named. At the boundary, this same list-link keeps the paradise tableau continuous before 88:17 turns outward into a looking question.\",\"root_display\":\"—\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:16:2:1","source_type":"qac_morpheme","support_id":"sup_e3910ce32ec5b9382a41","text":"{\"lemma_ar\":\"مَبْثُوثَة\",\"morph_features\":\"STEM|POS:ADJ|PASS|PCPL|LEM:mabovuwvap|ROOT:bvv|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"88:16:2:1\",\"qac_word_ref\":\"88:16:2\",\"root_ar\":\"ب ث ث\",\"surface_ar\":\"مَبْثُوثَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:1:alternative-values-narrowed","source_type":"word_analysis","support_id":"sup_f408300454515a0774b2","text":"{\"blocking_evidence\":null,\"headline\":\"resumptive and circumstantial values limited\",\"reader_payoff\":\"The reader keeps the particle's range in view while seeing the local noun phrase narrow it to additive list-continuation.\",\"reason\":\"The following nominative furnishing noun and the repeated inventory frame favor coordination; broader particle values are acknowledged but do not control the local parse.\",\"representative_source_ids\":[\"QG-0bb91d6a\",\"QG-a6249cea\",\"QS-87d90db3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:non-reflexive-non-causative-limit","source_type":"word_analysis","support_id":"sup_f849eb1849ba2c0385bb","text":"{\"blocking_evidence\":null,\"headline\":\"self-dispersal and causation kept out\",\"reader_payoff\":\"The reader understands the carpets as objects of prior placement, not as things dispersing themselves or as a cue to analyze the spreading agent.\",\"reason\":\"The passive participle supports result-state; broader causative or reflexive possibilities are not selected by the local surface.\",\"representative_source_ids\":[\"QF-6c283ccc\",\"QF-e57e4554\",\"MF-8208bcdc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:16:3:rare-marked-form","source_type":"word_analysis","support_id":"sup_fe6f23e0898a8283888a","text":"{\"blocking_evidence\":null,\"headline\":\"limited passive-participle recurrence\",\"reader_payoff\":\"The reader treats the adjective as marked because its limited recurrence makes the hospitable usage stand out.\",\"reason\":\"The contextual profile marks the exact root-form group as low occurrence, and the CRITICAL rows tie that rarity to the local reversal of dispersal.\",\"representative_source_ids\":[\"QI-4148e6af\",\"QH-44c89dda\",\"QH-f40ee799\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000083/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000083","role":"Physical scattering and laying out supply the focus's completed areal-distribution mechanism.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"Many carpets have been deliberately distributed into an accessible field that extends comfort across the surface.","before":"A set of carpets simply lies in the scene."},"confidence":"strong","focus_anchor":"Word 2 is a passive adjective from ب ث ث modifying the plural carpets.","mechanism":"The physical branch presents separation and spreading as a completed result. The carpets are not one floor covering but a multiplicity distributed across an area, making the surface broadly available.","model_id":"baseline_areal_distribution"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_areal_distribution","source_type":"hft","support_id":"sup_59a386babb4f3cd37cff","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000083/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000083","role":"Disclosure of concealed inward content turns the visible spread into a material showing of otherwise hidden welcome.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"The carpets make an inward condition of welcome and ease visible throughout the environment.","before":"The carpets are decorative objects."},"confidence":"medium","focus_anchor":"The adjective at word 2 can activate the inward-disclosure branch of ب ث ث while still describing the visible carpets.","mechanism":"A branch normally used for bringing concealed feeling or news outward lets the material arrangement function as exteriorized interiority. What would remain inward as welcome, ease, or generosity becomes publicly legible in the spread furnishings.","model_id":"baseline_disclosed_interior"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_disclosed_interior","source_type":"hft","support_id":"sup_0727bd5e706fb64231ea","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000083/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000083","role":"Investigating and exposing a matter supplies the exploratory sense of a scene opened out for inspection.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"The eye encounters a layout opened out so that its order and contents can be examined.","before":"The eye encounters a finished decorative surface."},"confidence":"exploratory","focus_anchor":"Word 2 remains the anchor, through the investigative and exposing branch of ب ث ث.","mechanism":"The branch is form-distant because it is associated with an extended reduplicated use, but it keeps the core motion of opening a matter out. The laid carpets can therefore be carried as an inspectable layout, a scene whose contents have been exposed rather than merely ornamented.","model_id":"baseline_inspectable_layout"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inspectable_layout","source_type":"hft","support_id":"sup_234d2dc528ca35284ccd","trust":"legacy_unbound"}]}
</lane_packet_json>
