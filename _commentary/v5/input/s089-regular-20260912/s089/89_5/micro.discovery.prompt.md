# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:5**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_5/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:5",
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
{"branch_registry":[{"boundary":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B001","candidate_links":[{"candidate_id":"cand_c611bb7effb19043c8a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"engelleme ve erişimi sınırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeye ulaşmanın, ondan yararlanmanın veya onun üzerinde işlem yapmanın önlenmesini anlatan genel karşılıktır.","boundary_detail":"Dal, katı nesne ya da çevrili mekan anlamını değil, erişimi veya işlem yapmayı önleyen sınırlandırmayı anlatır.","branch_image_ar":"المنع والإحاطة","concept_gloss":"engelleme ve erişimi sınırlama","contextual_glosses":[{"applicability":"Bir nesnenin, eylemin veya erişimin kuralla izin dışına çıkarıldığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kurallı biçimde izin vermeme ve erişimi önleme anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"yasaklama","usage_role":"contextual"},{"applicability":"Bir kişinin malı üzerinde hukuken işlem yapmasının önlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mal üzerindeki işlem yetkisinin yargısal olarak sınırlandırılmasını açıkça korur."},"facet_ids":["F003"],"text":"tasarruf yetkisini kısıtlama","usage_role":"explanatory"}],"definition":"Bir şeye ulaşmayı, ondan yararlanmayı ya da onun üzerinde işlem yapmayı engelleyen bir sınır koymadır. Bu çekirdek, bir şeyi yasak saymayı ve kişinin malı üzerindeki işlem yetkisini yargı kararıyla kısıtlamayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa erişmeyi, ondan yararlanmayı veya onun üzerinde işlem yapmayı engelleyen sınırlandırmadır."},{"facet_id":"F002","role":"specialization","statement":"Bir şeyi dokunulması ya da yapılması yasak saymak, genel engellemenin kurallı bir uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Bir kişinin malı üzerinde işlem yapma yetkisini yargı kararıyla kısıtlamak, çekirdeğin hukuki uygulamasıdır."}],"identity_rationale":"Kaynak ifadesi dalı tutarlı biçimde engelleme ve çevreleme ilkesiyle tanımlar; genel erişim engeli, yasaklama ve mal üzerinde işlem yapmanın yargı kararıyla kısıtlanması bu ilkenin açık uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erişimi veya işlem yapmayı engelleme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yasaklanmış, dokunulması önlenmiş şey"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"benden uzak dur; bana zarar vermen yasaktır"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sığınak ya da koruyucu dayanak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"geniş tutulmuş bir imkanı yasaklayıp daraltmak"}],"lexicalization_note":"Tanım genel engelleme çekirdeğini korur; belirli söz kalıplarındaki yasak, sığınma ve daraltma kullanımları yalnızca kendi sözcüksel karşılıklarında ele alınır.","neighbor_coverage_note":"Tüm adaylar incelendi; en güçlü iki sınır karşılaştırması yayımlandı, yalnızca koruma, aynı konu alanı veya uzak çağrışım paylaşan adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan izin vermemenin ve engellemenin alan örneklerini öne çıkarır; odak dal ise çevreleyici sınır fikrini ve kişinin mal üzerindeki işlem yetkisinin kaldırılmasını da kendi çekirdeğine bağlar.","focus_only":"Mal üzerinde işlem yetkisinin yargısal olarak kısıtlanmasını ve genel çevreleme ilkesini de kapsar.","gloss":"yasaklama ve engelleme","neighbor_only":"Ekin veya otlak kullanımını engelleme gibi belirli arazi kullanımlarına ayrıca uzanır.","neighbor_ref":"root_000338/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir eylemi, erişimi veya yararlanmayı izin alanının dışında bırakır."},{"boundary_match":"partial","distinction":"Odak dal engeli çevreleme ve hukuki işlem kısıtıyla kurar; komşu dal ise geçişi tutan kişilerden cezai sınıra kadar daha geniş bir alıkoyma düzeni taşır.","focus_only":"Çevreleme ilkesi ile mal üzerinde işlem yapma yetkisinin hukuken sınırlandırılmasını içerir.","gloss":"alıkoyma ve yasak koyma","neighbor_only":"Kapı görevlisi, tutuklu kişi ve yeniden suç işlemeyi önleyen ceza sınırı gibi rolleri içerir.","neighbor_ref":"root_000002/B002","relation_type":"near_synonym","shared_zone":"İki dal da giriş, çıkış veya eylem imkanını bir sınırla önleme alanında buluşur."}],"source_phrase_ar":"أصل واحد مطرد وهو المنع والإحاطة (maqayis)؛ الحجر والحجر لغتان وهو الحرام (ayn;tahdhib)؛ كل شيء حجرت عليه فقد منعت عنه (jamhara)؛ حجر عليه القاضي إذا منعه من التصرف في ماله (sihah)؛ وأصل الحجر في اللغة ما حجرت عليه أي منعته (tahdhib)؛ الحجر الممنوع منه بتحريمه (mufradat)","source_summary":"Kaynakların ortak anlatımı, temel anlamı engelleme ve çevreleme olarak verir; yasaklanmış şey ile mal üzerinde işlem yapması önlenen kişi bu ortak çekirdeğin belirgin uygulamalarıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه المنع والحظر والتحريم والاعتصام والذمام والمنعة ومنع التصرف في المال","what_is_not_ar":"ليس الحجر الصلب ولا الحجرة المبنية ولا دارة القمر"},"support_links":["sup_a78427d687a82ce6cde3"]},{"boundary":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_kind":"bare","branch_ref":"root_000296/B002","candidate_links":[{"candidate_id":"cand_fc0e8bdb54afc874a3cf","lane":"micro"},{"candidate_id":"cand_163b5ea0f853d568ac00","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"yanlıştan alıkoyan akıl","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Zihinsel yetinin düşünme ile davranışı dizginleme işlevlerinin birlikte anlatılması gereken bağlamlarda kullanılır.","boundary_detail":"Buradaki engel dışarıdan konan bir yasak değil, kişinin davranışını içeriden denetleyen anlama ve yargılama yetisidir.","branch_image_ar":"العقل الحاجز","concept_gloss":"yanlıştan alıkoyan akıl","contextual_glosses":[{"applicability":"Engelleyici işlevin bağlamdan anlaşıldığı doğal ve kısa kullanımlarda uygun karşılıktır.","error_profile":{"adds":null,"collision":"Genel zihinsel kapasite anlamıyla bağlam dışında karışabilir.","fit":"narrowing","loses":"Uygun olmayan davranıştan alıkoyma işlevini açıkça söylemez.","preserves":"Düşünme ve yargılama yetisi anlamını doğal biçimde korur."},"facet_ids":["F001"],"text":"akıl","usage_role":"general"}],"definition":"İnsanın düşünüp yargılamasını ve uygun olmayan davranışlardan kendini alıkoymasını sağlayan zihinsel yetidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlama ve yargılama gücü, kişiyi yapılmaması gereken davranışlardan alıkoyan içsel bir engel gibi işler."}],"identity_rationale":"Kaynak ifadesi, zihinsel yetiyi insanı uygun olmayan davranışlardan alıkoyma işlevi üzerinden tanımlar; dalın engelleyici akıl çerçevesi bu ilişkiyi doğru ve eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kişiyi yanlıştan alıkoyan akıl ve sağduyu"}],"lexicalization_note":"Dal yalın sözcükteki zihinsel yeti anlamını tanımlar ve başka yapılara özgü yasaklama ya da maddi çevreleme anlamlarını içeri almaz.","neighbor_coverage_note":"Tüm adaylar incelendi; zihinsel yetiyle doğrudan karışabilecek iki dal ve aynı kökün genel engelleme dalı seçildi, yalnızca sonuç veya konu yakınlığı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekler çok yakındır; odak dal uygun olmayan davranış ölçüsünü daha genel kurarken komşu dal engeli özellikle çirkin davranış ekseninde belirginleştirir.","focus_only":"Yapılması uygun olmayan davranışların bütününe karşı işleyen genel zihinsel yetiyi anlatır.","gloss":"kötü davranıştan alıkoyan akıl","neighbor_only":"Özellikle çirkin davranışı durduran zihinsel uyarı yönünü öne çıkarır.","neighbor_ref":"root_001560/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da akıl, kişiyi yanlış veya çirkin davranıştan geri tutan içsel güçtür."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı çekirdeği davranışı engelleme işlevidir; komşu dal aynı yetinin bilgi edinme, anlama ve sağlam karar verme boyutlarını da bağımsız bileşenler olarak taşır.","focus_only":"Zihinsel yetinin davranış üzerinde engelleyici bir sınır kurmasını merkez alır.","gloss":"anlama ve kendini dizginleme gücü","neighbor_only":"Bilgi, ayırt etme, anlama ve sağlam karar verme gibi bilişsel işlevleri daha geniş biçimde kapsar.","neighbor_ref":"root_001036/B001","relation_type":"near_synonym","shared_zone":"İki dal da anlayan, ayırt eden ve kişiyi yanlış davranıştan geri tutan zihinsel yetiyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir zihinsel yetiyi adlandırır; komşu dal ise nesnelere, eylemlere veya mal üzerindeki işlemlere getirilen engelleme eylemini ve durumunu adlandırır.","focus_only":"Engeli kuran şey kişinin kendi anlama ve yargılama yetisidir.","gloss":"içsel davranış engeli","neighbor_only":"Engel dışarıdan konan yasak, erişim sınırı veya yargısal işlem kısıtı olabilir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir eylemi yapılmaması gereken sınırın gerisinde tutma düşüncesini paylaşır."}],"source_phrase_ar":"العقل يسمى حجرا لأنه يمنع من إتيان ما لا ينبغي (maqayis)؛ والحجر العقل (jamhara)؛ والحجر العقل (sihah)؛ والحجر اللب والعقل (tahdhib)؛ فقيل للعقل حجر لكون الإنسان في منع منه مما تدعو إليه نفسه (mufradat)","source_summary":"Kaynaklar zihinsel yetiyi yalnızca düşünme gücü olarak değil, kişinin isteklerini denetleyip onu uygun olmayan eylemden geri tutan bir iç sınır olarak açıklar.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر بمعنى العقل واللب الذي يمنع صاحبه مما لا ينبغي","what_is_not_ar":"ليس التحريم ولا الحجر على المال ولا الحجارة"},"support_links":["sup_62a26cba386d7e726bcd","sup_c7ccb4b0d9457b7d5cbe"]},{"boundary":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"taş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sert ve katı doğal nesnenin tekil ya da tür adı olarak karşılandığı genel bağlamlarda kullanılır.","boundary_detail":"Dalın çekirdeği sert taş nesnesidir; türemiş eylemler, deyimsel felaket anlatımı ve altın-gümüş ikilisi yalnızca kendi birimleriyle sınırlıdır.","branch_image_ar":"الحَجَر الصلب","concept_gloss":"taş","contextual_glosses":[{"applicability":"Nesnenin katılığı ile tek bir parça oluşunun açıkça belirtilmesi gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın sert ve katı bir nesne oluşunu, tek parça görünümüyle birlikte korur."},"facet_ids":["F001"],"text":"sert taş parçası","usage_role":"explanatory"}],"definition":"Doğada bulunan, sert ve katı yapılı bilinen taş nesnesi ile bu nesnenin tekil ve çoğul örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bilinen sert ve katı taş nesnesini, tek bir parçayı ve aynı türden taşların çoğulunu anlatır."}],"identity_rationale":"Kaynak ifadesi dal düzeyinde bilinen sert taşı ve onun çoğul biçimlerini açıkça destekler. Geçici çerçevedeki taşlaşma, deyim ve özel adlandırmalar ise ayrı sözcüksel birimlerde bulunur ve yalın taş çekirdeğinin kurucu parçaları sayılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"taş; taşlar"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"taşlaşmak ve sertleşmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"başına çok çetin bir kişi ya da ağır bir iş gelmek"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"altın ve gümüş"}],"lexicalization_note":"Tanım yalın taş anlamını temel alır; taşlaşma, deyimsel kullanım ve özel ikili adlandırma ayrı sözcüksel karşılıklarda tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; genel taşla en kolay karışan iri kaya ve çakıl dalları ile aynı kökün çevrili mekan dalı yayımlandı, uzak deyim ve nitelik benzerlikleri elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıradan boyuttaki taşı da kapsayan genel addır; komşu dal ise aynı nesne alanını büyüklük ve kaya kütlesi niteliğiyle daraltır.","focus_only":"Boyut bakımından büyük olma şartı taşımayan genel taş türünü ve çoğulunu kapsar.","gloss":"iri ve sert kaya","neighbor_only":"Özellikle büyük ve kütleli kaya ya da iri taş olma sınırını taşır.","neighbor_ref":"root_000847/B001","relation_type":"near_synonym","shared_zone":"İki dal da sert, katı ve doğal taş maddesinden oluşan nesneleri adlandırır."},{"boundary_match":"partial","distinction":"Odak dal boyut ve zemin türü bakımından sınırsız genel taş adıdır; komşu dal küçük çakıl boyutuna ve çakıllı yüzeye özgüdür.","focus_only":"Küçük ya da büyük her türlü sıradan taş parçasını kapsayabilir.","gloss":"çakıl ve küçük taş","neighbor_only":"Küçük, yuvarlanmış çakıl parçalarını ve bunlarla kaplı zemini özellikle adlandırır.","neighbor_ref":"root_000332/B001","relation_type":"near_synonym","shared_zone":"Her iki dal taş maddesinden oluşan ayrık parçaları anlatır."},{"boundary_match":"partial","distinction":"Odak dal sınırı oluşturan malzeme ya da nesnedir; komşu dal ise bu veya başka bir sınırın içinde kalan mekandır.","focus_only":"Sınır kurup kurmamasından bağımsız olarak taş maddesini ve taş parçasını adlandırır.","gloss":"taş ile çevrili yer ayrımı","neighbor_only":"Taş veya duvarla çevrilmiş alanı, odayı, ağılı ya da yerleşim bölümünü adlandırır.","neighbor_ref":"root_000296/B004","relation_type":"near_neighbor","shared_zone":"Çevrili mekanın sınırı taşla kurulabildiği için iki dal aynı somut sahnede buluşabilir."}],"source_phrase_ar":"والحجر معروف (maqayis)؛ الأحجار جمع الحجر والحجارة جمع الحجر أيضا (ayn)؛ الحجر معروف ويجمع أحجارا وحجارة (jamhara)؛ الحجر جمعه في القلة أحجار وفي الكثرة حجار وحجارة (sihah)؛ الحجر وجمعه الحجارة (tahdhib)؛ الحجر الجوهر الصلب المعروف وجمعه أحجار وحجارة (mufradat)","source_summary":"Kaynaklar ortak biçimde bilinen sert taş nesnesini tanır ve bu nesne için birden çok çoğul biçimin kullanıldığını belirtir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر المعروف والحجارة والصلابة والتحجر وما يلحق بذلك من أمثال وأسماء مبنية على الحجارة","what_is_not_ar":"ليس الحرام ولا العقل ولا الحجرة المحوطة"},"support_links":[]},{"boundary":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"çevrili yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Duvar, taş veya başka bir sınır içinde kalan mekanın genel ve türden bağımsız karşılığıdır.","boundary_detail":"Dal sınırın yapıldığı taşı veya duvarı değil, sınırın içinde kalan yeri ve bu modele göre adlandırılmış mekanları anlatır.","branch_image_ar":"المكان المحوط","concept_gloss":"çevrili yer","contextual_glosses":[{"applicability":"Bir yapının içinde duvarlarla ayrılmış yaşama veya kullanma bölümü anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapı içinde sınırlarla ayrılmış kapalı bölüm anlamını eksiksiz korur."},"facet_ids":["F002"],"text":"oda","usage_role":"contextual"},{"applicability":"Hayvanların çevrili bir alanda tutulduğu barınak bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanları sınır içinde bir arada tutan çevrili barınak anlamını korur."},"facet_ids":["F003"],"text":"ağıl","usage_role":"contextual"},{"applicability":"Bir evin ya da yerleşimin yakınındaki ayrılmış ve korunan alan anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşimin yakınında sınırlandırılmış ve korunan alan anlamını tam olarak korur."},"facet_ids":["F004"],"text":"korunan çevre","usage_role":"explanatory"}],"definition":"Duvar, taş dizisi ya da başka bir sınırla çevrilmiş ve dışarıdan ayrılmış yerdir. Oda, hayvan ağılı, bir yerleşimin yanı ve bu çevreleme modeline göre adlandırılmış belirli mekanlar bu çekirdeğin uygulamalarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir sınır, duvar veya taş çevre içinde kalan ve dışarıdan ayrılan mekandır."},{"facet_id":"F002","role":"specialization","statement":"Bir yapının içindeki oda ya da ayrılmış bölüm, çevrili mekanın yapı içindeki uygulamasıdır."},{"facet_id":"F003","role":"specialization","statement":"Hayvanları bir arada tutan çevrili ağıl, çekirdeğin barınak uygulamasıdır."},{"facet_id":"F004","role":"extension","statement":"Bir topluluğun evinin veya yerleşiminin yanı ve korunan çevresi, mekan çekirdeğinin alan uzantısıdır."},{"facet_id":"F005","role":"source_variant","statement":"Kaynaklarda kutsal bir yapının çevrili yanı ile eski bir topluluğun yurdu da bu çevreleme modeline göre adlandırılır."}],"identity_rationale":"Kaynak ifadesi oda, duvarla çevrili yer, hayvan ağılı, evin yanı ve belirli kutsal ya da eski yer adlarını çevrilmiş alan ilişkisiyle birlikte verir; mekan merkezli dal çerçevesi bu ortak yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kutsal yapının çevrili yan bölümü"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"eski bir topluluğun yurt edindiği bölge"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"oda, çevrili yer veya ağıl"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"topluluğun evinin yanı ya da korunan çevresi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"vadide veya çukur yerde suyu tutan setli alan"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bahçe, koruluk veya köy çevresindeki korunan alan"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çevrili bir yer edinmek"}],"lexicalization_note":"Genel çevrili mekan çekirdeği ile oda ve ağıl uygulamaları tanımda ayrılır; belirli yapı, yer, su tutma alanı ve köy çevresi kullanımları kendi birimlerine bağlı kalır.","neighbor_coverage_note":"Tüm adaylar incelendi; ağıl, duvar ve ayrılmış yapı bölümüyle kurulan en açıklayıcı üç sınır yayımlandı, yalnızca aynı sahneyi paylaşan uzak mekan adayları elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal hayvan ağılına ve kapsama işlevine özgüdür; odak dal aynı çevreleme düzenini odadan yerleşim çevresine kadar daha geniş mekanlara taşır.","focus_only":"Oda, ev yanı, kutsal yapı bölümü ve geniş yerleşim alanı gibi farklı mekan türlerini kapsar.","gloss":"çevrili ağıl","neighbor_only":"İçindekileri bir arada tutan ağıl olma işlevini adlandırmanın açık merkezi yapar.","neighbor_ref":"root_000036/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir sınırın içindekileri dışarıdan ayırdığı çevrili mekanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal çevrelenen iç mekandır; komşu dal ise bu mekanı oluşturan dik sınır yapısıdır ve iç alanın kendisi yerine duvarı öne çıkarır.","focus_only":"Duvarın veya sınırın içinde kalan oda, ağıl ya da bölgeyi adlandırır.","gloss":"çevrili alan ile duvar ayrımı","neighbor_only":"Alanı çevreleyen yükseltilmiş duvarı, seti veya suyu tutan yapı unsurunu adlandırır.","neighbor_ref":"root_000228/B001","relation_type":"near_neighbor","shared_zone":"Bir duvarın çevrelediği mekan sahnesinde iki dal doğrudan yan yana bulunur."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yalnızca çevrilmiş olmaktır; komşu dal ise büyük yapı ya da yapı içindeki özel ayrılmış kesim türlerini kendi adlandırma alanına alır.","focus_only":"Basit oda, hayvan ağılı ve yerleşim çevresi gibi büyük yapı niteliği gerektirmeyen mekanları kapsar.","gloss":"ayrılmış yapı bölümü","neighbor_only":"Büyük yapı olarak sarayı ve ev ya da ibadet yapısı içindeki özel ayrılmış bölümü kapsar.","neighbor_ref":"root_001231/B005","relation_type":"near_neighbor","shared_zone":"İki dal da duvarlarla belirlenmiş bir yapı veya yapı içi bölüm alanında buluşur."}],"source_phrase_ar":"حجرة القوم ناحية دارهم والحجرة من الأبنية معروفة (maqayis)؛ الحجر حطيم مكة وحجر موضع كان لثمود والحجرة ناحية كل موضع (ayn)؛ الحجر حجر الكعبة والحجر بلاد ثمود والحجرة الحائط يحجر على دار (jamhara)؛ الحجرة حظيرة الإبل ومنه حجرة الدار والحجر حجر الكعبة والحجر منازل ثمود (sihah)؛ الحجرة التي ينزلها الناس وهو ما حوطوا عليه (tahdhib)؛ سمي ما أحيط به الحجارة حجرا وبه سمي حجر الكعبة وديار ثمود (mufradat)","source_summary":"Kaynaklar çevrelenerek ayrılmış yer çekirdeğinde birleşir; oda, duvarlı bölüm, hayvan ağılı, evin yakını, kutsal bir yapının yanı ve eski bir yerleşim alanı bu mekan düzeninin farklı gerçekleşmeleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجرة والحائط والحظيرة وحجر الكعبة وديار ثمود والحديقة والحاجر ومحجر القرية","what_is_not_ar":"ليس الحِجر بمعنى الحضن ولا دارة القمر ولا الفرس الأنثى"},"support_links":[]},{"boundary":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"kucak ve yakın koruma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bedensel kucak alanı ile bundan gelişen koruma ilişkisini birlikte karşılamanın gerektiği genel açıklamalarda kullanılır.","boundary_detail":"Dal genel yasaklamayı ya da yapı içindeki odayı değil, kucak alanını ve bir kişinin yakın koruması altında bulunma durumunu anlatır.","branch_image_ar":"الحِجر والحضن","concept_gloss":"kucak ve yakın koruma","contextual_glosses":[{"applicability":"Bir insanın otururken gövdesi ile bacakları arasındaki yakın tutma alanı anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bedensel yakınlık ve birini ya da bir şeyi sararak tutma alanını korur."},"facet_ids":["F001"],"text":"kucak","usage_role":"general"},{"applicability":"Bir kişinin başka birinin yakın koruması ve denetimi altında bulunduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Birinin yakın koruması ve gözetimi altında bulunma ilişkisini doğal biçimde korur."},"facet_ids":["F002"],"text":"kanadı altında","usage_role":"contextual"}],"definition":"İnsanın otururken gövdesi ile bacakları arasında oluşan, birini ya da bir şeyi yakınında tutup sardığı kucak alanıdır. Bu bedensel yakınlık, birinin koruması ve denetimi altında bulunma ilişkisine de uzanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın gövdesi ile bacakları arasında, birini veya bir şeyi yakında tutmaya yarayan kucak alanıdır."},{"facet_id":"F002","role":"extension","statement":"Birinin kucağında ya da kanadı altında olmak, onun yakın koruması ve denetimi altında bulunmayı anlatır."}],"identity_rationale":"Kaynak ifadesi insanın, özellikle kadının, kucağını ve birinin kucağında ya da kanadı altında bulunmayı birlikte verir; yakın bedensel alan ile bu alandan gelişen koruma ilişkisi dal çerçevesinde doğru biçimde ayrılabilir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kucak, yakın sığınak ve koruma"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinin kanadı ve denetimi altında"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"gömleğin içinde bir şeyi tutan kıvrım"}],"lexicalization_note":"Kucak anlamı ile yakın koruma uzantısı tanımda ayrılır; birinin kanadı altında bulunma ve gömlek kıvrımı kullanımları kendi sözcüksel birimleriyle sınırlıdır.","neighbor_coverage_note":"Tüm adaylar incelendi; sığınak, sarılma ve genel engelleme ile kurulabilecek başlıca karışıklıklar yayımlandı, yalnızca aile veya koruma sahnesini uzaktan paylaşanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık üzerinden kurar; komşu dal ise kişiden bağımsız fiziksel siperleri ve doğa koşullarından saklanmayı da kapsar.","focus_only":"İnsanın bedensel kucak alanını ve bu alana dayalı yakın denetimi içerir.","gloss":"sığınak ve kanat altı","neighbor_only":"Rüzgar, soğuk veya güneşten koruyan ağaç ve benzeri siperleri de kapsar.","neighbor_ref":"root_000513/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişi ya da nesnenin yakınına girerek korunma durumunu anlatır."},{"boundary_match":"partial","distinction":"Odak dal bir yer ve koruma ilişkisi olarak kucağı anlatır; komşu dal ise bedenlerin birbirine sarılması eylemini anlatır.","focus_only":"Kucak olarak kullanılan bedensel alanı ve orada korunma durumunu adlandırır.","gloss":"kucak ile sarılma ayrımı","neighbor_only":"İki bedenin birbirine sarılması ve bu temasın sürdürülmesi eylemini adlandırır.","neighbor_ref":"root_001354/B005","relation_type":"near_neighbor","shared_zone":"İki dal bedensel yakınlık, sarma ve temas sahnesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal korumayı kucak ve kişisel yakınlık ilişkisiyle somutlaştırır; komşu dalın çekirdeği ise herhangi bir erişim ya da işlemi engellemektir.","focus_only":"Yakın bedensel alanı ve bir kişinin koruması altında bulunmayı içerir.","gloss":"yakın koruma ile engelleme ayrımı","neighbor_only":"Genel erişim yasağını ve mal üzerinde işlem yapma yetkisinin hukuken kısıtlanmasını içerir.","neighbor_ref":"root_000296/B001","relation_type":"near_neighbor","shared_zone":"Korunan kişiye dışarıdan müdahaleyi önleme düşüncesi iki dalı birbirine bağlar."}],"source_phrase_ar":"الحجر حجر الإنسان وقد تكسر حاؤه (maqayis)؛ حجر المرأة وحجرها لغتان للحضنين (ayn)؛ حجر المرأة وقالوا حجرها (jamhara)؛ حجر الإنسان وحجره والجمع حجور (sihah)؛ حجر المرأة وحجرها حضنها وفلان حجر فلان أي في كنفه ومنعته (tahdhib)؛ فلان في حجر فلان أي في منع منه وجمعه حجور (mufradat)","source_summary":"Kaynaklar kucak alanını ortak çekirdek olarak verir; bir kişinin yakınında, korumasında ve denetimi altında bulunma ilişkisi bu bedensel alandan gelişen uzantıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه حجر الإنسان وحجر المرأة والحضن والكنف والمنعة القريبة","what_is_not_ar":"ليس حجر القاضي على المال ولا حجر الكعبة ولا الحجر الصلب"},"support_links":[]},{"boundary":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000296/B006","candidate_links":[{"candidate_id":"cand_c611bb7effb19043c8a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"çevreleyen halka veya sınır","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesnenin çevresini halka, çizgi ya da belirgin bölge olarak kuşatan biçimin genel karşılığıdır.","boundary_detail":"Dal her türlü daireselliği kapsamaz; bir nesnenin, özellikle ayın ya da gözün, çevresini belirleyen halka, iz ve bölgeyle sınırlıdır.","branch_image_ar":"الدائرة حول الشيء","concept_gloss":"çevreleyen halka veya sınır","contextual_glosses":[{"applicability":"Ayın çevresinde ince ve yuvarlak bir ışık kuşağı görüldüğü gökyüzü bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayın çevresinde beliren ince ve yuvarlak halka görünümünü açıkça korur."},"facet_ids":["F002"],"text":"ayın çevresindeki ışık halkası","usage_role":"contextual"},{"applicability":"Bir hayvanın gözünün çevresinin yuvarlak bir damgayla işaretlendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın göz çevresinde damgayla yuvarlak bir iz oluşturma eylemini tam korur."},"facet_ids":["F003"],"text":"göz çevresine yuvarlak damga vurmak","usage_role":"explanatory"},{"applicability":"Gözün çevresindeki anatomik bölge veya yüz örtüsünün göz yanında durduğu kesim anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gözün çevresindeki belirgin yüz bölgesini ve sınır niteliğini korur."},"facet_ids":["F004"],"text":"göz çukuru çevresi","usage_role":"contextual"}],"definition":"Bir şeyin, özellikle ayın ya da gözün, çevresini halka, ince çizgi veya belirgin bir bölge halinde kuşatan çevredir. Hayvan gözünün çevresine yuvarlak damga vurma eylemi bu biçimi kasıtlı olarak oluşturur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesnenin çevresini halka, çizgi veya belirgin bölge halinde kuşatan çevre sınırıdır."},{"facet_id":"F002","role":"specialization","statement":"Ayın çevresinde beliren ince halka, çevre sınırının gökyüzündeki görünümüdür."},{"facet_id":"F003","role":"associated_use","statement":"Bir hayvanın göz çevresine yuvarlak damga vurmak, halka biçimli sınırı kasıtlı olarak oluşturma eylemidir."},{"facet_id":"F004","role":"extension","statement":"Göz çukuru çevresi ile yüz örtüsünün göz çevresine oturduğu bölüm, çekirdeğin bedensel alan uzantısıdır."}],"identity_rationale":"Kaynak ifadesi ayın çevresindeki halka, hayvan gözünün çevresine vurulan yuvarlak damga ve göz çevresi bölgesini ortak bir çevre çizgisi ilişkisiyle birleştirir. Dal korunabilir, ancak çekirdek dönme eylemi değil bir şeyi kuşatan halka, iz veya çevre bölgesidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"ayın çevresinde ince bir halka belirmek"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hayvanın göz çevresine yuvarlak damga vurmak"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"göz çukuru çevresi veya yüz örtüsünün gözü açıkta bırakan bölümü"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"çocukların çizilmiş bir çember çevresinde oynadığı oyun"}],"lexicalization_note":"Genel çevre halkası çekirdeği korunur; ay halkası, göz çevresine damga vurma, göz çevresi bölgesi ve çocuk oyunu yalnızca kendi yapılardaki kullanımlarıyla ayrılır.","neighbor_coverage_note":"Tüm adaylar incelendi; ay halkası, genel dairesellik ve çevresini kuşatma ile kurulan üç temel sınır yayımlandı, yalnızca biçim ya da aynı sahne çağrışımı taşıyanlar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ay bağlamında karşılıklar çok yakındır; odak dal aynı çevre biçimini göz çevresi ve yuvarlak damga alanına da taşırken komşu dal yalnızca ay halkasına özgüdür.","focus_only":"Göz çevresi, yüz bölgesi ve göz çevresine vurulan yuvarlak damga kullanımlarını da kapsar.","gloss":"ayın çevresindeki halka","neighbor_only":"Ay çevresindeki ışık görünümünü bağımsız ve yalnızca gökyüzüne özgü bir anlam olarak adlandırır.","neighbor_ref":"root_001613/B003","relation_type":"near_synonym","shared_zone":"İki dal da ayın çevresinde görülen yuvarlak kuşağı doğrudan anlatır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği çevreleyen sınırın kendisidir; komşu dal ise hem daire biçimini hem de dönme ve döndürme hareketini kapsayan daha geniş bir süreç alanına sahiptir.","focus_only":"Bir nesnenin çevresini kuşatan sabit halka, iz veya anatomik bölgeyi merkez alır.","gloss":"çevre halkası ile dönme ayrımı","neighbor_only":"Dönme eylemini, dönüş döngüsünü ve döndürülen araç ya da nesneleri geniş biçimde kapsar.","neighbor_ref":"root_000499/B001","relation_type":"near_neighbor","shared_zone":"Daire biçimi ve bir merkez çevresinde düzenlenme iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal çevrede oluşan biçim veya bölgedir; komşu dal ise katılımcıların bir nesnenin etrafını çevirmesi eylemidir.","focus_only":"Halka, ince çizgi, damga izi veya göz çevresi gibi kalıcı ya da görünür sınırı adlandırır.","gloss":"çevre çizgisi ile kuşatma ayrımı","neighbor_only":"İnsanların veya başka ögelerin bir şeyin çevresinde toplanıp onu kuşatması eylemini adlandırır.","neighbor_ref":"root_000300/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal bir merkezin bütün çevresinin sarılması ilişkisini taşır."}],"source_phrase_ar":"حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين ما يدور بها (maqayis)؛ المحجر حيث يقع عليه النقاب من الوجه (ayn)؛ حجر القمر إذا صارت حوله دارة وحجرت عين البعير إذا وسمت حولها بميسم مستدير ومحجر العين معروف (jamhara)؛ حجر القمر إذا استدار بخط دقيق والتحجير أن تسم حول عين البعير بميسم مستدير (sihah)؛ المحجر من الوجه حيث يقع عليه النقاب والمحجر العين (tahdhib)؛ حجرت عين الفرس إذا وسمت حولها بميسم وحجر القمر صار حوله دائرة ومحجر العين منه (mufradat)","source_summary":"Kaynak anlatımı ay çevresindeki ince halkayı, hayvan gözünün çevresine vurulan yuvarlak damgayı ve göz ya da yüz çevresindeki bölgeyi aynı çevreleme biçiminin farklı uygulamaları olarak bir araya getirir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه دارة القمر والوسم المستدير حول عين الدابة ومحجر العين وما يشبه الخط المستدير","what_is_not_ar":"ليس الحائط والحجرة ولا الحجر بمعنى الحرام"},"support_links":["sup_a78427d687a82ce6cde3"]},{"boundary":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_kind":"bare","branch_ref":"root_000296/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","surface_ar":"حِجْرٍ"}],"gloss":"dişi at, özellikle damızlık kısrak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referent, genel hayvan türü içinde özellikle dişi attır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}}],"root_ar":"ح ج ر","root_id":"root_000296","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dişi at çekirdeği ile üreme için ayrılıp korunma niteliğinin birlikte gösterilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal genel olarak dişi hayvanı değil dişi atı anlatır; koruma ve damızlık için ayırma bu referentin belirgin fakat kaynaklarda farklı vurgulanan nitelikleridir.","branch_image_ar":"الفرس الأنثى المصونة","concept_gloss":"dişi at, özellikle damızlık kısrak","contextual_glosses":[{"applicability":"Yalnızca hayvanın cinsiyeti ve türünün gerekli olduğu doğal metin bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dişi at referentini kısa ve doğal biçimde eksiksiz korur."},"facet_ids":["F001"],"text":"kısrak","usage_role":"general"},{"applicability":"Dişi atın üreme için ayrılıp özenle korunduğu yetiştiricilik bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yalnızca seçilmiş bir erkekle çiftleştirilme koşulunu açıkça belirtmez.","preserves":"Dişi atın üreme amacıyla ayrılması ve korunması anlamını korur."},"facet_ids":["F002"],"text":"damızlık kısrak","usage_role":"contextual"}],"definition":"Dişi at, özellikle üreme için ayrılıp korunan ve yalnızca seçilmiş bir erkekle çiftleştirilen kısraktır. Adlandırma kaynaklarda ayrıca karnında yavru taşımasına bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referent, genel hayvan türü içinde özellikle dişi attır."},{"facet_id":"F002","role":"specialization","statement":"Dişi atın üreme için ayrılması, özenle korunması ve yalnızca seçilmiş bir erkekle çiftleştirilmesi belirgin yetiştirme uygulamasıdır."},{"facet_id":"F003","role":"source_variant","statement":"Adlandırma, dişi atın karnında yavru taşıyıp onu içinde barındırmasıyla da açıklanır."}],"identity_rationale":"Kaynak ifadesi dişi atı temel referent olarak verir ve onu korunan, üreme için ayrılan, seçilmiş erkek dışında çiftleştirilmeyen ya da yavru taşıyan hayvan olarak açıklar; geçici dal çerçevesi bu ortak alanı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"korunan ya da damızlık olarak ayrılan kısrak"}],"lexicalization_note":"Dal yalın sözcükteki dişi at anlamını tanımlar; koruma, damızlık için ayırma ve yavru taşıma açıklamaları aynı referentin sınırları içinde tutulur.","neighbor_coverage_note":"Tüm adaylar incelendi; üreyen dişi hayvan, korunan seçkin hayvan ve yavru-soy alanlarıyla kurulan üç açıklayıcı karşılaştırma yayımlandı, yalnızca erkek hayvan ya da çiftleşme olayı odaklı adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tür bakımından dişi atla sınırlıdır ve seçici çiftleştirmeyi vurgular; komşu dal üreme değeri taşıyan dişi hayvanları daha geniş bir tür alanında toplar.","focus_only":"Yalnızca at türündeki dişiyi ve seçilmiş erkekle çiftleştirme kısıtını kapsar.","gloss":"yavru vermesi beklenen dişi hayvan","neighbor_only":"At dışındaki mal ve çiftlik hayvanlarının yavru vermesi beklenen dişilerini de kapsar.","neighbor_ref":"root_000233/B006","relation_type":"near_synonym","shared_zone":"İki dal da yavru üretmesi beklenen ve bu amaçla değer verilen dişi hayvanı anlatır."},{"boundary_match":"partial","distinction":"Odak dal dişi atı damızlık olarak korur; komşu dal ise seçkin deveyi güvenilir yedek olarak saklar ve aynı çiftleştirme sınırını taşımaz.","focus_only":"Korunan hayvan dişi attır ve üreme amacı ile eş seçimi açıkça belirleyicidir.","gloss":"özenle saklanan seçkin hayvan","neighbor_only":"Korunan hayvan devedir; seçim cinsiyetten çok yormadan saklama, güvenilir yedek ve sürü niteliğine dayanır.","neighbor_ref":"root_001235/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal da değerli bir hayvanın yıpratılmadan korunup gelecekteki yarar için ayrılmasını anlatır."},{"boundary_match":"field_only","distinction":"Odak dal üremeye katılan korunan dişi hayvandır; komşu dal ise üremenin sonucu olan yavruyu ve kuşaklar boyunca çoğalan soyu anlatır.","focus_only":"Üreme için ayrılan ana hayvanı, yani dişi atı adlandırır.","gloss":"damızlık ana ile yavru-soy ayrımı","neighbor_only":"Doğan yavruyu, soyu ve canlıların birbirinden çoğalmasını adlandırır.","neighbor_ref":"root_001499/B001","relation_type":"same_field","shared_zone":"İki dal hayvan yetiştiriciliği, çiftleşme ve neslin sürdürülmesi alanını paylaşır."}],"source_phrase_ar":"والحجر الفرس الأنثى وهي تصان ويضن بها (maqayis)؛ أحجار الخيل ما اتخذ منها للنسل (ayn)؛ سميت الأنثى من الخيل حجرا لأنها حجرت عن الذكور إلا عن فحل كريم (jamhara)؛ والحجر أيضا الأنثى من الخيل (sihah)؛ الحجر الفرس الأنثى وما اتخذ منها للنسل (tahdhib)؛ يقال للأنثى من الفرس حجر لكونها مشتملة على ما في بطنها من الولد (mufradat)","source_summary":"Kaynaklar referentin dişi at olduğu konusunda birleşir; korunan ve üreme için ayrılan hayvan oluşu, seçilmiş erkek dışında çiftleştirilmemesi ve karnında yavru taşıması adlandırmayı açıklayan tamamlayıcı vurgulardır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الحجر من الخيل وهي الأنثى المصونة أو المعدة للنسل","what_is_not_ar":"ليس حجر المرأة ولا الحجر الصلب ولا الحرام"},"support_links":[]},{"boundary":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yüz güzelliği","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın soyut güzellik çekirdeğini ve güzelliğin özellikle yüzde görünmesini birlikte karşılar.","boundary_detail":"Dal, malı bölme, yemin etme, öğle sıcağı ve öteki eşsesli anlamları kapsamaz.","branch_image_ar":"حسن موزع في الوجه","concept_gloss":"yüz güzelliği","contextual_glosses":[{"applicability":"Bir kişiyi yüzünün güzelliğiyle niteleyen kullanımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soyut güzellik adı olarak kullanılabilme yönünü dışarıda bırakır.","preserves":"Kişinin yüz güzelliğini ve olumlu görünüşünü korur."},"facet_ids":["F002"],"text":"güzel yüzlü","usage_role":"contextual"},{"applicability":"Doğrudan yüzün kendisinin güzel diye nitelendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin bütünü için kullanılan niteleme ve soyut nitelik adı kapsamını kaybeder.","preserves":"Güzelliğin yüzde gerçekleşmesi yönünü korur."},"facet_ids":["F001","F002"],"text":"güzel yüz","usage_role":"contextual"}],"definition":"Yüzde ya da kişinin görünüşünde beliren güzellik ve yüz güzelliği niteliğidir. Bazı kullanımlar doğrudan güzel yüzü, bazıları da böyle bir yüze sahip kişiyi niteler.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüzde veya insan görünüşünde algılanan güzellik niteliğini bildirir."},{"facet_id":"F002","role":"specialization","statement":"Güzel yüzün kendisini ya da güzel yüzlü kişiyi niteleyen kullanımları kapsar."}],"identity_rationale":"Kaynak ifadesi, güzelliği özellikle yüzde görülen bir nitelik olarak verir; hem soyut güzellik adlarını hem de güzel yüzlü kişi ve yüz betimlemelerini kapsar. Bu nedenle dalın yüz güzelliği ekseni kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"güzellik, güzel görünüş"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"eksiksiz güzellik"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yüz, özellikle yüzün güzel bölümü"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yakışıklı ya da güzel yaradılışlı erkek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"güzel yüzlü"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"yüzü güzel ve uyumlu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"güzel yüz"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güzel yüzlü kadın"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güzel"}],"lexicalization_note":"Tanım, yalın güzellik adlarıyla yüzü niteleyen kalıpları ayırır; kalıba bağlı kişi nitelemelerini bütün dalın tek biçimi saymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalnızca genel güzellik ve yüz uyumu dalları, yüz merkezli sınırı açıklayan yararlı karşılaştırmalar sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yüz merkezli ve kişi nitelemelerine açıkken komşu dal nesnelere de uzanan genel güzellik ile kusursuzluğu bir araya getirir.","focus_only":"Güzelliği özellikle insan yüzünde ve güzel yüzlü kişi nitelemelerinde toplar.","gloss":"güzellik ve kusursuzluk","neighbor_only":"Her türlü şeyin güzelliğini ve kusurdan arınmışlığını daha geniş biçimde kapsar.","neighbor_ref":"root_000660/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin ya da yüzün güzel oluşunu bildirir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği güzelliktir; komşu dalın çekirdeği ise güzelliği doğuran yüz oranlarının karşılıklı dengelenmesidir.","focus_only":"Yüz güzelliğini uyumun nasıl kurulduğunu şart koşmadan bildirir.","gloss":"yüz güzelliğindeki uyum","neighbor_only":"Yüz parçalarının birbirine denk ve dengeli oluşunu güzelliğin belirleyici koşulu yapar.","neighbor_ref":"root_001511/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal yüzün güzel görünmesi alanında buluşur."}],"source_phrase_ar":"القسام وهو الحسن والجمال (maqayis)؛ القسيم من الرجال الحسن الخلق والقسمة الوجه (ayn)؛ القسام: الحسن وفلان قسيم الوجه ومقسم الوجه (sihah)؛ القسامة: الحسن التام ووجه مقسم أي حسن (tahdhib)؛ فلان مقسم الوجه وقسيم الوجه والقسامة الحسن (mufradat)","source_summary":"Kaynaklar, bu anlam alanında güzelliği ve yüz güzelliğini ortak çekirdek olarak verir; ad ve niteleme biçimleri güzel yüzü veya güzel yüzlü kişiyi anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حسن الوجه والقسمة والقسامة بمعنى الحسن، ووصف الرجل أو الوجه بأنه قسيم أو مقسم.","what_is_not_ar":"ليس هو تقسيم المال أو الحظوظ، ولا اليمين، ولا الاستقسام بالأزلام."},"support_links":[]},{"boundary":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_kind":"bare","branch_ref":"root_001226/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"şiddetli öğle sıcağı veya vakti","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynaklardaki sıcaklık yoğunluğu ile gün ortası zamanı okumalarının ikisini de açıkça taşır.","boundary_detail":"Anlam, genel sıcaklığa değil özellikle gün ortasındaki şiddetli sıcağa veya onun vaktine bağlıdır.","branch_image_ar":"حر الهاجرة","concept_gloss":"şiddetli öğle sıcağı veya vakti","contextual_glosses":[{"applicability":"Sözün sıcaklığın şiddetini anlattığı metinlerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sözcüğün doğrudan bir vakti adlandırabildiği okumasını kaybeder.","preserves":"Gün ortasındaki sıcaklığın yüksek şiddetini korur."},"facet_ids":["F001"],"text":"kavurucu öğle sıcağı","usage_role":"contextual"},{"applicability":"Sözün günün sıcak bir zaman dilimini adlandırdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıcağın şiddetini başlı başına adlandıran okumayı geri plana iter.","preserves":"Gün ortasıyla sıcaklığın birlikte belirlediği vakti korur."},"facet_ids":["F002"],"text":"öğle sıcağı vakti","usage_role":"contextual"}],"definition":"Gün ortasında bastıran şiddetli sıcak ya da bu sıcağın yaşandığı vakittir. Kaynak anlatımı yoğunluk ile zaman adlandırmasını yan yana bırakır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün ortasında hissedilen şiddetli sıcağı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı söz, şiddetli öğle sıcağının yaşandığı vakti de adlandırır."}],"identity_rationale":"Kaynak ifadesi tek bir noktada birleşmez: bir aktarım sözcüğü öğle sıcağının şiddeti, diğeri ise bu sıcağın görüldüğü vakit olarak açıklar. Dal korunabilir, ancak hem yoğunluk hem zaman okuması açıkça belirtilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şiddetli öğle sıcağı veya öğle sıcağı vakti"}],"lexicalization_note":"Tanım yalın dalı kapsar ve başka dallardaki güzellik, bölüştürme ya da yemin anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; gün ortası sıcağı dalı tam örtüşme, yaz sıcağı dalı ise zaman sınırını gösteren yakın karşılaştırma sağladı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek anlam ve sınırlar aynıdır; komşu karttaki hareket ve yemek bağlantıları bu ortak çekirdeğin bağımlı kullanımlarıdır.","focus_only":null,"gloss":"öğle sıcağı ve vakti","neighbor_only":null,"neighbor_ref":"root_001578/B005","relation_type":"synonym","shared_zone":"Her iki dal da gün ortasındaki şiddetli sıcağı ve bu sıcağın vaktini çekirdek anlam yapar."},{"boundary_match":"partial","distinction":"Odak dal gün ortasıyla sınırlıyken komşu dal yaz mevsimi ve sıcak dönemin süresi üzerinden daha geniş bir zaman çerçevesi kurar.","focus_only":"Sıcağı özellikle gün ortasına bağlar ve vakit adı olarak da kullanır.","gloss":"şiddetli yaz sıcağı","neighbor_only":"Şiddetli yaz sıcağını veya bunun sürdüğü dönemi gün ortası şartı olmadan anlatır.","neighbor_ref":"root_001672/B004","relation_type":"near_synonym","shared_zone":"İki dal da ağır ve bunaltıcı sıcaklık alanını paylaşır."}],"source_phrase_ar":"والقسام في شعر النابغة شدة الحر (maqayis)؛ القسام: وقت الهاجرة (tahdhib)","source_summary":"Toplu kaynak anlatımı, sözü bir yandan şiddetli öğle sıcağına, öte yandan bu sıcağın vaktine bağlar; bu iki okuma tek bir yoğun gün ortası sahnesinde birleşir.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه القسام بمعنى شدة الحر أو وقت الهاجرة كما في الشواهد.","what_is_not_ar":"ليس هو القسام بمعنى الحسن، ولا القسام الذي يقسم بين الناس."},"support_links":[]},{"boundary":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B003","candidate_links":[{"candidate_id":"cand_c611bb7effb19043c8a8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"paylara ayırma ve ayrılmış pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşlem olarak bölüştürmeyi ve sonuç olarak belirlenen payı aynı kısa karşılıkta korur.","boundary_detail":"Dal, yemin etmeyi ve payın ok çekerek aranmasını değil gerçek bölme, dağıtma ve belirlenmiş payı kapsar.","branch_image_ar":"إفراز النصيب وتقسيم الشيء","concept_gloss":"paylara ayırma ve ayrılmış pay","contextual_glosses":[{"applicability":"Bir şeyin kişiler veya paylar arasında dağıtıldığı işlem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İşlem sonunda ortaya çıkan belirli payı ad olarak karşılamaz.","preserves":"Bütünü paylara ayırma ve dağıtma işlemini korur."},"facet_ids":["F001","F003"],"text":"bölüştürme","usage_role":"general"},{"applicability":"Bir bölüştürme sonucunda kişiye düşen bölümün anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bütünü ayırma ve payları dağıtma işlemini karşılamaz.","preserves":"Bir kimseye ayrılan belirli bölüm veya hak sonucunu korur."},"facet_ids":["F002"],"text":"pay","usage_role":"contextual"}],"definition":"Bir şeyi parçalara ya da hak sahiplerinin paylarına ayırma ve dağıtma işlemidir; ayrıca bu işlem sonunda ayrılan payı bildirir. Paylaşmaya katılan kişi ve miras ya da ganimetin sahiplerine dağıtılması bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bütünü parçalara, kişilere veya belirlenmiş paylara ayırma ve dağıtma işlemini bildirir."},{"facet_id":"F002","role":"core","statement":"Ayırma işlemi sonunda bir kimseye düşen belirli payı veya hakkı bildirir."},{"facet_id":"F003","role":"specialization","statement":"Birlikte paylaşan kişiyi ve miras ya da savaş kazancının hak sahiplerine dağıtılmasını kapsar."}],"identity_rationale":"Kaynak ifadesi bir bütünü parçalara veya hak sahiplerine ayırma işlemini, bu işlemle belirlenen payı ve paylaşmaya katılan kişiyi birlikte verir. Dalın işlem ve sonuç ayrımı bu içeriği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir şeyi parçalara veya paylara ayırmak"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"paylara ayırma"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"pay, kişiye düşen bölüm"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bölüştürme, paylaşma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"arazi veya evleri paylaştıran kimse"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"birlikte paylaşan ortak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"öteki araziden ayrılmış arazi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"az suyu eşit paylaştırmaya yarayan taş"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kişilere ayrılmış paylar"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ayırma ve dağıtma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"zaman onları ayırıp dağıttı"}],"lexicalization_note":"Tanım yalın bölme ve pay anlamlarını korurken belirli nesne, kişi ve araç kalıplarını bağımlı özel kullanımlar olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel dağıtma, belirli hisse ve ortaklık dalları işlem, sonuç ve ortak sahiplik sınırlarını en açık biçimde gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirlenmiş pay ve hak sahibi yapısını korurken komşu dalın çekirdeği daha genel ayırma ve dağıtmadır.","focus_only":"Bölme işleminin yanında ayrılmış payı ve paylaşmaya katılan kişiyi de kapsar.","gloss":"bölme ve dağıtma","neighbor_only":"Dağılma ve genel dağıtma yönünü, belirli bir pay sonucu gerektirmeden öne çıkarır.","neighbor_ref":"root_001644/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünü parçalara ayırma ve parçaları dağıtma işlemini bildirir."},{"boundary_match":"partial","distinction":"Odak dal işlem ile sonucu dengeler; komşu dalda belirli parça veya hisse, işlemin kendisinden daha merkezîdir.","focus_only":"Bütünün bölünme işlemini ve bölüştüren ya da birlikte paylaşan kişileri de kapsar.","gloss":"hisse ve pay","neighbor_only":"Bütünden kopan parçayı ve o parçanın birine verilmesini daha doğrudan öne çıkarır.","neighbor_ref":"root_000329/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir bütünden kişiye ayrılan payı ve payların bölüşülmesini kapsar."},{"boundary_match":"field_only","distinction":"Odak dalın çekirdeği ayırma ve pay belirlemedir; komşu dalın çekirdeği ise henüz ayrılmamış ortak sahiplik veya katılımdır.","focus_only":"Ortak veya tekil bir bütünü fiilen paylara ayırır ve her payı belirler.","gloss":"ortaklık ve katılma","neighbor_only":"Bir şeyin birden çok kişi arasında ortak olmasını ve ortakların ilişki kurmasını bildirir.","neighbor_ref":"root_000791/B001","relation_type":"same_field","shared_zone":"Her iki dal pay, ortaklar ve birden çok kişinin aynı mal üzerindeki ilişkisi alanında bulunur."}],"source_phrase_ar":"تجزئة شيء والنصيب قسم (maqayis)؛ القسم مصدر قسم والقسم الحظ من الخير والقسيم الذي يقاسمك أرضا أو مالا (ayn)؛ القسم مصدر قسمت الشئ والقسم الحظ والنصيب والتقسيم التفريق (sihah)؛ قسمت الشيء بينهم قسما وقسمة والقسم الحظ والنصيب (tahdhib)؛ القسم: إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما (mufradat)","source_summary":"Kaynaklar bölme, paylara ayırma ve dağıtma işlemiyle bu işlemden doğan pay üzerinde birleşir; ortaklaşa paylaşan kişi ile miras ve savaş kazancının sahiplerine verilmesi de bu çekirdeğe bağlanır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه قسم الشيء وقسمته، وإفراز النصيب، والحظ والنصيب المقسوم، والقاسم والقسام، والقسيم الذي يقاسمك، وعزل أرض عن أرض، وتفريق الشيء أو الناس، وحصاة القسم في تسوية الماء.","what_is_not_ar":"ليس هو اليمين، ولا جمال الوجه، ولا طي القسامي، ولا حر الهاجرة."},"support_links":["sup_a78427d687a82ce6cde3"]},{"boundary":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B004","candidate_links":[{"candidate_id":"cand_fc0e8bdb54afc874a3cf","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel yemin eylemiyle özel hukuk uygulamasındaki dağıtılmış yeminleri birlikte temsil eder.","boundary_detail":"Buradaki dağıtma, mal paylaştırma anlamı değil; öldürme davasında yeminlerin ilgililere bölüştürülmesidir.","branch_image_ar":"يمين مقسومة على أهلها","concept_gloss":"yemin etme ve öldürme davasında paylaştırılan yeminler","contextual_glosses":[{"applicability":"Genel olarak yemin etme veya verilen güçlü sözün adlandırıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öldürme davasında yeminlerin yakınlara paylaştırılması düzenini göstermez.","preserves":"Sözü yeminle güvenceye bağlama çekirdeğini korur."},"facet_ids":["F001"],"text":"yemin","usage_role":"general"},{"applicability":"Öldürme iddiasına özgü toplu yemin uygulamasının açıklanması gereken bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü yemin için geçerli olan genel eylem anlamını dışarıda bırakır.","preserves":"Yeminlerin öldürülen kişinin yakınları arasında dağıtılması özelliğini korur."},"facet_ids":["F002"],"text":"öldürme davasındaki paylaştırılmış yeminler","usage_role":"explanatory"}],"definition":"Bir sözün doğruluğunu güçlü bir tanıklık çağrısıyla güvenceye bağlayarak yemin etmedir. Özel hukuk kullanımında, öldürme iddiasında yeminlerin öldürülen kişinin yakınları arasında paylaştırılmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir iddia veya söz için yemin etmeyi ve karşılıklı yeminleşmeyi bildirir."},{"facet_id":"F002","role":"specialization","statement":"Öldürme iddiasında yeminlerin öldürülen kişinin yakınlarına bölüştürüldüğü hukuk uygulamasını kapsar."}],"identity_rationale":"Kaynak ifadesi genel olarak yemin etmeyi ve bunun özel bir kökeni sayılan, öldürme davasında maktulün yakınlarına dağıtılan yeminleri birlikte açıklar. Dalın genel yemin ile özel hukuk uygulaması ayrımı bu yapıya uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yemin"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yemin etti"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"ona yemin etti veya onunla antlaştı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Tanrı adına karşılıklı yemin ettiler"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"öldürme davasında yakınlara paylaştırılan yeminler"}],"lexicalization_note":"Tanım yalın yemin anlamıyla belirli yeminleşme ve öldürme davası kalıplarını ayırır; özel uygulamayı her yeminin zorunlu içeriği yapmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel yemin dalı anlam yakınlığını, öldürme bedeli dalı ise özel hukuk alanındaki araç farkını görünür kıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel yemin alanında yakın olsalar da odak dalın belirleyici ek sınırı öldürme davasındaki dağıtılmış yeminlerdir.","focus_only":"Öldürme davasında yakınlara paylaştırılan yeminlerden oluşan özel uygulamayı da kapsar.","gloss":"yemin ve yemin etme","neighbor_only":"Çok yemin etme, birine yemin ettirme ve üzerine yemin edilen şeyi daha geniş biçimde kapsar.","neighbor_ref":"root_000349/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir sözü yemin yoluyla güçlü biçimde doğrulamayı bildirir."},{"boundary_match":"field_only","distinction":"Odak dal kanıtlama veya iddiayı destekleme aracı olarak yeminleri, komşu dal ise ceza yerine ödenen maddi bedeli merkez alır.","focus_only":"Öldürme iddiasını yeminlerin yakınlar arasında paylaştırılması yoluyla ele alır.","gloss":"öldürme bedeli","neighbor_only":"Öldürme karşılığında ödenen bedeli, bu bedeli ödeyen topluluğu ve bedel yoluyla çözümü bildirir.","neighbor_ref":"root_001036/B004","relation_type":"same_field","shared_zone":"İki dal da öldürme olayının hukukî sonuçları ve yakınların hak iddiası alanında yer alır."}],"source_phrase_ar":"اليمين فالقسم وأصل ذلك من القسامة وهي الأيمان تقسم على أولياء المقتول (maqayis)؛ القسم اليمين والفعل أقسم (ayn)؛ أقسمت حلفت وأصله من القسامة (sihah)؛ القسم اليمين وأقسمت إقساما وقسما والقسامة في الدم (tahdhib)؛ وأقسم: حلف وأصله من القسامة ثم صار اسما لكل حلف (mufradat)","source_summary":"Kaynaklar genel yemin anlamında birleşir ve bu anlamı, öldürme davasında yeminlerin yakınlara paylaştırıldığı özel uygulamayla ilişkilendirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القسم بمعنى اليمين، وأقسم وحلف، وقاسمه حلف له، وتقاسموا بالله، والقسامة في الدم بوصفها أيمانا تقسم على أولياء المقتول.","what_is_not_ar":"ليس هو قسمة المال أو النصيب إلا من جهة الأصل الذي ترده المصادر إلى القسامة."},"support_links":["sup_62a26cba386d7e726bcd"]},{"boundary":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_kind":"collocation","branch_ref":"root_001226/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"işaretli ok çekerek karar arama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca işaretli oklarla yapılacak işi veya kişiye ayrılan sonucu belirleme uygulamasını karşılar.","boundary_detail":"Dal yalnızca işaretli oklarla karar veya ayrılmış sonuç arama uygulamasına bağlıdır; genel bölüştürme ya da oyun oku anlamı değildir.","branch_image_ar":"طلب القسم بالأزلام","concept_gloss":"işaretli ok çekerek karar arama","contextual_glosses":[{"applicability":"Bir eyleme girişme ya da ondan vazgeçme kararının ok çekmeyle arandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiye önceden ayrılmış sonucu öğrenme yönünü açıkça karşılamaz.","preserves":"Ok çekme aracını ve yapma ya da bırakma kararını korur."},"facet_ids":["F001"],"text":"işaretli oklarla yapıp yapmamaya karar vermek","usage_role":"explanatory"}],"definition":"Üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılmış sonucu veya bir işi yapıp yapmamayı belirlemeye çalışma uygulamasıdır. Aynı türetimin birinden paylaştırmasını isteme kullanımı, çekirdeğin dışında bir kaynak çeşitlemesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşaretli oklar çekerek ayrılmış sonucu ya da bir işi yapma veya bırakma kararını aramayı bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Aynı türetim ayrıca birinden bir şeyi paylaştırmasını isteme anlamında aktarılır."}],"identity_rationale":"Kaynak ifadesinin ana bölümü, üzerinde yönlendirme işaretleri bulunan okları çekerek kişiye ayrılan sonucu veya yapılacak işi aramayı anlatır. Aynı toplu iddia daha geniş biçimde birinden paylaştırmasını istemeyi de anar; bu ikinci kullanım, oklarla yapılan uygulamanın çekirdeğine genellenemez.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işaretli ok çekerek ayrılmış sonucu veya yapılacak işi belirleme"}],"lexicalization_note":"Tanım açıkça işaretli oklarla kurulan yapıya bağlıdır; aynı türetimin genel olarak paylaştırma isteme kullanımı yalın dal anlamına çevrilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; fiziksel ok ve araç adları anlam sınırını keskinleştirmedi, yalnızca gerçek paylaştırma dalı yararlı bir karşıtlık sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal işaretli oklarla bilgi ya da karar arayan bir uygulamadır; komşu dal ise gerçek bir nesneyi veya hakkı paylaştırma işlemidir.","focus_only":"İşaretli oklar çekerek gelecekte yapılacak işi veya kişiye ayrıldığı düşünülen sonucu arar.","gloss":"paylara ayırma","neighbor_only":"Bir bütünü fiilen parçalara ve hak sahiplerinin paylarına ayırır.","neighbor_ref":"root_001226/B003","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye düşen bölüm veya sonuç düşüncesi çevresinde ilişki kurar."}],"source_phrase_ar":"الاستقسام أنهم كانوا يجيلون السهام أي الأزلام (ayn)؛ واستقسم: طلب القسم بالازلام (sihah)؛ تستقسموا بالأزلام معناه تطلبوا من جهة الأزلام وما كتب عليها ما قسم لكم (tahdhib)؛ واستقسمته: سألته أن يقسم ثم قد يستعمل في معنى قسم (mufradat)","source_summary":"Toplu kaynak anlatımı, işaretli okları çevirip çekerek kişiye ayrılmış sonucu veya yapılacak işi arama uygulamasında birleşir; ayrıca aynı türetimin genel paylaştırma isteme kullanımı bulunduğunu belirtir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاستقسام بالأزلام والقداح، أي طلب ما قسم أو تعيين المضي والترك بضرب السهام.","what_is_not_ar":"ليس هو مطلق القسمة بين الشركاء، ولا اليمين، ولا قداح الميسر حين تفرقها المصادر عن أزلام الأمر والنهي."},"support_links":[]},{"boundary":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001226/B006","candidate_links":[{"candidate_id":"cand_163b5ea0f853d568ac00","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın karar değerlendirmesi ile kaygı kaynaklı zihinsel dağılma kullanımlarını ayrı bölümler halinde korur.","boundary_detail":"Bu dal maddi bir şeyi paylaştırmayı değil, kararın seçeneklere ayrılmasını veya zihnin kaygılarla dağılmasını anlatır.","branch_image_ar":"بال مقسم بين وجوه الأمر","concept_gloss":"işi ölçüp biçme; kaygıyla zihnin dağılması","contextual_glosses":[{"applicability":"Bir kişinin nasıl davranacağını düşünüp seçenekleri değerlendirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaygıların zihni farklı yönlere dağıtması anlamını dışarıda bırakır.","preserves":"Bir işin uygulanışını düşünme ve seçenekleri değerlendirme sürecini korur."},"facet_ids":["F001"],"text":"işi ölçüp biçmek","usage_role":"contextual"},{"applicability":"Kaygıların kişinin düşüncesini birçok yöne çektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir işi planlayarak nasıl yapacağını değerlendirme anlamını karşılamaz.","preserves":"Kaygı nedeniyle düşüncenin bölünüp dağılması sonucunu korur."},"facet_ids":["F002"],"text":"kaygıdan zihni dağılmak","usage_role":"contextual"}],"definition":"Bir işi nasıl yürüteceğini ölçüp biçerek seçenekleri değerlendirmeyi anlatır. Başka bir kullanımda, kaygıların kişinin düşüncesini farklı yönlere çekip dağıtmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işin nasıl yapılacağını ölçüp biçme ve seçenekleri değerlendirme sürecini bildirir."},{"facet_id":"F002","role":"extension","statement":"Kaygıların zihni veya kalbi farklı yönlere çekerek düşünceyi dağıtmasını bildirir."}],"identity_rationale":"Kaynak ifadesi bölme düşüncesini zihinsel alana iki ayrı biçimde taşır: kişi bir işi nasıl yapacağını ölçüp biçer veya kaygılar düşüncesini farklı yönlere dağıtır. Dal, bu iki kullanımı birbirine karıştırmadan ayırdığı sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"işini ölçüp biçiyor ve nasıl yapacağını düşünüyor"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"kaygının dağıttığı zihin"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kaygılar yüzünden düşüncesi dağılmış"}],"lexicalization_note":"Tanım, işi ölçüp biçme yapısıyla kaygılı zihin nitelemelerini ayrı tutar ve bunlardan genel bir yalın bölme anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; görüş karışıklığı ve tek olmayan görüş dalları zihinsel bölünmenin nedenini ve katılımcı yapısını ayırt etmeye yaradı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değerlendirme sürecini de içerebilir ve dağılmayı kaygıya bağlar; komşu dalda belirleyici olan kuşku ve görüş karışıklığıdır.","focus_only":"Ya bilinçli seçenek değerlendirmesini ya da kaygının düşünceyi yönlere ayırmasını bildirir.","gloss":"kararsız ve karışık görüş","neighbor_only":"Kişinin görüşünde kuşkuya düşmesini ve ne yapacağını bilemeyecek ölçüde karışmasını bildirir.","neighbor_ref":"root_000576/B005","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek bir kararlı yönde ilerleyemediği zihinsel durumu kapsar."},{"boundary_match":"partial","distinction":"Odak dal içsel değerlendirme ya da kaygı kaynaklı dağılmadır; komşu dalın ayrılığı ise görüşün ortaklaşa taşınması veya kişinin kendine seslenmesidir.","focus_only":"Tek kişinin zihninin seçenekler veya kaygılar arasında bölünmesini anlatır.","gloss":"ortak veya tek olmayan görüş","neighbor_only":"Bir görüşün birden çok kişi arasında ortak olmasını veya kişinin kendi kendine konuşmasını anlatır.","neighbor_ref":"root_000791/B008","relation_type":"near_neighbor","shared_zone":"İki dal da düşüncenin tek ve yalın bir yön taşımaması noktasında buluşur."}],"source_phrase_ar":"أمسى فلان متقسما أي كأن خواطر الهموم تقسمته (maqayis)؛ هو يقسم أمره قسما أي يقدره وينظر فيه كيف يفعل (sihah)؛ يقسم أمره قسما أي يقدره ينظر كيف يعمل فيه (tahdhib)؛ رجل منقسم القلب أي اقتسمه الهم (mufradat)","source_summary":"Kaynaklar bölünme tasarımını zihinsel alana taşır: bir kullanım işi nasıl yapacağını düşünüp tartmayı, öteki kullanım ise kaygıların zihni bölüp dağıtmasını anlatır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تقسيم الأمر بمعنى تقديره والنظر كيف يفعل، وتوزع القلب أو الخاطر بالهموم.","what_is_not_ar":"ليس هو التقسيم الحسي للمال أو الأرض، ولا الاستقسام بالأزلام."},"support_links":["sup_c7ccb4b0d9457b7d5cbe"]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001226/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"yalıtık adlandırmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"طي القسامي أول الثوب","concept_gloss":"yalıtık adlandırmalar","contextual_glosses":[{"applicability":"Kumaşın ilk kez katlanıp kat izlerinin oluşturulduğu meslek veya iş bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki durum arasında bulunan şey veya hayvan anlamını dışarıda bırakır.","preserves":"Giysiyi ilk kez katlayan kişiyi ve ilk kat oluşturma işini korur."},"facet_ids":["F001"],"text":"giysinin ilk katını yapan kimse","usage_role":"explanatory"},{"applicability":"Bir varlığın iki gelişim durumu arasında kaldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Giysiyi ilk kez katlayan kişi anlamını dışarıda bırakır.","preserves":"Bir varlığın iki ayrı durum arasında bulunması özelliğini korur."},"facet_ids":["F002"],"text":"iki durum arasında bulunan","usage_role":"explanatory"}],"definition":"Kayıt, bir yanda giysileri ilk kez katlayarak kat yerlerini oluşturan kişiyi, öte yanda iki durum arasında bulunan şeyi anlatır. Bu iki anlam tek bir kavram değildir ve ayrı dallar gerektirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Giysileri ilk kez katlayıp kumaşta ilk kat izlerini oluşturan kişiyi bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Bir şeyin iki durum arasında bulunmasını, özellikle bir atın iki gelişim evresi arasında kalmasını bildirir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"giysiyi ilk kez katlayıp kat izlerini oluşturan kimse"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"iki durum arasında bulunan, özellikle iki gelişim evresi arasındaki at"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"القسامى وهو الذي يطوى الثياب أول طيها (maqayis)؛ القسامى الذى يطوى الثياب أول طيها حتى تتكسر على طيه (sihah)؛ القسامي الذي يطوي الثياب أول طيها والقسامي الذي يكون بين شيئين (tahdhib)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه القسامي الذي يطوي الثياب أول طيها، وما ألحق به من كونه بين شيئين في وصف الفرس.","what_is_not_ar":"ليس هو القاسم الذي يقسم المال، ولا القسام بمعنى الحسن أو الحر."},"support_links":[]},{"boundary":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_kind":"bare","branch_ref":"root_001226/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","surface_ar":"قَسَمٌ"}],"gloss":"düşman ile Müslümanlar arasındaki ateşkes","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}}],"root_ar":"ق س م","root_id":"root_001226","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta belirtilen iki taraf arasında çatışmanın durdurulduğu özel ateşkes anlamını karşılar.","boundary_detail":"Bu dal genel barışın bütün türlerini, yüz güzelliğini veya öldürme davasındaki yeminleri kapsamaz.","branch_image_ar":"هدنة قسامة","concept_gloss":"düşman ile Müslümanlar arasındaki ateşkes","contextual_glosses":[{"applicability":"Tarafların metinde zaten açık olduğu ve çatışmaya ara verilmesinin anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":"Kaynakta belirtilen taraflar dışındaki her türlü ateşkese uygulanabilen daha geniş bir kapsam ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Çatışmanın anlaşmayla durdurulması çekirdeğini korur."},"facet_ids":["F001"],"text":"ateşkes","usage_role":"contextual"}],"definition":"Düşman ile Müslümanlar arasında çatışmaya ara veren ateşkestir. Kaynak, tarafları ve savaşın geçici olarak durmasını anlamın sınırı olarak verir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Düşman ile Müslümanlar arasında çatışmayı durduran ateşkesi bildirir."}],"identity_rationale":"Kaynak ifadesi anlamı doğrudan düşman ile Müslümanlar arasındaki çatışmasızlık anlaşması olarak verir. Dalın ateşkes çerçevesi bu tekil aktarımı eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"düşman ile Müslümanlar arasındaki ateşkes"}],"lexicalization_note":"Tanım yalın dalı kaynakta belirtilen taraflar arasındaki ateşkesle sınırlar ve başka barış türlerine kendiliğinden genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı çatışmayı bırakma ve genel barış dalları ateşkesin taraf ve süre bakımından daha dar sınırını gösterdi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli taraflar arasındaki ateşkestir; komşu dal tarafları sınırlamayan ve uzlaşma ile saldırmama sözünü de kapsayan daha geniş bir bırakışmadır.","focus_only":"Tarafları özellikle düşman ile Müslümanlar olarak sınırlar.","gloss":"karşılıklı çatışmayı bırakma","neighbor_only":"Karşılıklı saldırmama, uzlaşma, savaşı bırakma ve savaş açmama sözü gibi daha geniş anlaşma türlerini kapsar.","neighbor_ref":"root_001635/B004","relation_type":"near_synonym","shared_zone":"İki dal da karşıt tarafların çatışmayı bırakması ve bir süre saldırmaması alanında buluşur."},{"boundary_match":"partial","distinction":"Ateşkes geçici ve tarafları belirli bir çatışma düzenlemesidir; komşu dal daha genel ve kalıcı olabilen barış durumunu anlatır.","focus_only":"Belirli taraflar arasında çatışmaya ara veren sınırlı ateşkesi bildirir.","gloss":"barış ve uzlaşma","neighbor_only":"Savaşın karşıtı olarak genel barış, uzlaşma ve barış içinde olma durumunu kapsar.","neighbor_ref":"root_000737/B004","relation_type":"near_synonym","shared_zone":"Her iki dal silahlı çatışmanın durması ve tarafların savaşmaması durumunu içerir."}],"source_phrase_ar":"القسامة: الهدنة بين العدو وبين المسلمين (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Bu anlam yalnızca bir kaynakta, düşman ile Müslümanlar arasındaki ateşkes olarak aktarılır."}],"source_summary":"Tek kaynaklı aktarım, sözü düşman ile Müslümanlar arasındaki ateşkes olarak tanımlar ve başka bir barış ya da yemin anlamı eklemez.","sources":["TA"],"what_is_ar":"يدخل فيه القسامة بمعنى الهدنة بين العدو وبين المسلمين.","what_is_not_ar":"ليس هو القسامة بمعنى الحسن، ولا القسامة في الدم والأيمان."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:5:1"],"branch_refs":[],"candidate_id":"cand_49af8216f076e649f9ce","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:1:delayed-oath-discovery","source_type":"word_analysis","support_ids":["sup_3fd74ef1185b62e1d95a","sup_9ca801b4bd2d29ec6f7b"],"title":"question holds back the oath noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:1","qac_refs":["89:5:1:1"],"status":"accepted"}},{"anchor_refs":["89:5:1"],"branch_refs":[],"candidate_id":"cand_de79c6745c2c04af54b7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:1:full-clause-recognition-test","source_type":"word_analysis","support_ids":["sup_46661344d5b701fcd550","sup_9ca801b4bd2d29ec6f7b"],"title":"whole proposition becomes a recognition test","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:1","qac_refs":["89:5:1:1"],"status":"accepted"}},{"anchor_refs":["89:5:1"],"branch_refs":[],"candidate_id":"cand_5feb2b483546be974590","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:1:hinge-after-oaths","source_type":"word_analysis","support_ids":["sup_1bf187eca9920344ae20","sup_9ca801b4bd2d29ec6f7b"],"title":"oath sequence shifts into evaluation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:1","qac_refs":["89:5:1:1"],"status":"accepted"}},{"anchor_refs":["89:5:1"],"branch_refs":[],"candidate_id":"cand_52b82b2e66f45756a330","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:1:sound-arrest","source_type":"word_analysis","support_ids":["sup_8be7a89f9676bb73ece2","sup_9ca801b4bd2d29ec6f7b"],"title":"brief opening arrests attention","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:1","qac_refs":["89:5:1:1"],"status":"accepted"}},{"anchor_refs":["89:5:2"],"branch_refs":[],"candidate_id":"cand_9dd84ff213a3296ec90e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:2:amid-sense-narrowed","source_type":"word_analysis","support_ids":["sup_71142fa808adebda8297","sup_948f15bb973881a1373a"],"title":"amid-sense limited to the oath sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:2","qac_refs":["89:5:2:1"],"status":"accepted"}},{"anchor_refs":["89:5:2"],"branch_refs":[],"candidate_id":"cand_7fae3658c10dc6572b0d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:2:compact-to-expanded-cadence","source_type":"word_analysis","support_ids":["sup_1312072c12bae41dddbb","sup_948f15bb973881a1373a"],"title":"short preposition opens the demonstrative package","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:2","qac_refs":["89:5:2:1"],"status":"accepted"}},{"anchor_refs":["89:5:2"],"branch_refs":[],"candidate_id":"cand_111cb67206e10f9f3e5a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:2:contained-domain","source_type":"word_analysis","support_ids":["sup_8facf03a4281edfe0d6b","sup_948f15bb973881a1373a"],"title":"prior signs become the search domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:2","qac_refs":["89:5:2:1"],"status":"accepted"}},{"anchor_refs":["89:5:2"],"branch_refs":[],"candidate_id":"cand_512c3233646147e0df9e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:2:fronted-predicate","source_type":"word_analysis","support_ids":["sup_1947a775fca4327c6953","sup_948f15bb973881a1373a"],"title":"fronted phrase delays the subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:2","qac_refs":["89:5:2:1"],"status":"accepted"}},{"anchor_refs":["89:5:2"],"branch_refs":[],"candidate_id":"cand_05bf83313db8bfdbdaf8","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:2:recategorizing-bridge","source_type":"word_analysis","support_ids":["sup_948f15bb973881a1373a","sup_ec1c1ebf996dbbe6c2ac"],"title":"oath chain becomes contained evidence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:2","qac_refs":["89:5:2:1"],"status":"accepted"}},{"anchor_refs":["89:5:3"],"branch_refs":[],"candidate_id":"cand_cd3a460eccd18c32706a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:3:deictic-echo","source_type":"word_analysis","support_ids":["sup_877007db47a0a62e7b4b","sup_d1296227f3928f27859c"],"title":"echo by reference rather than repetition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:3","qac_refs":["89:5:3:1"],"status":"accepted"}},{"anchor_refs":["89:5:3"],"branch_refs":[],"candidate_id":"cand_02309a8606b48363fc66","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:3:distal-reviewable-definiteness","source_type":"word_analysis","support_ids":["sup_c9e1c56c1dbd359db850","sup_d1296227f3928f27859c"],"title":"distal form makes the sequence reviewable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:3","qac_refs":["89:5:3:1"],"status":"accepted"}},{"anchor_refs":["89:5:3"],"branch_refs":[],"candidate_id":"cand_1a64f311fe4139cd4eb6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:3:governed-bridge","source_type":"word_analysis","support_ids":["sup_d1296227f3928f27859c","sup_ec0c3a7afd1a07f9f792"],"title":"governed pointer bridges domain and oath","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:3","qac_refs":["89:5:3:1"],"status":"accepted"}},{"anchor_refs":["89:5:3"],"branch_refs":[],"candidate_id":"cand_a9a33e52137909969e57","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:3:hard-close-pointer","source_type":"word_analysis","support_ids":["sup_d1296227f3928f27859c","sup_e1e0a693703f1df8d84d"],"title":"pointer closes as a package","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:3","qac_refs":["89:5:3:1"],"status":"accepted"}},{"anchor_refs":["89:5:3"],"branch_refs":[],"candidate_id":"cand_ee4fa40c3a71965d473b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:3:prior-oaths-packaged","source_type":"word_analysis","support_ids":["sup_17a5a4e07cd1c7961a79","sup_d1296227f3928f27859c"],"title":"several oath items become one object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:3","qac_refs":["89:5:3:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_a0ecef1834b0f0ebd9e6","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:delayed-indefinite-subject","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_e1cdfe7efb02dda7fe19"],"title":"delayed subject names possible oath-value","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_0be4dc0f37e8e31d5701","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:division-pressure-narrowed","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_bbbab68d6006ac9179e9"],"title":"division field sharpens oath as sorting boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_9c83c5d4753dd0ef1821","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:great-oath-echo","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_c313e2dbd5af2c67c074"],"title":"asserted great oath becomes a question","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_cd996d265a427a821bf9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:marked-reflective-use","source_type":"word_analysis","support_ids":["sup_2b1d1e44af5b40407869","sup_2fc7d4e2829085e34de5"],"title":"nominal label reflects on the sequence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_117c414d27bc21689948","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:oath-noun-not-new-oath-item","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_d3a886c7451456f012a3"],"title":"oath becomes evaluated status","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_599bd57be90a084a753b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:receiver-qualified-oath","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_c50c9f563b22af0abc50"],"title":"oath-force is qualified by its receiver","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_d902377076156c40b2bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:sound-binds-oath-to-receiver","source_type":"word_analysis","support_ids":["sup_2fc7d4e2829085e34de5","sup_a9f8ff8c2aacf0a89b52"],"title":"liaison audibly joins noun and receiver","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:4","qac_refs":["89:5:4:1"],"status":"accepted"}},{"anchor_refs":["89:5:5"],"branch_refs":[],"candidate_id":"cand_080597dfbd6953e6279d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:5:preposition-not-root","source_type":"word_analysis","support_ids":["sup_640115427acb9a83877d","sup_de4aaea0d20636c2d4b5"],"title":"segmentation keeps the mechanism prepositional","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:5","qac_refs":["89:5:5:1"],"status":"accepted"}},{"anchor_refs":["89:5:5"],"branch_refs":[],"candidate_id":"cand_cb67520bc09c2b8d2463","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:5:recipient-suitability-range","source_type":"word_analysis","support_ids":["sup_640115427acb9a83877d","sup_b8bb653b4cd967d85ec5"],"title":"recipient and suitability senses converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:5","qac_refs":["89:5:5:1"],"status":"accepted"}},{"anchor_refs":["89:5:5"],"branch_refs":[],"candidate_id":"cand_d8cbd2f2bd14cc538ba4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:5:sound-transition","source_type":"word_analysis","support_ids":["sup_640115427acb9a83877d","sup_97fdfd134f3f9f3f0c19"],"title":"sound tightens the move into the receiver phrase","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:5","qac_refs":["89:5:5:1"],"status":"accepted"}},{"anchor_refs":["89:5:5"],"branch_refs":[],"candidate_id":"cand_5ef74705fdf24d426449","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:5:specialized-receiver","source_type":"word_analysis","support_ids":["sup_640115427acb9a83877d","sup_c4257568a0d9929fe842"],"title":"oath is specialized to a restrained receiver","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:5","qac_refs":["89:5:5:1"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_64797a635d71b04be8a9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:construct-possessor-class","source_type":"word_analysis","support_ids":["sup_5919f531d12fdbafca97","sup_afc0b5943c63cf63b654"],"title":"construct possessor creates a receiver class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_1381e6de45cf4237ebbd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:generic-individual-accountability","source_type":"word_analysis","support_ids":["sup_27d86f076dc811d7d73d","sup_5919f531d12fdbafca97"],"title":"generic class remains individually addressed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_500086de13c8b2137048","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:oath-linked-possession","source_type":"word_analysis","support_ids":["sup_5919f531d12fdbafca97","sup_818d95038ac37d20db44"],"title":"oath recognition depends on possessive qualification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_631ea58216483881ee68","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:possession-pattern-echoes","source_type":"word_analysis","support_ids":["sup_5919f531d12fdbafca97","sup_72e693784137f385e96d"],"title":"possession language joins local and wider sign-reading patterns","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_93e26486b7c3b5587894","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:property-bearing-family-narrowed","source_type":"word_analysis","support_ids":["sup_513fc0445bba8f53b65c","sup_5919f531d12fdbafca97"],"title":"family range supports property-bearing identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_9578ba2e1caaa1ba4e6c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:relational-not-adjectival","source_type":"word_analysis","support_ids":["sup_0c410f8aa97bddac8625","sup_5919f531d12fdbafca97"],"title":"restraint is held as a defining capacity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_6fa4d3fe70054d63fa44","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:soft-length-before-closure","source_type":"word_analysis","support_ids":["sup_0852cf827c5c61885af0","sup_5919f531d12fdbafca97"],"title":"receiver phrase stretches before final closure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_8e57c657f875b377b13d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:5:6:visible-five-noun-form","source_type":"word_analysis","support_ids":["sup_5919f531d12fdbafca97","sup_771fb6be9ec622499adf"],"title":"genitive morphology carries possession","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:6","qac_refs":["89:5:5:2"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_47f2e989a56d90d4b0e5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:boundary-intellect-narrowed","source_type":"word_analysis","support_ids":["sup_79caa413f2bc023c5db8","sup_ce2eea9126fb3c53bd1b"],"title":"stone and enclosure pressure becomes disciplined cognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_c0aeab0914e3fbe8512e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:constricted-closure-sound","source_type":"word_analysis","support_ids":["sup_ce2eea9126fb3c53bd1b","sup_fce9cd8336f8788ab381"],"title":"compressed sound fits boundary meaning","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_1be1519e6c53ad069ef2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:final-question-landing","source_type":"word_analysis","support_ids":["sup_ce2eea9126fb3c53bd1b","sup_ed0664ed6cadb2390422"],"title":"the question lands on restrained reason","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_f39ad3128a3d597a3d4a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:form-and-rarity","source_type":"word_analysis","support_ids":["sup_ce2eea9126fb3c53bd1b","sup_d63dbcccccc40a7a232b"],"title":"rare abstract form makes restraint marked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_d753a503a2eee4aafe03","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:forward-seeing-bridge","source_type":"word_analysis","support_ids":["sup_c7d28ace786e0a8ec58a","sup_ce2eea9126fb3c53bd1b"],"title":"restraint prepares the next seeing test","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_26323b2d172dc0f894cb","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:passive-and-self-boundary-pressure","source_type":"word_analysis","support_ids":["sup_ce2eea9126fb3c53bd1b","sup_ef77e3bac4c0f8d8fa86"],"title":"barredness becomes mental filtering","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_638556e52908285d63b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:possessed-qualitative-restraint","source_type":"word_analysis","support_ids":["sup_534d4e929ff622adb570","sup_ce2eea9126fb3c53bd1b"],"title":"restraint defines the receiver","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_5bda02623c250dae585c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:possessive-restraint-formula","source_type":"word_analysis","support_ids":["sup_45c3ee6811bc5787ed76","sup_ce2eea9126fb3c53bd1b"],"title":"compact formula names intellect through restraint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:7"],"branch_refs":[],"candidate_id":"cand_4b4eb576c0be5ad489fa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:7:prohibition-echoes-internalized","source_type":"word_analysis","support_ids":["sup_88b30fb669eaf964c0cd","sup_ce2eea9126fb3c53bd1b"],"title":"external prohibition becomes internal restraint","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:5:7","qac_refs":["89:5:6:1"],"status":"accepted"}},{"anchor_refs":["89:5:4"],"branch_refs":[],"candidate_id":"cand_4235c970a75c84a8c492","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001226"],"scope":"focus_ayah","source_local_id":"89:5:4:1","source_type":"qac_morpheme","support_ids":["sup_b78344c68744204f420f"],"title":"QAC root occurrence: ق س م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:5:6"],"branch_refs":[],"candidate_id":"cand_5e82109814f13d3a52de","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000296"],"scope":"focus_ayah","source_local_id":"89:5:6:1","source_type":"qac_morpheme","support_ids":["sup_59a2a59383e16279df88"],"title":"QAC root occurrence: ح ج ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:5","branch_refs":["root_000296/B002","root_001226/B004"],"candidate_id":"cand_fc0e8bdb54afc874a3cf","commentary_obligation":"review","hft_ref":"hft_3cad5c05d04326179f05","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_oath_for_restraining_reason","source_type":"hft","support_ids":["sup_62a26cba386d7e726bcd"],"title":"baseline_oath_for_restraining_reason","trust":"legacy_unbound"},{"anchor_refs":["89:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:5","branch_refs":["root_000296/B001","root_000296/B006","root_001226/B003"],"candidate_id":"cand_c611bb7effb19043c8a8","commentary_obligation":"review","hft_ref":"hft_4a0c704d8e2957294bf1","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_apportioned_boundary","source_type":"hft","support_ids":["sup_a78427d687a82ce6cde3"],"title":"baseline_apportioned_boundary","trust":"legacy_unbound"},{"anchor_refs":["89:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:5","branch_refs":["root_000296/B002","root_001226/B006"],"candidate_id":"cand_163b5ea0f853d568ac00","commentary_obligation":"review","hft_ref":"hft_df844b209b2e17f45459","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_divided_deliberation","source_type":"hft","support_ids":["sup_c7ccb4b0d9457b7d5cbe"],"title":"baseline_divided_deliberation","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","qac_morphemes":[{"lemma_ar":"هَل","morph_features":"STEM|POS:INTG|LEM:hal","morpheme_role":"STEM","pos":"INTG","qac_ref":"89:5:1:1","qac_word_ref":"89:5:1","root_ar":"","surface_ar":"هَلْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:5:2:1","qac_word_ref":"89:5:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"89:5:3:1","qac_word_ref":"89:5:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","root_ar":"ق س م","surface_ar":"قَسَمٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:5:5:1","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:5:2","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","root_ar":"ح ج ر","surface_ar":"حِجْرٍ"}],"word_analysis_qac_refs":[["89:5:1:1"],["89:5:2:1"],["89:5:3:1"],["89:5:4:1"],["89:5:5:1"],["89:5:5:2"],["89:5:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:5:1","89:5:2","89:5:3","89:5:4","89:5:5","89:5:6","89:5:7"]},"focus_surface_evidence":{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","qac_morphemes":[{"lemma_ar":"هَل","morph_features":"STEM|POS:INTG|LEM:hal","morpheme_role":"STEM","pos":"INTG","qac_ref":"89:5:1:1","qac_word_ref":"89:5:1","root_ar":"","surface_ar":"هَلْ"},{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"89:5:2:1","qac_word_ref":"89:5:2","root_ar":"","surface_ar":"فِى"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"89:5:3:1","qac_word_ref":"89:5:3","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"قَسَم","morph_features":"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:4:1","qac_word_ref":"89:5:4","root_ar":"ق س م","surface_ar":"قَسَمٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"89:5:5:1","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"ذُو","morph_features":"STEM|POS:N|LEM:*uw|MS|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:5:2","qac_word_ref":"89:5:5","root_ar":"","surface_ar":"ذِى"},{"lemma_ar":"حِجْر","morph_features":"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"89:5:6:1","qac_word_ref":"89:5:6","root_ar":"ح ج ر","surface_ar":"حِجْرٍ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:5:1:1"],["89:5:2:1"],["89:5:3:1"],["89:5:4:1"],["89:5:5:1"],["89:5:5:2"],["89:5:6:1"]],"word_analysis_refs":["89:5:1","89:5:2","89:5:3","89:5:4","89:5:5","89:5:6","89:5:7"],"word_rows":[{"analysis_record_ref":"89:5:1","analytic_gloss_range_en":"yes-no interrogative particle whose local force is rhetorical recognition of the whole oath proposition","analytic_root_gloss_range_en":null,"qac_refs":["89:5:1:1"],"root":{"note":"—"},"surface":{"arabic":"هَلْ","transliteration":"hal"}},{"analysis_record_ref":"89:5:2","analytic_gloss_range_en":"preposition of containment and conceptual domain, fronting the prior oath sequence as the place where oath-force is tested","analytic_root_gloss_range_en":null,"qac_refs":["89:5:2:1"],"root":{"note":"—"},"surface":{"arabic":"فِى","transliteration":"fī"}},{"analysis_record_ref":"89:5:3","analytic_gloss_range_en":"distal demonstrative that packages the preceding oath sequence as one definite, reviewable discourse object","analytic_root_gloss_range_en":null,"qac_refs":["89:5:3:1"],"root":{"note":"—"},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"89:5:4","analytic_gloss_range_en":"indefinite oath-value or binding attestation discovered inside the prior sequence and directed toward a qualified receiver","analytic_root_gloss_range_en":"root range includes oath-taking, apportioning, division, shares, and other peripheral branches; local grammar selects oath while division/allotment remains image-pressure","qac_refs":["89:5:4:1"],"root":{"arabic":"ق س م","transliteration":"q-s-m"},"surface":{"arabic":"قَسَمٌۭ","transliteration":"qasamun"}},{"analysis_record_ref":"89:5:5","analytic_gloss_range_en":"prefixed preposition of specialization, suitability, and audience, making the oath operative for the possessor of restraint","analytic_root_gloss_range_en":null,"qac_refs":["89:5:5:1"],"root":{"note":"—"},"surface":{"arabic":"لِّ","transliteration":"li"}},{"analysis_record_ref":"89:5:6","analytic_gloss_range_en":"genitive five-noun construct head meaning possessor or bearer, forming a generic receiver class defined by restraint","analytic_root_gloss_range_en":"root range centers on possessor, bearer, or one characterized by a construct complement, with other demonstrative or relative-pronoun branches not active locally","qac_refs":["89:5:5:2"],"root":{"arabic":"ذ و و","transliteration":"dh-w-w"},"surface":{"arabic":"ذِى","transliteration":"dhī"}},{"analysis_record_ref":"89:5:7","analytic_gloss_range_en":"possessed restraint or disciplined intellect, qualitative rather than titular, functioning as the faculty that can recognize the oath","analytic_root_gloss_range_en":"root range includes restraint, prohibition, enclosure, hard stone, protected places, and reason as restraining faculty; local construct selects cognitive restraint while boundary and enclosure pressure remains active","qac_refs":["89:5:6:1"],"root":{"arabic":"ح ج ر","transliteration":"ḥ-j-r"},"surface":{"arabic":"حِجْرٍ","transliteration":"ḥijr"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":7,"words_total":7,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["89:5"],"branch_refs":["root_000296/B002","root_001226/B004"],"candidate_id":"cand_fc0e8bdb54afc874a3cf","evidence_scope":"focus_ayah","hft_ref":"hft_3cad5c05d04326179f05","item_id":"baseline_oath_for_restraining_reason","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_oath_for_restraining_reason","support_id":"sup_62a26cba386d7e726bcd"},{"anchor_refs":["89:5"],"branch_refs":["root_000296/B001","root_000296/B006","root_001226/B003"],"candidate_id":"cand_c611bb7effb19043c8a8","evidence_scope":"focus_ayah","hft_ref":"hft_4a0c704d8e2957294bf1","item_id":"baseline_apportioned_boundary","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_apportioned_boundary","support_id":"sup_a78427d687a82ce6cde3"},{"anchor_refs":["89:5"],"branch_refs":["root_000296/B002","root_001226/B006"],"candidate_id":"cand_163b5ea0f853d568ac00","evidence_scope":"focus_ayah","hft_ref":"hft_df844b209b2e17f45459","item_id":"baseline_divided_deliberation","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_divided_deliberation","support_id":"sup_c7ccb4b0d9457b7d5cbe"}],"diagnostics":[],"lane_counts":{"global":15,"macro":2,"micro":3},"packet_summary":{"ayah_count":30,"focus_ref":"89:5","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:5","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"89:5","lane":"micro","linguistic_source_ref":"89:5","surface_ref":"89:5","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:5","target_tokens":[["Bunlarda",["89:5:2","89:5:3"]],["akıl",["89:5:6"]],["sahibi",["89:5:5","89:5:6"]],["için",["89:5:5"]],["bir",["89:5:4"]],["yemin",["89:5:4"]],["yok",["89:5:1"]],["mu",["89:5:1"]]],"text":"Bunlarda akıl sahibi için bir yemin yok mu?"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":14,"id":"s089-p01-001-014","label":"Oaths and the downfall of tyrants","number":1,"refs":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:soft-length-before-closure","source_type":"word_analysis","support_id":"sup_0852cf827c5c61885af0","text":"{\"blocking_evidence\":null,\"headline\":\"receiver phrase stretches before final closure\",\"reader_payoff\":\"The reader hears the receiver phrase carry forward before the final restraint word closes it.\",\"reason\":\"The sound row matches the genitive form's long vowel and the following compact final noun.\",\"representative_source_ids\":[\"QP-a1c28e73\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:relational-not-adjectival","source_type":"word_analysis","support_id":"sup_0c410f8aa97bddac8625","text":"{\"blocking_evidence\":null,\"headline\":\"restraint is held as a defining capacity\",\"reader_payoff\":\"The reader sees intellect framed as an endowed capacity that structures the receiver, not as a flat adjective.\",\"reason\":\"The construct complement is a quality, so the possessor branch is locally realized as bearerhood or endowment rather than external ownership.\",\"representative_source_ids\":[\"QS-28aeb37e\",\"QS-abbfba2a\",\"MS-6b3ab3e6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2:compact-to-expanded-cadence","source_type":"word_analysis","support_id":"sup_1312072c12bae41dddbb","text":"{\"blocking_evidence\":null,\"headline\":\"short preposition opens the demonstrative package\",\"reader_payoff\":\"The reader hears a compact preposition open into a larger deictic package, matching the move from small operator to gathered sequence.\",\"reason\":\"The sound note reinforces the local construction without adding a separate lexical claim.\",\"representative_source_ids\":[\"QP-36ab5268\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3:prior-oaths-packaged","source_type":"word_analysis","support_id":"sup_17a5a4e07cd1c7961a79","text":"{\"blocking_evidence\":null,\"headline\":\"several oath items become one object\",\"reader_payoff\":\"The reader notices that the demonstrative forces one judgment over the whole preceding oath sequence.\",\"reason\":\"Attachment evidence identifies the demonstrative as referring back to the preceding oath discourse as a unit.\",\"representative_source_ids\":[\"QG-25667348\",\"MT-b4345fae\",\"QB-71833c80\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2:fronted-predicate","source_type":"word_analysis","support_id":"sup_1947a775fca4327c6953","text":"{\"blocking_evidence\":null,\"headline\":\"fronted phrase delays the subject\",\"reader_payoff\":\"The reader feels the clause enter the prior sign-complex before naming the oath-value found there.\",\"reason\":\"Attachment evidence identifies the fronted prepositional phrase as the predicate and the oath noun as the delayed subject.\",\"representative_source_ids\":[\"QG-7dc74330\",\"QT-f3c56005\",\"QT-39cca533\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:1:hinge-after-oaths","source_type":"word_analysis","support_id":"sup_1bf187eca9920344ae20","text":"{\"blocking_evidence\":null,\"headline\":\"oath sequence shifts into evaluation\",\"reader_payoff\":\"The reader sees 89:5 as a hinge from sworn presentation to judged sufficiency.\",\"reason\":\"The demonstrative reference gathers the preceding oath material, and the new interrogative frame evaluates it rather than adding another oath item.\",\"representative_source_ids\":[\"QT-9a7e354b\",\"QB-4f63cbdd\",\"QB-f2c88441\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:generic-individual-accountability","source_type":"word_analysis","support_id":"sup_27d86f076dc811d7d73d","text":"{\"blocking_evidence\":null,\"headline\":\"generic class remains individually addressed\",\"reader_payoff\":\"The reader notices a generic receiver class that still presses each possessor of restraint individually.\",\"reason\":\"The singular construct head and indefinite complement form a generic class rather than a named group, while the singular form keeps individual accountability visible.\",\"representative_source_ids\":[\"QG-a39fec28\",\"QF-587c5417\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:marked-reflective-use","source_type":"word_analysis","support_id":"sup_2b1d1e44af5b40407869","text":"{\"blocking_evidence\":null,\"headline\":\"nominal label reflects on the sequence\",\"reader_payoff\":\"The reader sees the noun as a reflective label for the previous sequence, not a routine oath verb.\",\"reason\":\"The contextual profile marks this noun form as low occurrence, and the local clause evaluates an already-heard sequence.\",\"representative_source_ids\":[\"QI-d7630792\",\"MT-f87a98fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4","source_type":"word_analysis","support_id":"sup_2fc7d4e2829085e34de5","text":"{\"gloss_range\":\"indefinite oath-value or binding attestation discovered inside the prior sequence and directed toward a qualified receiver\",\"prose\":\"{{ar:قَسَمٌۭ}} ({{tr:qasamun}}) names the oath-force only after the ayah has made the previous signs its search domain. Its indefinite nominative form makes the question ask whether any binding oath-value is present there, not whether another sworn object has been added. As a nominal label, it reflects on the already-heard oath chain instead of reporting a new act of swearing. The root's oath sense is the selected local reading, while its apportioning and division field gives the oath a sorting edge: recognition is divided between the possessor of restraint and the one who lets the signs pass. The contrast with an asserted great oath elsewhere (56:76) sharpens the local question: here oath-force must be recognized. The following {{ar:لِّذِى حِجْرٍ}} ({{tr:li-dhī ḥijr}}) then shows that this oath-force is not complete as a bare abstraction; it is effective for a qualified receiver, and the liaison in recitation audibly makes the oath noun lean into that receiver phrase.\",\"root_display\":\"{{ar:ق س م}} ({{tr:q-s-m}})\",\"root_gloss_range\":\"root range includes oath-taking, apportioning, division, shares, and other peripheral branches; local grammar selects oath while division/allotment remains image-pressure\",\"surface_display\":\"{{ar:قَسَمٌۭ}} ({{tr:qasamun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:1:delayed-oath-discovery","source_type":"word_analysis","support_id":"sup_3fd74ef1185b62e1d95a","text":"{\"blocking_evidence\":null,\"headline\":\"question holds back the oath noun\",\"reader_payoff\":\"The reader feels the delayed arrival of the oath noun as part of the recognition test.\",\"reason\":\"The fronted predicate precedes the delayed subject, so the question is already active before the noun naming oath-force appears.\",\"representative_source_ids\":[\"QT-d2346532\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:possessive-restraint-formula","source_type":"word_analysis","support_id":"sup_45c3ee6811bc5787ed76","text":"{\"blocking_evidence\":null,\"headline\":\"compact formula names intellect through restraint\",\"reader_payoff\":\"The reader notices that intellect is named through possessed restraint rather than through knowledge alone.\",\"reason\":\"The construct formula joins the possessor head and restraint noun into a compact expression for disciplined intellect.\",\"representative_source_ids\":[\"QH-d6a17be4\",\"MH-7563ecaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:1:full-clause-recognition-test","source_type":"word_analysis","support_id":"sup_46661344d5b701fcd550","text":"{\"blocking_evidence\":null,\"headline\":\"whole proposition becomes a recognition test\",\"reader_payoff\":\"The reader notices that the particle tests recognition of the whole oath proposition, not merely missing information.\",\"reason\":\"QAC and attachment evidence identify a yes-no question over the nominal clause, while the context after the oath sequence supports rhetorical confirmation.\",\"representative_source_ids\":[\"QG-8d518af8\",\"QS-426792df\",\"QI-2b4d49ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:property-bearing-family-narrowed","source_type":"word_analysis","support_id":"sup_513fc0445bba8f53b65c","text":"{\"blocking_evidence\":null,\"headline\":\"family range supports property-bearing identity\",\"reader_payoff\":\"The reader senses the receiver as defined by a stable carried capacity, while local grammar keeps the construct possessor sense selected.\",\"reason\":\"The broader family supports property-bearing pressure, but unrelated demonstrative or relative branches are not locally activated.\",\"representative_source_ids\":[\"QS-b03ee5b4\",\"QS-f19d117a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:possessed-qualitative-restraint","source_type":"word_analysis","support_id":"sup_534d4e929ff622adb570","text":"{\"blocking_evidence\":null,\"headline\":\"restraint defines the receiver\",\"reader_payoff\":\"The reader notices restraint as the possessed quality that defines the oath's receiver, not as a detached abstract noun.\",\"reason\":\"QAC and attachment evidence mark the word as the indefinite genitive complement of the construct possessor head.\",\"representative_source_ids\":[\"QG-1c6ce70e\",\"QG-69b801a9\",\"MG-b5853102\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6","source_type":"word_analysis","support_id":"sup_5919f531d12fdbafca97","text":"{\"gloss_range\":\"genitive five-noun construct head meaning possessor or bearer, forming a generic receiver class defined by restraint\",\"prose\":\"{{ar:ذِى}} ({{tr:dhī}}) turns the final quality into a person-class: one who possesses {{ar:حِجْرٍ}} ({{tr:ḥijr}}). It is genitive after {{ar:لِّ}} ({{tr:li}}) and governs the next noun in construct, so the receiver is not merely described near restraint but grammatically constituted as its bearer. The five-noun form makes possession visible, while the indefinite complement keeps the class generic and individually accountable. Wider family evidence supports property-bearing identity, but the local branch is the construct possessor branch, not demonstrative or relative-pronoun uses elsewhere. This makes the phrase the first local member of a possession pattern that later defines other bearers by different attributes (89:7; 89:10), while sign-reading intellect is also framed through possession language (3:190). In sound, the receiver phrase carries forward before the final restraint word closes it.\",\"root_display\":\"{{ar:ذ و و}} ({{tr:dh-w-w}})\",\"root_gloss_range\":\"root range centers on possessor, bearer, or one characterized by a construct complement, with other demonstrative or relative-pronoun branches not active locally\",\"surface_display\":\"{{ar:ذِى}} ({{tr:dhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:5:6:1","source_type":"qac_morpheme","support_id":"sup_59a2a59383e16279df88","text":"{\"lemma_ar\":\"حِجْر\",\"morph_features\":\"STEM|POS:N|LEM:Hijor|ROOT:Hjr|M|INDEF|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:5:6:1\",\"qac_word_ref\":\"89:5:6\",\"root_ar\":\"ح ج ر\",\"surface_ar\":\"حِجْرٍ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:5","source_type":"word_analysis","support_id":"sup_640115427acb9a83877d","text":"{\"gloss_range\":\"prefixed preposition of specialization, suitability, and audience, making the oath operative for the possessor of restraint\",\"prose\":\"{{ar:لِّ}} ({{tr:li}}) is the small pivot from oath-value to receiver. It governs {{ar:ذِى}} ({{tr:dhī}}) and attaches the final phrase to {{ar:قَسَمٌۭ}} ({{tr:qasamun}}), so the oath is not merely present but specialized for the one who possesses restraint. Its recipient, suitability, and entitlement range overlaps locally: the signs are oath for disciplined reason because that receiver is the one for whom the evidence becomes legible. The doubled transition and nasal liaison from the preceding noun make the move into the receiver phrase feel tightened in recitation. The segmentation also matters; this is a preposition with no root, not lexical material fused into the following possessor word.\",\"root_display\":\"—\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لِّ}} ({{tr:li}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2:amid-sense-narrowed","source_type":"word_analysis","support_id":"sup_71142fa808adebda8297","text":"{\"blocking_evidence\":null,\"headline\":\"amid-sense limited to the oath sequence\",\"reader_payoff\":\"The reader notices the oath-value as found amid a completed sequence, while local grammar keeps the preposition tied to its governed demonstrative.\",\"reason\":\"The broader circumstantial range is useful only as conceptual pressure; the local construction remains a prepositional phrase governing the demonstrative.\",\"representative_source_ids\":[\"QS-6c522a21\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:possession-pattern-echoes","source_type":"word_analysis","support_id":"sup_72e693784137f385e96d","text":"{\"blocking_evidence\":null,\"headline\":\"possession language joins local and wider sign-reading patterns\",\"reader_payoff\":\"The reader sees this restrained possessor as part of a possession-pattern: later local bearers are defined by other attributes (89:7; 89:10), and sign-reading intellect is also marked by possession language (3:190).\",\"reason\":\"The source rows give concrete same-surah references (89:7; 89:10) and a sign-reading parallel (3:190); these remain parallels, not controls over the local parse.\",\"representative_source_ids\":[\"QI-a77a825c\",\"QE-2738f8ec\",\"QE-a81d512c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:visible-five-noun-form","source_type":"word_analysis","support_id":"sup_771fb6be9ec622499adf","text":"{\"blocking_evidence\":null,\"headline\":\"genitive morphology carries possession\",\"reader_payoff\":\"The reader sees the receiver's possessed capacity marked in the visible case form, not only inferred from translation.\",\"reason\":\"QAC marks the word as a genitive masculine singular five-noun form governed by the preceding preposition.\",\"representative_source_ids\":[\"QG-46df0bbf\",\"QF-e07665b5\",\"MF-ae055a83\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:boundary-intellect-narrowed","source_type":"word_analysis","support_id":"sup_79caa413f2bc023c5db8","text":"{\"blocking_evidence\":null,\"headline\":\"stone and enclosure pressure becomes disciplined cognition\",\"reader_payoff\":\"The reader feels intellect as a hard boundary against misreading, while local grammar selects cognitive restraint rather than literal stone.\",\"reason\":\"V4 separates stone, enclosure, prohibition, and restraint-of-reason branches; the construct with a human possessor selects cognitive restraint while retaining boundary imagery.\",\"representative_source_ids\":[\"QS-03c17874\",\"QS-1653fe2e\",\"QS-db6a48c2\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:oath-linked-possession","source_type":"word_analysis","support_id":"sup_818d95038ac37d20db44","text":"{\"blocking_evidence\":null,\"headline\":\"oath recognition depends on possessive qualification\",\"reader_payoff\":\"The reader notices that the oath's audience is grammatically selected by possession of restraint.\",\"reason\":\"The local phrase links the oath noun, specialization preposition, possessor head, and restraint complement into one receiver mechanism.\",\"representative_source_ids\":[\"QI-5ed5742a\",\"QY-b4894460\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3:deictic-echo","source_type":"word_analysis","support_id":"sup_877007db47a0a62e7b4b","text":"{\"blocking_evidence\":null,\"headline\":\"echo by reference rather than repetition\",\"reader_payoff\":\"The reader hears the earlier signs return economically as a pronoun-shaped package rather than as repeated images.\",\"reason\":\"The antecedent is the preceding oath sequence, so the echo is referential rather than lexical repetition.\",\"representative_source_ids\":[\"QE-3887deaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:prohibition-echoes-internalized","source_type":"word_analysis","support_id":"sup_88b30fb669eaf964c0cd","text":"{\"blocking_evidence\":null,\"headline\":\"external prohibition becomes internal restraint\",\"reader_payoff\":\"The reader notices that root echoes of forbidden goods and barred access are redirected into disciplined perception (6:138; 25:22; 25:53).\",\"reason\":\"The source rows give concrete references where the root marks prohibition or barred access (6:138; 25:22; 25:53), while the local construct internalizes that boundary as cognition.\",\"representative_source_ids\":[\"QI-12ba2fca\",\"QI-fde4f32c\",\"MI-dad507dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:1:sound-arrest","source_type":"word_analysis","support_id":"sup_8be7a89f9676bb73ece2","text":"{\"blocking_evidence\":null,\"headline\":\"brief opening arrests attention\",\"reader_payoff\":\"The reader hears the short opening as an arrest before the prior signs are gathered for judgment.\",\"reason\":\"The sound observation coheres with the particle's local interrogative stop and does not add an unsupported semantic branch.\",\"representative_source_ids\":[\"QP-51817f28\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2:contained-domain","source_type":"word_analysis","support_id":"sup_8facf03a4281edfe0d6b","text":"{\"blocking_evidence\":null,\"headline\":\"prior signs become the search domain\",\"reader_payoff\":\"The reader notices that the oath is discovered within the prior sequence rather than imposed beside it.\",\"reason\":\"The preposition governs the demonstrative that points back to the preceding oath discourse, making that discourse the domain of the question.\",\"representative_source_ids\":[\"QG-7531b720\",\"QS-52681050\",\"MS-8ffa4b68\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2","source_type":"word_analysis","support_id":"sup_948f15bb973881a1373a","text":"{\"gloss_range\":\"preposition of containment and conceptual domain, fronting the prior oath sequence as the place where oath-force is tested\",\"prose\":\"{{ar:فِى}} ({{tr:fī}}) makes the previous oath sequence the domain in which {{ar:قَسَمٌۭ}} ({{tr:qasamun}}) is sought. The preposition governs {{ar:ذَٰلِكَ}} ({{tr:dhālika}}), but its placement also matters: the phrase stands first as the predicate, so containment is felt before the oath noun is named. The local force is conceptual containment, with an amid-sense narrowed to this completed sequence of signs. The ayah therefore asks whether oath-value is housed within the already-heard material, not whether a new proof is being added from outside. Its compact sound opening into the longer demonstrative mirrors the move from a small operator into a gathered evidentiary package.\",\"root_display\":\"—\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِى}} ({{tr:fī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:5:sound-transition","source_type":"word_analysis","support_id":"sup_97fdfd134f3f9f3f0c19","text":"{\"blocking_evidence\":null,\"headline\":\"sound tightens the move into the receiver phrase\",\"reader_payoff\":\"The reader hears the transition from oath noun to receiver phrase as tightened rather than casual.\",\"reason\":\"The sound rows align with the doubled preposition and the liaison from the preceding nunation into the receiver phrase.\",\"representative_source_ids\":[\"QP-d90d1c17\",\"QP-ee462f35\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:1","source_type":"word_analysis","support_id":"sup_9ca801b4bd2d29ec6f7b","text":"{\"gloss_range\":\"yes-no interrogative particle whose local force is rhetorical recognition of the whole oath proposition\",\"prose\":\"{{ar:هَلْ}} ({{tr:hal}}) opens the ayah by turning the preceding oath sequence into a question of recognition. It scopes the whole nominal proposition, so the issue is not an action the hearer performs but whether oath-force is present in what has just been presented. Its yes-no syntax remains real, while the discourse setting makes that yes-no form press toward confirmation. Because the question begins before {{ar:قَسَمٌۭ}} ({{tr:qasamun}}) appears, the listener is held inside the inquiry and only then meets the delayed oath noun as the thing to be recognized. The clipped opening also gives a brief arrest before the prior signs are gathered for judgment.\",\"root_display\":\"—\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هَلْ}} ({{tr:hal}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:sound-binds-oath-to-receiver","source_type":"word_analysis","support_id":"sup_a9f8ff8c2aacf0a89b52","text":"{\"blocking_evidence\":null,\"headline\":\"liaison audibly joins noun and receiver\",\"reader_payoff\":\"The reader hears the oath noun lean into the receiver phrase, matching the grammar that ties proof to qualified perception.\",\"reason\":\"The sound rows align with the attached receiver phrase and the repeated nunation at the noun and final restraint term.\",\"representative_source_ids\":[\"QP-a495b206\",\"QP-bee2eeb7\",\"MP-ddabf9d6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:6:construct-possessor-class","source_type":"word_analysis","support_id":"sup_afc0b5943c63cf63b654","text":"{\"blocking_evidence\":null,\"headline\":\"construct possessor creates a receiver class\",\"reader_payoff\":\"The reader notices that the ayah ends with a person-class defined by possessed restraint, not with an abstract quality alone.\",\"reason\":\"The word is genitive under the preposition and governs the following restraint noun in construct, matching the V4 possessor branch.\",\"representative_source_ids\":[\"QG-15a4e769\",\"QG-418abaae\",\"QT-25486fbf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:5:4:1","source_type":"qac_morpheme","support_id":"sup_b78344c68744204f420f","text":"{\"lemma_ar\":\"قَسَم\",\"morph_features\":\"STEM|POS:N|LEM:qasam|ROOT:qsm|M|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:5:4:1\",\"qac_word_ref\":\"89:5:4\",\"root_ar\":\"ق س م\",\"surface_ar\":\"قَسَمٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:5:recipient-suitability-range","source_type":"word_analysis","support_id":"sup_b8bb653b4cd967d85ec5","text":"{\"blocking_evidence\":null,\"headline\":\"recipient and suitability senses converge\",\"reader_payoff\":\"The reader keeps both audience and fitness in view: the oath is addressed to the restrained possessor because it is fit for that faculty.\",\"reason\":\"The broader range of the preposition is narrowed by its governed receiver phrase and by its attachment to the oath noun.\",\"representative_source_ids\":[\"QS-c6bfa568\",\"MS-4bdc71f5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:division-pressure-narrowed","source_type":"word_analysis","support_id":"sup_bbbab68d6006ac9179e9","text":"{\"blocking_evidence\":null,\"headline\":\"division field sharpens oath as sorting boundary\",\"reader_payoff\":\"The reader feels oath as a boundary-making act that separates accountable recognition from ordinary hearing, while the local noun still means oath.\",\"reason\":\"V4 separates oath and apportioning branches; local grammar selects the oath branch, while the root's division field survives as image-pressure rather than as an independent local sense.\",\"representative_source_ids\":[\"QS-300a217d\",\"QS-392b6865\",\"QS-e9cd5ac5\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:great-oath-echo","source_type":"word_analysis","support_id":"sup_c313e2dbd5af2c67c074","text":"{\"blocking_evidence\":null,\"headline\":\"asserted great oath becomes a question\",\"reader_payoff\":\"The reader notices a contrast with an asserted great oath elsewhere (56:76), while 89:5 makes recognition of oath-force the issue.\",\"reason\":\"The source rows give the concrete reference (56:76), and the local force is a question rather than an assertion.\",\"representative_source_ids\":[\"MI-1c6ad8e7\",\"QE-e2bc5f9d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:5:specialized-receiver","source_type":"word_analysis","support_id":"sup_c4257568a0d9929fe842","text":"{\"blocking_evidence\":null,\"headline\":\"oath is specialized to a restrained receiver\",\"reader_payoff\":\"The reader notices that oath-force becomes fully operative for a disciplined receiver, not for an undifferentiated audience.\",\"reason\":\"Attachment evidence marks the preposition as governing the possessor phrase and as the beneficiary or audience relation after the oath noun.\",\"representative_source_ids\":[\"QG-5a8c44f6\",\"QI-6e9e0238\",\"QY-f55307f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:receiver-qualified-oath","source_type":"word_analysis","support_id":"sup_c50c9f563b22af0abc50","text":"{\"blocking_evidence\":null,\"headline\":\"oath-force is qualified by its receiver\",\"reader_payoff\":\"The reader notices that oath-force in the ayah is inseparable from the class able to receive it.\",\"reason\":\"The following prepositional phrase attaches to the noun and identifies the beneficiary or audience of the oath evaluation.\",\"representative_source_ids\":[\"QG-1bc13041\",\"QT-0e779f38\",\"QY-5009027c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:forward-seeing-bridge","source_type":"word_analysis","support_id":"sup_c7d28ace786e0a8ec58a","text":"{\"blocking_evidence\":null,\"headline\":\"restraint prepares the next seeing test\",\"reader_payoff\":\"The reader sees why the following seeing challenge in 89:6 tests the same faculty required to recognize the oath.\",\"reason\":\"The source row gives the forward reference (89:6), and the local final receiver phrase supplies the faculty that the next challenge engages.\",\"representative_source_ids\":[\"QB-cd88de3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3:distal-reviewable-definiteness","source_type":"word_analysis","support_id":"sup_c9e1c56c1dbd359db850","text":"{\"blocking_evidence\":null,\"headline\":\"distal form makes the sequence reviewable\",\"reader_payoff\":\"The reader senses the prior signs as both already known and set apart for assessment.\",\"reason\":\"The demonstrative form supplies a definite pointer, while the local cross-reference makes that pointer backward-looking.\",\"representative_source_ids\":[\"QG-a25b4dd0\",\"QS-63ce1df8\",\"QF-f8f1f18e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7","source_type":"word_analysis","support_id":"sup_ce2eea9126fb3c53bd1b","text":"{\"gloss_range\":\"possessed restraint or disciplined intellect, qualitative rather than titular, functioning as the faculty that can recognize the oath\",\"prose\":\"{{ar:حِجْرٍ}} ({{tr:ḥijr}}) is the ayah's final criterion. As the genitive complement of {{ar:ذِى}} ({{tr:dhī}}), it is the possessed faculty that defines the receiver, and its indefinite form keeps that restraint qualitative rather than a fixed title. The local sense is disciplined intellect or restraint, not literal stone; still, the root's stone, enclosure, and interdiction field gives that intellect a boundary image. Reason here is the capacity that blocks misreading so the prior signs can be recognized as {{ar:قَسَمٌۭ}} ({{tr:qasamun}}). That makes the abstract restraint term marked against a wider concrete stone field, and the possessive formula names intellect through restraint rather than knowledge alone. Echoes of claimed prohibition and barred access are internalized as disciplined perception here (6:138; 25:22; 25:53). By ending on this compact, constricted word, the question lands on the hearer's bounded reason, and the next seeing challenge continues to test that faculty in 89:6.\",\"root_display\":\"{{ar:ح ج ر}} ({{tr:ḥ-j-r}})\",\"root_gloss_range\":\"root range includes restraint, prohibition, enclosure, hard stone, protected places, and reason as restraining faculty; local construct selects cognitive restraint while boundary and enclosure pressure remains active\",\"surface_display\":\"{{ar:حِجْرٍ}} ({{tr:ḥijr}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3","source_type":"word_analysis","support_id":"sup_d1296227f3928f27859c","text":"{\"gloss_range\":\"distal demonstrative that packages the preceding oath sequence as one definite, reviewable discourse object\",\"prose\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}}) compresses the preceding oath sequence into one definite object for review. Its distal form marks the prior signs as a completed set, yet its anaphoric function keeps them close enough to be judged. Because it is governed by {{ar:فِى}} ({{tr:fī}}), the demonstrative is not loose pointing; it becomes the chamber in which {{ar:قَسَمٌۭ}} ({{tr:qasamun}}) is tested. The single pointer lets the ayah ask one judgment over the whole prior sequence without repeating each oath item, and its firm close lets that package settle before the oath noun arrives.\",\"root_display\":\"—\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:oath-noun-not-new-oath-item","source_type":"word_analysis","support_id":"sup_d3a886c7451456f012a3","text":"{\"blocking_evidence\":null,\"headline\":\"oath becomes evaluated status\",\"reader_payoff\":\"The reader sees the ayah naming the oath frame after it has been performed, rather than extending the list with another sworn object.\",\"reason\":\"The nominative noun functions inside the nominal question, and the previous oath sequence is already complete before it is evaluated.\",\"representative_source_ids\":[\"QG-522fbbe5\",\"QF-f405df74\",\"QI-8065c365\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:form-and-rarity","source_type":"word_analysis","support_id":"sup_d63dbcccccc40a7a232b","text":"{\"blocking_evidence\":null,\"headline\":\"rare abstract form makes restraint marked\",\"reader_payoff\":\"The reader notices the close of the ayah using a marked abstract restraint term rather than a common word for knowing.\",\"reason\":\"The contextual evidence shows the exact root form as limited in occurrence, and CRITICAL rows contrast this abstract use with concrete stone forms.\",\"representative_source_ids\":[\"QF-066fd862\",\"QI-8384d3be\",\"QH-cec25366\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:5:preposition-not-root","source_type":"word_analysis","support_id":"sup_de4aaea0d20636c2d4b5","text":"{\"blocking_evidence\":null,\"headline\":\"segmentation keeps the mechanism prepositional\",\"reader_payoff\":\"The reader avoids treating the compact visible phrase as root material and sees the logic as prepositional specialization.\",\"reason\":\"The QAC row corrects the segmented word to a rootless prefixed preposition governing the next word.\",\"representative_source_ids\":[\"QF-fa57fd80\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:4:delayed-indefinite-subject","source_type":"word_analysis","support_id":"sup_e1cdfe7efb02dda7fe19","text":"{\"blocking_evidence\":null,\"headline\":\"delayed subject names possible oath-value\",\"reader_payoff\":\"The reader notices that the noun asks whether the whole prior chain amounts to one binding oath-value.\",\"reason\":\"QAC and attachment evidence mark the noun as an indefinite nominative delayed subject of the fronted predicate.\",\"representative_source_ids\":[\"QG-1481aa51\",\"QG-de07c4c4\",\"QF-e13d831f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3:hard-close-pointer","source_type":"word_analysis","support_id":"sup_e1e0a693703f1df8d84d","text":"{\"blocking_evidence\":null,\"headline\":\"pointer closes as a package\",\"reader_payoff\":\"The reader hears the demonstrative close firmly before the oath noun arrives.\",\"reason\":\"The sound observation supports the demonstrative's packaging function without changing the grammatical analysis.\",\"representative_source_ids\":[\"QP-fa8822c1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:3:governed-bridge","source_type":"word_analysis","support_id":"sup_ec0c3a7afd1a07f9f792","text":"{\"blocking_evidence\":null,\"headline\":\"governed pointer bridges domain and oath\",\"reader_payoff\":\"The reader sees the demonstrative as the grammatical bridge that lets the old oath sequence enter the new containment clause.\",\"reason\":\"The demonstrative is governed by the preposition and stands between the containment phrase and the delayed oath noun.\",\"representative_source_ids\":[\"QG-49876d03\",\"QT-551dd848\",\"QB-cbd4dbb6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:2:recategorizing-bridge","source_type":"word_analysis","support_id":"sup_ec1c1ebf996dbbe6c2ac","text":"{\"blocking_evidence\":null,\"headline\":\"oath chain becomes contained evidence\",\"reader_payoff\":\"The reader sees a chain of sworn items recategorized as a chamber of evidence.\",\"reason\":\"The demonstrative reference and fronted containment phrase together reframe the previous oath material as the field being evaluated.\",\"representative_source_ids\":[\"QB-684f04e8\",\"QY-2f493560\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:final-question-landing","source_type":"word_analysis","support_id":"sup_ed0664ed6cadb2390422","text":"{\"blocking_evidence\":null,\"headline\":\"the question lands on restrained reason\",\"reader_payoff\":\"The reader sees the ayah's close shift responsibility toward the hearer's bounded reason.\",\"reason\":\"The clause moves from question to oath noun to specialized receiver, ending with the faculty that makes recognition possible.\",\"representative_source_ids\":[\"QT-4bd0d64d\",\"MT-5be8f838\",\"QY-ba6f3075\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:passive-and-self-boundary-pressure","source_type":"word_analysis","support_id":"sup_ef77e3bac4c0f8d8fa86","text":"{\"blocking_evidence\":null,\"headline\":\"barredness becomes mental filtering\",\"reader_payoff\":\"The reader sees restraint as active mental filtering: some readings are barred so the oath can be recognized rightly.\",\"reason\":\"Passive and derived forms add filtering pressure, but the local surface remains the possessed faculty rather than an object being barred.\",\"representative_source_ids\":[\"QS-70b3867a\",\"QS-94c9795e\",\"QF-b161c168\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:5:7:constricted-closure-sound","source_type":"word_analysis","support_id":"sup_fce9cd8336f8788ab381","text":"{\"blocking_evidence\":null,\"headline\":\"compressed sound fits boundary meaning\",\"reader_payoff\":\"The reader hears the final word close compactly, matching its meaning of restraint and boundary.\",\"reason\":\"The sound rows reinforce the final-position boundary effect without changing the selected cognitive-restraint sense.\",\"representative_source_ids\":[\"QP-4c6be615\",\"QP-67977a5c\",\"MP-d6dfb7a1\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B002","root_001226/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001226","role":"The oath apportioned among its holders supplies the utterance's binding evidentiary force.","root":"ق س م","source_ref":"89:5","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000296","role":"Reason as a restraining barrier defines the hearer able to receive that force without reckless inference.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]}],"changed_reading":{"after":"The question tests whether the hearer possesses an intellect whose operative mark is self-restraint, so receiving the oath is itself an ethical-cognitive act.","before":"A conventional rhetorical affirmation that the preceding expressions are an oath for an intelligent person."},"confidence":"strong","focus_anchor":"قَسَمٌ at 89:5.4 as an oath and حِجْرٍ at 89:5.6 as reason whose defining action is restraint.","mechanism":"The interrogative joins an oath-speech-act to a qualified recipient: the oath becomes probative only for a faculty that can keep improper inference and action back. Intelligence is therefore functional and ethical, not merely informational.","model_id":"baseline_oath_for_restraining_reason"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_oath_for_restraining_reason","source_type":"hft","support_id":"sup_62a26cba386d7e726bcd","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B001","root_000296/B006","root_001226/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001226","role":"Apportioning a whole into shares turns qasam into an internal division within 'that.'","root":"ق س م","source_ref":"89:5","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000296","role":"Keeping back by enclosure makes hijr the capacity to preserve the resulting limits.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]},{"branch_id":"B006","mapped_root_id":"root_000296","role":"The circling boundary mark gives the discerned division a visible perimeter.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]}],"changed_reading":{"after":"The question can also ask whether 'that' contains a measured partition for one capable of recognizing and keeping boundaries.","before":"Qasam names only the speech-act of swearing and hijr is a conventional synonym for intellect."},"confidence":"medium","focus_anchor":"The locative فِى ذَٰلِكَ holds قَسَمٌ at 89:5.4 together with the enclosure and boundary possibilities of حِجْرٍ at 89:5.6.","mechanism":"If qasam is an apportioning and hijr is a kept boundary, the question asks whether the deictically gathered material contains a legible division. The possessor of hijr is then someone able both to detect and to preserve distinctions.","model_id":"baseline_apportioned_boundary"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_apportioned_boundary","source_type":"hft","support_id":"sup_a78427d687a82ce6cde3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ","ayah_ref":"89:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000296/B002","root_001226/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001226","role":"A mind divided between courses supplies the open alternatives under deliberation.","root":"ق س م","source_ref":"89:5","source_word_indices":["4"]},{"branch_id":"B002","mapped_root_id":"root_000296","role":"Restraining reason contains the alternatives long enough for discriminating judgment.","root":"ح ج ر","source_ref":"89:5","source_word_indices":["6"]}],"changed_reading":{"after":"The verse can stage a decision chamber: several courses are held apart and weighed by a reason defined through restraint.","before":"The verse merely asks whether an intelligent audience recognizes an oath."},"confidence":"exploratory","focus_anchor":"قَسَمٌ at 89:5.4 activates a mind divided among courses while حِجْرٍ at 89:5.6 activates the reason that restrains.","mechanism":"The two focus roots form a deliberative loop: an affair divides attention among possible courses, and restraining reason keeps that division from becoming dispersion. The interrogative tests whether the gathered material is sufficient for disciplined choice.","model_id":"baseline_divided_deliberation"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_divided_deliberation","source_type":"hft","support_id":"sup_c7ccb4b0d9457b7d5cbe","trust":"legacy_unbound"}]}
</lane_packet_json>
