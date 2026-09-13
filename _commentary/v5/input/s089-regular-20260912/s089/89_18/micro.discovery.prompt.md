# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:18**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_18/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:18",
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
{"branch_registry":[{"boundary":"Dal, yürütme ya da sürme hareketini değil, bir kişiyi bir eyleme yöneltmeyi anlatır; bağlam örnekleri ve karşılıklılık çekirdeğe bağlıdır.","branch_kind":"bare","branch_ref":"root_000334/B001","candidate_links":[{"candidate_id":"cand_f354c0f2f89f52911ea7","lane":"micro"},{"candidate_id":"cand_701b35c256c4d6fca187","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","surface_ar":"تَحَٰٓضُّ"}],"gloss":"birini belli bir eyleme ısrarla yöneltme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir katılımcı, başka bir katılımcıyı belli bir işi yapmaya güçlü biçimde yöneltir veya özendirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yöneltme, iyilik yapma veya savaşa katılma gibi belirli eylem alanlarında gerçekleşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karşılıklı biçimlerde katılımcılar aynı yöneltme eylemini birbirlerine uygular."}}],"root_ar":"ح ض ض","root_id":"root_000334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın kişi, hedef eylem ve güçlü yöneltme öğelerini birlikte veren en kısa genel karşılığıdır.","boundary_detail":"Dal, yürütme ya da sürme hareketini değil, bir kişiyi bir eyleme yöneltmeyi anlatır; bağlam örnekleri ve karşılıklılık çekirdeğe bağlıdır.","branch_image_ar":"الحَضّ على الشيء","concept_gloss":"birini belli bir eyleme ısrarla yöneltme","contextual_glosses":[{"applicability":"Katılımcıların aynı eyleme karşılıklı olarak yöneltildiği kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklılığı ve kişilerin birbirini bir eyleme yöneltmesini korur."},"facet_ids":["F003"],"text":"birbirini özendirme","usage_role":"contextual"},{"applicability":"Hedef eylemin savaş olduğu özel bağlamda, yöneltmenin gücünü açıkça verir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yöneltme çekirdeğini ve savaşla sınırlı bağlamsal hedefi birlikte korur."},"facet_ids":["F001","F002"],"text":"savaşa katılmaya güçlü biçimde yöneltme","usage_role":"contextual"}],"definition":"Bir kişiyi belli bir şeyi yapmaya güçlü ve ısrarlı biçimde yöneltmek veya özendirmektir. İyilik ve savaş bunun bağlamsal gerçekleşmeleri, kişilerin birbirini yöneltmesi ise karşılıklı bir uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir katılımcı, başka bir katılımcıyı belli bir işi yapmaya güçlü biçimde yöneltir veya özendirir."},{"facet_id":"F002","role":"specialization","statement":"Yöneltme, iyilik yapma veya savaşa katılma gibi belirli eylem alanlarında gerçekleşebilir."},{"facet_id":"F003","role":"extension","statement":"Karşılıklı biçimlerde katılımcılar aynı yöneltme eylemini birbirlerine uygular."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Hareket ettirme, hayvan gütme veya araç kullanma gibi bu dala ait olmayan eylemleri ekler.","collision":"Türkçede hareket ettirme ve araç kullanma anlamlarıyla doğrudan karışır.","fit":"displacement","loses":"Bir kişiyi belli bir eylemi yapmaya isteyerek ve ısrarla yöneltme çekirdeğini kaybeder.","preserves":"Bir katılımcının başka bir katılımcı üzerinde etkide bulunması gibi çok genel bir ilişkiyi korur."},"text":"sürme"}],"identity_rationale":"Kaynak sözü, birini belli bir şeyi yapmaya yöneltme ve özendirme çekirdeğini açıkça destekler. İyilik ve savaş bu çekirdeğin bağlama bağlı gerçekleşmeleridir; karşılıklı yöneltme ise özel türemiş biçimlerde ortaya çıkar ve dalın temel anlamıyla aynı düzeye çıkarılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"birini bir şeyi yapmaya güçlü biçimde yöneltmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"birini belli bir şeyi yapmaya ısrarla yöneltmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"birbirini bir eyleme yöneltme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"iki kişinin birbirini özendirmesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir eyleme güçlü biçimde yöneltme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ısrarlı özendirme adı veya biçimi"}],"lexicalization_note":"Tanım yalın dalın eyleme yöneltme çekirdeğiyle sınırlıdır; belirli bir bağlama veya özel bir söz öbeğine bağlı anlam genelleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Yalnızca eyleme yöneltme çekirdeğiyle doğrudan karışabilecek üç aday yayımlandı; öteki adaylar ortak bir konu alanı taşımıyor veya yalnızca eş sesli dalları temsil ediyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında belirleyici öğe eyleme yöneltmedir; komşu dal ise bu yöneltmeyi hızlandırma ve acele ettirmeyle birleştirebilir.","focus_only":"Karşılıklı yöneltmeyi adlandıran özel biçimleri de kapsar ve çabuklaştırmayı zorunlu kılmaz.","gloss":"yöneltme ve acele ettirme","neighbor_only":"Yöneltmeye ek olarak işi çabuklaştırma veya kişiyi acele ettirme öğesini kapsar.","neighbor_ref":"root_000293/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişiyi belli bir eylemi yapmaya güçlü biçimde yöneltir."},{"boundary_match":"partial","distinction":"Odak dalı genel güçlü yöneltmeyi anlatırken komşu dal, kişinin duygusal olarak kızıştırılıp eyleme hazırlanmasını daha belirgin kılar.","focus_only":"İyilik dahil farklı hedeflere yönelik nötr veya olumlu özendirmeyi ve karşılıklı yöneltmeyi kapsayabilir.","gloss":"eyleme kızıştırma","neighbor_only":"Kişiyi özellikle savaş gibi bir eylem için kızıştırma ve coşturma yönünü öne çıkarır.","neighbor_ref":"root_000309/B006","relation_type":"near_synonym","shared_zone":"İki dal da başka bir kişiyi bir eyleme yöneltme ve harekete geçirme alanında buluşur."},{"boundary_match":"partial","distinction":"Odak dalı eylemin kendisidir; komşu dal ise bu eylemi belirli bir çalışma ortamında yerine getiren kişiyi gösterir.","focus_only":"Yöneltme eylemini ve bunun karşılıklı biçimlerini adlandırır.","gloss":"işçiyi çalıştırmaya yönelten kişi","neighbor_only":"Bir işçiyi çalışmaya yönelten belirli görevdeki kişiyi adlandırır.","neighbor_ref":"root_001687/B007","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir kişinin başka bir kişiyi çalışmaya veya eyleme yöneltmesi vardır."}],"source_phrase_ar":"حضضته على كذا إذا حضضته عليه وحرضته (maqayis)؛ وقد حض يحض حضا (ayn)؛ حضه على القتال حضا أي حثه وحضضه أي حرضه والتحاض التحاث والمحاضة أن يحث كل واحد منهما صاحبه (sihah)؛ حض يحض حضا وهو الحث على الخير ويقال حضضت القوم على القتال تحضيضا إذا حرضتهم (tahdhib)؛ الحض التحريض كالحث (mufradat)","source_summary":"Kaynaklar, anlamın güçlü biçimde eyleme yöneltme ve özendirme olduğunu ortaklaşa gösterir. İyilik ve savaş bağlamları ile karşılıklı yöneltme biçimleri bu ortak çekirdeğe bağlı olarak verilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الحث والتحريض والحض المتبادل على الخير أو القتال أو طعام المسكين","what_is_not_ar":"ليس السير والسوق عند من فرقه عن الحث؛ وليس قرار الأرض ولا الدواء الحُضُض"},"support_links":["sup_26a54b72ec02ca8c0abd","sup_cb50b040fe06a4b16610"]},{"boundary":"Dal genel bir dayanak yüzeyi değil, dağın eteği veya bitimindeki alçak zemin bölümüdür.","branch_kind":"bare","branch_ref":"root_000334/B002","candidate_links":[{"candidate_id":"cand_fe03da26775d6cb2a540","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","surface_ar":"تَحَٰٓضُّ"}],"gloss":"dağ eteğindeki alçak taban","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çevresindeki yükseltiye göre aşağıda kalan bir zemin veya taban bölümünü gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu alçak bölüm özellikle dağın eteğinde veya dağın sona erdiği yerde konumlanır."}}],"root_ar":"ح ض ض","root_id":"root_000334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağla olan konumu ve çevresine göre alçakta kalan zemin niteliğini birlikte verir.","boundary_detail":"Dal genel bir dayanak yüzeyi değil, dağın eteği veya bitimindeki alçak zemin bölümüdür.","branch_image_ar":"الحَضيض قرار الأرض","concept_gloss":"dağ eteğindeki alçak taban","contextual_glosses":[{"applicability":"Dağın sona erdiği yerin özellikle belirtildiği arazi betimlemelerinde doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dağın bitimindeki konumu ve aşağıda kalan zemin niteliğini korur."},"facet_ids":["F001","F002"],"text":"dağın bittiği yerdeki alçak zemin","usage_role":"contextual"}],"definition":"Dağın eteğinde veya dağın sona erdiği noktada bulunan alçak zemin ya da taban bölümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çevresindeki yükseltiye göre aşağıda kalan bir zemin veya taban bölümünü gösterir."},{"facet_id":"F002","role":"specialization","statement":"Bu alçak bölüm özellikle dağın eteğinde veya dağın sona erdiği yerde konumlanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Herhangi bir nesneyi taşıyan her türlü yüzeyi kapsayan desteksiz bir genellik ekler.","collision":"Gündelik dayanak yüzeyi anlamıyla karışır ve arazi terimi olarak okunmasını engeller.","fit":"displacement","loses":"Dağ eteğindeki veya dağın bittiği yerdeki alçak arazi sınırını kaybeder.","preserves":"Yalnızca genel zemin veya yüzey düşüncesini korur."},"text":"üzerine bir şey konan yüzey"}],"identity_rationale":"Kaynak sözü, dağın eteğinde veya dağın sona erdiği yerde bulunan alçak zemini tutarlı biçimde gösterir. Geçici açıklamadaki herhangi bir nesnenin üzerine konduğu genel yüzey anlamı kaynak sözüyle desteklenmediği için dal korunmuş, fakat tanım bu ek kapsam çıkarılarak yeniden kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dağ eteğinde veya dağın bitiminde bulunan alçak zemin"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dağ eteğinde bulunan taş"}],"lexicalization_note":"Tanım, yalın dalın alçak arazi anlamını verir; taş adı gibi türemiş bir birimin anlamı dalın çekirdeğine katılmaz.","neighbor_coverage_note":"Bütün arazi ve eş seslilik adayları değerlendirildi. Dağın alt bölümü, yükselmiş arazi ve düz arazi sınırı açıklamaya en çok katkı sağladığı için yayımlandı; kalanlar yalnızca uzak arazi öğeleri veya başka anlam dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı aşağıda kalan zemini adlandırır; komşu dal ise dağın kendi alt bölümünü ve bazı ek arazi öğelerini daha geniş biçimde kapsar.","focus_only":"Dağın eteğinde veya bitiminde bulunan alçak zemin bölümünü öne çıkarır.","gloss":"dağın alt bölümü ve eteği","neighbor_only":"Dağın alt kısmını, kökünü veya yamacını ve aşağı sürüklenen çamuru da kapsayabilir.","neighbor_ref":"root_000235/B014","relation_type":"near_synonym","shared_zone":"Her iki dal da dağın aşağıdaki son bölümü veya eteğiyle ilişkilidir."},{"boundary_match":"opposed","distinction":"Odak dalı yükseklik ekseninin aşağı ucundaki tabanı, komşu dal ise aynı eksenin yukarı ucundaki yükseltiyi gösterir.","focus_only":"Dağ eteğinde veya bitiminde aşağıda kalan zemin bölümünü gösterir.","gloss":"yükselmiş arazi","neighbor_only":"Çevresine göre yükselmiş toprak veya arazi bölümünü gösterir.","neighbor_ref":"root_000537/B002","relation_type":"polarity_pair","shared_zone":"İki dal da bir arazi bölümünü çevresine göre düşey konumuyla tanımlar."},{"boundary_match":"partial","distinction":"Odak dalını belirleyen şey dağın alt sınırındaki konumdur; komşu dalda belirleyici özellik arazinin düz ve engebesiz olmasıdır.","focus_only":"Dağ eteği veya dağın bitimiyle zorunlu bir konum ilişkisi taşır.","gloss":"düz ve kolay geçilir arazi","neighbor_only":"Engebeli olmayan geniş ve kolay geçilir araziyi, dağ eteği şartı olmadan anlatır.","neighbor_ref":"root_000753/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da yükseltiden ayrılan daha alçak ve düz arazi tasarımında buluşabilir."}],"source_phrase_ar":"الحضيض وهو قرار الأرض (maqayis)؛ الحضيض قرار الأرض عند سفح الجبل (ayn;tahdhib)؛ الحضيض القرار من الأرض عند منقطع الجبل ويعني بالأرض (sihah)؛ الحضيض وهو قرار الأرض (mufradat)","source_summary":"Kaynaklar, anlamı dağın eteğindeki veya bitimindeki alçak zemin olarak ortaklaşa tanımlar. Bu tanım, herhangi bir nesneyi taşıyan genel yüzey anlamına genişletilemez.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"قرار الأرض عند سفح الجبل أو منقطع الجبل والأرض التي يوضع عليها الشيء","what_is_not_ar":"ليس الحث والتحريض؛ وليس الدواء الحُضُض"},"support_links":["sup_2e1fcc8a54c16e397523"]},{"boundary":"Dal bilinen acı sağaltım maddesini gösterir; maddeyi yalnızca tek bir reçineye veya yalnızca tek bir hazırlama yöntemine indirgemek desteklenmez.","branch_kind":"bare","branch_ref":"root_000334/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","surface_ar":"تَحَٰٓضُّ"}],"gloss":"yapısı farklı aktarılan acı reçinemsi sağaltım maddesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilinen bir sağaltım maddesidir ve acı, reçinemsi bir madde olarak betimlenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarım çizgisi, maddenin deve idrarından hazırlandığını bildirerek reçinemsi madde betimlemesinden farklı bir bileşim sunar."}}],"root_ar":"ح ض ض","root_id":"root_000334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddenin sağaltım işlevini, acılığını, reçinemsi betimini ve bileşimine ilişkin aktarım farkını birlikte korur.","boundary_detail":"Dal bilinen acı sağaltım maddesini gösterir; maddeyi yalnızca tek bir reçineye veya yalnızca tek bir hazırlama yöntemine indirgemek desteklenmez.","branch_image_ar":"الحُضُض دواء مر","concept_gloss":"yapısı farklı aktarılan acı reçinemsi sağaltım maddesi","contextual_glosses":[{"applicability":"Maddenin görünüşü ve sağaltım amacı öne çıktığında doğal, fakat kaynak farkını özetleyen dar bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve idrarından hazırlanmış olabileceğini bildiren farklı aktarımı dışarıda bırakır.","preserves":"Acı, reçinemsi ve sağaltım amaçlı bir madde olmasını korur."},"facet_ids":["F001"],"text":"acı reçinemsi ilaç","usage_role":"contextual"}],"definition":"Acı reçineye benzeyen bilinen bir sağaltım maddesidir. Bazı aktarımlarda deve idrarından hazırlandığı söylendiğinden, bileşimi tek bir madde veya yöntem olarak kesinleştirilmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilinen bir sağaltım maddesidir ve acı, reçinemsi bir madde olarak betimlenir."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarım çizgisi, maddenin deve idrarından hazırlandığını bildirerek reçinemsi madde betimlemesinden farklı bir bileşim sunar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnızca benzetme için kullanılan başka bir maddenin kendisiyle kesin özdeşlik ekler.","collision":"Komşu acı bitki özü adıyla doğrudan karışır.","fit":"displacement","loses":"Ayrı bir madde adı olmasını ve bileşimine ilişkin farklı aktarımı kaybeder.","preserves":"Acı ve sağaltım amacıyla kullanılan bitkisel salgı çağrışımını korur."},"text":"sarısabır özü"}],"identity_rationale":"Kaynak sözü, bilinen acı bir sağaltım maddesi kimliğinde birleşir, ancak maddenin yapısını bir yanda acı reçineye benzer bir salgı, öte yanda deve idrarından hazırlanan bir ürün olarak aktarır. Dal korunabilir, fakat tanım bu bileşim farkını kesin bir özdeşlik kurmadan açıkça göstermelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"acı reçineye benzetilen bilinen sağaltım maddesi"}],"lexicalization_note":"Tanım yalın dalın sağaltım maddesi anlamıyla sınırlıdır ve komşu bitki, reçine veya ilaç adlarını onunla özdeşleştirmez.","neighbor_coverage_note":"Bütün madde ve bitki adayları değerlendirildi. Acı bitki özü en yakın karışma noktasını, tatlı ağaç salgısı malzeme karşıtlığını ve sağaltım odunu yalnızca ortak kullanım alanını gösterir; kalan adaylar daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı komşu maddeye benzetilir, fakat onunla özdeş değildir; ayrıca hazırlama biçimine ilişkin ayrı bir aktarım taşır.","focus_only":"Ayrı bir sağaltım maddesini ve onun bileşimine ilişkin farklı aktarımı kapsar.","gloss":"acı bitki özü","neighbor_only":"Belirli bir acı bitkinin özsuyunu veya ondan elde edilen maddeyi gösterir.","neighbor_ref":"root_000840/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da acı, reçinemsi görünebilen ve sağaltımda kullanılan bir maddeyi gösterir."},{"boundary_match":"partial","distinction":"Odak madde acı ve sağaltım amaçlıdır; komşu madde ise ağaç kökeni ve tatlılığıyla ayrılır.","focus_only":"Acı oluşu ve sağaltım maddesi olarak tanınması belirleyicidir.","gloss":"ağaçtan çıkan tatlı sakızımsı salgı","neighbor_only":"Çeşitli ağaçlardan toplanan tatlı, sakızımsı salgıları gösterir.","neighbor_ref":"root_001096/B007","relation_type":"near_neighbor","shared_zone":"İki dal da salgı veya reçineyi andıran yoğun bir maddeyi gösterebilir."},{"boundary_match":"field_only","distinction":"Ortaklık yalnızca kullanım alanındadır; odak dalın acı reçinemsi maddesi ile komşunun kokulu odun ürünü farklı nesne türleridir.","focus_only":"Acı ve reçinemsi bir sağaltım maddesini gösterir.","gloss":"tütsü ve sağaltım odunu","neighbor_only":"Tütsüde ve sağaltımda kullanılan kokulu bir odun veya bitkisel ürünü gösterir.","neighbor_ref":"root_001224/B006","relation_type":"same_field","shared_zone":"Her iki dal da geleneksel sağaltımda kullanılan bir maddeyi adlandırır."}],"source_phrase_ar":"الحضض دواء يتخذ من أبوال الإبل (ayn;tahdhib)؛ الحُضُض والحُضَض دواء معروف وهو صمغ مر كالصبر (sihah)؛ الحُضُض والحُضَض صمغ من نحو الصبر والمر (tahdhib)","source_summary":"Aktarımlar bunun bilinen acı bir sağaltım maddesi olduğunda birleşir, fakat maddi yapısını aynı biçimde açıklamaz. Bir anlatım acı reçine benzeri bir salgıyı, başka bir anlatım deve idrarından hazırlanmayı öne çıkarır.","sources":["AY","SI","TA"],"what_is_ar":"الدواء المعروف الحُضُض أو الحُضَض وصمغه المر وما قيل فيه من اتخاذه من أبوال الإبل","what_is_not_ar":"ليس الحث والتحريض ولا الحضيض قرار الأرض؛ ولا تجعل روايات الظاء فرعا مستقلا هنا"},"support_links":[]},{"boundary":"Anlam yalnızca kişinin bir başkası için kendinden daha fazlasını istediği özel ifadeye aittir; genel isteme veya genel artış anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000334/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","surface_ar":"تَحَٰٓضُّ"}],"gloss":"bir kimse için kendinden daha fazlasını isteme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, daha fazlasını dışarıdaki bir nesneden değil kendi benliğinden veya çabasından ister."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kendinden daha fazlasını isteme, belirli bir başka kimse yararına veya onunla ilişkili olarak gerçekleşir."}}],"root_ar":"ح ض ض","root_id":"root_000334","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel ifadenin öz-yönelimini, artış isteğini ve bu isteğin bağlı olduğu kişiyi birlikte verir.","boundary_detail":"Anlam yalnızca kişinin bir başkası için kendinden daha fazlasını istediği özel ifadeye aittir; genel isteme veya genel artış anlamı değildir.","branch_image_ar":"استزادة النفس","concept_gloss":"bir kimse için kendinden daha fazlasını isteme","contextual_glosses":[{"applicability":"Konuşanın kendi çabasını artırmak istediği ve ilgili kişinin bağlamdan belli olduğu durumda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşanın kendine yönelişini, daha fazlasını istemesini ve yararlanıcı kişiyi korur."},"facet_ids":["F001","F002"],"text":"onun için kendimden daha fazlasını isteme","usage_role":"contextual"}],"definition":"Belirli bir kimse için kişinin kendinden, kendi gücünden veya çabasından daha fazlasını istemesini anlatan özel ifadedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, daha fazlasını dışarıdaki bir nesneden değil kendi benliğinden veya çabasından ister."},{"facet_id":"F002","role":"specialization","statement":"Kendinden daha fazlasını isteme, belirli bir başka kimse yararına veya onunla ilişkili olarak gerçekleşir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Her türlü niceliksel artışı ve dışarıdaki bir nesneyi artırmayı kapsayan genel bir anlam ekler.","collision":"Genel nicelik değişimiyle karışarak özel ifadenin katılımcı yapısını görünmez kılar.","fit":"displacement","loses":"İsteğin kişinin kendisine yönelmesini ve belirli bir kimse için gerçekleşmesini kaybeder.","preserves":"Bir miktarın veya çabanın daha çok olması yönündeki genel değişimi korur."},"text":"artırmak"}],"identity_rationale":"Kaynak sözü, kişinin belirli bir kimse için kendi benliğinden veya çabasından daha fazlasını istemesini anlatan özel ifadeyi doğrudan destekler. Geçici çerçeve bu öz-yönelimli artış isteğini doğru verir ve başka dalların anlamlarını buna katmaz.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir kimse için kendinden daha fazlasını istemek"}],"lexicalization_note":"Tanım yalnızca verilen sabit ifadeye bağlıdır; buradan yalın köke genel bir kendini artırma veya daha çok isteme anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel isteme, nicelik artışı ve benliğin işe yatkınlaşması özel ifadenin sınırını en iyi açıklar; öteki adaylar katılımcı yapısı bakımından daha uzak veya yalnızca eş seslidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal özel olarak kişinin kendinden daha fazlasını istemesidir; komşu dalda istenen şey dışsal olabilir ve öz-yönelim şart değildir.","focus_only":"İsteği kişinin kendi benliğine veya çabasına yöneltir ve belirli bir kimseye bağlar.","gloss":"bir şeyi arama ve isteme","neighbor_only":"Bir şeyi, gereksinimi veya amacı genel olarak aramayı ve başkası için istemeyi kapsar.","neighbor_ref":"root_000138/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da henüz elde olmayan daha çok şeyi isteme veya arama yönelimi bulunur."},{"boundary_match":"partial","distinction":"Odak dal bir kişinin kendisine yönelttiği isteği anlatır; komşu dal ise herhangi bir miktarın nesnel olarak artmasını gösterir.","focus_only":"Kişinin kendinden daha fazlasını istemesini ve bunu belirli biriyle ilişkilendirmesini anlatır.","gloss":"ölçünün üzerine çıkma","neighbor_only":"Sayı, verme veya söz miktarının ölçü bakımından çoğalmasını genel olarak anlatır.","neighbor_ref":"root_000558/B005","relation_type":"near_neighbor","shared_zone":"İki dal da başlangıçtaki düzeyin üstüne çıkma düşüncesini içerir."},{"boundary_match":"partial","distinction":"Odak dalda kişi kendinden daha fazlasını ister; komşu dalda benlik işi kolaylaştırır, benimser veya kişiyi ona hazırlar.","focus_only":"Kişinin belirli biri için kendinden daha fazla çaba istemesini gösterir.","gloss":"kendini bir işe yatkın kılma","neighbor_only":"Kişinin kendi benliğinin bir işi kolay, kabul edilebilir veya yapılabilir göstermesini anlatır.","neighbor_ref":"root_000956/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendi benliği eyleme ilişkin içsel bir yönelimin tarafıdır."}],"source_phrase_ar":"احتضضت نفسي لفلان وابتضضتها إذا استزدتها (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, ifadeyi kişinin belirli bir kimse için kendinden daha fazlasını istemesi olarak açıklar."}],"source_summary":"Kanıt yalnızca öz-yönelimli ve belirli bir kimseye bağlı bu özel ifadeyi gösterir; anlam yalın köke veya genel artış bildiren bütün kullanımlara taşınamaz.","sources":["TA"],"what_is_ar":"قول احتضضت نفسي لفلان بمعنى استزدتها وما قاربه في هذا التعبير","what_is_not_ar":"ليس الحث والتحريض؛ وليس الحضيض قرار الأرض؛ وليس الدواء الحُضُض"},"support_links":[]},{"boundary":"Bu dal yerleşme, ev halkı, yoksulluk ya da araç adlarını değil, hareketten sonra durma ve dinginleşmeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B001","candidate_links":[{"candidate_id":"cand_fe03da26775d6cb2a540","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"hareketin dinip durulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceden hareket eden veya çalkalanan şeyin hareketi sona erer."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hareketin bitmesiyle şey durur, yerinde kalır veya dingin bir duruma geçer."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Susma ile rüzgarın, yağmurun ve öfkenin dinmesi aynı değişimin bağlama bağlı kullanımlarıdır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki hareketin veya çalkantının sona erip ardından durma ve dinginlik oluştuğu genel çekirdeği karşılar.","boundary_detail":"Bu dal yerleşme, ev halkı, yoksulluk ya da araç adlarını değil, hareketten sonra durma ve dinginleşmeyi anlatır.","branch_image_ar":"ذهاب الحركة","concept_gloss":"hareketin dinip durulması","contextual_glosses":[{"applicability":"Rüzgar, yağmur veya öfke gibi hareketli ya da şiddetli bir durumun yatıştığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir hareket veya şiddet durumunun sona ererek yatışmasını korur."},"facet_ids":["F001","F002","F003"],"text":"dindi","usage_role":"contextual"},{"applicability":"Çalkantıdan sonra dengeli ve dingin duruma geçişin öne çıktığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çalkantının bitmesini ve ardından dengeli bir durum oluşmasını korur."},"facet_ids":["F001","F002"],"text":"duruldu","usage_role":"contextual"}],"definition":"Bir şeyin hareketi veya çalkantısı sona ererek durması, yerinde kalması ya da dinginleşmesidir. Susma ile rüzgarın, yağmurun ve öfkenin dinmesi bu değişimin belirli bağlamlardaki görünüşleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceden hareket eden veya çalkalanan şeyin hareketi sona erer."},{"facet_id":"F002","role":"core","statement":"Hareketin bitmesiyle şey durur, yerinde kalır veya dingin bir duruma geçer."},{"facet_id":"F003","role":"associated_use","statement":"Susma ile rüzgarın, yağmurun ve öfkenin dinmesi aynı değişimin bağlama bağlı kullanımlarıdır."}],"identity_rationale":"Kaynak sözü, önceki hareketin ya da çalkantının sona ermesini ve şeyin ardından durup dengelenmesini açıkça temel anlam olarak verir. Susma ile rüzgar, yağmur ve öfkenin dinmesi bu çekirdeğin bağlama bağlı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"hareketin sona erip şeyin durması"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"hareketi veya çalkantısı dindi ve durdu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"rüzgar, yağmur ya da öfke dindi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hareketsiz, yerinde duran veya dingin"}],"lexicalization_note":"Tanım yalın durma çekirdeğini korur; rüzgar, yağmur ve öfke kullanımlarını yalnızca belirli bağlamlara bağlı uzantılar olarak ayırır.","neighbor_coverage_note":"Verilen bütün komşu kartları değerlendirildi. En keskin eşdeğerlik, yakınlık ve karşıtlık bu üçünde bulundu; öteki kartlar ayrı kök dallarına, özel araçlara veya uzak bağlamlara aittir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Komşu karttaki su, rüzgar, gemi ve topluluk örnekleri sınırı değiştirmez; bunlar aynı durma ve dinginleşme çekirdeğinin örnekleridir.","focus_only":null,"gloss":"hareketten sonra durma ve dinginleşme","neighbor_only":null,"neighbor_ref":"root_000590/B001","relation_type":"synonym","shared_zone":"İki dal da hareket veya çalkantıdan sonra durmayı, yerinde kalmayı ve dinginleşmeyi aynı çekirdekte toplar."},{"boundary_match":"partial","distinction":"Odak dal bir durum değişimini, komşu dal ise bunun yanında yumuşak ve kaygısız oluş biçimini anlatır; bu yüzden her bağlamda birbirlerinin yerine geçmezler.","focus_only":"Odak dal, önceki hareketin veya çalkantının sona ermesini gerekli başlangıç noktası yapar.","gloss":"dingin durma ile yumuşaklık","neighbor_only":"Komşu dal yumuşaklık, kolaylık ve sertlikten uzak davranış biçimini de kapsar.","neighbor_ref":"root_000608/B001","relation_type":"near_synonym","shared_zone":"Her ikisi de çalkantısız, dingin ve zorlamasız bir durumu anlatabilir."},{"boundary_match":"opposed","distinction":"Odakta hareket sona erip denge oluşurken komşuda güçlü hareket ve dengesizlik belirginleşir; ortak eksende ters yönleri gösterirler.","focus_only":"Odak dal hareketin ve çalkantının biterek durulmasını anlatır.","gloss":"durulma ile şiddetli çalkantı","neighbor_only":"Komşu dal güçlü sarsıntı ve yoğun çalkantının sürmesini anlatır.","neighbor_ref":"root_000545/B001","relation_type":"antonym","shared_zone":"İki dal da bir şeyin hareket ve denge durumunu aynı eksende değerlendirir."}],"source_phrase_ar":"خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك","source_summary":"Kaynakların ortak çizgisi, hareket veya çalkantıdan sonra gelen durma, yerinde kalma ve dinginleşmedir; sessizlik ve doğa olaylarının ya da öfkenin yatışması da bu çizgide ele alınır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكون بعد الحركة والاستقرار والثبوت والهدوء والسكوت وسكون الريح والمطر والغضب","what_is_not_ar":"ليس السكنى ولا المسكنة ولا أسماء الآلة"},"support_links":["sup_2e1fcc8a54c16e397523"]},{"boundary":"Burada odak, yerleşme eylemi ve yaşanan yerdir; orada yaşayan kişiler ya da iç dinginlik bu dala girmez.","branch_kind":"bare","branch_ref":"root_000726/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"bir yere yerleşip orada yaşama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir yere yerleşir ve orada yaşamını sürdürür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yerleşilip yaşanan ev veya yer, bu eylemin yer adı olarak anlatılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birini bir yerde oturtma ve evi kira almadan kullanımına verme de bu alanın ettirgen ve hukuki uzantılarıdır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın eylem çekirdeğini, yani bir yeri sürekli veya yerleşik biçimde yaşanan yer edinmeyi karşılar.","boundary_detail":"Burada odak, yerleşme eylemi ve yaşanan yerdir; orada yaşayan kişiler ya da iç dinginlik bu dala girmez.","branch_image_ar":"استيطان المنزل","concept_gloss":"bir yere yerleşip orada yaşama","contextual_glosses":[{"applicability":"Eylemden çok kişinin yerleşip yaşadığı evin veya yerin kendisi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşilip yaşanan yer olma niteliğini korur."},"facet_ids":["F002"],"text":"konut","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini belirli bir evde veya yerde oturur duruma getirdiği ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başkasını bir yerde oturur ve yaşar duruma getirme işlemini korur."},"facet_ids":["F003"],"text":"yerleştirdi","usage_role":"contextual"}],"definition":"Bir yere yerleşip orada yaşama ve o yeri yaşanan yer edinmedir. Aynı alan, yaşanan yerin kendisini, birini oraya yerleştirmeyi ve bir evi kira almadan kullanımına vermeyi de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir yere yerleşir ve orada yaşamını sürdürür."},{"facet_id":"F002","role":"extension","statement":"Yerleşilip yaşanan ev veya yer, bu eylemin yer adı olarak anlatılır."},{"facet_id":"F003","role":"extension","statement":"Birini bir yerde oturtma ve evi kira almadan kullanımına verme de bu alanın ettirgen ve hukuki uzantılarıdır."}],"identity_rationale":"Kaynak sözü bir yerde yerleşip yaşamayı, yaşanan yeri, birini orada oturtmayı ve bir evi karşılıksız kullanıma bırakmayı birlikte bildirir. Dal çerçevesi bunları yerleşme ve konut ekseninde doğru biçimde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir yere yerleşip orada yaşadı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"konut, ev veya yaşanan yer"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir evi kira almadan oturması için verme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onu bir evde veya yerde oturttu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"konut olarak kullanılan ev veya yer"}],"lexicalization_note":"Tanım yalın yerleşip yaşama anlamını temel alır; konut, birini oturtma ve karşılıksız kullanım verme biçimlerini aynı söz ailesinin açık uzantıları olarak gösterir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilen üç komşu yerleşme, barınak ve sabit konum sınırlarını doğrudan aydınlatır; kalanlar dönemlik kalış, çadır, eşya veya uzak kök dallarıyla sınırlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaşama yerini yerleşme eylemiyle birlikte kurar; komşu dalın çekirdeği ise gecelemeye veya barınmaya yarayan yerin kendisidir.","focus_only":"Odak dal yerleşip yaşama eylemini, birini yerleştirmeyi ve karşılıksız kullanım vermeyi de içerir.","gloss":"yerleşip yaşama ile barınak","neighbor_only":"Komşu dal geceleme ve sığınma yerlerini, çadırı ve saray gibi farklı barınak adlarını da kapsar.","neighbor_ref":"root_000166/B001","relation_type":"near_synonym","shared_zone":"İki dal da insanın yaşadığı evi veya barındığı yeri gösterebilir."},{"boundary_match":"partial","distinction":"Odakta yerleşip yaşama ve konutlaşma belirgindir; komşuda yer seçme ve hazırlama işlemi ile hayvan barınağına uzanan daha geniş bir alan vardır.","focus_only":"Odak dal yerleşik yaşamı, konutu ve bir başkasını orada oturtmayı kapsar.","gloss":"yerleşme ile konak yeri edinme","neighbor_only":"Komşu dal insan veya hayvan için konak yeri seçme, hazırlama ve elverişli ya da elverişsiz çevre niteliğini kapsar.","neighbor_ref":"root_000162/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir yeri kalınacak veya yaşanacak yer olarak edinme vardır."},{"boundary_match":"partial","distinction":"Odak gündelik yerleşme ve konut alanıdır; komşu ise belirli kalıplara, özel bir yer adına ve başın boyundaki oturma noktasına bağlıdır.","focus_only":"Odak dal genel yerleşme eylemini ve yaşanan yeri anlatır.","gloss":"konut ile sabit konum","neighbor_only":"Komşu dal kalıplaşmış çoğul kullanımlarda konumları, düzeyleri veya alışılmış düzeni ve ayrıca bedensel bir yerleşme noktasını anlatır.","neighbor_ref":"root_000726/B009","relation_type":"near_neighbor","shared_zone":"İki dal da bir varlığın bulunduğu veya yerleştiği yeri gösterebilir."}],"source_phrase_ar":"يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن","source_summary":"Kaynaklar yerleşip yaşama eylemini, yaşanan ev veya yeri, bir başkasını oraya yerleştirmeyi ve bir evi kira karşılığı olmadan kullanımına bırakmayı aynı anlam alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سكن المكان والمسكن والمنزل والبيت والمساكن والسكنى والإسكان وإعارة المنزل بلا كراء","what_is_not_ar":"ليس أهل الدار أنفسهم ولا السكينة القلبية"},"support_links":[]},{"boundary":"Dal, evin kendisini değil evde yaşayanları ve ev halkını anlatır; genel akrabalık veya her tür topluluk bağı daha geniştir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"ev halkı ve orada yaşayanlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, evin kendisine değil o evde yaşayan kişilere yönelir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı evin halkı ve bakmakla yükümlü olunan aile üyeleri bu grubun belirgin özel alanıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çoğul kullanım, bir evde veya başka bir yerde oturanların tümüne genişleyebilir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Evde yaşayan topluluğu hem aile halkı hem de daha genel oturanlar yönüyle karşılar.","boundary_detail":"Dal, evin kendisini değil evde yaşayanları ve ev halkını anlatır; genel akrabalık veya her tür topluluk bağı daha geniştir.","branch_image_ar":"أهل الدار","concept_gloss":"ev halkı ve orada yaşayanlar","contextual_glosses":[{"applicability":"Aynı evde yaşayan aile ve bakmakla yükümlü olunan kişiler özellikle kastedildiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aynı evde yaşayan aile topluluğunu ve yakın ev bağını korur."},"facet_ids":["F001","F002"],"text":"ev halkı","usage_role":"contextual"},{"applicability":"Aile bağı aranmadan belirli bir evde veya yerde oturanların tümü kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli yerde oturan kişiler topluluğunu aile bağı eklemeden korur."},"facet_ids":["F001","F003"],"text":"orada yaşayanlar","usage_role":"contextual"}],"definition":"Bir evde yaşayan kişiler, özellikle aynı evin halkı ve aile yükümlülüğü içinde bulunan kimselerdir. Daha genel çoğul kullanım, belirli bir yerde oturanların tümünü gösterebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, evin kendisine değil o evde yaşayan kişilere yönelir."},{"facet_id":"F002","role":"specialization","statement":"Aynı evin halkı ve bakmakla yükümlü olunan aile üyeleri bu grubun belirgin özel alanıdır."},{"facet_id":"F003","role":"extension","statement":"Çoğul kullanım, bir evde veya başka bir yerde oturanların tümüne genişleyebilir."}],"identity_rationale":"Kaynak sözü evde yaşayanları, ev halkını ve bakmakla yükümlü olunan aile üyelerini açıkça dalın gönderimi yapar. Çerçeve, evi ya da yerleşme eylemini değil o yerde yaşayan insan topluluğunu doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"ev halkı ve aile üyeleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir yerde yaşayanlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar"}],"lexicalization_note":"Tanım ev halkını yalın çekirdek olarak verir; çoğul sakinler ve evde yaşayanları belirten kalıp kullanımı bu çekirdeğin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Tüm komşular değerlendirildi. Seçilenler ev halkı, daha geniş bağlı topluluk ve fiziksel konut arasındaki temel karışmaları gösterir; diğer adaylar tek kişi, eşlik veya uzak yan dallardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta belirleyici bağ fiilen evde yaşamaktır; komşuda aileye veya eve bağlanma, gerçek oturma bulunmadan da gönderimi kurabilir.","focus_only":"Odak dal evde oturanların tümüne uzanabilir ve aile bağını her kullanımda zorunlu tutmaz.","gloss":"ev halkı ve aile çevresi","neighbor_only":"Komşu dal aileye bağlanan kişileri ve kadın ya da topluluk için aktarmalı ev kullanımını da içerir.","neighbor_ref":"root_000166/B002","relation_type":"near_synonym","shared_zone":"İki dal da aynı eve bağlı aile halkını ve birlikte yaşayan kişileri gösterebilir."},{"boundary_match":"partial","distinction":"Odak için ortak yaşama yeri merkezdir; komşuda ortak ev yalnızca üyeliği kurabilen bağlardan biridir ve kapsam çok daha geniştir.","focus_only":"Odak dal belirli evde yaşayan kişilerle sınırlı bir topluluk kurar.","gloss":"ev halkı ile bağlı topluluk","neighbor_only":"Komşu dal eş, yakınlar, soy, din, iş ve ülke gibi çok farklı üyelik bağlarını da kapsar.","neighbor_ref":"root_000064/B001","relation_type":"near_synonym","shared_zone":"Her iki dal aynı evde yaşayan yakın kişiler topluluğunu anlatabilir."},{"boundary_match":"field_only","distinction":"Biri yaşayan kişilere, diğeri yaşama eylemine ve fiziksel yere yönelir; gönderimleri farklı olduğu için birbirlerinin yerine kullanılamaz.","focus_only":"Odak dal evde yaşayan insan topluluğunu gösterir.","gloss":"ev halkı ile konut","neighbor_only":"Komşu dal yerleşme eylemini, yaşanan evi ve birini oraya yerleştirmeyi gösterir.","neighbor_ref":"root_000726/B002","relation_type":"same_field","shared_zone":"İki dal aynı ev ve orada yaşama durumunun katılımcılarını paylaşır."}],"source_phrase_ar":"السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار","source_summary":"Kaynakların ortak anlatımı, sözü ev halkı, aile üyeleri ve evde ya da belirli bir yerde oturan kişiler için kullanır; fiziksel ev ile içindeki topluluk açıkça ayrılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكن بمعنى أهل الدار والعيال وسكان الدار ومن يقيمون فيها","what_is_not_ar":"ليس نفس المنزل ولا مجرد فعل السكنى"},"support_links":[]},{"boundary":"Odak iç dinginliği sağlayan kişi veya şeydir; yalnız fiziksel durma, ağırbaşlı iç durum ya da salt sıcaklık değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"insanı rahatlatıp içini yatıştıran dayanak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi sevdiği veya yakın bulduğu birine ya da şeye yönelir ve onun yanında içi yatışır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gece ve destekleyici yakarış, dinlenme veya güven verme işlevleriyle aynı adlandırma alanına girer."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yanında oturulup yakınlık ve rahatlık bulunan ateş bu anlamın somut bir gerçekleşmesidir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, zaman, sözlü destek veya ateşin insana yakınlık ve iç rahatlığı vermesi ortak çekirdeğini karşılar.","boundary_detail":"Odak iç dinginliği sağlayan kişi veya şeydir; yalnız fiziksel durma, ağırbaşlı iç durum ya da salt sıcaklık değildir.","branch_image_ar":"مأنس السكون","concept_gloss":"insanı rahatlatıp içini yatıştıran dayanak","contextual_glosses":[{"applicability":"Sevilen kişi ya da destekleyici söz gibi bir dayanağın ruhsal rahatlık sağladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin bir dayanağa yönelmesini ve onunla iç rahatlığı bulmasını korur."},"facet_ids":["F001","F002"],"text":"içini rahatlatan","usage_role":"contextual"},{"applicability":"Ateşin yalnız ısısı değil, yanında bulunmanın verdiği yakınlık ve rahatlık özellikle anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateşin somut varlığını ve yanında rahatlama işlevini birlikte korur."},"facet_ids":["F001","F003"],"text":"yanında iç ısıtan ateş","usage_role":"explanatory"}],"definition":"Kişinin yakınlık duyup yanında rahatladığı, içinin yatıştığı kişi veya şeydir. Gece, destekleyici yakarış ve yanında oturulan ateş bu rahatlatıcı işlevle adlandırılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi sevdiği veya yakın bulduğu birine ya da şeye yönelir ve onun yanında içi yatışır."},{"facet_id":"F002","role":"extension","statement":"Gece ve destekleyici yakarış, dinlenme veya güven verme işlevleriyle aynı adlandırma alanına girer."},{"facet_id":"F003","role":"specialization","statement":"Yanında oturulup yakınlık ve rahatlık bulunan ateş bu anlamın somut bir gerçekleşmesidir."}],"identity_rationale":"Kaynak sözü kişinin içinin yöneldiği ve yanında dinginleştiği sevgiliyi ya da şeyi temel alır; gece, yakarış ve ateş bunun örnekleridir. Dal çerçevesi bu rahatlatıcı ve yakınlık veren dayanağı doğru yakalar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"insanın yanında rahatlayıp içinin yatıştığı kişi veya şey"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yanında oturulup rahatlık bulunan ateş"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"senin yakarışların onları rahatlatır"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geceyi dinlenme ve dinginleşme zamanı yaptı"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"eğri sırığı ateş ve yağla doğrultma"}],"lexicalization_note":"Tanım yalın olarak kişinin yanında rahatlayıp dinginleştiği dayanağı verir; gece, yakarış ve ateş kullanımları ile ateşle düzeltme ayrı bağlamlara bağlı tutulur.","neighbor_coverage_note":"Bütün aday kartlar incelendi. Seçilenler yakınlık, alışma ve sıcaklıkla en olası karışmaları açıklar; diğer adaylar selamlama, üzüntü, unutma veya özel ve uzak kullanımlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta kişinin yöneldiği rahatlatıcı dayanak öne çıkar; komşuda yakınlık kurma ve yabancılık duygusunu giderme süreci daha geniştir.","focus_only":"Odak dal rahatlık veren kişi veya şeyi adlandırır ve gece ile ateş gibi insan olmayan dayanaklara uzanır.","gloss":"rahatlatan dayanak ile yakınlık","neighbor_only":"Komşu dal yakınlaşma, konuşma, sevinç ve ürkütücü olmayan hayvan niteliğini de kapsar.","neighbor_ref":"root_000059/B003","relation_type":"near_synonym","shared_zone":"İki dal da yalnızlık veya tedirginliğin yakınlık sayesinde azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Odakta sonuç olarak iç yatışması belirleyicidir; komşuda tekrar ve yakınlıkla oluşan alışma bağı belirleyicidir.","focus_only":"Odak dal kişinin yanında içinin yatıştığı dayanağı ve onun rahatlatıcı işlevini anlatır.","gloss":"iç rahatlığı ile alışkanlık","neighbor_only":"Komşu dal bir kişi, şey veya yere alışma, onu sürekli yanında tutma ve başkasını alıştırma eylemlerini kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"Yakın bulunup sürekli yönelinen kişi veya yer iki dalda da rahatlık verebilir."},{"boundary_match":"field_only","distinction":"Odakta ateşin yanında bulunmanın rahatlatıcı ve yakınlık veren yönü, komşuda ise ölçülebilir sıcaklık ve ısıtma işlevi çekirdektir.","focus_only":"Odak dal ateşi insana yakınlık ve iç rahatlığı veren bir dayanak olarak ele alır.","gloss":"ateşle rahatlama ve sıcaklık","neighbor_only":"Komşu dal sıcaklığı ve sıcak tutan giysi, ev ya da duvarı doğrudan ısı bakımından ele alır.","neighbor_ref":"root_000479/B001","relation_type":"same_field","shared_zone":"Ateş ve ısınma deneyimi iki dalın somut kullanım alanında buluşur."}],"source_phrase_ar":"كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها","source_summary":"Kaynaklar kişinin sevdiği veya yakın bulduğu şeyin yanında içinin yatışmasını ortak çekirdek yapar; geceyi, destekleyici yakarışı ve ateşi bu rahatlatıcı işlevin örnekleri olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كل ما تسكن إليه النفس من محبوب أو بيت أو ليل أو صلاة أو نار سميت بذلك للأنس والسكون إليها","what_is_not_ar":"ليس الوقار الخاص باسم السكينة ولا فقر المسكين"},"support_links":[]},{"boundary":"Bu dal dış hareketin yalnızca durmasını değil, güvenle birleşen ağırbaşlı ve dingin iç durumu anlatır; yoksulluk ve ezilmişlik ayrı kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"güven veren ağırbaşlı iç dinginlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İç dünyada güven, dinginlik ve ağırbaşlılık birlikte belirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalbin korkudan kurtulup güven duyması bu iç durumun belirgin gerçekleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir sandığın içindeki güven verici şey, insanların kalplerini yatıştırıp onları bir arada tutması bakımından adlandırılır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güven, kalp yatışması, yumuşak başlılık ve ağırbaşlılığın birlikte bulunduğu tam çekirdeği karşılar.","boundary_detail":"Bu dal dış hareketin yalnızca durmasını değil, güvenle birleşen ağırbaşlı ve dingin iç durumu anlatır; yoksulluk ve ezilmişlik ayrı kalır.","branch_image_ar":"طمأنينة الوقار","concept_gloss":"güven veren ağırbaşlı iç dinginlik","contextual_glosses":[{"applicability":"Korku veya tedirginlik içindeki kişinin kalben güvenli ve dingin duruma getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kalpteki korkunun yerini güven ve dinginliğin almasını korur."},"facet_ids":["F001","F002"],"text":"kalbine güven ve dinginlik verdi","usage_role":"contextual"},{"applicability":"Sandıktaki şeyin topluluğa güven verip dağılmasını önleyen işlevi açıklandığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut bir dayanağın kalpleri yatıştırıp güven oluşturma işlevini korur."},"facet_ids":["F003"],"text":"kalpleri yatıştıran güvence","usage_role":"explanatory"}],"definition":"Korku ve taşkınlığın yerini güvenin, ağırbaşlılığın ve yumuşak bir iç dinginliğinin almasıdır. Kalbe verilen güven ile topluluğu bir arada tutan sandık içeriği bu durumun özel anlatımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İç dünyada güven, dinginlik ve ağırbaşlılık birlikte belirir."},{"facet_id":"F002","role":"specialization","statement":"Kalbin korkudan kurtulup güven duyması bu iç durumun belirgin gerçekleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Bir sandığın içindeki güven verici şey, insanların kalplerini yatıştırıp onları bir arada tutması bakımından adlandırılır."}],"identity_rationale":"Kaynak sözü ağırbaşlılık, yumuşak başlılık, güven ve kalbin yatışmasını aynı iç durum çevresinde birleştirir. Sandık içindeki şeyin insanlara güven verip kaçmalarını önlemesi bu çekirdeğin özel anlatısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sandıktaki, kalpleri yatıştırıp güven veren şey"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"inananların kalplerine güven ve dinginlik verdi"}],"lexicalization_note":"Tanım ağırbaşlı iç dinginliği yalın çekirdek yapar; kalbe verilmesi ve sandıktaki güven verici şey yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Verilen bütün komşular gözden geçirildi. Dış durma, rahatlatıcı dayanak ve ezilmişlik ile olan üç sınır en yararlı karşılaştırmaları verir; dış adaylar bu anlamla yeterli ortak çekirdek taşımaz.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak insanın iç dünyasında güven ve ağırbaşlılık içerir; komşu için iç dünya ve güven gerekli değildir, hareketin sona ermesi yeterlidir.","focus_only":"Odak dal güven, ağırbaşlılık ve kalp yatışmasını bir iç nitelik olarak birleştirir.","gloss":"iç güven ile hareketin dinmesi","neighbor_only":"Komşu dal herhangi bir şeyin hareket veya çalkantıdan sonra fiziksel ya da genel olarak durmasını anlatır.","neighbor_ref":"root_000726/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da çalkantının azalması ve dingin bir son durum bulunabilir."},{"boundary_match":"partial","distinction":"Odak oluşan iç durumdur; komşu ise çoğunlukla bu durumu doğuran veya yanında bulunan dayanağa yönelir.","focus_only":"Odak dal kişinin içinde oluşan güvenli, ağırbaşlı ve dingin durumu anlatır.","gloss":"iç dinginlik ile rahatlatan dayanak","neighbor_only":"Komşu dal kişiyi rahatlatan ve kendisine yönelinen kişi, zaman, söz veya ateşi adlandırır.","neighbor_ref":"root_000726/B004","relation_type":"near_synonym","shared_zone":"Bir dayanak kişide güven ve iç yatışması oluşturduğunda iki alan örtüşür."},{"boundary_match":"field_only","distinction":"Odakta güven ve dengeli ağırbaşlılık vardır; komşuda yoksunluk, güçsüzlük ya da baskı altında boyun eğme vardır, bu nedenle değer ve neden bakımından ayrılırlar.","focus_only":"Odak dal güvenli, ağırbaşlı ve dengeli bir iç durumu bildirir.","gloss":"ağırbaşlı dinginlik ile ezilmişlik","neighbor_only":"Komşu dal yoksulluk, güçsüzlük, ezilmişlik ve boyun eğme durumlarını bildirir.","neighbor_ref":"root_000726/B006","relation_type":"same_field","shared_zone":"İki dal da dış taşkınlığın bulunmadığı, alçak sesli veya çekingen bir görünüşle ilişkilendirilebilir."}],"source_phrase_ar":"السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين","source_summary":"Kaynaklar ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliğini ortak bir iç durum olarak sunar; kalbe güven verilmesi ve sandıktaki güven verici şey bunun özel anlatılarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكينة بمعنى الوقار والوداعة والأمن وطمأنينة القلب وما في التابوت الذي تسكن به القلوب","what_is_not_ar":"ليس مطلق السكون الحسي ولا المسكنة"},"support_links":[]},{"boundary":"Dal hem yoksulluğu hem ezilmiş ve güçsüz durumu kapsar; ağırbaşlı iç dinginlik ya da evde yaşama anlamları buna dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B006","candidate_links":[{"candidate_id":"cand_f354c0f2f89f52911ea7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"yoksulluk, güçsüzlük ve ezilmişlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi geçim araçlarından yoksun ve yardıma gerek duyan durumda olabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz, maddi yoksunluktan bağımsız olarak güçsüzlük, ezilmişlik ve aşağı durumda bulunmayı da anlatabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişinin boyun eğmesi, kendini aşağı koyması veya yoksul duruma gelmesi türemiş eylemlerle ifade edilir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Maddi yoksunluk ile aşağı ve güçsüz durumda bulunma yönlerini birlikte taşıyan dalın tam alanını karşılar.","boundary_detail":"Dal hem yoksulluğu hem ezilmiş ve güçsüz durumu kapsar; ağırbaşlı iç dinginlik ya da evde yaşama anlamları buna dahil değildir.","branch_image_ar":"ذل المسكنة","concept_gloss":"yoksulluk, güçsüzlük ve ezilmişlik","contextual_glosses":[{"applicability":"Bir kişinin geçim araçlarından yoksun oluşu ile zayıf toplumsal durumunun birlikte kastedildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin hem maddi yoksunluğunu hem güçsüz durumunu korur."},"facet_ids":["F001","F002"],"text":"yoksul ve güçsüz kişi","usage_role":"contextual"},{"applicability":"Kişinin baskı veya bağlılık karşısında kendini güçsüz ve aşağı konuma koyduğu eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyun eğme ile kendini aşağı konuma koyma eylemini birlikte korur."},"facet_ids":["F002","F003"],"text":"boyun eğip kendini alçalttı","usage_role":"contextual"}],"definition":"Geçim araçlarından yoksun olma veya güçsüz, ezilmiş ve aşağı durumda bulunmadır. Bu durumdan hareketle kişinin boyun eğmesi ya da kendini aşağı koyması da aynı söz ailesinde anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi geçim araçlarından yoksun ve yardıma gerek duyan durumda olabilir."},{"facet_id":"F002","role":"extension","statement":"Söz, maddi yoksunluktan bağımsız olarak güçsüzlük, ezilmişlik ve aşağı durumda bulunmayı da anlatabilir."},{"facet_id":"F003","role":"associated_use","statement":"Kişinin boyun eğmesi, kendini aşağı koyması veya yoksul duruma gelmesi türemiş eylemlerle ifade edilir."}],"identity_rationale":"Kaynak sözü yoksulluk halini, güçsüzlük ve ezilmişliği, ayrıca kişinin boyun eğip kendini aşağı koymasını aynı dalda açıkça sayar. Dal çerçevesi maddi yoksunluk ile toplumsal veya iradi boyun eğme arasındaki bağı korur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yoksul ya da ezilmiş ve güçsüz kişi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yoksulluk veya ezilmişlik durumu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yoksul duruma geldi ya da boyun eğip kendini alçalttı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"boyun eğdi ve alçaldı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı onu yoksul duruma düşürdü"}],"lexicalization_note":"Tanım yalın tek anlam varsaymaz; yoksul kişi ve yoksulluk durumunu, ezilmişlik ile boyun eğme bildiren türemiş eylemlerden açıkça ayırır.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi. Seçilenler yoksulluk, aşağılanma ve ağır sürekli yoksulluk sınırlarını gösterir; diğerleri hor görülme, mal kaybı veya yalnız yoksullaşma sonucuna odaklanır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yoksulluktan toplumsal ezilmişliğe ve boyun eğmeye genişler; komşunun sınırı yoksulluk ile ona bağlı toprak görüntüsünde kalır.","focus_only":"Odak dal yoksulluğun yanında güçsüzlük, ezilmişlik ve boyun eğme eylemlerini de kapsar.","gloss":"yoksulluk ve ezilmişlik","neighbor_only":"Komşu dal yoksulluğu toprağa yapışma görüntüsü ve belirli bir kalıp sözle anlatır.","neighbor_ref":"root_000178/B002","relation_type":"near_synonym","shared_zone":"İki dal da maddi yoksunluğu, gereksinimi ve yardıma muhtaç durumu anlatır."},{"boundary_match":"partial","distinction":"Odakta yoksulluk bu alanın temel parçasıdır; komşuda maddi yoksunluk gerekmez, aşağılanma ve düşük konuma razı olma belirleyicidir.","focus_only":"Odak dal maddi yoksulluğu ve yoksul kişiyi de doğrudan kapsar.","gloss":"ezilmişlik ile aşağılanma","neighbor_only":"Komşu dal baskıyla gelen aşağılanmayı, düşük konumu ve buna razı olmayı özellikle öne çıkarır.","neighbor_ref":"root_000865/B002","relation_type":"near_synonym","shared_zone":"İki dal da kişinin aşağı, güçsüz ve baskı altında bir durumda bulunmasını gösterebilir."},{"boundary_match":"partial","distinction":"Odak daha geniş nitelikler ve eylemler taşır; komşu ise yoksulluğun ağır ve süreğen derecesiyle daha dardır.","focus_only":"Odak dal yoksulluğun yanında güçsüzlük, ezilmişlik ve boyun eğmeyi içerir.","gloss":"genel yoksulluk ile sürekli ağır yoksulluk","neighbor_only":"Komşu dal yalnız eksiksiz ve sürekli yoksulluk derecesini bildirir.","neighbor_ref":"root_000132/B003","relation_type":"near_synonym","shared_zone":"Her iki dal geçim araçlarından yoksun olma durumunu anlatır."}],"source_phrase_ar":"المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل","source_summary":"Kaynakların ortak çerçevesi yoksul kişiyi ve yoksulluk durumunu güçsüzlük, ezilmişlik ve boyun eğmeyle ilişkilendirir; türemiş eylemler kişinin yoksullaşmasını veya kendini aşağı koymasını anlatır.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه المسكين والمسكنة والفقر والذلة والضعف والخضوع والاستكانة والتمسكن","what_is_not_ar":"ليس السكينة بمعنى الوقار ولا السكنى في الدار"},"support_links":["sup_cb50b040fe06a4b16610"]},{"boundary":"Dal kesici bıçak ile onu yapan kişiyi kapsar; gemi dengeleme parçası ya da kesme eyleminin kendisi değildir.","branch_kind":"bare","branch_ref":"root_000726/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"kesici bıçak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, kesmekte kullanılan ağızlı bıçaktır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın kökeni, bıçağın kesilen hayvanın hareketini ölümle sona erdirmesine bağlanır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın araç gönderimini kısa ve doğal biçimde karşılar; adın köken açıklaması tanımda ayrıca korunur.","boundary_detail":"Dal kesici bıçak ile onu yapan kişiyi kapsar; gemi dengeleme parçası ya da kesme eyleminin kendisi değildir.","branch_image_ar":"إسكان الذبيحة بالسكين","concept_gloss":"kesici bıçak","contextual_glosses":[{"applicability":"Bıçağın kesilen hayvanın hareketini sona erdirme işlevi özellikle öne çıkarıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kesici aracı ve hayvan kesme bağlamındaki işlevini birlikte korur."},"facet_ids":["F001","F002"],"text":"hayvan kesme bıçağı","usage_role":"contextual"}],"definition":"Kesmekte kullanılan ağızlı bıçaktır. Kaynaklar adını, kesilen hayvanın hareketini ölümle sona erdirmesi üzerinden açıklar; aracı yapan kişi de ayrı bir türemiş adla gösterilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, kesmekte kullanılan ağızlı bıçaktır."},{"facet_id":"F002","role":"associated_use","statement":"Adın kökeni, bıçağın kesilen hayvanın hareketini ölümle sona erdirmesine bağlanır."}],"identity_rationale":"Kaynak sözü kesici bıçağı doğrudan adlandırır ve adlandırmayı kesilen hayvanın hareketini ölümle sona erdirmesine bağlar. Dal çerçevesi aracı ve verilen köken açıklamasını koruyarak gemi parçasından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kesici bıçak"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bıçak yapan kimse"}],"lexicalization_note":"Tanım bıçak adını yalın araç anlamıyla verir; hayvanın hareketini sona erdirmeye dayalı ad açıklamasını çekirdeğin yerine geçirmeyen bağlı bir açıklama olarak tutar.","neighbor_coverage_note":"Tüm komşu kartları incelendi. Seçilenler araç, keskin kenar ve kesme işlemi ayrımını en açık biçimde kurar; kalanlar kılıç türleri, hayvan öldürme yolları veya uzak kök dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belirli bıçak türünün genel adıdır; komşu farklı kesici araçları ve keskin ağız biçimlerini daha geniş bir kümede toplar.","focus_only":"Odak dal belirli bir bıçak adını ve hayvanın hareketini sona erdirmeye bağlanan ad açıklamasını içerir.","gloss":"bıçak ile kesici araç","neighbor_only":"Komşu dal kesme araçlarını, kılıcı, kısa geniş ağzı ve kesik oku kapsayan daha geniş bir araç ve ağız alanıdır.","neighbor_ref":"root_001240/B014","relation_type":"near_synonym","shared_zone":"Her iki dal keskin ağızla kesme işlevi gören elde kullanılan araçları kapsayabilir."},{"boundary_match":"field_only","distinction":"Odak araç bütünüdür, komşu ise aracın kesen kenarı veya ucudur; parça ile bütün aynı gönderime sahip değildir.","focus_only":"Odak dal bütün kesici bıçağın kendisini gösterir.","gloss":"bıçak ile keskin ağız","neighbor_only":"Komşu dal kılıç veya bıçağın keskin kenarını ve herhangi bir şeyin kesici ucunu gösterir.","neighbor_ref":"root_001078/B012","relation_type":"same_field","shared_zone":"Bıçak, kesme işini komşu dalın gösterdiği keskin kenar sayesinde yapar."},{"boundary_match":"thematic_only","distinction":"Odak olayda kullanılan nesnedir; komşu bu nesneyle yapılabilecek belirli bedensel işlemdir ve anlam çekirdekleri örtüşmez.","focus_only":"Odak dal kesme aracını adlandırır.","gloss":"kesme aracı ile boyun kesme işlemi","neighbor_only":"Komşu dal hayvanın boyun kemiğini kesme işlemini adlandırır.","neighbor_ref":"root_000088/B004","relation_type":"thematic","shared_zone":"İki dal hayvan kesme olayında araç ve işlem olarak birlikte yer alabilir."}],"source_phrase_ar":"السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح","source_summary":"Kaynaklar kesici bıçağın bilinen araç olduğunu ortaklaşa belirtir ve adlandırılmasını, kesilen hayvanın hareketini sona erdirme sonucuyla açıklar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه السكين والمدية وتسميتها لأنها تسكن اضطراب المذبوح بالموت","what_is_not_ar":"ليس سكان السفينة ولا السكين بمعنى الحمار"},"support_links":[]},{"boundary":"Bu dal yalnız geminin kıçındaki dengeleyici ve yöneltici bölüm ya da araçla ilgilidir; geminin tamamını veya genel durma eylemini adlandırmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"geminin kıçındaki dengeleyici yöneltme aracı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim geminin kıçında bulunan belirli bir bölüm veya araçtır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu bölüm veya araç gemiyi dengeler, yöneltir ve çalkantısını azaltır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçanın gemideki yerini ve gemiyi dengeleyip yöneltme işlevini birlikte karşılar.","boundary_detail":"Bu dal yalnız geminin kıçındaki dengeleyici ve yöneltici bölüm ya da araçla ilgilidir; geminin tamamını veya genel durma eylemini adlandırmaz.","branch_image_ar":"تسكين السفينة بالسكان","concept_gloss":"geminin kıçındaki dengeleyici yöneltme aracı","contextual_glosses":[{"applicability":"Tarihsel gemi bölümünün modern tek bir parça adıyla kesin eşleştirilmesi gerekmediğinde açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geminin kıçındaki yerini ve denge sağlama işlevini kesin olmayan tür eşleştirmesi yapmadan korur."},"facet_ids":["F001","F002"],"text":"gemiyi dengede tutan kıç parçası","usage_role":"explanatory"}],"definition":"Geminin kıçında bulunan, gemiyi dengede tutmaya, yöneltmeye ve çalkantısını azaltmaya yarayan bölüm veya araçtır. Adlandırma doğrudan bu dengeleme işlevine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim geminin kıçında bulunan belirli bir bölüm veya araçtır."},{"facet_id":"F002","role":"core","statement":"Bu bölüm veya araç gemiyi dengeler, yöneltir ve çalkantısını azaltır."}],"identity_rationale":"Kaynak sözü geminin kıçındaki, onu dengede tutup çalkantısını azaltan bölüm veya aracı açıkça verir. Dal çerçevesi bu gemiye özgü gönderimi ve dengeleme işlevini kesici bıçak anlamından doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"gemiyi dengede tutup çalkantısını azaltan kıç parçası"}],"lexicalization_note":"Tanım gemi parçasının özel adını yalın biçimde korur; gemiyle kurulan kalıp ifade aynı parçayı işleviyle belirleyen kullanımdır ve genel durma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Seçilen üç kart gemi donanımı, itme eylemi ve durma sonucu arasındaki sınırı gösterir; diğerleri gemi türleri, geminin bütünü veya uzak kök dallarıdır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odaktaki parça kıçta denge ve yön sağlar; komşudaki sırık dışarıdan su tabanına dayanarak gemiyi ileri iter.","focus_only":"Odak dal geminin kıçındaki sürekli dengeleme ve yöneltme bölümünü veya aracını gösterir.","gloss":"kıç dengeleyicisi ile itme sırığı","neighbor_only":"Komşu dal gemiyi itmek için suya dayanan uzun sırığı gösterir.","neighbor_ref":"root_000767/B006","relation_type":"same_field","shared_zone":"İki dal da geminin hareketini denetlemekte kullanılan donanımı adlandırır."},{"boundary_match":"thematic_only","distinction":"Odak bir gemi parçasıdır; komşu ise ayrı bir araçla yapılan itme hareketidir, bu nedenle yalnız aynı olay alanını paylaşırlar.","focus_only":"Odak dal gemiyi dengeleyen ve yönelten parçayı adlandırır.","gloss":"dengeleyici parça ile sırıkla itme","neighbor_only":"Komşu dal gemicinin bir sırıkla gemiyi itme eylemini adlandırır.","neighbor_ref":"root_001413/B006","relation_type":"thematic","shared_zone":"Her ikisi de geminin hareketinin insan eliyle denetlenmesi olayında yer alır."},{"boundary_match":"partial","distinction":"Odak bu sonucu sağlayan belirli araçtır; komşu ise aracın türünden bağımsız olarak ortaya çıkan durma veya az hareket durumudur.","focus_only":"Odak dal geminin çalkantısını azaltan belirli kıç bölümünü veya aracını gösterir.","gloss":"gemiyi dengeleme ile geminin durması","neighbor_only":"Komşu dal herhangi bir şeyin durmasını veya az hareket etmesini ve geminin denizde beklemesini anlatır.","neighbor_ref":"root_000114/B003","relation_type":"near_neighbor","shared_zone":"Geminin hareketinin azalması iki dalın gemi bağlamında buluştuğu sonuçtur."}],"source_phrase_ar":"سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به","source_summary":"Kaynaklar geminin kıçındaki bu bölüm veya aracı ortaklaşa tanımlar; temel işlevi gemiyi ayarlamak, dengede tutmak ve çalkantısını azaltmaktır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه سكان السفينة وذنبها أو كوثلها الذي تعدل به وتسكن عن الاضطراب","what_is_not_ar":"ليس السكين المدية ولا السكن أهل الدار"},"support_links":[]},{"boundary":"Bu dal genel olarak evde yaşama anlamına genişletilemez; bedensel yerleşme noktası, kalıplaşmış konum anlatıları ve özel yer adıyla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"sabit yer ve konum bildiren özel kullanımlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başın boyuna oturduğu nokta, bedendeki belirli bir yerleşme yeri olarak adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Çoğul kalıp ifadeler kişilerin yerlerini, konumlarını, düzeylerini, evlerini veya alışılmış düzenlerini gösterebilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim, belirli bir bölgedeki özel yerin adı olarak da aktarılır."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek bir yalın anlam olmadığını, bedensel yer, kalıplaşmış konum ve özel yer adı kullanımlarını bir şemsiye altında topladığını gösterir.","boundary_detail":"Bu dal genel olarak evde yaşama anlamına genişletilemez; bedensel yerleşme noktası, kalıplaşmış konum anlatıları ve özel yer adıyla sınırlıdır.","branch_image_ar":"موضع الاستقرار","concept_gloss":"sabit yer ve konum bildiren özel kullanımlar","contextual_glosses":[{"applicability":"Söz bedensel yapıda baş ile boynun birleştiği yerleşme noktasını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başın boyun üzerindeki belirli oturma noktasını korur."},"facet_ids":["F001"],"text":"başın boyuna oturduğu yer","usage_role":"explanatory"},{"applicability":"Çoğul kalıp kişilerin yerlerinde, düzeylerinde veya olağan düzenlerinde kalmasını anlattığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem fiziksel konum hem alışılmış düzen yorumunu açıkça korur."},"facet_ids":["F002"],"text":"yerlerinizde ve alışılmış düzeninizde","usage_role":"contextual"}],"definition":"Sabit yer veya konum düşüncesine bağlı birkaç özel kullanımdır: başın boyuna oturduğu nokta, çoğul kalıplarda kişilerin yerleri, konumları, düzeyleri ya da alışılmış düzenleri ve belirli bir yer adı. Bunlar genel yerleşip yaşama eylemi değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başın boyuna oturduğu nokta, bedendeki belirli bir yerleşme yeri olarak adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Çoğul kalıp ifadeler kişilerin yerlerini, konumlarını, düzeylerini, evlerini veya alışılmış düzenlerini gösterebilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı biçim, belirli bir bölgedeki özel yerin adı olarak da aktarılır."}],"identity_rationale":"Kaynak sözü tek bir genel yer anlamından fazlasını içerir: özel bir yer adı, başın boyuna oturduğu nokta ve kalıplaşmış çoğul ifadelerde yerler, konumlar, düzeyler veya alışılmış düzen vardır. Dal korunabilir, ancak yalnız bu özel ve kalıplaşmış yerleşiklik kullanımlarının şemsiyesi olarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"başın boyuna oturduğu yer"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yerlerinizde, konumlarınızda veya alışılmış düzeninizde"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"belirli bir bölgedeki özel yer adı"}],"lexicalization_note":"Tanım özel yer adını, bedensel yeri ve çoğul kalıp ifadeleri ayrı tutar; bunlardan genel bir yalın yerleşme anlamı çıkarmaz.","neighbor_coverage_note":"Bütün komşu adaylar değerlendirildi. Seçilenler genel yerleşme, bedensel bölüm ve özel yer adı sınırlarını açıklar; kalanlar yükseklik, başka yer adları veya yalnız mekanda kalma eylemidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yalnız özel ad ve kalıplarda yaşayan yer-konum kullanımlarını toplar; komşu gündelik ve üretken yerleşme ile konut alanıdır.","focus_only":"Odak dal bedensel yerleşme noktası, kalıplaşmış konumlar ve özel bir yer adıyla sınırlıdır.","gloss":"özel sabit konum ile yerleşme","neighbor_only":"Komşu dal genel olarak bir yere yerleşip yaşamayı, konutu ve başkasını orada oturtmayı anlatır.","neighbor_ref":"root_000726/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir şeyin bulunduğu ya da kalıcı biçimde bağlı olduğu yer düşüncesi vardır."},{"boundary_match":"partial","distinction":"Odakta baş ile boynun birleştiği özel oturma noktası vardır; komşuda kuşak çevresindeki orta ve yan bölüm belirleyicidir.","focus_only":"Odak dal bedende özellikle başın boyuna oturduğu noktayı gösterir ve başka kalıplaşmış yer kullanımları da taşır.","gloss":"baş-boyun yerleşme noktası ile orta bölüm","neighbor_only":"Komşu dal bel, yan taraf ve çevreleyen kuşağın bulunduğu orta bölgeyi insan, hayvan, bitki ve yeryüzü biçimlerine yayar.","neighbor_ref":"root_001519/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir bütünün bedensel veya biçimsel olarak belirlenmiş bölümünü yer bakımından gösterebilir."},{"boundary_match":"field_only","distinction":"Özel yer adları farklı gönderimlere sahiptir; ayrıca odaktaki bedensel ve toplumsal konum kullanımları komşunun at bekleme yeri anlamında bulunmaz.","focus_only":"Odak dal özel yer adının yanında bedensel ve kalıplaşmış konum anlamları taşır.","gloss":"özel yer ve bekleme konumu","neighbor_only":"Komşu dal başka bir özel yer adını ve atların salınmadan önce beklediği yeri gösterir.","neighbor_ref":"root_000291/B009","relation_type":"same_field","shared_zone":"Her iki dal belirli bir yer adı veya sabit duruş yeri olarak kullanılabilir."}],"source_phrase_ar":"موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم","source_summary":"Toplu kaynak sözü sabit yer düşüncesine bağlı fakat birbirinden ayrılması gereken kullanımları verir: bedensel yerleşme noktası, çoğul kalıplarda yer ve düzen anlatımı ile belirli bir özel yer adı.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السكنات بمعنى المواضع والمساكن والطبقات والمنازل ومقر الرأس من العنق","what_is_not_ar":"ليس فعل السكنى العام ولا أهل الدار"},"support_links":[]},{"boundary":"Dal her türlü yiyeceği veya otlağı değil, geçimi sürdürerek insanı ya da sürüyü bulunduğu yerde tutan yeterli besin kaynağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000726/B010","candidate_links":[{"candidate_id":"cand_701b35c256c4d6fca187","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","surface_ar":"مِسْكِينِ"}],"gloss":"yerinde kalmayı sağlayan geçimlik ve bol otlak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yiyecek veya geçimlik, kişinin yaşamını sürdürmesini ve bulunduğu yerde kalmasını sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak, aynı yerinde tutma işleviyle nitelenir."}}],"root_ar":"س ك ن","root_id":"root_000726","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan için geçimlik yiyeceği ve sürü için göçü gereksiz kılan bol otlağı ortak işlevleriyle birlikte karşılar.","boundary_detail":"Dal her türlü yiyeceği veya otlağı değil, geçimi sürdürerek insanı ya da sürüyü bulunduğu yerde tutan yeterli besin kaynağını anlatır.","branch_image_ar":"قوت يثبت المقام","concept_gloss":"yerinde kalmayı sağlayan geçimlik ve bol otlak","contextual_glosses":[{"applicability":"İnsanın geçimini sürdürmesine ve bulunduğu yerde yaşamaya devam etmesine yarayan besinler kastedildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaşamı sürdürmeye yarayan yiyeceklerin geçimlik işlevini korur."},"facet_ids":["F001"],"text":"geçimlik yiyecekler","usage_role":"contextual"},{"applicability":"Sürünün besin bulmak için başka yere götürülmesine gerek bırakmayan otlak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Otlak bolluğunu ve bunun göç gereğini kaldırma sonucunu birlikte korur."},"facet_ids":["F002"],"text":"göç gerektirmeyecek kadar bol otlak","usage_role":"explanatory"}],"definition":"İnsanın geçimini sürdürüp bulunduğu yerde kalmasını sağlayan yiyecek veya geçimliktir. Hayvancılık bağlamında, sürünün başka yere göç etmesini gerektirmeyecek kadar bol otlak aynı işlevle nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yiyecek veya geçimlik, kişinin yaşamını sürdürmesini ve bulunduğu yerde kalmasını sağlar."},{"facet_id":"F002","role":"specialization","statement":"Sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak, aynı yerinde tutma işleviyle nitelenir."}],"identity_rationale":"Kaynak sözü yiyecek ve geçimlikleri, kişinin onların sayesinde yerinde kalabilmesiyle açıklar; bol otlak da topluluğu göç etmekten alıkoyduğu için aynı işlevsel çizgidedir. Dal çerçevesi besin ile yerinde kalma sonucunu doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bulunduğu yerde geçinmeyi sağlayan yiyecekler"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"yerinde kalmayı sağlayan bir geçimlik"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak"}],"lexicalization_note":"Tanım geçimlik yiyecek biçimlerini yalın besin alanında, bol otlak kalıbını ise göçü gereksiz kılan özel hayvancılık bağlamında ayrı tutar.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi. Seçilenler genel temel yiyecek, az idarelik ve genel otlakla sınırı kurar; kalanlar pay, göçebe yaşam, otlatma eylemi veya yeterlilik sonucuna odaklanır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta yiyeceğin yer değiştirmeyi önleyip kalışı sağlaması belirgindir; komşuda temel sonuç bedenin ve yaşamın sürmesidir.","focus_only":"Odak dal besinin kişiyi bulunduğu yerde tutma işlevini ve bol otlak uzantısını içerir.","gloss":"yerinde tutan geçimlik ile yaşatan yiyecek","neighbor_only":"Komşu dal bedeni ayakta ve yaşamı sürer tutan yiyeceği, başkasını besleme eylemleriyle birlikte genel olarak kapsar.","neighbor_ref":"root_001268/B001","relation_type":"near_synonym","shared_zone":"İki dal da yaşamı sürdürmek için gereken temel yiyecek ve geçimliği anlatır."},{"boundary_match":"partial","distinction":"Odak yerinde kalmaya yetecek kaynak ve hatta bolluk içerir; komşu özellikle kıt, geçici ve ancak idare ettiren miktara yönelir.","focus_only":"Odak dal yeterli geçimliği ve göçü gereksiz kılan bol otlağı kapsar.","gloss":"yeterli geçimlik ile az idarelik","neighbor_only":"Komşu dal insan veya hayvanın bir süre idare etmesini sağlayan az yiyeceği ve bahara kadar yeten sınırlı otlamayı öne çıkarır.","neighbor_ref":"root_001039/B006","relation_type":"near_synonym","shared_zone":"Her iki dal insanın veya hayvanın yaşamını sürdürmesine yetecek besin kaynağını anlatabilir."},{"boundary_match":"partial","distinction":"Odak yalnız göç gereğini kaldıracak bolluktaki otlağı niteler; komşu her tür ot ve otlak için genel addır.","focus_only":"Odak dal otlağın bol olup sürüyü bulunduğu yerde tutması koşulunu taşır ve insan geçimliğine de uzanır.","gloss":"bol yerleşik otlak ile genel otlak","neighbor_only":"Komşu dal hayvanların yediği ot ve otlağı, bolluk veya yerinde tutma koşulu olmadan genel olarak adlandırır.","neighbor_ref":"root_000003/B001","relation_type":"near_neighbor","shared_zone":"İki dalın hayvancılık alanında ortak gönderimi otlayan hayvana besin sağlayan bitki ve otlaktır."}],"source_phrase_ar":"الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه","source_summary":"Tek kaynaklı anlatım, yiyecek ve geçimliği kişinin yerinde kalmasını sağlayan destek olarak açıklar; bol otlağı da sürüyü başka yere götürme gereğini kaldırdığı için aynı çizgiye bağlar.","sources":["TA"],"what_is_ar":"يدخل فيه الأسكان بمعنى الأقوات والمرعى المسكن الكثير الذي لا يخرج عنه إلى الظعن","what_is_not_ar":"ليس المسكن بمعنى البيت ولا السكينة"},"support_links":["sup_26a54b72ec02ca8c0abd"]},{"boundary":"Anlam, konuşmaya başlatma, mecazi geçim, meyvenin olgunlaşması ve başka özel dallara taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"tatma, yeme ve yenilen besin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin tadını duyuyla algılama ve ondan tat alma."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi yeme veya besin olarak tüketme."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yenilen, açlığı gideren ve kimi bağlamlarda içeceği de kapsayan besin."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı kullanımlarda besin adının özellikle buğdaya ayrılması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duyusal tatma, tüketme ve açlığı gideren besin çekirdeğini birlikte anlatan genel açıklamadır.","boundary_detail":"Anlam, konuşmaya başlatma, mecazi geçim, meyvenin olgunlaşması ve başka özel dallara taşınmaz.","branch_image_ar":"ذوق الشيء وتناوله","concept_gloss":"tatma, yeme ve yenilen besin","contextual_glosses":[{"applicability":"Bir yiyecek ya da içeceğin tadının duyuyla algılandığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yeme ve besin adı olma anlamlarını kapsamaz.","preserves":"Duyusal tat alma eylemini doğal biçimde korur."},"facet_ids":["F001"],"text":"tadına bakmak","usage_role":"contextual"},{"applicability":"Yenilen ve açlığı gideren şeyin adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tat alma eylemini ve içeceğin sınırlı kapsamını dışarıda bırakır.","preserves":"Yenilen besin ve açlığı giderme yönünü korur."},"facet_ids":["F003"],"text":"yiyecek","usage_role":"contextual"}],"definition":"Bir şeyin tadını duyuyla algılamak veya onu yemek; ayrıca yenilen ve açlığı gideren besin. İçecek, tadına bakılması ya da besleyici olması bakımından bu kapsama girebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin tadını duyuyla algılama ve ondan tat alma."},{"facet_id":"F002","role":"core","statement":"Bir şeyi yeme veya besin olarak tüketme."},{"facet_id":"F003","role":"extension","statement":"Yenilen, açlığı gideren ve kimi bağlamlarda içeceği de kapsayan besin."},{"facet_id":"F004","role":"specialization","statement":"Bazı kullanımlarda besin adının özellikle buğdaya ayrılması."}],"identity_rationale":"Kaynak ifadesi duyusal tatmayı, bir şeyi yemeyi ve yenilen besini aynı çekirdekte toplar; içecek de tadına bakılan veya besleyen bir şey olduğunda bu alana girer. Bu çerçeve, buğdaya özgü kullanımı ve doyurucu yiyecek ya da su kalıbını çekirdeğin özel gerçekleşmeleri olarak tutmayı gerektirir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tat, lezzet"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yemek veya tadına bakmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yiyecek, besin"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"özellikle buğday"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tadına bakma ve iştahını yoklama"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"doyuran ve besleyen yiyecek ya da su"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"yeme isteği veya iştah çekici şey"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çok yiyen, obur"}],"lexicalization_note":"Tanım yalın tatma, yeme ve besin anlamlarını kapsar; buğdaya özgü adlandırma ile doyurup besleyen yiyecek ya da su kullanımı ayrıca sınırlandırılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yararlı ayrım, tatma ve tüketme çekirdeğinin başkasını besleme eylemiyle karıştırılmasını önleyen iç komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki çekirdek tüketenin deneyimi ve tüketilen besindir; komşuda ise veren ya da isteyen ikinci bir katılımcı vardır, bu yüzden olağan bağlamda birbirlerinin yerine geçmezler.","focus_only":"Bu dal kişinin tatması, yemesi veya besinin kendisiyle ilgilidir.","gloss":"tüketme ile yedirme ayrımı","neighbor_only":"Komşu dal besini bir başkasına verme ya da ondan besin isteme eylemini içerir.","neighbor_ref":"root_000934/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yiyecek ve beslenme çevresinde buluşur."}],"source_phrase_ar":"أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)","source_summary":"Kaynakların ortak çizgisi tat duyusu, yeme eylemi ve yenilen besindir; içecek ise tadılan veya besleyen şey olarak bu çizgiye bağlanır. Bazı kullanımlarda genel besin adı özellikle buğdayı gösterebilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الطعم بمعنى الذوق والأكل والطعام وما يسد الجوع، ويدخل استعماله في الشراب إذا جعل ذوقا أو غذاء","what_is_not_ar":"ليس منه الاستفتاح في القراءة ولا الرزق المجازي ولا نضج الثمر إلا بفرع مخصوص"},"support_links":[]},{"boundary":"Konuşma ya da okuma sırasında söz isteme anlamı ve yalnızca iyi geçim içinde olma durumu bu dala girmez.","branch_kind":"bare","branch_ref":"root_000934/B002","candidate_links":[{"candidate_id":"cand_f354c0f2f89f52911ea7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"başkasını beslemek veya beslenmeyi istemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasına yiyecek ya da besleyici bir şey vererek onu doyurma."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başkasından yiyecek vermesini ve kendisini doyurmasını isteme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Besini verme ve karşı taraftan besin talep etme yönlerini birlikte gösteren tam kapsamlı açıklamadır.","boundary_detail":"Konuşma ya da okuma sırasında söz isteme anlamı ve yalnızca iyi geçim içinde olma durumu bu dala girmez.","branch_image_ar":"إطعام الغير وطلب الطعام","concept_gloss":"başkasını beslemek veya beslenmeyi istemek","contextual_glosses":[{"applicability":"Birine yiyecek ya da besleyici içecek verildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Karşı taraftan besin isteme yönünü göstermez.","preserves":"Başkasına besin verme yönünü doğal biçimde korur."},"facet_ids":["F001"],"text":"doyurmak","usage_role":"contextual"}],"definition":"Bir başkasına yiyecek veya yenilip içilebilen besleyici bir şey vermek; ayrıca bir başkasından kendisini beslemesini istemek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasına yiyecek ya da besleyici bir şey vererek onu doyurma."},{"facet_id":"F002","role":"extension","statement":"Bir başkasından yiyecek vermesini ve kendisini doyurmasını isteme."}],"identity_rationale":"Kaynak ifadesi bir başkasına yenilecek şey verme ile bir başkasından kendisini doyurmasını isteme yönlerini açıkça birlikte taşır. Dalın kimliği, kişinin kendisinin yemesinden değil besini veren ile alan arasındaki aktarım ilişkisinden doğar.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yiyecek vermek, doyurmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendisini doyurmasını istemek"}],"lexicalization_note":"Tanım, başkasını besleme ve beslenmeyi isteme eylemlerini yalın dal kapsamı içinde verir; özel konuşma kalıplarını içeri almaz.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; genel isteme alanıyla kurulan ayrım, besin aktarımına özgü katılımcı yapısını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki isteme besinle sınırlıdır ve besin verme karşılığını da kapsar; komşu ise nesnesi sınırlanmamış genel bir arama ve isteme alanıdır.","focus_only":"Bu dalda istenen şey özellikle beslenmedir ve ayrıca başkasını doyurma eylemi de bulunur.","gloss":"besin isteme ile genel isteme","neighbor_only":"Komşu dal herhangi bir şeyi arama, isteme veya onun peşine düşme anlamını taşır.","neighbor_ref":"root_000138/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da bir gereksinimin karşı taraftan istenmesi bulunabilir."}],"source_phrase_ar":"الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)","source_summary":"Kaynaklar, yenilip içilebilen bir şeyi başkasına vermeyi ve bunun istenmesini aynı aktarım alanında birleştirir. İhtiyaç sahibini doyurma bu temel ilişkinin belirgin uygulamasıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أطعمته الطعام واستطعمه أي سأله أن يطعمه وإطعام المحتاج","what_is_not_ar":"ليس منه تلقين الإمام عند الارتياج ولا مجرد حسن الحال في المطعم"},"support_links":["sup_cb50b040fe06a4b16610"]},{"boundary":"Bu dal yalnızca belirtilen konuşma ve okuma kalıplarına bağlıdır; gerçek yiyecek istemeye veya duyusal tatmaya genellenmez.","branch_kind":"collocation","branch_ref":"root_000934/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"söz istemek veya takılan imama söz vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiden konuşmasını veya anlatıyı sürdürmesini isteme."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Okuyuşta takılan imama unuttuğu bölümü söyleyip yol gösterme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen konuşma isteme ve okuyuşta takılan imama söz verme kalıplarının ortak işlevini açıklar.","boundary_detail":"Bu dal yalnızca belirtilen konuşma ve okuma kalıplarına bağlıdır; gerçek yiyecek istemeye veya duyusal tatmaya genellenmez.","branch_image_ar":"استطعام الكلام وفتح القراءة","concept_gloss":"söz istemek veya takılan imama söz vermek","contextual_glosses":[{"applicability":"İmam okuyuşta durakladığında unuttuğu sözün söylenerek devamının sağlandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Birinden konuşmasını isteme kalıbını kapsamaz.","preserves":"İmama gerekli sözü vererek yol gösterme işlevini korur."},"facet_ids":["F002"],"text":"imama sözü hatırlatmak","usage_role":"contextual"}],"definition":"Belirli söz kalıplarında birinden konuşmasını istemek veya imam okuyuşta takıldığında ona gerekli sözü söyleyerek devam etmesini sağlamak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiden konuşmasını veya anlatıyı sürdürmesini isteme."},{"facet_id":"F002","role":"associated_use","statement":"Okuyuşta takılan imama unuttuğu bölümü söyleyip yol gösterme."}],"identity_rationale":"Kaynak ifadesi iki sözlü yardım kalıbını bir araya getirir: birinden konuşmasını istemek ve okuyuşta takılan imama gerekli ifadeyi söyleyerek yol göstermek. Her ikisinde de gerçek yiyecek değil, sözün karşı taraftan sağlanması belirleyicidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"benden konuşmamı istedi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"imam okuyuşta takılırsa sözü hatırlatın"}],"lexicalization_note":"Tanım yalnızca söz isteme ve okuyana unuttuğu bölümü söyleme kalıplarını kapsar; yalın köke bağımsız bir konuşma anlamı yüklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın karışma, aynı isteme ve sağlama yapısını gerçek besinle kuran iç daldadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki kullanım yalnızca belirli sözlü yardım kalıplarına aittir; komşu dal ise gerçek besin aktarımını anlatır ve konuşma alanına taşınmaz.","focus_only":"Bu dalda sağlanan şey konuşma ya da okumayı sürdüren sözdür.","gloss":"söz sağlama ile besin sağlama","neighbor_only":"Komşu dalda sağlanan veya istenen şey gerçek yiyecek ya da besleyici içecektir.","neighbor_ref":"root_000934/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da bir kişinin ötekinden eksik olan şeyi sağlaması istenir."}],"source_phrase_ar":"استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)","source_summary":"Kaynaklar iki kalıplaşmış söz eylemini bildirir: konuşma talep etmek ve okuyuşta takılan imama gerekli ifadeyi vererek devamını açmak. Bu kullanımlarda besin aktarımı yalnızca biçimsel çağrışım düzeyindedir.","sources":["MQ","SI","MU"],"what_is_ar":"يدخل فيه استطعمني الحديث وإذا استطعمكم الإمام فأطعموه أي استفتح فافتحوا عليه أو لقنوه","what_is_not_ar":"ليس منه سؤال الطعام الحقيقي ولا الذوق الحسي"},"support_links":[]},{"boundary":"Dal, yemek yeme olayını değil geçim durumu, kazancın niteliği, konuk ağırlama bolluğu ve tahsis edilmiş gelir kaynağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B004","candidate_links":[{"candidate_id":"cand_701b35c256c4d6fca187","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"geçim, bol ikram ve tahsis edilmiş gelir","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Geçim, kazanç veya gelir bakımından iyi ve elverişli durumda olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlara ve konuklara sıkça, bolca yiyecek sunan kişi olma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kazanç yolu, arazi geliri, vergi payı veya kamu gelirinin birine geçim kaynağı olarak ayrılması."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kazancın temiz, uygun ya da kötü oluşunun nitelenmesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İyi geçim durumunu, bol yiyecek sunmayı ve kişiye ayrılan gelir kaynağını birlikte kapsayan açıklamadır.","boundary_detail":"Dal, yemek yeme olayını değil geçim durumu, kazancın niteliği, konuk ağırlama bolluğu ve tahsis edilmiş gelir kaynağını anlatır.","branch_image_ar":"رزق ومعاش وحسن حال","concept_gloss":"geçim, bol ikram ve tahsis edilmiş gelir","contextual_glosses":[{"applicability":"Bir arazi, yöre geliri veya kamu payı bir kişiye kazanç kaynağı olarak ayrıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyi durum, bol ikram ve kazancın niteliği yönlerini kapsamaz.","preserves":"Birine ayrılan gelir ve geçim kaynağı yönünü korur."},"facet_ids":["F003"],"text":"geçim payı","usage_role":"contextual"}],"definition":"Kişinin geçim ve kazanç bakımından iyi durumda veya payına düşen gelir bakımından talihli olması; ayrıca bol yiyecek sunması ya da bir gelir kaynağının birine geçim payı olarak ayrılması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Geçim, kazanç veya gelir bakımından iyi ve elverişli durumda olma."},{"facet_id":"F002","role":"specialization","statement":"İnsanlara ve konuklara sıkça, bolca yiyecek sunan kişi olma."},{"facet_id":"F003","role":"extension","statement":"Bir kazanç yolu, arazi geliri, vergi payı veya kamu gelirinin birine geçim kaynağı olarak ayrılması."},{"facet_id":"F004","role":"associated_use","statement":"Kazancın temiz, uygun ya da kötü oluşunun nitelenmesi."}],"identity_rationale":"Kaynak ifadesi iyi geçim içinde olma, rızkı açık olma, insanlara bolca yiyecek sunma ve gelir sağlayan pay ya da mülk anlamlarını ortak geçim alanında toplar. Yeme eylemi bu dalın özü değil, geçimin sağladığı maddi dayanağın arka planıdır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"geçimi yerinde"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"rızkı açık, kazançlı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"çok ikram eden"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"geçim veya kazanç kaynağı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kazancı temiz veya kötü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"araziyi birine geçim payı olarak ayırdı"}],"lexicalization_note":"Yalın nitelemeler iyi durum, rızık ve bol ikramı; kalıplaşmış kullanımlar ise kazancın niteliğini ve bir yerin gelir kaynağı olarak tahsisini gösterir.","neighbor_coverage_note":"Bütün komşular değerlendirildi; ayrılmış geçim payı komşusu, dalın gelir tahsisi ile kişisel geçim ve ikram yönleri arasındaki sınırı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme tahsis edilmiş geçim payındadır; buradaki dal kişinin iyi geçimi ve ikramcılığına kadar uzanırken komşu, ayrılan pay ve bağışın kendisine daha geniş biçimde odaklanır.","focus_only":"Bu dal iyi geçim durumunu, bol ikramı ve kazancın niteliğini de kapsar.","gloss":"geçim kaynağı ve ayrılmış pay","neighbor_only":"Komşu dal daha genel biçimde birine ayrılan pay, yiyecek veya hükümdar bağışını adlandırır.","neighbor_ref":"root_000043/B003","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişiye düşen rızık veya gelir payını anlatabilir."}],"source_phrase_ar":"رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)","source_summary":"Ortak alan kişinin geçim durumu ve elde ettiği rızıktır; bol ikram eden kişi, kazancın iyi ya da kötü niteliği ve tahsis edilmiş arazi veya gelir bu alanın farklı gerçekleşmeleridir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الطاعم حسن الحال والمطعم المرزوق والمطعام كثير القرى والطعمة مأكلة أو وجه مكسب أو ضيعة أو فيء وخراج","what_is_not_ar":"ليس منه نفس أكل الطعام إلا من جهة أنه مادة الرزق"},"support_links":["sup_26a54b72ec02ca8c0abd"]},{"boundary":"Anlam insan yiyeceğinin genel adı değildir ve kaynakta desteklenmeyen bütün nesnelerin tat kazanmasına genellenmez.","branch_kind":"collocation","branch_ref":"root_000934/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"olgunlaşıp tat kazanmak","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Meyvenin olgunlaşıp yenilebilir ve belirgin bir tat kazanması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hurma ağacı veya hurma meyvesi olgunlaştığında tadı belirginleşir."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Meyvenin olgunlaşmasını ve belirli süt kalıbındaki tat kazanımını ortak sonuç üzerinden anlatır.","boundary_detail":"Anlam insan yiyeceğinin genel adı değildir ve kaynakta desteklenmeyen bütün nesnelerin tat kazanmasına genellenmez.","branch_image_ar":"إدراك الثمر وأخذ الطعم","concept_gloss":"olgunlaşıp tat kazanmak","contextual_glosses":[{"applicability":"Hurma ağacı veya başka bir meyvenin yenilecek olgunluğa eriştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tulumdaki sütün hoş tat kazanması kullanımını kapsamaz.","preserves":"Meyvenin olgunlaşıp tat kazanma sürecini korur."},"facet_ids":["F001"],"text":"meyvesi olgunlaşmak","usage_role":"contextual"}],"definition":"Meyvenin, özellikle hurma ağacının ürünü olgunlaşarak yenilebilir ve belirgin bir tat kazanmış duruma gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Meyvenin olgunlaşıp yenilebilir ve belirgin bir tat kazanması."},{"facet_id":"F002","role":"specialization","statement":"Hurma ağacı veya hurma meyvesi olgunlaştığında tadı belirginleşir."}],"identity_rationale":"Kaynak ifadesi genel olarak her şeyin tadının bulunmasını değil, hurma ağacı veya meyvenin olgunlaşıp belirgin tat kazanmasını bildirir. Bu nedenle dal, meyvenin olgunlaşması ve tat kazanmasıyla sınırlı biçimde yeniden çerçevelenmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ağacın meyvesi olgunlaşıp tat kazandı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tulumda hoş tat kazanmış süt"}],"lexicalization_note":"Tanım yalnızca meyve veya hurma ağacının olgunlaşıp tat kazanması kalıbına bağlıdır.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel meyve olgunlaşması komşusu, bu dalın tat kazanma koşulunu en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Meyve bağlamında büyük ölçüde örtüşürler; buradaki dalın ayırıcı yanı olgunluğun tat kazanma olarak kavranmasıdır.","focus_only":"Bu dal meyvenin olgunlaşmasını özellikle yenilebilir tat kazanması bakımından kurar.","gloss":"tat kazanma ile genel olgunlaşma","neighbor_only":"Komşu dal meyve ve ağacın olgunlaşmasını tat vurgusu olmadan daha genel biçimde anlatır.","neighbor_ref":"root_001699/B001","relation_type":"near_synonym","shared_zone":"Her iki dal meyvenin olgunluğa erişmesini anlatır."}],"source_phrase_ar":"للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)","source_summary":"Kaynakların ortak çekirdeği meyvenin, özellikle hurma meyvesinin, olgunlaşıp tat kazanmasıdır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه أطعمت النخلة أو الثمرة إذا أدرك ثمرها أو أخذت الطعم، وكل شيء وجد طعمه، واللبن المطعم والشجر المثمر","what_is_not_ar":"ليس منه طعام الإنسان مطلقا ولا الرزق المالي"},"support_links":[]},{"boundary":"Genel insan besleme anlamı ile hayvanın semizliği bu av alanına dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"avı kazandıran araç, uzuv veya kişi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avı ele geçirerek avcıya yiyecek veya kazanç sağlayan araç olma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Avcı kuşun avı kavramaya yarayan öndeki kalın parmağı."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Avda sıkça başarı gösteren ve avdan yana payı açık kişi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Avın ele geçirilmesini sağlayan yay ve kuş parmağı ile avda başarılı kişiyi ortak işlev altında kapsar.","boundary_detail":"Genel insan besleme anlamı ile hayvanın semizliği bu av alanına dahil değildir.","branch_image_ar":"آلة الصيد التي تطعم صاحبها","concept_gloss":"avı kazandıran araç, uzuv veya kişi","contextual_glosses":[{"applicability":"Avı vurarak sahibine yiyecek veya kazanç sağlayan yayın nitelenmesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kuş parmağını ve avda talihli kişi anlamını kapsamaz.","preserves":"Yayın avı sahibine kazandırma işlevini korur."},"facet_ids":["F001"],"text":"av getiren yay","usage_role":"contextual"}],"definition":"Avı yakalayıp sahibine kazandıran yay veya avcı kuş uzvu; ayrıca avda sıkça başarılı olup avdan pay alan kişi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avı ele geçirerek avcıya yiyecek veya kazanç sağlayan araç olma."},{"facet_id":"F002","role":"specialization","statement":"Avcı kuşun avı kavramaya yarayan öndeki kalın parmağı."},{"facet_id":"F003","role":"extension","statement":"Avda sıkça başarı gösteren ve avdan yana payı açık kişi."}],"identity_rationale":"Kaynak ifadesi yalnızca bir av aracını değil, avı sahibine kazandıran yayı, avcı kuşun öndeki kalın parmağını ve avdan yana talihli kişiyi birlikte verir. Dal bu yüzden tek bir araç olarak değil, avı ele geçirmeye ve avdan pay almaya yarayan araç, uzuv ve kişi nitelemeleri olarak kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"av getiren yay"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"avcı kuşun öndeki kalın parmağı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"avdan yana talihli, avı bol"}],"lexicalization_note":"Tanım yay ve av başarısı kalıplarını ayrı tutarken avcı kuşun parmak adını yalın, bedensel bir alt anlam olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel avlanma dalı, buradaki işlevsel araç ve başarı nitelemelerinin dar kapsamını en iyi ortaya koyar.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Buradaki dar nitelemeler avı sahibine kazandırma sonucuna bağlıdır; komşu ise avlanma etkinliğinin ve nesnelerinin genel söz varlığıdır.","focus_only":"Bu dal avı kazandıran belirli yay, kuş parmağı ve başarılı avcı nitelemelerini adlandırır.","gloss":"av başarısı ile genel avlanma","neighbor_only":"Komşu dal avlanma eylemini, avı, av aracını ve av köpeğini genel bir alan olarak kapsar.","neighbor_ref":"root_000896/B001","relation_type":"same_field","shared_zone":"Her iki dal avın ele geçirilmesi ve av araçları alanındadır."}],"source_phrase_ar":"قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)","source_summary":"Kaynaklar yayı, kuşun öndeki avcı parmağını ve avda başarılı kişiyi avın sahibine kazandırılması bağıyla birleştirir. Bunlar sırasıyla araç, beden bölümü ve kişi niteliğidir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القوس المطعمة والجوارح أو الإصبع المطعمة وما يطعم صاحبه الصيد أو يكون مرزوقا منه","what_is_not_ar":"ليس منه الإطعام الآدمي العام ولا سمن الحيوان"},"support_links":[]},{"boundary":"Dal genel tat alma veya her türlü beden yağı değil, hayvanın belirli derecedeki semizliği ve ilikteki yağ belirtisiyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_000934/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"ilikte yağı beliren, biraz semiz hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvanın iliğinde yağ tadı ve belirtisi bulunması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanın biraz semiz veya zayıfla semiz arasında olması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın ilik yağını ve zayıfla semiz arasındaki beden durumunu birlikte ifade eder.","boundary_detail":"Dal genel tat alma veya her türlü beden yağı değil, hayvanın belirli derecedeki semizliği ve ilikteki yağ belirtisiyle sınırlıdır.","branch_image_ar":"سمن الحيوان وطعم الشحم","concept_gloss":"ilikte yağı beliren, biraz semiz hayvan","contextual_glosses":[{"applicability":"Koyun veya devenin zayıfla tam semiz arasında bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İlikte yağ tadı bulunması ölçütünü açıkça göstermez.","preserves":"Hayvanın kısmi semizlik derecesini korur."},"facet_ids":["F002"],"text":"biraz semiz","usage_role":"contextual"}],"definition":"Bir hayvanın iliğinde yağ tadı bulunacak kadar semiz olması veya zayıf ile tam semiz arasında bir miktar yağ tutmuş bulunması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvanın iliğinde yağ tadı ve belirtisi bulunması."},{"facet_id":"F002","role":"specialization","statement":"Hayvanın biraz semiz veya zayıfla semiz arasında olması."}],"identity_rationale":"Kaynak ifadesi hayvanın iliğinde yağ tadı bulunmasını ve koyun, deve ya da kesimlik hayvanın bir miktar semiz veya zayıfla semiz arasında olmasını bildirir. Duyusal tat burada bağımsız amaç değil, beden yağının saptanma belirtisidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"iliğinde yağ bulunan deve"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"biraz semiz, orta yağlı"}],"lexicalization_note":"Tanım hayvanın ilik ve beden yağından anlaşılan semizlik derecesini yalın dal anlamı olarak verir; başka alanlardaki özel kalıpları içeri almaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel yağlılık komşusu, bu dalın hayvana ve ilik belirtisine bağlı dar sınırını en iyi açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam hayvanla ve belirli bir semizlik derecesiyle sınırlıdır; komşu ise bedenin genel yağlanmasını daha geniş katılımcı kapsamıyla anlatır.","focus_only":"Bu dal hayvana özgüdür ve kısmi semizliği ilikteki yağ belirtisiyle birlikte tanımlar.","gloss":"kısmi hayvan semizliği ve genel yağlılık","neighbor_only":"Komşu dal insanı veya hayvanı kapsayan genel yağlılık ve bedenin yağla dolması anlamındadır.","neighbor_ref":"root_000779/B001","relation_type":"near_synonym","shared_zone":"Her iki dal bedende yağ bulunması ve semizlik alanında örtüşür."}],"source_phrase_ar":"المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)","source_summary":"Kaynaklar hayvandaki semizliği, ilikte algılanan yağ belirtisi ve zayıflıkla tam semizlik arasındaki beden durumu üzerinden tanımlar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه المطعم من الإبل إذا وجد في مخه طعم الشحم وشاة أو ناقة أو جزور طعوم أو طعيم في السمن","what_is_not_ar":"ليس منه الطعم بمعنى الذوق إلا باعتبار أثر السمن"},"support_links":[]},{"boundary":"Bu dal duyusal lezzeti veya yiyeceği değil, belirli kişi niteleme kalıplarında akıl, değer ve düzelmeye açıklık değerlendirmesini anlatır.","branch_kind":"collocation","branch_ref":"root_000934/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"akıl, değer ve düzelmeye açıklık niteliği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Akıl, sağlam yargı ve ölçülü karar gücü taşıma."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıpta akıl, devinim, değer veya dolgunluktan yoksun olma."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Öğüt, eğitim veya düzeltmeden yararlanmayıp uslanmama."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Olumlu ve olumsuz kişi niteleme kalıplarındaki değerlendirme eksenini birlikte gösterir.","boundary_detail":"Bu dal duyusal lezzeti veya yiyeceği değil, belirli kişi niteleme kalıplarında akıl, değer ve düzelmeye açıklık değerlendirmesini anlatır.","branch_image_ar":"طعم العقل والقيمة","concept_gloss":"akıl, değer ve düzelmeye açıklık niteliği","contextual_glosses":[{"applicability":"Kişinin akıllı ve sağlam yargılı olduğunun olumlu biçimde belirtildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Olumsuz değer, devinim ve eğitilemezlik kullanımlarını kapsamaz.","preserves":"Akıl ve sağlam yargı niteliğini korur."},"facet_ids":["F001"],"text":"aklı başında","usage_role":"contextual"}],"definition":"Belirli kişi nitelemelerinde akıl, sağlam yargı veya dikkate değer bir nitelik taşıma; olumsuz biçimlerde bunlardan yoksun, cılız, devinimsiz ya da düzeltilemez olma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Akıl, sağlam yargı ve ölçülü karar gücü taşıma."},{"facet_id":"F002","role":"source_variant","statement":"Olumsuz kalıpta akıl, devinim, değer veya dolgunluktan yoksun olma."},{"facet_id":"F003","role":"associated_use","statement":"Öğüt, eğitim veya düzeltmeden yararlanmayıp uslanmama."}],"identity_rationale":"Kaynak ifadesi olumlu olarak akıl ve sağlam yargıyı, olumsuz kalıplarda ise akılsızlık, devinimsizlik, değersizlik, eğitilemezlik veya cılızlığı bildirir. Dalın 'akıl ve değer' çerçevesi kullanılabilir, ancak olumsuz biçimlerin her zaman yalnızca akıl yokluğu demediği açıkça korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"akıllı ve sağlam yargılı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"aklı, devinimi veya değeri yok"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"terbiye kabul etmez, uslanmaz"}],"lexicalization_note":"Anlam yalnızca akıllı olma, akıl ya da değer yokluğu ve terbiyeden yararlanmama bildiren kişi niteleme kalıplarında geçerlidir.","neighbor_coverage_note":"Adayların tümü değerlendirildi; engelleyici akıl komşusu ortak çekirdeği gösterirken bu dalın değer ve eğitilebilirlik uzantılarını ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme akıl niteliğindedir; burada anlam olumlu ve olumsuz kişi değerlendirmelerine yayılırken komşuda aklın davranışı dizginleyen işlevi belirleyicidir.","focus_only":"Bu dal kalıplaşmış kişi nitelemelerinde değer, devinim ve eğitilebilirliği de akılla birlikte değerlendirir.","gloss":"kişi değeri ile engelleyici akıl","neighbor_only":"Komşu dal aklı özellikle kişiyi uygunsuz davranıştan alıkoyan iç engel olarak tanımlar.","neighbor_ref":"root_000296/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin akıllı ve ölçülü oluşunu anlatabilir."}],"source_phrase_ar":"ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)","source_summary":"Kaynaklar kişi hakkında olumlu bir akıl ve yargı niteliği ile bunun olumsuzlanmasını verir; olumsuzlama bağlama göre akılsızlık, devinimsizlik, değersizlik, cılızlık veya eğitilemezlik biçiminde açılır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه ذو طعم أي ذو عقل وحزم، وما بفلان طعم أي لا عقل ولا حراك أو لا قيمة، ولا يطعم أي لا يتأدب ولا ينجع فيه الإصلاح","what_is_not_ar":"ليس منه حسن الطعم الحسي ولا الطعام"},"support_links":[]},{"boundary":"Ağız bölümü ile koşma talebi ayrı tutulur; yiyecek, kuş ayağı veya atın fiilen koşması bu dalın doğrudan anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000934/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"atın ağız bölümü ve koşma talebi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Atın burun altı ile dudak uçları arasındaki ağız bölümü."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Attan hızlanmasını veya koşmasını isteme."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"At anatomisine ait adlandırmayı ve yalnızca ata yöneltilen koşma isteğini ayrı yönleriyle kapsar.","boundary_detail":"Ağız bölümü ile koşma talebi ayrı tutulur; yiyecek, kuş ayağı veya atın fiilen koşması bu dalın doğrudan anlamı değildir.","branch_image_ar":"مستطعم الفرس وطلب جريه","concept_gloss":"atın ağız bölümü ve koşma talebi","contextual_glosses":[{"applicability":"Binicinin attan koşmasını veya hızlanmasını istediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Atın ağız bölümü adlandırmasını kapsamaz.","preserves":"Ata yöneltilen koşma talebini korur."},"facet_ids":["F002"],"text":"atı koşturmaya çağırmak","usage_role":"contextual"}],"definition":"Atın burun altından dudaklarının uçlarına kadar uzanan ağız bölümü; ayrıca belirli bir kalıpta attan koşmasını isteme.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Atın burun altı ile dudak uçları arasındaki ağız bölümü."},{"facet_id":"F002","role":"associated_use","statement":"Attan hızlanmasını veya koşmasını isteme."}],"identity_rationale":"Kaynak ifadesi atın burun altından dudak uçlarına uzanan ağız bölümünü ve attan koşmasını isteme eylemini ayrı fakat aynı at alanında verir. Dalın kimliği bu iki alt alanı kaynaştırmadan birlikte koruduğunda kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"atın burun altı ve dudak çevresi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"attan koşmasını istedi"}],"lexicalization_note":"Atın ağız bölümü yalın adlandırma, koşmasını isteme ise yalnızca belirtilen kalıp olarak tanımlanır; ikisi tek bir eylem anlamında birleştirilmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; atın fiili koşusunu anlatan komşu, bu dalın koşmayı isteme yönünü en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Burada eylem binicinin ata yönelttiği taleptir; komşuda ise atın gerçekleştirdiği hızlı koşu ve bunun yere etkisi öne çıkar.","focus_only":"Bu dal koşmanın kendisini değil, attan koşmasını istemeyi ve ayrıca atın ağız bölümünü bildirir.","gloss":"koşma talebi ile atın koşusu","neighbor_only":"Komşu dal atın fiili koşusunu, hızını ve toynağıyla yeri güçlü biçimde eşmesini anlatır.","neighbor_ref":"root_001599/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal atın koşması çevresindeki aynı hareket sahnesine katılır."}],"source_phrase_ar":"مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)","source_summary":"Kaynaklar atın ağız ve dudak çevresindeki belirli bölgesini adlandırır; ayrıca ayrı bir söz kalıbında binicinin attan koşmasını istemesini bildirir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه مستطعم الفرس وهو ما تحت مرسنه إلى جحافله أو جحافله، واستطعمت الفرس إذا طلبت جريه","what_is_not_ar":"ليس منه الطعام ولا مطعمة الطائر"},"support_links":[]},{"boundary":"Anlam besleme değildir; yalnızca eklenen dalın birleşmeyi kabul etmesi ve gözün içine giren yabancı cismi tutması kalıplarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000934/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"eklenen şeyin tutması","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka ağaçtan eklenen dalın ana dalla birleşmeyi kabul edip tutması."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göze giren küçük yabancı cismin göz tarafından tutulması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Aşı dalının birleşmesi ve göze giren yabancı cismin kalması kullanımlarındaki ortak tutunma sonucunu açıklar.","boundary_detail":"Anlam besleme değildir; yalnızca eklenen dalın birleşmeyi kabul etmesi ve gözün içine giren yabancı cismi tutması kalıplarıyla sınırlıdır.","branch_image_ar":"إطعام الغصن وقبول الوصل","concept_gloss":"eklenen şeyin tutması","contextual_glosses":[{"applicability":"Başka ağaçtan eklenen dalın ana dala kaynayıp gelişebildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Göze giren yabancı cismin gözde kalması kullanımını kapsamaz.","preserves":"Eklenen dalın birleşmeyi kabul edip tutmasını korur."},"facet_ids":["F001"],"text":"aşı tutmak","usage_role":"contextual"}],"definition":"Bir ağaca eklenen başka bir dalın birleşip tutması; ayrıca göze giren küçük yabancı cismin gözde kalması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka ağaçtan eklenen dalın ana dalla birleşmeyi kabul edip tutması."},{"facet_id":"F002","role":"source_variant","statement":"Göze giren küçük yabancı cismin göz tarafından tutulması."}],"identity_rationale":"Kaynak ifadesi iki kabul ilişkisini birlikte verir: bir dala başka ağaçtan parça eklenmesi ve birleşmenin tutması, ayrıca göze çöp girip gözün onu içinde tutması. Dalın dal aşılama çerçevesi kullanılabilir, ancak gözde yabancı cismin tutunması bağımsız ikinci kalıp olarak açıkça korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dala aşı yaptı ve aşı tuttu"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gözüne küçük bir yabancı cisim girdi"}],"lexicalization_note":"Tanım, dal aşılama ve göze yabancı cisim girme kalıplarındaki kabul veya tutunma sonucuna bağlıdır; yalın köke genel birleşme anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel birleştirme komşusu, bu dalın tutunma ve kabul sonucu gerektiren dar yapısını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Burada eklenen unsurun alıcıda tutunması ve kabul edilmesi gerekir; komşuda ise genel katma veya toplama yeterlidir ve böyle bir sonuç koşulu yoktur.","focus_only":"Bu dal yalnızca aşı dalının veya gözdeki yabancı cismin tutunması sonucuna bağlıdır.","gloss":"tutunan ek ile genel birleştirme","neighbor_only":"Komşu dal nesneleri genel olarak birbirine katma, toplama ve birlikte bulundurma eylemlerini kapsar.","neighbor_ref":"root_000915/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal ayrı bir şeyin başka bir şeye katılması sahnesini içerir."}],"source_phrase_ar":"أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)","source_summary":"Tek kaynak, eklenen dalın ağaçta tutması ile küçük bir yabancı cismin gözde kalmasını kabul ve tutunma sonucu altında yan yana getirir.","sources":["TA"],"what_is_ar":"يدخل فيه إطعام الغصن إذا وصل به غصن من غير شجره فقبل الوصل، وإطعام العين قذى فطعمته","what_is_not_ar":"ليس منه الإطعام بمعنى التغذية"},"support_links":[]},{"boundary":"Anlam yalnızca belirtilen kalıpta bir şeye gücü yetmeyi anlatır; genel egemenlik, mülkiyet veya duyusal tat bu dala eklenmez.","branch_kind":"collocation","branch_ref":"root_000934/B011","candidate_links":[{"candidate_id":"cand_fe03da26775d6cb2a540","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"gücü yetmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi yapabilecek ya da bir şeyin üstesinden gelebilecek güce sahip olma."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta verilen kalıpta bir işi yapabilme veya bir şeyin üstesinden gelebilme anlamını tam karşılar.","boundary_detail":"Anlam yalnızca belirtilen kalıpta bir şeye gücü yetmeyi anlatır; genel egemenlik, mülkiyet veya duyusal tat bu dala eklenmez.","branch_image_ar":"القدرة على الشيء","concept_gloss":"gücü yetmek","contextual_glosses":[{"applicability":"Gücün belirli bir işi başarmaya veya engeli aşmaya yöneldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir şeye yeten güç ve başarı imkanını korur."},"facet_ids":["F001"],"text":"üstesinden gelebilmek","usage_role":"contextual"}],"definition":"Belirli bir söz kalıbında bir şeyi yapmaya veya onun üstesinden gelmeye gücü yetmek.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi yapabilecek ya da bir şeyin üstesinden gelebilecek güce sahip olma."}],"identity_rationale":"Kaynak ifadesi belirli bir edatlı kalıpta kişinin bir şey üzerinde gücü bulunmasını ve onu yapabilmesini doğrudan bildirir. Tatma ve yeme alanlarıyla biçim ortaklığı dışında bir anlam bağı kurulmaz.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"ona gücü yetti"}],"lexicalization_note":"Tanım yalnızca bir şey üzerinde gücü bulunma kalıbına bağlıdır ve yalın köke genel bir yeterlik anlamı vermez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel yeterlik komşusu, anlam yakınlığını ve bu dalın kalıba bağlı olma sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Anlamsal çekirdek büyük ölçüde aynıdır; buradaki dalın sınırı tek bir kalıba bağlı olması, komşunun ise genel yeterlik alanını kapsamasıdır.","focus_only":"Bu dal yeterliği yalnızca belirli bir edatlı söz kalıbında ve yöneldiği şeyle birlikte ifade eder.","gloss":"kalıba bağlı ve genel yeterlik","neighbor_only":"Komşu dal yapabilme ve güç yetirme anlamını daha genel söz biçimleriyle taşır.","neighbor_ref":"root_000048/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bir işi yapabilecek güç ve yeterliğe sahip olmayı anlatır."}],"source_phrase_ar":"الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)","source_summary":"Tek kaynak bu kullanımı, belirli bir kalıp içinde bir şeye gücü yetme ve onun üzerinde yeterli olma anlamıyla verir.","sources":["TA"],"what_is_ar":"يدخل فيه الطعم بمعنى القدرة، طعمت عليه أي قدرت عليه","what_is_not_ar":"ليس منه الذوق ولا الأكل"},"support_links":["sup_2e1fcc8a54c16e397523"]},{"boundary":"Dal genel tutma eylemini değil, boğma ve kavga sırasında boğazı kavrayıp sıkma hareketini anlatır.","branch_kind":"collocation","branch_ref":"root_000934/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"boğazından yakalayıp sıkmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin boğazını elle kavrayıp sıkarak nefesini baskılama."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemin yalnızca boğma veya dövüş bağlamında gerçekleştirilmesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Boğma ya da dövüşte boğazın kavranıp baskı altına alındığı hareketi doğrudan karşılar.","boundary_detail":"Dal genel tutma eylemini değil, boğma ve kavga sırasında boğazı kavrayıp sıkma hareketini anlatır.","branch_image_ar":"الأخذ بالمطعمة عند الخنق","concept_gloss":"boğazından yakalayıp sıkmak","contextual_glosses":[{"applicability":"Kavga sırasında karşı tarafın boğazının elle kavrandığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıkmanın nefesi baskılama sonucunu zorunlu olarak belirtmez.","preserves":"Boğazı doğrudan kavrama hareketini korur."},"facet_ids":["F001","F002"],"text":"boğazına sarılmak","usage_role":"contextual"}],"definition":"Boğma veya dövüş sırasında bir kişiyi boğazından kavrayıp baskı uygulayarak sıkmak.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin boğazını elle kavrayıp sıkarak nefesini baskılama."},{"facet_id":"F002","role":"specialization","statement":"Eylemin yalnızca boğma veya dövüş bağlamında gerçekleştirilmesi."}],"identity_rationale":"Kaynak ifadesi bir kişiyi boğma veya dövüş sırasında boğazından yakalayıp sıkmayı, yalnızca bu şiddet bağlamına özgü bir kalıpla bildirir. Beden bölümü, avcı kuşun parmağı ya da geçim anlamlarıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"boğazından yakalayıp sıktı"}],"lexicalization_note":"Tanım yalnızca boğma veya dövüş bağlamındaki boğazdan yakalama kalıbıyla sınırlıdır; yalın bir tutma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel boğma komşusu, bu dalın boğazdan elle yakalama ve kavga koşulunu en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam belirli bir elle yakalama kalıbı ve şiddet bağlamıdır; komşu dal yapanı, aracı ve kendiliğinden boğulmayı da içeren daha geniş boğma alanıdır.","focus_only":"Bu dal boğma veya kavga sırasında boğazı elle kavrayıp sıkma kalıbıyla sınırlıdır.","gloss":"boğazdan yakalama ve genel boğma","neighbor_only":"Komşu dal boğazı elle veya araçla sıkmayı, boğulmayı ve boğma aracını genel olarak kapsar.","neighbor_ref":"root_000444/B001","relation_type":"near_synonym","shared_zone":"Her iki dal boyun veya boğaza baskı uygulayarak boğma alanında örtüşür."}],"source_phrase_ar":"أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)","source_summary":"Tek kaynak kalıbı, boğma veya kavga sırasında karşı tarafın boğazını yakalayıp sıkma eylemine özgüler.","sources":["TA"],"what_is_ar":"يدخل فيه أخذ بمطعمة فلان أي أخذ بحلقه يعصره عند الخنق والقتال","what_is_not_ar":"ليس منه مطعمة الجارحة ولا المطعم بمعنى الرزق"},"support_links":[]},{"boundary":"Dal genel öpme, sarılma veya ağızla yeme anlamına değil, ağızların doğrudan birbirine geçirilmesi biçimindeki karşılıklı temasa bağlıdır.","branch_kind":"bare","branch_ref":"root_000934/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"ağız ağıza temas etmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki tarafın ağızlarını doğrudan ve karşılıklı olarak birbirine geçirmesi."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güvercinlerin öpüşmeye benzeyen ağız teması kurması."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağızların karşılıklı olarak birbirine değdirilip geçirilmesi biçimindeki bedensel teması açıklar.","boundary_detail":"Dal genel öpme, sarılma veya ağızla yeme anlamına değil, ağızların doğrudan birbirine geçirilmesi biçimindeki karşılıklı temasa bağlıdır.","branch_image_ar":"التطاعم بالفم","concept_gloss":"ağız ağıza temas etmek","contextual_glosses":[{"applicability":"Temasın öpüşme benzeri karşılıklı bir hareket olarak anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":"Türkçedeki öpüşme sözü, kaynakta zorunlu olmayan duygusal veya insani bir çağrışım ekleyebilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Ağızların karşılıklı ve doğrudan temasını korur."},"facet_ids":["F001","F002"],"text":"ağız ağıza öpüşmek","usage_role":"contextual"}],"definition":"İki canlının ağızlarını doğrudan birbirine değdirip birinin ağzını ötekininkine sokması; öpüşmeye benzeyen karşılıklı ağız teması.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki tarafın ağızlarını doğrudan ve karşılıklı olarak birbirine geçirmesi."},{"facet_id":"F002","role":"example","statement":"Güvercinlerin öpüşmeye benzeyen ağız teması kurması."}],"identity_rationale":"Kaynak ifadesi iki canlının ağızlarını birbirine değdirip birinin ağzını ötekininkine sokmasını, güvercin davranışıyla örneklenen öpüşme benzeri bir temas olarak verir. Burada ağızla yiyecek tüketme değil, karşılıklı bedensel temas esastır.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"ağız ağıza temas etme"}],"lexicalization_note":"Tanım ağızların karşılıklı doğrudan temasını yalın dal anlamı olarak korur ve yiyecek tüketme alanını dışarıda bırakır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel öpme komşusu, bu dalın karşılıklı ağız ağıza temas koşulunu en belirgin biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Buradaki anlam karşılıklı ağız ağıza geçme biçimiyle daralır; komşu dal ise temasın bu özel biçimini zorunlu kılmadan genel öpmeyi anlatır.","focus_only":"Bu dal ağızların karşılıklı olarak birbirine geçirilmesini ve iki taraflı teması gerektirir.","gloss":"ağız ağıza temas ve genel öpme","neighbor_only":"Komşu dal tek yönlü veya karşılıklı olabilen genel öpme eylemini kapsar.","neighbor_ref":"root_001198/B006","relation_type":"near_synonym","shared_zone":"Her iki dal ağız çevresindeki öpüşme benzeri bedensel teması anlatabilir."}],"source_phrase_ar":"التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)","source_summary":"Tek kaynak ağızların birbirine geçirilmesi biçimindeki karşılıklı teması tanımlar ve bunu güvercinlerin öpüşmeye benzeyen davranışıyla örnekler.","sources":["TA"],"what_is_ar":"يدخل فيه التطاعم أي إدخال الفم في الفم كما يفعل الحمام عند التقبيل","what_is_not_ar":"ليس منه تناول الطعام بالفم"},"support_links":[]},{"boundary":"Dal yalnızca oluşumun ardışık düzenini anlatır; genel zaman sürekliliğine, sonsuzluğa veya yiyecek alanına taşınmaz.","branch_kind":"collocation","branch_ref":"root_000934/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","surface_ar":"طَعَامِ"}],"gloss":"oluşumu ardışık olmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oluşumun parçalarının kesintisiz bir sıra içinde birbirini izlemesi."}}],"root_ar":"ط ع م","root_id":"root_000934","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın yapısal oluşumunda parçaların birbirini izlediği düzeni tam olarak açıklar.","boundary_detail":"Dal yalnızca oluşumun ardışık düzenini anlatır; genel zaman sürekliliğine, sonsuzluğa veya yiyecek alanına taşınmaz.","branch_image_ar":"تتابع الخلق","concept_gloss":"oluşumu ardışık olmak","contextual_glosses":[{"applicability":"Oluşumun evre veya parçalarının sırayla meydana geldiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların sırayla meydana gelmesi ve takip ilişkisini korur."},"facet_ids":["F001"],"text":"birbiri ardınca oluşmak","usage_role":"contextual"}],"definition":"Bir varlığın oluşumunun veya yapısının parçalarının birbirini izleyerek ardışık ve bağlantılı biçimde meydana gelmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oluşumun parçalarının kesintisiz bir sıra içinde birbirini izlemesi."}],"identity_rationale":"Kaynak ifadesi oluşumun veya yaratılışın bölümlerinin birbirini izleyerek ardışık biçimde kurulmasını bildirir. Süreklilik ya da sonsuzluk değil, meydana gelişteki sıra ve takip ilişkisi belirleyicidir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"oluşumu birbirini izleyen bölümlerden kurulu"}],"lexicalization_note":"Tanım yalnızca oluşum veya yaratılışın birbirini izleyen bölümler halinde kurulmasını bildiren kalıba bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ardışıklık komşusu, bu dalın oluşum yapısına bağlı özel kapsamını en açık biçimde sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ardışıklık çekirdeği ortaktır; buradaki dal bunu oluşum yapısına bağlar, komşu ise her türlü nesne ve eylem dizisine uygulanabilen genel bir anlam taşır.","focus_only":"Bu dal ardışıklığı bir varlığın oluşumuna veya yapısının kurulmasına özgüler.","gloss":"oluşumdaki ve genel ardışıklık","neighbor_only":"Komşu dal nesnelerin veya eylemlerin ara vermeden art arda gelmesini genel olarak kapsar.","neighbor_ref":"root_000175/B004","relation_type":"near_synonym","shared_zone":"Her iki dal parçaların ya da olayların birbirini aralıksız izlemesini anlatır."}],"source_phrase_ar":"متطاعم الخلق أي متتابع الخلق (tahdhib)","source_summary":"Tek kaynak bu kalıbı, oluşumun parçalarının birbiri ardından gelmesi ve yapının ardışık biçimde kurulması olarak açıklar.","sources":["TA"],"what_is_ar":"يدخل فيه متطاعم الخلق أي متتابع الخلق","what_is_not_ar":"ليس منه الطعام ولا الطعم الحسي"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:18:1"],"branch_refs":[],"candidate_id":"cand_bc394be5c7a95cec7b75","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:1:compact-negative-opening","source_type":"word_analysis","support_ids":["sup_46d08bd1786f738146ba","sup_fe10234f9dc0c2fa0bd5"],"title":"compact negative opening","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:1","qac_refs":["89:18:1:1"],"status":"accepted"}},{"anchor_refs":["89:18:1"],"branch_refs":[],"candidate_id":"cand_0985752508a97d54551e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:1:coordinated-negated-charge","source_type":"word_analysis","support_ids":["sup_7433e2b30982638f2889","sup_fe10234f9dc0c2fa0bd5"],"title":"coordinated negated charge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:1","qac_refs":["89:18:1:1"],"status":"accepted"}},{"anchor_refs":["89:18:1"],"branch_refs":[],"candidate_id":"cand_03a1e0f90e494cf85328","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:1:register-widening","source_type":"word_analysis","support_ids":["sup_187b553d24c14ff6f9d2","sup_fe10234f9dc0c2fa0bd5"],"title":"care widens into advocacy","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:1","qac_refs":["89:18:1:1"],"status":"accepted"}},{"anchor_refs":["89:18:2"],"branch_refs":[],"candidate_id":"cand_c7cdbf1a171bb159ed4e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:2:coupled-opening","source_type":"word_analysis","support_ids":["sup_ca81df6a363e02f09ccf","sup_fd51259b47c332d3fc53"],"title":"denial coupled to continuation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:2","qac_refs":["89:18:1:2"],"status":"accepted"}},{"anchor_refs":["89:18:2"],"branch_refs":[],"candidate_id":"cand_d9231a3ffbdcd4ad460b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:2:scope-over-provision","source_type":"word_analysis","support_ids":["sup_5408cf130a690a4aa425","sup_ca81df6a363e02f09ccf"],"title":"negation reaches provision","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:2","qac_refs":["89:18:1:2"],"status":"accepted"}},{"anchor_refs":["89:18:2"],"branch_refs":[],"candidate_id":"cand_4e7b5a4515ee32a0f1d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:2:standing-negated-practice","source_type":"word_analysis","support_ids":["sup_ca81df6a363e02f09ccf","sup_fb003661aa60648ab05e"],"title":"standing negated practice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:2","qac_refs":["89:18:1:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_93847143877a1769d762","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:audible-pressure","source_type":"word_analysis","support_ids":["sup_6727a3a7c67cf06e850b","sup_bd5a82cf7e55b3f32787"],"title":"audible pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_38cc2c93ab8834654329","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:form-and-variant-pressure","source_type":"word_analysis","support_ids":["sup_1fb949d1178fa6db1b9b","sup_bd5a82cf7e55b3f32787"],"title":"collective form with variant pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_0626bf0be6076004bc3a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:negated-plural-mobilization","source_type":"word_analysis","support_ids":["sup_708747bdf79237675762","sup_bd5a82cf7e55b3f32787"],"title":"negated plural mobilization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_f92c44fcf383c395aec8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:omitted-urged-object","source_type":"word_analysis","support_ids":["sup_14375f4364b760ab5ad2","sup_bd5a82cf7e55b3f32787"],"title":"unnamed urged object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_ce3de74a783b193260d1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:parallel-and-sequence","source_type":"word_analysis","support_ids":["sup_bd5a82cf7e55b3f32787","sup_c5e95fdaaf361fb28673"],"title":"parallel social failure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:3"],"branch_refs":[],"candidate_id":"cand_5a6082bb520e2d656f17","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:3:poor-food-judgment-field","source_type":"word_analysis","support_ids":["sup_bd5a82cf7e55b3f32787","sup_dd3b0c35b801b928b870"],"title":"poor-food judgment field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:3","qac_refs":["89:18:2:1","89:18:2:2"],"status":"accepted"}},{"anchor_refs":["89:18:4"],"branch_refs":[],"candidate_id":"cand_6226d1ed48f1cf4d9a43","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:4:governed-pressure-point","source_type":"word_analysis","support_ids":["sup_78cba4c789e228205aef","sup_aeb253d456dfa01cd8b4"],"title":"governed pressure-point","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:4","qac_refs":["89:18:3:1"],"status":"accepted"}},{"anchor_refs":["89:18:4"],"branch_refs":[],"candidate_id":"cand_31aa0e4c4bfd2c6687d1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:4:hinge-before-completion","source_type":"word_analysis","support_ids":["sup_3215fcab52f3e7eb5dce","sup_78cba4c789e228205aef"],"title":"hinge before completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:4","qac_refs":["89:18:3:1"],"status":"accepted"}},{"anchor_refs":["89:18:4"],"branch_refs":[],"candidate_id":"cand_395878646673a8fc15a0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:18:4:obligation-pressure","source_type":"word_analysis","support_ids":["sup_78cba4c789e228205aef","sup_7b9ed70df6cfbb46a082"],"title":"obligation pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:4","qac_refs":["89:18:3:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_7c602472b2d70be25d1b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:audible-materiality","source_type":"word_analysis","support_ids":["sup_772aee09f7ce5335998c","sup_f8181996b8d3e053a899"],"title":"audible materiality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_5f4c0acc5aea3966b9a5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:double-dependency-construct","source_type":"word_analysis","support_ids":["sup_4e7c56fe88e80cce1f60","sup_772aee09f7ce5335998c"],"title":"double dependency construct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_f102e323a03497a3b169","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:embodied-food-field","source_type":"word_analysis","support_ids":["sup_772aee09f7ce5335998c","sup_8559148302d974677b31"],"title":"embodied food field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_ba06bf75c66322b89254","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:formula-and-sequence","source_type":"word_analysis","support_ids":["sup_772aee09f7ce5335998c","sup_93d55fb951b4ace91159"],"title":"formula and sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_bd039f6a35ff5f4b0983","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:provision-and-entitlement","source_type":"word_analysis","support_ids":["sup_772aee09f7ce5335998c","sup_f9b4e6eb503b89b4e5ad"],"title":"provision and entitlement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_491b95b97692fe39d67e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:5:singular-concrete-form","source_type":"word_analysis","support_ids":["sup_772aee09f7ce5335998c","sup_faea3ce56d4b6a5edbd0"],"title":"singular concrete provision","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:5","qac_refs":["89:18:4:1"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_ba8073e219af6dd23666","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:audible-closure","source_type":"word_analysis","support_ids":["sup_007c6d0c42e7ad5e29ce","sup_a2f5157b0de468e214a7"],"title":"audible closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_e6a2d09858d59cb44371","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:definite-construct-category","source_type":"word_analysis","support_ids":["sup_a2f5157b0de468e214a7","sup_f125c6a4d128fb69500e"],"title":"definite construct category","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_322d12074e4339f38d91","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:deprivation-as-stillness","source_type":"word_analysis","support_ids":["sup_a2f5157b0de468e214a7","sup_e968d50391120b98af8a"],"title":"deprivation as stillness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_e96c3983d2a9072a5706","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:mediated-recipient","source_type":"word_analysis","support_ids":["sup_a2f5157b0de468e214a7","sup_f31ab7d7c8647e698905"],"title":"recipient mediated by provision","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_d0c638590aa7cded5678","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:poor-food-formula-completion","source_type":"word_analysis","support_ids":["sup_6dd2cb63ee88cb638f53","sup_a2f5157b0de468e214a7"],"title":"poor-food formula completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:6"],"branch_refs":[],"candidate_id":"cand_e09636b019fc944d3ec1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:6:vulnerable-category-sequence","source_type":"word_analysis","support_ids":["sup_086a291e29c8cbd6c3ae","sup_a2f5157b0de468e214a7"],"title":"vulnerable category sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:18:6","qac_refs":["89:18:5:1","89:18:5:2"],"status":"accepted"}},{"anchor_refs":["89:18:2"],"branch_refs":[],"candidate_id":"cand_24e8b984907547456f37","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000334"],"scope":"focus_ayah","source_local_id":"89:18:2:1","source_type":"qac_morpheme","support_ids":["sup_2ebf22eb456030557a1a"],"title":"QAC root occurrence: ح ض ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:18:4"],"branch_refs":[],"candidate_id":"cand_c5069db7bd295e3419cf","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000934"],"scope":"focus_ayah","source_local_id":"89:18:4:1","source_type":"qac_morpheme","support_ids":["sup_ca3d3f612ff6ac7ba925"],"title":"QAC root occurrence: ط ع م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:18:5"],"branch_refs":[],"candidate_id":"cand_9ebf2b21da7da98876b5","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000726"],"scope":"focus_ayah","source_local_id":"89:18:5:2","source_type":"qac_morpheme","support_ids":["sup_4b9fe1dc7eba1255b6b8"],"title":"QAC root occurrence: س ك ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:18","branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002"],"candidate_id":"cand_f354c0f2f89f52911ea7","commentary_obligation":"review","hft_ref":"hft_e2803d8bbadf905e8f4a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_reciprocal_provision","source_type":"hft","support_ids":["sup_cb50b040fe06a4b16610"],"title":"baseline_reciprocal_provision","trust":"legacy_unbound"},{"anchor_refs":["89:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:18","branch_refs":["root_000334/B001","root_000726/B010","root_000934/B004"],"candidate_id":"cand_701b35c256c4d6fca187","commentary_obligation":"review","hft_ref":"hft_87bdbcb7938a9ed77301","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_sustaining_share","source_type":"hft","support_ids":["sup_26a54b72ec02ca8c0abd"],"title":"baseline_sustaining_share","trust":"legacy_unbound"},{"anchor_refs":["89:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:18","branch_refs":["root_000334/B002","root_000726/B001","root_000934/B011"],"candidate_id":"cand_fe03da26775d6cb2a540","commentary_obligation":"review","hft_ref":"hft_35c26116f5ba63e57d9b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_counter_stillness","source_type":"hft","support_ids":["sup_2e1fcc8a54c16e397523"],"title":"baseline_counter_stillness","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:18:1:1","qac_word_ref":"89:18:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:18:1:2","qac_word_ref":"89:18:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","root_ar":"ح ض ض","surface_ar":"تَحَٰٓضُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:18:2:2","qac_word_ref":"89:18:2","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"89:18:3:1","qac_word_ref":"89:18:3","root_ar":"","surface_ar":"عَلَىٰ"},{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","root_ar":"ط ع م","surface_ar":"طَعَامِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:18:5:1","qac_word_ref":"89:18:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","root_ar":"س ك ن","surface_ar":"مِسْكِينِ"}],"word_analysis_qac_refs":[["89:18:1:1"],["89:18:1:2"],["89:18:2:1","89:18:2:2"],["89:18:3:1"],["89:18:4:1"],["89:18:5:1","89:18:5:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:18:1","89:18:2","89:18:3","89:18:4","89:18:5","89:18:6"]},"focus_surface_evidence":{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"89:18:1:1","qac_word_ref":"89:18:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"89:18:1:2","qac_word_ref":"89:18:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"تَحَٰٓضُّ","morph_features":"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP","morpheme_role":"STEM","pos":"V","qac_ref":"89:18:2:1","qac_word_ref":"89:18:2","root_ar":"ح ض ض","surface_ar":"تَحَٰٓضُّ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:2MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"89:18:2:2","qac_word_ref":"89:18:2","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"عَلَىٰ","morph_features":"STEM|POS:P|LEM:EalaY`","morpheme_role":"STEM","pos":"P","qac_ref":"89:18:3:1","qac_word_ref":"89:18:3","root_ar":"","surface_ar":"عَلَىٰ"},{"lemma_ar":"طَعَام","morph_features":"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:4:1","qac_word_ref":"89:18:4","root_ar":"ط ع م","surface_ar":"طَعَامِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:18:5:1","qac_word_ref":"89:18:5","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مِسْكِين","morph_features":"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:18:5:2","qac_word_ref":"89:18:5","root_ar":"س ك ن","surface_ar":"مِسْكِينِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:18:1:1"],["89:18:1:2"],["89:18:2:1","89:18:2:2"],["89:18:3:1"],["89:18:4:1"],["89:18:5:1","89:18:5:2"]],"word_analysis_refs":["89:18:1","89:18:2","89:18:3","89:18:4","89:18:5","89:18:6"],"word_rows":[{"analysis_record_ref":"89:18:1","analytic_gloss_range_en":"coordinating connector that carries the prior rebuke forward into another negated social charge","analytic_root_gloss_range_en":null,"qac_refs":["89:18:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"89:18:2","analytic_gloss_range_en":"descriptive negation of an ongoing plural practice, with scope over the urging verb and its provision complement","analytic_root_gloss_range_en":null,"qac_refs":["89:18:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"89:18:3","analytic_gloss_range_en":"negated second-person plural urging or mutual social mobilization, aimed through a prepositional matter rather than a stated direct object","analytic_root_gloss_range_en":"urging, inciting, and exerting pressure toward a matter; unrelated low-ground, resin, or increase branches are not locally activated","qac_refs":["89:18:2:1","89:18:2:2"],"root":{"arabic":"ح ض ض","transliteration":"ḥ-ḍ-ḍ"},"surface":{"arabic":"تَحَٰٓضُّونَ","transliteration":"taḥāḍḍūna"}},{"analysis_record_ref":"89:18:4","analytic_gloss_range_en":"preposition marking the governed matter or pressure-point of urging, not simple spatial height","analytic_root_gloss_range_en":null,"qac_refs":["89:18:3:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"عَلَىٰ","transliteration":"ʿalā"}},{"analysis_record_ref":"89:18:5","analytic_gloss_range_en":"food, feeding, or concrete provision as a singular construct bound to the needy recipient and governed as the matter of failed urging","analytic_root_gloss_range_en":"tasting, eating, feeding, nourishment, and provision; distant branches such as prompting speech, grafting, or throat-gripping are not locally licensed","qac_refs":["89:18:4:1"],"root":{"arabic":"ط ع م","transliteration":"ṭ-ʿ-m"},"surface":{"arabic":"طَعَامِ","transliteration":"ṭaʿāmi"}},{"analysis_record_ref":"89:18:6","analytic_gloss_range_en":"the definite singular needy or destitute person as recognized social category, genitively bound to the food phrase","analytic_root_gloss_range_en":"stillness, settling, dwelling, tranquility, and poverty or humble abasement; locally the poverty/deprivation status is selected, while calm or dwelling branches remain background only","qac_refs":["89:18:5:1","89:18:5:2"],"root":{"arabic":"س ك ن","transliteration":"s-k-n"},"surface":{"arabic":"ٱلْمِسْكِينِ","transliteration":"al-miskīni"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:18"],"branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002"],"candidate_id":"cand_f354c0f2f89f52911ea7","evidence_scope":"focus_ayah","hft_ref":"hft_e2803d8bbadf905e8f4a","item_id":"baseline_reciprocal_provision","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_reciprocal_provision","support_id":"sup_cb50b040fe06a4b16610"},{"anchor_refs":["89:18"],"branch_refs":["root_000334/B001","root_000726/B010","root_000934/B004"],"candidate_id":"cand_701b35c256c4d6fca187","evidence_scope":"focus_ayah","hft_ref":"hft_87bdbcb7938a9ed77301","item_id":"baseline_sustaining_share","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_sustaining_share","support_id":"sup_26a54b72ec02ca8c0abd"},{"anchor_refs":["89:18"],"branch_refs":["root_000334/B002","root_000726/B001","root_000934/B011"],"candidate_id":"cand_fe03da26775d6cb2a540","evidence_scope":"focus_ayah","hft_ref":"hft_35c26116f5ba63e57d9b","item_id":"baseline_counter_stillness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_counter_stillness","support_id":"sup_2e1fcc8a54c16e397523"}],"diagnostics":[],"lane_counts":{"global":13,"macro":8,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:18","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:18","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"89:18","lane":"micro","linguistic_source_ref":"89:18","surface_ref":"89:18","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:18","target_tokens":[["Ayrıca",["89:18:1"]],["birbirinizi",["89:18:2"]],["yoksulu",["89:18:5"]],["doyurmaya",["89:18:4"]],["teşvik",["89:18:2","89:18:3"]],["etmiyorsunuz",["89:18:1","89:18:2"]]],"text":"Ayrıca birbirinizi yoksulu doyurmaya teşvik etmiyorsunuz."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:audible-closure","source_type":"word_analysis","support_id":"sup_007c6d0c42e7ad5e29ce","text":"{\"blocking_evidence\":null,\"headline\":\"audible closure\",\"reader_payoff\":\"The reader hears the clause settle on the needy person after the compact negated predicate.\",\"reason\":\"The sound rows are anchored in the final local surface and reinforce its closure role.\",\"representative_source_ids\":[\"QP-aa250de4\",\"QP-bb074d18\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:vulnerable-category-sequence","source_type":"word_analysis","support_id":"sup_086a291e29c8cbd6c3ae","text":"{\"blocking_evidence\":null,\"headline\":\"vulnerable category sequence\",\"reader_payoff\":\"The reader notices the same audience moving from failed care for the orphan in 89:17 to neglected needy provision here and then to consumption and wealth-love in 89:19-20.\",\"reason\":\"The CRITICAL rows name the same-surah sequence, and the connective negation supports reading this noun as part of that chain.\",\"representative_source_ids\":[\"QI-43caa3c9\",\"QT-5625628c\",\"QB-72c70bb8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:omitted-urged-object","source_type":"word_analysis","support_id":"sup_14375f4364b760ab5ad2","text":"{\"blocking_evidence\":null,\"headline\":\"unnamed urged object\",\"reader_payoff\":\"The reader notices that the failure is larger than one missed exhortation because the human targets are left open while the provision matter is named.\",\"reason\":\"The verb instance has no direct object and takes the preposition-governed food phrase as its complement.\",\"representative_source_ids\":[\"QG-61586c4f\",\"MG-06adb5ec\",\"QT-997104b3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:1:register-widening","source_type":"word_analysis","support_id":"sup_187b553d24c14ff6f9d2","text":"{\"blocking_evidence\":null,\"headline\":\"care widens into advocacy\",\"reader_payoff\":\"The reader notices that the second charge expands the social field from face-to-face neglect to failed communal advocacy.\",\"reason\":\"The coordinated clause continues the same rebuke while the following verb and complement change the vulnerable-care register.\",\"representative_source_ids\":[\"QB-40470de1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:form-and-variant-pressure","source_type":"word_analysis","support_id":"sup_1fb949d1178fa6db1b9b","text":"{\"blocking_evidence\":null,\"headline\":\"collective form with variant pressure\",\"reader_payoff\":\"The reader notices that the local reading intensifies the charge as failed communal pressure, while variant evidence keeps simple urging and reported social type in view.\",\"reason\":\"The aligned form is second-person plural with collective or reciprocal force; variant rows are useful contrast but do not govern the canonical parse.\",\"representative_source_ids\":[\"QF-25618dc0\",\"QF-4200c138\",\"QF-4d88ce37\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:18:2:1","source_type":"qac_morpheme","support_id":"sup_2ebf22eb456030557a1a","text":"{\"lemma_ar\":\"تَحَٰٓضُّ\",\"morph_features\":\"STEM|POS:V|IMPF|(VI)|LEM:taHa`^D~u|ROOT:HDD|2MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:18:2:1\",\"qac_word_ref\":\"89:18:2\",\"root_ar\":\"ح ض ض\",\"surface_ar\":\"تَحَٰٓضُّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:4:hinge-before-completion","source_type":"word_analysis","support_id":"sup_3215fcab52f3e7eb5dce","text":"{\"blocking_evidence\":null,\"headline\":\"hinge before completion\",\"reader_payoff\":\"The reader notices the clause moving through the preposition before the final needy recipient is revealed.\",\"reason\":\"Local word order places the preposition between the negated urging verb and the food construct phrase.\",\"representative_source_ids\":[\"QT-7cdd94b2\",\"QT-9431eb01\",\"QP-59f51ec1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:1:compact-negative-opening","source_type":"word_analysis","support_id":"sup_46d08bd1786f738146ba","text":"{\"blocking_evidence\":null,\"headline\":\"compact negative opening\",\"reader_payoff\":\"The reader hears the ayah begin with a single compact movement of connection into refusal.\",\"reason\":\"The particle is split analytically but locally opens as the fused connector-negator unit, so the sound note supports the grammatical continuation.\",\"representative_source_ids\":[\"QF-e4f7436e\",\"QP-34837987\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:18:5:2","source_type":"qac_morpheme","support_id":"sup_4b9fe1dc7eba1255b6b8","text":"{\"lemma_ar\":\"مِسْكِين\",\"morph_features\":\"STEM|POS:N|LEM:misokiyn|ROOT:skn|MS|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:18:5:2\",\"qac_word_ref\":\"89:18:5\",\"root_ar\":\"س ك ن\",\"surface_ar\":\"مِسْكِينِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:double-dependency-construct","source_type":"word_analysis","support_id":"sup_4e7c56fe88e80cce1f60","text":"{\"blocking_evidence\":null,\"headline\":\"double dependency construct\",\"reader_payoff\":\"The reader notices food as the grammatical channel between denied social pressure and the needy person who specifies it.\",\"reason\":\"Attachment evidence marks the noun as governed by the preposition and as the construct head before the definite dependent.\",\"representative_source_ids\":[\"QG-bc3e7584\",\"MG-73b4ccc9\",\"QF-e57a37be\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:2:scope-over-provision","source_type":"word_analysis","support_id":"sup_5408cf130a690a4aa425","text":"{\"blocking_evidence\":null,\"headline\":\"negation reaches provision\",\"reader_payoff\":\"The reader notices that what is missing is the whole advocacy relation concerning food, not just a vague impulse to urge.\",\"reason\":\"Attachment support explicitly preserves the scope of negation over the urging verb and its prepositional complement.\",\"representative_source_ids\":[\"QG-6b70bcff\",\"MT-637446fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:audible-pressure","source_type":"word_analysis","support_id":"sup_6727a3a7c67cf06e850b","text":"{\"blocking_evidence\":null,\"headline\":\"audible pressure\",\"reader_payoff\":\"The reader hears pressure built into the verb's surface even though the sentence negates that pressure socially.\",\"reason\":\"The sound rows are anchored in the visible doubled consonant and lengthened surface of the local verb.\",\"representative_source_ids\":[\"QP-30ad8e13\",\"MP-0b3534f7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:poor-food-formula-completion","source_type":"word_analysis","support_id":"sup_6dd2cb63ee88cb638f53","text":"{\"blocking_evidence\":null,\"headline\":\"poor-food formula completion\",\"reader_payoff\":\"The reader notices that the phrase becomes the recognizable poor-food formula only when the final needy noun arrives.\",\"reason\":\"CRITICAL rows give concrete poor-food parallels in 69:34 and 107:3 and explain how the final noun completes the formula.\",\"representative_source_ids\":[\"MI-c8ec8b6e\",\"QE-bda91b3c\",\"QY-f6b5966e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:negated-plural-mobilization","source_type":"word_analysis","support_id":"sup_708747bdf79237675762","text":"{\"blocking_evidence\":null,\"headline\":\"negated plural mobilization\",\"reader_payoff\":\"The reader notices that the charge directly implicates the addressed plural audience in an active capacity they fail to exercise.\",\"reason\":\"QAC identifies a second masculine plural imperfect under negation, and attachment evidence treats the subject as carried by the surface agreement.\",\"representative_source_ids\":[\"QG-06c5c929\",\"QG-c0ad6bd7\",\"QF-2719165e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:1:coordinated-negated-charge","source_type":"word_analysis","support_id":"sup_7433e2b30982638f2889","text":"{\"blocking_evidence\":null,\"headline\":\"coordinated negated charge\",\"reader_payoff\":\"The reader notices that the poor-feeding failure is accumulated with the orphan failure from 89:17, not introduced as an isolated ethical topic.\",\"reason\":\"QAC and attachment support identify the word as a conjunction coordinating this negated clause with the previous negative charge.\",\"representative_source_ids\":[\"QG-cf83a934\",\"MG-682c809a\",\"QT-8fca4676\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5","source_type":"word_analysis","support_id":"sup_772aee09f7ce5335998c","text":"{\"gloss_range\":\"food, feeding, or concrete provision as a singular construct bound to the needy recipient and governed as the matter of failed urging\",\"prose\":\"{{ar:طَعَامِ}} ({{tr:ṭaʿāmi}}) is where the accusation becomes material. It is governed by {{ar:عَلَىٰ}} ({{tr:ʿalā}}) and then binds forward to {{ar:ٱلْمِسْكِينِ}} ({{tr:al-miskīni}}), so food becomes the channel between social pressure and the needy recipient. The construct allows both food for the poor person and the poor person's food, making provision feel like entitlement as well as charity. The root's tasting, eating, feeding, and nourishment field keeps the duty bodily and consumable, while the singular concrete noun keeps the needed substance in view rather than replacing it with an abstract act. Its heavy onset and long vowel give the provision word acoustic weight and stretch the relation toward the final needy person. In the surah sequence, this rightful object of advocacy is followed by devouring and wealth-love in 89:19-20; elsewhere, feeding the poor is praised or made a steep-path act (76:8; 90:14).\",\"root_display\":\"{{ar:ط ع م}} ({{tr:ṭ-ʿ-m}})\",\"root_gloss_range\":\"tasting, eating, feeding, nourishment, and provision; distant branches such as prompting speech, grafting, or throat-gripping are not locally licensed\",\"surface_display\":\"{{ar:طَعَامِ}} ({{tr:ṭaʿāmi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:4","source_type":"word_analysis","support_id":"sup_78cba4c789e228205aef","text":"{\"gloss_range\":\"preposition marking the governed matter or pressure-point of urging, not simple spatial height\",\"prose\":\"{{ar:عَلَىٰ}} ({{tr:ʿalā}}) is the hinge that connects the missing urging to its governed matter. It is not spatial height here; it makes {{ar:طَعَامِ}} ({{tr:ṭaʿāmi}}) the issue under pressure. The preposition's ordinary sense of being upon still gives the construction weight: the poor person's food is felt as a burden or obligation resting on the group. By coming before the food phrase is completed, it pulls the clause from denied social action toward the concrete provision that follows, while the people to be urged remain unnamed.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:عَلَىٰ}} ({{tr:ʿalā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:4:obligation-pressure","source_type":"word_analysis","support_id":"sup_7b9ed70df6cfbb46a082","text":"{\"blocking_evidence\":null,\"headline\":\"obligation pressure\",\"reader_payoff\":\"The reader feels the food matter as a burden of responsibility, not a remote topic of discussion.\",\"reason\":\"The local construction selects matter or target of urging while preserving a pressure nuance compatible with the preposition.\",\"representative_source_ids\":[\"QS-2cf9f4ec\",\"QS-64321c63\",\"MS-a1bed45d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:embodied-food-field","source_type":"word_analysis","support_id":"sup_8559148302d974677b31","text":"{\"blocking_evidence\":null,\"headline\":\"embodied food field\",\"reader_payoff\":\"The reader notices that the missing advocacy has to reach actual nourishment, not merely the language of concern.\",\"reason\":\"V4 supports taste, eating, feeding, and provision branches, while the local noun and construct keep only the food/provision field active.\",\"representative_source_ids\":[\"QS-1ffb2dc5\",\"QS-f72f1ad5\",\"QF-b719c07f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:formula-and-sequence","source_type":"word_analysis","support_id":"sup_93d55fb951b4ace91159","text":"{\"blocking_evidence\":null,\"headline\":\"formula and sequence\",\"reader_payoff\":\"The reader notices the phrase as both a known poor-feeding formula and a local contrast with later appetite and wealth desire in 89:19-20.\",\"reason\":\"CRITICAL rows give concrete references to 76:8, 90:14, 89:19, and 89:20, while contextual profiles show the local food noun participates in provision relations.\",\"representative_source_ids\":[\"MI-e1175bd3\",\"QE-30a8d8d8\",\"QY-67b0fdb8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6","source_type":"word_analysis","support_id":"sup_a2f5157b0de468e214a7","text":"{\"gloss_range\":\"the definite singular needy or destitute person as recognized social category, genitively bound to the food phrase\",\"prose\":\"{{ar:ٱلْمِسْكِينِ}} ({{tr:al-miskīni}}) completes the phrase and gives the ayah its final human focus. As a definite singular dependent, it makes the food belong to a recognized social category rather than to an incidental case; the recipient is reached through provision. The root's stillness field is narrowed here into deprivation: not tranquil repose, but a constrained status in which agency and access have been stilled. That is why the failure to urge is so pointed; a community that should move others toward food leaves the immobilized person at the end of the clause. Only when this final noun arrives does the food phrase become the recognizable poor-food formula, and its long final sound lets the clause settle audibly on the needy person. The final word also joins a vulnerable-category chain from the orphan in 89:17 toward inheritance and wealth failures in 89:19-20, and it completes the poor-food judgment formula seen in 69:34 and 107:3.\",\"root_display\":\"{{ar:س ك ن}} ({{tr:s-k-n}})\",\"root_gloss_range\":\"stillness, settling, dwelling, tranquility, and poverty or humble abasement; locally the poverty/deprivation status is selected, while calm or dwelling branches remain background only\",\"surface_display\":\"{{ar:ٱلْمِسْكِينِ}} ({{tr:al-miskīni}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:4:governed-pressure-point","source_type":"word_analysis","support_id":"sup_aeb253d456dfa01cd8b4","text":"{\"blocking_evidence\":null,\"headline\":\"governed pressure-point\",\"reader_payoff\":\"The reader notices that the food phrase is grammatically attached to the missing advocacy as its pressure-point.\",\"reason\":\"Attachment evidence marks the food noun as governed by the preposition within the verb's complement.\",\"representative_source_ids\":[\"QG-2c5de3d2\",\"QG-bb05c524\",\"MG-cc606a08\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3","source_type":"word_analysis","support_id":"sup_bd5a82cf7e55b3f32787","text":"{\"gloss_range\":\"negated second-person plural urging or mutual social mobilization, aimed through a prepositional matter rather than a stated direct object\",\"prose\":\"{{ar:تَحَٰٓضُّونَ}} ({{tr:taḥāḍḍūna}}) is the ayah's hinge word: the addressed plural community is charged with not mobilizing pressure. The verb leaves the people being urged unnamed and instead takes {{ar:عَلَىٰ طَعَامِ}} ({{tr:ʿalā ṭaʿāmi}}), so responsibility spreads through the community while food remains the explicit pressure-point. The form gives the missing act a reciprocal or collective shape; accepted variant pressures show that simpler urging and third-person report are available in the reading tradition, but the local surface directly confronts the audience. The root's urging field is rare and recognizable in poor-food judgment contexts (69:34; 107:3), and the doubled sound makes the absent pressure audible before the clause lands on material provision. Within the local sequence, the verb extends the negated plural pattern from direct honoring in 89:17 into failed advocacy here, before the surah turns to active devouring in 89:19.\",\"root_display\":\"{{ar:ح ض ض}} ({{tr:ḥ-ḍ-ḍ}})\",\"root_gloss_range\":\"urging, inciting, and exerting pressure toward a matter; unrelated low-ground, resin, or increase branches are not locally activated\",\"surface_display\":\"{{ar:تَحَٰٓضُّونَ}} ({{tr:taḥāḍḍūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:parallel-and-sequence","source_type":"word_analysis","support_id":"sup_c5e95fdaaf361fb28673","text":"{\"blocking_evidence\":null,\"headline\":\"parallel social failure\",\"reader_payoff\":\"The reader notices the surah's movement from direct vulnerable-person neglect in 89:17 to failed advocacy in 89:18 and then to active consumption in 89:19.\",\"reason\":\"The clause is coordinated with the prior negated plural charge, and the CRITICAL sequence rows name the same-surah development.\",\"representative_source_ids\":[\"QT-2b58b3d6\",\"MT-452d56db\",\"QB-abb5de58\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:18:4:1","source_type":"qac_morpheme","support_id":"sup_ca3d3f612ff6ac7ba925","text":"{\"lemma_ar\":\"طَعَام\",\"morph_features\":\"STEM|POS:N|LEM:TaEaAm|ROOT:TEm|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:18:4:1\",\"qac_word_ref\":\"89:18:4\",\"root_ar\":\"ط ع م\",\"surface_ar\":\"طَعَامِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:2","source_type":"word_analysis","support_id":"sup_ca81df6a363e02f09ccf","text":"{\"gloss_range\":\"descriptive negation of an ongoing plural practice, with scope over the urging verb and its provision complement\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) diagnoses a standing non-practice rather than issuing a prohibition. With the imperfect {{ar:تَحَٰٓضُّونَ}} ({{tr:taḥāḍḍūna}}), the charge is that the addressed group characteristically does not generate social pressure. Its scope reaches the whole verb-preposition phrase, so the absence is not urging in the abstract but advocacy concerning the poor person's food. Because it is coupled to the connector, the denial begins as part of the accumulating rebuke rather than after a pause.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:3:poor-food-judgment-field","source_type":"word_analysis","support_id":"sup_dd3b0c35b801b928b870","text":"{\"blocking_evidence\":null,\"headline\":\"poor-food judgment field\",\"reader_payoff\":\"The reader notices that the verb belongs to a recognizable judgment field where failure to urge around poor food marks moral collapse.\",\"reason\":\"V4 supports the urging branch, and contextual evidence shows the local root-form has the food noun as its top partner in this ayah.\",\"representative_source_ids\":[\"MS-82a9f9dd\",\"MI-65acd6cf\",\"QE-96c95427\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:deprivation-as-stillness","source_type":"word_analysis","support_id":"sup_e968d50391120b98af8a","text":"{\"blocking_evidence\":null,\"headline\":\"deprivation as stillness\",\"reader_payoff\":\"The reader sees poverty as immobilized deprivation, a condition that demands movement from others.\",\"reason\":\"V4 includes stillness, dwelling, tranquility, and poverty branches; the local intensive/status noun selects the poverty-deprivation branch while retaining stillness as image pressure.\",\"representative_source_ids\":[\"QS-5bc3b265\",\"QS-f99ddf44\",\"MS-ba7ae6e9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:definite-construct-category","source_type":"word_analysis","support_id":"sup_f125c6a4d128fb69500e","text":"{\"blocking_evidence\":null,\"headline\":\"definite construct category\",\"reader_payoff\":\"The reader notices that the final noun specifies the food phrase as a recognized social claim, not a floating moral emblem.\",\"reason\":\"QAC and attachment evidence identify the word as a definite singular genitive dependent after the food noun.\",\"representative_source_ids\":[\"QG-9976eee5\",\"QG-eb8ddec1\",\"QF-dc3b181c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:6:mediated-recipient","source_type":"word_analysis","support_id":"sup_f31ab7d7c8647e698905","text":"{\"blocking_evidence\":null,\"headline\":\"recipient mediated by provision\",\"reader_payoff\":\"The reader notices that the vulnerable person is reached through systems of provision, not only direct interpersonal concern.\",\"reason\":\"The final noun is the construct dependent of the food noun, and contextual evidence places the food root as a recurring partner.\",\"representative_source_ids\":[\"QS-90c9d1e5\",\"QT-4946be7f\",\"QB-8c0562f5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:audible-materiality","source_type":"word_analysis","support_id":"sup_f8181996b8d3e053a899","text":"{\"blocking_evidence\":null,\"headline\":\"audible materiality\",\"reader_payoff\":\"The reader hears the provision relation stretch from food toward the needy person.\",\"reason\":\"The sound rows are anchored in the local surface and reinforce the already retained provision relation.\",\"representative_source_ids\":[\"QP-7e86cd08\",\"QP-aa8b5c5f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:provision-and-entitlement","source_type":"word_analysis","support_id":"sup_f9b4e6eb503b89b4e5ad","text":"{\"blocking_evidence\":null,\"headline\":\"provision and entitlement\",\"reader_payoff\":\"The reader notices that the food is not generic charity; it is provision defined by the needy person's claim.\",\"reason\":\"The construct with a definite dependent licenses both recipient and possessive pressure without forcing a single English reduction.\",\"representative_source_ids\":[\"QG-9e17645e\",\"QS-d03155bc\",\"QG-2b1e1aa7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:5:singular-concrete-form","source_type":"word_analysis","support_id":"sup_faea3ce56d4b6a5edbd0","text":"{\"blocking_evidence\":null,\"headline\":\"singular concrete provision\",\"reader_payoff\":\"The reader notices that the wording holds onto the food itself rather than abstracting the charge into a feeding-gerund.\",\"reason\":\"The aligned word is a singular concrete noun in construct state, not a plural inventory or a verbal noun.\",\"representative_source_ids\":[\"QF-419fcf65\",\"QF-f8e3f321\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:2:standing-negated-practice","source_type":"word_analysis","support_id":"sup_fb003661aa60648ab05e","text":"{\"blocking_evidence\":null,\"headline\":\"standing negated practice\",\"reader_payoff\":\"The reader notices that the ayah indicts an established social habit, not a single missed act or a bare prohibition.\",\"reason\":\"The local particle negates an imperfect indicative plural verb, and attachment evidence confirms the negation as scope over the verbal predicate.\",\"representative_source_ids\":[\"QG-50925804\",\"QS-043be94a\",\"QF-5f22ef73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:2:coupled-opening","source_type":"word_analysis","support_id":"sup_fd51259b47c332d3fc53","text":"{\"blocking_evidence\":null,\"headline\":\"denial coupled to continuation\",\"reader_payoff\":\"The reader hears no neutral additive pause before the second accusation; the next clause opens directly into denial.\",\"reason\":\"The local opening joins connector and negator before the expanded verbal predicate.\",\"representative_source_ids\":[\"QF-c5b9e59d\",\"QP-206c6f2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:18:1","source_type":"word_analysis","support_id":"sup_fe10234f9dc0c2fa0bd5","text":"{\"gloss_range\":\"coordinating connector that carries the prior rebuke forward into another negated social charge\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) does not open a detached moral note. It fastens this ayah to the preceding accusation, so the failure concerning the poor person's food stands beside the failure toward the orphan in 89:17. Because it arrives immediately with {{ar:لَا}} ({{tr:lā}}), continuation and denial are heard together: the rebuke accumulates as another negated practice, and the register widens from direct care for a vulnerable person to public pressure around provision.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000334/B001","root_000726/B006","root_000934/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000334","role":"Urging and incitement supply the interpersonal pressure engine, while the reciprocal plural makes that pressure circulate.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000934","role":"Feeding another or asking to be fed gives the circulating pressure a concrete transfer endpoint.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_000726","role":"Poverty, weakness, and abasement identify the condition that the failed social relay leaves unrelieved.","root":"س ك ن","source_ref":"89:18","source_word_indices":["5"]}],"changed_reading":{"after":"The addressees fail to reproduce a communal norm in which people press one another until nourishment actually reaches the person in need.","before":"The addressees fail to recommend an individual charitable act."},"confidence":"strong","focus_anchor":"The plural reciprocal verb at focus word 2 governs the food at word 4 for the person characterized at word 5.","mechanism":"Provision is made socially mobile by reciprocal exhortation: each person is responsible not only to feed but to activate another feeder, so the censured failure is a broken relay of pressure and transfer.","model_id":"baseline_reciprocal_provision"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_reciprocal_provision","source_type":"hft","support_id":"sup_cb50b040fe06a4b16610","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000334/B001","root_000726/B010","root_000934/B004"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000334","role":"Exhortation supplies the collective action needed to secure an ongoing share rather than an isolated mouthful.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_000934","role":"Provision, livelihood, earnings, revenue, and legal share widen food into the material basis of a person's condition.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]},{"branch_id":"B010","mapped_root_id":"root_000726","role":"Provision that enables remaining in place makes stable subsistence the functional result of that share.","root":"س ك ن","source_ref":"89:18","source_word_indices":["5"]}],"changed_reading":{"after":"The verse concerns mobilizing a sustaining livelihood or share by which a materially vulnerable person can remain established.","before":"The verse concerns prompting someone to give a needy person food."},"confidence":"strong","focus_anchor":"The construction links exhortation to food and then to a noun from the settlement/stillness root.","mechanism":"Food expands from a meal into livelihood and an allocable share; the recipient's root then makes that provision what permits continued residence and material stability.","model_id":"baseline_sustaining_share"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_sustaining_share","source_type":"hft","support_id":"sup_26a54b72ec02ca8c0abd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ","ayah_ref":"89:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000334/B002","root_000726/B001","root_000934/B011"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000334","role":"Low ground at a mountain's foot spatializes the point from which the needed counter-motion must begin.","root":"ح ض ض","source_ref":"89:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000726","role":"Cessation of movement renders need as material immobilization rather than only low income.","root":"س ك ن","source_ref":"89:18","source_word_indices":["5"]},{"branch_id":"B011","mapped_root_id":"root_000934","role":"Capacity to do something lets nourishment function as restored ability, not merely consumption.","root":"ط ع م","source_ref":"89:18","source_word_indices":["4"]}],"changed_reading":{"after":"No communal counterforce is generated for a person immobilized at the social low point; nourishment would restore practical capacity and motion.","before":"No one advocates strongly enough for the poor."},"confidence":"exploratory","focus_anchor":"The focus juxtaposes an activation verb with a recipient root whose branches include stillness, low status, and settled position.","mechanism":"The sound cluster of exhortation also carries an image of low ground, while the recipient root carries stopped movement; social urging can therefore be carried as counter-motion generated at a social low point.","model_id":"baseline_counter_stillness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_counter_stillness","source_type":"hft","support_id":"sup_2e1fcc8a54c16e397523","trust":"legacy_unbound"}]}
</lane_packet_json>
