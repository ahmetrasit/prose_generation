# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **14:20**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s014-regular-20260919/s014/14_20/micro.discovery.json` and modify nothing
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
  "ayah_ref": "14:20",
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
{"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"14:20:4:1","qac_word_ref":"14:20:4","surface_ar":"ٱللَّهِ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":[]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"14:20:4:1","qac_word_ref":"14:20:4","surface_ar":"ٱللَّهِ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":[]},{"boundary":"Tanım kalıcı güç ve korunmuş saygınlığı merkeze alır; sonradan güçlenmeyi bütün dala yaymaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"güçlü, yenilmez ve saygın olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güç, korunmuşluk ve saygınlık kişiyi yenilmekten ve aşağılanmaktan uzak tutar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem kullanımı, bir kişinin güçsüzlükten güçlü ve saygın bir duruma geçmesini anlatır."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Korunmuş güç ve aşağılanmanın karşıtı olan saygın durumun birlikte anlatıldığı genel kullanıma uygundur.","boundary_detail":"Tanım kalıcı güç ve korunmuş saygınlığı merkeze alır; sonradan güçlenmeyi bütün dala yaymaz.","branch_image_ar":"العزة والقوة بعد الذل","concept_gloss":"güçlü, yenilmez ve saygın olma","contextual_glosses":[{"applicability":"Bir kişinin önceki güçsüz veya aşağı durumundan çıkıp güçlü bir konuma gelişini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Durum değişimini, kazanılan gücü ve saygınlığı birlikte korur."},"facet_ids":["F002"],"text":"güçlenip saygınlık kazanmak","usage_role":"contextual"}],"definition":"Başkalarınca alt edilemeyecek ölçüde güçlü, korunmuş ve saygın olma; ayrıca güçsüz veya aşağı bir durumdan böyle bir konuma gelme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güç, korunmuşluk ve saygınlık kişiyi yenilmekten ve aşağılanmaktan uzak tutar."},{"facet_id":"F002","role":"extension","statement":"Eylem kullanımı, bir kişinin güçsüzlükten güçlü ve saygın bir duruma geçmesini anlatır."}],"identity_rationale":"Kaynak ifadesinin çekirdeği yalnızca düşüklükten sonra güç kazanmak değil; güç, yenilmezlik, saygınlık ve aşağılanmanın karşıtı olan korunaklı durumdur. Güçsüzlükten bu duruma geçiş, çekirdeğin yanında ayrı bir oluş kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yenilmezlik sağlayan güç ve saygınlık durumu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güçlü, üstün gelen ve yenilmeyen"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"güçsüzlükten çıkıp güçlü ve saygın duruma gelmek"}],"lexicalization_note":"Ad ve sıfat biçimleri durum bildirirken eylem bir kişinin güçsüzlükten güçlü ve saygın duruma geçmesini bildirir; bu iki kapsam ayrılmıştır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; saygınlık, güç, yardım ve öteki kök içi anlamlar çekirdeği yeterince paylaşmadığı için yalnızca en açıklayıcı iki karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal korunmuş ve üstün konumu, komşu dal ise bunun karşıtı olan değersizleştirilmiş ve güçsüz konumu bildirir.","focus_only":"Güç, korunmuşluk ve yenilmez saygınlık bulunur.","gloss":"saygın güç ile aşağılanma","neighbor_only":"Aşağılanma, güçsüzlük ve küçümsenme bulunur.","neighbor_ref":"root_001608/B003","relation_type":"antonym","shared_zone":"İki dal kişinin toplumsal ve güç bakımından konumunu aynı değer ekseninde ele alır."},{"boundary_match":"partial","distinction":"Odak doğrudan güçlü ve yenilmez durumu anlatır; komşu ise çoğu kez bu gücü sağlayan dayanağı veya destek çevresini adlandırır.","focus_only":"Kişinin kendisinde bulunan yenilmezlik ve aşağılanmaya karşı saygınlık öne çıkar.","gloss":"korunmuş güç ve güçlü dayanak","neighbor_only":"Dayanak, sığınılan yan, topluluk desteği ve yapısal temel kapsamları da vardır.","neighbor_ref":"root_000596/B001","relation_type":"near_synonym","shared_zone":"Her iki dal güç, korunma ve dayanıklılık alanında örtüşür."}],"source_phrase_ar":"العين والزاء أصل صحيح واحد يدل على شدة وقوة (maqayis); العزة لله والله العزيز (ayn); عز يعز عزة وعزا إذا صار عزيزا (jamhara); العز خلاف الذل (sihah); العزيز الممتنع فلا يغلبه شيء (tahdhib); العزة حالة مانعة للإنسان من أن يغلب (mufradat)","source_summary":"Kaynaklar güç, korunmuşluk, saygınlık ve yenilmezlik çekirdeğinde birleşir; oluş kullanımı bu duruma sonradan erişmeyi gösterir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العز والعزة والعزيز بمعنى القوة والمنعة والشرف وخلاف الذل وصيرورة المرء عزيزا","what_is_not_ar":"ليس خصوص القلة ولا الأرض الصلبة ولا اسم الصنم"},"support_links":[]},{"boundary":"Dal salt saygınlığı veya güç niteliğini değil, bir karşılaşmada gerçekleşen üstün gelme sonucunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B002","candidate_links":[{"candidate_id":"cand_da4afc7cd3077fd14683","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"üstün gelip boyun eğdirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir taraf karşısındakini yenerek onun üzerinde üstünlük kurar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üstün gelme, konuşma veya çekişme sırasında karşı tarafı sözle yenme biçiminde gerçekleşebilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Galibin yenilenden mal almasını anlatan özlü söz, yenme sonucunu örnekler."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir karşılaşmada rakibi yenme ve onun üzerinde belirleyici üstünlük kurma çekirdeğine uygundur.","boundary_detail":"Dal salt saygınlığı veya güç niteliğini değil, bir karşılaşmada gerçekleşen üstün gelme sonucunu anlatır.","branch_image_ar":"الغلبة والقهر","concept_gloss":"üstün gelip boyun eğdirme","contextual_glosses":[{"applicability":"Konuşma, savunma veya tartışma sırasında karşı tarafı sözle yenme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözlü karşılaşma koşulunu ve üstün gelme sonucunu korur."},"facet_ids":["F002"],"text":"sözlü çekişmede üstün gelmek","usage_role":"contextual"}],"definition":"Bir rakibe mücadele, çekişme veya sözlü karşılaşmada üstün gelerek onu yenmek ve boyun eğdirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir taraf karşısındakini yenerek onun üzerinde üstünlük kurar."},{"facet_id":"F002","role":"specialization","statement":"Üstün gelme, konuşma veya çekişme sırasında karşı tarafı sözle yenme biçiminde gerçekleşebilir."},{"facet_id":"F003","role":"example","statement":"Galibin yenilenden mal almasını anlatan özlü söz, yenme sonucunu örnekler."}],"identity_rationale":"Kaynak ifadesi bir rakibe üstün gelme ve onu boyun eğdirme çekirdeğini açıkça destekler. Söyleşide veya çekişmede üstün gelme ile galibin ganimet almasını anlatan söz, bu çekirdeğin özel bağlamlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"onu yenip boyun eğdirmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onunla üstünlük yarışına girmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sözlü çekişmede beni yenmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"üstün gelen, yenilenin malını alır"}],"lexicalization_note":"Eylem biçimleri genel üstün gelmeyi, kalıp kullanımlar ise sözlü çekişme ve galibin alma hakkı gibi belirli bağlamları bildirir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; salt fiziksel üstten alma veya tek bir kalıba bağlı yenme adayları, seçilen genel eş ve sınır karşılaştırmalarını yinelediği için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar eşleşir; odaktaki sözlü çekişme örneği, ortak yenme anlamının yalnızca özel bir gerçekleşmesidir.","focus_only":null,"gloss":"yenme ve boyun eğdirme","neighbor_only":null,"neighbor_ref":"root_001098/B001","relation_type":"synonym","shared_zone":"İki dalın çekirdeği de rakibe üstün gelerek onu yenmek ve üzerinde egemenlik kurmaktır."},{"boundary_match":"partial","distinction":"Odak için yenme yeterlidir; komşuda galip tarafın zorlayıcı gücü ve mağlubu iradesi dışında boyun eğdirmesi kurucu niteliktedir.","focus_only":"Karşılaşmada üstün gelme, sözlü çekişme dahil daha genel bir yenme sonucu olabilir.","gloss":"üstün gelme ve zorla egemen olma","neighbor_only":"Zor kullanma, istem dışı boyun eğdirme ve aşağılama özellikle belirgindir.","neighbor_ref":"root_001266/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir tarafın diğerini yenip denetimi ele geçirmesini anlatır."},{"boundary_match":"partial","distinction":"Odak galibiyet sonucunu bildirir; komşu ise galibiyet çıkmasa da sürebilen karşılıklı tartışma etkinliğini bildirir.","focus_only":"Çekişmenin sonucu olarak rakibi yenme ve üstünlük kurma öne çıkar.","gloss":"sözde üstün gelme ve tartışma","neighbor_only":"Karşılıklı söz alışverişi, tartışma ve uyuşmazlığın sürdürülmesi öne çıkar.","neighbor_ref":"root_000229/B002","relation_type":"near_neighbor","shared_zone":"İki dal sözlü bir karşılaşma ve karşı tarafı aşma çabasında buluşabilir."}],"source_phrase_ar":"غلبة وقهر (maqayis); عزه على أمره إذا غلبه (maqayis); وعزني في الخطاب أي غلبني (ayn;tahdhib;mufradat); عز يعز عزا إذا قهر (jamhara); عزه يعزه عزا غلبه (sihah); عزه يعزه إذا غلبه وقهره (tahdhib)","source_summary":"Kaynaklar yenme, üstün gelme ve boyun eğdirme çekirdeğinde birleşir; sözlü çekişme ve galibin mal alması bu çekirdeğin bağlama bağlı görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه غلبة الخصم وقهره والمغالبة في الخطاب أو الخصومة والمثل من غلب سلب","what_is_not_ar":"ليس مطلق الشرف بلا مغالبة ولا مجرد صعوبة الشيء"},"support_links":["sup_ad60ff93718074053d21"]},{"boundary":"Buradaki güçlük rakip yenmekten değil, nesnenin kıt ve erişilmesi zor olmasından doğar.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B003","candidate_links":[{"candidate_id":"cand_919935841d58b1ceac26","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"çok kıt ve güç bulunur olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne veya tür, neredeyse bulunmayacak derecede azdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kıtlık, nesnenin elde edilmesini veya bir benzerinin bulunmasını güçleştirir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin aşırı azlığını ve bu azlığın doğurduğu erişim güçlüğünü birlikte anlatır.","boundary_detail":"Buradaki güçlük rakip yenmekten değil, nesnenin kıt ve erişilmesi zor olmasından doğar.","branch_image_ar":"العزة بمعنى الندرة وصعوبة المنال","concept_gloss":"çok kıt ve güç bulunur olma","contextual_glosses":[{"applicability":"Varlığı yok denecek kadar azalan bir nesne veya türün durumunu doğal cümlede anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Elde etme veya benzerini bulma güçlüğünü ayrıca söylemez.","preserves":"Aşırı azlık ve bulunamama derecesini açıkça korur."},"facet_ids":["F001"],"text":"neredeyse hiç bulunmamak","usage_role":"contextual"}],"definition":"Bir şeyin neredeyse bulunamayacak kadar kıt olması ve bu nedenle ona erişmenin ya da dengini bulmanın güçleşmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne veya tür, neredeyse bulunmayacak derecede azdır."},{"facet_id":"F002","role":"extension","statement":"Kıtlık, nesnenin elde edilmesini veya bir benzerinin bulunmasını güçleştirir."}],"identity_rationale":"Kaynak ifadesi bir şeyin neredeyse bulunamayacak kadar az olmasını ve bunun sonucu olarak elde edilmesinin ya da denginin bulunmasının güçleşmesini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"neredeyse bulunamayacak kadar azalmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kıt, güç bulunan ve benzeri olmayan"}],"lexicalization_note":"Eylem kalıbı bir şeyin seyrekleşmesini, sıfat biçimi ise kıt ve güç elde edilir niteliğini bildirir; ikisi aynı sonuç zincirinde ayrılır.","neighbor_coverage_note":"Bütün adaylar incelendi; pahalılık, değerli eşya, yoksunluk sonrası kazanç ve uzaklık gibi alanlar kıtlığın kendisini tanımlamadığından yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak aşırı azlığı bulunamama eşiğiyle tanımlar; komşu ise herhangi bir düşük miktarı veya küçük topluluğu kapsar.","focus_only":"Azlığın neredeyse bulunamamaya ve erişim güçlüğüne varması gerekir.","gloss":"kıtlık ve az miktar","neighbor_only":"Miktar veya sayı yalnızca düşük olabilir; bulunurluk sonucu zorunlu değildir.","neighbor_ref":"root_000427/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bir şeyin sayı veya miktar bakımından az oluşunu kapsar."},{"boundary_match":"partial","distinction":"Odak bulunacak örnek sayısının azlığını, komşu ise mevcut şeyin mekansal uzaklığını temel alır.","focus_only":"Erişim güçlüğü nesnenin kıtlığından ve benzerinin azlığından doğar.","gloss":"kıtlıktan ve uzaklıktan doğan erişim güçlüğü","neighbor_only":"Erişim güçlüğü aranan şeyin uzakta olmasından ve yolculuk gerektirmesinden doğar.","neighbor_ref":"root_000943/B006","relation_type":"near_neighbor","shared_zone":"İki dalda da istenen şeye ulaşmak güçtür ve arama gerekebilir."}],"source_phrase_ar":"عز الشيء حتى يكاد لا يوجد (maqayis); عز الشيء جامع لكل شيء إذا قل حتى يكاد لا يوجد (ayn); عز الشئ إذا قل لا يكاد يوجد (sihah); عز كذا وكذا إذا قل حتى لا يكاد يوجد (tahdhib); يصعب مناله ووجود مثله (mufradat)","source_summary":"Kaynaklar aşırı azlık ile zor erişim arasında bir sonuç ilişkisi kurar; az bulunan şeyin kendisine veya benzerine ulaşmak güçtür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قلة الشيء حتى لا يكاد يوجد وصعوبة مناله أو وجود مثله","what_is_not_ar":"ليس قوة الغلبة على خصم ولا صلابة الأرض"},"support_links":["sup_429d60eb8f71dfb3ee5d"]},{"boundary":"Dal bir güç niteliğini değil, gücü artıran veya yeni güç kazandıran geçişli işlemi anlatır.","branch_kind":"non_bare","branch_ref":"root_001008/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"güçlendirip pekiştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Etkileyen taraf kişi veya şeye güç, sağlamlık ya da saygınlık kazandırır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir unsur, yanına başka bir unsur eklenerek desteklenir ve daha güçlü kılınır."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyi daha güçlü ve sağlam kılan geçişli işlemin genel karşılığıdır.","boundary_detail":"Dal bir güç niteliğini değil, gücü artıran veya yeni güç kazandıran geçişli işlemi anlatır.","branch_image_ar":"التعزيز والتقوية","concept_gloss":"güçlendirip pekiştirme","contextual_glosses":[{"applicability":"Mevcut bir kişi veya unsurun üçüncü bir destekle daha güçlü kılındığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ek destek katılımcısını ve güç artışı sonucunu açıkça korur."},"facet_ids":["F002"],"text":"bir destek daha ekleyerek güçlendirmek","usage_role":"explanatory"}],"definition":"Bir kişi veya şeyi güçlü, sağlam ve saygın duruma getirmek; var olan desteği başka bir destekle daha da pekiştirmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Etkileyen taraf kişi veya şeye güç, sağlamlık ya da saygınlık kazandırır."},{"facet_id":"F002","role":"specialization","statement":"Bir unsur, yanına başka bir unsur eklenerek desteklenir ve daha güçlü kılınır."}],"identity_rationale":"Kaynak ifadesi kişi veya şeyi güçlü ve saygın duruma getirme, onu sağlamlaştırma ve bir desteği başka bir destekle pekiştirme işlemlerini açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onu güçlü ve saygın kılmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onu güçlendirip sağlamlaştırmak"}],"lexicalization_note":"Anlam yalnızca türemiş geçişli eylem biçimlerinde kanıtlanmıştır; yalın köke bağımsız bir güçlendirme anlamı yüklenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; salt güç niteliği, yardımcı kişi, dayanılan yan ve huzur bulma anlamları işlem sınırını paylaşmadığı için iki yararlı karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak sonuç olarak güç kazandırmayı anlatır; komşu, güç artışı zorunlu olmasa da yardım ve destek sunma ilişkisini anlatır.","focus_only":"Kişi yanında nesne veya yapı da doğrudan daha güçlü ve sağlam kılınabilir.","gloss":"güçlendirme ve yardım etme","neighbor_only":"Bir başkasına belirli bir işte yardım etme ve onun tarafını tutma ilişkisi belirgindir.","neighbor_ref":"root_000021/B005","relation_type":"near_synonym","shared_zone":"Her iki dal başka bir tarafın gücünü veya bir işi başarma kapasitesini artırabilir."},{"boundary_match":"partial","distinction":"Odak kuvvet artışını, komşu ise hareketi veya kararsızlığı sona erdiren sabitlenmeyi kurucu sonuç sayar.","focus_only":"Temel sonuç güç veya sağlamlık artışıdır.","gloss":"güçlendirme ve sabitleme","neighbor_only":"Temel sonuç yerinde kalma, kararlılık veya gönlün yatışmasıdır.","neighbor_ref":"root_000192/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyi daha dayanıklı ve sarsılmaz kılma bağlamında iki işlem örtüşebilir."}],"source_phrase_ar":"أعززته أنا جعلته عزيزا (maqayis); أعززته قويته وعززته أيضا (maqayis); أعزه الله (ayn); فعززنا بثالث أي قوينا وشددنا (sihah); قويناه وشددناه (tahdhib)","source_summary":"Kaynaklar geçişli güç kazandırma işleminde birleşir; ek bir destekle pekiştirme bu işlemin özel bir gerçekleşmesidir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه جعل الشيء أو الشخص عزيزا أو قويا وشديدا وتقوية الواحد بآخر","what_is_not_ar":"ليس مجرد كون الشيء عزيزا بلا إيقاع تقوية"},"support_links":[]},{"boundary":"Dal genel bir zorluk adı değil, belirli bir şeyin kişiye ağır ve çetin gelmesini bildiren bağımlı yapıdır.","branch_kind":"non_bare","branch_ref":"root_001008/B005","candidate_links":[{"candidate_id":"cand_ef75f62fff7795d680a0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"kişiye ağır ve çetin gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum veya eylem, onu yaşayan kişi için zor ve ağır hale gelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başkasının uğradığı olayın kişiye büyük ve sarsıcı gelmesi bu etkinin özel bir örneğidir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir olayın veya yapılacak işin özne üzerindeki zorlayıcı ve büyük etkisini anlatan yapıya uygundur.","boundary_detail":"Dal genel bir zorluk adı değil, belirli bir şeyin kişiye ağır ve çetin gelmesini bildiren bağımlı yapıdır.","branch_image_ar":"شدة الوقع والصعوبة","concept_gloss":"kişiye ağır ve çetin gelme","contextual_glosses":[{"applicability":"Başka bir kişinin uğradığı olayın konuşan üzerinde büyük ve zorlayıcı etki yarattığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etkilenen kişiyi, başkasının yaşadığı olayı ve ağırlık derecesini korur."},"facet_ids":["F002"],"text":"başına gelen bana çok ağır geldi","usage_role":"contextual"}],"definition":"Bir olayın, durumun veya yapılacak işin kişi üzerinde büyük bir ağırlık yaratması ve ona çetin, zor ya da katlanılması güç gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum veya eylem, onu yaşayan kişi için zor ve ağır hale gelir."},{"facet_id":"F002","role":"specialization","statement":"Başkasının uğradığı olayın kişiye büyük ve sarsıcı gelmesi bu etkinin özel bir örneğidir."}],"identity_rationale":"Kaynak ifadesi bir olayın, kaybın veya yapılacak işin kişi üzerinde büyük ve ağır bir etki yaratmasını; bu nedenle güç, çetin veya katlanılması zor gelmesini destekler.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu bana zor, ağır ve çetin geldi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"başına gelen bana çok büyük ve ağır geldi"}],"lexicalization_note":"Anlam kişi üzerinde etki bildiren belirli eylem yapılarıyla sınırlıdır; yalın biçime genel zorluk anlamı aktarılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yoğun sıkıntı, felaket, erime ve sarsıntı adayları zor gelme yapısından daha özel sonuçlar taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak zorluğu yaşayan kişiye bağlar; komşu ise zorluğu olayın veya işin kendi niteliği olarak daha genel biçimde sunar.","focus_only":"Belirli olayın veya işin bir kişiye ağır gelmesi ve onda yarattığı etki yapısal olarak gereklidir.","gloss":"kişiye ağır gelme ve genel zorluk","neighbor_only":"Zorluk, belirli bir etkilenen kişi belirtilmeden işin veya günün genel niteliği olabilir.","neighbor_ref":"root_001012/B001","relation_type":"near_synonym","shared_zone":"Her iki dal kolay olmayan, çetin ve güç bir durumu anlatır."},{"boundary_match":"partial","distinction":"Odak algılanan zorluk ve etkiyi, komşu ise ağırlığın kişiyi bastıracak ölçüde üstün gelmesini temel alır.","focus_only":"Bir şeyin öznel olarak ağır, büyük ve zor gelmesi yeterlidir.","gloss":"ağır gelme ve ezici yük","neighbor_only":"Yükün sahibini bastırması, ona üstün gelmesi ve giderek ağırlaşması öne çıkar.","neighbor_ref":"root_001062/B003","relation_type":"near_neighbor","shared_zone":"İki dal kişinin bir olayın ağırlığı altında zorlanmasını kapsar."}],"source_phrase_ar":"أعززت بما أصاب فلانا أي عظم علي واشتد (maqayis); أعزز علي بما أصاب فلانا أي أعظم علي (ayn); عز علي أن تفعل كذا (sihah); عز علي ذاك أي حق واشتد (sihah); عز علي كذا صعب (mufradat)","source_summary":"Kaynaklar bir şeyin kişiye zor, ağır ve büyük gelmesi noktasında birleşir; başkasının başına gelen olaydan etkilenme bunun özel bağlamıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ما يشتد على النفس أو يصعب ويعظم وقعه من مصيبة أو فعل","what_is_not_ar":"ليس غلبة خصم في خصومة ولا ندرة الشيء"},"support_links":["sup_007ec6e3a97e3f16395e"]},{"boundary":"İnsan cimriliği çekirdeğe katılmaz; yalnızca belirtilen atasözü benzeri kalıpta bağımlı bir kullanım olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"dar kanallı ve güç sağılan olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dar meme kanalı süt akışını azaltır ve sağımı güçleştirir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sütü çok olduğu halde zor veren hayvan imgesi, yalnızca kalıp sözde varlıklı fakat cimri kişiyi anlatır."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi deve veya keçide kanal darlığına bağlı az ya da zahmetli süt akışını anlatır.","boundary_detail":"İnsan cimriliği çekirdeğe katılmaz; yalnızca belirtilen atasözü benzeri kalıpta bağımlı bir kullanım olarak tutulur.","branch_image_ar":"ضيق الإحليل وقلة الدر","concept_gloss":"dar kanallı ve güç sağılan olma","contextual_glosses":[{"applicability":"Sadece bol varlığı olduğu halde vermekte direnen kişiyi hayvana benzeten kalıp söz için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Varlık bolluğu ile vermeme ve cimrilik karşıtlığını korur."},"facet_ids":["F002"],"text":"malı çok, eli sıkı kişi","usage_role":"contextual"}],"definition":"Dişi deve veya keçinin meme kanalının dar olması nedeniyle sütünün az gelmesi ya da ancak zor ve uğraştırıcı bir sağımla akması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dar meme kanalı süt akışını azaltır ve sağımı güçleştirir."},{"facet_id":"F002","role":"associated_use","statement":"Sütü çok olduğu halde zor veren hayvan imgesi, yalnızca kalıp sözde varlıklı fakat cimri kişiyi anlatır."}],"identity_rationale":"Kaynak ifadesinin çekirdeği dişi deve veya keçinin meme kanalının darlığı yüzünden sütünün az gelmesi ya da ancak güçlükle sağılmasıdır. Varlıklı ama cimri kişiye ilişkin söz, hayvan niteliğinin benzetmeli ve kalıba bağlı kullanımından ibarettir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"meme kanalı dar, sütü az veya güç sağılan dişi hayvan"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"malı çok olduğu halde vermeyen cimri kişi"}],"lexicalization_note":"Hayvanın niteliğini bildiren biçim ile varlıklı cimriyi anlatan kalıp ayrıdır; kalıptaki insan anlamı yalın biçime genellenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; doğum çevresi az süt, üç meme bölmesi, yağlanma, meme doluluğu ve sağım düzeni çekirdek nedeni paylaşmadığından yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak anatomik daralma yüzünden sütün zor çıkmasını, komşu ise nedeni bundan bağımsız olabilen azalma veya kesilmeyi anlatır.","focus_only":"Süt azlığı dar meme kanalından doğar ve sağımın emek istemesiyle birlikte tanımlanır.","gloss":"güç süt verme ve sütün kesilmesi","neighbor_only":"Sütün bütünüyle kesilmesi veya azlığı yanında yağmur kıtlığı da kapsama girer.","neighbor_ref":"root_000305/B005","relation_type":"near_neighbor","shared_zone":"İki dal süt veriminin az veya yetersiz olması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odakta daralma akışı güçleştirir ve azaltır; komşuda fiziksel kesilme veya bozulma sütü sona erdirir.","focus_only":"Kanal dardır ama süt uğraşla çıkabilir.","gloss":"zor akan ve kesilmiş süt","neighbor_only":"Kanalın kuruması, bozulması veya kesilmesi yüzünden süt bütünüyle durmuş olabilir.","neighbor_ref":"root_000861/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal dişi hayvanın meme kanalı ile süt akışı arasındaki bozukluğu anlatır."}],"source_phrase_ar":"ناقة عزوز إذا كانت ضيقة الإحليل لا تدر إلا بجهد (maqayis); العزوز الشاة الضيقة الإحليل (ayn); العزوز من النوق الضيقة الإحليل (sihah); شاة عزوز ضيقة الإحليل لا تدر حتى تحلب بجهد (tahdhib); شاة عزوز قل درها (mufradat)","source_summary":"Kaynaklar dar meme kanalı, az süt akışı ve zahmetli sağım ilişkisinde birleşir; cimri varlıklı kişi benzetmesi yalnızca özel kalıpta geçerlidir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الناقة أو الشاة العزوز لضيق الإحليل وقلة الدر أو عدم الدر إلا بجهد","what_is_not_ar":"ليس بخلا بشريا إلا في المثل المبني على العنز العزوز"},"support_links":[]},{"boundary":"Şiddetli yağmurun kendisi değil, zemini bastırıp sıkılaştıran etkisi bu dala girer.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B007","candidate_links":[{"candidate_id":"cand_daae2a6b87278baac4af","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"sertleşip sıkıca pekişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taşlı olması gerekmeyen zemin sert ve sıkı bir yapı gösterir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kum, et veya başka bir madde sıkılaşıp sertleşerek dağılmaz hale gelir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yağmur toprağı bastırıp tanelerini birbirine bağlayarak zemini pekiştirir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toprak veya başka bir maddenin sıkı, sert ve dağılmaz hale gelmesini anlatan genel karşılıktır.","boundary_detail":"Şiddetli yağmurun kendisi değil, zemini bastırıp sıkılaştıran etkisi bu dala girer.","branch_image_ar":"صلابة الأرض وتماسك الشيء","concept_gloss":"sertleşip sıkıca pekişme","contextual_glosses":[{"applicability":"Yağmurun toprağı sıkılaştıran ve yüzeyi daha sert hale getiren etkisini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmuru neden, toprağın sıkılaşmasını sonuç olarak korur."},"facet_ids":["F003"],"text":"yağmur toprağı bastırıp pekiştirdi","usage_role":"contextual"}],"definition":"Toprağın veya başka bir maddenin sert, sıkı ve dağılmaz bir yapıda olması ya da basınç ve yağmur etkisiyle böyle bir yapıya gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taşlı olması gerekmeyen zemin sert ve sıkı bir yapı gösterir."},{"facet_id":"F002","role":"extension","statement":"Kum, et veya başka bir madde sıkılaşıp sertleşerek dağılmaz hale gelir."},{"facet_id":"F003","role":"associated_use","statement":"Yağmur toprağı bastırıp tanelerini birbirine bağlayarak zemini pekiştirir."}],"identity_rationale":"Kaynak ifadesi taşsız sert toprağı, çeşitli maddelerin sıkılaşıp dağılmaz hale gelmesini ve yağmurun toprağı bastırıp pekiştirmesini ortak sertlik ve kohezyon ekseninde destekler.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"taşsız, sert ve su tutmayan zemin"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kum sıkılaşıp dağılmaz hale gelmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yağmur toprağı bastırıp pekiştirmek"}],"lexicalization_note":"Toprak adı yalın bir zemin türünü, eylem biçimleri ise kumun, etin veya toprağın sertleşip sıkılaşmasını bildirir; kapsamlar harmanlanmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; kaya, taş, yoğun gövde ve taşlı arazi adayları benzer sertlik alanını seçilen ilişkilerden daha az açıklayıcı biçimde yineledi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak tanelerin veya dokunun sıkılaşmasına ve özellikle zemine yönelir; komşu katı kütlenin yoğun ve içsiz yapısını daha geniş kapsar.","focus_only":"Yağmurla pekişme, kumun dağılmaz hale gelmesi ve taşsız sert toprak kullanımları bulunur.","gloss":"pekişmiş sertlik ve yoğun katılık","neighbor_only":"İçi boş olmama, yoğun taş kütlesi ve yüksek kaba yer kapsamları bulunur.","neighbor_ref":"root_000882/B002","relation_type":"near_synonym","shared_zone":"İki dal sert, sıkı ve boşluksuz denebilecek maddesel yapıları anlatır."},{"boundary_match":"partial","distinction":"Odak sertliği taşsızlık ve sıkı tutunmayla tanımlar; komşu zeminin kabalığına ve ondan kopan parçaya da uzanır.","focus_only":"Taşsız sert zemin yanında kum, et ve yağmurla pekişme uzantıları vardır.","gloss":"sert zemin ve kaba toprak","neighbor_only":"Kaba sert toprak yüzeyi ve yüzeyden kopmuş iri toprak parçası bulunur.","neighbor_ref":"root_000214/B007","relation_type":"near_synonym","shared_zone":"Her iki dal sert ve sıkı toprak yüzeyini adlandırabilir."},{"boundary_match":"opposed","distinction":"Odak sıkı ve sert ucu, komşu ise yumuşak veya çamurlu ucu temsil eder.","focus_only":"Sertlik, sıkılık ve dağılmama bulunur.","gloss":"sert zemin ve yumuşak çamur","neighbor_only":"Yumuşak toprak veya kara çamur bulunur.","neighbor_ref":"root_000373/B013","relation_type":"polarity_pair","shared_zone":"İki dal toprağı veya toprağa dayalı maddeyi kıvam ve yapı bakımından niteler."}],"source_phrase_ar":"العزازة أرض صلبة ليست بذات حجارة (maqayis); العزاز أرض صلبة (ayn;sihah;tahdhib); كل شيء صلب فقد استعز (jamhara); تعزز لحم الناقة إذا صلب واشتد (maqayis;tahdhib); استعز الرمل وغيره إذا تماسك فلم ينهل (maqayis;sihah); المطر يعزز الأرض أي يلبدها (sihah;mufradat)","source_summary":"Kaynaklar sertlik ve sıkı tutunma çekirdeğini toprak, kum ve et üzerinde gösterir; yağmur bu niteliğin nedeni olarak zemini bastırıp pekiştirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العزاز من الأرض وصلابة الطين وتماسك الرمل واللحم وتلبيد المطر للأرض","what_is_not_ar":"ليس المطر الشديد نفسه إلا من جهة أثره في تلبيد الأرض"},"support_links":["sup_8407e8aa4e90fe417077"]},{"boundary":"Dal zeminin sertliğini veya yağmurun toprağı pekiştirme etkisini değil, yıl ve yağış olaylarının şiddetini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"çetin ve baskın doğa şiddeti","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yıl, insanlar ve yaşam koşulları üzerinde ağır baskı yaratacak ölçüde çetindir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yağmur çok, sert ve iri damlalı biçimde yağar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sel çevresine üstün gelen baskın bir akış gücü taşır."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yılın ağır oluşunu, yağmurun sertliğini ve selin baskın gücünü ortak biçimde özetler.","boundary_detail":"Dal zeminin sertliğini veya yağmurun toprağı pekiştirme etkisini değil, yıl ve yağış olaylarının şiddetini anlatır.","branch_image_ar":"الشدة في السنة والمطر والسيل","concept_gloss":"çetin ve baskın doğa şiddeti","contextual_glosses":[{"applicability":"Yağmurun miktar ve vuruş bakımından güçlü olduğu özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmur alanını, bolluğu ve yüksek şiddeti birlikte korur."},"facet_ids":["F002"],"text":"çok şiddetli yağmur","usage_role":"contextual"},{"applicability":"Selin çevresine üstün gelen baskın akışını anlatan özel kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sel olayını ve baskın akış gücünü birlikte korur."},"facet_ids":["F003"],"text":"önüne geçilemeyen sel","usage_role":"contextual"}],"definition":"Bir yılın ağır ve çetin geçmesi, yağmurun çok ve sert yağması ya da selin baskın bir güç taşıması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yıl, insanlar ve yaşam koşulları üzerinde ağır baskı yaratacak ölçüde çetindir."},{"facet_id":"F002","role":"specialization","statement":"Yağmur çok, sert ve iri damlalı biçimde yağar."},{"facet_id":"F003","role":"specialization","statement":"Sel çevresine üstün gelen baskın bir akış gücü taşır."}],"identity_rationale":"Kaynak ifadesi çetin yılı, çok ve şiddetli yağmuru ve baskın seli destekler. Geçici çerçevedeki vadide şiddetli itme unsuru kaynak ifadesinde yer almadığından tanıma alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ağır ve çetin yıl"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"çok ve şiddetli yağmur"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"baskın ve güçlü sel"}],"lexicalization_note":"Yıl adı bağımsız bir biçimdir; şiddetli yağmur ve baskın sel anlamları yalnızca kendi ad tamlaması benzeri kalıplarında korunur.","neighbor_coverage_note":"Tüm adaylar incelendi; uzak yerden gelen sel, genel yağmur, kuraklık, savaş şiddeti ve geniş alana yağan yağmur seçilen yoğunluk karşılaştırmalarından daha uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belirli yıl, yağmur ve sel adlandırmalarına bağlıdır; komşu çeşitli hava olaylarının oluş sırasında şiddetlenmesini kapsar.","focus_only":"Çetin yıl ve baskın sel yanında şiddetli yağmur bulunur.","gloss":"şiddetli yağış ve hava olayının şiddetlenmesi","neighbor_only":"Rüzgar, sıcak ve soğuk gibi başka hava olaylarının şiddetlenmesi de kapsanır.","neighbor_ref":"root_000810/B005","relation_type":"near_synonym","shared_zone":"İki dal yağmurun sertleşip güçlü biçimde gerçekleşmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak seli baskın gücüyle niteler; komşu suyun yükselip taşmasını ve sürükleyici sonucunu ayrıntılandırır.","focus_only":"Çetin yıl ve çok şiddetli yağmur da bağımsız kapsamdır.","gloss":"baskın sel ve taşkın su","neighbor_only":"Suyun yükselerek taşması ve önüne kattığını sürüklemesi kurucu özelliktir.","neighbor_ref":"root_000937/B002","relation_type":"near_neighbor","shared_zone":"İki dal güçlü selin çevresine üstün gelen hareketinde örtüşür."},{"boundary_match":"opposed","distinction":"Odak eksenin yüksek şiddet ucunu, komşu ise düşük şiddet ve yüzeysel ıslatma ucunu temsil eder.","focus_only":"Çok, sert ve güçlü yağış bulunur.","gloss":"şiddetli ve hafif yağmur","neighbor_only":"Yalnızca yüzeyi hafifçe ıslatan zayıf yağış bulunur.","neighbor_ref":"root_000497/B003","relation_type":"polarity_pair","shared_zone":"İki dal yağmuru miktar ve etki şiddeti ekseninde niteler."}],"source_phrase_ar":"العزاء السنة الشديدة (maqayis;ayn;sihah); العز من المطر الكثير الشديد (maqayis); مطر عز أي شديد (sihah); العز المطر الشديد الوابل (tahdhib); سيل عز وهو السيل الغالب (maqayis)","source_summary":"Kaynaklar yılın çetinliği ile yağmur ve selin güçlü şiddetini aynı yoğunluk alanında toplar; her kullanım kendi adlandırma kalıbına bağlıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه السنة الشديدة والمطر الشديد الكثير والسيل الغالب والدفع الشديد في الوادي","what_is_not_ar":"ليس مجرد صلابة الأرض ولا تلبيدها إلا إذا ذكر أثر المطر"},"support_links":[]},{"boundary":"Bu dal genel iki rakip arasındaki yenme değil, belirli eylem yapısında hastalık, ölüm veya başka bir durumun kişiyi ele geçirmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001008/B009","candidate_links":[{"candidate_id":"cand_da4afc7cd3077fd14683","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"hastalık veya durumun kişiye üstün gelmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hastalık, ölüm veya başka bir durum kişiye üstün gelerek onu güçsüz bırakır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir iş veya ayartıcı etki kişi üzerinde ısrarla sürer ve onun denetimini aşar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kalıp niteleme, hastalığın çok ağır ve şiddetli olduğunu bildirir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi ele geçirip gücünü aşan hastalık, ölüm veya başka baskın durumlar için uygundur.","boundary_detail":"Bu dal genel iki rakip arasındaki yenme değil, belirli eylem yapısında hastalık, ölüm veya başka bir durumun kişiyi ele geçirmesidir.","branch_image_ar":"استعزاز المرض أو الموت أو الأمر","concept_gloss":"hastalık veya durumun kişiye üstün gelmesi","contextual_glosses":[{"applicability":"Hastalığın kişiye üstün gelecek ölçüde şiddetlendiği doğal cümle bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalığın artan şiddetini ve kişinin buna yenik düşmesini korur."},"facet_ids":["F001","F003"],"text":"hastalığı çok ağırlaştı","usage_role":"contextual"}],"definition":"Hastalık, ölüm veya başka baskın bir durumun kişiyi yenip gücünü kırması; bir işin ya da ayartıcı etkinin kişi üzerinde inatla egemenlik kurması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hastalık, ölüm veya başka bir durum kişiye üstün gelerek onu güçsüz bırakır."},{"facet_id":"F002","role":"extension","statement":"Bir iş veya ayartıcı etki kişi üzerinde ısrarla sürer ve onun denetimini aşar."},{"facet_id":"F003","role":"specialization","statement":"Kalıp niteleme, hastalığın çok ağır ve şiddetli olduğunu bildirir."}],"identity_rationale":"Kaynak ifadesi hastalık veya ölümün kişiye üstün gelmesini merkezde tutar, fakat aynı yapıyı başka baskın durumlara, bir işin inatla sürmesine ve ayartıcı gücün kişiye egemen olmasına da genişletir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hastalık, ölüm veya başka bir durum ona üstün gelmek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"iş onun üzerinde inatla sürüp egemen olmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hastalığı çok ağır olan kişi"}],"lexicalization_note":"Anlam belirli türemiş eylemler ve ağır hastalık kalıbıyla sınırlıdır; hastalık dışı kapsamlar da ancak bu yapılarda geçerlidir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; ani ölüm, çıkışsız durum, felaket, hastalık yinelemesi ve bilinç kaybı üstün gelme sürecinden farklı sonuçlar taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak etkenin kişiyi yenmesini ve ağırlaşmasını gerektirir; komşu ise bir durumun başlamasını veya bedeni tutmasını, üstünlük sonucu olmadan da kapsar.","focus_only":"Hastalık, ölüm veya başka etken kişiye üstün gelip onu güçsüz bırakır.","gloss":"hastalığın üstün gelmesi ve bedensel halin başlaması","neighbor_only":"Hastalık yanında göz rahatsızlığı, taşkınlık hali, hazımsızlık ve semirme gibi bedensel durumlar da yalnızca baş gösterir.","neighbor_ref":"root_000018/B007","relation_type":"near_neighbor","shared_zone":"İki dal hastalık veya başka bir bedensel durumun kişiyi ya da hayvanı etkisi altına almasını anlatır."},{"boundary_match":"partial","distinction":"Odak özellikle kişinin hastalık veya başka durum karşısında yenilmesini, komşu ise etkenin hedefi örtüp üzerine çökmesini kurucu imge yapar.","focus_only":"Hastalık ve ölümün kişiyi yenmesi ile bir işin inatla sürmesi belirgindir.","gloss":"kişiye üstün gelme ve üzerine çökme","neighbor_only":"Olumsuzluk, aşağılık veya darlığın bir şeyin üzerine çöküp onu bütünüyle örtmesi belirgindir.","neighbor_ref":"root_000606/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir etkenin hedefini kaplayıp onun üzerinde zorlayıcı egemenlik kurmasını anlatır."}],"source_phrase_ar":"استعز على المريض إذا اشتد مرضه (maqayis); استعز به المرض (maqayis); استعز عليه الشيطان أي غلب عليه (maqayis); استعز عليه الأمر إذا لج فيه (maqayis); استعز بفلان أي غلب في كل شيء مرض أو غيره (sihah;tahdhib); استعز بفلان إذا غلب بمرض أو بموت (mufradat)","source_summary":"Kaynaklar hastalık veya ölüm başta olmak üzere bir durumun kişiye üstün gelmesi çekirdeğinde birleşir; işin sürüp gitmesi ve ayartıcı etkinin egemenliği kapsam uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه غلبة المرض أو الموت على الشخص وغلبة الشيطان أو الأمر ولجاجه","what_is_not_ar":"ليس مطلق الغلبة بين خصمين إلا إذا جاء بصيغة الاستعزاز ونحوه"},"support_links":["sup_ad60ff93718074053d21"]},{"boundary":"Bu dal yalnızca at anatomisine ait bir bölge adıdır; manevi güç, saygınlık veya sert zemin anlamı taşımaz.","branch_kind":"bare","branch_ref":"root_001008/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"atın iki kalça ucu arasındaki bölge","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bölge atın arka bedeninde sağrı, uyluk ve iki kalça ucu arasındaki yakın alanda bulunur."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atın sağrı ve uyluk çevresindeki belirli arka beden bölümünü adlandırmak için uygundur.","boundary_detail":"Bu dal yalnızca at anatomisine ait bir bölge adıdır; manevi güç, saygınlık veya sert zemin anlamı taşımaz.","branch_image_ar":"العزيزاء من الفرس","concept_gloss":"atın iki kalça ucu arasındaki bölge","definition":"Atın arka bedeninde, sağrı ile uyluğun birleşimine yakın, iki kalça ucu veya arka yan çıkıntısı arasında kalan bölge.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bölge atın arka bedeninde sağrı, uyluk ve iki kalça ucu arasındaki yakın alanda bulunur."}],"identity_rationale":"Kaynak ifadesi atın sağrı ve uyluk çevresinde, iki arka yan veya kalça ucu arasında yer alan belirli anatomik bölgeyi adlandırır. Kaynaklardaki tarifler aynı arka beden yöresinin yakın sınırlarını verir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"atın sağrı ile uyluk yakınındaki iki kalça ucu arası"}],"lexicalization_note":"Kanıt tek bir yalın anatomik adla sınırlıdır; başka beden parçalarına veya mecazi anlamlara genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; omur çıkıntısı, kalça siniri, sarkıntı ve kalça eti eksikliği aynı arka beden alanında olsa da doğrudan konum eşleşmesi vermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Konumlar yakın olsa da odak atın iki yan arasındaki bölgesine, komşu devenin belirli birleşim yerine bağlıdır.","focus_only":"Atın sağrı-uyluk çevresindeki iki kalça ucu arası adlandırılır.","gloss":"at ve devede sağrı-uyluk çevresi","neighbor_only":"Devenin sağrısı ile uyluğu arasındaki eklem bölgesi adlandırılır.","neighbor_ref":"root_001655/B010","relation_type":"near_neighbor","shared_zone":"İki dal büyük bir binek hayvanının arka bedeninde sağrı ile uyluğa yakın anatomik alanı gösterir."},{"boundary_match":"field_only","distinction":"Odak tür ve konum bakımından dar bir at anatomisi terimidir; komşu genel arka bölüm ve sağrı alanını kapsar.","focus_only":"Atın iki kalça ucu arasındaki dar anatomik bölgeyi gösterir.","gloss":"belirli kalça aralığı ve genel sağrı","neighbor_only":"İnsan veya hayvanda sağrı, kaba et ve bir şeyin arkası gibi daha geniş arka bölüm anlamlarını kapsar.","neighbor_ref":"root_000556/B003","relation_type":"same_field","shared_zone":"İki dal bedenin arka, sağrı ve kalça çevresindeki alanları adlandırır."}],"source_phrase_ar":"العزيزاء من الفرس ما بين عكوته وجاعرته (maqayis); العزيزى من الفرس وهما طرفا الوركين (sihah); العزيزاء وهما عزيزاوا الفرس ما بين جاعرتيه (tahdhib)","source_summary":"Kaynak tarifleri atın arka bedenindeki aynı bölgeyi, sağrı-uyluk birleşimi ile iki kalça ucu arasındaki yakın anatomik sınırlarla açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العزيزاء من الفرس وما بين الجاعرتين أو طرفا الورك","what_is_not_ar":"ليس العزة المعنوية ولا العزاز من الأرض"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001008/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"biçime bağlı adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir biçim, en güçlü veya en üstün anlamındaki sıfatın dişil karşılığıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim ayrıca tapınılan bir putun veya ağacın özel adı olarak aktarılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir sesletim ceylan yavrusunu ve bundan türeyen kadın adını bildirir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"العزى وما جاورها من أسماء","concept_gloss":"biçime bağlı adlandırmalar","definition":"Kanıt, aynı yazı ailesinde dişil bir üstünlük biçimi ile bundan kavramsal olarak ayrı olan kült, ceylan yavrusu ve kadın adlandırmalarını birlikte sunar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir biçim, en güçlü veya en üstün anlamındaki sıfatın dişil karşılığıdır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim ayrıca tapınılan bir putun veya ağacın özel adı olarak aktarılır."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir sesletim ceylan yavrusunu ve bundan türeyen kadın adını bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"en güçlü veya en üstün sıfatının dişil biçimi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"tapınılan bir putun veya kutsal ağacın adı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ceylan yavrusu; buradan türeyen kadın adı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"العزى تأنيث الأعز (maqayis;tahdhib); العزى صنم (mufradat); العزى سمرة كانت لغطفان يعبدونها (sihah;tahdhib); العزة بالفتح بنت الظبية وبها سميت المرأة عزة (sihah;tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العزى تأنيث الأعز واسم الصنم وعزة اسما للظبية أو المرأة","what_is_not_ar":"ليس معنى الغلبة أو الندرة إلا من جهة الاشتقاق من الأعز"},"support_links":[]},{"boundary":"Dal güç, saygınlık veya yenme anlamı taşımaz; yalnızca keçiye yöneltilen belirli kovma ünlemi ve bundan kurulan eylemdir.","branch_kind":"non_bare","branch_ref":"root_001008/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","surface_ar":"عَزِيزٍ"}],"gloss":"keçiyi kovma ünlemiyle sürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşan, keçiyi kovmak veya yönlendirmek amacıyla belirli bir ünlem çıkarır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tekrarlı eylem biçimi, keçiyi bu ünlemle azarlayıp sürme işlemini bildirir."}}],"root_ar":"ع ز ز","root_id":"root_001008","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Keçiye belirli bir ses çıkararak onu uzaklaştırma veya yönlendirme eylemini anlatır.","boundary_detail":"Dal güç, saygınlık veya yenme anlamı taşımaz; yalnızca keçiye yöneltilen belirli kovma ünlemi ve bundan kurulan eylemdir.","branch_image_ar":"زجر العنز بعز عز","concept_gloss":"keçiyi kovma ünlemiyle sürme","contextual_glosses":[{"applicability":"Ünlemin kendisi yerine yapılan eylemin doğal Türkçe açıklamasının gerektiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kovma sesini, keçiyi ve uzaklaştırma eylemini açıkça korur."},"facet_ids":["F002"],"text":"keçiyi bir kovma sesiyle uzaklaştırmak","usage_role":"explanatory"}],"definition":"Keçiyi uzaklaştırmak veya yönlendirmek için ona belirli bir kovma ünlemi söylemek ve bu seslenişle hayvanı sürmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşan, keçiyi kovmak veya yönlendirmek amacıyla belirli bir ünlem çıkarır."},{"facet_id":"F002","role":"extension","statement":"Tekrarlı eylem biçimi, keçiyi bu ünlemle azarlayıp sürme işlemini bildirir."}],"identity_rationale":"Tek kaynaklı ifade, keçiyi belirli bir ünlemle azarlayıp sürme sesini ve bu sesle yapılan kovma eylemini açıkça aynı sözlü yönlendirme kullanımında birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"keçiyi kovmak için çıkarılan ünlem"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"keçiyi bu ünlemle azarlayıp sürmek"}],"lexicalization_note":"Anlam bir sesleniş kalıbı ve ondan kurulan tekrar biçimli eylemle sınırlıdır; yalın köke bağımsız bir kovma anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; köpek, deve, katır ve yılan-koyun seslenişleri aynı genel hayvan yönlendirme alanında olsa da tür ve ünlem sınırları farklıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İşlevler yakın olsa da odak yalnızca keçiye yöneltilen kendi kovma ünlemine, komşu ise farklı bir ses ve daha geniş hayvan kapsamına bağlıdır.","focus_only":"Belirli bir ünlemle özellikle keçiyi kovma eylemidir.","gloss":"keçiyi farklı ünlemlerle yönlendirme","neighbor_only":"Başka bir seslenişle keçi veya koyunu çağırma ve azarlama kapsamı vardır.","neighbor_ref":"root_000477/B003","relation_type":"near_synonym","shared_zone":"İki dal küçükbaş hayvana seslenerek onu çağırma, sürme veya azarlama işlevinde örtüşür."}],"source_phrase_ar":"يقال للعنز إذا زجرت عز عز (tahdhib); عزعزت بها فلم تعزعز (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Keçiye özgü kovma ünlemi ve ondan kurulan sürme eylemi yalnızca bu tanıklıkta yer alır."}],"source_summary":"Tek tanıklık, keçiye yöneltilen kovma ünlemiyle bu ünlemi söyleyerek hayvanı sürme eylemini birlikte kaydeder.","sources":["TA"],"what_is_ar":"يدخل فيه قول عز عز عند زجر العنز وما اتصل به من عزعزت بها","what_is_not_ar":"ليس من عزة القوة ولا من غلبة الخصم"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["14:20:1"],"branch_refs":[],"candidate_id":"cand_da013dd4025c01198c9f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:1:fused-negating-onset","source_type":"word_analysis","support_ids":["sup_456d7c1b4512c8c823b1","sup_8cc3fb769ca0caf4c219"],"title":"connector fused to denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:1","qac_refs":["14:20:1:1"],"status":"accepted"}},{"anchor_refs":["14:20:1"],"branch_refs":[],"candidate_id":"cand_bde589ebfd2faa804122","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:1:resumptive-coda","source_type":"word_analysis","support_ids":["sup_8cc3fb769ca0caf4c219","sup_a1ec86350fe5e7690d8d"],"title":"linked closure after 14:19","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:1","qac_refs":["14:20:1:1"],"status":"accepted"}},{"anchor_refs":["14:20:2"],"branch_refs":[],"candidate_id":"cand_b6eb72af653639aaa0e3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:2:case-dispute-neutralized","source_type":"word_analysis","support_ids":["sup_36f41327d56f4e1a9dad","sup_633205c4b2446e00379c"],"title":"case does not settle the mā analysis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:2","qac_refs":["14:20:1:2"],"status":"accepted"}},{"anchor_refs":["14:20:2"],"branch_refs":[],"candidate_id":"cand_0774305ff74e93a732b2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:2:local-negative-reparse","source_type":"word_analysis","support_ids":["sup_633205c4b2446e00379c","sup_8c025153a5eaf7f9f662"],"title":"polyfunctional particle locally negates","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:2","qac_refs":["14:20:1:2"],"status":"accepted"}},{"anchor_refs":["14:20:2"],"branch_refs":[],"candidate_id":"cand_a51c45e9b823e2e88f96","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:2:nominal-static-denial","source_type":"word_analysis","support_ids":["sup_633205c4b2446e00379c","sup_ac52ba282818b46a07cf"],"title":"verbless non-difficulty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:2","qac_refs":["14:20:1:2"],"status":"accepted"}},{"anchor_refs":["14:20:2"],"branch_refs":[],"candidate_id":"cand_52d03eb96b99a0383af3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:2:opening-cadence","source_type":"word_analysis","support_ids":["sup_633205c4b2446e00379c","sup_808598609b5bb497b4b7"],"title":"light onset before dense closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:2","qac_refs":["14:20:1:2"],"status":"accepted"}},{"anchor_refs":["14:20:2"],"branch_refs":[],"candidate_id":"cand_0c9809ee96e96371d7ee","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:2:reinforced-clause-negation","source_type":"word_analysis","support_ids":["sup_633205c4b2446e00379c","sup_bcace4348ad018c4a38b"],"title":"reinforced clause-wide denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:2","qac_refs":["14:20:1:2"],"status":"accepted"}},{"anchor_refs":["14:20:3"],"branch_refs":[],"candidate_id":"cand_0e781f037e595cd3a527","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:3:anaphoric-subject","source_type":"word_analysis","support_ids":["sup_370469a2f2f33be84add","sup_c0d1e08500f9f5e74b53"],"title":"backward-pointing subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:3","qac_refs":["14:20:2:1"],"status":"accepted"}},{"anchor_refs":["14:20:3"],"branch_refs":[],"candidate_id":"cand_110ede66d91de05f0804","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:3:compact-referent","source_type":"word_analysis","support_ids":["sup_bff7ae4be79725fd0aa3","sup_c0d1e08500f9f5e74b53"],"title":"prior action condensed into a pointer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:3","qac_refs":["14:20:2:1"],"status":"accepted"}},{"anchor_refs":["14:20:3"],"branch_refs":[],"candidate_id":"cand_e81480dc19b6f2a6300c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:3:far-deictic-remoteness","source_type":"word_analysis","support_ids":["sup_8617be10938ae1e77db1","sup_c0d1e08500f9f5e74b53"],"title":"remote yet recoverable referent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:3","qac_refs":["14:20:2:1"],"status":"accepted"}},{"anchor_refs":["14:20:3"],"branch_refs":[],"candidate_id":"cand_590f9988ac18741bc43d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:3:formula-variable","source_type":"word_analysis","support_ids":["sup_c0335bf6d7a8847f4b5e","sup_c0d1e08500f9f5e74b53"],"title":"variable slot in repeated formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:3","qac_refs":["14:20:2:1"],"status":"accepted"}},{"anchor_refs":["14:20:3"],"branch_refs":[],"candidate_id":"cand_032882869326d6afff20","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:3:word-order-suspense","source_type":"word_analysis","support_ids":["sup_3bcfd1c2b83fe2db01cd","sup_c0d1e08500f9f5e74b53"],"title":"subject before divine frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:3","qac_refs":["14:20:2:1"],"status":"accepted"}},{"anchor_refs":["14:20:4"],"branch_refs":[],"candidate_id":"cand_15d6464cca127cffb04d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:4:burden-frame","source_type":"word_analysis","support_ids":["sup_b5516c9b70307f9aa2ae","sup_c226f2a749ac50a44551"],"title":"difficulty as denied burden upon God","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:4","qac_refs":["14:20:3:1"],"status":"accepted"}},{"anchor_refs":["14:20:4"],"branch_refs":[],"candidate_id":"cand_599f3c70fb088bbe153e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:4:intervening-divine-frame","source_type":"word_analysis","support_ids":["sup_b5516c9b70307f9aa2ae","sup_bbaaad62d06d4adb741d"],"title":"divine phrase before predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:4","qac_refs":["14:20:3:1"],"status":"accepted"}},{"anchor_refs":["14:20:4"],"branch_refs":[],"candidate_id":"cand_9aa0aa69f751ee6a745f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:4:spatial-pressure","source_type":"word_analysis","support_ids":["sup_976addc6f592a4094e59","sup_b5516c9b70307f9aa2ae"],"title":"upon-ness becomes pressure language","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:4","qac_refs":["14:20:3:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_70443db723dca7069bef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:divine-name-aziz-inversion","source_type":"word_analysis","support_ids":["sup_c71bbad4adfd48f1270f","sup_e0dab9520adcddf2963f"],"title":"attribute pairing inverted locally","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_66c37ae2142e1dde00bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:governed-proper-name","source_type":"word_analysis","support_ids":["sup_ccc61a9ca5ab0fd29d38","sup_e0dab9520adcddf2963f"],"title":"proper name inside the burden phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_979f6e02b07ab49c5f72","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:named-refuge-not-generic-class","source_type":"word_analysis","support_ids":["sup_179ff54bb5c12e82c16e","sup_e0dab9520adcddf2963f"],"title":"named God, not generic deity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_15d0ccf35c94231ace8e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:sound-and-attachment","source_type":"word_analysis","support_ids":["sup_1456683eb0b6345f58a7","sup_e0dab9520adcddf2963f"],"title":"recited attachment to the preposition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_13852f7c54105526345c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:surah-agent-thread","source_type":"word_analysis","support_ids":["sup_6975466376c31620965c","sup_e0dab9520adcddf2963f"],"title":"surah-local divine reference","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_f2f9f6d5cb4289100092","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:5:worship-bewilderment-pressure","source_type":"word_analysis","support_ids":["sup_64638551ea4642e11eac","sup_e0dab9520adcddf2963f"],"title":"human bewilderment reversed into divine ease","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:5","qac_refs":["14:20:4:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_2d6c73c0ea19aea953ad","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:case-role-mask","source_type":"word_analysis","support_ids":["sup_499f5e122511ff40190e","sup_49db6aa95a7db12a52aa"],"title":"genitive surface, predicate role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_ba9968e6c00af69075ca","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:creation-bridge","source_type":"word_analysis","support_ids":["sup_499f5e122511ff40190e","sup_7f155867dc7b4da18ab3"],"title":"from new creation to denied difficulty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_270927cd8d6fc8fb31d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:distributed-negation-frame","source_type":"word_analysis","support_ids":["sup_3d8678ac1596ac6f677d","sup_499f5e122511ff40190e"],"title":"mā and bāʾ bracket the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_74eced8883aa43fe26be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:fused-final-predicate","source_type":"word_analysis","support_ids":["sup_0e3cc94e792234f10a78","sup_499f5e122511ff40190e"],"title":"bound form marks the final predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_e605d6488cbe2180b1d0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:ordinary-ba-narrowed","source_type":"word_analysis","support_ids":["sup_499f5e122511ff40190e","sup_8bde17aea2c2098d24ed"],"title":"ordinary contact senses stripped back","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:6"],"branch_refs":[],"candidate_id":"cand_6b19c1bf68ba6da18993","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"14:20:6:reinforcing-ba","source_type":"word_analysis","support_ids":["sup_499f5e122511ff40190e","sup_cbc5197749cfeed44e98"],"title":"bāʾ zāʾida strengthens denial","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:6","qac_refs":["14:20:5:1"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_f3ff82fd2afb35dc709b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:agreement-with-demonstrative","source_type":"word_analysis","support_ids":["sup_6061812ce2536d2288af","sup_d40ecd30e5b3ff96d191"],"title":"predicate binds back to the demonstrative","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_df518e16e8b0a823baaa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:case-dispute-neutralized","source_type":"word_analysis","support_ids":["sup_0b6652fa9eec00ba2a80","sup_d40ecd30e5b3ff96d191"],"title":"case cannot decide the mā dispute","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_a793d7b4ecd4bfeed981","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:causative-forms-excluded","source_type":"word_analysis","support_ids":["sup_9c9426b094ff69f0ac47","sup_d40ecd30e5b3ff96d191"],"title":"adjective, not causative action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_84b573a3721357731944","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:denied-predicate-grammar","source_type":"word_analysis","support_ids":["sup_d40ecd30e5b3ff96d191","sup_f5318e5147e20f5ae973"],"title":"genitive adjective remains denied predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_86f4d56e1175a1bfbcc8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:difficult-inaccessible-sense","source_type":"word_analysis","support_ids":["sup_d40ecd30e5b3ff96d191","sup_dde7c91fd8465ae51ed2"],"title":"difficulty enriched by inaccessibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_c49bbe53fa7065ee710a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:divine-title-inversion","source_type":"word_analysis","support_ids":["sup_4c76d9bb6453aa3d8fd4","sup_d40ecd30e5b3ff96d191"],"title":"divine title field reversed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_0872e9fe6e7f733432a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:final-landing","source_type":"word_analysis","support_ids":["sup_712b9059e8e10a469f20","sup_d40ecd30e5b3ff96d191"],"title":"predicate as ayah closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_6427019a89bfd3f4bbd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:formulaic-closure","source_type":"word_analysis","support_ids":["sup_36ed5ac0b8c853abc045","sup_d40ecd30e5b3ff96d191"],"title":"repeatable capacity seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_68b048e6aaf1b04eaf54","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:fortress-scarcity-image","source_type":"word_analysis","support_ids":["sup_8fbd6992d910b3bb2819","sup_d40ecd30e5b3ff96d191"],"title":"no fortified or scarce obstacle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_1d1d1b33e87698a95a0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:forward-exposure-bridge","source_type":"word_analysis","support_ids":["sup_d40ecd30e5b3ff96d191","sup_e00da0f319fe20ef2f39"],"title":"denied inaccessibility before exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_ef125dd9f0552af9fe55","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:marked-adjective-use","source_type":"word_analysis","support_ids":["sup_20147df504d310625021","sup_d40ecd30e5b3ff96d191"],"title":"marked predicate use of familiar root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_f6a7858e938e81e45c2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:mighty-not-overpowering","source_type":"word_analysis","support_ids":["sup_4bd83720cf4bb26ff5ec","sup_d40ecd30e5b3ff96d191"],"title":"mighty resistance denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_fc0859b8a7421c29a8b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:nominal-coda","source_type":"word_analysis","support_ids":["sup_191297a3d0a8e43a5102","sup_d40ecd30e5b3ff96d191"],"title":"static closure after dynamic threat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_4a510f6cc3e91ddd82df","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:phonetic-weight","source_type":"word_analysis","support_ids":["sup_72630373af6c8ce28ce4","sup_d40ecd30e5b3ff96d191"],"title":"heavy sound denied by grammar","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_441663886e35fefe36a9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:settled-quality-negated","source_type":"word_analysis","support_ids":["sup_33010596b7c7d93b110f","sup_d40ecd30e5b3ff96d191"],"title":"faʿīl quality denied as settled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:7"],"branch_refs":[],"candidate_id":"cand_d7634a4374ea74ec35a8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:7:surah-power-thread","source_type":"word_analysis","support_ids":["sup_99ff8601f8fbf48db7e5","sup_d40ecd30e5b3ff96d191"],"title":"same-surah power thread at 14:4 and 14:47","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"14:20:7","qac_refs":["14:20:5:2"],"status":"accepted"}},{"anchor_refs":["14:20:4"],"branch_refs":[],"candidate_id":"cand_05e949f8da837634935f","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"14:20:4:1","source_type":"qac_morpheme","support_ids":["sup_88fd4806d137160d69e2"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["14:20:5"],"branch_refs":[],"candidate_id":"cand_c26d0cfd3dc07b709616","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001008"],"scope":"focus_ayah","source_local_id":"14:20:5:2","source_type":"qac_morpheme","support_ids":["sup_11d04ae6dc871baff9b5"],"title":"QAC root occurrence: ع ز ز","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["14:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"14:20","branch_refs":["root_001008/B005"],"candidate_id":"cand_ef75f62fff7795d680a0","commentary_obligation":"review","hft_ref":"hft_71c182aab9c4bd7cadda","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_difficulty_burden","source_type":"hft","support_ids":["sup_007ec6e3a97e3f16395e"],"title":"b_difficulty_burden","trust":"legacy_unbound"},{"anchor_refs":["14:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"14:20","branch_refs":["root_001008/B003"],"candidate_id":"cand_919935841d58b1ceac26","commentary_obligation":"review","hft_ref":"hft_d76db1c3c5918fd1e87f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_unattainable_object","source_type":"hft","support_ids":["sup_429d60eb8f71dfb3ee5d"],"title":"b_unattainable_object","trust":"legacy_unbound"},{"anchor_refs":["14:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"14:20","branch_refs":["root_001008/B002","root_001008/B009"],"candidate_id":"cand_da4afc7cd3077fd14683","commentary_obligation":"review","hft_ref":"hft_650a33cc688aad547d57","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_overmastering_affair","source_type":"hft","support_ids":["sup_ad60ff93718074053d21"],"title":"b_overmastering_affair","trust":"legacy_unbound"},{"anchor_refs":["14:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"14:20","branch_refs":["root_001008/B007"],"candidate_id":"cand_daae2a6b87278baac4af","commentary_obligation":"review","hft_ref":"hft_0030e6f2058d96eeeae3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_cohesive_resistance","source_type":"hft","support_ids":["sup_8407e8aa4e90fe417077"],"title":"b_cohesive_resistance","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"14:20:1:1","qac_word_ref":"14:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"14:20:1:2","qac_word_ref":"14:20:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"14:20:2:1","qac_word_ref":"14:20:2","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"14:20:3:1","qac_word_ref":"14:20:3","root_ar":"","surface_ar":"عَلَى"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"14:20:4:1","qac_word_ref":"14:20:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"14:20:5:1","qac_word_ref":"14:20:5","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","root_ar":"ع ز ز","surface_ar":"عَزِيزٍ"}],"word_analysis_qac_refs":[["14:20:1:1"],["14:20:1:2"],["14:20:2:1"],["14:20:3:1"],["14:20:4:1"],["14:20:5:1"],["14:20:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["14:20:1","14:20:2","14:20:3","14:20:4","14:20:5","14:20:6","14:20:7"]},"focus_surface_evidence":{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"14:20:1:1","qac_word_ref":"14:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"14:20:1:2","qac_word_ref":"14:20:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"14:20:2:1","qac_word_ref":"14:20:2","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"14:20:3:1","qac_word_ref":"14:20:3","root_ar":"","surface_ar":"عَلَى"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"14:20:4:1","qac_word_ref":"14:20:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"14:20:5:1","qac_word_ref":"14:20:5","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"عَزِيز","morph_features":"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"14:20:5:2","qac_word_ref":"14:20:5","root_ar":"ع ز ز","surface_ar":"عَزِيزٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["14:20:1:1"],["14:20:1:2"],["14:20:2:1"],["14:20:3:1"],["14:20:4:1"],["14:20:5:1"],["14:20:5:2"]],"word_analysis_refs":["14:20:1","14:20:2","14:20:3","14:20:4","14:20:5","14:20:6","14:20:7"],"word_rows":[{"analysis_record_ref":"14:20:1","analytic_gloss_range_en":"resumptive or coordinative connector that joins the ayah to the prior removal-and-replacement claim","analytic_root_gloss_range_en":null,"qac_refs":["14:20:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"14:20:2","analytic_gloss_range_en":"negative particle governing the clause-level denial, strengthened later by the bound bāʾ predicate","analytic_root_gloss_range_en":null,"qac_refs":["14:20:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"14:20:3","analytic_gloss_range_en":"far demonstrative subject resuming the removal-and-replacement proposition from 14:19","analytic_root_gloss_range_en":null,"qac_refs":["14:20:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"14:20:4","analytic_gloss_range_en":"preposition establishing the divine reference point upon whom the denied burden would bear","analytic_root_gloss_range_en":null,"qac_refs":["14:20:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَى","transliteration":"ʿalā"}},{"analysis_record_ref":"14:20:5","analytic_gloss_range_en":"the definite proper divine name as governed complement inside the burden-frame","analytic_root_gloss_range_en":"divine-name field tied in the supplied rows to worship, refuge, and bewilderment; the local form is the proper name, not a generic deity noun","qac_refs":["14:20:4:1"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"ٱللَّهِ","transliteration":"allāhi"}},{"analysis_record_ref":"14:20:6","analytic_gloss_range_en":"bound reinforcing bāʾ on the negated predicate, creating visible genitive without ordinary instrumental meaning","analytic_root_gloss_range_en":null,"qac_refs":["14:20:5:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"14:20:7","analytic_gloss_range_en":"negated qualitative predicate: not difficult, inaccessible, overpowering, or scarce with respect to God","analytic_root_gloss_range_en":"might, honor, overcoming, rarity, inaccessibility, severity, and difficulty; the local adjective selects the difficult/inaccessible burden sense under negation while echoing divine-might uses at 14:4 and 14:47","qac_refs":["14:20:5:2"],"root":{"arabic":"ع ز ز","transliteration":"ʿ-z-z"},"surface":{"arabic":"عَزِيزٍۢ","transliteration":"ʿazīzin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["14:20"],"branch_refs":["root_001008/B005"],"candidate_id":"cand_ef75f62fff7795d680a0","evidence_scope":"focus_ayah","hft_ref":"hft_71c182aab9c4bd7cadda","item_id":"b_difficulty_burden","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_difficulty_burden","support_id":"sup_007ec6e3a97e3f16395e"},{"anchor_refs":["14:20"],"branch_refs":["root_001008/B003"],"candidate_id":"cand_919935841d58b1ceac26","evidence_scope":"focus_ayah","hft_ref":"hft_d76db1c3c5918fd1e87f","item_id":"b_unattainable_object","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_unattainable_object","support_id":"sup_429d60eb8f71dfb3ee5d"},{"anchor_refs":["14:20"],"branch_refs":["root_001008/B002","root_001008/B009"],"candidate_id":"cand_da4afc7cd3077fd14683","evidence_scope":"focus_ayah","hft_ref":"hft_650a33cc688aad547d57","item_id":"b_overmastering_affair","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_overmastering_affair","support_id":"sup_ad60ff93718074053d21"},{"anchor_refs":["14:20"],"branch_refs":["root_001008/B007"],"candidate_id":"cand_daae2a6b87278baac4af","evidence_scope":"focus_ayah","hft_ref":"hft_0030e6f2058d96eeeae3","item_id":"b_cohesive_resistance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_cohesive_resistance","support_id":"sup_8407e8aa4e90fe417077"}],"diagnostics":[],"lane_counts":{"global":20,"macro":1,"micro":4},"packet_summary":{"ayah_count":52,"focus_ref":"14:20","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["14:1","14:2","14:3","14:4","14:5","14:6","14:7","14:8","14:9","14:10","14:11","14:12","14:13","14:14","14:15","14:16","14:17","14:18","14:19","14:20","14:21","14:22","14:23","14:24","14:25","14:26","14:27","14:28","14:29","14:30","14:31","14:32","14:33","14:34","14:35","14:36","14:37","14:38","14:39","14:40","14:41","14:42","14:43","14:44","14:45","14:46","14:47","14:48","14:49","14:50","14:51","14:52"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"14:20","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"14:20","lane":"micro","linguistic_source_ref":"14:20","surface_ref":"14:20","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"14:20","target_tokens":[["Bu",["14:20:2"]],["Allah",["14:20:3","14:20:4"]],["için",["14:20:3","14:20:4"]],["zor",["14:20:1","14:20:2","14:20:3","14:20:4","14:20:5"]],["değildir",["14:20:1","14:20:2","14:20:3","14:20:4","14:20:5"]]],"text":"Bu Allah için zor değildir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":16,"ayah_to":27,"id":"s014-p02-016-027","label":"Judgment and parables of belief","number":2,"refs":["14:16","14:17","14:18","14:19","14:20","14:21","14:22","14:23","14:24","14:25","14:26","14:27"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:case-dispute-neutralized","source_type":"word_analysis","support_id":"sup_0b6652fa9eec00ba2a80","text":"{\"blocking_evidence\":null,\"headline\":\"case cannot decide the mā dispute\",\"reader_payoff\":\"The reader avoids using the genitive ending as decisive evidence for one analysis of the negative particle.\",\"reason\":\"The final genitive is caused by the bāʾ, so it does not independently settle the Hijazi-versus-Tamimi analysis.\",\"representative_source_ids\":[\"QG-5b0a0ca8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:fused-final-predicate","source_type":"word_analysis","support_id":"sup_0e3cc94e792234f10a78","text":"{\"blocking_evidence\":null,\"headline\":\"bound form marks the final predicate\",\"reader_payoff\":\"The reader sees the final adjective arrive already carrying the grammar of reinforced denial.\",\"reason\":\"The bāʾ is proclitic to the final adjective and visibly changes its case surface.\",\"representative_source_ids\":[\"QF-798f53f0\",\"QF-c2acc403\",\"QY-0f7028a0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"14:20:5:2","source_type":"qac_morpheme","support_id":"sup_11d04ae6dc871baff9b5","text":"{\"lemma_ar\":\"عَزِيز\",\"morph_features\":\"STEM|POS:N|LEM:Eaziyz|ROOT:Ezz|MS|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"14:20:5:2\",\"qac_word_ref\":\"14:20:5\",\"root_ar\":\"ع ز ز\",\"surface_ar\":\"عَزِيزٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:sound-and-attachment","source_type":"word_analysis","support_id":"sup_1456683eb0b6345f58a7","text":"{\"blocking_evidence\":null,\"headline\":\"recited attachment to the preposition\",\"reader_payoff\":\"The reader hears the preposition and divine name as one governed unit before the dense final predicate.\",\"reason\":\"The formal and phonetic rows cohere with the forced prepositional attachment and do not change the syntactic role.\",\"representative_source_ids\":[\"QF-277fc84e\",\"QP-05cff6a4\",\"QP-72004ac9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:named-refuge-not-generic-class","source_type":"word_analysis","support_id":"sup_179ff54bb5c12e82c16e","text":"{\"blocking_evidence\":null,\"headline\":\"named God, not generic deity\",\"reader_payoff\":\"The reader notices that the denial of difficulty is anchored to the proper divine name rather than to a generic divine category.\",\"reason\":\"The local form is tagged as the proper divine name and the contextual profile gives God as the dominant referent; missing V4 rows for this root do not reject the CRITICAL derivational claim.\",\"representative_source_ids\":[\"QS-5d9a2858\",\"QS-fd72b154\",\"QF-df886a5f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:nominal-coda","source_type":"word_analysis","support_id":"sup_191297a3d0a8e43a5102","text":"{\"blocking_evidence\":null,\"headline\":\"static closure after dynamic threat\",\"reader_payoff\":\"The reader moves from the dynamic conditional act in 14:19 to a timeless judgment of non-difficulty.\",\"reason\":\"The ayah is a negated nominal clause whose demonstrative subject resumes the prior conditional action (14:19).\",\"representative_source_ids\":[\"QT-4fafab18\",\"QT-942a899f\",\"QB-8b631f3b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:marked-adjective-use","source_type":"word_analysis","support_id":"sup_20147df504d310625021","text":"{\"blocking_evidence\":null,\"headline\":\"marked predicate use of familiar root\",\"reader_payoff\":\"The reader sees a familiar divine-power root placed in a less expected negated task-predicate slot.\",\"reason\":\"The contextual profile identifies the local form as a qualitative adjective and shows divine referent associations without making the local word a divine title.\",\"representative_source_ids\":[\"QI-58a10cbd\",\"QI-63de5dee\",\"QH-6c5e22a0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:settled-quality-negated","source_type":"word_analysis","support_id":"sup_33010596b7c7d93b110f","text":"{\"blocking_evidence\":null,\"headline\":\"faʿīl quality denied as settled\",\"reader_payoff\":\"The reader hears the negation remove difficulty as an inherent quality of the act, not only as a present inconvenience.\",\"reason\":\"The local word is a qualitative adjective on the faʿīl pattern and indefinite under negation.\",\"representative_source_ids\":[\"QF-f31963ba\",\"MF-64410073\",\"QF-9f84ae6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:formulaic-closure","source_type":"word_analysis","support_id":"sup_36ed5ac0b8c853abc045","text":"{\"blocking_evidence\":null,\"headline\":\"repeatable capacity seal\",\"reader_payoff\":\"The reader recognizes the phrase as a specialized closure formula for creation or replacement contexts (35:17).\",\"reason\":\"The CRITICAL rows provide the exact repeated phrase at 35:17; this comparison supports formulaic closure without controlling the local parse.\",\"representative_source_ids\":[\"QI-0262dd2e\",\"MI-597b6e89\",\"QH-76771c47\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2:case-dispute-neutralized","source_type":"word_analysis","support_id":"sup_36f41327d56f4e1a9dad","text":"{\"blocking_evidence\":null,\"headline\":\"case does not settle the mā analysis\",\"reader_payoff\":\"The reader avoids over-reading the final genitive as proof of one classical analysis of the negative particle.\",\"reason\":\"The final adjective is genitive because of the reinforcing bāʾ, so surface case cannot by itself decide between the two mā analyses.\",\"representative_source_ids\":[\"QG-ad435dbd\",\"MG-608aa63e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3:anaphoric-subject","source_type":"word_analysis","support_id":"sup_370469a2f2f33be84add","text":"{\"blocking_evidence\":null,\"headline\":\"backward-pointing subject\",\"reader_payoff\":\"The reader resolves the subject as the prior removal-and-replacement act from 14:19, not as a local noun.\",\"reason\":\"Attachment evidence explicitly says the demonstrative resumes the conditional removal and replacement in 14:19.\",\"representative_source_ids\":[\"QG-00d59cde\",\"QB-653a6e96\",\"QY-d32e456b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3:word-order-suspense","source_type":"word_analysis","support_id":"sup_3bcfd1c2b83fe2db01cd","text":"{\"blocking_evidence\":null,\"headline\":\"subject before divine frame\",\"reader_payoff\":\"The reader first receives the threatened act as a subject, then watches it be remeasured by the divine frame.\",\"reason\":\"The demonstrative precedes the intervening prepositional phrase, matching the CRITICAL claim about movement from direct threat to assessed proposition.\",\"representative_source_ids\":[\"QT-7441940a\",\"QB-d15c5c05\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:distributed-negation-frame","source_type":"word_analysis","support_id":"sup_3d8678ac1596ac6f677d","text":"{\"blocking_evidence\":null,\"headline\":\"mā and bāʾ bracket the clause\",\"reader_payoff\":\"The reader notices the denial stretching across the clause, surrounding the demonstrative and divine phrase.\",\"reason\":\"The negative particle opens the clause and the bound bāʾ marks the delayed predicate near the end.\",\"representative_source_ids\":[\"QT-c9db982a\",\"QP-0680e292\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:1:fused-negating-onset","source_type":"word_analysis","support_id":"sup_456d7c1b4512c8c823b1","text":"{\"blocking_evidence\":null,\"headline\":\"connector fused to denial\",\"reader_payoff\":\"The reader hears the coda begin swiftly, with the connector leaning straight into the negation.\",\"reason\":\"The opening particle is attached directly to the following negative particle, matching the CRITICAL claim that linkage and denial are compressed at the onset.\",\"representative_source_ids\":[\"QF-74c58bdd\",\"QP-47e941db\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6","source_type":"word_analysis","support_id":"sup_499f5e122511ff40190e","text":"{\"gloss_range\":\"bound reinforcing bāʾ on the negated predicate, creating visible genitive without ordinary instrumental meaning\",\"prose\":\"{{ar:بِ}} ({{tr:bi}}) is syntactically visible but semantically light: it governs the final adjective's genitive surface while reinforcing the negation begun by {{ar:مَا}} ({{tr:mā}}). Because it is fused to {{ar:عَزِيزٍ}} ({{tr:ʿazīzin}}), the very predicate being denied carries the mark of denial on its face, and ordinary instrument or accompaniment senses are stripped back. The opening negator and this bound bāʾ bracket the demonstrative and divine phrase, so the denial stretches across the clause rather than sitting beside one word. It also answers the prior bridge from 14:19, where bringing a new creation was phrased with {{ar:بِخَلْقٍ}} ({{tr:bi-khalqin}}); here the bound {{ar:بِ}} ({{tr:bi}}) declares that such bringing is not difficult upon God.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:case-role-mask","source_type":"word_analysis","support_id":"sup_49db6aa95a7db12a52aa","text":"{\"blocking_evidence\":null,\"headline\":\"genitive surface, predicate role\",\"reader_payoff\":\"The reader avoids mistaking the genitive case for a loss of predicate function.\",\"reason\":\"Attachment evidence says the final adjective is governed by the reinforcing bāʾ while remaining the denied predicate of the demonstrative.\",\"representative_source_ids\":[\"QG-cf901907\",\"MG-b6b215fa\",\"QF-cf73da38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:mighty-not-overpowering","source_type":"word_analysis","support_id":"sup_4bd83720cf4bb26ff5ec","text":"{\"blocking_evidence\":null,\"headline\":\"mighty resistance denied\",\"reader_payoff\":\"The reader hears the power-root reversed: the act does not overpower God.\",\"reason\":\"The might and overcoming branches remain valid root pressure, but local negation applies them to the act as denied resistance rather than to God as an affirmed attribute.\",\"representative_source_ids\":[\"QS-87fa65d4\",\"MS-18a1055b\",\"QS-bbe2bdc0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:divine-title-inversion","source_type":"word_analysis","support_id":"sup_4c76d9bb6453aa3d8fd4","text":"{\"blocking_evidence\":null,\"headline\":\"divine title field reversed\",\"reader_payoff\":\"The reader distinguishes God as the Mighty from any imagined mighty difficulty upon God.\",\"reason\":\"Contextual profiles show the adjective root often associates with God, while local grammar negates it as a predicate of the act; CRITICAL rows give same-surah and cross-Quran examples (14:4; 14:47; 59:23).\",\"representative_source_ids\":[\"QI-207cd6ee\",\"MI-72c6e8ea\",\"QY-2e215dc3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:agreement-with-demonstrative","source_type":"word_analysis","support_id":"sup_6061812ce2536d2288af","text":"{\"blocking_evidence\":null,\"headline\":\"predicate binds back to the demonstrative\",\"reader_payoff\":\"The reader sees the final adjective evaluate the prior act rather than the nearer divine name.\",\"reason\":\"The predicate relation in attachment evidence links the final adjective to the demonstrative head.\",\"representative_source_ids\":[\"QG-543cbbbb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2","source_type":"word_analysis","support_id":"sup_633205c4b2446e00379c","text":"{\"gloss_range\":\"negative particle governing the clause-level denial, strengthened later by the bound bāʾ predicate\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) supplies the clause's polarity and reaches across the whole nominal sentence, so the prior act resumed by {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) is denied as difficult upon God. The later {{ar:بِ}} ({{tr:bi}}) on the predicate reinforces that denial, while the verbless structure makes non-difficulty a standing relation rather than a narrated process. In isolation this particle can serve other functions, but the local {{ar:مَا}} ({{tr:mā}}) ... {{ar:بِ}} ({{tr:bi}}) frame selects negation and leaves the Hijazi-versus-Tamimi case question unresolved by surface case alone. Its open, light onset gives the denial a quick start before the clause lands on the denser final adjective.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:worship-bewilderment-pressure","source_type":"word_analysis","support_id":"sup_64638551ea4642e11eac","text":"{\"blocking_evidence\":null,\"headline\":\"human bewilderment reversed into divine ease\",\"reader_payoff\":\"The reader feels the human response of refuge and bewilderment while the local clause denies any such difficulty for God.\",\"reason\":\"The derivational dispute and root-family associations are retained as semantic pressure, but the local word remains the fixed proper name in a prepositional phrase.\",\"representative_source_ids\":[\"QS-3da364bb\",\"QS-7e2c3f3f\",\"QS-7fa2827d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:surah-agent-thread","source_type":"word_analysis","support_id":"sup_6975466376c31620965c","text":"{\"blocking_evidence\":null,\"headline\":\"surah-local divine reference\",\"reader_payoff\":\"The reader sees the proper name as part of the surah's repeated divine-agent thread (14:2; 14:10; 14:22; 14:25; 14:27), not as a one-off reference.\",\"reason\":\"The CRITICAL rows provide concrete same-surah references (14:2; 14:10; 14:22; 14:25; 14:27) and corpus root proximity; the local grammar narrows that evidence to background association rather than a new parse.\",\"representative_source_ids\":[\"QE-bd6f9747\",\"QE-e7380dd7\",\"ME-dcd87476\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:final-landing","source_type":"word_analysis","support_id":"sup_712b9059e8e10a469f20","text":"{\"blocking_evidence\":null,\"headline\":\"predicate as ayah closure\",\"reader_payoff\":\"The reader leaves the ayah on the very category being denied, with indefiniteness keeping the exclusion open-ended.\",\"reason\":\"The word is final, indefinite, and marked with tanwīn, matching the CRITICAL closure claim.\",\"representative_source_ids\":[\"QT-e9ba415c\",\"QP-3c0604f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:phonetic-weight","source_type":"word_analysis","support_id":"sup_72630373af6c8ce28ce4","text":"{\"blocking_evidence\":null,\"headline\":\"heavy sound denied by grammar\",\"reader_payoff\":\"The reader feels a dense sound of resistance just before the clause denies resistance upon God.\",\"reason\":\"The phonetic rows are reader-facing sound observations that cohere with the final predicate and do not create a new lexical sense.\",\"representative_source_ids\":[\"QP-1c862ca5\",\"QP-c3a9ce76\",\"MP-c6084364\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:creation-bridge","source_type":"word_analysis","support_id":"sup_7f155867dc7b4da18ab3","text":"{\"blocking_evidence\":null,\"headline\":\"from new creation to denied difficulty\",\"reader_payoff\":\"The reader links the prior new-creation phrase in 14:19 to the current denial of difficulty.\",\"reason\":\"The demonstrative cross-reference to 14:19 supports the boundary row connecting the earlier bāʾ phrase to the present bāʾ-marked predicate.\",\"representative_source_ids\":[\"QB-b8d90018\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2:opening-cadence","source_type":"word_analysis","support_id":"sup_808598609b5bb497b4b7","text":"{\"blocking_evidence\":null,\"headline\":\"light onset before dense closure\",\"reader_payoff\":\"The reader hears the clause begin lightly and decisively before the heavy final predicate is negated.\",\"reason\":\"The CRITICAL cadence claim coheres with the opening sequence and does not alter the grammatical analysis.\",\"representative_source_ids\":[\"QT-607a39c6\",\"QP-a30fca71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3:far-deictic-remoteness","source_type":"word_analysis","support_id":"sup_8617be10938ae1e77db1","text":"{\"blocking_evidence\":null,\"headline\":\"remote yet recoverable referent\",\"reader_payoff\":\"The reader feels the antecedent as conceptually distant or large from a human vantage point before its difficulty is denied.\",\"reason\":\"QAC marks the word as a demonstrative pronoun with far-deixis, and the cross-reference fixes its backward discourse target (14:19).\",\"representative_source_ids\":[\"QS-2e134855\",\"MS-c5e32e33\",\"QF-e0d8a778\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"14:20:4:1","source_type":"qac_morpheme","support_id":"sup_88fd4806d137160d69e2","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"14:20:4:1\",\"qac_word_ref\":\"14:20:4\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:ordinary-ba-narrowed","source_type":"word_analysis","support_id":"sup_8bde17aea2c2098d24ed","text":"{\"blocking_evidence\":null,\"headline\":\"ordinary contact senses stripped back\",\"reader_payoff\":\"The reader recognizes the usual bāʾ range but does not import instrument, cause, or accompaniment into this predicate.\",\"reason\":\"The negated predicate construction narrows the particle to reinforcement, blocking ordinary instrumental lexicalization.\",\"representative_source_ids\":[\"QS-588e80ea\",\"QS-d07cb5f1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2:local-negative-reparse","source_type":"word_analysis","support_id":"sup_8c025153a5eaf7f9f662","text":"{\"blocking_evidence\":null,\"headline\":\"polyfunctional particle locally negates\",\"reader_payoff\":\"The reader can recognize the particle's wider range while seeing that this construction forces the negative reading.\",\"reason\":\"The broader particle range is real, but QAC and local syntax identify the active function here as negation.\",\"representative_source_ids\":[\"QS-b9f80f1e\",\"QF-8843fdc0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:1","source_type":"word_analysis","support_id":"sup_8cc3fb769ca0caf4c219","text":"{\"gloss_range\":\"resumptive or coordinative connector that joins the ayah to the prior removal-and-replacement claim\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens 14:20 as a linked coda, not as a fresh scene. It carries 14:19 forward and lets the denial that follows land as a verdict on the prior possibility of removal and new creation. Because the connector is fused immediately to {{ar:مَا}} ({{tr:mā}}), linkage and negation arrive together: the ayah does not narrate another event but seals the prior threat with a compact statement of capacity.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:fortress-scarcity-image","source_type":"word_analysis","support_id":"sup_8fbd6992d910b3bb2819","text":"{\"blocking_evidence\":null,\"headline\":\"no fortified or scarce obstacle\",\"reader_payoff\":\"The reader imagines impossibility as fortress-like inaccessibility only to see that barrier removed before God.\",\"reason\":\"V4 supports rarity and inaccessibility branches; the local predicate keeps them as metaphorical pressure under the selected difficulty sense.\",\"representative_source_ids\":[\"QS-0afe0f23\",\"QS-115d8da8\",\"QS-df19e8d6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:4:spatial-pressure","source_type":"word_analysis","support_id":"sup_976addc6f592a4094e59","text":"{\"blocking_evidence\":null,\"headline\":\"upon-ness becomes pressure language\",\"reader_payoff\":\"The reader keeps the pressure image of something bearing down while recognizing that local grammar uses it for difficulty, not literal location.\",\"reason\":\"The preposition's concrete range is narrowed by the predicate frame into burden or pressure semantics.\",\"representative_source_ids\":[\"QS-980bd503\",\"QS-bc9589f1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:surah-power-thread","source_type":"word_analysis","support_id":"sup_99ff8601f8fbf48db7e5","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah power thread at 14:4 and 14:47\",\"reader_payoff\":\"The reader hears 14:20 within the surah's power language: affirmed divine might at 14:4 and 14:47 surrounds this denial of obstacle.\",\"reason\":\"The CRITICAL rows provide same-surah references at 14:4 and 14:47 and a broader formula field (35:17); these survive as echo, not as a change to local predicate grammar.\",\"representative_source_ids\":[\"QE-84461588\",\"QE-f420a4f7\",\"QE-3a8f4fa8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:causative-forms-excluded","source_type":"word_analysis","support_id":"sup_9c9426b094ff69f0ac47","text":"{\"blocking_evidence\":null,\"headline\":\"adjective, not causative action\",\"reader_payoff\":\"The reader sees that the ayah denies a quality of the act, not a process of strengthening or making mighty.\",\"reason\":\"The broader family includes causative forms, but QAC tags the local word as a qualitative adjective.\",\"representative_source_ids\":[\"QS-18c99d9f\",\"QS-1e080e7a\",\"QF-cd13f07f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:1:resumptive-coda","source_type":"word_analysis","support_id":"sup_a1ec86350fe5e7690d8d","text":"{\"blocking_evidence\":null,\"headline\":\"linked closure after 14:19\",\"reader_payoff\":\"The reader notices that the ayah is a closure judgment on 14:19 rather than an isolated maxim.\",\"reason\":\"QAC allows coordination or resumption, and the attachment evidence treats the whole ayah as a negated nominal clause continuing the prior discourse (14:19).\",\"representative_source_ids\":[\"QG-f03835fc\",\"QT-45f28d07\",\"QB-77d963e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2:nominal-static-denial","source_type":"word_analysis","support_id":"sup_ac52ba282818b46a07cf","text":"{\"blocking_evidence\":null,\"headline\":\"verbless non-difficulty\",\"reader_payoff\":\"The reader notices that the ayah states a standing capacity relation rather than describing God doing a process.\",\"reason\":\"The clause is syntactically nominal, so the CRITICAL atemporal-denial claim is locally supported.\",\"representative_source_ids\":[\"QG-cad95313\",\"QT-f7256ca8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:4","source_type":"word_analysis","support_id":"sup_b5516c9b70307f9aa2ae","text":"{\"gloss_range\":\"preposition establishing the divine reference point upon whom the denied burden would bear\",\"prose\":\"{{ar:عَلَى}} ({{tr:ʿalā}}) makes the statement a burden-frame: the question is not whether the antecedent looks immense in itself, but whether it bears upon God as difficulty. Its concrete upon-ness remains useful as pressure imagery, yet the negation removes that pressure from the divine side. Because {{ar:عَلَى ٱللَّهِ}} ({{tr:ʿalā llāhi}}) intervenes before the final predicate, the reader meets the divine reference before hearing the quality that cannot attach.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَى}} ({{tr:ʿalā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:4:intervening-divine-frame","source_type":"word_analysis","support_id":"sup_bbaaad62d06d4adb741d","text":"{\"blocking_evidence\":null,\"headline\":\"divine phrase before predicate\",\"reader_payoff\":\"The reader encounters God as the measuring frame before the denied adjective arrives.\",\"reason\":\"The prepositional phrase stands between the demonstrative subject and the final bāʾ-marked predicate.\",\"representative_source_ids\":[\"QT-b3ee17d2\",\"MT-86092475\",\"QB-8d0ef74a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:2:reinforced-clause-negation","source_type":"word_analysis","support_id":"sup_bcace4348ad018c4a38b","text":"{\"blocking_evidence\":null,\"headline\":\"reinforced clause-wide denial\",\"reader_payoff\":\"The reader sees the denial cover the whole proposition, not merely soften the final adjective.\",\"reason\":\"QAC marks the word as a negative particle, and attachment evidence identifies the whole ayah as a negated nominal clause with a reinforcing predicate bāʾ.\",\"representative_source_ids\":[\"QG-3485e72c\",\"QG-7adb5896\",\"QY-acad4d1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3:compact-referent","source_type":"word_analysis","support_id":"sup_bff7ae4be79725fd0aa3","text":"{\"blocking_evidence\":null,\"headline\":\"prior action condensed into a pointer\",\"reader_payoff\":\"The reader sees creation-and-replacement language carried forward without being lexically repeated.\",\"reason\":\"The demonstrative resolves to the prior proposition (14:19), allowing the earlier creation language to be syntactically compressed into one subject.\",\"representative_source_ids\":[\"QG-5df132c1\",\"QT-04a6a37d\",\"QB-d4f1af59\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3:formula-variable","source_type":"word_analysis","support_id":"sup_c0335bf6d7a8847f4b5e","text":"{\"blocking_evidence\":null,\"headline\":\"variable slot in repeated formula\",\"reader_payoff\":\"The reader notices that the demonstrative can carry different antecedents while the same non-difficulty formula remains stable (35:17).\",\"reason\":\"The CRITICAL rows give the exact repeated closure at 35:17, and no guardrail evidence contradicts the formulaic comparison.\",\"representative_source_ids\":[\"MT-b3c348ad\",\"QE-536464ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:3","source_type":"word_analysis","support_id":"sup_c0d1e08500f9f5e74b53","text":"{\"gloss_range\":\"far demonstrative subject resuming the removal-and-replacement proposition from 14:19\",\"prose\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}}) is the subject of the negated nominal sentence, but its content is supplied by 14:19: the possibility of removal and new creation. The far demonstrative turns that prior action into a compact, identifiable referent, distant enough to feel immense from the human side and yet immediately assessed as not difficult upon God. Because the subject appears before the intervening divine frame, the threatened act is first received as the thing being evaluated and only then remeasured by God. In the repeated closure formula (35:17), this same demonstrative position can be filled by another context's antecedent, making {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) the formula's variable slot.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:4:burden-frame","source_type":"word_analysis","support_id":"sup_c226f2a749ac50a44551","text":"{\"blocking_evidence\":null,\"headline\":\"difficulty as denied burden upon God\",\"reader_payoff\":\"The reader sees difficulty framed as a possible burden upon God and then categorically removed.\",\"reason\":\"QAC marks the particle as governing the genitive and bearing relation, and attachment evidence makes the divine name its complement.\",\"representative_source_ids\":[\"QG-a2b36497\",\"MG-036f0576\",\"QI-6e5afc8b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:divine-name-aziz-inversion","source_type":"word_analysis","support_id":"sup_c71bbad4adfd48f1270f","text":"{\"blocking_evidence\":null,\"headline\":\"attribute pairing inverted locally\",\"reader_payoff\":\"The reader distinguishes God's affirmed might from the denied idea that any act could be mighty or difficult upon God.\",\"reason\":\"The contextual data shows a strong God association for the final adjective root, and the CRITICAL rows give same-surah contrast with 14:4 and 14:47.\",\"representative_source_ids\":[\"QI-d7a88897\",\"QI-deb40a27\",\"MI-7ae64e4e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:6:reinforcing-ba","source_type":"word_analysis","support_id":"sup_cbc5197749cfeed44e98","text":"{\"blocking_evidence\":null,\"headline\":\"bāʾ zāʾida strengthens denial\",\"reader_payoff\":\"The reader sees that the denial is strengthened rather than merely stated with a simple bare predicate.\",\"reason\":\"QAC identifies the preposition as bāʾ zāʾida reinforcing the negation, and translation support warns not to lexicalize it as an independent preposition.\",\"representative_source_ids\":[\"QG-dfc0b8a6\",\"MG-e3b799d5\",\"QI-cb24a724\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5:governed-proper-name","source_type":"word_analysis","support_id":"sup_ccc61a9ca5ab0fd29d38","text":"{\"blocking_evidence\":null,\"headline\":\"proper name inside the burden phrase\",\"reader_payoff\":\"The reader keeps God as the reference point of denied difficulty without misparsing the divine name as the subject.\",\"reason\":\"QAC marks the word as a definite proper noun governed by the preposition, while attachment evidence identifies the demonstrative as the head of the denied predicate relation.\",\"representative_source_ids\":[\"QG-10d40897\",\"QG-746fce03\",\"QG-a7655995\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7","source_type":"word_analysis","support_id":"sup_d40ecd30e5b3ff96d191","text":"{\"gloss_range\":\"negated qualitative predicate: not difficult, inaccessible, overpowering, or scarce with respect to God\",\"prose\":\"{{ar:عَزِيزٍۢ}} ({{tr:ʿazīzin}}) is the final predicate, genitive by the bound {{ar:بِ}} ({{tr:bi}}) yet semantically denied of the antecedent carried by {{ar:ذَٰلِكَ}} ({{tr:dhālika}}), not of the nearer divine name; that bāʾ-caused genitive also keeps the Hijazi-versus-Tamimi analysis of {{ar:مَا}} ({{tr:mā}}) from being decided by case alone. The prior replacement scene in 14:19 selects the difficulty branch, but the wider {{ar:ع ز ز}} ({{tr:ʿ-z-z}}) field gives that difficulty texture: what might be mighty, rare, fortified, or inaccessible is all removed as a burden upon God. The surface adjective, not a Form II or Form IV causative, denies a quality borne by the act itself; as a faʿīl quality, the denial feels settled rather than temporary. The word also reverses a familiar expectation: {{ar:ٱلْعَزِيزُ}} ({{tr:al-ʿazīzu}}) names God's might at 14:4, divine avenging might returns at 14:47, the exact closure formula recurs at 35:17, and this marked adjective predicate denies that anything can be {{ar:عَزِيزٍ}} ({{tr:ʿazīzin}}) upon God. As the ayah's final indefinite word, it turns the dynamic threat of 14:19 into a timeless closure and leaves no open instance of difficulty; its dense final sound lets the idea of resistance be felt before the grammar dismisses it, while the denied inaccessibility prepares the exposed emergence before God in 14:21.\",\"root_display\":\"{{ar:ع ز ز}} ({{tr:ʿ-z-z}})\",\"root_gloss_range\":\"might, honor, overcoming, rarity, inaccessibility, severity, and difficulty; the local adjective selects the difficult/inaccessible burden sense under negation while echoing divine-might uses at 14:4 and 14:47\",\"surface_display\":\"{{ar:عَزِيزٍۢ}} ({{tr:ʿazīzin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:difficult-inaccessible-sense","source_type":"word_analysis","support_id":"sup_dde7c91fd8465ae51ed2","text":"{\"blocking_evidence\":null,\"headline\":\"difficulty enriched by inaccessibility\",\"reader_payoff\":\"The reader gets more than a flat 'easy': the act is not difficult, scarce in divine capacity, or walled off from God's reach.\",\"reason\":\"V4 accepts branches for might, rarity, inaccessibility, and difficulty, while the 14:19 antecedent narrows the active local sense to difficulty with accessible root-image pressure.\",\"representative_source_ids\":[\"QS-e152f36b\",\"QS-9ae5658a\",\"QY-8b29c698\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:forward-exposure-bridge","source_type":"word_analysis","support_id":"sup_e00da0f319fe20ef2f39","text":"{\"blocking_evidence\":null,\"headline\":\"denied inaccessibility before exposure\",\"reader_payoff\":\"The reader can connect the denial of any fortified obstacle here with the exposed emergence before God in 14:21.\",\"reason\":\"The boundary row gives the forward link to the next ayah (14:21); it is kept as bridge evidence without altering the local sense.\",\"representative_source_ids\":[\"QB-a4123b6e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:5","source_type":"word_analysis","support_id":"sup_e0dab9520adcddf2963f","text":"{\"gloss_range\":\"the definite proper divine name as governed complement inside the burden-frame\",\"prose\":\"{{ar:ٱللَّهِ}} ({{tr:allāhi}}) is governed by {{ar:عَلَى}} ({{tr:ʿalā}}), so it is not the sentence subject; the subject remains the prior act carried by {{ar:ذَٰلِكَ}} ({{tr:dhālika}}). Yet the proper name is structurally central, because the act is measured specifically upon God, not upon an abstract deity category. The supplied root-family pressure of worship, refuge, and bewilderment survives as a narrowed payoff: the act that would overwhelm creatures is placed before the named refuge of worship, for whom it is not bewildering or difficult. The name also belongs to the surah's repeated divine-agent thread (14:2; 14:10; 14:22; 14:25; 14:27), and in recitation it leans as one governed unit with the preposition before the dense final predicate. The same surah contrast matters: {{ar:ٱلْعَزِيزُ}} ({{tr:al-ʿazīzu}}) is affirmed of God at 14:4, while {{ar:عَزِيزٍ}} ({{tr:ʿazīzin}}) is denied as a burden upon God here and divine avenging might returns at 14:47.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"divine-name field tied in the supplied rows to worship, refuge, and bewilderment; the local form is the proper name, not a generic deity noun\",\"surface_display\":\"{{ar:ٱللَّهِ}} ({{tr:allāhi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"14:20:7:denied-predicate-grammar","source_type":"word_analysis","support_id":"sup_f5318e5147e20f5ae973","text":"{\"blocking_evidence\":null,\"headline\":\"genitive adjective remains denied predicate\",\"reader_payoff\":\"The reader reads the final word as the predicate denied of the prior act, not as an affirmed divine attribute.\",\"reason\":\"QAC and attachment evidence identify the adjective as bāʾ-governed, indefinite, and the denied predicate of the demonstrative.\",\"representative_source_ids\":[\"QG-ce3ddeb9\",\"QG-f98ce307\",\"QF-6bb9f4e9\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","ayah_ref":"14:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001008/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001008","role":"The severe-impact and difficulty branch supplies the denied burden.","root":"ع ز ز","source_ref":"14:20","source_word_indices":["5"]}],"changed_reading":{"after":"The unspecified matter does not weigh as a difficult or severe undertaking upon Allah.","before":"Aziz is heard only as an honorific meaning mighty or honorable."},"confidence":"strong","focus_anchor":"The negated predicate at focus word 5 stands in the construction 'not ... upon Allah.'","mechanism":"The severe-impact branch makes the demonstrative matter a burden whose difficulty is denied relative to Allah.","model_id":"b_difficulty_burden"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_difficulty_burden","source_type":"hft","support_id":"sup_007ec6e3a97e3f16395e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","ayah_ref":"14:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001008/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001008","role":"The rarity and hard-to-attain branch turns difficulty into denied inaccessibility.","root":"ع ز ز","source_ref":"14:20","source_word_indices":["5"]}],"changed_reading":{"after":"The matter is denied the status of a scarce or unobtainable outcome for Allah.","before":"The matter is merely said to be easy."},"confidence":"medium","focus_anchor":"The focus predicate at word 5 can describe rarity and resistance to attainment.","mechanism":"Negation removes scarcity or inaccessibility from the demonstrative: no needed outcome lies beyond Allah's reach as a rare object would.","model_id":"b_unattainable_object"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_unattainable_object","source_type":"hft","support_id":"sup_429d60eb8f71dfb3ee5d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","ayah_ref":"14:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001008/B002","root_001008/B009"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001008","role":"The prevailing-over-an-opponent branch supplies the adversarial resistance being denied.","root":"ع ز ز","source_ref":"14:20","source_word_indices":["5"]},{"branch_id":"B009","mapped_root_id":"root_001008","role":"The branch of an affair becoming dominant supplies the intractability being denied.","root":"ع ز ز","source_ref":"14:20","source_word_indices":["5"]}],"changed_reading":{"after":"The matter cannot become an opponent or runaway affair that overmasters Allah.","before":"The statement concerns effort alone."},"confidence":"medium","focus_anchor":"The focus root at word 5 includes prevailing over an opponent and an affair becoming dominant.","mechanism":"The negation denies that the demonstrative either defeats Allah from outside or grows into an intractable affair that masters its agent.","model_id":"b_overmastering_affair"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_overmastering_affair","source_type":"hft","support_id":"sup_ad60ff93718074053d21","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا ذَٰلِكَ عَلَى ٱللَّهِ بِعَزِيزٍۢ","ayah_ref":"14:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001008/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001008","role":"The hard-ground and cohesion branch supplies a material image of denied resistance.","root":"ع ز ز","source_ref":"14:20","source_word_indices":["5"]}],"changed_reading":{"after":"The matter presents no compact, unyielding resistance before Allah.","before":"Difficulty is an abstract measure of effort."},"confidence":"exploratory","focus_anchor":"The focus predicate at word 5 has a material branch of hard ground and cohesive matter.","mechanism":"The demonstrative is pictured as lacking compact solidity that would make an operation meet an unyielding substrate.","model_id":"b_cohesive_resistance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_cohesive_resistance","source_type":"hft","support_id":"sup_8407e8aa4e90fe417077","trust":"legacy_unbound"}]}
</lane_packet_json>
