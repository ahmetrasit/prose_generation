# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **88:19**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_19/micro.discovery.json` and modify nothing
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
  "ayah_ref": "88:19",
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
{"branch_registry":[{"boundary":"Bu dal küçük tepecikleri, insan kuşağını ve sözcüğün öteki mecazlı kullanımlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000217/B001","candidate_links":[{"candidate_id":"cand_9a5ed1d7c0a7f63c0671","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"dağ","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Büyük ve uzun oluşuyla çevresindeki araziden yükselen doğal kara kütlesini belirtir."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Büyük ve uzun doğal kara yükseltisinin bütün çekirdeğini doğal biçimde karşılar.","boundary_detail":"Bu dal küçük tepecikleri, insan kuşağını ve sözcüğün öteki mecazlı kullanımlarını kapsamaz.","branch_image_ar":"تجمع مرتفع صلب","concept_gloss":"dağ","contextual_glosses":[{"applicability":"Dağın biçim ve ölçek özelliklerinin açıkça anlatılması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yükselti, büyüklük ve doğal kara kütlesi özelliklerini birlikte korur."},"facet_ids":["F001"],"text":"yüksek ve büyük kara kütlesi","usage_role":"explanatory"}],"definition":"Yerden belirgin biçimde yükselen, büyük ve uzun doğal kara kütlesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Büyük ve uzun oluşuyla çevresindeki araziden yükselen doğal kara kütlesini belirtir."}],"identity_rationale":"Kaynak ifadesi, yerden belirgin biçimde yükselen büyük ve uzun doğal kara kütlesini doğrudan tanımlar; geçici çerçeve bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dağ"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"dağlar"}],"lexicalization_note":"Yalın dal olarak yalnız doğal yükselti anlamı tanımlanır; öteki yapılara bağlı anlamlar buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağ adıyla özel bölüm adı arasındaki sınırı en iyi gösteren karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak genel dağ adıdır; komşu ise dağ anlamına ek olarak dağın orta kesimini belirten özel bir sınır taşır.","focus_only":"Odak dal, herhangi bir büyük ve uzun doğal dağın tamamını genel olarak adlandırır.","gloss":"dağ ve dağın orta bölümü","neighbor_only":"Komşu dal ayrıca dağın özellikle orta bölümünü adlandıran daha dar bir kullanıma sahiptir.","neighbor_ref":"root_000840/B017","relation_type":"near_synonym","shared_zone":"Her iki dal da büyük doğal kara yükseltisini adlandırma alanında buluşur."}],"source_phrase_ar":"تجمع الشيء في ارتفاع؛ الجبل معروف (maqayis)؛ اسم لكل وتد من أوتاد الأرض إذا عظم وطال (ayn;tahdhib)؛ الجبل واحد الجبال (sihah)؛ الجبل جمعه أجبال وجبال (mufradat)","source_summary":"Kaynakların ortak çekirdeği, büyük ve uzun bir doğal yükseltinin genel adıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجبل المعروف وما عظم وطال من أوتاد الأرض والأعلام والأطوار والجبال","what_is_not_ar":"ليس الآكام والقيران الصغيرة؛ وليس الجيل من الناس"},"support_links":["sup_2be521c5a9464c806ebb"]},{"boundary":"İnsan topluluğu çekirdeği ile mal ve nüfus çokluğunu bildiren yapıya bağlı kullanımlar ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B002","candidate_links":[{"candidate_id":"cand_d7cab3964f68704994d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"çok büyük topluluk ya da çok miktarda mal","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çok sayıda insandan oluşan büyük bir topluluğu veya geçmiş bir halkı belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli söz öbeklerinde malın çokluğunu veya bir topluluğun nüfusça kalabalıklığını bildirir."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan kalabalığı çekirdeğini ve yapıya bağlı mal çokluğu kullanımını birlikte temsil eder.","boundary_detail":"İnsan topluluğu çekirdeği ile mal ve nüfus çokluğunu bildiren yapıya bağlı kullanımlar ayrı tutulur.","branch_image_ar":"كثرة كالجبل","concept_gloss":"çok büyük topluluk ya da çok miktarda mal","contextual_glosses":[{"applicability":"İnsanlardan oluşan büyük ve kalabalık bir topluluğun söz konusu olduğu bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Mal çokluğunu bildiren yapıya bağlı kullanımı dışarıda bırakır.","preserves":"İnsan topluluğunun büyüklüğünü ve kalabalıklığını korur."},"facet_ids":["F001"],"text":"çok büyük kalabalık","usage_role":"contextual"},{"applicability":"Yalnız malın olağanüstü çok olduğunu bildiren söz öbeğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan topluluğu ve nüfus kalabalığı anlamlarını dışarıda bırakır.","preserves":"Malın çok büyük miktarda olması özelliğini korur."},"facet_ids":["F002"],"text":"yüklü miktarda mal","usage_role":"contextual"}],"definition":"Çok büyük ve kalabalık bir insan topluluğunu belirtir; belirli yapılarda malın ya da bir topluluğun sayıca çokluğunu da bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çok sayıda insandan oluşan büyük bir topluluğu veya geçmiş bir halkı belirtir."},{"facet_id":"F002","role":"extension","statement":"Belirli söz öbeklerinde malın çokluğunu veya bir topluluğun nüfusça kalabalıklığını bildirir."}],"identity_rationale":"Kaynak ifadesi hem çok büyük insan topluluğunu hem de belirli yapılarda kişi sayısı veya mal çokluğunu açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok büyük insan topluluğu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"büyük insan topluluğu veya geçmiş bir halk"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çok miktarda mal"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"nüfusu çok kalabalık topluluk"}],"lexicalization_note":"Yalın biçim büyük insan topluluğunu, bağlı yapılar ise çok malı veya çok kalabalık bir topluluğu bildirir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; insan kalabalığı çekirdeğine en çok yaklaşan ve kapsam farkını gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, insan kalabalığından mal çokluğuna uzanan özel kullanımlara sahiptir; komşunun sınırı ise halk kitlesi ve toplu geliş çevresindedir.","focus_only":"Odak dal geçmiş bir halkı ve belirli bir yapıda çok miktarda malı da kapsar.","gloss":"büyük insan kalabalığı","neighbor_only":"Komşu dal kalabalık halk kitlesini ve topluluğun bir kerelik gelişini ayrıca kapsar.","neighbor_ref":"root_000496/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da çok sayıda insandan oluşan büyük topluluğu belirtir."}],"source_phrase_ar":"الجبل الجماعة العظيمة الكثيرة (maqayis)؛ الخلق الجبلة وكل أمة مضت فهي جبلة (ayn)؛ الجبل من الناس الجماعة (jamhara;sihah)؛ الجبل الناس الكثير (tahdhib)؛ الجماعة العظيمة جبل (mufradat)؛ مال جبل أي كثير (jamhara;sihah;tahdhib)","source_summary":"Kaynaklar büyük insan topluluğu anlamında birleşir ve aynı benzetmeli ölçüyü mal ile nüfus çokluğuna da uygular.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجماعة العظيمة الكثيرة والخلق الكثير والأمة والمال الكثير","what_is_not_ar":"ليس الجبل الأرضي نفسه؛ وليس الجيل بمعنى الصنف من الناس"},"support_links":["sup_efb84234ab2b0b50832c"]},{"boundary":"Bu dal doğuştan huyu değil, bedenin veya nesnenin gözle görülür irilik, kalınlık ve sertlik özelliklerini anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B003","candidate_links":[{"candidate_id":"cand_0200dffa7b3c3c9746d7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"bedensel irilik ve kalınlık; kalın ve kuru olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir insanın veya hayvanın beden bakımından iri ve kalın yapılı olmasını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hörgücün büyüklüğüne, yüz derisinin kalınlığına ya da baş derisi ve kemiklerinin kalınlığına uygulanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bedenden bağımsız bir nesnenin kalın ve kuru olmasını bildiren sınırlı bir kullanımı vardır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel çekirdeği ve nesneye özgü sınırlı uzantıyı birbirine karıştırmadan birlikte gösterir.","boundary_detail":"Bu dal doğuştan huyu değil, bedenin veya nesnenin gözle görülür irilik, kalınlık ve sertlik özelliklerini anlatır.","branch_image_ar":"غلظ الخلقة والجسم","concept_gloss":"bedensel irilik ve kalınlık; kalın ve kuru olma","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın genel beden yapısının anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hörgüç ve deri ayrıntılarıyla kalın kuru nesne kullanımını dışarıda bırakır.","preserves":"Genel bedensel irilik ve kalınlık çekirdeğini korur."},"facet_ids":["F001"],"text":"iri ve kalın yapılı","usage_role":"contextual"},{"applicability":"Yalnız bedenden bağımsız bir nesnenin kalın ve kuru niteliğini anlatan kullanımda geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bedensel irilik ile özel beden bölümlerine ilişkin kullanımları dışarıda bırakır.","preserves":"Nesnenin kalın ve kuru olması özelliğini korur."},"facet_ids":["F003"],"text":"kalın ve kuru şey","usage_role":"contextual"}],"definition":"Bedenin iri, kalın veya kaba yapılı olmasını belirtir; özel kullanımlarda hörgüç, yüz ya da baş dokusunun kalınlığını ve bir nesnenin kalın-kuru oluşunu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir insanın veya hayvanın beden bakımından iri ve kalın yapılı olmasını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hörgücün büyüklüğüne, yüz derisinin kalınlığına ya da baş derisi ve kemiklerinin kalınlığına uygulanır."},{"facet_id":"F003","role":"extension","statement":"Bedenden bağımsız bir nesnenin kalın ve kuru olmasını bildiren sınırlı bir kullanımı vardır."}],"identity_rationale":"Kaynak ifadesi bedensel irilik ve kalınlığı, hörgüç ile deri ve kemik gibi özel gerçekleşmeleri ve kalın kuru nesne kullanımını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iri ve kalın yapılı kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"iri ve kalın yapılı"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iri ve kalın yapılı kadın"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"hörgüç veya yaradılıştaki bedensel irilik"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"yüz derisi ya da baş derisi ve kemikleri kalın"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kalın ve kuru şey"}],"lexicalization_note":"Bedensel irilik yalın ve bağlı biçimlerde görülür; yüz, baş, kadın ve nesne kullanımları kendi yapılarıyla sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bedensel irilik çekirdeğini paylaşırken özel uygulamalarda ayrılan en yakın aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belirli beden bölümleri ile nesne uzantısını içerir; komşu ise genişlik, sertlik ve güçlü hayvan betimlemesine uzanır.","focus_only":"Odak dal hörgücü, yüz ve baş dokularını ve ayrıca kalın kuru nesneyi kapsar.","gloss":"iri ve kalın yapılı","neighbor_only":"Komşu dal bazı insan ve deve adlandırmalarında genişlik, sertlik ve güç özelliklerini ayrıca taşır.","neighbor_ref":"root_000148/B008","relation_type":"near_synonym","shared_zone":"Her iki dal da bedenin iri veya kalın yapılı olmasını anlatır."}],"source_phrase_ar":"الناقة العظيمة السنام جبلة؛ امرأة جبلة عظيمة الخلق (maqayis)؛ رجل جبل الوجه غليظ بشرة الوجه؛ رجل جبل الرأس غليظ جلد الرأس والعظام (ayn;tahdhib)؛ ذو جبلة إذا كان غليظ الجسم (jamhara;mufradat)؛ شيء جبل غليظ جاف؛ الجبلة السنام؛ امرأة مجبال غليظة الخلق (sihah)","source_summary":"Kaynakların ortak alanı bedensel irilik ve kalınlıktır; hörgüç, deri, kemik ve kalın kuru nesne bunun özel uygulamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"غلظ الجسم والخلق والسنام والبشرة وجلدة الرأس والعظام وما كان غليظا جافا","what_is_not_ar":"ليس الفطرة والطبع الباطن؛ وليس الجبل الأرضي"},"support_links":["sup_b7f19790cde1af2162cd"]},{"boundary":"Buradaki yapı dış görünüşteki irilikten ayrıdır ve sonradan edinilen geçici davranışları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"doğuştan yapı ve ona göre biçimlenme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığın doğuştan gelen, kolayca değişmeyen temel yapısını ve huyunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir varlığı yaratmayı, ona belirli bir yapı vermeyi veya onu bir işe doğuştan yatkın kılmayı anlatır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kalıcı yaradılış özelliğini hem de bu özelliği verme eylemini kapsar.","boundary_detail":"Buradaki yapı dış görünüşteki irilikten ayrıdır ve sonradan edinilen geçici davranışları kapsamaz.","branch_image_ar":"خلقة مطبوعة","concept_gloss":"doğuştan yapı ve ona göre biçimlenme","contextual_glosses":[{"applicability":"Bir varlığın yaratılıştan gelen temel yapısı veya değişmesi güç huyu anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yaratma ve belirli bir yapıya göre biçimlendirme eylemini dışarıda bırakır.","preserves":"Doğuştan gelen ve kolay değişmeyen yapı çekirdeğini korur."},"facet_ids":["F001"],"text":"doğuştan gelen yapı","usage_role":"general"},{"applicability":"Birinin belirli bir eğilime veya davranışa yatkın kılındığı eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalın ad olarak doğuştan yapı anlamını dışarıda bırakır.","preserves":"Belirli bir yapıyı verme ve yatkın kılma eylemini korur."},"facet_ids":["F002"],"text":"belli bir huyla biçimlendirmek","usage_role":"contextual"}],"definition":"Bir varlığın yaratılıştan taşıdığı temel yapı, eğilim ve huydur; eylem olarak da onu bu yapıyla yaratmayı veya belli bir şeye yatkın kılmayı belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığın doğuştan gelen, kolayca değişmeyen temel yapısını ve huyunu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir varlığı yaratmayı, ona belirli bir yapı vermeyi veya onu bir işe doğuştan yatkın kılmayı anlatır."}],"identity_rationale":"Kaynak ifadesi bir varlığın yaratılıştan taşıdığı yapıyı ve onun belirli bir yapıya veya huya göre yaratılıp biçimlendirilmesini açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"doğuştan yapı, yaradılış ve huy"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onu yarattı ve belli bir yapıyla donattı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanı bir işe doğuştan yatkın kıldı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yaratılmış veya belli bir huyda biçimlenmiş kimseler"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"dağın yaratılıştan gelen yapısının kuruluşu"}],"lexicalization_note":"Yalın biçimler doğuştan yapıyı, bağlı eylem yapıları ise yaratma veya belli bir huya göre biçimlendirmeyi belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğuştan yapı çekirdeği en güçlü biçimde örtüşen aday, eylem kapsamı farkıyla yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ad olarak çekirdekleri büyük ölçüde örtüşür; odak dal ayrıca bu yapıyı yaratma ve verme eylemlerini açıkça içerir.","focus_only":"Odak dal yaratma, belli bir yapı verme ve bir şeye yatkın kılma eylemlerini de kapsar.","gloss":"doğuştan yapı ve huy","neighbor_only":null,"neighbor_ref":"root_000926/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın veya başka bir varlığın yaratılıştan gelen temel yapısını belirtir."}],"source_phrase_ar":"الجبلة الخليقة (maqayis)؛ جبلة كل مخلوق توسه الذي طبع عليه؛ جبل الإنسان على هذا الأمر أي طبع عليه (ayn)؛ الجبلة الفطرة؛ خليقته التي خلق عليها (jamhara)؛ جبله الله أي خلقه؛ الجبلة الخلقة (sihah)؛ الجبل الخلق جبلهم الله فهم مجبولون؛ جبل الإنسان على هذا الأمر أي طبع عليه (tahdhib)؛ جبله الله على كذا؛ الطبع الذي يأبى على الناقل نقله (mufradat)","source_summary":"Kaynaklar doğuştan gelen temel yapı ile bu yapının yaratma ve biçimlendirme yoluyla verilmesini aynı anlam alanında toplar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الجبلة والخليقة والفطرة والطبع الذي خلق عليه الإنسان أو المخلوق","what_is_not_ar":"ليس مجرد غلظ الجسم؛ وليس كثرة الجماعة"},"support_links":[]},{"boundary":"Anlam yalnız kazı sırasında sert katmana ulaşmayla ilgilidir; dağa çıkma veya sırf sert yer adı değildir.","branch_kind":"collocation","branch_ref":"root_000217/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"kazarken kazılamayan sert zemine ulaşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kazı yapan kişi veya topluluk, kazının sürdürülemediği sert bir yer, dağ veya kaya katmanına ulaşır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bağlı ad kullanımı, kazı olayı anlatmadan yerin kendi sertliğini adlandırır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kazı eylemini, sert katmana varmayı ve ilerlemenin durmasını birlikte karşılar.","boundary_detail":"Anlam yalnız kazı sırasında sert katmana ulaşmayla ilgilidir; dağa çıkma veya sırf sert yer adı değildir.","branch_image_ar":"صلابة توقف الحفر","concept_gloss":"kazarken kazılamayan sert zemine ulaşma","contextual_glosses":[{"applicability":"Kazının sert toprak veya kaya yüzünden sürdürülemediği anlatımlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazı sırasında sert engelle karşılaşmayı ve ilerleyememeyi korur."},"facet_ids":["F001","F002"],"text":"kazıda sert tabakaya dayanmak","usage_role":"contextual"}],"definition":"Bağlı kullanımlarda yerin sertliğini belirtir; kazı bağlamında ise kazı yapanların ilerlemeyi durduran, kazılamayacak kadar sert bir toprak, dağ veya kaya katmanına ulaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kazı yapan kişi veya topluluk, kazının sürdürülemediği sert bir yer, dağ veya kaya katmanına ulaşır."},{"facet_id":"F002","role":"associated_use","statement":"Bağlı ad kullanımı, kazı olayı anlatmadan yerin kendi sertliğini adlandırır."}],"identity_rationale":"Kaynak ifadesi kazı yapan kişi veya topluluğun kazılamayacak kadar sert zemine ya da kayalık katmana ulaşmasını açıkça anlatır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yerin sertliği"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kazıda kazılamayan sert yere ulaşmak"}],"lexicalization_note":"Tanım kazı ve sert zemine ulaşma yapısına bağlıdır; yalın bir sertlik veya dağ anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kazıyı durduran sert katmana ulaşma çekirdeği tam örtüşen aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek işlem, koşul ve sonuç bakımından anlamlı bir sınır farkı yoktur; iki dal bu kullanımda birbirinin yerine geçebilir.","focus_only":null,"gloss":"kazıyı durduran sert zemin","neighbor_only":null,"neighbor_ref":"root_001289/B001","relation_type":"synonym","shared_zone":"Her iki dal da kazı sırasında ilerlemeyi durduran sert toprak veya kaya katmanına ulaşmayı belirtir."}],"source_phrase_ar":"حفر القوم فأجبلوا إذا بلغوا مكانا صلبا (maqayis)؛ جبلة الأرض صلابها (ayn)؛ أجبل الحافر إذا أفضى إلى جبل لا يمكنه الحفر فيه (jamhara)؛ أجبل القوم إذا حفروا فبلغوا المكان الصلب (sihah)","source_summary":"Kaynakların ortak anlatımı, kazının sert bir yere varması ve bu sertliğin kazmayı artık olanaksız kılmasıdır.","sources":["MQ","AY","JA","SI","TA"],"what_is_ar":"بلوغ الحافر أو القوم أرضا صلبة أو جبلا لا يمكن الحفر فيه","what_is_not_ar":"ليس مجرد الصعود إلى الجبل؛ وليس الجبل اسما للمكان فقط"},"support_links":[]},{"boundary":"Bu dal kazının sert zeminde durmasını veya kumdan bir yükseltiye rastlamayı değil, dağlık alana hareketi bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"dağlara varma veya girme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun dağa yönelerek dağlık alana varmasını belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı eylem biçiminde hareketin sonucu dağların içine girmek olarak anlatılır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dağlık alana yönelme, varma ve içeri girme görünümlerini birlikte karşılar.","boundary_detail":"Bu dal kazının sert zeminde durmasını veya kumdan bir yükseltiye rastlamayı değil, dağlık alana hareketi bildirir.","branch_image_ar":"دخول الجبال","concept_gloss":"dağlara varma veya girme","contextual_glosses":[{"applicability":"Bir topluluğun hareket sonunda dağlık bir alana ulaştığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dağların içine girme görünümünü açıkça belirtmez.","preserves":"Dağa doğru hareketin varış sonucunu korur."},"facet_ids":["F001"],"text":"dağlık bölgeye varmak","usage_role":"contextual"},{"applicability":"Hareketin dağlık alanın içine giriş olarak anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnız dağa yönelip varma görünümünü dışarıda bırakır.","preserves":"Dağlık alanın içine girme sonucunu korur."},"facet_ids":["F002"],"text":"dağların içine girmek","usage_role":"contextual"}],"definition":"Bir topluluğun dağa veya dağlık bölgeye yönelip oraya varması ya da dağların içine girmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun dağa yönelerek dağlık alana varmasını belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı eylem biçiminde hareketin sonucu dağların içine girmek olarak anlatılır."}],"identity_rationale":"Kaynak ifadesi bir topluluğun dağa yönelmesini, dağlık alana varmasını veya dağların içine girmesini açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"topluluk dağa veya dağlara vardı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"dağların içine girdiler"}],"lexicalization_note":"Toplulukla kurulan yapı dağa varmayı, ayrı eylem biçimi ise dağların içine girmeyi belirtir; ikisi ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hareket ve varış ortaklığını gösterip dağlık hedef sınırını belirginleştiren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yalnız dağlık alana yönelme ve giriştir; komşu ise hedef türünü sınırlamayan göç ve yerleşme hareketlerini anlatır.","focus_only":"Odak dal hareketin hedefini özellikle dağ veya dağlık alan olarak sınırlar.","gloss":"bir yere varma ve yerleşme","neighbor_only":"Komşu dal ülkeden ülkeye göçü, kentte kalmayı veya bir eve yerleşmeyi de kapsar.","neighbor_ref":"root_000139/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir topluluğun veya kişinin başka bir yere hareket edip orada bulunmasını içerir."}],"source_phrase_ar":"أجبل القوم أي صاروا في الجبال وتجبلوا أي دخلوها (ayn;tahdhib)؛ أجبل القوم أي صاروا إلى الجبل (sihah)","source_summary":"Kaynaklar dağa doğru hareket ve dağlık alana giriş çekirdeğinde birleşir; varış ile içeri giriş aynı hareketin yakın görünümleridir.","sources":["AY","SI","TA"],"what_is_ar":"مصير القوم إلى الجبل أو في الجبال ودخولها","what_is_not_ar":"ليس الحفر حتى يبلغ الصلب؛ وليس مصادفة جبل من الرمل"},"support_links":[]},{"boundary":"Anlam kumaşın yapım niteliğiyle sınırlıdır; insan yaradılışını veya genel bedensel kalınlığı anlatmaz.","branch_kind":"collocation","branch_ref":"root_000217/B007","candidate_links":[{"candidate_id":"cand_6bddffd02279b87a580a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"dokuması, ipliği ve bükümü iyi kumaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kumaşın dokuma, iplik eğirme ve büküm işlerinin birlikte iyi ve sağlam olmasını belirtir."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kumaşın üç yapım unsurundaki iyi işçiliği birlikte ve yapıya bağlı biçimde karşılar.","boundary_detail":"Anlam kumaşın yapım niteliğiyle sınırlıdır; insan yaradılışını veya genel bedensel kalınlığı anlatmaz.","branch_image_ar":"إحكام النسج","concept_gloss":"dokuması, ipliği ve bükümü iyi kumaş","contextual_glosses":[{"applicability":"Dokuma niteliği iplik ve büküm işçiliğini de içine alacak biçimde anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kumaşın bütün yapımında iyi ve sağlam işçiliği korur."},"facet_ids":["F001"],"text":"iyi ve sağlam dokunmuş kumaş","usage_role":"explanatory"}],"definition":"Bir kumaşın dokumasının, ipliğinin ve iplik bükümünün sağlam ve iyi yapılmış olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kumaşın dokuma, iplik eğirme ve büküm işlerinin birlikte iyi ve sağlam olmasını belirtir."}],"identity_rationale":"Kaynak ifadesi bir kumaşın dokuma, iplik ve büküm bakımından iyi yapılmış olmasını açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"dokuması, ipliği ve bükümü iyi kumaş"}],"lexicalization_note":"Tanım yalnız kumaşın iyi dokunmuş, eğrilmiş ve bükülmüş olduğunu bildiren sabit yapıya bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kumaş dokumasındaki sağlamlığı paylaşırken kapsamı daha geniş olan en yakın aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kumaşın iplik ve büküm işçiliğini de kurucu sayar; komşu daha genel sağlamlık ve düzgün konuşma alanlarına uzanır.","focus_only":"Odak dal kumaşın dokumasıyla birlikte ipliğinin ve bükümünün iyi oluşunu şart koşar.","gloss":"sağlam ve iyi dokunmuş kumaş","neighbor_only":"Komşu dal sağlamlığı konuşma ve genel bir işi doğrulama alanına da genişletir.","neighbor_ref":"root_000347/B010","relation_type":"near_synonym","shared_zone":"Her iki dal da kumaşın sıkı, sağlam ve iyi dokunmuş olmasını anlatır."}],"source_phrase_ar":"الثوب الجيد النسج والغزل والفتل جيد الجبلة (ayn;tahdhib)؛ ثوب جيد الجبلة (mufradat)","source_summary":"Kaynaklar kumaşın dokuması, ipliği ve bükümünün iyi oluşunu tek bir yapım niteliği olarak verir.","sources":["AY","TA","MU"],"what_is_ar":"جودة نسج الثوب وغزله وفتله وجودة جبلته","what_is_not_ar":"ليس خلقة الإنسان؛ وليس غلظ الجسم"},"support_links":["sup_1d2bde21ee5faa7dff30"]},{"boundary":"Bu dal bütün kuru bitkileri veya herhangi bir kalın nesneyi değil, özellikle kurumuş ağacı belirtir.","branch_kind":"bare","branch_ref":"root_000217/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"kurumuş ağaç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuruma durumuna gelmiş ağacı toplu veya türsel olarak belirtir."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağaç olma ve kurumuşluk özelliklerini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Bu dal bütün kuru bitkileri veya herhangi bir kalın nesneyi değil, özellikle kurumuş ağacı belirtir.","branch_image_ar":"يبس الشجر","concept_gloss":"kurumuş ağaç","contextual_glosses":[{"applicability":"Toplu veya çoğul bir ağaç kümesinin kurumuş olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağaçların kurumuş olma niteliğini ve toplu okumayı korur."},"facet_ids":["F001"],"text":"kuru ağaçlar","usage_role":"contextual"}],"definition":"Kuruyup canlılığını ve yaşlığını yitirmiş ağaç veya ağaçlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuruma durumuna gelmiş ağacı toplu veya türsel olarak belirtir."}],"identity_rationale":"Kaynak ifadesi yalın biçimi doğrudan kurumuş ağaç veya ağaçlar olarak tanımlar ve geçici çerçeveyle bütünüyle uyuşur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kurumuş ağaç veya ağaçlar"}],"lexicalization_note":"Yalın dal yalnız kurumuş ağaç anlamında tanımlanır; başka bitki türleri veya bağlı kullanımlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuru ağaç çekirdeğine en yakın olup dökülme ve neden bakımından genişleyen aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kuru ağacın genel adıdır; komşu dökülme durumunu ve kurumanın sıcak ya da soğuk nedenini ayrıca içerebilir.","focus_only":"Odak dal kurumuş ağacı durumun nedeni veya parçalanma aşaması belirtilmeden adlandırır.","gloss":"kurumuş veya dökülmüş ağaç","neighbor_only":"Komşu dal ağaçtan dökülen parçaları ve sıcak ya da soğuk yüzünden kuruyan ağacı da kapsar.","neighbor_ref":"root_000734/B014","relation_type":"near_synonym","shared_zone":"Her iki dal da kuruyup canlılığını yitiren ağaç malzemesini belirtir."}],"source_phrase_ar":"الجبل الشجر اليابس (ayn;tahdhib)","source_summary":"Kaynakların ortak ve sınırlı tanımı, canlılığını yitirmiş kuru ağaçtır.","sources":["AY","TA"],"what_is_ar":"الشجر اليابس","what_is_not_ar":"ليس الجبل الأرضي؛ وليس الغلظ العام"},"support_links":[]},{"boundary":"Dal genel güçlük veya genel zorlama anlamına genişletilmemeli; iki tanıklı kullanım ayrı ayrı korunmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"sözün tıkanması veya engelleme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ozanın söz söylemesinin güçleşmesini ve anlatımın tıkanmasını belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir ad biçimi, kaynakta kısa biçimde engelleme veya alıkonma alanına bağlanır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki tanıklı kullanımı ortak bir tıkanma düşüncesi altında, kapsamlarını genellemeden temsil eder.","boundary_detail":"Dal genel güçlük veya genel zorlama anlamına genişletilmemeli; iki tanıklı kullanım ayrı ayrı korunmalıdır.","branch_image_ar":"عسر ومنع","concept_gloss":"sözün tıkanması veya engelleme","contextual_glosses":[{"applicability":"Yalnız ozanın söyleyiş sırasında zorlanıp sözünün tıkandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Engelleme veya alıkonma alanındaki ayrı ad kullanımını dışarıda bırakır.","preserves":"Ozana özgü söz söyleme güçlüğünü korur."},"facet_ids":["F001"],"text":"ozanın söz bulamaması","usage_role":"contextual"},{"applicability":"Kaynakta engelleme alanına bağlanan kısa ve belirsiz ad kullanımını temkinli biçimde açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ozanın söz söylemekte zorlanması kullanımını dışarıda bırakır.","preserves":"Engelleme alanındaki ad kullanımını korur."},"facet_ids":["F002"],"text":"engelleme veya alıkonma","usage_role":"explanatory"}],"definition":"İki sınırlı kullanımı vardır: ozanın söz bulup söylemekte tıkanması ve ayrı bir ad biçiminde engelleme ya da alıkonma durumu.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ozanın söz söylemesinin güçleşmesini ve anlatımın tıkanmasını belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir ad biçimi, kaynakta kısa biçimde engelleme veya alıkonma alanına bağlanır."}],"identity_rationale":"Kaynak ifadesi biri ozanın söz söylemekte zorlanması, diğeri engelleme alanındaki bir ad olmak üzere iki sınırlı kullanım verir; bunlar ancak tıkanma üst başlığı altında birlikte tutulabilir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ozanın söz söylemekte zorlanması"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"engelleme veya alıkonma alanındaki şey"}],"lexicalization_note":"Ozanla kurulan yapı sözün zorlaşmasını, ayrı ad biçimi ise engelleme veya alıkonma alanını bildirir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nitelikli dalın söz güçlüğü yönünü aydınlatan genel güçlük adayı, kapsam farkı belirtilerek seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak iki özel dilsel kullanımla sınırlıdır; komşu ise konusu belirtilmemiş iş ve durumlara uygulanan genel güçlüğü anlatır.","focus_only":"Odak dal güçlüğü özellikle ozanın söz söylemesine bağlar ve ayrıca engelleme alanında ayrı bir ad kullanımı taşır.","gloss":"bir işin zorlaşması","neighbor_only":"Komşu dal herhangi bir işin yürümemesi, zorlaşması veya olanaksızlaşması gibi genel durumları kapsar.","neighbor_ref":"root_000995/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir eylemin güçleşmesi veya yürütülememesi düşüncesi vardır."}],"source_phrase_ar":"أجبل الشاعر إذا صعب عليه القول (jamhara)؛ المجبل في المنع (tahdhib)","source_summary":"Kaynak ifadesi genel bir anlam vermek yerine sözün zorlaşması ile engelleme alanındaki iki ayrı ve dar kullanımı yan yana getirir.","sources":["TA","JA"],"what_is_ar":"إجبل الشاعر إذا صعب عليه القول والمجبل في المنع","what_is_not_ar":"ليس الصلابة التي توقف الحفر؛ وليس الإجبار على أمر"},"support_links":[]},{"boundary":"Anlam yalnız kişiyi bir işe zorlama yapısına bağlıdır; doğuştan biçimlendirme veya salt engelleme değildir.","branch_kind":"collocation","branch_ref":"root_000217/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"birini bir işi yapmaya zorlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Etkileyen kişi, başka birini belli bir işi yapmaya iradesi dışında zorlar."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zorlayan kişi, etkilenen kişi ve dayatılan iş arasındaki ilişkiyi eksiksiz karşılar.","boundary_detail":"Anlam yalnız kişiyi bir işe zorlama yapısına bağlıdır; doğuştan biçimlendirme veya salt engelleme değildir.","branch_image_ar":"حمل على أمر","concept_gloss":"birini bir işi yapmaya zorlamak","contextual_glosses":[{"applicability":"Bir kişinin istemediği bir işi yapmaya zorlandığı anlatımlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İrade dışı yaptırma ve belirli işe yöneltme özelliklerini korur."},"facet_ids":["F001"],"text":"birini bir şeye mecbur bırakmak","usage_role":"contextual"}],"definition":"Bir kişiyi belirli bir işi yapmaya kendi isteği dışında zorlamak veya mecbur bırakmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Etkileyen kişi, başka birini belli bir işi yapmaya iradesi dışında zorlar."}],"identity_rationale":"Kaynak ifadesi bir kişiyi belirli bir işi yapmaya kendi isteği dışında zorlamayı açık ve tek anlamlı biçimde bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"birini belirli bir işi yapmaya zorlamak"}],"lexicalization_note":"Tanım kişi ve zorlandığı işi birlikte belirten yapıya bağlıdır; yalın biçime veya genel güç anlamına taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; zorla yaptırma çekirdeğini paylaşan, fakat daha geniş kapsamlı olan en yakın aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak tek bir kişi-iş yapısındaki zorlamadır; komşu daha geniş baskı, egemenlik ve düşünce alanlarına yayılır.","focus_only":"Odak dal belirli bir kişiyi belirli bir işi yapmaya zorlama yapısıyla sınırlıdır.","gloss":"zorlama ve baskıyla yaptırma","neighbor_only":"Komşu dal baskı, egemenlik, haksız savaş ve insan iradesine ilişkin öğretisel kullanımlara da uzanır.","neighbor_ref":"root_000216/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir insanın iradesini baskı altına alıp ona bir şey yaptırmayı belirtir."}],"source_phrase_ar":"اجتبلت فلانا على أمر وجبلته أي أجبرته (tahdhib)","source_summary":"Tek tanıklık, bir kişiyi belirli bir işi yapmaya zorlama eylemini açıkça verir.","sources":["TA"],"what_is_ar":"جبل فلانا أو اجتبله على أمر بمعنى أجبره","what_is_not_ar":"ليس الطبع الذي خلق عليه الإنسان؛ وليس المنع المجرد"},"support_links":[]},{"boundary":"Bu dal genel olarak dağa girmeyi veya her kum sırtını değil, geniş ve uzun kum yükseltisine rastlama olayını belirtir.","branch_kind":"bare","branch_ref":"root_000217/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"geniş ve uzun kum sırtına rastlamak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket eden kişi genişliği ve uzunluğu belirgin bir kum yükseltisiyle karşılaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaşılan kum biçimi, ince uzun kum sırtından özellikle geniş olmasıyla ayrılır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşılaşma eylemini ve kum yükseltisinin genişlik ile uzunluk koşullarını birlikte korur.","boundary_detail":"Bu dal genel olarak dağa girmeyi veya her kum sırtını değil, geniş ve uzun kum yükseltisine rastlama olayını belirtir.","branch_image_ar":"مصادفة رمل عريض","concept_gloss":"geniş ve uzun kum sırtına rastlamak","contextual_glosses":[{"applicability":"Yol üzerinde geniş ve uzanan bir kum kütlesine rastlama anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılaşmayı, kum oluşumunu ve ayırt edici genişliği korur."},"facet_ids":["F001","F002"],"text":"geniş bir kum yükseltisiyle karşılaşmak","usage_role":"contextual"}],"definition":"Yol alırken geniş ve uzun bir kum sırtına veya kum yükseltisine rastlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket eden kişi genişliği ve uzunluğu belirgin bir kum yükseltisiyle karşılaşır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaşılan kum biçimi, ince uzun kum sırtından özellikle geniş olmasıyla ayrılır."}],"identity_rationale":"Kaynak ifadesi eylemi, geniş ve uzun bir kum yükseltisine rastlamak olarak tanımlar ve onu ince uzun kum sırtından açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"geniş ve uzun bir kum sırtına rastlamak"}],"lexicalization_note":"Yalın dal, verilen eylem biçiminin geniş ve uzun kum yükseltisine rastlama anlamıyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kum sırtının biçimini paylaşırken olay ile nesne sınırını en açık gösteren aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak geniş kum sırtıyla karşılaşma eylemidir; komşu ise kum sırtının kendisini ve biçim özelliklerini adlandırır.","focus_only":"Odak dal kum sırtının geniş olmasını ve bir yolcunun ona rastlaması olayını birlikte içerir.","gloss":"uzun kum sırtı","neighbor_only":"Komşu dal kum sırtının varlığını, uzunluğunu, yüksekliğini ve çok kumlu oluşunu olaydan bağımsız adlandırır.","neighbor_ref":"root_000291/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da uzunlamasına uzanan belirgin bir kum sırtını konu edinir."}],"source_phrase_ar":"أجبل إذا صادف جبلا من الرمل وهو العريض الطويل؛ أحبل إذا صادف حبلا من الرمل وهو الدقيق الطويل (tahdhib)","source_summary":"Tek tanıklık, geniş ve uzun kum yükseltisine rastlama eylemini verir ve ince uzun kum sırtıyla karşıtlığını açıklar.","sources":["TA"],"what_is_ar":"أجبل إذا صادف جبلا من الرمل العريض الطويل","what_is_not_ar":"ليس حبل الرمل الدقيق الطويل؛ وليس دخول الجبال"},"support_links":[]},{"boundary":"Bu dal kalabalık halkı veya doğal dağları değil, topluluk içinde öne çıkan önder ve bilgin kişileri belirtir.","branch_kind":"mixed_non_bare","branch_ref":"root_000217/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","surface_ar":"جِبَالِ"}],"gloss":"topluluğun önderi veya bilgini; ileri gelenler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluk içinde önderlik ve bilgi bakımından öne çıkan kişiyi belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir çoğul yapıda topluluğun önderlerini ve ileri gelenlerini birlikte adlandırır."}}],"root_ar":"ج ب ل","root_id":"root_000217","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tekil önder ve bilgin anlamıyla çoğul yapıdaki ileri gelenler kullanımını birlikte gösterir.","boundary_detail":"Bu dal kalabalık halkı veya doğal dağları değil, topluluk içinde öne çıkan önder ve bilgin kişileri belirtir.","branch_image_ar":"سادات كالجِبال","concept_gloss":"topluluğun önderi veya bilgini; ileri gelenler","contextual_glosses":[{"applicability":"Tek bir kişinin hem önderlik hem bilgi bakımından toplulukta öne çıktığı bağlama uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çoğul yapıdaki toplu ileri gelenler kullanımını dışarıda bırakır.","preserves":"Tekil kişinin önderlik ve bilginlik özelliklerini korur."},"facet_ids":["F001"],"text":"topluluğun önderi ve bilgini","usage_role":"contextual"},{"applicability":"Belirli bir topluluğun önderlerinin çoğul olarak anıldığı yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir bilgin ve önder kişiyi adlandıran kullanımı dışarıda bırakır.","preserves":"Topluluğa bağlı çoğul önderler ve ileri gelenler anlamını korur."},"facet_ids":["F002"],"text":"bir topluluğun ileri gelenleri","usage_role":"contextual"}],"definition":"Bir topluluğun önderi ve bilgini olan seçkin kişiyi belirtir; çoğul yapıda o topluluğun ileri gelenlerini topluca adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluk içinde önderlik ve bilgi bakımından öne çıkan kişiyi belirtir."},{"facet_id":"F002","role":"extension","statement":"Belirli bir çoğul yapıda topluluğun önderlerini ve ileri gelenlerini birlikte adlandırır."}],"identity_rationale":"Kaynak ifadesi tekilde topluluğun önderi ve bilgini, çoğul yapıda ise topluluğun ileri gelenleri anlamını doğrudan verir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"topluluğun önderi ve bilgini"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir topluluğun önderleri ve ileri gelenleri"}],"lexicalization_note":"Yalın biçim tek bir önder veya bilgini, bağlı çoğul yapı ise belirli bir topluluğun ileri gelenlerini bildirir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; önder ve ileri gelen alanını paylaşırken bilginlik ile saygınlık sınırını gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak önderlik ile bilginliği birleştiren özel bir adlandırmadır; komşu daha genel saygınlık ve toplumsal konum alanındadır.","focus_only":"Odak dal topluluğun önderini bilginlik özelliğiyle birlikte adlandırır ve özel bir çoğul yapı taşır.","gloss":"önder, seçkin ve ileri gelen","neighbor_only":"Komşu dal kişisel saygınlık, toplumsal konum ve bir yerin bütün ileri gelenlerini daha geniş biçimde kapsar.","neighbor_ref":"root_001630/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da toplum içinde yüksek konuma sahip önder veya ileri gelen kişileri belirtir."}],"source_phrase_ar":"الجبل سيد القوم وعالمهم؛ هؤلاء جبال بني فلان؛ أي سادتهم (tahdhib)","source_summary":"Tek tanıklık, önder ve bilgin kişiyi tekil olarak; bir topluluğun ileri gelenlerini ise çoğul yapı içinde verir.","sources":["TA"],"what_is_ar":"سادة القوم وعلماؤهم الذين يقال لهم جبال بني فلان","what_is_not_ar":"ليس جماعة الناس الكثيرة؛ وليس الجبال التي تسكنها الجن"},"support_links":[]},{"boundary":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_9a5ed1d7c0a7f63c0671","lane":"micro"},{"candidate_id":"cand_0200dffa7b3c3c9746d7","lane":"micro"},{"candidate_id":"cand_6bddffd02279b87a580a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"dikme, dik durma ve yükselme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel bir nesnenin dik konuma getirilmesini veya bir varlığın dik ve yükselmiş durumda bulunmasını birlikte anlatır.","boundary_detail":"Bu dal yalnızca fiziksel dikme, dik durma ve yükselme alanındadır; tapınma taşı, pay, yorgunluk ve öteki dalların özel anlamlarını içermez.","branch_image_ar":"إقامة الشيء منتصبا بارزا","concept_gloss":"dikme, dik durma ve yükselme","contextual_glosses":[{"applicability":"Mızrak, taş, direk, yapı veya benzeri bir nesne dik konuma getirildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi dik ve belirgin konuma getiren fiziksel işlemi tam olarak korur."},"facet_ids":["F001"],"text":"dikmek","usage_role":"contextual"},{"applicability":"Bir insanın, hayvanın ya da beden bölümünün yükselmiş ve dik durumda bulunmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlı veya beden bölümü için dik ve yükselmiş durumu eksiksiz korur."},"facet_ids":["F002"],"text":"dik durmak","usage_role":"contextual"},{"applicability":"Tozun yerden kalkıp havada belirginleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun yukarı doğru hareket edip görünür hâle gelmesini korur."},"facet_ids":["F003"],"text":"havaya yükselmek","usage_role":"contextual"}],"definition":"Bir şeyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirmek ya da yükseltmek; ayrıca bir varlığın veya bölümünün bu biçimde dik durmasıdır. Tozun yükselmesi ve belirli nesnelerin kurulması bu uzamsal çekirdeğin bağlama bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi dik, çıkıntılı veya belirgin duracak biçimde yerleştirme ya da yükseltme."},{"facet_id":"F002","role":"core","statement":"Bir insanın, hayvanın, boynuzun veya göğsün dik ve yükselmiş durumda bulunması."},{"facet_id":"F003","role":"extension","statement":"Toz gibi dağınık bir maddenin havaya yükselerek belirginleşmesi."},{"facet_id":"F004","role":"associated_use","statement":"Perdeyi kaldırma, av için tuzak kurma veya kazanı taşıyacak demir desteği yerleştirme gibi nesneye bağlı uygulamalar."}],"identity_rationale":"Dalın kimliği, bir şeyi dik ve belirgin duracak biçimde yerleştirme veya yükseltme çekirdeğini doğru yansıtır. Boynuz, göğüs ve baş gibi bölümlerin dik durması ile tozun yükselmesi aynı uzamsal görünümün geçişsiz gerçekleşmeleridir; perde kaldırma ve tuzak kurma ise belirli nesnelerle sınırlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi dikmek veya dik konuma kaldırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"boynuzları dik olan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"boynuzu dik veya göğsü yüksek dişi hayvan"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"havaya yükselmiş toz"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"perdeyi kaldırmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kuş avlamak için tuzak kurmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kazanın üzerine konduğu demir destek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dikili direk veya sütun"}],"lexicalization_note":"Tanım, yalın dikme ve dik durma çekirdeğini özel nesnelerle kurulan perde kaldırma, tuzak kurma ve kazan desteği gibi kullanımlardan açıkça ayırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; çoğu yalnızca diklik senaryosunu paylaşan nesne, özel kullanım veya diğer kök anlamıdır. Okur açısından en yakın sınır karışıklığını dikilme ve sabit kalma adayı verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın merkezi yerleştirme ve yükseltmedir; komşu dalın merkezi ise dik duruşla birlikte sabitlik ve bir yere bağlı kalmadır.","focus_only":"Odak dal, bir nesneyi dik konuma getiren geçişli işlemi ve toz gibi şeylerin yükselmesini de kapsar.","gloss":"dikilme ve sabit kalma","neighbor_only":"Komşu dal, yerde veya bir şey üzerinde sabit kalma, bağlanma ve sıkıca yapışma anlamlarını da taşır.","neighbor_ref":"root_000232/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın dik veya yükselmiş durumda bulunmasını anlatabilir."}],"source_phrase_ar":"أصل صحيح يدل على إقامة شيء وإهداف في استواء (maqayis)؛ النصب رفعك شيئا تنصبه قائما منتصبا (ayn;tahdhib)؛ نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر (mufradat)؛ نصبت الشئ إذا أقمته (sihah)؛ كل شيء رفعته فقد نصبته (jamhara)؛ تيس أنصب وعنزة نصباء وناقة نصباء وغبار منتصب (maqayis;ayn;sihah;tahdhib;mufradat)؛ نصبت للقطاة شركا ونصبت للقدر نصبا (tahdhib)؛ نصب الستر رفعه (mufradat)","source_summary":"Anlamın ortak çekirdeği, bir şeyi dik ve görünür konuma getirme ile bu konumda bulunmadır. Nesne örnekleri mızrak, yapı, taş, perde ve tuzağı; durum örnekleri ise dik boynuz, yükselmiş göğüs ve havaya kalkmış tozu kapsar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصب الشيء وإقامته ورفعه قائما، كنصب الرمح والبناء والحجر والستر والشرك، وقيام الشخص أو الحيوان منتصب الرأس أو القرن أو الصدر، وارتفاع الغبار ونحوه","what_is_not_ar":"لا يختص بالعبادة ولا بالحظ ولا بالتعب إلا إذا صرحت العبارة بذلك"},"support_links":["sup_1d2bde21ee5faa7dff30","sup_2be521c5a9464c806ebb","sup_b7f19790cde1af2162cd"]},{"boundary":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_kind":"bare","branch_ref":"root_001507/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"tapınma veya adak kesme taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinsel amaçla dikilmiş, tapınılan ya da üzerinde adak hayvanı kesilen taş için kullanılır.","boundary_detail":"Sıradan sınır taşı, kuyu çevresi taşı veya başka bir dikili nesne bu dala ancak tapınma ya da adak kesme işlevi varsa girer.","branch_image_ar":"حجر منصوب للعبادة والذبح","concept_gloss":"tapınma veya adak kesme taşı","contextual_glosses":[{"applicability":"Taşın doğrudan kutsal nesne sayılıp kendisine tapınıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın doğrudan tapınma nesnesi olmasını tam olarak korur."},"facet_ids":["F001"],"text":"tapınılan dikili taş","usage_role":"contextual"},{"applicability":"Hayvanın taş üzerinde kesildiği veya kanının taş üzerine döküldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın kesim ve kan dökme törenindeki özel işlevini korur."},"facet_ids":["F002"],"text":"adak kesme taşı","usage_role":"contextual"}],"definition":"Tapınmak, çevresinde dönmek, yakınlık sunmak veya üzerinde adak kesip kan dökmek için dikilmiş taş ya da bu tür taşlardan oluşan kutsal nesnedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tapınılmak veya çevresinde dinsel tören yapılmak üzere dikilmiş taş."},{"facet_id":"F002","role":"core","statement":"Üzerinde adak hayvanı kesilen veya kan dökülen dikili taş."}],"identity_rationale":"Dal, dikilmiş taşın tapınma, çevresinde dönme, adak kesme veya kan dökme amacıyla kullanılan kutsal nesne oluşunu doğru biçimde birleştirir. Taşın yalnızca dikili olması yeterli değildir; dinsel yönelim ya da kesim işlevi anlamın ayırt edici koşuludur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"tapınılan veya üzerinde adak kesilen dikili taş"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"tapınılan ya da adak kesilen dikili taşlar"}],"lexicalization_note":"Tanım yalın taş adını dinsel işleviyle verir ve başka dallardaki sıradan dikili taş anlamlarını bu çekirdeğe katmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; kesme, adak, çevresinde dönme ve belirli put adları senaryonun ayrı parçalarıdır. En yararlı karşılaştırma, dikili tören taşı ile genel tapınma nesnesi arasındaki sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikili taş ve onun kesim törenindeki kullanımıyla sınırlıdır; komşu dal ise tapınılan nesnenin biçimini veya tören işlevini böyle sınırlamaz.","focus_only":"Odak dal, taşın dikili olmasını ve üzerinde kesim yapılıp kan dökülmesi işlevini özellikle içerir.","gloss":"tapınma nesnesi","neighbor_only":"Komşu dal, taşla sınırlı olmayan tapınma nesnelerini ve putları daha genel biçimde kapsar.","neighbor_ref":"root_001624/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların tapındığı cansız ve kutsallaştırılmış bir nesneyi kapsayabilir."}],"source_phrase_ar":"النصب حجر كان ينصب فيعبد وتصب عليه دماء الذبائح للأصنام (maqayis)؛ حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب (ayn)؛ حجارة كانت تنصب في الجاهلية ويطاف بها ويتقرب عندها (jamhara)؛ ما نصب فعبد من دون الله والجمع الأنصاب (sihah)؛ النصب الآلهة التي كانت تعبد من أحجار (tahdhib)؛ حجارة تعبدها وتذبح عليها (mufradat)","source_summary":"Ortak anlatım, taşın dikilmiş olmasını tapınma ve kesim törenleriyle birlikte verir. Taş hem tapınılan bir nesne hem de adak hayvanının kesildiği ve kanının döküldüğü tören odağı olabilir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب والأنصاب: حجارة منصوبة كانت تعبد أو يذبح عليها أو تصب عليها دماء الذبائح","what_is_not_ar":"لا يدخل مطلق العلامة أو حجارة الحوض إذا لم تكن عبادة أو ذبحا"},"support_links":[]},{"boundary":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001507/B003","candidate_links":[{"candidate_id":"cand_9a5ed1d7c0a7f63c0671","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"sınır işareti veya kuyu-havuz taşı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yeri belirleyen dikili işaretlerle kuyu ya da havuz çevresine yerleştirilen taşları kapsar.","boundary_detail":"Ayırt edici özellik, taşın işaret, sınır veya su yapısının kenar elemanı olmasıdır; dinsel kullanım ve pay anlamı dışarıda kalır.","branch_image_ar":"علامة أو حجارة منصوبة للحد أو الحوض","concept_gloss":"sınır işareti veya kuyu-havuz taşı","contextual_glosses":[{"applicability":"Bir topluluğun yerini veya kutsal sayılan bir bölgenin sınırını belirtme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikili taşın yer veya sınır bildiren işaret işlevini korur."},"facet_ids":["F001"],"text":"dikili sınır taşı","usage_role":"contextual"},{"applicability":"Kuyu veya havuz ağzının çevresine yerleştirilen taşlardan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın su yapısının çevresini ve kenarını oluşturma işlevini korur."},"facet_ids":["F002"],"text":"kuyu ya da havuz kenarı taşı","usage_role":"contextual"}],"definition":"Bir topluluğu veya sınırı göstermek için dikilen işaret ya da kuyu ve havuz kenarına destek veya çevre oluşturacak biçimde yerleştirilen taştır. Taşlardan kurulmuş havuzun kendisi de bu düzenlemeden doğan adlaşmış bir anlamdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yerini veya bir bölgenin sınırını bildirmek üzere dikilmiş işaret taşı."},{"facet_id":"F002","role":"specialization","statement":"Kuyu ya da havuz ağzının çevresine kenar ve destek oluşturacak biçimde yerleştirilen taş."},{"facet_id":"F003","role":"extension","statement":"Çevresi taşlarla kurulmuş havuzun kendisi."}],"identity_rationale":"Dal, bir topluluğu ya da sınırı gösteren dikili işaret ile kuyu veya havuz kenarına yerleştirilen taşları kaynak ifadesine uygun biçimde kapsar. Taşlardan yapılmış havuz adı bu yerleştirme düzeninden doğan adlaşmış bir uzantıdır; tapınma işlevi bu dalın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dikili işaret veya havuz kenarı taşı"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kuyu ya da havuz ağzının çevresine dizilen taşlar"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"taşlardan kurulmuş havuz"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluk veya sınır için dikilmiş işaret"}],"lexicalization_note":"Tanım, yalın adların işaret ve su yapısı anlamlarını kapsar; başka bir yapıya özgü deyimsel anlam eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınır, kıyı ve uç anlamları işaret edilen çizgiye, su yapısı adayları ise yapının kenarına odaklanır. En yakın karışıklık, dikili kenar taşları ile kenarın genel adı arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kenarı oluşturan dikili taşlara dayanır; komşu dal ise kenarın kendisini malzemesinden ve kurulma biçiminden bağımsız olarak belirtir.","focus_only":"Odak dal, kuyu ve havuz çevresindeki belirli taşları ayrıca bağımsız sınır ve topluluk işaretlerini kapsar.","gloss":"kuyu veya havuz kenarı","neighbor_only":"Komşu dal, taş olma veya dikilme koşulu aramadan kuyu ve havuzun yanlarını genel olarak adlandırır.","neighbor_ref":"root_001370/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da kuyu ve havuz ağzının çevresindeki kenar yapısını gösterebilir."}],"source_phrase_ar":"النصائب حجارة تنصب حوالي شفير البئر فتجعل عضائد (maqayis)؛ النصيب الحوض ينصب من الحجارة (maqayis)؛ النصب العلم؛ النصيبة علامة تنصب للقوم؛ نصائب الحوض (ayn)؛ أنصاب الحرم حجارة تنصب لتعرف حدوده بها (jamhara)؛ النصيبة حجارة تنصب حول الحوض؛ النصيب الحوض (sihah)؛ النصائب ما نصب حول الحوض من الأحجار؛ النصب جماعة النصيبة وهي علامة تنصب للقوم (tahdhib)؛ النصيب الحجارة تنصب على الشيء وجمعه نصائب ونصب (mufradat)","source_summary":"Ortak anlam, bir yeri belli eden veya bir su yapısının kenarını oluşturan dikili taştır. Kullanım, topluluk işaretinden bölge sınırına, kuyu ve havuz çevresindeki taşlara ve bu taşlarla yapılmış havuz adına uzanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامات المنصوبة للقوم أو حدود الحرم، ونصائب الحوض وحجارته المنصوبة على شفيره، والحوض المبني من الحجارة","what_is_not_ar":"لا يدخل الحجر المعبود أو المذبوح عليه، ولا نصيب الحظ"},"support_links":["sup_2be521c5a9464c806ebb"]},{"boundary":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B004","candidate_links":[{"candidate_id":"cand_0200dffa7b3c3c9746d7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"yorgunluk ve yıpratıcı sıkıntı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel bitkinliği ve hastalık, kaygı ya da belanın insan üzerinde bıraktığı yorucu etkiyi kapsar.","boundary_detail":"Dik durma ile kurulan açıklama tarihsel bir anlamlandırmadır; fiziksel diklik bu dalın güncel kavramsal koşulu değildir.","branch_image_ar":"تعب وعناء وبلاء ينهك الإنسان","concept_gloss":"yorgunluk ve yıpratıcı sıkıntı","contextual_glosses":[{"applicability":"İnsan bedeninin emek, yürüyüş veya hastalık yüzünden gücünü yitirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel gücün azalmasıyla ortaya çıkan yoğun yorgunluğu korur."},"facet_ids":["F001"],"text":"bitkinlik","usage_role":"contextual"},{"applicability":"Bir olayın, kaygının veya hastalığın kişide yorgunluk ve tedirginlik oluşturduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış etkenin kişide yorgunluk ve huzursuzluk oluşturmasını korur."},"facet_ids":["F003"],"text":"yorup huzursuz etmek","usage_role":"contextual"}],"definition":"Emek, hastalık, kaygı, üzüntü veya başka bir sıkıntının insanı yıpratmasıyla oluşan yorgunluk ve bitkinliktir. Aynı anlam alanı, bir etkenin kişiyi yorup huzursuz etmesini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedensel ya da ruhsal yükün doğurduğu yorgunluk, bitkinlik ve tükenmişlik."},{"facet_id":"F002","role":"extension","statement":"Hastalık, kaygı, üzüntü, kötülük veya bela nedeniyle yaşanan yıpratıcı sıkıntı."},{"facet_id":"F003","role":"associated_use","statement":"Bir olayın, hastalığın veya düşüncenin kişiyi yorup huzursuz etmesi."}],"identity_rationale":"Dal, bedensel bitkinlik ve yorulmayı, insanı yıpratan emek, hastalık, kaygı, üzüntü ve belayı ortak bir etkilenme ekseninde doğru toplar. Bir şeyin kişiyi yormasını bildiren ettirgen kullanım da aynı etkinin katılımcı yönünü değiştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yorgunluk, bitkinlik, zahmet ve sıkıntı"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"hastalığın verdiği bitkinlik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"beni yordu ve huzursuz etti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yorucu veya yorgunluk içindeki"}],"lexicalization_note":"Tanım yalın yorgunluk anlamını korur; hastalık, kaygı ve bir şeyin kişiyi yorması gibi yapıya bağlı kullanımları ayrı yüzler olarak gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bazıları yalnızca bedensel bitkinliği, bazıları zorluğu, bazıları da başkasını yorma eylemini öne çıkarır. En geniş gerçek örtüşme yorgunluk ve güçsüzlük dalındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal etkileyen hastalık ve ruhsal sıkıntıya kadar uzanır; komşu dal ise güçsüzlük ile süregelen emek ve meşakkat boyutunu daha belirgin taşır.","focus_only":"Odak dal, yorgunluğun yanında hastalık, kaygı, üzüntü ve belanın doğurduğu yıpratıcı etkiyi özellikle kapsar.","gloss":"yorgunluk ve güçsüzlük","neighbor_only":"Komşu dal, yorgunlukla birlikte güçsüzlük durumunu ve uzun uğraşın getirdiği genel meşakkati daha açık biçimde kapsar.","neighbor_ref":"root_001360/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yorgunluk, bitkinlik ve bir başkasını yorma anlamlarında geniş ölçüde örtüşür."}],"source_phrase_ar":"النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي (maqayis)؛ النصب الإعياء والتعب؛ النصب الشر والبلاء؛ نصب الداء (ayn)؛ تغير الحال من مرض أو تعب؛ الحزن إذا أثر فيه؛ المنصبة كد وتعب (jamhara)؛ نصب الرجل تعبا؛ النصب الشر والبلاء (sihah)؛ النصب الإعياء من العناء؛ نصب له الهم وأنصبه؛ نصب الداء (tahdhib)؛ النصب التعب؛ أنصبني كذا أي أتعبني وأزعجني (mufradat)","source_summary":"Ortak çekirdek yorgunluk, bitkinlik ve zahmettir. Anlam bedensel emekten hastalık ve ruhsal sıkıntının etkisine uzanır; geçişli kullanımda ise bu durumu doğuran olay veya hastalık özne olur.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب بمعنى الإعياء والتعب والعناء والكد، وما ينشأ من مرض أو هم أو حزن أو بلاء، وأنصبني الشيء إذا أتعبني","what_is_not_ar":"لا يدخل القيام المنتصب الحسي إلا من جهة تفسير التعب بالملازمة حتى الإعياء"},"support_links":["sup_b7f19790cde1af2162cd"]},{"boundary":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_kind":"bare","branch_ref":"root_001507/B005","candidate_links":[{"candidate_id":"cand_d7cab3964f68704994d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"belirlenmiş pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bütünden kişiye ayrılmış veya ona düşmüş belirli bölümü en kısa biçimde karşılar.","boundary_detail":"Anlam bir bütünden ayrılan belirli payla sınırlıdır; borç, hak, ölçü eşiği veya bölüştürme işleminin kendisi zorunlu değildir.","branch_image_ar":"حظ معين مرفوع لصاحبه","concept_gloss":"belirlenmiş pay","contextual_glosses":[{"applicability":"Bağlam, bir bütünden kime ne kadar düştüğünü zaten belirgin kılıyorsa doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir bütünden kişiye düşen veya ayrılan bölüm anlamını korur."},"facet_ids":["F001"],"text":"pay","usage_role":"general"}],"definition":"Bir şeyden bir kişi için ayrılan, ona düşen veya onun adına belirlenen paydır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünden belirli bir kişiye ayrılan veya ona düşen pay."}],"identity_rationale":"Dal, bir bütünden bir kişiye düşen veya onun için belirlenen pay anlamını doğru verir. Payın belirlenmiş olması çekirdektir; dikili taş, taş havuz, köken ya da ölçü eşiği anlamları aynı ses biçimini paylaşsa da bu dala girmez.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"pay veya bir şeyden ayrılan belirli bölüm"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"pay"}],"lexicalization_note":"Tanım yalın pay anlamını verir ve belirli hukuk, miras, ceza ya da ölçü kalıplarını genel anlama eklemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hak, borç, ceza payı ve hesap terimleri daha dar bağlamlara bağlıdır. En yakın sınır, belirlenmiş pay ile paylaştırma işlemini de kapsayan komşu anlam arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bölüştürmenin sonucundaki paydır; komşu dal hem bu sonucu hem de paylara ayırma işlemini içerir.","focus_only":"Odak dal, yalnızca kişiye düşen veya onun için belirlenen payı adlandırır.","gloss":"pay ve paylaştırma","neighbor_only":"Komşu dal, payın yanı sıra şeyi kişiler arasında bölme, denkleştirme ve paylaştırma işlemini de kapsar.","neighbor_ref":"root_001224/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir bütünden kişinin aldığı belirli bölümü pay olarak adlandırır."}],"source_phrase_ar":"النصيب الحظ من الشيء (maqayis;sihah)؛ النصب النصيب لغة (ayn;tahdhib)؛ النصيب معروف والجمع أنصباء وأنصبة (jamhara)؛ النصيب الحظ المنصوب أي المعين (mufradat)","source_summary":"Ortak anlatım, bir şeyden kişiye düşen belirli payı gösterir. Çoğul biçimler bu payların birden çok kişiye veya bölüme ait olabileceğini belirtir, fakat çekirdeği değiştirmez.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه النصيب بمعنى الحظ أو القسم المعين من الشيء، وما سمي منصوبا أو مرفوعا لصاحبه","what_is_not_ar":"لا يدخل الحجارة أو الحوض المسمى نصيبا، ولا النصاب بمعنى الأصل أو القدر"},"support_links":["sup_efb84234ab2b0b50832c"]},{"boundary":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B006","candidate_links":[{"candidate_id":"cand_d7cab3964f68704994d0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"temel veya sabit başvuru noktası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bıçağın elde tutulan sapı veya arka bölümü."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."}},{"facet_id":"F005","role":"specialization","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın söz kalıplarına göre köken, dayanak, dönüş noktası veya belirlenmiş eşik olarak gerçekleşen ortak çekirdeğini verir.","boundary_detail":"Genel bir pay veya rastgele miktar anlamı çıkarılamaz; her özel gerçekleşme kanıtlanan nesne ve söz kalıbıyla sınırlıdır.","branch_image_ar":"نصاب الشيء: أصله ومقداره الثابت","concept_gloss":"temel veya sabit başvuru noktası","contextual_glosses":[{"applicability":"Bıçağın elde tutulan arka bölümü veya ona sonradan takılan sap anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bıçağın elde tutulan sap veya arka bölümünü eksiksiz karşılar."},"facet_ids":["F002"],"text":"bıçak sapı","usage_role":"contextual"},{"applicability":"Mal miktarının belirli bir mali yükümlülüğü doğurduğu alt sınırdan söz edildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sabit mal miktarının yükümlülüğü başlatan alt eşik oluşunu korur."},"facet_ids":["F003"],"text":"yükümlülük eşiği","usage_role":"explanatory"},{"applicability":"Kişinin geldiği aile çizgisi, kökeni ve buna bağlı saygınlığı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ailesel kökenini ve geldiği soy çizgisini korur."},"facet_ids":["F004"],"text":"soy kökeni","usage_role":"contextual"},{"applicability":"Güneşin ufukta kaybolduğu yön veya yer bir dönüş noktası gibi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Güneşin gün sonunda ufukta kaybolduğu yeri tam olarak korur."},"facet_ids":["F005"],"text":"güneşin battığı yer","usage_role":"contextual"}],"definition":"Bir şeyin dayandığı temel, döndüğü başvuru noktası veya sabitlenmiş ölçüsüdür. Bu çekirdek, yalnızca belirli kullanımlarda bıçağın sapını, mali yükümlülük doğuran alt eşiği, kişinin köken ve soyunu ya da güneşin batış yerini gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin dayandığı temel, köken, dönüş noktası veya sabit başvuru ölçüsü."},{"facet_id":"F002","role":"specialization","statement":"Bıçağın elde tutulan sapı veya arka bölümü."},{"facet_id":"F003","role":"specialization","statement":"Malın belirli bir mali yükümlülüğü doğurduğu sabit alt miktar."},{"facet_id":"F004","role":"specialization","statement":"Bir kişinin geldiği köken, yetiştiği soy ve bu kökene dayanan saygınlık."},{"facet_id":"F005","role":"specialization","statement":"Güneşin gün sonunda döner gibi görünüp battığı yer."}],"identity_rationale":"Dal, temel, dönüş noktası ve sabit ölçü düşüncesini taşıyan kullanımları doğru toplar; ancak bunlar tek bir yalın ve her bağlama uygulanabilir anlam değildir. Bıçak sapı, mali yükümlülük eşiği, soy kökeni ve güneşin batış yeri yalnızca kendi söz kalıpları içinde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin temeli ve dönülen başvuru noktası"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bıçağın sapı veya arka bölümü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"mal için mali yükümlülük doğuran alt miktar"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"köken, soy ve aileden gelen saygınlık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"güneşin battığı ve döndüğü yer"}],"lexicalization_note":"Tanım ortak temel ve sabit başvuru noktasını verir; bıçak, mal, soy ve güneşle kurulan anlamları ayrı ve kalıba bağlı uzmanlaşmalar olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hesap, ağırlık ve ölçme dalları yalnızca sabit miktar yüzünü, köken dalları ise yalnızca temel yüzünü paylaşır. Bu nedenle yayımlanan ilişki eş anlamlılık değil aynı alan karşılaştırmasıdır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak köken alanına rağmen odak dal farklı nesnelerde sabit başvuru ve eşik anlamları taşıyan bir kullanım ailesidir; komşu dalın nesne kapsamı ayrıdır.","focus_only":"Odak dal, kökenin yanı sıra bıçak sapı, mali eşik ve güneşin batış yeri gibi kalıplaşmış başvuru noktalarını kapsar.","gloss":"köken ve çıkış yeri","neighbor_only":"Komşu dal, kişinin soy kökenini ve hörgücün kök bölümünü kendi sözlüksel alanında adlandırır.","neighbor_ref":"root_000340/B005","relation_type":"same_field","shared_zone":"Her iki dal da bir varlığın geldiği temel veya köken noktasını gösterebilir."}],"source_phrase_ar":"نصاب الشيء أصله؛ نصاب السكين؛ بلغ المال النصاب الذي تجب فيه الزكاة (maqayis)؛ نصاب كل شيء أصله ومرجعه؛ رجع إلى مركبه ومنصبه أي أصل منبته وحسبه؛ نصاب الشمس مغيبها (ayn)؛ نصاب السكين؛ نصاب صدق أي حسب ثابت (jamhara)؛ المنصب الأصل وكذلك النصاب؛ النصاب من المال القدر الذي تجب فيه الزكاة؛ نصاب السكين مقبضه (sihah)؛ نصاب كل شيء أصله ومرجعه؛ نصاب الشمس مغيبها؛ أنصبت السكين جعلت لها نصابا (tahdhib)؛ نصاب السكين ونصبه؛ نصاب الشيء أصله؛ رجع فلان إلى منصبه أي أصله (mufradat)","source_summary":"Ortak malzeme temel ve geri dönülen başvuru noktası çevresinde toplanır, fakat kullanımlar güçlü biçimde sözlüksel sınırlıdır. Bıçak sapı, mali eşik, soy kökeni ve güneşin batış yeri aynı genel sözcük ailesinin ayrı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه نصاب الشيء أي أصله ومرجعه، ونصاب السكين ومقبضها أو عجزها، ونصاب المال الذي تجب فيه الزكاة، ونصاب الشمس مغيبها، والمنصب بمعنى الأصل والحسب","what_is_not_ar":"لا يدخل النصيب بمعنى الحظ، ولا النصب بمعنى التعب أو الحجر المعبود"},"support_links":["sup_efb84234ab2b0b50832c"]},{"boundary":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_kind":"collocation","branch_ref":"root_001507/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"dil bilgisinde yükleme konumu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca çekim ve değişmez biçim çözümlemesindeki özel dil bilgisi kategorisini adlandırır.","boundary_detail":"Bu anlam yalnızca belirtilen dil bilgisi terimi ve ona bağlı sözcük biçimleri için geçerlidir; fiziksel yükseltme veya şarkı söyleme anlamına genellenmez.","branch_image_ar":"نصب الكلمة في الإعراب","concept_gloss":"dil bilgisinde yükleme konumu","contextual_glosses":[{"applicability":"Bir sözcüğün cümle içindeki çekim konumu özel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sözcüğün yükleme konumuna yerleştirilmiş olmasını tam olarak korur."},"facet_ids":["F001"],"text":"yükleme konumundaki sözcük","usage_role":"explanatory"}],"definition":"Çekimli dil bilgisinde üst konumun karşıtı olan yükleme konumu; değişmez yapılarda ise açık ünlülü biçime denk sayılan dil bilgisel kategoridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekimli sözcüklerde üst konumun karşısında bulunan yükleme konumu."},{"facet_id":"F002","role":"source_variant","statement":"Değişmez sözcük biçimlerinde açık ünlülü yapıya denk sayılan terimsel kullanım."}],"identity_rationale":"Dal, çekimli dil bilgisinde üst konumun karşısında yer alan yükleme konumunu ve değişmez biçimlerde açık ünlülü yapıyla kurulan benzerliği doğru verir. Ağız içindeki ses yükselişine ilişkin açıklama kategori tanımının kendisi değil, sesletim temelli bir gerekçelendirmedir.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çekimde üst konumun karşıtı olan yükleme konumu"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yükleme konumuna getirilmiş sözcük"}],"lexicalization_note":"Tanım açıkça dil bilgisi yapısına bağlıdır ve bu terimsel kullanımdan yalın kök için genel bir anlam çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; diğerleri dil bilgisinin farklı bölümlerini veya genel anlatımı paylaşır, fakat aynı çekim ekseninde yer almaz. Doğrudan karşıtlık yalnızca üst konum dalıyla kuruludur.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bunlar aynı eksenin karşıt kutuplarıdır: odak dal yükleme yönündeki konumu, komşu dal ise üst konumu belirtir.","focus_only":"Odak dal, çekimde yükleme yönündeki alt konumu ve değişmez biçimde açık ünlülü yapıyı gösterir.","gloss":"karşıt çekim konumları","neighbor_only":"Komşu dal, aynı çekim düzenindeki karşıt üst konumu ve değişmez biçimde yuvarlak ünlülü yapıyı gösterir.","neighbor_ref":"root_000582/B012","relation_type":"polarity_pair","shared_zone":"İki dal aynı dil bilgisi sisteminde sözcüğün biçimsel çekim konumunu belirler."}],"source_phrase_ar":"في الفتح هو النصب كأن الكلمة تنتصب في الفم (maqayis)؛ النصب ضد الرفع في الإعراب؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (ayn)؛ النصب في الإعراب كالفتح في البناء (sihah)؛ الكلمة المنصوبة يرفع صوتها إلى الغار الأعلى (tahdhib)؛ النصب في الإعراب معروف (mufradat)","source_summary":"Ortak çekirdek belirli bir dil bilgisi konumudur ve karşıt üst konumla tanımlanır. Bazı açıklamalar bunu değişmez yapılardaki açık ünlülü biçime veya sözcüğün ağızda daha yukarıdan seslendirilmesine benzetir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب النحوي ضد الرفع أو كالفتح في البناء، والكلمة المنصوبة والحرف المنصوب","what_is_not_ar":"لا يدخل رفع الشيء حسيا ولا رفع الصوت في الغناء إلا من جهة التشبيه الذي ذكرته المصادر"},"support_links":[]},{"boundary":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_kind":"non_bare","branch_ref":"root_001507/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"birine savaş veya düşmanlıkla karşı çıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir kişiye açıkça hasım olma, savaş açma veya düşmanlık yöneltme bağlamlarında kullanılır.","boundary_detail":"Kullanım kişiyle ve düşmanlık ya da savaş içeriğiyle sınırlıdır; genel karşı koyma, savunma veya fiziksel dikme tek başına bu dala girmez.","branch_image_ar":"مواجهة العداوة والحرب","concept_gloss":"birine savaş veya düşmanlıkla karşı çıkma","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişiye açıkça düşmanlık besleyip bunu davranışa dönüştürdüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşmanlığın belirli bir kişiye yönelmesini ve açık hâle gelmesini korur."},"facet_ids":["F001"],"text":"ona düşman kesilmek","usage_role":"contextual"},{"applicability":"Hasmane yönelişin doğrudan savaş başlatma veya savaşla karşı karşıya gelme biçiminde gerçekleştiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Savaşın belirli bir kişiye yöneltilmesini açık biçimde korur."},"facet_ids":["F002"],"text":"ona savaş açmak","usage_role":"contextual"}],"definition":"Bir kişiye savaş, kötülük veya düşmanlıkla yönelmek; onun karşısına açıkça hasım olarak çıkmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin karşısına savaş veya düşmanlıkla çıkıp ona hasım olmak."},{"facet_id":"F002","role":"specialization","statement":"Düşmanlığı veya savaşı belirli bir kişiye yöneltilmiş bir tutum olarak kurmak."}],"identity_rationale":"Dal, belirli bir kişiye savaş, kötülük veya düşmanlıkla açıkça yönelme anlamını doğru verir. Anlam sıradan bir nesneyi dikmekten değil, karşı tarafa hasmane bir tutum veya savaş durumu kurmaktan oluşur.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"birine savaş veya düşmanlıkla karşı çıkmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"ona düşman olmak veya düşmanlık yöneltmek"}],"lexicalization_note":"Tanım yalnızca kişiyle kurulan düşmanlık ve savaş yapılarına bağlıdır; bu kullanımlardan yalın ve genel bir kök anlamı üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; savaş, savunma, mücadele ve uzun süreli husumet dalları aynı senaryonun farklı bölümleridir. En yakın sınır, genel hasmane yöneliş ile düşmanlığı ilk kez açık etme arasındadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hasmane karşılaşmanın genel durumunu verir; komşu dal ise düşmanlığın ilk açık ilanı veya başlangıç anıyla sınırlıdır.","focus_only":"Odak dal, bir kişiye savaş veya düşmanlıkla yönelmeyi, bunun başlamış ya da sürmekte olmasını kapsar.","gloss":"açık düşmanlık başlatma","neighbor_only":"Komşu dal, düşmanlığın ilk kez açıkça ortaya konmasını ve karşı tarafa bildirilmesini özellikle şart koşar.","neighbor_ref":"root_001302/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da düşmanlığın belirli bir kişiye açıkça yöneltilmesini anlatır."}],"source_phrase_ar":"ناصبت فلانا الشر والحرب والعداوة (ayn;tahdhib)؛ نصبت لفلان نصبا إذا عاديته؛ ناصبته الحرب مناصبة (sihah)؛ ناصبه الحرب والعداوة ونصب له (mufradat)","source_summary":"Ortak anlatım, savaşın veya düşmanlığın belirli bir kişiye yöneltilmesini ve kişinin karşısına hasım olarak çıkılmasını gösterir. Fiil, hem karşılıklı savaşmayı hem de birine düşmanlık kurmayı anlatabilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ناصب فلانا الشر أو الحرب أو العداوة، ونصب له أو نصب لهم حربا، أي واجهه وعداه","what_is_not_ar":"لا يدخل مجرد نصب الشيء الحسي إلا إذا كان المنصوب هو الحرب أو العداوة"},"support_links":[]},{"boundary":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"özel bir şarkı veya ezgi türü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kendine özgü bir şarkı veya ezgi türü."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel olarak kanıtlanan özel şarkı veya ezgi türünü belirtir; bazı kullanımlarda yolculukta söylenen, hayvan sürme çağrısına benzer görece yumuşak biçimi kapsar.","boundary_detail":"Dal belirli ezgi türüyle sınırlıdır; genel şarkı söyleme, güzel ses, çalgı sesi veya yalnızca yüksek sesle söyleme bu anlamı tek başına karşılamaz.","branch_image_ar":"غناء يرفع به الصوت","concept_gloss":"özel bir şarkı veya ezgi türü","contextual_glosses":[{"applicability":"Bağlam ezginin özel türünü ve yolculuk sırasında söylendiğini zaten gösteriyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özel şarkı türünün yolculuk bağlamındaki kullanımını korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisi","usage_role":"contextual"},{"applicability":"Bir yolcunun bu özel ezgi türünü seslendirmesi eylem olarak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yolcunun belirli ezgi türünü söylemesi eylemini tam olarak korur."},"facet_ids":["F001","F002"],"text":"yolcu ezgisini söylemek","usage_role":"contextual"}],"definition":"Belirli bir şarkı veya ezgi türüdür. Bazı kaynaklarda yolcuların söylediği, hayvan sürerken kullanılan çağrılı ezgiye benzeyen ve ondan daha yumuşak olabilen bir tür olarak açıklanır. Adının sesi yükseltmeyle ilişkisi kesin anlam değil, olası bir türetme açıklamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kendine özgü bir şarkı veya ezgi türü."},{"facet_id":"F002","role":"specialization","statement":"Yolcuların söylediği, hayvan sürme çağrılı ezgisine benzeyen fakat ondan daha yumuşak olabilen ezgi."},{"facet_id":"F003","role":"source_variant","statement":"Tür adını sesi yükseltme düşüncesine bağlayan kesin olmayan açıklama."}],"identity_rationale":"Kaynak ifadesinin çekirdeği sesi yükseltmenin kendisi değil, belirli bir şarkı ve ezgi türüdür. Yolcuların söylediği ve hayvan sürme ezgisine benzediği, fakat daha yumuşak olabildiği belirtilir; ses yükseltme bağlantısı yalnızca olası bir adlandırma açıklamasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"yolcuların söylediği özel ezgi türü"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"hayvan sürme çağrısına benzeyen yumuşak yolcu ezgisi"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"yolcu ezgisini söyledi"}],"lexicalization_note":"Tanım ezgi türünün yalın adını, onun yolcu şarkısı kalıbını ve bu ezgiyi söyleme fiilini ayırır; yüksek ses varsayımını çekirdeğe dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çalgı, ses yineleme, yüksek ses ve biçimlenmiş ezgi adayları yalnızca müzik senaryosunu paylaşır. En yakın sınır özel yolcu ezgisi ile genel şarkı ve ezgili ses alanıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir yolcu ezgisi türüdür; komşu dal ise şarkı ve ezgili ses alanının genel adıdır.","focus_only":"Odak dal, yolcularla ve hayvan sürme çağrılı ezgisine benzer yumuşak söyleyişle sınırlı özel bir türdür.","gloss":"şarkı ve ezgili ses","neighbor_only":"Komşu dal, şarkıyı, güzel sesi, ezgili dinletiyi ve okumanın duygulu ya da ince söylenişini daha genel kapsar.","neighbor_ref":"root_001110/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da insan sesiyle ezgili ve dinlenebilir bir söyleyişi anlatır."}],"source_phrase_ar":"النصب جنس من الغناء ولعله مما ينصب أي يعلي به الصوت (maqayis)؛ غناء النصب ضرب من الألحان؛ غناء لهم يشبه الحداء إلا أنه أرق منه (sihah)؛ النصب ضرب من أغاني الأعراب؛ نصب الراكب إذا غنى النصب؛ غناء الركبان؛ حداء يشبه الغناء (tahdhib)؛ في الغناء ضرب منه (mufradat)","source_summary":"Ortak çekirdek belirli bir ezgi türüdür. Bu tür yolculuk ve hayvan sürme bağlamıyla ilişkilendirilir, benzer çağrılı ezgiden daha yumuşak sayılabilir ve adının sesi yükseltmekten geldiği yalnızca olasılık olarak açıklanır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه النصب ضربا من الغناء أو الألحان، وغناء الركبان أو الحداء المشبه بالغناء، والفعل نصب الراكب إذا غناه","what_is_not_ar":"لا يدخل النصب النحوي ولا رفع الشيء الحسي إلا من جهة رفع الصوت"},"support_links":[]},{"boundary":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001507/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","surface_ar":"نُصِبَتْ"}],"gloss":"yolculuğu yumuşak sürdürme veya artırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}}],"root_ar":"ن ص ب","root_id":"root_001507","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel söz yapısında hem gün boyu yumuşak ilerleme hem de yol alışını yükseltme çeşitlemesini kapsar.","boundary_detail":"Anlam, yolculuğu sürdürme yapısına bağlıdır; yorgunluk sonucu, gece yolculuğu, hızlı geçiş veya kesintisiz ilerleme tek başına bu dal değildir.","branch_image_ar":"سير اليوم سيرا لينا","concept_gloss":"yolculuğu yumuşak sürdürme veya artırma","contextual_glosses":[{"applicability":"Topluluğun gündüz boyunca hafif ve yumuşak bir yürüyüşle yol aldığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gün boyu süren yumuşak ilerleyiş çeşitlemesini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"gün boyu yumuşak ilerlemek","usage_role":"contextual"},{"applicability":"Topluluğun ilerleyişini yükselttiği veya yolculuk çabasını artırdığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alışını yükseltme ve ilerleyişi artırma çeşitlemesini korur."},"facet_ids":["F001","F003"],"text":"yol alışını artırmak","usage_role":"contextual"}],"definition":"Bir topluluğun yolculuğu sürdürmesiyle ilgili özel kullanımdır. Bağlama göre gün boyunca yumuşak biçimde ilerlemeyi veya yol alışını yükseltip artırmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun yolculuk hâlinde ilerlemesi ve yol alışını sürdürmesi."},{"facet_id":"F002","role":"source_variant","statement":"Topluluğun gün boyunca yumuşak bir yürüyüşle yol alması."},{"facet_id":"F003","role":"source_variant","statement":"Topluluğun yol alışını yükseltmesi veya ilerleyişini artırması."}],"identity_rationale":"Dalın yolculukla ilgili kimliği doğrudur, ancak kaynak ifadesi tek biçimli bir hız niteliği vermez. Bir anlatım yol alışını yükseltip artırmayı, diğer anlatımlar ise gün boyunca yumuşak biçimde ilerlemeyi bildirir; iki çeşitleme aynı özel söz yapısı içinde ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"gün boyunca yumuşak biçimde ilerlediler"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"yol alışlarını yükseltip artırdılar"}],"lexicalization_note":"Tanım yalnızca topluluğun yol alması ve yolculuğu sürdürmesi yapılarında geçerlidir; gün boyu yumuşak ilerleme ile yol alışını artırma çeşitlemelerini birbirine karıştırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kesintisiz, geceleyin, hızlı veya uzaklara yapılan yolculuklar farklı koşullar taşır. En yakın örtüşme yumuşak ilerleyiştedir, ancak odak dalın gün boyu sürme ve artırma çeşitlemeleri daha geniştir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli topluluk ve yolculuk yapısında gün boyu sürme ya da artırma seçeneklerini taşır; komşu dal yalnızca yumuşak hız niteliğine odaklanır.","focus_only":"Odak dal, topluluğun gün boyunca yol almasını ve ayrıca yol alışını artırma çeşitlemesini içerir.","gloss":"yumuşak yol alma","neighbor_only":"Komşu dal, gün boyu sürme veya ilerleyişi artırma koşulu olmadan yalnızca yumuşak yürüyüşü belirtir.","neighbor_ref":"root_000664/B013","relation_type":"near_synonym","shared_zone":"Her iki dal da yolculuğun yumuşak ve hafif bir ilerleyişle yapılmasını anlatabilir."}],"source_phrase_ar":"نصب القوم السير نصبا إذا رفعوه (jamhara)؛ نصب القوم ساروا يومهم وهو سير لين (sihah)؛ نصبوا نصبا وهو سير لين (tahdhib)","source_summary":"Ortak bağlam bir topluluğun yol almasıdır, fakat nitelik anlatımı ikiye ayrılır: gün boyunca yumuşak ilerleme ve yol alışını yükseltip artırma. Bu karşıt görünümler tek bir hız özelliğine indirgenmeden korunmalıdır.","sources":["JA","SI","TA"],"what_is_ar":"يدخل فيه نصب القوم أو نصب السير: ساروا يومهم أو رفعوا السير، وهو سير لين في بعض المصادر","what_is_not_ar":"لا يدخل التعب من السفر إلا إذا دل السياق على الإعياء لا على نوع السير"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["88:19:1"],"branch_refs":[],"candidate_id":"cand_5a8efb929e2b53877b8b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:1:coordinating-continuation","source_type":"word_analysis","support_ids":["sup_2a3a21306ec16300cce0","sup_c23f57768f8f2c421c4f"],"title":"continuation rather than restart","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:1","qac_refs":["88:19:1:1"],"status":"accepted"}},{"anchor_refs":["88:19:1"],"branch_refs":[],"candidate_id":"cand_8d0a416d2bd747068ca1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:1:separate-from-preposition","source_type":"word_analysis","support_ids":["sup_0a40a9b38e1332ab32a0","sup_c23f57768f8f2c421c4f"],"title":"connector heard against direction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:1","qac_refs":["88:19:1:1"],"status":"accepted"}},{"anchor_refs":["88:19:1"],"branch_refs":[],"candidate_id":"cand_a7fd9d3efbf0c23b2ac3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:1:survey-link","source_type":"word_analysis","support_ids":["sup_9ba415ff3e3f452027d7","sup_c23f57768f8f2c421c4f"],"title":"middle link in the repeated survey","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:1","qac_refs":["88:19:1:1"],"status":"accepted"}},{"anchor_refs":["88:19:2"],"branch_refs":[],"candidate_id":"cand_5ac79d7a53636eda7660","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:2:attentional-target","source_type":"word_analysis","support_ids":["sup_1ab72ff56bb4318af845","sup_f0cb39ac974d0aec31cd"],"title":"direction of attention","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:2","qac_refs":["88:19:1:2"],"status":"accepted"}},{"anchor_refs":["88:19:2"],"branch_refs":[],"candidate_id":"cand_7ae3cab8d12458fb282e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:2:independent-preposition","source_type":"word_analysis","support_ids":["sup_1ab72ff56bb4318af845","sup_401e4d7491784b17e437"],"title":"separate governed form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:2","qac_refs":["88:19:1:2"],"status":"accepted"}},{"anchor_refs":["88:19:2"],"branch_refs":[],"candidate_id":"cand_99233ea41de47c5967d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:2:repeated-attention-operator","source_type":"word_analysis","support_ids":["sup_1ab72ff56bb4318af845","sup_f01ecebca715dd48461e"],"title":"repeated operator in the chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:2","qac_refs":["88:19:1:2"],"status":"accepted"}},{"anchor_refs":["88:19:2"],"branch_refs":[],"candidate_id":"cand_701a6512107b73c6c4eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:2:target-before-manner","source_type":"word_analysis","support_ids":["sup_1ab72ff56bb4318af845","sup_f68cd6dfc907c88f631c"],"title":"target precedes the question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:2","qac_refs":["88:19:1:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_3c6549283ecb5cda07a9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:acoustic-weight","source_type":"word_analysis","support_ids":["sup_2c681a2bb5104d3ce1bc","sup_faf97018b6065ab91be6"],"title":"broad target cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_56eed6e9d01a7de78440","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:definite-public-class","source_type":"word_analysis","support_ids":["sup_2c681a2bb5104d3ce1bc","sup_3796c009e003bc514c64"],"title":"recognized plural mountain class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_3a9592bcd17ecbeaa1a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:formed-mass-pressure","source_type":"word_analysis","support_ids":["sup_2c681a2bb5104d3ce1bc","sup_c2f703ef6e385dde1d55"],"title":"formed mass, not abstract height","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_5a3ec6254e9adeac3e0e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:sequence-architecture","source_type":"word_analysis","support_ids":["sup_2c681a2bb5104d3ce1bc","sup_7075a1a871e557c97fb2"],"title":"mountains mediate the survey","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_c3ae6bc2d925e13c302e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:stabilizing-intertexts","source_type":"word_analysis","support_ids":["sup_2c681a2bb5104d3ce1bc","sup_779675dc194e089aecb7"],"title":"pegs and anchoring contrasts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_f7bc5ecf9ac365cc7b7d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:3:target-and-patient","source_type":"word_analysis","support_ids":["sup_25ce4f79ab909115bc9e","sup_2c681a2bb5104d3ce1bc"],"title":"one noun carries two roles","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:3","qac_refs":["88:19:2:1","88:19:2:2"],"status":"accepted"}},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_43b75d996a1d20589ca0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:4:configuration-not-yes-no","source_type":"word_analysis","support_ids":["sup_619b19406c16748b0c88","sup_c92ec1041d87e8c90bcc"],"title":"visible result is presumed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:4","qac_refs":["88:19:3:1"],"status":"accepted"}},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_ce5582f423c3a3707f5a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:4:manner-over-passive","source_type":"word_analysis","support_ids":["sup_619b19406c16748b0c88","sup_d740f3fc4690996ad681"],"title":"manner question over the passive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:4","qac_refs":["88:19:3:1"],"status":"accepted"}},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_a9aaed7d04dffb9cc1b4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:4:pivot-architecture","source_type":"word_analysis","support_ids":["sup_619b19406c16748b0c88","sup_b3bdbdc6f2d6d88808c0"],"title":"pivot between target and result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:4","qac_refs":["88:19:3:1"],"status":"accepted"}},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_76b94f6c138b6c7e4738","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:4:repeated-method","source_type":"word_analysis","support_ids":["sup_3eab08ae379aa621edd4","sup_619b19406c16748b0c88"],"title":"same question binds the sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:4","qac_refs":["88:19:3:1"],"status":"accepted"}},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_16369a2c8cd5b40a00f2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:4:short-rhythmic-tightening","source_type":"word_analysis","support_ids":["sup_32d7312a75b162189918","sup_619b19406c16748b0c88"],"title":"short beat before closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:4","qac_refs":["88:19:3:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_6cb7273f98f236454e27","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:collective-agreement","source_type":"word_analysis","support_ids":["sup_62ca31c4123a2292de3b","sup_db73be2e54d137ad6daf"],"title":"plural mountains gathered grammatically","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_6bd39998b481bcf4f900","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:compact-fixed-sound","source_type":"word_analysis","support_ids":["sup_ac4f199368cebb144faa","sup_db73be2e54d137ad6daf"],"title":"compact fixed-sounding close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_18cac5eabd0f9a76cb50","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:distributional-standout","source_type":"word_analysis","support_ids":["sup_3a7f549b236353c04e0e","sup_db73be2e54d137ad6daf"],"title":"rare passive-result use","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_32a0dd52628f59b2c6a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:intertext-root-contrasts","source_type":"word_analysis","support_ids":["sup_bd4d791fd094b556ae45","sup_db73be2e54d137ad6daf"],"title":"anchoring and toil contrasts","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_8ae0aa6254db1854ec33","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:passive-completed-result","source_type":"word_analysis","support_ids":["sup_6b8cdb862d2c1cf98821","sup_db73be2e54d137ad6daf"],"title":"completed passive result","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_5dd52f6dee09487122c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:passive-result-series","source_type":"word_analysis","support_ids":["sup_2e22b4f0160a6a07f749","sup_db73be2e54d137ad6daf"],"title":"member of the passive-result series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_e780f1cf249eb44d39f1","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:upright-emplacement-root","source_type":"word_analysis","support_ids":["sup_37d5d25e39d9dd8876f8","sup_db73be2e54d137ad6daf"],"title":"upright emplacement from the root","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:5"],"branch_refs":[],"candidate_id":"cand_f7591b92ee8253c52004","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:5:variant-agency-contrast","source_type":"word_analysis","support_ids":["sup_d3d03c70255eed518eea","sup_db73be2e54d137ad6daf"],"title":"variant exposes agency contrast","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"88:19:5","qac_refs":["88:19:4:1"],"status":"accepted"}},{"anchor_refs":["88:19:2"],"branch_refs":[],"candidate_id":"cand_a37fa002c1d9047897f2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000217"],"scope":"focus_ayah","source_local_id":"88:19:2:2","source_type":"qac_morpheme","support_ids":["sup_bcdf4f4bf2826d33b245"],"title":"QAC root occurrence: ج ب ل","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:19:3"],"branch_refs":[],"candidate_id":"cand_b3019c8b5040e1c733ae","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"88:19:3:1","source_type":"qac_morpheme","support_ids":["sup_852c580c77526fa92e50"],"title":"QAC root occurrence: ك ي ف","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:19:4"],"branch_refs":[],"candidate_id":"cand_5615eeac7bd2e700d765","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001507"],"scope":"focus_ayah","source_local_id":"88:19:4:1","source_type":"qac_morpheme","support_ids":["sup_7e1ff9d400d0fcf4bcce"],"title":"QAC root occurrence: ن ص ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:19","branch_refs":["root_000217/B001","root_001507/B001","root_001507/B003"],"candidate_id":"cand_9a5ed1d7c0a7f63c0671","commentary_obligation":"review","hft_ref":"hft_6b404df600b2f7a0393c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_landmark_erection","source_type":"hft","support_ids":["sup_2be521c5a9464c806ebb"],"title":"b_landmark_erection","trust":"legacy_unbound"},{"anchor_refs":["88:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:19","branch_refs":["root_000217/B002","root_001507/B005","root_001507/B006"],"candidate_id":"cand_d7cab3964f68704994d0","commentary_obligation":"review","hft_ref":"hft_8bd1642a984b9c36a751","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_fixed_measure","source_type":"hft","support_ids":["sup_efb84234ab2b0b50832c"],"title":"b_fixed_measure","trust":"legacy_unbound"},{"anchor_refs":["88:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:19","branch_refs":["root_000217/B003","root_001507/B001","root_001507/B004"],"candidate_id":"cand_0200dffa7b3c3c9746d7","commentary_obligation":"review","hft_ref":"hft_4dc425ad3fe1f3a25225","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_embodied_posture","source_type":"hft","support_ids":["sup_b7f19790cde1af2162cd"],"title":"b_embodied_posture","trust":"legacy_unbound"},{"anchor_refs":["88:19"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:19","branch_refs":["root_000217/B007","root_001507/B001"],"candidate_id":"cand_6bddffd02279b87a580a","commentary_obligation":"review","hft_ref":"hft_c609e6b24e48f3c853a4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_woven_fixture","source_type":"hft","support_ids":["sup_1d2bde21ee5faa7dff30"],"title":"b_woven_fixture","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:19:1:1","qac_word_ref":"88:19:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:19:1:2","qac_word_ref":"88:19:1","root_ar":"","surface_ar":"إِلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:19:2:1","qac_word_ref":"88:19:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","root_ar":"ج ب ل","surface_ar":"جِبَالِ"},{"lemma_ar":"كَيْف","morph_features":"STEM|POS:INTG|LEM:kayof|ROOT:kyf","morpheme_role":"STEM","pos":"INTG","qac_ref":"88:19:3:1","qac_word_ref":"88:19:3","root_ar":"ك ي ف","surface_ar":"كَيْفَ"},{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","root_ar":"ن ص ب","surface_ar":"نُصِبَتْ"}],"word_analysis_qac_refs":[["88:19:1:1"],["88:19:1:2"],["88:19:2:1","88:19:2:2"],["88:19:3:1"],["88:19:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:19:1","88:19:2","88:19:3","88:19:4","88:19:5"]},"focus_surface_evidence":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:19:1:1","qac_word_ref":"88:19:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"إِلَىٰ","morph_features":"STEM|POS:P|LEM:<ilaY`","morpheme_role":"STEM","pos":"P","qac_ref":"88:19:1:2","qac_word_ref":"88:19:1","root_ar":"","surface_ar":"إِلَى"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"88:19:2:1","qac_word_ref":"88:19:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"جَبَل","morph_features":"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"88:19:2:2","qac_word_ref":"88:19:2","root_ar":"ج ب ل","surface_ar":"جِبَالِ"},{"lemma_ar":"كَيْف","morph_features":"STEM|POS:INTG|LEM:kayof|ROOT:kyf","morpheme_role":"STEM","pos":"INTG","qac_ref":"88:19:3:1","qac_word_ref":"88:19:3","root_ar":"ك ي ف","surface_ar":"كَيْفَ"},{"lemma_ar":"نُصِبَتْ","morph_features":"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"88:19:4:1","qac_word_ref":"88:19:4","root_ar":"ن ص ب","surface_ar":"نُصِبَتْ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:19:1:1"],["88:19:1:2"],["88:19:2:1","88:19:2:2"],["88:19:3:1"],["88:19:4:1"]],"word_analysis_refs":["88:19:1","88:19:2","88:19:3","88:19:4","88:19:5"],"word_rows":[{"analysis_record_ref":"88:19:1","analytic_gloss_range_en":"coordinating continuation in the repeated observation chain; locally additive rather than a loose restart or chronology marker","analytic_root_gloss_range_en":null,"qac_refs":["88:19:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:19:2","analytic_gloss_range_en":"directional preposition orienting attention toward the mountains as the inspected target, not a marker of physical travel or the endpoint of the setting-up action","analytic_root_gloss_range_en":null,"qac_refs":["88:19:1:2"],"root":{},"surface":{"arabic":"إِلَى","transliteration":"ilā"}},{"analysis_record_ref":"88:19:3","analytic_gloss_range_en":"the recognized plural mountain-masses as public, inspectable terrain; locally concrete mountains with formed-mass pressure, not an abstract high place or unrelated mountain-like abundance","analytic_root_gloss_range_en":"root range includes mountains as high solid masses, mountain-like abundance, thick build, formed constitution, hardness, and mountain-entering; here the local noun selects the concrete mountain class while formed constitution and mass remain lexical pressure","qac_refs":["88:19:2:1","88:19:2:2"],"root":{"arabic":"ج ب ل","transliteration":"j-b-l"},"surface":{"arabic":"ٱلْجِبَالِ","transliteration":"al-jibāli"}},{"analysis_record_ref":"88:19:4","analytic_gloss_range_en":"manner interrogative asking about mode, state, and configuration of the passive result; not a yes-no question and not an adjective for the mountains","analytic_root_gloss_range_en":null,"qac_refs":["88:19:3:1"],"root":{},"surface":{"arabic":"كَيْفَ","transliteration":"kayfa"}},{"analysis_record_ref":"88:19:5","analytic_gloss_range_en":"completed passive setting-up or emplacement of the mountains as an externally arranged result; the installer is withheld, and broader toil, share, marker, hostility, song, or travel branches are not selected locally except as contrastive pressure","analytic_root_gloss_range_en":"root range includes setting something upright and prominent, erected worship or boundary markers, weariness and strain, assigned share, fixed base or origin, grammatical accusative setting, hostile opposition, song mode, and a day-long march; local grammar selects passive upright emplacement","qac_refs":["88:19:4:1"],"root":{"arabic":"ن ص ب","transliteration":"n-ṣ-b"},"surface":{"arabic":"نُصِبَتْ","transliteration":"nuṣibat"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["88:19"],"branch_refs":["root_000217/B001","root_001507/B001","root_001507/B003"],"candidate_id":"cand_9a5ed1d7c0a7f63c0671","evidence_scope":"focus_ayah","hft_ref":"hft_6b404df600b2f7a0393c","item_id":"b_landmark_erection","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_landmark_erection","support_id":"sup_2be521c5a9464c806ebb"},{"anchor_refs":["88:19"],"branch_refs":["root_000217/B002","root_001507/B005","root_001507/B006"],"candidate_id":"cand_d7cab3964f68704994d0","evidence_scope":"focus_ayah","hft_ref":"hft_8bd1642a984b9c36a751","item_id":"b_fixed_measure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_fixed_measure","support_id":"sup_efb84234ab2b0b50832c"},{"anchor_refs":["88:19"],"branch_refs":["root_000217/B003","root_001507/B001","root_001507/B004"],"candidate_id":"cand_0200dffa7b3c3c9746d7","evidence_scope":"focus_ayah","hft_ref":"hft_4dc425ad3fe1f3a25225","item_id":"b_embodied_posture","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_embodied_posture","support_id":"sup_b7f19790cde1af2162cd"},{"anchor_refs":["88:19"],"branch_refs":["root_000217/B007","root_001507/B001"],"candidate_id":"cand_6bddffd02279b87a580a","evidence_scope":"focus_ayah","hft_ref":"hft_c609e6b24e48f3c853a4","item_id":"b_woven_fixture","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_woven_fixture","support_id":"sup_1d2bde21ee5faa7dff30"}],"diagnostics":[],"lane_counts":{"global":15,"macro":6,"micro":4},"packet_summary":{"ayah_count":26,"focus_ref":"88:19","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:19","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"88:19","lane":"micro","linguistic_source_ref":"88:19","surface_ref":"88:19","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:19","target_tokens":[["Ve",["88:19:1"]],["dağlara",["88:19:1","88:19:2"]],["nasıl",["88:19:3"]],["dikildiklerine",["88:19:4"]]],"text":"Ve dağlara, nasıl dikildiklerine;"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:1:separate-from-preposition","source_type":"word_analysis","support_id":"sup_0a40a9b38e1332ab32a0","text":"{\"blocking_evidence\":null,\"headline\":\"connector heard against direction\",\"reader_payoff\":\"The reader notices that the sound surface joins continuation to directed attention while the grammar still keeps the connector and preposition distinct.\",\"reason\":\"The bundle splits the prefixed coordinator from {{ar:إِلَى}} ({{tr:ilā}}), so the sound fusion can be noted without assigning directional force to {{ar:وَ}} ({{tr:wa}}).\",\"representative_source_ids\":[\"QF-18fb1b6e\",\"QP-b087b9ec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:2","source_type":"word_analysis","support_id":"sup_1ab72ff56bb4318af845","text":"{\"gloss_range\":\"directional preposition orienting attention toward the mountains as the inspected target, not a marker of physical travel or the endpoint of the setting-up action\",\"prose\":\"{{ar:إِلَى}} ({{tr:ilā}}) turns the listener toward the mountains before the ayah asks about their manner of standing. The preposition governs {{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}) as an endpoint of attention inherited from the earlier looking command, not as the endpoint or instrument of {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}). It sends perception and thought toward distant mass without implying physical travel. Because it remains distinct after {{ar:وَ}} ({{tr:wa}}), the prefixed opening does not erase the preposition's own government; it gives both continuity and orientation. Its repeated role in the inspection chain makes varied created domains parallel targets rather than separate proofs, and it prepares the same governed attention frame to move on to the ground-domain in 88:20.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِلَى}} ({{tr:ilā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:target-and-patient","source_type":"word_analysis","support_id":"sup_25ce4f79ab909115bc9e","text":"{\"blocking_evidence\":null,\"headline\":\"one noun carries two roles\",\"reader_payoff\":\"The reader notices that the mountains are first aimed at as the object of attention and then gathered as the passive patient of the result-state.\",\"reason\":\"{{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}) is genitive under {{ar:إِلَى}} ({{tr:ilā}}), and the passive verb agrees with the nonhuman plural as a feminine singular collective.\",\"representative_source_ids\":[\"QG-b0f403ed\",\"QG-ba5fbd9f\",\"QF-007064fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:1:coordinating-continuation","source_type":"word_analysis","support_id":"sup_2a3a21306ec16300cce0","text":"{\"blocking_evidence\":null,\"headline\":\"continuation rather than restart\",\"reader_payoff\":\"The reader notices that the ayah starts inside an ongoing inspection command, so the mountain scene is added to a survey rather than launched as a separate proof.\",\"reason\":\"The local ayah has no fresh looking verb, and the attachment evidence ties the fronted phrase back to the earlier observation frame; broader resumptive values of {{ar:وَ}} ({{tr:wa}}) are therefore narrowed to coordinating continuation here.\",\"representative_source_ids\":[\"QG-332c231f\",\"QG-95130038\",\"QS-d5cebaf4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3","source_type":"word_analysis","support_id":"sup_2c681a2bb5104d3ce1bc","text":"{\"gloss_range\":\"the recognized plural mountain-masses as public, inspectable terrain; locally concrete mountains with formed-mass pressure, not an abstract high place or unrelated mountain-like abundance\",\"prose\":\"{{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}) gives the ayah a public object: not a private marvel, but the recognized class of mountains. Its definite broken plural makes many landforms available as one familiar field of inspection, a formed class rather than a counted list. Grammar stacks two roles onto the same noun: it is governed by {{ar:إِلَى}} ({{tr:ilā}}) as the target of attention, then recovered by {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}) as the affected collective, so visible stability is recast as received emplacement. The {{ar:ج ب ل}} ({{tr:j-b-l}}) range keeps the concrete image of high solid mass and formed constitution alive: the listener is made to meet the mountains as concentrated bulk, not pass over them as scenery, while the local noun keeps the sense at actual mountains rather than unrelated branches such as mountain-like abundance. Intertexts sharpen the same public mass: mountains are called pegs in 78:7, and anchoring is stated with direct agency in 79:32, making this passive question's withheld agency more noticeable. Positioned between the encompassing height of the sky in 88:18 and the ground surface of 88:20, the noun mediates a vertical survey, and its broad cadence gives the target weight before the short manner-result close.\",\"root_display\":\"{{ar:ج ب ل}} ({{tr:j-b-l}})\",\"root_gloss_range\":\"root range includes mountains as high solid masses, mountain-like abundance, thick build, formed constitution, hardness, and mountain-entering; here the local noun selects the concrete mountain class while formed constitution and mass remain lexical pressure\",\"surface_display\":\"{{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:passive-result-series","source_type":"word_analysis","support_id":"sup_2e22b4f0160a6a07f749","text":"{\"blocking_evidence\":null,\"headline\":\"member of the passive-result series\",\"reader_payoff\":\"The reader notices that the word resolves the mountain ayah while handing the same passive-result grammar forward to the earth question.\",\"reason\":\"The adjacent passive closes in 88:18, 88:19, and 88:20 create a patterned survey from elevation to upright emplacement to horizontal spreading.\",\"representative_source_ids\":[\"QE-90dbd489\",\"QB-40dff339\",\"QY-8778d627\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4:short-rhythmic-tightening","source_type":"word_analysis","support_id":"sup_32d7312a75b162189918","text":"{\"blocking_evidence\":null,\"headline\":\"short beat before closure\",\"reader_payoff\":\"The reader notices the rhythm tighten after the longer target phrase and before the compact passive ending.\",\"reason\":\"The sound row has a distinct local payoff because the word's shortness supports the target-pivot-result staging.\",\"representative_source_ids\":[\"QP-0e6ccf2b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:definite-public-class","source_type":"word_analysis","support_id":"sup_3796c009e003bc514c64","text":"{\"blocking_evidence\":null,\"headline\":\"recognized plural mountain class\",\"reader_payoff\":\"The reader notices that ordinary, publicly recognized mountains are made newly inspectable rather than treated as background scenery.\",\"reason\":\"The local noun is definite, plural, concrete, and distributionally common; the manner question reactivates that familiar class as evidence.\",\"representative_source_ids\":[\"QG-56764076\",\"QF-940b4ae4\",\"QI-5e5131fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:upright-emplacement-root","source_type":"word_analysis","support_id":"sup_37d5d25e39d9dd8876f8","text":"{\"blocking_evidence\":null,\"headline\":\"upright emplacement from the root\",\"reader_payoff\":\"The reader notices the mountains as set upright and fixed into visible order, with marker and toil fields sharpening the contrast rather than replacing the local sense.\",\"reason\":\"V4 supports a primary branch of setting something upright and prominent, while local passive grammar selects that emplacement branch and does not license reflexive standing, human toil, cultic marker, share, hostility, song, or travel branches as local meanings.\",\"representative_source_ids\":[\"QS-4b7bc1e9\",\"QS-e0134ea9\",\"QI-5ff9db79\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:distributional-standout","source_type":"word_analysis","support_id":"sup_3a7f549b236353c04e0e","text":"{\"blocking_evidence\":null,\"headline\":\"rare passive-result use\",\"reader_payoff\":\"The reader notices that this passive-result verb stands out inside a root family often represented by nominal share or portion forms.\",\"reason\":\"The contextual profile marks this exact passive form as low occurrence, and V4 shows other accepted root branches; the local form remains verbal emplacement.\",\"representative_source_ids\":[\"QI-bca2ae5f\",\"QH-1ff9569a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4:repeated-method","source_type":"word_analysis","support_id":"sup_3eab08ae379aa621edd4","text":"{\"blocking_evidence\":null,\"headline\":\"same question binds the sequence\",\"reader_payoff\":\"The reader notices that different created domains are inspected through the same repeated manner-question rather than through separate argument types.\",\"reason\":\"The boundary rows and repeated construction place 88:19 between the sky question (88:18) and the earth question (88:20) in the same interrogative pattern.\",\"representative_source_ids\":[\"QE-9d3ee04c\",\"QB-0865b3b0\",\"QB-47457575\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:2:independent-preposition","source_type":"word_analysis","support_id":"sup_401e4d7491784b17e437","text":"{\"blocking_evidence\":null,\"headline\":\"separate governed form\",\"reader_payoff\":\"The reader notices that the prefixed opening does not erase the preposition's own government of the mountain noun.\",\"reason\":\"The QAC split and local case government keep {{ar:إِلَى}} ({{tr:ilā}}) as a distinct preposition with its own complement.\",\"representative_source_ids\":[\"QF-3042236f\",\"QT-0e11a0e4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4","source_type":"word_analysis","support_id":"sup_619b19406c16748b0c88","text":"{\"gloss_range\":\"manner interrogative asking about mode, state, and configuration of the passive result; not a yes-no question and not an adjective for the mountains\",\"prose\":\"{{ar:كَيْفَ}} ({{tr:kayfa}}) is the hinge of the ayah. It looks forward to {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}), asking about the mode, state, and configuration of the mountains' achieved standing, not modifying {{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}) as a descriptive adjective. The question therefore presumes the visible result instead of asking whether the mountains were set up, and it presses the reader to treat their arrangement as evidence demanding recognition. Its placement makes the ayah's three-beat architecture explicit: viewed target, manner pivot, passive result. In the repeated creation-sign sequence, this same interrogative method binds different domains to one question-form rather than separate argument types, while its short beat tightens the rhythm before the passive close.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَيْفَ}} ({{tr:kayfa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:collective-agreement","source_type":"word_analysis","support_id":"sup_62ca31c4123a2292de3b","text":"{\"blocking_evidence\":null,\"headline\":\"plural mountains gathered grammatically\",\"reader_payoff\":\"The reader notices that many mountains are grammatically gathered into one patient-collective at the verb's ending.\",\"reason\":\"The passive perfect is third feminine singular, agreeing with the nonhuman plural {{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}) and recovering it as the implicit passive subject.\",\"representative_source_ids\":[\"QG-2174cab5\",\"QG-93e2644a\",\"QF-a3ebee98\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:passive-completed-result","source_type":"word_analysis","support_id":"sup_6b8cdb862d2c1cf98821","text":"{\"blocking_evidence\":null,\"headline\":\"completed passive result\",\"reader_payoff\":\"The reader notices that the word presents an accomplished upright state while withholding the installer, so agency is inferred through the visible result.\",\"reason\":\"The local verb is a perfect passive with no expressed agent; attachment evidence marks the passive agent as unresolved and the result as the clause-final predicate.\",\"representative_source_ids\":[\"QG-0702819e\",\"QG-1a900434\",\"QT-2ee28d41\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:sequence-architecture","source_type":"word_analysis","support_id":"sup_7075a1a871e557c97fb2","text":"{\"blocking_evidence\":null,\"headline\":\"mountains mediate the survey\",\"reader_payoff\":\"The reader notices that the mountain noun is staged before the question and mediates the movement from sky-height to earth-surface in the inspection sequence.\",\"reason\":\"The ayah names the target before {{ar:كَيْفَ}} ({{tr:kayfa}}) and {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}), while the boundary rows place the noun between the sky question (88:18) and the earth question (88:20).\",\"representative_source_ids\":[\"QT-39cedfc1\",\"QE-fc30814f\",\"QY-f684c4c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:stabilizing-intertexts","source_type":"word_analysis","support_id":"sup_779675dc194e089aecb7","text":"{\"blocking_evidence\":null,\"headline\":\"pegs and anchoring contrasts\",\"reader_payoff\":\"The reader notices that the local setup question is sharpened by mountain-pegs language (78:7) and by an anchoring statement with explicit agency (79:32).\",\"reason\":\"The rows give concrete references, so the parallels survive as contrastive apparatus without controlling the local parse.\",\"representative_source_ids\":[\"QI-30bbd6cb\",\"QI-53457d49\",\"MI-c8527075\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:19:4:1","source_type":"qac_morpheme","support_id":"sup_7e1ff9d400d0fcf4bcce","text":"{\"lemma_ar\":\"نُصِبَتْ\",\"morph_features\":\"STEM|POS:V|PERF|PASS|LEM:nuSibato|ROOT:nSb|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"88:19:4:1\",\"qac_word_ref\":\"88:19:4\",\"root_ar\":\"ن ص ب\",\"surface_ar\":\"نُصِبَتْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:19:3:1","source_type":"qac_morpheme","support_id":"sup_852c580c77526fa92e50","text":"{\"lemma_ar\":\"كَيْف\",\"morph_features\":\"STEM|POS:INTG|LEM:kayof|ROOT:kyf\",\"morpheme_role\":\"STEM\",\"pos\":\"INTG\",\"qac_ref\":\"88:19:3:1\",\"qac_word_ref\":\"88:19:3\",\"root_ar\":\"ك ي ف\",\"surface_ar\":\"كَيْفَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:1:survey-link","source_type":"word_analysis","support_id":"sup_9ba415ff3e3f452027d7","text":"{\"blocking_evidence\":null,\"headline\":\"middle link in the repeated survey\",\"reader_payoff\":\"The reader notices the ayah as a carried-over station between the sky and earth questions, with the boundary preserving grammar as well as theme.\",\"reason\":\"The repeated connective-directional opening is marked as a construction unit parallel to 88:18 and anticipating 88:20.\",\"representative_source_ids\":[\"QT-0332c9bc\",\"QE-ee98827d\",\"QB-30b20838\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:compact-fixed-sound","source_type":"word_analysis","support_id":"sup_ac4f199368cebb144faa","text":"{\"blocking_evidence\":null,\"headline\":\"compact fixed-sounding close\",\"reader_payoff\":\"The reader notices the sound contract from the broad mountain target into a compressed ending that matches fixed upright placement.\",\"reason\":\"The phonetic rows carry a specific cadence payoff tied to the semantic image of fixed emplacement.\",\"representative_source_ids\":[\"QP-335ee33d\",\"QP-dd7776a2\",\"MP-108114a9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4:pivot-architecture","source_type":"word_analysis","support_id":"sup_b3bdbdc6f2d6d88808c0","text":"{\"blocking_evidence\":null,\"headline\":\"pivot between target and result\",\"reader_payoff\":\"The reader notices the ayah's three-beat architecture: viewed target, manner pivot, passive result.\",\"reason\":\"The word is positioned between the fronted mountain target and the final passive verb, turning object-recognition into manner inquiry.\",\"representative_source_ids\":[\"QT-5dbcfff2\",\"QT-e064f37a\",\"MT-1d7f0ccb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"88:19:2:2","source_type":"qac_morpheme","support_id":"sup_bcdf4f4bf2826d33b245","text":"{\"lemma_ar\":\"جَبَل\",\"morph_features\":\"STEM|POS:N|LEM:jabal|ROOT:jbl|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"88:19:2:2\",\"qac_word_ref\":\"88:19:2\",\"root_ar\":\"ج ب ل\",\"surface_ar\":\"جِبَالِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:intertext-root-contrasts","source_type":"word_analysis","support_id":"sup_bd4d791fd094b556ae45","text":"{\"blocking_evidence\":null,\"headline\":\"anchoring and toil contrasts\",\"reader_payoff\":\"The reader notices that direct anchoring language elsewhere (79:32) and toil language within the surah (88:3) sharpen this passive emplacement in 88:19.\",\"reason\":\"The rows provide concrete references, so they survive as contrasts: direct agency in 79:32 and root-family toil pressure in 88:3 clarify what the passive setup question does here.\",\"representative_source_ids\":[\"QI-deafe2b4\",\"MI-0657ec26\",\"QE-8035eaa9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:1","source_type":"word_analysis","support_id":"sup_c23f57768f8f2c421c4f","text":"{\"gloss_range\":\"coordinating continuation in the repeated observation chain; locally additive rather than a loose restart or chronology marker\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) opens the ayah as continuation before any mountain or predicate is heard. Its payoff is not mere addition: it carries the mountain phrase back into the already active looking sequence from 88:17 and keeps 88:19 from becoming an isolated proof. The ayah boundary therefore carries grammar, not only theme; the phrase is still dependent on the earlier inspection frame. The particle remains analytically distinct from {{ar:إِلَى}} ({{tr:ilā}}), so continuation and direction arrive together in sound without being collapsed into one compound. The repeated onset across the neighboring inspection stations (88:18; 88:20) makes this ayah a middle link in a cumulative visual survey from sky toward earth, not a chronological or causal step.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:formed-mass-pressure","source_type":"word_analysis","support_id":"sup_c2f703ef6e385dde1d55","text":"{\"blocking_evidence\":null,\"headline\":\"formed mass, not abstract height\",\"reader_payoff\":\"The reader notices the mountains as formed, weighty masses whose constitution makes the question of emplacement concrete.\",\"reason\":\"V4 supports the mountain and formed-constitution branches of {{ar:ج ب ل}} ({{tr:j-b-l}}), but local grammar selects the concrete plural mountain noun and does not activate unrelated abundance, body-thickness, or entering-mountains branches.\",\"representative_source_ids\":[\"QS-08092fc9\",\"QS-8c19a53e\",\"MS-b1926841\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4:configuration-not-yes-no","source_type":"word_analysis","support_id":"sup_c92ec1041d87e8c90bcc","text":"{\"blocking_evidence\":null,\"headline\":\"visible result is presumed\",\"reader_payoff\":\"The reader notices that the question form turns visible mountains into evidence demanding recognition rather than asking for missing information.\",\"reason\":\"The interrogative asks for mode, state, or configuration over an already visible passive result; the bundle gives no yes-no particle in this position.\",\"representative_source_ids\":[\"QS-8375b609\",\"QS-bde9260f\",\"QI-aef29fa1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5:variant-agency-contrast","source_type":"word_analysis","support_id":"sup_d3d03c70255eed518eea","text":"{\"blocking_evidence\":null,\"headline\":\"variant exposes agency contrast\",\"reader_payoff\":\"The reader notices how the canonical passive makes arrangement argue indirectly, while the variant contrast shows the agent-pressure that could be made explicit.\",\"reason\":\"{{ar:نَصَبْتُ}} ({{tr:naṣabtu}}) is useful as variant contrast, but it does not replace the aligned canonical passive {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}) in the local parse.\",\"representative_source_ids\":[\"QG-f7012191\",\"QS-399aa63d\",\"QY-3f7d60a1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:4:manner-over-passive","source_type":"word_analysis","support_id":"sup_d740f3fc4690996ad681","text":"{\"blocking_evidence\":null,\"headline\":\"manner question over the passive\",\"reader_payoff\":\"The reader notices that the ayah asks how the mountains are configured, not whether they exist or what kind of mountains they are.\",\"reason\":\"Attachment evidence marks {{ar:كَيْفَ}} ({{tr:kayfa}}) as an adverbial dependent of {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}), not as a modifier of the noun.\",\"representative_source_ids\":[\"QG-29fa6c70\",\"QG-631ae76a\",\"MG-7ffbfaf3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:5","source_type":"word_analysis","support_id":"sup_db73be2e54d137ad6daf","text":"{\"gloss_range\":\"completed passive setting-up or emplacement of the mountains as an externally arranged result; the installer is withheld, and broader toil, share, marker, hostility, song, or travel branches are not selected locally except as contrastive pressure\",\"prose\":\"{{ar:نُصِبَتْ}} ({{tr:nuṣibat}}) closes the ayah on a completed passive result: the mountains stand as set up, while the installer is not named. The perfect aspect makes the arrangement already there for inspection, and the feminine singular ending visibly locks the final verb back to {{ar:ٱلْجِبَالِ}} ({{tr:al-jibāli}}), gathering many masses as one nonhuman plural collective. The root image of {{ar:ن ص ب}} ({{tr:n-ṣ-b}}) makes the standing feel like upright emplacement, fixed into visible order rather than mere height; marker, appointment, and toil branches sharpen the image only as contrast, because the local passive selects cosmic installation rather than cultic markers, human labor, shares, or hostility. That selection also stands out distributionally: this rare passive-result use focuses the root on emplacement inside a family often represented by nominal share or portion forms. The variant {{ar:نَصَبْتُ}} ({{tr:naṣabtu}}) exposes what the base form withholds: an explicit speaker-agent, so the canonical passive lets visible arrangement argue before agency is named. Within the surah, {{ar:نَّاصِبَةٌ}} ({{tr:nāṣibah}}) burdens faces in 88:3 while this word fixes mountains in 88:19; nearby, {{ar:رُفِعَتْ}} ({{tr:rufiʿat}}) in 88:18, {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}) here, and {{ar:سُطِحَتْ}} ({{tr:suṭiḥat}}) in 88:20 form a passive-result series from raised sky to installed mountains to spread earth. Its compact nu-ṣi-bat close, with emphatic ṣ and stop consonants, audibly contracts the broad mountain target into a fixed result.\",\"root_display\":\"{{ar:ن ص ب}} ({{tr:n-ṣ-b}})\",\"root_gloss_range\":\"root range includes setting something upright and prominent, erected worship or boundary markers, weariness and strain, assigned share, fixed base or origin, grammatical accusative setting, hostile opposition, song mode, and a day-long march; local grammar selects passive upright emplacement\",\"surface_display\":\"{{ar:نُصِبَتْ}} ({{tr:nuṣibat}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:2:repeated-attention-operator","source_type":"word_analysis","support_id":"sup_f01ecebca715dd48461e","text":"{\"blocking_evidence\":null,\"headline\":\"repeated operator in the chain\",\"reader_payoff\":\"The reader notices the same prepositional grammar moving from one created domain to the next, keeping the survey cumulative.\",\"reason\":\"The bundle marks the repeated construction as a context-window feature and a parallel to adjacent inspection clauses.\",\"representative_source_ids\":[\"QE-992f1db4\",\"QB-810f88b4\",\"QB-bfd74efd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:2:attentional-target","source_type":"word_analysis","support_id":"sup_f0cb39ac974d0aec31cd","text":"{\"blocking_evidence\":null,\"headline\":\"direction of attention\",\"reader_payoff\":\"The reader notices that the mountains are made an object of directed inspection, while the preposition does not describe their being set up.\",\"reason\":\"Attachment evidence recovers the governing observation verb from 88:17, so the directional range of {{ar:إِلَى}} ({{tr:ilā}}) is narrowed to attentional orientation rather than physical movement or verbal government by {{ar:نُصِبَتْ}} ({{tr:nuṣibat}}).\",\"representative_source_ids\":[\"QG-ca39bb20\",\"QG-cf8c194b\",\"QS-4d8f3d0a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:2:target-before-manner","source_type":"word_analysis","support_id":"sup_f68cd6dfc907c88f631c","text":"{\"blocking_evidence\":null,\"headline\":\"target precedes the question\",\"reader_payoff\":\"The reader notices the staging: attention first lands on the visible object, then the manner question begins.\",\"reason\":\"The fronted prepositional phrase precedes {{ar:كَيْفَ}} ({{tr:kayfa}}), so the visible target is presented before the mode of arrangement is queried.\",\"representative_source_ids\":[\"QT-39311501\",\"MT-64c1e343\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"88:19:3:acoustic-weight","source_type":"word_analysis","support_id":"sup_faf97018b6065ab91be6","text":"{\"blocking_evidence\":null,\"headline\":\"broad target cadence\",\"reader_payoff\":\"The reader notices the noun's breadth before the clause tightens into the short manner and passive-result ending.\",\"reason\":\"The cadence rows add a distinct sound-shape payoff that matches the mass-and-result staging rather than merely decorating it.\",\"representative_source_ids\":[\"QP-383b0db3\",\"QP-f6336837\",\"MP-7a194a0e\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000217/B001","root_001507/B001","root_001507/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000217","role":"The high solid mass supplies the stable body that can dominate a terrain.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Upright prominent setting supplies the visible operation performed on that mass.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]},{"branch_id":"B003","mapped_root_id":"root_001507","role":"The upright boundary-marker image turns mere height into orientation and demarcation.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"changed_reading":{"after":"An invitation to inspect mountains as deliberately erected, conspicuous markers that structure and orient terrain.","before":"A generic invitation to notice mountains as large created objects."},"confidence":"strong","focus_anchor":"The plural mountain mass at word 2 is joined to a passive setting operation at word 4.","mechanism":"A high solid mass is fixed upright and made conspicuous; the marker branch of the same setting root gives that prominence an orienting and boundary-making function.","model_id":"b_landmark_erection"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_landmark_erection","source_type":"hft","support_id":"sup_2be521c5a9464c806ebb","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000217/B002","root_001507/B005","root_001507/B006"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000217","role":"Mountain-like abundance supplies a plurality large enough to be distributed and measured.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]},{"branch_id":"B005","mapped_root_id":"root_001507","role":"The assigned-share image recasts setting as allotting each mass its portion.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]},{"branch_id":"B006","mapped_root_id":"root_001507","role":"The fixed base and quantitative threshold supply stable measure to the allotment.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"changed_reading":{"after":"The mountains were assigned fixed standings and measures that calibrate the world's distribution.","before":"The mountains were placed at unspecified locations."},"confidence":"exploratory","focus_anchor":"The passive form at word 4 can activate the allotted-share and fixed-threshold branches of ن ص ب while remaining attached to the mountain plurality.","mechanism":"The mountains become apportioned masses: each is given a fixed standing, base, or measure within an ordered world rather than merely lifted into place.","model_id":"b_fixed_measure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_fixed_measure","source_type":"hft","support_id":"sup_efb84234ab2b0b50832c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000217/B003","root_001507/B001","root_001507/B004"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000217","role":"Thick bodily build, including the hump image, supplies an anatomical profile for the mountain.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Upright setting supplies bodily posture to the thick mass.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]},{"branch_id":"B004","mapped_root_id":"root_001507","role":"Fatigue and wearing strain make the maintained posture feel load-bearing.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"changed_reading":{"after":"Mountains are thick world-bodies made to stand and bear strain in their posture.","before":"Mountains are inert geology that happens to stand high."},"confidence":"exploratory","focus_anchor":"The mountain root can name thick bodily build, while the setting root can name both upright posture and exhausting strain.","mechanism":"The verse can momentarily animate mountains as thick bodies or humps made to stand, with their stable posture holding latent effort rather than inert mass alone.","model_id":"b_embodied_posture"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_embodied_posture","source_type":"hft","support_id":"sup_b7f19790cde1af2162cd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000217/B007","root_001507/B001"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_000217","role":"The firm weave image supplies a tightly made material field for the mountain.","root":"ج ب ل","source_ref":"88:19","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"The upright projecting fixture supplies a reinforcement point in that field.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"changed_reading":{"after":"The verse also permits mountains as upright reinforcements in a firmly made world-fabric.","before":"The verse asks only how separate rocky objects were raised."},"confidence":"exploratory","focus_anchor":"A textile-construction branch of ج ب ل at word 2 can combine with the upright-fixture branch of ن ص ب at word 4.","mechanism":"Firm weaving supplies a world-fabric, while upright installation supplies the stiff points that hold its form; mountains become structural reinforcements rather than only rock masses.","model_id":"b_woven_fixture"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_woven_fixture","source_type":"hft","support_id":"sup_1d2bde21ee5faa7dff30","trust":"legacy_unbound"}]}
</lane_packet_json>
