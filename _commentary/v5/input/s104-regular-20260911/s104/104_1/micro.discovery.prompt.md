# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **104:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s104-regular-20260911/s104/104_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "104:1",
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
{"analysis_context":{"analysis_id":"s104-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"104:1","host_surah":104,"lane_context_refs":[],"ordered_context_refs":["104:0","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal bütünlük bildiren kullanımları ve mirasla ilgili akrabalık anlamını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"körelip güçten düşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Keskinliğin, gücün veya iş görme yetisinin azalması temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürüyen insanın ya da hayvanın yorulması ve kılıç, dil, bakış, işitme veya rüzgarın etkisizleşmesi bu çekirdeğin gerçekleşmeleridir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli ettirgen söz öbeği, kişinin bineğini yorup güçten düşürmesini anlatır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Keskinlik, dayanma gücü veya etkinlik kaybının birlikte anlatıldığı dal çekirdeğine uygundur.","boundary_detail":"Bu dal bütünlük bildiren kullanımları ve mirasla ilgili akrabalık anlamını kapsamaz.","branch_image_ar":"الكَلال وخلاف الحدة","concept_gloss":"körelip güçten düşme","contextual_glosses":[{"applicability":"İnsan veya hayvanın yürüme ve çalışma sonucu güçten düştüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı taşıyıcının yorulma ve güç kaybını eksiksiz korur."},"facet_ids":["F002"],"text":"yorulup gücü kesilmek","usage_role":"contextual"},{"applicability":"Kılıç, dil, bakış veya başka bir etkin yetinin keskinliğini yitirdiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Keskinlik ve etkinlik kaybını doğal bir Türkçe karşılıkla korur."},"facet_ids":["F001","F002"],"text":"körelmek","usage_role":"contextual"}],"definition":"Bir insanın, hayvanın, aracın, organın ya da etkin gücün keskinliğini, dayanma gücünü veya iş görme yetisini yitirerek körelmesi ya da yorulmasıdır. Bineği bu duruma düşürme, ayrıca belirli bir ettirgen söz öbeğinde anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Keskinliğin, gücün veya iş görme yetisinin azalması temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Yürüyen insanın ya da hayvanın yorulması ve kılıç, dil, bakış, işitme veya rüzgarın etkisizleşmesi bu çekirdeğin gerçekleşmeleridir."},{"facet_id":"F003","role":"associated_use","statement":"Belirli ettirgen söz öbeği, kişinin bineğini yorup güçten düşürmesini anlatır."}],"identity_rationale":"Kaynak anlatımı, keskinlik veya iş görme gücünün azalmasıyla insanın, hayvanın, rüzgarın ve duyuların yorulmasını aynı çekirdekte toplar. Verilen dal bu ortak güçten düşme sınırını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"körelmek, yorulup güçten düşmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"körleşmiş, yorgun veya etkisiz"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bineğini yorup güçten düşürmek"}],"lexicalization_note":"Tanım yalın güçten düşme anlamını kapsar; bineği yorma anlamı ise yalnız belirtilen ettirgen söz öbeğine bağlıdır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; yalnız bedensel yorgunluk ve güç tükenmesiyle gerçek anlam örtüşmesi kuran iki komşu yayımlandı, aynı kökün öteki eşsesli dalları ayrım sağlamadığı için alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bedensel yorgunlukla sınırlıyken bu dal, aynı güç kaybını araçların keskinliği ile dilin ve duyuların etkinliğine de taşır.","focus_only":"Kılıç, dil, duyu ve rüzgar gibi taşıyıcılarda keskinlik veya etkinlik kaybını da kapsar.","gloss":"bedensel yorgunluk","neighbor_only":null,"neighbor_ref":"root_001070/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da yürüme sonucunda insanın veya hayvanın yorulup güçten düşmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal körelme ile yorulmayı geniş bir taşıyıcı dizisine uygular; komşu dal ise tükenme, kesilme ve bıkkınlık sonucunu daha belirgin kılar.","focus_only":"Kılıç, dil ve rüzgarın etkisizleşmesi bu dalda açıkça yer alır.","gloss":"gücü tükenmişlik","neighbor_only":"Gücün tümüyle tükenmesi, bıkkınlık ve eldekinin bitmesi komşu dalın ek kapsamıdır.","neighbor_ref":"root_000320/B003","relation_type":"near_synonym","shared_zone":"İki dal yorgunluk, bakışın zayıflaması ve gücün kesilmesi alanında örtüşür."}],"source_phrase_ar":"خلاف الحدة وكل السيف واللسان والطرف (maqayis)؛ الكليل السيف الذي لا حد له ولسان كليل والكال المعيي (ayn)؛ كللت من المشي وكل السيف والريح والطرف واللسان (sihah)؛ الكليل السيف ولسان كليل والكال المعيي وثقل سمعه وكل بصره (tahdhib)؛ كل الرجل في مشيته والسيف عن ضريبته واللسان عن الكلام (mufradat)","source_summary":"Kaynaklar, yorulma ile keskinliğini veya etkinliğini yitirmeyi ortak bir güçten düşme alanında birleştirir; kullanım insan, hayvan, kılıç, dil, bakış, işitme ve rüzgar gibi farklı taşıyıcılara uzanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه كلال السيف واللسان والطرف والسمع والبصر، وإعياء الماشي والبعير والراحلة والريح","what_is_not_ar":"لا يدخل فيه الكُلّ بمعنى الإحاطة ولا الكَلالة في الميراث"},"support_links":[]},{"boundary":"Buradaki ağırlık fiziksel ağırlık değil, bir başkasının üstlendiği bakım ve geçim yüküdür.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"bakımı başkasına yük olan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şeyin bakım, geçim veya taşıma bakımından başkasına yük olması çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yetim, çocuğu bulunmayan kişi veya hem çocuğu hem ebeveyni bulunmayan kişi kanıta bağlı özel referanslardır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Taşınan tapınma nesnesi ve geçimi bir kişiye kalan akrabalar, bağımlılık ilişkisinin söz öbeğine bağlı örnekleridir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kaynak anlatımında ağır tabiatlı kişi ve başkası adına iş gören kişi de bu adlandırmanın çevresinde anılır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçim, bakım veya taşıma sorumluluğunun başka bir kişiye düştüğü çekirdek ilişkiye uygundur.","boundary_detail":"Buradaki ağırlık fiziksel ağırlık değil, bir başkasının üstlendiği bakım ve geçim yüküdür.","branch_image_ar":"الكُلّ عيالا وثقلا","concept_gloss":"bakımı başkasına yük olan","contextual_glosses":[{"applicability":"Bir kimsenin geçimini sağlamak zorunda olduğu aile veya yakınlar için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakım sorumluluğunu ve bağımlı kişiler topluluğunu açıkça korur."},"facet_ids":["F001","F003"],"text":"bakmakla yükümlü olduğu kişiler","usage_role":"contextual"},{"applicability":"Yetim veya doğrudan aile desteğinden yoksun kişi için açıklayıcı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin yakın desteğinden yoksun olma özelliğini korur."},"facet_ids":["F002"],"text":"dayanağı olmayan kimse","usage_role":"contextual"}],"definition":"Bakımı, geçimi veya taşınması başkasının sorumluluğuna yük olan kişi ya da şeydir. Yetim, çocuğu bulunmayan kişi veya hem çocuğu hem de ebeveyni bulunmayan kişi gibi geleneksel adlandırmalar ile akrabaların birine bağımlı hale gelmesi bu çekirdeğe bağlı özel kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şeyin bakım, geçim veya taşıma bakımından başkasına yük olması çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Yetim, çocuğu bulunmayan kişi veya hem çocuğu hem ebeveyni bulunmayan kişi kanıta bağlı özel referanslardır."},{"facet_id":"F003","role":"associated_use","statement":"Taşınan tapınma nesnesi ve geçimi bir kişiye kalan akrabalar, bağımlılık ilişkisinin söz öbeğine bağlı örnekleridir."},{"facet_id":"F004","role":"source_variant","statement":"Kaynak anlatımında ağır tabiatlı kişi ve başkası adına iş gören kişi de bu adlandırmanın çevresinde anılır."}],"identity_rationale":"Kaynak sözü, başkasının bakımına ve geçimine yük olan kişiyi çekirdek yapar; yetim, yakın desteği bulunmayan kişi ve bakmakla yükümlü olunan kimse bu alanda sayılır. Dal kullanılabilir, ancak bütün bu kişileri özleri gereği değersizleştiren bir niteleme gibi okunmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bakımı ve geçimi sahibine yük olan"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yetim veya yakın aile desteği bulunmayan kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sahibinin taşıdığı, ona yük olan tapınma nesnesi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bakmakla yükümlü olduğum kişiler"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yakınlarının geçim yükünü üstlenir duruma gelmek"}],"lexicalization_note":"Yalın ad bağımlı kişiyi veya yükü bildirir; akrabaların kişiye yük olması gibi okumalar yalnız verilen söz öbeklerine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; bakım yüküyle doğrudan sınır paylaşan ve aynı geçim senaryosunu aydınlatan iki komşu seçildi, öteki adaylar farklı eylem ve eşsesli anlamlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bakım ve geçimde bağımlı olan kişiyi ya da şeyi öne çıkarır; komşu dal ise taşınan somut veya soyut yükün kendisini adlandırır.","focus_only":"Bakımı üstlenilen kişi veya taşınan şey, yükün kendisi olarak adlandırılır.","gloss":"üstlenilen ağır yük","neighbor_only":"Komşu dal günah, ağır sözleşme ve üstlenilmiş soyut sorumluluğu da kapsar.","neighbor_ref":"root_000037/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin üzerinde kalan ve onu ağırlaştıran yük ilişkisini anlatır."},{"boundary_match":"thematic_only","distinction":"Bu dal kimin başkasının bakımına bağımlı olduğunu belirtir; komşu dal ise bakımı üstlenen kişinin harcamayı genişletme eylemidir.","focus_only":"Bağımlı kişilerin geçim yükü ve bu yükü taşıyanla ilişkisi anlatılır.","gloss":"aileye bol harcama","neighbor_only":"Aile için yapılan harcamanın artırılması ve geçimin genişletilmesi anlatılır.","neighbor_ref":"root_001133/B004","relation_type":"thematic","shared_zone":"İki dal aile bireylerinin geçimini sağlama senaryosunda buluşur."}],"source_phrase_ar":"الكُلّ العيال واليتيم (maqayis)؛ الكل اليتيم والكل الرجل الذي لا ولد له والكل أيضا الذي هو عيال وثقل (ayn)؛ الكل العيال والثقل والكل اليتيم والكل الذي لا ولد له ولا والد (sihah)؛ الكل الثقيل الروح واليتيم والوكيل والذي هو عيال وثقل على صاحبه (tahdhib)","source_summary":"Ortak çekirdek, geçimi veya bakımı bir başkasının üzerinde kalan bağımlı kişi ya da şeydir. Yetim, çocuğu bulunmayan kişi ve hem çocuğu hem ebeveyni bulunmayan kişi öne çıkan özel durumlar, taşınan nesne ile geçimi üstlenilen akrabalar ise ilişkiyi somutlaştıran kullanımlardır. Bir kaynak, ağır tabiatlı kişiyi ve başkası adına iş gören kişiyi de bu adlandırma çevresinde anar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكُلّ بمعنى العيال والثقل، واليتيم، ومن لا ولد له، وما يكون عالة على غيره","what_is_not_ar":"لا يدخل فيه الكُلّ الذي يفيد الإحاطة ولا الكَلالة بوصفها حكما في الورثة"},"support_links":[]},{"boundary":"Bu dal bir şeyin olgunlaşıp tamamlanma sürecini değil, var olan bütünün eksiksiz kapsamını bildirir.","branch_kind":"bare","branch_ref":"root_001315/B003","candidate_links":[{"candidate_id":"cand_5ce8d59c5bd5accadb08","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"bütün, tüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin parçalarının veya bir kümedeki bireylerin hiçbirini dışarıda bırakmadan kapsanması çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük biçimce tekil kullanılırken anlamca bir topluluğun tamamına yönelebilir."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaların veya bireylerin eksiksiz kapsamını bildiren yalın belirleyici için uygundur.","boundary_detail":"Bu dal bir şeyin olgunlaşıp tamamlanma sürecini değil, var olan bütünün eksiksiz kapsamını bildirir.","branch_image_ar":"الكُلّ إحاطة وتماما","concept_gloss":"bütün, tüm","contextual_glosses":[{"applicability":"Tek bir şeyin bütün parçalarının birlikte kastedildiği adlaşmış bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin hiçbir parçasını dışarıda bırakmayan tam kapsamı korur."},"facet_ids":["F001"],"text":"tamamı","usage_role":"contextual"}],"definition":"Bir bütünün parçalarını ya da bir kümenin bireylerini eksiksiz biçimde kapsayan, biçimce tekil olsa da toplu anlam verebilen belirleyicidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin parçalarının veya bir kümedeki bireylerin hiçbirini dışarıda bırakmadan kapsanması çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Sözcük biçimce tekil kullanılırken anlamca bir topluluğun tamamına yönelebilir."}],"identity_rationale":"Kaynak sözü, parçaları veya bireyleri eksiksiz kapsayan ve biçimce tekil olsa da toplu anlam veren belirleyiciyi açıkça tanımlar. Dalın bütünlük ve tamlık çerçevesi bu dilbilgisel çekirdeğe uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bütün, tüm, tamamı"}],"lexicalization_note":"Tanım yalnız yalın kapsam belirleyicisini açıklar; belirli kalıplardan yeni bir temel anlam çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi; sayı bakımından özel kapsam ile tamamlanma durumunu ayıran iki komşu yararlı bulundu, deyimsel bütünlük anlatımları çekirdeği ayrıca keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sayı bakımından genel bir bütünlük belirleyicisidir; komşu dal yalnız iki öğenin ikisini birden kapsayan özel belirleyicileri anlatır.","focus_only":"Her büyüklükteki kümenin veya bir nesnenin parçalarının tamamını kapsayabilir.","gloss":"ikisinin de tamamı","neighbor_only":"Kapsamı özellikle iki öğeyle sınırlıdır ve iki ayrı biçimle kurulur.","neighbor_ref":"root_001317/B007","relation_type":"near_synonym","shared_zone":"Her iki dal belirtilen kümedeki öğeleri eksiksiz kapsar."},{"boundary_match":"partial","distinction":"Bu dal nicel kapsam kuran bir belirleyicidir; komşu dal ise bir şeyin tamam olma durumu ile tamamlanma eylemini de içerir.","focus_only":"Var olan parçaların veya bireylerin eksiksiz olarak kapsama alınmasını bildirir.","gloss":"tamlık ve tamamlanma","neighbor_only":"Bir şeyin gelişip tamamlanması, eksikliğinin giderilmesi veya olgun duruma erişmesi de anlatılır.","neighbor_ref":"root_001318/B001","relation_type":"near_neighbor","shared_zone":"İki dal eksiksizlik ve tam olma düşüncesinde buluşur."}],"source_phrase_ar":"كل اسم موضوع للإحاطة مضاف أبدا (maqayis)؛ كل لفظه واحد ومعناه جمع (sihah)؛ يقع كل على اسم منكور موحد فيؤدي معنى الجماعة وكلهم للإحاطة (tahdhib)؛ لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام (mufradat)","source_summary":"Kaynaklar, sözcüğün parçaları bir araya getirerek tam kapsam verdiğinde ve tekil biçimle topluluğun bütününü gösterdiğinde birleşir. Bir kaynak, sözcüğü daima tamlanan olarak kullanılan bir kapsam adı şeklinde sınırlar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه لفظ الكُلّ لضم الأجزاء وإحاطة الشيء أو الذوات، ومعنى التمام في كل البسط ونحوه","what_is_not_ar":"لا يدخل فيه الكُلّ بمعنى العيال والثقل ولا كلال القوة والحدة"},"support_links":["sup_06fe90d5be6dce824180"]},{"boundary":"Ana baba ile çocuk bu sınıfın dışındadır; olumsuz söz öbeği ise yan koldan değil doğrudan hakla miras almayı bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"üstsoy ve altsoy dışı mirasçılık","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Doğrudan üstsoy ve altsoy dışında kalan yan kol veya uzak akrabalık temel sınırdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, ana babası ve çocuğu bulunmadan ölen kişiye, onun yan kol mirasçılarına veya bu miras biçimine yönelebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Olumsuz miras söz öbeği doğrudan hakla miras almayı, kuzenlik söz öbeği ise uzak akrabalığı belirtir."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana baba ve çocuk dışındaki yakınlar üzerinden kurulan miras ilişkisini açıklamak için uygundur.","boundary_detail":"Ana baba ile çocuk bu sınıfın dışındadır; olumsuz söz öbeği ise yan koldan değil doğrudan hakla miras almayı bildirir.","branch_image_ar":"الكَلالة قرابة عارضة","concept_gloss":"üstsoy ve altsoy dışı mirasçılık","contextual_glosses":[{"applicability":"Ana baba veya çocuk olmayan uzak bir yakının mirasçı olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mirasçının doğrudan soy çizgisi dışında bulunmasını açıkça korur."},"facet_ids":["F001","F002"],"text":"yan koldan mirasçı","usage_role":"contextual"},{"applicability":"Yakın kuzen olmayan, soy bağı daha uzaktan kurulan kuzen için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuzenlik bağının doğrudan ve yakın olmayan derecesini korur."},"facet_ids":["F003"],"text":"uzak kuzen","usage_role":"contextual"}],"definition":"Ana baba ve çocuk dışındaki, özellikle uzak veya yan koldaki yakınlar üzerinden kurulan mirasçılık ve akrabalık ilişkisidir. Ad, böyle bir miras bırakan kişi, bu yolla mirasçı olanlar veya ilişkinin kendisi için kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Doğrudan üstsoy ve altsoy dışında kalan yan kol veya uzak akrabalık temel sınırdır."},{"facet_id":"F002","role":"extension","statement":"Ad, ana babası ve çocuğu bulunmadan ölen kişiye, onun yan kol mirasçılarına veya bu miras biçimine yönelebilir."},{"facet_id":"F003","role":"associated_use","statement":"Olumsuz miras söz öbeği doğrudan hakla miras almayı, kuzenlik söz öbeği ise uzak akrabalığı belirtir."}],"identity_rationale":"Kaynak sözü, ana baba ve çocuk dışındaki mirasçı yakınları, uzak soy bağını ve doğrudan değil yan koldan geçen mirası birlikte verir. Dal doğru yöndedir; ancak adın ölen kişi, mirasçı topluluğu, akrabalık türü veya miras ilişkisinin kendisi için kullanılabildiği açık tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ana baba ve çocuk dışındaki yan kol mirasçılığı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yan koldan değil, doğrudan hakla miras almak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"uzak kuzen"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"soy bakımından daha uzak olmak"}],"lexicalization_note":"Tanım yan kol akrabalığı çekirdeğini korur; doğrudan miras ve uzak kuzenlik okumaları kendi söz öbeklerine bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel akrabalık ve genel miras aktarımı en açıklayıcı iki sınırı verdi, öteki adaylar özel miras hükümleri veya yalnız aynı aile alanındaki uzak konulardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal miras bağlamında doğrudan üstsoy ve altsoyu dışarıda bırakan özel bir akrabalık sınıfıdır; komşu dal soy yakınlığının tamamını kapsar.","focus_only":"Akrabalığı ana baba ve çocuk dışındaki yan kollara ve miras bağlamına sınırlar.","gloss":"kan ve soy yakınlığı","neighbor_only":"Her türlü kan ve soy yakınlığını, doğrudan üstsoy ile altsoyu da kapsar.","neighbor_ref":"root_001212/B003","relation_type":"near_synonym","shared_zone":"İki dal insanlar arasındaki soy bağını ve yakınlık derecesini anlatır."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir akraba ve mirasçı sınıfını sınırlar; komşu dal ise mirasın kaynaktan mirasçıya geçmesi olayının genel adıdır.","focus_only":"Mirasçının doğrudan soy çizgisi dışında bulunma koşulunu öne çıkarır.","gloss":"mirasın mirasçıya geçmesi","neighbor_only":"Malın ölen kişiden herhangi bir yasal veya soy temelli mirasçıya geçmesi olayını anlatır.","neighbor_ref":"root_001639/B001","relation_type":"same_field","shared_zone":"Her iki dal ölen kişiden kalan malın yakınlara geçmesi alanındadır."}],"source_phrase_ar":"الكلالة هم الرجال الورثة وبنو العم الأباعد ومن مات وليس له ولد ولا والد (maqayis)؛ الكل النسب البعيد (ayn)؛ لم يرثه كلالة أي لم يرثه عن عرض والكلالة بنو العم الأباعد (sihah)؛ الكلالة من القرابة ما خلا الوالد والولد (tahdhib)؛ الكلالة اسم لما عدا الولد والوالد من الورثة (mufradat)","source_summary":"Ortak anlatım ana baba ve çocuk dışındaki mirasçı yakınları, uzak kuzenleri ve yan koldan geçen mirası bir araya getirir. Sözcüğün ölen kişiye mi, mirasçılara mı, akrabalığa mı yoksa mirasa mı yöneldiği bağlama göre değişebilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكَلالة للميت أو الوارث أو القرابة التي عدا الوالد والولد، وبنو العم الأباعد، والميراث من عرض لا من قرب مباشر","what_is_not_ar":"لا يدخل فيه الولد والوالد، ولا الإرث عن قرب واستحقاق مباشر"},"support_links":[]},{"boundary":"Dal, çevreleme biçimini temel alır; dikilmiş koruyucu perde veya genel bütünlük belirleyicisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"çevresini kuşak gibi saran oluşum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin çevresini kuşak gibi sarma veya kenarını çevreleyerek belirginleştirme çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Süslü baş kuşağı veya taç ile belirli bir gök konumu, yalın adın özel karşılıklarıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yeri dolaşan bulut ya da başka bir örtümsü bulut görünümü çevreleme çekirdeğinin göğe uzanmasıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çiçeklerle çevrili çayır ve çevresinde küçük bulut parçaları bulunan bulut, belirli niteleme kalıplarıdır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Baş, yer veya göksel görünüm çevresinde kuşatıcı bir sınır oluşturan dal çekirdeğine uygundur.","boundary_detail":"Dal, çevreleme biçimini temel alır; dikilmiş koruyucu perde veya genel bütünlük belirleyicisi değildir.","branch_image_ar":"الإكليل وما يحيط","concept_gloss":"çevresini kuşak gibi saran oluşum","contextual_glosses":[{"applicability":"Başı çevreleyen süslü kuşak veya değerli taşlarla bezeli başlık bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başı saran süslü başlık anlamını doğal ve kısa biçimde korur."},"facet_ids":["F002"],"text":"taç","usage_role":"contextual"},{"applicability":"Ana bulutun çevresinde daha küçük bulut parçalarının bulunduğu görünüm için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Merkezdeki bulutu ve onu çevreleyen parçaları birlikte korur."},"facet_ids":["F004"],"text":"çevresi bulut parçalarıyla sarılı","usage_role":"contextual"}],"definition":"Bir başın, yerin ya da göksel görünümün çevresini kuşak gibi saran veya kenarlarını belirginleştiren nesne ve oluşumdur. Süslü baş kuşağı, belirli bir gök konumu, çevreleyen bulut ve çiçek ya da küçük bulutlarla çevrilmiş görünüm bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin çevresini kuşak gibi sarma veya kenarını çevreleyerek belirginleştirme çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Süslü baş kuşağı veya taç ile belirli bir gök konumu, yalın adın özel karşılıklarıdır."},{"facet_id":"F003","role":"extension","statement":"Bir yeri dolaşan bulut ya da başka bir örtümsü bulut görünümü çevreleme çekirdeğinin göğe uzanmasıdır."},{"facet_id":"F004","role":"associated_use","statement":"Çiçeklerle çevrili çayır ve çevresinde küçük bulut parçaları bulunan bulut, belirli niteleme kalıplarıdır."}],"identity_rationale":"Kaynak sözü, bir şeyin başı veya çevresi boyunca kuşatıcı biçimde yer alan nesne ve görünümleri ortaklaştırır. Baş çevresindeki süslü kuşak, gök konumu, çevreleyen bulut ve kenarı çiçek ya da küçük bulutlarla sarılı yer bu çekirdeğin destekli uzantılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"taç veya süslü baş kuşağı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Ay'ın konaklarından biri, Akrep takımyıldızının başı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir yerin çevresini dolaşan örtümsü bulut"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çiçeklerle çevrili çayır"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"çevresi küçük bulut parçalarıyla sarılı bulut"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"başına taç takmak"}],"lexicalization_note":"Yalın adın çevreleyen nesne anlamları korunur; çiçekle veya bulut parçalarıyla çevrilme yalnız verilen niteleme kalıplarına bağlanır.","neighbor_coverage_note":"Bütün çevreleme adayları gözden geçirildi; halka biçimli nesne ile çevresini alma eylemi en yararlı iki karşılaştırmadır, diğerleri yalnız aynı uzamsal alanda kalan özel nesnelerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal çevreleme biçimini belirli taç ve gök görünümlerinde adlaştırır; komşu dal ise boyun çevresindeki ve başka nesnelerdeki halkayı daha genel ele alır.","focus_only":"Süslü baş kuşağı, belirli gök konumu ve bulut çevrelenmesi gibi özel adlandırmaları kapsar.","gloss":"çevreleyen halka","neighbor_only":"Boyun halkası, değirmen parçası ve çeşitli dairesel nesneler gibi daha geniş halka kullanımları vardır.","neighbor_ref":"root_000958/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin çevresine dolanan halka veya kuşak biçimini anlatır."},{"boundary_match":"partial","distinction":"Bu dal çoğunlukla çevreleyen kuşağın veya göksel görünümün adıdır; komşu dal çevresini alma ve kuşatma eylemini öne çıkarır.","focus_only":"Çevreleyen nesne veya görünümün kendisini ve ondan türeyen özel adları belirtir.","gloss":"çevresini kuşatmak","neighbor_only":"Bir topluluğun bir kişi ya da nesnenin çevresini alması eylemini de anlatır.","neighbor_ref":"root_000300/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir merkezin çevresinde halka oluşturma düşüncesini paylaşır."}],"source_phrase_ar":"إطافة شيء بشيء والإكليل منزل من منازل القمر والسحاب يدور بالمكان (maqayis)؛ الإكليل شبه عصابة مزينة بالجواهر والإكليل من منازل القمر وروضة مكللة حفت بالنور (ayn)؛ الإكليل شبه عصابة ويسمى التاج إكليلا والإكليل منزل والسحاب كأن غشاء ألبسه وروضة مكللة وسحاب مكلل (sihah)؛ الغمام المكلل السحابة تكون حولها قطع والإكليل شبه عصابة والإكليل منزل (tahdhib)؛ الإكليل سمي بذلك لإطافته بالرأس (mufradat)","source_summary":"Kaynaklar başı saran süslü kuşağı, belirli gök konumunu ve çevreleme biçimi gösteren bulut ile çayır tasvirlerini aynı çevresini sarma düşüncesinde toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإكليل، وإطافة الشيء بالرأس أو بالمكان، ومنزل القمر، والسحاب المحيط، والروضة المحفوفة بالنور، والسحاب المكلل بالقطع","what_is_not_ar":"لا يدخل فيه الكَلالة في أحكام الميراث إلا من جهة أصل الإحاطة، ولا يدخل فيه الكِلّة السترية بوصفها بيتا مخيطا"},"support_links":[]},{"boundary":"Çekirdek dikilmiş koruyucu örtüdür; mezar yapısı, yalnız ona benzeyen yükseltilmiş yapı kalıbındaki uzantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"ev biçimli ince koruyucu örtü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnce kumaştan dikilen ve küçük bir ev gibi kurulabilen koruyucu örtü temel nesnedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Örtünün sivrisinek ve tahtakurusu gibi böceklere karşı korunma amacı vardır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mezarın üzerine küçük kule veya kubbe benzeri yapı yükseltmek, biçim benzerliğine dayalı söz öbeği uzantısıdır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnce kumaştan dikilen ve böceklerden korunmak için kurulan temel nesneye uygundur.","boundary_detail":"Çekirdek dikilmiş koruyucu örtüdür; mezar yapısı, yalnız ona benzeyen yükseltilmiş yapı kalıbındaki uzantıdır.","branch_image_ar":"الكِلّة سترا وبيتا","concept_gloss":"ev biçimli ince koruyucu örtü","contextual_glosses":[{"applicability":"Uyuyan kişiyi sivrisinek ve benzeri böceklerden koruyan kumaş örtü bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Böceklerden koruyan yatak çevresi örtüsünü doğal Türkçe adıyla korur."},"facet_ids":["F001","F002"],"text":"cibinlik","usage_role":"contextual"},{"applicability":"Mezar üzerinde küçük kule veya kubbe benzeri yapı yükseltme söz öbeği için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapının mezar üzerinde yükseltilmesini ve kubbemsi biçimini korur."},"facet_ids":["F003"],"text":"mezar üzerine kubbeli yapı kurmak","usage_role":"contextual"}],"definition":"Sivrisinek veya tahtakurusu gibi böceklerden korunmak için ince kumaştan dikilip küçük bir ev gibi kurulan örtüdür. Mezar üzerine buna benzeyen küçük kule veya kubbe biçimli yapı yükseltmek, söz öbeğine bağlı bir uzantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnce kumaştan dikilen ve küçük bir ev gibi kurulabilen koruyucu örtü temel nesnedir."},{"facet_id":"F002","role":"specialization","statement":"Örtünün sivrisinek ve tahtakurusu gibi böceklere karşı korunma amacı vardır."},{"facet_id":"F003","role":"extension","statement":"Mezarın üzerine küçük kule veya kubbe benzeri yapı yükseltmek, biçim benzerliğine dayalı söz öbeği uzantısıdır."}],"identity_rationale":"Kaynak sözü, ince kumaştan dikilip küçük bir ev gibi kurulan böcek koruyucu örtüyü açıkça verir; mezarlar üzerine küçük yapı, kubbe veya kule yükseltme kullanımı da aynı biçim benzerliğiyle eklenir. Bu ikinci kullanım temel nesnenin kendisiyle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"böceklerden koruyan ev biçimli ince örtü, cibinlik"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"mezar üzerine küçük kule veya kubbe biçimli yapı yükseltmek"}],"lexicalization_note":"Yalın ad dikilmiş ince örtüyü bildirir; mezar üstüne yapı yükseltme anlamı yalnız belirtilen söz öbeğinde geçerlidir.","neighbor_coverage_note":"Bütün örtü ve yapı adayları incelendi; genel örtme ile çadırın dikilmiş özel parçası sınırı açıklar, diğer adaylar işlev veya yapı bakımından daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal biçimi dikilmiş küçük eve benzeyen ve böceklere karşı kullanılan özel örtüdür; komşu dal örtme ve gizlenmenin genel alanıdır.","focus_only":"İnce kumaştan dikilip ev gibi kurulur ve özellikle böceklere karşı korur.","gloss":"örtü ve gizlenme","neighbor_only":"Her türlü örtme, gizlenme ve örtü nesnesini biçim veya amaç sınırlaması olmadan kapsar.","neighbor_ref":"root_000674/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyi kumaş veya benzeri engelle örterek koruma alanındadır."},{"boundary_match":"partial","distinction":"Bu dal böceklere karşı çevreleyen bağımsız koruyucu örtüdür; komşu dal çadırın belirli bir bölümünü kapatan yapı parçasıdır.","focus_only":"Kişinin çevresine kurulan bütün bir koruyucu örtü düzenini belirtir.","gloss":"çadırın arka örtüsü","neighbor_only":"Çadırın yalnız arka bölümünü oluşturan dikilmiş bir veya iki kumaş parçasıdır.","neighbor_ref":"root_001305/B004","relation_type":"near_neighbor","shared_zone":"İki dal dikilmiş kumaş parçalarının küçük ev veya çadır düzeninde kullanılmasını paylaşır."}],"source_phrase_ar":"الكلة غشاء من ثوب يتوقى به من البعوض (ayn)؛ الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق (sihah)؛ الكلة من الستور ما خيط فصار كالبيت والتكليل رفعها ببناء مثل الكلل وهي الصوامع والقباب (tahdhib)","source_summary":"Kaynakların ortak nesnesi, böceklerden korunmak için ince kumaştan dikilen ev biçimli örtüdür. Mezar üzerinde küçük yapı veya kubbe yükseltme, bu biçimden hareket eden özel bir yapı kullanımını oluşturur.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الكِلّة غشاء أو ستر رقيق يخاط كالبيت للوقاية من البعوض والبق، وما يشبه الصوامع والقباب في تكليل القبور","what_is_not_ar":"لا يدخل فيه الإكليل الذي يحيط بالرأس، ولا الكُلّ بمعنى الجميع"},"support_links":[]},{"boundary":"Bu dal yalnız göğüs bölgesini adlandırır; kısa ve kalın erkek nitelemesiyle topluluk anlamındaki çoğul biçim ayrı dallardır.","branch_kind":"bare","branch_ref":"root_001315/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"göğüs","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedenin ön üst bölümündeki göğüs bölgesinin adı olması tek ve doğrudan çekirdektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı beden bölgesi iki yakın ses biçimiyle adlandırılır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya hayvan bedeninin boyun altındaki ön üst bölgesini adlandıran bütün kullanımlara uygundur.","boundary_detail":"Bu dal yalnız göğüs bölgesini adlandırır; kısa ve kalın erkek nitelemesiyle topluluk anlamındaki çoğul biçim ayrı dallardır.","branch_image_ar":"الكُلْكُل صدرا","concept_gloss":"göğüs","contextual_glosses":[{"applicability":"Beden bölümünün konumunu açıkça belirtmenin gerektiği açıklayıcı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Anatomik bölgenin göğüs olduğunu açık ve eksiksiz biçimde korur."},"facet_ids":["F001"],"text":"göğüs bölgesi","usage_role":"explanatory"}],"definition":"İnsan veya hayvan bedeninin boyun ile karın arasında kalan ön üst bölümü, yani göğüstür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedenin ön üst bölümündeki göğüs bölgesinin adı olması tek ve doğrudan çekirdektir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı beden bölgesi iki yakın ses biçimiyle adlandırılır."}],"identity_rationale":"Kaynaklar iki ses biçimini de göğüs karşılığı olarak doğrudan ve tutarlı biçimde verir. Dalın beden bölgesi kimliği ek bir işlem, nitelik veya mecaz gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"göğüs"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"göğüs"}],"lexicalization_note":"Tanım yalın beden bölgesi adını verir ve niteleme ya da söz öbeği anlamı eklemez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; genel göğüs dalı ile belirli göğüs kemiği, bütün-parça sınırını en iyi gösterdi, diğer anatomik adaylar daha uzak bölümlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yalnız beden bölgesi adıdır; komşu dal aynı bölgeyi merkez alarak hastalık, örtü, işaret ve niteleme gibi ilişkili kullanımlara da açılır.","focus_only":"Yalnız göğüs bölgesinin yalın adı olarak sınırlandırılmıştır.","gloss":"göğüs ve ona bağlı kullanımlar","neighbor_only":"Göğsün üst çıkıntısı, rahatsızlıkları, örtüleri, işaretleri ve güce dayalı adlandırmaları da kapsar.","neighbor_ref":"root_000849/B001","relation_type":"near_synonym","shared_zone":"İki dal insan veya hayvan bedeninin göğüs bölgesini doğrudan adlandırır."},{"boundary_match":"field_only","distinction":"Bu dal geniş beden bölgesinin adıdır; komşu dal o bölgede yer alan belirli bir kemik yapısını adlandırır.","focus_only":"Göğsün tüm bölgesini genel bir beden bölümü olarak belirtir.","gloss":"göğüsteki çıkıntılı kemik","neighbor_only":"Göğüs ile karın sınırında öne çıkan belirli bir kemiği anlatır.","neighbor_ref":"root_000604/B007","relation_type":"same_field","shared_zone":"Her iki dal göğüs anatomisi alanındadır."}],"source_phrase_ar":"الكلكل الصدر (maqayis)؛ الكلكل الصدر (ayn)؛ الكلكل والكلكال الصدر (sihah)؛ الكلكل فهو الصدر (tahdhib)؛ الكلكل الصدر (mufradat)","source_summary":"Bütün kaynak anlatımları sözcüğü doğrudan göğüs bölgesinin adı olarak verir; bir kaynak yakın sesli ikinci biçimi de aynı anlamla kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكُلْكُل والكُلْكال بمعنى الصدر","what_is_not_ar":"لا يدخل فيه الرجل الكُلْكُل القصير الغليظ ولا الكلاكل الجماعات"},"support_links":[]},{"boundary":"Bu anlam yalnız erkek niteleyen söz öbeğinde geçerlidir; göğüs adı veya topluluk adı olarak genelleştirilemez.","branch_kind":"collocation","branch_ref":"root_001315/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"kısa, kalın ve güçlü yapılı erkek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkeğin kısa veya çok uzun olmayan boyu ile kalın ve güçlü beden yapısı birlikte belirtilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedenin dağınık değil toplu, sıkı ve derli toplu görünmesi nitelemenin tamamlayıcı yönüdür."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız erkeğin boyunu ve toplu güçlü beden yapısını birlikte niteleyen söz öbeğine uygundur.","boundary_detail":"Bu anlam yalnız erkek niteleyen söz öbeğinde geçerlidir; göğüs adı veya topluluk adı olarak genelleştirilemez.","branch_image_ar":"الكُلْكُل قصر وغلظ","concept_gloss":"kısa, kalın ve güçlü yapılı erkek","contextual_glosses":[{"applicability":"Kısa veya orta boylu, kalın ve toplu yapılı bir erkeği doğal metinde nitelemek için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplu beden yapısını, görece kısa boyu ve gücü birlikte korur."},"facet_ids":["F001","F002"],"text":"tıknaz ve güçlü adam","usage_role":"contextual"}],"definition":"Bir erkeği çok uzun olmayan, kısa ya da orta boylu; kalın, güçlü ve bedeni toplu yapılı olarak niteleyen söz öbeğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkeğin kısa veya çok uzun olmayan boyu ile kalın ve güçlü beden yapısı birlikte belirtilir."},{"facet_id":"F002","role":"specialization","statement":"Bedenin dağınık değil toplu, sıkı ve derli toplu görünmesi nitelemenin tamamlayıcı yönüdür."}],"identity_rationale":"Kaynak sözü, erkek için kısa boy, kalınlık, güç ve toplu beden yapısını birlikte verir. Dal bu nitelikleri tek bir yapı betimlemesi olarak doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kısa, kalın, güçlü ve toplu yapılı erkek"}],"lexicalization_note":"Tanım açıkça erkek niteleyen söz öbeğine bağlıdır ve sözcüğe bağımsız bir temel anlam yüklemez.","neighbor_coverage_note":"Bütün yapı nitelemeleri değerlendirildi; kısa ve toplu beden ile geniş taşıyıcılı kalınlık dalları gerçek sınırları gösterdi, yalnız iri veya ağır olmayı anlatanlar daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kısa boyu kalınlık ve güçle birlikte verir; komşu dal kısalığı ve toplu yapıyı öne çıkarır, güç ile kalınlığı zorunlu kılmaz.","focus_only":"Kalınlık ve güç, kısa veya orta boyla birlikte kurucu niteliklerdir.","gloss":"kısa ve toplu yapılı","neighbor_only":"Kısalık, boyun kesilmiş gibi eksik kalması düşüncesiyle açıklanır.","neighbor_ref":"root_000080/B006","relation_type":"near_synonym","shared_zone":"İki dal kısa boylu ve bedeni toplu bir kişiyi betimler."},{"boundary_match":"partial","distinction":"Bu dal insan bedenine ve toplu yapıya sıkıca bağlıdır; komşu dal kalınlık ile sıkılığı hayvan, yer ve bitkiye kadar genişletir.","focus_only":"Yalnız erkek bedeninin kısa, kalın ve toplu yapısını niteleyen kalıptır.","gloss":"kalın, güçlü ve sıkı","neighbor_only":"Kalın boyun, aslan, tepe, bahçe ve sıklaşıp dolanan ot gibi çok farklı taşıyıcılara uzanır.","neighbor_ref":"root_001098/B002","relation_type":"near_synonym","shared_zone":"İki dal insan için kalınlık, güç ve görece kısa yapıda örtüşür."}],"source_phrase_ar":"الكلكل القصير (maqayis)؛ الكلكل الرجل الضرب ليس بجد طويل والمربوع المجتمع الخلق (ayn)؛ رجل كلكل قصير غليظ مع شدة (sihah)؛ رجل كلكل وكلاكل وكوألل قصر وغلظ مع شدة (tahdhib)","source_summary":"Kaynaklar erkek nitelemesinde kısa ya da çok uzun olmayan boyu, kalınlığı, gücü ve toplu beden yapısını bir arada verir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه وصف الرجل بالقصَر والغلظ والشدة واجتماع الخلق","what_is_not_ar":"لا يدخل فيه الكُلْكُل بمعنى الصدر ولا الكلاكل الجماعات"},"support_links":[]},{"boundary":"Bu dal birden çok topluluğu adlandırır; göğüs anlamı ve insanın kısa kalın yapısı bu çoğul biçime dahil değildir.","branch_kind":"bare","branch_ref":"root_001315/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"topluluklar, kümeler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir arada bulunan birden çok topluluğu veya kümeyi adlandırmak çekirdektir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atların bir arada duran kümeleri, topluluk anlamını açıklayan benzetme örneğidir."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir arada bulunan insan veya başka varlık topluluklarını çoğul olarak adlandıran çekirdeğe uygundur.","boundary_detail":"Bu dal birden çok topluluğu adlandırır; göğüs anlamı ve insanın kısa kalın yapısı bu çoğul biçime dahil değildir.","branch_image_ar":"الكلاكل جماعات","concept_gloss":"topluluklar, kümeler","contextual_glosses":[{"applicability":"Birden fazla insan veya hayvan kümesinin birlikte bulunduğu bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir araya gelme niteliğini ve grup çoğulluğunu açıkça korur."},"facet_ids":["F001","F002"],"text":"bir araya gelmiş gruplar","usage_role":"contextual"}],"definition":"İnsanların veya bağlamca başka varlıkların oluşturduğu topluluklar, özellikle bir arada duran kümelerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir arada bulunan birden çok topluluğu veya kümeyi adlandırmak çekirdektir."},{"facet_id":"F002","role":"example","statement":"Atların bir arada duran kümeleri, topluluk anlamını açıklayan benzetme örneğidir."}],"identity_rationale":"Kaynak sözü çoğul biçimi doğrudan topluluklar olarak açıklar ve at topluluklarını benzetme örneği olarak verir. Dalın kimliği kısa ama yeterince belirgindir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"topluluklar, kümeler"}],"lexicalization_note":"Tanım yalın çoğul topluluk adını verir ve komşu insan ya da hayvan topluluğu türlerini ona eklemez.","neighbor_coverage_note":"Topluluk adaylarının hepsi karşılaştırıldı; yalın topluluk dalı eşdeğer, insan grubu dalı ise kapsamca daha özeldir, parça ve belirli hayvan sürüsü anlamları çekirdeğe eklenmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda iki dalın çekirdek sınırları aynıdır; biçimlerin tekil veya çoğul gerçekleşmesi kavramsal eşdeğerliği bozmaz.","focus_only":null,"gloss":"topluluk","neighbor_only":null,"neighbor_ref":"root_000897/B008","relation_type":"synonym","shared_zone":"İki dal da ek bir katılımcı veya oluşma koşulu getirmeden bir araya gelmiş topluluğu adlandırır."},{"boundary_match":"partial","distinction":"Bu dal genel bir topluluk çoğuludur; komşu dal insan grubuna yönelir ve grupların peş peşe gelişini de anlatabilir.","focus_only":"Topluluk türünü ve art arda geliş biçimini zorunlu olarak belirtmez.","gloss":"insan grubu, bölük","neighbor_only":"İnsan topluluğunu ve bir grubun ardından başka bir grubun gelmesini açıkça kapsar.","neighbor_ref":"root_001184/B001","relation_type":"near_synonym","shared_zone":"İki dal bir araya gelmiş insan topluluğunu adlandırabilir."}],"source_phrase_ar":"الكلاكل من الجماعات كالكراكر من الخيل (ayn)؛ الكلاكل هي الجماعات كالكراكر (tahdhib)","source_summary":"Kaynaklar çoğul biçimi topluluklar anlamında birleştirir ve atların oluşturduğu kümeleri bu kullanım için açıklayıcı bir benzetme olarak sunar.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الكلاكل بمعنى الجماعات","what_is_not_ar":"لا يدخل فيه الكُلْكُل الصدر ولا الرجل القصير الغليظ"},"support_links":[]},{"boundary":"İlerleme ve korkakça geri durma aynı olayın tek sonucu değildir; bağlam hangi karşıt okumanın amaçlandığını belirler.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"saldırıda ilerleme veya korkup geri durma; itaatsizlik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saldırıda kararlılıkla ileri gidip geri dönmemek savaş bağlamındaki olumlu okumadır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı biçim karşıt okumada korkmak, çekinmek veya saldırıyı sürdürememek anlamına gelebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiye yöneltilen kullanım, onun buyruğuna uymamayı veya ona karşı gelmeyi anlatır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşıt savaş okumaları ile kişi nesnesi alan ayrı itaatsizlik kullanımını birlikte gösteren dal özeti olarak uygundur.","boundary_detail":"İlerleme ve korkakça geri durma aynı olayın tek sonucu değildir; bağlam hangi karşıt okumanın amaçlandığını belirler.","branch_image_ar":"الحمل بين المضي والإحجام","concept_gloss":"saldırıda ilerleme veya korkup geri durma; itaatsizlik","contextual_glosses":[{"applicability":"Savaşçının geri dönmeden rakibine ulaşıncaya kadar saldırıyı sürdürdüğü bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İleri hareketi, kararlılığı ve geri dönmeme koşulunu birlikte korur."},"facet_ids":["F001"],"text":"saldırıda durmadan ilerlemek","usage_role":"contextual"},{"applicability":"Karşıt okumada savaşçının korkaklık gösterip saldırıyı sürdürmediği bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Korkuyu ve ileri hareketin kesilmesini birlikte korur."},"facet_ids":["F002"],"text":"korkup saldırıdan geri durmak","usage_role":"contextual"},{"applicability":"Bir kişinin buyruğuna uymama veya ona karşı gelme anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Buyruğa uymama ve karşı gelme ilişkisini doğrudan korur."},"facet_ids":["F003"],"text":"itaat etmemek","usage_role":"contextual"}],"definition":"Saldırı bağlamında ya ileri atılıp rakibe ulaşıncaya dek geri dönmemeyi ya da karşıt biçimde korkup ilerlememeyi anlatan söz öbeği kullanımıdır. Bir kişiye yöneldiğinde ayrıca ona itaat etmemek anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saldırıda kararlılıkla ileri gidip geri dönmemek savaş bağlamındaki olumlu okumadır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı biçim karşıt okumada korkmak, çekinmek veya saldırıyı sürdürememek anlamına gelebilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişiye yöneltilen kullanım, onun buyruğuna uymamayı veya ona karşı gelmeyi anlatır."}],"identity_rationale":"Kaynak sözü saldırıda ileri atılıp geri dönmemeyi, bunun karşıtı olarak korkup geri durmayı ve bir kişiye itaat etmemeyi aynı biçim çevresinde kaydeder. Dal korunabilir, ancak bunlar tek bir kararsız ara durum değil, bağlama göre ayrılan karşıt savaş okumaları ile ayrı bir itaatsizlik kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"saldırıda durmadan ileri gitmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"savaşta korkup geri durmak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ona itaat etmemek, karşı gelmek"}],"lexicalization_note":"Savaşla ilgili karşıt okumalar kendi söz öbeklerine, itaatsizlik anlamı ise kişi nesnesi alan kullanıma bağlı tutulur.","neighbor_coverage_note":"Bütün savaş ve ilerleme adayları değerlendirildi; saldırının doğruluğu karşıtlığı ile genel cesur ilerleme en keskin sınırları verir, birlik türleri ve gelişigüzel zarar verme farklı çekirdeklere aittir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal savaş karşıtlığına ek olarak kişiye itaatsizliği de kapsar; komşu dal saldırının kararlı biçimde gerçekleştirilip gerçekleştirilmediğini merkez alır.","focus_only":"Kişiye itaat etmeme kullanımı ile saldırının karşıt iki sonucu aynı dalda yer alır.","gloss":"saldırıyı sürdürme veya boşa çıkarma","neighbor_only":"Saldırının doğru ve kararlı yapılması ya da yalancı çıkması karşıtlığına sıkıca bağlıdır.","neighbor_ref":"root_001290/B004","relation_type":"near_synonym","shared_zone":"İki dal saldırıda geri durmama ile korkup saldırıyı sürdürememe karşıtlığını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal belirli saldırı söz öbeğinde geri dönmemeyi ve karşıt korkaklık okumasını taşır; komşu dal cesurca öne çıkmanın genel alanıdır.","focus_only":"İleri atılmanın yanında korkup geri durma ve itaatsizlik okumaları da bulunur.","gloss":"cesaretle öne atılma","neighbor_only":"Savaş dışındaki işlere veya düşmana cesaretle yönelmeyi ve ilerleme buyruğunu da kapsar.","neighbor_ref":"root_001207/B006","relation_type":"near_neighbor","shared_zone":"İki dal tehlikeye rağmen ileri gitme ve düşmana yönelme alanında örtüşür."}],"source_phrase_ar":"كلل حمل ولعله أن يكون من المتضادات (maqayis)؛ المكلل الجاد حمل فكلل مضى قدما وقد يكون كلل بمعنى جبن (sihah)؛ المكلل الذي يحمل فلا يرجع حتى يقع بقرنه وكلل فلان فلانا لم يطعه (tahdhib)","source_summary":"Toplu kaynak anlatımı savaş kullanımında karşıt iki okuma verir: saldırıda durmadan ilerleme ve korkup geri kalma. Kişi nesnesiyle kurulan ayrı kullanım ise buyruğa uymamayı bildirir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه كلل في الحمل بمعنى مضى قدما ولم يرجع، وما يقابله من الجبن أو الكذب أو عدم الطاعة","what_is_not_ar":"لا يدخل فيه كلال الإعياء ولا الكُلّ بمعنى العيال"},"support_links":[]},{"boundary":"Bulut kullanımı genel parıltı değil, koyu bulut içinde diş gibi görünen kısa beyaz şimşek görünümüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_001315/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","surface_ar":"كُلِّ"}],"gloss":"dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gülümseme veya hafif gülme sırasında dişlerin görünmesi temel insan eylemidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koyu bulut içindeki beyaz şimşeğin görünmesi, diş gösteren gülümsemeye benzetilen göksel uzantıdır."}}],"root_ar":"ك ل ل","root_id":"root_001315","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan eylemini ve ona görünüş benzerliğiyle bağlı bulut söz öbeğini birlikte temsil eder.","boundary_detail":"Bulut kullanımı genel parıltı değil, koyu bulut içinde diş gibi görünen kısa beyaz şimşek görünümüdür.","branch_image_ar":"الانكلال تبسما ولمعا","concept_gloss":"dişleri görünerek gülümseme ve bulutun şimşekle gülümser gibi olması","contextual_glosses":[{"applicability":"Kadın veya erkeğin hafifçe gülüp dişlerini gösterdiği insan bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gülümsemeyi ve dişlerin görünmesi koşulunu birlikte korur."},"facet_ids":["F001"],"text":"dişleri görünerek gülümsemek","usage_role":"contextual"},{"applicability":"Koyu bulutun içindeki beyazlığın kısa süre şimşekle göründüğü söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bulutu, şimşeği ve koyu zemin içindeki beyaz görünümü korur."},"facet_ids":["F002"],"text":"bulutun içinden beyaz şimşek çakmak","usage_role":"contextual"}],"definition":"İnsanın gülümseyip dişlerini göstermesidir. Koyu bulutun içindeki beyaz şimşeğin diş görünümü vermesi, bu insan eyleminden kurulmuş söz öbeği uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gülümseme veya hafif gülme sırasında dişlerin görünmesi temel insan eylemidir."},{"facet_id":"F002","role":"extension","statement":"Koyu bulut içindeki beyaz şimşeğin görünmesi, diş gösteren gülümsemeye benzetilen göksel uzantıdır."}],"identity_rationale":"Kaynak sözü, insanın dişleri görünür biçimde gülümsemesi ile karanlık bulut içinden çakan beyaz şimşeği açık bir görünüş benzerliği üzerinden bağlar. Dal bu somut gülümseme çekirdeğini ve buluta aktarılan görüntü uzantısını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"dişleri görünerek gülümsemek"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bulutun içinden beyaz şimşek çakmak"}],"lexicalization_note":"İnsanın gülümsemesi yalın kullanımda kalır; bulutun gülümser gibi şimşek göstermesi yalnız verilen söz öbeğine bağlıdır.","neighbor_coverage_note":"Bütün şimşek ve görünme adayları karşılaştırıldı; belli belirsiz şimşek ile genel parıltı en yararlı iki sınırı verir, bulutun kapanması ve göğün açılması karşıt senaryolardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal şimşeği insanın diş gösteren gülümsemesine benzetir; komşu dal benzetme kurmadan parıltının zayıf ve gizli oluşunu öne çıkarır.","focus_only":"İnsan gülümsemesi çekirdeğini ve bulutun diş gösterir gibi şimşeklenmesini kapsar.","gloss":"buluttan belli belirsiz şimşek","neighbor_only":"Şimşeğin özellikle gizli, zayıf veya belli belirsiz olması koşulunu taşır.","neighbor_ref":"root_000428/B004","relation_type":"near_synonym","shared_zone":"İki dal bulut içinden kısa ve sınırlı bir şimşek görünmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal belirli bulut söz öbeğinde gülümseme benzetmesine dayanır; komşu dal şimşeği ve başka nesnelerdeki parlamayı genel olarak anlatır.","focus_only":"Bulut içindeki beyaz şimşek, gülümsemede görünen dişlere benzetilir.","gloss":"şimşek ve genel parıltı","neighbor_only":"Gökyüzü dışında kılıç, yüz, deri ve yağlı yiyecek gibi çok farklı parlak nesneleri kapsar.","neighbor_ref":"root_000108/B001","relation_type":"near_neighbor","shared_zone":"İki dal bulutta şimşeğin çakması ve ışığın kısa süre görünmesi alanında buluşur."}],"source_phrase_ar":"انكلت المرأة إذا ضحكت (maqayis)؛ انكل الرجل انكلالا تبسم وتنكل عن غر عذاب وانكلال الغيم بالبرق (sihah)؛ انكلت المرأة إذا تبسمت وانكل السحاب بالبرق إذا تبسم بالبرق (tahdhib)","source_summary":"Kaynak anlatımı insanın gülümseyip dişlerini göstermesinde birleşir ve bulut içindeki beyaz şimşeği bu görünümün benzetmeli uzantısı olarak verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه انكلال المرأة أو الرجل تبسما مع ظهور الأسنان، وانكلال الغيم أو السحاب بالبرق","what_is_not_ar":"لا يدخل فيه تأكل السيف أو البرق إذا نص المصدر أنه ليس من هذا الباب"},"support_links":[]},{"boundary":"Bu dal, fiziksel vurma ya da itme anlamını kapsamaz; yüzüne karşı ince biçimde yerme ile arkasından kusur araştırıp çekiştirme aynı ayıplama çekirdeğine bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001376/B001","candidate_links":[{"candidate_id":"cand_5ce8d59c5bd5accadb08","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لُّمَزَة","morph_features":"STEM|POS:N|LEM:l~umazap|ROOT:lmz|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:4:1","qac_word_ref":"104:1:4","surface_ar":"لُّمَزَةٍ"}],"gloss":"kusur arayıp sözle veya işaretle ayıplama ve çekiştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişide kusur bulma, bu kusur üzerinden onu ayıplama ve yerme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayıplama, kişinin yüzüne karşı göz veya ağız işaretiyle ya da alçak sesli, üstü kapalı bir sözle yapılabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem, kişinin arkasından onu çekiştirmeyi ve kusurlarını araştırıp ortaya dökmeyi de kapsayabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bu davranışı sık sık yapan kişi, sürekli kusur bulan ve başkalarını ayıplayan biri olarak nitelenir."}}],"root_ar":"ل م ز","root_id":"root_001376","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kusur bulma, ayıplama, ince söz veya işaretle yerme ve arkasından çekiştirme yönlerini birlikte anlatan genel karşılıktır.","boundary_detail":"Bu dal, fiziksel vurma ya da itme anlamını kapsamaz; yüzüne karşı ince biçimde yerme ile arkasından kusur araştırıp çekiştirme aynı ayıplama çekirdeğine bağlıdır.","branch_image_ar":"العيب باللمز","concept_gloss":"kusur arayıp sözle veya işaretle ayıplama ve çekiştirme","contextual_glosses":[{"applicability":"Birinin kusurunu öne çıkararak onu kötüleme eyleminin genel ve akıcı anlatımıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnce işaret veya alçak sesli sözle gerçekleştirme ile arkasından kusur araştırıp çekiştirme yönlerini açıkça söylemez.","preserves":"Bir kişide kusur bulup onu değersizleştirme ve kötüleme çekirdeğini korur."},"facet_ids":["F001"],"text":"ayıplamak ve yermek","usage_role":"general"},{"applicability":"Göz veya ağız işaretiyle ya da alçak sesli sözle kişinin yüzüne karşı yapılan ince yerme için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüzüne karşı yapılma koşulunu, ince anlatımı ve söz veya işaret yoluyla yermeyi korur."},"facet_ids":["F002"],"text":"yüzüne karşı üstü kapalı biçimde yermek","usage_role":"contextual"},{"applicability":"Kişinin bulunmadığı yerde onu kötüleme ve kusurlarını izleyip ortaya çıkarma uzantısı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arkasından çekiştirme ile kusurları araştırıp ortaya çıkarma yönlerini birlikte korur."},"facet_ids":["F003"],"text":"arkasından çekiştirip kusurlarını araştırmak","usage_role":"contextual"}],"definition":"Birinin kusurlarını bulup onu sözle ya da işaretle ayıplamak, yermek ve küçük düşürmektir. Bu davranış yüzüne karşı ince bir işaret veya alçak sesli sözle yapılabildiği gibi, arkasından çekiştirme ve kusurlarını araştırma biçimini de alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişide kusur bulma, bu kusur üzerinden onu ayıplama ve yerme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Ayıplama, kişinin yüzüne karşı göz veya ağız işaretiyle ya da alçak sesli, üstü kapalı bir sözle yapılabilir."},{"facet_id":"F003","role":"extension","statement":"Eylem, kişinin arkasından onu çekiştirmeyi ve kusurlarını araştırıp ortaya dökmeyi de kapsayabilir."},{"facet_id":"F004","role":"associated_use","statement":"Bu davranışı sık sık yapan kişi, sürekli kusur bulan ve başkalarını ayıplayan biri olarak nitelenir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Söz veya işaret yerine bedensel güç ve fiziksel temas anlamı ekler.","collision":"Aynı kökün fiziksel vurma ve itme dalıyla karışır.","fit":"displacement","loses":"Kusur bulma, ayıplama, yerme ve arkasından çekiştirme çekirdeğinin tamamını yitirir.","preserves":"Eylemin başka bir kişiye yönelmiş olmasını korur."},"text":"itmek veya vurmak"},{"category":"alternative","error_profile":{"adds":"Açık ve kaba sözlü saldırı anlamını zorunluymuş gibi ekler.","collision":"Ayıplamanın ince ve dolaylı biçimlerini açık sövgüyle karıştırır.","fit":"displacement","loses":"Kusur araştırma, ince işaret, alçak sesli söz ve arkasından çekiştirme kapsamını yitirir.","preserves":"Birini sözle kötüleme ve değersizleştirme yönünü kısmen korur."},"text":"sövüp saymak"}],"identity_rationale":"Kaynak ifadesi, birinin kusurunu bulup onu ayıplama ve yerme çekirdeğini açıkça destekler. Yüzüne karşı göz ya da ağız işaretiyle veya alçak sesli sözle yapılan yerme ile arkasından çekiştirme ve kusur araştırma, bu çekirdeğin desteklenen gerçekleşme biçimleri ve kapsam uzantılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ayıplama, yerme, kusur arayıp çekiştirme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"onu ayıpladı ve yerdi; kimi zaman bir işaretle veya alçak sesli sözle"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"onu yüzüne karşı ağzınla alçak sesle ayıplarsın"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yardımların dağıtımında isteğini dudaklarını oynatarak belli eder"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanı yüzüne karşı ayıplayan veya sık sık kusur bulan kimse"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çokça ayıplayıp kusur bulan kimse; söz taşıyan kimse için de söylenir"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"insanları arkalarından çekiştirip ayıplayan ve küçük düşüren kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"başkalarını ayıplamayın; yoksa onlar da sizi ayıplar ve böylece kendinizi ayıplamış gibi olursunuz"}],"lexicalization_note":"Dalın çıplak ayıplama ve yerme anlamı ile belirli söz ve kullanım kalıpları birlikte tanıklanmıştır. Tanımdaki çekirdek çıplak kullanıma dayanır; dudak hareketiyle istek belirtme ve karşılıklılık bildiren öğüt gibi okumalar yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Burada fiziksel eş dal ile anlamca en yakın ayıplama, kötü söz ve söz taşıma dalları seçildi; öteki konuşma adayları bu ayrımları yinelediği, öteki fiziksel adaylar ise yalnız uzak alan benzerliği taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dal toplumsal ve değerlendirici bir kötüleme eylemidir; komşu dal ise doğrudan bedensel temas ve güç uygulamasıdır. Biri ötekinin bağlama göre değişen karşılığı sayılamaz.","focus_only":"Birinin kusurunu bulup onu sözle veya işaretle ayıplama ve çekiştirme vardır.","gloss":"ayıplama ile vurup itme","neighbor_only":"Birine fiziksel güç uygulayarak onu vurma veya itme vardır.","neighbor_ref":"root_001376/B002","relation_type":"other","shared_zone":"Aynı söz biçiminin farklı anlam dallarında kullanılması dışında ortak anlam çekirdeği yoktur."},{"boundary_match":"partial","distinction":"Odak dal, ince yüz işareti ve alçak söz gibi gerçekleştirme yollarını ayrıca belirginleştirir. Komşu dal genel kötü söz ve sözlü saldırı alanına daha rahat uzandığı için sınırlar yalnız kısmen çakışır.","focus_only":"Yüzüne karşı göz veya ağız işaretiyle ya da alçak sesli sözle yerme ve kusur izleme açıkça kapsanır.","gloss":"ayıplama ve çekiştirme","neighbor_only":"Kötü sözle saldırma ve genel olarak insanların ardından konuşma yönü daha geniş bir çerçevede sunulur.","neighbor_ref":"root_001600/B004","relation_type":"near_synonym","shared_zone":"İki dal da insanların kusurlarını öne çıkararak onları ayıplama ve arkalarından kötü konuşma alanında örtüşür."},{"boundary_match":"partial","distinction":"Eylemin ayıplama ve çekiştirme bölümü güçlü biçimde örtüşür. Odak dalın ince işaret ve gizli söz yolları ile komşu dalın etkili çarpma imgesi aynı sınırın bütünü değildir.","focus_only":"İnce göz veya ağız işareti, alçak sesli söz ve kusurları izleme yolları açıkça belirtilir.","gloss":"kusur bulup arkasından çekiştirme","neighbor_only":"Ayıplama, etkili bir vurma veya çarpma izlenimi veren ayrı bir anlatım imgesiyle sunulur.","neighbor_ref":"root_001541/B007","relation_type":"near_synonym","shared_zone":"İki dal da birini ayıplama, hakkında kötü konuşma ve kusurlarını öne çıkarma çekirdeğini paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal kötü sözle kusur yükleme ve sözlü saldırı üzerinde durur. Odak dal ise sözün yanında ince işareti, çekiştirmeyi ve kusur araştırmayı da içerdiğinden tam yerine geçme yoktur.","focus_only":"Sözsüz işaretle ayıplama ve arkasından kusur araştırma, odak dalda bağımsız olarak kapsanır.","gloss":"kusur yükleyerek kötüleme","neighbor_only":"Kişinin onuru, inancı veya sözü gibi alanlara kötü söz yöneltme kapsamı açıkça öne çıkar.","neighbor_ref":"root_000935/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiye kusur yükleyip onu sözle kötüleme ve değersizleştirme alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği kusur bulup ayıplamaktır; bir sözü üçüncü kişiye aktarmak gerekmez. Komşu dalın çekirdeği ise sözü insanlar arasında taşımaktır ve kusur bulma zorunlu değildir.","focus_only":"Birinin kusurunu bulup onu doğrudan veya arkasından ayıplama eylemi vardır.","gloss":"ayıplama ile söz taşıma","neighbor_only":"İnsanlar arasında başkalarına ilişkin kötü söz ve haber taşıma eylemi vardır.","neighbor_ref":"root_000457/B004","relation_type":"same_field","shared_zone":"Her iki dal da konuşma yoluyla insanlar arasındaki ilişkileri zedeleyebilen davranışları anlatır."}],"source_phrase_ar":"اللَّمْز وهو العيب (maqayis)؛ اللمز كالغمز في الوجه تلمزه بفيك بكلام خفي (ayn;tahdhib)؛ أصله الإشارة بالعين ونحوها (sihah)؛ اللمز الاغتياب وتتبع المعاب (mufradat)؛ رجل لماز ولمزة أي عياب (maqayis;sihah;mufradat)","source_summary":"Ortak tanıklık, anlamı kusur bulma ve ayıplama çevresinde birleştirir. Yerme yüzüne karşı ince bir işaret veya alçak sesli sözle gerçekleşebilir; kapsam ayrıca arkasından çekiştirmeye, kusur araştırmaya ve bu işi alışkanlık hâline getiren kişiyi nitelemeye uzanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"العيب والطعن وتتبع المعاب والاغتياب والإشارة بالعين أو الفم والكلام الخفي، ويشمل اللماز واللمزة","what_is_not_ar":"الدفع والضرب؛ الهمز من خلف إذا فرق المصدر بينهما"},"support_links":["sup_06fe90d5be6dce824180"]},{"boundary":"Dal yalnız fiziksel vurma ve itmeyi kapsar; sözle ya da işaretle ayıplama, kusur araştırma ve arkasından çekiştirme bu anlamın dışında kalır.","branch_kind":"bare","branch_ref":"root_001376/B002","candidate_links":[{"candidate_id":"cand_11790f2358e1d516f0ba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"لُّمَزَة","morph_features":"STEM|POS:N|LEM:l~umazap|ROOT:lmz|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:4:1","qac_word_ref":"104:1:4","surface_ar":"لُّمَزَةٍ"}],"gloss":"vurmak veya itmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, bir kişiye doğrudan bedensel güç uygulamayı gerektirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedensel güç uygulama, vurma veya itme biçiminde gerçekleşebilir."}}],"root_ar":"ل م ز","root_id":"root_001376","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Herhangi bir özel araç, hedef bölge veya şiddet derecesi gerektirmeden fiziksel eylemin iki tanıklanan biçimini birlikte karşılar.","boundary_detail":"Dal yalnız fiziksel vurma ve itmeyi kapsar; sözle ya da işaretle ayıplama, kusur araştırma ve arkasından çekiştirme bu anlamın dışında kalır.","branch_image_ar":"الدفع باللمز","concept_gloss":"vurmak veya itmek","contextual_glosses":[{"applicability":"Bedensel güç uygulamanın darbe indirme biçiminde gerçekleştiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin darbe indirmeden yalnızca itme biçiminde gerçekleşebilmesini dışarıda bırakır.","preserves":"Doğrudan fiziksel güç uygulama ve darbe indirme yönünü korur."},"facet_ids":["F001","F002"],"text":"vurmak","usage_role":"contextual"},{"applicability":"Bedensel gücün kişiyi bulunduğu yerden uzaklaştırmaya yöneldiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eylemin itmeden, doğrudan darbe indirme biçiminde gerçekleşebilmesini dışarıda bırakır.","preserves":"Bir kişiye doğrudan fiziksel güç uygulayıp onu itme yönünü korur."},"facet_ids":["F001","F002"],"text":"itmek","usage_role":"contextual"}],"definition":"Bir kişiye doğrudan bedensel güç uygulayarak onu vurmak veya itmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, bir kişiye doğrudan bedensel güç uygulamayı gerektirir."},{"facet_id":"F002","role":"source_variant","statement":"Bedensel güç uygulama, vurma veya itme biçiminde gerçekleşebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kusur bulma ve kişiyi sözle ya da işaretle kötüleme anlamı ekler.","collision":"Aynı kökün ayıplama ve kusur araştırma dalıyla karışır.","fit":"displacement","loses":"Bedensel güç, fiziksel temas, vurma ve itme çekirdeğinin tamamını yitirir.","preserves":"Eylemin başka bir kişiye yönelmiş olmasını korur."},"text":"ayıplamak veya çekiştirmek"}],"identity_rationale":"Kaynak ifadesi, eylemi birine bedensel güç uygulayarak onu vurma veya itme olarak açıkça tanımlar. Bu fiziksel anlam, kusur bulma ve ayıplama dalından ayrı tutulduğunda verilen dal çerçevesi kaynakla tam uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onu vurdu veya itti"}],"lexicalization_note":"Tanıklık çıplak eylem anlamını doğrudan vurma veya itme olarak verir. Belirli bir araç, beden bölgesi, şiddet derecesi ya da sonuç tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Burada ayıplama eş dalı, genel itme ve vurma komşuları ile yere serme sonucu taşıyan en yararlı karşıtlıklar seçildi; beden bölgesi, araç veya zeminle sınırlı öteki adaylar bu sınırları tekrarladığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dal doğrudan fiziksel temas ve güç uygulamasıdır; komşu dal ise toplumsal ve değerlendirici bir kötüleme eylemidir. Biri ötekinin bağlama göre değişen karşılığı sayılamaz.","focus_only":"Birine doğrudan bedensel güç uygulayarak onu vurma veya itme vardır.","gloss":"vurup itme ile ayıplama","neighbor_only":"Birinin kusurunu bulup onu sözle veya işaretle ayıplama ve çekiştirme vardır.","neighbor_ref":"root_001376/B001","relation_type":"other","shared_zone":"Aynı söz biçiminin farklı anlam dallarında kullanılması dışında ortak anlam çekirdeği yoktur."},{"boundary_match":"partial","distinction":"Odak dal sıradan vurma veya itmeyi kapsar ve şiddet şartı koymaz. Komşu dal itmenin şiddetli ve kaba biçimini öne çıkarır, ayrıca azarlama ve yöneltme kapsamına uzanır.","focus_only":"Vurma seçeneği vardır ve itmenin şiddetli ya da kaba olması gerekmez.","gloss":"itmek ve sertçe kakmak","neighbor_only":"Şiddetli itme, kaba davranma, azarlama ve birini belirli bir yöne sürme kapsamı bulunur.","neighbor_ref":"root_000477/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye bedensel güç uygulayıp onu itme eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Vurma bağlamında karşılıklar birbirine yaklaşır; ancak odak dal itmeyi de içerir. Komşu dal ise farklı araçlarla doğrudan darbe indirme alanını daha geniş örnekler.","focus_only":"Darbe indirmeden yalnız itme biçiminde güç uygulama da kapsanır.","gloss":"vurmak","neighbor_only":"El, sopa veya kılıç gibi araçlarla doğrudan darbe indirme örnekleri daha geniş biçimde kapsanır.","neighbor_ref":"root_000906/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye doğrudan fiziksel güç uygulayıp ona darbe indirme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın vurma yönü komşuyla örtüşür, fakat şiddet veya çarpışma şartı taşımaz ve itmeyi de kapsar. Komşu dal kuvvetli çarpışma ve tokat gibi daha özel biçimleri gerektirir.","focus_only":"Sıradan itme veya şiddet derecesi belirtilmeyen vurma eylemi kapsanır.","gloss":"şiddetle çarpıp vurmak","neighbor_only":"İki şeyin kuvvetle çarpışması, şiddetli darbe ve yüze tokat atma kapsamı açıkça bulunur.","neighbor_ref":"root_000874/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da doğrudan fiziksel temasla bir kişiye darbe uygulama alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalda düşme ya da yere çarpma sonucu gerekli değildir. Komşu dal ise kuvvet uygulamasını kişiyi yere serme veya yere atma sonucuyla sınırlar.","focus_only":"Birini düşürmeden yalnızca vurmak veya itmek yeterlidir.","gloss":"vurup itme ile yere serme","neighbor_only":"Kişiyi yere sermek, kaldırıp atmak veya yere çarpmak gibi belirli bir sonuç ve hareket dizisi vardır.","neighbor_ref":"root_000249/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye bedensel güç uygulama ve onun konumunu etkileyebilme alanında buluşur."}],"source_phrase_ar":"لمزه إذا ضربه ودفعه (sihah)؛ الأصل في الهمز واللمز الدفع؛ همزته ولمزته ولهزته إذا دفعته (tahdhib)","source_summary":"Ortak tanıklık, bu dalı bir kişiye doğrudan bedensel güç uygulama olarak verir ve eylemin vurma ya da itme biçiminde gerçekleşebildiğini belirtir.","sources":["SI","TA"],"what_is_ar":"الدفع والضرب ونحوهما في قول لمزه أو همزته أو لهزته","what_is_not_ar":"العيب والاغتياب وتتبع المعاب والكلام الخفي"},"support_links":["sup_03e6984b5b8ec06cede8"]},{"boundary":"Bu dal somut sıkma ve ezmeyle sınırlıdır; ses çıkarma, birini kötüleme ve zihinsel etki bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001600/B001","candidate_links":[{"candidate_id":"cand_11790f2358e1d516f0ba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","surface_ar":"هُمَزَةٍ"}],"gloss":"elle bastırıp sıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi elle bastırma, sıkıştırma veya ezme yönünde fiziksel kuvvet uygulama."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nesneyi avuç içinde sıkma ile başı veya cevizi bastırıp ezme, çekirdeğin somut örnekleridir."}}],"root_ar":"ه م ز","root_id":"root_001600","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel bir nesneye elle baskı uygulayıp onu sıkıştırma veya ezme çekirdeğinin tamamı için uygundur.","boundary_detail":"Bu dal somut sıkma ve ezmeyle sınırlıdır; ses çıkarma, birini kötüleme ve zihinsel etki bu sınırın dışındadır.","branch_image_ar":"ضغط الشيء وعصره باليد","concept_gloss":"elle bastırıp sıkma","contextual_glosses":[{"applicability":"Bir nesnenin avuç içine alınıp baskıyla sıkıştırıldığı anlatımlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Baş gibi avuçta tutulmayan nesnelere uygulanan baskı örneklerini dışarıda bırakır.","preserves":"Avuç içinde elle uygulanan sıkıştırıcı baskıyı korur."},"facet_ids":["F001","F002"],"text":"avucunda sıkmak","usage_role":"contextual"},{"applicability":"Uygulanan baskının nesneyi zedelediği veya parçaladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ezilmeyle sonuçlanmayan daha hafif sıkıştırma uygulamalarını dışarıda bırakır.","preserves":"Güçlü fiziksel baskı ve ezme sonucunu korur."},"facet_ids":["F001","F002"],"text":"bastırıp ezmek","usage_role":"contextual"}],"definition":"Bir nesneye, çoğunlukla elle veya avuç içinde, onu sıkıştıracak ya da ezecek biçimde fiziksel baskı uygulamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi elle bastırma, sıkıştırma veya ezme yönünde fiziksel kuvvet uygulama."},{"facet_id":"F002","role":"example","statement":"Nesneyi avuç içinde sıkma ile başı veya cevizi bastırıp ezme, çekirdeğin somut örnekleridir."}],"identity_rationale":"Kaynak ifadesi, bir nesneye özellikle avuç içinde baskı uygulayıp onu sıkma veya ezme çekirdeğini açıkça destekler. Baş ve ceviz örnekleri bu fiziksel işlemin nesneye göre değişen uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi bastırıp sıkma veya ezme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi avucunda bastırıp sıkmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"başı bastırıp ezecek kadar sıkmak"}],"lexicalization_note":"Tanım, genel fiziksel işlemi avuçta nesne sıkma ve başı sıkma gibi belirli kullanımlardan ayırarak birlikte gösterir.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; en yararlı sınırlar, elle yoklama ile itme veya dürtme karşısındaki ayrımlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği sıkıştırma ve ezmedir; komşu dal ise baskının yanında dokunarak yoklama işlevine de uzanır, bu nedenle tam ikame kurulamaz.","focus_only":"Bu dal, nesneyi belirgin biçimde sıkıştıran veya ezen güçlü baskıyı öne çıkarır.","gloss":"elle sıkma ve yoklama","neighbor_only":"Komşu dal, elle yoklama ve bir hayvanı durumunu anlamak için hafifçe elleme kullanımını da kapsar.","neighbor_ref":"root_001106/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da el aracılığıyla nesneye basınç uygulanabilir."},{"boundary_match":"partial","distinction":"Sıkıştırmada kuvvet nesne üzerinde baskı kurar; itme ve dürtmede ise nesnenin yönü veya hareketi değiştirilir.","focus_only":"Bu dalda kuvvet nesneyi iki yönden sıkıştırır veya ezmeye yönelir.","gloss":"sıkıştırma ile itme","neighbor_only":"Komşu dalda kuvvet nesneyi itme, vurma ya da dürtme yoluyla harekete geçirir.","neighbor_ref":"root_001600/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesneye doğrudan fiziksel kuvvet uygulanmasını anlatır."}],"source_phrase_ar":"تدل على ضغط وعصر (maqayis)؛ همزت الشيء في كفي (maqayis;sihah;mufradat)؛ الهمز كالعصر (mufradat)؛ همزت رأسه وهمزت الجوز بكفي (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bir şeyi baskı altına alarak sıkmak veya ezmektir; baş ve ceviz örnekleri yalnız belirli aktarım ayrıntılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عصر الشيء أو الرأس أو الجوز في الكف وما قاربه من ضغط حسي.","what_is_not_ar":"لا يدخل فيه عيب الناس ولا وسوسة الشيطان ولا مجرد نطق الهمزة إلا من جهة التشبيه بالضغط."},"support_links":["sup_03e6984b5b8ec06cede8"]},{"boundary":"Dal yalnızca konuşma sesinin baskılı çıkarılışına ilişkindir; genel konuşma, fiziksel sıkma ve itme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001600/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","surface_ar":"هُمَزَةٍ"}],"gloss":"sesi baskılı biçimde çıkarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşma sesini baskılı ve sıkıştırılmış bir söyleyişle belirginleştirme."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin ses üzerinde yapılması kadar, sesin bu etkiyi alıp baskılı biçimde çıkması da anlatılır."}}],"root_ar":"ه م ز","root_id":"root_001600","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Konuşma sesinin sıkıştırılmış gibi belirgin çıkarılması ve bu etkinin ses üzerinde gerçekleşmesi için uygundur.","boundary_detail":"Dal yalnızca konuşma sesinin baskılı çıkarılışına ilişkindir; genel konuşma, fiziksel sıkma ve itme anlamlarını kapsamaz.","branch_image_ar":"ضغط الحرف في الكلام","concept_gloss":"sesi baskılı biçimde çıkarma","contextual_glosses":[{"applicability":"Konuşanın belirli bir sesi baskılı bir söyleyişle çıkardığı cümlelerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşanın sese uyguladığı baskılı ve sıkıştırıcı söyleyiş işlemini korur."},"facet_ids":["F001"],"text":"sesi sıkıştırarak söylemek","usage_role":"contextual"},{"applicability":"Sesin işlemi alan taraf olarak baskılı biçimde çıktığının anlatıldığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin baskı etkisini alarak çıkması yönünü açıkça korur."},"facet_ids":["F002"],"text":"sesin baskılı çıkması","usage_role":"contextual"}],"definition":"Konuşmada bir sesi, sanki üzerine baskı uygulanıyormuş gibi sıkıştırarak belirgin biçimde çıkarmaktır; aynı anlatım sesin bu baskıyı alarak çıkmasını da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşma sesini baskılı ve sıkıştırılmış bir söyleyişle belirginleştirme."},{"facet_id":"F002","role":"extension","statement":"İşlemin ses üzerinde yapılması kadar, sesin bu etkiyi alıp baskılı biçimde çıkması da anlatılır."}],"identity_rationale":"Kaynak ifadesi, konuşmadaki belirli ses çıkarma işlemini harfe baskı uygulama benzetmesiyle açıklar ve işlemin hem uygulanmasını hem de sesin bu etkiyi almasını belirtir. Bu nedenle dal fiziksel baskı değil, baskı imgesiyle açıklanan bir söyleyiş biçimidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"konuşmada sesi baskılı biçimde çıkarma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sesi sıkıştırarak belirgin çıkarmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sesin baskılı ve sıkışmış biçimde çıkması"}],"lexicalization_note":"Tanım, konuşma içindeki belirli kullanımı ve ses üzerinde işlemin yapılmış olmasını ayrı yönler olarak korur; bunu genel bir kök anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; fiziksel baskı dalı ve genel söz söyleme dalı, sesletimin özel sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda baskı, bir konuşma sesinin çıkarılış niteliğidir; komşu dalda ise fiziksel bir nesne üzerinde gerçekleşen somut işlemdir.","focus_only":"Bu dal, konuşma sesinin baskılı biçimde çıkarılmasını anlatır.","gloss":"seste baskı ile fiziksel baskı","neighbor_only":"Komşu dal, elle uygulanan gerçek baskıyla somut bir nesneyi sıkıştırır veya ezer.","neighbor_ref":"root_001600/B001","relation_type":"near_neighbor","shared_zone":"Sesletim, somut sıkıştırma dalındaki baskı imgesiyle açıklanır."},{"boundary_match":"field_only","distinction":"Odak dal belirli bir sesletim biçimini tanımlar; komşu dal ise kelime, cümle ve daha uzun sözlerin söylenmesi gibi genel konuşma eylemidir.","focus_only":"Bu dal, belirli bir sesin baskılı ve sıkıştırılmış biçimde çıkarılışına odaklanır.","gloss":"baskılı sesletim ve söz söyleme","neighbor_only":"Komşu dal, tek bir söyleyiş niteliğiyle sınırlanmadan söz ve konuşmanın dışa vurulmasını kapsar.","neighbor_ref":"root_001272/B001","relation_type":"same_field","shared_zone":"Her iki dal da insan konuşmasının sesli olarak gerçekleştirilmesi alanındadır."}],"source_phrase_ar":"الهمز في الكلام كأنه يضغط الحرف (maqayis)؛ ومنه الهمز في الكلام لأنه يضغط وقد همزت الحرف فانهمز (sihah)؛ ومنه الهمز في الحرف (mufradat)","source_summary":"Kaynaklar, konuşmadaki bu sesletimi bir harfe baskı uygulama imgesiyle açıklar; sesin bu etkiyi alarak çıkması Sihah'a bağlı aktarım yönüdür.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الهمز في الكلام والحرف من حيث تصويره كضغط للحرف.","what_is_not_ar":"لا يدخل فيه ضغط الأجسام بذاته ولا الغيبة والعيب ولا دفع السهم."},"support_links":[]},{"boundary":"Çekirdek hareket ettiren itme, vurma veya dürtmedir; sıkıştırma, konuşma sesi ve insanları kötüleme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001600/B003","candidate_links":[{"candidate_id":"cand_11790f2358e1d516f0ba","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","surface_ar":"هُمَزَةٍ"}],"gloss":"itme, vurma veya dürtme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi itme, vurma veya dürtme yoluyla harekete geçirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yayın oku güçlü biçimde ileri sürmesi, hareket ettirici kuvvetin özel bir uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Binicinin hayvanı dürtüp yürütmek için kullandığı metal araç, dürtme yönünün araçlaşmış biçimidir."}}],"root_ar":"ه م ز","root_id":"root_001600","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesne ya da canlı üzerinde hareket doğuran doğrudan kuvvetin temel eylem türlerini birlikte karşılar.","boundary_detail":"Çekirdek hareket ettiren itme, vurma veya dürtmedir; sıkıştırma, konuşma sesi ve insanları kötüleme bu dala girmez.","branch_image_ar":"دفع ونخس يحرّك الشيء","concept_gloss":"itme, vurma veya dürtme","contextual_glosses":[{"applicability":"Bir yayın oku güçlü kuvvetle ileri gönderme niteliğinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel vurma ve dürtme kullanımları ile hayvanı harekete geçiren araç anlamını dışarıda bırakır.","preserves":"İleri yönlü güçlü itme ve hareket ettirme yönünü korur."},"facet_ids":["F001","F002"],"text":"oku güçlü biçimde ileri sürmek","usage_role":"contextual"},{"applicability":"Bir hayvanın metal bir araçla dürtülüp harekete geçirildiği bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel itme ve vurma ile yayın oku ileri sürmesi kullanımlarını dışarıda bırakır.","preserves":"Dürtme yoluyla hareket ettirme yönünü korur."},"facet_ids":["F001","F003"],"text":"dürterek yürütmek","usage_role":"contextual"}],"definition":"Bir şeyi itmek, vurmak ya da dürterek harekete geçirmektir. Aynı kuvvet imgesi, oku güçlü süren yay ve bir hayvanı dürtüp yürütmeye yarayan metal araç için özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi itme, vurma veya dürtme yoluyla harekete geçirme."},{"facet_id":"F002","role":"specialization","statement":"Yayın oku güçlü biçimde ileri sürmesi, hareket ettirici kuvvetin özel bir uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Binicinin hayvanı dürtüp yürütmek için kullandığı metal araç, dürtme yönünün araçlaşmış biçimidir."}],"identity_rationale":"Kaynak ifadesi itme, vurma ve dürtmeyi aynı hareket ettirici kuvvet alanında toplar; oku güçlü süren yay ile hayvanı dürtmekte kullanılan metal araç da bu çekirdeğin özelleşmiş gerçekleşmeleridir. Dal başlığı bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onu itti veya vurdu"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"oku güçlü biçimde ileri süren yay"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"binicinin hayvanı dürtmek için topuğunda kullandığı metal araç"}],"lexicalization_note":"Tanım, genel itme ve vurma eylemini yay ile hayvanı dürten araç gibi yapıya bağlı özelleşmelerden açıkça ayırır.","neighbor_coverage_note":"Tüm komşular incelendi; sertçe kakma ile değnekle sürme, genel itme ve dürtme çekirdeğine en yakın fakat sınırı farklı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hareket ettirici kuvvetin itme, vurma ve dürtme çeşitlerini kapsar; komşu dal ise özellikle sert ve kaba bir kakmayı öne çıkarır.","focus_only":"Bu dal nötr itmenin yanında vurma, dürtme, yay ve dürtme aracı kullanımlarını da kapsar.","gloss":"itme ve sertçe kakma","neighbor_only":"Komşu dal, sertlik, kabalık ve azarlama çağrışımı taşıyan zorlayıcı itişe uzanır.","neighbor_ref":"root_000477/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyi doğrudan kuvvetle ileri veya yana itme bulunur."},{"boundary_match":"partial","distinction":"Odak dal araçtan bağımsız genel bir kuvvet çekirdeğine sahiptir; komşu dalın ayırt edici sınırı değnekle sürme veya itmedir.","focus_only":"Bu dal genel itme ve vurmayı, güçlü yayı ve metal dürtme aracını da içerir.","gloss":"dürtme ve değnekle sürme","neighbor_only":"Komşu dal hayvanı değnekle sürme ve bir şeyi özellikle değnek kullanarak itme alanına bağlıdır.","neighbor_ref":"root_001493/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir canlıyı dışarıdan kuvvet uygulayarak harekete geçirebilir."}],"source_phrase_ar":"قوس همزي شديدة الدفع للسهم (maqayis)؛ همزه أي دفعه وضربه (sihah)؛ قوس همزى أي شديدة الدفع للسهم والمهمز والمهماز حديدة في مؤخر خف الرائض (sihah)؛ همزته ولمزته ولهزته ونهزته إذا دفعته (tahdhib)؛ كل شيء دفعته فقد همزته (tahdhib)؛ من النخس والغمز (tahdhib)","source_summary":"Kanıt bütünü itme, vurma ve dürtmeyi hareket ettirici kuvvet çekirdeğinde birleştirir; güçlü yay belirli kaynaklarda, metal dürtme aracı Sihah'ta, Tahdhib'in genel itme açıklaması da ayrı aktarım ayrıntısı olarak durur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الدفع والضرب والنخس، وما وصف به القوس الشديدة الدفع للسهم والمهماز الذي يحث الدابة.","what_is_not_ar":"لا يدخل فيه العيب والغيبة ولا نطق الحرف، وإن اشترك الجميع في صورة الضغط."},"support_links":["sup_03e6984b5b8ec06cede8"]},{"boundary":"Dal insanı kusuru üzerinden kötüleme ve çekiştirmeyle sınırlıdır; fiziksel baskı, itme ve zihne gelen kötü düşünceler bunun dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001600/B004","candidate_links":[{"candidate_id":"cand_5ce8d59c5bd5accadb08","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","surface_ar":"هُمَزَةٍ"}],"gloss":"ayıplama ve çekiştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimseyi kusur bularak ayıplama, kötüleme veya çekiştirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiyi yokluğunda ve arkasından kötülemek, çekirdeğin özellikle belirtilen bir gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam, sürekli kusur bulan veya başkalarını arkalarından kötüleyen kişiyi niteleyen biçimlere uzanır."}}],"root_ar":"ه م ز","root_id":"root_001600","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kusur bularak kötüleme çekirdeğini ve bunun kişinin arkasından yapılabilen biçimini birlikte karşılar.","boundary_detail":"Dal insanı kusuru üzerinden kötüleme ve çekiştirmeyle sınırlıdır; fiziksel baskı, itme ve zihne gelen kötü düşünceler bunun dışındadır.","branch_image_ar":"عيب الناس والوقيعة فيهم","concept_gloss":"ayıplama ve çekiştirme","contextual_glosses":[{"applicability":"Bir kişinin kusurlarının öne çıkarılarak ayıplandığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötülemenin özellikle kişinin yokluğunda yapılması yönünü zorunlu olarak belirtmez.","preserves":"Kusur bulma ve kişiyi bunun üzerinden kötüleme çekirdeğini korur."},"facet_ids":["F001"],"text":"kusur bulup kötülemek","usage_role":"general"},{"applicability":"Bir kişinin yokluğunda kusurlarının konuşulup kötülenmesi bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin yüzüne karşı veya bulunma koşulundan bağımsız yapılan genel ayıplamayı dışarıda bırakır.","preserves":"Kişinin yokluğunda kötülenmesi ve kusurlarının konuşulması yönünü korur."},"facet_ids":["F001","F002"],"text":"arkasından çekiştirmek","usage_role":"contextual"}],"definition":"Bir kimsenin kusurlarını öne çıkararak onu ayıplamak veya arkasından kötüleyip çekiştirmektir; aynı anlam alanı bu işi yapan kişiyi de niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimseyi kusur bularak ayıplama, kötüleme veya çekiştirme."},{"facet_id":"F002","role":"specialization","statement":"Kişiyi yokluğunda ve arkasından kötülemek, çekirdeğin özellikle belirtilen bir gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"Aynı anlam, sürekli kusur bulan veya başkalarını arkalarından kötüleyen kişiyi niteleyen biçimlere uzanır."}],"identity_rationale":"Kaynak ifadesi insanlarda kusur bulmayı, onları ayıplamayı ve özellikle arkalarından kötüleyip çekiştirmeyi ortak bir dalda toplar. Eylem adları ile bu işi yapan kişiyi bildiren biçimler aynı anlam alanını düzenli biçimde gerçekleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"insanları ayıplama veya arkalarından kötüleme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kusur bulan veya başkalarını kötüleyen kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sürekli kusur bulan veya arkadan kötüleyen kimse"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayıplayan veya çekiştiren kimse"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bir insanı arkasından kötülemek veya ayıplamak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yakınını arkasından ayıplayıp kötülemek"}],"lexicalization_note":"Tanım, genel ayıplama eylemini arkadan kötüleme yapısından ve bu işi yapan kişiyi belirten biçimlerden ayırarak korur.","neighbor_coverage_note":"Bütün komşular değerlendirildi; işaretle ayıplama ve kişinin yokluğunda anılması, bu dalın kötüleme koşulunu en iyi belirginleştiren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kusur bulma ile arkadan kötülemeyi öne çıkarır; komşu dal buna göz, ağız veya örtük sözle yapılan iğneleyici ayıplamayı da ekler.","focus_only":"Bu dal, ayıplayan kişi biçimlerini ve kişinin arkasından kötülenmesini özellikle belirginleştirir.","gloss":"ayıplama ve işaretle kusur gösterme","neighbor_only":"Komşu dal, göz veya ağız işaretiyle ayıplamayı ve örtük sözle kusur göstermeyi de açıkça kapsar.","neighbor_ref":"root_001376/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir kişide kusur bulma, onu ayıplama ve hakkında kötü konuşma vardır."},{"boundary_match":"partial","distinction":"Odak dal ayıplama ve kötülemeyi zorunlu kılar; komşu dal ise kişinin yokluğunda anılmasını merkez alır ve sınırı bazı anlatımlarda kötü sözden daha geniştir.","focus_only":"Bu dal genel kusur bulup ayıplamayı ve bu davranışı yapan kişiyi de kapsar.","gloss":"arkadan kötüleme ve yokluğunda anma","neighbor_only":"Komşu dalın çekirdeği, bir kişiden özellikle o yokken söz etmektir ve bazı aktarımlarda söz olumlu da olabilir.","neighbor_ref":"root_001117/B004","relation_type":"near_synonym","shared_zone":"Her iki dal, bir kişi yokken onun kusurlarından söz ederek onu kötüleme bağlamında örtüşür."}],"source_phrase_ar":"الهماز العياب وكذا الهمزة (maqayis)؛ الهمز مثل اللمز والهامز والهماز العياب والهمزة مثله (sihah)؛ الهماز المغتابون في الغيب واللماز المغتابون في الحضرة (tahdhib)؛ الهمز العيب (tahdhib)؛ الهماز والهمزة الذي يهمز أخاه في قفاه من خلفه (tahdhib)؛ همز الإنسان اغتيابه (mufradat)","source_summary":"Kaynakların ortak anlam alanı, insanlarda kusur bulma, onları ayıplama ve kötüleme ile bu davranışı yapan kişiyi niteleyen biçimlerdir; yoklukta ve arkadan kötüleme ayrımı Tahdhib'e, gıybet açıklaması Mufradat'a bağlı aktarım ayrıntılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الهمز بمعنى العيب والغيبة والوقيعة، وأوصاف الهامز والهماز والهمزة.","what_is_not_ar":"لا يدخل فيه الضغط الحسي ولا دفع السهم ولا خطرات الشيطان إلا إذا صرحت المادة بعيب الناس."},"support_links":["sup_06fe90d5be6dce824180"]},{"boundary":"Bu dal yalnızca şeytana bağlanan zihinsel veya kalbi bastıran etki içindir; sıradan düşünce, fiziksel baskı ve insanları kötüleme kapsam dışıdır.","branch_kind":"collocation","branch_ref":"root_001600/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","surface_ar":"هُمَزَةٍ"}],"gloss":"şeytanın kalbe kötü düşünce veya ağır etki salması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şeytanın insanın kalbine kötü düşünceler sokması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkinin kalbi bastıran ağır bir nöbet veya delilik gibi açıklanması."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu ağır etkinin içten dürtme ve sıkıştırma imgesiyle adlandırılması."}}],"root_ar":"ه م ز","root_id":"root_001600","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca şeytana bağlanan kötü düşünce düşürme ve kalbi bastıran ağır etki açıklamalarını birlikte karşılar.","boundary_detail":"Bu dal yalnızca şeytana bağlanan zihinsel veya kalbi bastıran etki içindir; sıradan düşünce, fiziksel baskı ve insanları kötüleme kapsam dışıdır.","branch_image_ar":"همز الشيطان يغلب على القلب","concept_gloss":"şeytanın kalbe kötü düşünce veya ağır etki salması","contextual_glosses":[{"applicability":"Şeytanın insanın zihnine veya kalbine kötü düşünceler soktuğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalbi bastıran ağır durum ve delilik biçimindeki kaynak değişkesini dışarıda bırakır.","preserves":"Şeytanın kalbe kötü düşünceler sokması yönünü korur."},"facet_ids":["F001"],"text":"kalbe kötü düşünceler düşürme","usage_role":"contextual"},{"applicability":"Etkinin ağır bir nöbet, delilik veya içten dürtülme gibi açıklandığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalbe tek tek kötü düşünceler düşürülmesi açıklamasını doğrudan belirtmez.","preserves":"Şeytanı kaynak olarak ve kalbi ağır biçimde etkileyen baskı yönünü korur."},"facet_ids":["F002","F003"],"text":"şeytanın kalbi bastıran etkisi","usage_role":"explanatory"}],"definition":"Şeytanın insanın kalbine kötü düşünceler düşürmesi veya kalbini bastıran ağır bir etki yaratmasıdır. Bu ikinci etki delilik, içten dürtme ya da sıkıştırma imgesiyle de açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şeytanın insanın kalbine kötü düşünceler sokması."},{"facet_id":"F002","role":"source_variant","statement":"Etkinin kalbi bastıran ağır bir nöbet veya delilik gibi açıklanması."},{"facet_id":"F003","role":"associated_use","statement":"Bu ağır etkinin içten dürtme ve sıkıştırma imgesiyle adlandırılması."}],"identity_rationale":"Kaynak ifadesi tek bir olayı değil, şeytanın insanın kalbine kötü düşünceler düşürmesi ile kalbi bastıran ve delilik gibi yorumlanan ağır bir etkiyi birlikte aktarır. Dal korunabilir, ancak bu iki açıklama birbirine indirgenmeden kaynak değişkeleri olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şeytanın insanın kalbine düşürdüğü kötü düşünceler"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"şeytanın kalbi bastıran, delilik veya içten dürtme gibi açıklanan etkisi"}],"lexicalization_note":"Tanım yalnızca şeytanın etkisini bildiren yapıya bağlıdır ve buradan bağımsız, genel bir zihinsel etki anlamı çıkarmaz.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; yalnızca fiziksel dürtme dalı, bu yapının açıklayıcı imgesini sınırlandıran doğrudan bir karşılaştırma sağlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda dürtme yalnızca görünmez ve kalbe yönelen etkinin açıklama imgesidir; komşu dalda ise gerçek bir hareket doğuran fiziksel eylemdir.","focus_only":"Bu dal, kötücül bir varlığa bağlanan kalp ve zihin üzerindeki görünmez etkiyi anlatır.","gloss":"içsel etki ve fiziksel dürtme","neighbor_only":"Komşu dal, bir nesne veya canlıya uygulanan somut itme, vurma ve dürtme eylemlerini anlatır.","neighbor_ref":"root_001600/B003","relation_type":"near_neighbor","shared_zone":"Kötücül etki, kaynak anlatımında fiziksel dürtme ve sıkıştırma imgesiyle açıklanır."}],"source_phrase_ar":"همز الشيطان كالموتة تغلب على قلب الإنسان (maqayis)؛ همزات الشيطان خطراته التي يخطرها بقلب الإنسان (sihah)؛ أما همزه فالموتة والموتة الجنون وإنما سماه همزا لأنه جعله من النخس والغمز (tahdhib)؛ أعوذ بك من همزات الشياطين (mufradat)","source_summary":"Kanıt bütünü, şeytana bağlanan etkiyi kalbe düşürülen düşünceler ve kalbi bastıran ağır bir durum yönleriyle aktarır; kötü düşünceler Sihah'ta, ölüm benzeri kalp etkisi Maqayis'te, delilik ve dürtme-sıkma gerekçesi Tahdhib'de, dua içindeki kullanım Mufradat'ta ayrışır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه همز الشيطان وخطراته أو الموتة التي تغلب على قلب الإنسان، وما فسر في الحديث بالجنون أو النخس والغمز.","what_is_not_ar":"لا يدخل فيه عيب الناس ولا ضغط الأجسام ولا الهمز الصوتي."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_341eb63e41bdd75b2ee0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:doom-and-imprecation-range","source_type":"word_analysis","support_ids":["sup_330f8bf28d9ad7ee9b34","sup_ccca0ae6738ec6629df6"],"title":"doom noun with imprecatory force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_8abd1c9996673a577f60","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:indefinite-unbounded-woe","source_type":"word_analysis","support_ids":["sup_0fc32ff00c82916b2f42","sup_ccca0ae6738ec6629df6"],"title":"indefiniteness leaves woe unmeasured","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_87d39349603d2b1629d4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:local-salience-summary","source_type":"word_analysis","support_ids":["sup_5e821335a2dbbbc54685","sup_ccca0ae6738ec6629df6"],"title":"opening word governs the ayah frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_a8933b5feda32b81473d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:nominal-verdict-frame","source_type":"word_analysis","support_ids":["sup_27b56735722664987d1d","sup_ccca0ae6738ec6629df6"],"title":"verbless nominal verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_ffc6b03eca33571eb432","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:opening-compression-and-sound-link","source_type":"word_analysis","support_ids":["sup_46a0a2e388d16b8945df","sup_ccca0ae6738ec6629df6"],"title":"compressed opening carries verdict into target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:1"],"branch_refs":[],"candidate_id":"cand_a53880893446d04e27a6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"104:1:1:quranic-woe-formula-specialized","source_type":"word_analysis","support_ids":["sup_ccca0ae6738ec6629df6","sup_d6edfedab233741e616f"],"title":"known woe formula redirected to social harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:1","qac_refs":["104:1:1:1"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_20c0290707b88590c5ed","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:construct-chain-compression","source_type":"word_analysis","support_ids":["sup_818f6e6596e93a3757b8","sup_afb1ecb88f555c28cc53"],"title":"construct chain binds scope to descriptor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_56adc38cb8f4be7efb16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:distributive-totality","source_type":"word_analysis","support_ids":["sup_175fb9fd5604ab552a74","sup_afb1ecb88f555c28cc53"],"title":"every member is included","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_d84e9621eb365c317bec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:exhaustive-completeness-pressure","source_type":"word_analysis","support_ids":["sup_0d9addcdb722731c6e2a","sup_afb1ecb88f555c28cc53"],"title":"root image sharpens total coverage","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_f0c1cab308ee2c893c27","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:preposition-governs-allocation","source_type":"word_analysis","support_ids":["sup_1309cd8b909da0acb44e","sup_afb1ecb88f555c28cc53"],"title":"prefixed preposition assigns the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_6805da104b5bffa22f05","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:sound-binding-to-target","source_type":"word_analysis","support_ids":["sup_268f7880811cf6828bf3","sup_afb1ecb88f555c28cc53"],"title":"sound carries function into content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_6dc0180a45ba4fe05af9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:variant-preserves-standard-apposition","source_type":"word_analysis","support_ids":["sup_08f651e817fa982b7556","sup_afb1ecb88f555c28cc53"],"title":"variant contrast protects one generic target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_1b9011a0d52cc33beb0f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:woe-to-every-formula","source_type":"word_analysis","support_ids":["sup_1cd857572c25ceb381ed","sup_afb1ecb88f555c28cc53"],"title":"woe-to-every formula is visible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:2","qac_refs":["104:1:2:1","104:1:2:2"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_e6ad83b2ac15cd70fc9a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:appositional-paired-offender","source_type":"word_analysis","support_ids":["sup_879da00ae8ee95fade04","sup_c7175e71ec7a01e66525"],"title":"first half of one composite offender","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_0702999a0fe4bd41dc5b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:generic-distributed-descriptor","source_type":"word_analysis","support_ids":["sup_c42813d75ede20d7b82a","sup_c7175e71ec7a01e66525"],"title":"descriptor narrows the universal target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_f439c70a7c1de65b275c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:intensive-generic-agent-form","source_type":"word_analysis","support_ids":["sup_bfceafbb54fd742e9ad8","sup_c7175e71ec7a01e66525"],"title":"intensive form makes habit into identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_870573fbf96844a385f4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:negative-agent-valence","source_type":"word_analysis","support_ids":["sup_2af4d3e31e743bbaca52","sup_c7175e71ec7a01e66525"],"title":"moral blame is built into the lexeme","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_88cdb2593b8857def53e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:pressure-image-in-social-aggression","source_type":"word_analysis","support_ids":["sup_c7175e71ec7a01e66525","sup_ec4050b4d14f2e725263"],"title":"pressure image becomes verbal attack","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_8dd04da888275b1dcb9a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:rare-form-and-68-11-echo","source_type":"word_analysis","support_ids":["sup_c7175e71ec7a01e66525","sup_d2444be5e60666f56f46"],"title":"rare slander field focused at the opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_63b2b2f8645739285312","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:sound-pair-with-semantic-split","source_type":"word_analysis","support_ids":["sup_901f03a8e69dbeed87b2","sup_c7175e71ec7a01e66525"],"title":"near-rhyme binds without flattening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:3","qac_refs":["104:1:3:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_9ad207f5ddd45599e186","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:appositional-second-description","source_type":"word_analysis","support_ids":["sup_6ff37a1bd74e831c863f","sup_a93cf0c5584614034c2e"],"title":"second descriptor stays on the same offender","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_1f37f6bcbd2817d8039e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:closing-cadence-pair","source_type":"word_analysis","support_ids":["sup_39a9825a11f989449c95","sup_6ff37a1bd74e831c863f"],"title":"final cadence completes the pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_f3f1135b1c7ae7b42c97","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:covert-fault-marking-sense","source_type":"word_analysis","support_ids":["sup_6ff37a1bd74e831c863f","sup_a9928166a6b9e8e98f2f"],"title":"covert contempt and defect-marking","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_7891e9999767507e10b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:form-rarity-identity-focus","source_type":"word_analysis","support_ids":["sup_6ff37a1bd74e831c863f","sup_bd79728355dce1c7ceda"],"title":"rare adjective concentrates identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_f6bc00d695dbc1453c01","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:intensive-generic-agent-and-variant","source_type":"word_analysis","support_ids":["sup_3e3ed8a5817d4cb08bfd","sup_6ff37a1bd74e831c863f"],"title":"habitual generic agent, not one act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_1fd85551541cc4126bd0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:quranic-fault-finding-field","source_type":"word_analysis","support_ids":["sup_506786b2048e1499c2ea","sup_6ff37a1bd74e831c863f"],"title":"rare fault-finding field contextualizes the word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_a504c7ccb6d01d0211b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:sound-texture-side-channel","source_type":"word_analysis","support_ids":["sup_0eb8598a42010e37e557","sup_6ff37a1bd74e831c863f"],"title":"sound texture suits side-channel contempt","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"104:1:4","qac_refs":["104:1:4:1"],"status":"accepted"}},{"anchor_refs":["104:1:2"],"branch_refs":[],"candidate_id":"cand_d7449ea65b8a31dfeca5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001315"],"scope":"focus_ayah","source_local_id":"104:1:2:2","source_type":"qac_morpheme","support_ids":["sup_7df3b5ed64b6e6280e63"],"title":"QAC root occurrence: ك ل ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:1:3"],"branch_refs":[],"candidate_id":"cand_a2a26c1d8a1c415a2183","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001600"],"scope":"focus_ayah","source_local_id":"104:1:3:1","source_type":"qac_morpheme","support_ids":["sup_235a9b221627fda2945d"],"title":"QAC root occurrence: ه م ز","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:1:4"],"branch_refs":[],"candidate_id":"cand_4f084590564722c2ae0a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001376"],"scope":"focus_ayah","source_local_id":"104:1:4:1","source_type":"qac_morpheme","support_ids":["sup_e44a10b5b3941b2cbb8d"],"title":"QAC root occurrence: ل م ز","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["104:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:1","branch_refs":["root_001315/B003","root_001376/B001","root_001600/B004"],"candidate_id":"cand_5ce8d59c5bd5accadb08","commentary_obligation":"review","hft_ref":"hft_3b7c4387668565168cd4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_dual_channel_faultfinding","source_type":"hft","support_ids":["sup_06fe90d5be6dce824180"],"title":"b_dual_channel_faultfinding","trust":"legacy_unbound"},{"anchor_refs":["104:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"104:1","branch_refs":["root_001376/B002","root_001600/B001","root_001600/B003"],"candidate_id":"cand_11790f2358e1d516f0ba","commentary_obligation":"review","hft_ref":"hft_8a4307594d5a22f8551f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_pressure_and_impulse","source_type":"hft","support_ids":["sup_03e6984b5b8ec06cede8"],"title":"b_pressure_and_impulse","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ","qac_morphemes":[{"lemma_ar":"وَيْل","morph_features":"STEM|POS:N|LEM:wayol|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:1:1","qac_word_ref":"104:1:1","root_ar":"","surface_ar":"وَيْلٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"104:1:2:1","qac_word_ref":"104:1:2","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","root_ar":"ك ل ل","surface_ar":"كُلِّ"},{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","root_ar":"ه م ز","surface_ar":"هُمَزَةٍ"},{"lemma_ar":"لُّمَزَة","morph_features":"STEM|POS:N|LEM:l~umazap|ROOT:lmz|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:4:1","qac_word_ref":"104:1:4","root_ar":"ل م ز","surface_ar":"لُّمَزَةٍ"}],"word_analysis_qac_refs":[["104:1:1:1"],["104:1:2:1","104:1:2:2"],["104:1:3:1"],["104:1:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["104:1:1","104:1:2","104:1:3","104:1:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ","qac_morphemes":[{"lemma_ar":"وَيْل","morph_features":"STEM|POS:N|LEM:wayol|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:1:1","qac_word_ref":"104:1:1","root_ar":"","surface_ar":"وَيْلٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"104:1:2:1","qac_word_ref":"104:1:2","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"كُلّ","morph_features":"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:2:2","qac_word_ref":"104:1:2","root_ar":"ك ل ل","surface_ar":"كُلِّ"},{"lemma_ar":"هُمَزَة","morph_features":"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:3:1","qac_word_ref":"104:1:3","root_ar":"ه م ز","surface_ar":"هُمَزَةٍ"},{"lemma_ar":"لُّمَزَة","morph_features":"STEM|POS:N|LEM:l~umazap|ROOT:lmz|F|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"104:1:4:1","qac_word_ref":"104:1:4","root_ar":"ل م ز","surface_ar":"لُّمَزَةٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["104:1:1:1"],["104:1:2:1","104:1:2:2"],["104:1:3:1"],["104:1:4:1"]],"word_analysis_refs":["104:1:1","104:1:2","104:1:3","104:1:4"],"word_rows":[{"analysis_record_ref":"104:1:1","analytic_gloss_range_en":"an indefinite doom or woe placed as the opening subject of a verbless condemnation, with exclamatory force still felt","analytic_root_gloss_range_en":"doom, destructive harm, punishment, calamity, disgrace, lament, and state or place of ruin; the local word selects the doom-allocation branch while retaining imprecatory force","qac_refs":["104:1:1:1"],"root":{"arabic":"و ي ل","transliteration":"w-y-l"},"surface":{"arabic":"وَيْلٌ","transliteration":"waylun"}},{"analysis_record_ref":"104:1:2","analytic_gloss_range_en":"for every, with the prefixed preposition assigning the verdict and the construct quantifier distributing it to each fitting individual","analytic_root_gloss_range_en":"totality, completeness, and other distant branches such as weariness, dependence, surrounding, and collateral relation; locally the totality branch is selected","qac_refs":["104:1:2:1","104:1:2:2"],"root":{"arabic":"ك ل ل","transliteration":"k-l-l"},"surface":{"arabic":"لِكُلِّ","transliteration":"li-kulli"}},{"analysis_record_ref":"104:1:3","analytic_gloss_range_en":"a generic intensive descriptor for a habitual slanderer or verbal aggressor, with pressure and compression imagery behind the social attack","analytic_root_gloss_range_en":"pressing, squeezing, prodding, articulatory pressure, taunting, disparaging, backbiting, and satanic prompting; locally the social disparagement branch is selected with physical pressure as image-pressure","qac_refs":["104:1:3:1"],"root":{"arabic":"ه م ز","transliteration":"h-m-z"},"surface":{"arabic":"هُمَزَةٍ","transliteration":"humazatin"}},{"analysis_record_ref":"104:1:4","analytic_gloss_range_en":"a second intensive descriptor for habitual indirect fault-finding, coded contempt, or defect-marking, appositional to the previous descriptor","analytic_root_gloss_range_en":"covert blame, fault-finding, defect-tracking, backbiting, gesture or hidden speech, and a distinct physical pushing branch; locally the covert fault-finding branch is selected","qac_refs":["104:1:4:1"],"root":{"arabic":"ل م ز","transliteration":"l-m-z"},"surface":{"arabic":"لُمَزَةٍ","transliteration":"lumazatin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["104:1"],"branch_refs":["root_001315/B003","root_001376/B001","root_001600/B004"],"candidate_id":"cand_5ce8d59c5bd5accadb08","evidence_scope":"focus_ayah","hft_ref":"hft_3b7c4387668565168cd4","item_id":"b_dual_channel_faultfinding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_dual_channel_faultfinding","support_id":"sup_06fe90d5be6dce824180"},{"anchor_refs":["104:1"],"branch_refs":["root_001376/B002","root_001600/B001","root_001600/B003"],"candidate_id":"cand_11790f2358e1d516f0ba","evidence_scope":"focus_ayah","hft_ref":"hft_8a4307594d5a22f8551f","item_id":"b_pressure_and_impulse","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_pressure_and_impulse","support_id":"sup_03e6984b5b8ec06cede8"}],"diagnostics":[],"lane_counts":{"global":10,"macro":12,"micro":2},"packet_summary":{"ayah_count":9,"focus_ref":"104:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"104:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"104:1","lane":"micro","linguistic_source_ref":"104:1","surface_ref":"104:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"104:1","target_tokens":[["Her",["104:1:2"]],["karalayıp",["104:1:3"]],["ayıplayanın",["104:1:4"]],["vay",["104:1:1"]],["hâline",["104:1:1"]]],"text":"Her karalayıp ayıplayanın vay hâline!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":9,"id":"s104-p01-001-009","label":"Whole surah","number":1,"refs":["104:1","104:2","104:3","104:4","104:5","104:6","104:7","104:8","104:9"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:variant-preserves-standard-apposition","source_type":"word_analysis","support_id":"sup_08f651e817fa982b7556","text":"{\"blocking_evidence\":null,\"headline\":\"variant contrast protects one generic target\",\"reader_payoff\":\"The reader notices that the standard wording keeps a universal construct chain with layered descriptors, instead of splitting the descriptors into two coordinated known figures.\",\"reason\":\"The accepted variant is useful as contrast, but local grammar is governed by the standard surface: no coordinating particle appears between the two descriptors, and the second descriptor is appositional.\",\"representative_source_ids\":[\"QF-13ae8f0e\",\"QF-15e201d7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:exhaustive-completeness-pressure","source_type":"word_analysis","support_id":"sup_0d9addcdb722731c6e2a","text":"{\"blocking_evidence\":null,\"headline\":\"root image sharpens total coverage\",\"reader_payoff\":\"The reader feels the universal as exhaustive coverage, not as a loose plural gesture.\",\"reason\":\"The selected local branch is totality and completeness. Other root-family images such as weariness or exhaustion are not independent local senses, but they can be retained cautiously as image-pressure for exhaustive coverage.\",\"representative_source_ids\":[\"QS-385b4c67\",\"QY-8c33d550\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:sound-texture-side-channel","source_type":"word_analysis","support_id":"sup_0eb8598a42010e37e557","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture suits side-channel contempt\",\"reader_payoff\":\"The reader hears the word's side-channel texture as matching its indirect gesture-and-signal semantics.\",\"reason\":\"The phonetic row remains locally tied to the selected covert fault-finding branch, so it adds sound texture without creating a separate semantic branch.\",\"representative_source_ids\":[\"QP-36514a1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:indefinite-unbounded-woe","source_type":"word_analysis","support_id":"sup_0fc32ff00c82916b2f42","text":"{\"blocking_evidence\":null,\"headline\":\"indefiniteness leaves woe unmeasured\",\"reader_payoff\":\"The reader feels the threat as open-ended because the word names a woe without defining its size, kind, or limit.\",\"reason\":\"The local noun is singular and indefinite, and the QAC grammar explicitly treats that indefiniteness as rhetorically marked rather than accidental.\",\"representative_source_ids\":[\"QG-6161443c\",\"QF-063864a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:preposition-governs-allocation","source_type":"word_analysis","support_id":"sup_1309cd8b909da0acb44e","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed preposition assigns the verdict\",\"reader_payoff\":\"The reader sees that the second word does not merely mean every; its prefixed preposition grammatically assigns the opening woe to the target class.\",\"reason\":\"Attachment evidence marks the prepositional relation as syntactically forced, and QAC identifies the prefixed preposition as governing the genitive quantifier.\",\"representative_source_ids\":[\"QG-5798d48e\",\"QG-c26ed4be\",\"QS-13902409\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:distributive-totality","source_type":"word_analysis","support_id":"sup_175fb9fd5604ab552a74","text":"{\"blocking_evidence\":null,\"headline\":\"every member is included\",\"reader_payoff\":\"The reader notices that the condemnation is distributive: each qualifying person is covered, not only the class in the abstract.\",\"reason\":\"V4 lists totality and completeness as the relevant branch, and the QAC grammar says the construct universalizes every instance of the described behavior.\",\"representative_source_ids\":[\"QG-bf82e49e\",\"QS-1356c8f5\",\"QF-9677ede0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:woe-to-every-formula","source_type":"word_analysis","support_id":"sup_1cd857572c25ceb381ed","text":"{\"blocking_evidence\":null,\"headline\":\"woe-to-every formula is visible\",\"reader_payoff\":\"The reader sees a marked Qur'anic allocation pattern in which woe is attached to every member of a condemned type (45:7).\",\"reason\":\"The supplied cooccurrence rows explicitly connect the local roots with the same allocation pattern at 45:7, while the commonness of the quantifier itself does not erase the marked pairing.\",\"representative_source_ids\":[\"QI-330b29de\",\"QI-48e18b22\",\"QE-1eaaeb99\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:1:3:1","source_type":"qac_morpheme","support_id":"sup_235a9b221627fda2945d","text":"{\"lemma_ar\":\"هُمَزَة\",\"morph_features\":\"STEM|POS:N|LEM:humazap|ROOT:hmz|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:1:3:1\",\"qac_word_ref\":\"104:1:3\",\"root_ar\":\"ه م ز\",\"surface_ar\":\"هُمَزَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:sound-binding-to-target","source_type":"word_analysis","support_id":"sup_268f7880811cf6828bf3","text":"{\"blocking_evidence\":null,\"headline\":\"sound carries function into content\",\"reader_payoff\":\"The reader hears the function word bind the verdict to its target before the full descriptor phrase is complete.\",\"reason\":\"The sound observation tracks the actual local sequence and supports, rather than replaces, the syntactic allocation relation.\",\"representative_source_ids\":[\"QE-96137102\",\"QP-81140a5f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:nominal-verdict-frame","source_type":"word_analysis","support_id":"sup_27b56735722664987d1d","text":"{\"blocking_evidence\":null,\"headline\":\"verbless nominal verdict\",\"reader_payoff\":\"The reader notices that the ayah does not narrate a punishment event; it places ruin itself as the standing subject before the target is named.\",\"reason\":\"QAC and attachment evidence identify {{ar:وَيْلٌ}} ({{tr:waylun}}) as an indefinite nominative subject in a nominal predication, with the following prepositional phrase supplying the recipient relation.\",\"representative_source_ids\":[\"QG-2cc3755c\",\"QG-72fee9b1\",\"QT-95f43ac5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:negative-agent-valence","source_type":"word_analysis","support_id":"sup_2af4d3e31e743bbaca52","text":"{\"blocking_evidence\":null,\"headline\":\"moral blame is built into the lexeme\",\"reader_payoff\":\"The reader notices that the word already carries moral accusation before the surah adds any later punishment scene.\",\"reason\":\"The locally selected branch includes taunting, faultfinding, disparaging, and backbiting, and the form makes the offender the active bearer of that blame.\",\"representative_source_ids\":[\"QS-6975e138\",\"QY-291f5b71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:doom-and-imprecation-range","source_type":"word_analysis","support_id":"sup_330f8bf28d9ad7ee9b34","text":"{\"blocking_evidence\":null,\"headline\":\"doom noun with imprecatory force\",\"reader_payoff\":\"The reader sees that the word is not a neutral label for sadness; it assigns destructive doom while still sounding like an uttered curse.\",\"reason\":\"V4 supports doom, destructive harm, punishment, calamity, and lament. The local nominal syntax selects the doom-allocation noun, while the exclamatory or lament force survives as discourse pressure rather than a separate local sense.\",\"representative_source_ids\":[\"QS-20269405\",\"QS-7ad685e9\",\"QS-81a2a730\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:closing-cadence-pair","source_type":"word_analysis","support_id":"sup_39a9825a11f989449c95","text":"{\"blocking_evidence\":null,\"headline\":\"final cadence completes the pair\",\"reader_payoff\":\"The reader hears the final word complete the paired sound-frame while giving indirect contempt the ayah's closing position.\",\"reason\":\"The two descriptors share pattern, case, and final cadence, and the ayah closes on the second descriptor. The sound effect therefore reinforces the appositional pair without erasing the semantic split.\",\"representative_source_ids\":[\"QT-3b395f79\",\"QE-5dc437ee\",\"QE-f7c8c3c4\",\"QP-e08d7e1d\",\"QY-214b24a3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:intensive-generic-agent-and-variant","source_type":"word_analysis","support_id":"sup_3e3ed8a5817d4cb08bfd","text":"{\"blocking_evidence\":null,\"headline\":\"habitual generic agent, not one act\",\"reader_payoff\":\"The reader sees the standard form preserve one generic habitual offender, rather than a single event or two definite coordinated labels.\",\"reason\":\"The word row marks the same intensive pattern as the preceding descriptor, and the variant evidence functions as contrast for agent-versus-act and apposition-versus-coordination.\",\"representative_source_ids\":[\"QF-1a370880\",\"QF-b3fd5314\",\"QF-c66d48e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:opening-compression-and-sound-link","source_type":"word_analysis","support_id":"sup_46a0a2e388d16b8945df","text":"{\"blocking_evidence\":null,\"headline\":\"compressed opening carries verdict into target\",\"reader_payoff\":\"The reader hears and sees the opening verdict run directly into the recipient phrase, matching the grammar of allocation.\",\"reason\":\"The ayah is one uninterrupted nominal sentence, and the local surface places the indefinite ending immediately before the governed recipient phrase.\",\"representative_source_ids\":[\"QT-22a4176e\",\"QT-8f113020\",\"QF-c85e8033\",\"QE-e02d17ff\",\"QP-3d606e01\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:quranic-fault-finding-field","source_type":"word_analysis","support_id":"sup_506786b2048e1499c2ea","text":"{\"blocking_evidence\":null,\"headline\":\"rare fault-finding field contextualizes the word\",\"reader_payoff\":\"The reader places the word within a wider Qur'anic fault-finding field that includes charity-related criticism (9:58; 9:79) and self-damaging mutual contempt (49:11).\",\"reason\":\"The occurrence rows give concrete references at 9:58, 9:79, and 49:11. They contextualize the local descriptor as corrosive fault-finding, but the claim is narrowed so those passages do not make charity or reflexive self-harm the selected local sense in 104:1.\",\"representative_source_ids\":[\"MS-83984557\",\"QI-25447541\",\"QI-43bae173\",\"QI-93e2a2ec\",\"QE-03c0c064\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:local-salience-summary","source_type":"word_analysis","support_id":"sup_5e821335a2dbbbc54685","text":"{\"blocking_evidence\":null,\"headline\":\"opening word governs the ayah frame\",\"reader_payoff\":\"The reader recognizes the first word as the governing frame of the ayah, not as a disposable opening cry.\",\"reason\":\"Although the lexeme is common in the supplied occurrence profile, its first-word position and nominal-clause role make it locally salient as the frame under which the descriptors are read.\",\"representative_source_ids\":[\"QI-ec338079\",\"QP-1e3f8788\",\"QY-54063d2b\",\"QS-e82496f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4","source_type":"word_analysis","support_id":"sup_6ff37a1bd74e831c863f","text":"{\"gloss_range\":\"a second intensive descriptor for habitual indirect fault-finding, coded contempt, or defect-marking, appositional to the previous descriptor\",\"prose\":\"{{ar:لُمَزَةٍ}} ({{tr:lumazatin}}) does not introduce a second offender. It stays genitive, indefinite, and appositional to {{ar:هُمَزَةٍ}} ({{tr:humazatin}}), so the same generic person is described from another angle. Its local sense is indirect fault-finding: gesture, signal, hidden speech, and social defect-marking rather than a second synonym for frontal attack. The intensive form makes this a settled habit, and the variant evidence helps show what the standard wording preserves: one generic agent carrying both traits, not two coordinated figures and not a one-time act. As the final word of the ayah, it gives covert contempt the closing sound, while the repeated -maza cadence with a changed onset keeps it inseparable from the first descriptor. Its lateral opening and buzzing close also suit the side-channel texture of coded fault-marking. The wider occurrence field, including charity-related criticism in 9:58 and 9:79 and reflexive self-damaging contempt in 49:11, makes the word part of a Qur'anic profile of corrosive fault-finding, but those passages contextualize the local descriptor rather than replacing its immediate appositional role.\",\"root_display\":\"{{ar:ل م ز}} ({{tr:l-m-z}})\",\"root_gloss_range\":\"covert blame, fault-finding, defect-tracking, backbiting, gesture or hidden speech, and a distinct physical pushing branch; locally the covert fault-finding branch is selected\",\"surface_display\":\"{{ar:لُمَزَةٍ}} ({{tr:lumazatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:1:2:2","source_type":"qac_morpheme","support_id":"sup_7df3b5ed64b6e6280e63","text":"{\"lemma_ar\":\"كُلّ\",\"morph_features\":\"STEM|POS:N|LEM:kul~|ROOT:kll|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:1:2:2\",\"qac_word_ref\":\"104:1:2\",\"root_ar\":\"ك ل ل\",\"surface_ar\":\"كُلِّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2:construct-chain-compression","source_type":"word_analysis","support_id":"sup_818f6e6596e93a3757b8","text":"{\"blocking_evidence\":null,\"headline\":\"construct chain binds scope to descriptor\",\"reader_payoff\":\"The reader notices the hinge function of the word: it completes the verbless sentence while preparing the descriptor phrase as the covered behavior.\",\"reason\":\"The local attachments show a prepositional predicate relation back to the first word and an idafa relation forward to the first descriptor, matching the CRITICAL hinge claim.\",\"representative_source_ids\":[\"QF-73da5cd9\",\"QT-3feb55bb\",\"QT-a5ef2073\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:appositional-paired-offender","source_type":"word_analysis","support_id":"sup_879da00ae8ee95fade04","text":"{\"blocking_evidence\":null,\"headline\":\"first half of one composite offender\",\"reader_payoff\":\"The reader sees one composite offender being built by two matched descriptors, with frontal pressure paired to indirect fault-finding.\",\"reason\":\"Attachment evidence marks the next descriptor as appositional and translation support warns against collapsing the pair into one generic insult. The paired form and case therefore preserve one composite offender with two distinguishable traits.\",\"representative_source_ids\":[\"QG-9b6067a5\",\"QT-afa2a89f\",\"QE-64147e35\",\"QP-48591ab1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:sound-pair-with-semantic-split","source_type":"word_analysis","support_id":"sup_901f03a8e69dbeed87b2","text":"{\"blocking_evidence\":null,\"headline\":\"near-rhyme binds without flattening\",\"reader_payoff\":\"The reader hears the two descriptors as a paired cadence while still keeping direct pressure distinct from indirect contempt.\",\"reason\":\"The local surfaces share the same pattern and cadence, and the grammar supports apposition rather than repetition. Sound therefore reinforces the composite portrait without turning the roots into synonyms.\",\"representative_source_ids\":[\"QE-b798f662\",\"MH-432b9d14\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:appositional-second-description","source_type":"word_analysis","support_id":"sup_a93cf0c5584614034c2e","text":"{\"blocking_evidence\":null,\"headline\":\"second descriptor stays on the same offender\",\"reader_payoff\":\"The reader sees that the final word layers another trait onto the same generic offender, rather than naming a separate person.\",\"reason\":\"QAC and attachment evidence mark {{ar:لُمَزَةٍ}} ({{tr:lumazatin}}) as genitive and appositional to the preceding descriptor, with matching form and case.\",\"representative_source_ids\":[\"QG-2f94baa1\",\"QG-4b04a16c\",\"QG-d4c10df1\",\"QT-212615f1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:covert-fault-marking-sense","source_type":"word_analysis","support_id":"sup_a9928166a6b9e8e98f2f","text":"{\"blocking_evidence\":null,\"headline\":\"covert contempt and defect-marking\",\"reader_payoff\":\"The reader notices that the second descriptor adds indirect social signaling and defect-marking to the direct pressure of the first.\",\"reason\":\"V4 supports a local branch of covert blame, fault-finding, backbiting, and signaling by eye, mouth, or hidden speech. The distinct physical pushing branch is not selected by the local appositional social-descriptor frame.\",\"representative_source_ids\":[\"QS-02ae4751\",\"QS-50c28f27\",\"QS-860fcea6\",\"QT-4b414c09\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:2","source_type":"word_analysis","support_id":"sup_afb1ecb88f555c28cc53","text":"{\"gloss_range\":\"for every, with the prefixed preposition assigning the verdict and the construct quantifier distributing it to each fitting individual\",\"prose\":\"{{ar:لِكُلِّ}} ({{tr:li-kulli}}) turns the opening verdict into an assigned rule. The prefixed preposition governs the quantifier, so the woe is not left as a loose cry; it is routed to a recipient class. The quantifier then distributes that verdict across each member who fits the following description, not merely over a vague collective. Its construct form keeps the sentence compressed: the universal scope and the first descriptor are bound in one governed chain. A variant with definiteness and coordination shows what the standard wording avoids; the local form keeps one generic offender-type carrying both traits. The same word also participates in the marked woe-to-every allocation pattern noted at 45:7. The l-sound chain makes that allocation audible, beginning at the preposition and returning in the closing descriptor. The wider root can have other branches, but here totality and completeness are the selected force, with the secondary sense of exhaustion only sharpening the idea that no exception is left outside the scope.\",\"root_display\":\"{{ar:ك ل ل}} ({{tr:k-l-l}})\",\"root_gloss_range\":\"totality, completeness, and other distant branches such as weariness, dependence, surrounding, and collateral relation; locally the totality branch is selected\",\"surface_display\":\"{{ar:لِكُلِّ}} ({{tr:li-kulli}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:4:form-rarity-identity-focus","source_type":"word_analysis","support_id":"sup_bd79728355dce1c7ceda","text":"{\"blocking_evidence\":null,\"headline\":\"rare adjective concentrates identity\",\"reader_payoff\":\"The reader notices that this exact adjective is locally concentrated on identity, while the related occurrences elsewhere are verbal.\",\"reason\":\"The contextual profile marks the local adjective as low occurrence, and the supplied occurrence rows distinguish this exact adjective from verbal uses elsewhere.\",\"representative_source_ids\":[\"QH-186eed94\",\"QH-9883db69\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:intensive-generic-agent-form","source_type":"word_analysis","support_id":"sup_bfceafbb54fd742e9ad8","text":"{\"blocking_evidence\":null,\"headline\":\"intensive form makes habit into identity\",\"reader_payoff\":\"The reader sees that the form condemns a habitual agent, not a single act and not a sex-specific label.\",\"reason\":\"The word row identifies the form as an intensive adjective used generically. The sukun variant is useful as contrast because it shows how the standard vowels preserve agenthood.\",\"representative_source_ids\":[\"QF-fe46afaa\",\"QF-58102e25\",\"QF-690b86d9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:generic-distributed-descriptor","source_type":"word_analysis","support_id":"sup_c42813d75ede20d7b82a","text":"{\"blocking_evidence\":null,\"headline\":\"descriptor narrows the universal target\",\"reader_payoff\":\"The reader notices the sentence turn from universal scope into a specific behavioral type: the woe covers any bearer of this trait.\",\"reason\":\"QAC and attachment evidence place {{ar:هُمَزَةٍ}} ({{tr:humazatin}}) as the genitive complement of the construct quantifier, making it the first lexical narrowing of the condemned class.\",\"representative_source_ids\":[\"QG-0dcd25e8\",\"QG-e85d996c\",\"QT-7e332683\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3","source_type":"word_analysis","support_id":"sup_c7175e71ec7a01e66525","text":"{\"gloss_range\":\"a generic intensive descriptor for a habitual slanderer or verbal aggressor, with pressure and compression imagery behind the social attack\",\"prose\":\"{{ar:هُمَزَةٍ}} ({{tr:humazatin}}) is the first descriptor that gives the universal verdict a behavioral shape. Its genitive case makes it the complement of the quantifier, so the ayah is not naming one offender but any person who fits this trait. The intensive form makes the action habitual and identity-forming rather than occasional, and the form is generic rather than sex-specific. The sukun variant also shows the pressure point: the standard vowels keep responsibility attached to a habitual agent rather than shifting toward the act alone. The root's physical pressure range matters, but locally it is narrowed into social aggression: slander and disparagement feel like pressure applied to another person's honor, with even the compressed-breath image behind hamza retained as image-pressure rather than a separate sense. Beside {{ar:لُمَزَةٍ}} ({{tr:lumazatin}}), the word carries the more frontal half of the pair, while the shared -maza body with a changed onset makes the two descriptors one audible portrait without erasing their difference. Its rarity and its link with the trait-list in 68:11 concentrate the choice: here the slanderer-type is not buried in a list but placed at the center of the opening condemnation.\",\"root_display\":\"{{ar:ه م ز}} ({{tr:h-m-z}})\",\"root_gloss_range\":\"pressing, squeezing, prodding, articulatory pressure, taunting, disparaging, backbiting, and satanic prompting; locally the social disparagement branch is selected with physical pressure as image-pressure\",\"surface_display\":\"{{ar:هُمَزَةٍ}} ({{tr:humazatin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1","source_type":"word_analysis","support_id":"sup_ccca0ae6738ec6629df6","text":"{\"gloss_range\":\"an indefinite doom or woe placed as the opening subject of a verbless condemnation, with exclamatory force still felt\",\"prose\":\"{{ar:وَيْلٌ}} ({{tr:waylun}}) opens the ayah as a noun, not as a verb of threatening or narrating. Because the clause is verbless, the ruin is presented as a standing verdict before the offender is named. Its indefiniteness matters: the wording does not point to a known, measured punishment, but leaves the woe open in extent. The word also keeps its cry-like force, so the first sound of the ayah is both a verdict and an imprecation. Its wider root range can name destructive doom, calamity, lament, or even a state or place of ruin; here the following governed phrase assigns that inhabitable ruin to a behavioral type. The boundary is not inert either: the indefinite ending and repeated l-sound carry the verdict directly into its recipient phrase. The familiar Qur'anic woe formula visible beside 45:7 and 77:15 is therefore specialized: the threat is not aimed only at cosmic denial or liar formulas, but at the social violence named by the two descriptors that follow.\",\"root_display\":\"{{ar:و ي ل}} ({{tr:w-y-l}})\",\"root_gloss_range\":\"doom, destructive harm, punishment, calamity, disgrace, lament, and state or place of ruin; the local word selects the doom-allocation branch while retaining imprecatory force\",\"surface_display\":\"{{ar:وَيْلٌ}} ({{tr:waylun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:rare-form-and-68-11-echo","source_type":"word_analysis","support_id":"sup_d2444be5e60666f56f46","text":"{\"blocking_evidence\":null,\"headline\":\"rare slander field focused at the opening\",\"reader_payoff\":\"The reader notices that the rare slander field linked with 68:11 is isolated here as the surah's central opening portrait.\",\"reason\":\"The occurrence evidence identifies the root and form as rare in this profile and gives 68:11 as a concrete related slander context; that echo supports contrast in rhetorical placement without making 68:11 govern the local parse.\",\"representative_source_ids\":[\"QI-201f020b\",\"QI-749d4148\",\"QI-f3e28c11\",\"QE-16edd440\",\"QH-82fd8852\",\"QH-d19f0a75\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:1:quranic-woe-formula-specialized","source_type":"word_analysis","support_id":"sup_d6edfedab233741e616f","text":"{\"blocking_evidence\":null,\"headline\":\"known woe formula redirected to social harm\",\"reader_payoff\":\"The reader notices a familiar Qur'anic woe-allocation pattern being focused here on habitual slander and contempt, not only on denier formulas.\",\"reason\":\"The cooccurrence and occurrence rows support comparison with a woe-to-every formula (45:7) and other woe declarations. The absence of an explicit time marker in 104:1 lets the verdict stand without importing the stronger claim that the punishment is only present rather than eschatological.\",\"representative_source_ids\":[\"MS-355f503c\",\"QI-54e122e5\",\"QI-73e3c93a\",\"QE-260b6aa0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"104:1:4:1","source_type":"qac_morpheme","support_id":"sup_e44a10b5b3941b2cbb8d","text":"{\"lemma_ar\":\"لُّمَزَة\",\"morph_features\":\"STEM|POS:N|LEM:l~umazap|ROOT:lmz|F|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"104:1:4:1\",\"qac_word_ref\":\"104:1:4\",\"root_ar\":\"ل م ز\",\"surface_ar\":\"لُّمَزَةٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"104:1:3:pressure-image-in-social-aggression","source_type":"word_analysis","support_id":"sup_ec4050b4d14f2e725263","text":"{\"blocking_evidence\":null,\"headline\":\"pressure image becomes verbal attack\",\"reader_payoff\":\"The reader feels slander here as constricting pressure against another person's dignity, not as a flat synonym for bad speech.\",\"reason\":\"V4 separates physical pressing, articulatory pressure, prodding, and disparagement branches. The local paired descriptor frame selects social disparagement, while the pressure and compressed-speech imagery survives as image-pressure.\",\"representative_source_ids\":[\"QS-40665435\",\"QS-8de70d48\",\"QS-ea68687b\",\"QP-5d953ad5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ","ayah_ref":"104:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001315/B003","root_001376/B001","root_001600/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001315","role":"The branch literally supplies totality and completeness; here it distributes the condemnation across every instance of the paired aggressive type.","root":"ك ل ل","source_ref":"104:1","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001600","role":"The branch literally supplies taunting, backbiting, and attacking people's standing; it forms the more overt reputational channel.","root":"ه م ز","source_ref":"104:1","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001376","role":"The branch literally supplies covert fault-finding and signaling by eye, mouth, or hidden speech; it forms the deniable channel paired with overt attack.","root":"ل م ز","source_ref":"104:1","source_word_indices":["4"]}],"changed_reading":{"after":"Woe attaches to the habitual two-channel aggressor who circulates between open reputational attack and covert defect-signaling; the two labels map a social method rather than simply repeat one gloss.","before":"Woe to every person who insults or slanders."},"confidence":"strong","focus_anchor":"The distributive construction attaches woe to the paired habitual labels rooted in ه م ز and ل م ز.","mechanism":"The pair is not merely redundant abuse: one branch supplies overt taunting and reputational attack, while the other includes defect-tracking, backbiting, and covert signals by eye or mouth. Together they describe an aggressor who can move between public speech and deniable gesture, while the totalizer makes the type exhaustively liable.","model_id":"b_dual_channel_faultfinding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_dual_channel_faultfinding","source_type":"hft","support_id":"sup_06fe90d5be6dce824180","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ","ayah_ref":"104:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001376/B002","root_001600/B001","root_001600/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001600","role":"The branch literally supplies hand-pressure and squeezing; it makes the first label a social compression of the target.","root":"ه م ز","source_ref":"104:1","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001600","role":"The branch literally supplies a prod or impulse that sets something moving; it lets the attack mobilize others against the compressed target.","root":"ه م ز","source_ref":"104:1","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001376","role":"The branch literally supplies pushing or striking; it gives the second label the force of a social shove rather than a neutral observation.","root":"ل م ز","source_ref":"104:1","source_word_indices":["4"]}],"changed_reading":{"after":"The two nouns stage contempt as pressure and impulse: the victim is first compressed into a flaw and then pushed through the social field by word, look, or gesture.","before":"The two nouns name kinds of bad speech."},"confidence":"medium","focus_anchor":"Both focus labels retain physical-force branches: squeezing or prodding under ه م ز and pushing or striking under ل م ز.","mechanism":"The paired acts can be felt as a sequence of applied pressure: compress a person into a defect, then prod or shove that person before an audience. Verbal and gestural contempt thereby operate as social force, not merely as descriptive speech.","model_id":"b_pressure_and_impulse"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_pressure_and_impulse","source_type":"hft","support_id":"sup_03e6984b5b8ec06cede8","trust":"legacy_unbound"}]}
</lane_packet_json>
