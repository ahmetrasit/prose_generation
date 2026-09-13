# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **99:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s099-regular-20260912/s099/99_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "99:1",
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
{"branch_registry":[{"boundary":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_32649a1bedfdcf77dc2d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"yer ve yere bakan alt bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer küresi anlamını ve ona bağlı alt bölüm yönelimini birlikte özetleyen en kısa doğal karşılıktır.","boundary_detail":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_image_ar":"السفل المقابل للسماء","concept_gloss":"yer ve yere bakan alt bölüm","contextual_glosses":[{"applicability":"Üzerinde yaşanan ve göğün karşısında bulunan yer küresi söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin altı ile hayvan ayağının alt bölümüne bağlı kullanımları dışarıda bırakır.","preserves":"Üzerinde yaşanan aşağı yer ve göğe karşıt konum anlamını korur."},"facet_ids":["F001"],"text":"yeryüzü","usage_role":"contextual"}],"definition":"Göğün karşısında aşağıda bulunan, üzerinde yaşadığımız yer küresini belirtir. Belirli tamlamalarda bir şeyin yere bakan altını ve hayvanın tırnağını ya da ayağının alt bölümünü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}],"identity_rationale":"Kaynak ifadesi, göğün karşısında aşağıda bulunan ve üzerinde yaşanan yeri temel anlam olarak verir; nesnelerin yere bakan altı ile hayvan ayağının alt bölümü de buna bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yer, yeryüzü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, ülkeler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin yere bakan altı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hayvanın tırnağı veya ayaklarının altı"}],"lexicalization_note":"Tanım yalın yer anlamını kapsar; alt bölüm ve hayvan ayağı anlamlarını ise yalnız belirtilen tamlamalara bağlı yan yüzler olarak tutar.","neighbor_coverage_note":"Sağlanan bütün komşu kartları değerlendirildi; yer yüzeyiyle doğrudan karışabilecek en yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği aşağıda ve göğün karşısında bulunan yerdir; komşu dal ise yüzeyin genişliği ve düzlüğü ile serilmiş eşya fikrini öne çıkarır.","focus_only":"Göğün karşısındaki yer küresini ve tamlamalardaki alt bölüm anlamlarını kapsar.","gloss":"geniş düz yer veya yaygı","neighbor_only":"Geniş ve düz araziyi, ayrıca serilip yayılan eşyayı anlatır.","neighbor_ref":"root_000116/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da yayılmış bir yüzey olarak yer alanına dokunur."}],"source_phrase_ar":"كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)","source_summary":"Kaynaklar, anlamın merkezinde göğün karşısındaki aşağı yerin bulunduğunu; alt bölüm ve hayvan ayağı kullanımlarının bu mekansal çekirdeğe dayandığını birlikte gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","what_is_not_ar":"ليس الزكام ولا الرعدة ولا الدودة ولا البساط"},"support_links":["sup_2434f755fe567f436990"]},{"boundary":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"yumuşak ve verimli toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oğlak yer bitkisini yer."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın toprak niteliğine dayanan çekirdeğini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_image_ar":"الأرض اللينة المنبتة","concept_gloss":"yumuşak ve verimli toprak","contextual_glosses":[{"applicability":"Bitkinin toprağa yerleşerek çoğalması anlatılan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın genel niteliğini ve oğlağın bu bitkiyle beslenmesi yüzünü dışarıda bırakır.","preserves":"Bitkinin toprağa yerleşmesi ve gelişerek çoğalması sürecini korur."},"facet_ids":["F002"],"text":"iyice köklenip çoğalmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda yumuşak, iyi, verimli ve bol bitki yetiştiren toprağı anlatır. Buna bağlı yapılarda bitkinin toprağa iyice yerleşip çoğalması veya biçilebilir olması, köklü fidan ve yer bitkisini yiyen oğlak; ayrı bir kaynak kullanımında ise semiz oğlak ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."},{"facet_id":"F002","role":"extension","statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."},{"facet_id":"F003","role":"associated_use","statement":"Oğlak yer bitkisini yer."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}],"identity_rationale":"Kaynak ifadesi yumuşak, iyi ve verimli toprağı merkez alır; bitkinin köklenip çoğalması veya biçilecek duruma gelmesi ile oğlağın bu ottan yiyip semirmesi buna bağlı gelişmelerdir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yumuşak, verimli ve bol bitkili toprak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşak tabanlı geniş çayırlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak verimlileşti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprakta kök salmış fidan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"oğlak yer bitkisini yedi veya onunla semirdi"}],"lexicalization_note":"Tanım, nitelikli toprak anlamını yalnız kanıtlanan tamlamalara; bitki, fidan ve oğlakla ilgili anlamları da kendi kanıtlanmış yapılarına bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; verimli toprak çekirdeğine en yakın olup kapsam farkı taşıyan kart seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yumuşaklık ve iyi bitkilenmeyle birlikte belirli bitki ve oğlak yapılarını taşır; komşu dal kolaylık ve hızlı yetişme niteliğine uzanır.","focus_only":"Bitkinin yerleşmesi, biçilebilir olması ve oğlağın bitkiyle beslenmesi gibi bağlı kullanımları vardır.","gloss":"kolay işlenen verimli toprak","neighbor_only":"Kolay işlenen yer ve bitkinin hızlı yetişmesi özelliklerini daha genel biçimde kapsar.","neighbor_ref":"root_000058/B004","relation_type":"near_synonym","shared_zone":"İki dal da verimli, iyi bitki yetiştiren toprağı anlatır."}],"source_phrase_ar":"أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)","source_summary":"Birleşik kanıt, verimli ve yumuşak toprağı; bu toprakta gelişen bitkiyi ve bitkiden yararlanan oğlağı aynı üretkenlik ilişkisi içinde toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض الأريضة والروضة الأريضة؛ الأرض الزاكية الحسنة النبت؛ النبات المتأرض إذا تمكن في الأرض وكثر أو أمكن جزه؛ الجدي الأريض إذا تناول نبت الأرض أو سمن","what_is_not_ar":"ليس أسفل الشيء مطلقا ولا الرعدة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_kind":"collocation","branch_ref":"root_000025/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"iyiliğe yatkın ve layık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyiliğe yatkın ve ona layıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişi hakkında kurulan belirtilmiş yapıda dalın temel niteliğini karşılar.","boundary_detail":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_image_ar":"الخليق بالخير كالأرض الأريضة","concept_gloss":"iyiliğe yatkın ve layık","contextual_glosses":[{"applicability":"Bir topluluk içinden belirli işi yapmaya en uygun kişi seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğe yatkın ve alçak gönüllü kişi niteliğini dışarıda bırakır.","preserves":"Belirli eyleme başkalarından daha uygun ve layık olma karşılaştırmasını korur."},"facet_ids":["F002"],"text":"bunu yapmaya en uygunları","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişinin iyiliğe yatkın ve ona layık olmasını anlatır; bir kaynak bu niteliği alçak gönüllülükle birlikte verir. Karşılaştırmalı kullanımda ise bir işi yapmaya başkalarından daha uygun olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyiliğe yatkın ve ona layıktır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}],"identity_rationale":"Kaynak ifadesi belirli yapılarda bir kişinin iyiliğe yatkın, ona layık ve alçak gönüllü oluşunu; karşılaştırmalı yapıda ise bir işi yapmaya en uygun kişi sayılmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iyiliğe yatkın, layık ve alçak gönüllü kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu yapmaya en uygunları"}],"lexicalization_note":"Tanım bütünüyle belirtilen kişi ve eylem tamlamalarına bağlıdır; yalın biçime bağımsız bir uygunluk anlamı yüklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel layıklık alanıyla karışma olasılığı en yüksek olan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iyilik alanına ve iki belirli yapıya bağlıdır; komşu dalın uygunluk ve hazır oluş kapsamı daha geneldir.","focus_only":"İyiliğe yatkınlıkla birlikte alçak gönüllülük çağrışımı ve belirli kalıplara bağlılık taşır.","gloss":"bir şeye layık ve hazır","neighbor_only":"Herhangi bir şeye hazır, uygun veya layık olmayı daha geniş biçimde anlatır.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ile uygun görüldüğü nitelik veya eylem arasındaki yatkınlık ilişkisini bildirir."}],"source_phrase_ar":"رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)","source_summary":"Kaynaklar, iyiliğe yatkınlık ve layıklık ile belirli bir eyleme en uygun olma yargısını yapı bağımlı tek bir uygunluk alanında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الرجل الأريض للخير؛ آرض القوم أن يفعل الشيء أي أخلقهم به","what_is_not_ar":"ليس الأرض الحسية ولا الزكام ولا الرعدة"},"support_links":[]},{"boundary":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_kind":"non_bare","branch_ref":"root_000025/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan sabit adlandırmanın kişi anlamını doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_image_ar":"ابن الأرض الغريب","concept_gloss":"yabancı kimse","definition":"Belirli bir sabit adlandırmada, bulunduğu çevreye dışarıdan gelen veya oraya ait olmayan yabancı kimseyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}],"identity_rationale":"Tek kaynak ifadesi, sabit bir adlandırmanın doğrudan yabancı kimse anlamına geldiğini belirtir; yer sakini veya soy bağına ilişkin daha ayrıntılı bir koşul kurmaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yabancı kimse"}],"lexicalization_note":"Tanım yalnız kanıtlanan sabit söz birimine bağlanır; parçaların yalın anlamlarından yeni bir kişi sınıfı türetilmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel yabancı anlamına en yakın, fakat topluluk koşuluyla ayrılan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kanıtı yalnız yabancı olmayı söyler; komşu dal yabancının başka bir topluluk içinde bulunması koşulunu açıkça taşır.","focus_only":"Yabancılığı herhangi bir ek topluluk koşulu vermeden sabit bir adlandırmayla bildirir.","gloss":"başka bir topluluğa girmiş yabancı","neighbor_only":"Kişinin kendisinden olmayan bir topluluğun içine girmiş bulunmasını özellikle belirtir.","neighbor_ref":"root_000009/B006","relation_type":"near_synonym","shared_zone":"İki dal da bulunduğu insan çevresine aslen ait olmayan kişiyi anlatır."}],"source_phrase_ar":"فلان ابن أرض أي غريب (maqayis)","source_summary":"Tek kanıt, söz biriminin yabancı kimseyi belirten kısıtlı ve kalıplaşmış bir adlandırma olduğunu gösterir.","sources":["MQ"],"what_is_ar":"ابن أرض إذا أريد الغريب","what_is_not_ar":"ليس ساكن الأرض مطلقا ولا الأرض التي نحن عليها"},"support_links":[]},{"boundary":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_kind":"bare","branch_ref":"root_000025/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"kalın yün veya kıl yaygı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin türünü, belirleyici kalınlığını ve iki olası malzemesini birlikte karşılar.","boundary_detail":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_image_ar":"الإراض البساط الضخم","concept_gloss":"kalın yün veya kıl yaygı","definition":"Yünden veya hayvan kılından yapılmış kalın ve büyükçe bir yaygıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}],"identity_rationale":"Kaynak ifadesi nesneyi kalın, büyükçe bir yaygı olarak tanımlar ve malzemesini yün ya da hayvan kılıyla sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın yün veya kıl yaygı"}],"lexicalization_note":"Tanım yalın adın kanıtlanan nesne anlamıyla sınırlıdır ve komşu döşeme türlerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Sağlanan kartların tümü değerlendirildi; nesne türü bakımından en yakın fakat kapsamı daha geniş döşeme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal malzeme ve kalınlıkla tanımlanan belirli bir yaygıdır; komşu dal işlevi bakımından daha geniş bir döşeme sınıfıdır.","focus_only":"Yaygının kalın ve özellikle yün ya da hayvan kılından yapılmış olmasını gerektirir.","gloss":"döşek veya alta serilen örtü","neighbor_only":"Döşek, yatak örtüsü ve genel olarak alta serilen nesneleri kapsar.","neighbor_ref":"root_001397/B007","relation_type":"same_field","shared_zone":"Her iki dal da zemine ya da yatma yerine serilen ev eşyalarını adlandırır."}],"source_phrase_ar":"الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)","source_summary":"Kaynaklar nesnenin yaygı oluşunda, kalınlığında ve yün ya da hayvan kılından yapılmasında birleşir.","sources":["MQ","SI"],"what_is_ar":"الإراض بالكسر؛ بساط ضخم من وبر أو صوف","what_is_not_ar":"ليس الأرض ولا الأرضة ولا الأريضة"},"support_links":[]},{"boundary":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_kind":"bare","branch_ref":"root_000025/B006","candidate_links":[{"candidate_id":"cand_2d6c90f8e14e997aaf11","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"yere çökercesine ağırlaşıp oyalanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yerden ayrılmayarak yere bağlı kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yere bağlılık, ağırlaşma ve gecikme bileşenlerini tek bir eylem karşılığında toplar.","boundary_detail":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_image_ar":"لزوم الأرض والتثاقل إليها","concept_gloss":"yere çökercesine ağırlaşıp oyalanmak","contextual_glosses":[{"applicability":"Kişinin doğrudan yere bağlı kalması öne çıktığında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere doğru ağırlaşma ile oyalanıp gecikme görünüşlerini dışarıda bırakır.","preserves":"Yere bağlı kalma ve bulunduğu noktadan ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"yerinden ayrılmamak","usage_role":"contextual"}],"definition":"Kişinin yere bağlı kalmasını veya yere çökercesine ağırlaşmasını ve bu yüzden bir süre oyalanıp gecikmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yerden ayrılmayarak yere bağlı kalır."},{"facet_id":"F002","role":"extension","statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi kişinin yere bağlı kalmasını, yere doğru ağırlaşmasını ve bunun sonucu oyalanıp gecikmesini aynı hareket durumu içinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yere bağlı kalmak, ağırlaşıp oyalanmak"}],"lexicalization_note":"Tanım yalın eylem dalının yere bağlı kalma, ağırlaşma ve gecikme bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yere bağlı kalma çekirdeğini en doğrudan paylaşan ve kapsam farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin yere doğru ağırlaşıp gecikmesini anlatır; komşu dal farklı canlı ve nesnelerde yere yapışma ya da sabit kalma alanına daha geniş yayılır.","focus_only":"İnsan için yere doğru ağırlaşma ve bununla birlikte oyalanma anlamını taşır.","gloss":"yere yapışıp yerinde kalmak","neighbor_only":"İnsan dışında kuş ve yırtıcıları, ayrıca yuva ve yerinde ağır duran nesne örneklerini de kapsar.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dalda da yere yakın durma ve bulunulan yerden ayrılmama durumu vardır."}],"source_phrase_ar":"تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)","source_summary":"Kanıt, yere bağlı kalmayı çekirdek alır ve yere doğru ağırlaşma ile oyalanmayı bu durumun görünüşleri olarak birleştirir.","sources":["MQ","SI"],"what_is_ar":"تأرض فلان إذا لزم الأرض؛ التأرض بمعنى التثاقل والتلبث إلى الأرض","what_is_not_ar":"ليس التصدي والتعرض للغير ولا النبات المتأرض"},"support_links":["sup_e5a84824c68fc5490d2e"]},{"boundary":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_kind":"bare","branch_ref":"root_000025/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"karşısına çıkıp kendini ortaya koymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yönelmiş karşı duruşu ve görünür biçimde ortaya çıkmayı birlikte karşılar.","boundary_detail":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_image_ar":"التعرض والتصدي","concept_gloss":"karşısına çıkıp kendini ortaya koymak","definition":"Birine doğru yönelip onun karşısına çıkmayı, kendini ortaya koyarak ona karşı durmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}],"identity_rationale":"Tek kaynak ifadesi eylemi, birine doğru çıkıp onun karşısında kendini ortaya koymak ve ona karşı durmak biçiminde açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkıp kendini ortaya koymak"}],"lexicalization_note":"Tanım yalın eylem dalını, bir hedefe yönelme ve karşısına çıkma koşullarıyla sınırlar.","neighbor_coverage_note":"Tüm komşular değerlendirildi; yönelme ve karşıya çıkma çekirdeğini en yakından paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşıya çıkışı öne çıkarır; komşu dal bakma, gözetme ve genel yüzünü dönme kullanımlarını da kapsar.","focus_only":"Bir kişiye doğru gelerek onun karşısında kendini ortaya koyma hareketini bildirir.","gloss":"bir şeye yönelip karşısına çıkmak","neighbor_only":"Bir şeye bakmak üzere yükselme, onu gözetme veya yalnızca yüzünü ona çevirme kapsamına uzanır.","neighbor_ref":"root_000853/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe yönelme ve onun karşısında konum alma anlamını taşır."}],"source_phrase_ar":"جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)","source_summary":"Tek kanıt, eylemin hedefe yönelmiş bir karşıya çıkma ve kendini ortaya koyma hareketi olduğunu gösterir.","sources":["SI"],"what_is_ar":"جاء فلان يتأرض إلى غيره أي يتصدى ويتعرض له","what_is_not_ar":"ليس التثاقل إلى الأرض ولا لزومها"},"support_links":[]},{"boundary":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_kind":"bare","branch_ref":"root_000025/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"titreme veya ürperme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedenindeki kısa ya da süren sarsıntı durumunu doğrudan karşılar.","boundary_detail":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_image_ar":"الأَرْض الرعدة","concept_gloss":"titreme veya ürperme","definition":"Bir insanın bedeninde beliren titreme, sarsılma veya ürperme durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı insanda görülen titreme, sarsılma veya ürperme olarak açıkça tanımlar ve yer ya da hastalık anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"insanı tutan titreme veya ürperme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"titreme ve sarsılma"}],"lexicalization_note":"Tanım yalın biçimlerin insandaki titreme ve ürperme anlamıyla sınırlıdır; komşu hastalık nedenleri eklenmez.","neighbor_coverage_note":"Sağlanan bütün kartlar incelendi; genel titreme çekirdeğine en yakın ve kapsam farkı belirgin olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın bir insan titremesidir; komşu dal nedeni ve öznesi bakımından daha geniştir, ayrıca korkaklık ve gevşeklik nitelemelerine uzanır.","focus_only":"İnsan bedenindeki titreme durumunu herhangi bir özel neden belirtmeden adlandırır.","gloss":"korku veya hastalıktan sarsılma","neighbor_only":"Korku, hastalık veya gevşeklik nedeniyle insan ya da başka bir şeyin sarsılmasını ve kişilik nitelemelerini kapsar.","neighbor_ref":"root_000573/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insan bedenindeki titreme ve sarsılma alanında örtüşür."}],"source_phrase_ar":"الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)","source_summary":"Kaynaklar bu adın insanda görülen titreme ve ürperme durumunu bildirdiğinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الرعدة أو النفضة في الإنسان","what_is_not_ar":"ليس الأرض التي تقابل السماء ولا الزكام"},"support_links":[]},{"boundary":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_kind":"bare","branch_ref":"root_000025/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"soğuk algınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soğuk algınlığı durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hastalık çekirdeğini Türkçede en doğal ve ayırt edici biçimde karşılar.","boundary_detail":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_image_ar":"الأَرْض الزكام","concept_gloss":"soğuk algınlığı","contextual_glosses":[{"applicability":"Hastalığın kendisi değil, bu hastalığa tutulmuş kişi nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık adını ve birini hastalığa uğratma eylemini bağımsız olarak karşılamaz.","preserves":"Soğuk algınlığı ile kişi arasındaki etkilenme ilişkisini korur."},"facet_ids":["F002"],"text":"soğuk algınlığına yakalanmış","usage_role":"contextual"}],"definition":"Soğuk algınlığı hastalığını, bu hastalığa yakalanmış kişiyi ve birini bu hastalığa uğratma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soğuk algınlığı durumudur."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}],"identity_rationale":"Kaynak ifadesi hastalığı soğuk algınlığı olarak, etkilenen kişiyi bu hastalığa yakalanmış olarak ve ettirgen biçimi hastalığa uğratmak olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk algınlığı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına yakalanmış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına uğratmak"}],"lexicalization_note":"Tanım yalın hastalık adını ve aynı dalda kanıtlanan hasta kişi ile hastalığa uğratma türevlerini korur.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; aynı hastalık ve hasta kişi alanını en doğrudan paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın türetim dizisinde hastalığa uğratma da vardır; komşu dalın kanıtı ise bir kaynakta daha genel hastalık yorumu içerir.","focus_only":"Hastalık adı, hastaya ilişkin niteleme ve hastalığa uğratma eylemini birlikte kapsar.","gloss":"soğuk algınlığı ve hasta olma","neighbor_only":"Soğuk algınlığı yanında daha genel bir hastalık alanına açılan ayrı bir kaynak yorumunu da taşır.","neighbor_ref":"root_000916/B003","relation_type":"near_synonym","shared_zone":"Her iki dal soğuk algınlığını ve bu hastalığa yakalanmış kişiyi ifade eder."}],"source_phrase_ar":"الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)","source_summary":"Kaynaklar hastalık adı ile hasta kişi nitelemesinde birleşir; kanıt ayrıca hastalığa uğratma eylemini aynı türetim alanında gösterir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الزكمة أو الزكام؛ مأروض لمن أصابه الزكام","what_is_not_ar":"ليس الرعدة ولا الأرض الحسية"},"support_links":[]},{"boundary":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"odun yiyen küçük canlı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük canlı odunla beslenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıyı kanıtlanan boyutu ve onu ayırt eden beslenme davranışıyla kısa ve doğal biçimde karşılar.","boundary_detail":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_image_ar":"الأَرَضَة آكلة الخشب","concept_gloss":"odun yiyen küçük canlı","contextual_glosses":[{"applicability":"Bir odunun bu canlı tarafından yenerek zarar görmüş olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlının beyaz ve karıncaya benzer oluşunu bağımsız bir tanım olarak vermez.","preserves":"Odunun canlı tarafından yenmiş ve zarar görmüş olma sonucunu korur."},"facet_ids":["F002"],"text":"odun yiyen küçük canlı tarafından yenmiş","usage_role":"contextual"}],"definition":"Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük canlı odunla beslenir."},{"facet_id":"F002","role":"associated_use","statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}],"identity_rationale":"Kaynak ifadesi beyaz, karıncaya benzeyen ve odun yiyen küçük canlıyı tanımlar; ayrıca bu canlının odunu yiyerek onu zarar görmüş hale getirmesini verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"odun yiyen küçük canlı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"odunu bu canlı yedi ve zarar verdi"}],"lexicalization_note":"Tanım canlı adını yalın çekirdek olarak verir ve odunun yenmesini yalnız kanıtlanan tamlamaya bağlı sonuç yüzü olarak ayırır.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; odun yiyen canlı çekirdeğine en yakın fakat canlı ve nesne kapsamı farklı olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal odun yiyen küçük canlı ve onun oduna etkisidir; komşu dal ağaç, yaprak ve gövde üzerinde beslenen başka bir canlıya özgüdür.","focus_only":"Odun yiyen küçük canlıyı ve bu canlının yediği odunun sonucunu belirtir.","gloss":"ağacı delen ve yiyen küçük canlı","neighbor_only":"Özellikle ağaçta delik açan, yaprak veya odun yiyen başka bir küçük canlıyı ve ağacın uğradığı durumu kapsar.","neighbor_ref":"root_000699/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da odunsu bitki maddesini yiyerek zarar veren küçük canlıları anlatır."}],"source_phrase_ar":"الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)","source_summary":"Kaynaklar odun yiyen küçük canlı ile onun odunda oluşturduğu yenme ve zarar görme sonucunu aynı anlam alanında birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الأَرَضَة؛ دويبة تأكل الخشب؛ أرضت الخشبة فهي مأروضة إذا أكلتها الأرضة","what_is_not_ar":"ليس الأرض ولا الأرض الأريضة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_kind":"collocation","branch_ref":"root_000025/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"yaranın irinlenip bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yara bağlamında irin toplama ile ortaya çıkan bozulma sürecini eksiksiz karşılar.","boundary_detail":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_image_ar":"فساد القرحة بالمدة","concept_gloss":"yaranın irinlenip bozulması","definition":"Bir yaranın irin toplaması, kabarıp su toplaması ve bu irinlenme yüzünden bozulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}],"identity_rationale":"Tek kaynak ifadesi, yaranın irin toplamasıyla kabarıp bozulmasını bir süreç olarak verir; yalnız irin maddesini veya genel deri şişliğini adlandırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yara irinlenip kabardı ve bozuldu"}],"lexicalization_note":"Tanım yalnız yara öznesiyle kurulan kanıtlanmış tamlamaya bağlıdır; yalın biçime genel bozulma anlamı verilmez.","neighbor_coverage_note":"Bütün komşular incelendi; irin birikmesi çekirdeğini en yakından paylaşan ve sonuç bakımından ayrılan kart yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal irin birikimini yaranın kabarıp bozulmasına bağlar; komşu dal yalnız irin toplanması ya da dışarı çıkmasıyla yetinebilir.","focus_only":"Yaranın irinlenmeyle kabarıp bozulması sürecini zorunlu olarak içerir.","gloss":"yarada irin toplanması","neighbor_only":"İrinin yarada toplanmasını veya yaradan çıkmasını, bozulma sonucu aramadan kapsar.","neighbor_ref":"root_001664/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da yaranın içinde irin birikmesi durumunu anlatır."}],"source_phrase_ar":"أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)","source_summary":"Tek kanıt, yara içindeki irinlenme ile kabarma ve bozulmayı birbirine bağlı tek bir hastalık süreci olarak gösterir.","sources":["SI"],"what_is_ar":"أرضت القرحة إذا مجلت وفسدت بالمدة","what_is_not_ar":"ليس الزكام ولا الأرضة ولا الرعدة"},"support_links":[]},{"boundary":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_000025/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","surface_ar":"أَرْضُ"}],"gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Neden yorumunu, akıl durumunu ve belirleyici istemsiz beden hareketini birlikte açıklar.","boundary_detail":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_image_ar":"المأروض المخبول من أهل الأرض","concept_gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","contextual_glosses":[{"applicability":"Kişinin gözlenebilir beden hareketi ön plana çıkarıldığında açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl bozukluğunu ve durumun görünmez varlıkların etkisine bağlanmasını dışarıda bırakır.","preserves":"Baş ve gövdenin bilinçli amaç olmadan hareket etmesi belirtisini korur."},"facet_ids":["F002"],"text":"başıyla gövdesini istemsizce sarsan kişi","usage_role":"explanatory"}],"definition":"Yerle ilişkilendirilen görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğudur; etkilenen kişi başını ve gövdesini isteği dışında hareket ettirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."},{"facet_id":"F002","role":"specialization","statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}],"identity_rationale":"Kaynak ifadesi, görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğunu; kişinin başını ve gövdesini istemeden hareket ettirmesiyle birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi"}],"lexicalization_note":"Tanım yalın kişi nitelemesinin doğaüstü açıklama, akıl bozukluğu ve istemsiz beden hareketi bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğaüstü etkiye bağlanan akıl bozukluğu çekirdeğini en doğrudan paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kaynak ilişkilendirmesi ve istemsiz baş-gövde hareketi gerektirir; komşu dal daha genel bir doğaüstü dokunuş açıklamasıdır.","focus_only":"Yerle ilişkilendirilen görünmez varlıklar açıklamasını ve istemsiz baş-gövde hareketini birlikte taşır.","gloss":"doğaüstü dokunuşa bağlanan akıl karışıklığı","neighbor_only":"Doğaüstü bir dokunuşla açıklanan akıl karışıklığını beden hareketi koşulu olmadan daha genel verir.","neighbor_ref":"root_001423/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da akıl bozukluğunu görünmez bir varlığın etkisiyle açıklayan geleneksel anlayışta buluşur."}],"source_phrase_ar":"المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)","source_summary":"Tek kanıt, doğaüstü varlıklara bağlanan akıl karışıklığını ve istemsiz baş-gövde hareketini aynı kişi durumunun ayrılmaz parçaları olarak verir.","sources":["SI"],"what_is_ar":"المأروض الذي به خبل من الجن وأهل الأرض ويحرك رأسه وجسده على غير عمد","what_is_not_ar":"ليس المزكوم المأروض ولا الخشبة المأروضة"},"support_links":[]},{"boundary":"Çekirdek fiziksel sarsıntılı harekettir; çağın sıkıntıları ve kolay içilen su bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000638/B001","candidate_links":[{"candidate_id":"cand_32649a1bedfdcf77dc2d","lane":"micro"},{"candidate_id":"cand_2d6c90f8e14e997aaf11","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"زُلْزِلُ","morph_features":"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:1:2:1","qac_word_ref":"99:1:2","surface_ar":"زُلْزِلَتِ"},{"lemma_ar":"زِلْزَال","morph_features":"STEM|POS:N|LEM:zilozaAl|ROOT:zlzl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:4:1","qac_word_ref":"99:1:4","surface_ar":"زِلْزَالَ"}],"gloss":"sarsıntılı hareket","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Durağanlığın bozulmasıyla sarsıntılı ve titreşimli bir hareket ortaya çıkar."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerin sarsılması, bu hareketin kaynakta verilen somut gerçekleşmesidir."}}],"root_ar":"ز ل ز ل","root_id":"root_000638","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Durağanlığın bozulup fiziksel bir sarsılma ve titreşime dönüştüğü genel çekirdeği karşılar.","boundary_detail":"Çekirdek fiziksel sarsıntılı harekettir; çağın sıkıntıları ve kolay içilen su bu dala girmez.","branch_image_ar":"اضطراب واهتزاز","concept_gloss":"sarsıntılı hareket","contextual_glosses":[{"applicability":"Bağlam hareketin titreşimli niteliğini açıkça gösterdiğinde genel durum adı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durağanlığın bozulmasını ve sarsıntılı hareketi korur."},"facet_ids":["F001"],"text":"sarsılma","usage_role":"general"},{"applicability":"Hareket eden varlık yer olduğunda kaynakta verilen somut kullanımı doğal biçimde karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerin özne olduğu sarsıntılı hareket örneğini tam olarak korur."},"facet_ids":["F002"],"text":"yerin sarsılması","usage_role":"contextual"}],"definition":"Bir şeyin durağanlığını yitirip sarsıntılı ve titreşimli biçimde hareket etmesi; yerin sarsılması bunun kaynakta verilen somut örneğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Durağanlığın bozulmasıyla sarsıntılı ve titreşimli bir hareket ortaya çıkar."},{"facet_id":"F002","role":"example","statement":"Yerin sarsılması, bu hareketin kaynakta verilen somut gerçekleşmesidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Anlamı belirli bir doğal yer olayına sınırlar.","collision":"Genel sarsılma ile yalnızca yer kabuğundaki olayı birbirine karıştırabilir.","fit":"narrowing","loses":"Yalnız yere bağlı olmayan genel sarsıntılı hareket çekirdeğini kaybeder.","preserves":"Yerin sarsılması biçimindeki somut örneği korur."},"text":"deprem"},{"category":"alternative","error_profile":{"adds":"Toplumsal ya da zihinsel düzensizlik anlamını öne çıkarır.","collision":"Fiziksel hareketi soyut düzensizlikle karıştırır.","fit":"displacement","loses":"Fiziksel sarsılma ve titreşim hareketini kaybeder.","preserves":"Düzenli durumun bozulması yönünü kısmen korur."},"text":"kargaşa"}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan sarsıntılı hareket ve düzenli durumun bozulması olarak verir; yerin sarsılması da bu çekirdeğin somut örneğidir. Hazırlanmış dal çerçevesi bu anlamı, çağın sıkıntıları ve suyun niteliğiyle ilgili öteki dallardan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sarsıntı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerin sarsılması"}],"lexicalization_note":"Tanım genel sarsıntı durumuyla yerin sarsılmasını anlatan yapıyı ayrı tutar; yapıya bağlı örnek bütün dalın tek kapsamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Benzer sarsılma adaylarından yinelenenler, yalnız hız ya da genel hareket bildirenler ve kırıp yıkmayı merkez alan aday seçilmedi; su dalı ise anlam ortaklığı taşımadığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sarsıntılı hareket durumunu adlandırır; komşu dal ise çoğu kullanımında bu hareketi meydana getiren etkin sarsma eylemini öne çıkarır.","focus_only":"Odak dal, sarsıntılı hareketin kendisini bir durum olarak öne çıkarır.","gloss":"sarsarak hareket ettirme","neighbor_only":"Komşu dal, bir şeyi sarsarak hareket ettirme eylemini ve denizin çalkalanmasını da kapsar.","neighbor_ref":"root_000541/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da sarsıntı ve düzenli hareketin bozulması vardır."},{"boundary_match":"partial","distinction":"Komşuda şiddet anlam sınırının parçasıdır; odakta ise temel ölçüt sarsıntılı harekettir ve şiddet zorunlu değildir.","focus_only":"Odak dalın çekirdeği belirli bir şiddet derecesini zorunlu kılmaz.","gloss":"şiddetli sarsılma","neighbor_only":"Komşu dal şiddetli sarsılmayı öne çıkarır ve kalp, deniz, diş ile ağaç gibi geniş bir örnek alanı verir.","neighbor_ref":"root_000545/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın titreşimli ve düzensiz hareketini anlatır."},{"boundary_match":"partial","distinction":"Odaktaki hareket sarsıntılıdır; komşudaki hareket ise sarsıntı olmadan eğilme ya da salınma biçiminde de gerçekleşebilir.","focus_only":"Odak dal, sarsıntı ve titreşim niteliğini merkezde tutar.","gloss":"hareket etme ve salınma","neighbor_only":"Komşu dal eğilme ve salınmayı da kapsayan daha geniş bir hareket alanına sahiptir.","neighbor_ref":"root_001459/B001","relation_type":"near_synonym","shared_zone":"Her iki dal durağanlığın bozulup hareket ve düzensizliğin ortaya çıkmasında buluşur."},{"boundary_match":"partial","distinction":"Komşu çoğunlukla bir şeyi hareket ettirme eylemini anlatırken odak bu eylem sonucunda görülen sarsıntılı durumu adlandırır.","focus_only":"Odak dal meydana gelen sarsıntılı hareket durumunu anlatır.","gloss":"bir şeyi sallama","neighbor_only":"Komşu dal bir nesneyi sallayan etkene, duyulur harekete ve çeşitli hareket eden varlıklara uzanır.","neighbor_ref":"root_001588/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da sallanma, titreşim ve duyulur hareket bulunur."},{"boundary_match":"thematic_only","distinction":"Birinci dal fiziksel harekettir; ikinci dal ise yaşanan ağır sıkıntılara verilen aktarmalı bir addır ve fiziksel sarsıntı bildirmez.","focus_only":"Odak dal gerçek ve fiziksel bir sarsıntılı hareketi anlatır.","gloss":"çağın ağır sıkıntıları","neighbor_only":"Komşu dal yalnız belirli bir ifadede çağın getirdiği ağır sıkıntıları anlatır.","neighbor_ref":"root_000638/B002","relation_type":"thematic","shared_zone":"Her iki dalda düzeni bozan güçlü bir sarsma düşüncesi sezilebilir."}],"source_phrase_ar":"الزلزلة: الاضطراب أخذ من زلزلت الأرض زلزالا","source_qualifications":[{"kind":"sole_attestation","summary":"Sarsıntılı hareket anlamını verir ve yerin sarsılmasını bu anlamın somut dayanağı olarak gösterir."}],"source_summary":"Bu dal için birden fazla kaynak arasında ortaklaştırılacak ayrı bir iddia yoktur.","sources":["JA"],"what_is_ar":"يدخل فيه معنى الزلزلة بوصفها اضطرابا، ومنه زلزلت الأرض زلزالا.","what_is_not_ar":"لا يدخل فيه زلازل الدهر بمعنى الشدائد، ولا ماء زلال أو زلازل بمعنى الماء الصافي السائغ."},"support_links":["sup_2434f755fe567f436990","sup_e5a84824c68fc5490d2e"]},{"boundary":"Anlam çağın getirdiği ağır sıkıntılarla sınırlıdır; fiziksel sarsılma ya da su niteliği bildirmez.","branch_kind":"collocation","branch_ref":"root_000638/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُلْزِلُ","morph_features":"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:1:2:1","qac_word_ref":"99:1:2","surface_ar":"زُلْزِلَتِ"},{"lemma_ar":"زِلْزَال","morph_features":"STEM|POS:N|LEM:zilozaAl|ROOT:zlzl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:4:1","qac_word_ref":"99:1:4","surface_ar":"زِلْزَالَ"}],"gloss":"çağın ağır sıkıntıları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir çağın akışı içinde karşılaşılan ağır sıkıntılar ve yıkıcı olaylar topluca anlatılır."}}],"root_ar":"ز ل ز ل","root_id":"root_000638","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli söz öbeğindeki çoğul ve güçlü sıkıntı anlamını doğal Türkçeyle karşılar.","boundary_detail":"Anlam çağın getirdiği ağır sıkıntılarla sınırlıdır; fiziksel sarsılma ya da su niteliği bildirmez.","branch_image_ar":"شدائد الدهر","concept_gloss":"çağın ağır sıkıntıları","contextual_glosses":[{"applicability":"İfadenin bir dönem boyunca yaşanan güçlü zorlukları anlattığının açıklanması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıkıntıların zaman içinden gelmesi ve ağır olması yönlerini korur."},"facet_ids":["F001"],"text":"zamanın getirdiği ağır sıkıntılar","usage_role":"explanatory"},{"applicability":"Bağlam ağır sıkıntıları yaşayan bir kişi ya da topluluğu açıkça gösterdiğinde doğal bir çeviri olur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Felaket sayılmayabilecek uzun süreli ağır sıkıntıları geri plana iter.","preserves":"Yıkıcı olayların ağırlığını ve yaşanan olumsuzluğu korur."},"facet_ids":["F001"],"text":"başına gelen büyük felaketler","usage_role":"contextual"}],"definition":"Belirli bir söz öbeğinde, bir çağın ya da yaşam döneminin getirdiği ağır sıkıntılar ve yıkıcı olaylar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir çağın akışı içinde karşılaşılan ağır sıkıntılar ve yıkıcı olaylar topluca anlatılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel bir yer hareketi anlamını getirir.","collision":"Bu dalı kökün fiziksel sarsıntı dalıyla karıştırır.","fit":"displacement","loses":"Bir çağ boyunca yaşanan ağır sıkıntılar anlamını kaybeder.","preserves":"Sarsıcı ve yıkıcı etki düşüncesini kısmen korur."},"text":"deprem"},{"category":"alternative","error_profile":{"adds":null,"collision":"Gündelik küçük güçlüklerle ağır sıkıntılar arasındaki farkı silebilir.","fit":"narrowing","loses":"Kaynak ifadesindeki ağırlık ve yıkıcılık derecesini kaybeder.","preserves":"Olumsuz ve güç koşulları genel olarak korur."},"text":"zorluklar"}],"identity_rationale":"Kaynak ifadesi belirli bir çağ ifadesini doğrudan o çağın ağır sıkıntılarıyla açıklar. Hazırlanmış dal bu yapıya bağlı anlamı fiziksel sarsıntıdan ve suyun niteliğini bildiren daldan doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çağın ağır sıkıntıları"}],"lexicalization_note":"Tanım yalnız kaynakta verilen söz öbeğine bağlıdır; ağır sıkıntı anlamı kökün bağımsız ve genel anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Ölüm ve yok oluşu, tekil felaketi ya da açlık, yoksulluk ve borç gibi özel sıkıntıları merkez alan adaylar daha dar oldukları için seçilmedi; su dalında ise anlam ortaklığı yoktur.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Odak dal sıkıntılara verilen aktarmalı bir addır; komşu dal ise bir varlığın gerçekten sarsılıp hareket etmesini bildirir.","focus_only":"Odak dal belirli bir ifadede çağın ağır sıkıntılarını anlatır.","gloss":"fiziksel sarsıntı","neighbor_only":"Komşu dal gerçek ve fiziksel sarsıntılı hareketi anlatır.","neighbor_ref":"root_000638/B001","relation_type":"thematic","shared_zone":"İki dalda da düzeni bozan güçlü bir sarsma düşüncesi sezilebilir."},{"boundary_match":"partial","distinction":"Odak belirli bir söz öbeğinde çağın sıkıntılarını topluca anlatır; komşu ise tekil bir ağır olayı ve daha geniş zaman değişimlerini de adlandırabilir.","focus_only":"Odak dal çoğul sıkıntıları belirli bir çağ ifadesi içinde topluca adlandırır.","gloss":"çağın ağır olayı","neighbor_only":"Komşu dal tek bir ağır olay, genel şiddet ve zamanın değişen yönlerini de kapsar.","neighbor_ref":"root_001378/B006","relation_type":"near_synonym","shared_zone":"Her iki dal çağ içinde karşılaşılan ağır sıkıntı ve yıkıcı olayları anlatır."},{"boundary_match":"partial","distinction":"Odak çağ ifadesine bağlıdır; komşu ise aynı şiddet alanını soğuktan doğan zarar gibi başka nedenlere de genişletir.","focus_only":"Odak dal çağın getirdiği ağır sıkıntıları bir bütün olarak anlatır.","gloss":"ağır sıkıntı","neighbor_only":"Komşu dal zamanın sıkıntısına ek olarak soğuğun insanlara verdiği ağır zararı da kapsar.","neighbor_ref":"root_001289/B005","relation_type":"near_synonym","shared_zone":"İki dal da insanların karşılaştığı ağır ve bunaltıcı güçlükleri kapsar."},{"boundary_match":"partial","distinction":"Komşu genel bir ağır olay adıdır; odak ise anlamını çağa bağlayan belirli söz öbeği içinde birden çok sıkıntıyı toplar.","focus_only":"Odak dal bir çağ boyunca karşılaşılan ağır sıkıntıların çoğul toplamını anlatır.","gloss":"çok ağır olay","neighbor_only":"Komşu dal belirli bir zaman bağı olmadan tek bir çok ağır olay ya da çıkışsız durum bildirebilir.","neighbor_ref":"root_000884/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da şiddetli sıkıntı ve yıkıcı olay anlamı bulunur."},{"boundary_match":"partial","distinction":"Odakta belirleyici olan çağın sıkıntılarıdır; komşuda aynı olumsuzluk bir sınama ya da ceza çerçevesine yerleşebilir.","focus_only":"Odak dal çağın getirdiği ağır sıkıntıları anlatır ve sınanma düşüncesini zorunlu kılmaz.","gloss":"sınayıcı güçlük","neighbor_only":"Komşu dal sınanma, ceza ve kimi zaman rahatlık yoluyla denenme anlamlarını da taşır.","neighbor_ref":"root_001128/B004","relation_type":"near_neighbor","shared_zone":"İki dal da insanın karşılaştığı ağır ve acı verici durumları kapsar."}],"source_phrase_ar":"زلازل الدهر: شدائده","source_qualifications":[{"kind":"sole_attestation","summary":"Belirli çağ ifadesini o çağın getirdiği ağır sıkıntılar olarak açıklar."}],"source_summary":"Bu dal için birden fazla kaynak arasında ortaklaştırılacak ayrı bir iddia yoktur.","sources":["JA"],"what_is_ar":"يدخل فيه التعبير زلازل الدهر بمعنى شدائده.","what_is_not_ar":"لا يدخل فيه اضطراب الأرض ولا وصف الماء الصافي السائغ."},"support_links":[]},{"boundary":"Anlam berraklığı nedeniyle kolay içilen suyla sınırlıdır; yalnız berraklık ya da yalnız tatlılık yeterli değildir.","branch_kind":"collocation","branch_ref":"root_000638/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"زُلْزِلُ","morph_features":"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:1:2:1","qac_word_ref":"99:1:2","surface_ar":"زُلْزِلَتِ"},{"lemma_ar":"زِلْزَال","morph_features":"STEM|POS:N|LEM:zilozaAl|ROOT:zlzl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:4:1","qac_word_ref":"99:1:4","surface_ar":"زِلْزَالَ"}],"gloss":"berrak ve kolay içimli su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Suyun berraklığı, onun boğazdan güçlük çıkarmadan geçmesini ve kolay içilmesini sağlar."}}],"root_ar":"ز ل ز ل","root_id":"root_000638","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Suyun berraklığını ve bu berraklıktan doğan zahmetsiz içimi birlikte karşılar.","boundary_detail":"Anlam berraklığı nedeniyle kolay içilen suyla sınırlıdır; yalnız berraklık ya da yalnız tatlılık yeterli değildir.","branch_image_ar":"ماء صاف سائغ","concept_gloss":"berrak ve kolay içimli su","contextual_glosses":[{"applicability":"Berraklığın kolay içime nasıl bağlandığının açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Berraklık nedenini ve boğazdan zahmetsiz geçiş sonucunu korur."},"facet_ids":["F001"],"text":"boğazdan kolay geçen berrak su","usage_role":"explanatory"},{"applicability":"Suyun içme deneyiminin doğal ve akıcı Türkçeyle verilmek istendiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duru olmayı ve güçlük çekmeden içilebilmeyi korur."},"facet_ids":["F001"],"text":"içimi rahat, duru su","usage_role":"contextual"}],"definition":"Berraklığı sayesinde boğazdan zahmetsizce geçen, kolay içimli su.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Suyun berraklığı, onun boğazdan güçlük çıkarmadan geçmesini ve kolay içilmesini sağlar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Berraklığın sağladığı zahmetsiz yutma ve kolay içim yönünü kaybeder.","preserves":"Suyun gözle algılanan duruluğunu korur."},"text":"berrak su"},{"category":"confusable","error_profile":{"adds":"Tada ya da tuzlu olmama özelliğine dayalı yeni bir ölçüt getirir.","collision":"Berrak ve kolay içimli suyu tat ya da tuzluluk sınıfıyla karıştırabilir.","fit":"displacement","loses":"Berraklık ile boğazdan zahmetsiz geçiş arasındaki bağı kaybeder.","preserves":"İçilmeye elverişli su düşüncesini kısmen korur."},"text":"tatlı su"}],"identity_rationale":"Kaynak ifadesi iki su nitelemesini aynı koşulla açıklar: su, berraklığı sayesinde zahmetsizce içilir. Hazırlanmış dal hem berraklığı hem kolay geçişi korur ve bu anlamı fiziksel sarsıntı ile çağın sıkıntılarından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"berrak ve kolay içimli su"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"berrak ve kolay içimli su"}],"lexicalization_note":"Tanım yalnız suyu niteleyen kaynak yapıları için geçerlidir; berraklık ve kolay içim kökün bağımsız genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Boğazdan kolay geçiş alanında yinelenen aday, su katılmış süt, atılan köpük ve tortu ile yalnız biçim akrabalığı taşıyan iki kardeş dal seçilmedi; bunlar sınırı ek bir yarar sağlamadan genişletiyor ya da anlam ortaklığı taşımıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Su bağlamında çekirdekler çok yakındır; komşu dal ayrıca tatlılığı ve su dışındaki bir parlaklık benzetmesini kapsadığı için sınırı daha geniştir.","focus_only":"Odak dal yalnız suyun berraklıktan ötürü zahmetsiz içilmesini tanımlar.","gloss":"duru ve yumuşak içimli su","neighbor_only":"Komşu dal tatlılığı da suyun niteliğine katar ve berraklığı altına aktaran bir kullanıma uzanır.","neighbor_ref":"root_000641/B003","relation_type":"near_synonym","shared_zone":"İki dal da berrak ve boğazdan kolay geçen suyu merkez alır."},{"boundary_match":"partial","distinction":"Odak berrak suyla ve berraklıktan doğan kolay içimle sınırlıdır; komşu ise çeşitli içecekleri ve akış kolaylığını daha geniş nedenlerle kapsar.","focus_only":"Odak dal suyun berraklığını kolay içimin açık nedeni olarak belirler.","gloss":"yumuşak içim ve akış","neighbor_only":"Komşu dal başka içecekleri, serinlik ve tatlılığı, ayrıca akışın kolaylığını da kapsar.","neighbor_ref":"root_000731/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda içeceğin boğazdan kolay geçmesi ve hoş içimi bulunur."},{"boundary_match":"partial","distinction":"Odakta belirleyici nitelik berraklığın sağladığı kolay geçiştir; komşuda tatlılık ve hoşluk yeterli olabilir ve kapsam suyun dışına çıkabilir.","focus_only":"Odak dal berrak su ile onun boğazdan zahmetsiz geçişi arasındaki bağı zorunlu tutar.","gloss":"tatlı ve hoş su","neighbor_only":"Komşu dal tatlı ve hoş olmayı öne çıkarır, ayrıca yiyecek ve başka içeceklere genişler.","neighbor_ref":"root_000994/B001","relation_type":"near_synonym","shared_zone":"İki dal da içilmesi hoş ve kolay olan su alanında kesişir."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği tatlı ve taze sudur; odakta ise tat ya da tazelikten çok berraklığın sağladığı zahmetsiz içim belirleyicidir.","focus_only":"Odak dal berraklık ve boğazdan zahmetsiz geçiş koşullarını birlikte taşır.","gloss":"tatlı ve taze su","neighbor_only":"Komşu dal suyun tatlı ve taze olmasını anlatır, fakat berraklık ile geçiş kolaylığını zorunlu kılmaz.","neighbor_ref":"root_001137/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal içmeye elverişli ve hoş suyu anlatan aynı alanda bulunur."},{"boundary_match":"field_only","distinction":"Odak içme sırasında boğazdan geçişe ve berraklığa bakar; komşu ise suyun dış dünyadaki akış veya yayılma hareketini anlatır.","focus_only":"Odak dal suyun berraklığından doğan kolay yutulma niteliğini anlatır.","gloss":"akan ya da yayılan su","neighbor_only":"Komşu dal suyun akmasını, dökülmesini ya da çevreye yayılmasını anlatır.","neighbor_ref":"root_001162/B006","relation_type":"same_field","shared_zone":"Her iki dalın merkezinde su bulunur, ancak suya yüklenen özellikler ayrıdır."}],"source_phrase_ar":"ماء زلال وزلازل إذا كان ينساغ بلا كلفة من صفائه","source_qualifications":[{"kind":"sole_attestation","summary":"İki su nitelemesini, berraklık nedeniyle boğazdan zahmetsiz geçme koşulunda birleştirir."}],"source_summary":"Bu dal için birden fazla kaynak arasında ortaklaştırılacak ayrı bir iddia yoktur.","sources":["JA"],"what_is_ar":"يدخل فيه ماء زلال أو زلازل إذا كان ينساغ بلا كلفة من صفائه.","what_is_not_ar":"لا يدخل فيه الزلزلة بمعنى الاضطراب، ولا زلازل الدهر بمعنى الشدائد."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["99:1:1"],"branch_refs":[],"candidate_id":"cand_fd13c00325b383eb3a32","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:1:deferred-response","source_type":"word_analysis","support_ids":["sup_4b4b5bb4a7125e7f272b","sup_91a60b9f523089992766"],"title":"suspended response beyond the first ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:1","qac_refs":["99:1:1:1"],"status":"accepted"}},{"anchor_refs":["99:1:1"],"branch_refs":[],"candidate_id":"cand_86259032caabf4b3716b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:1:future-certain-condition","source_type":"word_analysis","support_ids":["sup_91a60b9f523089992766","sup_9b36de3bda4d03020c6f"],"title":"future certainty in conditional form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:1","qac_refs":["99:1:1:1"],"status":"accepted"}},{"anchor_refs":["99:1:1"],"branch_refs":[],"candidate_id":"cand_4eb8d2c85264465a6a06","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:1:temporal-conditional-double-value","source_type":"word_analysis","support_ids":["sup_91a60b9f523089992766","sup_f9e0f45548082cf8e1fe"],"title":"time and condition stay together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:1","qac_refs":["99:1:1:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_39d97fd3bbb87b1dfa4d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:audible-oscillation","source_type":"word_analysis","support_ids":["sup_6919449925e7bc6b46e3","sup_a283c846eb37f0025273"],"title":"sound performs oscillation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_64d60ec93187fef08d3b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:conditioned-core-event","source_type":"word_analysis","support_ids":["sup_a283c846eb37f0025273","sup_f958786c985874a5a65c"],"title":"first content beat after the frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_1bb7712ab4e41e6d711e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:convergent-passive-quake","source_type":"word_analysis","support_ids":["sup_1b042b93158a1db05045","sup_a283c846eb37f0025273"],"title":"passive, rarity, sound, and motion converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_73309158e285f0c62879","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:passive-earth-binding","source_type":"word_analysis","support_ids":["sup_a283c846eb37f0025273","sup_af79a5c7800acd9fee7d"],"title":"passive foregrounds earth, not agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_92171c3f8a9fbee760f9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:rare-crisis-distribution","source_type":"word_analysis","support_ids":["sup_60248f492c81da11fb6e","sup_a283c846eb37f0025273"],"title":"rare root carries crisis pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_d06a57339f1689ec9a64","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:reduplicated-kinetic-shaking","source_type":"word_analysis","support_ids":["sup_1d7e61adf3410c5eeafd","sup_a283c846eb37f0025273"],"title":"reduplication makes shaking iterative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_7c62cc56b5b6ee078f51","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:stability-disruption","source_type":"word_analysis","support_ids":["sup_5cfc156fafa2828759fc","sup_a283c846eb37f0025273"],"title":"shaking opposes security","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_0bda1127434112479631","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:verb-noun-echo","source_type":"word_analysis","support_ids":["sup_43e5563a6a2c3d0238bd","sup_a283c846eb37f0025273"],"title":"verb anticipates its cognate measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:2","qac_refs":["99:1:2:1"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_ab81d0e8d9af8d57365f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:article-knownness-form","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_609e8a9f5e80009439e5"],"title":"knownness is carried in the form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_d1379b8cb35259e1eecc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:audible-verb-subject-join","source_type":"word_analysis","support_ids":["sup_1bfd7e1fce757c51962e","sup_46facc2d5f7235dd2549"],"title":"recitation joins verb to subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_f8f546651188f4cad5af","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:definite-total-earth","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_7ef3fe1a56e9d1f9a969"],"title":"definite singular makes one known earth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_5d20b0be3336dd7b68c7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:earth-to-possessor-pivot","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_e0a5ac4aa2b4b2de970d"],"title":"earth becomes possessor of the quake","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_e43b4efe5e269b978015","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:ground-stability-overturned","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_a4e1b223d7b4d5df8ca4"],"title":"stable ground becomes shaken substrate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_7a03e1141590ea7476ee","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:promoted-passive-subject","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_c8f45dd2109e7177e308"],"title":"earth is promoted as patient-subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_de498206df9567287f93","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:surah-thread-patient-to-reporter","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_63169069a4c44d5a7d77"],"title":"earth carries the surah thread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_0b9f673300c7798f7090","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"99:1:3:terrestrial-focus-without-sky","source_type":"word_analysis","support_ids":["sup_46facc2d5f7235dd2549","sup_56b2a91b8400934a2550"],"title":"no sky counterpart broadens the earth focus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:3","qac_refs":["99:1:3:1","99:1:3:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_07c4d2b04d210c7709e7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:acoustic-saturation","source_type":"word_analysis","support_ids":["sup_9b41cb6848952a6a5e1e","sup_fc025676ab3a43f604c8"],"title":"quake sound saturates the ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_f5007b26baec56cb5b8b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:closure-ring-echo","source_type":"word_analysis","support_ids":["sup_5322b476599e98e849d4","sup_9b41cb6848952a6a5e1e"],"title":"final noun closes the root ring","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_67573c6d8b5979ebffcf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:cognate-accusative-measure","source_type":"word_analysis","support_ids":["sup_9b41cb6848952a6a5e1e","sup_cef5be500939bbd802e3"],"title":"verbal noun measures the verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_5e4f84d2c8e97b72254a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:earth-specific-possession","source_type":"word_analysis","support_ids":["sup_499354c75f8aa829e2bc","sup_9b41cb6848952a6a5e1e"],"title":"suffix binds quake to earth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_13697c069cc64ae5745d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:final-layer-convergence","source_type":"word_analysis","support_ids":["sup_1227cbe991485f691830","sup_9b41cb6848952a6a5e1e"],"title":"grammar, suffix, echo, and closure meet","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_dea95931e2643cb470e3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:qiraat-process-event-pressure","source_type":"word_analysis","support_ids":["sup_30956bd325b396352e7e","sup_9b41cb6848952a6a5e1e"],"title":"vowel contrast exposes process and event pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_6b81927a3e92e69e965d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:rare-gerund-field","source_type":"word_analysis","support_ids":["sup_0560139df27173c9dde4","sup_9b41cb6848952a6a5e1e"],"title":"small gerund class carries weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:4"],"branch_refs":[],"candidate_id":"cand_3a3ba0a85f73f4d36917","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:4:root-family-loading","source_type":"word_analysis","support_ids":["sup_9b41cb6848952a6a5e1e","sup_f5097dde16936f4469dc"],"title":"noun loads the previous verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"99:1:4","qac_refs":["99:1:4:1","99:1:4:2"],"status":"accepted"}},{"anchor_refs":["99:1:2"],"branch_refs":[],"candidate_id":"cand_4b7714699b79326eb372","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000638"],"scope":"focus_ayah","source_local_id":"99:1:2:1","source_type":"qac_morpheme","support_ids":["sup_bcf23b435295eda8a4bb"],"title":"QAC root occurrence: ز ل ز ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:1:3"],"branch_refs":[],"candidate_id":"cand_87717ac7b8306ff98edf","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000025"],"scope":"focus_ayah","source_local_id":"99:1:3:2","source_type":"qac_morpheme","support_ids":["sup_873cacb5bad93852b865"],"title":"QAC root occurrence: ء ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["99:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:1","branch_refs":["root_000025/B001","root_000638/B001"],"candidate_id":"cand_32649a1bedfdcf77dc2d","commentary_obligation":"review","hft_ref":"hft_d08cd4aea323d2fad823","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b1_totalizing_ground_convulsion","source_type":"hft","support_ids":["sup_2434f755fe567f436990"],"title":"b1_totalizing_ground_convulsion","trust":"legacy_unbound"},{"anchor_refs":["99:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"99:1","branch_refs":["root_000025/B006","root_000638/B001"],"candidate_id":"cand_2d6c90f8e14e997aaf11","commentary_obligation":"review","hft_ref":"hft_e40d9b425bedb0a5996d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b2_support_function_reversed","source_type":"hft","support_ids":["sup_e5a84824c68fc5490d2e"],"title":"b2_support_function_reversed","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا","qac_morphemes":[{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"99:1:1:1","qac_word_ref":"99:1:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"زُلْزِلُ","morph_features":"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:1:2:1","qac_word_ref":"99:1:2","root_ar":"ز ل ز ل","surface_ar":"زُلْزِلَتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"99:1:3:1","qac_word_ref":"99:1:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"زِلْزَال","morph_features":"STEM|POS:N|LEM:zilozaAl|ROOT:zlzl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:4:1","qac_word_ref":"99:1:4","root_ar":"ز ل ز ل","surface_ar":"زِلْزَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:1:4:2","qac_word_ref":"99:1:4","root_ar":"","surface_ar":"هَا"}],"word_analysis_qac_refs":[["99:1:1:1"],["99:1:2:1"],["99:1:3:1","99:1:3:2"],["99:1:4:1","99:1:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["99:1:1","99:1:2","99:1:3","99:1:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا","qac_morphemes":[{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"99:1:1:1","qac_word_ref":"99:1:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"زُلْزِلُ","morph_features":"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"99:1:2:1","qac_word_ref":"99:1:2","root_ar":"ز ل ز ل","surface_ar":"زُلْزِلَتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"99:1:3:1","qac_word_ref":"99:1:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:3:2","qac_word_ref":"99:1:3","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"زِلْزَال","morph_features":"STEM|POS:N|LEM:zilozaAl|ROOT:zlzl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"99:1:4:1","qac_word_ref":"99:1:4","root_ar":"ز ل ز ل","surface_ar":"زِلْزَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"99:1:4:2","qac_word_ref":"99:1:4","root_ar":"","surface_ar":"هَا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["99:1:1:1"],["99:1:2:1"],["99:1:3:1","99:1:3:2"],["99:1:4:1","99:1:4:2"]],"word_analysis_refs":["99:1:1","99:1:2","99:1:3","99:1:4"],"word_rows":[{"analysis_record_ref":"99:1:1","analytic_gloss_range_en":"temporal-conditional opener that frames the following perfect passive as a certain future condition whose response is still pending","analytic_root_gloss_range_en":null,"qac_refs":["99:1:1:1"],"root":{},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"99:1:2","analytic_gloss_range_en":"perfect passive, third feminine singular; an earth-bound shaking event under the opening temporal condition, with the external agent suppressed","analytic_root_gloss_range_en":"local branch is violent shaking or disturbance; wider accepted branches such as time's shocks or clear water slipping down are not locally activated by this passive verb","qac_refs":["99:1:2:1"],"root":{"arabic":"ز ل ز ل","transliteration":"z-l-z-l"},"surface":{"arabic":"زُلْزِلَتِ","transliteration":"zulzilat"}},{"analysis_record_ref":"99:1:3","analytic_gloss_range_en":"the definite singular earth as the nominative passive subject and continuing referent for the possessed shaking","analytic_root_gloss_range_en":"ground, land, soil, territory, and earth are possible ranges, but this definite singular passive-subject context narrows the local sense to the whole terrestrial realm","qac_refs":["99:1:3:1","99:1:3:2"],"root":{"arabic":"أ ر ض","transliteration":"ʾ-r-ḍ"},"surface":{"arabic":"ٱلْأَرْضُ","transliteration":"al-arḍu"}},{"analysis_record_ref":"99:1:4","analytic_gloss_range_en":"possessed verbal noun in accusative cognate function, measuring and intensifying the same shaking while binding it to earth","analytic_root_gloss_range_en":"local branch is shaking or disturbance in a maṣdar/cognate-accusative construction; accepted wider branches such as hardships of time and clear slipping water do not control this local noun","qac_refs":["99:1:4:1","99:1:4:2"],"root":{"arabic":"ز ل ز ل","transliteration":"z-l-z-l"},"surface":{"arabic":"زِلْزَالَهَا","transliteration":"zilzālahā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["99:1"],"branch_refs":["root_000025/B001","root_000638/B001"],"candidate_id":"cand_32649a1bedfdcf77dc2d","evidence_scope":"focus_ayah","hft_ref":"hft_d08cd4aea323d2fad823","item_id":"b1_totalizing_ground_convulsion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b1_totalizing_ground_convulsion","support_id":"sup_2434f755fe567f436990"},{"anchor_refs":["99:1"],"branch_refs":["root_000025/B006","root_000638/B001"],"candidate_id":"cand_2d6c90f8e14e997aaf11","evidence_scope":"focus_ayah","hft_ref":"hft_e40d9b425bedb0a5996d","item_id":"b2_support_function_reversed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b2_support_function_reversed","support_id":"sup_e5a84824c68fc5490d2e"}],"diagnostics":[],"lane_counts":{"global":7,"macro":7,"micro":2},"packet_summary":{"ayah_count":8,"focus_ref":"99:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ذ ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000511","furuq_root_norm":"ذ ر ر","furuq_source_root_norm":"ذ ر ر","is_dominant":true,"target_occurrences":2,"target_rank":1}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]}],"window":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"99:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":9,"unstructured_record_count":0},"identity":{"ayah_ref":"99:1","lane":"micro","linguistic_source_ref":"99:1","surface_ref":"99:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"99:1","target_tokens":[["Yer",["99:1:3"]],["kendi",["99:1:4"]],["sarsıntısıyla",["99:1:4"]],["sarsıldığında",["99:1:1","99:1:2"]]],"text":"Yer kendi sarsıntısıyla sarsıldığında,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s099-p01-001-008","label":"Whole surah","number":1,"refs":["99:1","99:2","99:3","99:4","99:5","99:6","99:7","99:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:rare-gerund-field","source_type":"word_analysis","support_id":"sup_0560139df27173c9dde4","text":"{\"blocking_evidence\":null,\"headline\":\"small gerund class carries weight\",\"reader_payoff\":\"The reader notices that the final noun belongs to a small marked field, so the root repetition in this four-word opening is concentrated rather than routine.\",\"reason\":\"Contextual evidence marks the gerund and passive classes as low-occurrence and supports comparison with 2:214, 22:1, and 33:11.\",\"representative_source_ids\":[\"QI-27e0e4c9\",\"QI-c33e1503\",\"QI-eb3fc01a\",\"QI-f5d7bbd4\",\"QH-34ab58e7\",\"QH-a6829cab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:final-layer-convergence","source_type":"word_analysis","support_id":"sup_1227cbe991485f691830","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, suffix, echo, and closure meet\",\"reader_payoff\":\"The reader sees why the final word is dense: it measures the verb, binds the quake to earth, reprises the root, and closes the ayah at once.\",\"reason\":\"All four elements are independently supported by local grammar and CRITICAL rows, so the convergence is preserved as a reader-facing payoff.\",\"representative_source_ids\":[\"QY-806a8efa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:convergent-passive-quake","source_type":"word_analysis","support_id":"sup_1b042b93158a1db05045","text":"{\"blocking_evidence\":null,\"headline\":\"passive, rarity, sound, and motion converge\",\"reader_payoff\":\"The reader sees the word as a convergence of suppressed agency, repeated motion, audible oscillation, and rare quake vocabulary.\",\"reason\":\"The convergence survives, but any implication about who imposes the event is limited to the grammatically suppressed agent.\",\"representative_source_ids\":[\"QY-fbee2341\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:audible-verb-subject-join","source_type":"word_analysis","support_id":"sup_1bfd7e1fce757c51962e","text":"{\"blocking_evidence\":null,\"headline\":\"recitation joins verb to subject\",\"reader_payoff\":\"The reader hears the passive verb run into the definite subject, making their dependency audible.\",\"reason\":\"The phonetic claim supports the already forced verb-subject dependency and does not create a separate grammatical relation.\",\"representative_source_ids\":[\"QP-61787e46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:reduplicated-kinetic-shaking","source_type":"word_analysis","support_id":"sup_1d7e61adf3410c5eeafd","text":"{\"blocking_evidence\":null,\"headline\":\"reduplication makes shaking iterative\",\"reader_payoff\":\"The reader notices a repeated, oscillatory motion in the root form itself, so the verb feels like convulsion rather than a single static shock.\",\"reason\":\"The kinetic reduplication payoff survives, while V4 narrows local activation to the shaking-disturbance branch rather than activating the time-shock or clear-water branches.\",\"representative_source_ids\":[\"QS-321b9131\",\"QS-5298e037\",\"MS-6273d0bc\",\"MF-3f26c417\",\"QP-8bb4d971\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:qiraat-process-event-pressure","source_type":"word_analysis","support_id":"sup_30956bd325b396352e7e","text":"{\"blocking_evidence\":null,\"headline\":\"vowel contrast exposes process and event pressure\",\"reader_payoff\":\"The reader notices that the surface verbal noun can be heard against a variant that leans toward event naming, without letting the variant replace the local form.\",\"reason\":\"The accepted qirāʾa contrast is useful for process-event pressure, but canonical local parsing remains the supplied surface maṣdar.\",\"representative_source_ids\":[\"MG-460d86dc\",\"QS-732e8c4a\",\"QS-f3d8de0d\",\"QF-09584f62\",\"QP-51b89e64\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:verb-noun-echo","source_type":"word_analysis","support_id":"sup_43e5563a6a2c3d0238bd","text":"{\"blocking_evidence\":null,\"headline\":\"verb anticipates its cognate measure\",\"reader_payoff\":\"The reader hears the finite verb already preparing the matching final noun, so the quake continues across the ayah instead of stopping at the verb.\",\"reason\":\"Attachment evidence confirms the final noun as a cognate accusative from the same root, supporting the local echo claim.\",\"representative_source_ids\":[\"QE-050cf954\",\"QE-7380e358\",\"QP-4a1c3a0f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3","source_type":"word_analysis","support_id":"sup_46facc2d5f7235dd2549","text":"{\"gloss_range\":\"the definite singular earth as the nominative passive subject and continuing referent for the possessed shaking\",\"prose\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}}) is not an ordinary object after the verb; it is nominative passive subject, the named patient around which the clause is built. Its feminine singular agreement with {{ar:زُلْزِلَتِ}} ({{tr:zulzilat}}) locks the quake to one definite earth, and its placement between verb and cognate noun makes it the hinge between event and measure. The article and singular form narrow the range from land, soil, or region to the known terrestrial whole. That matters because the normally stable ground, floor, and settling-place is the thing being destabilized, and the common earth term becomes marked by the rare {{ar:ز ل ز ل}} ({{tr:z-l-z-l}}) event. The same referent then returns compactly through the hā suffix in {{ar:زِلْزَالَهَا}} ({{tr:zilzālahā}}), so the earth moves from passive subject to possessor of the quake's defining noun. Within the surah, this begins a local thread: earth recurs at 99:2 and the shaken substrate becomes the reporting surface at 99:4, so a place of settling and storage turns toward disclosure. The usual sky-earth pairing is absent here, keeping the frame concentrated on the terrestrial field rather than a vertical cosmos.\",\"root_display\":\"{{ar:أ ر ض}} ({{tr:ʾ-r-ḍ}})\",\"root_gloss_range\":\"ground, land, soil, territory, and earth are possible ranges, but this definite singular passive-subject context narrows the local sense to the whole terrestrial realm\",\"surface_display\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:earth-specific-possession","source_type":"word_analysis","support_id":"sup_499354c75f8aa829e2bc","text":"{\"blocking_evidence\":null,\"headline\":\"suffix binds quake to earth\",\"reader_payoff\":\"The reader notices that the quake is grammatically possessed by earth, making the final noun earth-specific rather than abstract.\",\"reason\":\"The possessive suffix and same-ayah antecedent are supported, while the claim of intrinsic predetermined destiny is narrowed to grammatical possession and affectedness.\",\"representative_source_ids\":[\"QG-0ebd38ac\",\"QG-c05c66e8\",\"QG-c6e35a1c\",\"QS-5d107a0f\",\"MS-b71ee43e\",\"QF-905a5301\",\"QF-ea767359\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:1:deferred-response","source_type":"word_analysis","support_id":"sup_4b4b5bb4a7125e7f272b","text":"{\"blocking_evidence\":null,\"headline\":\"suspended response beyond the first ayah\",\"reader_payoff\":\"The reader notices that the first word launches a scenario whose resolution is delayed, making the surah begin in syntactic suspense.\",\"reason\":\"The deferred-response claim survives, but the evidence gives candidates at 99:4, 99:6, or elision, so it is narrowed away from naming 99:6 as the only possible response.\",\"representative_source_ids\":[\"QT-34d9b870\",\"QT-db7ef1e2\",\"MT-64253f24\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:closure-ring-echo","source_type":"word_analysis","support_id":"sup_5322b476599e98e849d4","text":"{\"blocking_evidence\":null,\"headline\":\"final noun closes the root ring\",\"reader_payoff\":\"The reader notices that the ayah ends by returning to the root that opened the event, making the quake both entry and closure.\",\"reason\":\"The local sequence begins the event with the passive verb, places earth between, and closes on the possessed cognate noun.\",\"representative_source_ids\":[\"QT-1ee08cc4\",\"QT-a9d5691a\",\"MT-cb234969\",\"QE-dab6e9cd\",\"QE-f5f037c2\",\"QY-861617d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:terrestrial-focus-without-sky","source_type":"word_analysis","support_id":"sup_56b2a91b8400934a2550","text":"{\"blocking_evidence\":null,\"headline\":\"no sky counterpart broadens the earth focus\",\"reader_payoff\":\"The reader notices that a familiar sky-earth pairing is withheld, concentrating the scene on earth as the affected domain.\",\"reason\":\"The contextual collocation profile shows common sky-earth pairing, while the local ayah names only earth.\",\"representative_source_ids\":[\"QI-aec14ad2\",\"ME-6a43835e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:stability-disruption","source_type":"word_analysis","support_id":"sup_5cfc156fafa2828759fc","text":"{\"blocking_evidence\":null,\"headline\":\"shaking opposes security\",\"reader_payoff\":\"The reader notices that the verb overturns the expected stability of earth by placing it in a field of disturbed security and settlement.\",\"reason\":\"The row's security contrast coheres with the local patient being the earth and with the accepted shaking-disturbance branch.\",\"representative_source_ids\":[\"QI-cb7690fe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:rare-crisis-distribution","source_type":"word_analysis","support_id":"sup_60248f492c81da11fb6e","text":"{\"blocking_evidence\":null,\"headline\":\"rare root carries crisis pressure\",\"reader_payoff\":\"The reader notices that this is marked quake vocabulary, linked with a small Quranic field of cosmic and communal crisis rather than routine motion.\",\"reason\":\"The contextual evidence marks the root and passive class as low-occurrence and provides the crisis field across 2:214, 22:1, and 33:11.\",\"representative_source_ids\":[\"QS-b19530bf\",\"QI-3ff1fd7f\",\"QI-90292d97\",\"MI-faad5577\",\"QH-a56233ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:article-knownness-form","source_type":"word_analysis","support_id":"sup_609e8a9f5e80009439e5","text":"{\"blocking_evidence\":null,\"headline\":\"knownness is carried in the form\",\"reader_payoff\":\"The reader notices that definiteness is not an added comment but part of the word's visible form.\",\"reason\":\"The article is part of the surface noun and coheres with the definite singular reading.\",\"representative_source_ids\":[\"QF-d120748d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:surah-thread-patient-to-reporter","source_type":"word_analysis","support_id":"sup_63169069a4c44d5a7d77","text":"{\"blocking_evidence\":null,\"headline\":\"earth carries the surah thread\",\"reader_payoff\":\"The reader notices that the same earth begins as shaken substrate, recurs at 99:2, and moves toward reporting and disclosure at 99:4.\",\"reason\":\"The same-surah evidence supports recurrence at 99:2 and the later reporting role at 99:4, preserving the patient-to-reporter arc.\",\"representative_source_ids\":[\"QS-b7a91dad\",\"QS-c9c8323d\",\"MS-16edd1d3\",\"QI-b06117f2\",\"QE-9981755e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:audible-oscillation","source_type":"word_analysis","support_id":"sup_6919449925e7bc6b46e3","text":"{\"blocking_evidence\":null,\"headline\":\"sound performs oscillation\",\"reader_payoff\":\"The reader notices that the alternating sound texture makes the repeated shaking felt in the word's surface.\",\"reason\":\"The phonetic claim reinforces the locally accepted shaking-disturbance sense and does not alter grammar or branch selection.\",\"representative_source_ids\":[\"QP-f59bfee4\",\"MP-fe384c7a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:definite-total-earth","source_type":"word_analysis","support_id":"sup_7ef3fe1a56e9d1f9a969","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular makes one known earth\",\"reader_payoff\":\"The reader notices that the ayah does not speak of a patch of land or one territory, but of the known earth as a single affected field.\",\"reason\":\"The definite singular form and cosmic shaking context support total-earth scope; missing V4 rows for this root are not negative evidence.\",\"representative_source_ids\":[\"QG-c889ae74\",\"QS-fe239d77\",\"QF-69e2a34a\",\"MT-a03cf0a9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:1:3:2","source_type":"qac_morpheme","support_id":"sup_873cacb5bad93852b865","text":"{\"lemma_ar\":\"أَرْض\",\"morph_features\":\"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"99:1:3:2\",\"qac_word_ref\":\"99:1:3\",\"root_ar\":\"ء ر ض\",\"surface_ar\":\"أَرْضُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:1","source_type":"word_analysis","support_id":"sup_91a60b9f523089992766","text":"{\"gloss_range\":\"temporal-conditional opener that frames the following perfect passive as a certain future condition whose response is still pending\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) opens the surah by putting the quake into a temporal condition rather than a bare report. With the perfect passive {{ar:زُلْزِلَتِ}} ({{tr:zulzilat}}) after it, the event is framed as future-certain: the wording says when the quake-condition arrives, not if it might arrive. The particle also leaves the syntax suspended, because this first ayah gives the protasis while the answer is structurally awaited; the supplied evidence allows the response to be heard around 99:4, 99:6, or as an elided completion, so the opening should not be flattened into a self-contained timestamp. Its payoff is a threshold effect: certainty begins immediately, but resolution is deferred beyond the first line.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:1:future-certain-condition","source_type":"word_analysis","support_id":"sup_9b36de3bda4d03020c6f","text":"{\"blocking_evidence\":null,\"headline\":\"future certainty in conditional form\",\"reader_payoff\":\"The reader notices that the opening is conditional in shape but certain in force, so the quake is presented as an arriving event rather than a possible one.\",\"reason\":\"QAC identifies a temporal conditional particle governing a following perfect passive, and attachment support confirms that the particle opens the condition frame.\",\"representative_source_ids\":[\"QG-afe1b74f\",\"QG-ca4d122c\",\"MG-7ba4c7b5\",\"QS-ce4f103c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4","source_type":"word_analysis","support_id":"sup_9b41cb6848952a6a5e1e","text":"{\"gloss_range\":\"possessed verbal noun in accusative cognate function, measuring and intensifying the same shaking while binding it to earth\",\"prose\":\"{{ar:زِلْزَالَهَا}} ({{tr:zilzālahā}}) closes the ayah by turning the finite shaking into its own measure. As a maṣdar in cognate accusative function, it does not add a second object or a new event; it intensifies the same action named by {{ar:زُلْزِلَتِ}} ({{tr:zulzilat}}). The hā suffix makes the shaking earth-specific: the final word is not a generic earthquake label but the earth's own shaking, with the idafa keeping earth as both bearer of the quake and affected target, though that possession should be read grammatically rather than as a claim about hidden destiny. The qirāʾa contrast with {{ar:زَلْزَالَهَا}} ({{tr:zalzālahā}}) keeps a process-event pressure visible, and its changed opening vowel slightly shifts the onset weight while the canonical surface remains the local form. Distributionally, the gerund class is small and load-bearing, with the root field touching 2:214, 22:1, and 33:11. Structurally and acoustically, the final noun reprises the opening quake-root, shifts from passive verb to possessed accusative noun, and lands as the last beat; its repeated z and l around the long ā leave the ayah folding back onto the sound and measure of shaking itself.\",\"root_display\":\"{{ar:ز ل ز ل}} ({{tr:z-l-z-l}})\",\"root_gloss_range\":\"local branch is shaking or disturbance in a maṣdar/cognate-accusative construction; accepted wider branches such as hardships of time and clear slipping water do not control this local noun\",\"surface_display\":\"{{ar:زِلْزَالَهَا}} ({{tr:zilzālahā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2","source_type":"word_analysis","support_id":"sup_a283c846eb37f0025273","text":"{\"gloss_range\":\"perfect passive, third feminine singular; an earth-bound shaking event under the opening temporal condition, with the external agent suppressed\",\"prose\":\"{{ar:زُلْزِلَتِ}} ({{tr:zulzilat}}) is the first content word after {{ar:إِذَا}} ({{tr:idhā}}), so the surah moves straight from the temporal frame into the quake-event. Its perfect passive form makes {{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}}) the affected grammatical subject while leaving the external agent unnamed; the grammar should not be expanded by adding an explanatory actor. The feminine singular ending and recitational flow into {{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}}) bind the verb to that earth-subject before the final cognate noun arrives. The reduplicated {{ar:ز ل ز ل}} ({{tr:z-l-z-l}}) root makes the motion iterative and bodily: not a mild disturbance, but repeated destabilizing convulsion; the alternating z and l texture makes that back-and-forth motion audible in the word's surface. V4 keeps the local branch to shaking or disturbance, while the broader accepted branches of time's shocks and easy-slipping water remain outside the local sense. The root is also rare and crisis-marked across 2:214, 22:1, and 33:11, so this passive verb carries both cosmic shaking and undergone upheaval. Against the security-and-settlement pressure noted in the field, the stable earth is recast as a destabilized domain. Its sound returns in {{ar:زِلْزَالَهَا}} ({{tr:zilzālahā}}), turning the verb's action into the measure that will close the ayah.\",\"root_display\":\"{{ar:ز ل ز ل}} ({{tr:z-l-z-l}})\",\"root_gloss_range\":\"local branch is violent shaking or disturbance; wider accepted branches such as time's shocks or clear water slipping down are not locally activated by this passive verb\",\"surface_display\":\"{{ar:زُلْزِلَتِ}} ({{tr:zulzilat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:ground-stability-overturned","source_type":"word_analysis","support_id":"sup_a4e1b223d7b4d5df8ca4","text":"{\"blocking_evidence\":null,\"headline\":\"stable ground becomes shaken substrate\",\"reader_payoff\":\"The reader notices that the scene targets the very ground normally imagined as stable, making its stability visibly fail under the rare quake event.\",\"reason\":\"The ground and stability contrast survives, but the creation-context comparison to 2:22 and 21:30 is kept as contrast rather than as a claim that this ayah reverses creation itself.\",\"representative_source_ids\":[\"QS-7532a8ac\",\"QI-d79d9aac\",\"MI-6bde96f2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:passive-earth-binding","source_type":"word_analysis","support_id":"sup_af79a5c7800acd9fee7d","text":"{\"blocking_evidence\":null,\"headline\":\"passive foregrounds earth, not agent\",\"reader_payoff\":\"The reader notices that the grammar concentrates attention on the earth as the affected subject while the cause remains structurally unspoken.\",\"reason\":\"The passive and feminine agreement are secure, but the row that names a divine agent is narrowed because the supplied grammar marks the agent as suppressed and unresolved.\",\"representative_source_ids\":[\"QG-a97c06ff\",\"QG-e6e202c1\",\"MG-5610e4d5\",\"QF-389cb18a\",\"QF-c3dfb8d8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"99:1:2:1","source_type":"qac_morpheme","support_id":"sup_bcf23b435295eda8a4bb","text":"{\"lemma_ar\":\"زُلْزِلُ\",\"morph_features\":\"STEM|POS:V|PERF|PASS|LEM:zulozilu|ROOT:zlzl|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"99:1:2:1\",\"qac_word_ref\":\"99:1:2\",\"root_ar\":\"ز ل ز ل\",\"surface_ar\":\"زُلْزِلَتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:promoted-passive-subject","source_type":"word_analysis","support_id":"sup_c8f45dd2109e7177e308","text":"{\"blocking_evidence\":null,\"headline\":\"earth is promoted as patient-subject\",\"reader_payoff\":\"The reader notices that earth is not merely mentioned after the quake; grammar promotes it as the clause's affected subject and structural center.\",\"reason\":\"QAC and attachment evidence mark the noun as nominative passive subject of the preceding passive verb.\",\"representative_source_ids\":[\"QG-3b9b53e9\",\"QG-a346f55a\",\"QT-c0d17349\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:cognate-accusative-measure","source_type":"word_analysis","support_id":"sup_cef5be500939bbd802e3","text":"{\"blocking_evidence\":null,\"headline\":\"verbal noun measures the verb\",\"reader_payoff\":\"The reader notices that the final noun is not a second event but the same shaking measured, intensified, and named from itself.\",\"reason\":\"Attachment evidence syntactically forces the final maṣdar as cognate accusative of the preceding passive verb.\",\"representative_source_ids\":[\"QG-6c65e93b\",\"MG-ec695a4e\",\"QF-38a3cbc9\",\"QE-29a8d5ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:3:earth-to-possessor-pivot","source_type":"word_analysis","support_id":"sup_e0a5ac4aa2b4b2de970d","text":"{\"blocking_evidence\":null,\"headline\":\"earth becomes possessor of the quake\",\"reader_payoff\":\"The reader notices the same referent moving from named subject to compact suffix, so the final shaking is earth-specific without repeating the noun.\",\"reason\":\"Attachment evidence marks the final suffix as a possessive element on the maṣdar, and the critical rows route it back to the same earth.\",\"representative_source_ids\":[\"QG-474a7839\",\"QT-0276adf3\",\"QE-07b27373\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:root-family-loading","source_type":"word_analysis","support_id":"sup_f5097dde16936f4469dc","text":"{\"blocking_evidence\":null,\"headline\":\"noun loads the previous verb\",\"reader_payoff\":\"The reader notices that the final noun defines the previous verb from inside the same motion-family.\",\"reason\":\"The same accepted shaking-disturbance branch underlies both the passive verb and the maṣdar.\",\"representative_source_ids\":[\"QS-e30b57d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:2:conditioned-core-event","source_type":"word_analysis","support_id":"sup_f958786c985874a5a65c","text":"{\"blocking_evidence\":null,\"headline\":\"first content beat after the frame\",\"reader_payoff\":\"The reader notices that the quake is not background scenery; it is the event-nucleus launched immediately after the temporal opener.\",\"reason\":\"The verb falls under the opening conditional particle and organizes the following subject and cognate accusative.\",\"representative_source_ids\":[\"QG-8c850881\",\"QT-7aff1e25\",\"QT-dfa221b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:1:temporal-conditional-double-value","source_type":"word_analysis","support_id":"sup_f9e0f45548082cf8e1fe","text":"{\"blocking_evidence\":null,\"headline\":\"time and condition stay together\",\"reader_payoff\":\"The reader notices that the word both locates the quake in time and makes later movement depend on that quake-condition.\",\"reason\":\"The local syntax supports both temporal framing and conditional scope, so neither value should be reduced away.\",\"representative_source_ids\":[\"QS-60597928\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"99:1:4:acoustic-saturation","source_type":"word_analysis","support_id":"sup_fc025676ab3a43f604c8","text":"{\"blocking_evidence\":null,\"headline\":\"quake sound saturates the ayah\",\"reader_payoff\":\"The reader hears the repeated root texture lingering at the end, so the ayah sounds like the motion it names.\",\"reason\":\"The acoustic claim reinforces the locally active shaking-disturbance branch and the same-root recurrence.\",\"representative_source_ids\":[\"ME-6232096a\",\"QP-37a3fd56\",\"QP-90ce8414\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا","ayah_ref":"99:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000638/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000638","role":"Shaking disturbance supplies the literal motion, and its verb-noun repetition intensifies that motion into the event's defining action.","root":"ز ل ز ل","source_ref":"99:1","source_word_indices":["2","4"]},{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground opposite the sky supplies the affected world-support, giving the disturbance a total terrestrial field.","root":"ء ر ض","source_ref":"99:1","source_word_indices":["3"]}],"changed_reading":{"after":"The whole lower support is made to undergo its own defining and fully realized convulsion.","before":"A tremor happens to the ground."},"confidence":"strong","focus_anchor":"The repeated root in `زُلْزِلَت ... زِلْزَالَهَا` joins a passive verb to its possessed cognate noun, with `الأرض` as the affected subject.","mechanism":"The ordinary lower support is acted upon, while the cognate construction makes the disturbance exhaustive and proper to this earth rather than a passing tremor.","model_id":"b1_totalizing_ground_convulsion"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b1_totalizing_ground_convulsion","source_type":"hft","support_id":"sup_2434f755fe567f436990","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا","ayah_ref":"99:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B006","root_000638/B001"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000025","role":"Sticking to the ground and lingering supplies the normal downward anchoring function that the verse overturns.","root":"ء ر ض","source_ref":"99:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000638","role":"Shaking disturbance supplies the reversal by making the usual anchor generate movement.","root":"ز ل ز ل","source_ref":"99:1","source_word_indices":["2","4"]}],"changed_reading":{"after":"The event overturns the earth's role as anchor: the thing that normally holds everything down now moves everything else.","before":"The earth is merely the surface on which instability occurs."},"confidence":"medium","focus_anchor":"`الأرض` is the locus normally associated with staying down and holding position, yet it is paired with doubled shaking.","mechanism":"The event reverses the ground's normal anchoring function: what bodies cling to and weigh toward becomes the mover, so stability itself changes sides.","model_id":"b2_support_function_reversed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b2_support_function_reversed","source_type":"hft","support_id":"sup_e5a84824c68fc5490d2e","trust":"legacy_unbound"}]}
</lane_packet_json>
