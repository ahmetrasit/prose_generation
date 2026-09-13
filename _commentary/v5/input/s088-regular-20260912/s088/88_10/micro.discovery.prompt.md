# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:10**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_10/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:10",
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
{"branch_registry":[{"boundary":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B001","candidate_links":[{"candidate_id":"cand_ec76527ea9d12c6a4987","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"örtme ve duyulardan gizleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin örtülmesini, bir kişinin saklanmasını veya örtü işlevli bir şeyi birlikte temsil eden en geniş karşılıktır.","boundary_detail":"Dal yalnızca örtme ve gizlenme alanındadır; akıl yitimi, bahçe ve görünmeyen varlık anlamlarını içermez.","branch_image_ar":"الستر والاستتار","concept_gloss":"örtme ve duyulardan gizleme","contextual_glosses":[{"applicability":"Bir öznenin nesneyi görünmez veya algılanamaz duruma getirdiği geçişli kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geçişli örtme eylemini ve bunun doğurduğu gizlenme sonucunu eksiksiz korur."},"facet_ids":["F001"],"text":"örtüp gizlemek","usage_role":"contextual"},{"applicability":"Kişinin bir örtü veya engel aracılığıyla kendini duyulardan sakladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örtü aracını ve öznenin kendisini algıdan saklaması anlamını birlikte korur."},"facet_ids":["F002"],"text":"bir şeyin arkasına gizlenmek","usage_role":"contextual"}],"definition":"Bir şeyi duyuların erişiminden çıkaracak biçimde örtmek ya da gizlemek; kişinin bir şeyin arkasına saklanması, bir şeyi içinde saklaması ve insanı örten giysi bu çekirdeğin gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey örtülerek ya da gizlenerek duyuların erişiminden çıkarılır."},{"facet_id":"F002","role":"extension","statement":"Bir örtünün arkasına saklanma, bir şeyi içinde saklama ve insanı örten giysi aynı gizleme çekirdeğine dayanır."}],"identity_rationale":"Kaynak ifadesi dalı örtme, duyulardan gizleme ve bir örtünün arkasına saklanma çekirdeğinde kurar; içte saklama ile insanı örten giysi de bu çekirdeğin açık gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"örtmek; gizleyecek bir örtü sağlamak; içinde saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyin arkasına gizlenmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insanı örten giysi veya örtü"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallara ya da yalnızca belirli bir söz öbeğine bağlı anlamları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırmasını genel örtme dalı sağladığı için yalnızca bu ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu sonucu duyusal erişimden gizlenmedir; komşu dal ise genel örtme ve kaplama alanını daha geniş biçimde adlandırır.","focus_only":"Odak dal, duyulardan saklanmayı, içte gizlemeyi ve insanı örten giysiyi aynı çekirdekte toplar.","gloss":"örtme ve gizleme","neighbor_only":"Komşu dal, örtü ve örtme araçlarının genel söz varlığını daha doğrudan kapsar.","neighbor_ref":"root_000674/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi örtme ve böylece görünmesini engelleme alanında buluşur."}],"source_phrase_ar":"الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)","source_summary":"Kaynakların ortak ekseni, bir şeyi duyusal algıdan örterek gizlemek ve bu örtünün sağladığı saklılık durumudur.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ستر الشيء عن الحس والاستتار بشيء وإكنان الشيء في الصدر وما يواري من ثوب أو غيره","what_is_not_ar":"ليس الجنون ولا الجنة ولا الجن"},"support_links":["sup_9698ebdaa2dd3e82a738"]},{"boundary":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_kind":"bare","branch_ref":"root_000266/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"gecenin karartıp örtmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gece karanlığının bir kişi, yer veya nesneyi kaplayıp görünmez kıldığı bütün yalın kullanımlara uygundur.","boundary_detail":"Sırf gece, sırf karanlık veya güneşin batması yeterli değildir; karanlığın bir şeyi örtmesi kurucudur.","branch_image_ar":"غشيان الليل","concept_gloss":"gecenin karartıp örtmesi","contextual_glosses":[{"applicability":"Bir yerin veya nesnenin gece bastığında karanlık içinde görünmez hale geldiği anlatımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gecenin bastırmasını ve nesnenin karanlıkla örtülmesini birlikte korur."},"facet_ids":["F001"],"text":"gece karanlığına gömülmek","usage_role":"contextual"}],"definition":"Gecenin kararması ve bir şeyi kendi karanlığıyla örterek görünmez kılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gece kararır ve karanlığı bir şeyin üzerini örter."}],"identity_rationale":"Kaynak ifadesi yalnızca gecenin kararıp bir şeyi karanlığıyla örtmesini bildirir; dalın gece karanlığı ile örtme işlemini birlikte tutan çerçevesi buna uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"gecenin kararıp üzerini örtmesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"gecenin koyu karanlığı ve nesneleri örtmesi"}],"lexicalization_note":"Tanım yalın dalı verir; başka gece sözlerine veya insan topluluğu ve iç dünya anlamlarına genişletilmez.","neighbor_coverage_note":"Bütün gece, ışık ve aynı kökten gelen dal adayları değerlendirildi; örtme koşulunu en iyi sınayan kararma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu için kararma yeterliyken odak dalda karanlığın bir kişi, yer veya nesneyi örtmesi anlamın kurucu parçasıdır.","focus_only":"Odak dalda gece karanlığı yalnızca artmaz, aynı zamanda bir şeyin üzerini örter.","gloss":"gecenin kararması","neighbor_only":"Komşu dal gecenin karanlık hale gelmesini örtülen bir nesne şartı olmadan kapsar.","neighbor_ref":"root_001094/B001","relation_type":"near_synonym","shared_zone":"İki dal da gecenin karanlıklaşması ve yoğun karanlık alanında örtüşür."}],"source_phrase_ar":"جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)","source_summary":"Kaynaklar gecenin kararmasını, bu karanlığın nesneleri örtüp görünmez kılmasıyla birlikte anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الليل على الشيء إذا أظلم وستره بسواده","what_is_not_ar":"ليس سواد الناس ولا الجنان بمعنى القلب"},"support_links":[]},{"boundary":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_kind":"bare","branch_ref":"root_000266/B003","candidate_links":[{"candidate_id":"cand_968ccc94923129f4bf92","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"zemini ağaçlarla örtülü bahçe","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaçların veya hurmalıkların yoğunluğu sayesinde zemini örtülen bahçe ve koruluklar için tam karşılıktır.","boundary_detail":"Her çevrili alan veya her ekili toprak bu dala girmez; ağaçlı bahçe ve ağaçların örttüğü zemin esastır.","branch_image_ar":"البستان المستور بالشجر","concept_gloss":"zemini ağaçlarla örtülü bahçe","contextual_glosses":[{"applicability":"Bağlam zeminin ağaçlarla örtülü olduğunu zaten gösterdiğinde doğal ve kısa bir çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaçlarla kaplı bahçe referansını bağlam desteğiyle eksiksiz korur."},"facet_ids":["F001"],"text":"ağaçlık bahçe","usage_role":"contextual"}],"definition":"Ağaçları, özellikle de sık ağaç veya hurmalıkları zemini örten bahçe ya da koruluk niteliğindeki yerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ağaçlı bahçenin zemini ağaçların oluşturduğu örtü altında kalır."}],"identity_rationale":"Kaynak ifadesi bahçeyi ağaçları veya hurmalıkları toprağı örten ağaçlı bir yer olarak tanımlar; dalın ağaç örtüsünü merkeze alan çerçevesi kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"zemini ağaçlarla örtülü bahçe veya koruluk"}],"lexicalization_note":"Tanım yalın ağaçlı bahçe anlamını taşır ve ölüm sonrası ödül yurdu ya da genel bitki örtüsü anlamını içeri almaz.","neighbor_coverage_note":"Bütün bahçe, hurmalık, bitki ve aynı kökten dal adayları değerlendirildi; dış sınır ile ağaç örtüsü karşıtlığı en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta içteki ağaç örtüsü, komşuda ise alanı dıştan kuşatan sınır belirleyicidir; bu yüzden sıradan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bahçeyi ağaçların zemini örtmesiyle tanımlar.","gloss":"ağaç örtülü ve çevrili bahçe","neighbor_only":"Komşu dal bahçeyi çevresindeki duvar, engel veya yükseltiyle tanımlar.","neighbor_ref":"root_000300/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağaç veya bitki içeren sınırlı bir bahçe alanına gönderimde bulunabilir."}],"source_phrase_ar":"الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)","source_summary":"Kaynaklar anlamı bahçe, ağaçlı bahçe ve hurmalık çevresinde birleştirir; ayırt edici özellik ağaçların zemini örtmesidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الجنة بمعنى البستان والحديقة ذات الشجر والنخل الساتر","what_is_not_ar":"ليس الجنة الأخروية ولا الجنون"},"support_links":["sup_60b3b1d27e1f81999199"]},{"boundary":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_kind":"bare","branch_ref":"root_000266/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"ölüm sonrası gizli nimetler yurdu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Müslümanların ölümden sonra ulaşacağı ödül yurdundan ve henüz görünmeyen nimetlerinden söz edilen bağlamlara uygundur.","boundary_detail":"Dal ölüm sonrası ödül yurduyla sınırlıdır; dünyadaki ağaçlı bahçe veya görünmeyen varlıklar topluluğu değildir.","branch_image_ar":"الجنة الأخروية","concept_gloss":"ölüm sonrası gizli nimetler yurdu","contextual_glosses":[{"applicability":"Nimetlerin henüz görünmediği bilgisi bağlamdan anlaşıldığında akıcı bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüm sonrası varış yerini ve ödül olma niteliğini bağlam desteğiyle korur."},"facet_ids":["F001"],"text":"ölüm sonrası ödül yurdu","usage_role":"contextual"}],"definition":"Müslümanların ölümden sonra ulaşacağı, ödülü ve nimetleri bugün onlardan gizli olan yurttur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Müslümanların ölümden sonra varacağı ödül yurdunun nimetleri bugün kendilerinden gizlidir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırma ya dünyadaki ağaçlı bahçeye benzetilmekte ya da nimetlerin şimdilik gizli oluşuyla açıklanmaktadır."}],"identity_rationale":"Kaynak ifadesi Müslümanların ölümden sonra ulaşacağı ödül yurdunu ve bugün onlardan gizli olan nimetlerini bildirir; dünyevi bahçe benzetmesi yalnızca adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ölüm sonrası ödül ve gizli nimetler yurdu"}],"lexicalization_note":"Tanım yalın ölüm sonrası ödül yurdu anlamını korur ve dünyadaki bahçe anlamını bu dala katmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dış adaylar bitki adlarıyla sınırlı kaldığından en açıklayıcı karşılaştırma aynı kökün dünyevi bahçe dalıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Biri ölüm sonrası ve inanç alanına ait bir varış yeridir, diğeri dünyadaki ağaçlı bir alandır; benzetme referansları özdeş kılmaz.","focus_only":"Odak dal ölüm sonrası ulaşılan ödül yurdunu ve bugün gizli olan nimetleri bildirir.","gloss":"ödül yurdu ve ağaçlı bahçe","neighbor_only":"Komşu dal dünyadaki, zemini ağaçlarla örtülü somut bir bahçeyi bildirir.","neighbor_ref":"root_000266/B003","relation_type":"near_neighbor","shared_zone":"Adlandırma, ödül yurdunu ağaçlı bahçe imgesiyle ilişkilendirebilir."}],"source_phrase_ar":"الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)","source_summary":"Kaynaklar ölüm sonrası ödül yurdunda birleşir; adın gerekçesini ağaçlı bahçe benzetmesi veya nimetlerin bugün gizli olmasıyla açıklar.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه الجنة التي يصير إليها المسلمون وثوابها المستور عنهم","what_is_not_ar":"ليس البستان الدنيوي ولا جماعة الجن"},"support_links":[]},{"boundary":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000266/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"gözle görülmeyen ruhani varlıklar topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın biçimlerin gizli ruhani varlık türünü veya bu türün topluluğunu bildirdiği genel bağlamlara uygundur.","boundary_detail":"Yılan adı ve akıl yitimi bu dalın dışında kalır; yer anlamı yalnızca çokluk bildiren belirli söz öbeğine bağlıdır.","branch_image_ar":"الجن المستترون","concept_gloss":"gözle görülmeyen ruhani varlıklar topluluğu","contextual_glosses":[{"applicability":"Söz konusu türün tek bir bireyi veya atası anlatıldığında tekil bağlama uyar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birey olmayı, ruhani niteliği ve insan duyularından gizli oluşu korur."},"facet_ids":["F001","F002"],"text":"görünmeyen ruhani varlık","usage_role":"contextual"},{"applicability":"Yalnızca kanıtta verilen yer söz öbeğinin çokluk bildiren bağımlı kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer referansını, varlıkların çokluğunu ve kullanımın söz öbeğine bağlılığını korur."},"facet_ids":["F003"],"text":"görünmeyen varlıkların çok bulunduğu yer","usage_role":"explanatory"}],"definition":"İnsanların duyularından gizli kabul edilen ruhani varlıklar ve onların topluluğudur. Bu varlıklardan çok bulunan yer anlamı yalnızca ilgili yer söz öbeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ruhani varlıklar insan gözünden ve duyularından gizlidir; ad hem türü hem topluluğunu karşılayabilir."},{"facet_id":"F002","role":"specialization","statement":"Tekil biçim bu varlıkların atasını veya bir bireyini, başka biçimler ise topluluğunu bildirir."},{"facet_id":"F003","role":"extension","statement":"Bu varlıkların çok bulunduğu yer anlamı yalın değildir ve belirli bir yer söz öbeğiyle sınırlıdır."}],"identity_rationale":"Kaynak ifadesi insan gözünden gizli ruhani varlıkları, onların tekil ve topluluk adlarını ve bu varlıkların çok bulunduğu yer için kullanılan bağımlı söz öbeğini birlikte verir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gözle görülmeyen ruhani varlıklar"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"görünmeyen varlıkların atası veya bir bireyi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların topluluğu"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"görünmeyen ruhani varlıkların çok bulunduğu yer"}],"lexicalization_note":"Yalın varlık ve topluluk anlamları, bu varlıkların çok bulunduğu yeri bildiren söz öbeğine bağlı kullanımdan ayrı tutulur.","neighbor_coverage_note":"Bütün varlık, canlı, yer ve aynı kökten adaylar değerlendirildi; genel tür ile ayrı alt topluluk arasındaki sınır en yararlı ayrımdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel tür ve topluluk adıdır; komşu ise aynı alandaki ayrı bir sınıf veya ona bağlı varlıkları bildirir, bu yüzden ikame edilemez.","focus_only":"Odak dal görünmeyen ruhani varlık türünün genel adını, bireyini ve topluluğunu kapsar.","gloss":"görünmeyen varlıklar ve bir alt topluluk","neighbor_only":"Komşu dal bu alandaki ayrı bir topluluğu, alt türü veya onlara bağlanan köpekleri bildirir.","neighbor_ref":"root_000364/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal insan gözünden gizli kabul edilen ruhani varlıklar alanındadır."}],"source_phrase_ar":"الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)","source_summary":"Kaynaklar insan duyularından gizli ruhani varlıklar çekirdeğinde birleşir; birey, ata, topluluk ve çok bulundukları yer için ayrı biçimler verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجن والجان والجنة جماعة الجن والموضع الكثير الجن","what_is_not_ar":"ليس الجان بمعنى الحية ولا الجنة بمعنى الجنون"},"support_links":[]},{"boundary":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_kind":"bare","branch_ref":"root_000266/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"aklı örten akıl yitimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin akıl işleyişini kaybettiği veya aklı ile benliği arasına engel girdiği genel durumlara uygundur.","boundary_detail":"Dal gerçek ya da gösterilen akıl yitimiyle sınırlıdır; görünmeyen varlıklar ve ağaçlı bahçe anlamları dışarıda kalır.","branch_image_ar":"ستر العقل بالجنون","concept_gloss":"aklı örten akıl yitimi","contextual_glosses":[{"applicability":"Kişinin gerçek bir akıl yitimi durumuna girdiği geçişsiz kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin akıl işleyişini kaybetmesini ve durum değişimini korur."},"facet_ids":["F001","F002"],"text":"aklını yitirmek","usage_role":"contextual"},{"applicability":"Kişinin gerçek durumu değil, bu durumun görünüşünü isteyerek sergilediği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akıl yitimini gerçek yaşamadan onun görünüşünü sergileme ayrımını korur."},"facet_ids":["F003"],"text":"aklını yitirmiş gibi davranmak","usage_role":"contextual"}],"definition":"Aklın işleyişini örten veya benlik ile akıl arasına engel koyan akıl yitimi durumudur; kişi bu duruma düşebilir, düşürülebilir ya da böyleymiş gibi davranabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl yitimi, aklın örtülmesi veya benlik ile akıl arasına engel girmesi olarak kavranır."},{"facet_id":"F002","role":"extension","statement":"Kişinin aklını yitirmesi ile bir etkenin onu bu duruma getirmesi katılımcıları farklı iki süreçtir."},{"facet_id":"F003","role":"associated_use","statement":"Gerçek durumdan ayrı olarak kişi kendisini aklını yitirmiş gibi gösterebilir."}],"identity_rationale":"Kaynak ifadesi aklın örtülmesini, benlik ile akıl arasına engel girmesini, kişinin bu duruma düşmesini veya düşürülmesini bildirir; görünüşte bu hali takınma da ayrı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"aklını yitirmek; aklını yitirmiş duruma getirmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"akıl yitimi; benlik ile akıl arasındaki engel"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aklını yitirmiş gibi davranmak"}],"lexicalization_note":"Tanım yalın akıl yitimi dalını kapsar ve başka dalların varlık ya da yer anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün akıl, karar, görünmeyen etki ve aynı kökten adaylar değerlendirildi; kapsamı en çok çakışan bozulma dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtülme temelli akıl yitimini ve onun dilbilgisel süreçlerini öne çıkarır; komşu ise neden ve bozulma türleri bakımından daha geniştir.","focus_only":"Odak dal akıl yitimini örtülme veya benlik ile akıl arasına giren engel olarak kurar ve bu görünüşü takınmayı da kapsar.","gloss":"akıl işleyişinin bozulması","neighbor_only":"Komşu dal akıl ve yürek bozulmasını hastalık, dokunma, sevgi veya başka etkenlerle daha geniş biçimde ilişkilendirir.","neighbor_ref":"root_000390/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da aklın sağlıklı işleyişini yitirmesi alanında önemli ölçüde örtüşür."}],"source_phrase_ar":"الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)","source_summary":"Kaynaklar akıl işleyişinin örtülmesi ve kişinin aklını yitirmesi çekirdeğinde birleşir; ettirgen süreç ile görünüşte bu hali takınmayı da kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنون والجنة والمجنة والجنن ومجنون وتجانن إذا تعلق المعنى بزوال العقل أو إظهاره","what_is_not_ar":"ليس الجن ولا الجنة البستان"},"support_links":[]},{"boundary":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"ana rahmindeki doğmamış çocuk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çocuğun doğumdan önce annesinin karnında veya rahminde bulunduğu bütün yalın bağlamlara uygundur.","boundary_detail":"Dal rahimdeki çocuk ve onun saklı bulunduğu dönemle sınırlıdır; gömülmüş kişi veya gömüt anlamına gelmez.","branch_image_ar":"الجنين المستور في البطن","concept_gloss":"ana rahmindeki doğmamış çocuk","contextual_glosses":[{"applicability":"Annenin doğmamış çocuğu karnında taşıdığı süreç özne üzerinden anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Annenin taşıyan katılımcı, çocuğun da rahimde saklı katılımcı oluşunu korur."},"facet_ids":["F002"],"text":"rahminde çocuk taşımak","usage_role":"contextual"}],"definition":"Doğmamış çocuk, annesinin karnında veya rahminde kaldığı süre boyunca bu dalın referansıdır; annenin onu taşıması ve çocuğun rahimde saklı kalması buna bağlı süreçlerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çocuk, annesinin karnında veya rahminde bulunduğu süre boyunca doğmamış durumdadır."},{"facet_id":"F002","role":"associated_use","statement":"Annenin doğmamış çocuğu taşıması ile çocuğun rahimde saklı bulunması katılımcıları farklı bağlantılı süreçlerdir."}],"identity_rationale":"Kaynaklar çocuğu annesinin karnında veya rahminde kaldığı süre boyunca tanımlar ve annenin bu çocuğu taşımasıyla çocuğun rahimde saklı kalmasını ayrı süreçler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ana rahmindeki doğmamış çocuk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"rahminde çocuk taşımak; çocuğun rahimde saklı kalması"}],"lexicalization_note":"Tanım yalın rahimdeki çocuk anlamını korur; gebelik, doğum veya gömme alanının tamamına genişletilmez.","neighbor_coverage_note":"Bütün rahim, gebelik, doğum ve aynı kökten adaylar değerlendirildi; çocuk ile gebelik durumu ayrımı en açıklayıcı sınırı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği rahimdeki çocuktur; komşu dalın çekirdeği ise annenin taşıma durumu ve bunun süresidir.","focus_only":"Odak dal anne rahminde bulunan doğmamış çocuğu referans alır.","gloss":"doğmamış çocuk ve gebelik","neighbor_only":"Komşu dal annenin gebelik durumunu, süresini ve karındaki yükü daha geniş biçimde kapsar.","neighbor_ref":"root_000291/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da annenin karnındaki çocuk ve doğum öncesi dönem alanındadır."}],"source_phrase_ar":"الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)","source_summary":"Kaynaklar rahimde veya anne karnında bulunan doğmamış çocuk tanımında birleşir; taşıma ve rahimde saklı kalma süreçlerini de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنين والولد ما دام في بطن أمه وأجنة البطون","what_is_not_ar":"ليس المقبور ولا القبر"},"support_links":[]},{"boundary":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_kind":"bare","branch_ref":"root_000266/B008","candidate_links":[{"candidate_id":"cand_ec76527ea9d12c6a4987","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"koruyucu siper veya savaş donanımı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalkan, zırh ya da kişinin arkasına sığınıp kendini koruduğu başka bir savaş örtüsü için uygundur.","boundary_detail":"Dal koruyucu siper veya savaş donanımıyla sınırlıdır; bahçe, akıl yitimi ve sıradan örtü anlamlarına genişlemez.","branch_image_ar":"الجُنّة الواقية","concept_gloss":"koruyucu siper veya savaş donanımı","contextual_glosses":[{"applicability":"Kaynak biçim özellikle elde taşınan koruyucu savaş aracını gösterdiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elde taşınan siper aracını ve sahibini koruma işlevini tam olarak korur."},"facet_ids":["F001","F002"],"text":"kalkan","usage_role":"contextual"}],"definition":"Kişinin tehlikeden korunmak için arkasına sığındığı veya üzerine aldığı koruyucu örtü ya da savaş donanımıdır; kalkan ve zırh bunun başlıca türleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir örtü veya savaş donanımı kişiyi tehlikeden koruyan siper işlevi görür."},{"facet_id":"F002","role":"specialization","statement":"Kalkan ve zırh, koruyucu siper çekirdeğinin açık araç türleridir."}],"identity_rationale":"Kaynak ifadesi korunmak için arkasına sığınılan silah veya örtüyü genel çekirdek, kalkanı ve zırhı ise belirgin gerçekleşmeler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"koruyucu örtü, siper veya savaş donanımı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kalkan"}],"lexicalization_note":"Tanım yalın koruyucu örtü ve silah anlamını kapsar; yalnızca belirli bir savaş söz öbeğine bağlanmaz.","neighbor_coverage_note":"Bütün kalkan, zırh, hazırlık, korunma ve aynı kökten adaylar değerlendirildi; giyilebilir zırh ile genel siper ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kalkan gibi giyilmeyen siperleri de kapsar; komşu ise giyilebilir zırh ve korunma giysisine daha sıkı bağlıdır.","focus_only":"Odak dal kalkanı ve korunmak için arkasına sığınılan her türlü savaş örtüsünü kapsar.","gloss":"koruyucu savaş donanımı","neighbor_only":"Komşu dal özellikle savaşta giyilen zırhı ve giyilebilir koruyucu donanımı öne çıkarır.","neighbor_ref":"root_001341/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da savaşta bedeni saldırıdan koruyan araç ve donanımları bildirir."}],"source_phrase_ar":"المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)","source_summary":"Kaynaklar korunmak için kullanılan örtü veya silah çekirdeğinde birleşir ve özellikle kalkan ile zırhı bu kapsamda anar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنة التي يتقى بها والمجن الترس والسلاح وما وقاك","what_is_not_ar":"ليس الجنة البستان ولا الجنون"},"support_links":["sup_9698ebdaa2dd3e82a738"]},{"boundary":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_kind":"bare","branch_ref":"root_000266/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"ölüyü örtüp gömme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölünün gözden kaldırılarak toprağa verilmesini ve bu işlemin örtme yönünü birlikte anlatan bağlamlara uygundur.","boundary_detail":"Dal ölü ve gömme alanındadır; anne rahmindeki doğmamış çocuk anlamıyla yalnızca biçim benzerliği paylaşır.","branch_image_ar":"مواراة الميت","concept_gloss":"ölüyü örtüp gömme","contextual_glosses":[{"applicability":"Örtme ayrıntısının gömme eyleminden doğal olarak anlaşıldığı akıcı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölü katılımcısını ve gömerek gözden kaldırma işlemini bağlam içinde korur."},"facet_ids":["F001"],"text":"ölüyü toprağa vermek","usage_role":"contextual"}],"definition":"Ölüyü örterek gözden kaldırmak ve toprağa gömmektir; gömüt, ölü örtüsü ve gömülmüş kişi bu işlemin yer, araç ve sonuç odaklı adlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölü örtülerek gözden kaldırılır ve toprağa gömülür."},{"facet_id":"F002","role":"extension","statement":"Gömüt, ölü örtüsü ve gömülmüş kişi aynı işlemin sırasıyla yer, araç ve sonuç katılımcılarını adlandırır."}],"identity_rationale":"Kaynak ifadesi ölüyü örterek gözden kaldırma ve gömme eylemini, gömütü, ölü örtüsünü ve gömülmüş kişiyi aynı dalda açıkça kaydeder.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ölüyü örtmek ve gömmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömüt; ölü örtüsü; gömülmüş kişi"}],"lexicalization_note":"Tanım yalın gömme ve ölü örtme dalını kapsar; genel çukur açma veya doğmamış çocuk anlamına genişletilmez.","neighbor_coverage_note":"Bütün gömme, gömüt, örtme ve aynı kökten adaylar değerlendirildi; genel gömüt dalı en yakın fakat kapsamı farklı komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak örtüp gözden kaldırma çekirdeği ile ölü örtüsü sonucunu korur; komşu ise gömüt kurumu ve gömme izni gibi daha geniş işlemleri kapsar.","focus_only":"Odak dal gömmenin yanında ölü örtüsünü ve gömülmüş kişi yorumunu da aynı biçim alanında taşır.","gloss":"ölüyü gömme","neighbor_only":"Komşu dal gömüt yerini, gömme eylemini, gömüt hazırlamayı ve gömülmeye izin vermeyi daha geniş biçimde kapsar.","neighbor_ref":"root_001195/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ölünün gömüte yerleştirilerek toprağa verilmesi alanında örtüşür."}],"source_phrase_ar":"الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)","source_summary":"Kaynaklar ölüyü örtüp gömme eyleminde birleşir; aynı biçim alanında gömüt, ölü örtüsü ve gömülmüş kişi yorumlarını da verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جن الميت وأجنه إذا واراه والجنن القبر والكفن والجنين بمعنى المقبور أو القبر","what_is_not_ar":"ليس الجنين في الرحم"},"support_links":[]},{"boundary":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_000266/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"duyulardan saklı yürek ve gizli yön","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bedende saklı yüreği hem de bir işin görünmeyen iç yönünü kapsaması gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal içte saklı yürek ve gizli yönle sınırlıdır; gece karanlığı veya insan topluluğu anlamlarını içermez.","branch_image_ar":"الجنان المستور في الصدر","concept_gloss":"duyulardan saklı yürek ve gizli yön","contextual_glosses":[{"applicability":"Bedendeki iç organ veya korkunun yerleştiği iç merkez anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedende saklı iç organı ve duygusal iç merkez işlevini korur."},"facet_ids":["F001"],"text":"yürek","usage_role":"contextual"},{"applicability":"Somut organ değil, bir olayın görünmeyen veya saklı tarafı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyut iş referansını ve onun görünmeyen iç tarafını eksiksiz korur."},"facet_ids":["F002"],"text":"işin gizli yönü","usage_role":"contextual"}],"definition":"Duyulardan saklı olduğu için yürek veya yüreğin iç yönü; buradan hareketle bir işin gizli, görünmeyen yanı anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yürek ve onun korkuyla sarsılan iç yönü bedende duyulardan saklıdır."},{"facet_id":"F002","role":"extension","statement":"Bir işin gizli veya görünmeyen yanı, içte saklı olma özelliğinden türeyen soyut kullanımdır."}],"identity_rationale":"Kaynak ifadesi duyulardan saklı iç organı ve onun korkuyla sarsılan iç yönünü, ayrıca gizli iş veya görünmeyen yön kullanımını açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yürek veya yüreğin saklı iç yönü"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"gizli iş veya görünmeyen yön"}],"lexicalization_note":"Tanım yalın içte saklı yürek ve gizli yön anlamlarını kapsar; başka söz öbeklerinden anlam aktarmaz.","neighbor_coverage_note":"Bütün göğüs, yürek, gizli iş ve aynı kökten adaylar değerlendirildi; iç organ ile içte saklama eylemi ayrımı en yararlı karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir iç organı veya gizli yönü adlandırır; komşu ise bir içeriği zihinde saklama eylemini kurar, bu nedenle çekirdekleri farklıdır.","focus_only":"Odak dal öncelikle duyulardan saklı yüreği adlandırır ve gizli iş anlamına uzanır.","gloss":"yürek ve içte saklama","neighbor_only":"Komşu dal bilgi, düşünce veya sırrın kişinin iç dünyasında saklanması eylemini bildirir.","neighbor_ref":"root_001324/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin iç dünyası ve duyulardan saklı içerik alanında buluşur."}],"source_phrase_ar":"الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)","source_summary":"Kaynaklar duyulardan saklı yürek anlamında birleşir; bir kaynak aynı biçimi gizli iş ve görünmeyen yön için de kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنان بمعنى القلب أو روع القلب والأمر الخفي المستور","what_is_not_ar":"ليس جنان الليل ولا جنان الناس"},"support_links":[]},{"boundary":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_kind":"bare","branch_ref":"root_000266/B011","candidate_links":[{"candidate_id":"cand_831c1c10c985a90aeebb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"bitkinin güçlenip boylanması ve sıklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin gelişerek uzadığı, yoğunlaştığı, birbirine dolaştığı veya çiçek açtığı genel bağlamlara uygundur.","boundary_detail":"Dal bitki gelişimi ve yoğunluğuyla sınırlıdır; böcek sesi veya sırf ağaçlı bahçe adı bu çekirdeğe girmez.","branch_image_ar":"التفاف النبات واندفاعه","concept_gloss":"bitkinin güçlenip boylanması ve sıklaşması","contextual_glosses":[{"applicability":"Bahçe, vadi veya ufuk gibi bir alanın yoğun bitki örtüsüyle kaplandığı bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alan katılımcısını ve bitki örtüsünün yoğunlaşıp alanı kaplaması sonucunu korur."},"facet_ids":["F001","F002"],"text":"bitkiyle dolup sıklaşmak","usage_role":"contextual"}],"definition":"Bitkinin güçlenmesi, boy atması, sıklaşıp birbirine dolaşması veya çiçek açmasıdır; uzun ağaç ve bol, otlanmamış bitki örtüsü bu gelişimin sonuç odaklı görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitki güçlenir, boy atar, sıklaşıp dolaşır veya çiçek açarak gelişimini belirginleştirir."},{"facet_id":"F002","role":"extension","statement":"Uzun ağaç ile yoğun ve bol otlu arazi, bitkisel gelişimin sonuç veya alan odaklı uzantılarıdır."},{"facet_id":"F003","role":"specialization","statement":"Bol otlu arazi kullanımında bitki örtüsünün henüz otlanmamış olması ayrıca belirtilir."}],"identity_rationale":"Kaynak ifadesi bitkinin güçlenme, boy atma, sıklaşıp birbirine dolaşma veya çiçek açma gelişimini; uzun ağaç ve bol otlu arazi sonuçlarını da buna bağlı biçimde verir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"uzun ağaç; bol otlu ve henüz otlanmamış arazi"}],"lexicalization_note":"Tanım yalın bitki gelişimi dalını korur ve böcek sesine bağlı kullanımı ya da başka dalların yer adlarını içeri almaz.","neighbor_coverage_note":"Bütün yoğun bitki, bahçe, ot ve aynı kökten adaylar değerlendirildi; gelişim süreci ile dolaşık düzen arasındaki sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak gelişimin birden çok aşamasını ve sonucunu kapsar; komşunun çekirdeği ise bitkilerin birbirine dolaşmış düzenidir.","focus_only":"Odak dal bitkinin güçlenmesini, boy atmasını ve çiçek açmasını sıklaşmanın yanında kapsar.","gloss":"bitkinin sıklaşıp dolaşması","neighbor_only":"Komşu dal bitki veya ağaçların özellikle birbirine dolaşmış, kat kat kıvrılmış düzenini öne çıkarır.","neighbor_ref":"root_001365/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yoğunlaşan bitkilerin birbirine girip sık bir örtü oluşturması alanında örtüşür."}],"source_phrase_ar":"جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)","source_summary":"Kaynaklar bitkinin güçlenmesi, uzaması, sıklaşması ve çiçeklenmesi çevresinde birleşir; uzun ağaç ile bol ve otlanmamış araziyi sonuç olarak ekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النبات إذا اشتد أو طال أو التف أو خرج زهره والنخل الطويل والأرض الكثيرة العشب","what_is_not_ar":"ليس الذباب إذا حمل على الصوت"},"support_links":["sup_f3f9cb1403b2445d7df4"]},{"boundary":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_kind":"bare","branch_ref":"root_000266/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"yılan, özellikle beyaz bir tür","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Biçimin genel bir yılanı, beyaz yılanı veya belirli bir yılan türünü adlandırdığı bağlamlara uygundur.","boundary_detail":"Dal yılan referansıyla sınırlıdır; görünmeyen ruhani varlığın atası veya bireyi anlamını içermez.","branch_image_ar":"الجان حية","concept_gloss":"yılan, özellikle beyaz bir tür","contextual_glosses":[{"applicability":"Kaynağın veya bağlamın yılanın beyaz olduğunu açıkça belirttiği kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yılan türünü ve bağlamda açıkça verilen beyazlık niteliğini korur."},"facet_ids":["F001"],"text":"beyaz yılan","usage_role":"contextual"}],"definition":"Yılanı, özellikle beyaz bir yılanı veya belirli bir yılan türünü adlandıran kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans bir yılan, kimi kaynaklarda özellikle beyaz yılan veya belirli bir yılan türüdür."},{"facet_id":"F002","role":"source_variant","statement":"Görünmeyen varlık bireyine benzetme, yılan referansının açıklaması olup onu o varlıkla özdeşleştirmez."}],"identity_rationale":"Kaynak ifadesi biçimi yılan, beyaz yılan veya belirli bir yılan türü olarak verir; görünmeyen varlık anlamıyla bağ yalnızca benzetme açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yılan, beyaz yılan veya belirli bir yılan türü"}],"lexicalization_note":"Tanım yalın yılan adını korur ve aynı biçimin görünmeyen varlık anlamını bu dala taşımaz.","neighbor_coverage_note":"Bütün yılan, küçük canlı ve aynı kökten adaylar değerlendirildi; beyaz yılan ortaklığı taşıyan ayrı ad en keskin karşılaştırmayı sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Referans özellikleri kesişse de bunlar ayrı yılan adlarıdır; odak daha geniş ve türü değişken, komşu ise ayrı benzetmeyle kurulmuş addır.","focus_only":"Odak dal genel yılanı veya beyaz ya da belirli bir yılan türünü aynı ad altında kapsar.","gloss":"beyaz yılan adları","neighbor_only":"Komşu dal beyaz yılanı bir takı parçasının biçimine benzetilen ayrı bir adla sınırlar.","neighbor_ref":"root_001248/B009","relation_type":"near_neighbor","shared_zone":"Her iki dalın referansı bazı kullanımlarda beyaz bir yılan olabilir."}],"source_phrase_ar":"الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)","source_summary":"Kaynaklar yılan referansında birleşir; bazıları beyazlığı belirtir, biri bunu görünmeyen varlık bireyine benzetmeyle açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجان بمعنى الحية أو الحية البيضاء أو ضرب من الحيات","what_is_not_ar":"ليس الجان أبو الجن إلا من جهة اللفظ"},"support_links":[]},{"boundary":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_kind":"bare","branch_ref":"root_000266/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"halkın büyük kitlesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun çoğunluğunu, ana gövdesini veya sıradan insanlardan oluşan geniş kesimini anlatan bağlamlara uygundur.","boundary_detail":"Her küçük grup bu dala girmez; insanların ana gövdesi, büyük kitlesi veya çoğunluğu söz konusudur.","branch_image_ar":"سواد الناس وجماعتهم","concept_gloss":"halkın büyük kitlesi","contextual_glosses":[{"applicability":"Sayısal veya toplumsal bakımdan grubun ana bölümünün kastedildiği cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan grubunu ve grubun büyük ana bölümünü gösterme işlevini korur."},"facet_ids":["F001"],"text":"insanların çoğunluğu","usage_role":"contextual"}],"definition":"Bir insan topluluğunun büyük çoğunluğu, sıradan kitlesi veya topluca oluşturduğu ana gövdesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların çoğunluğu veya ana kitlesi tek bir toplumsal gövde olarak ele alınır."}],"identity_rationale":"Kaynak ifadesi insanların büyük çoğunluğunu, sıradan kitlesini veya topluca oluşturduğu ana gövdeyi bildirir; gece karanlığı ve yürek anlamları açıkça dışarıdadır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"insanların çoğunluğu veya halkın büyük kitlesi"}],"lexicalization_note":"Tanım yalın insan kitlesi anlamını korur ve başka topluluk türlerini ya da karanlık anlamını içeri almaz.","neighbor_coverage_note":"Bütün topluluk, çoğunluk, kalabalık ve aynı kökten adaylar değerlendirildi; ana kitle ile fiziksel izdiham ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta toplumsal çoğunluk veya ana gövde yeterlidir; komşuda insanların birbirini örten yoğun bir kalabalık oluşturması kurucu koşuldur.","focus_only":"Odak dal bir topluluğun ana gövdesini veya çoğunluğunu, fiziksel sıkışıklık şartı olmadan bildirir.","gloss":"insan kitlesi ve sık kalabalık","neighbor_only":"Komşu dal insanların kalabalıkta birbirini örtecek ölçüde sıkışmasını ve izdihamını gerektirir.","neighbor_ref":"root_001105/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da çok sayıda insanın oluşturduğu büyük topluluk alanında örtüşür."}],"source_phrase_ar":"جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)","source_summary":"Kaynaklar insanların çoğunluğu, kalabalık ana kitlesi ve sıradan toplumsal gövdesi anlamlarında birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه جنان الناس بمعنى معظمهم أو دهمائهم أو سوادهم وجماعتهم","what_is_not_ar":"ليس جنان الليل ولا الجنان القلب"},"support_links":[]},{"boundary":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_kind":"bare","branch_ref":"root_000266/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"bir şeyin ilk ve yeni dönemi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gençlik, çocukluk, dönem veya başka bir sürecin henüz başlangıçta olduğu ilk evresini anlatmaya uygundur.","boundary_detail":"Dal bir şeyin ilk ve yeni evresiyle sınırlıdır; genel olarak başlama eylemi veya ardışık evrelerin tamamı değildir.","branch_image_ar":"جن الشيء في بدايته","concept_gloss":"bir şeyin ilk ve yeni dönemi","contextual_glosses":[{"applicability":"Bir kişinin gençlik döneminin başlangıç kısmı özellikle kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençlik dönemini ve bu dönemin ilk, yeni evresini tam olarak korur."},"facet_ids":["F001","F002"],"text":"gençliğinin ilk yılları","usage_role":"contextual"}],"definition":"Gençlik, çocukluk, bir dönem veya herhangi bir şeyin henüz yeni olduğu ilk başlangıç evresidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin sürecindeki ilk, yeni ve henüz gelişmekte olan başlangıç dönemi seçilir."},{"facet_id":"F002","role":"example","statement":"Gençliğin veya çocukluğun ilk dönemi bu genel başlangıç evresinin belirgin örnekleridir."}],"identity_rationale":"Kaynak ifadesi gençlik, çocukluk, dönem veya herhangi bir şeyin ilk başlangıcını ve henüz yeni oluşunu bildirir; bu nedenle dal başlangıç evresi olarak doğru kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"gençliğin, çocukluğun veya bir dönemin ilk başlangıcı"}],"lexicalization_note":"Tanım yalın ilk dönem anlamını kapsar ve belirli bir başlama söz öbeğine ya da bütün yaşam evrelerine genişletilmez.","neighbor_coverage_note":"Bütün gençlik, başlama, evre ve karşıt zaman adayları değerlendirildi; başlangıç evresi ile başlama eylemi ayrımı en yararlı olandır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bir başlangıç evresini adlandırır; komşu ise başlama eylemini ve yeniden başlatmayı da kapsar, bu yüzden kapsamları tam çakışmaz.","focus_only":"Odak dal başlayan şeyin ilk ve yeni dönemini, yani süreç içindeki bir evreyi adlandırır.","gloss":"başlangıç ve ilk dönem","neighbor_only":"Komşu dal bir işe başlama, yeniden başlama veya yakın geçmişteki ilk zamanı da kapsayan eylemsel bir alandır.","neighbor_ref":"root_000060/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sürecin ilk noktasına veya başlangıç bölümüne yönelir."}],"source_phrase_ar":"كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)","source_summary":"Kaynaklar gençlik ve çocukluk örneklerinden hareketle anlamı herhangi bir şeyin ilk başlangıç ve yenilik dönemine geneller.","sources":["SI","TA"],"what_is_ar":"يدخل فيه جن الشباب أو الصبا أو العهد أو كل شيء بمعنى أول ابتدائه وحدثانه","what_is_not_ar":"ليس جنون العقل"},"support_links":[]},{"boundary":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_kind":"bare","branch_ref":"root_000266/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"uçuş sırasında çoğalan sinek vızıltısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Referansın sinek veya benzeri küçük uçucu canlı olduğu ve sesin uçuşta arttığı bağlamlara uygundur.","boundary_detail":"Ses anlamı böcek yorumu şartına bağlıdır; aynı biçim bitkiyi gösterdiğinde sıklaşma anlamı bu dalın dışında kalır.","branch_image_ar":"جن الذباب وصوت الخازباز","concept_gloss":"uçuş sırasında çoğalan sinek vızıltısı","contextual_glosses":[{"applicability":"Sinek veya benzeri küçük uçucu canlının çıkardığı sesin çoğalması eylem olarak anlatıldığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Böcek sesini ve bu sesin miktar veya yoğunluk bakımından artmasını korur."},"facet_ids":["F001"],"text":"vızıldaması artmak","usage_role":"contextual"}],"definition":"Sineğin veya sinek olarak yorumlanan küçük uçucu canlının uçuş sırasında sesini ve vızıltısını çoğaltmasıdır. Aynı ad bitkiyi gösterirse anlam ses değil, bitkinin sıklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sinek uçarken çıkardığı sesi veya vızıltıyı çoğaltır."},{"facet_id":"F002","role":"source_variant","statement":"İki yorumlu ad böceği gösterirse uçuş sesi, bitkiyi gösterirse sıklaşıp dolaşma anlamına gelir."}],"identity_rationale":"Kaynak ifadesi sineğin sesinin çoğalmasını açıkça destekler, ancak ikinci biçimin hem uçarken çok ses çıkaran bir böceğe hem de sıklaşan bir bitkiye yorumlanabileceğini söyler; dal yalnızca böcek yorumu altında ses dalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"sineğin vızıltısının veya sesinin çoğalması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması"}],"lexicalization_note":"Yalın ses dalı korunur, fakat iki yorumlu biçim yalnızca böcek referansı kesin olduğunda bu tanıma bağlanır.","neighbor_coverage_note":"Bütün böcek, ses, hareket ve aynı kökten adaylar değerlendirildi; ses kaynağını sınayan genel hareket uğultusu dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta ses kaynağı küçük uçucu böcektir ve ses çoğalır; komşu çok çeşitli hareket kaynaklarından çıkan hışırtı ve uğultuyu kapsar.","focus_only":"Odak dal belirli bir uçucu böceğin uçarken artan vızıltısına bağlıdır.","gloss":"vızıltı ve hareket uğultusu","neighbor_only":"Komşu dal rüzgar, hareket, alay veya kaynayan kap gibi çeşitli kaynakların hışırtı ve uğultusunu kapsar.","neighbor_ref":"root_001588/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da hareket sırasında doğan sürekli veya yinelenen sesi anlatabilir."}],"source_phrase_ar":"جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)","source_summary":"Kaynaklar sineğin sesinin çoğalmasını verir; iki yorumlu adın böcek okumasında uçuş vızıltısı, bitki okumasında ise sıklaşma bildirdiğini ayrıca belirtir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه كثرة صوت الذباب أو ترنم الخازباز حيث نص المصدر على ذلك","what_is_not_ar":"ليس نبات الخازباز إذا حمل على النبات"},"support_links":[]},{"boundary":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000266/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"göğüs kemikleri ve kaburga uçları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Göğüs kafesindeki kemiklerin topluca veya kaburgaların göğse yakın uçlarının özel olarak kastedildiği bağlamlara uygundur.","boundary_detail":"Dal göğüs kafesinin kemik yapısıyla sınırlıdır; yürek, göğüs eti veya kalça kemikleri anlamına gelmez.","branch_image_ar":"الجناجن عظام الصدر","concept_gloss":"göğüs kemikleri ve kaburga uçları","contextual_glosses":[{"applicability":"Anatomik anlatım genel göğüs kemiklerinden daha dar olarak kaburga uçlarını seçtiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaburga katılımcısını, uç bölümünü ve göğse yakın konumu eksiksiz korur."},"facet_ids":["F001"],"text":"kaburgaların göğse yakın uçları","usage_role":"explanatory"}],"definition":"Göğüs kafesindeki kemikler, özellikle kaburgaların göğse yakın uçları ve kimi açıklamada göğsün içteki orta kemiğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referans göğüs kafesinin kemikleri veya kaburgaların göğse yakın uçlarıdır."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklama aynı anatomik adı göğsün içteki orta kemiğine kadar genişletir."}],"identity_rationale":"Kaynak ifadesi göğüs kemiklerini ve kaburgaların göğse yakın uçlarını bildirir; bir kaynak içteki orta kemiği de aynı anatomik bölgeye dahil eder.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"göğüs kemikleri veya kaburgaların göğse yakın uçları"}],"lexicalization_note":"Tanım yalın anatomik kemik adını korur ve komşu organ, et veya başka eklem adlarını içeri almaz.","neighbor_coverage_note":"Bütün göğüs, kaburga, kalça, eklem ve aynı kökten adaylar değerlendirildi; kemik grubu ile orta göğüs kemiği ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak çoğul bir kemik grubu ve kaburga uçlarıdır; komşu ise göğsün ortasındaki belirli tek kemiği adlandırır.","focus_only":"Odak dal göğüs kemiklerini topluca ve özellikle kaburgaların göğse yakın uçlarını kapsar.","gloss":"göğüs kemikleri ve orta göğüs kemiği","neighbor_only":"Komşu dal göğsün ortasındaki tek kemiği, başını ve üzerindeki kıl çıkış yerini kapsar.","neighbor_ref":"root_001232/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal göğüs kafesinin ön ve orta bölümündeki kemik yapılarıyla ilgilidir."}],"source_phrase_ar":"الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)","source_summary":"Kaynaklar göğüs kemikleri tanımında birleşir; daha ayrıntılı açıklama kaburga uçlarını ve göğsün içteki orta kemiğini belirtir.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه الجناجن والجنجن عظام الصدر أو أطراف الأضلاع مما يلي الصدر","what_is_not_ar":"ليس الجنان القلب"},"support_links":[]},{"boundary":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000266/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","surface_ar":"جَنَّةٍ"}],"gloss":"içine girilip saklanılan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}}],"root_ar":"ج ن ن","root_id":"root_000266","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin görünmemek veya korunmak için içine girdiği genel saklanma yerini anlatan bağlamlara uygundur.","boundary_detail":"Genel anlam saklanma yeridir; özel yer kullanımı belirli bir tarihsel pazar adına bağlıdır ve akıl yitimi anlamıyla karıştırılmaz.","branch_image_ar":"المَجَنَّة موضع الاستتار","concept_gloss":"içine girilip saklanılan yer","contextual_glosses":[{"applicability":"Özel tarihsel yer adı değil, genel olarak saklanmaya yarayan mekan kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mekan referansını ve saklanma işlevini bağlam içinde eksiksiz korur."},"facet_ids":["F001"],"text":"saklanma yeri","usage_role":"contextual"}],"definition":"Bir kişinin içine girip saklanabildiği yerdir; ayrıca kaynakta anılan kentten birkaç mil uzakta bulunan belirli bir eski pazar yerinin adı olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer, kişinin içine girerek görünmekten saklanmasına imkan verir."},{"facet_id":"F002","role":"specialization","statement":"Aynı biçim kaynakta anılan kent yakınındaki belirli bir eski pazar yerinin adı olarak da kullanılır."}],"identity_rationale":"Tek kaynaklı ifade hem kişinin saklanabildiği bir yeri hem de kaynakta anılan kentten birkaç mil uzaktaki belirli eski pazar yerinin adını verir; dal iki kullanımı da kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı"}],"lexicalization_note":"Tanım yalın saklanma yeri anlamını ve kanıttaki özel yer kullanımını korur; barınak eylemlerinin tamamına genişletilmez.","neighbor_coverage_note":"Bütün barınak, gizlenme, korku, yer ve aynı kökten adaylar değerlendirildi; mekan ile sığınağa girme eylemi ayrımı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak öncelikle mekanı adlandırır; komşu ise bu mekana girme ve orada gizlenme eylemlerini kurucu anlam olarak taşır.","focus_only":"Odak dal saklanmaya imkan veren yeri adlandırır ve ayrıca belirli bir tarihsel yer kullanımına sahiptir.","gloss":"saklanma yeri ve sığınağa girme","neighbor_only":"Komşu dal bir sığınağa girme, orada kalma ve yüzünü gizleme eylemlerini de kapsar.","neighbor_ref":"root_001324/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin bir örtü veya sığınak içinde görünmekten saklanması alanındadır."}],"source_phrase_ar":"المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Saklanma yeri anlamı ile belirli eski pazar yerinin adı aynı tek kaynakta birlikte tanıklanır."}],"source_summary":"Tek kaynak saklanılan yer anlamını, kent yakınındaki ve eski pazarlar arasında sayılan belirli bir yer adıyla birlikte verir.","sources":["SI"],"what_is_ar":"يدخل فيه المجنة اسم موضع أو الموضع الذي يستتر فيه","what_is_not_ar":"ليس المجنة بمعنى الجنون"},"support_links":[]},{"boundary":"Dal, saygınlık ya da baskı anlamlarını değil, somut yukarı olma ve yükselmeyi kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B001","candidate_links":[{"candidate_id":"cand_968ccc94923129f4bf92","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"yukarı yükselme ve yüksekte olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, yukarıda olma ve aşağı karşıtı yüksekliktir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerde yükselme, bu çekirdeğin somut yer bağlamındaki gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dal, değer veya zorbalık anlamına geçmeden genel yukarı yön ve yükseklik alanında kalır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut yükseklik, yukarı konum ve aşağı karşıtı olma çekirdeği için kullanılır.","boundary_detail":"Dal, saygınlık ya da baskı anlamlarını değil, somut yukarı olma ve yükselmeyi kapsar.","concept_gloss":"yukarı yükselme ve yüksekte olma","contextual_glosses":[{"applicability":"Bir şeyin bulunduğu yerden daha yukarı konuma çıkmasını anlatan akışlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut yukarı çıkma olayını korur."},"facet_ids":["F002"],"text":"yükseldi","usage_role":"contextual"},{"applicability":"Hareketten çok yukarı konumda bulunma vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksek konum ve aşağı karşıtlığını korur."},"facet_ids":["F001"],"text":"yüksekteydi","usage_role":"contextual"}],"definition":"Bir şeyin aşağı karşıtı bir konuma çıkması veya baştan yukarı ve yüksek durumda bulunmasıdır; yer, cisim ve benzeri somut alanlarda yükseklik çekirdeğini taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, yukarıda olma ve aşağı karşıtı yüksekliktir."},{"facet_id":"F002","role":"specialization","statement":"Bir yerde yükselme, bu çekirdeğin somut yer bağlamındaki gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Dal, değer veya zorbalık anlamına geçmeden genel yukarı yön ve yükseklik alanında kalır."}],"identity_rationale":"Kaynak ifadesi bu dalı yukarıda olma, yukarı çıkma ve aşağı karşıtı yükseklik çekirdeğiyle verir. Geçici çerçeve bunu kişi değeri, zorbalık veya gramer ilgeci anlamına taşımadan somut yükselme alanında tuttuğu için korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yukarı olma; aşağı karşıtı yükseklik"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir yerde yükselmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"günün yükselmesi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yükselip uzaklaşmak"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım çıplak yükseklik çekirdeğini verirken yapı içi örnekleri buna bağlı tutar.","neighbor_coverage_note":"Adayların çoğu yukarı alanını paylaşır; en yararlı sınırlar fiziksel yükseklik, üst taraf, saygınlık ve karşıt alçalma arasında seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yüksekte olma ya da yükselme çekirdeğini taşır; komşu dal ise olaydan çok üst tarafı, üst yönden gelişi veya üst konumu adlandırır.","focus_only":"Yükselme veya yüksek durumda bulunma olayını anlatır.","gloss":"yükseklik ile üst taraf","neighbor_only":"Bir nesnenin üst yanı ya da yukarıdan geliş yönünü anlatır.","neighbor_ref":"root_001042/B005","relation_type":"near_neighbor","shared_zone":"İkisi de aşağı karşıtı yukarı alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal fiziksel veya yönsel yükseklikten söz eder; komşu dal aynı imgeyi toplumsal değer ve saygın mevki için kullanır.","focus_only":"Somut yukarı konum ve yükselme alanındadır.","gloss":"fiziksel yükseklik ile saygınlık","neighbor_only":"Kişi değeri, saygınlık ve yüksek mevki alanındadır.","neighbor_ref":"root_001042/B002","relation_type":"same_field","shared_zone":"Yüksek olma imgesi iki dalda da arka plandadır."},{"boundary_match":"partial","distinction":"Komşu dal hareketli çıkış ve tırmanma alanına daha dardır; bu dal ise hem yükselme eylemini hem de yüksek durumda bulunmayı kapsar.","focus_only":"Yüksekte bulunmayı hareket olmadan da kapsar.","gloss":"yükselme ile tırmanma","neighbor_only":"Merdiven, dağ veya benzeri bir yere tırmanma ve yukarı çıkma hareketini öne çıkarır.","neighbor_ref":"root_000862/B001","relation_type":"near_synonym","shared_zone":"İkisi de yukarı yöne çıkmayı anlatabilir."},{"boundary_match":"opposed","distinction":"Bu dal yukarı yönlü ya da yüksek konumu bildirirken komşu dal aşağı yönlü eğilme, çökme veya alçalma kutbunu bildirir.","focus_only":"Yukarı çıkma ve yüksekte olma yönündedir.","gloss":"yükselme ile alçalma","neighbor_only":"Baş, boyun veya gök cismi gibi şeylerde aşağı eğilme ve alçalma yönündedir.","neighbor_ref":"root_000419/B002","relation_type":"polarity_pair","shared_zone":"İkisi de dikey konum değişimi alanındadır."}],"source_summary":"Ortak kanıt, kökün temelini yukarıda bulunma, yükselme ve aşağı karşıtı yükseklik olarak kurar. Yer bağlamındaki kullanım bu çekirdeği somutlaştırır; saygınlık, zorbalık ve ilgeç kullanımı ayrı dallarda tutulmalıdır."},"support_links":["sup_60b3b1d27e1f81999199"]},{"boundary":"Dal, fiziksel yükselmeyi değil, değer ve saygınlık bakımından yüksek mevkiyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B002","candidate_links":[{"candidate_id":"cand_ec76527ea9d12c6a4987","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"saygınlıkta yüksek mevki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, değer ve saygınlık bakımından yüksek konumdur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi veya topluluk için seçkin ve yüksek mevki sahibi olma kullanımı bulunur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"En üstün ya da ölçüye sığmaz derecede yüce olma ifadesi aynı değer yüksekliğine bağlıdır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi, topluluk veya derece için değer bakımından yüksek konum anlatıldığında uygundur.","boundary_detail":"Dal, fiziksel yükselmeyi değil, değer ve saygınlık bakımından yüksek mevkiyi anlatır.","concept_gloss":"saygınlıkta yüksek mevki","contextual_glosses":[{"applicability":"Bir kişi veya aile için toplumdaki değer ve seçkinlik vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye ait saygınlık ve yüksek mevkiyi korur."},"facet_ids":["F001","F002"],"text":"saygın ve yüksek mevki sahibi","usage_role":"contextual"},{"applicability":"Derece üstünlüğü veya ölçüye sığmaz yücelik vurgusunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün derece ve değer yüksekliği unsurunu korur."},"facet_ids":["F003"],"text":"en yüce ve en değerli","usage_role":"contextual"}],"definition":"Bir kişinin, topluluğun veya derece bildiren konumun değer ve saygınlık bakımından yukarıda sayılmasıdır; yüksek mevki, seçkinlik ve kazanılmış onur dereceleri buna bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, değer ve saygınlık bakımından yüksek konumdur."},{"facet_id":"F002","role":"specialization","statement":"Kişi veya topluluk için seçkin ve yüksek mevki sahibi olma kullanımı bulunur."},{"facet_id":"F003","role":"extension","statement":"En üstün ya da ölçüye sığmaz derecede yüce olma ifadesi aynı değer yüksekliğine bağlıdır."}],"identity_rationale":"Kaynak ifadesi dalı saygınlık, yüksek derece, değer üstünlüğü ve seçkinlik alanında kurar. Geçici çerçeve bu alanı somut yer yüksekliğinden ve kınanan taşkınlıktan ayırdığı için kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"saygınlık ve yüksek mevki"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"değeri yüksek kimse veya nitelik"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"en üstün ve en yüksek değerde olan"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"saygın ve yüksek mevki sahibi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toplumun seçkinleri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kazanılmış yüksek onur dereceleri"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım hem biçimlerdeki değer yüksekliğini hem de kalıplardaki seçkinlik kullanımını ayırarak verir.","neighbor_coverage_note":"Adaylar arasında saygınlık alanına çok yakın dallar vardır; yayımlananlar fiziksel yükseklik, kibir ve toplumsal itibar sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal toplumsal ya da değer bakımından yüksekliği bildirir; komşu dal doğrudan yukarı konum veya yükselme alanındadır.","focus_only":"Değer ve saygınlık bakımından yüksek konumu anlatır.","gloss":"saygınlık ile fiziksel yükseklik","neighbor_only":"Yer, cisim veya yön bakımından somut yükseklik anlatır.","neighbor_ref":"root_001042/B001","relation_type":"same_field","shared_zone":"İkisi de yüksek olma fikrinden beslenir."},{"boundary_match":"field_only","distinction":"Bu dal meşru ya da övülen yüksek değeri anlatır; komşu dal kişinin kendini üstün görerek haddi aşmasını anlatır.","focus_only":"Övülen saygınlık ve yüksek değer alanındadır.","gloss":"saygınlık ile kibir","neighbor_only":"Kınanan kibir, taşkınlık ve zorbalık alanındadır.","neighbor_ref":"root_001042/B003","relation_type":"same_field","shared_zone":"İkisi de kişinin başkalarına göre yüksek konumuyla ilgilidir."},{"boundary_match":"partial","distinction":"Komşu dal itibar ve önde görünme alanına daha yakındır; bu dal değer bakımından yukarıda sayılma imgesini korur.","focus_only":"Yükseklik imgesiyle değer ve dereceyi öne çıkarır.","gloss":"yüksek mevki ile itibar","neighbor_only":"Toplumsal yüz, itibar ve önder kişiler üzerinden saygınlığı öne çıkarır.","neighbor_ref":"root_001630/B006","relation_type":"near_synonym","shared_zone":"İkisi de toplum içinde saygın ve seçkin olmayı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal rütbe, başkanlık ve miras alanlarını genişçe kapsar; bu dalın çekirdeği değer bakımından yüksek sayılmadır.","focus_only":"Saygınlığı yükseklik ve derece diliyle kurar.","gloss":"yüksek saygınlık ile üstün mevki","neighbor_only":"Başkanlık, soylu miras, öğretme veya egemen mevki gibi alanları da kapsar.","neighbor_ref":"root_001281/B005","relation_type":"near_synonym","shared_zone":"İkisi de şerefli ve yüksek toplumsal konumu anlatır."}],"source_summary":"Ortak kanıt, dalı saygınlık ve yüksek derece alanında birleştirir. Kişinin yüksek değeri, toplumun seçkinleri ve kazanılmış onur basamakları aynı değer-yüksekliği çekirdeğine bağlıdır."},"support_links":["sup_9698ebdaa2dd3e82a738"]},{"boundary":"Dal, iyi değer yüksekliği değil, kınanan üstünlük taslama ve taşkınlık alanıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"kibirli üstünlük taslama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, kınanan büyüklük taslama ve kendini üstün görmedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeryüzünde ya da bir yönetici için taşkınlık ve baskıcılık anlamı belirginleşir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim övülen veya kınanan alanda kullanılabilir; bu dal kınanan kullanımı ayırır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi veya güç sahibi kimsenin başkaları üzerinde haksız üstünlük iddiası anlatıldığında uygundur.","boundary_detail":"Dal, iyi değer yüksekliği değil, kınanan üstünlük taslama ve taşkınlık alanıdır.","concept_gloss":"kibirli üstünlük taslama","contextual_glosses":[{"applicability":"Bir kişinin toplum veya ülke içinde haddi aşan üstünlük tavrı anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kibirlenme ve taşkın davranma unsurunu korur."},"facet_ids":["F001","F002"],"text":"kibirlenip taşkınlık etti","usage_role":"contextual"},{"applicability":"Baskıdan çok iç tutum ve gururlu üstünlük iddiası vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baskı ve taşkınlık sonucu geri planda kalabilir.","preserves":"Kişinin üstünlük iddiasını korur."},"facet_ids":["F001"],"text":"kendini üstün gördü","usage_role":"contextual"}],"definition":"Kişinin veya yöneticinin kendini başkalarının üstünde görerek haksız büyüklük taslaması, taşkınlık etmesi ya da baskıcı davranmasıdır; övülen yüksek değerden ayrılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, kınanan büyüklük taslama ve kendini üstün görmedir."},{"facet_id":"F002","role":"specialization","statement":"Yeryüzünde ya da bir yönetici için taşkınlık ve baskıcılık anlamı belirginleşir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçim övülen veya kınanan alanda kullanılabilir; bu dal kınanan kullanımı ayırır."}],"identity_rationale":"Kaynak ifadesi dalı kınanan büyüklük taslama, kendini üstün görme ve zorbalıkla ilişkilendirir. Geçici çerçeve bu anlamı övülen saygınlık ve somut yükseklikten ayırdığı için kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kınanan büyüklük taslama"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yeryüzünde kibirlenip taşkınlık etmek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kibirli ve kendini üstün görenler"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım çıplak kınanan üstünlük anlamını ve yer yapısındaki taşkınlığı ayrı tutar.","neighbor_coverage_note":"Kibir, zorbalık ve taşkınlık adayları değerlendirildi; yayımlanan ayrımlar övülen mevki, zorba kişi ve fiili baskın gelme sınırlarını açar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ahlaken olumsuz üstünlük taslamayı anlatır; komşu dal yüksek değeri ve saygın mevkiyi anlatır.","focus_only":"Kınanan kibir ve taşkınlık alanındadır.","gloss":"kibir ile saygınlık","neighbor_only":"Övülen saygınlık ve yüksek değer alanındadır.","neighbor_ref":"root_001042/B002","relation_type":"same_field","shared_zone":"İkisi de başkalarına göre yüksek konum fikrini kullanır."},{"boundary_match":"partial","distinction":"Komşu dal taşma ve saldırgan yayılma imgesine yaslanır; bu dal kendini yukarıda görme ve büyüklük taslama çekirdeğini korur.","focus_only":"Yükseklik kök imgesiyle kınanan üstünlük taslar.","gloss":"kibirli üstünlük ile taşkınlık","neighbor_only":"Uzanıp taşma ve insanlara karşı yayılma imgesiyle baskıyı anlatır.","neighbor_ref":"root_000959/B006","relation_type":"near_synonym","shared_zone":"İkisi de insanlara karşı üstünlük ve zorbalık tavrını anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal kişi tipini ve yönetici zorbalığını öne çıkarır; bu dalın çekirdeği haksız şekilde kendini yukarıda görme eylemidir.","focus_only":"Tutum ve eylem olarak kibirli üstünlük taslamayı anlatır.","gloss":"üstünlük taslama ile zorba kişi","neighbor_only":"Zorba yönetici veya inatçı baskıcı kişi tipini adlandırır.","neighbor_ref":"root_000936/B004","relation_type":"near_neighbor","shared_zone":"İkisi de baskıcı ve kibirli güç kullanımına yaklaşır."},{"boundary_match":"partial","distinction":"Bu dal iç tutum ve kınanan büyüklük iddiasıdır; komşu dal yapı içinde gerçekleşen yenme veya bastırma ilişkisidir.","focus_only":"Ahlaki tutum olarak kibir ve taşkınlık bildirir.","gloss":"kibir ile üstün gelme","neighbor_only":"Belirli yapılarda birini yenme, bastırma veya işi üstlenme bildirir.","neighbor_ref":"root_001042/B004","relation_type":"near_neighbor","shared_zone":"İkisi de başkalarının üstüne çıkma fikrine dokunur."}],"source_summary":"Ortak kanıt, bu dalda yüksek olma imgesinin ahlaken olumsuz bir üstünlük taslama, zorbalık veya taşkınlık biçimine döndüğünü gösterir. Övülen saygınlık ve somut yükseklik ayrı dallar olarak korunur."},"support_links":[]},{"boundary":"Dal, belirli yapı ve nesnelerle üstün gelme alanındadır; çıplak yükseklik anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001042/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"yapı içinde üstün gelip bastırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bir şeyin üzerine üstün konuma geçip onu yenme veya bastırmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseye yöneldiğinde yenme ve galip gelme anlamı belirginleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Üzerine alma ve denetim kurma değeri, aynı yapı içi üstün konumdan gelişir."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, iş veya nesne üzerinde galip gelme ya da denetim kurma yapılarında uygundur.","boundary_detail":"Dal, belirli yapı ve nesnelerle üstün gelme alanındadır; çıplak yükseklik anlamına genellenmez.","concept_gloss":"yapı içinde üstün gelip bastırma","contextual_glosses":[{"applicability":"Nesne bir kişi olduğunda ve sonuç galibiyet olarak çevrildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üstüne çıkma ve yapı bağımlılığı açıkça görünmez.","preserves":"Galip gelme sonucunu korur."},"facet_ids":["F001","F002"],"text":"onu yendi","usage_role":"contextual"},{"applicability":"Bir işin sorumluluğunu kendi üzerine alma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşi üzerine alma ve tek başına yürütme değerini korur."},"facet_ids":["F003"],"text":"işi üstlendi","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişi, iş veya nesne üzerinde etkili üstün konuma geçip onu yenmek, bastırmak, üzerine almak ya da denetimine almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bir şeyin üzerine üstün konuma geçip onu yenme veya bastırmadır."},{"facet_id":"F002","role":"specialization","statement":"Bir kimseye yöneldiğinde yenme ve galip gelme anlamı belirginleşir."},{"facet_id":"F003","role":"extension","statement":"Üzerine alma ve denetim kurma değeri, aynı yapı içi üstün konumdan gelişir."}],"identity_rationale":"Kaynak ifadesi bu dalı bir şeye üstün gelip onu yenme, bastırma veya üzerinde etkili konuma geçme yapılarıyla verir. Geçici çerçeve bunu yalın yükseklik ve saygınlık anlamlarından ayırdığı için korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu yenip bastırmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kişiyi yenmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kılıçla vurmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"işi üstlenip tek başına yürütmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ata binmek"}],"lexicalization_note":"Mekanik kapsam kolokasyondur; tanım yalnız nesneye veya işe bağlanan yapılardaki üstün gelme değerini kapsar.","neighbor_coverage_note":"Adaylar arasında genel yenme ve baskı dalları çoktur; seçilenler yapı bağımlı üstün gelmeyi kibir, fiziksel yükseklik ve saf galibiyetten ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal daha geniş görünme ve güç yetirme alanlarına açılır; bu dal nesneye bağlı üstün gelme veya bastırma yapısıyla sınırlıdır.","focus_only":"Belirli yapılardaki yenme, bastırma ve üstlenme değerini kapsar.","gloss":"üstün gelme ile egemen olma","neighbor_only":"Görünür hale gelme, güç yetirme ve yukarı çıkma alanlarını da kapsar.","neighbor_ref":"root_000970/B007","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyin üzerinde galip ve güçlü konuma geçmeyi anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal genel yenme-kahretme anlamına daha doğrudandır; bu dal yapısal olarak bir şeyin üzerine çıkma ve üzerinde üstün konum alma imgesini taşır.","focus_only":"Üstüne çıkma imgesi ve kimi yapılarda üstlenme değerini korur.","gloss":"üstün gelme ile kahretme","neighbor_only":"Saf yenme ve kahretme çekirdeğini, zamanın her şeyi yenmesi gibi genişlemeleri kapsar.","neighbor_ref":"root_000494/B001","relation_type":"near_synonym","shared_zone":"İkisi de karşı tarafı yenme ve bastırma sonucunda buluşur."},{"boundary_match":"partial","distinction":"Bu dal ilişkisel bir eylem veya yapı içi sonuçtur; komşu dal ahlaki tutum ve taşkınlık alanındadır.","focus_only":"Fiili galip gelme, bastırma veya üstlenme ilişkisidir.","gloss":"üstün gelme ile kibir","neighbor_only":"Kınanan kibir ve kendini üstün görme tutumudur.","neighbor_ref":"root_001042/B003","relation_type":"near_neighbor","shared_zone":"İkisi de başkasının üstüne çıkma fikrinden yararlanır."},{"boundary_match":"field_only","distinction":"Bu dal yukarı imgesini galibiyet ve denetim ilişkisine taşır; komşu dalın çekirdeği fiziksel yükseklik veya yükselmedir.","focus_only":"Bir nesneye veya işe karşı üstünlük kurar.","gloss":"üstün gelme ile yükseklik","neighbor_only":"Somut yukarı konum veya yükselme bildirir.","neighbor_ref":"root_001042/B001","relation_type":"same_field","shared_zone":"İkisi de yukarıda olma imgesini paylaşır."}],"source_summary":"Ortak kanıt, bu dalda yukarıda olma imgesinin karşı tarafı yenme, bastırma veya üzerinde egemen konuma geçme ilişkisine dönüştüğünü gösterir. Bu yüzden anlam çıplak yükselme değil, yapı içinde üstün gelmedir."},"support_links":[]},{"boundary":"Dal, yükselme eylemi değil, üst taraf ve yukarıdanlık bildiren yapı alanıdır.","branch_kind":"collocation","branch_ref":"root_001042/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"üst yan ve yukarıdanlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bir şeyin üst tarafı ve aşağı karşıtı yukarı yönüdür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ev gibi nesnelerde üst kısım, alt kısmın karşıtı olarak adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yukarıdan gelme ve rüzgarın avın üstünde kalan yönü aynı üst-yön ilişkisini kullanır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üst kısmı, üst yönü veya yukarıdan geliş konumu anlatıldığında uygundur.","boundary_detail":"Dal, yükselme eylemi değil, üst taraf ve yukarıdanlık bildiren yapı alanıdır.","concept_gloss":"üst yan ve yukarıdanlık","contextual_glosses":[{"applicability":"Bir geliş ya da hareketin yukarıdaki taraftan olduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yukarıdanlık ve üst taraf yönünü korur."},"facet_ids":["F001","F003"],"text":"üst tarafından","usage_role":"contextual"},{"applicability":"Ev veya yapı için alt kısmın karşıtı üst bölüm anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üst kısım ve alt karşıtlığını korur."},"facet_ids":["F002"],"text":"evin üst katı","usage_role":"contextual"}],"definition":"Bir nesnenin aşağı karşıtı olan üst yanı veya o üst yandan geliş ve konumlanmadır; evin üst kısmı, yukarıdan gelme biçimleri ve rüzgarın üst yönü bu kapsamdadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bir şeyin üst tarafı ve aşağı karşıtı yukarı yönüdür."},{"facet_id":"F002","role":"specialization","statement":"Ev gibi nesnelerde üst kısım, alt kısmın karşıtı olarak adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Yukarıdan gelme ve rüzgarın avın üstünde kalan yönü aynı üst-yön ilişkisini kullanır."}],"identity_rationale":"Kaynak ifadesi bu dalı bir şeyin üst yanı, yukarıdan geliş biçimleri ve aşağı karşıtı yön olarak verir. Geçici çerçeve bunu oluşan yükselme ve değer yüksekliğinden ayırdığı için kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"evin üst kısmı; altının karşıtı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yukarıdan"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"üstten veya yukarıdan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yukarıdan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"rüzgarın avın üstünde kalan yönü"}],"lexicalization_note":"Mekanik kapsam kolokasyondur; tanım evin üstü, üstten geliş ve rüzgar yönü gibi bağlı yapılara özgüdür.","neighbor_coverage_note":"Yön ve üst taraf adayları değerlendirildi; seçilenler üst-alt kutbu, fiziksel yükselme ve baş kavramıyla karışabilecek sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal üst ve altında karşıtlığını daha genel verir; bu dal belirli kalıplarda üst yan, üstten geliş ve rüzgar yönü olarak kalır.","focus_only":"Belirli bağlı biçimlerle üst yan ve üstten geliş anlatır.","gloss":"üst yan ile yukarı konum","neighbor_only":"Üst, altında karşıtı ve yukarıdaki yüzey gibi daha genel yön ilişkilerini kapsar.","neighbor_ref":"root_001188/B001","relation_type":"near_synonym","shared_zone":"İkisi de alt karşıtı üst yön ve konum alanındadır."},{"boundary_match":"opposed","distinction":"Bu dal altın karşıtı üst tarafı bildirir; komşu dal aynı eksenin aşağı ve alt taraf kutbunu bildirir.","focus_only":"Üst yan ve yukarıdanlık bildirir.","gloss":"üst ile alt","neighbor_only":"Alt yan, aşağıda olma ve ayak altı gibi aşağı konum bildirir.","neighbor_ref":"root_000177/B001","relation_type":"polarity_pair","shared_zone":"İkisi de dikey yönde taraf ve konum belirtir."},{"boundary_match":"partial","distinction":"Bu dal yön ve taraf adıdır; komşu dal bir şeyin yükselmesi veya yüksek konumda olmasıdır.","focus_only":"Üst tarafı veya yukarıdan geliş yönünü adlandırır.","gloss":"üst taraf ile yükselme","neighbor_only":"Yükselme ya da yüksek durumda bulunma olayını anlatır.","neighbor_ref":"root_001042/B001","relation_type":"near_neighbor","shared_zone":"İkisi de yukarı alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal baş ve başlık alanına özgüleşir; bu dal daha genel olarak alt karşıtı üst yan ve yukarıdanlık verir.","focus_only":"Nesnenin üst tarafı veya üstten geliş yönünü kapsar.","gloss":"üst taraf ile baş","neighbor_only":"Baş, baş kısmı ve baş üzerinden gelişen çeşitli kişi veya nesne adlarını kapsar.","neighbor_ref":"root_000529/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin en üst bölümünü anlatabilir."}],"source_summary":"Ortak kanıt, dalı üst taraf ve yukarıdanlık alanında kurar. Bu kullanım bir şeyin yükselmesi değil, alt-üst karşıtlığında üst yanın veya üst yönden gelişin adlandırılmasıdır."},"support_links":[]},{"boundary":"Dal yalnız çağrı/emir biçimindedir; her zamanlı genel yükselme fiili değildir.","branch_kind":"non_bare","branch_ref":"root_001042/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"gel diye çağırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, muhatabı konuşana doğru gelmeye çağırmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım emir biçimine özgüdür ve genel fiil çekimi gibi yayılmaz."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çağrı anlamının arka planında daha yüksek yere çağırma veya yukarı çıkma imgesi bulunur."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Muhatabı konuşana doğru çağıran emir veya davet sözü için uygundur.","boundary_detail":"Dal yalnız çağrı/emir biçimindedir; her zamanlı genel yükselme fiili değildir.","concept_gloss":"gel diye çağırma","contextual_glosses":[{"applicability":"Doğrudan emir ve çağrı çevirisinde en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüksek yere çağırma kökeni açıkça görünmez.","preserves":"Muhataba yönelen gelme çağrısını korur."},"facet_ids":["F001","F002"],"text":"gel","usage_role":"contextual"},{"applicability":"Çağrının yalnız hareket emri değil, konuşana yönelme daveti olduğu açıklanmak istendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kısa emir doğallığı ve yukarı çıkma kökeni zayıflar.","preserves":"Çağrı ve konuşana yönelme unsurunu korur."},"facet_ids":["F001","F003"],"text":"buraya yönel","usage_role":"explanatory"}],"definition":"Yalnız çağrı ve emir kullanımında, muhatabı konuşana doğru gelmeye davet eden sözdür; kökeninde daha yüksek bir yere çağırma veya yukarı çıkma fikri bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, muhatabı konuşana doğru gelmeye çağırmadır."},{"facet_id":"F002","role":"specialization","statement":"Kullanım emir biçimine özgüdür ve genel fiil çekimi gibi yayılmaz."},{"facet_id":"F003","role":"extension","statement":"Çağrı anlamının arka planında daha yüksek yere çağırma veya yukarı çıkma imgesi bulunur."}],"identity_rationale":"Kaynak ifadesi dalı özel olarak emir ve çağrı biçimiyle muhatabı gelmeye davet eden söz olarak verir. Geçici çerçeve bunu genel fiil çekimi saymadan çağrı işleviyle sınırlandırdığı için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gel; buraya yönel"}],"lexicalization_note":"Mekanik kapsam çıplak değildir; tanım yalnız kalıplaşmış çağrı biçiminin işlevini verir.","neighbor_coverage_note":"Çağrı, seslenme ve gelme adayları içinden emir biçimine en yakın olanlar seçildi; ses ve genel davet dalları daha uzak bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal çağrı sözünü doğrudan verir; bu dalın sınırı emir biçimi ve yukarı yere çağırma kökeniyle belirlenir.","focus_only":"Yükseklikten gelen çağrı kökenini ve emir sınırını korur.","gloss":"gel çağrısı","neighbor_only":"Gel, yaklaş ve yönel anlamlı çağrı sözü olarak biçim eşitliği gösterebilir.","neighbor_ref":"root_001597/B001","relation_type":"near_synonym","shared_zone":"İkisi de muhatabı gelmeye veya yönelmeye çağırır."},{"boundary_match":"partial","distinction":"Komşu dal kalıplaşmış çağrı ifadesi içinde kullanılır; bu dal muhatabı konuşana doğru gelmeye çağıran özel biçimdir.","focus_only":"Tek başına gelmeye çağıran emir sözüdür.","gloss":"gel ile haydi gel","neighbor_only":"Belirli çağrı kalıplarında bir işe veya yiyeceğe yöneltme sözü olabilir.","neighbor_ref":"root_000383/B009","relation_type":"near_synonym","shared_zone":"İkisi de muhatabı bir yöne çağıran emir değeri taşıyabilir."},{"boundary_match":"field_only","distinction":"Bu dal tek bir gelme çağrısına daralır; komşu dal çağırma ve davet etmenin daha genel alanını kapsar.","focus_only":"Gelme emrini veren özel çağrı sözüdür.","gloss":"gel çağrısı ile genel davet","neighbor_only":"Seslenme, davet etme, yemeğe çağırma ve sözle yöneltme alanını genişçe kapsar.","neighbor_ref":"root_000478/B001","relation_type":"same_field","shared_zone":"İkisi de sözle çağırma alanındadır."},{"boundary_match":"partial","distinction":"Bu dal muhataba yönelen komuttur; komşu dal hareketin gerçekleşmesi veya gelme olayının kendisidir.","focus_only":"Emir ve çağrı sözüdür.","gloss":"gel çağrısı ile gelme","neighbor_only":"Fiilen gelme, varma veya getirme olayını anlatır.","neighbor_ref":"root_000009/B001","relation_type":"near_neighbor","shared_zone":"İkisi de konuşana ya da hedefe doğru geliş fikrinde buluşur."}],"source_summary":"Ortak kanıt, bu sözü gelmeye çağıran emir biçimi olarak açıklar ve kullanımını özellikle emirle sınırlar. Yükselme fikri anlamın kökeninde yer alır, fakat dalın işlevi çağrıdır."},"support_links":[]},{"boundary":"Dal, kişi için saygınlık sıfatı değil, yüksek yer veya yerleşmiş yer adı alanıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"yüksek yer adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, yüksek yer veya yüksek konumla adlandırılmış mekandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağ başı, yüksek yerleşim bölgesi ve üst oda gibi somut yer adları bu dala girer."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüce kayıt ya da cennetle ilişkili yer adı yorumları, yüksek yer çekirdeğine bağlı özel analizlerdir."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yukarı konumla adlandırılmış yer, oda, bölge veya yüce kayıt adları için uygundur.","boundary_detail":"Dal, kişi için saygınlık sıfatı değil, yüksek yer veya yerleşmiş yer adı alanıdır.","concept_gloss":"yüksek yer adları","contextual_glosses":[{"applicability":"Dağ başı veya yüksekte bulunan genel mekan anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksek mekan çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"yüksek yer","usage_role":"contextual"},{"applicability":"Evin veya yapının yukarıdaki odası kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapı içindeki yüksek oda değerini korur."},"facet_ids":["F002"],"text":"üst oda","usage_role":"contextual"}],"definition":"Yüksekte bulunan yerleri veya yukarı konumla adlandırılan yerleşim, oda ve yüce kayıt gibi adları kapsar; kişi için saygınlık sıfatı değil, mekanlaşmış addır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, yüksek yer veya yüksek konumla adlandırılmış mekandır."},{"facet_id":"F002","role":"specialization","statement":"Dağ başı, yüksek yerleşim bölgesi ve üst oda gibi somut yer adları bu dala girer."},{"facet_id":"F003","role":"source_variant","statement":"Yüce kayıt ya da cennetle ilişkili yer adı yorumları, yüksek yer çekirdeğine bağlı özel analizlerdir."}],"identity_rationale":"Kaynak ifadesi yüksek yer, oda, yerleşim alanı ve yukarı konumla adlandırılan özel yer/kayıt adlarını birlikte verir. Geçici çerçeve bunları kişi değeri ya da araç adı yapmadan yerleşmiş yer adları olarak tuttuğu için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"dağ başı veya yüksek yer"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"yüksek bölge veya yukarıdaki yerleşim"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yüksek yerler veya oraların halkı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst oda"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"iyi kimselere ait çok yüksek yer veya kayıt"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım biçimleşmiş yer adlarını çıplak yükseklikten ayırarak verir.","neighbor_coverage_note":"Yer ve konum adayları değerlendirildi; seçilenler yüksek mekan adlarını üst taraf, genel mekan ve baş konumdan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yüksekliği mekan adı olarak sabitler; komşu dal üst yan ve yukarıdanlık ilişkisini adlandırır.","focus_only":"Yerleşmiş yüksek mekan ve yer adlarını kapsar.","gloss":"yüksek yer ile üst taraf","neighbor_only":"Üst taraf, üstten geliş ve yukarı yön adlarını kapsar.","neighbor_ref":"root_001042/B005","relation_type":"near_neighbor","shared_zone":"İkisi de yukarı konum alanını paylaşır."},{"boundary_match":"field_only","distinction":"Bu dal yerleşmiş mekanları ve adları bildirir; komşu dal yükseklik durumunu ya da yükselme olayını bildirir.","focus_only":"Yüksek yer veya yerleşmiş mekan adıdır.","gloss":"yüksek yer ile yükselme","neighbor_only":"Yükselme veya yüksek durumda bulunma anlamıdır.","neighbor_ref":"root_001042/B001","relation_type":"same_field","shared_zone":"İkisi de yükseklik alanındadır."},{"boundary_match":"field_only","distinction":"Komşu dal mekan olma kavramını genişçe verir; bu dal yalnız yüksek konumla nitelenen yer adlarıdır.","focus_only":"Yüksek konumla adlandırılmış özel mekanları kapsar.","gloss":"yüksek yer ile genel mekan","neighbor_only":"Yer, mevki, yerleşme ve var olma alanından genel mekan kavramını kapsar.","neighbor_ref":"root_001332/B002","relation_type":"same_field","shared_zone":"İkisi de mekan ve konum alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal öncelik ve baş kısmı anlamlarını da taşır; bu dal yüksek konuma sahip mekan adlarıyla sınırlıdır.","focus_only":"Yüksek yer ve üst oda gibi mekan adlarını verir.","gloss":"yüksek yer ile ön-üst baş","neighbor_only":"Bir şeyin ön, üst veya ilk kısmını ve baş konumunu kapsar.","neighbor_ref":"root_000849/B002","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin üst veya önde gelen kısmına yaklaşabilir."}],"source_summary":"Ortak kanıt, dalı yüksek yer ve yerleşmiş mekan adları üzerinden kurar. Bazı örnekler somut oda veya bölge, bazıları ise çok yüksek manevi yer ya da kayıt yorumudur; hepsi yerleşmiş ad düzeyinde kalır."},"support_links":[]},{"boundary":"Dal, üstte duran ek şey veya üst parça alanıdır; bağımsız yüksek yer değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"üstüne eklenen veya üst parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bir yükün veya nesnenin üstüne eklenen şeydir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baş, boyun veya bir nesnenin üst kısmı aynı üstte bulunma ilişkisiyle adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kitap başlığı örneğinde üstte ve başta bulunma açıklaması baskındır, ancak köken yorumu kesin olmayabilir."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükün üstüne konan ek şey, nesnenin üst kısmı veya başta yer alan ad için uygundur.","boundary_detail":"Dal, üstte duran ek şey veya üst parça alanıdır; bağımsız yüksek yer değildir.","concept_gloss":"üstüne eklenen veya üst parça","contextual_glosses":[{"applicability":"Taşıma yükü tamamlandıktan sonra üste konan ek parça için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yük üstüne eklenen parça anlamını korur."},"facet_ids":["F001"],"text":"üst yük","usage_role":"contextual"},{"applicability":"Kitabın başta ve üstte yer alan adı için doğal çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel üstüne eklenme ve üst parça alanı kalmaz.","preserves":"Kitap başı ve adlandırma kullanımını korur."},"facet_ids":["F003"],"text":"başlık","usage_role":"contextual"}],"definition":"Bir taşıma ya da nesne tamamlandıktan sonra üstüne konan ek yük veya nesnenin üst kısmı olarak adlandırılan parçadır; baş, boyun ve kitabın başlığı gibi kullanımlar üstte bulunma ilişkisine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bir yükün veya nesnenin üstüne eklenen şeydir."},{"facet_id":"F002","role":"extension","statement":"Baş, boyun veya bir nesnenin üst kısmı aynı üstte bulunma ilişkisiyle adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Kitap başlığı örneğinde üstte ve başta bulunma açıklaması baskındır, ancak köken yorumu kesin olmayabilir."}],"identity_rationale":"Kaynak ifadesi dalı yükün veya nesnenin üstüne eklenen şey ve nesnenin üst kısmı olarak verir; kitap başlığı örneği de üstte ve başta bulunma ilişkisine bağlanır. Geçici çerçeve bunu bağımsız yüksek mekan veya ilgeç anlamıyla karıştırmadığı için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"tam yükten sonra üste konan ek yük"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"baş ve boyun"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir şeyin üst kısmı"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kitabın başlığı; başta ve üstte yer alan ad"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım hem biçimleşmiş adları hem de bağlı üst-parça kullanımlarını aynı üstte bulunma sınırında tutar.","neighbor_coverage_note":"Yük, üst parça ve nesne adı adayları değerlendirildi; seçilenler üst taraf, ağır yük ve araç adı sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal üstte duran ek yük veya parça adıdır; komşu dal üst tarafı ve yukarıdanlığı bildirir.","focus_only":"Üste eklenen şey veya üst parça adıdır.","gloss":"üst parça ile üst taraf","neighbor_only":"Üst taraf, üstten geliş veya yukarı yön ilişkisidir.","neighbor_ref":"root_001042/B005","relation_type":"near_neighbor","shared_zone":"İkisi de üstte bulunma alanını paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal yükün ağırlığını ve sorumluluğunu öne çıkarır; bu dal yükün tamamlandıktan sonra üstüne konan ek parçasına odaklanır.","focus_only":"Tam yükün üstüne konan ek parçayı da kapsar.","gloss":"üst yük ile ağır yük","neighbor_only":"Ağır yük, yükümlülük ve taşınan sorumluluk alanını genişçe kapsar.","neighbor_ref":"root_000971/B001","relation_type":"near_neighbor","shared_zone":"İkisi de taşınan yük alanına dokunabilir."},{"boundary_match":"field_only","distinction":"Bu dal nesnenin üstünde veya başında bulunma ilişkisini korur; komşu dal daha da sözlükselleşmiş araç ve parça adlarını listeler.","focus_only":"Üstte duran ek yük, baş-boyun ve kitap başlığı gibi üst parça adlarıdır.","gloss":"üst parça ile araç adı","neighbor_only":"Örs, taş, mızrak parçası, oyun oku ve kova düzeneği gibi araç/parça adlarıdır.","neighbor_ref":"root_001042/B009","relation_type":"same_field","shared_zone":"İkisi de kökten türeyen belirli nesne veya parça adlarıdır."},{"boundary_match":"field_only","distinction":"Komşu dal yükün ağırlık ve sorumluluk niteliğini anlatır; bu dal yükün konumuna, yani üstüne eklenmiş olmasına dayanır.","focus_only":"Üste eklenmiş nesne ya da üst parça anlamı taşır.","gloss":"üst ek ile yük ağırlığı","neighbor_only":"Taşınan ağır yük, günah veya ağır sözleşme anlamına odaklanır.","neighbor_ref":"root_000037/B004","relation_type":"same_field","shared_zone":"İkisi de yük ve taşıma alanıyla temas eder."}],"source_summary":"Ortak kanıt, dalı yükün üstüne konan ek şey ve nesnenin üst kısmı etrafında toplar. Kitap başlığı örneğinde üstte veya başta bulunma açıklaması verilirken köken yorumu bütünüyle kesinleştirilmez."},"support_links":[]},{"boundary":"Dal, genel yükseklik değil, belirli araç ve parça adlarının sözlükselleşmiş alanıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"belirli araç ve parça adları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, genel bir nitelik değil, belirli araç ve parça adları kümesidir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Örs ve süt ürünü konan taş gibi katı araç adları bu kümededir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mızrak bölümü, oyun oku ve kova düzeneğinde ipi düzelten kişi de aynı sözlükselleşmiş alandadır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Örs, taş, mızrak bölümü, oyun oku ve kova düzeneği gibi yerleşmiş adlar için uygundur.","boundary_detail":"Dal, genel yükseklik değil, belirli araç ve parça adlarının sözlükselleşmiş alanıdır.","concept_gloss":"belirli araç ve parça adları","contextual_glosses":[{"applicability":"Metal ya da taş örs adı kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Diğer araç ve parça adları dışarıda kalır.","preserves":"Sözlükselleşmiş araç adı değerini korur."},"facet_ids":["F002"],"text":"örs","usage_role":"contextual"},{"applicability":"Oyun okları içindeki özel yedinci ve en değerli ok anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyun oku, sıra ve üstün değer bilgisini korur."},"facet_ids":["F003"],"text":"yedinci oyun oku","usage_role":"explanatory"}],"definition":"Kökten türemiş belirli adlarla örs, süt ürünü için kullanılan taş, mızrak ucuna yakın bölüm, oyunda yedinci ok ve kova düzeneğinde görevli kişi gibi araç ve parça adları verilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, genel bir nitelik değil, belirli araç ve parça adları kümesidir."},{"facet_id":"F002","role":"example","statement":"Örs ve süt ürünü konan taş gibi katı araç adları bu kümededir."},{"facet_id":"F003","role":"example","statement":"Mızrak bölümü, oyun oku ve kova düzeneğinde ipi düzelten kişi de aynı sözlükselleşmiş alandadır."}],"identity_rationale":"Kaynak ifadesi dalı genel bir yükseklik sıfatı olarak değil, belirli araçlar ve parçalar için yerleşmiş adlar olarak verir. Geçici çerçeve örs, taş, mızrak bölümü, oyun oku ve kova düzeneği gibi adları aynı sözlükselleşmiş alanda tuttuğu için uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"örs"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kurutulmuş süt ürünü konan taş"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"mızrağın uç kısmına yakın bölümü"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"oyun oklarının yedincisi ve en değerlisi"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"kova ipini makaraya geri alan kişi"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"sağ yandan süt hayvanına yaklaşan kişi"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"ipi makaradaki yerine kaldırmak"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım biçim ve kolokasyonları genel sıfatlaştırmadan sözlükselleşmiş adlar olarak ayırır.","neighbor_coverage_note":"Araç, parça ve makara adayları değerlendirildi; seçilenler bu dalın genel alet anlamı değil, yerleşmiş adlar kümesi olduğunu gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal araç ve özel parça adları listesine dayanır; komşu dal üstte veya başta bulunma ilişkisini koruyan adlardır.","focus_only":"Örs, taş, mızrak bölümü ve oyun oku gibi yerleşmiş araç/parça adlarıdır.","gloss":"araç adı ile üst parça","neighbor_only":"Yük üstüne konan ek şey, baş-boyun ve kitap başlığı gibi üst parça adlarıdır.","neighbor_ref":"root_001042/B008","relation_type":"same_field","shared_zone":"İkisi de kökten türeyen nesne ve parça adlarıdır."},{"boundary_match":"field_only","distinction":"Komşu dal itme ve yontma araçlarına özgüdür; bu dal üstlük kökünden sözlükselleşmiş farklı araç ve parça adlarını toplar.","focus_only":"Örs, oyun oku ve kova düzeneği gibi bu köke özgü araç/parça adlarıdır.","gloss":"araç adları","neighbor_only":"Kısa mızrak, oluklu çubuk ve itme-yontma aracı gibi başka araç adlarıdır.","neighbor_ref":"root_000930/B006","relation_type":"same_field","shared_zone":"İkisi de somut araç veya parça adları alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal aygıtın kendisidir; bu dal ipi o aygıta yükselten kişi veya eylem gibi bağlı kullanımları içerir.","focus_only":"Kova ipini makaraya geri alan kişi veya ipi yerine kaldırma eylemini de içerir.","gloss":"makara görevlisi ile makara","neighbor_only":"Makaranın kendisini ve dönen küçük çarkı adlandırır.","neighbor_ref":"root_000143/B006","relation_type":"near_neighbor","shared_zone":"İkisi de kuyu ve makara düzeneği alanında buluşabilir."},{"boundary_match":"field_only","distinction":"Komşu dal araç kavramını daha genel verir; bu dal tek tek adlaşmış birimlerle sınırlıdır.","focus_only":"Belli sözlükselleşmiş araç ve parça adlarını verir.","gloss":"özel araç adları ile alet","neighbor_only":"Alet, taşıyıcı ve çadır parçaları gibi genel araç alanını kapsar.","neighbor_ref":"root_000067/B008","relation_type":"same_field","shared_zone":"İkisi de araç ve taşıyıcı parça alanındadır."}],"source_summary":"Ortak kanıt, dalı araç ve parça adlarının listesi olarak verir. Anlamı genel yükseklik sıfatına açmak yerine, her bir birimi yerleşmiş sözlük adı olarak ele almak gerekir."},"support_links":[]},{"boundary":"Dal, bedence uzun ve iri yapıdır; toplumsal saygınlık veya mekan yüksekliği değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B010","candidate_links":[{"candidate_id":"cand_831c1c10c985a90aeebb","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"uzun ve iri yapılı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bedence uzun ve iri yapılı olmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deve ve dişi deve örneklerinde irilik, uzunluk ve sağlam yaratılış birlikte belirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi ve hayvan uygulamalarında kapsam farkları bulunur, fakat hepsi bedensel yapı alanında kalır."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi veya hayvanın bedence uzun, iri ve sağlam oluşu anlatıldığında uygundur.","boundary_detail":"Dal, bedence uzun ve iri yapıdır; toplumsal saygınlık veya mekan yüksekliği değildir.","concept_gloss":"uzun ve iri yapılı","contextual_glosses":[{"applicability":"İnsan için bedensel görünüş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzunluk ve irilik unsurunu korur."},"facet_ids":["F001","F003"],"text":"uzun boylu ve iri","usage_role":"contextual"},{"applicability":"Deve veya dişi deve için sağlam ve iri beden vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan için irilik ve sağlam yaratılış unsurunu korur."},"facet_ids":["F002"],"text":"sağlam yapılı iri deve","usage_role":"contextual"}],"definition":"İnsan, deve veya özellikle dişi deve için uzun, iri ve bedence sağlam yaratılış bildiren kullanımdır; saygınlık ya da yüksek mekan anlamı taşımaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bedence uzun ve iri yapılı olmadır."},{"facet_id":"F002","role":"specialization","statement":"Deve ve dişi deve örneklerinde irilik, uzunluk ve sağlam yaratılış birlikte belirir."},{"facet_id":"F003","role":"source_variant","statement":"Kişi ve hayvan uygulamalarında kapsam farkları bulunur, fakat hepsi bedensel yapı alanında kalır."}],"identity_rationale":"Kaynak ifadesi dalı insan veya deve için uzunluk, irilik ve sağlam yaratılış alanında kurar. Geçici çerçeve bunu saygınlık veya yüksek yer anlamından ayırdığı için kaynakla uyumludur; cinsiyet ve tür uygulamalarındaki değişiklikler tanımda daraltıcı değil açıklayıcı sınır olarak tutulur.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"uzun iri kimse veya iri deve"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"sağlam yapılı dişi deve"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"uzun, iri ve sağlam yaratılışlı"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım biçim ve hayvan yapısı kalıplarını bedensel uzunluk/irilik alanında tutar.","neighbor_coverage_note":"Boy, irilik, sağlam yapı ve kas gücü adayları değerlendirildi; seçilenler uzun-iri beden anlamını genel yükseklikten ve kalınlıktan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal boy ve duruş ölçüsünü genişçe verir; bu dal uzunluğu irilik ve sağlam yaratılışla birlikte bildirir.","focus_only":"Uzunlukla birlikte irilik ve sağlam yaratılış bildirir.","gloss":"iri uzunluk ile boy","neighbor_only":"Boy, dik duruş ve beden ölçüsü alanını daha genel anlatır.","neighbor_ref":"root_001273/B011","relation_type":"near_synonym","shared_zone":"İkisi de bedensel uzunluk ve boy alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal genişlik ve kalınlığa daha yakındır; bu dal uzun ve yüksek beden yapısını irilikle birleştirir.","focus_only":"Uzunluk unsurunu irilikle birlikte taşır.","gloss":"uzun iri ile kalın iri","neighbor_only":"Kalınlık, genişlik ve kaba iri yapı unsurunu öne çıkarır.","neighbor_ref":"root_000148/B008","relation_type":"near_synonym","shared_zone":"İkisi de bedence büyük ve iri yapıyı anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal sıkı ve kuvvetli beden dokusuna odaklanır; bu dal bedenin uzun ve iri oluşunu öne çıkarır.","focus_only":"Uzun ve iri beden yapısını bildirir.","gloss":"uzun irilik ile sıkı yapı","neighbor_only":"Etin sıkılığı ve bedenin sert/kuvvetli oluşunu bildirir.","neighbor_ref":"root_000874/B004","relation_type":"near_neighbor","shared_zone":"İkisi de güçlü ve sağlam beden görünüşüyle temas eder."},{"boundary_match":"field_only","distinction":"Bu dal canlı bedeninin uzun ve iri yapısıdır; komşu dal herhangi bir şeyin yukarı konumu veya yükselmesidir.","focus_only":"Bedensel uzun ve iri yaratılış bildirir.","gloss":"boy iriliği ile yükseklik","neighbor_only":"Somut yükselme veya yüksekte bulunma bildirir.","neighbor_ref":"root_001042/B001","relation_type":"same_field","shared_zone":"İkisi de yukarı ve yüksek olma imgesine yaklaşır."}],"source_summary":"Ortak kanıt, uzunluk ve irilik anlamını insan ve deve örnekleriyle verir. Kimi kullanımda cinsiyet veya tür sınırı tartışmalı görünse de dalın ortak çekirdeği bedensel uzunluk, irilik ve sağlam yapıdır."},"support_links":["sup_f3f9cb1403b2445d7df4"]},{"boundary":"Dal, lohusalıktan temizlenme ve belirli hastalıktan kurtulma yapılarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001042/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"bedensel halden kurtulup esenleşme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek anlam, bedensel sıkıntı halinden kurtulup esenliğe çıkmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Lohusa kadının temizlenmesi ve kurtulması en belirgin sınırlı kullanımdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hastalıktan kurtulan erkek örneği de verilir, fakat bu dal genel iyileşme anlamına genişletilmez."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Lohusalık veya belirli hastalık sonrası kurtulma ve esenliğe çıkma bağlamında uygundur.","boundary_detail":"Dal, lohusalıktan temizlenme ve belirli hastalıktan kurtulma yapılarıyla sınırlıdır.","concept_gloss":"bedensel halden kurtulup esenleşme","contextual_glosses":[{"applicability":"Kadının lohusalık halinden çıkması ve esenliğe kavuşması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Lohusalık, temizlenme ve kurtulma unsurlarını korur."},"facet_ids":["F001","F002"],"text":"lohusalıktan temizlenip kurtuldu","usage_role":"contextual"},{"applicability":"Erkeğin belirli hastalıktan esenliğe çıkması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalık halinden kurtulmayı korur."},"facet_ids":["F001","F003"],"text":"hastalığından kurtuldu","usage_role":"contextual"}],"definition":"Sınırlı yapılarda, lohusa kadının temizlenip esenliğe çıkması veya erkeğin hastalıktan kurtulmasıdır; genel yükselme değil, sıkıntılı bedensel halden çıkıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek anlam, bedensel sıkıntı halinden kurtulup esenliğe çıkmadır."},{"facet_id":"F002","role":"specialization","statement":"Lohusa kadının temizlenmesi ve kurtulması en belirgin sınırlı kullanımdır."},{"facet_id":"F003","role":"source_variant","statement":"Hastalıktan kurtulan erkek örneği de verilir, fakat bu dal genel iyileşme anlamına genişletilmez."}],"identity_rationale":"Kaynak ifadesi bir yandan lohusa kadının temizlenip kurtulmasını özellikle sınırlar, diğer yandan hastalıktan kurtulan erkek için de bir yapı verir. Dal korunabilir, fakat tanım bu iki bağlı yapıyla sınırlanmalı ve genel yükselme ya da her türlü iyileşme anlamına genişletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_044","rendering_kind":"ordinary","target_gloss":"lohusalıktan temizlenip esenliğe kavuşmak"},{"lexical_unit_id":"lu_045","rendering_kind":"ordinary","target_gloss":"hastalıktan kurtulmak"}],"lexicalization_note":"Mekanik kapsam kolokasyondur; tanım yalnız lohusalık ve hastalık yapılarındaki kurtulma değerini verir.","neighbor_coverage_note":"İyileşme ve hastalık adayları değerlendirildi; seçilenler dalın genel şifa değil, sınırlı yapı içi kurtulma olduğunu gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel iyileşme anlamına daha doğrudur; bu dal belirli lohusalık ve hastalık yapılarıyla sınırlıdır.","focus_only":"Lohusalık veya belirli hastalık yapısıyla sınırlı kurtulmayı anlatır.","gloss":"sınırlı kurtulma ile iyileşme","neighbor_only":"Hastanın genel olarak iyileşmesi ve hastalıktan arınması alanını kapsar.","neighbor_ref":"root_000100/B003","relation_type":"near_synonym","shared_zone":"İkisi de hastalık veya bedensel halden kurtulma alanındadır."},{"boundary_match":"partial","distinction":"Komşu dal iyileştirme ve rahatlatma alanını genişletir; bu dal kendiliğinden ya da durumdan çıkış olarak sınırlı kurtulmadır.","focus_only":"Sıkıntılı bedensel halden çıkma yapısını verir.","gloss":"esenleşme ile şifa","neighbor_only":"İyileştirme, şifa verme ve gönül sıkıntısını giderme gibi geniş kullanımları da kapsar.","neighbor_ref":"root_000806/B001","relation_type":"near_synonym","shared_zone":"İkisi de rahatsızlık halinin giderilmesi alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu dal ateş ve ağır hastalık bağlamlarını öne çıkarır; bu dal özellikle lohusalık temizlenmesi ve bir hastalıktan kurtulma yapılarıyla verilir.","focus_only":"Lohusalık ve belli hastalık yapılarıyla sınırlıdır.","gloss":"hastalıktan çıkma","neighbor_only":"Ateş veya ağır hastalıktan ayrılma ve ayılma gibi belirli tıbbi çıkışı anlatır.","neighbor_ref":"root_001148/B010","relation_type":"near_synonym","shared_zone":"İkisi de hastalığın kişiden ayrılması ya da kişinin esenliğe çıkması alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal bedensel sıkıntıdan kurtulma sonucudur; komşu dal fiziksel yukarı konum veya yükselmedir.","focus_only":"Bedensel halden kurtulmayı yukarı çıkma imgesiyle anlatır.","gloss":"esenleşme ile yükselme","neighbor_only":"Somut yükseklik ve yükselme olayını anlatır.","neighbor_ref":"root_001042/B001","relation_type":"same_field","shared_zone":"İkisi de aşağıdan yukarı çıkma imgesine bağlanabilir."}],"source_summary":"Ortak kanıt, lohusalıktan temizlenme ve hastalıktan kurtulma yapılarını aynı sınırlı kurtulma alanında verir. Kanıt içinde kullanım sınırı dar tutulduğu için tanım genel iyileşme veya genel yükselme anlamına açılmaz."},"support_links":[]},{"boundary":"Dal, dil bilgisi görevi ve kalıplaşmış söz kullanımıdır; yükselme fiili değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001042/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","surface_ar":"عَالِيَةٍ"}],"gloss":"ilgeç ve kalıplaşmış görev sözü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, fiilden ayrı bir görev sözü ve ilgeç kullanımıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kimi yapılarda üzerinde, yanından veya üstünden gibi adlaşmış yön değerleri oluşur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıplaşmış emir yapılarında al veya bana ver gibi yöneltilmiş görev değerleri bulunur."}}],"root_ar":"ع ل و","root_id":"root_001042","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükselme fiili değil, gramer görevi veya kalıplaşmış emir sözü kastedildiğinde uygundur.","boundary_detail":"Dal, dil bilgisi görevi ve kalıplaşmış söz kullanımıdır; yükselme fiili değildir.","concept_gloss":"ilgeç ve kalıplaşmış görev sözü","contextual_glosses":[{"applicability":"İlgeç göreviyle konum veya yön ilişkisi kurduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adlaşmış ve emirleşmiş diğer görevler dışarıda kalır.","preserves":"İlgeç görevindeki üstlük ve yön ilişkisini korur."},"facet_ids":["F001","F002"],"text":"üzerinde veya üzerine","usage_role":"contextual"},{"applicability":"Kalıplaşmış emir yapısı bir nesneyi alma emri verdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalıplaşmış emir ve alma değerini korur."},"facet_ids":["F003"],"text":"şunu al","usage_role":"contextual"}],"definition":"Bağımsız yükselme fiili değil, belirli dil bilgisi görevlerinde kullanılan ilgeç, adlaşmış biçim veya kalıplaşmış emir sözüdür; bağlama göre üzerinde, yanından, al ya da ver değerleri taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, fiilden ayrı bir görev sözü ve ilgeç kullanımıdır."},{"facet_id":"F002","role":"specialization","statement":"Kimi yapılarda üzerinde, yanından veya üstünden gibi adlaşmış yön değerleri oluşur."},{"facet_id":"F003","role":"associated_use","statement":"Kalıplaşmış emir yapılarında al veya bana ver gibi yöneltilmiş görev değerleri bulunur."}],"identity_rationale":"Kaynak ifadesi dalı fiil anlamından ayrı olarak ilgeç, adlaşmış görev sözü ve kalıplaşmış emir kullanımlarıyla verir. Geçici çerçeve bunu şeref veya somut yükselme anlamına taşımadığı için kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_046","rendering_kind":"ordinary","target_gloss":"üzerinde, üzerine veya benzeri ilgeç görevi"},{"lexical_unit_id":"lu_047","rendering_kind":"ordinary","target_gloss":"şunu al"},{"lexical_unit_id":"lu_048","rendering_kind":"ordinary","target_gloss":"bana şunu ver"},{"lexical_unit_id":"lu_049","rendering_kind":"ordinary","target_gloss":"onun yanından veya üstünden"}],"lexicalization_note":"Mekanik kapsam karışıktır; tanım ilgeç görevini ve kalıplaşmış emir yapılarını çıplak fiil anlamından ayırır.","neighbor_coverage_note":"Dil bilgisi ve görev sözü adayları değerlendirildi; seçilenler bu dalı yön adından, tümleç teriminden ve başka görev sözlerinden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gramer görevi ve kalıplaşmış söz değeridir; komşu dal üst taraf veya yukarıdan geliş anlamını adlandırır.","focus_only":"İlgeç veya kalıplaşmış görev sözü olarak çalışır.","gloss":"ilgeç ile üst taraf","neighbor_only":"Üst taraf ve yukarıdanlık bildiren bağlı yön adlarıdır.","neighbor_ref":"root_001042/B005","relation_type":"near_neighbor","shared_zone":"İkisi de üstlük ve yukarı yön ilişkisine temas eder."},{"boundary_match":"field_only","distinction":"Komşu dal gramer sınıflarını adlandırır; bu dal belirli bir görev sözünün kullanımlarını verir.","focus_only":"İlgeç ve kalıplaşmış emir sözü olarak belirli görevler taşır.","gloss":"görev sözü ile tümleç","neighbor_only":"Dil bilgisinde tümleyen ve tümleç türlerini adlandıran teknik sınıfları kapsar.","neighbor_ref":"root_001167/B007","relation_type":"same_field","shared_zone":"İkisi de dil bilgisi ve söz görevleri alanındadır."},{"boundary_match":"field_only","distinction":"Komşu dal soru ve geçiş değerleri taşır; bu dal üstlük ilişkisi veya kalıplaşmış emir göreviyle sınırlıdır.","focus_only":"Üstlük kökenli ilgeç ve emirleşmiş kalıplardır.","gloss":"ilgeç görevi ile soru sözü","neighbor_only":"Soru, seçenek veya geçiş bildiren ayrı bir bağlaç/ilgeç alanıdır.","neighbor_ref":"root_000053/B016","relation_type":"same_field","shared_zone":"İkisi de bağımsız sözlük anlamından çok görev sözü olarak işler."},{"boundary_match":"field_only","distinction":"Komşu dal başka bir edat kalıbının anlamlarını verir; bu dal üstlük kökenli ilgeç ve emirleşmiş biçimleri kapsar.","focus_only":"Üzerinde, yanından, al veya ver gibi görevler taşır.","gloss":"farklı görev sözleri","neighbor_only":"Başka bir kalıpta ancak, dışında, üzere veya sebebiyle gibi görevler taşır.","neighbor_ref":"root_001459/B005","relation_type":"same_field","shared_zone":"İkisi de kalıplaşmış görev sözü alanındadır."}],"source_summary":"Ortak kanıt, dalı ilgeç ve adlaşmış/kalıplaşmış görev sözü olarak verir. Bazı örnekler konum veya kaynak yönünü, bazıları ise al ve ver gibi emir değerini gösterir; bunlar yükselme fiiliyle karıştırılmamalıdır."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_1d108a23f131e38a67d8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:carried-subject-continuity","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_299a9b314a7b1b9d052e"],"title":"prior group carried into location","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_c616824b9a27b08891c4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:compact-sound-entry","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_ea81b14f122587f55b81"],"title":"compact sound enters enclosure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_f32439e60182141c2702","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:domain-introduction-before-pronominal-return","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_47a9c6030d000ab15287"],"title":"named domain before later return","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_67b318fd0259ba545785","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:high-garden-formula","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_e15895eebfa0a4570582"],"title":"high-garden formula opened","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_f0248c9a53de4874cb7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:interiority-as-state-domain","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_c050b4c58e1f19e17915"],"title":"inside a place and condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:1"],"branch_refs":[],"candidate_id":"cand_7019adc5b35c9e06e7c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:10:1:predicative-locative-frame","source_type":"word_analysis","support_ids":["sup_19f682b407bc005c9a92","sup_4168ac247d4704f41006"],"title":"locative predicate leads the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:1","qac_refs":["88:10:1:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_fea9a73c3a5dc54c7707","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:boundary-from-satisfaction-to-shelter","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_b170bc059980308737ea"],"title":"satisfaction housed as shelter","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_e81b57a318d8ab1e79d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:branch-boundaries","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_3aef6f5cf5e11f9fb852"],"title":"covering field bounded by the noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_4c8d2cfbb83790a4bdc9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:covered-protective-garden","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_6b95dc23f5be0cfc73fa"],"title":"covered garden as refuge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_8d2efb1252bf02b981a5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:governed-head-hinge","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_6c9b2e8910852c7e33c1"],"title":"garden as governed hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_5fe0e0906a3994c33004","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:high-garden-reversal","source_type":"word_analysis","support_ids":["sup_08d4681691ac70b0a7a0","sup_255fbea119e5fbef1f2e"],"title":"high-garden reversal of exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_33f10d49e79737cd4b93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:indefinite-singular-environment","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_4e606b9a2b705cb11578"],"title":"open singular reward-space","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_a1163e87d6616b640870","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:sound-density-before-lift","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_28b8443818bc6727bb7d"],"title":"dense sound before lift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_35bf45480a4999352516","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:whole-domain-unpacked-later","source_type":"word_analysis","support_ids":["sup_255fbea119e5fbef1f2e","sup_cf5d30974ce9cdc64b5b"],"title":"garden named before interior unpacking","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:2","qac_refs":["88:10:2:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_cad140086450081de2a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:achieved-elevation-not-raising-act","source_type":"word_analysis","support_ids":["sup_31e8b738fdfac91b81b9","sup_d5a82002c1e23c702a10"],"title":"achieved elevation, not raising","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_d033c06a08b2361dfbcc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:agreeing-adjective-bound-to-garden","source_type":"word_analysis","support_ids":["sup_d5a82002c1e23c702a10","sup_eeae6d813918654c2924"],"title":"height bound to the garden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_fd329fb9af167bb9fdb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:bounded-root-branches","source_type":"word_analysis","support_ids":["sup_77849b472f688522c163","sup_d5a82002c1e23c702a10"],"title":"loftiness without conquest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_857d1098effc532d606a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:final-high-garden-formula","source_type":"word_analysis","support_ids":["sup_d0b727638740ea637878","sup_d5a82002c1e23c702a10"],"title":"final word seals formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_ef11243257e0e9530566","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:open-quality-not-superlative","source_type":"word_analysis","support_ids":["sup_cf24a92cb16e75663cc2","sup_d5a82002c1e23c702a10"],"title":"lofty, not ranked highest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_1020e3f3075fc4221fb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:reward-setting-after-satisfaction","source_type":"word_analysis","support_ids":["sup_6f8cbd8c9aa4f9896f52","sup_d5a82002c1e23c702a10"],"title":"satisfaction answered by elevation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_0b38a9332252930650f9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:sound-lift","source_type":"word_analysis","support_ids":["sup_d5a82002c1e23c702a10","sup_fd9412627333ecf6ef7b"],"title":"open vowel lift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_26f4329a2821a1e4ac8f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:spatial-and-rank-elevation","source_type":"word_analysis","support_ids":["sup_10053af0bb2bc0d41a86","sup_d5a82002c1e23c702a10"],"title":"spatial height with rank","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_326364c9b6f3c4ad8ab0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:stable-participial-quality","source_type":"word_analysis","support_ids":["sup_b5f1d42661a0be0970ee","sup_d5a82002c1e23c702a10"],"title":"stable quality, not event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:10:3","qac_refs":["88:10:3:1"],"status":"accepted"}},{"anchor_refs":["88:10:2"],"branch_refs":[],"candidate_id":"cand_39db81bf1cb45385af6a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000266"],"scope":"focus_ayah","source_local_id":"88:10:2:1","source_type":"qac_morpheme","support_ids":["sup_c32eab9e8f4633ddce45"],"title":"QAC root occurrence: ج ن ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:10:3"],"branch_refs":[],"candidate_id":"cand_977f0cc2afc7e8efb4f2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001042"],"scope":"focus_ayah","source_local_id":"88:10:3:1","source_type":"qac_morpheme","support_ids":["sup_1374e9829a959f37527b"],"title":"QAC root occurrence: ع ل و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:10","branch_refs":["root_000266/B003","root_001042/B001"],"candidate_id":"cand_968ccc94923129f4bf92","commentary_obligation":"review","hft_ref":"hft_0272913f9415bf5d2558","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_topographic_orchard","source_type":"hft","support_ids":["sup_60b3b1d27e1f81999199"],"title":"baseline_topographic_orchard","trust":"legacy_unbound"},{"anchor_refs":["88:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:10","branch_refs":["root_000266/B001","root_000266/B008","root_001042/B002"],"candidate_id":"cand_ec76527ea9d12c6a4987","commentary_obligation":"review","hft_ref":"hft_4435263aa63f61a43dc1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_sheltered_high_rank","source_type":"hft","support_ids":["sup_9698ebdaa2dd3e82a738"],"title":"baseline_sheltered_high_rank","trust":"legacy_unbound"},{"anchor_refs":["88:10"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:10","branch_refs":["root_000266/B011","root_001042/B010"],"candidate_id":"cand_831c1c10c985a90aeebb","commentary_obligation":"review","hft_ref":"hft_b8f25d3ebf1540ac76f0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_self_rising_growth","source_type":"hft","support_ids":["sup_f3f9cb1403b2445d7df4"],"title":"baseline_self_rising_growth","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:10:1:1","qac_word_ref":"88:10:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","root_ar":"ج ن ن","surface_ar":"جَنَّةٍ"},{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","root_ar":"ع ل و","surface_ar":"عَالِيَةٍ"}],"word_analysis_qac_refs":[["88:10:1:1"],["88:10:2:1"],["88:10:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:10:1","88:10:2","88:10:3"]},"focus_surface_evidence":{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"88:10:1:1","qac_word_ref":"88:10:1","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"جَنَّة","morph_features":"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:10:2:1","qac_word_ref":"88:10:2","root_ar":"ج ن ن","surface_ar":"جَنَّةٍ"},{"lemma_ar":"عَالِيَة","morph_features":"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:10:3:1","qac_word_ref":"88:10:3","root_ar":"ع ل و","surface_ar":"عَالِيَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:10:1:1"],["88:10:2:1"],["88:10:3:1"]],"word_analysis_refs":["88:10:1","88:10:2","88:10:3"],"word_rows":[{"analysis_record_ref":"88:10:1","analytic_gloss_range_en":"rootless preposition governing the following genitive noun; locally a predicative locative or state-domain frame for the carried blessed group","analytic_root_gloss_range_en":null,"qac_refs":["88:10:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"88:10:2","analytic_gloss_range_en":"indefinite singular genitive garden: a concrete, covered afterlife reward-space governed by the preposition and qualified by the height adjective","analytic_root_gloss_range_en":"broad root range includes covering, concealment, tree-covered garden, hidden afterlife garden, protective cover, hidden beings, mental covering, womb-hidden life, burial, and other cover-related branches; the local noun selects garden/refuge and narrows unrelated branches","qac_refs":["88:10:2:1"],"root":{"arabic":"ج ن ن","transliteration":"j-n-n"},"surface":{"arabic":"جَنَّةٍ","transliteration":"jannatin"}},{"analysis_record_ref":"88:10:3","analytic_gloss_range_en":"feminine singular genitive active-participial adjective modifying the garden; locally lofty or elevated in place and rank, without becoming a superlative, independent predicate, active conquest, or narrated raising","analytic_root_gloss_range_en":"broad root range includes physical height, rising, high rank, haughty domination, overcoming, upper direction, coming up, elevated places, and other specialized branches; the local adjective selects achieved elevation as a garden-quality","qac_refs":["88:10:3:1"],"root":{"arabic":"ع ل و","transliteration":"ʿ-l-w"},"surface":{"arabic":"عَالِيَةٍۢ","transliteration":"ʿāliyatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:10"],"branch_refs":["root_000266/B003","root_001042/B001"],"candidate_id":"cand_968ccc94923129f4bf92","evidence_scope":"focus_ayah","hft_ref":"hft_0272913f9415bf5d2558","item_id":"baseline_topographic_orchard","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_topographic_orchard","support_id":"sup_60b3b1d27e1f81999199"},{"anchor_refs":["88:10"],"branch_refs":["root_000266/B001","root_000266/B008","root_001042/B002"],"candidate_id":"cand_ec76527ea9d12c6a4987","evidence_scope":"focus_ayah","hft_ref":"hft_4435263aa63f61a43dc1","item_id":"baseline_sheltered_high_rank","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_sheltered_high_rank","support_id":"sup_9698ebdaa2dd3e82a738"},{"anchor_refs":["88:10"],"branch_refs":["root_000266/B011","root_001042/B010"],"candidate_id":"cand_831c1c10c985a90aeebb","evidence_scope":"focus_ayah","hft_ref":"hft_b8f25d3ebf1540ac76f0","item_id":"baseline_self_rising_growth","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_self_rising_growth","support_id":"sup_f3f9cb1403b2445d7df4"}],"diagnostics":[],"lane_counts":{"global":14,"macro":4,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:10","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:10","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"88:10","lane":"micro","linguistic_source_ref":"88:10","surface_ref":"88:10","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:10","target_tokens":[["Yüksek",["88:10:3"]],["bir",["88:10:2"]],["bahçededir",["88:10:1","88:10:2"]]],"text":"Yüksek bir bahçededir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:high-garden-reversal","source_type":"word_analysis","support_id":"sup_08d4681691ac70b0a7a0","text":"{\"blocking_evidence\":null,\"headline\":\"high-garden reversal of exposure\",\"reader_payoff\":\"The reader notices that the garden joins an exact high-garden formula at 69:22 while reversing the punitive environment of 88:4-7.\",\"reason\":\"The CRITICAL rows supply the formula echo at 69:22 and the local contrast with 88:4-7; attachment evidence supports this as the ayah's environment phrase.\",\"representative_source_ids\":[\"QI-c97ea3df\",\"QE-7119d319\",\"ME-dae79c09\",\"QY-79fc71b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:spatial-and-rank-elevation","source_type":"word_analysis","support_id":"sup_10053af0bb2bc0d41a86","text":"{\"blocking_evidence\":null,\"headline\":\"spatial height with rank\",\"reader_payoff\":\"The reader notices that the reward is lifted both as vertical imagery and as superior rank.\",\"reason\":\"V4 supports physical height and high-rank branches for {{ar:ع ل و}} ({{tr:ʿ-l-w}}), and the local adjective can carry both without forcing only one.\",\"representative_source_ids\":[\"QS-06da33b4\",\"QS-6ad898af\",\"QS-b419ea19\",\"MS-a5f1ff82\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:10:3:1","source_type":"qac_morpheme","support_id":"sup_1374e9829a959f37527b","text":"{\"lemma_ar\":\"عَالِيَة\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|LEM:EaAliyap|ROOT:Elw|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"88:10:3:1\",\"qac_word_ref\":\"88:10:3\",\"root_ar\":\"ع ل و\",\"surface_ar\":\"عَالِيَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1","source_type":"word_analysis","support_id":"sup_19f682b407bc005c9a92","text":"{\"gloss_range\":\"rootless preposition governing the following genitive noun; locally a predicative locative or state-domain frame for the carried blessed group\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) begins the ayah by making placement the first fact after the satisfied striving of 88:9. Because the phrase has no finite verb or newly stated subject, the preposition carries a predicative load: the prior blessed group is now located inside the garden phrase, not merely shown a scene. Its range can include both physical interiority and a lived reward-state, so the word opens a surrounding domain before {{ar:جَنَّةٍ}} ({{tr:jannatin}}) names it. The bare preposition also introduces the domain that later inside-the-garden clauses can refer back to in 88:11-13, and it helps form the exact high-garden expression also found at 69:22. The slim long-vowel particle releases into the dense garden noun and the two indefinite genitives, so the sound enacts entry into enclosure while the transition remains settled rather than narrated as an act of entering.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2","source_type":"word_analysis","support_id":"sup_255fbea119e5fbef1f2e","text":"{\"gloss_range\":\"indefinite singular genitive garden: a concrete, covered afterlife reward-space governed by the preposition and qualified by the height adjective\",\"prose\":\"{{ar:جَنَّةٍ}} ({{tr:jannatin}}) is the middle word and structural hinge of the ayah: it is governed by {{ar:فِى}} ({{tr:fī}}) and then governs the attachment of {{ar:عَالِيَةٍۢ}} ({{tr:ʿāliyatin}}). Its indefiniteness keeps the reward-space open in scale and kind, while its singular form lets one garden stand as an integrated environment before the following verses unfold its interior. The root field of {{ar:ج ن ن}} ({{tr:j-n-n}}) gives more than scenery: V4 supports garden and afterlife-garden branches together with covering and protective-cover branches, so the noun can present a cultivated enclosure that shelters life like a screened refuge, not just a pleasant view. That covering pressure is narrowed by the local concrete garden noun: concealment becomes habitable shelter and protected interior life, not hidden beings, mental covering, burial, or other remote branches. The word also prepares the repeated inside-the-garden clauses of 88:11-13; unlike the gardens-under-rivers formula at 2:25, enclosure itself carries the first reward before any internal abundance is named. With the following adjective, it echoes the high-garden phrase at 69:22 and reverses the fire, scalding drink, and thorn-food of 88:4-7. Its dense doubled sound before the long-vowel adjective adds a secondary movement from enclosure toward elevation.\",\"root_display\":\"{{ar:ج ن ن}} ({{tr:j-n-n}})\",\"root_gloss_range\":\"broad root range includes covering, concealment, tree-covered garden, hidden afterlife garden, protective cover, hidden beings, mental covering, womb-hidden life, burial, and other cover-related branches; the local noun selects garden/refuge and narrows unrelated branches\",\"surface_display\":\"{{ar:جَنَّةٍ}} ({{tr:jannatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:sound-density-before-lift","source_type":"word_analysis","support_id":"sup_28b8443818bc6727bb7d","text":"{\"blocking_evidence\":null,\"headline\":\"dense sound before lift\",\"reader_payoff\":\"The reader notices a secondary sound movement from the dense doubled noun into the lifted adjective.\",\"reason\":\"The phonetic payoff is visible in the local surface and is kept secondary to the grammar and lexical sense.\",\"representative_source_ids\":[\"QP-29acb7e2\",\"QP-51ae8eb1\",\"MP-c500c32c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:carried-subject-continuity","source_type":"word_analysis","support_id":"sup_299a9b314a7b1b9d052e","text":"{\"blocking_evidence\":null,\"headline\":\"prior group carried into location\",\"reader_payoff\":\"The reader notices that the same satisfied group from 88:8-9 is being housed here without being renamed.\",\"reason\":\"The attachment layer notes a predicative locative phrase without an overt subject and recommends reading the prior discourse window.\",\"representative_source_ids\":[\"QG-ac98ca07\",\"QG-e92a668a\",\"QB-ed15265a\",\"QY-8d3f0430\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:achieved-elevation-not-raising-act","source_type":"word_analysis","support_id":"sup_31e8b738fdfac91b81b9","text":"{\"blocking_evidence\":null,\"headline\":\"achieved elevation, not raising\",\"reader_payoff\":\"The reader notices elevation as an achieved quality of this garden while causative raising branches remain background rather than local action.\",\"reason\":\"V4 includes raising and related branches, but the local feminine adjective is grammatically adapted to the garden and does not narrate a causative event.\",\"representative_source_ids\":[\"QS-ca394356\",\"QF-7c542291\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:branch-boundaries","source_type":"word_analysis","support_id":"sup_3aef6f5cf5e11f9fb852","text":"{\"blocking_evidence\":null,\"headline\":\"covering field bounded by the noun\",\"reader_payoff\":\"The reader notices that concealment becomes habitable shelter here, while hidden beings, mental disturbance, and other cover-branches do not replace the garden sense.\",\"reason\":\"The broad root family is real, but QAC marks the local word as a concrete noun and V4 separates garden/refuge branches from hidden-being and mental-covering branches.\",\"representative_source_ids\":[\"QS-a3a029ae\",\"QS-ce917be6\",\"QF-13a3df3f\",\"QF-3be68b51\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:predicative-locative-frame","source_type":"word_analysis","support_id":"sup_4168ac247d4704f41006","text":"{\"blocking_evidence\":null,\"headline\":\"locative predicate leads the clause\",\"reader_payoff\":\"The reader notices that reward first appears as being placed inside a settled environment rather than as a narrated movement.\",\"reason\":\"QAC and attachment evidence identify {{ar:فِى}} ({{tr:fī}}) as a preposition governing the genitive garden noun in a verbless locative phrase.\",\"representative_source_ids\":[\"QG-51470373\",\"MG-1a6bb7f4\",\"QT-410fdf37\",\"MT-e5d743dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:domain-introduction-before-pronominal-return","source_type":"word_analysis","support_id":"sup_47a9c6030d000ab15287","text":"{\"blocking_evidence\":null,\"headline\":\"named domain before later return\",\"reader_payoff\":\"The reader notices that the garden domain is introduced here before later clauses can refer back to it from inside (88:11-13).\",\"reason\":\"The local wording uses bare {{ar:فِى}} ({{tr:fī}}) before an explicit noun, while the CRITICAL row points to later pronominal return.\",\"representative_source_ids\":[\"QF-a02f102d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:indefinite-singular-environment","source_type":"word_analysis","support_id":"sup_4e606b9a2b705cb11578","text":"{\"blocking_evidence\":null,\"headline\":\"open singular reward-space\",\"reader_payoff\":\"The reader notices one integrated garden-environment whose indefinite form keeps its magnitude and kind open.\",\"reason\":\"QAC identifies an indefinite feminine singular genitive noun; nothing in the guardrails requires a named site or pluralized reward.\",\"representative_source_ids\":[\"QG-8076c87d\",\"MG-26254a75\",\"QF-662d21e2\",\"QF-f879f4f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:covered-protective-garden","source_type":"word_analysis","support_id":"sup_6b95dc23f5be0cfc73fa","text":"{\"blocking_evidence\":null,\"headline\":\"covered garden as refuge\",\"reader_payoff\":\"The reader notices the garden as a cultivated enclosure that shelters, not merely a decorative landscape.\",\"reason\":\"V4 supports tree-covered garden, hidden afterlife garden, covering, and protective-cover branches; the local noun keeps that pressure inside the garden/refuge sense rather than activating every root branch.\",\"representative_source_ids\":[\"QS-30f8670f\",\"QS-50ddfcfe\",\"QS-8b9ed59e\",\"MS-fa877917\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:governed-head-hinge","source_type":"word_analysis","support_id":"sup_6c9b2e8910852c7e33c1","text":"{\"blocking_evidence\":null,\"headline\":\"garden as governed hinge\",\"reader_payoff\":\"The reader notices that the garden is not a detached subject; it mediates between the preposition before it and the height adjective after it.\",\"reason\":\"Attachment evidence marks {{ar:جَنَّةٍ}} ({{tr:jannatin}}) as the genitive complement of {{ar:فِى}} ({{tr:fī}}) and the head modified by the agreeing adjective.\",\"representative_source_ids\":[\"QG-488ca55c\",\"QG-7e666a57\",\"QG-8ae7b710\",\"QT-f2caa754\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:reward-setting-after-satisfaction","source_type":"word_analysis","support_id":"sup_6f8cbd8c9aa4f9896f52","text":"{\"blocking_evidence\":null,\"headline\":\"satisfaction answered by elevation\",\"reader_payoff\":\"The reader notices that the approved inner state from 88:9 is answered by an outwardly raised place in 88:10.\",\"reason\":\"The discourse window carries the prior subject into this locative phrase, and the CRITICAL rows identify elevation as the environmental confirmation of that state.\",\"representative_source_ids\":[\"ME-3c74a512\",\"QB-4c57a45f\",\"QB-6c6eba42\",\"QB-86626977\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:bounded-root-branches","source_type":"word_analysis","support_id":"sup_77849b472f688522c163","text":"{\"blocking_evidence\":null,\"headline\":\"loftiness without conquest\",\"reader_payoff\":\"The reader notices exalted loftiness while active dominance, self-assertive superiority, and root-dispute overreach are kept outside the local garden adjective.\",\"reason\":\"The broad root includes rank, domination, and mastery branches, but local agreement with the garden as an adjective restrains those branches into superior setting rather than active conquest.\",\"representative_source_ids\":[\"QS-1456f552\",\"QS-b09988d9\",\"QS-f30e3a4f\",\"QS-f61f0dd4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:boundary-from-satisfaction-to-shelter","source_type":"word_analysis","support_id":"sup_b170bc059980308737ea","text":"{\"blocking_evidence\":null,\"headline\":\"satisfaction housed as shelter\",\"reader_payoff\":\"The reader notices that inward satisfaction from 88:9 becomes an outward sheltered environment in 88:10.\",\"reason\":\"The attachment layer permits the prior blessed group to be carried into this phrase, and the CRITICAL rows identify the boundary movement from inner condition to environment.\",\"representative_source_ids\":[\"MT-b83d554b\",\"QB-040b4a76\",\"QB-2cf7ec83\",\"QY-1c98bb1f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:stable-participial-quality","source_type":"word_analysis","support_id":"sup_b5f1d42661a0be0970ee","text":"{\"blocking_evidence\":null,\"headline\":\"stable quality, not event\",\"reader_payoff\":\"The reader notices that the garden is presented as already lofty, not as undergoing a narrated ascent.\",\"reason\":\"The local form is tagged as a noun active participle used adjectivally, and contextual data supports adjective deployment for this form class.\",\"representative_source_ids\":[\"QF-4d4eda78\",\"QF-f3d10d56\",\"MF-7361a5c6\",\"QI-3e00b000\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:interiority-as-state-domain","source_type":"word_analysis","support_id":"sup_c050b4c58e1f19e17915","text":"{\"blocking_evidence\":null,\"headline\":\"inside a place and condition\",\"reader_payoff\":\"The reader notices that the preposition makes the garden a surrounding lived condition, not only a backdrop viewed from outside.\",\"reason\":\"The local prepositional construction licenses interior location, while the broader clause relation allows a state-domain reading without replacing the locative sense.\",\"representative_source_ids\":[\"QG-30b1e292\",\"QS-42a6768a\",\"QS-a1231617\",\"QB-dff2f78c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:10:2:1","source_type":"qac_morpheme","support_id":"sup_c32eab9e8f4633ddce45","text":"{\"lemma_ar\":\"جَنَّة\",\"morph_features\":\"STEM|POS:N|LEM:jan~ap|ROOT:jnn|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:10:2:1\",\"qac_word_ref\":\"88:10:2\",\"root_ar\":\"ج ن ن\",\"surface_ar\":\"جَنَّةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:open-quality-not-superlative","source_type":"word_analysis","support_id":"sup_cf24a92cb16e75663cc2","text":"{\"blocking_evidence\":null,\"headline\":\"lofty, not ranked highest\",\"reader_payoff\":\"The reader notices an expansive qualitative elevation rather than a fixed title or explicit highest-rank comparison.\",\"reason\":\"The adjective is indefinite and active-participial rather than definite, comparative, or superlative.\",\"representative_source_ids\":[\"QG-0757871d\",\"QF-9c6ffd08\",\"QF-f58ed6ab\",\"QS-663ab93a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:2:whole-domain-unpacked-later","source_type":"word_analysis","support_id":"sup_cf5d30974ce9cdc64b5b","text":"{\"blocking_evidence\":null,\"headline\":\"garden named before interior unpacking\",\"reader_payoff\":\"The reader notices that this single noun introduces the reward domain that 88:11-13 will unfold from inside.\",\"reason\":\"The CRITICAL rows give concrete continuation references, and the local noun is the only named domain available for those later inside-the-garden clauses.\",\"representative_source_ids\":[\"QS-68a27e9e\",\"MT-68a2a557\",\"QB-9de5d9f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:final-high-garden-formula","source_type":"word_analysis","support_id":"sup_d0b727638740ea637878","text":"{\"blocking_evidence\":null,\"headline\":\"final word seals formula\",\"reader_payoff\":\"The reader notices that the ayah ends on height, completing the exact high-garden phrase also found at 69:22.\",\"reason\":\"The CRITICAL rows give the exact phrase echo at 69:22 and locate this adjective as the closing qualifier of 88:10.\",\"representative_source_ids\":[\"QI-cc3ef9f8\",\"MI-07f88772\",\"QT-cb1e3af6\",\"QE-4ee6e813\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3","source_type":"word_analysis","support_id":"sup_d5a82002c1e23c702a10","text":"{\"gloss_range\":\"feminine singular genitive active-participial adjective modifying the garden; locally lofty or elevated in place and rank, without becoming a superlative, independent predicate, active conquest, or narrated raising\",\"prose\":\"{{ar:عَالِيَةٍۢ}} ({{tr:ʿāliyatin}}) closes the ayah by lifting the garden phrase itself. Its agreement with {{ar:جَنَّةٍ}} ({{tr:jannatin}}) makes elevation belong to the garden, not to a separate actor or independent predicate. The root field of {{ar:ع ل و}} ({{tr:ʿ-l-w}}) supports both spatial height and high rank, so the reward is vertically lifted and evaluatively superior at once; the documented ʿ-l-w versus ʿ-l-y analysis stays within that height and exaltedness family rather than changing the local adjective. The local active-participial adjective presents that elevation as a stable quality already attached to the place, not a narrated act of rising or raising. Because the form is indefinite and not comparative or superlative, it classifies the garden as expansively lofty rather than highest or technically titled; because it modifies the garden, haughty domination and active conquest branches are narrowed into superior setting. As the final word, it seals the exact high-garden phrase echoed at 69:22, gives the phrase an audible long-vowel rise after the dense garden noun, and turns the prior satisfaction into an outwardly elevated reward-space.\",\"root_display\":\"{{ar:ع ل و}} ({{tr:ʿ-l-w}})\",\"root_gloss_range\":\"broad root range includes physical height, rising, high rank, haughty domination, overcoming, upper direction, coming up, elevated places, and other specialized branches; the local adjective selects achieved elevation as a garden-quality\",\"surface_display\":\"{{ar:عَالِيَةٍۢ}} ({{tr:ʿāliyatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:high-garden-formula","source_type":"word_analysis","support_id":"sup_e15895eebfa0a4570582","text":"{\"blocking_evidence\":null,\"headline\":\"high-garden formula opened\",\"reader_payoff\":\"The reader notices that this opening preposition participates in the exact high-garden reward phrase also found at 69:22.\",\"reason\":\"The CRITICAL row supplies the concrete echo at 69:22; nothing in the guardrail evidence contradicts the formulaic comparison.\",\"representative_source_ids\":[\"QE-fb73411a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:1:compact-sound-entry","source_type":"word_analysis","support_id":"sup_ea81b14f122587f55b81","text":"{\"blocking_evidence\":null,\"headline\":\"compact sound enters enclosure\",\"reader_payoff\":\"The reader notices the short opening particle leading into the denser garden word as a secondary sound-payoff of entry into enclosure.\",\"reason\":\"The sound claim is limited to visible surface cadence and does not introduce an independent lexical sense.\",\"representative_source_ids\":[\"QP-33466339\",\"QP-7b2bd6b5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:agreeing-adjective-bound-to-garden","source_type":"word_analysis","support_id":"sup_eeae6d813918654c2924","text":"{\"blocking_evidence\":null,\"headline\":\"height bound to the garden\",\"reader_payoff\":\"The reader notices that elevation belongs to the garden phrase itself, not to a separate inhabitant or new predicate.\",\"reason\":\"QAC and attachment evidence mark the word as a feminine singular genitive adjective modifying {{ar:جَنَّةٍ}} ({{tr:jannatin}}).\",\"representative_source_ids\":[\"QG-1fc1e63b\",\"QG-6dc0b247\",\"MG-8285dfda\",\"QF-5647ef52\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:10:3:sound-lift","source_type":"word_analysis","support_id":"sup_fd9412627333ecf6ef7b","text":"{\"blocking_evidence\":null,\"headline\":\"open vowel lift\",\"reader_payoff\":\"The reader notices a secondary auditory rise as the phrase opens into the long vowel of the final adjective.\",\"reason\":\"The sound observation is tied to the visible local surface and kept subordinate to grammar and lexical sense.\",\"representative_source_ids\":[\"QP-b557ed0d\",\"QP-baae4222\",\"MP-5cd8f568\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B003","root_001042/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000266","role":"The covered orchard supplies the concrete enclosure that serves as the adjective's locus.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001042","role":"Physical rising supplies direct vertical elevation to the enclosed garden.","root":"ع ل و","source_ref":"88:10","source_word_indices":["3"]}],"changed_reading":{"after":"A canopied orchard-like enclosure situated high or rising above its surroundings.","before":"An unspecified garden."},"confidence":"strong","focus_anchor":"The noun at word 2 is modified by the feminine adjective at word 3 inside a locative construction.","mechanism":"A tree-covered enclosure is located on, or itself forms, elevated terrain.","model_id":"baseline_topographic_orchard"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_topographic_orchard","source_type":"hft","support_id":"sup_60b3b1d27e1f81999199","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B001","root_000266/B008","root_001042/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000266","role":"Concealment supplies an interior kept from exposure and ordinary perception.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_000266","role":"Protective covering turns enclosure into refuge rather than mere visual hiding.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001042","role":"Noble rank makes elevation a quality of the abode and its occupants.","root":"ع ل و","source_ref":"88:10","source_word_indices":["3"]}],"changed_reading":{"after":"A protected interior distinguished by high worth and dignity, whether or not altitude is foregrounded.","before":"A garden at a high location."},"confidence":"medium","focus_anchor":"The concealment potential of the noun at word 2 coexists with the rank potential of the adjective at word 3.","mechanism":"The place encloses and protects, while its highness marks qualitative dignity rather than only altitude.","model_id":"baseline_sheltered_high_rank"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_sheltered_high_rank","source_type":"hft","support_id":"sup_9698ebdaa2dd3e82a738","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000266/B011","root_001042/B010"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_000266","role":"Vigorous interwoven growth supplies a living mass that can produce height.","root":"ج ن ن","source_ref":"88:10","source_word_indices":["2"]},{"branch_id":"B010","mapped_root_id":"root_001042","role":"Tall, large-bodied form gives the vegetation a vertically expansive build.","root":"ع ل و","source_ref":"88:10","source_word_indices":["3"]}],"changed_reading":{"after":"A garden whose thick, towering life makes it high from within.","before":"A garden placed somewhere high."},"confidence":"exploratory","focus_anchor":"The garden noun can profile vigorous interwoven vegetation, and its adjective can profile tall, large-bodied form.","mechanism":"The enclosure is high because its own dense growth thrusts upward; elevation is generated internally by vegetation rather than supplied only by external terrain.","model_id":"baseline_self_rising_growth"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_self_rising_growth","source_type":"hft","support_id":"sup_f3f9cb1403b2445d7df4","trust":"legacy_unbound"}]}
</lane_packet_json>
