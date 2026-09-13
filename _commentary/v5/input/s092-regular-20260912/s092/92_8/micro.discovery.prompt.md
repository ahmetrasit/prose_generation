# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:8**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_8/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:8",
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
{"branch_registry":[{"boundary":"Haklı bir nedenle elde tutma bu anlamın dışında kalır; kavramı belirleyen, varlığı vermemenin haksız bir esirgeme oluşturmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000089/B001","candidate_links":[{"candidate_id":"cand_16172ceae129d4efa609","lane":"micro"},{"candidate_id":"cand_638de22cc4d95fd5b7f7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"بَخِلَ","morph_features":"STEM|POS:V|PERF|LEM:baxila|ROOT:bxl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:3:1","qac_word_ref":"92:8:3","surface_ar":"بَخِلَ"}],"gloss":"eldeki varlıkları haksız yere esirgeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eldeki varlıkları, alıkonmaları haklı olmadığı halde verilmesi gereken kişi ya da amaçtan esirgeme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Esirgeme kişinin kendi varlıklarına ilişkin olabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Esirgeyici tutum başkasına ait varlıklar üzerinde de gösterilebilir."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kavram, yerleşik bir kişi özelliğinin yanı sıra tek bir esirgeme olayını da anlatabilir."}}],"root_ar":"ب خ ل","root_id":"root_000089","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alıkoymanın haklı olmadığı ve varlığın verilmesi gereken yerden esirgendiği bütün çekirdek kullanımlarda geçerlidir.","boundary_detail":"Haklı bir nedenle elde tutma bu anlamın dışında kalır; kavramı belirleyen, varlığı vermemenin haksız bir esirgeme oluşturmasıdır.","branch_image_ar":"البخل","concept_gloss":"eldeki varlıkları haksız yere esirgeme","contextual_glosses":[{"applicability":"Bağlamın haksız esirgeme ölçütünü ve söz konusu varlıkları açıkça gösterdiği genel kullanımlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vermesi beklenen varlığı haksız biçimde esirgeyen tutumun genel adını korur."},"facet_ids":["F001"],"text":"cimrilik","usage_role":"general"},{"applicability":"Özellikle kişinin kendi varlıklarını vermeye yanaşmayan yerleşik tutumunun anlatıldığı kişi odaklı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına ait varlıklar üzerindeki esirgeme ile tek olay anlamını doğal olarak öne çıkarmaz.","preserves":"Kişinin elindeki varlığı vermekten kaçınan esirgeyici tutumunu korur."},"facet_ids":["F001","F002"],"text":"eli sıkılık","usage_role":"contextual"},{"applicability":"Bir eğilimden çok somut esirgeme davranışının açıklandığı ve eldeki varlığın bağlamdan anlaşıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Vermeme eylemini ve bu eylemin haklı bir alıkoyma olmayışını birlikte korur."},"facet_ids":["F001","F004"],"text":"haksız yere vermekten kaçınma","usage_role":"explanatory"}],"definition":"Kişinin, alıkonması haklı olmayan eldeki varlıkları verilmesi gereken kişi ya da amaçtan esirgemesidir. Bu tutum kişinin kendi varlıklarına veya başkasına ait varlıklara yönelik olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eldeki varlıkları, alıkonmaları haklı olmadığı halde verilmesi gereken kişi ya da amaçtan esirgeme."},{"facet_id":"F002","role":"specialization","statement":"Esirgeme kişinin kendi varlıklarına ilişkin olabilir."},{"facet_id":"F003","role":"specialization","statement":"Esirgeyici tutum başkasına ait varlıklar üzerinde de gösterilebilir."},{"facet_id":"F004","role":"specialization","statement":"Kavram, yerleşik bir kişi özelliğinin yanı sıra tek bir esirgeme olayını da anlatabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ölçülü ve haklı kaynak yönetimi anlamını ekler.","collision":"Olumlu görülen ekonomik davranışla karışır.","fit":"displacement","loses":"Vermemenin haksız oluşunu ve verilmesi gereken kişi ya da amacı yoksun bırakma yönünü siler.","preserves":"Eldeki varlığı hemen elden çıkarmama yönünü korur."},"text":"tutumluluk"},{"category":"confusable","error_profile":{"adds":"Biriktirme, depolama ve yığma davranışını ekler.","collision":"Vermemekten çok nesne biriktirme davranışıyla karışır.","fit":"displacement","loses":"Varlığı hakkı olan kişi ya da amaçtan esirgeme koşulunu siler.","preserves":"Varlıkları elde tutma yönünü korur."},"text":"istifçilik"},{"category":"alternative","error_profile":{"adds":"Haksız esirgeme içermeyen sıradan veya nötr vermeme durumlarını da kapsar.","collision":"Yalnızca cömertlik göstermemek ile etkin biçimde esirgemeyi birbirine yaklaştırır.","fit":"broadening","loses":"Eldeki varlığı haksız yere esirgeme biçimindeki belirleyici eylemi açıkça söylemez.","preserves":"Cömertçe vermenin bulunmadığı olumsuz kutbu korur."},"text":"cömert olmama"}],"identity_rationale":"Dal çerçevesi, eldeki varlıkları alıkoymanın haklı olmadığı bir durumda onları verilmesi gereken kişi ya da amaçtan esirgeme çekirdeğini doğru biçimde yansıtır. Kişinin kendi varlıklarına ve başkasına ait varlıklara ilişkin kullanımlar, kişi nitelemeleri ve tek bir esirgeme olayı bu çekirdeğe bağlı alt ayrımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"cimrilik; eldeki varlıkları haksız yere esirgeme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"cimrilik etmek; verilmesi gerekeni esirgemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"cimrilik eden kişi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sık sık cimrilik eden; cimri"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"cimriliği huy edinmiş kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"cimri diye nitelenen kişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tek bir cimrilik davranışı"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kişinin kendi varlıklarını esirgemesi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başkasına ait varlıklar konusunda esirgeyici davranma; daha ağır kınanan biçim"}],"lexicalization_note":"Tanım ortak anlam çekirdeğini verir; kişi nitelemeleri, tek olay anlatımı ve kişinin kendi ya da başkasının varlıklarına bağlı kullanımlar ayrı yüzler olarak korunur ve tek başlarına yalın çekirdeğe genellenmez.","neighbor_coverage_note":"Sekiz adayın tümü değerlendirildi; en açıklayıcı dört karşılaştırma yayımlandı. Geri kalanlar kişi için kullanılan bir niteleme, aynı karşıt kutbun yinelenen bir görünümü veya yaşam süresine bağlı bağış düzenlemeleri sunduğundan sınırı ayrıca keskinleştirmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği varlığın haksız yere alıkonmasına bağlıdır; komşu dal ise herhangi bir şeyden geri durmaya ve özellikle yardımı kesmeye uzanır. Bu nedenle örtüşürler, fakat sıradan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal, eldeki varlıkların alıkonması haklı değilken verilmesi gereken yerden esirgenmesini ve bunun mülkiyete göre alt biçimlerini belirler.","gloss":"geri durup yardımı esirgeme","neighbor_only":"Komşu dal genel geri durmayı, yardımı kesmeyi ve iyiliğin azlığını aynı alan içinde bir araya getirir.","neighbor_ref":"root_000328/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da beklenen bir yararı sunmama ve iyiliği kısma yönü vardır."},{"boundary_match":"partial","distinction":"Odak dal varlıkların haksız alıkonmasına dayanır; komşu dal ise iyiliğin genel azlığına ve bir hakkı yerine getirmemeye kadar genişler. Ortak esirgeme alanı güçlü olsa da kapsam sınırları aynı değildir.","focus_only":"Odak dal, kişinin kendi veya başkasına ait eldeki varlıkları haksız yere esirgemesini açık bir ölçüt olarak taşır.","gloss":"iyilik yapmaya eli varmama","neighbor_only":"Komşu dal iyilik yapmaya elin varmamasını, iyiliğin azlığını ve yerine getirilmesi gereken bir hakkı sunmamayı daha geniş bir görünüm altında toplar.","neighbor_ref":"root_000258/B003","relation_type":"near_neighbor","shared_zone":"İki dal da verilmesi veya yapılması beklenen iyiliğin sunulmamasında kesişir."},{"boundary_match":"opposed","distinction":"Odak dal bu yöneltmeyi haksız biçimde engellerken komşu dal onu geniş ve cömert biçimde gerçekleştirir; aynı verme ekseninde karşıt kutuplardır.","focus_only":"Odak dal, verilmesi gereken eldeki varlığı haksız yere esirger.","gloss":"cömertçe iyilikte bulunma","neighbor_only":"Komşu dal, iyilikte geniş davranarak cömertçe verir.","neighbor_ref":"root_000405/B006","relation_type":"antonym","shared_zone":"Her ikisi de kişinin elindeki imkânı başkasına veya bir iyilik amacına yöneltme eksenindedir."},{"boundary_match":"partial","distinction":"Odak dal normatif olarak haksız esirgemeyi tanımlar; komşu dal ise elde tutulan mal ve iyiliğin azlığı çevresindeki betimleyici görünüme dayanır. Yakın bir alan paylaşırlar, ancak çekirdekleri birbirinin yerine kullanılamaz.","focus_only":"Odak dal, esirgemenin haksız oluşunu ve varlığın verilmesi gereken yerden alıkonmasını anlamın zorunlu koşulu yapar.","gloss":"malı tutup iyiliği kısma","neighbor_only":"Komşu dal tutulmuş mal görünümünü, az iyilik eden kişiyi ve vermeyi kısma çağrışımını birlikte taşır.","neighbor_ref":"root_000338/B004","relation_type":"near_neighbor","shared_zone":"İki dal malı elde tutma ve beklenen iyiliği azaltma görünümünde örtüşür."}],"source_phrase_ar":"البخل والبخل؛ رجل بخيل وباخل؛ فهو بخال (maqayis); بخل بخلا وبخلا فهو بخيل بخال مبخل؛ والبخلة بخل مرة واحدة (ayn); البخل إمساك المقتنيات عما لا يحق حبسها عنه؛ ويقابله الجود؛ البخل ضربان بخل بقنيات نفسه وبخل بقنيات غيره (mufradat)","source_summary":"Ortak anlam, eldeki varlıkların tutulması haklı olmadığı halde verilmesi gereken yerden esirgenmesidir ve bunun karşı kutbunda cömertçe verme bulunur. Bu anlam kişinin kendi varlıklarına veya başkasına ait varlıklara yöneltilebilir; ayrıca davranış, bunu yapan kişi ve tek bir olay ayrı dilsel biçimlerle anlatılır.","sources":["MQ","AY","MU"],"what_is_ar":"إمساك المقتنيات عما لا يحق حبسها عنه وما يتصل به من بخيل وباخل وبخال ومبخل والبخلة وبخل قنيات النفس وقنيات الغير","what_is_not_ar":"الجود؛ مطلق الإمساك بحق"},"support_links":["sup_0542e0121dd688297e66","sup_ab3f358f8b44e4a47975"]},{"boundary":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B001","candidate_links":[{"candidate_id":"cand_16172ceae129d4efa609","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi varlık ile ihtiyaç duymama çekirdeğini birlikte anlatan genel kavram karşılığıdır.","boundary_detail":"Dal, başkasının ihtiyacını karşılamayı, sesle ezgi söylemeyi veya bir yerde kalmayı değil, varlıklı ve ihtiyaçtan bağımsız olmayı anlatır.","branch_image_ar":"الغنى والاستغناء","concept_gloss":"maddi bolluk ve ihtiyaçtan bağımsızlık","contextual_glosses":[{"applicability":"Bağlam yalnızca para, mal ve maddi bolluk durumunu öne çıkardığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ile bir şey sayesinde yetinme ilişkisini tek başına açıkça vermez.","preserves":"Maddi varlık ve bolluk yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"zenginlik","usage_role":"contextual"},{"applicability":"Kişinin bir şeye ihtiyaç duymaması veya elindekiyle yetinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Maddi servet ve çok sayıda mala sahip olma yönünü zorunlu olarak taşımaz.","preserves":"İhtiyaçtan bağımsızlık ve bir şeyle yetinme yönünü korur."},"facet_ids":["F002","F003"],"text":"kendine yetmek","usage_role":"contextual"}],"definition":"Maddi varlığa ve bolluğa sahip olma, ihtiyaç duymama ya da az ihtiyaç duyma durumudur. Bağıntılı kullanımlarda kişi bir şey sayesinde yetinir veya başka bir şeye gerek duymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Maddi varlık, bolluk ve çok sayıda mala sahip olma durumunu kapsar."},{"facet_id":"F002","role":"core","statement":"İhtiyaçların bulunmaması ya da az olması, maddi bollukla birlikte çekirdeğin bir parçasıdır."},{"facet_id":"F003","role":"extension","statement":"Bir şeyle yetinerek veya bir şeye gerek duymayarak ihtiyaçtan bağımsız hale gelme, bağıntılı yapılarda gerçekleşir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İhtiyaç duymama ve bir şeyle yetinme yönlerini karşılamaz.","preserves":"Maddi mala ve bolluğa sahip olma yönünü korur."},"text":"varlıklılık"},{"category":"confusable","error_profile":{"adds":"Bir şeyin başkası için yeterli olma işlevini çağrıştırır.","collision":"Başkası için yeterli olma dalıyla karışır.","fit":"displacement","loses":"Maddi bolluk ve kişinin ihtiyaçtan bağımsız olma durumunu silikleştirir.","preserves":"İhtiyacın karşılanmış olmasıyla ilgili sınırlı bir yakınlığı korur."},"text":"yeterlilik"}],"identity_rationale":"Kaynak sözü, maddi varlık ve bolluğun yanı sıra ihtiyaç duymama ya da az ihtiyaç duyma durumunu açıkça birlikte verir. Bir şey sayesinde yetinme ve bir şeye gerek duymama anlatımları da bu çekirdeğin bağıntılı kullanımlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"maddi zenginlik, bolluk ve ihtiyaçsızlık"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"varlıklı, zengin"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ona ihtiyaç duymamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"onunla yetinip başka bir şeye ihtiyaç duymamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeye ihtiyaç duymama durumu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"zenginlik ve bolluk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gönül tokluğu ve az şeye ihtiyaç duyma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"zengin etmek veya yoksunluğunu gidermek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"Kur'an'la yetinip başka bir şeye ihtiyaç duymamak"}],"lexicalization_note":"Yalın biçimler maddi bolluk ve ihtiyaçsızlık durumunu adlandırırken bağıntılı yapılar bir şeyle yetinmeyi veya bir şeye gerek duymamayı belirtir; bu iki kapsam tanımda ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; maddi bolluk, yeterlik ve sonradan zenginleşme sınırlarını en açık gösteren dört karşılaştırma seçildi, yalnızca dar örnek veya uzak alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir sahibin varlık ve ihtiyaçsızlık durumunu anlatır; komşu dal ise bir unsurun başka biri için yeterli olma ve onun işini görme ilişkisini anlatır.","focus_only":"Kişinin maddi bolluğu ve kendisinin ihtiyaçtan bağımsız oluşu bu dala özgüdür.","gloss":"kendine yeterlik ve başkasına yetme","neighbor_only":"Bir şeyin veya kişinin başkası için yeterli olması, yarar sağlaması ve onun yerini tutması komşuya özgüdür.","neighbor_ref":"root_001110/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir ihtiyacın ortadan kalkması veya karşılanması çevresinde buluşur."},{"boundary_match":"partial","distinction":"Komşu dal genişlik ve refahı öne çıkarırken odak dal bunu ihtiyaçların yokluğu veya azalması ve bağımsızlıkla daha sıkı bağlar.","focus_only":"Az ihtiyaç duyma, çok mala sahip olma ve bir şeyle yetinme bağıntıları odakta açıkça yer alır.","gloss":"bolluk ve refah","neighbor_only":"Genel genişlik ve ferahlık anlatımı komşu dalda daha belirgindir.","neighbor_ref":"root_001694/B003","relation_type":"near_synonym","shared_zone":"İki dal da maddi genişlik, refah ve yoksunluktan çıkma durumunu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal zenginliği ihtiyaçtan bağımsızlıkla tanımlar; komşu dal ise birikmiş malın veya başka şeylerin çokluğuna kadar genişleyebilir.","focus_only":"İhtiyaç duymama veya bir şeyle yetinme odak dalın kurucu sınırıdır.","gloss":"zenginlik ve mal çokluğu","neighbor_only":"Her tür çokluk ve malı iyi yönetme anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000459/B001","relation_type":"near_synonym","shared_zone":"Her iki dal maddi varlığın çokluğunu ve zenginliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel ve sürebilen bir zenginlik durumudur; komşu dal aynı sonucu özellikle önceki yoksulluktan sonraki değişim olarak sınırlar.","focus_only":"Öncesinde yoksulluk bulunması gerekmeksizin varlıklı ve ihtiyaçsız olmayı kapsar.","gloss":"zenginlik ve sonradan zenginleşme","neighbor_only":"Yoksulluktan sonra zenginleşme geçişi komşu dalın zorunlu koşuludur.","neighbor_ref":"root_000406/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin zengin duruma gelmesini veya zengin olmasını içerir."}],"source_phrase_ar":"الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)","source_summary":"Kaynakların ortak çerçevesi maddi zenginliği, bolluğu ve ihtiyaçların yokluğunu ya da azalmasını bir araya getirir; ayrıca bir şeyle yetinip başkasına ihtiyaç duymama kullanımını destekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغنى في المال والوفر وعدم الحاجة أو قلتها وكثرة القنيات والاستغناء بالشيء أو عنه وتغنى وتغانى بمعنى استغنى","what_is_not_ar":"ليس إجزاء الشيء عن غيره ولا الغناء بالصوت ولا المقام بالمكان"},"support_links":["sup_0542e0121dd688297e66"]},{"boundary":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B002","candidate_links":[{"candidate_id":"cand_638de22cc4d95fd5b7f7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir unsurun başkası için hem yeterli hem yararlı olması ve gerektiğinde başka bir unsurun işlevini üstlenmesi için kullanılır.","boundary_detail":"Dal, kendisi ihtiyaçsız olma durumundan ayrılır; burada bir unsur başka biri için yeterli olur, onun ihtiyacını karşılar veya yerini doldurur.","branch_image_ar":"الغَناء والكفاية","concept_gloss":"ihtiyacı karşılayıp yarar sağlama ve yerini tutma","contextual_glosses":[{"applicability":"Bir şeyin miktar veya işlev bakımından ihtiyacı karşılaması öne çıktığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yarar sağlama ve başka bir unsurun yerini tutma yönlerini açıkça belirtmez.","preserves":"Yeterli olma ve ihtiyacı karşılama çekirdeğini korur."},"facet_ids":["F001"],"text":"yetmek","usage_role":"contextual"},{"applicability":"Bir unsurun beklenen yararı sağlaması veya başka bir unsur yerine kullanılabilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yeterlik ile ihtiyacın bütünüyle karşılanmasını zorunlu olarak anlatmaz.","preserves":"Yarar sağlama ve beklenen işlevi yerine getirme yönünü korur."},"facet_ids":["F002","F003"],"text":"işini görmek","usage_role":"contextual"}],"definition":"Bir şeyin ya da kişinin başkası için yeterli olması, onun ihtiyacını karşılaması ve yarar sağlamasıdır; bağlama göre başka bir unsurun işini görüp onun yerini de tutabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir unsur, başka bir kişi veya durum için yeterli olur ve ihtiyacı karşılar."},{"facet_id":"F002","role":"core","statement":"Yeterli olan unsur yarar sağlar ve beklenen işlevi yerine getirir."},{"facet_id":"F003","role":"extension","statement":"Bağıntılı kullanımlarda bir kişi veya şey, başka birinin ya da şeyin yerini tutar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeterli olma, ihtiyacı karşılama ve başkasının yerini tutma ilişkilerini vermez.","preserves":"Olumlu sonuç ve işe yarama yönünü korur."},"text":"yarar"},{"category":"confusable","error_profile":{"adds":null,"collision":"Genel değiştirme ve takas alanıyla karışabilir.","fit":"narrowing","loses":"Yer değiştirme bulunmayan yeterlik ve yarar kullanımlarını dışarıda bırakır.","preserves":"Bir unsurun başka bir unsurun işlevini üstlenmesi yönünü korur."},"text":"yerine geçme"}],"identity_rationale":"Kaynak sözü, bir şeyin ya da kişinin başkası için yeterli olmasını, ihtiyacı karşılamasını, yarar sağlamasını ve gerektiğinde başka bir unsurun yerini tutmasını birlikte verir. Bu nedenle dalın çekirdeği, sahibin zenginliği değil, iki katılımcı arasındaki yeterlik ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yeterlilik, ihtiyacı karşılama ve yarar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu sana yetmez ve yarar sağlamaz"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yeterli ve ihtiyacı karşılayan"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin yerini tutan yeterlilik ve işlev"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"zararını benden uzak tut"}],"lexicalization_note":"Yalın biçimler yeterlik ve yararı adlandırır; bağıntılı yapılar kimin için yeterli olunduğunu, neyin yerini tuttuğunu veya hangi zararın uzak tutulduğunu açıklar.","neighbor_coverage_note":"Bütün adaylar incelendi; genel yeterlik, bir şeyle yetinme, başkası adına iş görme ve gerçek değiştirme arasındaki sınırları gösteren dört aday seçildi, daha uzak alan ortaklıkları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir unsurun başkası için yeterli ve yararlı oluşuna dayanır; komşu dal ise işi üstlenip sürdürerek açığı kapatma ve sonuca ulaştırma sürecini öne çıkarır.","focus_only":"Yarar sağlama ve bir kişi ya da şeyin yerini tutma ilişkileri odakta açıkça bulunur.","gloss":"yetme ve işi tamamlayarak yetme","neighbor_only":"Bir işi yürütüp açığı kapatarak amaca ulaşma süreci komşu dalda daha belirgindir.","neighbor_ref":"root_001310/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bir ihtiyacın karşılanması ve yeterli sonucun elde edilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal genel yeterlik ve yararı da içerir; komşu dal yerini tutma ve özellikle bir yükümlülüğü başkası adına yerine getirme ilişkisine daha sıkı bağlıdır.","focus_only":"Bir şeyin yalnızca yeterli veya yararlı olması, yer değiştirme gerçekleşmeden de bu dala girebilir.","gloss":"yetme ve başkasının yerine ödeme","neighbor_only":"Hak, borç veya bağış gibi yükümlülükleri başkası adına yerine getirme komşu dalın ek alanıdır.","neighbor_ref":"root_000244/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir unsurun başka birinin yerini tutup onun adına yeterli olmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dal yeterli unsur ile yararlanan katılımcı arasındaki ilişkiyi kurar; komşu dal eldeki şeyle yetinme ve başkasından vazgeçebilme sonucunu öne çıkarır.","focus_only":"Bir kişinin ya da şeyin başkası için yararlı ve yeterli olup onun yerini tutması odakta belirgindir.","gloss":"ihtiyacı karşılama ve bir şeyle yetinme","neighbor_only":"Bir şeyle yetinip başka bir şeye gerek duymama sonucu komşu dalda çekirdeğe daha yakındır.","neighbor_ref":"root_000241/B001","relation_type":"near_synonym","shared_zone":"Her iki dal, eldeki bir unsurun ihtiyacı karşılayarak başka bir gereği ortadan kaldırmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal işlev bakımından yetmeyi anlatır; komşu dal ise bir unsurun yerine diğerini koyma veya onları değiştirme işlemini anlatır.","focus_only":"Yeterli olma ve yarar sağlama, gerçek bir değiştirme işlemi olmadan da gerçekleşebilir.","gloss":"işlevsel yeterlik ve değiştirme","neighbor_only":"Bir unsurun çıkarılıp yerine başka bir unsurun konması ve karşılıklı değiştirme komşu dala özgüdür.","neighbor_ref":"root_000095/B001","relation_type":"near_neighbor","shared_zone":"Bir unsurun başka bir unsurun konumunu veya işlevini üstlenmesi iki dalda da görülebilir."}],"source_phrase_ar":"الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)","source_summary":"Kaynaklar yeterli olma, ihtiyacı karşılama, yarar sağlama ve başkasının yerini tutma yönlerinde birleşir; olumsuz yapılarda aynı ilişki yetersizlik veya yararsızlık olarak görünür.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يكفي الشيء أو الشخص غيره ويجزئ عنه وينفعه ويقوم مقامه","what_is_not_ar":"ليس اليسار والوفر ولا الغناء بالصوت ولا سكنى المكان"},"support_links":["sup_ab3f358f8b44e4a47975"]},{"boundary":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ses üretme, dinleme ve özel metin okuma yönlerini birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Çekirdek sesle ezgi üretme ve dinleme alanıdır; okuyuştaki duygulu seslendirme özel kullanımdır, maddi zenginlik ve yeterlik bu dala girmez.","branch_image_ar":"الغِناء والصوت","concept_gloss":"sesle ezgi söyleme, dinleme ve ezgili okuma","contextual_glosses":[{"applicability":"İnsan sesiyle ezgili bir parça seslendirme eylemi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dinleme ile metni hüzünlü ve yumuşak sesle okuma yönlerini dışarıda bırakır.","preserves":"Sesle ezgi üretme ve ezgili parça yönlerini korur."},"facet_ids":["F001","F002"],"text":"şarkı söylemek","usage_role":"contextual"},{"applicability":"Bir metnin sesi yumuşatıp duygulandırarak ezgili biçimde okunması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel şarkı söyleme, ezgili parça ve dinleme alanlarını kapsamaz.","preserves":"Okuyuşta ezgi, hüzün ve ses yumuşaklığı yönünü korur."},"facet_ids":["F003"],"text":"ezgili okumak","usage_role":"contextual"}],"definition":"Sesle ezgi söyleme, söylenen ezgili parça ve bunu dinleme alanıdır. Okuyuşu ezgili, hüzünlü ve yumuşak bir sesle gerçekleştirme bunun özel bir uygulamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan sesiyle ezgi söyleme ve bu seslendirmeyi dinleme çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Ezgili biçimde söylenen tek bir parça, bu ses etkinliğinin ürünüdür."},{"facet_id":"F003","role":"specialization","statement":"Bir metni ezgili, hüzünlü ve yumuşak sesle okumak, seslendirme çekirdeğinin özel kullanımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İnsan sesi bulunmayan çalgısal üretim ve düzenleme alanlarını da kapsar.","collision":"Çalgı müziğiyle gereksiz bir kapsam çakışması doğurur.","fit":"broadening","loses":null,"preserves":"Ezgi ve işitsel sanat alanıyla olan bağı korur."},"text":"müzik"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Söyleme ve dinleme etkinliğiyle özel ezgili okuma kullanımını tek başına karşılamaz.","preserves":"Ezgili söylenen parça yönünü güçlü biçimde korur."},"text":"şarkı"}],"identity_rationale":"Kaynak sözü sesle ezgi söylemeyi, söylenen ezgili parçayı ve dinlemeyi açıkça bu dalda toplar. Okuyuşu ezgili, hüzünlü ve yumuşak seslendirme ise aynı ses kullanımının özel bir uygulamasıdır, dalın bütününü tek başına tanımlamaz.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"şarkı söyleme, ezgili seslendirme ve dinleti"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"şarkı; ezgili söylenen parça"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"şarkı söylemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"şarkı söylemek veya sesi ezgili ve duygulu kullanmak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak"}],"lexicalization_note":"Yalın biçimler şarkı söyleme, ezgili parça ve dinletiyi adlandırır; belirli metni ezgili okuma anlamı yalnızca ilgili bağıntılı yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hoş insan sesi, özel yolcu ezgisi, ses yineleme ve çalgı sesiyle sınırı en iyi gösteren dört aday seçildi, yalnızca yüksek ses veya uzak konu ortaklığı sunanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şarkı söyleme, parça, dinleme ve özel okuma kullanımını toplar; komşu dal özellikle hoş işitilen ses niteliği ve bunu üreten kişiye yönelir.","focus_only":"Ezgili parça ile metni hüzünlü ve yumuşak sesle okuma kullanımı odakta açıkça bulunur.","gloss":"şarkı ve hoş ezgili ses","neighbor_only":"Sesin hoş ve zevk verici niteliği ile icracıyı adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_000741/B007","relation_type":"near_synonym","shared_zone":"İki dal da insan sesiyle üretilen hoş ezgiyi ve şarkı söylemeyi kapsar."},{"boundary_match":"partial","distinction":"Odak dal geniş sesli ezgi alanını anlatır; komşu dal bunu yüksek sesli ve yolculukla ilişkili belirli bir söyleyiş türüyle sınırlar.","focus_only":"Genel şarkı söyleme, ezgili parça, dinleme ve yumuşak okuyuş odak dalda yer alır.","gloss":"genel şarkı ve yolcu ezgisi","neighbor_only":"Yolcuların yüksek sesle söylediği çağrı ve belirli ezgi türü komşuya özgüdür.","neighbor_ref":"root_001507/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal insan sesiyle ezgili söyleme etkinliğine girer."},{"boundary_match":"partial","distinction":"Odak dal ezgi üretimi ve dinlemeyi tanımlar; komşu dal sesin yinelenmesi veya geri döndürülmesi biçimine dayanır ve ezgi gerektirmez.","focus_only":"Ezgili parça ve şarkı söyleme etkinliği odak dalın merkezindedir.","gloss":"ezgili söyleme ve ses yineleme","neighbor_only":"Çağrı, gök gürültüsü ve başka seslerde yineleme veya yankılanma komşu dalın ek kapsamıdır.","neighbor_ref":"root_000544/B007","relation_type":"near_neighbor","shared_zone":"Şarkı ve okuma sırasında sesin düzenli biçimde çevrilmesi iki dalda kesişebilir."},{"boundary_match":"field_only","distinction":"Odak dal insan sesi ve şarkıya dayanır; komşu dalın çekirdeği üflemeli çalgıdan çıkan sestir ve insan sesi zorunlu değildir.","focus_only":"İnsan sesiyle şarkı söyleme ve metni ezgili okuma odak dalın çekirdeğidir.","gloss":"insan sesi ve çalgı sesi","neighbor_only":"Üflemeli çalgıyla ses üretme ve aynı sözcüğün bazı hayvan seslerine uygulanması komşuya özgüdür.","neighbor_ref":"root_000643/B002","relation_type":"same_field","shared_zone":"İki dal ezgili veya hoş işitilebilen ses üretimi alanında buluşur."}],"source_phrase_ar":"الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)","source_summary":"Kaynaklar insan sesiyle ezgi söyleme, ezgili parça ve dinleme anlamlarında birleşir; ayrıca okuyuştaki ezgili, hüzünlü ve yumuşak seslendirmeyi özel bir kullanım olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغناء بالصوت والأغنية والسماع والتطريب وتحزين القراءة وترقيقها","what_is_not_ar":"ليس الغنى في المال ولا الغَناء بمعنى الكفاية ولا المقام بالمكان"},"support_links":[]},{"boundary":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001110/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"bir yerde uzun süre kalıp yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yer, süre ve yaşama katılımlarını birlikte taşıyan genel kavram karşılığıdır.","boundary_detail":"Dalın çekirdeği bir yerde oturmak ve uzun süre kalmaktır; geçmişte orada yaşamış olma ile ev ve yer adları buna bağlıdır.","branch_image_ar":"الغنى بالمكان","concept_gloss":"bir yerde uzun süre kalıp yaşama","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun belirli bir yeri yaşama yeri edinmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süre kalma vurgusunu ve bundan doğan yer adlarını açıkça vermez.","preserves":"Belirli bir yerde yaşama ve yerle bağ kurma yönünü korur."},"facet_ids":["F001"],"text":"bir yerde oturmak","usage_role":"contextual"},{"applicability":"Kalınan yer ile kalış süresinin öne çıktığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Orada yaşama ile ev veya yer adı türetme yönlerini zorunlu olarak taşımaz.","preserves":"Belirli yerde kalma ve süreklilik yönünü korur."},"facet_ids":["F001"],"text":"uzun süre kalmak","usage_role":"contextual"},{"applicability":"Geçmişte bir yerde bulunmuş ve yaşamış olmanın sonradan yokluğu anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel uzun süre kalma çekirdeği ile konut ve eylem adlarını kapsamaz.","preserves":"Geçmişte o yerde yaşama veya bulunma yönünü korur."},"facet_ids":["F002"],"text":"orada yaşamış olmak","usage_role":"contextual"}],"definition":"Bir yerde oturmak, orada uzun süre kalmak ve yaşamak anlamıdır. Geçmişte orada bulunmuş olma anlatımı ile bir topluluğun oturduğu evleri, kalma eylemini veya kalınan yeri bildiren adlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya topluluk belirli bir yerde oturur ve orada uzun süre kalır."},{"facet_id":"F002","role":"extension","statement":"Bağlama göre aynı alan, kişinin geçmişte o yerde yaşamış veya bulunmuş olmasını anlatır."},{"facet_id":"F003","role":"associated_use","statement":"Bir topluluğun oturduğu evler ile kalma eylemi veya kalınan yer bu çekirdekten adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun süreli oturma, yaşama ve o yerin ev sayılması yönlerini zayıflatır.","preserves":"Belirli bir yerde kalma yönünü korur."},"text":"konaklamak"},{"category":"alternative","error_profile":{"adds":"Başlangıçtaki taşınma ve kalıcı düzen kurma olayını öne çıkarır.","collision":"Yer edinme eylemiyle kalış durumunu birbirine yaklaştırır.","fit":"displacement","loses":"Geçmişte bulunmuş olma ve yalnızca uzun süre kalma kullanımlarını daraltır.","preserves":"Bir yeri yaşama yeri edinme yönünü korur."},"text":"yerleşmek"}],"identity_rationale":"Kaynak sözü bir yerde oturup uzun süre kalmayı çekirdek olarak verir; orada yaşamış veya bulunmuş olma anlatımı ile oturulan ev ve yer adları bu çekirdekten doğan kullanımlardır. Bu nedenle geçici bulunma ile konut adı aynı düzeyde tek anlam sayılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir yerde oturmak ve uzun süre kalmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sanki daha dün orada hiç yaşamamıştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir topluluğun oturduğu evler ve yurtlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"oturma eylemi veya oturulan yer"}],"lexicalization_note":"Bir yerde uzun kalma ve geçmişte orada yaşama anlamları belirli bağıntılı yapılarda görünür; yalın ad biçimleri ise kalma eylemini veya oturulan yeri gösterir.","neighbor_coverage_note":"Bütün adaylar incelendi; uzun kalış, genel kalma, konut edinme ve oturma duruşu arasındaki sınırı gösteren beş aday seçildi, yalnızca yer adı veya uzaktan alan ortaklığı sunanlar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama, geçmişte bulunma ve konut adlarına uzanır; komşu dal ise yerleşik kalmayı farklı kişi durumlarına ve özel kalış bağlamlarına genişletir.","focus_only":"Topluluğun evleri ile kalma eylemini veya yerini adlandıran biçimler odakta bulunur.","gloss":"uzun süre yaşama ve yerleşik kalma","neighbor_only":"Yabancının kalışı, kutsal yerde komşuluk, hapiste kalma ve öldürülmüş kişi kullanımları komşuya özgüdür.","neighbor_ref":"root_000211/B001","relation_type":"near_synonym","shared_zone":"İki dal da belirli bir yerde oturma, kalma ve özellikle uzun süren yerleşikliği anlatır."},{"boundary_match":"partial","distinction":"Odak dal uzun yaşama ile bundan doğan ev ve yer adlarını toplar; komşu dal aynı alanı durma, bekleme ve soyut yerleşiklik kullanımlarına taşır.","focus_only":"Geçmişte orada yaşamış olma ve topluluğun evlerini adlandırma odakta belirgindir.","gloss":"oturma ve yerleşik kalma","neighbor_only":"Durma, ağırdan alma ve eskiden beri yerleşmiş bir iş anlatımı komşu dalın ek kapsamıdır.","neighbor_ref":"root_000536/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir yerde oturma, ev ve yerleşik kalma alanında geniş ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dal süreyi, yaşamayı ve bağlı yer adlarını içerir; komşu dal ise süre veya konut sonucu belirtmeden bir yerde kalma eylemiyle sınırlıdır.","focus_only":"Uzun süre yaşama, geçmişte bulunma ve oturulan evleri adlandırma odakta yer alır.","gloss":"uzun süre yaşama ve bir yerde kalma","neighbor_only":"Komşu dal yalnızca bir yerde kalmayı bildiren daha dar bir eylem çerçevesidir.","neighbor_ref":"root_000168/B016","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin belirli bir yerde kalmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal sürmekte olan kalış ve yaşam durumunu anlatır; komşu dal ise yeri konut seçme ya da başkasına konut sağlama işlemini öne çıkarır.","focus_only":"Bir yerde fiilen uzun süre yaşama ve geçmişte orada bulunmuş olma odak dalın merkezidir.","gloss":"orada yaşama ve konut edinme","neighbor_only":"Bir yeri konut edinme veya birini bir yere yerleştirme işlemi komşu dalda belirgindir.","neighbor_ref":"root_000162/B001","relation_type":"near_neighbor","shared_zone":"İki dal da kişi ile yaşadığı yer arasında kalıcı veya uzun süreli bir bağ kurar."},{"boundary_match":"partial","distinction":"Odak dal yaşama yeri ve uzun kalışla ilgilidir; komşu dal bedenin oturma duruşunu ve bu duruş çevresindeki birlikteliği anlatır.","focus_only":"Yerde uzun süre yaşama ve o yeri konut edinme odak dala özgüdür.","gloss":"bir yerde yaşama ve oturma duruşu","neighbor_only":"İnsan bedeninin oturma duruşu, oturum ve birlikte oturma komşu dalın çekirdeğidir.","neighbor_ref":"root_000254/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda kişi bir yerde bulunur ve o yere bağlı bir süreklilik gösterebilir."}],"source_phrase_ar":"غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)","source_summary":"Kaynaklar bir yerde oturma ve uzun süre kalma çekirdeğinde birleşir; geçmişte orada yaşama anlatımını, topluluğun evlerini ve hem eylemi hem yeri gösterebilen adları da bu alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإقامة وطول المقام في الدار أو المحلة والمغاني منازل القوم والمغنى للمصدر أو المكان وما يقرب من العيش والكون السابق","what_is_not_ar":"ليس الغنى في المال ولا الكفاية ولا الغناء بالصوت"},"support_links":[]},{"boundary":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_kind":"bare","branch_ref":"root_001110/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana açıklama ile kaynaklarda görülen daha geniş kadın nitelemelerini birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Süsten bağımsız sayılma ana açıklamadır, fakat sözcük her kaynakta aynı koşulları taşımaz; gençlik, güzellik, evlilik ve genel kadın kullanımları ayrı sınır çeşitleridir.","branch_image_ar":"الغانية المستغنية","concept_gloss":"süsten bağımsız sayılan; bazen genç, güzel veya evli kadın","contextual_glosses":[{"applicability":"Nitelemenin kadının kendi güzelliği sayesinde süslenmeye gerek duymaması açıklamasına dayandığı bağlamda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde bağımsızlık ile yalnız gençlik, evlilik veya genel kadın kullanımını dışarıda bırakır.","preserves":"Güzellik nedeniyle süsten bağımsız sayılma yönünü açıkça korur."},"facet_ids":["F001"],"text":"güzelliğiyle süse ihtiyaç duymayan kadın","usage_role":"explanatory"},{"applicability":"Kaynak sınırının gençlik ve güzellik özelliklerine dayandığı kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş veya güzellik sayesinde süsten bağımsız olma açıklamasını ve genel kadın kullanımını vermez.","preserves":"Gençlik ve güzellik temelli kaynak çeşidini korur."},"facet_ids":["F002"],"text":"genç ve güzel kadın","usage_role":"contextual"},{"applicability":"Nitelemenin yalnızca evlilik durumuna göre sınırlandığı kaynak kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güzellik, gençlik, süsten bağımsızlık ve evli olmayan kadın kullanımlarını dışarıda bırakır.","preserves":"Evlilik koşuluna dayanan dar kaynak çeşidini korur."},"facet_ids":["F002"],"text":"evli kadın","usage_role":"contextual"}],"definition":"Eşi sayesinde takıya gerek duymadığı veya güzelliği nedeniyle süslenmeye ihtiyaç duymadığı düşünülen kadını anlatan bir nitelemedir. Kullanım sınırı bazı kaynaklarda genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın olacak kadar genişler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, eşi veya kendi güzelliği sayesinde takı ve süslenmeye ihtiyaç duymayan biri olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Nitelemenin sınırı gençlik, güzellik veya evlilik koşullarından yalnızca birine dayanabilir."},{"facet_id":"F003","role":"source_variant","statement":"En geniş kaynak kullanımında niteleme belirli bir koşul aranmadan genel olarak kadına uygulanabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eş sayesinde süsten bağımsızlık, evlilik, gençlik ve koşulsuz kadın kullanımlarını dışarıda bırakır.","preserves":"Güzellik özelliğine dayanan kullanımı korur."},"text":"güzel kadın"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evli olmayan güzel kadın, süsten bağımsız kadın ve genel kadın kullanımlarını kapsamaz.","preserves":"Gençlik ile evliliği birlikte arayan dar kaynak çeşidini korur."},"text":"evli genç kadın"}],"identity_rationale":"Kaynak sözü, eşi veya güzelliği sayesinde takı ve süslenmeye ihtiyaç duymadığı düşünülen kadın açıklamasını güçlü biçimde destekler; ancak bütün tanımlar bu sınırı korumaz. Bazı kullanımlar genç evli kadın, güzel genç kadın, evli olsun olmasın güzel kadın, hatta genel olarak kadın düzeyine kadar genişler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar"}],"lexicalization_note":"Tanım yalın kadın nitelemesine bağlıdır; eşi, güzelliği, gençliği veya evliliği anlatan sınır çeşitleri korunur ve başka dallardaki evlenme olayına dönüştürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ihtiyaçsızlık, genç ve güzel kadın, süs eşyası ve evlilik durumu ile sınırı gösteren dört aday seçildi, yalnızca aynı toplumsal sahneyi paylaşan daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli ve sınırları değişken bir kadın adıdır; komşu dal ise cinsiyet veya niteleme sınırlaması olmadan zenginlik ve ihtiyaçsızlık durumunu anlatır.","focus_only":"Belirli bir kadın nitelemesi ve bunun gençlik, güzellik veya evlilik sınırları odak dala özgüdür.","gloss":"kadın nitelemesi ve genel ihtiyaçsızlık","neighbor_only":"Genel maddi bolluk, mal çokluğu ve herhangi bir kişinin ihtiyaçtan bağımsızlığı komşu dalın kapsamıdır.","neighbor_ref":"root_001110/B001","relation_type":"near_neighbor","shared_zone":"Kadının eşi veya güzelliği sayesinde süse ihtiyaç duymadığı açıklaması, ihtiyaçtan bağımsızlık düşüncesiyle kesişir."},{"boundary_match":"partial","distinction":"Odak dalın ana açıklaması eş veya güzellik sayesinde süsten bağımsızlıktır ve sınırı değişkendir; komşu dal doğrudan gençlik ve güzelliği bildirir.","focus_only":"Eş veya güzellik sayesinde süse ihtiyaç duymama ve evlilik sınırı odakta bulunabilir.","gloss":"süsten bağımsız kadın ve genç güzel kız","neighbor_only":"Genç ve güzel kız olma, başka bir gerekçe aranmadan komşu dalın doğrudan çekirdeğidir.","neighbor_ref":"root_000610/B008","relation_type":"near_neighbor","shared_zone":"İki dal da genç ve güzel bir kadını nitelemek için kullanılabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal bir kadını süse gerek duymama veya başka özelliklerle niteler; komşu dal ise süs eşyasını ve süslenme eylemini anlatır.","focus_only":"Süse ihtiyaç duymadığı düşünülen kadının kendisi odak dalda adlandırılır.","gloss":"süsten bağımsız kadın ve süs eşyası","neighbor_only":"Takı ve süs eşyasının kendisi ile bunları takma eylemi komşu dalda adlandırılır.","neighbor_ref":"root_000353/B001","relation_type":"thematic","shared_zone":"Her iki dal kadın, takı ve süslenme durumunun aynı sahnesinde yer alır."},{"boundary_match":"field_only","distinction":"Odakta evlilik yalnızca değişken sınırlardan biridir; komşu dal ise önceki evlilik veya birleşme sonrasındaki medeni durumu doğrudan tanımlar.","focus_only":"Güzellik, gençlik veya eş sayesinde süsten bağımsızlıkla kurulan kadın nitelemesi odakta yer alır.","gloss":"kadın nitelemesi ve önceki evlilik durumu","neighbor_only":"Evlilik ilişkisinin sona ermesi ya da evlilikte cinsel birleşme sonrası kazanılan durum komşuya özgüdür.","neighbor_ref":"root_000209/B005","relation_type":"same_field","shared_zone":"Her iki dal bir kadını evlilik durumu üzerinden niteleyebilir."}],"source_phrase_ar":"الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)","source_summary":"Kaynaklar kadın nitelemesinde birleşir, fakat sınırı farklı kurar: eşi veya güzelliği nedeniyle süse ihtiyaç duymama ana açıklamadır; gençlik, güzellik, evlilik ve koşulsuz kadın kullanımları daha geniş çeşitlerdir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الغانية والغواني على اختلاف تفسيرها بالمتزوجة أو الشابة أو الحسناء أو من استغنت بزوجها أو حسنها عن الزينة","what_is_not_ar":"ليس الغناء بالصوت ولا مطلق الغنى في المال ولا التزويج نفسه"},"support_links":[]},{"boundary":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_kind":"bare","branch_ref":"root_001110/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","surface_ar":"ٱسْتَغْنَىٰ"}],"gloss":"evlenme ve evlendirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}}],"root_ar":"غ ن ي","root_id":"root_001110","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evlilik bağının kurulmasını hem kişinin kendisi hem de bir başkasını evlendiren katılımcı açısından kapsar.","boundary_detail":"Dal evlilik bağı kurma ve birini evlendirme olayına aittir; evliliğin koruyucu sayılması buna bağlı bir değerlendirmedir.","branch_image_ar":"الغنى والتزويج","concept_gloss":"evlenme ve evlendirme","contextual_glosses":[{"applicability":"Kişinin evlenmesi veya evlilik durumuna girmesi anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir başkasını evlendirme ve evliliği koruyucu sayma yönlerini dışarıda bırakır.","preserves":"Kişinin evlenmesi ve evlilik bağının kurulması yönünü korur."},"facet_ids":["F001"],"text":"evlilik bağı kurmak","usage_role":"contextual"},{"applicability":"Ettirgen kullanımda bir gelin için evlilik bağı kurulması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi evlenmesini ve evliliğin koruyucu sayılmasını kapsamaz.","preserves":"Bir başkasını, özellikle gelini, evlendirme yönünü korur."},"facet_ids":["F002"],"text":"bir gelini evlendirmek","usage_role":"contextual"}],"definition":"Evlilik bağı kurma veya birini, özellikle bir gelini, evlendirme anlamıdır. Evlilik ayrıca bekâr kişiyi koruyan bir güvence olarak tasarlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi evlilik bağı kurar veya evlilik durumu adlandırılır."},{"facet_id":"F002","role":"core","statement":"Ettirgen kullanımda bir başkası, özellikle bir gelin, evlendirilir."},{"facet_id":"F003","role":"associated_use","statement":"Evlilik, bekâr kişi için koruma sağlayan bir güvence olarak değerlendirilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kutlama ve tören olayını zorunluymuş gibi öne çıkarır.","collision":"Evlilik bağı ile düğün törenini birbirine karıştırır.","fit":"displacement","loses":"Evlilik bağını kurma ve birini evlendirme işlemlerini hukuki ve ilişkisel yönleriyle vermez.","preserves":"Evlilik çevresindeki toplumsal olaya gönderme yapar."},"text":"düğün"}],"identity_rationale":"Kaynak sözü evlenmeyi, gelinleri evlendirmeyi ve evliliğin bekâr kişi için koruyucu bir durum sayılmasını aynı dalda açıkça verir. Kadın nitelemesi, maddi zenginlik ve sesle ezgi anlamları bu çekirdeğin parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"evlenme; bekâr kişi için koruyucu sayılan evlilik"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gelinleri evlendirme"}],"lexicalization_note":"Tanım yalın ad ve ettirgen biçimlerin evlenme ile evlendirme anlamlarını kapsar; düğün töreni, eşin kendisi veya evliliğin sonraki aşamaları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; evlilik sözleşmesi, eş edinme, birlikte yaşama aşaması, örtülü evlilik anlatımı ve kadın nitelemesiyle sınırı gösteren beş aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal evlenme ile başkasını evlendirmeyi birlikte kapsar; komşu dal özellikle evlilik sözleşmesini ve bu sözleşmeyle evlenmeyi öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği bekâr için koruyucu sayma yönleri odakta bulunur.","gloss":"evlenme ve evlilik sözleşmesi","neighbor_only":"Evlilik sözleşmesinin kendisini doğrudan adlandırma komşu dalda daha belirgindir.","neighbor_ref":"root_001548/B002","relation_type":"near_synonym","shared_zone":"Her iki dal evlilik bağının kurulmasını ve kişinin evlenmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal evlilik bağını kurma ve kurdurma olayını anlatır; komşu dal eş ve aile edinme sonucunu öne çıkarır.","focus_only":"Bir gelini evlendirme ve evliliği koruyucu bir güvence sayma odak dala özgüdür.","gloss":"evlenme ve eş edinme","neighbor_only":"Eş edinerek aile sahibi olma ve kişiye bir eş verilmesi komşu dalda daha belirgindir.","neighbor_ref":"root_000064/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin evlenerek bir eş ve aile bağı edinmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal bağın kurulmasını anlatır; komşu dal ise kurulmuş evliliğin ardından eşlerin bir araya gelmesi ve ortak yaşama geçmesi aşamasına yönelir.","focus_only":"Evlilik bağını kurma ve bir başkasını evlendirme odak dalın çekirdeğidir.","gloss":"evlenme ve eşlerin birleşmesi","neighbor_only":"Evliliğin ardından eşlerin birlikte yaşamaya başlaması ve gelinin eve getirilmesi komşuya özgüdür.","neighbor_ref":"root_000156/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal evlilik sürecinin birbirine yakın aşamalarında yer alır."},{"boundary_match":"partial","distinction":"Odak dal doğrudan evlenme ve evlendirme anlamındadır; komşu dal örtülü bir anlatımla evlilikten cinsel birleşmeye kadar genişleyebilir.","focus_only":"Bir başkasını evlendirme ve koruyucu evlilik düşüncesi odak dalda açıkça yer alır.","gloss":"evlilik bağı ve evlilik için örtülü anlatım","neighbor_only":"Evlilik yanında cinsel birleşmeye kadar uzanan örtülü kullanım komşu dalın ek kapsamıdır.","neighbor_ref":"root_000161/B005","relation_type":"near_neighbor","shared_zone":"İki dal da evlenme anlamını veya evliliğe gönderme yapan bir kullanımı kapsar."},{"boundary_match":"field_only","distinction":"Odak dal bir olay ve ilişki kurma sürecidir; komşu dal ise evli olabilen veya başka özelliklerle tanımlanan bir kadın adıdır.","focus_only":"Evlilik bağını kurma veya birini evlendirme olayı odak dala özgüdür.","gloss":"evlenme olayı ve kadın nitelemesi","neighbor_only":"Evlilik, güzellik veya gençlik üzerinden tanımlanan kadın nitelemesi komşu dala özgüdür.","neighbor_ref":"root_001110/B005","relation_type":"same_field","shared_zone":"Her iki dal evlilik ve kadınla ilgili aynı toplumsal alan içinde yer alabilir."}],"source_phrase_ar":"الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynaklı kullanım, evlenmeyi ve gelinleri evlendirmeyi anlatır; evliliği de bekâr kişi için koruyucu bir güvence sayar."}],"source_summary":"Bu dalda ad ve ettirgen biçim, evlilik bağı kurma çevresinde birleşir; koruma düşüncesi evlenmenin sonucu olarak sunulur.","sources":["TA"],"what_is_ar":"يدخل فيه الغنى بمعنى التزويج والأغناء بمعنى إملاكات العرائس وجعل التزويج حصنا للعزب","what_is_not_ar":"ليس الغانية نفسها ولا الغناء بالصوت ولا الغنى في المال"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:8:1"],"branch_refs":[],"candidate_id":"cand_e9c19fa4d6266f07194d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:1:contrastive-reset","source_type":"word_analysis","support_ids":["sup_82b411f4ea6c901a4396","sup_90eee1e81c0e93fed593"],"title":"joined counter-case after a completed branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:1","qac_refs":["92:8:1:1"],"status":"accepted"}},{"anchor_refs":["92:8:1"],"branch_refs":[],"candidate_id":"cand_1929f577d4310674a5cc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:1:light-form-heavy-task","source_type":"word_analysis","support_ids":["sup_49d998dd3bb67f9f97d9","sup_82b411f4ea6c901a4396"],"title":"single-letter pivot into the frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:1","qac_refs":["92:8:1:1"],"status":"accepted"}},{"anchor_refs":["92:8:1"],"branch_refs":[],"candidate_id":"cand_7f303518d8a2222e281b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:1:local-wa-range","source_type":"word_analysis","support_ids":["sup_82b411f4ea6c901a4396","sup_bce30f8d314fc81c49f7"],"title":"broad connective range narrowed to contrastive joining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:1","qac_refs":["92:8:1:1"],"status":"accepted"}},{"anchor_refs":["92:8:2"],"branch_refs":[],"candidate_id":"cand_1964767a1915d9a58779","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:2:deferred-answer","source_type":"word_analysis","support_ids":["sup_0f322cd87dc9243a4cda","sup_1ce661bc5df2efabe9a3"],"title":"case opened now, answer delayed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:2","qac_refs":["92:8:1:2"],"status":"accepted"}},{"anchor_refs":["92:8:2"],"branch_refs":[],"candidate_id":"cand_e53fa9680621bf2efcb5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:2:marked-sound-frame","source_type":"word_analysis","support_ids":["sup_063e5204e0d1f8cec34e","sup_1ce661bc5df2efabe9a3"],"title":"geminated frame has audible weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:2","qac_refs":["92:8:1:2"],"status":"accepted"}},{"anchor_refs":["92:8:2"],"branch_refs":[],"candidate_id":"cand_5fc126d2a8eb4ecb7b0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:2:paired-amma-frame","source_type":"word_analysis","support_ids":["sup_0886713d177968eaa30f","sup_1ce661bc5df2efabe9a3"],"title":"second detailing frame mirrors the first","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:2","qac_refs":["92:8:1:2"],"status":"accepted"}},{"anchor_refs":["92:8:2"],"branch_refs":[],"candidate_id":"cand_d486ba9600d7760c8477","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:2:whole-man-topic","source_type":"word_analysis","support_ids":["sup_1ce661bc5df2efabe9a3","sup_c1f16c05834b24d7651e"],"title":"behavior-defined topic under the particle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:2","qac_refs":["92:8:1:2"],"status":"accepted"}},{"anchor_refs":["92:8:3"],"branch_refs":[],"candidate_id":"cand_043067820c26f299da77","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:3:mirrored-pronoun-slot","source_type":"word_analysis","support_ids":["sup_66acc7c4fa3c4958b62d","sup_cd5d84db1ca283b725c9"],"title":"same subject slot as the positive branch","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:3","qac_refs":["92:8:2:1"],"status":"accepted"}},{"anchor_refs":["92:8:3"],"branch_refs":[],"candidate_id":"cand_45bc698b8ae8a5e97907","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:3:one-subject-two-verbs","source_type":"word_analysis","support_ids":["sup_2d4494777a35a830cf2e","sup_66acc7c4fa3c4958b62d"],"title":"one pronoun controls both predicates","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:3","qac_refs":["92:8:2:1"],"status":"accepted"}},{"anchor_refs":["92:8:3"],"branch_refs":[],"candidate_id":"cand_7025ba8ffa186cfa4b62","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:3:open-behavior-class","source_type":"word_analysis","support_ids":["sup_66acc7c4fa3c4958b62d","sup_abec7b5f6c525110d4b3"],"title":"whoever is defined by the verbs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:3","qac_refs":["92:8:2:1"],"status":"accepted"}},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_6345a03d8f160222cc27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:4:contraction-image","source_type":"word_analysis","support_ids":["sup_76970c30b353fe45386b","sup_77af8a1cd2dfa8bbea74"],"title":"moral withholding feels like contraction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:4","qac_refs":["92:8:3:1"],"status":"accepted"}},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_ab1b23a6b9e4e45b471a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:4:direct-form-i-agency","source_type":"word_analysis","support_ids":["sup_77af8a1cd2dfa8bbea74","sup_92524d4e1a19aab42c34"],"title":"direct active characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:4","qac_refs":["92:8:3:1"],"status":"accepted"}},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_70b078b8e17601f82295","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:4:mirror-of-giving","source_type":"word_analysis","support_ids":["sup_77af8a1cd2dfa8bbea74","sup_940e8eaa9d7b09e448ae"],"title":"first negative verb reverses giving","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:4","qac_refs":["92:8:3:1"],"status":"accepted"}},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_5b2ee00fb164fe0574b1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:4:objectless-withholding","source_type":"word_analysis","support_ids":["sup_69e7b06c732bf9331351","sup_77af8a1cd2dfa8bbea74"],"title":"withholding left without a specified object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:4","qac_refs":["92:8:3:1"],"status":"accepted"}},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_74faad14ac6f83c3426c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:4:paired-with-self-sufficiency","source_type":"word_analysis","support_ids":["sup_516844d36b7771e40bfc","sup_77af8a1cd2dfa8bbea74"],"title":"withholding paired with claimed sufficiency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:4","qac_refs":["92:8:3:1"],"status":"accepted"}},{"anchor_refs":["92:8:5"],"branch_refs":[],"candidate_id":"cand_58e58f0e97224e53ad38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:5:audible-hinge","source_type":"word_analysis","support_ids":["sup_74ca7c5876499f592605","sup_987611896c3bebc3c682"],"title":"small hinge between heavy verbs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:5","qac_refs":["92:8:4:1"],"status":"accepted"}},{"anchor_refs":["92:8:5"],"branch_refs":[],"candidate_id":"cand_f6b613b0dd4c910b3948","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:5:coordinated-two-predicates","source_type":"word_analysis","support_ids":["sup_5493bbbdcee4fe2644cd","sup_987611896c3bebc3c682"],"title":"two predicates, one subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:5","qac_refs":["92:8:4:1"],"status":"accepted"}},{"anchor_refs":["92:8:5"],"branch_refs":[],"candidate_id":"cand_5828102f5e295c1eb454","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:8:5:mirrored-wa-slot","source_type":"word_analysis","support_ids":["sup_962c9d5b7b6570bb2bec","sup_987611896c3bebc3c682"],"title":"same connective slot as the positive pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:5","qac_refs":["92:8:4:1"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_2c1f8563369c0c7474be","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:divine-sufficiency-contrast","source_type":"word_analysis","support_ids":["sup_460c70508b17bcf007f2","sup_f0a2569b592b5ed4aed8"],"title":"human claim set against true sufficiency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_b7c73b2e74a88c1e25cd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:form-x-self-claim","source_type":"word_analysis","support_ids":["sup_d4526f9b7df1c775050d","sup_f0a2569b592b5ed4aed8"],"title":"Form X makes sufficiency self-attributed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_63a7afaa1e5d0b0caf4e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:opposes-taqwa-slot","source_type":"word_analysis","support_ids":["sup_d2fba574fbee7ff621e9","sup_f0a2569b592b5ed4aed8"],"title":"second slot reverses guarded dependence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_0e18027d3d7085767ebb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:same-root-availing-reversal","source_type":"word_analysis","support_ids":["sup_41e872bd7278b8062f9a","sup_f0a2569b592b5ed4aed8"],"title":"self-sufficiency tested by non-availing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_d5a8e9b613a31e8293d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:same-subject-closure","source_type":"word_analysis","support_ids":["sup_9b1d2ca5bd28b2b9f991","sup_f0a2569b592b5ed4aed8"],"title":"second verb closes the two-part subject profile","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_d9843b37f7b4ca2b0923","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:self-seeing-echo","source_type":"word_analysis","support_ids":["sup_70257f45e0497cc69399","sup_f0a2569b592b5ed4aed8"],"title":"same Form X diagnosis at 96:7","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_5e2a3429f079b372677a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:sound-and-boundary","source_type":"word_analysis","support_ids":["sup_103930e63bbf060df237","sup_f0a2569b592b5ed4aed8"],"title":"heavy cluster opens into final long vowel","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:6"],"branch_refs":[],"candidate_id":"cand_5407b320190c316ba3f9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:6:unexpressed-source","source_type":"word_analysis","support_ids":["sup_c586f23cd3b74640de00","sup_f0a2569b592b5ed4aed8"],"title":"needlessness left open-ended","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:8:6","qac_refs":["92:8:4:2"],"status":"accepted"}},{"anchor_refs":["92:8:3"],"branch_refs":[],"candidate_id":"cand_78484d219a0e31cf6d25","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000089"],"scope":"focus_ayah","source_local_id":"92:8:3:1","source_type":"qac_morpheme","support_ids":["sup_ceca1619a8677596fbd9"],"title":"QAC root occurrence: ب خ ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:8:4"],"branch_refs":[],"candidate_id":"cand_92d610dab28b2a54a24b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001110"],"scope":"focus_ayah","source_local_id":"92:8:4:2","source_type":"qac_morpheme","support_ids":["sup_b9eb7e436def3260c336"],"title":"QAC root occurrence: غ ن ي","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:8","branch_refs":["root_000089/B001","root_001110/B001"],"candidate_id":"cand_16172ceae129d4efa609","commentary_obligation":"review","hft_ref":"hft_a5d9ee3496db194d7842","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_closed_autonomy","source_type":"hft","support_ids":["sup_0542e0121dd688297e66"],"title":"base_closed_autonomy","trust":"legacy_unbound"},{"anchor_refs":["92:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:8","branch_refs":["root_000089/B001","root_001110/B002"],"candidate_id":"cand_638de22cc4d95fd5b7f7","commentary_obligation":"review","hft_ref":"hft_228f305c927778997296","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_retained_proxy","source_type":"hft","support_ids":["sup_ab3f358f8b44e4a47975"],"title":"base_retained_proxy","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:8:1:1","qac_word_ref":"92:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"92:8:1:2","qac_word_ref":"92:8:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"92:8:2:1","qac_word_ref":"92:8:2","root_ar":"","surface_ar":"مَنۢ"},{"lemma_ar":"بَخِلَ","morph_features":"STEM|POS:V|PERF|LEM:baxila|ROOT:bxl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:3:1","qac_word_ref":"92:8:3","root_ar":"ب خ ل","surface_ar":"بَخِلَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:8:4:1","qac_word_ref":"92:8:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","root_ar":"غ ن ي","surface_ar":"ٱسْتَغْنَىٰ"}],"word_analysis_qac_refs":[["92:8:1:1"],["92:8:1:2"],["92:8:2:1"],["92:8:3:1"],["92:8:4:1"],["92:8:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:8:1","92:8:2","92:8:3","92:8:4","92:8:5","92:8:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:8:1:1","qac_word_ref":"92:8:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَمَّا","morph_features":"STEM|POS:EXL|LEM:>am~aA","morpheme_role":"STEM","pos":"EXL","qac_ref":"92:8:1:2","qac_word_ref":"92:8:1","root_ar":"","surface_ar":"أَمَّا"},{"lemma_ar":"مَن","morph_features":"STEM|POS:COND|LEM:man","morpheme_role":"STEM","pos":"COND","qac_ref":"92:8:2:1","qac_word_ref":"92:8:2","root_ar":"","surface_ar":"مَنۢ"},{"lemma_ar":"بَخِلَ","morph_features":"STEM|POS:V|PERF|LEM:baxila|ROOT:bxl|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:3:1","qac_word_ref":"92:8:3","root_ar":"ب خ ل","surface_ar":"بَخِلَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:8:4:1","qac_word_ref":"92:8:4","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"ٱسْتَغْنَىٰ","morph_features":"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:8:4:2","qac_word_ref":"92:8:4","root_ar":"غ ن ي","surface_ar":"ٱسْتَغْنَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:8:1:1"],["92:8:1:2"],["92:8:2:1"],["92:8:3:1"],["92:8:4:1"],["92:8:4:2"]],"word_analysis_refs":["92:8:1","92:8:2","92:8:3","92:8:4","92:8:5","92:8:6"],"word_rows":[{"analysis_record_ref":"92:8:1","analytic_gloss_range_en":"opening conjunction linking the new counter-case to the completed prior branch","analytic_root_gloss_range_en":null,"qac_refs":["92:8:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:8:2","analytic_gloss_range_en":"conditional detailing particle that specifies a case and defers its answer","analytic_root_gloss_range_en":null,"qac_refs":["92:8:1:2"],"root":{},"surface":{"arabic":"أَمَّا","transliteration":"ammā"}},{"analysis_record_ref":"92:8:3","analytic_gloss_range_en":"generic relative pronoun, whoever, whose identity is supplied by the following predicates","analytic_root_gloss_range_en":null,"qac_refs":["92:8:2:1"],"root":{},"surface":{"arabic":"مَنْ","transliteration":"man"}},{"analysis_record_ref":"92:8:4","analytic_gloss_range_en":"withheld or acted stingily, locally objectless and active as the first defining predicate","analytic_root_gloss_range_en":"stingy withholding, refusal to release what should circulate, and the image of contraction; local grammar does not specify one withheld object","qac_refs":["92:8:3:1"],"root":{"arabic":"ب خ ل","transliteration":"b-kh-l"},"surface":{"arabic":"بَخِلَ","transliteration":"bakhila"}},{"analysis_record_ref":"92:8:5","analytic_gloss_range_en":"internal conjunction coordinating the two perfect predicates under one subject","analytic_root_gloss_range_en":null,"qac_refs":["92:8:4:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:8:6","analytic_gloss_range_en":"Form X perfect active self-sufficiency claim, locally without an expressed source or complement","analytic_root_gloss_range_en":"sufficiency, wealth, independence, availing, song, dwelling, marriage-related sufficiency, and disputed woman-description branches; the local Form X selects claimed needlessness, while availing remains active as a later same-root test","qac_refs":["92:8:4:2"],"root":{"arabic":"غ ن ي","transliteration":"gh-n-y"},"surface":{"arabic":"ٱسْتَغْنَىٰ","transliteration":"istaghnā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":2,"assigned_records":[{"anchor_refs":["92:8"],"branch_refs":["root_000089/B001","root_001110/B001"],"candidate_id":"cand_16172ceae129d4efa609","evidence_scope":"focus_ayah","hft_ref":"hft_a5d9ee3496db194d7842","item_id":"base_closed_autonomy","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_closed_autonomy","support_id":"sup_0542e0121dd688297e66"},{"anchor_refs":["92:8"],"branch_refs":["root_000089/B001","root_001110/B002"],"candidate_id":"cand_638de22cc4d95fd5b7f7","evidence_scope":"focus_ayah","hft_ref":"hft_228f305c927778997296","item_id":"base_retained_proxy","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_retained_proxy","support_id":"sup_ab3f358f8b44e4a47975"}],"diagnostics":[],"lane_counts":{"global":15,"macro":7,"micro":2},"packet_summary":{"ayah_count":21,"focus_ref":"92:8","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:8","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"92:8","lane":"micro","linguistic_source_ref":"92:8","surface_ref":"92:8","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:8","target_tokens":[["Ama",["92:8:1"]],["kim",["92:8:2"]],["cimrilik",["92:8:3"]],["eder",["92:8:3"]],["ve",["92:8:4"]],["kendini",["92:8:4"]],["yeterli",["92:8:4"]],["sayarsa",["92:8:2","92:8:4"]]],"text":"Ama kim cimrilik eder ve kendini yeterli sayarsa,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":2,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:2:marked-sound-frame","source_type":"word_analysis","support_id":"sup_063e5204e0d1f8cec34e","text":"{\"blocking_evidence\":null,\"headline\":\"geminated frame has audible weight\",\"reader_payoff\":\"The reader hears the entry into the counter-case as a marked and weighty frame rather than a light topic shift.\",\"reason\":\"The surface form contains the doubled consonantal shape of {{ar:أَمَّا}} ({{tr:ammā}}), matching its grammatical load.\",\"representative_source_ids\":[\"QF-562d8cff\",\"QP-fad52c8a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:2:paired-amma-frame","source_type":"word_analysis","support_id":"sup_0886713d177968eaa30f","text":"{\"blocking_evidence\":null,\"headline\":\"second detailing frame mirrors the first\",\"reader_payoff\":\"The reader sees the counter-case arranged in the same kind of frame as the positive case in 92:5.\",\"reason\":\"The particle follows the opening conjunction and introduces the second protasis corresponding to the earlier {{ar:فَأَمَّا}} ({{tr:fa-ammā}}) frame in 92:5.\",\"representative_source_ids\":[\"QT-8de838f0\",\"QT-f0b036cd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:2:deferred-answer","source_type":"word_analysis","support_id":"sup_0f322cd87dc9243a4cda","text":"{\"blocking_evidence\":null,\"headline\":\"case opened now, answer delayed\",\"reader_payoff\":\"The reader notices that 92:8 is syntactically suspended and must be read through the answer in 92:10.\",\"reason\":\"QAC tags {{ar:أَمَّا}} ({{tr:ammā}}) as a conditional detailing particle, and translation support states that the structure is completed by the later answer in 92:10.\",\"representative_source_ids\":[\"QG-865ba432\",\"QG-bb666f58\",\"QY-7b48195d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:sound-and-boundary","source_type":"word_analysis","support_id":"sup_103930e63bbf060df237","text":"{\"blocking_evidence\":null,\"headline\":\"heavy cluster opens into final long vowel\",\"reader_payoff\":\"The reader hears the claim as both constricted in its consonants and expansive at the ayah boundary.\",\"reason\":\"The surface form contains the heavy {{tr:st-gh-n}} cluster and ends with the long open final {{tr:ā}}.\",\"representative_source_ids\":[\"QF-e72a062f\",\"QP-d9013f31\",\"QY-443ef5ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:2","source_type":"word_analysis","support_id":"sup_1ce661bc5df2efabe9a3","text":"{\"gloss_range\":\"conditional detailing particle that specifies a case and defers its answer\",\"prose\":\"{{ar:أَمَّا}} ({{tr:ammā}}) is the heavy detailing particle, with its doubled mim, that turns the following {{ar:مَنْ}} ({{tr:man}}) clause into a specified case. It does not finish the sentence inside 92:8: the expected answer is delayed until 92:10, so the listener must hold the human profile before hearing the consequence. The same particle slot mirrors the earlier positive block in 92:5, making this a paired taxonomy rather than a disconnected warning.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَمَّا}} ({{tr:ammā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:3:one-subject-two-verbs","source_type":"word_analysis","support_id":"sup_2d4494777a35a830cf2e","text":"{\"blocking_evidence\":null,\"headline\":\"one pronoun controls both predicates\",\"reader_payoff\":\"The reader sees withholding and self-sufficiency as a combined profile of one subject, not as separable cases.\",\"reason\":\"Attachment evidence makes {{ar:مَنْ}} ({{tr:man}}) the subject of {{ar:بَخِلَ}} ({{tr:bakhila}}), while the second verb shares that subject through coordinated agreement.\",\"representative_source_ids\":[\"QG-5567529a\",\"QG-98cd4e85\",\"QG-a12901e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:same-root-availing-reversal","source_type":"word_analysis","support_id":"sup_41e872bd7278b8062f9a","text":"{\"blocking_evidence\":null,\"headline\":\"self-sufficiency tested by non-availing\",\"reader_payoff\":\"The reader notices that the root's claim of sufficiency in 92:8 is answered from the same root by failure to avail in 92:11.\",\"reason\":\"V4 includes an availing branch for {{ar:غ ن ي}} ({{tr:gh-n-y}}), and the CRITICAL rows give the concrete same-surah reversal at 92:11.\",\"representative_source_ids\":[\"QI-8b38c97e\",\"QE-f7682da4\",\"ME-b918f405\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:divine-sufficiency-contrast","source_type":"word_analysis","support_id":"sup_460c70508b17bcf007f2","text":"{\"blocking_evidence\":null,\"headline\":\"human claim set against true sufficiency\",\"reader_payoff\":\"The reader senses the irony of a human Form X claim touching a quality that belongs truly and securely to {{ar:ٱلْغَنِيّ}} ({{tr:al-Ghaniyy}}), while the local word remains the human verb.\",\"reason\":\"The root field includes true sufficiency language, but the local surface is a human Form X verb, so the contrast is evaluative rather than a claim that the divine name is locally present.\",\"representative_source_ids\":[\"QS-1838d5ee\",\"MS-207e3308\",\"QY-5bf99a37\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:1:light-form-heavy-task","source_type":"word_analysis","support_id":"sup_49d998dd3bb67f9f97d9","text":"{\"blocking_evidence\":null,\"headline\":\"single-letter pivot into the frame\",\"reader_payoff\":\"The reader hears and sees a very light particle carrying the pivot into a weightier counter-case frame.\",\"reason\":\"The written word is the one-letter conjunction immediately before the marked detailing particle.\",\"representative_source_ids\":[\"QF-43720b08\",\"QP-483888b4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4:paired-with-self-sufficiency","source_type":"word_analysis","support_id":"sup_516844d36b7771e40bfc","text":"{\"blocking_evidence\":null,\"headline\":\"withholding paired with claimed sufficiency\",\"reader_payoff\":\"The reader sees outward non-circulation joined to inward needlessness as one profile.\",\"reason\":\"Attachment evidence coordinates {{ar:بَخِلَ}} ({{tr:bakhila}}) with {{ar:ٱسْتَغْنَىٰ}} ({{tr:istaghnā}}), and contextual collocation notes the local pairing with {{ar:غ ن ي}} ({{tr:gh-n-y}}).\",\"representative_source_ids\":[\"QG-7d332596\",\"QI-42ee5427\",\"QE-ae332730\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:5:coordinated-two-predicates","source_type":"word_analysis","support_id":"sup_5493bbbdcee4fe2644cd","text":"{\"blocking_evidence\":null,\"headline\":\"two predicates, one subject\",\"reader_payoff\":\"The reader notices that outward withholding and inward self-sufficiency jointly define one person.\",\"reason\":\"QAC tags the word as a conjunction, and attachment evidence coordinates {{ar:ٱسْتَغْنَىٰ}} ({{tr:istaghnā}}) with {{ar:بَخِلَ}} ({{tr:bakhila}}) under the same subject.\",\"representative_source_ids\":[\"QG-4a6c35e7\",\"QG-4a92fee6\",\"QS-156a612d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:3","source_type":"word_analysis","support_id":"sup_66acc7c4fa3c4958b62d","text":"{\"gloss_range\":\"generic relative pronoun, whoever, whose identity is supplied by the following predicates\",\"prose\":\"{{ar:مَنْ}} ({{tr:man}}) leaves the person unnamed and open: whoever fits the following description enters the case. Its compact singular grammar controls both perfect verbs, so withholding and claimed sufficiency describe one subject rather than two examples. Because this pronoun occupies the same slot as the earlier {{ar:مَنْ}} ({{tr:man}}) in 92:5, the contrast falls on the verbs that follow, not on different kinds of people.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَنْ}} ({{tr:man}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4:objectless-withholding","source_type":"word_analysis","support_id":"sup_69e7b06c732bf9331351","text":"{\"blocking_evidence\":null,\"headline\":\"withholding left without a specified object\",\"reader_payoff\":\"The reader notices that the ayah diagnoses a broad refusal to let what is due circulate, not only a named act of not spending money.\",\"reason\":\"The local verb instance has no object or prepositional complement, while V4 supports the accepted withholding branch for {{ar:ب خ ل}} ({{tr:b-kh-l}}).\",\"representative_source_ids\":[\"QG-83b3f3f9\",\"QS-11f267a7\",\"QS-a81cb0fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:self-seeing-echo","source_type":"word_analysis","support_id":"sup_70257f45e0497cc69399","text":"{\"blocking_evidence\":null,\"headline\":\"same Form X diagnosis at 96:7\",\"reader_payoff\":\"The reader recognizes the self-sufficiency language as a diagnosis of human self-assessment, clarified by the same theme in 96:7.\",\"reason\":\"The CRITICAL rows cite 96:7 as a same-form self-sufficiency parallel, and contextual supplement samples include 96:7 for the Form X profile.\",\"representative_source_ids\":[\"QI-c865c086\",\"MI-68386d16\",\"QH-4f2165de\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:5:audible-hinge","source_type":"word_analysis","support_id":"sup_74ca7c5876499f592605","text":"{\"blocking_evidence\":null,\"headline\":\"small hinge between heavy verbs\",\"reader_payoff\":\"The reader hears the pair as linked but still separated into two analyzable acts.\",\"reason\":\"The short written conjunction stands between the two heavier verbal surfaces.\",\"representative_source_ids\":[\"QP-3a1123b1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4:contraction-image","source_type":"word_analysis","support_id":"sup_76970c30b353fe45386b","text":"{\"blocking_evidence\":null,\"headline\":\"moral withholding feels like contraction\",\"reader_payoff\":\"The reader feels the act as self-enclosed tightening of hand, chest, and circulation rather than as a flat legal label.\",\"reason\":\"The accepted root branch centers stingy withholding, and the sound row is locally anchored in the {{ar:خ}} ({{tr:kh}}) of the surface word.\",\"representative_source_ids\":[\"QS-4d8de5cf\",\"MS-41c959dd\",\"QY-a2eb6acf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4","source_type":"word_analysis","support_id":"sup_77af8a1cd2dfa8bbea74","text":"{\"gloss_range\":\"withheld or acted stingily, locally objectless and active as the first defining predicate\",\"prose\":\"{{ar:بَخِلَ}} ({{tr:bakhila}}) is a perfect active Form I verb, so the open {{ar:مَنْ}} ({{tr:man}}) is characterized by performed withholding, not by someone else's label. No object or prepositional complement specifies what is withheld; the word therefore names a posture of blocking circulation rather than only a financial transaction. Its root image of tightening makes the moral act feel like closed hand, chest, and circulation, and its slot directly reverses the giving verb in 92:5 before the next verb adds the inward claim of sufficiency.\",\"root_display\":\"{{ar:ب خ ل}} ({{tr:b-kh-l}})\",\"root_gloss_range\":\"stingy withholding, refusal to release what should circulate, and the image of contraction; local grammar does not specify one withheld object\",\"surface_display\":\"{{ar:بَخِلَ}} ({{tr:bakhila}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:1","source_type":"word_analysis","support_id":"sup_82b411f4ea6c901a4396","text":"{\"gloss_range\":\"opening conjunction linking the new counter-case to the completed prior branch\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens 92:8 by connecting the new case to the branch that has just reached its result in 92:7. Because the next word is {{ar:أَمَّا}} ({{tr:ammā}}), the connection becomes a contrastive reset: the ayah is joined to the prior moral frame while beginning the opposite conditional arc. The one-letter form does large structural work, and its light onset gives way immediately to the heavier detailing particle.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:1:contrastive-reset","source_type":"word_analysis","support_id":"sup_90eee1e81c0e93fed593","text":"{\"blocking_evidence\":null,\"headline\":\"joined counter-case after a completed branch\",\"reader_payoff\":\"The reader sees that 92:8 is not a loose new sentence but the coordinated opposite case after the first branch has already landed in 92:7.\",\"reason\":\"QAC marks {{ar:وَ}} ({{tr:wa}}) as a conjunction, and the attachment support identifies the following {{ar:أَمَّا}} ({{tr:ammā}}) block as a contrasting conditional structure whose resolution comes later.\",\"representative_source_ids\":[\"QG-cadc4a9a\",\"QT-9ece36b1\",\"QY-6753fc46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4:direct-form-i-agency","source_type":"word_analysis","support_id":"sup_92524d4e1a19aab42c34","text":"{\"blocking_evidence\":null,\"headline\":\"direct active characterization\",\"reader_payoff\":\"The reader sees withholding as the subject's own settled act or state within the relative clause, not as an abstract noun or external accusation.\",\"reason\":\"QAC identifies a perfect active Form I verb, and the subject relation links the act to {{ar:مَنْ}} ({{tr:man}}).\",\"representative_source_ids\":[\"QG-1bcc04ae\",\"QF-ef1d604c\",\"MF-b4bf60c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:4:mirror-of-giving","source_type":"word_analysis","support_id":"sup_940e8eaa9d7b09e448ae","text":"{\"blocking_evidence\":null,\"headline\":\"first negative verb reverses giving\",\"reader_payoff\":\"The reader sees the moral binary begin at the exact verb slot: giving in 92:5 is answered by withholding in 92:8.\",\"reason\":\"The verb occupies the first predicate position after {{ar:مَنْ}} ({{tr:man}}), corresponding to the first predicate in 92:5.\",\"representative_source_ids\":[\"QS-4ec7969d\",\"MI-01656cda\",\"QT-e6f18230\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:5:mirrored-wa-slot","source_type":"word_analysis","support_id":"sup_962c9d5b7b6570bb2bec","text":"{\"blocking_evidence\":null,\"headline\":\"same connective slot as the positive pair\",\"reader_payoff\":\"The reader sees the negative verb pair laid into the same syntactic skeleton as the giving-and-guarding pair in 92:5.\",\"reason\":\"The conjunction stands between the two negative verbs in the same paired position as the internal conjunction between the two positive verbs in 92:5.\",\"representative_source_ids\":[\"QT-3edfe3a9\",\"MT-970903ba\",\"QY-d0eb0969\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:5","source_type":"word_analysis","support_id":"sup_987611896c3bebc3c682","text":"{\"gloss_range\":\"internal conjunction coordinating the two perfect predicates under one subject\",\"prose\":\"The middle {{ar:وَ}} ({{tr:wa}}) keeps {{ar:بَخِلَ}} ({{tr:bakhila}}) and {{ar:ٱسْتَغْنَىٰ}} ({{tr:istaghnā}}) as two coordinated predicates under the same {{ar:مَنْ}} ({{tr:man}}). It prevents the first verb from completing the description by itself and prevents the second from becoming a subordinate explanation. The same connective position mirrors the earlier pair in 92:5, while the brief sound hinge lets the listener hear linkage without losing the two-part shape.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:same-subject-closure","source_type":"word_analysis","support_id":"sup_9b1d2ca5bd28b2b9f991","text":"{\"blocking_evidence\":null,\"headline\":\"second verb closes the two-part subject profile\",\"reader_payoff\":\"The reader sees self-sufficiency as the second trait of the same conditional person, closing the description while the consequence remains pending.\",\"reason\":\"QAC identifies a 3ms perfect active verb, and attachment evidence states that it shares the subject of {{ar:بَخِلَ}} ({{tr:bakhila}}) through coordination.\",\"representative_source_ids\":[\"QG-13e6f7f4\",\"QG-e19a0e65\",\"QB-a0e42c83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:3:open-behavior-class","source_type":"word_analysis","support_id":"sup_abec7b5f6c525110d4b3","text":"{\"blocking_evidence\":null,\"headline\":\"whoever is defined by the verbs\",\"reader_payoff\":\"The reader notices that the ayah defines an open class by behavior rather than identifying a named group.\",\"reason\":\"QAC identifies a relative pronoun, and the cross-reference evidence treats it as the contrasting conditional-relative human topic for the predicates.\",\"representative_source_ids\":[\"QG-a2d71b72\",\"QS-cd580682\",\"QY-04b7536d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:8:4:2","source_type":"qac_morpheme","support_id":"sup_b9eb7e436def3260c336","text":"{\"lemma_ar\":\"ٱسْتَغْنَىٰ\",\"morph_features\":\"STEM|POS:V|PERF|(X)|LEM:{sotagonaY`|ROOT:gny|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:8:4:2\",\"qac_word_ref\":\"92:8:4\",\"root_ar\":\"غ ن ي\",\"surface_ar\":\"ٱسْتَغْنَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:1:local-wa-range","source_type":"word_analysis","support_id":"sup_bce30f8d314fc81c49f7","text":"{\"blocking_evidence\":null,\"headline\":\"broad connective range narrowed to contrastive joining\",\"reader_payoff\":\"The reader notices that the conjunction can carry more than neutral addition, while the local frame selects contrastive coordination rather than a separate circumstantial reading.\",\"reason\":\"The particle has a broad connective range, but here it stands before the second {{ar:أَمَّا}} ({{tr:ammā}}) frame and is best limited to coordinated antithesis.\",\"representative_source_ids\":[\"QS-4738c68d\",\"QS-49a1923f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:2:whole-man-topic","source_type":"word_analysis","support_id":"sup_c1f16c05834b24d7651e","text":"{\"blocking_evidence\":null,\"headline\":\"behavior-defined topic under the particle\",\"reader_payoff\":\"The reader sees the subject classified by the whole following verb profile, not by a name or fixed identity.\",\"reason\":\"The attachment evidence treats {{ar:مَنْ}} ({{tr:man}}) with the following predicates as the topic introduced after {{ar:أَمَّا}} ({{tr:ammā}}).\",\"representative_source_ids\":[\"QG-913eecc4\",\"QS-8c7ecb68\",\"MT-31da8893\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:unexpressed-source","source_type":"word_analysis","support_id":"sup_c586f23cd3b74640de00","text":"{\"blocking_evidence\":null,\"headline\":\"needlessness left open-ended\",\"reader_payoff\":\"The reader notices that the ayah does not restrict the claimed independence to money, people, God, or obligation alone.\",\"reason\":\"The local verb instance is intransitive with no object or prepositional source phrase, so the independence claim remains grammatically open.\",\"representative_source_ids\":[\"QG-a8f2bf05\",\"QG-bc803bc0\",\"QY-f9cffa2a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:3:mirrored-pronoun-slot","source_type":"word_analysis","support_id":"sup_cd5d84db1ca283b725c9","text":"{\"blocking_evidence\":null,\"headline\":\"same subject slot as the positive branch\",\"reader_payoff\":\"The reader sees that the two branches contrast actions inside the same pronoun frame rather than contrasting social labels.\",\"reason\":\"The pronoun follows the second {{ar:أَمَّا}} ({{tr:ammā}}) frame as the corresponding subject slot to 92:5.\",\"representative_source_ids\":[\"QT-866d5c1b\",\"MT-331d7a4c\",\"QB-5982e278\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:8:3:1","source_type":"qac_morpheme","support_id":"sup_ceca1619a8677596fbd9","text":"{\"lemma_ar\":\"بَخِلَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:baxila|ROOT:bxl|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:8:3:1\",\"qac_word_ref\":\"92:8:3\",\"root_ar\":\"ب خ ل\",\"surface_ar\":\"بَخِلَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:opposes-taqwa-slot","source_type":"word_analysis","support_id":"sup_d2fba574fbee7ff621e9","text":"{\"blocking_evidence\":null,\"headline\":\"second slot reverses guarded dependence\",\"reader_payoff\":\"The reader sees claimed needlessness as the direct counterpart to the guarded dependence named in 92:5.\",\"reason\":\"The verb stands after the internal conjunction in the same paired slot as {{ar:ٱتَّقَىٰ}} ({{tr:ittaqā}}) in 92:5.\",\"representative_source_ids\":[\"QS-6b428bc4\",\"QT-101cba39\",\"MT-41726171\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6:form-x-self-claim","source_type":"word_analysis","support_id":"sup_d4526f9b7df1c775050d","text":"{\"blocking_evidence\":null,\"headline\":\"Form X makes sufficiency self-attributed\",\"reader_payoff\":\"The reader sees the word as a reflexive estimate of sufficiency, not as a simple statement that the person truly is sufficient.\",\"reason\":\"QAC marks the local verb as Form X, and V4 supports the sufficiency and wealth branch for {{ar:غ ن ي}} ({{tr:gh-n-y}}) while the selected form presents self-attribution.\",\"representative_source_ids\":[\"QS-8355b807\",\"QF-1c1c4c39\",\"MF-f6734499\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:8:6","source_type":"word_analysis","support_id":"sup_f0a2569b592b5ed4aed8","text":"{\"gloss_range\":\"Form X perfect active self-sufficiency claim, locally without an expressed source or complement\",\"prose\":\"{{ar:ٱسْتَغْنَىٰ}} ({{tr:istaghnā}}) closes the ayah as a perfect active Form X verb tied to the same {{ar:مَنْ}} ({{tr:man}}). The form presents claimed or sought sufficiency, not proven possession of true independence; against divine self-sufficiency language, the human Form X wording remains a self-claim. No complement says from whom or from what the subject considers himself free, so money, people, God, and obligation all remain in view without being singled out. That open-ended self-claim answers the guarded-dependence verb in 92:5: dependence and guardedness are opposed by asserted needlessness. The same root will be tested in 92:11, where what the person has does not avail, and 96:7 sharpens the diagnosis as self-seeing sufficiency. The dense consonant cluster sounds constricted before the final long vowel lets that claim ring at the boundary while the consequence still waits.\",\"root_display\":\"{{ar:غ ن ي}} ({{tr:gh-n-y}})\",\"root_gloss_range\":\"sufficiency, wealth, independence, availing, song, dwelling, marriage-related sufficiency, and disputed woman-description branches; the local Form X selects claimed needlessness, while availing remains active as a later same-root test\",\"surface_display\":\"{{ar:ٱسْتَغْنَىٰ}} ({{tr:istaghnā}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000089/B001","root_001110/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000089","role":"Withholding possessions from an outlet where they should not be withheld supplies the closed material boundary.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001110","role":"Wealth or reduced need supplies the inward claim that makes the closed boundary appear sufficient.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]}],"changed_reading":{"after":"A person closes what should circulate and interprets that closure as exemption from need.","before":"A person happens to be both miserly and wealthy."},"confidence":"strong","focus_anchor":"The sequence joins بَخِلَ to the reflexive claim ٱسْتَغْنَىٰ.","mechanism":"A possession that ought to pass outward is held inside, while need itself is disavowed. Withholding and self-sufficiency therefore form one closure mechanism rather than two unrelated defects, although the focus alone leaves open whether felt independence licenses retention or retention manufactures felt independence.","model_id":"base_closed_autonomy"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_closed_autonomy","source_type":"hft","support_id":"sup_0542e0121dd688297e66","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ","ayah_ref":"92:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000089/B001","root_001110/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000089","role":"Wrongful retention keeps the would-be substitute under the subject's control.","root":"ب خ ل","source_ref":"92:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001110","role":"Sufficing and standing in for something supplies the proxy relation assigned to the retained asset.","root":"غ ن ي","source_ref":"92:8","source_word_indices":["4"]}],"changed_reading":{"after":"He keeps a possession in place so that it can impersonate the relations and supports he refuses to need.","before":"He keeps wealth because he already has enough."},"confidence":"medium","focus_anchor":"The branch of غ ن ي in ٱسْتَغْنَىٰ that means sufficing, availing, or standing in for another element.","mechanism":"The retained possession is not merely accumulated; it is appointed as a substitute for whatever relation, recipient, or support the subject declines. بخل secures the proxy by preventing its departure, and استغناء names confidence that the proxy can stand in for what has been excluded.","model_id":"base_retained_proxy"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_retained_proxy","source_type":"hft","support_id":"sup_ab3f358f8b44e4a47975","trust":"legacy_unbound"}]}
</lane_packet_json>
