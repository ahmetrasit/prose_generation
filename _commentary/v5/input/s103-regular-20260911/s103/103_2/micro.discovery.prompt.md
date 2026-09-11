# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **103:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s103-regular-20260911/s103/103_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "103:2",
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
{"analysis_context":{"analysis_id":"s103-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"103:2","host_surah":103,"lane_context_refs":[],"ordered_context_refs":["103:0","103:1","103:3","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B001","candidate_links":[{"candidate_id":"cand_9f9d9d1a9b464576a7c7","lane":"micro"},{"candidate_id":"cand_752bff4320c50f5d2433","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"insan türü ve bu türden bir kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsanları bir tür veya topluluk olarak anlatırken de bu türün tek bir üyesini belirtirken de kullanılabilir.","boundary_detail":"Dal, insan türünü ve onun tekil ya da toplu üyelerini kapsar; yakınlık duygusunu, duyusal algıyı ve insana dönük yanı kapsamaz.","branch_image_ar":"ظهور الإنسان المخالف للتوحش والجن","concept_gloss":"insan türü ve bu türden bir kişi","contextual_glosses":[{"applicability":"Türün üyeleri topluca veya görünmeyen varlıklar sınıfının karşıtı olarak anıldığında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan türünün toplu olarak adlandırılmasını açık ve doğal biçimde korur."},"facet_ids":["F001"],"text":"insanlar","usage_role":"general"},{"applicability":"Bağlam türün tek bir üyesini veya herhangi bir kimseyi gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan topluluğundan tek bir üyenin belirtilmesini korur."},"facet_ids":["F001"],"text":"bir kişi","usage_role":"contextual"}],"definition":"Görünmeyen varlıklar sınıfının karşısında yer alan insan türünü, bu türün topluluğunu ya da tek bir üyesini belirtir. İnsanların görünür oluşu, bu adlandırma için aktarılan bir gerekçedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan türünü, insanların oluşturduğu topluluğu veya bu türün tek bir üyesini görünmeyen varlıklar sınıfının karşısında adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Adlandırmanın insanların duyularla görünür oluşuna bağlanması, anlamın özü değil kökene ilişkin bir açıklamadır."}],"identity_rationale":"Kaynak ifadesi, görünmeyen varlıklar sınıfının karşısındaki insan türünü, bu türün topluluğunu ve tek bir üyesini birlikte gösterir. Görünür olma açıklaması adlandırma gerekçesidir; insan olmanın kurucu tanımı değildir. Evde kimsenin bulunmadığını bildiren kalıp ise dal çekirdeğine genellenemez ve yalnızca kendi sözcüksel biriminde korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanlar; insan topluluğu"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"insan; insan türü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"insan topluluğunun bir üyesi; insana veya insanlara ait"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"insanlar; insan toplulukları"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"insanlar; halk"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"belirli bir ağızda insan ve onun çoğulu"}],"lexicalization_note":"Çıplak biçimlerdeki insan ve insan topluluğu anlamı dal çekirdeğidir; evde hiç kimse bulunmadığını anlatan kalıp ayrı tutulur ve çekirdeğe yeni bir genel anlam katmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Yalnız insanı adlandırma sınırını yaratılmışlar kapsamından ve yakınlık duygusundan ayıran, okuyucu için en yararlı üç karşıtlık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yer değiştirme yalnız insanı genel olarak adlandıran bağlamlarda mümkündür. Odak dalın görünmeyen varlıklarla sınıf karşıtlığı, komşunun ise görünür beden yönü kendi sınırında kalır.","focus_only":"Odak dal, insanları görünmeyen varlıklar sınıfının karşısında bir tür olarak kurar ve görünürlüğe dayalı bir adlandırma açıklaması taşır.","gloss":"insan türünü iki ayrı yönden adlandırma","neighbor_only":"Komşu dal, insanı görünür ten ve yaratılmış beden yönüyle adlandırır; tekil, çoğul, erkek ve kadın kapsamını özellikle öne çıkarır.","neighbor_ref":"root_000120/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da insanı hem tür hem bu türün üyesi olarak gösterebilir."},{"boundary_match":"partial","distinction":"Komşunun genel yaratılmışlar kapsamı odak dala taşınamaz; odak dal da yalnız insanları belirttiği için bütün yaratılmışların yerine kullanılamaz.","focus_only":"Odak dal yalnız insan türünü ve bu türün tekil ya da toplu üyelerini belirtir.","gloss":"insan türü ile bütün yaratılmışlar ayrımı","neighbor_only":"Komşu dal yeryüzündeki bütün yaratılmışları kapsayabilir ve bazı yorumlarda insanlarla görünmeyen varlıkları birlikte içerir.","neighbor_ref":"root_000061/B001","relation_type":"near_neighbor","shared_zone":"İnsanlar iki dalın gönderim alanında da bulunabilir."},{"boundary_match":"field_only","distinction":"Birinde insanın kim olduğu adlandırılır, diğerinde bir kişi ya da şey karşısındaki duygusal durum anlatılır; sıradan bağlamlarda birbirlerinin yerine geçmezler.","focus_only":"Odak dal insan türünü ve bu türün üyelerini adlandırır.","gloss":"insan adı ile yakınlık duygusu ayrımı","neighbor_only":"Komşu dal yabancılık ve ürkme duygusunun kalkmasını, yakınlık ve rahatlık oluşmasını anlatır.","neighbor_ref":"root_000059/B003","relation_type":"same_field","shared_zone":"Her iki dalda da insan, temel gönderim noktası veya deneyim sahibi olabilir."}],"source_phrase_ar":"الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)","source_summary":"Aktarımlar, dalın insan türünü hem topluluk hem tek kişi olarak gösterebildiğinde ve görünmeyen varlıklar sınıfıyla karşıtlık kurduğunda birleşir. Görünürlük, ortak anlamdan çok adlandırmanın gerekçesi olarak sunulur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الإنس والبشر والناس والأناسي والإنسان من حيث الجماعة أو الواحد، وما بالدار أنيس بمعنى أحد.","what_is_not_ar":"لا يدخل مجرد الاستئناس النفسي ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":["sup_329b406a8e841fffa9c2","sup_fb369d0ac1a3794876b1"]},{"boundary":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B002","candidate_links":[{"candidate_id":"cand_5b8551b50da8179c61e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görme çekirdeğiyle birlikte yalnız belirtilen bağlamlarda ortaya çıkan işitme, sezme ve çevreyi araştırma uzantılarını topluca verir.","boundary_detail":"Dal duyusal olarak fark etmeyi ve belirtilen bağlamlardaki işitme, sezme ve bakıp araştırma kullanımlarını kapsar; yakınlık ve rahatlık duygusunu kapsamaz.","branch_image_ar":"إيناس الشيء برؤية أو إحساس أو سماع","concept_gloss":"görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma","contextual_glosses":[{"applicability":"Nesnenin gözle seçildiği veya görüldüğü temel kullanımda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözle görme ve görüleni fark etme işlemlerini birlikte korur."},"facet_ids":["F001"],"text":"görüp fark etmek","usage_role":"general"},{"applicability":"Nesne açıkça bir ses olduğunda kullanılan bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sesin kulakla algılanması biçimindeki özel kullanımı korur."},"facet_ids":["F002"],"text":"sesi işitmek","usage_role":"contextual"},{"applicability":"Bir kimsedeki olgunluk veya kaygı uyandıran durum gibi bir belirtinin ayırt edildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duyusal belirtiden bir durumun varlığını anlayıp ayırt etmeyi korur."},"facet_ids":["F003"],"text":"belirtiyi sezmek","usage_role":"contextual"},{"applicability":"Çevreyi gözleyip birinin bulunup bulunmadığını anlamaya çalışma kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikkatle bakma ile birini bulmaya yönelik araştırmayı birlikte korur."},"facet_ids":["F004"],"text":"bakıp araştırmak","usage_role":"explanatory"}],"definition":"Bir şeyi görüp fark etmeyi anlatır. Belirli kullanımlarda bir sesi işitmeye, bir kimsedeki olgunluk belirtisini ya da kaygı veren bir durumu sezmeye ve çevreye bakarak birinin bulunup bulunmadığını araştırmaya uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi gözle görerek fark etmeyi veya seçmeyi anlatır."},{"facet_id":"F002","role":"extension","statement":"Belirli bir ses nesnesiyle kullanıldığında o sesi işitmeyi anlatır."},{"facet_id":"F003","role":"extension","statement":"Bir kimsedeki olgunluk belirtisini bilip ayırt etmeyi veya kaygı veren bir durumu duyularla sezmeyi anlatabilir."},{"facet_id":"F004","role":"associated_use","statement":"Çevreye bakıp dikkatle araştırarak birinin bulunup bulunmadığını anlamaya çalışma kullanımını taşır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Zamanla gelişen yakınlık ve yabancılığın kalkması anlamını ekler.","collision":"Yakınlık ve rahatlık bildiren ayrı dalla karışır.","fit":"displacement","loses":"Görme, işitme, belirtiyi sezme ve çevreye bakıp araştırma işlemlerini siler.","preserves":"Bir kişi veya şeye yönelen deneyim fikrini çok genel biçimde korur."},"text":"alışmak"}],"identity_rationale":"Kaynak ifadesi görmeyi temel alır, fakat belirli kullanımlarda işitmeyi, bir belirtiyi anlayıp ayırt etmeyi ve çevreye bakarak birini aramayı da aynı dalda aktarır. Bu yüzden dal genel ve sınırsız bir algı yetisi diye tanımlanamaz; her uzantı kendi bağlamına bağlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir şeyi görmek ve fark etmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sesi işitmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"onda olgunluk belirtisi görmek ve bunu anlamak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ürken yabani hayvanın birini sezip çevreye bakınması"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çevreye bakıp birinin olup olmadığını araştırmak"}],"lexicalization_note":"Görüp fark etme çekirdeği ile ses işitme, olgunluk belirtisini ayırt etme ve çevreye bakıp araştırma kalıpları ayrı tutulur; kalıplardaki kapsam çıplak biçime genellenmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Görme, genel duyumsama ve yakınlık duygusuyla karışma olasılığı en yüksek üç sınır yayımlandı; diğer adaylar dalı açıklayan ek bir karşıtlık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yalnız görsel algı bağlamında yakın karşılık olabilirler. Odak dalın işitme ve belirtiyi sezme uzantıları komşuya, komşunun göz organı anlamı da odak dala taşınamaz.","focus_only":"Odak dal, görmenin yanında belirli yapılarda işitme, belirti sezme ve çevreyi araştırma uzantılarını taşır.","gloss":"fark etme ile gözle görme ayrımı","neighbor_only":"Komşu dal göz organını, görme duyusunu ve göz açıp dikkatle bakma eylemini kendi başına kapsar.","neighbor_ref":"root_000121/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi göz yoluyla görüp seçme alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu daha genel bir duyu alanıdır; odak dalın uzantıları ise kanıtlanan nesne ve yapılara bağlıdır. Bu nedenle genel duyumsama her durumda odak ifadeyle karşılanamaz.","focus_only":"Odak dal görmeyi merkez alır ve yalnız belirli söz çevrelerinde işitme, sezme ve araştırmaya uzanır.","gloss":"belirli algı kullanımları ile genel duyumsama","neighbor_only":"Komşu dal herhangi bir duyu aracılığıyla algılama, bilme ve varlığını saptama alanını genel olarak kapsar.","neighbor_ref":"root_000321/B002","relation_type":"near_synonym","shared_zone":"Her ikisi de bir şeyin duyular aracılığıyla fark edilmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal algısal saptamayı, komşu dal ise karşılaşma sonrasındaki duygusal rahatlığı bildirir. Algı gerçekleşebilir ama yakınlık doğmayabilir.","focus_only":"Odak dal bir nesneyi görme, işitme veya belirtilerinden sezme eylemini anlatır.","gloss":"duyusal fark etme ile yakınlık hissetme","neighbor_only":"Komşu dal bir kişi ya da şey karşısında yabancılık ve ürkme duymayıp yakınlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Bir kişi veya şeyle karşılaşma iki anlam alanının ortak başlangıç durumu olabilir."}],"source_phrase_ar":"آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)","source_summary":"Aktarılan anlam alanının merkezi görüp fark etmektir. Aynı ifade ailesi belirli nesne ve yapılarda işitme, bir belirtiyi anlayıp ayırt etme, kaygı veren şeyi sezme ve bakıp araştırma yönlerinde kullanılır; bunlar sınırsız bir genel algı anlamı oluşturmaz.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه آنس الشيء إذا أبصره أو رآه، وآنس الصوت إذا سمعه، وأحس الفزع أو وجد الشيء في نفسه، والاستئناس بمعنى النظر والتبصر.","what_is_not_ar":"لا يدخل الأنس بمعنى الراحة والمؤالفة ولا الإنس بمعنى البشر إلا بقرينة."},"support_links":["sup_a61478b7b22aee44dda8"]},{"boundary":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeyin ürkütücü ve yabancı gelmemesi, tersine yakınlık ve iç rahatlığı vermesi anlatıldığında dalın çekirdeğini karşılar.","boundary_detail":"Dal duygusal yakınlık, rahatlık ve bunları sağlayan varlıkları kapsar; insan türünün adı, duyusal fark etme ve insana bakan yan anlamları dışarıda kalır.","branch_image_ar":"الأنس الذي يزيل الوحشة","concept_gloss":"yabancılık duymadan yakınlık ve rahatlık hissetme","contextual_glosses":[{"applicability":"Bir kişi veya şey karşısındaki yabancılık duygusunun kalktığı temel durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alışma sonucunda yabancılığın kalkmasını ve yakınlık oluşmasını korur."},"facet_ids":["F001"],"text":"alışıp yakınlık duymak","usage_role":"general"},{"applicability":"Yalnızlığı veya ürkmeyi gideren bir arkadaş, nesne ya da başka bir dayanak adlandırıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık ve güven veren kaynağın kişiyle sınırlı olmamasını korur."},"facet_ids":["F002"],"text":"yanında rahatlık veren kişi veya şey","usage_role":"explanatory"},{"applicability":"İnsandan kaçmayan ve ısırıp saldırmayan evcil ya da alışkın hayvan için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın insana alışıklığını ve saldırgan olmama sınırını birlikte korur."},"facet_ids":["F003"],"text":"insana alışık ve saldırgan olmayan","usage_role":"contextual"}],"definition":"Bir kişi ya da şey karşısında yabancılık, ürkme veya kaçınma duymayıp yakınlık, rahatlık ve sevinç hissetmeyi anlatır. Bu duyguyu veren kişi veya şeye ve insana alışık, saldırgan olmayan hayvana da aktarılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey karşısında yabancılık ve ürkme duygusunun kalkıp yakınlık, rahatlık veya sevinç oluşmasını anlatır."},{"facet_id":"F002","role":"extension","statement":"Kişiye arkadaşlık ederek veya yanında bulunarak yabancılık duygusunu gideren kişi ya da şeyi adlandırır."},{"facet_id":"F003","role":"specialization","statement":"İnsana alışık ve saldırgan olmayan hayvanı, özellikle bu nitelikteki köpeği anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Her türlü sevincin bu dala ait olduğu izlenimini verebilir.","fit":"narrowing","loses":"Yabancılığın ve ürkmenin kalkmasını, alışmayı ve rahatlık veren kişi ya da şey kapsamını kaybeder.","preserves":"Yakınlık durumunda ortaya çıkabilen olumlu duyguyu korur."},"text":"sevinç"}],"identity_rationale":"Kaynak ifadesi, bir kişi veya şey karşısında yabancılık ve ürkme duygusunun kalkmasını çekirdek anlam olarak verir. Yakınlık ve sevinç, rahatlık veren kişi ya da şey ve insana alışık saldırgan olmayan hayvan kullanımları bu çekirdekten bağımlı biçimde açıklanabilir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yakınlık ve rahatlık; yabancılık duymama"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"birine alışıp onun yanında sevinmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yakın arkadaş; rahatlık veren kişi veya şey"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yakınlıktan ve söyleşiden hoşlanan genç kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"insana alışık, saldırgan olmayan köpek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"gece yolcusuna veya konaklayana güven veren ateş"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları"}],"lexicalization_note":"Yabancılık duymama çekirdeği ile rahatlık veren kişi veya şey ve insana alışık hayvan gibi özelleşmiş biçimler ayrı katmanlarda tutulur; özel biçimler bütün dalı tanımlamaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı. Alışıp bağlanma, özel dostluk ve insan türünü adlandırma alanları dal sınırını en açık gösterdiği için yalnız bu üç ayrım yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın belirleyici yönü yabancılık ve ürkmenin karşıtı olan iç rahatlığıdır; komşu dal süreklilik, bağlanma ve alışkanlık yönlerini odaktan daha geniş taşır.","focus_only":"Odak dal yabancılık ve ürkmenin kalkmasıyla oluşan yakınlık ve rahatlığı, ayrıca bunu sağlayan varlığı öne çıkarır.","gloss":"yakınlık rahatlığı ile alışıp bağlanma","neighbor_only":"Komşu dal bir kişi, yer veya şeye alışmayı, ona bağlanmayı, onunla sürekli bulunmayı ve hayvanın evcilleşmesini daha geniş biçimde kapsar.","neighbor_ref":"root_000045/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi, yer, şey veya hayvana karşı yabancılığın azalmasını anlatabilir."},{"boundary_match":"partial","distinction":"Her rahatlık veren yakınlık özel ve arı bir dostluk değildir. Komşunun karşılıklı dostluk sınırı odak dalın nesne ve hayvan uzantılarına uygulanamaz.","focus_only":"Odak dal kişi dışındaki şeylerin verdiği rahatlığı ve insana alışık hayvanı da kapsayabilir.","gloss":"rahatlık veren yakınlık ile özel dostluk","neighbor_only":"Komşu dal seçilmiş kişiler arasındaki arı, özel ve karşılıklı dostluk bağını anlatır.","neighbor_ref":"root_000430/B007","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında yakınlık ve içtenlik bulunan durumlarda buluşur."},{"boundary_match":"field_only","distinction":"Odak dal bir duygusal ilişkiyi, komşu dal ise bir varlık sınıfını adlandırır. İnsan olmak yakınlık hissetmeyi gerektirmez ve iki ifade birbirinin yerine geçmez.","focus_only":"Odak dal yabancılığın kalkmasıyla doğan duygusal yakınlığı ve rahatlığı anlatır.","gloss":"yakınlık durumu ile insan adı ayrımı","neighbor_only":"Komşu dal insan türünü, insan topluluğunu veya bu türden tek bir kişiyi adlandırır.","neighbor_ref":"root_000059/B001","relation_type":"same_field","shared_zone":"İnsan, iki dalda da temel katılımcı veya gönderim noktasıdır."}],"source_phrase_ar":"الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)","source_summary":"Ortak çekirdek, yabancılık ve kaçınmanın karşıtı olan yakınlık ve rahatlıktır. Bu durum birine alışıp onun yanında sevinmeyi, rahatlık veren kişi veya şeyi ve insana alışık saldırgan olmayan hayvanı kapsayacak biçimde genişler.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه أنس الإنسان بالشيء أو بفلان، المؤانسة والتأنيس، الأنيس وكل ما يؤنس به، الفرح بالقرب والحديث، والحيوان الأنوس غير العقور.","what_is_not_ar":"لا يدخل الإنس بمعنى البشر ولا الإيناس بمعنى الإبصار ولا الجانب الإنسي إلا بدليل."},"support_links":[]},{"boundary":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_kind":"bare","branch_ref":"root_000059/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"insana dönük yan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin yönü, ona yaklaşan veya onu kullanan insana göre belirlendiğinde dalın ortak çekirdeğini verir.","boundary_detail":"Dal, bir nesnenin insana veya kullanıcıya bakan yanını belirtir; salt sol, salt sağ, genel ön taraf ya da insanın kendisi anlamına gelmez.","branch_image_ar":"الجانب الإنسي المقبل على الإنسان","concept_gloss":"insana dönük yan","contextual_glosses":[{"applicability":"Hayvanın binme ve sağma sırasında insana yakın kalan yanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yanını biniciyle kurduğu işlevsel ilişkiye göre belirler."},"facet_ids":["F002"],"text":"biniciye yakın yan","usage_role":"contextual"},{"applicability":"Yayın kullanım sırasında okçuya doğru dönük olan yüzü belirtilirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yay yüzünün yönünü okçunun konumuna göre belirleme özelliğini korur."},"facet_ids":["F003"],"text":"okçuya bakan yay yüzü","usage_role":"explanatory"}],"definition":"Bir nesnenin insana, kullanıcıya veya onun bulunduğu yöne bakan yanıdır. Hayvan ve yay üzerinde işlevsel ilişkiyle belirlenir; bu yanın sabit olarak sol ya da sağ sayılması konusunda aktarım uyuşmazlığı vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin insana en yakın olan veya insana doğru bakan yanını belirtir."},{"facet_id":"F002","role":"specialization","statement":"Hayvanda binicinin bulunduğu, binme ve sağma işlemlerinde insana yakın olan yanı anlatır."},{"facet_id":"F003","role":"specialization","statement":"Yayda okçuya doğru bakan ve kullanıcının karşısında bulunan yanı anlatır."},{"facet_id":"F004","role":"source_variant","statement":"İnsana yakın yan bazı aktarımda sol, başka bir aktarımda sağ diye belirlenir; yönün özü bu değişken tanımlardan bağımsızdır."}],"identity_rationale":"Kaynak ifadesinin güvenilir çekirdeği, bir şeyin insana veya onu kullanan kişiye dönük ve yakın olan yanıdır. Bu yanın solda mı sağda mı olduğu konusunda aktarımlar uyuşmaz; hayvan ve yay örnekleri yönü işlevsel ilişkiyle belirler. Bu nedenle sabit bir sağ-sol tanımı dalın özüne konamaz.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bir şeyin insana bakan veya en yakın olan yanı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yayın okçuya bakan yüzü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hayvanın biniciye yakın olan yanı"}],"lexicalization_note":"Tanım çıplak dalın insana dönük yan çekirdeğiyle sınırlıdır. Hayvan ve yay uygulamaları bu çekirdeğin örneklenmesidir; yalnız bu kullanımlardan yeni bir genel yön anlamı çıkarılmaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Genel ön taraf, yönelme eylemi ve arka bölümle kurulan karşılaştırmalar insana göre belirlenen yanın sınırını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda yön, insanın nesneyle kurduğu konum veya kullanım ilişkisine bağlıdır. Komşu dalın genel ön ve yakın anlamları bu özel bağı gerektirmez.","focus_only":"Odak dal bir nesnenin insana veya onu kullanan kişiye dönük yanını ilişkiye göre belirler.","gloss":"insana dönük yan ile genel ön taraf","neighbor_only":"Komşu dal genel olarak ön, önde, yakın veya karşıda bulunma yönlerini kişiye bağlı bir kullanım ilişkisi gerektirmeden anlatır.","neighbor_ref":"root_000053/B011","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin bakana göre karşıda veya önde kalan bölümünü gösterebilir."},{"boundary_match":"partial","distinction":"Bir nesnenin insana dönük yanı bir bölüm adıdır; komşu ise dönme veya yönelme olayını anlatır. Sonuç konumu ile o konuma geçiş eylemi birbirinin yerine kullanılamaz.","focus_only":"Odak dal, yönelme tamamlandıktan sonra insana dönük olan sabit yanı adlandırır.","gloss":"dönük yan ile yönelme eylemi","neighbor_only":"Komşu dal yüz, baş, el, kap veya hayvanın bir hedefe doğru dönmesi ve yönelmesi eylemini anlatır.","neighbor_ref":"root_001263/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi veya hedefe doğru bakma yönünü içerir."},{"boundary_match":"partial","distinction":"Bağlama göre karşıt görünebilseler de odak dal her zaman geometrik ön yüz değildir ve bu yüzden düzenli bir karşıt çift oluşturmaz; belirleyici ölçüt insana yakınlıktır.","focus_only":"Odak dal insana veya kullanıcıya yakın ve ona bakan yanı gösterir.","gloss":"insana bakan yan ile arka taraf","neighbor_only":"Komşu dal bir şeyin arkasında kalan, yüzünün karşıtı olan arka bölümünü gösterir.","neighbor_ref":"root_000458/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir nesnenin başka bir yöne göre belirlenen bölümünü adlandırır."}],"source_phrase_ar":"الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)","source_summary":"Ortak anlam, nesnenin insana veya kullanıcıya dönük yanıdır; hayvanda biniciye, yayda okçuya göre belirlenir. İnsan bedenindeki tekil uygulamada öteki bacağa bakan yan kastedilir. Bu yanın solda mı sağda mı bulunduğuna ilişkin anlatımlar ayrıştığı için genel tanım sabit bir yön seçmez.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إنسي الدابة والقوس وكل شيئين: ما يلي الإنسان أو يقبل على الراكب أو الرامي، في مقابلة الوحشي.","what_is_not_ar":"لا يدخل الإنسان نفسه ولا الأنس النفسي ولا الإبصار."},"support_links":[]},{"boundary":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_kind":"bare","branch_ref":"root_000059/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"göz bebeğinde görülen küçük yansıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakanın göz bebeğinde beliren küçük insan biçimli görüntü adlandırıldığında dalın ortak ve temel anlamını karşılar.","boundary_detail":"Dal göz bebeğinde görülen küçük görüntüyü, ayrıca ayrı bir aktarım olarak parmak ucunu kapsar; gözün kendisini veya genel insan türünü belirtmez.","branch_image_ar":"إنسان العين وصورة الإنسان في السواد","concept_gloss":"göz bebeğinde görülen küçük yansıma","contextual_glosses":[{"applicability":"Yansımanın insan biçiminde algılanması özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüntünün göz bebeğinde bulunmasını ve küçük insan biçiminde görünmesini korur."},"facet_ids":["F001"],"text":"göz bebeğindeki küçük insan görüntüsü","usage_role":"explanatory"},{"applicability":"Yalnız parmak ucunu aynı adla veren ayrı kaynak kullanımında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göz anlamından bağımsız olan parmak ucu kullanımını doğrudan korur."},"facet_ids":["F002"],"text":"parmak ucu","usage_role":"contextual"}],"definition":"Gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Ayrı bir kaynak kullanımında aynı ad parmak ucuna da verilir, ancak bu kullanım göz görüntüsü çekirdeğini değiştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göz bebeğinin kara bölümünde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı bir aktarımda parmak ucu veya eldeki parmak ucunu anlatan kullanım da aynı adla verilir."}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği, gözün kara bölümünde görülen küçük insan biçimli görüntü veya yansımadır. Parmak ucu anlamı tek aktarım içinde eklenir ve gözdeki görüntünün kurucu parçası değildir; bağımlı bir kaynak varyantı olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"göz bebeğinde görülen küçük görüntü veya yansıma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"göz bebeklerinde görülen küçük görüntüler"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"parmak ucu; eldeki parmak ucunu anlatan kullanım"}],"lexicalization_note":"Çıplak dalın çekirdeği gözün kara bölümündeki küçük görüntüdür. Parmak ucu aktarımı bağımlı bir varyanttır; gözle ilgili belirli biçimlerden genel görüntü veya genel insan anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi. Anatomik göz bebeği, genel tasvir ve göz organı karşılaştırmaları görüntünün yerini ve türünü en iyi sınırladığı için bu üçü yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komşu anatomik bölümün kendisidir; odak dal ise o bölümde görülen görüntüdür. Taşıyıcı yapı ile üzerinde beliren yansıma birbirinin yerine kullanılamaz.","focus_only":"Odak dal göz bebeğinde görülen küçük insan biçimli görüntüyü veya yansımayı adlandırır.","gloss":"göz bebeği ile göz bebeğindeki yansıma","neighbor_only":"Komşu dal göz bebeğinin kendisini, onun kara bölümünü ve anatomik yapısını adlandırır.","neighbor_ref":"root_000300/B002","relation_type":"same_field","shared_zone":"İki dal aynı göz bölgesine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak görüntü göz bebeğindeki belirli yansımadır; komşu ise konum ve oluşum biçimi bakımından çok daha genel tasvirleri kapsar. Her tasvir gözdeki yansıma değildir.","focus_only":"Odak dal yalnız göz bebeğinde beliren küçük insan biçimli görüntüyü ve ayrı bir parmak ucu varyantını kapsar.","gloss":"gözdeki yansıma ile genel tasvir","neighbor_only":"Komşu dal resim, model, heykel veya başka bir varlığa göre biçimlendirilmiş genel örnekleri kapsar.","neighbor_ref":"root_001397/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal başka bir varlığın görünüşünü taşıyan bir görüntüyü anlatabilir."},{"boundary_match":"field_only","distinction":"Göz, görmeyi sağlayan organdır; odak dal ise gözde görülen yansımadır. Organın adı yansımanın, yansımanın adı da organın genel karşılığı değildir.","focus_only":"Odak dal gören gözün içinde beliren küçük görüntüyü adlandırır.","gloss":"göz organı ile içindeki küçük görüntü","neighbor_only":"Komşu dal görme organı olan gözün kendisini ve onun görme işlevini adlandırır.","neighbor_ref":"root_001069/B001","relation_type":"same_field","shared_zone":"Her iki dal göz ve görme alanına aittir."}],"source_phrase_ar":"إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)","source_summary":"Ortak aktarım, göz bebeğinin kara bölümünde görülen küçük görüntüyü bir insan biçimi olarak tanımlar. Buna ek olarak parmak ucu anlamı da bildirilir, fakat bu ek kullanım gözdeki yansıma çekirdeğinden ayrı tutulur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه إنسان العين: المثال أو الصبي الذي يرى في سواد العين، وما ألحقه تهذيب اللغة من الأنملة أو إنسان الكف.","what_is_not_ar":"لا يدخل الإنسان بمعنى البشر عموما ولا الأنس بمعنى الراحة."},"support_links":[]},{"boundary":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000059/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kaynakta gösterilen soru ve kişi bağlantısı kuruluşlarını topluca açıklarken kullanılabilir; genel bir kişi ya da akraba adı değildir.","boundary_detail":"Dal yalnız belirtilen söz kuruluşlarında kişinin kendisini veya seçkin yakınını gösterir; genel insan, gerçek evlatlık ve her türlü arkadaşlık anlamına genişletilemez.","branch_image_ar":"ابن الإنس للنفس والصفوة","concept_gloss":"belirli sözlerde kişinin kendisi veya seçilmiş yakını","contextual_glosses":[{"applicability":"Muhataba kendi durumunun nasıl olduğu sorulduğunda doğal Türkçe karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorunun muhatabın kendi durumuna yönelmesini korur."},"facet_ids":["F001"],"text":"kendin; nasılsın","usage_role":"contextual"},{"applicability":"Bir kişinin seçip özel tuttuğu yakın arkadaş veya sırdaş anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakın kişinin seçilmiş, özel ve güvenilen biri olmasını korur."},"facet_ids":["F002"],"text":"onun en yakını ve sırdaşı","usage_role":"contextual"},{"applicability":"Yakın dost, içten arkadaş ve birlikte oturup konuşulan kişi için sıralanan paralel adları açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakınlık, dostluk ve sürekli görüşme ilişkilerini birlikte korur."},"facet_ids":["F003"],"text":"yakın dostum ve görüşme arkadaşım","usage_role":"explanatory"}],"definition":"Belirli bir soru kuruluşunda muhatabın kendisini ve durumunu, başka bir kişiyle kurulan adlandırmada ise onun seçilmiş yakınını, sırdaşını veya sürekli görüştüğü arkadaşını belirtir. İki kullanım aynı kuruluş ailesinde bulunsa da katılımcı ilişkileri ayrıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişiye kendi durumunu soran belirli kuruluşta muhatabın kendisini gösterir."},{"facet_id":"F002","role":"core","statement":"Bir kişiye bağlanarak söylendiğinde onun seçilmiş yakınını, özel arkadaşını veya sırdaşını belirtir."},{"facet_id":"F003","role":"associated_use","statement":"Aynı anlam çevresindeki paralel adlar yakın dostu, içten arkadaşı ve oturup konuşulan kişiyi gösterebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gerçek bir baba ile erkek çocuk arasındaki soy ilişkisini ekler.","collision":"Sözün amaçlanan kişi ilişkisini gerçek akrabalıkla karıştırır.","fit":"displacement","loses":"Kişinin kendisini veya seçilmiş yakınını gösteren kalıplaşmış gönderimi kaybeder.","preserves":"Kuruluşun yüzeyindeki çocuk ve soy ilişkisi çağrışımını korur."},"text":"oğlu"}],"identity_rationale":"Kaynak ifadesi iki ayrı kalıplaşmış ilişkiyi açıkça ayırır: kişiye kendi durumunu soran sözde kişinin kendisi, bir başkasına bağlanan sözde ise seçilmiş yakın ve sırdaş kastedilir. Yakın arkadaş ve oturup konuşulan kişi için verilen paralel adlar ikinci alanı destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kendin; kendi durumun nasıl"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"onun seçkin yakını ve sırdaşı"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"yakınım, içten dostum ve görüşme arkadaşım"}],"lexicalization_note":"Kişinin kendisini soran kuruluş, seçilmiş yakını belirten kuruluş ve yakın arkadaş adları ayrı tutulur. Bunların hiçbiri çıplak biçime genel kişi veya akrabalık anlamı olarak taşınmaz.","neighbor_coverage_note":"Aday kartların tamamı incelendi. Kişinin kendisini gösteren başka kuruluş, iç çevre ve genel dostluk alanları iki ayrı gönderimi en iyi sınırlandırdığı için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak gönderim yalnız benlik anlamındadır; kuruluşlar değiştirilemez. Odak dalın seçilmiş yakın ve sırdaş anlamı komşuda bulunmaz.","focus_only":"Odak dal kişinin kendisini belirli bir soru kuruluşunda gösterir ve ayrıca seçilmiş yakın anlamını da taşır.","gloss":"kişinin kendisini gösteren iki ayrı söz","neighbor_only":"Komşu dal şiirsel bir söyleyişte yalnız kişinin kendi benliğini başka bir kalıpla belirtir.","neighbor_ref":"root_001271/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli bir söz kuruluşunda kişinin kendisine gönderimde bulunur."},{"boundary_match":"partial","distinction":"Odak dal çoğunlukla tek bir yakın veya sırdaşı gösterir; komşu kişinin iç çevresini ve işlerine alınan özel kişileri daha geniş kapsar.","focus_only":"Odak dal seçilmiş yakını ve sırdaşı gösterebilir, fakat kişinin kendisini soran ayrı bir kullanım da içerir.","gloss":"seçilmiş yakın ile iç çevre","neighbor_only":"Komşu dal bir kişinin işine ve sırrına alınan bütün iç çevreyi ve özel kişileri topluluk olarak kapsayabilir.","neighbor_ref":"root_000128/B004","relation_type":"near_neighbor","shared_zone":"Güvenilen ve özel tutulan kişi iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Her dost odak daldaki özel adlandırmanın taşıdığı seçilmiş yakın değildir; odak dalın kişinin kendisine gönderimi de genel dostluk alanının dışındadır.","focus_only":"Odak dal özel kuruluşlarla kişinin kendisini ya da seçilmiş yakınını belirtir.","gloss":"seçilmiş sırdaş ile genel dostluk","neighbor_only":"Komşu dal arkadaşlık ve dostluk ilişkisini açık ya da gizli yönleriyle genel olarak anlatır.","neighbor_ref":"root_000397/B001","relation_type":"near_neighbor","shared_zone":"Seçilmiş yakın kişi aynı zamanda dost veya arkadaş olabilir."}],"source_phrase_ar":"كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)","source_summary":"Aktarımlar, doğrudan hitapta kişinin kendi durumunu soran kullanım ile birinin seçkin yakını ve sırdaşını gösteren kullanımı birlikte verir. Yakın dost ve sürekli görüşülen arkadaş anlamındaki paralel adlar ikinci ilişki alanını genişletir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه كيف ابن إنسك للسؤال عن النفس، وفلان ابن أنس فلان لصفيه وخاصته، وما قاربه من الخدن والأنيس والخلص والجليس.","what_is_not_ar":"لا يدخل مطلق الإنسان ولا مطلق المؤانسة إلا إذا جاء بصيغة هذا الباب أو قرينته."},"support_links":[]},{"boundary":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000059/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","surface_ar":"إِنسَٰنَ"}],"gloss":"girişten önce izin ve kabul arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}}],"root_ar":"ء ن س","root_id":"root_000059","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir eve girmeden önce selam, izin sorusu veya içeridekilerin kabulünü yoklama yoluyla girişe onay arandığında kullanılır.","boundary_detail":"Dal eve girmeden önce izin ve kabul arama durumuyla sınırlıdır; genel görme, genel yakınlık, eve yerleşme veya barınma anlamına gelmez.","branch_image_ar":"الاستئناس قبل دخول البيوت","concept_gloss":"girişten önce izin ve kabul arama","contextual_glosses":[{"applicability":"Giriş izninin selam ve açık bir izin sorusuyla istendiğini belirten açıklamada uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Selam verme, izin sorma ve girişten önce bekleme işlemlerini korur."},"facet_ids":["F001"],"text":"selam verip girebilir miyim diye sormak","usage_role":"explanatory"},{"applicability":"İçeridekilerin yakınlık ve kabul gösterdiğini anlayarak girişe elverişli ortam bulma yorumunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Girişten önce kabul ve yakınlık işareti bulma yönünü korur."},"facet_ids":["F002"],"text":"girişe açık bir karşılama bulmak","usage_role":"contextual"}],"definition":"Bir eve girmeden önce selam vererek izin istemeyi ve içeridekilerin girişe açık olduğunu anlamayı anlatır. Aktarımın bir yönü doğrudan izin sorusunu, diğer yönü girişe elverişli bir kabul ve yakınlık bulmayı öne çıkarır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eve girmeden önce selam verip girmek için izin istemeyi ve kabul beklemeyi anlatır."},{"facet_id":"F002","role":"source_variant","statement":"Ayrı açıklama, girişten önce içeridekilerden yakınlık ve kabul işareti bulmayı öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Yalnız gözle inceleme ve bir şeyi görme anlamını ekler.","collision":"Duyusal fark etme ve çevreye bakıp araştırma dalıyla karışır.","fit":"displacement","loses":"Selam verme, izin isteme ve içeridekilerin kabulünü bekleme koşullarını kaybeder.","preserves":"Girişten önce çevreyi yoklama düşüncesine sınırlı ölçüde yaklaşır."},"text":"bakıp görmek"}],"identity_rationale":"Kaynak ifadesi yalnız eve giriş öncesindeki belirli söz çevresinde açıklanır. Bir aktarım bunu selam verip izin isteme ve girebilir miyim diye sorma olarak, diğeri ise girişe elverişli bir kabul ve yakınlık bulma olarak yorumlar. Dal bu iki açıklamayı korumalı, fakat çıplak biçime genel bakma veya genel rahatlık anlamı yüklememelidir.","lexicalization_note":"Mekanik kapsam çözümlenmemiştir ve eldeki kanıt yalnız giriş öncesi kuruluşu gösterir. Bu nedenle tanım bu söz çevresine bağlanır, çıplak bir genel anlam varsayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Genel yakınlık, çevreyi gözleme ve barınma senaryosu giriş öncesi izin sınırını en iyi açıkladığı için bu üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir giriş davranışı ve onay koşuludur; komşu dal yer ve zamanla sınırlı olmayan duygusal durumdur. Genel yakınlık, giriş izninin yerine geçmez.","focus_only":"Odak dal eve girişten önce selam, izin sorusu ve kabul bekleme yoluyla yürütülen sınırlı bir davranışı anlatır.","gloss":"giriş kabulü ile genel yakınlık duygusu","neighbor_only":"Komşu dal kişi veya şey karşısında genel olarak yabancılık ve ürkme duymayıp yakınlık ve rahatlık hissetmeyi anlatır.","neighbor_ref":"root_000059/B003","relation_type":"near_neighbor","shared_zone":"Kabul gören kişi giriş öncesinde kendini yabancı hissetmeyebilir ve yakınlık işareti bulabilir."},{"boundary_match":"partial","distinction":"Çevreyi gözlemek yalnız bilgi edinir; odak dal içeridekilerden onay almayı amaçlar. Birini görmek veya sesini duymak, tek başına giriş izni değildir.","focus_only":"Odak dal girişten önce selam verip izin ve kabul aramayı gerektirir.","gloss":"izin arama ile çevreyi gözleme","neighbor_only":"Komşu dal görme, işitme, belirti sezme veya çevreye bakarak birini araştırma eylemlerini anlatır.","neighbor_ref":"root_000059/B002","relation_type":"near_neighbor","shared_zone":"Girişten önce içeride birinin bulunup bulunmadığını anlamaya çalışma iki alanı aynı durumda buluşturabilir."},{"boundary_match":"thematic_only","distinction":"Odak dal girişten önceki toplumsal onayı, komşu dal ise bir yere yönelip orada barınmayı anlatır; aralarında sıradan sözcüksel yer değiştirme yoktur.","focus_only":"Odak dal bir eve girmeden önce kabul ve izin arama davranışıdır.","gloss":"eve giriş izni ile barınma","neighbor_only":"Komşu dal bir yere sığınma, yerleşme, barınma veya başkasını barındırma hareketini anlatır.","neighbor_ref":"root_000070/B001","relation_type":"thematic","shared_zone":"İki dal da bir yerle insan arasındaki giriş ve bulunma senaryosunda yer alabilir."}],"source_phrase_ar":"حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)","source_summary":"Giriş öncesi davranış iki yönden açıklanır: selam verip açıkça izin istemek ve girebilir miyim diye sormak ya da içeridekilerden girişe elverişli bir kabul ve yakınlık bulmak. Her iki açıklama da eve izinsiz girmeme sınırında birleşir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه تفسير حتى تستأنسوا بالاستئذان أو السلام وطلب الدخول، أو بإيجاد إيناس قبل الدخول.","what_is_not_ar":"لا يدخل مطلق الإبصار أو مطلق الأنس إلا في صيغة الدخول المذكورة."},"support_links":[]},{"boundary":"Bu dal yalnızca genel eksilmeyi anlatır; ticari sonuç, ölçüde haksızlık veya kişinin yıkıma sürüklenmesi anlamlarını kendi başına taşımaz.","branch_kind":"bare","branch_ref":"root_000409/B001","candidate_links":[{"candidate_id":"cand_9f9d9d1a9b464576a7c7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","surface_ar":"خُسْرٍ"}],"gloss":"eksilme ve değer yitimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, sahip olduğu miktarın, bütünlüğün veya değerin bir bölümünü yitirir."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eksilme tartıda görülebilir, ancak dalın kapsamı tartıyla sınırlı değildir."}}],"root_ar":"خ س ر","root_id":"root_000409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir varlığın miktar, bütünlük veya değer bakımından önceki düzeyinin altına düşmesini alan belirtmeden anlatırken kullanılır.","boundary_detail":"Bu dal yalnızca genel eksilmeyi anlatır; ticari sonuç, ölçüde haksızlık veya kişinin yıkıma sürüklenmesi anlamlarını kendi başına taşımaz.","branch_image_ar":"النقص العام","concept_gloss":"eksilme ve değer yitimi","contextual_glosses":[{"applicability":"Miktarı gözlenebilen bir şeyin önceki düzeyinin altına inmesini akıcı biçimde anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütünlük veya değer kaybı biçimindeki daha geniş uygulamayı belirtmez.","preserves":"Önceki miktarın altına düşme yönünü açıkça korur."},"facet_ids":["F001"],"text":"azalmak","usage_role":"contextual"},{"applicability":"Bir sonuç ya da elde kalan miktar beklenen düzeye ulaşmadığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eksilmeye yol açan süreci ve genel değer yitimini açıkça taşımaz.","preserves":"Beklenen veya önceki düzeyin altında kalma sonucunu korur."},"facet_ids":["F001"],"text":"eksik çıkmak","usage_role":"contextual"}],"definition":"Bir şeyin miktarından, bütünlüğünden veya değerinden bir bölümün gitmesi ve böylece önceki düzeyinin altına düşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, sahip olduğu miktarın, bütünlüğün veya değerin bir bölümünü yitirir."},{"facet_id":"F002","role":"example","statement":"Eksilme tartıda görülebilir, ancak dalın kapsamı tartıyla sınırlı değildir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede yoğun düş kırıklığı ve duygusal çöküş çağrışımı ekler.","collision":"Türkçedeki yerleşik duygusal kullanımı, genel nicel eksilme anlamıyla karışır.","fit":"drifted_loanword","loses":"Miktar, bütünlük veya değerdeki yalın eksilmeyi karşılamaz.","preserves":"Olumsuz bir sonuç ve yitim duygusunu kısmen korur."},"text":"hüsran"}],"identity_rationale":"Kaynak cümlesi, dalın ortak çekirdeğini bir şeyin önceki miktarından, bütünlüğünden veya değerinden eksilmesi olarak kurar. Tartı örneği bu genel çekirdeğin bir gerçekleşmesidir; alım satım, ölçüde eksik verme ve yıkıma uğrama ise ayrı dallarda özelleşir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"eksilme ve değerden düşme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"eksilme, azalma ve değer yitimi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"azalmak veya bir eksilmeye uğramak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"eksilme ya da eksik kalan sonuç"}],"lexicalization_note":"Mekanik sınıf çıplaktır; tanım, herhangi bir özel söz dizimine bağlı olmadan genel eksilme çekirdeğini verir ve öteki dalların bağlama özgü anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel nicel azalma ve iki kardeş özelleşme sınırı en çok açıklayan karşıtlıklar olarak seçildi. Öteki adaylar aynı eksilme alanındaki daha dar örnekleri yineliyor veya yalnızca uzak bir ölçme ve yokluk alanını paylaşıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel ve nötr bir azalma sözlüğü sunarken odak dal, eksilmeyi bir şeyden pay veya değer gitmesi yönüyle öne çıkarır; bu yüzden kapsamlar güçlü biçimde örtüşse de her bağlamda birbirinin yerine geçmez.","focus_only":"Odak dal, eksilmeyi aynı zamanda değer veya bütünlük yitimi olarak çerçeveler.","gloss":"değer yitimi ile nötr nicel azalma","neighbor_only":"Komşu dal, artışın karşıtı olan nicel azalmayı geçişli ve geçişsiz kullanımlarıyla daha nötr biçimde kapsar.","neighbor_ref":"root_001542/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin önceki miktarından bir bölümün gitmesini ve daha az hale gelmesini anlatır."},{"boundary_match":"partial","distinction":"Ticari dalın çekirdeğinde alım satım ve kazanç beklentisi vardır; odak dalda ise böyle bir işlem veya beklenti bulunması gerekmez.","focus_only":"Odak dal, alan belirtmeden her türlü miktar veya değer eksilmesini kapsar.","gloss":"genel eksilme ile ticari yitim","neighbor_only":"Komşu dal, alım satımda kazanç doğmamasını veya anaparanın eksilmesini şart koşar.","neighbor_ref":"root_000409/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da eldeki değerin azalması ortak bir sonuç olabilir."},{"boundary_match":"partial","distinction":"Odak dal durum veya sonuç düzeyinde genel eksilmeyi karşılar; komşu dal ise ölçme ya da tartma sırasında nesneyi eksik bırakmaya bağlı geçişli bir işlemdir.","focus_only":"Odak dal, eksilmenin kendisini anlatır ve bir ölçme işlemi gerektirmez.","gloss":"kendiliğinden eksilme ile ölçüde eksiltme","neighbor_only":"Komşu dal, bir failin ölçü veya tartı sonucunu eksik bırakmasını anlatır.","neighbor_ref":"root_000409/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ortaya çıkan sonuç beklenen miktardan daha azdır."}],"source_phrase_ar":"أصل واحد يدل على النقض (maqayis); الخسر النقصان والخسران كذلك (ayn;tahdhib); خسر إذا نقص ميزانا أو غيره (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bir şeyin miktar veya değer bakımından eksilmesidir; tek asıl açıklaması Maqayis'e, tartıda veya başka şeyde eksilme ayrıntısı ise Tahdhib'e aittir.","sources":["MQ","AY","TA"],"what_is_ar":"النقص والانتقاص وذهاب القدر على وجه عام","what_is_not_ar":"وضع التجارة; تنقيص الكيل والميزان; الهلاك والضلال إذا صارا فرعا مستقلا"},"support_links":["sup_fb369d0ac1a3794876b1"]},{"boundary":"Bu dal yalnızca alım satım ve ticaret sonucuna ilişkindir; genel eksilme veya ölçüde eksik verme anlamı buradan türetilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000409/B002","candidate_links":[{"candidate_id":"cand_752bff4320c50f5d2433","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","surface_ar":"خُسْرٍ"}],"gloss":"alım satımda kazanç sağlayamama veya anaparadan yitirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alım satımın sonunda başlangıç anaparasından bir bölüm yitirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Anapara bütünüyle korunmuş olsa bile beklenen kazancın doğmaması bu ticari sonuca girebilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kazanç getirmeyen bir alışveriş, dalın tipik gerçekleşmesidir."}}],"root_ar":"خ س ر","root_id":"root_000409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir satışın ya hiç kazanç getirmediği ya da işe konan anaparayı azalttığı ticari sonuçların tamamında kullanılır.","boundary_detail":"Bu dal yalnızca alım satım ve ticaret sonucuna ilişkindir; genel eksilme veya ölçüde eksik verme anlamı buradan türetilmez.","branch_image_ar":"خسارة التجارة","concept_gloss":"alım satımda kazanç sağlayamama veya anaparadan yitirme","contextual_glosses":[{"applicability":"Alım satım anaparayı tüketmese de beklenen getiriyi doğurmadığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anaparanın gerçekten azaldığı daha ağır sonucu tek başına belirtmez.","preserves":"Beklenen ticari getirinin gerçekleşmemesini doğal biçimde korur."},"facet_ids":["F002"],"text":"kazanç sağlayamamak","usage_role":"contextual"},{"applicability":"Bir ticari işlem başlangıçta işe konan parayı azalttığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Anapara eksilmeden yalnızca kazancın doğmadığı durumu kapsamaz.","preserves":"Ticari işlem sonucunda anaparanın eksilmesini tam olarak korur."},"facet_ids":["F001"],"text":"anaparadan yitirmek","usage_role":"contextual"}],"definition":"Bir alım satımın beklenen kazancı sağlamaması veya başlangıçta işe konan anaparayı azaltmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alım satımın sonunda başlangıç anaparasından bir bölüm yitirilir."},{"facet_id":"F002","role":"core","statement":"Anapara bütünüyle korunmuş olsa bile beklenen kazancın doğmaması bu ticari sonuca girebilir."},{"facet_id":"F003","role":"example","statement":"Kazanç getirmeyen bir alışveriş, dalın tipik gerçekleşmesidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Borçları ödeyememe ve bütün işletmenin mali çöküşü anlamını ekler.","collision":"Bir işlemin olumsuz sonucu ile işletmenin ödeme gücünü yitirmesi karışır.","fit":"displacement","loses":"Yalnızca kazanç doğmaması veya tek bir işlemde anapara azalması gibi daha hafif durumları dışarıda bırakır.","preserves":"Ticari işin olumsuz bir sonuç vermesini korur."},"text":"iflas etmek"}],"identity_rationale":"Kaynak cümlesi ticari sonucu iki tamamlayıcı görünümle verir: alım satım beklenen kazancı sağlamaz ya da başlangıç anaparasını azaltır. Kazanç getirmeyen alışveriş örneği de bu sınırı doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"satıcının anaparasından yitirmesi veya kazanç sağlayamaması"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"satışta kazanç sağlayamamak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"alışverişinde kazanç sağlayamayan veya anaparasından yitiren kişi"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"alım satımda kazanç sağlayamama ya da anaparadan yitirme"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kazanç getirmeyen alışveriş"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"alışveriş işinin kazanç getirmemesi veya anaparayı eksiltmesi"}],"lexicalization_note":"Mekanik sınıf karışık ve çıplak olmayan kullanımlar içerir; bağımsız biçimler ticari yitimi adlandırırken söz öbekleri satış, alışveriş ve iş bağlamına bağlı kalır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; anaparadan düşüş bildiren yakın komşu, kazanç kutbu ve ölçüde eksiltme sınırı yayıma değer bulundu. Ticaret, para, satış ve mal edinme adaylarının geri kalanı aynı alanı paylaşsa da bu dalın olumsuz sonuç çekirdeğiyle doğrudan örtüşmez.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kazançsızlığı da içine alan işlem sonucuna yönelir; komşu dal ise anaparadan yapılan düşüşü ve bedelin indirilmesini daha belirgin biçimde öne çıkarır.","focus_only":"Odak dal, anapara azalmadan yalnızca beklenen kazancın doğmamasını da kapsar.","gloss":"ticari yitim ile anaparadan indirim","neighbor_only":"Komşu dal, anaparadan indirim ve işlem bedelini aşağı çekme isteğini ayrıca kapsar.","neighbor_ref":"root_001657/B004","relation_type":"near_synonym","shared_zone":"İki dal da ticarette başlangıç değerinin azalmasını ve olumsuz işlem sonucunu anlatır."},{"boundary_match":"opposed","distinction":"Odak dal sonuç değerinin bekleneni karşılamadığı olumsuz kutbu, komşu dal ise işlemden artı değer doğduğu olumlu kutbu anlatır.","focus_only":"Odak dalda kazanç doğmaz veya anapara azalır.","gloss":"ticari yitim ve ticari kazanç","neighbor_only":"Komşu dalda alım satım artı değer ve kazanç üretir.","neighbor_ref":"root_000533/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal aynı alım satımın başlangıç değeri ile sonuç değeri arasındaki ilişkiyi değerlendirir."},{"boundary_match":"field_only","distinction":"Ticari yitim, ölçü doğru olsa bile piyasa veya işlem sonucu olarak doğabilir; eksik ölçme ise kazanç sonucundan bağımsız, ölçüm eyleminin kendisindeki eksiltmedir.","focus_only":"Odak dal, ticari işin kazanç ve anapara bakımından sonucunu bildirir.","gloss":"işlem sonucu ile eksik ölçme","neighbor_only":"Komşu dal, ölçme veya tartma sırasında teslim edilen miktarın eksik bırakılmasını bildirir.","neighbor_ref":"root_000409/B003","relation_type":"same_field","shared_zone":"İki dal da alışveriş çevresinde taraflardan birinin daha az değer elde etmesine yol açabilir."}],"source_phrase_ar":"الخاسر الذي وضع في تجارته (ayn;tahdhib); خسر التاجر إذا وضع من رأس ماله (jamhara); خسر في البيع خسرا وخسرانا (sihah); انتقاص رأس المال (mufradat); صفقة خاسرة أي غير مربحة (ayn;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, ticaret veya alım satımın kazançsız ya da eksilten bir sonuç vermesidir; anapara eksilmesi Jamhara ve Mufradat'ta, satışta kaybetme Sihah'ta, kazanç getirmeyen alışveriş Ayn ve Tahdhib çizgisinde ayrı görünür.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"وضع رأس المال أو عدم الربح في البيع والتجارة والصفقة","what_is_not_ar":"النقص المجرد; تنقيص المكيال والميزان; الهلاك الأخروي"},"support_links":["sup_329b406a8e841fffa9c2"]},{"boundary":"Bu dal ticari kazanç sonucunu değil, ölçme ve tartma eyleminde miktarın eksik bırakılmasını anlatır; alan belirtilmeden gerçekleşen her azalmaya yayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000409/B003","candidate_links":[{"candidate_id":"cand_5b8551b50da8179c61e8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","surface_ar":"خُسْرٍ"}],"gloss":"ölçü ve tartıda eksiltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir fail, ölçü veya tartı sonucunu olması gerekenden daha az hale getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eksiltme, ölçülen ya da tartılan nesnenin teslim edilen miktarında gerçekleşebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Olumsuz emir kullanımı, ölçü ve tartının eksiltilmeden doğru tutulmasını ister."}}],"root_ar":"خ س ر","root_id":"root_000409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölçülen, tartılan veya teslim edilen miktarın bir fail tarafından gereken düzeyin altında bırakıldığı durumlarda kullanılır.","boundary_detail":"Bu dal ticari kazanç sonucunu değil, ölçme ve tartma eyleminde miktarın eksik bırakılmasını anlatır; alan belirtilmeden gerçekleşen her azalmaya yayılmaz.","branch_image_ar":"إخسار الكيل والميزان","concept_gloss":"ölçü ve tartıda eksiltme","contextual_glosses":[{"applicability":"Bir malın hacim veya sayım temelli ölçüsü gereken miktarın altında bırakıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağırlıkla yapılan tartma uygulamasını tek başına belirtmez.","preserves":"Ölçme sırasında ortaya çıkarılan eksik miktarı açıkça korur."},"facet_ids":["F001","F002"],"text":"eksik ölçmek","usage_role":"contextual"},{"applicability":"Bir malın ağırlığı belirlenirken sonuç gereken miktarın altında bırakıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ağırlık dışındaki ölçme uygulamalarını tek başına kapsamaz.","preserves":"Tartma sırasında miktarı eksik bırakma işlemini açıkça korur."},"facet_ids":["F001","F002"],"text":"eksik tartmak","usage_role":"contextual"}],"definition":"Ölçülen veya tartılan şeyi, ölçü aracını ya da teslim edilen miktarı gereken düzeyin altında bırakacak biçimde eksiltmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir fail, ölçü veya tartı sonucunu olması gerekenden daha az hale getirir."},{"facet_id":"F002","role":"specialization","statement":"Eksiltme, ölçülen ya da tartılan nesnenin teslim edilen miktarında gerçekleşebilir."},{"facet_id":"F003","role":"associated_use","statement":"Olumsuz emir kullanımı, ölçü ve tartının eksiltilmeden doğru tutulmasını ister."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Fazla tartma veya istemeden yapılan her türlü ölçüm yanlışını da kapsama ekler.","collision":"Yönü belirsiz ölçüm hatası, gereken miktarı eksik bırakma işlemiyle karışır.","fit":"broadening","loses":"Sapmanın özellikle eksiltme yönünde ve teslim edilen miktarda olduğunu kesinleştirmez.","preserves":"Tartı sonucunun doğru değerden ayrılmasını kısmen korur."},"text":"yanlış tartmak"}],"identity_rationale":"Kaynak cümlesi, ölçülen veya tartılan şeyi ya da ölçü aracını gereken düzeyin altında bırakmaya yönelik geçişli bir işlemi açıkça gösterir. Olumsuz emir biçimi, aynı işlemin adil ölçüye aykırı sınırını belirler.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"teraziyi veya tartılan şeyi eksik bırakmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ölçerken ya da tartarken eksik vermek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"verirken eksik ölçüp alırken daha çoğunu isteyen kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ölçü ve tartıda eksiltmeyin, haksızlık etmeyin"}],"lexicalization_note":"Mekanik sınıf karışık ve çıplak olmayan kullanımlar içerir; ölçü, tartı ve nesneyle kurulan söz öbekleri kendi işlem sınırında tutulur, bağımsız kişi biçimi ise yalnızca bu işi yapanı adlandırır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; ölçüyü tamamlamama, haktan eksiltme, miktarı belirleme ve ticari sonuç sınırları en açıklayıcı dört ayrım olarak seçildi. Ölü birim adları ve genel eksilme adayları bu ayrımlara yeni bir sınır eklemediği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal özellikle ölçüyü tamamlamayıp karşı tarafa eksik pay verme üzerinde yoğunlaşır; odak dal ise teraziyi, ölçüyü veya nesneyi eksiltmeye yönelik daha genel geçişli anlatımları da kapsar.","focus_only":"Odak dal, ölçü aracını veya ölçülen şeyi doğrudan eksiltme anlatımını daha geniş biçimde kapsar.","gloss":"ölçüyü eksiltme ile ölçüyü tamamlamama","neighbor_only":"Komşu dal, teslim ve karşılama sırasında pay sahibine ölçüyü tamamlamamayı özellikle öne çıkarır.","neighbor_ref":"root_000940/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da ölçülen veya tartılan miktarın hak sahibine gerekenden az verilmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal ölçüm işlemini zorunlu kılar; komşu dal ise bir hakkın veya değerin azaltılmasını daha geniş bir alan içinde anlatır ve her zaman ölçü aracı gerektirmez.","focus_only":"Odak dalın çekirdeği ölçme veya tartma işleminde eksiltmedir.","gloss":"ölçüde eksiltme ile haktan eksiltme","neighbor_only":"Komşu dal hak, bedel, karşılık ve küçük miktar gibi ölçüm dışındaki eksiltmeleri de kapsar.","neighbor_ref":"root_000087/B001","relation_type":"near_neighbor","shared_zone":"İki dal da birine düşen miktarı veya değeri olması gerekenden az hale getirebilir."},{"boundary_match":"field_only","distinction":"Komşu dalın çekirdeği aracın doğruluğunu belirleyen ayar ve ölçüttür; odak dalın çekirdeği ise ölçülen ya da teslim edilen miktarı gereken düzeyin altında bırakmaktır.","focus_only":"Odak dal ölçüm sonucunu gereken düzeyin altına indirmeyi anlatır.","gloss":"ölçüyü eksiltme ile ölçüyü ayarlama","neighbor_only":"Komşu dal, ölçü ve tartı araçları için doğruluğu belirleyen ayar ve ölçütü anlatır.","neighbor_ref":"root_001066/B013","relation_type":"same_field","shared_zone":"Her iki dalın gerçekleşmesinde ölçü veya tartı aracının verdiği miktar temel alınır."},{"boundary_match":"field_only","distinction":"Eksik ölçme, işlemin sonucundan bağımsız olarak ölçümün nasıl yapıldığıyla ilgilidir; ticari yitim ise ölçü doğru olsa bile ortaya çıkabilen kazançsızlık veya anapara azalmasıdır.","focus_only":"Odak dal ölçme veya tartma eylemindeki eksiltmeyi bildirir.","gloss":"eksik ölçme ile ticari yitim","neighbor_only":"Komşu dal alım satımın kazanç veya anapara bakımından olumsuz sonucunu bildirir.","neighbor_ref":"root_000409/B002","relation_type":"same_field","shared_zone":"İki dal da bir alışverişte taraflardan birinin beklenenden daha az değer elde etmesiyle ilişkilendirilebilir."}],"source_phrase_ar":"خسرت الميزان وأخسرته إذا نقصته (maqayis); كلته ووزنته فأخسرته أي نقصته (ayn;tahdhib); أخسرت الميزان وخسرته (tahdhib); خسرت الشيء وأخسرته نقصته (sihah); ولا تخسروا الميزان (mufradat); ينقصون في الكيل والوزن (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, ölçü veya tartı sonucunu gereken miktarın altında bırakacak biçimde eksiltmektir; teraziye bağlı fiiller Maqayis ve Tahdhib'te, daha genel eksiltme Sihah'ta, olumsuz emir ve adalet açıklaması Mufradat'ta, eksik ölçüp tartan davranışı ise Tahdhib'te belirginleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"تنقيص الميزان أو المكيال أو الشيء عند الكيل والوزن","what_is_not_ar":"خسارة التجارة من غير كيل; الهلاك والضلال; النقص العام بلا معاملة"},"support_links":["sup_a61478b7b22aee44dda8"]},{"boundary":"Dal yalnızca ölümü veya dış mal kaybını anlatmaz; doğru yönelişten ve kişiye bağlı iyiliklerden yoksun kalmayı da kapsar, ancak her cezayı doğrudan bu anlamla eşitlemez.","branch_kind":"mixed_non_bare","branch_ref":"root_000409/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","surface_ar":"خُسْرٍ"}],"gloss":"doğru yoldan sapıp iyiliklerini yitirerek yıkıma düşme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi doğru yönden sapar, iyilikten uzaklaşır ve yıkıma götüren bir yitime düşer."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yitirilen şey dış mal olabileceği gibi sağlık, güvenlik, akıl, inanç veya yapılan iyiliğin karşılığı da olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İşlenen kötülüklerin karşılığına düşmek ve iyilikten uzaklaştırılmak bu yıkıcı yitimin sonuçları olarak anlatılabilir."}}],"root_ar":"خ س ر","root_id":"root_000409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin dış veya kendine bağlı kazanımlarını, doğru yönelişini ve iyi son beklentisini birlikte yitirdiği ağır durumlarda kullanılır.","boundary_detail":"Dal yalnızca ölümü veya dış mal kaybını anlatmaz; doğru yönelişten ve kişiye bağlı iyiliklerden yoksun kalmayı da kapsar, ancak her cezayı doğrudan bu anlamla eşitlemez.","branch_image_ar":"الضلال والهلاك","concept_gloss":"doğru yoldan sapıp iyiliklerini yitirerek yıkıma düşme","contextual_glosses":[{"applicability":"Yitimin kişiyi bütünüyle kötü ve geri döndürülemez görünen bir sona sürüklediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Doğru yönden sapma ile tek tek iyiliklerin yitirilmesi aşamalarını açıkça göstermez.","preserves":"Yitimin ağır ve yok edici sonucunu güçlü biçimde korur."},"facet_ids":["F001"],"text":"yıkıma uğramak","usage_role":"contextual"},{"applicability":"Kişinin yaptığı işlerin beklenen iyi karşılığı üretmediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sağlık, güvenlik, yakınlar ve kişinin bütünüyle yıkıma düşmesi gibi öteki kapsamları dışarıda bırakır.","preserves":"Yapılan işin iyi karşılığının yitirilmesini korur."},"facet_ids":["F002"],"text":"yaptıkları boşa gitmek","usage_role":"contextual"},{"applicability":"Yitimin kişinin kendi varlığına ve yakınlarıyla bağlarına yöneldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl, inanç, güvenlik ve yapılan iyiliğin karşılığı gibi öteki kazanımları belirtmez.","preserves":"Kişinin kendisini ve yakınlarını kapsayan ağır yitim alanını korur."},"facet_ids":["F002"],"text":"kendini ve yakınlarını yitirmek","usage_role":"explanatory"}],"definition":"Kişinin doğru yönelişini ve sahip olduğu iyilikleri yitirerek kötü bir sona, hatta yıkıma düşmesidir. Bu yitim dış mallarla sınırlı değildir; sağlık, güvenlik, akıl, inanç ve yapılan iyiliğin karşılığı gibi kişiye bağlı kazanımları da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi doğru yönden sapar, iyilikten uzaklaşır ve yıkıma götüren bir yitime düşer."},{"facet_id":"F002","role":"extension","statement":"Yitirilen şey dış mal olabileceği gibi sağlık, güvenlik, akıl, inanç veya yapılan iyiliğin karşılığı da olabilir."},{"facet_id":"F003","role":"associated_use","statement":"İşlenen kötülüklerin karşılığına düşmek ve iyilikten uzaklaştırılmak bu yıkıcı yitimin sonuçları olarak anlatılabilir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Güncel Türkçede kişisel düş kırıklığı ve duygusal sarsıntı anlamını öne çıkarır.","collision":"Duygusal düş kırıklığı, kişiyi ve kazanımlarını kuşatan daha geniş yıkıcı yitimle karışır.","fit":"drifted_loanword","loses":"Doğru yönden sapma, çeşitli iyiliklerden yoksun kalma ve yıkım kapsamını açıkça taşımaz.","preserves":"Ağır bir olumsuz sonuca ve yitim duygusuna düşmeyi korur."},"text":"hüsrana uğramak"},{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sapma, iyilikten uzaklaşma ve ölüm olmadan gerçekleşen kişisel kazanım yitimlerini dışarıda bırakır.","preserves":"Yıkımın yaşamın sona ermesine vardığı en uç durumu korur."},"text":"ölmek"}],"identity_rationale":"Kaynak cümlesi doğru yönden sapma ve yıkıma uğramayı çekirdekte birleştirir; sağlık, güvenlik, akıl, inanç ve yapılan iyiliğin karşılığı gibi kişiye bağlı kazanımların yitimi bu çekirdeğin kapsamını genişletir. İşlenen kötülüklerin karşılığına düşmek ise çekirdeğin kendisi değil, bu yitimin bağlamsal sonucudur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"doğru yoldan sapma ve yıkıma uğrama"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"sapma, yitim ve yıkım"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"maddi olmayan iyilikleri de kapsayan yitim ve yıkım"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yıkıma uğramak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yıkıma uğratma veya iyilikten uzaklaştırma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bu dünyadaki ve öte dünyadaki kazanımlarını yitirmek"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kendilerini ve yakınlarını yitirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yarar sağlamayan dönüş"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yaptıkları en çok boşa giden"}],"lexicalization_note":"Mekanik sınıf karışık ve çıplak olmayan kullanımlar içerir; bağımsız biçimler yitim ve yıkımı adlandırırken dünya, öte dünya, kişi, yakınlar ve yararsız dönüş söz öbekleri kendi bağlamlarıyla sınırlı tutulur.","neighbor_coverage_note":"Bütün adaylar incelendi; genel eksilme, malı tüketme ve ticari yitimle kurulan üç sınır dalın kapsamını açıklıyor. Diğer adaylar satış, bedel, bolluk veya işlem biçimi alanında kaldığından doğru yönden sapma ve kişisel yıkım çekirdeğine doğrudan bir karşılaştırma sunmuyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel eksilme küçük ve nötr bir azalma için de kullanılabilir; odak dal ise kişinin yönelişini ve temel kazanımlarını etkileyen, kötü sona varan ağır yoksunluğu gerektirir.","focus_only":"Odak dal doğru yöneliş, kişiye bağlı iyilikler ve yıkıcı son bakımından ağırlaşmış bir yitimi anlatır.","gloss":"genel eksilme ile kişisel yıkım","neighbor_only":"Komşu dal, herhangi bir şeydeki genel miktar veya değer eksilmesini alan belirtmeden kapsar.","neighbor_ref":"root_000409/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da önceden sahip olunan bir miktar, değer veya iyilik artık elde değildir."},{"boundary_match":"thematic_only","distinction":"Komşu dal yitimin nedeni olabilecek tüketme veya alma eylemini fail açısından kurar; odak dal ise etkilenen kişinin maddi alanı aşabilen yoksunluk ve yıkım durumunu anlatır.","focus_only":"Odak dal, yitiren kişinin dış ve kendine bağlı iyiliklerden yoksun kalıp yıkıma düşen durumunu anlatır.","gloss":"yoksun kalma ile malı tüketme","neighbor_only":"Komşu dal, bir failin malı tüketmesi, harcaması veya başkasının malını alması eylemini anlatır.","neighbor_ref":"root_000043/B004","relation_type":"thematic","shared_zone":"Birinin maldan veya değerden yoksun kalması iki dalın yer aldığı ortak senaryoda sonuç olabilir."},{"boundary_match":"partial","distinction":"Ticari dal tek bir ekonomik işlemle sınırlıdır; odak dal ise dış mallardan kişinin sağlığına, aklına, inancına ve iyi son beklentisine kadar uzanan daha ağır bir yitim alanıdır.","focus_only":"Odak dal kişinin yönelişini, varlığını ve maddi olmayan kazanımlarını da kuşatır.","gloss":"kişisel yıkım ile ticari yitim","neighbor_only":"Komşu dal yalnızca alım satımın kazanç ve anapara bakımından olumsuz sonucuna bağlıdır.","neighbor_ref":"root_000409/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da eldeki bir değer veya beklenen iyi sonuç yitirilir."}],"source_phrase_ar":"الخسر والخسار والخسران واحد وهو الضلال (jamhara); التخسير الإهلاك (sihah); الخسار والخسارة والخيسرى الضلال والهلاك (sihah); خسر إذا هلك (tahdhib); لفي عقوبة بذنوبه (tahdhib); غير إبعاد من الخير (tahdhib); المقتنيات النفسية كالصحة والسلامة والعقل والإيمان والثواب (mufradat)","source_summary":"Kaynakların ortak çekirdeği, sapma veya yıkıma varan ağır bir yitim durumudur; ad biçimlerinin sapma eşdeğerliği Jamhara ve Sihah'ta, yıkım ve yıkıma uğratma Sihah ve Tahdhib'te, ceza ve iyilikten uzaklaştırılma Tahdhib'te, sağlık, güvenlik, akıl, inanç ve karşılık yitimi ise Mufradat'ta ayrışır.","sources":["JA","SI","TA","MU"],"what_is_ar":"الضلال والهلاك والعقوبة والخسران في النفس والأهل والإيمان والثواب","what_is_not_ar":"خسارة البيع وحدها; تنقيص الميزان وحده; النقص اللفظي العام"},"support_links":[]},{"boundary":"Dal bir biçim ailesi olarak korunabilir, ancak iki anlam kümesi birbirine karıştırılmamalı ve bu özel biçimlerin anlamı genel kök anlamına yayılmamalıdır.","branch_kind":"bare","branch_ref":"root_000409/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","surface_ar":"خُسْرٍ"}],"gloss":"yitim, yıkım veya güçsüz kişileri bildiren genişlemiş biçimler","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sesçe genişlemiş bağımsız biçimler, iki ayrı anlam kümesinde kalıplaşmış özel sözler oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Biçimlerin bir bölümü yitim veya yıkım bildiren sözlerin yerinde kullanılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir çoğul biçim, güçsüz veya aşağı görülen insanları topluca adlandırır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Başka bir çoğul biçim tekili bulunmadan doğrudan yıkım anlamında kullanılır."}}],"root_ar":"خ س ر","root_id":"root_000409","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek bir olay anlamı yerine, kaynakta verilen özel bağımsız biçimleri ve bunların iki anlam kümesini birlikte tanıtması gerektiğinde kullanılır.","boundary_detail":"Dal bir biçim ailesi olarak korunabilir, ancak iki anlam kümesi birbirine karıştırılmamalı ve bu özel biçimlerin anlamı genel kök anlamına yayılmamalıdır.","branch_image_ar":"الخنسرى والخيسرى والخناسر","concept_gloss":"yitim, yıkım veya güçsüz kişileri bildiren genişlemiş biçimler","contextual_glosses":[{"applicability":"Özel genişlemiş biçimlerden biri kayıp veya yok oluş bildiren sözün yerinde kullanıldığında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Güçsüz veya aşağı görülen insanları adlandıran öteki anlam kümesini dışarıda bırakır.","preserves":"Biçim ailesinin yitim ve yıkım bildiren anlam kümesini korur."},"facet_ids":["F002","F004"],"text":"yitim ya da yıkım","usage_role":"contextual"},{"applicability":"İnsan topluluğunu bildiren özel çoğul biçimin güç veya toplumsal değer bakımından küçümseyici kullanımında geçerlidir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yitim ve yıkım bildiren biçimleri ve tekilsiz çoğul kullanımını dışarıda bırakır.","preserves":"Kişileri güçsüz veya aşağı sayan toplu adlandırmayı korur."},"facet_ids":["F003"],"text":"güçsüz ve aşağı görülen kişiler","usage_role":"explanatory"}],"definition":"Bu dal, sesçe genişlemiş ve kalıplaşmış biçimlerin oluşturduğu bir söz varlığı kümesidir. Biçimlerden bir bölümü yitim veya yıkımı, bir bölümü güçsüz ya da aşağı görülen insanları adlandırır; yıkım bildiren çoğul biçimlerden biri tekilsiz kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sesçe genişlemiş bağımsız biçimler, iki ayrı anlam kümesinde kalıplaşmış özel sözler oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Biçimlerin bir bölümü yitim veya yıkım bildiren sözlerin yerinde kullanılır."},{"facet_id":"F003","role":"specialization","statement":"Bir çoğul biçim, güçsüz veya aşağı görülen insanları topluca adlandırır."},{"facet_id":"F004","role":"source_variant","statement":"Başka bir çoğul biçim tekili bulunmadan doğrudan yıkım anlamında kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kişi adından bağımsız soyut bir nitelik anlamı ekler.","collision":"Özel bir kişi adlandırması, genel güçsüzlük niteliğiyle karışır.","fit":"displacement","loses":"Yitim ve yıkım anlamlarını, kişi topluluğunu ve özel biçim ailesini dışarıda bırakır.","preserves":"İnsanları güçsüz gösteren kullanımın bir yönünü korur."},"text":"zayıflık"}],"identity_rationale":"Kaynak cümlesi tek bir yalın anlamdan çok, sesçe genişlemiş ve kalıplaşmış birkaç biçimi bir araya getirir. Bu biçimlerin bir bölümü yitim veya yıkımı, bir bölümü ise güçsüz ya da aşağı görülen insanları bildirir; ayrıca yıkım bildiren tekilsiz bir çoğul biçim vardır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yitim veya kayıp bildiren genişlemiş biçim"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"yitim ya da yıkım bildiren genişlemiş biçim"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"güçsüz veya aşağı görülen insanlar"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"tekili bulunmayan, yıkım anlamındaki çoğul biçim"}],"lexicalization_note":"Mekanik sınıf çıplaktır ve bütün birimler bağımsız biçimlerdir; yine de anlamlar her kalıplaşmış biçime bağlı tutulur, özel kişi ve yıkım kullanımlarından yeni bir genel kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğrudan yıkım, güçsüz ve yararsız varlıklar ile genel eksilme sınırları en açıklayıcı üç karşılaştırma olarak seçildi. Kalan adaylar yalnızca güçsüzlük, küçüklük, aşağı görme veya harfçe genişleme yönlerinden birini yineliyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal yıkım kavramını doğrudan ve eylemsel uzantılarıyla işler; odak dal ise bu anlamı yalnızca belirli genişlemiş biçimlerde taşır ve ayrıca kişi adlandıran ayrı bir kümeye sahiptir.","focus_only":"Odak dal, sesçe genişlemiş özel biçimleri ve güçsüz veya aşağı görülen kişi adlarını da kapsar.","gloss":"özel genişlemiş biçimler ile doğrudan yıkım","neighbor_only":"Komşu dal, doğrudan yitim, yıkım, bunlara yönelik dilek ve yıkıma uğratma anlamlarını kapsar.","neighbor_ref":"root_000172/B001","relation_type":"near_neighbor","shared_zone":"İki dalın bir bölümünde yitim ve yıkım aynı anlam alanını oluşturur."},{"boundary_match":"partial","distinction":"Odak daldaki kişi anlamı belirli bir çoğul biçime bağlıdır; komşu dal ise yararsızlık ve güçsüzlüğü insanlar ile başka canlılara uzanan daha genel bir niteleme olarak kurar.","focus_only":"Odak dal, yitim ve yıkım bildiren genişlemiş biçimleri de içerir.","gloss":"güçsüz kişiler ile yararsız varlıklar","neighbor_only":"Komşu dal, yararsız, güçsüz veya savaşamayacak kişi ve düşük nitelikli canlıları daha geniş biçimde kapsar.","neighbor_ref":"root_000309/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal insanları güçsüz, düşük değerli veya aşağı görülen kimseler olarak adlandırabilir."},{"boundary_match":"partial","distinction":"Genel dal üretken ve alan belirtmeyen bir eksilme çekirdeğidir; odak dal ise anlamı tek tek kalıplaşmış genişlemiş biçimlerden alınan sınırlı bir söz varlığı kümesidir.","focus_only":"Odak dal belirli genişlemiş biçimlerden oluşur ve güçsüz kişi adlandırmasını da içerir.","gloss":"özel yitim biçimleri ile genel eksilme","neighbor_only":"Komşu dal biçim ailesine bağlı olmadan genel miktar, bütünlük veya değer eksilmesini anlatır.","neighbor_ref":"root_000409/B001","relation_type":"near_neighbor","shared_zone":"Odak daldaki bazı özel biçimler, genel eksilme ve yitim alanıyla bağlantılıdır."}],"source_phrase_ar":"رجل خنسرى وقالوا خيسرى في موضع الخسران النون والياء زائدتان (jamhara); الخناسر جمع خنسر وهو نحو الخنسرى وفي معناه وهم لئام الناس ورذالهم (jamhara); الخناسر الضعاف من الناس (jamhara); الخناسير الهلاك لا واحد له (sihah)","source_summary":"Kaynakların ortak kesişimi, özel biçimlerin yitim ve yıkım anlam alanıyla bağlantı kurmasıdır; artırılmış biçimler ile güçsüz veya aşağı görülen kişi adları Jamhara'ya, tekilsiz yıkım çoğulu ise Sihah'a aittir.","sources":["JA","SI"],"what_is_ar":"الألفاظ المزيدة خنسرى وخيسرى والخناسر إذا جعلت في موضع الخسران أو الهلاك أو اللؤم والضعف","what_is_not_ar":"النقص المجرد; خسارة التجارة; تنقيص الميزان"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["103:2:1"],"branch_refs":[],"candidate_id":"cand_adc40cfac8f732333e6f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:1:audible-heavy-opening","source_type":"word_analysis","support_ids":["sup_12656e2cecc7daba8ba5","sup_44d73d4c94340f058b06"],"title":"the opening sounds compressed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:1","qac_refs":["103:2:1:1"],"status":"accepted"}},{"anchor_refs":["103:2:1"],"branch_refs":[],"candidate_id":"cand_0f75339d115a2ee528bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:1:double-emphasis-frame","source_type":"word_analysis","support_ids":["sup_44d73d4c94340f058b06","sup_60536bf6330f72c285d7"],"title":"opening emphasis is corroborated","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:1","qac_refs":["103:2:1:1"],"status":"accepted"}},{"anchor_refs":["103:2:1"],"branch_refs":[],"candidate_id":"cand_cc9969a3a424d57f668e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:1:governed-emphatic-proposition","source_type":"word_analysis","support_ids":["sup_44d73d4c94340f058b06","sup_958f839ed435975df403"],"title":"emphasis governs the whole claim","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:1","qac_refs":["103:2:1:1"],"status":"accepted"}},{"anchor_refs":["103:2:1"],"branch_refs":[],"candidate_id":"cand_d05ffe16818534a7356c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:1:oath-answer-boundary","source_type":"word_analysis","support_ids":["sup_1014367683cc4f0fa469","sup_44d73d4c94340f058b06"],"title":"the oath receives its answer","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:1","qac_refs":["103:2:1:1"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_1fcc3a425cb4137f235d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:generic-species-scope","source_type":"word_analysis","support_ids":["sup_6866d62f4b1328019b32","sup_f14e092991a88c603ad6"],"title":"one noun carries the species","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_e98131af96863c5d10d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:governed-standing-condition","source_type":"word_analysis","support_ids":["sup_8eb32ba7a51e32865f14","sup_f14e092991a88c603ad6"],"title":"humanity receives the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_65617d01f0dfefb5dd0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:human-loss-root-pair","source_type":"word_analysis","support_ids":["sup_dbbc932cd406cb566813","sup_f14e092991a88c603ad6"],"title":"human and loss form a marked pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_17ba8e14ce0c723b1184","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:oath-to-human-verdict","source_type":"word_analysis","support_ids":["sup_dadfeb58115e113a6fc1","sup_f14e092991a88c603ad6"],"title":"time witness turns human","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_8e41313a040f4fd204d7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:social-forgetful-derivation","source_type":"word_analysis","support_ids":["sup_7e52a93bb49f1df92d34","sup_f14e092991a88c603ad6"],"title":"sociality and forgetfulness create tension","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_ebf3961918c36a9cdd8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:2:sound-thread","source_type":"word_analysis","support_ids":["sup_8b386b837c042c9743e6","sup_f14e092991a88c603ad6"],"title":"sound binds subject to predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:2","qac_refs":["103:2:2:1","103:2:2:2"],"status":"accepted"}},{"anchor_refs":["103:2:3"],"branch_refs":[],"candidate_id":"cand_5290b34930cd83182fc7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:3:containment-predicate","source_type":"word_analysis","support_ids":["sup_0678a58d7152e9152e95","sup_f0f025c485b2ca75919d"],"title":"loss becomes predicate space","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:3","qac_refs":["103:2:3:1","103:2:3:2"],"status":"accepted"}},{"anchor_refs":["103:2:3"],"branch_refs":[],"candidate_id":"cand_305c051ab04362b4e17a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:3:fused-compact-surface","source_type":"word_analysis","support_ids":["sup_ae58052ec008f27d83b9","sup_f0f025c485b2ca75919d"],"title":"two mechanisms are compressed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:3","qac_refs":["103:2:3:1","103:2:3:2"],"status":"accepted"}},{"anchor_refs":["103:2:3"],"branch_refs":[],"candidate_id":"cand_d67ac928d32eb5505b8a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:3:predicate-lam-emphasis","source_type":"word_analysis","support_ids":["sup_9a81e847552de4cede38","sup_f0f025c485b2ca75919d"],"title":"the lām lands on the predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:3","qac_refs":["103:2:3:1","103:2:3:2"],"status":"accepted"}},{"anchor_refs":["103:2:3"],"branch_refs":[],"candidate_id":"cand_0646e13327bd6c67234c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"103:2:3:temporal-to-spatial-boundary","source_type":"word_analysis","support_ids":["sup_9ee014b6ac4f3b5792e0","sup_f0f025c485b2ca75919d"],"title":"time pressure becomes location","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:3","qac_refs":["103:2:3:1","103:2:3:2"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_8e725a604835d6dcb016","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:clipped-form-and-variants","source_type":"word_analysis","support_ids":["sup_3d5708f3e9c3648cdc8d","sup_3f27105b39e3e21a6a9e"],"title":"the standard form lands clipped","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_275bb5f2ae75f0774db0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:closure-and-sound-link","source_type":"word_analysis","support_ids":["sup_10a1e09c762a44cc68d6","sup_3d5708f3e9c3648cdc8d"],"title":"loss is the closing landing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_b2830206c62ea1be040c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:deficit-ruin-root-field","source_type":"word_analysis","support_ids":["sup_3d5708f3e9c3648cdc8d","sup_7e1cc1f94bc8c4e9a0f1"],"title":"deficit and ruin load the loss","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_69ef510469a8337e95b8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:forward-exception-pressure","source_type":"word_analysis","support_ids":["sup_3d5708f3e9c3648cdc8d","sup_98dfca46560686209a24"],"title":"loss demands the exception","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_0bd1b3705c4a9faa186f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:human-loss-recurrence","source_type":"word_analysis","support_ids":["sup_3d5708f3e9c3648cdc8d","sup_fc6df446a0152c333eda"],"title":"the human-loss pair recurs","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_ba9008d94752461be77d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:masdar-state-container","source_type":"word_analysis","support_ids":["sup_34568a2e0df6a3dab4e2","sup_3d5708f3e9c3648cdc8d"],"title":"loss is a state, not an act","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_07b29bf92cd19da515d6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:root-recurrence-specialized","source_type":"word_analysis","support_ids":["sup_301610979788d717110e","sup_3d5708f3e9c3648cdc8d"],"title":"the root concentrates into a gerund","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_9f27b802aaa577a44a1e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:unbounded-indefinite-loss","source_type":"word_analysis","support_ids":["sup_3d5708f3e9c3648cdc8d","sup_fb20b0328bb5218b6951"],"title":"the loss remains unbounded","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"103:2:4","qac_refs":["103:2:4:1"],"status":"accepted"}},{"anchor_refs":["103:2:2"],"branch_refs":[],"candidate_id":"cand_22d052089f274efe1d4a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000059"],"scope":"focus_ayah","source_local_id":"103:2:2:2","source_type":"qac_morpheme","support_ids":["sup_61693beebd12863aaa1c"],"title":"QAC root occurrence: ء ن س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["103:2:4"],"branch_refs":[],"candidate_id":"cand_2b60ac30b4ef577937a0","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000409"],"scope":"focus_ayah","source_local_id":"103:2:4:1","source_type":"qac_morpheme","support_ids":["sup_4613dce73b9ff08d752b"],"title":"QAC root occurrence: خ س ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["103:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:2","branch_refs":["root_000059/B001","root_000409/B001"],"candidate_id":"cand_9f9d9d1a9b464576a7c7","commentary_obligation":"review","hft_ref":"hft_46ff2999869c1a447c55","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_encompassing_deficit","source_type":"hft","support_ids":["sup_fb369d0ac1a3794876b1"],"title":"baseline_encompassing_deficit","trust":"legacy_unbound"},{"anchor_refs":["103:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:2","branch_refs":["root_000059/B001","root_000409/B002"],"candidate_id":"cand_752bff4320c50f5d2433","commentary_obligation":"review","hft_ref":"hft_26060501b9f2464df43e","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_unprofitable_human_account","source_type":"hft","support_ids":["sup_329b406a8e841fffa9c2"],"title":"baseline_unprofitable_human_account","trust":"legacy_unbound"},{"anchor_refs":["103:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"103:2","branch_refs":["root_000059/B002","root_000409/B003"],"candidate_id":"cand_5b8551b50da8179c61e8","commentary_obligation":"review","hft_ref":"hft_2e5cfb47c3477dc76aba","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_short_measure_of_awareness","source_type":"hft","support_ids":["sup_a61478b7b22aee44dda8"],"title":"baseline_short_measure_of_awareness","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"103:2:1:1","qac_word_ref":"103:2:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"103:2:2:1","qac_word_ref":"103:2:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"103:2:3:1","qac_word_ref":"103:2:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"103:2:3:2","qac_word_ref":"103:2:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","root_ar":"خ س ر","surface_ar":"خُسْرٍ"}],"word_analysis_qac_refs":[["103:2:1:1"],["103:2:2:1","103:2:2:2"],["103:2:3:1","103:2:3:2"],["103:2:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["103:2:1","103:2:2","103:2:3","103:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ","qac_morphemes":[{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"103:2:1:1","qac_word_ref":"103:2:1","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"103:2:2:1","qac_word_ref":"103:2:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"إِنسَٰن","morph_features":"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:2:2","qac_word_ref":"103:2:2","root_ar":"ء ن س","surface_ar":"إِنسَٰنَ"},{"lemma_ar":"","morph_features":"PREFIX|l:EMPH+","morpheme_role":"PREFIX","pos":"EMPH","qac_ref":"103:2:3:1","qac_word_ref":"103:2:3","root_ar":"","surface_ar":"لَ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"103:2:3:2","qac_word_ref":"103:2:3","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"خُسْر","morph_features":"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"103:2:4:1","qac_word_ref":"103:2:4","root_ar":"خ س ر","surface_ar":"خُسْرٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["103:2:1:1"],["103:2:2:1","103:2:2:2"],["103:2:3:1","103:2:3:2"],["103:2:4:1"]],"word_analysis_refs":["103:2:1","103:2:2","103:2:3","103:2:4"],"word_rows":[{"analysis_record_ref":"103:2:1","analytic_gloss_range_en":"emphatic particle opening the oath answer and governing the human-loss proposition","analytic_root_gloss_range_en":null,"qac_refs":["103:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِنَّ","transliteration":"inna"}},{"analysis_record_ref":"103:2:2","analytic_gloss_range_en":"definite singular species noun, accusative as the ism of inna, naming humankind as the subject of the loss verdict","analytic_root_gloss_range_en":"root field of human sociality, familiarity, and perception; a classical derivational dispute also lets forgetfulness pressure remain as a narrowed lexical tension","qac_refs":["103:2:2:1","103:2:2:2"],"root":{"arabic":"أ ن س","transliteration":"ʾ-n-s"},"surface":{"arabic":"ٱلْإِنسَٰنَ","transliteration":"al-insāna"}},{"analysis_record_ref":"103:2:3","analytic_gloss_range_en":"fused predicate lām plus fī, combining corroborating emphasis with containment in the khabar","analytic_root_gloss_range_en":null,"qac_refs":["103:2:3:1","103:2:3:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَفِى","transliteration":"la-fī"}},{"analysis_record_ref":"103:2:4","analytic_gloss_range_en":"indefinite gerund of loss, deficiency, and ruin, locally serving as the genitive complement of fī in the emphatic predicate","analytic_root_gloss_range_en":"accepted root range includes general deficiency, trade loss, deficient measure, spiritual ruin and perdition, and augmented loss/baseness forms; local grammar selects the abstract loss-state while allowing deficit and ruin pressure","qac_refs":["103:2:4:1"],"root":{"arabic":"خ س ر","transliteration":"kh-s-r"},"surface":{"arabic":"خُسْرٍ","transliteration":"khusrin"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["103:2"],"branch_refs":["root_000059/B001","root_000409/B001"],"candidate_id":"cand_9f9d9d1a9b464576a7c7","evidence_scope":"focus_ayah","hft_ref":"hft_46ff2999869c1a447c55","item_id":"baseline_encompassing_deficit","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_encompassing_deficit","support_id":"sup_fb369d0ac1a3794876b1"},{"anchor_refs":["103:2"],"branch_refs":["root_000059/B001","root_000409/B002"],"candidate_id":"cand_752bff4320c50f5d2433","evidence_scope":"focus_ayah","hft_ref":"hft_26060501b9f2464df43e","item_id":"baseline_unprofitable_human_account","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_unprofitable_human_account","support_id":"sup_329b406a8e841fffa9c2"},{"anchor_refs":["103:2"],"branch_refs":["root_000059/B002","root_000409/B003"],"candidate_id":"cand_5b8551b50da8179c61e8","evidence_scope":"focus_ayah","hft_ref":"hft_2e5cfb47c3477dc76aba","item_id":"baseline_short_measure_of_awareness","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_short_measure_of_awareness","support_id":"sup_a61478b7b22aee44dda8"}],"diagnostics":[],"lane_counts":{"global":8,"macro":8,"micro":3},"packet_summary":{"ayah_count":3,"focus_ref":"103:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[],"window":["103:1","103:2","103:3"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"103:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"103:2","lane":"micro","linguistic_source_ref":"103:2","surface_ref":"103:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"103:2","target_tokens":[["İnsan",["103:2:2"]],["gerçekten",["103:2:1","103:2:3"]],["kayıp",["103:2:4"]],["içindedir",["103:2:3","103:2:4"]]],"text":"İnsan gerçekten kayıp içindedir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":3,"id":"s103-p01-001-003","label":"Whole surah","number":1,"refs":["103:1","103:2","103:3"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:3:containment-predicate","source_type":"word_analysis","support_id":"sup_0678a58d7152e9152e95","text":"{\"blocking_evidence\":null,\"headline\":\"loss becomes predicate space\",\"reader_payoff\":\"The reader notices that {{ar:فِى}} ({{tr:fī}}) turns loss into a containing predicate space, not a loose object or trait.\",\"reason\":\"QAC and attachment evidence mark {{ar:لَفِى خُسْرٍ}} ({{tr:la-fī khusrin}}) as the prepositional khabar, with {{ar:فِى}} ({{tr:fī}}) governing the loss noun.\",\"representative_source_ids\":[\"QG-8874a77c\",\"QG-cc82a49e\",\"QS-3529166f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:1:oath-answer-boundary","source_type":"word_analysis","support_id":"sup_1014367683cc4f0fa469","text":"{\"blocking_evidence\":null,\"headline\":\"the oath receives its answer\",\"reader_payoff\":\"The reader notices that the oath by {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) (103:1) is not left hanging; {{ar:إِنَّ}} ({{tr:inna}}) releases it into the asserted verdict.\",\"reason\":\"QAC explicitly identifies {{ar:إِنَّ}} ({{tr:inna}}) as the jawāb al-qasam for the oath in 103:1, matching the CRITICAL boundary rows.\",\"representative_source_ids\":[\"QG-d4fa0376\",\"QI-715bd831\",\"QB-794b4880\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:closure-and-sound-link","source_type":"word_analysis","support_id":"sup_10a1e09c762a44cc68d6","text":"{\"blocking_evidence\":null,\"headline\":\"loss is the closing landing\",\"reader_payoff\":\"The reader notices that the final loss noun is the ayah's semantic landing and also joins the r-ending chain across 103:1, 103:2, and 103:3.\",\"reason\":\"{{ar:خُسْرٍ}} ({{tr:khusrin}}) is the final lexical word of 103:2, and its ending aligns audibly with the surrounding ayah closures named in the CRITICAL rows.\",\"representative_source_ids\":[\"QT-db0a548e\",\"QE-d21d0cb3\",\"QP-75d6da0b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:1:audible-heavy-opening","source_type":"word_analysis","support_id":"sup_12656e2cecc7daba8ba5","text":"{\"blocking_evidence\":null,\"headline\":\"the opening sounds compressed\",\"reader_payoff\":\"The reader notices that the geminated nasal opening makes the emphatic particle feel vocally held before the human noun arrives.\",\"reason\":\"The surface form contains the doubled nūn in {{ar:إِنَّ}} ({{tr:inna}}), and the following {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) keeps the nasal sound near the particle-subject boundary.\",\"representative_source_ids\":[\"QF-ff958b31\",\"QP-67ffa817\",\"QP-c7fa9845\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:root-recurrence-specialized","source_type":"word_analysis","support_id":"sup_301610979788d717110e","text":"{\"blocking_evidence\":null,\"headline\":\"the root concentrates into a gerund\",\"reader_payoff\":\"The reader notices that a wider loss root field is concentrated here into a bare abstract gerund after {{ar:فِى}} ({{tr:fī}}).\",\"reason\":\"The local form is GERUND, and V4 sense groups support the broad accepted root field without requiring other derivatives to be locally active.\",\"representative_source_ids\":[\"QI-adc75c60\",\"QI-cf491dd7\",\"QE-76c2c5cb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:masdar-state-container","source_type":"word_analysis","support_id":"sup_34568a2e0df6a3dab4e2","text":"{\"blocking_evidence\":null,\"headline\":\"loss is a state, not an act\",\"reader_payoff\":\"The reader notices that {{ar:خُسْرٍ}} ({{tr:khusrin}}) names the condition enclosing humanity rather than calling the human a loser or narrating a losing event.\",\"reason\":\"The word is an abstract maṣdar in a prepositional predicate, and translation support warns against over-physicalizing the locative while preserving the state role.\",\"representative_source_ids\":[\"QG-c7c4d58a\",\"QS-6736a138\",\"QF-41e33a6e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4","source_type":"word_analysis","support_id":"sup_3d5708f3e9c3648cdc8d","text":"{\"gloss_range\":\"indefinite gerund of loss, deficiency, and ruin, locally serving as the genitive complement of fī in the emphatic predicate\",\"prose\":\"{{ar:خُسْرٍ}} ({{tr:khusrin}}) is the landing word of the verdict, and its form keeps the loss both asserted and unbounded. It is indefinite, so the clause does not point to a named, limited loss; the double emphasis pushes the reader to a final noun whose tanwīn refuses to define the boundary. As a maṣdar governed by {{ar:فِى}} ({{tr:fī}}), it names a state or condition inside which the human is placed, not an action of losing and not an active label such as loser. The root field supports more than a thin abstraction: deficiency, capital loss, deficient measure, ruin, perdition, and misdirection all press around the local sense, while grammar keeps the selected meaning as the abstract loss-state. Under the oath by time, that deficit field can feel like capital steadily diminished under pressure, not imported literal commerce. Its clipped standard surface also matters at the close, especially against the fuller variant {{ar:خُسُرٍ}} ({{tr:khusurin}}): the verdict lands compactly, while the fuller variant slows the noun and the reported expansion makes duration more explicit. Its final r links the endings of {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) (103:1), {{ar:خُسْرٍ}} ({{tr:khusrin}}) (103:2), and {{ar:ٱلصَّبْرِ}} ({{tr:al-ṣabr}}) (103:3). The word also creates forward pressure, because the exception in 103:3 answers the condition named here through faith, righteous action, and mutual counsel.\",\"root_display\":\"{{ar:خ س ر}} ({{tr:kh-s-r}})\",\"root_gloss_range\":\"accepted root range includes general deficiency, trade loss, deficient measure, spiritual ruin and perdition, and augmented loss/baseness forms; local grammar selects the abstract loss-state while allowing deficit and ruin pressure\",\"surface_display\":\"{{ar:خُسْرٍ}} ({{tr:khusrin}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:clipped-form-and-variants","source_type":"word_analysis","support_id":"sup_3f27105b39e3e21a6a9e","text":"{\"blocking_evidence\":null,\"headline\":\"the standard form lands clipped\",\"reader_payoff\":\"The reader notices that the standard clipped form closes the ayah sharply, while fuller readings expose the same loss sense with heavier acoustic weight.\",\"reason\":\"The canonical local surface is {{ar:خُسْرٍ}} ({{tr:khusrin}}); variant evidence can illuminate sound and weight, but it must not replace the standard reading.\",\"representative_source_ids\":[\"QF-63dc3ceb\",\"QF-e7b2908f\",\"QP-da44f9e8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:1","source_type":"word_analysis","support_id":"sup_44d73d4c94340f058b06","text":"{\"gloss_range\":\"emphatic particle opening the oath answer and governing the human-loss proposition\",\"prose\":\"{{ar:إِنَّ}} ({{tr:inna}}) does more than add general emphasis. It opens the answer to the oath by {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) (103:1), governs {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) as its accusative ism, and sends the clause toward the predicate {{ar:لَفِى خُسْرٍ}} ({{tr:la-fī khusrin}}). The reader therefore hears certainty before subject or loss is named: the ayah enters as a sworn declarative verdict, not as a neutral observation. Its force is then corroborated by the lām in {{ar:لَفِى}} ({{tr:la-fī}}), so the assertion is stacked at both the opening and the predicate. Even the written shaddah and doubled n-sound of {{ar:إِنَّ}} ({{tr:inna}}) make the opening visibly and vocally heavy before the nasal sound binds into the following human noun.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِنَّ}} ({{tr:inna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"103:2:4:1","source_type":"qac_morpheme","support_id":"sup_4613dce73b9ff08d752b","text":"{\"lemma_ar\":\"خُسْر\",\"morph_features\":\"STEM|POS:N|LEM:xusor|ROOT:xsr|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"103:2:4:1\",\"qac_word_ref\":\"103:2:4\",\"root_ar\":\"خ س ر\",\"surface_ar\":\"خُسْرٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:1:double-emphasis-frame","source_type":"word_analysis","support_id":"sup_60536bf6330f72c285d7","text":"{\"blocking_evidence\":null,\"headline\":\"opening emphasis is corroborated\",\"reader_payoff\":\"The reader notices that the loss claim is confirmed twice, first by {{ar:إِنَّ}} ({{tr:inna}}) and then by the predicate lām in {{ar:لَفِى}} ({{tr:la-fī}}).\",\"reason\":\"The word table and translation support both flag the paired emphatic force of {{ar:إِنَّ}} ({{tr:inna}}) and the lām attached to the predicate.\",\"representative_source_ids\":[\"QI-e15043a1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"103:2:2:2","source_type":"qac_morpheme","support_id":"sup_61693beebd12863aaa1c","text":"{\"lemma_ar\":\"إِنسَٰن\",\"morph_features\":\"STEM|POS:N|LEM:<insa`n|ROOT:Ans|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"103:2:2:2\",\"qac_word_ref\":\"103:2:2\",\"root_ar\":\"ء ن س\",\"surface_ar\":\"إِنسَٰنَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:generic-species-scope","source_type":"word_analysis","support_id":"sup_6866d62f4b1328019b32","text":"{\"blocking_evidence\":null,\"headline\":\"one noun carries the species\",\"reader_payoff\":\"The reader notices that the singular definite noun makes the verdict broad enough for the exception in 103:3 to matter.\",\"reason\":\"QAC marks the article as generic for the human species, and attachment translation support warns that the immediately following exception in 103:3 constrains the broad statement.\",\"representative_source_ids\":[\"QG-0b183c6e\",\"QF-971e23eb\",\"QI-c73e3401\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:deficit-ruin-root-field","source_type":"word_analysis","support_id":"sup_7e1cc1f94bc8c4e9a0f1","text":"{\"blocking_evidence\":null,\"headline\":\"deficit and ruin load the loss\",\"reader_payoff\":\"The reader notices that the local word for loss carries deficit, diminished capital, deficient measure, and ruin pressure under the oath by time in 103:1.\",\"reason\":\"V4 accepts deficiency, trade loss, deficient measure, and ruin branches for {{ar:خ س ر}} ({{tr:kh-s-r}}), but the local maṣdar under {{ar:فِى}} ({{tr:fī}}) selects an abstract loss-state rather than literal commerce or weighing.\",\"representative_source_ids\":[\"QS-22b3ab87\",\"QS-5c8d7f98\",\"QY-7307f8fc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:social-forgetful-derivation","source_type":"word_analysis","support_id":"sup_7e52a93bb49f1df92d34","text":"{\"blocking_evidence\":null,\"headline\":\"sociality and forgetfulness create tension\",\"reader_payoff\":\"The reader notices that the subject can carry social and forgetful pressure, making the mutual-counsel exception in 103:3 lexically apt.\",\"reason\":\"The local alignment selects {{ar:أ ن س}} ({{tr:ʾ-n-s}}), so forgetfulness must not replace the local root; it survives only as a classical derivational tension joined to the forward exception in 103:3.\",\"representative_source_ids\":[\"QS-0b486b8c\",\"MS-fd442c03\",\"QY-c3cdd788\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:sound-thread","source_type":"word_analysis","support_id":"sup_8b386b837c042c9743e6","text":"{\"blocking_evidence\":null,\"headline\":\"sound binds subject to predicate\",\"reader_payoff\":\"The reader notices an audible thread from nasal assertion into the sibilant pressure of the human-loss clause.\",\"reason\":\"The local surfaces support the row's limited sound observation across {{ar:إِنَّ}} ({{tr:inna}}), {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}), and {{ar:خُسْرٍ}} ({{tr:khusrin}}).\",\"representative_source_ids\":[\"QP-16f1e665\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:governed-standing-condition","source_type":"word_analysis","support_id":"sup_8eb32ba7a51e32865f14","text":"{\"blocking_evidence\":null,\"headline\":\"humanity receives the predicate\",\"reader_payoff\":\"The reader notices that the human noun is governed inside a nominal verdict of condition, not presented as the agent of a losing action.\",\"reason\":\"The grammar identifies {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) as accusative ism of {{ar:إِنَّ}} ({{tr:inna}}), with the prepositional phrase as the predicate.\",\"representative_source_ids\":[\"QG-5288a0dc\",\"QG-d38691f7\",\"QS-20ef5db1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:1:governed-emphatic-proposition","source_type":"word_analysis","support_id":"sup_958f839ed435975df403","text":"{\"blocking_evidence\":null,\"headline\":\"emphasis governs the whole claim\",\"reader_payoff\":\"The reader notices that {{ar:إِنَّ}} ({{tr:inna}}) asserts and governs the whole human-loss proposition rather than merely decorating the opening.\",\"reason\":\"QAC and attachment evidence identify an inna clause in which {{ar:إِنَّ}} ({{tr:inna}}) governs {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) and takes {{ar:لَفِى خُسْرٍ}} ({{tr:la-fī khusrin}}) as its predicate.\",\"representative_source_ids\":[\"QG-80dff681\",\"QS-07f993c3\",\"QT-5e35cb78\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:forward-exception-pressure","source_type":"word_analysis","support_id":"sup_98dfca46560686209a24","text":"{\"blocking_evidence\":null,\"headline\":\"loss demands the exception\",\"reader_payoff\":\"The reader notices that the loss verdict is not sealed off; it creates the need answered by the exception chain in 103:3.\",\"reason\":\"Attachment translation support says the next ayah's exception takes scope from this general clause, so the loss predicate must be read with 103:3 in view.\",\"representative_source_ids\":[\"QE-071ad4ac\",\"QB-b929ff72\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:3:predicate-lam-emphasis","source_type":"word_analysis","support_id":"sup_9a81e847552de4cede38","text":"{\"blocking_evidence\":null,\"headline\":\"the lām lands on the predicate\",\"reader_payoff\":\"The reader notices that the emphatic load reaches the predicate itself through the shifted lām, completing the {{ar:إِنَّ}} ({{tr:inna}})...lām frame.\",\"reason\":\"The word table identifies the lām as the predicate lām in the double-emphasis construction, and translation support warns against treating it as an ordinary particle.\",\"representative_source_ids\":[\"QG-a58201e4\",\"QI-770d3573\",\"QT-f8da726d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:3:temporal-to-spatial-boundary","source_type":"word_analysis","support_id":"sup_9ee014b6ac4f3b5792e0","text":"{\"blocking_evidence\":null,\"headline\":\"time pressure becomes location\",\"reader_payoff\":\"The reader notices that the oath by time in 103:1 is answered by a spatial containment phrase in 103:2.\",\"reason\":\"The local word carries both the predicate lām tied to the oath answer and {{ar:فِى}} ({{tr:fī}}), whose containment force shapes the verdict.\",\"representative_source_ids\":[\"QB-6d552d63\",\"QY-3ce456f3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:3:fused-compact-surface","source_type":"word_analysis","support_id":"sup_ae58052ec008f27d83b9","text":"{\"blocking_evidence\":null,\"headline\":\"two mechanisms are compressed\",\"reader_payoff\":\"The reader notices that corroboration and containment are not spaced out; they are fused into the compact predicate opener.\",\"reason\":\"The local surface combines the bound lām and {{ar:فِى}} ({{tr:fī}}), and the following noun is immediately governed by that preposition.\",\"representative_source_ids\":[\"QF-50e07ddd\",\"QF-8da3ddf6\",\"QP-7eb2f9fd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:oath-to-human-verdict","source_type":"word_analysis","support_id":"sup_dadfeb58115e113a6fc1","text":"{\"blocking_evidence\":null,\"headline\":\"time witness turns human\",\"reader_payoff\":\"The reader notices the register shift from the oath by time in 103:1 into an anthropological verdict in 103:2.\",\"reason\":\"The previous oath is answered by the current inna clause, and {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) is the named subject of that answer.\",\"representative_source_ids\":[\"QB-ebbabf26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2:human-loss-root-pair","source_type":"word_analysis","support_id":"sup_dbbc932cd406cb566813","text":"{\"blocking_evidence\":null,\"headline\":\"human and loss form a marked pair\",\"reader_payoff\":\"The reader notices that the subject-predicate relation belongs to a cited Quranic pattern where human language and loss language meet in judgment contexts (22:11, 46:18, 41:25).\",\"reason\":\"The CRITICAL rows give concrete recurrence references, while contextual evidence confirms {{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) as a broad human referent; the topic is kept as recurrence payoff, not as a new local sense.\",\"representative_source_ids\":[\"QI-1ebb5146\",\"QI-47d1ed50\",\"QI-7b450101\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:3","source_type":"word_analysis","support_id":"sup_f0f025c485b2ca75919d","text":"{\"gloss_range\":\"fused predicate lām plus fī, combining corroborating emphasis with containment in the khabar\",\"prose\":\"{{ar:لَفِى}} ({{tr:la-fī}}) is the predicate hinge where emphasis and containment arrive in one surface word. The lām corroborates the opening {{ar:إِنَّ}} ({{tr:inna}}), shifted onto the predicate because the opening position is already occupied, while {{ar:فِى}} ({{tr:fī}}) governs {{ar:خُسْرٍ}} ({{tr:khusrin}}) and makes loss the environment in which the human is placed. That means the clause does not merely say that humanity has loss; it locates the human category inside an abstract state. The fused spelling also compresses the two mechanisms, so the predicate begins as a tight audible unit before the loss noun lands. Across the ayah boundary, this word helps turn the oath by {{ar:ٱلْعَصْرِ}} ({{tr:al-ʿaṣr}}) (103:1) into a spatial diagnosis: time is sworn by, then loss is named as the containing space.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَفِى}} ({{tr:la-fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:2","source_type":"word_analysis","support_id":"sup_f14e092991a88c603ad6","text":"{\"gloss_range\":\"definite singular species noun, accusative as the ism of inna, naming humankind as the subject of the loss verdict\",\"prose\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}}) is singular and definite, so one noun gathers the human species under the verdict before 103:3 carves out the exception. The definiteness makes the scope question visible as a class statement that the next ayah later partitions. Its accusative case makes it the governed ism of {{ar:إِنَّ}} ({{tr:inna}}), not an independent actor doing a verb; the clause places humanity inside a standing condition. The lexical pressure is also not flat. The local QAC root is {{ar:أ ن س}} ({{tr:ʾ-n-s}}), with sociality, familiarity, and perception in view, while the classical derivational dispute with forgetfulness can survive only as a narrowed tension, not as a replacement of the aligned root. That tension matters because the exception in 103:3 names faith, righteous action, and mutual counsel: the social, forgetful human is answered by an action-defined community. The sound also participates in the frame, as nasal assertion passes into the human noun and the sibilant pressure then ties the human noun toward loss. The preceding oath by time therefore turns immediately into an anthropological verdict, not an isolated oath formula. The subject also belongs to a wider Quranic human-loss pairing, with cited judgment contexts at 22:11, 46:18, and 41:25, so this short ayah concentrates a known association into one subject-predicate frame.\",\"root_display\":\"{{ar:أ ن س}} ({{tr:ʾ-n-s}})\",\"root_gloss_range\":\"root field of human sociality, familiarity, and perception; a classical derivational dispute also lets forgetfulness pressure remain as a narrowed lexical tension\",\"surface_display\":\"{{ar:ٱلْإِنسَٰنَ}} ({{tr:al-insāna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:unbounded-indefinite-loss","source_type":"word_analysis","support_id":"sup_fb20b0328bb5218b6951","text":"{\"blocking_evidence\":null,\"headline\":\"the loss remains unbounded\",\"reader_payoff\":\"The reader notices that the emphatic verdict ends in an indefinite noun, so the asserted loss remains vast and unspecified.\",\"reason\":\"QAC marks {{ar:خُسْرٍ}} ({{tr:khusrin}}) as indefinite and governed by {{ar:فِى}} ({{tr:fī}}), supporting unbounded loss inside the emphatic predicate.\",\"representative_source_ids\":[\"QG-37fc6462\",\"QF-2fb25037\",\"QY-6f3ca6cc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"103:2:4:human-loss-recurrence","source_type":"word_analysis","support_id":"sup_fc6df446a0152c333eda","text":"{\"blocking_evidence\":null,\"headline\":\"the human-loss pair recurs\",\"reader_payoff\":\"The reader notices that this compact predicate belongs to a cited Quranic field where human reference and loss language meet in judgment contexts (22:11, 46:18, 41:25).\",\"reason\":\"The CRITICAL rows provide concrete recurrence references, and the contextual profiles support a human-referent setting for the local loss predicate.\",\"representative_source_ids\":[\"QI-903dc736\",\"QI-fbcdd6c6\",\"QY-0ace1c76\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ","ayah_ref":"103:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000409/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000059","role":"Makes the subject visible human presence as a class, giving the claim an anthropological rather than incident-specific scope.","root":"ء ن س","source_ref":"103:2","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000409","role":"Supplies broad diminution as the condition that spatially surrounds the human subject.","root":"خ س ر","source_ref":"103:2","source_word_indices":["4"]}],"changed_reading":{"after":"The human, precisely as manifest human presence, is emphatically situated inside an encompassing condition of diminution.","before":"Humans sometimes suffer losses."},"confidence":"strong","focus_anchor":"The generic human noun, paired emphatic particles, and the locative construction placing the subject 'in' loss.","mechanism":"Manifest human presence is not described as merely undergoing an isolated setback; the locative construction embeds humanity inside broad diminution as its encompassing default condition.","model_id":"baseline_encompassing_deficit"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_encompassing_deficit","source_type":"hft","support_id":"sup_fb369d0ac1a3794876b1","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ","ayah_ref":"103:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B001","root_000409/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000059","role":"Provides the lived human presence treated, by analogy, as the capital exposed in the account.","root":"ء ن س","source_ref":"103:2","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000409","role":"Activates loss of capital or absent profit, turning the state into an accounting mechanism.","root":"خ س ر","source_ref":"103:2","source_word_indices":["4"]}],"changed_reading":{"after":"Human existence reads as a running account whose committed capital is being spent without adequate return.","before":"Loss is undifferentiated harm."},"confidence":"medium","focus_anchor":"The generic human subject is placed inside the indefinite loss noun, whose inventory includes an unprofitable transaction.","mechanism":"Human presence can be modeled as capital already committed to a running transaction. Being 'in loss' then means not only deprivation but a life-account in which principal is consumed or no adequate return appears.","model_id":"baseline_unprofitable_human_account"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_unprofitable_human_account","source_type":"hft","support_id":"sup_329b406a8e841fffa9c2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِنَّ ٱلْإِنسَٰنَ لَفِى خُسْرٍ","ayah_ref":"103:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000059/B002","root_000409/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000059","role":"Foregrounds the human as a perceiving and detecting being rather than only a biological class.","root":"ء ن س","source_ref":"103:2","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000409","role":"Introduces under-measurement, making deficiency a failure of measure as well as a suffered result.","root":"خ س ر","source_ref":"103:2","source_word_indices":["4"]}],"changed_reading":{"after":"The perceiving human is constituted within short measure: what the human apprehends, values, or renders may already be deficient.","before":"A neutral human subject later incurs an external loss."},"confidence":"exploratory","focus_anchor":"The human root can foreground perception and the loss root can foreground deficient measure; both remain attached to the two lexical anchors of the focus ayah.","mechanism":"The being that senses and brings things into awareness is itself enclosed in short measure. The deficit can therefore occur within apprehension and valuation: the human may perceive, assess, or render less than the whole.","model_id":"baseline_short_measure_of_awareness"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_short_measure_of_awareness","source_type":"hft","support_id":"sup_a61478b7b22aee44dda8","trust":"legacy_unbound"}]}
</lane_packet_json>
