# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:21**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_21/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:21",
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
{"branch_registry":[{"boundary":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B001","candidate_links":[{"candidate_id":"cand_709e1828426a34c65cee","lane":"micro"},{"candidate_id":"cand_b6f5299d18ffdcc3ba5a","lane":"micro"},{"candidate_id":"cand_b32dc363460b5bca94e4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"yer ve yere bakan alt bölüm","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer küresi anlamını ve ona bağlı alt bölüm yönelimini birlikte özetleyen en kısa doğal karşılıktır.","boundary_detail":"Temel yer anlamı ile yalnız tamlamalarda beliren alt bölüm ve hayvan ayağı anlamları birbirinden ayrılmalıdır.","branch_image_ar":"السفل المقابل للسماء","concept_gloss":"yer ve yere bakan alt bölüm","contextual_glosses":[{"applicability":"Üzerinde yaşanan ve göğün karşısında bulunan yer küresi söz konusu olduğunda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnelerin altı ile hayvan ayağının alt bölümüne bağlı kullanımları dışarıda bırakır.","preserves":"Üzerinde yaşanan aşağı yer ve göğe karşıt konum anlamını korur."},"facet_ids":["F001"],"text":"yeryüzü","usage_role":"contextual"}],"definition":"Göğün karşısında aşağıda bulunan, üzerinde yaşadığımız yer küresini belirtir. Belirli tamlamalarda bir şeyin yere bakan altını ve hayvanın tırnağını ya da ayağının alt bölümünü de anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Göğün karşısında aşağıda bulunan ve üzerinde yaşanan yer küresidir."},{"facet_id":"F002","role":"extension","statement":"Bir şeyin yere bakan alt bölümü, belirli bir tamlama içinde bu adla anılır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanın tırnağı veya ayağının yere değen alt bölümü için kullanılan özel bir tamlama vardır."}],"identity_rationale":"Kaynak ifadesi, göğün karşısında aşağıda bulunan ve üzerinde yaşanan yeri temel anlam olarak verir; nesnelerin yere bakan altı ile hayvan ayağının alt bölümü de buna bağlı kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yer, yeryüzü"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yerler, ülkeler"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir şeyin yere bakan altı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hayvanın tırnağı veya ayaklarının altı"}],"lexicalization_note":"Tanım yalın yer anlamını kapsar; alt bölüm ve hayvan ayağı anlamlarını ise yalnız belirtilen tamlamalara bağlı yan yüzler olarak tutar.","neighbor_coverage_note":"Sağlanan bütün komşu kartları değerlendirildi; yer yüzeyiyle doğrudan karışabilecek en yararlı sınır karşılaştırması yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği aşağıda ve göğün karşısında bulunan yerdir; komşu dal ise yüzeyin genişliği ve düzlüğü ile serilmiş eşya fikrini öne çıkarır.","focus_only":"Göğün karşısındaki yer küresini ve tamlamalardaki alt bölüm anlamlarını kapsar.","gloss":"geniş düz yer veya yaygı","neighbor_only":"Geniş ve düz araziyi, ayrıca serilip yayılan eşyayı anlatır.","neighbor_ref":"root_000116/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da yayılmış bir yüzey olarak yer alanına dokunur."}],"source_phrase_ar":"كل شيء يسفل ويقابل السماء (maqayis)؛ الأرض التي نحن عليها (maqayis)؛ الأرض الجرم المقابل للسماء (mufradat)؛ كل ما سفل فهو أرض (sihah)؛ الأرض حافر الدابة (ayn)؛ أسفل قوائم الدابة (sihah)","source_summary":"Kaynaklar, anlamın merkezinde göğün karşısındaki aşağı yerin bulunduğunu; alt bölüm ve hayvan ayağı kullanımlarının bu mekansal çekirdeğe dayandığını birlikte gösterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض التي نحن عليها؛ كل ما سفل وقابل السماء؛ أسفل الشيء وقوائم الدابة وما يلي الأرض منها","what_is_not_ar":"ليس الزكام ولا الرعدة ولا الدودة ولا البساط"},"support_links":["sup_04213bd4a2b53768737f","sup_128aad8e82588a4803b9","sup_a940d452a99401e00bee"]},{"boundary":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"yumuşak ve verimli toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Oğlak yer bitkisini yer."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın toprak niteliğine dayanan çekirdeğini eksiksiz ve doğal biçimde karşılar.","boundary_detail":"Toprağın niteliği çekirdektir; bitkinin gelişmesi ve oğlağın beslenmesi sonuç ya da ilişkili kullanım olarak kalmalıdır.","branch_image_ar":"الأرض اللينة المنبتة","concept_gloss":"yumuşak ve verimli toprak","contextual_glosses":[{"applicability":"Bitkinin toprağa yerleşerek çoğalması anlatılan bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağın genel niteliğini ve oğlağın bu bitkiyle beslenmesi yüzünü dışarıda bırakır.","preserves":"Bitkinin toprağa yerleşmesi ve gelişerek çoğalması sürecini korur."},"facet_ids":["F002"],"text":"iyice köklenip çoğalmak","usage_role":"contextual"}],"definition":"Belirtilen yapılarda yumuşak, iyi, verimli ve bol bitki yetiştiren toprağı anlatır. Buna bağlı yapılarda bitkinin toprağa iyice yerleşip çoğalması veya biçilebilir olması, köklü fidan ve yer bitkisini yiyen oğlak; ayrı bir kaynak kullanımında ise semiz oğlak ifade edilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprak veya çayırlık yumuşak, verimli ve iyi bitki yetiştirir."},{"facet_id":"F002","role":"extension","statement":"Bitki toprağa iyice yerleşir, çoğalır veya biçilecek olgunluğa ulaşır."},{"facet_id":"F003","role":"associated_use","statement":"Oğlak yer bitkisini yer."},{"facet_id":"F004","role":"source_variant","statement":"Bir kaynakta ilgili niteleme semiz oğlağı belirtir."}],"identity_rationale":"Kaynak ifadesi yumuşak, iyi ve verimli toprağı merkez alır; bitkinin köklenip çoğalması veya biçilecek duruma gelmesi ile oğlağın bu ottan yiyip semirmesi buna bağlı gelişmelerdir.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yumuşak, verimli ve bol bitkili toprak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yumuşak tabanlı geniş çayırlık"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"toprak verimlileşti"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bitki iyice köklendi, çoğaldı veya biçilecek duruma geldi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"toprakta kök salmış fidan"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"oğlak yer bitkisini yedi veya onunla semirdi"}],"lexicalization_note":"Tanım, nitelikli toprak anlamını yalnız kanıtlanan tamlamalara; bitki, fidan ve oğlakla ilgili anlamları da kendi kanıtlanmış yapılarına bağlar.","neighbor_coverage_note":"Bütün adaylar incelendi; verimli toprak çekirdeğine en yakın olup kapsam farkı taşıyan kart seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yumuşaklık ve iyi bitkilenmeyle birlikte belirli bitki ve oğlak yapılarını taşır; komşu dal kolaylık ve hızlı yetişme niteliğine uzanır.","focus_only":"Bitkinin yerleşmesi, biçilebilir olması ve oğlağın bitkiyle beslenmesi gibi bağlı kullanımları vardır.","gloss":"kolay işlenen verimli toprak","neighbor_only":"Kolay işlenen yer ve bitkinin hızlı yetişmesi özelliklerini daha genel biçimde kapsar.","neighbor_ref":"root_000058/B004","relation_type":"near_synonym","shared_zone":"İki dal da verimli, iyi bitki yetiştiren toprağı anlatır."}],"source_phrase_ar":"أرض أريضة لينة طيبة (maqayis;ayn)؛ أرض أريضة أي زكية (sihah)؛ حسنة النبت (mufradat)؛ تأرض النبت إذا أمكن أن يجز (maqayis;sihah)؛ تأرض النبت تمكن على الأرض فكثر (mufradat)؛ تأرض الجدي إذا تناول نبت الأرض (mufradat)؛ جدي أريض أي سمين (sihah)","source_summary":"Birleşik kanıt, verimli ve yumuşak toprağı; bu toprakta gelişen bitkiyi ve bitkiden yararlanan oğlağı aynı üretkenlik ilişkisi içinde toplar.","sources":["MQ","AY","SI","MU"],"what_is_ar":"الأرض الأريضة والروضة الأريضة؛ الأرض الزاكية الحسنة النبت؛ النبات المتأرض إذا تمكن في الأرض وكثر أو أمكن جزه؛ الجدي الأريض إذا تناول نبت الأرض أو سمن","what_is_not_ar":"ليس أسفل الشيء مطلقا ولا الرعدة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_kind":"collocation","branch_ref":"root_000025/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"iyiliğe yatkın ve layık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi iyiliğe yatkın ve ona layıktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kişi hakkında kurulan belirtilmiş yapıda dalın temel niteliğini karşılar.","boundary_detail":"Anlam yalnız verilen kişi ve eylem yapılarında geçerlidir; genel bir kök anlamı veya doğrudan ahlaki iyilik adı değildir.","branch_image_ar":"الخليق بالخير كالأرض الأريضة","concept_gloss":"iyiliğe yatkın ve layık","contextual_glosses":[{"applicability":"Bir topluluk içinden belirli işi yapmaya en uygun kişi seçildiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İyiliğe yatkın ve alçak gönüllü kişi niteliğini dışarıda bırakır.","preserves":"Belirli eyleme başkalarından daha uygun ve layık olma karşılaştırmasını korur."},"facet_ids":["F002"],"text":"bunu yapmaya en uygunları","usage_role":"contextual"}],"definition":"Belirli yapılarda bir kişinin iyiliğe yatkın ve ona layık olmasını anlatır; bir kaynak bu niteliği alçak gönüllülükle birlikte verir. Karşılaştırmalı kullanımda ise bir işi yapmaya başkalarından daha uygun olmayı bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi iyiliğe yatkın ve ona layıktır."},{"facet_id":"F002","role":"specialization","statement":"Karşılaştırmalı yapıda kişi, belirli bir işi yapmaya grubun en uygun üyesidir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak bu kişi niteliğini alçak gönüllülükle birlikte verir."}],"identity_rationale":"Kaynak ifadesi belirli yapılarda bir kişinin iyiliğe yatkın, ona layık ve alçak gönüllü oluşunu; karşılaştırmalı yapıda ise bir işi yapmaya en uygun kişi sayılmasını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"iyiliğe yatkın, layık ve alçak gönüllü kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"bunu yapmaya en uygunları"}],"lexicalization_note":"Tanım bütünüyle belirtilen kişi ve eylem tamlamalarına bağlıdır; yalın biçime bağımsız bir uygunluk anlamı yüklenmez.","neighbor_coverage_note":"Tüm komşular değerlendirildi; genel layıklık alanıyla karışma olasılığı en yüksek olan karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal iyilik alanına ve iki belirli yapıya bağlıdır; komşu dalın uygunluk ve hazır oluş kapsamı daha geneldir.","focus_only":"İyiliğe yatkınlıkla birlikte alçak gönüllülük çağrışımı ve belirli kalıplara bağlılık taşır.","gloss":"bir şeye layık ve hazır","neighbor_only":"Herhangi bir şeye hazır, uygun veya layık olmayı daha geniş biçimde anlatır.","neighbor_ref":"root_000434/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ile uygun görüldüğü nitelik veya eylem arasındaki yatkınlık ilişkisini bildirir."}],"source_phrase_ar":"رجل أريض للخير أي خليق له شبه بالأرض الأريضة (maqayis)؛ رجل أريض أي متواضع خليق للخير (sihah)؛ هو آرضهم أن يفعل ذلك أي أخلقهم (sihah)","source_summary":"Kaynaklar, iyiliğe yatkınlık ve layıklık ile belirli bir eyleme en uygun olma yargısını yapı bağımlı tek bir uygunluk alanında birleştirir.","sources":["MQ","SI"],"what_is_ar":"الرجل الأريض للخير؛ آرض القوم أن يفعل الشيء أي أخلقهم به","what_is_not_ar":"ليس الأرض الحسية ولا الزكام ولا الرعدة"},"support_links":[]},{"boundary":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_kind":"non_bare","branch_ref":"root_000025/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"yabancı kimse","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız kanıtlanan sabit adlandırmanın kişi anlamını doğal biçimde karşılar.","boundary_detail":"Bu anlam yalnız sabit adlandırmaya aittir ve genel olarak yeryüzünde yaşayan kişiyi anlatmaz.","branch_image_ar":"ابن الأرض الغريب","concept_gloss":"yabancı kimse","definition":"Belirli bir sabit adlandırmada, bulunduğu çevreye dışarıdan gelen veya oraya ait olmayan yabancı kimseyi belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit söz birimi, bir yerde yabancı olan kimseyi adlandırır."}],"identity_rationale":"Tek kaynak ifadesi, sabit bir adlandırmanın doğrudan yabancı kimse anlamına geldiğini belirtir; yer sakini veya soy bağına ilişkin daha ayrıntılı bir koşul kurmaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yabancı kimse"}],"lexicalization_note":"Tanım yalnız kanıtlanan sabit söz birimine bağlanır; parçaların yalın anlamlarından yeni bir kişi sınıfı türetilmez.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel yabancı anlamına en yakın, fakat topluluk koşuluyla ayrılan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kanıtı yalnız yabancı olmayı söyler; komşu dal yabancının başka bir topluluk içinde bulunması koşulunu açıkça taşır.","focus_only":"Yabancılığı herhangi bir ek topluluk koşulu vermeden sabit bir adlandırmayla bildirir.","gloss":"başka bir topluluğa girmiş yabancı","neighbor_only":"Kişinin kendisinden olmayan bir topluluğun içine girmiş bulunmasını özellikle belirtir.","neighbor_ref":"root_000009/B006","relation_type":"near_synonym","shared_zone":"İki dal da bulunduğu insan çevresine aslen ait olmayan kişiyi anlatır."}],"source_phrase_ar":"فلان ابن أرض أي غريب (maqayis)","source_summary":"Tek kanıt, söz biriminin yabancı kimseyi belirten kısıtlı ve kalıplaşmış bir adlandırma olduğunu gösterir.","sources":["MQ"],"what_is_ar":"ابن أرض إذا أريد الغريب","what_is_not_ar":"ليس ساكن الأرض مطلقا ولا الأرض التي نحن عليها"},"support_links":[]},{"boundary":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_kind":"bare","branch_ref":"root_000025/B005","candidate_links":[{"candidate_id":"cand_9e38a11249262f78f209","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"kalın yün veya kıl yaygı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin türünü, belirleyici kalınlığını ve iki olası malzemesini birlikte karşılar.","boundary_detail":"Bu dal genel yer, hasır, döşek veya süslü kumaş değil; malzemesi ve kalınlığı belirtilmiş bir yaygıdır.","branch_image_ar":"الإراض البساط الضخم","concept_gloss":"kalın yün veya kıl yaygı","definition":"Yünden veya hayvan kılından yapılmış kalın ve büyükçe bir yaygıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, yün ya da hayvan kılından yapılmış kalın bir yaygıdır."}],"identity_rationale":"Kaynak ifadesi nesneyi kalın, büyükçe bir yaygı olarak tanımlar ve malzemesini yün ya da hayvan kılıyla sınırlar.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kalın yün veya kıl yaygı"}],"lexicalization_note":"Tanım yalın adın kanıtlanan nesne anlamıyla sınırlıdır ve komşu döşeme türlerinin özelliklerini içeri almaz.","neighbor_coverage_note":"Sağlanan kartların tümü değerlendirildi; nesne türü bakımından en yakın fakat kapsamı daha geniş döşeme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal malzeme ve kalınlıkla tanımlanan belirli bir yaygıdır; komşu dal işlevi bakımından daha geniş bir döşeme sınıfıdır.","focus_only":"Yaygının kalın ve özellikle yün ya da hayvan kılından yapılmış olmasını gerektirir.","gloss":"döşek veya alta serilen örtü","neighbor_only":"Döşek, yatak örtüsü ve genel olarak alta serilen nesneleri kapsar.","neighbor_ref":"root_001397/B007","relation_type":"same_field","shared_zone":"Her iki dal da zemine ya da yatma yerine serilen ev eşyalarını adlandırır."}],"source_phrase_ar":"الإراض بساط ضخم من وبر أو صوف (maqayis)؛ الإراض بالكسر بساط ضخم من صوف أو وبر (sihah)","source_summary":"Kaynaklar nesnenin yaygı oluşunda, kalınlığında ve yün ya da hayvan kılından yapılmasında birleşir.","sources":["MQ","SI"],"what_is_ar":"الإراض بالكسر؛ بساط ضخم من وبر أو صوف","what_is_not_ar":"ليس الأرض ولا الأرضة ولا الأريضة"},"support_links":["sup_7892890c2ad85c8d7e9f"]},{"boundary":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_kind":"bare","branch_ref":"root_000025/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"yere çökercesine ağırlaşıp oyalanmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yerden ayrılmayarak yere bağlı kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yere bağlılık, ağırlaşma ve gecikme bileşenlerini tek bir eylem karşılığında toplar.","boundary_detail":"Dal, yere yönelen ağırlık ve kalma durumudur; tembellik, geri kayma veya bir başkasına karşı çıkma değildir.","branch_image_ar":"لزوم الأرض والتثاقل إليها","concept_gloss":"yere çökercesine ağırlaşıp oyalanmak","contextual_glosses":[{"applicability":"Kişinin doğrudan yere bağlı kalması öne çıktığında kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yere doğru ağırlaşma ile oyalanıp gecikme görünüşlerini dışarıda bırakır.","preserves":"Yere bağlı kalma ve bulunduğu noktadan ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"yerinden ayrılmamak","usage_role":"contextual"}],"definition":"Kişinin yere bağlı kalmasını veya yere çökercesine ağırlaşmasını ve bu yüzden bir süre oyalanıp gecikmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yerden ayrılmayarak yere bağlı kalır."},{"facet_id":"F002","role":"extension","statement":"Yere doğru ağırlaşma, oyalanma ve gecikme olarak gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi kişinin yere bağlı kalmasını, yere doğru ağırlaşmasını ve bunun sonucu oyalanıp gecikmesini aynı hareket durumu içinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yere bağlı kalmak, ağırlaşıp oyalanmak"}],"lexicalization_note":"Tanım yalın eylem dalının yere bağlı kalma, ağırlaşma ve gecikme bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yere bağlı kalma çekirdeğini en doğrudan paylaşan ve kapsam farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişinin yere doğru ağırlaşıp gecikmesini anlatır; komşu dal farklı canlı ve nesnelerde yere yapışma ya da sabit kalma alanına daha geniş yayılır.","focus_only":"İnsan için yere doğru ağırlaşma ve bununla birlikte oyalanma anlamını taşır.","gloss":"yere yapışıp yerinde kalmak","neighbor_only":"İnsan dışında kuş ve yırtıcıları, ayrıca yuva ve yerinde ağır duran nesne örneklerini de kapsar.","neighbor_ref":"root_000222/B001","relation_type":"near_synonym","shared_zone":"İki dalda da yere yakın durma ve bulunulan yerden ayrılmama durumu vardır."}],"source_phrase_ar":"تأرض فلان إذا لزم الأرض (maqayis)؛ فقام عجلان وما تأرضا أي ما تلبث (sihah)؛ التأرض أيضا التثاقل إلى الأرض (sihah)","source_summary":"Kanıt, yere bağlı kalmayı çekirdek alır ve yere doğru ağırlaşma ile oyalanmayı bu durumun görünüşleri olarak birleştirir.","sources":["MQ","SI"],"what_is_ar":"تأرض فلان إذا لزم الأرض؛ التأرض بمعنى التثاقل والتلبث إلى الأرض","what_is_not_ar":"ليس التصدي والتعرض للغير ولا النبات المتأرض"},"support_links":[]},{"boundary":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_kind":"bare","branch_ref":"root_000025/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"karşısına çıkıp kendini ortaya koymak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiye yönelmiş karşı duruşu ve görünür biçimde ortaya çıkmayı birlikte karşılar.","boundary_detail":"Bu dal bir başkasına yönelmiş karşı duruşu anlatır; yere çökme, ağırlaşma veya yalnızca yüz yüze bulunma değildir.","branch_image_ar":"التعرض والتصدي","concept_gloss":"karşısına çıkıp kendini ortaya koymak","definition":"Birine doğru yönelip onun karşısına çıkmayı, kendini ortaya koyarak ona karşı durmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir başkasına yönelir, karşısına çıkar ve kendini ona karşı ortaya koyar."}],"identity_rationale":"Tek kaynak ifadesi eylemi, birine doğru çıkıp onun karşısında kendini ortaya koymak ve ona karşı durmak biçiminde açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinin karşısına çıkıp kendini ortaya koymak"}],"lexicalization_note":"Tanım yalın eylem dalını, bir hedefe yönelme ve karşısına çıkma koşullarıyla sınırlar.","neighbor_coverage_note":"Tüm komşular değerlendirildi; yönelme ve karşıya çıkma çekirdeğini en yakından paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiler arası karşıya çıkışı öne çıkarır; komşu dal bakma, gözetme ve genel yüzünü dönme kullanımlarını da kapsar.","focus_only":"Bir kişiye doğru gelerek onun karşısında kendini ortaya koyma hareketini bildirir.","gloss":"bir şeye yönelip karşısına çıkmak","neighbor_only":"Bir şeye bakmak üzere yükselme, onu gözetme veya yalnızca yüzünü ona çevirme kapsamına uzanır.","neighbor_ref":"root_000853/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da bir hedefe yönelme ve onun karşısında konum alma anlamını taşır."}],"source_phrase_ar":"جاء فلان يتأرض إلي أي يتصدى ويتعرض (sihah)","source_summary":"Tek kanıt, eylemin hedefe yönelmiş bir karşıya çıkma ve kendini ortaya koyma hareketi olduğunu gösterir.","sources":["SI"],"what_is_ar":"جاء فلان يتأرض إلى غيره أي يتصدى ويتعرض له","what_is_not_ar":"ليس التثاقل إلى الأرض ولا لزومها"},"support_links":[]},{"boundary":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_kind":"bare","branch_ref":"root_000025/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"titreme veya ürperme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan bedenindeki kısa ya da süren sarsıntı durumunu doğrudan karşılar.","boundary_detail":"Dal genel şiddetli sarsıntı veya belirli bir ateş nöbeti değil, insanda görülen titreme durumudur.","branch_image_ar":"الأَرْض الرعدة","concept_gloss":"titreme veya ürperme","definition":"Bir insanın bedeninde beliren titreme, sarsılma veya ürperme durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan bedenini tutan bir titreme veya ürperme meydana gelir."}],"identity_rationale":"Kaynak ifadesi bu dalı insanda görülen titreme, sarsılma veya ürperme olarak açıkça tanımlar ve yer ya da hastalık anlamlarından ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"insanı tutan titreme veya ürperme"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"titreme ve sarsılma"}],"lexicalization_note":"Tanım yalın biçimlerin insandaki titreme ve ürperme anlamıyla sınırlıdır; komşu hastalık nedenleri eklenmez.","neighbor_coverage_note":"Sağlanan bütün kartlar incelendi; genel titreme çekirdeğine en yakın ve kapsam farkı belirgin olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalın bir insan titremesidir; komşu dal nedeni ve öznesi bakımından daha geniştir, ayrıca korkaklık ve gevşeklik nitelemelerine uzanır.","focus_only":"İnsan bedenindeki titreme durumunu herhangi bir özel neden belirtmeden adlandırır.","gloss":"korku veya hastalıktan sarsılma","neighbor_only":"Korku, hastalık veya gevşeklik nedeniyle insan ya da başka bir şeyin sarsılmasını ve kişilik nitelemelerini kapsar.","neighbor_ref":"root_000573/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da insan bedenindeki titreme ve sarsılma alanında örtüşür."}],"source_phrase_ar":"الأرض الرعدة (maqayis;ayn)؛ بفلان أرض أي رعدة (maqayis)؛ الأرْص النفضة والرعدة (sihah)","source_summary":"Kaynaklar bu adın insanda görülen titreme ve ürperme durumunu bildirdiğinde birleşir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الرعدة أو النفضة في الإنسان","what_is_not_ar":"ليس الأرض التي تقابل السماء ولا الزكام"},"support_links":[]},{"boundary":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_kind":"bare","branch_ref":"root_000025/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"soğuk algınlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soğuk algınlığı durumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hastalık çekirdeğini Türkçede en doğal ve ayırt edici biçimde karşılar.","boundary_detail":"Dal solunumla ilgili başka hastalıkları veya genel beden titremesini değil, soğuk algınlığı durumunu ve ilgili türevleri kapsar.","branch_image_ar":"الأَرْض الزكام","concept_gloss":"soğuk algınlığı","contextual_glosses":[{"applicability":"Hastalığın kendisi değil, bu hastalığa tutulmuş kişi nitelendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hastalık adını ve birini hastalığa uğratma eylemini bağımsız olarak karşılamaz.","preserves":"Soğuk algınlığı ile kişi arasındaki etkilenme ilişkisini korur."},"facet_ids":["F002"],"text":"soğuk algınlığına yakalanmış","usage_role":"contextual"}],"definition":"Soğuk algınlığı hastalığını, bu hastalığa yakalanmış kişiyi ve birini bu hastalığa uğratma eylemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soğuk algınlığı durumudur."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, soğuk algınlığına yakalanmış kişiyi niteler."},{"facet_id":"F003","role":"associated_use","statement":"Ettirgen biçim, birini soğuk algınlığına uğratmayı bildirir."}],"identity_rationale":"Kaynak ifadesi hastalığı soğuk algınlığı olarak, etkilenen kişiyi bu hastalığa yakalanmış olarak ve ettirgen biçimi hastalığa uğratmak olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"soğuk algınlığı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına yakalanmış"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"soğuk algınlığına uğratmak"}],"lexicalization_note":"Tanım yalın hastalık adını ve aynı dalda kanıtlanan hasta kişi ile hastalığa uğratma türevlerini korur.","neighbor_coverage_note":"Bütün komşu kartları değerlendirildi; aynı hastalık ve hasta kişi alanını en doğrudan paylaşan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın türetim dizisinde hastalığa uğratma da vardır; komşu dalın kanıtı ise bir kaynakta daha genel hastalık yorumu içerir.","focus_only":"Hastalık adı, hastaya ilişkin niteleme ve hastalığa uğratma eylemini birlikte kapsar.","gloss":"soğuk algınlığı ve hasta olma","neighbor_only":"Soğuk algınlığı yanında daha genel bir hastalık alanına açılan ayrı bir kaynak yorumunu da taşır.","neighbor_ref":"root_000916/B003","relation_type":"near_synonym","shared_zone":"Her iki dal soğuk algınlığını ve bu hastalığa yakalanmış kişiyi ifade eder."}],"source_phrase_ar":"الأرض الزكمة رجل مأروض أي مزكوم (maqayis)؛ الأرض الزكام وأرض فهو مأروض (ayn)؛ الأرض الزكام وقد آرضه الله إيراضا أي أزكمه فهو مأروض (sihah)","source_summary":"Kaynaklar hastalık adı ile hasta kişi nitelemesinde birleşir; kanıt ayrıca hastalığa uğratma eylemini aynı türetim alanında gösterir.","sources":["MQ","AY","SI"],"what_is_ar":"الأَرْض بمعنى الزكمة أو الزكام؛ مأروض لمن أصابه الزكام","what_is_not_ar":"ليس الرعدة ولا الأرض الحسية"},"support_links":[]},{"boundary":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_kind":"mixed_non_bare","branch_ref":"root_000025/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"odun yiyen küçük canlı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Küçük canlı odunla beslenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlıyı kanıtlanan boyutu ve onu ayırt eden beslenme davranışıyla kısa ve doğal biçimde karşılar.","boundary_detail":"Canlının kendisi çekirdektir; odunun yenmiş duruma gelmesi yalnız belirtilen eylem yapısına bağlı sonuçtur.","branch_image_ar":"الأَرَضَة آكلة الخشب","concept_gloss":"odun yiyen küçük canlı","contextual_glosses":[{"applicability":"Bir odunun bu canlı tarafından yenerek zarar görmüş olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Canlının beyaz ve karıncaya benzer oluşunu bağımsız bir tanım olarak vermez.","preserves":"Odunun canlı tarafından yenmiş ve zarar görmüş olma sonucunu korur."},"facet_ids":["F002"],"text":"odun yiyen küçük canlı tarafından yenmiş","usage_role":"contextual"}],"definition":"Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Küçük canlı odunla beslenir."},{"facet_id":"F002","role":"associated_use","statement":"Canlı odunu yiyerek onu aşınmış ve zarar görmüş hale getirir."},{"facet_id":"F003","role":"source_variant","statement":"Bir kaynak canlıyı beyaz ve karıncaya benzer olarak niteler."}],"identity_rationale":"Kaynak ifadesi beyaz, karıncaya benzeyen ve odun yiyen küçük canlıyı tanımlar; ayrıca bu canlının odunu yiyerek onu zarar görmüş hale getirmesini verir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"odun yiyen küçük canlı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"odunu bu canlı yedi ve zarar verdi"}],"lexicalization_note":"Tanım canlı adını yalın çekirdek olarak verir ve odunun yenmesini yalnız kanıtlanan tamlamaya bağlı sonuç yüzü olarak ayırır.","neighbor_coverage_note":"Tüm aday kartlar değerlendirildi; odun yiyen canlı çekirdeğine en yakın fakat canlı ve nesne kapsamı farklı olan komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal odun yiyen küçük canlı ve onun oduna etkisidir; komşu dal ağaç, yaprak ve gövde üzerinde beslenen başka bir canlıya özgüdür.","focus_only":"Odun yiyen küçük canlıyı ve bu canlının yediği odunun sonucunu belirtir.","gloss":"ağacı delen ve yiyen küçük canlı","neighbor_only":"Özellikle ağaçta delik açan, yaprak veya odun yiyen başka bir küçük canlıyı ve ağacın uğradığı durumu kapsar.","neighbor_ref":"root_000699/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da odunsu bitki maddesini yiyerek zarar veren küçük canlıları anlatır."}],"source_phrase_ar":"الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)؛ الأرضة بالتحريك دويبة تأكل الخشب (sihah)؛ أرضت الخشبة تؤرض أرضا فهي مأروضة إذا أكلتها (sihah)؛ الأرضة الدودة التي تقع في الخشب من الأرض (mufradat)؛ أرضت الخشبة فهي مأروضة (mufradat)","source_summary":"Kaynaklar odun yiyen küçük canlı ile onun odunda oluşturduğu yenme ve zarar görme sonucunu aynı anlam alanında birleştirir.","sources":["AY","SI","MU"],"what_is_ar":"الأَرَضَة؛ دويبة تأكل الخشب؛ أرضت الخشبة فهي مأروضة إذا أكلتها الأرضة","what_is_not_ar":"ليس الأرض ولا الأرض الأريضة ولا الزكام"},"support_links":[]},{"boundary":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_kind":"collocation","branch_ref":"root_000025/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"yaranın irinlenip bozulması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız yara bağlamında irin toplama ile ortaya çıkan bozulma sürecini eksiksiz karşılar.","boundary_detail":"Anlam yalnız yara ile kurulan yapıda geçerlidir ve irinlenmenin yol açtığı bozulmayı zorunlu olarak içerir.","branch_image_ar":"فساد القرحة بالمدة","concept_gloss":"yaranın irinlenip bozulması","definition":"Bir yaranın irin toplaması, kabarıp su toplaması ve bu irinlenme yüzünden bozulmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yara irin toplayarak kabarır ve irinlenme sonucunda bozulur."}],"identity_rationale":"Tek kaynak ifadesi, yaranın irin toplamasıyla kabarıp bozulmasını bir süreç olarak verir; yalnız irin maddesini veya genel deri şişliğini adlandırmaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yara irinlenip kabardı ve bozuldu"}],"lexicalization_note":"Tanım yalnız yara öznesiyle kurulan kanıtlanmış tamlamaya bağlıdır; yalın biçime genel bozulma anlamı verilmez.","neighbor_coverage_note":"Bütün komşular incelendi; irin birikmesi çekirdeğini en yakından paylaşan ve sonuç bakımından ayrılan kart yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal irin birikimini yaranın kabarıp bozulmasına bağlar; komşu dal yalnız irin toplanması ya da dışarı çıkmasıyla yetinebilir.","focus_only":"Yaranın irinlenmeyle kabarıp bozulması sürecini zorunlu olarak içerir.","gloss":"yarada irin toplanması","neighbor_only":"İrinin yarada toplanmasını veya yaradan çıkmasını, bozulma sonucu aramadan kapsar.","neighbor_ref":"root_001664/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da yaranın içinde irin birikmesi durumunu anlatır."}],"source_phrase_ar":"أرضت القرحة تأرض أرضا أي مجلت وفسدت بالمدة (sihah)","source_summary":"Tek kanıt, yara içindeki irinlenme ile kabarma ve bozulmayı birbirine bağlı tek bir hastalık süreci olarak gösterir.","sources":["SI"],"what_is_ar":"أرضت القرحة إذا مجلت وفسدت بالمدة","what_is_not_ar":"ليس الزكام ولا الأرضة ولا الرعدة"},"support_links":[]},{"boundary":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_kind":"bare","branch_ref":"root_000025/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","surface_ar":"أَرْضُ"}],"gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}}],"root_ar":"ء ر ض","root_id":"root_000025","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Neden yorumunu, akıl durumunu ve belirleyici istemsiz beden hareketini birlikte açıklar.","boundary_detail":"Dal yalnız akıl karışıklığı değildir; doğaüstü nedene bağlanma ve istemsiz baş-gövde hareketi birlikte korunmalıdır.","branch_image_ar":"المأروض المخبول من أهل الأرض","concept_gloss":"doğaüstü etkiye bağlanan istemsiz sarsıntılı akıl bozukluğu","contextual_glosses":[{"applicability":"Kişinin gözlenebilir beden hareketi ön plana çıkarıldığında açıklayıcı karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Akıl bozukluğunu ve durumun görünmez varlıkların etkisine bağlanmasını dışarıda bırakır.","preserves":"Baş ve gövdenin bilinçli amaç olmadan hareket etmesi belirtisini korur."},"facet_ids":["F002"],"text":"başıyla gövdesini istemsizce sarsan kişi","usage_role":"explanatory"}],"definition":"Yerle ilişkilendirilen görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğudur; etkilenen kişi başını ve gövdesini isteği dışında hareket ettirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin akıl ve beden durumu görünmez varlıkların etkisine bağlanır."},{"facet_id":"F002","role":"specialization","statement":"Etkilenen kişi başını ve gövdesini bilinçli bir amaç olmadan hareket ettirir."}],"identity_rationale":"Kaynak ifadesi, görünmez varlıkların etkisine bağlanan bir akıl ve beden bozukluğunu; kişinin başını ve gövdesini istemeden hareket ettirmesiyle birlikte tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"görünmez varlıkların etkisine bağlanan, başını ve gövdesini istemsizce hareket ettiren kişi"}],"lexicalization_note":"Tanım yalın kişi nitelemesinin doğaüstü açıklama, akıl bozukluğu ve istemsiz beden hareketi bileşenleriyle sınırlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; doğaüstü etkiye bağlanan akıl bozukluğu çekirdeğini en doğrudan paylaşan komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli bir kaynak ilişkilendirmesi ve istemsiz baş-gövde hareketi gerektirir; komşu dal daha genel bir doğaüstü dokunuş açıklamasıdır.","focus_only":"Yerle ilişkilendirilen görünmez varlıklar açıklamasını ve istemsiz baş-gövde hareketini birlikte taşır.","gloss":"doğaüstü dokunuşa bağlanan akıl karışıklığı","neighbor_only":"Doğaüstü bir dokunuşla açıklanan akıl karışıklığını beden hareketi koşulu olmadan daha genel verir.","neighbor_ref":"root_001423/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da akıl bozukluğunu görünmez bir varlığın etkisiyle açıklayan geleneksel anlayışta buluşur."}],"source_phrase_ar":"المأروض الذي به خبل من الجن وأهل الأرض وهو الذي يحرك رأسه وجسده على غير عمد (sihah)","source_summary":"Tek kanıt, doğaüstü varlıklara bağlanan akıl karışıklığını ve istemsiz baş-gövde hareketini aynı kişi durumunun ayrılmaz parçaları olarak verir.","sources":["SI"],"what_is_ar":"المأروض الذي به خبل من الجن وأهل الأرض ويحرك رأسه وجسده على غير عمد","what_is_not_ar":"ليس المزكوم المأروض ولا الخشبة المأروضة"},"support_links":[]},{"boundary":"Anlam, yalnızca yıkılmayı değil, darbeyle kırma ve sonunda yere düzleme sonucunu da gerektirir.","branch_kind":"mixed_non_bare","branch_ref":"root_000482/B001","candidate_links":[{"candidate_id":"cand_709e1828426a34c65cee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"dövüp kırarak yerle bir etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hedefe kuvvetli darbeler uygulayarak onu kırma ve yapısını bozma."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kırılan yapıyı ayakta kalmayacak biçimde yıkıp yer düzeyine indirme."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yıkıcı darbenin hedefi sarsması ve zemine benzer bir duruma getirmesi."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Duvarın veya dağın kırılıp yıkılması bu işlemin belirgin örneğidir."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Darbe, kırılma, yıkılma ve yere düzlenme aşamalarının birlikte anlatıldığı genel kullanım için uygundur.","boundary_detail":"Anlam, yalnızca yıkılmayı değil, darbeyle kırma ve sonunda yere düzleme sonucunu da gerektirir.","branch_image_ar":"الدق والهدم حتى التسوية","concept_gloss":"dövüp kırarak yerle bir etme","contextual_glosses":[{"applicability":"Duvar, dağ veya başka bir yapının kırılarak ayakta kalmaz hale getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıkma işlemini ve hedefin yer düzeyine indirilmesini açıkça korur."},"facet_ids":["F001","F002","F004"],"text":"yıkıp yere düzlemek","usage_role":"contextual"},{"applicability":"Tek ve güçlü bir darbenin hedefi sarsarak yıktığı bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sarsmayı, yıkıcı darbeyi ve yere indirme sonucunu birlikte korur."},"facet_ids":["F001","F002","F003"],"text":"sarsıp yerle bir etmek","usage_role":"contextual"}],"definition":"Bir şeyi darbelerle dövüp kırarak yapısını bozmak ve onu yer düzeyine inecek ölçüde yıkmaktır; işlem sarsmayı da içerebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hedefe kuvvetli darbeler uygulayarak onu kırma ve yapısını bozma."},{"facet_id":"F002","role":"core","statement":"Kırılan yapıyı ayakta kalmayacak biçimde yıkıp yer düzeyine indirme."},{"facet_id":"F003","role":"associated_use","statement":"Yıkıcı darbenin hedefi sarsması ve zemine benzer bir duruma getirmesi."},{"facet_id":"F004","role":"example","statement":"Duvarın veya dağın kırılıp yıkılması bu işlemin belirgin örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Darbeyle kırma sürecini ve yer düzeyine kadar indirme sınırını belirtmez.","preserves":"Hedefin ayakta kalmayacak biçimde bozulması sonucunu korur."},"text":"yıkma"},{"category":"confusable","error_profile":{"adds":"Sıkıştırma ve basınçla biçim bozma yöntemini öne çıkarır.","collision":"Yıkıcı darbe yerine sıkıştırma işlemi anlaşılabilir.","fit":"displacement","loses":"Yapıyı kırıp yıkarak yer düzeyine indirme sonucunu kaybeder.","preserves":"Kuvvet uygulanması ve biçimin bozulması yönünü kısmen korur."},"text":"ezme"}],"identity_rationale":"Kaynak ifadesi, bir şeyi dövüp kırma ve yıkma işlemini, onu yer düzeyine indirinceye kadar sürdürmeyi açıkça bir arada verir. Sarsma bu işlemin eşlik eden biçimidir; tek başına titreşim anlamı değildir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"dövüp kırarak yerle bir etme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi dövüp kırarak yere düzlemek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"duvarı veya dağı kırıp yıkmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tek darbede sarsıp yerle bir etmek"}],"lexicalization_note":"Dal hem yalın eylem ve ad biçimlerini hem de duvar, dağ ve tek darbe ile sınırlı kuruluşları içerir; kuruluş örnekleri yalın anlamın tamamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar kırma, çökme, sarsma, biçim, gömme, güç, zaman, kalabalık ve ağırlık sınırları bakımından karşılaştırıldı. Okur açısından en yakın dört karışma noktası seçildi; öteki adaylar yalnızca aynı senaryoya katılıyor veya ayrı bir çekirdeğe sahip.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal etkin bir dövme ve kırma sürecini yere düzleme sonucuyla sınırlar; komşu dal ise yapısal çöküşü ve bundan türeyen soyut kayıpları da kapsar.","focus_only":"Darbeyle kırmayı ve hedefi yer düzeyine kadar indirmeyi zorunlu kılar.","gloss":"yerle bir etme ile çöküş","neighbor_only":"Kendiliğinden çökme, düzenin bozulması, aşağılanma ve gücün yok olması gibi daha geniş sonuçları da kapsar.","neighbor_ref":"root_000204/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yapının ayakta kalma düzenini yitirip yıkılması alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dalda son sınır yere düzlemektir; komşuda ise kırmanın yok edici şiddeti belirleyicidir ve düzleme sonucu gerekli değildir.","focus_only":"Kırılan hedefin yere eşitlenecek ölçüde düzlenmesi temel sonuçtur.","gloss":"yerle bir etme ile parçalayarak yok etme","neighbor_only":"Öldürücü veya yok edici kırmayı ve karşısına çıkanı parçalayan gücü öne çıkarır.","neighbor_ref":"root_001234/B002","relation_type":"near_synonym","shared_zone":"İki dal da şiddetli kırma yoluyla hedefin bütünlüğünü ortadan kaldırır."},{"boundary_match":"partial","distinction":"Bu dal sarsıntıyı yıkım sürecinin parçası yapar; komşunun çekirdeği ise yapısal yıkım gerektirmeyen hareket ve titreşimdir.","focus_only":"Sarsıntı, kırma ve yıkma yoluyla kalıcı bir düzleme sonucuna bağlanır.","gloss":"yıkıcı sarsma ile titreşim","neighbor_only":"Nesnenin veya yerin yıkılmadan yalnızca titreyip kararsızlaşmasını da kapsar.","neighbor_ref":"root_000638/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da hedefin güçlü biçimde sarsılması bulunabilir."},{"boundary_match":"partial","distinction":"Bu dal bir değişim ve yıkma eylemidir; komşu dal ise çoğunlukla var olan biçim ve görünüş niteliğidir.","focus_only":"Bir hedefi darbeyle kırıp alçaltan etkin süreci anlatır.","gloss":"düzleme işlemi ile basık biçim","neighbor_only":"Arazi, kum veya beden biçiminde bulunan yayvan, geniş ya da alçak görünümü anlatır.","neighbor_ref":"root_000482/B002","relation_type":"near_neighbor","shared_zone":"Yere yakın veya düz bir görünüm iki dalın kesişen sonucudur."}],"source_phrase_ar":"دككت الشيء مثل دققته (maqayis)؛ الدك كسر الحائط والجبل (ayn;tahdhib)؛ الدك الدق وضربته وكسرته حتى سويته بالأرض (sihah)؛ دكتا زلزلتا ودك هدم (tahdhib)؛ جعلت بمنزلة الأرض اللينة (mufradat)","source_summary":"Ortak anlatım, kuvvetli darbe, kırma ve yıkmayı tek bir süreçte birleştirir; sürecin ayırt edici sonu, hedefin yer düzeyine indirilmesidir. Sarsma, bu yıkıcı sürecin bir görünümü olarak aktarılır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"دك الشيء بمعنى دقه وكسره وهدمه وزلزله حتى يسويه بالأرض","what_is_not_ar":"ليس مجرد عرض الظهر ولا تمام الزمان ولا الدكان"},"support_links":["sup_a940d452a99401e00bee"]},{"boundary":"Düzlük ve alçaklık merkezde kalır, ancak geniş sırtlar ile alçak veya belirgin toprak tepecikleri dışarıda bırakılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000482/B002","candidate_links":[{"candidate_id":"cand_709e1828426a34c65cee","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"yayvan, geniş veya alçak yükseltili biçim","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzey veya gövde biçiminde yüksekliğin sınırlı, enin geniş ve görünümün yayvan olması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazinin geniş ve düz, kumun ise yere yapışık ve yükselmeyen durumda bulunması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin hörgücünün bulunmaması veya atın geniş sırtlı ve kısa yapılı olması."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Biçim adının alçak dağ, tepe benzeri yükselti veya doğal kil tepecikleri için de kullanılması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Arazi, kum ve beden biçimindeki ortak düşük yükselti ve genişlik çekirdeğini birlikte anlatmak için uygundur.","boundary_detail":"Düzlük ve alçaklık merkezde kalır, ancak geniş sırtlar ile alçak veya belirgin toprak tepecikleri dışarıda bırakılamaz.","branch_image_ar":"الانبساط والانخفاض","concept_gloss":"yayvan, geniş veya alçak yükseltili biçim","contextual_glosses":[{"applicability":"Arazinin yayvan, geniş ve düz olduğu kullanımlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Araziye özgü genişlik ve düzlük niteliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"geniş ve düz arazi","usage_role":"contextual"},{"applicability":"Devenin hörgücünün bulunmadığını veya yitmiş olduğunu belirten kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deveye özgü gövde biçimini ve hörgücün yokluğunu açıkça korur."},"facet_ids":["F001","F003"],"text":"hörgüçsüz deve","usage_role":"contextual"},{"applicability":"Atın sırt genişliği ile kısa veya alçak yapısının birlikte anlatıldığı kuruluş için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ata özgü geniş sırtı ve kısa gövde yapısını birlikte korur."},"facet_ids":["F001","F003"],"text":"geniş sırtlı kısa at","usage_role":"contextual"}],"definition":"Bir yüzeyin veya beden biçiminin yayvan, geniş, basık ya da sınırlı yükseltili oluşudur; arazi ve kumda düzlüğü veya alçak kabarıklığı, hayvanda ise hörgüçsüzlüğü ya da geniş ve kısa sırtı belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzey veya gövde biçiminde yüksekliğin sınırlı, enin geniş ve görünümün yayvan olması."},{"facet_id":"F002","role":"specialization","statement":"Arazinin geniş ve düz, kumun ise yere yapışık ve yükselmeyen durumda bulunması."},{"facet_id":"F003","role":"specialization","statement":"Devenin hörgücünün bulunmaması veya atın geniş sırtlı ve kısa yapılı olması."},{"facet_id":"F004","role":"source_variant","statement":"Biçim adının alçak dağ, tepe benzeri yükselti veya doğal kil tepecikleri için de kullanılması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Geniş sırtı, hörgüçsüzlüğü ve alçak tepe biçimlerini dışarıda bırakır.","preserves":"Arazi ve kum örneklerindeki yükselmeme ve düz görünüm yönünü korur."},"text":"düzlük"},{"category":"confusable","error_profile":{"adds":"Yüzeyin içeri doğru oyulmuş olduğu izlenimini ekler.","collision":"Alçak kabarıklık, yanlış biçimde bir çukur olarak anlaşılabilir.","fit":"displacement","loses":"Genişlik, yayvanlık ve doğal tepecik biçimlerini karşılamaz.","preserves":"Yüksekliğin azlığı ve alçak görünüm yönünü kısmen korur."},"text":"çöküklük"}],"identity_rationale":"Kaynak ifadesi düz ve alçak araziyi desteklemekle birlikte yalnızca alçalma anlatmaz; geniş ve kısa sırtı, yükselmeyen sıkışık kumu, alçak dağı ve doğal kil tepeciklerini de kapsar. Bu nedenle dal, tek bir düzleşme sonucu yerine yayvanlık, genişlik ve sınırlı yükselti çevresinde tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geniş ve düz arazi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"hörgücü olmayan veya hörgücünü yitirmiş deve"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"geniş sırtlı, kısa yapılı at"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yere yapışık, yükselmeyen kumluk"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"doğal kil tepecikleri"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"alçak tepe veya yayvan dağ"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çökmüş kum tepeleri, yarılmış tepeler veya hörgüçleri çökmüş develer"}],"lexicalization_note":"Dal, arazi ve tepe adları gibi yalın biçimlerle belirli arazi, deve ve at kuruluşlarını birlikte içerir; hayvanlara özgü nitelikler arazi anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar düzlük, yumuşaklık, sertlik, çıkıntı, genişlik ve aynı kökün öteki dalları bakımından değerlendirildi. En yararlı dört sınır seçildi; kalan adaylar yalnızca uzak biçim benzerliği gösteriyor veya ayrı kullanım alanlarına aittir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal düzlüğü daha geniş bir biçim ailesinin parçası yapar; komşu dalın çekirdeği ise pürüzsüz ve düzgün arazi yüzeyidir.","focus_only":"Kum, dağ ve hayvan sırtındaki yayvan ya da basık biçimleri de kapsar.","gloss":"yayvan biçim ile pürüzsüz düzlük","neighbor_only":"Arazi yüzeyinin pürüzsüz ve tek çizgide görünmesini özellikle belirtir.","neighbor_ref":"root_000870/B001","relation_type":"near_synonym","shared_zone":"İki dal da özellikle arazi için düz ve yayılmış bir yüzey görünümünü anlatabilir."},{"boundary_match":"partial","distinction":"Bu dalın ayırıcı yönü biçim ve düşük yükseltidir; komşu dalda yumuşaklık ve incelik belirleyicidir.","focus_only":"Yayvanlığı sertlik veya yumuşaklık gerektirmeden, beden ve tepe biçimlerine kadar genişletir.","gloss":"yayvan düzlük ile yumuşak düzlük","neighbor_only":"Arazinin ince ve yumuşak olmasını, suyun yayılıp çekilebildiği bir yüzeyi içerir.","neighbor_ref":"root_000586/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da alçak, düz veya yayılmış bir arazi görünümü bulunur."},{"boundary_match":"partial","distinction":"Düzlük ortak olsa da bu dal biçimsel alçaklık ve genişliğe, komşu ise malzemenin sertlik ve kalınlığına dayanır.","focus_only":"Yüzeyin yayvan, alçak veya geniş biçimini anlatır ve sertlik koşulu koymaz.","gloss":"yayvan arazi ile sert arazi","neighbor_only":"Arazinin kalın, dayanıklı ve sert yapısını temel nitelik yapar.","neighbor_ref":"root_000253/B003","relation_type":"near_neighbor","shared_zone":"İki dal da düz araziyi betimleyebilir."},{"boundary_match":"partial","distinction":"Bu dal bir biçim durumudur; komşu dal o durumu ortaya çıkaran yıkıcı işlemi anlatır.","focus_only":"Var olan yayvan, geniş veya düşük yükseltili biçimi niteler.","gloss":"basık biçim ile yerle bir etme","neighbor_only":"Bir şeyi darbeyle kırıp yıkarak düzleme eylemini anlatır.","neighbor_ref":"root_000482/B001","relation_type":"near_neighbor","shared_zone":"Düz veya yere yakın görünüm, iki dalda sonuç ya da nitelik olarak bulunabilir."}],"source_phrase_ar":"الأرض الدكاء الأرض العريضة المستوية (maqayis)؛ الدكداك من الرمل ما التبد بالأرض فلم يرتفع (maqayis;sihah;tahdhib)؛ أرض دكاء مسواة وناقة دكاء لا سنام لها (mufradat)؛ فرس أدك عريض الظهر قصير (sihah;tahdhib)؛ الدك شبه التل والدكاوات تلال خلقة (ayn)","source_summary":"Toplu kanıt, düz ve geniş araziyi, yere yapışık kumu, geniş ve kısa hayvan sırtını ve hörgüçsüzlüğü ortak bir yayvan biçim çevresinde toplar. Tepe ve kil kabartısı örnekleri, bu biçimin mutlak düzlük olmadığını gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الأرض الدكاء والجبل الدك والدكداك من الرمل والناقة الدكاء والفرس الأدك فيما يدل على الانخفاض أو الاستواء أو عرض الظهر","what_is_not_ar":"ليس فعل الدق والهدم نفسه ولا الدفن بالتراب ولا تمام الحول"},"support_links":["sup_a940d452a99401e00bee"]},{"boundary":"Anlam yalnızca verilen ölü ve kuyu kuruluşlarında geçerlidir; yalın biçime genel bir gömme anlamı yüklenemez.","branch_kind":"collocation","branch_ref":"root_000482/B003","candidate_links":[{"candidate_id":"cand_b32dc363460b5bca94e4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"üzerine toprak yığıp gömme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprağı hedefin üzerine döküp yığarak onu örtme veya doldurma."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Mezardaki ölünün üzerine toprak yığarak gömme işlemini tamamlama."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kuyuyu toprakla doldurup görünmez ve kullanılamaz hale getirme."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ölünün üzerine toprak yığma ile kuyuyu toprakla doldurma kuruluşlarının ortak işlemini anlatır.","boundary_detail":"Anlam yalnızca verilen ölü ve kuyu kuruluşlarında geçerlidir; yalın biçime genel bir gömme anlamı yüklenemez.","branch_image_ar":"إهالة التراب والدفن","concept_gloss":"üzerine toprak yığıp gömme","contextual_glosses":[{"applicability":"Mezardaki ölünün toprakla örtüldüğü özel kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölüyü, toprağın üzerine yığılmasını ve gömme bağlamını korur."},"facet_ids":["F001","F002"],"text":"ölünün üzerine toprak yığmak","usage_role":"contextual"},{"applicability":"Bir kuyunun içine toprak dökülerek kapatıldığı özel kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuyuyu toprakla doldurma ve kapatma işlemini eksiksiz korur."},"facet_ids":["F001","F003"],"text":"kuyuyu toprakla doldurmak","usage_role":"contextual"}],"definition":"Verilen kuruluşlarda, ölünün üzerine toprağı döküp yığmak veya bir kuyuyu toprakla doldurarak kapatıp gömmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprağı hedefin üzerine döküp yığarak onu örtme veya doldurma."},{"facet_id":"F002","role":"specialization","statement":"Mezardaki ölünün üzerine toprak yığarak gömme işlemini tamamlama."},{"facet_id":"F003","role":"extension","statement":"Kuyuyu toprakla doldurup görünmez ve kullanılamaz hale getirme."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Toprağı hedefin üzerine yığmadan yapılan başka gömme ve saklama yöntemlerini de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Hedefin toprak altında kalması sonucunu genel olarak korur."},"text":"gömmek"},{"category":"confusable","error_profile":{"adds":"Kumaş, kapak veya başka araçlarla yapılan her türlü kapatmayı da kapsar.","collision":"Toprağı döküp yığma işlemi sıradan bir üst örtmeyle karışabilir.","fit":"broadening","loses":null,"preserves":"Hedefin üstünün kapanması sonucunu korur."},"text":"örtmek"}],"identity_rationale":"Kaynak ifadesi iki kuruluşu aynı somut işlemde birleştirir: ölünün üzerine toprağı döküp yığmak ve kuyuyu toprakla doldurarak gömmek. Dal genel saklama değil, toprağın hedefin üzerine yığılmasıyla gerçekleşen örtme ve doldurma işlemidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ölünün üzerine mezarda toprak yığmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kuyuyu toprakla doldurup kapatmak"}],"lexicalization_note":"Dal bütünüyle iki toprak yığma kuruluşuna bağlıdır; ölü gömme veya herhangi bir şeyi saklama anlamı yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar mezar, gizleme, örtme, canlı gömme, toprağı açma ve aynı kökün öteki dalları açısından karşılaştırıldı. Seçilen dört komşu işlem, hedef ve yön farklarını en açık biçimde gösteriyor; kalanlar nesne adı veya daha uzak senaryo ortaklığı düzeyindedir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal toprağı üzerine dökme hareketine bağlı ve kuyuya da uzanır; komşu dal ölünün mezara konulmasını merkez alır.","focus_only":"Ölünün üzerine toprak yığma işlemini ve ayrıca kuyuyu toprakla doldurmayı belirtir.","gloss":"toprak yığma ile mezara gömme","neighbor_only":"Ölüyü mezara yerleştirme, ona mezar sağlama ve mezarlık gibi daha geniş gömme alanını kapsar.","neighbor_ref":"root_001195/B001","relation_type":"near_synonym","shared_zone":"İki dal da ölünün toprak altında bırakıldığı gömme sürecinde buluşur."},{"boundary_match":"partial","distinction":"Bu dal belirli hedefler üzerine toprak dökme işlemidir; komşu dalın çekirdeği araçtan bağımsız biçimde gizlemektir.","focus_only":"Ölü veya kuyu üzerine toprak yığılmasıyla sınırlıdır.","gloss":"toprak yığma ile gizleyerek gömme","neighbor_only":"Herhangi bir şeyi başka bir nesnenin altına ya da toprağa sokarak gizlemeyi kapsar.","neighbor_ref":"root_000475/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda hedef toprak aracılığıyla gözden kaldırılabilir."},{"boundary_match":"opposed","distinction":"Bu dal örtme yönünde ilerler; komşu dal toprağı dağıtıp gizlenmiş hedefi görünür kılar.","focus_only":"Toprağı hedefin üzerine yığarak onu örter ve kapatır.","gloss":"gömme ile açığa çıkarma","neighbor_only":"Toprağı kaldırıp çevirerek gömülü olanı açığa çıkarır.","neighbor_ref":"root_000130/B001","relation_type":"antonym","shared_zone":"İki dal aynı toprak ve gömülü hedef ekseninde ters yönlü işlemler anlatır."},{"boundary_match":"partial","distinction":"Bu dalın insan hedefi ölüdür; komşu dal canlı kurbanı gömme ve öldürme yönüyle ayrılır.","focus_only":"Ölü üzerine veya kuyuya toprak yığma kuruluşlarını kapsar.","gloss":"ölüyü örtme ile canlıyı gömme","neighbor_only":"Canlı bir kız çocuğunu toprakla örtüp öldürme eylemini içerir.","neighbor_ref":"root_001615/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir insanın üzerine toprak yükseltilerek beden görünmez kılınır."}],"source_phrase_ar":"دككت التراب على الميت إذا هلته عليه (maqayis;tahdhib)؛ دككت الركى أي دفنته بالتراب (sihah)","source_summary":"Kanıt, toprağın hedef üzerine yığılmasını ortak işlem olarak verir. Ölü üzerindeki toprak gömme işlevi görürken, kuyuya dökülen toprak boşluğu doldurup kuyuyu kapatır.","sources":["MQ","SI","TA"],"what_is_ar":"دك التراب على الميت أو دك الركية بمعنى هال التراب عليها ودفنها","what_is_not_ar":"ليس كسر الجبل ولا عرض الظهر ولا تمام الزمن"},"support_links":["sup_128aad8e82588a4803b9"]},{"boundary":"Ateşli hastalık dalın ana ve açık bağlamıdır; bunun yanında bir kaynakta neden belirtilmeden verilen genel hasta durumu da korunur.","branch_kind":"mixed_non_bare","branch_ref":"root_000482/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"ateşli hastalığa tutulma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateşli hastalığın kişiyi etkisi altına alarak hasta etmesi."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu etkilenmenin sonucu olarak kişinin hasta durumda bulunması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir tanıklıkta türemiş biçimin hastalık nedeni belirtilmeden genel olarak hasta kişi için kullanılması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateşli hastalığın kişiyi yakalaması ve hasta duruma getirmesi çekirdeğini anlatır.","boundary_detail":"Ateşli hastalık dalın ana ve açık bağlamıdır; bunun yanında bir kaynakta neden belirtilmeden verilen genel hasta durumu da korunur.","branch_image_ar":"دك الحمى","concept_gloss":"ateşli hastalığa tutulma","contextual_glosses":[{"applicability":"Hastalığın kişiyi etkileyip hasta ettiği eylem kuruluşunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin ateşli hastalığın etkisine girmesini doğal bir eylemle anlatır."},"facet_ids":["F001"],"text":"ateşli hastalığa yakalanmak","usage_role":"contextual"},{"applicability":"Kişinin hastalığın etkisindeki durumunu niteleyen kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateşli hastalığın sonucunda oluşan hasta durumunu korur."},"facet_ids":["F002"],"text":"ateşli hastalığa tutulmuş","usage_role":"contextual"}],"definition":"Ateşli bir hastalığın kişiyi yakalayıp hasta etmesi veya bir kaynakta neden belirtilmeden verildiği üzere kişinin hastalanmış durumda bulunmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateşli hastalığın kişiyi etkisi altına alarak hasta etmesi."},{"facet_id":"F002","role":"associated_use","statement":"Bu etkilenmenin sonucu olarak kişinin hasta durumda bulunması."},{"facet_id":"F003","role":"source_variant","statement":"Bir tanıklıkta türemiş biçimin hastalık nedeni belirtilmeden genel olarak hasta kişi için kullanılması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Ateşsiz ve başka nedenli bütün hastalıkları da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Kişinin sağlıklı durumdan hasta duruma geçmesini korur."},"text":"hastalanma"},{"category":"confusable","error_profile":{"adds":"Geçici sıcaklık hissi veya duygusal tepki anlamını ekler.","collision":"Hastalık, kısa süreli bir sıcaklık nöbetiyle karıştırılabilir.","fit":"displacement","loses":"Kişiyi hasta eden süreli ateşli hastalık durumunu kaybeder.","preserves":"Bedende hissedilen sıcaklık yönünü kısmen korur."},"text":"ateş basması"}],"identity_rationale":"Kaynak ifadesinin çoğu ateşli hastalığın kişiyi yakalamasını açıkça destekler; bir tanıklık ise türemiş biçimi hastalığın nedenini belirtmeden kişinin hastalanması olarak verir. Bu nedenle ateşli hastalık ana bağlamdır, ancak genel hastalık tanıklığı dışlanamaz.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ateşli hastalık onu yakalayıp hasta etti"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ateşli hastalığa tutulmuş kişi"}],"lexicalization_note":"Dal, ateşli hastalığın kişiyi yakaladığı kuruluşla bu durumdaki hastayı belirten biçimi birlikte içerir; bunlar genel bir yalın hastalanma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar ateşli hastalık, zamanlı nöbet, bedensel bozulma, zehir ısısı, öksürük, yakma ve aynı kökün öteki dalları bakımından karşılaştırıldı. Seçilen dört aday hastalık türü, etken ve sonuç sınırlarını en açık biçimde gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kişiye yönelen hastalık etkisini anlatır; komşu dal daha geniş bir varlık grubunda ateşli olma alanını kapsar.","focus_only":"Ateşli hastalığın kişiyi yakalaması ve bu nedenle hasta olması kuruluşuna bağlıdır.","gloss":"ateşli hastalığa tutulma ile ateşli durum","neighbor_only":"İnsan dışındaki hayvan, arazi ve yiyecek için kullanılan ateşli durumları da kapsar.","neighbor_ref":"root_000001/B005","relation_type":"near_synonym","shared_zone":"İki dal da insan bedenindeki ateşli hastalık durumunu ifade edebilir."},{"boundary_match":"partial","distinction":"Bu dal genel yakalanma durumudur; komşu dalın ayırıcı özelliği nöbetin bilinen zamanda gelmesidir.","focus_only":"Hastalığın yakalamasını zaman veya tekrar koşulu koymadan anlatır.","gloss":"ateşe tutulma ile zamanlı ateş nöbeti","neighbor_only":"Ateş nöbetinin belirli bir zamanda gelip hastayı yeniden tutmasını belirtir.","neighbor_ref":"root_001640/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da ateşli hastalık kişiye yönelip onu etkiler."},{"boundary_match":"field_only","distinction":"Bu dalın hastalık türü ve insan hedefi belirgindir; komşu dal çok çeşitli bedensel durumlar için daha geniştir.","focus_only":"Belirli olarak ateşli hastalığın kişiyi hasta etmesini anlatır.","gloss":"ateşli hastalık ile bedeni tutan durum","neighbor_only":"Göz hastalığı, bedensel rahatsızlık, sersemlik ve başka durumların bedeni ele geçirmesini kapsar.","neighbor_ref":"root_000018/B007","relation_type":"same_field","shared_zone":"İki dal da bir hastalık veya bozukluğun bedeni etkisi altına alması alanındadır."},{"boundary_match":"field_only","distinction":"Bu dal ateşli hastalığın etkisini adlandırır; komşu dal hastalığın türünden bağımsız zayıflama ve değişimi öne çıkarır.","focus_only":"Hastalık etkeninin kişiyi yakalamasını ve ateşli hasta durumunu bildirir.","gloss":"ateşe tutulma ile bedensel zayıflama","neighbor_only":"Bedenin zayıflaması, rengin veya genel halin değişmesini sonuç görünümü olarak bildirir.","neighbor_ref":"root_000576/B004","relation_type":"same_field","shared_zone":"Her iki dal hastalıkla bağlantılı bedensel bozulmayı anlatır."}],"source_phrase_ar":"دك الرجل فهو مدكوك إذا مرض (maqayis)؛ دكته الحمى دكا (ayn;tahdhib)؛ دك الرجل فهو مدكوك إذا دكته الحمى (sihah)","source_summary":"Kanıtın çoğu ateşli hastalığın kişiye yönelen etkisini ve bunun doğurduğu hasta durumunu bir arada verir. Bir tanıklık ise türemiş biçimi hastalığın nedenini belirtmeden genel bir hasta durumu olarak aktarır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"إصابة الحمى للإنسان حتى يقال دكته الحمى أو الرجل مدكوك","what_is_not_ar":"ليس الدك بمعنى الدفن ولا الدكان ولا تمام الحول"},"support_links":[]},{"boundary":"Oturma yeri ve niteliği ayrıca açıklanmayan bilinen mekân anlamı kabul edilir, fakat ikinci biçimin bu köke bağlanması tartışmalı bir çözüm olarak kalır.","branch_kind":"bare","branch_ref":"root_000482/B005","candidate_links":[{"candidate_id":"cand_9e38a11249262f78f209","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"oturma yeri veya bilinen mekân","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın üzerine oturabildiği yer veya oturma yüzeyi."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın, niteliği kaynakta ayrıca açıklanmayan bilinen bir mekân için kullanılması."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İkinci biçimin bu kökten mi yoksa son ünsüzü kökün parçası olan başka bir yapıdan mı geldiğinin tartışmalı olması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki mekân kullanımını ve aralarındaki ad bağlantısını kısa biçimde göstermek için uygundur.","boundary_detail":"Oturma yeri ve niteliği ayrıca açıklanmayan bilinen mekân anlamı kabul edilir, fakat ikinci biçimin bu köke bağlanması tartışmalı bir çözüm olarak kalır.","branch_image_ar":"الدكة والدكان","concept_gloss":"oturma yeri veya bilinen mekân","contextual_glosses":[{"applicability":"İnsanların üzerine oturduğu yer anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üzerine oturulan yeri ve oturma işlevini açıkça korur."},"facet_ids":["F001"],"text":"üzerine oturulan yer","usage_role":"contextual"},{"applicability":"Kaynakta niteliği ayrıca açıklanmadan bilinen sayılan mekân adı için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kaynağın verdiği bilinen mekân kullanımını ek bir işlev yüklemeden korur."},"facet_ids":["F002"],"text":"bilinen mekân","usage_role":"contextual"}],"definition":"Üzerine oturulan bir yer veya niteliği kaynakta ayrıca açıklanmayan bilinen bir mekândır; ikinci adın bu kökle bağlantısı kesin değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın üzerine oturabildiği yer veya oturma yüzeyi."},{"facet_id":"F002","role":"extension","statement":"Adın, niteliği kaynakta ayrıca açıklanmayan bilinen bir mekân için kullanılması."},{"facet_id":"F003","role":"source_variant","statement":"İkinci biçimin bu kökten mi yoksa son ünsüzü kökün parçası olan başka bir yapıdan mı geldiğinin tartışmalı olması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İşlevi ve ölçeği belirsiz bütün yapı türlerini kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"İkinci kullanımın yapılmış bir mekân olması yönünü korur."},"text":"yapı"},{"category":"confusable","error_profile":{"adds":null,"collision":"Taşınabilir bir nesne, sabit bir yer sanılabilir.","fit":"narrowing","loses":"Yükseltilmiş mekânı ve küçük işyeri kullanımını dışarıda bırakır.","preserves":"Üzerine oturma işlevini korur."},"text":"oturak"}],"identity_rationale":"Kaynak ifadesi üzerine oturulan yeri ve niteliği ayrıca açıklanmayan bilinen mekânı bu dalda aktarır, fakat ikinci biçimin kök üyeliği konusunda iki ayrı çözüm bulunduğunu da açıkça belirtir. Anlam korunabilir; ancak kökle ilişki kesin bir türetme gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"üzerine oturulan yer"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"üzerine oturulan yer veya kaynakta niteliği açıklanmayan bilinen mekân"}],"lexicalization_note":"Mekân adları yalın biçimler olarak tanıklanır; tanım yalnızca üzerine oturulan yer ile niteliği kaynakta ayrıca açıklanmayan bilinen mekânı kapsar.","neighbor_coverage_note":"Bütün adaylar oturma, eşya yerleştirme, küçük işyeri, çatılı mekân, temel ve sağlam yapı anlamları bakımından değerlendirildi. Seçilen dört komşu işlev ve yapı türü karışmalarını gösteriyor; diğerleri yalnızca genel yapı alanını paylaşıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir oturma yeri ve yapı adıdır; komşu dal yatak ve destek yüzeyi işlevlerini daha geniş kapsar.","focus_only":"Üzerine oturulan yeri ve kaynakta niteliği açıklanmayan bilinen mekânı adlandırır.","gloss":"oturma yükseltisi ile dinlenme yüzeyi","neighbor_only":"Yatma, dayanma, başı koyma ve yaşam rahatlığıyla ilgili çok çeşitli destek yüzeylerini kapsar.","neighbor_ref":"root_000697/B011","relation_type":"near_neighbor","shared_zone":"Her iki dalda da insanın bedenini dayandırdığı veya üzerinde bulunduğu bir yüzey vardır."},{"boundary_match":"partial","distinction":"Bu dal üzerine oturulan yeri veya niteliği açıklanmayan bilinen mekânı adlandırır; komşu dal eşyayı yerleştirme ve düzenleme işlevine bağlıdır.","focus_only":"İnsanların üzerine oturduğu yeri veya kaynakta bilinen sayılan mekânı belirtir.","gloss":"oturma yeri ile eşya sergileme yeri","neighbor_only":"Eşya ve giysilerin üst üste dizildiği yatak, askılık veya yer işlevini belirtir.","neighbor_ref":"root_001515/B003","relation_type":"near_neighbor","shared_zone":"İki dal da yükseltilmiş ya da ayrılmış bir yüzey veya yer adı olabilir."},{"boundary_match":"partial","distinction":"Bu dal yapım malzemesi, çatı biçimi veya ticari işlev belirtmez; komşu dal belirli hafif yapı malzemeleri ve kemerli biçimle sınırlıdır.","focus_only":"Üzerine oturulan yerle birlikte, niteliği kaynakta açıklanmayan bilinen mekân adını içerir.","gloss":"bilinen mekân ile hafif tezgâh yapısı","neighbor_only":"Kamıştan veya ağaçtan yapılan, kemerli biçimli ev ya da tezgâh yapısını belirtir.","neighbor_ref":"root_000414/B004","relation_type":"near_neighbor","shared_zone":"İki dal da insan kullanımındaki bir mekân veya yapı adı olabilir."},{"boundary_match":"field_only","distinction":"Bu dal oturma işlevini veya yalnızca bilinen mekânı verir; komşu dalın sınırı çatının bulunmasıdır.","focus_only":"Üzerine oturulan yeri veya niteliği kaynakta açıklanmayan bilinen mekânı belirtir.","gloss":"işlevsel yer ile çatılı mekân","neighbor_only":"Bir yerin üstünün çatıyla kapalı olmasını belirleyici yapar.","neighbor_ref":"root_000720/B002","relation_type":"same_field","shared_zone":"Her iki dal insan kullanımına ayrılmış küçük bir yapı veya bölüm alanındadır."}],"source_phrase_ar":"من ذلك الدكان وهو معروف (maqayis)؛ الدكان يقال هو فعلان من الدك ويقال هو فعال من الدكن (ayn;tahdhib)؛ الدكة والدكان الذي يقعد عليه وناس يجعلون النون أصلية (sihah)؛ ومنه الدكان (mufradat)","source_summary":"Toplu kanıt, üzerine oturulan yeri ve niteliği ayrıca açıklanmayan bilinen mekânı aynı ad ailesinde aktarır. Bununla birlikte ikinci biçimin yapısı iki farklı kök çözümüne izin verir; bu ayrılık anlamı değil, kökle bağlantının kesinlik derecesini etkiler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الدكة والدكان موضع يقعد عليه أو بناء معروف إذا جعل من هذا الأصل","what_is_not_ar":"ليس من الدكن إذا جعلت النون أصلية"},"support_links":["sup_7892890c2ad85c8d7e9f"]},{"boundary":"Anlam genel bir güç adı değildir; sert basan erkek ve işte güçlü kadın köle kuruluşlarıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000482/B006","candidate_links":[{"candidate_id":"cand_b6f5299d18ffdcc3ba5a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"işte güçlü olma veya yere sert basma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedensel gücün belirli bir eylemi kuvvetle yerine getirme kapasitesi olarak görünmesi."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir erkeğin yere güçlü ve sert biçimde basması."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kadın kölenin iş yapabilecek güçte olması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kaynakta verilen iki kişi nitelemesinin ortak bedensel güç alanını anlatır.","boundary_detail":"Anlam genel bir güç adı değildir; sert basan erkek ve işte güçlü kadın köle kuruluşlarıyla sınırlıdır.","branch_image_ar":"القوة وشدة الوطء","concept_gloss":"işte güçlü olma veya yere sert basma","contextual_glosses":[{"applicability":"Erkeğin yürürken veya basarken yere güçlü baskı uyguladığını belirten kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Erkek katılımcıyı ve yere yönelik kuvvetli basışı korur."},"facet_ids":["F001","F002"],"text":"yere sert basan adam","usage_role":"contextual"},{"applicability":"Kadın kölenin çalışma gücünü ve iş yükünü karşılayabilmesini belirten kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Katılımcıyı ve iş yapabilme gücünü açık biçimde korur."},"facet_ids":["F001","F003"],"text":"iş görmeye güçlü kadın köle","usage_role":"contextual"}],"definition":"Verilen kişi nitelemelerinde, bedensel gücün yere sert basma veya iş yapabilme biçiminde belirginleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedensel gücün belirli bir eylemi kuvvetle yerine getirme kapasitesi olarak görünmesi."},{"facet_id":"F002","role":"specialization","statement":"Bir erkeğin yere güçlü ve sert biçimde basması."},{"facet_id":"F003","role":"specialization","statement":"Bir kadın kölenin iş yapabilecek güçte olması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Zihinsel, siyasal, maddi ve her türlü genel gücü kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Bedensel kapasite ve kuvvet yönünü korur."},"text":"güçlü"},{"category":"confusable","error_profile":{"adds":null,"collision":"Güç uygulama, yalnızca uzun süre yıpranmama özelliğiyle karıştırılabilir.","fit":"narrowing","loses":"Yere sert basma ve etkin kuvvet uygulama yönünü kaybeder.","preserves":"İş yükünü karşılayabilme yönünü kısmen korur."},"text":"dayanıklı"}],"identity_rationale":"Kaynak ifadesi gücü iki ayrı kuruluşla somutlaştırır: bir erkeğin yere sert basması ve kadın kölenin iş yapmaya güçlü olması. Ortak çekirdek, bedensel gücün belirli bir eylemde açıkça ortaya çıkmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yere güçlü ve sert basan adam"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"iş yapmaya güçlü kadın köle"}],"lexicalization_note":"Dal yalnızca iki kişi nitelemesi içinde tanıklanır; sert basma ve işe dayanma özellikleri yalın kökün bağımsız anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar genel güç, taşıma kapasitesi, güçsüzlük, yorgunluk ve aynı kökün öteki dalları açısından değerlendirildi. Seçilen dört aday, kuruluşla sınırlı gücü hem yakın anlamlardan hem de karşıt bedensel durumlardan ayırıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal iki kalıpla sınırlı somut güç görünümüdür; komşu dal genel ve çok alanlı güç kavramıdır.","focus_only":"Gücü yalnızca sert basan erkek ve işte güçlü kadın köle kuruluşlarında belirtir.","gloss":"kuruluşa bağlı güç ile genel güç","neighbor_only":"Beden, yürek, yardımcı, mal, binek, halat ve genel yeti gibi geniş güç alanlarını kapsar.","neighbor_ref":"root_001274/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin bir işi yapmasını sağlayan bedensel kuvveti ifade edebilir."},{"boundary_match":"partial","distinction":"Bu dalın iş alanı daha geniştir ve sert basışa da uzanır; komşu dal taşıma yüküyle sınırlıdır.","focus_only":"Sert basmayı ve genel iş yapabilme gücünü iki ayrı kuruluşta içerir.","gloss":"iş gücü ile yük taşıma gücü","neighbor_only":"Özellikle yükü taşıyabilecek güce sahip olmayı belirtir.","neighbor_ref":"root_000793/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bedensel gücün zor bir görevi karşılayabilmesini anlatır."},{"boundary_match":"opposed","distinction":"Bu dal yeterli ve belirgin kuvveti, komşu dal ise kapasite ve çare eksikliğini gösterir.","focus_only":"Eylemi güçlü biçimde yerine getirecek bedensel kapasiteyi bildirir.","gloss":"güç ile güçsüzlük","neighbor_only":"Güçsüzlüğü ve işi yapacak çarenin azlığını bildirir.","neighbor_ref":"root_000969/B008","relation_type":"antonym","shared_zone":"İki dal kişinin bir yükü veya işi karşılayabilme kapasitesi eksenindedir."},{"boundary_match":"opposed","distinction":"Bu dal eylem kapasitesinin varlığıdır; komşu dal bu kapasitenin yorulma yoluyla azalmasıdır.","focus_only":"Çalışmayı veya güçlü basışı mümkün kılan etkin kuvveti bildirir.","gloss":"etkin güç ile bitkinlik","neighbor_only":"Yürüme ve bedensel çaba sonucunda gücün tükenmesini ve yorgunluğu bildirir.","neighbor_ref":"root_001070/B003","relation_type":"polarity_pair","shared_zone":"İki dal bedenin eylem sürdürebilme durumu üzerinde karşıt kutupları gösterir."}],"source_phrase_ar":"أمة مدكة قوية على العمل (maqayis;sihah;tahdhib)؛ رجل مدك شديد الوطء (ayn;sihah;tahdhib)","source_summary":"Kanıt, genel ve soyut bir güç kavramından çok, gücün eylemdeki iki görünümünü birleştirir. Biri ayağın yere şiddetli basışıdır; öteki iş yükünü karşılayabilecek bedensel dayanımdır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الرجل المدك شديد الوطء والأمة المدكة قوية على العمل","what_is_not_ar":"ليس الرجل المدكوك بالحمى ولا الدك بمعنى الكسر"},"support_links":["sup_04213bd4a2b53768737f"]},{"boundary":"Anlam yalnızca verilen zaman birimi kuruluşlarında tamlık bildirir; genel tamamlanma veya zamanın sona ermesi anlamına genişletilmez.","branch_kind":"collocation","branch_ref":"root_000482/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"eksiksiz tamamlanmış zaman birimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ölçülen zaman biriminin hiçbir bölümü eksik olmadan tam olması."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir tam yıllık çevrimin eksiksiz geçirilmiş olması."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ayın başlangıcından sonuna kadar bütün olarak tamamlanması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yıl veya ayın tam ölçüsüyle gerçekleştiğini anlatan bütün kaynak kuruluşları için uygundur.","boundary_detail":"Anlam yalnızca verilen zaman birimi kuruluşlarında tamlık bildirir; genel tamamlanma veya zamanın sona ermesi anlamına genişletilmez.","branch_image_ar":"تمام الزمن","concept_gloss":"eksiksiz tamamlanmış zaman birimi","contextual_glosses":[{"applicability":"Bir yıllık sürenin eksiksiz gerçekleştiği iki yıl kuruluşunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yıl birimini ve sürenin eksiksiz olmasını açıkça korur."},"facet_ids":["F001","F002"],"text":"tam bir yıl","usage_role":"contextual"},{"applicability":"Bir aylık sürenin baştan sona eksiksiz olduğu kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ay birimini ve bütün sürenin tamamlanmasını açıkça korur."},"facet_ids":["F001","F003"],"text":"tam bir ay","usage_role":"contextual"}],"definition":"Verilen zaman birimi kuruluşlarında, bir yılın veya ayın eksilmeden bütünüyle tamamlanmış olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ölçülen zaman biriminin hiçbir bölümü eksik olmadan tam olması."},{"facet_id":"F002","role":"example","statement":"Bir tam yıllık çevrimin eksiksiz geçirilmiş olması."},{"facet_id":"F003","role":"example","statement":"Bir ayın başlangıcından sonuna kadar bütün olarak tamamlanması."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Ölçüsü belirsiz ve görece uzun bir süre anlamını ekler.","collision":"Tamlık, sürenin uzunluğuyla karıştırılabilir.","fit":"displacement","loses":"Belirli bir yıl veya ay ölçüsünün eksiksiz tamamlanmasını kaybeder.","preserves":"Bir zaman süresinden söz edildiğini korur."},"text":"uzun zaman"},{"category":"alternative","error_profile":{"adds":"Eksik geçmiş olsa bile biten her süreyi ve sona erme olayını kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Bir zaman diliminin tamamlanmış görünmesini kısmen korur."},"text":"sona ermiş zaman"}],"identity_rationale":"Kaynak ifadesi yıl, ay ve genel yıl adlarıyla kurulan nitelemelerde ortak olarak zaman biriminin eksiksiz tamamlanmasını verir. Burada zamanın geçmesi veya sona ermesi değil, ölçülen birimin tam olması belirleyicidir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tam bir yıl"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"tam bir ay"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"eksiksiz bir yıl"}],"lexicalization_note":"Dal bütünüyle yıl ve ay adlarıyla kurulan nitelemelere bağlıdır; tamlık niteliği yalın biçimin genel anlamı sayılmaz.","neighbor_coverage_note":"Bütün adaylar süre, zaman adı, tamlık, sona erme, ay hesabı ve aynı kökün öteki dalları bakımından karşılaştırıldı. Seçilen dört aday, eksiksiz ölçüyü genel zaman ve daha geniş tamamlanma anlamlarından ayırıyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ölçünün eksiksizliğine odaklanır; komşu dal tamamlanmanın yanında geçiş ve sona erme olayını da anlatır.","focus_only":"Belirli yıl ve ay nitelemelerinde eksiksiz zaman ölçüsünü anlatır.","gloss":"tam süre ile sürenin geçmesi","neighbor_only":"Zamanın geçip sona ermesini ve belirli süreden çıkmayı da kapsar.","neighbor_ref":"root_000239/B006","relation_type":"near_synonym","shared_zone":"Her iki dal yıl, ay veya başka bir zaman biriminin tamamlanmış olmasını ifade edebilir."},{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır, ancak her dal farklı ve sabit zaman kuruluşlarıyla sınırlıdır.","focus_only":"Üç belirli kuruluşta yıl veya ayın tamlığını bildirir.","gloss":"tam yıl ile eksiksiz zaman çifti","neighbor_only":"İki gün veya iki ay gibi çift zaman birimlerinin eksiksizliğini de adlandırır.","neighbor_ref":"root_000234/B008","relation_type":"near_synonym","shared_zone":"İki dal bir zaman ölçüsünün eksiksiz ve noksansız olmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal yalnızca zaman birimi kuruluşudur; komşu dal tamamlanmayı çok farklı süreç ve ölçülere yayar.","focus_only":"Tamlığı yıl ve ay sürelerine bağlar.","gloss":"tam zaman birimi ile genel ölçü tamlığı","neighbor_only":"Gebelik, doğum, ayın dolması, sayma ve ölçme gibi zaman dışı tamamlanmaları da kapsar.","neighbor_ref":"root_000188/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal ölçülen bir bütünün eksiksiz hale gelmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal yılın eksiksizliğini yüklem olarak bildirir; komşu dal yalnızca zaman biriminin adıdır.","focus_only":"Bir yıllık sürenin eksiksiz olmasını özellikle niteler.","gloss":"tam yıl ile yıl","neighbor_only":"Yılı mevsimleriyle birlikte bir zaman birimi olarak adlandırır, tamlık koşulu koymaz.","neighbor_ref":"root_001063/B002","relation_type":"near_neighbor","shared_zone":"İki dal bir yıllık zaman çevrimini gösterebilir."}],"source_phrase_ar":"أقمت عنده حولا دكيكا أي تاما (maqayis;ayn;sihah;tahdhib)؛ الدكيك الشهر التام (tahdhib)؛ عام دكيك أي تام (tahdhib)","source_summary":"Kanıtın ortak noktası, yıl ve ay adlarının eksiksiz süreyi bildiren bir nitelemeyle kullanılmasıdır. Tamlık, sürenin yalnızca sona ermesini değil, bütün ölçü biriminin gerçekleşmesini anlatır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"الحول الدكيك أو الشهر الدكيك أو العام الدكيك بمعنى التام","what_is_not_ar":"ليس الدك بمعنى الهدم ولا الدكداك من الرمل"},"support_links":[]},{"boundary":"Anlam verilen topluluk kuruluşuna bağlıdır ve sıradan toplanma ya da nesnelerin üst üste yığılmasıyla özdeş değildir.","branch_kind":"collocation","branch_ref":"root_000482/B008","candidate_links":[{"candidate_id":"cand_b6f5299d18ffdcc3ba5a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"bir şeyin üzerine üşüşüp sıkışma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Birden çok kişinin aynı hedefe yönelerek dar bir alanda birbirine sıkışması."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kalabalığın belirli bir şeyin üzerine veya çevresine doğru yoğunlaşması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun aynı hedefe yönelerek yoğun kalabalık oluşturduğu kuruluş için uygundur.","boundary_detail":"Anlam verilen topluluk kuruluşuna bağlıdır ve sıradan toplanma ya da nesnelerin üst üste yığılmasıyla özdeş değildir.","branch_image_ar":"التزاحم والتراكم","concept_gloss":"bir şeyin üzerine üşüşüp sıkışma","contextual_glosses":[{"applicability":"Topluluğun belirli bir kişi veya şey çevresinde kalabalıklaştığı akıcı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çok kişinin aynı hedefe doğru yoğun biçimde yönelmesini korur."},"facet_ids":["F001","F002"],"text":"üzerine üşüşmek","usage_role":"contextual"},{"applicability":"Hedef çevresindeki bedensel sıkışmanın özellikle açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hedef çevresindeki yoğunluğu, kalabalığı ve sıkışmayı açıkça korur."},"facet_ids":["F001","F002"],"text":"çevresinde sıkışıp kalabalıklaşmak","usage_role":"explanatory"}],"definition":"Bir topluluğun belirli bir şeyin üzerine veya çevresine doğru üşüşerek birbirine sıkışmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Birden çok kişinin aynı hedefe yönelerek dar bir alanda birbirine sıkışması."},{"facet_id":"F002","role":"specialization","statement":"Kalabalığın belirli bir şeyin üzerine veya çevresine doğru yoğunlaşması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Sıkışma veya ortak hedef bulunmayan düzenli buluşmaları da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Birden çok kişinin aynı yerde bulunmasını korur."},"text":"toplanma"},{"category":"confusable","error_profile":{"adds":"İnsan dışındaki nesne ve maddelerin üst üste birikmesini de kapsar.","collision":"İnsanların hedefe yönelişi, edilgin nesne birikimiyle karıştırılabilir.","fit":"broadening","loses":null,"preserves":"Yoğunlaşma ve dar alanda birikme yönünü korur."},"text":"yığılma"}],"identity_rationale":"Tek kaynak ifadesi, bir topluluğun belirli bir şeyin üzerine veya çevresine doğru sıkışarak kalabalıklaşmasını açıkça verir. Toplanma tek başına yetmez; yönelinen bir hedef ve bedensel sıkışma bulunur.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"topluluk bir şeyin üzerine üşüşüp sıkıştı"}],"lexicalization_note":"Dal yalnızca topluluğun bir hedef üzerinde kalabalıklaşmasını anlatan kuruluşta tanıklanır; yalın biçime genel bir kalabalık veya yığılma anlamı verilmez.","neighbor_coverage_note":"Bütün adaylar hedefe yönelme, itişme, baskı, daralma, topluluk, katmanlı birikme ve aynı kökün öteki dalları bakımından karşılaştırıldı. Seçilen dört aday kalabalığın hareketi ile sonucu arasındaki en yakın sınırları gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ortak hedefe yönelişle sınırlıdır; komşu dal karşılıklı itme ve genel kalabalıklaşmayı daha geniş kapsar.","focus_only":"Kalabalığın belirli bir şeyin üzerine doğru yönelmesini gerektirir.","gloss":"bir hedefe üşüşme ile karşılıklı itişme","neighbor_only":"Yol ve dolaşma alanlarında karşılıklı itişmeyi, hayvan kalabalığını ve başka yoğunlukları da kapsar.","neighbor_ref":"root_000144/B001","relation_type":"near_synonym","shared_zone":"İki dal da insanların dar alanda kalabalıklaşıp birbirini sıkıştırmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dalın sınırı hedefe yöneliştir; komşu dalda belirleyici özellik karşılıklı basınç ve itişmedir.","focus_only":"Aynı şeyin üzerine üşüşen topluluğu anlatır.","gloss":"hedefe üşüşme ile baskılı izdiham","neighbor_only":"Kalabalığın birbirini itip bastırmasını ve baskının şiddetini öne çıkarır.","neighbor_ref":"root_001233/B007","relation_type":"near_synonym","shared_zone":"Her iki dal yoğun kalabalıkta kişilerin birbirine sıkışmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal insan topluluğunun hedefe hareketidir; komşu dal katmanlı birikmeyi insan dışı çokluklara da yayar.","focus_only":"İnsan topluluğunun belirli hedef çevresindeki yönlü kalabalığını anlatır.","gloss":"üşüşme ile üst üste birikme","neighbor_only":"İnsan veya başka varlıkların üst üste binmesini ve malın katmanlı biçimde birikmesini de kapsar.","neighbor_ref":"root_001340/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da çokluk dar alanda yoğunlaşıp birbirinin üzerine binebilir."},{"boundary_match":"partial","distinction":"Bu dal topluluğun eylemini, komşu dal ise çokluğun yol açtığı yer veya çözüm darlığını öne çıkarır.","focus_only":"Kalabalığı oluşturan kişilerin hedefe doğru üşüşme hareketini bildirir.","gloss":"üşüşme ile kalabalıktan daralma","neighbor_only":"Kalabalık nedeniyle yerin dolup daralmasını veya bir sorunun çözüm alanını daraltmasını bildirir.","neighbor_ref":"root_001025/B006","relation_type":"near_neighbor","shared_zone":"İnsan çokluğu bir alanı doldurup sıkışıklık doğurabilir."}],"source_phrase_ar":"تداك عليه القوم إذا ازدحموا عليه (tahdhib)","source_summary":"Tek tanıklık, insan topluluğunun aynı hedefe yönelmesiyle oluşan yoğun ve sıkışık kalabalığı anlatır. Anlam, yalnızca insanların bir arada bulunmasından daha dar; hedefe doğru üşüşmeyi gerektirir.","sources":["TA"],"what_is_ar":"تداك القوم على الشيء بمعنى ازدحموا عليه","what_is_not_ar":"ليس الدك بمعنى تسوية الجبل ولا الدكداك من الرمل"},"support_links":["sup_04213bd4a2b53768737f"]},{"boundary":"Anlam yalnızca verilen cinsel kuruluşta, erkeğin beden ağırlığıyla kadın köleyi zorlamasını anlatır.","branch_kind":"collocation","branch_ref":"root_000482/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","surface_ar":"دُكَّتِ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","surface_ar":"دَكًّا"}],"gloss":"birleşmede beden ağırlığıyla zorlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Cinsel birleşme sırasında erkeğin beden ağırlığını kadın kölenin üzerine vermesi."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu ağırlığın kadın köle üzerinde güçlük ve zorlanma oluşturması."}}],"root_ar":"د ك ك","root_id":"root_000482","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen cinsel birleşme kuruluşundaki katılımcıları, ağırlık aktarımını ve zorlanma sonucunu birlikte anlatır.","boundary_detail":"Anlam yalnızca verilen cinsel kuruluşta, erkeğin beden ağırlığıyla kadın köleyi zorlamasını anlatır.","branch_image_ar":"إلقاء الثقل في المخالطة","concept_gloss":"birleşmede beden ağırlığıyla zorlama","contextual_glosses":[{"applicability":"Erkeğin cinsel birleşme sırasında beden ağırlığını kadın kölenin üzerine bindirdiği anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Cinsel bağlamı ve beden ağırlığının karşı tarafa aktarılmasını korur."},"facet_ids":["F001","F002"],"text":"birleşmede ağırlığını üzerine vermek","usage_role":"contextual"},{"applicability":"Birleşme bağlamı çevrede zaten açıkken ağırlığın doğurduğu zorlanmayı açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ağırlık uygulamasını ve bunun karşı tarafta oluşturduğu güçlüğü korur."},"facet_ids":["F001","F002"],"text":"beden ağırlığıyla zorlamak","usage_role":"explanatory"}],"definition":"Erkeğin cinsel birleşme sırasında beden ağırlığını kadın kölenin üzerine vererek onu zorlamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Cinsel birleşme sırasında erkeğin beden ağırlığını kadın kölenin üzerine vermesi."},{"facet_id":"F002","role":"core","statement":"Bu ağırlığın kadın köle üzerinde güçlük ve zorlanma oluşturması."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Beden ağırlığıyla zorlama bulunmayan bütün birleşmeleri de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Eylemin cinsel temas türünü korur."},"text":"cinsel birleşme"},{"category":"confusable","error_profile":{"adds":"Cinsel bağlam dışında yapılan her türlü fiziksel yüklenmeyi de kapsar.","collision":"Belirli cinsel kuruluş, sıradan bir itme veya yaslanma hareketiyle karıştırılabilir.","fit":"broadening","loses":null,"preserves":"Beden ağırlığını başka birinin üzerine verme yönünü korur."},"text":"üzerine abanma"}],"identity_rationale":"Kaynak ifadesi belirli bir cinsel birleşme kuruluşunda erkeğin ağırlığını kadın kölenin üzerine vermesini ve bunun onu zorlamasını birlikte şart koşar. Genel birleşme veya genel ağırlık anlamı bu ayrıntılı katılımcı ve eylem yapısını karşılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"erkeğin cinsel birleşmede kadın köleyi beden ağırlığıyla zorlaması"}],"lexicalization_note":"Dal tek bir cinsel birleşme kuruluşuna bağlıdır; ağırlık, zorlama veya cinsel temas öğelerinden hiçbiri yalın köke bağımsız anlam olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar beden ağırlığı, şiddetli birleşme, genel cinsel temas, yük altında zorlanma, bedensel tepki ve aynı kökün öteki dalları bakımından karşılaştırıldı. Seçilen dört aday eylemin cinsel, ağırlığa bağlı ve katılımcıları belirli sınırını en iyi gösteriyor.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir beden ağırlığı mekanizmasını ve katılımcıları şart koşar; komşu dal şiddeti daha genel bırakır.","focus_only":"Şiddeti, erkeğin ağırlığını kadın kölenin üzerine vermesiyle somutlaştırır.","gloss":"ağırlıkla zorlama ile şiddetli birleşme","neighbor_only":"Şiddetli cinsel birleşmeyi ağırlık aktarımı veya aynı katılımcı sınırı olmadan anlatır.","neighbor_ref":"root_001403/B009","relation_type":"near_synonym","shared_zone":"İki dal da zorlayıcı veya şiddetli cinsel birleşme alanında buluşur."},{"boundary_match":"partial","distinction":"Bu dal eylemin belirli ve zorlayıcı yapılış biçimidir; komşu dal genel cinsel temas alanını gösterir.","focus_only":"Cinsel birleşmede beden ağırlığıyla karşı tarafı zorlama ayrıntısını içerir.","gloss":"ağırlıkla zorlama ile cinsel temas","neighbor_only":"Cinsel birleşmeyi veya cinsel teması bu ağırlık ve zorlama koşulu olmadan adlandırır.","neighbor_ref":"root_000311/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalın senaryosu cinsel birleşmedir."},{"boundary_match":"partial","distinction":"Bu dal bedensel ve cinsel bir eyleme bağlıdır; komşu dal yük ve güçlüğü genel alanda anlatır.","focus_only":"Ağırlık cinsel birleşme sırasında doğrudan başka bir bedenin üzerine verilir.","gloss":"beden ağırlığıyla zorlama ile ağır yük","neighbor_only":"Herhangi bir yükün veya işin sahibini eğecek ölçüde ağırlaşmasını anlatır.","neighbor_ref":"root_000066/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da ağırlık, başka bir kişi üzerinde güçlük ve baskı oluşturur."},{"boundary_match":"partial","distinction":"Bu dal belirli cinsel katılımcılarla sınırlıdır; komşu dal dayanma ve kendini zorlama gibi cinsel olmayan eylemleri kapsar.","focus_only":"Birleşme sırasında ağırlığın kadın köle üzerine verilmesini anlatır.","gloss":"cinsel ağırlık ile zorlanarak yüklenme","neighbor_only":"Kişinin kendini zorlu yürüyüşe yüklemesini, birine dayanmasını veya genel meşakkati kapsar.","neighbor_ref":"root_000357/B007","relation_type":"near_neighbor","shared_zone":"Her iki dalda bedenin ağırlığını verme veya güçlük altında zorlama bulunabilir."}],"source_phrase_ar":"دك الرجل جاريته إذا جهدها بإلقائه ثقله عليها إذا خالطها (tahdhib)","source_summary":"Tek tanıklık, cinsel birleşmeyi genel biçimde adlandırmakla yetinmez; erkeğin ağırlığını kadın kölenin üzerine vermesini ve onu bu yolla zorlamasını anlamın kurucu parçaları yapar.","sources":["TA"],"what_is_ar":"دك الرجل جاريته بمعنى جهدها بثقله عند المخالطة","what_is_not_ar":"ليس الدك بمعنى الهدم ولا الدفن ولا تمام الزمن"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:21:1"],"branch_refs":[],"candidate_id":"cand_58785f086f7c8ada3a8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:1:no-root-form","source_type":"word_analysis","support_ids":["sup_385c3ee7d728e6d36299","sup_fc95ed939740d47df0b7"],"title":"fixed particle carries the turn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:1","qac_refs":["89:21:1:1"],"status":"accepted"}},{"anchor_refs":["89:21:1"],"branch_refs":[],"candidate_id":"cand_46366b1a0336b49fac38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:1:outside-idha-scope","source_type":"word_analysis","support_ids":["sup_385c3ee7d728e6d36299","sup_44510a5b0448e021e523"],"title":"particle outside the when-clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:1","qac_refs":["89:21:1:1"],"status":"accepted"}},{"anchor_refs":["89:21:1"],"branch_refs":[],"candidate_id":"cand_b811cc6929bfd6a7f299","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:1:rebuke-pivot","source_type":"word_analysis","support_ids":["sup_11f9a6051523eb298147","sup_385c3ee7d728e6d36299"],"title":"rebuke before the eschatological threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:1","qac_refs":["89:21:1:1"],"status":"accepted"}},{"anchor_refs":["89:21:1"],"branch_refs":[],"candidate_id":"cand_700ce950344952aa1cee","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:1:return-and-cadence","source_type":"word_analysis","support_ids":["sup_12ae45dc6b7bbc1703e1","sup_385c3ee7d728e6d36299"],"title":"returning refusal and held sound","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:1","qac_refs":["89:21:1:1"],"status":"accepted"}},{"anchor_refs":["89:21:2"],"branch_refs":[],"candidate_id":"cand_7a4e38b7d582be3f1f8c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:2:delayed-protasis","source_type":"word_analysis","support_ids":["sup_2025c68aa0bdde7d0e52","sup_73558a8d472a20051e92"],"title":"when-clause held open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:2","qac_refs":["89:21:2:1"],"status":"accepted"}},{"anchor_refs":["89:21:2"],"branch_refs":[],"candidate_id":"cand_fd6427e594f7ad3428c3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:2:eventive-when-not-duration","source_type":"word_analysis","support_ids":["sup_3f3aa785266c70e3329c","sup_73558a8d472a20051e92"],"title":"decisive eventive threshold","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:2","qac_refs":["89:21:2:1"],"status":"accepted"}},{"anchor_refs":["89:21:2"],"branch_refs":[],"candidate_id":"cand_01c6e1634f4a8c5f0fef","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:2:fixed-form-and-sound-entry","source_type":"word_analysis","support_ids":["sup_0f515181a5bb6cde48ff","sup_73558a8d472a20051e92"],"title":"light entry into impact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:2","qac_refs":["89:21:2:1"],"status":"accepted"}},{"anchor_refs":["89:21:2"],"branch_refs":[],"candidate_id":"cand_e4ed22e419a7fb0b6e7e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:2:forward-sequence","source_type":"word_analysis","support_ids":["sup_4b111c984779b49560f8","sup_73558a8d472a20051e92"],"title":"threshold anticipates 89:22","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:2","qac_refs":["89:21:2:1"],"status":"accepted"}},{"anchor_refs":["89:21:2"],"branch_refs":[],"candidate_id":"cand_f8f4a88e6bb23e0f99ce","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:2:future-completed-threshold","source_type":"word_analysis","support_ids":["sup_73558a8d472a20051e92","sup_a5de104e89a92a10cf6c"],"title":"future threshold with completed force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:2","qac_refs":["89:21:2:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_9de2fc30abf9fb03e3eb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:arrival-after-collapse","source_type":"word_analysis","support_ids":["sup_261ecd300a5520737456","sup_dbdf10bcfcee1d9b3edb"],"title":"collapse before arrival","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_0aa1f6a419f0a73e38a3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:crushing-result-field","source_type":"word_analysis","support_ids":["sup_b4dc3fc5f1833ff5eb77","sup_dbdf10bcfcee1d9b3edb"],"title":"crushing toward leveled aftermath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_5cfb66ae853d64c5f715","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:echo-and-boundary","source_type":"word_analysis","support_ids":["sup_dbdf10bcfcee1d9b3edb","sup_eddb65b2ccb69587f7ad"],"title":"verb echoed by doublet and boundary reversal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_3cb2f5e8539f06885176","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:feminine-agreement","source_type":"word_analysis","support_ids":["sup_4429cf6b6603aaf82254","sup_dbdf10bcfcee1d9b3edb"],"title":"agreement locks the verb to earth","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_49e6a2776fa54595b1b9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:form-choice-not-iterative","source_type":"word_analysis","support_ids":["sup_0c870f3f3b0aef69337b","sup_dbdf10bcfcee1d9b3edb"],"title":"received action, repetition supplied later","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_3f06121f79e45cb9fc35","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:passive-patient-focus","source_type":"word_analysis","support_ids":["sup_adef905f536d39b9b3fd","sup_dbdf10bcfcee1d9b3edb"],"title":"passive patient-focus with unexpressed agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_afcea237801cfe22237d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:rare-earth-crushing-field","source_type":"word_analysis","support_ids":["sup_8044f5a33224070ca9b6","sup_dbdf10bcfcee1d9b3edb"],"title":"rare d-k-k earth-crushing field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:3","qac_refs":["89:21:3:1"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_667fb7b28e0e9bfee275","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:definite-support-domain","source_type":"word_analysis","support_ids":["sup_ddba9bf90fd4984b8bc8","sup_f83e98fca385db7aeeec"],"title":"known ground as inhabited support","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_d909c4dbae82feb51bd2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:earth-scenes-contrast","source_type":"word_analysis","support_ids":["sup_5ecb7555cdeb89dfe168","sup_f83e98fca385db7aeeec"],"title":"crushing among earth transformation scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_544f0156655bc814053c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:enclosed-by-crushing","source_type":"word_analysis","support_ids":["sup_d75043d5d6249b19d529","sup_f83e98fca385db7aeeec"],"title":"earth enclosed by d-k-k forms","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_7533351995c965aa9c30","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:lower-support-boundary","source_type":"word_analysis","support_ids":["sup_160b3ddfc0d998d9aea5","sup_f83e98fca385db7aeeec"],"title":"from possession to ground","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_dc9fe4b0b0878f27c371","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:passive-subject-earth","source_type":"word_analysis","support_ids":["sup_b845afb7c133599b87ed","sup_f83e98fca385db7aeeec"],"title":"earth as passive subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_8f3d70ad68e32d405a3d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:21:4:total-earth-scale","source_type":"word_analysis","support_ids":["sup_0326d824d6c03fa1ff15","sup_f83e98fca385db7aeeec"],"title":"earth range compressed into one domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:4","qac_refs":["89:21:4:1","89:21:4:2"],"status":"accepted"}},{"anchor_refs":["89:21:5"],"branch_refs":[],"candidate_id":"cand_a586452d4b9c38656881","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:5:first-cognate-accusative","source_type":"word_analysis","support_ids":["sup_2d68ffc0d275cb0940fe","sup_80aa9f88e386d40656b6"],"title":"first cognate accusative specifies manner","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:5","qac_refs":["89:21:5:1"],"status":"accepted"}},{"anchor_refs":["89:21:5"],"branch_refs":[],"candidate_id":"cand_ad2337870cef5063ff48","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:5:first-half-doublet","source_type":"word_analysis","support_ids":["sup_2d68ffc0d275cb0940fe","sup_f969f71c420d7989df3d"],"title":"first half of the exact doublet","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:5","qac_refs":["89:21:5:1"],"status":"accepted"}},{"anchor_refs":["89:21:5"],"branch_refs":[],"candidate_id":"cand_af30ab0b8f059c6f5bb8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:5:passive-color-narrowed","source_type":"word_analysis","support_ids":["sup_2d68ffc0d275cb0940fe","sup_ae50792a07148b26ced5"],"title":"received-collapse coloring under passive context","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:5","qac_refs":["89:21:5:1"],"status":"accepted"}},{"anchor_refs":["89:21:5"],"branch_refs":[],"candidate_id":"cand_2aaba953abe474ff8efd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:5:process-force","source_type":"word_analysis","support_ids":["sup_22daf48fa0953cf3924b","sup_2d68ffc0d275cb0940fe"],"title":"crushing process made explicit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:5","qac_refs":["89:21:5:1"],"status":"accepted"}},{"anchor_refs":["89:21:5"],"branch_refs":[],"candidate_id":"cand_ce57da78fa0d1f6c028e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:5:sound-and-boundary","source_type":"word_analysis","support_ids":["sup_04fb7655955b77023f1b","sup_2d68ffc0d275cb0940fe"],"title":"compact first blow answers excess","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:5","qac_refs":["89:21:5:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_f0cdf2de4323773a82ac","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:asyndetic-final-cadence","source_type":"word_analysis","support_ids":["sup_89ef6c475b0a4bf3f155","sup_a404c4b44c1ec536ae9f"],"title":"unjoined percussive close","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_ada9c844a7d974badc47","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:boundary-moral-reversal","source_type":"word_analysis","support_ids":["sup_a404c4b44c1ec536ae9f","sup_a7eaa5f4c750ce92a40f"],"title":"excess answered by exhaustive leveling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_c4157779dd9c12c5c412","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:forward-rank-echo","source_type":"word_analysis","support_ids":["sup_86eb48dded501504d0ee","sup_a404c4b44c1ec536ae9f"],"title":"doublet prepares 89:22","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_346d2cd30a64cf0fcf5d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:iteration-totalization","source_type":"word_analysis","support_ids":["sup_71084dbe7f2927bf598e","sup_a404c4b44c1ec536ae9f"],"title":"exact repetition creates totalizing force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_b159079575974f32d022","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:lexical-doubling-not-derived-stem","source_type":"word_analysis","support_ids":["sup_219378bb1161f9dbec22","sup_a404c4b44c1ec536ae9f"],"title":"iteration by lexical doubling","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_61d826be019dcd1e1864","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:rare-form-density","source_type":"word_analysis","support_ids":["sup_4101d8c109477ae42f98","sup_a404c4b44c1ec536ae9f"],"title":"rare gerund repeated immediately","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:6"],"branch_refs":[],"candidate_id":"cand_d01dfa439ab5e4e47aa8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:6:second-appositive-accusative","source_type":"word_analysis","support_ids":["sup_13db9c7b692ca77efe7a","sup_a404c4b44c1ec536ae9f"],"title":"second accusative intensifies the first","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:21:6","qac_refs":["89:21:6:1"],"status":"accepted"}},{"anchor_refs":["89:21:3"],"branch_refs":[],"candidate_id":"cand_85886a5c956e3aa832eb","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000482"],"scope":"focus_ayah","source_local_id":"89:21:3:1","source_type":"qac_morpheme","support_ids":["sup_dfc1024b0f2e5bec2e0a"],"title":"QAC root occurrence: د ك ك","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:21:4"],"branch_refs":[],"candidate_id":"cand_5552a85cd6903e96b3c1","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000025"],"scope":"focus_ayah","source_local_id":"89:21:4:2","source_type":"qac_morpheme","support_ids":["sup_7dff391d0604319672e2"],"title":"QAC root occurrence: ء ر ض","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:21","branch_refs":["root_000025/B001","root_000482/B001","root_000482/B002"],"candidate_id":"cand_709e1828426a34c65cee","commentary_obligation":"review","hft_ref":"hft_e19b1d8e11d01c7e4106","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_crush_to_plane","source_type":"hft","support_ids":["sup_a940d452a99401e00bee"],"title":"b_crush_to_plane","trust":"legacy_unbound"},{"anchor_refs":["89:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:21","branch_refs":["root_000025/B001","root_000482/B006","root_000482/B008"],"candidate_id":"cand_b6f5299d18ffdcc3ba5a","commentary_obligation":"review","hft_ref":"hft_f3e4a211ba443360c9b4","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_pressing_mass","source_type":"hft","support_ids":["sup_04213bd4a2b53768737f"],"title":"b_pressing_mass","trust":"legacy_unbound"},{"anchor_refs":["89:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:21","branch_refs":["root_000025/B001","root_000482/B003"],"candidate_id":"cand_b32dc363460b5bca94e4","commentary_obligation":"review","hft_ref":"hft_3e57250a5c810cd452b1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_burial_inversion","source_type":"hft","support_ids":["sup_128aad8e82588a4803b9"],"title":"b_burial_inversion","trust":"legacy_unbound"},{"anchor_refs":["89:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:21","branch_refs":["root_000025/B005","root_000482/B005"],"candidate_id":"cand_9e38a11249262f78f209","commentary_obligation":"review","hft_ref":"hft_3e0be013b1bf9e80b5ea","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_prepared_surface","source_type":"hft","support_ids":["sup_7892890c2ad85c8d7e9f"],"title":"b_prepared_surface","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"89:21:1:1","qac_word_ref":"89:21:1","root_ar":"","surface_ar":"كَلَّآ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"89:21:2:1","qac_word_ref":"89:21:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","root_ar":"د ك ك","surface_ar":"دُكَّتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:21:4:1","qac_word_ref":"89:21:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","root_ar":"د ك ك","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","root_ar":"د ك ك","surface_ar":"دَكًّا"}],"word_analysis_qac_refs":[["89:21:1:1"],["89:21:2:1"],["89:21:3:1"],["89:21:4:1","89:21:4:2"],["89:21:5:1"],["89:21:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:21:1","89:21:2","89:21:3","89:21:4","89:21:5","89:21:6"]},"focus_surface_evidence":{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","qac_morphemes":[{"lemma_ar":"كَلَّا","morph_features":"STEM|POS:AVR|LEM:kal~aA","morpheme_role":"STEM","pos":"AVR","qac_ref":"89:21:1:1","qac_word_ref":"89:21:1","root_ar":"","surface_ar":"كَلَّآ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"89:21:2:1","qac_word_ref":"89:21:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"دُكَّتِ","morph_features":"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS","morpheme_role":"STEM","pos":"V","qac_ref":"89:21:3:1","qac_word_ref":"89:21:3","root_ar":"د ك ك","surface_ar":"دُكَّتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:21:4:1","qac_word_ref":"89:21:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"أَرْض","morph_features":"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:4:2","qac_word_ref":"89:21:4","root_ar":"ء ر ض","surface_ar":"أَرْضُ"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:5:1","qac_word_ref":"89:21:5","root_ar":"د ك ك","surface_ar":"دَكًّا"},{"lemma_ar":"دَكّ","morph_features":"STEM|POS:N|VN|LEM:dak~|ROOT:dkk|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"89:21:6:1","qac_word_ref":"89:21:6","root_ar":"د ك ك","surface_ar":"دَكًّا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:21:1:1"],["89:21:2:1"],["89:21:3:1"],["89:21:4:1","89:21:4:2"],["89:21:5:1"],["89:21:6:1"]],"word_analysis_refs":["89:21:1","89:21:2","89:21:3","89:21:4","89:21:5","89:21:6"],"word_rows":[{"analysis_record_ref":"89:21:1","analytic_gloss_range_en":"emphatic rebuke and refusal that arrests the preceding moral frame before opening the eschatological scene","analytic_root_gloss_range_en":null,"qac_refs":["89:21:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَلَّآ","transliteration":"kallā"}},{"analysis_record_ref":"89:21:2","analytic_gloss_range_en":"eventive when-threshold that opens a future conditional scene and holds its consequence beyond the local ayah","analytic_root_gloss_range_en":null,"qac_refs":["89:21:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"89:21:3","analytic_gloss_range_en":"passive perfect crushing and leveling of the earth, with the agent unexpressed and the following cognate accusatives carrying repeated intensity","analytic_root_gloss_range_en":"root range centered here on crushing, demolishing, pounding, compacting, and leveling; other dictionary branches such as soil-covering, crowding, or platform senses are not locally selected","qac_refs":["89:21:3:1"],"root":{"arabic":"د ك ك","transliteration":"d-k-k"},"surface":{"arabic":"دُكَّتِ","transliteration":"dukkati"}},{"analysis_record_ref":"89:21:4","analytic_gloss_range_en":"the definite earth or ground-domain as known support, passive subject, and inhabited substrate being crushed","analytic_root_gloss_range_en":"earth, land, ground, soil, territory, and inhabited realm; local grammar concentrates that range into the definite support-domain under collapse","qac_refs":["89:21:4:1","89:21:4:2"],"root":{"arabic":"أ ر ض","transliteration":"ʾ-r-ḍ"},"surface":{"arabic":"ٱلْأَرْضُ","transliteration":"al-arḍu"}},{"analysis_record_ref":"89:21:5","analytic_gloss_range_en":"first accusative cognate verbal noun naming the manner and intensity of the passive crushing and opening the repeated doublet","analytic_root_gloss_range_en":"root range centered here on crushing, pounding, compacting, pulverizing, and leveling; the local gerund makes the process explicit as a cognate accusative","qac_refs":["89:21:5:1"],"root":{"arabic":"د ك ك","transliteration":"d-k-k"},"surface":{"arabic":"دَكًّۭا","transliteration":"dakkan"}},{"analysis_record_ref":"89:21:6","analytic_gloss_range_en":"second matching accusative verbal noun that intensifies the first into repeated, distributive, and total crushing","analytic_root_gloss_range_en":"root range centered here on repeated crushing, pounding, compacting, and leveling; exact lexical doubling supplies iteration without changing the local form","qac_refs":["89:21:6:1"],"root":{"arabic":"د ك ك","transliteration":"d-k-k"},"surface":{"arabic":"دَكًّۭا","transliteration":"dakkan"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":6,"words_total":6,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:21"],"branch_refs":["root_000025/B001","root_000482/B001","root_000482/B002"],"candidate_id":"cand_709e1828426a34c65cee","evidence_scope":"focus_ayah","hft_ref":"hft_e19b1d8e11d01c7e4106","item_id":"b_crush_to_plane","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_crush_to_plane","support_id":"sup_a940d452a99401e00bee"},{"anchor_refs":["89:21"],"branch_refs":["root_000025/B001","root_000482/B006","root_000482/B008"],"candidate_id":"cand_b6f5299d18ffdcc3ba5a","evidence_scope":"focus_ayah","hft_ref":"hft_f3e4a211ba443360c9b4","item_id":"b_pressing_mass","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_pressing_mass","support_id":"sup_04213bd4a2b53768737f"},{"anchor_refs":["89:21"],"branch_refs":["root_000025/B001","root_000482/B003"],"candidate_id":"cand_b32dc363460b5bca94e4","evidence_scope":"focus_ayah","hft_ref":"hft_3e57250a5c810cd452b1","item_id":"b_burial_inversion","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_burial_inversion","support_id":"sup_128aad8e82588a4803b9"},{"anchor_refs":["89:21"],"branch_refs":["root_000025/B005","root_000482/B005"],"candidate_id":"cand_9e38a11249262f78f209","evidence_scope":"focus_ayah","hft_ref":"hft_3e0be013b1bf9e80b5ea","item_id":"b_prepared_surface","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_prepared_surface","support_id":"sup_7892890c2ad85c8d7e9f"}],"diagnostics":[],"lane_counts":{"global":15,"macro":8,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:21","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:21","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"89:21","lane":"micro","linguistic_source_ref":"89:21","surface_ref":"89:21","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:21","target_tokens":[["Hayır",["89:21:1"]],["Yer",["89:21:4"]],["tekrar",["89:21:5"]],["tekrar",["89:21:6"]],["ezildiğinde",["89:21:2","89:21:3"]]],"text":"Hayır! Yer tekrar tekrar ezildiğinde,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:total-earth-scale","source_type":"word_analysis","support_id":"sup_0326d824d6c03fa1ff15","text":"{\"blocking_evidence\":null,\"headline\":\"earth range compressed into one domain\",\"reader_payoff\":\"The reader notices that soil, land, terrain, and inhabited world are compressed into one definite earth-domain.\",\"reason\":\"The definite singular concrete noun supports a totalizing local range without requiring plural land-forms.\",\"representative_source_ids\":[\"QG-57eab782\",\"QS-3d9c5554\",\"MS-3d0469f7\",\"QF-c77ae415\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5:sound-and-boundary","source_type":"word_analysis","support_id":"sup_04fb7655955b77023f1b","text":"{\"blocking_evidence\":null,\"headline\":\"compact first blow answers excess\",\"reader_payoff\":\"The reader hears a compact first blow whose intensity answers the immediately preceding moral excess.\",\"reason\":\"The gerund is low occurrence, part of a marked passive-plus-repeated-cognate construction, and the boundary row ties the intensified form to the prior discourse.\",\"representative_source_ids\":[\"ME-18eaeb32\",\"QP-8f70d0d7\",\"QH-6af575df\",\"QB-d6e542fa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:form-choice-not-iterative","source_type":"word_analysis","support_id":"sup_0c870f3f3b0aef69337b","text":"{\"blocking_evidence\":null,\"headline\":\"received action, repetition supplied later\",\"reader_payoff\":\"The reader notices that the finite verb presents received crushing, while repeated impact is pushed into the later doublet.\",\"reason\":\"The local finite form is passive Form I; the following two gerunds carry the repetition by cognate accusative construction.\",\"representative_source_ids\":[\"QF-0a454c4b\",\"QF-32a5234c\",\"QY-93e26d46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2:fixed-form-and-sound-entry","source_type":"word_analysis","support_id":"sup_0f515181a5bb6cde48ff","text":"{\"blocking_evidence\":null,\"headline\":\"light entry into impact\",\"reader_payoff\":\"The reader notices that the uninflected particle gains force from position and from its immediate movement into the heavy crushing verb.\",\"reason\":\"The particle has no inflectional marking, so its force is carried by placement before the passive clause.\",\"representative_source_ids\":[\"QF-b3e4c791\",\"QP-32444053\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:1:rebuke-pivot","source_type":"word_analysis","support_id":"sup_11f9a6051523eb298147","text":"{\"blocking_evidence\":null,\"headline\":\"rebuke before the eschatological threshold\",\"reader_payoff\":\"The reader notices that the ayah begins by rejecting the preceding moral logic before showing the catastrophic answer.\",\"reason\":\"The QAC row identifies an emphatic response and rebuke particle, and attachment support marks the preceding context window as relevant before the temporal clause begins.\",\"representative_source_ids\":[\"QG-3130dc83\",\"QS-375f03e9\",\"QT-be8a1bb0\",\"QB-a008b388\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:1:return-and-cadence","source_type":"word_analysis","support_id":"sup_12ae45dc6b7bbc1703e1","text":"{\"blocking_evidence\":null,\"headline\":\"returning refusal and held sound\",\"reader_payoff\":\"The reader hears the refusal as a boundary sound that carries the social indictment into the collapse scene.\",\"reason\":\"The row family links the particle to the preceding indictment and to the immediate transition into the temporal threshold.\",\"representative_source_ids\":[\"QE-c8f216b8\",\"QP-5216b34c\",\"QP-665e4d20\",\"QB-f370ab5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:second-appositive-accusative","source_type":"word_analysis","support_id":"sup_13db9c7b692ca77efe7a","text":"{\"blocking_evidence\":null,\"headline\":\"second accusative intensifies the first\",\"reader_payoff\":\"The reader sees the second word as intensifying the same manner-force, not introducing a separate argument.\",\"reason\":\"Attachment evidence marks the second gerund as a same-root cognate accusative that repeats the first.\",\"representative_source_ids\":[\"QG-355d4ca2\",\"QG-35d76d31\",\"QG-3ea39c5e\",\"MG-1c8f7742\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:lower-support-boundary","source_type":"word_analysis","support_id":"sup_160b3ddfc0d998d9aea5","text":"{\"blocking_evidence\":null,\"headline\":\"from possession to ground\",\"reader_payoff\":\"The reader sees the discourse shift from what humans possess to the ground that makes possession possible.\",\"reason\":\"The local noun is concrete earth without an explicit heaven-earth pair, and the boundary rows link it to the preceding value-field.\",\"representative_source_ids\":[\"QS-415e9f8d\",\"QS-a8847d5c\",\"QF-d1c3767a\",\"QB-7c074067\",\"QY-fbde5254\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2:delayed-protasis","source_type":"word_analysis","support_id":"sup_2025c68aa0bdde7d0e52","text":"{\"blocking_evidence\":null,\"headline\":\"when-clause held open\",\"reader_payoff\":\"The reader feels 89:21 as an unfinished condition whose answer accumulates in the next scene.\",\"reason\":\"Attachment evidence marks word 2 as opening the temporal scene; the CRITICAL rows correctly press the delayed scope of that scene.\",\"representative_source_ids\":[\"QG-aca928bf\",\"QG-ea39b829\",\"QT-5ca31266\",\"QB-d5174a9c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:lexical-doubling-not-derived-stem","source_type":"word_analysis","support_id":"sup_219378bb1161f9dbec22","text":"{\"blocking_evidence\":null,\"headline\":\"iteration by lexical doubling\",\"reader_payoff\":\"The reader notices that repeated pounding is achieved by exact word repetition rather than by shifting to a different derived stem.\",\"reason\":\"The local second word is the same gerund form as word 5; no alternate iterative surface is present.\",\"representative_source_ids\":[\"QS-bd9d1025\",\"QF-98d0584d\",\"QF-e39d0b03\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5:process-force","source_type":"word_analysis","support_id":"sup_22daf48fa0953cf3924b","text":"{\"blocking_evidence\":null,\"headline\":\"crushing process made explicit\",\"reader_payoff\":\"The reader feels a concrete process of pounding, compaction, and reduction rather than a softened leveling.\",\"reason\":\"The accepted V4 branch centers on crushing and demolishing until leveled, matching the local same-root gerund.\",\"representative_source_ids\":[\"QS-0877fd3a\",\"QS-255d4220\",\"QS-c717fd49\",\"MS-3aa63335\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:arrival-after-collapse","source_type":"word_analysis","support_id":"sup_261ecd300a5520737456","text":"{\"blocking_evidence\":null,\"headline\":\"collapse before arrival\",\"reader_payoff\":\"The reader notices that 89:22 arrives only after the passive collapse has already framed the ground.\",\"reason\":\"The row's concrete 89:22 contrast is consistent with the temporal sequence opened by word 2.\",\"representative_source_ids\":[\"MI-de3aef0a\",\"QB-6152a403\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5","source_type":"word_analysis","support_id":"sup_2d68ffc0d275cb0940fe","text":"{\"gloss_range\":\"first accusative cognate verbal noun naming the manner and intensity of the passive crushing and opening the repeated doublet\",\"prose\":\"The first {{ar:دَكًّۭا}} ({{tr:dakkan}}) turns the verb's event into an explicit process: crushing as the manner and measure of what happens to the earth. Its accusative verbal-noun form keeps it attached to the passive verb, so the unnamed agent does not weaken intensity. In that passive scene it can carry received-collapse coloring, while the local form remains a gerund naming applied force rather than a different reflexive verb. As the first half of an exact doublet, the word is open to immediate repetition; no conjunction interrupts the sequence, and the compact, rare sound prepares the second blow. Its intensified cadence also answers the immediately preceding moral excess with intensified leveling.\",\"root_display\":\"{{ar:د ك ك}} ({{tr:d-k-k}})\",\"root_gloss_range\":\"root range centered here on crushing, pounding, compacting, pulverizing, and leveling; the local gerund makes the process explicit as a cognate accusative\",\"surface_display\":\"{{ar:دَكًّۭا}} ({{tr:dakkan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:1","source_type":"word_analysis","support_id":"sup_385c3ee7d728e6d36299","text":"{\"gloss_range\":\"emphatic rebuke and refusal that arrests the preceding moral frame before opening the eschatological scene\",\"prose\":\"{{ar:كَلَّآ}} ({{tr:kallā}}) is not a neutral scene-opener. It first blocks the preceding logic of security, wealth, and desire, then lets the coming earth-collapse answer that logic. Because the particle stands outside the when-clause and carries no root imagery, its force comes from discourse position: refusal before explanation, rebuke before the threshold. Even its held opening sound helps the ayah pause at refusal before the next temporal scene begins.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَلَّآ}} ({{tr:kallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2:eventive-when-not-duration","source_type":"word_analysis","support_id":"sup_3f3aa785266c70e3329c","text":"{\"blocking_evidence\":null,\"headline\":\"decisive eventive threshold\",\"reader_payoff\":\"The reader reads the word as the trigger-point of collapse, not as a vague stretch of time.\",\"reason\":\"The QAC and attachment rows both treat the particle as governing an eventive temporal clause.\",\"representative_source_ids\":[\"QG-88ab39af\",\"QS-8a50438b\",\"QS-de6d63ac\",\"QT-d309120d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:rare-form-density","source_type":"word_analysis","support_id":"sup_4101d8c109477ae42f98","text":"{\"blocking_evidence\":null,\"headline\":\"rare gerund repeated immediately\",\"reader_payoff\":\"The reader notices that an uncommon d-k-k gerund becomes the ayah's final two-word formal density.\",\"reason\":\"Contextual profiles mark the gerund as low occurrence and strongly tied to the same-root passive construction.\",\"representative_source_ids\":[\"QI-35c43074\",\"QH-473b1192\",\"QH-c479a6e1\",\"QY-efc375eb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:feminine-agreement","source_type":"word_analysis","support_id":"sup_4429cf6b6603aaf82254","text":"{\"blocking_evidence\":null,\"headline\":\"agreement locks the verb to earth\",\"reader_payoff\":\"The reader notices that the feminine ending ties the impact to the earth before the noun is even fully processed.\",\"reason\":\"The subject attachment and QAC grammar identify feminine agreement with the following earth noun.\",\"representative_source_ids\":[\"QG-61de4360\",\"QF-29631dec\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:1:outside-idha-scope","source_type":"word_analysis","support_id":"sup_44510a5b0448e021e523","text":"{\"blocking_evidence\":null,\"headline\":\"particle outside the when-clause\",\"reader_payoff\":\"The reader sees that the refusal is not simply a complement inside the when-clause but a discourse halt before that clause.\",\"reason\":\"The temporal clause is marked as beginning at word 2, leaving word 1 as a prior discourse particle.\",\"representative_source_ids\":[\"QG-d5ccba41\",\"MG-e5d1281f\",\"QT-4785ca8c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2:forward-sequence","source_type":"word_analysis","support_id":"sup_4b111c984779b49560f8","text":"{\"blocking_evidence\":null,\"headline\":\"threshold anticipates 89:22\",\"reader_payoff\":\"The reader carries the crushing forward into the next ayah, where the event frame continues (89:22).\",\"reason\":\"The rows name the forward dependency, and the local clause evidence supports a temporal frame rather than an isolated assertion.\",\"representative_source_ids\":[\"QI-1425e708\",\"QE-71402c52\",\"QB-7f80301c\",\"MT-325ec7ef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:earth-scenes-contrast","source_type":"word_analysis","support_id":"sup_5ecb7555cdeb89dfe168","text":"{\"blocking_evidence\":null,\"headline\":\"crushing among earth transformation scenes\",\"reader_payoff\":\"The reader distinguishes this earth-scene from shaking (99:1), stretching (84:3), replacement (14:48), and the earth-and-mountains crushing pattern (69:14).\",\"reason\":\"The CRITICAL rows provide concrete references, and the contextual evidence supports the earth noun as a common creation-domain term locally constrained by d-k-k.\",\"representative_source_ids\":[\"QI-357e182d\",\"MI-432482e4\",\"MI-96653305\",\"QI-9b440ec3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:iteration-totalization","source_type":"word_analysis","support_id":"sup_71084dbe7f2927bf598e","text":"{\"blocking_evidence\":null,\"headline\":\"exact repetition creates totalizing force\",\"reader_payoff\":\"The reader hears the same crushing force spread across the whole surface through exact repetition.\",\"reason\":\"The local form duplicates the first gerund exactly, and the accepted V4 branch supports crushing and leveling as the active field.\",\"representative_source_ids\":[\"QS-3e8a67a0\",\"QS-6ce48e1e\",\"MS-38b632da\",\"QF-cbc6e5ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2","source_type":"word_analysis","support_id":"sup_73558a8d472a20051e92","text":"{\"gloss_range\":\"eventive when-threshold that opens a future conditional scene and holds its consequence beyond the local ayah\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) turns the collapse into a threshold rather than a freestanding report. It points forward to the moment when the earth is crushed, while the perfect passive inside its clause makes that future event feel already sealed. Because the particle itself is fixed and uninflected, its force is read from position: a light temporal entry is immediately compressed by the heavy crushing verb. The syntax also withholds full closure: the listener must carry this when-clause into the following arrival and judgment scene, so 89:21 functions as the opening condition of a larger sequence.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:21:4:2","source_type":"qac_morpheme","support_id":"sup_7dff391d0604319672e2","text":"{\"lemma_ar\":\"أَرْض\",\"morph_features\":\"STEM|POS:N|LEM:>aroD|ROOT:ArD|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:21:4:2\",\"qac_word_ref\":\"89:21:4\",\"root_ar\":\"ء ر ض\",\"surface_ar\":\"أَرْضُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:rare-earth-crushing-field","source_type":"word_analysis","support_id":"sup_8044f5a33224070ca9b6","text":"{\"blocking_evidence\":null,\"headline\":\"rare d-k-k earth-crushing field\",\"reader_payoff\":\"The reader links this verb to a rare Quranic earth-crushing field, including the earth-and-mountains crushing scene (69:14).\",\"reason\":\"Contextual profiles mark the passive d-k-k form as low occurrence and include 69:14 among the same-form implicit-agent references.\",\"representative_source_ids\":[\"QI-6159ed4c\",\"QI-e069fe8f\",\"MI-824420d1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5:first-cognate-accusative","source_type":"word_analysis","support_id":"sup_80aa9f88e386d40656b6","text":"{\"blocking_evidence\":null,\"headline\":\"first cognate accusative specifies manner\",\"reader_payoff\":\"The reader notices that crushing is grammatically restated as the event's own measure, not merely inferred from the verb.\",\"reason\":\"Attachment evidence marks word 5 as a same-root cognate accusative attached to the passive verb.\",\"representative_source_ids\":[\"QG-13a9b25b\",\"QG-83aed54f\",\"MG-36d74006\",\"QF-0eb5d4a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:forward-rank-echo","source_type":"word_analysis","support_id":"sup_86eb48dded501504d0ee","text":"{\"blocking_evidence\":null,\"headline\":\"doublet prepares 89:22\",\"reader_payoff\":\"The reader carries the doubled crushing cadence into the doubled ranks of the next scene (89:22).\",\"reason\":\"The concrete forward reference is coherent with the temporal sequence opened in 89:21 and continued in 89:22.\",\"representative_source_ids\":[\"QE-577e9566\",\"QB-b9c97609\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:asyndetic-final-cadence","source_type":"word_analysis","support_id":"sup_89ef6c475b0a4bf3f155","text":"{\"blocking_evidence\":null,\"headline\":\"unjoined percussive close\",\"reader_payoff\":\"The reader hears the ayah close with compressed repeated impact rather than a coordinated list.\",\"reason\":\"The two gerunds stand adjacent without a conjunction, and both are marked as repeated cognate accusatives.\",\"representative_source_ids\":[\"QT-0ee4b798\",\"QT-b37fe7e0\",\"MT-0943617d\",\"QP-00719747\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6","source_type":"word_analysis","support_id":"sup_a404c4b44c1ec536ae9f","text":"{\"gloss_range\":\"second matching accusative verbal noun that intensifies the first into repeated, distributive, and total crushing\",\"prose\":\"The second {{ar:دَكًّۭا}} ({{tr:dakkan}}) does not add a new object or a new clause; it repeats the first accusative measure and makes recurrence itself the form of intensity. Because it is bare, appositive, and unjoined, the final cadence feels compressed rather than listed. Exact duplication turns crushing into succession, distribution, and completeness, while the hard repeated d-k-k sound closes the ayah with the impact it names. The repeated rare gerund keeps the same earth-crushing field active through the ayah's last word. The doublet also prepares the doubled ranks of the following scene (89:22), linking collapse to arranged arrival, and it turns prior accumulation and excess into exhaustive leveling.\",\"root_display\":\"{{ar:د ك ك}} ({{tr:d-k-k}})\",\"root_gloss_range\":\"root range centered here on repeated crushing, pounding, compacting, and leveling; exact lexical doubling supplies iteration without changing the local form\",\"surface_display\":\"{{ar:دَكًّۭا}} ({{tr:dakkan}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:2:future-completed-threshold","source_type":"word_analysis","support_id":"sup_a5de104e89a92a10cf6c","text":"{\"blocking_evidence\":null,\"headline\":\"future threshold with completed force\",\"reader_payoff\":\"The reader notices that the coming collapse is introduced as future and yet already completed in aspect.\",\"reason\":\"The particle opens an eventive temporal frame, and the governed verb is a perfect passive.\",\"representative_source_ids\":[\"QG-56d7a31e\",\"MG-369fff4b\",\"QY-ad9297c6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:6:boundary-moral-reversal","source_type":"word_analysis","support_id":"sup_a7eaa5f4c750ce92a40f","text":"{\"blocking_evidence\":null,\"headline\":\"excess answered by exhaustive leveling\",\"reader_payoff\":\"The reader sees prior accumulation and excess answered by a double image of reduction.\",\"reason\":\"The boundary rows tie the final doublet to the preceding moral charge, and the context-window evidence supports reading the transition across ayahs.\",\"representative_source_ids\":[\"QB-82778720\",\"QB-ec4517c7\",\"QB-ec4ccd10\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:passive-patient-focus","source_type":"word_analysis","support_id":"sup_adef905f536d39b9b3fd","text":"{\"blocking_evidence\":null,\"headline\":\"passive patient-focus with unexpressed agent\",\"reader_payoff\":\"The reader sees the collapse from the side of the earth being acted upon, while the agent is left unexpressed.\",\"reason\":\"The aligned verb is passive, has no expressed object or agent, and governs the event whose subject is the earth.\",\"representative_source_ids\":[\"QG-1c35df6f\",\"QG-f4ac7027\",\"MG-86efc5cf\",\"QS-096732bb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5:passive-color-narrowed","source_type":"word_analysis","support_id":"sup_ae50792a07148b26ced5","text":"{\"blocking_evidence\":null,\"headline\":\"received-collapse coloring under passive context\",\"reader_payoff\":\"The reader hears the first gerund as applied force in a passive scene, with received-collapse coloring but not a different local form.\",\"reason\":\"The local word is a gerund, not a reflexive finite form; the passive context can color the process without replacing the local morphology.\",\"representative_source_ids\":[\"QS-4df843e2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:crushing-result-field","source_type":"word_analysis","support_id":"sup_b4dc3fc5f1833ff5eb77","text":"{\"blocking_evidence\":null,\"headline\":\"crushing toward leveled aftermath\",\"reader_payoff\":\"The reader feels the verb as forceful terrain-reduction, not as a bland change of state.\",\"reason\":\"V4 accepts the crushing and leveling branch, and the local subject is the earth.\",\"representative_source_ids\":[\"QS-18a48310\",\"QS-61be3bd8\",\"QS-db055c15\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:passive-subject-earth","source_type":"word_analysis","support_id":"sup_b845afb7c133599b87ed","text":"{\"blocking_evidence\":null,\"headline\":\"earth as passive subject\",\"reader_payoff\":\"The reader notices that the earth grammatically bears the passive collapse rather than appearing as an active verb's object.\",\"reason\":\"Attachment evidence makes the noun the passive subject of the preceding verb, and the QAC row marks it nominative.\",\"representative_source_ids\":[\"QG-179e1661\",\"QG-80b20a39\",\"MG-5bd59154\",\"QF-0c2d26a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:enclosed-by-crushing","source_type":"word_analysis","support_id":"sup_d75043d5d6249b19d529","text":"{\"blocking_evidence\":null,\"headline\":\"earth enclosed by d-k-k forms\",\"reader_payoff\":\"The reader sees the earth positioned between the crushing verb and the repeated crushing nouns, as if syntactically enclosed by impact.\",\"reason\":\"The noun is attached as subject between the passive d-k-k verb and two same-root cognate accusatives.\",\"representative_source_ids\":[\"QS-70570292\",\"QT-ddb232c8\",\"MT-5cc7acc8\",\"QE-56682e53\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3","source_type":"word_analysis","support_id":"sup_dbdf10bcfcee1d9b3edb","text":"{\"gloss_range\":\"passive perfect crushing and leveling of the earth, with the agent unexpressed and the following cognate accusatives carrying repeated intensity\",\"prose\":\"{{ar:دُكَّتِ}} ({{tr:dukkati}}) is the clause's engine: a passive perfect that makes the earth bear the collapse while leaving the crusher unnamed. Its feminine ending already locks the impact to the earth before the noun's full scale is unfolded. The local root pressure is physical reduction, not gentle smoothing or abstract defeat; stable ground is broken toward levelness. The verb itself is not an iterative stem, so the ayah separates patient-focused received action from repetition, which the two following cognate accusatives supply. Its rare d-k-k field and the earth-and-mountains crushing scene (69:14) make the local scene feel formally marked, while 89:22 follows only after the ground has been leveled.\",\"root_display\":\"{{ar:د ك ك}} ({{tr:d-k-k}})\",\"root_gloss_range\":\"root range centered here on crushing, demolishing, pounding, compacting, and leveling; other dictionary branches such as soil-covering, crowding, or platform senses are not locally selected\",\"surface_display\":\"{{ar:دُكَّتِ}} ({{tr:dukkati}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4:definite-support-domain","source_type":"word_analysis","support_id":"sup_ddba9bf90fd4984b8bc8","text":"{\"blocking_evidence\":null,\"headline\":\"known ground as inhabited support\",\"reader_payoff\":\"The reader feels the collapse as an attack on the shared ground and support-system beneath habitation.\",\"reason\":\"The noun is definite and concrete; V4 lacks root rows for this root, so local grammar and CRITICAL evidence preserve the support-domain payoff.\",\"representative_source_ids\":[\"QG-4ecb1555\",\"QS-407c5b08\",\"QS-e8d7f108\",\"QF-a9eb1286\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:21:3:1","source_type":"qac_morpheme","support_id":"sup_dfc1024b0f2e5bec2e0a","text":"{\"lemma_ar\":\"دُكَّتِ\",\"morph_features\":\"STEM|POS:V|PERF|PASS|LEM:duk~ati|ROOT:dkk|3FS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"89:21:3:1\",\"qac_word_ref\":\"89:21:3\",\"root_ar\":\"د ك ك\",\"surface_ar\":\"دُكَّتِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:3:echo-and-boundary","source_type":"word_analysis","support_id":"sup_eddb65b2ccb69587f7ad","text":"{\"blocking_evidence\":null,\"headline\":\"verb echoed by doublet and boundary reversal\",\"reader_payoff\":\"The reader hears the verb answered by its own root echo as the previous excess gives way to leveling.\",\"reason\":\"The attachments identify the two following same-root cognate accusatives, and the CRITICAL boundary rows tie that echo to the discourse turn.\",\"representative_source_ids\":[\"QE-09b8ba9a\",\"QE-f9cc74b7\",\"ME-44ebc45c\",\"QB-632ce6c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:4","source_type":"word_analysis","support_id":"sup_f83e98fca385db7aeeec","text":"{\"gloss_range\":\"the definite earth or ground-domain as known support, passive subject, and inhabited substrate being crushed\",\"prose\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}}) is not the object of an active seizure; it is the nominative passive subject that bears the collapse. Its definiteness gathers the familiar support-domain beneath human life, not an indefinite patch of soil, and compresses soil, land, terrain, and inhabited world into one threatened domain. The common earth noun is locally constrained by the rare d-k-k environment: crushing appears before it and the repeated manner follows it, placing the ground at the hinge of the ayah's impact. Inter-ayah contrasts sharpen the choice: 99:1 shakes the earth, 84:3 stretches it, 14:48 replaces it, and earth and mountains are crushed together (69:14), while 89:21 makes reduction of the ground itself the defining event. The boundary also shifts from what humans love and possess to the ground that makes possession possible.\",\"root_display\":\"{{ar:أ ر ض}} ({{tr:ʾ-r-ḍ}})\",\"root_gloss_range\":\"earth, land, ground, soil, territory, and inhabited realm; local grammar concentrates that range into the definite support-domain under collapse\",\"surface_display\":\"{{ar:ٱلْأَرْضُ}} ({{tr:al-arḍu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:5:first-half-doublet","source_type":"word_analysis","support_id":"sup_f969f71c420d7989df3d","text":"{\"blocking_evidence\":null,\"headline\":\"first half of the exact doublet\",\"reader_payoff\":\"The reader hears the first unit as prepared for exact repetition, so one manner noun becomes the start of a process.\",\"reason\":\"The second same-root gerund is attached as a repeated cognate accusative, making the first word the opening unit of a doublet.\",\"representative_source_ids\":[\"QG-ac41dfe7\",\"QF-de3720ee\",\"QT-bca74803\",\"QE-ef1ee215\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:21:1:no-root-form","source_type":"word_analysis","support_id":"sup_fc95ed939740d47df0b7","text":"{\"blocking_evidence\":null,\"headline\":\"fixed particle carries the turn\",\"reader_payoff\":\"The reader notices that a compact function word, not a lexical root image, performs the opening reversal.\",\"reason\":\"The aligned word is tagged as a particle with no root, while its grammar carries rebuke and reversal.\",\"representative_source_ids\":[\"QF-baa486e8\",\"QI-d06bd1a5\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000482/B001","root_000482/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000482","role":"Crushing through demolition supplies the destructive operation and its endpoint in levelling.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B002","mapped_root_id":"root_000482","role":"Flat low spread supplies the resulting geometry after the repeated operation.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B001","mapped_root_id":"root_000025","role":"The lower ground opposite the sky identifies both the material target and the vertical baseline.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]}],"changed_reading":{"after":"The earth is processed to completion until every protruding difference is reduced to one lower plane.","before":"The earth receives an overwhelmingly violent blow."},"confidence":"strong","focus_anchor":"The passive operation at word 3 targets the earth at word 4 and is reiterated by the cognate nouns at words 5-6.","mechanism":"Repeated crushing does not stop at damage: it removes raised form until the lower member opposite the sky becomes one flat plane. The three occurrences of the same root make levelling the saturated endpoint of the operation.","model_id":"b_crush_to_plane"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_crush_to_plane","source_type":"hft","support_id":"sup_a940d452a99401e00bee","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000482/B006","root_000482/B008"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_000482","role":"Crowding and mutual pressure convert repetition into accumulating lateral compression.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B006","mapped_root_id":"root_000482","role":"Heavy strength and hard tread supply the downward load borne by the surface.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B001","mapped_root_id":"root_000025","role":"Ground supplies the common load-bearing plane on which crowding and tread converge.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]}],"changed_reading":{"after":"Converging mass and heavy tread compact the common ground under an intolerable load.","before":"Separate impacts strike a passive landscape."},"confidence":"medium","focus_anchor":"The repeated root at words 3, 5, and 6 permits the event to be heard as accumulated pressure as well as successive blows.","mechanism":"Crowding and hard tread make the repetition bidirectional: force descends onto the ground while masses converge across it. The earth is therefore not only broken but overloaded by compacting weight.","model_id":"b_pressing_mass"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_pressing_mass","source_type":"hft","support_id":"sup_04213bd4a2b53768737f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B001","root_000482/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000482","role":"Heaping soil and filling a cavity supply the covering and sealing operation.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B001","mapped_root_id":"root_000025","role":"The ground becomes the paradoxical patient of the operation normally performed with ground.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]}],"changed_reading":{"after":"The covering ground is itself filled over and sealed, a burial of the ordinary medium of burial.","before":"The surface is smashed from above."},"confidence":"exploratory","focus_anchor":"The passive earth at word 4 can receive the soil-covering branch carried by the repeated root around it.","mechanism":"The usual covering medium becomes the covered object. Repetition turns the event into filling and sealing: the ground that normally buries bodies or closes wells is itself buried over.","model_id":"b_burial_inversion"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_burial_inversion","source_type":"hft","support_id":"sup_128aad8e82588a4803b9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا","ayah_ref":"89:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000025/B005","root_000482/B005"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_000482","role":"The bench or platform image supplies a product made by the levelling event.","root":"د ك ك","source_ref":"89:21","source_word_indices":["3","5","6"]},{"branch_id":"B005","mapped_root_id":"root_000025","role":"The thick mat image makes the earth a spread substrate rather than only damaged matter.","root":"ء ر ض","source_ref":"89:21","source_word_indices":["4"]}],"changed_reading":{"after":"The removal of terrain simultaneously produces a broad platform-like substrate.","before":"The event leaves only ruins."},"confidence":"exploratory","focus_anchor":"The result nouns at words 5-6 allow a product-like surface reading alongside the event reading.","mechanism":"A platform branch in the repeated root and a thick-mat branch in the earth root converge on a made substrate. Destruction and preparation coexist: the old terrain is removed while a broad surface is produced.","model_id":"b_prepared_surface"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_prepared_surface","source_type":"hft","support_id":"sup_7892890c2ad85c8d7e9f","trust":"legacy_unbound"}]}
</lane_packet_json>
