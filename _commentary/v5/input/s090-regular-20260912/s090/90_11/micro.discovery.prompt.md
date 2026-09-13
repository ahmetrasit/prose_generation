# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **90:11**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s090-regular-20260912/s090/90_11/micro.discovery.json` and modify nothing
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
  "ayah_ref": "90:11",
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
{"analysis_context":{"analysis_id":"s090-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"90:11","host_surah":90,"lane_context_refs":[],"ordered_context_refs":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, çıplak topuk anlamını değil, malzeme olan sinir dokusunu ve ona bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"bağlama ve kiriş yapımında kullanılan sert beyaz tendon","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Beyaz, sert ve dayanıklı sinir ya da tendon dokusu kiriş yapımında kullanılan temel malzemedir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayak bileklerinin arkasındaki gergin tendon, aynı doku adının anatomik bir özelleşmesidir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ok, yay, mızrak ve benzeri araçlar bu dokuyla sarılarak sağlamlaştırılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel malzemesini ve bu malzemenin başlıca işlevini birlikte karşılar.","boundary_detail":"Dal, çıplak topuk anlamını değil, malzeme olan sinir dokusunu ve ona bağlı kullanımları kapsar.","branch_image_ar":"العَقَب الأبيض الشديد","concept_gloss":"bağlama ve kiriş yapımında kullanılan sert beyaz tendon","contextual_glosses":[{"applicability":"Ok, yay, mızrak veya benzeri bir aracın bu malzemeyle bağlandığı yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tendon malzemesini, sarma işlemini ve sağlamlaştırma sonucunu korur."},"facet_ids":["F003"],"text":"tendonla sarıp sağlamlaştırmak","usage_role":"contextual"}],"definition":"Kiriş yapımında ve araçları sarıp sağlamlaştırmada kullanılan beyaz, sert ve dayanıklı sinir ya da tendon dokusudur; ayak bileklerinin arkasındaki gergin tendon da buna bağlı bir anatomik kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Beyaz, sert ve dayanıklı sinir ya da tendon dokusu kiriş yapımında kullanılan temel malzemedir."},{"facet_id":"F002","role":"specialization","statement":"Ayak bileklerinin arkasındaki gergin tendon, aynı doku adının anatomik bir özelleşmesidir."},{"facet_id":"F003","role":"associated_use","statement":"Ok, yay, mızrak ve benzeri araçlar bu dokuyla sarılarak sağlamlaştırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Dalın merkezinde bulunmayan çıplak ayak arkası anlamını ekler.","collision":"Aynı kökün ayak arkasını anlatan ayrı dalıyla karışır.","fit":"displacement","loses":"Sert tendon dokusunu ve bu dokunun malzeme olarak kullanımını yitirir.","preserves":"Ayak bölgesiyle dolaylı anatomik yakınlığı korur."},"text":"topuk"}],"identity_rationale":"Kaynak ifadesi, kiriş yapılan sert beyaz sinir dokusunu, ayak bileği arkasındaki gergin uzantısını ve bu dokuyla araçları sarıp sağlamlaştırma işini birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kiriş yapılan sert beyaz tendon"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ayak bileklerinin arkasındaki gergin tendon"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"oku, yayı ya da mızrağı tendonla sarıp sağlamlaştırmak"}],"lexicalization_note":"Tanım, dokunun yalın adını anatomik uzantısından ve araçları bu dokuyla sarma yapısından ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın sınır karşılaştırması belirli sırt tendonu dalıdır, öteki adaylar yalnız araç, ip veya aynı kökün uzak anlamlarını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu, belirli bir anatomik kaynağa ve kiriş üretimine daralır; odak dalı daha geniş tendon malzemesini ve bağlama kullanımını içerir.","focus_only":"Bu dal, genel sert tendon malzemesini ve onunla araç sarma işini de kapsar.","gloss":"yay kirişi yapılan sırt tendonu","neighbor_only":"Komşu dal, özellikle sırtın iki yanından çıkarılıp yay kirişi yapılan belirli tendon parçalarını anlatır.","neighbor_ref":"root_000698/B008","relation_type":"near_synonym","shared_zone":"İki dal da hayvansal tendonun işlenip yay kirişi yapılmasını kapsar."}],"source_phrase_ar":"العقب العصب الذي تعمل منه الأوتار (ayn); عقب الإنسان والدابة معروف في معنى العصب (jamhara); العقب بالتحريك العصب الذي تعمل منه الأوتار (sihah); عقبت الخوق وعقبت القدح بالعقب (tahdhib); العقب ما يقعب به الرماح والسهام وهو أصلبهما وأمتنهما (maqayis); عقبت الرمح شددته بالعقب (mufradat); العرقوب عقب موتر خلف الكعبين والراء زائدة (maqayis-variant)","source_summary":"Kaynaklar sert sinir dokusunu hem kiriş malzemesi hem de ok, yay ve mızrak gibi araçları bağlayıp güçlendiren malzeme olarak verir; bir biçim çeşidi ayak bileği arkasındaki gergin tendonu gösterir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العَقَب بمعنى العصب أو الوتر الأبيض الصلب الذي تعمل منه الأوتار وتشد به السهام والقداح والرماح والقسي وحلقة القرط، وما اتصل به من العرقوب الموتر خلف الكعبين","what_is_not_ar":"ليس مؤخر القدم المجرد ولا العاقبة ولا العقوبة"},"support_links":[]},{"boundary":"Dal, zaman içindeki genel ardışıklığı değil, ayak arkasından gelişen uzamsal iz ve takip ilişkisini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B002","candidate_links":[{"candidate_id":"cand_4addf1548a483e1bc40d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"topuk ve hemen arkasında kalan iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim ayağın arka bölümü, yani topuktur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayak arkasındaki yer ve iz, birinin hemen ardından gelme ilişkisine genişler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin ardınca çok kimsenin yürümesi, onun çok sayıda izleyeni olduğunu anlatır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Anatomik çekirdeği ve ondan doğan uzamsal art alanı birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Dal, zaman içindeki genel ardışıklığı değil, ayak arkasından gelişen uzamsal iz ve takip ilişkisini kapsar.","branch_image_ar":"مؤخر القدم والأثر","concept_gloss":"topuk ve hemen arkasında kalan iz","contextual_glosses":[{"applicability":"Bir kişinin gittiği yolun veya yaptığı hareketin doğrudan arkasından gelme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki kişinin izine ve arkasındaki yakın konuma bağlı takip ilişkisini korur."},"facet_ids":["F002"],"text":"hemen ardından","usage_role":"contextual"}],"definition":"Ayağın arka bölümü ve bu bölümün gerisinde kalan yer ya da izdir; buna bağlı yapılar birinin hemen ardından gelmeyi veya çok sayıda kişi tarafından izlenmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim ayağın arka bölümü, yani topuktur."},{"facet_id":"F002","role":"extension","statement":"Ayak arkasındaki yer ve iz, birinin hemen ardından gelme ilişkisine genişler."},{"facet_id":"F003","role":"associated_use","statement":"Bir kişinin ardınca çok kimsenin yürümesi, onun çok sayıda izleyeni olduğunu anlatır."}],"identity_rationale":"Kaynak ifadesi ayağın arka bölümünü temel alır ve buradan kişinin hemen arkasındaki iz, yer ve izleyenler için kurulan kullanımlara geçer.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"topuk, ayağın arka bölümü"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"topuklar"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ardınca çok kişi yürüyen, çok izlenen"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birinin hemen ardından, onun izinden"}],"lexicalization_note":"Yalın anatomik anlam, çoğul biçim, çok izleneni anlatan söz ve birinin hemen ardını belirten yapı ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; izden gitme dalı en yararlı karşılaştırmadır, ötekiler yalnız yürüyüş, ayak konumu veya geniş uzam özellikleri paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı anatomik ve uzamsal bir adlandırmadan takip ilişkisine geçer; komşu dalın çekirdeği ise iz sürerek ilerleme eylemidir.","focus_only":"Odak dalında ayağın arka bölümü ve onun gerisindeki yer temel anlamdır.","gloss":"öncekinin izinden gitmek","neighbor_only":"Komşu dal, öncekinin izini izleyerek yol alma eylemini doğrudan anlatır.","neighbor_ref":"root_000011/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişinin ardından onun bıraktığı izi izlemeyi kapsar."}],"source_phrase_ar":"العقب مؤخر القدم (ayn); عقب الإنسان معروف يحرك ويسكن (jamhara); العقب بكسر القاف مؤخر القدم (sihah); عقب القدم مؤخرها وجمعه أعقاب (tahdhib); العقب مؤخر الرجل وجمعه أعقاب (mufradat); من الباب عقب القدم مؤخرها (maqayis); موطأ العقب أي كثير الأتباع (maqayis)","source_summary":"Kaynaklar ayağın arka bölümünde birleşir; aynı görüntü, birinin ardındaki izi ve yeri, hemen ardından gelmeyi ve çok izleyeni olmayı anlatan yapılara temel olur.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العقب بمعنى مؤخر القدم وما خلف الإنسان أو القوم من أثر وموضع يتبع، ومنه وطء العقب وكون الإنسان موطأ العقب","what_is_not_ar":"ليس التعاقب الزمني ولا العقبى ولا الطائر"},"support_links":["sup_e117d9ededbe9a855043"]},{"boundary":"Bu anlam yalnız belirtilen dönüş ve olumsuz dönüş yapılarında geçerlidir; yalın ayak arkası anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_001033/B003","candidate_links":[{"candidate_id":"cand_4addf1548a483e1bc40d","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"dönüp geri çekilmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İleri gidişten sonra yön değiştirip geri çekilme hareketi anlatılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz yapı, uzaklaşanın dönmemesini, arkasına bakmamasını veya beklememesini belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İleri hareketten sonra yönünü tersine çeviren kişi için kullanılan yapıyı doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız belirtilen dönüş ve olumsuz dönüş yapılarında geçerlidir; yalın ayak arkası anlamına genişletilmez.","branch_image_ar":"الرجوع على العقب","concept_gloss":"dönüp geri çekilmek","contextual_glosses":[{"applicability":"Geri dönme, arkaya bakma veya bekleme eylemlerinin olumsuzlandığı kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Uzaklaşmayı ve geriye yönelmenin gerçekleşmemesini açık biçimde korur."},"facet_ids":["F002"],"text":"arkasına bakmadan uzaklaşmak","usage_role":"contextual"}],"definition":"İleri yönelmişken dönüp geri çekilmek veya geldiği yöne dönmektir; olumsuz yapıda ise uzaklaşırken geri dönmemek, arkaya bakmamak ya da beklememektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İleri gidişten sonra yön değiştirip geri çekilme hareketi anlatılır."},{"facet_id":"F002","role":"associated_use","statement":"Olumsuz yapı, uzaklaşanın dönmemesini, arkasına bakmamasını veya beklememesini belirtir."}],"identity_rationale":"Kaynak ifadesi, ileri gidişten sonra dönüp geri çekilmeyi ve olumsuz yapıda geriye dönmemeyi, bakmamayı ya da beklememeyi açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dönüp geri çekilmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"geri dönmedi, arkasına bakmadı veya beklemedi"}],"lexicalization_note":"Tanım bütünüyle geri dönme ve dönmeden uzaklaşma kalıplarına bağlıdır; yalın kök anlamı ileri sürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sırt çevirip uzaklaşma dalı en yakın sınırı verir, diğerleri genel dönüş, sapma veya arkadan alma eylemleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli geri dönüş kalıplarıyla sınırlıdır; komşu dal fiziksel dönüşün yanında soyut yüz çevirme ve yenilgiyi de içerir.","focus_only":"Odak dalı, ilerledikten sonra geldiği yöne fiziksel olarak dönüp çekilmeyi öne çıkarır.","gloss":"dönüp uzaklaşma","neighbor_only":"Komşu dal, savaşta sırt çevirme, sözden yüz çevirme ve yenilgi gibi daha geniş uzaklaşmaları kapsar.","neighbor_ref":"root_000458/B003","relation_type":"near_synonym","shared_zone":"İki dal da ileri yönelişi bırakıp ters yöne dönmeyi anlatabilir."}],"source_phrase_ar":"ولى فلان على عقبه وعقبيه أي انثنى راجعا (ayn); ولى مدبرا ولم يعقب أي لم يعطف ولم ينتظر (sihah); كل راجع معقب ولم يلتفت ولم يرجع (tahdhib); رجع على عقبه وانقلب على عقبيه (mufradat); ولي مدبرا ولم يعقب أي لم يعطف (maqayis)","source_summary":"Kaynaklar, kişinin geldiği yöne dönüp çekilmesinde ve olumsuz biçimde dönmeden, bakmadan veya beklemeden uzaklaşmasında birleşir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"الرجوع والانثناء والنكوص بعد الإقبال، ومنه ولى على عقبه أو عقبيه، ولم يعقب بمعنى لم يعطف أو لم يرجع أو لم يلتفت","what_is_not_ar":"ليس مجرد مؤخر القدم ولا التعاقب الدوري ولا طلب الحق بعده"},"support_links":["sup_e117d9ededbe9a855043"]},{"boundary":"Dal genel sonu veya sonucu değil, bir kişinin kendisinden sonra süren doğrudan soyunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"ardında kalan çocuklar ve torunlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin kendisinden sonra kalan çocukları ve torunları sürmekte olan soyunu oluşturur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olumsuz kalıp, kişinin ardında çocuk veya devam eden bir soy bırakmadığını belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin ölümünden veya ayrılışından sonra soyunu sürdüren alt kuşakları birlikte anlatır.","boundary_detail":"Dal genel sonu veya sonucu değil, bir kişinin kendisinden sonra süren doğrudan soyunu anlatır.","branch_image_ar":"العَقِب من الولد","concept_gloss":"ardında kalan çocuklar ve torunlar","contextual_glosses":[{"applicability":"Bir kişinin kendisinden sonra yaşayan çocuk veya devam eden soy bırakmadığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soyun devam etmemesini ve kişinin ardında alt kuşak kalmamasını korur."},"facet_ids":["F002"],"text":"ardında soy bırakmadı","usage_role":"contextual"}],"definition":"Bir kişinin ardından kalan çocukları ve çocuklarının çocukları, yani sürmekte olan soyudur; olumsuz kullanım kişinin ardında çocuk veya soy bırakmadığını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin kendisinden sonra kalan çocukları ve torunları sürmekte olan soyunu oluşturur."},{"facet_id":"F002","role":"associated_use","statement":"Olumsuz kalıp, kişinin ardında çocuk veya devam eden bir soy bırakmadığını belirtir."}],"identity_rationale":"Kaynak ifadesi, kişinin ardından kalan çocuklarını ve torunlarını açıkça tanımlar; soy bırakmama kalıbı da aynı sınırın olumsuzunu verir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kişinin ardından kalan çocukları ve torunları"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ardında çocuk veya soy bırakmadı"}],"lexicalization_note":"Soy adı ile soy kalmadığını bildiren olumsuz kalıp ayrılır; anlam genel bir sonralık kavramına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel çocuk ve soy dalı en yakın karşılıktır, ötekiler soyun kesilmesi, hane halkı veya özel akrabalık türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında atadan sonra kalma ilişkisi kurucudur; komşu dalda ise genel çocuk ve üreme bağı yeterlidir.","focus_only":"Odak dalı, özellikle bir kişiden sonra kalan ve onun soyunu sürdüren alt kuşakları anlatır.","gloss":"çocuklar ve süren soy","neighbor_only":"Komşu dal, çocuk ve soy kavramını genel üreme ve nesil üretme ilişkisi içinde ele alır.","neighbor_ref":"root_001499/B001","relation_type":"near_synonym","shared_zone":"İki dal da çocukları, torunları ve neslin devamını kapsar."}],"source_phrase_ar":"عقب الرجل ولده وولد ولده الباقون من بعده (ayn); ليست لفلان عاقبة أي ولد وعقب الرجل ولده وولد ولده (sihah); قيل لولد الرجل عقبه وكذلك آخر كل شيء عقبه (tahdhib); استعير العقب للولد وولد الولد وفلان لم يعقب (mufradat); ليس لفلان عاقبة يعني عقبا (maqayis)","source_summary":"Kaynaklar anlamı kişinin ardından kalan çocuklar ve torunlarda birleştirir; soy bırakmama anlatımı bu kavramın olumsuz sınırını gösterir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"ولد الرجل وولد ولده ومن يبقى بعده من نسله، وما ينفى بقولهم لا عقب له، والذرية الباقية في عقب الإنسان","what_is_not_ar":"ليس العاقبة العامة ولا العقبى الجزاء ولا مجرد آخر الشيء"},"support_links":[]},{"boundary":"Dal, tek başına geri dönüşü veya nihai sonucu değil, sonradan gelme, yerini alma ve sıra değişimini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"birbirinin ardından gelme ve yerini alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sonraki öğe öncekinin ardından gelir ve onun bıraktığı yeri alır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki taraflı düzende öğeler sırayla birbirinin yerini alarak dönüşümlü ilerler."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Gece ile gündüzün, görevli toplulukların veya binicilerin sıra değişimi bu düzeni örnekler."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem tek yönlü ardıllığı hem de iki tarafın dönüşümlü biçimde yer değiştirmesini kapsar.","boundary_detail":"Dal, tek başına geri dönüşü veya nihai sonucu değil, sonradan gelme, yerini alma ve sıra değişimini kapsar.","branch_image_ar":"الخلف والتعاقب","concept_gloss":"birbirinin ardından gelme ve yerini alma","contextual_glosses":[{"applicability":"Gece ile gündüz veya iki görevli gibi tarafların dönüşümlü geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dönüşümlü sırayı ve her tarafın ötekinin ardından gelip yerini almasını korur."},"facet_ids":["F002","F003"],"text":"sırayla birbirinin yerini almak","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyden sonra gelmesi ve onun yerini almasıdır; karşılıklı düzenlerde taraflar sırayla birbirinin ardından gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sonraki öğe öncekinin ardından gelir ve onun bıraktığı yeri alır."},{"facet_id":"F002","role":"specialization","statement":"İki taraflı düzende öğeler sırayla birbirinin yerini alarak dönüşümlü ilerler."},{"facet_id":"F003","role":"example","statement":"Gece ile gündüzün, görevli toplulukların veya binicilerin sıra değişimi bu düzeni örnekler."}],"identity_rationale":"Kaynak ifadesi bir şeyin diğerinden sonra gelmesini, onun yerini almasını ve iki tarafın sırayla birbirini izlemesini ortak bir ardıllık çekirdeğinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"öncekinin ardından gelen ve onun yerini alan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ardıl, bir başkasının ardından gelen"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gece ile gündüzün sırayla birbirinin yerini alması"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"sırayla nöbet değiştiren gece ve gündüz görevlileri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"binme veya çalışma sırası, nöbet"}],"lexicalization_note":"Genel ardıl adı, gece ile gündüzün sıra değişimi ve sırayla binme ya da çalışma kullanımları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dönüşümlü yer alma dalı en yakın sınırı verir, diğerleri yalnız nöbet, süreklilik, sonralık veya ilerleme alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal dönüşümlü yer değişimine daha sıkı bağlıdır; odak dalı genel ardıllığı ve sonradan gelen kişiyi de içerir.","focus_only":"Odak dalı, dönüşüm gerekmeksizin bir ardılın öncekinin ardından gelmesini de kapsar.","gloss":"ardından gelip yerini alma","neighbor_only":"Komşu dal, bir şeyin gidip benzerinin yerine gelmesiyle kurulan dönüşümlü değişimi öne çıkarır.","neighbor_ref":"root_000433/B006","relation_type":"near_synonym","shared_zone":"İki dal da öğelerin birbirinin ardından gelerek yer değiştirmesini kapsar."}],"source_phrase_ar":"كل شيء يعقب شيئا فهو عقيبه (ayn;maqayis); العاقب الذي يجيء في أثر صاحبه (jamhara); كل من خلف بعد شيء فهو عاقبه (sihah); كل شيء خلف بعد شيء فهو عاقب له (tahdhib); التعقيب أن يأتي بشيء بعد آخر والمعقبات ملائكة يتعاقبون (mufradat); الليل والنهار يتعاقبان (tahdhib)","source_summary":"Kaynaklar sonradan gelme ve öncekinin yerini alma çekirdeğinde birleşir; gece ile gündüz, görevli topluluklar ve binme nöbetleri bu çekirdeğin dönüşümlü örnekleridir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"مجيء شيء بعد شيء وخلافته له، وتعاقب الليل والنهار والملائكة والطير والإبل والركاب والنوب، والعاقب الذي يأتي في أثر غيره أو يخلفه","what_is_not_ar":"ليس الجزاء والعقوبة المختصة ولا الرجوع والنكوص ولا الصعود الصعب"},"support_links":[]},{"boundary":"Genel sonuç çekirdeği korunmalı, iyi karşılığa özgü kullanım ve hastalık kalıntısı bütün dala yayılmamalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B006","candidate_links":[{"candidate_id":"cand_2919f56e6cc6eab0cc88","lane":"micro"},{"candidate_id":"cand_e16caf2a6d6cae89049f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"sonuç ve varılan son durum","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir süreç veya işin vardığı son durum ve nihai sonuç temel anlamı oluşturur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kullanım sonuç alanını özellikle yararlı ve iyi karşılıkla sınırlar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir eylemin ardından hastalık, pişmanlık, iyilik veya kötülük gibi bir sonuç doğabilir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin bitişini ve o işten sonra ortaya çıkan iyi ya da kötü nihai durumu birlikte anlatır.","boundary_detail":"Genel sonuç çekirdeği korunmalı, iyi karşılığa özgü kullanım ve hastalık kalıntısı bütün dala yayılmamalıdır.","branch_image_ar":"آخر الشيء وعاقبته","concept_gloss":"sonuç ve varılan son durum","contextual_glosses":[{"applicability":"Bir davranışın ardından iyi veya kötü yeni bir durumun doğduğunu bildiren yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki eylem ile ardından doğan sonuç arasındaki neden ilişkisini korur."},"facet_ids":["F003"],"text":"buna yol açtı","usage_role":"contextual"}],"definition":"Bir şeyin sonu veya bir eylemin ardından ortaya çıkan nihai sonuçtur; sonuç iyi ya da kötü olabilir, kimi kullanım iyi karşılığa daralır ve hastalıktan kalan belirti ayrı bir kalıntı örneğidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir süreç veya işin vardığı son durum ve nihai sonuç temel anlamı oluşturur."},{"facet_id":"F002","role":"source_variant","statement":"Bir kullanım sonuç alanını özellikle yararlı ve iyi karşılıkla sınırlar."},{"facet_id":"F003","role":"associated_use","statement":"Bir eylemin ardından hastalık, pişmanlık, iyilik veya kötülük gibi bir sonuç doğabilir."}],"identity_rationale":"Kaynak ifadesi son, sonuç ve bir eylemin doğurduğu iyi ya da kötü durumu destekler; ancak bir kullanım sonucu özellikle iyi karşılıkla sınırlar ve hastalıktan kalan belirtiyi yan bir kalıntı olarak ekler.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"son, sonuç, varılan nihai durum"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"karşılık veya sonuç; kimi kullanımda iyi karşılık"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"buna yol açtı, ardından bunu doğurdu"}],"lexicalization_note":"Son ve sonuç adları, iyi karşılığa daralan biçim ile bir şeyin sonuç doğurmasını anlatan yapıdan ayrı gösterilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; varılan son durum dalı en yakın karşılıktır, ötekiler yalnız bitiş, yarar, neden olunan zarar veya gecikme alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki işin sonucu olma ilişkisi belirgindir; komşu dalda dönüşme ve bir sona varma daha geniştir.","focus_only":"Odak dalı, işin ardından doğan iyi ya da kötü sonucu ve karşılığı da kapsar.","gloss":"varılan son durum","neighbor_only":"Komşu dal, bir şeyin başka bir duruma dönüşmesini veya belirli bir varış noktasına ulaşmasını öne çıkarır.","neighbor_ref":"root_000897/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir sürecin sonunda ulaşılan durumu anlatır."}],"source_phrase_ar":"أتى فلان خبرا فعقب بخير منه (ayn); أعقب الله فلانا عقبى نافعة (jamhara); عاقبة كل شيء آخره والعقبى جزاء الأمر (sihah); عاقبة كل شيء آخره واستعقب من أمره ندما (tahdhib;maqayis); العقب والعقبى يختصان بالثواب والعاقبة للمتقين (mufradat); العقبول بقية المرض واللام زائدة (maqayis-variant)","source_summary":"Kaynak ifadesi son ve sonuç anlamını iyi ya da kötü doğabilecek etkilerle verir; bunun içinde iyi karşılığa daralan bir yorum ve ağır hastalıktan sonra kalan belirti de yer alır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"آخر الشيء وخاتمته وعاقبته وعقباه، وما يورثه الفعل أو يستعقبه من خير أو شر أو ندم أو مرض","what_is_not_ar":"لا يدخل فيه العقاب بمعنى الطائر ولا العقبة الجبلية ولا العصب"},"support_links":["sup_51c3aae11b81820403fc","sup_81d06cc4fbb6b9e3d6d8"]},{"boundary":"Dal her türlü karşılığı değil, kusur veya suçtan sonra verilen kötü ve acı verici karşılığı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"suçtan sonra verilen kötü karşılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kötü davranış veya suçtan sonra fail kötü bir karşılıkla sorumlu tutulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Savaş bağlamındaki yorum, karşı tarafı cezalandırarak üstün gelip kazanç elde etmeyi anlatır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir failin önceki kötülüğü nedeniyle acı verici bir karşılıkla sorumlu tutulduğu durumları kapsar.","boundary_detail":"Dal her türlü karşılığı değil, kusur veya suçtan sonra verilen kötü ve acı verici karşılığı kapsar.","branch_image_ar":"العقوبة بعد الذنب","concept_gloss":"suçtan sonra verilen kötü karşılık","contextual_glosses":[{"applicability":"Kişinin belirli bir suça veya kötü davranışa karşılık sorumlu tutulduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Faili, önceki suçu ve ona karşılık verilen cezayı açıkça korur."},"facet_ids":["F001"],"text":"işlediği suçtan dolayı cezalandırmak","usage_role":"general"}],"definition":"Bir kişiye işlediği suç veya kötülükten sonra kötü ve acı verici bir karşılık vermek, onu sorumlu tutup cezalandırmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kötü davranış veya suçtan sonra fail kötü bir karşılıkla sorumlu tutulur."},{"facet_id":"F002","role":"specialization","statement":"Savaş bağlamındaki yorum, karşı tarafı cezalandırarak üstün gelip kazanç elde etmeyi anlatır."}],"identity_rationale":"Kaynak ifadesi, işlenen suç veya kötülükten sonra kötü bir karşılık verme, sorumlu tutma ve acı çektirme anlamında birleşir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ceza, cezalandırma"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"onları cezalandırıp üstün geldiniz ve kazanç elde ettiniz"}],"lexicalization_note":"Genel ceza biçimleri ile savaşta cezalandırma sonucunda ele geçirme yorumu ayrı bir özel kullanım olarak tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öç alma yönü taşıyan ceza dalı en yakın sınırı verir, ötekiler yargılama, caydırma, kısas veya genel karşılıktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı genel cezalandırmadır; komşu dalda cezaya kızgınlık, karşılık verme ve öç alma güdüsü eşlik eder.","focus_only":"Odak dalı, suçtan sonra verilen her türlü kötü ve acı verici cezayı kapsar.","gloss":"kötülüğe ceza ile karşılık verme","neighbor_only":"Komşu dal, kızgınlık ve öç alma yönü belirgin olan cezayı öne çıkarır.","neighbor_ref":"root_001545/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kötülükten sonra faili cezalandırmayı kapsar."}],"source_phrase_ar":"عاقبه الله عقابا ومعاقبة وعقوبة (jamhara); العقاب العقوبة وقد عاقبته بذنبه (sihah); العقاب والمعاقبة أن تجزي الرجل بما فعل سوءا (tahdhib); العقوبة والمعاقبة والعقاب يختص بالعذاب (mufradat); سميت عقوبة لأنها تكون آخرا وثاني الذنب (maqayis)","source_summary":"Kaynaklar cezayı, kişinin yaptığı kötülüğe daha sonra verilen acı verici karşılık olarak tanımlar; savaş bağlamındaki özel yorum cezalandırma yoluyla üstün gelmeye uzanır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقاب والعقوبة والمعاقبة بمعنى الجزاء بالسوء أو المؤاخذة على الذنب أو إدراك الثأر، وما فسر به فعاقبتم من الإصابة والغنيمة على وجه العقوبة","what_is_not_ar":"ليس العقبى المحمودة ولا العقاب الطائر ولا العقب الوتر"},"support_links":[]},{"boundary":"Dal sırf zaman bakımından sonra gelmeyi değil, önceki bir işin izini amaçlı biçimde sürüp yeniden ele almayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"ardından izleyip yeniden inceleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki kişi veya iş, ardından gidilip izi sürülerek yeniden ele alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İzleme; hak isteme, şüphe üzerine yeniden sorma, inceleme veya karşı çıkma amacı taşıyabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hükmün ardından onu geri çevirecek veya ona karşı çıkacak kimsenin bulunmaması ayrıca anlatılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Önceki bir işin veya haberin izini sürerek onu soru, hak talebi ya da itirazla yeniden ele almayı kapsar.","boundary_detail":"Dal sırf zaman bakımından sonra gelmeyi değil, önceki bir işin izini amaçlı biçimde sürüp yeniden ele almayı anlatır.","branch_image_ar":"التعقب والمراجعة","concept_gloss":"ardından izleyip yeniden inceleme","contextual_glosses":[{"applicability":"Şüphe duyulan bir haber veya iş hakkında yeniden soru sorulup inceleme yapıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki konuya geri dönmeyi, soru sormayı ve araştırmayı korur."},"facet_ids":["F001","F002"],"text":"yeniden dönüp araştırmak","usage_role":"contextual"}],"definition":"Bir kişi, haber, iş veya hükmün ardından giderek onu hak arama, soru sorma, inceleme, karşı çıkma ya da geri çevirme amacıyla yeniden ele almaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki kişi veya iş, ardından gidilip izi sürülerek yeniden ele alınır."},{"facet_id":"F002","role":"specialization","statement":"İzleme; hak isteme, şüphe üzerine yeniden sorma, inceleme veya karşı çıkma amacı taşıyabilir."},{"facet_id":"F003","role":"associated_use","statement":"Bir hükmün ardından onu geri çevirecek veya ona karşı çıkacak kimsenin bulunmaması ayrıca anlatılır."}],"identity_rationale":"Kaynak ifadesi bir kişiyi, işi, haberi veya hükmü sonradan izleyip hak arama, yeniden sorma, inceleme, karşı çıkma ya da geri çevirme işlemlerini destekler.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"hak istemek veya itiraz etmek için ardından izleyen kişi"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"onun hükmünü geri çevirecek veya sorgulayacak kimse yoktur"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"haberi veya işi yeniden dönüp araştırmak"}],"lexicalization_note":"İzleyen kişi adı, hükmün geri çevrilemezliğini bildiren söz ve haberi yeniden inceleme yapısı ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; haberin izini sürme dalı en yakın karşılıktır, ötekiler inkâr, kanıt, hüküm açıklama veya kapsamlı arama alanında kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki konuya geri dönme ve onu inceleme kurucudur; komşu dal genel haber edinme etkinliğidir.","focus_only":"Odak dalı, önceden verilmiş hükme karşı çıkmayı ve hak istemek için kişiyi izlemeyi de kapsar.","gloss":"haberin izini sürüp araştırma","neighbor_only":"Komşu dal, henüz öğrenilmek istenen haberi soru, dinleme veya gözlemle toplama üzerinde yoğunlaşır.","neighbor_ref":"root_000321/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir haberin izini sürmeyi ve soru yoluyla bilgi aramayı kapsar."}],"source_phrase_ar":"المعقب الذي يتتبع عقب إنسان في طلب حق (ayn); لا معقب لحكمه أي لا راد لقضائه (ayn); تعقبت الرجل إذا أخذته بذنب وتعقبت عن الخبر إذا شككت وعدت للسؤال (sihah); المعقب الذي يكر على الشيء ولا يكر أحد على ما أحكمه الله (tahdhib); لا أحد يتعقبه ويبحث عن فعله (mufradat); تعقبت ما صنع فلان أي تتبعت أثره (maqayis)","source_summary":"Kaynaklar önceki kişi, haber, iş veya hükmün izini amaçlı biçimde sürme çekirdeğinde birleşir; amaç hak isteme, yeniden sorma, inceleme, itiraz veya geri çevirme olabilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"تتبع الأمر أو الخبر أو الحكم بعده للسؤال أو الطلب أو الاعتراض أو الرد، ومنه المعقب طالب الحق ولا معقب لحكمه أي لا راد أو لا متتبع معارض","what_is_not_ar":"ليس مجرد التعاقب الزمني ولا الرجوع على العقب ولا العقوبة"},"support_links":[]},{"boundary":"Dal yalnız birinin ardından gelmeyi değil, daha önce yapılmış aynı tür etkinliğe yeniden dönmeyi gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"aynı tür işi yeniden yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Daha önce yapılmış bir işin ardından aynı tür iş yeniden gerçekleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşu ve otlama gibi etkinliklerde benzer veya karşılıklı evreler yeniden başlar."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuşun yükselip alçalması ve ayın kaybolduktan sonra yeniden görünmesi döngüsel örneklerdir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir işin tamamlanmasından sonra aynı tür etkinliğe yeniden dönülen bütün temel bağlamları kapsar.","boundary_detail":"Dal yalnız birinin ardından gelmeyi değil, daha önce yapılmış aynı tür etkinliğe yeniden dönmeyi gerektirir.","branch_image_ar":"العود مرة بعد مرة","concept_gloss":"aynı tür işi yeniden yapma","contextual_glosses":[{"applicability":"Sefer, ibadet veya koşu gibi tamamlanmış bir etkinliğin yeniden yapıldığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İlk tamamlanmayı, geri dönüşü ve aynı tür etkinliğin yinelenmesini korur."},"facet_ids":["F001","F002"],"text":"bir kez daha dönüp yapmak","usage_role":"contextual"}],"definition":"Bir işi yaptıktan sonra aynı tür işe yeniden dönmek veya benzer bir hareket evresini yinelemektir; koşu, otlama, uçuş ve aylık görünme bunun özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Daha önce yapılmış bir işin ardından aynı tür iş yeniden gerçekleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Koşu ve otlama gibi etkinliklerde benzer veya karşılıklı evreler yeniden başlar."},{"facet_id":"F003","role":"example","statement":"Kuşun yükselip alçalması ve ayın kaybolduktan sonra yeniden görünmesi döngüsel örneklerdir."}],"identity_rationale":"Kaynak ifadesi aynı tür işin bir ilk gerçekleştirmeden sonra yeniden yapılmasını ve koşu, otlama, uçuş ya da aylık dönüş gibi yinelenen devreleri destekler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"aynı tür işi yeniden yapma"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"atın bir koşudan sonra yeniden ve daha iyi koşması"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"bir otlak türünden ötekine dönüşümlü geçen deve sürüsü"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kuşun yükselişiyle alçalışı arasındaki hareket evresi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ayın kaybolduktan sonra yeniden görünmesi, aylık dönüşü"}],"lexicalization_note":"Genel yeniden yapma biçimi, koşu ve otlama yapıları ile kuş ve ayın döngüsel hareket adları ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yeniden yapma dalı en yakın sınırı verir, ötekiler dönüş, tereddüt, erken gitme veya konu dışı alanlardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında önceki etkinliğe dönüş ve yeni bir evre başlatma belirgindir; komşu dal genel yineleme sayısını öne çıkarır.","focus_only":"Odak dalı, tamamlanan işe geri dönmeyi ve koşu, otlama, uçuş gibi belirli devreleri kapsar.","gloss":"bir işi yeniden yapma","neighbor_only":"Komşu dal, aynı şeyin iki kez veya art arda yinelenmesini daha genel biçimde anlatır.","neighbor_ref":"root_000208/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir eylemin daha önceki örneğinden sonra yeniden gerçekleşmesini kapsar."}],"source_phrase_ar":"التعقيب غزوة بعد غزوة وسير بعد سير والخيل تعقب في حضرها (ayn); المعقب الذي يجيء مرة بعد أخرى وعقب الغازي إذا قفل ثم رجع (jamhara); عقب للفرس جري بعد جري والتعقيب أن يغزو الرجل ثم يثني من سنته (sihah); كل من عمل عملا ثم عاد إليه فقد عقب والتعقيب صلاة أو غيرها ثم يعود فيه (tahdhib); عقب الفرس في عدوه وعقبة الطائر صعوده وانحداره (mufradat); عقبة الإبل أن ترعى الحمض مرة والخلة أخرى (maqayis)","source_summary":"Kaynaklar bir işten sonra aynı tür işe yeniden dönmede birleşir; sefer, ibadet, koşu, otlama, uçuş ve ayın görünmesi bu yinelemenin farklı bağlamlarıdır.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"العود إلى العمل بعد عمل مثله، كغزوة بعد غزوة، وصلاة بعد صلاة، وجري بعد جري، ومرعى بعد مرعى، وطلوع بعد غياب","what_is_not_ar":"ليس التعاقب الذي هو خلافة شخص لشخص فقط ولا آخر الشيء وحده"},"support_links":[]},{"boundary":"Üç kullanım ortak bir değişim ve güvence alanında tutulabilir, fakat her birinin işlem koşulları ayrı belirtilmelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B010","candidate_links":[{"candidate_id":"cand_2919f56e6cc6eab0cc88","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"bedel, satış başvurusu ve elde tutma güvencesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi veya şeyin yerine başka bir bedel alınır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Satılan maldaki sorun nedeniyle satıcıya sonradan başvurma ve ondan karşılık isteme hakkı doğar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Satıcı malı ödeme gelene dek yanında tutarsa, malın kaybından kendisi sorumlu olur."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tek kavrama indirgenemeyen üç alışveriş kullanımını kısa ve açık biçimde birlikte gösterir.","boundary_detail":"Üç kullanım ortak bir değişim ve güvence alanında tutulabilir, fakat her birinin işlem koşulları ayrı belirtilmelidir.","branch_image_ar":"العقبة بدلا وضمانا","concept_gloss":"bedel, satış başvurusu ve elde tutma güvencesi","contextual_glosses":[{"applicability":"Satıştan sonra bir kusur veya kayıp nedeniyle sorumluluğun kime ait olduğunun belirtildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satışı, sonradan doğan başvuruyu ve malı elde tutanın sorumluluğunu korur."},"facet_ids":["F002","F003"],"text":"satılan maldan doğan başvuru ve güvence","usage_role":"contextual"}],"definition":"Değişim ve satış alanında, bir şeyin yerine alınan bedeli, satılan mal yüzünden sonradan doğan başvuru ve sorumluluğu ya da malın ödeme gelene dek satıcıda tutulup onun güvencesinde kalmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi veya şeyin yerine başka bir bedel alınır."},{"facet_id":"F002","role":"specialization","statement":"Satılan maldaki sorun nedeniyle satıcıya sonradan başvurma ve ondan karşılık isteme hakkı doğar."},{"facet_id":"F003","role":"specialization","statement":"Satıcı malı ödeme gelene dek yanında tutarsa, malın kaybından kendisi sorumlu olur."}],"identity_rationale":"Kaynak ifadesi bedel alma, satışta sonradan doğan sorumluluk ve satılan malı ödeme gelene dek elde tutma güvencesini destekler; bunlar tek işlem değil, aynı dalda toplanmış üç hukuk ve alışveriş kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"tutsağın veya bir şeyin yerine alınan bedel"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"satılan maldan doğan başvuru hakkı ve sorumluluk"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"malı ödeme gelene dek elinde tutan satıcı kayıptan sorumludur"}],"lexicalization_note":"Bedel, satıştaki sonradan doğan sorumluluk ve malı elde tutan satıcının güvencesi ayrı söz birimleri olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; satış güvencesi dalı en yakın sınırı verir, diğer adaylar yalnız bedel, kefalet, rehin, ibra veya emanet alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel satış güvencesidir; odak dalı bunun yanında ayrı bir bedel alma işlemini ve malı elinde tutan satıcıyı içerir.","focus_only":"Odak dalı, yerine alınan bedeli ve satılan malı ödeme gelene dek elde tutma sorumluluğunu da kapsar.","gloss":"satıştan doğan güvence ve başvuru","neighbor_only":"Komşu dal, alışverişte kusur çıkarsa başvurmayı güvenceye alan belge, koşul ve yükümlülüğü geniş biçimde kapsar.","neighbor_ref":"root_001055/B006","relation_type":"near_neighbor","shared_zone":"İki dal da satıştan sonra ortaya çıkabilecek kusur veya kayıp için güvence ve sorumluluk kurar."}],"source_phrase_ar":"أخذت من أسيري عقبة إذا أخذت منه بدلا (sihah); المعتقب ضامن لما اعتقب أي اعتقبت الشيء إذا حبسته عندك (tahdhib); عقب علي في تلك السلعة عقب أي أدركني فيها درك والتعقبة الدرك (maqayis); أخذت عقبة من أسيري وهو أن تأخذ منه بدلا (maqayis)","source_summary":"Kaynak ifadesi üç ayrı işlemi bir araya getirir: yerine bedel alma, satıştan doğan sonradan başvuru ve satılan malı ödeme gelene dek elde tutanın sorumluluğu.","sources":["SI","TA","MQ"],"what_is_ar":"العقبة بمعنى بدل يؤخذ مكان شيء، أو درك يلحق في السلعة، أو احتباس المبيع حتى يقبض الثمن مع ضمان المعتقب","what_is_not_ar":"ليس العقبة الجبلية ولا النوبة في الركوب ولا العقوبة العامة"},"support_links":["sup_81d06cc4fbb6b9e3d6d8"]},{"boundary":"Dal nihai hüküm veya soy anlamını değil, önceki madde, durum ya da niteliğin geride bıraktığı kalanı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"geride kalan son parça ya da iz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Önceki şey tükendikten veya değiştikten sonra ondan bir bölüm ya da iz kalır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapta kalan son yemek suyu, maddi kalıntının belirgin örneğidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Geçmiş bir nitelik veya hastalık, kişide görünür bir iz ya da belirti bırakabilir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem maddi bir artığı hem de geçmiş durumdan kişide kalan görünür belirtiyi kapsar.","boundary_detail":"Dal nihai hüküm veya soy anlamını değil, önceki madde, durum ya da niteliğin geride bıraktığı kalanı kapsar.","branch_image_ar":"بقية الشيء وأثره","concept_gloss":"geride kalan son parça ya da iz","contextual_glosses":[{"applicability":"Hastalık, görünüş veya başka bir niteliğin etkisi kişide sürmeye devam ettiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki durumu, ondan sonra kalmayı ve görünür belirtinin sürmesini korur."},"facet_ids":["F003"],"text":"önceki durumdan kalan belirti","usage_role":"contextual"}],"definition":"Bir madde, durum veya niteliğin kullanım ya da değişimden sonra geride kalan son bölümü, belirtisi veya görünür izidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Önceki şey tükendikten veya değiştikten sonra ondan bir bölüm ya da iz kalır."},{"facet_id":"F002","role":"example","statement":"Kapta kalan son yemek suyu, maddi kalıntının belirgin örneğidir."},{"facet_id":"F003","role":"extension","statement":"Geçmiş bir nitelik veya hastalık, kişide görünür bir iz ya da belirti bırakabilir."}],"identity_rationale":"Kaynak ifadesi bir şeyin kullanım veya değişim sonrasında kalan son bölümünü, kişide görülen kalıcı izi ve hastalıktan geriye kalan belirtiyi ortak kalıntı çekirdeğinde destekler.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"ağır hastalıktan kalan belirti"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"kapta kalan son yemek suyu"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"soyluluk ve güzellikten kişide kalan görünür iz"}],"lexicalization_note":"Hastalık kalıntısı biçimi, kapta kalan son bölüm ve kişide kalan görünür nitelik ayrı söz birimleri olarak korunur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geçmiş şeyi gösteren kalıcı iz dalı en yakın karşılıktır, ötekiler az miktar, özel madde izi veya bozulma durumudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kalan son bölüm veya belirti yeterlidir; komşu dalda iz, geçmiş varlığı ya da olayı gösteren bir işarettir.","focus_only":"Odak dalı, kapta kalan maddi son bölümü ve hastalıktan kalan belirtiyi de kapsar.","gloss":"önceki şeyden kalan iz","neighbor_only":"Komşu dal, geçmişte var olmuş bir şeyi gösteren işaret ve kalıntının kanıt değerini öne çıkarır.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"İki dal da geçmiş bir madde veya durumdan geriye kalan izi kapsar."}],"source_phrase_ar":"العقبة شيء من المرق يرده مستعير القدر (sihah); عليه عقبه السرو والجمال أي أثر ذلك وهيئته (sihah); العقبة الشيء من المرق يرده مستعير القدر (tahdhib); عقبة القدر آخر ما في القدر أو يبقى بعد أن يغرف منها (maqayis); العقبول بقية المرض (maqayis-variant)","source_summary":"Kaynaklar kapta kalan son yemek suyu ile kişide süren görünüş veya hastalık belirtisini, önceki şeyden geriye kalan bölüm ya da iz olarak birleştirir.","sources":["SI","TA","MQ"],"what_is_ar":"ما يبقى في آخر الشيء أو يرد بعد استعماله أو يظهر أثره وهيئته، كعقبة القدر وبقية السرو والجمال وبقية المرض","what_is_not_ar":"ليس العاقبة الحكمية وحدها ولا الولد الباقي ولا العقبة الطريق"},"support_links":[]},{"boundary":"Dal dağ yolunun sarp yükselişini ve kayalık çıkıntıyı kapsar; binme sırası veya ceza anlamına geçmez.","branch_kind":"bare","branch_ref":"root_001033/B012","candidate_links":[{"candidate_id":"cand_74ca34cd4d71b4ba40cf","lane":"micro"},{"candidate_id":"cand_185b710aa73a655c0c92","lane":"micro"},{"candidate_id":"cand_e16caf2a6d6cae89049f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"sarp dağ geçidi ve kayalık çıkıntı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dağdaki yol yukarı yönelir, sarptır ve geçilmesi belirgin güçlük taşır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu veya dağ yüzündeki dışarı taşan sert kaya, basamak ya da çıkıntı aynı alana bağlıdır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükselen zorlu yolu ve aynı alandaki dışarı taşan kaya anlamını birlikte temsil eder.","boundary_detail":"Dal dağ yolunun sarp yükselişini ve kayalık çıkıntıyı kapsar; binme sırası veya ceza anlamına geçmez.","branch_image_ar":"العقبة الصعبة والناشز","concept_gloss":"sarp dağ geçidi ve kayalık çıkıntı","contextual_glosses":[{"applicability":"Dağda yukarı çıkan, engebeli ve geçilmesi güç yol veya geçit için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yukarı yönü, dağ ortamını, sarplığı ve geçiş güçlüğünü korur."},"facet_ids":["F001"],"text":"dik ve zorlu dağ yolu","usage_role":"general"}],"definition":"Dağda yükselen sarp, engebeli ve geçilmesi güç yol veya geçittir; ayrıca kuyu içinde ya da dağ yüzünde dışarı taşan sert kaya ve basamak benzeri çıkıntıyı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dağdaki yol yukarı yönelir, sarptır ve geçilmesi belirgin güçlük taşır."},{"facet_id":"F002","role":"extension","statement":"Kuyu veya dağ yüzündeki dışarı taşan sert kaya, basamak ya da çıkıntı aynı alana bağlıdır."}],"identity_rationale":"Kaynak ifadesi dağdaki dik, sarp ve zorlu yolu temel anlam olarak verir; kuyu veya dağ yüzündeki dışarı taşan kaya ve yükseltiyi aynı sertlik ve yükselme alanında ayrıca destekler.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"dik ve zorlu dağ yolu veya geçidi"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"kuyu ya da dağ yüzündeki dışarı taşan kaya"}],"lexicalization_note":"Tanım yalnız kanıtlanan yalın coğrafi anlamları kapsar ve başka yapılardaki sıra ya da ceza anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sarp geçit dalı en yakın karşılıktır, ötekiler iniş, taşlı arazi, uzunluk, yükselti veya yol kıvrımı gibi yan sınırlar sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal zorluk niteliğine daha dardır; odak dalı coğrafi yolu ve ayrıca çıkıntılı kaya anlamını taşır.","focus_only":"Odak dalı, sarp dağ yolunun yanında kuyu veya dağ yüzündeki kaya çıkıntısını da kapsar.","gloss":"çıkılması güç sarp geçit","neighbor_only":"Komşu dal, özellikle çıkılması çok güç olan tepe ve dik geçit niteliğine daralır.","neighbor_ref":"root_001051/B005","relation_type":"near_synonym","shared_zone":"İki dal da dik, sarp ve çıkılması zor bir dağ geçidini kapsar."}],"source_phrase_ar":"العقبة المصعد في الجبل والجمع عقاب (jamhara); العقبة واحدة عقاب الجبال والعقاب حجر ناتئ في جوف بئر (sihah); العقبة الجبل الطويل يعرض للطريق وهو صعب شديد (tahdhib); العقبة طريق وعر في الجبل (mufradat); الأصل الآخر يدل على ارتفاع وشدة وصعوبة والعقبة طريق في الجبل (maqayis)","source_summary":"Kaynaklar dağdaki sarp ve zorlu yükselen yolda birleşir; ayrıca kuyu içindeki veya dağ yüzündeki çıkıntılı kaya ve basamak benzeri yükseltiyi verir.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقبة طريق وعر صاعد في الجبل، وما شابهها من مرقى أو صخرة أو حجر ناشز في البئر أو عرض الجبل أو بناء الطي","what_is_not_ar":"ليس النوبة في الركوب ولا العقوبة ولا العقاب الطائر"},"support_links":["sup_44e0be4d69ef9ea83f12","sup_51c3aae11b81820403fc","sup_70b5a391671fcb47d1e4"]},{"boundary":"Kuş çekirdektir; sancak benzetme yoluyla bağlıdır, korkunç bela ise özel bir türevdir ve ceza anlamıyla karıştırılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001033/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"kartal ve ona benzetilen büyük sancak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim güçlü ve büyük yırtıcı kuştur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Büyük sancak, görünüşü yırtıcı kuşa benzetildiği için aynı adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Büyütme ve korkutma etkisi taşıyan özel türev, ağır ve korkunç belayı belirtir."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş çekirdeğini ve biçim benzerliğiyle oluşan sancak uzantısını birlikte temsil eder.","boundary_detail":"Kuş çekirdektir; sancak benzetme yoluyla bağlıdır, korkunç bela ise özel bir türevdir ve ceza anlamıyla karıştırılmaz.","branch_image_ar":"العقاب الجارح والراية","concept_gloss":"kartal ve ona benzetilen büyük sancak","contextual_glosses":[{"applicability":"Kuşun kendisi değil, ona görünüş bakımından benzetilmiş bayrak veya büyük sancak anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sancağı, büyüklüğünü ve kartalla kurulan görünüş benzetmesini korur."},"facet_ids":["F002"],"text":"kartala benzetilen büyük sancak","usage_role":"explanatory"}],"definition":"Gücüyle tanınan büyük bir yırtıcı kuştur; biçim benzerliği nedeniyle büyük sancak veya bayrak da onun adıyla anılır, özel bir büyütülmüş biçim ise korkunç belayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim güçlü ve büyük yırtıcı kuştur."},{"facet_id":"F002","role":"extension","statement":"Büyük sancak, görünüşü yırtıcı kuşa benzetildiği için aynı adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Büyütme ve korkutma etkisi taşıyan özel türev, ağır ve korkunç belayı belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Önceki suça verilen kötü karşılık anlamını ekler.","collision":"Aynı kökün cezalandırma dalıyla doğrudan karışır.","fit":"displacement","loses":"Yırtıcı kuşu, güç niteliğini ve sancak benzetmesini bütünüyle yitirir.","preserves":"Aynı ses dizisine bağlı başka bir sözlük alanıyla yalnız biçimsel yakınlık taşır."},"text":"ceza"}],"identity_rationale":"Kaynak ifadesi güçlü yırtıcı kuşu temel alır, büyük sancağın biçim benzerliğiyle ondan adlandırılmasını açıklar ve büyütülmüş türevde korkunç bela anlamını ayrıca verir.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"kartal, güçlü yırtıcı kuş"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"kartala benzetilen büyük sancak veya bayrak"},{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"korkunç ve ağır bela"}],"lexicalization_note":"Yalın kuş adı, kuşa benzetilen sancak ve korkunç belayı anlatan türemiş biçim birbirinden ayrılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikili sancak dalı uzantı için en yararlı karşılaştırmadır, ötekiler yalnız güç, renk, öncülük veya görünüş alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalındaki sancak kuş benzetmesine dayanan bir uzantıdır; komşu dalda bayrak doğrudan temel gönderimdir.","focus_only":"Odak dalı yırtıcı kuşu temel alır ve sancağı yalnız kuşa benzetilmesi yoluyla kapsar.","gloss":"görünür büyük sancak","neighbor_only":"Komşu dal, görünür olmak üzere dikilmiş bayrak veya işareti benzetme gerektirmeden anlatır.","neighbor_ref":"root_000531/B011","relation_type":"near_neighbor","shared_zone":"İki dal da uzaktan görülebilen büyük bayrak veya sancağı kapsar."}],"source_phrase_ar":"العقاب الطائر المعروف وسميت الراية عقابا (jamhara); العقاب طائر والعقاب عقاب الراية (sihah); العقاب هذا الطائر والعقاب العلم الضخم واللواء (tahdhib); العقاب سمي لتعاقب جريه في الصيد وبه شبه في الهيئة الراية (mufradat); العقاب من الطير سميت لشددتها وقوتها ثم شبهت الراية بها (maqayis); العقنباة الداهية من العقبان وأصلها عقاب (maqayis-variant)","source_summary":"Kaynaklar güçlü yırtıcı kuşta ve biçimce ona benzetilen büyük sancakta birleşir; ayrıca tek kaynaklı biçim çeşidi korkunç bela anlamını taşır.","sources":["JA","SI","TA","MU","MQ"],"what_is_ar":"العقاب الطائر الجارح المعروف، وما شبه به من الراية أو اللواء أو الناقة السوداء، والعقنباة الداهية من العقبان","what_is_not_ar":"ليس العقاب بمعنى العقوبة ولا العقبة الطريق ولا العقب الوتر"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001033/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"source_variant","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım, ortak kavramsal bağ gösterilmeden erkek kişi adı olarak verilmiştir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hayvan merkezli kullanımın temel gönderimi erkek kekliktir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Atlar görünüş veya hareket benzerliği yoluyla erkek kekliğe benzetilerek adlandırılır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"يعقوب واليعقوب","concept_gloss":"özel adlandırma kümesi","contextual_glosses":[{"applicability":"Kişi adından bağımsız olan hayvan merkezli kullanım ve onun benzetme uzantısı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek keklik çekirdeğini ve atlara aktarılan benzetme ilişkisini korur."},"facet_ids":["F002","F003"],"text":"erkek keklik; ona benzetilen at","usage_role":"explanatory"}],"definition":"Bu dal tek bir üretken kök anlamına indirgenmez: bir yanda erkek kişi adı, öte yanda erkek keklik ve ona benzetilerek adlandırılan at aynı sınırlı adlandırma kümesi içinde tutulur.","distinctive_facets":[{"facet_id":"F001","role":"source_variant","statement":"Bir kullanım, ortak kavramsal bağ gösterilmeden erkek kişi adı olarak verilmiştir."},{"facet_id":"F002","role":"core","statement":"Hayvan merkezli kullanımın temel gönderimi erkek kekliktir."},{"facet_id":"F003","role":"extension","statement":"Atlar görünüş veya hareket benzerliği yoluyla erkek kekliğe benzetilerek adlandırılır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"erkek kişi adı"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"erkek keklik ve ona benzetilen at"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"يعقوب اسم رجل واليعقوب ذكر الحجل (sihah); يعقوب متعلق بعقب عيصو واليعقوب ذكر الحجل وتسمى الخيل يعاقيب (tahdhib); اليعقوب ذكر الحجل لما له من عقب الجري (mufradat)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["SI","TA","MU"],"what_is_ar":"يعقوب اسم رجل في الاستعمال العربي والقرآني، واليعقوب ذكر الحجل وما شبه به من الخيل، مع تعليل بعض المصادر بالتعلق بالعقب أو عقب الجري","what_is_not_ar":"ليس كل عاقب أو معقب ولا العقاب الطائر الجارح"},"support_links":[]},{"boundary":"Dal yalnız bitkiyle kurulan yapıda, sararma ve kurumaya yaklaşma evresini anlatır; genel son veya sonuç anlamına genişlemez.","branch_kind":"collocation","branch_ref":"root_001033/B015","candidate_links":[{"candidate_id":"cand_185b710aa73a655c0c92","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","surface_ar":"عَقَبَةَ"}],"gloss":"bitkinin sararıp kurumaya yaklaşması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bitkinin sapı incelirken yaprağı veya meyvesi sararır ve kuruma evresi yaklaşır."}}],"root_ar":"ع ق ب","root_id":"root_001033","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sapın incelmesiyle yaprak veya meyvenin sarardığı ve kurumanın yaklaştığı bitki evresini karşılar.","boundary_detail":"Dal yalnız bitkiyle kurulan yapıda, sararma ve kurumaya yaklaşma evresini anlatır; genel son veya sonuç anlamına genişlemez.","branch_image_ar":"اصفرار النبت ويبس العود","concept_gloss":"bitkinin sararıp kurumaya yaklaşması","contextual_glosses":[{"applicability":"Bitki veya çalının olgunluk sonrasında kurumadan hemen önceki görünüşü için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sararmayı, kurumanın henüz tamamlanmamasını ve ona yaklaşmayı korur."},"facet_ids":["F001"],"text":"sararıp kurumaya yüz tutmak","usage_role":"contextual"}],"definition":"Bir bitkinin sapının incelip sertleşmesi, yaprak veya meyvesinin sararması ve kurumaya çok yaklaşmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bitkinin sapı incelirken yaprağı veya meyvesi sararır ve kuruma evresi yaklaşır."}],"identity_rationale":"Kaynak ifadesi bitkinin sapının incelmesini, yaprak veya meyvesinin sararmasını ve bunun hemen ardından kuruma evresine yaklaşmasını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"bitkinin sapı incelip yaprağı veya meyvesi sararmak ve kurumaya yaklaşmak"}],"lexicalization_note":"Tanım yalnız bitki veya belirli çalı adıyla kurulan yapıya bağlıdır; yalın kök için genel kuruma anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bitki sararması ve kuruması dalı en yakın sınırı verir, ötekiler belirli kuru bitkiler veya farklı olgunlaşma evreleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı kurumadan hemen önceki belirli evreye ve sap incelmesine bağlıdır; komşu dal genel sararma ve kuruluğu içerir.","focus_only":"Odak dalı, sapın incelmesi ve yaprak veya meyvenin sararmasından sonra kurumanın yaklaşmasını belirli yapıda anlatır.","gloss":"bitkinin sararıp kuruması","neighbor_only":"Komşu dal, çeşitli bitki ve arazide genel sararma, kuruma ve kurutma durumlarını daha geniş kapsar.","neighbor_ref":"root_001612/B001","relation_type":"near_synonym","shared_zone":"İki dal da bitkinin yeşilliğini yitirip sararmasını ve kuruma yönünde değişmesini kapsar."}],"source_phrase_ar":"عقب العرفج إذا اصفرت ثمرته وحان يبسه (sihah); عقب النبت إذا دق عوده واصفر ورقه (tahdhib); عقب العرفج يعقب وعقبه أن يدق عوده وتصفر ثمرته ثم ليس بعد ذلك إلا يبسه (maqayis)","source_summary":"Kaynaklar bitki veya belirli çalının sapının incelmesi, yaprak ya da meyvesinin sararması ve bundan sonra kurumanın yaklaşması üzerinde birleşir.","sources":["SI","TA","MQ"],"what_is_ar":"عقب النبت أو العرفج إذا دق عوده واصفر ورقه أو ثمره وحان يبسه، بوصفه انتقالا إلى شدة ويبوسة","what_is_not_ar":"ليس العاقبة العامة ولا عقبة الطريق ولا العقوبة"},"support_links":["sup_44e0be4d69ef9ea83f12"]},{"boundary":"Bu dal, tehlikeli giriş eylemini anlatır; tehlikenin, yol güçlüğünün veya kötü sonucun adı olan kullanımları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001202/B001","candidate_links":[{"candidate_id":"cand_74ca34cd4d71b4ba40cf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"düşünmeden tehlikeye atılma veya sokma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, sonucunu ölçmeden veya yolu bilmeden güç ya da korkutucu bir şeyin içine atılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Giriş, yüksekten aşağı düşme, bir nehre ya da çukura atılma gibi yön ve ortam bakımından somutlaşabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"At, binicisini yüzüstü düşürebilir veya onu korkulan bir yere kadar götürebilir; burada girişin etkisini binici taşır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Erkek deve, kendisine izin verilmesini beklemeden dişi deve sürüsünün içine kendiliğinden girebilir."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem kişinin korkutucu bir şeye kendini atmasını hem de belirli yapılarda başka bir katılımcının oraya sürüklenmesini kapsayan en kısa tam karşılıktır.","boundary_detail":"Bu dal, tehlikeli giriş eylemini anlatır; tehlikenin, yol güçlüğünün veya kötü sonucun adı olan kullanımları kapsamaz.","branch_image_ar":"اقتحام الشدة بلا روية","concept_gloss":"düşünmeden tehlikeye atılma veya sokma","contextual_glosses":[{"applicability":"Kişinin güç, korkutucu veya yönü belirsiz bir işe ya da yere düşünmeden girdiği bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka bir katılımcıyı tehlikeye sokan ettirgen yapıları ve hayvanlara özgü gerçekleşmeleri kapsamaz.","preserves":"Düşünmeden yapılan atılgan girişi ve bunun taşıdığı tehlike duygusunu korur."},"facet_ids":["F001","F002"],"text":"gözü kapalı dalmak","usage_role":"contextual"},{"applicability":"Atın biniciyi korkulan yere götürmesi veya düşürmesi gibi, tehlikeli hareketin etkisini başka katılımcının taşıdığı bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin kendi başına ve düşünmeden içeri atılması anlamını dışarıda bırakır.","preserves":"Başka bir katılımcının istemsiz biçimde tehlikeli duruma sokulmasını korur."},"facet_ids":["F003"],"text":"tehlikeye sürüklemek","usage_role":"contextual"}],"definition":"Korkutucu, güç veya yönü belirsiz bir şeye yeterli deneyim, yol bilgisi ya da düşünme olmadan kendini atarak girmek; bazı yapılarda başka bir katılımcıyı böyle bir girişe zorlamak, taşımak veya düşürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, sonucunu ölçmeden veya yolu bilmeden güç ya da korkutucu bir şeyin içine atılır."},{"facet_id":"F002","role":"specialization","statement":"Giriş, yüksekten aşağı düşme, bir nehre ya da çukura atılma gibi yön ve ortam bakımından somutlaşabilir."},{"facet_id":"F003","role":"specialization","statement":"At, binicisini yüzüstü düşürebilir veya onu korkulan bir yere kadar götürebilir; burada girişin etkisini binici taşır."},{"facet_id":"F004","role":"specialization","statement":"Erkek deve, kendisine izin verilmesini beklemeden dişi deve sürüsünün içine kendiliğinden girebilir."}],"identity_rationale":"Dalın çerçevesi, korkutucu veya güç bir şeye deneyimsizce ve düşünmeden girme ya da bir katılımcıyı böyle bir duruma sokma ortak çekirdeğini doğru yansıtır. Atın biniciyi atması ve erkek devenin sürüye kendiliğinden girmesi bu çekirdeğin katılımcıları belirli özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir işe deneyimsizce ve düşünmeden atılmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"korkutucu bir güçlüğün ortasına dalma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüksekten aşağı düşmek veya yolunu bilmeden bir şeye girmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"atın binicisini yüzüstü atması ya da tehlikeye götürmesi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kendini düşünmeden bir şeye sokmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dişi deve sürüsüne salınmadan kendiliğinden giren erkek deve"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bir işe atılanlar veya dişi deve sürüsüne kendiliğinden giren develer"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"sıraya girmek"}],"lexicalization_note":"Tanım, genel giriş ve atılma çekirdeğiyle belirli yapılara bağlı ettirgen ve hayvanlara özgü kullanımları ayırır; özel yapılar bütün dala genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eylem ile tehlikeli nesne ayrımını ve ölümcül gözü karalıkla olan kapsam farkını en açık gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta hareket ve katılımcının düşüncesiz girişi kurucudur; komşuda ise hareketten bağımsız olarak tehlikeli yer, büyük güçlük veya kötü sonuç kurucudur.","focus_only":"Odak dal, güç veya tehlikeli şeye düşünmeden girme ya da birini sokma eylemini bildirir.","gloss":"tehlikeye atılma ile tehlikeli engel","neighbor_only":"Komşu dal, eylemi değil, karşılaşılan tehlikeleri, yol güçlüklerini ve istenmeyen sonuçları adlandırır.","neighbor_ref":"root_001202/B002","relation_type":"near_neighbor","shared_zone":"İki dal da güçlük ve zarar ihtimali bulunan bir durumun içine girme senaryosunda buluşur."},{"boundary_match":"partial","distinction":"Odak için düşüncesizlik veya yol bilgisinin yokluğu yeterlidir; komşu ise ölümcül tehlikenin kişiyi kuşatmasını ve ölüm kaygısının önemsenmemesini gerektirir.","focus_only":"Odak, ölüm ihtimali gerektirmeden yönsüz, deneyimsiz veya düşüncesiz her güç girişini kapsayabilir.","gloss":"düşünmeden dalma ile ölümü göze alma","neighbor_only":"Komşu, kişinin ölümden çekinmeden kendini özellikle yıkıcı tehlikelere ve savaşa atmasını öne çıkarır.","neighbor_ref":"root_001105/B006","relation_type":"near_synonym","shared_zone":"Her ikisinde de kişi kendini ağır ve tehlikeli bir durumun içine atar."}],"source_phrase_ar":"قحم في الأمور قحوما رمى بنفسه فيها من غير دربة (maqayis)؛ رميه بنفسه في نهر أو وهدة أو في أمر من غير روية (ayn)؛ انقحم الرجل انقحاما واقتحم اقتحاما إذا هوى من علو إلى سفل أو دخل في شيء من غير هداية (jamhara)؛ قحم في الأمر قحوما رمى بنفسه فيه من غير روية (sihah)؛ الاقتحام توسط شدة مخيفة (mufradat)؛ قحم فلان نفسه في كذا من غير روية (mufradat)؛ قحم الفرس فارسه (maqayis;ayn;sihah;mufradat)؛ المقحام الفحل الذي يقتحم الشول من غير إرسال فيها (maqayis;ayn;sihah)","source_summary":"Ortak anlatım, düşünmeden veya yolunu bilmeden güç bir ortama girmeyi temel alır; ettirgen kullanımlarda bu tehlikeli hareketin yükünü başka bir katılımcı taşır.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"دخول الشيء المخيف أو الشديد أو الإقدام عليه بلا روية؛ إقحام النفس أو غيرها فيه؛ اقتحام الفحل الشول بلا إرسال","what_is_not_ar":"ليس قُحَم الطريق والمهالك اسما للمواضع؛ وليس كبر الشيخ؛ وليس سن البعير"},"support_links":["sup_70b5a391671fcb47d1e4"]},{"boundary":"Burada adlandırılan şey giriş eylemi değil, o girişte karşılaşılan tehlike, güçlük veya kötü sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_001202/B002","candidate_links":[{"candidate_id":"cand_4addf1548a483e1bc40d","lane":"micro"},{"candidate_id":"cand_2919f56e6cc6eab0cc88","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"tehlikeli engel, büyük güçlük veya kötü sonuç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan şey, insanı yıkıma götürebilen veya herkesin göze alamayacağı kadar büyük olan tehlikeli güçlüktür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol bağlamında, ilerlemeyi zorlaştıran ve aşılması güç olan kesimler ya da engeller kastedilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çekişmenin kişiyi istemediği ve zarar verici sonuçlara sürükleyen tehlikeli sonuçları bu adla anılır."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıkıma götüren tehlikeyi, herkesin üstlenemediği güçlüğü, yol engellerini ve çekişmenin istenmeyen sonuçlarını birlikte karşılar.","boundary_detail":"Burada adlandırılan şey giriş eylemi değil, o girişte karşılaşılan tehlike, güçlük veya kötü sonuçtur.","branch_image_ar":"قُحَم المهالك ومصاعب الطريق","concept_gloss":"tehlikeli engel, büyük güçlük veya kötü sonuç","contextual_glosses":[{"applicability":"Yol üzerindeki somut güçlüklerin veya tehlikeli geçişlerin anlatıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel yıkım tehlikesini ve çekişmenin istenmeyen sonuçlarını kapsam dışında bırakır.","preserves":"Yolun ilerlemeyi zorlaştıran ve tehlike doğuran kesimlerini açıkça korur."},"facet_ids":["F002"],"text":"yolun aşılması güç kesimleri","usage_role":"contextual"},{"applicability":"Bir çekişmenin kişiyi istemediği veya zarar göreceği bir sonuca götürmesinden söz edilen bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yol güçlüklerini ve bağlamdan bağımsız tehlikeli büyük işi dışarıda bırakır.","preserves":"Çekişme ile onun zarar verici ve istenmeyen sonuçları arasındaki bağı korur."},"facet_ids":["F003"],"text":"çekişmenin ağır sonuçları","usage_role":"contextual"}],"definition":"İnsanı yıkıma götürebilecek tehlike, herkesin üstlenemeyeceği büyük güçlük veya yolun aşılması zor kesimidir; çekişme bağlamında kişiyi istemediği sonuca sürükleyen sonuçları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan şey, insanı yıkıma götürebilen veya herkesin göze alamayacağı kadar büyük olan tehlikeli güçlüktür."},{"facet_id":"F002","role":"specialization","statement":"Yol bağlamında, ilerlemeyi zorlaştıran ve aşılması güç olan kesimler ya da engeller kastedilir."},{"facet_id":"F003","role":"associated_use","statement":"Çekişmenin kişiyi istemediği ve zarar verici sonuçlara sürükleyen tehlikeli sonuçları bu adla anılır."}],"identity_rationale":"Dalın çerçevesi, yolun aşılması güç kesimlerini, herkesin göze alamayacağı büyük ve tehlikeli işi, yıkıma götüren durumları ve çekişmenin istenmeyen sonuçlarını tek bir adlandırma alanında doğru toplar.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yolun güç ve tehlikeli kesimleri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yıkıma götüren tehlike veya herkesin göze alamayacağı büyük iş"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"insanın başına gelen yıkıcı tehlikeler ve ağır belalar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çekişmenin kişiyi istemediği yere sürükleyen ağır sonuçları"}],"lexicalization_note":"Tanım, tehlike ve büyük güçlüğü adlandıran biçimleri temel alır; yol ve çekişme yapılarındaki özel kapsamlar ayrı tutulur.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı; eylem ile tehlike ayrımını ve yol güçlüğünün iki yakın fakat farklı türünü açıklayan üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, senaryodaki engel veya tehlikeli sonucu gösterir; komşu ise katılımcının o senaryoya nasıl girdiğini gösterir.","focus_only":"Odak dal, karşılaşılan tehlikeyi, yol güçlüğünü veya kötü sonucu bir varlık ya da durum olarak adlandırır.","gloss":"tehlikeli engel ile tehlikeye atılma","neighbor_only":"Komşu dal, kişinin düşünmeden tehlikeye girmesi veya başka bir katılımcıyı oraya sokması eylemidir.","neighbor_ref":"root_001202/B001","relation_type":"near_neighbor","shared_zone":"İki dal, ağır bir güçlükle yüzleşme ve zarar ihtimali taşıyan ortak bir senaryoya bağlıdır."},{"boundary_match":"partial","distinction":"Odak için büyük ve aşılması güç tehlike yeterlidir; komşu ise özellikle tökezleme, çukur veya tuzak niteliğindeki tehlikeyi öne çıkarır.","focus_only":"Odak, herkesin göze alamayacağı büyük işi ve çekişmenin kötü sonuçlarını da kapsar.","gloss":"yıkıcı güçlük ile tökezleten tehlike","neighbor_only":"Komşu, tökezleme yeri, çukur veya birini düşürmek için kurulmuş düzen gibi belirli somut ya da kasıtlı tehlikeleri kapsar.","neighbor_ref":"root_000982/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de insanı zarara veya yıkıma götürebilecek tehlikeli yer ve durumları adlandırabilir."},{"boundary_match":"partial","distinction":"Odak tehlike ve kötü sonuç kapsamına açılırken komşu, yukarı çıkma ve sarp geçit imgesini kurucu sınır olarak korur.","focus_only":"Odak, yıkım tehlikesini ve çekişmenin istenmeyen sonuçlarını içerebilir.","gloss":"tehlikeli güçlük ile sarp geçit","neighbor_only":"Komşu, dik çıkış, sarp geçit ve kişiye ağır gelen sıkıntı veya azap ekseninde kuruludur.","neighbor_ref":"root_000862/B003","relation_type":"near_synonym","shared_zone":"İki dal da ilerlemeyi zorlaştıran ağır yol kesimini ve bunun doğurduğu güçlüğü karşılayabilir."}],"source_phrase_ar":"قحم الطريق مصاعبه (maqayis;sihah)؛ القحمة الأمر العظيم لا يركبها كل أحد (ayn)؛ سميت المهالك قحما (jamhara)؛ القحمة المهلكة (sihah)؛ للخصومة قحم (maqayis;ayn;jamhara;sihah)","source_summary":"Ortak çekirdek, karşılaşılması veya üstlenilmesi ağır olan tehlike ve güçlüktür; yolun zorlu kesimleri ile çekişmenin kötü sonuçları bunun bağlama bağlı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI"],"what_is_ar":"المهلكة؛ الأمر العظيم الذي لا يركبه كل أحد؛ مصاعب الطريق؛ عواقب الخصومة المكروهة","what_is_not_ar":"ليس فعل الاقتحام نفسه؛ وليس سنة الجدب؛ وليس الشيخ القحم ولا البعير المقحم"},"support_links":["sup_81d06cc4fbb6b9e3d6d8","sup_e117d9ededbe9a855043"]},{"boundary":"Bu dal genel güçlüğü veya her kuraklığı değil, göçebeleri yerleşik bölgelere gitmeye zorlayan çetin kuraklık yılını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001202/B003","candidate_links":[{"candidate_id":"cand_185b710aa73a655c0c92","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"göçebeleri yerleşik bölgelere süren kuraklık yılı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz konusu zaman dilimi, yağış ve geçim kaynaklarının yetersizliğiyle belirlenen çetin ve kurak bir yıldır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yılın kuraklığı, çölde yaşayan göçebeleri yurtlarından çıkarıp kırsal veya yerleşik bölgelere inmeye zorlar."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kurak yılın hem geçim sıkıntısını hem de çölde yaşayan toplulukları yerleşik çevrelere yönelten zorlayıcı sonucunu korur.","boundary_detail":"Bu dal genel güçlüğü veya her kuraklığı değil, göçebeleri yerleşik bölgelere gitmeye zorlayan çetin kuraklık yılını anlatır.","branch_image_ar":"القَحْمة سنة الجدب","concept_gloss":"göçebeleri yerleşik bölgelere süren kuraklık yılı","contextual_glosses":[{"applicability":"Kuraklığın yol açtığı geçim sıkıntısı nedeniyle topluluğun yer değiştirmesinin öne çıktığı anlatımlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etkilenenlerin özellikle çölde yaşayan göçebeler ve varışın kırsal ya da yerleşik çevre olması ayrıntılarını siler.","preserves":"Çetin yıl ile onun zorunlu göç doğuran geçim baskısını korur."},"facet_ids":["F001","F002"],"text":"göçe zorlayan kıtlık yılı","usage_role":"contextual"}],"definition":"Çölde yaşayan göçebe toplulukları kıtlıkla karşı karşıya bırakıp geçim için kırsal veya yerleşik bölgelere gitmeye zorlayan çetin ve kurak yıldır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz konusu zaman dilimi, yağış ve geçim kaynaklarının yetersizliğiyle belirlenen çetin ve kurak bir yıldır."},{"facet_id":"F002","role":"core","statement":"Yılın kuraklığı, çölde yaşayan göçebeleri yurtlarından çıkarıp kırsal veya yerleşik bölgelere inmeye zorlar."}],"identity_rationale":"Dalın çerçevesi, belirli bir şiddet türünü eksiksiz verir: kurak ve çetin yıl, çölde yaşayan göçebe toplulukları geçim baskısıyla kırsal ya da yerleşik bölgelere indirir. Göç sonucu, sıradan bir örnek değil, anlatılan yılın ayırt edici etkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"göçebeleri yerleşik bölgelere süren çetin kuraklık yılı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"çöl göçebelerini kıtlıkla vurup yerleşik bölgelere süren yıl"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kurak yıl göçebeleri çölden yerleşik bölgeye indirdi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çölde yaşayanlar kuraklığa uğrayıp kırsal bölgeye girdiler"}],"lexicalization_note":"Tanım, yılı adlandıran biçimle yılın göçebeleri yerleşik bölgelere sürmesini anlatan yapılara bağlı etkisini ayrı fakat bağlantılı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kurak yıl çekirdeğini paylaşırken göç, yıpratma ve yaygın açlık sonuçlarında ayrılan üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta kuraklığın belirli topluluğu yerleşik çevreye itmesi anlamın parçasıdır; komşuda zamanın çetinliği veya yılın kuraklığı tek başına yeterlidir.","focus_only":"Odak, kurak yılın çölde yaşayan göçebeleri yerleşik bölgelere sürmesi sonucunu zorunlu kılar.","gloss":"göçe zorlayan kurak yıl ile çetin dönem","neighbor_only":"Komşu, kurak yılı aşarak genel olarak çetin bir dönemi de anlatabilir ve göç sonucu gerektirmez.","neighbor_ref":"root_001313/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da kurak ve ağır bir yılı adlandırabilir."},{"boundary_match":"partial","distinction":"Odak yer değiştirme sonucuyla, komşu ise insanlar ve mal üzerindeki kırıcı yıpratmayla sınırlandırılır.","focus_only":"Odak, göçebe topluluğun çölden kırsal veya yerleşik bölgeye gitmesini belirleyici sonuç sayar.","gloss":"göçe zorlayan yıl ile kırıp geçiren yıl","neighbor_only":"Komşu, çetin ve kurak yılın insanlar ile malları kırıp yıpratmasını öne çıkarır.","neighbor_ref":"root_000337/B003","relation_type":"near_synonym","shared_zone":"İki dal da insanları ağır biçimde etkileyen çetin ve kurak yılı gösterir."},{"boundary_match":"partial","distinction":"Odakta kurak yıl, etkilenen göçebe topluluk ve yerleşik bölgeye gidiş birlikte gereklidir; komşuda yaygın açlık tek başına belirleyicidir.","focus_only":"Odak, kuraklığın çölde yaşayan göçebeleri belirli bir yöne göçe zorlamasını içerir.","gloss":"kuraklık göçü ile genel kıtlık zamanı","neighbor_only":"Komşu, nedeni ve yer değiştirme sonucu belirtilmeden açlığın topluma yayıldığı herhangi bir zamanı kapsar.","neighbor_ref":"root_000278/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da yiyecek ve geçim yetersizliğinin belirlediği ağır bir zaman söz konusudur."}],"source_phrase_ar":"القحمة السنة تقحم الأعراب بلاد الريف (maqayis)؛ وقحمة الأعراب سنة جدبة تتقحم عليهم أو تقحم الأعراب بلاد الريف (ayn)؛ أقحمت السنة الأعراب إذا حطتهم من البدو إلى الحضر (jamhara)؛ السنة المقحمة المجدبة (jamhara)؛ القحمة السنة الشديدة (sihah)","source_summary":"Ortak anlatım, kurak ve ağır bir yılı bu yılın göçebe topluluklar üzerindeki yer değiştirme etkisiyle birlikte tanımlar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"السنة الشديدة أو المجدبة التي تصيب الأعراب بالقحط فتدخلهم بلاد الريف أو الحضر","what_is_not_ar":"ليست مطلق الشدة المخيفة؛ وليست مصاعب الطريق؛ وليست هرما"},"support_links":["sup_44e0be4d69ef9ea83f12"]},{"boundary":"İleri yaş temel anlamdır; bunama zorunlu bir özellik değil, yaşlı erkeği niteleyen daha dar bir kullanımdır.","branch_kind":"collocation","branch_ref":"root_001202/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"ileri yaşlı, kimi kullanımda bunamış kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan, yaşamının ileri yaş evresine varmış ve yaşlanmış olarak nitelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek için kullanılan niteleme, bazı bağlamlarda yaşlılığa bağlı zihinsel zayıflığı da bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kadına özgü yapıda, ileri yaşa varmış yaşlı kadın anlatılır."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İleri yaş çekirdeğini her iki cinsiyet için korur ve erkek nitelemesindeki olası zihinsel zayıflığı zorunluymuş gibi sunmaz.","boundary_detail":"İleri yaş temel anlamdır; bunama zorunlu bir özellik değil, yaşlı erkeği niteleyen daha dar bir kullanımdır.","branch_image_ar":"شيخ قَحْم في الهرم","concept_gloss":"ileri yaşlı, kimi kullanımda bunamış kişi","contextual_glosses":[{"applicability":"Bir kişinin ileri yaşa varmasını veya ileri yaşlı oluşunu bunama anlamı gerektirmeden anlatan bağlamlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek nitelemesinde bulunabilen yaşlılığa bağlı zihinsel zayıflık anlamını belirtmez.","preserves":"İleri yaşa varma ve yaşlı olma çekirdeğini açık biçimde korur."},"facet_ids":["F001","F003"],"text":"iyice yaşlanmış","usage_role":"general"}],"definition":"Belirli yapılarda bir insanın ileri yaşa varmasını veya ileri yaşlı erkek ve kadını anlatır; erkek için kullanılan niteleme kimi bağlamlarda zihinsel yetileri yaşlılıkla zayıflamış olmayı da içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan, yaşamının ileri yaş evresine varmış ve yaşlanmış olarak nitelenir."},{"facet_id":"F002","role":"specialization","statement":"Erkek için kullanılan niteleme, bazı bağlamlarda yaşlılığa bağlı zihinsel zayıflığı da bildirir."},{"facet_id":"F003","role":"specialization","statement":"Kadına özgü yapıda, ileri yaşa varmış yaşlı kadın anlatılır."}],"identity_rationale":"Dal insanın ileri yaşa varmasını ve yaşlı erkek ya da kadını doğru biçimde toplar; ancak bunama yalnızca erkek için verilen daha dar bir nitelemedir ve bütün yaşlılık alanına yayılmamalıdır. Tanım bu alt sınırı açık tutar.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yaşlanmak, ileri yaşa varmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yaşlı, kimi bağlamda bunamış erkek"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ileri yaşlı kadın"}],"lexicalization_note":"Anlam yalnızca yaşlanma fiil yapısına ve yaşlı erkek ya da kadını niteleyen belirli söz öbeklerine bağlı tutulur; bağımsız genel anlama çevrilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yaşlılıkla kapsam farkını ve düşkün yaşlılıkla derece farkını gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak yapı bakımından sınırlı ve kimi kullanımda bunama çağrışımlıdır; komşu ise insan yaşlılığının genel adlandırma alanıdır.","focus_only":"Odak, belirli niteleme yapılarında yaşlı erkeğin zihinsel zayıflığını da bildirebilir.","gloss":"özel yaşlı nitelemesi ile genel yaşlılık","neighbor_only":"Komşu, yaşlı erkek ve kadının yanı sıra yaşlılık durumunu ve yaşlanma eylemini daha genel bir söz varlığıyla kapsar.","neighbor_ref":"root_000834/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın ileri yaşa varmasını ve yaşlı kişi oluşunu anlatır."},{"boundary_match":"partial","distinction":"Odak genişçe ileri yaş alanını kapsar; komşu ise zihinsel yetilerin belirgin biçimde yitirildiği en düşkün evreyle sınırlıdır.","focus_only":"Odakta sıradan ileri yaş yeterlidir ve zihinsel zayıflık her kullanımda bulunmaz.","gloss":"ileri yaş ile düşkün yaşlılık","neighbor_only":"Komşu, insanın bilirken bilmez duruma düştüğü en düşkün yaşlılık evresini zorunlu kılar.","neighbor_ref":"root_000559/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yaşlılıkla bağlantılı zihinsel zayıflığı anlatabilir."}],"source_phrase_ar":"قحم قحوما إذا كبر (ayn)؛ القحم الشيخ الخرف والقحمة الشيخة (ayn)؛ شيخ قحم وعجوز قحمة إذا أسنا (jamhara)؛ شيخ قحم أي هم مثل قحل (sihah)","source_summary":"Ortak anlam ileri yaştır; erkek ve kadın için ayrı niteleme yapıları bulunur, zihinsel zayıflık ise erkek nitelemesinin daha dar bir yorumudur.","sources":["AY","JA","SI"],"what_is_ar":"كبر الرجل أو المرأة وهرمهما؛ الشيخ الخرف؛ العجوز القحمة","what_is_not_ar":"ليس البعير المقحم في سنه؛ وليس سنة الجدب؛ وليس اقتحام الشدة"},"support_links":[]},{"boundary":"Anlam yalnızca devenin iki yaş ve diş evresini tek yılda geçmesiyle ilgilidir; genel yaşlanma ya da tek bir dişin çıkması değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001202/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"iki yaş evresini bir yılda geçen deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve, normal gelişim sırasındaki iki ayrı yaş evresini tek yıl içinde geçirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu hızlanma, iki ardışık yaş basamağına ait diş değişimlerinin aynı yılda gerçekleşmesiyle gözlenir."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın olağandışı gelişim hızını, iki ardışık evrenin tek yılda tamamlanmasını ve bunun deveye özgü oluşunu birlikte karşılar.","boundary_detail":"Anlam yalnızca devenin iki yaş ve diş evresini tek yılda geçmesiyle ilgilidir; genel yaşlanma ya da tek bir dişin çıkması değildir.","branch_image_ar":"البعير المُقْحَم يركب سنا على سن","concept_gloss":"iki yaş evresini bir yılda geçen deve","contextual_glosses":[{"applicability":"Yaş basamaklarının hayvanın diş gelişimi üzerinden açıklandığı bağlamlarda daha somut ve doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deveyi, aynı yılda gerçekleşen iki ardışık diş değişimini ve hızlanmış gelişim sırasını korur."},"facet_ids":["F001","F002"],"text":"bir yılda iki diş evresi geçiren deve","usage_role":"explanatory"}],"definition":"Normalde art arda gelen iki yaş ve diş gelişimi basamağını tek bir yıl içinde tamamlayarak yaş evrelerini olağandışı biçimde üst üste bindiren devedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve, normal gelişim sırasındaki iki ayrı yaş evresini tek yıl içinde geçirir."},{"facet_id":"F002","role":"specialization","statement":"Bu hızlanma, iki ardışık yaş basamağına ait diş değişimlerinin aynı yılda gerçekleşmesiyle gözlenir."}],"identity_rationale":"Dalın çerçevesi, devenin normalde ayrı zamanlarda gerçekleşen iki yaş ve diş gelişimi basamağını tek yılda tamamlamasını doğru verir. Buradaki yaşlılık insan yaşlılığı değil, hayvanın alışılmadık hızdaki gelişim sırasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"iki yaş ve diş evresini bir yılda tamamlayan deve"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"normalde ardışık iki yaş basamağını tek yılda geçen deve"}],"lexicalization_note":"Tanım, deveyi adlandıran biçimle belirli deve nitelemesini aynı gelişim olgusuna bağlar; bu hayvana özgü anlam genel yaş kavramına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hızlanmış gelişimi genel yaş ve diş alanından, tek diş evresinden ve belirli sıradaki dişten ayıran üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak gelişim sırasındaki iki evrenin zaman bakımından üst üste binmesidir; komşu için böyle bir zaman sıkışması gerekmez.","focus_only":"Odak, iki ardışık deve yaş ve diş evresinin olağandışı biçimde tek yılda tamamlanmasını gerektirir.","gloss":"hızlanmış deve gelişimi ile diş ve yaş","neighbor_only":"Komşu, dişin kendisini, genel yaşı, genç oluşu ve hayvanın belirli diş evresine erişmesini daha geniş kapsamda adlandırır.","neighbor_ref":"root_000750/B004","relation_type":"same_field","shared_zone":"İki dal da hayvanın yaşının diş gelişimi yoluyla belirlenmesi alanına girer."},{"boundary_match":"partial","distinction":"Odak iki ardışık evren arasındaki zaman ilişkisidir; komşu ise tek bir diş türü ve ona bağlı yaş basamağıdır.","focus_only":"Odak, iki yaş basamağının aynı yılda geçirilmesi gibi olağandışı bir gelişim hızını bildirir.","gloss":"iki evrenin üst üste binmesi ile tek diş evresi","neighbor_only":"Komşu, ön dişleri ve hayvanın belirli bir dişi düşürerek eriştiği tek yaş evresini adlandırır.","neighbor_ref":"root_000208/B009","relation_type":"near_neighbor","shared_zone":"Her iki dalda da devenin yaşı, belirli ön dişlerin değişimiyle bağlantılıdır."},{"boundary_match":"field_only","distinction":"Odakta kurucu özellik evrelerin birleşen zamanıdır; komşuda kurucu özellik belirli sıradaki diş ve onun normal yaş basamağıdır.","focus_only":"Odak, devenin iki gelişim evresini tek yıla sığdıran olağandışı ilerlemesini gösterir.","gloss":"hızlı yaş geçişi ile belirli yaş dişi","neighbor_only":"Komşu, belirli bir sırada gelen tek bir deve dişi ve yaş basamağını gösterir.","neighbor_ref":"root_000689/B003","relation_type":"same_field","shared_zone":"İki dal, devenin yaş evrelerini dişlerin çıkma veya düşme sırasıyla belirler."}],"source_phrase_ar":"القحم البعير يثني ويربع في سنة واحدة فيقحم سنا على سن (maqayis)؛ المقحم البعير الذي يربع ويثنى في سنة واحدة فتقتحم سن (ayn)؛ المقحم البعير الذي يطرح سنين في سن (jamhara)؛ المقحم البعير الذي يربع ويثني في سنة واحدة فيقحم سنا على سن (sihah)","source_summary":"Ortak anlatım, devenin iki ardışık yaş ve diş gelişimi basamağını tek yıla sığdırmasını olağandışı bir ilerleme olarak tanımlar.","sources":["MQ","AY","JA","SI"],"what_is_ar":"البعير الذي يثني ويربع في سنة واحدة أو يطرح سنين في سن؛ تقدم سنه الحيواني على غير مجراه المعتاد","what_is_not_ar":"ليس الشيخ القحم؛ وليس اقتحام النهر أو الأمر؛ وليس سنة الجدب"},"support_links":[]},{"boundary":"Deve kullanımında sürücüsüz ilerleme, insan kullanımında ise çölde yetişip oradan ayrılmama kurucudur; iki koşul birbirine aktarılmaz.","branch_kind":"collocation","branch_ref":"root_001202/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"sürücüsüz ilerleyen deve veya çölden ayrılmamış kişi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Deve, çölde kendisini otlatan veya yönlendiren bir kişi olmaksızın ilerler."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi çölde yetişmiştir ve yetiştiği çöl çevresinden hiç ayrılmamıştır."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız belirtilmiş iki yapıda geçerlidir ve deve için hareket koşulunu, insan için yetişme ve kalma koşulunu ayrı ayrı korur.","boundary_detail":"Deve kullanımında sürücüsüz ilerleme, insan kullanımında ise çölde yetişip oradan ayrılmama kurucudur; iki koşul birbirine aktarılmaz.","branch_image_ar":"المُقْحَم في المفازة بلا سوق","concept_gloss":"sürücüsüz ilerleyen deve veya çölden ayrılmamış kişi","contextual_glosses":[{"applicability":"Devenin çölde kendisini otlatan veya yönlendiren kimse bulunmadan ilerlediği yapı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çölde yetişip oradan hiç ayrılmamış insanı anlatan ayrı yapıyı kapsamaz.","preserves":"Deveyi, çöl ortamını ve yönlendiren kişi olmadan ilerleme koşulunu korur."},"facet_ids":["F001"],"text":"çölde sürücüsüz ilerleyen deve","usage_role":"contextual"},{"applicability":"Bir insanın çölde yetişmesi ve yaşam çevresinden hiç çıkmaması birlikte anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çölde yönlendiren kimse olmadan ilerleyen deveye özgü yapıyı kapsamaz.","preserves":"İnsanın çölde yetişmesini ve o çevreden hiç ayrılmamasını birlikte korur."},"facet_ids":["F002"],"text":"çölde büyüyüp oradan hiç ayrılmamış kişi","usage_role":"contextual"}],"definition":"Belirli yapılardan biri, çölde kendisini otlatan veya süren kimse olmadan ilerleyen deveyi; diğeri ise çölde yetişmiş ve yaşamı boyunca oradan ayrılmamış kişiyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Deve, çölde kendisini otlatan veya yönlendiren bir kişi olmaksızın ilerler."},{"facet_id":"F002","role":"core","statement":"Kişi çölde yetişmiştir ve yetiştiği çöl çevresinden hiç ayrılmamıştır."}],"identity_rationale":"Dal, aynı çöl çevresine bağlı iki ayrı yapıyı birlikte taşır: biri sürücüsüz ilerleyen deveyi, diğeri çölde yetişip oradan hiç çıkmamış kişiyi anlatır. Tek bir genel nitelik varsaymak yerine bu iki yapı tanımda açıkça ayrılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"çölde otlatıcısı ve sürücüsü olmadan ilerleyen deve"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"çölde yetişmiş ve oradan hiç ayrılmamış kişi"}],"lexicalization_note":"Anlam yalnızca iki belirtilmiş yapıya bağlıdır; deve ve insan için farklı olan koşullar korunur ve bağımsız bir genel anlam üretilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; çölün yer adı olarak kullanımıyla olan alan ilişkisini ve uzak otlak hareketiyle olan yalnızca tematik bağı gösteren iki komşu seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak araziyi adlandırmaz, o çevredeki deve ve insanın özel durumunu niteler; komşu ise doğrudan arazi türünü gösterir.","focus_only":"Odak, çölde bulunan deve veya insan için sürücüsüz hareket ve yaşam boyu ayrılmama gibi belirli koşullar getirir.","gloss":"çöle bağlı katılımcı ile çöl arazisi","neighbor_only":"Komşu, kara ile deniz karşıtlığını, çölü ve ıssız açık araziyi yer türü olarak genel biçimde adlandırır.","neighbor_ref":"root_000104/B005","relation_type":"same_field","shared_zone":"İki dal da çöl ve ıssız kara çevresini ortak alan olarak paylaşır."},{"boundary_match":"thematic_only","distinction":"Odak sürücüsüz ilerleme ya da çölden ayrılmama koşuludur; komşu ise uzak otlağa yönelme ve yerleşimden uzaklaşma hareketidir.","focus_only":"Odakta deve sürücüsüz ilerler veya insan çölde yetişip oradan hiç ayrılmaz.","gloss":"çölde kalış ile uzak otlağa gidiş","neighbor_only":"Komşuda hayvan, sürü ya da onu güden kişi uzak otlağa gitme ve yerleşimden uzaklaşma hareketiyle tanımlanır.","neighbor_ref":"root_001006/B003","relation_type":"thematic","shared_zone":"İki dalda da hayvanlar, insanlar ve yerleşimden uzak açık arazi aynı yaşam sahnesinde bulunur."}],"source_phrase_ar":"بعير مقحم يقحم في مفازة من غير مسيم ولا سائق (ayn)؛ أعرابي مقحم أي نشأ في المفازة لم يخرج منها (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, sürücüsüz ilerleyen deve ile çölde yetişip hiç ayrılmamış kişiyi iki ayrı yapıda verir."}],"source_summary":"İki kullanım ortak olarak çöl çevresine bağlıdır, ancak biri devenin sürücüsüz hareketini, diğeri insanın yetişme yeri ve oradan ayrılmamasını anlatır.","sources":["AY"],"what_is_ar":"البعير الذي يمضي في المفازة من غير مسيم ولا سائق؛ الأعرابي الذي نشأ في المفازة ولم يخرج منها","what_is_not_ar":"ليس اقتحام النهر؛ وليس سنة الجدب التي تنقل الأعراب إلى الريف؛ وليس البعير المقحم في سنه"},"support_links":[]},{"boundary":"Anlam görsel değerlemeye bağlı iki ayrı sonucu kapsar; yaşından büyük sayma, küçümsemenin derecesi değil, görünüşün doğurduğu karşıt bir sonuçtur.","branch_kind":"collocation","branch_ref":"root_001202/B007","candidate_links":[{"candidate_id":"cand_e16caf2a6d6cae89049f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","surface_ar":"ٱقْتَحَمَ"}],"gloss":"gözde küçümseme veya görünüşünden yaşını büyük sayma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gözün görünene ilişkin değerlendirmesi, onun değerini veya görünüşünden çıkarılan yaşını belirler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir sonuçta görülen şey gözde küçülür, değersiz ve önemsiz bulunur."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer sonuçta küçük yaştaki biri heybeti ve güzelliği yüzünden gerçek yaşından daha büyük değerlendirilir."}}],"root_ar":"ق ح م","root_id":"root_001202","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirtilmiş göz yapılarında hem değeri düşüren yargıyı hem de heybet ve güzelliğin doğurduğu yüksek yaş tahminini birlikte temsil eder.","boundary_detail":"Anlam görsel değerlemeye bağlı iki ayrı sonucu kapsar; yaşından büyük sayma, küçümsemenin derecesi değil, görünüşün doğurduğu karşıt bir sonuçtur.","branch_image_ar":"اقتحام العين قدر الشيء","concept_gloss":"gözde küçümseme veya görünüşünden yaşını büyük sayma","contextual_glosses":[{"applicability":"Görülen şeyin değersiz, önemsiz veya aşağı görülmesi sonucunu anlatan yapıda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Heybet ve güzellik nedeniyle küçük birini yaşından büyük değerlendirme sonucunu dışarıda bırakır.","preserves":"Gözün yaptığı değer düşürücü yargıyı ve küçümseme sonucunu korur."},"facet_ids":["F001","F002"],"text":"gözünde küçümsemek","usage_role":"contextual"},{"applicability":"Küçük yaştaki birinin heybetli ve güzel görünmesi nedeniyle gerçek yaşından daha büyük değerlendirildiği yapıya uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir şeyi gözde değersiz ve önemsiz bulma sonucunu kapsamaz.","preserves":"Görsel izlenimden doğan yaş yükseltmesini ve bunun heybet ile güzelliğe dayanmasını korur."},"facet_ids":["F001","F003"],"text":"görünüşünden yaşını büyük sanmak","usage_role":"contextual"}],"definition":"Belirli göz yapılarında, görülen şeyi değersiz ve önemsiz bulmak veya küçük yaştaki birini heybeti ve güzelliği nedeniyle gerçek yaşından daha büyük saymaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gözün görünene ilişkin değerlendirmesi, onun değerini veya görünüşünden çıkarılan yaşını belirler."},{"facet_id":"F002","role":"source_variant","statement":"Bir sonuçta görülen şey gözde küçülür, değersiz ve önemsiz bulunur."},{"facet_id":"F003","role":"source_variant","statement":"Diğer sonuçta küçük yaştaki biri heybeti ve güzelliği yüzünden gerçek yaşından daha büyük değerlendirilir."}],"identity_rationale":"Kaynak ifadesi tek yönlü bir küçümsemeyi değil, gözün yaptığı iki ayrı değerlemeyi verir: bir şey gözde değersizleşebilir; küçük görünen biri de heybeti ve güzelliği nedeniyle gerçek yaşının üstünde değerlendirilebilir. Dal bu karşıt sonuçları tek sonuca indirmeden yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"gözümde küçüldü; onu küçümsedim"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"gözün küçük yaştakini heybeti ve güzelliği yüzünden yaşından büyük sayması"}],"lexicalization_note":"İki anlam yalnızca gözün değerlendirmesini anlatan belirtilmiş yapılara bağlı tutulur; bağımsız bir görme ya da değer biçme anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; küçümseme, heybetli görünüş ve karşılaştırmalı güzellik alanlarındaki üç farklı sınırı açıklayan komşular seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odakta yargı göz üzerinden kurulur ve karşıt bir yaş yükseltme sonucu da bulunur; komşu ise genel küçümseme alanında kalır.","focus_only":"Odak, gözün değerlendirmesine bağlıdır ve ayrıca görünüşten dolayı birini yaşından büyük sayma sonucunu içerir.","gloss":"gözde küçümseme ile genel hor görme","neighbor_only":"Komşu, görsel yapı gerektirmeden bir şeyi hafif, önemsiz veya değersiz bulmayı genel olarak kapsar.","neighbor_ref":"root_000255/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyin değerini düşürüp onu önemsiz görme yargısını anlatabilir."},{"boundary_match":"partial","distinction":"Odakta yükselen değerlendirme gerçek yaşın üstünde bir yaş tahminidir; komşuda büyüklük ve gösteriş doğrudan görünüş niteliğidir.","focus_only":"Odak, küçük yaştaki birini etkileyici görünüşü nedeniyle gerçek yaşının üstünde değerlendirmeye kadar uzanır.","gloss":"yaşı büyük sanma ile gözde heybetli görünme","neighbor_only":"Komşu, kişi veya topluluğun gözde büyük ve gösterişli görünmesini, yaş tahmini gerektirmeden anlatır.","neighbor_ref":"root_000269/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da görülen kişinin heybetli ve etkileyici görünmesi değerlendirmeyi yükseltir."},{"boundary_match":"field_only","distinction":"Odakta karşılaştırma grubu gerekmez ve yaş tahmini de mümkündür; komşuda değer değişimi daha güzel kişilerle yan yana gelmeye bağlıdır.","focus_only":"Odak, gözde küçümseme ile görünüşten yaş yükseltme gibi iki değerlendirme sonucunu içerir.","gloss":"gözün değerlemesi ile karşılaştırmalı güzellik","neighbor_only":"Komşu, tek başına güzel görünen bir kadının daha güzel kişiler arasında sönük kalmasını karşılaştırmalı olarak anlatır.","neighbor_ref":"root_000425/B005","relation_type":"same_field","shared_zone":"İki dal da görünüşe dayanarak değer ve güzellik hakkında değişebilen bir yargı kurar."}],"source_phrase_ar":"اقتحمته عيني ازدرته (sihah)؛ وقد يكون الذي تقحمه عينك صغيرا فترفعه فوق سنه لعظمه وحسنه (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, gözde küçümseme ile görünüşten dolayı yaşını büyük tahmin etme sonuçlarını birlikte verir."}],"source_summary":"Gözün değerlendirmesi iki farklı sonuca açılır: görülen şeyin değeri düşürülebilir veya küçük yaştaki biri etkileyici görünüşü nedeniyle yaşından büyük sayılabilir.","sources":["SI"],"what_is_ar":"ازدراء العين للشيء؛ وقد ترفعه فوق سنه لعظمه وحسنه","what_is_not_ar":"ليس دخولا في الشدة؛ وليس سن البعير في نفسه؛ وليس قحم الطريق"},"support_links":["sup_51c3aae11b81820403fc"]}],"candidate_inventory":[{"anchor_refs":["90:11:1"],"branch_refs":[],"candidate_id":"cand_d7d4cc470a9bbc396948","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:11:1:consequential-link-to-guidance","source_type":"word_analysis","support_ids":["sup_7998a29c9560a02cf684","sup_faf39bf8ef9d5c837202"],"title":"consequence after disclosed routes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:1","qac_refs":["90:11:1:1"],"status":"accepted"}},{"anchor_refs":["90:11:1"],"branch_refs":[],"candidate_id":"cand_fbcc226ede1520507ff3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:11:1:fused-adversative-opening","source_type":"word_analysis","support_ids":["sup_4094d3c8be9e7721baa7","sup_faf39bf8ef9d5c837202"],"title":"relation fused with refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:1","qac_refs":["90:11:1:1"],"status":"accepted"}},{"anchor_refs":["90:11:2"],"branch_refs":[],"candidate_id":"cand_ca154b08d0e2b07c0e2d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:11:2:evaluative-fronted-denial","source_type":"word_analysis","support_ids":["sup_002446883b14d4e4bd67","sup_0cc507545d7ee4cf73a7"],"title":"fronted evaluative refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:2","qac_refs":["90:11:1:2"],"status":"accepted"}},{"anchor_refs":["90:11:2"],"branch_refs":[],"candidate_id":"cand_c94d7776cb9e9c1b2ea0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"90:11:2:perfect-predicate-negated","source_type":"word_analysis","support_ids":["sup_0cc507545d7ee4cf73a7","sup_6c270a39b83080ff820c"],"title":"achieved crossing denied","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:2","qac_refs":["90:11:1:2"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_b33da555888989847bb2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:delayed-object-forward-bridge","source_type":"word_analysis","support_ids":["sup_277e7d25e34473ed8717","sup_35a683403d4204a81764"],"title":"verb launches unresolved threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_cfef7f1dcf90e9264394","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:direct-breach-target","source_type":"word_analysis","support_ids":["sup_35a683403d4204a81764","sup_8c6bb3d31d5a5d8a6bfa"],"title":"pass as breached object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_1d0502b5d7d789f4ab9f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:hazardous-entry-field","source_type":"word_analysis","support_ids":["sup_07bd05535254551c7d53","sup_35a683403d4204a81764"],"title":"hazardous entry into resistance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_47dbb4e48ca24515777f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:marked-form-and-variant-apparatus","source_type":"word_analysis","support_ids":["sup_35a683403d4204a81764","sup_a8f959ae75771ee0c9b3"],"title":"rare canonical breach form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_efda9e6db0b2e725c177","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:punitive-plunging-contrast","source_type":"word_analysis","support_ids":["sup_35a683403d4204a81764","sup_408d8eb5bddc2f91ab8b"],"title":"punitive plunging contrasted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_d884793ca3891a69bc75","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:responsible-self-involving-subject","source_type":"word_analysis","support_ids":["sup_35a683403d4204a81764","sup_42011a431917cf80c3e2"],"title":"accountable self-involving subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_e63ae372edec93ce8906","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:3:sound-and-continuity-pressure","source_type":"word_analysis","support_ids":["sup_35a683403d4204a81764","sup_7fb844d7025ee6e54dba"],"title":"sound presses into resistance","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:3","qac_refs":["90:11:2:1"],"status":"accepted"}},{"anchor_refs":["90:11:4"],"branch_refs":[],"candidate_id":"cand_97e402f4d527013cae32","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:4:closure-and-repetition-to-question","source_type":"word_analysis","support_ids":["sup_02b676747485f912ae17","sup_552f85e02e6d5bacbc5e"],"title":"closure becomes question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:4","qac_refs":["90:11:3:1","90:11:3:2"],"status":"accepted"}},{"anchor_refs":["90:11:4"],"branch_refs":[],"candidate_id":"cand_641c51b5bca054718dd9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:4:definite-accusative-target","source_type":"word_analysis","support_ids":["sup_4d42d5631b3becd6f78d","sup_552f85e02e6d5bacbc5e"],"title":"definite object as target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:4","qac_refs":["90:11:3:1","90:11:3:2"],"status":"accepted"}},{"anchor_refs":["90:11:4"],"branch_refs":[],"candidate_id":"cand_17b7dceb572f984f97e6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:4:steep-pass-with-aftermath-pressure","source_type":"word_analysis","support_ids":["sup_0fe39e56b5548d433009","sup_552f85e02e6d5bacbc5e"],"title":"steep pass with consequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:4","qac_refs":["90:11:3:1","90:11:3:2"],"status":"accepted"}},{"anchor_refs":["90:11:4"],"branch_refs":[],"candidate_id":"cand_f7d648bc225907db22ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:4:threshold-pair-and-sound","source_type":"word_analysis","support_ids":["sup_552f85e02e6d5bacbc5e","sup_885cf4aaa91e0d69084f"],"title":"hard-edged threshold pair","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:4","qac_refs":["90:11:3:1","90:11:3:2"],"status":"accepted"}},{"anchor_refs":["90:11:4"],"branch_refs":[],"candidate_id":"cand_9d8e33efc2038232925f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:4:two-routes-to-one-threshold","source_type":"word_analysis","support_ids":["sup_552f85e02e6d5bacbc5e","sup_fcdbbcea6a7d9e474736"],"title":"two routes narrow to one pass","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"90:11:4","qac_refs":["90:11:3:1","90:11:3:2"],"status":"accepted"}},{"anchor_refs":["90:11:2"],"branch_refs":[],"candidate_id":"cand_d2e5c4d54bfdc3bc089d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001202"],"scope":"focus_ayah","source_local_id":"90:11:2:1","source_type":"qac_morpheme","support_ids":["sup_e250ed6e0774ad76bf63"],"title":"QAC root occurrence: ق ح م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:11:3"],"branch_refs":[],"candidate_id":"cand_2e2f51e3098302ec7239","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001033"],"scope":"focus_ayah","source_local_id":"90:11:3:2","source_type":"qac_morpheme","support_ids":["sup_572c584a7e1bcd791bc0"],"title":"QAC root occurrence: ع ق ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["90:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:11","branch_refs":["root_001033/B012","root_001202/B001"],"candidate_id":"cand_74ca34cd4d71b4ba40cf","commentary_obligation":"review","hft_ref":"hft_4e1fed8f850f6fd95774","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_arduous_ascent","source_type":"hft","support_ids":["sup_70b5a391671fcb47d1e4"],"title":"baseline_arduous_ascent","trust":"legacy_unbound"},{"anchor_refs":["90:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:11","branch_refs":["root_001033/B002","root_001033/B003","root_001202/B002"],"candidate_id":"cand_4addf1548a483e1bc40d","commentary_obligation":"review","hft_ref":"hft_dc16978a15a0c0060f43","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_no_return_threshold","source_type":"hft","support_ids":["sup_e117d9ededbe9a855043"],"title":"baseline_no_return_threshold","trust":"legacy_unbound"},{"anchor_refs":["90:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:11","branch_refs":["root_001033/B006","root_001033/B010","root_001202/B002"],"candidate_id":"cand_2919f56e6cc6eab0cc88","commentary_obligation":"review","hft_ref":"hft_29ab4cd6158a52b34407","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_aftereffect_liability","source_type":"hft","support_ids":["sup_81d06cc4fbb6b9e3d6d8"],"title":"baseline_aftereffect_liability","trust":"legacy_unbound"},{"anchor_refs":["90:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:11","branch_refs":["root_001033/B012","root_001033/B015","root_001202/B003"],"candidate_id":"cand_185b710aa73a655c0c92","commentary_obligation":"review","hft_ref":"hft_f99bf9abd8801c46fa52","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_ecological_displacement","source_type":"hft","support_ids":["sup_44e0be4d69ef9ea83f12"],"title":"baseline_ecological_displacement","trust":"legacy_unbound"},{"anchor_refs":["90:11"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"90:11","branch_refs":["root_001033/B006","root_001033/B012","root_001202/B007"],"candidate_id":"cand_e16caf2a6d6cae89049f","commentary_obligation":"review","hft_ref":"hft_0e32edca4d8f9f880b1a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_misvalued_scale","source_type":"hft","support_ids":["sup_51c3aae11b81820403fc"],"title":"baseline_misvalued_scale","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"90:11:1:1","qac_word_ref":"90:11:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:11:1:2","qac_word_ref":"90:11:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","root_ar":"ق ح م","surface_ar":"ٱقْتَحَمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:11:3:1","qac_word_ref":"90:11:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","root_ar":"ع ق ب","surface_ar":"عَقَبَةَ"}],"word_analysis_qac_refs":[["90:11:1:1"],["90:11:1:2"],["90:11:2:1"],["90:11:3:1","90:11:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["90:11:1","90:11:2","90:11:3","90:11:4"]},"focus_surface_evidence":{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"90:11:1:1","qac_word_ref":"90:11:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"لَا","morph_features":"STEM|POS:NEG|LEM:laA","morpheme_role":"STEM","pos":"NEG","qac_ref":"90:11:1:2","qac_word_ref":"90:11:1","root_ar":"","surface_ar":"لَا"},{"lemma_ar":"ٱقْتَحَمَ","morph_features":"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"90:11:2:1","qac_word_ref":"90:11:2","root_ar":"ق ح م","surface_ar":"ٱقْتَحَمَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"90:11:3:1","qac_word_ref":"90:11:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عَقَبَة","morph_features":"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"90:11:3:2","qac_word_ref":"90:11:3","root_ar":"ع ق ب","surface_ar":"عَقَبَةَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["90:11:1:1"],["90:11:1:2"],["90:11:2:1"],["90:11:3:1","90:11:3:2"]],"word_analysis_refs":["90:11:1","90:11:2","90:11:3","90:11:4"],"word_rows":[{"analysis_record_ref":"90:11:1","analytic_gloss_range_en":"consequential discourse particle that links the failed crossing to the prior disclosure of the two routes, with an adversative turn once joined to the following negator","analytic_root_gloss_range_en":null,"qac_refs":["90:11:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"90:11:2","analytic_gloss_range_en":"negative particle scoping over the completed perfect predicate and its object, denying achieved entry into the pass rather than issuing a prohibition","analytic_root_gloss_range_en":null,"qac_refs":["90:11:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَا","transliteration":"lā"}},{"analysis_record_ref":"90:11:3","analytic_gloss_range_en":"negated Form VIII perfect of forceful self-involving entry into a difficult object; locally transitive with the pass as explicit target and not a general term for smooth ascent","analytic_root_gloss_range_en":"root range centered on plunging, thrusting, or being driven into hardship and dangerous undertakings, with other branches such as drought, decrepitude, age-stage overlap, unled desert-going, and eye-estimation not selected by this local frame","qac_refs":["90:11:2:1"],"root":{"arabic":"ق ح م","transliteration":"q-ḥ-m"},"surface":{"arabic":"ٱقْتَحَمَ","transliteration":"iqtaḥama"}},{"analysis_record_ref":"90:11:4","analytic_gloss_range_en":"the definite singular pass as accusative direct object: a concrete steep threshold that also carries follow-through and consequence pressure into the next ayah","analytic_root_gloss_range_en":"broad root range involving heel or rear trace, following after, return, outcome, punitive consequence, residue, and a steep pass; local grammar selects the steep-pass threshold while preserving aftermath pressure","qac_refs":["90:11:3:1","90:11:3:2"],"root":{"arabic":"ع ق ب","transliteration":"ʿ-q-b"},"surface":{"arabic":"ٱلْعَقَبَةَ","transliteration":"al-ʿaqabah"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["90:11"],"branch_refs":["root_001033/B012","root_001202/B001"],"candidate_id":"cand_74ca34cd4d71b4ba40cf","evidence_scope":"focus_ayah","hft_ref":"hft_4e1fed8f850f6fd95774","item_id":"baseline_arduous_ascent","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_arduous_ascent","support_id":"sup_70b5a391671fcb47d1e4"},{"anchor_refs":["90:11"],"branch_refs":["root_001033/B002","root_001033/B003","root_001202/B002"],"candidate_id":"cand_4addf1548a483e1bc40d","evidence_scope":"focus_ayah","hft_ref":"hft_dc16978a15a0c0060f43","item_id":"baseline_no_return_threshold","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_no_return_threshold","support_id":"sup_e117d9ededbe9a855043"},{"anchor_refs":["90:11"],"branch_refs":["root_001033/B006","root_001033/B010","root_001202/B002"],"candidate_id":"cand_2919f56e6cc6eab0cc88","evidence_scope":"focus_ayah","hft_ref":"hft_29ab4cd6158a52b34407","item_id":"baseline_aftereffect_liability","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_aftereffect_liability","support_id":"sup_81d06cc4fbb6b9e3d6d8"},{"anchor_refs":["90:11"],"branch_refs":["root_001033/B012","root_001033/B015","root_001202/B003"],"candidate_id":"cand_185b710aa73a655c0c92","evidence_scope":"focus_ayah","hft_ref":"hft_f99bf9abd8801c46fa52","item_id":"baseline_ecological_displacement","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_ecological_displacement","support_id":"sup_44e0be4d69ef9ea83f12"},{"anchor_refs":["90:11"],"branch_refs":["root_001033/B006","root_001033/B012","root_001202/B007"],"candidate_id":"cand_e16caf2a6d6cae89049f","evidence_scope":"focus_ayah","hft_ref":"hft_0e32edca4d8f9f880b1a","item_id":"baseline_misvalued_scale","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_misvalued_scale","support_id":"sup_51c3aae11b81820403fc"}],"diagnostics":[],"lane_counts":{"global":17,"macro":7,"micro":5},"packet_summary":{"ayah_count":20,"focus_ref":"90:11","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ح ل ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000351","furuq_root_norm":"ح ل ل","furuq_source_root_norm":"ح ل ل","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000353","furuq_root_norm":"ح ل ي","furuq_source_root_norm":"ح ل ي","is_dominant":false,"target_occurrences":6,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"و ص د","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000036","furuq_root_norm":"ء ص د","furuq_source_root_norm":"أ ص د","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001653","furuq_root_norm":"و ص د","furuq_source_root_norm":"و ص د","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["90:1","90:2","90:3","90:4","90:5","90:6","90:7","90:8","90:9","90:10","90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"90:11","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"90:11","lane":"micro","linguistic_source_ref":"90:11","surface_ref":"90:11","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"90:11","target_tokens":[["Ama",["90:11:1"]],["sarp",["90:11:3"]],["yokuşa",["90:11:3"]],["atılmadı",["90:11:1","90:11:2"]]],"text":"Ama sarp yokuşa atılmadı."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":11,"ayah_to":20,"id":"s090-p02-011-020","label":"The steep path and the two companies","number":2,"refs":["90:11","90:12","90:13","90:14","90:15","90:16","90:17","90:18","90:19","90:20"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:2:evaluative-fronted-denial","source_type":"word_analysis","support_id":"sup_002446883b14d4e4bd67","text":"{\"blocking_evidence\":null,\"headline\":\"fronted evaluative refusal\",\"reader_payoff\":\"The reader feels the negation as an evaluative verdict after guidance, arriving before the action and target are disclosed.\",\"reason\":\"The surface sequence places the negator immediately after the discourse particle and before the perfect verb and object.\",\"representative_source_ids\":[\"QS-e7b21398\",\"QT-a93f1e78\",\"QB-4817f07d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4:closure-and-repetition-to-question","source_type":"word_analysis","support_id":"sup_02b676747485f912ae17","text":"{\"blocking_evidence\":null,\"headline\":\"closure becomes question\",\"reader_payoff\":\"The reader notices that the final object is not left self-explanatory; its exact recurrence in the next ayah (90:12) turns refusal into an interpretive question.\",\"reason\":\"The attachment support explicitly recommends reading the following ayah because it asks what the pass is and unfolds the answer sequence.\",\"representative_source_ids\":[\"QI-e67c1304\",\"QE-c8c60a92\",\"QY-8bd50960\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:hazardous-entry-field","source_type":"word_analysis","support_id":"sup_07bd05535254551c7d53","text":"{\"blocking_evidence\":null,\"headline\":\"hazardous entry into resistance\",\"reader_payoff\":\"The reader feels the demanded good as a plunge into resistance, not as smooth motion along a known route.\",\"reason\":\"The local object is the pass, so the root field of entering hardship is locally licensed as the pressure behind the moral threshold.\",\"representative_source_ids\":[\"QS-5db4a7de\",\"QS-edb1cdd5\",\"MS-1beb050b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:2","source_type":"word_analysis","support_id":"sup_0cc507545d7ee4cf73a7","text":"{\"gloss_range\":\"negative particle scoping over the completed perfect predicate and its object, denying achieved entry into the pass rather than issuing a prohibition\",\"prose\":\"{{ar:لَا}} ({{tr:lā}}) denies the whole predicate {{ar:ٱقْتَحَمَ ٱلْعَقَبَةَ}} ({{tr:iqtaḥama al-ʿaqabah}}). The scope is not merely a negative mood around the verb, and it is not a command not to enter; it says the achieved crossing did not take place. Since it follows {{ar:فَ}} ({{tr:fa}}), the refusal is bound to the prior disclosure of routes (90:10). The listener meets non-performance first, then the clustered verb and final object reveal what demanding act was left undone.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَا}} ({{tr:lā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4:steep-pass-with-aftermath-pressure","source_type":"word_analysis","support_id":"sup_0fe39e56b5548d433009","text":"{\"blocking_evidence\":null,\"headline\":\"steep pass with consequence\",\"reader_payoff\":\"The reader sees the word as both concrete terrain and costly follow-through: local grammar selects the pass, while the root field keeps aftermath pressure alive.\",\"reason\":\"The local verb-object frame selects the steep-pass branch, while accepted root branches for following and outcome support the retained consequence pressure without replacing the concrete noun.\",\"representative_source_ids\":[\"QS-7d26748e\",\"QS-c4cbbd8b\",\"QY-056185fd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:delayed-object-forward-bridge","source_type":"word_analysis","support_id":"sup_277e7d25e34473ed8717","text":"{\"blocking_evidence\":null,\"headline\":\"verb launches unresolved threshold\",\"reader_payoff\":\"The reader notices that the force of non-entry arrives before the object is named, preparing the next ayah's question about the pass (90:12).\",\"reason\":\"The local order places the verb before the object, and the attachment support warns that the following ayah explains the pass.\",\"representative_source_ids\":[\"QT-df9e85d6\",\"QB-285e4152\",\"QB-33ef7291\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3","source_type":"word_analysis","support_id":"sup_35a683403d4204a81764","text":"{\"gloss_range\":\"negated Form VIII perfect of forceful self-involving entry into a difficult object; locally transitive with the pass as explicit target and not a general term for smooth ascent\",\"prose\":\"{{ar:ٱقْتَحَمَ}} ({{tr:iqtaḥama}}) is the clause engine: the negator targets this completed act, and the following definite pass is its direct object. The verb therefore names not vague goodness but forceful entry into a resistant target. Because the verb arrives before the object, the force of missing action is heard before the pass is named, setting up the question in 90:12. Its Form VIII shape keeps the implicit human from 90:10 personally inside the action; the failure belongs to the guided person as an accountable subject, not to an absent opportunity. The root field of plunging into hardship makes the moral passage feel hazardous and costly, while local grammar keeps the selected sense to this transitive breach of {{ar:ٱلْعَقَبَةَ}} ({{tr:al-ʿaqabah}}). The guttural-heavy root texture closing into mīm and the Form VIII infix cluster make the pronunciation itself push into resistance. The rare finite form also stands out against variant or related event-shapes: a verbal-noun apparatus can expose the same absent undertaking, but the canonical local wording remains the denied finite act. Against the other supplied scene of punitive plunging (38:59), here the demanded entry would have been voluntary saving hardship, and it is precisely what did not happen.\",\"root_display\":\"{{ar:ق ح م}} ({{tr:q-ḥ-m}})\",\"root_gloss_range\":\"root range centered on plunging, thrusting, or being driven into hardship and dangerous undertakings, with other branches such as drought, decrepitude, age-stage overlap, unled desert-going, and eye-estimation not selected by this local frame\",\"surface_display\":\"{{ar:ٱقْتَحَمَ}} ({{tr:iqtaḥama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:punitive-plunging-contrast","source_type":"word_analysis","support_id":"sup_408d8eb5bddc2f91ab8b","text":"{\"blocking_evidence\":null,\"headline\":\"punitive plunging contrasted\",\"reader_payoff\":\"The reader sees the contrast with punitive plunging (38:59): this ayah negates a voluntary entry into saving hardship, not a forced crowding into punishment.\",\"reason\":\"The supplied comparison is a real same-root scene, but it is an active participle in another context, so it works as contrast rather than as the local parse.\",\"representative_source_ids\":[\"QI-e78cf2f8\",\"MI-68d94d52\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:1:fused-adversative-opening","source_type":"word_analysis","support_id":"sup_4094d3c8be9e7721baa7","text":"{\"blocking_evidence\":null,\"headline\":\"relation fused with refusal\",\"reader_payoff\":\"The reader hears the turn into denial before any lexical scene appears, so the ayah begins with connected reversal rather than neutral setup.\",\"reason\":\"The source surface joins the particle to the following negator, while the analytical split preserves the particle's discourse role.\",\"representative_source_ids\":[\"QS-c20bf886\",\"QF-76086847\",\"QT-0867303c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:responsible-self-involving-subject","source_type":"word_analysis","support_id":"sup_42011a431917cf80c3e2","text":"{\"blocking_evidence\":null,\"headline\":\"accountable self-involving subject\",\"reader_payoff\":\"The reader notices that the missing action is assigned to the same guided human as a personally undertaken entry, not to a detached observer or external blockage.\",\"reason\":\"The verb is active perfect third masculine singular with an implicit subject inferred from the surrounding discourse, and the Form VIII rows coherently press self-involving entry.\",\"representative_source_ids\":[\"QG-6758d61e\",\"QG-d9c01366\",\"QF-16c7ffee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4:definite-accusative-target","source_type":"word_analysis","support_id":"sup_4d42d5631b3becd6f78d","text":"{\"blocking_evidence\":null,\"headline\":\"definite object as target\",\"reader_payoff\":\"The reader notices that the pass is the direct, definite thing refused, not an indefinite obstacle or a place merely approached.\",\"reason\":\"The noun is definite feminine singular accusative and is syntactically forced as the explicit object of the preceding verb.\",\"representative_source_ids\":[\"QG-650b5cd2\",\"QG-e46908f1\",\"QG-fdef5855\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4","source_type":"word_analysis","support_id":"sup_552f85e02e6d5bacbc5e","text":"{\"gloss_range\":\"the definite singular pass as accusative direct object: a concrete steep threshold that also carries follow-through and consequence pressure into the next ayah\",\"prose\":\"{{ar:ٱلْعَقَبَةَ}} ({{tr:al-ʿaqabah}}) is the definite accusative object of {{ar:ٱقْتَحَمَ}} ({{tr:iqtaḥama}}), so the verb has a marked target rather than a vague heroic mood. The article and singular form make the pass identifiable and concentrated: not some scattered set of obstacles, but the one threshold that follows the disclosed routes of 90:10. The root field keeps the image double: it is a steep pass to enter, and it is also the costly follow-through or consequence after prior endowment. Because the word closes 90:11 and recurs in 90:12, the refused object is left unresolved on purpose; the next ayah reopens the same pass as a question. Its hard consonantal texture and final closure fit the obstacle that halts the clause after the denied verb.\",\"root_display\":\"{{ar:ع ق ب}} ({{tr:ʿ-q-b}})\",\"root_gloss_range\":\"broad root range involving heel or rear trace, following after, return, outcome, punitive consequence, residue, and a steep pass; local grammar selects the steep-pass threshold while preserving aftermath pressure\",\"surface_display\":\"{{ar:ٱلْعَقَبَةَ}} ({{tr:al-ʿaqabah}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:11:3:2","source_type":"qac_morpheme","support_id":"sup_572c584a7e1bcd791bc0","text":"{\"lemma_ar\":\"عَقَبَة\",\"morph_features\":\"STEM|POS:N|LEM:Eaqabap|ROOT:Eqb|F|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"90:11:3:2\",\"qac_word_ref\":\"90:11:3\",\"root_ar\":\"ع ق ب\",\"surface_ar\":\"عَقَبَةَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:2:perfect-predicate-negated","source_type":"word_analysis","support_id":"sup_6c270a39b83080ff820c","text":"{\"blocking_evidence\":null,\"headline\":\"achieved crossing denied\",\"reader_payoff\":\"The reader notices that the ayah denies accomplished entry into the pass, not mere reluctance, future unwillingness, or a bare negative feeling.\",\"reason\":\"The attachment evidence explicitly marks the negator as scoping over the verbal predicate with its object.\",\"representative_source_ids\":[\"QG-3621cc75\",\"QG-b2512e21\",\"QS-32ffb4fc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:1:consequential-link-to-guidance","source_type":"word_analysis","support_id":"sup_7998a29c9560a02cf684","text":"{\"blocking_evidence\":null,\"headline\":\"consequence after disclosed routes\",\"reader_payoff\":\"The reader notices that the failed crossing is a consequence drawn from prior guidance (90:10), not an isolated saying about difficulty.\",\"reason\":\"The QAC row identifies the word as the prefixed conjunction or discourse particle introducing the negated clause, and the clause evidence keeps that clause syntactically unified.\",\"representative_source_ids\":[\"QG-8b26863e\",\"QG-9ab49f87\",\"QB-16664712\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:sound-and-continuity-pressure","source_type":"word_analysis","support_id":"sup_7fb844d7025ee6e54dba","text":"{\"blocking_evidence\":null,\"headline\":\"sound presses into resistance\",\"reader_payoff\":\"The reader hears the clustered, guttural-heavy verb as fitting the sense of pushing into a hard obstacle.\",\"reason\":\"The sound rows are locally tied to the actual verb and its neighboring object, and they do not require a semantic claim beyond phonetic reinforcement.\",\"representative_source_ids\":[\"QE-d07f764f\",\"QP-3aeb9128\",\"QP-7a510265\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4:threshold-pair-and-sound","source_type":"word_analysis","support_id":"sup_885cf4aaa91e0d69084f","text":"{\"blocking_evidence\":null,\"headline\":\"hard-edged threshold pair\",\"reader_payoff\":\"The reader hears the object as a hard-edged close to the verb-object pair, matching the sense of a barrier that stops movement.\",\"reason\":\"The rows tie the sound texture to the actual local verb-object pair and do not require importing an unsupported branch.\",\"representative_source_ids\":[\"ME-f564a358\",\"QP-2ee565fe\",\"QP-d19b3127\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:direct-breach-target","source_type":"word_analysis","support_id":"sup_8c6bb3d31d5a5d8a6bfa","text":"{\"blocking_evidence\":null,\"headline\":\"pass as breached object\",\"reader_payoff\":\"The reader sees that the verb takes the pass itself as the thing to be entered, so the ayah judges a missed breach of a definite target.\",\"reason\":\"The attachment row marks the following noun as the explicit direct object governed by this verb.\",\"representative_source_ids\":[\"QG-0942275a\",\"QI-7c1cf93e\",\"QT-525ca36b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:3:marked-form-and-variant-apparatus","source_type":"word_analysis","support_id":"sup_a8f959ae75771ee0c9b3","text":"{\"blocking_evidence\":null,\"headline\":\"rare canonical breach form\",\"reader_payoff\":\"The reader notices that the canonical wording preserves a rare finite Form VIII breach act, while variant and related forms clarify the event without replacing the local parse.\",\"reason\":\"The canonical local form is a perfect active Form VIII verb; variant or neighboring forms can illuminate the event shape but do not govern the aligned surface.\",\"representative_source_ids\":[\"QF-a3579001\",\"QI-7196b294\",\"QH-556ded71\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"90:11:2:1","source_type":"qac_morpheme","support_id":"sup_e250ed6e0774ad76bf63","text":"{\"lemma_ar\":\"ٱقْتَحَمَ\",\"morph_features\":\"STEM|POS:V|PERF|(VIII)|LEM:{qotaHama|ROOT:qHm|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"90:11:2:1\",\"qac_word_ref\":\"90:11:2\",\"root_ar\":\"ق ح م\",\"surface_ar\":\"ٱقْتَحَمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:1","source_type":"word_analysis","support_id":"sup_faf39bf8ef9d5c837202","text":"{\"gloss_range\":\"consequential discourse particle that links the failed crossing to the prior disclosure of the two routes, with an adversative turn once joined to the following negator\",\"prose\":\"{{ar:فَ}} ({{tr:fa}}) makes 90:11 answer the prior disclosure of the two raised routes (90:10). The ayah does not float a moral proverb; it turns given capacity and guidance into an evaluative consequence: the expected crossing has not happened. Because the particle is heard and written into {{ar:فَلَا}} ({{tr:fa-lā}}), relation and refusal arrive together before the verb or object is named. The brief opening snaps the discourse from bestowed orientation into negated action.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"90:11:4:two-routes-to-one-threshold","source_type":"word_analysis","support_id":"sup_fcdbbcea6a7d9e474736","text":"{\"blocking_evidence\":null,\"headline\":\"two routes narrow to one pass\",\"reader_payoff\":\"The reader sees the movement from two disclosed raised routes (90:10) into one definite threshold that tests whether guidance becomes costly passage.\",\"reason\":\"The same-surah bridge is supplied by the CRITICAL rows, and the local noun's singular definiteness supports the contraction from open orientation to one named pass.\",\"representative_source_ids\":[\"MT-22b90a77\",\"QE-94fc28bf\",\"QB-5eb76031\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","ayah_ref":"90:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001033/B012","root_001202/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001202","role":"Entering severe danger without prior security supplies the forceful launch into the mechanism.","root":"ق ح م","source_ref":"90:11","source_word_indices":["2"]},{"branch_id":"B012","mapped_root_id":"root_001033","role":"The steep pass and jutting rock give that dangerous entry its resistant upward terrain.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]}],"changed_reading":{"after":"He did not launch into the steep, dangerous ascent; the failure occurs before committed entry, not only at the summit.","before":"He simply failed to get past an unspecified obstacle."},"confidence":"strong","focus_anchor":"The verb ٱقْتَحَمَ and the object ٱلْعَقَبَةَ join forceful entry to a steep obstruction.","mechanism":"A severe or frightening undertaking is spatialized as a rising, jutting pass: crossing requires entering the danger rather than remaining before it.","model_id":"baseline_arduous_ascent"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_arduous_ascent","source_type":"hft","support_id":"sup_70b5a391671fcb47d1e4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","ayah_ref":"90:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001033/B002","root_001033/B003","root_001202/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001202","role":"A perilous great affair not ridden by everyone makes entry a selective commitment.","root":"ق ح م","source_ref":"90:11","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001033","role":"Turning back on the heel supplies the live reverse motion against which committed advance is measured.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001033","role":"The heel and rear trace locate the abandoned path immediately behind the would-be crosser.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]}],"changed_reading":{"after":"The clause can instead expose recoil at a no-easy-return threshold: he never converts approach into committed advance.","before":"The clause reports inability to surmount difficult ground."},"confidence":"medium","focus_anchor":"The same two focus words can organize danger around advance, heel, and recoil.","mechanism":"The pass is a commitment threshold: it is an affair not everyone undertakes, and its opposite motion is retreat on the heel. The negation therefore marks refusal to enter a course whose first step forecloses easy recoil.","model_id":"baseline_no_return_threshold"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_no_return_threshold","source_type":"hft","support_id":"sup_e117d9ededbe9a855043","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","ayah_ref":"90:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001033/B006","root_001033/B010","root_001202/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001202","role":"Road dangers and unwanted consequences of dispute let forceful entry extend from terrain into costly aftermath.","root":"ق ح م","source_ref":"90:11","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_001033","role":"The end and result turn the pass into what follows from an action.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]},{"branch_id":"B010","mapped_root_id":"root_001033","role":"Substitution and retained liability give the aftermath a concrete claim that remains to be discharged.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]}],"changed_reading":{"after":"He did not enter the accountable consequence of action—the pass is also the claim and aftermath one accepts rather than evades.","before":"He did not cross a piece of difficult terrain."},"confidence":"exploratory","focus_anchor":"ٱلْعَقَبَةَ also carries aftermath, follow-up claim, and retained liability, while ٱقْتَحَمَ can enter dangers and unwanted consequences.","mechanism":"The obstacle is temporal and juridical as well as spatial. To act is to enter what the act leaves behind—its outcome, claim, or liability—whereas non-crossing is avoidance of that accountable aftermath.","model_id":"baseline_aftereffect_liability"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_aftereffect_liability","source_type":"hft","support_id":"sup_81d06cc4fbb6b9e3d6d8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","ayah_ref":"90:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001033/B012","root_001033/B015","root_001202/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001202","role":"The barren year that drives desert people into settled land supplies compelled crisis-movement.","root":"ق ح م","source_ref":"90:11","source_word_indices":["2"]},{"branch_id":"B015","mapped_root_id":"root_001033","role":"Plant yellowing and approaching dryness supplies the environmental pressure behind that movement.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]},{"branch_id":"B012","mapped_root_id":"root_001033","role":"The difficult pass keeps the ecological transition anchored in the focus noun's terrain.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]}],"changed_reading":{"after":"The pass may also be a drought-made threshold that forces vulnerable movement; refusing it means declining encounter with displacement and scarcity.","before":"The pass is a stable mountain obstacle chosen by an individual."},"confidence":"exploratory","focus_anchor":"A focus branch of ٱقْتَحَمَ names a drought-year that drives people into settlement, while a branch of ٱلْعَقَبَةَ tracks vegetation hardening toward dryness.","mechanism":"The pass can be an ecological threshold: drying land forces movement across a harsh boundary. The negated entry then evokes failure to face a crisis that displaces bodies rather than a voluntary feat of mountaineering.","model_id":"baseline_ecological_displacement"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_ecological_displacement","source_type":"hft","support_id":"sup_44e0be4d69ef9ea83f12","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ","ayah_ref":"90:11"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001033/B006","root_001033/B012","root_001202/B007"],"payload":{"activation_trace":[{"branch_id":"B007","mapped_root_id":"root_001202","role":"The eye's under- or over-estimation makes faulty appraisal an internal cause of non-entry.","root":"ق ح م","source_ref":"90:11","source_word_indices":["2"]},{"branch_id":"B012","mapped_root_id":"root_001033","role":"The visibly steep pass is the demand whose apparent and effective scale can diverge.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]},{"branch_id":"B006","mapped_root_id":"root_001033","role":"Outcome supplies the less visible measure by which the pass should be valued.","root":"ع ق ب","source_ref":"90:11","source_word_indices":["3"]}],"changed_reading":{"after":"His failure may begin in seeing wrongly: he mistakes visible size for the pass's true, outcome-bearing cost.","before":"He sees a hard obstacle and fails to cross it."},"confidence":"medium","focus_anchor":"A branch internal to ٱقْتَحَمَ concerns the eye under- or over-sizing a thing, and ٱلْعَقَبَةَ supplies the thing whose scale must be judged.","mechanism":"Non-entry may arise from distorted valuation rather than absent strength. The pass is mis-sized by the observer, so apparent magnitude and actual demand come apart.","model_id":"baseline_misvalued_scale"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_misvalued_scale","source_type":"hft","support_id":"sup_51c3aae11b81820403fc","trust":"legacy_unbound"}]}
</lane_packet_json>
