# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:20**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_20/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:20",
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
{"branch_registry":[{"boundary":"Dinlenme, insan topluluğu ve çıkıntısızlık bu dalın değil, aynı kökün ayrı dallarının kapsamındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000261/B001","candidate_links":[{"candidate_id":"cand_2e44a647ba80a0a1b00c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"çoğalıp birikerek doluluğa ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey çoğalır, bir araya gelir ve belirgin bir bolluk oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu suyu bakımından, suyun kuyuda toplanıp çoğalması ya da bu suyun toplandığı yer anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölçü ve kapla kurulan kullanımlarda, içeriğin üst sınıra ulaşması veya dolmaya çok yaklaşması anlatılır."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel çokluk çekirdeğini, kuyudaki su birikimini ve ölçüye bağlı doluluk uzantısını birlikte karşılar.","boundary_detail":"Dinlenme, insan topluluğu ve çıkıntısızlık bu dalın değil, aynı kökün ayrı dallarının kapsamındadır.","branch_image_ar":"كثرة الشيء واجتماعه حتى يمتلئ","concept_gloss":"çoğalıp birikerek doluluğa ulaşma","contextual_glosses":[{"applicability":"Mal veya başka bir şeyin miktarca çokluğu söz konusu olduğunda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genel miktar çokluğunu ve bundan doğan bolluğu korur."},"facet_ids":["F001"],"text":"çok ve bol olma","usage_role":"contextual"},{"applicability":"Su, ölçü veya kap içeriğinin toplanıp üst sınıra ulaştığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birikme ile doluluk arasındaki aşamalı ilişkiyi korur."},"facet_ids":["F002","F003"],"text":"birikip ağzına kadar dolma","usage_role":"contextual"}],"definition":"Bir şeyin miktarca çoğalıp bir araya gelmesi ve bu birikmenin bolluk ya da doluluğa varmasıdır. Su için kuyuda toplanmayı, ölçü ve kap içinse ağza yaklaşan doluluğu anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey çoğalır, bir araya gelir ve belirgin bir bolluk oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Kuyu suyu bakımından, suyun kuyuda toplanıp çoğalması ya da bu suyun toplandığı yer anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Ölçü ve kapla kurulan kullanımlarda, içeriğin üst sınıra ulaşması veya dolmaya çok yaklaşması anlatılır."}],"identity_rationale":"Kaynak sözü, bir şeyin çoğalıp bir araya gelmesini ana çizgi olarak verir; bol malı, kuyuda biriken suyu ve ölçünün dolmaya yaklaşmasını bu çizginin gerçekleşmeleri olarak gösterir. Bu nedenle dalın çokluk, birikme ve doluluğu birlikte tutan çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"çoğalıp birikmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çok, bol"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"kuyuda biriken bol su"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kuyuda suyun toplandığı yer veya orada biriken su"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu veya kuyudaki su bolluğu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ölçeğin ağzına dek dolması veya dolmaya yaklaşması"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"içindeki ölçü ağzına kadar ulaşmış kap"}],"lexicalization_note":"Tanım, yalın çokluk ve birikme çekirdeğini korur; ölçü kabının ağzına dek dolması yalnızca verilen kalıplara bağlı bir gerçekleşme olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlanan üç karşılaştırma, genel birikme çekirdeğini dolma eylemi ve insan topluluğu alanından en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal çoğalma ile birikmeyi genel bir çekirdek olarak kurar; komşu dal ise tutulma, dönme ve belirli dolu ortamları öne çıkarır.","focus_only":"Bu dal, genel miktar çokluğunu ve ölçünün dolmaya yaklaşmasını da kapsar.","gloss":"birikme ve dolma","neighbor_only":"Komşu dal, suyun tutulup dönmesini, ağır bulutu ve aile ya da mal çokluğunu ayrıca kapsar.","neighbor_ref":"root_000377/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da suyun veya başka bir içeriğin bir yerde toplanıp doluluk oluşturması vardır."},{"boundary_match":"partial","distinction":"Odakta miktarın artıp birikmesi temelken komşuda belirli bir hazneyi dolduran geçişli eylem temeldir.","focus_only":"Odak dal kendiliğinden çoğalma, birikme ve doluluk durumunu anlatır.","gloss":"doluluk durumu ile doldurma","neighbor_only":"Komşu dal özellikle bir havuzu doldurma eylemini ve dolu havuzu anlatır.","neighbor_ref":"root_000642/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir kabın ya da haznenin dolu hale gelmesi çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak miktar ve doluluk bildirir; komşu ise bir araya gelen insanların oluşturduğu toplumsal bütünü adlandırır.","focus_only":"Odak dal insanla sınırlı olmayan miktar çokluğu, su birikimi ve doluluğu kapsar.","gloss":"çokluk ile topluluk","neighbor_only":"Komşu dal insan topluluklarını, topluca gelişleri ve boy örgütlenmelerini kapsar.","neighbor_ref":"root_000261/B003","relation_type":"near_neighbor","shared_zone":"Birçok öğenin bir araya gelerek büyük bir bütün oluşturması iki dalın ortak alanıdır."}],"source_phrase_ar":"كثرة الشيء واجتماعه (maqayis)؛ جم الشيء واستجم أي كثر (ayn;tahdhib)؛ جم المال وغيره إذا كثر والجم الكثير (sihah)؛ أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ (jamhara)؛ جمة الماء معظمه ومجتمعه (mufradat)","source_summary":"Aktarımlar ortak olarak çoğalma ve birikmeyi bildirir; bol miktarı, kuyuda toplanan çok suyu ve bir ölçünün üst sınırına varan doluluğu aynı dal içinde örnekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الكثرة العامة، والمال الجم، وامتلاء الإناء أو المكيال، واجتماع ماء البئر وكثرته.","what_is_not_ar":"لا يدخل فيه الجمام بمعنى الراحة، ولا الجماء بمعنى عدم القرن أو السلاح، ولا جمجمة الكلام."},"support_links":["sup_e0d2cb9d95b3280c98e3"]},{"boundary":"Buradaki çekirdek salt durgunluk değil, yorgunluğun giderilmesi ve gücün geri gelmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000261/B002","candidate_links":[{"candidate_id":"cand_b669b627254226f5a0db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"dinlenip gücünü yeniden toplama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dinlenme, yorgunluğu giderir ve tükenmiş gücün geri dönmesini sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At, bir süre binilmeden bırakılır; böylece yorgunluğu geçer ve gücünü yeniden toplar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiye kendisini bir veya birkaç gün dinlendirmesi söylenebilir."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yorgunluğun sona ermesi ile gücün geri kazanılması arasındaki ilişkiyi bütün dal için karşılar.","boundary_detail":"Buradaki çekirdek salt durgunluk değil, yorgunluğun giderilmesi ve gücün geri gelmesidir.","branch_image_ar":"جمام الراحة ورجوع القوة","concept_gloss":"dinlenip gücünü yeniden toplama","contextual_glosses":[{"applicability":"Kişi veya hayvanın bir çabanın ardından dinlenerek yeniden güçlenmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yorgunluktan dinlenmeye ve yeniden güçlenmeye uzanan süreci korur."},"facet_ids":["F001","F002"],"text":"yorgunluğunu atıp güç toplamak","usage_role":"contextual"},{"applicability":"Bir kimsenin kısa bir süre çalışmayı bırakıp dinlenmesi istendiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yöneltilen kısa süreli dinlenme isteğini korur."},"facet_ids":["F003"],"text":"kendini birkaç gün dinlendirmek","usage_role":"contextual"}],"definition":"Yorgunluğun dinlenmeyle giderilmesi ve harcanmış gücün yeniden toplanmasıdır. At için, bir süre binilmeyip dinlendirildikten sonra gücünün geri gelmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dinlenme, yorgunluğu giderir ve tükenmiş gücün geri dönmesini sağlar."},{"facet_id":"F002","role":"specialization","statement":"At, bir süre binilmeden bırakılır; böylece yorgunluğu geçer ve gücünü yeniden toplar."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişiye kendisini bir veya birkaç gün dinlendirmesi söylenebilir."}],"identity_rationale":"Kaynak sözü dinlenmeyi, yorgunluğun geçmesini ve kullanılmadan bırakılan atın gücünü yeniden toplamasını birlikte bildirir. Dalın dinlenme yoluyla güç yenileme çerçevesi bu aşama ilişkisini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dinlenme ve yorgunluğun geçmesi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"atın yorgunluğu geçmek veya güç toplaması için onu dinlendirmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kendini bir süre dinlendir"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"koşu gücünü her düşüşten sonra yeniden toplayan at"}],"lexicalization_note":"Tanım dinlenme ve güç toplama çekirdeğini verir; kişiyi dinlendirme buyruğu ile ata özgü kullanımlar kendi biçimlerine bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler dinlenme, ayılma ve yorgunluk kutupları arasındaki en yararlı sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dinlenmeyi gücün yenilenmesine bağlar; komşu dal ise daha genel bir dinlenme ve kolaylama alanına yayılır.","focus_only":"Odak dal, yorgunluk sonrası gücün geri toplanmasını ve atın dinlendirilmesini özellikle içerir.","gloss":"dinlenme ve toparlanma","neighbor_only":"Komşu dal dinlenmenin yanında kolaylık, soluklanma ve başka geniş kullanımları da içerir.","neighbor_ref":"root_000609/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda da yorgunluğun ardından dinlenme ve kişinin kendine gelmesi vardır."},{"boundary_match":"partial","distinction":"Odak dinlenmeye bağlı bedensel toparlanmadır; komşu bilinç ve sağlık bozukluğundan uyanma ya da iyileşmeyi de kapsar.","focus_only":"Odakta olağan yorgunluğun dinlenmeyle geçmesi ve gücün toplanması vardır.","gloss":"güç toplama ile ayılma","neighbor_only":"Komşuda bayılma, sarhoşluk, hastalık veya bilinç kaybından ayılma da vardır.","neighbor_ref":"root_001188/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da zayıflamış bir durumdan güce veya olağan hale geri dönüşü içerir."},{"boundary_match":"opposed","distinction":"Biri dinlenmeyle güç kazanmayı, öteki ise yorgunluk ve bezginliğin ağır basmasını bildirir.","focus_only":"Odak dal yorgunluğun giderildiği ve gücün geri geldiği kutbu anlatır.","gloss":"toparlanma ile bezginlik","neighbor_only":"Komşu dal bıkkınlık, bezginlik ve yorgunluğun sürdüğü ya da başkasına verildiği kutbu anlatır.","neighbor_ref":"root_000110/B002","relation_type":"polarity_pair","shared_zone":"İki dal da yorgunluk ve kişinin bir yük karşısındaki güç durumu eksenindedir."}],"source_phrase_ar":"الجمام الراحة (maqayis;ayn;sihah)؛ جم الفرس إذا ذهب إعياؤه (sihah;tahdhib)؛ جم الفرس وأجم إذا ترك أن يركب (maqayis)؛ أجمم نفسك يوما أو يومين (sihah;tahdhib)؛ أصل الكلمة من الجمام أي الراحة للإقامة وترك تحمل التعب (mufradat)","source_summary":"Aktarımlar dinlenme, yorgunluğun geçmesi ve gücün geri gelmesinde birleşir; hem kişinin kendisini dinlendirmesini hem de atın binilmeyerek güç toplamasını örnekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الجمام بمعنى الراحة، وذهاب الإعياء عن الفرس، وتركه حتى تثوب قوته، وإجمام النفس والقلب.","what_is_not_ar":"لا يدخل فيه مجرد الكثرة أو امتلاء المكيال، ولا انعدام القرن أو السلاح."},"support_links":["sup_1d76b90172560ca8ae8a"]},{"boundary":"Bu dal genel miktar çokluğunu değil, insanların topluluk olarak bir araya gelmesini ve örgütlenmesini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000261/B003","candidate_links":[{"candidate_id":"cand_05458f7947e967787ba4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"bir araya gelmiş kalabalık insan bütünü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlar eksiksiz ya da kalabalık biçimde bir araya gelerek bir topluluk oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir öldürme karşılığında ödenecek bedeli istemek üzere toplanan insan grubu anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birçok alt topluluğu birleştiren büyük boylar veya bu toplulukların önderleri anlatılır."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel kalabalığı, belli amaçla toplanan grubu ve alt grupları birleştiren büyük toplumsal bütünü karşılar.","boundary_detail":"Bu dal genel miktar çokluğunu değil, insanların topluluk olarak bir araya gelmesini ve örgütlenmesini anlatır.","branch_image_ar":"الجماعة المتراكمة والقبائل الجامعة","concept_gloss":"bir araya gelmiş kalabalık insan bütünü","contextual_glosses":[{"applicability":"Bir topluluğun geride kimse kalmadan veya büyük bir kalabalık halinde gelişi için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsanların kalabalık ve toplu biçimde gelişini korur."},"facet_ids":["F001"],"text":"hep birlikte gelen kalabalık","usage_role":"contextual"},{"applicability":"Birçok soy kolunu kendi çatısı altında toplayan büyük topluluk için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alt toplulukları birleştiren üst toplumsal bütün özelliğini korur."},"facet_ids":["F003"],"text":"alt boyları birleştiren büyük boy","usage_role":"contextual"}],"definition":"İnsanların kalabalık bir bütün halinde bir araya gelmesi veya daha küçük toplulukları birleştiren büyük bir toplumsal bütün oluşturmasıdır. Belirli bir bedeli istemek için toplanan grup ile büyük boylar ya da onların önderleri bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlar eksiksiz ya da kalabalık biçimde bir araya gelerek bir topluluk oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bir öldürme karşılığında ödenecek bedeli istemek üzere toplanan insan grubu anlatılır."},{"facet_id":"F003","role":"extension","statement":"Birçok alt topluluğu birleştiren büyük boylar veya bu toplulukların önderleri anlatılır."}],"identity_rationale":"Kaynak sözü topluca gelen insanları, bir ödeme istemek için bir araya gelen grubu ve alt toplulukları birleştiren büyük boyları ya da önderlerini açıkça aynı dalda verir. Dalın insan topluluğu ve birleştirici büyük toplumsal yapı çerçevesi bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"öldürme karşılığı ödenecek bedeli istemek için toplanan grup"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"geride kimse kalmadan gelen bütün kalabalık"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"alt boyları birleştiren büyük boylar veya onların önderleri"}],"lexicalization_note":"İnsan topluluğu çekirdeği korunur; herkesin birlikte gelişi ve büyük boyları anlatan kullanımlar yalnızca kendi kalıplarının sınırında açıklanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilen karşılaştırmalar kalabalık, eksiksiz toplu geliş ve soy temelli topluluk arasındaki sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal bütün topluluğun birlikte gelişiyle sınırlıyken odak dalın toplumsal örgütlenme ve amaçlı toplanma uzantıları da vardır.","focus_only":"Odak dal, belirli bir bedeli istemek için toplanan grubu ve büyük boy örgütlenmelerini de kapsar.","gloss":"bütün kalabalık","neighbor_only":"Komşu dal özellikle bir topluluğun bütün üyeleriyle ve kimse geri kalmadan gelişine bağlıdır.","neighbor_ref":"root_001096/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da insanların topluca, kalabalık ve eksiksiz biçimde bir araya gelişini anlatır."},{"boundary_match":"partial","distinction":"Odak dal toplanma ve birleştirici örgüt yapısını da taşır; komşu dalın çekirdeği ise doğrudan büyük insan sayısıdır.","focus_only":"Odak dal, kalabalığın yanında alt boyları birleştiren büyük toplumsal yapıyı ve önderleri içerir.","gloss":"çok sayıda insan topluluğu","neighbor_only":"Komşu dal sayıca çok ve ayrıntıları belirsiz halk kalabalığını öne çıkarır.","neighbor_ref":"root_000496/B002","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı sayıca çok insanın oluşturduğu kalabalık topluluktur."},{"boundary_match":"field_only","distinction":"Odakta kalabalık biçimde bir araya gelme veya birleştirici büyüklük vardır; komşuda belirleyici bağ ortak soydur.","focus_only":"Odak dal genel kalabalığı ve birçok alt boyu birleştiren büyük yapıları kapsar.","gloss":"topluluk ile soy topluluğu","neighbor_only":"Komşu dal soy bağıyla oluşan topluluğu, sayısı az ya da çok olsun, temel alır.","neighbor_ref":"root_000383/B010","relation_type":"same_field","shared_zone":"Her iki dal insan topluluklarını ve boy yapısını konu edinir."}],"source_phrase_ar":"الجمة القوم يسألون في الدية (maqayis;jamhara)؛ الجماء الغفير الجماعة من الناس (maqayis;ayn;sihah;mufradat)؛ جاءوا جما غفيرا وجماء أي بجماعتهم (tahdhib)؛ جماجم العرب القبائل التي تجمع البطون (maqayis;sihah)؛ جماجم العرب رؤساؤهم (tahdhib)","source_summary":"Aktarımlar kalabalık insan topluluğunu ortak çekirdek olarak verir; herkesin birlikte gelişini, belirli bir ödeme isteğiyle toplanmayı ve alt toplulukları birleştiren büyük boyları ya da önderleri bu çekirdeğe bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الجماء الغفير، والجماعة من الناس، والجمة التي تسأل في الدية، وجماجم العرب الجامعة للبطون أو رؤساؤها.","what_is_not_ar":"لا يدخل فيه جمة الشعر، ولا جمجمة الرأس، ولا كثرة المال إلا من جهة الجماعة."},"support_links":["sup_56d989c3579557b90075"]},{"boundary":"Saç kütlesi ile kafatası ayrı göndermelerdir; insan topluluğu ve anlaşılmaz konuşma bu dala girmez.","branch_kind":"bare","branch_ref":"root_000261/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"başta toplanmış saç ya da beyni saran kafatası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Baş üzerinde veya başı çevreleyerek bir bütün oluşturan bedensel yapı anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başta, özellikle alın üstünde bir araya gelmiş saç kütlesi anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Beyni içine alan kafatası ve ona bağlı baş kemikleri anlatılır."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın saç kütlesi ve kafatası olarak ayrılan iki bedensel göndermesini açıkça birlikte gösterir.","boundary_detail":"Saç kütlesi ile kafatası ayrı göndermelerdir; insan topluluğu ve anlaşılmaz konuşma bu dala girmez.","branch_image_ar":"مجتمع شعر الرأس وعظامه","concept_gloss":"başta toplanmış saç ya da beyni saran kafatası","contextual_glosses":[{"applicability":"Başta veya alın üstünde bir araya gelen saç kütlesi söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saçın başta toplu bir kütle oluşturmasını korur."},"facet_ids":["F002"],"text":"başta toplanmış uzun saç","usage_role":"contextual"},{"applicability":"Başın beyni içine alan kemiksi bütünü anlatıldığında doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kafatasının beyni içine alan baş kemiği olmasını korur."},"facet_ids":["F003"],"text":"beyni çevreleyen kafatası","usage_role":"contextual"}],"definition":"Başta bir araya gelmiş saç kütlesini veya beyni içine alıp çevreleyen kafatasını anlatır. Biri saçtan oluşan dış kümeyi, öteki başın kemiksi bütününü gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Baş üzerinde veya başı çevreleyerek bir bütün oluşturan bedensel yapı anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Başta, özellikle alın üstünde bir araya gelmiş saç kütlesi anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Beyni içine alan kafatası ve ona bağlı baş kemikleri anlatılır."}],"identity_rationale":"Kaynak sözü hem başta toplanmış saç kütlesini hem de beyni içine alan kafatasını açıkça bildirir. Dal bu iki bedensel göndermeyi birbirine karıştırmadan baş çevresindeki toplanmış veya kuşatıcı bütünler olarak koruyabilir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"başta toplanmış saç kütlesi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"baş saçı uzun adam"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kafatası ve ona bağlı baş kemikleri"}],"lexicalization_note":"Tanım yalnızca verilen yalın biçimlerin baş saçı ve kafatası anlamlarını kapsar; başka dallardaki kalıba bağlı anlamları buraya taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; saç tutamları ile beyin yaralanması alanları, dalın iki göndermesine en yakın ve en açıklayıcı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta saçın bir araya gelmiş bütünü vardır; komşuda tek tek saç tutamları ve onları düzenleme işi öne çıkar.","focus_only":"Odak dal baştaki saçın toplu kütlesini ve ayrıca kafatasını anlatır.","gloss":"saç kütlesi ile saç tutamları","neighbor_only":"Komşu dal saçın ayrı tutamlarını, yanağa uzanan bölümlerini ve saçı düzenleyen kişiyi kapsar.","neighbor_ref":"root_001420/B012","relation_type":"near_neighbor","shared_zone":"İki dal da baştaki saçın biçimlenmiş veya ayırt edilebilir bölümlerini konu edinir."},{"boundary_match":"field_only","distinction":"Odak bir baş yapısını adlandırır; komşu ise beyni ve ona ulaşan yaralanma olayını merkez alır.","focus_only":"Odak dal kafatasının kemiksi bütününü ve baştaki saç kütlesini adlandırır.","gloss":"kafatası ile beyin çevresi","neighbor_only":"Komşu dal beyni, ona ulaşan yarayı, yaralanan kişiyi ve başı ezen aracı kapsar.","neighbor_ref":"root_000053/B003","relation_type":"same_field","shared_zone":"Her iki dal baş, beyin ve onları çevreleyen yapıların bedensel alanındadır."}],"source_phrase_ar":"الجمة مجتمع شعر ناصيته (maqayis)؛ الجمة الشعر (ayn;jamhara;tahdhib)؛ الجمة بالضم مجتمع شعر الرأس (sihah)؛ ما اجتمع من شعر الناصية (mufradat)؛ الجمجمة عظم الرأس المشتمل على الدماغ (sihah)؛ الجمجمة القحف وما تعلق به من العظام (ayn;tahdhib)","source_summary":"Aktarımlar başta toplanan saçı ortak biçimde verir; ayrıca kafatasını, beyni içine alan ve bağlı kemikleriyle bir bütün oluşturan baş yapısı olarak açıklar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الجمة للشعر المجتمع على الرأس، والجمجمة للقحف أو عظم الرأس المشتمل على الدماغ.","what_is_not_ar":"لا يدخل فيه جماجم العرب القبلية، ولا جمجمة الكلام غير المبين."},"support_links":[]},{"boundary":"Her türlü bitki değil, toprağı örtecek ölçüde gelişmiş ama henüz tamamlanmamış genç bitki topluluğu anlatılır.","branch_kind":"bare","branch_ref":"root_000261/B005","candidate_links":[{"candidate_id":"cand_1e3635f4a00aae40f812","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"toprağı örten, henüz olgunlaşmamış genç bitki örtüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Genç bitki veya ot, toprağı örten toplu bir örtü oluşturur fakat henüz tam gelişmemiştir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki biraz boy atmış veya ürün vermeye yaklaşırken sıklaşıp bir araya gelmiştir."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin toplu oluşunu, yeri örtmesini, biraz büyümesini ve gelişiminin tamamlanmamış olmasını birlikte karşılar.","boundary_detail":"Her türlü bitki değil, toprağı örtecek ölçüde gelişmiş ama henüz tamamlanmamış genç bitki topluluğu anlatılır.","branch_image_ar":"الجميم من النبات الغاض المجتمع","concept_gloss":"toprağı örten, henüz olgunlaşmamış genç bitki örtüsü","contextual_glosses":[{"applicability":"Henüz olgunlaşmadan toprağın yüzünü örten ot veya bitki için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genç bitkinin yeri örten toplu görünümünü korur."},"facet_ids":["F001"],"text":"yeri kaplayan genç ot","usage_role":"contextual"},{"applicability":"Bitkinin ürün verme öncesinde sıklaşıp toplandığı gelişme aşamasında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ürün verme eşiğini ve bitkinin toplu biçimde sıklaşmasını korur."},"facet_ids":["F002"],"text":"ürün vermeye yaklaşan sık bitki","usage_role":"contextual"}],"definition":"Toprağı örtecek kadar bir araya gelip biraz boy atmış, ancak gelişimini henüz tamamlamamış genç bitki veya ot örtüsüdür. Ürün vermeye yaklaşırken sıklaşıp toplanan bitki de bu kapsamdadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Genç bitki veya ot, toprağı örten toplu bir örtü oluşturur fakat henüz tam gelişmemiştir."},{"facet_id":"F002","role":"specialization","statement":"Bitki biraz boy atmış veya ürün vermeye yaklaşırken sıklaşıp bir araya gelmiştir."}],"identity_rationale":"Kaynak sözü toprağı örten, biraz boy atmış fakat gelişimini tamamlamamış bitkiyi ve ürün verme eşiğinde toplanan otu bildirir. Dalın genç, sıklaşmış ve henüz olgunlaşmamış bitki örtüsü çerçevesi bu koşulların tümünü korur.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"toprağı örten, henüz tam gelişmemiş genç bitki veya ot"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"toprağın genç bitki örtüsü tamamlanmak veya bitki toplu bir baş oluşturmak"}],"lexicalization_note":"Tanım yalın bitki anlamıyla sınırlıdır; saç, insan topluluğu veya başka kalıplara bağlı toplanma anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler genç ve tamamlanmamış örtüyü genel yeşillik, yoğunluk ve ileri büyümeden ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü toplu halde yeri örtme ve tamamlanmamış gelişmedir; komşuda yeşillik tek başına yeterlidir.","focus_only":"Odak dal bitkinin toprağı örtmesini ve henüz gelişimini tamamlamamış olmasını şart koşar.","gloss":"genç bitki örtüsü","neighbor_only":"Komşu dal yeşil ve körpe bitkiyi, ekini ve ilkbaharda çıkan yeşilliği daha geniş biçimde kapsar.","neighbor_ref":"root_000418/B002","relation_type":"near_synonym","shared_zone":"İki dal da taze, yeşil ve henüz sertleşmemiş bitki büyümesini anlatır."},{"boundary_match":"partial","distinction":"Odak belirli bir genç gelişme aşamasıdır; komşu ise yaşına bakmadan bitki yoğunluğunu öne çıkarır.","focus_only":"Odak dal gençlik, kısmi boylanma ve henüz olgunlaşmama aşamasını içerir.","gloss":"sık bitki topluluğu","neighbor_only":"Komşu dal bitkinin veya ağacın çok ve sık oluşunu, gelişme aşamasından bağımsız olarak anlatır.","neighbor_ref":"root_000798/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bitkinin yeryüzünde sık ve toplu bir görünüm oluşturması vardır."},{"boundary_match":"partial","distinction":"Odak erken ve tamamlanmamış örtü aşamasında kalır; komşu daha güçlü, uzun, dolanmış veya çiçeklenmiş büyümeye uzanır.","focus_only":"Odakta toprağı örten fakat gelişimini henüz tamamlamamış bitki vardır.","gloss":"genç örtü ile ileri büyüme","neighbor_only":"Komşuda bitkinin güçlenmesi, uzaması, birbirine dolanması veya çiçek açması gibi ileri gelişme durumları vardır.","neighbor_ref":"root_000266/B011","relation_type":"near_neighbor","shared_zone":"İki dal bitkinin toplu büyümesini ve gelişme sürecindeki görünümünü konu edinir."}],"source_phrase_ar":"الجميم مجتمع من البهمى (maqayis)؛ الجميم النبات إذا تخطى الأرض (ayn)؛ الجميم ما تجمم من البقل إذا أراد أن يثمر (jamhara)؛ الجميم النبت الذي طال بعض الطول ولم يتم (sihah)؛ جميم حسن لنبت قد غطى الأرض ولم يتم بعد (tahdhib)","source_summary":"Aktarımlar toprağı örten ve henüz gelişimini tamamlamamış bitkiyi ortaklaştırır; biraz boy atma, sıklaşma ve ürün verme eşiğine gelme ayrıntıları bu genç örtünün aşamalarını belirtir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الجميم للنبات أو البقل الذي غطى الأرض أو طال بعض الطول ولم يتم، وما تجمع منه عند إرادة الإثمار.","what_is_not_ar":"لا يدخل فيه جمة الشعر ولا جماعة الناس، وإن اشتركت في صورة الاجتماع."},"support_links":["sup_30532e533a0ec594e9ed"]},{"boundary":"Yokluk, her türlü eksiklik değil; verilen varlıkta beklenen mızrak, boynuz, mazgal veya bedensel çıkıntının bulunmamasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000261/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"beklenen araçtan veya çıkıntıdan yoksun olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beklenen bir savunma aracı veya dışarı doğru çıkan belirgin bölüm bulunmaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaşçı mızraksız, koyun boynuzsuz veya yapı duvar üstündeki mazgallardan yoksundur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kadının dirseklerinin dışarı doğru belirgin biçimde çıkmaması da aynı yokluk görüntüsüyle anlatılır."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mızrak, boynuz, yapı üstü mazgal ve bedensel çıkıntı yokluğunu tek ortak sınır altında karşılar.","boundary_detail":"Yokluk, her türlü eksiklik değil; verilen varlıkta beklenen mızrak, boynuz, mazgal veya bedensel çıkıntının bulunmamasıdır.","branch_image_ar":"الأجم والجماء بلا ناتئ أو سلاح","concept_gloss":"beklenen araçtan veya çıkıntıdan yoksun olma","contextual_glosses":[{"applicability":"Savaş alanında yanında mızrağı bulunmayan kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin beklenen savaş aracından yoksun oluşunu korur."},"facet_ids":["F001","F002"],"text":"mızraksız savaşçı","usage_role":"contextual"},{"applicability":"Koyunda beklenen boynuzun bulunmadığı hayvan betimlemesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvandaki belirgin çıkıntının bulunmamasını korur."},"facet_ids":["F001","F002"],"text":"boynuzsuz koyun","usage_role":"contextual"},{"applicability":"Duvarlarının üstünde çıkıntılı mazgal veya diş bulunmayan yapı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapıdaki üst çıkıntıların yokluğunu korur."},"facet_ids":["F001","F002"],"text":"üstü mazgalsız yapı","usage_role":"contextual"}],"definition":"Bir kişi ya da nesnede beklenen savunma aracının, boynuzun veya belirgin çıkıntının bulunmamasıdır. Savaşçının mızraksız, koyunun boynuzsuz, yapının mazgalsız ve dirseklerin çıkıntısız oluşunda gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beklenen bir savunma aracı veya dışarı doğru çıkan belirgin bölüm bulunmaz."},{"facet_id":"F002","role":"specialization","statement":"Savaşçı mızraksız, koyun boynuzsuz veya yapı duvar üstündeki mazgallardan yoksundur."},{"facet_id":"F003","role":"extension","statement":"Bir kadının dirseklerinin dışarı doğru belirgin biçimde çıkmaması da aynı yokluk görüntüsüyle anlatılır."}],"identity_rationale":"Kaynak sözü savaşta mızrağı olmayan kişiyi, boynuzu olmayan koyunu, mazgalsız yapıyı ve dirsekleri çıkıntısız kadını birlikte verir. Ortak sınır, beklenen bir araç ya da belirgin çıkıntının bulunmamasıdır; dal çerçevesi bunu doğru biçimde yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"savaşta yanında mızrağı olmayan kişi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"boynuzsuz koyun"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"duvarlarının üstünde mazgal bulunmayan yapı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dirsekleri dışarı doğru çıkıntı yapmayan kadın"}],"lexicalization_note":"Araç veya çıkıntı yoksunluğu ortak çekirdektir; koyun, yapı ve dirsek anlamları yalnızca verilen ad tamlamalarıyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler çıkıntı yokluğunu çıkıntının varlığı, silahın kendisi ve yüzey örtüsü yokluğundan ayırır.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak beklenen çıkıntının yok olduğu kutuptur; komşu ise çıkıntının güçlü ve görünür biçimde bulunduğu kutuptur.","focus_only":"Odak dal boynuzun veya başka belirgin bir çıkıntının bulunmamasını anlatır.","gloss":"çıkıntısızlık ile belirgin çıkıntı","neighbor_only":"Komşu dal boynuzu ve ona benzetilen güçlü, sivri ya da dışarı taşan bölümleri anlatır.","neighbor_ref":"root_001221/B006","relation_type":"polarity_pair","shared_zone":"İki dal hayvan başındaki boynuz ve ona benzeyen dışa taşkın biçimler eksenindedir."},{"boundary_match":"partial","distinction":"Odak kişide aracın yokluğunu yüklem yapar; komşu ise var olan silahı ve onun sivri bölümünü adlandırır.","focus_only":"Odak dal savaşçının mızraktan yoksun oluşunu ve başka çıkıntı yokluklarını anlatır.","gloss":"mızraksız kişi ile mızrak","neighbor_only":"Komşu dal mızrağın kendisini ve sivri ucunu adlandırır.","neighbor_ref":"root_000302/B004","relation_type":"near_neighbor","shared_zone":"İki dal savaş sahnesinde mızrağın bulunması ya da bulunmaması çevresinde ilişkilidir."},{"boundary_match":"field_only","distinction":"Odakta dışarı taşan parça veya araç yoktur; komşuda yüzeyi örten kıl azalır ya da bütünüyle kaybolur.","focus_only":"Odak dal boynuz, mızrak, mazgal veya dirsek çıkıntısının yokluğuna bağlıdır.","gloss":"çıkıntısızlık ile kılsızlık","neighbor_only":"Komşu dal insan ya da hayvan bedeninde kılın azlığı veya yokluğu ile yüzeyin düzgünlüğünü anlatır.","neighbor_ref":"root_000234/B003","relation_type":"same_field","shared_zone":"Her iki dal bir varlığın olağan dış görünüş öğelerinden birinin bulunmamasını konu edinir."}],"source_phrase_ar":"الأجم الذي لا رمح معه في الحرب (maqayis;ayn;sihah;tahdhib)؛ الشاة الجماء التي لا قرن لها (maqayis;ayn;sihah;tahdhib;mufradat)؛ بنيان أجم لا شرف له (sihah)؛ المساجد جما أي لا يكون لجدرانها شرف (maqayis;tahdhib)؛ امرأة جماء المرافق (sihah)","source_summary":"Aktarımlar beklenen araç veya çıkıntının yokluğunda birleşir; mızraksız savaşçı, boynuzsuz koyun, mazgalsız yapı ve çıkıntısız dirsek bu ortak görünümün ayrı uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأجم الذي لا رمح معه، والشاة الجماء التي لا قرن لها، والبناء أو المسجد الجم بلا شرفات، وما يشبه ذلك من ذهاب الناتئ أو الآلة.","what_is_not_ar":"لا يدخل فيه الكثرة والاجتماع، ولا الراحة، ولا الجمة بمعنى الشعر إلا عند من يعلل الشاة الجماء باعتبار جمة الناصية."},"support_links":[]},{"boundary":"Mekânsal doluluk değil, bir olayın veya gereksinimin zaman bakımından yaklaşması ve gerçekleşme vaktinin gelmesi anlatılır.","branch_kind":"mixed_non_bare","branch_ref":"root_000261/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"yaklaşıp vakti gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey zaman bakımından yaklaşır, hazır hale gelir veya gerçekleşme vakti gelir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işin, gereksinimin, ayrılığın veya bir kişinin gelişinin yaklaşması bu zaman ilişkisini örnekler."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir olay veya gereksinimin zaman bakımından yakınlaşmasını ve gerçekleşme eşiğine varmasını karşılar.","boundary_detail":"Mekânsal doluluk değil, bir olayın veya gereksinimin zaman bakımından yaklaşması ve gerçekleşme vaktinin gelmesi anlatılır.","branch_image_ar":"دنو الأمر وحينه","concept_gloss":"yaklaşıp vakti gelmek","contextual_glosses":[{"applicability":"Bir iş veya gereksinim artık yakın ve yapılmaya hazır olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşin yaklaşmasını ve gerçekleşme zamanının gelmesini korur."},"facet_ids":["F001","F002"],"text":"işin vakti gelip çatmak","usage_role":"contextual"},{"applicability":"Bir kişinin gelmesine az zaman kaldığını anlatan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geliş olayının zaman bakımından yakınlaşmasını korur."},"facet_ids":["F002"],"text":"gelişi yaklaşmak","usage_role":"contextual"}],"definition":"Bir olayın, gereksinimin, ayrılığın ya da gelişin zaman bakımından yaklaşması ve gerçekleşme vaktinin gelip çatmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey zaman bakımından yaklaşır, hazır hale gelir veya gerçekleşme vakti gelir."},{"facet_id":"F002","role":"example","statement":"Bir işin, gereksinimin, ayrılığın veya bir kişinin gelişinin yaklaşması bu zaman ilişkisini örnekler."}],"identity_rationale":"Kaynak sözü bir şeyin, gereksinimin, işin veya ayrılığın yaklaşmasını; ayrıca vaktinin gelmesini bildirir. Dalın yaklaşma, hazır bulunma ve zamanın gelip çatması çerçevesi bu ortak zaman ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"iş yaklaşmak, hazır olmak veya vakti gelmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"birinin gelişi yaklaşmak ve vakti gelmek"}],"lexicalization_note":"Zamansal yaklaşma çekirdeği korunur; iş, gereksinim, ayrılık ve bir kişinin gelişi yalnızca verildikleri biçimlerde örneklenir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen dal ile daha geniş yakınlık ve zaman gelişimi dalları yayımlanarak sınır açıklaştırıldı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında çekirdek, koşul ve zaman sınırı bakımından anlamlı bir ayrım görünmez.","focus_only":null,"gloss":"bir işin yaklaşıp vaktinin gelmesi","neighbor_only":null,"neighbor_ref":"root_000001/B006","relation_type":"synonym","shared_zone":"Her iki dal da işin veya gereksinimin yaklaşmasını, hazır bulunmasını ve zamanının gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak olay zamanının gelip çatmasına yönelir; komşu ise hem genel yakınlığı hem de yakınlıktan doğan zaman darlığını içerir.","focus_only":"Odak dal özellikle olay, gereksinim, ayrılık veya gelişin vaktinin gelmesine bağlıdır.","gloss":"yaklaşma ve vaktin gelmesi","neighbor_only":"Komşu dal nesnelerin genel yakınlığını ve zaman darlığını daha geniş biçimde kapsar.","neighbor_ref":"root_000029/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin yakınlaşmasını ve zaman bakımından gerçekleşme eşiğine gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak yalnızca yaklaşma ve vaktin gelmesinde kalır; komşu yaklaşmayı tamamlanma, batış, yenilik ve geçip gitmeyle genişletir.","focus_only":"Odak dal yaklaşan olayın veya gereksinimin gerçekleşme vaktini temel alır.","gloss":"zamanın yaklaşması","neighbor_only":"Komşu dal ürünün olgunlaşması, güneşin batışı, yenilik ve geride kalıp gitme gibi ek yönleri kapsar.","neighbor_ref":"root_001212/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir zamanın, söz verilen olayın veya sonucun yaklaşması vardır."}],"source_phrase_ar":"أجم الشيء دنا (maqayis)؛ أجمت الحاجة أي دنت وحاجت (ayn)؛ أجم الأمر إذا دنا وحضر وأجم الفراق إذا حان (sihah)؛ أجمت الحاجة إذا دنت وحانت وأجم الفراق إذا دنا (tahdhib)","source_summary":"Aktarımlar bir şeyin zaman bakımından yaklaşması ve vaktinin gelmesinde birleşir; iş, gereksinim, ayrılık ve geliş bu ortak ilişkinin örnekleridir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه أجم الأمر أو الحاجة أو الفراق أو القدوم إذا دنا وحضر أو حان وقته.","what_is_not_ar":"لا يدخل فيه الامتلاء المكاني ولا الراحة، إلا من جهة المصدر الذي ألحقه بالباب العام."},"support_links":[]},{"boundary":"Çekirdek sözün açık edilmemesidir; bunun bedensel konuşma güçlüğünden doğduğu ya da doğmadığı kesin bir koşul sayılamaz.","branch_kind":"bare","branch_ref":"root_000261/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"sözü açık ve anlaşılır biçimde söylememe","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşan kişi sözünü açıkça ayırıp anlaşılır biçimde dile getirmez."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirsiz söyleyişin konuşma güçlüğünden doğup doğmadığı konusunda aktarımlar birbiriyle uyuşmaz."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirsiz konuşma davranışını karşılar ve kaynağı konusunda kanıtın taşımadığı bir neden ileri sürmez.","boundary_detail":"Çekirdek sözün açık edilmemesidir; bunun bedensel konuşma güçlüğünden doğduğu ya da doğmadığı kesin bir koşul sayılamaz.","branch_image_ar":"جمجمة الكلام بلا بيان","concept_gloss":"sözü açık ve anlaşılır biçimde söylememe","contextual_glosses":[{"applicability":"Kişinin sözünü açıkça söylemeyip dinleyenin anlamasını güçleştirdiği bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözün açık seçik ortaya konmamasını korur."},"facet_ids":["F001"],"text":"sözü ağzında gevelemek","usage_role":"contextual"},{"applicability":"Söyleyişin nedeni belirtilmeden yalnızca sözün anlaşılmadığı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmanın anlaşılır olmaması çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"anlaşılmaz konuşmak","usage_role":"general"}],"definition":"Konuşanın söylemek istediğini açık ve anlaşılır biçimde ortaya koymaması ya da koyamamasıdır. Kaynaklar bunun konuşma güçlüğüyle ilişkisi konusunda ayrıldığı için neden tanımın parçası yapılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşan kişi sözünü açıkça ayırıp anlaşılır biçimde dile getirmez."},{"facet_id":"F002","role":"source_variant","statement":"Belirsiz söyleyişin konuşma güçlüğünden doğup doğmadığı konusunda aktarımlar birbiriyle uyuşmaz."}],"identity_rationale":"Kaynak sözü konuşanın sözünü açık seçik ortaya koymamasında birleşir, ancak bunun konuşma güçlüğünden kaynaklanıp kaynaklanmadığı konusunda karşıt kayıtlar içerir. Dal korunabilir; tanım nedeni kesinleştirmeden yalnızca anlaşılır söyleyişin gerçekleşmemesini bildirmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"sözünü açık söylememek veya anlaşılmaz konuşmak"}],"lexicalization_note":"Tanım yalın konuşma eyleminin belirsizliğini verir; kafatası veya baş saçı anlamları ve başka kalıplar bu dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yayımlananlar belirsiz söyleyişi sessiz ağız hareketinden, dil tutulmasından ve açık anlatım kutbundan ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta anlaşılmaz bir söyleyiş bulunabilir; komşuda konuşma hareketi yapılmasına rağmen belirli bir söz veya ses hiç oluşmayabilir.","focus_only":"Odak dal, söylenen sözün açık ve anlaşılır olmamasını bildirir.","gloss":"geveleme ile sessiz ağız hareketi","neighbor_only":"Komşu dal ağız veya dudakların konuşmak için hareket etmesine karşın açık bir sözün, hatta bir sesin çıkmamasını kapsar.","neighbor_ref":"root_000601/B008","relation_type":"near_synonym","shared_zone":"Her iki dalda da kişi konuşmaya yönelir fakat açık bir söz ortaya çıkmaz."},{"boundary_match":"partial","distinction":"Odak genel bir açık söylememe davranışıdır; komşu ise dil tutulması ya da sözün yapısal karmaşıklığına dayanır.","focus_only":"Odak dal nedenini kesinleştirmeden sözün açık edilmemesini anlatır.","gloss":"anlaşılmaz söyleyiş","neighbor_only":"Komşu dal dilde tutulmayı ve sözün düğümlü, çözülmesi güç yapısını özellikle kapsar.","neighbor_ref":"root_001034/B007","relation_type":"near_synonym","shared_zone":"İki dal da konuşmanın açıkça ayrıştırılamaması ve dinleyenin anlamakta zorlanması alanında buluşur."},{"boundary_match":"opposed","distinction":"Odakta açıklık başarısız olur; komşuda dil, açıklığı ve ayrımı sağlayan olumlu kutuptur.","focus_only":"Odak dal sözün açık ve ayırt edilir biçimde ortaya çıkmadığı kutbu anlatır.","gloss":"belirsiz söyleyiş ile açık anlatım","neighbor_only":"Komşu dal dili, sözleri açığa çıkarıp konuları birbirinden ayıran anlatım aracı olarak verir.","neighbor_ref":"root_001159/B004","relation_type":"polarity_pair","shared_zone":"İki dal konuşmanın açıklığı ve sözlerin birbirinden ayırt edilebilirliği eksenindedir."}],"source_phrase_ar":"الجمجمة ألا تبين كلامك من غير عي (ayn)؛ جمجم الرجل وتجمجم إذا لم يبين كلامه (sihah)؛ الجمجمة ألا تبين كلامك من عي (tahdhib)","source_summary":"Aktarımlar sözün açık ve anlaşılır biçimde söylenmemesinde birleşir; bir bölüm bunu konuşma güçlüğünden bağımsız gösterirken bir bölüm konuşma güçlüğüne bağlar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه جمجم الرجل أو تجمجم إذا لم يبين كلامه.","what_is_not_ar":"لا يدخل فيه الجمجمة بمعنى القحف، ولا الجمة بمعنى الشعر."},"support_links":[]},{"boundary":"Bu anlam yalnızca verilen genişlik ve darlık ifadelerine bağlıdır; kökün genel ve yalın bir genişlik anlamı sayılmaz.","branch_kind":"collocation","branch_ref":"root_000261/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","surface_ar":"جَمًّا"}],"gloss":"göğsü geniş ve kolu açık olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli niteleme kalıpları kişiyi göğsü geniş ve kolu açık olarak betimler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşıt niteleme aynı ölçüyü göğüs darlığı yönünde kurar."}}],"root_ar":"ج م م","root_id":"root_000261","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen kişi nitelemelerinde geniş göğüs ile açık kol görünümünü ve bunun dar karşıtını temsil eder.","boundary_detail":"Bu anlam yalnızca verilen genişlik ve darlık ifadelerine bağlıdır; kökün genel ve yalın bir genişlik anlamı sayılmaz.","branch_image_ar":"رحابة المجم في الصدر","concept_gloss":"göğsü geniş ve kolu açık olma","contextual_glosses":[{"applicability":"Geniş biçimin kişiyi açık ve rahat bir duruşla nitelediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğüs açıklığını ve kol rahatlığını doğal Türkçe bir kişi nitelemesiyle korur."},"facet_ids":["F001"],"text":"göğsü geniş, eli kolu rahat","usage_role":"contextual"},{"applicability":"Verilen karşıt nitelemede kişinin göğüs darlığını belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Genişlik ölçüsünün dar karşıtını doğrudan korur."},"facet_ids":["F002"],"text":"göğsü dar","usage_role":"contextual"}],"definition":"Verilen niteleme kalıplarında bir kişinin göğsünün geniş ve kolunun açık, karşıt kalıpta ise göğsünün dar oluşudur. Geniş biçim bedensel açıklıkla birlikte rahat ve açık bir tutumu da sezdirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli niteleme kalıpları kişiyi göğsü geniş ve kolu açık olarak betimler."},{"facet_id":"F002","role":"specialization","statement":"Karşıt niteleme aynı ölçüyü göğüs darlığı yönünde kurar."}],"identity_rationale":"Kaynak sözü bir kişiyi göğsü geniş ve kolu açık diye niteleyen iki yakın ifadeyi, karşıt olarak da göğüs darlığını verir. Dalın bedensel genişlikten kişinin rahat ve geniş tutumuna uzanan karşıtlıklı çerçevesi, verilen ifadelerin sınırında tutulduğunda kaynağa uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"göğsü geniş, eli kolu rahat"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"göğsü dar"}],"lexicalization_note":"Tanım yalnızca göğüs genişliği veya darlığı bildiren verilen kalıplara bağlıdır; buradan yalın köke genel bir genişlik anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; seçilenler kalıba bağlı kişi nitelemesini yakın göğüs ölçüsünden ve genel mekânsal genişlikten ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır; ancak odak kol açıklığını taşır ve her dal farklı, kendi başına sınırlı bir niteleme kalıbında sözlükselleşir.","focus_only":"Odak dal kendi iki genişlik ve darlık nitelemesine ve kol açıklığı ayrıntısına bağlıdır.","gloss":"göğüs genişliği ve darlığı","neighbor_only":"Komşu dal başka bir niteleme kalıbıyla göğüs genişliğini kişinin hareket alanının genişliğiyle birlikte verir.","neighbor_ref":"root_000246/B005","relation_type":"near_synonym","shared_zone":"Her iki dal kişi için göğüs genişliği ile darlığını karşıt bir ölçü olarak kullanır."},{"boundary_match":"partial","distinction":"Odak belirli kişi nitelemelerinin dar sözlüksel alanındadır; komşu fiziksel mekândan izne kadar uzanan genel bir genişleme çekirdeğidir.","focus_only":"Odak dal yalnızca kişiyi göğüs ve kol genişliğiyle niteleyen belirli kalıplara bağlıdır.","gloss":"göğüs açıklığı ile genel genişlik","neighbor_only":"Komşu dal yer, ev, toplantı alanı, izin, göğüs ferahlığı ve iki şeyin arasını açma gibi genel genişlemeleri kapsar.","neighbor_ref":"root_001153/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da genişlik, kişide açıklık ve rahatlık düşüncesine uzanabilir."},{"boundary_match":"field_only","distinction":"Odak kişinin göğüs ve koluna bağlı bir nitelemedir; komşunun çekirdeği ise doğrudan fiziksel mekân genişliğidir.","focus_only":"Odak dal kişide göğüs ve kol genişliğiyle kurulan sınırlı bir nitelemedir.","gloss":"kişide açıklık ile mekânda genişlik","neighbor_only":"Komşu dal ev, arazi, ülke ve açık alanların fiziksel genişliğini anlatır.","neighbor_ref":"root_000549/B001","relation_type":"same_field","shared_zone":"Her iki dal genişlik ve ferahlık düşüncesini taşır."}],"source_phrase_ar":"رجل رحب المجم أي رحب الصدر (jamhara)؛ فلان واسع المجم إذا كان واسع الصدر رحب الذراع (tahdhib)؛ ضيق المجم (tahdhib)","source_summary":"Aktarımlar geniş biçimi göğüs açıklığı ve kol genişliğiyle açıklar; ayrıca aynı nitelemenin dar karşıtını da kaydeder.","sources":["JA","TA"],"what_is_ar":"يدخل فيه رحب المجم أو واسع المجم بمعنى واسع الصدر ورحب الذراع، وضده ضيق المجم.","what_is_not_ar":"لا يدخل فيه جمام المكيال ولا جماعة الناس."},"support_links":[]},{"boundary":"Temel anlam yenebilir ya da ekilebilir tane ve tohumdur; parça, dolu ve küpe kullanımları benzer biçime dayalı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B001","candidate_links":[{"candidate_id":"cand_1e3635f4a00aae40f812","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"tane, tohum ve taneye benzeyen tek parça","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tahıl, baklagil ve kokulu bitkilerde yenebilen veya ekilebilen tane ya da tohum."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tane veya bir şeyin taneye benzeyen tek parçası."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Biçim benzerliğiyle dolu tanesine ve tek taneli küpeye verilen ad."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkisel çekirdeği ve kaynak ifadesindeki biçimsel uzantıları birlikte temsil eden üst düzey karşılıktır.","boundary_detail":"Temel anlam yenebilir ya da ekilebilir tane ve tohumdur; parça, dolu ve küpe kullanımları benzer biçime dayalı uzantılardır.","branch_image_ar":"الحبة التي تنبت وتحمل الحب","concept_gloss":"tane, tohum ve taneye benzeyen tek parça","contextual_glosses":[{"applicability":"Bu karşılık buğday, arpa ve benzeri yenebilir ürünlerden söz edilen bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Diğer bitki tohumlarını, genel tek parçayı, doluyu ve küpe uzantısını dışarıda bırakır.","preserves":"Yenebilir tahıl tanesi anlamını açık biçimde korur."},"facet_ids":["F001"],"text":"tahıl tanesi","usage_role":"contextual"}],"definition":"Tahılın, baklagilin veya kokulu bitkinin ekilebilen ya da yenebilen tanesi ve bunun tek birimidir. Taneye benzetilen parça, dolu tanesi ve tek taneli küpe bu çekirdeğe bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tahıl, baklagil ve kokulu bitkilerde yenebilen veya ekilebilen tane ya da tohum."},{"facet_id":"F002","role":"specialization","statement":"Bir tane veya bir şeyin taneye benzeyen tek parçası."},{"facet_id":"F003","role":"extension","statement":"Biçim benzerliğiyle dolu tanesine ve tek taneli küpeye verilen ad."}],"identity_rationale":"Kaynak ifadesi tahıl ve bitki tanelerini temel alırken tek taneyi, taneye benzeyen parçayı, dolu tanesini ve tek taneli küpeyi de aynı kayıtta toplar. Dal korunabilir, ancak benzetmeye dayalı kullanımlar temel bitkisel anlamla özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tahıl tanesi ve yenebilir bitki tohumu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tek tane, tohum veya taneye benzeyen parça"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"dolu tanesi"}],"lexicalization_note":"Dal yalın tane biçimleriyle birlikte doluya özgü bir söz öbeği içerir; söz öbeğinin anlamı genel tane anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli bir bitki tanesiyle genel tane arasındaki sınırı en iyi gösteren karşılaştırma yayımlandı, yalnızca konu veya kök biçimi paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal biçim ve birim bakımından genel bir tane kavramıdır; komşu ise belirli bir bitki türüne ve onun tanesine bağlıdır, bu yüzden olağan kullanımda birbirlerinin yerine geçmezler.","focus_only":"Odak dal bütün tahıl ve bitki tanelerini, ayrıca taneye benzeyen parçaları kapsar.","gloss":"genel tane ile hardal tanesi","neighbor_only":"Komşu dal özellikle hardal bitkisini ve onun tek tanesini adlandırır.","neighbor_ref":"root_000401/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da ekilebilir küçük bir bitki tanesini kapsar."}],"source_phrase_ar":"الحبة واحد الحب (jamhara;sihah)؛ الحب والحبة في الحنطة والشعير وبزور الرياحين (maqayis;tahdhib;mufradat)؛ الحبة من الشيء القطعة منه وحب الغمام وحب المزن وحب قر والحب القرط من حبة واحدة (sihah;tahdhib)","source_summary":"Ortak kayıt, bitkisel taneyi ve tek taneyi merkez alır; parça, dolu ve tek taneli küpe kullanımlarını biçim benzerliğine bağlı olarak ekler.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحب والحبة للحنطة والشعير والبقول والرياحين، والحبة الواحدة، وما شبه بها كالقطعة والبرد والقرط من حبة.","what_is_not_ar":"ليس المحبة ولا حبذا ولا حباب الماء ولا حبة القلب إذا أريد سويداء القلب."},"support_links":["sup_30532e533a0ec594e9ed"]},{"boundary":"Dal sevgi duygusunu, sevme eylemini ve bir şeyi başkasına yeğlemeyi kapsar; tahıl tanesi veya övgü kalıbı anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000286/B002","candidate_links":[{"candidate_id":"cand_2e44a647ba80a0a1b00c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"sevgi ve yeğleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye veya şeye yönelen sevgi ve olumlu bağlılık; nefretin karşıtı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyi olduğu görülen veya sanılan şeyi güçlü biçimde isteme."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sevilen veya istenen bir şeyi başka bir seçeneğe üstün tutma."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duygusal bağlılık çekirdeği ile seçimde üstün tutma uzantısını birlikte karşılayan kısa ifadedir.","boundary_detail":"Dal sevgi duygusunu, sevme eylemini ve bir şeyi başkasına yeğlemeyi kapsar; tahıl tanesi veya övgü kalıbı anlamlarını kapsamaz.","branch_image_ar":"المحبة الملازمة للقلب","concept_gloss":"sevgi ve yeğleme","contextual_glosses":[{"applicability":"Bir kişiye veya şeye duyulan olumlu bağlılığın öne çıktığı genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi başka bir şeye bilinçli olarak yeğleme uzantısını açıkça vermez.","preserves":"Duygusal bağlılık ve nefretin karşıtı olma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"sevgi","usage_role":"general"}],"definition":"Bir kişiyi veya iyi görülen bir şeyi gönülden isteme ve ona olumlu bağlanma duygusudur; nefretin karşıtıdır. Bu yönelim, bir şeyi başka bir şeye yeğleme biçiminde seçime de dönüşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye veya şeye yönelen sevgi ve olumlu bağlılık; nefretin karşıtı."},{"facet_id":"F002","role":"specialization","statement":"İyi olduğu görülen veya sanılan şeyi güçlü biçimde isteme."},{"facet_id":"F003","role":"extension","statement":"Sevilen veya istenen bir şeyi başka bir seçeneğe üstün tutma."}],"identity_rationale":"Kaynak ifadesi sevgiyi nefretin karşıtı olarak verir, onu iyi görülen şeye yönelen güçlü istekle açıklar ve yeğleme kullanımını ayrıca belirtir. Sağlanan dal çerçevesi bu duygusal ve seçimsel alanı doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sevgi; nefretin karşıtı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"iyi görülen şeye yönelen güçlü sevgi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sevmek veya sevdirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeğlemek veya sevmeye yönelmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"birbirini sevmek"}],"lexicalization_note":"Dal yalın kök anlamını verir; taneye, övgü kalıbına veya başka özel söz öbeklerine ait anlamlar tanıma taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sevgi çekirdeğine en yakın komşu yayımlandı. Arzu, düşmanlık, kur yapma ve aynı kökün diğer anlamları ikame sağlamadığı için alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Duygusal çekirdekte büyük ölçüde örtüşürler; odak dal seçimsel yeğlemeye uzanırken komşu dal karşılıklı yakınlık ve ilişki boyutunu daha geniş tuttuğu için sınırları tam değildir.","focus_only":"Odak dal iyi görülene yönelen isteği ve bir seçeneği ötekine yeğlemeyi açıkça kapsar.","gloss":"sevgi ile gönül yakınlığı","neighbor_only":"Komşu dal karşılıklı yakınlık, sevgi gösterisi ve sevginin doğmasına yol açan ilişkileri daha belirgin kapsar.","neighbor_ref":"root_001634/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı kişiye veya şeye duyulan olumlu bağlılık ve sevgidir."}],"source_phrase_ar":"الحب والمحبة اشتقاقه من أحبه إذا لزمه (maqayis)؛ أحببته نقيض أبغضته (ayn)؛ المحبة إرادة ما تراه أو تظنه خيرا (mufradat)؛ استحبوا أي آثروه عليه (mufradat)","source_summary":"Ortak kayıt sevgiyi nefretin karşıtı ve iyi görülene yönelen güçlü istek olarak kurar; aynı yönelimin seçimde yeğleme anlamı kazandığını da belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحب والمحبة ونقيض البغض، والتحبيب، والمحبوب، والاستحباب بمعنى الإيثار، والمودة المتبادلة.","what_is_not_ar":"ليس الحب بمعنى الحبوب، ولا حبذا وصيغ المدح، ولا لزوم البعير مكانه إلا من جهة الأصل اللغوي."},"support_links":["sup_e0d2cb9d95b3280c98e3"]},{"boundary":"Bu dal genel sevgi duygusunu değil, övgü, en güçlü istek veya nazik kabul bildiren belirli kalıpları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B003","candidate_links":[{"candidate_id":"cand_05458f7947e967787ba4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"övgü, güçlü istek ve kabul bildiren kalıplar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli söz kalıplarıyla övgü, güçlü istek veya hoşnut kabul bildirme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi veya şeyi öven ve iyi bulduğunu bildiren kalıp."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işi yapmayı isteğin son noktası olarak sunan ya da öneriyi memnuniyetle kabul eden kalıp."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirinden farklı üç kalıplaşmış söylem işlevini genel sevgiyle karıştırmadan birlikte temsil eder.","boundary_detail":"Bu dal genel sevgi duygusunu değil, övgü, en güçlü istek veya nazik kabul bildiren belirli kalıpları kapsar.","branch_image_ar":"صيغة المدح وغاية الرغبة","concept_gloss":"övgü, güçlü istek ve kabul bildiren kalıplar","contextual_glosses":[{"applicability":"Bir kişi veya şey hakkında doğrudan övgü ve beğeni bildirilen kalıp bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"En güçlü istek bildirimini ve memnuniyetle kabul cevabını dışarıda bırakır.","preserves":"Övgü ve beğeni bildiren kalıplaşmış işlevi korur."},"facet_ids":["F001","F002"],"text":"ne güzel","usage_role":"contextual"}],"definition":"Belirli kalıplarla bir kişiyi ya da şeyi övme, bir eylemi en güçlü istek olarak sunma veya öneriyi hoşnutlukla kabul etme işlevidir. Bu işlevler genel sevgi anlamı değil, kalıba bağlı söylem kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli söz kalıplarıyla övgü, güçlü istek veya hoşnut kabul bildirme."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi veya şeyi öven ve iyi bulduğunu bildiren kalıp."},{"facet_id":"F003","role":"specialization","statement":"Bir işi yapmayı isteğin son noktası olarak sunan ya da öneriyi memnuniyetle kabul eden kalıp."}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlam değil, övgü bildiren kalıbı, bir işi yapmaya yönelik en güçlü isteği ve hoş bir kabul cevabını birlikte verir. Dal ancak bu üç kullanımın ayrı kalıplar olduğu açıkça belirtilirse korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne güzel; ne iyi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"en büyük isteğin bunu yapmaktır"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"peki, memnuniyetle ve baş üstüne"}],"lexicalization_note":"Dal iki söz öbeği ile bir kalıplaşmış cevap birimini içerir; bunların işlevleri yalın kökün genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; övgü işlevini doğrudan karşılaştıran aday yayımlandı. Genel övme eylemleri, cevap kalıpları ve aynı kökün ilgisiz anlamları ikincil kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Övgü işlevinde yaklaşırlar, fakat odak dal belirli bir yapıyla sınırlıdır ve ayrıca istek ile kabul kalıplarını içerir; komşu dalın övgü yapısı bu ek işlevleri taşımaz.","focus_only":"Odak dal övgünün yanında güçlü istek ve nazik kabul bildiren başka kalıpları da kapsar.","gloss":"kalıpla övgü bildirme","neighbor_only":"Komşu dal, karşıt bir yergi kalıbıyla eşleşen genel övgü ve beğeni yapısını kapsar.","neighbor_ref":"root_001525/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi veya şeyi kalıplaşmış sözle iyi ve övgüye değer gösterir."}],"source_phrase_ar":"حبذا حرفان حب وذا تقول حبذا زيد (ayn;sihah;tahdhib)؛ حبابك أن تفعل ذاك معناه غاية محبتك (ayn;sihah;tahdhib;mufradat)؛ الحبة بالضم الحب يقال نعم وحبة وكرامة (sihah)","source_summary":"Ortak kayıt, övgü kalıbını, bir eyleme yönelik en yüksek istek bildirimini ve olumlu kabul cevabını aynı kalıplaşmış kullanım alanında toplar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حبذا، وحبابك أن تفعل، ونعم وحبة وكرامة، وما جاء بصيغة مدح أو بلوغ الغاية في المحبة.","what_is_not_ar":"ليس مطلق المحبة ولا الحبوب ولا لزوم البعير."},"support_links":["sup_56d989c3579557b90075"]},{"boundary":"Anlam yalnızca kalbin içindeki kara nokta veya öz için kullanılan söz öbeğine bağlıdır; genel sevgi ya da bitkisel tane anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000286/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"kalbin içindeki kara öz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalbin içindeki kara nokta veya kara doku."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin özü ya da meyvesi olarak açıklanan iç bölüm."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İç bölümün biçim bakımından taneye benzetilmesi."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalbin kara iç dokusu ile öz veya meyve açıklamasını birlikte taşıyan söz öbeği karşılığıdır.","boundary_detail":"Anlam yalnızca kalbin içindeki kara nokta veya öz için kullanılan söz öbeğine bağlıdır; genel sevgi ya da bitkisel tane anlamı değildir.","branch_image_ar":"حبة القلب سويداؤه","concept_gloss":"kalbin içindeki kara öz","contextual_glosses":[{"applicability":"İçteki kara doku fiziksel bir bölüm olarak açıklanırken kullanılabilecek açık karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalbin özü veya meyvesi biçimindeki açıklayıcı değişkeleri geri plana iter.","preserves":"Kalbin içindeki kara bölümün fiziksel görünümünü korur."},"facet_ids":["F001","F003"],"text":"kalbin kara noktası","usage_role":"explanatory"}],"definition":"Kalbin içindeki kara nokta, kara doku veya kalbin özü sayılan bölümdür. Tane adı bu bölüme biçim benzerliğiyle verilmiştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalbin içindeki kara nokta veya kara doku."},{"facet_id":"F002","role":"source_variant","statement":"Kalbin özü ya da meyvesi olarak açıklanan iç bölüm."},{"facet_id":"F003","role":"extension","statement":"İç bölümün biçim bakımından taneye benzetilmesi."}],"identity_rationale":"Kaynak ifadesi kalbin içindeki kara bölümü, çekirdeği ya da meyvesi olarak adlandırılan kısmı ve bunun taneye biçimce benzetilmesini açıkça verir. Sağlanan dal çerçevesi bu anatomik ve benzetmeli sınırı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kalbin kara iç noktası veya özü"}],"lexicalization_note":"Tanım yalnızca kalbin iç bölümünü adlandıran söz öbeğine bağlıdır ve yalın tane ya da sevgi anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalbin kara iç bölümünü doğrudan paylaşan aday yayımlandı. Ağız, boyun, diş ve yalnızca genel içlik bildiren adaylar daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kalp bağlamında büyük ölçüde örtüşürler; komşu dal ayrıca çörek otu tanesini kapsadığı, odak dal ise iç dokunun öz ve meyve açıklamalarını belirginleştirdiği için sınır kısmen eşleşir.","focus_only":"Odak dal kalbin içindeki kara dokuyu ayrıca kalbin özü veya meyvesi olarak açıklar.","gloss":"kalbin kara iç bölümü","neighbor_only":"Komşu dal aynı kalp bölgesinin yanında çörek otu tanesini de aynı adlandırma alanına alır.","neighbor_ref":"root_000757/B009","relation_type":"near_synonym","shared_zone":"Her iki dal kalbin kara iç noktasını ve öz sayılan bölümünü adlandırır."}],"source_phrase_ar":"حبة القلب سويداؤه ويقال ثمرته (maqayis;sihah)؛ حبة القلب هي العلقة السوداء التي تكون داخل القلب (tahdhib)؛ حبة القلب تشبيها بالحبة في الهيئة (mufradat)","source_summary":"Ortak kayıt kalbin kara iç bölümünü temel alır; bu bölümün kalbin özü veya meyvesi diye açıklanmasını ve taneye biçimce benzetilmesini birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حبة القلب بمعنى سويدائه أو ثمرته أو العلقة السوداء داخله، وما صيغ كإصابة حبة القلب.","what_is_not_ar":"ليس مطلق المحبة إلا إذا صرحت العبارة بحبة القلب، وليس الحبة النباتية."},"support_links":[]},{"boundary":"Bu anlam devenin güçsüzlük veya direnme nedeniyle bulunduğu yerde kalmasına özgüdür; sevgi veya suyla dolma anlamı değildir.","branch_kind":"bare","branch_ref":"root_000286/B005","candidate_links":[{"candidate_id":"cand_b669b627254226f5a0db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"devenin güçsüzlükten yerinden ayrılamaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin durup veya çöküp bulunduğu yerde kalması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareketsizliğin bitkinlik, hastalık, kırık veya direnmeden doğması."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Katılımcıyı, nedeni ve yerinde kalma sonucunu birlikte veren tam açıklayıcı karşılıktır.","boundary_detail":"Bu anlam devenin güçsüzlük veya direnme nedeniyle bulunduğu yerde kalmasına özgüdür; sevgi veya suyla dolma anlamı değildir.","branch_image_ar":"البعير يلزم مكانه من عجز","concept_gloss":"devenin güçsüzlükten yerinden ayrılamaması","contextual_glosses":[{"applicability":"Nedenin hastalık olduğu ve devenin çöktüğü anlatı bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitkinlik, kırık veya direnme gibi öteki nedenleri dışarıda bırakır.","preserves":"Hastalık yüzünden devenin çöküp yerinde kalmasını korur."},"facet_ids":["F001","F002"],"text":"hastalıktan çöküp kalan deve","usage_role":"contextual"}],"definition":"Bir devenin bitkinlik, hastalık, kırık veya direnme nedeniyle durması, çökmesi ve bulunduğu yerden ayrılamamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin durup veya çöküp bulunduğu yerde kalması."},{"facet_id":"F002","role":"specialization","statement":"Hareketsizliğin bitkinlik, hastalık, kırık veya direnmeden doğması."}],"identity_rationale":"Kaynak ifadesi devenin yorgunluk, hastalık, kırık veya direnme yüzünden durup yerinden ayrılamamasını tutarlı biçimde anlatır. Dal çerçevesi hem katılımcıyı hem nedeni hem de kalıcı durma sonucunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"devenin güçsüzlükten durup yerinden ayrılamaması"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"devenin hastalık veya güçsüzlükten çökmesi"}],"lexicalization_note":"Dal devenin durup yerinde kalmasıyla ilgili yalın eylem alanıdır; komşu söz öbeklerinin anlamları tanıma eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; güçsüzlük ile yerinde kalma bağını en iyi paylaşan aday yayımlandı. Yalnızca hayvan türü, gecikme veya genel yatma bildirenler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal devenin gerçek durma ve yerinden ayrılamama olayını bildirir; komşu dal ise aşırı zayıflığı, hareketsizliğe benzer görünümüyle niteler ve insanı da kapsar.","focus_only":"Odak dal özellikle devenin hastalık, kırık, bitkinlik veya direnme yüzünden yerinden ayrılamamasını anlatır.","gloss":"güçsüzlükten hareketsiz kalma","neighbor_only":"Komşu dal insanı veya deveyi aşırı zayıflayıp sanki sabit kalmış görünmesi bakımından niteler.","neighbor_ref":"root_000607/B005","relation_type":"near_neighbor","shared_zone":"İki dalda da bedensel güç kaybı hareket edememe veya yerinde kalma sonucuna yaklaşır."}],"source_phrase_ar":"المحب البعير الذي يحسر فيلزم مكانه (maqayis)؛ بعير محب وقد أحب إحبابا وهو أن يصيبه مرض أو كسر فلا يبرح من مكانه (sihah;tahdhib)؛ أحب البعير إذا حرن ولزم مكانه (mufradat)","source_summary":"Ortak kayıt devenin durup yerini terk edememesini temel alır ve bu durumu bitkinlik, hastalık, kırık ya da direnmeye bağlar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أحب البعير، والبعير المحب، والإحباب في الإبل إذا وقف أو برك أو لزم مكانه من حسر أو مرض أو كسر.","what_is_not_ar":"ليس المحبة القلبية، ولا الامتلاء من الماء، ولا صغر الجسم."},"support_links":["sup_1d76b90172560ca8ae8a"]},{"boundary":"Hayvanın suyla doyması ve kabın doldurulması aynı doluluk alanındadır; hasta devenin çökmesi veya büyük küp anlamı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000286/B006","candidate_links":[{"candidate_id":"cand_b669b627254226f5a0db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"suyla dolmak veya doldurup dolulaştırmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşek veya devenin su içerek dolması ya da suya kanmanın ilk aşamasına ulaşması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tulum veya benzeri bir kabı doldurup dolu hale getirme."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın su içerek dolmasıyla kabın ettirgen biçimde doldurulmasını katılımcı farkını koruyarak birleştirir.","boundary_detail":"Hayvanın suyla doyması ve kabın doldurulması aynı doluluk alanındadır; hasta devenin çökmesi veya büyük küp anlamı bu dala girmez.","branch_image_ar":"الري حتى الامتلاء","concept_gloss":"suyla dolmak veya doldurup dolulaştırmak","contextual_glosses":[{"applicability":"Eşek veya develerin yeterince su içtiği hayvan bağlamında kullanılabilecek doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir tulumun veya başka kabın dışarıdan doldurulması kullanımını dışarıda bırakır.","preserves":"Hayvanın su içerek dolması ve doygunluğa yaklaşması anlamını korur."},"facet_ids":["F001"],"text":"suya kanmak","usage_role":"contextual"}],"definition":"Bir hayvanın su içerek dolması veya suya kanma aşamasına ulaşmasıdır. Ettirgen kullanımda tulum gibi bir kabı doldurup dolu hale getirmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşek veya devenin su içerek dolması ya da suya kanmanın ilk aşamasına ulaşması."},{"facet_id":"F002","role":"extension","statement":"Tulum veya benzeri bir kabı doldurup dolu hale getirme."}],"identity_rationale":"Kaynak ifadesi hayvanın su içerek dolmasını veya suya kanmanın ilk aşamasını, ayrıca tulum gibi bir kabı doldurup dolu hale getirmeyi birlikte verir. Dal korunabilir, ancak içenin doyması ile bir kabın doldurulması ayrı katılımcı yapıları olarak gösterilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"su içip dolmak veya suya kanmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"doldurup dolu hale getirmek"}],"lexicalization_note":"Dal su içerek dolma ve bir şeyi doldurma eylemlerinin yalın alanıdır; kap adı veya hayvanın güçsüzlükten çökmesi tanıma katılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak doldurma işlemini katılımcı farkıyla gösteren aday yayımlandı. Genel susuzluk, içme veya aynı kökün ilgisiz dalları daha zayıf kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal canlı bir içenin suya kanmasını ve taşınabilir kabı da kapsarken komşu dal sabit bir yalak ya da havuzun doldurulmasına bağlıdır; katılımcı sınırları farklıdır.","focus_only":"Odak dal su içen hayvanın doymasını ve tulum gibi bir kabın doldurulmasını kapsar.","gloss":"suyla doldurma","neighbor_only":"Komşu dal özellikle bir yalak veya havuzun doldurulmasını ve dolu durumunu anlatır.","neighbor_ref":"root_000642/B008","relation_type":"near_neighbor","shared_zone":"İki dal da bir alıcıyı suyla doldurma ve doluluk sonucuna ulaştırma alanındadır."}],"source_phrase_ar":"تحبب الحمار إذا امتلأ من الماء وشربت الإبل حتى حببت (sihah)؛ أول الري التحبب وحببته فتحبب إذا ملأته للسقاء وغيره (tahdhib)","source_summary":"Ortak kayıt su içen hayvanın dolmasını ve suya kanma aşamasını, ayrıca bir kabın doldurularak dolu hale getirilmesini aynı eylem ailesinde verir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه تحبب الحمار أو الإبل من الماء، وأول الري، وملء السقاء ونحوه حتى يمتلئ.","what_is_not_ar":"ليس الإحباب بمعنى بروك البعير من مرض، ولا الحب بمعنى الجرة."},"support_links":["sup_1d76b90172560ca8ae8a"]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000286/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"iri küp ve iki kulplu küpün dört parçalı desteği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İri küp veya büyük saklama kabı."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki kulplu küpün altına konan dört parçalı ahşap destek."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıttaki iki göndergenin ikisini de, iri saklama kabını ve bu kabın altına konan ahşap desteği, tek bir üretken anlam varsaymadan temsil eder.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"الحب جرة عظيمة أو موضعها","concept_gloss":"iri küp ve iki kulplu küpün dört parçalı desteği","definition":"Kayıt, iri bir küp ile iki kulplu küpün altına konan dört parçalı desteği aynı dalda birleştirir. Bu iki ayrı nesne yapısal olarak ayrılmadan tek bir kavram tanımı kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İri küp veya büyük saklama kabı."},{"facet_id":"F002","role":"source_variant","statement":"İki kulplu küpün altına konan dört parçalı ahşap destek."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iri küp veya büyük saklama kabı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"iki kulplu küpün dört parçalı ayağı"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الحب الجرة الضخمة ويجمع على حببة وحباب (ayn;tahdhib)؛ الحب الخابية فارسي معرب والجمع حباب وحببة (sihah)؛ الحب الخشبات الأربع التي توضع عليها الجرة ذات العروتين (ayn;tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه الحب بمعنى الجرة الضخمة أو الخابية، وجمعه حباب وحببة، وما قيل في الخشبات التي توضع عليها الجرة.","what_is_not_ar":"ليس الحب بمعنى المحبة ولا الحبة النباتية."},"support_links":[]},{"boundary":"Su kabarcığı, su kütlesi ve yüzey izi söz öbeğine bağlı değişkelerdir; ağaç üzerindeki çiy ayrı bir uzantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su yüzeyinde yüzen kabarcıklar."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun ana kütlesi, dalgası veya yüzeyindeki çizgiler."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ağaçların üzerinde sabah görülen çiy."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su söz öbeğinin değişkenlerini ve ayrı çiy uzantısını kapsam ayrılığını koruyarak temsil eder.","boundary_detail":"Su kabarcığı, su kütlesi ve yüzey izi söz öbeğine bağlı değişkelerdir; ağaç üzerindeki çiy ayrı bir uzantıdır.","branch_image_ar":"حباب الماء فقاقيعه وطرائقه","concept_gloss":"su kabarcıkları, su yüzeyi ve ağaç üzerindeki çiy","contextual_glosses":[{"applicability":"Suyun üzerinde yüzen küçük hava keseciklerinin anlatıldığı fiziksel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Suyun ana kütlesi, dalgaları, yüzey çizgileri ve ağaç üzerindeki çiy kullanımlarını dışarıda bırakır.","preserves":"Suyun yüzeyindeki yüzen kabarcıklar anlamını tam korur."},"facet_ids":["F001"],"text":"su kabarcıkları","usage_role":"contextual"}],"definition":"Suya bağlı söz öbeğinde yüzeyde yüzen kabarcıkları, suyun ana kütlesini veya dalga ve çizgilerini anlatır. Ayrı bir yalın kullanımda ağaçların üzerinde sabah görülen çiyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su yüzeyinde yüzen kabarcıklar."},{"facet_id":"F002","role":"source_variant","statement":"Suyun ana kütlesi, dalgası veya yüzeyindeki çizgiler."},{"facet_id":"F003","role":"extension","statement":"Ağaçların üzerinde sabah görülen çiy."}],"identity_rationale":"Kaynak ifadesi su yüzeyindeki kabarcıkları, suyun ana kütlesini, dalga ve çizgilerini, ayrıca ağaç üzerindeki çiyi birlikte verir. Dal kullanılabilir, ancak suya bağlı söz öbeğinin değişkenleri ile ayrı çiy kullanımı tek bir fiziksel olgu gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"su kabarcıkları, suyun ana kütlesi, dalgası veya yüzey çizgileri"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ağaç üzerindeki çiy"}],"lexicalization_note":"Dal suya bağlı bir söz öbeği ile yalın çiy kullanımını içerir; söz öbeğinin bütün değişkeleri genel yalın anlama dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su yüzeyindeki çizgileri doğrudan paylaşan aday yayımlandı. Köpük, rüzgâr, dalga ve aynı kökün başka anlamları yalnızca alan komşuluğu sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yüzey çizgileri bakımından yakınlaşırlar; odak dal çok anlamlı söz öbeği içinde kabarcık, su kütlesi ve çiyi de içerdiği için komşunun daha dar görsel alanıyla tam örtüşmez.","focus_only":"Odak dal yüzey çizgilerinin yanında kabarcıkları, su kütlesini, dalgayı ve ağaç üzerindeki çiyi de kapsar.","gloss":"suyun yüzey çizgileri","neighbor_only":"Komşu dal özellikle suyun süslü görünüm veren çizgi ve biçimlerine odaklanır.","neighbor_ref":"root_000628/B004","relation_type":"near_synonym","shared_zone":"İki dal su yüzeyinde görülen çizgileri ve düzenli görünüşleri kapsar."}],"source_phrase_ar":"حباب الماء فقاقيعه الطافية (ayn;tahdhib)؛ حباب الماء معظمه (maqayis;ayn;sihah;tahdhib)؛ حباب الماء موجه والطرائق التي في الماء (tahdhib)؛ الحباب من الماء النفاخات تشبيها به (mufradat)؛ الحباب الطل على الشجر (tahdhib)","source_summary":"Ortak kayıt su bağlamında kabarcık, ana su kütlesi, dalga ve yüzey çizgisi değişkelerini toplar; ayrıca ağaç üzerindeki çiyi ayrı bir kullanım olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حباب الماء بمعنى الفقاقيع الطافية أو معظم الماء أو موجه وطرائقه، وما ألحق به من الطل على الشجر.","what_is_not_ar":"ليس الحب الحبوب، ولا حبب الأسنان، ولا الحباب بمعنى الحية."},"support_links":[]},{"boundary":"Dal diş dizilişi ve üzerindeki beyaz tükürük görünüşüyle sınırlıdır; su kabarcığı veya bitkisel tane anlamı değildir.","branch_kind":"bare","branch_ref":"root_000286/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"düzenli diş dizisi ve beyaz tükürük parıltısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişlerin taneler gibi düzenli ve yan yana dizilmesi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişlerin üzerinde beyaz tükürüğün tanecikli ve parlak görünmesi."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişlerin hem düzenini hem de üzerlerindeki beyaz görünüşü taşıyan açıklayıcı karşılıktır.","boundary_detail":"Dal diş dizilişi ve üzerindeki beyaz tükürük görünüşüyle sınırlıdır; su kabarcığı veya bitkisel tane anlamı değildir.","branch_image_ar":"حبب الأسنان انتظام كالدرر","concept_gloss":"düzenli diş dizisi ve beyaz tükürük parıltısı","contextual_glosses":[{"applicability":"Dişlerin düzenli ve güzel dizilişinin betimlendiği bağlamda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişlerin üzerinde görülen beyaz tükürük tanecikleri ve parıltısını açıkça vermez.","preserves":"Dişlerin küçük taneler gibi düzenli dizilişini korur."},"facet_ids":["F001"],"text":"inci gibi dizilmiş dişler","usage_role":"contextual"}],"definition":"Dişlerin taneler gibi düzenli biçimde yan yana dizilmesi ve üzerlerinde beyaz tükürüğün tanecikli bir parlaklık oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişlerin taneler gibi düzenli ve yan yana dizilmesi."},{"facet_id":"F002","role":"extension","statement":"Dişlerin üzerinde beyaz tükürüğün tanecikli ve parlak görünmesi."}],"identity_rationale":"Kaynak ifadesi dişlerin düzenli dizilişini ve dişlerin üzerinde tanecikler halinde görünen beyaz tükürük parıltısını açıkça birleştirir. Sağlanan dal çerçevesi düzen ile beyaz görünüşü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"düzenli diş dizisi veya dişlerdeki beyaz tükürük parıltısı"}],"lexicalization_note":"Dal dişlerin düzeni ve beyaz görünüşüne ait yalın biçimi tanımlar; başka nesnelerdeki tane veya kabarcık anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; diş düzeni ve beyazlığını birlikte paylaşan aday yayımlandı. Yalnızca parlaklık, belirli diş türü veya yüz güzelliği bildirenler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Düzen ve beyazlıkta yakın anlamlıdırlar; odak dal tanecikli tükürük görünüşüne özgüyken komşu dal diş yapısının düzgünlük, aralık ve genel güzellik özelliklerini daha geniş tutar.","focus_only":"Odak dal taneye benzer düzenin yanında dişler üzerindeki beyaz tükürük parıltısını özellikle kapsar.","gloss":"düzgün ve beyaz dişler","neighbor_only":"Komşu dal dişlerin düzgün çıkışını, aralıklı oluşunu, beyazlığını ve genel güzelliğini daha geniş biçimde kapsar.","neighbor_ref":"root_000540/B003","relation_type":"near_synonym","shared_zone":"İki dal dişlerin düzenli dizilişini, beyazlığını ve güzel görünüşünü paylaşır."}],"source_phrase_ar":"الحبب تنضد الأسنان (maqayis;ayn;sihah;tahdhib)؛ الحبب تنضد الأسنان تشبيها بالحب (mufradat)؛ حبب الفم ما يتحبب من بياض الريق على الأسنان (tahdhib)","source_summary":"Ortak kayıt dişlerin düzenli dizilişini temel alır ve bu görünüşü taneye benzetir; dişler üzerindeki beyaz tükürük parıltısını da aynı alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحبب وحبب الأسنان، أي تنضد الأسنان وظهور بياض الريق عليها.","what_is_not_ar":"ليس حباب الماء، ولا الحبة النباتية إلا من جهة التشبيه."},"support_links":[]},{"boundary":"Temel alan kısa veya küçük beden yapısıdır; develerdeki cılızlık ayrı ve türemiş bir kullanım olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"kısa veya küçük yapılı; develerde cılız","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın kısa boylu veya küçük bedenli olması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Küçük kişileri topluca niteleyen çoğul kullanım."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Develerin cılız ve zayıf oluşunu bildiren söz öbeği."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan için temel beden ölçüsünü ve deve söz öbeğindeki zayıflık uzantısını ayrı tutan karşılıktır.","boundary_detail":"Temel alan kısa veya küçük beden yapısıdır; develerdeki cılızlık ayrı ve türemiş bir kullanım olarak tutulur.","branch_image_ar":"الحبحاب الصغير القصير","concept_gloss":"kısa veya küçük yapılı; develerde cılız","contextual_glosses":[{"applicability":"Bir insanın boyunun kısa olduğu doğrudan niteleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel küçük beden anlamını ve develere özgü cılızlık kullanımını dışarıda bırakır.","preserves":"İnsan için kısa boy nitelemesini açık biçimde korur."},"facet_ids":["F001"],"text":"kısa boylu","usage_role":"contextual"}],"definition":"Bir insanın kısa boylu veya küçük bedenli olmasıdır. Develere bağlı söz öbeğinde ise kısa boydan çok cılız ve zayıf oluşu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın kısa boylu veya küçük bedenli olması."},{"facet_id":"F002","role":"specialization","statement":"Küçük kişileri topluca niteleyen çoğul kullanım."},{"facet_id":"F003","role":"extension","statement":"Develerin cılız ve zayıf oluşunu bildiren söz öbeği."}],"identity_rationale":"Kaynak ifadesi kısa veya küçük yapılı insanı ve küçükleri temel alırken zayıf develeri ayrıca aynı türemiş biçim alanında verir. Dal korunabilir, ancak insanın kısa ve küçük oluşu ile develerin zayıflığı tek bedensel özellik gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kısa boylu veya küçük bedenli kimse"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"cılız develer"}],"lexicalization_note":"Dal yalın kısa veya küçük beden nitelemesiyle develere bağlı bir söz öbeğini içerir; deve cılızlığı genel kısa boy anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kısa ve küçük beden çekirdeğini en doğrudan paylaşan aday yayımlandı. Yalnızca zayıflık, irilik veya hayvan türü paylaşanlar daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsan nitelemesinde yakın anlamlıdırlar; odak dalın deve cılızlığına özgü uzantısı, komşunun ise daha genel küçüklük ve alçaklık kapsamı bulunduğu için sınırlar kısmen eşleşir.","focus_only":"Odak dal insanın kısa veya küçük bedenini ve söz öbeğinde develerin cılızlığını kapsar.","gloss":"kısa ve küçük yapılı","neighbor_only":"Komşu dal insan dışındaki küçük varlıkları ve fiziksel alçaklığı da kapsayan daha genel bir küçüklük alanına uzanır.","neighbor_ref":"root_000336/B005","relation_type":"near_synonym","shared_zone":"İki dal insan için kısa boy ve küçük beden nitelemesinde örtüşür."}],"source_phrase_ar":"الحبحاب الرجل القصير (maqayis)؛ الحباحب الصغار (maqayis;sihah)؛ الحبحاب الصغير الجسم (tahdhib)؛ إبل حبحبة مهازيل (tahdhib)","source_summary":"Ortak kayıt insan için kısa boy ve küçük beden nitelemesini verir; aynı biçim ailesindeki deve söz öbeğini ise cılızlık ve zayıflık anlamıyla ekler.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الحبحاب والحباحب بمعنى القصير أو الصغير الجسم، وما وصف به من هزال الإبل.","what_is_not_ar":"ليس البعير المحب الذي يبرك من عجز، ولا نار الحباحب."},"support_links":[]},{"boundary":"Çekirdek zayıf ve işe yaramayan kıvılcımdır; gece ışıldayan böcek, ışık görünüşüne bağlı ayrı bir değişkedir.","branch_kind":"mixed_non_bare","branch_ref":"root_000286/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taş çarpışmasından veya at toynağından çıkan, işe yaramayan zayıf kıvılcım."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geceleri uçarken kandil gibi ışık saçan böcek."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu tür zayıf kıvılcımın veya ateşin tutuşması."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kıvılcım çekirdeğini ve ışık benzerliğine dayalı böcek değişkesini birlikte karşılar.","boundary_detail":"Çekirdek zayıf ve işe yaramayan kıvılcımdır; gece ışıldayan böcek, ışık görünüşüne bağlı ayrı bir değişkedir.","branch_image_ar":"نار الحباحب شرر لا ينتفع به","concept_gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek","contextual_glosses":[{"applicability":"Taşların veya toynakların çarpışmasıyla çıkan ve ateş yakmaya yetmeyen kıvılcım bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geceleri ışık saçan böcek değişkesini ve tutuşma eylemini dışarıda bırakır.","preserves":"Kıvılcımın zayıf ve yararlanılamaz oluşunu korur."},"facet_ids":["F001"],"text":"boşuna çıkan zayıf kıvılcım","usage_role":"contextual"}],"definition":"Taşların çarpışmasından veya atların toynaklarından havaya saçılan, ateş yakmaya yaramayan zayıf kıvılcımdır. Aynı adlandırma, geceleri kandil gibi ışık saçarak uçan böcek için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taş çarpışmasından veya at toynağından çıkan, işe yaramayan zayıf kıvılcım."},{"facet_id":"F002","role":"source_variant","statement":"Geceleri uçarken kandil gibi ışık saçan böcek."},{"facet_id":"F003","role":"associated_use","statement":"Bu tür zayıf kıvılcımın veya ateşin tutuşması."}],"identity_rationale":"Kaynak ifadesi taşların çarpışmasından veya atların toynaklarından çıkan yararsız kıvılcımları ve geceleri ışık saçan uçucu böceği birlikte verir. Dal korunabilir, ancak böcek kıvılcımın bir aşaması değil, ışık benzerliğiyle aynı adlandırma alanına giren ayrı bir referanstır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yararsız zayıf kıvılcım veya gece ışıldayan böcek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"zayıf kıvılcımın tutuşması"}],"lexicalization_note":"Dal bir kalıplaşmış birim ile onun tutuşma biçimini içerir; kıvılcım ve ışıldayan böcek değişkeleri yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kıvılcım alanını doğrudan paylaşan aday yayımlandı. Taş, parlama, tutuşma ve kanat çırpma adayları yalnızca senaryo bağı kurdu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kıvılcım alanında yakın anlamlıdırlar; odak dal kaynak ve yararsızlık koşullarıyla daralır, ayrıca ışıldayan böceğe uzanır, komşu ise genel kıvılcım adıdır.","focus_only":"Odak dal belirli çarpışmalardan doğan yararsız zayıf kıvılcımı ve ayrıca ışıldayan gece böceğini kapsar.","gloss":"ateşten sıçrayan kıvılcım","neighbor_only":"Komşu dal kaynağına, yararına veya gücüne bakmadan ateşten sıçrayan kıvılcımı genel olarak kapsar.","neighbor_ref":"root_000787/B003","relation_type":"near_synonym","shared_zone":"İki dal da havaya saçılan küçük ateş parçalarını ve kıvılcımları kapsar."}],"source_phrase_ar":"نار الحباحب ما اقتدحت من شرار النار في الهواء من تصادم الحجارة (ayn;tahdhib)؛ نار الحباحب ما أورت الخيل لا ينتفع به (maqayis;sihah;tahdhib)؛ ذباب يطير بالليل له شعاع كالسراج (ayn;sihah;tahdhib)","source_summary":"Ortak kayıt çarpışma veya toynak vuruşuyla çıkan yararsız kıvılcımı temel alır ve geceleri ışık saçan uçucu böceği görünüş benzerliğiyle aynı adlandırmaya bağlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه نار الحباحب، الشرر الضعيف من الحجارة أو حوافر الخيل، والذباب أو الطائر المضيء ليلا، والنار التي لا ينتفع بها.","what_is_not_ar":"ليس الحباحب بمعنى الصغار، ولا الحب بمعنى المحبة."},"support_links":[]},{"boundary":"Temel anlam yılandır; kötücül ruh adı, yılanla kurulan adlandırma ilişkisine bağlı ikincil kullanımdır.","branch_kind":"bare","branch_ref":"root_000286/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","surface_ar":"تُحِبُّ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","surface_ar":"حُبًّا"}],"gloss":"yılan; yılanla ilişkilendirilen kötücül ruh adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yılanı adlandıran yalın sözlük anlamı."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yılanla kurulan adlandırma ilişkisi üzerinden kötücül bir ruhun adı olarak kullanım."}}],"root_ar":"ح ب ب","root_id":"root_000286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Temel hayvan referansını ve ondan türeyen ad kullanımını hiyerarşisini bozmadan karşılar.","boundary_detail":"Temel anlam yılandır; kötücül ruh adı, yılanla kurulan adlandırma ilişkisine bağlı ikincil kullanımdır.","branch_image_ar":"الحباب الحية أو الشيطان","concept_gloss":"yılan; yılanla ilişkilendirilen kötücül ruh adı","contextual_glosses":[{"applicability":"Sözün doğrudan hayvanı adlandırdığı temel sözlük bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yılanla ilişkilendirilerek kurulan kötücül ruh adı kullanımını dışarıda bırakır.","preserves":"Dalın temel hayvan referansı olan yılan anlamını tam korur."},"facet_ids":["F001"],"text":"yılan","usage_role":"general"}],"definition":"Bir yılanı adlandırır. Yılanın kötücül ruhla özdeşleştirildiği adlandırma geleneği üzerinden aynı söz bir kötücül ruhun adı olarak da kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yılanı adlandıran yalın sözlük anlamı."},{"facet_id":"F002","role":"associated_use","statement":"Yılanla kurulan adlandırma ilişkisi üzerinden kötücül bir ruhun adı olarak kullanım."}],"identity_rationale":"Kaynak ifadesi sözün temel referansını yılan olarak verir ve kötücül ruh adı kullanımını yılanın da böyle adlandırılmasıyla açıklar. Dal korunabilir, ancak yılan ile kötücül ruh eş anlamlı iki temel anlam gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"yılan veya yılanla ilişkilendirilen kötücül ruh adı"}],"lexicalization_note":"Dal yalın biçimin yılan anlamını ve buna bağlı kötücül ruh adı kullanımını kapsar; su veya sevgi söz öbekleri tanıma girmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yılan referansını en doğrudan paylaşan aday yayımlandı. Belirli yılan türleri, özel adlar ve yalnızca kötücül ruh alanı paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Temel hayvan referansında yakın anlamlıdırlar; odak dal kötücül ruh adına uzanırken komşu dal yılanın cinsiyet ve türeme alanını genişletir, bu yüzden sınırları tam eşleşmez.","focus_only":"Odak dal yılan anlamının yanında yılanla ilişkilendirilen kötücül ruh adı kullanımını kapsar.","gloss":"yılan adı","neighbor_only":"Komşu dal yılanın erkeğini, dişisini ve yılanlarla uğraşan kişiye bağlı türemiş adları daha geniş biçimde kapsar.","neighbor_ref":"root_000383/B004","relation_type":"near_synonym","shared_zone":"İki dalın temel referansı cinsiyet ayrımı yapılmadan yılan hayvanıdır."}],"source_phrase_ar":"ومما شذ عن الباب الحباب وهو الحية (maqayis)؛ الحباب أيضا الحية (sihah)؛ الحباب الحية وإنما قيل الحباب اسم شيطان لأن الحية يقال لها شيطان (tahdhib)","source_summary":"Ortak kayıt yalın anlamı yılan olarak verir; kötücül ruh adı kullanımını ise yılanın da kötücül ruh sayılmasına dayanan bir adlandırma ilişkisiyle açıklar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الحباب بمعنى الحية، وما قيل في اسم الشيطان لكون الحية شيطانا.","what_is_not_ar":"ليس حباب الماء، ولا حبابك بمعنى غاية محبتك، ولا الحب بمعنى المحبة."},"support_links":[]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_2e44a647ba80a0a1b00c","lane":"micro"},{"candidate_id":"cand_05458f7947e967787ba4","lane":"micro"},{"candidate_id":"cand_1e3635f4a00aae40f812","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:2:2","qac_word_ref":"89:20:2","surface_ar":"مَالَ"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_30532e533a0ec594e9ed","sup_56d989c3579557b90075","sup_e0d2cb9d95b3280c98e3"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:2:2","qac_word_ref":"89:20:2","surface_ar":"مَالَ"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:20:1"],"branch_refs":[],"candidate_id":"cand_89c0a01213fd6587d9e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:20:1:accumulating-rebuke-cadence","source_type":"word_analysis","support_ids":["sup_4aa072369db9cdfc69be","sup_4b17e2fc7422dd79cbd3"],"title":"accumulating rebuke cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:1","qac_refs":["89:20:1:1"],"status":"accepted"}},{"anchor_refs":["89:20:1"],"branch_refs":[],"candidate_id":"cand_ad0837dbc8c8182bd384","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:20:1:coordinate-charge","source_type":"word_analysis","support_ids":["sup_4b17e2fc7422dd79cbd3","sup_98bcf7c0292a8e070f00"],"title":"coordinate continuation, not chronology","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:1","qac_refs":["89:20:1:1"],"status":"accepted"}},{"anchor_refs":["89:20:1"],"branch_refs":[],"candidate_id":"cand_85a38fe23fcb2fe90b31","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:20:1:prefixed-opening","source_type":"word_analysis","support_ids":["sup_0b4ee53c3de5f010bd95","sup_4b17e2fc7422dd79cbd3"],"title":"prefixed connector fused to accusation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:1","qac_refs":["89:20:1:1"],"status":"accepted"}},{"anchor_refs":["89:20:1"],"branch_refs":[],"candidate_id":"cand_385fbcad06d197a971e0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:20:1:same-addressee-bridge","source_type":"word_analysis","support_ids":["sup_309b3b0cfbf4f32a1e12","sup_4b17e2fc7422dd79cbd3"],"title":"same audience carried into motive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:1","qac_refs":["89:20:1:1"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_adc707adee7c74447010","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:communal-ongoing-address","source_type":"word_analysis","support_ids":["sup_0881a9c245341e16ad2a","sup_8dc3a5fa40ad89b260ab"],"title":"ongoing plural accusation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_81b53d3dfc073677faef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:directed-value-target","source_type":"word_analysis","support_ids":["sup_6c3c3be417ba5eb633e7","sup_8dc3a5fa40ad89b260ab"],"title":"directed preference toward wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_6783a7ecd71f759e3d6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:motive-after-economic-failure","source_type":"word_analysis","support_ids":["sup_82d66fc09d1068a62859","sup_8dc3a5fa40ad89b260ab"],"title":"motive follows outward failure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_934149ef936ef031b282","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:qiraat-person-shift","source_type":"word_analysis","support_ids":["sup_8dc3a5fa40ad89b260ab","sup_d147fc3a26018d35ec12"],"title":"person marking changes stance, not structure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_4fb57069437503e1eb2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:root-branch-narrowing","source_type":"word_analysis","support_ids":["sup_8dc3a5fa40ad89b260ab","sup_a3bfc0a9914945014f95"],"title":"love branch selected over seed or social branches","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_b253b7f9b9b0e634a17c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:root-echo-and-sound","source_type":"word_analysis","support_ids":["sup_811b054774df396c1567","sup_8dc3a5fa40ad89b260ab"],"title":"love repeats as action and measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_4e064a6853f687cf61e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:2:verb-object-measure-order","source_type":"word_analysis","support_ids":["sup_4caa7d432f668c95ebe3","sup_8dc3a5fa40ad89b260ab"],"title":"disposition, target, then measure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:2","qac_refs":["89:20:1:2","89:20:1:3"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_de742d1c31003bb5f972","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:broad-object-sound","source_type":"word_analysis","support_ids":["sup_afb8c154e18dc5846669","sup_b8c7226286435f959c60"],"title":"broad object sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_df2cdf7365a9e6c7e5b6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:definite-object","source_type":"word_analysis","support_ids":["sup_08d11f98fde76365c76c","sup_afb8c154e18dc5846669"],"title":"definite accusative loved object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_b93939024b967069a9bf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:enclosed-by-love","source_type":"word_analysis","support_ids":["sup_a283d90f0600b712f8e1","sup_afb8c154e18dc5846669"],"title":"wealth enclosed by doubled love","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_fb11e531246453b3170e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:noun-not-finance-process","source_type":"word_analysis","support_ids":["sup_afb8c154e18dc5846669","sup_fca4c112db99b1121c03"],"title":"surface noun, not acquisition predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_fa1f8639ee5ae86a62ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:redirected-care-context","source_type":"word_analysis","support_ids":["sup_0099c316a89c317d4e1b","sup_afb8c154e18dc5846669"],"title":"withheld care redirected to wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:3"],"branch_refs":[],"candidate_id":"cand_cad9c24ac16617ce47b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:3:resource-field","source_type":"word_analysis","support_ids":["sup_62aea18d68d6d1a5d0d3","sup_afb8c154e18dc5846669"],"title":"wealth as controllable resource field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:3","qac_refs":["89:20:2:1","89:20:2:2"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_4b82ceeebb8182d663ca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:boundary-from-consumption","source_type":"word_analysis","support_ids":["sup_20234f71d73b973e4423","sup_d6e0d985e405d3bbc2de"],"title":"consumption pattern becomes love pattern","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_9216600a654b63f24054","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:cognate-accusative-measure","source_type":"word_analysis","support_ids":["sup_8809ce8e257b94780d07","sup_d6e0d985e405d3bbc2de"],"title":"cognate accusative measures love","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_2b96f0983195793b2a9f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:delayed-after-object","source_type":"word_analysis","support_ids":["sup_d6e0d985e405d3bbc2de","sup_f98632b203b5754c9203"],"title":"measure delayed after target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_b28ae4b2c96268c6ef51","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:gerund-branch-narrowing","source_type":"word_analysis","support_ids":["sup_5e182b2e8a9f7906e429","sup_d6e0d985e405d3bbc2de"],"title":"affective gerund over seed branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_4b97a90d96300df964c5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:head-for-final-adjective","source_type":"word_analysis","support_ids":["sup_ab8f161f3571b7bfc51a","sup_d6e0d985e405d3bbc2de"],"title":"grammatical head for final excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_44291572a7468f86874e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:indefinite-open-measure","source_type":"word_analysis","support_ids":["sup_d6e0d985e405d3bbc2de","sup_e0de4213d2c0a9cdc1c4"],"title":"indefinite love awaiting scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_e09ae38b7f378591b3fd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:love-as-affection-and-preference","source_type":"word_analysis","support_ids":["sup_cc507875bd68ba0d99df","sup_d6e0d985e405d3bbc2de"],"title":"love as feeling and priority","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_314f44dee7dd576b9813","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:root-reprise-and-sound","source_type":"word_analysis","support_ids":["sup_d4ca72edb6de05a2184e","sup_d6e0d985e405d3bbc2de"],"title":"love-root reverberation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_8ee7fddfc521246f43fb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:4:value-priority-contrast","source_type":"word_analysis","support_ids":["sup_b246bd6f2cfab12afea2","sup_d6e0d985e405d3bbc2de"],"title":"love clings instead of yielding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:4","qac_refs":["89:20:3:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_9b075bc01834559ded2c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:adjective-of-love","source_type":"word_analysis","support_ids":["sup_06799ae655ed67c68465","sup_07b99b8c75b70af9bd26"],"title":"abundance modifies love, not wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_6dd9ba187346984a5a27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:convergent-closure","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_4370f29351bb1c7afd93"],"title":"rare heavy modifier convergence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_dae7a29a3eb5e4347acd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:discourse-pivot","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_2400ba429acff95d732f"],"title":"excess answered by abrupt break","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_fa02da83dd20245c43dc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:final-position-disclosure","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_a1ad4ce7a0028374db59"],"title":"final word reveals the scale","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_468f8da9086ed2defcf8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:gathered-abundance-image","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_fa0059c01f8939c422a1"],"title":"gathered fullness as excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_cfcdeaf8705832ce4745","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:heavy-geminate-sound","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_538c43b97ce1caff8671"],"title":"heavy sealed sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_ef580ccb8967418bbac5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:qualitative-measure-form","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_7c681705c67f561b0daf"],"title":"qualitative measure completing the phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_c32f52158101440e8279","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:rare-final-pressure","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_324abd1848a2d39e88e0"],"title":"rare marked closing adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:5"],"branch_refs":[],"candidate_id":"cand_48b07257728da58f634e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:5:same-surah-accumulation-echo","source_type":"word_analysis","support_ids":["sup_07b99b8c75b70af9bd26","sup_fca44258227b797afc63"],"title":"consumption excess becomes affection excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:20:5","qac_refs":["89:20:4:1"],"status":"accepted"}},{"anchor_refs":["89:20:1"],"branch_refs":[],"candidate_id":"cand_f2e33aa7b416f2a21e0b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000286"],"scope":"focus_ayah","source_local_id":"89:20:1:2","source_type":"qac_morpheme","support_ids":["sup_43c16fdc5312b2d10641"],"title":"QAC root occurrence: ح ب ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:20:2"],"branch_refs":[],"candidate_id":"cand_ac3434c041e784e79318","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"89:20:2:2","source_type":"qac_morpheme","support_ids":["sup_9869fe3c1328a2909220"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:20:4"],"branch_refs":[],"candidate_id":"cand_56306889ff5a81ef7523","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000261"],"scope":"focus_ayah","source_local_id":"89:20:4:1","source_type":"qac_morpheme","support_ids":["sup_3dd30adc871644ff8201"],"title":"QAC root occurrence: ج م م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:20","branch_refs":["root_000261/B001","root_000286/B002","root_001457/B001"],"candidate_id":"cand_2e44a647ba80a0a1b00c","commentary_obligation":"review","hft_ref":"hft_89d434df93d3a946393d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_attachment_fullness","source_type":"hft","support_ids":["sup_e0d2cb9d95b3280c98e3"],"title":"base_attachment_fullness","trust":"legacy_unbound"},{"anchor_refs":["89:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:20","branch_refs":["root_000261/B003","root_000286/B003","root_001457/B001"],"candidate_id":"cand_05458f7947e967787ba4","commentary_obligation":"review","hft_ref":"hft_f4af861a78ab9c0fd923","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_public_valuation_mass","source_type":"hft","support_ids":["sup_56d989c3579557b90075"],"title":"base_public_valuation_mass","trust":"legacy_unbound"},{"anchor_refs":["89:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:20","branch_refs":["root_000261/B002","root_000286/B005","root_000286/B006"],"candidate_id":"cand_b669b627254226f5a0db","commentary_obligation":"review","hft_ref":"hft_9d5aaf75dd42bf0a607a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_stuck_satiation","source_type":"hft","support_ids":["sup_1d76b90172560ca8ae8a"],"title":"base_stuck_satiation","trust":"legacy_unbound"},{"anchor_refs":["89:20"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:20","branch_refs":["root_000261/B005","root_000286/B001","root_001457/B001"],"candidate_id":"cand_1e3635f4a00aae40f812","commentary_obligation":"review","hft_ref":"hft_ac151f2f5b03a10ee542","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_seed_stock_growth","source_type":"hft","support_ids":["sup_30532e533a0ec594e9ed"],"title":"base_seed_stock_growth","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:20:1:1","qac_word_ref":"89:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","root_ar":"ح ب ب","surface_ar":"تُحِبُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:20:1:3","qac_word_ref":"89:20:1","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:20:2:1","qac_word_ref":"89:20:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:2:2","qac_word_ref":"89:20:2","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","root_ar":"ح ب ب","surface_ar":"حُبًّا"},{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","root_ar":"ج م م","surface_ar":"جَمًّا"}],"word_analysis_qac_refs":[["89:20:1:1"],["89:20:1:2","89:20:1:3"],["89:20:2:1","89:20:2:2"],["89:20:3:1"],["89:20:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:20:1","89:20:2","89:20:3","89:20:4","89:20:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:20:1:1","qac_word_ref":"89:20:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَحْبَبْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:20:1:2","qac_word_ref":"89:20:1","root_ar":"ح ب ب","surface_ar":"تُحِبُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:20:1:3","qac_word_ref":"89:20:1","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:20:2:1","qac_word_ref":"89:20:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:2:2","qac_word_ref":"89:20:2","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"حُبّ","morph_features":"STEM|POS:N|LEM:Hub~|ROOT:Hbb|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:20:3:1","qac_word_ref":"89:20:3","root_ar":"ح ب ب","surface_ar":"حُبًّا"},{"lemma_ar":"جَمّ","morph_features":"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:20:4:1","qac_word_ref":"89:20:4","root_ar":"ج م م","surface_ar":"جَمًّا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:20:1:1"],["89:20:1:2","89:20:1:3"],["89:20:2:1","89:20:2:2"],["89:20:3:1"],["89:20:4:1"]],"word_analysis_refs":["89:20:1","89:20:2","89:20:3","89:20:4","89:20:5"],"word_rows":[{"analysis_record_ref":"89:20:1","analytic_gloss_range_en":"coordinating continuation that adds the wealth-love clause to the same charge sequence without making it a later event","analytic_root_gloss_range_en":null,"qac_refs":["89:20:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:20:2","analytic_gloss_range_en":"ongoing plural-directed love as affective preference and value ranking toward wealth","analytic_root_gloss_range_en":"root range includes love, affection, preference, belovedness, seed or kernel imagery, and other remote branches; this verb selects the love/preference branch while concrete seed senses remain non-operative contrast","qac_refs":["89:20:1:2","89:20:1:3"],"root":{"arabic":"ح ب ب","transliteration":"ḥ-b-b"},"surface":{"arabic":"تُحِبُّونَ","transliteration":"tuḥibbūna"}},{"analysis_record_ref":"89:20:3","analytic_gloss_range_en":"definite wealth as the direct object: the recognizable field of owned, controllable value loved by the addressees","analytic_root_gloss_range_en":"root range centers wealth, property, possession, acquisition, and material means; the local noun selects owned value rather than a finance process or unrelated review branch","qac_refs":["89:20:2:1","89:20:2:2"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"ٱلْمَالَ","transliteration":"al-māla"}},{"analysis_record_ref":"89:20:4","analytic_gloss_range_en":"indefinite cognate verbal noun naming and measuring the loving itself before its final excess qualifier","analytic_root_gloss_range_en":"root range includes love, affection, preference, belovedness, intimacy, seed or kernel imagery, and other remote branches; the local gerund selects the love/preference noun field","qac_refs":["89:20:3:1"],"root":{"arabic":"ح ب ب","transliteration":"ḥ-b-b"},"surface":{"arabic":"حُبًّۭا","transliteration":"ḥubban"}},{"analysis_record_ref":"89:20:5","analytic_gloss_range_en":"final accusative adjective qualifying the love as gathered, copious, heaped, and excessive","analytic_root_gloss_range_en":"root range includes gathered abundance, fullness, crowding, recovery, nearness, and other branches; this adjective selects the abundant gathered-fullness branch as a qualifier of love","qac_refs":["89:20:4:1"],"root":{"arabic":"ج م م","transliteration":"j-m-m"},"surface":{"arabic":"جَمًّۭا","transliteration":"jamman"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:20"],"branch_refs":["root_000261/B001","root_000286/B002","root_001457/B001"],"candidate_id":"cand_2e44a647ba80a0a1b00c","evidence_scope":"focus_ayah","hft_ref":"hft_89d434df93d3a946393d","item_id":"base_attachment_fullness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_attachment_fullness","support_id":"sup_e0d2cb9d95b3280c98e3"},{"anchor_refs":["89:20"],"branch_refs":["root_000261/B003","root_000286/B003","root_001457/B001"],"candidate_id":"cand_05458f7947e967787ba4","evidence_scope":"focus_ayah","hft_ref":"hft_f4af861a78ab9c0fd923","item_id":"base_public_valuation_mass","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_public_valuation_mass","support_id":"sup_56d989c3579557b90075"},{"anchor_refs":["89:20"],"branch_refs":["root_000261/B002","root_000286/B005","root_000286/B006"],"candidate_id":"cand_b669b627254226f5a0db","evidence_scope":"focus_ayah","hft_ref":"hft_9d5aaf75dd42bf0a607a","item_id":"base_stuck_satiation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_stuck_satiation","support_id":"sup_1d76b90172560ca8ae8a"},{"anchor_refs":["89:20"],"branch_refs":["root_000261/B005","root_000286/B001","root_001457/B001"],"candidate_id":"cand_1e3635f4a00aae40f812","evidence_scope":"focus_ayah","hft_ref":"hft_ac151f2f5b03a10ee542","item_id":"base_seed_stock_growth","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_seed_stock_growth","support_id":"sup_30532e533a0ec594e9ed"}],"diagnostics":[],"lane_counts":{"global":13,"macro":7,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:20","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:20","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"89:20","lane":"micro","linguistic_source_ref":"89:20","surface_ref":"89:20","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:20","target_tokens":[["Malı",["89:20:2"]],["da",["89:20:1"]],["çok",["89:20:4"]],["büyük",["89:20:4"]],["bir",["89:20:3"]],["sevgiyle",["89:20:3"]],["seviyorsunuz",["89:20:1"]]],"text":"Malı da çok büyük bir sevgiyle seviyorsunuz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:redirected-care-context","source_type":"word_analysis","support_id":"sup_0099c316a89c317d4e1b","text":"{\"blocking_evidence\":null,\"headline\":\"withheld care redirected to wealth\",\"reader_payoff\":\"The reader sees how the preceding failures toward orphan, poor, and inheritance are explained by a broader object of attachment.\",\"reason\":\"The final coordinated charge follows the earlier economic accusations and names the broad wealth field that competes with vulnerable claims.\",\"representative_source_ids\":[\"QI-22764ebd\",\"MI-e871e0fe\",\"QB-02c842ba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:adjective-of-love","source_type":"word_analysis","support_id":"sup_06799ae655ed67c68465","text":"{\"blocking_evidence\":null,\"headline\":\"abundance modifies love, not wealth\",\"reader_payoff\":\"The reader notices that the ayah condemns accumulated attachment, not merely possession of a large quantity of wealth.\",\"reason\":\"The word is an indefinite accusative masculine adjective qualifying the preceding indefinite accusative love noun.\",\"representative_source_ids\":[\"QG-af4dd528\",\"QG-b885a70b\",\"MG-49471e4a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5","source_type":"word_analysis","support_id":"sup_07b99b8c75b70af9bd26","text":"{\"gloss_range\":\"final accusative adjective qualifying the love as gathered, copious, heaped, and excessive\",\"prose\":\"{{ar:جَمًّۭا}} ({{tr:jamman}}) is the final adjective of {{ar:حُبًّۭا}} ({{tr:ḥubban}}), so the abundance belongs to the love and not directly to the amount of property. Its root pressure pictures excess as gathered fullness: piled, massed, overflowing attachment rather than merely strong emotion. Because it closes the ayah, the last pressure left in the ear is not wealth alone but love accumulated beyond measure. The same-surah pattern with the prior intensified consumption phrase in 89:19 makes the final word a motive-level handoff: what was swept together in action is now heaped up in affection. Its rarity, doubled consonant, and matching accusative ending with {{ar:حُبًّۭا}} ({{tr:ḥubban}}) make the closure feel grammatically sealed and heavy before the abrupt break in 89:21.\",\"root_display\":\"{{ar:ج م م}} ({{tr:j-m-m}})\",\"root_gloss_range\":\"root range includes gathered abundance, fullness, crowding, recovery, nearness, and other branches; this adjective selects the abundant gathered-fullness branch as a qualifier of love\",\"surface_display\":\"{{ar:جَمًّۭا}} ({{tr:jamman}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:communal-ongoing-address","source_type":"word_analysis","support_id":"sup_0881a9c245341e16ad2a","text":"{\"blocking_evidence\":null,\"headline\":\"ongoing plural accusation\",\"reader_payoff\":\"The reader notices that love of wealth is charged as a shared continuing disposition, not as one isolated private act.\",\"reason\":\"The verb is Form IV imperfect indicative active with second-person plural agreement and a morphologically present plural subject.\",\"representative_source_ids\":[\"QG-264b31f6\",\"QG-6381af05\",\"MG-07922d7d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:definite-object","source_type":"word_analysis","support_id":"sup_08d11f98fde76365c76c","text":"{\"blocking_evidence\":null,\"headline\":\"definite accusative loved object\",\"reader_payoff\":\"The reader notices that wealth is the grammatical target of love and a recognizable class-category, not just one fortune.\",\"reason\":\"The noun is definite masculine singular accusative and is syntactically forced as the direct object of the love verb.\",\"representative_source_ids\":[\"QG-0e3520cd\",\"QG-d089adb3\",\"QG-f6d4d152\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:1:prefixed-opening","source_type":"word_analysis","support_id":"sup_0b4ee53c3de5f010bd95","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed connector fused to accusation\",\"reader_payoff\":\"The reader hears the ayah open as continuation plus verbal accusation, with no pause for a new scene marker or named subject.\",\"reason\":\"The particle is a rootless clitic conjunction split from the attached finite verb, so its force is grammatical continuation.\",\"representative_source_ids\":[\"QF-398226f9\",\"QF-48446300\",\"QT-b12bc9c2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:boundary-from-consumption","source_type":"word_analysis","support_id":"sup_20234f71d73b973e4423","text":"{\"blocking_evidence\":null,\"headline\":\"consumption pattern becomes love pattern\",\"reader_payoff\":\"The reader sees the prior pattern of excessive consumption recast as excessive affection, joining outward appropriation to inward attachment.\",\"reason\":\"The same masdar-plus-intensifier architecture carries from the previous economic charge into the love phrase.\",\"representative_source_ids\":[\"QB-81179808\",\"QB-ad96daf9\",\"QY-b9b7212f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:discourse-pivot","source_type":"word_analysis","support_id":"sup_2400ba429acff95d732f","text":"{\"blocking_evidence\":null,\"headline\":\"excess answered by abrupt break\",\"reader_payoff\":\"The reader sees the final heaped-love diagnosis set up the abrupt negating break that follows in 89:21.\",\"reason\":\"The row family links the accumulated-love closure to the preceding excess pattern and the following discourse pivot.\",\"representative_source_ids\":[\"QB-50156620\",\"QB-6f2adf68\",\"QB-bd59c377\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:1:same-addressee-bridge","source_type":"word_analysis","support_id":"sup_309b3b0cfbf4f32a1e12","text":"{\"blocking_evidence\":null,\"headline\":\"same audience carried into motive\",\"reader_payoff\":\"The reader sees no change of audience between the outward economic charges and the inward wealth-love charge.\",\"reason\":\"The following verb carries second-person plural agreement, continuing the direct addressee chain.\",\"representative_source_ids\":[\"QT-f0636d83\",\"QB-05b0f456\",\"QB-842a9fc1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:rare-final-pressure","source_type":"word_analysis","support_id":"sup_324abd1848a2d39e88e0","text":"{\"blocking_evidence\":null,\"headline\":\"rare marked closing adjective\",\"reader_payoff\":\"The reader treats the final qualifier as specially marked rather than a routine intensifier.\",\"reason\":\"The contextual evidence marks this exact root-form as a singleton here, supporting the CRITICAL rarity payoff.\",\"representative_source_ids\":[\"QH-40787a2c\",\"QH-5fcdff13\",\"MH-f9671e08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:20:4:1","source_type":"qac_morpheme","support_id":"sup_3dd30adc871644ff8201","text":"{\"lemma_ar\":\"جَمّ\",\"morph_features\":\"STEM|POS:ADJ|LEM:jam~|ROOT:jmm|MS|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"89:20:4:1\",\"qac_word_ref\":\"89:20:4\",\"root_ar\":\"ج م م\",\"surface_ar\":\"جَمًّا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:convergent-closure","source_type":"word_analysis","support_id":"sup_4370f29351bb1c7afd93","text":"{\"blocking_evidence\":null,\"headline\":\"rare heavy modifier convergence\",\"reader_payoff\":\"The reader sees rarity, grammar, sound, and final position converge on one closing image of accumulated attachment.\",\"reason\":\"The final word modifies the repeated love-root noun, shares its accusative ending, and closes the ayah with the rare gathered-abundance adjective.\",\"representative_source_ids\":[\"ME-a93c64cd\",\"QP-fef3b76b\",\"QY-f723e8fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:20:1:2","source_type":"qac_morpheme","support_id":"sup_43c16fdc5312b2d10641","text":"{\"lemma_ar\":\"أَحْبَبْ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:>aHobabo|ROOT:Hbb|2MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:20:1:2\",\"qac_word_ref\":\"89:20:1\",\"root_ar\":\"ح ب ب\",\"surface_ar\":\"تُحِبُّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:1:accumulating-rebuke-cadence","source_type":"word_analysis","support_id":"sup_4aa072369db9cdfc69be","text":"{\"blocking_evidence\":null,\"headline\":\"accumulating rebuke cadence\",\"reader_payoff\":\"The reader feels the short connector as part of an accumulating rebuke whose sound runs straight into the love verb.\",\"reason\":\"The row family adds a sound-and-boundary payoff without contradicting the grammatical conjunction analysis.\",\"representative_source_ids\":[\"MT-18b146cc\",\"QP-255e3d67\",\"QB-ea3afd5a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:1","source_type":"word_analysis","support_id":"sup_4b17e2fc7422dd79cbd3","text":"{\"gloss_range\":\"coordinating continuation that adds the wealth-love clause to the same charge sequence without making it a later event\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not restart the scene. It fastens the whole wealth-love clause to the earlier accusations as another coordinate charge, so the reader hears motive being added to public economic failure rather than a new episode beginning. Because it is prefixed to {{ar:تُحِبُّونَ}} ({{tr:tuḥibbūna}}), continuation and accusation arrive together with no new scene marker or named subject. The short connector also keeps the rebuke accumulating in sound and syntax, carrying the same addressed plural from the inheritance-devouring charge into the love-of-wealth diagnosis.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:verb-object-measure-order","source_type":"word_analysis","support_id":"sup_4caa7d432f668c95ebe3","text":"{\"blocking_evidence\":null,\"headline\":\"disposition, target, then measure\",\"reader_payoff\":\"The reader experiences the diagnosis step by step: the loving is exposed, then the target appears, then the measure intensifies it.\",\"reason\":\"The local word order places the finite verb before the explicit object and the cognate accusative.\",\"representative_source_ids\":[\"QT-335fb5c5\",\"QT-ecd130e0\",\"MT-f42c5d14\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:heavy-geminate-sound","source_type":"word_analysis","support_id":"sup_538c43b97ce1caff8671","text":"{\"blocking_evidence\":null,\"headline\":\"heavy sealed sound\",\"reader_payoff\":\"The reader hears the doubled closing consonant and matching accusative ending compress the image of massed abundance.\",\"reason\":\"The phonetic rows support the local semantic image and final-position effect without claiming an independent grammar.\",\"representative_source_ids\":[\"QP-7f212d96\",\"QP-d7e30297\",\"MP-73f7906f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:gerund-branch-narrowing","source_type":"word_analysis","support_id":"sup_5e182b2e8a9f7906e429","text":"{\"blocking_evidence\":null,\"headline\":\"affective gerund over seed branch\",\"reader_payoff\":\"The reader keeps the noun's affective force while recognizing that remote concrete seed branches are only contrastive background here.\",\"reason\":\"The local form is a gerund functioning as a cognate accusative after the finite love verb, selecting the affective verbal-noun register.\",\"representative_source_ids\":[\"QF-4d5dd28c\",\"QF-58905ab6\",\"QF-61243057\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:resource-field","source_type":"word_analysis","support_id":"sup_62aea18d68d6d1a5d0d3","text":"{\"blocking_evidence\":null,\"headline\":\"wealth as controllable resource field\",\"reader_payoff\":\"The reader sees the charge reach the full field of controllable value rather than only money.\",\"reason\":\"The accepted root branch centers wealth, property, possession, livestock, and material means, and no local evidence narrows the object to cash.\",\"representative_source_ids\":[\"QS-2d104e8d\",\"QS-4cff4394\",\"MS-138cedbe\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:directed-value-target","source_type":"word_analysis","support_id":"sup_6c3c3be417ba5eb633e7","text":"{\"blocking_evidence\":null,\"headline\":\"directed preference toward wealth\",\"reader_payoff\":\"The reader sees wealth named as the chosen target of affective valuation, not wealth merely existing near the addressees.\",\"reason\":\"The local frame gives the verb an explicit direct object, and the accepted root branch supports love, preference, and holding dear.\",\"representative_source_ids\":[\"QG-7a703f54\",\"QS-55f88630\",\"QF-96af8696\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:qualitative-measure-form","source_type":"word_analysis","support_id":"sup_7c681705c67f561b0daf","text":"{\"blocking_evidence\":null,\"headline\":\"qualitative measure completing the phrase\",\"reader_payoff\":\"The reader sees the word complete the cognate accusative phrase as a quality of the measured love rather than as a new action.\",\"reason\":\"The local form is tagged as a qualitative adjective, not as a second verbal noun.\",\"representative_source_ids\":[\"QF-60a47e48\",\"QF-d1a0b476\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:root-echo-and-sound","source_type":"word_analysis","support_id":"sup_811b054774df396c1567","text":"{\"blocking_evidence\":null,\"headline\":\"love repeats as action and measure\",\"reader_payoff\":\"The reader hears attachment become unavoidable because the same root returns from the verb into the measuring noun.\",\"reason\":\"The following cognate accusative repeats the same root, and the sound rows reinforce that grammatical mechanism.\",\"representative_source_ids\":[\"QE-287042ed\",\"QE-a1d3ee42\",\"QP-7a9408e3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:motive-after-economic-failure","source_type":"word_analysis","support_id":"sup_82d66fc09d1068a62859","text":"{\"blocking_evidence\":null,\"headline\":\"motive follows outward failure\",\"reader_payoff\":\"The reader sees the clause move from visible failures around feeding and inheritance into the inward preference that explains them.\",\"reason\":\"The coordinated sequence and explicit object allow the row family to function as a discourse bridge from earlier economic charges to motive.\",\"representative_source_ids\":[\"QI-c21b2dcf\",\"MI-991af62f\",\"QB-eede64ed\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:cognate-accusative-measure","source_type":"word_analysis","support_id":"sup_8809ce8e257b94780d07","text":"{\"blocking_evidence\":null,\"headline\":\"cognate accusative measures love\",\"reader_payoff\":\"The reader notices that the word does not add another object but turns the act of loving into a measured event.\",\"reason\":\"The noun repeats the verb root as an indefinite accusative verbal noun functioning as a cognate accusative.\",\"representative_source_ids\":[\"QG-01a000a7\",\"QG-8c7947e5\",\"MG-19c9ee06\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2","source_type":"word_analysis","support_id":"sup_8dc3a5fa40ad89b260ab","text":"{\"gloss_range\":\"ongoing plural-directed love as affective preference and value ranking toward wealth\",\"prose\":\"{{ar:تُحِبُّونَ}} ({{tr:tuḥibbūna}}) makes the charge communal and ongoing: the addressees themselves keep directing preference toward {{ar:ٱلْمَالَ}} ({{tr:al-māla}}). The Form IV love branch is not a vague feeling here; with an explicit object it names wealth as the chosen value target, emotionally dear and practically ranked, while remote seed or social-affection branches stay outside this verb frame. After the failure to urge feeding in 89:18 and the devouring of inheritance in 89:19, this first lexical action exposes the motive: a value-priority construction in which outward exploitation and inward desire belong to one continuous accusation. The verb then receives its own cognate measure in {{ar:حُبًّۭا}} ({{tr:ḥubban}}), so love is heard first as action and then as a measured state before {{ar:جَمًّۭا}} ({{tr:jamman}}) names its excess. The reported person-prefix variant shifts the stance from direct confrontation to third-person exposure, but the same verb, object, and cognate-measure structure remain.\",\"root_display\":\"{{ar:ح ب ب}} ({{tr:ḥ-b-b}})\",\"root_gloss_range\":\"root range includes love, affection, preference, belovedness, seed or kernel imagery, and other remote branches; this verb selects the love/preference branch while concrete seed senses remain non-operative contrast\",\"surface_display\":\"{{ar:تُحِبُّونَ}} ({{tr:tuḥibbūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:20:2:2","source_type":"qac_morpheme","support_id":"sup_9869fe3c1328a2909220","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:20:2:2\",\"qac_word_ref\":\"89:20:2\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:1:coordinate-charge","source_type":"word_analysis","support_id":"sup_98bcf7c0292a8e070f00","text":"{\"blocking_evidence\":null,\"headline\":\"coordinate continuation, not chronology\",\"reader_payoff\":\"The reader notices that the final clause is another member of the same indictment rather than a later event in a sequence.\",\"reason\":\"The aligned word is a coordinating conjunction, and the local clause is marked as a coordinated verbal charge.\",\"representative_source_ids\":[\"QG-51f33ef3\",\"QG-54f6617e\",\"QS-9fa9ee64\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:final-position-disclosure","source_type":"word_analysis","support_id":"sup_a1ad4ce7a0028374db59","text":"{\"blocking_evidence\":null,\"headline\":\"final word reveals the scale\",\"reader_payoff\":\"The reader waits until the last word to learn that the measured love is accumulated excess.\",\"reason\":\"The adjective is postposed after the cognate noun and is the closing word of the ayah.\",\"representative_source_ids\":[\"QT-078456f2\",\"QT-80bad208\",\"MT-6b3f1c03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:enclosed-by-love","source_type":"word_analysis","support_id":"sup_a283d90f0600b712f8e1","text":"{\"blocking_evidence\":null,\"headline\":\"wealth enclosed by doubled love\",\"reader_payoff\":\"The reader notices wealth placed between the love action and the love measure, making it the center of doubled attachment.\",\"reason\":\"The object sits after the finite love verb and before the cognate accusative that intensifies that same verb.\",\"representative_source_ids\":[\"QT-7325656a\",\"QE-9ee24cde\",\"ME-84350e0f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:root-branch-narrowing","source_type":"word_analysis","support_id":"sup_a3bfc0a9914945014f95","text":"{\"blocking_evidence\":null,\"headline\":\"love branch selected over seed or social branches\",\"reader_payoff\":\"The reader keeps the force of ranked dearness while avoiding import of remote root branches into this verb frame.\",\"reason\":\"The local Form IV affective syntax selects the love/preference branch; seed, ingratiating, and other remote branches are not locally licensed.\",\"representative_source_ids\":[\"QS-0a84092c\",\"QS-36ba5a6b\",\"QF-f6c45a6c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:head-for-final-adjective","source_type":"word_analysis","support_id":"sup_ab8f161f3571b7bfc51a","text":"{\"blocking_evidence\":null,\"headline\":\"grammatical head for final excess\",\"reader_payoff\":\"The reader sees that the final abundance belongs grammatically to the love, because this noun creates the exact slot for the adjective.\",\"reason\":\"The following accusative adjective agrees with and qualifies this verbal noun.\",\"representative_source_ids\":[\"QG-21703eb9\",\"QG-c3ee474d\",\"QT-d7ef9b53\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3","source_type":"word_analysis","support_id":"sup_afb8c154e18dc5846669","text":"{\"gloss_range\":\"definite wealth as the direct object: the recognizable field of owned, controllable value loved by the addressees\",\"prose\":\"{{ar:ٱلْمَالَ}} ({{tr:al-māla}}) is the accusative object of {{ar:تُحِبُّونَ}} ({{tr:tuḥibbūna}}), so the diagnosis is not desire in general but attachment fastening onto wealth. Its definiteness gathers wealth into a recognizable class of owned value, wider than coin or cash: property, possessions, goods, assets, and usable means can all stand inside the object field. The surface noun names already-objectified value rather than making acquisition, funding, or a merely financial relation the predicate, keeping the diagnostic focus on what has become beloved. After the failures toward orphan, poor, and inheritance in 89:17-19, this broad object field shows where withheld care has been redirected. Placed between the love verb and {{ar:حُبًّۭا}} ({{tr:ḥubban}}), wealth is caught inside doubled love language; the target is named first, then the clause reveals how swollen the love is.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"root range centers wealth, property, possession, acquisition, and material means; the local noun selects owned value rather than a finance process or unrelated review branch\",\"surface_display\":\"{{ar:ٱلْمَالَ}} ({{tr:al-māla}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:value-priority-contrast","source_type":"word_analysis","support_id":"sup_b246bd6f2cfab12afea2","text":"{\"blocking_evidence\":null,\"headline\":\"love clings instead of yielding\",\"reader_payoff\":\"The reader sees the love noun belong to a value-priority field where love can either be overcome in giving or cling possessively to wealth.\",\"reason\":\"The CRITICAL row gives a concrete contrast with giving despite love for the food (76:8), while the local phrase keeps love attached to wealth.\",\"representative_source_ids\":[\"QI-22326bf0\",\"MI-9debc9e9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:broad-object-sound","source_type":"word_analysis","support_id":"sup_b8c7226286435f959c60","text":"{\"blocking_evidence\":null,\"headline\":\"broad object sound\",\"reader_payoff\":\"The reader hears the marked object broaden the clause between compressed love forms while remaining syntactically governed by the verb.\",\"reason\":\"The sound rows reinforce, rather than replace, the grammatical object and definiteness payoff.\",\"representative_source_ids\":[\"QP-372557ab\",\"QP-55106563\",\"QY-3cc3b00e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:love-as-affection-and-preference","source_type":"word_analysis","support_id":"sup_cc507875bd68ba0d99df","text":"{\"blocking_evidence\":null,\"headline\":\"love as feeling and priority\",\"reader_payoff\":\"The reader notices that the noun names both inward affection and practical valuation rather than mere emotional intensity.\",\"reason\":\"The accepted love branch covers affection, preference, being dear, and attachment, and the local phrase applies that field to wealth-love.\",\"representative_source_ids\":[\"QS-25fdb5e4\",\"QS-5ba89232\",\"QS-6ca756ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:2:qiraat-person-shift","source_type":"word_analysis","support_id":"sup_d147fc3a26018d35ec12","text":"{\"blocking_evidence\":null,\"headline\":\"person marking changes stance, not structure\",\"reader_payoff\":\"The reader notices that person morphology controls whether the rebuke confronts the audience or exposes them, while the wealth-love pattern stays intact.\",\"reason\":\"The canonical aligned surface is second person plural, while the reported third-person variant is useful as stance contrast rather than replacement of the local parse.\",\"representative_source_ids\":[\"QG-6fef75b1\",\"QF-79aa8191\",\"MI-2347274c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:root-reprise-and-sound","source_type":"word_analysis","support_id":"sup_d4ca72edb6de05a2184e","text":"{\"blocking_evidence\":null,\"headline\":\"love-root reverberation\",\"reader_payoff\":\"The reader hears the love-root repeat so that attachment becomes both action and compact noun before the final intensifier expands it.\",\"reason\":\"The same root occurs in the finite verb and the cognate verbal noun; the sound rows reinforce that local repetition.\",\"representative_source_ids\":[\"QE-13c3f618\",\"QE-ab84bb03\",\"QP-620df6b7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4","source_type":"word_analysis","support_id":"sup_d6e0d985e405d3bbc2de","text":"{\"gloss_range\":\"indefinite cognate verbal noun naming and measuring the loving itself before its final excess qualifier\",\"prose\":\"{{ar:حُبًّۭا}} ({{tr:ḥubban}}) is the cognate accusative of {{ar:تُحِبُّونَ}} ({{tr:tuḥibbūna}}), not a second loved object. It repeats the act as a named measure, turning love for {{ar:ٱلْمَالَ}} ({{tr:al-māla}}) into something inspectable and excessive in quantity or kind. Its indefiniteness leaves the measure open until {{ar:جَمًّۭا}} ({{tr:jamman}}) qualifies it, so the final phrase diagnoses both inward attachment and practical preference. The same root has remote seed and kernel branches, but this gerund stays in the affective love field while letting the repeated sound make attachment answer itself. Because the measure comes after the wealth object, the target appears first and then love closes back over it as intensified state. The contrast with giving food despite love for it (76:8) sharpens the reversal: here love clings to wealth, and the intensified consumption pattern of 89:19 is recast as intensified affection.\",\"root_display\":\"{{ar:ح ب ب}} ({{tr:ḥ-b-b}})\",\"root_gloss_range\":\"root range includes love, affection, preference, belovedness, intimacy, seed or kernel imagery, and other remote branches; the local gerund selects the love/preference noun field\",\"surface_display\":\"{{ar:حُبًّۭا}} ({{tr:ḥubban}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:indefinite-open-measure","source_type":"word_analysis","support_id":"sup_e0de4213d2c0a9cdc1c4","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite love awaiting scale\",\"reader_payoff\":\"The reader feels a notable kind or quantity of love opened before the last word specifies its excess.\",\"reason\":\"The word is an indefinite accusative verbal noun followed by an indefinite accusative adjective.\",\"representative_source_ids\":[\"QS-6ea18e86\",\"MS-31843c2d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:4:delayed-after-object","source_type":"word_analysis","support_id":"sup_f98632b203b5754c9203","text":"{\"blocking_evidence\":null,\"headline\":\"measure delayed after target\",\"reader_payoff\":\"The reader first sees the target, then hears the love close back over it as an intensified measure.\",\"reason\":\"The cognate accusative follows the explicit object rather than immediately following the verb.\",\"representative_source_ids\":[\"QT-05027785\",\"MT-b5c9edf5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:gathered-abundance-image","source_type":"word_analysis","support_id":"sup_fa0059c01f8939c422a1","text":"{\"blocking_evidence\":null,\"headline\":\"gathered fullness as excess\",\"reader_payoff\":\"The reader imagines the love as a gathered mass of excess rather than a flat synonym for intensity.\",\"reason\":\"The accepted branch of the root supports abundant gathered fullness, while other branches such as recovery, nearness, or hornlessness are not activated by this local adjective.\",\"representative_source_ids\":[\"QS-374007d9\",\"QS-43afa401\",\"MS-85d31fae\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:5:same-surah-accumulation-echo","source_type":"word_analysis","support_id":"sup_fca44258227b797afc63","text":"{\"blocking_evidence\":null,\"headline\":\"consumption excess becomes affection excess\",\"reader_payoff\":\"The reader sees the prior intensified consumption pattern in 89:19 transformed into an intensified love pattern in 89:20.\",\"reason\":\"The row family explicitly ties the final phrase to the previous ayah's masdar-plus-intensifier architecture and accumulation semantics.\",\"representative_source_ids\":[\"QI-a145fd01\",\"QE-156908e8\",\"QY-1a4a3978\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:20:3:noun-not-finance-process","source_type":"word_analysis","support_id":"sup_fca4c112db99b1121c03","text":"{\"blocking_evidence\":null,\"headline\":\"surface noun, not acquisition predicate\",\"reader_payoff\":\"The reader keeps the asset and possession pressure while seeing that the ayah names wealth itself rather than narrating acquisition or funding.\",\"reason\":\"The local form is a concrete noun in the object slot; derived acquisition and finance possibilities remain adjacent background, not the selected predicate.\",\"representative_source_ids\":[\"QS-cde88d11\",\"QF-54715111\",\"QF-f2262057\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000261/B001","root_000286/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000286","role":"Love as clinging attachment supplies the affective bond that keeps the subject oriented toward wealth.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquiring and possessing wealth supplies the repeatable material process on which attachment can act.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000261","role":"Gathered abundance filling a measure turns the terminal qualifier into saturation rather than a bare degree word.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"The clause diagnoses a clinging attachment whose acquisition keeps gathering until wealth and desire alike press toward fullness.","before":"You like wealth very much."},"confidence":"strong","focus_anchor":"The repeated ح ب ب at words 1 and 3 encloses wealth at word 2, while جَمًّا at word 4 qualifies the enacted love.","mechanism":"Clinging attachment drives acquisition, and acquisition feeds a gathered fullness. The cognate verb-noun repetition makes desire itself accumulate alongside its object, so abundance describes both the wealth and the affective pressure around it.","model_id":"base_attachment_fullness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_attachment_fullness","source_type":"hft","support_id":"sup_e0d2cb9d95b3280c98e3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000261/B003","root_000286/B003","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000286","role":"A formula of approval and utmost desire lets love function as social commendation, not only inward feeling.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Wealth as acquired possession supplies the publicly legible object around which valuation can converge.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000261","role":"A massed crowd or inclusive group gives the plural love a collective body.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"The plural community collectively ratifies wealth as desirable, making its love a socially self-reinforcing valuation regime.","before":"Many individuals happen to love wealth."},"confidence":"medium","focus_anchor":"The second-person plural subject, the approval branch of ح ب ب, and the collective branch of ج م م all remain attached to loving wealth.","mechanism":"A plural audience does not merely share many private desires; it can form a crowd that approves wealth as the common measure of what deserves desire. Public commendation and collective massing reinforce one another.","model_id":"base_public_valuation_mass"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_public_valuation_mass","source_type":"hft","support_id":"sup_56d989c3579557b90075","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000261/B002","root_000286/B005","root_000286/B006"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000286","role":"An exhausted animal fixed in place supplies the surprising image of desire becoming immobilization.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B006","mapped_root_id":"root_000286","role":"Filling a vessel or drinker to repletion supplies the promise of satiation that keeps acquisition running.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B002","mapped_root_id":"root_000261","role":"Rest and recovered strength supply the repose wealth-love seeks but may fail to deliver.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"The pursuit is also a self-stalling search for satiation: it promises replenishment while fastening the lover to the place of exhaustion.","before":"Intense love energetically drives the pursuit of wealth."},"confidence":"exploratory","focus_anchor":"The focus repeats ح ب ب and closes with جَمًّا, allowing secondary branches of fixity, filling, and recovery to remain tethered to the clause's attachment and intensity.","mechanism":"Wealth promises to fill and rest the desiring subject, yet the attachment can fix that subject in place like an exhausted animal. The desired satiation and the resulting incapacity coexist as two sides of the same possessive loop.","model_id":"base_stuck_satiation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_stuck_satiation","source_type":"hft","support_id":"sup_1d76b90172560ca8ae8a","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا","ayah_ref":"89:20"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000261/B005","root_000286/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000286","role":"A carried seed-grain supplies a small unit whose value lies in storage and multiplication.","root":"ح ب ب","source_ref":"89:20","source_word_indices":["1","3"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquired property turns the seed image into capital held for increase.","root":"م و ل","source_ref":"89:20","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000261","role":"Clustered young herbage supplies growth gathered before fruition, making the abundance anticipatory.","root":"ج م م","source_ref":"89:20","source_word_indices":["4"]}],"changed_reading":{"after":"It can also expose attachment to wealth as reproductive potential, loving the stored kernel for the future increase imagined inside it.","before":"The clause condemns attachment to a large present quantity."},"confidence":"exploratory","focus_anchor":"The seed branch of ح ب ب, the acquisition branch of م و ل, and the clustered young-growth branch of ج م م all arise from roots present in the focus ayah.","mechanism":"Wealth is loved as seed stock: a carried kernel valued less for present use than for its capacity to multiply. The gathered but not yet mature vegetation image makes abundance prospective, converting possession into imagined future growth.","model_id":"base_seed_stock_growth"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_seed_stock_growth","source_type":"hft","support_id":"sup_30532e533a0ec594e9ed","trust":"legacy_unbound"}]}
</lane_packet_json>
