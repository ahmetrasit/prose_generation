# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:17**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_17/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:17",
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
{"branch_registry":[{"boundary":"Anlam yalnızca uzak durmayı değil, somut bir yanı, yan bölgeyi veya ona bitişik çevreyi bildirir.","branch_kind":"bare","branch_ref":"root_000262/B001","candidate_links":[{"candidate_id":"cand_13684e2604e7488c4c6a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"bedenin veya şeyin yanı ve bitişik çevresi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya hayvan bedeninin böğrünü ve bir şeyin yanını ya da tarafını belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir evin veya topluluğun yerleşimine bitişik yakın çevreyi belirtebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Vadi, ordu veya ırmak gibi bir bütünün iki yanından her birini belirtir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Devenin böğründen alınan ve kap yapımında kullanılabilen deri parçasını belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedenin böğrü, bir nesnenin tarafı ve o tarafa bitişik yakın alan birlikte kastedildiğinde en uygun karşılıktır.","boundary_detail":"Anlam yalnızca uzak durmayı değil, somut bir yanı, yan bölgeyi veya ona bitişik çevreyi bildirir.","branch_image_ar":"الجنب جانب الجسد وناحية الشيء","concept_gloss":"bedenin veya şeyin yanı ve bitişik çevresi","contextual_glosses":[{"applicability":"Vadi, ordu veya ırmak gibi iki taraflı düşünülen yapıların karşılıklı yanları için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı bir bütünün karşılıklı yanlarını eksiksiz belirtir."},"facet_ids":["F003"],"text":"iki yan","usage_role":"contextual"}],"definition":"İnsan ya da hayvan gövdesinin böğrü veya herhangi bir şeyin yanı ve bu yana bitişik yakın çevredir. İki yandan oluşan düzenlerde her bir yanı, ayrıca böğürden alınan deri parçasını da adlandırabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya hayvan bedeninin böğrünü ve bir şeyin yanını ya da tarafını belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir evin veya topluluğun yerleşimine bitişik yakın çevreyi belirtebilir."},{"facet_id":"F003","role":"specialization","statement":"Vadi, ordu veya ırmak gibi bir bütünün iki yanından her birini belirtir."},{"facet_id":"F004","role":"specialization","statement":"Devenin böğründen alınan ve kap yapımında kullanılabilen deri parçasını belirtir."}],"identity_rationale":"Kaynak ifadesi insanın veya hayvanın böğrünü, bir şeyin yanını ve bu temel anlamdan gelişen bitişik çevreyi birlikte doğrular. Vadi ve ordu gibi yapıların iki yanı ile böğürden alınan deri parçası, aynı yan bölge çekirdeğinin belirli uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanın veya hayvanın böğrü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yan, taraf"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"evin önü veya topluluğun yerleşimine bitişik çevre"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"vadinin, ordunun veya ırmağın iki yanı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"devenin böğür derisinden alınan parça"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"ordunun sağ ve sol kanadı"}],"lexicalization_note":"Dal yalın kullanıma dayanır; tanım, özel bir söz öbeğine bağlı anlamları çekirdeğe katmadan yan ve bitişik çevre alanını kapsar.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yan ve taraf alanındaki en güçlü sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yön ve çevresel uçlar üzerinden tarafı anlatırken bu dal beden böğrünü temel alır ve bitişik çevre ile deri parçasına uzanır.","focus_only":"Bedenin böğrünü, yerleşime bitişik çevreyi ve böğürden alınan deri parçasını da kapsar.","gloss":"yan ve taraf","neighbor_only":"Dağ veya at gibi varlıkların yüksek ve dışa uzanan uçlarını da kapsar.","neighbor_ref":"root_001238/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yanını veya tarafını adlandırabilir."}],"source_phrase_ar":"أصل الجنب الجارحة وجمعه جنوب (mufradat)؛ الجنب للإنسان وغيره (maqayis)؛ الجانب والجوانب معروفة والجنبتان ناحيتا كل شيء (ayn)؛ الجنب معروف والجانب الناحية (sihah)؛ جنبتا الوادي ناحيتاه وجناب القوم ما حولهم (tahdhib)؛ جنب الإنسان والدابة معروف وأعطني جنبة جلد جنب بعير (jamhara)","source_summary":"Anlamın ortak çekirdeği bedenin veya bir nesnenin yanıdır. Yakın çevre, iki yandan biri ve böğür derisinden alınan parça bu mekansal çekirdeğin belirli uzantılarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنب الإنسان والدابة، والجانب والناحية، وجنبتا الوادي أو العسكر أو النهر، وجناب الدار والقوم وما قرب من محلتهم، وما يؤخذ من جلد الجنب.","what_is_not_ar":"لا يدخل فيه مجرد البعد والاجتناب ولا الجنوب الريح ولا الأعلام كجنب الحي وجناب الموضع."},"support_links":["sup_f71a62865a6b271f833c"]},{"boundary":"Yakınlık çekirdeği ile belirli söz öbeklerinin buyruk, yol veya bir kimse hakkındaki anlamları ayrı tutulmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"yanında yakın bulunma ve eşlik etme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseye yakın olmayı, yanında bulunmayı veya kolayca yaklaşılabilir olmayı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolculukta bir kimsenin yanında bulunan eşlikçiyi belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli dinsel yapılarda yakınlık yanında buyruk, iş veya izlenen yol anlamını taşır."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaklaşılabilirlik, yan yana bulunma ve eşlik etme çekirdeğinin birlikte anlatılması gerektiğinde kullanılır.","boundary_detail":"Yakınlık çekirdeği ile belirli söz öbeklerinin buyruk, yol veya bir kimse hakkındaki anlamları ayrı tutulmalıdır.","branch_image_ar":"الجنب قرب ومجاورة على الجانب","concept_gloss":"yanında yakın bulunma ve eşlik etme","contextual_glosses":[{"applicability":"Yolculuk sırasında kişinin yanında bulunan ve ona eşlik eden kimse için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolculuk bağlamındaki yakın eşlik ilişkisini tam olarak korur."},"facet_ids":["F002"],"text":"yol arkadaşı","usage_role":"contextual"}],"definition":"Bir kimseye yanından yakın olma, kolayca yaklaşabilme veya ona eşlik etme ilişkisidir. Belirli yapılarda bu mekansal yakınlık, bir buyruğa ya da yola bağlılık anlamına kayar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseye yakın olmayı, yanında bulunmayı veya kolayca yaklaşılabilir olmayı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Yolculukta bir kimsenin yanında bulunan eşlikçiyi belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli dinsel yapılarda yakınlık yanında buyruk, iş veya izlenen yol anlamını taşır."}],"identity_rationale":"Kaynak ifadesi yumuşak yaklaşılabilirliği ve yolda eşliği gerçekten yakınlık çekirdeğine bağlar; ancak Tanrı ile ilgili yapılarda yakınlık yanında buyruk, iş ve yol yorumları da vardır. Bu nedenle dal korunur, fakat her yapının yalnızca fiziksel komşuluk diye genellenmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yaklaşması ve ilişki kurması kolay"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yol arkadaşı veya yakın eşlikçi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'ya yakınlıkta veya Tanrı'nın buyruğu ve yolu üzerinde"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kardeşin hakkında, özellikle onu çekiştirme konusunda"}],"lexicalization_note":"Dal hem yan üzerinden kurulan yakınlık çekirdeğini hem de belirli yapılara bağlı anlamları içerir; bu yapılar yalın anlama genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel komşulukla örtüşme ve aynı kökteki karşıt uzaklaşma yönü en açıklayıcı iki sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel komşuluk düzenini anlatır; bu dal ise yan yana bulunma imgesinden gelişen kişisel yaklaşılabilirlik ve eşlik ilişkisine odaklanır.","focus_only":"Yaklaşılabilir kişiliği, yol arkadaşlığını ve belirli yapılardaki buyruk ya da yol anlamını içerir.","gloss":"yakınlık ve komşuluk","neighbor_only":"Yerleşimlerin, toprak parçalarının ve eşlerin komşuluğunu genel biçimde kapsar.","neighbor_ref":"root_000275/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da yakın bulunma ve komşu olma ilişkisini anlatır."},{"boundary_match":"opposed","distinction":"Bu dal yakınlık ve eşlik kutbunu, komşu dal ise mesafe koyma ve ayrı kalma kutbunu gerçekleştirir.","focus_only":"Yakınlaşma, yanında bulunma ve eşlik etme yönünü taşır.","gloss":"yakın durma ve uzak durma","neighbor_only":"Uzaklaşma, kaçınma, ayırma ve yabancılık yönünü taşır.","neighbor_ref":"root_000262/B003","relation_type":"polarity_pair","shared_zone":"İki dal da kişiler veya şeyler arasındaki göreli mesafe ve ilişki eksenindedir."}],"source_phrase_ar":"رجل لين الجانب والجنب أي سهل القرب (ayn;tahdhib)؛ الصاحب بالجنب صاحبك في السفر (sihah)؛ الجنب القرب وفي قرب الله وجواره (tahdhib)؛ في أمره وحده الذي حده لنا (mufradat)","source_summary":"Yakınlık ve yanında bulunma, kolay yaklaşılabilen kişi ile yol arkadaşını açıklayan ortak çekirdektir. Belirli dinsel söyleyişlerde aynı yapı mekansal yakınlığın ötesine geçerek buyruk, iş veya yol ilişkisini anlatır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القرب والجوار والمصاحبة من جهة الجنب، مثل الصاحب بالجنب، لين الجانب أو الجنب، وما فسرته المصادر في جنب الله بالقرب أو الجوار أو الأمر أو الطريق.","what_is_not_ar":"لا يدخل فيه الغريب الأجنبي والجار الجنب إذا أريد به البعيد من غير قومك، ولا الجنابة الشرعية."},"support_links":[]},{"boundary":"Dal yakın komşuluğu değil, kişinin uzak durmasını, başkasını uzaklaştırmasını veya uzaklık sonucu yabancı kalmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B003","candidate_links":[{"candidate_id":"cand_be84f0bc12bd73f104ee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"uzak durma veya uzaklaştırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin bir şeyden uzaklaşmasını, ona yaklaşmamasını veya onu bırakmasını belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseyi bir şeyden uzaklaştırmayı veya kötülüğü ondan savmayı belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanlardan ayrı bir yerde durma ve yalnız kalma durumuna uzanır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Akrabalık, soy veya yerleşim bakımından uzak olan yabancı kişiyi belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin kendisinin mesafe koymasını hem de bir başkasını bir şeyden uzak tutmayı kapsayan genel karşılıktır.","boundary_detail":"Dal yakın komşuluğu değil, kişinin uzak durmasını, başkasını uzaklaştırmasını veya uzaklık sonucu yabancı kalmasını anlatır.","branch_image_ar":"المجانبة إبعاد واعتزال وغربة","concept_gloss":"uzak durma veya uzaklaştırma","contextual_glosses":[{"applicability":"Bir kişinin topluluktan çekilip ayrı bir yerde kalması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluktan ayrılma ve ayrı yerde kalma anlamını korur."},"facet_ids":["F003"],"text":"insanlardan ayrı durma","usage_role":"contextual"},{"applicability":"Soy veya yerleşim yakınlığı bulunmayan bir kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soy veya yer bakımından uzak ve yabancı olma sonucunu korur."},"facet_ids":["F004"],"text":"akrabalığı bulunmayan yabancı","usage_role":"contextual"}],"definition":"Bir kişi veya şeyle araya mesafe koymak, ondan uzak durmak ya da birini ondan uzaklaştırmaktır. Bu ayrılma kötülükten korunma, insanlardan ayrı yaşama veya soy ve yer bakımından yabancı olma sonucunu da doğurabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin bir şeyden uzaklaşmasını, ona yaklaşmamasını veya onu bırakmasını belirtir."},{"facet_id":"F002","role":"core","statement":"Bir kimseyi bir şeyden uzaklaştırmayı veya kötülüğü ondan savmayı belirtir."},{"facet_id":"F003","role":"extension","statement":"İnsanlardan ayrı bir yerde durma ve yalnız kalma durumuna uzanır."},{"facet_id":"F004","role":"extension","statement":"Akrabalık, soy veya yerleşim bakımından uzak olan yabancı kişiyi belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeyden uzaklaşmayı, onu bırakmayı, birini ondan uzaklaştırmayı, kötülüğü savmayı, insanlardan ayrı durmayı ve akrabalık ya da yerleşim bakımından yabancı olmayı açıkça aynı uzaklık alanında toplar. Etken ve edilgen katılımcı yönleri tanımda ayrı tutulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzak durmak, sakınmak veya bırakmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birini bir şeyden uzaklaştırmak veya kötülükten korumak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"beni ve çocuklarımı putlara tapmaktan uzak tut"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanlardan ayrı bir yerde durma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"akrabalıkta, soyda veya yerleşimde uzak olan yabancı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başka bir topluluktan gelip akrabalığı bulunmayan komşu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"uzaktan ve yabancı olarak"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birini iyilikten yoksun bırakmak"}],"lexicalization_note":"Yalın uzaklık alanı ile belirli yapılardaki kaçınma, koruma ve yabancılık kullanımları ayrıştırılır; yapı anlamları bütüne yayılmaz.","neighbor_coverage_note":"Bütün komşular incelendi; genel uzaklık ve tek başına kalma dalları çekirdeğin sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve özellikle yurt merkezli uzaklığa yayılır; bu dal ise bilinçli kaçınma, uzaklaştırma ve yakınlık bağının kesilmesini çekirdek alır.","focus_only":"Kaçınmayı, birini kötülükten uzak tutmayı ve soyca yabancı olmayı da kapsar.","gloss":"uzaklaşma ve yabancılık","neighbor_only":"Yurttan uzak kalmayı, sürgünü, uzaktan gelen haberi ve av köpeklerinin uzun takibini de kapsar.","neighbor_ref":"root_001077/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da uzaklık, ayrılma ve yabancı kalma durumlarını kapsar."},{"boundary_match":"partial","distinction":"Komşu dal tek başına bulunma durumuna odaklanır; bu dalın çekirdeği ise bir hedefe karşı mesafe koyma veya koydurmadır.","focus_only":"Bir şeyden sakınmayı, başkasını uzaklaştırmayı ve yabancılığı kapsar.","gloss":"ayrı durma","neighbor_only":"Bir topluluktan sapıp tek başına bir yerde veya gök cisminde bulunmayı kapsar.","neighbor_ref":"root_000305/B004","relation_type":"near_neighbor","shared_zone":"İki dal da topluluktan çekilme ve ayrı kalma durumunda buluşur."}],"source_phrase_ar":"الأصل الآخر البعد والجنابة (maqayis)؛ جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها (ayn)؛ الجناب مصدر جانبته مجانبة وهو من المباعدة (jamhara)؛ جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه (sihah)؛ أجنب تباعد والجنابة ضد القرابة (tahdhib)؛ جنبته عن كذا أي أبعدته واجتنبوا عبارة عن تركهم إياه (mufradat)","source_summary":"Ortak anlam mesafe koyma ve yakınlığı kesmedir. Kişinin kendisinin uzak durması, başka birini uzaklaştırması, kötülüğü savması, ayrı kalması ve yabancı sayılması bu çekirdeğin katılımcı ve sonuç çeşitleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جانبته وتجنبته واجتنبته، جنبته أو أجنبته عن الشيء أي أبعدته ونحيته، النجاة أو الدفع عن المكروه، الجنبة بمعنى الاعتزال، والأجنب أو الجنب بمعنى الغريب أو غير القريب في النسب والدار.","what_is_not_ar":"لا يدخل فيه القرب والمصاحبة إذا كان المراد جوارا وملازمة، ولا حالة الجنابة الشرعية إلا من جهة تعليلها بالبعد."},"support_links":["sup_c9904beb5653fc047bc7"]},{"boundary":"Dal genel uzaklık veya bedensel yan anlamını değil, cinsel ilişki sonrası arınmaya dek süren dinsel kısıtlılığı belirtir.","branch_kind":"bare","branch_ref":"root_000262/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"cinsel ilişki sonrası arınma gerektiren dinsel durum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Cinsel ilişki sonrasında arınma gerektiren ve kişiyi namazdan ve mescitten uzak tutan durumu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu durumda bulunan kadın, erkek veya birden çok kişiyi niteleyebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, kişinin arınana kadar namazdan ve mescitten uzak durmasıyla açıklanır."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Durumun sebebi, geçici dinsel kısıtı ve arınmayla sona ermesi birlikte anlatılmak istendiğinde kullanılır.","boundary_detail":"Dal genel uzaklık veya bedensel yan anlamını değil, cinsel ilişki sonrası arınmaya dek süren dinsel kısıtlılığı belirtir.","branch_image_ar":"الجنابة حالة تجنب مواضع الصلاة","concept_gloss":"cinsel ilişki sonrası arınma gerektiren dinsel durum","contextual_glosses":[{"applicability":"Cinsel ilişki sonrası geçici dinsel kısıt altında bulunan kişinin nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin arınma gerektiren geçici durumunu bağlam içinde korur."},"facet_ids":["F002"],"text":"arınması gereken kişi","usage_role":"contextual"}],"definition":"Cinsel ilişki sonrasında arınma yapılıncaya kadar kişinin namazdan ve mescitten uzak durduğu dinsel durumdur. Bu durumda bulunan kadın, erkek veya topluluk da aynı adlandırmayla nitelenebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Cinsel ilişki sonrasında arınma gerektiren ve kişiyi namazdan ve mescitten uzak tutan durumu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bu durumda bulunan kadın, erkek veya birden çok kişiyi niteleyebilir."},{"facet_id":"F003","role":"associated_use","statement":"Adlandırma, kişinin arınana kadar namazdan ve mescitten uzak durmasıyla açıklanır."}],"identity_rationale":"Kaynak ifadesi cinsel ilişki sonrasında oluşan dinsel durumu, bu durumdaki kişi ve toplulukları ve adlandırmanın arınmaya kadar belirli ibadetlerden ve yerlerden uzak durma gerekçesini açıkça destekler. Bu uzak durma genel kaçınma değil, belirli bir dinsel hükmün sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"cinsel ilişkiden sonra arınana dek dinsel kısıt altında bulunan kişi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"cinsel ilişki sonrası arınma gerektiren duruma girmek"}],"lexicalization_note":"Dal yalın bir dinsel durum ve bu durumdaki kişi anlamındadır; genel uzak durma anlamı tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; cinsel ilişkiden sürekli uzak durma dalı, bu geçici durumla karışma olasılığı en yüksek komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ilişkiye girmemeyi seçme veya sürdürme halidir; bu dal ise ilişki gerçekleştikten sonra arınmaya kadar doğan geçici dinsel durumdur.","focus_only":"Gerçekleşmiş cinsel ilişkiden sonra arınmaya kadar süren dinsel kısıtlılığı belirtir.","gloss":"cinsel ilişkiden uzak kalma","neighbor_only":"Evlilikten ve cinsel ilişkiden sürekli ya da iradi biçimde uzak durmayı belirtir.","neighbor_ref":"root_000082/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da cinsel ilişkiyle bağlantılı bir uzak durma durumuna değinir."}],"source_phrase_ar":"الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد (maqayis)؛ أجنب الرجل إذا أصابته الجنابة (ayn;jamhara;sihah;tahdhib)؛ رجل جنب وامرأة جنب وقوم جنب (jamhara;sihah;tahdhib)؛ سميت الجنابة بذلك لكونها سببا لتجنب الصلاة في حكم الشرع (mufradat)","source_summary":"Ortak tanım, cinsel ilişki sonrasında başlayan ve arınmaya kadar kişiyi namazdan ve mescitten uzak tutan durumdur. Durumun adı, bu uzak durmayla ilişkilendirilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه رجل أو امرأة أو قوم جنب، أصابته الجنابة، أجنب أو جنب أو اجتنب أو تجنب، وسبب التسمية بتجنب الصلاة أو مواضعها حتى الطهر.","what_is_not_ar":"لا يدخل فيه مطلق البعد أو الغربة، ولا الجنب الجارحة."},"support_links":[]},{"boundary":"Çekirdek, bir varlığı kişinin yanında bağlı veya yönlendirilmiş biçimde götürmektir; genel eşlikçilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B005","candidate_links":[{"candidate_id":"cand_5b909c34455ae4ceef13","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"yanında yönlendirerek götürme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hayvanı veya tutsağı kişinin kendi yanında yönlendirerek götürmesini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yanda çekilerek götürülen hayvanı veya hayvana bağlı götürülen tutsağı belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hayvan veya tutsağın kişinin yanında bağlı ya da yönlendirilmiş biçimde götürülmesini anlatır.","boundary_detail":"Çekirdek, bir varlığı kişinin yanında bağlı veya yönlendirilmiş biçimde götürmektir; genel eşlikçilik değildir.","branch_image_ar":"التجنيب قيادة شيء إلى الجنب","concept_gloss":"yanında yönlendirerek götürme","contextual_glosses":[{"applicability":"Binek olarak kullanılmadan bir kişinin yanında çekilerek götürülen hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanda ve bir yönlendiricinin denetiminde götürülmesini korur."},"facet_ids":["F002"],"text":"yanda çekilerek götürülen hayvan","usage_role":"contextual"}],"definition":"Bir hayvanı veya tutsağı kişinin kendi yanında, bağlı ya da yönlendirilmiş biçimde götürmesidir. Bu biçimde yanda götürülen hayvan veya bağlı tutsak da aynı anlam alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hayvanı veya tutsağı kişinin kendi yanında yönlendirerek götürmesini belirtir."},{"facet_id":"F002","role":"extension","statement":"Yanda çekilerek götürülen hayvanı veya hayvana bağlı götürülen tutsağı belirtir."}],"identity_rationale":"Yetkili dal ifadesi hayvanı veya tutsağı kişinin yanında götürmesini ve yanda götürülen varlığı destekler. Yarışta yedek at bulundurma yasağı yalnız ayrı bir sözcük biriminde tanıklanmıştır; bu nedenle dal tanımına kurucu anlam olarak alınmamış, yalnız o birimin karşılığında korunmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanı veya atı yanında yürütmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tutsağı yürütmek veya hayvanın yanına bağlamak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yanda çekilerek götürülen hayvan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yarış atının yanında yedek bir at koşturma yasağı"}],"lexicalization_note":"Yalın götürme çekirdeği ile hayvan, tutsak ve yarış bağlamındaki belirli birimler ayrı tutulur; yarış yasağı bütüne genellenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; atı yanda götürme ile bağ kullanarak çekme, işlemin sınırını en iyi gösteren iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnız atın yanda götürülmesine odaklanır; bu dal hayvanları ve tutsakları kapsayan daha geniş bir götürme düzenidir.","focus_only":"Hayvan yanında tutsak götürmeyi ve yanda götürülen varlığın adını da kapsar.","gloss":"atı yanda götürme","neighbor_only":"Özellikle bir atı binmeden yanda götürme biçimiyle sınırlıdır.","neighbor_ref":"root_001519/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir atı kişinin yanında, ona binmeden yönlendirerek götürmeyi kapsar."},{"boundary_match":"partial","distinction":"Komşu dal çekme aracına ve bağlı hayvana odaklanırken bu dal götürülen varlığın yönlendiricinin yanında bulunmasına odaklanır.","focus_only":"Yönlendirilen varlığın kişinin yanında götürülmesi konumunu kurucu sayar.","gloss":"bağla çekip götürme","neighbor_only":"Boyun ipini, yuları ve bu bağlarla çekilen hayvanı araç merkezli olarak kapsar.","neighbor_ref":"root_000235/B003","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanın bir bağ veya yönlendirme yoluyla götürülmesi sahnesini paylaşır."}],"source_phrase_ar":"جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير (maqayis;jamhara)؛ الجنيبة كل دابة تقاد والجنيب الأسير مشدود إلى جنب الدابة (ayn)؛ جنبت الدابة إذا قدتها إلى جنبك ومنه خيل مجنبة (sihah)؛ جنبت الفرس أجنبه جنبا إذا قدته والجنيبة الدابة تقاد (tahdhib)؛ من جنبت الفرس كأنما سأله أن يقوده عن جانب الشرك (mufradat)","source_summary":"Anlam çekirdeği, bir hayvanı ya da tutsağı kişinin yanında yönlendirerek götürmesidir. Eylem, yanda çekilen hayvanı ve hayvana bağlı tutsağı adlandıran sonuç biçimlerine de uzanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنبت الدابة أو الفرس أو الأسير إذا قدته إلى جنبك، الجنيبة الدابة المقادة، والجنب المنهي عنه في الرهان بإحضار فرس إلى جنب فرس السباق.","what_is_not_ar":"لا يدخل فيه مجرد كون الشيء ناحية، ولا الرفيق المصاحب بلا معنى القيادة."},"support_links":["sup_69f8a590a5c636481a8c"]},{"boundary":"Dal genel olarak her yeli değil, belirli güney yönünden esen yeli belirtir; ona bağlı olaylar ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"güneyden esen yel","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli güney yönünden esen ve kuzeyden esen yelin karşıtı olan yeli belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yelin yönü sağ taraf, iki başka yelin yönleri arasındaki bölge veya kutsal yapının bir yanı üzerinden tarif edilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yel sıcak oluşuyla da nitelenebilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yelin ayırt edici yönünün güney olduğu ve kuzeyden esen yele karşı konumlandığı bağlamlarda kullanılır.","boundary_detail":"Dal genel olarak her yeli değil, belirli güney yönünden esen yeli belirtir; ona bağlı olaylar ayrı kullanımlardır.","branch_image_ar":"الجنوب ريح من جهة مخصوصة","concept_gloss":"güneyden esen yel","contextual_glosses":[{"applicability":"Yönün yanı sıra yelin sıcak niteliğinin de öne çıktığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güney yönünü ve kaynakta belirtilen sıcaklık niteliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"sıcak güney yeli","usage_role":"contextual"}],"definition":"Belirli güney yönünden esen, kuzeyden esen yelin karşısında konumlanan ve sıcaklığıyla da nitelenebilen yeldir. Yön tarifi geleneksel yön işaretlerine göre daha ayrıntılı biçimde belirtilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli güney yönünden esen ve kuzeyden esen yelin karşıtı olan yeli belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Yelin yönü sağ taraf, iki başka yelin yönleri arasındaki bölge veya kutsal yapının bir yanı üzerinden tarif edilir."},{"facet_id":"F003","role":"specialization","statement":"Bu yel sıcak oluşuyla da nitelenebilir."}],"identity_rationale":"Yetkili dal ifadesi belirli bir yönden esen, kuzey yeline karşıt ve çoğu kez sıcak sayılan yeli açıkça tanımlar. Bu yelin esmesi, insanların ona girmesi veya bir bulutu sürüklemesi ayrı sözcük birimlerinde tanıklanır; bunlar dalın yönsel yel çekirdeğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"güney yeli"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yelin güneyden esmesi veya topluluğun bu yele girip ona tutulması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güney yelinin sürüklediği bulut"}],"lexicalization_note":"Belirli yelin yalın adı ile esme, ona tutulma ve bulut sürükleme yapıları ayrıdır; yapıların olay anlamı yalın ada yüklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel yel alanı ve farklı yönlü belirli bir yel, dalın yönsel sınırını en açık gösteren adaylardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yel ve esinti alanıdır; bu dal yalnız belirli güney yönünden gelen yeldir.","focus_only":"Yeli güney yönü ve kuzeyden esen yele karşıtlığıyla sınırlar.","gloss":"yel","neighbor_only":"Yelin yönünden bağımsız olarak hafif veya sert esintileri ve havalandırma araçlarını da kapsar.","neighbor_ref":"root_000609/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da hareket eden havayı ve onun esmesini adlandırır."},{"boundary_match":"field_only","distinction":"Aynı yel sınıflandırmasına katılsalar da esiş yönleri farklıdır ve birbirlerinin yerine kullanılamazlar.","focus_only":"Güney yönünden esen ve kuzey yeline karşı konumlanan yeli belirtir.","gloss":"yönlü yeller","neighbor_only":"Kutsal yapının arkasından veya batı yönünden geldiği tarif edilen başka bir yeli belirtir.","neighbor_ref":"root_000458/B012","relation_type":"same_field","shared_zone":"İki dal da geleneksel yön noktalarıyla ayırt edilen belirli bir yeli adlandırır."}],"source_phrase_ar":"مما شذ عن الباب ريح الجنوب (maqayis)؛ الجنوب ريح تجيء عن يمين القبلة وقد جنبت الريح (ayn)؛ الجنوب ريح معروفة (jamhara)؛ الجنوب الريح التي تقابل الشمال (sihah)؛ الجنوب من الرياح حارة ومهبها ما بين مهبي الصبا والدبور (tahdhib)؛ الجنوب يصح أن يعتبر فيها معنى المجيء من جانب الكعبة (mufradat)","source_summary":"Ortak çekirdek, kuzeyden esen yelin karşısındaki güney yönlü yeldir. Kaynak ifadesinde yön, geleneksel yön noktalarıyla farklı biçimlerde açıklanır ve yelin sıcak olduğu da belirtilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الجنوب الريح، هبوبها، الدخول في الجنوب، وإصابة القوم بها، والسحابة المجنوبة.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة ولا الاجتناب والبعد."},"support_links":[]},{"boundary":"Dal sağlam böğrü değil, insan veya hayvanda böğür bölgesini tutan hastalık ve ağrı durumunu belirtir.","branch_kind":"bare","branch_ref":"root_000262/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"böğür bölgesini tutan ağrı veya hastalık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın böğründe ağrı bulunmasını veya akciğer zarını tutan hastalığa yakalanmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Devenin aşırı susuzluk yüzünden akciğerinin böğrüne yapıştığı hastalık durumunu belirtir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve devedeki farklı gerçekleşmeleri ortak böğür bölgesi ve bedensel bozukluk çekirdeğinde birleştirmek için kullanılır.","boundary_detail":"Dal sağlam böğrü değil, insan veya hayvanda böğür bölgesini tutan hastalık ve ağrı durumunu belirtir.","branch_image_ar":"داء الجنب وأثره في البدن","concept_gloss":"böğür bölgesini tutan ağrı veya hastalık","contextual_glosses":[{"applicability":"İnsanın böğür ağrısıyla beliren akciğer zarı hastalığına yakalanması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsandaki belirli hastalık ve böğür ağrısı bağlantısını korur."},"facet_ids":["F001"],"text":"akciğer zarı hastalığına tutulma","usage_role":"contextual"}],"definition":"İnsanda böğür ağrısı veya akciğer zarını tutan ağır hastalık, devede ise aşırı susuzluğun akciğeri böğre yapıştırdığı hastalık durumudur. Ortak nokta, böğür bölgesinin ağrı ya da iç bozuklukla etkilenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın böğründe ağrı bulunmasını veya akciğer zarını tutan hastalığa yakalanmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Devenin aşırı susuzluk yüzünden akciğerinin böğrüne yapıştığı hastalık durumunu belirtir."}],"identity_rationale":"Yetkili dal ifadesi insanın böğür ağrısını veya akciğer zarı hastalığını ve devenin aşırı susuzluk sonucu akciğerinin böğrüne yapışmasını destekler. Vurularak böğrün incitilmesi yalnız ayrı sözcük biriminde tanıklıdır; bu nedenle dalın hastalık çekirdeğine katılmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"böğrü ağrımak veya akciğer zarı hastalığına tutulmak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"vurarak böğrünü incitmek veya kırmak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"devenin aşırı susuzluktan akciğeri böğrüne yapışacak ölçüde hastalanması"}],"lexicalization_note":"Dal yalın hastalık ve ağrı anlamında tanımlanır; ayrı bir birimdeki vurma sonucu yaralanma çekirdeğe eklenmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel kırık olmayan ağrı ile başka bir bölgeye özgü ağrı en yararlı sınırları sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal organ ve neden bakımından geneldir; bu dal böğür bölgesine ve belirli insan ya da deve hastalıklarına bağlıdır.","focus_only":"Böğür bölgesine özgüdür ve belirli iç hastalıklarla deve susuzluğu durumunu kapsar.","gloss":"kırık olmayan ağrı","neighbor_only":"Herhangi bir organda kırığa varmayan genel bir ağrıyı belirtir.","neighbor_ref":"root_000417/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedende kırık olmak zorunda olmayan bir ağrı veya incinme durumunu anlatır."},{"boundary_match":"field_only","distinction":"Ağrı alanları farklıdır: bu dal böğür ve akciğer çevresine, komşu dal boyna özgüdür.","focus_only":"Böğür ve akciğer çevresindeki ağrıyı veya hastalığı belirtir.","gloss":"bölgesel beden ağrısı","neighbor_only":"Yalnız boyun ağrısını ve bunun sağaltılmasını belirtir.","neighbor_ref":"root_000016/B006","relation_type":"same_field","shared_zone":"İki dal da belirli bir beden bölgesindeki ağrıyı adlandırır."}],"source_phrase_ar":"الجنب أن يشتد عطش البعير حتى تلتصق رئته بجنبه (maqayis)؛ أجنب فلان إذا أخذته ذات الجنب والجنيب الذي يشتكي جنبه (ayn)؛ جنب الرجل إذا اشتكى جنبه (jamhara)؛ المجنوب الذي به ذات الجنب وجنب البعير من شدة العطش (sihah)؛ ذات الجنب علة صعبة وجنب جنبا إذا اشتكى جنبه (tahdhib)؛ جنب شكا جنبه (mufradat)","source_summary":"Ortak alan böğür bölgesini tutan ağrı veya hastalıktır. İnsan için böğür ağrısı ve akciğer zarı hastalığı, deve içinse aşırı susuzluğun akciğeri böğre yapıştırdığı özel durum belirtilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه اشتكى جنبه، ذات الجنب، المجنوب، ضربه فجنبه، وجنب البعير من شدة العطش حتى تلتصق رئته بجنبه أو يلتوي.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة بلا علة، ولا الجنوب الريح."},"support_links":[]},{"boundary":"Dal hayvan sayısının azlığını veya genel güçsüzlüğü değil, özellikle develerde süt veriminin azalmasını belirtir.","branch_kind":"mixed_non_bare","branch_ref":"root_000262/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"develerde sütün azalması veya tükenmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun develerindeki sütün azalmasını veya hiç kalmamasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sütü azalan develerin sahibi olan kişi veya topluluk, bu eksiklik üzerinden nitelenir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi ya da topluluğun deve sürüsündeki süt verimi eksikliğini genel olarak anlatmak için kullanılır.","boundary_detail":"Dal hayvan sayısının azlığını veya genel güçsüzlüğü değil, özellikle develerde süt veriminin azalmasını belirtir.","branch_image_ar":"التجنيب قلة لبن الإبل","concept_gloss":"develerde sütün azalması veya tükenmesi","contextual_glosses":[{"applicability":"Bir topluluğa ait develerde hiç süt kalmadığının özellikle belirtildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deve sürüsündeki tam süt yokluğunu bağlama uygun biçimde korur."},"facet_ids":["F001"],"text":"sütü tükenen deve sürüsü","usage_role":"contextual"}],"definition":"Bir kişinin veya topluluğun develerinde sütün azalması ya da bütünüyle tükenmesidir. Değişen katılımcı, sütü azalan hayvanların sahibi veya içinde bulundukları topluluktur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun develerindeki sütün azalmasını veya hiç kalmamasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Sütü azalan develerin sahibi olan kişi veya topluluk, bu eksiklik üzerinden nitelenir."}],"identity_rationale":"Yetkili dal ifadesi bir topluluğun develerindeki sütün azalması veya tükenmesini ortak ve açık biçimde destekler. Sütün kaybolduğu yıl anlamı ayrı söz öbeğinde tanıklanmıştır; dalın kurucu tanımı sürüdeki süt yokluğuyla sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"topluluğun develerinde sütün azalması veya tükenmesi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"süt kıtlığı yaşanan yıl"}],"lexicalization_note":"Sürüde süt azalması çekirdeği ile süt kıtlığı yılına bağlı söz öbeği ayrı tutulur; yıl anlamı yalın dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tek devenin az sütü ile sütün geri dönmesi umudu, dalın sürü ve sonuç sınırlarını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tek hayvanın niteliğine ve genel güçsüzlüğe uzanır; bu dal sahip veya topluluk düzeyindeki sürüsel süt eksikliğine odaklanır.","focus_only":"Bir kişi veya topluluğun bütün deve varlığındaki süt azalmasını ya da yokluğunu belirtir.","gloss":"az süt verme","neighbor_only":"Tek bir dişi devenin az süt vermesini ve insan ya da iş için genel güçsüzlüğü de kapsar.","neighbor_ref":"root_000497/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da develerde süt miktarının düşük olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal mevcut süt eksikliğini bildirir; komşu dal ise bu eksikliğe ek olarak sütün geri gelmesi beklentisini taşır.","focus_only":"Sütün azalması veya yokluğu durumunu, geri dönüş beklentisi olmadan bildirir.","gloss":"sütün kesilmesi","neighbor_only":"Kesilmiş ya da kuşkulu sütün yeniden gelmesinin umulmasını kurucu olarak içerir.","neighbor_ref":"root_001015/B006","relation_type":"near_neighbor","shared_zone":"İki dal da develerde sütün bulunmaması veya azalması durumuyla ilgilidir."}],"source_phrase_ar":"جنب القوم إذا قلت ألبانهم (maqayis;sihah)؛ جنب بنو فلان إذا لم يكن في إبلهم لبن (ayn;tahdhib)؛ جنب الرجل إذا قلت ألبان إبله (jamhara)؛ جنب بنو فلان إذا لم يكن في إبلهم اللبن (mufradat)","source_summary":"Ortak anlam, bir kişi ya da topluluğa ait develerde sütün azalması veya kalmamasıdır. Söyleyiş hayvanı doğrudan değil, bu süt eksikliğinden etkilenen sahibi ya da topluluğu özne yapar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه جنب القوم أو بنو فلان إذا قلت ألبان إبلهم أو لم يكن في إبلهم لبن، وعام تجنيب.","what_is_not_ar":"لا يدخل فيه الجنب الجارحة ولا المجنوب المريض."},"support_links":[]},{"boundary":"Dal bağımsız ve genel çokluk anlamı değildir; çokluk yalnız belirtilen iyi veya kötü yapısı içinde gerçekleşir.","branch_kind":"collocation","branch_ref":"root_000262/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"çok miktarda iyilik veya kötülük","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz öbeğinde iyilik veya kötülüğün çok miktarda olmasını belirtir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyiliğin çokluğu, onun kişinin yanında hazır bulunması düşüncesiyle açıklanabilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirtilen iyi veya kötü adlarıyla kurulan yapının çokluk anlamını karşılamak için kullanılır.","boundary_detail":"Dal bağımsız ve genel çokluk anlamı değildir; çokluk yalnız belirtilen iyi veya kötü yapısı içinde gerçekleşir.","branch_image_ar":"المجنب خير أو شر كثير","concept_gloss":"çok miktarda iyilik veya kötülük","contextual_glosses":[{"applicability":"Söz öbeğinin olumlu kutbunda çok miktarda iyilik bulunduğunu anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumlu bağlamdaki iyilik ve çokluk anlamlarını birlikte korur."},"facet_ids":["F001"],"text":"bolca iyilik","usage_role":"contextual"}],"definition":"Yalnız belirli bir söz öbeği içinde, iyiliğin veya kötülüğün çok miktarda bulunmasını belirtir. İyiliğin kişiye yakın bulunması, çokluğu açıklayan ikincil bir tasarım olarak verilebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz öbeğinde iyilik veya kötülüğün çok miktarda olmasını belirtir."},{"facet_id":"F002","role":"associated_use","statement":"İyiliğin çokluğu, onun kişinin yanında hazır bulunması düşüncesiyle açıklanabilir."}],"identity_rationale":"Kaynak ifadesi yalnız belirli iyi ve kötü adlarıyla kurulan yapıda çokluk anlamını doğrular. İyilik için verilen kişinin yanında bulunma açıklaması olası bir anlamlandırmadır; çekirdek, söz konusu iyi veya kötünün çok miktarda olmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"pek çok iyilik veya kötülük"}],"lexicalization_note":"Tanım yalnız çok miktarda iyilik veya kötülük bildiren belirli söz öbeğine bağlıdır; yalın köke genel çokluk anlamı verilmez.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel çoklukla kapsam farkı ve azlıkla karşıtlık, yapıya bağlı anlamın sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel çokluk anlamıdır; bu dal yalnız iyilik veya kötülükle kurulan belirli yapıda çokluk bildirir.","focus_only":"Çokluk anlamı yalnız belirli iyi veya kötü adlarıyla kurulan söz öbeğinde geçerlidir.","gloss":"çokluk","neighbor_only":"Her türlü şeyin, sayının veya malın çokluğunu ve bir şeyi çoğaltmayı genel olarak kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin yüksek miktarda bulunmasını bildirir."},{"boundary_match":"opposed","distinction":"Bu dal yüksek miktar kutbunda, komşu dal ise azlık ve küçüklük kutbundadır.","focus_only":"Belirli bir iyilik veya kötülüğün yüksek miktarını bildirir.","gloss":"çok ve az","neighbor_only":"Bir şeyin az, küçük, önemsiz veya değersiz oluşunu bildirir.","neighbor_ref":"root_000053/B013","relation_type":"antonym","shared_zone":"İki dal miktarın yüksek ya da düşük olması ekseninde karşı karşıya gelir."}],"source_phrase_ar":"المجنب الخير الكثير كأنه إلى جنب الإنسان (maqayis)؛ شرا مجنبا وخيرا مجنبا أي كثيرا (ayn)؛ خيرا مجنبة ومجنبا وشرا مجنبا أي كثيرا (jamhara)؛ المجنب بالفتح الشيء الكثير وخيرا مجنبا وشرا مجنبا (sihah)؛ المجنب الخير الكثير والمجنب يقال في الشر إذا كثر (tahdhib)؛ جنب فلان خيرا وجنب شرا (mufradat)","source_summary":"Ortak anlam, belirli iyi ve kötü adlarıyla birlikte kullanıldığında çok miktar bildirmesidir. Kişinin yanında bulunan iyilik açıklaması, çokluk çekirdeğinin kaynakta sunulan ikincil yorumudur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه خير مجنب أو شر مجنب بمعنى كثير، وما جعلته بعض المصادر كأنه إلى جنب الإنسان.","what_is_not_ar":"لا يدخل فيه القيادة إلى الجنب ولا الترس المجنب."},"support_links":[]},{"boundary":"Dal genel olarak her otu değil, yaz döneminde kalan veya gelişen köklü küçük bitki ve çalı kümesini belirtir.","branch_kind":"bare","branch_ref":"root_000262/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"yazın kalan köklü küçük bitkiler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yazın kalan veya yaz döneminde yeniden gelişen köklü küçük bitki ve çalıların genel adıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birçok ayrı bitkiyi, kalıcı kök ve yaz döneminde varlığını sürdürme ortaklığıyla tek kümede toplar."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir tür yerine yaz döneminde varlığını sürdüren çeşitli köklü küçük bitkilerin ortak adı gerektiğinde kullanılır.","boundary_detail":"Dal genel olarak her otu değil, yaz döneminde kalan veya gelişen köklü küçük bitki ve çalı kümesini belirtir.","branch_image_ar":"الجنبة نبت متوسط مستقل","concept_gloss":"yazın kalan köklü küçük bitkiler","contextual_glosses":[{"applicability":"Yaz döneminde kalan veya yeniden gelişen bitki kümesini açıklayıcı biçimde anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaz dönemindeki küçük çalı ve ot kümesini anlaşılır biçimde korur."},"facet_ids":["F001","F002"],"text":"yazın kalan veya yeniden gelişen bitkiler","usage_role":"explanatory"}],"definition":"Yaz döneminde kalan ya da yeniden gelişen, kökü bulunan çeşitli küçük bitki ve çalıların ortak adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yazın kalan veya yaz döneminde yeniden gelişen köklü küçük bitki ve çalıların genel adıdır."},{"facet_id":"F002","role":"extension","statement":"Birçok ayrı bitkiyi, kalıcı kök ve yaz döneminde varlığını sürdürme ortaklığıyla tek kümede toplar."}],"identity_rationale":"Kaynak ifadesi tek bir türden çok, yaz boyunca kalan veya yazın yeniden gelişen çeşitli köklü küçük bitkiler için ortak bir ad verir. Bu nedenle tanım belirli bir bitki türü değil, mevsimsel özellikleri ortak bir bitki kümesidir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yazın kalan, köklü küçük bitki veya çalı"}],"lexicalization_note":"Dal yalın bir bitki kümesi adıdır; belirli bir tür veya yalnız tek bir otla sınırlandırılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; yaz bitkisi ve hasat sonrası otlak karşılaştırmaları bu genel bitki kümesinin mevsim ve tür sınırını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal mevsimsel olarak ortaya çıkan belirli yaz otunu anlatır; bu dal yazın kalan köklü çeşitli bitkilerin daha geniş ortak adıdır.","focus_only":"Yazın kalan ya da yazın gelişen köklü birçok küçük bitki ve çalıyı ortak ad altında toplar.","gloss":"yaz bitkisi","neighbor_only":"İlkbahar geçtikten sonra küçük ağaçların yeşermesiyle oluşan belirli yaz otlağını anlatır.","neighbor_ref":"root_000993/B011","relation_type":"near_synonym","shared_zone":"Her iki dal da ilkbahar sonrasındaki yaz döneminde görülen bitkileri kapsar."},{"boundary_match":"partial","distinction":"Komşu dal hasat sonrası tarla kalıntısına bağlıdır; bu dalın çekirdeği ise köklü küçük bitkilerin yazın varlığını sürdürmesidir.","focus_only":"Bitkileri köklü oluşları ve yaz boyunca kalmaları temelinde sınıflandırır.","gloss":"mevsim sonrasında kalan bitki örtüsü","neighbor_only":"Hasattan sonra tarlada kalan ekin artığını ve altından çıkan yeşil otu birlikte kapsar.","neighbor_ref":"root_000324/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da asıl mevsim veya hasat sonrasında kalan bitki örtüsüne değinir."}],"source_phrase_ar":"الجنبة اسم يقع على عامة الشجر يترك في الصيف (ayn)؛ الجنبة ضرب من النبت (jamhara)؛ الجنبة اسم لكل نبت يتربل في الصيف (sihah)؛ الجنبة اسم واحد لنبوت كثيرة هي كلها عروة (tahdhib)","source_summary":"Anlam tek bir türe değil, yaz boyunca kalan veya yazın yeniden yeşeren çeşitli küçük bitkilere yönelir. Ortak özellikleri köklü olmaları ve yaz döneminde varlığını sürdürmeleri ya da yeniden gelişmeleridir.","sources":["AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الجنبة اسم عام لنبات يترك في الصيف أو يتربل فيه، مما له أرومة ويبقى في المحل ويعصم المال.","what_is_not_ar":"لا يدخل فيه الجنبة بمعنى الاعتزال ولا الجنب الجارحة."},"support_links":[]},{"boundary":"Dal genel olarak her örtüyü değil, kişinin yanında bulunan ve yanını koruyan kalkanı veya benzer koruyucu örtüyü belirtir.","branch_kind":"bare","branch_ref":"root_000262/B011","candidate_links":[{"candidate_id":"cand_13684e2604e7488c4c6a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"yanı koruyan kalkan veya örtü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin yanında taşıdığı ve bedenini koruyan kalkanı belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalkan dışında koruyucu bir örtü için de kullanılabilir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalkan çekirdeğini ve kaynakta verilen daha geniş koruyucu örtü yorumunu birlikte yansıtmak için kullanılır.","boundary_detail":"Dal genel olarak her örtüyü değil, kişinin yanında bulunan ve yanını koruyan kalkanı veya benzer koruyucu örtüyü belirtir.","branch_image_ar":"المجنب وقاء إلى الجنب","concept_gloss":"yanı koruyan kalkan veya örtü","contextual_glosses":[{"applicability":"Savaşta veya savunmada kişinin yanında tuttuğu koruyucu kalkan özellikle kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalkanın koruyucu işlevini ve kişinin yanındaki konumunu korur."},"facet_ids":["F001"],"text":"kişinin yanında taşıdığı kalkan","usage_role":"contextual"}],"definition":"Kişinin yanında taşıdığı ve özellikle yanını koruduğu düşünülen kalkandır. Daha geniş bir kaynak yorumunda, aynı koruma işlevindeki bir örtüyü de belirtebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin yanında taşıdığı ve bedenini koruyan kalkanı belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Kalkan dışında koruyucu bir örtü için de kullanılabilir."}],"identity_rationale":"Kaynak ifadesi kişinin yanında bulunan kalkanı ortak anlam olarak verir ve bir kaynakta koruyucu örtü yorumunu da ekler. Yanında bulunma açıklaması nesnenin konumunu, kalkan ve örtü ise koruyucu işlevini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kişinin yanında taşıdığı kalkan veya koruyucu örtü"}],"lexicalization_note":"Dal yalın bir koruyucu nesne adıdır; çokluk bildiren benzer biçimli söz öbeği veya atın beden yapısı bu tanıma katılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel kalkan ve genel koruyucu örtü dalları bu nesnenin konum ve işlev sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel koruyucu araç alanına yayılır; bu dal kalkanı kişinin yanındaki konumuyla sınırlar ve yalnız ikincil olarak örtüye uzanır.","focus_only":"Kalkanı kişinin yanındaki konumu ve yanını koruması üzerinden adlandırır; örtü yorumunu da taşır.","gloss":"koruyucu kalkan","neighbor_only":"Korunmak için kullanılan kalkanı, silahı veya herhangi bir koruyucu aracı genel olarak kapsar.","neighbor_ref":"root_000266/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendini korumak için kullandığı kalkanı kapsar."},{"boundary_match":"partial","distinction":"Komşu dal genel örtme ve saklama alanıdır; bu dal kişinin yanında taşıdığı savunma nesnesiyle sınırlıdır.","focus_only":"Kişinin yanında taşınan kalkanı temel alır.","gloss":"koruyucu örtü","neighbor_only":"Baş, eşya, tel veya gök gibi çok farklı şeyleri örten ve koruyan genel örtme eylemi ile nesnelerini kapsar.","neighbor_ref":"root_001096/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir şeyi örterek veya araya girerek koruyan nesne alanında buluşur."}],"source_phrase_ar":"سمي الترس مجنبا لأنه إلى جنب الإنسان (maqayis)؛ المجنب الترس (ayn;sihah;tahdhib)؛ المجنب الترس ويقال المجنب والمجنب الستر أيضا (jamhara)","source_summary":"Ortak karşılık kişinin yanında taşıdığı kalkandır; adlandırma nesnenin yandaki konumuyla açıklanır. Daha geniş tekil yorum, koruyucu örtüyü de aynı işlev alanına alır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه المجنب بمعنى الترس، وما روي بمعنى الستر، باعتباره شيئا إلى جنب الإنسان أو يحمي جانبه.","what_is_not_ar":"لا يدخل فيه المجنب بمعنى الكثير ولا الفرس المجنب في الخلقة."},"support_links":["sup_f71a62865a6b271f833c"]},{"boundary":"Dal hareket sırasında bacağı yana atmayı değil, özellikle atın bacaklarında doğuştan bulunan ölçülü açıklık ve biçim özelliğini belirtir.","branch_kind":"bare","branch_ref":"root_000262/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","surface_ar":"يُجَنَّبُ"}],"gloss":"atın bacaklarında doğuştan ölçülü açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın iki bacağının doğuştan birbirinden uzak ve açık durmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bacakta eğrilik veya gerginlik görünümü bulunabilir, fakat açıklık aşırı ayrık bacaklılık değildir."}}],"root_ar":"ج ن ب","root_id":"root_000262","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atın bacakları arasındaki yapısal uzaklığın doğuştan olduğu ve aşırı ayrıklığa varmadığı bağlamlarda kullanılır.","boundary_detail":"Dal hareket sırasında bacağı yana atmayı değil, özellikle atın bacaklarında doğuştan bulunan ölçülü açıklık ve biçim özelliğini belirtir.","branch_image_ar":"التجنيب تباعد في هيئة القوائم","concept_gloss":"atın bacaklarında doğuştan ölçülü açıklık","contextual_glosses":[{"applicability":"Bu doğuştan beden yapısını taşıyan atın doğrudan nitelenmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Atın bacak açıklığını ve bunun aşırı olmadığı sınırını korur."},"facet_ids":["F001","F002"],"text":"bacakları ölçülü biçimde ayrık at","usage_role":"contextual"}],"definition":"Özellikle atın iki bacağının doğuştan birbirinden ölçülü biçimde uzak durduğu beden yapısıdır. Bacakta eğrilik veya gerginlik görünümü oluşturabilir, ancak aşırı ayrık bacaklılık düzeyine ulaşmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın iki bacağının doğuştan birbirinden uzak ve açık durmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Bacakta eğrilik veya gerginlik görünümü bulunabilir, fakat açıklık aşırı ayrık bacaklılık değildir."}],"identity_rationale":"Kaynak ifadesi atın bacağında eğrilik veya gerginlik görünümünü ve iki bacağın doğuştan birbirinden uzak durmasını destekler. Ayrıca bu açıklığın aşırı ayrık bacaklılık olmadığı açıkça sınırlandırılır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"atın bacaklarının doğuştan birbirinden ayrı durması, fakat aşırı ayrık olmaması"}],"lexicalization_note":"Dal yalın bir beden yapısı niteliğidir; hayvanı yanda götürme eylemi veya ayrı bir yürüyüş biçimi tanıma katılmaz.","neighbor_coverage_note":"Bütün komşular değerlendirildi; genel ayrık bacak yapısı ile devenin bacak genişliği, at türü ve derece sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal beden bölgesi ve derece bakımından daha geniştir; bu dal ata özgüdür ve aşırı ayrıklığı özellikle dışlar.","focus_only":"Özellikle atın bacaklarındaki doğuştan ve aşırı olmayan açıklığı belirtir.","gloss":"bacak açıklığı","neighbor_only":"İnsan veya hayvanda aşık kemikleri, uyluklar ya da dizler arasındaki açıklığı ve bunun ağır derecesini kapsar.","neighbor_ref":"root_001133/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bacakların veya eklemlerin birbirinden uzak durduğu beden yapısını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal deveye ve sırt yapısına uzanır; bu dal atın bacakları arasındaki doğuştan uzaklıkla sınırlıdır.","focus_only":"Atın iki bacağının birbirinden uzak durmasını ve eğrilik görünümünü belirtir.","gloss":"hayvan bacağında açıklık","neighbor_only":"Devenin bacağındaki hafif genişlik yanında sırtın yayvanlığını ve hörgüçsüzlüğü de kapsar.","neighbor_ref":"root_001143/B015","relation_type":"near_neighbor","shared_zone":"İki dal da bir hayvanın bacak yapısındaki açıklık veya yayvanlık niteliğine değinir."}],"source_phrase_ar":"التجنيب انحناء وتوتير في رجل الفرس (sihah)؛ المجنب من الخيل البعيد ما بين الرجلين من غير فجج والتجنيب بالجيم في الرجلين (tahdhib)؛ التجنيب الروح في الرجلين وذلك إبعاد إحدى الرجلين عن الأخرى خلقة (mufradat)","source_summary":"Ortak anlam, atın bacaklarının doğuştan birbirinden uzak durduğu bir beden yapısıdır. Görünüm eğrilik veya gerginlik olarak tarif edilir ve aşırı ayrıklıkla arasına açık bir sınır konur.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه التجنيب في رجل الفرس أو قوائمه، والمجنب من الخيل البعيد ما بين الرجلين من غير فجج، وما وصف بأنه إبعاد إحدى الرجلين عن الأخرى خلقة.","what_is_not_ar":"لا يدخل فيه قيادة الدابة إلى الجنب ولا الجنيبة المقادة."},"support_links":[]},{"boundary":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B001","candidate_links":[{"candidate_id":"cand_13684e2604e7488c4c6a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","surface_ar":"أَتْقَى"}],"gloss":"araya engel koyarak zarardan koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel eylem ile koruyucu aracın ortak çekirdeğini, herhangi bir özel kullanım alanına bağlamadan karşılar.","boundary_detail":"Dal genel koruma işlemini ve koruyucu aracı kapsar; kişinin kendini sakınması, ağırlık ölçüsü, hayvanın aksaması ve kuş adı bu sınıra girmez.","branch_image_ar":"دفع الضرر بوقاية","concept_gloss":"araya engel koyarak zarardan koruma","contextual_glosses":[{"applicability":"Eylemden çok, zarar ile korunacak şey arasına koyulan araç veya katman kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araya koyulan unsurun koruyucu işlevini ve zararı kesen konumunu korur."},"facet_ids":["F002"],"text":"koruyucu engel","usage_role":"contextual"},{"applicability":"Kadına ait özel bez kullanımını açıkça anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bezin yerini, maddi niteliğini ve koruyucu ara katman işlevini korur."},"facet_ids":["F003"],"text":"saç ile dış örtü arasındaki koruyucu bez","usage_role":"explanatory"}],"definition":"Bir şeyi ona zarar verecek başka bir şeyden korumak için araya bir araç ya da engel koyma ve böylece zararı ondan uzak tutma. Bu işlevi gören araç veya engel de aynı kavram alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Korunan şeyden zarar verici etkiyi uzak tutma ve onu incinmekten ya da bozulmaktan saklama işlemidir."},{"facet_id":"F002","role":"core","statement":"Koruma, zarar ile korunacak şey arasına başka bir araç, katman veya engel koyularak gerçekleştirilir."},{"facet_id":"F003","role":"example","statement":"Kadının saçı ile dış örtüsü arasına koyduğu bez, bu koruyucu ara katmanın özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi ona zarar verecek başka bir şeyden korumayı ve bunun için araya koruyucu bir unsur koymayı ortak çekirdek olarak verir. Koruyucu bez örneği bu genel işlemin özel bir gerçekleşmesidir ve dalın kimliğini değiştirmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi koruyucu bir engelle zarardan saklamak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"koruma; zararı önleyen araç veya engel"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi korumaya yarayan araç ya da engel"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"zarardan koruyan şey"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"zararı savan koruyucu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının saçı ile dış örtüsü arasına koyduğu koruyucu bez"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"koruyucu şeyler"}],"lexicalization_note":"Tanım, genel koruma çekirdeğini özel ad ve kalıplardan ayırır; kadına ait koruyucu bez yalnızca yapıya bağlı bir örnek olarak tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan beş ilişki koruma çekirdeğine en yakın sınırları gösterir. Kale, bekçilik, tutunarak korunma, üstü açıklık ve öteki kök içi dallar ya daha uzak alan ortaklığı kurar ya da ayrı adlandırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda ayırt edici unsur, başka bir şeyi koruyucu engel olarak araya koymaktır; komşu dalın çekirdeği ise etkiyi bulunduğu yerden itmek veya doğrudan savmaktır.","focus_only":"Koruma, zarar ile hedef arasına başka bir unsur koyma mekanizmasıyla tanımlanır.","gloss":"koruma ile itip uzaklaştırma","neighbor_only":"Öteki dal yer değiştirtmeyi, karşılıklı itişmeyi ve kötülüğü doğrudan savmayı da kapsar.","neighbor_ref":"root_000480/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da zararlı veya istenmeyen bir etkinin hedefe ulaşmasını engeller."},{"boundary_match":"partial","distinction":"Bu dal koruyucu engel üzerinden zararı savmaya odaklanır; komşu dal ise engel gerektirmeyen bakım, gözetim ve süreklilik taşıyan kollamayı da içerir.","focus_only":"Zararı kesen bir araç ya da engelin araya girmesi açıkça kurucu unsurdur.","gloss":"koruma ile gözetip kollama","neighbor_only":"Sürekli gözetme, bakım, kollama ve bir şeyi iyi durumda tutma süreçlerini de kapsar.","neighbor_ref":"root_000372/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi zarar ve bozulmadan uzak tutma alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal genel koruma işlemi ile onun aracını birlikte kapsar; komşu dal belirli bir koruyucu engel veya dayanak kavramında yoğunlaşır.","focus_only":"Koruma eylemi her tür araç veya katmanla gerçekleştirilebilir ve araç da adlandırılabilir.","gloss":"koruyucu araç ile koruyan engel","neighbor_only":"Koruyan ve çevreleyen belirli bir engel ya da dayanak adı merkezde yer alır.","neighbor_ref":"root_000071/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda bir engel, dış etkiden koruma ve çevreleyerek güvence sağlama işlevi görür."},{"boundary_match":"partial","distinction":"Komşu dal giysilerin birbirini koruduğu özel uygulamayı adlandırır; bu dal ise aynı araya koyma mekanizmasını her tür korunacak şeye açar.","focus_only":"Korunacak varlık ve zarar türü bakımından genel bir koruma şeması sunar.","gloss":"genel koruma ile giysiyi örtüyle koruma","neighbor_only":"Bir giysiyi başka bir giysiyle örtüp yıpranmaktan koruyan özel uygulamaya bağlıdır.","neighbor_ref":"root_001635/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir katman, başka bir şeyi yıpranma veya zarardan korur."},{"boundary_match":"partial","distinction":"Bu dal genel ve çoğu kez maddi koruma ilişkisini anlatır; komşu dal aynı şemayı kişinin kendi davranışını ve güvenliğini gözetmesine özgüler.","focus_only":"Korunan katılımcı herhangi bir nesne veya canlı olabilir ve maddi bir engel kullanılabilir.","gloss":"bir şeyi koruma ile kendini sakınma","neighbor_only":"Korunan katılımcı kişinin kendisidir; korkulan şeyden ve yanlış davranıştan sakınma öne çıkar.","neighbor_ref":"root_001677/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da zarar ile korunacak taraf arasına koruyucu bir mesafe veya önlem koyar."}],"source_phrase_ar":"دفع شيء عن شيء بغيره (maqayis)؛ كل ما وقى شيئا فهو وقاء له ووقاية (ayn;jamhara;tahdhib)؛ حفظ الشيء مما يؤذيه ويضره (mufradat)؛ وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها (jamhara)","source_summary":"Kaynakların ortak anlatımı, korumayı zararlı etkiyi başka bir şey aracılığıyla savma olarak kurar; hem koruma eylemini hem de bu işte kullanılan engeli kapsar. Kadının saçını dış örtüden ayıran bez, bu mekanizmanın özel bir örneğidir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه وقى الشيء وحفظه مما يؤذيه، والوقاء والوقاية والواقية وما يجعل حاجزا بين الشيء والضرر، ووقاية المرأة","what_is_not_ar":"لا يدخل فيه اسم الوزن أوقية ولا اسم الصرد ولا الظلع اليسير إلا من جهة الصورة العامة للاتقاء"},"support_links":["sup_f71a62865a6b271f833c"]},{"boundary":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B002","candidate_links":[{"candidate_id":"cand_be84f0bc12bd73f104ee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","surface_ar":"أَتْقَى"}],"gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem genel öz-koruma çekirdeğini hem de kişiyi yanlış davranıştan uzak tutan yönünü birlikte verir.","boundary_detail":"Dal kişinin kendisini koruması ve sakınmasıyla sınırlıdır; herhangi bir nesneyi koruma, yalnız başına iyi iş yapma veya işlenmiş yanlıştan dönme anlamına genişletilmez.","branch_image_ar":"جعل النفس في وقاية","concept_gloss":"korkulan şeyden ya da yanlış davranıştan kendini koruma","contextual_glosses":[{"applicability":"Korunulan tehlike veya yanlış davranış bağlamdan açıkça anlaşıldığında doğal ve kısa bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkulan şeyin veya yanlış davranışın türünü ve araya önlem koyma şemasını açıkça söylemez.","preserves":"Kişinin kendi güvenliğini ve davranışını gözeten öz-koruma yönünü korur."},"facet_ids":["F001","F002"],"text":"kendini sakınma","usage_role":"general"},{"applicability":"İnanç ve sorumluluk bağlamında, kişinin davranışını yasak olandan uzak tutması kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnanç bağlamındaki muhatabı, sakınma tutumunu ve yanlış davranıştan uzak durmayı korur."},"facet_ids":["F003"],"text":"Tanrı'ya karşı gelmekten sakınma","usage_role":"contextual"}],"definition":"Kişinin kendisini korktuğu veya zarar beklediği şeyden koruyacak bir önlem altına alması ve yanlış davranıştan uzak tutması. Tanrı'ya karşı gelmekten sakınma, bu öz-koruma tutumunun inanç alanındaki özel biçimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, korkulan ya da zarar verecek şey ile kendi arasına koruyucu bir önlem koyar."},{"facet_id":"F002","role":"specialization","statement":"Öz-koruma, kişiyi suç doğuran ve yanlış sayılan davranışlardan uzak tutma biçimini alabilir."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'ya karşı gelmekten sakınma, kişi ile sakınılan sonuç arasına koruyucu bir tutum koymak olarak düşünülür."}],"identity_rationale":"Kaynak ifadesi, kişinin kendisini korktuğu şeyden koruma altına almasını ve yanlış davranıştan uzak tutmasını aynı öz-koruma şemasında birleştirir. Tanrı'ya karşı gelmekten sakınma bu çekirdeğin inanç alanındaki belirgin gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kendini korkulan ya da zarar verecek şeyden korumak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi kendine koruyucu yapmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı'ya karşı gelmekten sakınmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin kendini korktuğu şeyden ve yanlış davranıştan koruması"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sakınma ve kendini koruma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sakınma; kendini kötülükten koruma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sakınıp kendini koruma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini yanlış davranışlardan koruyan kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sakınan ve kendini yanlış davranıştan koruyan kimse"}],"lexicalization_note":"Genel öz-koruma anlamı ile bir aracı kendine koruyucu yapma ve Tanrı'ya karşı gelmekten sakınma kalıpları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genel koruma, yanlıştan uzak durma, iyi davranış, suç korkusu ve tapınma sınırlarını en açık biçimde gösterir. Bağışlanma, tövbeye çağırma, benlik ve örtü adayları daha dolaylıdır; öteki kök içi dallar ayrı anlamlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel koruma şemasını kişinin kendi güvenliğine ve davranışına taşır; komşu dal katılımcıyı ve zarar türünü sınırlandırmayan genel korumadır.","focus_only":"Korunan taraf zorunlu olarak kişinin kendisidir ve davranışsal sakınma da kapsama girer.","gloss":"kendini sakınma ile genel koruma","neighbor_only":"Herhangi bir nesne veya canlı, maddi bir araç ya da engel kullanılarak korunabilir.","neighbor_ref":"root_001677/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da zarar ile korunacak taraf arasına koruyucu bir önlem koyma şeması vardır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği önleyici öz-korumadır; komşu dal ise yanlış karşısında çekinmenin yanında işlenmiş bir yanlıştan çıkma sonucunu da kapsar.","focus_only":"Henüz gerçekleşmemiş tehlikeden ve yanlış davranıştan önleyici biçimde korunmayı da kapsar.","gloss":"yanlıştan sakınma ile yanlışın yükünden çıkma","neighbor_only":"İşlenmiş bir yanlışın yükünden çıkma ve ondan dönmüş olma anlamına kadar uzanabilir.","neighbor_ref":"root_000013/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin yanlış davranıştan uzak durmasını ve suç doğuran eylemi işlememesini anlatabilir."},{"boundary_match":"partial","distinction":"Bu dal koruyucu ve kaçınmacı tutumu tanımlar; komşu dal ise sakınmanın ötesinde olumlu iyilik ve itaat eylemlerini geniş biçimde kapsar.","focus_only":"Korkulan sonuç ile kişi arasına koruyucu bir sakınma tutumu koymak merkezde yer alır.","gloss":"sakınma ile iyilik ve itaat","neighbor_only":"İyi olma, itaat ve çok çeşitli yararlı işleri yapma yönünde olumlu bir eylem alanı sunar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranışa yönelmeyi ve yanlış olandan uzak kalmayı destekler."},{"boundary_match":"partial","distinction":"Bu dal koruyucu davranış ve uzak durma eylemidir; komşu dal ise suç durumunu ve ona düşme korkusunu merkeze alır.","focus_only":"Kişinin korkulan veya suç doğuran durumdan kendini etkin biçimde korumasını anlatır.","gloss":"suçtan korunma ile suç korkusu","neighbor_only":"Suçun kendisini, suç kazanmayı ve kötü davranışa düşme korkusunu adlandırır.","neighbor_ref":"root_001051/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da yanlış davranış, onun doğuracağı yük ve bundan duyulan korku bulunur."},{"boundary_match":"field_only","distinction":"Ortak alan inanç ve sorumluluktur; bu dal sakınma yoluyla öz-korumayı, komşu dal ise tapınma ve yakınlık arama eylemini tanımlar.","focus_only":"Yanlış davranıştan uzak durarak kişinin kendisini koruması öne çıkar.","gloss":"sakınma ile tapınma","neighbor_only":"Tapınma, yakınlık arama ve kulluk eylemlerini olumlu uygulamalar olarak adlandırır.","neighbor_ref":"root_001498/B001","relation_type":"same_field","shared_zone":"İki dal inanç alanında kişinin Tanrı karşısındaki davranışını konu edinir."}],"source_phrase_ar":"اتق الله توقه أي اجعل بينك وبينه كالوقاية (maqayis)؛ التقوى في الأصل وقوى فعلى من وقيت (ayn;tahdhib)؛ التقوى جعل النفس في وقاية مما يخاف (mufradat)؛ حفظ النفس عما يؤثم (mufradat)؛ اتقى تقية وتقاة (sihah)","source_summary":"Kaynaklar bu dalı, kişinin kendisini korkulan şey karşısında koruma altına alması ve yanlış davranıştan uzak tutması olarak açıklar. İnanç bağlamındaki kullanım, Tanrı'ya karşı gelmekten sakınmayı kişi ile kötü sonuç arasındaki koruyucu tutum şeklinde somutlaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اتقى واتقاء وتقوى وتقى وتقاة وتقية وتقي، أي توقي الله أو النار أو المعاصي أو ما يخاف","what_is_not_ar":"لا يدخل فيه مطلق الوقاية المادية إلا إذا صار اتقاء للنفس"},"support_links":["sup_c9904beb5653fc047bc7"]},{"boundary":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B003","candidate_links":[{"candidate_id":"cand_5b909c34455ae4ceef13","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","surface_ar":"أَتْقَى"}],"gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek sözcüklü çekirdeğini ve atın ağrılı ya da hassas toynak nedeniyle gösterdiği sakınan yürüyüşü birlikte karşılar.","boundary_detail":"Çekirdek hafif topallama ve ağrılı ya da hassas toynak yüzünden sakınarak yürümedir; eyer, emir ve sert zemin kullanımları bağımlı yan kullanımlardır.","branch_image_ar":"توقي الدابة من وجع الحافر","concept_gloss":"hafif topallama ve toynak ağrısıyla yürümekten çekinme","contextual_glosses":[{"applicability":"Tek sözcüklü durum adı, neden veya hayvanın türü ayrıca belirtilmeden kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamanın hafif derecesini ve yürüyüş bozukluğu olmasını doğrudan korur."},"facet_ids":["F001"],"text":"hafif topallama","usage_role":"general"},{"applicability":"Atın topallaması veya toynak acısı yüzünden adım atmaktan çekinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan türünü, toynaktaki ağrıyı ve bunun yol açtığı çekingen yürüyüşü korur."},"facet_ids":["F002"],"text":"toynak ağrısıyla yürümekten çekinen at","usage_role":"explanatory"},{"applicability":"Topallayan hayvana ya da biniciye, mevcut aksamayı gözeterek yürümeyi sürdürmesi söylendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aksamayı sürdürme, onu hesaba katma ve hareketi zorlamama yönündeki emri korur."},"facet_ids":["F003"],"text":"aksayışını gözet ve ağırdan al","usage_role":"contextual"},{"applicability":"Eyerin hayvanın sırtında yara veya bere oluşturmadığı belirtilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyerin türünü ve hayvanın sırtını yaralamama sonucunu açıkça korur."},"facet_ids":["F004"],"text":"yara açmayan eyer","usage_role":"contextual"}],"definition":"Hafif topallama ile, özellikle toynak ağrısı veya hassasiyeti yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atın durumu. Aynı kullanım kümesi, hayvanın aksamasına göre davranmayı, sert zeminden yakınmamayı ve hayvanda yara açmayan eyeri de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tek sözcüklü temel anlam, hayvanın yürüyüşündeki hafif topallamadır."},{"facet_id":"F002","role":"specialization","statement":"At, topalladığı veya toynağındaki ağrı yüzünden yürümekten çekindiği ve sert zeminde ayağını sakındığı için bu nitelemeyi alır."},{"facet_id":"F003","role":"associated_use","statement":"Hayvana yönelik emir kalıbı, onun aksayışını gözeterek yürümeyi sürdürme ve kendini zorlamama anlamı taşır."},{"facet_id":"F004","role":"associated_use","statement":"Eyer için kullanıldığında hayvanın sırtını yaralamayan veya berelenmesine yol açmayan eyer anlatılır."},{"facet_id":"F005","role":"associated_use","statement":"Sert ve engebeli zeminle kurulan olumsuz emir, arazinin güçlüğünden yakınmama anlamına gelir."}],"identity_rationale":"Kaynak ifadesi yalnızca toynak ağrısından kaçınmayı değil, hafif topallamayı, topallayan atın davranışını, hayvanda yara açmayan eyeri ve aksayışa göre davranma sözünü birlikte verir. Bu nedenle dal korunabilir, fakat geçici hayvanın kendini koruması çerçevesi bütün malzemeyi taşıyacak biçimde aksama ve ona bağlı kullanımlar olarak yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hafif topallama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"topallayan, toynak ağrısıyla yürümekten çekinen veya ayağını sert zeminden sakınan at"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"hayvanın sırtında yara açmayan eyer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"aksayışını gözet ve ağırdan al"}],"lexicalization_note":"Tek sözcüklü hafif topallama anlamı, atın yürüyüşü ile eyer ve emir kalıplarına bağlı anlamlardan açıkça ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan ilişkiler genel aksama, uzuv hastalığı, toynak anatomisi ve koruma bağlantısını ayırır. Keçi hastalıkları, düzensiz yürüyüş, binme ve öteki kök içi dallar daha uzak alan ortaklıklarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hafif dereceyi ve toynak ağrısına bağlı çekingen yürüyüşü belirginleştirir; komşu dal daha genel aksama durumunda kalır.","focus_only":"Toynak ağrısıyla yürümekten çekinme ile yara açmayan eyer ve emir gibi bağımlı kullanımları da kapsar.","gloss":"hafif topallama ile hayvandaki genel aksama","neighbor_only":"Hayvandaki aksama veya eziklik daha genel bir durum adı olarak verilir ve koruyucu yan kullanımlar taşımaz.","neighbor_ref":"root_000448/B009","relation_type":"near_synonym","shared_zone":"Her iki dal hayvanın, özellikle atın, aksayan veya topallayan yürüyüşünü anlatır."},{"boundary_match":"partial","distinction":"Bu dal ağrının yürüyüşteki belirtisini ve sakınma davranışını anlatır; komşu dal ise ağrıyı doğuran hastalık veya yaralanmanın kendisini adlandırır.","focus_only":"Ağrıya verilen topallama ve yürümekten çekinme tepkisi ile ona bağlı kullanımlar merkezde yer alır.","gloss":"ağrılı yürüyüş ile uzuvdaki hastalık","neighbor_only":"Omuz veya toynağı etkileyen hastalığı ve taşın tırnak ya da toynağı çizmesini doğrudan adlandırır.","neighbor_ref":"root_001546/B006","relation_type":"near_neighbor","shared_zone":"İki dal toynak veya başka bir uzuvdaki ağrı ve bunun hayvan üzerindeki etkisiyle ilgilidir."},{"boundary_match":"field_only","distinction":"Ortak alan toynaktır; bu dal toynağa bağlı ağrı ve yürüyüş davranışını, komşu dal ise anatomik uzvun kendisini tanımlar.","focus_only":"Toynak ağrısının yol açtığı topallama ve sakınan yürüyüşü anlatır.","gloss":"toynak ağrısıyla yürüme ile toynak","neighbor_only":"Toynağın kendisini, biçimini ve zeminde iz açan uzuv olmasını adlandırır.","neighbor_ref":"root_000341/B002","relation_type":"same_field","shared_zone":"Her iki dal atın veya başka bir hayvanın toynağını ortak katılımcı olarak içerir."},{"boundary_match":"field_only","distinction":"Bu dal bir yürüyüş durumu ve ağrı tepkisidir; komşu dal ise toynağın sağ ve sol yanlarını gösteren anatomik addır.","focus_only":"Hayvanın ağrı nedeniyle aksaması ve sert zeminde ayağını sakınması bulunur.","gloss":"toynak ağrısı ile toynağın yanları","neighbor_only":"Toynağın iki yanındaki belirli anatomik bölümleri adlandırır.","neighbor_ref":"root_000358/B010","relation_type":"same_field","shared_zone":"Her iki dal toynak yapısı ve hayvanın ayağı çevresindeki aynı somut alana bağlıdır."},{"boundary_match":"thematic_only","distinction":"Koruma bu dalda yalnızca bazı at ve eyer kullanımlarının bağımlı yönüdür; komşu dalda ise bütün kavramın genel çekirdeğidir.","focus_only":"Hafif topallama ve ağrı yüzünden sakınarak yürüme, dalın temel kimliğini oluşturur.","gloss":"aksayarak sakınma ile genel koruma","neighbor_only":"Her tür varlığı zarardan korumak için araya araç veya engel koyan genel işlemi tanımlar.","neighbor_ref":"root_001677/B001","relation_type":"thematic","shared_zone":"Atın ayağını sert zeminden sakınması ve eyerin yara açmaması koruma düşüncesiyle ilişki kurar."}],"source_phrase_ar":"الوقى هو الظلع اليسير (maqayis)؛ فرس واق إذا كان ظالعا (ayn)؛ ق على ظلعك أي الزمه (sihah)؛ فرس واق إذا كان يهاب المشي من وجع يجده في حافره (sihah)؛ سرج واق إذا لم يكن معقرا (sihah;tahdhib)؛ لا تقي بالجدجد أي لا تشتكي حزونة الأرض (tahdhib)","source_summary":"Toplu kaynak ifadesi hafif topallamayı çekirdek yapar ve bunu topallayan, toynak ağrısı yüzünden yürümekten çekinen ya da sert zeminde ayağını sakınan atla açımlar. Aksamaya göre davranma, sert zeminden yakınmama ve yara açmayan eyer kullanımları aynı kümede yer alan fakat çekirdeğe bağımlı yan kullanımlardır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الوَقَى بمعنى الظلع اليسير، والفرس الواقي إذا يهاب المشي أو يقي حافره الموضع الغليظ، والسرج الواقي غير المعقر","what_is_not_ar":"لا يدخل فيه الوقاية العامة ولا التقوى ولا اسم الصرد"},"support_links":["sup_69f8a590a5c636481a8c"]},{"boundary":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001677/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","surface_ar":"أَتْقَى"}],"gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçü ailesinin iki bağlama göre değişen değerini tek açıklayıcı karşılıkta birlikte göstermenin gerektiği yerlerde kullanılır.","boundary_detail":"Dal yalnızca bu adlandırılmış ağırlık ölçüsü ve onun biçimleriyle sınırlıdır; genel tartma eylemine, her türlü miktara veya modern bir ölçü adına genişletilmez.","branch_image_ar":"الأوقية وزن معلوم","concept_gloss":"kırk gümüş para ağırlığındaki, yağda yedi birimlik biçimi bulunan ölçü","contextual_glosses":[{"applicability":"Para ağırlığının esas alındığı ilk biçim ve kullanım kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçünün ağırlık niteliğini ve kırk gümüş para ağırlığına eşit değerini korur."},"facet_ids":["F001"],"text":"kırk gümüş para ağırlığına denk ölçü","usage_role":"contextual"},{"applicability":"Başındaki ses düşmüş biçimin yağ ölçümündeki özel değeri açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağ bağlamını, ağırlık ölçüsü olmasını ve yedi temel birime eşit değeri korur."},"facet_ids":["F002"],"text":"yağ için yedi temel birimlik ağırlık ölçüsü","usage_role":"explanatory"},{"applicability":"Ölçü adının birden fazla çoğul söylenişi bulunduğu açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Söz konusu biçimlerin aynı ağırlık ölçüsü adının çoğulları olmasını korur."},"facet_ids":["F003"],"text":"bu ağırlık ölçüsünün çoğul biçimleri","usage_role":"explanatory"}],"definition":"Bir kullanımda kırk gümüş paranın ağırlığına, başındaki ses düşmüş başka bir biçim ve kullanımda ise yağ için yedi temel ağırlık birimine eşit kabul edilen ölçü. İlk biçim daha düzgün sayılır ve birden çok çoğul biçimi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel biçim, belirli bir ağırlık ölçüsüdür ve para hesabında kırk gümüş paranın ağırlığına eşitlenir."},{"facet_id":"F002","role":"source_variant","statement":"Başındaki ses düşmüş biçim, yağ ölçümünde kullanılan ve yedi temel ağırlık birimine eşit sayılan ayrı bir değeri bildirir."},{"facet_id":"F003","role":"source_variant","statement":"Başlangıç sesini koruyan biçim daha düzgün kabul edilir ve ölçü adının iki çoğul söylenişi kaydedilir."}],"identity_rationale":"Kaynak ifadesi dalı bilinen bir ağırlık ölçüsü olarak doğrular, ancak tek ve değişmez bir nicelik vermez. Bir kullanım kırk gümüş para ağırlığını, başındaki ses düşmüş başka bir biçim ise yağ için yedi temel ağırlık birimini gösterir; tanım bu bağlam farkını açıkça korumalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kırk gümüş para ağırlığına eşit bilinen ölçü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yağ için yedi temel ağırlık birimine eşit ölçü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bu ağırlık ölçüsü adının çoğul biçimleri"}],"lexicalization_note":"Tanım, iki sözcük biçimine bağlı farklı ölçü değerlerini ve çoğul biçimleri ayırır; bunlardan genel bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlananlar genel ağırlık, küçük para ölçüsü, başka geleneksel birim, hacim-miktar ölçüsü ve ayar standardı sınırlarını gösterir. Artış ve çok büyük tahıl ölçüsü daha uzaktır; öteki kök içi dallar anlamsal olarak ayrıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal değerleri ve sözcük biçimleri belirlenmiş tek bir geleneksel ölçüyü adlandırır; komşu dal ağırlık ve tartma alanının genel kavramıdır.","focus_only":"Bağlama göre kırk gümüş para veya yedi temel birim değerini taşıyan belirli bir ölçü adıdır.","gloss":"özel ağırlık ölçüsü ile genel tartma","neighbor_only":"Ağırlık, tartı aracı ve bir şeye ağırlığını verme gibi genel ölçme alanını kapsar.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirlenmiş ağırlık ve ölçme düşüncesinde buluşur."},{"boundary_match":"partial","distinction":"Ölçülerin adları ve değerleri ayrıdır: bu dal kırk paralık değeri ve yağdaki değişkeyi taşırken komşu dal çoğunlukla beş paralık küçük miktarı bildirir.","focus_only":"Para hesabında kırk gümüş para ağırlığına veya yağda yedi birime bağlanan ölçüdür.","gloss":"kırk paralık ölçü ile beş paralık ölçü","neighbor_only":"Altın veya gümüş için kullanılan, çoğunlukla beş gümüş para ağırlığıyla açıklanan daha küçük ölçüdür.","neighbor_ref":"root_001570/B004","relation_type":"near_neighbor","shared_zone":"İki dal da değerli maden veya para üzerinden açıklanan geleneksel ağırlık ölçüleridir."},{"boundary_match":"partial","distinction":"Bu dalın ölçü adı ve verilen değerleri kendine özgüdür; komşu dal başka birim adını ve ağırlığın yanında hacim kullanımını kapsar.","focus_only":"İki sözcük biçimi ve iki bağlamsal değeri bulunan belirli bir ağırlık ölçüsüdür.","gloss":"iki ayrı geleneksel ölçü adı","neighbor_only":"Başka bir adla anılan, hem ağırlık hem hacim ölçüsü olabilen ayrı bir geleneksel birimdir.","neighbor_ref":"root_001449/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli adları, tekil ve çoğul biçimleri bulunan geleneksel ölçü birimleridir."},{"boundary_match":"partial","distinction":"Bu dal ağırlığa ve belirli değerlere bağlıdır; komşu dal hacim ile para miktarı arasında daha geniş bir ölçüm alanına yayılır.","focus_only":"Öncelikle ağırlık ölçüsüdür ve iki özel sayısal değere bağlanır.","gloss":"ağırlık ölçüsü ile hacim ve miktar ölçüsü","neighbor_only":"Hacim ölçüsünü, yarım başka bir hacim ölçüsünü ve para miktarını birlikte kapsayabilir.","neighbor_ref":"root_001224/B007","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir veya ölçülebilir bir miktarı geleneksel birimle belirtir."},{"boundary_match":"field_only","distinction":"Bu dal ölçülen miktarı bildiren birimdir; komşu dal ise ölçü araçlarının ve paraların doğruluğunu belirleyen ayar standardıdır.","focus_only":"Kendi adı, biçimleri ve geleneksel değerleri bulunan ölçü birimini tanımlar.","gloss":"ölçü birimi ile ölçü ayarı","neighbor_only":"Ölçekleri ve paraları denetlemeye yarayan ayarı veya ölçünleme işlemini tanımlar.","neighbor_ref":"root_001066/B013","relation_type":"same_field","shared_zone":"Her iki dal doğru ağırlık ve ölçü değerinin belirlenmesi alanındadır."}],"source_phrase_ar":"الأوقية في الحديث أربعون درهما (sihah;tahdhib)؛ الوقية وزن من أوزان الدهن وهي سبعة مثاقيل (tahdhib)؛ اللغة الجيدة أوقية وجمعها أواقي وأواق (tahdhib)","source_summary":"Toplu kaynak anlatımı, aynı ölçü ailesinde bağlama ve sözcük biçimine göre iki değer aktarır: para hesabında kırk gümüş para ağırlığı ve yağ hesabında yedi temel ağırlık birimi. Başlangıç sesini taşıyan biçim daha düzgün kabul edilir; ölçü adının iki çoğul biçimi de verilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الأوقية والأواقي بوصفها وزنا معلوما للدراهم أو الدهن","what_is_not_ar":"لا يدخل فيه الوقاية ولا التقوى ولا الواقي بمعنى الصرد"},"support_links":[]},{"boundary":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_kind":"non_bare","branch_ref":"root_001677/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","surface_ar":"أَتْقَى"}],"gloss":"örümcek kuşu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}}],"root_ar":"و ق ي","root_id":"root_001677","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş türünün Türkçedeki doğal adı olarak dalın adlandırma çekirdeğini doğrudan karşılar.","boundary_detail":"Dal yalnızca örümcek kuşunun bu iki adına ve adlandırma açıklamasına aittir; koruyan kişi, topallayan at veya yara açmayan eyer anlamlarına geçmez.","branch_image_ar":"الواقي اسم للصرد","concept_gloss":"örümcek kuşu","contextual_glosses":[{"applicability":"Kuş adının yürüyüş biçimiyle ilişkilendirilen açıklaması da bağlamda görünür kılınmak istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuş türünü ve adlandırmaya gerekçe gösterilen kısa adımlı yürüyüş özelliğini birlikte korur."},"facet_ids":["F001","F003"],"text":"kısa adımlarla yürüyen örümcek kuşu","usage_role":"explanatory"}],"definition":"Örümcek kuşunun, biri son sesi koruyan diğeri bu sesi düşüren iki biçimde söylenen adı. Adlandırma, kuşun yürürken adımlarını fazla açmamasıyla açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, örümcek kuşunu adlandıran özel bir kuş adıdır."},{"facet_id":"F002","role":"source_variant","statement":"Kuş adı, son sesi bulunan daha uzun ve bu sesin düştüğü daha kısa iki biçimde kullanılır."},{"facet_id":"F003","role":"associated_use","statement":"Adın kuşa verilmesi, yürürken adımlarını fazla açmayan kısa adımlı yürüyüşüyle açıklanır."}],"identity_rationale":"Kaynak ifadesi dalı doğrudan örümcek kuşunun adı olarak verir, adın son sesi bulunan ve düşmüş iki biçimini kaydeder ve adlandırmayı kuşun yürürken adımlarını fazla açmamasına bağlar. Geçici çerçeve bu sınırı doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"örümcek kuşu; aynı kuş adının uzun ve kısalmış biçimleri"}],"lexicalization_note":"Tanım, kuşa verilmiş iki özel ad biçimiyle sınırlı tutulur ve bunlardan genel bir koruma ya da yürüme anlamı türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan dört karşılaştırma kuş adları arasındaki tür ayrımını yeterince gösterir. Öteki kuş adayları da yalnızca aynı alanı paylaşır; kurt adı ile koruma, ağırlık ve hayvan yürüyüşü dalları farklı kimliklerdir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortaklık yalnızca kuş adı olmalarıdır; bu dal örümcek kuşunu, komşu dal ise ibibiği adlandırır ve türler birbirinin yerine geçmez.","focus_only":"Örümcek kuşunu ve onun kısa adımlı yürüyüşüne bağlanan adını belirtir.","gloss":"örümcek kuşu ile ibibik","neighbor_only":"İbibik kuşunu ve o kuşa ait ad biçimlerini belirtir.","neighbor_ref":"root_001580/B005","relation_type":"same_field","shared_zone":"Her iki dal belirli bir kuş türünü doğrudan adlandıran sözleri içerir."},{"boundary_match":"field_only","distinction":"Bu dal örümcek kuşunun adıdır; komşu dal tarla kuşunun adıdır. Aynı üst alanda bulunsalar da tür kimlikleri ayrıdır.","focus_only":"Kısa adımlı yürüyüşüyle açıklanan örümcek kuşu adı merkezde yer alır.","gloss":"örümcek kuşu ile tarla kuşu","neighbor_only":"Tarla kuşunu ve ona ait farklı ad biçimlerini belirtir.","neighbor_ref":"root_001195/B003","relation_type":"same_field","shared_zone":"İki dal da küçük kuş türlerine verilmiş adları ve bu adların biçimlerini ele alır."},{"boundary_match":"field_only","distinction":"Anlamsal ortaklık kuş kategorisiyle sınırlıdır; dallar büyüklük, yapı ve tür bakımından bütünüyle farklı kuşları adlandırır.","focus_only":"Örümcek kuşunun özel adını bildirir.","gloss":"örümcek kuşu ile deve kuşu","neighbor_only":"Çok daha büyük ve uçamayan deve kuşunun tür adını bildirir.","neighbor_ref":"root_001525/B006","relation_type":"same_field","shared_zone":"Her iki dal bir kuş türünün doğrudan adı olarak kullanılır."},{"boundary_match":"field_only","distinction":"Bu dalın göndergesi örümcek kuşudur; komşu dal başka bir küçük kuş türünü adlandırır ve ortak kuş alanı tür özdeşliği oluşturmaz.","focus_only":"Örümcek kuşunu adlandırır ve adını kuşun yürüyüşüyle ilişkilendirir.","gloss":"örümcek kuşu ile bir serçe türü","neighbor_only":"Serçelere benzeyen başka bir küçük kuş türünün adını bildirir.","neighbor_ref":"root_000465/B008","relation_type":"same_field","shared_zone":"İki dal da küçük kuşlardan birine verilmiş sözlü adları taşır."}],"source_phrase_ar":"الواقي الصرد (sihah;tahdhib)؛ الواق بكسر القاف بلا ياء (sihah)؛ قيل للصرد واق لأنه لا ينبسط في مشيه (tahdhib)","source_summary":"Kaynakların ortak anlatımı bu sözcüğü örümcek kuşunun adı olarak tanımlar ve son sesi bulunan biçimin yanında o sesin düştüğü kısa biçimi de kaydeder. Adın nedeni, kuşun yürürken adımlarını fazla açmaması olarak açıklanır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الواقي والواق اسما للصرد","what_is_not_ar":"لا يدخل فيه الواقي بمعنى الدافع ولا الفرس الواقي ولا السرج الواقي"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:17:1"],"branch_refs":[],"candidate_id":"cand_33595df751d5eb07b5d8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:17:1:wa-sa-onset","source_type":"word_analysis","support_ids":["sup_2365ffc6053c7ea26f6a","sup_2d871492eb9cabfee1b8"],"title":"pivot and future marker fuse at the onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:1","qac_refs":["92:17:1:1"],"status":"accepted"}},{"anchor_refs":["92:17:1"],"branch_refs":[],"candidate_id":"cand_2939b70687dd78918327","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:17:1:warning-rescue-pivot","source_type":"word_analysis","support_ids":["sup_2365ffc6053c7ea26f6a","sup_2b48b24141b8a41ffa7c"],"title":"connector pivots from warning to rescue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:1","qac_refs":["92:17:1:1"],"status":"accepted"}},{"anchor_refs":["92:17:1"],"branch_refs":[],"candidate_id":"cand_c52bf0cc7429b71721cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:17:1:whole-clause-scope","source_type":"word_analysis","support_ids":["sup_2365ffc6053c7ea26f6a","sup_d3b03af9ab9dc4330029"],"title":"particle links the whole promised outcome","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:1","qac_refs":["92:17:1:1"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_657076839f608d18d45d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:attached-fire-object","source_type":"word_analysis","support_ids":["sup_263c471aa377887cee58","sup_2650e29cd21f2cb8fd75"],"title":"suffix keeps the Fire as the separation object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_878bf185bda83088ad71","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:causative-not-reflexive","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_55aba204adfa3480d2f3"],"title":"Form II passive differs from self-avoidance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_0d2bf3b45f3cbe989d7f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:contested-shelter-echo","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_823de5f3f436536683a6"],"title":"disputed shelter echo remains only as contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_5c390e03b3c5449e8ec7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:delayed-subject-promise","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_f82bf3431537625064b3"],"title":"verb arrives before the saved identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_7ae6bf90ab1aed55ad2c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:fire-reversal","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_bcacaa142b4e66eb9e77"],"title":"same Fire referent receives the opposite relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_5993080ba9eedf625de6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:future-passive-rescue","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_bd1f2373c62103cbb339"],"title":"future passive makes rescue received and certain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_7ee1e52a5dd7e09f1f7a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:protection-root-pair","source_type":"word_analysis","support_ids":["sup_0756bf2909d0b116d7f7","sup_2650e29cd21f2cb8fd75"],"title":"distancing pairs with guarding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_5c34e22ffe072ce2749e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:side-distance-image","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_81dbad185747bed275e0"],"title":"side-root image makes removal spatially concrete","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_7ca7aeff7dcbae8c94f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:sound-compression","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_c00ffcc029e32d2588d0"],"title":"compact sound carries promise and object together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_d4f9565c8037e31b5f77","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:2:withdrawal-to-rescue","source_type":"word_analysis","support_ids":["sup_2650e29cd21f2cb8fd75","sup_cb46d2f3706d80374a42"],"title":"active turning-away yields to passive rescue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:2","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_978e73a1cae2bc29d0a9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:act-to-identity","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_f911670c2bbe30c4e028"],"title":"same root moves from act to identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_9ba8ac5186426529e897","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:agreement-separates-roles","source_type":"word_analysis","support_ids":["sup_5ba5d7128e00e2969f77","sup_61cb4b627466c404a77e"],"title":"agreement separates subject from Fire suffix","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_78a97bbd8d72f2f5a70f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:definite-peak-type","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_80a794f6d5e2185bfcf9"],"title":"definite superlative names a peak type","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_c17f5917d276825cf54e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:delayed-final-reveal","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_71917623f0664a3b1e30"],"title":"delayed subject lands as final reveal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_f90d5ba1e998b8bd7b3b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:forward-definition","source_type":"word_analysis","support_ids":["sup_1cb6f7c0f76b19e24df2","sup_61cb4b627466c404a77e"],"title":"complete subject still opens definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_4a5aba261bb086e6a561","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:guarding-shield-field","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_82ac4a006507dc99e1ea"],"title":"guarding field supplies protective force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_9a853685463943a7e2da","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:honor-criterion-echo","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_8eb119ffbaff03d3f4d5"],"title":"superlative links rescue and honor criterion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_7c76916e8087fef84956","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:opposite-superlatives","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_d2d5f514a7b986094406"],"title":"opposite superlatives frame opposite Fire relations","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_cf57a811fb051fd63a6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:passive-subject","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_ff7050ddff1c81e153c4"],"title":"elative becomes the rescued passive subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_6f7f47324c4e8e69dcfe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:protection-pair","source_type":"word_analysis","support_ids":["sup_14944ddd01d60108a0fc","sup_61cb4b627466c404a77e"],"title":"self-shielding meets external distancing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_63b8128db54649139b93","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:rare-elative-peak","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_e3e9c4330b05395497e3"],"title":"rare elative marks the apex of a common field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_4506888394cbe9772690","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:self-guarding-morphology","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_ebb7c134047bcb4eea16"],"title":"reflexive guarding becomes superlative identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:3"],"branch_refs":[],"candidate_id":"cand_01d1259b488d5b9cdbd1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:3:sound-rhyme-release","source_type":"word_analysis","support_ids":["sup_61cb4b627466c404a77e","sup_bbabb2bca6f61457be9a"],"title":"final sound answers the opposite extreme","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:17:3","qac_refs":["92:17:2:1","92:17:2:2"],"status":"accepted"}},{"anchor_refs":["92:17:1"],"branch_refs":[],"candidate_id":"cand_6e9583d4dc4e15b18839","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000262"],"scope":"focus_ayah","source_local_id":"92:17:1:3","source_type":"qac_morpheme","support_ids":["sup_1fd5e2fc9888a4be0e66"],"title":"QAC root occurrence: ج ن ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:17:2"],"branch_refs":[],"candidate_id":"cand_6a3092cfd2c1334ce984","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001677"],"scope":"focus_ayah","source_local_id":"92:17:2:2","source_type":"qac_morpheme","support_ids":["sup_f76aec05c7f78669de28"],"title":"QAC root occurrence: و ق ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:17","branch_refs":["root_000262/B003","root_001677/B002"],"candidate_id":"cand_be84f0bc12bd73f104ee","commentary_obligation":"review","hft_ref":"hft_23f60b25072a4de4bd02","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_passive_completion_of_self_guarding","source_type":"hft","support_ids":["sup_c9904beb5653fc047bc7"],"title":"b01_passive_completion_of_self_guarding","trust":"legacy_unbound"},{"anchor_refs":["92:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:17","branch_refs":["root_000262/B001","root_000262/B011","root_001677/B001"],"candidate_id":"cand_13684e2604e7488c4c6a","commentary_obligation":"review","hft_ref":"hft_c4d37ca478b291a9de00","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_safe_flank_and_side_shield","source_type":"hft","support_ids":["sup_f71a62865a6b271f833c"],"title":"b02_safe_flank_and_side_shield","trust":"legacy_unbound"},{"anchor_refs":["92:17"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:17","branch_refs":["root_000262/B005","root_001677/B003"],"candidate_id":"cand_5b909c34455ae4ceef13","commentary_obligation":"review","hft_ref":"hft_073f8254dfb82156ef94","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_guarded_escort_at_the_edge","source_type":"hft","support_ids":["sup_69f8a590a5c636481a8c"],"title":"b03_guarded_escort_at_the_edge","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:17:1:1","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|sa+","morpheme_role":"PREFIX","pos":"FUT","qac_ref":"92:17:1:2","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"سَ"},{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","root_ar":"ج ن ب","surface_ar":"يُجَنَّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:17:1:4","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:17:2:1","qac_word_ref":"92:17:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","root_ar":"و ق ي","surface_ar":"أَتْقَى"}],"word_analysis_qac_refs":[["92:17:1:1"],["92:17:1:2","92:17:1:3","92:17:1:4"],["92:17:2:1","92:17:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:17:1","92:17:2","92:17:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:17:1:1","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|sa+","morpheme_role":"PREFIX","pos":"FUT","qac_ref":"92:17:1:2","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"سَ"},{"lemma_ar":"يُجَنَّبُ","morph_features":"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:17:1:3","qac_word_ref":"92:17:1","root_ar":"ج ن ب","surface_ar":"يُجَنَّبُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:17:1:4","qac_word_ref":"92:17:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:17:2:1","qac_word_ref":"92:17:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَتْقَى","morph_features":"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:17:2:2","qac_word_ref":"92:17:2","root_ar":"و ق ي","surface_ar":"أَتْقَى"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:17:1:1"],["92:17:1:2","92:17:1:3","92:17:1:4"],["92:17:2:1","92:17:2:2"]],"word_analysis_refs":["92:17:1","92:17:2","92:17:3"],"word_rows":[{"analysis_record_ref":"92:17:1","analytic_gloss_range_en":"connective particle that pivots from the Fire-warning panel into the promised rescue clause while keeping the contrast syntactically joined","analytic_root_gloss_range_en":null,"qac_refs":["92:17:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:17:2","analytic_gloss_range_en":"future passive causative distancing from the previously named Fire, with the saved person receiving removal rather than initiating self-avoidance","analytic_root_gloss_range_en":"side, flank, adjacency, avoidance, keeping aside, distance, foreignness, and several specialized branches; the local word selects caused separation from harm while side-distance imagery remains useful pressure","qac_refs":["92:17:1:2","92:17:1:3","92:17:1:4"],"root":{"arabic":"ج ن ب","transliteration":"j-n-b"},"surface":{"arabic":"سَيُجَنَّبُهَا","transliteration":"sayujannabuhā"}},{"analysis_record_ref":"92:17:3","analytic_gloss_range_en":"definite singular elative substantive meaning the most guarded or most God-conscious one, functioning here as the passive subject who is kept from the Fire","analytic_root_gloss_range_en":"warding harm off, protective covering, self-guarding, moral caution, taqwā, and specialized nonlocal branches; this word selects the peak moral self-guarding branch with protective-shield imagery","qac_refs":["92:17:2:1","92:17:2:2"],"root":{"arabic":"و ق ي","transliteration":"w-q-y"},"surface":{"arabic":"ٱلْأَتْقَى","transliteration":"al-atqā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["92:17"],"branch_refs":["root_000262/B003","root_001677/B002"],"candidate_id":"cand_be84f0bc12bd73f104ee","evidence_scope":"focus_ayah","hft_ref":"hft_23f60b25072a4de4bd02","item_id":"b01_passive_completion_of_self_guarding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_passive_completion_of_self_guarding","support_id":"sup_c9904beb5653fc047bc7"},{"anchor_refs":["92:17"],"branch_refs":["root_000262/B001","root_000262/B011","root_001677/B001"],"candidate_id":"cand_13684e2604e7488c4c6a","evidence_scope":"focus_ayah","hft_ref":"hft_c4d37ca478b291a9de00","item_id":"b02_safe_flank_and_side_shield","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_safe_flank_and_side_shield","support_id":"sup_f71a62865a6b271f833c"},{"anchor_refs":["92:17"],"branch_refs":["root_000262/B005","root_001677/B003"],"candidate_id":"cand_5b909c34455ae4ceef13","evidence_scope":"focus_ayah","hft_ref":"hft_073f8254dfb82156ef94","item_id":"b03_guarded_escort_at_the_edge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_guarded_escort_at_the_edge","support_id":"sup_69f8a590a5c636481a8c"}],"diagnostics":[],"lane_counts":{"global":17,"macro":7,"micro":3},"packet_summary":{"ayah_count":21,"focus_ref":"92:17","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:17","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"92:17","lane":"micro","linguistic_source_ref":"92:17","surface_ref":"92:17","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:17","target_tokens":[["En",["92:17:2"]],["çok",["92:17:2"]],["sakınan",["92:17:2"]],["ise",["92:17:1","92:17:2"]],["ondan",["92:17:1"]],["uzak",["92:17:1"]],["tutulacaktır",["92:17:1"]]],"text":"En çok sakınan ise ondan uzak tutulacaktır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":12,"ayah_to":21,"id":"s092-p02-012-021","label":"Guidance, fire, and generous salvation","number":2,"refs":["92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:protection-root-pair","source_type":"word_analysis","support_id":"sup_0756bf2909d0b116d7f7","text":"{\"blocking_evidence\":null,\"headline\":\"distancing pairs with guarding\",\"reader_payoff\":\"The reader sees the root of distancing paired locally with the root of guarding, so self-protection and external separation converge.\",\"reason\":\"The local attachment joins the {{ar:ج ن ب}} ({{tr:j-n-b}}) verb to the {{ar:و ق ي}} ({{tr:w-q-y}}) subject, and the contextual collocation profile records this exact root-form pairing.\",\"representative_source_ids\":[\"QI-74f07cae\",\"QE-f94a0568\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:protection-pair","source_type":"word_analysis","support_id":"sup_14944ddd01d60108a0fc","text":"{\"blocking_evidence\":null,\"headline\":\"self-shielding meets external distancing\",\"reader_payoff\":\"The reader sees the guarded person's inward protection matched by external removal from harm.\",\"reason\":\"The local collocation joins the {{ar:و ق ي}} ({{tr:w-q-y}}) subject to the {{ar:ج ن ب}} ({{tr:j-n-b}}) passive verb.\",\"representative_source_ids\":[\"QI-f21578d7\",\"ME-ea5d6ac2\",\"QY-71387920\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:forward-definition","source_type":"word_analysis","support_id":"sup_1cb6f7c0f76b19e24df2","text":"{\"blocking_evidence\":null,\"headline\":\"complete subject still opens definition\",\"reader_payoff\":\"The reader feels the clause close syntactically while still leaning forward to the defining description in 92:18-21.\",\"reason\":\"The word completes the passive clause, while the following relative clauses in 92:18-21 define the identified figure.\",\"representative_source_ids\":[\"QG-8a17e73b\",\"QS-13ce0f12\",\"QB-d72a6a36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:17:1:3","source_type":"qac_morpheme","support_id":"sup_1fd5e2fc9888a4be0e66","text":"{\"lemma_ar\":\"يُجَنَّبُ\",\"morph_features\":\"STEM|POS:V|IMPF|PASS|(II)|LEM:yujan~abu|ROOT:jnb|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:17:1:3\",\"qac_word_ref\":\"92:17:1\",\"root_ar\":\"ج ن ب\",\"surface_ar\":\"يُجَنَّبُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:1","source_type":"word_analysis","support_id":"sup_2365ffc6053c7ea26f6a","text":"{\"gloss_range\":\"connective particle that pivots from the Fire-warning panel into the promised rescue clause while keeping the contrast syntactically joined\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is small, but it makes 92:17 arrive as the counter-turn to the Fire panel rather than as an isolated sentence. It can be heard as both connection and fresh resumption: the warning remains in view, yet the promise opens as its own declaration. Because the particle scopes over the whole future passive clause, it links the entire outcome, not only the next verb, to what came before. Its direct fusion with {{ar:سَيُجَنَّبُهَا}} ({{tr:sayujannabuhā}}) also makes the pivot and the promised future move in one compact onset.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:attached-fire-object","source_type":"word_analysis","support_id":"sup_263c471aa377887cee58","text":"{\"blocking_evidence\":null,\"headline\":\"suffix keeps the Fire as the separation object\",\"reader_payoff\":\"The reader sees that the promise is specifically distance from the Fire already introduced, not a generic rescue formula.\",\"reason\":\"Attachment evidence marks the feminine suffix as the retained clitic object and links it to {{ar:نَارًا}} ({{tr:nāran}}) in 92:14.\",\"representative_source_ids\":[\"QG-d555ef17\",\"QG-ebaae5a1\",\"MT-5e55d576\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2","source_type":"word_analysis","support_id":"sup_2650e29cd21f2cb8fd75","text":"{\"gloss_range\":\"future passive causative distancing from the previously named Fire, with the saved person receiving removal rather than initiating self-avoidance\",\"prose\":\"{{ar:سَيُجَنَّبُهَا}} ({{tr:sayujannabuhā}}) compresses the promise into one future passive form: the most guarded one will be caused to be kept away, while the causer remains unnamed. The attached {{ar:هَا}} ({{tr:hā}}) keeps the Fire from 92:14 inside the verb as the object of separation, so the clause does not describe vague safety; it promises distance from that same threat. The Form II passive differs from reflexive avoidance forms: the decisive movement is received, not self-produced. At the same time, the root's side and avoidance field makes the rescue spatially concrete, as if the person is set aside from the Fire's domain rather than merely told to avoid it. Beside the following guarded subject, the distancing root forms a protection cluster: inward self-guarding and external separation converge. The disputed garden or concealment near-echo remains only as a shelter-versus-Fire contrast, while the local word stays the caused-distancing verb. The word also answers the earlier Fire-contact wording in 92:15 and the active turning-away of 92:16: culpable withdrawal gives way to promised protective displacement. Because the verb and object suffix arrive before the subject, the promise of removal is heard before the saved identity lands. Its compact sound, with future prefix, doubled middle, nasal cluster, and final object suffix, lets promise, removal, and Fire-reference arrive as a single verbal unit.\",\"root_display\":\"{{ar:ج ن ب}} ({{tr:j-n-b}})\",\"root_gloss_range\":\"side, flank, adjacency, avoidance, keeping aside, distance, foreignness, and several specialized branches; the local word selects caused separation from harm while side-distance imagery remains useful pressure\",\"surface_display\":\"{{ar:سَيُجَنَّبُهَا}} ({{tr:sayujannabuhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:1:warning-rescue-pivot","source_type":"word_analysis","support_id":"sup_2b48b24141b8a41ffa7c","text":"{\"blocking_evidence\":null,\"headline\":\"connector pivots from warning to rescue\",\"reader_payoff\":\"The reader notices that the rescue promise is both joined to the Fire warning and launched as a counter-declaration.\",\"reason\":\"QAC marks {{ar:وَ}} ({{tr:wa}}) as a conjunction, and the local clause evidence lets it connect the prior warning panel to the new passive promise.\",\"representative_source_ids\":[\"QG-25ffb110\",\"QG-5ecf6f0c\",\"MT-b58e6e05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:1:wa-sa-onset","source_type":"word_analysis","support_id":"sup_2d871492eb9cabfee1b8","text":"{\"blocking_evidence\":null,\"headline\":\"pivot and future marker fuse at the onset\",\"reader_payoff\":\"The reader hears the transition into promise immediately, with no heavy pause between contrast and future rescue.\",\"reason\":\"The surface joins {{ar:وَ}} ({{tr:wa}}) directly to the future-marked passive verb, so the formal observation is locally anchored.\",\"representative_source_ids\":[\"QF-09b3bca3\",\"QF-e944ddfb\",\"QP-706f85b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:causative-not-reflexive","source_type":"word_analysis","support_id":"sup_55aba204adfa3480d2f3","text":"{\"blocking_evidence\":null,\"headline\":\"Form II passive differs from self-avoidance\",\"reader_payoff\":\"The reader notices that the form makes avoidance caused for the person rather than chosen as an independent reflexive act.\",\"reason\":\"The local form is passive Form II with a clitic object, not a Form VIII reflexive avoidance construction.\",\"representative_source_ids\":[\"QS-3f5e4a2d\",\"QF-c50a89d8\",\"MF-f9566a81\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:agreement-separates-roles","source_type":"word_analysis","support_id":"sup_5ba5d7128e00e2969f77","text":"{\"blocking_evidence\":null,\"headline\":\"agreement separates subject from Fire suffix\",\"reader_payoff\":\"The reader sees who is kept away and what is kept away from, even though both relations are packed into a short clause.\",\"reason\":\"The masculine singular subject agrees with the passive verb, while the feminine suffix is the object linked to the Fire.\",\"representative_source_ids\":[\"QG-45d39b23\",\"QG-6d73f1bf\",\"QG-adda4811\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3","source_type":"word_analysis","support_id":"sup_61cb4b627466c404a77e","text":"{\"gloss_range\":\"definite singular elative substantive meaning the most guarded or most God-conscious one, functioning here as the passive subject who is kept from the Fire\",\"prose\":\"{{ar:ٱلْأَتْقَى}} ({{tr:al-atqā}}) is an elative adjective turned into the clause's substantive subject: the quality of maximal guarding becomes the person who receives rescue. Its masculine singular agreement keeps it distinct from the feminine Fire suffix, so the clause separates the avoided object from the rescued subject with unusual economy. The definite superlative makes the figure both recognizable and still awaiting definition; 92:18-21 will specify who this peak guarded one is. Lexically, the {{ar:و ق ي}} ({{tr:w-q-y}}) field brings guarding, shielding, and cultivated self-protection into the word, so the person kept from the Fire is not merely generically good but maximally oriented toward protection from harm. The form is marked because the common taqwā family is narrowed into a rare peak elative, and the surah has already shown the same root as an act in 92:5 before naming it here as identity. The same rare superlative also links rescue here with the Quranic honor criterion in 49:13. Placed after the verb and Fire suffix, the subject lands as the final reveal and release point of the promise. It also completes the opposite superlative pair in 92:15: two matching shapes stand at opposite relations to the same Fire, and the qā-final rhyme binds the extremes while their roots reverse the meaning.\",\"root_display\":\"{{ar:و ق ي}} ({{tr:w-q-y}})\",\"root_gloss_range\":\"warding harm off, protective covering, self-guarding, moral caution, taqwā, and specialized nonlocal branches; this word selects the peak moral self-guarding branch with protective-shield imagery\",\"surface_display\":\"{{ar:ٱلْأَتْقَى}} ({{tr:al-atqā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:delayed-final-reveal","source_type":"word_analysis","support_id":"sup_71917623f0664a3b1e30","text":"{\"blocking_evidence\":null,\"headline\":\"delayed subject lands as final reveal\",\"reader_payoff\":\"The reader feels the rescued identity arrive as the clause's final landing point.\",\"reason\":\"The passive verb and object suffix precede the subject, and the subject closes the ayah phonologically and syntactically.\",\"representative_source_ids\":[\"QT-dfbe67bc\",\"MT-6e2dd059\",\"QP-311e1ca9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:definite-peak-type","source_type":"word_analysis","support_id":"sup_80a794f6d5e2185bfcf9","text":"{\"blocking_evidence\":null,\"headline\":\"definite superlative names a peak type\",\"reader_payoff\":\"The reader sees a recognizable moral type, not only a comparative adjective.\",\"reason\":\"The definite article joined to the elative shape lets the adjective function substantively as the named subject.\",\"representative_source_ids\":[\"QG-25e9445b\",\"QS-1167a805\",\"QF-033556e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:side-distance-image","source_type":"word_analysis","support_id":"sup_81dbad185747bed275e0","text":"{\"blocking_evidence\":null,\"headline\":\"side-root image makes removal spatially concrete\",\"reader_payoff\":\"The reader pictures salvation as being set aside from the Fire's domain, while the local verb still means caused avoidance from the referenced Fire.\",\"reason\":\"V4 separates side/flank and keeping-aside branches, so the side image can survive as lexical pressure, while the local passive frame selects caused separation from the Fire.\",\"representative_source_ids\":[\"QS-49d10589\",\"QS-bd9f98d8\",\"QS-fe63d740\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:contested-shelter-echo","source_type":"word_analysis","support_id":"sup_823de5f3f436536683a6","text":"{\"blocking_evidence\":null,\"headline\":\"disputed shelter echo remains only as contrast\",\"reader_payoff\":\"The reader may hear a shelter-versus-Fire contrast, while the local word remains the caused-distancing verb from {{ar:ج ن ب}} ({{tr:j-n-b}}).\",\"reason\":\"The supplied relation to garden or concealment is disputed and not the aligned local root, so it cannot govern the parse; it survives only as a cautious echo.\",\"representative_source_ids\":[\"QS-76fbbdb5\",\"QE-f1f7076f\",\"ME-ed3ded88\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:guarding-shield-field","source_type":"word_analysis","support_id":"sup_82ac4a006507dc99e1ea","text":"{\"blocking_evidence\":null,\"headline\":\"guarding field supplies protective force\",\"reader_payoff\":\"The reader hears piety as maximized guarding and protection from harm, not as a vague moral compliment.\",\"reason\":\"V4 supports warding harm and self-guarding as accepted {{ar:و ق ي}} ({{tr:w-q-y}}) branches, and the local elative selects their moral peak.\",\"representative_source_ids\":[\"QS-042246cf\",\"QS-0f3ad252\",\"QS-599ad32a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:honor-criterion-echo","source_type":"word_analysis","support_id":"sup_8eb119ffbaff03d3f4d5","text":"{\"blocking_evidence\":null,\"headline\":\"superlative links rescue and honor criterion\",\"reader_payoff\":\"The reader can connect the rescued figure of 92:17 with the Quranic criterion of honor in 49:13.\",\"reason\":\"The rows provide the concrete 49:13 comparison, and the local word has the same elative identity without making that other verse control the local parse.\",\"representative_source_ids\":[\"QI-72944224\",\"QE-c2468739\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:sound-rhyme-release","source_type":"word_analysis","support_id":"sup_bbabb2bca6f61457be9a","text":"{\"blocking_evidence\":null,\"headline\":\"final sound answers the opposite extreme\",\"reader_payoff\":\"The reader hears the qā-final superlative rhyme bind the two moral extremes while their roots reverse the meaning.\",\"reason\":\"The surface cadence of {{ar:ٱلْأَتْقَى}} ({{tr:al-atqā}}) closely answers {{ar:ٱلْأَشْقَى}} ({{tr:al-ashqā}}) in 92:15.\",\"representative_source_ids\":[\"QP-a2809b9b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:fire-reversal","source_type":"word_analysis","support_id":"sup_bcacaa142b4e66eb9e77","text":"{\"blocking_evidence\":null,\"headline\":\"same Fire referent receives the opposite relation\",\"reader_payoff\":\"The reader tracks the same Fire referent from contact in 92:15 to separation in 92:17.\",\"reason\":\"The suffix in 92:17 resumes the same Fire noun introduced in 92:14 and answered by the Fire-contact wording in 92:15.\",\"representative_source_ids\":[\"QI-32508868\",\"MT-c427a121\",\"QE-f12f61a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:future-passive-rescue","source_type":"word_analysis","support_id":"sup_bd1f2373c62103cbb339","text":"{\"blocking_evidence\":null,\"headline\":\"future passive makes rescue received and certain\",\"reader_payoff\":\"The reader notices that the saved person is the recipient of a promised act of rescue, not the visible agent of self-removal.\",\"reason\":\"QAC and attachment evidence identify a future-marked passive imperfect with the passive subject in word 3, preserving future certainty and deagentivized rescue.\",\"representative_source_ids\":[\"QG-41ea6f1a\",\"QG-6e50f577\",\"QY-a0040ded\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:sound-compression","source_type":"word_analysis","support_id":"sup_c00ffcc029e32d2588d0","text":"{\"blocking_evidence\":null,\"headline\":\"compact sound carries promise and object together\",\"reader_payoff\":\"The reader hears the promise, doubled removal, and attached Fire-reference compressed into one dense verbal unit.\",\"reason\":\"The surface form includes the future prefix, passive Form II shape, and final object suffix in one word.\",\"representative_source_ids\":[\"QP-2d184004\",\"QP-8034dac2\",\"MP-5cad02d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:withdrawal-to-rescue","source_type":"word_analysis","support_id":"sup_cb46d2f3706d80374a42","text":"{\"blocking_evidence\":null,\"headline\":\"active turning-away yields to passive rescue\",\"reader_payoff\":\"The reader feels the discourse reverse from human blame in 92:16 to promised protection in 92:17.\",\"reason\":\"The rows contrast 92:16 with 92:17, and the local verb's future passive form supports that reversal without changing the local parse.\",\"representative_source_ids\":[\"QI-d7ca5346\",\"QB-6a4339e5\",\"QB-9b80d1dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:opposite-superlatives","source_type":"word_analysis","support_id":"sup_d2d5f514a7b986094406","text":"{\"blocking_evidence\":null,\"headline\":\"opposite superlatives frame opposite Fire relations\",\"reader_payoff\":\"The reader sees the most wretched and the most guarded as matched extremes with reversed relations to the Fire.\",\"reason\":\"The word answers the same al-plus-elative pattern in 92:15 while the Fire pronoun relation reverses.\",\"representative_source_ids\":[\"QT-f1f368ec\",\"QE-3d2d72e2\",\"QY-0196085a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:1:whole-clause-scope","source_type":"word_analysis","support_id":"sup_d3b03af9ab9dc4330029","text":"{\"blocking_evidence\":null,\"headline\":\"particle links the whole promised outcome\",\"reader_payoff\":\"The reader sees the connective governing the relation between discourse units, not merely attaching mechanically to the following verb.\",\"reason\":\"The attachment evidence treats 92:17 as one passive verbal clause, so the connector relates the full rescue clause to the previous Fire scene.\",\"representative_source_ids\":[\"QG-9b33f53c\",\"QS-be1d0b72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:rare-elative-peak","source_type":"word_analysis","support_id":"sup_e3e9c4330b05395497e3","text":"{\"blocking_evidence\":null,\"headline\":\"rare elative marks the apex of a common field\",\"reader_payoff\":\"The reader notices that the ayah chooses a marked peak-form from a familiar ethical root family.\",\"reason\":\"The bundle identifies the word as an elative/superlative adjective and records low occurrence for the exact form profile.\",\"representative_source_ids\":[\"QS-033688d4\",\"MS-772a4f45\",\"QH-14229485\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:self-guarding-morphology","source_type":"word_analysis","support_id":"sup_ebb7c134047bcb4eea16","text":"{\"blocking_evidence\":null,\"headline\":\"reflexive guarding becomes superlative identity\",\"reader_payoff\":\"The reader sees the excellence as cultivated self-guarding intensified into identity.\",\"reason\":\"The surface elative belongs to the taqwā and self-guarding family, while the local syntax makes that peak quality the rescued subject.\",\"representative_source_ids\":[\"QS-6f385967\",\"QF-3de2a5ba\",\"MF-23a75f18\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:17:2:2","source_type":"qac_morpheme","support_id":"sup_f76aec05c7f78669de28","text":"{\"lemma_ar\":\"أَتْقَى\",\"morph_features\":\"STEM|POS:N|LEM:>atoqaY|ROOT:wqy|MS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:17:2:2\",\"qac_word_ref\":\"92:17:2\",\"root_ar\":\"و ق ي\",\"surface_ar\":\"أَتْقَى\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:2:delayed-subject-promise","source_type":"word_analysis","support_id":"sup_f82bf3431537625064b3","text":"{\"blocking_evidence\":null,\"headline\":\"verb arrives before the saved identity\",\"reader_payoff\":\"The reader encounters the promised removal before learning the final identity of the one rescued.\",\"reason\":\"Attachment evidence identifies word 3 as the passive subject following the verb, so the verb-first order creates real end-focus.\",\"representative_source_ids\":[\"QF-6b7352db\",\"QT-25f9a79e\",\"QB-def24034\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:act-to-identity","source_type":"word_analysis","support_id":"sup_f911670c2bbe30c4e028","text":"{\"blocking_evidence\":null,\"headline\":\"same root moves from act to identity\",\"reader_payoff\":\"The reader sees the earlier act of guarding in 92:5 become the named identity of the rescued person in 92:17.\",\"reason\":\"Both rows are same-surah references to the {{ar:و ق ي}} ({{tr:w-q-y}}) root, and the local form in 92:17 is the definite elative identity.\",\"representative_source_ids\":[\"QI-83149bd7\",\"QE-557522b8\",\"ME-e97bba07\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:17:3:passive-subject","source_type":"word_analysis","support_id":"sup_ff7050ddff1c81e153c4","text":"{\"blocking_evidence\":null,\"headline\":\"elative becomes the rescued passive subject\",\"reader_payoff\":\"The reader notices that a superlative quality is personalized as the one acted upon in rescue.\",\"reason\":\"QAC identifies a definite elative adjective, and attachment evidence marks it as the nominative passive subject of {{ar:سَيُجَنَّبُهَا}} ({{tr:sayujannabuhā}}).\",\"representative_source_ids\":[\"QG-11abc618\",\"QG-5f962f94\",\"QY-de0306e7\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","ayah_ref":"92:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B003","root_001677/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000262","role":"Removal to a side supplies the passive spatial operation performed on the subject.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_001677","role":"Placing oneself under protective caution supplies the subject's prior disposition.","root":"و ق ي","source_ref":"92:17","source_word_indices":["2"]}],"changed_reading":{"after":"The most self-guarding person is made to occupy a removed position; granted deliverance completes a practiced placing of the self under protection.","before":"A pious person will simply be spared."},"confidence":"strong","focus_anchor":"The future passive verb at word 1 places a subject aside, while the superlative at word 2 names maximal self-protective caution.","mechanism":"An inwardly acquired habit of guarding is paired with an outward causative relocation. The subject does not merely avoid danger by personal effort; another agency completes that effort by putting the subject in a removed position.","model_id":"b01_passive_completion_of_self_guarding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_passive_completion_of_self_guarding","source_type":"hft","support_id":"sup_c9904beb5653fc047bc7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","ayah_ref":"92:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B001","root_000262/B011","root_001677/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000262","role":"The bodily flank and spatial edge supply a lateral safe-side geometry.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]},{"branch_id":"B011","mapped_root_id":"root_000262","role":"A cover or shield stationed at the side turns that geometry into active screening.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001677","role":"A guard interposed against harm supplies the barrier function of the screened flank.","root":"و ق ي","source_ref":"92:17","source_word_indices":["2"]}],"changed_reading":{"after":"The protected subject is assigned to a safe flank and screened at the boundary, so lateral placement and interposition coexist with distance.","before":"Being kept away means only increasing the distance from danger."},"confidence":"medium","focus_anchor":"The side-root at word 1 can organize a flank, edge, or precinct and can also image a shield held at the side; word 2 supplies the protective-barrier logic.","mechanism":"Side, shield, and barrier branches create layered geometry. Safety is not only more distance from an unnamed object but assignment to a screened flank where the boundary itself bears the exposure.","model_id":"b02_safe_flank_and_side_shield"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_safe_flank_and_side_shield","source_type":"hft","support_id":"sup_f71a62865a6b271f833c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَسَيُجَنَّبُهَا ٱلْأَتْقَى","ayah_ref":"92:17"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000262/B005","root_001677/B003"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000262","role":"Leading or keeping a being alongside supplies an escort rather than a bare expulsion.","root":"ج ن ب","source_ref":"92:17","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001677","role":"A guarded gait around painful ground supplies cautious movement within that escort.","root":"و ق ي","source_ref":"92:17","source_word_indices":["2"]}],"changed_reading":{"after":"Safety may be a conducted passage along the field's edge, with proximity controlled by an escort and a guarded gait.","before":"Safety requires complete absence from the threatening field."},"confidence":"exploratory","focus_anchor":"The passive verb at word 1 also touches a branch of leading something alongside, while word 2 has a branch of wary, pain-avoiding movement.","mechanism":"The two branches permit controlled proximity: a guarded subject can be conducted along the edge of danger rather than abandoned or exposed to it. Safety then lies in guided adjacency and calibrated movement.","model_id":"b03_guarded_escort_at_the_edge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_guarded_escort_at_the_edge","source_type":"hft","support_id":"sup_69f8a590a5c636481a8c","trust":"legacy_unbound"}]}
</lane_packet_json>
