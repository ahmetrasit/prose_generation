# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:7",
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
{"branch_registry":[{"boundary":"Anlam, fiziksel dayama ve dik direk anlamlarından ayrılır; özel kalıplar çıplak kullanıma genellenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B001","candidate_links":[{"candidate_id":"cand_147167b5b7178d4856e1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"isteyerek yönelme ve bilerek yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eylem, yanlışlıkla ya da dalgınlıkla değil, bilinçli bir seçimle gerçekleştirilir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişiye veya şeye isteyerek yönelme, bu çekirdeğin yöneltili kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıp, işi ciddi, kesin ve bütünüyle bilerek yapmayı anlatır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel çekirdeği, hem hedefe yönelmeyi hem de eylemin yanlışlıkla yapılmamasını belirtmek gerektiğinde karşılar.","boundary_detail":"Anlam, fiziksel dayama ve dik direk anlamlarından ayrılır; özel kalıplar çıplak kullanıma genellenmez.","branch_image_ar":"القصد المتعمد","concept_gloss":"isteyerek yönelme ve bilerek yapma","contextual_glosses":[{"applicability":"Bir eylemin yanlışlıkla değil, bilinçli olarak yapıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin bilinçli ve isteyerek yapılmış olmasını korur."},"facet_ids":["F001"],"text":"bunu bile isteye yaptı","usage_role":"contextual"}],"definition":"Bir kişiye ya da şeye isteyerek yönelmek veya bir işi yanılma ve dalgınlık olmadan bilerek yapmaktır. Belirli bir kalıp, bu bilinçli yapışı ciddiyet ve kesinlikle güçlendirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eylem, yanlışlıkla ya da dalgınlıkla değil, bilinçli bir seçimle gerçekleştirilir."},{"facet_id":"F002","role":"specialization","statement":"Bir kişiye veya şeye isteyerek yönelme, bu çekirdeğin yöneltili kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir kalıp, işi ciddi, kesin ve bütünüyle bilerek yapmayı anlatır."}],"identity_rationale":"Kaynak anlatımı, bir kişiye ya da şeye isteyerek yönelmeyi ve bir işi dalgınlıkla veya yanlışlıkla değil bilerek yapmayı açıkça birlikte verir. Güçlü kararlılık bildiren kalıp ise bu çekirdeğin özel bir gerçekleşmesidir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeye isteyerek yönelmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yanlışlıkla değil, bilerek yapılan eylem"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bile isteye, ciddiyetle ve kesinlikle"}],"lexicalization_note":"Tanım, genel bilerek yapma çekirdeğini yönelme ve güçlü kesinlik bildiren kalıba bağlı kullanımlardan ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sınırı en açık biçimde gösteren yönelme ve seçme komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, yönelmenin yanında eylemin bilinçli yapılmasını da kapsar; komşu dal ise seçenekler arasından birini ayırıp yalnız ona yönelmeyi öne çıkarır.","focus_only":"Bir işi yanlışlıkla değil bilerek yapma karşıtlığını da içerir.","gloss":"seçerek yönelme","neighbor_only":"Seçilen şeyden başkasını istememe ve yalnız ona gitme vurgusu taşır.","neighbor_ref":"root_001049/B009","relation_type":"near_synonym","shared_zone":"Her ikisi de belirli bir hedefe istek ve seçimle yönelmeyi anlatır."}],"source_phrase_ar":"عمدت فلانا إذا قصدت إليه (maqayis); عمدت فلانا أي قصدته وتعمدته (ayn); عمدت للشئ قصدت له وهو نقيض الخطاء (sihah); عمدت للشيء إذا قصدت له (tahdhib); العمد والتعمد خلاف السهو (mufradat)","source_summary":"Kaynaklar, isteyerek yönelme ile yanlışlık ve dalgınlığın karşıtı olan bilinçli yapma üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قصد الشيء وتعمده وفعل الأمر عمدا أو معتمدا","what_is_not_ar":"ليس إسناد الشيء بعماد ولا العمود الحسي"},"support_links":["sup_14444bd6493996e6672c"]},{"boundary":"Bu dal, desteğin kendisini adlandıran daldan ve istemli yönelme anlamından ayrılır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B002","candidate_links":[{"candidate_id":"cand_474be92bd565b6e4974c","lane":"micro"},{"candidate_id":"cand_147167b5b7178d4856e1","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"dayanak koyarak destekleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, yaslandığı ya da altına konduğu dayanak aracılığıyla desteklenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş biçim, nesnenin altına taşıyıcı destek koyma işlemini özellikle belirtir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin başka bir taşıyıcıya yaslanarak veya altından desteklenerek ayakta tutulduğu durumları karşılar.","boundary_detail":"Bu dal, desteğin kendisini adlandıran daldan ve istemli yönelme anlamından ayrılır.","branch_image_ar":"إسناد الشيء بعماد","concept_gloss":"dayanak koyarak destekleme","contextual_glosses":[{"applicability":"Duvar gibi fiziksel bir nesnenin devrilmemesi için dıştan dayandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesnenin fiziksel bir dayanakla tutulmasını açıkça korur."},"facet_ids":["F001"],"text":"duvarı payandayla destekledi","usage_role":"contextual"}],"definition":"Bir nesneyi, dayandığı bir destekle ayakta tutmak veya altına onu taşıyacak bir dayanak yerleştirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, yaslandığı ya da altına konduğu dayanak aracılığıyla desteklenir."},{"facet_id":"F002","role":"specialization","statement":"Türemiş biçim, nesnenin altına taşıyıcı destek koyma işlemini özellikle belirtir."}],"identity_rationale":"Kaynak anlatımı, bir nesneyi dayamak, ayakta tutmak ve altına onu taşıyan bir destek koymak işlemlerini doğrudan bildirir. Dalın kimliği destek nesnesinden çok bu destekleme eylemidir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"nesneyi dayayıp desteklemek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"nesnenin altına dayanak koymak"}],"lexicalization_note":"Tanım, nesneyi destekleme eylemini ve altına destek koyduran biçimi kapsar; bunları destek nesnesinin adıyla karıştırmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eylem olarak desteklemeye en çok yaklaşan komşu sınır karşılaştırması için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal fiziksel dayama işlemiyle sınırlıdır; komşu dal ise fiziksel desteğin yanı sıra yardım ve iş birliğini de kapsayan daha geniş bir destek alanına sahiptir.","focus_only":"Fiziksel bir nesneyi taşıyan desteğin yerleştirilmesini özellikle bildirir.","gloss":"destekleme ve yardım","neighbor_only":"Yardım etme, birlikte güç verme ve kişiler arası destek alanına da yayılır.","neighbor_ref":"root_000554/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da zayıf veya yük taşıyan bir şeyin güçlendirilmesi vardır."}],"source_phrase_ar":"تعمد الشيء بعماد يمسكه ويعتمد عليه (maqayis;ayn); عمدت الشيء أسندته (maqayis;mufradat); أقمته بعماد يعتمد عليه وأعمدته جعلت تحته عمدا (sihah); عمدت الحائط إذا دعمته (tahdhib)","source_summary":"Kaynaklar, nesneyi bir dayanağa yaslayarak destekleme ve altına destek yerleştirme işlemlerini ortak biçimde aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه إقامة الشيء ودعمه بعماد يعتمد عليه وجعل العمد تحته","what_is_not_ar":"ليس القصد بالنية ولا العمود اسما للخشبة نفسها"},"support_links":["sup_14444bd6493996e6672c","sup_916521bbd784ed36a48f"]},{"boundary":"Dal, destekleme eylemini değil dik destek parçasını adlandırır; özel ateş kalıbı genel nesne anlamına katılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B003","candidate_links":[{"candidate_id":"cand_474be92bd565b6e4974c","lane":"micro"},{"candidate_id":"cand_d8d83c9c69457e20eed7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"taşıyıcı dik direk veya sütun","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, bir yapıyı taşıyan veya ona dayanma sağlayan dik parçadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Direk; ahşap, demir ya da mermer sütun gibi farklı maddi gerçekleşmelere sahip olabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel bir kalıp, uzatılmış ateş sütunlarını veya ateşten çadır benzeri yapıları anlatır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir yapıyı ya da çadırı dik tutan, çeşitli maddelerden yapılabilen taşıyıcı parça için uygundur.","boundary_detail":"Dal, destekleme eylemini değil dik destek parçasını adlandırır; özel ateş kalıbı genel nesne anlamına katılmaz.","branch_image_ar":"العمود والعماد","concept_gloss":"taşıyıcı dik direk veya sütun","contextual_glosses":[{"applicability":"Çadırın ortasında dik durup örtüyü taşıyan ahşap parça söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çadır bağlamını, orta konumu ve taşıyıcı işlevi korur."},"facet_ids":["F001"],"text":"çadırın orta direği","usage_role":"contextual"}],"definition":"Bir yapı, çadır veya başka bir düzenek için dik duran ve yükü taşıyan direk ya da sütundur. Belirli bir anlatımda uzatılmış ateş sütunlarına veya ateşten çadırı andıran yapılara da uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, bir yapıyı taşıyan veya ona dayanma sağlayan dik parçadır."},{"facet_id":"F002","role":"extension","statement":"Direk; ahşap, demir ya da mermer sütun gibi farklı maddi gerçekleşmelere sahip olabilir."},{"facet_id":"F003","role":"associated_use","statement":"Özel bir kalıp, uzatılmış ateş sütunlarını veya ateşten çadır benzeri yapıları anlatır."}],"identity_rationale":"Kaynak anlatımı, yapı veya çadır gibi bir şeyi taşıyan dik parçayı; bunun ahşap, demir, mermer ve benzeri maddelerden olabilen türlerini verir. Ateşten uzatılmış dik parçalar anlatımı bu nesne çekirdeğinin özel bir benzetmeli kullanımıdır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"dayanak veya taşıyıcı direk"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ahşap, demir ya da taş sütun"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"uzatılmış ateş sütunları içinde"}],"lexicalization_note":"Tanım, dik destek nesnesini temel alır ve uzatılmış ateş parçaları bildiren kalıbı ayrı bir özel kullanım olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; taşıyıcı nesne sınırına en yakın sütun dalı yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal malzeme ve kullanım bakımından daha geniştir ve çadır direğini de içerir; komşu dal daha çok taş ya da tuğladan yapılmış sütun türüne bağlıdır.","focus_only":"Çadır direğini ve demir, ahşap ya da ateş gibi daha geniş gerçekleşmeleri kapsar.","gloss":"taş veya tuğla sütun","neighbor_only":"Taş veya tuğladan yapılmış silindir biçimli sütunu özellikle öne çıkarır.","neighbor_ref":"root_000702/B005","relation_type":"near_synonym","shared_zone":"Her ikisi de dik duran sütun veya direk türü bir yapı parçasını adlandırır."}],"source_phrase_ar":"الشيء الذي يسند إليه عماد وجمع العماد عمد والعمود من خشب أو حديد (maqayis); عمود الخباء من خشب قائم في الوسط (ayn); العمود عمود البيت وجمعه أعمدة وعمد (sihah); العمد أساطين الرخام وفي عمد من النار (tahdhib); العمود خشب تعتمد عليه الخيمة وجمعه عمد (mufradat)","source_summary":"Kaynaklar, taşıyıcı dik parçayı ve onun yapı ile çadırdaki örneklerini ortaklaştırır; ateşten uzatılmış parçalar özel bir anlatımdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العمود والعماد والأعمدة والعمد من خشب أو حديد أو نار أو رخام وما يقوم عليه البيت أو الخباء","what_is_not_ar":"ليس فعل القصد ولا السيد المعتمد عليه"},"support_links":["sup_916521bbd784ed36a48f","sup_ba7ed5f2baaf4b1f8089"]},{"boundary":"Anlam yalnızca verilen topluluk adlandırmasına bağlıdır; her çadır sakini veya her çadır kümesi bununla karşılanmaz.","branch_kind":"non_bare","branch_ref":"root_001043/B004","candidate_links":[{"candidate_id":"cand_d8d83c9c69457e20eed7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"yalnız çadırlarda yaşayan topluluk","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Topluluk, barınma ve konaklama biçimi olarak yalnızca çadırları kullanmasıyla tanımlanır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu topluluk otlaklara doğru yer değiştiren çadır sahipleri olarak da betimlenir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çadırı sürekli barınma biçimi olarak kullanan ve başka konak türlerine yerleşmeyen topluluk için uygundur.","boundary_detail":"Anlam yalnızca verilen topluluk adlandırmasına bağlıdır; her çadır sakini veya her çadır kümesi bununla karşılanmaz.","branch_image_ar":"أهل العمود والعماد","concept_gloss":"yalnız çadırlarda yaşayan topluluk","contextual_glosses":[{"applicability":"Bağlam, başka konak türü kullanmayan çadır sahiplerini zaten belirtiyorsa kısa karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çadırlarda yaşayan insan topluluğu anlamını bağlam içinde korur."},"facet_ids":["F001"],"text":"çadır halkı","usage_role":"contextual"}],"definition":"Çadırlarda yaşayan ve başka tür konaklara yerleşmeyen çadır halkıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Topluluk, barınma ve konaklama biçimi olarak yalnızca çadırları kullanmasıyla tanımlanır."},{"facet_id":"F002","role":"associated_use","statement":"Bu topluluk otlaklara doğru yer değiştiren çadır sahipleri olarak da betimlenir."}],"identity_rationale":"Kaynak anlatımı, çadırlarda yaşayan ve başka tür konaklara yerleşmeyen topluluğu açıkça tanımlar. Bu nedenle dal, çadırın kendisine değil, bu yaşam biçimiyle belirlenen insan grubuna aittir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başka yerde konaklamayan çadır halkı"}],"lexicalization_note":"Tanım, yalnızca çadır halkını bildiren yerleşik söz öbeğine bağlı kalır ve bağımsız bir kök anlamı varsaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; topluluk ile çadır yerleşimi arasındaki en olası karışıklık yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal yerleşim düzenini değil, çadırdan başka yerde kalmayan insan topluluğunu anlatır; komşu dal ise insanların kimliğinden çok bir araya gelmiş barınakları anlatır.","focus_only":"İnsanları, yalnızca çadırlarda yaşamaları bakımından sınıflandırır.","gloss":"çadır ve ev kümesi","neighbor_only":"Birbirine yakın tek bir çadırı veya çadır ve ev kümesini yerleşim olarak adlandırır.","neighbor_ref":"root_000374/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da çadırlı yaşama ve yerleşme alanıyla ilişkilidir."}],"source_phrase_ar":"أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها (maqayis;ayn); كانوا أهل عمد ينتقلون إلى الكلأ (tahdhib); أصحاب الأخبية الذين لا ينزلون غيرها (tahdhib)","source_summary":"Kaynaklar, başka tür konaklara yerleşmeyip çadırlarda yaşayan insanları belirten topluluk adında birleşir.","sources":["MQ","AY","TA"],"what_is_ar":"يدخل فيه أصحاب الأخبية وأهل العمود أو العماد الذين لا ينزلون غيرها","what_is_not_ar":"ليس كل عماد بمعنى أهل الخباء ولا تفسير ذات العماد بالطول"},"support_links":["sup_ba7ed5f2baaf4b1f8089"]},{"boundary":"Anlam yalnızca verilen uzunluk ve yücelik kalıplarına bağlıdır; her direk veya her yükselme bu dala girmez.","branch_kind":"collocation","branch_ref":"root_001043/B005","candidate_links":[{"candidate_id":"cand_474be92bd565b6e4974c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"kalıba bağlı uzunluk ve yücelik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, belirli söz öbeklerinde uzunluk veya yükseklik niteliğini bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Uzunluk bildiren kalıp, kişinin boyuna veya ziyaretçilere uzaktan görünen yüksek evine yorumlanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yücelik bildiren kalıp, kişinin başkalarınca güvenilir dayanak sayılan yüksek konumunu anlatabilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca sağlanan söz öbeklerinin kişi boyu, yüksek yapı veya dayanılan yüksek konum yorumlarını topluca göstermek için uygundur.","boundary_detail":"Anlam yalnızca verilen uzunluk ve yücelik kalıplarına bağlıdır; her direk veya her yükselme bu dala girmez.","branch_image_ar":"الطول والرفعة في العماد","concept_gloss":"kalıba bağlı uzunluk ve yücelik","contextual_glosses":[{"applicability":"Uzunluk kalıbının kişinin ziyaretçilerince kolay görülen yüksek konutunu anlattığı yorumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksekliği, görünürlüğü ve kişiyle bağlantılı konut yorumunu korur."},"facet_ids":["F002"],"text":"yüksek ve uzaktan görünen ev sahibi","usage_role":"explanatory"}],"definition":"Verilen söz öbeklerinde bir kişinin uzunluğunu, yüksek ve görünür yapısını ya da başkalarının dayandığı yüce konumunu anlatır; hangi yorumun geçerli olduğu kalıba ve bağlama bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, belirli söz öbeklerinde uzunluk veya yükseklik niteliğini bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Uzunluk bildiren kalıp, kişinin boyuna veya ziyaretçilere uzaktan görünen yüksek evine yorumlanabilir."},{"facet_id":"F003","role":"source_variant","statement":"Yücelik bildiren kalıp, kişinin başkalarınca güvenilir dayanak sayılan yüksek konumunu anlatabilir."}],"identity_rationale":"Kaynak anlatımı, verilen kalıplarda uzunluk, yüksek yapı ve bir kişinin dayanak olarak yüceliği gibi birbirine bağlı fakat aynı olmayan yorumlar aktarır. Dal korunabilir, ancak bunlar bağımsız bir genel yükselme anlamı olarak birleştirilemez.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"uzun boylu veya evi uzaktan görünen"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dayanak sayılan yüce kişi"}],"lexicalization_note":"Tanım, uzunluk ve yücelik yorumlarını yalnızca sağlanan söz öbeklerine bağlar ve çıplak köke genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıba bağlı yüceliği genel fiziksel yükselmeden ayıran komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kalıba bağlı kişi, konut ve saygınlık yorumları taşır; komşu dal ise nesnelerin genel olarak yükselmesi ve uzamasıyla ilgilidir.","focus_only":"Uzunluk ve yüceliği yalnızca belirli kişi ve yapı kalıplarında bildirir.","gloss":"genel yükselme ve uzama","neighbor_only":"Nesnenin yükselmesi, boyun uzaması ve yukarı çıkma gibi genel fiziksel yükselmeyi kapsar.","neighbor_ref":"root_000742/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da uzunluk veya yukarıda bulunma düşüncesi vardır."}],"source_phrase_ar":"رجل معمد أي طويل والعماد الطول (maqayis); العماد الأبنية الرفيعة وفلان طويل العماد (sihah); ذات العماد أي ذات الطول وقيل ذات البناء الرفيع (tahdhib)","source_summary":"Kaynaklar, kalıpları uzunluk ve yükseklik çevresinde toplar; kişi boyu, yüksek yapı, görünür konut ve dayanılan yüce konum yorumları bağlama göre ayrışır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العماد بمعنى الطول والبناء الرفيع والمنزل الظاهر العالي","what_is_not_ar":"ليس أصحاب الأخبية إلا في تفسير آخر وليس مجرد خشبة العمود"},"support_links":["sup_916521bbd784ed36a48f"]},{"boundary":"Bu dal fiziksel direği değil, bir topluluğun ya da işin güvenilir insanî veya soyut dayanağını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B006","candidate_links":[{"candidate_id":"cand_3682dfe1a4128f9e0b43","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"güvenilip dayanılan önder veya temel unsur","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ya da unsur, başkalarının güvenip dayandığı başlıca başvuru noktasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Topluluk bağlamında bu dayanak, onların önderi ve işlerinde başvurduğu kişidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Daha genel biçim, güvenilen bir kişi yanında malı veya işi de dayanak olarak gösterebilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir topluluğun başvurduğu kişi veya bir işin güvenilir başlıca dayanağı anlatıldığında kullanılır.","boundary_detail":"Bu dal fiziksel direği değil, bir topluluğun ya da işin güvenilir insanî veya soyut dayanağını anlatır.","branch_image_ar":"المعتمد عليه في القوم","concept_gloss":"güvenilip dayanılan önder veya temel unsur","contextual_glosses":[{"applicability":"Bir grubun işlerinde başvurduğu ve kendisine dayandığı baş kişi söz konusu olduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önderliği ve topluluğun ona güvenip dayanmasını korur."},"facet_ids":["F001","F002"],"text":"topluluğun güvendiği önder","usage_role":"contextual"}],"definition":"Bir topluluğun güvenip başvurduğu önder veya bir işte kendisine dayanılan kişi, mal ya da temel unsurdur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ya da unsur, başkalarının güvenip dayandığı başlıca başvuru noktasıdır."},{"facet_id":"F002","role":"specialization","statement":"Topluluk bağlamında bu dayanak, onların önderi ve işlerinde başvurduğu kişidir."},{"facet_id":"F003","role":"extension","statement":"Daha genel biçim, güvenilen bir kişi yanında malı veya işi de dayanak olarak gösterebilir."}],"identity_rationale":"Kaynak anlatımı, topluluğun başındaki kişiyi yalnızca yönetici olarak değil, insanların güvenip başvurduğu dayanak olarak tanımlar. Daha genel biçim kişi, mal veya iş gibi güvenilen dayanaklara da uzanır.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"topluluğun güvendiği önder"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"güvenilip dayanılan kişi, mal veya temel unsur"}],"lexicalization_note":"Tanım, topluluk önderini bildiren söz öbeğiyle kişi, mal veya iş için kullanılan daha genel dayanak biçimini ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; önderlik ile güvenilir dayanak arasındaki sınırı en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda önderlik, insanların o kişiye güvenip dayanmasıyla kurulur; komşu dal yalnızca topluluğun baş kişisi olma konumunu bildirir.","focus_only":"Önderi, topluluğun güvenip dayandığı başvuru kişisi olmasıyla tanımlar.","gloss":"topluluk başı","neighbor_only":"Topluluğun baş kişisini, güvenilir dayanak olma koşulunu belirtmeden adlandırır.","neighbor_ref":"root_001571/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da topluluğun başında bulunan kişiyi anlatabilir."}],"source_phrase_ar":"عميد القوم سيدهم ومعتمدهم (maqayis); عميد القوم سيدهم الذي يعتمدون عليه (ayn); عميد القوم وعمودهم سيدهم والعمدة ما يعتمد عليه (sihah); فلان عمدة قومه إذا كانوا يعتمدونه (tahdhib); العميد السيد الذي يعمده الناس (mufradat)","source_summary":"Kaynaklar, topluluğun güvendiği önder ile kişi, mal veya iş olarak dayanılan temel unsur düşüncesinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العميد والعمدة والسيد ومن يعتمد عليه القوم عند الأمر","what_is_not_ar":"ليس العمود الحسي ولا الوجع الذي يعمد الإنسان"},"support_links":["sup_bac52f2a61736fb54294"]},{"boundary":"Her kullanım kendi söz öbeğine bağlıdır; bir örneğin özel özelliği bütün dala genellenmez.","branch_kind":"collocation","branch_ref":"root_001043/B007","candidate_links":[{"candidate_id":"cand_3682dfe1a4128f9e0b43","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"kalıba göre ana, orta veya uzunlamasına parça","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz öbeği, ilgili bütünün ana taşıyıcı, orta veya uzunlamasına uzanan bölümünü seçer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İş ve görüş bağlamında, bütünün düzgün yürümesini sağlayan temel dayanağı belirtir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kulak, mızrak ucu, karın, sırt, karaciğer, ana damar ve kılıçta orta, ana veya uzanan yapısal parçayı belirtir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tan ışığının ilk yayılışı ve erkek devekuşunun direğe benzetilen bacakları da bu adlandırmaya girer."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilen iş, organ, silah, tan ve hayvan söz öbeklerinin ortak yapısal benzerliğini belirtmek için uygundur.","boundary_detail":"Her kullanım kendi söz öbeğine bağlıdır; bir örneğin özel özelliği bütün dala genellenmez.","branch_image_ar":"قوام الشيء ووسطه","concept_gloss":"kalıba göre ana, orta veya uzunlamasına parça","contextual_glosses":[{"applicability":"Bir işin onsuz düzgün yürümeyeceği ana dayanağı anlatan söz öbeğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşin ayakta kalmasını sağlayan temel unsur anlamını korur."},"facet_ids":["F002"],"text":"işin belkemiği","usage_role":"contextual"}],"definition":"Verilen söz öbeklerinde bir şeyin ayakta kalmasını sağlayan ana unsurunu, orta ya da uzunlamasına bölümünü veya direğe benzetilen belirgin parçasını anlatır. Tam karşılık, iş, organ, silah, tan ışığı ya da hayvan bacağı bağlamına göre değişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz öbeği, ilgili bütünün ana taşıyıcı, orta veya uzunlamasına uzanan bölümünü seçer."},{"facet_id":"F002","role":"specialization","statement":"İş ve görüş bağlamında, bütünün düzgün yürümesini sağlayan temel dayanağı belirtir."},{"facet_id":"F003","role":"specialization","statement":"Kulak, mızrak ucu, karın, sırt, karaciğer, ana damar ve kılıçta orta, ana veya uzanan yapısal parçayı belirtir."},{"facet_id":"F004","role":"extension","statement":"Tan ışığının ilk yayılışı ve erkek devekuşunun direğe benzetilen bacakları da bu adlandırmaya girer."}],"identity_rationale":"Kaynak anlatımı yalnızca tek bir genel orta parça anlamı vermez; işin ayakta kalmasını sağlayan ana unsur, organ ve araçların orta ya da uzunlamasına bölümü, tan ışığının başlangıcı ve benzetmeli bacak adları gibi kalıba bağlı kullanımları sıralar. Dal bu ortak dikey, orta veya taşıyıcı benzerlik altında korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"işin belkemiği ve ana dayanağı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kulağın ana ve büyük bölümü"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"mızrak ucunun iki ağzı arasındaki orta bölüm"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"karında uzanan damar veya gövdeyi taşıyan sırt"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"karaciğeri besleyen damar ve ana atardamar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tan ışığının ilk yayılışı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kılıç sırtının ortasındaki uzun çizgi"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"erkek devekuşunun direğe benzeyen iki bacağı"}],"lexicalization_note":"Tanım yalnızca verilen söz öbeklerini kapsar; orta, ana veya uzunlamasına bölüm anlamını bağımsız bir sözcük anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; orta bölüm ile ana dayanak kapsamlarını ayıran en yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal, orta bölüm yanında bir işin ana dayanağını ve başka benzetmeli kalıpları da içerir; komşu dal belirli beden ve silah bölümleriyle sınırlı ayrı bir adlandırmadır.","focus_only":"Ana dayanak, tan ışığı ve çok sayıda kalıba bağlı orta parça kullanımını kapsar.","gloss":"gövde veya sapın orta kesimi","neighbor_only":"Hayvan gövdesi ile ok veya mızrak sapının belirli orta kesimlerini kendi adlarıyla belirtir.","neighbor_ref":"root_000634/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir bedenin ya da uzun nesnenin orta bölümünü seçebilir."}],"source_phrase_ar":"عمود الأمر قوامه (maqayis;ayn); عمود الأذن معظمها وقوامها (maqayis;ayn;tahdhib); عمود السنان ما توسط شفرتيه (maqayis;ayn;tahdhib); عمود البطن شبه عرق ممدود (maqayis;ayn;tahdhib); عمود الكبد عرق يسقيها وعمود السحر الوتين (maqayis;ayn;tahdhib); عمود الصبح ابتداء ضوئه (sihah;mufradat); عمود السيف الشطيبة في وسط متنه (tahdhib)","source_summary":"Toplu anlatım, ana dayanak ile orta veya uzunlamasına parça düşüncesini çeşitli söz öbeklerinde birleştirir; organ, silah, tan ve hayvan örneklerinin kapsamı kendi bağlamlarıyla sınırlıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه عمود الأمر وقوامه وعمود الأذن والسنان والسيف والبطن والكبد والسحر والصبح وما شاكل ذلك من معظم الشيء أو وسطه","what_is_not_ar":"ليس السيد المعتمد عليه ولا الخباء نفسه"},"support_links":["sup_bac52f2a61736fb54294"]},{"boundary":"Dal, sıradan ağrıdan daha ağır biçimde güçten düşürme ve ezme sonucunu içerir; hayvan hörgücü yaralanması ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"acıyla ezilip güçten düşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Acı veren durum, kişiyi yalnız incitmekle kalmaz, onu ağırlaştırıp gücünü kırar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hasta kişi, destek almadan oturamayacak ölçüde güçsüz düşebilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ezici etki, sevgi acısı veya derin üzüntüyle yıkılmış yürek için de kullanılır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hastalık veya duygusal acının kişiyi ağır biçimde tükettiği ve olağan gücünü kırdığı durumları karşılar.","boundary_detail":"Dal, sıradan ağrıdan daha ağır biçimde güçten düşürme ve ezme sonucunu içerir; hayvan hörgücü yaralanması ayrı daldadır.","branch_image_ar":"وجع يهد ويفدح","concept_gloss":"acıyla ezilip güçten düşme","contextual_glosses":[{"applicability":"Hastalığın kişiyi ağır biçimde güçsüz ve bitkin bıraktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hastalığın sürüklediği ağır güç kaybını ve yıpranmayı korur."},"facet_ids":["F001","F002"],"text":"hastalık onu tüketti","usage_role":"contextual"}],"definition":"Hastalık, üzüntü veya sevgi acısının bir kişiyi ya da yüreğini ezip güçten düşürmesi ve ağır biçimde acıtmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Acı veren durum, kişiyi yalnız incitmekle kalmaz, onu ağırlaştırıp gücünü kırar."},{"facet_id":"F002","role":"specialization","statement":"Hasta kişi, destek almadan oturamayacak ölçüde güçsüz düşebilir."},{"facet_id":"F003","role":"extension","statement":"Aynı ezici etki, sevgi acısı veya derin üzüntüyle yıkılmış yürek için de kullanılır."}],"identity_rationale":"Kaynak anlatımı, hastalık yüzünden oturamayacak kadar güçten düşen kişiyi ve sevgi, üzüntü ya da hastalığın ezdiği kişiyi veya yüreği ortak bir ağır acı çekirdeğinde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"oturamayacak kadar güçten düşmüş hasta"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sevgi veya üzüntü acısıyla yıkılmış yürek"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"hastalık onu tüketip acıttı"}],"lexicalization_note":"Tanım, güçten düşmüş hasta biçimini, ezilmiş yürek kalıbını ve hastalığın kişiyi tüketmesi kullanımını ayrı görünümler olarak korur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ağır güç kaybını genel hastalık ve ağrıdan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ağır acının ezici ve güçten düşürücü sonucunu zorunlu kılar; komşu dal bu dereceyi gerektirmeyen genel hastalık ve ağrı alanıdır.","focus_only":"Acının kişiyi ezip destek almadan oturamayacak kadar güçten düşürmesini içerir.","gloss":"hastalık ve ağrı","neighbor_only":"Genel hastalık, ağrıdan yakınma ve ağrıyan organ anlatımlarını da kapsar.","neighbor_ref":"root_000814/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da hastalık ve bedensel acı yaşayan kişiyi anlatabilir."}],"source_phrase_ar":"العميد الرجل المعمود لا يستطيع الجلوس من مرضه (maqayis;ayn;tahdhib); القلب العميد المعمود المشعوف الذي هده العشق (maqayis;ayn); عمد المرض فدحه (sihah); المعمود الحزين الشديد الحزن وما يعمدك أي ما يوجعك (tahdhib); القلب الذي يعمده الحزن والسقيم الذي يعمده السقم (mufradat)","source_summary":"Kaynaklar, hastalık, üzüntü veya sevgi acısının kişiyi ya da yüreğini ağır biçimde ezmesi ve güçten düşürmesi üzerinde birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المريض المعمود والعميد والقلب الذي هده العشق أو الحزن والسقم الذي يضني صاحبه","what_is_not_ar":"ليس نية العمد ولا عماد الخباء ولا فساد سنام البعير نفسه"},"support_links":[]},{"boundary":"Dal yalnızca verilen hayvan ve yara kalıplarını kapsar; insanın hastalıkla güçten düşmesi bu dala girmez.","branch_kind":"collocation","branch_ref":"root_001043/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"baskıyla içten zedelenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Baskı veya sıkma, dokuda dıştan hemen anlaşılmayabilen bir zedelenme oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Binme yükü, büyük hörgücün iç yapısını çökertip bozabilir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Olgunlaşmadan sıkılan yara, bu müdahalenin ardından şişer."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca hörgücün yükten içten çökmesi ve yaranın erken sıkılınca şişmesi biçimindeki iki sağlanmış bağlamı topluca karşılar.","boundary_detail":"Dal yalnızca verilen hayvan ve yara kalıplarını kapsar; insanın hastalıkla güçten düşmesi bu dala girmez.","branch_image_ar":"انشداح السنام والجرح","concept_gloss":"baskıyla içten zedelenme","contextual_glosses":[{"applicability":"Uzun süre binme veya yük baskısıyla hörgücün iç kısmı bozulmuş deve için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanı, yük nedenini ve hörgücün içten bozulmasını korur."},"facet_ids":["F001","F002"],"text":"yükten hörgücü içten çökmüş deve","usage_role":"contextual"}],"definition":"Verilen söz öbeklerinde baskı yüzünden içten zedelenmeyi anlatır: binme yükü bir devenin hörgücünü dışı sağlam görünürken içten çökertir ya da erken sıkılan yara şişer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Baskı veya sıkma, dokuda dıştan hemen anlaşılmayabilen bir zedelenme oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Binme yükü, büyük hörgücün iç yapısını çökertip bozabilir."},{"facet_id":"F003","role":"specialization","statement":"Olgunlaşmadan sıkılan yara, bu müdahalenin ardından şişer."}],"identity_rationale":"Kaynak anlatımı, binme baskısıyla hörgücün içten çökmesi ile olgunlaşmadan sıkılan yaranın şişmesini iki ayrı söz öbeğinde verir. Bunların ortak noktası baskı sonucu oluşan iç zedelenmedir; tek bir genel yara türüymüş gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"binme yükünden hörgücü içten çökmüş deve"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"erken sıkıldığı için şişen yara"}],"lexicalization_note":"Tanım, hörgüç ve yara kullanımlarını kendi söz öbeklerine bağlar; ortak zedelenme çekirdeğini bağımsız bir çıplak anlama dönüştürmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli baskı sonucunu genel deri şişliği ve izlerinden ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir baskı ya da sıkma sürecine ve onun sonucuna bağlıdır; komşu dal çok çeşitli deri çıkıntılarını ve izlerini daha geniş biçimde adlandırır.","focus_only":"Baskının hörgüçte iç çökme veya erken sıkılan yarada şişme oluşturmasını gerektirir.","gloss":"deri kabartısı ve yara izi","neighbor_only":"Çeşitli deri kabartıları, çıbanlar, deri bozulmaları ve darbe izlerini neden sınırlaması olmadan kapsar.","neighbor_ref":"root_000228/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bedende beliren yara, şişlik veya doku bozulması bulunabilir."}],"source_phrase_ar":"السنام إذا كان ضخما فحمل عليه فكسر وبعير عمد وناقة عمدة (maqayis); عمد البعير إذا انفضح داخل سنامه من الركوب (sihah); العمد في السنام أن ينشدخ انشداخا والجرح العمد الذي يعصر فيرم (tahdhib); عمد البعير توجع من عقر ظهره (mufradat)","source_summary":"Toplu anlatım, binme baskısıyla içten bozulan hörgüç ile erken sıkıldıktan sonra şişen yarayı kalıba bağlı iki zedelenme olarak verir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه بعير عمد وناقة عمدة إذا فسد السنام من الركوب أو انشدخ وبقي ظاهره صحيحا ويدخل فيه الجرح العمد الذي يعصر فيرم","what_is_not_ar":"ليس مرض الإنسان أو حزنه إلا بالتشبيه عند بعض المصادر"},"support_links":[]},{"boundary":"Gerekli sınır, yağmurun derine işlemesi ve nemli toprağın birleşip topaklanmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001043/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"yağmurla derinden ıslanıp topaklanan toprak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yağmur suyu yalnız yüzeyi ıslatmaz, toprağın nemli alt katmanlarına kadar işler."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Islanan toprak parçaları üst üste gelir, birleşir ve avuçta topaklanır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yağmurun derine işlediği ve nemli toprağın elde birleşip topaklandığı zemin için uygundur.","boundary_detail":"Gerekli sınır, yağmurun derine işlemesi ve nemli toprağın birleşip topaklanmasıdır.","branch_image_ar":"ثرى عمد","concept_gloss":"yağmurla derinden ıslanıp topaklanan toprak","contextual_glosses":[{"applicability":"Eylem, yağmur suyunun yüzeyden aşağı inip nemli toprak katmanına ulaşmasını anlatıyorsa kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yağmur suyunun toprağa derinlemesine işlemesini korur."},"facet_ids":["F001"],"text":"yağmur toprağın derinine işledi","usage_role":"contextual"}],"definition":"Yağmurun toprağın alt katmanlarına işlemesiyle nemli toprağın üst üste birikip elde topaklanacak ölçüde birleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yağmur suyu yalnız yüzeyi ıslatmaz, toprağın nemli alt katmanlarına kadar işler."},{"facet_id":"F002","role":"core","statement":"Islanan toprak parçaları üst üste gelir, birleşir ve avuçta topaklanır."}],"identity_rationale":"Kaynak anlatımı, yağmur suyunun toprağın alt katmanlarına işlemesini, nemli toprağın üst üste yığılıp elde topaklanmasını açıkça bildirir. Dal yalnız yüzey ıslaklığına indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yağmurla ıslanıp avuçta topaklanan toprak"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"yağmur toprağın derinine işledi"}],"lexicalization_note":"Tanım, nemli toprak söz öbeği ile yağmurun yere işlemesini bildiren kullanımı ayrı tutarak ortak sonucu açıklar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; derin ıslanma ve topaklanmayı genel nemli toprak alanından ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir derine işleme ve topaklanma sürecine bağlıdır; komşu dal nemli toprak ve ıslaklık için daha geniş, süreç belirtmeyen bir alana sahiptir.","focus_only":"Yağmurun derine işlemesi ve toprağın avuçta topaklanacak biçimde birleşmesini gerektirir.","gloss":"nemli toprak ve ıslaklık","neighbor_only":"Nemli toprak yanında genel ıslaklık, ter nemi ve başka ıslanmış maddeleri de kapsar.","neighbor_ref":"root_000198/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da nemli toprağı ve yağmurla oluşan ıslaklığı anlatabilir."}],"source_phrase_ar":"ثرى عمد إذا بلته الأمطار (maqayis); عمدت الأرض إذا رسخ فيها المطر إلى الثرى وتعقد في كفك (maqayis;tahdhib); عمد الثرى إذا بلله المطر وتعقد واجتمع من ندوته (sihah); عمد الثرى إذا كان تراكب بعضه على بعض وندي (tahdhib)","source_summary":"Kaynaklar, yağmurun toprağa derinlemesine işlemesi ve nemli toprağın birikip elde topaklanması sonucunda birleşir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه الثرى أو الأرض إذا رسخ فيها المطر فاجتمع التراب وتعقد في الكف","what_is_not_ar":"ليس العمود ولا القصد ولا الوجع"},"support_links":[]},{"boundary":"Dal genel gençlikten ve genel şişmanlıktan daha dardır; gençlik dolgunluğu ile gelişkin beden birlikte önemlidir.","branch_kind":"bare","branch_ref":"root_001043/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"gençliğinin dolgun çağında, gelişkin bedenli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, gençliğin olgun ve dolgun evresinde gelişkin bir bedene sahiptir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişil biçim, gövdeli ve dolgun yapılı kadını belirtir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaşça genç olmanın yanında bedenin dolgun, gelişkin ve güçlü oluşu da anlatıldığında uygundur.","boundary_detail":"Dal genel gençlikten ve genel şişmanlıktan daha dardır; gençlik dolgunluğu ile gelişkin beden birlikte önemlidir.","branch_image_ar":"الشاب العمداني","concept_gloss":"gençliğinin dolgun çağında, gelişkin bedenli","contextual_glosses":[{"applicability":"Genç bir kişinin bedensel dolgunluğu ve gücü özellikle belirtilmek istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençliği, bedensel gelişkinliği ve güçlülüğü korur."},"facet_ids":["F001"],"text":"güçlü ve gelişkin yapılı genç","usage_role":"contextual"}],"definition":"Gençliğinin dolgun çağında bulunan, bedeni gelişkin ve güçlü genç; dişil kullanımda ise gövdeli ve dolgun yapılı kadındır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, gençliğin olgun ve dolgun evresinde gelişkin bir bedene sahiptir."},{"facet_id":"F002","role":"extension","statement":"Dişil biçim, gövdeli ve dolgun yapılı kadını belirtir."}],"identity_rationale":"Kaynak anlatımı, gençliğinin dolgunluğundaki güçlü genci ve gövdeli, dolgun yapılı kadını aynı bedensel gelişkinlik altında verir. Anlam yalnız yaşça genç olmayı değil, bedenin dolgun ve güçlü oluşunu da gerektirir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"gençliğinin dolgun çağında, gelişkin bedenli kişi"}],"lexicalization_note":"Tanım, çıplak dalın gençlik çağındaki dolgun ve güçlü beden niteliğini verir; başka dalların kalıp anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gençliğe bağlı gelişkinliği genel beden dolgunluğundan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal insanın gençlik çağındaki gelişkin bedenine bağlıdır; komşu dal yaş ve insan sınırı olmadan genel şişmanlık ve beden dolgunluğunu kapsar.","focus_only":"Gençlik çağını ve gelişkin, güçlü beden yapısını birlikte gerektirir.","gloss":"bedensel dolgunluk ve şişmanlık","neighbor_only":"Çocuk, kertenkele veya deve gibi farklı canlılarda yaş sınırı olmadan şişmanlık ve dolgunluk bildirir.","neighbor_ref":"root_000352/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedenin dolgunlaşmasını ve etlenmesini anlatabilir."}],"source_phrase_ar":"العمد الشاب الممتلئ شبابا وهو العمداني وامرأة عمدانية ذات جسم وعبالة (maqayis); العمد الشاب الشديد الممتلئ شبابا والمرأة عمدانية (ayn); العمد الشاب الممتلىء شبابا وامرأة عمدانية (tahdhib)","source_summary":"Kaynaklar, gençliğinin dolgun çağındaki güçlü genç ile gövdeli ve dolgun yapılı kadın kullanımını ortaklaştırır.","sources":["MQ","AY","TA"],"what_is_ar":"يدخل فيه العمد الشاب الممتلئ شبابا والعمداني والمرأة العمدانية ذات الجسم والعبالة","what_is_not_ar":"ليس العمود ولا تعمد الفعل ولا المرض"},"support_links":[]},{"boundary":"Anlam yalnızca sağlanan karşılaştırmalı kalıba bağlıdır ve iki kaynak yorumunun açıklıkla ayrı tutulmasını gerektirir.","branch_kind":"non_bare","branch_ref":"root_001043/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"bundan daha fazlası veya şaşırtıcısı var mı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sabit karşılaştırma kalıbı, verilen örneği değerlendirir ve iki farklı yorum taşır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yorumda kalıp, verilen örnekten daha fazlasının bulunup bulunmadığını sorar."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer yorumda kalıp, verilen örneğin olağanüstü şaşırtıcılığını dile getirir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen sabit karşılaştırma kalıbının iki aktarılan yorumunu birlikte görünür kılmak için uygundur.","boundary_detail":"Anlam yalnızca sağlanan karşılaştırmalı kalıba bağlıdır ve iki kaynak yorumunun açıklıkla ayrı tutulmasını gerektirir.","branch_image_ar":"صيغة أعمد من كذا","concept_gloss":"bundan daha fazlası veya şaşırtıcısı var mı","contextual_glosses":[{"applicability":"Kalıp, verilen örneğin şaşırtıcılığını soru biçiminde vurguladığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Soru biçimini ve güçlü şaşırma değerlendirmesini korur."},"facet_ids":["F003"],"text":"bundan daha şaşırtıcı ne olabilir","usage_role":"contextual"}],"definition":"Belirli bir karşılaştırmalı söz kalıbı, verilen örneği aşan bir şey olup olmadığını sorma veya o örneğin şaşırtıcılığını belirtme biçiminde iki türlü yorumlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sabit karşılaştırma kalıbı, verilen örneği değerlendirir ve iki farklı yorum taşır."},{"facet_id":"F002","role":"source_variant","statement":"Bir yorumda kalıp, verilen örnekten daha fazlasının bulunup bulunmadığını sorar."},{"facet_id":"F003","role":"source_variant","statement":"Diğer yorumda kalıp, verilen örneğin olağanüstü şaşırtıcılığını dile getirir."}],"identity_rationale":"Kaynak anlatımı, belirli kalıbın iki aktarılan açıklamasını verir: verilen örnekten daha fazla olup olmadığını sorma ve onu daha şaşırtıcı bulma. Dal korunabilir, ancak bu iki yorum tek ve kesin bir anlama indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"bundan daha fazlası mı, yoksa daha şaşırtıcısı mı"}],"lexicalization_note":"Tanım, artış sorusu ile şaşırma yorumunu yalnızca sabit karşılaştırmalı kalıpta tutar; bağımsız bir kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kalıplaşmış anlatım ortaklığını ama anlam ayrılığını en iyi gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal daha fazla olma ve şaşırtıcılık çevresinde yorumlanır; komşu dal yalnızca gerçekleşme hızını değerlendirir, bu nedenle anlam bakımından birbirinin yerine geçmez.","focus_only":"Artış sorusu ile şaşırma arasında iki aktarılan yoruma sahip özel bir karşılaştırma kalıbıdır.","gloss":"ne çabuk oldu","neighbor_only":"Bir olayın ne kadar çabuk gerçekleştiğini ünlemli ya da bildirmeli kalıpla anlatır.","neighbor_ref":"root_000698/B003","relation_type":"same_field","shared_zone":"Her ikisi de kalıplaşmış, güçlü değerlendirme veya şaşırma bildiren sözlerdir."}],"source_phrase_ar":"أعمد من سيد قتله قومه (maqayis;sihah;tahdhib); هل زاد على سيد قتله قومه (maqayis;tahdhib); أعجب من سيد قتله قومه (maqayis;tahdhib); أنا أعمد من كذا أي أعجب منه (sihah)","source_summary":"Toplu anlatım, aynı sabit kalıp için artış sorusu ile şaşırma bildiren iki açıklama aktarır; kanıt bunlardan birini tek geçerli yorum olarak seçmez.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه قولهم أعمد من سيد قتله قومه وأعمد من كذا على معنى هل زاد على هذا أو أعجب منه","what_is_not_ar":"ليس القصد ولا العماد الحسي ولا وجع المرض"},"support_links":[]},{"boundary":"Anlam, genel olarak bir boşluğu kapatmak değil, selin akış yönünü kapatıp suyu biriktirmektir.","branch_kind":"non_bare","branch_ref":"root_001043/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"selin önünü kapatıp suyu biriktirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Selin aktığı yön, toprak ya da taşla fiziksel olarak kapatılır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kapatmanın sonucu, akışın durması ve suyun bir yerde birikmesidir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sel akışının toprak veya taşla durdurulduğu ve suyun belirli bir yerde toplandığı işlem için uygundur.","boundary_detail":"Anlam, genel olarak bir boşluğu kapatmak değil, selin akış yönünü kapatıp suyu biriktirmektir.","branch_image_ar":"سد مجرى السيل","concept_gloss":"selin önünü kapatıp suyu biriktirme","contextual_glosses":[{"applicability":"Taş kullanılarak sel akışının kesildiği ve suyun bir yerde biriktirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşla kapatma işlemini ve suyu toplama sonucunu korur."},"facet_ids":["F001","F002"],"text":"sel yatağını taşla kapatıp suyu topladı","usage_role":"contextual"}],"definition":"Sel suyunun akış yönünü toprak veya taşla kapatarak suyun belirli bir yerde toplanmasını sağlamaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Selin aktığı yön, toprak ya da taşla fiziksel olarak kapatılır."},{"facet_id":"F002","role":"core","statement":"Kapatmanın sonucu, akışın durması ve suyun bir yerde birikmesidir."}],"identity_rationale":"Tek kaynak anlatımı, sel akışının önünü toprak veya taşla kapatıp suyu bir yerde toplama işlemini bütün aşamalarıyla açıkça verir.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"selin önünü kapatıp suyu bir yerde toplamak"}],"lexicalization_note":"Tanım, yalnızca sel akışını kapatma kullanımına bağlıdır ve bunu genel bir engelleme anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kapatma eylemi ile sel bendinin kendisi arasındaki sınırı gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal toprak veya taşla yapılan kapatma işlemini ve birikme sonucunu anlatır; komşu dal ise suyu gerektiğinde geçirebilen yapısal engeli adlandırır.","focus_only":"Sel akışını kapatma eylemini ve suyun bir yerde birikmesi sonucunu bildirir.","gloss":"sel bendi","neighbor_only":"Seli geri çeviren ve gerektiği kadar su salabilen yapının kendisini adlandırır.","neighbor_ref":"root_000751/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de sel suyunu bir engelle tutma ve akışı denetleme durumuyla ilgilidir."}],"source_phrase_ar":"عمدت السيل تعميدا إذا سددت وجه جريته حتى يجتمع في موضع بتراب أو حجارة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, selin önünü toprak veya taşla kapatma ve suyu bir yerde toplama sonucunu birlikte verir."}],"source_summary":"Bu dal yalnız bir kaynakta, sel yolunu toprak veya taşla kapatıp suyu bir yerde biriktirme işlemi olarak tanıklanmıştır.","sources":["TA"],"what_is_ar":"يدخل فيه تعميد السيل بسد وجه جريته بتراب أو حجارة حتى يجتمع في موضع","what_is_not_ar":"ليس عمود الشيء ولا قصد الشيء"},"support_links":[]},{"boundary":"Anlam yalnızca verilen bağlı kullanımda geçerlidir; güvenip dayanma veya fiziksel direk anlamı taşımaz.","branch_kind":"non_bare","branch_ref":"root_001043/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"yanından ayrılmadan bağlı kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özne, bağlandığı kişi veya şeyden ayrılmayıp onun yanında kalır."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi veya şeye sürekli eşlik etme ve ondan ayrılmama durumu sağlanan yapıyla anlatıldığında uygundur.","boundary_detail":"Anlam yalnızca verilen bağlı kullanımda geçerlidir; güvenip dayanma veya fiziksel direk anlamı taşımaz.","branch_image_ar":"لزوم الشيء","concept_gloss":"yanından ayrılmadan bağlı kalma","contextual_glosses":[{"applicability":"Öznenin bir kişi veya şeyle kalmayı sürdürdüğü bağlamlarda açık ve doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süren bağlılığı ve yanından ayrılmama durumunu korur."},"facet_ids":["F001"],"text":"ona bağlı kaldı ve yanından ayrılmadı","usage_role":"contextual"}],"definition":"Bir kimseye veya şeye bağlı kalmak, yanından ayrılmamak ve onunla birlikte kalmayı sürdürmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özne, bağlandığı kişi veya şeyden ayrılmayıp onun yanında kalır."}],"identity_rationale":"Tek kaynak anlatımı, belirli edatlı kullanımda bir kimseye veya şeye bağlı kalmayı ve ondan ayrılmamayı doğrudan bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"ona bağlı kalıp yanından ayrılmamak"}],"lexicalization_note":"Tanım, ayrılmadan yanında kalma anlamını yalnızca sağlanan edatlı yapıya bağlar ve çıplak köke genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişiye veya şeye bağlı kalmayı genel yerleşme ve kalıcılıktan ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli yapıda bir kişi veya şeye bağlı kalmaya odaklanır; komşu dal yerleşme ve uzun süre bir yerde durma gibi daha geniş kullanımları da içerir.","focus_only":"Belirli edatlı yapıda bir kişi veya şeye bağlanıp yanından ayrılmamayı anlatır.","gloss":"kalma ve yerleşme","neighbor_only":"Bir yerde oturmayı ve bir bulutun uzun süre kalmasını da kapsayan daha geniş bir kalıcılık alanına sahiptir.","neighbor_ref":"root_000155/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yerde veya bir şeyle kalmayı ve ayrılmamayı anlatabilir."}],"source_phrase_ar":"حلس به وعرس به وعمد به ولزب به إذا لزمه (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, bir kişi veya şeye bağlı kalma ve yanından ayrılmama anlamını verir."}],"source_summary":"Bu dal yalnız bir kaynakta, belirli edatlı yapıyla bir kişi veya şeye bağlı kalıp ondan ayrılmama anlamında tanıklanmıştır.","sources":["TA"],"what_is_ar":"يدخل فيه عمد به بمعنى لزمه أو أقام ملازما له","what_is_not_ar":"ليس الاعتماد على الشخص ولا عماد الخباء"},"support_links":[]},{"boundary":"Üstün gelme anlamı dışarıda bırakılır; öfke çekirdeği ile acı çekme uzantısı birbirinden ayrılır.","branch_kind":"bare","branch_ref":"root_001043/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","surface_ar":"عِمَادِ"}],"gloss":"öfke ve onunla bağlantılı acılı sıkıntı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çıplak adlandırmanın temel anlamı öfke ve kızgınlıktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgili eylem, üzüntü, öfke veya hastalık yüzünden acı çekmeyi de bildirebilir."}}],"root_ar":"ع م د","root_id":"root_001043","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Öfke adını ve ilgili kullanımda öfke, üzüntü veya hastalık yüzünden çekilen acıyı birlikte göstermek için uygundur.","boundary_detail":"Üstün gelme anlamı dışarıda bırakılır; öfke çekirdeği ile acı çekme uzantısı birbirinden ayrılır.","branch_image_ar":"الغضب والغلبة بالغضب","concept_gloss":"öfke ve onunla bağlantılı acılı sıkıntı","contextual_glosses":[{"applicability":"Öfkenin yalnız duygu değil, kişiyi acı içinde bırakan bir sıkıntı olarak anlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öfkeyi ve onun doğurduğu acılı sıkıntıyı birlikte korur."},"facet_ids":["F001","F002"],"text":"öfke yüzünden acı çekti","usage_role":"contextual"}],"definition":"Öfke duygusudur; ilgili kullanım ayrıca üzüntü, öfke veya hastalık yüzünden acı çekmeyi anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çıplak adlandırmanın temel anlamı öfke ve kızgınlıktır."},{"facet_id":"F002","role":"extension","statement":"İlgili eylem, üzüntü, öfke veya hastalık yüzünden acı çekmeyi de bildirebilir."}],"identity_rationale":"Kaynak anlatımı öfkeyi ve üzüntü, öfke veya hastalık yüzünden acı çekmeyi verir; geçici dal başlığındaki öfkeyle üstün gelme düşüncesini desteklemez. Dal, öfke ile ona veya başka ağır durumlara eşlik eden acılı sıkıntı olarak yeniden çerçevelenmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"öfke veya öfkenin verdiği acılı sıkıntı"}],"lexicalization_note":"Tanım, çıplak biçimdeki öfke anlamını temel alır ve acı çekme kullanımını bağlı bir uzantı olarak belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; öfke çekirdeğini acılı sıkıntı ve hınç uzantıları üzerinden ayıran komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal öfkeyle bağlantılı acılı sıkıntıya uzanır; komşu dal ise hınç, kışkırtma ve öfkeli hayvan gibi farklı yönlere genişler.","focus_only":"Öfkenin yanında üzüntü veya hastalıktan doğan acı çekme kullanımını da içerir.","gloss":"öfke ve hınç","neighbor_only":"Kişiyi kışkırtan şeye yönelen hıncı ve öfkeli hayvan kullanımını da kapsar.","neighbor_ref":"root_000305/B003","relation_type":"near_synonym","shared_zone":"Her iki dalın temel alanında öfke ve kızgınlık duygusu bulunur."}],"source_phrase_ar":"العمد والضمد الغضب (tahdhib); عمد توجع من حزن أو غضب أو سقم (mufradat)","source_summary":"Toplu anlatım, temel olarak öfkeyi; ayrıca üzüntü, öfke veya hastalığın doğurduğu acılı sıkıntıyı aktarır. Üstün gelme anlamı desteklenmez.","sources":["TA","MU"],"what_is_ar":"يدخل فيه العمد بمعنى الغضب وما يتصل بتوجع الغضب","what_is_not_ar":"ليس القصد ولا العمود ولا مرض السقم"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:7:1"],"branch_refs":[],"candidate_id":"cand_d1ed0d566c066418b440","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:1:cross-ayah-identification","source_type":"word_analysis","support_ids":["sup_257d92dc429a7b10ac2f","sup_7a788e5d2a42f7deb9ee"],"title":"name continues the prior governed object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:1","qac_refs":["89:7:1:1"],"status":"accepted"}},{"anchor_refs":["89:7:1"],"branch_refs":[],"candidate_id":"cand_59f33a779ea11d579f5f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:1:marker-and-variant-pressure","source_type":"word_analysis","support_ids":["sup_257d92dc429a7b10ac2f","sup_51253dfbb9cd0ecdbdec"],"title":"marker field colors the name without replacing it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:1","qac_refs":["89:7:1:1"],"status":"accepted"}},{"anchor_refs":["89:7:1"],"branch_refs":[],"candidate_id":"cand_9029199d286fba6ced23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:1:proper-name-opacity","source_type":"word_analysis","support_ids":["sup_257d92dc429a7b10ac2f","sup_464090d7a8ae223d7ef1"],"title":"rare name needs its epithet","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:1","qac_refs":["89:7:1:1"],"status":"accepted"}},{"anchor_refs":["89:7:2"],"branch_refs":[],"candidate_id":"cand_c46bc26f8e08c60ace1f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:2:construct-epithet","source_type":"word_analysis","support_ids":["sup_011603f5664472a21c3b","sup_b644b8b07d814891cfb7"],"title":"construct head binds the support noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:2","qac_refs":["89:7:2:1"],"status":"accepted"}},{"anchor_refs":["89:7:2"],"branch_refs":[],"candidate_id":"cand_e5adf1ebbf536fd43d0c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:2:feminine-form-and-formula-echoes","source_type":"word_analysis","support_ids":["sup_011603f5664472a21c3b","sup_7843bbec8f3b4872f54f"],"title":"feminine bearer within a wider formula","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:2","qac_refs":["89:7:2:1"],"status":"accepted"}},{"anchor_refs":["89:7:2"],"branch_refs":[],"candidate_id":"cand_5c44a1a49b84e00b3f9e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:2:possession-as-characterization","source_type":"word_analysis","support_ids":["sup_011603f5664472a21c3b","sup_8a1444995074ecab5239"],"title":"possession becomes identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:2","qac_refs":["89:7:2:1"],"status":"accepted"}},{"anchor_refs":["89:7:2"],"branch_refs":[],"candidate_id":"cand_784e2438631bd31122d7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:7:2:qiraat-case-pressure","source_type":"word_analysis","support_ids":["sup_011603f5664472a21c3b","sup_b6893246b8c85ff350b1"],"title":"variants expose construct closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:2","qac_refs":["89:7:2:1"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_fbb3d176a6e2fb3b32d8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:concrete-support-range","source_type":"word_analysis","support_ids":["sup_2de50e491e8df1c9b73b","sup_82042e70de4743fbe0a6"],"title":"support noun with engineered reliance pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:3","qac_refs":["89:7:3:1","89:7:3:2"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_881315094ef8ab6bb49d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:definite-genitive-complement","source_type":"word_analysis","support_ids":["sup_82042e70de4743fbe0a6","sup_a367bbc6b29baf100634"],"title":"definite complement completes the construct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:3","qac_refs":["89:7:3:1","89:7:3:2"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_4909134270d1a0073112","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:final-visual-landing","source_type":"word_analysis","support_ids":["sup_196735407a811cbda6cc","sup_82042e70de4743fbe0a6"],"title":"final word resolves the image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:3","qac_refs":["89:7:3:1","89:7:3:2"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_585a92cdb6c9707b8365","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:quranic-support-contrasts","source_type":"word_analysis","support_ids":["sup_006f91a9de3b1819aade","sup_82042e70de4743fbe0a6"],"title":"visible supports contrast with other support scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:3","qac_refs":["89:7:3:1","89:7:3:2"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_be3f95b81f0389db4438","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_82042e70de4743fbe0a6","sup_d7ed15badc43db41d8ec"],"title":"firm sound lets the image settle","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:7:3","qac_refs":["89:7:3:1","89:7:3:2"],"status":"accepted"}},{"anchor_refs":["89:7:3"],"branch_refs":[],"candidate_id":"cand_eca4ff2b562c8ac495c7","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001043"],"scope":"focus_ayah","source_local_id":"89:7:3:2","source_type":"qac_morpheme","support_ids":["sup_93c879e49b18969ca33f"],"title":"QAC root occurrence: ع م د","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:7","branch_refs":["root_001043/B002","root_001043/B003","root_001043/B005"],"candidate_id":"cand_474be92bd565b6e4974c","commentary_obligation":"review","hft_ref":"hft_8c709cdadea8faf0ec04","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_monumental_vertical_system","source_type":"hft","support_ids":["sup_916521bbd784ed36a48f"],"title":"base_monumental_vertical_system","trust":"legacy_unbound"},{"anchor_refs":["89:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:7","branch_refs":["root_001043/B003","root_001043/B004"],"candidate_id":"cand_d8d83c9c69457e20eed7","commentary_obligation":"review","hft_ref":"hft_6acebd7713d661a39813","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_tent_pole_collective","source_type":"hft","support_ids":["sup_ba7ed5f2baaf4b1f8089"],"title":"base_tent_pole_collective","trust":"legacy_unbound"},{"anchor_refs":["89:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:7","branch_refs":["root_001043/B006","root_001043/B007"],"candidate_id":"cand_3682dfe1a4128f9e0b43","commentary_obligation":"review","hft_ref":"hft_5c7e8717b34029c5edcc","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_civic_mainstay","source_type":"hft","support_ids":["sup_bac52f2a61736fb54294"],"title":"base_civic_mainstay","trust":"legacy_unbound"},{"anchor_refs":["89:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:7","branch_refs":["root_001043/B001","root_001043/B002"],"candidate_id":"cand_147167b5b7178d4856e1","commentary_obligation":"review","hft_ref":"hft_1ec38384ec6bd43b6102","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base_purposive_construction","source_type":"hft","support_ids":["sup_14444bd6493996e6672c"],"title":"base_purposive_construction","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","qac_morphemes":[{"lemma_ar":"إِرَم","morph_features":"STEM|POS:PN|LEM:<iram|F|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"89:7:1:1","qac_word_ref":"89:7:1","root_ar":"","surface_ar":"إِرَمَ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:2:1","qac_word_ref":"89:7:2","root_ar":"","surface_ar":"ذَاتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:7:3:1","qac_word_ref":"89:7:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","root_ar":"ع م د","surface_ar":"عِمَادِ"}],"word_analysis_qac_refs":[["89:7:1:1"],["89:7:2:1"],["89:7:3:1","89:7:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:7:1","89:7:2","89:7:3"]},"focus_surface_evidence":{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","qac_morphemes":[{"lemma_ar":"إِرَم","morph_features":"STEM|POS:PN|LEM:<iram|F|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"89:7:1:1","qac_word_ref":"89:7:1","root_ar":"","surface_ar":"إِرَمَ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|FS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:2:1","qac_word_ref":"89:7:2","root_ar":"","surface_ar":"ذَاتِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:7:3:1","qac_word_ref":"89:7:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"عِمَاد","morph_features":"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:7:3:2","qac_word_ref":"89:7:3","root_ar":"ع م د","surface_ar":"عِمَادِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:7:1:1"],["89:7:2:1"],["89:7:3:1","89:7:3:2"]],"word_analysis_refs":["89:7:1","89:7:2","89:7:3"],"word_rows":[{"analysis_record_ref":"89:7:1","analytic_gloss_range_en":"proper name identifying or specifying the ʿĀd reference carried over from 89:6, locally made legible by the following possessed-support epithet rather than by direct lexical translation","analytic_root_gloss_range_en":"rare proper-name field with debated links to lineage, settlement, eponym, and marker-place associations; locally the proper-name function governs, while marker and ruin pressure remain secondary","qac_refs":["89:7:1:1"],"root":{"arabic":"إ ر م","transliteration":"ʾ-r-m"},"surface":{"arabic":"إِرَمَ","transliteration":"irama"}},{"analysis_record_ref":"89:7:2","analytic_gloss_range_en":"feminine construct bearer or possessor term that turns Iram into an entity characterized by the following supports, allowing possession and defining quality to remain jointly live","analytic_root_gloss_range_en":"possessor, bearer, or entity characterized by an attached noun; other branches such as demonstrative or relative uses are not selected by this local construct frame","qac_refs":["89:7:2:1"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذَاتِ","transliteration":"dhāti"}},{"analysis_record_ref":"89:7:3","analytic_gloss_range_en":"definite genitive support noun, singular or collective, naming the pillars, posts, tent-poles, or load-bearing structures that complete Iram's epithet","analytic_root_gloss_range_en":"root range includes deliberate aiming, propping, pillars or columns, tent-poles, reliance, central supports, and other extended branches; locally the concrete support noun is selected, with intentional engineering and reliance pressure surviving as coloring","qac_refs":["89:7:3:1","89:7:3:2"],"root":{"arabic":"ع م د","transliteration":"ʿ-m-d"},"surface":{"arabic":"ٱلْعِمَادِ","transliteration":"al-ʿimādi"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:7"],"branch_refs":["root_001043/B002","root_001043/B003","root_001043/B005"],"candidate_id":"cand_474be92bd565b6e4974c","evidence_scope":"focus_ayah","hft_ref":"hft_8c709cdadea8faf0ec04","item_id":"base_monumental_vertical_system","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_monumental_vertical_system","support_id":"sup_916521bbd784ed36a48f"},{"anchor_refs":["89:7"],"branch_refs":["root_001043/B003","root_001043/B004"],"candidate_id":"cand_d8d83c9c69457e20eed7","evidence_scope":"focus_ayah","hft_ref":"hft_6acebd7713d661a39813","item_id":"base_tent_pole_collective","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_tent_pole_collective","support_id":"sup_ba7ed5f2baaf4b1f8089"},{"anchor_refs":["89:7"],"branch_refs":["root_001043/B006","root_001043/B007"],"candidate_id":"cand_3682dfe1a4128f9e0b43","evidence_scope":"focus_ayah","hft_ref":"hft_5c7e8717b34029c5edcc","item_id":"base_civic_mainstay","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_civic_mainstay","support_id":"sup_bac52f2a61736fb54294"},{"anchor_refs":["89:7"],"branch_refs":["root_001043/B001","root_001043/B002"],"candidate_id":"cand_147167b5b7178d4856e1","evidence_scope":"focus_ayah","hft_ref":"hft_1ec38384ec6bd43b6102","item_id":"base_purposive_construction","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base_purposive_construction","support_id":"sup_14444bd6493996e6672c"}],"diagnostics":[],"lane_counts":{"global":16,"macro":6,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":16,"unstructured_record_count":0},"identity":{"ayah_ref":"89:7","lane":"micro","linguistic_source_ref":"89:7","surface_ref":"89:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:7","target_tokens":[["Sütunlar",["89:7:3"]],["sahibi",["89:7:2","89:7:3"]],["İrem'e",["89:7:1"]]],"text":"Sütunlar sahibi İrem'e,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3:quranic-support-contrasts","source_type":"word_analysis","support_id":"sup_006f91a9de3b1819aade","text":"{\"blocking_evidence\":null,\"headline\":\"visible supports contrast with other support scenes\",\"reader_payoff\":\"The reader notices that Iram's visible supports belong to a wider Quranic field where support can mark creation, human monumentality, or judgment.\",\"reason\":\"The CRITICAL rows give concrete reference contrasts with unseen heavenly pillars in 13:2 and 31:10 and enclosing punishment pillars in 104:9; these contrasts do not override the local concrete support reading.\",\"representative_source_ids\":[\"QI-731e41e0\",\"QI-7610c4e3\",\"QE-95f48aba\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:2","source_type":"word_analysis","support_id":"sup_011603f5664472a21c3b","text":"{\"gloss_range\":\"feminine construct bearer or possessor term that turns Iram into an entity characterized by the following supports, allowing possession and defining quality to remain jointly live\",\"prose\":\"{{ar:ذَاتِ}} ({{tr:dhāti}}) is the hinge that prevents {{ar:إِرَمَ}} ({{tr:irama}}) from remaining a bare label. As a feminine construct head, it must be completed by {{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}}), so the supports are not a loose image after the name; they become the attribute through which Iram is identified. The recited join from {{ar:ذَاتِ}} ({{tr:dhāti}}) to {{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}}) reinforces that bond, and the longer cadence after short {{ar:إِرَمَ}} ({{tr:irama}}) slows the moment where the bare name becomes relational description. The word also does more than a simple adjective would do: it lets possession, bearing, and defining quality overlap, so Iram can be remembered by structures it has and by the structural character those supports give it. The feminine form leaves the referent open enough for place, city, tribe-name, or collective identity, while the local construct frame keeps relative-pronoun and demonstrative branches out of play. Variant shapes with tanwīn or accusative pressure show how much the base reading depends on tight construct closure, and the same possessor pattern resonates inside the surah by naming reason (89:5), pillars here, and Pharaoh's stakes (89:10), while also joining attribute-bearing formulas elsewhere (85:1; 51:7; 86:11).\",\"root_display\":\"{{ar:ذ و و}} ({{tr:dh-w-w}})\",\"root_gloss_range\":\"possessor, bearer, or entity characterized by an attached noun; other branches such as demonstrative or relative uses are not selected by this local construct frame\",\"surface_display\":\"{{ar:ذَاتِ}} ({{tr:dhāti}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3:final-visual-landing","source_type":"word_analysis","support_id":"sup_196735407a811cbda6cc","text":"{\"blocking_evidence\":null,\"headline\":\"final word resolves the image\",\"reader_payoff\":\"The reader notices that the ayah lands as a still civilizational image: name, relation, then the support-mark that makes the name memorable.\",\"reason\":\"The CRITICAL rows are coherent with the local three-word nominal structure: no finite verb appears in 89:7, and the final noun supplies the delayed image.\",\"representative_source_ids\":[\"QT-db265700\",\"QT-dd6dd0e9\",\"QH-76fa8eb7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:1","source_type":"word_analysis","support_id":"sup_257d92dc429a7b10ac2f","text":"{\"gloss_range\":\"proper name identifying or specifying the ʿĀd reference carried over from 89:6, locally made legible by the following possessed-support epithet rather than by direct lexical translation\",\"prose\":\"{{ar:إِرَمَ}} ({{tr:irama}}) does not restart the sentence after 89:6; it specifies the prior {{ar:عَادٍ}} ({{tr:ʿĀdin}}) reference inside the same governed object chain. That makes the ayah break part of the identification: the listener has to carry the previous prepositional frame forward before the name can settle. The word is definite as a proper name, but it is also opaque and rare, so recognition arrives through the next two words, {{ar:ذَاتِ ٱلْعِمَادِ}} ({{tr:dhāti al-ʿimādi}}), rather than through an ordinary lexical label. It also becomes the first named display answer to the prior question about how the Lord acted, shifting inquiry into nominal presentation. Debated etymologies, marker-stone associations, and sound variants such as Arima or Aramma can make the name feel physically marked, prestigious, and already shadowed by ruin, but the local grammar keeps those pressures secondary: the surface is first a name, then a name made visible by its support-bearing epithet.\",\"root_display\":\"{{ar:إ ر م}} ({{tr:ʾ-r-m}})\",\"root_gloss_range\":\"rare proper-name field with debated links to lineage, settlement, eponym, and marker-place associations; locally the proper-name function governs, while marker and ruin pressure remain secondary\",\"surface_display\":\"{{ar:إِرَمَ}} ({{tr:irama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3:concrete-support-range","source_type":"word_analysis","support_id":"sup_2de50e491e8df1c9b73b","text":"{\"blocking_evidence\":null,\"headline\":\"support noun with engineered reliance pressure\",\"reader_payoff\":\"The reader sees Iram's remembered strength as a load-bearing system, not merely as decorative vertical objects.\",\"reason\":\"V4 accepts pillar, support, tent-pole, propping, reliance, and intent branches for {{ar:ع م د}} ({{tr:ʿ-m-d}}), but the aligned local form is a concrete noun, so the prose keeps support as selected and treats deliberate engineering or reliance as pressure.\",\"representative_source_ids\":[\"QS-2bf4b129\",\"QS-459d827e\",\"QF-0dcba43f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:1:proper-name-opacity","source_type":"word_analysis","support_id":"sup_464090d7a8ae223d7ef1","text":"{\"blocking_evidence\":null,\"headline\":\"rare name needs its epithet\",\"reader_payoff\":\"The reader notices that the line first gives a singular remembered name and only afterward supplies the feature by which that name becomes intelligible.\",\"reason\":\"The aligned word is a proper noun and the contextual profile marks it as a one-off exact-root form; the absence of V4 rows for the root does not weaken the CRITICAL payoff because the local phrase itself supplies the stabilizing descriptor.\",\"representative_source_ids\":[\"QG-4293f7b8\",\"QH-64235eff\",\"QY-1fb01a0f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:1:marker-and-variant-pressure","source_type":"word_analysis","support_id":"sup_51253dfbb9cd0ecdbdec","text":"{\"blocking_evidence\":null,\"headline\":\"marker field colors the name without replacing it\",\"reader_payoff\":\"The reader notices why the rare name can feel already marked by visible traces and unstable memory before the final support image appears.\",\"reason\":\"The CRITICAL rows press marker and variant associations, but local grammar and QAC form keep {{ar:إِرَمَ}} ({{tr:irama}}) from being translated as a common architectural or decay noun.\",\"representative_source_ids\":[\"QS-93e419a3\",\"QS-d6c56e69\",\"QF-78790167\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:2:feminine-form-and-formula-echoes","source_type":"word_analysis","support_id":"sup_7843bbec8f3b4872f54f","text":"{\"blocking_evidence\":null,\"headline\":\"feminine bearer within a wider formula\",\"reader_payoff\":\"The reader notices that the grammar can characterize Iram without resolving whether it is place, city, tribe, or collective, while still placing it inside a repeated possession formula.\",\"reason\":\"The local form is feminine singular and construct-bound; the CRITICAL rows give concrete formula comparisons in 89:5, 89:10, 85:1, 51:7, and 86:11, while V4 keeps the local branch to possessor or characterized-by usage.\",\"representative_source_ids\":[\"QF-1073a8db\",\"QI-27dccac9\",\"QE-297aca73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:1:cross-ayah-identification","source_type":"word_analysis","support_id":"sup_7a788e5d2a42f7deb9ee","text":"{\"blocking_evidence\":null,\"headline\":\"name continues the prior governed object\",\"reader_payoff\":\"The reader notices that the ayah boundary intensifies identification instead of severing the syntax from 89:6.\",\"reason\":\"QAC describes {{ar:إِرَمَ}} ({{tr:irama}}) as apposition or explanatory substitution to the prior {{ar:عَادٍ}} ({{tr:ʿĀdin}}) reference, and the attachment translation support warns that a one-ayah rendering can detach what is syntactically carried from 89:6.\",\"representative_source_ids\":[\"QG-48f371b3\",\"QG-53370570\",\"QB-de9d6875\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3","source_type":"word_analysis","support_id":"sup_82042e70de4743fbe0a6","text":"{\"gloss_range\":\"definite genitive support noun, singular or collective, naming the pillars, posts, tent-poles, or load-bearing structures that complete Iram's epithet\",\"prose\":\"{{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}}) is the word that makes the three-word scene visible. As the definite genitive complement of {{ar:ذَاتِ}} ({{tr:dhāti}}), it closes the construct and sends specificity backward through the epithet: Iram is known by the supports. The noun remains concrete but not archaeologically narrow; its singular or collective form can gather pillars, columns, tent-poles, posts, or load-bearing frames into one civilizational signature. The wider {{ar:ع م د}} ({{tr:ʿ-m-d}}) field includes intentional aiming, propping, and reliance, so the selected support image can feel engineered and dependency-bearing without turning the local noun into a verb of intending. Because the ayah has no event verb, this final word has unusual weight: after name and relation, it supplies the visual answer to the earlier question about divine action, and the support image prepares the next ayah's unmatched-likeness claim (89:8). Even its sound does some work: the firm guttural-to-dental texture and long final i cadence let the support image settle at the close rather than pass quickly. Its Quranic support field is also unstable in a revealing way: heavens stand without visible pillars (13:2; 31:10), while pillars become enclosing punishment in 104:9, so Iram's prestige marker is already vulnerable inside the broader vocabulary of supports.\",\"root_display\":\"{{ar:ع م د}} ({{tr:ʿ-m-d}})\",\"root_gloss_range\":\"root range includes deliberate aiming, propping, pillars or columns, tent-poles, reliance, central supports, and other extended branches; locally the concrete support noun is selected, with intentional engineering and reliance pressure surviving as coloring\",\"surface_display\":\"{{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:2:possession-as-characterization","source_type":"word_analysis","support_id":"sup_8a1444995074ecab5239","text":"{\"blocking_evidence\":null,\"headline\":\"possession becomes identity\",\"reader_payoff\":\"The reader notices that Iram is remembered through a relation to supports, not merely described as pillared in passing.\",\"reason\":\"V4 accepts the possessor or characterized-by branch for {{ar:ذ و و}} ({{tr:dh-w-w}}), and local grammar realizes that branch through the construct phrase without forcing a choice between detachable ownership and defining attribute.\",\"representative_source_ids\":[\"QS-915ead7e\",\"QF-b11c47eb\",\"QY-030af7fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:7:3:2","source_type":"qac_morpheme","support_id":"sup_93c879e49b18969ca33f","text":"{\"lemma_ar\":\"عِمَاد\",\"morph_features\":\"STEM|POS:N|LEM:EimaAd|ROOT:Emd|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:7:3:2\",\"qac_word_ref\":\"89:7:3\",\"root_ar\":\"ع م د\",\"surface_ar\":\"عِمَادِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3:definite-genitive-complement","source_type":"word_analysis","support_id":"sup_a367bbc6b29baf100634","text":"{\"blocking_evidence\":null,\"headline\":\"definite complement completes the construct\",\"reader_payoff\":\"The reader notices that the supports define Iram from inside the construct phrase, not as a loose descriptive add-on.\",\"reason\":\"QAC marks {{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}}) as the definite genitive second term after {{ar:ذَاتِ}} ({{tr:dhāti}}), and the attachment evidence treats that iḍāfa as syntactically forced.\",\"representative_source_ids\":[\"QG-56793306\",\"QG-888482b0\",\"MG-10062349\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:2:construct-epithet","source_type":"word_analysis","support_id":"sup_b644b8b07d814891cfb7","text":"{\"blocking_evidence\":null,\"headline\":\"construct head binds the support noun\",\"reader_payoff\":\"The reader notices that the supports are pulled into one descriptive unit rather than appended as a separate visual afterthought.\",\"reason\":\"QAC and attachment evidence make {{ar:ذَاتِ}} ({{tr:dhāti}}) a feminine construct qualifier of {{ar:إِرَمَ}} ({{tr:irama}}) that governs {{ar:ٱلْعِمَادِ}} ({{tr:al-ʿimādi}}).\",\"representative_source_ids\":[\"QG-2833f0ef\",\"QG-505898f7\",\"QF-b73bdaa2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:2:qiraat-case-pressure","source_type":"word_analysis","support_id":"sup_b6893246b8c85ff350b1","text":"{\"blocking_evidence\":null,\"headline\":\"variants expose construct closure\",\"reader_payoff\":\"The reader notices that the canonical construct bond is doing real work because nearby variants make its closure and case pressure audible.\",\"reason\":\"The variant rows clarify how the phrase could sound with looser tanwīn or accusative pressure, but QAC and attachment evidence keep the aligned local reading as construct-bound {{ar:ذَاتِ}} ({{tr:dhāti}}).\",\"representative_source_ids\":[\"QF-5b612847\",\"QF-e6dc22eb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:7:3:sound-and-cadence","source_type":"word_analysis","support_id":"sup_d7ed15badc43db41d8ec","text":"{\"blocking_evidence\":null,\"headline\":\"firm sound lets the image settle\",\"reader_payoff\":\"The reader hears the final support noun as a settling close rather than a quickly passing item in a list.\",\"reason\":\"The sound rows are modest but directly tied to the final local word and support the same landing effect described by the structural rows.\",\"representative_source_ids\":[\"QP-41824861\",\"QP-ae3dc432\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B002","root_001043/B003","root_001043/B005"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001043","role":"The image of propping something upright supplies the load-bearing function of Iram's defining structures.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001043","role":"The literal pillar or column image supplies the visible architectural members of the model.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B005","mapped_root_id":"root_001043","role":"The image of height and elevated structure turns the supports into a skyline and a claim to prominence.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"changed_reading":{"after":"Iram is characterized as a monumental vertical system: a place or formation made recognizable by what holds it high.","before":"Iram bears an unspecified epithet involving supports."},"confidence":"strong","focus_anchor":"The noun عِمَادِ at word 3 is made a defining possession of Iram by the construction إِرَمَ ذَاتِ ٱلْعِمَادِ.","mechanism":"Propping, concrete columns, and elevated structure converge on a built environment whose identity lies in conspicuous load-bearing verticality.","model_id":"base_monumental_vertical_system"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_monumental_vertical_system","source_type":"hft","support_id":"sup_916521bbd784ed36a48f","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B003","root_001043/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001043","role":"The image of tent dwellers literally links people to poles and makes a mobile social formation the phrase's referent.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_001043","role":"The concrete pole image supplies the repeatable center from which each dwelling is raised.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"changed_reading":{"after":"The phrase can instead describe a people of poles, with mobility and tent-based dwelling constitutive of Iram's identity.","before":"The phrase describes a fixed city furnished with columns."},"confidence":"medium","focus_anchor":"عِمَادِ at word 3 can identify people through the poles around which their dwellings are erected.","mechanism":"The same concrete pole can classify a mode of habitation rather than a masonry city, so ذات العماد may mark a mobile people whose collective space repeatedly rises around tent supports.","model_id":"base_tent_pole_collective"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_tent_pole_collective","source_type":"hft","support_id":"sup_ba7ed5f2baaf4b1f8089","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B006","root_001043/B007"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001043","role":"The reliable chief or mainstay image supplies a human support on whom the group depends.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B007","mapped_root_id":"root_001043","role":"The central supporting part supplies the institutional core that gives the whole formation its standing.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"changed_reading":{"after":"Iram may be 'possessor of mainstays': a polity defined by concentrated human or institutional supports.","before":"The supports are only architectural objects."},"confidence":"medium","focus_anchor":"The possessive epithet ذات العماد remains attached to عِمَادِ at word 3 while the root inventory permits human and systemic supports.","mechanism":"A mainstay relied upon by a group and the central part that gives an affair its standing shift the phrase from construction materials to the persons or institutions that keep a polity coherent.","model_id":"base_civic_mainstay"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_civic_mainstay","source_type":"hft","support_id":"sup_bac52f2a61736fb54294","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"إِرَمَ ذَاتِ ٱلْعِمَادِ","ayah_ref":"89:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001043/B001","root_001043/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001043","role":"The image of intentional aiming supplies deliberate purpose behind the structures or system.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001043","role":"The propping image gives that intention a concrete result: something deliberately made to stand.","root":"ع م د","source_ref":"89:7","source_word_indices":["3"]}],"changed_reading":{"after":"Iram's supports register organized intention, a deliberately erected and maintained order.","before":"Iram merely happens to have supports."},"confidence":"exploratory","focus_anchor":"The root of عِمَادِ at word 3 also carries deliberate aiming alongside the act of supporting.","mechanism":"The actional branch colors the physical supports as products of sustained intention: Iram's standing is designed, aimed at, and maintained rather than accidental.","model_id":"base_purposive_construction"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base_purposive_construction","source_type":"hft","support_id":"sup_14444bd6493996e6672c","trust":"legacy_unbound"}]}
</lane_packet_json>
