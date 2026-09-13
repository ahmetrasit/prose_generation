# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **94:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s094-regular-20260912/s094/94_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "94:3",
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
{"branch_registry":[{"boundary":"Bu dal sırtı, gün ortasını veya belirli bir edatla kurulan öğrenme anlamını kapsamaz.","branch_kind":"bare","branch_ref":"root_000970/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"açığa çıkıp belirginleşmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceden gizli olan şey açığa çıkar, belirginleşir ve artık saklı kalmaz."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gizli veya örtülü bir şeyin görünür ya da anlaşılır hale geldiği genel bağlamlarda kullanılır.","boundary_detail":"Bu dal sırtı, gün ortasını veya belirli bir edatla kurulan öğrenme anlamını kapsamaz.","branch_image_ar":"البروز والانكشاف","concept_gloss":"açığa çıkıp belirginleşmek","definition":"Gizli, örtülü veya fark edilmeyen bir şeyin belirerek görülebilir ve anlaşılır duruma gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceden gizli olan şey açığa çıkar, belirginleşir ve artık saklı kalmaz."}],"identity_rationale":"Kaynak sözü, gizli veya örtülü bir şeyin belirip görülebilir ve anlaşılır duruma gelmesini anlatır. Verilen dal çerçevesi bu çekirdeği doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"açığa çıkmak, belirip anlaşılır olmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"görünür ve dışta olan"}],"lexicalization_note":"Tanım yalın dalın açığa çıkma çekirdeğiyle sınırlıdır; kalıplaşmış kullanımlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü karışma, açığa çıkma ile bilgiye ulaşma arasındaki sınırda bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B001 nesnenin görünür veya anlaşılır duruma gelişini, B008 ise belirli bir kalıp içinde öznenin bilgi edinmesini anlatır.","focus_only":"Bu dalda şeyin kendisi gizlilikten çıkıp belirginleşir.","gloss":"açığa çıkma ile öğrenme ayrımı","neighbor_only":"Komşu dalda kişi bir konuya ilişkin bilgiye ulaşır.","neighbor_ref":"root_000970/B008","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceden erişilemeyen bir içerik erişilebilir hale gelir."}],"source_phrase_ar":"ظهر الشيء إذا انكشف وبرز (maqayis)؛ الظهور بدو الشيء الخفي (ayn;tahdhib)؛ ظهر الشيء ظهورا تبين (sihah)؛ أن يحصل شيء على ظهر الأرض فلا يخفى (mufradat)","source_summary":"Kaynaklar, anlamın gizlilikten açıklığa ve fark edilebilirliğe geçiş olduğunu ortak biçimde bildirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ظهور الشيء وانكشافه وتبينه وما كان ظاهرا غير باطن","what_is_not_ar":"ليس خاصا بظهر الجارحة ولا وقت الظهر"},"support_links":[]},{"boundary":"Çekirdek beden sırtı ve arka yüzdür; bağlama, yardım etme veya açığa çıkma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B002","candidate_links":[{"candidate_id":"cand_3ea049afe073cca537db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"sırt ve arka yüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sırt, bedende karın tarafının karşısındaki bölüm; nesnede ise buna benzetilen arka yüzdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sırtın güçlü, ağrılı veya darbeyle zarar görmüş oluşu ayrı türemiş kullanımlarla anlatılır."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedenin sırtı, nesnenin arka yüzü ve sırtın durumunu bildiren türemiş kullanımlar için geçerlidir.","boundary_detail":"Çekirdek beden sırtı ve arka yüzdür; bağlama, yardım etme veya açığa çıkma anlamı değildir.","branch_image_ar":"الظهر وخلاف البطن","concept_gloss":"sırt ve arka yüz","definition":"Canlının karın tarafının karşısındaki sırtı veya bir şeyin ön ya da iç yüzüne karşı arka yüzüdür. Sırtın güçlü, ağrılı ya da zarar görmüş olması bu çekirdeğe bağlı özel kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sırt, bedende karın tarafının karşısındaki bölüm; nesnede ise buna benzetilen arka yüzdür."},{"facet_id":"F002","role":"associated_use","statement":"Sırtın güçlü, ağrılı veya darbeyle zarar görmüş oluşu ayrı türemiş kullanımlarla anlatılır."}],"identity_rationale":"Kaynak sözü sırtı, karın ya da ön tarafın karşısındaki arka yüz olarak verir ve sırtın güçlü veya ağrılı oluşunu buna bağlı kullanımlar olarak ekler. Dal çerçevesi bu yapıyı korur.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"sırt; karın ya da ön tarafın karşıtı olan arka yüz"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sırtı güçlü kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sırtı ağrıyan veya incinmiş kimse"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"birinin sırtına vurmak veya zarar vermek"},{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"kolları arkada bağlayan veya yere düşüren tutuş"}],"lexicalization_note":"Yalın sırt anlamı ile güçlü, ağrılı veya zarar görmüş sırtı bildiren türemiş kullanımlar ayrı tutulur.","neighbor_coverage_note":"Adaylar içinde en yararlı sınır, bedensel arka yüz ile dışta ya da üstte kalan yüz arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B002 bedensel sırtı ve arka yönü merkez alır; B003 ise yerin yüksek kesimini ve kaplamanın dış ya da üst yüzünü merkez alır.","focus_only":"Bu dal bedenin sırtını ve nesnenin arka yüzünü temel alır.","gloss":"arka yüz ile dış yüz ayrımı","neighbor_only":"Komşu dal yüksek araziyi ve dışta ya da üstte kalan yüzeyi kapsar.","neighbor_ref":"root_000970/B003","relation_type":"near_neighbor","shared_zone":"İki dal da içe veya öne karşı konumlanan bir yüzü anlatabilir."}],"source_phrase_ar":"ظهر الإنسان خلاف بطنه (maqayis)؛ الظهر خلاف البطن من كل شيء (ayn;sihah;tahdhib)؛ الظهر الجارحة وجمعه ظهور (mufradat)؛ رجل مظهر شديد الظهر ورجل ظهر يشتكي ظهره (maqayis;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar sırtı karın tarafının karşıtı sayar; güç, ağrı ve sırtı yaralama bildiren kullanımları da bu organ anlamına bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الظهر جارحة أو جهة مقابلة للبطن في الإنسان وغيره وما ينسب إلى شدة الظهر أو وجعه","what_is_not_ar":"ليس معنى العون ولا الظهار الفقهي ولا مجرد الظهور المعنوي"},"support_links":["sup_5954c008807b647b10d2"]},{"boundary":"Yükselmiş arazi ile dış veya üst yüz bağlantılı fakat ayrı uygulamalardır; yalın açığa çıkma anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B003","candidate_links":[{"candidate_id":"cand_1815138d94a3d37806a7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"yüksek ya da dışta kalan yüz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Arazi kullanımında çevresinden yüksek, belirgin ve açıkta kalan yer kesimini gösterir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nesnelerde astara veya iç yüze karşı dışta ya da üstte kalan yüzü gösterir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yüksek arazi kesimiyle nesnenin dış veya üst yüzünü birlikte kapsayan üst düzey karşılık olarak kullanılır.","boundary_detail":"Yükselmiş arazi ile dış veya üst yüz bağlantılı fakat ayrı uygulamalardır; yalın açığa çıkma anlamına genişletilmez.","branch_image_ar":"ظهر الأرض وظاهرها","concept_gloss":"yüksek ya da dışta kalan yüz","definition":"Yerin çevresine göre yükselmiş ve açıkta kalan bölümü ile bir şeyin içe bakan yüzünün karşıtı olan dış ya da üst yüzüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Arazi kullanımında çevresinden yüksek, belirgin ve açıkta kalan yer kesimini gösterir."},{"facet_id":"F002","role":"extension","statement":"Nesnelerde astara veya iç yüze karşı dışta ya da üstte kalan yüzü gösterir."}],"identity_rationale":"Kaynak sözü hem yerin yükselmiş kesimini hem de bir nesnenin içe bakan yüzünün karşıtı olan dış ya da üst yüzü içerir. Verilen çerçeve kullanılabilir, ancak bu iki uygulamanın tek bir yer anlamı gibi birleştirilmemesi gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yerin yüksek veya açıkta kalan yüzü"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dış ya da üst yüz; astarın karşıtı"}],"lexicalization_note":"Yerle kurulan kalıp ile dış ya da üst yüzü bildiren biçim ayrı yüzey uygulamaları olarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bedensel sırt dalı, yüzey sınırını açıklayan en yakın karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B003 yüzeyin dışta veya üstte oluşunu, B002 ise beden sırtını ve arka yönü temel alır.","focus_only":"Bu dal yükselmiş araziyi ve dış ya da üst yüzeyi kapsar.","gloss":"dış yüz ile sırt ayrımı","neighbor_only":"Komşu dal beden sırtını ve önün karşısındaki arka yüzü kapsar.","neighbor_ref":"root_000970/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal karşıt yüzler üzerinden konum bildirir."}],"source_phrase_ar":"الظهر من الأرض ما غلط وارتفع (ayn;tahdhib)؛ الظاهرة كل أرض غليظة مشرفة (ayn)؛ الظواهر أشراف الأرض (sihah;tahdhib)؛ ظهر الأرض وبطنها (mufradat)؛ الظهارة خلاف البطانة (ayn;sihah;tahdhib)","source_summary":"Kaynaklar yüksek ve belirgin araziyi, ayrıca iç yüzün karşısındaki dış ya da üst yüzü aynı yüzey ailesinde toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"ظهر الأرض وظاهر الشيء وما غلظ وارتفع أو علا وبرز من أرض أو ثوب أو بساط","what_is_not_ar":"ليس نفس ظهور الأمر بعد خفائه ولا الظهر الجارحة"},"support_links":["sup_c44bbb58772171dd5594"]},{"boundary":"Bu dal yalnızca öğle zamanına ve o zamana bağlı eylemlere ilişkindir; genel görünürlük anlamı değildir.","branch_kind":"bare","branch_ref":"root_000970/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"öğle vakti ve ona bağlı eylemler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel zaman dilimi gün ortası ve hemen sonrasındaki öğle vaktidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öğle namazı, öğle vaktine girme veya yol alma ve sürünün o saatte suya gelmesi zaman çekirdeğine bağlıdır."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gün ortasını ve doğrudan o zamana bağlanan namaz, hareket veya sulama kullanımlarını kapsar.","boundary_detail":"Bu dal yalnızca öğle zamanına ve o zamana bağlı eylemlere ilişkindir; genel görünürlük anlamı değildir.","branch_image_ar":"وقت الظهر والظهيرة","concept_gloss":"öğle vakti ve ona bağlı eylemler","definition":"Gün ortası ve güneşin tepeyi geçmesi çevresindeki öğle vaktidir. O vakitte kılınan namaz, o vakte girme ya da yol alma ve hayvanların öğleyin suya gelmesi buna bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel zaman dilimi gün ortası ve hemen sonrasındaki öğle vaktidir."},{"facet_id":"F002","role":"associated_use","statement":"Öğle namazı, öğle vaktine girme veya yol alma ve sürünün o saatte suya gelmesi zaman çekirdeğine bağlıdır."}],"identity_rationale":"Kaynak sözü gün ortası ve güneşin tepeyi geçtiği öğle vaktini merkez alır; namaz, o vakte girme veya yol alma ve hayvanların o saatte suya gelmesi buna bağlıdır. Dal çerçevesi bu bağı doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"öğle vakti ve o vakitte kılınan namaz"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gün ortası veya öğle sıcağı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"öğle vaktine girmek veya o sırada yol almak"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"hayvanların her gün öğleyin suya gelmesi"}],"lexicalization_note":"Yalın zaman çekirdeği tanımlanır; namaz, yol alma ve suya gelme bu çekirdeğin bağlı kullanımlarıdır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; hiçbiri öğle zamanı ile ona bağlı eylemler arasındaki sınırı daha yararlı biçimde keskinleştirmedi.","source_phrase_ar":"وقت الظهر والظهيرة أظهر أوقات النهار (maqayis)؛ الظهر ساعة الزوال وصلاة الظهر والظهيرة حد انتصاف النهار (ayn;tahdhib)؛ الظهر بعد الزوال والظهيرة الهاجرة (sihah)؛ صلاة الظهر والظهيرة وقت الظهر وأظهر فلان حصل في ذلك الوقت (mufradat)؛ الظاهرة أن ترد كل يوم ظهرا (sihah;tahdhib)","source_summary":"Kaynaklar öğle zamanında birleşir ve namazı, bu vakte girmeyi, yol almayı ve günlük sulama gelişini ona bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"وقت الظهر والظهيرة والدخول في ذلك الوقت والصلاة المسماة به والورد فيه","what_is_not_ar":"ليس مطلق البروز ولا الظهر الجارحة"},"support_links":[]},{"boundary":"Dal taşıma hayvanını ve yedek deveyi anlatır; genel yardım veya soyut önlem anlamına dönüşmez.","branch_kind":"bare","branch_ref":"root_000970/B005","candidate_links":[{"candidate_id":"cand_cd329fee262b4b69404a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"yük bineği ve yedek deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanlar yükü sırtlarında taşıdıkları için binek ve yük hayvanı topluluğu bu adla anılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gerektiğinde binmek veya başka bir ihtiyacı karşılamak için hazır tutulan deve özel bir yedek türüdür."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yük ya da yolcu taşıyan hayvanlarla ihtiyaç için hazır bekletilen deve söz konusu olduğunda kullanılır.","boundary_detail":"Dal taşıma hayvanını ve yedek deveyi anlatır; genel yardım veya soyut önlem anlamına dönüşmez.","branch_image_ar":"الركاب والعدة المحمولة","concept_gloss":"yük bineği ve yedek deve","definition":"Yük veya yolcu taşımada kullanılan binek hayvanları ile gerektiğinde kullanılmak üzere hazır tutulan yedek devedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanlar yükü sırtlarında taşıdıkları için binek ve yük hayvanı topluluğu bu adla anılır."},{"facet_id":"F002","role":"specialization","statement":"Gerektiğinde binmek veya başka bir ihtiyacı karşılamak için hazır tutulan deve özel bir yedek türüdür."}],"identity_rationale":"Kaynak sözü, yük veya yolcu taşıyan binekleri sırtları üzerinden adlandırır ve gerektiğinde kullanılmak üzere tutulan deveyi aynı somut alana bağlar. Verilen dal çerçevesi bu iki kullanımı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yük taşıyan binek veya deve topluluğu"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gerektiğinde kullanılmak üzere hazır tutulan deve"}],"lexicalization_note":"Yalın dal taşıma için kullanılan hayvanları kapsar; soyut güvence anlamı yalnızca ayrı dalda ele alınır.","neighbor_coverage_note":"Adaylar değerlendirildi; en yararlı karşılaştırma, somut yedek hayvan ile soyut hazırlık anlamı arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B005 somut hayvanı ve taşıma işlevini, B021 ise bu örnekten soyutlanan önlem alma ve güvence sağlama tutumunu merkez alır.","focus_only":"Bu dal somut taşıma hayvanını ve yedek deveyi adlandırır.","gloss":"yedek hayvan ile önlem ayrımı","neighbor_only":"Komşu dal yedek hazırlama yoluyla genel önlem ve güvenceyi anlatır.","neighbor_ref":"root_000970/B021","relation_type":"near_neighbor","shared_zone":"Yedek deve, gelecekteki ihtiyaca karşı hazır bulundurma düşüncesini taşır."}],"source_phrase_ar":"الركاب الظهر لأن الذي يحمل منها الشيء ظهورها (maqayis)؛ الظهر الركاب تحمل الأثقال في السفر (ayn;tahdhib)؛ الظهر الركاب وبنو فلان مظهرون (sihah)؛ يعبر عن المركوب بالظهر وظهري معد للركوب (mufradat)؛ البعير الظهري العدة للحاجة (sihah;tahdhib)","source_summary":"Kaynaklar yük taşıyan binekleri ve ihtiyaç halinde kullanılmak üzere hazır tutulan deveyi somut taşıma alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الظهر بمعنى الركاب التي تحمل الأثقال والبعير المعد للحاجة أو الركوب","what_is_not_ar":"ليس العون المجازي إلا إذا صرح بكونه مستندا إلى الظهر"},"support_links":["sup_52b4c2e3a56e5271f92b"]},{"boundary":"Bu dal destek verme veya alma üzerinedir; üstün gelme ve birbirine sırt çevirme anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B006","candidate_links":[{"candidate_id":"cand_6443dda8797836b7e903","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"yardım edip güçlendirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir taraf diğerine yardım ve dayanak sağlayarak onun gücünü artırır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı destek ilişkisi karşılıklı yardımlaşma, yardımcı kişi ve birinden güç alma biçimlerinde gerçekleşir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Destek veren kişi, yardım eylemi, karşılıklı yardımlaşma ve birinden güç alma bağlamlarının tümünde geçerlidir.","boundary_detail":"Bu dal destek verme veya alma üzerinedir; üstün gelme ve birbirine sırt çevirme anlamları dışarıda kalır.","branch_image_ar":"التقوي بالظهر والعون","concept_gloss":"yardım edip güçlendirmek","definition":"Birine yardım ederek onu güçlendirmek, karşılıklı destekleşmek veya bir yardımcıdan güç almaktır; destek veren kişi de bu çekirdeğin adlandırılmış katılımcısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir taraf diğerine yardım ve dayanak sağlayarak onun gücünü artırır."},{"facet_id":"F002","role":"extension","statement":"Aynı destek ilişkisi karşılıklı yardımlaşma, yardımcı kişi ve birinden güç alma biçimlerinde gerçekleşir."}],"identity_rationale":"Kaynak sözü yardımcıyı, yardım etmeyi, karşılıklı destekleşmeyi ve birinden güç almayı aynı destek çekirdeğinde toplar. Dal çerçevesi katılımcı rollerini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yardımcı, destekçi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yardımlaşma ve destek olma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ondan yardım alıp güçlenmek"}],"lexicalization_note":"Yardımcı adı ve yardım etme biçimleriyle, birinden yardım alma kalıbı kapsamları belirtilerek ayrı tutulur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; destekçi topluluğu ve karşılıklı sırt çevirme, dalın sınırını en iyi gösteren iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B006 destek ilişkisinin kişi ve eylem biçimlerini kapsar; B016 ise özellikle yardımcılar ve yakınlardan oluşan topluluğu adlandırır.","focus_only":"Bu dal yardım eylemini, yardımcı kişiyi ve yardım alma ilişkisini kapsar.","gloss":"yardım ilişkisi ile destekçi topluluğu","neighbor_only":"Komşu dal kişinin güç aldığı toplu destekçi çevresini adlandırır.","neighbor_ref":"root_000970/B016","relation_type":"near_synonym","shared_zone":"Her iki dalda da başkasının desteği kişinin gücünü artırır."},{"boundary_match":"opposed","distinction":"B006 dayanışma ve güçlendirme yönünde, B022 ise karşılıklı uzaklaşma ve ilişkiyi kesme yönünde işler.","focus_only":"Bu dal tarafların birbirine destek vererek yakınlaşmasını anlatır.","gloss":"destekleşme ile sırt çevirme","neighbor_only":"Komşu dal tarafların birbirine sırt çevirerek uzaklaşmasını anlatır.","neighbor_ref":"root_000970/B022","relation_type":"polarity_pair","shared_zone":"İki dal da tarafların birbirine göre toplumsal yönelişini düzenler."}],"source_phrase_ar":"الظهير المعين كأنه أسند ظهره إلى ظهرك (maqayis)؛ الظهير العون والمظاهر المعاون وهما يتظاهران أي يتعاونان (ayn)؛ الظهير المعين والمظاهرة المعاونة والتظاهر التعاون واستظهر به استعان به (sihah)؛ ظهير في معنى ظهراء أي أعوان وظاهروا أي عاونوا (tahdhib)؛ ظاهرته عاونته وما له منهم من ظهير أي معين (mufradat)","source_summary":"Kaynaklar yardımcı, yardım etme, karşılıklı destek ve birinden güç alma kullanımlarını ortak destek ilişkisine bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الظهير والمعين والمظاهر والتظاهر بمعنى المعاونة والاستعانة والتقوي بالأعوان","what_is_not_ar":"ليس الغلبة نفسها ولا التدابر الذي فيه جعل الظهر إلى الآخر"},"support_links":["sup_e63c0d8bc95eae738acf"]},{"boundary":"Anlam yalnızca belirtilen kalıpta geçerlidir; fiziksel üstüne çıkma ile üstün gelme ayrı bağlamsal gerçekleşmelerdir.","branch_kind":"collocation","branch_ref":"root_000970/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"üzerine çıkmak veya üstün gelmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güç ilişkilerinde karşı tarafı yenerek onun üzerinde üstünlük ve denetim kurmayı anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fiziksel bağlamda duvar, dam veya başka bir yüzeyin üstüne çıkmayı anlatır."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca belirtilen kalıbın fiziksel yükselme ya da güç ilişkisi bağlamlarında kullanılır.","boundary_detail":"Anlam yalnızca belirtilen kalıpta geçerlidir; fiziksel üstüne çıkma ile üstün gelme ayrı bağlamsal gerçekleşmelerdir.","branch_image_ar":"العلو والغلبة","concept_gloss":"üzerine çıkmak veya üstün gelmek","definition":"Belirtilen kalıp içinde bir yüzeyin üstüne çıkmak veya bir kişi, topluluk ya da alan üzerinde güç ve başarıyla üstünlük kurmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güç ilişkilerinde karşı tarafı yenerek onun üzerinde üstünlük ve denetim kurmayı anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Fiziksel bağlamda duvar, dam veya başka bir yüzeyin üstüne çıkmayı anlatır."}],"identity_rationale":"Kaynak sözü aynı kalıp içinde hem fiziksel olarak bir yüzeyin üstüne çıkmayı hem de bir kişi ya da şey üzerinde üstünlük kurmayı verir. Dal korunabilir, ancak fiziksel yükselme ile güç yoluyla üstün gelme tek işlemmiş gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"üstün gelmek veya üzerinde güç kurmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"damın veya yüzeyin üstüne çıkmak"}],"lexicalization_note":"Tanım yalnızca belirtilen edatlı yapıya bağlıdır ve bu yapının yükselme ile üstün gelme okumalarını ayırır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; aynı yapının bilgi edinme kullanımı en önemli biçimsel ve anlamsal karışma noktasıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B007 konumsal ya da güç bakımından üstte olmayı, B008 ise bilginin erişilebilir hale gelmesini ve öğrenilmesini anlatır.","focus_only":"Bu dal fiziksel üstüne çıkmayı veya güç yoluyla üstün gelmeyi anlatır.","gloss":"üstün gelme ile bilgi edinme","neighbor_only":"Komşu dal bir konuya ilişkin bilgiye ulaşıp onu öğrenmeyi anlatır.","neighbor_ref":"root_000970/B008","relation_type":"near_neighbor","shared_zone":"Her iki anlam aynı edatlı yapı içinde bir hedefe erişme görüntüsü taşıyabilir."}],"source_phrase_ar":"الظهور الغلبة (maqayis)؛ الظهور الظفر بالشيء (ayn;tahdhib)؛ ظهرت على الرجل غلبته وظهرت البيت علوته (sihah)؛ ظهر على الحائط وعلى السطح وظهر على الشيء إذا غلبه وعلاه (tahdhib)؛ ظهر عليه غلبه وليظهره على الدين كله (mufradat)","source_summary":"Kaynaklar kalıbın üstün gelme ve fiziksel olarak üstüne çıkma kullanımlarını birlikte kaydeder; iki okuma bağlama göre ayrılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الظهور على الشيء بمعنى علوه وغلبته والقدرة عليه والصعود فوقه","what_is_not_ar":"ليس مجرد الاطلاع على الخفي ولا العون"},"support_links":[]},{"boundary":"Dal yalnızca belirtilen kalıpta bilgiye erişmeyi anlatır; yenme veya yüzeyin üstüne çıkma anlamlarını içermez.","branch_kind":"collocation","branch_ref":"root_000970/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"bilgiye ulaşıp öğrenmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne daha önce bilmediği veya erişemediği bir bilgiye ulaşır."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilinmeyen, gizli veya kayıp bir şey hakkında bilgi edinilen kalıp bağlamlarında kullanılır.","boundary_detail":"Dal yalnızca belirtilen kalıpta bilgiye erişmeyi anlatır; yenme veya yüzeyin üstüne çıkma anlamlarını içermez.","branch_image_ar":"الاطلاع والعثور","concept_gloss":"bilgiye ulaşıp öğrenmek","definition":"Belirtilen kalıp içinde gizli, kayıp veya bilinmeyen bir konuya ilişkin bilgiye ulaşıp onu öğrenmek ya da bulmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne daha önce bilmediği veya erişemediği bir bilgiye ulaşır."}],"identity_rationale":"Kaynak sözü belirtilen kalıbı bir konuya ilişkin bilgiye ulaşma, bir şeyi bulma ve onu öğrenme anlamında açıkça sınırlar. Verilen dal çerçevesi bu bilgi edinme çekirdeğini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şeyi öğrenmek veya bulup ortaya çıkarmak"}],"lexicalization_note":"Bilgi edinme anlamı belirtilen kalıba bağlı tutulur ve yalın açığa çıkma anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı yapıdaki üstün gelme okuması, bilgi edinme sınırını en açık gösteren komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B008 bilişsel erişimi, B007 ise fiziksel yükseklik veya güç üstünlüğünü kodlar.","focus_only":"Bu dal bilinmeyen bir konuya ilişkin bilgi edinmeyi anlatır.","gloss":"öğrenme ile üstün gelme","neighbor_only":"Komşu dal fiziksel olarak üstüne çıkmayı veya güçle üstün gelmeyi anlatır.","neighbor_ref":"root_000970/B007","relation_type":"near_neighbor","shared_zone":"İki dal aynı edatlı yapı içinde bir hedefe erişme biçiminde kurulabilir."}],"source_phrase_ar":"ظهرت على كذا إذا اطلعت عليه (maqayis)؛ والله أظهرنا عليه أي أطلعنا (ayn)؛ أظهرني الله على ما سرق مني أي أعثرني عليه وظهرت على الأمر (tahdhib)؛ فلا يظهر على غيبه أحدا أي لا يطلع عليه (mufradat)","source_summary":"Kaynaklar bu kalıbı öğrenme, bir şeyin yerini bulma ve gizli bilgiye erişme çekirdeğinde birleştirir.","sources":["MQ","AY","TA","MU"],"what_is_ar":"الظهور على الأمر بمعنى الاطلاع عليه والعثور عليه وبلوغ معرفته","what_is_not_ar":"ليس الغلبة العسكرية أو الصعود الحسي إلا إذا قرن به علو أو قهر"},"support_links":[]},{"boundary":"Bu dal yalnızca gözün çıkıklığını anlatır; genel görünürlük veya dışta olma anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000970/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"çıkık göz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz çökük değil, yuvasını dolduracak biçimde dışa çıkık görünür."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca gözün yuvasına göre dışa çıkık yapısını anlatan özel kullanımda geçerlidir.","boundary_detail":"Bu dal yalnızca gözün çıkıklığını anlatır; genel görünürlük veya dışta olma anlamına genişletilmez.","branch_image_ar":"العين الظاهرة","concept_gloss":"çıkık göz","definition":"Gözün çukurunu doldurup dışa doğru belirgin biçimde çıkık olması ve çökük gözün karşıtını oluşturmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz çökük değil, yuvasını dolduracak biçimde dışa çıkık görünür."}],"identity_rationale":"Kaynak sözü gözün çukurunu dolduracak ölçüde dışa çıkık olmasını ve bunun çökük gözün karşıtı olduğunu belirtir. Verilen özel göz çerçevesi tam olarak desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çökük gözün karşıtı olan çıkık göz"}],"lexicalization_note":"Tanım gözle sınırlı sözlüksel birime bağlıdır ve genel bir dışa çıkma anlamı olarak kullanılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gözle sınırlı bu özel yapıyı açıklamak için ek bir komşu karşılaştırması gerekli görülmedi.","source_phrase_ar":"الظاهرة العين الجاحظة (maqayis)؛ الظاهرة العين الجاحظة وهي خلاف الغائرة (ayn)؛ الظاهرة من العيون الجاحظة (sihah)؛ العين الظاهرة التي ملأت نقرة العين وهي خلاف الغائرة (tahdhib)","source_summary":"Kaynaklar gözün dışa çıkık ve çökük gözün karşıtı oluşunda birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"العين الظاهرة أو الجاحظة الخارجة خلاف الغائرة","what_is_not_ar":"ليس كل ظاهر أو مكشوف بل صفة خاصة للعين"},"support_links":[]},{"boundary":"Bu dal belirli evlilik sözüne bağlıdır; sırttan, yardımdan veya genel yasaklamadan ibaret değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"eşe yönelik benzetmeli yasaklama sözü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Koca, eşini yakın bir kadınla sırt benzetmesi üzerinden kendisine yasak saydığını bildiren kalıbı söyler."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu geleneksel söz, ilişkiye dair bir giderim yükümlülüğü doğurur."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca geleneksel evlilik hukukundaki belirli benzetme sözü ve onun sonucu için kullanılır.","boundary_detail":"Bu dal belirli evlilik sözüne bağlıdır; sırttan, yardımdan veya genel yasaklamadan ibaret değildir.","branch_image_ar":"ظِهار المرأة","concept_gloss":"eşe yönelik benzetmeli yasaklama sözü","definition":"Kocanın eşini, evlenmesi sürekli yasak olan bir kadının sırtına benzeten belirli bir sözle kendisine yasak saydığını bildirmesidir; kaynak bu sözün bir giderim yükümlülüğü doğurduğunu da belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Koca, eşini yakın bir kadınla sırt benzetmesi üzerinden kendisine yasak saydığını bildiren kalıbı söyler."},{"facet_id":"F002","role":"associated_use","statement":"Bu geleneksel söz, ilişkiye dair bir giderim yükümlülüğü doğurur."}],"identity_rationale":"Kaynak sözü, kocanın eşini evlenmesi sürekli yasak bir kadının sırtına benzeterek kendisine yasak saydığını bildiren belirli sözü ve bunun doğurduğu yükümlülüğü anlatır. Dal çerçevesi bu geleneksel hukuk kullanımını doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kocanın eşini kendisine yasak saydığını bildiren geleneksel söz"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"eşini annesinin sırtına benzeterek kendisine yasak sayma sözü"}],"lexicalization_note":"Geleneksel işlem adı ile onu kuran belirli söz kalıbı birlikte, fakat kapsamları belirtilerek tanımlanır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; belirli hukuk kalıbı kendi başına yeterince sınırlı olduğundan ek karşılaştırma yayımlanmadı.","source_phrase_ar":"الظهار قول الرجل لامرأته أنت علي كظهر أمي (maqayis;sihah;mufradat)؛ مظاهرة الرجل امرأته إذا قال هي علي كظهر أمي أو كظهر ذات رحم محرم (ayn)؛ وأوجبت الكفارة على من ظاهر من امرأته (tahdhib)","source_summary":"Kaynaklar belirli sırt benzetmesini eşe yönelik yasaklama bildirimi sayar ve bunun giderim gerektiren bir işlem olduğunu kaydeder.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الظِهار من المرأة بقول الرجل أنت علي كظهر أمي أو ذات رحم محرم","what_is_not_ar":"ليس مطلق المعاونة ولا الظهور ولا ظهر الجارحة مجردا"},"support_links":[]},{"boundary":"Bu dal yalnızca kanat veya ok tüyünün dışta kalan bölümüne ilişkindir; beden sırtı değildir.","branch_kind":"bare","branch_ref":"root_000970/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"kanadın dış tüyleri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tüyün dışta görünen ya da sapın sırt yönüne karşılık gelen bölümü seçilir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanatta görünen tüyler veya ok yapımında tüy sapının sırt yönündeki parça için kullanılır.","boundary_detail":"Bu dal yalnızca kanat veya ok tüyünün dışta kalan bölümüne ilişkindir; beden sırtı değildir.","branch_image_ar":"ريش الظهار","concept_gloss":"kanadın dış tüyleri","definition":"Kanatta dıştan görünen tüyler veya ok tüyünde sapın sırt yönünden alınarak kullanılan bölümdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tüyün dışta görünen ya da sapın sırt yönüne karşılık gelen bölümü seçilir."}],"identity_rationale":"Kaynak sözü kanatta dıştan görünen tüyleri ve okun yapımında tüy sapının sırt yönünden alınan parçayı belirtir. Verilen dal çerçevesi bu özel tüy anlamını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kanadın dıştan görünen tüyleri veya tüy sapının sırt yönündeki parçası"}],"lexicalization_note":"Yalın sözlüksel biçimin özel tüy anlamı tanımlanır; genel dış yüz anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel tüy parçası anlamını daha iyi açıklayan, gereksiz olmayan bir komşu bulunmadı.","source_phrase_ar":"الظهار من الريش ما يظهر منه في الجناح (maqayis)؛ الظهار من الريش الذي يظهر من ريش الطائر وهو في الجناح (ayn;tahdhib)؛ الظهار ما جعل من ظهر عسيب الريشة والظهران الجانب القصير من الريش (sihah;tahdhib)","source_summary":"Kaynaklar kanadın görünen tüylerini ve tüy sapının sırt yönünden alınan kısmını aynı özel ad altında toplar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الظِهار أو الظهران من الريش وما جعل من ظهر عسيب الريشة في الجناح أو السهم","what_is_not_ar":"ليس البطنان ولا الظهر الجارحة"},"support_links":[]},{"boundary":"Bu dal geriye atıp ihmal etmeyi anlatır; ihtiyaç için yedek tutma ve önlem alma bunun karşıtı yöndedir.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"geriye atıp önemsememek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir şeyi arkasında bırakır ve ona ilgi göstermeyerek unutulmaya terk eder."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin unutulduğu, bir isteğin dikkate alınmadığı veya işin ilgisizce geride bırakıldığı bağlamlarda kullanılır.","boundary_detail":"Bu dal geriye atıp ihmal etmeyi anlatır; ihtiyaç için yedek tutma ve önlem alma bunun karşıtı yöndedir.","branch_image_ar":"جعله بظهره","concept_gloss":"geriye atıp önemsememek","definition":"Bir şeyi sanki sırtın arkasına atar gibi geride bırakmak, ona yönelmemek, onu unutmak veya önemsememektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir şeyi arkasında bırakır ve ona ilgi göstermeyerek unutulmaya terk eder."}],"identity_rationale":"Kaynak sözü bir şeyi sırtın arkasına atma görüntüsünden hareketle unutmayı, önemsememeyi ve ilgilenmeden geride bırakmayı anlatır. Dal çerçevesi bu ihmal çekirdeğini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"arkaya atılıp unutulan şey"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir isteği önemsemeyip geriye atmak"}],"lexicalization_note":"İhmal edilen şeyin adı ile bir isteği geriye atma kalıbı ayrı biçimler olarak, aynı ihmal çekirdeğinde tutulur.","neighbor_coverage_note":"Adaylar değerlendirildi; hazır tutma dalı, geriye atıp unutma çekirdeğinin en açık karşıt yönünü gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B012 eldeki şeyi ilgi dışına çıkarır; B021 ise tam tersine onu ihtiyaç halinde kullanılmak üzere korur ve güvenceye dönüştürür.","focus_only":"Bu dal şeyi geriye atarak unutmayı ve önemsememeyi anlatır.","gloss":"ihmal ile hazır tutma","neighbor_only":"Komşu dal şeyi ilerideki ihtiyaç için hazır tutarak önlem almayı anlatır.","neighbor_ref":"root_000970/B021","relation_type":"polarity_pair","shared_zone":"Her iki dal bir şeyin gelecekteki ihtiyaçla ilişkisini sırt görüntüsü üzerinden kurar."}],"source_phrase_ar":"الظهري كل شيء تجعله بظهر أي تنساه (maqayis)؛ الظهري الشيء تنساه وتغفل عنه (ayn;tahdhib)؛ لا تجعل حاجتي بظهر أي لا تنسها (sihah)؛ ظهرت بكذا أي خلفته ولم ألتفت إليه (mufradat)","source_summary":"Kaynaklar geride bırakma görüntüsünü unutma, ilgisizlik ve bir isteği önemsememe sonucuyla açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"جعل الشيء بظهر أو وراء الظهر بمعنى تركه ونسيانه والإعراض عنه والاستخفاف به","what_is_not_ar":"ليس العدة المدخرة للحاجة إلا إذا قصد الاحتياط لا الإهمال"},"support_links":[]},{"boundary":"Buradaki nitelik ayıbın kişiden uzak olmasıdır; ayıbın görünür hale gelmesi kastedilmez.","branch_kind":"collocation","branch_ref":"root_000970/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"ayıbı kişiden uzak olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olumsuz nitelik kişiye bağlanmaz ve onun üzerinde kalıcı bir yük oluşturmaz."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir suçlama veya kusurun muhataba bağlanmadığını bildiren kalıplaşmış sözlerde kullanılır.","boundary_detail":"Buradaki nitelik ayıbın kişiden uzak olmasıdır; ayıbın görünür hale gelmesi kastedilmez.","branch_image_ar":"ظاهر عنك العار","concept_gloss":"ayıbı kişiden uzak olmak","definition":"Bir ayıp, kusur veya suçlamanın kişiye yapışmaması, ondan uzak kalması ve onu sorumlu duruma düşürmemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olumsuz nitelik kişiye bağlanmaz ve onun üzerinde kalıcı bir yük oluşturmaz."}],"identity_rationale":"Kaynak sözü bir ayıp veya kusurun kişiye yapışmaması, ondan uzak kalması ve onun üzerinde yük oluşturmaması anlamını verir. Dal çerçevesi bu uzaklık ve sorumsuzluk sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"ayıbı sana yapışmayan, senden uzak söz veya durum"}],"lexicalization_note":"Anlam yalnızca ayıp veya kusurun kişiden uzaklığını bildiren kalıba bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ayıbın kişiye bağlanmaması sınırı ek bir komşu yayımlamadan yeterince açık kaldı.","source_phrase_ar":"أمر ظاهر عنك عاره أي زائل (maqayis;sihah)؛ ظهر عني هذا العيب أي نبا عني ولم يعلق بي (tahdhib)؛ تلك شكاة ظاهر عنك عارها (maqayis;sihah;tahdhib)","source_summary":"Kaynaklar ayıp veya kusurun kişiden uzak kalması ve ona yapışmaması anlamında birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"الأمر أو العار الظاهر عن الشخص بمعنى الزائل غير اللازم له","what_is_not_ar":"ليس الظهور بمعنى الانكشاف ولا الغلبة"},"support_links":[]},{"boundary":"Çekirdek ev eşyasıdır; genel yardımcı kişi veya soyut hazırlık anlamına genişletilmez.","branch_kind":"bare","branch_ref":"root_000970/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"ev eşyası ve yedek mallar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evde tutulan taşınır eşya ve giysiler bu adın somut gönderimini oluşturur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu eşyanın gerektiğinde yararlanılacak bir dayanak olması adlandırmanın açıklayıcı yönüdür."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evde bulunan eşya ve giysiler, özellikle gerektiğinde yararlanılan birikim olarak düşünüldüğünde kullanılır.","boundary_detail":"Çekirdek ev eşyasıdır; genel yardımcı kişi veya soyut hazırlık anlamına genişletilmez.","branch_image_ar":"الظهرة متاع البيت","concept_gloss":"ev eşyası ve yedek mallar","definition":"Evde bulunan eşya ve giysiler ile bunların kişiye günlük kullanımda dayanak ve yedek sağlamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evde tutulan taşınır eşya ve giysiler bu adın somut gönderimini oluşturur."},{"facet_id":"F002","role":"associated_use","statement":"Bu eşyanın gerektiğinde yararlanılacak bir dayanak olması adlandırmanın açıklayıcı yönüdür."}],"identity_rationale":"Kaynak sözü evde bulunan eşya ve giysileri adlandırır, bunların kişiye dayanak ve yedek sağladığı düşüncesini de açıklar. Verilen çerçeve somut eşya çekirdeğini ve bağlı işlevi doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"ev eşyası ve gerektiğinde yararlanılan mallar"}],"lexicalization_note":"Yalın sözlüksel biçimin ev eşyası anlamı tanımlanır; dayanak olma yalnızca bu eşyanın işlevsel açıklamasıdır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; soyut önlem dalı, eşyanın kendisi ile işlevi arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B014 somut ev eşyasını merkez alır; B021 ise herhangi bir yedek aracılığıyla önlem ve güvence oluşturma işlemini merkez alır.","focus_only":"Bu dal evdeki somut eşya ve giysileri adlandırır.","gloss":"ev eşyası ile hazırlık","neighbor_only":"Komşu dal yedek hazırlayarak önlem alma tutumunu anlatır.","neighbor_ref":"root_000970/B021","relation_type":"near_neighbor","shared_zone":"Evde tutulan eşya ilerideki ihtiyaç karşısında dayanak sağlayabilir."}],"source_phrase_ar":"الظهرة متاع البيت وأحسب هذه مستعارة من الظهر أيضا لأن الإنسان يستظهر بها (maqayis)؛ الظهرة بالتحريك متاع البيت (sihah)؛ الظهرة ما في البيت من المتاع والثياب (tahdhib)","source_summary":"Kaynaklar ev eşyası ve giysilerde birleşir; bunların kişiye dayanak sağlamasını adın bağlı açıklaması olarak verir.","sources":["MQ","SI","TA"],"what_is_ar":"الظهرة بمعنى متاع البيت وما يستظهر به ويتقوى به","what_is_not_ar":"ليس ظهر الجسد ولا العون الشخصي المباشر"},"support_links":[]},{"boundary":"Kara yolu ve dıştaki yüksek yer ayrı sözlüksel uygulamalardır; beden sırtı veya genel görünürlük anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"kara yolu ve dıştaki yüksek kesim","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yol kullanımında denizden değil karadan izlenen güzergahı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yer kullanımında kentin veya dağın dışta, yukarıda ya da çevrede kalan kesimini ve orada yaşayanları gösterir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kara güzergahını veya bir yerleşimin dış ve yüksek bölümünü bildiren ayrı sözlüksel bağlamlarda kullanılır.","boundary_detail":"Kara yolu ve dıştaki yüksek yer ayrı sözlüksel uygulamalardır; beden sırtı veya genel görünürlük anlamına genişletilmez.","branch_image_ar":"طريق الظهر وظواهر البلد","concept_gloss":"kara yolu ve dıştaki yüksek kesim","definition":"Deniz yolunun karşıtı olan kara yolu ile bir yerleşimin veya dağın iç kesimine karşı dışta ve yüksekte kalan bölgesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yol kullanımında denizden değil karadan izlenen güzergahı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Yer kullanımında kentin veya dağın dışta, yukarıda ya da çevrede kalan kesimini ve orada yaşayanları gösterir."}],"identity_rationale":"Kaynak sözü hem deniz yoluna karşı kara yolunu hem de bir yerleşimin ya da dağın dışta ve yüksekte kalan kesimini kaydeder. Dal korunabilir, ancak yol adı ile dış veya yüksek yer adı tek gönderim gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deniz yolunun karşıtı olan kara yolu"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"Mekke'nin dış veya yüksek kesimlerinde yaşayan Kureyşliler"}],"lexicalization_note":"Kara yolu kalıbı ile dış veya yüksek kesimde yaşayanları bildiren sözlüksel birim ayrı kapsamlarla tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yüksek ve dış yüz dalı, bu dalın yer ve yol kısıtını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B015 belirli kara yolu ve yerleşim konumlarını adlandırır; B003 ise arazi veya nesnenin yüksek, dış ya da üst yüzünü daha genel bir yüzey ilişkisiyle verir.","focus_only":"Bu dal kara yolu ile yerleşimin dış veya yüksek kesimini adlandırır.","gloss":"yer adı ile yüzey ayrımı","neighbor_only":"Komşu dal yükselmiş araziyi ve nesnenin dış ya da üst yüzünü genel olarak anlatır.","neighbor_ref":"root_000970/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal arazinin dışta veya yüksekte kalan bölümüne dokunur."}],"source_phrase_ar":"طريق الظهر (ayn;sihah;tahdhib)؛ سلكنا الظهر يريدون طريق البر (maqayis)؛ قريش الظواهر سموا بذلك لأنهم ينزلون ظاهر مكة (maqayis;sihah;tahdhib)؛ ظاهرة الجبل أعلاه وظاهرة كل شيء أعلاه (tahdhib)","source_summary":"Kaynaklar kara yolunu ve bir yerin dış ya da yüksek kesimini kaydeder; bu iki kullanım konumsal dışlık üzerinden ilişkilidir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"طريق البر المسمى طريق الظهر وظاهر البلد أو ظواهره وأعاليه الخارجة عن بطنه","what_is_not_ar":"ليس ظهر الجارحة ولا مجرد ظهور الشيء"},"support_links":[]},{"boundary":"Bu dal destekçi topluluğunu adlandırır; yardım eyleminin bütün biçimlerini veya tek bir yardımcıyı merkez almaz.","branch_kind":"bare","branch_ref":"root_000970/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"güç alınan destekçi topluluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yardımcılar ve yakın topluluk, kişiye toplu bir güç ve dayanak sağlar."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin yanında duran yardımcıları, yakınları veya toplu destekçileri adlandırmak için kullanılır.","boundary_detail":"Bu dal destekçi topluluğunu adlandırır; yardım eyleminin bütün biçimlerini veya tek bir yardımcıyı merkez almaz.","branch_image_ar":"الظهرة والظهراء من القوم","concept_gloss":"güç alınan destekçi topluluğu","definition":"Kişinin yanında duran, ona yardım eden ve kendilerinden güç aldığı kimselerden oluşan destekçi topluluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yardımcılar ve yakın topluluk, kişiye toplu bir güç ve dayanak sağlar."}],"identity_rationale":"Kaynak sözü kişinin yanında bulunan topluluğu, yardımcılarını ve güç aldığı destekçi çevresini adlandırır. Verilen dal çerçevesi toplu katılımcı sınırını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kişinin güç aldığı yardımcıları ve yakın topluluğu"}],"lexicalization_note":"Yalın sözlüksel biçim, kişinin güç aldığı yardımcılar ve yakın toplulukla sınırlı tanımlanır.","neighbor_coverage_note":"Adaylar değerlendirildi; genel yardım dalı, toplulukla sınırlı bu sözlüksel birimin sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B016 destek veren topluluğun adıdır; B006 ise destek ilişkisini kişi, eylem ve yardım alma biçimleriyle kapsayan daha geniş bir daldır.","focus_only":"Bu dal özellikle toplu destekçi çevresini adlandırır.","gloss":"destekçi çevresi ile yardım ilişkisi","neighbor_only":"Komşu dal yardım eylemini, yardımcı kişiyi ve yardım alma ilişkisini daha geniş kapsar.","neighbor_ref":"root_000970/B006","relation_type":"near_synonym","shared_zone":"İki dal da başkasının desteğiyle güç kazanma alanındadır."}],"source_phrase_ar":"جاء فلان في ظهرته وناهضته أي قومه (maqayis;sihah)؛ الظهرة ظهر الرجل وأنصاره (tahdhib)؛ الظهراء أعوان النبي (tahdhib)","source_summary":"Kaynaklar kişinin topluluğunu, yardımcılarını ve destekçilerini güç sağlayan bir çevre olarak birleştirir.","sources":["MQ","SI","TA"],"what_is_ar":"الظهرة بمعنى الأعوان والقوم والناصرين الذين يتقوى بهم المرء","what_is_not_ar":"ليس مطلق الظهير المفرد إلا من جهة العون"},"support_links":[]},{"boundary":"Topluluk ortası ile zaman aralığı ayrı kalıplardır; ikisi de yalnızca kendi yapısında geçerlidir.","branch_kind":"collocation","branch_ref":"root_000970/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"topluluk veya zaman sınırları arasında","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toplulukla kurulan kalıp, kişinin onların arasında ve ortasında bulunduğunu bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zamanla kurulan ayrı kalıp, iki gün veya daha geniş iki zaman sınırı arasındaki konumu bildirir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtta verilen topluluk ortası ve iki zaman arasındaki konum kalıplarında kullanılır.","boundary_detail":"Topluluk ortası ile zaman aralığı ayrı kalıplardır; ikisi de yalnızca kendi yapısında geçerlidir.","branch_image_ar":"بين ظهرانيهم","concept_gloss":"topluluk veya zaman sınırları arasında","definition":"Bir kalıpta kişinin bir topluluğun arasında veya ortasında bulunmasını, başka bir kalıpta ise iki gün, yıl ya da zaman diliminin arasında bulunmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toplulukla kurulan kalıp, kişinin onların arasında ve ortasında bulunduğunu bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Zamanla kurulan ayrı kalıp, iki gün veya daha geniş iki zaman sınırı arasındaki konumu bildirir."}],"identity_rationale":"Kaynak sözü iki ayrı kalıbı içerir: bir topluluğun arasında bulunma ve iki gün ya da zaman arasında olma. Geçici çerçeve yalnızca ilkini öne çıkarır; dal, iki kalıp birbirine karıştırılmadan ikisini de gösterecek biçimde yeniden kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"aralarında, topluluğun ortasında"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki gün veya iki zaman sınırı arasında"}],"lexicalization_note":"Tanım iki ayrı kalıba bağlıdır; topluluk içindeki konum ile günler arasındaki zaman konumu birbirine genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dal içindeki iki kalıp arasındaki ayrım, dış komşularla kurulacak ek karşılaştırmalardan daha belirleyicidir.","source_phrase_ar":"أنا بين ظهرانيهم وظهريهم (ayn)؛ نازل بين ظهريهم وظهرانيهم (sihah)؛ نزل فلان بين ظهرينا وظهرانينا وأظهرنا (tahdhib)؛ بين الظهرانين معناه في اليومين أو في الأيام (sihah;tahdhib)","source_summary":"Kaynaklar topluluk arasında bulunma kalıbını ve iki zaman sınırı arasında bulunma kalıbını ayrı kullanımlar olarak kaydeder.","sources":["AY","SI","TA"],"what_is_ar":"كون الشيء بين ظهري قوم أو ظهرانيهم أي في وسطهم أو بينهم","what_is_not_ar":"ليس النصرة ولا الإعراض وراء الظهر"},"support_links":[]},{"boundary":"Anlam yalnızca verilen kalıpta bir konuyu çok yönlü incelemektir; nesneyi bedenen çevirmek değildir.","branch_kind":"collocation","branch_ref":"root_000970/B018","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"bir konuyu her yönüyle incelemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konu tek yönden bırakılmaz; çeşitli yönleri çevrilip değerlendirilerek ayrıntılı biçimde düşünülür."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin veya düşüncenin farklı yönlerden ele alınıp ayrıntılı değerlendirildiği kalıp bağlamında kullanılır.","boundary_detail":"Anlam yalnızca verilen kalıpta bir konuyu çok yönlü incelemektir; nesneyi bedenen çevirmek değildir.","branch_image_ar":"قلب الأمر ظهرا لبطن","concept_gloss":"bir konuyu her yönüyle incelemek","definition":"Bir konuyu önünü arkasını çevirir gibi farklı yönlerinden tekrar tekrar ele alarak düşünmek ve incelemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konu tek yönden bırakılmaz; çeşitli yönleri çevrilip değerlendirilerek ayrıntılı biçimde düşünülür."}],"identity_rationale":"Kaynak sözü bir konuyu ön ve arka yönleriyle tekrar tekrar çevirme görüntüsünü verir; bu, konuyu farklı yönlerinden inceleyip düşünmek olarak anlaşılır. Dal çerçevesi bu inceleme işlemini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir konuyu evirip çevirerek her yönüyle incelemek"}],"lexicalization_note":"Çok yönlü inceleme anlamı belirtilen kalıba bağlı tutulur ve yalın kök anlamı sayılmaz.","neighbor_coverage_note":"Adaylar değerlendirildi; hiçbiri bu özel evirip çevirerek inceleme kalıbına gereksiz tekrar olmadan daha keskin bir sınır eklemedi.","source_phrase_ar":"قلبت الأمر ظهرا لبطن (ayn;tahdhib)","source_summary":"Kaynaklar kalıbı bir konuyu önlü arkalı çevirme görüntüsüyle verir; ortak anlam çok yönlü incelemedir.","sources":["AY","TA"],"what_is_ar":"تقليب الأمر ظهرا لبطن أو تدبيره من وجوهه","what_is_not_ar":"ليس الظهور بمعنى البروز ولا قلب الجسد"},"support_links":[]},{"boundary":"Bu dal bellekte tutma ve kitaba bakmadan söylemeyle sınırlıdır; genel öğrenme ya da açığa çıkma anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000970/B019","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"ezberleyip bellekten söylemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçerik dış bir metne başvurmadan yeniden üretilebilecek biçimde bellekte tutulur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bellekte tutma sonucu konuşma veya okuma sırasında içeriğin ezberden aktarılmasıyla görünür."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir metnin bellekte tutulduğu ve dış kaynağa bakılmadan okunduğu veya söylendiği bağlamlarda kullanılır.","boundary_detail":"Bu dal bellekte tutma ve kitaba bakmadan söylemeyle sınırlıdır; genel öğrenme ya da açığa çıkma anlamı değildir.","branch_image_ar":"ظهر الغيب والقلب","concept_gloss":"ezberleyip bellekten söylemek","definition":"Bir sözü veya metni bellekte sağlam biçimde tutmak ve kitaba bakmadan bellekten söylemek ya da okumaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçerik dış bir metne başvurmadan yeniden üretilebilecek biçimde bellekte tutulur."},{"facet_id":"F002","role":"associated_use","statement":"Bellekte tutma sonucu konuşma veya okuma sırasında içeriğin ezberden aktarılmasıyla görünür."}],"identity_rationale":"Kaynak sözü kitaba bakmadan bellekte tutmayı, bellekten söylemeyi veya okumayı ve bir metni bu amaçla ezberlemeyi anlatır. Dal çerçevesi bellekte saklama ile bellekten üretme aşamalarını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"kitaba bakmadan, ezberden"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"ezberlemek ve kitaba bakmadan okumak"}],"lexicalization_note":"Bellekten söyleme kalıbı ile ezberleme biçimi ayrı aşamalar olarak aynı bellek alanında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bellekte tutma ile bellekten söyleme aşamaları dal içinde açıkça ayrıldığı için ek komşu yayımlanmadı.","source_phrase_ar":"تكلمت بذلك عن ظهر غيب (ayn;tahdhib)؛ ظهر القلب حفظ من غير كتاب (ayn;tahdhib)؛ استظهر الشيء أي حفظه وقرأه ظاهرا (sihah)؛ حمل القرآن على ظهر لسانه (tahdhib)","source_summary":"Kaynaklar ezberlemeyi ve metne bakmadan bellekten söylemeyi aynı kalıcı bellek kullanımında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"عن ظهر غيب أو ظهر القلب والحفظ والاستظهار من غير كتاب","what_is_not_ar":"ليس الظهر العضو ولا الغيب نفسه"},"support_links":[]},{"boundary":"Anlam yalnızca iki giysi ya da zırhı üst üste getirme kalıbına bağlıdır; yardım etme anlamını içermez.","branch_kind":"collocation","branch_ref":"root_000970/B020","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"iki katmanı üst üste getirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki giyim ya da koruyucu katman eşleştirilir ve üst üste konur."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki giysi ya da zırhın birbirine denk getirilerek katmanlandığı özel kalıp için kullanılır.","boundary_detail":"Anlam yalnızca iki giysi ya da zırhı üst üste getirme kalıbına bağlıdır; yardım etme anlamını içermez.","branch_image_ar":"ظاهر بين الشيئين","concept_gloss":"iki katmanı üst üste getirmek","definition":"İki giysi veya iki zırhı birbirine denk getirerek birini diğerinin üzerine yerleştirmek ve katmanlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki giyim ya da koruyucu katman eşleştirilir ve üst üste konur."}],"identity_rationale":"Kaynak sözü iki giysi veya iki zırhı birbirine denk getirip birini ötekinin üzerine yerleştirmeyi anlatır. Dal çerçevesi katmanlama ve eşleştirme işlemlerini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"iki giysiyi veya iki zırhı üst üste getirmek"}],"lexicalization_note":"Katmanlama anlamı yalnızca iki giysi veya zırh arasında kurulan belirtilen kalıpla sınırlandırılır.","neighbor_coverage_note":"Adayların tümü değerlendirildi; iki katmanı eşleştirme işlemi yeterince özel olduğundan ek karşılaştırma yayımlanmadı.","source_phrase_ar":"ظاهر بين ثوبين أي طارق بينهما وطابق (sihah)؛ ظاهر فلان بين ثوبين وبين درعين إذا طابق بينهما (tahdhib)","source_summary":"Kaynaklar iki giysi veya iki zırhın eşleştirilip üst üste konması işleminde birleşir.","sources":["SI","TA"],"what_is_ar":"المظاهرة بين ثوبين أو درعين بمعنى المطابقة ووضع أحدهما على الآخر","what_is_not_ar":"ليس المعاونة إلا بلفظ ظاهر فلان فلانا"},"support_links":[]},{"boundary":"Bu dal ihtiyaç için hazır tutmayı anlatır; bir şeyi arkaya atıp unutma anlamının karşıt yönündedir.","branch_kind":"bare","branch_ref":"root_000970/B021","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"yedek hazırlayıp güvence sağlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi olası ihtiyaca karşı yedek bulundurur ve böylece durumunu daha güvenli kılar."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gerektiğinde kullanılmak üzere fazladan deve hazır tutmak bu önlemin somut örneğidir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gelecekteki ihtiyaç için fazladan araç bulundurma ve bununla önlem alma bağlamlarında kullanılır.","boundary_detail":"Bu dal ihtiyaç için hazır tutmayı anlatır; bir şeyi arkaya atıp unutma anlamının karşıt yönündedir.","branch_image_ar":"الاحتياط والاستيثاق","concept_gloss":"yedek hazırlayıp güvence sağlamak","definition":"Gelecekte doğabilecek ihtiyaç için fazladan bir araç veya yedek hazırlayarak önlem almak ve kendine güvence sağlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi olası ihtiyaca karşı yedek bulundurur ve böylece durumunu daha güvenli kılar."},{"facet_id":"F002","role":"example","statement":"Gerektiğinde kullanılmak üzere fazladan deve hazır tutmak bu önlemin somut örneğidir."}],"identity_rationale":"Kaynak sözü gelecekteki ihtiyaca karşı yedek araç bulundurmayı, böylece önlem almayı ve güvence sağlamayı anlatır. Dal çerçevesi hazırlık işlemi ile güvence sonucunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gerektiğinde kullanılmak üzere hazır tutulan deve"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"yedek hazırlayarak önlem almak ve güvence sağlamak"}],"lexicalization_note":"Yalın dal genel önlem ve güvence çekirdeğini tanımlar; yedek deve bunun somut gerçekleşmesidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ihmal karşıtlığı ve somut yedek hayvan, dalın işlem sınırını en iyi gösteren iki komşudur.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B021 eldeki şeyi koruyup yedeğe dönüştürür; B012 ise onu ilgi alanının dışına atıp unutulmaya bırakır.","focus_only":"Bu dal şeyi ihtiyaç için hazır tutarak güvence oluşturur.","gloss":"hazır tutma ile ihmal","neighbor_only":"Komşu dal şeyi geriye atarak unutur ve önemsemez.","neighbor_ref":"root_000970/B012","relation_type":"polarity_pair","shared_zone":"İki dal bir şeyin gelecekteki ihtiyaç karşısında nasıl konumlandırıldığını anlatır."},{"boundary_match":"partial","distinction":"B021 hazırlık tutumunu ve sonucunu, B005 ise taşıma hayvanını ve yedek devenin kendisini merkez alır.","focus_only":"Bu dal genel önlem alma ve güvence sağlama işlemini merkez alır.","gloss":"önlem ile yedek hayvan","neighbor_only":"Komşu dal yük hayvanlarını ve somut yedek deveyi adlandırır.","neighbor_ref":"root_000970/B005","relation_type":"near_neighbor","shared_zone":"Yedek deve olası ihtiyaç için hazır bulundurulan bir güvence aracıdır."}],"source_phrase_ar":"البعير الظهري العدة للحاجة (sihah;tahdhib)؛ الاستظهار في كلامهم الاحتياط والاستيثاق (tahdhib)؛ استظهر ببعيرين ظهريين محتاطا بهما (tahdhib)","source_summary":"Kaynaklar yedek deve hazırlamayı genel önlem alma ve güvence sağlama düşüncesinin somut uygulaması olarak verir.","sources":["SI","TA"],"what_is_ar":"الاستظهار بمعنى الاحتياط والاستيثاق واتخاذ عدة زائدة للحاجة","what_is_not_ar":"ليس الإهمال بجعله وراء الظهر"},"support_links":[]},{"boundary":"Bu dal karşılıklı sırt çevirme ve uzaklaşmadır; aynı biçimin yardımlaşma anlamıyla karıştırılmaz.","branch_kind":"bare","branch_ref":"root_000970/B022","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"birbirine sırt çevirip uzaklaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Her taraf ötekine sırtını döner ve karşılıklı yakınlık yerine ayrışma ortaya çıkar."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarafların karşılıklı olarak yüz çevirdiği ve ilişkilerini gevşettiği ya da kestiği bağlamlarda kullanılır.","boundary_detail":"Bu dal karşılıklı sırt çevirme ve uzaklaşmadır; aynı biçimin yardımlaşma anlamıyla karıştırılmaz.","branch_image_ar":"التدابر بالظهور","concept_gloss":"birbirine sırt çevirip uzaklaşmak","definition":"İki veya daha çok tarafın birbirine sırt çevirerek karşılıklı biçimde uzaklaşması, ilişkiyi kesmesi veya birbirinden yüz çevirmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Her taraf ötekine sırtını döner ve karşılıklı yakınlık yerine ayrışma ortaya çıkar."}],"identity_rationale":"Kaynak sözü tarafların birbirine sırtını dönerek karşılıklı uzaklaşmasını ve ilişkiyi kesmesini anlatır. Dal çerçevesi katılımcıların karşılıklılığını ve ayrışma sonucunu doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"birbirine sırt çevirip uzaklaşmak"}],"lexicalization_note":"Yalın dal karşılıklı uzaklaşma çekirdeğiyle tanımlanır ve destekleşme kullanımı dışarıda tutulur.","neighbor_coverage_note":"Adaylar değerlendirildi; biçimsel olarak kolay karışan yardımlaşma dalı, karşılıklı uzaklaşma sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"B022 ilişkiyi uzaklaşma yönünde çözer; B006 ise aynı katılımcıları destek ve dayanışma yönünde birleştirir.","focus_only":"Bu dal tarafların karşılıklı biçimde uzaklaşıp ilişkiyi kesmesini anlatır.","gloss":"sırt çevirme ile yardımlaşma","neighbor_only":"Komşu dal tarafların birbirine yardım edip güç vermesini anlatır.","neighbor_ref":"root_000970/B006","relation_type":"polarity_pair","shared_zone":"İki dal tarafların birbirine yönelişini ve aralarındaki toplumsal bağı düzenler."}],"source_phrase_ar":"تظاهر القوم إذا تدابروا (maqayis;sihah)؛ كل واحد منهما أدبر عن صاحبه وجعل ظهره إليه (maqayis)","source_summary":"Kaynaklar tarafların birbirine sırtını dönmesini karşılıklı uzaklaşma ve ilişkiyi kesme olarak açıklar.","sources":["MQ","SI"],"what_is_ar":"تظاهر القوم بمعنى تدابروا وولى كل واحد ظهره إلى صاحبه","what_is_not_ar":"ليس التظاهر بمعنى التعاون"},"support_links":[]},{"boundary":"İlk kalıp karşılıksız başlangıcı, ikinci kalıp ihtiyaç fazlası bolluğu bildirir; ikisi kendi yapılarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000970/B023","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"karşılıksız veya artandan vermek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Verme eylemi önceki bir karşılığın ödenmesi olarak değil, verenin başlangıcıyla gerçekleşir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı kalıp, verilecek şeyin kişinin geçim ihtiyacından artan bolluktan gelmesini bildirir."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca karşılık beklememe ya da geçim ihtiyacından artan bolluk koşulunu bildiren iki kanıtlı kalıpta kullanılır.","boundary_detail":"İlk kalıp karşılıksız başlangıcı, ikinci kalıp ihtiyaç fazlası bolluğu bildirir; ikisi kendi yapılarıyla sınırlıdır.","branch_image_ar":"عن ظهر يد وغنى","concept_gloss":"karşılıksız veya artandan vermek","definition":"Bir kalıpta karşılık beklemeden ve kendiliğinden vermeyi, diğerinde ise geçim gereklerinden artan bolluktan vermeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Verme eylemi önceki bir karşılığın ödenmesi olarak değil, verenin başlangıcıyla gerçekleşir."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı kalıp, verilecek şeyin kişinin geçim ihtiyacından artan bolluktan gelmesini bildirir."}],"identity_rationale":"Kaynak sözü iki ayrı kalıp verir: karşılık beklemeden başlayan verme ve geçim gereklerinden artan bolluktan verme. Dal çerçevesi ikisini doğru anar, ancak başlangıç biçimi ile ekonomik kaynak birbirine karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"karşılık beklemeden, kendiliğinden vermek"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"geçim gereklerinden artan bolluktan vermek"}],"lexicalization_note":"Tanım iki ayrı kalıba bağlıdır; karşılık beklememe ile ihtiyaç fazlasından verme ayrı koşullar olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; iki kalıbın kendi koşullarını açıklamak, dış komşularla ek karşılaştırmadan daha yararlı bulundu.","source_phrase_ar":"عن ظهر يد معناه ابتداء من غير مكافأة (tahdhib)؛ ما كان عن ظهر غنى عن فضل عيال (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, karşılık beklemeden başlatılan verme ile geçim ihtiyacından artan bolluktan vermeyi iki ayrı kalıpta bildirir."}],"source_summary":"Bu dal için kaynaklar arası ortak bir özet kurulamaz; kanıt tek bir sözlük kaydına dayanır.","sources":["TA"],"what_is_ar":"عن ظهر يد أو ظهر غنى بمعنى ابتداء بلا مكافأة أو من فضل وسعة","what_is_not_ar":"ليس ظهر اليد الجارحة مجردا"},"support_links":[]},{"boundary":"Bu dal belirtilen kalıpta övünmeyi anlatır; bir rakibi yenme veya yalnızca görünür olma anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000970/B024","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","surface_ar":"ظَهْرَ"}],"gloss":"bir şeyle övünmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi sahip olduğu veya ilişkilendirildiği bir şeyi övünç dayanağı yapar."}}],"root_ar":"ظ ه ر","root_id":"root_000970","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlık veya niteliğin başkalarına karşı övünç ve üstünlük göstergesi yapıldığı kalıpta kullanılır.","boundary_detail":"Bu dal belirtilen kalıpta övünmeyi anlatır; bir rakibi yenme veya yalnızca görünür olma anlamı değildir.","branch_image_ar":"الافتخار به","concept_gloss":"bir şeyle övünmek","definition":"Bir şeyi kendi üstünlüğünün veya değerinin göstergesi sayarak onunla başkalarına karşı övünmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi sahip olduğu veya ilişkilendirildiği bir şeyi övünç dayanağı yapar."}],"identity_rationale":"Kaynak sözü bir şeyi kişinin övünme dayanağı yapmasını ve onunla başkalarına karşı övünmesini açıkça bildirir. Verilen dal çerçevesi bu tutum ve araç ilişkisini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"bir şeyle övünmek ve onu övünç dayanağı yapmak"}],"lexicalization_note":"Övünme anlamı yalnızca bir şeyi övünç dayanağı yapan belirtilen kalıba bağlı tutulur.","neighbor_coverage_note":"Adaylar değerlendirildi; üstün gelme dalı, övünme tutumu ile gerçek üstünlük arasındaki sınırı en açık gösteren komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"B024 kişinin bir şeyle övünme tutumudur; B007 ise güç, başarı veya konum bakımından fiilen üstte olmayı bildirir.","focus_only":"Bu dal bir şeyi övünç dayanağı yaparak başkalarına karşı övünmeyi anlatır.","gloss":"övünme ile üstün gelme","neighbor_only":"Komşu dal bir hedef üzerinde gerçekten üstünlük kurmayı veya onun üstüne çıkmayı anlatır.","neighbor_ref":"root_000970/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal başkalarına göre yüksek ya da üstün görünme düşüncesine yaklaşabilir."}],"source_phrase_ar":"ظهرت به أي افتخرت به (tahdhib)؛ واظهر ببزته أي افخر به على غيره (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kayıt, bir şeyi başkalarına karşı övünme ve üstünlük gösterme dayanağı yapma anlamını bildirir."}],"source_summary":"Bu dal için kaynaklar arası ortak bir özet kurulamaz; kanıt tek bir sözlük kaydına dayanır.","sources":["TA"],"what_is_ar":"ظهر بالشيء أو ظهر به بمعنى افتخر به وجعله وجها للفخر","what_is_not_ar":"ليس الظهور بمعنى الانكشاف فقط ولا الغلبة على الخصم"},"support_links":[]},{"boundary":"Fiziksel sökme çekirdeği ile bağlayıcı sözü geçersiz kılma ve karşı savla çürütme uzantıları korunmalı; ses, bitki ve yolculuk yorgunluğu anlamları bu dala katılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001543/B001","candidate_links":[{"candidate_id":"cand_6443dda8797836b7e903","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"kurulu bütünü çözme, geçersiz kılma veya karşı savla çürütme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İp, örgü, yapı veya düğüm gibi önceden bir araya getirilmiş bir bütünü çözme, sökme ya da bozma."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ant, sözleşme veya pekiştirilmiş söz gibi bağlayıcı bir düzenlemeyi bozup geçersiz kılma."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir sözün ya da şiirin ileri sürdüğü anlamı karşı bir söz veya şiirle çürütme."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Sökülmüş ip, kumaş veya yapı parçasını; ayrıca ipekli dokumayı sökme işini ve bu işi yapan kişiyi adlandırma."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel olarak kurulmuş bütünlerde, bağlayıcı sözlerde ve önceki bir savı boşa çıkaran karşı sözlerde dalın çekirdeğini birlikte karşılar.","boundary_detail":"Fiziksel sökme çekirdeği ile bağlayıcı sözü geçersiz kılma ve karşı savla çürütme uzantıları korunmalı; ses, bitki ve yolculuk yorgunluğu anlamları bu dala katılmamalıdır.","branch_image_ar":"حل المبرم وإبطال بنائه","concept_gloss":"kurulu bütünü çözme, geçersiz kılma veya karşı savla çürütme","contextual_glosses":[{"applicability":"İp, örgü, düğüm ve yapı gibi somut olarak kurulmuş bütünlerin parçalara ayrılması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bağlayıcı sözü geçersiz kılma ve bir savı karşı sözle çürütme uzantılarını karşılamaz.","preserves":"Somut bir bütünün kuruluşunu tersine çevirerek parçalarını ayırma anlamını korur."},"facet_ids":["F001"],"text":"sökmek","usage_role":"contextual"},{"applicability":"Ant, sözleşme veya pekiştirilmiş bir sözün bağlayıcılığını kaldırma bağlamında kullanılabilir.","error_profile":{"adds":"Genel kullanımda her türlü zarar verme veya işleyişi aksatma anlamını da taşıyabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Önceden kurulmuş bağlayıcı düzenin geçerliliğini ortadan kaldırma sonucunu korur."},"facet_ids":["F002"],"text":"bozmak","usage_role":"contextual"},{"applicability":"Bir sözün, savın veya şiirin ileri sürdüğü anlamı karşı sözle geçersiz gösterme bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut sökme ile bağlayıcı söz veya sözleşmeyi bozma kullanımlarını içermez.","preserves":"Önceki bir söylemi karşı söylemle boşa çıkarma ilişkisini tam olarak korur."},"facet_ids":["F003"],"text":"çürütmek","usage_role":"contextual"}],"definition":"Önceden örülmüş, bağlanmış veya kurulmuş bir bütünü parçalarına ayırarak çözmek ya da düzenini bozmak; buna benzetilerek bağlayıcı bir sözü geçersiz kılmak veya bir savı karşı sözle çürütmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İp, örgü, yapı veya düğüm gibi önceden bir araya getirilmiş bir bütünü çözme, sökme ya da bozma."},{"facet_id":"F002","role":"extension","statement":"Ant, sözleşme veya pekiştirilmiş söz gibi bağlayıcı bir düzenlemeyi bozup geçersiz kılma."},{"facet_id":"F003","role":"associated_use","statement":"Bir sözün ya da şiirin ileri sürdüğü anlamı karşı bir söz veya şiirle çürütme."},{"facet_id":"F004","role":"extension","statement":"Sökülmüş ip, kumaş veya yapı parçasını; ayrıca ipekli dokumayı sökme işini ve bu işi yapan kişiyi adlandırma."}],"identity_rationale":"Kaynak ifadesi, önceden örülmüş ya da kurulmuş bir bütünü çözme çekirdeğini; yapı, ip ve bağlayıcı sözlerin bozulmasına, ayrıca söz veya şiirin karşı sözle çürütülmesine uzanan kullanımlarla birlikte açıkça destekliyor.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kurulmuş bir bütünü çözme veya sökme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"antlaşmayı ya da bağlayıcı sözü bozma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"pekiştirilmiş yeminleri bozma"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sökülmüş yapı, ip veya kumaş parçası"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sökülmüş kıl ipi veya ipekli dokuma sökme işi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ipekli dokuma söken usta"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"söz veya şiirle karşı çıkıp çürütme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"önceki bir şiiri veya sözü çürüten karşı şiir ya da yazı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"aynı durumda birlikte doğru olamayan iki önerme"}],"lexicalization_note":"Tanım, yalın çözme ve sökme çekirdeğini verirken bağlayıcı söz ve yeminlerin bozulmasını ve şiirsel karşı çıkışı yalnızca bunlara özgü kullanımlar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel iptal ve yapı yıkımı, çekirdeğin sınırını en iyi gösteren iki karşılaştırma olarak seçildi. Öteki adaylar ya yalnızca aynı senaryoya katılıyor ya da bu iki ayrımı tekrarlıyordu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, var olan bir kuruluşu tersine çevirme tasarımını korur; komşu ise nesnenin daha önce kurulmuş olmasını gerektirmeyen daha genel bir iptal ve ortadan kaldırma alanına sahiptir.","focus_only":"Önceden örülmüş, bağlanmış veya kurulmuş bir düzenin çözülmesi ve bunun söz ya da şiire aktarılması.","gloss":"kurulmuş olanı çözme ile genel iptal etme","neighbor_only":"Önceden kurulmuş olma şartı aranmadan herhangi bir şeyi geçersizleştirme, bozma veya ortadan kaldırma.","neighbor_ref":"root_000127/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin geçerliliğini, bütünlüğünü veya işlerliğini ortadan kaldırabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği kurulmuş bütünü çözme olduğu için ipten söze kadar uzanır; komşu dalın çekirdeği ise yapının yıkılması veya çökmesidir.","focus_only":"İp ve düğümü çözmenin yanı sıra antlaşma, söz ve sav gibi soyut kuruluşları da bozabilir.","gloss":"kuruluşu çözme ile yapıyı yıkma","neighbor_only":"Bina, duvar, ev veya kuyu kenarı gibi yapıların yıkılması ve çökmesiyle sınırlı bir yapı alanına odaklanır.","neighbor_ref":"root_001581/B001","relation_type":"near_neighbor","shared_zone":"Somut bir yapının önceki bütünlüğünü kaybetmesi iki dalın kesişme alanıdır."}],"source_phrase_ar":"يدل على نكث شيء؛ نقضت الحبل والبناء؛ نقض العهد؛ المناقضة في الشعر (maqayis)؛ إفساد ما أبرمت من حبل أو بناء؛ النقاض الذي ينقض الدمقس (ayn;tahdhib)؛ ما نقض من ثوب صوف أو إبريسيم فهو نقض ونكث (tahdhib)؛ نقض البناء والحبل والعهد؛ المناقضة في القول (sihah)؛ نقضت البناء والحبل والعقد؛ استعير نقض العهد؛ لا تنقضوا الأيمان؛ المناقضة في الكلام والشعر (mufradat)","source_summary":"Kaynakların ortak çekirdeği, kurulmuş veya örülmüş bir şeyi çözerek eski bütünlüğünü bozmadır. Aynı tasarım bağlayıcı sözlerin geçersiz kılınmasına ve söz ya da şiirde karşı savla çürütmeye aktarılır; sökülmüş malzeme ile sökme işi de bu çekirdeğe bağlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إفساد المبرم أو حله: الحبل والبناء والعقد، ونقض العهد واليمين، والمناقضة في القول أو الشعر، والمنقوض من الحبل أو الثوب.","what_is_not_ar":"ليس صوت المفاصل أو زجر الدواب، ولا هزال البعير، ولا انتقاض الجرح بعد البرء."},"support_links":["sup_e63c0d8bc95eae738acf"]},{"boundary":"Yalnızca genel zayıflık değil, yolculuğun tükettiği deve veya dişi deve durumu korunmalıdır.","branch_kind":"bare","branch_ref":"root_001543/B002","candidate_links":[{"candidate_id":"cand_cd329fee262b4b69404a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"yolculukların gücünü tükettiği deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolculukların bir deve veya dişi devenin gücünü tüketip onu zayıf ve bitkin bırakması."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolculuk yüzünden zayıflamış erkek veya dişi deve için dalın nedeni, katılımcısı ve sonucunu birlikte verir.","boundary_detail":"Yalnızca genel zayıflık değil, yolculuğun tükettiği deve veya dişi deve durumu korunmalıdır.","branch_image_ar":"بعير أنهكته الأسفار","concept_gloss":"yolculukların gücünü tükettiği deve","contextual_glosses":[{"applicability":"Bir devenin yolculuklar sonucunda gücünü yitirdiğini akıcı biçimde açıklayan bağlamlarda uygundur.","error_profile":{"adds":"Uzun sözcüğü, kaynakta açıkça belirtilmeyen bir süre ölçüsü ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Yolculuk nedeniyle devenin gücünü yitirip zayıflaması anlamını korur."},"facet_ids":["F001"],"text":"uzun yolların zayıf düşürdüğü deve","usage_role":"explanatory"}],"definition":"Deve veya dişi devenin yolculuklar yüzünden gücünü yitirerek zayıf ve bitkin duruma düşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolculukların bir deve veya dişi devenin gücünü tüketip onu zayıf ve bitkin bırakması."}],"identity_rationale":"Kaynak ifadesi, deve veya dişi devenin yolculuklar yüzünden gücünü yitirip zayıflamasını dalın ayırt edici anlamı olarak ortak biçimde veriyor.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yolculukların güçten düşürdüğü deve"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yolculukların güçten düşürdüğü dişi deve veya binek hayvanı"}],"lexicalization_note":"Tanım yalın dalı, yolculukların gücünü tükettiği deve durumu olarak sınırlar ve başka yorgunluk ya da zayıflık türlerini içine almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yol bitkinliği ve yorgunluktan geride kalan binek, neden ile sonuç sınırını en açık gösteren karşılaştırmalardır. Güçlü binek ve yolculuğa hazır deve gibi öteki adaylar yalnızca aynı alanı paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hayvan türünü deve olarak sabitler; komşu dal ise yol yorgunluğu ve zayıflığını daha genel bir katılımcı alanında anlatır.","focus_only":"Yolculuğun zayıflattığı katılımcıyı özellikle deve veya dişi deve olarak sınırlar.","gloss":"yolculuktan zayıflamış deve ile genel yol bitkinliği","neighbor_only":"Yürüme ve yolculuktan doğan yorgunluk, bitkinlik ve zayıflığı insan ya da başka canlılara daha genel biçimde uygular.","neighbor_ref":"root_000944/B003","relation_type":"near_synonym","shared_zone":"Yolculuk veya ilerleme sonucunda güç kaybı ve zayıflama iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Odak dal kalıcı görünen zayıflık ve tükenmişliği adlandırır; komşu dal ise bu güç kaybının geride kalma ve hareketsizlik biçimindeki yol davranışını adlandırır.","focus_only":"Yolculukların bedeni zayıflatıp gücü tüketmesi sonucu ortaya çıkan deve niteliğidir.","gloss":"yolculuktan zayıflama ile yorgunluktan geride kalma","neighbor_only":"Binek hayvanının yorgunluktan geride kalması, sürüye yetişememesi ve hareket edememesi davranışsal sonucunu öne çıkarır.","neighbor_ref":"root_000520/B006","relation_type":"near_neighbor","shared_zone":"Yolculukta binek hayvanının gücünü kaybetmesi ortak senaryodur."}],"source_phrase_ar":"البعير المهزول نقض كأن الأسفار نقضته (maqayis)؛ الجمل والناقة اللذان هزلتهما الأسفار (ayn;tahdhib)؛ البعير الذي أضناه السفر وكذلك الناقة (sihah)؛ البعير المهزول (mufradat)","source_summary":"Kaynaklar, devenin yolculuklar nedeniyle gücünü kaybedip zayıflamasında birleşir; bazı ifadeler hem erkek hem dişi deveyi açıkça kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وصف الجمل أو الناقة إذا أضناهما السفر وأذهب قوتهما، وما يجمع على أنقاض.","what_is_not_ar":"ليس كل هزال مطلق، ولا نقض الحبل أو العهد، ولا صوت الظهر أو المفاصل."},"support_links":["sup_52b4c2e3a56e5271f92b"]},{"boundary":"Genel bir toprak çatlağı değil, yer mantarının çıkışına bağlı açılma ve bunun belirlediği yüzey anlatılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001543/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"yer mantarı çıkışıyla yarılan toprak yüzü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yer mantarının çıkışı sırasında toprak yüzünün çatlayıp açılması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yer mantarının çıkışıyla açılmış olan toprak yüzünü veya yeri adlandırma."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yer mantarının toprağı açma olayını hem de bu olayla belirlenen yüzeyi birlikte temsil eder.","boundary_detail":"Genel bir toprak çatlağı değil, yer mantarının çıkışına bağlı açılma ve bunun belirlediği yüzey anlatılmalıdır.","branch_image_ar":"تفتح الأرض عن الكمأة","concept_gloss":"yer mantarı çıkışıyla yarılan toprak yüzü","contextual_glosses":[{"applicability":"Toprağın açılma sürecini anlatan cümlelerde, yer adından çok olayın kendisini öne çıkarır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Açılmanın görüldüğü toprak parçasını adlandıran sonuç anlamını içermez.","preserves":"Yer mantarının çıkışı sırasında toprağın çatlayıp açılması olayını korur."},"facet_ids":["F001"],"text":"yer mantarları çıkarken toprağın yarılması","usage_role":"explanatory"}],"definition":"Yer mantarı topraktan çıkarken yer yüzünün çatlayıp açılması ve bu açılmanın görüldüğü toprak parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yer mantarının çıkışı sırasında toprak yüzünün çatlayıp açılması."},{"facet_id":"F002","role":"extension","statement":"Yer mantarının çıkışıyla açılmış olan toprak yüzünü veya yeri adlandırma."}],"identity_rationale":"Kaynak ifadesi hem yer mantarı çıkarken toprağın çatlayıp açılmasını hem de bu açılmanın görüldüğü toprak yüzünü veya yeri destekliyor.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yer mantarının çıkışıyla yarılmış toprak yüzü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"toprağın yer mantarı çıkarken yarılıp açılması"}],"lexicalization_note":"Tanım, yer mantarı çıkışının belirlediği yalın yer adını bu olaya özgü toprak açılması anlatımından ayırır; genel çatlama anlamına genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yarılma dalı süreç sınırını, mantar adı dalı ise katılımcı ile yer arasındaki ayrımı gösterdiği için seçildi. Öteki çatlama ve bitki adayları bu karşıtlıkları yinelemektedir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda açılmanın nedeni yer mantarının çıkışıdır ve sonuçtaki yer de adlandırılabilir; komşu dal ise nesne ve neden bakımından geniş bir yarılma alanıdır.","focus_only":"Toprağın açılmasını yer mantarının çıkışına bağlar ve açılan yüzeyi de adlandırır.","gloss":"yer mantarı için açılan toprak ile genel yarılma","neighbor_only":"Deri, dağ, yer, diş veya tan aydınlığı gibi çok farklı nesne ve olaylardaki yarılma ve açılmayı kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_synonym","shared_zone":"Toprak yüzünün çatlayıp açılması iki dalın ortak alanıdır."},{"boundary_match":"thematic_only","distinction":"Odak dal mantarın kendisini değil toprağın açılmasını ve açılan yeri anlatır; komşu dal ise doğrudan mantar türünü adlandırır.","focus_only":"Yer mantarının çıkarken yardığı toprak yüzünü ve yarılma olayını anlatır.","gloss":"yer mantarının çıkış izi ile mantarın kendisi","neighbor_only":"Belirli bir yer mantarı türünü veya onun tek örneğini adlandırır.","neighbor_ref":"root_001165/B008","relation_type":"thematic","shared_zone":"İki dal aynı yer mantarı çıkışı senaryosunda yer alır."}],"source_phrase_ar":"النقض منتقض الكمأة من الأرض (maqayis;ayn)؛ الموضع الذي ينتقض عن الكمأة؛ تنقضت الأرض عن الكمأة أي تفطرت (sihah)؛ نقضت وجه الأرض نقضا فانتقضت الأرض (tahdhib)؛ منتقض الأرض من الكمأة نقض (mufradat)","source_summary":"Kaynaklar, yer mantarının çıkışıyla toprak yüzünün yarılıp açılmasını ve bu olayın belirlediği yeri aynı anlam alanında verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه موضع الكمأة أو وجه الأرض حين يتفطر وينتفض لخروج الكمأة.","what_is_not_ar":"ليس انتقاض الجرح بعد البرء، ولا هدم البناء، ولا صوت المفاصل."},"support_links":[]},{"boundary":"İlk kez oluşan yara veya düzensizlik değil, iyileşme ya da toparlanma sonrasında eski bozuk durumun geri dönmesi anlatılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001543/B004","candidate_links":[{"candidate_id":"cand_1815138d94a3d37806a7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"iyileşme veya toparlanma sonrası yeniden bozulma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İyileşmiş yara veya kapanmış çıbanın yeniden açılması ya da bozulması."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toparlanıp düzene girmiş bir işin veya sınır düzeninin yeniden bozulması."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yara ve çıbanın yeniden açılmasını da düzene girmiş iş veya sınırın yeniden aksamasını da ortak geri dönüş koşuluyla kapsar.","boundary_detail":"İlk kez oluşan yara veya düzensizlik değil, iyileşme ya da toparlanma sonrasında eski bozuk durumun geri dönmesi anlatılmalıdır.","branch_image_ar":"عودة الشيء بعد التئامه إلى الانفتاح","concept_gloss":"iyileşme veya toparlanma sonrası yeniden bozulma","contextual_glosses":[{"applicability":"Önceden iyileşmiş bir yara veya kapanmış bir çıbanın tekrar açılması bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toparlanmış iş veya sınır düzeninin yeniden bozulması uzantısını içermez.","preserves":"İyileşmeden sonra bedensel yaranın yeniden açılması koşulunu korur."},"facet_ids":["F001"],"text":"yaranın yeniden açılması","usage_role":"contextual"},{"applicability":"Düzene girmiş bir işin veya güvenliği toparlanmış bir sınır bölgesinin tekrar bozulması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yara veya çıbanın iyileşme sonrasında yeniden açılması anlamını içermez.","preserves":"Toparlanmış bir düzenin yeniden bozulması ve işlerliğini kaybetmesi anlamını korur."},"facet_ids":["F002"],"text":"yeniden aksamaya başlamak","usage_role":"contextual"}],"definition":"İyileşmiş bir yara veya kapanmış bir çıbanın yeniden açılıp bozulması; buna benzetilerek toparlanmış bir işin ya da sınır düzeninin yeniden aksamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İyileşmiş yara veya kapanmış çıbanın yeniden açılması ya da bozulması."},{"facet_id":"F002","role":"extension","statement":"Toparlanıp düzene girmiş bir işin veya sınır düzeninin yeniden bozulması."}],"identity_rationale":"Kaynak ifadesi, yaranın iyileşmesinden veya bir işin ve sınır düzeninin toparlanmasından sonra yeniden açılma ya da bozulma koşulunu açıkça koruyor.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"iyileşme veya toparlanma sonrası yeniden bozulma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kapanmış çıbanın yeniden açılması"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"iyileşmiş yaranın yeniden açılıp bozulması"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"toparlanmış işin veya sınır düzeninin yeniden bozulması"}],"lexicalization_note":"Tanım, yalın geri bozulma adını yara, iş ve sınır düzenine özgü anlatımlardan ayırır; ilk bozulma veya genel yıkım anlamına genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaranın özel yinelemesi ile kökün genel çözme dalı, zorunlu önceki iyileşme koşulunu en iyi görünür kıldı. Tedavi, koruma ve ilk bozulma adayları daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sağlıktan düzene uzanan genel bir toparlanma sonrası bozulma örüntüsüdür; komşu dal ise yara ve damardaki gizli bozuklukla sınırlı, daha özel bir yinelemedir.","focus_only":"Bedensel yaranın yanı sıra toparlanmış işin veya sınır düzeninin yeniden bozulmasını da kapsar.","gloss":"genel geri bozulma ile içten bozuk yaranın yinelemesi","neighbor_only":"İçten bozuk biçimde kapanmış yara ya da yatıştıktan sonra yeniden etkinleşen damar durumunu özellikle belirtir.","neighbor_ref":"root_001071/B003","relation_type":"near_synonym","shared_zone":"Yara iyileşmiş veya yatışmış göründükten sonra bozukluğun geri dönmesi ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal çevrimsel bir geri dönüş içerir: durum düzelmişken yeniden bozulur. Komşu dal ise kurulmuş bütünün çözülmesini anlatır ve arada bir iyileşme aşaması gerektirmez.","focus_only":"Önce iyileşme veya toparlanma, ardından bozukluğun geri dönmesi aşamalarını zorunlu kılar.","gloss":"yeniden bozulma ile kurulmuş olanı bozma","neighbor_only":"Bir ipi, yapıyı, antlaşmayı veya savı daha önce iyileşmiş olma şartı olmadan çözme ya da bozmadır.","neighbor_ref":"root_001543/B001","relation_type":"near_neighbor","shared_zone":"Önceden bütün veya düzenli olan bir durumun bütünlüğünü kaybetmesi ortak alandır."}],"source_phrase_ar":"انتقضت القرحة (maqayis;mufradat)؛ الانتقاض أن يعود الجرح بعد البرء وكذلك انتقاض الأمور والثغور (ayn)؛ الانتقاض الانتكاث (sihah)؛ انتقض الجرح بعد البرء؛ انتقض الأمر بعد التئامه؛ انتقض أمر الثغر (tahdhib)","source_summary":"Ortak anlam, daha önce iyileşmiş veya toparlanmış bir durumun yeniden açılması ya da bozulmasıdır. Bu geri dönüş hem yara ve çıban için hem de düzen kazanmış işler ve sınır bölgeleri için verilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه انتقاض القرحة أو الجرح بعد البرء، وانتقاض الأمر أو الثغر بعد التئامه واستقراره.","what_is_not_ar":"ليس خروج الكمأة من الأرض، ولا مجرد هدم البناء ابتداء، ولا صوت العظام."},"support_links":["sup_c44bbb58772171dd5594"]},{"boundary":"Buradaki ses baskı, eklem hareketi veya yük taşıyan nesneden doğar; hayvan ötüşleri ve hayvan yönlendiren dil sesleri bu daldan ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001543/B005","candidate_links":[{"candidate_id":"cand_3ea049afe073cca537db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"baskı altındaki eklem veya yük aracının gıcırtısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eklem, parmak, kaburga veya kemiğin hareket ya da baskı altında gıcırdaması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ağır yükün sırta baskı yaparak ondan duyulur bir gıcırtı çıkarması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çekme kupası, yük taşıma düzeneği veya eyer gibi araçların çıkardığı benzer sesi adlandırma."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eklem ve kemik seslerini, yükün sırttan çıkardığı sesi ve yük taşıma araçlarının benzer gıcırtısını kapsar.","boundary_detail":"Buradaki ses baskı, eklem hareketi veya yük taşıyan nesneden doğar; hayvan ötüşleri ve hayvan yönlendiren dil sesleri bu daldan ayrıdır.","branch_image_ar":"صرير المفاصل والظهر تحت الثقل","concept_gloss":"baskı altındaki eklem veya yük aracının gıcırtısı","contextual_glosses":[{"applicability":"Parmak, eklem, kaburga veya kemiklerin hareket sırasında ses çıkarması bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağır yükün sırta etkisini ve araçlardan çıkan benzer sesleri içermez.","preserves":"Bedendeki eklem ve kemiklerden çıkan gıcırtı sesini korur."},"facet_ids":["F001"],"text":"eklemlerin gıcırdaması","usage_role":"contextual"},{"applicability":"Bir yükün sırta, ses çıkaracak kadar ağır baskı yaptığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka eklemlerin ve yük taşıma araçlarının gıcırtılarını içermez.","preserves":"Yükün ağırlığı ile sırttan çıkan ses arasındaki neden ilişkisini korur."},"facet_ids":["F002"],"text":"yükün sırtı gıcırdatması","usage_role":"explanatory"}],"definition":"Eklemlerin, kemiklerin veya yük taşıyan araçların baskı ve hareket altında çıkardığı gıcırtıdır; ağır yükün sırta böyle bir ses çıkartacak ölçüde baskı yapması da bu alana girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eklem, parmak, kaburga veya kemiğin hareket ya da baskı altında gıcırdaması."},{"facet_id":"F002","role":"specialization","statement":"Ağır yükün sırta baskı yaparak ondan duyulur bir gıcırtı çıkarması."},{"facet_id":"F003","role":"extension","statement":"Çekme kupası, yük taşıma düzeneği veya eyer gibi araçların çıkardığı benzer sesi adlandırma."}],"identity_rationale":"Kaynak ifadesi eklem, parmak ve kaburga sesini; çekme kupası, taşıma düzeneği ve eyer seslerini; ayrıca ağır yükün sırttan ses çıkarmasına yol açmasını tek bir gıcırtı alanında topluyor.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"eklem, parmak, kaburga veya yüklü sırt gıcırtısı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çekme kupasının emilirken çıkardığı ses"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yükün sırtı ses çıkaracak kadar ağırlaştırması"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yük taşıma düzenekleri ile eyerlerin gıcırtısı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kemiklerinin ses çıkarması"}],"lexicalization_note":"Tanım, yalın gıcırtı adını eklem, sırt, çekme kupası ve yük taşıma araçlarına özgü anlatımlardan ayırır; hayvan seslerine genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ağırlığın sessiz baskısı ve kökün hayvan sesi dalı, sesin zorunluluğunu ve kaynağını en açık biçimde sınırlar. Öteki yük ve beden adayları bu ayrımları keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici sonucu sestir; komşu dal ise ağırlığın kişiyi zorlaması ve eğmesiyle ilgilenir, herhangi bir ses gerektirmez.","focus_only":"Ağırlığın eklem veya sırttan duyulur bir gıcırtı çıkarmasını ve bu sesi adlandırır.","gloss":"yük altında gıcırdama ile yük altında eğilme","neighbor_only":"Yükün veya işin kişiyi zorlayıp eğmesi için ses çıkması şartını aramaz.","neighbor_ref":"root_000066/B002","relation_type":"near_neighbor","shared_zone":"Ağır bir yükün beden üzerinde zorlayıcı baskı kurması ortak senaryodur."},{"boundary_match":"field_only","distinction":"Odak dalda sesin kaynağı eklem, kemik veya araçtır; komşu dalda ise ses hayvanın kendisinden ya da insanın hayvana yönelttiği ağız hareketinden çıkar.","focus_only":"Eklem, kemik, sırt ve yük taşıyan araçlardan baskı veya hareketle çıkan gıcırtıyı anlatır.","gloss":"bedensel gıcırtı ile hayvan ve çağrı sesi","neighbor_only":"Hayvanların ötüşlerini ve insanın hayvan çağırmak ya da yönlendirmek için çıkardığı dil sesini anlatır.","neighbor_ref":"root_001543/B006","relation_type":"same_field","shared_zone":"Her iki dal da kısa ve ayırt edici sesleri adlandırır."}],"source_phrase_ar":"صوت المفاصل نقيضها (maqayis)؛ النقيض صوت الأصابع والمفاصل والأضلاع؛ نقيض المحجمة صوتها (ayn)؛ أنقض الحمل ظهره أي أثقله؛ النقيض صوت المحامل والرحال (sihah)؛ الظهر إذا أثقله حمله سمع له نقيض؛ كل صوت لمفصل أو إصبع أو ضلع فهو نقيض (tahdhib)؛ أنقض ظهرك؛ نقيض المفاصل صوتها (mufradat)","source_summary":"Kaynakların ortak alanı, eklem ve kemiklerden ya da yük taşıyan araçlardan gelen gıcırtıdır. Ağır yükün sırta baskı yapıp bu sesi doğurması, ses ile onu oluşturan ağırlık arasındaki bağı açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النقيض صوت المفاصل والأصابع والأضلاع والمحاجم والمحامل والرحال، وأنقض الظهر إذا أثقله الحمل حتى يسمع له صوت.","what_is_not_ar":"ليس زجر القعود أو دعاء المعز أو أصوات الدجاج والعقبان، ولا نقض العهد أو البناء."},"support_links":["sup_5954c008807b647b10d2"]},{"boundary":"Canlının çıkardığı ince ses ile insanın hayvana yönelik dil sesi ayrılmalı; eklem, sırt ve eyer gıcırtıları bu dala katılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001543/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"ince hayvan sesi veya hayvan yönlendiren dil şaklatması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tavuk, kartal, yavru kuş, civciv veya deve yavrusu gibi hayvanların çıkardığı ince ötüş ya da tıklama sesi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanın diliyle tıklama sesi çıkararak genç deveyi veya eşeği yönlendirmesi ya da keçiyi çağırması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sakız çiğnerken çıkan tıklama sesini adlandırma."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı hareketlerin son bölümünde çıkan sesi civciv sesine benzeterek adlandırma."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın kendi ince sesini ve insanın hayvana yönelik benzer ağız sesini iki ayrı çekirdek olarak birlikte karşılar.","boundary_detail":"Canlının çıkardığı ince ses ile insanın hayvana yönelik dil sesi ayrılmalı; eklem, sırt ve eyer gıcırtıları bu dala katılmamalıdır.","branch_image_ar":"نقر وزجر وأصوات الحيوان","concept_gloss":"ince hayvan sesi veya hayvan yönlendiren dil şaklatması","contextual_glosses":[{"applicability":"Tavuk, kartal, yavru kuş, civciv veya deve yavrusu gibi hayvanların kendi sesini anlattığı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanın hayvanı çağıran dil sesini ve cansız kaynaklı uzantıları içermez.","preserves":"Hayvanın çıkardığı ince ve kısa ses niteliğini korur."},"facet_ids":["F001"],"text":"ince ince ötmek","usage_role":"contextual"},{"applicability":"Keçi çağırma veya genç deve ve eşek yönlendirme gibi insandan hayvana yönelen sesli eylemlerde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanların kendiliğinden çıkardığı sesleri ve sakız sesi uzantısını içermez.","preserves":"İnsanın diliyle ses çıkarıp hayvana yönelmesi ve onu çağırması anlamını korur."},"facet_ids":["F002"],"text":"dil şaklatarak çağırmak","usage_role":"contextual"}],"definition":"Bazı hayvanların çıkardığı ince ötüş veya tıklama sesi ile insanın diliyle benzer bir ses çıkarıp hayvanı çağırması ya da yönlendirmesidir; sakız ve bazı hareketlerden çıkan benzer sesler de buna bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tavuk, kartal, yavru kuş, civciv veya deve yavrusu gibi hayvanların çıkardığı ince ötüş ya da tıklama sesi."},{"facet_id":"F002","role":"core","statement":"İnsanın diliyle tıklama sesi çıkararak genç deveyi veya eşeği yönlendirmesi ya da keçiyi çağırması."},{"facet_id":"F003","role":"extension","statement":"Sakız çiğnerken çıkan tıklama sesini adlandırma."},{"facet_id":"F004","role":"source_variant","statement":"Bazı hareketlerin son bölümünde çıkan sesi civciv sesine benzeterek adlandırma."}],"identity_rationale":"Kaynak ifadesi tavuk, kartal, yavru kuş ve deve yavrusu gibi hayvanların seslerini; genç deveyi yönlendirme, keçiyi çağırma ve eşek için dil şaklatma seslerini aynı dalda açıkça topluyor.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"tavuğun ses çıkarması"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kartalın ses çıkarması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yavru kuşun ince ötmesi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"genç deveyi yönlendirmeye yarayan dil şaklatması"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"keçileri çağıran dil sesi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"dilin ucunu üst damağa değdirip eşek için ses çıkarma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"sakızın çiğnenirken çıkardığı ses"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deve yavrularının sesleri"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"civcivlerin sesleri veya bunlara benzeyen sesler"}],"lexicalization_note":"Tanım, yalın ince ses ve dil şaklatması alanını hayvan türlerine, çağırma ve yönlendirme eylemlerine özgü anlatımlardan ayırır; eklem gıcırtısına genişlemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; koyun çağrısı, genel seslenme ve mekanik gıcırtı adayları sesin kaynağı ile yöneldiği katılımcıyı en iyi ayırdı. Kuş ve kedi sesi adayları yalnızca tek tek örnekleri yineliyordu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hayvanın kendi sesini de içerir ve birden çok hayvan türüne yayılır; komşu dal yalnızca çobanın koyun sürüsüne yönelttiği çağrı ve yönlendirme sesidir.","focus_only":"Hayvanların kendi seslerini ve keçi, genç deve veya eşek için çıkarılan farklı çağrı ve yönlendirme seslerini kapsar.","gloss":"çeşitli hayvan sesleri ile çobanın koyun çağrısı","neighbor_only":"Çobanın koyun sürüsünü hem çağırmak hem de yönlendirmek için çıkardığı sese özgüdür.","neighbor_ref":"root_001523/B001","relation_type":"near_neighbor","shared_zone":"İnsanın küçükbaş hayvana yönelttiği çağırma veya yönlendirme sesi iki dalda kesişir."},{"boundary_match":"partial","distinction":"Odak dal belirli bir kısa ağız sesini ve hayvan ötüşlerini birleştirir; komşu dalın seslenme alanı daha geniştir ve konuşma gürültüsünü de kapsar.","focus_only":"Dil ucunun damağa değmesiyle çıkan kısa tıklama sesini ve belirli hayvan ötüşlerini kapsar.","gloss":"dil şaklatması ile genel seslenme ve gürültü","neighbor_only":"Koyuna seslenmenin yanı sıra dildeki genel gürültü, bağırış ve çok konuşma alanına uzanır.","neighbor_ref":"root_000104/B004","relation_type":"near_neighbor","shared_zone":"Küçükbaş hayvana insan sesiyle yönelme iki dalın ortak alanıdır."},{"boundary_match":"field_only","distinction":"Odak dalın sesi canlı ötüşü veya amaçlı ağız hareketidir; komşu dalın sesi ise eklem ya da nesnenin mekanik baskı ve hareketinden doğar.","focus_only":"Hayvanın çıkardığı ötüşü veya insanın hayvana yönelttiği dil şaklatmasını anlatır.","gloss":"hayvan ve çağrı sesi ile eklem gıcırtısı","neighbor_only":"Eklem, kemik, sırt ve yük taşıma araçlarının baskı altında çıkardığı gıcırtıyı anlatır.","neighbor_ref":"root_001543/B005","relation_type":"same_field","shared_zone":"Her iki dal da kısa, ayırt edici sesleri adlandırır."}],"source_phrase_ar":"أنقضت الدجاجة صوتت؛ الإنقاض زجر القعود (maqayis)؛ أنقضت بالحمار؛ أصوات الفراريج والعقاب (ayn)؛ أنقضت العقاب وكذلك الدجاجة؛ الانقاض أصوات صغار الابل؛ أنقضت بالمعز إنقاضا دعوت بها (sihah)؛ أنقضت إنقاضا بالمعز إذا دعوته؛ أنقض الفرخ؛ أصوات أواخر الميس إنقاض الفراريج؛ أنقضت بالحمار (tahdhib)؛ انتقضت الدجاجة صوتت؛ الإنقاض صوت لزجر القعود (mufradat)","source_summary":"Kaynaklar, belirli hayvanların ince sesleriyle insanın hayvan çağırmak veya yönlendirmek için çıkardığı dil sesini aynı alanda birleştirir. Sakızın sesi ve civciv sesine benzetilen başka hareket sesleri bu çekirdeğin sınırlı uzantılarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إنقاض الدجاجة والعقاب والفرخ والفراريج وصغار الإبل، وزجر القعود، ودعاء المعز، والصوت باللسان للحمار ونحوه.","what_is_not_ar":"ليس صرير المفاصل والظهر والمحامل، ولا نقض البناء أو العهد."},"support_links":[]},{"boundary":"Tanım yalnızca adı verilmiş bir bitkiyle sınırlı kalmalı ve aynı biçimin dokuma söken usta anlamıyla karıştırılmamalıdır.","branch_kind":"bare","branch_ref":"root_001543/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"türü belirtilmemiş bir bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Türü ve ayırt edici özellikleri belirtilmemiş bir bitkiyi adlandırma."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eldeki kanıt yalnızca bitki olduğunu söylediği için tür, görünüş veya kullanım yüklemeden dalın tamamını karşılar.","boundary_detail":"Tanım yalnızca adı verilmiş bir bitkiyle sınırlı kalmalı ve aynı biçimin dokuma söken usta anlamıyla karıştırılmamalıdır.","branch_image_ar":"النقاض اسم نبات","concept_gloss":"türü belirtilmemiş bir bitki","contextual_glosses":[{"applicability":"Botanik kimliği bilinmeyen bu tarihsel adın ne tür bir varlığı gösterdiğini kısaca açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün bir bitkiyi adlandırdığına ilişkin mevcut bilginin tamamını korur."},"facet_ids":["F001"],"text":"bir bitki adı","usage_role":"explanatory"}],"definition":"Kaynaklarda türü ve özellikleri açıklanmadan yalnızca adı verilen bir bitkidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Türü ve ayırt edici özellikleri belirtilmemiş bir bitkiyi adlandırma."}],"identity_rationale":"Kaynak ifadesi sözcüğü yalnızca bir bitki adı olarak tanıklıyor; bitkinin türü, görünüşü veya kullanımına ilişkin daha ileri bir özellik vermiyor.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir bitki adı"}],"lexicalization_note":"Tanım, yalın bitki adını eldeki tek anlamsal içerik olarak korur; bitkinin türü veya özellikleri hakkında ek bilgi varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öteki bitki adlarıyla paylaşılan tek özellik bitki olmalarıdır ve tür kimliği bilinmediğinden kanıtlı bir anlam karşıtlığı kurulamaz. Kökün öteki dalları da yalnızca biçim benzerliği taşır.","source_phrase_ar":"النقاض نبات (ayn;tahdhib)","source_summary":"İki kaynak, başka bir botanik açıklama eklemeden bunun bir bitki adı olduğunu ortak biçimde bildirir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الاسم النباتي النقاض كما ورد مجردا في عين وتهذيب.","what_is_not_ar":"ليس النقاض صاحب حرفة نقض الدمقس، ولا المنقوض من الحبل أو الثوب."},"support_links":[]},{"boundary":"Anlam yalnızca aygıra özgü bu özel durumda geçerlidir; genel cinsel yorgunluk, akıntı veya hareket gevşekliği olarak genişletilmemelidir.","branch_kind":"collocation","branch_ref":"root_001543/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","surface_ar":"أَنقَضَ"}],"gloss":"aygırın organını salıp tam sertleşememesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Aygırın cinsel organını aşağı salmasıyla birlikte sertleşmenin tam güç kazanmaması."}}],"root_ar":"ن ق ض","root_id":"root_001543","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca aygırın cinsel organını aşağı saldığı, fakat sertleşmenin tam güç kazanmadığı özel durum için geçerlidir.","boundary_detail":"Anlam yalnızca aygıra özgü bu özel durumda geçerlidir; genel cinsel yorgunluk, akıntı veya hareket gevşekliği olarak genişletilmemelidir.","branch_image_ar":"نقض الفرس في تعبير نوادر الأعراب","concept_gloss":"aygırın organını salıp tam sertleşememesi","contextual_glosses":[{"applicability":"Öznesi açıkça aygır olan ve olayın iki aşamasını açıklayan cümlelerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Organın aşağı salınması ile sertleşmenin tam güç kazanmaması arasındaki eşzamanlı durumu korur."},"facet_ids":["F001"],"text":"sertleşme tamamlanmadan organını salmak","usage_role":"explanatory"}],"definition":"Aygırın cinsel organını aşağı salması, ancak sertleşmesinin tam ve güçlü duruma gelmemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Aygırın cinsel organını aşağı salmasıyla birlikte sertleşmenin tam güç kazanmaması."}],"identity_rationale":"Tek kaynak ifadesi, anlamı aygıra özgü olarak cinsel organın aşağı salınması ve sertleşmenin tam güç kazanmaması biçiminde açıkça sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"aygırın organını salıp tam sertleşememesi"}],"lexicalization_note":"Tanım yalnızca aygırın organını salıp tam sertleşememesini anlatan belirtilmiş ifadeye bağlıdır ve yalın bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; birleşmenin tamamlanmaması ile organ uzanması ve akıntı dalları, eksik sertleşme sınırını en iyi gösterir. Atın yürüyüşü, idrarın kesik gelmesi ve beden yapısı adayları yalnızca daha uzak senaryolar paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal aygırdaki belirli organ duruşunu ve eksik sertleşmeyi birlikte gerektirir; komşu dal ise insanı veya erkek hayvanı kapsayan daha geniş bir boşalamama ve güçten düşme alanıdır.","focus_only":"Aygırın organını aşağı saldığı halde sertleşmenin tam güç kazanmaması durumunu belirtir.","gloss":"aygırda eksik sertleşme ile birleşmenin tamamlanmaması","neighbor_only":"Erkeğin birleşme sırasında boşalmaması veya erkek hayvanın çiftleşme eyleminde güçten düşmesi gibi daha geniş tamamlanmama durumlarını kapsar.","neighbor_ref":"root_001299/B002","relation_type":"near_neighbor","shared_zone":"Erkek katılımcıda cinsel uyarılmanın veya çiftleşme eyleminin tam sonuca ulaşmaması ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalda eksik sertleşme zorunludur ve katılımcı aygırdır; komşu dal ise sıvı akışı ve organın uzanması gibi daha geniş bedensel olayları içerir.","focus_only":"Yalnızca aygırda organın aşağı salınması ve sertleşmenin tam olmaması birleşimini anlatır.","gloss":"eksik sertleşmeli salınma ile organ uzanması ve akıntı","neighbor_only":"İdrar sonrası gelen sıvıyı, erkek insan veya hayvanda organın dışarı uzanmasını, sertleşmeyi ve damlamayı kapsar.","neighbor_ref":"root_001637/B001","relation_type":"near_neighbor","shared_zone":"Erkek hayvanda cinsel organın görünür durumu ve sertleşmeyle ilişkisi iki dalda kesişir."}],"source_phrase_ar":"في نوادر الأعراب: نقض الفرس ورفض إذا أدلى ولم يستحكم إنعاظه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Özel kullanım, aygırın organını saldığı halde sertleşmesinin tam olarak güçlenmemesini anlatır."}],"source_summary":"Bu dal için kaynaklar arasında ortaklaşan çoklu bir anlatım yoktur; anlam tek bir özel kullanım tanıklığına dayanır.","sources":["TA"],"what_is_ar":"يختص بتعبير نوادر الأعراب: نقض الفرس، أي أدلى ولم يستحكم إنعاظه.","what_is_not_ar":"ليس نقض العهد أو البناء، ولا صوت المفاصل، ولا هزال البعير من السفر."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["94:3:1"],"branch_refs":[],"candidate_id":"cand_a807a14aebfa1c9a0e35","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:3:1:antecedent-bound-relative","source_type":"word_analysis","support_ids":["sup_0d930da164b8d76a80be","sup_8444311f06758d44f835"],"title":"relative pronoun binds the ayah to the prior burden","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:1","qac_refs":["94:3:1:1"],"status":"accepted"}},{"anchor_refs":["94:3:1"],"branch_refs":[],"candidate_id":"cand_e4420c6649dde9a9eb32","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:3:1:recited-carryover","source_type":"word_analysis","support_ids":["sup_8444311f06758d44f835","sup_e3e1c4bcd3b07172e115"],"title":"opening sound carries the syntax forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:1","qac_refs":["94:3:1:1"],"status":"accepted"}},{"anchor_refs":["94:3:1"],"branch_refs":[],"candidate_id":"cand_93362f8f77a12a513d5a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"94:3:1:relative-subject-role","source_type":"word_analysis","support_ids":["sup_8444311f06758d44f835","sup_c43d0c5fd9c966ecb9b7"],"title":"relative form supplies the subject slot","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:1","qac_refs":["94:3:1:1"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_6024a00c91310027e35c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:causative-burden-agency","source_type":"word_analysis","support_ids":["sup_90f18a5c198e1c294474","sup_dcf3f78848c1082a2108"],"title":"causative verb makes the burden the damaging agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:2","qac_refs":["94:3:2:1"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_02915abb27eda2cd6213","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:completed-retrospective-harm","source_type":"word_analysis","support_ids":["sup_c093d9c55ba333e4aea6","sup_dcf3f78848c1082a2108"],"title":"perfect verb discloses completed harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:2","qac_refs":["94:3:2:1"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_2d38237e81b4d1a89aa3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:creaking-structural-damage","source_type":"word_analysis","support_ids":["sup_9cf654ec292dea90a7e1","sup_dcf3f78848c1082a2108"],"title":"cracking and groaning are both locally live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:2","qac_refs":["94:3:2:1"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_6baa5ba71ada462883ec","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:phonetic-impact","source_type":"word_analysis","support_ids":["sup_09397a70853807b36b5c","sup_dcf3f78848c1082a2108"],"title":"compact heavy sound concentrates the impact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:2","qac_refs":["94:3:2:1"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_7010f184cd7544d6390d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:rare-breach-root-physical-use","source_type":"word_analysis","support_ids":["sup_dcf3f78848c1082a2108","sup_e3a9b12a47f7156d6f5b"],"title":"breach-root background is narrowed into bodily damage","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:2","qac_refs":["94:3:2:1"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_65a6e6cf0913530090db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:aka-sound-closure","source_type":"word_analysis","support_ids":["sup_5cd2967d00b39c538b19","sup_6f60942ea1b5d63f718e"],"title":"final -aka closure binds the opening arc","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_a57dfe0377d6eb239cc4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:chest-back-body-frame","source_type":"word_analysis","support_ids":["sup_281240d76cf950397765","sup_5cd2967d00b39c538b19"],"title":"back answers the earlier chest frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_decd4ac52510d7142833","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:direct-object-landing","source_type":"word_analysis","support_ids":["sup_467bd7d3ef65af008d4a","sup_5cd2967d00b39c538b19"],"title":"final object completes the relative clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_8c94d1e5a068a36f713e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:load-bearing-anatomy","source_type":"word_analysis","support_ids":["sup_26d8cb6393617ecf83dc","sup_5cd2967d00b39c538b19"],"title":"back is the exact load-bearing anatomy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_98d7f15b789c6254382b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:possessed-addressee-back","source_type":"word_analysis","support_ids":["sup_4f28a198aa37a2f18f59","sup_5cd2967d00b39c538b19"],"title":"suffix makes the damaged back personally possessed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_6b525032c7487b3480a6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:support-manifest-range-narrowed","source_type":"word_analysis","support_ids":["sup_4597189f19d7c6f18c13","sup_5cd2967d00b39c538b19"],"title":"support and manifestation remain controlled resonance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"94:3:3","qac_refs":["94:3:3:1","94:3:3:2"],"status":"accepted"}},{"anchor_refs":["94:3:2"],"branch_refs":[],"candidate_id":"cand_9865278f4eab2619cf31","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001543"],"scope":"focus_ayah","source_local_id":"94:3:2:1","source_type":"qac_morpheme","support_ids":["sup_06d1733c132bd8bb56ae"],"title":"QAC root occurrence: ن ق ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:3:3"],"branch_refs":[],"candidate_id":"cand_e5b00ea5ebaa08764b76","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000970"],"scope":"focus_ayah","source_local_id":"94:3:3:1","source_type":"qac_morpheme","support_ids":["sup_7a542d571c6d03dbaf17"],"title":"QAC root occurrence: ظ ه ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["94:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:3","branch_refs":["root_000970/B002","root_001543/B005"],"candidate_id":"cand_3ea049afe073cca537db","commentary_obligation":"review","hft_ref":"hft_94534ccc24552bd44380","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_audible_load","source_type":"hft","support_ids":["sup_5954c008807b647b10d2"],"title":"baseline_audible_load","trust":"legacy_unbound"},{"anchor_refs":["94:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:3","branch_refs":["root_000970/B006","root_001543/B001"],"candidate_id":"cand_6443dda8797836b7e903","commentary_obligation":"review","hft_ref":"hft_76a36a0f0e4ea8b2c56f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_unmade_backing","source_type":"hft","support_ids":["sup_e63c0d8bc95eae738acf"],"title":"baseline_unmade_backing","trust":"legacy_unbound"},{"anchor_refs":["94:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:3","branch_refs":["root_000970/B005","root_001543/B002"],"candidate_id":"cand_cd329fee262b4b69404a","commentary_obligation":"review","hft_ref":"hft_73c49e3e8406882bee6b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_journey_worn_carrier","source_type":"hft","support_ids":["sup_52b4c2e3a56e5271f92b"],"title":"baseline_journey_worn_carrier","trust":"legacy_unbound"},{"anchor_refs":["94:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"94:3","branch_refs":["root_000970/B003","root_001543/B004"],"candidate_id":"cand_1815138d94a3d37806a7","commentary_obligation":"review","hft_ref":"hft_d1a99f48e735586f62d0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_reopened_surface","source_type":"hft","support_ids":["sup_c44bbb58772171dd5594"],"title":"baseline_reopened_surface","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"94:3:1:1","qac_word_ref":"94:3:1","root_ar":"","surface_ar":"ٱلَّذِىٓ"},{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","root_ar":"ن ق ض","surface_ar":"أَنقَضَ"},{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","root_ar":"ظ ه ر","surface_ar":"ظَهْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:3:3:2","qac_word_ref":"94:3:3","root_ar":"","surface_ar":"كَ"}],"word_analysis_qac_refs":[["94:3:1:1"],["94:3:2:1"],["94:3:3:1","94:3:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["94:3:1","94:3:2","94:3:3"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"94:3:1:1","qac_word_ref":"94:3:1","root_ar":"","surface_ar":"ٱلَّذِىٓ"},{"lemma_ar":"أَنقَضَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"94:3:2:1","qac_word_ref":"94:3:2","root_ar":"ن ق ض","surface_ar":"أَنقَضَ"},{"lemma_ar":"ظَهْر","morph_features":"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"94:3:3:1","qac_word_ref":"94:3:3","root_ar":"ظ ه ر","surface_ar":"ظَهْرَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"94:3:3:2","qac_word_ref":"94:3:3","root_ar":"","surface_ar":"كَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["94:3:1:1"],["94:3:2:1"],["94:3:3:1","94:3:3:2"]],"word_analysis_refs":["94:3:1","94:3:2","94:3:3"],"word_rows":[{"analysis_record_ref":"94:3:1","analytic_gloss_range_en":"masculine singular relative pronoun that retrieves the prior burden and launches a defining relative clause","analytic_root_gloss_range_en":null,"qac_refs":["94:3:1:1"],"root":{},"surface":{"arabic":"ٱلَّذِىٓ","transliteration":"alladhī"}},{"analysis_record_ref":"94:3:2","analytic_gloss_range_en":"Form IV perfect causative: made crack, creak, or groan under load, with the prior burden as causer and the back as direct object","analytic_root_gloss_range_en":"broad root field of undoing, breaking, breach, and collapse-pressure; the local object selects the bodily cracking and audible strain branch","qac_refs":["94:3:2:1"],"root":{"arabic":"ن ق ض","transliteration":"n-q-ḍ"},"surface":{"arabic":"أَنقَضَ","transliteration":"anqaḍa"}},{"analysis_record_ref":"94:3:3","analytic_gloss_range_en":"singular possessed back as the explicit direct object, the concrete load-bearing body part affected by the burden","analytic_root_gloss_range_en":"broad field includes back, outwardness, surface, support, and backing; the local noun selects the concrete back while support and manifestation remain controlled resonance","qac_refs":["94:3:3:1","94:3:3:2"],"root":{"arabic":"ظ ه ر","transliteration":"ẓ-h-r"},"surface":{"arabic":"ظَهْرَكَ","transliteration":"ẓahraka"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["94:3"],"branch_refs":["root_000970/B002","root_001543/B005"],"candidate_id":"cand_3ea049afe073cca537db","evidence_scope":"focus_ayah","hft_ref":"hft_94534ccc24552bd44380","item_id":"baseline_audible_load","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_audible_load","support_id":"sup_5954c008807b647b10d2"},{"anchor_refs":["94:3"],"branch_refs":["root_000970/B006","root_001543/B001"],"candidate_id":"cand_6443dda8797836b7e903","evidence_scope":"focus_ayah","hft_ref":"hft_76a36a0f0e4ea8b2c56f","item_id":"baseline_unmade_backing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_unmade_backing","support_id":"sup_e63c0d8bc95eae738acf"},{"anchor_refs":["94:3"],"branch_refs":["root_000970/B005","root_001543/B002"],"candidate_id":"cand_cd329fee262b4b69404a","evidence_scope":"focus_ayah","hft_ref":"hft_73c49e3e8406882bee6b","item_id":"baseline_journey_worn_carrier","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_journey_worn_carrier","support_id":"sup_52b4c2e3a56e5271f92b"},{"anchor_refs":["94:3"],"branch_refs":["root_000970/B003","root_001543/B004"],"candidate_id":"cand_1815138d94a3d37806a7","evidence_scope":"focus_ayah","hft_ref":"hft_d1a99f48e735586f62d0","item_id":"baseline_reopened_surface","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_reopened_surface","support_id":"sup_c44bbb58772171dd5594"}],"diagnostics":[],"lane_counts":{"global":9,"macro":12,"micro":4},"packet_summary":{"ayah_count":8,"focus_ref":"94:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"و ز ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001643","furuq_root_norm":"و ز ر","furuq_source_root_norm":"و ز ر","is_dominant":true,"target_occurrences":24,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000654","furuq_root_norm":"ز و ر","furuq_source_root_norm":"ز و ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"94:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"94:3","lane":"micro","linguistic_source_ref":"94:3","surface_ref":"94:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"94:3","target_tokens":[["O",["94:3:1"]],["belini",["94:3:3"]],["ağırlaştırmıştı",["94:3:2"]]],"text":"O, belini ağırlaştırmıştı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s094-p01-001-008","label":"Whole surah","number":1,"refs":["94:1","94:2","94:3","94:4","94:5","94:6","94:7","94:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:3:2:1","source_type":"qac_morpheme","support_id":"sup_06d1733c132bd8bb56ae","text":"{\"lemma_ar\":\"أَنقَضَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>anqaDa|ROOT:nqD|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"94:3:2:1\",\"qac_word_ref\":\"94:3:2\",\"root_ar\":\"ن ق ض\",\"surface_ar\":\"أَنقَضَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2:phonetic-impact","source_type":"word_analysis","support_id":"sup_09397a70853807b36b5c","text":"{\"blocking_evidence\":null,\"headline\":\"compact heavy sound concentrates the impact\",\"reader_payoff\":\"The reader notices that the compact qaf-and-dad sound cluster sits at the clause center where the cracking or groaning damage-event is named.\",\"reason\":\"The phonetic claim is aligned with the same central verb that grammar and semantics already mark as the damage-event.\",\"representative_source_ids\":[\"QP-34523fdc\",\"QP-62fddc49\",\"MP-8950b271\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:1:antecedent-bound-relative","source_type":"word_analysis","support_id":"sup_0d930da164b8d76a80be","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun binds the ayah to the prior burden\",\"reader_payoff\":\"The reader notices that the ayah boundary falls inside the syntax, so the current clause identifies the already-mentioned burden rather than starting a fresh event.\",\"reason\":\"QAC and attachment evidence identify the word as a masculine singular relative pronoun whose modified head lies in 94:2, while translation support warns that a single-ayah rendering can obscure that dependency.\",\"representative_source_ids\":[\"QG-240de6c8\",\"QG-6b5190c6\",\"QG-ba0e588b\",\"MT-b527a5a2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:load-bearing-anatomy","source_type":"word_analysis","support_id":"sup_26d8cb6393617ecf83dc","text":"{\"blocking_evidence\":null,\"headline\":\"back is the exact load-bearing anatomy\",\"reader_payoff\":\"The reader notices that the burden strikes the body part made for carrying weight, so the image is mechanically precise.\",\"reason\":\"The local noun is a concrete singular back, and V4 keeps the back and load-support branch available for the root.\",\"representative_source_ids\":[\"QS-5fa6cfe3\",\"QS-adcecc14\",\"MS-0df11cac\",\"QF-f06e8d50\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:chest-back-body-frame","source_type":"word_analysis","support_id":"sup_281240d76cf950397765","text":"{\"blocking_evidence\":null,\"headline\":\"back answers the earlier chest frame\",\"reader_payoff\":\"The reader notices the same-surah body frame: the opened chest in 94:1 is answered by the relieved back in 94:3.\",\"reason\":\"The row gives the concrete same-surah reference, and the current word is the matching body-part term at the end of 94:3.\",\"representative_source_ids\":[\"QE-cf565bdb\",\"ME-796657d3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:support-manifest-range-narrowed","source_type":"word_analysis","support_id":"sup_4597189f19d7c6f18c13","text":"{\"blocking_evidence\":null,\"headline\":\"support and manifestation remain controlled resonance\",\"reader_payoff\":\"The reader notices that the concrete back also evokes backing, support, and visible strain, while grammar keeps the local sense from becoming an abstract support term.\",\"reason\":\"V4 lists support and manifestation branches for the root, but QAC and attachment constrain the local form to a concrete possessed back as direct object.\",\"representative_source_ids\":[\"QS-00ec8638\",\"QS-7d057a83\",\"MS-c65216d9\",\"QI-f1c91635\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:direct-object-landing","source_type":"word_analysis","support_id":"sup_467bd7d3ef65af008d4a","text":"{\"blocking_evidence\":null,\"headline\":\"final object completes the relative clause\",\"reader_payoff\":\"The reader notices that the ayah withholds completion until the final word names the affected structure.\",\"reason\":\"Attachment evidence makes the word the explicit direct object of the verb, and the relative clause remains grammatically incomplete until that object arrives.\",\"representative_source_ids\":[\"QG-2a0b90ba\",\"QT-a931e9ed\",\"QT-c05c338d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:possessed-addressee-back","source_type":"word_analysis","support_id":"sup_4f28a198aa37a2f18f59","text":"{\"blocking_evidence\":null,\"headline\":\"suffix makes the damaged back personally possessed\",\"reader_payoff\":\"The reader notices that the damage is held inside direct address: the burden and the back both belong to the same addressed person.\",\"reason\":\"QAC marks a singular concrete noun with a second-person masculine singular suffix, and attachment evidence treats the suffix as the possessive complement of the noun.\",\"representative_source_ids\":[\"QG-1ef06661\",\"QG-801927c2\",\"QF-b888c750\",\"QB-8094df59\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3","source_type":"word_analysis","support_id":"sup_5cd2967d00b39c538b19","text":"{\"gloss_range\":\"singular possessed back as the explicit direct object, the concrete load-bearing body part affected by the burden\",\"prose\":\"{{ar:ظَهْرَكَ}} ({{tr:ẓahraka}}) lands the clause on the addressee's own back, not on a generic body or a loose metaphor. The suffix binds the affected body part to the same addressee who had the prior burden, while the accusative object role makes the back the structure directly acted on. The noun's load-bearing range keeps the image concrete: this is the platform on which weight bears down, so damage to it also signals weakened backing capacity. At the same time, the root's support and manifestation field is only a controlled resonance; hidden pressure becomes visible through damage to the bearer, but the local word remains the singular concrete back. The final word also answers the earlier chest-opening body frame (94:1) with the burdened back and closes the opening arc with the repeated -aka sound.\",\"root_display\":\"{{ar:ظ ه ر}} ({{tr:ẓ-h-r}})\",\"root_gloss_range\":\"broad field includes back, outwardness, surface, support, and backing; the local noun selects the concrete back while support and manifestation remain controlled resonance\",\"surface_display\":\"{{ar:ظَهْرَكَ}} ({{tr:ẓahraka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:3:aka-sound-closure","source_type":"word_analysis","support_id":"sup_6f60942ea1b5d63f718e","text":"{\"blocking_evidence\":null,\"headline\":\"final -aka closure binds the opening arc\",\"reader_payoff\":\"The reader notices that the final possessed form echoes the -aka endings of 94:1-2 and gives the three-ayah opening a shared closure sound.\",\"reason\":\"The same second-person suffix sound closes the key body and burden terms across 94:1-3.\",\"representative_source_ids\":[\"QP-42f4d95b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"94:3:3:1","source_type":"qac_morpheme","support_id":"sup_7a542d571c6d03dbaf17","text":"{\"lemma_ar\":\"ظَهْر\",\"morph_features\":\"STEM|POS:N|LEM:Zahor|ROOT:Zhr|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"94:3:3:1\",\"qac_word_ref\":\"94:3:3\",\"root_ar\":\"ظ ه ر\",\"surface_ar\":\"ظَهْرَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:1","source_type":"word_analysis","support_id":"sup_8444311f06758d44f835","text":"{\"gloss_range\":\"masculine singular relative pronoun that retrieves the prior burden and launches a defining relative clause\",\"prose\":\"{{ar:ٱلَّذِىٓ}} ({{tr:alladhī}}) does not begin a new independent statement; it pulls the prior burden across the ayah boundary and defines that burden by what it did. Its masculine singular relative form fills the subject-link for {{ar:أَنقَضَ}} ({{tr:anqaḍa}}), so the burden itself becomes the grammatical cause in the clause. Its fused entry and lengthened ending give the boundary-opening relative marker audible carryover rather than a hard restart: the reader must bring the earlier noun forward before the damage can be understood.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِىٓ}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2:causative-burden-agency","source_type":"word_analysis","support_id":"sup_90f18a5c198e1c294474","text":"{\"blocking_evidence\":null,\"headline\":\"causative verb makes the burden the damaging agent\",\"reader_payoff\":\"The reader notices that the burden actively causes the damage rather than remaining a passive possession or background weight.\",\"reason\":\"QAC marks a Form IV perfect verb, and attachment evidence gives it a relative subject-link to the prior burden plus an explicit direct object.\",\"representative_source_ids\":[\"QG-08c11a68\",\"QG-f61dca66\",\"QF-c1cd36c5\",\"MF-71cd92a9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2:creaking-structural-damage","source_type":"word_analysis","support_id":"sup_9cf654ec292dea90a7e1","text":"{\"blocking_evidence\":null,\"headline\":\"cracking and groaning are both locally live\",\"reader_payoff\":\"The reader notices that the verb evokes both structural fracture and audible strain, making the burden's pressure perceptible rather than abstract.\",\"reason\":\"The explicit object is a back, so the physical and auditory strain sense is locally licensed while more general undoing remains background.\",\"representative_source_ids\":[\"QS-e222ede5\",\"QS-f2d43a18\",\"MS-3fee65d8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2:completed-retrospective-harm","source_type":"word_analysis","support_id":"sup_c093d9c55ba333e4aea6","text":"{\"blocking_evidence\":null,\"headline\":\"perfect verb discloses completed harm\",\"reader_payoff\":\"The reader notices that the relief already mentioned is explained by a completed injury: the burden had been damaging the bearer.\",\"reason\":\"The perfect form presents the damage as accomplished, and the clause remains subordinate to the burden already named in 94:2.\",\"representative_source_ids\":[\"QG-832d872b\",\"MG-4f998b37\",\"QB-cf5a3729\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:1:relative-subject-role","source_type":"word_analysis","support_id":"sup_c43d0c5fd9c966ecb9b7","text":"{\"blocking_evidence\":null,\"headline\":\"relative form supplies the subject slot\",\"reader_payoff\":\"The reader notices that the burden is not merely named in the background; it is routed into the clause as the actor whose effect is described.\",\"reason\":\"Attachment evidence associates the relative pronoun with the subject relation for the verb, and the verb instance routes the subject through the prior burden.\",\"representative_source_ids\":[\"QG-4274fffc\",\"QT-76d454ca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2","source_type":"word_analysis","support_id":"sup_dcf3f78848c1082a2108","text":"{\"gloss_range\":\"Form IV perfect causative: made crack, creak, or groan under load, with the prior burden as causer and the back as direct object\",\"prose\":\"{{ar:أَنقَضَ}} ({{tr:anqaḍa}}) is the ayah's pressure point. As a Form IV perfect, it presents the damaging action as a completed fact and assigns causation to the prior burden: the load made the back crack or groan. The root's wider undoing and breach field, familiar from covenant-breaking uses (2:27; 13:25), is narrowed here by {{ar:ظَهْرَكَ}} ({{tr:ẓahraka}}) into bodily load-strain, so the abstract burden becomes audible structural damage like a load-bearing frame creaking under weight. The compact qaf-and-dad impact cluster concentrates that cracking or groaning sound at the clause center without replacing the grammatical frame.\",\"root_display\":\"{{ar:ن ق ض}} ({{tr:n-q-ḍ}})\",\"root_gloss_range\":\"broad root field of undoing, breaking, breach, and collapse-pressure; the local object selects the bodily cracking and audible strain branch\",\"surface_display\":\"{{ar:أَنقَضَ}} ({{tr:anqaḍa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:2:rare-breach-root-physical-use","source_type":"word_analysis","support_id":"sup_e3a9b12a47f7156d6f5b","text":"{\"blocking_evidence\":null,\"headline\":\"breach-root background is narrowed into bodily damage\",\"reader_payoff\":\"The reader notices that a root familiar from undoing and covenant breach (2:27; 13:25) is unusually pressed into a physical back-cracking scene.\",\"reason\":\"The broader root field supports undoing and breach pressure, but the local Form IV verb with a concrete back object selects bodily cracking or groaning rather than an actual covenant action.\",\"representative_source_ids\":[\"QS-81e0ce17\",\"MS-6ce552d4\",\"MI-e7f05b6f\",\"MH-c6f573d9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"94:3:1:recited-carryover","source_type":"word_analysis","support_id":"sup_e3e1c4bcd3b07172e115","text":"{\"blocking_evidence\":null,\"headline\":\"opening sound carries the syntax forward\",\"reader_payoff\":\"The reader notices that the opening relative marker is heard as continuation, not as a hard restart after the previous ayah.\",\"reason\":\"The surface form is the same relative marker that carries the prior noun into the new verse-unit, so the phonetic observation supports the syntactic carryover already licensed by attachment evidence.\",\"representative_source_ids\":[\"QF-862541de\",\"QP-35d3f2e6\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000970/B002","root_001543/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001543","role":"The literal image of a back or joints creaking under weight supplies the audible stress signal in the mechanism.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000970","role":"The anatomical back opposite the belly supplies the load-bearing body part on which the force is registered.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"The burden made the body's supporting frame announce its strain: the verse gives an acoustic, near-failure measure of its force.","before":"The burden was simply very heavy."},"confidence":"strong","focus_anchor":"The causative verb and the possessed back form a direct load-and-response construction.","mechanism":"A weight does not merely rest on the back; it loads the body until its supporting joints audibly register strain. The sound is evidence of force nearing the body's carrying limit.","model_id":"baseline_audible_load"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_audible_load","source_type":"hft","support_id":"sup_5954c008807b647b10d2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000970/B006","root_001543/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001543","role":"Undoing a firm rope, knot, or structure supplies the action of dismantling an organized support rather than merely pressing it.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000970","role":"Backing and assistance supply the functional support that the burden threatens to unmake.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"A load was undoing the addressee's means of being supported, bodily and potentially relational, from the structure outward.","before":"A load hurt one bodily location."},"confidence":"medium","focus_anchor":"The verb can undo what was made firm, while the noun can denote backing or support.","mechanism":"The burden acts structurally: it unfastens the very support by which the addressee remains braced. This can coexist with the anatomical reading while extending the back into capacity, aid, or a support system.","model_id":"baseline_unmade_backing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_unmade_backing","source_type":"hft","support_id":"sup_e63c0d8bc95eae738acf","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000970/B005","root_001543/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001543","role":"The camel worn down by travel supplies cumulative depletion rather than a single instant of pressure.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_000970","role":"The load-bearing mount supplies the carrier role assigned to the possessed back.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"The burden had turned the addressee into a journey-worn carrier whose load-bearing reserve was being spent over distance and time.","before":"The burden was an abstract oppressive weight."},"confidence":"exploratory","focus_anchor":"Both focus roots have load-animal branches: travel-worn exhaustion and a mount kept for bearing loads.","mechanism":"The addressee is momentarily imaged as a carrier depleted by repeated journeys. The back is not passive anatomy but transport infrastructure whose strength has been consumed by what it carries.","model_id":"baseline_journey_worn_carrier"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_journey_worn_carrier","source_type":"hft","support_id":"sup_52b4c2e3a56e5271f92b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ","ayah_ref":"94:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000970/B003","root_001543/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001543","role":"A wound or settled matter reopening after closure supplies the relapse mechanism.","root":"ن ق ض","source_ref":"94:3","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000970","role":"The upper or outer surface supplies the bodily plane across which the reopened seam is imagined.","root":"ظ ه ر","source_ref":"94:3","source_word_indices":["3"]}],"changed_reading":{"after":"The burden reopened a previously closed vulnerability in the body's outer frame, making the strain recurrent rather than merely acute.","before":"The burden produced undifferentiated damage."},"confidence":"exploratory","focus_anchor":"The verb can describe a healed closure reopening, and the back can be an outer or upper surface.","mechanism":"Pressure reopens what had once closed or settled across the body's outer supporting surface. This gives the verse a relapse model: strain can reactivate an old seam rather than create damage from nothing.","model_id":"baseline_reopened_surface"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_reopened_surface","source_type":"hft","support_id":"sup_c44bbb58772171dd5594","trust":"legacy_unbound"}]}
</lane_packet_json>
