# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:18**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_18/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:18",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:18","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Geçici bir karşılaşma yeterli değildir; anlam, görece sürekli eşlik veya yakın birliktelik gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000844/B001","candidate_links":[{"candidate_id":"cand_04fd5b234f3dc5ca3b01","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"süreğen eşlik ve yakın birliktelik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek, iki tarafın yakın ve süreğen biçimde birlikte bulunması ya da birinin ötekine eşlik etmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eşlik eden taraf kişi, hayvan, yer veya zamanla ilişkili olabilir; tekil eşlikçi ve eşlikçiler topluluğu da adlandırılabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli ad tamlamalarında bir şeyin sahibi, ona bağlı kişi veya onun işini yürüten sorumlu kastedilir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişinin yanında kendisine eşlik eden birinin bulunması da bu anlam alanının yapıya bağlı uzantısıdır."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Geçici buluşmayı değil, birine veya bir şeye eşlik etme ve onunla birlikte kalma çekirdeğini karşılar.","boundary_detail":"Geçici bir karşılaşma yeterli değildir; anlam, görece sürekli eşlik veya yakın birliktelik gerektirir.","branch_image_ar":"الصُّحبة والملازمة","concept_gloss":"süreğen eşlik ve yakın birliktelik","contextual_glosses":[{"applicability":"Bir kişi ya da şeyle süren beraberliği fiil olarak anlatan genel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birlikte bulunma ile eşlik etme eylemini korur."},"facet_ids":["F001"],"text":"birlikte bulunmak ve eşlik etmek","usage_role":"general"},{"applicability":"Bir varlığa, topluluğa ya da yöneticiye bağlanan görev ve sahiplik yapılarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapıya bağlı sahiplik ve sorumluluk uzantısını korur."},"facet_ids":["F003"],"text":"sahibi veya işinden sorumlu kişi","usage_role":"contextual"}],"definition":"Bir kişi ya da şeyle geçici olmayan biçimde birlikte bulunmak, ona eşlik etmek veya onunla yakınlığını sürdürmektir. Belirli yapılarda bir şeyin sahibi ya da sorumlusu olmayı ve kişinin yanında bir eşlikçi bulunmasını da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek, iki tarafın yakın ve süreğen biçimde birlikte bulunması ya da birinin ötekine eşlik etmesidir."},{"facet_id":"F002","role":"specialization","statement":"Eşlik eden taraf kişi, hayvan, yer veya zamanla ilişkili olabilir; tekil eşlikçi ve eşlikçiler topluluğu da adlandırılabilir."},{"facet_id":"F003","role":"extension","statement":"Belirli ad tamlamalarında bir şeyin sahibi, ona bağlı kişi veya onun işini yürüten sorumlu kastedilir."},{"facet_id":"F004","role":"extension","statement":"Bir kişinin yanında kendisine eşlik eden birinin bulunması da bu anlam alanının yapıya bağlı uzantısıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyin başka bir şeyle yakın ve süreğen biçimde birlikte bulunmasını çekirdek anlam olarak verir. Kişi, hayvan, yer ve zamanla kurulan eşlik ilişkisi bu çekirdeğe girerken sahiplik, bir işin başında bulunma ve yanında bir eşlikçi bulunması belirli yapılara bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"eşlik etmek veya birlikte bulunmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sürekli eşlik eden kimse veya yoldaş"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"eşlik edenler topluluğu veya yoldaşlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"eşlik etme ve birlikte bulunma durumu"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"karşılıklı ve süreğen biçimde birlikte bulunma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeyin sahibi veya o şeye sahip kişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir topluluğun ya da yöneticinin işini yürüten görevli"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"ey arkadaşım"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"iyi ve istekli biçimde arkadaşlık eden"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yanında bir eşlikçisi bulunmak"}],"lexicalization_note":"Tanım, yalın eşlik çekirdeği ile sahiplik, görev ve bir eşlikçisi bulunma gibi yapıya bağlı kullanımları ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en güçlü karışma olasılıkları eşlik, sevgiye dayalı arkadaşlık ve karışma alanlarında bulundu, kalan adaylar daha uzak ya da bu ayrımları yineleyen örneklerdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı daha genel bir süreğen eşlik ilişkisi kurar; komşu dal ise tarafların birbirine eş olarak bağlanmasını veya bir eşlikçinin kişiye bağlanmasını belirginleştirir.","focus_only":"Odak dalı eşliğin yanında kişi dışındaki varlıklarla süreğen birlikteliği ve yapıya bağlı sahiplik ile sorumluluk uzantılarını da kapsar.","gloss":"birbirine bağlanmış eşlikçiler","neighbor_only":"Komşu dal özellikle birbirine bağlanmış eşleri, eşi ve insana bağlanan ya da onun buyruğuna verilen eşlikçileri öne çıkarır.","neighbor_ref":"root_001221/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir tarafın başka bir tarafla birlikte bulunması ve ona eşlik etmesi vardır."},{"boundary_match":"partial","distinction":"Odak dalı için sürekli birlikte bulunma yeterlidir; komşu dal bu birlikteliğe sevgi ve gönül yakınlığı koşulu ekler.","focus_only":"Odak dalındaki eşlik, sevgi bağı bulunmadan da kişi, hayvan, yer veya zamanla kurulabilir.","gloss":"sevgiye dayalı yakın arkadaşlık","neighbor_only":"Komşu dal, arkadaşlığı sevgi, yakınlık ve içten bağlılıkla birlikte sınırlar.","neighbor_ref":"root_000676/B003","relation_type":"near_synonym","shared_zone":"İki dal da yakın ilişki içindeki kişilerin birbirine eşlik etmesini anlatır."},{"boundary_match":"partial","distinction":"Eşlik, tarafların ayrı kimliğini koruyarak birlikte bulunmasıdır; karışma dalı ise iç içe geçme veya ortak mal ilişkisine kadar uzanır.","focus_only":"Odak dalının çekirdeği, tarafların birbirine karışması değil, birinin ötekine eşlik ederek yakın kalmasıdır.","gloss":"karışma, ortaklık ve yakın temas","neighbor_only":"Komşu dal insan ilişkilerinin yanında malların birbirine karışmasını ve ortaklık düzenlemelerini de kapsar.","neighbor_ref":"root_000431/B002","relation_type":"near_neighbor","shared_zone":"İnsanların yakın temasta bulunması ve bir ilişkiyi paylaşması iki alanın kesiştiği noktadır."}],"source_phrase_ar":"أصل واحد يدل على مقارنة شيء ومقاربته (maqayis)؛ الصاحب يجمع بالصحب والصحبان والصحبة والصحاب والأصحاب (ayn)؛ الصحب والصحاب والأصحاب والصحابة واحد (jamhara)؛ صحبه يصحبه صحبة وصحابة وجمع الصاحب صحب (sihah)؛ الصاحب الملازم إنسانا كان أو حيوانا أو مكانا أو زمانا (mufradat)؛ المصاحبة والاصطحاب أبلغ من الاجتماع (mufradat)؛ يقال للمالك للشيء هو صاحبه (mufradat)؛ وأصحب الرجل إذا كان ذا صاحب (ayn)","source_summary":"Kaynakların ortak çizgisi, sıradan bir araya gelmeden daha güçlü olan yakın ve sürekli eşliktir; kişi adları, topluluk adları, sahiplik ve sorumluluk kullanımları bu çekirdeğin çevresinde yer alır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الصاحب والصحب والصحابة والمصاحبة والاصطحاب والملازمة وكون المرء ذا صاحب وذو الشيء أو القائم عليه","what_is_not_ar":"ليس مجرد اجتماع عابر بلا ملازمة"},"support_links":["sup_8c1771c59d9dbffb6dba"]},{"boundary":"Dal, koruma dilekleri ve eşlik ederek destek olma bağlamlarıyla sınırlıdır; genel arkadaşlık anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000844/B002","candidate_links":[{"candidate_id":"cand_92fb5a8e6344a4e767a0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"eşlik eden koruma ve destek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kimsenin kendisine eşlik eden bir gözetim ve destek yoluyla korunması çekirdeği oluşturur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dinginlik, iç güç ve yumuşak desteğin bir kimseye ulaşıp ona eşlik etmesi koruyucu sonucun uzantısıdır."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Korumanın veya iç rahatlatan desteğin kişiye eşlik ettiği dalın bütün çekirdeği için kullanılır.","boundary_detail":"Dal, koruma dilekleri ve eşlik ederek destek olma bağlamlarıyla sınırlıdır; genel arkadaşlık anlamına genişletilmez.","branch_image_ar":"الحفظ بالمصاحبة","concept_gloss":"eşlik eden koruma ve destek","contextual_glosses":[{"applicability":"Bir kimse için koruma dilendiğinde veya korunduğu bildirildiğinde doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koruma ve gözetme sonucunu doğrudan korur."},"facet_ids":["F001"],"text":"koruyup gözetmek","usage_role":"contextual"},{"applicability":"Kişiye dinginlik, iç güç veya yumuşak yardımın eşlik ettiği bağlamları açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İç rahatlatan ve güç veren destek uzantısını korur."},"facet_ids":["F002"],"text":"dinginlik ve destek vermek","usage_role":"explanatory"}],"definition":"Bir kimseyi eşlik eden bir gözetimle korumak veya ona dinginlik, iç güç ve yumuşak destek ulaştırmaktır. Anlam özellikle koruma dileklerinde ve bu tür desteğin kişiye eşlik ettiği bağlamlarda gerçekleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kimsenin kendisine eşlik eden bir gözetim ve destek yoluyla korunması çekirdeği oluşturur."},{"facet_id":"F002","role":"extension","statement":"Dinginlik, iç güç ve yumuşak desteğin bir kimseye ulaşıp ona eşlik etmesi koruyucu sonucun uzantısıdır."}],"identity_rationale":"Kaynak ifadesi, eşlik düşüncesini koruma sonucuna taşıyan kullanımları açıkça bir araya getirir. Bir kimsenin korunması ile ona eşlik eden dinginlik, iç güç ve yumuşak destek aynı koruyucu eşlik çerçevesinde yer alır; bu anlam sıradan iki kişilik arkadaşlık değildir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı seni korusun"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Tanrı onu korumasın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"korunmak veya dinginlik ve destek görmek"}],"lexicalization_note":"Koruma dileği bildiren kalıp sözler ile birine dinginlik ve destek eşlik etmesini anlatan bağlama bağlı kullanım ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel koruma dalları ve kökün eşlik dalı sınırı en iyi açıklayan karşılaştırmalardır, merhamet ve sığınak adayları ise daha dolaylıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında koruma eşlik eden bir yardım gibi kavranır; komşu dalda ise koruma ve bekçilik bağımsız eylem ve görevlerdir.","focus_only":"Odak dalı korumayı kişiye eşlik eden gözetim, dinginlik ve destek çerçevesinde sunar.","gloss":"genel koruma ve bekçilik","neighbor_only":"Komşu dal genel korumayı, bekçiliği, sakınmayı ve bir yeri ya da yöneticiyi gözeten kişileri kapsar.","neighbor_ref":"root_000307/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak sonucu bir kişi ya da şeyin zarardan korunmasıdır."},{"boundary_match":"partial","distinction":"Odak dalı eşlik yoluyla korumaya ve ruhsal desteğe bağlıdır; komşu dal sürekli bakım ve önlem alma yönünden daha geniştir.","focus_only":"Odak dalı, korunana dinginlik ve iç destek eşlik etmesi gibi sonuçları da içerir.","gloss":"koruma, bakım ve önlem","neighbor_only":"Komşu dal, bir şeyi düzenli gözetme, bakımını sürdürme, önlem alma ve onu çevreleyerek koruma kapsamına uzanır.","neighbor_ref":"root_000372/B002","relation_type":"near_synonym","shared_zone":"Bir varlığı gözetip zarar görmesini engelleme anlamı iki dalda da bulunur."},{"boundary_match":"partial","distinction":"Bu dal eşliği koruyucu bir işleve bağlar; komşu dal ise işlevden bağımsız olarak süreğen birlikteliği anlatır.","focus_only":"Odak dalında eşlik, koruma veya iç destek sağlayan bir sonuç doğurur.","gloss":"süreğen eşlik ve birliktelik","neighbor_only":"Komşu dalda birlikte bulunma kendi başına yeterlidir ve koruma sonucu zorunlu değildir.","neighbor_ref":"root_000844/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir kişiyle birlikte kalma veya ona eşlik etme düşüncesi vardır."}],"source_phrase_ar":"صحبك الله أي حفظك (ayn)؛ صحبه الله وأصحبه وصاحبه أي حفظه (jamhara)؛ لا يكون لهم من جهتنا ما يصحبهم من سكينة وروح وترفيق (mufradat)","source_summary":"Kaynaklar koruma anlamında birleşir; toplu kanıt, doğrudan koruma dileğinin yanında kişiye eşlik eden dinginlik, iç güç ve yumuşak desteği de aynı çerçevede gösterir.","sources":["AY","JA","MU"],"what_is_ar":"صحبه الله وأصحبه وصاحبه بمعنى حفظه وما يصحب الإنسان من سكينة وروح وترفيق","what_is_not_ar":"ليس الصحبة المجردة بين شخصين"},"support_links":["sup_b0b3565f14a959742289"]},{"boundary":"Çekirdek, gönüllü ya da dirençten sonra ortaya çıkan uyma durumudur; salt arkadan gitme veya eşlik ettirme değildir.","branch_kind":"bare","branch_ref":"root_000844/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"boyun eğip uyumlu duruma gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi veya hayvanın boyun eğmesi, uyum göstermesi ve dirençten sonra yönetilebilir duruma gelmesi çekirdektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kimsenin ardından boyun eğmiş ve uyumlu biçimde gitmek çekirdeğin izleme bağlamındaki gerçekleşmesidir."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi veya hayvanın direnç göstermeyi bırakıp uyması ve yönetilebilir olması çekirdeğini karşılar.","boundary_detail":"Çekirdek, gönüllü ya da dirençten sonra ortaya çıkan uyma durumudur; salt arkadan gitme veya eşlik ettirme değildir.","branch_image_ar":"الإصحاب والانقياد","concept_gloss":"boyun eğip uyumlu duruma gelme","contextual_glosses":[{"applicability":"Önceden zorluk çıkaran kişi veya hayvanın sonradan uyduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki direncin ardından gelen boyun eğmeyi korur."},"facet_ids":["F001"],"text":"direncini bırakıp boyun eğmek","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini uymuş durumda izlediği özel bağlamı karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İzleme eylemini ve izleyenin boyun eğmiş durumunu korur."},"facet_ids":["F002"],"text":"boyun eğerek ardından gitmek","usage_role":"contextual"}],"definition":"Bir kişi ya da hayvanın boyun eğerek uyması, kimi durumda önceki güçlüğü veya direnci bırakarak izler duruma gelmesidir. Bir kimsenin ardından gitme kullanımı da izleyenin bu uymuş durumunu içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi veya hayvanın boyun eğmesi, uyum göstermesi ve dirençten sonra yönetilebilir duruma gelmesi çekirdektir."},{"facet_id":"F002","role":"specialization","statement":"Bir kimsenin ardından boyun eğmiş ve uyumlu biçimde gitmek çekirdeğin izleme bağlamındaki gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi insan veya hayvanın boyun eğmesi, uyması ve kimi bağlamlarda önceki güçlüğün ardından yumuşayıp izler duruma gelmesi üzerinde birleşir. Bir kişiyi izleme örneği de izleyenin boyun eğmiş olması koşulunu korur; bu dal bir başkasını eşlikçi kılma anlamından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"boyun eğmek ve güçlükten sonra uyumlu duruma gelmek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir kimsenin ardından boyun eğerek gitmek"}],"lexicalization_note":"Tanım yalın dalın boyun eğme ve uyma çekirdeğiyle sınırlıdır; başka yapılardaki eşlik veya koruma anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel söz dinleme ve dışarıdan uysallaştırma dalları gerçek sınır farklarını gösterir, kalan adaylar yalnızca aynı senaryoya uzaktan katılır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı dirençten sonraki yumuşamayı ve izleme bağlamını belirginleştirir; komşu dal genel söz dinleme durumuna daha geniş yer verir.","focus_only":"Odak dalı özellikle önceki güçlükten sonra uyumlu duruma gelmeyi ve bu halde birini izlemeyi kapsar.","gloss":"boyun eğme ve söz dinleme","neighbor_only":"Komşu dal boyun eğme, uyma ve hızlıca söz dinleme durumunu daha genel biçimde anlatır.","neighbor_ref":"root_000514/B001","relation_type":"near_synonym","shared_zone":"İki dalda da öznenin karşı koymayı bırakıp başka bir iradeye uyması vardır."},{"boundary_match":"partial","distinction":"Odak dalındaki uyma çoğu kez direncin sona ermesiyle görünür; komşu dal uysallığı ve emre bağlılığı daha genel olarak adlandırır.","focus_only":"Odak dalı, bir hayvanın güçlükten sonra yönetilebilir olması gibi belirli bir durum değişikliğini öne çıkarır.","gloss":"isteyerek uyma ve söz dinleme","neighbor_only":"Komşu dal emre uyma, söz dinleme ve el, dizgin ya da dil altında kolayca yönelme kapsamını taşır.","neighbor_ref":"root_000956/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın merkezinde bir buyruğa veya yönlendirmeye karşı koymadan uyma bulunur."},{"boundary_match":"partial","distinction":"Odak dalı ortaya çıkan boyun eğme durumudur; komşu dal ise bu durumu meydana getiren eğitme ve yumuşatma sürecidir.","focus_only":"Odak dalı boyun eğmiş ve uyumlu hale gelmiş öznenin durumunu bildirir.","gloss":"eğiterek uysallaştırma","neighbor_only":"Komşu dal bir insanı veya hayvanı eğitip sertliğini gidererek uysallaştıran dış müdahaleyi anlatır.","neighbor_ref":"root_001200/B002","relation_type":"near_neighbor","shared_zone":"Her iki alanda da dirençli bir kişi ya da hayvanın daha kolay yönetilir hale gelmesi söz konusudur."}],"source_phrase_ar":"أصحب فلان إذا انقاد (maqayis)؛ أصحبت الرجل إذا اتبعته منقادا (jamhara)؛ أصحب البعير والدابة إذا انقاد بعد صعوبة (sihah)؛ الإصحاب للشيء الانقياد له (mufradat)","source_summary":"Kaynaklar boyun eğip uyma çekirdeğinde birleşir; hayvan örneği önceki güçlüğün aşılmasını, kişi örneği ise uymuş durumda birinin ardından gitmeyi belirginleştirir.","sources":["MQ","JA","SI","MU"],"what_is_ar":"الإصحاب للشيء والانقياد له واتباع الرجل أو الدابة بعد صعوبة","what_is_not_ar":"ليس جعل الشيء صاحبا لغيره ولا الحفظ"},"support_links":[]},{"boundary":"Dal, eşlik ilişkisini kurma, yanında götürme veya uygun düşme ile sınırlıdır; yalnızca aynı yerde bulunmayı anlatmaz.","branch_kind":"bare","branch_ref":"root_000844/B004","candidate_links":[{"candidate_id":"cand_e593f23cda67de7e3223","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"eşlikçi kılmak, yanında götürmek veya uygun düşmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyi başka birinin eşlikçisi durumuna getirmek temel işlemdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kitap gibi bir nesneyi yanına alıp beraberinde götürmek bu işlemin somut gerçekleşmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İki şeyin birbirine uygun düşmesi ve böylece birlikte kalabilmesi eşlik bağının durum uzantısıdır."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bir eşlik bağı kuran işlemlerini ve bu bağı mümkün kılan uygunluk görünümünü birlikte karşılar.","boundary_detail":"Dal, eşlik ilişkisini kurma, yanında götürme veya uygun düşme ile sınırlıdır; yalnızca aynı yerde bulunmayı anlatmaz.","branch_image_ar":"جعل الشيء مصاحبا واستصحابه","concept_gloss":"eşlikçi kılmak, yanında götürmek veya uygun düşmek","contextual_glosses":[{"applicability":"Bir kişi veya şeyin başka birine eşlikçi yapıldığı geçişli bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eşlik ilişkisini kuran geçişli işlemi korur."},"facet_ids":["F001"],"text":"birine eşlikçi vermek","usage_role":"contextual"},{"applicability":"Kitap veya başka bir nesnenin kişiyle birlikte götürüldüğü bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneyi yanında taşıma ve birlikte götürme işlemini korur."},"facet_ids":["F002"],"text":"yanına alıp götürmek","usage_role":"contextual"},{"applicability":"İki şeyin bağdaşarak birlikte kalabildiği uygunluk bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bağdaşma ve birlikte kalabilme durumunu korur."},"facet_ids":["F003"],"text":"birbirine uygun düşmek","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye eşlikçi kılmak veya bir nesneyi yanına alıp birlikte götürmektir. İki şeyin birbirine uygun düşerek birlikte kalabilmesi de bu eşlik bağının durum bildiren görünümüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyi başka birinin eşlikçisi durumuna getirmek temel işlemdir."},{"facet_id":"F002","role":"specialization","statement":"Kitap gibi bir nesneyi yanına alıp beraberinde götürmek bu işlemin somut gerçekleşmesidir."},{"facet_id":"F003","role":"extension","statement":"İki şeyin birbirine uygun düşmesi ve böylece birlikte kalabilmesi eşlik bağının durum uzantısıdır."}],"identity_rationale":"Kaynak ifadesi üç bağlı görünümü destekler: bir şeyi başka bir şeye eşlikçi kılmak, bir nesneyi yanında götürmek ve iki şeyin birlikte kalabilecek ölçüde birbirine uygun düşmesi. Bunların tümünde bir şeyin ötekine katılması veya onunla bağdaşarak eşlik etmesi korunur; boyun eğme anlamı bu dalda yoktur.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şeyi ona eşlikçi kılmak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kitabı veya başka bir şeyi yanına alıp götürmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ona uygun düşmek ve onunla bağdaşmak"}],"lexicalization_note":"Tanım yalın dalın eşlikçi kılma, yanında götürme ve uygun düşme görünümlerini kapsar; yapıya bağlı başka kök anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıcı eşlik, eşleştirme ve kurulmuş arkadaşlık dalları işlem ile durum sınırını en açık biçimde gösterir, diğerleri daha dar örneklerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı bir eşlikçi verme veya yanına alma işlemini de kapsar; komşu dal kurulmuş ilişkinin sürekliliğini ve değişmezliğini öne çıkarır.","focus_only":"Odak dalı eşlik bağını kuran geçişli işlemi ve bir şeyi yanında götürmeyi içerir.","gloss":"kalıcı eşlik ve ayrılmama","neighbor_only":"Komşu dal bir şeyin başka bir şeyle uzun süre sabit kalmasını ve ondan ayrılmamasını durum olarak vurgular.","neighbor_ref":"root_001354/B001","relation_type":"near_synonym","shared_zone":"İki şeyin birlikte kalması ve birbirinden ayrılmaması iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dalı eşlik bağı kurar; komşu dal karşılıklı bir çift veya sınıflandırılmış eş oluşturur.","focus_only":"Odak dalı kitap gibi bir nesneyi yanında götürmeyi ve iki şeyin uygun düşmesini de kapsar.","gloss":"iki şeyi eşleştirmek","neighbor_only":"Komşu dal iki tarafı çift yapmak, evlilik bağıyla birleştirmek veya türlerine göre eşleştirmek anlamlarına uzanır.","neighbor_ref":"root_000652/B003","relation_type":"near_synonym","shared_zone":"Bir şeyi başka bir şeyle bağlantılı ve birlikte olacak duruma getirmek her iki dalda bulunur."},{"boundary_match":"partial","distinction":"Bu dal eşlik ilişkisini kuran ya da sürdüren işlemi anlatır; komşu dal ilişkinin kendisini ve eşlik eden tarafı anlatır.","focus_only":"Odak dalı bir eşlikçi belirleme veya bir nesneyi yanına alma işlemini bildirir.","gloss":"süreğen eşlik durumu","neighbor_only":"Komşu dal kurulmuş eşlik ilişkisini ve tarafların süreğen birlikte bulunmasını bildirir.","neighbor_ref":"root_000844/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın merkezinde bir tarafın başka bir tarafla birlikte bulunması vardır."}],"source_phrase_ar":"كل شيء لاءم شيئا فقد استصحبه (maqayis;ayn;sihah)؛ أصحبته الشيء جعلته له صاحبا (sihah)؛ استصحبته الكتاب وغيره (sihah)؛ أصحب فلان فلانا جعل صاحبا له (mufradat)","source_summary":"Kaynaklar bir şeyi eşlikçi kılma, bir nesneyi beraberinde götürme ve iki şeyin birbirine uygun düşmesi görünümlerini ortak bir eşlik bağı altında toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"جعل شيء صاحبا لغيره واستصحاب الشيء وملازمة الشيء وملاءمته لشيء آخر","what_is_not_ar":"ليس الانقياد ولا بلوغ الابن"},"support_links":["sup_2f25bfde6e82a7d8f8d7"]},{"boundary":"Olgunlaşan katılımcı oğuldur ve sonuç babaya yoldaş olabilmesidir; genel yetişkinliğe erişme tek başına yeterli değildir.","branch_kind":"bare","branch_ref":"root_000844/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"oğlunun büyüyüp babasına yoldaş olması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Oğul büyür ve babasıyla yetişkin bir yoldaş ilişkisi kurabilecek olgunluğa erişir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Değişim baba üzerinden bildirilse de yaş ve durum değişikliğini yaşayan kişi onun oğludur."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Oğlun olgunlaşmasını ve bunun sonucunda babasıyla yoldaş ilişkisi kurabilmesini birlikte anlatır.","boundary_detail":"Olgunlaşan katılımcı oğuldur ve sonuç babaya yoldaş olabilmesidir; genel yetişkinliğe erişme tek başına yeterli değildir.","branch_image_ar":"بلوغ الابن صاحبا","concept_gloss":"oğlunun büyüyüp babasına yoldaş olması","contextual_glosses":[{"applicability":"Durumun baba üzerinden bildirildiği bir cümlede doğal Türkçe karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baba üzerinden anlatımı ve oğuldaki olgunlaşma sonucunu korur."},"facet_ids":["F001","F002"],"text":"oğlu büyüyüp kendisine yoldaş oldu","usage_role":"contextual"}],"definition":"Bir erkeğin oğlunun büyüyüp olgunlaşarak babasına yoldaş olabilecek duruma gelmesidir. Durum babaya yüklenerek anlatılsa da olgunlaşan katılımcı oğuldur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Oğul büyür ve babasıyla yetişkin bir yoldaş ilişkisi kurabilecek olgunluğa erişir."},{"facet_id":"F002","role":"specialization","statement":"Değişim baba üzerinden bildirilse de yaş ve durum değişikliğini yaşayan kişi onun oğludur."}],"identity_rationale":"Kaynak ifadesi, babanın oğlunun büyüyüp onunla arkadaşlık edebilecek veya ona yoldaş olabilecek olgunluğa erişmesini tek bir durum değişikliği olarak verir. Anlam, erkeğin herhangi bir eşlikçisi bulunması değil, oğlun büyümesiyle baba-oğul ilişkisinin yeni bir aşamaya geçmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"oğlu büyüyüp kendisine yoldaş olacak yaşa gelmek"}],"lexicalization_note":"Tanım yalın dalın oğul, baba, büyüme ve yoldaş olma katılımcılarını aynen korur; genel ergenlik anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ergenlik, kapsamlı olgunlaşma ve yaşlı ebeveynin çocuğu karşılaştırmaları katılımcı ve sonuç sınırlarını gösterir, diğerleri bunları yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı aile içindeki yeni yoldaşlık ilişkisini kurucu sonuç sayar; komşu dal yalnızca yaşa bağlı ergenliği bildirir.","focus_only":"Odak dalı oğlun olgunlaşmasını babasına yoldaş olma sonucuna bağlar ve durumu baba üzerinden bildirir.","gloss":"ergenlik çağına ulaşma","neighbor_only":"Komşu dal herhangi bir kişinin ergenlik çağına erişmesini, belirli bir aile ilişkisi veya yoldaşlık sonucu aramadan anlatır.","neighbor_ref":"root_000352/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da genç kişinin çocukluktan çıkarak daha olgun bir yaşa gelmesi vardır."},{"boundary_match":"partial","distinction":"Odak dalı olgunluğu babaya eşlik edebilme ilişkisiyle ölçer; komşu dal kişisel güç ve kavrayışın tamamlanmasına odaklanır.","focus_only":"Odak dalında belirli oğul-baba katılımcıları ve babaya yoldaş olma sonucu zorunludur.","gloss":"güç ve sağduyuda olgunlaşma","neighbor_only":"Komşu dal güç, sağduyu, deneyim ve gençliğin tamamlanması bakımından genel olgunluğa erişmeyi kapsar.","neighbor_ref":"root_000782/B004","relation_type":"near_neighbor","shared_zone":"Bir gencin büyüyerek daha yetkin ve olgun bir aşamaya gelmesi ortak alandır."},{"boundary_match":"thematic_only","distinction":"Odak dalının konusu çocuğun büyüyüp ilişki değiştirmesidir; komşu dalın konusu ebeveyn yaşlıyken doğan son çocuğun kimliğidir.","focus_only":"Odak dalı oğlun büyüyerek babasına yetişkin bir yoldaş haline gelmesini anlatır.","gloss":"yaşlı ebeveynin son çocuğu","neighbor_only":"Komşu dal yaşlı anne veya babanın son çocuğunu ve çocuğun ebeveynlerin ileri yaşında doğmuş olmasını anlatır.","neighbor_ref":"root_000985/B007","relation_type":"thematic","shared_zone":"Her iki dal da çocuğun yaşı ile ebeveynin yaşam evresini aynı aile sahnesinde ilişkilendirir."}],"source_phrase_ar":"أصحب الرجل إذا بلغ ابنه (maqayis;sihah)؛ أصحب فلان إذا كبر ابنه فصار صاحبه (mufradat)","source_summary":"Kaynaklar, oğlun büyümesi ile babasına yoldaş olabilecek hale gelmesini aynı durum değişikliğinin iki tamamlayıcı aşaması olarak sunar.","sources":["MQ","SI","MU"],"what_is_ar":"إصحاب الرجل إذا بلغ ابنه أو كبر فصار صاحبه","what_is_not_ar":"ليس مجرد كون الرجل ذا صاحب"},"support_links":[]},{"boundary":"Ayırt edici koşul kılın veya yünün deri üzerinde bırakılmasıdır; kılsız deri ve yalnızca yünün kendisi bu dala girmez.","branch_kind":"bare","branch_ref":"root_000844/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"kılı veya yünü üzerinde bırakılmış deri","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzme veya deri işleme sırasında kılın ya da yünün bir bölümü veya tamamı deri üzerinde bırakılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin sonucu, üzerinde kendi kılı veya yünü duran deri, post ya da deri tulumdur."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşleme sonunda kendi kılı ya da yünü bütünüyle giderilmemiş deri, post ve tulum için kullanılır.","boundary_detail":"Ayırt edici koşul kılın veya yünün deri üzerinde bırakılmasıdır; kılsız deri ve yalnızca yünün kendisi bu dala girmez.","branch_image_ar":"أديم مُصحَب عليه الشعر","concept_gloss":"kılı veya yünü üzerinde bırakılmış deri","contextual_glosses":[{"applicability":"Hayvanı yüzme veya deriyi işleme eyleminin özellikle anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kıl veya yünü gidermeyip deri üzerinde bırakma işlemini korur."},"facet_ids":["F001"],"text":"tüyünü derinin üzerinde bırakmak","usage_role":"contextual"},{"applicability":"İşlemden sonra üzerinde kıl ya da yün kalan ürünün kısa karşılığı olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ortaya çıkan postu ve tüyün korunmuş olmasını birlikte korur."},"facet_ids":["F002"],"text":"tüylü bırakılmış post","usage_role":"contextual"}],"definition":"Bir hayvanı yüzerken veya deriyi işlerken kılın ya da yünün tümünü gidermeyip deri üzerinde bırakmak ve bu işlem sonunda üzerinde kıl veya yün bulunan deri, post ya da tulum elde etmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzme veya deri işleme sırasında kılın ya da yünün bir bölümü veya tamamı deri üzerinde bırakılır."},{"facet_id":"F002","role":"specialization","statement":"İşlemin sonucu, üzerinde kendi kılı veya yünü duran deri, post ya da deri tulumdur."}],"identity_rationale":"Kaynak ifadesi, hayvanın yüzülmesi veya derinin işlenmesi sırasında kılın ya da yünün bütünüyle kazınmayıp deri üzerinde bırakılmasını tutarlı biçimde anlatır. Dal hem bu işlemi hem de işlem sonunda üzerinde kıl veya yün kalan deri, post ya da tulum durumunu içerir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kılı veya yünü üzerinde bırakılmış deri, post ya da tulum"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"hayvanı yüzerken kılı veya yünü deri üzerinde bırakmak"}],"lexicalization_note":"Tanım yalın dalın işleme eylemi ile tüylü deri sonucunu kapsar; genel deri, kürk veya yün adlarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tüyü alınmamış ham deri en yakın anlamdır, genel deri ve tabaklama evresi ise alan sınırını gösterir; yün ve kürk adayları yalnızca malzeme bakımından ilişkilidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı tüyü bırakma işlemi ile çeşitli deri ürünlerini kapsar; komşu dal tüyü korunmuş ve belirli biçimde işlenmemiş ham deriye odaklanır.","focus_only":"Odak dalı yüzme veya deri işleme eylemini ve üzerinde tüy bırakılan tulumu da kapsar.","gloss":"tüyü alınmamış ham deri","neighbor_only":"Komşu dal tüyü alınmamış veya tüyüyle kurumuş, ayrıca ıslatılıp yumuşatılmamış deriyi daha dar bir işlem durumuyla niteler.","neighbor_ref":"root_001021/B006","relation_type":"near_synonym","shared_zone":"Her iki dalda da derinin kendi kılı veya yünü yüzeyinde kalır."},{"boundary_match":"field_only","distinction":"Odak dalı yüzeyde tüy kalmasına göre, komşu dal ise tabaklama evresine göre sınıflandırılır.","focus_only":"Odak dalını belirleyen özellik derinin üzerinde kıl veya yün bırakılmasıdır.","gloss":"tabaklama evresindeki deri","neighbor_only":"Komşu dal deriyi tabaklama sürecindeki bir evre veya deri türü olarak adlandırır, tüyün kalmasını kurucu koşul yapmaz.","neighbor_ref":"root_000040/B005","relation_type":"same_field","shared_zone":"İki dal da hayvan derisinin yüzme sonrasındaki işlenmiş veya işlenmekte olan durumunu anlatır."},{"boundary_match":"field_only","distinction":"Odak dalı özel bir yüzey durumunu adlandırır; komşu dal tüy durumu aramadan deriyi işlevi ve malzemesi bakımından kapsar.","focus_only":"Odak dalı derinin tüyü korunarak hazırlanmış olmasını zorunlu kılar.","gloss":"genel deri ve deri ürünü","neighbor_only":"Komşu dal bedeni veya içindeki şeyi tutan genel deri ve deriden yapılan kayış gibi ürünleri kapsar.","neighbor_ref":"root_001424/B005","relation_type":"same_field","shared_zone":"Her iki dalın gönderimi hayvan derisine ve deriden hazırlanabilen ürünlere uzanır."}],"source_phrase_ar":"الأديم إذا ترك عليه شعره مصحب (maqayis)؛ جلد مصحب إذا كان عليه شعره وصوفه (ayn)؛ صحبت المذبوح إذا سلخته وأبقيت على الجلد صوفا أو شعرا (jamhara)؛ أديم مصحب إذا دبغته وتركت عليه بعض الصوف أو الشعر (jamhara)؛ المصحب من الزقاق ما الشعر عليه (sihah)؛ أصحبته إذا تركت صوفه أو شعره عليه (sihah)؛ أديم مصحب أصحب الشعر الذي عليه ولم يجز عنه (mufradat)","source_summary":"Kaynaklar, yüzme veya işleme sırasında kıl ya da yünün deri üzerinde bırakılması ve ortaya çıkan tüylü deri durumunda birleşir; deri, post ve tulum örnekleri aynı sınırı korur.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الأديم والجلد والزق إذا أبقي عليه شعره أو صوفه عند السلخ أو الدبغ","what_is_not_ar":"ليس الحَمِيت الذي لا شعر عليه"},"support_links":[]},{"boundary":"Yosun suyun üzerinde bir örtü oluşturmalıdır; köpük, dalga, süt kaymağı veya karayı örten su bu dala girmez.","branch_kind":"bare","branch_ref":"root_000844/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"suyun yüzünü yosun kaplaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yosun suyun üstüne çıkarak yüzeyi kaplar ve görünür bir örtü oluşturur."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yosunun su üstünde yayılıp yüzeyi örttüğü durum değişikliğini tam olarak karşılar.","boundary_detail":"Yosun suyun üzerinde bir örtü oluşturmalıdır; köpük, dalga, süt kaymağı veya karayı örten su bu dala girmez.","branch_image_ar":"طُحلب يعلو الماء","concept_gloss":"suyun yüzünü yosun kaplaması","contextual_glosses":[{"applicability":"Suyun üstünde yosun tabakası oluştuğunu doğal bir Türkçe cümleyle bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Suyun yosunla kaplanmış duruma gelmesini korur."},"facet_ids":["F001"],"text":"su yosun tuttu","usage_role":"contextual"}],"definition":"Suyun üst yüzeyini yosunun kaplaması ve suyun yosunla örtülü bir duruma gelmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yosun suyun üstüne çıkarak yüzeyi kaplar ve görünür bir örtü oluşturur."}],"identity_rationale":"Kaynak ifadesi tek ve açık bir durum değişikliği verir: suyun üst yüzeyini yosunun kaplaması. Dal yosunun genel adı değildir; su, yüzey ve yüzeyi örten yosun katmanı birlikte korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"suyun yüzü yosunla kaplanmak"}],"lexicalization_note":"Tanım yalın dalın su yüzeyinin yosunla kaplanması anlamında kalır ve başka yüzey tabakalarına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su üstündeki yosun adı, köpük ve süt tabakası yüzey örtüsü sınırını en iyi gösterir, dalga ve bitki adayları daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı suyun uğradığı değişimi anlatır; komşu dal yüzeydeki yosun oluşumunu adlandırır.","focus_only":"Odak dalı suyun yosunla kaplanmış duruma gelmesini olay ve durum olarak bildirir.","gloss":"su yüzeyindeki yosun tabakası","neighbor_only":"Komşu dal su yüzeyinde beliren yosunu belirli bir adla nesne olarak gösterir.","neighbor_ref":"root_000210/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda suyun üstünde görünen ve yüzeyi örtebilen yosun bulunur."},{"boundary_match":"field_only","distinction":"Odak dalı yosunun suyu kaplamasıdır; komşu dal kabarcıklı köpük maddesidir ve yalnızca suyla sınırlı değildir.","focus_only":"Odak dalında yüzey örtüsünü oluşturan madde canlı kökenli yosundur.","gloss":"yüzeyde yüzen köpük","neighbor_only":"Komşu dal su, deniz, süt veya içecek üstünde oluşabilen beyaz köpüğü ve başka yerlerdeki köpüksü oluşumları kapsar.","neighbor_ref":"root_000620/B001","relation_type":"same_field","shared_zone":"İki dalda da bir sıvının üst yüzeyinde görünen ve yüzeyden ayrışan bir tabaka vardır."},{"boundary_match":"partial","distinction":"Yüzey yapısı benzese de odak dalının sıvısı su ve örtüsü yosundur; komşu dalda sıvı süt, örtü ise süt tabakasıdır.","focus_only":"Odak dalı su yüzeyine çıkan yosunu ve suyun bununla kaplanmasını gerektirir.","gloss":"sütün üstündeki kaymak tabakası","neighbor_only":"Komşu dal sütün üstüne çıkan kaymak benzeri tabakayı veya doğrudan bu tabakanın kendisini anlatır.","neighbor_ref":"root_001300/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir sıvının üstünü örten ayrı ve görünür bir yüzey katmanı oluşur."}],"source_phrase_ar":"أصحب الماء إذا علاه الطحلب (maqayis;sihah)","source_summary":"Kaynaklar aynı yalın sınırı verir: yosun suyun üstüne çıkar ve yüzeyini örter.","sources":["MQ","SI"],"what_is_ar":"إصحاب الماء حين يعلوه الطحلب","what_is_not_ar":"ليس الأديم المصحب ولا لون الحيوان"},"support_links":[]},{"boundary":"Renk kızıla yaklaşan açık toprak tonudur ve kanıt yalnızca eşek nitelemesini destekler; genel renk adına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000844/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","surface_ar":"أَصْحَٰبُ"}],"gloss":"kızıla çalan açık toprak renginde eşek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşeğin rengi açık bir toprak tonudur ve belirgin biçimde kızıla yaklaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Renk nitelemesi bağımsız bir genel sıfat olarak değil, eşeği niteleyen sözlüksel birim içinde kullanılır."}}],"root_ar":"ص ح ب","root_id":"root_000844","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtta verilen eşek nitelemesini, hayvanı ve renk tonunu birlikte koruyarak karşılar.","boundary_detail":"Renk kızıla yaklaşan açık toprak tonudur ve kanıt yalnızca eşek nitelemesini destekler; genel renk adına genişletilmez.","branch_image_ar":"لون أَصحَب إلى الحمرة","concept_gloss":"kızıla çalan açık toprak renginde eşek","contextual_glosses":[{"applicability":"Eşeğin rengini doğal Türkçe içinde kısa ve gözle görülür bir tonla anlatmak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı ve kızıla yaklaşan açık renk tonunu korur."},"facet_ids":["F001","F002"],"text":"kızıla çalan açık kahverengi eşek","usage_role":"contextual"}],"definition":"Bir eşeğin renginin açık toprak tonunda olup kızıla çalmasıdır; niteleme yalnızca bu hayvanla kurulan sözlüksel kullanım içinde tanıklanmıştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşeğin rengi açık bir toprak tonudur ve belirgin biçimde kızıla yaklaşır."},{"facet_id":"F002","role":"specialization","statement":"Renk nitelemesi bağımsız bir genel sıfat olarak değil, eşeği niteleyen sözlüksel birim içinde kullanılır."}],"identity_rationale":"Kaynak ifadesi, eşeğe özgü bir renk nitelemesini ve bu rengin kızıla çalan açık toprak tonu olduğunu açıkça bildirir. Dal genel kırmızılık veya her canlıya uygulanabilen bağımsız bir renk adı olarak değil, eşek için kullanılan sınırlı bir niteleme olarak kurulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kızıla çalan açık toprak renginde eşek"}],"lexicalization_note":"Tanım, eşekle kurulan sözlüksel nitelemeye bağlı kalır; renk sıfatı yalın ve sınırsız bir kullanıma genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel kırmızılık, kırmızı nesneler ve bulanık ara renk dalları ton ile kapsam sınırını gösterir, öteki adaylar daha uzak renk karşılaştırmalarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli hayvandaki kırmızımsı açık toprak tonudur; komşu dal nesne ve canlı türü bakımından sınırlanmayan genel kırmızılıktır.","focus_only":"Odak dalı açık toprak tonunun kızıla çalmasını ve nitelemenin eşekle sınırlı olmasını gerektirir.","gloss":"genel kırmızı renk","neighbor_only":"Komşu dal kırmızı rengin kendisini, bir şeyin kızarmasını ve kırmızılığın kalıcı veya geçici görünmesini genel olarak kapsar.","neighbor_ref":"root_000356/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da görünür renk kırmızıya yaklaşır veya kırmızılık taşır."},{"boundary_match":"partial","distinction":"Odak dalı tek bir hayvan nitelemesidir; komşu dal kırmızı rengin kendisine ve çeşitli kırmızı nesnelere uzanır.","focus_only":"Odak dalı rengi yalnızca eşeğin açık ve kızıla çalan tonu olarak sınırlar.","gloss":"kırmızılık ve kırmızı nesneler","neighbor_only":"Komşu dal genel kırmızılığı, kırmızı yanakları, kırmızı boncuğu ve kırmızı taş türünü kapsar.","neighbor_ref":"root_001699/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal kırmızı görünümü veya kırmızıya yaklaşan bir renk niteliğini içerir."},{"boundary_match":"field_only","distinction":"Odak dalının tonu ve hayvanı sabittir; komşu dalın renk yönü değişkendir ve hoşnutsuzluk değerlendirmesi taşır.","focus_only":"Odak dalı eşekte görülen kızıla çalan belirli ve görece açık bir toprak tonunu anlatır.","gloss":"bulanık ve hoş olmayan renk","neighbor_only":"Komşu dal bulanık, hoş görülmeyen ve kırmızı, sarı, beyaz veya kül rengi yönlerinde değişebilen geniş bir renk karışımını kapsar.","neighbor_ref":"root_001161/B003","relation_type":"same_field","shared_zone":"İki dal da saf bir ana renkten çok karışık veya ara bir renk görünümünü niteleyebilir."}],"source_phrase_ar":"حمار أصحب أي أصحر يضرب لونه إلى الحمرة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, eşeğin açık toprak renginin kızıla çaldığını ve nitelemenin bu hayvana bağlı olduğunu bildirir."}],"source_summary":"Ortak çok kaynaklı bir açıklama bulunmaz; kanıt tek bir sözlükteki eşeğe bağlı renk nitelemesinden oluşur.","sources":["SI"],"what_is_ar":"الأصحب في لون الحمار وهو أصحر يضرب إلى الحمرة","what_is_not_ar":"ليس الصحبة والملازمة ولا الطحلب"},"support_links":[]},{"boundary":"Dal, sağ elin veya sağ yönün kendisini değil, bunlara ancak uğur ve mutluluk değeri yüklendiği kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001698/B001","candidate_links":[{"candidate_id":"cand_92fb5a8e6344a4e767a0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"uğur ve iyilik getirme, bunları umma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin çevresine iyilik, bolluk ve mutluluk getiren olumlu niteliği."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi, nesne ya da görüşü olumlu sonuç getirecek sayarak ondan iyilik umma eylemi."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sağ tarafı bildiren kimi sözlerin mutluluk, iyi yazgı ve Tanrı'ya yakınlık için mecazlaşması."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın olumlu nitelik, bu niteliği umma ve iyi yazgıya aktarma çekirdeğini birlikte karşılar.","boundary_detail":"Dal, sağ elin veya sağ yönün kendisini değil, bunlara ancak uğur ve mutluluk değeri yüklendiği kullanımları kapsar.","branch_image_ar":"اليمن والبركة","concept_gloss":"uğur ve iyilik getirme, bunları umma","contextual_glosses":[{"applicability":"Bir kişinin veya şeyin çevresine olumlu sonuç getiren niteliği anlatan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişi veya şeyin uğur ve iyilik getiren olumlu niteliğini eksiksiz korur."},"facet_ids":["F001"],"text":"uğurlu ve iyilik getirici","usage_role":"contextual"},{"applicability":"Bir kişiden, nesneden veya görüşten olumlu sonuç beklendiğini anlatan eylem bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyi uğurlu sayma ve ondan olumlu sonuç umma eylemlerini birlikte korur."},"facet_ids":["F002"],"text":"uğur sayıp iyilik ummak","usage_role":"contextual"}],"definition":"Bir kimse, şey, görüş ya da işarette bulunan ve iyilik, bolluk ya da mutluluk getiren olumlu niteliktir. Bir kişi, nesne veya görüşten bu niteliğe bağlı olarak iyilik umma da dala bağlı kullanımdır; sağ tarafla ilgili kimi kalıplar yalnız mutluluk, iyi yazgı veya Tanrı'ya yakınlık çağrışımı taşıdıklarında bu dala girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin çevresine iyilik, bolluk ve mutluluk getiren olumlu niteliği."},{"facet_id":"F002","role":"associated_use","statement":"Bir kişi, nesne ya da görüşü olumlu sonuç getirecek sayarak ondan iyilik umma eylemi."},{"facet_id":"F003","role":"extension","statement":"Sağ tarafı bildiren kimi sözlerin mutluluk, iyi yazgı ve Tanrı'ya yakınlık için mecazlaşması."}],"identity_rationale":"Kaynak ifadesi bu dalı uğur, iyilik artışı ve mutluluk getiren nitelik ile bir kişi, nesne ya da görüşten böyle bir sonuç umma eylemi çevresinde açıkça kurar. Sağ tarafı bildiren kimi ifadelerin iyi yazgı ve mutluluk için mecazlaşması da aynı olumlu değer çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"uğur, iyilik artışı ve mutluluk"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"uğurlu ve iyilik getiren"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"topluluğuna uğur ve iyilik getirdi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"uğur ve iyilik getiren kimse"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onu uğurlu sayıp iyilik umdu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onun görüşünü uğurlu sayıp iyilik umuyor"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"mutluluk ve iyi yazgı sahipleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"mutluluğa ve Tanrı'ya yakınlığa ulaştıran araç sayılan Kara Taş"}],"lexicalization_note":"Tanım, yalın uğur ve iyilik getirme anlamını kalıba bağlı iyilik umma ve iyi yazgı kullanımlarından ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; uğurlu nitelik, iyiliğin çoğalması ve anlık iyiye yorma arasındaki sınırı en iyi gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal olumlu yazgı getiren nitelik ve onu uğurlu sayma üzerinde durur; komşu dal ise iyiliğin artması, yerleşmesi ve sürekliliği üzerinde durur.","focus_only":"Uğurlu sayma, mutluluk ve iyi yazgıdan iyilik umma eylemi bu dalda belirgindir.","gloss":"uğur ile çoğalan ve kalıcı iyilik","neighbor_only":"İyiliğin yerleşmesi, çoğalması ve süreklilik kazanması komşu dalda daha belirgindir.","neighbor_ref":"root_000109/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyde iyilik bulunmasını ve bu iyiliğin başkasına olumlu sonuç vermesini anlatır."},{"boundary_match":"field_only","distinction":"Bu dal uğurlu nitelik ve ondan iyilik umma kavramıdır; komşu dal belirli bir olayın iyiye yorulmasıdır.","focus_only":"Bu dal kişi, nesne veya görüşe yüklenen kalıcı ya da genellenebilir uğur niteliğini de kapsar.","gloss":"uğur ve iyiye yorma","neighbor_only":"Komşu dal, bir kabın taşması gibi belirli bir olaydan anlık iyiye yorma çıkarır.","neighbor_ref":"root_000481/B007","relation_type":"same_field","shared_zone":"İki dal da bir belirtiyi olumlu sonuçla ilişkilendiren iyi yazgı alanına girer."}],"source_phrase_ar":"واليمن البركة وهو ميمون (maqayis)؛ يمن الرجل فهو ميمون والميمن الذي أتى باليمن والبركة (ayn)؛ اليمن البركة وتيمنت به تبركت (sihah)؛ اليمن نظير البركة ويمن الرجل فهو ميمون (tahdhib)؛ أصحاب اليمين أصحاب السعادات والميامن واستعير اليمين للتيمن والسعادة (mufradat)","source_summary":"Kaynaklar uğur ve iyilik getiren niteliği, bu niteliğe sahip kişiyi ve bir kişi ya da görüşten olumlu sonuç umma eylemini aynı anlam alanında birleştirir; sağ taraf söylemi de mutluluk ve iyi yazgıya aktarılabilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"البركة والسعادة والتبرك وما يوصف بأنه ميمون","what_is_not_ar":"اليد اليمنى والجهة واليمين الحلف وبلاد اليمن"},"support_links":["sup_b0b3565f14a959742289"]},{"boundary":"Dal, uğur, ant, güç veya ülke anlamlarını değil, somut sağ el ile sağ yönü ve bunlara doğrudan bağlı hareketleri kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001698/B002","candidate_links":[{"candidate_id":"cand_04fd5b234f3dc5ca3b01","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"sağ el ve sağ yön","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın ya da başka bir varlığın sağ eli veya sağ taraftaki bedensel yanı."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sol yönün karşıtı olan sağ yan ve bu yana karşılık gelen yön."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sağa doğru ilerleme, başkalarını sağa götürme veya bir şeyi sağ elle verme."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Somut organı, bedenin sağ yanını ve bunun uzamsal yön karşılığını birlikte anlatan genel karşılıktır.","boundary_detail":"Dal, uğur, ant, güç veya ülke anlamlarını değil, somut sağ el ile sağ yönü ve bunlara doğrudan bağlı hareketleri kapsar.","branch_image_ar":"اليد اليمنى والجهة اليمنى","concept_gloss":"sağ el ve sağ yön","contextual_glosses":[{"applicability":"Söz konusu olan bedensel organ veya sağ taraftaki el olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel organ olarak sağ el anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"sağ el","usage_role":"contextual"},{"applicability":"Bir kişinin ilerlediği veya başkalarını götürdüğü yönün sağ taraf olduğunu anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sağ yönü ve bu yöne doğru gerçekleşen hareketi birlikte korur."},"facet_ids":["F002","F003"],"text":"sağa doğru","usage_role":"contextual"}],"definition":"İnsan veya başka bir varlıktaki sağ el ya da bedenin sağ yanı ile bu yana karşılık gelen yön. Sağa ilerleme, bir topluluğu sağa götürme ve sağ elle verme gibi kullanımlar bu somut organ-yön çekirdeğine bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın ya da başka bir varlığın sağ eli veya sağ taraftaki bedensel yanı."},{"facet_id":"F002","role":"core","statement":"Sol yönün karşıtı olan sağ yan ve bu yana karşılık gelen yön."},{"facet_id":"F003","role":"associated_use","statement":"Sağa doğru ilerleme, başkalarını sağa götürme veya bir şeyi sağ elle verme."}],"identity_rationale":"Kaynak ifadesi sağ eli, sağ bedensel yanı ve bu yana karşılık gelen yönü birlikte verir; sağa gitme, bir topluluğu sağa götürme ve sağ elle verme kullanımları da bu somut el-yön çekirdeğine bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sağ el veya sağ yön"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yanındakileri sağa götür"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sağ taraf veya sağ yön"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"solun karşıtı olan sağ taraf"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sağa doğru ilerledi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"iki sağ eliyle verdiği azık"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sağ eller"}],"lexicalization_note":"Tanım sağ el ve sağ yön çekirdeğini korur; sağa götürme, sağa gitme ve sağ elle verme yalnız kendi kalıpları içinde ele alınır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşıt yönü ve taraf belirtmeyen genel el kavramını gösteren iki komşu, dal sınırını en açık biçimde belirledi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı el-yön ekseninin karşıt uçlarıdır: bu dal sağ tarafı, komşu dal sol tarafı gösterir.","focus_only":"Bu dal sağ eli ve sağ yönü bildirir.","gloss":"sağ ile sol karşıtlığı","neighbor_only":"Komşu dal sol eli ve sol yönü bildirir.","neighbor_ref":"root_001694/B004","relation_type":"antonym","shared_zone":"İki dal da bedensel bir eli ve o ele karşılık gelen uzamsal yönü adlandırır."},{"boundary_match":"partial","distinction":"Bu dal taraf ve yön bilgisini kurucu sayar; komşu dal ise el organını sağ-sol ayrımı olmadan ele alır.","focus_only":"Bu dal eli özellikle sağ taraf oluşuyla sınırlar ve sağ yönü de kapsar.","gloss":"sağ el ile genel el","neighbor_only":"Komşu dal taraf ayrımı yapmadan el organını ve onun başına gelen durumları kapsar.","neighbor_ref":"root_001693/B001","relation_type":"near_neighbor","shared_zone":"İki dalın ortak alanı bedensel el organıdır."}],"source_phrase_ar":"فاليمين يمين اليد (maqayis)؛ واليمين اليد اليمنى والأيمان جمعه (ayn)؛ اليمنة خلاف اليسرة والأيمن والميمنة خلاف الأيسر والميسرة (sihah)؛ يقال لليد اليمنى يمين وأخذ فلان يمينا وأخذ يسارا ويامن بأصحابك (tahdhib)؛ اليمين أصله الجارحة والميمنة ناحية اليمين (mufradat)","source_summary":"Kaynaklar sağ eli temel bedensel anlam, sağ tarafı da bunun yönsel karşılığı olarak birleştirir; sağa yönelme ve sağ elle yapılan verme eylemleri bu çekirdeğe bağlı kullanımlardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"اليد اليمنى والجارحة والجانب الأيمن والسير أو الأخذ جهة اليمين وما يعطى باليمين","what_is_not_ar":"البركة والحلف والقوة وبلاد اليمن"},"support_links":["sup_8c1771c59d9dbffb6dba"]},{"boundary":"Dal, sağ elin kendisini veya genel bir antlaşmayı değil, ant içme eylemini, onun sonucundaki bağlı sözü ve ant sözlerini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001698/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"kutsal tanıklı ant ve söz güvencesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iddia veya davranış sözünü güvenceye bağlayan ant içme eylemi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ant içme sonucunda ortaya çıkan bağlayıcı söz veya güvence."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı adına ant içmek için kullanılan tam, hitaplı veya kısaltılmış söz kalıpları."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ant içme eylemini, bunun bağlayıcı söz sonucunu ve kutsal tanıklık unsurunu birlikte karşılar.","boundary_detail":"Dal, sağ elin kendisini veya genel bir antlaşmayı değil, ant içme eylemini, onun sonucundaki bağlı sözü ve ant sözlerini kapsar.","branch_image_ar":"يمين الحلف","concept_gloss":"kutsal tanıklı ant ve söz güvencesi","contextual_glosses":[{"applicability":"Kutsal tanıklıkla verilen bağlayıcı sözün ad olarak geçtiği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kutsal tanıklıkla bağlayıcı söz verme anlamını doğal ve kısa biçimde korur."},"facet_ids":["F001","F002"],"text":"ant","usage_role":"contextual"},{"applicability":"Ant içme işlevindeki tam veya kısaltılmış söz kalıplarını Türkçe akış içinde karşılar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'yı tanık gösteren ant sözü işlevini eksiksiz korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"}],"definition":"Bir sözün doğruluğunu ya da bir işi yapıp yapmayacağını ant yoluyla güvenceye bağlama ve böylece bağlayıcı söz verme. Tanrı adıyla kurulan kalıplar ve bu işlev için kullanılan kısa ant sözleri de dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iddia veya davranış sözünü güvenceye bağlayan ant içme eylemi."},{"facet_id":"F002","role":"core","statement":"Ant içme sonucunda ortaya çıkan bağlayıcı söz veya güvence."},{"facet_id":"F003","role":"associated_use","statement":"Tanrı adına ant içmek için kullanılan tam, hitaplı veya kısaltılmış söz kalıpları."}],"identity_rationale":"Kaynak ifadesi dalı ant içme, verilen sözün güvenceye bağlanması ve bu işlevde kullanılan söz kalıpları olarak açıkça tanımlar. Tanrı adıyla kurulan kalıplar bu alanın belirli biçimleridir; el anlamından aktarılmış olması tarihsel açıklamadır, dalın güncel çekirdeği söz güvencesidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ant veya kutsal tanıklı söz güvencesi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"antlar ve bağlayıcı sözler"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"senin adına ant olsun"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"Tanrı adına edilen ant"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun diyen kısaltılmış söz"}],"lexicalization_note":"Tanım ant içme çekirdeğini korur; Tanrı adına söylenen belirli söz kalıplarını yalnız kendi ant bağlamları içinde gösterir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çekirdeği en çok paylaşan genel ant dalı ile antın bozulmasını anlatan sonuç dalı seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdek büyük ölçüde ortaktır; bu dal belirli söz biçimlerine, komşu dal ise ant içmenin daha geniş eylem ve katılımcı türevlerine uzanır.","focus_only":"Bu dal belirli ant sözlerini ve bunların el anlamından aktarılmış açıklamasını da içerir.","gloss":"ant ve ant içme","neighbor_only":"Komşu dal sık ant içme, başkasına ant içirtme ve ant verilmiş kişi gibi daha geniş eylem türevlerini de kapsar.","neighbor_ref":"root_000349/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı ant içme ve bağlayıcı söz güvencesi verme eylemidir."},{"boundary_match":"partial","distinction":"Bu dal söz güvencesini kurar; komşu dal ise o güvenceye sonradan aykırı davranmayı konu edinir.","focus_only":"Bu dal antın kurulmasını ve bağlayıcı sözün verilmesini anlatır.","gloss":"ant vermek ile antı bozmak","neighbor_only":"Komşu dal kurulmuş bir antın tutulmamasını veya bozulmasını anlatır.","neighbor_ref":"root_000359/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da bağlayıcı bir antın varlığını gerektirir."}],"source_phrase_ar":"واليمين الحلف (maqayis)؛ واليمين من القسم والأيمان جماعته وأيمن حرف وضع للقسم (ayn)؛ اليمين القسم الجمع أيمن وأيمان وأيمن الله اسم وضع للقسم (sihah)؛ الأصل يمين الله وأيمن الله وليمنك (tahdhib)؛ اليمين في الحلف مستعار من اليد (mufradat)","source_summary":"Kaynaklar ant içme eylemi ile bu eylemin oluşturduğu bağlayıcı sözü aynı çekirdekte birleştirir ve Tanrı adına kullanılan çeşitli kısa sözleri bu işlevin dilsel biçimleri olarak verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الحلف والقسم والعهد المحلوف وصيغ أيمن الله وليمنك وما يجري مجراها","what_is_not_ar":"اليد المجردة والبركة وبلاد اليمن والقوة"},"support_links":[]},{"boundary":"Güç çekirdeği ile doğruluk veya dinî gerekçenin geldiği güçlü taraf kullanımı ayrılır; somut sağ el bu dalın doğrudan anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001698/B004","candidate_links":[{"candidate_id":"cand_e593f23cda67de7e3223","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"güç, savunma ve güçlü doğruluk dayanağı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sağ el imgesiyle anlatılan güç, yetki ve etkili olabilme niteliği."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güç kullanarak birini engelleme, savma veya etkisiz bırakma."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Doğruluğun veya dinî gerekçenin geldiği yön ve bu yüzden başvurulan en güçlü dayanak."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın güç-yetki çekirdeğini, bunun engelleme işlevini ve doğruluk dayanağına uzanan kullanımını birlikte karşılar.","boundary_detail":"Güç çekirdeği ile doğruluk veya dinî gerekçenin geldiği güçlü taraf kullanımı ayrılır; somut sağ el bu dalın doğrudan anlamı değildir.","branch_image_ar":"يمين القوة والحق","concept_gloss":"güç, savunma ve güçlü doğruluk dayanağı","contextual_glosses":[{"applicability":"Sağ el imgesinin doğrudan güç veya etkili olabilme anlamına aktarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sağ el imgesiyle kurulan güç ve yetki çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"güç ve yetki","usage_role":"contextual"},{"applicability":"Doğruluk veya dinî gerekçe yönünden gelen güçlü etki ve ikna aracını anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doğruluk yönünden gelen en güçlü gerekçe ve dayanak anlamını korur."},"facet_ids":["F003"],"text":"en güçlü dayanak","usage_role":"contextual"}],"definition":"Sağ el veya sağ taraf imgesinden aktarılan güç, yetki, savunma ve engelleme. Belirli bağlamlarda doğruluğun ya da dinî gerekçenin geldiği tarafı ve böylece en güçlü dayanağı da bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sağ el imgesiyle anlatılan güç, yetki ve etkili olabilme niteliği."},{"facet_id":"F002","role":"specialization","statement":"Güç kullanarak birini engelleme, savma veya etkisiz bırakma."},{"facet_id":"F003","role":"extension","statement":"Doğruluğun veya dinî gerekçenin geldiği yön ve bu yüzden başvurulan en güçlü dayanak."}],"identity_rationale":"Kaynak ifadesi sağ taraf söylemini güç, yetki, engelleme ve savunmaya aktarır; ayrıca doğruluğun veya dinî gerekçenin geldiği yönü en güçlü dayanak olarak verir. Bu nedenle dal korunabilir, ancak bütün kullanımları tek bir yalın 'güç' anlamına indirgememek gerekir.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"güç, yetki veya doğruluğun güçlü tarafı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"dinî gerekçe veya doğruluk yönünden"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güçle veya doğruluğa dayanarak"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"güç kullanarak engelledi ve savdı"}],"lexicalization_note":"Yalın güç aktarımı ile belirli söz dizilerindeki savunma, engelleme ve güçlü dayanak anlamları birbirine karıştırılmadan tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; el imgesinden gelen güç ile genel kuvvet kavramını karşılaştıran iki komşu, dalın mecaz ve kapsam sınırını en iyi gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal sağ taraf imgesine ve belirli savunma-doğruluk bağlamlarına bağlıdır; komşu dal taraf belirtmeyen daha genel el-güç aktarımıdır.","focus_only":"Bu dal güç yanında engelleme ile doğruluk veya dinî gerekçeden gelen güçlü yönü de kapsar.","gloss":"sağ tarafın gücü ile el gücü","neighbor_only":"Komşu dal, el sözünün doğrudan güç, yetenek ve enerji için kullanılmasına odaklanır.","neighbor_ref":"root_001693/B002","relation_type":"near_synonym","shared_zone":"İki dal da el imgesini güç, yetki ve etkili olabilme anlamına aktarır."},{"boundary_match":"partial","distinction":"Bu dal belirli bir sağ taraf aktarımına bağlıdır; komşu dal ise herhangi bir taşıyıcıdaki genel kuvvet kavramıdır.","focus_only":"Bu dal sağ taraf imgesini, engelleme işlevini ve doğruluk yönünden gelen dayanağı taşır.","gloss":"mecazlı sağ güç ile genel kuvvet","neighbor_only":"Komşu dal beden, bağ, yardımcı, binek ve mal gibi çok çeşitli taşıyıcılardaki genel kuvveti kapsar.","neighbor_ref":"root_001274/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalın ortak alanı güç, dayanıklılık ve bir işi yapabilme kapasitesidir."}],"source_phrase_ar":"اليمين القوة (maqayis)؛ واليمين القوة وعن اليمين من قبل الدين (sihah)؛ باليمين أي بالقوة وقيل بالقوة والحق وتخدعوننا بأقوى الأسباب من قبل الدين (tahdhib)؛ لأخذنا منه باليمين أي منعناه ودفعناه (mufradat)","source_summary":"Kaynaklar sağ taraf söylemini güç ve yetkiye aktarır; bu güç engelleme ve savmada etkili olurken bazı bağlamlarda doğruluk ya da dinî gerekçenin sağladığı güçlü dayanağı anlatır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"القوة والقدرة والدفع والمنع والناحية التي منها الحق أو أقوى الأسباب","what_is_not_ar":"اليد الحسية والحلف والبركة وبلاد اليمن"},"support_links":["sup_2f25bfde6e82a7d8f8d7"]},{"boundary":"Dal uğur veya sağ yön anlamını değil, Yemen ülkesini, halkını ve bu yere doğrudan aidiyet ya da yönelişi kapsar.","branch_kind":"bare","branch_ref":"root_001698/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"Yemen ülkesi, halkı ve ona aidiyet","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yemen ülkesi, bu ülkenin toprakları ve burada yaşayan halk."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişinin, nesnenin veya niteliğin Yemen'e ait olduğunu bildirme."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yemen yönüne gitme, o yöne sapma veya Yemen'e varma."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yemen'e özgü dokumalardan yapılmış belirli bir örtü türü."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer adını, ülke halkını ve bu yere bağlı aidiyet çekirdeğini birlikte karşılayan en kısa doğal ifadedir.","boundary_detail":"Dal uğur veya sağ yön anlamını değil, Yemen ülkesini, halkını ve bu yere doğrudan aidiyet ya da yönelişi kapsar.","branch_image_ar":"اليمن البلد والانتساب","concept_gloss":"Yemen ülkesi, halkı ve ona aidiyet","contextual_glosses":[{"applicability":"Bir kişi veya nesnenin Yemen'e ait olduğunu bildiren bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yemen ülkesine mensubiyet veya bu ülkeye ait olma anlamını korur."},"facet_ids":["F002"],"text":"Yemenli","usage_role":"contextual"},{"applicability":"Bir topluluğun Yemen'e doğru yöneldiğini veya ülkeye vardığını anlatan hareket bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yemen yönünü hedefleyen hareket ve ülkeye varma anlamını birlikte korur."},"facet_ids":["F003"],"text":"Yemen yönüne gitmek","usage_role":"contextual"}],"definition":"Yemen adıyla bilinen ülke, onun toprakları ve halkı. Bu ülkeye aidiyet, ona doğru yönelme ve oraya özgü dokuma türü, yer çekirdeğine bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yemen ülkesi, bu ülkenin toprakları ve burada yaşayan halk."},{"facet_id":"F002","role":"extension","statement":"Bir kişinin, nesnenin veya niteliğin Yemen'e ait olduğunu bildirme."},{"facet_id":"F003","role":"associated_use","statement":"Yemen yönüne gitme, o yöne sapma veya Yemen'e varma."},{"facet_id":"F004","role":"specialization","statement":"Yemen'e özgü dokumalardan yapılmış belirli bir örtü türü."}],"identity_rationale":"Kaynak ifadesi Yemen'i ülke, toprak ve halk olarak tanımlar; bu yere aitlik bildiren biçimleri, Yemen yönüne gitmeyi ve oraya özgü dokumaları da aynı yer-aidiyet alanında toplar. Bu unsurlar ülke adının çekirdeğini değiştirmeyen türev ve bağlantılı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Yemen ülkesi veya Yemen yönü"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"Yemenli veya Yemen'e ait"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Yemenli veya Yemen'e ait"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Yemenli kadın veya Yemen'e ait dişil varlık"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"Yemenli kadın veya Yemen yönünden olan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"Yemen dokumasından yapılmış örtü"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"Yemen'e mensup oldu"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"Yemen yönüne gitti veya Yemen'e vardı"}],"lexicalization_note":"Tanım yalın dalı Yemen ülkesi ve halkı olarak kurar; aidiyet, yöneliş ve dokuma adları çekirdeğe bağlı ayrı türevler olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ülke ile ülke içindeki kent ayrımını ve farklı yer adlarına göre kurulan aidiyet örüntüsünü gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ülke düzeyindedir; komşu dal ülke içindeki tek bir kente ve o kentin ürünlerine özgüdür.","focus_only":"Bu dal Yemen ülkesini, halkını ve ülkeye genel aidiyeti kapsar.","gloss":"Yemen ile Yemen'deki belirli kent","neighbor_only":"Komşu dal Yemen içindeki belirli bir kenti ve yalnız o kente ait kişi ile ürünleri kapsar.","neighbor_ref":"root_000965/B012","relation_type":"near_neighbor","shared_zone":"İki dal da Yemen coğrafyası içinde yer adı ve o yere aidiyet bildirir."},{"boundary_match":"field_only","distinction":"İlişki türü ortaktır, ancak bağlı olunan yer ve buna göre adlandırılan varlıkların kimliği farklıdır.","focus_only":"Bu dal Yemen'e ait kişi, yön ve dokuma türlerini bildirir.","gloss":"yer adına göre aidiyet","neighbor_only":"Komşu dal Katar'a ait dokuma, binek ve başka varlıkları bildirir.","neighbor_ref":"root_001238/B013","relation_type":"same_field","shared_zone":"Her iki dal da bir yer adına aidiyet kurar ve o yerle anılan dokuma türlerini kapsar."}],"source_phrase_ar":"وكذلك اليمن وهو بلد ورجل يماز وسيف يمان (maqayis)؛ واليمن أرض وجيل من الناس واليمن ما كان على يمين القبلة (ayn)؛ اليمن بلاد للعرب والنسبة إليها يمنى ويمان وتيمن تنسب إلى اليمن واليمنة البردة من برود اليمن (sihah)؛ تيامن القوم وأيمنوا إذا أتوا اليمن وقولهم رجل يمان منسوب إلى اليمن واليمنة ضرب من برود اليمين (tahdhib)","source_summary":"Kaynaklar Yemen'i ülke, toprak ve halk adı olarak verir; bu yere ait kişi ve nesne adları, Yemen yönüne hareket ve Yemen dokumasından örtü de yer merkezli türevlerdir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"بلاد اليمن وأهلها والنسبة إليها وما يتجه إلى ناحية اليمن وما ينسب إلى برودها","what_is_not_ar":"البركة واليد اليمنى والحلف والقوة"},"support_links":[]},{"boundary":"Antlaşmayla bağlı kişi ile kesin sahiplik bildirimi ayrı tutulur; genel ant, el veya güç anlamı bu dala taşınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001698/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"antlaşma bağı veya kesin sahiplik bildiren sağ el sözleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sağ el söyleminin yalnız belirli sözlerde bağlayıcı ilişki veya kesin tasarruf bildirmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Konuşanla arasında karşılıklı antlaşma bulunan bağlı kişi."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şey üzerinde sıradan elde bulundurmadan daha kesin sahiplik ve tasarruf."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki ayrı sınırlı kullanımını, aralarında yapay bir genel sahiplik anlamı kurmadan birlikte gösterir.","boundary_detail":"Antlaşmayla bağlı kişi ile kesin sahiplik bildirimi ayrı tutulur; genel ant, el veya güç anlamı bu dala taşınmaz.","branch_image_ar":"ملك اليمين وعقده","concept_gloss":"antlaşma bağı veya kesin sahiplik bildiren sağ el sözleri","contextual_glosses":[{"applicability":"Konuşan ile başka bir kişi arasındaki karşılıklı antlaşma ilişkisini adlandıran sözde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiler arasındaki karşılıklı antlaşma bağını ve bağlı kişi rolünü korur."},"facet_ids":["F002"],"text":"antlaşmayla bağlı kişi","usage_role":"contextual"},{"applicability":"Konuşanın bir şey üzerindeki güçlü ve tartışmasız sahiplik ile tasarrufunu bildiren sözde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sıradan elde bulundurmadan güçlü kesin sahiplik ve tasarruf anlamını korur."},"facet_ids":["F003"],"text":"kesin sahip olduğum şey","usage_role":"contextual"}],"definition":"Belirli sağ el sözlerinde kurulan bağlayıcı ilişki: biri konuşanla arasında antlaşma bulunan kişiyi, diğeri konuşanın bir şey üzerindeki kesin sahiplik ve tasarrufunu bildirir. Bu iki kullanımdan genel bir yalın anlam çıkarılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sağ el söyleminin yalnız belirli sözlerde bağlayıcı ilişki veya kesin tasarruf bildirmesi."},{"facet_id":"F002","role":"specialization","statement":"Konuşanla arasında karşılıklı antlaşma bulunan bağlı kişi."},{"facet_id":"F003","role":"specialization","statement":"Bir şey üzerinde sıradan elde bulundurmadan daha kesin sahiplik ve tasarruf."}],"identity_rationale":"Kaynak ifadesi tek bir genel sahiplik anlamı değil, iki ayrı sınırlı kullanım verir: konuşanla arasında antlaşma bulunan kişi ve konuşanın kesin sahiplik ile tasarrufunu bildiren söz. Dal bu iki kullanım korunarak tutulabilir, fakat bunlardan yalın ve sınırsız bir 'sağ el sahipliği' anlamı çıkarılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"aranda antlaşma bulunan bağlı kişi"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"kesin sahip olduğum ve tasarrufumda bulunan şey"}],"lexicalization_note":"Dal yalnız tanıklanan iki sınırlı sözde geçerlidir; antlaşma bağı ve kesin sahiplik anlamları genelleştirilmeden ayrı ayrı tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tanıklanan iki kullanımın söz güvencesi ve somut sağ el ile karıştırılmasını önleyen iç komşular en yararlı karşılaştırmaları sağladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişiler arasındaki kurulmuş ilişkiyi adlandırır; komşu dal ise bir sözü kutsal tanıklıkla güvenceye bağlama eylemidir.","focus_only":"Bu dal kurulmuş antlaşmayla bağlı kişiyi ve ayrı bir kesin sahiplik sözünü kapsar.","gloss":"antlaşma bağı ile ant içme","neighbor_only":"Komşu dal kutsal tanıklıkla ant içme eylemini ve ant sözlerini kapsar.","neighbor_ref":"root_001698/B003","relation_type":"near_neighbor","shared_zone":"İki dal da sözle kurulan bağlayıcılık ve yükümlülük alanına girer."},{"boundary_match":"partial","distinction":"Bu dalda sağ el ilişki ve tasarruf bildiren sözün parçasıdır; komşu dalda doğrudan organ veya yöndür.","focus_only":"Bu dal sağ el söylemini antlaşma bağı ve kesin sahiplik için sınırlı biçimde kullanır.","gloss":"bağlayıcı sağ el sözü ile somut sağ el","neighbor_only":"Komşu dal somut sağ eli, sağ bedensel yanı ve sağ yönü bildirir.","neighbor_ref":"root_001698/B002","relation_type":"near_neighbor","shared_zone":"İki dal aynı sağ el imgesini taşır."}],"source_phrase_ar":"ومولى اليمين هو من بينك وبينه معاهدة وملك يميني أنفذ وأبلغ من قولهم في يدي (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, antlaşmayla bağlı kişiyi ve elde bulundurmadan daha güçlü kesin sahiplik bildirimini yan yana verir."}],"source_summary":"Tanıklanan iki kullanım, sağ el söylemini birinde kişiler arası antlaşma bağına, diğerinde kesin sahiplik ve tasarrufa bağlar; aralarında bu sınırlı bağlayıcılık dışında tek bir genel anlam kurulmaz.","sources":["MU"],"what_is_ar":"الملك والحيازة والمعاهدة المنسوبة إلى اليمين","what_is_not_ar":"الحلف المجرد والجارحة المجردة والبركة"},"support_links":[]},{"boundary":"Dal yalnız ölmek anlamındaki özel kullanımı kapsar; uğur umma, sağa gitme veya gömme eyleminin kendisi bu dalın çekirdeği değildir.","branch_kind":"bare","branch_ref":"root_001698/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","surface_ar":"مَيْمَنَةِ"}],"gloss":"ölmek; mezarda sağ yana yatırılmayla ilişkilendirilen kullanım","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin yaşamının sona ermesi, yani ölmesi."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ölüm anlamının, ölünün mezarda sağ yanına yatırılmasıyla açıklanan bağlantısı."}}],"root_ar":"ي م ن","root_id":"root_001698","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölüm çekirdeğini ve sağ yana yatırılma üzerinden kurulan açıklayıcı bağlantıyı birlikte gösterir.","boundary_detail":"Dal yalnız ölmek anlamındaki özel kullanımı kapsar; uğur umma, sağa gitme veya gömme eyleminin kendisi bu dalın çekirdeği değildir.","branch_image_ar":"التيمن الموت","concept_gloss":"ölmek; mezarda sağ yana yatırılmayla ilişkilendirilen kullanım","contextual_glosses":[{"applicability":"Fiilin bir kişinin yaşamının sona erdiğini bildirdiği doğal anlatım bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir kişinin yaşamının sona ermesi anlamını doğal Türkçe fiille eksiksiz korur."},"facet_ids":["F001"],"text":"öldü","usage_role":"contextual"}],"definition":"Bir kişinin ölmesi; kullanım, ölünün mezarda sağ yanına yatırılmasıyla açıklanır. Sağ yana yatırma ölümün kendisiyle eşitlenmez, yalnız anlam bağlantısını kurar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin yaşamının sona ermesi, yani ölmesi."},{"facet_id":"F002","role":"associated_use","statement":"Ölüm anlamının, ölünün mezarda sağ yanına yatırılmasıyla açıklanan bağlantısı."}],"identity_rationale":"Kaynak ifadesi belirli fiili açıkça ölmek anlamında verir ve bu kullanımı ölünün mezarda sağ yanına yatırılmasıyla açıklar. Bu açıklama uğur veya yönelme anlamı değil, ölüm anlamının gerekçesidir.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"öldü; mezarda sağ yanına yatırılmasıyla ilişkilendirilen kullanım"}],"lexicalization_note":"Tanım yalın ölüm kullanımını esas alır ve mezarda sağ yana yatırılmayı yalnız bu anlamı açıklayan bağlantı olarak tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ölüm sonucunu can verme sürecinden ve ölüm sonrası gömme işleminden ayıran iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ölüm sonucunu adlandırır; komşu dal o sonuca yaklaşırken yaşanan can verme sürecini öne çıkarır.","focus_only":"Bu dal ölüm olayını, mezardaki sağ yan konumuyla açıklanan özel bir fiille bildirir.","gloss":"ölmek ile can verme süreci","neighbor_only":"Komşu dal can verme sırasında yaşanan son çekişme ve süreci bildirir.","neighbor_ref":"root_001489/B016","relation_type":"near_neighbor","shared_zone":"İki dal da yaşamın sona erdiği ölüm durumuna ilişkindir."},{"boundary_match":"thematic_only","distinction":"Bu dal yaşamın sona ermesidir; komşu dal ölümden sonra bedenin örtülmesi ve toprağa konmasıdır.","focus_only":"Bu dal kişinin ölmesini bildirir.","gloss":"ölüm ve ölünün gömülmesi","neighbor_only":"Komşu dal ölünün gizlenmesini, gömülmesini ve mezar ya da kefenle örtülmesini bildirir.","neighbor_ref":"root_000266/B009","relation_type":"thematic","shared_zone":"İki dal aynı ölüm ve defin senaryosunda art arda yer alır."}],"source_phrase_ar":"والتيمن الموت يقال تيمن فلان تيمنا إذا مات والأصل فيه أنه يوسد يمينه إذا مات في قبره (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, ölmek anlamını verir ve bunu ölünün mezarda sağ yanına yatırılmasıyla gerekçelendirir."}],"source_summary":"Özel kullanım bir kişinin ölmesini bildirir ve anlamın sağ tarafla ilişkisini, ölünün mezarda sağ yanına yatırılması geleneği üzerinden açıklar.","sources":["TA"],"what_is_ar":"التيمن بمعنى الموت لما يوسد الميت يمينه","what_is_not_ar":"التيمن بمعنى التبرك أو قصد ناحية اليمن"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["90:18:1"],"branch_refs":[],"candidate_id":"cand_360c52b3d200914f1e60","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:18:1:audible-suspension","source_type":"word_analysis","support_ids":["sup_20d1355cdf4ba2332399","sup_8271ddab876f7ff96476"],"title":"long deictic onset","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:1","qac_refs":["90:18:1:1"],"status":"accepted"}},{"anchor_refs":["90:18:1"],"branch_refs":[],"candidate_id":"cand_77b5d9673fb83e053e5d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:18:1:boundary-compression","source_type":"word_analysis","support_ids":["sup_1d73b9c01291c161a601","sup_20d1355cdf4ba2332399"],"title":"boundary compression","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:1","qac_refs":["90:18:1:1"],"status":"accepted"}},{"anchor_refs":["90:18:1"],"branch_refs":[],"candidate_id":"cand_af81abab860094a9cb1b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:18:1:evaluative-distance","source_type":"word_analysis","support_ids":["sup_20d1355cdf4ba2332399","sup_61e5946a594d3ea9fb79"],"title":"evaluative distance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:1","qac_refs":["90:18:1:1"],"status":"accepted"}},{"anchor_refs":["90:18:1"],"branch_refs":[],"candidate_id":"cand_4dd4fd52891cc4764466","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:18:1:nominal-verdict-subject","source_type":"word_analysis","support_ids":["sup_20d1355cdf4ba2332399","sup_d9b547a2309e2d43b9c0"],"title":"verdict subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:1","qac_refs":["90:18:1:1"],"status":"accepted"}},{"anchor_refs":["90:18:1"],"branch_refs":[],"candidate_id":"cand_c348ced4cae8b33794ef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:18:1:prior-group-reference","source_type":"word_analysis","support_ids":["sup_20d1355cdf4ba2332399","sup_91a260eb93505fb0d510"],"title":"resolved prior group","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:1","qac_refs":["90:18:1:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_0fa00c73707504c599f4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:belonging-sense","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_89d85897c3f1b30bd9ff"],"title":"belonging over casual friendship","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_1499167b611e98483575","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:construct-binding","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_9a1a3d2c0a1831e2274d"],"title":"construct-bound title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_ba1b39ee18e3085f0c95","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:human-predicate-class","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_cd42783c4189d9e15f32"],"title":"human predicate class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_1c3ba384810eceb1259b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:paired-title-and-sound","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_cb117fb9080586a64e2f"],"title":"paired title and sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_f3405665bf9c1b79d67f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:participial-class-form","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_e8479a58a2459b9354a0"],"title":"participial cohort form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_553274c36f5060e9eb63","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:right-side-formula-field","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_e8c84b3c4ccd1435b845"],"title":"right-side formula field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_725dc0d2eb796f1e9c59","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:route-becomes-identity","source_type":"word_analysis","support_ids":["sup_46d0612e82c8b1835f69","sup_ba55520a4dc568ae11ab"],"title":"route becomes identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:2","qac_refs":["90:18:2:1"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_504915582df47a195d8d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:closure-from-mercy-to-status","source_type":"word_analysis","support_ids":["sup_6a1046cd6bb4385376b9","sup_ea619aded3dfca3b82d3"],"title":"mercy becomes status","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_207d615038c903a7d997","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:definite-genitive-completion","source_type":"word_analysis","support_ids":["sup_6a1046cd6bb4385376b9","sup_a4c5c307eb5a392bfd18"],"title":"definite genitive completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_6335d7a8c19f9bafb691","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:formula-and-pairing","source_type":"word_analysis","support_ids":["sup_4ec88644f50a980361d8","sup_6a1046cd6bb4385376b9"],"title":"formula and pairing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_3590847f3738b8418288","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:meem-domain-form","source_type":"word_analysis","support_ids":["sup_5fcef1547a427ef755c7","sup_6a1046cd6bb4385376b9"],"title":"meem-form domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_6dff3e1415e0a174c14c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:right-blessing-allotment","source_type":"word_analysis","support_ids":["sup_6a1046cd6bb4385376b9","sup_9b7eba86cb8993cf0f03"],"title":"right-side blessing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_e24ab459586f2180e9ff","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:same-surah-opposite","source_type":"word_analysis","support_ids":["sup_0f0599411bf955deef44","sup_6a1046cd6bb4385376b9"],"title":"same-surah opposite","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_dbdb948f4ca3b090e4f4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:single-known-pole","source_type":"word_analysis","support_ids":["sup_6a1046cd6bb4385376b9","sup_758b543f7637b96a5156"],"title":"single known pole","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_9c902a1247c462e0cf97","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:sound-closure","source_type":"word_analysis","support_ids":["sup_6a1046cd6bb4385376b9","sup_e60d1eaaf0e3b01f6b42"],"title":"nasal closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:18:3","qac_refs":["90:18:3:1","90:18:3:2"],"status":"accepted"}},{"anchor_refs":["90:18:2"],"branch_refs":[],"candidate_id":"cand_a255a60eea1ec4260c7e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000844"],"scope":"focus_ayah","source_local_id":"90:18:2:1","source_type":"qac_morpheme","support_ids":["sup_3d404cbbe6db2cd37410"],"title":"QAC root occurrence: ص ح ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:18:3"],"branch_refs":[],"candidate_id":"cand_c6c8f809d2392bf434f2","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001698"],"scope":"focus_ayah","source_local_id":"90:18:3:2","source_type":"qac_morpheme","support_ids":["sup_ad17a1c04e6a45de984e"],"title":"QAC root occurrence: ي م ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:18","branch_refs":["root_000844/B001","root_001698/B002"],"candidate_id":"cand_04fd5b234f3dc5ca3b01","commentary_obligation":"review","hft_ref":"hft_73795790b8ac7ecd89af","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_affiliation_axis","source_type":"hft","support_ids":["sup_8c1771c59d9dbffb6dba"],"title":"base_affiliation_axis","trust":"legacy_unbound"},{"anchor_refs":["90:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:18","branch_refs":["root_000844/B002","root_001698/B001"],"candidate_id":"cand_92fb5a8e6344a4e767a0","commentary_obligation":"review","hft_ref":"hft_42cf7569593337ae83c7","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_protective_blessing","source_type":"hft","support_ids":["sup_b0b3565f14a959742289"],"title":"base_protective_blessing","trust":"legacy_unbound"},{"anchor_refs":["90:18"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:18","branch_refs":["root_000844/B004","root_001698/B004"],"candidate_id":"cand_e593f23cda67de7e3223","commentary_obligation":"review","hft_ref":"hft_d07a989a58dad18320c6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_carried_rightful_force","source_type":"hft","support_ids":["sup_2f25bfde6e82a7d8f8d7"],"title":"base_carried_rightful_force","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ","qac_morphemes":[{"lemma_ar":"أُولَٰٓئِك","morph_features":"STEM|POS:DEM|LEM:>uwla`^}ik|P","morpheme_role":"STEM","pos":"DEM","qac_ref":"90:18:1:1","qac_word_ref":"90:18:1","root_ar":"","surface_ar":"أُو۟لَٰٓئِكَ"},{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","root_ar":"ص ح ب","surface_ar":"أَصْحَٰبُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:18:3:1","qac_word_ref":"90:18:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","root_ar":"ي م ن","surface_ar":"مَيْمَنَةِ"}],"word_analysis_qac_refs":[["90:18:1:1"],["90:18:2:1"],["90:18:3:1","90:18:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:18:1","90:18:2","90:18:3"]},"focus_surface_evidence":{"arabic_uthmani":"أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ","qac_morphemes":[{"lemma_ar":"أُولَٰٓئِك","morph_features":"STEM|POS:DEM|LEM:>uwla`^}ik|P","morpheme_role":"STEM","pos":"DEM","qac_ref":"90:18:1:1","qac_word_ref":"90:18:1","root_ar":"","surface_ar":"أُو۟لَٰٓئِكَ"},{"lemma_ar":"أَصْحَٰب","morph_features":"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:2:1","qac_word_ref":"90:18:2","root_ar":"ص ح ب","surface_ar":"أَصْحَٰبُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:18:3:1","qac_word_ref":"90:18:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَيْمَنَة","morph_features":"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"90:18:3:2","qac_word_ref":"90:18:3","root_ar":"ي م ن","surface_ar":"مَيْمَنَةِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:18:1:1"],["90:18:2:1"],["90:18:3:1","90:18:3:2"]],"word_analysis_refs":["90:18:1","90:18:2","90:18:3"],"word_rows":[{"analysis_record_ref":"90:18:1","analytic_gloss_range_en":"masculine plural distal demonstrative subject, locally pointing back to the plural group described in 90:17","analytic_root_gloss_range_en":null,"qac_refs":["90:18:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"أُو۟لَٰٓئِكَ","transliteration":"ulāʾika"}},{"analysis_record_ref":"90:18:2","analytic_gloss_range_en":"construct plural predicate: companions, possessors, people of, or adherents, locally narrowed to a right-side class title","analytic_root_gloss_range_en":"companionship, association, possession-like attachment, protective accompaniment, compliance, and unrelated material/color branches; local syntax selects durable class belonging through iḍāfa","qac_refs":["90:18:2:1"],"root":{"arabic":"ص ح ب","transliteration":"ṣ-ḥ-b"},"surface":{"arabic":"أَصْحَٰبُ","transliteration":"aṣḥābu"}},{"analysis_record_ref":"90:18:3","analytic_gloss_range_en":"definite genitive meem-form noun naming the right-side, blessed domain or station that completes the construct title","analytic_root_gloss_range_en":"right side, blessing, auspicious fortune, right-hand pledge, strength, possession, Yemen, and death-by-right-side branches; local form and syntax select the right-side blessed station","qac_refs":["90:18:3:1","90:18:3:2"],"root":{"arabic":"ي م ن","transliteration":"y-m-n"},"surface":{"arabic":"ٱلْمَيْمَنَةِ","transliteration":"al-maymanati"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["90:18"],"branch_refs":["root_000844/B001","root_001698/B002"],"candidate_id":"cand_04fd5b234f3dc5ca3b01","evidence_scope":"focus_ayah","hft_ref":"hft_73795790b8ac7ecd89af","item_id":"base_affiliation_axis","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_affiliation_axis","support_id":"sup_8c1771c59d9dbffb6dba"},{"anchor_refs":["90:18"],"branch_refs":["root_000844/B002","root_001698/B001"],"candidate_id":"cand_92fb5a8e6344a4e767a0","evidence_scope":"focus_ayah","hft_ref":"hft_42cf7569593337ae83c7","item_id":"base_protective_blessing","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_protective_blessing","support_id":"sup_b0b3565f14a959742289"},{"anchor_refs":["90:18"],"branch_refs":["root_000844/B004","root_001698/B004"],"candidate_id":"cand_e593f23cda67de7e3223","evidence_scope":"focus_ayah","hft_ref":"hft_d07a989a58dad18320c6","item_id":"base_carried_rightful_force","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_carried_rightful_force","support_id":"sup_2f25bfde6e82a7d8f8d7"}],"diagnostics":[],"lane_counts":{"global":20,"macro":4,"micro":3},"packet_summary":{"ayah_count":20,"focus_ref":"90:18","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:18","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"90:18","lane":"micro","linguistic_source_ref":"90:18","surface_ref":"90:18","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:18","target_tokens":[["İşte",["90:18:1"]],["onlar",["90:18:1"]],["sağ",["90:18:3"]],["tarafın",["90:18:3"]],["insanlarıdır",["90:18:2"]]],"text":"İşte onlar sağ tarafın insanlarıdır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:same-surah-opposite","source_type":"word_analysis","support_id":"sup_0f0599411bf955deef44","text":"{\"blocking_evidence\":null,\"headline\":\"same-surah opposite\",\"reader_payoff\":\"The reader notices that 90:18 is the first half of a paired classification, with the opposite side-term arriving in 90:19 rather than a new unrelated topic.\",\"reason\":\"The next ayah supplies the antonymic side-term, making the local word a polarity marker in a same-surah pair.\",\"representative_source_ids\":[\"QS-9075c541\",\"QE-8e8680d9\",\"ME-8384c053\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1:boundary-compression","source_type":"word_analysis","support_id":"sup_1d73b9c01291c161a601","text":"{\"blocking_evidence\":null,\"headline\":\"boundary compression\",\"reader_payoff\":\"The reader notices the hinge from process to status: multiple acts in 90:17 are compressed into one pointer before the title is pronounced.\",\"reason\":\"The demonstrative is a single fused deictic unit at the start of a new nominal clause, and the attachment evidence keeps its antecedent in the prior ayah.\",\"representative_source_ids\":[\"QF-2df38f01\",\"QF-db72e24b\",\"QT-00eca35c\",\"QT-e79ab806\",\"MT-cd738c85\",\"QB-4c31293e\",\"QY-eb83bd5c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1","source_type":"word_analysis","support_id":"sup_20d1355cdf4ba2332399","text":"{\"gloss_range\":\"masculine plural distal demonstrative subject, locally pointing back to the plural group described in 90:17\",\"prose\":\"{{ar:أُو۟لَٰٓئِكَ}} ({{tr:ulāʾika}}) begins by pointing back, so the ayah does not introduce a new moral type from scratch. Its masculine plural form gathers the believers shaped in 90:17 by faith, endurance-counsel, and mercy-counsel, not the nearby abstract mercy noun alone. Because it is the subject of a verbless verdict clause, the earlier verbal process is now held still as identity: that delimited group is titled {{ar:أَصْحَٰبُ ٱلْمَيْمَنَةِ}} ({{tr:aṣḥābu al-maymanati}}). The transition comes without a wa- or fa- connector, so the prior sequence is resolved into a verdict rather than simply coordinated with another act. The distal demonstrative also gives the discourse-near group evaluative prominence, and its long, fused opening shape lets the act of pointing linger before the compact title arrives.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أُو۟لَٰٓئِكَ}} ({{tr:ulāʾika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:18:2:1","source_type":"qac_morpheme","support_id":"sup_3d404cbbe6db2cd37410","text":"{\"lemma_ar\":\"أَصْحَٰب\",\"morph_features\":\"STEM|POS:N|LEM:>aSoHa`b|ROOT:SHb|MP|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:18:2:1\",\"qac_word_ref\":\"90:18:2\",\"root_ar\":\"ص ح ب\",\"surface_ar\":\"أَصْحَٰبُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2","source_type":"word_analysis","support_id":"sup_46d0612e82c8b1835f69","text":"{\"gloss_range\":\"construct plural predicate: companions, possessors, people of, or adherents, locally narrowed to a right-side class title\",\"prose\":\"{{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}}) is the predicate head that turns the pointer into a social and eschatological title. It is plural and human, so the classification lands on the people described in 90:17 rather than on the abstract qualities of patience or mercy. Its construct bareness is not looseness: the word leans forward into {{ar:ٱلْمَيْمَنَةِ}} ({{tr:al-maymanati}}), making belonging to the right-side domain inseparable from the name. The root field of {{ar:ص ح ب}} ({{tr:ṣ-ḥ-b}}) keeps association and attachment audible, so the title means a settled people-of status, not casual friendship or a new action. The form also participates in the familiar right-hand companion field, including 56:27, while 90:18 keeps its exact {{ar:ٱلْمَيْمَنَةِ}} ({{tr:al-maymanati}}) wording marked beside broader right-hand formulas, grounds that title in the local path of faith, patience, and mercy, and prepares the side-flipped counterpart in 90:19.\",\"root_display\":\"{{ar:ص ح ب}} ({{tr:ṣ-ḥ-b}})\",\"root_gloss_range\":\"companionship, association, possession-like attachment, protective accompaniment, compliance, and unrelated material/color branches; local syntax selects durable class belonging through iḍāfa\",\"surface_display\":\"{{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:formula-and-pairing","source_type":"word_analysis","support_id":"sup_4ec88644f50a980361d8","text":"{\"blocking_evidence\":null,\"headline\":\"formula and pairing\",\"reader_payoff\":\"The reader notices that the local title participates in a larger Quranic sorting formula, while 90:18 supplies faith, patience, and mercy as the local grammar behind that sorting.\",\"reason\":\"The formula rows give concrete references, especially 56:8-9, and the local construct phrase supports a companion-side classification without needing any fallback routing.\",\"representative_source_ids\":[\"QI-cb26cb75\",\"MI-5add9ed2\",\"QE-1e0e0943\",\"QY-8671fe07\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:meem-domain-form","source_type":"word_analysis","support_id":"sup_5fcef1547a427ef755c7","text":"{\"blocking_evidence\":null,\"headline\":\"meem-form domain\",\"reader_payoff\":\"The reader notices that the ayah selects a marked station-like form from a broad root family, concentrating the short verdict in this final word.\",\"reason\":\"QAC tags the word as a GERUND_MEEM noun, and contextual evidence shows this exact form as low occurrence and tightly tied to the companion-side title.\",\"representative_source_ids\":[\"QF-08fd80a0\",\"QF-e204bc98\",\"MF-efaa4c21\",\"QI-4fa65469\",\"QI-e3f02145\",\"QH-dcd5bae0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1:evaluative-distance","source_type":"word_analysis","support_id":"sup_61e5946a594d3ea9fb79","text":"{\"blocking_evidence\":null,\"headline\":\"evaluative distance\",\"reader_payoff\":\"The reader notices that distance is not mainly physical here; the demonstrative lifts the prior group into marked evaluative view before naming them.\",\"reason\":\"The referent is immediately recoverable from 90:17, so the distal force is best read as evaluative prominence rather than spatial remoteness.\",\"representative_source_ids\":[\"QS-255056a6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3","source_type":"word_analysis","support_id":"sup_6a1046cd6bb4385376b9","text":"{\"gloss_range\":\"definite genitive meem-form noun naming the right-side, blessed domain or station that completes the construct title\",\"prose\":\"{{ar:ٱلْمَيْمَنَةِ}} ({{tr:al-maymanati}}) completes the title and carries the verdict's landing weight. Its feminine singular genitive form is not adjective agreement with {{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}}); it is the iḍāfa complement that defines what kind of companions are meant. The root field of {{ar:ي م ن}} ({{tr:y-m-n}}) lets right side, blessing, and favorable allotment meet, while the rare meem-form steers the word toward a domain or station rather than merely a hand, oath, or other branch. As the final word, it turns the mercy-and-patience community of 90:17 into a spatially and morally favorable classification, anticipates the opposite side-term in 90:19, and joins the exact maymanah and mashʾamah sorting of 56:8-9 while still resonating with the wider right-hand title field. Its nasal close and shared -ah cadence carry the sound handoff from mercy into right-side classification and toward the coming contrast.\",\"root_display\":\"{{ar:ي م ن}} ({{tr:y-m-n}})\",\"root_gloss_range\":\"right side, blessing, auspicious fortune, right-hand pledge, strength, possession, Yemen, and death-by-right-side branches; local form and syntax select the right-side blessed station\",\"surface_display\":\"{{ar:ٱلْمَيْمَنَةِ}} ({{tr:al-maymanati}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:single-known-pole","source_type":"word_analysis","support_id":"sup_758b543f7637b96a5156","text":"{\"blocking_evidence\":null,\"headline\":\"single known pole\",\"reader_payoff\":\"The reader notices that the final noun names one recognizable category, not one favorable trait among many.\",\"reason\":\"The singular definite nominal shape supports a stable domain reading, and no guardrail evidence contradicts that classification payoff.\",\"representative_source_ids\":[\"QG-3770adb9\",\"QF-87918971\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1:audible-suspension","source_type":"word_analysis","support_id":"sup_8271ddab876f7ff96476","text":"{\"blocking_evidence\":null,\"headline\":\"long deictic onset\",\"reader_payoff\":\"The reader notices that the sound of the opening delays closure, making the pointer itself felt before the title arrives.\",\"reason\":\"The phonetic payoff is not contradicted by the grammar; it supports the same opening deictic role rather than creating a separate parse.\",\"representative_source_ids\":[\"QP-069574e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:belonging-sense","source_type":"word_analysis","support_id":"sup_89d85897c3f1b30bd9ff","text":"{\"blocking_evidence\":null,\"headline\":\"belonging over casual friendship\",\"reader_payoff\":\"The reader notices that the title pictures durable attachment to a domain: companion, possessor, and people-of senses converge, while casual friendship is not the local force.\",\"reason\":\"V4 accepts association and accompaniment for {{ar:ص ح ب}} ({{tr:ṣ-ḥ-b}}), but the genitive complement is a side or station, so the local sense is people attached to or characterized by that domain.\",\"representative_source_ids\":[\"QG-64134aaa\",\"QS-35b9452a\",\"QS-68e090e0\",\"QS-aa2e8fe7\",\"QS-c9be3f2a\",\"MS-1963d8fd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1:prior-group-reference","source_type":"word_analysis","support_id":"sup_91a260eb93505fb0d510","text":"{\"blocking_evidence\":null,\"headline\":\"resolved prior group\",\"reader_payoff\":\"The reader notices that the right-side title belongs to the exact faith, patience, and mercy community described in 90:17, not to an open class of good people.\",\"reason\":\"The attachment evidence resolves the masculine plural demonstrative back to the preceding plural relative group, and QAC identifies it as a nominative demonstrative subject.\",\"representative_source_ids\":[\"QG-0c5f0806\",\"QG-6b418ae7\",\"QI-fc8c2db9\",\"QB-5d1da107\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:construct-binding","source_type":"word_analysis","support_id":"sup_9a1a3d2c0a1831e2274d","text":"{\"blocking_evidence\":null,\"headline\":\"construct-bound title\",\"reader_payoff\":\"The reader notices that the companions cannot be understood apart from the final right-side value term; the phrase is one bound title.\",\"reason\":\"The attachment pass marks an iḍāfa relation from {{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}}) to the final genitive, so the apparent bareness is construct dependency rather than indefiniteness.\",\"representative_source_ids\":[\"QG-4560d4b2\",\"QG-82c047a1\",\"QF-567e519c\",\"ME-44800bf4\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:right-blessing-allotment","source_type":"word_analysis","support_id":"sup_9b7eba86cb8993cf0f03","text":"{\"blocking_evidence\":null,\"headline\":\"right-side blessing\",\"reader_payoff\":\"The reader notices that the verdict is both spatial and moral: the people are placed on the favorable side and associated with blessed allotment, while oath, Yemen, death, and bare hand branches are not selected.\",\"reason\":\"V4 lists multiple accepted branches for {{ar:ي م ن}} ({{tr:y-m-n}}), but the local meem-form genitive inside the title selects the right-side blessed-domain branch and only allows the broader root field as pressure.\",\"representative_source_ids\":[\"QS-4af16799\",\"QS-58a64a85\",\"QS-7b00ad6c\",\"QS-acc54e02\",\"QS-f488e37a\",\"MS-1db0752b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:definite-genitive-completion","source_type":"word_analysis","support_id":"sup_a4c5c307eb5a392bfd18","text":"{\"blocking_evidence\":null,\"headline\":\"definite genitive completion\",\"reader_payoff\":\"The reader notices that the clause's identity claim remains incomplete until the final value-domain arrives and defines the companions.\",\"reason\":\"QAC and attachment evidence identify the word as a definite feminine singular genitive complement governed by {{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}}), not as an agreeing adjective.\",\"representative_source_ids\":[\"QG-0f27cc21\",\"QG-19293e37\",\"QG-6e15708a\",\"QG-cf0ac634\",\"MG-a96afe01\",\"QF-0336b74b\",\"QT-43f2d02f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:18:3:2","source_type":"qac_morpheme","support_id":"sup_ad17a1c04e6a45de984e","text":"{\"lemma_ar\":\"مَيْمَنَة\",\"morph_features\":\"STEM|POS:N|LEM:mayomanap|ROOT:ymn|F|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:18:3:2\",\"qac_word_ref\":\"90:18:3\",\"root_ar\":\"ي م ن\",\"surface_ar\":\"مَيْمَنَةِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:route-becomes-identity","source_type":"word_analysis","support_id":"sup_ba55520a4dc568ae11ab","text":"{\"blocking_evidence\":null,\"headline\":\"route becomes identity\",\"reader_payoff\":\"The reader notices that faith, patience-counsel, and mercy-counsel are not restated; they are resolved into the name of the people.\",\"reason\":\"The word sits between the backward-pointing demonstrative and the final genitive domain, so it bridges prior conduct into classification.\",\"representative_source_ids\":[\"QT-0fe63f00\",\"QT-4d80a81b\",\"MT-f28d97c7\",\"QB-b06508d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:paired-title-and-sound","source_type":"word_analysis","support_id":"sup_cb117fb9080586a64e2f","text":"{\"blocking_evidence\":null,\"headline\":\"paired title and sound\",\"reader_payoff\":\"The reader notices both architecture and sound: 90:18 establishes the positive half of a paired classification that 90:19 will reverse, and the heavier title onset gives way to the final side word.\",\"reason\":\"The same head recurs in 90:19 with a changed side-term, and the local adjacency of the construct pair supports reading the phrase as a single formulaic unit.\",\"representative_source_ids\":[\"MI-ede7cdac\",\"QE-514c664a\",\"QE-a6bff3b5\",\"QP-42b8268e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:human-predicate-class","source_type":"word_analysis","support_id":"sup_cd42783c4189d9e15f32","text":"{\"blocking_evidence\":null,\"headline\":\"human predicate class\",\"reader_payoff\":\"The reader notices that the title names the people formed by the prior ethic, not patience or mercy as abstractions.\",\"reason\":\"QAC identifies {{ar:أَصْحَٰبُ}} ({{tr:aṣḥābu}}) as a broken masculine plural nominative predicate, and attachment evidence links it to the demonstrative subject.\",\"representative_source_ids\":[\"QG-0390d713\",\"QG-9271867e\",\"QF-da3ba066\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:1:nominal-verdict-subject","source_type":"word_analysis","support_id":"sup_d9b547a2309e2d43b9c0","text":"{\"blocking_evidence\":null,\"headline\":\"verdict subject\",\"reader_payoff\":\"The reader notices that 90:18 classifies the already described group in the present shape of a verdict, rather than adding one more deed to the list.\",\"reason\":\"The clause is syntactically forced as nominal, with {{ar:أُو۟لَٰٓئِكَ}} ({{tr:ulāʾika}}) as subject and the construct title as predicate.\",\"representative_source_ids\":[\"QG-edd237d1\",\"MG-e4d97a9a\",\"QT-12ac84bd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:sound-closure","source_type":"word_analysis","support_id":"sup_e60d1eaaf0e3b01f6b42","text":"{\"blocking_evidence\":null,\"headline\":\"nasal closure\",\"reader_payoff\":\"The reader notices that the final word does acoustic work too: it softens the close after the heavier companion head and connects mercy, right-side classification, and the coming contrast by cadence.\",\"reason\":\"The sound rows are locally coherent with the same final-word position and do not conflict with the grammatical analysis.\",\"representative_source_ids\":[\"QE-f35bdbb3\",\"QP-cfd89fa0\",\"QP-e8f4ebb2\",\"MP-73ac64ea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:participial-class-form","source_type":"word_analysis","support_id":"sup_e8479a58a2459b9354a0","text":"{\"blocking_evidence\":null,\"headline\":\"participial cohort form\",\"reader_payoff\":\"The reader notices that the ayah names people by a durable relational identity, not by a finite act or by a simple reward noun.\",\"reason\":\"QAC gives the local form as a noun from the active-participial pattern, and contextual data shows the form functioning strongly as a nominal classing expression.\",\"representative_source_ids\":[\"QF-4d71ffc6\",\"QF-9c84aa21\",\"MF-1fba45d7\",\"QI-59dd2111\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:2:right-side-formula-field","source_type":"word_analysis","support_id":"sup_e8c84b3c4ccd1435b845","text":"{\"blocking_evidence\":null,\"headline\":\"right-side formula field\",\"reader_payoff\":\"The reader notices that 90:18 is not an isolated label; it specializes a familiar right-hand companion title by tying it to faith, patience, and mercy.\",\"reason\":\"The row-provided formula evidence is coherent with the local construct title; 56:27 is retained as a concrete formula parallel without controlling the local wording.\",\"representative_source_ids\":[\"QI-01ac878a\",\"QI-415336f8\",\"MI-88254719\",\"QE-5be5ff7b\",\"QY-819b9bea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:18:3:closure-from-mercy-to-status","source_type":"word_analysis","support_id":"sup_ea619aded3dfca3b82d3","text":"{\"blocking_evidence\":null,\"headline\":\"mercy becomes status\",\"reader_payoff\":\"The reader notices the boundary movement from communal practice in 90:17 to spatialized destiny in 90:18.\",\"reason\":\"As the terminal genitive complement, the word resolves the demonstrative and construct head into the value-domain that names the group.\",\"representative_source_ids\":[\"QT-f3651f9f\",\"MT-0b1bb48b\",\"QB-9909b6d0\",\"QB-ca22a20d\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ","ayah_ref":"90:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000844/B001","root_001698/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000844","role":"Sustained companionship turns أصحاب into a relational company whose members remain attached to a shared pole.","root":"ص ح ب","source_ref":"90:18","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001698","role":"The right hand and right side give الميمنة a concrete directional pole for that continuing affiliation.","root":"ي م ن","source_ref":"90:18","source_word_indices":["3"]}],"changed_reading":{"after":"A durable company whose identity is formed by continuing attachment to the right-hand side.","before":"A bare deictic label: those are the people placed on the right."},"confidence":"strong","focus_anchor":"The construct أَصْحَابُ ٱلْمَيْمَنَةِ joins a plural relation noun to a noun of side and orientation.","mechanism":"The companionship branch makes membership a sustained association, while the right-side branch supplies its axis. The phrase therefore classifies by durable side-affiliation rather than by a momentary location.","model_id":"base_affiliation_axis"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_affiliation_axis","source_type":"hft","support_id":"sup_8c1771c59d9dbffb6dba","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ","ayah_ref":"90:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000844/B002","root_001698/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000844","role":"Protective accompaniment makes the company an active medium of keeping, calm, and aid.","root":"ص ح ب","source_ref":"90:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001698","role":"Blessing and good fortune supply the favorable condition sustained by that accompaniment.","root":"ي م ن","source_ref":"90:18","source_word_indices":["3"]}],"changed_reading":{"after":"They are a company held within protective accompaniment whose shared condition is blessing.","before":"The group merely receives a favorable title."},"confidence":"medium","focus_anchor":"أصحاب can image accompaniment that keeps safe, and الميمنة can image blessing rather than geometry alone.","mechanism":"Protective accompaniment and auspicious blessing combine into a condition of being kept in beneficent company. This reading coexists with the spatial one: rightness is experienced as a sheltering relation, not merely assigned as a coordinate.","model_id":"base_protective_blessing"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_protective_blessing","source_type":"hft","support_id":"sup_b0b3565f14a959742289","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ","ayah_ref":"90:18"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000844/B004","root_001698/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000844","role":"Taking or making something accompany another supplies the active carrying relation in أصحاب.","root":"ص ح ب","source_ref":"90:18","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001698","role":"Right-hand power, restraint, and rightful force identify what is carried and how the company is tested.","root":"ي م ن","source_ref":"90:18","source_word_indices":["3"]}],"changed_reading":{"after":"Rightness is a form of power carried as a fitting companion, making the group an active ethical alignment.","before":"Rightness is a static place occupied by a fortunate group."},"confidence":"exploratory","focus_anchor":"The two focus roots permit an active relation: something may be taken along as a fitting companion, and the right hand may signify power, restraint, and rightful force.","mechanism":"Instead of naming passive occupants of a side, the phrase can name people whose companionship carries a fitting form of rightful power. The oddity is useful because it makes rightness a manner of bearing force rather than a badge.","model_id":"base_carried_rightful_force"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_carried_rightful_force","source_type":"hft","support_id":"sup_2f25bfde6e82a7d8f8d7","trust":"legacy_unbound"}]}
</lane_packet_json>
