# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:25**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_25/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:25",
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
{"branch_registry":[{"boundary":"Çıplak dönüş çekirdeği ile dönüş yeri kullanımı birlikte verilir; sadece belirli söz öbeklerine ait yer adları genelleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000065/B001","candidate_links":[{"candidate_id":"cand_eaa3627c0a8949dbb768","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"dönüş ve dönüş yeri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel çekirdek, bir kişinin veya şeyin geri dönmesi ve önceki ya da beklenen varış yerine yönelmesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dönüşün kendisi yanında dönüş zamanı ve dönüş yeri de aynı anlam alanına girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuyu ortasında suyun toplandığı yer veya değirmende unun çıktığı yer gibi kullanımlar belirli yer adlarıdır."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çekirdek geri dönme eylemini ve bundan doğan dönüş yeri ya da dönüş zamanı anlamını birlikte taşıdığında uygundur.","boundary_detail":"Çıplak dönüş çekirdeği ile dönüş yeri kullanımı birlikte verilir; sadece belirli söz öbeklerine ait yer adları genelleştirilmez.","branch_image_ar":"الرجوع إلى المآب والموضع","concept_gloss":"dönüş ve dönüş yeri","contextual_glosses":[{"applicability":"Eylem biçimlerinde kişinin veya şeyin yerleştiği ya da beklenen yere dönmesini karşılar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dönüş yeri ve dönüş zamanı adlarını dışarıda bırakır.","preserves":"Dönüş hareketini korur."},"facet_ids":["F001"],"text":"geri dönmek","usage_role":"contextual"},{"applicability":"Bir yerin ya da varış noktasının dönüş noktası olarak anlatıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dönme eyleminin kendisini ve dönüş zamanı kullanımını dışarıda bırakır.","preserves":"Dönüş yeri yönünü korur."},"facet_ids":["F002","F003"],"text":"dönülen yer","usage_role":"contextual"}],"definition":"Bir kimsenin ya da şeyin geldiği yere, yerleştiği yere veya varacağı dönüş noktasına geri dönmesi; bundan hareketle dönüşün kendisi, dönüş zamanı ya da dönüş yeri de anlatılır. Bazı kullanımlarda anlam, suyun veya öğütülen şeyin toplandığı belirli yerle sınırlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel çekirdek, bir kişinin veya şeyin geri dönmesi ve önceki ya da beklenen varış yerine yönelmesidir."},{"facet_id":"F002","role":"extension","statement":"Dönüşün kendisi yanında dönüş zamanı ve dönüş yeri de aynı anlam alanına girer."},{"facet_id":"F003","role":"specialization","statement":"Kuyu ortasında suyun toplandığı yer veya değirmende unun çıktığı yer gibi kullanımlar belirli yer adlarıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Geri dönme koşulu bulunmayan her ulaşmayı da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir hedefe ulaşma yönünü kısmen korur."},"text":"varış"}],"identity_rationale":"Kaynak ifadesi bu dalı dönüş, geri gelme, varılacak dönüş yeri ve bazı şeylerin toplandığı yer çevresinde kuruyor. Provisional çerçeve de bu çekirdeği koruyor; yalnız kuyu ortasında suyun toplandığı yer ve değirmen çıkışı gibi kullanımlar çıplak dönüş anlamına değil, dönüş veya toplanma yerinin özel gerçekleşmelerine bağlı kalmalı.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yerleştiği ya da döneceği yere geri dönmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"geri dönüş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"geri dönme, dönüş"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir kez geri dönüş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dönülen yer, dönüş noktası"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuyunun ortasında suyun toplandığı yer"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"değirmende unun çıktığı ve altta kalan şeyin ulaştığı yer"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kovanına dönüp duran arılar"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"geri dönmek"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iyi ve hızlı geri dönen"}],"lexicalization_note":"Dal hem çıplak dönüş biçimlerini hem de kuyu veya değirmen gibi yapıya bağlı kullanımları içerir; tanım bu iki kapsamı ayırır.","neighbor_coverage_note":"Aday komşuların tamamı dönüş, varış, yön veya hareket alanında gözden geçirildi; yayımlananlar okuyucu için en muhtemel karışma noktalarını verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal geri dönme eylemini ve dönüş yerini birlikte taşır; komşu dalda ise nihai varış, sonuç ya da geri dönülecek yer daha belirleyici hale gelir.","focus_only":"Dönüş eylemi, dönüş yeri ve bazı somut toplanma yerleri aynı dalda yer alır.","gloss":"dönüş yeri ile son varış","neighbor_only":"Son varış, sonuç ve dönülecek son yer fikri daha belirgindir.","neighbor_ref":"root_001058/B002","relation_type":"near_synonym","shared_zone":"İkisi de bir yere dönme veya varılacak dönüş noktası anlam alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal somut ve adlandırılmış dönüş ilişkisini merkeze alır; komşu dalda dönüş, sonuç ve açıklamaya varma gibi daha soyut yönlere açılır.","focus_only":"Çekirdek açıkça geri dönüş ve dönüş yeri etrafındadır.","gloss":"dönüş ile sonuca varma","neighbor_only":"Bir şeyin sonucuna varması, son haline dönmesi veya sözün açıklanacağı anlama bağlanması da kapsama girer.","neighbor_ref":"root_000067/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeye geri bağlanma veya bir son noktaya yönelme hissi vardır."},{"boundary_match":"field_only","distinction":"Bu dal dönüşün genel adını ve yerini verir; komşu dal bedensel hareketin tekrarlı gidip gelmesine ya da özel yol alma biçimine bağlıdır.","focus_only":"Genel geri dönme ve dönüş yeri anlamını taşır.","gloss":"dönüş ile yürüyüşte salınım","neighbor_only":"Yürüyüşte el ve ayakların gidip gelmesi, gündüz yol alma ve eli silaha ya da oka götürme gibi hareket kalıplarıyla sınırlıdır.","neighbor_ref":"root_000065/B003","relation_type":"same_field","shared_zone":"Her ikisinde de geri gelme veya yönelme fikri bulunur."},{"boundary_match":"partial","distinction":"Bu dal dönüşü zaman şartı olmadan kurar; komşu dalda anlam gece vakti gelme ya da geceyle birlikte dönme sınırına bağlanır.","focus_only":"Dönüş herhangi bir zamana bağlı olmak zorunda değildir.","gloss":"dönüş ile gece gelişi","neighbor_only":"Gece gelme veya geceyle birlikte geri dönme koşulu belirleyicidir.","neighbor_ref":"root_000065/B006","relation_type":"near_neighbor","shared_zone":"İkisi de geliş veya geri dönüş hareketini içerir."}],"source_phrase_ar":"الأصل الرجوع (maqayis)؛ آب الغائب يؤوب أوبا أي رجع والمآب المرجع (ayn)؛ آب الرجل يؤوب إيابا إذا رجع إلى مستقره والمآب المرجع (jamhara)؛ آب أي رجع يؤوب أوبا وأوبة وإيابا والمآب المرجع (sihah)؛ الأوب ضرب من الرجوع يقال آب أوبا وإيابا ومآبا والمآب المصدر واسم الزمان والمكان (mufradat)؛ مآبة البئر حيث يجتمع إليه الماء في وسطها (ayn)","source_summary":"Kaynaklar ortak biçimde dönüşü temel alır; dönüş eylemi, dönüşün adı, dönüş yeri ve dönüş zamanını aynı çekirdekten açıklar. Kuyu ortasındaki su toplanma yeri ve değirmen çıkışı gibi örnekler, bu çekirdeğin belirli yerlere uygulanmış halidir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه آب يؤوب بمعنى رجع، والإياب والأوبة والمآب مرجعا أو موضعا، وما يرجع إلى مأواه أو يجتمع في موضعه.","what_is_not_ar":"ليس الإباء بمعنى ترك الطاعة، ولا الوباء، ولا مجرد الناحية إلا في فرع كل أوب."},"support_links":["sup_3db60bfcde263e2716e8"]},{"boundary":"Bu dal genel geri dönüş değildir; kişinin yanlış davranışı bırakıp Tanrı'ya yönelmesiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000065/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"Tanrı'ya dönüş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, kişinin yanlış davranışlardan dönüp Tanrı'ya yönelmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu dönüş, doğru kulluk eylemlerine yönelme ve önceki kusurlu halden vazgeçme şartıyla dini bir anlam taşır."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin yanlış davranışları bırakıp Tanrı'ya ve doğru eyleme yönelmesini anlatan dini bağlamlarda uygundur.","boundary_detail":"Bu dal genel geri dönüş değildir; kişinin yanlış davranışı bırakıp Tanrı'ya yönelmesiyle sınırlıdır.","branch_image_ar":"الرجوع إلى الله بالتوبة","concept_gloss":"Tanrı'ya dönüş","contextual_glosses":[{"applicability":"Ahlaki vazgeçme yönünün öne çıktığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı'ya yönelme ve doğru kulluk eylemlerine dönme yönünü açıkça söylemez.","preserves":"Yanlış davranıştan vazgeçme yönünü korur."},"facet_ids":["F001"],"text":"yanlıştan dönmek","usage_role":"contextual"}],"definition":"Kişinin yanlış davranışları bırakıp Tanrı'ya yönelmesi ve doğru kulluk eylemlerine dönmesidir. Anlam, yolculuktaki fiziksel dönüşten değil ahlaki ve dini dönüşten oluşur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, kişinin yanlış davranışlardan dönüp Tanrı'ya yönelmesidir."},{"facet_id":"F002","role":"specialization","statement":"Bu dönüş, doğru kulluk eylemlerine yönelme ve önceki kusurlu halden vazgeçme şartıyla dini bir anlam taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Fiziksel yolculuk dönüşüyle karıştırır.","fit":"displacement","loses":"Yanlış davranışı bırakma ve Tanrı'ya yönelme çekirdeğini kaybeder.","preserves":"Geri dönme fikrini korur."},"text":"seyahatten dönüş"}],"identity_rationale":"Kaynak ifadesi bu dalı kişinin Tanrı'ya yönelerek yanlış davranışları bırakması ve doğru eylemlere dönmesi biçiminde dini dönüş olarak kuruyor. Provisional çerçeve bu anlamı doğru yakalıyor ve genel yolculuk dönüşünden ayrılması gerektiğini de belirtiyor.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yanlış davranışı bırakıp Tanrı'ya dönen kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yanlış davranıştan Tanrı'ya dönüş"}],"lexicalization_note":"Mekanik kapsam çıplak daldır; tanım özel bir söz öbeğine değil, dini dönüş anlamının kendisine bağlanır.","neighbor_coverage_note":"Komşu adayların çoğu beden parçaları veya duruş alanındaydı ve bu dalın dini dönüş çekirdeğiyle ancak zayıf tematik bağ kurdu; en yararlı karşıtlıklar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, kişinin yanlış davranışı bırakıp Tanrı'ya yönelmesiyle tanımlanır; komşu dal böyle bir ahlaki şart taşımayan genel dönüş alanıdır.","focus_only":"Dönüş ahlaki ve dini bir yön değiştirmedir.","gloss":"dini dönüş ile genel dönüş","neighbor_only":"Genel fiziksel dönüş, dönüş yeri ve dönüş zamanı anlamlarını taşır.","neighbor_ref":"root_000065/B001","relation_type":"near_neighbor","shared_zone":"İkisi de dönme çekirdeğini paylaşır."},{"boundary_match":"thematic_only","distinction":"Bu dal iradi ve dini yönelişi anlatır; komşu dal bedensel biçim ve fiziksel eğrilik alanındadır.","focus_only":"Kişinin davranış ve yöneliminde dini dönüş vardır.","gloss":"ahlaki dönüş ile ayak eğriliği","neighbor_only":"Ayak veya bacak yapısındaki eğrilik ve fiziksel yön sapması vardır.","neighbor_ref":"root_000362/B001","relation_type":"thematic","shared_zone":"İkisi de yön değişimi veya sapma çağrışımı kurabilir."}],"source_phrase_ar":"الأواب التائب (sihah)؛ الأواب كالتواب وهو الراجع إلى الله تعالى بترك المعاصي وفعل الطاعات ومنه قيل للتوبة أوبة (mufradat)","source_summary":"Kaynaklar bu dalı dini dönüş olarak verir: kişi yanlış davranışları bırakır, Tanrı'ya yönelir ve doğru eyleme döner. Aynı çekirdek, bu dönüş eyleminin adı için de kullanılır.","sources":["SI","MU"],"what_is_ar":"يدخل فيه الأواب والتوبة والأوبة الدينية، أي الرجوع إلى الله بترك المعاصي وفعل الطاعات.","what_is_not_ar":"ليس كل راجع في الطريق أو السفر أو الليل أو سير الدابة."},"support_links":[]},{"boundary":"Dal, yürüyüş ve el hareketi gibi bedensel ya da yol alma bağlamlarına bağlıdır; genel eve dönüş anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000065/B003","candidate_links":[{"candidate_id":"cand_08d506b45cda59766291","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"yürüyüşte gidip gelme hareketi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, hareket eden uzvun geri gelip tekrar yönelmesi veya gidip gelmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yürüyüşte el ve ayakların hızlı çevrilmesi veya salınması bu çekirdeğin özel gerçekleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gündüz boyunca yol alma ve gece konaklama kullanımı, yolculuk düzenine bağlı ayrı bir kullanım olarak kalır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Elin kılıca veya okun bulunduğu yere geri götürülmesi bu hareket çekirdeğinin örneklerindendir."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"El ve ayakların yürüyüşte salınması ile bu hareketten türeyen özel yol alma ve el uzatma bağlamlarını karşılar.","boundary_detail":"Dal, yürüyüş ve el hareketi gibi bedensel ya da yol alma bağlamlarına bağlıdır; genel eve dönüş anlamına genişletilmez.","branch_image_ar":"تردد الجوارح في السير والتأويب","concept_gloss":"yürüyüşte gidip gelme hareketi","contextual_glosses":[{"applicability":"Yolculuğun gündüz boyunca sürdürülüp gece konaklamaya bağlandığı kullanımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzuvların yürüyüşte gidip gelmesi ve elin silaha yönelmesi yönlerini dışarıda bırakır.","preserves":"Yol alma ve gündüz süresi yönünü korur."},"facet_ids":["F003"],"text":"gündüz boyu yol almak","usage_role":"contextual"},{"applicability":"Kılıç ya da ok gibi bir nesneye elin geri yönelmesi anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yürüyüşte ayak ve el salınımı ile gündüz yol alma yönlerini dışarıda bırakır.","preserves":"Hedefli el dönüşünü korur."},"facet_ids":["F004"],"text":"elini geri götürmek","usage_role":"contextual"}],"definition":"Yürüyüşte el ve ayakların gidip gelmesi ya da hızlı salınması, yolculuğun gündüz boyunca sürdürülmesi ve elin kılıç veya oka doğru geri götürülmesi gibi hareket düzenleridir. Bu dalda dönüş çekirdeği, bedensel salınım veya belirli yol alma biçimi olarak özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, hareket eden uzvun geri gelip tekrar yönelmesi veya gidip gelmesidir."},{"facet_id":"F002","role":"specialization","statement":"Yürüyüşte el ve ayakların hızlı çevrilmesi veya salınması bu çekirdeğin özel gerçekleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Gündüz boyunca yol alma ve gece konaklama kullanımı, yolculuk düzenine bağlı ayrı bir kullanım olarak kalır."},{"facet_id":"F004","role":"example","statement":"Elin kılıca veya okun bulunduğu yere geri götürülmesi bu hareket çekirdeğinin örneklerindendir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Bu dalı genel dönüş dalıyla karıştırır.","fit":"displacement","loses":"Yürüyüşte uzuv hareketi, gündüz yol alma ve elin silaha yönelmesi kullanımlarını kaybeder.","preserves":"Geri dönme yönünü kısmen korur."},"text":"eve dönmek"}],"identity_rationale":"Kaynak ifadesi el ve ayakların yürüyüşte gidip gelmesi, gündüz yol alma, elin kılıca ya da oka dönmesi ve hızlı geri salınan deve eli gibi hareket kullanımlarını birlikte veriyor. Provisional çerçeve bu kullanımları doğru topluyor, fakat bunlar genel dönüş anlamı değil hareket düzenine bağlı özel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yürüyüşte el ve ayakların gidip gelmesi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gündüz boyunca yol alma ve gece konaklama"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bu gündüz yol alışın tek bir seferi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ön ayaklarını hızlı geri salan deve"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kılıcını çekmek için elini kılıca geri götürmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"okçunun elinin oka geri dönmesi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bineklerin yürüyüşte birbirleriyle yarışması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"develeri barınaklarına döndürmek veya gündüz yol aldırmak"}],"lexicalization_note":"Kapsam hem türemiş biçimleri hem de belirli söz öbeklerini içerir; tanım çıplak dönüşle bu hareket kalıplarını birleştirmez.","neighbor_coverage_note":"Hareket, yürüyüş, uzuv bozukluğu ve iç dal adayları incelendi; yayımlanan ayrımlar gerçek karışma riski taşıyan hareket komşularıyla sınırlı tutuldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yürüyüş salınımını daha geniş bir hareket ve yolculuk ağına bağlar; komşu dal hayvan yürüyüşündeki geri adım hareketinde daha dar durur.","focus_only":"Gündüz yol alma ve eli kılıç ya da oka döndürme gibi bağlı kullanımlar da içerir.","gloss":"yürüyüşte geri salınım","neighbor_only":"Daha özel olarak hayvanın yürüyüşte ellerini ve adımlarını geri getirmesine odaklanır.","neighbor_ref":"root_000544/B008","relation_type":"near_synonym","shared_zone":"İkisi de yürüyüş sırasında uzuvların geri hareketini anlatır."},{"boundary_match":"partial","distinction":"Bu dal insan, hayvan ve araçlı hareket bağlamlarını birlikte taşır; komşu dal deve yürüyüşündeki belirli el hareketine daha dar bağlıdır.","focus_only":"El ve ayakların yürüyüşte genel gidip gelişi ile gündüz yol alma ve elin silaha yönelmesi de kapsama girer.","gloss":"uzuv salınımı ile deve eli","neighbor_only":"Devenin ellerinin yürüyüşte geri gelmesiyle sınırlıdır.","neighbor_ref":"root_000009/B009","relation_type":"near_synonym","shared_zone":"İki dal da yürüyüşte ön uzuvların geri hareketini paylaşır."},{"boundary_match":"partial","distinction":"Bu dal hareketin geri geliş ve tekrar yönünü merkeze alır; komşu dalda asıl unsur hız veya sarsıntılı harekettir.","focus_only":"Geri dönme ve gidip gelme yönü açıkça çekirdektedir.","gloss":"geri salınım ile hızlı sarsılma","neighbor_only":"Sarsılma, hızlanma veya çalkalanma dönüş şartı olmadan da bulunur.","neighbor_ref":"root_001014/B004","relation_type":"near_neighbor","shared_zone":"İkisi de hareket, hız ve beden ya da nesne salınımı alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal geri gelmeyi hareket tekniği veya yolculuk düzeni olarak işler; komşu dal dönüşün genel adını ve yerini verir.","focus_only":"Yürüyüş ve uzuv hareketi bağlamlarına bağlıdır.","gloss":"salınım ile dönüş","neighbor_only":"Genel geri dönüş, dönüş yeri ve dönüş zamanı anlamlarını taşır.","neighbor_ref":"root_000065/B001","relation_type":"same_field","shared_zone":"İkisi de geri gelme fikrini paylaşır."}],"source_phrase_ar":"آب فلان إلى سيفه أي رد يده ليستله والأوب ترجيع الأيدي والقوائم في السير والتأويب وسير النهار تأويبا (maqayis)؛ الأوب ترجيح الأيدي والقوائم في السير والتأويب سير النهار إلى الليل (ayn)؛ الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل (sihah)؛ آبت يد الرامي إلى السهم وناقة أؤوب سريعة رجع اليدين (mufradat)","source_summary":"Kaynaklar bu dalda uzuvların yürüyüşte gidip gelmesini, hızlı el ve ayak hareketini, gündüz yol almayı ve elin silaha ya da oka yönelmesini aynı hareket alanında toplar. Ortak nokta, genel dönüşten çok tekrarlı ya da hedefli geri hareketin belirli bağlamlara uygulanmasıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه أوب الأيدي والقوائم في السير، وسرعة رجع اليدين، وتأويب الإبل وسير النهار، ورد اليد إلى السيف أو السهم.","what_is_not_ar":"ليس مطلق الرجوع إلى الوطن، ولا التسبيح، ولا الإتيان ليلا إلا إذا صرحت المادة بذلك."},"support_links":["sup_849d326c5fc0c32f98f8"]},{"boundary":"Bu dal yalnız her yön, her taraf anlamındaki söz öbeğine bağlıdır; çıplak dönüş anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000065/B004","candidate_links":[{"candidate_id":"cand_f7808808c4d691c5fa5f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"her yönden","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, gelişin tek bir yönden değil her yönden gerçekleşmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anlam, belirli söz öbeğinde yön veya taraf anlamıyla sınırlıdır."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir gelişin farklı yönlerden veya her taraftan gerçekleştiği söz öbeği bağlamında uygundur.","boundary_detail":"Bu dal yalnız her yön, her taraf anlamındaki söz öbeğine bağlıdır; çıplak dönüş anlamı değildir.","branch_image_ar":"الأوب ناحية يؤتى منها","concept_gloss":"her yönden","contextual_glosses":[{"applicability":"İnsanların veya bir topluluğun çeşitli yönlerden geldiği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çok yönlü geliş anlamını korur."},"facet_ids":["F001"],"text":"her taraftan","usage_role":"contextual"}],"definition":"Bir topluluğun her yönden, her taraftan veya çeşitli yönlerden gelmesini anlatan söz öbeği kullanımıdır. Buradaki anlam dönüş değil, gelişin yönlerinin çokluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, gelişin tek bir yönden değil her yönden gerçekleşmesidir."},{"facet_id":"F002","role":"specialization","statement":"Anlam, belirli söz öbeğinde yön veya taraf anlamıyla sınırlıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel dönüş dalıyla karışır.","fit":"displacement","loses":"Bu söz öbeğindeki her yön veya her taraf anlamını kaybeder.","preserves":"Aynı kökün başka bir dalındaki dönüş çağrışımını korur."},"text":"geri dönüş"}],"identity_rationale":"Kaynak ifadesi tek bir kalıpta, insanların her yönden ya da her taraftan gelmesini anlatıyor. Provisional çerçeve bu söz öbeği sınırını doğru koruyor ve bunu genel dönüş veya yürüyüş hareketiyle karıştırmıyor.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"her yön, her taraf"}],"lexicalization_note":"Mekanik kapsam söz öbeğidir; tanım sadece her yönden gelme kalıbına uygulanır ve çıplak kök anlamına genelleştirilmez.","neighbor_coverage_note":"Yön, yol ve taraf alanındaki adaylar değerlendirildi; çoğu yalnız genel alan ortaklığı taşıdığı için en açıklayıcı iki ayrım verildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal gelişin çok yönlülüğünü anlatan sabit kalıptır; komşu dal taraf veya uç anlamını geliş koşulu olmadan daha geniş kullanır.","focus_only":"Her yönden gelme söz öbeğine bağlıdır.","gloss":"her yön ile taraf","neighbor_only":"Bir işin tarafı, hali veya kenarı gibi daha genel taraf anlamlarını kapsar.","neighbor_ref":"root_000859/B009","relation_type":"near_neighbor","shared_zone":"İkisi de yön, taraf veya yan anlam alanında buluşur."},{"boundary_match":"field_only","distinction":"Bu dal gelişin yönlerini ifade eder; komşu dal kişinin veya şeyin geri dönmesini ve dönülen yeri ifade eder.","focus_only":"Yön ve taraf anlamındaki söz öbeğidir.","gloss":"her yön ile dönüş","neighbor_only":"Geri dönme, dönüş yeri ve dönüş zamanı anlamlarını taşır.","neighbor_ref":"root_000065/B001","relation_type":"same_field","shared_zone":"Aynı kökün dönüşten genişleyen anlam ağı içinde bulunurlar."}],"source_phrase_ar":"جاءوا من كل أوب أي ناحية ووجه (maqayis)؛ جاءوا من كل أوب أي من كل وجه وناحية (ayn)؛ جاء القوم من كل أوب أي من كل ناحية (jamhara)؛ جاءوا من كل أوب أي من كل ناحية (sihah)","source_summary":"Kaynaklar ortak biçimde bu kalıbı her yönden veya her taraftan gelme diye açıklar. Dönüş çekirdeği burada bağımsız bir eylem olarak değil, yön anlamına dönüşmüş söz öbeği içinde kalır.","sources":["MQ","AY","JA","SI"],"what_is_ar":"يدخل فيه قولهم جاءوا من كل أوب، أي من كل ناحية أو وجه.","what_is_not_ar":"ليس المآب مرجعا، ولا أوب الجوارح في السير."},"support_links":["sup_28f84d3a542114988830"]},{"boundary":"Bu dal yalnız kutsal övgünün tekrarlanması veya karşılık verilmesi bağlamındadır; fiziksel dönüş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000065/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"kutsal övgüyü yineleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, kutsal övgünün sesle yinelenmesi veya ona karşılık verilmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım, dağlara yönelen emir bağlamındaki birlikte yüceltme söyleyişine bağlıdır."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağlara yöneltilen hitapta övgü sözünü sesle tekrarlama veya karşılık verme anlamında uygundur.","boundary_detail":"Bu dal yalnız kutsal övgünün tekrarlanması veya karşılık verilmesi bağlamındadır; fiziksel dönüş değildir.","branch_image_ar":"ترجيع التسبيح","concept_gloss":"kutsal övgüyü yineleme","contextual_glosses":[{"applicability":"Emir kipindeki hitapta övgü sözünü birlikte seslendirme yönünü doğal biçimde verir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sesin tekrarlı karşılık verme yönünü açıkça söylemez.","preserves":"Emir ve yüceltme yönünü korur."},"facet_ids":["F001","F002"],"text":"birlikte yüceltin","usage_role":"contextual"}],"definition":"Dağlara yöneltilen hitapta kutsal övgüyü tekrarlama, ona sesle karşılık verme veya birlikte yineleme anlamıdır. Dönüş fikri burada fiziksel geri gelme değil, sesin ve övgünün karşılıklı yinelenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, kutsal övgünün sesle yinelenmesi veya ona karşılık verilmesidir."},{"facet_id":"F002","role":"specialization","statement":"Kullanım, dağlara yönelen emir bağlamındaki birlikte yüceltme söyleyişine bağlıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Fiziksel dönüş anlamıyla karıştırır.","fit":"displacement","loses":"Kutsal övgüyü sesle yineleme anlamını kaybeder.","preserves":"Kökün başka dallarındaki dönüş çağrışımını korur."},"text":"geri dönmek"}],"identity_rationale":"Kaynak ifadesi dağlara yönelik emir bağlamında Tanrı'yı yüceltme sözünü yinelemek veya karşılık vermek anlamını gösteriyor. Provisional çerçeve bunu duyusal geri dönüşten ve gündüz yol alıştan ayırarak doğru sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kutsal övgüyü sesle yineleyin"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kutsal övgüyü yineleme"}],"lexicalization_note":"Kapsam belirli bağlamdaki emir biçimiyle türemiş ad kullanımını birlikte taşır; tanım dini sesli yineleme alanıyla sınırlanır.","neighbor_coverage_note":"Zaman, yineleme, kutsal söyleyiş ve iç dal adayları gözden geçirildi; açık sınır kuran iki aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"thematic_only","distinction":"Bu dal sesli övgünün tekrarıdır; komşu dal başlangıç veya önce gelme fikrini taşır.","focus_only":"Kutsal övgüyü yineleme veya karşılık verme anlamındadır.","gloss":"yineleme ile ilk olma","neighbor_only":"Başlangıç, ilk olma veya zaman ve sıra bakımından öne geçme anlamındadır.","neighbor_ref":"root_000067/B001","relation_type":"thematic","shared_zone":"İki dal aynı ses benzerliği ve sıralama hissi üzerinden karıştırılabilir."},{"boundary_match":"partial","distinction":"Bu dal fiziksel veya yerel dönüş değil, övgü sesinin tekrar edilmesi anlamıdır; komşu dal gerçek dönüş ve dönüş yeri alanındadır.","focus_only":"Dönüş fikri sesli övgünün yankılı veya karşılıklı yinelenmesine aktarılmıştır.","gloss":"övgüyü yineleme ile dönüş","neighbor_only":"Kişi, şey, dönüş yeri ve dönüş zamanı alanındaki genel geri dönüştür.","neighbor_ref":"root_000065/B001","relation_type":"near_neighbor","shared_zone":"İkisi de geri gelme veya karşılık verme hissinden yararlanır."}],"source_phrase_ar":"التأويب التسبيح في قوله يا جبال أوبي معه والطير (maqayis)؛ يا جبال أوبي معه أي سبحي (sihah)","source_summary":"Kaynaklar bu dalı kutsal övgüyü seslendirme veya yineleme olarak açıklar ve verilen hitap bağlamına bağlar. Ortak anlam fiziksel dönüş değil, övgü sözünün karşılıklı ya da tekrarlı seslendirilmesidir.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه أوبي بمعنى سبحي في خطاب الجبال، أي إرجاع التسبيح ومجاوبته.","what_is_not_ar":"ليس مجرد الرجوع الحسي ولا سير النهار."},"support_links":[]},{"boundary":"Anlam gece şartına bağlıdır; herhangi bir zamanda gerçekleşen genel dönüş bu dala alınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000065/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"geceleyin gelmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, gece vakti gelme veya birine geceleyin uğramadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Geceyle birlikte geri dönen kişi de aynı zaman şartlı dönüş alanına girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı ifadelerde geliş özellikle gecenin başında gerçekleşir."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birine gece uğrama, gece gelme veya geceyle birlikte dönme bağlamlarında uygundur.","boundary_detail":"Anlam gece şartına bağlıdır; herhangi bir zamanda gerçekleşen genel dönüş bu dala alınmaz.","branch_image_ar":"الإتيان ليلا والعودة مع الليل","concept_gloss":"geceleyin gelmek","contextual_glosses":[{"applicability":"Bir kişiye geceleyin gelme veya onu gece ziyaret etme bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geceyle birlikte geri dönen kişi kullanımını dışarıda bırakır.","preserves":"Gece gelme ve birine uğrama yönünü korur."},"facet_ids":["F001","F003"],"text":"gece uğramak","usage_role":"contextual"},{"applicability":"Kişinin geceyle birlikte geri dönmüş olması vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birine geceleyin gelme veya uğrama kullanımını dışarıda bırakır.","preserves":"Gece vakti geri dönme yönünü korur."},"facet_ids":["F002"],"text":"gece dönen kişi","usage_role":"contextual"}],"definition":"Bir kimseye gece vakti gelmek, geceleyin uğramak veya geceyle birlikte geri dönmek anlamıdır. Bu dalda dönüş ya da geliş, özellikle gece zamanı ile sınırlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, gece vakti gelme veya birine geceleyin uğramadır."},{"facet_id":"F002","role":"extension","statement":"Geceyle birlikte geri dönen kişi de aynı zaman şartlı dönüş alanına girer."},{"facet_id":"F003","role":"specialization","statement":"Bazı ifadelerde geliş özellikle gecenin başında gerçekleşir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gece şartı olmayan dönüşleri de kapsar.","collision":"Genel dönüş dalıyla karıştırır.","fit":"broadening","loses":null,"preserves":"Geri dönme yönünü korur."},"text":"her dönüş"}],"identity_rationale":"Kaynak ifadesi gece gelme, geceleyin birine uğrama ve geceyle birlikte geri dönen kişi anlamlarını bir arada veriyor. Provisional çerçeve doğru; ancak bu dal genel dönüş değil, zaman koşulu gece olan geliş veya dönüş kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"birine geceleyin gelmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"geceyle birlikte geri dönen"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gecenin başında veya geceleyin gelen"}],"lexicalization_note":"Kapsam türemiş biçimler ve nesneli kullanım içerir; tanım gece vaktine bağlı geliş veya dönüş sınırını korur.","neighbor_coverage_note":"Gece, sabah, yolculuk ve iç dal adayları karşılaştırıldı; yayımlanan ayrımlar zaman şartını en iyi görünür kılan adaylardır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal geceyi bir eylemin zamanı olarak şart koşar; komşu dal gece kavramının kendisini anlatır.","focus_only":"Gece vaktinde gerçekleşen gelme veya geri dönme eylemidir.","gloss":"gece gelişi ile gece","neighbor_only":"Gece zamanının kendisi, karanlığı ve uzunluğu anlatılır.","neighbor_ref":"root_001392/B001","relation_type":"same_field","shared_zone":"İki dal gece zaman alanını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal varış veya uğrama noktasını da taşıyan gece gelişidir; komşu dal yolculuğun gece içinde sürdürülmesine odaklanır.","focus_only":"Birine gece gelme veya geceyle birlikte dönme anlamındadır.","gloss":"gece gelmek ile gece yol almak","neighbor_only":"Gece boyunca yorucu veya sürekli yol alma anlamı ağır basar.","neighbor_ref":"root_001422/B003","relation_type":"near_neighbor","shared_zone":"İkisi de gece vaktindeki hareket ve yolculuk alanındadır."},{"boundary_match":"opposed","distinction":"Bu dal gece vaktini şart koşar; komşu dal aynı tür gelişi sabah vaktine bağlayan karşı zaman kutbudur.","focus_only":"Gelişin gece gerçekleşmesi belirleyicidir.","gloss":"gece gelmek ile sabah gelmek","neighbor_only":"Gelişin sabah gerçekleşmesi belirleyicidir.","neighbor_ref":"root_000839/B002","relation_type":"polarity_pair","shared_zone":"İkisi de bir geliş eylemini günün belirli zamanına bağlar."},{"boundary_match":"partial","distinction":"Bu dal hareketi gece zamanına bağlar; komşu dal dönüşü zaman şartı olmadan kurar.","focus_only":"Gece vakti gelme veya geceyle birlikte dönüş sınırı vardır.","gloss":"gece gelişi ile genel dönüş","neighbor_only":"Dönüş zaman şartı olmadan, dönüş yeri ve dönüş adıyla birlikte verilir.","neighbor_ref":"root_000065/B001","relation_type":"near_neighbor","shared_zone":"İkisi de gelme veya geri dönme hareketini paylaşır."}],"source_phrase_ar":"تأوبني أي أتاني ليلا وأكثر ما يجيء الإياب مع الليل (maqayis)؛ كل راجع مع الليل فهو آئب (jamhara)؛ تأوبتهم إذا أتيتهم ليلا وتأوبت إذا جئت أول الليل (sihah)","source_summary":"Kaynaklar bu dalı geceleyin gelme veya geceyle birlikte geri dönme olarak birleştirir. Ortak sınır, geliş ya da dönüşün gece zamanına bağlanmasıdır; bu yüzden genel dönüş anlamı buraya taşınmaz.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه تأوبني أو تأوبتهم بمعنى أتاني أو جئتهم ليلا، وكل راجع مع الليل فهو آئب.","what_is_not_ar":"ليس كل إياب في أي وقت، ولا الأوب بمعنى الناحية."},"support_links":[]},{"boundary":"Bu dal güneşe ve onun batıya doğru gidip batmasına bağlıdır; genel dönüş veya dini dönüş değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000065/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","surface_ar":"إِيَابَ"}],"gloss":"güneşin batması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, güneşin batma yerine gidip görünmez olmasıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneşin doğu ile batı arasındaki günlük seyri ve batıya varışı da bu alana bağlanır."}}],"root_ar":"ء و ب","root_id":"root_000065","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güneşin batıdaki kayboluşu veya batma yerine varışı anlatıldığında uygundur.","boundary_detail":"Bu dal güneşe ve onun batıya doğru gidip batmasına bağlıdır; genel dönüş veya dini dönüş değildir.","branch_image_ar":"غروب الشمس إلى مآبها","concept_gloss":"güneşin batması","contextual_glosses":[{"applicability":"Cümlede güneşin görünmez olacak şekilde batması anlatıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin doğudan batıya günlük seyri yönünü açıkça söylemez.","preserves":"Güneşin batışını korur."},"facet_ids":["F001"],"text":"güneş battı","usage_role":"contextual"},{"applicability":"Güneşin günlük yolunda batıya varması veya batı ufkuna yönelmesi vurgulandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin kaybolup batması sonucunu açıkça söylemez.","preserves":"Batıya yöneliş ve varış yönünü korur."},"facet_ids":["F002"],"text":"batıya yönelmek","usage_role":"contextual"}],"definition":"Güneşin batma yerine yönelerek kaybolması veya doğudan batıya günlük yolunu tamamlaması anlamıdır. Dönüş fikri burada güneşin batıya varışı ve batışıyla sınırlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, güneşin batma yerine gidip görünmez olmasıdır."},{"facet_id":"F002","role":"extension","statement":"Güneşin doğu ile batı arasındaki günlük seyri ve batıya varışı da bu alana bağlanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Güneş dışındaki bütün geri dönüşleri de kapsar.","collision":"Genel dönüş dalıyla karıştırır.","fit":"broadening","loses":null,"preserves":"Dönüş yönünü soyut olarak korur."},"text":"geri dönmek"}],"identity_rationale":"Kaynak ifadesi güneşin batışını, batma yerine yönelmesini ve doğu ile batı arasındaki günlük gidişini anlatıyor. Provisional çerçeve bunu doğru sınırlar; anlam insan ya da hayvan dönüşü değil, güneşin batıya yönelen kayboluşudur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"güneşin batma yerine varıp kaybolması"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"güneşin doğudan batıya günlük gidişi ve batıya varışı"}],"lexicalization_note":"Kapsam güneşe bağlı söz öbeği ile güneşin günlük gidişini adlandıran biçimi birlikte içerir; tanım güneş dışına genelleştirilmez.","neighbor_coverage_note":"Batış, batıya yönelme, güneşin kaybolması ve iç dal adayları değerlendirildi; aşama ve kapsam farkı kuran adaylar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal güneşin batma yerine varmasını dönüş köküyle anlatır; komşu dal batı ve batış alanının daha doğrudan ve geniş adlandırmasıdır.","focus_only":"Güneşin batma yerine dönüşü ve günlük seyri bu kökün dönüş çerçevesiyle anlatılır.","gloss":"güneşin batması ile batı","neighbor_only":"Batı yönü, güneşin batışı ve doğu-batı karşıtlığı daha geniş biçimde kapsanır.","neighbor_ref":"root_001077/B006","relation_type":"near_synonym","shared_zone":"İkisi de güneşin batması ve batı yönü alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal batışı dönüş yeri ve günlük seyir diliyle açıklar; komşu dal kaybolma ve ufukta batma eylemine daha doğrudan odaklanır.","focus_only":"Güneşin batıya yönelen günlük yolunu ve batma yerine varışını da içerir.","gloss":"batma yerine varış ile ufukta kaybolma","neighbor_only":"Ufukta kaybolma veya batma eylemi doğrudan çekirdektir.","neighbor_ref":"root_001112/B004","relation_type":"near_synonym","shared_zone":"İkisi de güneşin batması ve gözden kaybolması anlamını paylaşır."},{"boundary_match":"partial","distinction":"Bu dal varış ve batış sonucunu taşır; komşu dal yalnız bu sonuca yaklaşma evresini anlatır.","focus_only":"Batma veya batma yerine varma sonucunu anlatır.","gloss":"batmak ile batmaya yaklaşmak","neighbor_only":"Güneşin batmaya yaklaşması, henüz batmaması anlamındadır.","neighbor_ref":"root_000908/B006","relation_type":"near_neighbor","shared_zone":"İkisi de güneşin gün sonundaki batı ufkuna yönelmesi alanındadır."},{"boundary_match":"thematic_only","distinction":"Bu dal göksel olaydır; komşu dal insan gelişinin gece zamanına bağlanmasıdır.","focus_only":"Güneşin batması ve günün kapanışı anlamındadır.","gloss":"gün batımı ile gece gelişi","neighbor_only":"Bir kişinin geceleyin gelmesi veya geceyle birlikte dönmesi anlamındadır.","neighbor_ref":"root_000065/B006","relation_type":"thematic","shared_zone":"İkisi de günün akşam ve gece sınırıyla ilişkilidir."}],"source_phrase_ar":"آيت الشمس إيابا إذا غابت في مآبها والمؤوبة الشمس وتأويبها ما بين المشرق والمغرب وتؤوب المغرب (maqayis)؛ آبت الشمس إيابا إذا غابت في مآبها أي مغيبها (ayn)؛ آبت الشمس لغة في غابت (sihah)","source_summary":"Kaynaklar güneş için bu dalı batma, batma yerine varma ve doğudan batıya süren günlük yolun batıda tamamlanması olarak verir. Ortak sınır, anlamın güneşe ve batış yönüne bağlı olmasıdır.","sources":["MQ","AY","SI"],"what_is_ar":"يدخل فيه آبت الشمس إذا غابت في مآبها، والمؤوبة أو تأويب الشمس في سيرها إلى المغرب.","what_is_not_ar":"ليس رجوع الإنسان أو الدابة، ولا التوبة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:25:1"],"branch_refs":[],"candidate_id":"cand_ec3142f0046b0125a9b1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:1:certified-return-proposition","source_type":"word_analysis","support_ids":["sup_53fb730f87b546f986f7","sup_712800e75b590e041d18"],"title":"emphatic certification of the return claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:1","qac_refs":["88:25:1:1"],"status":"accepted"}},{"anchor_refs":["88:25:1"],"branch_refs":[],"candidate_id":"cand_8e39dde98011f50c7d4c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:1:fronted-predicate-governance","source_type":"word_analysis","support_ids":["sup_712800e75b590e041d18","sup_8220a08e77aca3f265a1"],"title":"governance across a reordered nominal clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:1","qac_refs":["88:25:1:1"],"status":"accepted"}},{"anchor_refs":["88:25:1"],"branch_refs":[],"candidate_id":"cand_66de6a3616bc078cc7f6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:1:nominal-verdict-after-punishment","source_type":"word_analysis","support_ids":["sup_712800e75b590e041d18","sup_728ceb83869eb16263fb"],"title":"event narration shifts into standing verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:1","qac_refs":["88:25:1:1"],"status":"accepted"}},{"anchor_refs":["88:25:1"],"branch_refs":[],"candidate_id":"cand_6467b6d060aa79a05ba3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:1:opening-sound-weight","source_type":"word_analysis","support_ids":["sup_712800e75b590e041d18","sup_d0570e0cfb9392f41629"],"title":"audible weight of the opening assertion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:1","qac_refs":["88:25:1:1"],"status":"accepted"}},{"anchor_refs":["88:25:1"],"branch_refs":[],"candidate_id":"cand_361b55f579d2921c98e4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:1:return-and-account-certification","source_type":"word_analysis","support_ids":["sup_712800e75b590e041d18","sup_c54365c044d4a0a07ae5"],"title":"return and reckoning as paired certified stages","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:1","qac_refs":["88:25:1:1"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_277a51fefda858ae022e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:bound-speaker-reference","source_type":"word_analysis","support_ids":["sup_257c82698080cc46bf67","sup_95db8113b0faf313d183"],"title":"bound first-person suffix makes the endpoint immediate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_2787d8e8ed01aca3c1c1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:cadenced-endpoint","source_type":"word_analysis","support_ids":["sup_95db8113b0faf313d183","sup_c4d8f4dff60e8ce71a9b"],"title":"lengthened endpoint before the compact return noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_172dcf1b016ce626bf17","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:destination-endpoint","source_type":"word_analysis","support_ids":["sup_5488aac0f89d0c8a92a4","sup_95db8113b0faf313d183"],"title":"endpoint and authority fused in the destination phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_b309b88f57bf5ac6fac9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:fronted-restrictive-predicate","source_type":"word_analysis","support_ids":["sup_37b10333da65135d26c8","sup_95db8113b0faf313d183"],"title":"fronted endpoint governs how the return is heard","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_5b3ec69e8e435b21a4ae","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:return-formula-echo","source_type":"word_analysis","support_ids":["sup_81406d92623ee6245177","sup_95db8113b0faf313d183"],"title":"return-to-divine-endpoint formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:2"],"branch_refs":[],"candidate_id":"cand_f7b76a968a8f10c69afc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:2:return-to-account-bridge","source_type":"word_analysis","support_ids":["sup_493ed937a16de0c4ce06","sup_95db8113b0faf313d183"],"title":"same speaker-frame moves from destination to responsibility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:2","qac_refs":["88:25:2:1","88:25:2:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_5f7ea4430d03961cb156","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:accountability-valenced-homecoming","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_ce72dfc2730ab499eb5f"],"title":"homeward return becomes answerable arrival","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_04445aaaf80dc6684899","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:delayed-return-under-endpoint","source_type":"word_analysis","support_ids":["sup_26787dfdda11936d13ba","sup_2f387180687b5af4865d"],"title":"return noun lands after certainty and endpoint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_4242b1842c7ed811a3bf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:endpoint-return-sound-link","source_type":"word_analysis","support_ids":["sup_07d3348b3b7c9a581587","sup_2f387180687b5af4865d"],"title":"endpoint and return are linked in adjacent sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_89614b57e26224af3b36","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:masdar-not-finite-or-place","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_86ec85b64532cdd28c0b"],"title":"event noun instead of verb, place, or repeated form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_1c680573388158ad42c8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:possessed-return-event","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_4cc3bd21432fce59c718"],"title":"possessed masdar binds the group to return","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_48083dea91ce13d6781d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:rare-dense-closure","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_fe6568437333a47ae53d"],"title":"rare event noun concentrates the clause closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_41dd73b14651ba9bc770","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:repentance-overlap-limited","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_4285fc4da89d68e063f8"],"title":"return-field overlap without repentance sense","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_0711f08f9f331ab7612c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:return-enables-account-bridge","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_634cb9573fe7189ffe16"],"title":"arrival stage hands forward to account","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_bb173de269ca66c8dea0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:return-not-generic-motion","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_3788428e93b027d687c1"],"title":"coming back reverses prior turning away","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_93cae67156cf2e8541d2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:returner-to-account-patient","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_c96a938750bf40ec73f2"],"title":"returning subject becomes reckoned patient","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_c297c07a9ae02ae9cfbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:root-family-limits","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_ee92257a4a845c39b9f0"],"title":"related root forms stay as contrast, not replacements","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_b342215933d146d190d8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:singular-abstract-plural-group","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_9259d4b95fdc410e304d"],"title":"one return-event gathers the plural group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_b3ae9ee85f7d960099c1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:sound-closure","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_8677716412b069941356"],"title":"sharp return-noun onset and bound closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_2ccdae2b85b9bf03913a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:25:3:variant-and-expansion-contrast","source_type":"word_analysis","support_ids":["sup_2f387180687b5af4865d","sup_f03536da7644a772fe83"],"title":"variant apparatus highlights compact canonical wording","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:25:3","qac_refs":["88:25:3:1","88:25:3:2"],"status":"accepted"}},{"anchor_refs":["88:25:3"],"branch_refs":[],"candidate_id":"cand_c3db1708f7df9bb30738","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000065"],"scope":"focus_ayah","source_local_id":"88:25:3:1","source_type":"qac_morpheme","support_ids":["sup_f43d0161ef2b51cefe6d"],"title":"QAC root occurrence: ء و ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:25","branch_refs":["root_000065/B001"],"candidate_id":"cand_eaa3627c0a8949dbb768","commentary_obligation":"review","hft_ref":"hft_6e650ab81c0f69876496","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_return_as_gathering_point","source_type":"hft","support_ids":["sup_3db60bfcde263e2716e8"],"title":"baseline_return_as_gathering_point","trust":"legacy_unbound"},{"anchor_refs":["88:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:25","branch_refs":["root_000065/B004"],"candidate_id":"cand_f7808808c4d691c5fa5f","commentary_obligation":"review","hft_ref":"hft_6e2ac4b9d61d1d52436e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_many_quarters_one_destination","source_type":"hft","support_ids":["sup_28f84d3a542114988830"],"title":"baseline_many_quarters_one_destination","trust":"legacy_unbound"},{"anchor_refs":["88:25"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:25","branch_refs":["root_000065/B003"],"candidate_id":"cand_08d506b45cda59766291","commentary_obligation":"review","hft_ref":"hft_afcbe26627efffc33364","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_rhythmic_return","source_type":"hft","support_ids":["sup_849d326c5fc0c32f98f8"],"title":"baseline_rhythmic_return","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:25:1:1","qac_word_ref":"88:25:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:25:2:1","qac_word_ref":"88:25:2","root_ar":"","surface_ar":"إِلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:25:2:2","qac_word_ref":"88:25:2","root_ar":"","surface_ar":"نَآ"},{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","root_ar":"ء و ب","surface_ar":"إِيَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:25:3:2","qac_word_ref":"88:25:3","root_ar":"","surface_ar":"هُمْ"}],"word_analysis_qac_refs":[["88:25:1:1"],["88:25:2:1","88:25:2:2"],["88:25:3:1","88:25:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:25:1","88:25:2","88:25:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:25:1:1","qac_word_ref":"88:25:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:25:2:1","qac_word_ref":"88:25:2","root_ar":"","surface_ar":"إِلَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:25:2:2","qac_word_ref":"88:25:2","root_ar":"","surface_ar":"نَآ"},{"lemma_ar":"إِيَاب","morph_features":"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"88:25:3:1","qac_word_ref":"88:25:3","root_ar":"ء و ب","surface_ar":"إِيَابَ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"88:25:3:2","qac_word_ref":"88:25:3","root_ar":"","surface_ar":"هُمْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:25:1:1"],["88:25:2:1","88:25:2:2"],["88:25:3:1","88:25:3:2"]],"word_analysis_refs":["88:25:1","88:25:2","88:25:3"],"word_rows":[{"analysis_record_ref":"88:25:1","analytic_gloss_range_en":"emphatic annulling particle that certifies the whole fronted-predicate nominal clause as settled news","analytic_root_gloss_range_en":null,"qac_refs":["88:25:1:1"],"root":{},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"88:25:2","analytic_gloss_range_en":"fronted prepositional destination predicate: movement is routed to the divine speaker as endpoint and jurisdictional authority","analytic_root_gloss_range_en":null,"qac_refs":["88:25:2:1","88:25:2:2"],"root":{},"surface":{"arabic":"إِلَيْنَآ","transliteration":"ilaynā"}},{"analysis_record_ref":"88:25:3","analytic_gloss_range_en":"possessed masdar naming the warned group's return-event: a coming back to the divine endpoint, morally valenced by refusal and framed as the arrival stage before reckoning","analytic_root_gloss_range_en":"return and coming-back range, with related fields of homeward reversion, final resort, repeated return, and returner profile; the local surface selects the event noun rather than a place of return, a finite verb, or a praised returner title","qac_refs":["88:25:3:1","88:25:3:2"],"root":{"arabic":"أ و ب","transliteration":"ʾ-w-b"},"surface":{"arabic":"إِيَابَهُمْ","transliteration":"iyābahum"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["88:25"],"branch_refs":["root_000065/B001"],"candidate_id":"cand_eaa3627c0a8949dbb768","evidence_scope":"focus_ayah","hft_ref":"hft_6e650ab81c0f69876496","item_id":"baseline_return_as_gathering_point","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_return_as_gathering_point","support_id":"sup_3db60bfcde263e2716e8"},{"anchor_refs":["88:25"],"branch_refs":["root_000065/B004"],"candidate_id":"cand_f7808808c4d691c5fa5f","evidence_scope":"focus_ayah","hft_ref":"hft_6e2ac4b9d61d1d52436e","item_id":"baseline_many_quarters_one_destination","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_many_quarters_one_destination","support_id":"sup_28f84d3a542114988830"},{"anchor_refs":["88:25"],"branch_refs":["root_000065/B003"],"candidate_id":"cand_08d506b45cda59766291","evidence_scope":"focus_ayah","hft_ref":"hft_afcbe26627efffc33364","item_id":"baseline_rhythmic_return","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_rhythmic_return","support_id":"sup_849d326c5fc0c32f98f8"}],"diagnostics":[],"lane_counts":{"global":15,"macro":5,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:25","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:25","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"88:25","lane":"micro","linguistic_source_ref":"88:25","surface_ref":"88:25","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:25","target_tokens":[["Onların",["88:25:3"]],["dönüşü",["88:25:3"]],["kesinlikle",["88:25:1"]],["bizedir",["88:25:2"]]],"text":"Onların dönüşü kesinlikle bizedir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:endpoint-return-sound-link","source_type":"word_analysis","support_id":"sup_07d3348b3b7c9a581587","text":"{\"blocking_evidence\":null,\"headline\":\"endpoint and return are linked in adjacent sound\",\"reader_payoff\":\"The reader notices sound continuity between the destination phrase and the return noun, reinforcing their syntactic bond.\",\"reason\":\"The adjacent words {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) and {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) are syntactically bound as predicate and delayed noun, and the sound rows observe their adjacent i/yā-like pressure.\",\"representative_source_ids\":[\"QE-701032fa\",\"QP-c180ff1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:bound-speaker-reference","source_type":"word_analysis","support_id":"sup_257c82698080cc46bf67","text":"{\"blocking_evidence\":null,\"headline\":\"bound first-person suffix makes the endpoint immediate\",\"reader_payoff\":\"The reader notices that the destination is compressed into a bound first-person speaker-form and that the discourse moves from a named third-person agent to direct divine speech.\",\"reason\":\"The suffix in {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) is a surface first-person plural pronoun, and the previous ayah names {{ar:ٱللَّهُ}} ({{tr:allāhu}}) as the agent (88:24).\",\"representative_source_ids\":[\"QF-2bbfc105\",\"QF-6a3cfca5\",\"QI-d6eecce3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:delayed-return-under-endpoint","source_type":"word_analysis","support_id":"sup_26787dfdda11936d13ba","text":"{\"blocking_evidence\":null,\"headline\":\"return noun lands after certainty and endpoint\",\"reader_payoff\":\"The reader notices that the return noun is the closure point, arriving only after certainty and the divine endpoint have already framed it.\",\"reason\":\"The grammar makes {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) the delayed governed noun of {{ar:إِنَّ}} ({{tr:inna}}) after the fronted predicate {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}).\",\"representative_source_ids\":[\"QG-c6e18f56\",\"QI-4cac3505\",\"QT-9da5596a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3","source_type":"word_analysis","support_id":"sup_2f387180687b5af4865d","text":"{\"gloss_range\":\"possessed masdar naming the warned group's return-event: a coming back to the divine endpoint, morally valenced by refusal and framed as the arrival stage before reckoning\",\"prose\":\"{{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) closes the clause by naming the return as a possessed event: the plural suffix is attached to the masdar, so the return clings to the warned group as their own liability. Because the noun arrives after {{ar:إِنَّ}} ({{tr:inna}}) and the fronted {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}), the event is already certified and routed to Us before the group is named in the suffix. The root pressure is not generic motion; it is coming back after departure, so after the turning away of 88:23 the word gives refusal a reversal: voluntary aversion cannot cancel compulsory return. That return-field pressure can stand near repentance language, but the local endpoint keeps the meaning as return-to-authority, not repentance. The local form keeps this as a return-event, not a place of return like {{ar:مَآب}} ({{tr:maʾāb}}) or a praised returner profile like {{ar:أَوَّاب}} ({{tr:awwāb}}), and variant or expansion evidence only highlights the noun and suffix pressure without replacing the compact canonical clause. Its singular abstract form gathers the plural group into one owned return, the adjacent i/yā-like sound links endpoint and event before the suffix closes them, and 88:26 then turns the same group's return into {{ar:حِسَابَهُم}} ({{tr:ḥisābahum}}), their account.\",\"root_display\":\"{{ar:أ و ب}} ({{tr:ʾ-w-b}})\",\"root_gloss_range\":\"return and coming-back range, with related fields of homeward reversion, final resort, repeated return, and returner profile; the local surface selects the event noun rather than a place of return, a finite verb, or a praised returner title\",\"surface_display\":\"{{ar:إِيَابَهُمْ}} ({{tr:iyābahum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:return-not-generic-motion","source_type":"word_analysis","support_id":"sup_3788428e93b027d687c1","text":"{\"blocking_evidence\":null,\"headline\":\"coming back reverses prior turning away\",\"reader_payoff\":\"The reader notices return as reversal after departure and refusal, not as mere travel into an unspecified future.\",\"reason\":\"The CRITICAL rows tie the return field to the immediate prior turning-away scene (88:23), and no guardrail evidence contradicts the coming-back sense.\",\"representative_source_ids\":[\"QS-33f4cdad\",\"QS-3fd89af7\",\"ME-ee099499\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:fronted-restrictive-predicate","source_type":"word_analysis","support_id":"sup_37b10333da65135d26c8","text":"{\"blocking_evidence\":null,\"headline\":\"fronted endpoint governs how the return is heard\",\"reader_payoff\":\"The reader notices the endpoint before the return noun, so destination controls the clause before the event is named.\",\"reason\":\"The local syntax forces {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) as the fronted predicate before the delayed noun {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}), supporting endpoint focus and restriction without adding fallback routing.\",\"representative_source_ids\":[\"MG-ff052fda\",\"QT-7dad0ad0\",\"QI-ff5d0311\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:repentance-overlap-limited","source_type":"word_analysis","support_id":"sup_4285fc4da89d68e063f8","text":"{\"blocking_evidence\":null,\"headline\":\"return-field overlap without repentance sense\",\"reader_payoff\":\"The reader notices the strength of the return field while keeping the local meaning as return to authority rather than repentance.\",\"reason\":\"The derivational dispute can sharpen the return-field pressure, but the local endpoint frame selects return-to-authority and does not call the group repentant.\",\"representative_source_ids\":[\"QS-f63d72fb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:return-to-account-bridge","source_type":"word_analysis","support_id":"sup_493ed937a16de0c4ce06","text":"{\"blocking_evidence\":null,\"headline\":\"same speaker-frame moves from destination to responsibility\",\"reader_payoff\":\"The reader notices that the next ayah keeps the divine speaker-frame while turning arrival into reckoning responsibility.\",\"reason\":\"The bridge is local and concrete: 88:25 says return to Us, and 88:26 says account upon Us with the same first-person plural speaker-frame.\",\"representative_source_ids\":[\"QB-1978e556\",\"QB-ada7c414\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:possessed-return-event","source_type":"word_analysis","support_id":"sup_4cc3bd21432fce59c718","text":"{\"blocking_evidence\":null,\"headline\":\"possessed masdar binds the group to return\",\"reader_payoff\":\"The reader notices that the return is not an indefinite event; it is a defined liability attached to the group by the suffix.\",\"reason\":\"Attachment evidence marks the suffix of {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) as the genitive possessor of the masdar, with referent choice depending on the prior human discourse group.\",\"representative_source_ids\":[\"QG-2574624d\",\"QG-3cb36e05\",\"MG-fbba5909\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1:certified-return-proposition","source_type":"word_analysis","support_id":"sup_53fb730f87b546f986f7","text":"{\"blocking_evidence\":null,\"headline\":\"emphatic certification of the return claim\",\"reader_payoff\":\"The reader notices that the ayah grammatically certifies the return claim before treating it as a settled verdict, not an inferred threat.\",\"reason\":\"QAC and attachment evidence identify {{ar:إِنَّ}} ({{tr:inna}}) as the annulling emphatic particle governing the whole nominal clause.\",\"representative_source_ids\":[\"QG-3f6f6b99\",\"MG-efda6aaa\",\"QI-d2dc4f06\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:destination-endpoint","source_type":"word_analysis","support_id":"sup_5488aac0f89d0c8a92a4","text":"{\"blocking_evidence\":null,\"headline\":\"endpoint and authority fused in the destination phrase\",\"reader_payoff\":\"The reader notices that return is directed to a definite divine endpoint, not toward an unnamed place or vague future.\",\"reason\":\"Attachment evidence identifies the prepositional phrase with first-person plural suffix as the destination complement associated with the return.\",\"representative_source_ids\":[\"QG-2e8ef55a\",\"QG-37def9ef\",\"QS-01fee22b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:return-enables-account-bridge","source_type":"word_analysis","support_id":"sup_634cb9573fe7189ffe16","text":"{\"blocking_evidence\":null,\"headline\":\"arrival stage hands forward to account\",\"reader_payoff\":\"The reader notices that return is the arrival stage that creates the forward need for reckoning in 88:26.\",\"reason\":\"The next ayah (88:26) follows the return with account, keeping the same group and speaker-frame.\",\"representative_source_ids\":[\"QB-7e28ffdb\",\"QB-b1583a49\",\"QY-b8d9abd3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1","source_type":"word_analysis","support_id":"sup_712800e75b590e041d18","text":"{\"gloss_range\":\"emphatic annulling particle that certifies the whole fronted-predicate nominal clause as settled news\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) makes the three-word clause begin with certainty before either destination or return is named. Its governance reaches across the fronted predicate, so {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) receives focus while {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) remains the asserted noun under the particle. After the punitive action of 88:24, this emphatic nominal frame changes the register from narrated event to settled jurisdictional verdict: their return is not a possible sequel but certified news. The doubled sound of the particle gives that certainty audible weight, and the next ayah repeats the emphatic frame after {{ar:ثُمَّ}} ({{tr:thumma}}) (88:26), making return and reckoning two confirmed stages.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1:nominal-verdict-after-punishment","source_type":"word_analysis","support_id":"sup_728ceb83869eb16263fb","text":"{\"blocking_evidence\":null,\"headline\":\"event narration shifts into standing verdict\",\"reader_payoff\":\"The reader notices the move from punishment as narrated action in 88:24 to return as a standing jurisdictional proposition in 88:25.\",\"reason\":\"The row family is structural and is not contradicted: 88:24 has verbal punitive narration, while 88:25 is an emphatic nominal clause.\",\"representative_source_ids\":[\"QT-92ea2f26\",\"QB-5e31113a\",\"QB-ef083007\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:return-formula-echo","source_type":"word_analysis","support_id":"sup_81406d92623ee6245177","text":"{\"blocking_evidence\":null,\"headline\":\"return-to-divine-endpoint formula\",\"reader_payoff\":\"The reader notices that 88:25 participates in a wider return-to-divine-endpoint formula while selecting a more possessed return noun than 96:8.\",\"reason\":\"The inter-ayah row gives a concrete formula parallel in 96:8; the local wording keeps the endpoint pressure but uses {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) for the warned group's possessed return.\",\"representative_source_ids\":[\"MI-1a8c0330\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1:fronted-predicate-governance","source_type":"word_analysis","support_id":"sup_8220a08e77aca3f265a1","text":"{\"blocking_evidence\":null,\"headline\":\"governance across a reordered nominal clause\",\"reader_payoff\":\"The reader notices that certainty comes first, the endpoint receives fronted focus, and the return noun still remains the governed asserted noun.\",\"reason\":\"Attachment evidence marks {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) as the fronted predicate and {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) as the delayed governed noun of {{ar:إِنَّ}} ({{tr:inna}}).\",\"representative_source_ids\":[\"QG-df852fd5\",\"QT-97e4dfd3\",\"MT-02c4ae79\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:sound-closure","source_type":"word_analysis","support_id":"sup_8677716412b069941356","text":"{\"blocking_evidence\":null,\"headline\":\"sharp return-noun onset and bound closure\",\"reader_payoff\":\"The reader notices that the return noun enters sharply after the lengthened endpoint and closes on the attached group suffix.\",\"reason\":\"The sound rows describe the local surface of {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}), especially its hamza onset, long vowel movement, and suffixed closure.\",\"representative_source_ids\":[\"QF-5f360de2\",\"QP-855fe8ab\",\"MP-db9e28e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:masdar-not-finite-or-place","source_type":"word_analysis","support_id":"sup_86ec85b64532cdd28c0b","text":"{\"blocking_evidence\":null,\"headline\":\"event noun instead of verb, place, or repeated form\",\"reader_payoff\":\"The reader notices that return is objectified as a substantive fact inside the nominal clause rather than narrated as a timed action or named as a destination-place.\",\"reason\":\"QAC identifies the local word as a gerund/masdar, and the surrounding clause is nominal rather than a finite return verb.\",\"representative_source_ids\":[\"QF-724c46c5\",\"QF-74ae4d41\",\"QF-7c2db42e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:singular-abstract-plural-group","source_type":"word_analysis","support_id":"sup_9259d4b95fdc410e304d","text":"{\"blocking_evidence\":null,\"headline\":\"one return-event gathers the plural group\",\"reader_payoff\":\"The reader notices the discourse widening from a singular punished refuser to a plural group gathered into one possessed return-event.\",\"reason\":\"The suffix of {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}) is plural, while the previous punishment verse individualizes with a singular object (88:24).\",\"representative_source_ids\":[\"QF-f2d28f0b\",\"QI-d63eaee7\",\"QB-5fe46f11\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2","source_type":"word_analysis","support_id":"sup_95db8113b0faf313d183","text":"{\"gloss_range\":\"fronted prepositional destination predicate: movement is routed to the divine speaker as endpoint and jurisdictional authority\",\"prose\":\"{{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) is not a loose setting for the return; it is the fronted destination predicate. The preposition gives the movement an endpoint, and the attached first-person plural suffix makes that endpoint the speaking divine authority. Because the phrase comes before {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}), the reader meets the destination first and only then the return-event, so the return is heard as already confined to Us rather than open-ended. The shift from third-person {{ar:ٱللَّهُ}} ({{tr:allāhu}}) in 88:24 to {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) in 88:25 turns the named punishing agent into the immediate speaking destination. The same return-to-divine-endpoint pressure appears in the formula of 96:8, but this ayah makes it the possessed return of the warned group; 88:26 then changes the same speaker-frame from return to Us into account upon Us.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِلَيْنَآ}} ({{tr:ilaynā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:2:cadenced-endpoint","source_type":"word_analysis","support_id":"sup_c4d8f4dff60e8ce71a9b","text":"{\"blocking_evidence\":null,\"headline\":\"lengthened endpoint before the compact return noun\",\"reader_payoff\":\"The reader notices the endpoint lingering in recitation before the return noun closes the clause.\",\"reason\":\"The sound rows track the final length of {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}) as a local recitational effect before {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}).\",\"representative_source_ids\":[\"QF-6e66e51e\",\"QP-dac0f652\",\"MP-1c4ddc9c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1:return-and-account-certification","source_type":"word_analysis","support_id":"sup_c54365c044d4a0a07ae5","text":"{\"blocking_evidence\":null,\"headline\":\"return and reckoning as paired certified stages\",\"reader_payoff\":\"The reader notices that 88:25 and 88:26 share an emphatic frame, so return and accounting are heard as linked certified stages.\",\"reason\":\"The forward bridge is concrete: the next ayah repeats the assertion particle after {{ar:ثُمَّ}} ({{tr:thumma}}) (88:26).\",\"representative_source_ids\":[\"QB-474f0e15\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:returner-to-account-patient","source_type":"word_analysis","support_id":"sup_c96a938750bf40ec73f2","text":"{\"blocking_evidence\":null,\"headline\":\"returning subject becomes reckoned patient\",\"reader_payoff\":\"The reader notices the same group first owning the return-event in 88:25 and then facing account in 88:26.\",\"reason\":\"The local construct makes the group possess or perform the return, while the forward row identifies the same suffix group in the account noun of 88:26.\",\"representative_source_ids\":[\"QG-5cfd35ec\",\"QS-7c71c026\",\"QB-371a2fad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:accountability-valenced-homecoming","source_type":"word_analysis","support_id":"sup_ce72dfc2730ab499eb5f","text":"{\"blocking_evidence\":null,\"headline\":\"homeward return becomes answerable arrival\",\"reader_payoff\":\"The reader notices that the ordinary image of coming back is morally charged by refusal, punishment, and the divine endpoint.\",\"reason\":\"The return-event is locally framed by {{ar:إِلَيْنَآ}} ({{tr:ilaynā}}), preceded by refusal and punishment, and followed by accounting in 88:26.\",\"representative_source_ids\":[\"QS-448f2ad7\",\"QS-95768a1e\",\"QS-9b42853c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:1:opening-sound-weight","source_type":"word_analysis","support_id":"sup_d0570e0cfb9392f41629","text":"{\"blocking_evidence\":null,\"headline\":\"audible weight of the opening assertion\",\"reader_payoff\":\"The reader notices that the opening certainty is also heard as a compressed, weighty onset before the destination phrase arrives.\",\"reason\":\"The sound observation is local to the recited surface of {{ar:إِنَّ}} ({{tr:inna}}) and does not alter the grammar.\",\"representative_source_ids\":[\"QF-fdb374dc\",\"QP-5a9a0109\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:root-family-limits","source_type":"word_analysis","support_id":"sup_ee92257a4a845c39b9f0","text":"{\"blocking_evidence\":null,\"headline\":\"related root forms stay as contrast, not replacements\",\"reader_payoff\":\"The reader notices that the word draws on the return field while choosing the event noun instead of a place-of-return noun or a praised repeated-returner title.\",\"reason\":\"V4 has no guardrail rows for this root, so absence cannot reject the family pressure; local grammar narrows the payoff to the surface event noun {{ar:إِيَابَهُمْ}} ({{tr:iyābahum}}), not {{ar:مَآب}} ({{tr:maʾāb}}) or {{ar:أَوَّاب}} ({{tr:awwāb}}).\",\"representative_source_ids\":[\"QS-9311c7ce\",\"QS-af4e19f8\",\"QS-fc8c89ac\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:variant-and-expansion-contrast","source_type":"word_analysis","support_id":"sup_f03536da7644a772fe83","text":"{\"blocking_evidence\":null,\"headline\":\"variant apparatus highlights compact canonical wording\",\"reader_payoff\":\"The reader notices that variant and expansion evidence highlights the pressure points of the return noun and suffix without replacing the canonical three-word clause.\",\"reason\":\"The variants are useful as contrast: they do not change the local destination syntax or require adding an explicit referent to the canonical suffix.\",\"representative_source_ids\":[\"QF-4d6b3f38\",\"QF-8941c7dc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:25:3:1","source_type":"qac_morpheme","support_id":"sup_f43d0161ef2b51cefe6d","text":"{\"lemma_ar\":\"إِيَاب\",\"morph_features\":\"STEM|POS:N|LEM:<iyaAb|ROOT:Awb|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:25:3:1\",\"qac_word_ref\":\"88:25:3\",\"root_ar\":\"ء و ب\",\"surface_ar\":\"إِيَابَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:25:3:rare-dense-closure","source_type":"word_analysis","support_id":"sup_fe6568437333a47ae53d","text":"{\"blocking_evidence\":null,\"headline\":\"rare event noun concentrates the clause closure\",\"reader_payoff\":\"The reader notices that the unusual return-event form makes the tiny clause lexically dense at its closing point.\",\"reason\":\"The contextual profile marks the exact root and form as a single low-occurrence instance, while the missing V4 root note prevents overclaiming from dictionary absence.\",\"representative_source_ids\":[\"QH-85118749\",\"QH-a52970b5\",\"QY-6793cdcb\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000065/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000065","role":"Return to a return-place supplies both the homeward motion and its terminal gathering function.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"changed_reading":{"after":"Their return is a collective convergence whose very return-place is with Us.","before":"They will come back to Us."},"confidence":"strong","focus_anchor":"The nominal إِيَابَهُمْ is governed by the fronted destination إِلَيْنَا.","mechanism":"The return-place branch lets إياب name both movement back and the point at which dispersed persons gather. Fronting إِلَيْنَا makes the destination constitutive of the event: this is not motion in general but their convergence upon Us.","model_id":"baseline_return_as_gathering_point"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_return_as_gathering_point","source_type":"hft","support_id":"sup_3db60bfcde263e2716e8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000065/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000065","role":"The image of a quarter from which one comes turns the plural return into convergence from multiple directions.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"changed_reading":{"after":"However divergent their quarters and orientations, every line of arrival closes upon Us.","before":"All of them share a destination."},"confidence":"medium","focus_anchor":"The plural suffix in إِيَابَهُمْ is drawn through the singular deictic vector إِلَيْنَا.","mechanism":"The quarter-or-direction branch keeps the plurality spatially live: their arrivals may issue from many orientations, yet the fronted إِلَيْنَا collapses those quarters into one endpoint.","model_id":"baseline_many_quarters_one_destination"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_many_quarters_one_destination","source_type":"hft","support_id":"sup_28f84d3a542114988830","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000065/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000065","role":"Rhythmic return of limbs in travel gives the return an iterative, embodied interior.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"changed_reading":{"after":"Their return gathers the repeated motions and exertions by which their whole course was traveled.","before":"Their return is one terminal transition."},"confidence":"exploratory","focus_anchor":"The event noun إِيَاب can retain an internal texture of recurrent travel rather than only its endpoint.","mechanism":"The branch of limbs repeatedly returning in travel expands إياب into accumulated back-and-forth exertion. The final return gathers a history of repeated bodily motions, not merely a single last reversal.","model_id":"baseline_rhythmic_return"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_rhythmic_return","source_type":"hft","support_id":"sup_849d326c5fc0c32f98f8","trust":"legacy_unbound"}]}
</lane_packet_json>
