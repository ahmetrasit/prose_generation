# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **106:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s106-regular-20260911/s106/106_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "106:1",
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
{"analysis_context":{"analysis_id":"s106-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"106:1","host_surah":106,"lane_context_refs":[],"ordered_context_refs":["106:0","106:2","106:3","106:4","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Anlam sayı alanıyla sınırlıdır; yakınlık, alıştırma, nesneleri birleştirme veya alfabe işareti anlamı buraya taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000045/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"bin sayısı ve bine tamamlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel çekirdek, bilinen bin sayısının kendisi ve onun çoğul adlarıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir grup veya miktar eksikken onu bin sayısına tamamlamak aynı sayısal çekirdeğe bağlıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Para gibi sayılabilir varlıklarda toplamın bin değerine varması özel bir uygulamadır."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sayı adını hem de sayılabilir bir bütünün bin değerine ulaştırılmasını kapsayan en kısa doğal karşılıktır.","boundary_detail":"Anlam sayı alanıyla sınırlıdır; yakınlık, alıştırma, nesneleri birleştirme veya alfabe işareti anlamı buraya taşınmaz.","branch_image_ar":"الألف واجتماع المئين","concept_gloss":"bin sayısı ve bine tamamlama","contextual_glosses":[{"applicability":"Sadece yalın sayı adı bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir topluluğu veya miktarı bine ulaştırma işlemini dışarıda bırakır.","preserves":"Bilinen bin sayısı korunur."},"facet_ids":["F001"],"text":"bin","usage_role":"general"},{"applicability":"Topluluk, para veya başka bir sayılabilir şeyin bin değerine çıkarıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eksik bir sayılabilir bütünün bin değerine ulaştırılması korunur."},"facet_ids":["F002","F003"],"text":"bine tamamlamak","usage_role":"contextual"}],"definition":"Bir şeyin sayısal değerinin bin olması ya da bir topluluğun, para miktarının veya benzeri sayılabilir bir bütünün bine ulaştırılmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel çekirdek, bilinen bin sayısının kendisi ve onun çoğul adlarıdır."},{"facet_id":"F002","role":"extension","statement":"Bir grup veya miktar eksikken onu bin sayısına tamamlamak aynı sayısal çekirdeğe bağlıdır."},{"facet_id":"F003","role":"extension","statement":"Para gibi sayılabilir varlıklarda toplamın bin değerine varması özel bir uygulamadır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Alışkanlık ve yakınlık anlamı ekler.","collision":"Kökün başka bir dalındaki yakınlık anlamıyla karışır.","fit":"displacement","loses":"Bin sayısı ve sayısal tamamlama çekirdeğini kaybeder.","preserves":"Bir şeye yöneltme fikrinden çok zayıf bir iz taşıyabilir."},"text":"alıştırmak"}],"identity_rationale":"Kaynak ifadesi hem bilinen bin sayısını hem de insan, para gibi sayılabilir şeylerin bine ulaştırılması ya da bin olması kullanımını birlikte verir. Geçici çerçeve, bu sayısal çekirdeği ve ona bağlı tamamlama kullanımını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilinen bin sayısı; çoğulu binler"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir topluluğu bin kişiye tamamlamak veya onların bin kişi olması"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"para miktarını bin değerine ulaştırmak"}],"lexicalization_note":"Çıplak sayı adı ile belirli tamamlama kalıpları birlikte bulunur; tanım sayı çekirdeğini korur ve kalıp kullanımlarını ona bağlı gösterir.","neighbor_coverage_note":"Komşular sayı, sayma, birleştirme, yakınlık ve alfabe alanlarına göre tarandı; en açıklayıcı sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yerine geçebilirlik yalnızca yapı düzeyindedir; odak dalın sayısal eşiği bin, komşunun eşiği yüzdür.","focus_only":"Odak dal bin sayısını ve bine tamamlama kullanımını kapsar.","gloss":"bin ile yüz ayrımı","neighbor_only":"Komşu dal yüz sayısını ve yüze ulaştırmayı kapsar.","neighbor_ref":"root_001394/B002","relation_type":"near_synonym","shared_zone":"İkisi de belirli bir sayı adı ve bir miktarı o sayıya çıkarma alanındadır."},{"boundary_match":"field_only","distinction":"Odak belirli bir sayısal değerdir; komşu, değer ne olursa olsun sayma veya hesaplama işlemidir.","focus_only":"Odak dal belirli bin değerini adlandırır veya ona ulaştırır.","gloss":"belirli sayı ile sayma","neighbor_only":"Komşu dal sayma, hesaplama ve sayılabilirliği genel süreç olarak ele alır.","neighbor_ref":"root_000989/B001","relation_type":"same_field","shared_zone":"İkisi de sayı ve miktar alanında buluşur."},{"boundary_match":"field_only","distinction":"B001'de bütünün sınırı bin sayısıdır; B002'de sayı eşiği yoktur, parça ve ilişki düzenlemesi esastır.","focus_only":"Odak dalın ölçütü bin değeridir.","gloss":"sayı ile birleştirme","neighbor_only":"Komşu dal farklı parçaları birleştirme ve düzenleme çekirdeğine sahiptir.","neighbor_ref":"root_000045/B002","relation_type":"same_field","shared_zone":"İkisinde de bir bütün oluşturma fikri görülebilir."},{"boundary_match":"field_only","distinction":"B001 matematiksel sayıyı ve sayıya tamamlama işlemini verir; B005 kişiler, yerler veya canlılarla kurulan alışılmış yakınlığı verir.","focus_only":"Odak dal sayısal bin anlamındadır.","gloss":"bin ile alışkanlık","neighbor_only":"Komşu dal yakınlık, alışma, ünsiyet ve bir yerde durma anlamındadır.","neighbor_ref":"root_000045/B005","relation_type":"same_field","shared_zone":"Aynı kök ailesinde yer alırlar."},{"boundary_match":"field_only","distinction":"B001 niceliği gösterir; B006 yazı ve ses düzenindeki bir işareti gösterir.","focus_only":"Odak dal sayı adıdır.","gloss":"sayı ile alfabe işareti","neighbor_only":"Komşu dal alfabe işareti adıdır.","neighbor_ref":"root_000045/B006","relation_type":"same_field","shared_zone":"İkisi de aynı sesli biçimle anılan teknik adlardır."}],"source_phrase_ar":"الألف معروف والجمع الآلاف (maqayis)؛ الألف عدد والجمع ألوف وآلاف (sihah)؛ والألف من العدد معروف (tahdhib)؛ الألف العدد المخصوص (mufradat)؛ آلفت القوم صيرتهم ألفا (maqayis;sihah)؛ آلفت الدراهم أي بلغت بها الألف (mufradat)","source_summary":"Kaynaklar ortak biçimde bin sayısını esas alır; ayrıca insan topluluğu veya para gibi sayılabilir şeylerin bu sayıya çıkarılması aynı dala bağlanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"العدد ألف وجمعه آلاف وألوف؛ وبلوغ القوم أو الدراهم أو غيرها ألفا","what_is_not_ar":"ليس الألفة ولا تأليف القلوب ولا حرف الألف"},"support_links":[]},{"boundary":"Bu dal parça ve ilişki düzenleme alanındadır; bin sayısı, kalpleri kazanma veya yalın alışkanlık anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000045/B002","candidate_links":[{"candidate_id":"cand_d1af02360b5fac473e3a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"birleştirip düzenlemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir şeyi başka bir şeye katma ve parçaları birbirine bağlamadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrılmış kimseler veya şeyler arasında yeniden birlik kurmak özel bir gerçekleşmedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Farklı parçaları düzenli bir sıraya koyarak bir eser veya bütün oluşturmak bu çekirdeğin düzenleme yönüdür."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaları bağlama, ayrılığı giderme ve düzenli bir bütün kurma çekirdeğini birlikte taşıyan genel karşılıktır.","boundary_detail":"Bu dal parça ve ilişki düzenleme alanındadır; bin sayısı, kalpleri kazanma veya yalın alışkanlık anlamı değildir.","branch_image_ar":"ضم الشيء إلى الشيء والتأليف","concept_gloss":"birleştirip düzenlemek","contextual_glosses":[{"applicability":"Ayrı kişiler veya şeyler arasında birlik kurulması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçaları bağlama ve düzenli eser haline getirme yönlerini eksiltir.","preserves":"Ayrı öğeleri bir araya toplama fikri korunur."},"facet_ids":["F002"],"text":"bir araya getirmek","usage_role":"contextual"},{"applicability":"Kitap veya düzenli bütün oluşturma bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bağlama ve iki şey arasında birlik kurma yönünü dışarıda bırakır.","preserves":"Farklı parçaları seçip düzenli bir bütün haline getirme yönü korunur."},"facet_ids":["F003"],"text":"derlemek","usage_role":"contextual"}],"definition":"Ayrı veya farklı parçaları birbirine katıp bağlayarak uyumlu ve düzenli bir bütün haline getirmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir şeyi başka bir şeye katma ve parçaları birbirine bağlamadır."},{"facet_id":"F002","role":"specialization","statement":"Ayrılmış kimseler veya şeyler arasında yeniden birlik kurmak özel bir gerçekleşmedir."},{"facet_id":"F003","role":"extension","statement":"Farklı parçaları düzenli bir sıraya koyarak bir eser veya bütün oluşturmak bu çekirdeğin düzenleme yönüdür."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçaları bağlama, uyum sağlama ve düzenleme işlemini zayıflatır.","preserves":"Dağınık şeyleri bir araya getirme yönünü korur."},"text":"toplamak"}],"identity_rationale":"Kaynak ifadesi şeyleri birbirine katma, ayrıyken toplama, parçaları bağlama ve farklı parçaları düzenli bir bütün haline getirme çekirdeğini açıkça verir. Geçici çerçeve bu çekirdeği kitap düzenleme örneğiyle birlikte ama ona indirgemeden taşır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyin parçalarını birbirine katmak veya bağlamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iki şeyin arasını birleştirmek veya ayrılıktan sonra toplamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"farklı parçalardan düzenlenmiş bütün"}],"lexicalization_note":"Çıplak biçim ve belirli iki şey arasında kurulan kalıp birlikte bulunur; tanım ikisini parçaları bağlama çekirdeğinde ayırarak kapsar.","neighbor_coverage_note":"Adaylar bağlantı, toplama, inşa, parça ve kök içi yakın dallar açısından değerlendirildi; anlam sınırını en çok keskinleştirenler seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda parçaların düzeni ve uyumu önemlidir; komşuda bağlantı veya temas kurma çekirdeği daha geneldir.","focus_only":"Odak dal farklı parçaların düzenli ve uyumlu bütün haline getirilmesini kapsar.","gloss":"düzenli birleştirme ile temas","neighbor_only":"Komşu dal bir şeyi başka bir şeye iliştirip temas veya bağlantı kurmayı öne çıkarır.","neighbor_ref":"root_001655/B001","relation_type":"near_synonym","shared_zone":"İkisi de bağlantı ve birleşme alanında örtüşür."},{"boundary_match":"partial","distinction":"Her toplama düzenli bir bütün kurmaz; odak dalın ayırıcı yanı ilişki ve tertip kurmasıdır.","focus_only":"Odak dal bağlama, düzenleme ve parçaları uyumlu kılma işlemini taşır.","gloss":"düzenlemek ile toplamak","neighbor_only":"Komşu dal farklı yönlerden toplama ve yığılma fikrini taşır.","neighbor_ref":"root_001216/B001","relation_type":"near_neighbor","shared_zone":"İkisi de dağınık şeylerin bir araya gelmesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dalın kapsamı eser oluşturma ve düzenlemeye açılır; komşu dal onarım ve yarığı kapatma durumuna daha bağlıdır.","focus_only":"Odak dal farklı parçaların düzenli bir bütün haline getirilmesini de kapsar.","gloss":"birleştirme ile onarma","neighbor_only":"Komşu dal çatlak veya ayrılmış şeyi onarma ve yeniden kaynaştırma yönünü öne çıkarır.","neighbor_ref":"root_000797/B002","relation_type":"near_synonym","shared_zone":"İkisinde de ayrılmış şeylerin tekrar bir araya gelmesi vardır."},{"boundary_match":"field_only","distinction":"B002'de bütünün niteliği parça ilişkilerinden gelir; B001'de belirleyici sınır sayısal bin değeridir.","focus_only":"Odak dal parçaları veya kişileri bağlayıp düzenler.","gloss":"birleştirme ile bin","neighbor_only":"Komşu dal bin sayısını ve bine ulaşmayı belirtir.","neighbor_ref":"root_000045/B001","relation_type":"same_field","shared_zone":"İkisi de bir bütün oluşması fikrinde gevşekçe buluşur."},{"boundary_match":"partial","distinction":"B002 dışsal bir düzenleme ve birleştirme yapar; B005 içsel alışma ve yakınlık durumunu belirtir.","focus_only":"Odak dal nesneleri veya kişileri birbirine bağlama işlemidir.","gloss":"bağlama ile yakınlık","neighbor_only":"Komşu dal alışma, yakınlık ve bir şeye ünsiyet duymadır.","neighbor_ref":"root_000045/B005","relation_type":"near_neighbor","shared_zone":"İkisinde de ayrılığın azalması veya yakınlık kurulması görülebilir."}],"source_phrase_ar":"انضمام الشيء إلى الشيء (maqayis)؛ كل شيء ضممت بعضه إلى بعض فقد ألفته تأليفا (maqayis)؛ ألفت بين الشيئين تأليفا (sihah)؛ ألفت بينهم تأليفا إذا جمعت بينهم بعد تفرق (tahdhib)؛ ألفت الشيء وصلت بعضه ببعض ومنه تأليف الكتب (tahdhib)؛ اجتماع مع التئام (mufradat)؛ المؤلف ما جمع من أجزاء مختلفة ورتب ترتيبا (mufradat)","source_summary":"Kaynaklar, dağınık veya farklı parçaların birbirine katılması, bağlanması ve düzenli bir bütün haline getirilmesi üzerinde birleşir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"ضم بعض الأشياء إلى بعض؛ الجمع بعد تفرق؛ وصل الشيء؛ تأليف الكتب؛ ترتيب الأجزاء المختلفة","what_is_not_ar":"ليس العدد ألفا ولا الإيلاف الخاص بقريش ولا تألف القلوب بالمال"},"support_links":["sup_4c89e808b11e1e9ab1b0"]},{"boundary":"Anlam, kişilerin gönlünü kazanma çabasıdır; sıradan nesne birleştirme, sayı veya yerleşik alışkanlık anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000045/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"gönlünü kazanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel çekirdek, kişilerin gönlünü yakın davranışla kazanma çabasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Maddi destek veya pay verme, bu kazanma çabasının özel bir aracıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gözetme ve ilgilenme, aynı amaçla kurulan yakınlaştırıcı ilişkiyi açıklar."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yakınlık, gözetme ve destekle bir kişiyi veya grubu kendine ısındırma bağlamını doğal biçimde verir.","boundary_detail":"Anlam, kişilerin gönlünü kazanma çabasıdır; sıradan nesne birleştirme, sayı veya yerleşik alışkanlık anlamı değildir.","branch_image_ar":"تأليف القلوب بالمقاربة والعطاء","concept_gloss":"gönlünü kazanmak","contextual_glosses":[{"applicability":"Kişiyi bir topluluğa veya yöne ısındırma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Destek verme ve gözetme araçlarını açıkça söylemez.","preserves":"Yakınlık kurma ve yönlendirme amacı korunur."},"facet_ids":["F001"],"text":"yakınlaştırmak","usage_role":"contextual"},{"applicability":"Maddi destek veya pay verme aracının vurgulandığı kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazanma amacı ile destek verme aracı birlikte korunur."},"facet_ids":["F001","F002"],"text":"destekle kazanmak","usage_role":"explanatory"}],"definition":"Bir kişiyi veya grubu yakınlık göstererek, gözeterek ya da destek vererek bir tarafa ısındırıp kazanma çabasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel çekirdek, kişilerin gönlünü yakın davranışla kazanma çabasıdır."},{"facet_id":"F002","role":"specialization","statement":"Maddi destek veya pay verme, bu kazanma çabasının özel bir aracıdır."},{"facet_id":"F003","role":"associated_use","statement":"Gözetme ve ilgilenme, aynı amaçla kurulan yakınlaştırıcı ilişkiyi açıklar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Karşılıksız duygu anlamı ekler.","collision":null,"fit":"broadening","loses":"Bilinçli kazanma, gözetme ve destek verme işlemini kaybeder.","preserves":"Olumlu yakınlık fikrini zayıf biçimde korur."},"text":"sevmek"}],"identity_rationale":"Kaynak ifadesi belirli kimselerin yakın ilgi, gözetme ve maddi destekle kazanılmasını anlatır. Geçici çerçeve bu özel sosyal ve dini bağlamı, genel nesne birleştirme anlamına indirgemeden doğru tutar.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"gönülleri yakınlık ve destekle kazanılmaya çalışılan kimseler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birini yakınlık, ilgi veya destekle kazanmak"}],"lexicalization_note":"Belirli adlaşmış ifade ve kişiyle kurulan kalıp birlikte bulunur; tanım bu sosyal kazanma bağlamıyla sınırlıdır.","neighbor_coverage_note":"Dış adayların çoğu ayrılma veya beden alanındadır; kök içi dallar bu özel sosyal anlamı açıklamak için yeterli ve daha keskindir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B003 sosyal ikna ve kazanma amacına bağlıdır; B002 daha genel bir bağlama ve düzenleme işlemidir.","focus_only":"Odak dal kişiyi yakınlık ve destekle kazanma amacına bağlıdır.","gloss":"gönül kazanma ile birleştirme","neighbor_only":"Komşu dal parçaları veya kişiler arasında birlik kurma ve düzenleme işlemidir.","neighbor_ref":"root_000045/B002","relation_type":"near_neighbor","shared_zone":"İkisinde de ayrılığı azaltma ve yakınlaştırma görülebilir."},{"boundary_match":"partial","distinction":"B003 amaçlı ve çoğu kez destekli bir kazanma sürecidir; B005 oluşmuş alışkanlık veya yakınlık halidir.","focus_only":"Odak dal başkasının gönlünü kazanmak için uygulanan yakınlaştırıcı eylemdir.","gloss":"kazanma ile alışma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışma ve onunla ünsiyet durumudur.","neighbor_ref":"root_000045/B005","relation_type":"near_neighbor","shared_zone":"İkisi de kişiler arasında yakınlık ve ünsiyet alanına dokunur."},{"boundary_match":"field_only","distinction":"B003 kişilerle kurulan etki ilişkisini açıklar; B001 tamamen sayısal bir anlam taşır.","focus_only":"Odak dal sosyal yakınlaştırmadır.","gloss":"gönül kazanma ile sayı","neighbor_only":"Komşu dal bin sayısı ve bine ulaştırmadır.","neighbor_ref":"root_000045/B001","relation_type":"other","shared_zone":"Ortaklık yalnızca aynı kök ailesinde bulunmalarıdır."}],"source_phrase_ar":"تألفته على الإسلام ومنه المؤلفة قلوبهم (sihah)؛ والمؤلفة قلوبهم هؤلاء قوم من سادة العرب أمر الله نبيه بتألفهم أي بمقاربتهم وإعطائهم من الصدقات (tahdhib)؛ والمؤلفة قلوبهم هم الذين يتحرى فيهم بتفقدهم (mufradat)","source_summary":"Kaynaklar, bazı kimselerin yakınlık, gözetme ve verilen destek yoluyla kazanılması fikrinde birleşir; anlam, genel sevgi değil bilinçli yakınlaştırma eylemidir.","sources":["SI","TA","MU"],"what_is_ar":"تألف القلوب؛ المقاربة والعطاء لاستمالة القوم؛ المؤلفة قلوبهم","what_is_not_ar":"ليس مجرد ضم الأشياء ولا عدد الألف ولا حرف الألف"},"support_links":[]},{"boundary":"Bu dal yalnızca özel yolculuk ve güvence bağlamındadır; sayı, kitap düzenleme veya genel yakınlık anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000045/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"mevsimlik yolculuk düzeni","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel bağlam, belirli topluluğun iki mevsim yolculuğunun özel ifadesidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklama yolculukların birbirine bağlanıp kesintisiz kalmasını öne çıkarır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka açıklamalar yolculuğu hazırlama, donatma veya güvence sağlama yönünü verir."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel ifade için doğal bir açıklayıcı karşılıktır; yolculukların bağlanması, hazırlanması ve güvence altına alınması yönlerini kapsar.","boundary_detail":"Bu dal yalnızca özel yolculuk ve güvence bağlamındadır; sayı, kitap düzenleme veya genel yakınlık anlamına genişletilmez.","branch_image_ar":"إيلاف قريش ورحلتها","concept_gloss":"mevsimlik yolculuk düzeni","contextual_glosses":[{"applicability":"İki mevsim yolculuğunun kesintisiz yürütülmesi vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hazırlama ve güvence sağlama açıklamalarını dışarıda bırakır.","preserves":"Yolculukları birleştirme ve süreklilik yönü korunur."},"facet_ids":["F002"],"text":"yolculukları birbirine bağlama","usage_role":"contextual"},{"applicability":"Koruma veya güvence açıklamasının öne çıktığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolculukları birleştirme ve hazırlama yönlerini dışarıda bırakır.","preserves":"Yolculuk için güvence sağlama yönünü korur."},"facet_ids":["F003"],"text":"yolculuk güvenliği sağlama","usage_role":"contextual"}],"definition":"Belirli bir topluluğun kış ve yaz yolculuklarını birbirine bağlama, kesintisiz yürütme, hazırlama veya güvence altına alma şeklindeki özel ifadedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel bağlam, belirli topluluğun iki mevsim yolculuğunun özel ifadesidir."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklama yolculukların birbirine bağlanıp kesintisiz kalmasını öne çıkarır."},{"facet_id":"F003","role":"source_variant","statement":"Başka açıklamalar yolculuğu hazırlama, donatma veya güvence sağlama yönünü verir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Genel kişisel alışma anlamı ekler.","collision":"Kökün yakınlık ve alışma dalıyla karışır.","fit":"displacement","loses":"Özel ifade, iki mevsim yolculuğu, hazırlık ve güvence yönlerini kaybeder.","preserves":"Tekrarlanan yolculuk fikrine gevşek biçimde yaklaşabilir."},"text":"alışkanlık"}],"identity_rationale":"Kaynak ifadesi belirli bir topluluğun kış ve yaz yolculuklarıyla bağlantılı özel kullanımını verir; açıklamalarda yolculukları birleştirme, kesintisiz kılma, hazırlama ve güvence sağlama yönleri bulunur. Geçici çerçeve uygundur, fakat dal yalın kök anlamı gibi genellenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"belirli topluluğun kış ve yaz yolculuklarını bağlama, hazırlama veya güvenceye alma ifadesi"}],"lexicalization_note":"Mekanik profil dalı yalın olmayan belirli ifade olarak sınırlar; tanım bu özel yolculuk bağlamının dışına çıkarılmaz.","neighbor_coverage_note":"Adaylar yolculuk, güvence, dayanma ve kök içi dallar açısından değerlendirildi; özel ifade sınırını açıklayanlar seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B004 özel tarihsel ve yolculuk bağlamını bırakmaz; B002 bu bağlam olmadan genel düzenleme işlemidir.","focus_only":"Odak dal özel mevsimlik yolculuk ifadesine bağlıdır.","gloss":"özel yolculuk ile birleştirme","neighbor_only":"Komşu dal genel parça birleştirme ve düzenleme anlamındadır.","neighbor_ref":"root_000045/B002","relation_type":"near_neighbor","shared_zone":"Yolculukları birbirine bağlama açıklaması genel birleştirme alanıyla örtüşür."},{"boundary_match":"partial","distinction":"B004 metinsel yolculuk düzenine bağlıdır; B005 genel bir alışma veya yakınlık halidir.","focus_only":"Odak dal yolculuk düzeni, hazırlık ve güvence etrafındadır.","gloss":"yolculuk düzeni ile ünsiyet","neighbor_only":"Komşu dal alışma, ünsiyet ve yer ya da kişiyle yakınlık kurmadır.","neighbor_ref":"root_000045/B005","relation_type":"near_neighbor","shared_zone":"Özel ifade, yakınlık veya alışılmış ilişki fikriyle gevşek temas kurabilir."},{"boundary_match":"field_only","distinction":"B004 ticari yolculuk düzenine bağlı özel kullanım taşır; komşu dal borç, kişi veya iş için sorumluluk üstlenmeyi anlatır.","focus_only":"Odak dal yolculukların bağlanması, hazırlanması ve güvenceye alınmasıdır.","gloss":"güvence ile kefalet","neighbor_only":"Komşu dal kefalet, bakım ve üstlenme alanındadır.","neighbor_ref":"root_001309/B005","relation_type":"same_field","shared_zone":"İkisinde de başkası için güvence veya üstlenme alanı bulunabilir."}],"source_phrase_ar":"لإيلاف قريش (maqayis;mufradat)؛ لتؤلف قريش رحلة الشتاء والصيف أي تجمع بينهما (sihah)؛ لتؤلف قريش الرحلتين فيتصلا ولا ينقطعا (tahdhib)؛ يؤلفون يهيئون ويجهزون (tahdhib)؛ يؤلفون يجيرون (tahdhib)؛ لهم إلف وليس لكم إيلاف (tahdhib)","source_summary":"Kaynaklar özel ifadeyi belirli topluluğun mevsimlik yolculukları etrafında toplar; açıklamalar yolculukları birleştirme, kesintisiz sürdürme, hazırlama ve güvence sağlama yönleri arasında değişir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"إيلاف قريش؛ إلفهم أو إيلافهم الرحلة؛ وصل الرحلتين؛ تهيئة الرحلة وتجهيزها؛ الجوار الذي يؤمن التجارة","what_is_not_ar":"ليس عدد الألف ولا تأليف الكتب ولا حرف الألف"},"support_links":[]},{"boundary":"Bu dal yakınlık ve alışma halidir; parçaları düzenleme veya bin sayısına ulaştırma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000045/B005","candidate_links":[{"candidate_id":"cand_60729d217274922a8ffa","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"ünsiyet ve alışma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel çekirdek, bir kişi veya şeyle ünsiyet kurup onu tanıdık bulmadır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alışılan şeye bağlı kalma ve onu bırakmama, ünsiyetin süreklilik yönüdür."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yere veya eve alışmış kuş ve evcil güvercin örnekleri bu çekirdeğin canlılara uygulanışıdır."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi, yer, şey veya canlılarla kurulan tanışıklık, yakınlık ve bağlı kalma anlamını birlikte karşılar.","boundary_detail":"Bu dal yakınlık ve alışma halidir; parçaları düzenleme veya bin sayısına ulaştırma anlamı değildir.","branch_image_ar":"الألفة والأنس والملازمة","concept_gloss":"ünsiyet ve alışma","contextual_glosses":[{"applicability":"Bir yer, kişi veya şeye zamanla yakınlık kurma bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma, tanıdık bulma ve bağ kurma yönleri korunur."},"facet_ids":["F001","F002"],"text":"alışmak","usage_role":"general"},{"applicability":"Kuş veya güvercin gibi canlıların ev ya da yere alışmış olmasını anlatan bağlamlarda uygundur.","error_profile":{"adds":"Evcil hayvanlık çağrışımı ekleyebilir.","collision":null,"fit":"narrowing","loses":"İnsanlar ve genel nesnelerle ünsiyet anlamını dışarıda bırakır.","preserves":"Canlının bir yere alışmış ve orayı bırakmayan hali korunur."},"facet_ids":["F003"],"text":"evcilleşmiş olmak","usage_role":"contextual"}],"definition":"Bir kişi, yer veya şeyle ünsiyet kurup ona alışma, onunla kalmayı sürdürme ve bu yüzden onun tanıdık ya da alışılmış hale gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel çekirdek, bir kişi veya şeyle ünsiyet kurup onu tanıdık bulmadır."},{"facet_id":"F002","role":"core","statement":"Alışılan şeye bağlı kalma ve onu bırakmama, ünsiyetin süreklilik yönüdür."},{"facet_id":"F003","role":"example","statement":"Bir yere veya eve alışmış kuş ve evcil güvercin örnekleri bu çekirdeğin canlılara uygulanışıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dışsal parça düzenleme işlemi ekler.","collision":"Kökün birleştirme dalıyla karışır.","fit":"displacement","loses":"Ünsiyet, alışma ve bağlı kalma halini kaybeder.","preserves":"Yakınlaşma fikrine uzak bir temas taşıyabilir."},"text":"birleştirmek"}],"identity_rationale":"Kaynak ifadesi bir kişi, şey veya yerle ünsiyet kurma, ona alışma ve onu bırakmadan sürdürme anlamlarını verir; evcilleşmiş veya bir yere alışmış kuş örnekleri de buna bağlıdır. Geçici çerçeve bu çekirdeği doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"alışılan, tanıdık ve ünsiyet duyulan kişi veya şey"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir yere alışmak, orada kalmayı sürdürmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bir kimseyle ünsiyet kurmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir eve veya yere alışmış kuşlar"}],"lexicalization_note":"Form adları ve kişi, yer, kuş gibi kalıplı kullanımlar birlikte bulunur; tanım hepsini alışma ve ünsiyet çekirdeğinde tutar.","neighbor_coverage_note":"Adaylar ünsiyet, arkadaşlık, evcillik, yabanilik ve kök içi anlamlar bakımından tarandı; karşıt ve yakın sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B005 alışma ve süreklilik vurgusu taşır; komşu dal yabancılık veya ürküntünün kalkması yönünden daha belirgindir.","focus_only":"Odak dal alışma, tanıdık bulma ve bağlı kalma yönlerini de taşır.","gloss":"ünsiyet ile yabancılığı giderme","neighbor_only":"Komşu dal korku veya yabancılığı gideren yakınlık ve sevinç alanını öne çıkarır.","neighbor_ref":"root_000059/B003","relation_type":"near_synonym","shared_zone":"İkisinde de yakınlık ve rahatlama alanı vardır."},{"boundary_match":"opposed","distinction":"B005 yakınlık ve alışmışlığı bildirir; komşu dal bunun karşısında uzak duran, alışmayan hali bildirir.","focus_only":"Odak dal birine veya bir yere alışıp yakınlık kurmadır.","gloss":"alışma ile yabanilik","neighbor_only":"Komşu dal kimseye alışmayan ve sokulmayan yabani haldir.","neighbor_ref":"root_000727/B010","relation_type":"antonym","shared_zone":"İkisi de canlıların başkalarıyla yakınlık kurup kurmaması eksenindedir."},{"boundary_match":"partial","distinction":"B005 daha çok tanışıklık ve alışkanlık ilişkisini verir; komşu dal psikolojik rahatlama ve açılma yönünü taşır.","focus_only":"Odak dal alışılan kişi, yer veya şeye bağlı kalmayı içerir.","gloss":"alışma ile rahatlama","neighbor_only":"Komşu dal insana veya şeye karşı rahatlama, açılma ve iç ferahlığını öne çıkarır.","neighbor_ref":"root_000563/B007","relation_type":"near_synonym","shared_zone":"İkisinde de ünsiyet ve yakınlık vardır."},{"boundary_match":"opposed","distinction":"B005 yakınlık kurmayı ve alışmayı belirtir; komşu dal bu yakınlıktan kaçan veya ayrı duran hali belirtir.","focus_only":"Odak dal insan, yer veya şeye alışma ve ünsiyettir.","gloss":"ünsiyet ile yaban","neighbor_only":"Komşu dal insandan uzaklaşan veya evcilleşmeyen yabani varlık alanıdır.","neighbor_ref":"root_001632/B001","relation_type":"antonym","shared_zone":"İkisi de evcil-yabani ve yakın-uzak ekseninde karşılaşır."},{"boundary_match":"partial","distinction":"B005 içsel ve ilişkisel yakınlık halini anlatır; B002 dışsal birleştirme ve tertip kurma işlemidir.","focus_only":"Odak dal alışma ve ünsiyet halidir.","gloss":"alışma ile bağlama","neighbor_only":"Komşu dal parçaları bağlama ve düzenleme işlemidir.","neighbor_ref":"root_000045/B002","relation_type":"near_neighbor","shared_zone":"İkisi de yakınlık veya ayrılığın azalması alanına dokunur."}],"source_phrase_ar":"ألفت الشيء آلفه والألفة مصدر الائتلاف (maqayis)؛ إلفك وأليفك الذي تألفه (maqayis)؛ آلفت المكان والقوم (maqayis)؛ أوالف الطير التي بمكة (maqayis)؛ فلان قد ألف هذا الموضع يألفه إلفا (sihah)؛ ألفت الشيء وآلفته بمعنى واحد أي لزمته (tahdhib)؛ ألفت فلانا إذا أنست به (tahdhib)؛ أوالف الحمام دواجنها التي تألف البيوت (tahdhib)؛ يقال للمألوف إلف وأليف (mufradat)؛ أوالف الطير ما ألفت الدار (mufradat)","source_summary":"Kaynaklar, kişi, yer veya şeyle kurulan alışma ve ünsiyet ilişkisini ortak çekirdek yapar; bir yere bağlı kalan kuş örnekleri bu çekirdeğin somut kullanımını gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"إلف الشيء أو الشخص أو المكان؛ الأنس به؛ لزومه؛ جعل غيره يألفه؛ أوالف الطير والحمام والدواجن","what_is_not_ar":"ليس جمع الأشياء تأليفا ولا بلوغ الألف عددا"},"support_links":["sup_cd1d4c03614064588e72"]},{"boundary":"Bu dal yazı ve ses işareti adıdır; bin sayısı, ünsiyet veya parçaları birleştirme anlamı değildir.","branch_kind":"bare","branch_ref":"root_000045/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","surface_ar":"إِيلَٰفِ"}],"gloss":"alfabe işareti adı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel çekirdek, alfabe içindeki belirli yazı ve ses işaretinin adıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu işaretin dil bilgisi ve yazı kullanımındaki tür adları aynı teknik dala bağlıdır."}}],"root_ar":"ء ل ف","root_id":"root_000045","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yazı ve ses sistemi içinde belirli işaretin adı ve teknik alt adları için uygundur.","boundary_detail":"Bu dal yazı ve ses işareti adıdır; bin sayısı, ünsiyet veya parçaları birleştirme anlamı değildir.","branch_image_ar":"الألف حرف من حروف الهجاء","concept_gloss":"alfabe işareti adı","contextual_glosses":[{"applicability":"İşaretin yazı sistemi içindeki biçimi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ses ve dil bilgisi alt adlarını açıkça taşımaz.","preserves":"Yazı işareti olma yönü korunur."},"facet_ids":["F001"],"text":"yazı işareti","usage_role":"contextual"},{"applicability":"İşaretin yazım veya dil bilgisi türlerinden biri olarak geçtiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel alfabe adı yönünü daraltır.","preserves":"Teknik yazı ve dil bilgisi sınıflaması korunur."},"facet_ids":["F002"],"text":"dil bilgisi işareti","usage_role":"contextual"}],"definition":"Alfabedeki belirli yazı ve ses işaretinin adı ile bu işaretin dil bilgisi ve yazım içindeki tür adlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel çekirdek, alfabe içindeki belirli yazı ve ses işaretinin adıdır."},{"facet_id":"F002","role":"specialization","statement":"Bu işaretin dil bilgisi ve yazı kullanımındaki tür adları aynı teknik dala bağlıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sayı anlamı ekler.","collision":"Kökün sayı dalıyla karışır.","fit":"displacement","loses":"Alfabe işareti ve teknik yazı-dil bilgisi alanını kaybeder.","preserves":"Aynı biçimli ada işaret eder."},"text":"bin"}],"identity_rationale":"Kaynak ifadesi açıkça alfabe işaretinin adını ve bu işaretle ilgili yazı ve dil bilgisi adlandırmalarını verir. Geçici çerçeve, sayı veya yakınlık anlamlarını karıştırmadan bu teknik alanı doğru ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"alfabedeki belirli yazı ve ses işaretinin adı ve teknik türleri"}],"lexicalization_note":"Mekanik profil yalın dalı verir; tanım yalnızca alfabe işareti ve ona bağlı teknik adlandırmalarla sınırlıdır.","neighbor_coverage_note":"Adaylar alfabe işaretleri, sözcük birimi ve kök içi karışabilecek dallar bakımından tarandı; yazı-sayı ayrımı özellikle belirtildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yerine geçemezler; aynı türden teknik adlardır fakat gösterdikleri işaretler farklıdır.","focus_only":"Odak dal alfabedeki belirli bir başka yazı-ses işaretidir.","gloss":"iki alfabe işareti","neighbor_only":"Komşu dal başka bir alfabe işaretinin adı ve ona bağlı ses olaylarıdır.","neighbor_ref":"root_001569/B003","relation_type":"near_synonym","shared_zone":"İkisi de alfabe işareti adları ve teknik kullanımlar alanındadır."},{"boundary_match":"field_only","distinction":"Aynı alanı paylaşırlar ama her biri farklı bir işarete gönderir; bu yüzden anlamları eşdeğer değildir.","focus_only":"Odak dal kendi yazı-ses işaretini adlandırır.","gloss":"ayrı işaret adları","neighbor_only":"Komşu dal başka bir yazı-ses işaretini adlandırır.","neighbor_ref":"root_000896/B006","relation_type":"same_field","shared_zone":"İkisi de alfabe işaretlerinin adlarıdır."},{"boundary_match":"field_only","distinction":"B006 tek işaret adıdır; komşu dal anlam taşıyan daha büyük söz birimlerini kapsar.","focus_only":"Odak dal tek bir alfabe işaretinin adıdır.","gloss":"işaret ile sözcük","neighbor_only":"Komşu dal anlamlı söz, sözcük veya ifade birimi alanındadır.","neighbor_ref":"root_001316/B002","relation_type":"same_field","shared_zone":"İkisi de dil ve yazı birimleri alanına aittir."},{"boundary_match":"field_only","distinction":"B006 yazı ve ses sistemine aittir; B001 nicelik ve sayı alanına aittir.","focus_only":"Odak dal alfabe işareti adıdır.","gloss":"işaret ile sayı","neighbor_only":"Komşu dal bin sayısıdır.","neighbor_ref":"root_000045/B001","relation_type":"same_field","shared_zone":"İkisi de aynı biçimli teknik adlar olarak karışabilir."},{"boundary_match":"field_only","distinction":"B006 bir yazı birimini adlandırır; B002 parçaları bağlayan veya düzenleyen eylemsel anlamı taşır.","focus_only":"Odak dal tek bir alfabe işareti adıdır.","gloss":"işaret ile düzenleme","neighbor_only":"Komşu dal parçaları birleştirip düzenleme işlemidir.","neighbor_ref":"root_000045/B002","relation_type":"other","shared_zone":"Ortaklık aynı kök ailesi ve teknik ad benzerliğiyle sınırlıdır."}],"source_phrase_ar":"الألف من حروف التهجي (mufradat)؛ أصول الألفات ثلاثة (tahdhib)؛ الألف الفاصلة (tahdhib)؛ ألف العبارة (tahdhib)؛ الألف اللينة (tahdhib)؛ هذه ألف مؤلفة (tahdhib)","source_summary":"Kaynaklar, dalı alfabe işareti adı ve bu işaretle ilgili yazı-dil bilgisi türleri olarak sınırlar; anlam sayı veya ünsiyet alanına geçmez.","sources":["TA","MU"],"what_is_ar":"اسم حرف الألف من حروف الهجاء؛ وألقاب الألف في النحو والكتابة","what_is_not_ar":"ليس العدد ألفا ولا الألفة ولا تأليف الأشياء"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_5b92778e4df723a5f378","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:accumulated-ties-pressure","source_type":"word_analysis","support_ids":["sup_94ab949d6382191b7692","sup_97fdf2079132e15cf037"],"title":"number-field pressure suggests multiplied ties","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_c5d7b077135bf1322a15","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:caused-binding-range","source_type":"word_analysis","support_ids":["sup_97fdf2079132e15cf037","sup_9d01f3fcf8f9583ce59e"],"title":"caused binding includes pact, habituation, and social joining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_f1eed3e543723b63d4a1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:compact-cadence-and-hamza","source_type":"word_analysis","support_ids":["sup_1fc3ce21ae90843928ee","sup_97fdf2079132e15cf037"],"title":"genitive cadence and hamza make dependency audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_0bd6f0bbe7081d149537","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:construct-masdar-role-gap","source_type":"word_analysis","support_ids":["sup_8720cd2d3579f2faf4d4","sup_97fdf2079132e15cf037"],"title":"construct verbal noun leaves the binder unnamed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_96c6e40eec6ed6d927c6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:opening-lam-dependency","source_type":"word_analysis","support_ids":["sup_97fdf2079132e15cf037","sup_ae20504ec18c55eba9a7"],"title":"opening dependency creates a three-way grammatical pull","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_e6830a5bafa1dc1c4547","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:rare-reprise-before-command","source_type":"word_analysis","support_ids":["sup_97fdf2079132e15cf037","sup_e50abd8bbd0e58247a7d"],"title":"rare verbal noun immediately reprises in 106:2","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_3c8c3f825b8f2f75d440","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:1:variant-form-contrast","source_type":"word_analysis","support_ids":["sup_321262af64ada83af942","sup_97fdf2079132e15cf037"],"title":"variant apparatus shows what the standard form preserves","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:1","qac_refs":["106:1:1:1","106:1:1:2"],"status":"accepted"}},{"anchor_refs":["106:1:2"],"branch_refs":[],"candidate_id":"cand_b34932457d91449c7636","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:2:declinable-transparent-name","source_type":"word_analysis","support_ids":["sup_3e195d949625812e3dbd","sup_dde064dbc88f418aeb21"],"title":"tanwīn and diminutive shape keep the name transparent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:2","qac_refs":["106:1:2:1"],"status":"accepted"}},{"anchor_refs":["106:1:2"],"branch_refs":[],"candidate_id":"cand_73924a3b04fa0eebd2ca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:2:genitive-bound-referent","source_type":"word_analysis","support_ids":["sup_0b80a6b7773d27c2acdd","sup_3e195d949625812e3dbd"],"title":"proper name is bound as genitive complement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:2","qac_refs":["106:1:2:1"],"status":"accepted"}},{"anchor_refs":["106:1:2"],"branch_refs":[],"candidate_id":"cand_47313691608d7d09d188","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:2:hapax-local-concentration","source_type":"word_analysis","support_ids":["sup_065d03b7f60117438ba7","sup_3e195d949625812e3dbd"],"title":"single occurrence concentrates the name in this phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:2","qac_refs":["106:1:2:1"],"status":"accepted"}},{"anchor_refs":["106:1:2"],"branch_refs":[],"candidate_id":"cand_dedef5e4f7b9bc05a465","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:2:root-field-bound-gatherer","source_type":"word_analysis","support_ids":["sup_2753c732f9e7e3f8aff6","sup_3e195d949625812e3dbd"],"title":"gathering, acquisition, and dominance pressure remain bounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:2","qac_refs":["106:1:2:1"],"status":"accepted"}},{"anchor_refs":["106:1:2"],"branch_refs":[],"candidate_id":"cand_4e948e749c8bc2d6cf29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"106:1:2:sharp-final-cadence","source_type":"word_analysis","support_ids":["sup_031f2ac1ba372fd63475","sup_3e195d949625812e3dbd"],"title":"final sound seals the two-word phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"106:1:2","qac_refs":["106:1:2:1"],"status":"accepted"}},{"anchor_refs":["106:1:1"],"branch_refs":[],"candidate_id":"cand_fd908106cf72c211bbac","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000045"],"scope":"focus_ayah","source_local_id":"106:1:1:2","source_type":"qac_morpheme","support_ids":["sup_be4ebe98d20186a67028"],"title":"QAC root occurrence: ء ل ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["106:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"106:1","branch_refs":["root_000045/B005"],"candidate_id":"cand_60729d217274922a8ffa","commentary_obligation":"review","hft_ref":"hft_f8e01a71383bc0b79060","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_habituated_attachment","source_type":"hft","support_ids":["sup_cd1d4c03614064588e72"],"title":"b_habituated_attachment","trust":"legacy_unbound"},{"anchor_refs":["106:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"106:1","branch_refs":["root_000045/B002"],"candidate_id":"cand_d1af02360b5fac473e3a","commentary_obligation":"review","hft_ref":"hft_73849d7abdb9febe0cac","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_composed_collective","source_type":"hft","support_ids":["sup_4c89e808b11e1e9ab1b0"],"title":"b_composed_collective","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"لِإِيلَٰفِ قُرَيْشٍ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"106:1:1:1","qac_word_ref":"106:1:1","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","root_ar":"ء ل ف","surface_ar":"إِيلَٰفِ"},{"lemma_ar":"قُرَيْش","morph_features":"STEM|POS:PN|LEM:qurayo$|P|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"106:1:2:1","qac_word_ref":"106:1:2","root_ar":"","surface_ar":"قُرَيْشٍ"}],"word_analysis_qac_refs":[["106:1:1:1","106:1:1:2"],["106:1:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["106:1:1","106:1:2"]},"focus_surface_evidence":{"arabic_uthmani":"لِإِيلَٰفِ قُرَيْشٍ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"106:1:1:1","qac_word_ref":"106:1:1","root_ar":"","surface_ar":"لِ"},{"lemma_ar":"إِلَٰف","morph_features":"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"106:1:1:2","qac_word_ref":"106:1:1","root_ar":"ء ل ف","surface_ar":"إِيلَٰفِ"},{"lemma_ar":"قُرَيْش","morph_features":"STEM|POS:PN|LEM:qurayo$|P|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"106:1:2:1","qac_word_ref":"106:1:2","root_ar":"","surface_ar":"قُرَيْشٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["106:1:1:1","106:1:1:2"],["106:1:2:1"]],"word_analysis_refs":["106:1:1","106:1:2"],"word_rows":[{"analysis_record_ref":"106:1:1","analytic_gloss_range_en":"dependent lām plus Form IV verbal noun naming caused familiarity, binding, or covenantal habituation for Quraysh; the phrase is not a standalone declaration","analytic_root_gloss_range_en":"root range pressed here includes familiarity, habituation, tameness, social joining, reconciliation, composition, and a distant numerical accumulation field; the local Form IV maṣdar selects caused binding rather than every root branch","qac_refs":["106:1:1:1","106:1:1:2"],"root":{"arabic":"أ ل ف","transliteration":"ʾ-l-f"},"surface":{"arabic":"لِإِيلَٰفِ","transliteration":"li-ʾīlāfi"}},{"analysis_record_ref":"106:1:2","analytic_gloss_range_en":"the definite tribal proper name as genitive complement of the binding verbal noun; its declinable and diminutive shape keeps gathering, acquisition, and dominance pressures audible without replacing the name-sense","analytic_root_gloss_range_en":"root range includes gathering, drawing together, Quraysh as a name and affiliation, earning or acquiring bit by bit, sea-creature dominance, and rough cutting or interlocking images; the local word selects the proper-name branch while other branches survive only as derivational pressure","qac_refs":["106:1:2:1"],"root":{"arabic":"ق ر ش","transliteration":"q-r-sh"},"surface":{"arabic":"قُرَيْشٍ","transliteration":"qurayshin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["106:1"],"branch_refs":["root_000045/B005"],"candidate_id":"cand_60729d217274922a8ffa","evidence_scope":"focus_ayah","hft_ref":"hft_f8e01a71383bc0b79060","item_id":"b_habituated_attachment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_habituated_attachment","support_id":"sup_cd1d4c03614064588e72"},{"anchor_refs":["106:1"],"branch_refs":["root_000045/B002"],"candidate_id":"cand_d1af02360b5fac473e3a","evidence_scope":"focus_ayah","hft_ref":"hft_73849d7abdb9febe0cac","item_id":"b_composed_collective","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_composed_collective","support_id":"sup_4c89e808b11e1e9ab1b0"}],"diagnostics":[],"lane_counts":{"global":9,"macro":13,"micro":2},"packet_summary":{"ayah_count":4,"focus_ref":"106:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["106:1","106:2","106:3","106:4"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"106:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"106:1","lane":"micro","linguistic_source_ref":"106:1","surface_ref":"106:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"106:1","target_tokens":[["Kureyş'in",["106:1:2"]],["alışması",["106:1:1","106:1:2"]],["nedeniyle",["106:1:1"]]],"text":"Kureyş'in alışması nedeniyle,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":4,"id":"s106-p01-001-004","label":"Whole surah","number":1,"refs":["106:1","106:2","106:3","106:4"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2:sharp-final-cadence","source_type":"word_analysis","support_id":"sup_031f2ac1ba372fd63475","text":"{\"blocking_evidence\":null,\"headline\":\"final sound seals the two-word phrase\",\"reader_payoff\":\"The reader hears the name close the ayah with a compact, sharp texture rather than merely filling a syntactic slot.\",\"reason\":\"The sound observation remains locally tied to the final genitive complement and its tanwīn closure.\",\"representative_source_ids\":[\"QP-c4eef803\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2:hapax-local-concentration","source_type":"word_analysis","support_id":"sup_065d03b7f60117438ba7","text":"{\"blocking_evidence\":null,\"headline\":\"single occurrence concentrates the name in this phrase\",\"reader_payoff\":\"The reader notices that Quraysh has no second Quranic setting to dilute this phrase; its corpus role is concentrated in this one binding frame.\",\"reason\":\"The contextual profiles mark the form as a single low-occurrence proper name and tie its later pronoun references to the same surah, matching the CRITICAL hapax rows.\",\"representative_source_ids\":[\"QI-c175c405\",\"QH-a3210cf5\",\"QH-daf040a5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2:genitive-bound-referent","source_type":"word_analysis","support_id":"sup_0b80a6b7773d27c2acdd","text":"{\"blocking_evidence\":null,\"headline\":\"proper name is bound as genitive complement\",\"reader_payoff\":\"The reader notices Quraysh as the named participant inside the binding phrase, not as a free subject or new clause.\",\"reason\":\"QAC and attachment evidence make Quraysh the genitive muḍāf ilayh of the preceding verbal noun, while the ayah's order lands the fragment on that referent.\",\"representative_source_ids\":[\"QG-4e051b7d\",\"QG-51a894de\",\"QT-270b0b41\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:compact-cadence-and-hamza","source_type":"word_analysis","support_id":"sup_1fc3ce21ae90843928ee","text":"{\"blocking_evidence\":null,\"headline\":\"genitive cadence and hamza make dependency audible\",\"reader_payoff\":\"The reader hears the opening as one compact genitive unit whose onset can either catch at the hamza or smooth in variant recitation without changing the bond.\",\"reason\":\"Both local words are genitive in the forced construct relation, and the phonetic rows remain tied to the local surface and attested reading contrast.\",\"representative_source_ids\":[\"QP-25450b41\",\"QP-3e93a249\",\"QP-7a11ebab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2:root-field-bound-gatherer","source_type":"word_analysis","support_id":"sup_2753c732f9e7e3f8aff6","text":"{\"blocking_evidence\":null,\"headline\":\"gathering, acquisition, and dominance pressure remain bounded\",\"reader_payoff\":\"The reader hears the named tribe as a gatherer and acquirer being gathered into a bond, while the local sense remains the proper name Quraysh.\",\"reason\":\"V4 accepts separate branches for gathering, Quraysh as a name, acquisition, and dominance imagery; the local noun selects the name branch, so the other branches survive as derivational pressure rather than replacement meanings.\",\"representative_source_ids\":[\"QS-3ee8827e\",\"QS-b49060ba\",\"QY-0e066353\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:variant-form-contrast","source_type":"word_analysis","support_id":"sup_321262af64ada83af942","text":"{\"blocking_evidence\":null,\"headline\":\"variant apparatus shows what the standard form preserves\",\"reader_payoff\":\"The reader notices that the standard wording keeps a compressed nominal purpose frame rather than turning the opening into a direct command, a static companionship noun, or an explicit verbal clause.\",\"reason\":\"The variant rows function as contrastive apparatus: they clarify the canonical surface without replacing the aligned local reading.\",\"representative_source_ids\":[\"QF-33aefcfb\",\"QF-814eed34\",\"QF-d84a501c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2","source_type":"word_analysis","support_id":"sup_3e195d949625812e3dbd","text":"{\"gloss_range\":\"the definite tribal proper name as genitive complement of the binding verbal noun; its declinable and diminutive shape keeps gathering, acquisition, and dominance pressures audible without replacing the name-sense\",\"prose\":\"{{ar:قُرَيْشٍ}} ({{tr:qurayshin}}) is not an independent subject dropped into the line; it is the genitive complement that gives the opening bond its named social referent. The proper name identifies a known tribe without an article, while its kasra and tanwīn keep it fully declined and visibly responsive to {{ar:لِإِيلَٰفِ}} ({{tr:li-ʾīlāfi}}). That form matters because the name is not wholly opaque: its declinable, diminutive shape lets gathering, acquisition, and even dominance imagery press against the local proper-name sense. Those derivations do not make the ayah stop naming Quraysh, but they make the named gatherer the one being bound inside the phrase. Since the name appears only here in the corpus and closes the two-word ayah, its entire Quranic weight is concentrated in this suspended binding phrase; its q-r-sh texture moves from deep qaf to liquid r and closes on sh plus final tanwīn, making the close compact and sharp while audibly sealing the dependency.\",\"root_display\":\"{{ar:ق ر ش}} ({{tr:q-r-sh}})\",\"root_gloss_range\":\"root range includes gathering, drawing together, Quraysh as a name and affiliation, earning or acquiring bit by bit, sea-creature dominance, and rough cutting or interlocking images; the local word selects the proper-name branch while other branches survive only as derivational pressure\",\"surface_display\":\"{{ar:قُرَيْشٍ}} ({{tr:qurayshin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:construct-masdar-role-gap","source_type":"word_analysis","support_id":"sup_8720cd2d3579f2faf4d4","text":"{\"blocking_evidence\":null,\"headline\":\"construct verbal noun leaves the binder unnamed\",\"reader_payoff\":\"The reader notices that the word names an act-like bond without naming the causer, so Quraysh can stand within both agency and receptivity.\",\"reason\":\"The local construction makes the word a genitive construct head over Quraysh, and the maṣdar relation leaves the participant direction and ultimate agent unstated.\",\"representative_source_ids\":[\"QG-0a4eaf1f\",\"QG-dff5bbeb\",\"QI-3e5ccc36\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:accumulated-ties-pressure","source_type":"word_analysis","support_id":"sup_94ab949d6382191b7692","text":"{\"blocking_evidence\":null,\"headline\":\"number-field pressure suggests multiplied ties\",\"reader_payoff\":\"The reader can hear the bond as a network of accumulated connections, while the local word still means caused binding rather than a number.\",\"reason\":\"The numerical field is not selected as the local sense, but the row's accumulation claim can survive as limited pressure because it does not replace the maṣdar reading.\",\"representative_source_ids\":[\"QS-5bb97b9f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1","source_type":"word_analysis","support_id":"sup_97fdf2079132e15cf037","text":"{\"gloss_range\":\"dependent lām plus Form IV verbal noun naming caused familiarity, binding, or covenantal habituation for Quraysh; the phrase is not a standalone declaration\",\"prose\":\"{{ar:لِإِيلَٰفِ}} ({{tr:li-ʾīlāfi}}) begins with dependency rather than completion. The opening lām can pull the phrase forward toward the worship command (106:3), be read backward toward the prior surah, or carry exclamatory force; in all three cases the first word makes the reader hold the phrase open instead of treating the ayah as a finished statement. As a construct maṣdar, it keeps verbal force while leaving the binder unnamed, so {{ar:قُرَيْشٍ}} ({{tr:qurayshin}}) can be heard within a bond that is both their cohesion and their being made cohesive. The selected Form IV shape makes familiarity something caused: covenant, habituation around the House named in 106:3, taming, and social joining converge, while the numerical accumulation field remains only a secondary pressure of multiplied ties. Variant readings that turn the opening into a jussive command, a static companionship noun, or an explicit verbal clause show what the standard wording preserves: a compressed nominal purpose frame with the actor less explicit. The same rare verbal noun returns as {{ar:إِۦلَٰفِهِمْ}} ({{tr:ʾīlāfihim}}) in 106:2, moving from bare binding to their binding before the command response, and the genitive cadence plus hamza onset makes the two-word opening feel compact but audibly arrested; the hamza-dropping variant smooths that onset without replacing the same semantic bond.\",\"root_display\":\"{{ar:أ ل ف}} ({{tr:ʾ-l-f}})\",\"root_gloss_range\":\"root range pressed here includes familiarity, habituation, tameness, social joining, reconciliation, composition, and a distant numerical accumulation field; the local Form IV maṣdar selects caused binding rather than every root branch\",\"surface_display\":\"{{ar:لِإِيلَٰفِ}} ({{tr:li-ʾīlāfi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:caused-binding-range","source_type":"word_analysis","support_id":"sup_9d01f3fcf8f9583ce59e","text":"{\"blocking_evidence\":null,\"headline\":\"caused binding includes pact, habituation, and social joining\",\"reader_payoff\":\"The reader sees Quraysh's stability as something produced through covenantal and habituating cohesion, not as a neutral tribal fact.\",\"reason\":\"The local Form IV maṣdar licenses caused familiarity and binding; related family evidence for reconciliation, taming, and composition survives as lexical pressure, while no V4 rows are available to further separate the root branches.\",\"representative_source_ids\":[\"QS-21906178\",\"QS-e38ba04d\",\"QY-6722669d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:opening-lam-dependency","source_type":"word_analysis","support_id":"sup_ae20504ec18c55eba9a7","text":"{\"blocking_evidence\":null,\"headline\":\"opening dependency creates a three-way grammatical pull\",\"reader_payoff\":\"The reader notices that the surah opens by making the phrase lean beyond itself, with forward, backward, and exclamatory readings generated by the same initial dependency.\",\"reason\":\"The QAC grammar and translation support identify a dependent lām plus maṣdar construction completed by the wider discourse, while the CRITICAL rows preserve the recognized structural alternatives.\",\"representative_source_ids\":[\"QG-054b75a3\",\"MG-b5338d29\",\"QY-7fa98f51\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"106:1:1:2","source_type":"qac_morpheme","support_id":"sup_be4ebe98d20186a67028","text":"{\"lemma_ar\":\"إِلَٰف\",\"morph_features\":\"STEM|POS:N|VN|(IV)|LEM:<ila`f|ROOT:Alf|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"106:1:1:2\",\"qac_word_ref\":\"106:1:1\",\"root_ar\":\"ء ل ف\",\"surface_ar\":\"إِيلَٰفِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:2:declinable-transparent-name","source_type":"word_analysis","support_id":"sup_dde064dbc88f418aeb21","text":"{\"blocking_evidence\":null,\"headline\":\"tanwīn and diminutive shape keep the name transparent\",\"reader_payoff\":\"The reader sees the word as a definite tribal name that still sounds morphologically formed and open to its older common-noun field.\",\"reason\":\"The grammar flags the proper noun as triptotic with tanwīn and notes its diminutive form, while V4 preserves Quraysh as a name alongside related root branches.\",\"representative_source_ids\":[\"QG-5e9158e3\",\"QF-a9db75ad\",\"QF-acf808ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"106:1:1:rare-reprise-before-command","source_type":"word_analysis","support_id":"sup_e50abd8bbd0e58247a7d","text":"{\"blocking_evidence\":null,\"headline\":\"rare verbal noun immediately reprises in 106:2\",\"reader_payoff\":\"The reader notices that the opening abstraction is not left alone; it is immediately restated as their binding in 106:2 before the command response appears.\",\"reason\":\"Contextual evidence marks the exact form as low-occurrence and the supplement points to 106:2, matching the CRITICAL same-surah echo rows.\",\"representative_source_ids\":[\"QE-54a9fd23\",\"QH-6af8993c\",\"QI-40170849\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"لِإِيلَٰفِ قُرَيْشٍ","ayah_ref":"106:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000045/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000045","role":"Familiar attachment and habitual staying supply the affective-temporal core: recurrence settles Quraysh into an enduring relation.","root":"ء ل ف","source_ref":"106:1","source_word_indices":["1"]}],"changed_reading":{"after":"An open causal or purposive heading about an acquired disposition to remain attached, with possessor and producer still unresolved.","before":"A static label for the familiarity of Quraysh."},"confidence":"strong","focus_anchor":"The prefixed lām leaves the relation open, while the verbal noun and its genitive attachment to Quraysh do not settle whether Quraysh possess the habit or are made to acquire it.","mechanism":"The focus can name repeated acclimation that turns a person, place, or practice into something familiar and stayable. Focus-only, both Quraysh's habituated attachment and the habituating of Quraysh remain live.","model_id":"b_habituated_attachment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_habituated_attachment","source_type":"hft","support_id":"sup_cd1d4c03614064588e72","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لِإِيلَٰفِ قُرَيْشٍ","ayah_ref":"106:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000045/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000045","role":"Joining differentiated parts after separation supplies the constructive operation and makes Quraysh the composed whole or its beneficiary.","root":"ء ل ف","source_ref":"106:1","source_word_indices":["1"]}],"changed_reading":{"after":"Quraysh are actively composed, or have a composite arrangement made for them, out of parts that could otherwise remain separate.","before":"Quraysh simply enjoy harmony."},"confidence":"medium","focus_anchor":"The verbal noun in the focus can denote an operation, and Quraysh as its genitive can mark the collective assembled by it or the collective for whom it is arranged.","mechanism":"Joining after separation makes īlāf an active composition rather than a mood of concord. Distinct people, practices, or relations are fitted together so that Quraysh exists or functions as a coherent social body.","model_id":"b_composed_collective"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_composed_collective","source_type":"hft","support_id":"sup_4c89e808b11e1e9ab1b0","trust":"legacy_unbound"}]}
</lane_packet_json>
