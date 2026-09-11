# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **101:1**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s101-regular-20260911/s101/101_1/micro.discovery.json` and modify nothing
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
  "ayah_ref": "101:1",
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
{"analysis_context":{"analysis_id":"s101-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"101:1","host_surah":101,"lane_context_refs":[],"ordered_context_refs":["101:0","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal fiziksel vuruş ve çarpma ile sınırlıdır; kura, felaket, kellik ve başka eş sesli anlamlar buna girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B001","candidate_links":[{"candidate_id":"cand_70acc7510365cddb374e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"bir şeye vurmak veya çarpmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne başka bir nesneye vurulur veya çarptırılır; kapı çalma ve hayvana vurma bu çekirdeğin uygulamalarıdır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesneler arasındaki doğrudan vuruş, çarpma ve bu temasla uyarma çekirdeğinin tamamında kullanılabilir.","boundary_detail":"Dal fiziksel vuruş ve çarpma ile sınırlıdır; kura, felaket, kellik ve başka eş sesli anlamlar buna girmez.","branch_image_ar":"ضرب شيء على شيء","concept_gloss":"bir şeye vurmak veya çarpmak","contextual_glosses":[{"applicability":"Vuruşun bir kapıya yönelip içeridekilere seslenme veya varlığını bildirme amacı taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kapı dışındaki nesneleri ve uyarma amacı taşımayan vuruşları dışarıda bırakır.","preserves":"Vurarak temas ve ses çıkarma unsurunu korur."},"facet_ids":["F001"],"text":"kapıyı çalmak","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye kuvvet uygulayarak vurmak, çarptırmak veya bu yolla dikkat çekici bir ses çıkarmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne başka bir nesneye vurulur veya çarptırılır; kapı çalma ve hayvana vurma bu çekirdeğin uygulamalarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başka bir şeye vurma veya çarptırma çekirdeğini açıkça destekler. Kapı çalma, hayvana vurma ve çeşitli araçlar bu fiziksel temas çekirdeğinin özel gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"vurmak, çarpmak veya vurarak uyarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kaptakini sonuna kadar içince kabın alnına değmesi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"hayvana vurmak için kullanılan değnek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"taş kırmaya yarayan balta benzeri araç"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"ateş yakmak için kullanılan çakma aracı"}],"lexicalization_note":"Tanım yalın vurma çekirdeğini verir; kaba, hayvana veya belirli araçlara bağlı kullanımlar ayrı ve yapıya bağlı kalır.","neighbor_coverage_note":"Bütün aday komşular karşılaştırıldı; yalnızca genel vurma anlamıyla en yakın ve sınır açıklayıcı karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal nesne-nesne çarpmasını ve sesle uyarmayı da kapsarken komşu dal daha çok el veya araçla yapılan doğrudan darbeye odaklanır.","focus_only":"Nesneleri birbirine çarptırma ve kapı çalma gibi uyarıcı vuruşları da kapsar.","gloss":"doğrudan vurma","neighbor_only":"El, sopa veya silah gibi bir araçla doğrudan vurma eylemini özellikle öne çıkarır.","neighbor_ref":"root_000906/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da kuvvet uygulanarak bir şeyin başka bir şeye temas ettirilmesi vardır."}],"source_phrase_ar":"القاف والراء والعين معظم الباب ضرب الشيء (maqayis)؛ كل شيء ضربته فقد قرعته (ayn)؛ قرعت الباب أقرعه قرعا (sihah)؛ قرع راحلته أي ضربها بسوطه (tahdhib)؛ القرع ضرب شيء على شيء (mufradat)","source_summary":"Kaynaklar, anlamın temelini iki şey arasındaki doğrudan vuruş veya çarpma olarak ortak biçimde verir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قرع الشيء والباب والرأس والإناء والجبهة، وما يضرب به كالمقرعة والمقراع، وضرب الدابة أو كبحها إذا صرح النص بالضرب أو الصك.","what_is_not_ar":"لا يدخل فيه الاقتراع ولا القارعة ولا القرع بمعنى ذهاب الشعر إلا بقرينة مستقلة."},"support_links":["sup_efb12cfd015bdbe0f87d"]},{"boundary":"Dal savaş veya silahlı mücadeledeki karşılıklı çarpışmadır; kura çekme ve sıradan fiziksel vurma bu sınıra girmez.","branch_kind":"bare","branch_ref":"root_001219/B002","candidate_links":[{"candidate_id":"cand_db086dcddb5daaf9093e","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"kılıçlarla karşılıklı çarpışmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf savaş bağlamında birbirine karşı çıkar ve kılıçlarla karşılıklı darbeler indirir."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Savaşçıların veya rakip tarafların kılıçlarla birbirine karşılıklı saldırdığı bütün bağlamlarda uygundur.","boundary_detail":"Dal savaş veya silahlı mücadeledeki karşılıklı çarpışmadır; kura çekme ve sıradan fiziksel vurma bu sınıra girmez.","branch_image_ar":"مقارعة ومضاربة","concept_gloss":"kılıçlarla karşılıklı çarpışmak","contextual_glosses":[{"applicability":"Metin iki savaşçının veya iki rakip tarafın yüz yüze mücadelesini öne çıkardığında doğal bir karşılıktır.","error_profile":{"adds":"Kılıç kullanılmayan veya savaş dışında kalan mücadeleleri de çağrıştırabilir.","collision":null,"fit":"broadening","loses":null,"preserves":"Rakipler arasındaki karşılıklı mücadeleyi korur."},"facet_ids":["F001"],"text":"rakibiyle çarpışmak","usage_role":"contextual"}],"definition":"Savaşta veya silahlı mücadelede rakiplerin birbirine kılıç darbeleri indirerek karşılıklı dövüşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf savaş bağlamında birbirine karşı çıkar ve kılıçlarla karşılıklı darbeler indirir."}],"identity_rationale":"Kaynak ifadesi, savaşta rakiplerin birbirine kılıçla vurmasını ve karşılıklı dövüşmesini açıkça anlatır. Rakip kişi de bu karşılıklı mücadelede yüz yüze gelinen kişidir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"savaşta kılıçlarla karşılıklı dövüşme"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dövüşte karşı karşıya gelen rakip"}],"lexicalization_note":"Tanım yalın dalı kapsar ve onu belirli bir kalıba, tek bir savaşçı çiftine veya özel bir örneğe bağlamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bire bir dövüş komşusu, karşılıklılık ile tekli karşılaşma arasındaki sınırı en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın çekirdeği karşılıklı silahlı çarpışmadır; komşu dal ise özellikle topluluktan ayrılarak yapılan bire bir dövüşü belirtir.","focus_only":"Daha geniş bir savaş sahnesinde karşılıklı kılıç dövüşünü ve rakipliği kapsayabilir.","gloss":"bire bir dövüş","neighbor_only":"Bir savaşçının topluluğundan çıkıp tek bir rakiple bire bir dövüşmesini gerektirir.","neighbor_ref":"root_000105/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da savaşçıların yüz yüze gelerek birbirleriyle dövüşmesi bulunur."}],"source_phrase_ar":"مقارعة الأبطال قرع بعضهم بعضا (maqayis)؛ المقارعة والقراع المضاربة بالسيف في الحرب (ayn)؛ قريعك الذي يقارعك (sihah)؛ القراع والمقارعة المضاربة بالسيوف (tahdhib)","source_summary":"Kaynaklar, karşılıklı savaşmayı ve özellikle kılıçlarla yapılan silahlı çarpışmayı ortak çekirdek olarak sunar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه مقارعة الأبطال، والقراع والمقارعة في الحرب، ومغالبة القرين أو من يقارعك.","what_is_not_ar":"لا يدخل فيه الإقراع بمعنى القرعة والمساهمة، ولا القارعة بمعنى النازلة."},"support_links":["sup_a9b5d109afcf62570e4b"]},{"boundary":"Dal hayvanların çiftleşme ve damızlık kullanımıyla sınırlıdır; genel vurma, rastgele seçim veya önderlik anlamına genişletilemez.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"damızlık erkeğin dişiyle çiftleşmesi ve dişinin erkeği istemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Damızlık erkek, üreme amacıyla dişinin üzerine çıkar ve onunla çiftleşir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi deve veya sığır çiftleşme isteği göstererek damızlık erkeği arar."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeğin çiftleşme eylemini ve dişinin çiftleşme isteğini birlikte kapsayan genel açıklama olarak kullanılır.","boundary_detail":"Dal hayvanların çiftleşme ve damızlık kullanımıyla sınırlıdır; genel vurma, rastgele seçim veya önderlik anlamına genişletilemez.","branch_image_ar":"ضراب الفحل وإنزاؤه","concept_gloss":"damızlık erkeğin dişiyle çiftleşmesi ve dişinin erkeği istemesi","contextual_glosses":[{"applicability":"Özne damızlık erkek hayvan ve anlatılan olay onun dişiye çıkması olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dişinin çiftleşme isteyip erkeği araması yönünü dışarıda bırakır.","preserves":"Erkek hayvanın üreme amaçlı çiftleşme eylemini korur."},"facet_ids":["F001"],"text":"dişiyle çiftleşmek","usage_role":"contextual"},{"applicability":"Özne dişi deve veya sığır ve odak onun çiftleşme isteği olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Damızlık erkeğin dişiye çıkıp çiftleşmesi eylemini dışarıda bırakır.","preserves":"Dişinin çiftleşme isteğini ve erkeğe yönelmesini korur."},"facet_ids":["F002"],"text":"kızışıp erkek aramak","usage_role":"contextual"}],"definition":"Damızlık erkek hayvanın dişiye çiftleşmek için çıkmasıdır. Aynı sahnede dişi deve veya sığırın çiftleşme isteyerek erkeği araması da anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Damızlık erkek, üreme amacıyla dişinin üzerine çıkar ve onunla çiftleşir."},{"facet_id":"F002","role":"associated_use","statement":"Dişi deve veya sığır çiftleşme isteği göstererek damızlık erkeği arar."}],"identity_rationale":"Kaynak ifadesi hem damızlık erkeğin dişiye çıkmasını hem de dişi deve veya sığırın çiftleşme isteyip erkeği aramasını içerir. Bu iki katılımcı yönü aynı üreme sahnesinde açıkça ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"erkek hayvanın dişiye çiftleşmek için çıkması"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"çiftleşme için ayrılmış damızlık erkek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"dişi deve veya sığırın çiftleşmek istemesi"}],"lexicalization_note":"Tanım erkek hayvanın çiftleşme eylemiyle dişinin çiftleşme isteğini ayırır; belirli hayvanlı kalıplar yalın anlama yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; en yakın çiftleşme komşusu katılımcı ve istek sınırlarını açıklamak için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal erkek eylemiyle dişinin isteğini aynı yapı içinde verir; komşu dal özellikle erkek devenin gelişi ve dişi ya da sahibi tarafından çağrılması çevresindedir.","focus_only":"Damızlık erkeğin niteliğini ve dişi deve veya sığırın kendi çiftleşme isteğini birlikte kapsar.","gloss":"erkek devenin dişiyle çiftleşmesi","neighbor_only":"Dişinin yanı sıra sahibinin de erkek hayvanı çiftleşmeye çağırmasını kapsayabilir.","neighbor_ref":"root_000906/B011","relation_type":"near_synonym","shared_zone":"Her iki dalda da erkek hayvanın dişiye üreme amacıyla yönelmesi ve çiftleşmesi vardır."}],"source_phrase_ar":"القريع الفحل لأنه يقرع الناقة (maqayis)؛ القريع من الإبل الفحل (ayn)؛ قرع الفحل الناقة يقرعها قرعا وقراعا (sihah)؛ استقرعت الناقة إذا اشتهت الضراب (tahdhib)","source_summary":"Kaynaklar damızlık erkeğin dişiyle çiftleşmesini ortak çekirdek sayar ve dişinin çiftleşme isteğini aynı üreme sahnesine bağlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه قرع الفحل الناقة، والقريع من الإبل، واستقرعت الناقة أو البقرة إذا طلبت الفحل، وإعطاء الفحل ليضرب الإناث.","what_is_not_ar":"لا يدخل فيه القرعة في القسمة ولا القريع بمعنى السيد إلا إذا نصت العبارة على الفحل أو الضراب."},"support_links":[]},{"boundary":"Dal kura yoluyla seçim veya paylaştırmadır; savaşma, sıradan pay sahibi olma ve en iyi malı seçme anlamlarından ayrıdır.","branch_kind":"bare","branch_ref":"root_001219/B004","candidate_links":[{"candidate_id":"cand_86f68c487f781750ef27","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"kura çekmek ve kurayla paylaştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok kişi veya ortak, seçim ya da bölüşüm sonucunu tarafsız biçimde belirlemek için kura çeker."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir seçim, sıra veya paylaşımın kura sonucuyla belirlendiği bütün genel bağlamlarda kullanılabilir.","boundary_detail":"Dal kura yoluyla seçim veya paylaştırmadır; savaşma, sıradan pay sahibi olma ve en iyi malı seçme anlamlarından ayrıdır.","branch_image_ar":"اقتراع ومساهمة","concept_gloss":"kura çekmek ve kurayla paylaştırmak","contextual_glosses":[{"applicability":"Birden çok kişinin seçim, sıra veya paylaşım için aynı kuraya katıldığı cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcılar arasındaki kura işlemini ve sonucu belirleme işlevini korur."},"facet_ids":["F001"],"text":"aralarında kura çekmek","usage_role":"general"}],"definition":"Bir seçim veya paylaşım sonucunu belirlemek için kişiler arasında kura düzenlemek, kuraya katılmak ve sonucu kuraya göre belirlemektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok kişi veya ortak, seçim ya da bölüşüm sonucunu tarafsız biçimde belirlemek için kura çeker."}],"identity_rationale":"Kaynak ifadesi, kişiler veya ortaklar arasında kura düzenlenmesini, kuraya katılmayı ve bir şeyi kura sonucuna göre bölüşmeyi açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kura veya kurada çıkan pay"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"aralarında kura çektirmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"kura çekerek seçmek veya paylaştırmak"}],"lexicalization_note":"Tanım yalın kura çekme ve kurayla paylaştırma alanını kapsar; belirli bir araç veya tarihsel uygulama zorunlu sayılmaz.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; araçtan bağımsız kura ile okla kura arasındaki sınırı gösteren en yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel kura işlemini anlatır; komşu dal aynı işlemi özellikle ok kullanımı ve kurada çıkan pay çevresinde somutlaştırır.","focus_only":"Kura yöntemini belirli bir fiziksel araca bağlamadan kişiler veya ortaklar arasında uygular.","gloss":"oklarla kura çekmek","neighbor_only":"Özellikle oklarla yapılan kura çekimini ve kuradan çıkan payı öne çıkarır.","neighbor_ref":"root_000754/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da seçim veya paylaşım sonucu katılımcılar arasında kura ile belirlenir."}],"source_phrase_ar":"الإقراع والمقارعة هي المساهمة (maqayis)؛ أقرع القوم وتقارعوا بينهم والاسم القرعة (ayn)؛ أقرعت بينهم من القرعة واقترعوا وتقارعوا بمعنى (sihah)؛ أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه (tahdhib)","source_summary":"Kaynaklar kişiler ve ortaklar arasında kura düzenleme, karşılıklı kura çekme ve bölüşümü kura sonucuna bağlama konusunda birleşir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الإقراع بين القوم أو الشركاء، والقرعة، والاقتراع، والمقارعة إذا نصت على المساهمة والقسمة أو خروج السهم.","what_is_not_ar":"لا يدخل فيه مقارعة الحرب، ولا الاختيار بمعنى خيار المال إلا بقرينة القرعة أو الاقتراع."},"support_links":["sup_ba2139012ee8286b2d08"]},{"boundary":"Dal sarsıcı büyük felaket ve dünyanın sonundaki hesap günüyle sınırlıdır; koruyucu okuma kullanımı yalnızca kendi sözcük biriminde gösterilir.","branch_kind":"bare","branch_ref":"root_001219/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"sarsıcı büyük felaket veya dünyanın sonundaki hesap günü","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun başına büyük ve sarsıcı sonuçlarla inen ağır bir felaket veya yıkım anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dünyanın sonundaki büyük hesap günü, bu sarsıcı felaket kavramının özel ve yüce ölçekli uygulamasıdır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem insanlara inen büyük yıkımı hem de bunun özel kullanımı olan son hesap gününü kapsayan açıklayıcı karşılıktır.","boundary_detail":"Dal sarsıcı büyük felaket ve dünyanın sonundaki hesap günüyle sınırlıdır; koruyucu okuma kullanımı yalnızca kendi sözcük biriminde gösterilir.","branch_image_ar":"قارعة نازلة تضرب","concept_gloss":"sarsıcı büyük felaket veya dünyanın sonundaki hesap günü","contextual_glosses":[{"applicability":"Bir topluluğun ağır ve yıkıcı bir olayla karşılaştığı dünyevi bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dünyanın sonundaki hesap gününe özgü kullanımı dışarıda bırakır.","preserves":"İnsanlara inen sarsıcı ve yıkıcı felaket anlamını korur."},"facet_ids":["F001"],"text":"başlarına büyük bir felaket geldi","usage_role":"contextual"},{"applicability":"Sözcük, bütün insanlığı bekleyen son günün adı olarak kullanıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dünyevi ağır felaketler için kullanılan genel çekirdeği dışarıda bırakır.","preserves":"Son hesap gününe özgü yüce ölçekli kullanımı korur."},"facet_ids":["F002"],"text":"dünyanın sonundaki hesap günü","usage_role":"explanatory"}],"definition":"İnsanların başına inen, onları sarsan ve büyük yıkım getiren ağır bir felakettir. Aynı ad dünyanın sonundaki hesap günü için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun başına büyük ve sarsıcı sonuçlarla inen ağır bir felaket veya yıkım anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Dünyanın sonundaki büyük hesap günü, bu sarsıcı felaket kavramının özel ve yüce ölçekli uygulamasıdır."}],"identity_rationale":"Yetkili kaynak ifadesi ağır felaketi, insanın başına inen büyük yıkımı ve dünyanın sonundaki hesap gününü destekler. Koruyucu kutsal metin bölümleri yalnızca ayrı bir sözcük biriminde tanıklanmıştır ve dalın kurucu anlamına alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"büyük felaket veya dünyanın sonundaki hesap günü"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Kuran'dan korkuya karşı okunan koruyucu bölümler"}],"lexicalization_note":"Tanım yalın felaket anlamını ve onun dünyanın sonundaki hesap gününe uygulanmasını verir; sözcük birimi ayrıntıları çekirdeğe eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ağır felaket ile savaş ve zaman sıkıntısı arasındaki sınırı en iyi gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal felaketin kendisini ve son hesap gününü adlandırır; komşu dal savaş ve zaman içinde yaşanan şiddetli sıkıntılar alanına yayılır.","focus_only":"Genel büyük felaketi ve dünyanın sonundaki hesap gününü adlandırır.","gloss":"savaşta ve zamanda inen sıkıntı","neighbor_only":"Özellikle savaşın şiddetini, zamanın getirdiği sıkıntıları ve keskin kılıcı kapsar.","neighbor_ref":"root_001295/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da insanların üzerine inen ağır, korkutucu ve yıkıcı olayları anlatabilir."}],"source_phrase_ar":"القارعة الشديدة من شدائد الدهر والقارعة القيامة (maqayis)؛ القارعة القيامة والقارعة الشدة (ayn)؛ القارعة الشديدة من شدائد الدهر وهي الداهية (sihah)؛ النازلة الشديدة تنزل عليهم بأمر عظيم (tahdhib)؛ القارعة ما القارعة (mufradat)","source_summary":"Kaynaklar sarsıcı büyük felaket anlamında birleşir ve aynı sözcüğü dünyanın sonundaki hesap günü için de kullanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القارعة من شدائد الدهر، والقيامة، والنازلة الشديدة، وقوارع القرآن التي تقرع الجن أو الشيطان أو تدفع الفزع.","what_is_not_ar":"لا يدخل فيه كل ضرب حسي ولا القرعة، إلا إذا صارت الشدة أو النازلة هي الصورة المقصودة."},"support_links":[]},{"boundary":"Dal söz dinleyip geri dönme ile başkasını durdurma veya kınama yönlerini ayırır; pişmanlık hareketi yalnızca kendi kalıbına aittir.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B006","candidate_links":[{"candidate_id":"cand_9617eb159c6f29f6f4d7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"öğütle yola gelmek; durdurmak veya azarlamak","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi öğüdü kabul eder, yanlış tutumundan vazgeçer ve doğru olana geri döner."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi başka birini yapmakta olduğu şeyden alıkoyar ve onu durdurur."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sertçe azarlama ve kınama, muhatabı yanlış davranıştan caydırmaya yönelir."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öğüt alan kişinin davranış değişikliğini ve başkasını caydıran kişinin eylemini birlikte kapsayan açıklayıcı karşılıktır.","boundary_detail":"Dal söz dinleyip geri dönme ile başkasını durdurma veya kınama yönlerini ayırır; pişmanlık hareketi yalnızca kendi kalıbına aittir.","branch_image_ar":"ردع يقرع السامع","concept_gloss":"öğütle yola gelmek; durdurmak veya azarlamak","contextual_glosses":[{"applicability":"Kişinin bir uyarı veya öğüt üzerine kendi yanlış davranışını bıraktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını durdurma ve sertçe kınama yönlerini dışarıda bırakır.","preserves":"Öğüdü kabul etme ve davranıştan geri dönme yönünü korur."},"facet_ids":["F001"],"text":"söz dinleyip vazgeçmek","usage_role":"contextual"},{"applicability":"Bir kişinin başka birini sert sözlerle yanlış davranıştan alıkoyduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öğüt alan kişinin kendi isteğiyle doğruya dönmesi yönünü dışarıda bırakır.","preserves":"Sertçe kınama yoluyla başkasını durdurma yönünü korur."},"facet_ids":["F002","F003"],"text":"azarlayıp caydırmak","usage_role":"contextual"}],"definition":"Bir uyarı veya öğüt karşısında söz dinleyip yanlışından vazgeçmek ve doğru olana dönmektir. Ettirgen yönde birini durdurmak ya da sertçe kınayarak caydırmak anlamına gelir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi öğüdü kabul eder, yanlış tutumundan vazgeçer ve doğru olana geri döner."},{"facet_id":"F002","role":"extension","statement":"Bir kişi başka birini yapmakta olduğu şeyden alıkoyar ve onu durdurur."},{"facet_id":"F003","role":"associated_use","statement":"Sertçe azarlama ve kınama, muhatabı yanlış davranıştan caydırmaya yönelir."}],"identity_rationale":"Yetkili kaynak ifadesi öğüt kabul etmeyi, doğruya dönmeyi, birini durdurmayı ve sertçe kınamayı destekler. Pişmanlıkla dişe vurma hareketi yalnızca ayrı bir kalıpta tanıklanır ve dalın kurucu anlamı yapılmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"öğüt dinleyip vazgeçmek"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"doğru olana geri dönüp boyun eğmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"alıkoymak ve caydırmak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"sertçe azarlama ve kınama"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"pişmanlıktan dişine vurmak"}],"lexicalization_note":"Tanım yalın davranış değişikliği ve ettirgen durdurma yönlerini ayırır; pişmanlık bildiren diş kalıbı genelleştirilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; seçilen komşu, kişinin geri dönüşü ile dışarıdan durdurulması arasındaki katılımcı farkını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hem kişinin söz dinlemesini hem de bir başkasının onu durdurup kınamasını kapsar; komşu dal kişinin kötü davranıştan kendi geri çekilişine odaklanır.","focus_only":"Öğüt kabulünü, doğruya dönüşü, başkasını durdurmayı ve sertçe kınamayı birlikte kapsar.","gloss":"yanlıştan geri durmak","neighbor_only":"Özellikle çirkin veya bilgisizce davranıştan kişinin kendini çekmesini ve iyi bir dönüş yapmasını anlatır.","neighbor_ref":"root_000574/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da yanlış bir davranıştan vazgeçme ve daha doğru bir tutuma dönme bulunur."}],"source_phrase_ar":"رجل قرع إذا كان يقبل مشورة المشير (maqayis)؛ أقرعت إلى الحق إقراعا رجعت (maqayis)؛ فلان لا يقرع إقراعا إذا كان لا يقبل المشورة والنصيحة (sihah)؛ التقريع التعنيف (sihah)؛ فلان لا يقرع أي لا يرتدع (tahdhib)؛ أقرعته إذا كففته (tahdhib)","source_summary":"Kaynaklar öğütle yola gelme ve doğruya dönme yönünü, başkasını durdurma ve sertçe kınama yönleriyle birlikte verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه قبول المشورة والارتداع، الرجوع إلى الحق، الكف، التقريع بمعنى التعنيف، وقرع السن ندما.","what_is_not_ar":"لا يدخل فيه الضرب الحسي الخالص ولا القارعة إلا إذا ظهر معنى الوعظ أو الكف أو الرجوع."},"support_links":["sup_ea1faabc41f65db60642"]},{"boundary":"Dal kişi, mal veya yer içindeki seçkin ve en iyi olana ilişkindir; rastgele kura sonucu ve damızlık eylemi bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B007","candidate_links":[{"candidate_id":"cand_86f68c487f781750ef27","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"seçilmiş önder veya bir şeyin en iyi bölümü; en iyisini vermek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi seçilmiş, üstün ve işlerde kendisine güvenilen önder olarak öne çıkar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir mal topluluğunun en iyi ve en değerli bölümü seçkin parça olarak adlandırılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir evin sıcak veya soğuk bakımından en elverişli yeri, yerin en iyi bölümü sayılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kişiye malın sıradan bir bölümünü değil, en iyi ve seçkin bölümünü vermek anlatılır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişide seçkinlik, mal veya yerde en iyi bölüm ve bunu başkasına verme yönlerinin tamamını açıklamak için kullanılır.","boundary_detail":"Dal kişi, mal veya yer içindeki seçkin ve en iyi olana ilişkindir; rastgele kura sonucu ve damızlık eylemi bu sınıra girmez.","branch_image_ar":"مقروع مختار وخيار","concept_gloss":"seçilmiş önder veya bir şeyin en iyi bölümü; en iyisini vermek","contextual_glosses":[{"applicability":"Bir toplulukta seçkinliği ve kendisine güvenilmesi nedeniyle öne çıkan kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Malın veya yerin en iyi bölümü ile en iyisini verme yönlerini dışarıda bırakır.","preserves":"Seçilmiş ve güvenilen kişi yönünü korur."},"facet_ids":["F001"],"text":"güvenilen önder","usage_role":"contextual"},{"applicability":"Bir mal topluluğu içinden nitelikçe üstün bölümün kastedildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önder, evin en iyi yeri ve başkasına verme yönlerini dışarıda bırakır.","preserves":"Mal içindeki seçkin ve en değerli bölüm yönünü korur."},"facet_ids":["F002"],"text":"malın en iyi kısmı","usage_role":"contextual"}],"definition":"Bir topluluk içinde seçilmiş, güvenilen önderi veya bir malın ya da yerin en iyi bölümünü belirtir. Ettirgen yapıda birine sahip olunan malın en iyisini vermeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi seçilmiş, üstün ve işlerde kendisine güvenilen önder olarak öne çıkar."},{"facet_id":"F002","role":"extension","statement":"Bir mal topluluğunun en iyi ve en değerli bölümü seçkin parça olarak adlandırılır."},{"facet_id":"F003","role":"specialization","statement":"Bir evin sıcak veya soğuk bakımından en elverişli yeri, yerin en iyi bölümü sayılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir kişiye malın sıradan bir bölümünü değil, en iyi ve seçkin bölümünü vermek anlatılır."}],"identity_rationale":"Kaynak ifadesi güvenilen önderi veya seçilmiş kişiyi, malın en iyi bölümünü, evin en iyi yerini ve birine malın en iyisini vermeyi birlikte destekler. Ortak eksen seçilmişlik ve üstün niteliktir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"güvenilen önder veya başkan"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"seçilmiş kişi veya önder"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"malın en iyi ve seçkin bölümü"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"evin sıcak veya soğukta en iyi yeri"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"ona malının en iyi bölümünü vermek"}],"lexicalization_note":"Tanım seçkin kişi ile mal veya yerin en iyi kısmını ayırır; en iyi malı verme anlamı yalnızca ilgili yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel seçme alanı ile bu dalın seçkin kişi ve en iyi bölüm odağını ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal seçilmiş önder ve somut olarak en iyi bölüm üzerinde yoğunlaşır; komşu dal seçme ve yeğleme işlemini daha genel biçimde anlatır.","focus_only":"Güvenilen önderi, mal veya yerin en iyi bölümünü ve en iyi malı verme eylemini kapsar.","gloss":"seçmek ve seçkin kılmak","neighbor_only":"Seçme eylemini, seçilmiş seçkin kişiyi veya şeyi ve birini başka birine yeğlemeyi genel olarak kapsar.","neighbor_ref":"root_000873/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir kişi veya şey başkaları arasından üstün görülerek seçilir."}],"source_phrase_ar":"القريع وهو السيد سمى بذلك لأنه يعول عليه في الأمور (maqayis)؛ أقرع فلان فلانا أعطاه خير ماله وخيار المال قرعته (maqayis)؛ القريعة وهو خير بيت في الربع (maqayis)؛ المقروع المختار للفحلة والمقروع السيد (sihah)؛ قريعة البيت خير موضع فيه (tahdhib)؛ القريعة والقرعة خيار المال (tahdhib)","source_summary":"Kaynaklar seçilmiş ve güvenilir kişi ile malın veya yerin en iyi bölümü anlamlarını, üstün olanın ayrılması ortak ekseninde birleştirir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القريع السيد أو الرئيس، المقروع المختار، قرعة أو قريعة المال أي خياره، قريعة البيت خير موضعه، وما يعطى من خيار المال.","what_is_not_ar":"لا يدخل فيه القرعة العشوائية في القسمة إلا عند ذكر الاقتراع، ولا الفحل إلا إذا صار المقصود ضرابه."},"support_links":["sup_ba2139012ee8286b2d08"]},{"boundary":"Dal örtünün kaybı ile yerin insan, hayvan veya bitkiden yoksun kalmasına dayanır; sözcük birimlerine özgü ek örnekler genelleştirilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B008","candidate_links":[{"candidate_id":"cand_9b031ae7b2be569da6f3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"saç ya da örtü kaybı; bir yerin boş veya bitkisiz kalması","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başta bulunan saç, bir hastalık veya bozukluk sonucunda dökülür ve baş çıplak kalır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yavru hayvan benzer bir deri veya tüy kaybı hastalığına tutulur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Avlu veya hayvan barınağı sakinlerinden boşalır; arazi de bitkisiz ya da otlatılarak çıplak kalır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Başın veya hayvanın örtü kaybını ve yerin insan, hayvan ya da bitkiden yoksun kalmasını birlikte açıklar.","boundary_detail":"Dal örtünün kaybı ile yerin insan, hayvan veya bitkiden yoksun kalmasına dayanır; sözcük birimlerine özgü ek örnekler genelleştirilmez.","branch_image_ar":"قرع وانكشاف وخلو","concept_gloss":"saç ya da örtü kaybı; bir yerin boş veya bitkisiz kalması","contextual_glosses":[{"applicability":"Bir insanın başındaki saçın hastalık veya başka bir bozukluk nedeniyle kaybolduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hayvandaki hastalığı ve yerin boş ya da bitkisiz kalmasını dışarıda bırakır.","preserves":"Hastalık sonucu başın saç örtüsünü kaybetmesi yönünü korur."},"facet_ids":["F001"],"text":"hastalıktan saçı dökülmek","usage_role":"contextual"},{"applicability":"Bir avlu, barınak veya arazinin sakinlerinden ya da bitki örtüsünden yoksun kalması için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsan başındaki ve hayvan bedenindeki hastalığa bağlı örtü kaybını dışarıda bırakır.","preserves":"Mekanın doluluğunu veya doğal örtüsünü kaybetmesi yönünü korur."},"facet_ids":["F003"],"text":"boş ve çıplak kalmak","usage_role":"contextual"}],"definition":"Başın hastalık yüzünden saçını, bir hayvanın da tüy veya deri örtüsünü kaybetmesidir. Genişlemiş kullanımda bir avlu ya da barınağın boşalmasını ve toprağın bitki örtüsünden yoksun kalmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başta bulunan saç, bir hastalık veya bozukluk sonucunda dökülür ve baş çıplak kalır."},{"facet_id":"F002","role":"specialization","statement":"Yavru hayvan benzer bir deri veya tüy kaybı hastalığına tutulur."},{"facet_id":"F003","role":"extension","statement":"Avlu veya hayvan barınağı sakinlerinden boşalır; arazi de bitkisiz ya da otlatılarak çıplak kalır."}],"identity_rationale":"Yetkili kaynak ifadesi hastalık nedeniyle saç veya tüy kaybını, bir avlu ya da hayvan barınağının boşalmasını ve arazinin bitkisiz kalmasını destekler. Açıkta kalan beden bölgesi ve tüysüz yılan yalnızca ayrı sözcük birimlerinde tanıklanır ve dal çekirdeğine alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir hastalık yüzünden saçların dökülmesi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"saçı hastalık nedeniyle dökülmüş; kel"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"deri veya tüy hastalığına tutulmuş yavru deve"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"avlu veya hayvan barınağının boş kalması"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bitki yetiştirmeyen veya otlatılıp çıplak kalmış arazi"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"açıkta kalan cinsel bölge"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"başında tüy bulunmayan iri yılan"}],"lexicalization_note":"Tanım saç veya tüy kaybı ile yerin boş ya da bitkisiz kalmasını ayırır; özel beden ve hayvan kalıpları kendi sınırında tutulur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel örtü kaybı komşusu, hastalık ve mekan boşalması sınırlarını en yararlı biçimde görünür kılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal hastalığa bağlı kellik ile boşalma anlamlarını birleştirir; komşu dal örtünün herhangi bir yolla kaybolmasını daha genel olarak anlatır.","focus_only":"Hastalığa bağlı saç veya tüy kaybını ve avlu ya da barınağın sakinlerinden boşalmasını kapsar.","gloss":"örtüsünden sıyrılmak","neighbor_only":"Dal, ağaç, kum, beden ve hayvanın üzerini kaplayan şeylerden genel olarak sıyrılmasını kapsar.","neighbor_ref":"root_001413/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir bedenin, bitkinin veya yerin kendisini örten şeyden yoksun kalması vardır."}],"source_phrase_ar":"مما شذ عن هذا الأصل القرع وفصيل مقرع والقرع أيضا ذهاب الشعر من الرأس (maqayis)؛ القرع ذهاب شعر الرأس من داء (ayn)؛ الأقرع الذي ذهب شعر رأسه من آفة (sihah)؛ قرع الفناء إذا خلا من الغاشية (sihah)؛ أرض قرعة لا تنبت شيئا (tahdhib)؛ أصبحت الرياض قرعا قد جردتها المواشي (tahdhib)","source_summary":"Kaynaklar saç kaybını temel görünüm olarak verir; boş avlu, hayvansız barınak ve bitkisiz araziyi örtü veya doluluk kaybıyla ilişkilendirir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه ذهاب شعر الرأس، الفصيل المقرع وداء القرع، قلة الأهل أو الغاشية، خلو المراح أو الفناء، الأرض أو الرياض المجردة، والسوأة القرعاء المنكشفة.","what_is_not_ar":"لا يدخل فيه القرع المأكول ولا مجرد الصلابة إلا إذا دل النص على الخلو أو التجرد."},"support_links":["sup_f769668f935b8828e200"]},{"boundary":"Dal bitkinin kendisine değil yenebilir meyvesine ilişkindir; saç kaybı, yakı aracı ve başka eş sesli anlamlar dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001219/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"kabak meyvesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kabak türü bitkinin meyvesi ve bu meyvenin tek bir tanesi adlandırılır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kabak türü bitkinin meyvesinin genel adı veya tek bir meyve tanesi için kullanılır.","boundary_detail":"Dal bitkinin kendisine değil yenebilir meyvesine ilişkindir; saç kaybı, yakı aracı ve başka eş sesli anlamlar dışarıda kalır.","branch_image_ar":"قرع اليقطين","concept_gloss":"kabak meyvesi","contextual_glosses":[{"applicability":"Sayılan tek bir meyve tanesinin kastedildiği doğal cümle bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Meyve türünün toplu veya sayılamayan genel ad kullanımını dışarıda bırakır.","preserves":"Tek bir kabak meyvesi tanesini korur."},"facet_ids":["F001"],"text":"bir kabak","usage_role":"contextual"}],"definition":"Kabak türü bitkinin meyvesidir; tek bir meyve tanesini de belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kabak türü bitkinin meyvesi ve bu meyvenin tek bir tanesi adlandırılır."}],"identity_rationale":"Kaynak ifadesi doğrudan kabakgillerden bitkinin meyvesini ve tek bir meyve tanesini belirtir. Geçici dal açıklaması bu dar nesne anlamıyla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"kabak meyvesi"}],"lexicalization_note":"Tanım yalın meyve adını verir ve onu bitkinin gövde yapısına, ürüne ilişkin genel bir anlama veya başka kalıplara genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; bitki ile onun meyvesi arasındaki temel nesne farkını gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal bitkinin meyvesidir; komşu dal ise meyveyi taşıyan, yere yayılan gövdesiz bitkiyi anlatır.","focus_only":"Bitkinin taşıdığı yenebilir meyveyi ve tek bir meyve tanesini adlandırır.","gloss":"yayılan kabak bitkisi","neighbor_only":"Yere yayılan, belirgin gövdesi olmayan bitkinin kendisini ve büyüme biçimini adlandırır.","neighbor_ref":"root_001243/B010","relation_type":"near_neighbor","shared_zone":"Her iki dal da aynı bitki alanına ve kabak türlerine ilişkindir."}],"source_phrase_ar":"القرع حمل اليقطين الواحدة قرعة (ayn)؛ القرع حمل اليقطين الواحدة قرعة (sihah)؛ القرع حمل اليقطين (tahdhib)","source_summary":"Kaynaklar anlamı kabak türü bitkinin meyvesi ve onun tek bir tanesi olarak ortak biçimde verir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه القرع بمعنى حمل اليقطين والواحدة قرعة.","what_is_not_ar":"لا يدخل فيه القرع بمعنى داء الفصيل أو ذهاب الشعر، ولا قرع الميسم والمكواة."},"support_links":[]},{"boundary":"Dal yolun veya evin açık alanına ilişkindir; büyük felaket, evin en iyi iç yeri ve soyut yol yöntemi anlamlarına genişletilmez.","branch_kind":"bare","branch_ref":"root_001219/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"yolun açık üst kesimi veya evin önü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yolun açık, görünür, üstte veya gelip geçilen bölümü adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Evin önündeki açık alan veya avlu, aynı mekansal görünümle adlandırılır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolun görünür ve kullanılan bölümüyle evin önündeki açık alanı birlikte karşılayan açıklayıcı gloss olarak uygundur.","boundary_detail":"Dal yolun veya evin açık alanına ilişkindir; büyük felaket, evin en iyi iç yeri ve soyut yol yöntemi anlamlarına genişletilmez.","branch_image_ar":"قارعة الطريق والدار","concept_gloss":"yolun açık üst kesimi veya evin önü","contextual_glosses":[{"applicability":"Sözcük bir evin önünde veya çevresinde bulunan açık alanı belirttiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yolun açık, üst veya gelip geçilen bölümü anlamını dışarıda bırakır.","preserves":"Eve bağlı açık alan ve avlu yönünü korur."},"facet_ids":["F002"],"text":"evin önündeki açık alan","usage_role":"contextual"}],"definition":"Yolun açık, üstte veya gelip geçilen kesimi ile evin önündeki açık alanı ve avluyu belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yolun açık, görünür, üstte veya gelip geçilen bölümü adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Evin önündeki açık alan veya avlu, aynı mekansal görünümle adlandırılır."}],"identity_rationale":"Kaynak ifadesi yolun açık veya üst kesimini, evin de önündeki açık alanı belirtir. Dal açıklaması görünür ve gelip geçilen mekan ortaklığını doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"yolun açık veya üst kesimi; evin önündeki açık alan"}],"lexicalization_note":"Tanım yalın mekan adını verir; yol ve ev uygulamalarını korur ama bunlardan soyut yöntem veya hareket anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; ev önü ortaklığını ve bu dalın ek yol anlamını en iyi açıklayan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ev önü anlamını yolun açık kesimiyle birleştirir; komşu dal yalnızca eve bağlı avlu ve çevresindeki geniş alanı anlatır.","focus_only":"Yolun açık veya üst kesimini de evin önündeki alanla aynı dalda kapsar.","gloss":"evin avlusu ve önü","neighbor_only":"Eve bitişik avluyu, evin yanlarına uzanan alanı ve ön taraftaki genişliği özellikle kapsar.","neighbor_ref":"root_001181/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da evin önünde veya çevresinde bulunan açık alanı adlandırabilir."}],"source_phrase_ar":"قارعة الدار ساحتها وقارعة الطريق أعلاه (sihah)؛ قرعاء الدار ساحتها (tahdhib)؛ قارعة الطريق ساحتها وقارعة الطريق أعلاه (tahdhib)","source_summary":"Kaynaklar yolun açık ya da üst kesimi ile evin önündeki açık alanı aynı mekan adı altında birleştirir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه قارعة الطريق أعلاه أو ساحته، وقارعة الدار أو قرعاء الدار ساحتها، وما يدل على الموضع الظاهر المطروق.","what_is_not_ar":"لا يدخل فيه القارعة بمعنى القيامة أو المصيبة، ولا القريعة بمعنى خير موضع البيت."},"support_links":[]},{"boundary":"Dal sertlik ve yüzeyin ovma ya da soyma ile düzleşmesiyle sınırlıdır; saç kaybı veya mekanın boşalması anlamları buna katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001219/B011","candidate_links":[{"candidate_id":"cand_9b031ae7b2be569da6f3","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"sert ve dayanıklı; kazınıp pürüzsüzleştirilmiş","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kalkan veya yer gibi bir nesne sert, sağlam ve dış etkiye dirençli olarak nitelenir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kap çakılla ovularak veya dal kabuğundan soyularak yüzeyi düz ve örtüsüz hale getirilir."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem nesnenin yapısal sertliğini hem de ovma veya soyma sonucu ortaya çıkan düz yüzeyi açıklamak için kullanılır.","boundary_detail":"Dal sertlik ve yüzeyin ovma ya da soyma ile düzleşmesiyle sınırlıdır; saç kaybı veya mekanın boşalması anlamları buna katılmaz.","branch_image_ar":"قراع صلب ممسوح","concept_gloss":"sert ve dayanıklı; kazınıp pürüzsüzleştirilmiş","contextual_glosses":[{"applicability":"Bir kalkanın, yerin veya başka bir nesnenin dirençli yapısı öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ovma veya soyma yoluyla yüzeyin düzleştirilmesi yönünü dışarıda bırakır.","preserves":"Nesnenin yapısal sertlik ve dayanıklılık yönünü korur."},"facet_ids":["F001"],"text":"sert ve sağlam","usage_role":"contextual"},{"applicability":"Bir kabın çakılla ovulması veya bir dalın kabuğunun soyulması sonucunda yüzey değiştiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesne veya yerin kendi yapısından gelen genel sertlik anlamını dışarıda bırakır.","preserves":"Yüzeyin sürtme veya soyma yoluyla düzleşmesi yönünü korur."},"facet_ids":["F002"],"text":"ovulup düzleştirilmiş","usage_role":"contextual"}],"definition":"Bir nesnenin veya yerin sert, sağlam ve dirençli olmasıdır. Ayrı fakat ilişkili kullanımda bir kabın ovularak ya da bir dalın kabuğu soyularak yüzeyinin düzleştirilmesini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kalkan veya yer gibi bir nesne sert, sağlam ve dış etkiye dirençli olarak nitelenir."},{"facet_id":"F002","role":"source_variant","statement":"Kap çakılla ovularak veya dal kabuğundan soyularak yüzeyi düz ve örtüsüz hale getirilir."}],"identity_rationale":"Yetkili kaynak ifadesi sert ve dayanıklı nesne veya yeri, ayrıca çakılla ovulmuş kabı destekler. Toynak ve işkembenin sertleşmesi yalnızca ayrı sözcük biriminde tanıklanmıştır; bu nedenle dal tanımı sertlik ile kazınıp düzleşmiş yüzeyi ayırarak kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"sert ve dayanıklı"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"çakılla ovulmuş kap veya kabuğu soyulmuş dal"},{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"sertleşmiş toynak veya işkembe"}],"lexicalization_note":"Tanım yalın sertlik yönüyle ovulmuş veya soyulmuş yüzey yönünü ayırır; toynak ve işkembe kalıbı genel anlama yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel güç ve sağlamlık komşusu bu dalın yüzey işleme yönünü en açık biçimde ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal özellikle sert yüzeyleri ve yüzeyin ovulup düzleşmesini içerir; komşu dal güç ve dayanıklılığı canlılara ve kumaşa kadar genişletir.","focus_only":"Sert nesne veya yere ek olarak ovulmuş ya da soyulmuş düz yüzeyi kapsar.","gloss":"güç ve sağlamlık","neighbor_only":"Güç, kalıcılık, semizlik ve kumaş dayanıklılığı gibi daha geniş nitelik alanlarına yayılır.","neighbor_ref":"root_000973/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir varlığın sert, güçlü ve dış etkilere dayanıklı olmasını anlatır."}],"source_phrase_ar":"القراع الصلب الشديد (sihah)؛ ترس أقرع إذا كان صلبا وهو القراع أيضا (tahdhib)؛ قدح أقرع وهو الذي حك بالحصى (tahdhib)؛ مكان أقرع شديد صلب (tahdhib)","source_summary":"Kaynaklar sertlik ve sağlamlık anlamını verir; ovma veya soyma sonucu yüzeyi düzleşen nesne bu görünümle ilişkilendirilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه القراع أو الأقرع بمعنى الصلب الشديد، الترس القراع، المكان الأقرع، الحافر أو الكرش إذا اشتد أو ذهب خمله، والقدح أو العود إذا حك أو قشر.","what_is_not_ar":"لا يدخل فيه الخلو من الناس أو ذهاب الشعر إلا إذا كانت الصلابة أو الحك هي المقصودة."},"support_links":["sup_f769668f935b8828e200"]},{"boundary":"Dal yiyecek veya hurma koymaya yarayan torba ve kaplarla sınırlıdır; kura, kabak meyvesi ve soyut toplama anlamları buna girmez.","branch_kind":"bare","branch_ref":"root_001219/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","surface_ar":"قَارِعَةُ"}],"gloss":"yiyecek veya hurma konan torba ya da kap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yiyecek veya hurma, taşımaya ve bir arada tutmaya yarayan torba ya da kap içinde toplanır."}}],"root_ar":"ق ر ع","root_id":"root_001219","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yiyeceğin saklandığı veya hurmanın toplandığı torba, tulum ve benzeri kapların tamamı için açıklayıcı karşılıktır.","boundary_detail":"Dal yiyecek veya hurma koymaya yarayan torba ve kaplarla sınırlıdır; kura, kabak meyvesi ve soyut toplama anlamları buna girmez.","branch_image_ar":"وعاء وجمع في مقرع","concept_gloss":"yiyecek veya hurma konan torba ya da kap","contextual_glosses":[{"applicability":"Kap özellikle toplanan hurmaların içine konduğu araç olarak geçtiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka yiyecekler için kullanılan küçük veya geniş torba ve tulumları dışarıda bırakır.","preserves":"Hurma toplama ve ürünü kap içinde biriktirme işlevini korur."},"facet_ids":["F001"],"text":"hurma toplama kabı","usage_role":"contextual"}],"definition":"Yiyecek koymak veya hurma toplamak için kullanılan, küçük ya da geniş olabilen torba, tulum veya benzeri kaptır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yiyecek veya hurma, taşımaya ve bir arada tutmaya yarayan torba ya da kap içinde toplanır."}],"identity_rationale":"Kaynak ifadesi yiyecek konan geniş veya küçük torbayı, hurma toplanan kabı ve tulum benzeri kapları açıkça destekler. Geçici dal açıklaması bu kap ve toplama işlevini doğru biçimde yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"yiyecek koymaya yarayan küçük veya geniş torba"},{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"hurma toplamak için kullanılan kap"}],"lexicalization_note":"Tanım yalın kap adını ve yiyecek toplama işlevini verir; onu kura aracına veya genel yerleştirme eylemine genişletmez.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; taşınabilir çuval komşusu, içerik ve kap türü sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yiyecek ve hurmaya göre işlev kazanır ve farklı kap boylarını kapsar; komşu dal özellikle saman için kullanılan büyük çuvala odaklanır.","focus_only":"Yiyecek koyulan torbayı, hurma toplama kabını ve tulum benzeri kapları kapsar.","gloss":"taşınabilir büyük çuval","neighbor_only":"Özellikle saman taşımaya yarayan büyük ve taşınabilir çuvalı anlatır.","neighbor_ref":"root_001078/B013","relation_type":"near_synonym","shared_zone":"Her iki dalda da ürünleri içine alıp taşımaya yarayan torba veya çuval türü bir kap vardır."}],"source_phrase_ar":"القرعة الجراب الواسع يلقى فيه الطعام (tahdhib)؛ القرعة الجراب الصغير وجمعها قرع (tahdhib)؛ المقرع وعاء يجبى فيه التمر (tahdhib)؛ قرع فلان في مقرعه كله السقاء والزق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Geniş veya küçük yiyecek torbası, hurma toplanan kap ve tulum benzeri kap kullanımları birlikte verilir."}],"source_summary":"Bu dalın anlamı tek bir kaynakta yiyecek veya hurma için kullanılan torba ve kap çeşitleriyle tanıklanır.","sources":["TA"],"what_is_ar":"يدخل فيه القرعة بمعنى الجراب أو الوعاء، والمقرع وعاء يجمع فيه التمر، وما نص على السقاء أو الزق في مقرعه.","what_is_not_ar":"لا يدخل فيه القرعة بمعنى السهم أو الاقتراع، ولا قرع اليقطين."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_aa1a49a2fb7af4b76b4c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:acoustic-impact-surface","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_c0ecae90308725d7a921"],"title":"sound texture reinforces impact without changing meaning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_4024b22cd1ebc60a116d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:compressed-nominative-title","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_c362d91f96b3e19fc6cf"],"title":"standalone nominative title with delayed predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_4cf9688009be6b6d1e97","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:definite-proper-name-launch","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_cc6fd3d135e495196eb7"],"title":"definiteness turns the striker into the named event","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_ded4257f373db5894a95","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:feminine-action-title-pattern","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_3aba9a841320fa79cb46"],"title":"feminine active participle makes an action-title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_db641c0a91e2c6709675","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:narrowed-root-pressure","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_abe6fd19107fe9642e35"],"title":"secondary root branches remain pressure, not local activation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_5aead559e9a4299cb466","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:rare-distribution-and-cross-surah","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_5ed1adb6f3fbd742ead0"],"title":"rare root links 69:4 to the 101:1 title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_f86b0c84ba5e73b6d23d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:striking-calamity-agency","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_fb2e5311047c6767b4f0"],"title":"impact-root makes the event an acting calamity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_8080a0cd02c89332c5a0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:triple-refrain-handoff","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_df11a79e72ab55358749"],"title":"same word becomes a three-beat opening refrain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_95ca233faa2bfcab8cd0","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:variant-exclamatory-case","source_type":"word_analysis","support_ids":["sup_0ebed66d2fd66d71d31e","sup_be4852f8de1b278d33df"],"title":"accusative variant as exclamatory apparatus","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"101:1:1","qac_refs":["101:1:1:1","101:1:1:2"],"status":"accepted"}},{"anchor_refs":["101:1:1"],"branch_refs":[],"candidate_id":"cand_469626d6d58d643f97c3","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001219"],"scope":"focus_ayah","source_local_id":"101:1:1:2","source_type":"qac_morpheme","support_ids":["sup_09bf42a2f1345e2de6ce"],"title":"QAC root occurrence: ق ر ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["101:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:1","branch_refs":["root_001219/B001"],"candidate_id":"cand_70acc7510365cddb374e","commentary_obligation":"review","hft_ref":"hft_31226e6105f6eca80c92","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-impact","source_type":"hft","support_ids":["sup_efb12cfd015bdbe0f87d"],"title":"baseline-impact","trust":"legacy_unbound"},{"anchor_refs":["101:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:1","branch_refs":["root_001219/B002"],"candidate_id":"cand_db086dcddb5daaf9093e","commentary_obligation":"review","hft_ref":"hft_50319873364c0a383775","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-counterstroke","source_type":"hft","support_ids":["sup_a9b5d109afcf62570e4b"],"title":"baseline-counterstroke","trust":"legacy_unbound"},{"anchor_refs":["101:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:1","branch_refs":["root_001219/B006"],"candidate_id":"cand_9617eb159c6f29f6f4d7","commentary_obligation":"review","hft_ref":"hft_9f64b6970a0e861a58ea","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-warning","source_type":"hft","support_ids":["sup_ea1faabc41f65db60642"],"title":"baseline-warning","trust":"legacy_unbound"},{"anchor_refs":["101:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:1","branch_refs":["root_001219/B008","root_001219/B011"],"candidate_id":"cand_9b031ae7b2be569da6f3","commentary_obligation":"review","hft_ref":"hft_11373c7828e8e27f0824","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-stripping","source_type":"hft","support_ids":["sup_f769668f935b8828e200"],"title":"baseline-stripping","trust":"legacy_unbound"},{"anchor_refs":["101:1"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"101:1","branch_refs":["root_001219/B004","root_001219/B007"],"candidate_id":"cand_86f68c487f781750ef27","commentary_obligation":"review","hft_ref":"hft_409937652cf984185235","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-allotment","source_type":"hft","support_ids":["sup_ba2139012ee8286b2d08"],"title":"baseline-allotment","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلْقَارِعَةُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"101:1:1:1","qac_word_ref":"101:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","root_ar":"ق ر ع","surface_ar":"قَارِعَةُ"}],"word_analysis_qac_refs":[["101:1:1:1","101:1:1:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["101:1:1"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلْقَارِعَةُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"101:1:1:1","qac_word_ref":"101:1:1","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَارِعَة","morph_features":"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"101:1:1:2","qac_word_ref":"101:1:1","root_ar":"ق ر ع","surface_ar":"قَارِعَةُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["101:1:1:1","101:1:1:2"]],"word_analysis_refs":["101:1:1"],"word_rows":[{"analysis_record_ref":"101:1:1","analytic_gloss_range_en":"the definite singular eschatological title, locally selecting the striking-calamity sense and presenting the event as an active impact-name with explanation withheld","analytic_root_gloss_range_en":"broad q-r-ʿ range around striking, knocking, severe calamity, checking by warning, drawing lots, stripping bare, and other branch-specific senses; the local proper-name form selects striking calamity while allowing only narrowed pressure from some neighboring branches","qac_refs":["101:1:1:1","101:1:1:2"],"root":{"arabic":"ق ر ع","transliteration":"q-r-ʿ"},"surface":{"arabic":"ٱلْقَارِعَةُ","transliteration":"al-qāriʿa"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":1,"words_total":1,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["101:1"],"branch_refs":["root_001219/B001"],"candidate_id":"cand_70acc7510365cddb374e","evidence_scope":"focus_ayah","hft_ref":"hft_31226e6105f6eca80c92","item_id":"baseline-impact","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-impact","support_id":"sup_efb12cfd015bdbe0f87d"},{"anchor_refs":["101:1"],"branch_refs":["root_001219/B002"],"candidate_id":"cand_db086dcddb5daaf9093e","evidence_scope":"focus_ayah","hft_ref":"hft_50319873364c0a383775","item_id":"baseline-counterstroke","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-counterstroke","support_id":"sup_a9b5d109afcf62570e4b"},{"anchor_refs":["101:1"],"branch_refs":["root_001219/B006"],"candidate_id":"cand_9617eb159c6f29f6f4d7","evidence_scope":"focus_ayah","hft_ref":"hft_9f64b6970a0e861a58ea","item_id":"baseline-warning","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-warning","support_id":"sup_ea1faabc41f65db60642"},{"anchor_refs":["101:1"],"branch_refs":["root_001219/B008","root_001219/B011"],"candidate_id":"cand_9b031ae7b2be569da6f3","evidence_scope":"focus_ayah","hft_ref":"hft_11373c7828e8e27f0824","item_id":"baseline-stripping","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-stripping","support_id":"sup_f769668f935b8828e200"},{"anchor_refs":["101:1"],"branch_refs":["root_001219/B004","root_001219/B007"],"candidate_id":"cand_86f68c487f781750ef27","evidence_scope":"focus_ayah","hft_ref":"hft_409937652cf984185235","item_id":"baseline-allotment","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-allotment","support_id":"sup_ba2139012ee8286b2d08"}],"diagnostics":[],"lane_counts":{"global":9,"macro":15,"micro":5},"packet_summary":{"ayah_count":11,"focus_ref":"101:1","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000469","furuq_root_norm":"د ر ر","furuq_source_root_norm":"د ر ر","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000473","furuq_root_norm":"د ر ي","furuq_source_root_norm":"د ر ي","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"101:1","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"101:1","lane":"micro","linguistic_source_ref":"101:1","surface_ref":"101:1","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"101:1","target_tokens":[["Çarpan",["101:1:1"]],["felaket",["101:1:1"]]],"text":"Çarpan felaket!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s101-p01-001-011","label":"Whole surah","number":1,"refs":["101:1","101:2","101:3","101:4","101:5","101:6","101:7","101:8","101:9","101:10","101:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"101:1:1:2","source_type":"qac_morpheme","support_id":"sup_09bf42a2f1345e2de6ce","text":"{\"lemma_ar\":\"قَارِعَة\",\"morph_features\":\"STEM|POS:N|LEM:qaAriEap|ROOT:qrE|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"101:1:1:2\",\"qac_word_ref\":\"101:1:1\",\"root_ar\":\"ق ر ع\",\"surface_ar\":\"قَارِعَةُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1","source_type":"word_analysis","support_id":"sup_0ebed66d2fd66d71d31e","text":"{\"gloss_range\":\"the definite singular eschatological title, locally selecting the striking-calamity sense and presenting the event as an active impact-name with explanation withheld\",\"prose\":\"{{ar:ٱلْقَارِعَةُ}} ({{tr:al-qāriʿa}}) opens as a one-word, definite, singular title: the event is not introduced by a preface but placed before the listener as the named strike. Grammatically, the nominative nominal form can stand as a subject-title with its predicate left unsaid, so the first ayah closes on the name before the following questions reopen it (101:2-3). The selected lexical branch is the striking calamity: the root's knock and impact field makes the Day arrive as forceful contact and interrupting summons rather than as a neutral abstract label. The feminine active-participle shape keeps agency inside the noun, making the event the one that strikes while still sounding like a named catastrophic event rather than a personal striker; that action-title pattern also links this opening to other eschatological openings (69:1, 56:1, 80:33, 79:34). Several root-family pressures survive only in narrowed form: rebuke, exposure after stripping, and lot-like decision can describe how the impact confronts, unveils, and settles outcomes, but they do not make every dictionary branch locally active. The recurrence of the same ending across the opening sequence (101:1-3), together with the hard consonant texture and audible article boundary, turns the title into a repeated lexical and phonetic blow. The rare-root distribution also matters: a calamity denied in 69:4 is isolated here as the surah-opening title, while 13:31 and 101:2-3 keep the root concentrated in calamity and title uses. Variant readings add apparatus: the accusative reading tilts the title toward exclamation, and the imāla reading sharpens vowel color, but neither replaces the canonical nominative title.\",\"root_display\":\"{{ar:ق ر ع}} ({{tr:q-r-ʿ}})\",\"root_gloss_range\":\"broad q-r-ʿ range around striking, knocking, severe calamity, checking by warning, drawing lots, stripping bare, and other branch-specific senses; the local proper-name form selects striking calamity while allowing only narrowed pressure from some neighboring branches\",\"surface_display\":\"{{ar:ٱلْقَارِعَةُ}} ({{tr:al-qāriʿa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:feminine-action-title-pattern","source_type":"word_analysis","support_id":"sup_3aba9a841320fa79cb46","text":"{\"blocking_evidence\":null,\"headline\":\"feminine active participle makes an action-title\",\"reader_payoff\":\"The reader notices that the title names the Day through an action-like feminine participle, aligning it with other eschatological openings (69:1, 56:1, 80:33, 79:34).\",\"reason\":\"The morphology is a feminine active participle used as a proper eschatological title; the comparison to other action-like title openings is a distributional payoff, not a new local sense.\",\"representative_source_ids\":[\"QF-731712f5\",\"QI-96c0545f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:rare-distribution-and-cross-surah","source_type":"word_analysis","support_id":"sup_5ed1adb6f3fbd742ead0","text":"{\"blocking_evidence\":null,\"headline\":\"rare root links 69:4 to the 101:1 title\",\"reader_payoff\":\"The reader notices that this rare root is concentrated in calamity and title uses, with the denied object in 69:4 isolated here as a surah-opening title.\",\"reason\":\"Contextual profiles mark the exact root-form as low-occurrence and proper-name/abstract-concept oriented; the CRITICAL rows provide the concrete distributional links to 13:31, 69:4, and 101:2-3.\",\"representative_source_ids\":[\"QI-8c8fc2d8\",\"QI-a60f86cb\",\"QE-aaa7ed3a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:narrowed-root-pressure","source_type":"word_analysis","support_id":"sup_abe6fd19107fe9642e35","text":"{\"blocking_evidence\":null,\"headline\":\"secondary root branches remain pressure, not local activation\",\"reader_payoff\":\"The reader can hear the strike as confronting, exposing, and outcome-settling, while still knowing that the local word selects the striking-calamity branch.\",\"reason\":\"V4 accepts branches for warning, lot-drawing, and stripping, so those images can survive as narrowed pressure; the local proper-name noun does not license the composite claim that all dictionary branches are simultaneously active.\",\"representative_source_ids\":[\"QS-146f866d\",\"QS-3885b384\",\"MI-f759ea7c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:variant-exclamatory-case","source_type":"word_analysis","support_id":"sup_be4852f8de1b278d33df","text":"{\"blocking_evidence\":null,\"headline\":\"accusative variant as exclamatory apparatus\",\"reader_payoff\":\"The reader sees that case variation can expose an exclamatory stance toward the named strike, while the canonical local form remains the nominative title.\",\"reason\":\"The accusative reading helps explain exclamatory force and a suppressed governor, but QAC and attachment evidence for this aligned surface keep the local parse nominative with an omitted predicate.\",\"representative_source_ids\":[\"QG-5ca82111\",\"QF-046518e4\",\"QY-49b7b5de\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:acoustic-impact-surface","source_type":"word_analysis","support_id":"sup_c0ecae90308725d7a921","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture reinforces impact without changing meaning\",\"reader_payoff\":\"The reader hears the word's abruptness, consonant roughness, and recitational variants as acoustic reinforcement of the strike-image.\",\"reason\":\"The one-word ayah and retained article boundary support abrupt sound payoff; the imāla row is narrowed because it changes recitational color without replacing the root or referent.\",\"representative_source_ids\":[\"QP-0284f01d\",\"QP-e3193458\",\"QF-13c82806\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:compressed-nominative-title","source_type":"word_analysis","support_id":"sup_c362d91f96b3e19fc6cf","text":"{\"blocking_evidence\":null,\"headline\":\"standalone nominative title with delayed predicate\",\"reader_payoff\":\"The reader notices that the one-word opening is grammatically compressed: the name stands first, while explanation is withheld for the next questions (101:2-3).\",\"reason\":\"QAC and attachment evidence identify a definite nominative noun functioning as a nominal subject with a strongly licensed omitted predicate; this supports compression and delayed explanation rather than an ordinary completed sentence.\",\"representative_source_ids\":[\"QG-131ccdbe\",\"QG-daa23611\",\"QT-096ca251\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:definite-proper-name-launch","source_type":"word_analysis","support_id":"sup_cc6fd3d135e495196eb7","text":"{\"blocking_evidence\":null,\"headline\":\"definiteness turns the striker into the named event\",\"reader_payoff\":\"The reader notices that the article and singular shape make this a recognized title, not a warning about any possible calamity.\",\"reason\":\"The local word is definite, singular, and tagged as a proper noun; contextual evidence treats the referent as an abstract concept, fitting a title-like named event.\",\"representative_source_ids\":[\"QG-59877561\",\"QF-ac2bdad9\",\"QT-e3d59782\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:triple-refrain-handoff","source_type":"word_analysis","support_id":"sup_df11a79e72ab55358749","text":"{\"blocking_evidence\":null,\"headline\":\"same word becomes a three-beat opening refrain\",\"reader_payoff\":\"The reader notices that the title is not a one-off label; it is handed into the question and meta-question that follow (101:2-3).\",\"reason\":\"Attachment support warns that the one-ayah rendering should be read with the following questions, and the CRITICAL rows give the concrete recurrence across 101:1-3.\",\"representative_source_ids\":[\"QE-16daf72f\",\"QE-4b7a0c4c\",\"QY-54b6131f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"101:1:1:striking-calamity-agency","source_type":"word_analysis","support_id":"sup_fb2e5311047c6767b4f0","text":"{\"blocking_evidence\":null,\"headline\":\"impact-root makes the event an acting calamity\",\"reader_payoff\":\"The reader feels the Day named by what it does: it strikes, knocks, and confronts before any later scene describes it.\",\"reason\":\"V4 includes an accepted striking-calamity branch for this root, and QAC identifies the local form as an active participial proper noun naming the eschatological event.\",\"representative_source_ids\":[\"QS-0e419a8c\",\"QS-37df7dcb\",\"QY-c3b92260\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001219/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001219","role":"Physical striking supplies the event's core action and makes impact, rather than a generic disaster, its naming mechanism.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]}],"changed_reading":{"after":"The title names the impact itself: an arrival that makes realities meet by force.","before":"A bare title for an unspecified calamity."},"confidence":"strong","focus_anchor":"The definite feminine active noun الْقَارِعَةُ names the event through the root ق ر ع.","mechanism":"The unnamed event is apprehended first as contact: one thing strikes another, and the forceful meeting is substantial enough to name the whole event.","model_id":"baseline-impact"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-impact","source_type":"hft","support_id":"sup_efb12cfd015bdbe0f87d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001219/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001219","role":"Meeting blow with blow turns the named event into a reciprocal collision in which prior forces and structures are tested.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]}],"changed_reading":{"after":"The event is an encounter of forces, exposing what can answer, absorb, or fail under the counterstroke.","before":"A force simply descends upon passive objects."},"confidence":"medium","focus_anchor":"The same noun can activate the reciprocal branch of ق ر ع without leaving its audible and kinetic form.","mechanism":"The event may be a collision or contest rather than a unilateral blow: what is struck meets the striker, so the title holds resistance and counterforce.","model_id":"baseline-counterstroke"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-counterstroke","source_type":"hft","support_id":"sup_a9b5d109afcf62570e4b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001219/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001219","role":"A warning that strikes its hearer supplies an auditory-cognitive blow whose function is restraint and possible return.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]}],"changed_reading":{"after":"Its utterance is already an intervention: a striking warning meant to stop and reorient its hearer.","before":"The title only forecasts an external event."},"confidence":"medium","focus_anchor":"The striking noun remains attached to ق ر ع while activating its rebuking and restraining force.","mechanism":"Impact can occur in attention: a hard warning checks motion, arrests complacency, and attempts to turn the hearer before consequences arrive.","model_id":"baseline-warning"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-warning","source_type":"hft","support_id":"sup_ea1faabc41f65db60642","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001219/B008","root_001219/B011"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_001219","role":"Stripping, exposure, and emptiness make the event an uncovering force that deprives things of shelter and concealment.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]},{"branch_id":"B011","mapped_root_id":"root_001219","role":"The hard scraped surface supplies the material remainder exposed once softer coverings have been beaten or removed.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]}],"changed_reading":{"after":"The event strips worlds to their exposed remainder, making hidden condition and structural hardness publicly legible.","before":"The event damages what it hits."},"confidence":"exploratory","focus_anchor":"The focus noun can carry the bare, emptied, or scraped surface branches of its own root.","mechanism":"The strike removes coverings and occupants, leaving what had seemed furnished or protected exposed as a hard, bare remainder.","model_id":"baseline-stripping"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-stripping","source_type":"hft","support_id":"sup_f769668f935b8828e200","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلْقَارِعَةُ","ayah_ref":"101:1"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001219/B004","root_001219/B007"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001219","role":"Casting lots supplies decisive partition and assignment, while leaving open whether the eventual allocation is random or measured.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_001219","role":"The chosen or choice item supplies selection, rank, and reliance as possible outcomes of the event.","root":"ق ر ع","source_ref":"101:1","source_word_indices":["1"]}],"changed_reading":{"after":"The title may also announce a decisive allocation that separates outcomes and reveals what has weight or standing.","before":"The title announces undifferentiated impact."},"confidence":"exploratory","focus_anchor":"The root inventory of الْقَارِعَةُ also contains drawing shares and selecting what is chosen or choice.","mechanism":"The event can function as a decisive sorter: a stroke or draw ends indeterminacy, separates shares, and identifies what will count or be relied upon.","model_id":"baseline-allotment"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-allotment","source_type":"hft","support_id":"sup_ba2139012ee8286b2d08","trust":"legacy_unbound"}]}
</lane_packet_json>
