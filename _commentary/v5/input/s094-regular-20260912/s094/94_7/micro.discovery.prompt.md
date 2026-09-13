# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **94:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s094-regular-20260912/s094/94_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "94:7",
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
{"branch_registry":[{"boundary":"Dal hem uğraşın bitmesini hem de iç dünyadaki belirli bir içeriğin yokluğunu kapsar; dökme, genişlik, karşılıksız kan ve yönelme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001147/B001","candidate_links":[{"candidate_id":"cand_1cf3500c040656af62e5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"meşguliyetten çıkma veya içi boş kalma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir uğraşın bitmesi ve kişinin artık o işle meşgul olmaması dalın temel yüzüdür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin sabırdan veya akıldan yoksun kalması, genel boş kalma durumunun iç dünyaya uzanan kullanımıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Korkunun kalplerden gitmesi, içte bulunan bir durumun ortadan kalkması olarak anlatılır."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iş sonrasında serbest kalma çekirdeğini ve iç dünyadaki belirli bir içerikten yoksunluğu birlikte karşılar.","boundary_detail":"Dal hem uğraşın bitmesini hem de iç dünyadaki belirli bir içeriğin yokluğunu kapsar; dökme, genişlik, karşılıksız kan ve yönelme anlamlarını kapsamaz.","branch_image_ar":"الخلو بعد الشغل","concept_gloss":"meşguliyetten çıkma veya içi boş kalma","contextual_glosses":[{"applicability":"Bir işin tamamlanması ve kişinin artık onunla uğraşmaması anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalbin sabırdan, akıldan veya korkudan boşalması yüzünü taşımaz.","preserves":"Meşguliyetin sona ermesiyle serbest kalma yüzünü korur."},"facet_ids":["F001"],"text":"işini bitirip boşalmak","usage_role":"contextual"},{"applicability":"Kalpte sabır ya da akıl kalmaması veya korkunun kalpten gitmesi gibi iç durumlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işin bitmesiyle meşguliyetten çıkma yüzünü taşımaz.","preserves":"İç dünyadaki belirli bir içeriğin yok olmasını korur."},"facet_ids":["F002","F003"],"text":"içi bomboş kalmak","usage_role":"contextual"}],"definition":"Bir işin veya uğraşın sona ermesiyle artık onunla meşgul olmama ya da bir şeyden yoksun kalarak boş bulunma durumudur. Kalp bağlamında sabır, akıl veya korku gibi iç durumların ortadan kalkmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir uğraşın bitmesi ve kişinin artık o işle meşgul olmaması dalın temel yüzüdür."},{"facet_id":"F002","role":"extension","statement":"Kalbin sabırdan veya akıldan yoksun kalması, genel boş kalma durumunun iç dünyaya uzanan kullanımıdır."},{"facet_id":"F003","role":"extension","statement":"Korkunun kalplerden gitmesi, içte bulunan bir durumun ortadan kalkması olarak anlatılır."}],"identity_rationale":"Dalın meşguliyetin sona ermesiyle boş kalma çerçevesi kaynak ifadesinin ana bölümünü karşılar; ancak kaynak, kalbin sabırdan veya akıldan yoksun kalmasını ve korkunun kalpten gitmesini de aynı dalda verir. Bu nedenle kimlik korunmalı, fakat yalnız iş sonrası boşlukla sınırlandırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"işi bitip boş kalmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"meşguliyetsizlik, boş zaman"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boş, sabırdan veya akıldan yoksun"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"korku kalplerinden gitti"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"boşaltılmış, içi boş"}],"lexicalization_note":"Tanım, yalın biçimlerdeki meşguliyetsizlik ile kalbe ve korkuya bağlı özel kullanımları ayrı yüzler olarak tutar; özel kalıpları bütün dala yaymaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Yayımlanan iki ilişki, genel boşlukla kısmi örtüşmeyi ve meşguliyetle doğrudan karşıtlığı gösterir; diğerleri yer boşluğu, zamanın geçmesi, bekleme veya bu kökün ayrı anlam dalları olduğu için sınırı daha fazla keskinleştirmez.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, işin tamamlanmasıyla meşguliyetin sona ermesine ve kalpteki iç durumların silinmesine bağlıdır; komşu dal ise nesne, yer ve sahiplik alanlarına yayılan daha genel bir boşluk alanı kurar.","focus_only":"Bir uğraşın bitmesi ve kalpteki sabır, akıl veya korku gibi bir içeriğin ortadan kalkması özellikle öne çıkar.","gloss":"boş olma ve boş kalma","neighbor_only":"Kap, ev, el, hesap veya akıl gibi çok çeşitli şeylerin bir içerikten ya da değerden yoksunluğu kapsanır.","neighbor_ref":"root_000869/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin beklenen içerikten veya meşguliyetten yoksun bulunmasını anlatır."},{"boundary_match":"opposed","distinction":"Odak dal meşguliyetin sona eren kutbudur; komşu dal ise kişiyi dolduran ve başka bir işten alıkoyabilen meşguliyet kutbudur.","focus_only":"İşin bitmesiyle kişinin artık meşgul olmaması anlatılır.","gloss":"boşluk ve meşguliyet karşıtlığı","neighbor_only":"Kişiyi tutan, oyalayan veya başka bir şeyden alıkoyan iş ve meşguliyet anlatılır.","neighbor_ref":"root_000801/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal kişinin bir işle meşgul olup olmama durumunu aynı eksende ele alır."}],"source_phrase_ar":"الفراغ خلاف الشغل (maqayis;mufradat)؛ فرغت من الشغل (sihah)؛ فؤاد أم موسى فارغا أي خاليا من الصبر (ayn)؛ كأنما فرغ من لبها (mufradat)؛ حتى إذا فرغ عن قلوبهم أي ذهب بالخوف (ayn)","source_summary":"Kaynakların ortak çerçevesi, meşguliyetin karşıtı olan boş kalmayı ve bir işin sona ermesini temel alır; aynı çerçeve kalbin sabırdan ya da akıldan yoksun oluşuna ve korkunun kalpten gitmesine de uygulanır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الفراغ خلاف الشغل؛ خلو القلب؛ الفراغ من العمل","what_is_not_ar":"الصب من الوعاء؛ السعة؛ هدر الدم؛ القصد إلى الأمر"},"support_links":["sup_9faef572502a2fdd2210"]},{"boundary":"Dal dökme ve dökerek boşaltma çekirdeğiyle sınırlıdır; yalnız boş kalmayı, genişliği veya başka dallardaki sonuç anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001147/B002","candidate_links":[{"candidate_id":"cand_eefbe890023c35a8c3c6","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"dökerek boşaltma veya akıp dökülme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kaptaki suyu veya başka bir içeriği dökerek kabı boşaltmak dalın eylem çekirdeğidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun akıp dökülmesi ve kişinin suyu kendi üzerine dökmesi aynı sıvı hareketinin farklı katılımcı düzenleridir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kovanın suyun döküldüğü deliği veya yanı, dökme eylemine göre adlandırılan özel bir nesne bölümüdür."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kovanın ön ve arka su çıkışlarından ad alan iki ay konağı, nesne bölümünden türemiş bir adlandırmadır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Sabrın muhataplara bolca verilmesi, sıvı dökme görüntüsünün soyut bir niteliğe aktarılmasıdır."}},{"facet_id":"F006","role":"specialization","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Kenarları dolu halkanın dökülerek yapılması, eylemin üretim tekniğine bağlı özel bir kullanımdır."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Daldaki temel ettirgen dökme ve kendiliğinden akıp dökülme düzenlerini birlikte karşılar; nesne ve mecaz uzantıları bu çekirdeğe bağlıdır.","boundary_detail":"Dal dökme ve dökerek boşaltma çekirdeğiyle sınırlıdır; yalnız boş kalmayı, genişliği veya başka dallardaki sonuç anlamlarını içermez.","branch_image_ar":"الصب وإخلاء الوعاء","concept_gloss":"dökerek boşaltma veya akıp dökülme","contextual_glosses":[{"applicability":"Bir kapta bulunan suyun veya başka bir içeriğin dökülerek çıkarıldığı geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıvının akıp dökülmesini ve nesne, mecaz, adlandırma ile döküm uzantılarını taşımaz.","preserves":"İçeriğin dökülmesiyle kabın boşaltılmasını korur."},"facet_ids":["F001"],"text":"döküp boşaltmak","usage_role":"general"},{"applicability":"Suyun bir yerden akarak döküldüğü ve ayrı bir dökenin öne çıkarılmadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kabın bilinçli biçimde boşaltılmasını ve buna bağlı özel uzantıları taşımaz.","preserves":"Sıvının akışla dışarı çıkması yüzünü korur."},"facet_ids":["F002"],"text":"akıp dökülmek","usage_role":"contextual"},{"applicability":"Kovanın içindeki suyun döküldüğü delik veya yan bölüm adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dökme eylemini, sıvının akışını ve diğer mecaz ya da üretim uzantılarını taşımaz.","preserves":"Dökülme yönüne göre tanımlanan kova bölümünü korur."},"facet_ids":["F003"],"text":"su çıkış ağzı","usage_role":"explanatory"},{"applicability":"Kenarları dolu bir halkanın dökme yöntemiyle üretildiğini açıklayan nesne bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıvı boşaltma, akma, kova çıkışı ve mecaz aktarım yüzlerini taşımaz.","preserves":"Dökme eyleminin üretim tekniğine dönüşen özel yüzünü korur."},"facet_ids":["F006"],"text":"dökümle yapılmış halka","usage_role":"explanatory"}],"definition":"Bir kaptaki suyu ya da başka bir içeriği dökerek kabı boşaltma veya sıvının dökülüp akmasıdır. Bu çekirdeğe bağlı olarak kovanın su çıkışı ve ondan ad alan iki ay konağı, suyu kişinin üzerine dökmesi, sabrın bolca verilmesi, kapların boşaltılması ve dökümle oluşturulan dolu kenarlı halka anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kaptaki suyu veya başka bir içeriği dökerek kabı boşaltmak dalın eylem çekirdeğidir."},{"facet_id":"F002","role":"extension","statement":"Suyun akıp dökülmesi ve kişinin suyu kendi üzerine dökmesi aynı sıvı hareketinin farklı katılımcı düzenleridir."},{"facet_id":"F003","role":"specialization","statement":"Kovanın suyun döküldüğü deliği veya yanı, dökme eylemine göre adlandırılan özel bir nesne bölümüdür."},{"facet_id":"F004","role":"associated_use","statement":"Kovanın ön ve arka su çıkışlarından ad alan iki ay konağı, nesne bölümünden türemiş bir adlandırmadır."},{"facet_id":"F005","role":"extension","statement":"Sabrın muhataplara bolca verilmesi, sıvı dökme görüntüsünün soyut bir niteliğe aktarılmasıdır."},{"facet_id":"F006","role":"specialization","statement":"Kenarları dolu halkanın dökülerek yapılması, eylemin üretim tekniğine bağlı özel bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi suyu veya kaptaki içeriği dökme, kabı boşaltma ve suyun akıp dökülmesi çekirdeğini açıkça kurar. Kovanın su çıkışı, bu çıkışlardan ad alan iki ay konağı, kişinin suyu kendi üzerine dökmesi, sabır aktarımı ve döküm halka da bu çekirdeğe bağlı özel kullanımlar olarak verilir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"döküp boşaltmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bize bol bol sabır vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"su akıp döküldü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dökerek boşaltmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kapları boşaltma"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"suyu kendi üzerine dökmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kovanın su çıkış ağzı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kovanın suyun döküldüğü yanı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kovanın ön ve arka su çıkışlarından ad alan iki ay konağı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"dökümle yapılmış, kenarları dolu halka"}],"lexicalization_note":"Tanım, dökme ve akma çekirdeğini; kap boşaltma, kova çıkışı, mecaz aktarım ve döküm nesnesi gibi biçim ya da kalıp bağımlı yüzlerden ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilenler genel dökme, güçlü sıvı çıkışı ve dolu kova alanlarıyla en açıklayıcı sınırları kurar; öteki adaylar yalnız kova türü, kap kalıntısı, özel dökme tekniği, yürütme aracı veya bu kökün ayrı dalları düzeyinde kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kap içeriğini dökerek boşaltma düzenini ve bundan doğan nesne ile mecazları kurar; komşu dal ise sıvının birden ve güçlü biçimde dışarı atılmasına odaklanır.","focus_only":"Kabın dökülerek boşaltılması, kova çıkışı, ay konağı adlandırması, sabır aktarımı ve döküm halka uzantıları bulunur.","gloss":"sıvıyı dökme ve dışarı akıtma","neighbor_only":"Sıvının tek seferde güçlü biçimde fışkırması ve gözyaşı ya da çiy gibi çeşitli sıvılara yayılması özellikle öne çıkar.","neighbor_ref":"root_000481/B001","relation_type":"near_synonym","shared_zone":"İki dal da su veya başka bir sıvının bir kaynaktan dışarı çıkıp dökülmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal dökme ile kabı boşaltma arasındaki ilişkiyi ve sıvının akışını kurar; komşu dal yalnız genel bir dökme eylemini sınırlı bir söz varlığı içinde bildirir.","focus_only":"Boşaltılan kap, akan su, su çıkışı ve dökme çekirdeğine bağlı özel uzantılar ayrıntılı biçimde yer alır.","gloss":"bir şeyi dökmek","neighbor_only":"Dökme anlamı belirli bir sözcüğün sınırlı kullanımında genel nesneye yöneltilir.","neighbor_ref":"root_001288/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı bir şeyin dökülerek yer değiştirmesidir."},{"boundary_match":"partial","distinction":"Odak dal suyun kovadan çıkışını ve kabın boşalmasını anlatır; komşu dal ise su taşıyan dolu kovayı ve onun miktar ya da verme işlevini anlatır.","focus_only":"Kovanın içeriğini dökme, boşaltma ve su çıkışını adlandırma eylem merkezini oluşturur.","gloss":"dolu kova ve kovanın boşaltılması","neighbor_only":"Dolu veya doluya yakın büyük kovanın kendisi, onun doldurulması ve ölçü olarak verilmesi merkezdedir.","neighbor_ref":"root_000677/B001","relation_type":"near_neighbor","shared_zone":"İki dal kova, içindeki su ve suyun dökülmesi sahnesini paylaşır."}],"source_phrase_ar":"الفرغ مفرغ الدلو الذي ينصب منه الماء (maqayis)؛ أفرغت الماء صببته وافترغت إذا صببت الماء على نفسك (maqayis)؛ الفراغ ناحيته التي يصب الماء منها (ayn)؛ فرغ الماء انصب وأفرغت الدلاء أرقتها وفرغته تفريغا (sihah)؛ تفريغ الظروف إخلاؤها (sihah)؛ أفرغت الدلو صببت ما فيه ومنه استعير أفرغ علينا صبرا (mufradat)؛ الفرغان فرغ الدلو المقدم وفرغ الدلو المؤخر (sihah)؛ حلقة مفرغة لأنه شيء يصب صبا (maqayis)","source_summary":"Kaynakların ortak anlatımı, kaptaki suyu dökerek boşaltmayı ve suyun akıp dökülmesini merkeze alır. Kova çıkışı, bu çıkışlardan ad alan ay konakları, kap boşaltma, kişinin üzerine su dökmesi, sabrın bolca verilmesi ve döküm halka bu merkezin nesne, mecaz ve üretim uzantılarıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"صب الماء أو ما في الدلو؛ انصباب الماء؛ صب الماء على النفس؛ تفريغ الظروف؛ مخرج الماء من الدلو وما سمي منه الفرغان؛ الحلقة المصبوبة","what_is_not_ar":"الفراغ من الشغل؛ السعة في المشي والضرب؛ هدر الدم؛ النطفة"},"support_links":["sup_e8415fc36a3b17a7ffa5"]},{"boundary":"Buradaki ortaklık hız veya güç değil, yalnız belirtilen at, darbe, saplama ve yol nitelemelerindeki genişliktir.","branch_kind":"collocation","branch_ref":"root_001147/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"geniş adımlı, geniş izli veya enli olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın yürüyüşünün veya koşusunun geniş adımlı olması, hareket alanındaki özel nitelemedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Darbe veya saplamanın geniş olması ve darbeden kan akması, etkinin kapladığı genişliği anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolun enli olması, aynı genişlik niteliğinin mekansal bir güzergaha uygulanmasıdır."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız atın hareketi, darbe ya da saplamanın etkisi ve yolun eni için verilen niteleme kalıplarını birlikte karşılar.","boundary_detail":"Buradaki ortaklık hız veya güç değil, yalnız belirtilen at, darbe, saplama ve yol nitelemelerindeki genişliktir.","branch_image_ar":"السعة في الحركة والأثر","concept_gloss":"geniş adımlı, geniş izli veya enli olma","contextual_glosses":[{"applicability":"Atın yürüyüşünün veya koşusunun adım genişliğiyle nitelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Darbe, saplama ve yol için verilen genişlik yüzlerini taşımaz.","preserves":"At hareketindeki genişlik niteliğini korur."},"facet_ids":["F001"],"text":"geniş adımlı","usage_role":"contextual"},{"applicability":"Bir darbe veya saplamanın geniş bir açıklık bırakıp kan akıttığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"At hareketi ile yolun enine ilişkin nitelemeleri taşımaz.","preserves":"Darbe ve saplamanın geniş etkisini korur."},"facet_ids":["F002"],"text":"geniş yara açan","usage_role":"contextual"},{"applicability":"Yolun dar olmayıp geniş bir geçiş alanı sunduğu bağlamda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"At hareketi ile darbe ve saplamanın genişliği yüzlerini taşımaz.","preserves":"Yolun genişliği ve eni yüzünü korur."},"facet_ids":["F003"],"text":"enli","usage_role":"contextual"}],"definition":"Yalnız belirtilen niteleme kalıplarında, atın yürüyüş veya koşusunun geniş adımlı; darbe ya da saplamanın geniş bir iz veya açıklık bırakır nitelikte; yolun ise enli olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın yürüyüşünün veya koşusunun geniş adımlı olması, hareket alanındaki özel nitelemedir."},{"facet_id":"F002","role":"specialization","statement":"Darbe veya saplamanın geniş olması ve darbeden kan akması, etkinin kapladığı genişliği anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yolun enli olması, aynı genişlik niteliğinin mekansal bir güzergaha uygulanmasıdır."}],"identity_rationale":"Kaynak ifadesi atın yürüyüşü veya koşusu ile darbe ve saplamadaki genişliği açıkça destekler; ayrıca yolun enli oluşunu da aynı niteleme grubuna katar. Bu yüzden hareket ve etki çerçevesi kullanılabilir, ancak yol örneğini dışarıda bırakmayacak biçimde genişlik ortak paydasında sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geniş adımlı yürüyen veya koşan at"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"geniş yara açıp kan akıtan darbe"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"geniş yara açan saplama"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"enli yol"}],"lexicalization_note":"Tanım yalnız sağlanan at, darbe, saplama ve yol niteleme kalıplarına bağlıdır; bunlardan bağımsız yalın bir genişlik anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilen üç ilişki genişliği hız, hafiflik ve atılgan yürüyüşten ayırır; öteki adaylar ayak aşınması, toynak vuruşu, özel koşu biçimleri veya bu kökün anlamca ayrı dalları olduğundan ek bir yakınlık sağlamaz.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal hareketin hızını değil adımın genişliğini bildirir; komşu dal ise genişliği değil hız ve koşu gücünü öne çıkarır.","focus_only":"Atın yürüyüş veya koşusundaki geniş adım açıklığı anlatılır.","gloss":"geniş adım ile hızlı koşu","neighbor_only":"Atın koşuya hazır oluşu ve hızlı koşması anlatılır.","neighbor_ref":"root_000270/B004","relation_type":"same_field","shared_zone":"İki dal da atın yürüyüşünü veya koşusunu niteleyen özellikler alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal hareketin veya etkinin kapladığı genişliği anlatır; komşu dal ise aynı sahnelerde uzuvların hafifliğini ve hızını anlatır.","focus_only":"At hareketi ile darbe veya saplamanın genişliği ortak niteliktir.","gloss":"genişlik ile hareket hafifliği","neighbor_only":"Bacak ya da el hareketindeki hafiflik, hız ve kapıp geçme niteliği ortaktır.","neighbor_ref":"root_000727/B006","relation_type":"same_field","shared_zone":"İki dal hem hayvan hareketi hem de vurma ya da saplama sahnelerine dokunur."},{"boundary_match":"field_only","distinction":"Odak dal adımın genişliğini ölçü alır; komşu dal ise yürüyüşteki hazırlanma ve atılganlık biçimini ölçü alır.","focus_only":"Atın geniş adımlı yürümesi veya koşması söz konusudur.","gloss":"geniş adım ile atılgan yürüyüş","neighbor_only":"Yürüyenin belirli bir yürüyüş biçiminde tetikte ve atılmaya hazır hareket etmesi söz konusudur.","neighbor_ref":"root_000500/B005","relation_type":"same_field","shared_zone":"İki dal yürüyüş biçimini bedensel hareket özelliğiyle niteler."}],"source_phrase_ar":"فرس فريغ أي واسع المشي (maqayis;sihah)؛ ضربة فريغ واسعة وطعنة أيضا وطريق فريغ واسع (maqayis)؛ الطعنة الفرغاء ذات الفرغ وهو السعة (sihah)؛ فرس فريغ واسع العدو وضربة فريغة واسعة ينصب منها الدم (mufradat)","source_summary":"Kaynakların ortak malzemesi atın geniş adımlı yürüyüşü veya koşusu ile geniş darbe ve saplamayı verir; yolun enli oluşu da aynı niteleme alanına eklenir. Darbenin kan akıtması geniş etkinin sonucu olarak belirtilir.","sources":["MQ","SI","MU"],"what_is_ar":"السعة في مشي الفرس أو عدوه؛ السعة في الضربة والطعنة والطريق","what_is_not_ar":"الخلو من الشغل؛ الصب؛ هدر الدم؛ النطفة"},"support_links":[]},{"boundary":"Dal yalnız kanın karşılıksız kalıp öcünün aranmamasını bildiren kalıba bağlıdır; sıradan dökülme veya genel kayıp anlamına yayılmaz.","branch_kind":"collocation","branch_ref":"root_001147/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"kanı yerde kalmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Öldürülen kişinin kanının boşa ve karşılıksız gitmesi sonuç durumudur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu kan için öç veya hak aranmaması, karşılıksız kalma sonucunu kuran zorunlu koşuldur."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir öldürmenin ardından öç veya hak aranmadığı ve kanın karşılıksız kaldığı bütün dal bağlamını doğal biçimde karşılar.","boundary_detail":"Dal yalnız kanın karşılıksız kalıp öcünün aranmamasını bildiren kalıba bağlıdır; sıradan dökülme veya genel kayıp anlamına yayılmaz.","branch_image_ar":"الدم المهدور","concept_gloss":"kanı yerde kalmak","contextual_glosses":[{"applicability":"Öldürülen kişinin kanı için herhangi bir karşılık veya öç aranmadığı anlatıda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kanın karşılıksız kalması ve hesabının sorulmaması anlamını korur."},"facet_ids":["F001","F002"],"text":"kanı boşa gitmek","usage_role":"contextual"},{"applicability":"Kan görüntüsünü yinelemeden, ölüm için öç ya da hak aranmadığını açıklamak gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölümün karşılıksız bırakılması ve istem yokluğu koşulunu açıkça korur."},"facet_ids":["F001","F002"],"text":"ölümünün hesabı sorulmamak","usage_role":"explanatory"}],"definition":"Yalnız kanın gitmesi biçimindeki kalıpta, öldürülen kimsenin kanının karşılıksız kalması ve onun için öç ya da hak aranmamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Öldürülen kişinin kanının boşa ve karşılıksız gitmesi sonuç durumudur."},{"facet_id":"F002","role":"core","statement":"Bu kan için öç veya hak aranmaması, karşılıksız kalma sonucunu kuran zorunlu koşuldur."}],"identity_rationale":"Kaynak ifadesi kanın boşa veya karşılıksız gitmesini, onun için bir istemde ya da öç arayışında bulunulmamasıyla açıklar. Geçici dal çerçevesi bu sonuç ve koşulu eksiltmeden yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kanı yerde kaldı, öcü aranmadı"}],"lexicalization_note":"Tanım yalnız kanın boşa gitmesini bildiren sabit anlatım içinde geçerlidir ve yalın biçime genel bir karşılıksızlık anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilenler tam eşdeğer sonucu, kan bedeli ve bağışlama ayrıntılarını ve öç istemiyle karşıtlığı gösterir; diğer adaylar daha genel sorumsuzluk, tazminat düzeni veya aynı kökün ayrı anlam dalları olduğu için ek ayrım sağlamaz.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarında anlam sınırı bakımından bir ayrım görünmez; iki dal aynı sonucu farklı söz varlığıyla dile getirir.","focus_only":null,"gloss":"kanın karşılıksız kalması","neighbor_only":null,"neighbor_ref":"root_000125/B005","relation_type":"synonym","shared_zone":"Her iki dal da kanın boşa gitmesini ve ölüm için karşılık aranmamasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal karşılık aranmamasını genel bırakır; komşu dal hem öcün hem de kan bedelinin yokluğunu ayrı ayrı sınırlar.","focus_only":"Kanın boşa gitmesi ve onun için istemde bulunulmaması genel sonuç olarak verilir.","gloss":"öçsüz ve karşılıksız kalan kan","neighbor_only":"Öç alınmamasına ek olarak kan bedelinin de elde edilmemesi açıkça belirtilir.","neighbor_ref":"root_000127/B006","relation_type":"near_synonym","shared_zone":"İki dal da öldürülen kişinin kanının yerde kalması ve öcünün alınmaması alanını paylaşır."},{"boundary_match":"exact","distinction":"Komşu kartındaki bağışlama ve istemden vazgeçme durumları aynı sonucu örnekler; iki dalın anlam sınırı arasında ayrım yoktur.","focus_only":null,"gloss":"karşılıksız kalıp istenmeyen kan","neighbor_only":null,"neighbor_ref":"root_001581/B003","relation_type":"synonym","shared_zone":"İki dal da hakkında istemde bulunulmayan ve karşılıksız kalan kanı anlatır."},{"boundary_match":"opposed","distinction":"Odak dal arayışın bulunmadığı kutbu anlatır; komşu dal ise kaybın öç istemi doğurduğu karşı kutbu anlatır.","focus_only":"Ölüm için öç veya hak aranmaması söz konusudur.","gloss":"öcü aranmayan kan ile öç istemi","neighbor_only":"Bir öldürme ya da ağır kayıp, kişide öç istemi ve takip edilecek bir hak doğurur.","neighbor_ref":"root_001621/B002","relation_type":"polarity_pair","shared_zone":"İki dal öldürme veya ağır kayıp sonrasında öç ve hak arama ekseninde buluşur."}],"source_phrase_ar":"ذهب دمه فرغا أي باطلا لم يطلب به (maqayis)؛ ذهب دمه فرغا وفرغا أي هدرا لم يطلب به (sihah)؛ ذهب دمه فرغا أي مصبوبا ومعناه باطلا لم يطلب به (mufradat)","source_summary":"Kaynakların ortak açıklaması, kanın boşa ve karşılıksız gitmesini onun için bir istemde bulunulmamasına bağlar. Dökülme görüntüsü anılsa bile okuyucuya sunulan anlam, kanın yalnız akması değil hesabının sorulmamasıdır.","sources":["MQ","SI","MU"],"what_is_ar":"ذهاب الدم باطلا أو هدرا دون طلب بثأره","what_is_not_ar":"الفراغ من الشغل؛ الصب المجرد؛ السعة؛ النطفة"},"support_links":[]},{"boundary":"Dal erkeğin döl sıvısını adlandırır; cinsel birleşme, sıvının dışarı çıkması, rahme bırakılması veya boşalma öncesi başka bir sıvı bu kimliğin parçası değildir.","branch_kind":"bare","branch_ref":"root_001147/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"erkeğin döl sıvısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, erkeğin döl sıvısıdır ve dalda ayrıca bir eylem veya sonuç bildirilmez."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek göndergesini gündelik ve açıklayıcı Türkçeyle eksiksiz karşılar.","boundary_detail":"Dal erkeğin döl sıvısını adlandırır; cinsel birleşme, sıvının dışarı çıkması, rahme bırakılması veya boşalma öncesi başka bir sıvı bu kimliğin parçası değildir.","branch_image_ar":"ماء الرجل","concept_gloss":"erkeğin döl sıvısı","contextual_glosses":[{"applicability":"Erkeğe ait üreme sıvısının yalın ve gündelik bir ifadeyle anılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkeğe ait döl sıvısı göndergesini doğrudan korur."},"facet_ids":["F001"],"text":"erkeğin döl suyu","usage_role":"contextual"}],"definition":"Erkeğe ait döl sıvısını adlandıran yalın bir isimdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, erkeğin döl sıvısıdır ve dalda ayrıca bir eylem veya sonuç bildirilmez."}],"identity_rationale":"Kaynak ifadesi bu biçimi doğrudan erkeğin döl sıvısı olarak tanımlar. Geçici çerçeve aynı göndergeden söz eder ve başka bir süreç, katılımcı ya da sonuç eklemez.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"erkeğin döl sıvısı"}],"lexicalization_note":"Tanım, kanıtta yalın bir ad olarak verilen döl sıvısı anlamıyla sınırlıdır ve komşu eylem ya da ilişki kalıplarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilenler aynı göndergeyi, benzetmeli adlandırmayı, karıştırılabilecek başka bir sıvıyı ve sıvının rahme bırakılması olayını ayırır; diğerleri cinsel birleşme veya sıvının çıkışı gibi daha uzak olaylardır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Komşu kartındaki çocuğun oluşumuna kaynak olma açıklaması aynı göndergenin bağımlı niteliğidir; iki dalın anlam sınırı arasında ayrım yoktur.","focus_only":null,"gloss":"erkeğin döl sıvısı","neighbor_only":null,"neighbor_ref":"root_001450/B002","relation_type":"synonym","shared_zone":"İki dal erkeğin üremeyle ilgili döl sıvısını aynı gönderge alanında ele alır."},{"boundary_match":"partial","distinction":"Odak dal göndergesi için doğrudan bir ad sunar; komşu dal aynı göndergeyi ürün veren tohum düşüncesi üzerinden kurar.","focus_only":"Döl sıvısı doğrudan ve mecazsız bir adlandırmayla gösterilir.","gloss":"döl sıvısı ve tohum benzetmesi","neighbor_only":"Erkeğin döl sıvısı, ekilecek ürün görüntüsünden yararlanan bir benzetmeyle adlandırılır.","neighbor_ref":"root_000630/B004","relation_type":"near_synonym","shared_zone":"İki dalın göndergesi erkeğin döl sıvısıdır."},{"boundary_match":"partial","distinction":"Odak dal döl sıvısına gönderir; komşu dal ise ondan önce çıkabilen ve aynı olmayan başka bir sıvıyı gösterir.","focus_only":"Üremeyle ilgili döl sıvısı anlatılır.","gloss":"döl sıvısı ile ön sıvı","neighbor_only":"Döl sıvısından önce çıkan farklı bir erkek beden sıvısı anlatılır.","neighbor_ref":"root_000760/B005","relation_type":"near_neighbor","shared_zone":"İki dal erkek bedeninden cinsel bağlamda çıkan sıvıları konu alır."},{"boundary_match":"partial","distinction":"Odak dal bir maddeyi adlandırır; komşu dal ise o maddenin bir katılımcı tarafından rahme bırakılması eylemini anlatır.","focus_only":"Erkeğe ait döl sıvısının kendisi adlandırılır.","gloss":"döl sıvısı ve rahme bırakılması","neighbor_only":"Erkeğin bu sıvıyı dişinin rahmine bırakması olayı anlatılır.","neighbor_ref":"root_001458/B004","relation_type":"near_neighbor","shared_zone":"İki dal erkek döl sıvısı ve üreme sahnesinde buluşur."}],"source_phrase_ar":"الفراغة ماء الرجل وهو النطفة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu adlandırma yalnız bir kaynakta erkeğin döl sıvısı olarak verilir."}],"source_summary":"Dalın kaynak malzemesi tek ve doğrudan bir adlandırma sunar: söz konusu biçim erkeğin döl sıvısını gösterir.","sources":["SI"],"what_is_ar":"الفَراغة ماء الرجل وهي النطفة","what_is_not_ar":"الفراغ من الشغل؛ الصب؛ السعة؛ هدر الدم"},"support_links":[]},{"boundary":"Dal yalnız belirtilen yönelme ve kendini ayırma kalıplarında geçerlidir; salt boş olma, hazırlık, fiziksel varış veya genel niyet kavramlarının tamamını kapsamaz.","branch_kind":"collocation","branch_ref":"root_001147/B006","candidate_links":[{"candidate_id":"cand_fd2c0d0c34b75b9243ff","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","surface_ar":"فَرَغْ"}],"gloss":"birine veya işe yönelip kendini ona verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye veya işe bilerek yönelmek ve onu amaç edinmek temel yönelim yüzüdür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka uğraşları geride bırakıp kendini belirli bir işe vermek, yönelimin özel ve yoğunlaşmış gerçekleşmesidir."}}],"root_ar":"ف ر غ","root_id":"root_001147","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ya da işi amaç edinme çekirdeğiyle, belirli bir işe özel olarak ayrılma yüzünü birlikte karşılar.","boundary_detail":"Dal yalnız belirtilen yönelme ve kendini ayırma kalıplarında geçerlidir; salt boş olma, hazırlık, fiziksel varış veya genel niyet kavramlarının tamamını kapsamaz.","branch_image_ar":"القصد إلى الأمر","concept_gloss":"birine veya işe yönelip kendini ona verme","contextual_glosses":[{"applicability":"Yönelimin hedefi belirli bir kişi olduğunda doğal ve kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işe yönelme ve kendini yalnız o işe ayırma yüzünü taşımaz.","preserves":"Belirli bir hedefe bilinçli yönelme çekirdeğini korur."},"facet_ids":["F001"],"text":"birine yönelmek","usage_role":"contextual"},{"applicability":"Yönelimin hedefi bir iş veya mesele olduğunda ve bilinçli amaç vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendini o işe özel olarak ayırma ve başka uğraşlardan çekilme yüzünü taşımaz.","preserves":"Bir işe bilerek yönelip onu hedef alma yüzünü korur."},"facet_ids":["F001"],"text":"bir işi amaç edinmek","usage_role":"contextual"},{"applicability":"Kişinin başka uğraşlardan çekilip bütün dikkatini belirli bir işe ayırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir kişiye ya da işe yalnızca yönelme ve onu amaç edinme yüzünü taşımaz.","preserves":"Kendini belirli bir işe ayırma ve yoğunlaşma yüzünü korur."},"facet_ids":["F002"],"text":"kendini bir işe vermek","usage_role":"contextual"}],"definition":"Yalnız belirtilen yönelme kalıplarında, bir kişiye veya işe bilerek yönelip onu amaç edinme; dönüşlü yapıda ise başka uğraşlardan sıyrılarak kendini belirli bir işe verme anlamıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye veya işe bilerek yönelmek ve onu amaç edinmek temel yönelim yüzüdür."},{"facet_id":"F002","role":"extension","statement":"Başka uğraşları geride bırakıp kendini belirli bir işe vermek, yönelimin özel ve yoğunlaşmış gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi bir kişiye veya işe bilerek yönelmeyi ve belirli bir iş için kendini ayırmayı aynı yönelim alanında verir. Geçici dal çerçevesi hem amaç edinme çekirdeğini hem de kendini tek bir işe verme uzantısını doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"size yöneleceğiz"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir işe bilerek yönelmek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kendini belirli bir işe vermek"}],"lexicalization_note":"Tanım sağlanan kişi ya da işe yönelme ve kendini belirli işe verme kalıplarına bağlıdır; bu anlamı yalın biçime veya her türlü amaç bildirimine yaymaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilenler yalın amaç edinme, hazırlık, genel yönelme ve özenli hedef seçmeyle en yararlı sınırları kurar; diğerleri niyet, yön tayini, buyruk ya da aynı kökün ayrı anlam dalları olarak daha uzak kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Temel yönelme yüzünde iki dal büyük ölçüde örtüşür; odak dal buna kendini o işe özel olarak ayırma yüzünü eklediği için bütün sınırda birbirinin yerine geçmez.","focus_only":"Kendini belirli bir işe ayırıp başka uğraşlardan çekilme yüzü de bulunur.","gloss":"bir işe bilerek yönelmek","neighbor_only":null,"neighbor_ref":"root_001207/B010","relation_type":"near_synonym","shared_zone":"İki dal da bir işi bilinçli biçimde hedef almayı ve ona yönelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal yönelimi kendini hedefe ayırmaya kadar yoğunlaştırır; komşu dal ise yönelimden önceki karar ve hazırlık aşamalarını da kapsar.","focus_only":"Başka uğraşlardan çekilip kendini belirli bir işe verme anlamı vardır.","gloss":"amaç edinme ve hazırlanma","neighbor_only":"Hedefe yönelmenin yanı sıra hazırlanma, karar verme ve yola koyulmaya hazır olma anlamları vardır.","neighbor_ref":"root_000003/B002","relation_type":"near_synonym","shared_zone":"İki dal belirli bir işi amaç edinme ve ona bilinçli biçimde yönelme alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dal belirli kalıplarda amaç edinme ve kendini işe ayırmayla sınırlıdır; komşu dal fiziksel yaklaşma ve genel zihinsel yönelimi de kapsayan daha geniş bir alana sahiptir.","focus_only":"Kendini belirli bir işe ayırma ve ona yoğunlaşma yüzü bulunur.","gloss":"hedefe yönelme ve kendini işe verme","neighbor_only":"Hedefe doğru gitme, ona varma ve onu zihinde tutma gibi daha genel yönelim yüzleri bulunur.","neighbor_ref":"root_001230/B001","relation_type":"near_synonym","shared_zone":"İki dal bir kişi veya şeyi hedef alıp ona yönelme çekirdeğinde buluşur."},{"boundary_match":"partial","distinction":"Odak dal hedefe ayrılma ve yoğunlaşmayı anlatır; komşu dal ise hedefi arayıp seçmedeki dikkat ve özeni öne çıkarır.","focus_only":"Kendini belirli bir işe ayırma ve başka uğraşlardan çekilme yüzü vardır.","gloss":"yönelme ve özenle hedef seçme","neighbor_only":"Hedefi araştırarak veya özenle seçerek ona yönelme niteliği özellikle öne çıkar.","neighbor_ref":"root_000020/B003","relation_type":"near_synonym","shared_zone":"İki dal bir şeyi bilinçli biçimde hedef alma ve ona yönelme alanını paylaşır."}],"source_phrase_ar":"سنفرغ أي نعمد (maqayis)؛ فرغت إلى أمر كذا أي عمدت له (maqayis)؛ تفرغت لكذا (sihah)","source_summary":"Kaynakların ortak alanı bir kişi veya işe bilerek yönelip onu amaç edinmektir. Kendini belirli bir işe ayırma kullanımı, bu yönelimi başka uğraşlardan çekilip tek bir hedefe yoğunlaşma olarak özelleştirir.","sources":["MQ","SI"],"what_is_ar":"العمد إلى الأمر والتوجه له؛ التفرغ لشيء بعينه","what_is_not_ar":"الخلو المجرد؛ الصب؛ السعة؛ هدر الدم"},"support_links":["sup_eae703f666f77d883fbd"]},{"boundary":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_eefbe890023c35a8c3c6","lane":"micro"},{"candidate_id":"cand_fd2c0d0c34b75b9243ff","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"dikme, dik durma ve yükselme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel bir nesnenin dik konuma getirilmesini veya bir varlığın dik ve yükselmiş durumda bulunmasını birlikte anlatır.","boundary_detail":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_image_ar":"إقامة الشيء منتصبا بارزا","concept_gloss":"dikme, dik durma ve yükselme","contextual_glosses":[{"applicability":"Mızrak, taş, direk, yapı veya benzeri bir nesne dik konuma getirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi dik ve belirgin konuma getiren fiziksel işlemi tam olarak korur."},"facet_ids":["F001"],"text":"dikmek","usage_role":"contextual"},{"applicability":"Bir insanın, hayvanın ya da beden bölümünün yükselmiş ve dik durumda bulunmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı veya beden bölümü için dik ve yükselmiş durumu eksiksiz korur."},"facet_ids":["F002"],"text":"dik durmak","usage_role":"contextual"},{"applicability":"Tozun yerden kalkıp havada belirginleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun yukarı doğru hareket edip görünür hâle gelmesini korur."},"facet_ids":["F003"],"text":"havaya yükselmek","usage_role":"contextual"}],"definition":"Bir şeyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirmek ya da yükseltmek; ayrıca bir varlığın veya bölümünün bu biçimde dik durmasıdır. Tozun yükselmesi ve belirli nesnelerin kurulması bu uzamsal çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."},{"facet_id":"F002","role":"core","statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."},{"facet_id":"F003","role":"extension","statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."},{"facet_id":"F004","role":"associated_use","statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}],"identity_rationale":"Dalın kimliği, bir şeyi dik ve belirgin duracak biçimde yerleştirme veya yükseltme çekirdeğini doğru yansıtır. Boynuz, göğüs ve baş gibi bölümlerin dik durması ile tozun yükselmesi aynı uzamsal görünümün geçişsiz gerçekleşmeleridir; perde kaldırma ve tuzak kurma ise belirli nesnelerle sınırlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi dikmek veya dik konuma kaldırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"boynuzları dik olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boynuzu dik veya göğsü yüksek dişi hayvan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"havaya yükselmiş toz"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"perdeyi kaldırmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuş avlamak için tuzak kurmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kazanın üzerine konduğu demir destek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dikili direk veya sütun"}],"lexicalization_note":"Tanım, yalın dikme ve dik durma çekirdeğini özel nesnelerle kurulan perde kaldırma, tuzak kurma ve kazan desteği gibi kullanımlardan açıkça ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; çoğu yalnızca diklik senaryosunu paylaşan nesne, özel kullanım veya diğer kök anlamıdır. Okur açısından en yakın sınır karışıklığını dikilme ve sabit kalma adayı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın merkezi yerleştirme ve yükseltmedir; komşu dalın merkezi ise dik duruşla birlikte sabitlik ve bir yere bağlı kalmadır.","focus_only":"Odak dal, bir nesneyi dik konuma getiren geçişli işlemi ve toz gibi şeylerin yükselmesini de kapsar.","gloss":"dikilme ve sabit kalma","neighbor_only":"Komşu dal, yerde veya bir şey üzerinde sabit kalma, bağlanma ve sıkıca yapışma anlamlarını da taşır.","neighbor_ref":"root_000232/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın dik veya yükselmiş durumda bulunmasını anlatabilir."}],"source_phrase_ar":"أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)","source_summary":"Anlamın ortak çekirdeği, bir şeyi dik ve görünür konuma getirme ile bu konumda bulunmadır. Nesne örnekleri mızrak, yapı, taş, perde ve tuzağı; durum örnekleri ise dik boynuz, yükselmiş göğüs ve havaya kalkmış tozu kapsar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصب الشيء وإقامته ورفعه قائما، كنصب الرمح والبناء والحجر والستر والشرك، وقيام الشخص أو الحيوان منتصب الرأس أو القرن أو الصدر، وارتفاع الغبار ونحوه","what_is_not_ar":"لا يختص بالعبادة ولا بالحظ ولا بالتعب إلا إذا صرحت العبارة بذلك"},"support_links":["sup_e8415fc36a3b17a7ffa5","sup_eae703f666f77d883fbd"]},{"boundary":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_kind":"bare","branch_ref":"root_001507/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"tapınma veya adak kesme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinsel amaçla dikilmiş, tapınılan ya da üzerinde adak hayvanı kesilen taş için kullanılır.","boundary_detail":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_image_ar":"حجر منصوب للعبادة والذبح","concept_gloss":"tapınma veya adak kesme taşı","contextual_glosses":[{"applicability":"Taşın doğrudan kutsal nesne sayılıp kendisine tapınıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın doğrudan tapınma nesnesi olmasını tam olarak korur."},"facet_ids":["F001"],"text":"tapınılan dikili taş","usage_role":"contextual"},{"applicability":"Hayvanın taş üzerinde kesildiği veya kanının taş üzerine döküldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın kesim ve kan dökme törenindeki özel işlevini korur."},"facet_ids":["F002"],"text":"adak kesme taşı","usage_role":"contextual"}],"definition":"Tapınmak, çevresinde dönmek, yakınlık sunmak veya üzerinde adak kesip kan dökmek için dikilmiş taş ya da bu tür taşlardan oluşan kutsal nesnedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."},{"facet_id":"F002","role":"core","statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}],"identity_rationale":"Dal, dikilmiş taşın tapınma, çevresinde dönme, adak kesme veya kan dökme amacıyla kullanılan kutsal nesne oluşunu doğru biçimde birleştirir. Taşın yalnızca dikili olması yeterli değildir; dinsel yönelim ya da kesim işlevi anlamın ayırt edici koşuludur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"tapınılan veya üzerinde adak kesilen dikili taş"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tapınılan ya da adak kesilen dikili taşlar"}],"lexicalization_note":"Tanım yalın taş adını dinsel işleviyle verir ve başka dallardaki sıradan dikili taş anlamlarını bu çekirdeğe katmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kesme, adak, çevresinde dönme ve belirli put adları senaryonun ayrı parçalarıdır. En yararlı karşılaştırma, dikili tören taşı ile genel tapınma nesnesi arasındaki sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikili taş ve onun kesim törenindeki kullanımıyla sınırlıdır; komşu dal ise tapınılan nesnenin biçimini veya tören işlevini böyle sınırlamaz.","focus_only":"Odak dal, taşın dikili olmasını ve üzerinde kesim yapılıp kan dökülmesi işlevini özellikle içerir.","gloss":"tapınma nesnesi","neighbor_only":"Komşu dal, taşla sınırlı olmayan tapınma nesnelerini ve putları daha genel biçimde kapsar.","neighbor_ref":"root_001624/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların tapındığı cansız ve kutsallaştırılmış bir nesneyi kapsayabilir."}],"source_phrase_ar":"النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)","source_summary":"Ortak anlatım, taşın dikilmiş olmasını tapınma ve kesim törenleriyle birlikte verir. Taş hem tapınılan bir nesne hem de adak hayvanının kesildiği ve kanının döküldüğü tören odağı olabilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب والأنصاب: حجارة منصوبة كانت تعبد أو يذبح عليها أو تصب عليها دماء الذبائح","what_is_not_ar":"لا يدخل مطلق العلامة أو حجارة الحوض إذا لم تكن عبادة أو ذبحا"},"support_links":[]},{"boundary":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001507/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"sınır işareti veya kuyu-havuz taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yeri belirleyen dikili işaretlerle kuyu ya da havuz çevresine yerleştirilen taşları kapsar.","boundary_detail":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_image_ar":"علامة أو حجارة منصوبة للحد أو الحوض","concept_gloss":"sınır işareti veya kuyu-havuz taşı","contextual_glosses":[{"applicability":"Bir topluluğun yerini veya kutsal sayılan bir bölgenin sınırını belirtme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın yer veya sınır bildiren işaret işlevini korur."},"facet_ids":["F001"],"text":"dikili sınır taşı","usage_role":"contextual"},{"applicability":"Kuyu veya havuz ağzının çevresine yerleştirilen taşlardan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın su yapısının çevresini ve kenarını oluşturma işlevini korur."},"facet_ids":["F002"],"text":"kuyu ya da havuz kenarı taşı","usage_role":"contextual"}],"definition":"Bir topluluğu veya sınırı göstermek için dikilen işaret ya da kuyu ve havuz kenarına destek veya çevre oluşturacak biçimde yerleştirilen taştır. Taşlardan kurulmuş havuzun kendisi de bu düzenlemeden doğan adlaşmış bir anlamdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."},{"facet_id":"F002","role":"specialization","statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."},{"facet_id":"F003","role":"extension","statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}],"identity_rationale":"Dal, bir topluluğu ya da sınırı gösteren dikili işaret ile kuyu veya havuz kenarına yerleştirilen taşları kaynak ifadesine uygun biçimde kapsar. Taşlardan yapılmış havuz adı bu yerleştirme düzeninden doğan adlaşmış bir uzantıdır; tapınma işlevi bu dalın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dikili işaret veya havuz kenarı taşı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kuyu ya da havuz ağzının çevresine dizilen taşlar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"taşlardan kurulmuş havuz"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluk veya sınır için dikilmiş işaret"}],"lexicalization_note":"Tanım, yalın adların işaret ve su yapısı anlamlarını kapsar; başka bir yapıya özgü deyimsel anlam eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınır, kıyı ve uç anlamları işaret edilen çizgiye, su yapısı adayları ise yapının kenarına odaklanır. En yakın karışıklık, dikili kenar taşları ile kenarın genel adı arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kenarı oluşturan dikili taşlara dayanır; komşu dal ise kenarın kendisini malzemesinden ve kurulma biçiminden bağımsız olarak belirtir.","focus_only":"Odak dal, kuyu ve havuz çevresindeki belirli taşları ayrıca bağımsız sınır ve topluluk işaretlerini kapsar.","gloss":"kuyu veya havuz kenarı","neighbor_only":"Komşu dal, taş olma veya dikilme koşulu aramadan kuyu ve havuzun yanlarını genel olarak adlandırır.","neighbor_ref":"root_001370/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kuyu ve havuz ağzının çevresindeki kenar yapısını gösterebilir."}],"source_phrase_ar":"النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)","source_summary":"Ortak anlam, bir yeri belli eden veya bir su yapısının kenarını oluşturan dikili taştır. Kullanım, topluluk işaretinden bölge sınırına, kuyu ve havuz çevresindeki taşlara ve bu taşlarla yapılmış havuz adına uzanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامات المنصوبة للقوم أو حدود الحرم، ونصائب الحوض وحجارته المنصوبة على شفيره، والحوض المبني من الحجارة","what_is_not_ar":"لا يدخل الحجر المعبود أو المذبوح عليه، ولا نصيب الحظ"},"support_links":[]},{"boundary":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B004","candidate_links":[{"candidate_id":"cand_1cf3500c040656af62e5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"yorgunluk ve yıpratıcı sıkıntı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel bitkinliği ve hastalık, kaygı ya da belanın insan üzerinde bıraktığı yorucu etkiyi kapsar.","boundary_detail":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_image_ar":"تعب وعناء وبلاء ينهك الإنسان","concept_gloss":"yorgunluk ve yıpratıcı sıkıntı","contextual_glosses":[{"applicability":"İnsan bedeninin emek, yürüyüş veya hastalık yüzünden gücünü yitirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel gücün azalmasıyla ortaya çıkan yoğun yorgunluğu korur."},"facet_ids":["F001"],"text":"bitkinlik","usage_role":"contextual"},{"applicability":"Bir olayın, kaygının veya hastalığın kişide yorgunluk ve tedirginlik oluşturduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış etkenin kişide yorgunluk ve huzursuzluk oluşturmasını korur."},"facet_ids":["F003"],"text":"yorup huzursuz etmek","usage_role":"contextual"}],"definition":"Emek, hastalık, kaygı, üzüntü veya başka bir sıkıntının insanı yıpratmasıyla oluşan yorgunluk ve bitkinliktir. Aynı anlam alanı, bir etkenin kişiyi yorup huzursuz etmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."},{"facet_id":"F002","role":"extension","statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."},{"facet_id":"F003","role":"associated_use","statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}],"identity_rationale":"Dal, bedensel bitkinlik ve yorulmayı, insanı yıpratan emek, hastalık, kaygı, üzüntü ve belayı ortak bir etkilenme ekseninde doğru toplar. Bir şeyin kişiyi yormasını bildiren ettirgen kullanım da aynı etkinin katılımcı yönünü değiştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yorgunluk, bitkinlik, zahmet ve sıkıntı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hastalığın verdiği bitkinlik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"beni yordu ve huzursuz etti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yorucu veya yorgunluk içindeki"}],"lexicalization_note":"Tanım yalın yorgunluk anlamını korur; hastalık, kaygı ve bir şeyin kişiyi yorması gibi yapıya bağlı kullanımları ayrı yüzler olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bazıları yalnızca bedensel bitkinliği, bazıları zorluğu, bazıları da başkasını yorma eylemini öne çıkarır. En geniş gerçek örtüşme yorgunluk ve güçsüzlük dalındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal etkileyen hastalık ve ruhsal sıkıntıya kadar uzanır; komşu dal ise güçsüzlük ile süregelen emek ve meşakkat boyutunu daha belirgin taşır.","focus_only":"Odak dal, yorgunluğun yanında hastalık, kaygı, üzüntü ve belanın doğurduğu yıpratıcı etkiyi özellikle kapsar.","gloss":"yorgunluk ve güçsüzlük","neighbor_only":"Komşu dal, yorgunlukla birlikte güçsüzlük durumunu ve uzun uğraşın getirdiği genel meşakkati daha açık biçimde kapsar.","neighbor_ref":"root_001360/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yorgunluk, bitkinlik ve bir başkasını yorma anlamlarında geniş ölçüde örtüşür."}],"source_phrase_ar":"النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)","source_summary":"Ortak çekirdek yorgunluk, bitkinlik ve zahmettir. Anlam bedensel emekten hastalık ve ruhsal sıkıntının etkisine uzanır; geçişli kullanımda ise bu durumu doğuran olay veya hastalık özne olur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب بمعنى الإعياء والتعب والعناء والكد، وما ينشأ من مرض أو هم أو حزن أو بلاء، وأنصبني الشيء إذا أتعبني","what_is_not_ar":"لا يدخل القيام المنتصب الحسي إلا من جهة تفسير التعب بالملازمة حتى الإعياء"},"support_links":["sup_9faef572502a2fdd2210"]},{"boundary":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_kind":"bare","branch_ref":"root_001507/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"belirlenmiş pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünden kişiye ayrılmış veya ona düşmüş belirli bölümü en kısa biçimde karşılar.","boundary_detail":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_image_ar":"حظ معين مرفوع لصاحبه","concept_gloss":"belirlenmiş pay","contextual_glosses":[{"applicability":"Bağlam, bir bütünden kime ne kadar düştüğünü zaten belirgin kılıyorsa doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir bütünden kişiye düşen veya ayrılan bölüm anlamını korur."},"facet_ids":["F001"],"text":"pay","usage_role":"general"}],"definition":"Bir şeyden bir kişi için ayrılan, ona düşen veya onun adına belirlenen paydır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}],"identity_rationale":"Dal, bir bütünden bir kişiye düşen veya onun için belirlenen pay anlamını doğru verir. Payın belirlenmiş olması çekirdektir; dikili taş, taş havuz, köken ya da ölçü eşiği anlamları aynı ses biçimini paylaşsa da bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"pay veya bir şeyden ayrılan belirli bölüm"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"pay"}],"lexicalization_note":"Tanım yalın pay anlamını verir ve belirli hukuk, miras, ceza ya da ölçü kalıplarını genel anlama eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hak, borç, ceza payı ve hesap terimleri daha dar bağlamlara bağlıdır. En yakın sınır, belirlenmiş pay ile paylaştırma işlemini de kapsayan komşu anlam arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bölüştürmenin sonucundaki paydır; komşu dal hem bu sonucu hem de paylara ayırma işlemini içerir.","focus_only":"Odak dal, yalnızca kişiye düşen veya onun için belirlenen payı adlandırır.","gloss":"pay ve paylaştırma","neighbor_only":"Komşu dal, payın yanı sıra şeyi kişiler arasında bölme, denkleştirme ve paylaştırma işlemini de kapsar.","neighbor_ref":"root_001224/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir bütünden kişinin aldığı belirli bölümü pay olarak adlandırır."}],"source_phrase_ar":"النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)","source_summary":"Ortak anlatım, bir şeyden kişiye düşen belirli payı gösterir. Çoğul biçimler bu payların birden çok kişiye veya bölüme ait olabileceğini belirtir, fakat çekirdeği değiştirmez.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصيب بمعنى الحظ أو القسم المعين من الشيء، وما سمي منصوبا أو مرفوعا لصاحبه","what_is_not_ar":"لا يدخل الحجارة أو الحوض المسمى نصيبا، ولا النصاب بمعنى الأصل أو القدر"},"support_links":[]},{"boundary":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B006","candidate_links":[{"candidate_id":"cand_fd2c0d0c34b75b9243ff","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"temel veya sabit başvuru noktası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bıçağın elde tutulan sapı veya arka bölümü."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın söz kalıplarına göre köken, dayanak, dönüş noktası veya belirlenmiş eşik olarak gerçekleşen ortak çekirdeğini verir.","boundary_detail":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_image_ar":"نصاب الشيء: أصله ومقداره الثابت","concept_gloss":"temel veya sabit başvuru noktası","contextual_glosses":[{"applicability":"Bıçağın elde tutulan arka bölümü veya ona sonradan takılan sap anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bıçağın elde tutulan sap veya arka bölümünü eksiksiz karşılar."},"facet_ids":["F002"],"text":"bıçak sapı","usage_role":"contextual"},{"applicability":"Mal miktarının belirli bir mali yükümlülüğü doğurduğu alt sınırdan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sabit mal miktarının yükümlülüğü başlatan alt eşik oluşunu korur."},"facet_ids":["F003"],"text":"yükümlülük eşiği","usage_role":"explanatory"},{"applicability":"Kişinin geldiği aile çizgisi, kökeni ve buna bağlı saygınlığı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ailesel kökenini ve geldiği soy çizgisini korur."},"facet_ids":["F004"],"text":"soy kökeni","usage_role":"contextual"},{"applicability":"Güneşin ufukta kaybolduğu yön veya yer bir dönüş noktası gibi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin gün sonunda ufukta kaybolduğu yeri tam olarak korur."},"facet_ids":["F005"],"text":"güneşin battığı yer","usage_role":"contextual"}],"definition":"Bir şeyin dayandığı temel, döndüğü başvuru noktası veya sabitlenmiş ölçüsüdür. Bu çekirdek, yalnızca belirli kullanımlarda bıçağın sapını, mali yükümlülük doğuran alt eşiği, kişinin köken ve soyunu ya da güneşin batış yerini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."},{"facet_id":"F002","role":"specialization","statement":"Bıçağın elde tutulan sapı veya arka bölümü."},{"facet_id":"F003","role":"specialization","statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."},{"facet_id":"F004","role":"specialization","statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."},{"facet_id":"F005","role":"specialization","statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}],"identity_rationale":"Dal, temel, dönüş noktası ve sabit ölçü düşüncesini taşıyan kullanımları doğru toplar; ancak bunlar tek bir yalın ve her bağlama uygulanabilir anlam değildir. Bıçak sapı, mali yükümlülük eşiği, soy kökeni ve güneşin batış yeri yalnızca kendi söz kalıpları içinde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin temeli ve dönülen başvuru noktası"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bıçağın sapı veya arka bölümü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"mal için mali yükümlülük doğuran alt miktar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"köken, soy ve aileden gelen saygınlık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güneşin battığı ve döndüğü yer"}],"lexicalization_note":"Tanım ortak temel ve sabit başvuru noktasını verir; bıçak, mal, soy ve güneşle kurulan anlamları ayrı ve kalıba bağlı uzmanlaşmalar olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hesap, ağırlık ve ölçme dalları yalnızca sabit miktar yüzünü, köken dalları ise yalnızca temel yüzünü paylaşır. Bu nedenle yayımlanan ilişki eş anlamlılık değil aynı alan karşılaştırmasıdır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak köken alanına rağmen odak dal farklı nesnelerde sabit başvuru ve eşik anlamları taşıyan bir kullanım ailesidir; komşu dalın nesne kapsamı ayrıdır.","focus_only":"Odak dal, kökenin yanı sıra bıçak sapı, mali eşik ve güneşin batış yeri gibi kalıplaşmış başvuru noktalarını kapsar.","gloss":"köken ve çıkış yeri","neighbor_only":"Komşu dal, kişinin soy kökenini ve hörgücün kök bölümünü kendi sözlüksel alanında adlandırır.","neighbor_ref":"root_000340/B005","relation_type":"same_field","shared_zone":"Her iki dal da bir varlığın geldiği temel veya köken noktasını gösterebilir."}],"source_phrase_ar":"نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)","source_summary":"Ortak malzeme temel ve geri dönülen başvuru noktası çevresinde toplanır, fakat kullanımlar güçlü biçimde sözlüksel sınırlıdır. Bıçak sapı, mali eşik, soy kökeni ve güneşin batış yeri aynı genel sözcük ailesinin ayrı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصاب الشيء أي أصله ومرجعه، ونصاب السكين ومقبضها أو عجزها، ونصاب المال الذي تجب فيه الزكاة، ونصاب الشمس مغيبها، والمنصب بمعنى الأصل والحسب","what_is_not_ar":"لا يدخل النصيب بمعنى الحظ، ولا النصب بمعنى التعب أو الحجر المعبود"},"support_links":["sup_eae703f666f77d883fbd"]},{"boundary":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001507/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"dil bilgisinde yükleme konumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca çekim ve değişmez biçim çözümlemesindeki özel dil bilgisi kategorisini adlandırır.","boundary_detail":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_image_ar":"نصب الكلمة في الإعراب","concept_gloss":"dil bilgisinde yükleme konumu","contextual_glosses":[{"applicability":"Bir sözcüğün cümle içindeki çekim konumu özel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün yükleme konumuna yerleştirilmiş olmasını tam olarak korur."},"facet_ids":["F001"],"text":"yükleme konumundaki sözcük","usage_role":"explanatory"}],"definition":"Çekimli dil bilgisinde üst konumun karşıtı olan yükleme konumu; değişmez yapılarda ise açık ünlülü biçime denk sayılan dil bilgisel kategoridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."},{"facet_id":"F002","role":"source_variant","statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}],"identity_rationale":"Dal, çekimli dil bilgisinde üst konumun karşısında yer alan yükleme konumunu ve değişmez biçimlerde açık ünlülü yapıyla kurulan benzerliği doğru verir. Ağız içindeki ses yükselişine ilişkin açıklama kategori tanımının kendisi değil, sesletim temelli bir gerekçelendirmedir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çekimde üst konumun karşıtı olan yükleme konumu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yükleme konumuna getirilmiş sözcük"}],"lexicalization_note":"Tanım açıkça dil bilgisi yapısına bağlıdır ve bu terimsel kullanımdan yalın kök için genel bir anlam çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; diğerleri dil bilgisinin farklı bölümlerini veya genel anlatımı paylaşır, fakat aynı çekim ekseninde yer almaz. Doğrudan karşıtlık yalnızca üst konum dalıyla kuruludur.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bunlar aynı eksenin karşıt kutuplarıdır: odak dal yükleme yönündeki konumu, komşu dal ise üst konumu belirtir.","focus_only":"Odak dal, çekimde yükleme yönündeki alt konumu ve değişmez biçimde açık ünlülü yapıyı gösterir.","gloss":"karşıt çekim konumları","neighbor_only":"Komşu dal, aynı çekim düzenindeki karşıt üst konumu ve değişmez biçimde yuvarlak ünlülü yapıyı gösterir.","neighbor_ref":"root_000582/B012","relation_type":"polarity_pair","shared_zone":"İki dal aynı dil bilgisi sisteminde sözcüğün biçimsel çekim konumunu belirler."}],"source_phrase_ar":"في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)","source_summary":"Ortak çekirdek belirli bir dil bilgisi konumudur ve karşıt üst konumla tanımlanır. Bazı açıklamalar bunu değişmez yapılardaki açık ünlülü biçime veya sözcüğün ağızda daha yukarıdan seslendirilmesine benzetir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب النحوي ضد الرفع أو كالفتح في البناء، والكلمة المنصوبة والحرف المنصوب","what_is_not_ar":"لا يدخل رفع الشيء حسيا ولا رفع الصوت في الغناء إلا من جهة التشبيه الذي ذكرته المصادر"},"support_links":[]},{"boundary":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_kind":"non_bare","branch_ref":"root_001507/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"birine savaş veya düşmanlıkla karşı çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir kişiye açıkça hasım olma, savaş açma veya düşmanlık yöneltme bağlamlarında kullanılır.","boundary_detail":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_image_ar":"مواجهة العداوة والحرب","concept_gloss":"birine savaş veya düşmanlıkla karşı çıkma","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişiye açıkça düşmanlık besleyip bunu davranışa dönüştürdüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşmanlığın belirli bir kişiye yönelmesini ve açık hâle gelmesini korur."},"facet_ids":["F001"],"text":"ona düşman kesilmek","usage_role":"contextual"},{"applicability":"Hasmane yönelişin doğrudan savaş başlatma veya savaşla karşı karşıya gelme biçiminde gerçekleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaşın belirli bir kişiye yöneltilmesini açık biçimde korur."},"facet_ids":["F002"],"text":"ona savaş açmak","usage_role":"contextual"}],"definition":"Bir kişiye savaş, kötülük veya düşmanlıkla yönelmek; onun karşısına açıkça hasım olarak çıkmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."},{"facet_id":"F002","role":"specialization","statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}],"identity_rationale":"Dal, belirli bir kişiye savaş, kötülük veya düşmanlıkla açıkça yönelme anlamını doğru verir. Anlam sıradan bir nesneyi dikmekten değil, karşı tarafa hasmane bir tutum veya savaş durumu kurmaktan oluşur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"birine savaş veya düşmanlıkla karşı çıkmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"ona düşman olmak veya düşmanlık yöneltmek"}],"lexicalization_note":"Tanım yalnızca kişiyle kurulan düşmanlık ve savaş yapılarına bağlıdır; bu kullanımlardan yalın ve genel bir kök anlamı üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; savaş, savunma, mücadele ve uzun süreli husumet dalları aynı senaryonun farklı bölümleridir. En yakın sınır, genel hasmane yöneliş ile düşmanlığı ilk kez açık etme arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hasmane karşılaşmanın genel durumunu verir; komşu dal ise düşmanlığın ilk açık ilanı veya başlangıç anıyla sınırlıdır.","focus_only":"Odak dal, bir kişiye savaş veya düşmanlıkla yönelmeyi, bunun başlamış ya da sürmekte olmasını kapsar.","gloss":"açık düşmanlık başlatma","neighbor_only":"Komşu dal, düşmanlığın ilk kez açıkça ortaya konmasını ve karşı tarafa bildirilmesini özellikle şart koşar.","neighbor_ref":"root_001302/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da düşmanlığın belirli bir kişiye açıkça yöneltilmesini anlatır."}],"source_phrase_ar":"ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)","source_summary":"Ortak anlatım, savaşın veya düşmanlığın belirli bir kişiye yöneltilmesini ve kişinin karşısına hasım olarak çıkılmasını gösterir. Fiil, hem karşılıklı savaşmayı hem de birine düşmanlık kurmayı anlatabilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ناصب فلانا الشر أو الحرب أو العداوة، ونصب له أو نصب لهم حربا، أي واجهه وعداه","what_is_not_ar":"لا يدخل مجرد نصب الشيء الحسي إلا إذا كان المنصوب هو الحرب أو العداوة"},"support_links":[]},{"boundary":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"özel bir şarkı veya ezgi türü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kendine özgü bir şarkı veya ezgi türü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olarak kanıtlanan özel şarkı veya ezgi türünü belirtir; bazı kullanımlarda yolculukta söylenen, hayvan sürme çağrısına benzer görece yumuşak biçimi kapsar.","boundary_detail":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_image_ar":"غناء يرفع به الصوت","concept_gloss":"özel bir şarkı veya ezgi türü","contextual_glosses":[{"applicability":"Bağlam ezginin özel türünü ve yolculuk sırasında söylendiğini zaten gösteriyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel şarkı türünün yolculuk bağlamındaki kullanımını korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisi","usage_role":"contextual"},{"applicability":"Bir yolcunun bu özel ezgi türünü seslendirmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolcunun belirli ezgi türünü söylemesi eylemini tam olarak korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisini söylemek","usage_role":"contextual"}],"definition":"Belirli bir şarkı veya ezgi türüdür. Bazı kaynaklarda yolcuların söylediği, hayvan sürerken kullanılan çağrılı ezgiye benzeyen ve ondan daha yumuşak olabilen bir tür olarak açıklanır. Adının sesi yükseltmeyle ilişkisi kesin anlam değil, olası bir türetme açıklamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kendine özgü bir şarkı veya ezgi türü."},{"facet_id":"F002","role":"specialization","statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."},{"facet_id":"F003","role":"source_variant","statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}],"identity_rationale":"Kaynak ifadesinin çekirdeği sesi yükseltmenin kendisi değil, belirli bir şarkı ve ezgi türüdür. Yolcuların söylediği ve hayvan sürme ezgisine benzediği, fakat daha yumuşak olabildiği belirtilir; ses yükseltme bağlantısı yalnızca olası bir adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yolcuların söylediği özel ezgi türü"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yolcu ezgisini söyledi"}],"lexicalization_note":"Tanım ezgi türünün yalın adını, onun yolcu şarkısı kalıbını ve bu ezgiyi söyleme fiilini ayırır; yüksek ses varsayımını çekirdeğe dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çalgı, ses yineleme, yüksek ses ve biçimlenmiş ezgi adayları yalnızca müzik senaryosunu paylaşır. En yakın sınır özel yolcu ezgisi ile genel şarkı ve ezgili ses alanıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yolcu ezgisi türüdür; komşu dal ise şarkı ve ezgili ses alanının genel adıdır.","focus_only":"Odak dal, yolcularla ve hayvan sürme çağrılı ezgisine benzer yumuşak söyleyişle sınırlı özel bir türdür.","gloss":"şarkı ve ezgili ses","neighbor_only":"Komşu dal, şarkıyı, güzel sesi, ezgili dinletiyi ve okumanın duygulu ya da ince söylenişini daha genel kapsar.","neighbor_ref":"root_001110/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da insan sesiyle ezgili ve dinlenebilir bir söyleyişi anlatır."}],"source_phrase_ar":"النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)","source_summary":"Ortak çekirdek belirli bir ezgi türüdür. Bu tür yolculuk ve hayvan sürme bağlamıyla ilişkilendirilir, benzer çağrılı ezgiden daha yumuşak sayılabilir ve adının sesi yükseltmekten geldiği yalnızca olasılık olarak açıklanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب ضربا من الغناء أو الألحان، وغناء الركبان أو الحداء المشبه بالغناء، والفعل نصب الراكب إذا غناه","what_is_not_ar":"لا يدخل النصب النحوي ولا رفع الشيء الحسي إلا من جهة رفع الصوت"},"support_links":[]},{"boundary":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","surface_ar":"ٱنصَبْ"}],"gloss":"yolculuğu yumuşak sürdürme veya artırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel söz yapısında hem gün boyu yumuşak ilerleme hem de yol alışını yükseltme çeşitlemesini kapsar.","boundary_detail":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_image_ar":"سير اليوم سيرا لينا","concept_gloss":"yolculuğu yumuşak sürdürme veya artırma","contextual_glosses":[{"applicability":"Topluluğun gündüz boyunca hafif ve yumuşak bir yürüyüşle yol aldığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gün boyu süren yumuşak ilerleyiş çeşitlemesini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"gün boyu yumuşak ilerlemek","usage_role":"contextual"},{"applicability":"Topluluğun ilerleyişini yükselttiği veya yolculuk çabasını artırdığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alışını yükseltme ve ilerleyişi artırma çeşitlemesini korur."},"facet_ids":["F001","F003"],"text":"yol alışını artırmak","usage_role":"contextual"}],"definition":"Bir topluluğun yolculuğu sürdürmesiyle ilgili özel kullanımdır. Bağlama göre gün boyunca yumuşak biçimde ilerlemeyi veya yol alışını yükseltip artırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."},{"facet_id":"F002","role":"source_variant","statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."},{"facet_id":"F003","role":"source_variant","statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}],"identity_rationale":"Dalın yolculukla ilgili kimliği doğrudur, ancak kaynak ifadesi tek biçimli bir hız niteliği vermez. Bir anlatım yol alışını yükseltip artırmayı, diğer anlatımlar ise gün boyunca yumuşak biçimde ilerlemeyi bildirir; iki çeşitleme aynı özel söz yapısı içinde ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"gün boyunca yumuşak biçimde ilerlediler"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"yol alışlarını yükseltip artırdılar"}],"lexicalization_note":"Tanım yalnızca topluluğun yol alması ve yolculuğu sürdürmesi yapılarında geçerlidir; gün boyu yumuşak ilerleme ile yol alışını artırma çeşitlemelerini birbirine karıştırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kesintisiz, geceleyin, hızlı veya uzaklara yapılan yolculuklar farklı koşullar taşır. En yakın örtüşme yumuşak ilerleyiştedir, ancak odak dalın gün boyu sürme ve artırma çeşitlemeleri daha geniştir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli topluluk ve yolculuk yapısında gün boyu sürme ya da artırma seçeneklerini taşır; komşu dal yalnızca yumuşak hız niteliğine odaklanır.","focus_only":"Odak dal, topluluğun gün boyunca yol almasını ve ayrıca yol alışını artırma çeşitlemesini içerir.","gloss":"yumuşak yol alma","neighbor_only":"Komşu dal, gün boyu sürme veya ilerleyişi artırma koşulu olmadan yalnızca yumuşak yürüyüşü belirtir.","neighbor_ref":"root_000664/B013","relation_type":"near_synonym","shared_zone":"Her iki dal da yolculuğun yumuşak ve hafif bir ilerleyişle yapılmasını anlatabilir."}],"source_phrase_ar":"نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)","source_summary":"Ortak bağlam bir topluluğun yol almasıdır, fakat nitelik anlatımı ikiye ayrılır: gün boyunca yumuşak ilerleme ve yol alışını yükseltip artırma. Bu karşıt görünümler tek bir hız özelliğine indirgenmeden korunmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه نصب القوم أو نصب السير: ساروا يومهم أو رفعوا السير، وهو سير لين في بعض المصادر","what_is_not_ar":"لا يدخل التعب من السفر إلا إذا دل السياق على الإعياء لا على نوع السير"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["94:7:1"],"branch_refs":[],"candidate_id":"cand_549fa7b86fb56ad917a6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:1:consequential-pivot-from-ease","source_type":"word_analysis","support_ids":["sup_2f40c07009921b5b61f0","sup_a8bc742e789a647a5c20"],"title":"consequence from prior assurance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:1","qac_refs":["94:7:1:1"],"status":"accepted"}},{"anchor_refs":["94:7:1"],"branch_refs":[],"candidate_id":"cand_242c98cd0650adf99fe9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:1:first-fa-hosts-condition","source_type":"word_analysis","support_ids":["sup_2f40c07009921b5b61f0","sup_5bb2db14715e21078277"],"title":"outer connector, not response marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:1","qac_refs":["94:7:1:1"],"status":"accepted"}},{"anchor_refs":["94:7:1"],"branch_refs":[],"candidate_id":"cand_aa6ba8c29041fedbc42f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:1:open-toward-next-command","source_type":"word_analysis","support_ids":["sup_2f40c07009921b5b61f0","sup_6fdd95371fd51a46f924"],"title":"launch of a command pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:1","qac_refs":["94:7:1:1"],"status":"accepted"}},{"anchor_refs":["94:7:1"],"branch_refs":[],"candidate_id":"cand_b35008acd3d65fec95a6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:1:paired-fa-cadence","source_type":"word_analysis","support_ids":["sup_2f40c07009921b5b61f0","sup_bd308990153fe5ac3205"],"title":"paired clipped sequence markers","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:1","qac_refs":["94:7:1:1"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_c3542de49e1dc45c6797","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:2:assured-completion","source_type":"word_analysis","support_ids":["sup_6ae7902b2d165be84c35","sup_756d25e3a3797c6a3f42"],"title":"expected completion, not doubtful if","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:2","qac_refs":["94:7:1:2"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_dcc2b96b26c64f494b25","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:2:audible-conditional-onset","source_type":"word_analysis","support_ids":["sup_6814f5b22c6558c3c82c","sup_6ae7902b2d165be84c35"],"title":"fused and caught onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:2","qac_refs":["94:7:1:2"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_c54e409b78a996995ddc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:2:axiom-to-action-scene","source_type":"word_analysis","support_ids":["sup_00e82e41bc88c892c84c","sup_6ae7902b2d165be84c35"],"title":"assurance becomes operational","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:2","qac_refs":["94:7:1:2"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_0fad8a95169bf9b0cc3f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:2:extended-command-scope","source_type":"word_analysis","support_ids":["sup_6ae7902b2d165be84c35","sup_aa55cbc778ac40c18a62"],"title":"possible wider response through 94:8","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:2","qac_refs":["94:7:1:2"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_5fa347f3db44a32e85cb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:2:when-then-command-frame","source_type":"word_analysis","support_ids":["sup_6ae7902b2d165be84c35","sup_dedc7e92ad8a54d10bfd"],"title":"temporal condition and response","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:2","qac_refs":["94:7:1:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_aa87bdbdebacdde12be4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:completion-as-freeing-emptying","source_type":"word_analysis","support_ids":["sup_227a323ef0d967509ae0","sup_bb843f82a77a35198d4f"],"title":"finished and freed, with emptied pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_af2cba22208b308c4c2e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:deliberate-redirection-after-release","source_type":"word_analysis","support_ids":["sup_2675425f9effe0e0d1a0","sup_bb843f82a77a35198d4f"],"title":"completion as pivot into intent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_a49ccd7ffa07a6bdb51b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:direct-address-return","source_type":"word_analysis","support_ids":["sup_3536eb23db2cce1f5975","sup_bb843f82a77a35198d4f"],"title":"principle returns to you","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_a03977c30c8d410bd215","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:direct-perfect-trigger","source_type":"word_analysis","support_ids":["sup_bb843f82a77a35198d4f","sup_c251734db35ea5701718"],"title":"second-person perfect trigger","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_c831f5bfa2220bc41e96","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:pouring-echo","source_type":"word_analysis","support_ids":["sup_bb843f82a77a35198d4f","sup_f9c0fd7825baaa291d7f"],"title":"emptied-poured resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_19424ea24445946218b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:rare-conditional-placement","source_type":"word_analysis","support_ids":["sup_842c3f44230edebfb4fc","sup_bb843f82a77a35198d4f"],"title":"marked rare transition word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_d01082a78f260dad70b0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:self-affected-addressee","source_type":"word_analysis","support_ids":["sup_bb843f82a77a35198d4f","sup_c097ff10951652e8f5f1"],"title":"agent who is also freed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_aa2bc30a11c8b6e94b43","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:sound-of-release","source_type":"word_analysis","support_ids":["sup_8e28eb2ecfab6a61e3d3","sup_bb843f82a77a35198d4f"],"title":"open syllables then guttural close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_b3bc88d2853868876594","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:3:unnamed-completion-domain","source_type":"word_analysis","support_ids":["sup_bb843f82a77a35198d4f","sup_c0e6f4c96fc47a87f6d8"],"title":"open completed domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:3","qac_refs":["94:7:2:1","94:7:2:2"],"status":"accepted"}},{"anchor_refs":["94:7:4"],"branch_refs":[],"candidate_id":"cand_ee70b490707c5b2fb026","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:4:apodosis-response-marker","source_type":"word_analysis","support_ids":["sup_42e54cf0e30eebfcda7a","sup_be1916f05d2a6e5e679f"],"title":"condition answered by command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:4","qac_refs":["94:7:3:1"],"status":"accepted"}},{"anchor_refs":["94:7:4"],"branch_refs":[],"candidate_id":"cand_3dd86bb3c8799f0a9abc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:4:distinct-from-opening-fa","source_type":"word_analysis","support_ids":["sup_42e54cf0e30eebfcda7a","sup_b570f7f56e40c56c4a1f"],"title":"inner hinge, not outer bridge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:4","qac_refs":["94:7:3:1"],"status":"accepted"}},{"anchor_refs":["94:7:4"],"branch_refs":[],"candidate_id":"cand_8adc4a958daaf5844194","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:4:next-fa-command-continuation","source_type":"word_analysis","support_ids":["sup_16ea859317f02a3af74a","sup_42e54cf0e30eebfcda7a"],"title":"model for the next command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:4","qac_refs":["94:7:3:1"],"status":"accepted"}},{"anchor_refs":["94:7:4"],"branch_refs":[],"candidate_id":"cand_06e42f38a3bf21110efa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:7:4:particle-command-fusion","source_type":"word_analysis","support_ids":["sup_42e54cf0e30eebfcda7a","sup_63a10f527a8348276996"],"title":"bound response-unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:4","qac_refs":["94:7:3:1"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_1de874b5dfa93b335147","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:bound-wasl-onset","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_bc8217f1b8ac71bcfdf6"],"title":"response flows into command onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_8d4d413dd224caab6a39","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:clipped-imperative-command","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_3839db1c13e23bb9f835"],"title":"abrupt second-person command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_07be8800db55cf8eacf6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:cultic-object-contrast","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_cdec11ee31269c06bb32"],"title":"cultic stones contrasted, not commanded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_9a3caf7fffc4a2f07af0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:ease-to-action-to-orientation","source_type":"word_analysis","support_ids":["sup_1d026497647b39517e86","sup_30f6bc3683946a28a7db"],"title":"renewed action before orientation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_4d5fa27c7a2b56b33821","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:effortful-sound-closure","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_8029001662f07d75c408"],"title":"heavy percussive ending","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_c0c9267ecc9cc5f70a46","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:form-i-self-action","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_32126c01178430bf5c5d"],"title":"simple Form I self-action","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_ba5326f893fc4b6b95d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:intransitive-open-target","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_66a38fd43a1cf222174d"],"title":"self-exertion before named object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_904eef5e69f7dfbcadf8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:qiraat-pressure","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_c410426766efb96f4e55"],"title":"variant readings expose pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_10b61a013b93f1f7235b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:rare-verbal-imperative","source_type":"word_analysis","support_ids":["sup_1570d0049956e4a40867","sup_30f6bc3683946a28a7db"],"title":"rare command against nominal field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_1e9575b827327e979b40","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:upright-toil-image","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_7a32e58a71504bf2e671"],"title":"toil as upright re-engagement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:5"],"branch_refs":[],"candidate_id":"cand_d709e42d502a71e991cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:5:wider-root-field-resonance","source_type":"word_analysis","support_ids":["sup_30f6bc3683946a28a7db","sup_8a185875a3f7b7c1c31a"],"title":"erected objects and fixed positions as resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:7:5","qac_refs":["94:7:3:2"],"status":"accepted"}},{"anchor_refs":["94:7:2"],"branch_refs":[],"candidate_id":"cand_2b6278e9bcbc63299476","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001147"],"scope":"focus_ayah","source_local_id":"94:7:2:1","source_type":"qac_morpheme","support_ids":["sup_f079c82446d1daac4d82"],"title":"QAC root occurrence: ف ر غ","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:7:3"],"branch_refs":[],"candidate_id":"cand_e5903ddf393961faced0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"94:7:3:2","source_type":"qac_morpheme","support_ids":["sup_54de5fb334b1bffff923"],"title":"QAC root occurrence: ن ص ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:7","branch_refs":["root_001147/B001","root_001507/B004"],"candidate_id":"cand_1cf3500c040656af62e5","commentary_obligation":"review","hft_ref":"hft_69e68f8f9e232333ebc1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_release_to_chosen_strain","source_type":"hft","support_ids":["sup_9faef572502a2fdd2210"],"title":"baseline_release_to_chosen_strain","trust":"legacy_unbound"},{"anchor_refs":["94:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:7","branch_refs":["root_001147/B002","root_001507/B001"],"candidate_id":"cand_eefbe890023c35a8c3c6","commentary_obligation":"review","hft_ref":"hft_9a70b0a62ef2f63697a3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_empty_then_erect","source_type":"hft","support_ids":["sup_e8415fc36a3b17a7ffa5"],"title":"baseline_empty_then_erect","trust":"legacy_unbound"},{"anchor_refs":["94:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:7","branch_refs":["root_001147/B006","root_001507/B001","root_001507/B006"],"candidate_id":"cand_fd2c0d0c34b75b9243ff","commentary_obligation":"review","hft_ref":"hft_638633a9719198936e85","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_exclusive_attention_fixed","source_type":"hft","support_ids":["sup_eae703f666f77d883fbd"],"title":"baseline_exclusive_attention_fixed","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"94:7:1:1","qac_word_ref":"94:7:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"94:7:1:2","qac_word_ref":"94:7:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","root_ar":"ف ر غ","surface_ar":"فَرَغْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:7:2:2","qac_word_ref":"94:7:2","root_ar":"","surface_ar":"تَ"},{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"94:7:3:1","qac_word_ref":"94:7:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","root_ar":"ن ص ب","surface_ar":"ٱنصَبْ"}],"word_analysis_qac_refs":[["94:7:1:1"],["94:7:1:2"],["94:7:2:1","94:7:2:2"],["94:7:3:1"],["94:7:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["94:7:1","94:7:2","94:7:3","94:7:4","94:7:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"94:7:1:1","qac_word_ref":"94:7:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"94:7:1:2","qac_word_ref":"94:7:1","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"فَرَغْ","morph_features":"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:2:1","qac_word_ref":"94:7:2","root_ar":"ف ر غ","surface_ar":"فَرَغْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:7:2:2","qac_word_ref":"94:7:2","root_ar":"","surface_ar":"تَ"},{"lemma_ar":"","morph_features":"PREFIX|f:RSLT+","morpheme_role":"PREFIX","pos":"RSLT","qac_ref":"94:7:3:1","qac_word_ref":"94:7:3","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:7:3:2","qac_word_ref":"94:7:3","root_ar":"ن ص ب","surface_ar":"ٱنصَبْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["94:7:1:1"],["94:7:1:2"],["94:7:2:1","94:7:2:2"],["94:7:3:1"],["94:7:3:2"]],"word_analysis_refs":["94:7:1","94:7:2","94:7:3","94:7:4","94:7:5"],"word_rows":[{"analysis_record_ref":"94:7:1","analytic_gloss_range_en":"opening consequential connector that carries the command sequence forward from 94:5-6 while hosting the following temporal condition","analytic_root_gloss_range_en":null,"qac_refs":["94:7:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"94:7:2","analytic_gloss_range_en":"temporal-conditional when/whenever particle that treats completion as an expected trigger for the following command","analytic_root_gloss_range_en":null,"qac_refs":["94:7:1:2"],"root":{},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"94:7:3","analytic_gloss_range_en":"to finish, become free, or be emptied in the temporal condition; locally a completed state of availability that triggers the command","analytic_root_gloss_range_en":"root range includes completion or freedom after occupation, emptying or pouring out, and deliberate turning; local Form I perfect selects completion/freeing while allowing limited emptying and redirection pressure","qac_refs":["94:7:2:1","94:7:2:2"],"root":{"arabic":"ف ر غ","transliteration":"f-r-gh"},"surface":{"arabic":"فَرَغْتَ","transliteration":"faraghta"}},{"analysis_record_ref":"94:7:4","analytic_gloss_range_en":"response fa that introduces the apodosis of the temporal condition and makes the imperative immediate","analytic_root_gloss_range_en":null,"qac_refs":["94:7:3:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"94:7:5","analytic_gloss_range_en":"Form I second-person singular imperative to exert oneself, toil, or stand into effort; locally intransitive and command-focused","analytic_root_gloss_range_en":"root range includes setting upright, cultic or boundary stones, weariness and toil, fixed portions or positions, hostility, raised chant, and travel; local imperative selects self-exertion with uprightness and fatigue pressure","qac_refs":["94:7:3:2"],"root":{"arabic":"ن ص ب","transliteration":"n-ṣ-b"},"surface":{"arabic":"ٱنصَبْ","transliteration":"inṣab"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["94:7"],"branch_refs":["root_001147/B001","root_001507/B004"],"candidate_id":"cand_1cf3500c040656af62e5","evidence_scope":"focus_ayah","hft_ref":"hft_69e68f8f9e232333ebc1","item_id":"baseline_release_to_chosen_strain","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_release_to_chosen_strain","support_id":"sup_9faef572502a2fdd2210"},{"anchor_refs":["94:7"],"branch_refs":["root_001147/B002","root_001507/B001"],"candidate_id":"cand_eefbe890023c35a8c3c6","evidence_scope":"focus_ayah","hft_ref":"hft_9a70b0a62ef2f63697a3","item_id":"baseline_empty_then_erect","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_empty_then_erect","support_id":"sup_e8415fc36a3b17a7ffa5"},{"anchor_refs":["94:7"],"branch_refs":["root_001147/B006","root_001507/B001","root_001507/B006"],"candidate_id":"cand_fd2c0d0c34b75b9243ff","evidence_scope":"focus_ayah","hft_ref":"hft_638633a9719198936e85","item_id":"baseline_exclusive_attention_fixed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_exclusive_attention_fixed","support_id":"sup_eae703f666f77d883fbd"}],"diagnostics":[],"lane_counts":{"global":9,"macro":9,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"94:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ز ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001643","furuq_root_norm":"و ز ر","furuq_source_root_norm":"و ز ر","is_dominant":true,"target_occurrences":24,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000654","furuq_root_norm":"ز و ر","furuq_source_root_norm":"ز و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"94:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"94:7","lane":"micro","linguistic_source_ref":"94:7","surface_ref":"94:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"94:7","target_tokens":[["O",["94:7:1"]],["hâlde",["94:7:1"]],["boş",["94:7:2"]],["kaldığında",["94:7:1","94:7:2"]],["çabala",["94:7:3"]]],"text":"O hâlde, boş kaldığında çabala."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s094-p01-001-008","label":"Whole surah","number":1,"refs":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2:axiom-to-action-scene","source_type":"word_analysis","support_id":"sup_00e82e41bc88c892c84c","text":"{\"blocking_evidence\":null,\"headline\":\"assurance becomes operational\",\"reader_payoff\":\"The reader notices the discourse change from a general truth about hardship and ease to a timed second-person scene of action.\",\"reason\":\"The particle introduces the temporal condition that converts the preceding assurance into the local command sequence.\",\"representative_source_ids\":[\"QT-0e98834c\",\"QB-391e32b9\",\"QB-908a8d6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:rare-verbal-imperative","source_type":"word_analysis","support_id":"sup_1570d0049956e4a40867","text":"{\"blocking_evidence\":null,\"headline\":\"rare command against nominal field\",\"reader_payoff\":\"The reader notices that a root often represented through states or objects becomes here a direct verbal act commanded from the addressee.\",\"reason\":\"The contextual profile marks the exact root-form occurrence as low-occurrence and imperative, supporting the salience of the verbal command.\",\"representative_source_ids\":[\"MG-5966938f\",\"QI-6576cee4\",\"QH-8d1f4a2e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:4:next-fa-command-continuation","source_type":"word_analysis","support_id":"sup_16ea859317f02a3af74a","text":"{\"blocking_evidence\":null,\"headline\":\"model for the next command\",\"reader_payoff\":\"The reader notices that this fa-marked imperative sets up a command rhythm that can continue into the next fa-marked imperative in 94:8.\",\"reason\":\"The local apodosis remains strongly licensed in 94:7, while the row's 94:8 continuation is a discourse rhythm observation rather than a competing parse.\",\"representative_source_ids\":[\"QB-8c68c394\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:ease-to-action-to-orientation","source_type":"word_analysis","support_id":"sup_1d026497647b39517e86","text":"{\"blocking_evidence\":null,\"headline\":\"renewed action before orientation\",\"reader_payoff\":\"The reader notices that ease does not end action; it enables renewed exertion, which 94:8 then directs toward the Lord.\",\"reason\":\"The immediate command is local to 94:7, and the movement toward 94:8 survives as discourse continuation after that command.\",\"representative_source_ids\":[\"QB-0115c43c\",\"QB-0aa36d44\",\"QB-124f219e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:completion-as-freeing-emptying","source_type":"word_analysis","support_id":"sup_227a323ef0d967509ae0","text":"{\"blocking_evidence\":null,\"headline\":\"finished and freed, with emptied pressure\",\"reader_payoff\":\"The reader notices that finishing is pictured as becoming free or emptied for the next act, not merely checking off a task.\",\"reason\":\"V4 accepts the branch of emptiness or freedom after occupation for {{ar:ف ر غ}} ({{tr:f-r-gh}}), while the local Form I perfect and conditional sequence select completion/freeing rather than activating every remote branch.\",\"representative_source_ids\":[\"QS-48099cde\",\"QS-fe864396\",\"MS-67996c05\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:deliberate-redirection-after-release","source_type":"word_analysis","support_id":"sup_2675425f9effe0e0d1a0","text":"{\"blocking_evidence\":null,\"headline\":\"completion as pivot into intent\",\"reader_payoff\":\"The reader notices that the release of completion points forward into intentional reorientation, especially as the next ayah directs desire toward the Lord in 94:8.\",\"reason\":\"V4 accepts a deliberate-turning branch for {{ar:ف ر غ}} ({{tr:f-r-gh}}), and the row's reference to 37:91 supports root-family contrast; locally this remains a directional pressure, not a replacement for the completion sense.\",\"representative_source_ids\":[\"QS-4e03fbb6\",\"MI-44555621\",\"QB-54a7c11e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:1","source_type":"word_analysis","support_id":"sup_2f40c07009921b5b61f0","text":"{\"gloss_range\":\"opening consequential connector that carries the command sequence forward from 94:5-6 while hosting the following temporal condition\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes 94:7 arrive as consequence, not as a detached new saying: the repeated assurance of 94:5-6 is taken up into an actionable sequence. It also differs from the later {{ar:فَ}} ({{tr:fa}}) at 94:7:4; this first particle carries the whole condition forward, while the second marks the response. The repeated onset frames the ayah as clipped movement: consequence, condition, then command, with the sequence opening further toward the paired imperative in 94:8.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5","source_type":"word_analysis","support_id":"sup_30f6bc3683946a28a7db","text":"{\"gloss_range\":\"Form I second-person singular imperative to exert oneself, toil, or stand into effort; locally intransitive and command-focused\",\"prose\":\"{{ar:ٱنصَبْ}} ({{tr:inṣab}}) is the ayah's clipped landing point: a second-person singular imperative, not a description of toil. With the preceding {{ar:فَ}} ({{tr:fa}}) carried straight into its waṣl onset, it lands as a fused response-command rather than an imperative after a pause. Its intransitive surface leaves the work-domain unnamed, so the command governs the addressee's re-entry into effort before it specifies any object. The root {{ar:ن ص ب}} ({{tr:n-ṣ-b}}) makes that effort bodily: toiling carries the image of standing upright or being set into a fixed posture, answering the emptied availability of {{ar:فَرَغْتَ}} ({{tr:faraghta}}) with vertical re-engagement. Wider root branches around erected stones, cultic objects, portions, and fixed positions remain as narrowed resonance rather than the local sense; references to prohibited cultic objects at 5:3, 5:90, and 70:43 sharpen the contrast without making an object of worship the command here. Variant readings and pause treatments make the pressure concrete: final-kasra treatment softens the clipped stop, a fa-nṣabba-type reading pulls toward pouring down or out, and a fa-nṣib-type reading makes an omitted object more salient; the local reading remains a Form I imperative of self-exertion. As a rare verbal command in a root often represented by nouns, its heavy consonants and short shape make the final demand feel abrupt, marked, and embodied, while 94:8 supplies the next direction for that exertion.\",\"root_display\":\"{{ar:ن ص ب}} ({{tr:n-ṣ-b}})\",\"root_gloss_range\":\"root range includes setting upright, cultic or boundary stones, weariness and toil, fixed portions or positions, hostility, raised chant, and travel; local imperative selects self-exertion with uprightness and fatigue pressure\",\"surface_display\":\"{{ar:ٱنصَبْ}} ({{tr:inṣab}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:form-i-self-action","source_type":"word_analysis","support_id":"sup_32126c01178430bf5c5d","text":"{\"blocking_evidence\":null,\"headline\":\"simple Form I self-action\",\"reader_payoff\":\"The reader notices that the command falls on the addressee's own action, not on making some external system or object stand.\",\"reason\":\"QAC gives the local form as Form I imperative with a second-person implicit subject; no derived causative or intensive form is present.\",\"representative_source_ids\":[\"QF-0ed79442\",\"QF-562269c8\",\"QS-9b59fd5c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:direct-address-return","source_type":"word_analysis","support_id":"sup_3536eb23db2cce1f5975","text":"{\"blocking_evidence\":null,\"headline\":\"principle returns to you\",\"reader_payoff\":\"The reader notices the shift from the general assurance of 94:5-6 back into direct second-person address at the exact point of completion.\",\"reason\":\"The verb's second-person agreement and implicit subject evidence make the address local and direct.\",\"representative_source_ids\":[\"QI-f4464952\",\"QB-06b8a480\",\"QB-7d0f0e0f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:clipped-imperative-command","source_type":"word_analysis","support_id":"sup_3839db1c13e23bb9f835","text":"{\"blocking_evidence\":null,\"headline\":\"abrupt second-person command\",\"reader_payoff\":\"The reader notices that the ayah lands in obligation: the final word turns the condition into a direct command to the addressee.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱنصَبْ}} ({{tr:inṣab}}) as a Form I second-person masculine singular imperative in the apodosis.\",\"representative_source_ids\":[\"QG-926ba593\",\"QG-9ea326bf\",\"QT-501ee405\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:4","source_type":"word_analysis","support_id":"sup_42e54cf0e30eebfcda7a","text":"{\"gloss_range\":\"response fa that introduces the apodosis of the temporal condition and makes the imperative immediate\",\"prose\":\"The second {{ar:فَ}} ({{tr:fa}}) is the internal response marker: it converts {{ar:إِذَا فَرَغْتَ}} ({{tr:idhā faraghta}}) into {{ar:ٱنصَبْ}} ({{tr:inṣab}}) with no narrated interval. This particle is therefore smaller than the opening connector but more immediate; it is the hinge where completed availability becomes command. Because it is bound onto the imperative onset, the response is heard as one tight unit, and it also prepares the fa-marked continuation of 94:8 without dissolving its own same-ayah function.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:7:3:2","source_type":"qac_morpheme","support_id":"sup_54de5fb334b1bffff923","text":"{\"lemma_ar\":\"نُصِبَتْ\",\"morph_features\":\"STEM|POS:V|IMPV|LEM:nuSibato|ROOT:nSb|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"94:7:3:2\",\"qac_word_ref\":\"94:7:3\",\"root_ar\":\"ن ص ب\",\"surface_ar\":\"ٱنصَبْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:1:first-fa-hosts-condition","source_type":"word_analysis","support_id":"sup_5bb2db14715e21078277","text":"{\"blocking_evidence\":null,\"headline\":\"outer connector, not response marker\",\"reader_payoff\":\"The reader notices that the two identical particles do different grammatical work: this one launches the condition, while the later one answers it.\",\"reason\":\"The local clause analysis assigns the condition to {{ar:إِذَا فَرَغْتَ}} ({{tr:idhā faraghta}}) and the response to {{ar:فَ ٱنصَبْ}} ({{tr:fa inṣab}}), so the first {{ar:فَ}} ({{tr:fa}}) is not the internal apodosis marker.\",\"representative_source_ids\":[\"QG-73bf20cf\",\"QF-acf26367\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:4:particle-command-fusion","source_type":"word_analysis","support_id":"sup_63a10f527a8348276996","text":"{\"blocking_evidence\":null,\"headline\":\"bound response-unit\",\"reader_payoff\":\"The reader notices that the response particle and imperative arrive as a single compressed onset, reinforcing the absence of delay.\",\"reason\":\"The particle is directly before the imperative, and the surface/recitation observation coheres with the syntactic response relation.\",\"representative_source_ids\":[\"QF-e2aaef0e\",\"QP-e4f3af2a\",\"QP-fa86f638\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:intransitive-open-target","source_type":"word_analysis","support_id":"sup_66a38fd43a1cf222174d","text":"{\"blocking_evidence\":null,\"headline\":\"self-exertion before named object\",\"reader_payoff\":\"The reader notices that the command leaves the target unnamed, making exertion broadly available while keeping the first demand on the addressee's own action.\",\"reason\":\"The local verb frame is intransitive with no object or prepositional complement, so an erected-object branch can hover only as resonance; it cannot require object recovery.\",\"representative_source_ids\":[\"QG-56f5f391\",\"QG-ff250e8d\",\"QT-b38ff3d6\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2:audible-conditional-onset","source_type":"word_analysis","support_id":"sup_6814f5b22c6558c3c82c","text":"{\"blocking_evidence\":null,\"headline\":\"fused and caught onset\",\"reader_payoff\":\"The reader notices that the condition begins with a tight auditory shift: the opening connector runs directly into the temporal particle, then catches at the new frame.\",\"reason\":\"The topic is phonetic and form-based; it is not contradicted by the grammatical evidence, which places {{ar:إِذَا}} ({{tr:idhā}}) at the start of the conditional frame.\",\"representative_source_ids\":[\"QF-9be2eaf3\",\"QP-73866f02\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2","source_type":"word_analysis","support_id":"sup_6ae7902b2d165be84c35","text":"{\"gloss_range\":\"temporal-conditional when/whenever particle that treats completion as an expected trigger for the following command\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) turns the ayah into a when-then protocol: when completion is reached, the command becomes due. Because it governs the perfect {{ar:فَرَغْتَ}} ({{tr:faraghta}}), the unfinished future is treated as a sure completion rather than a doubtful possibility. The particle also shifts the discourse from the standing assurance of 94:5-6 into a timed action-scene, and that frame can be heard as wide enough to prepare the next imperative in 94:8 while the same-ayah response remains {{ar:فَ ٱنصَبْ}} ({{tr:fa inṣab}}). At the sound level, the preceding connector runs directly into {{ar:إِذَا}} ({{tr:idhā}}), and the hamza catch marks the start of the condition as a tight auditory turn.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:1:open-toward-next-command","source_type":"word_analysis","support_id":"sup_6fdd95371fd51a46f924","text":"{\"blocking_evidence\":null,\"headline\":\"launch of a command pair\",\"reader_payoff\":\"The reader notices that 94:7 is not closed by exertion alone; its opening connector helps begin a paired command movement that continues in 94:8.\",\"reason\":\"The same-ayah grammar strongly licenses the immediate command in 94:7, while the row's proposed continuation to 94:8 can survive as a discourse-level observation rather than as local syntactic control.\",\"representative_source_ids\":[\"QB-6d68d26e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2:assured-completion","source_type":"word_analysis","support_id":"sup_756d25e3a3797c6a3f42","text":"{\"blocking_evidence\":null,\"headline\":\"expected completion, not doubtful if\",\"reader_payoff\":\"The reader notices that finishing is grammatically expected; the command waits for an assured moment, not a speculative condition.\",\"reason\":\"QAC's note on {{ar:إِذَا}} ({{tr:idhā}}) and the perfect verb in the condition supports the certainty reading, with a repeatable whenever force remaining possible.\",\"representative_source_ids\":[\"QG-f803c14d\",\"MG-33891f6c\",\"QS-59f30c37\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:upright-toil-image","source_type":"word_analysis","support_id":"sup_7a32e58a71504bf2e671","text":"{\"blocking_evidence\":null,\"headline\":\"toil as upright re-engagement\",\"reader_payoff\":\"The reader notices a bodily turn: emptied completion is answered by standing into strenuous effort, not by passive rest.\",\"reason\":\"V4 accepts both upright-setting and weariness/toil branches for {{ar:ن ص ب}} ({{tr:n-ṣ-b}}), and the local imperative selects exertion while preserving the upright bodily image.\",\"representative_source_ids\":[\"QS-3600e90c\",\"QS-c1fed42f\",\"MT-a2245c5c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:effortful-sound-closure","source_type":"word_analysis","support_id":"sup_8029001662f07d75c408","text":"{\"blocking_evidence\":null,\"headline\":\"heavy percussive ending\",\"reader_payoff\":\"The reader notices that the final command sounds effortful and abrupt, with a heavy consonantal close matching the labor it orders.\",\"reason\":\"The sound observation is tied to the local imperative surface and reinforces, rather than replaces, the grammatical command.\",\"representative_source_ids\":[\"QP-093af0ed\",\"QP-b16e0b18\",\"MP-93b4697d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:rare-conditional-placement","source_type":"word_analysis","support_id":"sup_842c3f44230edebfb4fc","text":"{\"blocking_evidence\":null,\"headline\":\"marked rare transition word\",\"reader_payoff\":\"The reader notices that this is not a throwaway term for finishing; the rare root and rare perfect placement make the transition lexically heavy.\",\"reason\":\"The contextual profile marks the exact root-form occurrence as low-occurrence, and the local evidence identifies this as the perfect form in the conditional hinge.\",\"representative_source_ids\":[\"MS-810f3924\",\"QI-2452d512\",\"QH-2053a9b2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:wider-root-field-resonance","source_type":"word_analysis","support_id":"sup_8a185875a3f7b7c1c31a","text":"{\"blocking_evidence\":null,\"headline\":\"erected objects and fixed positions as resonance\",\"reader_payoff\":\"The reader notices that the root makes the command more concrete than generic striving, with erected things, fixed positions, and devotional misdirection present only as controlled background.\",\"reason\":\"V4 accepts several branches for {{ar:ن ص ب}} ({{tr:n-ṣ-b}}), including upright setting, cultic stones, assigned portions, and fixed bases, but the local intransitive imperative selects self-exertion and does not license a direct erected object.\",\"representative_source_ids\":[\"QS-513cb995\",\"QS-a1329ffd\",\"MS-a9b436c5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:sound-of-release","source_type":"word_analysis","support_id":"sup_8e28eb2ecfab6a61e3d3","text":"{\"blocking_evidence\":null,\"headline\":\"open syllables then guttural close\",\"reader_payoff\":\"The reader notices that the word's sound can perform release: open movement closes deep in the throat before the harder final command.\",\"reason\":\"This is a phonetic observation tied to the local surface form and is not contradicted by the lexical or grammatical evidence.\",\"representative_source_ids\":[\"QP-82cbc03b\",\"MP-f83a6276\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:1:consequential-pivot-from-ease","source_type":"word_analysis","support_id":"sup_a8bc742e789a647a5c20","text":"{\"blocking_evidence\":null,\"headline\":\"consequence from prior assurance\",\"reader_payoff\":\"The reader notices that the command grows out of the assurance in 94:5-6, so ease becomes the ground for renewed obligation rather than an endpoint.\",\"reason\":\"QAC describes the opening particle as connecting this ayah to 94:5-6, and attachment evidence then treats the following words as the conditional frame for the command.\",\"representative_source_ids\":[\"QG-48e87949\",\"MG-479f8054\",\"QB-0711e0a4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2:extended-command-scope","source_type":"word_analysis","support_id":"sup_aa55cbc778ac40c18a62","text":"{\"blocking_evidence\":null,\"headline\":\"possible wider response through 94:8\",\"reader_payoff\":\"The reader notices that the condition can prepare a compound command movement into 94:8, while the grammar still marks {{ar:فَ ٱنصَبْ}} ({{tr:fa inṣab}}) as the immediate response.\",\"reason\":\"Attachment evidence strongly licenses the same-ayah apodosis, so the 94:8 extension survives as discourse continuation rather than as the primary local parse.\",\"representative_source_ids\":[\"QG-0cc94f0e\",\"QB-8ce97d7c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:4:distinct-from-opening-fa","source_type":"word_analysis","support_id":"sup_b570f7f56e40c56c4a1f","text":"{\"blocking_evidence\":null,\"headline\":\"inner hinge, not outer bridge\",\"reader_payoff\":\"The reader notices the nested grammar: the first {{ar:فَ}} ({{tr:fa}}) bridges from prior discourse, while this {{ar:فَ}} ({{tr:fa}}) binds the condition to its command.\",\"reason\":\"The two particles occupy different clause positions, and the attachment evidence assigns the response function specifically to word 4.\",\"representative_source_ids\":[\"QG-4a575641\",\"QT-37b742d4\",\"MT-0994f81a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3","source_type":"word_analysis","support_id":"sup_bb843f82a77a35198d4f","text":"{\"gloss_range\":\"to finish, become free, or be emptied in the temporal condition; locally a completed state of availability that triggers the command\",\"prose\":\"{{ar:فَرَغْتَ}} ({{tr:faraghta}}) is the completed state inside the when-clause: the addressee is the one who has finished, and under {{ar:إِذَا}} ({{tr:idhā}}) that future completion is treated as already reached. That second-person form pulls the broad assurance of 94:5-6 back onto the addressee at the moment the condition changes. The missing object keeps the condition reusable: it does not name which work has ended, only the moment when the addressee is freed for what comes next. The root {{ar:ف ر غ}} ({{tr:f-r-gh}}) adds more than administrative finishing; its accepted field of emptiness, freedom after occupation, and deliberate turning, including root-family turning evidence at 37:91, lets completion feel like release into redirected action toward the next imperative in 94:8, while the local Form I perfect keeps the selected sense centered on the addressee's own completed availability. Pouring-language echoes from the same root family, including 2:250 and 7:126, can color that emptied state, but they do not replace the local grammar. The word is also rare in this exact role, and its open syllables ending in the guttural close make the release audible before the clipped command arrives.\",\"root_display\":\"{{ar:ف ر غ}} ({{tr:f-r-gh}})\",\"root_gloss_range\":\"root range includes completion or freedom after occupation, emptying or pouring out, and deliberate turning; local Form I perfect selects completion/freeing while allowing limited emptying and redirection pressure\",\"surface_display\":\"{{ar:فَرَغْتَ}} ({{tr:faraghta}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:bound-wasl-onset","source_type":"word_analysis","support_id":"sup_bc8217f1b8ac71bcfdf6","text":"{\"blocking_evidence\":null,\"headline\":\"response flows into command onset\",\"reader_payoff\":\"The reader notices that the preceding response particle carries straight into the imperative onset, making command and consequence feel fused.\",\"reason\":\"The local surface places {{ar:فَ}} ({{tr:fa}}) immediately before the imperative, matching the syntactic apodosis relation.\",\"representative_source_ids\":[\"QF-f06a5b3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:1:paired-fa-cadence","source_type":"word_analysis","support_id":"sup_bd308990153fe5ac3205","text":"{\"blocking_evidence\":null,\"headline\":\"paired clipped sequence markers\",\"reader_payoff\":\"The reader notices that the repeated particle is also an audible frame, making the ayah move in short linked steps rather than in loose clauses.\",\"reason\":\"Both occurrences are surface particles in the same short ayah, and the clause evidence supports a layered sequence rather than a single repeated function.\",\"representative_source_ids\":[\"QT-c5021f74\",\"MT-d234d1d1\",\"QP-329ebc30\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:4:apodosis-response-marker","source_type":"word_analysis","support_id":"sup_be1916f05d2a6e5e679f","text":"{\"blocking_evidence\":null,\"headline\":\"condition answered by command\",\"reader_payoff\":\"The reader notices that exertion is not merely next in sequence; it is the required response produced by the completed condition.\",\"reason\":\"Attachment evidence identifies {{ar:فَ ٱنصَبْ}} ({{tr:fa inṣab}}) as the apodosis of the {{ar:إِذَا}} ({{tr:idhā}}) clause, and QAC describes this particle as introducing the response.\",\"representative_source_ids\":[\"QG-4989ba94\",\"QG-7388c418\",\"MG-aca619d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:self-affected-addressee","source_type":"word_analysis","support_id":"sup_c097ff10951652e8f5f1","text":"{\"blocking_evidence\":null,\"headline\":\"agent who is also freed\",\"reader_payoff\":\"The reader notices that the addressee is not only commanded later; already in the condition, the same person becomes the one finished or freed.\",\"reason\":\"The second-person suffix is part of the perfect verb, and the local form is Form I rather than a causative pattern that would make someone else emptied.\",\"representative_source_ids\":[\"QS-c6fc7633\",\"QF-61451046\",\"QF-7e5e5f5a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:unnamed-completion-domain","source_type":"word_analysis","support_id":"sup_c0e6f4c96fc47a87f6d8","text":"{\"blocking_evidence\":null,\"headline\":\"open completed domain\",\"reader_payoff\":\"The reader notices that the verse names the completion moment without naming the completed task, making the trigger broad while preserving urgency.\",\"reason\":\"The local verb instance is intransitive with no object or prepositional complement, so the open-domain reading is licensed without supplying a mandatory object.\",\"representative_source_ids\":[\"QG-ace20614\",\"QT-0f3e86bc\",\"QT-a02bd1dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:direct-perfect-trigger","source_type":"word_analysis","support_id":"sup_c251734db35ea5701718","text":"{\"blocking_evidence\":null,\"headline\":\"second-person perfect trigger\",\"reader_payoff\":\"The reader notices that the addressee personally carries the completion inside the verb, and that completion is made certain enough to trigger the command.\",\"reason\":\"QAC and attachment evidence identify {{ar:فَرَغْتَ}} ({{tr:faraghta}}) as a Form I perfect, second masculine singular verb with an implicit second-person subject inside the {{ar:إِذَا}} ({{tr:idhā}}) condition.\",\"representative_source_ids\":[\"QG-8c56d151\",\"QG-96e7c4ee\",\"MG-5c029133\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:qiraat-pressure","source_type":"word_analysis","support_id":"sup_c410426766efb96f4e55","text":"{\"blocking_evidence\":null,\"headline\":\"variant readings expose pressure\",\"reader_payoff\":\"The reader notices that small changes in final vowel, form, or transitivity can swing the image toward softer closure, pouring out, or making stand, which clarifies what the standard command is doing.\",\"reason\":\"Accepted or apparatus variants can illuminate contrast, but the local canonical surface remains Form I imperative and intransitive in the supplied evidence.\",\"representative_source_ids\":[\"QF-3e26b083\",\"QF-784232c3\",\"MF-2c230d73\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:5:cultic-object-contrast","source_type":"word_analysis","support_id":"sup_cdec11ee31269c06bb32","text":"{\"blocking_evidence\":null,\"headline\":\"cultic stones contrasted, not commanded\",\"reader_payoff\":\"The reader notices a pointed root contrast: the root that can name erected cultic objects in prohibition contexts is repurposed here as upright striving toward commanded effort.\",\"reason\":\"The references to cultic objects at 5:3, 5:90, and 70:43 are valid root-family contrast, but local grammar has an intransitive imperative and no object of worship.\",\"representative_source_ids\":[\"MI-f9b559ec\",\"QE-d7a3965c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:2:when-then-command-frame","source_type":"word_analysis","support_id":"sup_dedc7e92ad8a54d10bfd","text":"{\"blocking_evidence\":null,\"headline\":\"temporal condition and response\",\"reader_payoff\":\"The reader notices that the verse is not a loose sequence but a conditional command structure: completion creates the occasion for exertion.\",\"reason\":\"QAC identifies {{ar:إِذَا}} ({{tr:idhā}}) as temporal-conditional, and attachment evidence explicitly links {{ar:إِذَا فَرَغْتَ}} ({{tr:idhā faraghta}}) as protasis with {{ar:فَ ٱنصَبْ}} ({{tr:fa inṣab}}) as apodosis.\",\"representative_source_ids\":[\"QG-f7db6594\",\"QT-edd2e500\",\"MT-76bb0e3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:7:2:1","source_type":"qac_morpheme","support_id":"sup_f079c82446d1daac4d82","text":"{\"lemma_ar\":\"فَرَغْ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:farago|ROOT:frg|2MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"94:7:2:1\",\"qac_word_ref\":\"94:7:2\",\"root_ar\":\"ف ر غ\",\"surface_ar\":\"فَرَغْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:7:3:pouring-echo","source_type":"word_analysis","support_id":"sup_f9c0fd7825baaa291d7f","text":"{\"blocking_evidence\":null,\"headline\":\"emptied-poured resonance\",\"reader_payoff\":\"The reader notices a root-family resonance in which the moment of being emptied can be heard against Quranic pouring-language pleas for being filled, including 2:250 and 7:126.\",\"reason\":\"V4 accepts a pouring and emptying branch for the root, but the local word is Form I perfect with no same-form corpus examples, so the echo is limited to resonance and cannot govern the local parse.\",\"representative_source_ids\":[\"QS-2019ab4a\",\"QE-579e2dc9\",\"ME-f764852b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001147/B001","root_001507/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001147","role":"Freedom or emptiness after occupation supplies the released capacity at the first side of the relay.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Weariness and strenuous toil supply the costly effort into which that released capacity is converted.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"changed_reading":{"after":"Whenever an occupation releases you, convert the newly free capacity immediately into chosen exertion.","before":"Finish one matter, then undertake another unspecified action."},"confidence":"strong","focus_anchor":"The temporal relay فَإِذَا ... فَـ joins second-person completion in فَرَغْتَ directly to the imperative فَٱنصَبْ.","mechanism":"Freedom after occupation is treated as newly available capacity, and the following imperative immediately spends that capacity in effort. Completion is therefore a transfer point rather than a terminal rest.","model_id":"baseline_release_to_chosen_strain"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_release_to_chosen_strain","source_type":"hft","support_id":"sup_9faef572502a2fdd2210","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001147/B002","root_001507/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001147","role":"Pouring out and emptying a container supplies active evacuation rather than passive leisure.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Setting something upright and prominent supplies the constructive form that follows evacuation.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"changed_reading":{"after":"Empty the occupied space, then use the clearance to establish a visible, upright form of action.","before":"Completion merely precedes more labor."},"confidence":"medium","focus_anchor":"The two focus roots can form a single material sequence: evacuation in فَرَغْتَ followed by erection in فَٱنصَبْ.","mechanism":"The first verb can image contents being poured out of a vessel; the second can image something being fixed upright and made salient. The verse then becomes a clear-and-establish operation: removal creates the room in which a new stance or work can be installed.","model_id":"baseline_empty_then_erect"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_empty_then_erect","source_type":"hft","support_id":"sup_e8415fc36a3b17a7ffa5","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَإِذَا فَرَغْتَ فَٱنصَبْ","ayah_ref":"94:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001147/B006","root_001507/B001","root_001507/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001147","role":"Deliberately turning and devoting oneself to a matter supplies exclusive attention.","root":"ف ر غ","source_ref":"94:7","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001507","role":"A fixed base, origin, or threshold supplies durable footing and measure for the devoted action.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Upright prominent placement turns inward concentration into an established stance.","root":"ن ص ب","source_ref":"94:7","source_word_indices":["3"]}],"changed_reading":{"after":"When attention has been cleared and made single, establish that devotion on a fixed, upright footing.","before":"Wait for spare time and then become busy again."},"confidence":"medium","focus_anchor":"فَرَغْتَ can involve turning deliberately to one matter, while فَٱنصَبْ can evoke both erect placement and a fixed base or threshold.","mechanism":"The condition is not only that a prior task has ended; it can mark attention becoming exclusive. The imperative answers that concentration by giving it stable footing, measure, and outward form.","model_id":"baseline_exclusive_attention_fixed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_exclusive_attention_fixed","source_type":"hft","support_id":"sup_eae703f666f77d883fbd","trust":"legacy_unbound"}]}
</lane_packet_json>
