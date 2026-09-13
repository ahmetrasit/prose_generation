# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:18**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_18/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:18",
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
{"branch_registry":[{"boundary":"Çekirdek anlam gelme ve ulaşmadır; gelmeyi isteme yalnız ilgili kalıba bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"gelmek, ulaşmak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey gelir veya bir hedefe ulaşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir açıklamada gelişin kolaylıkla gerçekleşmesi özellikle belirtilir."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin bir yere gelişi ya da hedefe varışı anlatılırken kullanılır.","boundary_detail":"Çekirdek anlam gelme ve ulaşmadır; gelmeyi isteme yalnız ilgili kalıba bağlıdır.","branch_image_ar":"الإتيان والمجيء","concept_gloss":"gelmek, ulaşmak","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişinin bulunduğu yere gelişi söz konusu olduğunda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişi dışındaki şeylerin gelişi ile daha genel ulaşma kapsamını dışarıda bırakır.","preserves":"Kişinin bir hedefe doğru gelip ulaşmasını korur."},"facet_ids":["F001"],"text":"yanına gelmek","usage_role":"contextual"}],"definition":"Bir kişinin ya da şeyin bulunduğu yere gelmesi veya bir hedefe ulaşmasıdır; bazı kullanımlarda bu gelişin kolayca gerçekleştiği belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey gelir veya bir hedefe ulaşır."},{"facet_id":"F002","role":"source_variant","statement":"Bir açıklamada gelişin kolaylıkla gerçekleşmesi özellikle belirtilir."}],"identity_rationale":"Kaynak ifadesi dalın çekirdeğini gelme ve ulaşma olarak doğrular; kolaylık niteliği açıklamalardan yalnız birinde belirgindir. Gelmeyi isteme ise dalın genel anlamı değil, ayrı bir kalıpta görülen kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"gelmek veya ulaşmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ona gitmek veya yanına varmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"geciktiğini düşünüp gelmesini istemek"}],"lexicalization_note":"Yalın gelme anlamı ile birini gecikmiş sayıp gelmesini istemeyi bildiren kalıp birbirine karıştırılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en doğrudan eş anlamlı karşılık yayımlandı, diğerleri geliş senaryosunu paylaşsa da çekirdeği keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kaynak kartlarındaki çekirdek ve kapsam bakımından anlamlı bir sınır farkı yoktur.","focus_only":null,"gloss":"gelmek","neighbor_only":null,"neighbor_ref":"root_000281/B001","relation_type":"synonym","shared_zone":"Her iki dal da kişi veya şeyin gelmesini ve bir hedefe ulaşmasını anlatır."}],"source_phrase_ar":"أتى يأتي أتيا (jamhara)؛ الإتيان المجئ (sihah)؛ أتاني فلان إتيانا وأتيا وأتية وأتوة (tahdhib;maqayis)؛ الإتيان مجيء بسهولة (mufradat)","source_summary":"Kaynaklar gelme ve ulaşma çekirdeğinde birleşir; kolaylık, çekirdeği sınırlamayan ek bir niteleme olarak görünür.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"المجيء والوصول بالذات أو بالأمر أو بالتدبير، وطلب الإتيان أو وقوع الأمر المتوقع","what_is_not_ar":"ليس الإعطاء ولا الخراج ولا ريع الزرع"},"support_links":[]},{"boundary":"Dal gelme eylemini değil, bir alıcıya verme veya bir şeyi getirip sunma eylemini anlatır.","branch_kind":"bare","branch_ref":"root_000009/B002","candidate_links":[{"candidate_id":"cand_44bb0198bb7ffca9c530","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"vermek; getirip sunmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey bir alıcıya verilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şey getirilip hazır edilerek karşı tarafa sunulur."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin alıcıya geçirilmesi veya getirilerek onun önüne konması anlatılırken kullanılır.","boundary_detail":"Dal gelme eylemini değil, bir alıcıya verme veya bir şeyi getirip sunma eylemini anlatır.","branch_image_ar":"الإيتاء والإعطاء","concept_gloss":"vermek; getirip sunmak","contextual_glosses":[{"applicability":"Bir nesne veya yararın doğrudan bir alıcıya aktarılması bağlamında en doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi getirip hazır ederek sunma uzantısını belirtmez.","preserves":"Bir şeyi alıcıya aktarma çekirdeğini korur."},"facet_ids":["F001"],"text":"vermek","usage_role":"general"}],"definition":"Bir şeyi birine vermek; ayrıca bir şeyi getirip hazır ederek karşı tarafa sunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey bir alıcıya verilir."},{"facet_id":"F002","role":"extension","statement":"Bir şey getirilip hazır edilerek karşı tarafa sunulur."}],"identity_rationale":"Kaynak ifadesi doğrudan verme anlamını ve ikincil olarak bir şeyi getirip hazır etme kullanımını bildirir. Bu iki geçişli kullanım dal çerçevesiyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"vermek; bir şeyi getirip sunmak"}],"lexicalization_note":"Tanım yalın fiilin verme ve getirip sunma kapsamıyla sınırlıdır; vergi ya da başka bir kalıp anlamı içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; istek üzerine verme dalı en yakın sınır karşılaştırmasını sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel verme alanına sahipken komşu dal alıcının istemiş olması koşuluyla daha dardır.","focus_only":"Verme eylemi bir isteğe bağlı olmadan da gerçekleşebilir ve getirip sunma kullanımını kapsar.","gloss":"isteneni vermek","neighbor_only":"Komşu dal özellikle kendisinden istenen bir şeyi verme durumunu öne çıkarır.","neighbor_ref":"root_001403/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şey bir alıcıya verilir."}],"source_phrase_ar":"آتى يؤتي إيتاء في معنى أعطى (jamhara)؛ آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به (sihah)؛ الإتياء الإعطاء (tahdhib)؛ الإيتاء الإعطاء (mufradat;maqayis)","source_summary":"Ortak çekirdek vermedir; bir açıklama aynı biçimin bir şeyi getirip hazır etme kullanımını da kapsadığını gösterir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"الإعطاء، وإتيان الشيء بالشيء أو إحضاره","what_is_not_ar":"ليس مجرد المجيء ولا الإتاوة المفروضة"},"support_links":["sup_fda4e2db2bba27fe0669"]},{"boundary":"Dal tek bir yalın anlama indirgenmez; yaklaşım, uyum, elverişlilik ve ihtiyacı usulünce yürütme kullanımları ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B003","candidate_links":[{"candidate_id":"cand_06c6ae616da4d61b813c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"uygun yoldan ele almak ve elverişli hale gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işe sonuç alınabilecek uygun yönünden yaklaşılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimseye belirli bir işte uyulur ve onun isteğine razı olunur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şey kişi için elverişli ve yapılabilir hale gelir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir ihtiyaç uygun yol gözetilerek incelikle yürütülür."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşin uygun yönü, kişiler arası uyum veya bir şeyin yapılabilir hale gelişi birlikte temsil edileceğinde kullanılır.","boundary_detail":"Dal tek bir yalın anlama indirgenmez; yaklaşım, uyum, elverişlilik ve ihtiyacı usulünce yürütme kullanımları ayrıdır.","branch_image_ar":"مأتى الأمر وتهيؤه","concept_gloss":"uygun yoldan ele almak ve elverişli hale gelmek","contextual_glosses":[{"applicability":"Bir şeyin kişi için yapılabilir veya mümkün hale gelmesini anlatan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uygun yönden yaklaşma, kişiye uyma ve ihtiyacı incelikle yürütme kullanımlarını dışarıda bırakır.","preserves":"Bir şeyin elverişli hale gelişi anlamını korur."},"facet_ids":["F003"],"text":"elverişli hale gelmek","usage_role":"contextual"}],"definition":"Bir işi uygun yönünden ele almak, bir kimseye bir işte uyup razı olmak veya bir şeyin yapılabilir hale gelmesidir. İhtiyacı usulünce ve incelikle yürütme de bu alandaki ayrı bir kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işe sonuç alınabilecek uygun yönünden yaklaşılır."},{"facet_id":"F002","role":"extension","statement":"Bir kimseye belirli bir işte uyulur ve onun isteğine razı olunur."},{"facet_id":"F003","role":"associated_use","statement":"Bir şey kişi için elverişli ve yapılabilir hale gelir."},{"facet_id":"F004","role":"associated_use","statement":"Bir ihtiyaç uygun yol gözetilerek incelikle yürütülür."}],"identity_rationale":"Kaynak ifadesi bir işe uygun yönünden yaklaşmayı, birine uyup razı olmayı, bir şeyin elverişli hale gelmesini ve ihtiyacı incelikle yürütmeyi birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"işin uygun yönü ve tutulacak yolu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"uyma ve razı olma"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir şeyin ona elverişli hale gelmesi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ihtiyacını uygun yoldan ve incelikle yürütmek"}],"lexicalization_note":"Biçimlere bağlı yaklaşım ve uyum anlamları ile iki ayrı kalıptaki elverişlilik ve incelikli yürütme anlamları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; elverişlilik ortaklığı bulunan komşu, dalın yöntem ve uyum sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak elverişlilik alanına rağmen odak dal yöntem ve uyum ilişkileri taşır; komşu dalın çekirdeği ise güçlüğün karşıtı olan kolaylıktır.","focus_only":"Odak dal uygun yönden yaklaşmayı, birine uymayı ve ihtiyacı incelikle yürütmeyi de kapsar.","gloss":"kolaylaşıp elverişli olmak","neighbor_only":"Komşu dal güçlüğün kalkıp genel olarak kolaylığın ortaya çıkmasını merkez alır.","neighbor_ref":"root_001694/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir işin yapılabilir ve elverişli hale gelmesini anlatabilir."}],"source_phrase_ar":"أتيت الأمر من مأتاته (sihah;maqayis)؛ آتيته على ذلك الأمر مواتاة إذا وافقته وطاوعته (sihah)؛ آتيت فلانا على أمره مؤاتاة وهو حسن المطاوعة (maqayis)؛ تأتى له الشيء أي تهيأ (sihah)؛ تأتى فلان لحاجته إذا ترفق لها (tahdhib)","source_summary":"Toplu kanıt, uygun yoldan yaklaşma çevresinde uyma, elverişli hale gelme ve ihtiyacı incelikle yürütme kullanımlarını bir araya getirir.","sources":["SI","TA","MQ"],"what_is_ar":"إتيان الأمر من وجهه، والموافقة والمطاوعة، والترفق للحاجة، وتهيؤ الشيء","what_is_not_ar":"ليس مطلق المجيء بالذات ولا الإعطاء"},"support_links":["sup_8038e12b74ed5c66816f"]},{"boundary":"Su yolu ve akışı kolaylaştırma çekirdektir; akışı tutan odun ya da yaprak birikintisi kaynakça sınırlı bir yan kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B004","candidate_links":[{"candidate_id":"cand_107e37a196c78dc2dda9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"su kanalı açmak ve akışı yönlendirmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su için açılan veya suyu araziye taşıyan bir kanal bulunur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun akacağı yol kolaylaştırılır ve akış belirli bir yöne çevrilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir açıklamada nehirdeki odun ve yaprak birikintisinin suyu tutması adlandırılır."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem suyu taşıyan yol hem de bu yolu açıp akışı kolaylaştırma kavramsal olarak birlikte verileceğinde uygundur.","boundary_detail":"Su yolu ve akışı kolaylaştırma çekirdektir; akışı tutan odun ya da yaprak birikintisi kaynakça sınırlı bir yan kullanımdır.","branch_image_ar":"مجرى الماء وتسليك سبيله","concept_gloss":"su kanalı açmak ve akışı yönlendirmek","contextual_glosses":[{"applicability":"Suyu araziye veya havuza taşıyan somut su yolu adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akışı kolaylaştırma eylemini ve suyu tutan birikinti kullanımını dışarıda bırakır.","preserves":"Suyu taşıyan kanal anlamını korur."},"facet_ids":["F001"],"text":"sulama kanalı","usage_role":"contextual"}],"definition":"Suyun akacağı kanal veya suya bir yol açarak akışını kolaylaştırıp yönlendirmedir. Bir kaynakta aynı ad, nehirde birikip suyu tutan odun ve yapraklar için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su için açılan veya suyu araziye taşıyan bir kanal bulunur."},{"facet_id":"F002","role":"core","statement":"Suyun akacağı yol kolaylaştırılır ve akış belirli bir yöne çevrilir."},{"facet_id":"F003","role":"source_variant","statement":"Bir açıklamada nehirdeki odun ve yaprak birikintisinin suyu tutması adlandırılır."}],"identity_rationale":"Kaynak ifadesi su için yol açma ve akışı yöneltme eylemlerini, su kanalı adını ve bir açıklamada akışı tutan birikintiyi açıkça içerir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"su kanalı; suyu tutan odun ve yaprak birikintisi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bu suya yol açıp akışını yönlendirmek"}],"lexicalization_note":"Su yolu adı ile suya yol açmayı bildiren kalıp ayrılır; akışı tutan birikinti yalnız biçimin özel kapsamındadır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sulama kanalı komşusu somut yol ile akışı yöneltme eylemi arasındaki sınırı en iyi belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal suya özgü yol açma eylemiyle bağlantılıdır; komşu dal ise farklı sıvıların geçitlerini kapsayan daha geniş bir kanal adıdır.","focus_only":"Odak dal kanalın yanında suya yol açma ve akışı yönlendirme eylemini de kapsar.","gloss":"su taşıyan kanal","neighbor_only":"Komşu dal su dışında süt ve ilik için de kullanılan akış yollarını kapsar.","neighbor_ref":"root_000707/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal suyu taşıyan ve toprağı sulayan bir kanal anlamında kesişir."}],"source_phrase_ar":"أت لمائك أي سهل له سبيلا وذلك السبيل الأتي (jamhara)؛ الأتي الجدول يؤتيه الرجل إلى أرضه (sihah)؛ كل جدول ماء أتي (tahdhib)؛ أت لهذا الماء أي سهل جريه (maqayis)؛ الأتي ما وقع في النهر من خشب أو ورق مما يحبس الماء (maqayis)","source_summary":"Kanıt su kanalı ile suyun akışına yol açma anlamlarını birleştirir; akışı tutan birikinti aynı toplu iddia içindeki sınırlı bir karşı kullanımdır.","sources":["JA","SI","TA","MQ"],"what_is_ar":"الجدول أو النهر إلى الحوض، وتسهيل جريان الماء أو توجيه مجراه، وما يقع في النهر فيحبس الماء عند مقاييس","what_is_not_ar":"ليس السيل الآتي من بلد آخر نفسه ولا ريع الزرع"},"support_links":["sup_1d73dfb73c1b46debef4"]},{"boundary":"Anlam yalnız dışarıdaki yağış alanından gelen sel kalıbına bağlıdır; genel sel veya genel akış değildir.","branch_kind":"collocation","branch_ref":"root_000009/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"başka bölgeden gelen sel","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Selin suyu yağmur alan başka bir bölgeden gelir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sel, kendi yağmurunu almamış bir bölgeye ulaşıp oradan geçer."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Selin ulaştığı yerde yağmur yağmamış, su başka bir yağış alanından gelmişse kullanılır.","boundary_detail":"Anlam yalnız dışarıdaki yağış alanından gelen sel kalıbına bağlıdır; genel sel veya genel akış değildir.","branch_image_ar":"السيل الآتي من غير البلد","concept_gloss":"başka bölgeden gelen sel","definition":"Yağmur alan başka bir bölgeden, yağmur almamış bir bölgeye yatağı boyunca ulaşıp geçen seldir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Selin suyu yağmur alan başka bir bölgeden gelir."},{"facet_id":"F002","role":"core","statement":"Sel, kendi yağmurunu almamış bir bölgeye ulaşıp oradan geçer."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yerel yağmurdan doğan selleri de kapsayarak zorunlu dış kaynak koşulunu kaldırır.","collision":null,"fit":"broadening","loses":null,"preserves":"Akan büyük su kütlesi olma niteliğini korur."},"text":"sel"}],"identity_rationale":"Kaynakların tümü, yağmurun düştüğü başka bir yerden yağmur almamış bölgeye ulaşan seli veya kendi yatağında dışarıdan geçip gelen seli tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yağmur alan başka bir bölgeden gelen sel"}],"lexicalization_note":"Tanım yalnız belirtilen sel nitelemesine bağlı tutulur ve sözcükten genel bir yalın anlam türetilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel su akışı dalı, bu kalıbın dışarıdan gelme koşulunu en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kaynağı ve hedef bölgenin yağış durumuyla sınırlı özel bir sel türüdür; komşu dal genel akış alanıdır.","focus_only":"Sel, yağmur alan başka bir bölgeden yağmur almamış bölgeye gelmelidir.","gloss":"akmak ve sel olmak","neighbor_only":"Komşu dal her türlü su akışını, akıtmayı, akan suyu ve akış yerini kapsar.","neighbor_ref":"root_000770/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da yatakta ilerleyen akan su bulunur."}],"source_phrase_ar":"الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك (jamhara)؛ سيل أتي وأتاوي إذا جاءك ولم يصبك مطره (sihah)؛ المسيل الذي يأتي من بلد قد مطر فيه إلى بلد لم يمطر فيه أتي (tahdhib)؛ السيل المار على وجهه أتي وأتاوي (mufradat)؛ الأتي أيضا السيل الذي يأتي من بلد غير بلدك (maqayis)","source_summary":"Kaynaklar, yerel yağıştan doğmayan ve yağmur alan başka bir yerden geçerek gelen sel sınırında birleşir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"السيل الذي يأتي من بلد أصابه المطر إلى بلد لم يصبه المطر","what_is_not_ar":"ليس الجدول المصنوع ولا الغريب من الناس"},"support_links":[]},{"boundary":"Bu anlam yalnız bir topluluk içinde onlardan olmayan yabancı kişi nitelemesine bağlıdır.","branch_kind":"collocation","branch_ref":"root_000009/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"topluluğa yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir topluluğun içinde bulunur ancak o topluluktan değildir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi topluluğa göre yabancı ve dışarıdan gelmiş sayılır."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin içinde bulunduğu topluluğun mensubu olmadığını belirtmek için kullanılır.","boundary_detail":"Bu anlam yalnız bir topluluk içinde onlardan olmayan yabancı kişi nitelemesine bağlıdır.","branch_image_ar":"الغريب الداخل في غير قومه","concept_gloss":"topluluğa yabancı kimse","definition":"Bir topluluk içinde bulunan, fakat o topluluğa mensup olmayan yabancı erkektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir topluluğun içinde bulunur ancak o topluluktan değildir."},{"facet_id":"F002","role":"core","statement":"Kişi topluluğa göre yabancı ve dışarıdan gelmiş sayılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Bir topluluk içinde bulunmayan kişiler ile tanınmayan şeyleri de kapsayabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Kişinin gruba göre dışarıdan oluşunu korur."},"text":"yabancı"}],"identity_rationale":"Kaynak ifadesi, içinde bulunduğu topluluğa mensup olmayan yabancı erkeği ortak biçimde tanımlar ve dal çerçevesindeki sınırı doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"içinde bulunduğu topluluğa mensup olmayan yabancı adam"}],"lexicalization_note":"Tanım kişi niteleyen kalıpla sınırlıdır; her gelen kişi veya dışarıdan gelen sel bu kapsama alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; topluluğa karışmış yabancı dalı mensubiyet ile sonradan giriş arasındaki farkı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal mensubiyet dışılığını merkez alır; komşu dal dışarıdan girme ve topluluğa karışma görünümünü daha belirgin taşır.","focus_only":"Odak dal kişinin topluluğa yabancı oluşunu bildirir, sonradan karışma biçimini zorunlu kılmaz.","gloss":"topluluğa karışmış yabancı","neighbor_only":"Komşu dal topluluğa dışarıdan girip ona karışan kişi görünümünü özellikle taşır.","neighbor_ref":"root_001478/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir topluluk içinde o topluluktan olmayan kişiyi anlatır."}],"source_phrase_ar":"رجل أتي وأتاوي وهو الغريب (jamhara)؛ الاتي أيضا والاتاوى الغريب (sihah)؛ إنما هو أتي فينا (tahdhib)؛ به شبه الغريب فقيل أتاوي (mufradat)؛ رجل أتي أي غريب في قوم ليس منهم وأتاوي كذلك (maqayis)","source_summary":"Kaynaklar, kişinin bulunduğu topluluğa mensup olmaması ve bu nedenle yabancı sayılması üzerinde birleşir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"الرجل الغريب في قوم ليس منهم، وما يقال له أَتِيّ أو أتاوي","what_is_not_ar":"ليس كل آت مطلقا ولا السيل الآتي من بلد آخر"},"support_links":[]},{"boundary":"Bitkisel ürün ve artış çekirdektir; suyun çoğalması uzantı, tulumdan yağ çıkması ise ayrı kalıp kullanımıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B007","candidate_links":[{"candidate_id":"cand_8cc17107b0431dc9cad9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"gelişip bol ürün vermek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ekin veya hurma gelişir, ürün verir ve verimi artar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun miktarı çoğalır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayrı bir kalıpta çalkalanan tulumun yağı ortaya çıkar."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ekin veya hurmanın gelişmesi, ürün çıkarması ve veriminin artması birlikte anlatılacağında kullanılır.","boundary_detail":"Bitkisel ürün ve artış çekirdektir; suyun çoğalması uzantı, tulumdan yağ çıkması ise ayrı kalıp kullanımıdır.","branch_image_ar":"خروج النماء والنتاج","concept_gloss":"gelişip bol ürün vermek","contextual_glosses":[{"applicability":"Ekinin veya hurmanın çıkan ürünü ve yüksek verimi adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gelişme sürecini, suyun çoğalmasını ve tulum yağı kullanımını dışarıda bırakır.","preserves":"Bitkinin ürünü ile verim bolluğunu korur."},"facet_ids":["F001"],"text":"bol ürün","usage_role":"contextual"}],"definition":"Ekin ve hurmanın gelişip ürün vermesi, ürününün ve veriminin bol olmasıdır; suyun çoğalması da bu artış alanına uzanır. Ayrı bir kalıp, çalkalanan tulumda yağın ortaya çıkmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ekin veya hurma gelişir, ürün verir ve verimi artar."},{"facet_id":"F002","role":"extension","statement":"Suyun miktarı çoğalır."},{"facet_id":"F003","role":"associated_use","statement":"Ayrı bir kalıpta çalkalanan tulumun yağı ortaya çıkar."}],"identity_rationale":"Kaynak ifadesi ekin ve hurmanın ürünü, gelişmesi ve bol verimi ile suyun çoğalmasını destekler. Çalkalanan tulumdan yağın çıkması ise yalnız ayrı kalıbın kaynak ifadesiyle açıklanabilen, çekirdeğe bağlı olmayan bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ekin ve hurmanın gelişmesi, ürünü ve bol verimi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çalkalanan tulumun yağının ortaya çıkması"}],"lexicalization_note":"Ürün ve gelişme bildiren biçim, suyun çoğalması ve çalkalanan tulumda yağın belirmesini bildiren kalıptan ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ürün dalı, ürünün kendisi ile gelişme ve bol verim arasındaki ayrımı en iyi belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ürünle birlikte gelişme ve bolluk sürecini öne çıkarır; komşu dal ürünün kendisine daha genel biçimde yönelir.","focus_only":"Odak dal ürünün yanında gelişme, verim bolluğu ve suyun çoğalması kapsamlarını taşır.","gloss":"ağaç ve ekin ürünü","neighbor_only":"Komşu dal ağaç, hurma, ekin ve toprağın verdiği ürünü daha genel bir ürün adı olarak kapsar.","neighbor_ref":"root_000043/B002","relation_type":"near_synonym","shared_zone":"Her iki dal ekin ve hurmanın meydana getirdiği ürünü anlatır."}],"source_phrase_ar":"أتاء هذا النخل أي ثمره وكذلك الزرع (jamhara)؛ الاتاء البركة والنماء وحمل النخل (sihah)؛ جاء أتوه (sihah;mufradat)؛ إتاء النخلة ريعها وزكاؤها وكثرة ثمارها (tahdhib)؛ الإتاء نماء الزرع والنخل وأتى الماء إتاء أي كثر (maqayis)","source_summary":"Toplu kanıt bitkisel gelişme, ürün ve bol verimi merkez alır; su artışı ve tulum yağının belirmesi farklı kapsamlı kullanımlardır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"ريع الزرع والنخل وثمرهما، وكثرة الماء، وما يجيء من زبد السقاء عند الصحاح والمفردات","what_is_not_ar":"ليس الإيتاء بمعنى الإعطاء ولا الإتاوة المفروضة"},"support_links":["sup_2a7d73f23e85348cfd4f"]},{"boundary":"Düzenli veya zorunlu kamu ödemesi çekirdektir; rüşvet, aynı biçimin ayrı kalıptaki özel kullanımıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"ödenen vergi; rüşvet","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluk veya kişi yönetime vergi niteliğinde para öder."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ödeme baş vergisi veya benzeri yükümlülük niteliği taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ayrı bir kullanımda bir kimseye rüşvet verilir."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yönetime ödenen mali yükümlülük ile ayrı rüşvet kullanımı birlikte gösterileceğinde kullanılır.","boundary_detail":"Düzenli veya zorunlu kamu ödemesi çekirdektir; rüşvet, aynı biçimin ayrı kalıptaki özel kullanımıdır.","branch_image_ar":"الإتاوة المؤداة","concept_gloss":"ödenen vergi; rüşvet","contextual_glosses":[{"applicability":"Topluluğun veya kişinin yönetime yaptığı zorunlu mali ödeme söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Rüşvet olarak verilen ödeme kullanımını dışarıda bırakır.","preserves":"Yönetime yapılan mali yükümlülük ödemesini korur."},"facet_ids":["F001","F002"],"text":"vergi","usage_role":"general"}],"definition":"Bir topluluğun veya kişinin yönetime ödediği vergi ya da baş vergisidir. Ayrı bir kalıpta, bir kimseye çıkar sağlamak için verilen rüşveti veya rüşvet verme eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluk veya kişi yönetime vergi niteliğinde para öder."},{"facet_id":"F002","role":"specialization","statement":"Ödeme baş vergisi veya benzeri yükümlülük niteliği taşır."},{"facet_id":"F003","role":"associated_use","statement":"Ayrı bir kullanımda bir kimseye rüşvet verilir."}],"identity_rationale":"Kaynak ifadesi yönetime ödenen vergi veya baş vergisini ortak alan olarak verir ve aynı toplu iddia içinde bir kişiye sunulan rüşvet kullanımını da bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"vergi veya baş vergisi; rüşvet"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ona rüşvet vermek"}],"lexicalization_note":"Vergi adı olarak kullanılan biçim ile birine rüşvet vermeyi bildiren kalıp kapsam bakımından ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; mali yükümlülük komşusu vergi çekirdeği ile rüşvet uzantısı arasındaki sınırı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal vergi adının yanında rüşvet kullanımına sahiptir; komşu dal ise üzerine konan mali yükümlülük türlerini daha geniş kapsar.","focus_only":"Odak dal aynı biçimin rüşvet kullanımını da kapsar.","gloss":"kişiye veya toprağa konan vergi","neighbor_only":"Komşu dal kişiye, köleye veya toprağa konan vergi, gelir ve görev ödemelerini daha geniş sınıflar halinde kapsar.","neighbor_ref":"root_000906/B010","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişi veya topluluğa yüklenen vergi ve kamu ödemesi alanında kesişir."}],"source_phrase_ar":"الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك (jamhara)؛ الاتاوة الخراج والجمع الاتاوي (sihah)؛ الإتاوة الخراج وجمعها الأتاوى والإتاوات (tahdhib)؛ أتوته أتوة إذا رشوته إتاوة وهي الرشوة (tahdhib)","source_summary":"Toplu iddia vergi ve baş vergisi anlamlarını ortaklaştırır; rüşvet kullanımı kaynaklara ayrı ayrı dağıtılamayan özel bir karşılık olarak aynı iddiada yer alır.","sources":["JA","SI","TA"],"what_is_ar":"الخراج أو الجزية أو الرشوة التي يؤديها القوم أو الشخص","what_is_not_ar":"ليس الإيتاء بمعنى مطلق الإعطاء ولا ريع الزرع"},"support_links":[]},{"boundary":"Anlam yalnız devenin yürüyüşte ön ayaklarını geri getirme biçimini niteleyen kalıba bağlıdır.","branch_kind":"collocation","branch_ref":"root_000009/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"devenin ön ayaklarını geri getirişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve yürüyüş sırasında ön ayaklarını geri getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu hareket devenin yürüyüş niteliği olarak değerlendirilir."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devenin yürüyüşündeki belirli ön ayak hareketi adlandırıldığında kullanılır.","boundary_detail":"Anlam yalnız devenin yürüyüşte ön ayaklarını geri getirme biçimini niteleyen kalıba bağlıdır.","branch_image_ar":"رجع يدي الناقة في السير","concept_gloss":"devenin ön ayaklarını geri getirişi","definition":"Devenin yürürken ön ayaklarını ileri adımdan sonra düzenli biçimde geri getirme hareketidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve yürüyüş sırasında ön ayaklarını geri getirir."},{"facet_id":"F002","role":"specialization","statement":"Bu hareket devenin yürüyüş niteliği olarak değerlendirilir."}],"identity_rationale":"Kaynak ifadesi bütünüyle devenin yürüyüş sırasında ön ayaklarını geri getirme hareketini anlatır ve verilen dal sınırıyla örtüşür.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"devenin yürürken ön ayaklarını geri getirişi"}],"lexicalization_note":"Tanım devenin ön ayak hareketini bildiren kalıpla sınırlıdır; genel yürüyüş veya geliş anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel binek ayağı hareketi komşusu, deveye ve ön ayaklara özgü sınırı en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve ve ön ayaklarla sınırlıdır; komşu dal hayvan ve yürüyüş türü bakımından daha geniştir.","focus_only":"Odak dal özellikle devenin ön ayaklarını geri getirmesine bağlıdır.","gloss":"bineğin ayağını geri getirmesi","neighbor_only":"Komşu dal farklı bineklerin ayak hareketini, adımını ve bir yürüyüş türünden ötekine geçişini kapsar.","neighbor_ref":"root_000544/B008","relation_type":"near_synonym","shared_zone":"Her iki dal yürüyen bir hayvanın ayaklarını geri getirme hareketini anlatır."}],"source_phrase_ar":"ما أحسن أتو قوائم الناقة وأتيها في السير (jamhara)؛ ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير (sihah)؛ ما أحسن أتو يديها وأتي يديها يعني رجع يديها (tahdhib)","source_summary":"Kaynaklar, devenin yürüyüşünde ön ayakların geri getirilişini aynı hareket niteliği olarak tanımlar.","sources":["JA","SI","TA"],"what_is_ar":"أتو أو أتي يدي الناقة، أي رجع يديها في السير","what_is_not_ar":"ليس مطلق الإتيان ولا طريق الماء"},"support_links":[]},{"boundary":"Yol adı, yarış sonu ve konumsal hizalama aynı biçim ailesindeki ayrı kullanımlardır; biri ötekine indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000009/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"işlek ana yol, son sınır ve karşı hizası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanların kullandığı işlek veya yürünmüş ana yol adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolların birleştiği kavşak veya yolun belirgin ana kesimi anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yarış atlarının koşusunun ulaştığı son sınır adlandırılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir yapı başka bir yapının karşısında veya aynı hizasında bulunur."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yol ailesindeki temel adlar ile yarış sonu ve karşıda bulunma kullanımları topluca temsil edileceğinde kullanılır.","boundary_detail":"Yol adı, yarış sonu ve konumsal hizalama aynı biçim ailesindeki ayrı kullanımlardır; biri ötekine indirgenmez.","branch_image_ar":"الميتاء طريق ومحاذاة","concept_gloss":"işlek ana yol, son sınır ve karşı hizası","contextual_glosses":[{"applicability":"İnsanların yürüdüğü veya yolların birleştiği belirgin yol adlandırıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarış sonu ile bir yapının karşısında veya hizasında bulunma kullanımlarını dışarıda bırakır.","preserves":"İşlek ve yürünmüş yol anlamını korur."},"facet_ids":["F001","F002"],"text":"işlek ana yol","usage_role":"contextual"}],"definition":"İşlek veya yürünmüş ana yol, yolların birleştiği yer ya da yarış atlarının koşusunun bittiği son sınırdır. Bir konum kalıbında, bir evin karşısında veya onunla aynı hizada bulunmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanların kullandığı işlek veya yürünmüş ana yol adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Yolların birleştiği kavşak veya yolun belirgin ana kesimi anlatılır."},{"facet_id":"F003","role":"extension","statement":"Yarış atlarının koşusunun ulaştığı son sınır adlandırılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir yapı başka bir yapının karşısında veya aynı hizasında bulunur."}],"identity_rationale":"Kaynak ifadesi yarışın son sınırı, işlek ya da yürünmüş yol, yol kavşağı ve bir evin karşısında veya hizasında olma kullanımlarını açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yarışın son sınırı; işlek ana yol veya yol kavşağı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yarışın son sınırı veya yolun ana kesimi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir evin karşısında veya aynı hizasında"}],"lexicalization_note":"Yol ve son sınır bildiren adlar ile bir evin karşısında bulunmayı bildiren kalıp ayrı kapsamlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ana yol ve kavşak komşusu, dalın yol dışındaki yarış sonu ve hizalama kapsamlarını en iyi açığa çıkardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yol çekirdeğinin ötesinde yarış sonu ve konumsal hizalama kullanımlarına sahiptir; komşu dal bu uzantıları taşımaz.","focus_only":"Odak dal yarışın son sınırını ve bir yapının karşısındaki hizayı da kapsar.","gloss":"ana yol ve kavşak","neighbor_only":"Komşu dal yolun toplandığı ana cadde ve bu caddeyi tutma eylemiyle sınırlıdır.","neighbor_ref":"root_000214/B008","relation_type":"near_synonym","shared_zone":"Her iki dal işlek ana yol ve yolların birleştiği yer anlamında kesişir."}],"source_phrase_ar":"الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل (sihah)؛ الميتاء الطريق العامر ومجتمع الطريق (sihah)؛ داري بميتاء دار فلان وميداء دار فلان أي تلقاء داره ومحاذية لها (sihah)؛ طريق ميتاء مسلوك وميتاء الطريق وميداؤه محجته (tahdhib)","source_summary":"Toplu kanıt yol, kavşak ve yarış sonu anlamlarını; ayrıca yapıların karşı karşıya veya aynı hizada oluşunu bildiren kalıbı bir araya getirir.","sources":["SI","TA"],"what_is_ar":"الميتاء والميداء: آخر الغاية، والطريق العامر أو المسلوك، ومجتمع الطريق، ومحاذاة الدار","what_is_not_ar":"ليس مجيء الشخص ولا الجدول المائي"},"support_links":[]},{"boundary":"Dal yalnız belirtilen zarar ve tehdit kalıplarına bağlıdır; genel gelme eylemi veya her türlü yok oluş değildir.","branch_kind":"collocation","branch_ref":"root_000009/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"felakete uğramak, kaybetmek veya düşmanca ele geçirilmek","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ölüm, ağır hastalık, bela veya uzuv kırılması gibi ağır bir zarara uğrar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin malı yok olur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişi öldürülür, götürülür veya üzerinde üstünlük kurulur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Düşman kişiye yaklaşır ve tehdit oluşturur."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıttaki farklı zarar kalıplarının ortak olumsuz sonucunu topluca göstermek için kullanılır.","boundary_detail":"Dal yalnız belirtilen zarar ve tehdit kalıplarına bağlıdır; genel gelme eylemi veya her türlü yok oluş değildir.","branch_image_ar":"إتيان البلاء والهلاك","concept_gloss":"felakete uğramak, kaybetmek veya düşmanca ele geçirilmek","contextual_glosses":[{"applicability":"Ölüm, ağır hastalık, bela veya kırık gibi kişisel zarar anlatan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal kaybını, öldürülüp götürülmeyi ve düşmanın yaklaşmasını dışarıda bırakır.","preserves":"Kişinin ağır bir zarara uğramasını korur."},"facet_ids":["F001"],"text":"ağır bir felakete uğramak","usage_role":"contextual"}],"definition":"Belirli kalıplarda bir kişiye ölüm, ağır hastalık, bela veya kırık gelmesi; malının yok olması; öldürülüp götürülmesi ya da düşmanın ona yaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ölüm, ağır hastalık, bela veya uzuv kırılması gibi ağır bir zarara uğrar."},{"facet_id":"F002","role":"associated_use","statement":"Bir kişinin malı yok olur."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişi öldürülür, götürülür veya üzerinde üstünlük kurulur."},{"facet_id":"F004","role":"associated_use","statement":"Düşman kişiye yaklaşır ve tehdit oluşturur."}],"identity_rationale":"Kaynak ifadesi belirli kalıplarda kişiye ölüm, ağır hastalık, bela veya kırık gelmesini; malın yok olmasını; kişinin öldürülüp götürülmesini ve düşmanın yaklaşmasını destekler. Genel olarak gelişin iyi veya kötü olabileceği notu, bu dalın yalnız zararlı kalıplarını genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ölüm, ağır hastalık, bela veya kırığa uğramak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"malı yok olmak"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"uğruna öldürülmek, götürülmek veya yenilmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"düşman yaklaşmış olmak"}],"lexicalization_note":"Ölüm, hastalık, mal kaybı, yenilgi ve düşman yaklaşması anlamları yalnız kendi kalıplarında korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kökten yok oluş komşusu, zarar kalıpları ile doğrudan yok etme çekirdeği arasındaki farkı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal farklı zarar olaylarının kişiye veya malına erişmesini anlatan kalıplardır; komşu dalın çekirdeği doğrudan ve tam yok etmedir.","focus_only":"Odak dal ağır hastalık ve kırığı, mal kaybını, kişinin götürülmesini ve düşmanın yaklaşmasını ayrı kalıplarda kapsar.","gloss":"tümüyle yok etmek","neighbor_only":"Komşu dal bir şeyi bütünüyle yok etme ve kökünü kazıma eylemini merkez alır.","neighbor_ref":"root_000487/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal ölüm, kayıp ve ağır yıkım sonuçlarında kesişir."}],"source_phrase_ar":"أتى على فلان أتو أي موت أو بلاء أصابه (tahdhib)؛ الأتو المرض الشديد أو كسر يد أو رجل أو موت (tahdhib)؛ أتي على يد فلان إذا هلك له مال (tahdhib)؛ يؤتى دونه أي يذهب به ويغلب عليه (tahdhib)؛ أتي فلان إذا أطل عليه العدو (tahdhib)؛ الإتيان يقال في الخير وفي الشر (mufradat)","source_summary":"Toplu kanıt, farklı kalıplarda kişisel felaket, mal kaybı, öldürülme veya götürülme ve yaklaşan düşman tehdidini sıralar; genel gelişin olumlu da olabileceği ayrıca belirtilir.","sources":["TA","MU"],"what_is_ar":"أتى على فلان أتو: موت أو بلاء أو مرض شديد أو كسر، وهلاك المال، والقتل أو الذهاب به، وإطلال العدو","what_is_not_ar":"ليس مطلق المجيء المحايد ولا الإعطاء"},"support_links":[]},{"boundary":"Anlam yalnız dişi devenin çiftleşme isteğini bildiren kalıba bağlıdır; yürüyüş hareketi değildir.","branch_kind":"collocation","branch_ref":"root_000009/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"dişi devenin çiftleşmek istemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dişi deve çiftleşme isteği gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi deve erkek deveyi ister."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi devenin erkek deveye yönelen çiftleşme isteği anlatıldığında kullanılır.","boundary_detail":"Anlam yalnız dişi devenin çiftleşme isteğini bildiren kalıba bağlıdır; yürüyüş hareketi değildir.","branch_image_ar":"استئتاء الناقة","concept_gloss":"dişi devenin çiftleşmek istemesi","definition":"Dişi devenin çiftleşme isteği göstererek erkek deve istemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dişi deve çiftleşme isteği gösterir."},{"facet_id":"F002","role":"core","statement":"Dişi deve erkek deveyi ister."}],"identity_rationale":"Tek kaynaklı ifade, dişi devenin çiftleşme isteği gösterip erkeği istemesini doğrudan ve eksiksiz biçimde tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"dişi devenin çiftleşmek için erkek deve istemesi"}],"lexicalization_note":"Tanım dişi deve ve çiftleşme isteğini bildiren kalıpla sınırlıdır; başka hayvanlara yalın biçimde genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dişi toynaklının erkek istemesi dalı tür kapsamındaki farkı en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dişi deveyle sınırlıdır; komşu dal hayvan türü ve görülen belirtiler bakımından daha geniştir.","focus_only":"Odak dal yalnız dişi deveye özgüdür ve fiziksel belirtiyi zorunlu kılmaz.","gloss":"dişi hayvanın erkek istemesi","neighbor_only":"Komşu dal toynaklı dişileri genel olarak kapsar ve çiftleşme isteğine eşlik eden ıslaklığı da bildirebilir.","neighbor_ref":"root_001636/B002","relation_type":"near_synonym","shared_zone":"Her iki dal dişi bir toynaklının çiftleşmek için erkeği istemesini anlatır."}],"source_phrase_ar":"استأتت الناقة استئتاء مهموز أي ضبعت وأرادت الفحل (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Dişi devenin çiftleşme isteği gösterip erkek deve istemesi bu kalıpla tek başına tanıklanır."}],"source_summary":"Kanıt tek sözlükte yer alır ve dişi devenin çiftleşme isteğini belirli bir kalıpta bildirir.","sources":["SI"],"what_is_ar":"استئتاء الناقة: ضبعتها وإرادتها الفحل","what_is_not_ar":"ليس رجع يدي الناقة في السير"},"support_links":[]},{"boundary":"Anlam yalnız bir erkeği etkili ve işini yürütebilir diye niteleyen kalıba bağlıdır; yabancılık bildirmez.","branch_kind":"collocation","branch_ref":"root_000009/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","surface_ar":"يُؤْتِى"}],"gloss":"etkili ve işini yürüten adam","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sözü veya yaptığı iş etkisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi kararını uygulayıp işi sonuçlandırabilecek niteliktedir."}}],"root_ar":"ء ت ي","root_id":"root_000009","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir erkeğin sözü geçen ve kararını uygulayabilen biri olduğu anlatıldığında kullanılır.","boundary_detail":"Anlam yalnız bir erkeği etkili ve işini yürütebilir diye niteleyen kalıba bağlıdır; yabancılık bildirmez.","branch_image_ar":"نَفاذ الرجل","concept_gloss":"etkili ve işini yürüten adam","definition":"Sözü veya işi etkili olan, kararını uygulayıp işini yürütebilen adamdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sözü veya yaptığı iş etkisini gösterir."},{"facet_id":"F002","role":"core","statement":"Kişi kararını uygulayıp işi sonuçlandırabilecek niteliktedir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fiziksel güç ve genel kuvvet anlamlarını ekleyerek etkililik sınırını aşar.","collision":"Bedensel kuvveti anlatan kişi nitelemeleriyle karışabilir.","fit":"broadening","loses":null,"preserves":"Kişinin bir işi gerçekleştirebilme kapasitesini kısmen korur."},"text":"güçlü adam"}],"identity_rationale":"Tek kaynaklı ifade, belirli kişi nitelemesini doğrudan etkili, sözü veya işi geçen bir adam anlamında verir; yabancılık anlamıyla aynı biçimde olsa da semantik olarak ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"etkili ve işini yürütebilen adam"}],"lexicalization_note":"Tanım kişi niteleyen bu kalıpla sınırlıdır; genel güç, çaba veya yalın bir fiil anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; işte etkili olma komşusu kişi niteliği ile soyut yeterlik arasındaki farkı en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiyi niteleyen kalıptır; komşu dal ise iş üzerindeki nüfuz ve yürütme yetisini kavram olarak adlandırır.","focus_only":"Odak dal bu niteliği bir erkeğin kalıcı veya ayırt edici özelliği olarak bildirir.","gloss":"bir işte etkili olma","neighbor_only":"Komşu dal belirli bir işte nüfuz ve o işi yürütme gücünü soyut ad olarak kapsar.","neighbor_ref":"root_000625/B005","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi etkili biçimde yürütme ve sonuçlandırma gücünü anlatır."}],"source_phrase_ar":"رجل أتي إذا كان نافذا (maqayis)","source_qualifications":[{"kind":"sole_attestation","summary":"Bir erkeğin etkili ve işini yürütebilir oluşu bu kişi nitelemesiyle tek başına tanıklanır."}],"source_summary":"Kanıt tek sözlükte yer alır ve erkeği etkili, işi yürüyen veya hükmü geçen kişi olarak niteleyen özel bir kullanımdır.","sources":["MQ"],"what_is_ar":"وصف الرجل بأنه أَتِيّ، أي نافذ","what_is_not_ar":"ليس الغريب في قومه، وإن اتحد اللفظ"},"support_links":[]},{"boundary":"Bu dal, büyüme ve artmayı kapsar; ahlaki arınma, mali yükümlülük, uygunluk ve tek-çift karşıtlığı ayrı dallarda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B001","candidate_links":[{"candidate_id":"cand_8cc17107b0431dc9cad9","lane":"micro"},{"candidate_id":"cand_107e37a196c78dc2dda9","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","surface_ar":"يَتَزَكَّىٰ"}],"gloss":"büyüyüp artma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, bir şeyin önceki durumuna göre büyümesi ve artmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ekinin gelişmesi, herhangi bir şeyin çoğalması ve bir canlının dolgunlaşması bu artışın somut gerçekleşmeleridir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı açıklamalarda büyüme, ilahi iyiliğin sağladığı verim ve bollukla ilişkilendirilir."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin gelişme, miktar veya dolgunluk bakımından önceki durumunu aşmasını anlatan genel karşılıktır.","boundary_detail":"Bu dal, büyüme ve artmayı kapsar; ahlaki arınma, mali yükümlülük, uygunluk ve tek-çift karşıtlığı ayrı dallarda kalır.","branch_image_ar":"النماء والزيادة","concept_gloss":"büyüyüp artma","contextual_glosses":[{"applicability":"Ekinin veya başka bir varlığın zaman içinde büyüyerek miktarca artması anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süreç içindeki gelişmeyi ve bunun sonucundaki artışı birlikte korur."},"facet_ids":["F001","F002"],"text":"gelişip çoğalmak","usage_role":"contextual"},{"applicability":"Artışın verim ve iyilikle gelen bolluk yönü özellikle öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk niteliği taşımayan yalın büyüme ve dolgunlaşma kullanımlarını kapsamaz.","preserves":"Verim ve bollukla sonuçlanan artış yönünü korur."},"facet_ids":["F003"],"text":"bolluk kazanmak","usage_role":"contextual"}],"definition":"Bir varlığın gelişerek büyümesi, miktarının artması veya daha dolgun ve verimli duruma gelmesidir. Bu gelişme kimi anlatımlarda ilahi iyiliğin doğurduğu bolluk olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, bir şeyin önceki durumuna göre büyümesi ve artmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Ekinin gelişmesi, herhangi bir şeyin çoğalması ve bir canlının dolgunlaşması bu artışın somut gerçekleşmeleridir."},{"facet_id":"F003","role":"source_variant","statement":"Bazı açıklamalarda büyüme, ilahi iyiliğin sağladığı verim ve bollukla ilişkilendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gelişme, dolgunlaşma ve verim kazanma yönlerini dışarıda bırakır.","preserves":"Miktarca artma yönünü korur."},"text":"yalnızca çoğalma"}],"identity_rationale":"Kaynak ifadesi, ortak çekirdeği bir şeyin büyümesi, miktarca artması veya dolgunlaşması olarak açıkça kurar; ekin, genel varlıklar ve bollukla gelişme bu çekirdeğin farklı gerçekleşmeleridir. İlahi iyilikle elde edilen gelişme, çekirdeği değiştiren ayrı bir anlam değil, artışın kaynağını belirten bir açıklamadır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"büyümek, artmak ve verim kazanmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"büyüme ve artış"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"gelişmiş ve artışı belirgin"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu büyütüp artırdı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ekin büyüyüp arttı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişi bolluğa kavuşup rahat yaşadı"}],"lexicalization_note":"Yalın biçimlerdeki büyüme çekirdeği ile ekin, kişi ve ettirgenlik bildiren sınırlı kullanımlar ayrı tutulur; bu kullanımlar bütün dalı tek bir bağlama daraltmaz.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; büyüme sınırını en açık gösteren beş karşılaştırma seçildi, yağmur, verimli arazi, su bolluğu, uygunluk ve tek-çift alanındaki daha uzak adaylar yayıma alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değişimin kendisini, yani büyüyüp artmayı bildirir; komşu dal ise ortaya çıkan çokluk ve bolluk durumunu, daha geniş alanlarla birlikte öne çıkarır.","focus_only":"Odak dal, herhangi bir şeyin büyüme ve dolgunlaşma sürecini doğrudan adlandırır.","gloss":"büyüme ile bolluk","neighbor_only":"Komşu dal, malda, toplulukta veya soyda çokluğu ve uğurlu bolluğu daha geniş biçimde kapsar.","neighbor_ref":"root_000051/B004","relation_type":"near_synonym","shared_zone":"İki dal da artış, verim ve bolluk fikrinde kesişir."},{"boundary_match":"partial","distinction":"Odak dal süreç ve gelişme merkezlidir; komşu dal ise asla eklenen fazlalık ile ürün, yiyecek ve hayvan gibi alanlardaki verim ölçüsünü belirginleştirir.","focus_only":"Odak dal, genel büyümeyi ve ilahi iyilikle gelen gelişmeyi de kapsar.","gloss":"artma ile fazlalık","neighbor_only":"Komşu dal, özellikle asıl miktarın üzerindeki fazlayı ve belirli üretim alanlarındaki verim artışını öne çıkarır.","neighbor_ref":"root_000618/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir başlangıç durumunu aşan büyüme ve artışı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği nicel ya da gelişimsel artıştır; komşu dalın çekirdeği ise kişinin geçim durumunu düzeltmek veya güçlendirmektir.","focus_only":"Odak dal, varlığın kendisinde gerçekleşen büyüme ve miktar artışını bildirir.","gloss":"artış ile durumun düzelmesi","neighbor_only":"Komşu dal, bir kişinin geçim ve varlık durumunun yardım ya da güçlendirmeyle düzelmesini kapsar.","neighbor_ref":"root_000617/B004","relation_type":"near_neighbor","shared_zone":"İki dal da daha iyi ve daha varlıklı bir duruma geçişi çağrıştırabilir."},{"boundary_match":"opposed","distinction":"Odak dal olumlu büyüme kutbunu, komşu dal ise bitki üretmeyen toprağın olumsuz kutbunu gösterir; kapsamları tam karşıt sözcükler olacak kadar eşit değildir.","focus_only":"Odak dal, ekin dahil olmak üzere varlıkların gelişip artmasını geniş biçimde kapsar.","gloss":"gelişme ile verimsizlik","neighbor_only":"Komşu dal, özellikle hiçbir şey bitirmeyen verimsiz toprağı adlandırır.","neighbor_ref":"root_001321/B003","relation_type":"polarity_pair","shared_zone":"İki dal, toprağın veya ürünün gelişme ve verim ekseninde karşılaştırılabilir."},{"boundary_match":"partial","distinction":"Büyüme dalında belirleyici unsur artıştır; arınma dalında ise kusurdan uzaklaşıp temiz ve doğru duruma gelmektir.","focus_only":"Odak dal, fiziksel veya nicel büyümeyi, çoğalmayı ve dolgunlaşmayı içerir.","gloss":"gelişme ile arınma","neighbor_only":"Komşu dal, ahlaki temizlik, doğruluk ve birini bu duruma getirme anlamlarını içerir.","neighbor_ref":"root_000637/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal daha iyi bir duruma geçiş düşüncesinde yaklaşabilir."}],"source_phrase_ar":"أصل يدل على نماء وزيادة (maqayis)؛ زكا الزرع يزكو زكاء ازداد ونما وكل شيء ازداد ونما فهو يزكو زكاء (ayn)؛ زكا الزرع يزكو زكاء ممدود أي نما (sihah)؛ كل شيء يزداد ويسمن فهو يزكو زكاء (tahdhib)؛ أصل الزكاة النمو الحاصل عن بركة الله تعالى (mufradat)","source_summary":"Kaynakların ortak anlatımı büyüme ve artmayı merkeze alır; ekin gelişmesi, genel çoğalma, dolgunlaşma ve iyilikle gelen verim bu ortak anlamın kapsamındadır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه نماء الزرع وزيادة الشيء وسمنه وبركته وخصب الرجل وتنعمه.","what_is_not_ar":"لا يدخل فيه معنى الزكاة المالية إلا من جهة كونها سببا للنماء أو البركة، ولا معنى الزوج والشفع."},"support_links":["sup_1d73dfb73c1b46debef4","sup_2a7d73f23e85348cfd4f"]},{"boundary":"Bu dal ahlaki ve manevi temizlik ile düzgünlüğü kapsar; yalın büyüme ve maldan ödenen zorunlu pay kendi dallarına aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B002","candidate_links":[{"candidate_id":"cand_44bb0198bb7ffca9c530","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","surface_ar":"يَتَزَكَّىٰ"}],"gloss":"ahlaken arınıp düzgünleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, ahlaki veya manevi bakımdan temiz ve düzgün durumda olmaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin bu niteliği taşıması, doğru davranan ve kötülükten sakınan biri olmasıyla belirginleşir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Anlam, bir kişiyi veya iç dünyayı arındırıp düzeltme ve iyiliklerle geliştirme eylemine uzanır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yiyecek için kullanıldığında dinen izin verilen, iyi ve sonradan zarar doğurmayan seçeneği belirtir."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Maldan verilen zorunlu payın temizleyici sayılması, bu ahlaki temizlik alanıyla kurulan açıklayıcı bir bağlantıdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin veya iç durumun kusurdan uzaklaşıp temiz, doğru ve sakınan bir niteliğe kavuşmasını anlatan temel karşılıktır.","boundary_detail":"Bu dal ahlaki ve manevi temizlik ile düzgünlüğü kapsar; yalın büyüme ve maldan ödenen zorunlu pay kendi dallarına aittir.","branch_image_ar":"الطهارة والصلاح","concept_gloss":"ahlaken arınıp düzgünleşme","contextual_glosses":[{"applicability":"Bir kişiyi veya onun iç dünyasını temizleyip ahlaken daha iyi duruma getirme eyleminde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Arındırma ile doğru duruma getirme eylemlerini birlikte korur."},"facet_ids":["F003"],"text":"arındırıp düzeltmek","usage_role":"contextual"},{"applicability":"Yiyecek seçiminin izin verilir ve sonradan zarar vermeyecek nitelikte olduğunu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yiyeceğin izin verilir oluşunu ve iyi sonucunu birlikte korur."},"facet_ids":["F004"],"text":"dinen uygun ve sonu iyi","usage_role":"contextual"}],"definition":"Bir kişinin veya iç durumun kusurdan arınıp ahlaken temiz, doğru ve sakınan bir niteliğe kavuşması ya da bir başkasının onu bu duruma getirmesidir. Yiyecek bağlamında dinen izin verilen ve sonu zarar getirmeyen olmayı da anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, ahlaki veya manevi bakımdan temiz ve düzgün durumda olmaktır."},{"facet_id":"F002","role":"specialization","statement":"Bir kişinin bu niteliği taşıması, doğru davranan ve kötülükten sakınan biri olmasıyla belirginleşir."},{"facet_id":"F003","role":"extension","statement":"Anlam, bir kişiyi veya iç dünyayı arındırıp düzeltme ve iyiliklerle geliştirme eylemine uzanır."},{"facet_id":"F004","role":"specialization","statement":"Yiyecek için kullanıldığında dinen izin verilen, iyi ve sonradan zarar doğurmayan seçeneği belirtir."},{"facet_id":"F005","role":"associated_use","statement":"Maldan verilen zorunlu payın temizleyici sayılması, bu ahlaki temizlik alanıyla kurulan açıklayıcı bir bağlantıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ahlaki düzgünlük, sakınma ve birini daha iyi duruma getirme yönlerini eksiltir.","preserves":"Kusurdan uzak olma yönünü korur."},"text":"yalnızca temizlik"}],"identity_rationale":"Kaynak ifadesi temizlik, düzgünlük ve sakınmayı aynı ahlaki çekirdekte birleştirir; birini düzeltip arındırma, iç temizliği ve dinen uygun olup kötü sonuç doğurmayan yiyecek bu çekirdeğin bağlama bağlı açılımlarıdır. Mali payın temizleyici sayılması burada yalnız anlam ilişkisini açıklar; mali uygulamanın kendisi ayrı dalda tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"arınmak ve düzgünleşmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"temiz, doğru ve kötülükten sakınan"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"arındırıp düzeltmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"arındırma, düzeltme ve iyiliklerle geliştirme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iç temizliği ve ahlaki düzgünlük"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kendini övmek veya sözle temiz saymak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"dinen uygun ve sonu zarar vermeyen yiyecek"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"temizlik ve düzgünlük"}],"lexicalization_note":"Yalın temizlik ve düzgünlük anlamı; kişiyi düzeltme, iç dünya, kendini övme ve yiyeceğin uygunluğu gibi yapıya bağlı kullanımlarla karıştırılmadan sunulur.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; ahlaki temizlik ve düzgünlük sınırını en iyi açıklayan beş aday seçildi, doğruluk, sakınma, kir, büyüme, uygunluk ve tek-çift alanındaki daha uzak adaylar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı ahlaki doğruluk ve bağlama bağlı uygunluktur; komşu dalın sınırı ise daha genel arıtma, uzak tutma ve kutsama alanına yayılır.","focus_only":"Odak dal, ahlaki düzgünlüğü, sakınan kişiyi ve yiyeceğin dinen uygun sonucunu da kapsar.","gloss":"ahlaki arınma ile genel arıtma","neighbor_only":"Komşu dal, arıtma yanında yüceltme, kutsama ve bunlara bağlı iyiliği daha geniş biçimde kapsar.","neighbor_ref":"root_001206/B001","relation_type":"near_synonym","shared_zone":"İki dal da kirden veya kusurdan uzaklaştırıp temiz duruma getirme fikrinde birleşir."},{"boundary_match":"partial","distinction":"Odak dal kişilik ve davranış değerini belirler; komşu dal ise bir karışımı, kiri veya bulanıklığı gidererek saflaştırma sürecini öne çıkarır.","focus_only":"Odak dal, ahlaki düzgünlük ve kötülükten sakınma niteliğini içerir.","gloss":"ahlaki arınma ile arıtma","neighbor_only":"Komşu dal, karışmış veya kirlenmiş bir şeyi süzüp arı ve duru hale getirme işlemini içerir.","neighbor_ref":"root_000430/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal, istenmeyen bir unsurdan kurtulup temiz hale gelmeyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal ahlaki arınma ve düzgünlüğe bağlıdır; komşu dal ise duyu, gönül ve din ölçülerindeki her türlü iyi ve hoş niteliğe uzanır.","focus_only":"Odak dal, arınıp ahlaken düzgünleşme sürecini ve bu niteliği özellikle öne çıkarır.","gloss":"arınmışlık ile iyi ve temiz olma","neighbor_only":"Komşu dal, duyusal hoşluk, temiz oluş, yararlılık ve dinen izin verilirlik gibi çok daha geniş bir iyi olma alanını kapsar.","neighbor_ref":"root_000961/B001","relation_type":"near_synonym","shared_zone":"İki dal, temiz, doğru ve dinen uygun sayılan şeylerde örtüşür."},{"boundary_match":"opposed","distinction":"Odak olumlu arınma ve doğruluk kutbunu, komşu ise bozulma ve kötülük kutbunu gösterir; odaktaki arındırma süreci komşuda bulunmaz.","focus_only":"Odak dal, arınmış, doğru ve sakınan olmayı veya bu duruma gelmeyi bildirir.","gloss":"düzgünlük ile bozukluk","neighbor_only":"Komşu dal, bozulmuş, kötü ve düzgünlüğün karşıtı olan durumu bildirir.","neighbor_ref":"root_000944/B005","relation_type":"polarity_pair","shared_zone":"İki dal ahlaki veya niteliksel düzgünlük ekseninin karşı kutuplarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal kişinin temiz ve düzgün niteliğine veya arındırılmasına yönelir; komşu dal ise yapılan iyi işlerin ve bağlılığın geniş kapsamına yönelir.","focus_only":"Odak dal, iç temizliği ve kusurdan arınarak düzgün duruma gelmeyi öne çıkarır.","gloss":"arınmışlık ile iyilik","neighbor_only":"Komşu dal, inanç ve davranış alanındaki iyilik ve görevleri geniş bir eylem alanı olarak kapsar.","neighbor_ref":"root_000104/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal doğru davranış, sakınma ve ahlaki iyilik alanında buluşur."}],"source_phrase_ar":"الطهارة زكاة المال؛ زكاة لأنها طهارة (maqayis)؛ والزكاة الصلاح؛ رجل زكي تقي (ayn)؛ معناه صلاحا؛ ما صلح؛ أي يصلح (tahdhib)؛ بزكاء النفس وطهارتها؛ حلالا لا يستوخم عقباه (mufradat)","source_summary":"Ortak anlatım temizlik ve düzgünlüğü, kişinin sakınan niteliğini, birini düzeltip arındırmayı ve iç temizliğini birleştirir; yiyeceğin dinen uygun ve sonucu iyi olması da bağlama bağlı bir açılımdır.","sources":["MQ","AY","TA","MU"],"what_is_ar":"يدخل فيه التطهير والتزكية والصلاح والتقوى وزكاء النفس أو الشخص، ومنه الطعام الأزكى بمعنى الحلال الطيب العاقبة.","what_is_not_ar":"لا يدخل فيه مجرد الزيادة الحسية في الزرع والمال إلا إذا جعلتها المصادر وجها للتزكية، ولا يدخل فيه الشفع والزوج."},"support_links":["sup_fda4e2db2bba27fe0669"]},{"boundary":"Bu dal maldan çıkarılan payı ve verme eylemini kapsar; genel arınma, büyüme veya başka tür bir yükümlülük bu sınırı tek başına karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","surface_ar":"يَتَزَكَّىٰ"}],"gloss":"yoksula verilmesi gereken mal payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, maldan yoksullara ayrılan ve dinen onların hakkı sayılan paydır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam, mal için gereken payı çıkarıp hak sahiplerine ödeme eylemini de kapsar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Maldan karşılıksız yardımda bulunmak, zorunlu payla aynı verme alanında yer alan daha genel bir kullanımdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maldan dinen hak sahibi yoksullara ayrılan payın kendisini ve bu paya dayalı mali yükümlülüğü anlatır.","boundary_detail":"Bu dal maldan çıkarılan payı ve verme eylemini kapsar; genel arınma, büyüme veya başka tür bir yükümlülük bu sınırı tek başına karşılamaz.","branch_image_ar":"زكاة المال والصدقة","concept_gloss":"yoksula verilmesi gereken mal payı","contextual_glosses":[{"applicability":"Bir kişinin malı için ayrılması gereken payı hak sahiplerine ödediği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gerekli payı maldan çıkarma ve hak sahibine verme eylemini korur."},"facet_ids":["F002"],"text":"gereken mal payını vermek","usage_role":"contextual"},{"applicability":"Zorunlu payın özel sınırı belirtilmeden, kişinin malıyla karşılıksız yardım etmesi anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maldan başkasına karşılıksız verme eylemini korur."},"facet_ids":["F003"],"text":"malından karşılıksız vermek","usage_role":"contextual"}],"definition":"Bir kişinin malından, dinen hak sahibi sayılan yoksullara vermesi gereken pay ve bu payı mal adına çıkarıp ödeme eylemidir. Aynı alan, maldan karşılıksız yardımda bulunma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, maldan yoksullara ayrılan ve dinen onların hakkı sayılan paydır."},{"facet_id":"F002","role":"extension","statement":"Anlam, mal için gereken payı çıkarıp hak sahiplerine ödeme eylemini de kapsar."},{"facet_id":"F003","role":"associated_use","statement":"Maldan karşılıksız yardımda bulunmak, zorunlu payla aynı verme alanında yer alan daha genel bir kullanımdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Dinen belirlenmiş payın dışında kalan her türlü isteğe bağlı yardımı ana anlama katar.","collision":"Zorunlu mal payı ile isteğe bağlı yardım arasındaki sınırı belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Karşılıksız mal verme yönünü korur."},"text":"genel bağış"}],"identity_rationale":"Kaynak ifadesi, maldan yoksullara verilmesi dinen hak sayılan payı, bu payı ödeme eylemini ve karşılıksız mal vermeyi aynı mali yardım alanında toplar. Dal bu nedenle salt ahlaki temizlik olarak değil, malın belirli bir bölümünü hak sahibine çıkarma ve verme uygulaması olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yoksullara verilmesi gereken mal payı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"malının gereken payını ödemek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"malından karşılıksız vermek"}],"lexicalization_note":"Mali payı adlandıran biçim, payı ödeme yapısı ve karşılıksız verme eylemi ayrı gerçekleşmeler olarak korunur; anlam genel yardım veya genel arınma diye genişletilmez.","neighbor_coverage_note":"Sunulan on adayın tamamı değerlendirildi; mali payın yardım, arınma, bedel ve yükümlülük alanlarından ayrımını gösteren dört aday seçildi, akıl eksikliği, sapma, iç körlük, büyüme, uygunluk ve tek-çift adayları anlamsal sınırı keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirlenmiş pay ve onun ödenmesiyle sınırlıdır; komşu dal isteğe bağlı yardım, haktan vazgeçme ve tahsil görevi gibi ek katılımcı ve işlemlere uzanır.","focus_only":"Odak dal, yoksullara verilmesi gereken belirli mal payını ve bu payı ödeme eylemini öne çıkarır.","gloss":"zorunlu pay ile mali yardım","neighbor_only":"Komşu dal, karşılıksız verilen malı, bir haktan vazgeçmeyi ve yardım payını alan görevliyi daha geniş biçimde kapsar.","neighbor_ref":"root_000852/B006","relation_type":"near_synonym","shared_zone":"İki dal da maldan hak sahibine karşılıksız aktarım ve belirli mali hak alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal somut bir mali hak ve aktarım uygulamasıdır; komşu dal ise ahlaki veya manevi bir nitelik ve dönüşümdür.","focus_only":"Odak dal, maldan yoksullara aktarılan payı ve ödeme eylemini bildirir.","gloss":"mali pay ile arınma","neighbor_only":"Komşu dal, kişinin ahlaken arınmış ve düzgün niteliğini veya bu duruma getirilmesini bildirir.","neighbor_ref":"root_000637/B002","relation_type":"near_neighbor","shared_zone":"Mali payın temizleyici sayılması iki dal arasında açıklayıcı bir bağ kurar."},{"boundary_match":"field_only","distinction":"Odakta alıcı yoksul ve verilen şey onun hakkı olan mal payıdır; komşuda verilen şey bir kişi veya yükümlülük yerine geçen kurtarma ya da karşılama bedelidir.","focus_only":"Odak dal, yoksulların hakkı sayılan mal payını düzenli bir mali yükümlülük olarak verir.","gloss":"hak payı ile kurtarma bedeli","neighbor_only":"Komşu dal, bir kişiyi kurtarmak, bir zararı gidermek veya bir ibadet borcunu karşılamak için mal ya da canı bedel kılar.","neighbor_ref":"root_001136/B001","relation_type":"same_field","shared_zone":"İki dal da dini veya ahlaki bir gerekçeyle değerli bir şeyi elden çıkarma alanındadır."},{"boundary_match":"thematic_only","distinction":"Odak, yükümlülüğün konusu olan mal payının verilmesini tanımlar; komşu ise yükümlülüğü kişinin üzerine koyma işlemini, ödeme şartı olmadan tanımlar.","focus_only":"Odak dal, belirli bir mal payını hak sahibine fiilen aktarmayı içerir.","gloss":"mali yükümlülük ile görevlendirme","neighbor_only":"Komşu dal, herhangi bir işi, görevi veya inancı bir kişinin sorumluluğuna yüklemeyi içerir.","neighbor_ref":"root_001249/B004","relation_type":"thematic","shared_zone":"Her iki dal kişiye bağlanan bir yükümlülük düşüncesinde aynı senaryoya katılır."}],"source_phrase_ar":"زكاة المال (maqayis;ayn;sihah;tahdhib)؛ زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق (sihah)؛ ما يخرج الإنسان من حق الله تعالى إلى الفقراء (mufradat)","source_summary":"Kaynaklar maldan ayrılan bilinen payı ortak biçimde tanır; payın mal adına ödenmesi, yoksullara aktarılması ve karşılıksız mal verme eylemi aynı anlatımda bir araya gelir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه زكاة المال المعروفة وأداء الزكاة والتصدق وما يخرج من حق الله تعالى إلى الفقراء، مع تعليلها بالتطهير أو النماء أو البركة.","what_is_not_ar":"لا يدخل فيه كل صلاح أو طهارة مجردة إلا إذا كان الكلام على الزكاة المالية أو عملها."},"support_links":[]},{"boundary":"Anlam, bir işin kişiye yakışmadığını veya durumuna uygun düşmediğini bildiren yapıyla sınırlıdır; genel uyum alanına taşınmaz.","branch_kind":"collocation","branch_ref":"root_000637/B004","candidate_links":[{"candidate_id":"cand_06c6ae616da4d61b813c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","surface_ar":"يَتَزَكَّىٰ"}],"gloss":"yakışmamak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş veya durum, değerlendirilen kişiye yakışmaz ve onun haliyle bağdaşmaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değerlendirme kaynakta olumsuz yapı içinde verilir ve genel uygunluk bildiren bağımsız bir anlama genişletilmez."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin veya durumun belirli bir kişiye uygun olmadığını ve onun konumuyla bağdaşmadığını anlatan yapı için kullanılır.","boundary_detail":"Anlam, bir işin kişiye yakışmadığını veya durumuna uygun düşmediğini bildiren yapıyla sınırlıdır; genel uyum alanına taşınmaz.","branch_image_ar":"الملاءمة واللياقة","concept_gloss":"yakışmamak","contextual_glosses":[{"applicability":"Bir davranışın veya işin kişinin hali, konumu ya da niteliğiyle bağdaşmadığı söylenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli kişiye göre kurulan uygunsuzluk ve bağdaşmazlık yargısını korur."},"facet_ids":["F001","F002"],"text":"ona uygun düşmemek","usage_role":"contextual"}],"definition":"Belirli bir işin, davranışın veya durumun bir kişiye yakışmadığını ve onun konumuna ya da haline uygun düşmediğini bildiren kalıplaşmış bir değerlendirmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş veya durum, değerlendirilen kişiye yakışmaz ve onun haliyle bağdaşmaz."},{"facet_id":"F002","role":"specialization","statement":"Değerlendirme kaynakta olumsuz yapı içinde verilir ve genel uygunluk bildiren bağımsız bir anlama genişletilmez."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İki tarafın zaman içinde birbirine ayak uydurması anlamını ekler.","collision":"Karşılıklı uyum süreciyle karışır.","fit":"displacement","loses":"Belirli bir işin kişiye yakışmadığını bildiren olumsuz değerlendirmeyi ortadan kaldırır.","preserves":"Uygunluk alanıyla olan genel ilişkiyi korur."},"text":"uyum sağlamak"}],"identity_rationale":"Kaynak ifadesi uygunluk alanını doğrular, ancak tanıklıklar bunu özellikle bir işin veya durumun kişiye uygun düşmediğini söyleyen olumsuz yapıda verir. Bu nedenle dal korunabilir, fakat genel ve bağımsız bir uygunluk anlamına genişletilmeden söz konusu yapı içinde tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ona yakışmamak veya durumuna uygun düşmemek"}],"lexicalization_note":"Tanım yalnız kaynakta verilen olumsuz uygunluk yapısına bağlıdır; kökün tek başına her türlü uygunluk veya uyum bildirdiği varsayılmaz.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; uygunluk sınırını doğrudan aydınlatan dört aday seçildi, kınama, kusuru görmezden gelme, ayıplama, kötüleme, büyüme, arınma ve tek-çift alanları yalnız uzak çağrışım taşıdığı için yayıma alınmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olumsuz ve yapıya bağlı bir yargıdır; komşu dal olumlu ya da olumsuz değerlendirilebilen daha genel yakışma alanına sahiptir.","focus_only":"Odak dal, kaynakta yalnız bir işin kişiye yakışmadığını bildiren belirli olumsuz yapıyla sınırlıdır.","gloss":"yakışmamak ile yakışmak","neighbor_only":"Komşu dal, bir şeyin kişiye uygun veya güzel düşmesi alanını daha genel biçimde kapsar.","neighbor_ref":"root_001391/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir iş veya şey ile kişi arasındaki yakışma ve uygunluk yargısını anlatır."},{"boundary_match":"partial","distinction":"Odak dal yalnız uygunsuzluk hükmü verir; komşu dal ise kişinin ihtiyacına veya durumuna uygunluğu genel bir ilişki olarak kurar.","focus_only":"Odak dal, bir işin kişiye yakışmadığını belirten olumsuz değerlendirmeyi taşır.","gloss":"yakışmama ile uygun olma","neighbor_only":"Komşu dal, bir şeyin kişi için işe yarar ve uygun olmasını olumlu yönden de bildirebilir.","neighbor_ref":"root_000876/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin kişiye uygun düşüp düşmediğini değerlendirir."},{"boundary_match":"partial","distinction":"Odakta ilişki bir iş ile kişi arasında ve değerlendirme yönlüdür; komşuda iki tarafın karşılıklı uygunluğu veya görüş birliği belirleyicidir.","focus_only":"Odak dal, bir işin kişinin haline yakışıp yakışmadığına ilişkin değer yargısı taşır.","gloss":"yakışma ile karşılıklı uyum","neighbor_only":"Komşu dal, iki şeyin veya görüşün aynı yönde buluşmasını ve karşılıklı uyuşmasını anlatır.","neighbor_ref":"root_001668/B001","relation_type":"near_neighbor","shared_zone":"İki dal, iki unsur arasında bağdaşma bulunup bulunmadığını sorgular."},{"boundary_match":"partial","distinction":"Odak kişiye yakışma ölçütüne bağlıdır; komşu ise yapılması doğru olanı veya ulaşılabilir sonucu değerlendiren daha geniş bir alan taşır.","focus_only":"Odak dal, bir davranışın kişiye yakışmaması ve haliyle bağdaşmaması yargısını verir.","gloss":"yakışmama ile doğru bulma","neighbor_only":"Komşu dal, bir işi yapmanın doğru veya beklenebilir olup olmadığını ve istenen sonuca erişmeyi kapsar.","neighbor_ref":"root_001572/B003","relation_type":"near_neighbor","shared_zone":"İki dal, bir davranışın kişi bakımından yerinde olup olmadığını değerlendirebilir."}],"source_phrase_ar":"أمر لا يزكو بفلان أي لا يليق به (maqayis;sihah)؛ وهذا الأمر لا يزكو أي لا يليق (ayn)؛ هذا الأمر لا يزكو بفلان أي لا يليق به (tahdhib)","source_summary":"Kaynakların ortak anlatımı, bir işin veya durumun belirli bir kişiye yakışmadığını ve onun haline uygun düşmediğini bildiren olumsuz değerlendirmede birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه قولهم لا يزكو بفلان أي لا يليق به أو لا يناسب حاله.","what_is_not_ar":"لا يدخل فيه زكاء المال أو النفس ولا معنى الزوج والشفع."},"support_links":["sup_8038e12b74ed5c66816f"]},{"boundary":"Bu dal çift ve tek karşıtlığıyla sınırlıdır; büyüme, arınma, mali pay ve uygunluk anlamlarıyla birleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000637/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","surface_ar":"يَتَزَكَّىٰ"}],"gloss":"çift olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, tek olanın karşıtı olarak çift veya iki öğeli olma durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sabit karşılaştırma sözünde tek ve çift seçenekleri birbirine karşı konur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Avuçta saklanan bir şeyin tek mi çift mi olduğunu sorma ve tahmin etme, karşıtlığın oyun içindeki kullanımıdır."}}],"root_ar":"ز ك و","root_id":"root_000637","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin tek değil, iki öğeli veya çift sayıda olduğunu bildiren genel karşılıktır.","boundary_detail":"Bu dal çift ve tek karşıtlığıyla sınırlıdır; büyüme, arınma, mali pay ve uygunluk anlamlarıyla birleştirilmez.","branch_image_ar":"الزوج والشفع","concept_gloss":"çift olma","contextual_glosses":[{"applicability":"İki seçeneği karşılaştıran sözde veya avuçta saklanan şeyin sayısını tahmin etme oyununda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek ile çift arasındaki karşıtlığı ve soru işlevini korur."},"facet_ids":["F002","F003"],"text":"tek mi çift mi","usage_role":"contextual"}],"definition":"Bir şeyin tek değil, iki öğeli veya çift sayıda olduğunu bildiren anlamdır. Tek-çift karşıtlığını kuran sözlerde ve avuçta saklanan bir şeyin tek mi çift mi olduğunu tahmin etme oyununda özel olarak kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, tek olanın karşıtı olarak çift veya iki öğeli olma durumudur."},{"facet_id":"F002","role":"specialization","statement":"Sabit karşılaştırma sözünde tek ve çift seçenekleri birbirine karşı konur."},{"facet_id":"F003","role":"associated_use","statement":"Avuçta saklanan bir şeyin tek mi çift mi olduğunu sorma ve tahmin etme, karşıtlığın oyun içindeki kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Birbirine denk olma, benzerlik veya evlilikteki taraf anlamlarını gereksiz yere ekler.","collision":"Sayısal çiftlik ile denk veya evli taraf anlamları birbirine karışır.","fit":"broadening","loses":null,"preserves":"İki öğenin birlikte düşünülmesi yönünü kısmen korur."},"text":"eş"}],"identity_rationale":"Kaynak ifadesi sözcüğü çift veya iki öğeden oluşan taraf için açıkça tanımlar ve onu tek olanın karşısına koyar. Avuçta saklanan şey üzerine sorulan tek-çift sorusu ile buna eşlik eden söyleyiş, aynı karşıtlığın oyun ve tahmin bağlamındaki özel kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"çift veya iki öğeli"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tek veya çift"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"avuçtaki çift mi tek mi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"avuçtaki şey için tek-çift söylemek"}],"lexicalization_note":"Çift olmayı adlandıran biçim ile tek-çift karşıtlığını kuran sözler ve avuçtaki şey üzerine söylenen oyun yapıları ayrı kapsamlarıyla korunur.","neighbor_coverage_note":"Sunulan on bir adayın tamamı değerlendirildi; çiftlik sınırını iki oluşturma, eşleşmiş ikili, iki öğeyi kapsama ve özel ikili adlarından ayıran dört aday seçildi, çift organlar, varsayım, on sayısına tamamlama, tahmin, büyüme, arınma ve uygunluk alanları dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sayısal tek-çift karşıtlığına açıktır; komşu dal ise benzer, karşıt veya tamamlayıcı iki öğenin birbirine eşlik etmesini öne çıkarır.","focus_only":"Odak dal, tek sayının karşıtı olan çiftliği ve tek-çift tahmin sözünü kapsar.","gloss":"çift sayı ile eşleşmiş ikili","neighbor_only":"Komşu dal, birbirine bağlanan iki öğenin her birini veya birlikte oluşturdukları karşılıklı çifti kapsar.","neighbor_ref":"root_000652/B001","relation_type":"near_synonym","shared_zone":"İki dal da tek olmayan, iki öğeli bir bütün veya çift fikrinde örtüşür."},{"boundary_match":"partial","distinction":"Odak bir sınıflandırma ve durumdur; komşu ise bir öğeye ikincisini katıp iki oluşturma sürecidir.","focus_only":"Odak dal, ortaya çıkmış çiftlik durumunu ve bunun tek olanla karşıtlığını adlandırır.","gloss":"çift olma ile ikiye çıkarma","neighbor_only":"Komşu dal, bire bir ekleyerek iki oluşturma, ikinci olma veya bir şeyi ikileme işlemini anlatır.","neighbor_ref":"root_000208/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal iki öğe ve iki sayısı çevresinde buluşur."},{"boundary_match":"field_only","distinction":"Odak dal çift olma niteliğini verir; komşu dal ise adı anılan iki öğeyi eksiksiz kapsayan dil bilgisel araçları konu edinir.","focus_only":"Odak dal, tek olanın karşıtı olarak çiftliği ve tahmin oyunundaki seçeneği bildirir.","gloss":"çiftlik ile ikisini birden kapsama","neighbor_only":"Komşu dal, iki varlığın ikisini birden kapsayan dil bilgisel ifadeleri ve onların kullanım kurallarını bildirir.","neighbor_ref":"root_001317/B007","relation_type":"same_field","shared_zone":"İki dal da tam olarak iki öğenin birlikte düşünülmesi alanındadır."},{"boundary_match":"field_only","distinction":"Odak genel ve sayısal bir sınıftır; komşu ise su ile yiyecek veya iki zaman dilimi gibi önceden belirlenmiş ikililerin özel adlandırılmasıdır.","focus_only":"Odak dal, herhangi bir şeyin çift veya çift sayıda olmasını genel biçimde bildirir.","gloss":"genel çiftlik ile adlandırılmış ikililer","neighbor_only":"Komşu dal, kültürel kullanımda birlikte anılan belirli ikililere verilen ortak bir adı kapsar.","neighbor_ref":"root_000168/B008","relation_type":"same_field","shared_zone":"Her iki dal iki öğenin tek bir ikili olarak anılması alanına girer."}],"source_phrase_ar":"الزكا الزوج وهو الشفع (maqayis)؛ وزكا الشفع يقال خسا أو زكا (sihah)؛ العرب تقول للفرد خسا وللزوجين اثنين زكا؛ هو يخسي ويزكي إذا قبض على شيء في كفه وقال أزكا أم خسا (tahdhib)","source_summary":"Kaynakların ortak anlatımı çift veya iki öğeli olmayı tek olanın karşısına koyar; tek-çift sözü ve avuçtaki şey üzerine yapılan tahmin bu karşıtlığın özel kullanımlarıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه زكا بمعنى الزوج أو الشفع، في مقابلة خسا للفرد، وألفاظ اللعب أو القبض على الشيء في الكف: أزكا أم خسا.","what_is_not_ar":"لا يدخل فيه النمو والطهارة والزكاة المالية."},"support_links":[]},{"boundary":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001457/B001","candidate_links":[{"candidate_id":"cand_44bb0198bb7ffca9c530","lane":"micro"},{"candidate_id":"cand_8cc17107b0431dc9cad9","lane":"micro"},{"candidate_id":"cand_107e37a196c78dc2dda9","lane":"micro"},{"candidate_id":"cand_06c6ae616da4d61b813c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:18:3:1","qac_word_ref":"92:18:3","surface_ar":"مَالَ"}],"gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."}},{"facet_id":"F004","role":"core","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."}},{"facet_id":"F006","role":"associated_use","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın sahip olunan varlık, onu edinme, varlıklı duruma gelme ve başkasını varlık sahibi kılma çekirdeklerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal yalnızca para ya da birikmiş değer değildir; varlığın kendisini, edinilmesini, artmasını, varlıklı duruma geçişi ve başkasına varlık kazandırmayı ayırarak kapsar.","branch_image_ar":"اتخاذ المال وكثرته","concept_gloss":"varlık; edinme, çoğalma ve başkasına kazandırma","contextual_glosses":[{"applicability":"Bir kişinin elindeki değer taşıyan şeylerin bütünü ya da bunların çoğulu ad olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Edinme, çoğalma, varlıklı duruma gelme ve başkasına varlık kazandırma süreçlerini karşılamaz.","preserves":"Dalın kişiye ait değerli varlıklar bildiren ad çekirdeğini korur."},"facet_ids":["F001"],"text":"sahip olunan değerli varlıklar","usage_role":"general"},{"applicability":"Kişinin değerli bir şeyi kendisi için edinip sahipliğinde tutması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlık adını, varlığın kendiliğinden artmasını ve başkasına varlık kazandırmayı dışarıda bırakır.","preserves":"Kendisi için varlık edinme ve onu kalıcı sahiplik konusu yapma sürecini korur."},"facet_ids":["F003"],"text":"kendine kalıcı varlık edinmek","usage_role":"contextual"},{"applicability":"Bir kişinin sahip olduklarının artması ya da kişinin varlık sahibi hale gelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın ad çekirdeğini, bilinçli edinmeyi ve başkasını varlık sahibi kılmayı karşılamaz.","preserves":"Varlık artışını ve kişinin varlıklı duruma geçişini açıkça korur."},"facet_ids":["F004"],"text":"varlığı çoğalmak veya varlıklı duruma gelmek","usage_role":"contextual"},{"applicability":"Bir kişinin başkasına değerli varlık vererek onun sahiplik durumunu değiştirmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Varlığın kendisini, kişinin kendisi için edinmesini ve kendi varlığının artmasını karşılamaz.","preserves":"Başkasına varlık kazandıran ettirgen katılımcı değişimini korur."},"facet_ids":["F005"],"text":"birini varlık sahibi yapmak","usage_role":"contextual"}],"definition":"Kişinin sahip olduğu değerli varlıkların bütünü ile bunları edinme, çoğaltma ya da bunlara sahip duruma gelme alanıdır. Ayrıca başkasını varlık sahibi kılmayı kapsar; göçebe topluluklara özgü kullanımda sahip olunan varlık özellikle hayvan sürüleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sahip olduğu ve değer taşıyan varlıkların bütünü bu dalın ad çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Göçebe toplulukların varlığına ilişkin belirli kullanımda bu varlık, hayvan sürüleriyle somutlaşır."},{"facet_id":"F003","role":"core","statement":"Kişinin kendisi için değerli varlık edinmesi ve onu kalıcı sahiplik konusu yapması eylem çekirdeğidir."},{"facet_id":"F004","role":"core","statement":"Kişinin varlığının çoğalması ya da onun varlık sahibi bir duruma geçmesi ayrı bir süreç görünümüdür."},{"facet_id":"F005","role":"extension","statement":"Bir başkasına değerli varlık vererek onu varlık sahibi duruma getirmek, çekirdeğin ettirgen uzantısıdır."},{"facet_id":"F006","role":"associated_use","statement":"Bir kimsenin varlığının çokluğuna şaşma bildiren söyleyiş, artış ve bolluk görünümüne bağlı bir kullanımdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Dalın bütün sahip olunan varlıkları kapsayan alanını yalnızca ödeme aracına indirger.","fit":"narrowing","loses":"Nakit dışındaki varlıkları, hayvan sürüsü özelleşmesini ve edinme, artma, varlıklılaşma ile kazandırma süreçlerini siler.","preserves":"Değer taşıyan ve sahip olunabilen bir şey düşüncesinin yalnızca nakit yönünü korur."},"text":"para"}],"identity_rationale":"Kaynak ifadesi, sahip olunan değerli varlıkları ve bunların çoğulunu; kişinin kendisi için varlık edinmesini, varlığının çoğalmasını ya da varlıklı duruma gelmesini ve başkasını varlık sahibi kılmasını birlikte aktarır. Göçebe toplulukların varlığının hayvan sürüleriyle somutlaşması bu çekirdeğin bağlama bağlı bir özelleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kişinin sahip olduğu değerli varlıklar"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"göçebe toplulukların başlıca varlığı sayılan hayvan sürüleri"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"varlık sahibi veya çok varlıklı kimse"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendine kalıcı varlık edinmek"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"varlığı çoğalmak veya varlık sahibi duruma gelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini varlık sahibi yapmak veya ona değerli varlık vermek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"mal sözcüğünün küçültme biçimi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ne çok varlığı var!"}],"lexicalization_note":"Tanım, genel varlık ve varlık edinme çekirdeğini ayrı tutar; göçebe toplulukların hayvan sürülerini varlık sayan kullanımını yalnızca belirli bir söz öbeğine bağlı özelleşme olarak sınırlar.","neighbor_coverage_note":"Sekiz adayın tümü karşılaştırıldı. Edinme ve varlık artışıyla doğrudan sınır paylaşan üç aday yayımlandı; para yönetimi, belirli varlık türleri, geçim ve sürü adlandırmalarıyla yalnızca uzak alan ortaklığı kuran ötekiler dal sınırını keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın edinme görünümü komşuya yaklaşır, fakat odak daha geniş bir sahip olunan varlık ve varlıklılaşma ailesidir. Komşu ise edinimin amacı ve saklama biçimiyle sınırlı, daha özel bir sahiplik türünü belirtir.","focus_only":"Odak dal, sahip olunan varlığın adını, varlığın artmasını, varlıklı duruma gelmeyi ve başkasını varlık sahibi kılmayı da kapsar.","gloss":"kendisi için edinilen ve saklanan varlık","neighbor_only":"Komşu dal, kişinin kendisi için satış ve ticaret amacı dışında edindiği, gereksinim sonrasında sakladığı ya da temel dayanak yaptığı varlığa özgü koşullar taşır.","neighbor_ref":"root_001265/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin kendisi için değerli varlık edinmesi ve bunu sahipliğinde tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşunun çekirdeği belirli bir mülk ve taşınmaz türüne yönelirken odak dal varlığın türünü sınırlandırmaz; ayrıca artış, varlıklı duruma geçiş ve ettirgen kazandırma anlamlarını içerir.","focus_only":"Odak dal taşınır ya da taşınmaz ayrımı yapmadan varlığı, varlık artışını ve başkasına varlık kazandırmayı kapsar.","gloss":"taşınmaz edinme ve elde tutma","neighbor_only":"Komşu dal özellikle taşınmazı, gelir getiren yeri ve bunları edinip kalıcı sahiplik konusu yapmayı öne çıkarır.","neighbor_ref":"root_001034/B004","relation_type":"near_synonym","shared_zone":"İki dal, değer taşıyan bir şeyi edinme ve kalıcı sahiplik altında bulundurma düşüncesinde birleşir."},{"boundary_match":"partial","distinction":"Örtüşme varlık artışıyla sınırlıdır. Odak dal sahiplik ve edinme ailesini kurarken komşu, büyüyen varlık ile onun bakımı ve artışına ilişkin değerlendirmeleri ayrı bir çekirdek yapar.","focus_only":"Odak dal varlığın genel adını, edinilmesini ve başkasının varlık sahibi yapılmasını da içerir.","gloss":"artan varlık ve onu iyi yönetme","neighbor_only":"Komşu dal büyüyen ya da çok olan varlığı, onun iyi yönetilmesini ve artması yönündeki iyi dileği özellikle öne çıkarır.","neighbor_ref":"root_000205/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sahip olunan varlığın çokluğu veya artışı belirgin bir ortak alandır."}],"source_phrase_ar":"تمول الرجل اتخذ مالا؛ مال يمال كثر ماله (maqayis)؛ المال معروف وجمعه أموال؛ كانت أموال العرب أنعامهم؛ رجل مال أي ذو مال والفعل تمول (ayn)؛ مال الرجل يمول ويمال إذا صار ذا مال؛ تمول مثله؛ موله غيره (sihah)؛ مال أهل البادية النعم؛ تمول فلان مالا إذا اتخذ قنية من المال؛ ما أموله أي ما أكثر ماله (tahdhib)","source_summary":"Kaynakların toplu anlatımı, sahip olunan değerli varlıkları ve bunların çoğulunu temel alır; varlık edinme, varlığın çoğalması, varlıklı duruma gelme ve başkasını varlık sahibi kılma süreçlerini bu temel çevresinde birleştirir. Hayvan sürüleri göçebe topluluklara özgü somutlaşma, çokluk karşısındaki şaşma söyleyişi ise bağlı bir kullanım olarak aktarılır. Mal adının küçültme biçimi de ayrıca kaydedilir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه المال والأموال واتخاذ المال قنية وكثرة المال وصيرورة الرجل ذا مال وتمويل غيره ونعم أهل البادية","what_is_not_ar":"ليس للمولة العنكبوت ولا للميل عن الوسط ولا لميل الحائط"},"support_links":["sup_1d73dfb73c1b46debef4","sup_2a7d73f23e85348cfd4f","sup_8038e12b74ed5c66816f","sup_fda4e2db2bba27fe0669"]},{"boundary":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_kind":"unresolved","branch_ref":"root_001457/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:18:3:1","qac_word_ref":"92:18:3","surface_ar":"مَالَ"}],"gloss":"örümcek için tartışmalı bir ad","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}}],"root_ar":"م و ل","root_id":"root_001457","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcüğün örümceğe gönderimi aktarılırken bu adlandırmanın güvenilirliğine ilişkin açık kuşkunun da korunması gereken her durumda uygundur.","boundary_detail":"Dal, örümceğin özelliklerini tanımlamaz; yalnızca örümcek için aktarılan ve güvenilirliği açıkça tartışılan bir adlandırmayı temsil eder.","branch_image_ar":"المُولة العنكبوت","concept_gloss":"örümcek için tartışmalı bir ad","contextual_glosses":[{"applicability":"Tartışmalı hayvan adının bir metinde doğrudan canlıya gönderim yaptığı bağlamda akıcı karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu adlandırmanın güvenilirliği ve yerleşikliği üzerindeki açık kaynak kuşkusunu görünmez kılar.","preserves":"Adlandırmanın gönderimde bulunduğu hayvanı doğru biçimde korur."},"facet_ids":["F001"],"text":"örümcek","usage_role":"contextual"}],"definition":"Örümceğe verilen bir ad olarak aktarılır; ancak bu adlandırmanın güvenilirliği kaynak anlatımının kendi içinde açıkça tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sözcük, bazı sözlük aktarımlarında örümceği gösteren bir hayvan adı olarak verilir."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın doğruluğu ve güvenilir aktarımı açıkça sorgulandığı için bu gönderim kesin kabul edilemez."}],"identity_rationale":"Kaynak ifadesi sözcüğü örümceğe verilen bir ad olarak aktarır, fakat aynı ifadenin içinde bu aktarımın kuşkuyla karşılandığını ve güvenilir bir aktarıcıdan işitilmediğini de açıkça bildirir. Bu nedenle hayvanla kurulan bağ korunabilir, ancak yerleşik ve tartışmasız bir ad gibi sunulamaz.","lexicalization_note":"Kanıt, bu tartışmalı adlandırmanın bağımsız ve yerleşik bir yalın sözlük birimi olup olmadığını mekanik olarak çözmez; tanım bu yüzden yalın kullanım varsaymaz.","neighbor_coverage_note":"Dokuz adayın tümü değerlendirildi. Aynı canlıya yönelen iki adlandırma gerçek bir sınır karşılaştırması sağladı; öteki hayvan adları yalnızca geniş canlılar alanını paylaştı, varlık dalı ise ortak köke rağmen anlamsal örtüşme göstermedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Gönderim ortak olsa da odak dalın sözlüksel kimliği kuşkulu bir ad aktarımına bağlıdır. Komşu dal ise canlının doğrudan adını ve onu tanıtan özellikleri kapsadığı için iki adın kullanım sınırları tam olarak eşleşmez.","focus_only":"Odak dal, aynı canlıya yönelen fakat güvenilirliği açıkça tartışılan özel bir ad aktarımıdır.","gloss":"ağ ören örümcek","neighbor_only":"Komşu dal canlının olağan adını, ağ örme niteliğini, ad çeşitlerini ve dil bilgisel biçimlerini kapsar.","neighbor_ref":"root_001054/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın hayvansal gönderimi aynı canlıya, yani örümceğe yönelir."},{"boundary_match":"partial","distinction":"Odak dal yalnızca kuşkulu hayvan adı aktarımıyla sınırlıdır; komşu dalın kendi ayrı adı ve yuvayı gösteren bağlı kullanımı vardır. Bu ek kapsam ve odaktaki güvenilirlik çekincesi tam eşdeğerliği engeller.","focus_only":"Odak dalın örümcek adı sayılması kaynak anlatımında açık kuşku ve güven sorunu taşır.","gloss":"örümcek ve yuvası için özel ad","neighbor_only":"Komşu dal başka bir örümcek adının yanı sıra o örümceğin yuvasını gösteren bağlı bir söz öbeğini de kapsar.","neighbor_ref":"root_001326/B008","relation_type":"near_synonym","shared_zone":"İki dal da örümceğe verilen alışılmadık bir adlandırma üzerinden aynı canlıya gönderimde bulunur."}],"source_phrase_ar":"إن المولة العنكبوت وفيه نظر (maqayis)؛ المولة اسم العنكبوت (ayn)؛ زعم قوم أن المول العنكبوت الواحدة مولة ولم أسمعه عن ثقة (sihah)؛ هي العنكبوت والمولة (tahdhib)","source_summary":"Toplu kaynak kaydı sözcüğü örümceğin adı olarak aktarır, fakat aynı kayıtta bu eşleştirmenin kuşkulu olduğu ve güvenilir bir kaynaktan işitilmediği yönünde açık çekinceler bulunur. Bu yüzden hayvana gönderim ile aktarımın belirsizliği birlikte korunmalıdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه إطلاق المولة أو المول على العنكبوت إذا ثبتت النسبة","what_is_not_ar":"ليس للمال والأموال ولا لاتخاذ القنية ولا لكثرة المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:18:1"],"branch_refs":[],"candidate_id":"cand_753b33a33c4caabe09f1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:1:asyndetic-boundary-shift","source_type":"word_analysis","support_ids":["sup_4847093d9ba9a99d6b2d","sup_4aaa2b7fd25831a0845b"],"title":"boundary moves straight into behavior","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:1","qac_refs":["92:18:1:1"],"status":"accepted"}},{"anchor_refs":["92:18:1"],"branch_refs":[],"candidate_id":"cand_fd635373952e83cc2c62","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:1:expanded-action-profile","source_type":"word_analysis","support_ids":["sup_4847093d9ba9a99d6b2d","sup_4baba0224427a7f4f8fd"],"title":"relative form opens an action profile","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:1","qac_refs":["92:18:1:1"],"status":"accepted"}},{"anchor_refs":["92:18:1"],"branch_refs":[],"candidate_id":"cand_e2cf5865128451bb29be","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:1:matched-moral-profiles","source_type":"word_analysis","support_ids":["sup_0cb386096ecfc06927cf","sup_4847093d9ba9a99d6b2d"],"title":"same relative opening mirrors the negative type","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:1","qac_refs":["92:18:1:1"],"status":"accepted"}},{"anchor_refs":["92:18:1"],"branch_refs":[],"candidate_id":"cand_1b6ad182d9d171450f68","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:1:prior-title-definition","source_type":"word_analysis","support_ids":["sup_0b8734b096e92bf2cd2d","sup_4847093d9ba9a99d6b2d"],"title":"relative pronoun defines the prior title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:1","qac_refs":["92:18:1:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_b2c825d99def43a7d9ab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:boundary-agency","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_269febb085d14dd0eec2"],"title":"rescued figure becomes active giver","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_a18f460af7bfc2618769","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:caused-transfer","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_f405e60c965a1cfa9e43"],"title":"Form IV makes wealth reach elsewhere","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_39fc4c20d792bd1667af","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:characterizing-imperfect","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_f02533d80549ac47a24f"],"title":"imperfect indicative marks a defining habit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_76d05016e4a632be4db7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:clipped-sound-onset","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_c47206678fffcbc2d8f0"],"title":"clipped verb sound precedes flowing object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_c3538a41b2492aa54d16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:giving-purification-collocation","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_fb4d24a5323a3241a324"],"title":"giving formula becomes self-purification sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_b9d1fdb94d4c062470ab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:18:2:intertextual-giving-frame","source_type":"word_analysis","support_ids":["sup_024aedccc5ea15e2fc9e","sup_3c9667159ba514e75c12"],"title":"giving sits in a wider righteousness frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:2","qac_refs":["92:18:2:1"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_d9fde3a5794c33ae4ba0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:boundary-material-practice","source_type":"word_analysis","support_ids":["sup_0284176e941bcccb85c3","sup_41261d6c2c505358bba8"],"title":"promise becomes material practice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_1f1d685bfef510d4cf8e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:hinge-between-transfer-and-purification","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_47a37bd9f62e61694e50"],"title":"wealth mediates outward gift and inward change","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_186959ec73d457190c7c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:possessed-direct-object","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_ee30cb3d76a2a9bdbf5b"],"title":"owned wealth is the object given","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_3c3ab940736d830fc30c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:possession-to-release-sound","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_5683e6d5d31098f048d9"],"title":"suffix sound moves toward release","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_e4c51e0987a182985629","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:property-with-inclination-pressure","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_4e3ea3a7d73fa0673177"],"title":"wealth sense carries qualified desire pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_3bd5cec272d0614af321","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:retained-versus-surrendered-wealth","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_92a8a887ebca3aef551d"],"title":"same-surah wealth echo reverses function","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_922838772927dd2a3732","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:singular-total-value","source_type":"word_analysis","support_ids":["sup_41261d6c2c505358bba8","sup_82f594eadf4f6d902193"],"title":"singular possession gathers the cost","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:3","qac_refs":["92:18:3:1","92:18:3:2"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_055bbdf3f8c4c30e5cb7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:final-interpretive-landing","source_type":"word_analysis","support_ids":["sup_2ca8f3918a24978a1e35","sup_80fd47f8b35f1a368d4f"],"title":"final verb explains the gift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_1e0071bf51bd0789f10b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:heavy-final-sound","source_type":"word_analysis","support_ids":["sup_80fd47f8b35f1a368d4f","sup_c5f6ad7a321e63e8737c"],"title":"gemination gives the ending weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_71a0edd29b0f91a73435","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:imperfect-state-purpose","source_type":"word_analysis","support_ids":["sup_80fd47f8b35f1a368d4f","sup_e741d835a68dc81e28f1"],"title":"finite imperfect leaves state and purpose live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_3d88bcbccd3cb00ded81","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:positive-path-bridge","source_type":"word_analysis","support_ids":["sup_314e6032f3dde5ff6df8","sup_80fd47f8b35f1a368d4f"],"title":"taqwa opens into self-cultivation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_168d7e893fb338acb9b4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:purity-growth-fusion","source_type":"word_analysis","support_ids":["sup_80fd47f8b35f1a368d4f","sup_d318635316f8ba450a6e"],"title":"purification and growth converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_ce1c08a3eb80739ca024","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:same-agent-reflexive","source_type":"word_analysis","support_ids":["sup_80fd47f8b35f1a368d4f","sup_8c4c41b9160816992a6f"],"title":"giver is also self-purifier","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_a7880fe4b7b9c9779feb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:self-purification-parallels","source_type":"word_analysis","support_ids":["sup_550ba46b7014b89e1ca3","sup_80fd47f8b35f1a368d4f"],"title":"final verb joins salvation purification scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_0aebab881bc9fac91b3b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:verbal-zakah-echo-transformed","source_type":"word_analysis","support_ids":["sup_80fd47f8b35f1a368d4f","sup_ffc1f1a6b18699f70bb5"],"title":"zakah field becomes a self-process","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:18:4","qac_refs":["92:18:4:1"],"status":"accepted"}},{"anchor_refs":["92:18:2"],"branch_refs":[],"candidate_id":"cand_04803758905514745292","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000009"],"scope":"focus_ayah","source_local_id":"92:18:2:1","source_type":"qac_morpheme","support_ids":["sup_bcb14512331aced96f29"],"title":"QAC root occurrence: ء ت ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:18:3"],"branch_refs":[],"candidate_id":"cand_f9b20f2453642e3610f4","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001457"],"scope":"focus_ayah","source_local_id":"92:18:3:1","source_type":"qac_morpheme","support_ids":["sup_fe6250b53860b0ecf691"],"title":"QAC root occurrence: م و ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:18:4"],"branch_refs":[],"candidate_id":"cand_bae2942a2c4ae5b73e24","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000637"],"scope":"focus_ayah","source_local_id":"92:18:4:1","source_type":"qac_morpheme","support_ids":["sup_6ab021729f46c8c6fef2"],"title":"QAC root occurrence: ز ك و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:18","branch_refs":["root_000009/B002","root_000637/B002","root_001457/B001"],"candidate_id":"cand_44bb0198bb7ffca9c530","commentary_obligation":"review","hft_ref":"hft_7cffd6225bcce3a944b3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b01_transfer_as_reflexive_purification","source_type":"hft","support_ids":["sup_fda4e2db2bba27fe0669"],"title":"b01_transfer_as_reflexive_purification","trust":"legacy_unbound"},{"anchor_refs":["92:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:18","branch_refs":["root_000009/B007","root_000637/B001","root_001457/B001"],"candidate_id":"cand_8cc17107b0431dc9cad9","commentary_obligation":"review","hft_ref":"hft_2a80cb2124dca05c218d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b02_release_as_increase","source_type":"hft","support_ids":["sup_2a7d73f23e85348cfd4f"],"title":"b02_release_as_increase","trust":"legacy_unbound"},{"anchor_refs":["92:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:18","branch_refs":["root_000009/B004","root_000637/B001","root_001457/B001"],"candidate_id":"cand_107e37a196c78dc2dda9","commentary_obligation":"review","hft_ref":"hft_31533ed8a1980544d761","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b03_wealth_as_routed_flow","source_type":"hft","support_ids":["sup_1d73dfb73c1b46debef4"],"title":"b03_wealth_as_routed_flow","trust":"legacy_unbound"},{"anchor_refs":["92:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:18","branch_refs":["root_000009/B003","root_000637/B004","root_001457/B001"],"candidate_id":"cand_06c6ae616da4d61b813c","commentary_obligation":"review","hft_ref":"hft_31cdfd9a2493392b98f0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b04_proper_access_and_fittingness","source_type":"hft","support_ids":["sup_8038e12b74ed5c66816f"],"title":"b04_proper_access_and_fittingness","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"92:18:1:1","qac_word_ref":"92:18:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","root_ar":"ء ت ي","surface_ar":"يُؤْتِى"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:18:3:1","qac_word_ref":"92:18:3","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:18:3:2","qac_word_ref":"92:18:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","root_ar":"ز ك و","surface_ar":"يَتَزَكَّىٰ"}],"word_analysis_qac_refs":[["92:18:1:1"],["92:18:2:1"],["92:18:3:1","92:18:3:2"],["92:18:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:18:1","92:18:2","92:18:3","92:18:4"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"92:18:1:1","qac_word_ref":"92:18:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"آتَى","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:2:1","qac_word_ref":"92:18:2","root_ar":"ء ت ي","surface_ar":"يُؤْتِى"},{"lemma_ar":"مَال","morph_features":"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"92:18:3:1","qac_word_ref":"92:18:3","root_ar":"م و ل","surface_ar":"مَالَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"92:18:3:2","qac_word_ref":"92:18:3","root_ar":"","surface_ar":"هُۥ"},{"lemma_ar":"تَزَكَّىٰ","morph_features":"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:18:4:1","qac_word_ref":"92:18:4","root_ar":"ز ك و","surface_ar":"يَتَزَكَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:18:1:1"],["92:18:2:1"],["92:18:3:1","92:18:3:2"],["92:18:4:1"]],"word_analysis_refs":["92:18:1","92:18:2","92:18:3","92:18:4"],"word_rows":[{"analysis_record_ref":"92:18:1","analytic_gloss_range_en":"masculine singular relative pronoun that resumes the prior superlative and opens its defining action clause","analytic_root_gloss_range_en":null,"qac_refs":["92:18:1:1"],"root":{},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"92:18:2","analytic_gloss_range_en":"Form IV imperfect giving as caused arrival or bestowal, with the recipient unexpressed and the owned wealth as explicit object","analytic_root_gloss_range_en":"coming, bringing, and causing to reach; the local Form IV selects bestowal or causing wealth to arrive, not simple coming","qac_refs":["92:18:2:1"],"root":{"arabic":"أ ت ي","transliteration":"ʾ-t-y"},"surface":{"arabic":"يُؤْتِى","transliteration":"yuʾtī"}},{"analysis_record_ref":"92:18:3","analytic_gloss_range_en":"his owned wealth or possessed value, functioning as the explicit object surrendered in the giving clause","analytic_root_gloss_range_en":"wealth, property, acquired possession, and valued resources; local syntax selects transferable possessed wealth, with inclination-language only as a qualified derivational pressure","qac_refs":["92:18:3:1","92:18:3:2"],"root":{"arabic":"م و ل","transliteration":"m-w-l"},"surface":{"arabic":"مَالَهُۥ","transliteration":"mālahū"}},{"analysis_record_ref":"92:18:4","analytic_gloss_range_en":"self-purifies, cultivates himself, or grows through purification; locally a finite Form V verb describing state or purpose with the same subject as the giver","analytic_root_gloss_range_en":"growth, increase, purity, rectitude, and the alms-purification field; local Form V selects self-directed purification/growth, not the noun zakah or unrelated branches such as fittingness or evenness","qac_refs":["92:18:4:1"],"root":{"arabic":"ز ك و","transliteration":"z-k-w"},"surface":{"arabic":"يَتَزَكَّىٰ","transliteration":"yatazakkā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["92:18"],"branch_refs":["root_000009/B002","root_000637/B002","root_001457/B001"],"candidate_id":"cand_44bb0198bb7ffca9c530","evidence_scope":"focus_ayah","hft_ref":"hft_7cffd6225bcce3a944b3","item_id":"b01_transfer_as_reflexive_purification","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b01_transfer_as_reflexive_purification","support_id":"sup_fda4e2db2bba27fe0669"},{"anchor_refs":["92:18"],"branch_refs":["root_000009/B007","root_000637/B001","root_001457/B001"],"candidate_id":"cand_8cc17107b0431dc9cad9","evidence_scope":"focus_ayah","hft_ref":"hft_2a80cb2124dca05c218d","item_id":"b02_release_as_increase","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b02_release_as_increase","support_id":"sup_2a7d73f23e85348cfd4f"},{"anchor_refs":["92:18"],"branch_refs":["root_000009/B004","root_000637/B001","root_001457/B001"],"candidate_id":"cand_107e37a196c78dc2dda9","evidence_scope":"focus_ayah","hft_ref":"hft_31533ed8a1980544d761","item_id":"b03_wealth_as_routed_flow","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b03_wealth_as_routed_flow","support_id":"sup_1d73dfb73c1b46debef4"},{"anchor_refs":["92:18"],"branch_refs":["root_000009/B003","root_000637/B004","root_001457/B001"],"candidate_id":"cand_06c6ae616da4d61b813c","evidence_scope":"focus_ayah","hft_ref":"hft_31cdfd9a2493392b98f0","item_id":"b04_proper_access_and_fittingness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b04_proper_access_and_fittingness","support_id":"sup_8038e12b74ed5c66816f"}],"diagnostics":[],"lane_counts":{"global":16,"macro":8,"micro":4},"packet_summary":{"ayah_count":21,"focus_ref":"92:18","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:18","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"92:18","lane":"micro","linguistic_source_ref":"92:18","surface_ref":"92:18","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:18","target_tokens":[["O",["92:18:1"]],["arınarak",["92:18:4"]],["malını",["92:18:3"]],["verir",["92:18:2"]]],"text":"O, arınarak malını verir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":12,"ayah_to":21,"id":"s092-p02-012-021","label":"Guidance, fire, and generous salvation","number":2,"refs":["92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2","source_type":"word_analysis","support_id":"sup_024aedccc5ea15e2fc9e","text":"{\"gloss_range\":\"Form IV imperfect giving as caused arrival or bestowal, with the recipient unexpressed and the owned wealth as explicit object\",\"prose\":\"{{ar:يُؤْتِى}} ({{tr:yuʾtī}}) begins the behavioral content of the relative clause with an active, imperfect Form IV verb. Its form does more than say that the figure is generous in the abstract: from the arrival root, it casts him as causing his own wealth to reach elsewhere. The explicit object {{ar:مَالَهُۥ}} ({{tr:mālahū}}) keeps the transfer material and costly, while the unnamed recipient leaves attention on the giver, the surrendered wealth, and the self-purifying aim or state. Its imperfect indicative shape makes the act a characterizing habit, not a command or a single past donation. The verb also stands in the familiar Quranic field where giving language meets purification or alms, but here the formula is transformed: the clause moves from {{ar:يُؤْتِى}} ({{tr:yuʾtī}}) to the finite self-purification verb {{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}}), so outward transfer and inward transformation answer each other. That directional giving refines the positive path opened by giving in 92:5 and belongs with righteousness scenes where wealth-giving is named (2:177; 76:8-9), while the next ayah denies any payback motive (92:19). Even in sound, the clipped hamza onset of {{ar:يُؤْتِى}} ({{tr:yuʾtī}}) separates the transfer act before the smoother possessed-wealth phrase.\",\"root_display\":\"{{ar:أ ت ي}} ({{tr:ʾ-t-y}})\",\"root_gloss_range\":\"coming, bringing, and causing to reach; the local Form IV selects bestowal or causing wealth to arrive, not simple coming\",\"surface_display\":\"{{ar:يُؤْتِى}} ({{tr:yuʾtī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:boundary-material-practice","source_type":"word_analysis","support_id":"sup_0284176e941bcccb85c3","text":"{\"blocking_evidence\":null,\"headline\":\"promise becomes material practice\",\"reader_payoff\":\"The reader sees future rescue grounded in a concrete practice: wealth is moved away from the self.\",\"reason\":\"The cross-boundary relation is coherent because the same referent moves from promised distancing from fire in 92:17 to voluntarily distancing wealth from himself in 92:18.\",\"representative_source_ids\":[\"QB-3b0a2f7c\",\"QB-b0377843\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:1:prior-title-definition","source_type":"word_analysis","support_id":"sup_0b8734b096e92bf2cd2d","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun defines the prior title\",\"reader_payoff\":\"The reader notices that 92:18 is the behavioral definition of the saved al-atqā from 92:17, not a self-contained maxim.\",\"reason\":\"The QAC and attachment evidence identify the word as a masculine singular relative pronoun whose antecedent is the prior masculine singular superlative, and the local clause supplies its verbal content.\",\"representative_source_ids\":[\"QG-90eb43f2\",\"MG-16a83a95\",\"QB-9870361f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:1:matched-moral-profiles","source_type":"word_analysis","support_id":"sup_0cb386096ecfc06927cf","text":"{\"blocking_evidence\":null,\"headline\":\"same relative opening mirrors the negative type\",\"reader_payoff\":\"The reader notices that the positive figure is defined with the same relative-clause mechanism used for the opposite figure in 92:16.\",\"reason\":\"The surah-internal recurrence is locally coherent: 92:16 and 92:18 both begin their moral profile with the same relative pronoun, while their following actions diverge.\",\"representative_source_ids\":[\"QI-aa182594\",\"QE-c01afd52\",\"QY-1f9bd48f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:boundary-agency","source_type":"word_analysis","support_id":"sup_269febb085d14dd0eec2","text":"{\"blocking_evidence\":null,\"headline\":\"rescued figure becomes active giver\",\"reader_payoff\":\"The reader sees the person kept from fire in 92:17 become the agent of social-material action in 92:18, before 92:19 denies repayment as the motive.\",\"reason\":\"The same cross-ayah referent is subject of the active verb, and the concrete follow-on reference to 92:19 supports the structural pairing without changing the local syntax.\",\"representative_source_ids\":[\"QB-2ace65a4\",\"QB-6727123d\",\"MT-2b43774a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:final-interpretive-landing","source_type":"word_analysis","support_id":"sup_2ca8f3918a24978a1e35","text":"{\"blocking_evidence\":null,\"headline\":\"final verb explains the gift\",\"reader_payoff\":\"The reader notices that the final word gives the preceding wealth-transfer its moral and inward meaning.\",\"reason\":\"The verb follows the giving-and-wealth phrase as the final isolated beat, and attachment evidence connects it as state or aim rather than an unrelated action.\",\"representative_source_ids\":[\"QT-a21e19ac\",\"QE-e03aee96\",\"QY-17dc2ead\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:positive-path-bridge","source_type":"word_analysis","support_id":"sup_314e6032f3dde5ff6df8","text":"{\"blocking_evidence\":null,\"headline\":\"taqwa opens into self-cultivation\",\"reader_payoff\":\"The reader sees the positive path of giving, guarding, and self-purification joined across 92:5, 92:17, and 92:18.\",\"reason\":\"The surah links giving and guarding in 92:5, names the most guarded figure in 92:17, and defines him with self-purification in 92:18.\",\"representative_source_ids\":[\"QI-29bd536c\",\"MI-3e0d6239\",\"QB-dcea9465\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:intertextual-giving-frame","source_type":"word_analysis","support_id":"sup_3c9667159ba514e75c12","text":"{\"blocking_evidence\":null,\"headline\":\"giving sits in a wider righteousness frame\",\"reader_payoff\":\"The reader can compare this directional wealth-giving with the earlier positive giving in 92:5 and with righteousness scenes where wealth-giving is named (2:177; 76:8-9).\",\"reason\":\"The references are concrete and do not control the local parse; they supply comparison for the positive path and for the righteous-giving register.\",\"representative_source_ids\":[\"QI-ca283687\",\"MI-7bf3ec64\",\"MI-c656fd13\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3","source_type":"word_analysis","support_id":"sup_41261d6c2c505358bba8","text":"{\"gloss_range\":\"his owned wealth or possessed value, functioning as the explicit object surrendered in the giving clause\",\"prose\":\"{{ar:مَالَهُۥ}} ({{tr:mālahū}}) is the explicit object of {{ar:يُؤْتِى}} ({{tr:yuʾtī}}): the clause names the thing transferred, not merely the virtue of giving. The attached possessive suffix makes the cost personal, binding the wealth to the same figure resumed by {{ar:ٱلَّذِى}} ({{tr:alladhī}}) before the verb hands it away. Its singular form gathers the owned value as his wealth rather than a detached list of assets or communal funds. Lexically, the local root alignment and V4 evidence keep the main sense in wealth and property, while the reported inclination derivation can still color the act as surrendering what the self leans toward. Structurally the word sits between transfer and purification, so the possessed object becomes the hinge: what is attached to him is moved outward and becomes the threshold for {{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}}). The sound follows that movement too: the possessive hū keeps the wealth close before the clause opens into the final ā of {{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}}). The surah-internal echo sharpens the hinge, because wealth that cannot avail when retained in 92:11 becomes defining when surrendered in 92:18; the person kept away from fire is marked by moving wealth away from himself.\",\"root_display\":\"{{ar:م و ل}} ({{tr:m-w-l}})\",\"root_gloss_range\":\"wealth, property, acquired possession, and valued resources; local syntax selects transferable possessed wealth, with inclination-language only as a qualified derivational pressure\",\"surface_display\":\"{{ar:مَالَهُۥ}} ({{tr:mālahū}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:hinge-between-transfer-and-purification","source_type":"word_analysis","support_id":"sup_47a37bd9f62e61694e50","text":"{\"blocking_evidence\":null,\"headline\":\"wealth mediates outward gift and inward change\",\"reader_payoff\":\"The reader notices the word's middle position: the wealth leaves through giving and immediately opens into self-purification.\",\"reason\":\"The object stands between the governing giving verb and the following circumstantial or purposive self-purification verb.\",\"representative_source_ids\":[\"QT-47ca46ba\",\"MT-af4aec9f\",\"QE-9956621f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:1","source_type":"word_analysis","support_id":"sup_4847093d9ba9a99d6b2d","text":"{\"gloss_range\":\"masculine singular relative pronoun that resumes the prior superlative and opens its defining action clause\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) makes 92:18 depend grammatically on the prior title al-atqā in 92:17. The word is definite, masculine, and singular, so it does not begin a loose maxim about anyone at all; it resumes the already named figure and turns the following giving and self-purification into that figure's definition. Because it opens with no coordinating particle, the ayah boundary falls inside a live grammatical dependency: the saved person of 92:17 is immediately unpacked as an acting person in 92:18. The same relative device also answers the negative profile introduced with alladhī in 92:16, so the surah defines both opposite moral types by what they do, not by labels alone.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:1:asyndetic-boundary-shift","source_type":"word_analysis","support_id":"sup_4aaa2b7fd25831a0845b","text":"{\"blocking_evidence\":null,\"headline\":\"boundary moves straight into behavior\",\"reader_payoff\":\"The reader feels the ayah boundary as immediate continuation from promised rescue into the conduct that marks the rescued person.\",\"reason\":\"The ayah begins directly with the relative pronoun rather than a coordinator, and attachment evidence keeps the clause dependent on the preceding antecedent.\",\"representative_source_ids\":[\"QT-16ba4ffa\",\"QB-e0aefb7e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:1:expanded-action-profile","source_type":"word_analysis","support_id":"sup_4baba0224427a7f4f8fd","text":"{\"blocking_evidence\":null,\"headline\":\"relative form opens an action profile\",\"reader_payoff\":\"The reader sees the relative word expand a title into a full profile of giving and self-purification.\",\"reason\":\"The pronoun stands before the finite verbs and supplies their shared referent, so the form functions as both connector and identifier.\",\"representative_source_ids\":[\"QS-a3f2f4a3\",\"QF-8084d0af\",\"MT-6fdbb655\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:property-with-inclination-pressure","source_type":"word_analysis","support_id":"sup_4e3ea3a7d73fa0673177","text":"{\"blocking_evidence\":null,\"headline\":\"wealth sense carries qualified desire pressure\",\"reader_payoff\":\"The reader can feel the gift as surrender of transferable property and, by qualified derivational pressure, of what the self inclines toward.\",\"reason\":\"The local alignment is to {{ar:م و ل}} ({{tr:m-w-l}}) and V4 supports the wealth/property branch, so the alternative inclination derivation is retained only as a meaning-bearing historical pressure, not as the selected local root.\",\"representative_source_ids\":[\"QS-007537f3\",\"QS-68083645\",\"MS-67ccf321\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:self-purification-parallels","source_type":"word_analysis","support_id":"sup_550ba46b7014b89e1ca3","text":"{\"blocking_evidence\":null,\"headline\":\"final verb joins salvation purification scenes\",\"reader_payoff\":\"The reader can place the verb beside other self-purification salvation contexts (79:18; 87:14; 35:18) without letting those contexts override this local clause.\",\"reason\":\"The cited parallels use the same self-purification field and are concrete enough to retain as comparison, while local syntax still governs the reading.\",\"representative_source_ids\":[\"QI-d70b897e\",\"MI-e4768e32\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:possession-to-release-sound","source_type":"word_analysis","support_id":"sup_5683e6d5d31098f048d9","text":"{\"blocking_evidence\":null,\"headline\":\"suffix sound moves toward release\",\"reader_payoff\":\"The reader hears the possessive suffix hold the wealth close before the clause opens into the final self-purification verb.\",\"reason\":\"The sound observation follows the local surface sequence from possessed wealth to the following final verb, and it remains secondary to the grammatical hinge.\",\"representative_source_ids\":[\"QP-47e6e0ec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:18:4:1","source_type":"qac_morpheme","support_id":"sup_6ab021729f46c8c6fef2","text":"{\"lemma_ar\":\"تَزَكَّىٰ\",\"morph_features\":\"STEM|POS:V|IMPF|(V)|LEM:tazak~aY`|ROOT:zkw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:18:4:1\",\"qac_word_ref\":\"92:18:4\",\"root_ar\":\"ز ك و\",\"surface_ar\":\"يَتَزَكَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4","source_type":"word_analysis","support_id":"sup_80fd47f8b35f1a368d4f","text":"{\"gloss_range\":\"self-purifies, cultivates himself, or grows through purification; locally a finite Form V verb describing state or purpose with the same subject as the giver\",\"prose\":\"{{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}}) closes the ayah by interpreting the gift just named. As a finite imperfect, it presents self-purification as an ongoing orientation, and because there is no overt purposive particle it can be heard both as the state accompanying the gift and as the aim for which the gift is made. The subject is not renamed: the same figure who gives {{ar:مَالَهُۥ}} ({{tr:mālahū}}) is the one being purified. Form V makes that inward return visible, with the subject acting upon himself rather than an external object being purified. The root field fuses cleansing with growth, so the final verb does not reduce the scene to a payment category; it describes a self-cultivating transformation in which surrender of wealth works like pruning, removing what clings while enabling growth. That is why the echo of the common giving-and-zakah field is real but transformed: the ayah chooses a finite self-purification verb rather than a noun for alms. The word also joins other self-purification salvation scenes (79:18; 87:14; 35:18), and within this surah it links the positive path of giving and guarding (92:5) to the title defined in 92:17. In final position, the heavier doubled sound and denser t-z-k-k texture make inward purification feel weightier than the outward transfer that initiates it.\",\"root_display\":\"{{ar:ز ك و}} ({{tr:z-k-w}})\",\"root_gloss_range\":\"growth, increase, purity, rectitude, and the alms-purification field; local Form V selects self-directed purification/growth, not the noun zakah or unrelated branches such as fittingness or evenness\",\"surface_display\":\"{{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:singular-total-value","source_type":"word_analysis","support_id":"sup_82f594eadf4f6d902193","text":"{\"blocking_evidence\":null,\"headline\":\"singular possession gathers the cost\",\"reader_payoff\":\"The reader sees the wealth as one personally possessed value being surrendered, not as a generic category of charity.\",\"reason\":\"The noun appears as a singular possessed surface word with the possessor built into the same written form.\",\"representative_source_ids\":[\"QF-6721f030\",\"QF-acf2f263\",\"QF-ca35cad7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:same-agent-reflexive","source_type":"word_analysis","support_id":"sup_8c4c41b9160816992a6f","text":"{\"blocking_evidence\":null,\"headline\":\"giver is also self-purifier\",\"reader_payoff\":\"The reader sees outward giving return inwardly upon the same subject as self-purification.\",\"reason\":\"The verb is Form V, intransitive in the local frame, and shares its understood subject with the relative pronoun and the giving verb.\",\"representative_source_ids\":[\"QG-529687cb\",\"QF-80a67c71\",\"MF-6c0d61cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:retained-versus-surrendered-wealth","source_type":"word_analysis","support_id":"sup_92a8a887ebca3aef551d","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah wealth echo reverses function\",\"reader_payoff\":\"The reader sees a surah-level antithesis: wealth fails as a hoped-for support in 92:11 but defines the saved figure when given in 92:18.\",\"reason\":\"The same wealth root and possessive profile recur within the surah, but syntax reverses the role from failed subject-like support in 92:11 to surrendered object in 92:18.\",\"representative_source_ids\":[\"MI-30e18974\",\"QE-8c395991\",\"QY-f7b987fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:18:2:1","source_type":"qac_morpheme","support_id":"sup_bcb14512331aced96f29","text":"{\"lemma_ar\":\"آتَى\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:A^taY|ROOT:Aty|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:18:2:1\",\"qac_word_ref\":\"92:18:2\",\"root_ar\":\"ء ت ي\",\"surface_ar\":\"يُؤْتِى\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:clipped-sound-onset","source_type":"word_analysis","support_id":"sup_c47206678fffcbc2d8f0","text":"{\"blocking_evidence\":null,\"headline\":\"clipped verb sound precedes flowing object\",\"reader_payoff\":\"The reader hears the transfer verb as a clipped onset before the smoother possessed-wealth phrase.\",\"reason\":\"The sound observation is locally anchored in the surface form, though it remains secondary to the grammatical and lexical topics.\",\"representative_source_ids\":[\"QP-39749ada\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:heavy-final-sound","source_type":"word_analysis","support_id":"sup_c5f6ad7a321e63e8737c","text":"{\"blocking_evidence\":null,\"headline\":\"gemination gives the ending weight\",\"reader_payoff\":\"The reader hears the doubled consonant give the final self-purification verb an effortful weight.\",\"reason\":\"The surface form contains the doubled consonantal base associated with the Form V reflexive, so the sound topic is locally anchored but secondary.\",\"representative_source_ids\":[\"QF-035e83b6\",\"QP-4e4ecd98\",\"MP-cd449955\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:purity-growth-fusion","source_type":"word_analysis","support_id":"sup_d318635316f8ba450a6e","text":"{\"blocking_evidence\":null,\"headline\":\"purification and growth converge\",\"reader_payoff\":\"The reader hears the final verb as cleansing that also cultivates growth, especially after wealth has just been surrendered.\",\"reason\":\"V4 supports accepted branches for growth and for purity or rectitude, and the local self-directed verb after wealth-giving lets both pressures remain productive.\",\"representative_source_ids\":[\"QS-8747f71e\",\"QS-cb36b24c\",\"MS-a5868da3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:imperfect-state-purpose","source_type":"word_analysis","support_id":"sup_e741d835a68dc81e28f1","text":"{\"blocking_evidence\":null,\"headline\":\"finite imperfect leaves state and purpose live\",\"reader_payoff\":\"The reader notices that self-purification is ongoing and can describe both how he gives and why he gives.\",\"reason\":\"QAC marks a finite imperfect verb, and attachment evidence licenses the verb as a circumstantial state or aim accompanying the giving clause rather than a separate sequential action.\",\"representative_source_ids\":[\"QG-01d135d5\",\"QG-3f066ad5\",\"MG-4d1bae7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:3:possessed-direct-object","source_type":"word_analysis","support_id":"sup_ee30cb3d76a2a9bdbf5b","text":"{\"blocking_evidence\":null,\"headline\":\"owned wealth is the object given\",\"reader_payoff\":\"The reader notices that the act costs the giver his own possessed wealth, not an abstract resource or delegated fund.\",\"reason\":\"Attachment evidence makes the noun the direct object of the giving verb and the suffix the genitive possessor resolving to the same masculine singular subject.\",\"representative_source_ids\":[\"QG-030b7c88\",\"QG-95884e94\",\"MG-379d1d65\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:characterizing-imperfect","source_type":"word_analysis","support_id":"sup_f02533d80549ac47a24f","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect indicative marks a defining habit\",\"reader_payoff\":\"The reader hears giving as the ongoing trait by which al-atqā is recognized, not as an isolated report or instruction.\",\"reason\":\"The verb is finite imperfect indicative, with its subject supplied through the relative pronoun; no local evidence makes it imperative, jussive, conditional, or passive.\",\"representative_source_ids\":[\"QG-32fb34e4\",\"QG-4c5b1578\",\"MG-ac4c2934\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:caused-transfer","source_type":"word_analysis","support_id":"sup_f405e60c965a1cfa9e43","text":"{\"blocking_evidence\":null,\"headline\":\"Form IV makes wealth reach elsewhere\",\"reader_payoff\":\"The reader notices that the verb pictures giving as active caused arrival of owned wealth, not vague benevolence.\",\"reason\":\"QAC and verb-instance evidence identify a Form IV active imperfect with an explicit object, while the local frame leaves any recipient unexpressed.\",\"representative_source_ids\":[\"QS-d4fe182e\",\"QF-ae3c30d7\",\"MF-11901a1d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:2:giving-purification-collocation","source_type":"word_analysis","support_id":"sup_fb4d24a5323a3241a324","text":"{\"blocking_evidence\":null,\"headline\":\"giving formula becomes self-purification sequence\",\"reader_payoff\":\"The reader notices the familiar giving-and-purification field, while the local wording turns it into a sequence of giving wealth and purifying oneself.\",\"reason\":\"The cooccurrence claim is coherent and reinforced by the local adjacency to {{ar:يَتَزَكَّىٰ}} ({{tr:yatazakkā}}), but it must be narrowed because the local construction does not say the noun zakah as an object; it uses a finite self-purification verb.\",\"representative_source_ids\":[\"QI-1a58fc27\",\"QE-d6235548\",\"QY-3c02afa5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:18:3:1","source_type":"qac_morpheme","support_id":"sup_fe6250b53860b0ecf691","text":"{\"lemma_ar\":\"مَال\",\"morph_features\":\"STEM|POS:N|LEM:maAl|ROOT:mwl|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:18:3:1\",\"qac_word_ref\":\"92:18:3\",\"root_ar\":\"م و ل\",\"surface_ar\":\"مَالَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:18:4:verbal-zakah-echo-transformed","source_type":"word_analysis","support_id":"sup_ffc1f1a6b18699f70bb5","text":"{\"blocking_evidence\":null,\"headline\":\"zakah field becomes a self-process\",\"reader_payoff\":\"The reader catches the giving-and-zakah resonance while seeing that the ayah names the giver's self-purification, not an alms noun as object.\",\"reason\":\"The collocation background is supported, but the local surface is a finite verb with no expressed object, so the topic must be narrowed away from reading the word as the noun zakah itself.\",\"representative_source_ids\":[\"QF-658e776a\",\"QE-ae285665\",\"ME-2000cf97\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000009/B002","root_000637/B002","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000009","role":"The granting-and-giving branch supplies the outward transfer that initiates the mechanism.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The acquisition-and-possession branch marks the object as wealth held as one's own and therefore genuinely relinquished.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000637","role":"The purity-and-rectitude branch supplies the reflexive inward result of the outward gift.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"changed_reading":{"after":"The person transfers owned wealth in a way that recursively cleans and rectifies the giver.","before":"A person simply parts with some property."},"confidence":"strong","focus_anchor":"The sequence يُؤْتِي مَالَهُ يَتَزَكَّىٰ joins an outward transfer of what is his to an inward reflexive change.","mechanism":"Possessed wealth is deliberately granted away, and the reflexive final verb makes the release act back upon the giver as purification and rectification.","model_id":"b01_transfer_as_reflexive_purification"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b01_transfer_as_reflexive_purification","source_type":"hft","support_id":"sup_fda4e2db2bba27fe0669","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000009/B007","root_000637/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000009","role":"The yield-and-produced-increase branch makes the act of giving capable of being imaged as releasing a return or crop.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The wealth-possession branch supplies the stock whose reduction would ordinarily look like loss.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"The growth-and-increase branch turns relinquishment into the giver's productive enlargement.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"changed_reading":{"after":"Giving is a release whose paradoxical product is increase and growth in the giver.","before":"Giving diminishes the giver's available wealth."},"confidence":"medium","focus_anchor":"The giving verb and يَتَزَكَّىٰ both carry branches of yield, increase, and growth.","mechanism":"The apparent subtraction of wealth is recoded as productive release: what leaves possession becomes yield, while the giver enters a process of growth rather than mere depletion.","model_id":"b02_release_as_increase"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b02_release_as_increase","source_type":"hft","support_id":"sup_2a7d73f23e85348cfd4f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000009/B004","root_000637/B001","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000009","role":"The watercourse-and-cleared-flow branch supplies the material image of routing wealth through rather than retaining it.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The possession branch supplies what can either pool as stock or be put into circulation.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000637","role":"The growth branch supplies the flourishing made possible by the reopened course.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"changed_reading":{"after":"Wealth is a current whose deliberate routing through the giver opens a channel of growth.","before":"Wealth is a quantity from which a gift is removed."},"confidence":"exploratory","focus_anchor":"The root of يُؤْتِي includes a watercourse and cleared-flow image beside the explicit wealth and growth sequence.","mechanism":"Wealth can be carried as a moving medium rather than a static hoard: giving clears or directs its course, and unobstructed circulation permits growth.","model_id":"b03_wealth_as_routed_flow"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b03_wealth_as_routed_flow","source_type":"hft","support_id":"sup_1d73dfb73c1b46debef4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ","ayah_ref":"92:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000009/B003","root_000637/B004","root_001457/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000009","role":"The proper-access, tact, and readiness branch supplies an apt way of bringing the wealth to its destination.","root":"ء ت ي","source_ref":"92:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001457","role":"The possession branch makes wealth the entrusted material whose outlet must be found.","root":"م و ل","source_ref":"92:18","source_word_indices":["3"]},{"branch_id":"B004","mapped_root_id":"root_000637","role":"The suitability-and-fittingness branch makes the resulting act something that befits and reshapes the giver.","root":"ز ك و","source_ref":"92:18","source_word_indices":["4"]}],"changed_reading":{"after":"Purification also lies in finding wealth's fitting outlet and becoming congruent with that rightly routed act.","before":"Purification follows from losing an amount of money."},"confidence":"exploratory","focus_anchor":"The sequence can join bringing a matter through its proper access to an act that fits or befits its agent.","mechanism":"The giver does not merely surrender an amount; the giver finds the proper outlet for wealth, and this apt handling makes the act congruent with the person the giver is becoming.","model_id":"b04_proper_access_and_fittingness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b04_proper_access_and_fittingness","source_type":"hft","support_id":"sup_8038e12b74ed5c66816f","trust":"legacy_unbound"}]}
</lane_packet_json>
