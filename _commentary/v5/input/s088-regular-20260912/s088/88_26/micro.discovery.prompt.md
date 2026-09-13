# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:26**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_26/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:26",
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
{"branch_registry":[{"boundary":"Çekirdek, sayı yoluyla nicelik belirlemektir; sanma, yeterlik ve yalnızca belirli söz öbeklerinde doğan sınırsız verme anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_a4e0fe6ca1974e8d2796","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"sayarak nicelik belirleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesneler tek tek sayılır ve nicelikleri sayı kullanılarak belirlenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneş ile ayın hareketleri, bilinen ve belirlenmiş bir sayı düzeni içinde ele alınır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnelerin sayılması ve sayı düzeniyle ölçünün ortaya çıkarılması anlatılırken kullanılır.","boundary_detail":"Çekirdek, sayı yoluyla nicelik belirlemektir; sanma, yeterlik ve yalnızca belirli söz öbeklerinde doğan sınırsız verme anlamları dışarıda kalır.","branch_image_ar":"العد والحساب","concept_gloss":"sayarak nicelik belirleme","contextual_glosses":[{"applicability":"Tek tek nesnelerin kaç tane olduğunun bulunmasını anlatan cümlelerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş ile ayın belirli sayı ve zaman düzenine bağlı oluşunu belirtmez.","preserves":"Nesneleri sayma ve ulaşılan niceliği belirleme işlemini korur."},"facet_ids":["F001"],"text":"sayısını çıkarmak","usage_role":"contextual"},{"applicability":"Güneş ile ayın ölçülü ve düzenli hareketini açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gündelik nesnelerin tek tek sayılması işlemini kapsamaz.","preserves":"Gök cisimleri için belirlenmiş sayı düzeni yönünü açıkça korur."},"facet_ids":["F002"],"text":"belirli bir sayı düzenine bağlı olmak","usage_role":"explanatory"}],"definition":"Nesneleri sayı yoluyla tek tek belirlemek ve sayı kullanarak niceliği ortaya çıkarmaktır. Güneş ile ay için bu, hareketlerin önceden belirlenmiş bir sayı ve zaman düzenine bağlı oluşuna uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesneler tek tek sayılır ve nicelikleri sayı kullanılarak belirlenir."},{"facet_id":"F002","role":"specialization","statement":"Güneş ile ayın hareketleri, bilinen ve belirlenmiş bir sayı düzeni içinde ele alınır."}],"identity_rationale":"Kaynak sözü, nesneleri sayma, sayıyı işlemde kullanma ve güneş ile ayın belirli bir sayı düzenine bağlı oluşunu açıkça destekler. Geçici çerçevedeki her türlü denetleme ve kestirim bu çekirdeğin parçası sayılamaz; bunlar ancak belirli türevlerde veya kuruluşlarda geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"nesneyi saymak ve niceliğini çıkarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sayma ve nicelik belirleme işlemi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sayma işlemi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sayı yoluyla belirleme"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"belirli sayı düzeni ve zaman ölçüsü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ölçmeden, denetlemeden veya kısmadan; beklenenden fazla"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sayıp değerlendiren ve gözeten"}],"lexicalization_note":"Tanım, yalın sayma çekirdeğini korur; gök cisimlerinin düzeni ve ölçüsüz verme gibi kurulu kullanımları bu çekirdekle birleştirmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; doğrudan sayma sınırını en iyi gösteren komşu yayımlandı, yalnızca aynı konu çevresinde duran veya başka dallara ait adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı sayma işlemiyle nicelik çıkarır ve belirli bir göksel düzene uzanabilir; komşu dal ise bütün öğeleri eksiksiz sayıp kuşatma sınırını öne çıkarır.","focus_only":"Saymanın yanında nicelik çıkarma ve gök cisimleri için belirli sayı düzeni kapsamı vardır.","gloss":"sayıyla belirleme ve eksiksiz sayıp dökme","neighbor_only":"Sayıyla eksiksiz kuşatma, bütün öğeleri tüketme ve bilgice kapsama vurgusu vardır.","neighbor_ref":"root_000332/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da çokluğu sayı yoluyla belirleme ve öğeleri tek tek ele alma alanında buluşur."}],"source_phrase_ar":"الأول العد؛ الحساب عدك الأشياء؛ حسبت الحساب؛ حسبته إذا عددته؛ الحساب استعمال العدد؛ الشمس والقمر بحسبان","source_summary":"Ortak anlatım, nesneleri saymayı ve sayıyı nicelik belirleme aracı olarak kullanmayı merkeze alır; güneş ile ayın düzeni de bilinen bir sayısal ölçüye bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عد الأشياء والحساب والمحاسبة والتقدير والمقدار وحساب الشمس والقمر","what_is_not_ar":"ليس هو الظن ولا الكفاية ولا الحسب والشرف"},"support_links":["sup_e97007a94d2330c09300"]},{"boundary":"Bu dal sayısal belirleme değil, kesin bilgi olmadan bir önermeyi zihinde daha olası görmedir.","branch_kind":"bare","branch_ref":"root_000318/B002","candidate_links":[{"candidate_id":"cand_b5c9ca19b5d577545362","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"öyle olduğunu sanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, kesinlik bulunmadığı halde bir durumun öyle olduğuna zihnen yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zihinsel yargı, iki karşıt olasılıktan birini ötekine üstün tutma biçiminde kurulabilir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir durum hakkında kesin olmayan fakat belirli bir yöne eğilen zihinsel yargı anlatılırken kullanılır.","boundary_detail":"Bu dal sayısal belirleme değil, kesin bilgi olmadan bir önermeyi zihinde daha olası görmedir.","branch_image_ar":"الحسبان والظن","concept_gloss":"öyle olduğunu sanmak","contextual_glosses":[{"applicability":"Bir kişi veya durum hakkında kesin olmayan olumlu ya da olumsuz yargıda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kesin olmayan zihinsel yönelişi ve yargının belirli bir seçeneğe bağlanmasını korur."},"facet_ids":["F001","F002"],"text":"öyle sanmak","usage_role":"general"}],"definition":"Kesin bilgiye ulaşmadan, karşıt olasılıklardan birini zihinde doğruya daha yakın görüp o yönde yargıya varmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, kesinlik bulunmadığı halde bir durumun öyle olduğuna zihnen yönelir."},{"facet_id":"F002","role":"specialization","statement":"Zihinsel yargı, iki karşıt olasılıktan birini ötekine üstün tutma biçiminde kurulabilir."}],"identity_rationale":"Kaynak sözü, bir şeyi doğru kabul etmeye yönelik fakat kesinliğe ulaşmamış zihinsel yargıyı açıkça anlatır. İki karşıt olasılıktan birine yönelme, dalın sanma çekirdeğini sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öyle sanmak ve zihnen öyle olduğuna hükmetmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sanı ve kesin olmayan yargı"}],"lexicalization_note":"Tanım yalın sanma ve kesin olmayan yargı alanıyla sınırlıdır; başka kuruluşlara özgü sayma veya yeterlik anlamı içeri alınmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kesin olmayan inanışla en yakın sınırı kuran dal seçildi, yalnızca kuşku, bilgi veya aynı kökün başka anlamlarını taşıyanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı bir seçeneği doğruya daha yakın görerek yargı kurmayı öne çıkarır; komşu dalda ise kuşku ve zayıf dayanak belirleyici sınırdır.","focus_only":"İki karşıt olasılıktan biri lehine zihinsel hüküm kurma yönü açıkça bulunur.","gloss":"kesin olmadan sanma","neighbor_only":"Kesinsizlik, zayıf inanış ve güçsüz bir belirtiye dayanan kuruntu daha baskındır.","neighbor_ref":"root_000969/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kesin bilgi düzeyine varmayan bir inanış veya zihinsel yöneliş bildirir."}],"source_phrase_ar":"الحسبان الظن؛ حسبت كذا في معنى ظننت؛ حسبته صالحا أي ظننته؛ حسبت الشيء ظننته؛ الحسبان أن يحكم لأحد النقيضين","source_summary":"Ortak kaynak anlatımı, bir şeyi kesin olarak bilmekten ayrı biçimde öyle sanmayı ve karşıt seçeneklerden biri lehine zihinsel yargı kurmayı bildirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حسب الشيء أو الأمر بمعنى ظنه وقدره في النفس وما يقاربه من توقع غير جازم","what_is_not_ar":"ليس هو الحساب العددي ولا الكفاية ولا الاحتساب للأجر"},"support_links":["sup_b2f3834fe17247f1c19c"]},{"boundary":"Çekirdek bir ihtiyacı karşılayacak ölçüye ulaşmaktır; bol armağan yalnızca belirtilen verme kuruluşlarında bu çekirdeği aşar.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B003","candidate_links":[{"candidate_id":"cand_808152b76e5963944876","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"gereksinimi karşılayacak kadar yetmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, kişinin gereksinimini karşılar ve başka bir şeye yönelme ihtiyacını kaldırır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Verme bağlamında alıcıya yetecek, onu hoşnut edecek veya bol sayılacak miktar sunulur."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin gerekli ölçüyü karşılaması veya verilenin alıcıya yeterli gelmesi anlatılırken kullanılır.","boundary_detail":"Çekirdek bir ihtiyacı karşılayacak ölçüye ulaşmaktır; bol armağan yalnızca belirtilen verme kuruluşlarında bu çekirdeği aşar.","branch_image_ar":"الكفاية والإغناء","concept_gloss":"gereksinimi karşılayacak kadar yetmek","contextual_glosses":[{"applicability":"Bir nesnenin, miktarın veya desteğin ihtiyacı karşılaması anlatıldığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Verme kuruluşlarında görülen bol ve hoşnut edici miktar genişlemesini belirtmez.","preserves":"Gereksinimin karşılanması ve başka şeye ihtiyaç kalmaması yönünü korur."},"facet_ids":["F001"],"text":"yeterli gelmek","usage_role":"general"},{"applicability":"Bir kişiye onu doyuracak veya hoşnut edecek miktarda verme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyin kendi başına yeterli olması biçimindeki genel kullanımı kapsamaz.","preserves":"Yeterli miktar verme ve bunun bolluğa uzanabilmesi yönlerini korur."},"facet_ids":["F002"],"text":"yetecek kadar, hatta bolca vermek","usage_role":"contextual"}],"definition":"Bir kişi veya durum için gereken miktara ulaşıp başka bir şeye ihtiyaç bırakmamaktır. Verme bağlamında, alıcıyı doyuracak kadar hatta kimi kullanımda beklenenden çok vermeye uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, kişinin gereksinimini karşılar ve başka bir şeye yönelme ihtiyacını kaldırır."},{"facet_id":"F002","role":"extension","statement":"Verme bağlamında alıcıya yetecek, onu hoşnut edecek veya bol sayılacak miktar sunulur."}],"identity_rationale":"Kaynak sözü bir şeyin ihtiyacı karşılamasını, bir kimseye yeterli miktar verilmesini ve bazı verme kuruluşlarında bolluğu açıkça bir araya getirir. Yeterlik çekirdeği korunarak bol verme, kurulu kullanıma bağlı bir genişleme olarak tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bu sana yeter; bununla yetin"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı bize yeter"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bu bana yetti"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ona yetecek veya onu hoşnut edecek kadar vermek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yeterli ya da bol armağan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ölçmeden, denetlemeden veya kısmadan; beklenenden fazla"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"soyluluk ile yeterlik arasında iki türlü yorumlanan şiir sözü"}],"lexicalization_note":"Yalın yeterlik çekirdeği ile belirli verme sözlerinde görülen yeterli ya da bol miktar ayrı yüzler olarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik çekirdeğini en iyi sınayan komşu yayımlandı, yalnızca bolluk, hoşnutluk veya ilgisiz aynı-kök dalları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı gereken miktarın yeterli oluşunu ve verme kapsamını öne çıkarır; komşu dal ise işi üstlenip sonucu sağlayan etkin yeterliği de içerir.","focus_only":"Yeterlik bildiren kalıpların yanında alıcıya yeterli veya bol miktarda verme genişlemesi vardır.","gloss":"gereksinimi karşılayıp yeterli olma","neighbor_only":"Bir işi üstlenip sonuna kadar götürerek açığı kapatma ve amacı gerçekleştirme yönü vardır.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gereksinimin karşılanması ve başka bir desteğe ihtiyaç bırakılmaması alanında buluşur."}],"source_phrase_ar":"الأصل الثاني الكفاية؛ حسبك هذا أي كفاك؛ حسبي كذا أي يكفيني؛ أحسبني الشيء أي كفاني؛ حسبنا الله أي كافينا هو؛ عطاء حسابا أي كافيا","source_summary":"Ortak anlatım, bir şeyin yeterli olmasını ve verilen miktarın alıcının gereksinimini karşılamasını temel alır; bazı verme örnekleri bu miktarı bolluk yönünde genişletir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حسبك وحسبي وأحسبني وأحسبته وما يكون كافيا أو مرضيا أو واسعا في العطاء","what_is_not_ar":"ليس هو العد المحض ولا الظن ولا الحسب في المفاخر"},"support_links":["sup_5a0899d3cd7396aa3741"]},{"boundary":"Bu dal sayısal sayma değil, kişi ve ataları için sayılıp anılan iyi işler ile bunların sağladığı köklü saygınlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"atalardan gelen saygınlık ve iyi işler birikimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin ve atalarının iyi işleri ile övünülecek başarıları birlikte değerlendirilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu birikim kişiye veya topluluğuna kalıcı bir soyluluk ve saygınlık kazandırır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin veya topluluğun geçmişten gelen soyluluğu ve övünülecek eylemleri birlikte anlatıldığında kullanılır.","boundary_detail":"Bu dal sayısal sayma değil, kişi ve ataları için sayılıp anılan iyi işler ile bunların sağladığı köklü saygınlıktır.","branch_image_ar":"الحسب والمآثر","concept_gloss":"atalardan gelen saygınlık ve iyi işler birikimi","contextual_glosses":[{"applicability":"Ataların ve kişinin iyi işlerinden doğan yerleşik toplumsal değer öne çıktığında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Saygınlığı oluşturan tek tek iyi işler ve övünülecek başarılar geri planda kalır.","preserves":"İyi eylemlerden doğan ve kuşaklar boyunca süren saygınlık sonucunu korur."},"facet_ids":["F002"],"text":"köklü saygınlık","usage_role":"contextual"}],"definition":"Bir kişinin kendisine ve atalarına bağlanan iyi işler, övünülecek başarılar ve bunların oluşturduğu köklü saygınlık birikimidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin ve atalarının iyi işleri ile övünülecek başarıları birlikte değerlendirilir."},{"facet_id":"F002","role":"extension","statement":"Bu birikim kişiye veya topluluğuna kalıcı bir soyluluk ve saygınlık kazandırır."}],"identity_rationale":"Kaynak sözü, kişinin ve atalarının iyi işleri ile bunlardan doğan kalıcı saygınlığı aynı çekirdekte toplar. Dal, salt soy çizgisinden daha geniştir; kişinin kendi güzel eylemleri de bu birikime dahildir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"atalardan gelen saygınlık ve övünülecek işler"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"soylu, saygın veya eli açık kişi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"soyluluk ya da yeterlik diye yorumlanan şiir sözü"}],"lexicalization_note":"Tanım ortak saygınlık çekirdeğini verir; kişiyi niteleyen türevler ve iki anlamlı şiir sözü ayrı lexical yüzler olarak tutulur.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; birikmiş saygınlık ile tekil övgü değerini ayıran komşu yayımlandı, salt soy, yüksek konum veya karşıt düşüş adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı iyi işleri soy ve geçmiş içinde biriken saygınlığın bütünü olarak ele alır; komşu dal ise tekil bir güzel özellik veya övgüye değer işi belirtir.","focus_only":"Kişinin ve atalarının eylemlerinden oluşan kuşaklar arası saygınlık birikimi vardır.","gloss":"saygınlık birikimi ve soylu özellik","neighbor_only":"Tek bir soylu özellik, güzel davranış veya yiğitçe iş ayrı bir değer olarak adlandırılır.","neighbor_ref":"root_001539/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişiyi övgüye değer kılan iyi eylemler ve nitelikler alanındadır."}],"source_phrase_ar":"الحسب الذي يعد من الإنسان؛ الحسب الشرف الثابت في الآباء؛ حسب الرجل مآثر آبائه وأجداده؛ ما يعده الإنسان من مفاخر آبائه؛ الحسب الفعال الحسن له ولآبائه","source_summary":"Kaynaklar, kişi ve atalarının iyi eylemlerini, övünülecek başarılarını ve bunların kuşaklar boyunca oluşturduğu saygınlığı ortak içerik olarak sunar.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه شرف الآباء والمآثر والدين والمال والخلق والجود وما يعد للرجل أو قومه من مفاخر","what_is_not_ar":"ليس هو الحساب العددي ولا الكفاية ولا الوسادة"},"support_links":[]},{"boundary":"Eylem veya kayıp Tanrı katındaki karşılık amacıyla değer hanesine yazılır; gündelik sayım ya da kamusal denetim amaç değildir.","branch_kind":"bare","branch_ref":"root_000318/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"Tanrı katında karşılığını beklemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş, iyilik veya kayıp Tanrı katında kişinin değer hanesine yazılmış sayılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi bu değerlendirme karşılığında Tanrı'dan iyilik bekler."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin, iyiliğin veya kaybın Tanrı katında değerli sayılarak karşılığının beklendiği durumlarda kullanılır.","boundary_detail":"Eylem veya kayıp Tanrı katındaki karşılık amacıyla değer hanesine yazılır; gündelik sayım ya da kamusal denetim amaç değildir.","branch_image_ar":"الاحتساب عند الله","concept_gloss":"Tanrı katında karşılığını beklemek","contextual_glosses":[{"applicability":"İyi bir iş yapılırken veya acı bir kayıp kabullenilirken göksel karşılık beklentisini anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem ya da kaybın değerli sayılmasını ve karşılığın Tanrı'dan beklenmesini korur."},"facet_ids":["F001","F002"],"text":"karşılığını Tanrı'dan beklemek","usage_role":"general"}],"definition":"Yapılan bir işi, gerçekleşen bir iyiliği veya uğranan bir kaybı Tanrı katında değer hanesine yazıp bunun karşılığını beklemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş, iyilik veya kayıp Tanrı katında kişinin değer hanesine yazılmış sayılır."},{"facet_id":"F002","role":"core","statement":"Kişi bu değerlendirme karşılığında Tanrı'dan iyilik bekler."}],"identity_rationale":"Kaynak sözü, yapılan bir işi, bir iyiliği veya çocuk kaybını Tanrı katında değer hanesine yazıp karşılığını beklemeyi açıkça anlatır. Bu yön, iyi yönetim ve kötü davranışı denetleme dalından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir işi veya kaybı Tanrı katında değer hanesine yazıp karşılığını beklemek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"Tanrı katında karşılık umularak yapılan iş"}],"lexicalization_note":"Tanım, Tanrı katında karşılık bekleme çekirdeğini genel dal sınırı olarak korur ve yönetimle ilgili kurulu kullanımları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; değer hanesine yazma ile gerçek sayma arasındaki ayrımı gösteren iç komşu yayımlandı, ilgisiz kişi ve miktar adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalındaki değerlendirme inanç ve karşılık beklentisine yöneliktir; komşu dalda ise amaç nesnelerin sayısını ve niceliğini belirlemektir.","focus_only":"Bir iş veya kayıp Tanrı katında değerli sayılır ve bunun göksel karşılığı beklenir.","gloss":"değer hanesine yazma ve sayarak belirleme","neighbor_only":"Nesneler sayı yoluyla belirlenir ve nicelikleri çıkarılır.","neighbor_ref":"root_000318/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir şeyi kayda geçirip değerlendirme düşüncesi bulunur."}],"source_phrase_ar":"احتسب فلان ابنه؛ احتسابك الأجر؛ احتسب فلان عند الله خيرا؛ احتسبت بكذا أجرا عند الله؛ احتسب ابنا له أي اعتد به عند الله؛ الحسبة فعل ما يحتسب به عند الله تعالى","source_summary":"Ortak anlatım, bir işin veya çocuk kaybının Tanrı katında değerli sayılmasını ve kişinin bunun karşılığını beklemesini bir arada verir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه احتساب الأجر واعتداد الولد أو الخير عند الله تعالى","what_is_not_ar":"ليس هو حسن التدبير ولا الإنكار على القبيح ولا الظن"},"support_links":[]},{"boundary":"Dal, belirli kuruluşlara bağlı yönetme, kınama ve kamusal gözetim kullanımlarını kapsar; Tanrı katında karşılık beklemeyi kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B006","candidate_links":[{"candidate_id":"cand_0c8e0e4e66e50ed1c0db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"işi gözetme, kötü davranışı sorgulama ve kamusal denetim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş dikkatle ele alınır ve iyi biçimde çekip çevrilir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimsenin yaptığı kötü davranış kınanır ve o kişi bu davranış üzerinden sorgulanır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kentte davranışları ve kamu düzenini gözeten görevli bu işi kurumsal olarak yürütür."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen yönetme, birine karşı çıkma ve kent görevlisi kuruluşlarının ortak alanını anlatmak için kullanılır.","boundary_detail":"Dal, belirli kuruluşlara bağlı yönetme, kınama ve kamusal gözetim kullanımlarını kapsar; Tanrı katında karşılık beklemeyi kapsamaz.","branch_image_ar":"الحسبة والنظر في الأمر","concept_gloss":"işi gözetme, kötü davranışı sorgulama ve kamusal denetim","contextual_glosses":[{"applicability":"Bir işin dikkatli ve yerinde yönetilmesini bildiren kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü davranışı kınama ve kamusal görevli yüzlerini kapsamaz.","preserves":"İşi dikkatle ele alma ve iyi yönetme yüzünü korur."},"facet_ids":["F001"],"text":"işi iyi çekip çevirmek","usage_role":"contextual"},{"applicability":"Bir kimseye yaptığı yanlış davranış nedeniyle karşı çıkılan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyi yönetim ve kentteki kamusal görevli yüzlerini kapsamaz.","preserves":"Kötü davranışa karşı çıkma ve yapanı sorgulama yüzünü korur."},"facet_ids":["F002"],"text":"kötü davranışını kınayıp sorgulamak","usage_role":"contextual"}],"definition":"Belirli kuruluşlarda bir işi iyi çekip çevirmeyi, bir kimsenin kötü davranışını kınayıp sorgulamayı veya kentte bu tür kamusal gözetimi görev olarak yürütmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş dikkatle ele alınır ve iyi biçimde çekip çevrilir."},{"facet_id":"F002","role":"associated_use","statement":"Bir kimsenin yaptığı kötü davranış kınanır ve o kişi bu davranış üzerinden sorgulanır."},{"facet_id":"F003","role":"specialization","statement":"Kentte davranışları ve kamu düzenini gözeten görevli bu işi kurumsal olarak yürütür."}],"identity_rationale":"Kaynak sözü tek bir yalın anlamdan çok, belirli kuruluşlarda iyi yönetme, kötü davranışı kınama ve kentte bu görevi üstlenen kişiyi birlikte verir. Bu kullanımlar yönetim ve gözetim çevresinde ilişkilidir, ancak biri ötekinin zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kötü davranışından dolayı kınamak ve yaptığını sorgulamak"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işi iyi çekip çevirmek ve gözetmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kentte kamu düzenini ve davranışları gözeten görevli"}],"lexicalization_note":"Tanım, iyi yönetme, birine karşı kötü işi kınama ve kamusal görevli kullanımlarını ayrı kuruluşlara bağlı yüzler olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kamusal görev sınırını gösteren aday yayımlandı, adalet, hak ödeme, terbiye ve yalnızca aynı senaryoda yer alan dallar elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı kötü davranışı gözetme ve kınama gibi belirli bir görev alanına bağlıdır; komşu dal her tür kamu işine atanmayı ve o işi yürütmeyi daha genel biçimde kapsar.","focus_only":"İyi yönetme ve kötü davranışı kınama yanında belirli bir kent gözetimi görevi bulunur.","gloss":"kamusal gözetim ve kamu işine atanma","neighbor_only":"Yönetici tarafından herhangi bir kamu işine atanma ve o işi üstlenme genel olarak kapsanır.","neighbor_ref":"root_001046/B003","relation_type":"same_field","shared_zone":"Her iki dal da kamu adına bir işi üstlenen görevli ve görev yürütme alanında buluşur."}],"source_phrase_ar":"حسن الحسبة بالأمر إذا كان حسن التدبير؛ احتسب فلان على فلان أنكر عليه قبيحا عمله؛ احتسبت عليه كذا إذا أنكرته عليه؛ فلان محتسب البلد؛ حسن الحسبة في الأمر","source_summary":"Kaynak sözü, bir işi iyi yönetme, kötü bir davranışı yapan kişiye karşı çıkma ve kentte gözetim görevi üstlenme kullanımlarını aynı dalda fakat ayrı kuruluşlar halinde toplar.","sources":["MQ","JA","SI","TA"],"what_is_ar":"يدخل فيه حسن التدبير في الأمر والإنكار على القبيح والمحاسبة العملية ومحتسب البلد","what_is_not_ar":"ليس هو مجرد الأجر المحتسب عند الله ولا الظن ولا الكفاية"},"support_links":["sup_bbd518d33ca711827004"]},{"boundary":"Kısa ok veya atılan küçük nesne çekirdektir; gökten gelen kullanım, kaynakların değişik yorumladığı yıkıcı bir gönderim olarak ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"kısa ok veya yukarıdan gelen yıkıcı gönderim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kısa oklar veya bir hedefe fırlatılan küçük nesneler söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gökten gelen kullanım, yukarıdan gönderilen yıkıcı bir şey ya da olay anlamına uzanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu yıkıcı gönderimin dolu, ateş, çekirge veya genel bir yıkım olduğu konusunda farklı açıklamalar vardır."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kısa fırlatma nesnesi ile gökten gelen değişken yıkım yorumlarını birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Kısa ok veya atılan küçük nesne çekirdektir; gökten gelen kullanım, kaynakların değişik yorumladığı yıkıcı bir gönderim olarak ayrı tutulur.","branch_image_ar":"المرامي والحسبان النازل","concept_gloss":"kısa ok veya yukarıdan gelen yıkıcı gönderim","contextual_glosses":[{"applicability":"Yayla atılan küçük ve kısa nesneler anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gökten gelen yıkıcı gönderime ilişkin değişken kullanımı kapsamaz.","preserves":"Fırlatılan kısa oklar biçimindeki somut çekirdeği korur."},"facet_ids":["F001"],"text":"kısa oklar","usage_role":"contextual"},{"applicability":"Dolu, ateş, çekirge veya genel yıkım arasında değişen göksel gönderim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut küçük ok çekirdeğini ve yorumlar arasındaki ayrıntılı çeşitliliği kapsamaz.","preserves":"Yukarıdan gelme ve zarar verme ortak yönlerini korur."},"facet_ids":["F002","F003"],"text":"gökten gelen yıkıcı şey","usage_role":"explanatory"}],"definition":"Kısa okları veya fırlatılan küçük nesneleri bildirir. Gökten gelme kuruluşunda ise dolu, ateş, çekirge ya da başka bir yıkıcı gönderim olarak değişken biçimde yorumlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kısa oklar veya bir hedefe fırlatılan küçük nesneler söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Gökten gelen kullanım, yukarıdan gönderilen yıkıcı bir şey ya da olay anlamına uzanır."},{"facet_id":"F003","role":"source_variant","statement":"Bu yıkıcı gönderimin dolu, ateş, çekirge veya genel bir yıkım olduğu konusunda farklı açıklamalar vardır."}],"identity_rationale":"Kaynak sözü kısa oklar ve atılan küçük nesneler çekirdeğini açıkça verir; gökten gelen kullanım ise dolu, ateş, çekirge veya genel yıkım olarak değişik biçimlerde açıklanır. Bu ikinci alan tek bir nesne türüymüş gibi daraltılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kısa oklar veya atılan küçük nesneler"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"gökten gönderilen dolu, ateş, çekirge ya da yıkıcı şey"}],"lexicalization_note":"Yalın küçük ok anlamı ile gökten gelme kuruluşundaki dolu, ateş, çekirge veya yıkım yorumları birbirine karıştırılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi; gökten gelen yıkım alanındaki en yararlı sınır yayımlandı, ateş, ışık, sıcaklık ve aynı kökün ilgisiz dalları yalnızca tematik kaldığı için elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı kısa ok anlamından göksel yıkıcı gönderime uzanan değişken bir kapsama sahiptir; komşu dal ise şiddetli ses ve çarpma niteliğindeki belirli gök olayını merkez alır.","focus_only":"Kısa oklar çekirdeği ve gökten gelen çeşitli yıkıcı nesne yorumları bulunur.","gloss":"gökten gelen yıkım ve şiddetli gök olayı","neighbor_only":"Gök gürültüsüyle bağlantılı tek bir şiddetli çarpma, ses veya yıldırım olayı anlatılır.","neighbor_ref":"root_000864/B002","relation_type":"same_field","shared_zone":"Her iki dal gökten gelen, ateş veya yıkımla ilişkilendirilebilen korkutucu olay alanına girebilir."}],"source_phrase_ar":"الحسبان سهام صغار؛ حسبان من السماء بالبرد؛ حسبانا من السماء أي نارا تحرقها؛ حسبانا عذابا ولا أدري؛ الحسبان بالضم العذاب؛ أصاب الأرض حسبان أي جراد؛ الحسبان المرامي؛ نارا وعذابا","source_summary":"Ortak anlatım kısa okları ve fırlatılan küçük nesneleri verir; gökten gelen kullanımın dolu, ateş, çekirge veya genel bir yıkım sayılması konusunda tek bir nesneye indirgenemeyen açıklama çeşitliliği vardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحسبان بمعنى السهام أو المرامي أو ما يرسل من السماء من عذاب أو برد أو نار أو جراد أو صاعقة","what_is_not_ar":"ليس هو الحساب المنظم للشمس والقمر ولا الكفاية ولا الوسادة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000318/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başın altına konan, kimi anlatımda deriden yapılmış küçük bir yastık söz konusudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimse bu yastığın üzerine oturtulur veya başı yastıkla desteklenir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı iddiada geçen kısa ok anlamı yastık çekirdeğiyle birleşmez ve ayrı dala bağlanmayı gerektirir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"المحسبة والوسادة","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Baş altına konan küçük veya deriden yapılmış destek nesnesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birini yastığa oturtma eylemini ve karışmış kısa ok kaydını kapsamaz.","preserves":"Yastık nesnesinin küçüklüğünü ve baş desteği işlevini korur."},"facet_ids":["F001"],"text":"küçük yastık","usage_role":"contextual"}],"definition":"Bu dalın güvenli çekirdeği küçük yastık ve birini onun üzerine oturtma ya da başını onunla desteklemedir. Tek kaynak iddiasına kısa ok anlamı da karıştığı için dal ayrılmadan birleşik bir tanım kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başın altına konan, kimi anlatımda deriden yapılmış küçük bir yastık söz konusudur."},{"facet_id":"F002","role":"extension","statement":"Bir kimse bu yastığın üzerine oturtulur veya başı yastıkla desteklenir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı iddiada geçen kısa ok anlamı yastık çekirdeğiyle birleşmez ve ayrı dala bağlanmayı gerektirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"küçük yastık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"deriden yapılmış veya baş altına konan yastık"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini yastığa oturtmak veya başına yastık koymak"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yastıksız; bazı açıklamalarda ölü sargısına sarılmamış, gömülmemiş ya da onurlandırılmamış"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الحسبان جمع حسبانة وهي الوسادة الصغيرة؛ الحسبان سهام قصار؛ الحسبانة أيضا الوسادة الصغيرة؛ المحسبة وسادة من أدم؛ حسبته إذا وسدته؛ الحسبانة الوسادة الصغيرة","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الحسبانة أو المحسبة بمعنى الوسادة الصغيرة وإجلاس الرجل عليها أو توسيده بها","what_is_not_ar":"ليس هو سهام الحسبان ولا الحسب الشريف ولا العد"},"support_links":[]},{"boundary":"Dal belirli bir deri veya tüy görünümüdür; soyluluk, sayma ve yastık anlamlarıyla ilişkili değildir.","branch_kind":"bare","branch_ref":"root_000318/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"deri veya tüyde karışık ak, kızıl ve koyu görünüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan veya devenin derisi ya da tüyü alışılmıştan farklı bir renk görünümü taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görünüm hastalığa bağlı aklık, aklıkla kızıllık, koyu bozluk veya kızıla çalan karalık olarak değişebilir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin deri ve tüyündeki değişken renk karışımı ya da hastalıklı aklık anlatılırken kullanılır.","boundary_detail":"Dal belirli bir deri veya tüy görünümüdür; soyluluk, sayma ve yastık anlamlarıyla ilişkili değildir.","branch_image_ar":"لون الأحسب والأحسبية","concept_gloss":"deri veya tüyde karışık ak, kızıl ve koyu görünüm","contextual_glosses":[{"applicability":"Özellikle devenin tüyünde aklık ile kızıllığın birlikte görüldüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsandaki hastalık aklığını ve koyu boz ya da kızıla çalan renkleri kapsamaz.","preserves":"Deve tüyündeki aklık ve kızıllık karışımını açıkça korur."},"facet_ids":["F001","F002"],"text":"aklık ve kızıllık karışımı tüylü","usage_role":"contextual"}],"definition":"İnsan ya da devenin derisinde veya tüyünde hastalığa bağlı aklık ya da aklık, kızıllık, koyuluk ve bozluğun değişik birleşimlerinden oluşan görünümdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan veya devenin derisi ya da tüyü alışılmıştan farklı bir renk görünümü taşır."},{"facet_id":"F002","role":"source_variant","statement":"Görünüm hastalığa bağlı aklık, aklıkla kızıllık, koyu bozluk veya kızıla çalan karalık olarak değişebilir."}],"identity_rationale":"Kaynak sözü, insan veya devenin derisi ve tüyünde görülen aklık, kızıllık, koyuluk ve bozluk karışımlarını; ayrıca hastalıkla oluşan aklığı aynı renk alanında verir. Geçici çerçeve bu değişkenliği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"derisi hastalıkla beyazlamış ya da tüyünde aklık, kızıllık ve koyuluk karışmış kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"koyu zemin üstünde bozluk ya da kızıla çalan karalık"}],"lexicalization_note":"Tanım, insan ve devede görülen yalın renk veya deri durumu alanıyla sınırlıdır; başka söz öbeklerinden anlam aktarılmaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel karışık renk alanıyla en yararlı sınır yayımlandı, yalnızca aklık, toprak tonu, beden kusuru veya hastalık alanında kalanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı insan ve devenin deri ya da tüyündeki belirli görünüşlere, ayrıca hastalık aklığına bağlıdır; komşu dal daha geniş taşıyıcılarla genel renk karışımını adlandırır.","focus_only":"İnsan ve deveyle sınırlı deri veya tüy görünümü, hastalık aklığını ve belirli koyu tonları içerir.","gloss":"belirli deri rengi ve genel karışık renk","neighbor_only":"Renk içinde renk bulunması göz, kan, koyun ve başka taşıyıcılara uzanan daha genel bir karışım alanıdır.","neighbor_ref":"root_000813/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal aklık, kızıllık, karalık veya bozluğun tek görünümde karışmasını anlatabilir."}],"source_phrase_ar":"الأحسب الذي ابيضت جلدته من داء؛ الأحسب من الناس والإبل وهو الأبرص؛ الحسبة غبرة في كدرة؛ الأحسب من الإبل فيه بياض وحمرة؛ الحسبة سواد يضرب إلى الحمرة","source_summary":"Kaynak anlatımı insan ve devede görülen ayırt edici deri ya da tüy rengini ortak alan olarak verir; bu görünüm hastalık aklığından ak-kızıl karışıma ve koyu boz ya da kızıla çalan tona kadar değişir.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"يدخل فيه الأحسب من الناس أو الإبل وما في الجلد أو الشعر من بياض وحمرة أو غبرة أو داء يشبه البرص","what_is_not_ar":"ليس هو الحسب في الشرف ولا الحساب ولا الوسادة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000318/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","surface_ar":"حِسَابَ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir haber sorulur, izlenir ve hakkında bilgi edinilmeye çalışılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin elinde ne bulunduğu veya ne sağlayabileceği sınanarak öğrenilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alıcının verileceğini beklememesi yönündeki parça araştırma çekirdeğinden ayrıdır ve başka dala bağlanmayı gerektirir."}}],"root_ar":"ح س ب","root_id":"root_000318","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"التحسب والاستخبار","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Bir olay hakkında bilgi toplamak için soru sorma ve haber arama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişinin elindekini sınamayı ve karışmış beklenti parçasını kapsamaz.","preserves":"Haber isteme ve bilgi izini sürme işlemlerini korur."},"facet_ids":["F001"],"text":"haberi sorup izini sürmek","usage_role":"contextual"},{"applicability":"Bir kişinin neye sahip olduğunu veya ne sağlayabileceğini yoklama bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel haber aramayı ve karışmış beklenti parçasını kapsamaz.","preserves":"Kişide bulunanı sınama ve sonuçta öğrenme yönlerini korur."},"facet_ids":["F002"],"text":"elinde ne olduğunu sınayıp öğrenmek","usage_role":"contextual"}],"definition":"Bu dalın güvenli çekirdeği bir haberi sorup izini sürmek veya bir kişinin elinde ne bulunduğunu sınayarak öğrenmektir. Aynı iddiadaki beklememe parçası bu çekirdekle birleşmediği için yeniden bağlanmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir haber sorulur, izlenir ve hakkında bilgi edinilmeye çalışılır."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin elinde ne bulunduğu veya ne sağlayabileceği sınanarak öğrenilir."},{"facet_id":"F003","role":"source_variant","statement":"Alıcının verileceğini beklememesi yönündeki parça araştırma çekirdeğinden ayrıdır ve başka dala bağlanmayı gerektirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"haberi sorup izini sürmek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"birinin elinde ne olduğunu sınayıp öğrenmek"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"بغير أن حسب المعطى أنه يعطيه؛ تحسبت الخبر أي استخبرت؛ احتسبت فلانا اختبرت ما عنده؛ يتحسب الأخبار أي يتحسسها ويطلبها","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه تحسب الخبر واستخباره واختبار ما عند الإنسان وطلب الأخبار","what_is_not_ar":"ليس هو الظن المجرد ولا الحساب العددي ولا الحسبة في التدبير"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:26:1"],"branch_refs":[],"candidate_id":"cand_198d91d9c38804da7473","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:1:procedural-rank-not-clock","source_type":"word_analysis","support_ids":["sup_a7bbbacff2588e82a218","sup_c59219deda976c2ab3ab"],"title":"delay marks staged procedure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:1","qac_refs":["88:26:1:1"],"status":"accepted"}},{"anchor_refs":["88:26:1"],"branch_refs":[],"candidate_id":"cand_4dcf80313ecfefd996e5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:1:resumptive-closing-assertion","source_type":"word_analysis","support_ids":["sup_4a65324482fd60d94203","sup_c59219deda976c2ab3ab"],"title":"linked sequel becomes a fresh declaration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:1","qac_refs":["88:26:1:1"],"status":"accepted"}},{"anchor_refs":["88:26:1"],"branch_refs":[],"candidate_id":"cand_debc5b2bac355fbffadd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:1:sequel-after-return","source_type":"word_analysis","support_ids":["sup_6b5fa21c5613d0d458f6","sup_c59219deda976c2ab3ab"],"title":"return is followed by account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:1","qac_refs":["88:26:1:1"],"status":"accepted"}},{"anchor_refs":["88:26:1"],"branch_refs":[],"candidate_id":"cand_dbda65d3b4dff0123163","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:1:sound-handoff-to-certainty","source_type":"word_analysis","support_ids":["sup_8ac2e78e9329f7522f2a","sup_c59219deda976c2ab3ab"],"title":"nasal handoff into emphasis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:1","qac_refs":["88:26:1:1"],"status":"accepted"}},{"anchor_refs":["88:26:2"],"branch_refs":[],"candidate_id":"cand_fd4fb69457f79e14a953","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:2:audible-emphasis","source_type":"word_analysis","support_ids":["sup_007a4e593ba6818c6cb0","sup_df6abac4488c3b12a7dd"],"title":"doubled nūn carries certainty forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:2","qac_refs":["88:26:2:1"],"status":"accepted"}},{"anchor_refs":["88:26:2"],"branch_refs":[],"candidate_id":"cand_e5b48fcdc67941ae54d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:2:certainty-against-evasion","source_type":"word_analysis","support_ids":["sup_007a4e593ba6818c6cb0","sup_9820401eb529ea9bb3e4"],"title":"emphasis presses against evasion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:2","qac_refs":["88:26:2:1"],"status":"accepted"}},{"anchor_refs":["88:26:2"],"branch_refs":[],"candidate_id":"cand_c92400383f3d2df49582","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:2:governed-delayed-ism","source_type":"word_analysis","support_ids":["sup_007a4e593ba6818c6cb0","sup_aca26fd561f413139372"],"title":"delayed account remains under inna","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:2","qac_refs":["88:26:2:1"],"status":"accepted"}},{"anchor_refs":["88:26:2"],"branch_refs":[],"candidate_id":"cand_61e1e2716b9c438dcf60","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:2:independent-final-assertion","source_type":"word_analysis","support_ids":["sup_007a4e593ba6818c6cb0","sup_c7cd7f8730f79fcb799f"],"title":"kasra form launches declaration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:2","qac_refs":["88:26:2:1"],"status":"accepted"}},{"anchor_refs":["88:26:2"],"branch_refs":[],"candidate_id":"cand_9baebe3a178349718997","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:2:whole-clause-certification","source_type":"word_analysis","support_ids":["sup_007a4e593ba6818c6cb0","sup_f6317758f37919a22595"],"title":"certainty covers responsibility and account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:2","qac_refs":["88:26:2:1"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_d8a849ff773231f1c4e4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:answers-denied-control","source_type":"word_analysis","support_ids":["sup_28f2b69d409cd1e9e0e6","sup_ea0062d8a8c0c95a41c1"],"title":"denied over-them becomes upon-Us","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_33b135a9039ea1dafd65","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:certified-responsibility-scope","source_type":"word_analysis","support_ids":["sup_28f2b69d409cd1e9e0e6","sup_4d7d9e729b0b4d32e26a"],"title":"upon-Us falls inside certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_e87e085bca4cb6c3ffb1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:fronted-responsibility-focus","source_type":"word_analysis","support_ids":["sup_28f2b69d409cd1e9e0e6","sup_d071a52ceaeae40b2f39"],"title":"responsibility is heard before account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_858759e2f9d6c68e066a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:incumbency-not-destination","source_type":"word_analysis","support_ids":["sup_26c31f62c2664d0fbe65","sup_28f2b69d409cd1e9e0e6"],"title":"destination turns into responsibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_461fb2cc3676c84e4941","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:nasal-lead-to-account","source_type":"word_analysis","support_ids":["sup_28f2b69d409cd1e9e0e6","sup_c18f0517b43e7d82eab3"],"title":"sound foregrounds the responsible party","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:3"],"branch_refs":[],"candidate_id":"cand_5ad37b0da47cd30825a6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:26:3:same-divine-suffix","source_type":"word_analysis","support_ids":["sup_28f2b69d409cd1e9e0e6","sup_d8b58c4316c8ed376500"],"title":"same speaker, new prepositional host","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:3","qac_refs":["88:26:3:1","88:26:3:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_75f57bfa6091969069b9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:account-sound-texture","source_type":"word_analysis","support_ids":["sup_b0df08837744c3ad99e4","sup_b23b17ec736643d08848"],"title":"sound tightens the final account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_86dceed3d57e96648cbc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:common-root-final-gerund","source_type":"word_analysis","support_ids":["sup_b23b17ec736643d08848","sup_cdd9e482f57b3a42d717"],"title":"broad root lands as final noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_d7c5fa5f7bac1d36c6bb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:denied-control-resolved-by-account","source_type":"word_analysis","support_ids":["sup_b23b17ec736643d08848","sup_c8395154f850b3e285ae"],"title":"authority becomes reckoning, not coercion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_3e63da46164e414c6139","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:destination-to-burden-boundary","source_type":"word_analysis","support_ids":["sup_426837f7e7618b92042a","sup_b23b17ec736643d08848"],"title":"arrival becomes accounting procedure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_399c8c8c2923a10dad5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:evaluative-counting","source_type":"word_analysis","support_ids":["sup_b23b17ec736643d08848","sup_bc054adb3f962af5a215"],"title":"counting includes assessment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_d80c0f3b42f30bc6fdb8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:fawasil-pairing","source_type":"word_analysis","support_ids":["sup_1640ba1e86da49b78871","sup_b23b17ec736643d08848"],"title":"shared ending binds return to account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_63ade5263a19481a0de2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:final-surah-seal","source_type":"word_analysis","support_ids":["sup_addcd459634b7b803c3d","sup_b23b17ec736643d08848"],"title":"surah closes on accountability","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_f9c37fbd7719d47cc14c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:general-tail-after-specific-warning","source_type":"word_analysis","support_ids":["sup_94f9a4365066d52c2cab","sup_b23b17ec736643d08848"],"title":"specific warning opens into total account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_4218573d782e03619b59","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:governed-delayed-account","source_type":"word_analysis","support_ids":["sup_6162f2cc12164413e680","sup_b23b17ec736643d08848"],"title":"account arrives after responsibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_58252f8f7f9812421fd2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:local-reckoning-field","source_type":"word_analysis","support_ids":["sup_8efbb8112e04e25507af","sup_b23b17ec736643d08848"],"title":"measured audit, not vague aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_6acb6d7db1616774c093","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:masdar-charge-not-verb","source_type":"word_analysis","support_ids":["sup_648a2e7e869202bb4345","sup_b23b17ec736643d08848"],"title":"substantive charge replaces finite narration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_ceb2d2cf9ee056c22bdf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:objective-idafa","source_type":"word_analysis","support_ids":["sup_006fab176325abcf376b","sup_b23b17ec736643d08848"],"title":"possession becomes being audited","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_ba318e2ad74db3bf9c94","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:personal-account-liability","source_type":"word_analysis","support_ids":["sup_62c22820fe4fa06f1411","sup_b23b17ec736643d08848"],"title":"their account, not abstract reckoning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_86a6bf061b738ed87eef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:process-and-result","source_type":"word_analysis","support_ids":["sup_3c48b0b46275938a3b68","sup_b23b17ec736643d08848"],"title":"reckoning as procedure and settlement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_b8b7760916999c6be1ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:pronoun-routing","source_type":"word_analysis","support_ids":["sup_8d6ede5780dbcc4bab27","sup_b23b17ec736643d08848"],"title":"suffix keeps the accountable group in view","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_97bc7cb8f4ca3ecd6f15","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:return-account-formal-pair","source_type":"word_analysis","support_ids":["sup_b23b17ec736643d08848","sup_ce8a2bfe66aa4fa04336"],"title":"return and account share a bound shape","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_2e39f5a9bb2616c48c07","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:settled-nominal-assignment","source_type":"word_analysis","support_ids":["sup_ae5598a4dc7ca9a3b6fc","sup_b23b17ec736643d08848"],"title":"verbless architecture makes assignment settled","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_9b6a94c1e3af88088d67","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:singular-account-plural-group","source_type":"word_analysis","support_ids":["sup_a86f6cea805bcab8abbf","sup_b23b17ec736643d08848"],"title":"one account gathers a plural group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_8e43322538afc6b6122c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:sufficiency-value-color","source_type":"word_analysis","support_ids":["sup_508c308a2c1e68d70ca2","sup_b23b17ec736643d08848"],"title":"adequacy colors the account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:26:4","qac_refs":["88:26:4:1","88:26:4:2"],"status":"accepted"}},{"anchor_refs":["88:26:4"],"branch_refs":[],"candidate_id":"cand_c37c100f735fe174095a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000318"],"scope":"focus_ayah","source_local_id":"88:26:4:1","source_type":"qac_morpheme","support_ids":["sup_c1121e6b556c222d6a2b"],"title":"QAC root occurrence: ح س ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:26","branch_refs":["root_000318/B001"],"candidate_id":"cand_a4e0fe6ca1974e8d2796","commentary_obligation":"review","hft_ref":"hft_eae4ed394559ad80dadf","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_complete_reckoning","source_type":"hft","support_ids":["sup_e97007a94d2330c09300"],"title":"baseline_complete_reckoning","trust":"legacy_unbound"},{"anchor_refs":["88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:26","branch_refs":["root_000318/B006"],"candidate_id":"cand_0c8e0e4e66e50ed1c0db","commentary_obligation":"review","hft_ref":"hft_40f2c3d92ff7d91c6fe7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_accountable_custody","source_type":"hft","support_ids":["sup_bbd518d33ca711827004"],"title":"baseline_accountable_custody","trust":"legacy_unbound"},{"anchor_refs":["88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:26","branch_refs":["root_000318/B003"],"candidate_id":"cand_808152b76e5963944876","commentary_obligation":"review","hft_ref":"hft_1a9610ae6b80c3375933","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_sufficient_settlement","source_type":"hft","support_ids":["sup_5a0899d3cd7396aa3741"],"title":"baseline_sufficient_settlement","trust":"legacy_unbound"},{"anchor_refs":["88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:26","branch_refs":["root_000318/B002"],"candidate_id":"cand_b5c9ca19b5d577545362","commentary_obligation":"review","hft_ref":"hft_b3925232812c2b3ee6bb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_estimate_overruled","source_type":"hft","support_ids":["sup_b2f3834fe17247f1c19c"],"title":"baseline_estimate_overruled","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","qac_morphemes":[{"lemma_ar":"ثُمّ","morph_features":"STEM|POS:CONJ|LEM:vum~","morpheme_role":"STEM","pos":"CONJ","qac_ref":"88:26:1:1","qac_word_ref":"88:26:1","root_ar":"","surface_ar":"ثُمَّ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:26:2:1","qac_word_ref":"88:26:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:26:3:1","qac_word_ref":"88:26:3","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:26:3:2","qac_word_ref":"88:26:3","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","root_ar":"ح س ب","surface_ar":"حِسَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:26:4:2","qac_word_ref":"88:26:4","root_ar":"","surface_ar":"هُم"}],"word_analysis_qac_refs":[["88:26:1:1"],["88:26:2:1"],["88:26:3:1","88:26:3:2"],["88:26:4:1","88:26:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:26:1","88:26:2","88:26:3","88:26:4"]},"focus_surface_evidence":{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","qac_morphemes":[{"lemma_ar":"ثُمّ","morph_features":"STEM|POS:CONJ|LEM:vum~","morpheme_role":"STEM","pos":"CONJ","qac_ref":"88:26:1:1","qac_word_ref":"88:26:1","root_ar":"","surface_ar":"ثُمَّ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:26:2:1","qac_word_ref":"88:26:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:26:3:1","qac_word_ref":"88:26:3","root_ar":"","surface_ar":"عَلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:26:3:2","qac_word_ref":"88:26:3","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"حِسَاب","morph_features":"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:26:4:1","qac_word_ref":"88:26:4","root_ar":"ح س ب","surface_ar":"حِسَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:26:4:2","qac_word_ref":"88:26:4","root_ar":"","surface_ar":"هُم"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:26:1:1"],["88:26:2:1"],["88:26:3:1","88:26:3:2"],["88:26:4:1","88:26:4:2"]],"word_analysis_refs":["88:26:1","88:26:2","88:26:3","88:26:4"],"word_rows":[{"analysis_record_ref":"88:26:1","analytic_gloss_range_en":"ordered transition, with resumptive force; locally stages reckoning after return rather than merely starting a new sentence","analytic_root_gloss_range_en":null,"qac_refs":["88:26:1:1"],"root":{},"surface":{"arabic":"ثُمَّ","transliteration":"thumma"}},{"analysis_record_ref":"88:26:2","analytic_gloss_range_en":"emphatic sentence-launching particle governing the whole final nominal clause","analytic_root_gloss_range_en":null,"qac_refs":["88:26:2:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"88:26:3","analytic_gloss_range_en":"upon Us, with local incumbency and responsibility force; fronted as the predicate before the account is named","analytic_root_gloss_range_en":null,"qac_refs":["88:26:3:1","88:26:3:2"],"root":{},"surface":{"arabic":"عَلَيْنَا","transliteration":"ʿalaynā"}},{"analysis_record_ref":"88:26:4","analytic_gloss_range_en":"their reckoning, account, audit, or account-settlement; locally the delayed governed noun whose suffix makes the liability theirs","analytic_root_gloss_range_en":"root range includes counting, reckoning, deeming, sufficiency, counted worth, reward-counting, and accountable management; local sense selects reckoning/accounting while nearby branches color completeness and evaluation only under guardrail limits","qac_refs":["88:26:4:1","88:26:4:2"],"root":{"arabic":"ح س ب","transliteration":"ḥ-s-b"},"surface":{"arabic":"حِسَابَهُم","transliteration":"ḥisābahum"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:26"],"branch_refs":["root_000318/B001"],"candidate_id":"cand_a4e0fe6ca1974e8d2796","evidence_scope":"focus_ayah","hft_ref":"hft_eae4ed394559ad80dadf","item_id":"baseline_complete_reckoning","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_complete_reckoning","support_id":"sup_e97007a94d2330c09300"},{"anchor_refs":["88:26"],"branch_refs":["root_000318/B006"],"candidate_id":"cand_0c8e0e4e66e50ed1c0db","evidence_scope":"focus_ayah","hft_ref":"hft_40f2c3d92ff7d91c6fe7","item_id":"baseline_accountable_custody","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_accountable_custody","support_id":"sup_bbd518d33ca711827004"},{"anchor_refs":["88:26"],"branch_refs":["root_000318/B003"],"candidate_id":"cand_808152b76e5963944876","evidence_scope":"focus_ayah","hft_ref":"hft_1a9610ae6b80c3375933","item_id":"baseline_sufficient_settlement","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_sufficient_settlement","support_id":"sup_5a0899d3cd7396aa3741"},{"anchor_refs":["88:26"],"branch_refs":["root_000318/B002"],"candidate_id":"cand_b5c9ca19b5d577545362","evidence_scope":"focus_ayah","hft_ref":"hft_b3925232812c2b3ee6bb","item_id":"baseline_estimate_overruled","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_estimate_overruled","support_id":"sup_b2f3834fe17247f1c19c"}],"diagnostics":[],"lane_counts":{"global":16,"macro":7,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:26","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:26","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"88:26","lane":"micro","linguistic_source_ref":"88:26","surface_ref":"88:26","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:26","target_tokens":[["Sonra",["88:26:1"]],["onların",["88:26:4"]],["hesabını",["88:26:4"]],["görmek",["88:26:4"]],["kesinlikle",["88:26:2"]],["bize",["88:26:3"]],["düşer",["88:26:3"]]],"text":"Sonra onların hesabını görmek kesinlikle bize düşer."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:objective-idafa","source_type":"word_analysis","support_id":"sup_006fab176325abcf376b","text":"{\"blocking_evidence\":null,\"headline\":\"possession becomes being audited\",\"reader_payoff\":\"The reader notices that the group grammatically possesses the account while also being the ones accounted for.\",\"reason\":\"The construct relation ties the suffix to the noun, and the local reckoning semantics make the possessed account an audit of them rather than property they control.\",\"representative_source_ids\":[\"QG-1192c5f6\",\"QS-8d94c57b\",\"QY-ebd0a18b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2","source_type":"word_analysis","support_id":"sup_007a4e593ba6818c6cb0","text":"{\"gloss_range\":\"emphatic sentence-launching particle governing the whole final nominal clause\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) certifies the whole final assignment, not only the reckoning noun. Its scope covers the fronted {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) and the delayed {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}), so both divine responsibility and their account arrive as one emphatic assertion. The kasra form launches an independent declaration after {{ar:ثُمَّ}} ({{tr:thumma}}), not a subordinate complement, and the nominal architecture states reckoning as settled responsibility rather than narrating an accounting action. After reminder and non-control, the particle also presses against evasion: reckoning may not be humanly compelled, but its divine assignment is made certain. Its doubled sound makes certainty audible at the start, and the following n-sound in {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) carries that pressure into the responsible speaker before the account appears.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:fawasil-pairing","source_type":"word_analysis","support_id":"sup_1640ba1e86da49b78871","text":"{\"blocking_evidence\":null,\"headline\":\"shared ending binds return to account\",\"reader_payoff\":\"The reader hears {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) and {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) rhyme as the paired final movement.\",\"reason\":\"The adjacent verse endings share the long ā plus b-hum cadence, making the return-account sequence audible.\",\"representative_source_ids\":[\"QP-d51ae9a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:incumbency-not-destination","source_type":"word_analysis","support_id":"sup_26c31f62c2664d0fbe65","text":"{\"blocking_evidence\":null,\"headline\":\"destination turns into responsibility\",\"reader_payoff\":\"The reader notices the local pivot from return-to-Us in 88:25 to account-upon-Us in 88:26.\",\"reason\":\"The preposition changes from the destination relation in 88:25 to {{ar:عَلَى}} ({{tr:ʿalā}}) in 88:26, and the local predicate relation selects incumbency with residual upon-pressure.\",\"representative_source_ids\":[\"QG-00a4fef7\",\"QS-db6d2fb7\",\"QT-93e3d18e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3","source_type":"word_analysis","support_id":"sup_28f2b69d409cd1e9e0e6","text":"{\"gloss_range\":\"upon Us, with local incumbency and responsibility force; fronted as the predicate before the account is named\",\"prose\":\"{{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) changes the relation from destination to incumbency. The same divine suffix heard in 88:25 remains, but the preposition shifts from return-to-Us to account-upon-Us, making the divine speaker the bearer of reckoning responsibility. Because the phrase is fronted as the predicate under {{ar:إِنَّ}} ({{tr:inna}}), the listener hears the responsible party before {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) is named, with restriction-like pressure that reserves final accounting to that speaker. The suffix is not a separate noun; it is fused to the preposition, so the surface form itself carries the move from endpoint to obligation. This also answers the earlier denied control-domain in 88:22: control is not over them for the messenger, while final accounting is upon Us. The repeated nasal texture makes that responsible pronoun prominent before the account arrives.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَيْنَا}} ({{tr:ʿalaynā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:process-and-result","source_type":"word_analysis","support_id":"sup_3c48b0b46275938a3b68","text":"{\"blocking_evidence\":null,\"headline\":\"reckoning as procedure and settlement\",\"reader_payoff\":\"The reader notices that the noun can carry both the act of reckoning and the settled account produced by it.\",\"reason\":\"The gerund form names reckoning substantively, allowing process and result to remain visible without introducing a finite-tense accounting verb.\",\"representative_source_ids\":[\"QS-6a9e8393\",\"MF-0c17c514\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:destination-to-burden-boundary","source_type":"word_analysis","support_id":"sup_426837f7e7618b92042a","text":"{\"blocking_evidence\":null,\"headline\":\"arrival becomes accounting procedure\",\"reader_payoff\":\"The reader notices the boundary movement from arrival at the divine endpoint to the procedure that follows that arrival.\",\"reason\":\"The boundary rows connect 88:25's return-to-Us with 88:26's account-upon-Us, so the closing unit moves from motion to audit.\",\"representative_source_ids\":[\"ME-826d58af\",\"QB-3f444527\",\"QB-56a20653\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:1:resumptive-closing-assertion","source_type":"word_analysis","support_id":"sup_4a65324482fd60d94203","text":"{\"blocking_evidence\":null,\"headline\":\"linked sequel becomes a fresh declaration\",\"reader_payoff\":\"The reader notices that the account statement remains connected to the prior ayah while also standing as the surah's final declaration.\",\"reason\":\"The particle can resume discourse while sequencing it, so 88:26 is neither detached from 88:25 nor reduced to a mere parallel assertion.\",\"representative_source_ids\":[\"QG-5a61aeb7\",\"QS-95860d39\",\"QT-bba7df3b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:certified-responsibility-scope","source_type":"word_analysis","support_id":"sup_4d7d9e729b0b4d32e26a","text":"{\"blocking_evidence\":null,\"headline\":\"upon-Us falls inside certainty\",\"reader_payoff\":\"The reader notices that the upon-Us relation is the certified claim of the clause, with restriction-like pressure toward divine responsibility.\",\"reason\":\"{{ar:إِنَّ}} ({{tr:inna}}) scopes over the fronted predicate, and the fronting gives qaṣr-like pressure without needing to add an explicit exclusivity word.\",\"representative_source_ids\":[\"QG-6e9795e7\",\"QS-cf2a5d26\",\"QI-6ad834e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:sufficiency-value-color","source_type":"word_analysis","support_id":"sup_508c308a2c1e68d70ca2","text":"{\"blocking_evidence\":null,\"headline\":\"adequacy colors the account\",\"reader_payoff\":\"The reader notices that the account feels complete and sufficient to settle the matter, while the local noun still selects reckoning rather than a separate enoughness formula.\",\"reason\":\"V4 lists sufficiency, worth, reward-counting, and accountable-management branches, but local grammar and context select the reckoning-accounting noun; the broader branches survive only as adequacy and value-assessment pressure.\",\"representative_source_ids\":[\"QS-6d551f8f\",\"QS-83f3c747\",\"QI-19952072\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:governed-delayed-account","source_type":"word_analysis","support_id":"sup_6162f2cc12164413e680","text":"{\"blocking_evidence\":null,\"headline\":\"account arrives after responsibility\",\"reader_payoff\":\"The reader notices that the account is delayed until the divine responsibility frame has already been heard.\",\"reason\":\"{{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) is the delayed governed noun of {{ar:إِنَّ}} ({{tr:inna}}), while {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) is the fronted predicate.\",\"representative_source_ids\":[\"QG-289bfd0c\",\"QG-75e48862\",\"MG-8559c805\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:personal-account-liability","source_type":"word_analysis","support_id":"sup_62c22820fe4fa06f1411","text":"{\"blocking_evidence\":null,\"headline\":\"their account, not abstract reckoning\",\"reader_payoff\":\"The reader notices that the suffix turns reckoning into their attached liability rather than a generic doctrine.\",\"reason\":\"The attached 3mp suffix is the genitive possessor in an idafa-like construction, making {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) definite by relation to the liable group.\",\"representative_source_ids\":[\"QG-43b680bf\",\"QG-c599e90b\",\"QF-7061ed8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:masdar-charge-not-verb","source_type":"word_analysis","support_id":"sup_648a2e7e869202bb4345","text":"{\"blocking_evidence\":null,\"headline\":\"substantive charge replaces finite narration\",\"reader_payoff\":\"The reader notices that the ayah names the account as a substantive charge upon Us instead of narrating Us accounting them with a finite verb or agent title.\",\"reason\":\"The local form is a gerund; 2:284 provides a concrete finite divine-accounting contrast, while 88:26 makes accountability a noun-charge placed upon Us.\",\"representative_source_ids\":[\"QF-e7e4feda\",\"QF-f7370ecb\",\"QI-7cdfaf97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:1:sequel-after-return","source_type":"word_analysis","support_id":"sup_6b5fa21c5613d0d458f6","text":"{\"blocking_evidence\":null,\"headline\":\"return is followed by account\",\"reader_payoff\":\"The reader notices that the final ayah is heard through 88:25: return comes first, and reckoning is the ordered sequel.\",\"reason\":\"QAC marks the word as a sequential conjunction, and the CRITICAL boundary rows tie it specifically to the movement from 88:25 return into 88:26 account.\",\"representative_source_ids\":[\"QG-03bf460d\",\"QT-47c9a509\",\"QB-515d6c0b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:1:sound-handoff-to-certainty","source_type":"word_analysis","support_id":"sup_8ac2e78e9329f7522f2a","text":"{\"blocking_evidence\":null,\"headline\":\"nasal handoff into emphasis\",\"reader_payoff\":\"The reader hears the pressed transition of {{ar:ثُمَّ}} ({{tr:thumma}}) move directly into the emphatic certainty of {{ar:إِنَّ}} ({{tr:inna}}).\",\"reason\":\"The phonetic point is local and limited: the geminated nasal close of {{ar:ثُمَّ}} ({{tr:thumma}}) prepares the doubled nasal onset of {{ar:إِنَّ}} ({{tr:inna}}) without changing the syntax.\",\"representative_source_ids\":[\"QP-0019c17b\",\"QP-70613dc4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:pronoun-routing","source_type":"word_analysis","support_id":"sup_8d6ede5780dbcc4bab27","text":"{\"blocking_evidence\":null,\"headline\":\"suffix keeps the accountable group in view\",\"reader_payoff\":\"The reader notices continuity between the group whose return was named in 88:25 and the group whose account closes 88:26.\",\"reason\":\"Attachment evidence treats the suffix antecedent as discourse-linked and target-language-sensitive; the row's payoff is continuity of liability, not a forced single antecedent label.\",\"representative_source_ids\":[\"QG-0ade9bd6\",\"QB-313f85c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:local-reckoning-field","source_type":"word_analysis","support_id":"sup_8efbb8112e04e25507af","text":"{\"blocking_evidence\":null,\"headline\":\"measured audit, not vague aftermath\",\"reader_payoff\":\"The reader notices that the final noun names measured reckoning and audit, not an undefined post-return consequence.\",\"reason\":\"V4's accepted counting-and-reckoning branch supports the local accounting sense, and the closing warning context gives it judicial accountability force.\",\"representative_source_ids\":[\"QS-7a549260\",\"QS-89e37289\",\"QS-ba5b7375\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:general-tail-after-specific-warning","source_type":"word_analysis","support_id":"sup_94f9a4365066d52c2cab","text":"{\"blocking_evidence\":null,\"headline\":\"specific warning opens into total account\",\"reader_payoff\":\"The reader notices that the closing account gathers the preceding warning sequence into a total reckoning frame.\",\"reason\":\"After the messenger's limited role and the refuser's punishment profile, the final account noun generalizes the accountability that remains.\",\"representative_source_ids\":[\"QT-8c5e3f3e\",\"QB-78cb28f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2:certainty-against-evasion","source_type":"word_analysis","support_id":"sup_9820401eb529ea9bb3e4","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis presses against evasion\",\"reader_payoff\":\"The reader notices that the particle strengthens the truth of reckoning after reminder and non-control, where evasion might otherwise be imagined.\",\"reason\":\"The particle adds no new actor; its local payoff is assertive force over the final assignment of reckoning to the divine speaker.\",\"representative_source_ids\":[\"QS-3c7f497c\",\"MS-3199e746\",\"QI-e4ceffbf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:1:procedural-rank-not-clock","source_type":"word_analysis","support_id":"sup_a7bbbacff2588e82a218","text":"{\"blocking_evidence\":null,\"headline\":\"delay marks staged procedure\",\"reader_payoff\":\"The reader notices that {{ar:ثُمَّ}} ({{tr:thumma}}) separates return and account as ordered stages without requiring speculation about duration.\",\"reason\":\"The particle's sequential force licenses staged procedure; the local evidence does not require a claim about how much time passes between return and reckoning.\",\"representative_source_ids\":[\"QG-f3719a74\",\"MG-4cf69499\",\"QS-6427afe2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:singular-account-plural-group","source_type":"word_analysis","support_id":"sup_a86f6cea805bcab8abbf","text":"{\"blocking_evidence\":null,\"headline\":\"one account gathers a plural group\",\"reader_payoff\":\"The reader notices one accountable file or process gathering a plural group without dissolving their liability.\",\"reason\":\"The head noun is masculine singular while the attached possessor is third-person masculine plural.\",\"representative_source_ids\":[\"QF-afa53407\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2:governed-delayed-ism","source_type":"word_analysis","support_id":"sup_aca26fd561f413139372","text":"{\"blocking_evidence\":null,\"headline\":\"delayed account remains under inna\",\"reader_payoff\":\"The reader notices that the account is delayed for emphasis but still grammatically governed by the opening particle.\",\"reason\":\"The fronted predicate does not make the final noun independent; local syntax keeps the account inside the emphatic construction begun by {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-f3fb28c6\",\"QT-95c35d73\",\"QY-4b4f30e0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:final-surah-seal","source_type":"word_analysis","support_id":"sup_addcd459634b7b803c3d","text":"{\"blocking_evidence\":null,\"headline\":\"surah closes on accountability\",\"reader_payoff\":\"The reader notices that the surah's last word leaves the account itself as the final reality after reminder, refusal, return, and punishment.\",\"reason\":\"{{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) is both the ayah-final and surah-final word, so accountability receives the closing position.\",\"representative_source_ids\":[\"QT-27b6668b\",\"QT-36b39286\",\"QY-5f49cd4d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:settled-nominal-assignment","source_type":"word_analysis","support_id":"sup_ae5598a4dc7ca9a3b6fc","text":"{\"blocking_evidence\":null,\"headline\":\"verbless architecture makes assignment settled\",\"reader_payoff\":\"The reader notices that reckoning is presented as an established assignment rather than narrated as a future action.\",\"reason\":\"The local clause uses an emphatic nominal predication with no finite verb of accounting or judging, so the relation stands as settled responsibility.\",\"representative_source_ids\":[\"QG-4580c120\",\"QT-e3a29d8e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:account-sound-texture","source_type":"word_analysis","support_id":"sup_b0df08837744c3ad99e4","text":"{\"blocking_evidence\":null,\"headline\":\"sound tightens the final account\",\"reader_payoff\":\"The reader hears the final account word enclosed by nasal sounds and given a measured consonant texture.\",\"reason\":\"The sound rows remain local recitation texture: they support closure and tightness around {{ar:حِسَاب}} ({{tr:ḥisāb}}) without creating a separate semantic branch.\",\"representative_source_ids\":[\"QP-49c69e96\",\"QP-cfbc0ab8\",\"MP-583ea3dc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4","source_type":"word_analysis","support_id":"sup_b23b17ec736643d08848","text":"{\"gloss_range\":\"their reckoning, account, audit, or account-settlement; locally the delayed governed noun whose suffix makes the liability theirs\",\"prose\":\"{{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) is delayed until the clause has already certified whose responsibility the account is. Its suffix makes the reckoning definite and personal: not abstract accountability in general, but their account, the account taken of them; the same suffix chain keeps the group of the return in view while allowing the warning's broader audience to remain implicated. The singular verbal noun gathers a plural group into one accountable process and result, while withholding a finite verb so reckoning stands as a substantive charge placed upon Us, unlike a performed-action report such as 2:284's finite divine accounting. The {{ar:ح س ب}} ({{tr:ḥ-s-b}}) field gives that charge measured accounting, audit, and evaluation rather than raw aftermath; sufficiency and value-counting branches can color the account as complete and adequate, but the local sense remains reckoning-accounting. As the final word of the ayah and surah, {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) turns the return of 88:25 into a paired closing: their return is to Us, then their account is upon Us, and the preceding specific warnings open into a total reckoning frame. The sound pairing with {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) makes that sequence audible as well as grammatical, while nasal enclosure and the breathy-to-sibilant account stem give the final word a measured edge.\",\"root_display\":\"{{ar:ح س ب}} ({{tr:ḥ-s-b}})\",\"root_gloss_range\":\"root range includes counting, reckoning, deeming, sufficiency, counted worth, reward-counting, and accountable management; local sense selects reckoning/accounting while nearby branches color completeness and evaluation only under guardrail limits\",\"surface_display\":\"{{ar:حِسَابَهُم}} ({{tr:ḥisābahum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:evaluative-counting","source_type":"word_analysis","support_id":"sup_bc054adb3f962af5a215","text":"{\"blocking_evidence\":null,\"headline\":\"counting includes assessment\",\"reader_payoff\":\"The reader notices that reckoning is evaluative as well as numerical: what they are counted as answerable for is assessed.\",\"reason\":\"The supposition/deeming branch should not replace local reckoning, but it coherently supports the evaluative side of accounting in this warning context.\",\"representative_source_ids\":[\"QS-a2755915\",\"MS-eb1f299a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:26:4:1","source_type":"qac_morpheme","support_id":"sup_c1121e6b556c222d6a2b","text":"{\"lemma_ar\":\"حِسَاب\",\"morph_features\":\"STEM|POS:N|VN|(III)|LEM:HisaAb|ROOT:Hsb|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:26:4:1\",\"qac_word_ref\":\"88:26:4\",\"root_ar\":\"ح س ب\",\"surface_ar\":\"حِسَابَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:nasal-lead-to-account","source_type":"word_analysis","support_id":"sup_c18f0517b43e7d82eab3","text":"{\"blocking_evidence\":null,\"headline\":\"sound foregrounds the responsible party\",\"reader_payoff\":\"The reader hears the repeated nasal sounds of {{ar:إِنَّ عَلَيْنَا}} ({{tr:inna ʿalaynā}}) hold attention on the responsible party before the account noun arrives.\",\"reason\":\"The sound claim is a local recitation texture and does not alter the syntactic role of the prepositional phrase.\",\"representative_source_ids\":[\"QP-ff633039\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:1","source_type":"word_analysis","support_id":"sup_c59219deda976c2ab3ab","text":"{\"gloss_range\":\"ordered transition, with resumptive force; locally stages reckoning after return rather than merely starting a new sentence\",\"prose\":\"{{ar:ثُمَّ}} ({{tr:thumma}}) makes the last ayah a sequel to the return just asserted in 88:25. It does not only open another sentence; it stages {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) as the next procedural reality after arrival, while still giving the final assertion its own closing force. The particle also keeps the relation from becoming a flat schedule or an immediate fā-like consequence: the delay can mark rank and ordered procedure, not merely elapsed clock-time. Its compressed nasal ending then hands the listener into {{ar:إِنَّ}} ({{tr:inna}}), so transition and certainty are heard together before the account is named.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ثُمَّ}} ({{tr:thumma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2:independent-final-assertion","source_type":"word_analysis","support_id":"sup_c7cd7f8730f79fcb799f","text":"{\"blocking_evidence\":null,\"headline\":\"kasra form launches declaration\",\"reader_payoff\":\"The reader notices that the final clause is a fresh certified declaration rather than a dependent clause folded into the previous statement.\",\"reason\":\"The visible kasra-initial particle supports sentence-launching emphasis, while the preceding {{ar:ثُمَّ}} ({{tr:thumma}}) supplies the discourse link.\",\"representative_source_ids\":[\"QG-fbcde6b0\",\"QF-5e4d0e86\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:denied-control-resolved-by-account","source_type":"word_analysis","support_id":"sup_c8395154f850b3e285ae","text":"{\"blocking_evidence\":null,\"headline\":\"authority becomes reckoning, not coercion\",\"reader_payoff\":\"The reader notices that the earlier denial of messenger control is resolved by divine accounting rather than by coercion.\",\"reason\":\"The same closing unit contrasts denied control in 88:22 with the assignment of {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) to Us in 88:26.\",\"representative_source_ids\":[\"QE-c54a30ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:common-root-final-gerund","source_type":"word_analysis","support_id":"sup_cdd9e482f57b3a42d717","text":"{\"blocking_evidence\":null,\"headline\":\"broad root lands as final noun\",\"reader_payoff\":\"The reader notices that a widely distributed reckoning root is concentrated into the surah's last substantive noun.\",\"reason\":\"The contextual profile shows the exact root-form is not rare, so the payoff is not rarity but concentration of a common reckoning field at the surah close.\",\"representative_source_ids\":[\"QI-5eb76171\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:4:return-account-formal-pair","source_type":"word_analysis","support_id":"sup_ce8a2bfe66aa4fa04336","text":"{\"blocking_evidence\":null,\"headline\":\"return and account share a bound shape\",\"reader_payoff\":\"The reader notices that 88:25 and 88:26 pair return and account through matching verbal-noun-plus-suffix surfaces.\",\"reason\":\"The concrete pair is {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) in 88:25 and {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) in 88:26, with the same attached plural suffix shape but a change from return to reckoning.\",\"representative_source_ids\":[\"QF-7471a149\",\"QE-7d06bd96\",\"MT-8adbf54c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:fronted-responsibility-focus","source_type":"word_analysis","support_id":"sup_d071a52ceaeae40b2f39","text":"{\"blocking_evidence\":null,\"headline\":\"responsibility is heard before account\",\"reader_payoff\":\"The reader notices that the clause foregrounds who bears the account before stating what the account is.\",\"reason\":\"Attachment evidence identifies {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) as the fronted predicate and {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) as the delayed subject-like governed noun.\",\"representative_source_ids\":[\"QG-e38f16f8\",\"MG-fcd8a2d8\",\"QT-82721094\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:same-divine-suffix","source_type":"word_analysis","support_id":"sup_d8b58c4316c8ed376500","text":"{\"blocking_evidence\":null,\"headline\":\"same speaker, new prepositional host\",\"reader_payoff\":\"The reader notices that the same divine first-person plural remains while the fused preposition changes the relation.\",\"reason\":\"The suffix is bound to the preposition rather than stated as a separate noun, so the surface form itself makes divine responsibility visible through the prepositional relation.\",\"representative_source_ids\":[\"QG-74065f63\",\"QF-6c80b601\",\"QF-7883a438\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2:audible-emphasis","source_type":"word_analysis","support_id":"sup_df6abac4488c3b12a7dd","text":"{\"blocking_evidence\":null,\"headline\":\"doubled nūn carries certainty forward\",\"reader_payoff\":\"The reader hears the emphatic pressure of {{ar:إِنَّ}} ({{tr:inna}}) continue into {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}).\",\"reason\":\"The sound rows are locally coherent: the doubled nūn of {{ar:إِنَّ}} ({{tr:inna}}) and the nūn in {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) bind emphasis to the responsible pronoun.\",\"representative_source_ids\":[\"QF-f4e90ecb\",\"QP-434ded5c\",\"QP-6d44550b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:3:answers-denied-control","source_type":"word_analysis","support_id":"sup_ea0062d8a8c0c95a41c1","text":"{\"blocking_evidence\":null,\"headline\":\"denied over-them becomes upon-Us\",\"reader_payoff\":\"The reader notices that the control denied over them in 88:22 is resolved by assigning final account upon Us in 88:26.\",\"reason\":\"The local echo is concrete: 88:22 denies {{ar:عَلَيْهِم}} ({{tr:ʿalayhim}}) as the messenger's control-domain, and 88:26 states {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) as the divine responsibility frame.\",\"representative_source_ids\":[\"MI-08f34ce4\",\"QE-f649c01a\",\"QY-5a43ce71\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:26:2:whole-clause-certification","source_type":"word_analysis","support_id":"sup_f6317758f37919a22595","text":"{\"blocking_evidence\":null,\"headline\":\"certainty covers responsibility and account\",\"reader_payoff\":\"The reader notices that certainty is placed over the entire accountability architecture, not merely over a single noun.\",\"reason\":\"Attachment evidence makes {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}) the governed delayed noun and {{ar:عَلَيْنَا}} ({{tr:ʿalaynā}}) the fronted predicate under {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-50d35492\",\"MG-9c743a32\",\"QT-2bc557aa\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and reckoning supplies the literal audit image and anchors a complete, proportioned account of them.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"God takes upon Himself the complete reckoning of each person's case, with nothing delegated or left uncounted.","before":"God will generally judge them."},"confidence":"strong","focus_anchor":"The noun حسابهم at 88:26[4], with the possessive suffix and fronted علينا, makes their reckoning the responsibility assumed by the speaker.","mechanism":"Counting becomes a complete account of what belongs to each person, while علينا marks custody of both the procedure and its completion.","model_id":"baseline_complete_reckoning"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_complete_reckoning","source_type":"hft","support_id":"sup_e97007a94d2330c09300","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000318","role":"Supervision and accountable management supplies the literal administrative image and makes علينا an assignment of jurisdiction.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"Their entire accountability is an affair God undertakes, administers, and brings to resolution.","before":"Their account is a number God will calculate."},"confidence":"medium","focus_anchor":"حسابهم remains the focus noun, but علينا can frame it as an affair placed under divine responsibility rather than only a computed total.","mechanism":"The supervision branch turns reckoning into accountable management: the clause assigns an ongoing jurisdiction and not merely a moment of arithmetic.","model_id":"baseline_accountable_custody"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_accountable_custody","source_type":"hft","support_id":"sup_bbd518d33ca711827004","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000318","role":"Sufficiency and enoughness supplies a settling image: the divinely undertaken account is enough to resolve their case.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"The undertaken reckoning is also the sufficient settlement of all that is due from and to them.","before":"حسابهم names only an inventory of deeds."},"confidence":"exploratory","focus_anchor":"The same ح س ب root in حسابهم carries a branch of sufficiency, while علينا presents the matter as something the speaker guarantees.","mechanism":"Enoughness recasts the account as a settlement sufficient to dispose of every claim concerning them, without replacing the noun's primary reckoning sense.","model_id":"baseline_sufficient_settlement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_sufficient_settlement","source_type":"hft","support_id":"sup_5a0899d3cd7396aa3741","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000318/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000318","role":"Reckoning as supposition supplies the literal mental-estimate image and lets علينا reserve the conclusive estimate for God.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"It also places every estimate, including their own expectations about themselves, under a final divine determination.","before":"The verse concerns only an external audit performed on them."},"confidence":"exploratory","focus_anchor":"The possessive حسابهم can momentarily leave open whether the reckoning is merely of them or also the reckoning they form, while علينا relocates final determination.","mechanism":"The supposition branch creates an epistemic edge: human estimates remain provisional because the decisive reckoning rests with God.","model_id":"baseline_estimate_overruled"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_estimate_overruled","source_type":"hft","support_id":"sup_b2f3834fe17247f1c19c","trust":"legacy_unbound"}]}
</lane_packet_json>
