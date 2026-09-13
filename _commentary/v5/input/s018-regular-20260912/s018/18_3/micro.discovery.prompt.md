# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **18:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s018-regular-20260912/s018/18_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "18:3",
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
{"analysis_context":{"analysis_id":"s018-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"18:3","host_surah":18,"lane_context_refs":[],"ordered_context_refs":["18:1","18:2","18:4","18:5","18:6","18:7","18:8","18:9","18:10","18:11","18:12","18:13","18:14","18:15","18:16","18:17","18:18","18:19","18:20","18:21","18:22","18:23","18:24","18:25","18:26","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek zaman bakımından sonsuz ya da çok uzun sürmedir; kalıcı kılma bunun ettirgen uzantısıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000004/B001","candidate_links":[{"candidate_id":"cand_af2dad8902ad52c2b1c0","lane":"micro"},{"candidate_id":"cand_e02d95e4b8091a1a30c4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"sonsuz süre ve kalıcı kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sonu belirlenmeyen, çok uzun veya kesintisiz bir zaman süresini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Pekiştirici zaman kalıplarında bütün çağlar boyunca sürme anlamı öne çıkar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi sürekli, devredilemez veya sona erdirilemez duruma getirmeyi de kapsar."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zaman çekirdeği ile bir şeyi sürekli duruma getiren uzantıyı birlikte özetleyen üst karşılıktır.","boundary_detail":"Çekirdek zaman bakımından sonsuz ya da çok uzun sürmedir; kalıcı kılma bunun ettirgen uzantısıdır.","branch_image_ar":"طول المدة والدوام","concept_gloss":"sonsuz süre ve kalıcı kılma","contextual_glosses":[{"applicability":"Bütün zaman boyunca süren eylem ve durumları anlatan pekiştirici kalıplarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zamanın son sınırı bulunmadığı düşüncesini korur."},"facet_ids":["F001","F002"],"text":"sonsuza dek","usage_role":"contextual"},{"applicability":"Bir malı, düzenlemeyi veya durumu sürekli ve değişmez hale getiren türemiş biçimlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürekliliğin bir şeye kazandırılması işlemini korur."},"facet_ids":["F003"],"text":"kalıcı kılma","usage_role":"contextual"}],"definition":"Bir sürenin son sınır düşünülmeden uzaması veya bütün zaman boyunca devam etmesi; ayrıca bir şeyi bu biçimde sürekli ve değişmez kılma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sonu belirlenmeyen, çok uzun veya kesintisiz bir zaman süresini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Pekiştirici zaman kalıplarında bütün çağlar boyunca sürme anlamı öne çıkar."},{"facet_id":"F003","role":"extension","statement":"Bir şeyi sürekli, devredilemez veya sona erdirilemez duruma getirmeyi de kapsar."}],"identity_rationale":"Kaynak ifadesi uzun ve kesintisiz süreyi, bütün zaman boyunca sürmeyi ve bir şeyi kalıcı duruma getirmeyi birlikte destekler. Geçici kalış, yabanıllaşma ve ıssızlaşma bu dalın çekirdeğine girmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sonsuz zaman, çok uzun süre"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sonsuza dek, kesintisiz olarak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çağlar boyunca, sonsuza dek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bütün zaman boyunca"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kalıcı kılma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"sürekli kılınmış, devredilemez"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sonsuza dek veya çok uzun süre kalmak"}],"lexicalization_note":"Yalın zaman adı ile süreyi pekiştiren kalıplar ve kalıcı kılmayı bildiren türemiş biçimler ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zaman çekirdeğinin sınırını en açık gösteren iki yakın komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal uzun süre ve kalıcı kılma uzantısını kapsarken komşu dal zamanın kesintisiz bağlantısını merkez alır.","focus_only":"Bir şeyi sürekli ve değişmez kılmaya uzanan türemiş kullanım da bu dalda bulunur.","gloss":"kesintisiz zaman","neighbor_only":"Komşu dal, zamanın parçalarının birbirine bağlanmış kesintisizliği görüntüsünü özellikle öne çıkarır.","neighbor_ref":"root_000695/B005","relation_type":"near_synonym","shared_zone":"İki dal da son sınırı düşünülmeyen sürekli zamanı anlatır."},{"boundary_match":"partial","distinction":"Komşu dal geniş anlamda zaman ve uzun süreyi kapsar; odak dal ise sınırsız devamı ve ondan türeyen kalıcılığı belirginleştirir.","focus_only":"Sürenin son sınırının bulunmaması ve kalıcı kılma uzantısı odak dala özgüdür.","gloss":"uzun zaman","neighbor_only":"Komşu dal sıradan zaman, yaşam süresi veya dünyanın süresi gibi sonlu uzantıları da kapsar.","neighbor_ref":"root_000494/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de uzun bir zaman dilimini gösterebilir."}],"source_phrase_ar":"طول المدة (maqayis)؛ الأبد الدهر (maqayis;sihah)؛ أبد الآبدين وأبد الدهر (tahdhib)؛ الأبد الدائم والتأبيد التخليد (sihah)؛ مدة الزمان الممتد (mufradat)؛ وقفا مؤبدا وتأبيدا (tahdhib)","source_summary":"Kaynaklar dalı uzun zaman, sürekli devam ve bir şeyi kalıcı kılma çevresinde ortaklaştırır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الأبد والآباد وأبد الآبدين وأبد الدهر والدوام والتأبيد والتخليد وما جعل مؤبدا","what_is_not_ar":"ليس التوحش ولا خلو المنزل ولا الإبد الولود ولا الغضب"},"support_links":["sup_3739a293fcc71e9f2836","sup_f0a2c8786e47e0eb77be"]},{"boundary":"Dal, özellikle hayvanın insan çevresinden koparak yabanıllaşması ve insandan ürkmesiyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000004/B002","candidate_links":[{"candidate_id":"cand_93ce5f419863cf101634","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"yabanıllaşıp insandan ürkme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evcil ya da insana alışık bir hayvanın yabanıl duruma geçmesini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu değişim insandan ürkme, kaçınma ve yabani hayvanlara benzeme ile görünür olur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş adlar yabanıl, ürkek hayvanların kendisini de gösterebilir."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın evcil çevreden kopuşunu ve bunun insana karşı ürkeklik sonucunu birlikte karşılar.","boundary_detail":"Dal, özellikle hayvanın insan çevresinden koparak yabanıllaşması ve insandan ürkmesiyle sınırlıdır.","branch_image_ar":"التوحش والنفور","concept_gloss":"yabanıllaşıp insandan ürkme","contextual_glosses":[{"applicability":"Süreci değil, insanlara alışık olmayan ürkek hayvanları adlandıran çoğul biçimlerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsandan uzak duran yabanıl hayvan sınıfını korur."},"facet_ids":["F003"],"text":"yabani hayvanlar","usage_role":"contextual"}],"definition":"Bir hayvanın insana alışıklığını yitirerek yabanıllaşması, insanlardan ürküp kaçınması veya bu durumdaki yabanıl hayvanlardan olması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evcil ya da insana alışık bir hayvanın yabanıl duruma geçmesini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Bu değişim insandan ürkme, kaçınma ve yabani hayvanlara benzeme ile görünür olur."},{"facet_id":"F003","role":"extension","statement":"Türemiş adlar yabanıl, ürkek hayvanların kendisini de gösterebilir."}],"identity_rationale":"Kaynak ifadesi deve ve başka hayvanların insana alışıklığını yitirip yabani hayvanlar gibi ürkekleşmesini açıkça bir arada verir. Salt uzaklaşma, yerinde kalma veya zaman bakımından sürme bu kimliğe dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"devenin yabanıllaşması"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"hayvanın yabanıllaşıp insandan ürkmesi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yabani ve ürkek hayvanlar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yabani inek"}],"lexicalization_note":"Hayvanla kurulan eylem kalıpları ile yabanıl hayvanları adlandıran biçimler ayrılarak tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yabanıllaşma ile genel ürkme arasındaki sınırı gösteren iki komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hayvanın insandan ürkerek yabanıllaşma sürecini belirtir; komşu dal daha geniş katılımcılara uygulanabilen bir niteliktir.","focus_only":"Odak dal, insana alışıklığını yitiren deve ve başka hayvanlar ile bunların adlarına bağlanır.","gloss":"yabanıllık","neighbor_only":"Komşu dal insanları ve kuşları da içine alan daha geniş bir yabanıllık niteliğidir.","neighbor_ref":"root_000955/B006","relation_type":"near_synonym","shared_zone":"İki dal da alışılmış insan çevresinin dışına çıkıp yabanıllaşmayı anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel kaçınma ve uzaklaşma hareketidir; odak dal bu hareketi insana alışıklığın yitirilmesiyle oluşan yabanıllığa bağlar.","focus_only":"Yabanıl hayvan durumuna geçiş ve bu hayvanların adı odak dalda bulunur.","gloss":"ürküp uzaklaşma","neighbor_only":"Komşu dal herhangi bir şeyden ya da doğrudan uzaklaşmayı ve başkasını uzaklaştırmayı da kapsar.","neighbor_ref":"root_001532/B001","relation_type":"near_neighbor","shared_zone":"Hayvanın ürkerek bir şeyden uzaklaşması iki dalın ortak alanıdır."}],"source_phrase_ar":"تأبد البعير توحش (maqayis;mufradat)؛ أوابد كأوابد الوحش (maqayis;tahdhib)؛ أبدت البهيمة أي توحشت (sihah)؛ توحشت ونفرت من الإنس (tahdhib)؛ الوحشيات (mufradat)","source_summary":"Kaynaklar hayvanın yabanıllaşmasını, insandan ürkmesini ve yabanıl hayvan adıyla anılmasını ortak bir anlam alanında birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"توحش البهيمة والبعير والولد ونفورها من الإنس وكونها من الأوابد أو الوحشيات","what_is_not_ar":"ليس مجرد الإقامة بالمكان ولا خلو المنزل ولا الدوام الزماني"},"support_links":["sup_abd45caed90f8ffb2e9e"]},{"boundary":"Anlam yalnızca terk edilen ev veya yerleşim kalıbına bağlıdır; genel bir boşluk ya da yabanıllık anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000004/B003","candidate_links":[{"candidate_id":"cand_93ce5f419863cf101634","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"terk edilip ıssızlaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evin veya yerleşimin sakinlerinden boşalarak ıssız kalmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanların ardından yabani hayvanların yeri benimsemesi sürecin sonucu olarak belirtilir."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ev veya yerleşimin insanlardan boşalmasını ve terk edilmiş duruma gelmesini karşılayan kalıp anlamıdır.","boundary_detail":"Anlam yalnızca terk edilen ev veya yerleşim kalıbına bağlıdır; genel bir boşluk ya da yabanıllık anlamı değildir.","branch_image_ar":"خلو المنزل وإقفاره","concept_gloss":"terk edilip ıssızlaşmak","contextual_glosses":[{"applicability":"Terk edilmiş yerin insanlardan sonra yabani hayvanlarca kullanılmasını özellikle belirtir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Terk edilmenin ardından gelen hayvan yerleşimini korur."},"facet_ids":["F002"],"text":"yabani hayvanlara kalmak","usage_role":"explanatory"}],"definition":"Bir evin ya da yerleşimin sakinleri ayrıldıktan sonra boşalıp ıssızlaşması ve yabani hayvanların uğradığı bir yere dönüşmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evin veya yerleşimin sakinlerinden boşalarak ıssız kalmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"İnsanların ardından yabani hayvanların yeri benimsemesi sürecin sonucu olarak belirtilir."}],"identity_rationale":"Kaynak ifadesi bir evin ya da yerleşimin sakinlerince terk edilmesini, ıssız kalmasını ve ardından yabani hayvanların oraya yerleşmesini birlikte verir. Bu, hayvanın kendisinin yabanıllaşmasından farklı bir yer durumu ve süreçtir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"evin terk edilip ıssızlaşması ve yabani hayvanlara kalması"}],"lexicalization_note":"Tanım, terk edilen ev veya yerleşimle kurulan kalıba bağlı tutulur ve yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; terk edilmiş konut anlamını genel ıssızlık ve boşluktan ayıran iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bir evin terk edilip hayvanlara kalma sürecidir; komşu dal daha geniş yer türlerini ve duygusal yalnızlığı da kapsayan bir durum alanıdır.","focus_only":"Odak dal, sakinlerin ayrılmasından sonra yabani hayvanların yeri benimsemesi sonucunu içerir.","gloss":"ıssız yer","neighbor_only":"Komşu dal ülke, arazi, ev ve yıkıntılar yanında yalnızlıktan doğan iç sıkıntısını da kapsar.","neighbor_ref":"root_001632/B002","relation_type":"near_synonym","shared_zone":"İki dal da insanların bulunmadığı boş ve ürkütücü bir yeri anlatır."},{"boundary_match":"partial","distinction":"Komşu dal genel boşluk ve işlevsizliği anlatır; odak dal insan konutunun terk edilerek ıssızlaşmasıyla sınırlıdır.","focus_only":"Terk edilen yerin ıssızlaşıp yabani hayvanlara kalması odak dala özgüdür.","gloss":"boş ve işlemez kalma","neighbor_only":"Komşu dal kuyu, sürü, görev, sınır ve üretim gibi çok farklı şeylerin ilgilisiz ya da işlemez kalmasını kapsar.","neighbor_ref":"root_001027/B001","relation_type":"near_neighbor","shared_zone":"Bir yerin sakin veya görevli bulunmaması iki dalda da görülebilir."}],"source_phrase_ar":"تأبد المنزل خلا (maqayis)؛ تأبد المنزل أي أقفر وألفته الوحوش (sihah)؛ خلا منها أهلها خلفتهم الوحش بها قد تأبدت (tahdhib)","source_summary":"Kaynaklar sakinlerin ayrılmasıyla evin boş ve ıssız kalmasını, ardından yabani hayvanların oraya gelmesini ortak biçimde aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"تأبد المنزل أو الدار إذا خلا أهلها وأقفر المكان وخلفتهم الوحوش فيه","what_is_not_ar":"ليس توحش الحيوان نفسه ولا الإقامة بالمكان"},"support_links":["sup_abd45caed90f8ffb2e9e"]},{"boundary":"Dal, belirtilen dişi katılımcıların her yıl ürün vermesi veya doğurması niteliğiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000004/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"her yıl doğuran dişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir dişinin düzenli ve özellikle her yıl doğurma niteliğini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi eşek, kısrak ve köle kadın kaynakta bu niteliğin katılımcıları olarak sayılır."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düzenli yavru veren dişi hayvanı veya kaynakta aynı nitelikle anılan kadını gösterir.","boundary_detail":"Dal, belirtilen dişi katılımcıların her yıl ürün vermesi veya doğurması niteliğiyle sınırlıdır.","branch_image_ar":"الإبد الولود","concept_gloss":"her yıl doğuran dişi","contextual_glosses":[{"applicability":"Dişi hayvanın tekrarlanan ve verimli doğurma niteliğinin cümle içinde aktarılmasına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tekrarlanan doğurma ve yavru verme özelliğini korur."},"facet_ids":["F001"],"text":"düzenli yavrulayan","usage_role":"contextual"}],"definition":"Dişi eşek, kısrak veya köle kadın gibi her yıl doğuran ve düzenli yavru veren dişi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir dişinin düzenli ve özellikle her yıl doğurma niteliğini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Dişi eşek, kısrak ve köle kadın kaynakta bu niteliğin katılımcıları olarak sayılır."}],"identity_rationale":"Kaynak ifadesi dişi eşek, kısrak ve köle kadın gibi dişilerin düzenli, özellikle her yıl doğurmasını bu adın belirleyici özelliği olarak verir. Sürü, damızlık erkek veya yalnızca çok çocuk sahibi olma anlamları bu dalın çekirdeği değildir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"her yıl doğuran dişi eşek, kısrak veya köle kadın"}],"lexicalization_note":"Yalın ad, düzenli doğuran dişiyi gösterir; komşu üreme kalıplarından ek anlam alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; düzenli doğurganlığın yakın alanını ve karşıt durumunu gösteren iki ilişki seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal farklı dişilerin her yıl doğurmasına dayanır; komşu dal yalnız kadınlarda çocuk sayısının çokluğunu öne çıkarır.","focus_only":"Odak dal yıllık doğurma düzenini ve dişi hayvanları da kapsayan bir sınıf adını bildirir.","gloss":"çok doğuran kadın","neighbor_only":"Komşu dal çok çocuk doğuran kadını ve doğurmanın çokluğunu saçılma görüntüsüyle anlatır.","neighbor_ref":"root_001472/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir dişinin tekrarlanan doğurganlığını anlatır."},{"boundary_match":"opposed","distinction":"Odak dal düzenli doğumun olumlu kutbudur; komşu dal gebelik ve ürün vermenin kesildiği karşıt kutuptur.","focus_only":"Odak dal dişinin her yıl doğurmasını ve verimliliğini bildirir.","gloss":"doğuran ve kısır kalan","neighbor_only":"Komşu dal dişinin bir yıl veya daha uzun süre gebe kalmamasını bildirir.","neighbor_ref":"root_000373/B007","relation_type":"polarity_pair","shared_zone":"İki dal dişi hayvanın yıllık üreme durumunu karşıt yönlerden sınıflandırır."}],"source_phrase_ar":"الإبد ذات النتاج من المال كالأمة والفرس والأتان (maqayis)؛ الابد الولود من أمة أو أتان (sihah)؛ أتان إبد في كل عام تلد (tahdhib)","source_summary":"Kaynaklar adı, çeşitli dişiler arasında düzenli ve her yıl doğuran bireyin niteliği olarak ortak biçimde tanımlar.","sources":["MQ","SI","TA"],"what_is_ar":"الإبد من المال كالأتان والأمة والفرس التي تلد أو تنتج في كل عام","what_is_not_ar":"ليس الأبد بمعنى الدهر ولا الأوابد الوحشية"},"support_links":[]},{"boundary":"Yüzün görünüşündeki olumsuz değişim çekirdektir; öfke yalnızca aktarılan bir yorum olarak korunur.","branch_kind":"collocation","branch_ref":"root_000004/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"yüzün lekelenip sertleşmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzün lekeli veya rengi değişmiş bir görünüm almasını bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yüzün yabanıl, sert ve alışılmadık bir görünüm alması biçiminde de açıklanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzdeki bu değişim bir açıklamada öfkelenme olarak yorumlanır."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yüz kalıbındaki görünür ve olumsuz değişimin iki temel açıklamasını birlikte özetler.","boundary_detail":"Yüzün görünüşündeki olumsuz değişim çekirdektir; öfke yalnızca aktarılan bir yorum olarak korunur.","branch_image_ar":"تأبد الوجه وتغيره","concept_gloss":"yüzün lekelenip sertleşmesi","contextual_glosses":[{"applicability":"Yüzdeki değişimi öfke ile açıklayan kaynak varyantının cümle içindeki karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfke yorumunu ve bunun yüzde görünmesini birlikte korur."},"facet_ids":["F003"],"text":"yüzü öfkeden değişmek","usage_role":"contextual"}],"definition":"Yüzün lekelenerek, rengi değişerek veya yabanıl ve sert bir görünüm alarak olumsuz biçimde değişmesi; bir yorumda bu görünüm öfkeye bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzün lekeli veya rengi değişmiş bir görünüm almasını bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Yüzün yabanıl, sert ve alışılmadık bir görünüm alması biçiminde de açıklanır."},{"facet_id":"F003","role":"source_variant","statement":"Yüzdeki bu değişim bir açıklamada öfkelenme olarak yorumlanır."}],"identity_rationale":"Kaynak ifadesi aynı yüz kalıbını bir yanda lekelenme, öte yanda yabanıl veya sert bir görünüm alma biçiminde açıklar; öfkelenme ise ikinci açıklamanın ayrıca verilen yorumudur. Bu yüzden dal yüzün görünür değişimini çekirdek almalı, öfkeyi zorunlu anlam değil kaynak varyantı saymalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yüzün lekelenmesi, sertleşmesi veya öfkeden değişmesi"}],"lexicalization_note":"Anlam yalnız yüzle kurulan kalıba bağlıdır; genel değişme veya genel öfkelenme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yüz değişimi çekirdeğini ve öfke yorumunun sınırlı yerini gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel yüz ve renk değişimini anlatır; odak dal belirli kalıpta lekelenme, yabanıl görünüm ve öfke yorumunu bir arada tutar.","focus_only":"Odak dal yalnız belirli yüz kalıbında lekelenme ve yabanıl sertlik varyantlarını taşır.","gloss":"yüz renginin değişmesi","neighbor_only":"Komşu dal kaygı veya savaş gibi nedenlerle yüzün asılması ve rengin genel değişmesini kapsar.","neighbor_ref":"root_000754/B007","relation_type":"near_synonym","shared_zone":"İki dalda da yüzün rengi veya görünüşü olumsuz yönde değişir."},{"boundary_match":"partial","distinction":"Komşu dal doğrudan öfke izidir; odak dalda öfke yalnız bir yorumdur ve yüz değişiminin diğer açıklamaları da vardır.","focus_only":"Lekelenme ve yabanıl sertlik öfkeden bağımsız olarak da odak dalda bulunur.","gloss":"öfkeli yüz izi","neighbor_only":"Komşu dal yalnız öfkenin yüzde bıraktığı görünür izi merkez alır.","neighbor_ref":"root_000198/B006","relation_type":"near_neighbor","shared_zone":"Öfkenin yüz görünümünü değiştirmesi iki dalın kesişme alanıdır."}],"source_phrase_ar":"تأبد وجهه كلف (maqayis)؛ تأبد وجه فلان توحش وقد فسر بغضب (mufradat)","source_summary":"Toplu kanıt yüzün lekelenmesi ile yabanıl veya sert görünmesi arasında değişen açıklamalar sunar; öfke de ikinci açıklamaya bağlı bir yorumdur.","sources":["MQ","MU"],"what_is_ar":"تأبد الوجه إذا تغير بالوحشة أو الكلف أو فسر بالغضب","what_is_not_ar":"ليس توحش البهيمة ولا غضب الرجل المجرد إلا عند من فسره بذلك"},"support_links":[]},{"boundary":"Çekirdek belirli bir yerde kalıp ayrılmamaktır; kuşların yıl boyu aynı yerde bulunması bunun adlaşmış uzantısıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000004/B006","candidate_links":[{"candidate_id":"cand_af2dad8902ad52c2b1c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"bir yerde kalıp ayrılmama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin veya canlının belirli bir yerde kalıp oradan ayrılmamasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kış ve yaz boyunca aynı arazide kalan kuşlar bu yerleşikliğin özel örneğidir."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer tamlayıcılı eylemin kalış ve ayrılmama bileşenlerini birlikte karşılayan genel açıklamadır.","boundary_detail":"Çekirdek belirli bir yerde kalıp ayrılmamaktır; kuşların yıl boyu aynı yerde bulunması bunun adlaşmış uzantısıdır.","branch_image_ar":"الإقامة وعدم البراح","concept_gloss":"bir yerde kalıp ayrılmama","contextual_glosses":[{"applicability":"Kış ve yaz boyunca aynı arazide kalan, göç etmeyen kuşları adlandırırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuşların yıl boyu aynı yerde kalması özelliğini korur."},"facet_ids":["F002"],"text":"yerleşik kuşlar","usage_role":"contextual"}],"definition":"Bir yerde kalmak ve oradan ayrılmamak; ayrıca kış ve yaz boyunca aynı arazide kalan kuşları bu yerleşiklikleriyle adlandırmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin veya canlının belirli bir yerde kalıp oradan ayrılmamasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Kış ve yaz boyunca aynı arazide kalan kuşlar bu yerleşikliğin özel örneğidir."}],"identity_rationale":"Kaynak ifadesi bir yerde kalmayı ve oradan ayrılmamayı açıkça verir; aynı anlam, kış ve yaz boyunca aynı arazide kalan kuşlara da uygulanır. Bu dal genel zamansal sonsuzluk değil, belirli bir yerde sürekli bulunmadır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir yerde kalıp oradan ayrılmamak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kış yaz aynı arazide kalan kuşlar"}],"lexicalization_note":"Yer tamlayıcılı kalış kalıbı ile aynı arazide yıl boyu kalan kuşları gösteren birim ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yerinde kalma ile mevsimsel kalış arasındaki sınırı gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler büyük ölçüde örtüşür; odak dal yerleşik kuşlara, komşu dal ise belirli yerde kalan develere uzanan farklı özelleşmeler taşır.","focus_only":"Yıl boyunca aynı arazide kalan kuşlara ait adlaşmış kullanım odak dalda bulunur.","gloss":"bir yerde kalmak","neighbor_only":"Komşu dal develerin belirli bir otlak türünde kalmasını ayrıca kapsar.","neighbor_ref":"root_000026/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir yerde kalmayı ve oradan ayrılmamayı bildirir."},{"boundary_match":"partial","distinction":"Komşu dal kışla sınırlı mevsimsel bir çerçevedir; odak dalın yerinde kalma anlamı mevsimle sınırlı değildir.","focus_only":"Odak dal bütün mevsimler boyunca aynı yerde kalabilmeyi içerir.","gloss":"kışlamak","neighbor_only":"Komşu dal kış mevsiminin gelmesi, kışı geçirme ve kışlama yeri gibi mevsime bağlı anlamları kapsar.","neighbor_ref":"root_000776/B002","relation_type":"near_neighbor","shared_zone":"Bir yerde kış boyunca kalma iki dalın kesiştiği kullanım alanıdır."}],"source_phrase_ar":"أبد بالمكان أي أقام به (sihah)؛ أبدت بالمكان إذا أقمت به ولم تبرحه (tahdhib)؛ الطير المقيمة بأرض شتاءها وصيفها أوابد (tahdhib)","source_summary":"Kaynaklar belirli bir yerde kalıp ayrılmamayı ortak çekirdek sayar ve yıl boyu aynı arazide yaşayan kuşları özel kullanım olarak verir.","sources":["SI","TA"],"what_is_ar":"أبد بالمكان إذا أقام به ولم يبرحه والطير المقيمة بأرض شتاءها وصيفها","what_is_not_ar":"ليس الدوام المطلق ولا التوحش والنفور"},"support_links":["sup_f0a2c8786e47e0eb77be"]},{"boundary":"Olayın sıra dışılığı ile anısının uzun süre kalması birlikte zorunludur.","branch_kind":"mixed_non_bare","branch_ref":"root_000004/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"uzun süre anılan olağanüstü olay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Olağanüstü veya şaşırtıcı bir işin uzun süre anılmasını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem kalıbı, anısı kalacak ölçüde sıra dışı bir iş ortaya koymayı anlatır."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olayın sıra dışılığını ve bellekte kalıcılığını birlikte taşıyan en kapsamlı doğal karşılıktır.","boundary_detail":"Olayın sıra dışılığı ile anısının uzun süre kalması birlikte zorunludur.","branch_image_ar":"الآبدة الباقية الذكر","concept_gloss":"uzun süre anılan olağanüstü olay","contextual_glosses":[{"applicability":"Bir kişinin anısı kalacak kadar sıra dışı bir iş ortaya koymasını anlatan eylem kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşi ortaya koyan katılımcıyı ve kalıcı anıyı korur."},"facet_ids":["F002"],"text":"unutulmaz bir iş yapmak","usage_role":"contextual"}],"definition":"Sıra dışı, ağır veya şaşırtıcı olduğu için anısı çok uzun süre kalan bir iş ya da olay; böyle bir işi ortaya koyma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Olağanüstü veya şaşırtıcı bir işin uzun süre anılmasını bildirir."},{"facet_id":"F002","role":"extension","statement":"Eylem kalıbı, anısı kalacak ölçüde sıra dışı bir iş ortaya koymayı anlatır."}],"identity_rationale":"Kaynak ifadesi olağanüstü, ağır veya şaşırtıcı bir işin uzun süre anılmasını dalın belirleyici bileşeni yapar. Yalnızca ün kazanma, haber anlatma ya da alışılmadık bir söz olma bu birleşik anlamı karşılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"uzun süre anılan olağanüstü iş veya olay"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"unutulmayacak kadar sıra dışı bir iş yapmak"}],"lexicalization_note":"Olağanüstü işi adlandıran biçim ile böyle bir iş yapmayı bildiren kalıp ayrı fakat aynı çekirdeğe bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıcı anı bırakan olay ile genel ün ve anlatılma arasındaki farkı gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal anlatılan kişi ya da topluluğu merkez alır; odak dal kalıcı anı bırakan olağanüstü işin kendisini merkez alır.","focus_only":"Odak dalda işin sıra dışı veya ağır oluşu ve anısının kalıcılığı birlikte zorunludur.","gloss":"dillere düşen olay","neighbor_only":"Komşu dal kişi veya topluluğun insanlar arasında anlatılan bir öyküye dönüşmesini kapsar.","neighbor_ref":"root_000299/B004","relation_type":"near_neighbor","shared_zone":"Bir kişi veya olayın uzun süre insanlar arasında anlatılması iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Komşu dal genel bilinirlik ve ün alanıdır; odak dal sıra dışı olay ile onun kalıcı anısı arasındaki bağı gerektirir.","focus_only":"Olağanüstü işin anısının çok uzun sürmesi odak dala özgüdür.","gloss":"ünlü ve unutulmaz","neighbor_only":"Komşu dal iyi veya kötü herhangi bir şeyin açıkça bilinmesini, ününü ve rezilliğini kapsar.","neighbor_ref":"root_000823/B002","relation_type":"near_neighbor","shared_zone":"Sıra dışı bir olayın insanlarca bilinip anılması ortak alandır."}],"source_phrase_ar":"الأبدة الفعلة تبقى على الأبد (maqayis)؛ جاء فلان بآبدة أي بداهية يبقى ذكرها على الأبد (sihah)","source_summary":"Kaynaklar sıra dışı bir iş veya olay ile onun uzun süre unutulmayan anısını aynı anlam yapısında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الآبدة بمعنى بداهية أو فعلة يبقى ذكرها على الأبد","what_is_not_ar":"ليس الكلمة الوحشية ولا القافية الشاردة وحدها"},"support_links":[]},{"boundary":"Anlam yalnız alışılmadık söz ve aykırı şiir ya da uyak birimlerine bağlı özel kullanımdır.","branch_kind":"non_bare","branch_ref":"root_000004/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"yadırgatıcı söz veya başıboş uyak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alışılmış dil kullanımının dışında kalan yadırgatıcı sözcüğü bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şiirde başıboş veya aykırı görülen uyaklar için kullanılan özel bir addır."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözcük ve şiir alanındaki iki özel kullanımı ortak yadırgatıcılık görüntüsüyle birlikte özetler.","boundary_detail":"Anlam yalnız alışılmadık söz ve aykırı şiir ya da uyak birimlerine bağlı özel kullanımdır.","branch_image_ar":"الكلمة الوحشية والشاردة","concept_gloss":"yadırgatıcı söz veya başıboş uyak","contextual_glosses":[{"applicability":"Gündelik dilde yabansı ve anlaşılması güç görülen tek bir sözcüğü adlandırırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün alışılmış kullanımdan uzaklığını korur."},"facet_ids":["F001"],"text":"alışılmadık sözcük","usage_role":"contextual"},{"applicability":"Şiirde aykırı veya düzene bağlanmayan uyakları çoğul olarak adlandırırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uyakların şiir düzeninden ayrılan niteliğini korur."},"facet_ids":["F002"],"text":"başıboş uyaklar","usage_role":"contextual"}],"definition":"Dilde alışılmadık, yabansı ve yadırgatıcı bir sözcük ya da şiirde düzenin dışına çıkmış, başıboş görülen bir uyak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alışılmış dil kullanımının dışında kalan yadırgatıcı sözcüğü bildirir."},{"facet_id":"F002","role":"specialization","statement":"Şiirde başıboş veya aykırı görülen uyaklar için kullanılan özel bir addır."}],"identity_rationale":"Kaynak ifadesi alışılmadık ve yadırgatıcı sözcük ile şiirde başıboş, aykırı uyakları aynı yabanıl ve ele avuca sığmaz benzetmesi altında toplar. Bu dal ne yabanıl hayvanı ne de uzun süre anılan olağanüstü olayı gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yadırgatıcı, alışılmadık sözcük"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"şiirin başıboş veya aykırı uyakları"}],"lexicalization_note":"Tanım, sözcük ve şiir birimlerine özgü adlaşmış kullanımlarla sınırlıdır; yalın kök anlamı kurulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel şiir kullanımını teknik uyak kusuru ve genel dize kavramından ayıran iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal belirli bir sözcük yineleme kusurudur; odak dal teknik yapıyı belirtmeden başıboş veya aykırı uyağı adlandırır.","focus_only":"Odak dal aykırı veya başıboş görülen uyağı ve alışılmadık sözcüğü adlandırır.","gloss":"aykırı uyak","neighbor_only":"Komşu dal aynı sözcüğün iki uyakta yinelenmesi biçimindeki belirli bir teknik kusuru tanımlar.","neighbor_ref":"root_001659/B005","relation_type":"near_neighbor","shared_zone":"İki dal da şiirde uyak düzeninden kaynaklanan alışılmadık bir durumu ele alır."},{"boundary_match":"field_only","distinction":"Komşu dal sıradan şiir dizesini tanımlar; odak dal yalnız düzene sığmayan veya yabansı görülen dil birimini seçer.","focus_only":"Odak dal şiirdeki aykırı uyağı ve yadırgatıcı sözcüğü gösterir.","gloss":"şiir dizesi","neighbor_only":"Komşu dal ölçülü sözlerden oluşan şiir dizesinin genel adıdır.","neighbor_ref":"root_000166/B003","relation_type":"same_field","shared_zone":"Her iki dal şiirin söz ve dize yapısı alanında yer alır."}],"source_phrase_ar":"الشوارد من القوافي أوابد (sihah)؛ الكلمة الوحشية آبدة وجمعه الأوابد (tahdhib)","source_summary":"Kaynaklar alışılmadık sözcükleri ve şiirin başıboş uyaklarını, düzene sığmayan yadırgatıcı dil birimleri olarak bir araya getirir.","sources":["SI","TA"],"what_is_ar":"الآبدة للكلمة الوحشية والشوارد من القوافي والأوابد من الشعر","what_is_not_ar":"ليس آبدة البداهية الباقية الذكر ولا الوحش الحيواني"},"support_links":[]},{"boundary":"Dal, öfke durumunu ve öfkenin bir kişiye yönelmesini kapsayan iki eylem kalıbıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000004/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","surface_ar":"أَبَدًا"}],"gloss":"öfkelenmek veya birine öfkelenmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin öfke durumuna girmesini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgeçli kalıpta öfkenin yöneldiği kişi ayrıca belirtilir."}}],"root_ar":"ء ب د","root_id":"root_000004","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yöneltilmemiş öfke ile belirli bir kişiye yönelmiş öfkeyi birlikte kapsayan açıklayıcı karşılıktır.","boundary_detail":"Dal, öfke durumunu ve öfkenin bir kişiye yönelmesini kapsayan iki eylem kalıbıyla sınırlıdır.","branch_image_ar":"الغضب والغضب عليه","concept_gloss":"öfkelenmek veya birine öfkelenmek","contextual_glosses":[{"applicability":"Öfkenin belirli bir kişiye yöneldiği ilgeçli eylem kalıbında doğal cümle karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfkeyi ve öfkenin yöneldiği kişiyi birlikte korur."},"facet_ids":["F002"],"text":"birine kızmak","usage_role":"contextual"}],"definition":"Bir kişinin öfkelenmesi veya öfkesini belirli bir kişiye yöneltmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin öfke durumuna girmesini bildirir."},{"facet_id":"F002","role":"specialization","statement":"İlgeçli kalıpta öfkenin yöneldiği kişi ayrıca belirtilir."}],"identity_rationale":"Kaynak ifadesi kişinin öfkelenmesini ve birine yönelmiş öfkeyi açıkça bildirir. Yüzün öfkeden değişmesi bu dalın zorunlu parçası olmadığı gibi nefret, kin veya uzun süreli kırgınlık da eklenmez.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"adamın öfkelenmesi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"ona öfkelenmek"}],"lexicalization_note":"Anlam kişi öznesi ve kişiye yönelme kalıplarında korunur; yalın köke genel duygu anlamı yüklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam eşleşen öfke dalı ile sık karışabilecek nefret alanı yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kanıtta katılımcı, yönelme ve sonuç bakımından anlamlı bir sınır farkı görünmez.","focus_only":null,"gloss":"öfkelenmek","neighbor_only":null,"neighbor_ref":"root_000050/B002","relation_type":"synonym","shared_zone":"Her iki dal da kişinin öfkelenmesini ve öfkenin birine yönelmesini aynı sınırlarla anlatır."},{"boundary_match":"partial","distinction":"Odak dal öfkelenme olayıdır; komşu dal daha kalıcı hoşlanmama ve nefret tutumudur.","focus_only":"Odak dal anlık öfke durumunu ve bunun birine yönelmesini bildirir.","gloss":"öfke ve nefret","neighbor_only":"Komşu dal sevginin karşıtı olan hoşlanmama, nefret ve karşılıklı nefret ilişkilerini kapsar.","neighbor_ref":"root_000136/B001","relation_type":"near_neighbor","shared_zone":"Bir kişiye karşı olumsuz duygu besleme iki dalın kesişebildiği alandır."}],"source_phrase_ar":"أبد الرجل غضب (sihah)؛ أبد إذا غضب عليه (tahdhib)؛ وقد فسر بغضب (mufradat)","source_summary":"Kaynaklar kişinin öfkelenmesi ile bu öfkenin belirli bir kişiye yönelmesini aynı eylem alanında birleştirir.","sources":["SI","TA","MU"],"what_is_ar":"أبد الرجل أو أبد عليه إذا غضب أو غضب عليه","what_is_not_ar":"ليس التوحش الحيواني ولا تأبد الوجه إلا إذا فسر بالغضب"},"support_links":[]},{"boundary":"Bu dal, bir kişilik özelliği olarak ağırbaşlı ve acele etmez olmayı değil, durma, bekleme ya da bir yerde kalma durumunu anlatır.","branch_kind":"bare","branch_ref":"root_001437/B001","candidate_links":[{"candidate_id":"cand_af2dad8902ad52c2b1c0","lane":"micro"},{"candidate_id":"cand_93ce5f419863cf101634","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّٰكِثِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:m~a`kiviyn|ROOT:mkv|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:3:1:1","qac_word_ref":"18:3:1","surface_ar":"مَّٰكِثِينَ"}],"gloss":"bekleyerek durup kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareketi ya da ilerlemeyi kesip bir süre bekleyerek durmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerde ayrılmadan kalma veya oyalanma, bekleyiş çekirdeğinin yer bildiren görünümüdür."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı anlatımlarda bekleme, bazılarında ise bir yerde kalma ve süre geçirme yönü daha belirgindir."}}],"root_ar":"م ك ث","root_id":"root_001437","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bekleme ile bulunduğu yerde kalmayı birlikte taşıyan genel kullanımda dalın bütün çekirdeğini karşılar.","boundary_detail":"Bu dal, bir kişilik özelliği olarak ağırbaşlı ve acele etmez olmayı değil, durma, bekleme ya da bir yerde kalma durumunu anlatır.","branch_image_ar":"ثبات مع انتظار","concept_gloss":"bekleyerek durup kalma","contextual_glosses":[{"applicability":"Bir kimsenin ilerlemeyip bulunduğu yerde beklemesini anlatan genel bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beklemeyi, hareketin kesilmesini ve bulunduğu yerde kalmayı birlikte korur."},"facet_ids":["F001","F002"],"text":"bekleyip kalma","usage_role":"general"},{"applicability":"Yer ve süre vurgusunun bekleme eyleminden daha belirgin olduğu bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bekleme amacı ya da bekleyiş durumu bu sözle tek başına açıkça aktarılmaz.","preserves":"Bulunduğu yerden ayrılmama ve orada süre geçirme yönünü korur."},"facet_ids":["F002","F003"],"text":"bir yerde kalma","usage_role":"contextual"},{"applicability":"Bir olayın veya işin gerçekleşmesini gözleme yönünün öne çıktığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir yerde kalma ve orada süre geçirme yönü açıkça belirtilmez.","preserves":"İlerlemeyi kesip bir süre bekleme yönünü doğrudan korur."},"facet_ids":["F001","F003"],"text":"bekleme","usage_role":"contextual"}],"definition":"Hareketi veya ilerlemeyi kesip bir süre bekleyerek durma ya da bulunduğu yerde kalma durumudur. Bağlama göre bekleme yönü veya bir yerde kalıp oyalanma yönü öne çıkabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareketi ya da ilerlemeyi kesip bir süre bekleyerek durmadır."},{"facet_id":"F002","role":"specialization","statement":"Bir yerde ayrılmadan kalma veya oyalanma, bekleyiş çekirdeğinin yer bildiren görünümüdür."},{"facet_id":"F003","role":"source_variant","statement":"Bazı anlatımlarda bekleme, bazılarında ise bir yerde kalma ve süre geçirme yönü daha belirgindir."}],"identity_rationale":"Kaynak ifadesi durma, bekleme, oyalanma ve bir yerde kalma anlamlarını aynı çekirdekte toplar. Verilen dal çerçevesi de bekleyişle birlikte süren kalışı öne çıkararak bu kapsamı doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bekleme, oyalanma ve bir yerde kalma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"durdu, bekledi veya bir yerde kaldı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bekleyen ya da bir yerde kalan kimse"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"oyalandı; bir işi bekledi veya üzerinde durdu"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bekleyip kalma"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir yerde kalan kimse"}],"lexicalization_note":"Dal yalın kullanıma aittir; tanım, belirli bir söz öbeğine bağlı özel bir anlam eklemeden durma, bekleme ve bir yerde kalma çekirdeğiyle sınırlıdır.","neighbor_coverage_note":"Bütün komşu adayları karşılaştırıldı. Yayınlanan üç karşıtlık bekleme, yerinde kalma ve ağırbaşlılık sınırlarını en açık biçimde gösterirken öteki adaylar genel olarak yerleşme veya uzun süre kalma alanını tekrarladığı için ayrıca verilmedi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı somut bir durma, bekleme veya kalma durumunu anlatırken komşu dal insanın davranış biçimini ve niteliğini anlatır; bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Durma, bekleme ve bir yerde kalma olayını bildirir.","gloss":"bekleyiş ile ağırbaşlılık","neighbor_only":"Bir kişinin ağırbaşlı, ölçülü ve acele etmez oluşunu bildirir.","neighbor_ref":"root_001437/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da hızın azalması, acele edilmemesi ve bir durumun sürdürülmesi çağrışımı bulunur."},{"boundary_match":"partial","distinction":"Odak dalında bekleyerek kalma ve yerden ayrılmama daha merkeziyken komşu dal, bir iş için uygun zamanı gözleme ile beklenen yeri de kendi kapsamına alır.","focus_only":"Bir yerde kalma ve bulunduğu konumu sürdürme yönünü ayrıca kapsar.","gloss":"oyalanıp bekleme","neighbor_only":"Bir işin mümkün hale gelmesini bekleme ve oyalanılan yer anlamlarını ayrıca kapsar.","neighbor_ref":"root_000074/B001","relation_type":"near_synonym","shared_zone":"İki dal da hareketi veya ilerlemeyi keserek bir süre bekleme durumunda birleşir."},{"boundary_match":"partial","distinction":"Odak dalının çekirdeğinde durma ve bekleme bulunur; komşu dal ise yerle kurulan kalıcı ya da süreğen bağlılığa yönelir ve bekleme şartı taşımaz.","focus_only":"Kalmanın bekleyiş veya duraklama niteliği taşımasını öne çıkarır.","gloss":"bir yerde kalma","neighbor_only":"Bir yere bağlı kalmayı ve orada sürdürülmüş bulunmayı bekleme gerektirmeden kapsar.","neighbor_ref":"root_001339/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yerden ayrılmayıp orada bulunmayı sürdürmeyi anlatabilir."}],"source_phrase_ar":"كلمة تدل على توقف وانتظار (maqayis)؛ المكث الانتظار والماكث المنتظر (ayn)؛ المكث المقام وربما جعل المكث في معنى الانتظار (jamhara)؛ المكث: اللبث والانتظار وتمكث: تلبث (sihah)؛ الماكث: المنتظر وتمكث إذا انتظر أمرا أو أقام عليه (tahdhib)؛ المكث: ثبات مع انتظار (mufradat)","source_summary":"Toplu tanıklık, anlamı durup bekleme çevresinde birleştirir; bir yerde kalma, oyalanma ve bulunduğu konumu sürdürme bu çekirdeğin bağlama göre belirginleşen görünümleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه التوقف واللبث والمقام في المكان والانتظار والثبات المصحوب بانتظار.","what_is_not_ar":"ليس وصف الرزانة وترك العجلة إذا كان خلقا أو هيئة في الإنسان."},"support_links":["sup_abd45caed90f8ffb2e9e","sup_f0a2c8786e47e0eb77be"]},{"boundary":"Bu dal yalnızca bir yerde kalmayı veya bir şeyi beklemeyi değil, insanın işinde ve davranışında acele etmeyen ağırbaşlı tutumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001437/B002","candidate_links":[{"candidate_id":"cand_e02d95e4b8091a1a30c4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّٰكِثِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:m~a`kiviyn|ROOT:mkv|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:3:1:1","qac_word_ref":"18:3:1","surface_ar":"مَّٰكِثِينَ"}],"gloss":"acele etmeyen ağırbaşlılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin bir işte acele etmeyip ağırbaşlı ve ölçülü davranmasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Acele etmezlik, kişide yerleşik bir ağırbaşlılık ve davranış niteliği olarak belirtilebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yürüyüşü bildiren özel söz öbeğinde kişi yavaş, oyalanarak ve ağırdan alarak ilerler."}}],"root_ar":"م ك ث","root_id":"root_001437","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin işlerinde ölçülü, sakin ve acele etmez oluşunu anlatan dal çekirdeğinde en uygun karşılıktır.","boundary_detail":"Bu dal yalnızca bir yerde kalmayı veya bir şeyi beklemeyi değil, insanın işinde ve davranışında acele etmeyen ağırbaşlı tutumunu anlatır.","branch_image_ar":"أناة ورزانة بلا عجلة","concept_gloss":"acele etmeyen ağırbaşlılık","contextual_glosses":[{"applicability":"Bir kişiyi davranış biçimi ve yerleşik niteliği bakımından tanımlayan bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ağırbaşlılığını, ölçülü davranışını ve aceleden kaçınmasını korur."},"facet_ids":["F001","F002"],"text":"ağırbaşlı ve acele etmez","usage_role":"general"},{"applicability":"Bir işi veya hareketi acele etmeden yürütme biçiminin öne çıktığı bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":"Gündelik kullanımda işi isteksizce geciktirme çağrışımı doğurabilir.","fit":"narrowing","loses":"Kişinin yerleşik ağırbaşlılık niteliği tek başına açıkça aktarılmaz.","preserves":"Eylemin acele edilmeden yavaş ve ölçülü biçimde yapılmasını korur."},"facet_ids":["F001","F003"],"text":"ağırdan alarak","usage_role":"contextual"},{"applicability":"Yürüyüş biçimini bildiren özel söz öbeğinin doğal cümle içi karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağırbaşlılık ve ölçülü kişilik niteliği bu karşılıkta açık değildir.","preserves":"Yürüyüşte hızın düşmesini ve acele edilmeden ilerlemeyi korur."},"facet_ids":["F003"],"text":"yavaşça yürüdü","usage_role":"contextual"}],"definition":"Bir kişinin işlerinde acele etmeyen, ağırbaşlı ve ölçülü oluşudur. Yürüyüşü anlatan özel kullanımda bu nitelik, yavaş ve ağırdan ilerleme biçimi olarak görünür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin bir işte acele etmeyip ağırbaşlı ve ölçülü davranmasıdır."},{"facet_id":"F002","role":"specialization","statement":"Acele etmezlik, kişide yerleşik bir ağırbaşlılık ve davranış niteliği olarak belirtilebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yürüyüşü bildiren özel söz öbeğinde kişi yavaş, oyalanarak ve ağırdan alarak ilerler."}],"identity_rationale":"Kaynak ifadesi kişiyi ağırbaşlı ve acele etmez diye niteler, ayrıca yürüyüşte yavaş ve ağırdan davranan bir biçimi gösterir. Verilen dal çerçevesi hem kişilik niteliğini hem de eylemdeki yavaş ve ölçülü görünümü doğru sınırlar içinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ağırbaşlı, acele etmeyen"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ağırbaşlılık ve acele etmeme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"adam yavaş ve ağırdan alarak yürüdü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ağırbaşlı ve acele etmeyen kimseler"}],"lexicalization_note":"Dal, yalın biçimlerde ağırbaşlı ve acele etmez kişi niteliğini, yürüyüşü bildiren söz öbeğinde ise yavaş ve ağırdan ilerlemeyi taşır; bu özel yürüyüş anlamı bütün dala yayılmaz.","neighbor_coverage_note":"Bütün komşu adayları karşılaştırıldı. Yayınlanan dört ayrım bekleyiş, genel yavaşlık, yumuşak davranış ve ağır adımlı yürüyüşle karışma risklerini gösterir; kalan adaylar özdenetim, sakinlik veya yerinde durma alanlarında daha dolaylı kesişir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı insanın davranış niteliğidir; komşu dal ise kişinin durduğu, beklediği veya bir yerde kaldığı olayı anlatır. Birinde huy ve tutum, ötekinde durum merkezidir.","focus_only":"Kişinin ağırbaşlı, ölçülü ve acele etmez niteliğini bildirir.","gloss":"ağırbaşlılık ile bekleyiş","neighbor_only":"Durma, bekleme ve bir yerde kalma olayını bildirir.","neighbor_ref":"root_001437/B001","relation_type":"near_neighbor","shared_zone":"İki dal da acele edilmemesi, hızın azalması ve bir durumun sürdürülmesi çağrışımını paylaşır."},{"boundary_match":"partial","distinction":"Odak dalında ağırbaşlı ve acele etmez kişi niteliği çekirdektir; komşu dal ise bekleme ve gecikme dahil daha geniş bir yavaşlık alanına yayılır.","focus_only":"Ağırbaşlılığı kişinin acele etmez niteliği olarak öne çıkarır.","gloss":"acele etmeyen ölçülülük","neighbor_only":"Geciktirme, bekleme ve bir işi sonraya bırakma gibi daha geniş yavaşlama durumlarını kapsar.","neighbor_ref":"root_000063/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da aceleden kaçınmayı, yavaş ve düşünerek davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalının ayırt edici yanı ağırbaşlı acele etmezliktir; komşu dalın çekirdeğinde yumuşaklık ve çeşitli eylemleri sakin biçimde yürütme bulunur.","focus_only":"Kişinin ağırbaşlı ve acele etmez olmasını temel nitelik olarak belirtir.","gloss":"ağırbaşlılık ile yumuşaklık","neighbor_only":"Yumuşak davranma, sözü veya okumayı tane tane sürdürme ve bir işi doğrulayarak yapma yönlerini kapsar.","neighbor_ref":"root_000563/B004","relation_type":"near_neighbor","shared_zone":"İki dal da davranışta aceleyi bırakma, ölçülü ilerleme ve sakinlik bakımından kesişir."},{"boundary_match":"partial","distinction":"Odak dalında yavaş yürüyüş yalnızca özel bir görünümken komşu dalda ağır adımla ilerleme anlamın merkezindedir; odak dalı bunun dışında kişinin genel tutumunu da niteler.","focus_only":"Genel bir kişilik ve davranış niteliği olarak ağırbaşlı acele etmezliği kapsar.","gloss":"ağırdan davranma","neighbor_only":"Ağır adımlı yürüyüşü ve adımların yavaşlığını belirgin biçimde öne çıkarır.","neighbor_ref":"root_001615/B002","relation_type":"near_neighbor","shared_zone":"İki dal da hareketin yavaş ve ölçülü oluşunda, özellikle yürüyüş bağlamında kesişebilir."}],"source_phrase_ar":"رجل مكيث رزين غير عجول (maqayis)؛ مكث مكاثة فهو مكيث أي رزين لا يعجل (ayn)؛ سار الرجل متمكثا أي متلوما ورجل مكيث أي رزين (sihah)؛ رجل مكيث الرزين الذي لا يعجل في أمره والماكث المنتظر وإن لم يكن مكيثا في الرزانة (tahdhib)","source_summary":"Toplu tanıklık, insanın işinde acele etmeyen ağırbaşlı niteliğinde birleşir. Yürüyüşte yavaş ve ağırdan ilerleme ise bu çekirdeğin belirli bir eylemdeki özel görünümüdür.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه وصف الإنسان بالمكاثة والرزانة وترك العجلة والتمهل في السير أو الأمر.","what_is_not_ar":"ليس مجرد اللبث بالمكان أو الانتظار إذا لم يدل على الرزانة أو التمهل."},"support_links":["sup_3739a293fcc71e9f2836"]}],"candidate_inventory":[{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_c21b43f25ce1614ee436","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:cross-boundary-hal-participle","source_type":"word_analysis","support_ids":["sup_660cea269ced784a9d92","sup_fda93b74d0a0c41c0bf7"],"title":"cross-boundary participial state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_4b991a96557f4cb26793","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:form-and-variant-stability","source_type":"word_analysis","support_ids":["sup_5bd542723fdceca651e6","sup_660cea269ced784a9d92"],"title":"participle form survives recitational variation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_8ab3bd655932661e6bd5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:rare-judgment-pair","source_type":"word_analysis","support_ids":["sup_25e399b1b148f9670e20","sup_660cea269ced784a9d92"],"title":"rare participial judgment pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_c99411f53f3621f7719b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:settled-patient-abiding","source_type":"word_analysis","support_ids":["sup_660cea269ced784a9d92","sup_83e5d297278804911b40"],"title":"settled patient remaining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_82f58d90afaa6dda2c6c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:sound-boundary-carryover","source_type":"word_analysis","support_ids":["sup_660cea269ced784a9d92","sup_c165044029a21c99ab57"],"title":"sound carries the promise forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_2fd87dd9ad274cb50eb7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:state-location-duration-chain","source_type":"word_analysis","support_ids":["sup_660cea269ced784a9d92","sup_a9d6c35e95aba800f2fa"],"title":"state to location to duration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_e014c64559c51e0580db","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:waiting-and-domain-echoes","source_type":"word_analysis","support_ids":["sup_660cea269ced784a9d92","sup_6f19dd54dc91e4881e20"],"title":"waiting and domain-bound endurance echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:1","qac_refs":["18:3:1:1"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_e2b227a5dd4cc169d05b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:bound-compression","source_type":"word_analysis","support_ids":["sup_d2a7efc116866b1cea80","sup_ddd35fffe7fd1a008c6f"],"title":"preposition and suffix compress the prior reward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_cbb0d2c7faf16a9277cb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:i-vowel-cadence","source_type":"word_analysis","support_ids":["sup_a3c958bed63e3d0760b3","sup_d2a7efc116866b1cea80"],"title":"vowel cadence links state and containment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_d4c7659ea7da86ee02b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:middle-pivot-chain","source_type":"word_analysis","support_ids":["sup_a69a2d7852ca492dd2fd","sup_d2a7efc116866b1cea80"],"title":"middle locative pivots state toward duration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_e444a7e6078b86c2bc75","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:reward-antecedent-with-book-background","source_type":"word_analysis","support_ids":["sup_c7186d7db79fab266174","sup_d2a7efc116866b1cea80"],"title":"reward antecedent with farther Book background","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_8a7e208818b579acfaba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:reward-as-inhabited-container","source_type":"word_analysis","support_ids":["sup_8294bf472e5f7f0fc3a1","sup_d2a7efc116866b1cea80"],"title":"reward becomes inhabited container","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:2"],"branch_refs":[],"candidate_id":"cand_1ca55e1b2ec567c48151","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:2:spatial-and-abstract-immersion","source_type":"word_analysis","support_ids":["sup_5ee0a10a8c6b56859bf5","sup_d2a7efc116866b1cea80"],"title":"containment remains both spatial and state-like","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:2","qac_refs":["18:3:2:1","18:3:2:2"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_7ec381f9f1507bc18797","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:adverbial-form-and-tanwin","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_5b7e1ff994fd0881879c"],"title":"adverbial form and tanwīn make duration audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_70fed1172c1018767a51","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:adverbial-scope-over-abiding","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_ef27ec46fc3fab82849d"],"title":"duration adverb modifies the abiding state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_9e49ce43294c8e2f6735","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:affirmative-forever-not-negative-never","source_type":"word_analysis","support_ids":["sup_1d6b0252dcf4de45ec4a","sup_2e6cbec3f8f622d5b37e"],"title":"affirmation selects forever","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_2c9ca24c6a13517d4817","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:boundary-sound-continuity","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_6974140bf6a73fd16659"],"title":"sound links reward quality to duration","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_25272e96870ba8b6f1ff","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:final-seal-of-promise","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_daaadae31094ee4e7b4c"],"title":"final word seals the promise","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_135e05492077dc5882b8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:one-form-duration-profile","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_81da6f182c75a234ac65"],"title":"Quranic profile as duration operator","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_22f0288f73d24398c260","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:same-surah-and-reward-formula-echoes","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_cf865800a5be2de86d88"],"title":"duration thread and reward formula echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_e803d91c558f4c2c0c88","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:3:3:unbounded-permanence-with-local-filter","source_type":"word_analysis","support_ids":["sup_2e6cbec3f8f622d5b37e","sup_e224b687dd960ac6cd25"],"title":"unbounded permanence filtered by reward context","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:3:3","qac_refs":["18:3:3:1"],"status":"accepted"}},{"anchor_refs":["18:3:1"],"branch_refs":[],"candidate_id":"cand_506b6eb6588bd2b65ac8","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001437"],"scope":"focus_ayah","source_local_id":"18:3:1:1","source_type":"qac_morpheme","support_ids":["sup_ff046b6bb6e03756e49c"],"title":"QAC root occurrence: م ك ث","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:3:3"],"branch_refs":[],"candidate_id":"cand_50700ad0745daf594b17","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000004"],"scope":"focus_ayah","source_local_id":"18:3:3:1","source_type":"qac_morpheme","support_ids":["sup_45e53095c4edbd03e4d8"],"title":"QAC root occurrence: ء ب د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:3","branch_refs":["root_000004/B001","root_000004/B006","root_001437/B001"],"candidate_id":"cand_af2dad8902ad52c2b1c0","commentary_obligation":"review","hft_ref":"hft_765e780c1fc90d130761","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-exitless-residence","source_type":"hft","support_ids":["sup_f0a2c8786e47e0eb77be"],"title":"baseline-exitless-residence","trust":"legacy_unbound"},{"anchor_refs":["18:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:3","branch_refs":["root_000004/B001","root_001437/B002"],"candidate_id":"cand_e02d95e4b8091a1a30c4","commentary_obligation":"review","hft_ref":"hft_2ede7ce65984b7ff90c9","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-unhurried-abiding","source_type":"hft","support_ids":["sup_3739a293fcc71e9f2836"],"title":"baseline-unhurried-abiding","trust":"legacy_unbound"},{"anchor_refs":["18:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:3","branch_refs":["root_000004/B002","root_000004/B003","root_001437/B001"],"candidate_id":"cand_93ce5f419863cf101634","commentary_obligation":"review","hft_ref":"hft_31318be7165bdc2b9626","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier-permanent-estrangement","source_type":"hft","support_ids":["sup_abd45caed90f8ffb2e9e"],"title":"outlier-permanent-estrangement","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"مَّٰكِثِينَ فِيهِ أَبَدًۭا","qac_morphemes":[{"lemma_ar":"مَّٰكِثِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:m~a`kiviyn|ROOT:mkv|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:3:1:1","qac_word_ref":"18:3:1","root_ar":"م ك ث","surface_ar":"مَّٰكِثِينَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"18:3:2:1","qac_word_ref":"18:3:2","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:3:2:2","qac_word_ref":"18:3:2","root_ar":"","surface_ar":"هِ"},{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","root_ar":"ء ب د","surface_ar":"أَبَدًا"}],"word_analysis_qac_refs":[["18:3:1:1"],["18:3:2:1","18:3:2:2"],["18:3:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["18:3:1","18:3:2","18:3:3"]},"focus_surface_evidence":{"arabic_uthmani":"مَّٰكِثِينَ فِيهِ أَبَدًۭا","qac_morphemes":[{"lemma_ar":"مَّٰكِثِين","morph_features":"STEM|POS:N|ACT|PCPL|LEM:m~a`kiviyn|ROOT:mkv|MP|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:3:1:1","qac_word_ref":"18:3:1","root_ar":"م ك ث","surface_ar":"مَّٰكِثِينَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"18:3:2:1","qac_word_ref":"18:3:2","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:3:2:2","qac_word_ref":"18:3:2","root_ar":"","surface_ar":"هِ"},{"lemma_ar":"أَبَدًا","morph_features":"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC","morpheme_role":"STEM","pos":"T","qac_ref":"18:3:3:1","qac_word_ref":"18:3:3","root_ar":"ء ب د","surface_ar":"أَبَدًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["18:3:1:1"],["18:3:2:1","18:3:2:2"],["18:3:3:1"]],"word_analysis_refs":["18:3:1","18:3:2","18:3:3"],"word_rows":[{"analysis_record_ref":"18:3:1","analytic_gloss_range_en":"abiding as a settled participial state attached to the believers; locally resident, patient remaining rather than a new finite action","analytic_root_gloss_range_en":"remaining, lingering, waiting, and staying with deliberateness or composure; local grammar selects settled abiding while allowing patient duration pressure","qac_refs":["18:3:1:1"],"root":{"arabic":"م ك ث","transliteration":"m-k-th"},"surface":{"arabic":"مَّٰكِثِينَ","transliteration":"mākithīna"}},{"analysis_record_ref":"18:3:2","analytic_gloss_range_en":"within it; a bound prepositional phrase whose suffix most tightly resumes the good reward and makes that reward the domain of abiding","analytic_root_gloss_range_en":null,"qac_refs":["18:3:2:1","18:3:2:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"فِيهِ","transliteration":"fīhi"}},{"analysis_record_ref":"18:3:3","analytic_gloss_range_en":"forever, with unbounded temporal scope over the believers' abiding state; locally affirmative endless continuation rather than negated never","analytic_root_gloss_range_en":"permanence and unbounded duration, with wider family imagery of time hardened beyond ordinary limits; local reward context excludes desolation as the main sense","qac_refs":["18:3:3:1"],"root":{"arabic":"أ ب د","transliteration":"ʾ-b-d"},"surface":{"arabic":"أَبَدًۭا","transliteration":"abadan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["18:3"],"branch_refs":["root_000004/B001","root_000004/B006","root_001437/B001"],"candidate_id":"cand_af2dad8902ad52c2b1c0","evidence_scope":"focus_ayah","hft_ref":"hft_765e780c1fc90d130761","item_id":"baseline-exitless-residence","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-exitless-residence","support_id":"sup_f0a2c8786e47e0eb77be"},{"anchor_refs":["18:3"],"branch_refs":["root_000004/B001","root_001437/B002"],"candidate_id":"cand_e02d95e4b8091a1a30c4","evidence_scope":"focus_ayah","hft_ref":"hft_2ede7ce65984b7ff90c9","item_id":"baseline-unhurried-abiding","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-unhurried-abiding","support_id":"sup_3739a293fcc71e9f2836"},{"anchor_refs":["18:3"],"branch_refs":["root_000004/B002","root_000004/B003","root_001437/B001"],"candidate_id":"cand_93ce5f419863cf101634","evidence_scope":"focus_ayah","hft_ref":"hft_31318be7165bdc2b9626","item_id":"outlier-permanent-estrangement","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-permanent-estrangement","support_id":"sup_abd45caed90f8ffb2e9e"}],"diagnostics":[],"lane_counts":{"global":8,"macro":6,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"18:3","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["18:1","18:2","18:3","18:4","18:5","18:6","18:7","18:8","18:9","18:10","18:11","18:12","18:13","18:14","18:15","18:16","18:17","18:18","18:19","18:20","18:21","18:22","18:23","18:24","18:25","18:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"18:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":9,"unstructured_record_count":0},"identity":{"ayah_ref":"18:3","lane":"micro","linguistic_source_ref":"18:3","surface_ref":"18:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"18:3","target_tokens":[["Onlar",["18:3:1"]],["orada",["18:3:1"]],["sonsuza",["18:3:2"]],["dek",["18:3:2"]],["kalacaklardır",["18:3:3"]]],"text":"Onlar orada sonsuza dek kalacaklardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":26,"id":"s018-p01-001-026","label":"Revelation and the companions of the cave","number":1,"refs":["18:1","18:2","18:3","18:4","18:5","18:6","18:7","18:8","18:9","18:10","18:11","18:12","18:13","18:14","18:15","18:16","18:17","18:18","18:19","18:20","18:21","18:22","18:23","18:24","18:25","18:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:affirmative-forever-not-negative-never","source_type":"word_analysis","support_id":"sup_1d6b0252dcf4de45ec4a","text":"{\"blocking_evidence\":null,\"headline\":\"affirmation selects forever\",\"reader_payoff\":\"The reader notices that the same adverb can intensify opposite temporal directions, but the affirmative promise here selects forever.\",\"reason\":\"The local clause is affirmative, while the same surah supplies a negated use where {{ar:أَبَدًۭا}} ({{tr:abadan}}) functions as never (18:57).\",\"representative_source_ids\":[\"QS-3b9a4cb2\",\"QI-2bebe0fe\",\"MI-c9802f57\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:rare-judgment-pair","source_type":"word_analysis","support_id":"sup_25e399b1b148f9670e20","text":"{\"blocking_evidence\":null,\"headline\":\"rare participial judgment pair\",\"reader_payoff\":\"The reader notices the participle as a rare form that can mark fixed placement in both reward here and punishment elsewhere (43:77).\",\"reason\":\"The contextual profile marks the active participle as low occurrence, and the CRITICAL rows name the paired participial use in 43:77.\",\"representative_source_ids\":[\"QI-004f0d4a\",\"MI-bba7c3a0\",\"MH-885c9c3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3","source_type":"word_analysis","support_id":"sup_2e6cbec3f8f622d5b37e","text":"{\"gloss_range\":\"forever, with unbounded temporal scope over the believers' abiding state; locally affirmative endless continuation rather than negated never\",\"prose\":\"{{ar:أَبَدًۭا}} ({{tr:abadan}}) closes the clause by giving the participial state an unbounded duration. Its accusative adverbial form is not a new object or an adjective for the reward noun in 18:2; it measures how long the believers remain in the reward. In an affirmative setting, the word selects forever, while the same form can turn to never under negation inside the same surah (18:57). The root field presses beyond a merely long term into endpointless permanence, but the good reward phrase in 18:2 keeps desolation imagery from governing the reading. Its Quranic profile is strongly adverbial here: permanence enters as a duration operator, not as a local verb or adjective family. As the final word, with tanwīn cadence answering the good reward phrase in 18:2, it seals the promise, joins the wider permanent-recompense formula (4:57; 4:122; 9:22; 9:100; 98:8), and begins a local duration thread that returns in Sūrat al-Kahf (18:20; 18:35; 18:57).\",\"root_display\":\"{{ar:أ ب د}} ({{tr:ʾ-b-d}})\",\"root_gloss_range\":\"permanence and unbounded duration, with wider family imagery of time hardened beyond ordinary limits; local reward context excludes desolation as the main sense\",\"surface_display\":\"{{ar:أَبَدًۭا}} ({{tr:abadan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:3:3:1","source_type":"qac_morpheme","support_id":"sup_45e53095c4edbd03e4d8","text":"{\"lemma_ar\":\"أَبَدًا\",\"morph_features\":\"STEM|POS:T|LEM:>abadFA|ROOT:Abd|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"T\",\"qac_ref\":\"18:3:3:1\",\"qac_word_ref\":\"18:3:3\",\"root_ar\":\"ء ب د\",\"surface_ar\":\"أَبَدًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:adverbial-form-and-tanwin","source_type":"word_analysis","support_id":"sup_5b7e1ff994fd0881879c","text":"{\"blocking_evidence\":null,\"headline\":\"adverbial form and tanwīn make duration audible\",\"reader_payoff\":\"The reader notices case, indefiniteness, and closing sound working together in the final duration word.\",\"reason\":\"The accusative adverbial ending and tanwīn fit the word's scope over duration and also shape its closing cadence.\",\"representative_source_ids\":[\"QF-277583d5\",\"QF-a7a9ca55\",\"QF-fa69841c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:form-and-variant-stability","source_type":"word_analysis","support_id":"sup_5bd542723fdceca651e6","text":"{\"blocking_evidence\":null,\"headline\":\"participle form survives recitational variation\",\"reader_payoff\":\"The reader notices that recitational pacing may vary while the participial ḥāl function and reference remain stable.\",\"reason\":\"The variant rows affect vowel length around {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}), but they do not alter the plural participial case role.\",\"representative_source_ids\":[\"QF-b680e5b1\",\"QF-eaf14b9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:spatial-and-abstract-immersion","source_type":"word_analysis","support_id":"sup_5ee0a10a8c6b56859bf5","text":"{\"blocking_evidence\":null,\"headline\":\"containment remains both spatial and state-like\",\"reader_payoff\":\"The reader notices that the reward is not flattened into either a mere place or a mere abstraction; the phrase works as immersion in a recompense-state.\",\"reason\":\"The local prepositional phrase licenses containment, and the reward context allows that containment to be experienced as a state without erasing locative force.\",\"representative_source_ids\":[\"QS-255c78d7\",\"QS-e77888e4\",\"MS-b5500501\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1","source_type":"word_analysis","support_id":"sup_660cea269ced784a9d92","text":"{\"gloss_range\":\"abiding as a settled participial state attached to the believers; locally resident, patient remaining rather than a new finite action\",\"prose\":\"{{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}) opens 18:3 as an accusative active participle, so the ayah does not start a new finite action. Its case and plural agreement reach back to the believers in 18:2, making the ayah boundary fall inside the promise's grammar: the believers are already being described in the state of abiding. The root {{ar:م ك ث}} ({{tr:m-k-th}}) keeps that state from feeling like bare existence; it carries settled, patient remaining, while the local form keeps the selected sense as resident abiding rather than an independent command or causative act. Recitational variation can tighten the internal vowel, but the plural ḥāl role and cross-boundary reference stay fixed. The rare participial use also has a judgment-pair echo with punishment permanence (43:77), and the root's commanded-waiting scenes (20:10; 28:29) and domain-bound endurance pattern (13:17) sharpen the local image as temporary waiting fulfilled in settled reward-residence without replacing the grammar. Sound and structure join the same movement: liaison from the prior promise and the long ī link into {{ar:فِيهِ}} ({{tr:fīhi}}) make the opening state lead straight into {{ar:فِيهِ أَبَدًۭا}} ({{tr:fīhi abadan}}), so location and duration unfold as extensions of the participial seal.\",\"root_display\":\"{{ar:م ك ث}} ({{tr:m-k-th}})\",\"root_gloss_range\":\"remaining, lingering, waiting, and staying with deliberateness or composure; local grammar selects settled abiding while allowing patient duration pressure\",\"surface_display\":\"{{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:boundary-sound-continuity","source_type":"word_analysis","support_id":"sup_6974140bf6a73fd16659","text":"{\"blocking_evidence\":null,\"headline\":\"sound links reward quality to duration\",\"reader_payoff\":\"The reader hears the final cadence continue the previous reward phrase, tying reward quality to duration across the ayah break.\",\"reason\":\"The cadence rows connect the closing sound of {{ar:أَبَدًۭا}} ({{tr:abadan}}) with {{ar:أَجْرًا حَسَنًا}} ({{tr:ajran ḥasanan}}), preserving continuity across the promise boundary.\",\"representative_source_ids\":[\"QP-5adcdebe\",\"QP-8a7f0ce6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:waiting-and-domain-echoes","source_type":"word_analysis","support_id":"sup_6f19dd54dc91e4881e20","text":"{\"blocking_evidence\":null,\"headline\":\"waiting and domain-bound endurance echoes\",\"reader_payoff\":\"The reader notices that temporary waiting and domain-bound endurance elsewhere become a fulfilled, settled reward-state here.\",\"reason\":\"The echoes to commanded waiting (20:10; 28:29) and endurance within a domain (13:17) illuminate the local root field, but they remain parallels and do not control the canonical parse.\",\"representative_source_ids\":[\"QE-67430239\",\"QE-bc102d59\",\"ME-4c7bb677\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:one-form-duration-profile","source_type":"word_analysis","support_id":"sup_81da6f182c75a234ac65","text":"{\"blocking_evidence\":null,\"headline\":\"Quranic profile as duration operator\",\"reader_payoff\":\"The reader notices that the root appears here through a strongly adverbial duration profile rather than a varied local verb or noun family.\",\"reason\":\"Contextual profiles show the exact form functioning as an adverbial duration term, and V4 absence for the root does not contradict that profile.\",\"representative_source_ids\":[\"QI-332f000e\",\"QH-4edd8fbf\",\"MS-03a1ca22\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:reward-as-inhabited-container","source_type":"word_analysis","support_id":"sup_8294bf472e5f7f0fc3a1","text":"{\"blocking_evidence\":null,\"headline\":\"reward becomes inhabited container\",\"reader_payoff\":\"The reader notices the shift from having a reward to being located within the reward as an experienced condition.\",\"reason\":\"{{ar:فِي}} ({{tr:fī}}) governs the suffix as a complement of the abiding participle, supporting containment rather than a loose possession frame.\",\"representative_source_ids\":[\"QG-8b49363d\",\"QS-68d99d44\",\"QB-f2a593bc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:settled-patient-abiding","source_type":"word_analysis","support_id":"sup_83e5d297278804911b40","text":"{\"blocking_evidence\":null,\"headline\":\"settled patient remaining\",\"reader_payoff\":\"The reader notices abiding as settled residence with patient duration, not merely the fact that the believers continue to exist.\",\"reason\":\"V4 preserves staying and deliberateness branches for {{ar:م ك ث}} ({{tr:m-k-th}}), while the local active participle and following locative keep the reading to settled abiding rather than a causative or command sense.\",\"representative_source_ids\":[\"QS-255629d6\",\"QS-74ae20dc\",\"MS-3f634800\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:i-vowel-cadence","source_type":"word_analysis","support_id":"sup_a3c958bed63e3d0760b3","text":"{\"blocking_evidence\":null,\"headline\":\"vowel cadence links state and containment\",\"reader_payoff\":\"The reader hears the long vowel link between the state word and the containment phrase before the duration word closes the ayah.\",\"reason\":\"The cadence row reinforces the syntactic attachment between {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}) and {{ar:فِيهِ}} ({{tr:fīhi}}), without creating a separate grammatical parse.\",\"representative_source_ids\":[\"QP-bbc03ec2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:middle-pivot-chain","source_type":"word_analysis","support_id":"sup_a69a2d7852ca492dd2fd","text":"{\"blocking_evidence\":null,\"headline\":\"middle locative pivots state toward duration\",\"reader_payoff\":\"The reader notices that the middle word controls the clause's unfolding from abiding, to abiding within something, to abiding forever.\",\"reason\":\"{{ar:فِيهِ}} ({{tr:fīhi}}) stands between the participle and the duration adverb, while attachment evidence links both modifiers to the abiding state.\",\"representative_source_ids\":[\"QT-5952ff72\",\"QT-1e95c62c\",\"QY-ac1af019\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:state-location-duration-chain","source_type":"word_analysis","support_id":"sup_a9d6c35e95aba800f2fa","text":"{\"blocking_evidence\":null,\"headline\":\"state to location to duration\",\"reader_payoff\":\"The reader notices the three-word ayah building permanence step by step: state, contained domain, then unbounded duration.\",\"reason\":\"Attachment evidence links {{ar:فِيهِ}} ({{tr:fīhi}}) and {{ar:أَبَدًۭا}} ({{tr:abadan}}) to the participial state, supporting the compressed state-location-duration sequence.\",\"representative_source_ids\":[\"QT-645fcab3\",\"QT-ea11c1a1\",\"QY-ca0e4b1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:sound-boundary-carryover","source_type":"word_analysis","support_id":"sup_c165044029a21c99ab57","text":"{\"blocking_evidence\":null,\"headline\":\"sound carries the promise forward\",\"reader_payoff\":\"The reader hears the prior promise continuing into the abiding clause through liaison and the long vowel link with the following locative.\",\"reason\":\"The sound rows align with the same boundary mechanism already supported grammatically: the promise continues into {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}) and then into {{ar:فِيهِ}} ({{tr:fīhi}}).\",\"representative_source_ids\":[\"QP-e2681a19\",\"QP-f706150a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:reward-antecedent-with-book-background","source_type":"word_analysis","support_id":"sup_c7186d7db79fab266174","text":"{\"blocking_evidence\":null,\"headline\":\"reward antecedent with farther Book background\",\"reader_payoff\":\"The reader notices that the suffix must be resolved across the boundary, with the reward as the tight antecedent and the Book as a farther background echo.\",\"reason\":\"Attachment evidence strongly links the 3ms suffix in {{ar:فِيهِ}} ({{tr:fīhi}}) to the masculine singular reward in 18:2, so the Book reading is preserved only as a farther discourse layer.\",\"representative_source_ids\":[\"QG-3a54e1c1\",\"MG-edaf4293\",\"MG-2ddb5c67\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:same-surah-and-reward-formula-echoes","source_type":"word_analysis","support_id":"sup_cf865800a5be2de86d88","text":"{\"blocking_evidence\":null,\"headline\":\"duration thread and reward formula echoes\",\"reader_payoff\":\"The reader notices that the final duration word is both part of a wider righteous-reward formula and the start of a same-surah duration thread.\",\"reason\":\"The CRITICAL rows name reward formula parallels (4:57; 4:122; 9:22; 9:100; 98:8) and same-surah returns (18:20; 18:35; 18:57).\",\"representative_source_ids\":[\"QI-63d92864\",\"QE-777f3ffd\",\"QE-e8002905\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2","source_type":"word_analysis","support_id":"sup_d2a7efc116866b1cea80","text":"{\"gloss_range\":\"within it; a bound prepositional phrase whose suffix most tightly resumes the good reward and makes that reward the domain of abiding\",\"prose\":\"{{ar:فِيهِ}} ({{tr:fīhi}}) is the middle word that turns reward from something assigned to the believers into the domain they inhabit. The suffix most directly resumes the reward from 18:2, so the phrase means abiding within the promised reward; the farther link to the Book in 18:1 remains a background possibility, not the controlling local antecedent. The containment is both locative and state-like: the reward is not only a place and not only an abstraction, but an experienced recompense-medium. Because {{ar:فِي}} ({{tr:fī}}) and the suffix are fused in one word, containment and discourse memory are compressed together. Placed between {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}) and {{ar:أَبَدًۭا}} ({{tr:abadan}}), the word pivots the clause from state into contained state before the final duration arrives, and the long ī cadence from {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}) into {{ar:فِيهِ}} ({{tr:fīhi}}) lets that syntactic link be heard before duration closes the ayah.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِيهِ}} ({{tr:fīhi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:final-seal-of-promise","source_type":"word_analysis","support_id":"sup_daaadae31094ee4e7b4c","text":"{\"blocking_evidence\":null,\"headline\":\"final word seals the promise\",\"reader_payoff\":\"The reader notices that the promise sequence lands on duration as its final and climactic content.\",\"reason\":\"The word occupies the final slot of the compressed state-location-duration chain and closes the 18:2-3 reward promise.\",\"representative_source_ids\":[\"QT-ef2af123\",\"MT-1db74a47\",\"QY-876d526c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:2:bound-compression","source_type":"word_analysis","support_id":"sup_ddd35fffe7fd1a008c6f","text":"{\"blocking_evidence\":null,\"headline\":\"preposition and suffix compress the prior reward\",\"reader_payoff\":\"The reader notices how one bound word keeps the prior reward recoverable without repeating the noun.\",\"reason\":\"The preposition plus 3ms suffix form a single dependency word, preserving both containment and the remembered antecedent.\",\"representative_source_ids\":[\"QG-eb1ed2c1\",\"QF-1856ebca\",\"QF-8c9a1cc3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:unbounded-permanence-with-local-filter","source_type":"word_analysis","support_id":"sup_e224b687dd960ac6cd25","text":"{\"blocking_evidence\":null,\"headline\":\"unbounded permanence filtered by reward context\",\"reader_payoff\":\"The reader notices that the word removes the endpoint from the promise while the good reward setting filters out darker desolation pressure.\",\"reason\":\"The bundle lacks V4 rows for {{ar:أ ب د}} ({{tr:ʾ-b-d}}), which is not evidence against the CRITICAL semantic rows; local reward context keeps unbounded duration and blocks desolation from becoming the main reading.\",\"representative_source_ids\":[\"QS-ca3dbed9\",\"QS-65524f47\",\"MS-c101026c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:3:adverbial-scope-over-abiding","source_type":"word_analysis","support_id":"sup_ef27ec46fc3fab82849d","text":"{\"blocking_evidence\":null,\"headline\":\"duration adverb modifies the abiding state\",\"reader_payoff\":\"The reader notices that eternity measures the believers' remaining, not the pronoun or a separate object.\",\"reason\":\"QAC and attachment evidence identify {{ar:أَبَدًۭا}} ({{tr:abadan}}) as an accusative time adverb modifying {{ar:مَّٰكِثِينَ}} ({{tr:mākithīna}}).\",\"representative_source_ids\":[\"QG-58ff79e6\",\"QG-659b7c68\",\"MG-e31ca04c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:3:1:cross-boundary-hal-participle","source_type":"word_analysis","support_id":"sup_fda93b74d0a0c41c0bf7","text":"{\"blocking_evidence\":null,\"headline\":\"cross-boundary participial state\",\"reader_payoff\":\"The reader notices that 18:3 is grammatically attached to the believers in 18:2 rather than beginning an independent sentence.\",\"reason\":\"QAC and attachment evidence support an accusative masculine plural circumstantial participle whose discourse role continues the believers from 18:2.\",\"representative_source_ids\":[\"QG-3b8e99f8\",\"QG-cf9c6e2c\",\"MG-27027e03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:3:1:1","source_type":"qac_morpheme","support_id":"sup_ff046b6bb6e03756e49c","text":"{\"lemma_ar\":\"مَّٰكِثِين\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:m~a`kiviyn|ROOT:mkv|MP|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"18:3:1:1\",\"qac_word_ref\":\"18:3:1\",\"root_ar\":\"م ك ث\",\"surface_ar\":\"مَّٰكِثِينَ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"مَّٰكِثِينَ فِيهِ أَبَدًۭا","ayah_ref":"18:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000004/B001","root_000004/B006","root_001437/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001437","role":"Stability with waiting supplies the settled residence at the mechanism's center.","root":"م ك ث","source_ref":"18:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000004","role":"Long duration and continuity remove a temporal endpoint from the residence.","root":"ء ب د","source_ref":"18:3","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_000004","role":"Residence without departure makes the continuing tenure exitless as well as long.","root":"ء ب د","source_ref":"18:3","source_word_indices":["3"]}],"changed_reading":{"after":"They occupy it as a settled condition with neither temporal terminus nor departure.","before":"They stay there for a very long time."},"confidence":"strong","focus_anchor":"مَّٰكِثِينَ فِيهِ أَبَدًا, with م ك ث governing the stay and ء ب د removing departure and terminus.","mechanism":"م ك ث supplies settled stability with waiting, while ء ب د supplies both continuous duration and residence without leaving. Together they describe an enduring mode of occupancy, not a momentary reward event.","model_id":"baseline-exitless-residence"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-exitless-residence","source_type":"hft","support_id":"sup_f0a2c8786e47e0eb77be","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَّٰكِثِينَ فِيهِ أَبَدًۭا","ayah_ref":"18:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000004/B001","root_001437/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001437","role":"Unhurried gravity supplies the qualitative tempo of the abiding.","root":"م ك ث","source_ref":"18:3","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000004","role":"Continuity extends that unhurried mode without an endpoint.","root":"ء ب د","source_ref":"18:3","source_word_indices":["3"]}],"changed_reading":{"after":"Forever also names an unhurried, stable mode of remaining, free of pressure toward the next state.","before":"Forever states only how long they remain."},"confidence":"medium","focus_anchor":"The participial مَّٰكِثِينَ read through the deliberative branch of م ك ث, extended by أَبَدًا.","mechanism":"The unhurried steadiness branch of م ك ث changes permanence from mere extension into a manner of being: no haste, forced transition, or pressure toward an ending marks the stay.","model_id":"baseline-unhurried-abiding"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-unhurried-abiding","source_type":"hft","support_id":"sup_3739a293fcc71e9f2836","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"مَّٰكِثِينَ فِيهِ أَبَدًۭا","ayah_ref":"18:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000004/B002","root_000004/B003","root_001437/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001437","role":"Fixed residence supplies the new place or condition in which separation stabilizes.","root":"م ك ث","source_ref":"18:3","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000004","role":"Wildness and aversion image a permanent loss of domestication to the former order.","root":"ء ب د","source_ref":"18:3","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000004","role":"The emptied dwelling images the prior condition left vacant behind the abiding subjects.","root":"ء ب د","source_ref":"18:3","source_word_indices":["3"]}],"changed_reading":{"after":"Their permanence may also image irreversible estrangement from the former world, as though its old dwelling has been emptied behind them.","before":"They simply continue in the promised condition forever."},"confidence":"exploratory","containment":"This is surprising because it activates the non-temporal wildness and emptied-home branches of ء ب د inside the ordinary temporal adverb أَبَدًا. It remains anchored in that exact focus root and in settled م ك ث, but downstream prose should present it only as an image of irreversible separation from the former order, not as a replacement definition of 'forever.'","focus_anchor":"أَبَدًا carries branch images of wild estrangement and an emptied former dwelling beside مَّٰكِثِينَ's fixed residence.","outlier_id":"outlier-permanent-estrangement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier-permanent-estrangement","source_type":"hft","support_id":"sup_abd45caed90f8ffb2e9e","trust":"legacy_unbound"}]}
</lane_packet_json>
