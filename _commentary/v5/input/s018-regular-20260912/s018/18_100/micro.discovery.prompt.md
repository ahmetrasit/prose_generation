# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **18:100**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s018-regular-20260912/s018/18_100/micro.discovery.json` and modify nothing
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
  "ayah_ref": "18:100",
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
{"analysis_context":{"analysis_id":"s018-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"18:100","host_surah":18,"lane_context_refs":[],"ordered_context_refs":["18:99","18:101","18:102","18:103","18:104","18:105","18:106","18:107","18:108","18:109","18:110","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal, gösterme veya yüz çevirme eylemlerini değil, en boyutunu ve yan tarafı anlatır.","branch_kind":"bare","branch_ref":"root_001001/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"en, yan ve enli kılma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin uzunluğuna karşıt en boyutunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"En boyutunun belirlediği yan veya taraf için de kullanılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeyi enli duruma getirme işlemini de kapsar."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"En boyutunu, bu boyuta bağlı yanı ve ettirgen genişletmeyi birlikte anlatan genel açıklama olarak uygundur.","boundary_detail":"Bu dal, gösterme veya yüz çevirme eylemlerini değil, en boyutunu ve yan tarafı anlatır.","branch_image_ar":"العرض خلاف الطول والجانب","concept_gloss":"en, yan ve enli kılma","contextual_glosses":[{"applicability":"Bir nesnenin ölçüsü veya yan yüzü söz konusu olduğunda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi enli kılma işlemini belirtmez.","preserves":"En ölçüsünü ve yan taraf ilişkisini korur."},"facet_ids":["F001","F002"],"text":"en ve yan taraf","usage_role":"contextual"}],"definition":"Bir şeyin uzunluğuna dik uzanan en boyutu ya da bu boyutun belirlediği yan taraf; ayrıca bir şeyi bu yönde geniş duruma getirmedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin uzunluğuna karşıt en boyutunu belirtir."},{"facet_id":"F002","role":"extension","statement":"En boyutunun belirlediği yan veya taraf için de kullanılır."},{"facet_id":"F003","role":"specialization","statement":"Bir şeyi enli duruma getirme işlemini de kapsar."}],"identity_rationale":"Kaynak ifadesi, uzunluğa karşıt olan en ölçüsünü ve bir şeyin yanını aynı anlam alanında açıkça verir. Bir şeyi enli kılma da bu uzamsal çekirdeğin ettirgen gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"en; bir şeyin yanı veya tarafı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"enli, geniş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyi enli duruma getirmek"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"sütten kesilmiş, henüz erginleşmemiş güçlü oğlak"}],"lexicalization_note":"Tanım yalın dalın uzamsal anlamıyla sınırlıdır; özel tamlamalardan başka bir anlam aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en doğrudan sınır karşılaştırmasını sağlayan tek yakın anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği uzunluk-en karşıtlığıdır; komşu dal ise yan yüzlerin ve çeşitli nesne yüzlerinin daha geniş adlandırma alanına uzanır.","focus_only":"Odak dal uzunluğa karşıt ölçüyü açıkça kurar.","gloss":"en ve yan alanında yakın anlam","neighbor_only":"Komşu dal yüz, sayfa ve genişletilmiş nesne türlerini daha ayrıntılı sayar.","neighbor_ref":"root_000867/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin enini, yanını ve enli duruma getirilmesini kapsar."}],"source_phrase_ar":"العرض خلاف الطول (maqayis;ayn;sihah;tahdhib;mufradat)؛ عرض الشيء فهو عريض (maqayis;ayn;sihah;tahdhib)؛ العرض الجانب من كل شيء (tahdhib;mufradat)","source_summary":"Kaynakların ortak çekirdeği, uzunluğa karşıt en boyutu ile bu boyuta bağlı yan kavramıdır; niteleme ve ettirgenleştirme de bu çekirdeğe dayanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العرض الذي يخالف الطول، والعريض، وجعل الشيء عريضا، والجانب أو الناحية من الشيء.","what_is_not_ar":"لا يدخل فيه مجرد الإظهار للغير، ولا الإعراض بمعنى الصد، ولا عرض الدنيا إلا من جهة الأصل الصوري."},"support_links":[]},{"boundary":"Anlam yalnızca belirtilen sunma ve incelemeye çıkarma yapılarında geçerlidir.","branch_kind":"collocation","branch_ref":"root_001001/B002","candidate_links":[{"candidate_id":"cand_2ab01e70a8a6014a953e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"görmeye veya incelemeye sunma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir fail, bir nesneyi muhatabın görmesi veya değerlendirmesi için ortaya koyar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Malın satışa sunulması, askerin denetlenmesi ve kitabın okunup karşılaştırılması bu yapının özel gerçekleşmeleridir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin muhataba, satışa, denetime ya da okumaya çıkarıldığı yapıların tümünü kapsar.","boundary_detail":"Anlam yalnızca belirtilen sunma ve incelemeye çıkarma yapılarında geçerlidir.","branch_image_ar":"عرض الشيء وإبرازه للنظر","concept_gloss":"görmeye veya incelemeye sunma","contextual_glosses":[{"applicability":"Bir şeyi birine göstermek veya değerlendirmesine bırakmak bağlamında doğal karşılıktır.","error_profile":{"adds":"Türkçedeki sunmak fiilinin burada bulunmayan ikram ve bildirme anlamlarını da çağrıştırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir şeyi muhataba yöneltme eylemini korur."},"facet_ids":["F001"],"text":"sunmak","usage_role":"contextual"}],"definition":"Bir şeyi başka birinin görmesi, incelemesi, okuması veya değerlendirmesi için onun önüne getirmek ya da belirli bir amaca sunmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir fail, bir nesneyi muhatabın görmesi veya değerlendirmesi için ortaya koyar."},{"facet_id":"F002","role":"specialization","statement":"Malın satışa sunulması, askerin denetlenmesi ve kitabın okunup karşılaştırılması bu yapının özel gerçekleşmeleridir."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasının görmesine veya değerlendirmesine sunmayı; mal, asker ve kitap gibi belirli nesnelerle açıkça örnekler. Dalın kimliği kendiliğinden görünme değil, bir failin yönelttiği sunmadır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi birine göstermek veya sunmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"malı satışa çıkarmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"askerleri gözden geçirmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kitabı okumak veya başka bir nüshayla karşılaştırmak"}],"lexicalization_note":"Tanım, nesnenin birine, satışa veya incelemeye sunulduğu yapılara bağlıdır; yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sunma eyleminin fail ve amaç sınırını en iyi açıklayan yakın anlamlı komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın yapısı nesneyi muhataba veya incelemeye sunmaktır; komşu dalda hayvanın niteliğini hareket ettirerek ortaya çıkarma gibi daha özel bir sınama da vardır.","focus_only":"Odak dal satış, asker denetimi ve kitap incelemesi gibi yapılara bağlanır.","gloss":"gösterip değerlendirmeye sunma","neighbor_only":"Komşu dal özellikle hayvanı satış veya sınama amacıyla yürütüp yeteneğini ortaya çıkarabilir.","neighbor_ref":"root_000827/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi başkasına göstermek ve değerlendirmeye açmak anlamında örtüşür."}],"source_phrase_ar":"عرض المتاع يعرضه عرضا (maqayis)؛ يعرض علينا المتاع عرضا للبيع والهبة (ayn)؛ عرضت عليه أمر كذا وعرضت له الشيء أظهرته له وأبرزته إليه (sihah)؛ عرضت المتاع وغيره على البيع وكذلك عرض الجند والكتاب (tahdhib)؛ عرضت الشيء على البيع وعلى فلان وعرضنا جهنم (mufradat)","source_summary":"Ortak anlam, bir nesnenin bir muhataba veya belirli bir değerlendirme alanına bilinçli biçimde sunulmasıdır; satış, denetim ve okuma bunun özel bağlamlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الشيء أو الأمر على غيره، وعرض المتاع للبيع، وعرض الكتاب أو القرآن، وعرض الجند، وإبراز جهنم أو غيرها حتى يرى.","what_is_not_ar":"لا يدخل فيه مجرد الظهور من غير فاعل مبرز، ولا الصد والإعراض."},"support_links":["sup_318377b2b29b948dc703"]},{"boundary":"Dal, bir failin sunduğu nesneyi değil, göz önünde beliren şeyi anlatır.","branch_kind":"bare","branch_ref":"root_001001/B003","candidate_links":[{"candidate_id":"cand_98a237407e25b4f6e835","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"uzaktan belirme ve beliren oluşum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, bakan kişiye uzaktan veya bir yönden belirip görünür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ufukta beliren bulut başta olmak üzere geniş görünen oluşumun adı olabilir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem görünme olayını hem de özellikle ufukta beliren oluşumu birlikte temsil eder.","boundary_detail":"Dal, bir failin sunduğu nesneyi değil, göz önünde beliren şeyi anlatır.","branch_image_ar":"العارض البادي من جهة","concept_gloss":"uzaktan belirme ve beliren oluşum","contextual_glosses":[{"applicability":"Bir şeyin bakış alanında uzaktan belirdiği olay bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beliren bulut veya başka oluşumun ad olarak kullanımını vermez.","preserves":"Uzaktan belirme olayını doğal biçimde korur."},"facet_ids":["F001"],"text":"uzaktan görünmek","usage_role":"contextual"}],"definition":"Bir şeyin uzaktan veya belli bir yönden göz önünde belirmesi; ayrıca ufukta genişçe görünen bulut, çekirge sürüsü ya da dağ gibi belirgin oluşumdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, bakan kişiye uzaktan veya bir yönden belirip görünür."},{"facet_id":"F002","role":"specialization","statement":"Ufukta beliren bulut başta olmak üzere geniş görünen oluşumun adı olabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin uzaktan veya bir yönden belirip görünmesini ve bu görünüşün bulut gibi beliren bir varlık adı olmasını destekler. Burada görünme, başkasının sergileme eyleminden bağımsızdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uzaktan belirmek, görünmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"uzaktan beliren oluşum; özellikle bulut kümesi"}],"lexicalization_note":"Tanım yalın belirme ve görünme anlamıyla sınırlıdır; sunma yapılarına taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kendiliğinden belirme ile genel görünme arasındaki sınırı en iyi gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yönlü ve uzaktan belirmeye, ayrıca beliren oluşuma bağlıdır; komşu dal daha genel görünme ve görünür kılma alanını kapsar.","focus_only":"Odak dal uzaktan veya bir yönden beliren oluşumu, özellikle bulutu adlandırabilir.","gloss":"belirme ve görünür olma","neighbor_only":"Komşu dal bir şeyi başkasına görünür kılma ettirgenliğini de kapsar.","neighbor_ref":"root_000097/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin gizlilikten ya da görünmezlikten çıkıp görünmesini anlatır."}],"source_phrase_ar":"أعرض لك الشيء من بعيد إذا ظهر لك وبدا (maqayis)؛ عرض له أمر كذا أي ظهر (sihah)؛ أعرض لك الشيء أي بدا وظهر (tahdhib)؛ العارض البادي عرضه وتارة يخص بالسحاب (mufradat)","source_summary":"Ortak çekirdek, bir şeyin bakana doğru bir yönden belirip görünmesidir; bulut bu görünüşün öne çıkan özel adlandırmasıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه ما بدا وظهر للإنسان، وما استقبل من بعيد، والسحاب العارض، والجراد الكثير الذي يملأ الأفق، والجبل أو الشيء البادي عرضه.","what_is_not_ar":"لا يدخل فيه العرض بفعل مبرز للغير، ولا الإعراض بمعنى التولي."},"support_links":["sup_399d68221f85ed7c82ae"]},{"boundary":"Çekirdek araya girip engel oluşturmadır; müdahale ve saldırı kullanımları bu çekirdeğe bağlı özel yapılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B004","candidate_links":[{"candidate_id":"cand_ff5bb4621c1a7c8a9247","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"araya girip engelleme ve karşısına dikilme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık araya girerek başka bir varlığın geçişini veya ilerleyişini engeller."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin bir işe kendini sokması veya birinin karşısına dikilmesi olarak uygulanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir yapıda insanları karşılaşılan yönden ayrım gözetmeden öldürme veya yakalamayı anlatır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel engeli, müdahaleyi ve bunlara bağlı özel saldırı yapısını aynı çekirdekte toplar.","boundary_detail":"Çekirdek araya girip engel oluşturmadır; müdahale ve saldırı kullanımları bu çekirdeğe bağlı özel yapılardır.","branch_image_ar":"الاعتراض حيلولة ومقابلة في الطريق","concept_gloss":"araya girip engelleme ve karşısına dikilme","contextual_glosses":[{"applicability":"Bir varlığın geçişi fiziksel veya mecazi olarak engellendiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşe kendini sokma ve özel saldırı kullanımlarını kapsamaz.","preserves":"Karşıya çıkma ve engelleme ilişkisini korur."},"facet_ids":["F001"],"text":"önünü kesmek","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyin önüne veya arasına girerek geçişini engellemesi ya da bir kişinin bir işe kendini sokup karşısına dikilmesidir. Belirli bir yapıda, karşılaşılan insanları ayrım gözetmeden öldürme veya yakalama anlamına uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık araya girerek başka bir varlığın geçişini veya ilerleyişini engeller."},{"facet_id":"F002","role":"extension","statement":"Kişinin bir işe kendini sokması veya birinin karşısına dikilmesi olarak uygulanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir yapıda insanları karşılaşılan yönden ayrım gözetmeden öldürme veya yakalamayı anlatır."}],"identity_rationale":"Kaynak ifadesi araya girme, önünü kesme ve engel olma çekirdeğini doğrular; ayrıca işe kendini sokma ve insanları ayrım gözetmeden öldürme gibi yapılara uzanır. Bu yüzden dal yalnızca yoldaki fiziksel karşılaşma diye daraltılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"önüne geçip engel olmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birinin karşısına dikilmek, ona sataşmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"insanları ayrım gözetmeden öldürmek veya yakalamak"}],"lexicalization_note":"Yalın engel olma ile belirli müdahale ve ayrım gözetmeyen saldırı yapıları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; araya girme koşulunu genel engellemeden ayıran komşu en yararlı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı yanı, fiziksel ya da mecazi olarak araya girip karşıya dikilmektir; komşu dalda araya yerleşme şart olmadan genel alıkoyma yeterlidir.","focus_only":"Odak dal araya girme, işe müdahale etme ve özel saldırı yapısını kapsar.","gloss":"engelleme ve önünü kesme","neighbor_only":"Komşu dal failin birini istediği eylemden alıkoymasına ve vazgeçirmesine odaklanır.","neighbor_ref":"root_001448/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin veya şeyin hedefine ulaşmasını engelleme alanında örtüşür."}],"source_phrase_ar":"اعترض في الأمر إذا أدخل نفسه فيه (maqayis)؛ عرض القوم على السيف (ayn)؛ اعترض الشيء دون الشيء أي حال دونه (sihah)؛ كل مانع منعك فهو عارض (tahdhib)؛ اعترض الشيء في حلقه وقف فيه بالعرض (mufradat)","source_summary":"Kaynakların birleşik anlatımı, araya girerek engelleme çekirdeğini; işe müdahale etme ve karşılaşılan insanlara ayrım gözetmeden saldırma uzantılarıyla birlikte verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اعترض الشيء إذا حال ومنع، وعرض العارض، والتعرض للناس، والاعتراض في الطريق أو الأمر، واستعراض الناس قتلا أو أخذا من أي وجه.","what_is_not_ar":"لا يدخل فيه العرض الهادئ بمعنى الإظهار، ولا المعارضة بمعنى المقابلة بالمثل إلا إذا كان فيها حيلولة."},"support_links":["sup_f82496056045a990aee9"]},{"boundary":"Dal, dikkati ve yönelişi geri çekerek yüz çevirme eylemiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001001/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"yüz çevirip ilgiyi kesme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, birinden veya bir konudan yönelişini geri çekip yüz çevirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedensel olarak yanını gösterip dönme, ilgiyi kesmenin görünür gerçekleşmesidir."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiden veya konudan bedensel ya da tutumsal olarak uzaklaşmayı birlikte anlatır.","boundary_detail":"Dal, dikkati ve yönelişi geri çekerek yüz çevirme eylemiyle sınırlıdır.","branch_image_ar":"الإعراض تولية العرض","concept_gloss":"yüz çevirip ilgiyi kesme","contextual_glosses":[{"applicability":"Bir kişi veya konuyla ilgilenmeyi reddetme bağlamında doğal ve doğrudan karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel dönmeyi ve mecazi ilgisizleşmeyi birlikte korur."},"facet_ids":["F001","F002"],"text":"yüz çevirmek","usage_role":"general"}],"definition":"Bir kişiye veya konuya yönelmeyi bırakıp ondan yüz çevirmek, ilgiyi kesmek ve yanını dönerek uzaklaşmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, birinden veya bir konudan yönelişini geri çekip yüz çevirir."},{"facet_id":"F002","role":"extension","statement":"Bedensel olarak yanını gösterip dönme, ilgiyi kesmenin görünür gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi bir kişiden veya işten yüz çevirip uzaklaşmayı, yanını göstererek dönme imgesiyle açıkça destekler. Bu anlam görünme, sunma veya fiziksel en ölçüsü değildir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"birinden yüz çevirmek, onunla ilgiyi kesmek"}],"lexicalization_note":"Tanım yalın yüz çevirme anlamını verir; engelleme ya da gösterme yapıları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öznenin yüz çevirmesiyle başkasını uzaklaştırma arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal öznenin kendi dönüşüne ve ilgisini çekmesine bağlıdır; komşu dal hem öznenin uzaklaşmasını hem de başka birini engelleyip uzaklaştırmasını içerir.","focus_only":"Odak dal öznenin kendisinin yüz çevirip ilgisini kesmesini anlatır.","gloss":"yüz çevirme ve uzaklaşma","neighbor_only":"Komşu dal başkasını bir şeyden engelleyip uzaklaştıran ettirgen kullanımı da kapsar.","neighbor_ref":"root_000848/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi veya şeyden yönelişi kesip uzaklaşmayı anlatabilir."}],"source_phrase_ar":"أعرضت عن فلان وأعرضت عن هذا الأمر وأعرض بوجهه (maqayis)؛ الإعراض عن الشيء الصد عنه (sihah)؛ أعرض عني فمعناه ولى مبديا عرضه (mufradat)","source_summary":"Ortak çekirdek, bir kişiden veya işten yüz çevirip ilgiyi kesmektir; yanını dönme bu kopuşun bedensel görünümünü açıklar.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه أعرض عن فلان أو عن الأمر أو بوجهه، والصد عنه، والتولي مبديا الجانب.","what_is_not_ar":"لا يدخل فيه الظهور والإبراز، ولا مجرد العرض خلاف الطول."},"support_links":[]},{"boundary":"Karşılıklılık veya denklik şarttır; sırf engelleme ve genel muhalefet bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"denk karşılık verme, karşılaştırma veya değişme","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf hareket veya eylem bakımından birbirinin hizasında ya da dengi olur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki metni yan yana getirip karşılaştırma, denklik ilişkisinin özel yapısıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir malı başka bir mal karşılığında değiştirme, karşılıklı denk verme yapısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareket ve eylem denkliğini, metin karşılaştırmasını ve mal değişimini ortak ilişkileriyle temsil eder.","boundary_detail":"Karşılıklılık veya denklik şarttır; sırf engelleme ve genel muhalefet bu dala girmez.","branch_image_ar":"المعارضة مقابلة ومماثلة ومبادلة","concept_gloss":"denk karşılık verme, karşılaştırma veya değişme","contextual_glosses":[{"applicability":"Birinin yaptığına denk bir eylemle karşılık verme bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hizada ilerleme, metin karşılaştırma ve mal değişimi kullanımlarını vermez.","preserves":"Eylemler arasındaki denklik ve karşılıklılığı korur."},"facet_ids":["F001"],"text":"aynısıyla karşılık vermek","usage_role":"contextual"}],"definition":"Başkasının hizasında ilerlemek veya yaptığına denk bir eylemle karşılık vermek; belirli yapılarda iki metni karşılaştırmak ya da bir malı başka bir malla değişmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf hareket veya eylem bakımından birbirinin hizasında ya da dengi olur."},{"facet_id":"F002","role":"specialization","statement":"İki metni yan yana getirip karşılaştırma, denklik ilişkisinin özel yapısıdır."},{"facet_id":"F003","role":"specialization","statement":"Bir malı başka bir mal karşılığında değiştirme, karşılıklı denk verme yapısıdır."}],"identity_rationale":"Kaynak ifadesi geniş anlamda karşı çıkmayı değil, birinin hizasında ilerlemeyi, yaptığına denk bir karşılık vermeyi, iki metni karşılaştırmayı ve mal değişimini destekler. Bu nedenle dal, genel muhalefet veya sözlü tartışma yerine karşılıklı denklik ve eşleştirme çevresinde tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birinin hizasında gitmek veya yaptığına denk karşılık vermek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"iki metni karşılaştırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir malı başka bir malla değiştirmek"}],"lexicalization_note":"Hizada ilerleme çekirdeği ile metin karşılaştırma ve mal değişimi yapıları ayrı, fakat denklik ilişkisi altında tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel denklik ile bu dalın yapı bağımlı karşılıklılığı arasındaki farkı en iyi gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli karşılıklı eylem ve karşılaştırma yapılarına bağlıdır; komşu dal denklik ve eşdeğerlik durumunu daha genel bir ilişki olarak kurar.","focus_only":"Odak dal hizada ilerleme, metin karşılaştırma ve mal değişimi yapılarını birlikte taşır.","gloss":"denklik ve misliyle karşılık","neighbor_only":"Komşu dal eşlik, evlilikte denklik, savaşta denk güç ve ödüllendirme gibi daha geniş denklik alanlarını kapsar.","neighbor_ref":"root_001305/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da iki tarafın denkliği ve bir eyleme misliyle karşılık verilmesi alanında örtüşür."}],"source_phrase_ar":"عارضت فلانا في السير إذا سرت حياله وعارضته مثل ما صنع (maqayis)؛ عارضته في المسير وعارضت كتابي بكتابه (sihah)؛ عارضته بمتاع أو دابة معارضة إذا بادلته به وعارضت كتابي بكتابه (tahdhib)","source_summary":"Kaynakların ortak alanı, iki tarafı hizada veya karşılıklı denk konuma getirmedir; hareket, eyleme karşılık verme, metin karşılaştırma ve değiş tokuş bunun farklı gerçekleşmeleridir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه عارضه في السير، وعارضه بمثل صنيعه، والمعارضة في الكتاب أو الكلام، والمبادلة بالمتاع أو الدابة، والمباراة.","what_is_not_ar":"لا يدخل فيه الاعتراض المانع إذا لم تكن مقابلة أو مماثلة، ولا التعريض غير الصريح."},"support_links":[]},{"boundary":"Dalın ayırıcı niteliği sonradan ve çoğu kez beklenmedik biçimde ortaya çıkma ile kalıcı olmamadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"sonradan ortaya çıkan kalıcı olmayan durum veya nitelik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir durum veya nitelik sonradan ortaya çıkar ve kalıcı değildir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynağı bilinmeden isabet eden ok, beklenmedik gelişin somut örneğidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birine ansızın gönül bağlama, hazırlıksız ortaya çıkma özelliğine bağlı bir kullanımdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel durum ve nitelik çekirdeğini sonradan ortaya çıkma ve kalıcı olmama koşullarıyla temsil eder.","boundary_detail":"Dalın ayırıcı niteliği sonradan ve çoğu kez beklenmedik biçimde ortaya çıkma ile kalıcı olmamadır.","branch_image_ar":"العرض الطارئ الذي يعرض ثم يزول","concept_gloss":"sonradan ortaya çıkan kalıcı olmayan durum veya nitelik","contextual_glosses":[{"applicability":"Kişiye sonradan gelen ateş veya hastalık bağlamında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık dışındaki olayları ve özel beklenmedik yapıları kapsamaz.","preserves":"Sonradan gelen ve kalıcı olmayan hastalık yönünü korur."},"facet_ids":["F001"],"text":"geçici rahatsızlık","usage_role":"contextual"}],"definition":"Bir şeyde sonradan ortaya çıkan ve kalıcı olmayan durum veya niteliktir. Kişi bağlamında hastalık veya başa gelen olay; belirli yapılarda ise kaynağı bilinmeden gelen bir ok ya da ansızın doğan gönül bağını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir durum veya nitelik sonradan ortaya çıkar ve kalıcı değildir."},{"facet_id":"F002","role":"example","statement":"Kaynağı bilinmeden isabet eden ok, beklenmedik gelişin somut örneğidir."},{"facet_id":"F003","role":"associated_use","statement":"Birine ansızın gönül bağlama, hazırlıksız ortaya çıkma özelliğine bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi kişiye sonradan gelen hastalık veya olay ile kalıcılığı olmayan durumu açıkça birleştirir. Beklenmedik ok ve ansızın doğan bağlanma, bu geliş ve geçicilik çekirdeğinin özel yapılarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sonradan gelen geçici hastalık veya olay"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"nereden atıldığı bilinmeden isabet eden ok"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birine ansızın gönül bağlamak"}],"lexicalization_note":"Geçici olay çekirdeği ile beklenmedik ok ve ansızın bağlanma yapıları birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geçicilik ile musibet niteliği arasındaki sınırı en açık gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal olayın sonradan belirmesi ve kalıcı olmamasını öne çıkarır; komşu dal ise olayın musibet niteliğini kurar ve geçicilik şartı taşımaz.","focus_only":"Odak dal geçiciliği ve ansızın ortaya çıkmayı kurucu özellik sayar.","gloss":"başa gelen olay ve geçici durum","neighbor_only":"Komşu dal başa gelen olayın özellikle bela, felaket veya nöbet oluşuna odaklanır.","neighbor_ref":"root_001562/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin başına gelen hastalık veya olumsuz olay alanında buluşur."}],"source_phrase_ar":"العرض من أحداث الدهر كالمرض ونحوه (maqayis)؛ عرضه عارض من الحمى ونحوها (sihah)؛ العرض الأمر يعرض للرجل يبتلى به وسهم عرض (tahdhib)؛ العرض ما لا يكون له ثبات (mufradat)","source_summary":"Ortak çekirdek, sonradan ortaya çıkan ve kalıcılığı olmayan durum veya niteliktir; hastalık, kişinin başına gelen olay, beklenmedik isabet ve ansızın bağlanma bu çekirdeğin farklı bağlamlarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العارض من الحمى أو السقم، وأحداث الدهر، والمرض والموت ونحوهما، وسهم عرض، والحب أو الرأي الذي يقع بغتة، والعرض الكلامي لما لا ثبات له.","what_is_not_ar":"لا يدخل فيه متاع الدنيا من حيث هو مال أو بدل إلا إذا أريد طروؤه وعدم ثباته."},"support_links":[]},{"boundary":"Dal maddi dünya malı ve karşılık olarak verilen eşya ile sınırlıdır; geçici olay anlamı ancak tarihsel çağrışım düzeyindedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"dünya malı, nakit dışı eşya ve mal karşılığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Elde edilebilir dünyevi mal, eşya veya payı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nakit para dışında kalan ticari eşyalar bu dalın özel alanıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hak veya alacak yerine eşya verme, malın karşılık işlevine bağlı bir yapıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel dünyevi payı, ticari eşyayı ve hak yerine verilen malı birlikte açıklar.","boundary_detail":"Dal maddi dünya malı ve karşılık olarak verilen eşya ile sınırlıdır; geçici olay anlamı ancak tarihsel çağrışım düzeyindedir.","branch_image_ar":"العرض متاع وبدل وحظ من الدنيا","concept_gloss":"dünya malı, nakit dışı eşya ve mal karşılığı","contextual_glosses":[{"applicability":"Nakit para dışında alınıp satılan mallar söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel dünyevi payı ve hak yerine mal verme yapısını kapsamaz.","preserves":"Nakit dışı mal ve eşya yönünü korur."},"facet_ids":["F002"],"text":"ticari eşya","usage_role":"contextual"}],"definition":"Dünyaya ait elde edilebilir mal, eşya veya pay; özellikle nakit para dışında kalan ticari eşyadır. Belirli bir yapıda, bir alacak ya da hak yerine verilen malı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Elde edilebilir dünyevi mal, eşya veya payı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Nakit para dışında kalan ticari eşyalar bu dalın özel alanıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bir hak veya alacak yerine eşya verme, malın karşılık işlevine bağlı bir yapıdır."}],"identity_rationale":"Kaynak ifadesi dünya malı, nakit dışı eşya ve kolay elde edilen dünyevi payı açıkça destekler. Bir hak yerine verilen mal da bu maddi değer alanındaki belirli bir değişim yapısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dünya malı ve geçici dünyevi pay"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"nakit dışındaki ticari eşyalar"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hakkı yerine bir mal vermek"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"yol azığı olarak verilen yiyecek veya aileye götürülen hediye"}],"lexicalization_note":"Dünya malı ve nakit dışı eşya çekirdeği, hak yerine mal verme yapısından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel maddi mal ile ev eşyası alanını ayıran komşu en açıklayıcı karşılaştırma olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ticari ve karşılık işlevli nakit dışı malı da kapsayan daha soyut bir sınıftır; komşu dal ev eşyası ve çokluk görünümüne bağlıdır.","focus_only":"Odak dal genel dünya malını, nakit dışı ticari eşyayı ve mal karşılığını kapsar.","gloss":"eşya ve maddi mal","neighbor_only":"Komşu dal özellikle ev eşyası, döşek ve çok miktarda mal edinme alanındadır.","neighbor_ref":"root_000010/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da sahip olunan taşınır eşya ve maddi mal alanında buluşur."}],"source_phrase_ar":"العرض طمع الدنيا والدنيا عرض حاضر (maqayis)؛ العرض المتاع والعروض الأمتعة (sihah)؛ جميع متاع الدنيا عرض وما خالف الثمنين عروض (tahdhib)؛ تريدون عرض الدنيا ولو كان عرضا قريبا أي مطلبا سهلا (mufradat)","source_summary":"Ortak anlatım, elde edilebilir dünya malını ve özellikle nakit dışı eşyayı kapsar; kolay kazanç ve hak yerine eşya verme bu maddi değer alanına bağlıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الدنيا، والمتاع غير النقد، والعروض، وما يعطى بدلا عن حق، وما يعرض من المال أو العطاء.","what_is_not_ar":"لا يدخل فيه الحدث العارض كالمرض إلا بجامع الطروء، ولا العرض الجسدي أو الشرف."},"support_links":[]},{"boundary":"Kişinin korunmuş benliği ve bedeni ile yüzün yan bölümü ayrı alt kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"kişinin bedeni, saygınlığı ve yüzünün yanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin bedeni veya benliği, korunması gereken kişisel alan olarak adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin soyu ve kınanmaktan koruduğu toplumsal saygınlığı bu alana girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yüzün, yanağın veya ön dişlerin yan kısmı için bedensel bir adlandırma vardır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişisel bütünlük ve itibar alanıyla yüzün yan bölümünü birlikte, fakat ayırt ederek temsil eder.","boundary_detail":"Kişinin korunmuş benliği ve bedeni ile yüzün yan bölümü ayrı alt kullanımlardır.","branch_image_ar":"عرض الإنسان حماه وبدنه وظاهر وجهه","concept_gloss":"kişinin bedeni, saygınlığı ve yüzünün yanı","contextual_glosses":[{"applicability":"Bir kişinin kınanmaktan ve aşağılanmaktan koruduğu itibarı söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Beden, benlik ve yüzün yan bölümü kullanımlarını vermez.","preserves":"Korunan toplumsal saygınlık yönünü korur."},"facet_ids":["F002"],"text":"kişisel saygınlık","usage_role":"contextual"}],"definition":"Kişinin bedeni, benliği veya eleştiriden koruduğu toplumsal saygınlığıdır. Ayrı bir bedensel kullanımda yanağın, yüzün ya da ön dişlerin yan tarafını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin bedeni veya benliği, korunması gereken kişisel alan olarak adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Kişinin soyu ve kınanmaktan koruduğu toplumsal saygınlığı bu alana girer."},{"facet_id":"F003","role":"specialization","statement":"Yüzün, yanağın veya ön dişlerin yan kısmı için bedensel bir adlandırma vardır."}],"identity_rationale":"Kaynak ifadesi kişinin bedeni, benliği ve toplumsal saygınlığı yanında yüzün veya dişlerin yan kısmını da aynı dalda toplar. Bu nedenle dal yalnızca korunmuş onur diye daraltılamaz; bedensel ve itibari kullanımlar açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kişinin bedeni, benliği veya saygınlığı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ayıplanacak yanı olmayan, itibarı temiz"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yüzün veya yanağın yanı; ön dişlerin yan bölümü"}],"lexicalization_note":"Kişinin bedeni ve saygınlığına ilişkin yalın kullanım, temiz saygınlık tamlaması ve yüz yanı kullanımı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişisel korunma alanıyla soya dayalı itibar arasındaki sınırı en iyi gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda saygınlık, beden ve benlikle birlikte geniş bir kişisel korunma alanıdır; komşu dal ise soy ve köklülüğe dayalı itibarı özelleştirir.","focus_only":"Odak dal beden, benlik ve yüz yanı gibi bedensel kullanımları da taşır.","gloss":"saygınlık ve soy itibarı","neighbor_only":"Komşu dal saygınlığı özellikle soy kökeni, köklülük ve iffet üzerinden kurar.","neighbor_ref":"root_000875/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin toplumsal itibarı ve korunmuş saygınlığı alanında örtüşür."}],"source_phrase_ar":"العرض عرض الإنسان حسبة أو نفسه (maqayis)؛ العرض الجسد والنفس والحسب (sihah)؛ العرض بدن كل الحيوان والنفس وحسبه (tahdhib)؛ العارض بالخد وتارة بالسن والعوارض للثنايا (mufradat)","source_summary":"Kaynaklar kişinin bedenini, benliğini ve saygınlığını korunan kişisel alan altında birleştirir; yüz ve dişlerin yan bölümü de ayrı bir bedensel adlandırma olarak verilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الإنسان بمعنى حسبه أو نفسه أو بدنه أو ريحه، ونقاء العرض، وعارضا الوجه، والعوارض من الأسنان أو الخدود.","what_is_not_ar":"لا يدخل فيه العرض بمعنى المتاع، ولا مجرد عرض الشيء للبيع."},"support_links":[]},{"boundary":"Dal, sözün veya yazının doğrudan belirtilmeyen ikinci anlamına dayanır; genel mecazın tamamını kapsamaz.","branch_kind":"bare","branch_ref":"root_001001/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"üstü kapalı, çift yönlü anlatım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Konuşan kişi niyetini doğrudan söylemez, sözün başka bir yönünden anlaşılmasına bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözün görünür ve örtük iki anlam taşıması dolaylı anlatımın belirgin yapısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Niyetin doğrudan söylenmeyip sözün görünür anlamı altından sezdirildiği kullanımları kapsar.","boundary_detail":"Dal, sözün veya yazının doğrudan belirtilmeyen ikinci anlamına dayanır; genel mecazın tamamını kapsamaz.","branch_image_ar":"معاريض الكلام وجه غير مصرح به","concept_gloss":"üstü kapalı, çift yönlü anlatım","contextual_glosses":[{"applicability":"Bir niyetin açıkça değil sezdirilerek anlatıldığı gündelik bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Açık söylememe ve dolaylı biçimde sezdirme işlevini korur."},"facet_ids":["F001","F002"],"text":"üstü kapalı söylemek","usage_role":"general"}],"definition":"Bir düşünceyi açıkça söylemek yerine, sözün görünür anlamı altında anlaşılabilecek başka bir yön bırakarak dolaylı biçimde anlatmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Konuşan kişi niyetini doğrudan söylemez, sözün başka bir yönünden anlaşılmasına bırakır."},{"facet_id":"F002","role":"specialization","statement":"Sözün görünür ve örtük iki anlam taşıması dolaylı anlatımın belirgin yapısıdır."}],"identity_rationale":"Kaynak ifadesi açık söylemenin karşıtı olan, görünür sözün altında başka bir anlam taşıyan dolaylı anlatımı açıkça tanımlar. Evlilik niyetini üstü kapalı bildirme ve harfleri açık yazmama bunun bağlama bağlı örnekleridir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"görünür anlamının altında başka bir anlam taşıyan sözler"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"açıkça söylemeyip üstü kapalı anlatma"}],"lexicalization_note":"Tanım yalın dolaylı anlatım çekirdeğini verir; belirli söz ve yazı örnekleri tüm dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bilinçli üstü kapalılık ile genel anlam çıkarımı arasındaki sınırı en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda konuşan kişi doğrudan söylemek yerine bilinçli bir örtük yön bırakır; komşu dalda yüzeyden anlama geçiş daha genel olup çift anlamlı söz şart değildir.","focus_only":"Odak dal açık söyleyişin karşıtı olan çift yönlü ve üstü kapalı söz yapısını şart koşar.","gloss":"sözden örtük anlamı sezdirme","neighbor_only":"Komşu dal sözün görünür biçiminden genel anlamına, niyetine veya işaretine yönelmeyi daha geniş kapsar.","neighbor_ref":"root_001349/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sözün yüzeyinin ötesindeki anlam veya konuşma niyetine yönelir."}],"source_phrase_ar":"معاريض الكلام يخرج في معرض غير لفظه الظاهر (maqayis)؛ التعريض خلاف التصريح والمعاريض في الكلام (sihah)؛ التعريض ما كان خلاف التصريح والمعاريض من الكلام (tahdhib)؛ التعريض كلام له وجهان من صدق وكذب أو ظاهر وباطن (mufradat)","source_summary":"Ortak çekirdek, açık bildirim yerine görünür sözün altında ikinci bir anlam veya niyet bırakmaktır; farklı söz ve yazı bağlamları bu dolaylılığı örnekler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه التعريض خلاف التصريح، والمعاريض والتورية، والكلام الذي له ظاهر وباطن أو وجهان، والتعريض في خطبة النساء، وتعريض الكاتب إذا لم يبين.","what_is_not_ar":"لا يدخل فيه المعارضة بمعنى المقابلة بالمثل، ولا العرض بمعنى الإظهار الحسي."},"support_links":[]},{"boundary":"Hedef olarak ortaya konma ile bir işe güçlü ve hazır olma ayrı kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"hedef olarak ortaya koyma veya bir işe hazır olma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey, belirli bir etkiye açık hedef olarak ortaya konur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaya konan şey bağlama göre engel veya sürekli saldırı hedefi olabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yolculuğa ayrılan hayvanın bu işe güçlü ve hazır olması özel bir yapıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maruz bırakılma çekirdeğini ve yolculuk için güçlü-hazır olma yapısını birlikte belirtir.","boundary_detail":"Hedef olarak ortaya konma ile bir işe güçlü ve hazır olma ayrı kullanımlardır.","branch_image_ar":"العرضة نصب وقوة للتعرض","concept_gloss":"hedef olarak ortaya koyma veya bir işe hazır olma","contextual_glosses":[{"applicability":"Bir kişi veya şey başkalarının etkisine veya saldırısına açık bırakıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolculuğa güçlü ve hazır olma yapısını kapsamaz.","preserves":"Ortaya koyma ve etkiye açık bırakma yönünü korur."},"facet_ids":["F001","F002"],"text":"hedef hâline getirmek","usage_role":"contextual"}],"definition":"Bir kişi veya şeyi başkalarının etkisine, saldırısına ya da kullanımına açık bir hedef olarak ortaya koymaktır. Belirli bir yapıda, bir hayvanın yolculuğa dayanacak güçte ve hazır olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey, belirli bir etkiye açık hedef olarak ortaya konur."},{"facet_id":"F002","role":"extension","statement":"Ortaya konan şey bağlama göre engel veya sürekli saldırı hedefi olabilir."},{"facet_id":"F003","role":"specialization","statement":"Yolculuğa ayrılan hayvanın bu işe güçlü ve hazır olması özel bir yapıdır."}],"identity_rationale":"Kaynak ifadesi birini veya bir şeyi belirli bir etkiye açık hedef olarak yerleştirmeyi ve yolculuk gibi bir işe güçlü veya hazır olmayı destekler. Engel olma yorumu belirli bağlama bağlıdır; dalın tamamı yalnızca engel diye tanımlanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"hedef veya engel olarak ortaya konmuş şey"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yolculuğa dayanıklı ve hazır deve"}],"lexicalization_note":"Genel hedef veya maruz kalma kullanımı, yolculuğa güçlü olma tamlamasından ayrı tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hedef olarak ortaya konma ile genel hazırlık arasındaki sınırı en iyi açıklayan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda hazırlık, özellikle bir etkiye maruz kalacak biçimde ortaya konma ilişkisinden doğar; komşu dalda böyle bir hedef veya maruz kalma koşulu yoktur.","focus_only":"Odak dal hedef olarak ortaya konma ve etkiye açık bırakılma anlamını taşır.","gloss":"hazır ve elverişli olma","neighbor_only":"Komşu dal bir şeyi genel olarak hazırlama, hazır bulundurma veya yapabilecek güçte olma anlamındadır.","neighbor_ref":"root_001685/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişi veya şeyin belirli bir iş için hazır ya da elverişli olmasını anlatabilir."}],"source_phrase_ar":"فلان عرضة للناس لا يزالون يقعون فيه (maqayis)؛ فلان عرضة لذاك أي مقرن له قوي عليه وجعلت فلانا عرضة لكذا أي نصبته له (sihah)؛ لا تجعلوا الحلف بالله معترضا مانعا وجعلت فلانا عرضة أي نصبته له (tahdhib)؛ العرضة ما يجعل معرضا للشيء ولا تجعلوا الله عرضة لأيمانكم (mufradat)","source_summary":"Kaynakların ortak alanı, bir şeyi belirli bir etkiye açık biçimde ortaya koymaktır; sürekli hedef olma, engel oluşturma ve yolculuğa hazır güçte bulunma bağlama göre ayrışır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه جعل الشيء عرضة أي منصوبا أو معرضا، وعرضة للأيمان أو للشر أو للناس، والقوة على الشيء كناقة عرضة للسفر.","what_is_not_ar":"لا يدخل فيه الاعتراض المانع إلا إذا أفاد كونه نصبا أو عائقا، ولا العرض بمعنى المتاع."},"support_links":[]},{"boundary":"Dal yalnızca hareket içindeki yana sapma ve doğrultuyu koruyamama durumunu anlatır.","branch_kind":"bare","branch_ref":"root_001001/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"yana saparak ilerleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvan hareket ederken düz doğrultuyu korumaz ve yana sapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu yana sapmalı yürüyüş hayvanın güç idare edilmesi veya zor yürümesiyle ilişkilidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dağda sağa sola yönelerek ilerleme, aynı doğrusal olmayan hareketin insan bağlamındaki uzantısıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın veya yolcunun doğrultuyu korumadan sağa sola yöneldiği hareketi temsil eder.","boundary_detail":"Dal yalnızca hareket içindeki yana sapma ve doğrultuyu koruyamama durumunu anlatır.","branch_image_ar":"السير عارضا وصعوبة الاستقامة","concept_gloss":"yana saparak ilerleme","contextual_glosses":[{"applicability":"Düz bir yol tutamayan hayvan veya kişi hareketi için doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanın zor idare edilmesi ve yanını gösterme ayrıntılarını açıkça vermez.","preserves":"Doğrultudan yana saparak ilerleme biçimini korur."},"facet_ids":["F001","F003"],"text":"sağa sola saparak gitmek","usage_role":"contextual"}],"definition":"Bir hayvanın veya kişinin düz doğrultuda ilerlemeyip yana ya da sağa sola saparak gitmesidir. Bazı hayvan kullanımlarında yanını göstererek koşma veya zor idare edilme bu harekete eşlik eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvan hareket ederken düz doğrultuyu korumaz ve yana sapar."},{"facet_id":"F002","role":"specialization","statement":"Bu yana sapmalı yürüyüş hayvanın güç idare edilmesi veya zor yürümesiyle ilişkilidir."},{"facet_id":"F003","role":"extension","statement":"Dağda sağa sola yönelerek ilerleme, aynı doğrusal olmayan hareketin insan bağlamındaki uzantısıdır."}],"identity_rationale":"Kaynak ifadesi hayvanın düz ilerlemeyip yanını göstererek veya sağa sola saparak gitmesini ve bu yürüyüşteki zorluğu açıkça destekler. Dağda sağa sola yönelme de aynı doğrusal olmayan hareket özelliğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"atın koşarken yanını göstererek veya yana saparak gitmesi"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"yürüyüşü zor ve doğrultusunu korumayan dişi deve"}],"lexicalization_note":"Tanım yalın hareket ve yürüyüş anlamıyla sınırlıdır; durağan en ölçüsü bu dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yana sapmalı yürüyüşü durdurulamayan ileri hareketten ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalda belirleyici biçim yana sapma ve düzgün yürüyememedir; komşu dalda belirleyici güç, ileri atılma ve durdurulamamadır.","focus_only":"Odak dal hareketin yana sapmasına ve doğrultusuz güçlüğüne odaklanır.","gloss":"zor denetlenen hayvan hareketi","neighbor_only":"Komşu dal hayvanın biniciyi dinlemeden güçlü ve durdurulamaz biçimde ileri gitmesini anlatır.","neighbor_ref":"root_000257/B001","relation_type":"same_field","shared_zone":"Her iki dal da hayvanın sürücünün istediği doğrultuda kolayca yönetilemeyen hareketini konu alır."}],"source_phrase_ar":"عرض الفرس في عدوه كأنه يرى الناظر عرضه (maqayis)؛ عرض الفرس في عدوه إذا مر عارضا على جنب واحد (ayn)؛ اعترض الفرس في رسنه لم يستقم لقائده وناقة عرضية فيها صعوبة (sihah)؛ تعرض فلان في الجبل أخذ يمينا وشمالا (tahdhib)؛ اعترض الفرس في مشيه وفيه عرضية أي اعتراض في مشيه من الصعوبة (mufradat)","source_summary":"Ortak çekirdek, hareket sırasında düz doğrultudan yana sapmadır; hayvanın zor idare edilmesi ve dağda sağa sola ilerleme bu hareket biçiminin bağlamlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عرض الفرس في عدوه، واعتراض الفرس أو البعير إذا لم يستقم، والناقة العرضية أو العروض الصعبة، والتعرض في الجبل يمينا وشمالا.","what_is_not_ar":"لا يدخل فيه العرض خلاف الطول إذا لم يدل على حركة أو صعوبة سير."},"support_links":[]},{"boundary":"Dal, somut bir nesnenin enine yerleştirilmesi veya yana yönelmesiyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001001/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"enine yerleştirme, enine parça ve yana giden ok","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, başka bir nesneye göre enine gelecek biçimde yerleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapı veya taşıma düzenindeki enine kiriş, bu yönelimin yapısal nesnesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yana doğru giden veya tüyü bulunmayan özel ok, yönelime bağlı bir araç adıdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Enine yönelimi eylem, yapısal parça ve özel araç türleriyle birlikte temsil eder.","boundary_detail":"Dal, somut bir nesnenin enine yerleştirilmesi veya yana yönelmesiyle sınırlıdır.","branch_image_ar":"الشيء الموضوع عرضا أو المعترض عرضيا","concept_gloss":"enine yerleştirme, enine parça ve yana giden ok","contextual_glosses":[{"applicability":"Bir çubuk veya benzeri nesne başka bir nesnenin üzerine enine yerleştirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapısal parça ve özel ok adlarını kapsamaz.","preserves":"Enine yönelimi ve yerleştirme işlemini korur."},"facet_ids":["F001"],"text":"enlemesine koymak","usage_role":"contextual"}],"definition":"Bir nesneyi başka bir nesnenin üzerine veya açıklığa enine yerleştirmek; ayrıca enine duran taşıyıcı parça ya da yana doğru giden özel ok gibi somut nesnelerdir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, başka bir nesneye göre enine gelecek biçimde yerleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Kapı veya taşıma düzenindeki enine kiriş, bu yönelimin yapısal nesnesidir."},{"facet_id":"F003","role":"specialization","statement":"Yana doğru giden veya tüyü bulunmayan özel ok, yönelime bağlı bir araç adıdır."}],"identity_rationale":"Kaynak ifadesi bir çubuğu enlemesine yerleştirme eylemini, enine duran kapı ve taşıyıcı parçaları ve yana doğru giden özel oku açıkça aynı uzamsal yönelim altında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"çubuğu kabın üzerine enlemesine koymak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tüysüz veya yana doğru giden özel ok"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kapı sövelerini üstten tutan enine kiriş"}],"lexicalization_note":"Enine yerleştirme yapısı, enine taşıyıcı parça ve özel ok adlarından ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel enine yönelim ile özel taşıyıcı kiriş arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal enine yönelime dayalı daha geniş bir eylem ve nesne alanıdır; komşu dal işlevi belirlenmiş özel bir taşıyıcı kiriş adıdır.","focus_only":"Odak dal enine yerleştirme eylemini, çeşitli enine parçaları ve özel oku kapsar.","gloss":"enine konan taşıyıcı parça","neighbor_only":"Komşu dal özellikle asma çubuklarını veya ahşap uçlarını taşıyan tek tür enine kiriştir.","neighbor_ref":"root_000243/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da başka parçaları taşıyacak biçimde enine konan ahşap öğeyi kapsar."}],"source_phrase_ar":"عرضت العود على الإناء وضعته عليه عرضا (maqayis;ayn;sihah;tahdhib;mufradat)؛ المعراض سهم يمضي عرضا (maqayis;sihah;tahdhib)؛ عارضة الباب والعوارض سقائف المحمل (maqayis;sihah;tahdhib)","source_summary":"Ortak çekirdek enine yönelimdir; yerleştirme eylemi, kapı ve taşıma kirişleri ile yana giden özel ok bu yönelimin nesne ve araç kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه وضع العود على الإناء عرضا، وعوارض السقف أو المحمل، وعارضة الباب، والمعراض السهم الذي يمضي عرضا أو لا ريش له.","what_is_not_ar":"لا يدخل فيه الاعتراض المجازي في الكلام أو الناس إلا إذا دل على جسم موضوع بالعرض."},"support_links":[]},{"boundary":"Yön, dağ yolu, şiir ölçüsü ve belgelenen bölge adı korunur; genel yer adı sınıfı kurulmaz.","branch_kind":"bare","branch_ref":"root_001001/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","surface_ar":"عَرَضْ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","surface_ar":"عَرْضًا"}],"gloss":"yön, dağ yolu, bölge adı ve şiir ölçüsü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir yönü, yanı veya gidilen tarafı belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dağ içindeki yol ve belirli bölge adı, yer-yön kullanımının özelleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Şiirin ölçü düzeni, yön ve yan kavramından türemiş teknik bir kullanımdır."}}],"root_ar":"ع ر ض","root_id":"root_001001","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belgelenen yer-yön kullanımlarıyla teknik şiir ölçüsü kullanımını eksiksiz biçimde sıralar.","boundary_detail":"Yön, dağ yolu, şiir ölçüsü ve belgelenen bölge adı korunur; genel yer adı sınıfı kurulmaz.","branch_image_ar":"عروض ونواح وأسماء فنية أو موضعية","concept_gloss":"yön, dağ yolu, bölge adı ve şiir ölçüsü","contextual_glosses":[{"applicability":"Şiirin veznini ve ölçü düzenini inceleyen teknik alan söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yön, dağ yolu ve bölge adı kullanımlarını kapsamaz.","preserves":"Teknik şiir ölçüsü kullanımını açık biçimde korur."},"facet_ids":["F003"],"text":"şiir ölçüsü bilimi","usage_role":"contextual"}],"definition":"Bir yön veya yan, dağ içindeki bir yol ya da belirli bir bölgenin adı olabilir; teknik kullanımda şiirin veznini inceleyen ölçü düzenini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir yönü, yanı veya gidilen tarafı belirtir."},{"facet_id":"F002","role":"specialization","statement":"Dağ içindeki yol ve belirli bölge adı, yer-yön kullanımının özelleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Şiirin ölçü düzeni, yön ve yan kavramından türemiş teknik bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi yön veya yan, dağ yolu, şiir ölçüsü ve belirli bölge adı kullanımlarını destekler. Geçici çerçevedeki köy ve vadi genellemesi kaynak cümlesinde kurucu içerik değildir; dal yalnızca belgelenen teknik ve yer-yön kullanımlarıyla tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"şiir ölçüsü ve vezin bilimi"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"yön, dağ yolu veya belirli bölge"}],"lexicalization_note":"Tanım yalın ve belgelenmiş çoklu adlandırmaları verir; başka yer adları veya tamlamalar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yön kullanımını hareket bağlamındaki gelinen taraftan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yön anlamından teknik ve yer adlarına uzanan çoklu bir adlandırmadır; komşu dal yalnızca bir yerden geliş yönünü belirten bağlamsal bir taraf adıdır.","focus_only":"Odak dal yönün yanında dağ yolu, bölge adı ve teknik şiir ölçüsü kullanımlarını kapsar.","gloss":"yön ve gelinen taraf","neighbor_only":"Komşu dal özellikle insanların geldiği yön veya tarafı anlatan hareket bağlamına bağlıdır.","neighbor_ref":"root_000065/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir yönü, yanı veya tarafı adlandırma alanında buluşur."}],"source_phrase_ar":"العروض الناحية أو ناحية من العلم (maqayis)؛ العروض ميزان الشعر والعروض طريق في الجبل ومكة والمدينة وما حولهما (sihah)؛ العروض عروض الشعر وأخذ في عروض أي ناحية واستعمل على العروض (tahdhib)","source_summary":"Kaynakların birleşik içeriği yön veya yan anlamını, dağ yolu ve belirli bölge adıyla birlikte verir; şiir ölçüsü de bu adlandırmanın teknik uzantısıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العروض بمعنى الناحية أو الطريق في الجبل أو الموضع، وعروض الشعر وميزانه، والعروض اسما لمكة والمدينة وما حولهما، والأعراض للقرى أو الأودية.","what_is_not_ar":"لا يدخل فيه العرض العام خلاف الطول إلا أصل اشتقاق، ولا يعمم هذا على كل استعمال للناحية إذا كان له فرع أدق."},"support_links":[]},{"boundary":"Çekirdek fiziksel örtmedir; dinî inkâr, nimeti yadsıma ve günahı giderme bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B001","candidate_links":[{"candidate_id":"cand_2ab01e70a8a6014a953e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"örtmek, kapatmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin üstünü kapatarak onu görünmez veya örtülü duruma getirme işlemi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zırhı giysiyle kaplama, silahla örtünme ve külün üstünün toprakla kapanması çekirdeğin özel gerçekleşmeleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Güneşin yıldızları görünmez kılması da görsel örtme sonucu üzerinden bu çekirdeğe bağlanır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin üstünü başka bir şeyle kapatıp görünmesini engelleyen genel çekirdek için uygundur.","boundary_detail":"Çekirdek fiziksel örtmedir; dinî inkâr, nimeti yadsıma ve günahı giderme bu dala girmez.","branch_image_ar":"ستر وتغطية","concept_gloss":"örtmek, kapatmak","contextual_glosses":[{"applicability":"Zırhın giysiyle veya külün toprakla kaplanması gibi somut bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut bir nesnenin üstünün kapatılması işlemini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"üstünü örtmek","usage_role":"contextual"},{"applicability":"Güneş ışığının yıldızları görünmez kıldığı göksel bağlamda sonuç odaklı doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görsel örtmenin görünürlüğü ortadan kaldıran sonucunu korur."},"facet_ids":["F003"],"text":"görünmez kılmak","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeyle örterek görünmesini engellemek veya kapalı duruma getirmektir. Zırhın giysiyle, kişinin silahla ya da külün savrulan toprakla örtülmesi bu işlemin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin üstünü kapatarak onu görünmez veya örtülü duruma getirme işlemi."},{"facet_id":"F002","role":"specialization","statement":"Zırhı giysiyle kaplama, silahla örtünme ve külün üstünün toprakla kapanması çekirdeğin özel gerçekleşmeleridir."},{"facet_id":"F003","role":"extension","statement":"Güneşin yıldızları görünmez kılması da görsel örtme sonucu üzerinden bu çekirdeğe bağlanır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi örtme ve görünmez kılma çekirdeğini; zırhı giysiyle kaplama, silahla örtünme, külün toprakla kapanması ve yıldızların güneş ışığında görünmemesi gibi gerçekleşmelerle açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi örtmek ve kapatmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"zırhının üstüne bir giysi geçirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"silahlarıyla örtünmek veya silah kuşanmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"rüzgârın savurduğu toprakla örtülmüş kül"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güneşin yıldızları görünmez kılması"}],"lexicalization_note":"Tanım yalın örtme çekirdeğini korur; zırh, silah, kül ve gök cisimleriyle ilgili kullanımlar bu çekirdeğin yapıya bağlı gerçekleşmeleri olarak ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel örtme dalı en yakın karışma olasılığını taşıdığı için yayımlandı, öteki adaylar yalnızca örnek veya ortak senaryo düzeyinde kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek büyük ölçüde örtüşür; ancak komşu dal soyut gizlemeyi ve örtü nesnelerini de kapsarken bu dalın kanıtı belirli somut ve görsel gerçekleşmelere dayanır.","focus_only":"Bu dal zırh, silah, kül ve güneş ışığı gibi belirli gerçekleşmeleri de taşır.","gloss":"örtmek, kapatmak","neighbor_only":"Komşu dal haber veya tanıklığı gizleme ve örtü adı gibi daha geniş kullanımlara da uzanır.","neighbor_ref":"root_000438/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde bir şeyi örterek görünmesini engelleme vardır."}],"source_phrase_ar":"الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)","source_summary":"Kaynaklar örtme ve kapatma çekirdeğinde birleşir; farklı örnekler bu işlemin nesne, giysi, silah, kül ve gök görünümü üzerindeki gerçekleşmelerini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ستر الشيء وتغطيته وكفر الدرع بثوب وتغطية السلاح والرماد المكفور وستر الشمس النجوم والسحاب الشمس","what_is_not_ar":"ليس الكفر الديني ولا كفران النعمة ولا الكفارة ولا الزراعة"},"support_links":["sup_318377b2b29b948dc703"]},{"boundary":"Dal genel karanlık ya da genel su kütlesi değildir; kaynakta örtücü etkisiyle adlandırılan belirli varlıklarla sınırlıdır.","branch_kind":"bare","branch_ref":"root_001307/B002","candidate_links":[{"candidate_id":"cand_98a237407e25b4f6e835","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"örten karanlık veya enginlik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Karanlık, genişlik ya da kapatma etkisiyle başka şeylerin görünmesini veya seçilmesini engelleyen varlık."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece, deniz, büyük ırmak, gün batımı ve bulut kaynaklarda bu nitelemenin farklı gönderimleri olarak sıralanır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Farklı gönderimleri tek bir nesne türüne indirgemeden ortak örtücü etkiyi anlatmak için uygundur.","boundary_detail":"Dal genel karanlık ya da genel su kütlesi değildir; kaynakta örtücü etkisiyle adlandırılan belirli varlıklarla sınırlıdır.","branch_image_ar":"غمر ساتر","concept_gloss":"örten karanlık veya enginlik","contextual_glosses":[{"applicability":"Sözün karanlık geceyi nitelediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deniz, büyük ırmak, gün batımı ve bulut gönderimlerini dışarıda bırakır.","preserves":"Gecenin karanlığıyla kişileri ve görünümü örtmesi özelliğini korur."},"facet_ids":["F001","F002"],"text":"karanlığıyla örten gece","usage_role":"contextual"},{"applicability":"Sözün deniz veya büyük ırmak için kullanıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gece, gün batımı ve bulut gönderimlerini dışarıda bırakır.","preserves":"Deniz ve büyük ırmak gönderimlerinin genişlik ve kuşatıcılık yönünü korur."},"facet_ids":["F001","F002"],"text":"engin su kütlesi","usage_role":"contextual"}],"definition":"Karanlığı, genişliği veya kapatma etkisi nedeniyle kişileri ya da görünümü örten karanlık gece, deniz, büyük ırmak, gün batımı veya bulut için kullanılan bir nitelemedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Karanlık, genişlik ya da kapatma etkisiyle başka şeylerin görünmesini veya seçilmesini engelleyen varlık."},{"facet_id":"F002","role":"source_variant","statement":"Gece, deniz, büyük ırmak, gün batımı ve bulut kaynaklarda bu nitelemenin farklı gönderimleri olarak sıralanır."}],"identity_rationale":"Kaynak ifadesi karanlık geceyi, denizi, büyük ırmağı, gün batımını ve bulutu aynı adlandırma çevresinde toplar; bunların tümünü tek bir gerçek 'kuşatan örtü' türü saymak yerine, karanlık, genişlik veya kapatma etkisiyle örten farklı varlıklar olarak anlamak gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"karanlık gece, deniz, büyük ırmak, gün batımı veya bulut"}],"lexicalization_note":"Yalın dal, kaynakta doğrudan adlandırılan gece, deniz, büyük ırmak, gün batımı ve bulut kapsamıyla tanımlanır; yapıya özgü başka anlam eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; suyla örtme ve gece karanlığı adayları dalın iki temel gönderim alanını sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli varlıklara verilen bir nitelemeyi anlatır; komşu dal ise çok suyun örtmesi ve suya gömülme süreçlerini merkez alır.","focus_only":"Bu dal karanlık geceyi, gün batımını ve bulutu da aynı örtücü nitelemeye dahil eder.","gloss":"örten enginlik","neighbor_only":"Komşu dal suyun yükselmesi, dalma ve suyla kaplanma olaylarını da kapsar.","neighbor_ref":"root_001105/B001","relation_type":"near_neighbor","shared_zone":"Deniz ve büyük ırmak, genişlikleri ve örtücü etkileri bakımından iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Ortak gece örneğine rağmen bu dal çok gönderimli bir adlandırmadır; komşu dalın çekirdeği doğrudan gece karanlığıdır.","focus_only":"Bu dal gece dışında deniz, büyük ırmak, gün batımı ve bulutu da kapsar.","gloss":"karanlık gece","neighbor_only":"Komşu dal yalnızca gece karanlığının gölge veya karanlık örtü oluşunu işler.","neighbor_ref":"root_000966/B002","relation_type":"near_neighbor","shared_zone":"Karanlık gecenin görüşü örtmesi iki dalda da bulunur."}],"source_phrase_ar":"الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)","source_summary":"Kaynaklar aynı sözü karanlık gece, deniz ve büyük ırmak için verir; bazı aktarımlar gün batımını ve bulutu da örtücü etkileri nedeniyle bu listeye ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكافر للليل المظلم والبحر والنهر العظيم ومغيب الشمس وما يستر بظلمته أو سعته","what_is_not_ar":"ليس الأرض البعيدة ولا القرية ولا الجبل ولا الكفر الديني"},"support_links":["sup_399d68221f85ed7c82ae"]},{"boundary":"Dal dinî gerçeği ve inancı reddetmeyle sınırlıdır; nimeti yadsıma veya yalnızca genel bir gerçeği inkâr etme bunun tamamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B003","candidate_links":[{"candidate_id":"cand_ff5bb4621c1a7c8a9247","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"dinî gerçeği reddetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnancın karşıtı olarak dinî gerçeği, birliği, dinî hükmü veya peygamberliği reddetme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalben bilip sözle kabul etmeme, bilip boyun eğmeme, dıştan inanmış görünme ve hem kalple hem dille inkâr etme farklı türlerdir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnancın karşıtı olan çekirdeği ve reddedilen dinî içeriği birlikte ifade eder.","boundary_detail":"Dal dinî gerçeği ve inancı reddetmeyle sınırlıdır; nimeti yadsıma veya yalnızca genel bir gerçeği inkâr etme bunun tamamı değildir.","branch_image_ar":"حجب الحق","concept_gloss":"dinî gerçeği reddetme","contextual_glosses":[{"applicability":"Dalın genel dinî karşıtlık bağlamında eylem olarak çevrilmesi gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnancı kabul etmeme ve ona karşı durma çekirdeğini korur."},"facet_ids":["F001"],"text":"inancı reddetmek","usage_role":"general"},{"applicability":"Bile bile yadsıma veya direnme türünün açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İkiyüzlülük ve bütünüyle bilgisiz inkâr gibi öteki türleri dışarıda bırakır.","preserves":"Bilgi ile dışa vurulan ret arasındaki ayrımı korur."},"facet_ids":["F002"],"text":"kalben bilip kabul etmemek","usage_role":"explanatory"}],"definition":"İnancı, birliği, dinî hükmü veya peygamberliği reddederek dinî gerçeği örtmek ya da kabul etmemektir. Kaynaklar bunu inkâr, bile bile direnme, ikiyüzlülük, ortak koşma ve yalanlama gibi türlere ayırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnancın karşıtı olarak dinî gerçeği, birliği, dinî hükmü veya peygamberliği reddetme."},{"facet_id":"F002","role":"specialization","statement":"Kalben bilip sözle kabul etmeme, bilip boyun eğmeme, dıştan inanmış görünme ve hem kalple hem dille inkâr etme farklı türlerdir."}],"identity_rationale":"Kaynak ifadesi bu dalı inancın karşıtı ve gerçeğin örtülmesi olarak tanımlar; birliği, dinî hükmü veya peygamberliği yadsıma ile inkâr, bile bile direnme, ikiyüzlülük ve ortak koşma türlerini açıkça içerir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dinî gerçeği veya inancı reddetme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kalben bildiği gerçeği diliyle kabul etmeme"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gerçeği bildiği hâlde inatla kabul etmemek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kalben reddederken diliyle inanmış görünmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gerçeği hem kalple hem dille inkâr etmek"}],"lexicalization_note":"Yalın dinî reddetme çekirdeği korunur; kalben bilip söylememe, bilip kabul etmeme, dıştan inanmış görünme ve hem kalple hem dille reddetme yapıya bağlı türlerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yadsıma en yakın anlam komşusu, inanma ise açık karşıt kutup olduğu için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın dinî kapsamı ve birden çok tutum türü vardır; komşu dal ise konusu ne olursa olsun bilgiye rağmen yadsımayı merkez alır.","focus_only":"Bu dal özellikle dinî inancı ve gerçeği reddeder; ikiyüzlülük ve ortak koşma gibi türleri de kapsar.","gloss":"bile bile reddetme","neighbor_only":"Komşu dal, doğruluğu bilinen herhangi bir şeyi inkâr etmeyi din alanıyla sınırlamadan anlatır.","neighbor_ref":"root_000224/B001","relation_type":"near_synonym","shared_zone":"Bilinen bir gerçeği kabul etmeme iki dalın ortak alanıdır."},{"boundary_match":"opposed","distinction":"Biri gerçeği reddetme, diğeri onu doğrulayıp benimseme yönündedir.","focus_only":"Bu dal dinî gerçeği kabul etmemeyi ve reddetmeyi bildirir.","gloss":"reddetme / inanma","neighbor_only":"Komşu dal haberi veya dinî gerçeği doğrulayıp kalben benimsemeyi bildirir.","neighbor_ref":"root_000054/B002","relation_type":"polarity_pair","shared_zone":"İki dal aynı kabul-ret ekseninde dinî veya doğrulanabilir içerikle ilişki kurar."}],"source_phrase_ar":"الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)","source_summary":"Kaynaklar dalı inancın karşıtı sayar ve gerçeği örtme düşüncesiyle açıklar; toplu aktarım çeşitli inkâr, direnme ve ikiyüzlülük biçimlerini de sıralar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الكفر نقيض الإيمان وجحود الوحدانية أو الشريعة أو النبوة والإنكار والجحود والمعاندة والنفاق والشرك والتكذيب","what_is_not_ar":"ليس كفران النعمة وحده ولا البراءة ولا التكفير عن السيئات"},"support_links":["sup_f82496056045a990aee9"]},{"boundary":"Nesne özellikle nimettir ve belirleyici sonuç şükrün terkidir; genel dinî ret bu dala kendiliğinden girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"nimeti yadsıma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nimeti yadsıma veya şükrünü yerine getirmeyerek değerini örtme."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Nimetleri sürekli ve aşırı biçimde yadsıyan kişi bu tutumun yoğunlaşmış taşıyıcısıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nimeti tanımama ile ona şükretmeme çekirdeğini kısa ve doğal biçimde verir.","boundary_detail":"Nesne özellikle nimettir ve belirleyici sonuç şükrün terkidir; genel dinî ret bu dala kendiliğinden girmez.","branch_image_ar":"ستر النعمة","concept_gloss":"nimeti yadsıma","contextual_glosses":[{"applicability":"Bir nimetin veya yapılan iyiliğin tanınmadığı gündelik bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapılan iyiliği tanımama ve karşılığında şükretmeme tutumunu korur."},"facet_ids":["F001"],"text":"iyiliğin kıymetini bilmemek","usage_role":"contextual"}],"definition":"Bir nimeti tanımamak, değerini örtmek veya onun gerektirdiği şükrü yerine getirmemektir. Bu tutumda aşırı olan kişi de aynı anlam alanında nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nimeti yadsıma veya şükrünü yerine getirmeyerek değerini örtme."},{"facet_id":"F002","role":"specialization","statement":"Nimetleri sürekli ve aşırı biçimde yadsıyan kişi bu tutumun yoğunlaşmış taşıyıcısıdır."}],"identity_rationale":"Kaynak ifadesi nimeti yadsımayı, onu örtmeyi ve gereği olan şükrü yerine getirmemeyi aynı çekirdekte birleştirir; dalın geçici çerçevesi bu koşulu doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"nimeti yadsımak ve şükrünü yerine getirmemek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"nimeti yadsıma ve şükretmeme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"nimetleri aşırı biçimde yadsıyan kimse"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam"}],"lexicalization_note":"Nimeti yadsıma çekirdeği yalın ve türemiş kullanımlarda korunur; nimetle kurulan yapı ve aşırılık bildiren kişi nitelemesi ayrı gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; daha geniş nankörlük dalı yakın eş, şükür dalı ise doğrudan karşıt kutup olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal nankörlüğü daha geniş bir davranış kümesine yayar; bu dal doğrudan nimet ile şükür arasındaki ilişkiyle sınırlıdır.","focus_only":"Bu dal nimetin yadsınmasını ve şükrünün terkini doğrudan çekirdek yapar.","gloss":"nimeti yadsıma","neighbor_only":"Komşu dal nimet yanında dostluğu kesme, felaketleri sayıp nimetleri unutma ve yardımı esirgeme gibi tutumları da kapsar.","neighbor_ref":"root_001321/B002","relation_type":"near_synonym","shared_zone":"Nimeti tanımama ve ona şükretmeme iki dalda da merkezîdir."},{"boundary_match":"opposed","distinction":"Biri nimetin değerini örter ve şükrü bırakır; diğeri nimeti tanır ve şükrü gösterir.","focus_only":"Bu dal nimeti tanımamayı ve şükrünü terk etmeyi bildirir.","gloss":"nankörlük / şükür","neighbor_only":"Komşu dal nimeti tanımayı, övmeyi ve şükrü sözle ya da davranışla göstermeyi bildirir.","neighbor_ref":"root_000810/B001","relation_type":"polarity_pair","shared_zone":"İki dal nimetin tanınması ve karşılığının verilmesi eksenindedir."}],"source_phrase_ar":"كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)","source_summary":"Kaynaklar nimeti yadsımayı şükrün karşıtı sayar; örtme açıklaması, nimetin gerektirdiği şükrü yerine getirmemeyi bu karşıtlığın belirleyici davranışı yapar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه كفر النعمة وكفرانها وجحودها وترك شكرها والكفور في كفران النعمة","what_is_not_ar":"ليس الكفر الديني عند الإطلاق ولا الكفارة ولا البراءة"},"support_links":[]},{"boundary":"Bu dal bir inancı yadsımak değil, belirli bir şeyle bağı reddedip ondan uzaklaşmaktır.","branch_kind":"non_bare","branch_ref":"root_001307/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"bağını reddedip uzaklaşmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir şeyle bağı reddederek ondan uzaklaşma ve kendini onun dışında tutma."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, görüş, eylem veya sorumlulukla ilişkiyi açıkça reddeden bağlı kullanım için uygundur.","boundary_detail":"Bu dal bir inancı yadsımak değil, belirli bir şeyle bağı reddedip ondan uzaklaşmaktır.","branch_image_ar":"تبرؤ وتنصل","concept_gloss":"bağını reddedip uzaklaşmak","contextual_glosses":[{"applicability":"Aidiyet veya sorumluluk bağının reddedildiği bağlamlarda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aidiyet bağını reddetme ve kendini dışarıda konumlandırma sonucunu korur."},"facet_ids":["F001"],"text":"ondan olmadığını açıklamak","usage_role":"explanatory"}],"definition":"Bir şeyle olan bağı reddetmek, ondan uzak olduğunu açıklamak ve sorumluluk ya da aidiyet bağından sıyrılmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir şeyle bağı reddederek ondan uzaklaşma ve kendini onun dışında tutma."}],"identity_rationale":"Kaynak ifadesi sözün bir şeyden uzak olduğunu bildirme, onunla bağını reddetme ve ondan sıyrılma anlamında kullanılabildiğini açıkça söyler.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir şeyle bağını reddedip ondan uzaklaşmak"}],"lexicalization_note":"Anlam yalnızca bir şeyden uzaklaşmayı bildiren bağlı yapıda korunur; yalın köke genel bir ayrılma anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bağ kesme ve uzak durma dalı en yakın anlam sınırını verdiği için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yapısal olarak bağlı ve dar bir ilişki reddidir; komşu dal genel uzaklık, arınmışlık ve sorumsuzluk bildirimlerini de içerir.","focus_only":"Bu dal belirli bir bağlı söz yapısında ilişkiyi reddetmeyi anlatır.","gloss":"bağını reddedip uzaklaşmak","neighbor_only":"Komşu dal kişi, iş, kusur ve kötülükten arınma, uzak durma, uyarma ve mazeret bildirme gibi daha geniş bir alanı kapsar.","neighbor_ref":"root_000100/B002","relation_type":"near_synonym","shared_zone":"Bir kişi veya şeyle ilişkiyi reddetme ve ondan uzak durma iki dalda ortaktır."}],"source_phrase_ar":"يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)","source_summary":"Kaynaklar bağlı kullanımın bir şeyden uzak olduğunu ilan etme ve onunla ilişkiden sıyrılma anlamı taşıdığında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه الكفر بمعنى البراءة والتنصل من الشيء أو بعضهم من بعض","what_is_not_ar":"ليس جحود الإيمان ولا كفران النعمة ولا تغطية الشيء حسيا"},"support_links":[]},{"boundary":"Eylem kişinin kendi reddi değil, başka bir kişinin durumu hakkında adlandırma veya hüküm vermedir.","branch_kind":"bare","branch_ref":"root_001307/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"inançsız saymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka bir kişiyi inançsız diye niteleme veya bu yönde hüküm verme."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir başkasını dinî inancı reddeden kişi diye adlandırma veya böyle hükmetme bağlamında uygundur.","boundary_detail":"Eylem kişinin kendi reddi değil, başka bir kişinin durumu hakkında adlandırma veya hüküm vermedir.","branch_image_ar":"نسبة إلى الكفر","concept_gloss":"inançsız saymak","contextual_glosses":[{"applicability":"Resmî veya öğretisel bir hükmün vurgulandığı bağlamlarda daha açık karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin dinî durumu hakkında hüküm verme yönünü açıkça korur."},"facet_ids":["F001"],"text":"inancı reddettiğine hükmetmek","usage_role":"explanatory"}],"definition":"Bir kişiyi inançsız diye adlandırmak veya onun dinî gerçeği reddettiğine hükmetmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka bir kişiyi inançsız diye niteleme veya bu yönde hüküm verme."}],"identity_rationale":"Kaynak ifadesi bir kişiyi inançsız diye adlandırma ve onun inancı reddettiğine hükmetme işlemlerini doğrudan verir; geçici çerçeve bu katılımcı ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birini inançsız saymak veya öyle adlandırmak"}],"lexicalization_note":"Yalın biçimin ettirgen-hüküm verici anlamı korunur; suçlama veya zorlama gibi başka yapısal anlamlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hırsızlık isnadı yalnızca katılımcı yapısını açıklayan yararlı bir yakın komşu olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İsnat yapısı ortaktır; ancak yüklenen içerik ve hükmün dinî niteliği bütünüyle farklıdır, bu yüzden olağan ikame mümkün değildir.","focus_only":"Bu dal bir kişinin dinî inancı reddettiğine ilişkin niteleme veya hüküm verir.","gloss":"birine nitelik yüklemek","neighbor_only":"Komşu dal bir kişiye hırsızlık eylemini yükler.","neighbor_ref":"root_000700/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda konuşan, başka bir kişiye olumsuz bir nitelik veya eylem isnat eder."}],"source_phrase_ar":"أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)","source_summary":"Kaynaklar eylemi bir kişiye inançsız nitelemesi yöneltmek veya onun hakkında bu hükmü vermek olarak açıklar.","sources":["SI","MU"],"what_is_ar":"يدخل فيه أكفر الرجل بمعنى دعاه كافرا أو حكم بكفره أو نسبه إلى الكفر","what_is_not_ar":"ليس الإلجاء إلى العصيان ولا الكفر نفسه ولا التكفير عن السيئات"},"support_links":[]},{"boundary":"Genel zorlama değildir; itaat eden kişinin zorlanarak itaatsizliğe geçirilmesi şarttır.","branch_kind":"bare","branch_ref":"root_001307/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"itaatsizliğe zorlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İtaat eden bir kişiyi zorlayarak itaatsizliğe geçirmek."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başlangıçta itaat eden bir kişinin baskıyla itaatsiz davranmaya sürüklendiği bağlam için tam karşılıktır.","boundary_detail":"Genel zorlama değildir; itaat eden kişinin zorlanarak itaatsizliğe geçirilmesi şarttır.","branch_image_ar":"إلجاء إلى العصيان","concept_gloss":"itaatsizliğe zorlamak","contextual_glosses":[{"applicability":"İtaatsizliğin açık bir başkaldırı olarak gerçekleştiği anlatı bağlamlarında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkaldırı düzeyine varmayan itaatsiz davranışları dışarıda bırakır.","preserves":"Dış baskıyla itaatten karşı koymaya geçişi korur."},"facet_ids":["F001"],"text":"başkaldırmaya mecbur bırakmak","usage_role":"contextual"}],"definition":"Başlangıçta itaat eden bir kişiyi baskı veya zorlamayla itaatsiz davranmaya mecbur bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İtaat eden bir kişiyi zorlayarak itaatsizliğe geçirmek."}],"identity_rationale":"Kaynak ifadesi başlangıçta itaat eden bir kişiyi baskıyla itaatsizliğe sürükleme sürecini açıkça belirtir; geçici çerçeve başlangıç durumu, zorlama ve sonuç ayrımını korur.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"itaat eden birini itaatsizliğe zorlamak"}],"lexicalization_note":"Yalın biçim, itaat eden kişiyi itaatsizliğe zorlama anlamıyla sınırlanır; yalnızca hüküm verme anlamına veya genel baskıya genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel zorlama sınırı ve zorlamasız saptırma ayrımı dalın koşullarını en iyi açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın başlangıç ve sonuç koşulları belirgindir; komşu dalın zorlama çekirdeğinde itaatten itaatsizliğe geçiş şartı yoktur.","focus_only":"Bu dal hedefin önceden itaat etmesini ve zorlamanın onu itaatsizliğe götürmesini şart koşar.","gloss":"itaatsizliğe zorlamak","neighbor_only":"Komşu dal herhangi bir kişiyi herhangi bir şeye zorlamayı genel olarak kapsar.","neighbor_ref":"root_001343/B002","relation_type":"near_synonym","shared_zone":"Bir kişiyi istemediği bir davranışa baskıyla mecbur bırakma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Burada belirleyici araç zorlamadır; komşu dalda ise yöneltme ve ayartma bulunabilir, mecbur bırakma zorunlu değildir.","focus_only":"Bu dal sonucu doğrudan baskı ve mecbur bırakma yoluyla oluşturur.","gloss":"itaatten saptırmak","neighbor_only":"Komşu dal ayartma, aldatma veya isteği süsleme yoluyla doğru yoldan saptırmayı da kapsar.","neighbor_ref":"root_001128/B003","relation_type":"near_neighbor","shared_zone":"Bir kişiyi önceki doğru veya itaatkâr durumundan uzaklaştırma iki dalda ortaktır."}],"source_phrase_ar":"إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)","source_summary":"Kaynaklar aynı katılımcı değişimini verir: itaat eden kişi dış baskıyla itaatsiz davranmaya mecbur bırakılır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه أكفرته إذا ألجأت المطيع إلى أن يعصي","what_is_not_ar":"ليس الحكم بكفر شخص ولا دعوته كافرا ولا الكفر الديني نفسه"},"support_links":[]},{"boundary":"Dal ekimin bütünü değil, tohumu toprağa koyup üstünü örtme işlemi üzerinden çiftçiyi adlandırır.","branch_kind":"bare","branch_ref":"root_001307/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"tohumu örten çiftçi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tohumu toprağa yerleştirip üzerini toprakla örten kişi."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişiyi yalnızca meslek adıyla değil, tohumu toprakla örtme gerekçesiyle birlikte anlatır.","boundary_detail":"Dal ekimin bütünü değil, tohumu toprağa koyup üstünü örtme işlemi üzerinden çiftçiyi adlandırır.","branch_image_ar":"تغطية البذر","concept_gloss":"tohumu örten çiftçi","contextual_glosses":[{"applicability":"Eylemin gerekçesi bağlamdan açıkça anlaşıldığında doğal kişi adı olarak kullanılabilir.","error_profile":{"adds":"Tohumu örtme işiyle sınırlandırılmayan bütün çiftçilik faaliyetlerini kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Toprağı işleyip ekim yapan kişi rolünü korur."},"facet_ids":["F001"],"text":"çiftçi","usage_role":"contextual"}],"definition":"Tohumu veya taneyi toprağa yerleştirip üstünü toprakla örten çiftçidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tohumu toprağa yerleştirip üzerini toprakla örten kişi."}],"identity_rationale":"Kaynak ifadesi çiftçinin tohumu veya taneyi toprakla örtme işlemini adlandırmanın gerekçesi yapar; tekil ve çoğul kişi adları aynı eyleyen rolünü taşır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tohumu toprakla örten çiftçi"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tohumları toprakla örten çiftçiler"}],"lexicalization_note":"Yalın kişi adları, tohumu toprakla örten çiftçi anlamında tutulur; dinî kişi nitelemesine veya genel ekim sürecine genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ekim süreci ile genel çiftçi adı, eylem ve eyleyen sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal eyleyen kişiyi örtme gerekçesiyle niteler; komşu dal ise ekim işlemi, ürün ve tarla dâhil daha geniş bir tarım sürecidir.","focus_only":"Bu dal tohumu toprakla örten kişiyi adlandırır.","gloss":"tohumu örten çiftçi","neighbor_only":"Komşu dal tohumu atma, toprağı ekime hazırlama, ekin ve ekili tarla gibi bütün ekim alanını kapsar.","neighbor_ref":"root_000303/B002","relation_type":"near_neighbor","shared_zone":"Tohumun toprağa verilmesi ve çiftçinin bu süreçteki rolü iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Gönderim örtüşse de adlandırma sınırı farklıdır: biri tohumu örtme, diğeri toprağı işleme ve meslek yönünü öne çıkarır.","focus_only":"Bu dal çiftçiyi özellikle tohumu toprakla örtmesi bakımından adlandırır.","gloss":"çiftçi","neighbor_only":"Komşu dal çiftçiyi toprağı yarıp işleyen kişi ve çiftçilik mesleğinin taşıyıcısı olarak adlandırır.","neighbor_ref":"root_001175/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın gönderimi ekim yapan çiftçidir."}],"source_phrase_ar":"يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)","source_summary":"Kaynaklar çiftçinin adlandırılmasını tohumu veya taneyi toprakla örtmesine bağlar; tekil ve çoğul biçimler aynı eyleyen rolünü gösterir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه الكافر للزارع والكفار للزراع لأنهم يغطون الحب أو البذر بالتراب","what_is_not_ar":"ليس الكافر المضاد للإيمان ولا الكافر للبحر أو الليل"},"support_links":[]},{"boundary":"Çekirdek yalnızca bağışlama değildir; günah veya bozulmuş yemin karşısında yükü gideren bir işlem ya da karşılık bulunur.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"günah yükünü giderme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günahın yükünü örten veya silen karşılık ya da işlem."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bozulan yemin için gereken yükümlülüğü yerine getirme, çekirdeğin yapıya bağlı özel türüdür."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İşlemin sonucu, kötülüğün işlenmemiş gibi değerlendirilmesi veya etkisinin silinmesidir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem giderici işlemi hem de günahın etkisinin silinmesi sonucunu kapsayan genel karşılıktır.","boundary_detail":"Çekirdek yalnızca bağışlama değildir; günah veya bozulmuş yemin karşısında yükü gideren bir işlem ya da karşılık bulunur.","branch_image_ar":"محو الإثم بتغطيته","concept_gloss":"günah yükünü giderme","contextual_glosses":[{"applicability":"Yemin bozulduğunda doğan özel yükümlülüğün yerine getirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yemin dışındaki günah ve kötülüklerin giderilmesini dışarıda bırakır.","preserves":"Bozulan yemin nedeniyle gereken karşılığın yerine getirilmesini korur."},"facet_ids":["F002"],"text":"bozulan yeminin gereğini yerine getirmek","usage_role":"contextual"},{"applicability":"İşlemin günahı işlenmemiş gibi kılan sonucunun öne çıktığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günahın etkisini ve yükünü ortadan kaldırma sonucunu korur."},"facet_ids":["F001","F003"],"text":"günahı silmek","usage_role":"contextual"}],"definition":"Bir günahın ya da bozulan yeminin doğurduğu yükü, gereken karşılığı veya işlemi yerine getirerek örtmek, silmek ve işlenmemiş sayılacak duruma getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günahın yükünü örten veya silen karşılık ya da işlem."},{"facet_id":"F002","role":"specialization","statement":"Bozulan yemin için gereken yükümlülüğü yerine getirme, çekirdeğin yapıya bağlı özel türüdür."},{"facet_id":"F003","role":"extension","statement":"İşlemin sonucu, kötülüğün işlenmemiş gibi değerlendirilmesi veya etkisinin silinmesidir."}],"identity_rationale":"Kaynak ifadesi günahı veya bozulan yeminin doğurduğu yükü belirli bir karşılıkla örtme, silme ve işlenmemiş gibi kılma sürecini açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"günahı veya bozulan yeminin yükünü gideren karşılık"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bozulan yeminin gerektirdiği yükümlülüğü yerine getirme"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"günahları örtüp etkisini silme"}],"lexicalization_note":"Günah yükünü giderme çekirdeği korunur; bozulmuş yemin için gerekeni yapma yalnızca ilgili söz öbeğine bağlı özel gerçekleşmedir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bağışlama ile günahtan dönme, giderici işlem ile sonuç arasındaki sınırı en iyi açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda giderici karşılık veya yükümlülük belirleyicidir; komşu dalda belirleyici olan cezadan vazgeçme ve bağışlamadır.","focus_only":"Bu dal günah veya yemin yükünü belirli bir karşılık ya da işlemle giderir.","gloss":"günah yükünü giderme","neighbor_only":"Komşu dal hak edilmiş cezayı uygulamamayı ve suçu bağışlayarak silmeyi merkez alır.","neighbor_ref":"root_001032/B001","relation_type":"near_synonym","shared_zone":"Günahın sonucunu ortadan kaldırma ve onu silinmiş sayma iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Burada odak yükün silinmesidir; komşu dalda odak kişinin geri dönüşü ve davranışı bırakmasıdır.","focus_only":"Bu dal geçmiş eylemin yükünü gideren karşılığı veya işlemi bildirir.","gloss":"günahı giderme","neighbor_only":"Komşu dal kişinin günahtan dönmesini ve davranış yönünü değiştirmesini bildirir.","neighbor_ref":"root_000544/B003","relation_type":"near_neighbor","shared_zone":"İki dal da işlenmiş bir günahla ilişkiyi değiştiren dinî-ahlaki bir süreçtir."}],"source_phrase_ar":"الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)","source_summary":"Kaynaklar günahın veya yeminin yükünü gideren karşılıkta birleşir; toplu anlatım hem gereken eylemi hem de günahın silinmiş sayılması sonucunu korur.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الكفارة لما يكفر الخطيئة أو اليمين والتكفير للسيئات والمعاصي حتى تصير كأن لم تعمل","what_is_not_ar":"ليس الكفر ضد الإيمان ولا كفران النعمة ولا ستر الأشياء الحسية"},"support_links":[]},{"boundary":"Dal güzel kokulu maddeyi değil, üzüm veya hurma çiçeği ile meyveyi gelişme aşamasında örten bitkisel kılıfları kapsar.","branch_kind":"bare","branch_ref":"root_001307/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"çiçek veya meyve kılıfı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gelişen çiçek veya meyveyi dıştan örten bitkisel kılıf ya da kap."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üzüm salkımının çiçek öncesi kılıfı, hurma çiçeğinin kabı ve meyveyi örten yaprak farklı gönderimlerdir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Üzüm ve hurma dâhil gelişen bitki bölümünü örten kap veya yaprağı genel olarak karşılar.","boundary_detail":"Dal güzel kokulu maddeyi değil, üzüm veya hurma çiçeği ile meyveyi gelişme aşamasında örten bitkisel kılıfları kapsar.","branch_image_ar":"كمام الثمر","concept_gloss":"çiçek veya meyve kılıfı","contextual_glosses":[{"applicability":"Söz hurma ağacından çıkan çiçek kabını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üzüm salkımı ve başka meyve örtülerini dışarıda bırakır.","preserves":"Hurma çiçeğini örten kap biçimli bitki yapısını korur."},"facet_ids":["F001","F002"],"text":"hurma çiçeğinin kılıfı","usage_role":"contextual"}],"definition":"Üzüm salkımını çiçeklenmeden önce, hurma çiçeğini ya da gelişen meyveyi örten bitkisel kılıf, kap veya yapraktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gelişen çiçek veya meyveyi dıştan örten bitkisel kılıf ya da kap."},{"facet_id":"F002","role":"source_variant","statement":"Üzüm salkımının çiçek öncesi kılıfı, hurma çiçeğinin kabı ve meyveyi örten yaprak farklı gönderimlerdir."}],"identity_rationale":"Kaynak ifadesi üzüm salkımının çiçeklenmeden önceki kılıfını, hurma çiçeğinin kabını ve meyveyi örten yaprağı aynı örtücü bitki yapıları kümesinde toplar; bunlar yalnızca olgun meyvenin tek tip kabuğu değildir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"üzüm salkımının veya hurma çiçeğinin kılıfı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hurma çiçeğinin ya da meyvenin kılıfı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"hurma ağacından çıkan kapalı çiçek kılıfları"}],"lexicalization_note":"Yalın ad biçimleri bitkisel kılıf ve kap anlamında tutulur; güzel kokulu madde, su kaynağı veya bitki anlamları bu dala alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tahıl tanesi örtüsü ve ekinin kılıfa girme durumu, nesne ve gelişim aşaması sınırlarını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtülen bölüm ve yapı ölçeği farklıdır: bu dal salkım, çiçek veya meyve kabıdır; komşu dal tanenin başak içindeki ince örtüsüdür.","focus_only":"Bu dal üzüm salkımı, hurma çiçeği veya meyvenin dış kılıfını kapsar.","gloss":"bitkisel kılıf","neighbor_only":"Komşu dal yalnızca başaktaki tek bir tahıl tanesinin ince örtüsünü kapsar.","neighbor_ref":"root_000384/B008","relation_type":"near_neighbor","shared_zone":"Bir bitki üreme yapısını dıştan örten doğal kılıf iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Bu dal nesne adıdır; komşu dal ürünün kılıf içine girme aşamasını ve durumunu merkez alır.","focus_only":"Bu dal örtücü kılıfın kendisini adlandırır.","gloss":"ürün kılıfı","neighbor_only":"Komşu dal ekinin kendi kılıfına girip korunmuş duruma gelmesini anlatır.","neighbor_ref":"root_001019/B010","relation_type":"near_neighbor","shared_zone":"Gelişen bitki ürününün doğal bir kılıf içinde korunması iki dalda ortaktır."}],"source_phrase_ar":"الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)","source_summary":"Kaynaklar çiçek veya meyveyi örten bitkisel kapta birleşir; üzüm salkımı, hurma çiçeği ve meyve yaprağı bu üst kavramın farklı gönderimleridir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الكافور والكفرى والكوافير لأكمام العنب أو طلع النخل أو الورقة التي تستر الثمرة","what_is_not_ar":"ليس الكافور الطيب ولا عين الماء ولا النبات ولا الكفر الديني"},"support_links":[]},{"boundary":"Üç gönderim birbirinin örneği değildir; dal yalnızca kaynakta aynı ad altında toplanan bu ayrı sözlük anlamlarını korur.","branch_kind":"bare","branch_ref":"root_001307/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"koku maddesi, su kaynağı veya bitki","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güzel kokulu karışımlarda kullanılan bir madde."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Cennette bulunduğu belirtilen bir su kaynağı."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çiçeği papatya çiçeğine benzeyen bir bitki."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birbirinden ayrı üç sözlük gönderimini yapay bir ortak nesne türüne indirgemeden birlikte gösterir.","boundary_detail":"Üç gönderim birbirinin örneği değildir; dal yalnızca kaynakta aynı ad altında toplanan bu ayrı sözlük anlamlarını korur.","branch_image_ar":"كافور طيب","concept_gloss":"koku maddesi, su kaynağı veya bitki","contextual_glosses":[{"applicability":"Sözün güzel koku hazırlamada kullanılan maddeyi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Su kaynağı ve çiçekli bitki gönderimlerini dışarıda bırakır.","preserves":"Güzel kokulu karışımlarda kullanılan madde gönderimini korur."},"facet_ids":["F001"],"text":"güzel kokulu karışım maddesi","usage_role":"contextual"}],"definition":"Aynı sözle adlandırılan üç ayrı gönderimden oluşan bir sözlük kümesidir: güzel kokulu bir karışım maddesi, cennette bulunduğu belirtilen bir su kaynağı ve çiçeği papatyaya benzeyen bir bitki.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güzel kokulu karışımlarda kullanılan bir madde."},{"facet_id":"F002","role":"source_variant","statement":"Cennette bulunduğu belirtilen bir su kaynağı."},{"facet_id":"F003","role":"source_variant","statement":"Çiçeği papatya çiçeğine benzeyen bir bitki."}],"identity_rationale":"Kaynak ifadesi tek bir kavramsal tür vermek yerine aynı sözle anılan üç ayrı gönderimi sıralar: güzel kokulu bir madde, cennetteki bir su kaynağı ve çiçeği papatyaya benzeyen bir bitki. Tanım bu nedenle birleşik bir nesne sınıfı kurmadan sözlüksel çokanlamlılık kümesi olarak düzenlenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güzel kokulu karışımlarda kullanılan madde"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"cennetteki bir su kaynağı"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"çiçeği papatyaya benzeyen bir bitki"}],"lexicalization_note":"Yalın biçimin üç ayrı gönderimi birbirine karıştırılmadan verilir; meyve ve çiçek kılıfı anlamı bu dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca güzel kokulu bitki ve madde adayı bir facet için yararlı alan karşılaştırması sağladı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan yalnızca koku maddesi yönüdür; gönderimler ve bu dalın öteki iki sözlük anlamı farklı olduğu için ikame edilemezler.","focus_only":"Bu dalın güzel kokulu madde yanında su kaynağı ve ayrı bir bitki gönderimi de vardır.","gloss":"güzel kokulu madde","neighbor_only":"Komşu dal güzel kokulu kökü olan belirli bitkileri ve onlardan elde edilen kokuyu adlandırır.","neighbor_ref":"root_000707/B006","relation_type":"same_field","shared_zone":"İki dal güzel koku veren bitkisel madde alanında buluşur."}],"source_phrase_ar":"الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)","source_summary":"Toplu kaynak kanıtı güzel kokulu madde anlamını ortaklaştırır; aynı aggregate aktarım ayrıca su kaynağı ve papatyaya benzer çiçekli bitki anlamlarını ayrı gönderimler olarak kaydeder.","sources":["AY","SI","MU"],"what_is_ar":"يدخل فيه الكافور من الطيب وعين ماء في الجنة والنبات المسمى كافورا","what_is_not_ar":"ليس أكمام الثمر ولا الطلع ولا الكفر الديني"},"support_links":[]},{"boundary":"Uzak arazi çekirdeği ile köy, halk ve mezar kullanımları ayrı facetlerdir; dağ geçidi bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001307/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"uzak arazi; köy, uzak yer halkı veya mezar","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlardan uzak, pek uğranmayan veya geçilmeyen arazi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Köy, köyler ve uzak yerlerin halkı aynı söz ailesinin ayrı yer ve topluluk kullanımlarıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Mezar anlamı tek kaynaklı aktarım içinde verilen ayrı bir sözlük kullanımıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana uzak arazi anlamını öne alır ve kaynakta aynı dalda tutulan ayrı yer kullanımlarını açıkça işaretler.","boundary_detail":"Uzak arazi çekirdeği ile köy, halk ve mezar kullanımları ayrı facetlerdir; dağ geçidi bu dala girmez.","branch_image_ar":"موضع منقطع","concept_gloss":"uzak arazi; köy, uzak yer halkı veya mezar","contextual_glosses":[{"applicability":"Söz öbeğinin pek uğranmayan uzak araziyi gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Köy, halk ve mezar kullanımlarını dışarıda bırakır.","preserves":"Uzaklık ve insan uğrağından yoksunluk özelliklerini korur."},"facet_ids":["F001"],"text":"insanlardan uzak ıssız yer","usage_role":"contextual"}],"definition":"İnsanlardan uzak, pek inilmez ve geçilmez bir araziyi anlatır. Aynı söz ailesinde köy, köyler veya bu yerlerin halkı ve mezar için kaydedilmiş ayrı kullanımlar da bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlardan uzak, pek uğranmayan veya geçilmeyen arazi."},{"facet_id":"F002","role":"source_variant","statement":"Köy, köyler ve uzak yerlerin halkı aynı söz ailesinin ayrı yer ve topluluk kullanımlarıdır."},{"facet_id":"F003","role":"source_variant","statement":"Mezar anlamı tek kaynaklı aktarım içinde verilen ayrı bir sözlük kullanımıdır."}],"identity_rationale":"Kaynak ifadesi insanlardan uzak araziyi temel gönderim olarak verir; köy, köyler, bu yerlerin halkı ve mezar anlamları ise aynı söz ailesinin ayrı sözlük kullanımlarıdır. Tanım bunları tek bir 'ıssız yer' nesnesi gibi özdeşleştirmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"insanlardan uzak, pek uğranmayan arazi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"köy veya mezar"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"köyler veya uzak yerlerin halkı"}],"lexicalization_note":"Uzak araziye bağlı söz öbeği ile yalın köy, mezar ve çoğul yer-halk kullanımları ayrı tutulur; kapsamları tek anlamda eritilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yer kavramı ile fiziksel kopuk yer, uzaklık koşulunun sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli sözlük gönderimlerine ve uzaklık koşuluna bağlıdır; komşu dalın çekirdeği genel yer kavramıdır.","focus_only":"Bu dal insanlardan uzak araziyi öne çıkarır ve köy ile mezarı ayrı sözlük kullanımları olarak taşır.","gloss":"uzak arazi veya yer","neighbor_only":"Komşu dal her türlü sınırlı yeri; mamur, boş, yerleşik veya ıssız oluşuna bakmadan genel olarak kapsar.","neighbor_ref":"root_000148/B001","relation_type":"near_neighbor","shared_zone":"Arazi, köy ve mezar gibi yer gönderimleri iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Bu dalda uzaklık insanlarla ilişkilidir; komşu dalda fiziksel kopukluk ve ada yapısı belirleyicidir.","focus_only":"Bu dalın ana yeri insanlardan uzak arazidir; ayrıca köy ve mezar kullanımları vardır.","gloss":"uzak veya kopuk yer","neighbor_only":"Komşu dal belirli bir yer adı yanında deniz içindeki veya karadan kopuk adayı anlatır.","neighbor_ref":"root_000123/B005","relation_type":"near_neighbor","shared_zone":"İnsan yerleşiminden ya da ana karadan ayrılık düşüncesi iki dalı yakınlaştırır."}],"source_phrase_ar":"الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)","source_summary":"Kaynaklar insanlardan uzak arazi anlamında birleşir; toplu kanıt ayrıca köy, köylerin halkı ve mezar anlamlarını ortak çekirdekten ayrılması gereken sözlük kullanımları olarak taşır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكافر من الأرض البعيد عن الناس والكفور للقرى والكفر للقرية والقبر","what_is_not_ar":"ليس الثنايا من الجبال ولا البحر ولا الليل ولا الزرع"},"support_links":[]},{"boundary":"Dağ geçidi ve iri dağ coğrafi facetlerdir; alçak duvar ayrı bir sözlük varyantıdır, köy veya uzak arazi değildir.","branch_kind":"bare","branch_ref":"root_001307/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"dağ geçidi; iri dağ veya alçak duvar","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağlar arasındaki geçit veya geçitler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İri bir dağ, coğrafi alan içindeki ayrı bir kaynak varyantıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Alçak duvar, coğrafi çekirdekten ayrı bir sözlük kullanımıdır."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağ geçidi çekirdeğini öne alırken aynı dalda korunan iki ayrı sözlük varyantını da eksiltmeden gösterir.","boundary_detail":"Dağ geçidi ve iri dağ coğrafi facetlerdir; alçak duvar ayrı bir sözlük varyantıdır, köy veya uzak arazi değildir.","branch_image_ar":"ثنية مستورة","concept_gloss":"dağ geçidi; iri dağ veya alçak duvar","contextual_glosses":[{"applicability":"Çoğul veya tekil biçimin dağlar arasındaki geçidi gösterdiği coğrafi bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İri dağ ve alçak duvar varyantlarını dışarıda bırakır.","preserves":"Dağlık arazideki geçit gönderimini doğal biçimde korur."},"facet_ids":["F001"],"text":"dağ geçidi","usage_role":"contextual"}],"definition":"Dağlar arasındaki geçitler veya iri bir dağ için kullanılan coğrafi bir adlandırmadır; aynı söz ailesinde alçak duvar anlamı da ayrı bir sözlük kullanımı olarak kaydedilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağlar arasındaki geçit veya geçitler."},{"facet_id":"F002","role":"source_variant","statement":"İri bir dağ, coğrafi alan içindeki ayrı bir kaynak varyantıdır."},{"facet_id":"F003","role":"source_variant","statement":"Alçak duvar, coğrafi çekirdekten ayrı bir sözlük kullanımıdır."}],"identity_rationale":"Kaynak ifadesi dağ geçitlerini, iri bir dağı ve alçak duvarı aynı söz ailesinde sıralar; geçitleri 'örtülü' saymak kaynakta kurucu bir koşul değildir. Dal bu nedenle örtülülük altında birleştirilmeden coğrafi çekirdek ve ayrı duvar kullanımı olarak düzenlenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"dağ geçitleri"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"dağ geçidi veya iri dağ"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"alçak duvar"}],"lexicalization_note":"Yalın biçimlerin dağ geçidi, iri dağ ve alçak duvar gönderimleri ayrı tutulur; uzak yer veya genel örtme anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağ geçidi ile sarp dağ yolu, geçit türünün ve zorluk koşulunun sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Geçit gönderiminde yakınlık yüksektir; ancak komşu dal yolun kıvrım ve güzergâh yapısını, bu dal ise ayrı dağ ve duvar varyantlarını da içerir.","focus_only":"Bu dal dağ geçidi yanında iri dağ ve alçak duvar varyantlarını da taşır.","gloss":"dağ geçidi","neighbor_only":"Komşu dal geçidi özellikle dağ veya vadideki yol kıvrımı ve yürünür güzergâh olarak tanımlar.","neighbor_ref":"root_000208/B006","relation_type":"near_synonym","shared_zone":"Dağlık arazideki geçit iki dalın ortak gönderimidir."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeğinde sarplık veya tırmanış şartı yoktur; komşu dalda güç çıkılan yükselen yol belirleyicidir.","focus_only":"Bu dal geçidin yalnızca dağlık yer türünü adlandırır ve zorluk koşulu taşımaz.","gloss":"dağ geçidi","neighbor_only":"Komşu dal dik, engebeli ve çıkılması güç bir dağ yolunu veya benzer yükseltileri merkez alır.","neighbor_ref":"root_001033/B012","relation_type":"near_neighbor","shared_zone":"Dağlık arazide geçiş sağlayan yer iki dalda da bulunabilir."}],"source_phrase_ar":"الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)","source_summary":"Kaynakların çoğu dağ geçitlerini verir; toplu kanıt iri dağ ve alçak duvar anlamlarını da aynı söz ailesinin ayrı varyantları olarak kaydeder.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الكفرات والثنايا من الجبال والكفر العظيم من الجبال والحائط الواطئ","what_is_not_ar":"ليس القرية ولا القبر ولا الأرض البعيدة العامة"},"support_links":[]},{"boundary":"Dal genel içsel alçakgönüllülük değil, baş veya el ve gövdeyle yapılan belirli bir boyun eğme gösterisidir.","branch_kind":"bare","branch_ref":"root_001307/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"eğilerek boyun eğme gösterisi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedeni alçaltan bir hareketle başka birine boyun eğme gösterisi yapma."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup eğilmesi, bu gösterinin belirtilen bedensel biçimleridir."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçsel tutumdan çok baş, el ve gövdeyle yapılan belirli gösteriyi anlatır.","boundary_detail":"Dal genel içsel alçakgönüllülük değil, baş veya el ve gövdeyle yapılan belirli bir boyun eğme gösterisidir.","branch_image_ar":"خضوع متطامن","concept_gloss":"eğilerek boyun eğme gösterisi","contextual_glosses":[{"applicability":"Koruma altındaki gayrimüslim tebaanın başıyla boyun eğme işareti yaptığı tarihî bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Elin göğse konduğu ve bütün bedenin alçaldığı biçimi dışarıda bırakır.","preserves":"Koruma altındaki gayrimüslim tebaanın başıyla yaptığı boyun eğme işaretini korur."},"facet_ids":["F001","F002"],"text":"koruma altındaki gayrimüslim tebaanın başıyla boyun eğmesi","usage_role":"contextual"}],"definition":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup bedenini alçaltması yoluyla başka birine boyun eğdiğini göstermesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedeni alçaltan bir hareketle başka birine boyun eğme gösterisi yapma."},{"facet_id":"F002","role":"example","statement":"Koruma altındaki gayrimüslim tebaanın başıyla işaret etmesi veya bir kişinin elini göğsüne koyup eğilmesi, bu gösterinin belirtilen bedensel biçimleridir."}],"identity_rationale":"Kaynak ifadesi başla işaret etme ile eli göğse koyup bedenini alçaltmayı, başka birine boyun eğme gösterisinin iki bedensel gerçekleşmesi olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"başını eğmek veya elini göğsüne koyup eğilmek"}],"lexicalization_note":"Yalın eylem adı belirli bedensel boyun eğme hareketleriyle sınırlanır; günah giderme veya kişiyi inançsız sayma anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel alçakgönüllülük ve yere kapanma, bu dalın belirli beden hareketi sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli törensel beden hareketidir; komşu dal daha geniş bir içsel ve dışsal alçakgönüllülük alanıdır.","focus_only":"Bu dal başla işaret veya eli göğse koyup eğilme gibi belirli bir kişiye yönelmiş hareketleri şart koşar.","gloss":"eğilerek boyun eğmek","neighbor_only":"Komşu dal içsel alçalışı, ses ve bakışın sakinleşmesini, ibadet duruşunu ve genel gönüllü boyun eğmeyi de kapsar.","neighbor_ref":"root_000412/B001","relation_type":"near_synonym","shared_zone":"Başın ve bedenin alçaltılmasıyla boyun eğme iki dalda ortaktır."},{"boundary_match":"partial","distinction":"Hareketin biçimi farklıdır: bu dal ayakta yapılan eğilme işaretlerini, komşu dal yere kapanmaya kadar uzanan secdeyi kapsar.","focus_only":"Bu dalda alnı yere koymak şart değildir; baş işareti veya göğüste elle eğilme yeterlidir.","gloss":"bedensel boyun eğme","neighbor_only":"Komşu dal alnı yere koymayı ve secde biçimindeki boyun eğmeyi de çekirdeğe alır.","neighbor_ref":"root_000675/B001","relation_type":"near_neighbor","shared_zone":"Bedeni alçaltarak itaat ve saygı gösterme iki dalda ortaktır."}],"source_phrase_ar":"التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)","source_summary":"Kaynaklar başka birine bedensel olarak boyun eğme çekirdeğinde birleşir; başla işaret ve eli göğse koyarak eğilme iki farklı hareket biçimidir.","sources":["AY","SI"],"what_is_ar":"يدخل فيه التكفير بمعنى إيماء الذمي برأسه أو وضع اليد على الصدر والتطامن خضوعا","what_is_not_ar":"ليس تكفير اليمين ولا التكفير عن السيئات ولا نسبة الشخص إلى الكفر"},"support_links":[]},{"boundary":"Dal hükümdarlık tacı ve taç giydirme töreniyle sınırlıdır; genel baş örtüsü veya boyun eğme hareketi değildir.","branch_kind":"bare","branch_ref":"root_001307/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","surface_ar":"كَٰفِرِينَ"}],"gloss":"hükümdara taç giydirme veya taç","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taçlandırma işleminde kullanılan tacın kendisi için aktarılan nesne anlamı."}}],"root_ar":"ك ف ر","root_id":"root_001307","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Süreç ile nesne gönderimini birbirine indirgemeden aynı sözlük alanında birlikte korur.","boundary_detail":"Dal hükümdarlık tacı ve taç giydirme töreniyle sınırlıdır; genel baş örtüsü veya boyun eğme hareketi değildir.","branch_image_ar":"تاج يغطي","concept_gloss":"hükümdara taç giydirme veya taç","contextual_glosses":[{"applicability":"Sözün törensel işlemi bildirdiği eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tacın kendisini adlandıran nesne gönderimini dışarıda bırakır.","preserves":"Hükümdarın başına taç koyma işlemini korur."},"facet_ids":["F001"],"text":"hükümdara taç giydirmek","usage_role":"contextual"}],"definition":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemidir; aynı söz bu işlemde kullanılan tacın kendisini de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hükümdarın başına taç koyarak onu taçlandırma işlemi."},{"facet_id":"F002","role":"source_variant","statement":"Taçlandırma işleminde kullanılan tacın kendisi için aktarılan nesne anlamı."}],"identity_rationale":"Kaynak ifadesi hem hükümdara taç giydirme işlemini hem de bu işlemde kullanılan tacın kendisini açıkça verir; ancak geçici dal imgesindeki tacın örttüğü düşüncesi bir kaynak iddiası değildir. Süreç ve nesne ayrımı korunarak aynı dalda gösterilebilir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"hükümdara taç giydirme veya tacın kendisi"}],"lexicalization_note":"Yalın eylem adının taç giydirme süreci ve taç nesnesi gönderimleri birlikte fakat ayrı facetlerde korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; egemenlik için baş bağlama ve genel baş süsü dalları, taçlandırmanın işlevsel sınırını açıkladığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal taç ve hükümdarla sınırlıdır; komşu dal sarık, başa geçirme ve topluluğun kişiyi önder sayması gibi daha geniş süreçleri de içerir.","focus_only":"Bu dal özellikle hükümdara taç giydirme işlemini ve tacın kendisini adlandırır.","gloss":"taçlandırma","neighbor_only":"Komşu dal taç yanında sarık bağlamayı, kişiyi başa geçirmeyi ve egemenlik işaretini daha geniş biçimde kapsar.","neighbor_ref":"root_001018/B008","relation_type":"near_neighbor","shared_zone":"Baş üzerine taç koyma ve bunu egemenlik işareti yapma iki dalda ortaktır."},{"boundary_match":"field_only","distinction":"Bu dal hükümdarlık ve taçlandırma işlevine bağlıdır; komşu dalın çekirdeği başa konan nesnelerin genel sınıfıdır.","focus_only":"Bu dal taç giydirme eylemini ve hükümdarlık tacını bildirir.","gloss":"başa konan taç","neighbor_only":"Komşu dal başa süs veya örtü olarak konan sarık, başlık, taç ve bitki gibi nesneleri genel olarak kapsar.","neighbor_ref":"root_001044/B005","relation_type":"same_field","shared_zone":"Taç, başın üstüne konan bir nesne olarak iki dalın ortak alanıdır."}],"source_phrase_ar":"التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Söz hem hükümdara taç giydirme işlemi hem de bu işlemde kullanılan tacın adı olarak aktarılır."}],"source_summary":"Tek kaynaklı kanıt, hükümdarı taçlandırma süreci ile bu süreçte kullanılan taç nesnesini aynı sözün iki bağlı gönderimi olarak kaydeder.","sources":["AY"],"what_is_ar":"يدخل فيه التكفير بمعنى تتويج الملك بتاج أو التاج نفسه","what_is_not_ar":"ليس الخضوع ولا الكفارة ولا الكفر الديني"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["18:100:1"],"branch_refs":[],"candidate_id":"cand_4764ef13040b623577a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:1:boundary-continuation","source_type":"word_analysis","support_ids":["sup_22e6b4614775378f4303","sup_964c33044ee66522fdb3"],"title":"continuation that launches a new display scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:1","qac_refs":["18:100:1:1"],"status":"accepted"}},{"anchor_refs":["18:100:1"],"branch_refs":[],"candidate_id":"cand_8beb201d76b913c3a7a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:1:clitic-verbal-launch","source_type":"word_analysis","support_ids":["sup_22e6b4614775378f4303","sup_fe9c1bc2035b5bc0a792"],"title":"clitic transition fused to the display verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:1","qac_refs":["18:100:1:1"],"status":"accepted"}},{"anchor_refs":["18:100:1"],"branch_refs":[],"candidate_id":"cand_577551af932624103be3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:1:perfect-scene-register","source_type":"word_analysis","support_ids":["sup_22e6b4614775378f4303","sup_c12df497a568696ff887"],"title":"boundary into an accomplished-future register","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:1","qac_refs":["18:100:1:1"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_05c59dae1948527014fb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:boundary-visual-shift","source_type":"word_analysis","support_ids":["sup_1c2fbea877f5f9a3010a","sup_98a8fb505ec844e980d7"],"title":"gathering and sound become visual exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_587af6a6d2d8cc246d74","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:complete-display-frame","source_type":"word_analysis","support_ids":["sup_7bb6b93caff7dd5990ee","sup_98a8fb505ec844e980d7"],"title":"explicit object, target, time, and intensifier frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_21f7f8a051f0e61aa137","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:direct-display-selected","source_type":"word_analysis","support_ids":["sup_40f11c15b1d5f242f71e","sup_98a8fb505ec844e980d7"],"title":"direct manifestation over offer, occurrence, or oblique forms","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_68f6e09e027662cec5f8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:exposure-breadth-covering-reversal","source_type":"word_analysis","support_ids":["sup_557bcef5bcc8d98a4dac","sup_98a8fb505ec844e980d7"],"title":"exposure and breadth pressure around the display","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_31bc50c6b698a872c1f5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:local-root-envelope","source_type":"word_analysis","support_ids":["sup_98a8fb505ec844e980d7","sup_efec43da74cba5d6a6ad"],"title":"opening verb anticipates the closing cognate noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_56f34fbdffa93110b159","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:perfect-divine-agency","source_type":"word_analysis","support_ids":["sup_347ef784249e871e823c","sup_98a8fb505ec844e980d7"],"title":"completed first-person agency after passive sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:2"],"branch_refs":[],"candidate_id":"cand_02039a9e849f3d68baa4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:2:same-surah-display-echo","source_type":"word_analysis","support_ids":["sup_0fc25fcba09668627c0e","sup_98a8fb505ec844e980d7"],"title":"display root returns with reversed roles","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:2","qac_refs":["18:100:1:2","18:100:1:3"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_d7fe09de8b67c3715220","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:dense-sound-shape","source_type":"word_analysis","support_ids":["sup_74ba88ec33908d55ea65","sup_7719339d7c4df825d263"],"title":"heavy proper-name sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_8d2542e4c2e9c58d167f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:foreign-name-inside-arabic-frame","source_type":"word_analysis","support_ids":["sup_74ba88ec33908d55ea65","sup_a147f2c2421c41f7cf13"],"title":"foreign proper name absorbed into Arabic governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_b4a678a07e4d1da05d02","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:named-depth-not-generic-fire","source_type":"word_analysis","support_ids":["sup_74ba88ec33908d55ea65","sup_df23070da1bff7bfd3af"],"title":"named Jahannam with depth pressure, not generic fire","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_689a1a693f0a383177a4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:proper-object-diptote","source_type":"word_analysis","support_ids":["sup_36a408e9ff12f5782310","sup_74ba88ec33908d55ea65"],"title":"proper-name object with marked diptote case","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_3630133ccc5623804fc1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:recognized-kafir-pairing","source_type":"word_analysis","support_ids":["sup_1cd0c9266c0449c894a6","sup_74ba88ec33908d55ea65"],"title":"Jahannam paired with the classified recipients","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:3"],"branch_refs":[],"candidate_id":"cand_bccdbe9a171996ceab2f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:3:surah-local-jahannam-sequence","source_type":"word_analysis","support_ids":["sup_74ba88ec33908d55ea65","sup_e61d2fe33d81b742aa0e"],"title":"display begins a local Jahannam sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:3","qac_refs":["18:100:2:1"],"status":"accepted"}},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_da3ecf7b0fcf4c68c509","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:4:deictic-ellipsis-compound","source_type":"word_analysis","support_ids":["sup_6ec2700cc054420296cc","sup_fc6da9c4e1614994c40a"],"title":"compressed then-day with recoverable event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:4","qac_refs":["18:100:3:1"],"status":"accepted"}},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_e611ca02e22a77aaaaa9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:4:event-period-not-calendar-day","source_type":"word_analysis","support_ids":["sup_5e9dbda3445196af1a7a","sup_6ec2700cc054420296cc"],"title":"judgment-event period rather than ordinary day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:4","qac_refs":["18:100:3:1"],"status":"accepted"}},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_afda8e26599b41d8da79","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:4:same-surah-temporal-spine","source_type":"word_analysis","support_ids":["sup_6ec2700cc054420296cc","sup_de9e81cbc5cd75cdd23b"],"title":"repeated day-marker locks scenes together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:4","qac_refs":["18:100:3:1"],"status":"accepted"}},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_f623aaf10cd057795c35","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:4:structural-acoustic-pivot","source_type":"word_analysis","support_ids":["sup_6ec2700cc054420296cc","sup_9512c8cb783b9bc57bf2"],"title":"single-word pivot between object and recipients","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:4","qac_refs":["18:100:3:1"],"status":"accepted"}},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_aa2fc2c05ec6bdea5444","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:4:temporal-adverbial-scope","source_type":"word_analysis","support_ids":["sup_16b17752237ddb098447","sup_6ec2700cc054420296cc"],"title":"time-stamp over the whole display","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:4","qac_refs":["18:100:3:1"],"status":"accepted"}},{"anchor_refs":["18:100:5"],"branch_refs":[],"candidate_id":"cand_861a9b68fe4569b13a34","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:5:adverse-targeting","source_type":"word_analysis","support_ids":["sup_7a1bbb80c957054ccff5","sup_e1bddeee07116d77e1d3"],"title":"adversative target, not benefit or possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:5","qac_refs":["18:100:4:1"],"status":"accepted"}},{"anchor_refs":["18:100:5"],"branch_refs":[],"candidate_id":"cand_2ad9999b086124e404cd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:5:forward-lodging-formula","source_type":"word_analysis","support_ids":["sup_5a7b449f7e4fe0380c26","sup_e1bddeee07116d77e1d3"],"title":"current target relation anticipates 18:102","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:5","qac_refs":["18:100:4:1"],"status":"accepted"}},{"anchor_refs":["18:100:5"],"branch_refs":[],"candidate_id":"cand_c493e668255f432de57f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:5:fused-target-class-form","source_type":"word_analysis","support_ids":["sup_d6b476c3ffa2a41c665e","sup_e1bddeee07116d77e1d3"],"title":"fused preposition and article compact the target relation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:5","qac_refs":["18:100:4:1"],"status":"accepted"}},{"anchor_refs":["18:100:5"],"branch_refs":[],"candidate_id":"cand_74e832d05a75cd7f2923","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:100:5:scope-across-time","source_type":"word_analysis","support_ids":["sup_0f29c62bb772bd58ff09","sup_e1bddeee07116d77e1d3"],"title":"target phrase attaches across the temporal beat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:5","qac_refs":["18:100:4:1"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_7c8d304b672ad7685a5d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:covering-display-reversal","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_395e68c92a94f93ea2ed"],"title":"coverers confronted by exposure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_c28d318dc796694934a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:definite-agent-class-target","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_7358276849808a395ac4"],"title":"definite participial class under prepositional governance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_2d7138c8c418963317ff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:denial-over-ingratitude","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_a6bf1247ab25825625d0"],"title":"denial and concealment prioritized over mere ingratitude","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_83b2300e42534689e89d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:jahannam-kafir-sequence","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_e21867bd9d8455b23246"],"title":"recognized Jahannam-denier sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_f91f0fb7648d571dfd00","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:position-and-pronoun-resolution","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_fb1a5038f341b04f7eae"],"title":"delayed class name resolves the gathered mass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_33317734ad264897d6ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:rough-acoustic-label","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_760b0d4e78cd719569bb"],"title":"rough sound of the recipient label","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:6"],"branch_refs":[],"candidate_id":"cand_0092ae0fcf6bb829d59c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:6:surah-local-classification-thread","source_type":"word_analysis","support_ids":["sup_21beed8e45e9921030d3","sup_80bf6dd50913111c3d4c"],"title":"classification thread through the surah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:6","qac_refs":["18:100:4:2","18:100:4:3"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_cfd27e6ab2b35b5d7097","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:closing-display-ring","source_type":"word_analysis","support_ids":["sup_78fec2ca9e489910760d","sup_ae0646803c5f8e5ab7b1"],"title":"final root return frames the whole ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_05950b6b5c2c034b4191","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:closure-weight-and-cadence","source_type":"word_analysis","support_ids":["sup_78fec2ca9e489910760d","sup_831810f8afe033e645f9"],"title":"heavy final sound and matched boundary cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_baa75deb4bb8ca2d0549","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:cognate-accusative-emphasis","source_type":"word_analysis","support_ids":["sup_469111921d3ec4a25780","sup_78fec2ca9e489910760d"],"title":"internal emphasis, not a second object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_028e143bb4ea977bea7a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:display-breadth-pressure","source_type":"word_analysis","support_ids":["sup_1ca382fad2a8deffd424","sup_78fec2ca9e489910760d"],"title":"act of display with breadth and formal presentation pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_4b1afda246e668eca070","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:form-not-adjective-or-new-verb","source_type":"word_analysis","support_ids":["sup_3c7b12c7d8401db35e33","sup_78fec2ca9e489910760d"],"title":"maṣdar form avoids adjective-only width and new event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_7f46129b486ea1951e0e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:indefinite-unbounded-quality","source_type":"word_analysis","support_ids":["sup_78fec2ca9e489910760d","sup_ba3f48ebc3060ede955f"],"title":"indefinite display of unstated extent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:7"],"branch_refs":[],"candidate_id":"cand_ed162018abd9031cec22","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:7:marked-nominal-return","source_type":"word_analysis","support_ids":["sup_78fec2ca9e489910760d","sup_ec79bfa7bd907c3c7935"],"title":"minority gerund form makes the return marked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:100:7","qac_refs":["18:100:5:1"],"status":"accepted"}},{"anchor_refs":["18:100:1"],"branch_refs":[],"candidate_id":"cand_d971ad7f86b818c72be1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001001"],"scope":"focus_ayah","source_local_id":"18:100:1:2","source_type":"qac_morpheme","support_ids":["sup_4dc2f760eff493d2936f"],"title":"QAC root occurrence: ع ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:100:4"],"branch_refs":[],"candidate_id":"cand_4ba5cd8a2001082daef2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001307"],"scope":"focus_ayah","source_local_id":"18:100:4:3","source_type":"qac_morpheme","support_ids":["sup_880802722cb39ad2bddc"],"title":"QAC root occurrence: ك ف ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:100"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:100","branch_refs":["root_001001/B002","root_001307/B001"],"candidate_id":"cand_2ab01e70a8a6014a953e","commentary_obligation":"review","hft_ref":"hft_d50fafb5140637b8e16e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b1_forced_uncovering","source_type":"hft","support_ids":["sup_318377b2b29b948dc703"],"title":"b1_forced_uncovering","trust":"legacy_unbound"},{"anchor_refs":["18:100"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:100","branch_refs":["root_001001/B004","root_001307/B003"],"candidate_id":"cand_ff5bb4621c1a7c8a9247","commentary_obligation":"review","hft_ref":"hft_1a9cbbf1134fea23de99","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b2_blocking_confrontation","source_type":"hft","support_ids":["sup_f82496056045a990aee9"],"title":"b2_blocking_confrontation","trust":"legacy_unbound"},{"anchor_refs":["18:100"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:100","branch_refs":["root_001001/B003","root_001307/B002"],"candidate_id":"cand_98a237407e25b4f6e835","commentary_obligation":"review","hft_ref":"hft_5167e5f02cfbd609ac7e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b3_horizon_front","source_type":"hft","support_ids":["sup_399d68221f85ed7c82ae"],"title":"b3_horizon_front","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"18:100:1:1","qac_word_ref":"18:100:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","root_ar":"ع ر ض","surface_ar":"عَرَضْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:100:1:3","qac_word_ref":"18:100:1","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"جَهَنَّم","morph_features":"STEM|POS:PN|LEM:jahan~am|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"18:100:2:1","qac_word_ref":"18:100:2","root_ar":"","surface_ar":"جَهَنَّمَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"18:100:3:1","qac_word_ref":"18:100:3","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:100:4:1","qac_word_ref":"18:100:4","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"18:100:4:2","qac_word_ref":"18:100:4","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","root_ar":"ك ف ر","surface_ar":"كَٰفِرِينَ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","root_ar":"ع ر ض","surface_ar":"عَرْضًا"}],"word_analysis_qac_refs":[["18:100:1:1"],["18:100:1:2","18:100:1:3"],["18:100:2:1"],["18:100:3:1"],["18:100:4:1"],["18:100:4:2","18:100:4:3"],["18:100:5:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["18:100:1","18:100:2","18:100:3","18:100:4","18:100:5","18:100:6","18:100:7"]},"focus_surface_evidence":{"arabic_uthmani":"وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"18:100:1:1","qac_word_ref":"18:100:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"عَرَضَ","morph_features":"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:100:1:2","qac_word_ref":"18:100:1","root_ar":"ع ر ض","surface_ar":"عَرَضْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:100:1:3","qac_word_ref":"18:100:1","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"جَهَنَّم","morph_features":"STEM|POS:PN|LEM:jahan~am|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"18:100:2:1","qac_word_ref":"18:100:2","root_ar":"","surface_ar":"جَهَنَّمَ"},{"lemma_ar":"يَوْمَئِذ","morph_features":"STEM|POS:T|LEM:yawoma}i*","morpheme_role":"STEM","pos":"T","qac_ref":"18:100:3:1","qac_word_ref":"18:100:3","root_ar":"","surface_ar":"يَوْمَئِذٍ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:100:4:1","qac_word_ref":"18:100:4","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"18:100:4:2","qac_word_ref":"18:100:4","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"كَٰفِرُون","morph_features":"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:4:3","qac_word_ref":"18:100:4","root_ar":"ك ف ر","surface_ar":"كَٰفِرِينَ"},{"lemma_ar":"عَرْض","morph_features":"STEM|POS:N|LEM:EaroD|ROOT:ErD|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:100:5:1","qac_word_ref":"18:100:5","root_ar":"ع ر ض","surface_ar":"عَرْضًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["18:100:1:1"],["18:100:1:2","18:100:1:3"],["18:100:2:1"],["18:100:3:1"],["18:100:4:1"],["18:100:4:2","18:100:4:3"],["18:100:5:1"]],"word_analysis_refs":["18:100:1","18:100:2","18:100:3","18:100:4","18:100:5","18:100:6","18:100:7"],"word_rows":[{"analysis_record_ref":"18:100:1","analytic_gloss_range_en":"resumptive and coordinating conjunction that carries the reader from the gathered scene into the display scene","analytic_root_gloss_range_en":null,"qac_refs":["18:100:1:1"],"root":{"note":"no root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"18:100:2","analytic_gloss_range_en":"perfect first-person plural verb of deliberate display or presentation, with explicit object, time, target, and final cognate reinforcement","analytic_root_gloss_range_en":"broad root range of display, presentation, breadth, exposure, turning away, obstruction, occurrence, and honor; local Form I transitive grammar selects deliberate display while allowing exposure and breadth pressure","qac_refs":["18:100:1:2","18:100:1:3"],"root":{"arabic":"ع ر ض","transliteration":"ʿ-r-ḍ"},"surface":{"arabic":"عَرَضْنَا","transliteration":"ʿaraḍnā"}},{"analysis_record_ref":"18:100:3","analytic_gloss_range_en":"proper-name direct object of the display, marked accusative without tanwīn as a foreign diptote","analytic_root_gloss_range_en":"proper-name field for Jahannam as the eschatological abode of punishment, with foreign-name marking and secondary depth or abyss pressure; local grammar selects the named object of display","qac_refs":["18:100:2:1"],"root":{"arabic":"ج ه ن م","transliteration":"j-h-n-m"},"surface":{"arabic":"جَهَنَّمَ","transliteration":"jahannama"}},{"analysis_record_ref":"18:100:4","analytic_gloss_range_en":"accusative temporal adverbial compound meaning the day or time then, referring back to the prior eschatological event-frame","analytic_root_gloss_range_en":"range of day, time-span, event-period, and marked occasion; local compound selects the anaphoric judgment-event frame rather than an ordinary calendar day","qac_refs":["18:100:3:1"],"root":{"arabic":"ي و م","transliteration":"y-w-m"},"surface":{"arabic":"يَوْمَئِذٍۢ","transliteration":"yawmaʾidhin"}},{"analysis_record_ref":"18:100:5","analytic_gloss_range_en":"preposition governing the recipient class as the adverse target of the display, not a loose beneficiary","analytic_root_gloss_range_en":null,"qac_refs":["18:100:4:1"],"root":{"note":"no root"},"surface":{"arabic":"لِ","transliteration":"li"}},{"analysis_record_ref":"18:100:6","analytic_gloss_range_en":"definite active-participle plural governed by the target preposition, naming the affected class of deniers or coverers","analytic_root_gloss_range_en":"root range of covering, denial, ingratitude, expiation, concealment, farmer-covering, and related derivatives; local active participle selects the denier or coverer class while the display context reverses concealment","qac_refs":["18:100:4:2","18:100:4:3"],"root":{"arabic":"ك ف ر","transliteration":"k-f-r"},"surface":{"arabic":"الْكَافِرِينَ","transliteration":"al-kāfirīna"}},{"analysis_record_ref":"18:100:7","analytic_gloss_range_en":"indefinite accusative verbal noun functioning as a cognate accusative that intensifies the single display event","analytic_root_gloss_range_en":"root range of display, presentation, breadth, review, exposure, turning away, and related branches; local maṣdar selects the act of display while breadth and formal-presentation pressure remain secondary","qac_refs":["18:100:5:1"],"root":{"arabic":"ع ر ض","transliteration":"ʿ-r-ḍ"},"surface":{"arabic":"عَرْضًا","transliteration":"ʿarḍan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["18:100"],"branch_refs":["root_001001/B002","root_001307/B001"],"candidate_id":"cand_2ab01e70a8a6014a953e","evidence_scope":"focus_ayah","hft_ref":"hft_d50fafb5140637b8e16e","item_id":"b1_forced_uncovering","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b1_forced_uncovering","support_id":"sup_318377b2b29b948dc703"},{"anchor_refs":["18:100"],"branch_refs":["root_001001/B004","root_001307/B003"],"candidate_id":"cand_ff5bb4621c1a7c8a9247","evidence_scope":"focus_ayah","hft_ref":"hft_1a9cbbf1134fea23de99","item_id":"b2_blocking_confrontation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b2_blocking_confrontation","support_id":"sup_f82496056045a990aee9"},{"anchor_refs":["18:100"],"branch_refs":["root_001001/B003","root_001307/B002"],"candidate_id":"cand_98a237407e25b4f6e835","evidence_scope":"focus_ayah","hft_ref":"hft_5167e5f02cfbd609ac7e","item_id":"b3_horizon_front","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b3_horizon_front","support_id":"sup_399d68221f85ed7c82ae"}],"diagnostics":[],"lane_counts":{"global":7,"macro":7,"micro":3},"packet_summary":{"ayah_count":12,"focus_ref":"18:100","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["18:99","18:100","18:101","18:102","18:103","18:104","18:105","18:106","18:107","18:108","18:109","18:110"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"18:100","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":10,"unstructured_record_count":0},"identity":{"ayah_ref":"18:100","lane":"micro","linguistic_source_ref":"18:100","surface_ref":"18:100","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"18:100","target_tokens":[["O",["18:100:1"]],["gün",["18:100:1"]],["cehennemi",["18:100:2"]],["inkâr",["18:100:3"]],["edenlere",["18:100:3"]],["açıkça",["18:100:4"]],["gösteririz",["18:100:5"]]],"text":"O gün cehennemi inkâr edenlere açıkça gösteririz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":99,"ayah_to":110,"id":"s018-p06-099-110","label":"Final judgment and the measure of deeds","number":6,"refs":["18:99","18:100","18:101","18:102","18:103","18:104","18:105","18:106","18:107","18:108","18:109","18:110"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:5:scope-across-time","source_type":"word_analysis","support_id":"sup_0f29c62bb772bd58ff09","text":"{\"blocking_evidence\":null,\"headline\":\"target phrase attaches across the temporal beat\",\"reader_payoff\":\"The reader notices that the audience is delayed until after the day is fixed, yet the preposition still attaches the group to the display verb.\",\"reason\":\"The attachment evidence marks the prepositional complement as a dependent of the display verb despite its position after the temporal adverbial.\",\"representative_source_ids\":[\"QG-b24b0753\",\"QG-eb13daba\",\"QT-40c5105b\",\"QT-8761366a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:same-surah-display-echo","source_type":"word_analysis","support_id":"sup_0fc25fcba09668627c0e","text":"{\"blocking_evidence\":null,\"headline\":\"display root returns with reversed roles\",\"reader_payoff\":\"The reader notices the same-surah role reversal: humans are displayed before the Lord in 18:48, while here Jahannam is displayed before the deniers.\",\"reason\":\"The CRITICAL rows give concrete same-surah references, and nothing in the local grammar blocks using them as echo and contrast.\",\"representative_source_ids\":[\"QI-b54ceb85\",\"MI-9df3186a\",\"QE-db69dff6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4:temporal-adverbial-scope","source_type":"word_analysis","support_id":"sup_16b17752237ddb098447","text":"{\"blocking_evidence\":null,\"headline\":\"time-stamp over the whole display\",\"reader_payoff\":\"The reader notices that the word frames the whole event in time, instead of acting as another object or loose modifier.\",\"reason\":\"Attachment evidence marks the word as the temporal adverbial of the display verb, and QAC identifies its accusative time function.\",\"representative_source_ids\":[\"QG-5c16460c\",\"QG-8fd04f12\",\"QS-c1ad420b\",\"MT-a6faca97\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:boundary-visual-shift","source_type":"word_analysis","support_id":"sup_1c2fbea877f5f9a3010a","text":"{\"blocking_evidence\":null,\"headline\":\"gathering and sound become visual exposure\",\"reader_payoff\":\"The reader notices that the prior gathering supplies the audience and that the passive acoustic scene turns into active visual presentation.\",\"reason\":\"The boundary rows are concrete and align with the attachment evidence that the current clause is a new verbal display scene after 18:99.\",\"representative_source_ids\":[\"QB-1e8c82e4\",\"QB-209100ec\",\"QB-b5fa42ac\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:display-breadth-pressure","source_type":"word_analysis","support_id":"sup_1ca382fad2a8deffd424","text":"{\"blocking_evidence\":null,\"headline\":\"act of display with breadth and formal presentation pressure\",\"reader_payoff\":\"The reader notices that the word names the act of display while the root's breadth and exhibition field lets the closing act feel expansive and audience-directed.\",\"reason\":\"The cognate construction selects the verbal-noun display sense first, while V4 and the target phrase support breadth and formal presentation as secondary pressure.\",\"representative_source_ids\":[\"QS-27f159a1\",\"QS-796a91bd\",\"QS-ee223b2b\",\"QY-e546cab7\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:recognized-kafir-pairing","source_type":"word_analysis","support_id":"sup_1cd0c9266c0449c894a6","text":"{\"blocking_evidence\":null,\"headline\":\"Jahannam paired with the classified recipients\",\"reader_payoff\":\"The reader notices that the named object and the recipient class form a recognized judgment pairing, intensified here by the day frame.\",\"reason\":\"The contextual profiles support repeated co-occurrence with the recipient root and judgment-day timing, while local grammar keeps the word as the displayed object.\",\"representative_source_ids\":[\"QI-495c53b2\",\"QI-e955f941\",\"MI-ccfadb6d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6","source_type":"word_analysis","support_id":"sup_21beed8e45e9921030d3","text":"{\"gloss_range\":\"definite active-participle plural governed by the target preposition, naming the affected class of deniers or coverers\",\"prose\":\"{{ar:الْكَافِرِينَ}} ({{tr:al-kāfirīna}}) names the audience only after the object and day have been fixed. Its article, active participle, and masculine plural ending build a definite class out of an action, while the preposition makes that class the affected target rather than the displayed object. The covering root becomes pointed in this clause: those characterized by covering or denial are placed before a display that undoes concealment, while mere ingratitude remains secondary to that confrontation. The word also resolves the gathered mass from 18:99 and starts a local sequence in which the same class is linked with Jahannam in 18:102 and 18:106, after the earlier 18:29 fire formula has used a different recipient term. Its hard kāf, fricative fāʾ, and rolling rāʾ give the recipient label a rough audible edge before the final noun lands.\",\"root_display\":\"{{ar:ك ف ر}} ({{tr:k-f-r}})\",\"root_gloss_range\":\"root range of covering, denial, ingratitude, expiation, concealment, farmer-covering, and related derivatives; local active participle selects the denier or coverer class while the display context reverses concealment\",\"surface_display\":\"{{ar:الْكَافِرِينَ}} ({{tr:al-kāfirīna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:1","source_type":"word_analysis","support_id":"sup_22e6b4614775378f4303","text":"{\"gloss_range\":\"resumptive and coordinating conjunction that carries the reader from the gathered scene into the display scene\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah as both continuation and scene launch. It ties the display to the gathering in 18:99, but it also resets the discourse into a new divine presentation scene. Because the particle is fused to the following perfect verb in recitation and writing, the transition moves straight into an act presented as settled; the boundary does not pause before the display begins.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:perfect-divine-agency","source_type":"word_analysis","support_id":"sup_347ef784249e871e823c","text":"{\"blocking_evidence\":null,\"headline\":\"completed first-person agency after passive sound\",\"reader_payoff\":\"The reader notices a shift from the passive trumpet register of 18:99 into an explicitly claimed divine act of making visible.\",\"reason\":\"The verb is active perfect with first-person plural subject agreement carried in the suffix, and the eschatological context supports the accomplished-future force.\",\"representative_source_ids\":[\"QG-c4bb601c\",\"QG-dc35ecec\",\"QG-eec4533e\",\"QY-cb4a5de6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:proper-object-diptote","source_type":"word_analysis","support_id":"sup_36a408e9ff12f5782310","text":"{\"blocking_evidence\":null,\"headline\":\"proper-name object with marked diptote case\",\"reader_payoff\":\"The reader notices that the displayed object is a named reality placed under the verb, not an indefinite punishment term or a locative setting.\",\"reason\":\"QAC and attachment evidence identify the word as the accusative direct object, while the foreign proper noun and diptote behavior explain the lack of tanwīn.\",\"representative_source_ids\":[\"QG-3c704337\",\"QG-a41669e1\",\"QG-fd7fba1b\",\"QY-63cab00e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:covering-display-reversal","source_type":"word_analysis","support_id":"sup_395e68c92a94f93ea2ed","text":"{\"blocking_evidence\":null,\"headline\":\"coverers confronted by exposure\",\"reader_payoff\":\"The reader notices the local reversal: the class named by covering or denial is confronted by a display that makes hidden consequence visible.\",\"reason\":\"The root range includes covering and denial, while the local display frame blocks expiatory covering and selects the reversal of concealment.\",\"representative_source_ids\":[\"QS-2d378f35\",\"QS-c7d6136a\",\"QE-4713e8eb\",\"QY-c20bcd81\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:form-not-adjective-or-new-verb","source_type":"word_analysis","support_id":"sup_3c7b12c7d8401db35e33","text":"{\"blocking_evidence\":null,\"headline\":\"maṣdar form avoids adjective-only width and new event\",\"reader_payoff\":\"The reader notices that the form keeps focus on the act itself: it is neither a mere adjective of width nor a second finite display.\",\"reason\":\"The local form is a gerund or verbal noun, and the attachment evidence makes it dependent on the earlier verb.\",\"representative_source_ids\":[\"QF-0fe27374\",\"QF-3a9033c1\",\"QF-6d829edb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:direct-display-selected","source_type":"word_analysis","support_id":"sup_40f11c15b1d5f242f71e","text":"{\"blocking_evidence\":null,\"headline\":\"direct manifestation over offer, occurrence, or oblique forms\",\"reader_payoff\":\"The reader notices that the root range is routed into direct manifestation: Jahannam is made perceptible before the recipients, not offered for acceptance or merely said to occur.\",\"reason\":\"V4 preserves other branches, but the local Form I transitive frame with an explicit object and target selects deliberate presentation.\",\"representative_source_ids\":[\"QS-c3594ed8\",\"QS-e2434db4\",\"QS-e500b2a0\",\"QY-bb04bebd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:cognate-accusative-emphasis","source_type":"word_analysis","support_id":"sup_469111921d3ec4a25780","text":"{\"blocking_evidence\":null,\"headline\":\"internal emphasis, not a second object\",\"reader_payoff\":\"The reader notices that the closing noun intensifies the original display event from within rather than adding another thing displayed.\",\"reason\":\"Attachment evidence marks the word as a cognate accusative reinforcing the display verb, not as a separate direct object.\",\"representative_source_ids\":[\"QG-c1a0e90f\",\"QG-cedae3ce\",\"MG-4bd4d8ba\",\"QY-042090e2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:100:1:2","source_type":"qac_morpheme","support_id":"sup_4dc2f760eff493d2936f","text":"{\"lemma_ar\":\"عَرَضَ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:EaraDa|ROOT:ErD|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"18:100:1:2\",\"qac_word_ref\":\"18:100:1\",\"root_ar\":\"ع ر ض\",\"surface_ar\":\"عَرَضْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:exposure-breadth-covering-reversal","source_type":"word_analysis","support_id":"sup_557bcef5bcc8d98a4dac","text":"{\"blocking_evidence\":null,\"headline\":\"exposure and breadth pressure around the display\",\"reader_payoff\":\"The reader notices that the display root does more than mark seeing; it turns concealment into exposure and lets the final noun widen the act's force.\",\"reason\":\"The covering reversal and breadth pressure are coherent secondary payoffs, but the local verb still selects direct display rather than every root branch.\",\"representative_source_ids\":[\"QS-b79f5c24\",\"QS-d6095097\",\"MS-ebfc9ea0\",\"QY-6efb8629\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:5:forward-lodging-formula","source_type":"word_analysis","support_id":"sup_5a7b449f7e4fe0380c26","text":"{\"blocking_evidence\":null,\"headline\":\"current target relation anticipates 18:102\",\"reader_payoff\":\"The reader notices that the display-to relation in 18:100 becomes a prepared-for relation for the same class in 18:102.\",\"reason\":\"The boundary row provides a concrete same-surah forward reference, and local grammar supports the target relation that later returns.\",\"representative_source_ids\":[\"QB-7ac8b710\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4:event-period-not-calendar-day","source_type":"word_analysis","support_id":"sup_5e9dbda3445196af1a7a","text":"{\"blocking_evidence\":null,\"headline\":\"judgment-event period rather than ordinary day\",\"reader_payoff\":\"The reader notices that the day is a marked event-frame, not merely a twenty-four-hour calendar span.\",\"reason\":\"The root range allows ordinary day and event-period, but the eschatological context and deictic compound select the judgment-event frame.\",\"representative_source_ids\":[\"QS-32328519\",\"QS-516c3298\",\"QS-8867cf19\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4","source_type":"word_analysis","support_id":"sup_6ec2700cc054420296cc","text":"{\"gloss_range\":\"accusative temporal adverbial compound meaning the day or time then, referring back to the prior eschatological event-frame\",\"prose\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}}) time-stamps the whole display. As a bare accusative temporal adverbial, it is not another object or participant; it locates the act, object, and audience together. Its compound form points back through a suppressed event clause, and the consecutive repetition from 18:99 identifies that event as the trumpet, surging, and gathering scene. The word therefore works as a temporal clamp between the named object and the recipients, tying both scenes to one judgment-day frame rather than an ordinary calendar day. It also belongs to the surah's broader judgment-time thread, which continues through 18:105.\",\"root_display\":\"{{ar:ي و م}} ({{tr:y-w-m}})\",\"root_gloss_range\":\"range of day, time-span, event-period, and marked occasion; local compound selects the anaphoric judgment-event frame rather than an ordinary calendar day\",\"surface_display\":\"{{ar:يَوْمَئِذٍۢ}} ({{tr:yawmaʾidhin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:definite-agent-class-target","source_type":"word_analysis","support_id":"sup_7358276849808a395ac4","text":"{\"blocking_evidence\":null,\"headline\":\"definite participial class under prepositional governance\",\"reader_payoff\":\"The reader notices that the phrase is not a neutral plural label; it is a definite agent-class made the display's affected target.\",\"reason\":\"QAC identifies the word as a definite active participle plural governed by the preposition, matching the CRITICAL class-label rows.\",\"representative_source_ids\":[\"QG-03833458\",\"QG-d2f4bf18\",\"QF-984f4815\",\"QY-166c54c8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3","source_type":"word_analysis","support_id":"sup_74ba88ec33908d55ea65","text":"{\"gloss_range\":\"proper-name direct object of the display, marked accusative without tanwīn as a foreign diptote\",\"prose\":\"{{ar:جَهَنَّمَ}} ({{tr:jahannama}}) is fixed immediately as the thing displayed. It is definite by proper name rather than by article, accusative as the object of the verb, and diptote without ordinary tanwīn, so the grammar treats a marked foreign proper name as the visible object. The word is not just a generic fire term: its proper-name force, depth pressure, and later same-surah returns make this the first local presentation of the named destination that will be prepared for the denier class and named as recompense in 18:102 and 18:106. Its guttural and nasal sound-shape, especially the doubled nūn, gives the focal object audible density inside the compact clause.\",\"root_display\":\"{{ar:ج ه ن م}} ({{tr:j-h-n-m}})\",\"root_gloss_range\":\"proper-name field for Jahannam as the eschatological abode of punishment, with foreign-name marking and secondary depth or abyss pressure; local grammar selects the named object of display\",\"surface_display\":\"{{ar:جَهَنَّمَ}} ({{tr:jahannama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:rough-acoustic-label","source_type":"word_analysis","support_id":"sup_760b0d4e78cd719569bb","text":"{\"blocking_evidence\":null,\"headline\":\"rough sound of the recipient label\",\"reader_payoff\":\"The reader notices that the class label has a rough consonantal texture, giving the named recipients audible weight before the final display noun.\",\"reason\":\"The phonetic row is concrete and locally tied to the recipient label's sound-shape.\",\"representative_source_ids\":[\"QP-778de91b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:dense-sound-shape","source_type":"word_analysis","support_id":"sup_7719339d7c4df825d263","text":"{\"blocking_evidence\":null,\"headline\":\"heavy proper-name sound\",\"reader_payoff\":\"The reader notices that the focal object has a dense guttural and nasal sound-shape, matching its weight as the displayed noun.\",\"reason\":\"The phonetic rows are locally tied to the displayed proper noun and add a small but concrete reading payoff.\",\"representative_source_ids\":[\"QP-31effb29\",\"QP-90a375b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7","source_type":"word_analysis","support_id":"sup_78fec2ca9e489910760d","text":"{\"gloss_range\":\"indefinite accusative verbal noun functioning as a cognate accusative that intensifies the single display event\",\"prose\":\"{{ar:عَرْضًا}} ({{tr:ʿarḍan}}) closes the ayah by turning the opening display verb back into a noun of action. As a cognate accusative, it is not a second object and not a new event; it intensifies the one display as a complete displaying. Its indefinite, unmodified form leaves the force qualitative and unbounded, while the root's breadth and presentation field make the final act feel expansive, audience-directed, and formal rather than mechanically repeated. Because it is the last word and a marked gerund return to the display root, the object, day, and recipient class are all enclosed inside a display frame. The heavy final ḍād and tanwīn cadence make the closure audible, answering the prior gathering in 18:99 with a matched move from completed gathering to completed display.\",\"root_display\":\"{{ar:ع ر ض}} ({{tr:ʿ-r-ḍ}})\",\"root_gloss_range\":\"root range of display, presentation, breadth, review, exposure, turning away, and related branches; local maṣdar selects the act of display while breadth and formal-presentation pressure remain secondary\",\"surface_display\":\"{{ar:عَرْضًا}} ({{tr:ʿarḍan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:5:adverse-targeting","source_type":"word_analysis","support_id":"sup_7a1bbb80c957054ccff5","text":"{\"blocking_evidence\":null,\"headline\":\"adversative target, not benefit or possession\",\"reader_payoff\":\"The reader notices that the preposition makes the audience affected by the display, not benefited by it or merely adjacent to it.\",\"reason\":\"The display of Jahannam to the named class selects adverse targeting from the preposition's range.\",\"representative_source_ids\":[\"QG-3ec8f110\",\"MG-22d0b6c5\",\"QS-eca149ef\",\"QY-5b06a035\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:complete-display-frame","source_type":"word_analysis","support_id":"sup_7bb6b93caff7dd5990ee","text":"{\"blocking_evidence\":null,\"headline\":\"explicit object, target, time, and intensifier frame\",\"reader_payoff\":\"The reader notices that the verb distributes the entire scene into roles: what is displayed, when, to whom, and with what internal emphasis.\",\"reason\":\"Attachment evidence confirms the direct object, temporal adverbial, target phrase, and cognate accusative as distinct dependents of the display event.\",\"representative_source_ids\":[\"QG-263640d1\",\"QG-83282aec\",\"QT-f0e24650\",\"QY-c8e21eef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:surah-local-classification-thread","source_type":"word_analysis","support_id":"sup_80bf6dd50913111c3d4c","text":"{\"blocking_evidence\":null,\"headline\":\"classification thread through the surah\",\"reader_payoff\":\"The reader notices that this class label is part of a larger surah-local classification thread, including the shift from fire for wrongdoers in 18:29 to Jahannam for deniers here and in 18:102.\",\"reason\":\"The rows cite concrete same-surah references and distributional links that are compatible with the local target phrase.\",\"representative_source_ids\":[\"QI-7bbed46d\",\"QI-9699eb69\",\"QI-c23c63c8\",\"MI-6ccfa6f9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:closure-weight-and-cadence","source_type":"word_analysis","support_id":"sup_831810f8afe033e645f9","text":"{\"blocking_evidence\":null,\"headline\":\"heavy final sound and matched boundary cadence\",\"reader_payoff\":\"The reader notices that the final display lands with audible weight and answers the prior ayah's gathered ending in 18:99.\",\"reason\":\"The sound and boundary rows are tied to the final cognate noun and to the concrete 18:99 to 18:100 transition.\",\"representative_source_ids\":[\"ME-6eb9ca9d\",\"QP-375b4a75\",\"QP-b8a70457\",\"QB-9f417cc9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:100:4:3","source_type":"qac_morpheme","support_id":"sup_880802722cb39ad2bddc","text":"{\"lemma_ar\":\"كَٰفِرُون\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|LEM:ka`firuwn|ROOT:kfr|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"18:100:4:3\",\"qac_word_ref\":\"18:100:4\",\"root_ar\":\"ك ف ر\",\"surface_ar\":\"كَٰفِرِينَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4:structural-acoustic-pivot","source_type":"word_analysis","support_id":"sup_9512c8cb783b9bc57bf2","text":"{\"blocking_evidence\":null,\"headline\":\"single-word pivot between object and recipients\",\"reader_payoff\":\"The reader notices that the temporal word creates a hinge: the displayed object is named, then the day is fixed, then the recipients are named.\",\"reason\":\"The word stands between the displayed object and recipient phrase, and its internal stop-like sound reinforces that pivot.\",\"representative_source_ids\":[\"QT-8abe0f2a\",\"QT-abbfb3e9\",\"QP-d12b4ba4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:1:boundary-continuation","source_type":"word_analysis","support_id":"sup_964c33044ee66522fdb3","text":"{\"blocking_evidence\":null,\"headline\":\"continuation that launches a new display scene\",\"reader_payoff\":\"The reader notices that the ayah is neither detached from 18:99 nor merely appended to it; the particle carries gathering into display while opening a fresh scene.\",\"reason\":\"QAC allows the conjunction to work as coordination or resumption, and the boundary evidence makes both values locally useful after the prior gathering scene.\",\"representative_source_ids\":[\"QG-3879c527\",\"QG-c5967201\",\"MG-fefa793b\",\"QS-2920094f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2","source_type":"word_analysis","support_id":"sup_98a8fb505ec844e980d7","text":"{\"gloss_range\":\"perfect first-person plural verb of deliberate display or presentation, with explicit object, time, target, and final cognate reinforcement\",\"prose\":\"{{ar:عَرَضْنَا}} ({{tr:ʿaraḍnā}}) is the act that organizes the whole clause. It names a deliberate divine display, not an accidental occurrence or negotiable offer: the object is overt, the audience is routed through a target phrase, the time is inserted between them, and the final cognate noun returns to the same root as a closing frame. The perfect first-person form also reclaims agency after the passive trumpet scene of 18:99, so the display is presented as a settled act; the prior gathering supplies the audience for this focused visual exposure. The wider root range adds exposure, breadth, and a reversal of covering, but the local Form I frame keeps direct manifestation as the selected sense. The same-surah echo sharpens the reversal: humans are displayed before the Lord in 18:48, while here Jahannam is displayed before the deniers.\",\"root_display\":\"{{ar:ع ر ض}} ({{tr:ʿ-r-ḍ}})\",\"root_gloss_range\":\"broad root range of display, presentation, breadth, exposure, turning away, obstruction, occurrence, and honor; local Form I transitive grammar selects deliberate display while allowing exposure and breadth pressure\",\"surface_display\":\"{{ar:عَرَضْنَا}} ({{tr:ʿaraḍnā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:foreign-name-inside-arabic-frame","source_type":"word_analysis","support_id":"sup_a147f2c2421c41f7cf13","text":"{\"blocking_evidence\":null,\"headline\":\"foreign proper name absorbed into Arabic governance\",\"reader_payoff\":\"The reader notices the tension between otherness and integration: a foreign-marked name is governed by the Arabic display verb and case frame.\",\"reason\":\"The bundle marks the word as a FOREIGN proper noun while also showing its Arabic syntactic role as the direct object.\",\"representative_source_ids\":[\"QS-a907b1ed\",\"MS-e0501b24\",\"QI-9e49eb90\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:denial-over-ingratitude","source_type":"word_analysis","support_id":"sup_a6bf1247ab25825625d0","text":"{\"blocking_evidence\":null,\"headline\":\"denial and concealment prioritized over mere ingratitude\",\"reader_payoff\":\"The reader notices that the display context sharpens the participle toward denial and concealment, while ingratitude remains part of the broader root range.\",\"reason\":\"The wider root supports ingratitude and expiation branches, but the adverse display of Jahannam makes denial or concealment the locally stronger reading.\",\"representative_source_ids\":[\"QS-3e14f238\",\"QS-42b4c317\",\"QS-6ccff066\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:closing-display-ring","source_type":"word_analysis","support_id":"sup_ae0646803c5f8e5ab7b1","text":"{\"blocking_evidence\":null,\"headline\":\"final root return frames the whole ayah\",\"reader_payoff\":\"The reader notices that the ayah begins with display and ends by naming the display, enclosing Jahannam, the day, and the recipients inside one frame.\",\"reason\":\"The repeated root occupies the predicate opening and final word, while the final word is syntactically dependent on the opening verb.\",\"representative_source_ids\":[\"QT-3bb5b422\",\"MT-1607f8be\",\"QE-ae1e5232\",\"QY-8e1e2eeb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:indefinite-unbounded-quality","source_type":"word_analysis","support_id":"sup_ba3f48ebc3060ede955f","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite display of unstated extent\",\"reader_payoff\":\"The reader notices that the final noun leaves the display's extent qualitative and unbounded while the recipient class is definite.\",\"reason\":\"The word is indefinite, accusative, and unmodified, so it magnifies the action by quality rather than by specifying kind, number, or measure.\",\"representative_source_ids\":[\"QG-bcad58e9\",\"QG-c5f20008\",\"QF-d281fc2b\",\"QF-d8632f9d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:1:perfect-scene-register","source_type":"word_analysis","support_id":"sup_c12df497a568696ff887","text":"{\"blocking_evidence\":null,\"headline\":\"boundary into an accomplished-future register\",\"reader_payoff\":\"The reader notices that the opening particle carries directly into a perfect verb, making the coming judgment scene sound settled rather than tentative.\",\"reason\":\"The tense belongs to the following verb rather than to the particle itself, so the payoff is narrowed to the particle-plus-perfect launch pattern.\",\"representative_source_ids\":[\"MT-c6d86049\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:5:fused-target-class-form","source_type":"word_analysis","support_id":"sup_d6b476c3ffa2a41c665e","text":"{\"blocking_evidence\":null,\"headline\":\"fused preposition and article compact the target relation\",\"reader_payoff\":\"The reader notices that one bound letter carries a full participant relation and fuses that relation to the definite class name.\",\"reason\":\"The preposition governs the genitive recipient phrase and is fused with the following article in the surface form.\",\"representative_source_ids\":[\"QF-6a6c711d\",\"QF-6ba0018c\",\"QF-98b7bf41\",\"QP-7b028c0e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4:same-surah-temporal-spine","source_type":"word_analysis","support_id":"sup_de9e81cbc5cd75cdd23b","text":"{\"blocking_evidence\":null,\"headline\":\"repeated day-marker locks scenes together\",\"reader_payoff\":\"The reader notices that the time marker repeats from 18:99 and participates in the surah's judgment-day thread through 18:105.\",\"reason\":\"The CRITICAL rows cite concrete same-surah occurrences, and the attachment evidence confirms the current word continues the previous temporal reference.\",\"representative_source_ids\":[\"MI-2a931fe0\",\"QE-7d563d95\",\"QB-421c55d3\",\"QI-4c6db98c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:named-depth-not-generic-fire","source_type":"word_analysis","support_id":"sup_df23070da1bff7bfd3af","text":"{\"blocking_evidence\":null,\"headline\":\"named Jahannam with depth pressure, not generic fire\",\"reader_payoff\":\"The reader notices that the object is a fixed eschatological name with abyss pressure made visible, while the local syntax still keeps it as the displayed proper noun.\",\"reason\":\"The dictionary evidence supports both proper-name and depth associations, but the local object role selects the named eschatological referent rather than a common descriptive abyss term.\",\"representative_source_ids\":[\"QS-43d1e08d\",\"QS-56135daa\",\"QS-b04414df\",\"QY-f0dd8102\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:5","source_type":"word_analysis","support_id":"sup_e1bddeee07116d77e1d3","text":"{\"gloss_range\":\"preposition governing the recipient class as the adverse target of the display, not a loose beneficiary\",\"prose\":\"{{ar:لِ}} ({{tr:li}}) is the small hinge that turns the display toward its affected audience. In this context it is not simple benefit or ownership; Jahannam is displayed to the recipients as an adverse confrontation. Its phrase attaches back to the display verb across the intervening time word, and its fusion with the following article makes target relation and class identity arrive as one compact unit. The same targeting prepares the later local formula in 18:102.\",\"root_display\":\"no root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لِ}} ({{tr:li}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:jahannam-kafir-sequence","source_type":"word_analysis","support_id":"sup_e21867bd9d8455b23246","text":"{\"blocking_evidence\":null,\"headline\":\"recognized Jahannam-denier sequence\",\"reader_payoff\":\"The reader notices that the class named here belongs to a same-surah and Quranic pairing with Jahannam, returning in 18:102 and 18:106.\",\"reason\":\"The contextual profiles and CRITICAL rows support the pairing, and the local prepositional phrase makes the class the display's target.\",\"representative_source_ids\":[\"QI-281ac5e0\",\"MI-2b4cfa32\",\"QE-e2f4b0d7\",\"QB-db6fc68b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:3:surah-local-jahannam-sequence","source_type":"word_analysis","support_id":"sup_e61d2fe33d81b742aa0e","text":"{\"blocking_evidence\":null,\"headline\":\"display begins a local Jahannam sequence\",\"reader_payoff\":\"The reader notices a same-surah progression: Jahannam is displayed in 18:100, prepared for the deniers in 18:102, and named as recompense in 18:106.\",\"reason\":\"The CRITICAL rows provide concrete same-surah references, and the local proper noun matches those later occurrences.\",\"representative_source_ids\":[\"QI-218f11eb\",\"MT-44020207\",\"QE-93a27818\",\"QE-bfc6e217\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:7:marked-nominal-return","source_type":"word_analysis","support_id":"sup_ec79bfa7bd907c3c7935","text":"{\"blocking_evidence\":null,\"headline\":\"minority gerund form makes the return marked\",\"reader_payoff\":\"The reader notices that the closing verbal noun is a marked nominal return to the display root, making the final claim recipient-specific, day-framed, complete, and expansive.\",\"reason\":\"The contextual evidence marks the gerund as a minority form for this root, and the local construction gives it final emphatic force.\",\"representative_source_ids\":[\"QI-a5759c15\",\"QI-ba72e5fe\",\"QI-ce69c1f0\",\"QY-52419f70\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:2:local-root-envelope","source_type":"word_analysis","support_id":"sup_efec43da74cba5d6a6ad","text":"{\"blocking_evidence\":null,\"headline\":\"opening verb anticipates the closing cognate noun\",\"reader_payoff\":\"The reader notices that the verb begins a root frame that the final word closes, so the ayah returns to the act of display at its landing point.\",\"reason\":\"The final cognate accusative shares the same root and is syntactically tied back to this verb.\",\"representative_source_ids\":[\"QE-3f027987\",\"ME-78828f8e\",\"QP-4700fcad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:6:position-and-pronoun-resolution","source_type":"word_analysis","support_id":"sup_fb1a5038f341b04f7eae","text":"{\"blocking_evidence\":null,\"headline\":\"delayed class name resolves the gathered mass\",\"reader_payoff\":\"The reader notices that the named class arrives late, resolves the prior gathered group from 18:99, and stands just before the final display noun lands.\",\"reason\":\"Attachment cross-references support the earlier disbeliever chain, and the word's position after object and time gives the local sequence its narrowing movement.\",\"representative_source_ids\":[\"QT-0139c830\",\"QT-7f218a02\",\"QB-e10a9cae\",\"QB-ee938995\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:4:deictic-ellipsis-compound","source_type":"word_analysis","support_id":"sup_fc6da9c4e1614994c40a","text":"{\"blocking_evidence\":null,\"headline\":\"compressed then-day with recoverable event\",\"reader_payoff\":\"The reader notices that the small compound carries an unstated when-clause and points back to the known event instead of naming a vague time.\",\"reason\":\"The compound contains the deictic then element and tanwīn linked to an elided temporal complement, with 18:99 supplying the discourse anchor.\",\"representative_source_ids\":[\"QG-7d193e13\",\"QG-c0e87433\",\"MG-c6fbff7c\",\"QY-b2e4e95f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:100:1:clitic-verbal-launch","source_type":"word_analysis","support_id":"sup_fe9c1bc2035b5bc0a792","text":"{\"blocking_evidence\":null,\"headline\":\"clitic transition fused to the display verb\",\"reader_payoff\":\"The reader hears the transition and the act arrive in one movement, so the connector immediately becomes a verbal launch.\",\"reason\":\"The conjunction is a proclitic on the following verb, so the formal boundary is compact rather than a separate pause before the act.\",\"representative_source_ids\":[\"QF-27685fb7\",\"QF-94bdc9c1\",\"QY-6c9574b5\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا","ayah_ref":"18:100"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B002","root_001307/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001001","role":"Displaying and bringing something out for sight supplies the explicit unveiling action; the verb and verbal noun make that action emphatic.","root":"ع ر ض","source_ref":"18:100","source_word_indices":["1","5"]},{"branch_id":"B001","mapped_root_id":"root_001307","role":"Covering supplies the recipients' defining image and makes their forced exposure a reversal rather than a neutral viewing.","root":"ك ف ر","source_ref":"18:100","source_word_indices":["4"]}],"changed_reading":{"after":"The showing is a forced uncovering calibrated to people characterized by covering.","before":"Hell is shown to disbelievers."},"confidence":"strong","focus_anchor":"The cognate pair عرضنا ... عرضا at words 1 and 5 presents جهنم specifically to الكافرين at word 4.","mechanism":"The display branch of عرض and the covering branch of كفر form a reversal: the named coverers become recipients of an emphatic making-visible.","model_id":"b1_forced_uncovering"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b1_forced_uncovering","source_type":"hft","support_id":"sup_318377b2b29b948dc703","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا","ayah_ref":"18:100"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B004","root_001307/B003"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001001","role":"Interposition, obstruction, and encounter in a path supply the form-distant image of Hell placed across further escape.","root":"ع ر ض","source_ref":"18:100","source_word_indices":["1","5"]},{"branch_id":"B003","mapped_root_id":"root_001307","role":"Obstruction and denial of truth supply the evasion that the confronting placement ends.","root":"ك ف ر","source_ref":"18:100","source_word_indices":["4"]}],"changed_reading":{"after":"Hell is also a confronting barrier placed before those whose truth-blocking can no longer continue.","before":"Hell is a scene offered to view."},"confidence":"exploratory","focus_anchor":"The repeated عرض construction governs Hell as the object placed before the recipients.","mechanism":"The interception branch of عرض lets confrontation accompany visibility: Hell is set across the route of continued evasion, while كفر as obstruction of truth explains what is being terminated.","model_id":"b2_blocking_confrontation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b2_blocking_confrontation","source_type":"hft","support_id":"sup_f82496056045a990aee9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَعَرَضْنَا جَهَنَّمَ يَوْمَئِذٍۢ لِّلْكَٰفِرِينَ عَرْضًا","ayah_ref":"18:100"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001001/B003","root_001307/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001001","role":"An apparition approaching from a direction, like a cloud, swarm, or mountain filling sight, supplies the scale and frontal arrival.","root":"ع ر ض","source_ref":"18:100","source_word_indices":["1","5"]},{"branch_id":"B002","mapped_root_id":"root_001307","role":"An engulfing cover such as night or a vast sea supplies the field of enclosure against which the apparition becomes overwhelming.","root":"ك ف ر","source_ref":"18:100","source_word_indices":["4"]}],"changed_reading":{"after":"Hell comes on as an overwhelming front that occupies the viewers' horizon.","before":"A bounded object is displayed before an audience."},"confidence":"medium","focus_anchor":"عرضنا ... عرضا can activate the branch of something becoming visible from a direction while still naming an act of display.","mechanism":"The directional apparition branch of عرض and the engulfing-cover branch of كفر turn the scene into a horizon-filling front emerging against an audience habituated to enclosure.","model_id":"b3_horizon_front"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b3_horizon_front","source_type":"hft","support_id":"sup_399d68221f85ed7c82ae","trust":"legacy_unbound"}]}
</lane_packet_json>
