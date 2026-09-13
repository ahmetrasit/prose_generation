# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:11",
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
{"branch_registry":[{"boundary":"Taş atma eylemi ile atış veya kırma aracı olan taş bu dala girer; ölüm, giysi ve artış anlamları girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"taş atma ve taş kırma taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefe taş atma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Atılan taş, ayrıca başka taşları kırmak için vurulan iri taş olarak adlandırılır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem ile onun atma veya kırma aracı olan taşını birlikte anlatmak gerektiğinde kullanılır.","boundary_detail":"Taş atma eylemi ile atış veya kırma aracı olan taş bu dala girer; ölüm, giysi ve artış anlamları girmez.","branch_image_ar":"الرمي بالحجر والصخرة","concept_gloss":"taş atma ve taş kırma taşı","contextual_glosses":[{"applicability":"Bir kişinin veya topluluğun bir hedefe taş fırlattığı eylem bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atılan veya başka taşları kırmakta kullanılan araç taşı anlamını dışarıda bırakır.","preserves":"Hedefe taş fırlatma eylemini açık biçimde korur."},"facet_ids":["F001"],"text":"taş atmak","usage_role":"general"},{"applicability":"Başka taşları vurarak parçalamaya yarayan iri taşın adı gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir hedefe taş atma eylemini ve yalnızca atış için kullanılan taşı dışarıda bırakır.","preserves":"Taşın kırma aracı olarak kullanılmasını korur."},"facet_ids":["F002"],"text":"taş kırma taşı","usage_role":"contextual"}],"definition":"Bir hedefe taş atmayı; ayrıca atış aracı olan ya da başka taşları kırmak için vurulan taşı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefe taş atma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Atılan taş, ayrıca başka taşları kırmak için vurulan iri taş olarak adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Taşla atma dalını ölüm ve yok oluş dalıyla karıştırır.","fit":"displacement","loses":"Taş atma eylemini ve araç taşını bütünüyle yitirir.","preserves":"Aynı kökün başka bir dalındaki sona erme düşüncesini çağrıştırır."},"text":"ölüm"},{"category":"confusable","error_profile":{"adds":null,"collision":"Bu dalı ayrı olan giysi dalıyla karıştırır.","fit":"displacement","loses":"Taşla atma ve taş kırma aracına ilişkin bütün içeriği yitirir.","preserves":"Aynı kökün giysi dalına ait somut bir nesneyi belirtir."},"text":"omuz giysisi"}],"identity_rationale":"Yetkili kaynak cümlesi, bir hedefe taş atma eylemini ve atmak ya da başka taşları kırmak için kullanılan taşı birlikte açıkça destekler. Hazırlanan dal çerçevesi bu iki bağlı yönü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ona taş attı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"taşı bir kaya ya da kazmayla vurarak kırdı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"atmak veya başka taşları kırmak için kullanılan taş"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"atılan taş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kaya"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kayalar"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir topluluk adına taş atarak karşı koydu"}],"lexicalization_note":"Dal hem yalın ad biçimlerini hem de taşla atma, taş kırma ve bir topluluk adına taş atma gibi belirli kuruluşları içerir; kuruluşlara bağlı eylemler yalın biçimin bütünü sayılmaz.","neighbor_coverage_note":"Sunulan on iki adayın tümü değerlendirildi. Taş ve taş atma alanındaki dört aday sınırı açıklığa kavuşturduğu için seçildi; savaş, ateş, kuyu taşı ve aynı kökün hareket, yok oluş, giysi ve artış dalları yalnızca uzak konu ortaklığı ya da biçim ortaklığı taşıdığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal taşın boyutunu çakılla sınırlamaz ve araç taşını da adlandırır; komşu dal ise çakıl taşıyla atışı ve karşılıklı atış görünümünü öne çıkarır.","focus_only":"İri taşla atmayı ve başka taşları kırmakta kullanılan araç taşını da kapsar.","gloss":"taş atma / çakıl atma","neighbor_only":"Özellikle çakıl taşıyla atmayı ve karşılıklı çakıl atmayı kapsar.","neighbor_ref":"root_000325/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe küçük ya da büyük taş parçaları fırlatma eyleminde buluşur."},{"boundary_match":"partial","distinction":"Odak dalda karşılıklılık zorunlu değildir ve taşın araç adı da vardır; komşu dalın ayırt edici sınırı tarafların birbirine taş atmasıdır.","focus_only":"Tek yönlü taş atmayı ve atış ya da kırma aracını kapsar.","gloss":"taş atmak / karşılıklı taş atmak","neighbor_only":"İki tarafın birbirine taş atmasını belirgin bir karşılıklılık içinde anlatır.","neighbor_ref":"root_000408/B004","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı insanlara veya hedeflere taş fırlatma eylemidir."},{"boundary_match":"field_only","distinction":"Odak dalın temel işlemi taşı fırlatmak veya taşla taş kırmaktır; komşu dalda araç elde tutulur ve hedefe doğrudan vurulur.","focus_only":"Taş fırlatmayı ve taşla başka taşları kırmayı anlatır.","gloss":"taşla atma / sopayla vurma","neighbor_only":"Hurma salkımının sapı ya da sopa ile doğrudan vurmayı anlatır.","neighbor_ref":"root_000998/B004","relation_type":"same_field","shared_zone":"Her iki dal bir araç kullanarak hedefe güç uygulama alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal taşı belirli bir atma ya da kırma işlevi içinde ele alır; komşu dal taşın maddesini ve sertlik özelliklerini eylemden bağımsız adlandırır.","focus_only":"Taşın atılması veya kırma aracı olarak kullanılması eylemini ve işlevini bildirir.","gloss":"taş kullanımı / taşın kendisi","neighbor_only":"Taşın kendisini, sertliğini ve taşlaşmayla ilgili adlandırmaları genişçe kapsar.","neighbor_ref":"root_000296/B003","relation_type":"same_field","shared_zone":"Her iki dalın somut ortak öğesi taştır."}],"source_phrase_ar":"رديته بالحجارة أرديه رميته (maqayis); المردى حجر يرمى به (sihah); المرداة الحجر الذي يرمى به (tahdhib); المرداة حجر تكسر بها الحجارة فترديها (mufradat)","source_summary":"Kaynakların ortak çizgisi taşla atmayı ve bu işte kullanılan taşı bildirir; taşın başka taşları kırmakta kullanılması araç yönünü daha belirgin kılar.","sources":["MQ","SI","TA","MU"],"what_is_ar":"رمي الشيء بالحجارة؛ المرداة الحجر الذي يرمى به أو تكسر به الحجارة؛ الرداة الصخرة؛ المراماة عن القوم","what_is_not_ar":"ليس الرداء الملبوس ولا الردء المعين ولا رديء الشيء"},"support_links":[]},{"boundary":"Dal özel hızlı yürüyüş ve tek ayaklı sekme biçimleriyle sınırlıdır; ağır bacak adı yalnız kendi sözlük biriminde korunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B002","candidate_links":[{"candidate_id":"cand_ae25ea670591c9c755f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"atın özel hızlı gidişi, insanın tek ayaklı sekmesi ve karganın sekmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın özel hızlı gidişi, çocuk veya genç kızın tek ayaklı sekmesi ve karganın sekmesi, tanıklanan özneye bağlı hareket kullanımlarıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At için koşu ile sert yürüyüş arasında, yere belirgin basışlarla gerçekleşen hızlı gidiştir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çocuk veya genç kız için bir ayağı kaldırıp öteki ayak üzerinde ilerleme ya da sıçramadır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karga için hareket, sekerek yürüme biçiminde tanıklanır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Atın özel hızlı gidişini, çocuk veya genç kızın tek ayaklı sekmesini ve karganın sekmesini birlikte özetler.","boundary_detail":"Dal özel hızlı yürüyüş ve tek ayaklı sekme biçimleriyle sınırlıdır; ağır bacak adı yalnız kendi sözlük biriminde korunur.","branch_image_ar":"الترامي في العدو والقفز","concept_gloss":"atın özel hızlı gidişi, insanın tek ayaklı sekmesi ve karganın sekmesi","contextual_glosses":[{"applicability":"Atın yere belirgin basarak olağan yürüyüşten hızlı ilerlediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çocuk veya genç kızın tek ayak üzerinde sekmesini ve karganın sekmesini dışarıda bırakır.","preserves":"Atın özel hızlı ve sert basışlı gidişini korur."},"facet_ids":["F001","F002"],"text":"koşu ile sert yürüyüş arasında hızla gitmek","usage_role":"contextual"},{"applicability":"Bir çocuk veya genç kızın bir ayağını kaldırarak oyun içinde ilerlediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın koşu ile sert yürüyüş arasındaki hızlı gidişini ve kuş örneğini dışarıda bırakır.","preserves":"İnsandaki tek ayaklı sıçrama ve ilerleme biçimini korur."},"facet_ids":["F001","F003"],"text":"tek ayak üzerinde sekmek","usage_role":"contextual"},{"applicability":"Karganın sıçramalı yürüyüşünü doğal Türkçeyle anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın özel gidişini ve insanın tek ayaklı oyun hareketini dışarıda bırakır.","preserves":"Kuşun sekmeli ilerleyişini açıkça korur."},"facet_ids":["F001","F004"],"text":"sekerek yürümek","usage_role":"contextual"}],"definition":"Atın hızlı ve belirgin adımlarla, koşu ile sert yürüyüş arasında ilerlemesini; çocuk veya genç kızın bir ayağını kaldırıp öteki üzerinde sekmesini; karganın ise sekerek yürümesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın özel hızlı gidişi, çocuk veya genç kızın tek ayaklı sekmesi ve karganın sekmesi, tanıklanan özneye bağlı hareket kullanımlarıdır."},{"facet_id":"F002","role":"specialization","statement":"At için koşu ile sert yürüyüş arasında, yere belirgin basışlarla gerçekleşen hızlı gidiştir."},{"facet_id":"F003","role":"specialization","statement":"Çocuk veya genç kız için bir ayağı kaldırıp öteki ayak üzerinde ilerleme ya da sıçramadır."},{"facet_id":"F004","role":"example","statement":"Karga için hareket, sekerek yürüme biçiminde tanıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü koşuyu bu özel hareket dalına katar.","collision":null,"fit":"broadening","loses":"Koşu ile sert yürüyüş arasındaki özel basışı ve tek ayaklı sekmeyi yitirir.","preserves":"Atın olağan yürüyüşten daha hızlı ilerlemesini korur."},"text":"koşmak"},{"category":"confusable","error_profile":{"adds":"Yavaşlık ve genel hantallık anlamı ekler.","collision":"Ayrı sözlük birimindeki ağır bacak adını dalın hareket çekirdeği sanmaya yol açar.","fit":"displacement","loses":"Hızlı gidişi ve tek ayak üzerinde sekmeyi yitirir.","preserves":"Bazı hayvan bacaklarının ağır basışını çağrıştırır."},"text":"ağır yürümek"}],"identity_rationale":"Yetkili cümle atın hızlanmasını, koşu ile sert yürüyüş arasındaki gidişini, tek ayak üzerinde ilerleyen kızları ve karganın sekmesini destekler. Deve ile filin ağır basan bacakları ayrı bir sözlük birimi olarak tanıklanır, fakat dalın yetkili ortak iddiasının kurucu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"at koşu ile sert yürüyüş arasında hızla gitti"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"eşeğin bağlandığı yerle yuvarlandığı yer arasındaki koşusu"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çocuk bir ayağını kaldırıp ötekiyle sıçradı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"genç kızlar oyun oynarken tek ayak üzerinde sektiler"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"karga sekerek yürüdü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"deve ve filin ağır, sert basan bacakları"}],"lexicalization_note":"Anlamların çoğu belirli hayvan veya insan özneli kuruluşlarda gerçekleşir; yalın ad ve bu kuruluşlar ayrı tutulur, bunlardan genel bir hareket anlamı türetilmez.","neighbor_coverage_note":"Sunulan on iki adayın tümü değerlendirildi. Dört hareket adayı hız, adım düzeni ve sekme sınırlarını gerçekten ayırdığı için seçildi; yorgunluk, yavaş sürünme ve aynı kökün taş, yok oluş, giysi ve artış dalları anlam çekirdeğini açıklamadığı için dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tam koşudan daha özel bir ara gidişi ve sekmeyi içerir; komşu dalın çekirdeği ise hızlı ve art arda koşudur.","focus_only":"Koşu ile sert yürüyüş arasındaki özel gidişi ve tek ayaklı sekmeyi kapsar.","gloss":"özel hızlı gidiş / hızlı koşu","neighbor_only":"Kesintisiz, art arda gelen hızlı koşuyu ve belirli koşu duruşlarını öne çıkarır.","neighbor_ref":"root_000469/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da at veya başka bir hayvanın hızlı ilerlemesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal hız, sert basış ve sekme özellikleriyle belirlenir; komşu dal geniş adım ve katır yürüyüşüne benzerlikle sınırlıdır.","focus_only":"Tek ayaklı sekmeyi ve atın sert basışlı hızlı gidişini içerir.","gloss":"hızlı sekmeli gidiş / geniş adımlı gidiş","neighbor_only":"Binek hayvanının katır yürüyüşünü andıran geniş adımlı gidişini anlatır.","neighbor_ref":"root_000137/B002","relation_type":"near_synonym","shared_zone":"İki dal da hayvanın sıradan yürüyüşten ayrılan özel bir ilerleme biçimini adlandırır."},{"boundary_match":"partial","distinction":"Odak dal hızın yanında basış ve tek ayaklı hareket biçimini de şart koşar; komşu dal herhangi bir özel adım düzeni gerektirmeden hızlanmayı anlatır.","focus_only":"Belirli öznelerdeki ara yürüyüşü ve tek ayaklı sekmeyi kodlar.","gloss":"özel hareket biçimi / genel hızlanma","neighbor_only":"Yürüme veya koşmadaki genel hızlanmayı ve hızla uzaklaşmayı kapsar.","neighbor_ref":"root_001499/B002","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı hızlı ilerlemedir."},{"boundary_match":"partial","distinction":"Odak dal ilerleme biçimini adlandırır; komşu dal ise uzuvdaki bozukluk, sallanma veya ağırlık görünüşünü merkeze alır.","focus_only":"Hızlı ara gidiş veya düzenli tek ayaklı sekme içerir.","gloss":"sekmeli ilerleme / uzuv düzensizliği","neighbor_only":"Elin ya da ayağın düzensiz kalkması, sallanması veya yük yüzünden ağırlaşması üzerinde durur.","neighbor_ref":"root_000305/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal yürüyüşte bacakların olağandan farklı çalışmasını konu edinir."}],"source_phrase_ar":"ردى الفرس أسرع (maqayis); ردى الفرس بين العدو والمشى الشديد (sihah); الجواري يردين إذا رفعت إحداهن رجلها ومشت على رجل (tahdhib); الغراب يردي إذا حجل (tahdhib)","source_summary":"Kaynak tanıklıkları, atın hızlı ve sert basışlı gidişini, çocuk veya genç kızın tek ayak üzerindeki hareketini ve karganın sekmesini aynı hareket dalında toplar; görünüş özneye göre değişir.","sources":["MQ","SI","TA"],"what_is_ar":"عدو الفرس والحمار بين العدو والمشي الشديد؛ قفز الغلام أو الجارية على رجل؛ حجل الغراب؛ ثقل قوائم الإبل والفيل في الوطء","what_is_not_ar":"ليس الهلاك ولا السقوط في المهواة ولا الرمي بالحجارة"},"support_links":["sup_e686bb7ff19c95ffeeef"]},{"boundary":"Gerçek düşüş, ölüm tehlikesine giriş ve ölüm ya da yok oluş sonucu bu dala girer; taş atma veya giysi anlamları girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B003","candidate_links":[{"candidate_id":"cand_6f7a512a11799e9ec388","lane":"micro"},{"candidate_id":"cand_0b988127058ac570c7a3","lane":"micro"},{"candidate_id":"cand_d80164acff3c3d291407","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"düşerek ya da başka yolla ölme, yok olma veya yok etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir canlının ölmesi veya bir şeyin varlığını yitirip yok olmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir özne, kişiyi ya da şeyi öldürerek veya yok ederek bu sonuca götürebilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuyuya, dağdan aşağıya veya başka bir derinliğe düşme bu sonuca götüren somut yoldur."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin kendini ölüm tehlikesine atması, sonuç gerçekleşmeden önceki tehlikeli yönelişi anlatır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sonucu, bu sonucu başkasına yaşatmayı ve düşüş yoluyla ölüm tehlikesine girmeyi birlikte anlatan genel açıklamadır.","boundary_detail":"Gerçek düşüş, ölüm tehlikesine giriş ve ölüm ya da yok oluş sonucu bu dala girer; taş atma veya giysi anlamları girmez.","branch_image_ar":"السقوط إلى الهلاك","concept_gloss":"düşerek ya da başka yolla ölme, yok olma veya yok etme","contextual_glosses":[{"applicability":"Bir canlının ölmesi veya bir şeyin bütünüyle ortadan kalkması sonucunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını bu sonuca götürme, düşme ve kendini tehlikeye atma aşamalarını dışarıda bırakır.","preserves":"Ölüm ve yok oluş sonucunu doğrudan korur."},"facet_ids":["F001"],"text":"ölüp yok olmak","usage_role":"general"},{"applicability":"Bir öznenin başka bir kişiyi öldürdüğü veya ölüm sonucuna götürdüğü bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden ölme veya yok olmayı ve derinliğe düşme yolunu dışarıda bırakır.","preserves":"Başkasının ölümüne neden olma yönünü korur."},"facet_ids":["F001","F002"],"text":"birini ölüme sürüklemek","usage_role":"contextual"},{"applicability":"Dağdan, kuyuya veya başka yüksek bir yerden tehlikeli biçimde düşme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Düşüş olmadan gerçekleşen ölüm ve yok etme kullanımlarını dışarıda bırakır.","preserves":"Derinliğe düşme ve bunun taşıdığı ölüm tehlikesini korur."},"facet_ids":["F003","F004"],"text":"uçuruma düşmek","usage_role":"contextual"}],"definition":"Bir canlının ölmesi veya bir şeyin yok olması, başkasının bu sonuca götürülmesi ve özellikle kuyu ya da uçurum gibi bir derinliğe düşerek ölüm tehlikesine girmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir canlının ölmesi veya bir şeyin varlığını yitirip yok olmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Başka bir özne, kişiyi ya da şeyi öldürerek veya yok ederek bu sonuca götürebilir."},{"facet_id":"F003","role":"specialization","statement":"Kuyuya, dağdan aşağıya veya başka bir derinliğe düşme bu sonuca götüren somut yoldur."},{"facet_id":"F004","role":"extension","statement":"Kişinin kendini ölüm tehlikesine atması, sonuç gerçekleşmeden önceki tehlikeli yönelişi anlatır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Zararsız ve sıradan her türlü düşmeyi dala katar.","collision":null,"fit":"broadening","loses":"Ölüm ve yok oluş sonucunu, başkasını yok etmeyi ve tehlikeye atılmayı yitirir.","preserves":"Kuyuya veya uçuruma düşme yolunu korur."},"text":"düşmek"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yok etme, tehlikeli düşüş ve sonuca henüz varmayan tehlikeye giriş aşamalarını dışarıda bırakır.","preserves":"Dalın temel sonuçlarından biri olan yaşamın sona ermesini korur."},"text":"ölüm"}],"identity_rationale":"Yetkili cümle ölüm veya yok oluş sonucunu, başkasını bu sonuca götürmeyi, kuyuya ya da uçuruma düşmeyi ve kişinin kendini ölüm tehlikesine açmasını birlikte verir. Hazırlanan çerçeve süreç, neden ve sonuç ayrımlarını korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ölüm ve yok oluş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"öldü veya yok oldu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"onu öldürdü veya yok etti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"uçuruma yuvarlanma ve ölüm tehlikesine girme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuyuya düştü"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"dağdan aşağı yuvarlandı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"nereye gittiğini bilmiyorum"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kendini ölüm tehlikelerine atan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kötü ve tiksindirici şey"}],"lexicalization_note":"Dal yalın ölüm ve yok oluş adlarını, eylem biçimlerini ve kuyu ya da dağla kurulan özel söz öbeklerini birlikte içerir; özel düşüş kuruluşları bütün dalın tek anlamı değildir.","neighbor_coverage_note":"Sunulan on iki adayın tümü değerlendirildi. Ölüm, yok oluş ve düşüş sınırlarını ayıran dört aday seçildi; kötülük, karanlık sıkıntı, durgunluk ve aynı kökün taş, hareket, giysi ve artış dalları ya daha uzak kaldı ya da ek bir okuyucu ayrımı sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tehlikeli düşüşü ve sonuca doğru yönelişi kendi sınırına alır; komşu dal ölüm ve öldürme sonucuyla, ayrıca ölüm getiren etkenle daha doğrudan sınırlıdır.","focus_only":"Kuyuya veya uçuruma düşmeyi ve kendini ölüm tehlikesine atmayı da kapsar.","gloss":"ölme ve düşme / ölüme götürme","neighbor_only":"Ölüm getiren kişi veya şeyi ayrı bir özellik olarak daha belirgin biçimde adlandırır.","neighbor_ref":"root_001618/B002","relation_type":"near_synonym","shared_zone":"İki dal da ölme ve başkasını ölüme götürme çekirdeğinde büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın ayırt edici yolu aşağı düşme ve tehlikeye girmedir; komşu dalda temel görünüş bir şeyin gidip ortadan kalkmasıdır.","focus_only":"Derinliğe düşüşü ve kişinin kendini ölüm tehlikesine açmasını içerir.","gloss":"yok olma / çekip gitme ve yok olma","neighbor_only":"Zamanın veya ölümün birini alıp götürmesi gibi uzaklaşma görünüşünü öne çıkarır.","neighbor_ref":"root_001637/B004","relation_type":"near_synonym","shared_zone":"Her iki dal canlı veya nesne için yok olma ve başkası yüzünden yok edilme sonucunu anlatır."},{"boundary_match":"partial","distinction":"Odak dalda düşüş ölüm ve yok oluş yoludur; komşu dalın çekirdeği ise nesnenin düşmesi veya çökmesidir ve ölüm şart değildir.","focus_only":"Düşüşü ölüm veya yok oluş sonucuyla ve ölüm tehlikesiyle bağlar.","gloss":"ölümcül düşüş / çökme","neighbor_only":"Bir yapının çökmesini veya ağacın kökünden sökülmesini sonuç ölüm olmadan anlatabilir.","neighbor_ref":"root_000450/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal aşağı doğru düşme ve yapısal çözülme görünüşünde kesişir."},{"boundary_match":"partial","distinction":"Odak dal yaşamın sona ermesi ve tehlikeli düşüş çevresindedir; komşu dal yapının ya da düzenin dayanağını yitirip çökmesini temel alır.","focus_only":"Canlının ölmesini, başkasını öldürmeyi ve derinliğe düşmeyi birlikte kapsar.","gloss":"ölüp yok olma / yıkılıp çözülme","neighbor_only":"Ev veya düzenin yıkılmasıyla ayakta tutan yapının çözülmesini öne çıkarır.","neighbor_ref":"root_000204/B004","relation_type":"near_neighbor","shared_zone":"İki dal yok oluş, yıkım ve gücün ortadan kalkması alanında buluşur."}],"source_phrase_ar":"الردى وهو الهلاك (maqayis); أرداه الله أهلكه (maqayis); ردى في البئر وتردى إذا سقط في بئر (sihah); التردي هو التهور في مهواة (tahdhib); الردى الهلاك والتردي التعرض للهلاك (mufradat)","source_summary":"Kaynaklar ölüm ve yok oluş sonucunda birleşir; ettirgen kullanım başkasını bu sonuca götürür, düşüş ve tehlikeye atılma ise sonuca giden süreçleri gösterir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الهلاك والإهلاك؛ التردي في مهواة أو بئر أو جبل؛ الذهاب على وجه لا يدرى","what_is_not_ar":"ليس الرداء الملبوس ولا الزيادة ولا الردء المعين"},"support_links":["sup_1f1cf46d2c1b211c0421","sup_8caa746ce075b736baf6","sup_de39739a57bb8925974f"]},{"boundary":"Somut omuz giysisi çekirdektir; borç, süs ve benzeri kullanımlar örtme, bağlı durma veya bezeme benzetmesine dayanır.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"omuz giysisi, onu giyme ve örten ya da bezeyen şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Omuzlar ile boynun birleştiği yere alınarak giyilen dış giysidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu dış giysiyi omuzlara alma ve giyme eylemi aynı dal içinde adlandırılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişiye giysi gibi bağlı duran, onu örten veya bezeyen yükümlülük ve nitelikler benzetmeyle aynı ad altında toplanır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut giysiyi, giyme eylemini ve bu giysiye dayanan bağlılık veya bezeme benzetmelerini birlikte kapsar.","boundary_detail":"Somut omuz giysisi çekirdektir; borç, süs ve benzeri kullanımlar örtme, bağlı durma veya bezeme benzetmesine dayanır.","branch_image_ar":"الرداء وما يلازم المنكبين","concept_gloss":"omuz giysisi, onu giyme ve örten ya da bezeyen şey","contextual_glosses":[{"applicability":"Boyun çevresinden omuzların üzerine alınan somut giysiyi adlandırmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giyme eylemini ve bağlılık ya da bezeme benzetmelerini dışarıda bırakır.","preserves":"Dalın somut giysi çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"omuzlara alınan dış giysi","usage_role":"general"},{"applicability":"Giysinin omuzlara alınıp giyildiği eylem bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysinin nesne adı ile benzetmeli bağlılık ve bezeme kullanımlarını dışarıda bırakır.","preserves":"Somut giysiyi omuzlara alma ve giyme eylemini korur."},"facet_ids":["F001","F002"],"text":"omuz giysisini giymek","usage_role":"contextual"},{"applicability":"Borç, kılıç, kuşak veya gençlik gibi kişiye bağlı duran ya da onu bezeyen şeylerin benzetmeli kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut omuz giysisini ve onu giyme eylemini doğrudan adlandırmaz.","preserves":"Örtme, bağlı durma ve bezeme benzetmesini korur."},"facet_ids":["F003"],"text":"kişiyi örten veya bezeyen şey","usage_role":"explanatory"}],"definition":"Omuzlara alınan dış giysi ve onu giyme eylemidir; benzetmeyle kişiye bağlı duran, onu örten veya bezeyen yükümlülük, nesne ya da nitelik için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Omuzlar ile boynun birleştiği yere alınarak giyilen dış giysidir."},{"facet_id":"F002","role":"associated_use","statement":"Bu dış giysiyi omuzlara alma ve giyme eylemi aynı dal içinde adlandırılır."},{"facet_id":"F003","role":"extension","statement":"Kişiye giysi gibi bağlı duran, onu örten veya bezeyen yükümlülük ve nitelikler benzetmeyle aynı ad altında toplanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bedenin başka yerlerine giyilen her türlü giysiyi kapsama alır.","collision":null,"fit":"broadening","loses":"Omuzlara alınma biçimini, giyme eylemini ve benzetmeli genişlemeleri yitirir.","preserves":"Giyilen bir nesne olma özelliğini korur."},"text":"elbise"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Somut omuz giysisini, giyme eylemini ve yükümlülük gibi süs olmayan bağlılıkları dışarıda bırakır.","preserves":"Kişiyi bezeyen şeylere yönelik benzetmeli yönü korur."},"text":"süs"}],"identity_rationale":"Yetkili cümle omuzlara alınan dış giysiyi, onu giyme eylemini ve kişiye bağlı duran ya da onu bezeyen şeyler için yapılan benzetmeli genişlemeyi açıkça destekler. Kılıç, kuşak ve gençlik gibi örnekler bu çekirdeğe bağlı sözlük birimleri olarak kalır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"omuzlara alınan dış giysi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"omuz giysisini giydi"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"omuz giysisini güzel taşıma biçimi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"iyiliği bol ve eli açık"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"borcu veya yükümlülüğü az"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"boyna bağlı bir yükümlülük olarak borç"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"askılarıyla omuzda taşınan kılıç"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"çapraz takılan kuşak"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"genç kız çapraz kuşak taktı"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gençliğin güzelliği, canlılığı ve esenliği"}],"lexicalization_note":"Yalın giysi adı ile giyme biçimleri ve borç, kılıç, kuşak ya da gençlik üzerinden kurulan özel benzetmeler ayrıdır; benzetmeli kuruluşlar giysinin yalın tanımına katılmaz.","neighbor_coverage_note":"Sunulan on iki adayın tümü değerlendirildi. Beş giysi ve bezeme adayı nesne türü, giyme biçimi ve benzetme sınırlarını açıkladığı için seçildi; başlık, soğuk iklim giysisi ve aynı kökün taş, hareket, yok oluş ve artış dalları ek bir yakınlık göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal somut giysiden kişiye bağlı duran veya onu bezeyen şeylere uzanır; komşu dal giysi türleri ve omuzdan giyme biçimi çevresinde daha geniştir.","focus_only":"Borç, bezeme, kuşak ve gençlik gibi geniş benzetmeli kullanımları kapsar.","gloss":"omuz giysisi / omuzdan alınan giysi","neighbor_only":"Her türlü omuzdan alınan giysiyi ve pelerin benzeri belirli giysi adlarını daha geniş bir giyim sınıfında toplar.","neighbor_ref":"root_001026/B005","relation_type":"near_synonym","shared_zone":"Her iki dal omuzlara alınan dış giysi ve bu giysiyi giyme alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal belirli dış giysiyi ve onun benzetmeli uzantılarını adlandırır; komşu dalın çekirdeği kumaşa sarınma biçimidir.","focus_only":"Omuz giysisinin nesne adını ve ona dayanan benzetmeleri içerir.","gloss":"omuz giysisi / çapraz sarınma","neighbor_only":"Tek bir kumaşı veya giysiyi bedene çapraz biçimde sarınma eylemini öne çıkarır.","neighbor_ref":"root_001163/B005","relation_type":"near_neighbor","shared_zone":"İki dal giysiyi omuz ve gövde çevresine alma biçiminde kesişir."},{"boundary_match":"partial","distinction":"Odak dalda bezeme, omuz giysisinin örten ve kişiye bağlı duran yapısına dayanır; komşu dal süsü bu giysi bağı olmadan genel bir sınıf olarak verir.","focus_only":"Bezeme anlamını omuz giysisi benzetmesinden türetir.","gloss":"giysiyle bezeme / genel süs","neighbor_only":"İçsel, bedensel, dışsal ve dünyaya ilişkin her çeşit süsü genel olarak kapsar.","neighbor_ref":"root_000660/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal kişiyi güzel gösteren veya ona değer katan şeyleri anlatabilir."},{"boundary_match":"field_only","distinction":"Odak giysi omuz ve boyun çevresinde taşınır; komşu giysi daha geniştir ve başı, göğsü veya bedeni kapatma işleviyle ayrılır.","focus_only":"Omuzlara alınan dış giysiyi ve onun benzetmeli kullanımlarını anlatır.","gloss":"omuz örtüsü / uzun dış örtü","neighbor_only":"Baş ve göğsü ya da bütün bedeni örtebilen daha geniş ve uzun bir kadın giysisini anlatır.","neighbor_ref":"root_000252/B004","relation_type":"same_field","shared_zone":"Her iki dal bedeni örten dış giysiler alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal omuzdaki tek giysi parçasına dayanır; komşu dal birden çok parçanın takım oluşturmasını gerektirir.","focus_only":"Tek bir omuz giysisini ve onu giymeyi temel alır.","gloss":"omuz giysisi / giysi takımı","neighbor_only":"Alt ve üst parçadan ya da ikiden çok parçadan oluşan giysi takımını anlatır.","neighbor_ref":"root_000351/B007","relation_type":"same_field","shared_zone":"İki dal giyilen dış örtüler alanında yer alır."}],"source_phrase_ar":"الرداء الذي يلبس (maqayis); تردى وارتدى بمعنى أي لبس الرداء (sihah); يسمى الدين رداء (tahdhib); كل ما زينك فهو رداؤك (tahdhib)","source_summary":"Ortak çizgi omuz giysisi ve onu giymedir; buradan kişiye bağlılık, örtme ve bezeme özelliklerine dayanan benzetmeli kullanımlar gelişir.","sources":["MQ","SI","TA"],"what_is_ar":"الرداء الملبوس؛ التردي والارتداء؛ الردية حسن اللبس؛ الوشاح؛ ما يلزم العنق أو يزين صاحبه كالدين والسيف والشباب","what_is_not_ar":"ليس الردى الهلاك ولا الردى الزيادة ولا الرمي بالحجر"},"support_links":[]},{"boundary":"Önceden var olan sayı, verme veya söz üzerine eklenen fazlalık bu dala girer; genel çokluk, azalma ve kınanan aşırılık ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"belirli bir ölçünün üstüne ekleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Var olan bir ölçünün üzerine ekleme yaparak toplamı büyütmedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir sayının üstüne çıkmak, sayısal kullanımın açık örneğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Verilen paya veya söylenen söze eklenen bölüm de aynı artış ilişkisiyle adlandırılır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sayıya, verilen paya veya söze eklenen bölümün önceki düzeyi yükselttiği bütün dal kullanımlarını kapsar.","boundary_detail":"Önceden var olan sayı, verme veya söz üzerine eklenen fazlalık bu dala girer; genel çokluk, azalma ve kınanan aşırılık ayrı tutulur.","branch_image_ar":"الزيادة على القدر","concept_gloss":"belirli bir ölçünün üstüne ekleme","contextual_glosses":[{"applicability":"Bir toplamın elli gibi belirlenmiş bir sayıyı ekleme yoluyla geçtiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Verilen paya veya söze eklenen bölüm kullanımlarını dışarıda bırakır.","preserves":"Belirli bir sayının üzerine çıkma ilişkisini korur."},"facet_ids":["F001","F002"],"text":"sayının üzerine çıkmak","usage_role":"contextual"},{"applicability":"Birine daha önceki payın üzerinde ek bir şey verme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sayısal eşiği aşma ve söze ek yapma kullanımlarını dışarıda bırakır.","preserves":"Verilen paya yeni bir bölüm eklenmesini korur."},"facet_ids":["F001","F003"],"text":"fazladan vermek","usage_role":"contextual"},{"applicability":"Söylenmiş bir sözün üzerine yeni söz eklendiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sayı ve verilen pay üzerindeki artışları dışarıda bırakır.","preserves":"Sözün önceki içeriğine yeni bölüm eklenmesini korur."},"facet_ids":["F001","F003"],"text":"söze ek yapmak","usage_role":"contextual"}],"definition":"Belirlenmiş bir sayı, pay, verme veya sözün var olan düzeyine yeni bir bölüm ekleyerek onu önceki düzeyinin üstüne çıkarmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Var olan bir ölçünün üzerine ekleme yaparak toplamı büyütmedir."},{"facet_id":"F002","role":"specialization","statement":"Belirli bir sayının üstüne çıkmak, sayısal kullanımın açık örneğidir."},{"facet_id":"F003","role":"extension","statement":"Verilen paya veya söylenen söze eklenen bölüm de aynı artış ilişkisiyle adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kendiliğinden büyüme ve sayıca çoğalma süreçlerini de kapsar.","collision":null,"fit":"broadening","loses":"Belirli bir temel düzeyin üzerine eklenen pay ilişkisini belirsizleştirir.","preserves":"Önceki duruma göre daha çok olma sonucunu korur."},"text":"çoğalma"},{"category":"confusable","error_profile":{"adds":"Kınama, ölçüsüzlük ve yanlış davranış değerlendirmesi ekler.","collision":"Yansız artışı sınırı çiğneyen taşkınlıkla karıştırır.","fit":"broadening","loses":"Yansız biçimde sayı, pay veya söz üzerine ekleme anlamını yitirir.","preserves":"Bir sınırın veya ölçünün üzerine çıkma yönünü korur."},"text":"aşırılık"},{"category":"confusable","error_profile":{"adds":"Değişimin yönünü tersine çevirerek eksiltme bildirir.","collision":"Artışın karşıt yönüyle doğrudan karışır.","fit":"displacement","loses":"Var olan düzeyin üzerine ekleme yönünü bütünüyle yitirir.","preserves":"Aynı ölçü ve değişim alanında yer alır."},"text":"azalma"}],"identity_rationale":"Yetkili cümle belirlenmiş bir sayının üzerine çıkmayı ve verilen şey ya da söze eklenen payı ortak bir artış ilişkisi altında toplar. Hazırlanan dal, artışı kendiliğinden büyümeden ve ölçüyü aşan taşkınlıktan ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ellinin üzerine çıktı"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"ellinin üstüne ekledi"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"artış veya eklenen pay"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"verdiğin ek pay"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"sözüne yaptığın ek"}],"lexicalization_note":"Dal bir yalın artış adını ve sayı, verme ya da sözle kurulan özel söz öbeklerini içerir; bu kuruluşların kapsamı birbirine karıştırılmaz.","neighbor_coverage_note":"Sunulan on iki adayın tümü değerlendirildi. Genel artış, büyüme, sınırı aşma, çokluk ve eksiltme adayları yön ve kapsam ayrımını gösterdiği için seçildi; özel olumsuzlama, değer düşüklüğü ve aynı kökün taş, hareket, yok oluş ve giysi dalları yakın bir anlam sınırı sunmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sayı, verilen pay ve söz üzerine eklenen bölümü belirginleştirir; komşu dal nesne ve sayıda artışı daha genel bir çerçevede ele alır.","focus_only":"Verilen paya ve söze yapılan eki özel kullanım alanları olarak içerir.","gloss":"ölçünün üstüne ekleme / genel artış","neighbor_only":"Nesnenin ya da sayının artışını daha genel verir ve belirli kazanç türlerini de kapsar.","neighbor_ref":"root_000603/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir sayı veya şeyin önceki düzeyinin üzerine çıkmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir temele eklenen bölümü merkeze alır; komşu dal doğal büyüme, verim ve asıldan arta kalan payı da kapsar.","focus_only":"Önceden belirlenmiş sayı, pay veya söz üzerine yapılan eki anlatır.","gloss":"ekleme / büyüme ve verim","neighbor_only":"Ürün, toprak, yiyecek veya sürüde büyüme, verim ve elde kalan fazlayı kapsar.","neighbor_ref":"root_000618/B002","relation_type":"near_synonym","shared_zone":"İki dal önceki duruma göre artış ve fazlalık alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalda artışın yanlış veya aşırı olması gerekmez; komşu dal sınırı aşma ve ölçüsüzlük değerlendirmesini kurucu özellik yapar.","focus_only":"Eklemeyi yansız olarak sayı, verme ve söz alanlarında anlatabilir.","gloss":"artış / ölçüyü aşma","neighbor_only":"Buyrulan veya uygun görülen sınırı aşmayı ve ölçüsüzlüğü içerir.","neighbor_ref":"root_001145/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirlenmiş bir düzeyin üzerine çıkmayı konu edinir."},{"boundary_match":"partial","distinction":"Odak dal eklenen bölüm ile önceki temel arasındaki ilişkiyi gerektirir; komşu dal sonuçtaki çokluğu bu ek ilişkisi olmadan da anlatır.","focus_only":"Bir temel üzerine yapılan tekil eki ve eşiğin geçilmesini anlatır.","gloss":"ek pay / çokluk","neighbor_only":"Bir şeyin çok olmasını, sayıca büyümesini veya çoğaltılmasını genel olarak anlatır.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal niceliğin önceye göre daha büyük olmasıyla ilgilidir."},{"boundary_match":"opposed","distinction":"Odak dal değişimi yukarı yönlü ekleme olarak kurar; komşu dal aynı nicelik alanında azaltma yönünü taşır.","focus_only":"Var olan payın üzerine yeni bir bölüm ekler.","gloss":"artırma / eksiltme","neighbor_only":"Verilen payı azaltır veya eksiltir.","neighbor_ref":"root_000520/B007","relation_type":"polarity_pair","shared_zone":"İki dal verilen payın veya ölçünün nicel değişimini karşıt yönlerde anlatır."}],"source_phrase_ar":"أردى على الخمسين إذا زاد عليها (maqayis); رديت على الخمسين وأرديت أي زدت (sihah); الردى الزيادة (tahdhib); ردى عطائك أي زيادتك في العطية (tahdhib)","source_summary":"Ortak tanıklık, var olan düzeyin üzerine çıkma ve ona ek yapma ilişkisini sayı, verilen pay ve söz alanlarında doğrular.","sources":["MQ","SI","TA"],"what_is_ar":"الزيادة في العدد أو العطاء أو القول","what_is_not_ar":"ليس الردى الهلاك ولا الرداء الملبوس"},"support_links":[]},{"boundary":"Anlam dalı kullanılabilir, ancak tarihsel köken bakımından ters çevrilmiş biçim kaydı korunmalıdır; taş atarak savunma anlamıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000558/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","surface_ar":"تَرَدَّىٰٓ"}],"gloss":"yumuşakça razı etmeye çalışma ve idare etme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiyi yumuşak ve yinelenen bir çabayla istenen şeye razı etmeye çalışmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiyle çatışmak yerine ona yumuşak davranıp ilişkiyi idare ederek geçinmeyi de kapsar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu anlamı taşıyan biçim, seslerin yer değiştirmesiyle oluşmuş ters çevrilmiş bir biçim olarak açıklanır."}}],"root_ar":"ر د ي","root_id":"root_000558","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birini çatışmadan bir şeye yöneltme çabası ile onunla yumuşak davranarak geçinmeyi birlikte kapsar.","boundary_detail":"Anlam dalı kullanılabilir, ancak tarihsel köken bakımından ters çevrilmiş biçim kaydı korunmalıdır; taş atarak savunma anlamıyla birleştirilmez.","branch_image_ar":"المراودة والمداراة","concept_gloss":"yumuşakça razı etmeye çalışma ve idare etme","contextual_glosses":[{"applicability":"Bir kişiyi baskı kurmadan, dolaylı ve yumuşak davranışla istenen şeye yöneltme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyle yalnızca çatışmadan geçinme ve ilişkiyi idare etme yönünü dışarıda bırakır.","preserves":"Sonucu zorlamayan yumuşak razı etme çabasını korur."},"facet_ids":["F001"],"text":"yumuşakça razı etmeye çalışmak","usage_role":"general"},{"applicability":"Bir kişiyle açık çatışmaya girmeden, ilişkiyi incelikli davranışla yürütme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi belirli bir şeye razı etmeye yönelik etkin çabayı dışarıda bırakır.","preserves":"Yumuşak davranma ve çatışmadan geçinme yönünü korur."},"facet_ids":["F002"],"text":"yumuşak davranarak idare etmek","usage_role":"contextual"}],"definition":"Bir kişiyi sertçe karşıya almadan, yumuşak ve dolaylı davranarak bir şeye razı etmeye çalışmak ya da onunla idareli geçinmektir. Kullanılan biçim tarihsel olarak sesleri yer değiştirmiş bir oluşum sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiyi yumuşak ve yinelenen bir çabayla istenen şeye razı etmeye çalışmaktır."},{"facet_id":"F002","role":"specialization","statement":"Kişiyle çatışmak yerine ona yumuşak davranıp ilişkiyi idare ederek geçinmeyi de kapsar."},{"facet_id":"F003","role":"source_variant","statement":"Bu anlamı taşıyan biçim, seslerin yer değiştirmesiyle oluşmuş ters çevrilmiş bir biçim olarak açıklanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Çabanın kesin başarıya ulaştığı sonucunu ekler.","collision":null,"fit":"broadening","loses":"Yumuşak, dolaylı ve süren çabayı ve idareli geçinme yönünü yitirir.","preserves":"Karşı tarafın istenen şeye yönelmesi düşüncesini korur."},"text":"razı etmek"},{"category":"confusable","error_profile":{"adds":"Zaman geçirtme veya işi geciktirme amacı ekler.","collision":"Yumuşak yönlendirmeyi amaçsız geciktirmeyle karıştırır.","fit":"displacement","loses":"Razı etmeye çalışma ve yumuşakça geçinme amaçlarını yitirir.","preserves":"Karşı tarafla dolaylı biçimde ilgilenme görünüşünü kısmen çağrıştırır."},"text":"oyalamak"}],"identity_rationale":"Yetkili cümle bir kişiyi yumuşak ve dolaylı yollarla razı etmeye çalışma ile onunla çatışmadan geçinme anlamlarını destekler. Aynı cümle bu biçimin kökün öz gelişimi değil, seslerin yer değiştirmesiyle oluşmuş ters çevrilmiş bir biçim olduğunu özellikle bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"adamı yumuşakça razı etmeye çalıştı veya idare etti"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"gemin ağızlık parçası için yumuşakça pazarlık edilir"}],"lexicalization_note":"Dal yalnız verilen kişi ve nesne bağlantılı sözlük birimlerinde tanıklanır; bu özel kuruluşlardan bağımsız, sınırsız bir yalın kök anlamı çıkarılmaz.","neighbor_coverage_note":"Sunulan on üç adayın tümü değerlendirildi. Razı etme, yumuşak geçinme ve dolaylı yöneltmenin sınırlarını ayıran beş aday seçildi; hoşnut etme, aracılık, nazikçe başka yöne çevirme ve aynı kökün öteki dalları ya daha sonuç odaklı kaldı ya da ek bir ayrım sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kapsamı genel razı etme ve idareli geçinmedir; komşu dalda yumuşak davranış özellikle kişiyi belirli bir işe katma amacına bağlanır.","focus_only":"Genel olarak razı etmeye çalışma yanında kişiyle yumuşakça geçinmeyi de kapsar.","gloss":"yumuşakça yöneltme / bir işe yöneltme","neighbor_only":"Kişiyi belirli bir işe sokmak için yumuşak davranmayı açık amaç olarak taşır.","neighbor_ref":"root_000611/B006","relation_type":"near_synonym","shared_zone":"Her iki dal kişiyi yumuşak ve dolaylı davranışla istenen yöne çekmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal karşı tarafı yöneltme amacını taşıyabilir; komşu dalın ayırt edici amacı karşı tarafın zararından sakınarak iyi geçinmektir.","focus_only":"Birini belirli bir şeye razı etmeye yönelik etkin çabayı da kapsar.","gloss":"razı etmeye çalışma / sakınarak iyi geçinme","neighbor_only":"Kişinin zararından sakınmak için ona iyi davranma ve çatışmadan kaçınma amacını öne çıkarır.","neighbor_ref":"root_000466/B008","relation_type":"near_synonym","shared_zone":"İki dal da açık çatışma yerine yumuşak davranarak ilişkiyi yürütmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal idare etmenin yanında kişiyi bir şeye razı etme çabasını taşır; komşu dal bu yöneltme şartı olmadan incelikli geçinmeyi anlatır.","focus_only":"Razı etmeye çalışma yönünü ve ters çevrilmiş biçim kaydını içerir.","gloss":"razı etmeye çalışma / incelikle idare etme","neighbor_only":"Yumuşaklık ve incelikle idare etmeyi, ayrıca nazik davranmayı doğrudan merkeze alır.","neighbor_ref":"root_000485/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişiye yumuşak davranarak onunla çatışmadan geçinme anlamında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yöneltme ve razı etme çabasını öne çıkarır; komşu dal örtme ve karşılıklı ilişkiyi sürdürme yönüyle daha geniştir.","focus_only":"Kişiyi bir şeye razı etmeye çalışmayı açıkça içerir.","gloss":"yumuşakça yöneltme / örtülü idare","neighbor_only":"İdare etmenin yanında niyeti veya durumu örtme ve karşılıklı iyi geçinme görünüşlerini kapsar.","neighbor_ref":"root_000853/B010","relation_type":"near_synonym","shared_zone":"İki dal bir kişiyle açık çatışmadan, yumuşak ve dolaylı davranma alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dal davranışın yumuşaklığını ve ilişkiyi idare etmeyi kurucu kılar; komşu dal isteğin çevresinde dönerek yol arama düzenini merkeze alır.","focus_only":"Kişiye yumuşak davranıp onu razı etme veya onunla geçinme tutumunu anlatır.","gloss":"yumuşakça yöneltme / isteğin çevresinde dolanma","neighbor_only":"Bir istek çevresinde dönüp farklı yollardan sonuç arama hareketini anlatır.","neighbor_ref":"root_000372/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişiden istenen sonucu doğrudan baskı kurmadan elde etmeye çalışma alanındadır."}],"source_phrase_ar":"يرادى على فأس اللجام (maqayis;sihah;tahdhib); فليس هذا من الباب لأن هذا مقلوب ومعناه يراود (maqayis); راداه بمعنى داراه (sihah); راديت الرجل وداجيته وداليته وفانيته بمعنى واحد (tahdhib)","source_summary":"Kaynakların ortak tanıklığı yumuşakça razı etmeye çalışma ve idareli davranma anlamlarını verir; biçimin sesleri yer değiştirmiş bir oluşum olduğu kaydı bu anlamın kök içindeki yerini sınırlar.","sources":["MQ","SI","TA"],"what_is_ar":"راديت الرجل بمعنى راودته أو داريته","what_is_not_ar":"ليس راديت عن القوم بمعنى راميت عنهم"},"support_links":[]},{"boundary":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B001","candidate_links":[{"candidate_id":"cand_0b988127058ac570c7a3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi varlık ile ihtiyaç duymama çekirdeğini birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_image_ar":"الغنى والاستغناء","concept_gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","contextual_glosses":[{"applicability":"Bağlam yalnızca para, mal ve maddi bolluk durumunu öne çıkardığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ile bir şey sayesinde yetinme ilişkisini tek başına açıkça vermez.","preserves":"Maddi varlık ve bolluk yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"zenginlik","usage_role":"contextual"},{"applicability":"Kişinin bir şeye ihtiyaç duymaması veya elindekiyle yetinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi servet ve çok sayıda mala sahip olma yönünü zorunlu olarak taşımaz.","preserves":"İhtiyaçtan bağımsızlık ve bir şeyle yetinme yönünü korur."},"facet_ids":["F002","F003"],"text":"kendine yetmek","usage_role":"contextual"}],"definition":"Maddi varlığa ve bolluğa sahip olma, ihtiyaç duymama ya da az ihtiyaç duyma durumudur. Bağıntılı kullanımlarda kişi bir şey sayesinde yetinir veya başka bir şeye gerek duymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."},{"facet_id":"F002","role":"core","statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ve bir şeyle yetinme yönlerini karşılamaz.","preserves":"Maddi mala ve bolluğa sahip olma yönünü korur."},"text":"varlıklılık"},{"category":"confusable","error_profile":{"adds":"Bir şeyin başkası için yeterli olma işlevini çağrıştırır.","collision":"Başkası için yeterli olma dalıyla karışır.","fit":"displacement","loses":"Maddi bolluk ve kişinin ihtiyaçtan bağımsız olma durumunu silikleştirir.","preserves":"İhtiyacın karşılanmış olmasıyla ilgili sınırlı bir yakınlığı korur."},"text":"yeterlilik"}],"identity_rationale":"Kaynak sözü, maddi varlık ve bolluğun yanı sıra ihtiyaç duymama ya da az ihtiyaç duyma durumunu açıkça birlikte verir. Bir şey sayesinde yetinme ve bir şeye gerek duymama anlatımları da bu çekirdeğin bağıntılı kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"maddi zenginlik, bolluk ve ihtiyaçsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"varlıklı, zengin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona ihtiyaç duymamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onunla yetinip başka bir şeye ihtiyaç duymamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye ihtiyaç duymama durumu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"zenginlik ve bolluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gönül tokluğu ve az şeye ihtiyaç duyma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zengin etmek veya yoksunluğunu gidermek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"Kur'an'la yetinip başka bir şeye ihtiyaç duymamak"}],"lexicalization_note":"Yalın biçimler maddi bolluk ve ihtiyaçsızlık durumunu adlandırırken bağıntılı yapılar bir şeyle yetinmeyi veya bir şeye gerek duymamayı belirtir; bu iki kapsam tanımda ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; maddi bolluk, yeterlik ve sonradan zenginleşme sınırlarını en açık gösteren dört karşılaştırma seçildi, yalnızca dar örnek veya uzak alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir sahibin varlık ve ihtiyaçsızlık durumunu anlatır; komşu dal ise bir unsurun başka biri için yeterli olma ve onun işini görme ilişkisini anlatır.","focus_only":"Kişinin maddi bolluğu ve kendisinin ihtiyaçtan bağımsız oluşu bu dala özgüdür.","gloss":"kendine yeterlik ve başkasına yetme","neighbor_only":"Bir şeyin veya kişinin başkası için yeterli olması, yarar sağlaması ve onun yerini tutması komşuya özgüdür.","neighbor_ref":"root_001110/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir ihtiyacın ortadan kalkması veya karşılanması çevresinde buluşur."},{"boundary_match":"partial","distinction":"Komşu dal genişlik ve refahı öne çıkarırken odak dal bunu ihtiyaçların yokluğu veya azalması ve bağımsızlıkla daha sıkı bağlar.","focus_only":"Az ihtiyaç duyma, çok mala sahip olma ve bir şeyle yetinme bağıntıları odakta açıkça yer alır.","gloss":"bolluk ve refah","neighbor_only":"Genel genişlik ve ferahlık anlatımı komşu dalda daha belirgindir.","neighbor_ref":"root_001694/B003","relation_type":"near_synonym","shared_zone":"İki dal da maddi genişlik, refah ve yoksunluktan çıkma durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal zenginliği ihtiyaçtan bağımsızlıkla tanımlar; komşu dal ise birikmiş malın veya başka şeylerin çokluğuna kadar genişleyebilir.","focus_only":"İhtiyaç duymama veya bir şeyle yetinme odak dalın kurucu sınırıdır.","gloss":"zenginlik ve mal çokluğu","neighbor_only":"Her tür çokluk ve malı iyi yönetme anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000459/B001","relation_type":"near_synonym","shared_zone":"Her iki dal maddi varlığın çokluğunu ve zenginliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel ve sürebilen bir zenginlik durumudur; komşu dal aynı sonucu özellikle önceki yoksulluktan sonraki değişim olarak sınırlar.","focus_only":"Öncesinde yoksulluk bulunması gerekmeksizin varlıklı ve ihtiyaçsız olmayı kapsar.","gloss":"zenginlik ve sonradan zenginleşme","neighbor_only":"Yoksulluktan sonra zenginleşme geçişi komşu dalın zorunlu koşuludur.","neighbor_ref":"root_000406/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin zengin duruma gelmesini veya zengin olmasını içerir."}],"source_phrase_ar":"الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)","source_summary":"Kaynakların ortak çerçevesi maddi zenginliği, bolluğu ve ihtiyaçların yokluğunu ya da azalmasını bir araya getirir; ayrıca bir şeyle yetinip başkasına ihtiyaç duymama kullanımını destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغنى في المال والوفر وعدم الحاجة أو قلتها وكثرة القنيات والاستغناء بالشيء أو عنه وتغنى وتغانى بمعنى استغنى","what_is_not_ar":"ليس إجزاء الشيء عن غيره ولا الغناء بالصوت ولا المقام بالمكان"},"support_links":["sup_1f1cf46d2c1b211c0421"]},{"boundary":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_6f7a512a11799e9ec388","lane":"micro"},{"candidate_id":"cand_ae25ea670591c9c755f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir unsurun başkası için hem yeterli hem yararlı olması ve gerektiğinde başka bir unsurun işlevini üstlenmesi için kullanılır.","boundary_detail":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_image_ar":"الغَناء والكفاية","concept_gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","contextual_glosses":[{"applicability":"Bir şeyin miktar veya işlev bakımından ihtiyacı karşılaması öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarar sağlama ve başka bir unsurun yerini tutma yönlerini açıkça belirtmez.","preserves":"Yeterli olma ve ihtiyacı karşılama çekirdeğini korur."},"facet_ids":["F001"],"text":"yetmek","usage_role":"contextual"},{"applicability":"Bir unsurun beklenen yararı sağlaması veya başka bir unsur yerine kullanılabilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yeterlik ile ihtiyacın bütünüyle karşılanmasını zorunlu olarak anlatmaz.","preserves":"Yarar sağlama ve beklenen işlevi yerine getirme yönünü korur."},"facet_ids":["F002","F003"],"text":"işini görmek","usage_role":"contextual"}],"definition":"Bir şeyin ya da kişinin başkası için yeterli olması, onun ihtiyacını karşılaması ve yarar sağlamasıdır; bağlama göre başka bir unsurun işini görüp onun yerini de tutabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."},{"facet_id":"F002","role":"core","statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."},{"facet_id":"F003","role":"extension","statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeterli olma, ihtiyacı karşılama ve başkasının yerini tutma ilişkilerini vermez.","preserves":"Olumlu sonuç ve işe yarama yönünü korur."},"text":"yarar"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel değiştirme ve takas alanıyla karışabilir.","fit":"narrowing","loses":"Yer değiştirme bulunmayan yeterlik ve yarar kullanımlarını dışarıda bırakır.","preserves":"Bir unsurun başka bir unsurun işlevini üstlenmesi yönünü korur."},"text":"yerine geçme"}],"identity_rationale":"Kaynak sözü, bir şeyin ya da kişinin başkası için yeterli olmasını, ihtiyacı karşılamasını, yarar sağlamasını ve gerektiğinde başka bir unsurun yerini tutmasını birlikte verir. Bu nedenle dalın çekirdeği, sahibin zenginliği değil, iki katılımcı arasındaki yeterlik ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yeterlilik, ihtiyacı karşılama ve yarar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu sana yetmez ve yarar sağlamaz"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yeterli ve ihtiyacı karşılayan"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin yerini tutan yeterlilik ve işlev"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"zararını benden uzak tut"}],"lexicalization_note":"Yalın biçimler yeterlik ve yararı adlandırır; bağıntılı yapılar kimin için yeterli olunduğunu, neyin yerini tuttuğunu veya hangi zararın uzak tutulduğunu açıklar.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik, bir şeyle yetinme, başkası adına iş görme ve gerçek değiştirme arasındaki sınırları gösteren dört aday seçildi, daha uzak alan ortaklıkları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir unsurun başkası için yeterli ve yararlı oluşuna dayanır; komşu dal ise işi üstlenip sürdürerek açığı kapatma ve sonuca ulaştırma sürecini öne çıkarır.","focus_only":"Yarar sağlama ve bir kişi ya da şeyin yerini tutma ilişkileri odakta açıkça bulunur.","gloss":"yetme ve işi tamamlayarak yetme","neighbor_only":"Bir işi yürütüp açığı kapatarak amaca ulaşma süreci komşu dalda daha belirgindir.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir ihtiyacın karşılanması ve yeterli sonucun elde edilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel yeterlik ve yararı da içerir; komşu dal yerini tutma ve özellikle bir yükümlülüğü başkası adına yerine getirme ilişkisine daha sıkı bağlıdır.","focus_only":"Bir şeyin yalnızca yeterli veya yararlı olması, yer değiştirme gerçekleşmeden de bu dala girebilir.","gloss":"yetme ve başkasının yerine ödeme","neighbor_only":"Hak, borç veya bağış gibi yükümlülükleri başkası adına yerine getirme komşu dalın ek alanıdır.","neighbor_ref":"root_000244/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir unsurun başka birinin yerini tutup onun adına yeterli olmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yeterli unsur ile yararlanan katılımcı arasındaki ilişkiyi kurar; komşu dal eldeki şeyle yetinme ve başkasından vazgeçebilme sonucunu öne çıkarır.","focus_only":"Bir kişinin ya da şeyin başkası için yararlı ve yeterli olup onun yerini tutması odakta belirgindir.","gloss":"ihtiyacı karşılama ve bir şeyle yetinme","neighbor_only":"Bir şeyle yetinip başka bir şeye gerek duymama sonucu komşu dalda çekirdeğe daha yakındır.","neighbor_ref":"root_000241/B001","relation_type":"near_synonym","shared_zone":"Her iki dal, eldeki bir unsurun ihtiyacı karşılayarak başka bir gereği ortadan kaldırmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal işlev bakımından yetmeyi anlatır; komşu dal ise bir unsurun yerine diğerini koyma veya onları değiştirme işlemini anlatır.","focus_only":"Yeterli olma ve yarar sağlama, gerçek bir değiştirme işlemi olmadan da gerçekleşebilir.","gloss":"işlevsel yeterlik ve değiştirme","neighbor_only":"Bir unsurun çıkarılıp yerine başka bir unsurun konması ve karşılıklı değiştirme komşu dala özgüdür.","neighbor_ref":"root_000095/B001","relation_type":"near_neighbor","shared_zone":"Bir unsurun başka bir unsurun konumunu veya işlevini üstlenmesi iki dalda da görülebilir."}],"source_phrase_ar":"الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)","source_summary":"Kaynaklar yeterli olma, ihtiyacı karşılama, yarar sağlama ve başkasının yerini tutma yönlerinde birleşir; olumsuz yapılarda aynı ilişki yetersizlik veya yararsızlık olarak görünür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يكفي الشيء أو الشخص غيره ويجزئ عنه وينفعه ويقوم مقامه","what_is_not_ar":"ليس اليسار والوفر ولا الغناء بالصوت ولا سكنى المكان"},"support_links":["sup_de39739a57bb8925974f","sup_e686bb7ff19c95ffeeef"]},{"boundary":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ses üretme, dinleme ve özel metin okuma yönlerini birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_image_ar":"الغِناء والصوت","concept_gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","contextual_glosses":[{"applicability":"İnsan sesiyle ezgili bir parça seslendirme eylemi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinleme ile metni hüzünlü ve yumuşak sesle okuma yönlerini dışarıda bırakır.","preserves":"Sesle ezgi üretme ve ezgili parça yönlerini korur."},"facet_ids":["F001","F002"],"text":"şarkı söylemek","usage_role":"contextual"},{"applicability":"Bir metnin sesi yumuşatıp duygulandırarak ezgili biçimde okunması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel şarkı söyleme, ezgili parça ve dinleme alanlarını kapsamaz.","preserves":"Okuyuşta ezgi, hüzün ve ses yumuşaklığı yönünü korur."},"facet_ids":["F003"],"text":"ezgili okumak","usage_role":"contextual"}],"definition":"Sesle ezgi söyleme, söylenen ezgili parça ve bunu dinleme alanıdır. Okuyuşu ezgili, hüzünlü ve yumuşak bir sesle gerçekleştirme bunun özel bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."},{"facet_id":"F003","role":"specialization","statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İnsan sesi bulunmayan çalgısal üretim ve düzenleme alanlarını da kapsar.","collision":"Çalgı müziğiyle gereksiz bir kapsam çakışması doğurur.","fit":"broadening","loses":null,"preserves":"Ezgi ve işitsel sanat alanıyla olan bağı korur."},"text":"müzik"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söyleme ve dinleme etkinliğiyle özel ezgili okuma kullanımını tek başına karşılamaz.","preserves":"Ezgili söylenen parça yönünü güçlü biçimde korur."},"text":"şarkı"}],"identity_rationale":"Kaynak sözü sesle ezgi söylemeyi, söylenen ezgili parçayı ve dinlemeyi açıkça bu dalda toplar. Okuyuşu ezgili, hüzünlü ve yumuşak seslendirme ise aynı ses kullanımının özel bir uygulamasıdır, dalın bütününü tek başına tanımlamaz.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarkı söyleme, ezgili seslendirme ve dinleti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"şarkı; ezgili söylenen parça"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"şarkı söylemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"şarkı söylemek veya sesi ezgili ve duygulu kullanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak"}],"lexicalization_note":"Yalın biçimler şarkı söyleme, ezgili parça ve dinletiyi adlandırır; belirli metni ezgili okuma anlamı yalnızca ilgili bağıntılı yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hoş insan sesi, özel yolcu ezgisi, ses yineleme ve çalgı sesiyle sınırı en iyi gösteren dört aday seçildi, yalnızca yüksek ses veya uzak konu ortaklığı sunanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şarkı söyleme, parça, dinleme ve özel okuma kullanımını toplar; komşu dal özellikle hoş işitilen ses niteliği ve bunu üreten kişiye yönelir.","focus_only":"Ezgili parça ile metni hüzünlü ve yumuşak sesle okuma kullanımı odakta açıkça bulunur.","gloss":"şarkı ve hoş ezgili ses","neighbor_only":"Sesin hoş ve zevk verici niteliği ile icracıyı adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_000741/B007","relation_type":"near_synonym","shared_zone":"İki dal da insan sesiyle üretilen hoş ezgiyi ve şarkı söylemeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal geniş sesli ezgi alanını anlatır; komşu dal bunu yüksek sesli ve yolculukla ilişkili belirli bir söyleyiş türüyle sınırlar.","focus_only":"Genel şarkı söyleme, ezgili parça, dinleme ve yumuşak okuyuş odak dalda yer alır.","gloss":"genel şarkı ve yolcu ezgisi","neighbor_only":"Yolcuların yüksek sesle söylediği çağrı ve belirli ezgi türü komşuya özgüdür.","neighbor_ref":"root_001507/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal insan sesiyle ezgili söyleme etkinliğine girer."},{"boundary_match":"partial","distinction":"Odak dal ezgi üretimi ve dinlemeyi tanımlar; komşu dal sesin yinelenmesi veya geri döndürülmesi biçimine dayanır ve ezgi gerektirmez.","focus_only":"Ezgili parça ve şarkı söyleme etkinliği odak dalın merkezindedir.","gloss":"ezgili söyleme ve ses yineleme","neighbor_only":"Çağrı, gök gürültüsü ve başka seslerde yineleme veya yankılanma komşu dalın ek kapsamıdır.","neighbor_ref":"root_000544/B007","relation_type":"near_neighbor","shared_zone":"Şarkı ve okuma sırasında sesin düzenli biçimde çevrilmesi iki dalda kesişebilir."},{"boundary_match":"field_only","distinction":"Odak dal insan sesi ve şarkıya dayanır; komşu dalın çekirdeği üflemeli çalgıdan çıkan sestir ve insan sesi zorunlu değildir.","focus_only":"İnsan sesiyle şarkı söyleme ve metni ezgili okuma odak dalın çekirdeğidir.","gloss":"insan sesi ve çalgı sesi","neighbor_only":"Üflemeli çalgıyla ses üretme ve aynı sözcüğün bazı hayvan seslerine uygulanması komşuya özgüdür.","neighbor_ref":"root_000643/B002","relation_type":"same_field","shared_zone":"İki dal ezgili veya hoş işitilebilen ses üretimi alanında buluşur."}],"source_phrase_ar":"الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)","source_summary":"Kaynaklar insan sesiyle ezgi söyleme, ezgili parça ve dinleme anlamlarında birleşir; ayrıca okuyuştaki ezgili, hüzünlü ve yumuşak seslendirmeyi özel bir kullanım olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغناء بالصوت والأغنية والسماع والتطريب وتحزين القراءة وترقيقها","what_is_not_ar":"ليس الغنى في المال ولا الغَناء بمعنى الكفاية ولا المقام بالمكان"},"support_links":[]},{"boundary":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B004","candidate_links":[{"candidate_id":"cand_d80164acff3c3d291407","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"bir yerde uzun süre kalıp yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, süre ve yaşama katılımlarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_image_ar":"الغنى بالمكان","concept_gloss":"bir yerde uzun süre kalıp yaşama","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun belirli bir yeri yaşama yeri edinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süre kalma vurgusunu ve bundan doğan yer adlarını açıkça vermez.","preserves":"Belirli bir yerde yaşama ve yerle bağ kurma yönünü korur."},"facet_ids":["F001"],"text":"bir yerde oturmak","usage_role":"contextual"},{"applicability":"Kalınan yer ile kalış süresinin öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Orada yaşama ile ev veya yer adı türetme yönlerini zorunlu olarak taşımaz.","preserves":"Belirli yerde kalma ve süreklilik yönünü korur."},"facet_ids":["F001"],"text":"uzun süre kalmak","usage_role":"contextual"},{"applicability":"Geçmişte bir yerde bulunmuş ve yaşamış olmanın sonradan yokluğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel uzun süre kalma çekirdeği ile konut ve eylem adlarını kapsamaz.","preserves":"Geçmişte o yerde yaşama veya bulunma yönünü korur."},"facet_ids":["F002"],"text":"orada yaşamış olmak","usage_role":"contextual"}],"definition":"Bir yerde oturmak, orada uzun süre kalmak ve yaşamak anlamıdır. Geçmişte orada bulunmuş olma anlatımı ile bir topluluğun oturduğu evleri, kalma eylemini veya kalınan yeri bildiren adlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süreli oturma, yaşama ve o yerin ev sayılması yönlerini zayıflatır.","preserves":"Belirli bir yerde kalma yönünü korur."},"text":"konaklamak"},{"category":"alternative","error_profile":{"adds":"Başlangıçtaki taşınma ve kalıcı düzen kurma olayını öne çıkarır.","collision":"Yer edinme eylemiyle kalış durumunu birbirine yaklaştırır.","fit":"displacement","loses":"Geçmişte bulunmuş olma ve yalnızca uzun süre kalma kullanımlarını daraltır.","preserves":"Bir yeri yaşama yeri edinme yönünü korur."},"text":"yerleşmek"}],"identity_rationale":"Kaynak sözü bir yerde oturup uzun süre kalmayı çekirdek olarak verir; orada yaşamış veya bulunmuş olma anlatımı ile oturulan ev ve yer adları bu çekirdekten doğan kullanımlardır. Bu nedenle geçici bulunma ile konut adı aynı düzeyde tek anlam sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturmak ve uzun süre kalmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sanki daha dün orada hiç yaşamamıştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir topluluğun oturduğu evler ve yurtlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturma eylemi veya oturulan yer"}],"lexicalization_note":"Bir yerde uzun kalma ve geçmişte orada yaşama anlamları belirli bağıntılı yapılarda görünür; yalın ad biçimleri ise kalma eylemini veya oturulan yeri gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; uzun kalış, genel kalma, konut edinme ve oturma duruşu arasındaki sınırı gösteren beş aday seçildi, yalnızca yer adı veya uzaktan alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama, geçmişte bulunma ve konut adlarına uzanır; komşu dal ise yerleşik kalmayı farklı kişi durumlarına ve özel kalış bağlamlarına genişletir.","focus_only":"Topluluğun evleri ile kalma eylemini veya yerini adlandıran biçimler odakta bulunur.","gloss":"uzun süre yaşama ve yerleşik kalma","neighbor_only":"Yabancının kalışı, kutsal yerde komşuluk, hapiste kalma ve öldürülmüş kişi kullanımları komşuya özgüdür.","neighbor_ref":"root_000211/B001","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir yerde oturma, kalma ve özellikle uzun süren yerleşikliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal uzun yaşama ile bundan doğan ev ve yer adlarını toplar; komşu dal aynı alanı durma, bekleme ve soyut yerleşiklik kullanımlarına taşır.","focus_only":"Geçmişte orada yaşamış olma ve topluluğun evlerini adlandırma odakta belirgindir.","gloss":"oturma ve yerleşik kalma","neighbor_only":"Durma, ağırdan alma ve eskiden beri yerleşmiş bir iş anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000536/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir yerde oturma, ev ve yerleşik kalma alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreyi, yaşamayı ve bağlı yer adlarını içerir; komşu dal ise süre veya konut sonucu belirtmeden bir yerde kalma eylemiyle sınırlıdır.","focus_only":"Uzun süre yaşama, geçmişte bulunma ve oturulan evleri adlandırma odakta yer alır.","gloss":"uzun süre yaşama ve bir yerde kalma","neighbor_only":"Komşu dal yalnızca bir yerde kalmayı bildiren daha dar bir eylem çerçevesidir.","neighbor_ref":"root_000168/B016","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin belirli bir yerde kalmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sürmekte olan kalış ve yaşam durumunu anlatır; komşu dal ise yeri konut seçme ya da başkasına konut sağlama işlemini öne çıkarır.","focus_only":"Bir yerde fiilen uzun süre yaşama ve geçmişte orada bulunmuş olma odak dalın merkezidir.","gloss":"orada yaşama ve konut edinme","neighbor_only":"Bir yeri konut edinme veya birini bir yere yerleştirme işlemi komşu dalda belirgindir.","neighbor_ref":"root_000162/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişi ile yaşadığı yer arasında kalıcı veya uzun süreli bir bağ kurar."},{"boundary_match":"partial","distinction":"Odak dal yaşama yeri ve uzun kalışla ilgilidir; komşu dal bedenin oturma duruşunu ve bu duruş çevresindeki birlikteliği anlatır.","focus_only":"Yerde uzun süre yaşama ve o yeri konut edinme odak dala özgüdür.","gloss":"bir yerde yaşama ve oturma duruşu","neighbor_only":"İnsan bedeninin oturma duruşu, oturum ve birlikte oturma komşu dalın çekirdeğidir.","neighbor_ref":"root_000254/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda kişi bir yerde bulunur ve o yere bağlı bir süreklilik gösterebilir."}],"source_phrase_ar":"غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)","source_summary":"Kaynaklar bir yerde oturma ve uzun süre kalma çekirdeğinde birleşir; geçmişte orada yaşama anlatımını, topluluğun evlerini ve hem eylemi hem yeri gösterebilen adları da bu alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإقامة وطول المقام في الدار أو المحلة والمغاني منازل القوم والمغنى للمصدر أو المكان وما يقرب من العيش والكون السابق","what_is_not_ar":"ليس الغنى في المال ولا الكفاية ولا الغناء بالصوت"},"support_links":["sup_8caa746ce075b736baf6"]},{"boundary":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_kind":"bare","branch_ref":"root_001110/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana açıklama ile kaynaklarda görülen daha geniş kadın nitelemelerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_image_ar":"الغانية المستغنية","concept_gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","contextual_glosses":[{"applicability":"Nitelemenin kadının kendi güzelliği sayesinde süslenmeye gerek duymaması açıklamasına dayandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde bağımsızlık ile yalnız gençlik, evlilik veya genel kadın kullanımını dışarıda bırakır.","preserves":"Güzellik nedeniyle süsten bağımsız sayılma yönünü açıkça korur."},"facet_ids":["F001"],"text":"güzelliğiyle süse ihtiyaç duymayan kadın","usage_role":"explanatory"},{"applicability":"Kaynak sınırının gençlik ve güzellik özelliklerine dayandığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş veya güzellik sayesinde süsten bağımsız olma açıklamasını ve genel kadın kullanımını vermez.","preserves":"Gençlik ve güzellik temelli kaynak çeşidini korur."},"facet_ids":["F002"],"text":"genç ve güzel kadın","usage_role":"contextual"},{"applicability":"Nitelemenin yalnızca evlilik durumuna göre sınırlandığı kaynak kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güzellik, gençlik, süsten bağımsızlık ve evli olmayan kadın kullanımlarını dışarıda bırakır.","preserves":"Evlilik koşuluna dayanan dar kaynak çeşidini korur."},"facet_ids":["F002"],"text":"evli kadın","usage_role":"contextual"}],"definition":"Eşi sayesinde takıya gerek duymadığı veya güzelliği nedeniyle süslenmeye ihtiyaç duymadığı düşünülen kadını anlatan bir nitelemedir. Kullanım sınırı bazı kaynaklarda genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın olacak kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."},{"facet_id":"F003","role":"source_variant","statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde süsten bağımsızlık, evlilik, gençlik ve koşulsuz kadın kullanımlarını dışarıda bırakır.","preserves":"Güzellik özelliğine dayanan kullanımı korur."},"text":"güzel kadın"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evli olmayan güzel kadın, süsten bağımsız kadın ve genel kadın kullanımlarını kapsamaz.","preserves":"Gençlik ile evliliği birlikte arayan dar kaynak çeşidini korur."},"text":"evli genç kadın"}],"identity_rationale":"Kaynak sözü, eşi veya güzelliği sayesinde takı ve süslenmeye ihtiyaç duymadığı düşünülen kadın açıklamasını güçlü biçimde destekler; ancak bütün tanımlar bu sınırı korumaz. Bazı kullanımlar genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın düzeyine kadar genişler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar"}],"lexicalization_note":"Tanım yalın kadın nitelemesine bağlıdır; eşi, güzelliği, gençliği veya evliliği anlatan sınır çeşitleri korunur ve başka dallardaki evlenme olayına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ihtiyaçsızlık, genç ve güzel kadın, süs eşyası ve evlilik durumu ile sınırı gösteren dört aday seçildi, yalnızca aynı toplumsal sahneyi paylaşan daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli ve sınırları değişken bir kadın adıdır; komşu dal ise cinsiyet veya niteleme sınırlaması olmadan zenginlik ve ihtiyaçsızlık durumunu anlatır.","focus_only":"Belirli bir kadın nitelemesi ve bunun gençlik, güzellik veya evlilik sınırları odak dala özgüdür.","gloss":"kadın nitelemesi ve genel ihtiyaçsızlık","neighbor_only":"Genel maddi bolluk, mal çokluğu ve herhangi bir kişinin ihtiyaçtan bağımsızlığı komşu dalın kapsamıdır.","neighbor_ref":"root_001110/B001","relation_type":"near_neighbor","shared_zone":"Kadının eşi veya güzelliği sayesinde süse ihtiyaç duymadığı açıklaması, ihtiyaçtan bağımsızlık düşüncesiyle kesişir."},{"boundary_match":"partial","distinction":"Odak dalın ana açıklaması eş veya güzellik sayesinde süsten bağımsızlıktır ve sınırı değişkendir; komşu dal doğrudan gençlik ve güzelliği bildirir.","focus_only":"Eş veya güzellik sayesinde süse ihtiyaç duymama ve evlilik sınırı odakta bulunabilir.","gloss":"süsten bağımsız kadın ve genç güzel kız","neighbor_only":"Genç ve güzel kız olma, başka bir gerekçe aranmadan komşu dalın doğrudan çekirdeğidir.","neighbor_ref":"root_000610/B008","relation_type":"near_neighbor","shared_zone":"İki dal da genç ve güzel bir kadını nitelemek için kullanılabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal bir kadını süse gerek duymama veya başka özelliklerle niteler; komşu dal ise süs eşyasını ve süslenme eylemini anlatır.","focus_only":"Süse ihtiyaç duymadığı düşünülen kadının kendisi odak dalda adlandırılır.","gloss":"süsten bağımsız kadın ve süs eşyası","neighbor_only":"Takı ve süs eşyasının kendisi ile bunları takma eylemi komşu dalda adlandırılır.","neighbor_ref":"root_000353/B001","relation_type":"thematic","shared_zone":"Her iki dal kadın, takı ve süslenme durumunun aynı sahnesinde yer alır."},{"boundary_match":"field_only","distinction":"Odakta evlilik yalnızca değişken sınırlardan biridir; komşu dal ise önceki evlilik veya birleşme sonrasındaki medeni durumu doğrudan tanımlar.","focus_only":"Güzellik, gençlik veya eş sayesinde süsten bağımsızlıkla kurulan kadın nitelemesi odakta yer alır.","gloss":"kadın nitelemesi ve önceki evlilik durumu","neighbor_only":"Evlilik ilişkisinin sona ermesi ya da evlilikte cinsel birleşme sonrası kazanılan durum komşuya özgüdür.","neighbor_ref":"root_000209/B005","relation_type":"same_field","shared_zone":"Her iki dal bir kadını evlilik durumu üzerinden niteleyebilir."}],"source_phrase_ar":"الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)","source_summary":"Kaynaklar kadın nitelemesinde birleşir, fakat sınırı farklı kurar: eşi veya güzelliği nedeniyle süse ihtiyaç duymama ana açıklamadır; gençlik, güzellik, evlilik ve koşulsuz kadın kullanımları daha geniş çeşitlerdir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغانية والغواني على اختلاف تفسيرها بالمتزوجة أو الشابة أو الحسناء أو من استغنت بزوجها أو حسنها عن الزينة","what_is_not_ar":"ليس الغناء بالصوت ولا مطلق الغنى في المال ولا التزويج نفسه"},"support_links":[]},{"boundary":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_kind":"bare","branch_ref":"root_001110/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","surface_ar":"يُغْنِى"}],"gloss":"evlenme ve evlendirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik bağının kurulmasını hem kişinin kendisi hem de bir başkasını evlendiren katılımcı açısından kapsar.","boundary_detail":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_image_ar":"الغنى والتزويج","concept_gloss":"evlenme ve evlendirme","contextual_glosses":[{"applicability":"Kişinin evlenmesi veya evlilik durumuna girmesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını evlendirme ve evliliği koruyucu sayma yönlerini dışarıda bırakır.","preserves":"Kişinin evlenmesi ve evlilik bağının kurulması yönünü korur."},"facet_ids":["F001"],"text":"evlilik bağı kurmak","usage_role":"contextual"},{"applicability":"Ettirgen kullanımda bir gelin için evlilik bağı kurulması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi evlenmesini ve evliliğin koruyucu sayılmasını kapsamaz.","preserves":"Bir başkasını, özellikle gelini, evlendirme yönünü korur."},"facet_ids":["F002"],"text":"bir gelini evlendirmek","usage_role":"contextual"}],"definition":"Evlilik bağı kurma veya birini, özellikle bir gelini, evlendirme anlamıdır. Evlilik ayrıca bekâr kişiyi koruyan bir güvence olarak tasarlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."},{"facet_id":"F003","role":"associated_use","statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kutlama ve tören olayını zorunluymuş gibi öne çıkarır.","collision":"Evlilik bağı ile düğün törenini birbirine karıştırır.","fit":"displacement","loses":"Evlilik bağını kurma ve birini evlendirme işlemlerini hukuki ve ilişkisel yönleriyle vermez.","preserves":"Evlilik çevresindeki toplumsal olaya gönderme yapar."},"text":"düğün"}],"identity_rationale":"Kaynak sözü evlenmeyi, gelinleri evlendirmeyi ve evliliğin bekâr kişi için koruyucu bir durum sayılmasını aynı dalda açıkça verir. Kadın nitelemesi, maddi zenginlik ve sesle ezgi anlamları bu çekirdeğin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"evlenme; bekâr kişi için koruyucu sayılan evlilik"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gelinleri evlendirme"}],"lexicalization_note":"Tanım yalın ad ve ettirgen biçimlerin evlenme ile evlendirme anlamlarını kapsar; düğün töreni, eşin kendisi veya evliliğin sonraki aşamaları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; evlilik sözleşmesi, eş edinme, birlikte yaşama aşaması, örtülü evlilik anlatımı ve kadın nitelemesiyle sınırı gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal evlenme ile başkasını evlendirmeyi birlikte kapsar; komşu dal özellikle evlilik sözleşmesini ve bu sözleşmeyle evlenmeyi öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği bekâr için koruyucu sayma yönleri odakta bulunur.","gloss":"evlenme ve evlilik sözleşmesi","neighbor_only":"Evlilik sözleşmesinin kendisini doğrudan adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_001548/B002","relation_type":"near_synonym","shared_zone":"Her iki dal evlilik bağının kurulmasını ve kişinin evlenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal evlilik bağını kurma ve kurdurma olayını anlatır; komşu dal eş ve aile edinme sonucunu öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği koruyucu bir güvence sayma odak dala özgüdür.","gloss":"evlenme ve eş edinme","neighbor_only":"Eş edinerek aile sahibi olma ve kişiye bir eş verilmesi komşu dalda daha belirgindir.","neighbor_ref":"root_000064/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin evlenerek bir eş ve aile bağı edinmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bağın kurulmasını anlatır; komşu dal ise kurulmuş evliliğin ardından eşlerin bir araya gelmesi ve ortak yaşama geçmesi aşamasına yönelir.","focus_only":"Evlilik bağını kurma ve bir başkasını evlendirme odak dalın çekirdeğidir.","gloss":"evlenme ve eşlerin birleşmesi","neighbor_only":"Evliliğin ardından eşlerin birlikte yaşamaya başlaması ve gelinin eve getirilmesi komşuya özgüdür.","neighbor_ref":"root_000156/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal evlilik sürecinin birbirine yakın aşamalarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan evlenme ve evlendirme anlamındadır; komşu dal örtülü bir anlatımla evlilikten cinsel birleşmeye kadar genişleyebilir.","focus_only":"Bir başkasını evlendirme ve koruyucu evlilik düşüncesi odak dalda açıkça yer alır.","gloss":"evlilik bağı ve evlilik için örtülü anlatım","neighbor_only":"Evlilik yanında cinsel birleşmeye kadar uzanan örtülü kullanım komşu dalın ek kapsamıdır.","neighbor_ref":"root_000161/B005","relation_type":"near_neighbor","shared_zone":"İki dal da evlenme anlamını veya evliliğe gönderme yapan bir kullanımı kapsar."},{"boundary_match":"field_only","distinction":"Odak dal bir olay ve ilişki kurma sürecidir; komşu dal ise evli olabilen veya başka özelliklerle tanımlanan bir kadın adıdır.","focus_only":"Evlilik bağını kurma veya birini evlendirme olayı odak dala özgüdür.","gloss":"evlenme olayı ve kadın nitelemesi","neighbor_only":"Evlilik, güzellik veya gençlik üzerinden tanımlanan kadın nitelemesi komşu dala özgüdür.","neighbor_ref":"root_001110/B005","relation_type":"same_field","shared_zone":"Her iki dal evlilik ve kadınla ilgili aynı toplumsal alan içinde yer alabilir."}],"source_phrase_ar":"الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kullanım, evlenmeyi ve gelinleri evlendirmeyi anlatır; evliliği de bekâr kişi için koruyucu bir güvence sayar."}],"source_summary":"Bu dalda ad ve ettirgen biçim, evlilik bağı kurma çevresinde birleşir; koruma düşüncesi evlenmenin sonucu olarak sunulur.","sources":["TA"],"what_is_ar":"يدخل فيه الغنى بمعنى التزويج والأغناء بمعنى إملاكات العرائس وجعل التزويج حصنا للعزب","what_is_not_ar":"ليس الغانية نفسها ولا الغناء بالصوت ولا الغنى في المال"},"support_links":[]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_6f7a512a11799e9ec388","lane":"micro"},{"candidate_id":"cand_0b988127058ac570c7a3","lane":"micro"},{"candidate_id":"cand_d80164acff3c3d291407","lane":"micro"},{"candidate_id":"cand_ae25ea670591c9c755f9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:11:4:1","qac_word_ref":"92:11:4","surface_ar":"مَالُ"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_1f1cf46d2c1b211c0421","sup_8caa746ce075b736baf6","sup_de39739a57bb8925974f","sup_e686bb7ff19c95ffeeef"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:11:4:1","qac_word_ref":"92:11:4","surface_ar":"مَالُ"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:11:1"],"branch_refs":[],"candidate_id":"cand_193ec5fe8b237d882c72","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:1:connective-circumstantial-range","source_type":"word_analysis","support_ids":["sup_3ad5458ff18a3c2bc27f","sup_48ceb3028ede47867f80"],"title":"continuation with circumstantial pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:1","qac_refs":["92:11:1:1"],"status":"accepted"}},{"anchor_refs":["92:11:1"],"branch_refs":[],"candidate_id":"cand_a2d299fa78f025ae326f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:1:continuation-frame","source_type":"word_analysis","support_ids":["sup_3ad5458ff18a3c2bc27f","sup_c0e4337baf667ca35f40"],"title":"opening connector carries the prior consequence forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:1","qac_refs":["92:11:1:1"],"status":"accepted"}},{"anchor_refs":["92:11:1"],"branch_refs":[],"candidate_id":"cand_62a3f6c2712c40ad70bb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:1:fused-negative-onset","source_type":"word_analysis","support_ids":["sup_3ad5458ff18a3c2bc27f","sup_8f92780828b80b288f0d"],"title":"connector enters as a bound launch into negation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:1","qac_refs":["92:11:1:1"],"status":"accepted"}},{"anchor_refs":["92:11:2"],"branch_refs":[],"candidate_id":"cand_2264cda03404bfe202e8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:2:delayed-wealth-reversal","source_type":"word_analysis","support_ids":["sup_16e283550b431bf57d80","sup_2c348893c5bdb814f5d6"],"title":"wealth arrives after its failure has begun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:2","qac_refs":["92:11:1:2"],"status":"accepted"}},{"anchor_refs":["92:11:2"],"branch_refs":[],"candidate_id":"cand_73c84e39b5ca80a35f2a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:2:factual-atemporal-denial","source_type":"word_analysis","support_ids":["sup_16e283550b431bf57d80","sup_eb877f0e5b3d16e452ba"],"title":"factual denial rather than command or question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:2","qac_refs":["92:11:1:2"],"status":"accepted"}},{"anchor_refs":["92:11:2"],"branch_refs":[],"candidate_id":"cand_c3c274e52c24f37fdfcb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:2:quick-negative-onset","source_type":"word_analysis","support_ids":["sup_16e283550b431bf57d80","sup_f1efdf18f8c631863012"],"title":"short particles make a clipped negative entry","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:2","qac_refs":["92:11:1:2"],"status":"accepted"}},{"anchor_refs":["92:11:2"],"branch_refs":[],"candidate_id":"cand_2983a90a53813639ca15","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:2:whole-predicate-negation","source_type":"word_analysis","support_ids":["sup_16e283550b431bf57d80","sup_cdea2b293a3c44e01942"],"title":"negation scopes over the availing predication","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:2","qac_refs":["92:11:1:2"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_f99cdad4d20d5ed69cb0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:governed-beneficiary-frame","source_type":"word_analysis","support_ids":["sup_6bbf7ff713560bcfdf54","sup_ec8947367fbccd7308d4"],"title":"availing is aimed toward a governed person","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_2932a2bb54a1a2d2f2f3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:negated-form-iv-capability","source_type":"word_analysis","support_ids":["sup_970b3208e66e7ba94b2b","sup_ec8947367fbccd7308d4"],"title":"causative capability is denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_c9818ad51000924b7209","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:nonlocal-root-branches","source_type":"word_analysis","support_ids":["sup_066c255ed5fcec2b2e34","sup_ec8947367fbccd7308d4"],"title":"broader root branches are not selected here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_28e1b470ceab32f45ef5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:same-root-reversal-from-92-8","source_type":"word_analysis","support_ids":["sup_7be83388caedde8147c3","sup_ec8947367fbccd7308d4"],"title":"earlier self-sufficiency is reversed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_4bd451bbedd82ddc38d9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:two-beat-disclosure","source_type":"word_analysis","support_ids":["sup_391ed70a512d8e676717","sup_ec8947367fbccd7308d4"],"title":"negated efficacy becomes visible at the crisis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:3"],"branch_refs":[],"candidate_id":"cand_a62b92de621054be257b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:3:wealth-sufficiency-pair","source_type":"word_analysis","support_ids":["sup_2baf1416e6bdfae3757a","sup_ec8947367fbccd7308d4"],"title":"wealth and sufficiency are clause-bound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:3","qac_refs":["92:11:2:1"],"status":"accepted"}},{"anchor_refs":["92:11:4"],"branch_refs":[],"candidate_id":"cand_9054553740203de9a89b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:4:failed-beneficiary-complement","source_type":"word_analysis","support_ids":["sup_d6de499146ae2fbdd6ee","sup_d7987bf7d5766f68a7dc"],"title":"preposition marks the protected party","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:4","qac_refs":["92:11:3:1","92:11:3:2"],"status":"accepted"}},{"anchor_refs":["92:11:4"],"branch_refs":[],"candidate_id":"cand_a557a5edf7a7fdbb0083","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:4:pronoun-chain","source_type":"word_analysis","support_ids":["sup_218e54f44ffaa6cbc786","sup_d7987bf7d5766f68a7dc"],"title":"suffix continues the prior participant","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:4","qac_refs":["92:11:3:1","92:11:3:2"],"status":"accepted"}},{"anchor_refs":["92:11:4"],"branch_refs":[],"candidate_id":"cand_1e90f6123a622ae0b5bd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:4:relation-referent-fusion","source_type":"word_analysis","support_ids":["sup_171a4fd03b7338c3b252","sup_d7987bf7d5766f68a7dc"],"title":"relation and referent are fused in one word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:4","qac_refs":["92:11:3:1","92:11:3:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_cb5793695cab86f8520b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:delayed-possessed-subject","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_e46c4653551ed3f32290"],"title":"his wealth is the delayed failed subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_f397905f8fa5767d6c41","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:material-stockpile-range","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_e1b52da8732027ed731c"],"title":"wealth is concrete accumulated property","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_8a67ad0a61e29c29aca0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:personal-ownership-irony","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_2fb35e31f1bf4adb8310"],"title":"the resource is personally his","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_b60f275e348e8c7e32f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:possession-sound-chain","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_80532bbbbaa3173debcb"],"title":"suffix sound binds man and wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_fef76053efec3956e6a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:static-stockpile-agent-test","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_90ee7a8cc406921070ad"],"title":"static wealth is tested as an agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_1aecdb5869119f0950c7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:surah-wealth-axis","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_2749ae36cc70eaa9150d"],"title":"retained wealth contrasts with given wealth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:5"],"branch_refs":[],"candidate_id":"cand_81b19b7166cca7abb694","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:5:wealth-sufficiency-local-verdict","source_type":"word_analysis","support_ids":["sup_1f47143c0e50614c633f","sup_bf8f90ae3a1b889713a3"],"title":"wealth is excluded from rescue","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:5","qac_refs":["92:11:4:1","92:11:4:2"],"status":"accepted"}},{"anchor_refs":["92:11:6"],"branch_refs":[],"candidate_id":"cand_0641408a3a435ab61802","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:6:future-certain-when","source_type":"word_analysis","support_ids":["sup_14ad56f79f8ce64ab70b","sup_e54826844e350adacf1b"],"title":"the when-clause carries certainty","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:6","qac_refs":["92:11:5:1"],"status":"accepted"}},{"anchor_refs":["92:11:6"],"branch_refs":[],"candidate_id":"cand_2b85ba4780e832e3446f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:6:hardship-specified-as-fall","source_type":"word_analysis","support_ids":["sup_0c557aa6f4ee326f03d3","sup_14ad56f79f8ce64ab70b"],"title":"prior hardship becomes a fall-moment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:6","qac_refs":["92:11:5:1"],"status":"accepted"}},{"anchor_refs":["92:11:6"],"branch_refs":[],"candidate_id":"cand_0f635ed2a499834684fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:11:6:temporal-disclosure-hinge","source_type":"word_analysis","support_ids":["sup_14ad56f79f8ce64ab70b","sup_d78974e6c2df71945932"],"title":"particle hinges verdict and scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:6","qac_refs":["92:11:5:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_ab9e63b3cc7ecfad8764","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:certain-continuing-subject","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_f2565a12ee9efec3d339"],"title":"perfect fall continues the same man","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_a8e3941eaad9d1b2ff8e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:cloak-polysemy-narrowed","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_c0ebc4a16e1dbf839277"],"title":"mantle sense survives as image pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_dea95760e0f125106d5f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:closure-scene","source_type":"word_analysis","support_ids":["sup_3cb84a680df7222b810a","sup_5a932e4169f6c609432d"],"title":"fall closes the ayah as disclosure scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_05b1da495c2ed403d91d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:collapse-extension-narrowed","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_6c14a4219bad3582f237"],"title":"systemic collapse remains an extension","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_083e0243f7dcb9d11f17","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:falling-ruin-field","source_type":"word_analysis","support_ids":["sup_2f0b2a472f95ca5daf20","sup_5a932e4169f6c609432d"],"title":"fall image becomes terminal ruin","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_d8ebd66f1e045ee20c44","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:form-choice-against-causative","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_6105589a0da0553464df"],"title":"selected form avoids external hurling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_1dfab8f39dd44a5b8402","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:rare-cross-surah-field","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_b1747815762b0fbc400b"],"title":"rare root concentrates fatal-fall texture","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_beade2d6d4630aa93d71","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:self-involved-form-v","source_type":"word_analysis","support_ids":["sup_1bf9832325708a2592df","sup_5a932e4169f6c609432d"],"title":"Form V makes the ruin self-involved","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_691120b2a7b58766dbb9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:sound-and-orthographic-close","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_8e58a4eedbb84b986c81"],"title":"doubled sound and long ending carry the close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:7"],"branch_refs":[],"candidate_id":"cand_9ff342a486cd9e272890","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:7:surah-echoes","source_type":"word_analysis","support_ids":["sup_5a932e4169f6c609432d","sup_f9325816eaae34688cbf"],"title":"fall answers prior and following surah movements","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:11:7","qac_refs":["92:11:6:1"],"status":"accepted"}},{"anchor_refs":["92:11:2"],"branch_refs":[],"candidate_id":"cand_d21d30e3401cbfc70b16","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:11:2:1","source_type":"qac_morpheme","support_ids":["sup_2eafbe2cd2256bfab90b"],"title":"QAC root occurrence: غ ن ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:11:4"],"branch_refs":[],"candidate_id":"cand_345935547a36b3eec043","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:11:4:1","source_type":"qac_morpheme","support_ids":["sup_6d2929515a291f734547"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:11:6"],"branch_refs":[],"candidate_id":"cand_6960e5d35c86e4a888e6","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000558"],"scope":"focus_ayah","source_local_id":"92:11:6:1","source_type":"qac_morpheme","support_ids":["sup_8bf033f3c38ad8f14823"],"title":"QAC root occurrence: ر د ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:11","branch_refs":["root_000558/B003","root_001110/B002","root_001457/B001"],"candidate_id":"cand_6f7a512a11799e9ec388","commentary_obligation":"review","hft_ref":"hft_963d2a55b5d8e2fc2e24","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_non_substituting_capital","source_type":"hft","support_ids":["sup_de39739a57bb8925974f"],"title":"b01_non_substituting_capital","trust":"legacy_unbound"},{"anchor_refs":["92:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:11","branch_refs":["root_000558/B003","root_001110/B001","root_001457/B001"],"candidate_id":"cand_0b988127058ac570c7a3","commentary_obligation":"review","hft_ref":"hft_4ff3ef5e98dd887bad14","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_dependency_exposed","source_type":"hft","support_ids":["sup_1f1cf46d2c1b211c0421"],"title":"b02_dependency_exposed","trust":"legacy_unbound"},{"anchor_refs":["92:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:11","branch_refs":["root_000558/B003","root_001110/B004","root_001457/B001"],"candidate_id":"cand_d80164acff3c3d291407","commentary_obligation":"review","hft_ref":"hft_83abe17e8eb2c411d0c7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_habitation_outlived","source_type":"hft","support_ids":["sup_8caa746ce075b736baf6"],"title":"b03_habitation_outlived","trust":"legacy_unbound"},{"anchor_refs":["92:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:11","branch_refs":["root_000558/B002","root_001110/B002","root_001457/B001"],"candidate_id":"cand_ae25ea670591c9c755f9","commentary_obligation":"review","hft_ref":"hft_6a8e34942cc475d3d8fd","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_headlong_trajectory","source_type":"hft","support_ids":["sup_e686bb7ff19c95ffeeef"],"title":"b04_headlong_trajectory","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"92:11:1:1","qac_word_ref":"92:11:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"92:11:1:2","qac_word_ref":"92:11:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","root_ar":"غ ن ي","surface_ar":"يُغْنِى"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"92:11:3:1","qac_word_ref":"92:11:3","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:11:3:2","qac_word_ref":"92:11:3","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:11:4:1","qac_word_ref":"92:11:4","root_ar":"م و ل","surface_ar":"مَالُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:11:4:2","qac_word_ref":"92:11:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"92:11:5:1","qac_word_ref":"92:11:5","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","root_ar":"ر د ي","surface_ar":"تَرَدَّىٰٓ"}],"word_analysis_qac_refs":[["92:11:1:1"],["92:11:1:2"],["92:11:2:1"],["92:11:3:1","92:11:3:2"],["92:11:4:1","92:11:4:2"],["92:11:5:1"],["92:11:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:11:1","92:11:2","92:11:3","92:11:4","92:11:5","92:11:6","92:11:7"]},"focus_surface_evidence":{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"92:11:1:1","qac_word_ref":"92:11:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"92:11:1:2","qac_word_ref":"92:11:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"أَغْنَتْ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:2:1","qac_word_ref":"92:11:2","root_ar":"غ ن ي","surface_ar":"يُغْنِى"},{"lemma_ar":"عَن","morph_features":"STEM|POS:P|LEM:Ean","morpheme_role":"STEM","pos":"P","qac_ref":"92:11:3:1","qac_word_ref":"92:11:3","root_ar":"","surface_ar":"عَنْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:11:3:2","qac_word_ref":"92:11:3","root_ar":"","surface_ar":"هُ"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"92:11:4:1","qac_word_ref":"92:11:4","root_ar":"م و ل","surface_ar":"مَالُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:11:4:2","qac_word_ref":"92:11:4","root_ar":"","surface_ar":"هُۥٓ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"92:11:5:1","qac_word_ref":"92:11:5","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَرَدَّىٰٓ","morph_features":"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:11:6:1","qac_word_ref":"92:11:6","root_ar":"ر د ي","surface_ar":"تَرَدَّىٰٓ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:11:1:1"],["92:11:1:2"],["92:11:2:1"],["92:11:3:1","92:11:3:2"],["92:11:4:1","92:11:4:2"],["92:11:5:1"],["92:11:6:1"]],"word_analysis_refs":["92:11:1","92:11:2","92:11:3","92:11:4","92:11:5","92:11:6","92:11:7"],"word_rows":[{"analysis_record_ref":"92:11:1","analytic_gloss_range_en":"opening connector that carries the prior negative branch into the wealth-futility verdict","analytic_root_gloss_range_en":null,"qac_refs":["92:11:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:11:2","analytic_gloss_range_en":"negative particle placing the whole availing predication under factual denial","analytic_root_gloss_range_en":null,"qac_refs":["92:11:1:2"],"root":{},"surface":{"arabic":"مَا","transliteration":"ma"}},{"analysis_record_ref":"92:11:3","analytic_gloss_range_en":"negated Form IV availing or sufficing, with wealth as subject and an affected person governed through the preposition","analytic_root_gloss_range_en":"sufficiency, wealth, availing, benefit, replacement, dwelling, song, and other branches; the local Form IV construction selects availing or sufficing while nonmaterial branches remain outside the local sense","qac_refs":["92:11:2:1"],"root":{"arabic":"غ ن ي","transliteration":"gh-n-y"},"surface":{"arabic":"يُغْنِى","transliteration":"yughni"}},{"analysis_record_ref":"92:11:4","analytic_gloss_range_en":"preposition plus third-person suffix naming the affected person from whom need or harm is not averted","analytic_root_gloss_range_en":null,"qac_refs":["92:11:3:1","92:11:3:2"],"root":{},"surface":{"arabic":"عَنْهُ","transliteration":"anhu"}},{"analysis_record_ref":"92:11:5","analytic_gloss_range_en":"his personally possessed wealth, treated as the delayed subject whose power to avail is denied","analytic_root_gloss_range_en":"wealth, property, possessions, acquired resources, and livestock-as-wealth; locally the possessed stockpile is made syntactic subject but denied saving efficacy","qac_refs":["92:11:4:1","92:11:4:2"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"مَالُهُۥٓ","transliteration":"maluhu"}},{"analysis_record_ref":"92:11:6","analytic_gloss_range_en":"temporal-conditional particle introducing the certain crisis moment when wealth's failure is disclosed","analytic_root_gloss_range_en":null,"qac_refs":["92:11:5:1"],"root":{},"surface":{"arabic":"إِذَا","transliteration":"idha"}},{"analysis_record_ref":"92:11:7","analytic_gloss_range_en":"Form V perfect fall or perish in a self-involved ruin scene after the temporal particle","analytic_root_gloss_range_en":"falling into ruin, perishing, causing destruction, casting down, and mantle-wearing branches, with other stone, gait, increase, and cajoling branches outside the local selection","qac_refs":["92:11:6:1"],"root":{"arabic":"ر د ي","transliteration":"r-d-y"},"surface":{"arabic":"تَرَدَّىٰٓ","transliteration":"taradda"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["92:11"],"branch_refs":["root_000558/B003","root_001110/B002","root_001457/B001"],"candidate_id":"cand_6f7a512a11799e9ec388","evidence_scope":"focus_ayah","hft_ref":"hft_963d2a55b5d8e2fc2e24","item_id":"b01_non_substituting_capital","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_non_substituting_capital","support_id":"sup_de39739a57bb8925974f"},{"anchor_refs":["92:11"],"branch_refs":["root_000558/B003","root_001110/B001","root_001457/B001"],"candidate_id":"cand_0b988127058ac570c7a3","evidence_scope":"focus_ayah","hft_ref":"hft_4ff3ef5e98dd887bad14","item_id":"b02_dependency_exposed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_dependency_exposed","support_id":"sup_1f1cf46d2c1b211c0421"},{"anchor_refs":["92:11"],"branch_refs":["root_000558/B003","root_001110/B004","root_001457/B001"],"candidate_id":"cand_d80164acff3c3d291407","evidence_scope":"focus_ayah","hft_ref":"hft_83abe17e8eb2c411d0c7","item_id":"b03_habitation_outlived","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_habitation_outlived","support_id":"sup_8caa746ce075b736baf6"},{"anchor_refs":["92:11"],"branch_refs":["root_000558/B002","root_001110/B002","root_001457/B001"],"candidate_id":"cand_ae25ea670591c9c755f9","evidence_scope":"focus_ayah","hft_ref":"hft_6a8e34942cc475d3d8fd","item_id":"b04_headlong_trajectory","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_headlong_trajectory","support_id":"sup_e686bb7ff19c95ffeeef"}],"diagnostics":[],"lane_counts":{"global":18,"macro":5,"micro":4},"packet_summary":{"ayah_count":21,"focus_ref":"92:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"92:11","lane":"micro","linguistic_source_ref":"92:11","surface_ref":"92:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:11","target_tokens":[["Düştüğü",["92:11:5","92:11:6"]],["zaman",["92:11:5"]],["malı",["92:11:4"]],["ona",["92:11:3"]],["hiçbir",["92:11:1"]],["yarar",["92:11:2"]],["sağlamaz",["92:11:1","92:11:2"]]],"text":"Düştüğü zaman malı ona hiçbir yarar sağlamaz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:nonlocal-root-branches","source_type":"word_analysis","support_id":"sup_066c255ed5fcec2b2e34","text":"{\"blocking_evidence\":null,\"headline\":\"broader root branches are not selected here\",\"reader_payoff\":\"The reader keeps the local availing sense clear while recognizing that the root's wider dictionary range should not be imported into this clause.\",\"reason\":\"V4 separates availing from song, dwelling, and other branches, while the local construction selects the availing or sufficing branch.\",\"representative_source_ids\":[\"MS-305029f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:6:hardship-specified-as-fall","source_type":"word_analysis","support_id":"sup_0c557aa6f4ee326f03d3","text":"{\"blocking_evidence\":null,\"headline\":\"prior hardship becomes a fall-moment\",\"reader_payoff\":\"The reader connects the prior easing toward hardship in 92:10 with the concrete moment when wealth proves useless.\",\"reason\":\"The temporal clause specifies the scene in which the previous consequence is exhibited.\",\"representative_source_ids\":[\"QB-67baaa76\",\"QY-99719092\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:6","source_type":"word_analysis","support_id":"sup_14ad56f79f8ce64ab70b","text":"{\"gloss_range\":\"temporal-conditional particle introducing the certain crisis moment when wealth's failure is disclosed\",\"prose\":\"{{ar:إِذَا}} ({{tr:idha}}) turns the denial of wealth's efficacy into a timed scene. With the perfect verb {{ar:تَرَدَّىٰٓ}} ({{tr:taradda}}), it reads as a future-certain when, not an open-ended if: the fall is treated as the assured moment when the truth of the negated clause becomes visible. Structurally, the particle is the hinge between the general verdict and its crisis-point, converting the hardship of 92:10 into an event the listener can locate.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idha}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:2","source_type":"word_analysis","support_id":"sup_16e283550b431bf57d80","text":"{\"gloss_range\":\"negative particle placing the whole availing predication under factual denial\",\"prose\":\"{{ar:مَا}} ({{tr:ma}}) negates the whole verbal claim: {{ar:يُغْنِى}} ({{tr:yughni}}), its governed beneficiary, and the delayed subject {{ar:مَالُهُۥٓ}} ({{tr:maluhu}}). Because it governs an imperfect indicative verb, the denial is factual and open-ended rather than a prohibition or a past-only report. The short particle onset lets the denial strike before the heavier root-word unfolds. The word also front-loads the reversal of the earlier self-sufficiency claim in 92:8; before wealth is even named, its supposed saving function has already been placed inside futility.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:ma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:4:relation-referent-fusion","source_type":"word_analysis","support_id":"sup_171a4fd03b7338c3b252","text":"{\"blocking_evidence\":null,\"headline\":\"relation and referent are fused in one word\",\"reader_payoff\":\"The reader hears the failed-beneficiary role and the coming possessive wealth as one tight referential chain.\",\"reason\":\"The preposition and suffix form one surface word, and the following wealth noun repeats the same third-person suffix.\",\"representative_source_ids\":[\"QF-4a994316\",\"QP-e39c8667\",\"QY-165bda1f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:self-involved-form-v","source_type":"word_analysis","support_id":"sup_1bf9832325708a2592df","text":"{\"blocking_evidence\":null,\"headline\":\"Form V makes the ruin self-involved\",\"reader_payoff\":\"The reader notices that the man is not grammatically cast as a passive victim; the form places him inside his own collapse.\",\"reason\":\"The local verb is active Form V and intransitive, not a passive or a causative form with an external hurler.\",\"representative_source_ids\":[\"QG-13cc8161\",\"QS-4c357c7c\",\"MF-fe3c8515\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5","source_type":"word_analysis","support_id":"sup_1f47143c0e50614c633f","text":"{\"gloss_range\":\"his personally possessed wealth, treated as the delayed subject whose power to avail is denied\",\"prose\":\"{{ar:مَالُهُۥٓ}} ({{tr:maluhu}}) arrives late as the nominative subject of {{ar:يُغْنِى}} ({{tr:yughni}}), after its failure has already been announced. The possessive suffix makes the wealth specifically his, and the singular mass-like noun gathers the whole tangible stockpile into one tested resource. That is the irony: a concrete possession is promoted to grammatical agent only to show that possession cannot become rescue. It also makes the hardship of 92:10 material: the thing he relied on becomes the exhibit of uselessness at the fall. Within the surah, the same wealth-axis turns in opposite directions: the withheld resource of 92:8 is useless here, while wealth given in 92:18 moves toward purification.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"wealth, property, possessions, acquired resources, and livestock-as-wealth; locally the possessed stockpile is made syntactic subject but denied saving efficacy\",\"surface_display\":\"{{ar:مَالُهُۥٓ}} ({{tr:maluhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:4:pronoun-chain","source_type":"word_analysis","support_id":"sup_218e54f44ffaa6cbc786","text":"{\"blocking_evidence\":null,\"headline\":\"suffix continues the prior participant\",\"reader_payoff\":\"The reader follows the same unnamed man from 92:8-10 into the wealth-futility scene without needing him renamed.\",\"reason\":\"The attachment evidence links this suffix, the possessive suffix, and the implicit subject of the final verb to the same prior masculine singular participant.\",\"representative_source_ids\":[\"QG-0877e1bd\",\"MT-e2087e14\",\"QB-68d6c508\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:surah-wealth-axis","source_type":"word_analysis","support_id":"sup_2749ae36cc70eaa9150d","text":"{\"blocking_evidence\":null,\"headline\":\"retained wealth contrasts with given wealth\",\"reader_payoff\":\"The reader sees wealth become a moral fork inside the surah: retained into ruin here, given toward purification in 92:18.\",\"reason\":\"The same wealth noun recurs in the surah with opposed moral movement, and the 92:8 withholding background sharpens the local irony.\",\"representative_source_ids\":[\"MI-6c69d20a\",\"QT-ddc938a2\",\"QY-f078c83f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:wealth-sufficiency-pair","source_type":"word_analysis","support_id":"sup_2baf1416e6bdfae3757a","text":"{\"blocking_evidence\":null,\"headline\":\"wealth and sufficiency are clause-bound\",\"reader_payoff\":\"The reader sees the wealth-root and sufficiency-root forced into one verdict: the named wealth is excluded from the saving role.\",\"reason\":\"The delayed noun is the subject of this verb, so the cooccurrence is local syntax rather than a loose thematic association.\",\"representative_source_ids\":[\"QI-128150fe\",\"QI-438733fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:2:delayed-wealth-reversal","source_type":"word_analysis","support_id":"sup_2c348893c5bdb814f5d6","text":"{\"blocking_evidence\":null,\"headline\":\"wealth arrives after its failure has begun\",\"reader_payoff\":\"The reader feels the collapse of claimed sufficiency before the noun for wealth finally appears.\",\"reason\":\"The negation and verb precede the nominative subject, and the same root field as 92:8 is now introduced under negation.\",\"representative_source_ids\":[\"QT-d7c65908\",\"QE-e84592a1\",\"QY-6e7918bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:11:2:1","source_type":"qac_morpheme","support_id":"sup_2eafbe2cd2256bfab90b","text":"{\"lemma_ar\":\"أَغْنَتْ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:>agonato|ROOT:gny|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:11:2:1\",\"qac_word_ref\":\"92:11:2\",\"root_ar\":\"غ ن ي\",\"surface_ar\":\"يُغْنِى\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:falling-ruin-field","source_type":"word_analysis","support_id":"sup_2f0b2a472f95ca5daf20","text":"{\"blocking_evidence\":null,\"headline\":\"fall image becomes terminal ruin\",\"reader_payoff\":\"The reader sees the end as a concrete downward ruin, not only as an abstract moral decline.\",\"reason\":\"V4 includes a falling-into-ruin branch, and the local when-clause makes that branch the scene of disclosed non-availing.\",\"representative_source_ids\":[\"QS-054dfa62\",\"QS-3320fee2\",\"QS-799d0bda\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:personal-ownership-irony","source_type":"word_analysis","support_id":"sup_2fb35e31f1bf4adb8310","text":"{\"blocking_evidence\":null,\"headline\":\"the resource is personally his\",\"reader_payoff\":\"The reader sees that the failure lands on the man's own attached resource, not on wealth as a detached abstraction.\",\"reason\":\"The possessive suffix makes the noun definite by construct and links it to the same prior participant.\",\"representative_source_ids\":[\"QG-5e5585e1\",\"QG-ded44a94\",\"QF-1abe082e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:two-beat-disclosure","source_type":"word_analysis","support_id":"sup_391ed70a512d8e676717","text":"{\"blocking_evidence\":null,\"headline\":\"negated efficacy becomes visible at the crisis\",\"reader_payoff\":\"The reader sees that the verb states the rule whose truth is exposed in the following when-clause, before 92:12 shifts the reliable locus to guidance.\",\"reason\":\"The main negated clause is followed by a temporal clause, and the next ayah opens a contrasting guidance assertion in 92:12.\",\"representative_source_ids\":[\"QT-aa814e2d\",\"QB-03a9435e\",\"QY-173ec456\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:1","source_type":"word_analysis","support_id":"sup_3ad5458ff18a3c2bc27f","text":"{\"gloss_range\":\"opening connector that carries the prior negative branch into the wealth-futility verdict\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps 92:11 attached to the portrait of the miserly, self-sufficient denier in 92:8-10. The wealth clause therefore lands as a consequence and exhibit, not as a detached proverb about money, and it also describes the condition surrounding the coming fall. Because the connector runs directly into {{ar:مَا}} ({{tr:ma}}), the ayah enters through a clipped continuation-into-negation: the prior verdict carries straight into the denial that wealth will avail.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:closure-scene","source_type":"word_analysis","support_id":"sup_3cb84a680df7222b810a","text":"{\"blocking_evidence\":null,\"headline\":\"fall closes the ayah as disclosure scene\",\"reader_payoff\":\"The reader notices that the ayah does not end on wealth; it ends on the fall that proves wealth's non-availing.\",\"reason\":\"The final word sits inside the temporal clause that supplies the scene where the main denial is manifested.\",\"representative_source_ids\":[\"QT-628facd7\",\"QT-bbed5be2\",\"QB-afac7574\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:1:connective-circumstantial-range","source_type":"word_analysis","support_id":"sup_48ceb3028ede47867f80","text":"{\"blocking_evidence\":null,\"headline\":\"continuation with circumstantial pressure\",\"reader_payoff\":\"The reader can feel the clause both advancing the verdict and describing the state in which the fall is disclosed.\",\"reason\":\"The local tag supports conjunction first; the circumstantial value survives as pressure because the ayah immediately states the condition under which the prior fate becomes visible.\",\"representative_source_ids\":[\"QG-7eea93ef\",\"QS-d5c61edb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7","source_type":"word_analysis","support_id":"sup_5a932e4169f6c609432d","text":"{\"gloss_range\":\"Form V perfect fall or perish in a self-involved ruin scene after the temporal particle\",\"prose\":\"{{ar:تَرَدَّىٰٓ}} ({{tr:taradda}}) is where the ayah lands. After {{ar:إِذَا}} ({{tr:idha}}), the perfect form presents the fall as a future-certain event, and the hidden third-person masculine subject keeps it attached to the same man from 92:8-10. The Form V shape makes the ruin self-involved rather than a neutral report of death or an externally hurled collapse. Its root field gives the final scene a concrete downward image: he falls or perishes at the point where wealth cannot lift or rescue him. The rare fatal-fall field is sharpened by the fallen-animal occurrence in 5:3, while the local scene remains this man's ruin. The fall also answers same-surah movement: it shows where misguided striving in 92:4 leads, echoes the self-sufficiency cadence of 92:8 as collapse, and is followed by the guidance counter-axis in 92:12. The mantle branch survives only as narrowed image-pressure, making the ruin feel like a consequence he has put on himself; as a further extension, the word can model collapse below rescue without replacing the human subject. The verse-final long ending and doubled consonant let the fall occupy the acoustic close.\",\"root_display\":\"{{ar:ر د ي}} ({{tr:r-d-y}})\",\"root_gloss_range\":\"falling into ruin, perishing, causing destruction, casting down, and mantle-wearing branches, with other stone, gait, increase, and cajoling branches outside the local selection\",\"surface_display\":\"{{ar:تَرَدَّىٰٓ}} ({{tr:taradda}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:form-choice-against-causative","source_type":"word_analysis","support_id":"sup_6105589a0da0553464df","text":"{\"blocking_evidence\":null,\"headline\":\"selected form avoids external hurling\",\"reader_payoff\":\"The reader hears ruin as the man's own movement into consequence rather than as a form chosen to say another agent threw him down.\",\"reason\":\"The local Form V perfect is distinct from simple perishing or causative destruction forms in the root range.\",\"representative_source_ids\":[\"QF-1568b7e4\",\"QF-3bb20b88\",\"QF-bbdb422f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:governed-beneficiary-frame","source_type":"word_analysis","support_id":"sup_6bbf7ff713560bcfdf54","text":"{\"blocking_evidence\":null,\"headline\":\"availing is aimed toward a governed person\",\"reader_payoff\":\"The reader sees that the failure is not abstract; it is failure to protect or suffice for the named person.\",\"reason\":\"Attachment evidence marks the verb with no direct object and a governed prepositional complement, matching the dictionary construction for availing or sufficing.\",\"representative_source_ids\":[\"QG-1436163c\",\"QG-159ccc21\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:collapse-extension-narrowed","source_type":"word_analysis","support_id":"sup_6c14a4219bad3582f237","text":"{\"blocking_evidence\":null,\"headline\":\"systemic collapse remains an extension\",\"reader_payoff\":\"The reader may recognize the fall as a model of collapse below rescue, while the local referent remains the man's ruin.\",\"reason\":\"The attachment evidence supplies a human third-person subject; systemic collapse can illustrate the mechanism but cannot replace the local referent.\",\"representative_source_ids\":[\"QS-62e488ab\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:11:4:1","source_type":"qac_morpheme","support_id":"sup_6d2929515a291f734547","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:11:4:1\",\"qac_word_ref\":\"92:11:4\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:same-root-reversal-from-92-8","source_type":"word_analysis","support_id":"sup_7be83388caedde8147c3","text":"{\"blocking_evidence\":null,\"headline\":\"earlier self-sufficiency is reversed\",\"reader_payoff\":\"The reader hears the same sufficiency root return from 92:8, but now as the objective failure of what the man claimed.\",\"reason\":\"The root alignment links this verb with the same-root self-sufficiency claim in 92:8 while the local form shifts from self-assessment to conferred availing.\",\"representative_source_ids\":[\"MI-71a5e4e0\",\"MI-9befcc44\",\"ME-3acf277a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:possession-sound-chain","source_type":"word_analysis","support_id":"sup_80532bbbbaa3173debcb","text":"{\"blocking_evidence\":null,\"headline\":\"suffix sound binds man and wealth\",\"reader_payoff\":\"The reader hears the man and his wealth tightly linked even as the clause denies any saving power in that link.\",\"reason\":\"The possessive suffix is fused to the noun and echoes the prior suffix in the prepositional complement.\",\"representative_source_ids\":[\"QP-02e6495a\",\"QF-484e3c5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:11:6:1","source_type":"qac_morpheme","support_id":"sup_8bf033f3c38ad8f14823","text":"{\"lemma_ar\":\"تَرَدَّىٰٓ\",\"morph_features\":\"STEM|POS:V|PERF|(V)|LEM:tarad~aY`^|ROOT:rdy|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:11:6:1\",\"qac_word_ref\":\"92:11:6\",\"root_ar\":\"ر د ي\",\"surface_ar\":\"تَرَدَّىٰٓ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:sound-and-orthographic-close","source_type":"word_analysis","support_id":"sup_8e58a4eedbb84b986c81","text":"{\"blocking_evidence\":null,\"headline\":\"doubled sound and long ending carry the close\",\"reader_payoff\":\"The reader hears and sees the fall-word as heavy and prolonged at the verse boundary.\",\"reason\":\"The surface shows doubled consonantal marking and a verse-final long open ending, which supports the acoustic close without changing the lexical sense.\",\"representative_source_ids\":[\"QF-402b253f\",\"QF-eea83c9e\",\"QP-140ea01d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:1:fused-negative-onset","source_type":"word_analysis","support_id":"sup_8f92780828b80b288f0d","text":"{\"blocking_evidence\":null,\"headline\":\"connector enters as a bound launch into negation\",\"reader_payoff\":\"The reader notices that continuation is heard before and inside the negation, so the denial begins as linked follow-through.\",\"reason\":\"The surface sequence joins the connector directly to the negator while QAC still identifies the connector as its own particle.\",\"representative_source_ids\":[\"QF-a9cf1924\",\"QT-d22c7e6f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:static-stockpile-agent-test","source_type":"word_analysis","support_id":"sup_90ee7a8cc406921070ad","text":"{\"blocking_evidence\":null,\"headline\":\"static wealth is tested as an agent\",\"reader_payoff\":\"The reader notices the mismatch between a static possession and the active rescue role assigned to it.\",\"reason\":\"The root evidence is nominal and concrete, while local syntax makes the noun the subject of the verb whose efficacy is denied.\",\"representative_source_ids\":[\"QS-07ca74fa\",\"QS-8db7f4e4\",\"MS-b1d7ee1e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3:negated-form-iv-capability","source_type":"word_analysis","support_id":"sup_970b3208e66e7ba94b2b","text":"{\"blocking_evidence\":null,\"headline\":\"causative capability is denied\",\"reader_payoff\":\"The reader notices that wealth is tested as an active source of sufficiency, and that very capacity is what the ayah denies.\",\"reason\":\"QAC marks a Form IV imperfect indicative, and contextual evidence shows this form is frequently negated in sufficiency or availing contexts.\",\"representative_source_ids\":[\"MG-76518626\",\"QS-3891a16e\",\"QY-ce5266e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:rare-cross-surah-field","source_type":"word_analysis","support_id":"sup_b1747815762b0fbc400b","text":"{\"blocking_evidence\":null,\"headline\":\"rare root concentrates fatal-fall texture\",\"reader_payoff\":\"The reader hears a marked rare root at the endpoint, with the fallen-animal occurrence in 5:3 intensifying fatal plunge texture.\",\"reason\":\"The contextual profile marks the local form as low-occurrence, and the CRITICAL rows give the concrete 5:3 comparison without making it control the local parse.\",\"representative_source_ids\":[\"MS-5c38ed1c\",\"QI-8a657f76\",\"MI-208cc987\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:wealth-sufficiency-local-verdict","source_type":"word_analysis","support_id":"sup_bf8f90ae3a1b889713a3","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is excluded from rescue\",\"reader_payoff\":\"The reader sees the prior hardship made concrete as the failure of the very resource he relied on.\",\"reason\":\"The wealth noun is clause-bound to the negated availing verb and therefore functions as the concrete exhibit of non-rescue.\",\"representative_source_ids\":[\"QI-27c0f8c8\",\"QI-d625d832\",\"QB-23c71fd4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:1:continuation-frame","source_type":"word_analysis","support_id":"sup_c0e4337baf667ca35f40","text":"{\"blocking_evidence\":null,\"headline\":\"opening connector carries the prior consequence forward\",\"reader_payoff\":\"The reader hears 92:11 as the next step in the bad-branch arc from 92:8-10, not as a new isolated maxim.\",\"reason\":\"QAC marks the word as a conjunction, and the attachment evidence keeps the following suffixes and subject chain tied to the same prior participant.\",\"representative_source_ids\":[\"QG-71d8983a\",\"MG-99f6ae08\",\"QB-e72225cc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:cloak-polysemy-narrowed","source_type":"word_analysis","support_id":"sup_c0ebc4a16e1dbf839277","text":"{\"blocking_evidence\":null,\"headline\":\"mantle sense survives as image pressure\",\"reader_payoff\":\"The reader can feel ruin as something the man has wrapped around himself, while the local sense remains falling or perishing.\",\"reason\":\"V4 preserves the mantle branch, including the same surface form in dictionary evidence, but local syntax and context select the ruin or fall branch as the governing sense.\",\"representative_source_ids\":[\"QS-3cccc6b7\",\"QS-d970ceca\",\"MS-7f65769a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:2:whole-predicate-negation","source_type":"word_analysis","support_id":"sup_cdea2b293a3c44e01942","text":"{\"blocking_evidence\":null,\"headline\":\"negation scopes over the availing predication\",\"reader_payoff\":\"The reader notices that the ayah denies the efficacy of the entire wealth-availing event, not merely one noun phrase.\",\"reason\":\"QAC identifies the particle as negative, and attachment evidence marks the first clause as the negated main verbal clause.\",\"representative_source_ids\":[\"QG-02fee9d6\",\"QT-61c12eca\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:4:failed-beneficiary-complement","source_type":"word_analysis","support_id":"sup_d6de499146ae2fbdd6ee","text":"{\"blocking_evidence\":null,\"headline\":\"preposition marks the protected party\",\"reader_payoff\":\"The reader sees exactly whose protection fails: the clause marks the man as the party wealth cannot avail for.\",\"reason\":\"Attachment evidence marks the suffix as the governed complement of the availing verb through the preposition.\",\"representative_source_ids\":[\"QG-58ccec4e\",\"QG-b506aab6\",\"MG-e295d7f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:6:temporal-disclosure-hinge","source_type":"word_analysis","support_id":"sup_d78974e6c2df71945932","text":"{\"blocking_evidence\":null,\"headline\":\"particle hinges verdict and scene\",\"reader_payoff\":\"The reader sees the ayah split into a denial and the exact event that manifests it.\",\"reason\":\"Attachment evidence makes the particle and final verb a temporal clause attached to the negated availing event.\",\"representative_source_ids\":[\"QG-39b968f2\",\"QT-332f7ce2\",\"MT-8566a1d1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:4","source_type":"word_analysis","support_id":"sup_d7987bf7d5766f68a7dc","text":"{\"gloss_range\":\"preposition plus third-person suffix naming the affected person from whom need or harm is not averted\",\"prose\":\"{{ar:عَنْهُ}} ({{tr:anhu}}) tells where the expected protection fails. The preposition is not a loose separation marker here; it is governed by {{ar:يُغْنِى}} ({{tr:yughni}}), making the man the affected beneficiary from whom ruin or need would have to be averted. Its separation and behalf senses converge: wealth neither keeps ruin away from him nor stands in effectively for him. The attached suffix keeps him identical with the participant of 92:8-10, and its sound prepares {{ar:مَالُهُۥٓ}} ({{tr:maluhu}}): the man and his wealth are audibly bound even as the sentence denies that the wealth can act for him.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَنْهُ}} ({{tr:anhu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:material-stockpile-range","source_type":"word_analysis","support_id":"sup_e1b52da8732027ed731c","text":"{\"blocking_evidence\":null,\"headline\":\"wealth is concrete accumulated property\",\"reader_payoff\":\"The reader pictures accumulated tangible resources failing at the fall, not merely social status losing prestige.\",\"reason\":\"V4 gives the local root branch as wealth, property, and acquired resources, which fits the possessive noun.\",\"representative_source_ids\":[\"QS-7a3ea196\",\"QS-dfccbdfc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:5:delayed-possessed-subject","source_type":"word_analysis","support_id":"sup_e46c4653551ed3f32290","text":"{\"blocking_evidence\":null,\"headline\":\"his wealth is the delayed failed subject\",\"reader_payoff\":\"The reader watches the expected rescuer arrive only after grammar has already placed it under failure.\",\"reason\":\"QAC and attachment evidence identify the noun as a definite possessive nominative subject of the availing verb.\",\"representative_source_ids\":[\"QG-561cce50\",\"QG-ac9ab374\",\"MG-2318a3b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:6:future-certain-when","source_type":"word_analysis","support_id":"sup_e54826844e350adacf1b","text":"{\"blocking_evidence\":null,\"headline\":\"the when-clause carries certainty\",\"reader_payoff\":\"The reader hears the fall as an assured disclosure point rather than a merely possible scenario.\",\"reason\":\"QAC marks the particle as temporal-conditional and the following verb as perfect, matching the CRITICAL claim about future-certain timing.\",\"representative_source_ids\":[\"QG-34d06d7e\",\"MG-97bd6724\",\"QS-fedd1b24\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:2:factual-atemporal-denial","source_type":"word_analysis","support_id":"sup_eb877f0e5b3d16e452ba","text":"{\"blocking_evidence\":null,\"headline\":\"factual denial rather than command or question\",\"reader_payoff\":\"The reader hears a settled statement of impossibility at the crisis, not an instruction, wish, or open question.\",\"reason\":\"The following verb is an imperfect indicative under a negative particle, so the clause states factual non-availing.\",\"representative_source_ids\":[\"QG-774bafc4\",\"MG-eb5fa2d1\",\"MT-d0261ec1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:3","source_type":"word_analysis","support_id":"sup_ec8947367fbccd7308d4","text":"{\"gloss_range\":\"negated Form IV availing or sufficing, with wealth as subject and an affected person governed through the preposition\",\"prose\":\"{{ar:يُغْنِى}} ({{tr:yughni}}) is the ayah's main test-word: can the possessed wealth actually suffice, protect, or avail? The local frame answers no. The verb has no direct object here; it works with {{ar:عَنْهُ}} ({{tr:anhu}}), so the failure is personal, aimed at the very man for whom protection would be expected. Its Form IV imperfect makes the issue active capability, not mere status, and the clause-bound pairing with {{ar:مَالُهُۥٓ}} ({{tr:maluhu}}) forces wealth and sufficiency into one failed-rescue verdict. Its same-root return from 92:8 reverses the earlier self-sufficiency claim: what the man treated as independence cannot confer sufficiency when the fall arrives. The two-beat structure states the rule and then exposes it in the when-clause, before 92:12 shifts reliability from failed material sufficiency to guidance held with God. Broader root branches such as song or dwelling are real in the dictionary range but are not selected by this availing construction.\",\"root_display\":\"{{ar:غ ن ي}} ({{tr:gh-n-y}})\",\"root_gloss_range\":\"sufficiency, wealth, availing, benefit, replacement, dwelling, song, and other branches; the local Form IV construction selects availing or sufficing while nonmaterial branches remain outside the local sense\",\"surface_display\":\"{{ar:يُغْنِى}} ({{tr:yughni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:2:quick-negative-onset","source_type":"word_analysis","support_id":"sup_f1efdf18f8c631863012","text":"{\"blocking_evidence\":null,\"headline\":\"short particles make a clipped negative entry\",\"reader_payoff\":\"The reader hears a quick linked denial before the heavier root-word unfolds.\",\"reason\":\"The surface onset combines the connector and negator before the longer imperfect verb.\",\"representative_source_ids\":[\"QF-dfb5911d\",\"QP-9b96f752\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:certain-continuing-subject","source_type":"word_analysis","support_id":"sup_f2565a12ee9efec3d339","text":"{\"blocking_evidence\":null,\"headline\":\"perfect fall continues the same man\",\"reader_payoff\":\"The reader sees the fall as the assured future crisis of the same participant traced from 92:8-10.\",\"reason\":\"QAC marks a perfect third-person masculine verb, and attachment evidence identifies the unexpressed subject as continuing the same discourse participant.\",\"representative_source_ids\":[\"QG-cdb67afb\",\"QG-ed98c569\",\"MG-521a8d17\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:11:7:surah-echoes","source_type":"word_analysis","support_id":"sup_f9325816eaae34688cbf","text":"{\"blocking_evidence\":null,\"headline\":\"fall answers prior and following surah movements\",\"reader_payoff\":\"The reader connects the final fall with diverse striving in 92:4, self-sufficiency in 92:8, and the guidance assertion that follows in 92:12.\",\"reason\":\"The CRITICAL rows supply concrete same-surah references, and the local final position makes the echoes relevant without overriding the local verb sense.\",\"representative_source_ids\":[\"MT-68407c75\",\"QE-47ae4cfe\",\"QB-13529781\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000558/B003","root_001110/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficing, benefiting, and standing in for another supply the exact function that the focus negates.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Acquired property supplies the stock that is expected, but fails, to serve as substitute.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"A fall into ruin supplies the irreversible threshold at which substitution is exposed as impossible.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"At irreversible collapse, owned capital cannot spare, replace, or stand in for its owner; the denial concerns substitution, not merely usefulness.","before":"His wealth will not benefit him when he dies."},"confidence":"strong","focus_anchor":"The negated sufficing verb governs the possessive wealth noun, while the temporal descent clause names the point at which sufficiency is tested.","mechanism":"The availing-and-replacing branch of the first focus root is denied to acquired property at the falling-into-ruin branch of the final root. Possessions cannot function as a proxy for the possessor across irreversible collapse.","model_id":"b01_non_substituting_capital"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_non_substituting_capital","source_type":"hft","support_id":"sup_de39739a57bb8925974f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000558/B003","root_001110/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001110","role":"Wealth and freedom from need supply the identity the owner implicitly expects property to confer.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Accumulated possessions materialize the attempted self-sufficient identity.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Ruin functions as the stress test that uncovers dependence beneath apparent independence.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"The collapse disproves a category error: having wealth never made the owner self-sufficient, even while it made him appear so.","before":"A rich person loses the advantage of riches at the end."},"confidence":"medium","focus_anchor":"The focus places a self-sufficiency root beside a wealth root and then subjects both to a collapse condition.","mechanism":"The near-doubling of wealth and independence constructs an attempted identity: the owner treats having property as being without need. Descent reveals that the two are not equivalent, because possession cannot remove the owner's terminal dependence.","model_id":"b02_dependency_exposed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_dependency_exposed","source_type":"hft","support_id":"sup_1f1cf46d2c1b211c0421","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000558/B003","root_001110/B004","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001110","role":"Long dwelling and former habitation turn sufficiency into the stable place a life leaves behind.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Possessions furnish and mark the settled place but remain exterior to the departing owner.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_000558","role":"Disappearance toward an unknown direction breaks the link between owner and fixed habitation.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]}],"changed_reading":{"after":"The owner's settled world survives only as evidence that he once inhabited it; its very staying power shows why it cannot accompany or avail him.","before":"Wealth is left behind at death."},"confidence":"exploratory","focus_anchor":"A focus branch links the sufficiency root to settled dwelling, while the descent root includes disappearance in an unknown direction.","mechanism":"Property stabilizes a household and records that its owner once dwelt there, but it remains spatially fixed when the owner departs. The possessive expression becomes ironic: what was 'his' turns into a surviving habitation-marker that cannot accompany him.","model_id":"b03_habitation_outlived"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_habitation_outlived","source_type":"hft","support_id":"sup_8caa746ce075b736baf6","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ","ayah_ref":"92:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000558/B002","root_001110/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000558","role":"Rushing, bounding, and heavy gait supply an embodied trajectory rather than a motionless terminal state.","root":"ر د ي","source_ref":"92:11","source_word_indices":["6"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"The denied capacity to avail becomes, functionally, a denied capacity to arrest or redirect the course.","root":"غ ن ي","source_ref":"92:11","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"Accumulated means can propel activity but do not themselves provide orientation or restraint.","root":"م و ل","source_ref":"92:11","source_word_indices":["4"]}],"changed_reading":{"after":"The owner is already moving headlong; wealth can add means to motion but cannot brake the trajectory when it becomes ruinous.","before":"The owner eventually falls despite being rich."},"confidence":"exploratory","focus_anchor":"The final focus root carries both ruin and a rushing or bounding gait, allowing the temporal clause to be heard as motion before impact.","mechanism":"The focus can stage not only a passive fall but an already accelerated course. Wealth may finance movement, yet it supplies neither steering nor braking and therefore cannot alter the destination of headlong momentum.","model_id":"b04_headlong_trajectory"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_headlong_trajectory","source_type":"hft","support_id":"sup_e686bb7ff19c95ffeeef","trust":"legacy_unbound"}]}
</lane_packet_json>
