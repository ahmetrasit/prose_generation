# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **93:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s093-regular-20260912/s093/93_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "93:1",
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
{"branch_registry":[{"boundary":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B001","candidate_links":[{"candidate_id":"cand_9625e878390dc619a322","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"güneş yükseldikten sonraki kuşluk vakti","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın doğuş sonrası başlayıp öğleye yaklaşan temel zaman alanını doğal ve kısa biçimde karşılar.","boundary_detail":"Bu dal güneşe çıkmayı, görünür olmayı, yemek yemeyi ya da hayvan kesmeyi değil, bunlara ad verebilen gündüz vaktini anlatır.","branch_image_ar":"امتداد الضحى في النهار","concept_gloss":"güneş yükseldikten sonraki kuşluk vakti","contextual_glosses":[{"applicability":"Zaman dizisinin ilk aşamasını özellikle belirtmek gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğleye yaklaşan daha ileri kuşluk aşamalarını dışarıda bırakır.","preserves":"Doğuş sonrasındaki erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"güneş doğduktan hemen sonraki vakit","usage_role":"contextual"},{"applicability":"Bir eylemin erken gündüzün daha ileri bir aşamasına bırakıldığını anlatan cümlelere uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Zaman alanının doğuşa yakın ilk aşamasını karşılamaz.","preserves":"Günün yükselmesini ve eylemin o zamana bağlanmasını korur."},"facet_ids":["F002","F003"],"text":"gün iyice yükselince","usage_role":"contextual"}],"definition":"Güneş doğduktan sonra günün yükselip yayılmasıyla başlayan, aşamalar halinde ilerleyerek öğleye yaklaşan erken aydınlık zaman dilimidir. Bir yerde bu vakte kadar kalma veya bir işi bu vaktin daha ileri aşamasına bırakma kullanımları bu zaman çekirdeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güneş doğduktan sonra gün yükselir ve erken aydınlık zaman dilimi başlar."},{"facet_id":"F002","role":"specialization","statement":"Bu zaman, doğuşun hemen sonrasından başlayıp günün uzadığı ve öğleye yaklaştığı daha ileri aşamalara ayrılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir yerde bu vakte kadar kalmak veya bir eylemi vaktin yükselmesine kadar geciktirmek zaman anlamına bağlı kullanımlardır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Güneş doğmadan önceki ve dalın kapsamadığı daha geniş zaman aralığını da ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Günün erken bölümünde bulunma özelliğini korur."},"text":"sabah"}],"identity_rationale":"Kaynak ifadesi, güneş doğduktan sonra başlayan ve gün yükseldikçe ilerleyen bir zaman dizisini açıkça verir. Çerçevedeki günün yükselmesi ve uzaması bu diziyi doğru karşılar; eylemi bu zamana bırakma ise zaman anlamına bağlı bir kullanımdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"günün yükseldiği erken vakit"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kuşluk vakti"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"günün uzayıp öğleye yaklaştığı kuşluk vakti"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"güneş doğduktan sonraki ilk kuşluk vakti"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kuşluk vaktine girmek veya o vakte kadar kalmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuşluk namazını vakit iyice yükselene kadar geciktirmek"}],"lexicalization_note":"Tanım, günün erken aydınlık bölümünü temel alır; bu vakte girme ve bir işi vaktin ilerisine bırakma yalnızca ilgili biçim ve söz öbeklerine bağlıdır.","neighbor_coverage_note":"Verilen bütün komşu kartları değerlendirildi; zaman sınırını en açık gösteren üç karşılaştırma seçildi, yalnızca aynı gün içindeki olayları anan daha uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir erken gündüz zaman alanını ve onun aşamalarını adlandırır; komşu dal ise günün yükselmesini bir oluş olarak anlatır ve kaynak kartında daha geç bir güneş konumuna da uzanır.","focus_only":"Doğuş sonrasından öğleye yaklaşmaya kadar uzanan adlandırılmış zaman aşamalarını ve eylemi o vakte bırakmayı kapsar.","gloss":"günün yükselmesi","neighbor_only":"Günün yükselmesi yanında bazı kullanımlarda güneşin duvarlardan çekilmeye başlamasını da kapsar.","neighbor_ref":"root_000546/B012","relation_type":"near_synonym","shared_zone":"İki dal da gündüzün yükselip yayılmasını zaman belirleyici bir özellik olarak kullanır."},{"boundary_match":"partial","distinction":"Odak dalın gönderimi zamandır; komşunun çekirdeği ise dikleşme ve yükselme hareketidir. Bu nedenle olağan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Güneş doğduktan sonra ilerleyen zaman dilimini adlandırır.","gloss":"yükselen gündüz","neighbor_only":"Bir şeyin dikilmesini ve doğrulmasını temel alıp günün yükselmesini bu çekirdeğin bir uygulaması olarak verir.","neighbor_ref":"root_000642/B012","relation_type":"near_neighbor","shared_zone":"Her ikisinde de gündüzün yükselmesi ortak bir görüntüdür."},{"boundary_match":"field_only","distinction":"Birinci dal zamansal bir bölümdür; ikinci dal ise maruz kalma veya görünürlük durumudur. Aynı güneşli sahneyi paylaşmaları anlamlarını birleştirmez.","focus_only":"Güneşin yükselmesine göre belirlenen bir gündüz vaktini anlatır.","gloss":"vakit ile güneşe açıklık","neighbor_only":"Güneşe açık kalmayı, görünür olmayı ve dışta bulunan belirgin yanı anlatır.","neighbor_ref":"root_000904/B002","relation_type":"same_field","shared_zone":"Her iki dal da güneş ve açık gündüz çevresinde örgütlenir."}],"source_phrase_ar":"الضحاء امتداد النهار (maqayis); الضحو ارتفاع النهار والضحى فويق ذلك والضحاء ممدود إذا امتد النهار (ayn); الضحو لغة في الضحى (jamhara); ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء (sihah); الضحى انبساط الشمس وامتداد النهار وسمي الوقت به (mufradat)","source_summary":"Kaynakların ortak çizgisi, güneş doğduktan sonra günün yükselmesiyle açılan ve öğleye doğru ilerleyen bir zaman alanıdır. Adlandırmalar bu alanın birbirini izleyen erken ve ileri aşamalarını, ayrıca eylemin o vakte ulaşmasını anlatır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الضحو والضحى والضحاء ووقت ارتفاع النهار وتأخير الفعل إلى ذلك الوقت","what_is_not_ar":"لا يدخل فيه مجرد البروز للشمس ولا الذبيحة ولا الطعام إلا من جهة التسمية بالوقت"},"support_links":["sup_8f133d10337c648071e8"]},{"boundary":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B002","candidate_links":[{"candidate_id":"cand_ec156a18037e61a4e86d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"güneşe veya bakışa açık olup görünürleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın güneşe maruz kalma ile dışta ve görünür olma arasındaki ortak çekirdeğini birlikte karşılar.","boundary_detail":"Dal, gündüz vaktinin kendisini değil, güneşe veya bakışa açık olma ve böylece belirginleşme durumunu anlatır.","branch_image_ar":"البروز للشمس والظهور","concept_gloss":"güneşe veya bakışa açık olup görünürleşme","contextual_glosses":[{"applicability":"Bir kişinin ya da şeyin güneşe maruz kalmasını anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bakışa görünür olma, dış kenar ve alenen yapma kullanımlarını karşılamaz.","preserves":"Güneşe açık hale gelme ve ısıya maruz kalma yönünü korur."},"facet_ids":["F001","F004"],"text":"güneşe çıkmak","usage_role":"contextual"},{"applicability":"Yolun, yerin veya başka bir şeyin belirgin biçimde görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş ısısına maruz kalma ve terleme yönünü dışarıda bırakır.","preserves":"Bakışa açık ve belirgin olma yönünü korur."},"facet_ids":["F001","F002"],"text":"açıkça görünmek","usage_role":"contextual"},{"applicability":"Bir eylemin gizlenmeden ve herkesin görebileceği biçimde yapılmasına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yer, güneş ve bedensel maruz kalma kullanımlarını karşılamaz.","preserves":"Eylemin bakışa açık ve belirgin biçimde yapılmasını korur."},"facet_ids":["F003"],"text":"alenen yapmak","usage_role":"contextual"}],"definition":"Bir kişinin, yerin ya da şeyin güneşe veya bakışa açık duruma gelmesi ve böylece dışta, belirgin ya da görünür olmasıdır. Güneş ısısına maruz kalma ve terleme ile bir işi açıkça yapma, bu çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şey güneşe ya da bakışa açık hale gelir ve görünür olur."},{"facet_id":"F002","role":"extension","statement":"Bir yerin dışta kalan belirgin yanı, açık kenarı veya sürekli güneş alan bölümü aynı görünürlük çekirdeğiyle adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Bir işi açıkça ve herkesin görebileceği biçimde yapmak, görünür olmanın eylem alanındaki kullanımıdır."},{"facet_id":"F004","role":"associated_use","statement":"Güneş ısısına maruz kalma ve bununla bağlantılı terleme, güneşe açıklığın bedensel sonucudur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşe maruz kalmayı, dışta kalan yanı ve alenen yapma kapsamını tam olarak taşımaz.","preserves":"Görünür ve belirgin hale gelme yönünü korur."},"text":"ortaya çıkma"}],"identity_rationale":"Kaynak ifadesi güneşe çıkma, güneş ısısına maruz kalma, görünür hale gelme, dışta ve açıkta bulunan yan ile bir işi herkesin görebileceği biçimde yapma kullanımlarını birlikte destekler. Terleme, bu alanın bağımsız çekirdeği değil, güneş ısısına maruz kalmayla bağlantılı bir sonuçtur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güneşe çıkmak veya güneşin ısısına maruz kalmak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güneşe çık"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yol görünür hale geldi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yerleşimin dışta ve açıkta kalan yanı"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dışta kalan açık bölgeler veya kenarlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu açıkça ve herkesin gözü önünde yaptı"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"açıkta ve görünür yer"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"güneşin neredeyse hiç eksik olmadığı yer"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"atın bacakları arasındaki bölüm görünür olur"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"terledim"}],"lexicalization_note":"Güneşe çıkma ve görünür olma ortak çekirdektir; yolun görünmesi, açık yer, dış kenar, alenen yapma ve terleme ilgili biçim ve söz öbeklerinin ayrı gerçekleşmeleridir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel görünürlük dalları ile aynı kökün zaman dalı sınırı en çok keskinleştirdiği için yayımlandı, yalnızca dolaylı güneş veya açıklık çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu genel görünme ve açığa çıkma alanındadır; odak dal ise bu alanı güneşe açıklık, dış kenar ve açıkça yapılan eylemle özel olarak birleştirir.","focus_only":"Güneşe çıkmayı, güneş ısısına maruz kalmayı, dışta kalan yanı ve terlemeyi kapsar.","gloss":"açığa çıkıp görünür olma","neighbor_only":"Gizli veya içte olanın genel olarak açığa çıkıp anlaşılır hale gelmesini kapsar.","neighbor_ref":"root_000970/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin dışta, açık ve görünür olmasını anlatır."},{"boundary_match":"partial","distinction":"Odak için önceden gizli olma şart değildir ve güneş altında bulunma belirgindir; komşu ise gizlilikten görünürlüğe geçişi temel alır.","focus_only":"Güneşe maruz kalma ile öteden beri dışta ve açıkta bulunan yeri de kapsar.","gloss":"görünür hale gelme","neighbor_only":"Önceden gizli ya da örtülü olanın sonradan açılması ve bir metnin yayımlanması yönünü kapsar.","neighbor_ref":"root_000105/B001","relation_type":"near_synonym","shared_zone":"İki dalın kesişimi, bir şeyin saklı olmayıp görünür duruma gelmesidir."},{"boundary_match":"partial","distinction":"Komşu dar bir açık karşılaşma kalıbına bağlıdır; odak dal ise kişi, yol, yer ve eylem üzerinde daha geniş fakat güneşle güçlü biçimde ilişkili bir açıklık alanıdır.","focus_only":"Güneş altında kalma, dış kenar, alenen eylem ve terleme gibi daha geniş gerçekleşmeleri vardır.","gloss":"örtüsüz ve açıkta olma","neighbor_only":"Özellikle hiçbir şeyin örtmediği açık bir karşılaşma durumuna bağlıdır.","neighbor_ref":"root_000086/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de örtüsüz, dışta ve bakışa açık bulunmayı anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal bir açıklık ve görünürlük durumudur; komşu dal zamandır. Bir kişinin o vakitte bulunması onun zorunlu olarak güneşe açık olduğu anlamına gelmez.","focus_only":"Güneşe veya bakışa maruz kalıp görünür olmayı anlatır.","gloss":"güneşe açıklık ile kuşluk vakti","neighbor_only":"Güneşin yükselişine göre belirlenen erken gündüz zamanını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"İki dal güneşli erken gündüz sahnesini paylaşır."}],"source_phrase_ar":"ضحى الرجل يضحى إذا تعرض للشمس (maqayis); اضح أي ابرز للشمس (maqayis;ayn); ضحا الطريق إذا بدا وظهر (maqayis;sihah); ضاحية كل بلدة ناحيتها البارزة (maqayis;ayn;sihah;mufradat); فعل ذلك ضاحية أي ظاهرا بينا (maqayis;ayn;sihah); ضحيت عرقت وضحيت للشمس إذا برزت لها (sihah)","source_summary":"Kaynaklar, güneşe çıkma ile görünür ve dışta olmayı aynı anlam alanında birleştirir. Yolun görünmesi, yerin açık kenarı, işin alenen yapılması ve güneş altında terleme bu ortak açıklık durumunun farklı bağlamlarıdır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه التعرض للشمس وحرها والتعرق والبروز والظهور والناحية البارزة والعلانية","what_is_not_ar":"لا يدخل فيه وقت الضحى من حيث هو وقت ولا الأضحية ولا الغداء"},"support_links":["sup_2568c8300d64267c6352"]},{"boundary":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B003","candidate_links":[{"candidate_id":"cand_090e0b9fcaf784963274","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"erken gündüz öğünü ve o vakitte otlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın öğün ile hayvan otlatma kullanımlarını ortak zaman sınırı altında birlikte gösterir.","boundary_detail":"Dal yalnızca günün erken aydınlık vaktine bağlanan öğün ve otlatmayı kapsar; genel yemek, genel otlatma veya vaktin kendisi değildir.","branch_image_ar":"طعام الضحاء ورعي أوله","concept_gloss":"erken gündüz öğünü ve o vakitte otlatma","contextual_glosses":[{"applicability":"İnsanların günün erken aydınlık bölümündeki öğünü yemesini anlatan cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Deve ve koyunların otlatılması kullanımlarını dışarıda bırakır.","preserves":"Öğünü ve onun erken gündüz zamanını korur."},"facet_ids":["F001"],"text":"kuşluk öğünü yemek","usage_role":"contextual"},{"applicability":"Deve veya koyunların erken aydınlık vakitte otlaması ya da otlatılması bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların yediği öğün ve yeme eylemi anlamını karşılamaz.","preserves":"Otlatma eylemini ve erken gündüz zaman sınırını korur."},"facet_ids":["F002","F003"],"text":"günün başında otlatmak","usage_role":"contextual"}],"definition":"Günün erken aydınlık bölümünde yenen öğünü ve o sırada yemek yemeyi; ayrıca deve ya da koyunların günün başında otlamaya koyulmasını anlatan zaman bağlı kullanımlar alanıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Günün erken aydınlık bölümünde yenen öğün ve bu öğünü yeme eylemi adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Develerin günün başında otlamaya koyulması, aynı vakte bağlı hayvan yetiştiriciliği kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Koyunları erken aydınlık vakitte otlatmak, belirli bir söz öbeğine bağlı diğer hayvan yetiştiriciliği kullanımıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Günün ilk öğünü olma yönündeki çağdaş ve daha dar bir öğün düzenini çağrıştırır.","collision":"Çağdaş kahvaltı kavramıyla karışarak tarihsel zaman sınırını belirsizleştirir.","fit":"displacement","loses":"Kuşluk vaktine özgü zaman bağını ve hayvan otlatma kullanımlarını kaybeder.","preserves":"Günün erken bölümünde yenen bir öğün olma özelliğini korur."},"text":"kahvaltı"}],"identity_rationale":"Kaynak ifadesi iki zaman bağlı kullanımı açıkça bir araya getirir: günün erken aydınlık bölümünde yenen öğün ve evcil hayvanların o sırada otlamaya başlaması. Bunlar zamanın kendisi değildir; yeme ve otlatma eylemlerinin o vakitle sınırlandırılmış adlarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kuşluk öğünü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuşluk öğününü yemek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"develer günün başında otlamaya koyuldu"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"koyunlarını kuşluk vaktinde otlatmak"}],"lexicalization_note":"Öğün adı ve yemek yeme biçimleri ile deve ya da koyun otlatma söz öbekleri ayrı tutulur; zaman bağlantısı bu kullanımlardan bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün komşu adayları gözden geçirildi; erken gündüzü akşamdan, genel otlatmadan ve zamanın kendisinden ayıran dört kart yayımlandı, yem ve sürü çevresindeki daha dolaylı ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Eylem türleri paraleldir, fakat zaman ekseninin karşıt uçlarına yerleşirler: odak erken aydınlık vakte, komşu akşam ve geceye bağlıdır.","focus_only":"Erken aydınlık vakitteki öğün ve otlatmayı anlatır.","gloss":"gündüz başı ile akşam yeme ve otlatması","neighbor_only":"Akşam ya da geceye bağlı yemek ve otlatmayı anlatır.","neighbor_ref":"root_001017/B005","relation_type":"polarity_pair","shared_zone":"İki dal da bir öğünü ve hayvanların otlatılmasını günün belirli bölümüne bağlar."},{"boundary_match":"partial","distinction":"Odak dal zamana bağlı özel bir otlatma kullanımıdır; komşu dal otlatmanın genel alanını, otlağı ve yeneni de kapsar.","focus_only":"Otlatmayı günün erken aydınlık bölümüyle sınırlar ve ayrıca insan öğününü kapsar.","gloss":"erken vakitte otlatma","neighbor_only":"Hayvanın otlamasını, yemi ve otlak yerini zaman sınırı olmadan genel olarak kapsar.","neighbor_ref":"root_000574/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı evcil hayvanların otlamasıdır."},{"boundary_match":"field_only","distinction":"Odak dal zamanın adını eylem ve öğüne aktarır; komşu dal ise zaman diliminin kendisidir. Her iki yön tek bir yalın anlam olarak birleştirilmemelidir.","focus_only":"O vakitte yapılan yeme ve otlatma eylemlerini adlandırır.","gloss":"kuşluk vakti ile kuşluk etkinliği","neighbor_only":"Eylemlerden bağımsız olarak vaktin kendisini ve aşamalarını adlandırır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Yeme ve otlatma kullanımları komşu dalın belirlediği erken gündüz zamanında gerçekleşir."},{"boundary_match":"partial","distinction":"Odak için belirleyici olan günün vaktidir; komşu için belirleyici olan otlağın bolluğu ve hayvanın genişçe beslenmesidir.","focus_only":"Günün başındaki otlatma zamanını ve insan öğününü içerir.","gloss":"zamanlı otlatma ile bol otlak","neighbor_only":"Bolluk içinde dilediğince otlama, geniş otlak ve doygun beslenme koşulunu içerir.","neighbor_ref":"root_000538/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sürülerin otlamasını konu edinir."}],"source_phrase_ar":"للطعام الذي يؤكل في ذلك الوقت ضحاء (maqayis); هم يتضحون أي يتغدون والغداء الضحاء (maqayis); نتضحى أي نتغدى (ayn); تضحت الإبل أخذت في الرعي من أول النهار (ayn); الضحاء أيضا الغداء وهم يتضحون أي يتغدون (sihah); ضحى فلان غنمه أي رعاها بالضحا (sihah); تضحى أكل ضحى والضحاء والغداء لطعامهما (mufradat)","source_summary":"Kaynaklar erken aydınlık vakitte yenen öğünü ve o öğünü yeme eylemini ortak biçimde verir; aynı zaman bağı, develerin otlamaya başlamasına ve koyunların o vakitte otlatılmasına da uygulanır.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الغداء المسمى ضحاء ويتضحون بمعنى يتغدون ورعي الإبل أو الغنم في أول النهار","what_is_not_ar":"لا يدخل فيه الذبح ولا مطلق وقت الضحى بلا أكل أو رعي"},"support_links":["sup_9a27be223087b75d9b89"]},{"boundary":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"bayram gününde dinsel amaçla kesilen hayvan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne, belirli gün ve dinsel kesim koşullarını birlikte taşıyan en kısa doğal karşılığıdır.","boundary_detail":"Herhangi bir kesilmiş hayvanı değil, belirli bayram günündeki dinsel kesime ayrılan ve o gün kesilen hayvanı kapsar.","branch_image_ar":"ذبيحة يوم الأضحى","concept_gloss":"bayram gününde dinsel amaçla kesilen hayvan","contextual_glosses":[{"applicability":"Hayvanın ilgili bayram gününde kesilmek üzere ayrılmış olmasını öne çıkaran kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kesilmiş olabilme durumunu açıkça söylemez.","preserves":"Hayvanın belirli bayram gününde kesilmek üzere ayrılmasını korur."},"facet_ids":["F001"],"text":"bayram günü kesilmek üzere ayrılan hayvan","usage_role":"contextual"},{"applicability":"Koyunun ilgili günde kesilmesini bildiren söz öbeği için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvanı adlandıran genel biçimleri ve koyun dışındaki olası hayvanları kapsamaz.","preserves":"Koyunu, kesme eylemini, özel amacı ve günü korur."},"facet_ids":["F003"],"text":"bayram günü adaklık koyun kesmek","usage_role":"contextual"}],"definition":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen koyun ya da başka hayvandır. Böyle bir koyunu o gün kesme eylemi, nesne merkezli bu anlamın söz öbeğine bağlı gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bayram gününde dinsel amaçla kesilmek üzere ayrılan veya kesilen hayvan adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı hayvan için birden çok tekil ve çoğul biçim aktarılır."},{"facet_id":"F003","role":"associated_use","statement":"Bu amaçla ayrılmış bir koyunu belirli bayram gününde kesmek, ilgili söz öbeğinin eylem anlamıdır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Belirli bayram gününe bağlı olmayan daha genel sunu ve özveri anlamlarını da ekler.","collision":"Günlük dilde mecazi olarak zarar gören kişi anlamıyla da karışabilir.","fit":"broadening","loses":null,"preserves":"Dinsel amaçla sunulan veya kesilen şey yönünü korur."},"text":"kurban"}],"identity_rationale":"Kaynak ifadesi, belirli bayram gününde kesilen koyun ya da başka hayvanı, bu hayvan için kullanılan biçimleri ve koyun kesme eylemini açıkça verir. Dalın kimliği genel hayvan kesimi değil, gün ve dinsel uygulamayla sınırlandırılmış kesim nesnesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen koyun veya başka hayvan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla kesilen hayvan"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"aynı hayvan için kullanılan başka bir ad"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"dinsel hayvan kesiminin yapıldığı bayram günü veya o gün kesilen hayvanlar"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bayram gününde dinsel amaçla bir koyun kesmek"}],"lexicalization_note":"Hayvanı adlandıran biçimler dalın merkezindedir; koyun kesme eylemi yalnızca verilen söz öbeğinde ve belirli bayram günü koşuluyla tanımlanır.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; genel dinsel kesim hayvanı, genel kesme işlemi, belirli hayvan türü ve kesim sonrası işlemle kurulan dört sınır yayımlandı, yalnızca aynı tören alanını paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı belirli bayram günü ve o güne özgü adlandırmadır; komşu dal daha genel dinsel sunu alanına uzanır.","focus_only":"Belirli bayram gününü ve o gün kesilen hayvana ait ad biçimlerini şart koşar.","gloss":"bayramlık kesim hayvanı","neighbor_only":"Yaklaşma amacıyla sunulan kesim hayvanını ve dökülen kanı gün şartı olmadan daha genel biçimde kapsar.","neighbor_ref":"root_001498/B002","relation_type":"near_synonym","shared_zone":"İki dal da dinsel yakınlaşma amacıyla kesilen hayvanı anlatabilir."},{"boundary_match":"partial","distinction":"Odak nesne ve törensel zaman merkezlidir; komşu ise kesme işleminin tamamlanması merkezlidir. Her genel kesim bu dalın kapsamına girmez.","focus_only":"Belirli gün ve dinsel amaçla tanımlanan hayvanı merkez alır.","gloss":"kesim hayvanı ile kesme işlemi","neighbor_only":"Hayvanın yaşamını sona erdiren kesim işlemini, gün ve dinsel amaç koşulu olmadan merkez alır.","neighbor_ref":"root_000517/B003","relation_type":"near_neighbor","shared_zone":"Odak daldaki hayvanın gerçekleştirilmiş kullanımında bir kesme işlemi bulunur."},{"boundary_match":"partial","distinction":"Odak dal işlev ve günle, komşu dal ise hayvan türü ve sunulma durumuyla sınırlıdır; kapsamları kesişse de özdeş değildir.","focus_only":"Bayram günündeki dinsel kesime ayrılan hayvanı türden bağımsız bir işlevle adlandırır.","gloss":"bayramlık hayvan ile iri sunu hayvanı","neighbor_only":"Özellikle deve veya sığır türünden sunulan iri hayvanı adlandırır.","neighbor_ref":"root_000096/B003","relation_type":"near_neighbor","shared_zone":"Bazı iri hayvanlar her iki dalın gönderimine birden girebilir."},{"boundary_match":"thematic_only","distinction":"Odak hayvan ile kesim anına, komşu ise sonradan etin işlenmesine ve izleyen günlere aittir; anlamsal çekirdekleri ortak değildir.","focus_only":"Belirli günde kesilen hayvanı ve kesme eylemini anlatır.","gloss":"kesim ve sonrasındaki et kurutma","neighbor_only":"Kesimden sonra etin güneşte kurutulmasını ve bunu izleyen günlerin adlandırılmasını anlatır.","neighbor_ref":"root_000790/B002","relation_type":"thematic","shared_zone":"İki dal aynı bayram çevrimindeki hayvan kesimi ve et hazırlama sahnesinde yer alır."}],"source_phrase_ar":"الضحية معروفة وهي الأضحية (maqayis); أربع لغات أضحية وإضحية وضحية وأضحاة (maqayis;sihah); الضحية الأضحية والجميع الضحايا والأضاحي وهي الشاة يضحي بها يوم الأضحى (ayn); ضحى بشاة من الأضحية وهي شاة تذبح يوم الأضحى (sihah); الأضحية جمعها أضاحي وقيل ضحية وضحايا وأضحاة وأضحى (mufradat)","source_summary":"Kaynakların ortak çekirdeği, belirli bayram gününde dinsel amaçla kesilen hayvandır. Çeşitli tekil ve çoğul adlandırmalar aynı gönderime bağlanır; koyun kesme eylemi de bu gün ve amaç koşuluyla verilir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الأضحية والضحية والضحايا والأضاحي والأضحاة وما يذبح يوم الأضحى","what_is_not_ar":"لا يدخل فيه مطلق الطعام ولا الرعي ولا البروز للشمس"},"support_links":[]},{"boundary":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B005","candidate_links":[{"candidate_id":"cand_18d8300f186b147ddeb1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"kuşluk aydınlığını andıran parlak açıklık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Güneş, açık gökyüzü ve at rengi uzantılarını birleştiren temel görsel niteliği karşılar.","boundary_detail":"Dal vaktin kendisini değil, o vaktin aydınlığına benzetilen parlaklık, bulutsuz açıklık ve açık at rengini anlatır.","branch_image_ar":"ضياء الضحى وصفاؤه","concept_gloss":"kuşluk aydınlığını andıran parlak açıklık","contextual_glosses":[{"applicability":"Gece veya günün gökyüzü açıklığıyla birlikte aydınlık olduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneşin adı ve atların açık kır-boz rengi kullanımlarını karşılamaz.","preserves":"Aydınlık ile bulutsuz açıklığı birlikte korur."},"facet_ids":["F001","F003"],"text":"bulutsuz ve aydınlık","usage_role":"contextual"},{"applicability":"Atın açık, beyaza çalan kır-boz rengini anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güneş, gün ve gece aydınlığı kullanımlarını dışarıda bırakır.","preserves":"Parlak açıklığın at rengine aktarılmış yönünü korur."},"facet_ids":["F004"],"text":"açık kır-boz renkli","usage_role":"contextual"}],"definition":"Kuşluk aydınlığını andıran parlaklık ve bulutsuz açıklıktır. Bu nitelik güneşin adlandırılmasına, aydınlık gece ve güne ilişkin söz öbeklerine, ayrıca atların açık kır-boz rengine aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuşluk aydınlığını andıran parlak ve açık görünüm temel niteliktir."},{"facet_id":"F002","role":"extension","statement":"Güneş, verdiği güçlü aydınlık nedeniyle bu nitelikle adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Bulutsuz ve aydınlık gece ile gün, açıklık ve ışık niteliğini birlikte taşır."},{"facet_id":"F004","role":"extension","statement":"Atlarda erkek ve dişi için kullanılan açık kır-boz renk adları, parlak açıklığın renk alanına aktarımıdır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kaynağı ve niteliği sınırsız olan her türlü ışığı kapsama ekler.","collision":"At rengindeki açık kır-boz görünümü doğrudan karşılayamaz.","fit":"broadening","loses":null,"preserves":"Aydınlık ve parlaklık yönünü korur."},"text":"ışık"}],"identity_rationale":"Kaynak ifadesi güneşin bu adla anılmasını, bulutsuz ve aydınlık gece ile günü, ayrıca atlarda açık kır-boz rengi birlikte aktarır. Çerçevedeki kuşluk aydınlığı ve açıklık bunları birleştiren niteliktir; at rengi doğrudan ışık değil, bu açık parlak niteliğin renk alanına aktarımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güneş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gece"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bulutsuz, berrak ve aydınlık gece"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bulutsuz ve aydınlık gün"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli at"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"açık kır-boz renkli kısrak"}],"lexicalization_note":"Aydınlık ve açıklık ortak niteliktir; güneş adı, bulutsuz gece ve gün söz öbekleri ile at rengi biçimleri kendi özel kapsamlarında tutulur.","neighbor_coverage_note":"Verilen bütün komşular değerlendirildi; açık gökyüzü, aydınlanma, genel ışık ve aynı kökün zaman dalı temel sınırları gösterdiği için seçildi, yalnızca belirli ışık kaynaklarını anlatan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal niteliği geceye, güneş adına ve at rengine taşır; komşu dal gündüz beyazlığı ve karanlığın açılması çevresinde kalır.","focus_only":"Güneş adı, aydınlık gece ve atların açık kır-boz rengi uzantılarını kapsar.","gloss":"aydınlık ve açık gökyüzü","neighbor_only":"Gündüzün beyazlığı ile gökyüzü açıklığının karanlığı giderip günü yaymasını merkez alır.","neighbor_ref":"root_000256/B007","relation_type":"near_synonym","shared_zone":"İki dal da gün ışığının parlaklığı ile gökyüzünün açıklığını birleştirir."},{"boundary_match":"partial","distinction":"Odak kuşluk benzeri parlak açıklığa ve renk uzantısına dayanır; komşu karanlıktan aydınlığa çıkışı ve yüz parıltısını da kapsayan başka bir gelişim çizgisidir.","focus_only":"Bulutsuz geceyi ve atların açık kır-boz rengini içerir.","gloss":"aydınlanıp belirginleşme","neighbor_only":"Şafak aydınlığını, yüzün parlamasını ve karanlıktan sonra belirginleşen zamanı içerir.","neighbor_ref":"root_000712/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de aydınlık, beyazlık ve açık görünüm alanında buluşur."},{"boundary_match":"partial","distinction":"Odak belirli bir parlak-açık görünüm niteliğidir; komşu ise kaynağı ne olursa olsun ışığın yayılması ve bir şeyi aydınlatmasıdır.","focus_only":"Bulutsuz açıklığı ve atların açık kır-boz rengini kuşluk ışığı benzerliğiyle birleştirir.","gloss":"parlak açıklık ile yayılan ışık","neighbor_only":"Ateş, kandil, şimşek ve tan gibi çok çeşitli kaynaklardan yayılan ışığı ve aydınlatma eylemini kapsar.","neighbor_ref":"root_000919/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı ışık veren veya aydınlık görünen şeylerdir."},{"boundary_match":"field_only","distinction":"Bir dal görsel nitelik, diğeri zamansal bölümdür. Aydınlık başka zamanlara ve at rengine taşınabilirken zaman anlamı taşınmaz.","focus_only":"Kuşluk ışığına benzer parlaklık ve açıklık niteliğini anlatır.","gloss":"kuşluk aydınlığı ile kuşluk vakti","neighbor_only":"Kuşluk zamanını ve onun gündüz içindeki aşamalarını anlatır.","neighbor_ref":"root_000904/B001","relation_type":"same_field","shared_zone":"Odak niteliğin benzetme kaynağı, komşu dalın adlandırdığı zamanın ışığıdır."}],"source_phrase_ar":"تسمى الشمس الضحاء (ayn); ليلة إضحيانة وضحياء أي مضيئة لا غيم فيها (maqayis); ليلة ضحياء مضيئة لا غيم فيها وليلة إضحيانة (sihah); يوم إضحيان مضيء لا غيم فيه (ayn); الأضحى من الخيل الأشهب والأنثى ضحياء (sihah); ليلة إضحيانة وضحياء مضيئة إضاءة الضحى (mufradat)","source_summary":"Kaynakların toplu verisi kuşluk ışığına benzeyen parlak ve bulutsuz açıklığı gösterir. Güneş adı ile aydınlık gece ve gün bu niteliği doğrudan taşırken, atların açık kır-boz rengi görsel bir uzantı oluşturur.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الشمس المسماة الضحاء والليلة المضيئة الصافية والبياض الأشهب في الخيل","what_is_not_ar":"لا يدخل فيه مجرد وقت الضحى ولا البروز المكاني"},"support_links":["sup_15457aeff04af9b5fd88"]},{"boundary":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000904/B006","candidate_links":[{"candidate_id":"cand_c13526b1fd246335bb56","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","surface_ar":"ضُّحَىٰ"}],"gloss":"yumuşak davranıp acele etmemek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}}],"root_ar":"ض ح و","root_id":"root_000904","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki kayıtlı yapının ortak çekirdeği olan davranış yumuşaklığını ve hızın düşürülmesini birlikte karşılar.","boundary_detail":"Bu dal genel görünürlük veya gündüz anlamını taşımaz; yalnızca yumuşak davranma ve acele etmeme bildiren kayıtlı kullanımları kapsar.","branch_image_ar":"الرفق والإمهال","concept_gloss":"yumuşak davranıp acele etmemek","contextual_glosses":[{"applicability":"Bir işin sertlik ve acele olmadan ele alınmasını anlatan bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğrudan bir yavaşlama buyruğu olma işlevini karşılamaz.","preserves":"İşin yumuşak ve acele edilmeden yürütülmesini korur."},"facet_ids":["F001","F002"],"text":"işi ağırdan ve yumuşaklıkla yürütmek","usage_role":"contextual"},{"applicability":"Karşıdakinden hızını düşürmesini isteyen doğrudan buyruk bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi yumuşak davranarak yürütme anlamını tek başına taşımaz.","preserves":"Acele etmeme ve yavaşlama buyruğunu korur."},"facet_ids":["F003"],"text":"acele etme, yavaş ol","usage_role":"contextual"}],"definition":"Bir işi sertlik göstermeden, yumuşak davranarak ve acele etmeden yürütmektir. Bir kullanım eylem biçimini, diğeri ise doğrudan yavaşlama ve acele etmeme buyruğunu bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iş karşısında yumuşak davranmak ve onu aceleye getirmemek temel anlamdır."},{"facet_id":"F002","role":"specialization","statement":"Bir işi yumuşaklıkla ve ağırdan alarak yürütme, belirli bir söz öbeğine bağlı kullanımdır."},{"facet_id":"F003","role":"specialization","statement":"Acele etmeme ve yavaşlama buyruğu, diğer kayıtlı yapının doğrudan işlevini oluşturur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Eylemi tümüyle durdurup zaman geçmesini bekleme anlamını ekler.","collision":null,"fit":"displacement","loses":"Yumuşak davranarak işi sürdürme ve doğrudan yavaşlama buyruğunu kaybeder.","preserves":"Hızı düşürme ve acele etmeme yönünü kısmen korur."},"text":"beklemek"}],"identity_rationale":"Kaynak ifadesi bir iş karşısında yumuşak davranmayı ve acele etmeme buyruğunu doğrudan verir. Çerçevedeki yumuşaklık ve ağırdan alma bu iki kullanımı doğru bir ortak alanda tutar; ancak anlam yalın köke değil, verilen söz öbeklerine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bir işi yumuşak davranarak ve ağırdan alarak yürütmek"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"acele etme, yavaş ol"}],"lexicalization_note":"Yumuşak davranma ve acele etmeme iki kayıtlı yapı içinde tanımlanır; bunlardan sınırsız bir yalın kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; bekleme, genel yumuşaklık, geniş acele etmeme alanı ve başka bir yapıdaki yumuşak davranma en yararlı sınırları verdi, daha uzak ağırbaşlılık ve özdenetim adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda bekleme zorunlu değildir; iş yumuşakça sürdürülebilir. Komşu dal ise bekleme ve oyalanma yönünü açıkça içerir.","focus_only":"Yumuşak davranma ile acele etmeme buyruğunu iki kayıtlı yapı içinde birleştirir.","gloss":"yavaş davranıp beklemek","neighbor_only":"Bekleme eylemini doğrudan anlam alanına alır.","neighbor_ref":"root_000583/B008","relation_type":"near_synonym","shared_zone":"İki dal da hızın düşürülmesini ve bir işte zaman tanınmasını anlatır."},{"boundary_match":"partial","distinction":"Odak zamanlama ve acele etmeme yönünü de taşır ve belirli yapılara bağlıdır; komşu ise genel davranış yumuşaklığında daha geniştir.","focus_only":"Acele etmeme ve yavaşlama buyruğunu özellikle içerir.","gloss":"yumuşak ve ölçülü davranma","neighbor_only":"Sertliğin karşıtı olan genel davranış yumuşaklığını, kişilik niteliğini ve özenli uygulamayı daha geniş biçimde kapsar.","neighbor_ref":"root_000583/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da sertlikten kaçınarak yumuşak davranmayı anlatır."},{"boundary_match":"partial","distinction":"Odak dalın yumuşak davranma bileşeni ve yapı bağı önemlidir; komşu dal ise hız, bekleme ve kendini tutma yönlerinde daha geniştir.","focus_only":"Bir iş karşısındaki yumuşak davranışı kayıtlı söz öbekleriyle sınırlar.","gloss":"ağırdan alma ve acele etmeme","neighbor_only":"Gecikme, bekleme, ağırbaşlılık ve öfkeyi dizginleme gibi daha geniş acele etmeme alanını kapsar.","neighbor_ref":"root_000063/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işi aceleye getirmemeyi içerir."},{"boundary_match":"partial","distinction":"Odak dal yumuşaklığın yanında hızın düşürülmesini açıkça içerir; komşu kart yalnızca yönelinen şeye yumuşak davranmayı bildirir.","focus_only":"Acele etmeme buyruğunu ve işi ağırdan almayı da kapsar.","gloss":"bir şeye yumuşak davranma","neighbor_only":"Yumuşak davranmayı tek bir başka söz öbeği içinde, yönelinen kişi veya şeyle ilişkilendirir.","neighbor_ref":"root_001017/B008","relation_type":"near_synonym","shared_zone":"İki dal belirli bir yapı içinde bir işe veya şeye yumuşak davranmayı anlatır."}],"source_phrase_ar":"ضحيت عن الأمر إذا رفقت (maqayis;sihah); ضح رويدا أي لا تعجل (sihah)","source_summary":"Kaynakların ortak verisi, bir işte yumuşak davranma ile acele etmeyip ağırdan alma yönlerini birleştirir. Biri işin yürütülüşünü, diğeri doğrudan yavaşlama buyruğunu anlatan iki sınırlı kullanım vardır.","sources":["MQ","SI"],"what_is_ar":"يدخل فيه ضحيت عن الأمر بمعنى رفقت وضح رويدا بمعنى لا تعجل","what_is_not_ar":"لا يدخل فيه أصل البروز ولا الضحى ولا الأضحية"},"support_links":["sup_cb4152fbad62155754fe"]}],"candidate_inventory":[{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_26298ddb9604f645d168","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:bound-form-governance","source_type":"word_analysis","support_ids":["sup_145753211f7e253cc117","sup_88cff3af57beecaca0e1"],"title":"one attached letter carries clause force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_ad58a24ef529a4e91eca","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:delayed-oath-answer","source_type":"word_analysis","support_ids":["sup_67f8c6e29c133c275be6","sup_88cff3af57beecaca0e1"],"title":"oath answer waits beyond the ayah","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_817a0f8b873902828c81","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:fresh-oath-opener","source_type":"word_analysis","support_ids":["sup_613421e34abff2f11144","sup_88cff3af57beecaca0e1"],"title":"fresh discourse opens as oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_8b9ac8672580f8d60a23","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:fused-recitation-beat","source_type":"word_analysis","support_ids":["sup_88cff3af57beecaca0e1","sup_c7fa0b7602326f2a7807"],"title":"particle fuses into the brightness noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_e4e88b2028fbed1a722b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:oath-genitive-launch","source_type":"word_analysis","support_ids":["sup_88cff3af57beecaca0e1","sup_ab6f6392ede7cd626341"],"title":"opening particle governs the oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_078defadb341a7e125c4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:paired-oath-series","source_type":"word_analysis","support_ids":["sup_88cff3af57beecaca0e1","sup_eef6ad182837f222030c"],"title":"first oath particle prepares the second","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_c7b9d4080ef8e4a985ee","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"93:1:1:structural-hinge","source_type":"word_analysis","support_ids":["sup_8525927d7982e3e979d9","sup_88cff3af57beecaca0e1"],"title":"small word holds several opening functions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:1","qac_refs":["93:1:1:1"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_331c950f70f8fdba1997","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:definite-form-not-possessive","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_c950e92c251b95695499"],"title":"article definiteness replaces possessive binding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_337246805e23f188b9c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:definite-standalone-brightness","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_b5327d1ffcac8ea894e5"],"title":"known brightness stands by itself","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_e2156944a6052b8a9334","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:durative-nominal-brightness","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_50020df01af0126430c9"],"title":"noun names a luminous condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_dd5964483d30106ae3b0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:forenoon-disclosure-field","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_5d5a3a8f0fb5c2b9c0a3"],"title":"forenoon brightness carries disclosure pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_278d864c47afd14f2fa8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:light-night-witness-pair","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_ac532618fd9525c1f6ae"],"title":"brightness anticipates night","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_c929e9519fa084428184","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:load-bearing-convergence","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_65a5eccf59e98b0980da"],"title":"grammar, meaning, sound, and rarity converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_236ea644144816c13643","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:parallel-with-sun-brightness-oath","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_710b87323628a583a910"],"title":"93:1 isolates what 91:1 attaches to the sun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_e92ee2f6589f5752f9c6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:positive-exposure-witness","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_42896adb10de583fa49d"],"title":"exposure becomes positive witness here","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_3372584dd129aa980fbf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:quranic-distribution-and-rarity","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_58e9602df02cf29135f3"],"title":"rare root appears mostly as brightness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_941b7c13c841c166fcfa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:ritual-time-background","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_c385bcc801911ed10ca7"],"title":"sacrifice derivative stays background","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_8d690c5b282ffa689ca3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_517f5f85eb1bafe34094"],"title":"heavy onset releases into long cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_7c96759a56ff58411ca4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:spreading-and-transition-pressure","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_e2cb6e75e76cc03dc3fd"],"title":"light spreads without making the word a verb","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_4725fc6ed9b143fed602","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:sworn-object-delayed-answer","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_987efe734d14cc7b5d56"],"title":"brightness is the sworn witness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_096b3fac55426600ceb3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:time-and-manifestation-double-payoff","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_a6fb3ab050f299e92f2a"],"title":"time and manifestation work together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:2"],"branch_refs":[],"candidate_id":"cand_fe535ade8e97e42f4df8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:2:time-noun-in-oath-role","source_type":"word_analysis","support_ids":["sup_185deb28baa4d62fe07a","sup_ee6cc2de2c8cc966e516"],"title":"time-light term becomes oath object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"93:1:2","qac_refs":["93:1:1:2","93:1:1:3"],"status":"accepted"}},{"anchor_refs":["93:1:1"],"branch_refs":[],"candidate_id":"cand_6cbcb42e117b08c6ee2d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000904"],"scope":"focus_ayah","source_local_id":"93:1:1:3","source_type":"qac_morpheme","support_ids":["sup_4c63f9dd363feee59e76"],"title":"QAC root occurrence: ض ح و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["93:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B001"],"candidate_id":"cand_9625e878390dc619a322","commentary_obligation":"review","hft_ref":"hft_07c47bfdf709cc867592","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_duha_extended_ascent","source_type":"hft","support_ids":["sup_8f133d10337c648071e8"],"title":"b_duha_extended_ascent","trust":"legacy_unbound"},{"anchor_refs":["93:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B002"],"candidate_id":"cand_ec156a18037e61a4e86d","commentary_obligation":"review","hft_ref":"hft_86512daf7a0baa25fb7c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_duha_public_exposure","source_type":"hft","support_ids":["sup_2568c8300d64267c6352"],"title":"b_duha_public_exposure","trust":"legacy_unbound"},{"anchor_refs":["93:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B003"],"candidate_id":"cand_090e0b9fcaf784963274","commentary_obligation":"review","hft_ref":"hft_799d0c08fba06bf9ac0d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_duha_provisioning_window","source_type":"hft","support_ids":["sup_9a27be223087b75d9b89"],"title":"b_duha_provisioning_window","trust":"legacy_unbound"},{"anchor_refs":["93:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B005"],"candidate_id":"cand_18d8300f186b147ddeb1","commentary_obligation":"review","hft_ref":"hft_0e3600ab92aaf833c49a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_duha_clear_legibility","source_type":"hft","support_ids":["sup_15457aeff04af9b5fd88"],"title":"b_duha_clear_legibility","trust":"legacy_unbound"},{"anchor_refs":["93:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"93:1","branch_refs":["root_000904/B006"],"candidate_id":"cand_c13526b1fd246335bb56","commentary_obligation":"review","hft_ref":"hft_e4320f687a3a181c7fcc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_duha_gentle_delay","source_type":"hft","support_ids":["sup_cb4152fbad62155754fe"],"title":"b_duha_gentle_delay","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلضُّحَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"93:1:1:1","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:1:1:2","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","root_ar":"ض ح و","surface_ar":"ضُّحَىٰ"}],"word_analysis_qac_refs":[["93:1:1:1"],["93:1:1:2","93:1:1:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["93:1:1","93:1:2"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلضُّحَىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"93:1:1:1","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"93:1:1:2","qac_word_ref":"93:1:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"ضُحًى","morph_features":"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"93:1:1:3","qac_word_ref":"93:1:1","root_ar":"ض ح و","surface_ar":"ضُّحَىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["93:1:1:1"],["93:1:1:2","93:1:1:3"]],"word_analysis_refs":["93:1:1","93:1:2"],"word_rows":[{"analysis_record_ref":"93:1:1","analytic_gloss_range_en":"surah-opening oath particle that governs the following definite noun, launches fresh discourse, and keeps the oath answer beyond this ayah","analytic_root_gloss_range_en":null,"qac_refs":["93:1:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"93:1:2","analytic_gloss_range_en":"the definite forenoon brightness as a sworn witness: a recognized, self-standing light/time phenomenon with exposure and disclosure pressure, not a local sacrifice sense or mere clock point","analytic_root_gloss_range_en":"forenoon daylight, visible exposure, early-day activity, Adha sacrifice terms, brightness, and reviewed slow/gentle expressions; locally the forenoon daylight and exposure-brightness branches are relevant, while sacrifice and meal branches remain derivative background","qac_refs":["93:1:1:2","93:1:1:3"],"root":{"arabic":"ض ح و","transliteration":"ḍ-ḥ-w"},"surface":{"arabic":"ٱلضُّحَىٰ","transliteration":"aḍ-ḍuḥā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":2,"words_total":2,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["93:1"],"branch_refs":["root_000904/B001"],"candidate_id":"cand_9625e878390dc619a322","evidence_scope":"focus_ayah","hft_ref":"hft_07c47bfdf709cc867592","item_id":"b_duha_extended_ascent","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_duha_extended_ascent","support_id":"sup_8f133d10337c648071e8"},{"anchor_refs":["93:1"],"branch_refs":["root_000904/B002"],"candidate_id":"cand_ec156a18037e61a4e86d","evidence_scope":"focus_ayah","hft_ref":"hft_86512daf7a0baa25fb7c","item_id":"b_duha_public_exposure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_duha_public_exposure","support_id":"sup_2568c8300d64267c6352"},{"anchor_refs":["93:1"],"branch_refs":["root_000904/B003"],"candidate_id":"cand_090e0b9fcaf784963274","evidence_scope":"focus_ayah","hft_ref":"hft_799d0c08fba06bf9ac0d","item_id":"b_duha_provisioning_window","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_duha_provisioning_window","support_id":"sup_9a27be223087b75d9b89"},{"anchor_refs":["93:1"],"branch_refs":["root_000904/B005"],"candidate_id":"cand_18d8300f186b147ddeb1","evidence_scope":"focus_ayah","hft_ref":"hft_0e3600ab92aaf833c49a","item_id":"b_duha_clear_legibility","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_duha_clear_legibility","support_id":"sup_15457aeff04af9b5fd88"},{"anchor_refs":["93:1"],"branch_refs":["root_000904/B006"],"candidate_id":"cand_c13526b1fd246335bb56","evidence_scope":"focus_ayah","hft_ref":"hft_e4320f687a3a181c7fcc","item_id":"b_duha_gentle_delay","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_duha_gentle_delay","support_id":"sup_cb4152fbad62155754fe"}],"diagnostics":[],"lane_counts":{"global":11,"macro":14,"micro":5},"packet_summary":{"ayah_count":11,"focus_ref":"93:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"و ج د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001626","furuq_root_norm":"و ج د","furuq_source_root_norm":"و ج د","is_dominant":true,"target_occurrences":61,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000227","furuq_root_norm":"ج د د","furuq_source_root_norm":"ج د د","is_dominant":false,"target_occurrences":10,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ء ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000661","furuq_root_norm":"س ء ل","furuq_source_root_norm":"س أ ل","is_dominant":true,"target_occurrences":118,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000736","furuq_root_norm":"س ل ل","furuq_source_root_norm":"س ل ل","is_dominant":false,"target_occurrences":2,"target_rank":2}]}],"window":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"93:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"93:1","lane":"micro","linguistic_source_ref":"93:1","surface_ref":"93:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"93:1","target_tokens":[["Kuşluk",["93:1:1"]],["vaktine",["93:1:1"]],["andolsun",["93:1:1"]]],"text":"Kuşluk vaktine andolsun."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s093-p01-001-011","label":"Whole surah","number":1,"refs":["93:1","93:2","93:3","93:4","93:5","93:6","93:7","93:8","93:9","93:10","93:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:bound-form-governance","source_type":"word_analysis","support_id":"sup_145753211f7e253cc117","text":"{\"blocking_evidence\":null,\"headline\":\"one attached letter carries clause force\",\"reader_payoff\":\"The reader notices that a minimal bound particle replaces an explicit oath verb while still controlling the whole opening mode.\",\"reason\":\"The formulaic oath ellipsis is strongly licensed, so the CRITICAL emphasis on compact bound morphology has local grammatical support.\",\"representative_source_ids\":[\"QF-5df1f398\",\"QT-bb83f6c0\",\"QT-eeb84e7e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2","source_type":"word_analysis","support_id":"sup_185deb28baa4d62fe07a","text":"{\"gloss_range\":\"the definite forenoon brightness as a sworn witness: a recognized, self-standing light/time phenomenon with exposure and disclosure pressure, not a local sacrifice sense or mere clock point\",\"prose\":\"{{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) is the definite brightness named as the oath object. It is not a predicate inside this ayah and not a loose time adverb; under the oath particle it becomes the sworn witness whose answer waits for 93:3. The article makes the brightness recognizable, while the standalone form keeps it from being explicitly possessed by the sun as in the related oath scene at 91:1. Lexically, the word stays anchored in forenoon brightness, but the root's exposure and visibility field makes that brightness feel like disclosure: light spreads, things come into view, and the open world becomes perceptible. That exposure field is locally positive because the word is a sworn witness here, even though sun-exposure can be harmful in another setting (20:119). The noun form also matters: {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) presents a durative luminous condition rather than a punctual forenoon instant or a verb of entering daylight. Its Quranic distribution makes that nominal choice marked: this rare root appears mostly in brightness nouns, so the standalone oath presents light as a named state. Sacrifice and forenoon-meal derivatives remain background evidence that the root can organize timed action; they do not turn this ayah into a sacrifice or meal statement. The word then points forward to the night term in 93:2, completing a light/night witness pair. Its sound helps close the first beat: the assimilated, geminated onset and emphatic-pharyngeal texture give the noun weight, and the long final vowel opens into the cadence that the next oath ending answers.\",\"root_display\":\"{{ar:ض ح و}} ({{tr:ḍ-ḥ-w}})\",\"root_gloss_range\":\"forenoon daylight, visible exposure, early-day activity, Adha sacrifice terms, brightness, and reviewed slow/gentle expressions; locally the forenoon daylight and exposure-brightness branches are relevant, while sacrifice and meal branches remain derivative background\",\"surface_display\":\"{{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:positive-exposure-witness","source_type":"word_analysis","support_id":"sup_42896adb10de583fa49d","text":"{\"blocking_evidence\":null,\"headline\":\"exposure becomes positive witness here\",\"reader_payoff\":\"The reader notices that exposure is not harmful in this oath setting; the brightness serves as evidence by making concealment impossible, unlike the negative sun-exposure scene (20:119).\",\"reason\":\"The broader root field includes exposure and sun-heat, but the local oath frame gives the selected brightness a positive evidentiary function; the negative comparison at 20:119 remains contrastive, not controlling.\",\"representative_source_ids\":[\"QS-37d86d9c\",\"QS-cc2efa89\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"93:1:1:3","source_type":"qac_morpheme","support_id":"sup_4c63f9dd363feee59e76","text":"{\"lemma_ar\":\"ضُحًى\",\"morph_features\":\"STEM|POS:N|LEM:DuHFY|ROOT:DHw|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"93:1:1:3\",\"qac_word_ref\":\"93:1:1\",\"root_ar\":\"ض ح و\",\"surface_ar\":\"ضُّحَىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:durative-nominal-brightness","source_type":"word_analysis","support_id":"sup_50020df01af0126430c9","text":"{\"blocking_evidence\":null,\"headline\":\"noun names a luminous condition\",\"reader_payoff\":\"The reader notices that the form presents a durative brightness-state rather than a single clock instant or a verb of becoming exposed.\",\"reason\":\"QAC marks a definite NOUN_ABSTRACT, contextual evidence shows this root-form pattern is mostly nominal in the Quranic distribution, and V4 supports the forenoon-brightness sense; non-surface Form IV pressure is kept as background transition coloring.\",\"representative_source_ids\":[\"QS-62fe409e\",\"QF-73170379\",\"QF-d5b6f991\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:sound-and-cadence","source_type":"word_analysis","support_id":"sup_517f5f85eb1bafe34094","text":"{\"blocking_evidence\":null,\"headline\":\"heavy onset releases into long cadence\",\"reader_payoff\":\"The reader notices the sound-shape of the word: assimilated pressure at the beginning, emphatic weight in the middle, and a sustained final vowel that prepares the next oath ending.\",\"reason\":\"The written-recited form has the definite article, sun-letter assimilation, geminated emphatic onset, and final long vowel, so the CRITICAL cadence observations match the local surface.\",\"representative_source_ids\":[\"QF-a9ed33d3\",\"QP-171b158c\",\"MP-56c11e28\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:quranic-distribution-and-rarity","source_type":"word_analysis","support_id":"sup_58e9602df02cf29135f3","text":"{\"blocking_evidence\":null,\"headline\":\"rare root appears mostly as brightness\",\"reader_payoff\":\"The reader notices that this rare Quranic root is presented here in its dominant nominal brightness pattern, making the standalone oath use feel marked.\",\"reason\":\"Contextual evidence reports five NOUN_ABSTRACT instances for the exact root-form profile, with the local word matching that nominal pattern.\",\"representative_source_ids\":[\"MS-d7601d76\",\"QF-1e3f0f6a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:forenoon-disclosure-field","source_type":"word_analysis","support_id":"sup_5d5a3a8f0fb5c2b9c0a3","text":"{\"blocking_evidence\":null,\"headline\":\"forenoon brightness carries disclosure pressure\",\"reader_payoff\":\"The reader notices that the local forenoon brightness is also a visibility event: the world is exposed, opened, and made perceptible by light.\",\"reason\":\"V4 supports accepted branches for forenoon daylight, exposure to sun, and clear brightness; the topic is narrowed so exposure and disclosure color the local forenoon sense rather than replacing it with an abstract-only reading.\",\"representative_source_ids\":[\"QS-04fcdb1b\",\"QS-0e62637b\",\"MS-8dafc075\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:fresh-oath-opener","source_type":"word_analysis","support_id":"sup_613421e34abff2f11144","text":"{\"blocking_evidence\":null,\"headline\":\"fresh discourse opens as oath\",\"reader_payoff\":\"The reader notices that the surah begins with a fresh discourse launch and oath force at once, so the opening is neither bare resumption nor a detached oath formula.\",\"reason\":\"The sentence-initial position and oath grammar support the CRITICAL claim that the particle starts a new surah unit while carrying qasam force.\",\"representative_source_ids\":[\"QS-c1f86cd0\",\"QT-58dbb933\",\"MT-f022a429\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:load-bearing-convergence","source_type":"word_analysis","support_id":"sup_65a5eccf59e98b0980da","text":"{\"blocking_evidence\":null,\"headline\":\"grammar, meaning, sound, and rarity converge\",\"reader_payoff\":\"The reader notices why the word feels load-bearing: it is definite, semantically revelatory, acoustically forceful, and rare as a standalone oath term.\",\"reason\":\"The synthesis row accurately gathers already supported local features without adding an unsupported branch.\",\"representative_source_ids\":[\"QY-f8e91443\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:delayed-oath-answer","source_type":"word_analysis","support_id":"sup_67f8c6e29c133c275be6","text":"{\"blocking_evidence\":null,\"headline\":\"oath answer waits beyond the ayah\",\"reader_payoff\":\"The reader notices that the first ayah gives the sworn witness while withholding the asserted response until 93:3 and extending that response at 93:4.\",\"reason\":\"The oath particle and following noun form a complete witness phrase, but attachment evidence and the CRITICAL rows correctly preserve the pragmatic incompletion of the delayed oath response.\",\"representative_source_ids\":[\"QG-a73995cd\",\"QI-8fe5a7bb\",\"QB-39a0ae8c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:parallel-with-sun-brightness-oath","source_type":"word_analysis","support_id":"sup_710b87323628a583a910","text":"{\"blocking_evidence\":null,\"headline\":\"93:1 isolates what 91:1 attaches to the sun\",\"reader_payoff\":\"The reader notices that this oath isolates brightness itself, whereas the related oath at 91:1 binds the brightness to the sun.\",\"reason\":\"The CRITICAL rows provide the concrete 91:1 parallel, and the local grammar of 93:1 supports the contrast because {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) is standalone rather than suffixed.\",\"representative_source_ids\":[\"MI-3491361e\",\"QH-fa252530\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:structural-hinge","source_type":"word_analysis","support_id":"sup_8525927d7982e3e979d9","text":"{\"blocking_evidence\":null,\"headline\":\"small word holds several opening functions\",\"reader_payoff\":\"The reader notices that the smallest word is the hinge where fresh opening, oath force, bound-form compression, and forward pressure meet.\",\"reason\":\"The local evidence supports oath grammar, formulaic ellipsis, and forward oath scope, so the synthesis row is kept as a concise convergence topic.\",\"representative_source_ids\":[\"QT-b8e3edf6\",\"QY-b11c2df7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1","source_type":"word_analysis","support_id":"sup_88cff3af57beecaca0e1","text":"{\"gloss_range\":\"surah-opening oath particle that governs the following definite noun, launches fresh discourse, and keeps the oath answer beyond this ayah\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the surah as oath grammar, not as ordinary coordination alone. The particle governs {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) as the sworn-by object and leaves the oath act formulaically unspoken, so a single attached letter does the work an explicit oath verb might otherwise do. It also begins fresh discourse: the opening feels connective without needing a previous clause, giving the surah an immediate sworn-opening force. Because the answer is delayed, the first ayah is not a self-contained statement; it leans forward to the response at 93:3 and its extension at 93:4. The same opening particle also prepares the repeated oath particle of 93:2, making the brightness and the night a paired witness structure. In recitation, the small particle fuses into {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}), so the grammar of dependency is heard as one compact opening beat.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:sworn-object-delayed-answer","source_type":"word_analysis","support_id":"sup_987efe734d14cc7b5d56","text":"{\"blocking_evidence\":null,\"headline\":\"brightness is the sworn witness\",\"reader_payoff\":\"The reader notices that {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) is elevated from scene-setting brightness into the sworn witness whose answer waits beyond the ayah.\",\"reason\":\"QAC and attachment evidence place the definite noun under oath governance, while the ayah has no overt local predicate after the noun.\",\"representative_source_ids\":[\"QG-336a6a38\",\"QG-7c37fdef\",\"QI-17d11eec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:time-and-manifestation-double-payoff","source_type":"word_analysis","support_id":"sup_a6fb3ab050f299e92f2a","text":"{\"blocking_evidence\":null,\"headline\":\"time and manifestation work together\",\"reader_payoff\":\"The reader notices that the word is both concrete time of day and manifestation by light, which is why it can pair meaningfully with night in the oath frame.\",\"reason\":\"The local noun remains the concrete oath object, while accepted dictionary branches for forenoon daylight and exposure support the CRITICAL payoff that clock-time and manifestation are both relevant.\",\"representative_source_ids\":[\"QS-0ad7b193\",\"QS-7110525a\",\"QS-8ad106da\",\"QS-bb828a74\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:oath-genitive-launch","source_type":"word_analysis","support_id":"sup_ab6f6392ede7cd626341","text":"{\"blocking_evidence\":null,\"headline\":\"opening particle governs the oath object\",\"reader_payoff\":\"The reader notices that {{ar:وَ}} ({{tr:wa}}) makes {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) a governed sworn witness, not a loose opening noun or simple conjunction.\",\"reason\":\"QAC identifies the first word as conjunction and oath particle, while attachment evidence marks oath scope and a strongly licensed formulaic ellipsis of the oath verb.\",\"representative_source_ids\":[\"QG-61b0e698\",\"QG-7bb4fb3e\",\"MG-e6b1e5b7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:light-night-witness-pair","source_type":"word_analysis","support_id":"sup_ac532618fd9525c1f6ae","text":"{\"blocking_evidence\":null,\"headline\":\"brightness anticipates night\",\"reader_payoff\":\"The reader notices that {{ar:ٱلضُّحَىٰ}} ({{tr:aḍ-ḍuḥā}}) is designed to be completed by its opposite, the night term in the next oath (93:2).\",\"reason\":\"The next ayah supplies the paired night witness, so the CRITICAL forward bridge by semantic opposition is locally coherent.\",\"representative_source_ids\":[\"MT-aae1b237\",\"QB-ee5faaee\",\"QB-f6677162\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:definite-standalone-brightness","source_type":"word_analysis","support_id":"sup_b5327d1ffcac8ea894e5","text":"{\"blocking_evidence\":null,\"headline\":\"known brightness stands by itself\",\"reader_payoff\":\"The reader notices that the oath invokes recognizable brightness as a self-standing phenomenon, not an indefinite light or a brightness explicitly possessed by the sun.\",\"reason\":\"The article and standalone noun form support definiteness and non-possessive structure; the row's more specific claim about the Prophet's experience is narrowed to shared recognizability because the local grammar itself does not prove that biographical specification.\",\"representative_source_ids\":[\"QG-b15af085\",\"QG-e24074e5\",\"MG-6ab7a5f9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:ritual-time-background","source_type":"word_analysis","support_id":"sup_c385bcc801911ed10ca7","text":"{\"blocking_evidence\":null,\"headline\":\"sacrifice derivative stays background\",\"reader_payoff\":\"The reader notices that the root can mark an action-organizing time window, while the local ayah remains an oath by forenoon brightness, not a sacrifice statement.\",\"reason\":\"V4 includes accepted Adha-sacrifice and forenoon-meal branches, but the local surface is the definite brightness noun under oath governance; derivative ritual-time value is retained only as background temporal precision.\",\"representative_source_ids\":[\"QS-958ee502\",\"MS-81f238ed\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:fused-recitation-beat","source_type":"word_analysis","support_id":"sup_c7fa0b7602326f2a7807","text":"{\"blocking_evidence\":null,\"headline\":\"particle fuses into the brightness noun\",\"reader_payoff\":\"The reader notices that the opening oath is heard as a compact particle-plus-noun beat, with the small particle immediately bound to its witness.\",\"reason\":\"The surface sequence places the bound particle directly before the hamzat-waṣl and assimilated definite noun, matching the CRITICAL sound observation.\",\"representative_source_ids\":[\"QF-e2e2535a\",\"QP-25fd0520\",\"QP-c9877ab5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:definite-form-not-possessive","source_type":"word_analysis","support_id":"sup_c950e92c251b95695499","text":"{\"blocking_evidence\":null,\"headline\":\"article definiteness replaces possessive binding\",\"reader_payoff\":\"The reader notices that definiteness comes through the article, so the brightness is recognizable without being grammatically attached to a named source.\",\"reason\":\"QAC and noun-instance evidence show a definite standalone noun with no iḍāfa dependent or possessive suffix.\",\"representative_source_ids\":[\"QF-4357684a\",\"QF-f939ce0f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:spreading-and-transition-pressure","source_type":"word_analysis","support_id":"sup_e2cb6e75e76cc03dc3fd","text":"{\"blocking_evidence\":null,\"headline\":\"light spreads without making the word a verb\",\"reader_payoff\":\"The reader notices a sense of light extending and arriving into visibility, while the local form still names the resulting brightness rather than predicating an action.\",\"reason\":\"The CRITICAL rows preserve valid root pressure, but QAC keeps the local word as a noun, not a Form IV verb or independent process predicate.\",\"representative_source_ids\":[\"QS-35193fe1\",\"QS-ec154929\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:2:time-noun-in-oath-role","source_type":"word_analysis","support_id":"sup_ee6cc2de2c8cc966e516","text":"{\"blocking_evidence\":null,\"headline\":\"time-light term becomes oath object\",\"reader_payoff\":\"The reader notices the role split: a temporal light-word fills the formal oath-object slot and closes the ayah while leaving the oath claim unresolved.\",\"reason\":\"The noun is semantically a time or light phenomenon but grammatically genitive under oath governance, so the CRITICAL role distinction survives.\",\"representative_source_ids\":[\"QG-ec2c70e2\",\"QT-0ff212da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"93:1:1:paired-oath-series","source_type":"word_analysis","support_id":"sup_eef6ad182837f222030c","text":"{\"blocking_evidence\":null,\"headline\":\"first oath particle prepares the second\",\"reader_payoff\":\"The reader notices that the first {{ar:وَ}} ({{tr:wa}}) starts a repeated oath pattern that the next ayah continues with night (93:2).\",\"reason\":\"The first oath particle governs the brightness noun, and the CRITICAL rows correctly relate it to the second oath opening in 93:2.\",\"representative_source_ids\":[\"QB-e2de5625\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000904","role":"Risen forenoon daylight extending through the day supplies the model's sustained temporal span.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]}],"changed_reading":{"after":"An oath by daylight already risen and still unfolding, a span in which delayed things can mature.","before":"An oath by a bright morning instant."},"confidence":"strong","focus_anchor":"The noun ضحى names the risen forenoon and its extension into the day, not undifferentiated light.","mechanism":"The oath fixes attention on an interval that has risen and continues. Duration is part of the image, so the moment can carry maturation and the arrival of what was delayed.","model_id":"b_duha_extended_ascent"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_duha_extended_ascent","source_type":"hft","support_id":"sup_8f133d10337c648071e8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000904","role":"Sun-exposure and visible prominence turn forenoon into an arena of disclosure and public standing.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]}],"changed_reading":{"after":"The forenoon is the condition in which things become exposed, prominent, and publicly legible.","before":"The forenoon is merely luminous."},"confidence":"strong","focus_anchor":"The ضحى root can image open exposure to the sun, protrusion, visibility, and public appearance.","mechanism":"Light is a field of manifestation: what had no visible standing comes out into an exposed, shared arena. The oath concerns appearance and publicity as much as luminosity.","model_id":"b_duha_public_exposure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_duha_public_exposure","source_type":"hft","support_id":"sup_2568c8300d64267c6352","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000904","role":"Forenoon eating and early grazing supply a material cycle of seeking and receiving nourishment.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]}],"changed_reading":{"after":"The named time is a daily provisioning window structured by hunger, movement, and nourishment.","before":"The named time is a neutral point on the clock."},"confidence":"medium","focus_anchor":"The ضحى inventory includes the forenoon meal and early-day grazing.","mechanism":"The time is organized by embodied need: animals go out, food is sought, and a meal is taken. The oath can therefore evoke a recurring window in which life obtains provision.","model_id":"b_duha_provisioning_window"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_duha_provisioning_window","source_type":"hft","support_id":"sup_9a27be223087b75d9b89","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000904","role":"Clear forenoon brightness supplies the mechanism by which obscured forms become distinct and readable.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]}],"changed_reading":{"after":"Duha is brightness as clarification: the world becomes distinguishable enough to read and navigate.","before":"Duha is brightness as visual intensity."},"confidence":"strong","focus_anchor":"The ضحى branch of clear, unclouded brightness makes clarity itself salient.","mechanism":"Brightness removes visual ambiguity and gives contours to what is present. The oath can foreground a condition of discernibility, not simply a quantity of light.","model_id":"b_duha_clear_legibility"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_duha_clear_legibility","source_type":"hft","support_id":"sup_15457aeff04af9b5fd88","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلضُّحَىٰ","ayah_ref":"93:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000904/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000904","role":"Gentle slowing and respite make forenoon a temporal image of non-hasty care.","root":"ض ح و","source_ref":"93:1","source_word_indices":["1"]}],"changed_reading":{"after":"The oath can carry a patient tempo: what is delayed may be handled gently rather than abandoned.","before":"The oath's time arrives automatically and says nothing about waiting."},"confidence":"exploratory","focus_anchor":"A form-distant but explicit ضحى branch carries gentleness, slowing, and not hurrying.","mechanism":"The interval itself models patient handling. Delay need not be neglect; it can be the gentle pacing by which an outcome is allowed to arrive without force.","model_id":"b_duha_gentle_delay"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_duha_gentle_delay","source_type":"hft","support_id":"sup_cb4152fbad62155754fe","trust":"legacy_unbound"}]}
</lane_packet_json>
