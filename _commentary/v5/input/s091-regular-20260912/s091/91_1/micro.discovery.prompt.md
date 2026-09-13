# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **91:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s091-regular-20260912/s091/91_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "91:1",
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
{"branch_registry":[{"boundary":"Dal, gök cismini ve onun ışığını merkez alır; güneşli gün, güneşte yapılma ve güneşe çıkma anlamları yalnızca tanıklanan kuruluşlara bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000818/B001","candidate_links":[{"candidate_id":"cand_b35a297c8d16025c277f","lane":"micro"},{"candidate_id":"cand_c897026b9663d7760757","lane":"micro"},{"candidate_id":"cand_50df550fde99174493a2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"güneş, güneş diski ve ışığı; güneşli olma ve güneşe çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş, gökteki bilinen cisim, onun görünen yuvarlak yüzü ve çevreye yayılan ışığıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneşli gün kuruluşu, gündüzünün bütünü güneşli olan günü ve günün güneşinin güçlenmesini bildirir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türetilmiş biçimler, bir şeyin güneşte yapılmasını ya da kişinin güneşe çıkıp ona yönelmesini bildirir."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, yalın gök cismi çekirdeğiyle tanıklanan güneşli olma ve güneşe yönelme kullanımlarının tümünü birlikte özetler.","boundary_detail":"Dal, gök cismini ve onun ışığını merkez alır; güneşli gün, güneşte yapılma ve güneşe çıkma anlamları yalnızca tanıklanan kuruluşlara bağlıdır.","branch_image_ar":"الشمس والضح","concept_gloss":"güneş, güneş diski ve ışığı; güneşli olma ve güneşe çıkma","contextual_glosses":[{"applicability":"Gök cisminin, görünen yuvarlak yüzünün veya bağlama göre ondan yayılan ışığın kastedildiği kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Günün güneşli olması, güneşte yapılma ve kişinin güneşe çıkması gibi bağlı kullanımları tek başına göstermez.","preserves":"Dalın gök cismi ve bağlama bağlı disk ya da ışık çekirdeğini korur."},"facet_ids":["F001"],"text":"güneş","usage_role":"general"},{"applicability":"Günün bütün gündüz boyunca güneşli olduğu ya da güneşinin güçlendiği kuruluşlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gök cisminin kendisini ve güneşte yapılan şey ya da güneşe çıkan kişi kullanımlarını kapsamaz.","preserves":"Günün güneş taşıması ve güneşinin güçlenmesi anlamını korur."},"facet_ids":["F002"],"text":"güneşli gün; gün güneşlendi","usage_role":"contextual"},{"applicability":"Bir şeyin güneş altında yapılmasını veya kişinin güneş ışığına çıkıp yönelmesini anlatan türetilmiş biçimlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin kendisini ve günün güneşli oluşunu kapsamaz.","preserves":"Güneşte yapılma ve güneşe çıkıp yönelme anlamlarını korur."},"facet_ids":["F003"],"text":"güneşte yapılmış; güneşe çıkmak","usage_role":"contextual"}],"definition":"Gökte görülen güneş, onun yuvarlak yüzü ve ondan yayılan ışık bu dalın çekirdeğidir. Belirli kuruluşlarda bir günün bütünüyle güneşli olması, bir şeyin güneşte yapılması ve kişinin güneşe çıkıp ona yönelmesi de anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş, gökteki bilinen cisim, onun görünen yuvarlak yüzü ve çevreye yayılan ışığıdır."},{"facet_id":"F002","role":"specialization","statement":"Güneşli gün kuruluşu, gündüzünün bütünü güneşli olan günü ve günün güneşinin güçlenmesini bildirir."},{"facet_id":"F003","role":"associated_use","statement":"Türetilmiş biçimler, bir şeyin güneşte yapılmasını ya da kişinin güneşe çıkıp ona yönelmesini bildirir."}],"identity_rationale":"Kaynak ifadesi gökteki güneşi, onun görünen yuvarlak yüzünü ve yayılan ışığını aynı çekirdekte toplar; ayrıca günün güneşli oluşunu, bir şeyin güneşte yapılmasını ve kişinin güneşe çıkmasını belirli biçim ve kuruluşlarla bildirir. Verilen dal çerçevesi bu ayrımları doğru biçimde kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güneş; güneşin görünen diski ve yayılan ışığı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gündüzünün tamamı güneşli olan gün"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"günümüz güneşli oldu; güneşi güçlendi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güneşte yapılmış ya da güneşe tutulmuş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güneşe çıkıp ona yönelmek"}],"lexicalization_note":"Tanım, yalın güneş anlamını merkezde tutar; günün güneşli olması, güneşte yapılma ve güneşe yönelme anlamlarını ise tanıklanan biçim ve söz öbekleriyle sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güneş diski, gündüz ve güneş alan yerle olan üç karşıtlık dalın sınırını en açık biçimde gösterdi, öteki adaylar ya yalnızca aynı sahneyi paylaşıyor ya da başka kök içi anlamlara ayrılıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yalnızca güneşin cismi ya da yuvarlak yüzüdür; odak dal bunun yanında yayılan ışığı ve çeşitli bağlı güneşli olma kullanımlarını içerir.","focus_only":"Odak dal, güneşin ışığını ve güneşli gün, güneşte yapılma, güneşe çıkma gibi bağlı kullanımları da kapsar.","gloss":"güneşin görünen yuvarlak gövdesi","neighbor_only":null,"neighbor_ref":"root_001069/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da güneşin görünen cisimsel yüzünü doğrudan adlandırır."},{"boundary_match":"partial","distinction":"Odak dal ışığın kaynağı olan güneşi adlandırırken komşu dal aydınlık zaman dilimini adlandırır; biri diğerinin yerine genel olarak kullanılamaz.","focus_only":"Odak dalın çekirdeği güneşin kendisi, diski ve ışığıdır.","gloss":"gündüz ve gün ışığı","neighbor_only":"Komşu dal, tan ile gün batımı arasındaki zaman dilimini ve gecenin karşıtını bildirir.","neighbor_ref":"root_001559/B002","relation_type":"near_neighbor","shared_zone":"Güneş ışığı ile gündüzün aydınlığı aynı doğal zaman ve aydınlanma alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalda güneşe çıkma bağlı bir eylem anlamıdır; komşu dalın çekirdeği ise güneş alan yer ve o yerde oturmadır.","focus_only":"Odak dal güneş cismini, ışığını ve kişinin güneşe yönelme eylemini içerir.","gloss":"güneş alan yer ve orada oturma","neighbor_only":"Komşu dal güneş alan oturma yerini ve o yerde oturmayı adlandırır.","neighbor_ref":"root_000790/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin güneş ışığına açık bir konumda bulunması söz konusudur."}],"source_phrase_ar":"الشمس معروفة (maqayis)؛ الشمس عين الضح (ayn;tahdhib)؛ الشمس يقال للقرصة وللضوء المنتشر عنها (mufradat)؛ يوم شامس وقد شمس يشمس شموسا (ayn;tahdhib)؛ شيء مشمس وتشمس (sihah)","source_summary":"Kaynaklar güneşi hem gökteki cisim ve görünen yuvarlak yüz hem de ondan yayılan ışık olarak verir. Aynı kanıt kümesi, güneşli günü ve güneşte yapılma ya da güneşe çıkma bildiren bağlı kullanımları da içerir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الشمس وقرصها وضوؤها والنهار ذو الشمس والتعرض للشمس والعمل فيها","what_is_not_ar":"ليس الشماس النصراني ولا القلائد ولا الشموس من الدواب والطباع"},"support_links":["sup_6f33c65304294242491d","sup_7c1fd4c677030fea206e","sup_d1be31215508bd62eb34"]},{"boundary":"Dalın çekirdeği ürküp kaçınma ve durulmama halidir; atın sırtını kullandırmaması ile insanın huysuzluğu bunun katılımcıya göre özelleşmeleridir.","branch_kind":"bare","branch_ref":"root_000818/B002","candidate_links":[{"candidate_id":"cand_21dc8ec378d97588871e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"ürküp kaçınma, durulmama ve güçlük çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı, ürküp kaçar, bir yerde ya da tutumda durulmaz ve kolayca denetim altına girmez."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At ya da başka bir binek hayvanı dürtülünce yerinde durmaz ve sırtını biniciye kullandırmaz."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsan için zor, huysuz ve bir tutumda kalmayan mizaç; kadın için kuşkulu durumdan ürküp uzak durma anlatılır."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, hayvan ve insandaki ortak çekirdeği; ayrıca binek hayvanının sırtını kullandırmaması ile zor mizacı birlikte kapsar.","boundary_detail":"Dalın çekirdeği ürküp kaçınma ve durulmama halidir; atın sırtını kullandırmaması ile insanın huysuzluğu bunun katılımcıya göre özelleşmeleridir.","branch_image_ar":"الشماس والشموس في الدابة والخلق","concept_gloss":"ürküp kaçınma, durulmama ve güçlük çıkarma","contextual_glosses":[{"applicability":"Yerinde durmayan veya dürtülünce sırtını kullandırmayan at ve başka binek hayvanları için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsandaki zor mizaç ile kuşkulu durumdan kaçınma kullanımlarını kapsamaz.","preserves":"Hayvandaki ürkme, durulmama ve sırtını kullandırmama özelliklerini korur."},"facet_ids":["F001","F002"],"text":"huysuz, ürkek ve sırtına bindirmeyen hayvan","usage_role":"contextual"},{"applicability":"Bir tutumda durmayan, zor yaradılışlı insanı niteleyen kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın ürkmesi ve sırtını kullandırmaması ile kuşkulu durumdan kaçınma özelleşmesini kapsamaz.","preserves":"İnsandaki zor mizaç ve tutum kararsızlığını korur."},"facet_ids":["F003"],"text":"huysuz, geçimsiz ve tutumu değişken kişi","usage_role":"contextual"},{"applicability":"Kadının kuşku uyandıran bir durumdan kaçınmasını bildiren özel insan kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel huysuzluk ve hayvanın denetim güçlüğü anlamlarını kapsamaz.","preserves":"Kuşkulu durum karşısındaki ürkme ve uzaklaşmayı korur."},"facet_ids":["F003"],"text":"kuşkulu durumdan ürküp uzak duran kadın","usage_role":"explanatory"}],"definition":"Hayvanın ya da insanın ürküp kaçınması ve bir yerde veya tutumda durulmaması bu dalın çekirdeğidir. Hayvanda dürtülünce sırtını kullandırmama, insanda zor ve değişken mizaç, kadında ise kuşkulu durumdan uzak durma biçimlerinde gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı, ürküp kaçar, bir yerde ya da tutumda durulmaz ve kolayca denetim altına girmez."},{"facet_id":"F002","role":"specialization","statement":"At ya da başka bir binek hayvanı dürtülünce yerinde durmaz ve sırtını biniciye kullandırmaz."},{"facet_id":"F003","role":"extension","statement":"İnsan için zor, huysuz ve bir tutumda kalmayan mizaç; kadın için kuşkulu durumdan ürküp uzak durma anlatılır."}],"identity_rationale":"Kaynak ifadesi hayvanda yerinde durmama ve sırtını kullandırmama, insanda kaçıp durulmama ve zor mizaç, kadında ise kuşkulu durumdan ürküp uzaklaşma özelliklerini aynı kaçınma ve kararsızlık alanında verir. Sunulan dal çerçevesi bu katmanları korur.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yerinde durmayan, dürtülünce sırtını kullandırmayan hayvan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"huysuz, geçimsiz ve tutumu değişken adam"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kuşkulu bir durumdan ürküp uzak duran kadın"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kaçıp yerinde durmadı"}],"lexicalization_note":"Yalın dal, hayvan ve insan için kaçınma, yerinde ya da tutumunda durmama ve güçlük çıkarma çekirdeğiyle tanımlanır; başka dallardaki kalıplaşmış anlamlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yerinde durmama, genel ürkme ve yönetilme güçlüğü taşıyan dört komşu en açıklayıcı karşıtlıkları verdi, yalnızca aynı olay çevresinde bulunan diğer adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı denetim güçlüğü ve zor mizaca uzanır; komşu dal ise daha genel kaçınma ile bunu başkasında doğuran eylemi de kapsar.","focus_only":"Odak dal, binek hayvanının sırtını kullandırmamasını ve insandaki zor, değişken mizacı içerir.","gloss":"ürkme ve az durulma","neighbor_only":"Komşu dal, kötü davranıştan ya da erkeklerden sakınan iffetli kadını ve bir başkasını ürkütüp kaçırtmayı da içerir.","neighbor_ref":"root_001564/B006","relation_type":"near_synonym","shared_zone":"İki dal da hayvan veya insanın ürküp uzaklaşmasını ve bulunduğu durumda kalmamasını anlatır."},{"boundary_match":"partial","distinction":"Komşu dal katılımcıyı ve doğuştanlık koşulunu daraltır; odak dal farklı hayvanları ve insan davranışını kapsayan daha geniş bir kaçınma alanıdır.","focus_only":"Odak dal insan mizacına ve binek hayvanının sırtını kullandırmamasına kadar uzanır.","gloss":"yerinde durmayan deve","neighbor_only":"Komşu dal yalnız deve için, geçici ağrıdan değil yaradılıştan gelen yerinde durmama koşulunu belirtir.","neighbor_ref":"root_000023/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da hayvanın tek bir yerde durmaması çekirdeği bulunur."},{"boundary_match":"partial","distinction":"Odak dal için vahşilik şart değildir; komşu dal ise durulmama ya da sırtını kullandırmama yerine insanlardan uzak duran yabani hali öne çıkarır.","focus_only":"Odak dal yerinde durmama, sırtını kullandırmama ve zor insan mizacını içerir.","gloss":"vahşileşme ve insanlardan ürkme","neighbor_only":"Komşu dalın çekirdeği insanlara alışmamış vahşi olma ve insanlardan kaçmadır.","neighbor_ref":"root_000004/B002","relation_type":"near_neighbor","shared_zone":"Hayvanın ürkmesi ve denetimden uzaklaşması iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği ürkme ve durulmama iken komşu dalın çekirdeği eğrilik ve iş görmekte güçlük çıkarmadır.","focus_only":"Odak dal canlıdaki kaçınma, kararsızlık ve zor mizacı bildirir.","gloss":"eğrilik ve güç yönetilme","neighbor_only":"Komşu dal cansız bir nesnenin eğriliğini ve ancak vurulunca koşan atı da kapsar.","neighbor_ref":"root_000911/B002","relation_type":"near_neighbor","shared_zone":"İki dal, özellikle atın kolay yönetilememesi bakımından kesişir."}],"source_phrase_ar":"الشموس من الدواب الذي لا يكاد يستقر (maqayis)؛ الشمس والشموس من الدواب الذي إذا نخس لم يستقر (ayn;tahdhib)؛ شمس الفرس شموسا وشماسا أي منع ظهره (sihah)؛ رجل شموس عسر (ayn;tahdhib)؛ رجل شموس صعب الخلق (sihah)؛ امرأة شموس إذا كانت تنفر من الريبة (maqayis)؛ شمس فلان شماسا إذا ند ولم يستقر (mufradat)","source_summary":"Kaynaklar hayvanın yerinde durmamasını ve özellikle atın sırtını kullandırmamasını, insandaki zor ve değişken mizacı ve kuşkulu durumdan kaçınmayı aynı anlam alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"نفور الدابة وعدم استقرارها ومنع ظهرها وصعوبة الخلق والعسر في الإنسان","what_is_not_ar":"ليس جرم الشمس ولا ضوءها ولا إظهار العداوة بعبارة شمس لي فلان"},"support_links":["sup_067a3ce17719d86f29bc"]},{"boundary":"Anlam yalnız tanıklanan kişiye yönelme kuruluşuna bağlıdır; genel huysuzluk, kavga veya her türlü düşmanlık anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000818/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"birine düşmanlığını açıkça göstermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, belirli kuruluş içinde karşısındakine düşmanlığını açıkça gösterir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarım, açık düşmanlığın eyleme geçme niyeti sezdirir gibi olabileceğini belirtir."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık yalnız tanıklanan kişiye yönelme kuruluşunun çekirdek anlamını verir; bağımsız ve genel bir kök anlamı olarak kullanılmaz.","boundary_detail":"Anlam yalnız tanıklanan kişiye yönelme kuruluşuna bağlıdır; genel huysuzluk, kavga veya her türlü düşmanlık anlamına genişletilmez.","branch_image_ar":"إبداء العداوة","concept_gloss":"birine düşmanlığını açıkça göstermek","contextual_glosses":[{"applicability":"Kişinin düşmanlığını doğrudan karşısındakine belli ettiği anlatı bağlamlarında doğal bir çeviridir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşmanlığın belirli bir kişiye yönelmesini ve açıkça gösterilmesini korur."},"facet_ids":["F001"],"text":"ona açıkça düşmanca davrandı","usage_role":"contextual"},{"applicability":"Düşmanlık gösterisinin eyleme geçme niyeti sezdirir gibi sunulduğu özel aktarım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Niyet izlenimi taşımayan daha genel tanıklanmış kullanımları kapsamaz.","preserves":"Açık düşmanlık gösterisini ve eylem niyeti izlenimini korur."},"facet_ids":["F001","F002"],"text":"düşmanca çıkışıp harekete geçecekmiş gibi oldu","usage_role":"explanatory"}],"definition":"Tanıklanan kişiye yönelme kuruluşunda, bir kimse karşısındakine düşmanlığını açıkça gösterir ve sertçe davranır. Bu gösteri bazen eyleme geçmeyi tasarladığı izlenimini de taşır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, belirli kuruluş içinde karşısındakine düşmanlığını açıkça gösterir."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarım, açık düşmanlığın eyleme geçme niyeti sezdirir gibi olabileceğini belirtir."}],"identity_rationale":"Kaynak ifadesi belirli bir kişiye yönelen kalıp içinde düşmanlığın açıkça gösterilmesini bildirir; bir aktarımda bunun eyleme geçme niyeti sezdirir gibi oluşu da eklenir. Dalın düşmanlığı açığa vurma çerçevesi bu çekirdeğe uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bana düşmanlığını açıkça gösterdi ve sert davrandı"}],"lexicalization_note":"Tanım yalnızca tanıklanan kişiye yönelme kalıbındaki açık düşmanlık gösterisine uygulanır; buradan yalın kök için genel bir düşmanlık anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; açık düşmanlık, savaşma, tartışma ve yüzüne karşı sertlik dalları okuyucunun karıştırabileceği en yakın sınırları verdi, yalnız öfke veya dolaylı ilişki taşıyan adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal çekirdek çok yakındır; odak dalın sözdizimsel sınırı ve olası eylem niyeti tonu, komşu dalın daha genel açık ilan kapsamından ayrılır.","focus_only":"Odak dal belirli bir kişiye yönelen tanıklanmış kuruluşla ve kimi aktarımda eylem niyeti izlenimiyle sınırlıdır.","gloss":"düşmanlığı açıkça ilan etme","neighbor_only":"Komşu dal düşmanlığı genel olarak açıkça ilan etmeyi, belirli bir kuruluş şartı olmadan bildirir.","neighbor_ref":"root_000097/B004","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeği gizli düşmanlık değil, düşmanlığın karşı tarafa açıkça gösterilmesidir."},{"boundary_match":"partial","distinction":"Odak dal düşmanlığın görünür kılınmasına, komşu dal ise bunun fiili savaş veya çatışmaya dönüşmesine odaklanır.","focus_only":"Odak dalda düşmanlığı göstermek yeterlidir; fiili çatışma zorunlu değildir.","gloss":"düşmanlık ve savaşma","neighbor_only":"Komşu dal savaşma ve çatışmayı düşmanlıkla birlikte çekirdeğe alır.","neighbor_ref":"root_001550/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler ya da taraflar arasındaki açık düşmanlık alanındadır."},{"boundary_match":"field_only","distinction":"Tartışma düşmanlık göstermeden de gerçekleşebilir; odak dalda ise karşı tarafa düşmanlığı belli etmek kurucu öğedir.","focus_only":"Odak dal, belirli kişiye düşmanlığı açıkça göstermeyi gerektirir.","gloss":"çekişme ve tartışma","neighbor_only":"Komşu dal, kalıcı düşmanlık şartı olmadan karşılıklı çekişme ve tartışmayı bildirir.","neighbor_ref":"root_000787/B011","relation_type":"same_field","shared_zone":"Açık sertlik ve kişiler arası gerilim iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal için kaba söz ya da fiziksel vuruş gerekmez; komşu dalın yüz yüze sertlik çekirdeği ise düşmanlık niyetini zorunlu kılmaz.","focus_only":"Odak dal düşmanlık tutumunun açıkça gösterilmesini bildirir.","gloss":"yüzüne sert söz söyleme","neighbor_only":"Komşu dal kaba sözle yüzüne karşı çıkmayı veya doğrudan alna vurmayı da kapsar.","neighbor_ref":"root_000219/B002","relation_type":"near_neighbor","shared_zone":"Karşıdaki kişiye yöneltilen açık ve sert davranış iki dalı yakınlaştırır."}],"source_phrase_ar":"شمس لي فلان إذا أبدى لك عداوته (maqayis;sihah)؛ شمس لي فلان إذا أبدى لك عدواته (ayn)؛ شمس لي فلان إذا أبدى لك عداوته كأنه قد هم أن يفعل (tahdhib)","source_summary":"Kaynaklar kalıplaşmış kuruluşun karşısındaki kişiye düşmanlığı açıkça göstermeyi bildirdiğinde birleşir; kanıt ayrıca bu tavrın eyleme geçme niyeti sezdiren bir görünüm kazanabileceğini belirtir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"إظهار العداوة والمخاشنة في قولهم شمس لي فلان","what_is_not_ar":"ليس مجرد صعوبة الخلق ولا شموس الدابة ولا معنى الشمس والضح"},"support_links":[]},{"boundary":"Dal yalnız boyun takısındaki sarkıt parçaları ya da özel bir kolye türünü bildirir; genel takı, güneş veya hayvan niteliği anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000818/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"kolye sarkıtları ya da bir kolye türü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boyun kolyesine asılan süs parçalarını bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kaynak çözümünde, sarkıt parçalar yerine belirli bir kolye türünü bildirir."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki parça ve bütün yorumlarını birbirine indirgemeden aynı takı dalında birlikte verir.","boundary_detail":"Dal yalnız boyun takısındaki sarkıt parçaları ya da özel bir kolye türünü bildirir; genel takı, güneş veya hayvan niteliği anlamına gelmez.","branch_image_ar":"شموس القلائد","concept_gloss":"kolye sarkıtları ya da bir kolye türü","contextual_glosses":[{"applicability":"Sözcüğün kolyeye asılan ayrı süs parçaları olarak yorumlandığı aktarımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözcüğün bütün bir kolye türünü bildirdiği öteki kaynak çözümünü dışarıda bırakır.","preserves":"Kolyeye asılan parçalar yorumunu açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"kolye sarkıtları","usage_role":"contextual"},{"applicability":"Sözcüğün belirli bir bütün kolye türü olarak yorumlandığı aktarım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kolyeye asılan ayrı sarkıt parçaları yorumunu kapsamaz.","preserves":"Bütün kolye türü yorumunu korur."},"facet_ids":["F002"],"text":"bir kolye türü","usage_role":"contextual"}],"definition":"Boyun kolyelerine asılan süs parçaları ya da belirli bir kolye türüdür. Kaynak kanıtı, sarkıt parça ile bütün kolye yorumlarını tek bir biçim altında yan yana verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boyun kolyesine asılan süs parçalarını bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir kaynak çözümünde, sarkıt parçalar yerine belirli bir kolye türünü bildirir."}],"identity_rationale":"Kaynak ifadesi sözcüğü bir aktarımda kolyelere asılan parçalar, başka bir aktarımda ise bir kolye türü olarak açıklar. Verilen dal, bu iki yakın fakat aynı olmayan takı çözümünü birlikte ve doğru sınırda tutar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kolyeye asılan süsler ya da bir kolye türü"}],"lexicalization_note":"Yalın dal, kolye sarkıtları ile bir kolye türü arasındaki kaynak ayrımını korur; belirli bir söz öbeğine ya da genel süs eşyası anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kolye süsü, genel kolye ve boncuk ya da kabuk süsü karşıtlıkları parça, bütün, işlev ve malzeme sınırlarını yeterince gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tek bir özel süs türüyle sınırlıdır; odak dalın kanıtı ise sarkıtların çoğul kümesini ve alternatif olarak bütün kolye türünü kapsar.","focus_only":"Odak dal, birden çok sarkıtı veya bütün bir kolye türünü de adlandırabilir.","gloss":"kolyeye takılan süs parçası","neighbor_only":"Komşu dal yalnızca kolyeye yerleştirilen belirli bir süs parçasını adlandırır.","neighbor_ref":"root_000291/B008","relation_type":"near_synonym","shared_zone":"Her iki dal kolyenin üzerinde taşınan süs parçalarını adlandırır."},{"boundary_match":"partial","distinction":"Odak dal belirli sarkıtlar ya da kolye türüyle sınırlıyken komşu dal işaretleme işlevine ve farklı taşıyıcılara uzanan genel kolye alanıdır.","focus_only":"Odak dal kolyenin sarkıt parçalarını veya özel bir kolye türünü bildirir.","gloss":"boyunda taşınan işaret veya süs kolyesi","neighbor_only":"Komşu dal insanın, kurbanlık hayvanın ya da köpeğin boynundaki işaret veya süs kolyesini ve işaretleme eylemini kapsar.","neighbor_ref":"root_001249/B002","relation_type":"near_neighbor","shared_zone":"Boyunda taşınan kolye ve onun süs işlevi iki dalın ortak alanıdır."},{"boundary_match":"field_only","distinction":"Odak dal boyun kolyesindeki görev ve türle belirlenir; komşu dal ise malzemeyi ve çeşitli eşyaların süslenmesini öne çıkarır.","focus_only":"Odak dal kolye sarkıtlarını ya da kolyenin bir türünü bildirir.","gloss":"kabuk ve delinmiş boncuk süsleri","neighbor_only":"Komşu dal deniz kabuklarını, delinmiş boncukları ve bunlarla başka eşyaların süslenmesini kapsar.","neighbor_ref":"root_000743/B006","relation_type":"same_field","shared_zone":"İki dalda da delinip asılabilen küçük süs parçaları bulunabilir."}],"source_phrase_ar":"الشموس معاليق القلائد (ayn;tahdhib)؛ الشمس ضرب من القلائد (sihah)","source_summary":"Kanıt, aynı takı adını bazı aktarımlarda kolyeye asılan parçalar, başka bir aktarımda ise kolyenin belirli bir türü olarak çözümler. Ortak alan boyunda taşınan süs eşyasıdır, fakat parça ile bütün ayrımı korunmalıdır.","sources":["AY","SI","TA"],"what_is_ar":"الشموس وهي معاليق القلائد أو ضرب منها","what_is_not_ar":"ليس الشمس السماوية ولا الشموس من الدواب ولا الشماس النصراني"},"support_links":[]},{"boundary":"Dal bir Hristiyan din görevlisini makamı, baş tıraşı ve kiliseye sürekli bağlılığıyla tanımlar; genel rahip, keşiş, piskopos veya ibadet yeri adı değildir.","branch_kind":"bare","branch_ref":"root_000818/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"başı ortadan tıraşlı, kiliseye bağlı Hristiyan önder din görevlisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hristiyan topluluğu içinde önderlik konumu bulunan bir din görevlisidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başının ortasını tıraş etmesi ve kiliseye sürekli bağlı kalması bu görevlinin ayırt edici özellikleridir."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu açıklayıcı karşılık makamı, ayırt edici baş tıraşını ve kiliseye sürekli bağlılığı birlikte taşır.","boundary_detail":"Dal bir Hristiyan din görevlisini makamı, baş tıraşı ve kiliseye sürekli bağlılığıyla tanımlar; genel rahip, keşiş, piskopos veya ibadet yeri adı değildir.","branch_image_ar":"الشماس النصراني","concept_gloss":"başı ortadan tıraşlı, kiliseye bağlı Hristiyan önder din görevlisi","contextual_glosses":[{"applicability":"Makamın ayrıntılarının bağlamdan anlaşıldığı akıcı metinlerde genel karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":"Başka Hristiyan din görevlileriyle karışabilir.","fit":"narrowing","loses":"Önderlik derecesini, başın ortasını tıraş etmesini ve kiliseye sürekli bağlılığını açıkça göstermez.","preserves":"Kişinin Hristiyan dinî kurumundaki görevli kimliğini korur."},"facet_ids":["F001"],"text":"Hristiyan din görevlisi","usage_role":"general"},{"applicability":"Kurumsal bağlılık ve topluluk içindeki konumun öne çıktığı açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":"Makam adı verilmediğinde başka önder kilise görevlileriyle karışabilir.","fit":"narrowing","loses":"Başın ortasını tıraş etme özelliğini belirtmez.","preserves":"Önderlik konumunu ve kiliseye sürekli bağlı kalma özelliğini korur."},"facet_ids":["F001","F002"],"text":"kiliseye sürekli bağlı önder görevli","usage_role":"explanatory"}],"definition":"Hristiyan topluluğunun önderlerinden sayılan, başının ortasını tıraş eden ve kiliseye sürekli bağlı kalan din görevlisidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hristiyan topluluğu içinde önderlik konumu bulunan bir din görevlisidir."},{"facet_id":"F002","role":"specialization","statement":"Başının ortasını tıraş etmesi ve kiliseye sürekli bağlı kalması bu görevlinin ayırt edici özellikleridir."}],"identity_rationale":"Kaynak ifadesi bu kişiyi Hristiyan topluluğunun önderlerinden biri, başının ortasını tıraş eden ve kiliseye sürekli bağlı kalan görevli olarak tanımlar; çoğul biçimi de verir. Dal çerçevesi makam, görünüş ve kurumsal bağlılık öğelerini doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"başının ortasını tıraş eden ve kiliseye sürekli bağlı kalan Hristiyan önder din görevlisi"}],"lexicalization_note":"Yalın dal doğrudan bu tarihsel Hristiyan din görevlisini bildirir; kilise binası, ibadet ya da başka dinî makam anlamları tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; rahip, keşiş, piskopos ve kilise karşılaştırmaları kişi, makam ve mekân sınırlarını açıklar, ibadet ve başka ibadet yeri adayları ise daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli görünüş ve kurumsal bağlılık özellikleriyle sınırlandırılmıştır; komşu dalın ayırıcı yönü din bilgisi ve ibadettir.","focus_only":"Odak dal başın ortasını tıraş etme ve kiliseye sürekli bağlı kalma özelliklerini birlikte gerektirir.","gloss":"Hristiyan rahip ve bilgin","neighbor_only":"Komşu dal bilgili ve ibadete düşkün din adamı niteliğini öne çıkarır.","neighbor_ref":"root_001223/B003","relation_type":"near_synonym","shared_zone":"Her iki dal Hristiyan topluluğunda dinî önderlik veya görev üstlenen kişiyi adlandırır."},{"boundary_match":"partial","distinction":"Komşu dal keşiş veya çancıya kadar uzanır; odak dal ise kaynakta birlikte verilen makam, tıraş ve sürekli kilise bağlılığıyla belirlenir.","focus_only":"Odak dal topluluk önderliği, başın ortasını tıraş etme ve kiliseye bağlı kalmayı içerir.","gloss":"Hristiyan keşiş, önder veya çancı","neighbor_only":"Komşu dal keşişliği ve çan çalma görevini de kapsar.","neighbor_ref":"root_000006/B006","relation_type":"near_synonym","shared_zone":"İki dal da Hristiyan dinî yaşamında görevli ya da önder kişileri kapsar."},{"boundary_match":"partial","distinction":"Komşu dal belirli bir üst makamı adlandırır; odak dalın görevlisi ise farklı ayırt edici uygulamalarla tanımlanır ve aynı makam olduğu gösterilmez.","focus_only":"Odak dalın görevliyi belirleyen baş tıraşı ve sürekli kilise bağlılığı özellikleri vardır.","gloss":"Hristiyan topluluğunun baş din görevlisi","neighbor_only":"Komşu dal, Hristiyan hiyerarşisindeki baş makamı özellikle piskopos olarak adlandırır.","neighbor_ref":"root_000720/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal Hristiyan dinî hiyerarşisinde önder konum taşıyan görevliyi anlatır."},{"boundary_match":"thematic_only","distinction":"Biri kişi ve makam, diğeri mekândır; aralarındaki bağ görevlinin o yapıda hizmet etmesinden doğar.","focus_only":"Odak dal bir din görevlisini adlandırır.","gloss":"Hristiyan kilisesi","neighbor_only":"Komşu dal Hristiyanların kilise binasını ya da ibadet evini adlandırır.","neighbor_ref":"root_000169/B004","relation_type":"thematic","shared_zone":"Görevlinin sürekli bağlı kaldığı kurum, komşu dalın adlandırdığı ibadet yeridir."}],"source_phrase_ar":"الشماس من رؤساء النصارى الذي يحلق وسط رأسه لازما للبيعة (ayn;tahdhib)؛ الجميع الشمامسة (ayn;tahdhib)","source_summary":"Kaynaklar makamı Hristiyan topluluğundaki önderlik, başın ortasını tıraş etme ve kiliseye sürekli bağlı kalma özellikleriyle birlikte tanımlar ve bunun çoğul bir görevli topluluğu oluşturduğunu belirtir.","sources":["AY","TA"],"what_is_ar":"الشماس من رؤساء النصارى الملازم للبيعة","what_is_not_ar":"ليس الشمس والضح ولا القلائد ولا الشماس بمعنى نفور الدابة"},"support_links":[]},{"boundary":"Koruma ve güçlü topluluk dayanışması bir insan niteliğidir; iyiliği esirgeme ve birilerine cimrilik etme ise ayrı fakat ilişkili kişi ve kuruluş kullanımlarıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000818/B006","candidate_links":[{"candidate_id":"cand_21dc8ec378d97588871e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"arkasındakini koruma, topluluğunu savunma ve iyiliğini esirgeme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Türemiş kişi biçimi, arkasında bulunanı başkasının erişiminden koruyan ve engelleyen adamı bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı kişi niteliği, kendi topluluğunu güçlü biçimde savunma ve ona sıkı bağlılık gösterme olarak açıklanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi, kendisinden hiçbir iyiliğe erişilemeyen cimri olarak da nitelenir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişiye yönelen belirli kuruluş, birilerine karşı cimrilik edip iyiliği esirgemeyi bildirir."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu açıklayıcı karşılık yalnız tanıklanan türemiş kişi biçimi ve kişiye yönelen cimrilik kuruluşunun birleşik kapsamını özetler.","boundary_detail":"Koruma ve güçlü topluluk dayanışması bir insan niteliğidir; iyiliği esirgeme ve birilerine cimrilik etme ise ayrı fakat ilişkili kişi ve kuruluş kullanımlarıdır.","branch_image_ar":"التشمس بالمنع والبخل","concept_gloss":"arkasındakini koruma, topluluğunu savunma ve iyiliğini esirgeme","contextual_glosses":[{"applicability":"Türemiş kişi biçiminin koruma, engelleme ve güçlü topluluk bağlılığı anlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Cimri kişi ve belirli birine karşı iyiliğini esirgeme kullanımlarını kapsamaz.","preserves":"Koruyup engelleyen ve topluluğunu güçlü biçimde savunan kişi özelliklerini korur."},"facet_ids":["F001","F002"],"text":"arkasındakini koruyan ve topluluğunu güçlü biçimde savunan adam","usage_role":"explanatory"},{"applicability":"Türemiş kişi biçiminin iyiliğini vermeyen cimriyi nitelediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koruyup engelleme, topluluk savunusu ve yöneltilmiş cimrilik eylemini kapsamaz.","preserves":"Kişinin cimriliğini ve ondan iyilik elde edilememesini korur."},"facet_ids":["F003"],"text":"iyiliğine erişilemeyen cimri","usage_role":"contextual"},{"applicability":"Tanıklanan kişiye yönelme kuruluşunda, bir grubun beklediği iyiliğin verilmemesini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koruyucu kişi, topluluk savunusu ve genel cimri kişi niteliklerini kapsamaz.","preserves":"Belirli kişilere karşı cimrilik etme ve iyiliği esirgeme eylemini korur."},"facet_ids":["F004"],"text":"bize cimrilik etti ve iyiliğini esirgedi","usage_role":"contextual"}],"definition":"Türemiş kişi biçimi, arkasında bulunanı başkasından koruyup engelleyen veya topluluğunu güçlü biçimde savunan adamı; ayrıca iyiliğine erişilemeyen cimriyi bildirir. Belirli bir kişiye yönelen kuruluşta ise iyiliğini esirgeyip ona cimrilik etmek anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Türemiş kişi biçimi, arkasında bulunanı başkasının erişiminden koruyan ve engelleyen adamı bildirir."},{"facet_id":"F002","role":"specialization","statement":"Aynı kişi niteliği, kendi topluluğunu güçlü biçimde savunma ve ona sıkı bağlılık gösterme olarak açıklanır."},{"facet_id":"F003","role":"extension","statement":"Kişi, kendisinden hiçbir iyiliğe erişilemeyen cimri olarak da nitelenir."},{"facet_id":"F004","role":"associated_use","statement":"Kişiye yönelen belirli kuruluş, birilerine karşı cimrilik edip iyiliği esirgemeyi bildirir."}],"identity_rationale":"Kaynak ifadesi aynı türemiş biçim çevresinde arkasındakini engelleyip koruyan adamı, topluluğunu güçlü biçimde savunan kişiyi ve iyiliğini vermeyen cimriyi; ayrıca yalnız belirli bir kuruluşta birilerine cimrilik etmeyi birlikte verir. Dal korunabilir, ancak savunma ve topluluk bağlılığı genel cimriliğe indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"arkasındakini koruyup engelleyen ya da topluluğunu güçlü biçimde savunan adam"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bize karşı cimrilik etti ve iyiliğini esirgedi"}],"lexicalization_note":"Tanım türemiş kişi niteliğini, cimri kişi kullanımını ve birilerine cimrilik etme kuruluşunu ayrı tutar; bunlardan yalın köke genel bir koruma ya da cimrilik anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel vermeme, genel cimrilik ve genel engelleme dalları, bu dalın koruma ile cimriliği yalnız tanıklanan biçimlerde birleştiren sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel vermeme alanıdır; odak dal ise belirli türemiş kişi biçimi ve kuruluşta koruma, topluluk savunusu ve cimriliği birlikte taşır.","focus_only":"Odak dal koruyup engelleme, topluluğu savunma ve kişiye yönelen özel cimrilik kuruluşlarını içerir.","gloss":"vermeme ve iyiliği engelleme","neighbor_only":"Komşu dal vermenin karşıtı olan genel engellemeyi ve iyiliği tutan kişiye ilişkin daha geniş biçimleri kapsar.","neighbor_ref":"root_001448/B001","relation_type":"near_synonym","shared_zone":"Bir başkasının beklediği iyiliği vermemek ve erişimi engellemek iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak dalın cimrilik yönü tanıklanan biçim ve kuruluşlara bağlıdır ve koruyucu bir yön de taşır; komşu dal genel cimrilik kavramıdır.","focus_only":"Odak dal arkasındakini koruma ve topluluğunu güçlü biçimde savunma anlamlarına da sahiptir.","gloss":"malı haksız yere esirgeyen cimrilik","neighbor_only":"Komşu dal eldeki malı verilmesi gereken kişiden haksız yere tutmayı genel bir cimrilik kavramı olarak tanımlar.","neighbor_ref":"root_000089/B001","relation_type":"near_synonym","shared_zone":"İyiliği ya da eldeki şeyi vermemek ve cimri kişi niteliği ortak alandır."},{"boundary_match":"partial","distinction":"Komşu dal yalın engellemedir; odak dalın kullanımları kişi niteliği, topluluk bağlılığı ve cimrilik koşullarıyla sınırlıdır.","focus_only":"Odak dal engellemeyi koruma, topluluk savunusu veya cimri iyilik esirgemesi olarak özelleştirir.","gloss":"genel engelleme","neighbor_only":"Komşu dal amaç ve katılımcı ayrımı olmadan genel engellemeyi bildirir.","neighbor_ref":"root_000076/B009","relation_type":"near_neighbor","shared_zone":"Bir şeyin başkasına geçmesini ya da erişilebilir olmasını önleme iki dalda kesişir."}],"source_phrase_ar":"المتشمس من الرجال الذي يمنع ما وراء ظهره (tahdhib)؛ وهو الشديد القومية (tahdhib)؛ البخيل أيضا متشمس (tahdhib)؛ تشمس علينا أي بخل (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Koruyan ya da topluluğunu güçlü biçimde savunan kişi ile iyiliğini esirgeyen cimri ve kişiye yönelen cimrilik kuruluşu tek bir kaynakta tanıklanır."}],"source_summary":"Kanıt, koruyup engelleme ile güçlü topluluk bağlılığını bir kişi niteliğinde; iyiliğine erişilemeyen cimriyi ve birilerine cimrilik etmeyi ise ilişkili fakat ayrı kullanımlarda toplar.","sources":["TA"],"what_is_ar":"المتشمس الذي يمنع ما وراء ظهره والشديد القومية والبخيل الذي لا ينال منه خير","what_is_not_ar":"ليس التعرض للشمس ولا شموس الدابة ولا إظهار العداوة"},"support_links":["sup_067a3ce17719d86f29bc"]},{"boundary":"Dal yalnız sözlüksel olarak yerleşmiş adları, mensubiyet biçimlerini ve topluluğa bağlanma türetmesini kapsar; güneşin genel anlamını ya da her serbest adlandırmayı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000818/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","surface_ar":"شَّمْسِ"}],"gloss":"güneş kökünden kişi, topluluk, put ve yer adları ile bağlılık türetmeleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş sözcüğü kişi ya da topluluk adı olarak kullanılır ve bir birleşik kişi adının öğesi olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı sözlüksel öğe eski bir putun ve tanınmış bir su kaynağının özel adı olur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi ya da topluluk adına bağlı mensubiyet ve antlaşma, koruma ilişkisi veya bağlılık yoluyla o topluluğa katılma biçimleri türetilir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sözlükselleşmiş yer adları arasında çıkışı zor bir tepenin ve Firdevs'in karşısındaki iki bahçenin adı bulunur."}}],"root_ar":"ش م س","root_id":"root_000818","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu açıklayıcı karşılık sözlükselleşmiş ad türlerini, mensubiyeti ve topluluğa bağlanma eylemini birlikte kapsar; genel güneş anlamına uygulanmaz.","boundary_detail":"Dal yalnız sözlüksel olarak yerleşmiş adları, mensubiyet biçimlerini ve topluluğa bağlanma türetmesini kapsar; güneşin genel anlamını ya da her serbest adlandırmayı kapsamaz.","branch_image_ar":"التسمية بالشمس وما نسب إليها","concept_gloss":"güneş kökünden kişi, topluluk, put ve yer adları ile bağlılık türetmeleri","contextual_glosses":[{"applicability":"Kişi, topluluk, put, su kaynağı, tepe ve bahçe adlarının topluca anıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mensubiyet biçimini ve bir topluluğa antlaşma, koruma ilişkisi ya da bağlılık yoluyla katılma eylemini açıkça göstermez.","preserves":"Güneş sözcüğünün sözlükselleşmiş özel adlarda kullanılmasını korur."},"facet_ids":["F001","F002","F004"],"text":"güneş sözcüğünden kurulmuş özel adlar","usage_role":"general"},{"applicability":"Türetilmiş eylemin kişinin belirli bir toplulukla toplumsal bağ kurmasını anlattığı bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dalın kişi, topluluk, put ve yer adlarını kapsamaz.","preserves":"Antlaşma, koruma ilişkisi veya bağlılık yoluyla topluluğa bağlanma anlamını korur."},"facet_ids":["F003"],"text":"bir topluluğa antlaşma, koruma ilişkisi veya bağlılıkla katılmak","usage_role":"explanatory"}],"definition":"Güneş sözcüğüyle kurulmuş kişi ve topluluk adları, eski bir putun, bir su kaynağının, bir tepenin ve iki bahçenin adları ile bunlara bağlı mensubiyet biçimleri bu dalda toplanır. Ayrıca belirli bir topluluğa antlaşma, koruma ilişkisi veya bağlılık yoluyla katılmayı bildiren türemiş bir eylem vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş sözcüğü kişi ya da topluluk adı olarak kullanılır ve bir birleşik kişi adının öğesi olur."},{"facet_id":"F002","role":"extension","statement":"Aynı sözlüksel öğe eski bir putun ve tanınmış bir su kaynağının özel adı olur."},{"facet_id":"F003","role":"associated_use","statement":"Kişi ya da topluluk adına bağlı mensubiyet ve antlaşma, koruma ilişkisi veya bağlılık yoluyla o topluluğa katılma biçimleri türetilir."},{"facet_id":"F004","role":"example","statement":"Sözlükselleşmiş yer adları arasında çıkışı zor bir tepenin ve Firdevs'in karşısındaki iki bahçenin adı bulunur."}],"identity_rationale":"Kaynak ifadesi güneş sözcüğüyle kurulan kişi ve topluluk adlarını, eski bir putu, bir su kaynağını, bir tepeyi ve iki bahçeyi; ayrıca bir topluluğa antlaşma, koruma ilişkisi ya da bağlılıkla katılmayı bildiren türetmeleri toplar. Verilen adlandırma çerçevesi kullanılabilir, ancak put adı ile toplumsal bağ kuran türetme de açıkça korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kul ve güneş öğelerinden kurulmuş birleşik bir Arap kişi adı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"güneş adı verilen eski bir put"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"güneş adı verilen tanınmış bir su kaynağı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"belirli bir topluluk içinde güneş sözcüğüne bağlanan kişi ya da soy adı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"güneş öğeli kişi ya da soy adına mensup olan"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güneş öğeli topluluğa antlaşma, koruma ilişkisi ya da bağlılık yoluyla bağlanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"çıkışı zor olduğu için bu kökten adlandırılmış tanınmış bir tepe"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Firdevs'in karşısında bulunan iki bahçenin ortak adı"}],"lexicalization_note":"Tanım, sözlükselleşmiş kişi, topluluk, put ve yer adlarını mensubiyet ve topluluğa bağlanma türetmelerinden ayırır; bunları yalın güneş anlamıyla birleştirmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı sözlüksel kökten kişi, topluluk ve yer adı üretme düzenini paylaşan üç komşu sınıflandırma benzerliğini gösterir, fakat özel ad kimlikleri farklı olduğu için daha güçlü bir ilişki kurulmaz.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Adlandırma yöntemi ortaktır, ancak sözlüksel kökenler ve adların kimlikleri ayrıdır; odak dal ayrıca put, su kaynağı ve topluluğa bağlanma türetmesini taşır.","focus_only":"Odak dal güneş öğeli kişi, topluluk, put ve yer adlarıyla bunlara bağlı mensubiyet ve katılma türetmelerini içerir.","gloss":"bir sözcükten kurulmuş kişi ve yer adları","neighbor_only":"Komşu dal kendi ayrı sözlüksel öğesinden kurulmuş kişi ve yer adlarını içerir.","neighbor_ref":"root_000943/B007","relation_type":"same_field","shared_zone":"Her iki dal, genel sözlük anlamından özel ada aktarılmış kişi ve yer adlarını toplar."},{"boundary_match":"field_only","distinction":"Özel adların kökeni ve dağıldığı varlık türleri farklıdır; bu nedenle adlar birbirinin yerine geçmez ve yalnız sınıflandırma alanı ortaktır.","focus_only":"Odak dal güneş öğeli put ve su kaynağı adlarını, mensubiyeti ve topluluğa bağlanmayı içerir.","gloss":"kişi, topluluk ve yer adları","neighbor_only":"Komşu dal kendi sözcüğünden aktarılmış kişi, hayvan, hükümdar, topluluk ve vadi adlarını içerir.","neighbor_ref":"root_001053/B013","relation_type":"same_field","shared_zone":"Kişi, topluluk ve yer adlarının ortak bir sözlüksel kökten türemesi iki dalı aynı alana yerleştirir."},{"boundary_match":"field_only","distinction":"Ortak olan yalnız adlandırma yapısıdır; adların taşıdığı sözlüksel öğe, tek tek kimlikleri ve odak dalın put ile bağlılık türetmesi farklıdır.","focus_only":"Odak dal put, su kaynağı, tepe ve bahçe adlarıyla topluluğa bağlanma türetmesini de kapsar.","gloss":"kişi, kabile ve yer adları ailesi","neighbor_only":"Komşu dal kendi sözcüğünden türemiş daha geniş kişi adı, kabile ve yer adı ailesini kapsar.","neighbor_ref":"root_000707/B012","relation_type":"same_field","shared_zone":"İki dal da bir sözlüksel öğeden kurulan kişi, topluluk ve yer adlarını düzenler."}],"source_phrase_ar":"عبد شمس (maqayis;sihah)؛ الشمس صنم قديم (maqayis)؛ شمس عين ماء معروفة (maqayis)؛ عبشمس وعبشمي (maqayis;sihah)؛ تعبشم الرجل (sihah)؛ الشموس هضبة معروفة (tahdhib)؛ الشميستان جنتان بإزاء الفردوس (tahdhib)","source_summary":"Kanıt, güneş sözcüğünden kurulan adları kişiler, topluluklar, bir put, bir su kaynağı, bir tepe ve iki bahçeye dağıtır; mensubiyet ile antlaşma, koruma ilişkisi veya bağlılık üzerinden topluluğa katılma türetmelerini de bu adlandırma alanına bağlar.","sources":["MQ","SI","TA"],"what_is_ar":"الأعلام والأنساب والمواضع المسماة بالشمس أو المشتقة منها","what_is_not_ar":"ليس المعنى العام للشمس ولا صفات الدواب والطباع ولا القلائد"},"support_links":[]},{"boundary":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B001","candidate_links":[{"candidate_id":"cand_b35a297c8d16025c277f","lane":"micro"},{"candidate_id":"cand_331b3723f00db064710d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"güneş yükseldikten sonraki kuşluk vakti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın doğuş sonrası başlayıp öğleye yaklaşan temel zaman alanını doğal ve kısa biçimde karşılar.","boundary_detail":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_image_ar":"امتداد الضحى في النهار","concept_gloss":"güneş yükseldikten sonraki kuşluk vakti","contextual_glosses":[{"applicability":"Zaman dizisinin ilk aşamasını özellikle belirtmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğleye yaklaşan daha ileri kuşluk aşamalarını dışarıda bırakır.","preserves":"Doğuş sonrasındaki erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"güneş doğduktan hemen sonraki vakit","usage_role":"contextual"},{"applicability":"Bir eylemin erken gündüzün daha ileri bir aşamasına bırakıldığını anlatan cümlelere uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zaman alanının doğuşa yakın ilk aşamasını karşılamaz.","preserves":"Günün yükselmesini ve eylemin o zamana bağlanmasını korur."},"facet_ids":["F002","F003"],"text":"gün iyice yükselince","usage_role":"contextual"}],"definition":"Güneş doğduktan sonra günün yükselip yayılmasıyla başlayan, aşamalar halinde ilerleyerek öğleye yaklaşan erken aydınlık zaman dilimidir. Bir yerde bu vakte kadar kalma veya bir işi bu vaktin daha ileri aşamasına bırakma kullanımları bu zaman çekirdeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."},{"facet_id":"F002","role":"specialization","statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Güneş doğmadan önceki ve dalın kapsamadığı daha geniş zaman aralığını da ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Günün erken bölümünde bulunma özelliğini korur."},"text":"sabah"}],"identity_rationale":"Kaynak ifadesi, güneş doğduktan sonra başlayan ve gün yükseldikçe ilerleyen bir zaman dizisini açıkça verir. Çerçevedeki günün yükselmesi ve uzaması bu diziyi doğru karşılar; eylemi bu zamana bırakma ise zaman anlamına bağlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"günün yükseldiği erken vakit"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşluk vakti"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"günün uzayıp öğleye yaklaştığı kuşluk vakti"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güneş doğduktan sonraki ilk kuşluk vakti"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kuşluk vaktine girmek veya o vakte kadar kalmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuşluk namazını vakit iyice yükselene kadar geciktirmek"}],"lexicalization_note":"Tanım, günün erken aydınlık bölümünü temel alır; bu vakte girme ve bir işi vaktin ilerisine bırakma yalnızca ilgili biçim ve söz öbeklerine bağlıdır.","neighbor_coverage_note":"Verilen bütün komşu kartları değerlendirildi; zaman sınırını en açık gösteren üç karşılaştırma seçildi, yalnızca aynı gün içindeki olayları anan daha uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir erken gündüz zaman alanını ve onun aşamalarını adlandırır; komşu dal ise günün yükselmesini bir oluş olarak anlatır ve kaynak kartında daha geç bir güneş konumuna da uzanır.","focus_only":"Doğuş sonrasından öğleye yaklaşmaya kadar uzanan adlandırılmış zaman aşamalarını ve eylemi o vakte bırakmayı kapsar.","gloss":"günün yükselmesi","neighbor_only":"Günün yükselmesi yanında bazı kullanımlarda güneşin duvarlardan çekilmeye başlamasını da kapsar.","neighbor_ref":"root_000546/B012","relation_type":"near_synonym","shared_zone":"İki dal da gündüzün yükselip yayılmasını zaman belirleyici bir özellik olarak kullanır."},{"boundary_match":"partial","distinction":"Odak dalın gönderimi zamandır; komşunun çekirdeği ise dikleşme ve yükselme hareketidir. Bu nedenle olağan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Güneş doğduktan sonra ilerleyen zaman dilimini adlandırır.","gloss":"yükselen gündüz","neighbor_only":"Bir şeyin dikilmesini ve doğrulmasını temel alıp günün yükselmesini bu çekirdeğin bir uygulaması olarak verir.","neighbor_ref":"root_000642/B012","relation_type":"near_neighbor","shared_zone":"Her ikisinde de gündüzün yükselmesi ortak bir görüntüdür."},{"boundary_match":"field_only","distinction":"Birinci dal zamansal bir bölümdür; ikinci dal ise maruz kalma veya görünürlük durumudur. Aynı güneşli sahneyi paylaşmaları anlamlarını birleştirmez.","focus_only":"Güneşin yükselmesine göre belirlenen bir gündüz vaktini anlatır.","gloss":"vakit ile güneşe açıklık","neighbor_only":"Güneşe açık kalmayı, görünür olmayı ve dışta bulunan belirgin yanı anlatır.","neighbor_ref":"root_000904/B002","relation_type":"same_field","shared_zone":"Her iki dal da güneş ve açık gündüz çevresinde örgütlenir."}],"source_phrase_ar":"الضحاء امتداد النهار (maqayis); الضحو ارتفاع النهار والضحى فويق ذلك والضحاء ممدود إذا امتد النهار (ayn); الضحو لغة في الضحى (jamhara); ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء (sihah); الضحى انبساط الشمس وامتداد النهار وسمي الوقت به (mufradat)","source_summary":"Kaynakların ortak çizgisi, güneş doğduktan sonra günün yükselmesiyle açılan ve öğleye doğru ilerleyen bir zaman alanıdır. Adlandırmalar bu alanın birbirini izleyen erken ve ileri aşamalarını, ayrıca eylemin o vakte ulaşmasını anlatır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الضحو والضحى والضحاء ووقت ارتفاع النهار وتأخير الفعل إلى ذلك الوقت","what_is_not_ar":"لا يدخل فيه مجرد البروز للشمس ولا الذبيحة ولا الطعام إلا من جهة التسمية بالوقت"},"support_links":["sup_6f33c65304294242491d","sup_e27927c70ff171d708ba"]},{"boundary":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B002","candidate_links":[{"candidate_id":"cand_c897026b9663d7760757","lane":"micro"},{"candidate_id":"cand_21dc8ec378d97588871e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"güneşe veya bakışa açık olup görünürleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın güneşe maruz kalma ile dışta ve görünür olma arasındaki ortak çekirdeğini birlikte karşılar.","boundary_detail":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_image_ar":"البروز للشمس والظهور","concept_gloss":"güneşe veya bakışa açık olup görünürleşme","contextual_glosses":[{"applicability":"Bir kişinin ya da şeyin güneşe maruz kalmasını anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bakışa görünür olma, dış kenar ve alenen yapma kullanımlarını karşılamaz.","preserves":"Güneşe açık hale gelme ve ısıya maruz kalma yönünü korur."},"facet_ids":["F001","F004"],"text":"güneşe çıkmak","usage_role":"contextual"},{"applicability":"Yolun, yerin veya başka bir şeyin belirgin biçimde görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş ısısına maruz kalma ve terleme yönünü dışarıda bırakır.","preserves":"Bakışa açık ve belirgin olma yönünü korur."},"facet_ids":["F001","F002"],"text":"açıkça görünmek","usage_role":"contextual"},{"applicability":"Bir eylemin gizlenmeden ve herkesin görebileceği biçimde yapılmasına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer, güneş ve bedensel maruz kalma kullanımlarını karşılamaz.","preserves":"Eylemin bakışa açık ve belirgin biçimde yapılmasını korur."},"facet_ids":["F003"],"text":"alenen yapmak","usage_role":"contextual"}],"definition":"Bir kişinin, yerin ya da şeyin güneşe veya bakışa açık duruma gelmesi ve böylece dışta, belirgin ya da görünür olmasıdır. Güneş ısısına maruz kalma ve terleme ile bir işi açıkça yapma, bu çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."},{"facet_id":"F002","role":"extension","statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."},{"facet_id":"F004","role":"associated_use","statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşe maruz kalmayı, dışta kalan yanı ve alenen yapma kapsamını tam olarak taşımaz.","preserves":"Görünür ve belirgin hale gelme yönünü korur."},"text":"ortaya çıkma"}],"identity_rationale":"Kaynak ifadesi güneşe çıkma, güneş ısısına maruz kalma, görünür hale gelme, dışta ve açıkta bulunan yan ile bir işi herkesin görebileceği biçimde yapma kullanımlarını birlikte destekler. Terleme, bu alanın bağımsız çekirdeği değil, güneş ısısına maruz kalmayla bağlantılı bir sonuçtur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güneşe çıkmak veya güneşin ısısına maruz kalmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güneşe çık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yol görünür hale geldi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yerleşimin dışta ve açıkta kalan yanı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dışta kalan açık bölgeler veya kenarlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu açıkça ve herkesin gözü önünde yaptı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"açıkta ve görünür yer"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güneşin neredeyse hiç eksik olmadığı yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"atın bacakları arasındaki bölüm görünür olur"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"terledim"}],"lexicalization_note":"Güneşe çıkma ve görünür olma ortak çekirdektir; yolun görünmesi, açık yer, dış kenar, alenen yapma ve terleme ilgili biçim ve söz öbeklerinin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel görünürlük dalları ile aynı kökün zaman dalı sınırı en çok keskinleştirdiği için yayımlandı, yalnızca dolaylı güneş veya açıklık çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel görünme ve açığa çıkma alanındadır; odak dal ise bu alanı güneşe açıklık, dış kenar ve açıkça yapılan eylemle özel olarak birleştirir.","focus_only":"Güneşe çıkmayı, güneş ısısına maruz kalmayı, dışta kalan yanı ve terlemeyi kapsar.","gloss":"açığa çıkıp görünür olma","neighbor_only":"Gizli veya içte olanın genel olarak açığa çıkıp anlaşılır hale gelmesini kapsar.","neighbor_ref":"root_000970/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin dışta, açık ve görünür olmasını anlatır."},{"boundary_match":"partial","distinction":"Odak için önceden gizli olma şart değildir ve güneş altında bulunma belirgindir; komşu ise gizlilikten görünürlüğe geçişi temel alır.","focus_only":"Güneşe maruz kalma ile öteden beri dışta ve açıkta bulunan yeri de kapsar.","gloss":"görünür hale gelme","neighbor_only":"Önceden gizli ya da örtülü olanın sonradan açılması ve bir metnin yayımlanması yönünü kapsar.","neighbor_ref":"root_000105/B001","relation_type":"near_synonym","shared_zone":"İki dalın kesişimi, bir şeyin saklı olmayıp görünür duruma gelmesidir."},{"boundary_match":"partial","distinction":"Komşu dar bir açık karşılaşma kalıbına bağlıdır; odak dal ise kişi, yol, yer ve eylem üzerinde daha geniş fakat güneşle güçlü biçimde ilişkili bir açıklık alanıdır.","focus_only":"Güneş altında kalma, dış kenar, alenen eylem ve terleme gibi daha geniş gerçekleşmeleri vardır.","gloss":"örtüsüz ve açıkta olma","neighbor_only":"Özellikle hiçbir şeyin örtmediği açık bir karşılaşma durumuna bağlıdır.","neighbor_ref":"root_000086/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de örtüsüz, dışta ve bakışa açık bulunmayı anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal bir açıklık ve görünürlük durumudur; komşu dal zamandır. Bir kişinin o vakitte bulunması onun zorunlu olarak güneşe açık olduğu anlamına gelmez.","focus_only":"Güneşe veya bakışa maruz kalıp görünür olmayı anlatır.","gloss":"güneşe açıklık ile kuşluk vakti","neighbor_only":"Güneşin yükselişine göre belirlenen erken gündüz zamanını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"İki dal güneşli erken gündüz sahnesini paylaşır."}],"source_phrase_ar":"ضحى الرجل يضحى إذا تعرض للشمس (maqayis); اضح أي ابرز للشمس (maqayis;ayn); ضحا الطريق إذا بدا وظهر (maqayis;sihah); ضاحية كل بلدة ناحيتها البارزة (maqayis;ayn;sihah;mufradat); فعل ذلك ضاحية أي ظاهرا بينا (maqayis;ayn;sihah); ضحيت عرقت وضحيت للشمس إذا برزت لها (sihah)","source_summary":"Kaynaklar, güneşe çıkma ile görünür ve dışta olmayı aynı anlam alanında birleştirir. Yolun görünmesi, yerin açık kenarı, işin alenen yapılması ve güneş altında terleme bu ortak açıklık durumunun farklı bağlamlarıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه التعرض للشمس وحرها والتعرق والبروز والظهور والناحية البارزة والعلانية","what_is_not_ar":"لا يدخل فيه وقت الضحى من حيث هو وقت ولا الأضحية ولا الغداء"},"support_links":["sup_067a3ce17719d86f29bc","sup_7c1fd4c677030fea206e"]},{"boundary":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B003","candidate_links":[{"candidate_id":"cand_50df550fde99174493a2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"erken gündüz öğünü ve o vakitte otlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın öğün ile hayvan otlatma kullanımlarını ortak zaman sınırı altında birlikte gösterir.","boundary_detail":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_image_ar":"طعام الضحاء ورعي أوله","concept_gloss":"erken gündüz öğünü ve o vakitte otlatma","contextual_glosses":[{"applicability":"İnsanların günün erken aydınlık bölümündeki öğünü yemesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve ve koyunların otlatılması kullanımlarını dışarıda bırakır.","preserves":"Öğünü ve onun erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"kuşluk öğünü yemek","usage_role":"contextual"},{"applicability":"Deve veya koyunların erken aydınlık vakitte otlaması ya da otlatılması bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların yediği öğün ve yeme eylemi anlamını karşılamaz.","preserves":"Otlatma eylemini ve erken gündüz zaman sınırını korur."},"facet_ids":["F002","F003"],"text":"günün başında otlatmak","usage_role":"contextual"}],"definition":"Günün erken aydınlık bölümünde yenen öğünü ve o sırada yemek yemeyi; ayrıca deve ya da koyunların günün başında otlamaya koyulmasını anlatan zaman bağlı kullanımlar alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Günün ilk öğünü olma yönündeki çağdaş ve daha dar bir öğün düzenini çağrıştırır.","collision":"Çağdaş kahvaltı kavramıyla karışarak tarihsel zaman sınırını belirsizleştirir.","fit":"displacement","loses":"Kuşluk vaktine özgü zaman bağını ve hayvan otlatma kullanımlarını kaybeder.","preserves":"Günün erken bölümünde yenen bir öğün olma özelliğini korur."},"text":"kahvaltı"}],"identity_rationale":"Kaynak ifadesi iki zaman bağlı kullanımı açıkça bir araya getirir: günün erken aydınlık bölümünde yenen öğün ve evcil hayvanların o sırada otlamaya başlaması. Bunlar zamanın kendisi değildir; yeme ve otlatma eylemlerinin o vakitle sınırlandırılmış adlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kuşluk öğünü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuşluk öğününü yemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"develer günün başında otlamaya koyuldu"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"koyunlarını kuşluk vaktinde otlatmak"}],"lexicalization_note":"Öğün adı ve yemek yeme biçimleri ile deve ya da koyun otlatma söz öbekleri ayrı tutulur; zaman bağlantısı bu kullanımlardan bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün komşu adayları gözden geçirildi; erken gündüzü akşamdan, genel otlatmadan ve zamanın kendisinden ayıran dört kart yayımlandı, yem ve sürü çevresindeki daha dolaylı ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Eylem türleri paraleldir, fakat zaman ekseninin karşıt uçlarına yerleşirler: odak erken aydınlık vakte, komşu akşam ve geceye bağlıdır.","focus_only":"Erken aydınlık vakitteki öğün ve otlatmayı anlatır.","gloss":"gündüz başı ile akşam yeme ve otlatması","neighbor_only":"Akşam ya da geceye bağlı yemek ve otlatmayı anlatır.","neighbor_ref":"root_001017/B005","relation_type":"polarity_pair","shared_zone":"İki dal da bir öğünü ve hayvanların otlatılmasını günün belirli bölümüne bağlar."},{"boundary_match":"partial","distinction":"Odak dal zamana bağlı özel bir otlatma kullanımıdır; komşu dal otlatmanın genel alanını, otlağı ve yeneni de kapsar.","focus_only":"Otlatmayı günün erken aydınlık bölümüyle sınırlar ve ayrıca insan öğününü kapsar.","gloss":"erken vakitte otlatma","neighbor_only":"Hayvanın otlamasını, yemi ve otlak yerini zaman sınırı olmadan genel olarak kapsar.","neighbor_ref":"root_000574/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı evcil hayvanların otlamasıdır."},{"boundary_match":"field_only","distinction":"Odak dal zamanın adını eylem ve öğüne aktarır; komşu dal ise zaman diliminin kendisidir. Her iki yön tek bir yalın anlam olarak birleştirilmemelidir.","focus_only":"O vakitte yapılan yeme ve otlatma eylemlerini adlandırır.","gloss":"kuşluk vakti ile kuşluk etkinliği","neighbor_only":"Eylemlerden bağımsız olarak vaktin kendisini ve aşamalarını adlandırır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Yeme ve otlatma kullanımları komşu dalın belirlediği erken gündüz zamanında gerçekleşir."},{"boundary_match":"partial","distinction":"Odak için belirleyici olan günün vaktidir; komşu için belirleyici olan otlağın bolluğu ve hayvanın genişçe beslenmesidir.","focus_only":"Günün başındaki otlatma zamanını ve insan öğününü içerir.","gloss":"zamanlı otlatma ile bol otlak","neighbor_only":"Bolluk içinde dilediğince otlama, geniş otlak ve doygun beslenme koşulunu içerir.","neighbor_ref":"root_000538/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sürülerin otlamasını konu edinir."}],"source_phrase_ar":"للطعام الذي يؤكل في ذلك الوقت ضحاء (maqayis); هم يتضحون أي يتغدون والغداء الضحاء (maqayis); نتضحى أي نتغدى (ayn); تضحت الإبل أخذت في الرعي من أول النهار (ayn); الضحاء أيضا الغداء وهم يتضحون أي يتغدون (sihah); ضحى فلان غنمه أي رعاها بالضحا (sihah); تضحى أكل ضحى والضحاء والغداء لطعامهما (mufradat)","source_summary":"Kaynaklar erken aydınlık vakitte yenen öğünü ve o öğünü yeme eylemini ortak biçimde verir; aynı zaman bağı, develerin otlamaya başlamasına ve koyunların o vakitte otlatılmasına da uygulanır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الغداء المسمى ضحاء ويتضحون بمعنى يتغدون ورعي الإبل أو الغنم في أول النهار","what_is_not_ar":"لا يدخل فيه الذبح ولا مطلق وقت الضحى بلا أكل أو رعي"},"support_links":["sup_d1be31215508bd62eb34"]},{"boundary":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"bayram gününde dinsel amaçla kesilen hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne, belirli gün ve dinsel kesim koşullarını birlikte taşıyan en kısa doğal karşılığıdır.","boundary_detail":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_image_ar":"ذبيحة يوم الأضحى","concept_gloss":"bayram gününde dinsel amaçla kesilen hayvan","contextual_glosses":[{"applicability":"Hayvanın ilgili bayram gününde kesilmek üzere ayrılmış olmasını öne çıkaran kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kesilmiş olabilme durumunu açıkça söylemez.","preserves":"Hayvanın belirli bayram gününde kesilmek üzere ayrılmasını korur."},"facet_ids":["F001"],"text":"bayram günü kesilmek üzere ayrılan hayvan","usage_role":"contextual"},{"applicability":"Koyunun ilgili günde kesilmesini bildiren söz öbeği için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanı adlandıran genel biçimleri ve koyun dışındaki olası hayvanları kapsamaz.","preserves":"Koyunu, kesme eylemini, özel amacı ve günü korur."},"facet_ids":["F003"],"text":"bayram günü adaklık koyun kesmek","usage_role":"contextual"}],"definition":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen koyun ya da başka hayvandır. Böyle bir koyunu o gün kesme eylemi, nesne merkezli bu anlamın söz öbeğine bağlı gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Belirli bayram gününe bağlı olmayan daha genel sunu ve özveri anlamlarını da ekler.","collision":"Günlük dilde mecazi olarak zarar gören kişi anlamıyla da karışabilir.","fit":"broadening","loses":null,"preserves":"Dinsel amaçla sunulan veya kesilen şey yönünü korur."},"text":"kurban"}],"identity_rationale":"Kaynak ifadesi, belirli bayram gününde kesilen koyun ya da başka hayvanı, bu hayvan için kullanılan biçimleri ve koyun kesme eylemini açıkça verir. Dalın kimliği genel hayvan kesimi değil, gün ve dinsel uygulamayla sınırlandırılmış kesim nesnesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen koyun veya başka hayvan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen hayvan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aynı hayvan için kullanılan başka bir ad"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"dinsel hayvan kesiminin yapıldığı bayram günü veya o gün kesilen hayvanlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla bir koyun kesmek"}],"lexicalization_note":"Hayvanı adlandıran biçimler dalın merkezindedir; koyun kesme eylemi yalnızca verilen söz öbeğinde ve belirli bayram günü koşuluyla tanımlanır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel dinsel kesim hayvanı, genel kesme işlemi, belirli hayvan türü ve kesim sonrası işlemle kurulan dört sınır yayımlandı, yalnızca aynı tören alanını paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı belirli bayram günü ve o güne özgü adlandırmadır; komşu dal daha genel dinsel sunu alanına uzanır.","focus_only":"Belirli bayram gününü ve o gün kesilen hayvana ait ad biçimlerini şart koşar.","gloss":"bayramlık kesim hayvanı","neighbor_only":"Yaklaşma amacıyla sunulan kesim hayvanını ve dökülen kanı gün şartı olmadan daha genel biçimde kapsar.","neighbor_ref":"root_001498/B002","relation_type":"near_synonym","shared_zone":"İki dal da dinsel yakınlaşma amacıyla kesilen hayvanı anlatabilir."},{"boundary_match":"partial","distinction":"Odak nesne ve törensel zaman merkezlidir; komşu ise kesme işleminin tamamlanması merkezlidir. Her genel kesim bu dalın kapsamına girmez.","focus_only":"Belirli gün ve dinsel amaçla tanımlanan hayvanı merkez alır.","gloss":"kesim hayvanı ile kesme işlemi","neighbor_only":"Hayvanın yaşamını sona erdiren kesim işlemini, gün ve dinsel amaç koşulu olmadan merkez alır.","neighbor_ref":"root_000517/B003","relation_type":"near_neighbor","shared_zone":"Odak daldaki hayvanın gerçekleştirilmiş kullanımında bir kesme işlemi bulunur."},{"boundary_match":"partial","distinction":"Odak dal işlev ve günle, komşu dal ise hayvan türü ve sunulma durumuyla sınırlıdır; kapsamları kesişse de özdeş değildir.","focus_only":"Bayram günündeki dinsel kesime ayrılan hayvanı türden bağımsız bir işlevle adlandırır.","gloss":"bayramlık hayvan ile iri sunu hayvanı","neighbor_only":"Özellikle deve veya sığır türünden sunulan iri hayvanı adlandırır.","neighbor_ref":"root_000096/B003","relation_type":"near_neighbor","shared_zone":"Bazı iri hayvanlar her iki dalın gönderimine birden girebilir."},{"boundary_match":"thematic_only","distinction":"Odak hayvan ile kesim anına, komşu ise sonradan etin işlenmesine ve izleyen günlere aittir; anlamsal çekirdekleri ortak değildir.","focus_only":"Belirli günde kesilen hayvanı ve kesme eylemini anlatır.","gloss":"kesim ve sonrasındaki et kurutma","neighbor_only":"Kesimden sonra etin güneşte kurutulmasını ve bunu izleyen günlerin adlandırılmasını anlatır.","neighbor_ref":"root_000790/B002","relation_type":"thematic","shared_zone":"İki dal aynı bayram çevrimindeki hayvan kesimi ve et hazırlama sahnesinde yer alır."}],"source_phrase_ar":"الضحية معروفة وهي الأضحية (maqayis); أربع لغات أضحية وإضحية وضحية وأضحاة (maqayis;sihah); الضحية الأضحية والجميع الضحايا والأضاحي وهي الشاة يضحي بها يوم الأضحى (ayn); ضحى بشاة من الأضحية وهي شاة تذبح يوم الأضحى (sihah); الأضحية جمعها أضاحي وقيل ضحية وضحايا وأضحاة وأضحى (mufradat)","source_summary":"Kaynakların ortak çekirdeği, belirli bayram gününde dinsel amaçla kesilen hayvandır. Çeşitli tekil ve çoğul adlandırmalar aynı gönderime bağlanır; koyun kesme eylemi de bu gün ve amaç koşuluyla verilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الأضحية والضحية والضحايا والأضاحي والأضحاة وما يذبح يوم الأضحى","what_is_not_ar":"لا يدخل فيه مطلق الطعام ولا الرعي ولا البروز للشمس"},"support_links":[]},{"boundary":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B005","candidate_links":[{"candidate_id":"cand_b35a297c8d16025c277f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"kuşluk aydınlığını andıran parlak açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güneş, açık gökyüzü ve at rengi uzantılarını birleştiren temel görsel niteliği karşılar.","boundary_detail":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_image_ar":"ضياء الضحى وصفاؤه","concept_gloss":"kuşluk aydınlığını andıran parlak açıklık","contextual_glosses":[{"applicability":"Gece veya günün gökyüzü açıklığıyla birlikte aydınlık olduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin adı ve atların açık kır-boz rengi kullanımlarını karşılamaz.","preserves":"Aydınlık ile bulutsuz açıklığı birlikte korur."},"facet_ids":["F001","F003"],"text":"bulutsuz ve aydınlık","usage_role":"contextual"},{"applicability":"Atın açık, beyaza çalan kır-boz rengini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş, gün ve gece aydınlığı kullanımlarını dışarıda bırakır.","preserves":"Parlak açıklığın at rengine aktarılmış yönünü korur."},"facet_ids":["F004"],"text":"açık kır-boz renkli","usage_role":"contextual"}],"definition":"Kuşluk aydınlığını andıran parlaklık ve bulutsuz açıklıktır. Bu nitelik güneşin adlandırılmasına, aydınlık gece ve güne ilişkin söz öbeklerine, ayrıca atların açık kır-boz rengine aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."},{"facet_id":"F002","role":"extension","statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."},{"facet_id":"F004","role":"extension","statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynağı ve niteliği sınırsız olan her türlü ışığı kapsama ekler.","collision":"At rengindeki açık kır-boz görünümü doğrudan karşılayamaz.","fit":"broadening","loses":null,"preserves":"Aydınlık ve parlaklık yönünü korur."},"text":"ışık"}],"identity_rationale":"Kaynak ifadesi güneşin bu adla anılmasını, bulutsuz ve aydınlık gece ile günü, ayrıca atlarda açık kır-boz rengi birlikte aktarır. Çerçevedeki kuşluk aydınlığı ve açıklık bunları birleştiren niteliktir; at rengi doğrudan ışık değil, bu açık parlak niteliğin renk alanına aktarımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güneş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gece"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bulutsuz, berrak ve aydınlık gece"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gün"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli at"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli kısrak"}],"lexicalization_note":"Aydınlık ve açıklık ortak niteliktir; güneş adı, bulutsuz gece ve gün söz öbekleri ile at rengi biçimleri kendi özel kapsamlarında tutulur.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; açık gökyüzü, aydınlanma, genel ışık ve aynı kökün zaman dalı temel sınırları gösterdiği için seçildi, yalnızca belirli ışık kaynaklarını anlatan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal niteliği geceye, güneş adına ve at rengine taşır; komşu dal gündüz beyazlığı ve karanlığın açılması çevresinde kalır.","focus_only":"Güneş adı, aydınlık gece ve atların açık kır-boz rengi uzantılarını kapsar.","gloss":"aydınlık ve açık gökyüzü","neighbor_only":"Gündüzün beyazlığı ile gökyüzü açıklığının karanlığı giderip günü yaymasını merkez alır.","neighbor_ref":"root_000256/B007","relation_type":"near_synonym","shared_zone":"İki dal da gün ışığının parlaklığı ile gökyüzünün açıklığını birleştirir."},{"boundary_match":"partial","distinction":"Odak kuşluk benzeri parlak açıklığa ve renk uzantısına dayanır; komşu karanlıktan aydınlığa çıkışı ve yüz parıltısını da kapsayan başka bir gelişim çizgisidir.","focus_only":"Bulutsuz geceyi ve atların açık kır-boz rengini içerir.","gloss":"aydınlanıp belirginleşme","neighbor_only":"Şafak aydınlığını, yüzün parlamasını ve karanlıktan sonra belirginleşen zamanı içerir.","neighbor_ref":"root_000712/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de aydınlık, beyazlık ve açık görünüm alanında buluşur."},{"boundary_match":"partial","distinction":"Odak belirli bir parlak-açık görünüm niteliğidir; komşu ise kaynağı ne olursa olsun ışığın yayılması ve bir şeyi aydınlatmasıdır.","focus_only":"Bulutsuz açıklığı ve atların açık kır-boz rengini kuşluk ışığı benzerliğiyle birleştirir.","gloss":"parlak açıklık ile yayılan ışık","neighbor_only":"Ateş, kandil, şimşek ve tan gibi çok çeşitli kaynaklardan yayılan ışığı ve aydınlatma eylemini kapsar.","neighbor_ref":"root_000919/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı ışık veren veya aydınlık görünen şeylerdir."},{"boundary_match":"field_only","distinction":"Bir dal görsel nitelik, diğeri zamansal bölümdür. Aydınlık başka zamanlara ve at rengine taşınabilirken zaman anlamı taşınmaz.","focus_only":"Kuşluk ışığına benzer parlaklık ve açıklık niteliğini anlatır.","gloss":"kuşluk aydınlığı ile kuşluk vakti","neighbor_only":"Kuşluk zamanını ve onun gündüz içindeki aşamalarını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Odak niteliğin benzetme kaynağı, komşu dalın adlandırdığı zamanın ışığıdır."}],"source_phrase_ar":"تسمى الشمس الضحاء (ayn); ليلة إضحيانة وضحياء أي مضيئة لا غيم فيها (maqayis); ليلة ضحياء مضيئة لا غيم فيها وليلة إضحيانة (sihah); يوم إضحيان مضيء لا غيم فيه (ayn); الأضحى من الخيل الأشهب والأنثى ضحياء (sihah); ليلة إضحيانة وضحياء مضيئة إضاءة الضحى (mufradat)","source_summary":"Kaynakların toplu verisi kuşluk ışığına benzeyen parlak ve bulutsuz açıklığı gösterir. Güneş adı ile aydınlık gece ve gün bu niteliği doğrudan taşırken, atların açık kır-boz rengi görsel bir uzantı oluşturur.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الشمس المسماة الضحاء والليلة المضيئة الصافية والبياض الأشهب في الخيل","what_is_not_ar":"لا يدخل فيه مجرد وقت الضحى ولا البروز المكاني"},"support_links":["sup_6f33c65304294242491d"]},{"boundary":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B006","candidate_links":[{"candidate_id":"cand_331b3723f00db064710d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","surface_ar":"ضُحَىٰ"}],"gloss":"yumuşak davranıp acele etmemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kayıtlı yapının ortak çekirdeği olan davranış yumuşaklığını ve hızın düşürülmesini birlikte karşılar.","boundary_detail":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_image_ar":"الرفق والإمهال","concept_gloss":"yumuşak davranıp acele etmemek","contextual_glosses":[{"applicability":"Bir işin sertlik ve acele olmadan ele alınmasını anlatan bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan bir yavaşlama buyruğu olma işlevini karşılamaz.","preserves":"İşin yumuşak ve acele edilmeden yürütülmesini korur."},"facet_ids":["F001","F002"],"text":"işi ağırdan ve yumuşaklıkla yürütmek","usage_role":"contextual"},{"applicability":"Karşıdakinden hızını düşürmesini isteyen doğrudan buyruk bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yumuşak davranarak yürütme anlamını tek başına taşımaz.","preserves":"Acele etmeme ve yavaşlama buyruğunu korur."},"facet_ids":["F003"],"text":"acele etme, yavaş ol","usage_role":"contextual"}],"definition":"Bir işi sertlik göstermeden, yumuşak davranarak ve acele etmeden yürütmektir. Bir kullanım eylem biçimini, diğeri ise doğrudan yavaşlama ve acele etmeme buyruğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."},{"facet_id":"F003","role":"specialization","statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Eylemi tümüyle durdurup zaman geçmesini bekleme anlamını ekler.","collision":null,"fit":"displacement","loses":"Yumuşak davranarak işi sürdürme ve doğrudan yavaşlama buyruğunu kaybeder.","preserves":"Hızı düşürme ve acele etmeme yönünü kısmen korur."},"text":"beklemek"}],"identity_rationale":"Kaynak ifadesi bir iş karşısında yumuşak davranmayı ve acele etmeme buyruğunu doğrudan verir. Çerçevedeki yumuşaklık ve ağırdan alma bu iki kullanımı doğru bir ortak alanda tutar; ancak anlam yalın köke değil, verilen söz öbeklerine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir işi yumuşak davranarak ve ağırdan alarak yürütmek"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"acele etme, yavaş ol"}],"lexicalization_note":"Yumuşak davranma ve acele etmeme iki kayıtlı yapı içinde tanımlanır; bunlardan sınırsız bir yalın kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; bekleme, genel yumuşaklık, geniş acele etmeme alanı ve başka bir yapıdaki yumuşak davranma en yararlı sınırları verdi, daha uzak ağırbaşlılık ve özdenetim adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda bekleme zorunlu değildir; iş yumuşakça sürdürülebilir. Komşu dal ise bekleme ve oyalanma yönünü açıkça içerir.","focus_only":"Yumuşak davranma ile acele etmeme buyruğunu iki kayıtlı yapı içinde birleştirir.","gloss":"yavaş davranıp beklemek","neighbor_only":"Bekleme eylemini doğrudan anlam alanına alır.","neighbor_ref":"root_000583/B008","relation_type":"near_synonym","shared_zone":"İki dal da hızın düşürülmesini ve bir işte zaman tanınmasını anlatır."},{"boundary_match":"partial","distinction":"Odak zamanlama ve acele etmeme yönünü de taşır ve belirli yapılara bağlıdır; komşu ise genel davranış yumuşaklığında daha geniştir.","focus_only":"Acele etmeme ve yavaşlama buyruğunu özellikle içerir.","gloss":"yumuşak ve ölçülü davranma","neighbor_only":"Sertliğin karşıtı olan genel davranış yumuşaklığını, kişilik niteliğini ve özenli uygulamayı daha geniş biçimde kapsar.","neighbor_ref":"root_000583/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sertlikten kaçınarak yumuşak davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın yumuşak davranma bileşeni ve yapı bağı önemlidir; komşu dal ise hız, bekleme ve kendini tutma yönlerinde daha geniştir.","focus_only":"Bir iş karşısındaki yumuşak davranışı kayıtlı söz öbekleriyle sınırlar.","gloss":"ağırdan alma ve acele etmeme","neighbor_only":"Gecikme, bekleme, ağırbaşlılık ve öfkeyi dizginleme gibi daha geniş acele etmeme alanını kapsar.","neighbor_ref":"root_000063/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işi aceleye getirmemeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal yumuşaklığın yanında hızın düşürülmesini açıkça içerir; komşu kart yalnızca yönelinen şeye yumuşak davranmayı bildirir.","focus_only":"Acele etmeme buyruğunu ve işi ağırdan almayı da kapsar.","gloss":"bir şeye yumuşak davranma","neighbor_only":"Yumuşak davranmayı tek bir başka söz öbeği içinde, yönelinen kişi veya şeyle ilişkilendirir.","neighbor_ref":"root_001017/B008","relation_type":"near_synonym","shared_zone":"İki dal belirli bir yapı içinde bir işe veya şeye yumuşak davranmayı anlatır."}],"source_phrase_ar":"ضحيت عن الأمر إذا رفقت (maqayis;sihah); ضح رويدا أي لا تعجل (sihah)","source_summary":"Kaynakların ortak verisi, bir işte yumuşak davranma ile acele etmeyip ağırdan alma yönlerini birleştirir. Biri işin yürütülüşünü, diğeri doğrudan yavaşlama buyruğunu anlatan iki sınırlı kullanım vardır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه ضحيت عن الأمر بمعنى رفقت وضح رويدا بمعنى لا تعجل","what_is_not_ar":"لا يدخل فيه أصل البروز ولا الضحى ولا الأضحية"},"support_links":["sup_e27927c70ff171d708ba"]}],"candidate_inventory":[{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_b4ec1d5a04c2558bc652","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:1:connective-oath-sequence","source_type":"word_analysis","support_ids":["sup_82f194a308615fa6f271","sup_9332c2b4d543f3d02bfa"],"title":"one letter launches the oath chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:1","qac_refs":["91:1:1:1"],"status":"accepted"}},{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_b780360aecbdf55a09cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:1:cross-ayah-sound-chain","source_type":"word_analysis","support_ids":["sup_9332c2b4d543f3d02bfa","sup_e7ea3eccb6547a7906a7"],"title":"opening prepares the later refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:1","qac_refs":["91:1:1:1"],"status":"accepted"}},{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_a0e3d2bfbfd7ca579aeb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:1:fused-opening-surface","source_type":"word_analysis","support_ids":["sup_9332c2b4d543f3d02bfa","sup_c401b86da99dc83ff7cc"],"title":"particle and sun sound as one unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:1","qac_refs":["91:1:1:1"],"status":"accepted"}},{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_57d183a50fc398e7392f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:1:oath-genitive-launch","source_type":"word_analysis","support_ids":["sup_1118221cc5dc98ce16c8","sup_9332c2b4d543f3d02bfa"],"title":"opening particle governs the oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:1","qac_refs":["91:1:1:1"],"status":"accepted"}},{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_f14f2759c69ad80719a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:1:role-contrast-with-second-wa","source_type":"word_analysis","support_ids":["sup_9332c2b4d543f3d02bfa","sup_fa2542943e395d94eee1"],"title":"same particle form changes role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:1","qac_refs":["91:1:1:1"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_22148eaf4123e2980d69","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:compressed-sound-texture","source_type":"word_analysis","support_ids":["sup_9d18bf378f6d222f6aa3","sup_e09f5cf995434734e07e"],"title":"dense sound suits the source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_3085ca0a429a1c1934fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:concrete-sun-over-generic-radiance","source_type":"word_analysis","support_ids":["sup_e09f5cf995434734e07e","sup_fc2d2b5d54f024b2f885"],"title":"source and radiance stay distinct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_0e6fc11e774823685850","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:definite-cosmic-referent","source_type":"word_analysis","support_ids":["sup_0503c23eec12fc55267b","sup_e09f5cf995434734e07e"],"title":"the known sun is invoked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_64e9859755bd3b635601","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:eschatological-sun-contrast","source_type":"word_analysis","support_ids":["sup_5b3817eedf942c1d9654","sup_e09f5cf995434734e07e"],"title":"stable oath sun contrasts collapse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_8f47373d3432dc822e30","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:feminine-source-product-link","source_type":"word_analysis","support_ids":["sup_c5fd81bd0642e5579288","sup_e09f5cf995434734e07e"],"title":"sun becomes antecedent and source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_ae6b87ac400945ac82c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:genitive-oath-object","source_type":"word_analysis","support_ids":["sup_a172553912fea993f0c6","sup_e09f5cf995434734e07e"],"title":"genitive case makes witness role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_6249ae711c62f1368772","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:root-force-exposure-narrowed","source_type":"word_analysis","support_ids":["sup_e09f5cf995434734e07e","sup_fe9dd87437fe840ed0fb"],"title":"root field adds force but not a new sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_f5fe2d512dce30432c7f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:source-emitter-frame","source_type":"word_analysis","support_ids":["sup_a9567beafcfc993fced6","sup_e09f5cf995434734e07e"],"title":"stellar-source language supports the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_54e645584cd9733c1238","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:2:sun-moon-pairing","source_type":"word_analysis","support_ids":["sup_4b824d8bc6b0dfc596cf","sup_e09f5cf995434734e07e"],"title":"the familiar dyad is delayed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:2","qac_refs":["91:1:1:2","91:1:1:3"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_45cfc8cfece206a4f4b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:balanced-short-onsets","source_type":"word_analysis","support_ids":["sup_955f8195e15bf2ba13c3","sup_a0238db1fe509b78ef86"],"title":"two short onsets balance the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_6e993b40e0cb432d150b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:coordinated-oath-continuation","source_type":"word_analysis","support_ids":["sup_955f8195e15bf2ba13c3","sup_9b5f7be50bbaa5c3eb3a"],"title":"second particle extends the oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_ef8f7ceca64d8c7fbfe5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:coordination-versus-renewed-oath","source_type":"word_analysis","support_ids":["sup_0ed1d6f1511711a1655c","sup_955f8195e15bf2ba13c3"],"title":"classical options share oath force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_c03d931d91bb636ea655","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:fused-second-object","source_type":"word_analysis","support_ids":["sup_955f8195e15bf2ba13c3","sup_9f84e3ca17ecc8ca6bf8"],"title":"second half enters bound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_9bb8028bfe3dbd5c5cf6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:repeated-wa-refrain","source_type":"word_analysis","support_ids":["sup_955f8195e15bf2ba13c3","sup_a0c3a685200d1c1ab1e4"],"title":"repetition prepares the oath series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:3"],"branch_refs":[],"candidate_id":"cand_885d716008aacc94836e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"91:1:3:source-manifestation-pivot","source_type":"word_analysis","support_ids":["sup_955f8195e15bf2ba13c3","sup_feac70d1140c186d906d"],"title":"the connector prevents collapse","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:3","qac_refs":["91:1:2:1"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_1a4bc4dc74a699578f48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:article-versus-possessive-echo","source_type":"word_analysis","support_ids":["sup_15a6f383c41f96a92ce2","sup_cf6bed21af59261f4a61"],"title":"possessed brightness differs from independent brightness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_4ef39a92c321c522b537","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:becoming-and-transition-narrowed","source_type":"word_analysis","support_ids":["sup_5ba40b3218c13dc3c22d","sup_cf6bed21af59261f4a61"],"title":"becoming colors the brightness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_346680f09cf97946c5b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:case-role-and-oath-term","source_type":"word_analysis","support_ids":["sup_cf6bed21af59261f4a61","sup_e3d53995080a268f67cf"],"title":"role options stay under possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_d23b4aa9c882f3cce706","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:closure-and-open-cadence","source_type":"word_analysis","support_ids":["sup_cf6bed21af59261f4a61","sup_efabee209de18a519f6c"],"title":"radiance becomes the ayah landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_c3bee81bf3161dfb3886","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:cosmic-possessed-brightness-echo","source_type":"word_analysis","support_ids":["sup_5ba207705b34a3b65e1b","sup_cf6bed21af59261f4a61"],"title":"possessed brightness has cosmic echo","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_734b74fb324c7044c8bd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:forenoon-exposure-field","source_type":"word_analysis","support_ids":["sup_bfca8b67352531f4dc72","sup_cf6bed21af59261f4a61"],"title":"forenoon light makes visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_5264d16ecee1bcf62235","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:next-ayah-pronoun-link","source_type":"word_analysis","support_ids":["sup_29ac5520156a70d3d599","sup_cf6bed21af59261f4a61"],"title":"suffix prepares the next pronoun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_187b51f0918aa62dce2f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:possessive-solar-brightness","source_type":"word_analysis","support_ids":["sup_6ab2da79f2d15e2ea147","sup_cf6bed21af59261f4a61"],"title":"the brightness belongs to the sun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_fde589a55b3e3e7def8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:radiation-output-narrowed","source_type":"word_analysis","support_ids":["sup_ad66359bfbb17707ca10","sup_cf6bed21af59261f4a61"],"title":"emitted field sharpens brightness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_b12e209279f12b1b8538","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:rare-root-weight","source_type":"word_analysis","support_ids":["sup_7196148cfe136d2ef336","sup_cf6bed21af59261f4a61"],"title":"uncommon root concentrates attention","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_acd981d46504764ce977","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:sacrifice-expenditure-narrowed","source_type":"word_analysis","support_ids":["sup_2f732118dcec23b714a7","sup_cf6bed21af59261f4a61"],"title":"sacrifice branch stays secondary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_bebcfa8ea00cd5a5e01a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:source-product-dependence","source_type":"word_analysis","support_ids":["sup_1d5f0354904c199ffae0","sup_cf6bed21af59261f4a61"],"title":"radiance is product, not peer source","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_e3aaf54b6efddac8ee98","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:source-to-spread-sound","source_type":"word_analysis","support_ids":["sup_3287a8e5190ea093e695","sup_cf6bed21af59261f4a61"],"title":"pacing opens from source to spread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:4"],"branch_refs":[],"candidate_id":"cand_af3a25aa1467540467ec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:4:suffixal-definiteness","source_type":"word_analysis","support_ids":["sup_3ad0268a9a3caa9f33d9","sup_cf6bed21af59261f4a61"],"title":"possession makes the noun definite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"91:1:4","qac_refs":["91:1:2:2","91:1:2:3"],"status":"accepted"}},{"anchor_refs":["91:1:1"],"branch_refs":[],"candidate_id":"cand_91713eee9e7ba8dada2b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000818"],"scope":"focus_ayah","source_local_id":"91:1:1:3","source_type":"qac_morpheme","support_ids":["sup_6a4b69f50313c7cd2dab"],"title":"QAC root occurrence: ش م س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:1:2"],"branch_refs":[],"candidate_id":"cand_79bbe5316bf09c8a3ea4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"91:1:2:2","source_type":"qac_morpheme","support_ids":["sup_3a014ae17dd2c28eeadb"],"title":"QAC root occurrence: ض ح و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["91:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:1","branch_refs":["root_000818/B001","root_000904/B001","root_000904/B005"],"candidate_id":"cand_b35a297c8d16025c277f","commentary_obligation":"review","hft_ref":"hft_bc9559584107c9e5226f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_radiant_extension","source_type":"hft","support_ids":["sup_6f33c65304294242491d"],"title":"baseline_radiant_extension","trust":"legacy_unbound"},{"anchor_refs":["91:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:1","branch_refs":["root_000818/B001","root_000904/B002"],"candidate_id":"cand_c897026b9663d7760757","commentary_obligation":"review","hft_ref":"hft_dae3f14e89c3086e38ec","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exposure_event","source_type":"hft","support_ids":["sup_7c1fd4c677030fea206e"],"title":"baseline_exposure_event","trust":"legacy_unbound"},{"anchor_refs":["91:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:1","branch_refs":["root_000904/B001","root_000904/B006"],"candidate_id":"cand_331b3723f00db064710d","commentary_obligation":"review","hft_ref":"hft_3ff0325c4e4552697518","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_measured_ripening","source_type":"hft","support_ids":["sup_e27927c70ff171d708ba"],"title":"baseline_measured_ripening","trust":"legacy_unbound"},{"anchor_refs":["91:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:1","branch_refs":["root_000818/B001","root_000904/B003"],"candidate_id":"cand_50df550fde99174493a2","commentary_obligation":"review","hft_ref":"hft_70c47d2e6e772568b7ec","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_creaturely_provision","source_type":"hft","support_ids":["sup_d1be31215508bd62eb34"],"title":"baseline_creaturely_provision","trust":"legacy_unbound"},{"anchor_refs":["91:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"91:1","branch_refs":["root_000818/B002","root_000818/B006","root_000904/B002"],"candidate_id":"cand_21dc8ec378d97588871e","commentary_obligation":"review","hft_ref":"hft_14a4c672089778de2e61","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_guarded_restiveness","source_type":"hft","support_ids":["sup_067a3ce17719d86f29bc"],"title":"baseline_guarded_restiveness","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"91:1:1:1","qac_word_ref":"91:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:1:1:2","qac_word_ref":"91:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","root_ar":"ش م س","surface_ar":"شَّمْسِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:1:2:1","qac_word_ref":"91:1:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","root_ar":"ض ح و","surface_ar":"ضُحَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:1:2:3","qac_word_ref":"91:1:2","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["91:1:1:1"],["91:1:1:2","91:1:1:3"],["91:1:2:1"],["91:1:2:2","91:1:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["91:1:1","91:1:2","91:1:3","91:1:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"91:1:1:1","qac_word_ref":"91:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"91:1:1:2","qac_word_ref":"91:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"شَمْس","morph_features":"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:1:3","qac_word_ref":"91:1:1","root_ar":"ش م س","surface_ar":"شَّمْسِ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"91:1:2:1","qac_word_ref":"91:1:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"91:1:2:2","qac_word_ref":"91:1:2","root_ar":"ض ح و","surface_ar":"ضُحَىٰ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"91:1:2:3","qac_word_ref":"91:1:2","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["91:1:1:1"],["91:1:1:2","91:1:1:3"],["91:1:2:1"],["91:1:2:2","91:1:2:3"]],"word_analysis_refs":["91:1:1","91:1:2","91:1:3","91:1:4"],"word_rows":[{"analysis_record_ref":"91:1:1","analytic_gloss_range_en":"opening oath particle that governs the following genitive noun; not ordinary coordination alone","analytic_root_gloss_range_en":null,"qac_refs":["91:1:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:1:2","analytic_gloss_range_en":"the definite, concrete sun as sworn object and source of the following possessed brightness","analytic_root_gloss_range_en":"sun and daylight are locally active; wider root branches such as restive force, hostility, names, and withholding remain background unless they sharpen exposure or force without replacing the sun","qac_refs":["91:1:1:2","91:1:1:3"],"root":{"arabic":"ش م س","transliteration":"sh-m-s"},"surface":{"arabic":"ٱلشَّمْسِ","transliteration":"al-shamsi"}},{"analysis_record_ref":"91:1:3","analytic_gloss_range_en":"coordinating particle that carries the existing oath frame forward to the second oath term","analytic_root_gloss_range_en":null,"qac_refs":["91:1:2:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"91:1:4","analytic_gloss_range_en":"the sun's own forenoon brightness and exposed radiance, made definite by the feminine possessive suffix","analytic_root_gloss_range_en":"forenoon daylight and exposed visibility are locally central; becoming and sacrificial/expenditure branches provide narrowed secondary pressure but do not replace the surface noun's brightness sense","qac_refs":["91:1:2:2","91:1:2:3"],"root":{"arabic":"ض ح و","transliteration":"ḍ-ḥ-w"},"surface":{"arabic":"ضُحَىٰهَا","transliteration":"ḍuḥāhā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["91:1"],"branch_refs":["root_000818/B001","root_000904/B001","root_000904/B005"],"candidate_id":"cand_b35a297c8d16025c277f","evidence_scope":"focus_ayah","hft_ref":"hft_bc9559584107c9e5226f","item_id":"baseline_radiant_extension","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_radiant_extension","support_id":"sup_6f33c65304294242491d"},{"anchor_refs":["91:1"],"branch_refs":["root_000818/B001","root_000904/B002"],"candidate_id":"cand_c897026b9663d7760757","evidence_scope":"focus_ayah","hft_ref":"hft_dae3f14e89c3086e38ec","item_id":"baseline_exposure_event","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exposure_event","support_id":"sup_7c1fd4c677030fea206e"},{"anchor_refs":["91:1"],"branch_refs":["root_000904/B001","root_000904/B006"],"candidate_id":"cand_331b3723f00db064710d","evidence_scope":"focus_ayah","hft_ref":"hft_3ff0325c4e4552697518","item_id":"baseline_measured_ripening","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_measured_ripening","support_id":"sup_e27927c70ff171d708ba"},{"anchor_refs":["91:1"],"branch_refs":["root_000818/B001","root_000904/B003"],"candidate_id":"cand_50df550fde99174493a2","evidence_scope":"focus_ayah","hft_ref":"hft_70c47d2e6e772568b7ec","item_id":"baseline_creaturely_provision","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_creaturely_provision","support_id":"sup_d1be31215508bd62eb34"},{"anchor_refs":["91:1"],"branch_refs":["root_000818/B002","root_000818/B006","root_000904/B002"],"candidate_id":"cand_21dc8ec378d97588871e","evidence_scope":"focus_ayah","hft_ref":"hft_14a4c672089778de2e61","item_id":"baseline_guarded_restiveness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_guarded_restiveness","support_id":"sup_067a3ce17719d86f29bc"}],"diagnostics":[],"lane_counts":{"global":10,"macro":18,"micro":5},"packet_summary":{"ayah_count":15,"focus_ref":"91:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"91:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":23,"unstructured_record_count":0},"identity":{"ayah_ref":"91:1","lane":"micro","linguistic_source_ref":"91:1","surface_ref":"91:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"91:1","target_tokens":[["Güneşe",["91:1:1"]],["ve",["91:1:2"]],["onun",["91:1:2"]],["kuşluk",["91:1:2"]],["aydınlığına",["91:1:2"]]],"text":"Güneşe ve onun kuşluk aydınlığına,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":15,"id":"s091-p01-001-015","label":"Whole surah","number":1,"refs":["91:1","91:2","91:3","91:4","91:5","91:6","91:7","91:8","91:9","91:10","91:11","91:12","91:13","91:14","91:15"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:definite-cosmic-referent","source_type":"word_analysis","support_id":"sup_0503c23eec12fc55267b","text":"{\"blocking_evidence\":null,\"headline\":\"the known sun is invoked\",\"reader_payoff\":\"The reader notices that the ayah invokes the known, singular sun as a shared cosmic witness rather than introducing an indefinite light source.\",\"reason\":\"QAC marks {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) as definite, singular, concrete, and feminine; contextual evidence keeps the local referent in nature-creation usage.\",\"representative_source_ids\":[\"QG-01f7d01f\",\"QF-0eb74c90\",\"MT-209fe587\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:coordination-versus-renewed-oath","source_type":"word_analysis","support_id":"sup_0ed1d6f1511711a1655c","text":"{\"blocking_evidence\":null,\"headline\":\"classical options share oath force\",\"reader_payoff\":\"The reader notices the interpretive choice: the particle can be discussed as coordination or renewed oath force, but either way the brightness remains sworn by.\",\"reason\":\"The local QAC tag favors coordination, while the inherited oath frame preserves the CRITICAL debate as a narrowed apparatus point rather than a replacement parse.\",\"representative_source_ids\":[\"MG-a384e426\",\"QI-e87aab74\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1:oath-genitive-launch","source_type":"word_analysis","support_id":"sup_1118221cc5dc98ce16c8","text":"{\"blocking_evidence\":null,\"headline\":\"opening particle governs the oath object\",\"reader_payoff\":\"The reader notices that the surah opens as sworn testimony because {{ar:وَ}} ({{tr:wa}}) governs {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) as a genitive oath object.\",\"reason\":\"QAC and attachment evidence identify the first {{ar:وَ}} ({{tr:wa}}) as oath particle, with {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) as its genitive complement and an omitted oath performative.\",\"representative_source_ids\":[\"QG-281ab6f4\",\"QG-f6e195e2\",\"MG-b6810f79\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:article-versus-possessive-echo","source_type":"word_analysis","support_id":"sup_15a6f383c41f96a92ce2","text":"{\"blocking_evidence\":null,\"headline\":\"possessed brightness differs from independent brightness\",\"reader_payoff\":\"The reader notices that 91:1 binds brightness to the sun, while 93:1 presents the forenoon brightness independently.\",\"reason\":\"The CRITICAL rows provide the concrete comparison with 93:1, and the local possessive suffix supplies the contrast.\",\"representative_source_ids\":[\"QF-48b10c6c\",\"MI-10f97e17\",\"QE-a3c3541c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:source-product-dependence","source_type":"word_analysis","support_id":"sup_1d5f0354904c199ffae0","text":"{\"blocking_evidence\":null,\"headline\":\"radiance is product, not peer source\",\"reader_payoff\":\"The reader notices the ayah's source-product architecture: the second object is generated manifestation, not a second independent celestial source.\",\"reason\":\"The suffix points back to the sun and the conjoined oath structure pairs source with its manifestation.\",\"representative_source_ids\":[\"QS-1c7f44e5\",\"QI-07a7c5bc\",\"QY-3af8d68c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:next-ayah-pronoun-link","source_type":"word_analysis","support_id":"sup_29ac5520156a70d3d599","text":"{\"blocking_evidence\":null,\"headline\":\"suffix prepares the next pronoun\",\"reader_payoff\":\"The reader notices that the possessive {{tr:hā}} in 91:1 prepares the repeated feminine object pronoun when the moon follows it in 91:2.\",\"reason\":\"The local suffix points back to {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}), and the CRITICAL row supplies the continuation at 91:2.\",\"representative_source_ids\":[\"QB-c4ac7401\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:sacrifice-expenditure-narrowed","source_type":"word_analysis","support_id":"sup_2f732118dcec23b714a7","text":"{\"blocking_evidence\":null,\"headline\":\"sacrifice branch stays secondary\",\"reader_payoff\":\"The reader notices a secondary expenditure coloring in the root family, while the local word still means the sun's brightness and not sacrifice.\",\"reason\":\"V4 includes an Adha-sacrifice branch for {{ar:ض ح و}} ({{tr:ḍ-ḥ-w}}), but the local form is the abstract noun for brightness, so sacrifice colors expenditure only and does not govern translation.\",\"representative_source_ids\":[\"QS-37b47bba\",\"QS-85075a26\",\"QF-b8305f33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:source-to-spread-sound","source_type":"word_analysis","support_id":"sup_3287a8e5190ea093e695","text":"{\"blocking_evidence\":null,\"headline\":\"pacing opens from source to spread\",\"reader_payoff\":\"The reader notices a pacing contrast: the ayah moves from the compact sun word to the more open, extended sound of its brightness.\",\"reason\":\"The CRITICAL sound rows are coherent with the local surface and word order, provided they remain a sound-form payoff rather than semantic proof.\",\"representative_source_ids\":[\"QP-1adb7604\",\"QP-a87323f3\",\"MP-e1463345\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:1:2:2","source_type":"qac_morpheme","support_id":"sup_3a014ae17dd2c28eeadb","text":"{\"lemma_ar\":\"ضُحًى\",\"morph_features\":\"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:1:2:2\",\"qac_word_ref\":\"91:1:2\",\"root_ar\":\"ض ح و\",\"surface_ar\":\"ضُحَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:suffixal-definiteness","source_type":"word_analysis","support_id":"sup_3ad0268a9a3caa9f33d9","text":"{\"blocking_evidence\":null,\"headline\":\"possession makes the noun definite\",\"reader_payoff\":\"The reader notices that definiteness is carried by the attached suffix, not by an article, so the brightness is source-bound inside the word shape.\",\"reason\":\"The local noun is al-less but made definite by the possessive suffix, matching QAC and attachment evidence.\",\"representative_source_ids\":[\"QG-252c3e7a\",\"QF-32a4b94f\",\"QF-667ed83f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:sun-moon-pairing","source_type":"word_analysis","support_id":"sup_4b824d8bc6b0dfc596cf","text":"{\"blocking_evidence\":null,\"headline\":\"the familiar dyad is delayed\",\"reader_payoff\":\"The reader notices that the familiar sun-moon pairing is not completed inside 91:1; it is stretched into the next ayah when the moon follows the feminine sun reference (91:2).\",\"reason\":\"Contextual collocation evidence shows {{ar:ش م س}} ({{tr:sh-m-s}}) commonly paired with the moon root, and the CRITICAL rows give the concrete continuation at 91:2.\",\"representative_source_ids\":[\"QI-5194aeec\",\"MI-935a84ad\",\"QE-e7746238\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:eschatological-sun-contrast","source_type":"word_analysis","support_id":"sup_5b3817eedf942c1d9654","text":"{\"blocking_evidence\":null,\"headline\":\"stable oath sun contrasts collapse\",\"reader_payoff\":\"The reader notices a corpus contrast: 91:1 swears by the sun in full ordered force, while 81:1 imagines the sun folded up.\",\"reason\":\"The CRITICAL row supplies the concrete contrast to 81:1, and nothing in the local evidence contradicts using it as an echo rather than a controlling sense.\",\"representative_source_ids\":[\"QE-46c643be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:cosmic-possessed-brightness-echo","source_type":"word_analysis","support_id":"sup_5ba207705b34a3b65e1b","text":"{\"blocking_evidence\":null,\"headline\":\"possessed brightness has cosmic echo\",\"reader_payoff\":\"The reader notices that the possessed brightness wording participates in a wider cosmic illumination field also visible at 79:29.\",\"reason\":\"The CRITICAL row supplies the concrete echo at 79:29; it survives as an echo field, not a governing local parse.\",\"representative_source_ids\":[\"QE-0e39cf00\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:becoming-and-transition-narrowed","source_type":"word_analysis","support_id":"sup_5ba40b3218c13dc3c22d","text":"{\"blocking_evidence\":null,\"headline\":\"becoming colors the brightness\",\"reader_payoff\":\"The reader notices a transition-into-visibility pressure around the root, while the surface noun still names brightness rather than a verb of becoming.\",\"reason\":\"The CRITICAL Form IV material is useful background for transition, but V4 and QAC show the local word as a noun, so the topic is narrowed to secondary pressure.\",\"representative_source_ids\":[\"QF-b3a2f6d4\",\"MF-2726919f\",\"QI-284cb149\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"91:1:1:3","source_type":"qac_morpheme","support_id":"sup_6a4b69f50313c7cd2dab","text":"{\"lemma_ar\":\"شَمْس\",\"morph_features\":\"STEM|POS:N|LEM:$amos|ROOT:$ms|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"91:1:1:3\",\"qac_word_ref\":\"91:1:1\",\"root_ar\":\"ش م س\",\"surface_ar\":\"شَّمْسِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:possessive-solar-brightness","source_type":"word_analysis","support_id":"sup_6ab2da79f2d15e2ea147","text":"{\"blocking_evidence\":null,\"headline\":\"the brightness belongs to the sun\",\"reader_payoff\":\"The reader notices that {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) is not free-standing morning brightness; the suffix makes it the sun's own radiance.\",\"reason\":\"QAC marks a feminine possessive suffix referring to {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}), and attachment evidence forces the suffix as a possessive genitive linked to the noun.\",\"representative_source_ids\":[\"QG-1a03f604\",\"QG-6749025a\",\"MG-a8c17f2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:rare-root-weight","source_type":"word_analysis","support_id":"sup_7196148cfe136d2ef336","text":"{\"blocking_evidence\":null,\"headline\":\"uncommon root concentrates attention\",\"reader_payoff\":\"The reader notices that this is a marked brightness term from a small Quranic distribution, not the most generic light vocabulary.\",\"reason\":\"Contextual evidence gives a small exact-root/form profile for {{ar:ض ح و}} ({{tr:ḍ-ḥ-w}}), supporting the CRITICAL claim of concentrated lexical weight.\",\"representative_source_ids\":[\"MS-434f2a9c\",\"QI-50439b96\",\"QH-a246fe40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1:connective-oath-sequence","source_type":"word_analysis","support_id":"sup_82f194a308615fa6f271","text":"{\"blocking_evidence\":null,\"headline\":\"one letter launches the oath chain\",\"reader_payoff\":\"The reader notices that the first particle is both oath marker and chain-starter, preparing the repeated oath movement through 91:1-7 and the answer at 91:9.\",\"reason\":\"The local grammar gives oath force, while the CRITICAL rows correctly note that the same visible particle also initiates the linked oath series.\",\"representative_source_ids\":[\"QS-42179e2f\",\"QI-018b5bb4\",\"MT-7d47032c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1","source_type":"word_analysis","support_id":"sup_9332c2b4d543f3d02bfa","text":"{\"gloss_range\":\"opening oath particle that governs the following genitive noun; not ordinary coordination alone\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) begins the surah by putting the listener inside oath grammar before any lexical object appears. The following {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) is genitive under this particle, so the first noun is a sworn-by object, not a subject or a loose cosmic description. The one-letter form also keeps connective energy: it opens a chain of oath clauses that runs through the repeated particles of 91:1-7 and presses toward the oath answer at 91:9. Its matching particle at word 3 has the same surface sound but a continuation role before the possessed brightness, so identical form does not mean identical local attachment. In recitation and script, {{ar:وَٱلشَّمْسِ}} ({{tr:wa-l-shamsi}}) fuses the particle to its witness, while the later ending {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) starts the sound pattern that continues with the next {{tr:-hā}} cadence in 91:2.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3","source_type":"word_analysis","support_id":"sup_955f8195e15bf2ba13c3","text":"{\"gloss_range\":\"coordinating particle that carries the existing oath frame forward to the second oath term\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) is not a fresh, unrelated opening. QAC marks it as coordination, and the attachment evidence joins {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) to {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) as a second oath term. That means the particle both says \\\"and\\\" and carries the qasam force already launched by the first {{ar:وَ}} ({{tr:wa}}); even if discussed as renewed oath force, the brightness still remains sworn by inside the same local frame. The visible proclitic on the second object makes that half enter as a bound continuation, not a separate new sentence. It keeps source and manifestation paired but distinct: the oath moves from the sun itself to what belongs to it. Its repetition also trains the ear for the additive oath chain that continues into 91:2 and through the opening series toward 91:9, while the two short particle onsets balance the two halves of the ayah.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:coordinated-oath-continuation","source_type":"word_analysis","support_id":"sup_9b5f7be50bbaa5c3eb3a","text":"{\"blocking_evidence\":null,\"headline\":\"second particle extends the oath\",\"reader_payoff\":\"The reader notices that the second {{ar:وَ}} ({{tr:wa}}) keeps {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) inside the existing oath frame rather than starting a disconnected clause.\",\"reason\":\"QAC identifies the third word as coordinating {{ar:وَ}} ({{tr:wa}}), and attachment evidence strongly licenses {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) as conjoined to {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) within the oath frame.\",\"representative_source_ids\":[\"QG-5867b19c\",\"QG-685dbf1d\",\"QS-07741ea9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:compressed-sound-texture","source_type":"word_analysis","support_id":"sup_9d18bf378f6d222f6aa3","text":"{\"blocking_evidence\":null,\"headline\":\"dense sound suits the source\",\"reader_payoff\":\"The reader notices that the compact, assimilated sound of {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) gives the source a concentrated acoustic profile before the longer brightness word.\",\"reason\":\"The visible shaddah and compressed definite article support a modest sound-form observation without turning phonetics into lexical sense.\",\"representative_source_ids\":[\"QF-6724b5c8\",\"QP-541844c3\",\"QP-8940f27d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:fused-second-object","source_type":"word_analysis","support_id":"sup_9f84e3ca17ecc8ca6bf8","text":"{\"blocking_evidence\":null,\"headline\":\"second half enters bound\",\"reader_payoff\":\"The reader notices that {{ar:وَضُحَىٰهَا}} ({{tr:wa-ḍuḥāhā}}) enters as a bound continuation, not as a visually separate new sentence.\",\"reason\":\"The visible proclitic particle on {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) matches the conjoined second oath term.\",\"representative_source_ids\":[\"QF-e529c89b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:balanced-short-onsets","source_type":"word_analysis","support_id":"sup_a0238db1fe509b78ef86","text":"{\"blocking_evidence\":null,\"headline\":\"two short onsets balance the pair\",\"reader_payoff\":\"The reader notices the audible balance created when both halves of the ayah begin with the same compact particle sound.\",\"reason\":\"The repeated surface form supports a modest phonetic observation that reinforces the paired oath objects.\",\"representative_source_ids\":[\"QP-2aa294f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:repeated-wa-refrain","source_type":"word_analysis","support_id":"sup_a0c3a685200d1c1ab1e4","text":"{\"blocking_evidence\":null,\"headline\":\"repetition prepares the oath series\",\"reader_payoff\":\"The reader notices that the repeated {{ar:وَ}} ({{tr:wa}}) inside 91:1 establishes an additive rhythm that carries into the next oath link (91:2) and toward the answer (91:9).\",\"reason\":\"The second particle echoes the first while changing local role from opener to continuation, and the CRITICAL rows supply the concrete series references.\",\"representative_source_ids\":[\"MT-1ad34889\",\"QE-28eedfe0\",\"QB-fefffc72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:genitive-oath-object","source_type":"word_analysis","support_id":"sup_a172553912fea993f0c6","text":"{\"blocking_evidence\":null,\"headline\":\"genitive case makes witness role\",\"reader_payoff\":\"The reader notices that the sun's case is functional: it is grammatically made the sworn-by object under the opening particle.\",\"reason\":\"The attachment evidence syntactically forces {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) as the genitive complement of the oath particle.\",\"representative_source_ids\":[\"QG-4ccce397\",\"QG-72be0b31\",\"MG-b012777e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:source-emitter-frame","source_type":"word_analysis","support_id":"sup_a9567beafcfc993fced6","text":"{\"blocking_evidence\":null,\"headline\":\"stellar-source language supports the pair\",\"reader_payoff\":\"The reader notices the source-side direction of the image: the ayah names the sun as emitter, not a creature basking or an action of sunning.\",\"reason\":\"The CRITICAL rows' emitter language fits the source-product pair, but it is narrowed because the surface is a noun for the sun, not verbal basking or exposing forms.\",\"representative_source_ids\":[\"QS-6bf0ded6\",\"QS-a5e65fb6\",\"QF-8c82c900\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:radiation-output-narrowed","source_type":"word_analysis","support_id":"sup_ad66359bfbb17707ca10","text":"{\"blocking_evidence\":null,\"headline\":\"emitted field sharpens brightness\",\"reader_payoff\":\"The reader notices brightness as an emitted field that discloses surfaces, while the local wording remains classical forenoon radiance rather than a technical physics term.\",\"reason\":\"The output-field reading fits the source-bound possessive and exposure branch, but it is narrowed so modern radiation language does not replace the local forenoon-brightness sense.\",\"representative_source_ids\":[\"QS-17f5a09a\",\"QS-bb83e67d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:forenoon-exposure-field","source_type":"word_analysis","support_id":"sup_bfca8b67352531f4dc72","text":"{\"blocking_evidence\":null,\"headline\":\"forenoon light makes visible\",\"reader_payoff\":\"The reader notices that the word selects forenoon brightness and exposed clarity rather than a generic term for light.\",\"reason\":\"V4's accepted branches for {{ar:ض ح و}} ({{tr:ḍ-ḥ-w}}) include forenoon daylight and open exposure, supporting the CRITICAL payoff of time-bound manifested brightness.\",\"representative_source_ids\":[\"QS-12545fb3\",\"QS-7b319da0\",\"QS-fdac30b9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1:fused-opening-surface","source_type":"word_analysis","support_id":"sup_c401b86da99dc83ff7cc","text":"{\"blocking_evidence\":null,\"headline\":\"particle and sun sound as one unit\",\"reader_payoff\":\"The reader notices that the opening oath is not a detached preface; the particle is visibly and audibly bound to the sun noun.\",\"reason\":\"The surface sequence {{ar:وَٱلشَّمْسِ}} ({{tr:wa-l-shamsi}}) matches the licensed particle-complement relation, with recitational compression into the following definite noun.\",\"representative_source_ids\":[\"QF-da263d32\",\"QP-d2c89ee3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:feminine-source-product-link","source_type":"word_analysis","support_id":"sup_c5fd81bd0642e5579288","text":"{\"blocking_evidence\":null,\"headline\":\"sun becomes antecedent and source\",\"reader_payoff\":\"The reader notices that the sun is not only sworn by; it also becomes the feminine source to which the following brightness belongs.\",\"reason\":\"The feminine noun {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) licenses the possessive suffix in {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}), and the conjoined structure preserves the source-before-product order.\",\"representative_source_ids\":[\"QG-c5f55b89\",\"QS-e5f680be\",\"QT-777acfc6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4","source_type":"word_analysis","support_id":"sup_cf6bed21af59261f4a61","text":"{\"gloss_range\":\"the sun's own forenoon brightness and exposed radiance, made definite by the feminine possessive suffix\",\"prose\":\"{{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) closes the ayah on the sun's own brightness. The noun lacks an article, but the suffix {{tr:hā}} makes it definite by possession and routes it back to {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}), so the second oath term is not generic forenoon light floating beside the sun. It is the sun's manifestation: a forenoon/exposure field in which light makes things visible, and emitted-field language can sharpen that disclosure without turning the word into a technical physics term. The local surface keeps brightness primary; non-surface becoming forms add transition into manifest brightness, while sacrifice-related derivatives add offering-like expenditure without changing the translation target. The small Quranic distribution makes this brightness term marked rather than routine generic light vocabulary. The possessive form also matters intertextually: 93:1 has independently definite forenoon brightness, while 91:1 binds it to the sun, and 79:29 shares possessed brightness language in a cosmic illumination setting. As the final word, {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}) lets the ayah land not on the solar body itself but on its spreading radiance, with the long open ending preparing the next {{tr:-hā}} cadence and repeated feminine-pronoun motion in 91:2. After the compact sun word, its own pacing opens from emphatic onset into airy, long-vowel spread.\",\"root_display\":\"{{ar:ض ح و}} ({{tr:ḍ-ḥ-w}})\",\"root_gloss_range\":\"forenoon daylight and exposed visibility are locally central; becoming and sacrificial/expenditure branches provide narrowed secondary pressure but do not replace the surface noun's brightness sense\",\"surface_display\":\"{{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2","source_type":"word_analysis","support_id":"sup_e09f5cf995434734e07e","text":"{\"gloss_range\":\"the definite, concrete sun as sworn object and source of the following possessed brightness\",\"prose\":\"{{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) is the first lexical object of the surah: definite, singular, concrete, and genitive under the oath particle. Its article treats the sun as a shared cosmic referent, not a newly introduced object, while its case makes it the sworn-by witness. The noun also has forward work to do. As a feminine noun, it supplies the antecedent for the suffix in {{ar:ضُحَىٰهَا}} ({{tr:ḍuḥāhā}}), so the ayah first names the source and then its owned radiance; 91:2 continues that feminine reference when the moon follows it. The root field can add heat, exposure, and an untamable-force coloring, but the local form keeps the sense anchored in the physical sun, not in unrelated root branches. The source-side frame is emitter rather than a creature basking or an action of sunning, which protects the source-to-product direction of the pair. The familiar sun-moon pairing is stretched across the ayah boundary into 91:2, and the stable sun invoked here also contrasts with the sun's collapse at 81:1. Its assimilated, consonant-dense sound is compact before the longer brightness word, matching the movement from concentrated source to manifestation.\",\"root_display\":\"{{ar:ش م س}} ({{tr:sh-m-s}})\",\"root_gloss_range\":\"sun and daylight are locally active; wider root branches such as restive force, hostility, names, and withholding remain background unless they sharpen exposure or force without replacing the sun\",\"surface_display\":\"{{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:case-role-and-oath-term","source_type":"word_analysis","support_id":"sup_e3d53995080a268f67cf","text":"{\"blocking_evidence\":null,\"headline\":\"role options stay under possession\",\"reader_payoff\":\"The reader notices that the word is both a possessed solar quality and a coordinated oath term, while local evidence prevents it from becoming an independent, generic time-word.\",\"reason\":\"QAC allows accusative/genitive ambiguity, but attachment evidence strongly licenses coordination with {{ar:ٱلشَّمْسِ}} ({{tr:al-shamsi}}) and syntactically forces the possessive suffix, so descriptive or independent readings are kept as narrowed nuance.\",\"representative_source_ids\":[\"QG-47b210c1\",\"QG-6e2ee5dc\",\"QG-6eeb7f92\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1:cross-ayah-sound-chain","source_type":"word_analysis","support_id":"sup_e7ea3eccb6547a7906a7","text":"{\"blocking_evidence\":null,\"headline\":\"opening prepares the later refrain\",\"reader_payoff\":\"The reader notices that the first particle starts a formal chain whose sound and oath pattern continue immediately into 91:2.\",\"reason\":\"The ayah begins particle-first in oath mode, closes with the {{tr:-hā}} cadence, and the next ayah continues the particle-plus-oath pattern (91:2).\",\"representative_source_ids\":[\"QT-324ac06b\",\"QT-6d6cbc04\",\"QP-6780ee57\",\"QB-957bef95\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:4:closure-and-open-cadence","source_type":"word_analysis","support_id":"sup_efabee209de18a519f6c","text":"{\"blocking_evidence\":null,\"headline\":\"radiance becomes the ayah landing\",\"reader_payoff\":\"The reader notices that the ayah lands on spreading radiance, with an open {{tr:-āhā}} cadence rather than ending on the compact sun noun.\",\"reason\":\"The final word position and long-vowel-plus-suffix surface support the closure and cadence observation.\",\"representative_source_ids\":[\"QT-bafee701\",\"QF-f8b0ce75\",\"QP-d47464de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:1:role-contrast-with-second-wa","source_type":"word_analysis","support_id":"sup_fa2542943e395d94eee1","text":"{\"blocking_evidence\":null,\"headline\":\"same particle form changes role\",\"reader_payoff\":\"The reader notices that the two occurrences of {{ar:وَ}} ({{tr:wa}}) sound alike but do different local work: the first opens the oath, while the second continues it.\",\"reason\":\"QAC distinguishes the first particle as oath particle and the third word as coordinating particle, preserving the CRITICAL contrast between identical form and different attachment roles.\",\"representative_source_ids\":[\"QF-831d1b1e\",\"QE-a70fe185\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:concrete-sun-over-generic-radiance","source_type":"word_analysis","support_id":"sup_fc2d2b5d54f024b2f885","text":"{\"blocking_evidence\":null,\"headline\":\"source and radiance stay distinct\",\"reader_payoff\":\"The reader notices that the first noun names the concrete solar body, while the next term names its manifestation, so the pair does not collapse into generic light.\",\"reason\":\"The local form is a concrete noun and V4's active branch for {{ar:ش م س}} ({{tr:sh-m-s}}) includes sun and daylight, while the following possessed noun separately carries the radiance term.\",\"representative_source_ids\":[\"QS-7692a71e\",\"QS-d3dc7046\",\"QT-e4e57565\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:2:root-force-exposure-narrowed","source_type":"word_analysis","support_id":"sup_fe9dd87437fe840ed0fb","text":"{\"blocking_evidence\":null,\"headline\":\"root field adds force but not a new sense\",\"reader_payoff\":\"The reader notices that the sun is felt as a force of heat and exposure, while the local noun keeps that pressure subordinate to the literal solar body.\",\"reason\":\"V4 confirms broad {{ar:ش م س}} ({{tr:sh-m-s}}) branches including sun/daylight and restive force, but QAC and contextual evidence keep the local surface as the concrete sun, so the extra force is a narrowed coloring.\",\"representative_source_ids\":[\"QS-3f0d6677\",\"QS-6c41688a\",\"MS-68ebcea0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"91:1:3:source-manifestation-pivot","source_type":"word_analysis","support_id":"sup_feac70d1140c186d906d","text":"{\"blocking_evidence\":null,\"headline\":\"the connector prevents collapse\",\"reader_payoff\":\"The reader notices that the connector keeps the sun and its brightness as paired oath objects, not as one noun plus a mere explanatory gloss.\",\"reason\":\"The conjoined relation and source-before-product order support the CRITICAL claim that word 3 pivots from cosmic body to possessed manifestation.\",\"representative_source_ids\":[\"QS-f04de8e2\",\"QT-81e6b313\",\"QT-a0486ca2\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000818/B001","root_000904/B001","root_000904/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000818","role":"The literal sun and its radiating daylight supply the source from which the focus mechanism extends.","root":"ش م س","source_ref":"91:1","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000904","role":"The rising, extended forenoon supplies duration and turns the sun's light into an unfolding interval.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000904","role":"Clear ḍuḥā brightness supplies the qualitative clarity carried through that interval.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"changed_reading":{"after":"An oath by a luminous source and by the temporal-spatial unfolding of its clear reach.","before":"An oath by the sun followed by an ordinary time of morning."},"confidence":"strong","focus_anchor":"The construct-like pairing of the sun with its ḍuḥā joins a luminous body to a phase or reach attributed to it.","mechanism":"The sun supplies the radiating source, while ḍuḥā supplies brightness extended across a rising interval. The focus therefore presents illumination as an unfolding reach rather than a static object.","model_id":"baseline_radiant_extension"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_radiant_extension","source_type":"hft","support_id":"sup_6f33c65304294242491d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000818/B001","root_000904/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000818","role":"Solar light supplies the physical agent of manifestation.","root":"ش م س","source_ref":"91:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000904","role":"Exposure to heat, outward prominence, and public visibility supply the manifested field produced by the sun.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"changed_reading":{"after":"The verse names a source together with its act of placing a field openly under light and heat.","before":"The verse names a bright celestial object and its time of day."},"confidence":"strong","focus_anchor":"Ḍuḥāhā can name not only when the sun shines but the sun's making-visible, heat-bearing exposure.","mechanism":"Radiance moves outward until bodies and actions occupy an exposed, public surface. The paired terms thus describe an event of manifestation: a source brings what is outside into visibility.","model_id":"baseline_exposure_event"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exposure_event","source_type":"hft","support_id":"sup_7c1fd4c677030fea206e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B001","root_000904/B006"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000904","role":"The forenoon's rising extension supplies a process that takes time to reach fullness.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000904","role":"Gentle delay supplies the pacing rule by which the illumination unfolds without haste.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"changed_reading":{"after":"Ḍuḥā is a measured maturation of visibility, with delay functioning as part of how clarity forms.","before":"Ḍuḥā is a point on a clock."},"confidence":"medium","focus_anchor":"The temporal branches of ḍuḥā include both the day's gradual extension and an idiom of slowing or not rushing.","mechanism":"The light reaches fullness by measured continuation. This allows the focus to carry a tempo: manifestation ripens through delay rather than arriving as an instantaneous flash.","model_id":"baseline_measured_ripening"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_measured_ripening","source_type":"hft","support_id":"sup_e27927c70ff171d708ba","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000818/B001","root_000904/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000818","role":"Daylight supplies the environmental condition in which the provision interval operates.","root":"ش م س","source_ref":"91:1","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000904","role":"Forenoon feeding and early grazing supply the creaturely use that makes the interval materially consequential.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"changed_reading":{"after":"The sun's ḍuḥā is a usable life interval in which creatures feed, graze, and receive provision.","before":"The sun's ḍuḥā is abstract brightness."},"confidence":"medium","focus_anchor":"A focus branch places the ḍuḥā interval around early grazing and a sustaining meal.","mechanism":"The sunlight interval organizes embodied access to food rather than merely illuminating scenery. The possessive pairing can therefore be heard as the sun's creature-serving turn or usable allotment.","model_id":"baseline_creaturely_provision"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_creaturely_provision","source_type":"hft","support_id":"sup_d1be31215508bd62eb34","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلشَّمْسِ وَضُحَىٰهَا","ayah_ref":"91:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000818/B002","root_000818/B006","root_000904/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000818","role":"Restive refusal supplies a force that will not settle or submit to being ridden.","root":"ش م س","source_ref":"91:1","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_000818","role":"Guarding and withholding supply the protected interior or reserve carried by that force.","root":"ش م س","source_ref":"91:1","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000904","role":"Open prominence supplies the contrary motion by which the guarded or unruly force becomes visible.","root":"ض ح و","source_ref":"91:1","source_word_indices":["2"]}],"changed_reading":{"after":"The sun is also a difficult, guarded power whose outward exposure makes its force impossible to keep private.","before":"The sun is a serene emblem of regular brightness."},"confidence":"exploratory","focus_anchor":"Distant branches within the focus root inventory place restive refusal and protective withholding inside the lexical field of the sun, while ḍuḥā places effects in the open.","mechanism":"A force that resists capture or guards what lies behind it nevertheless becomes publicly manifest through its ḍuḥā. This yields a tense rather than placid solar image: withheld power declares itself by exposure.","model_id":"baseline_guarded_restiveness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_guarded_restiveness","source_type":"hft","support_id":"sup_067a3ce17719d86f29bc","trust":"legacy_unbound"}]}
</lane_packet_json>
