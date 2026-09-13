# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **89:27**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s089-regular-20260912/s089/89_27/micro.discovery.json` and modify nothing
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
  "ayah_ref": "89:27",
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
{"branch_registry":[{"boundary":"Dalın sınırı iç hareketin yatışması ve güven duygusuna geçiştir; fiziksel alçalma bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000948/B001","candidate_links":[{"candidate_id":"cand_273e88bd4ea4aeac7c40","lane":"micro"},{"candidate_id":"cand_82b0d0d8b27accd52efc","lane":"micro"},{"candidate_id":"cand_b7d41e0e669fe7d533a7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّطْمَئِنَّة","morph_features":"STEM|POS:ADJ|ACT|PCPL|(XII)|LEM:m~uToma}in~ap|ROOT:Tmn|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:27:3:2","qac_word_ref":"89:27:3","surface_ar":"مُطْمَئِنَّةُ"}],"gloss":"tedirginlikten sonra durulup güven duygusuna kavuşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tedirginlikten sonraki iç hareketlilik sona erer ve kişi, yürek ya da benlik durulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Durulmaya yabancılığın çözülmesi, yakınlık ve güven içinde rahat etme eşlik eder."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Çekirdek durum, bir yerde yerleşip durulmaya veya bir şeye yönelerek iç rahatlığı bulmaya uzanır."}}],"root_ar":"ط م ن","root_id":"root_000948","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın tedirginlikten durulmaya ve iç güvene uzanan bütün çekirdeğini karşılar.","boundary_detail":"Dalın sınırı iç hareketin yatışması ve güven duygusuna geçiştir; fiziksel alçalma bu dala girmez.","branch_image_ar":"السكون والطمأنينة","concept_gloss":"tedirginlikten sonra durulup güven duygusuna kavuşma","contextual_glosses":[{"applicability":"Kişi, yürek veya benliğin tedirginlikten sonra durulduğu anlatımlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir yerde veya bir şeye yönelerek yerleşme uzantısını açıkça söylemez.","preserves":"Tedirginlikten sonraki iç yatışmayı ve durulmayı korur."},"facet_ids":["F001","F002"],"text":"içi yatıştı","usage_role":"contextual"},{"applicability":"Yabancılığın çözülüp güven ve iç rahatlığının öne çıktığı insan bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Önceki tedirginlikten sonraki durulma sürecini ve yer uzantısını belirtmez.","preserves":"Güven ve yabancılık çekmeden rahat etme sonucunu korur."},"facet_ids":["F002"],"text":"kendini güvende hissetti","usage_role":"contextual"},{"applicability":"Bir yerde kalıcılık ve durulmanın birlikte anlatıldığı yer bağlamlarına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişinin tedirginlikten sonra güven duygusuna kavuşmasını tek başına karşılamaz.","preserves":"Bir yerde yerleşme ve hareketliliğin sona ermesi uzantısını korur."},"facet_ids":["F003"],"text":"orada yerleşip duruldu","usage_role":"contextual"}],"definition":"Bir kişi, yürek veya benlik tedirginlikten sonra iç hareketliliğini yitirip durulur ve kendini güvende, yabancılık çekmeden rahat hisseder. Aynı çekirdek, bir yerde yerleşip durulma veya bir şeye yönelerek iç rahatlığı bulma biçiminde de gerçekleşebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tedirginlikten sonraki iç hareketlilik sona erer ve kişi, yürek ya da benlik durulur."},{"facet_id":"F002","role":"core","statement":"Durulmaya yabancılığın çözülmesi, yakınlık ve güven içinde rahat etme eşlik eder."},{"facet_id":"F003","role":"extension","statement":"Çekirdek durum, bir yerde yerleşip durulmaya veya bir şeye yönelerek iç rahatlığı bulmaya uzanır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Genel bedensel kolaylık veya elverişlilik anlamlarıyla karışabilir.","fit":"narrowing","loses":"Önceki tedirginliği, durulma geçişini ve yerleşme uzantısını siler.","preserves":"Ortaya çıkan iç rahatlığını ve güvenli son durumu korur."},"text":"rahatlık"},{"category":"confusable","error_profile":{"adds":"Ses bulunmaması koşulunu gereksiz yere anlama ekler.","collision":"Duygusal durulma yerine işitilebilir sesin yokluğu anlaşılır.","fit":"displacement","loses":"İç yatışmasını, güveni ve tedirginlikten sonraki geçişi kaybeder.","preserves":"Hareketliliğin sona ermesi düşüncesinin yalnızca dış görünüşünü korur."},"text":"sessizlik"}],"identity_rationale":"Kaynak ifadesi, kişi, yürek veya benliğin tedirginlikten sonra durulmasını ve kendini yabancılık çekmeden güvende hissetmesini dalın çekirdeği olarak açıkça destekler. Yerleşme ve bir şeye yönelerek dinginleşme kullanımları da bu çekirdeğin katılımcıya veya yapıya bağlı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tedirginlikten sonra durulup kendini güvende hissetmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"tedirginlikten sonra durulma"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iç yatışması ve güven duygusu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeye güvenip onunla içi rahat eden"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"inançla dinginleşip Yaradan'a içten yönelen benlik"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"inançla güç bulup dingin kalan yürek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ondan dolayı durulmak"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ondan dolayı durulmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"dingin olanı küçültmeli veya sevecen biçimde anlatan söz"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"dinginliği küçültmeli veya sevecen biçimde anlatan söz"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ses ve anlamca hem durulmaya hem alçalmaya yaklaşan biçim"}],"lexicalization_note":"Tanım, genel durulma çekirdeğini belirli kişi, yürek, benlik, yer ve yönelme yapılarındaki gerçekleşmelerden ayırır; inanca bağlı özel kullanım bütün dala yayılmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnızca iç durulma sınırını fiziksel alçalma, yönelme, yakınlık, dayanıklılık ve korkuyu giderme alanlarından belirgin biçimde ayıran komşular yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal ruhsal ya da durumsal bir yatışmayı anlatır; komşu dal ise arazide veya bedende gözlemlenen aşağı yönlü konumu ve biçim değişmesini anlatır.","focus_only":"Tedirginlikten sonra iç hareketin yatışması ve güven duygusunun doğması bu dala özgüdür.","gloss":"iç durulma ile fiziksel alçalma","neighbor_only":"Arazi yüzeyinin alçakta kalması veya sırtın fiziksel olarak eğilmesi öteki dala özgüdür.","neighbor_ref":"root_000948/B002","relation_type":"same_field","shared_zone":"İki dal, hareketin veya yüksekliğin azalması imgesini aynı kök çevresinde taşır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği tedirginliğin ardından iç yatışmasıdır; komşu dalın çekirdeği ise bir şeye meyledip ona dayanarak yanında kalmaktır.","focus_only":"Tedirginlikten sonraki iç durulma ve güvene kavuşma geçişi odaktadır.","gloss":"bir şeye yönelip durulma","neighbor_only":"Bir şeye yönelme, ona dayanma ve onun yanında kalıcılık gösterme odaktadır.","neighbor_ref":"root_000596/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeye karşı yönelişle birlikte durulma ve kararlılık bildirebilir."},{"boundary_match":"partial","distinction":"Bu dal durulma sonucunu merkeze alır; komşu dal ise alışma, yakınlık ve bunun doğurduğu açık, çekinmesiz ilişkiyi merkeze alır.","focus_only":"Önceki tedirginliğin sona ermesi ve iç hareketin durulması bu dalın belirleyici yönüdür.","gloss":"alışma ve yakınlık duyma","neighbor_only":"Bir kişi veya şeye alışıp yakınlık duyarak açılma ve çekinmeden davranma komşuya özgüdür.","neighbor_ref":"root_000563/B007","relation_type":"near_neighbor","shared_zone":"Yabancılığın çözülmesi ve bir kişi ya da şey yanında rahat etme iki alanda da bulunur."},{"boundary_match":"partial","distinction":"Bu dal rahatsızlığın ardından gelen yatışmış durumu anlatır; komşu dal ise korku anında gösterilen direnç ve kararlılığı anlatır.","focus_only":"Tedirginlikten sonra iç hareketin yatışıp güvenli bir duruma dönüşmesi bu dalda esastır.","gloss":"yürek dayanıklılığı","neighbor_only":"Korku sürerken yüreği güçlü tutma, dayanma ve geri çekilmeme komşu dalda esastır.","neighbor_ref":"root_000535/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal korku veya tedirginlik karşısında iç düzenin korunmasıyla ilgilidir."},{"boundary_match":"partial","distinction":"Bu dal yaşayanın iç durumundaki yatışmayı adlandırır; komşu dal bu sonucu doğuran korkuyu giderme eylemini adlandırır.","focus_only":"Kişi veya yürekte ortaya çıkan durulmuş ve güvenli durum bu dalın konusudur.","gloss":"korkunun giderilmesi","neighbor_only":"Korkuyu kişiden ya da yürekten uzaklaştıran dışsal veya nedensel işlem komşunun konusudur.","neighbor_ref":"root_001152/B004","relation_type":"near_neighbor","shared_zone":"Korku ya da tedirginlik sonrasında rahatlama iki dalın ortak sonuç alanıdır."}],"source_phrase_ar":"الطمأنينة والاطمئنان السكون بعد الانزعاج (mufradat)؛ اطمأن الرجل واطمأن قلبه واطمأنت نفسه إذا سكن واستأنس (ayn)؛ اطمأن الرجل اطمئنانا وطمأنينة أي سكن (sihah)؛ اطمأن قلبه إذا سكن والاسم الطمأنينة (tahdhib)؛ يقال اطمأن المكان يطمئن طمأنينة وطامنت منه سكنت (maqayis)","source_summary":"Kaynakların ortak çizgisi, kişi, yürek ya da benlikte beliren durulma ve sakinleşmedir. Tedirginliğin ardından gelme kaydı ortak çizgi değil, kaynaklardan birinin ek belirlemesidir; yer ve yönelme yapıları bu temel durumun bağlama bağlı gerçekleşmelerini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"السكون والأنس وطمأنينة القلب أو النفس أو الرجل، والسكون إلى الشيء أو بالإيمان بعد انزعاج","what_is_not_ar":"انخفاض الأرض وحني الظهر إذا كان المراد صورة حسية لا سكونا ولا أنسا"},"support_links":["sup_76a7755cb4b4fa21581c","sup_b6eaa5b9e6cdd98e303b","sup_e01ceda026aa2914df65"]},{"boundary":"Dal yalnızca gözlenebilir alçak konum ve aşağı doğru eğme kullanımlarını kapsar; iç yatışması bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000948/B002","candidate_links":[{"candidate_id":"cand_c7c66cce6cec5fa0028f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُّطْمَئِنَّة","morph_features":"STEM|POS:ADJ|ACT|PCPL|(XII)|LEM:m~uToma}in~ap|ROOT:Tmn|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:27:3:2","qac_word_ref":"89:27:3","surface_ar":"مُطْمَئِنَّةُ"}],"gloss":"fiziksel olarak alçakta bulunma ya da aşağı doğru eğme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ortak fiziksel eksen, bir şeyin çevresine göre aşağıda bulunması veya aşağı yönlü biçim almasıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Arazi kullanımında, çevresindeki yüzeye göre alçakta kalan yer veya bölüm anlatılır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Beden kullanımında, sırt eğilerek aşağı indirilir ve ona alçalmış bir biçim verilir."}}],"root_ar":"ط م ن","root_id":"root_000948","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Araziye ait alçak konumu ve sırtı aşağı doğru eğme işlemini birlikte karşılar.","boundary_detail":"Dal yalnızca gözlenebilir alçak konum ve aşağı doğru eğme kullanımlarını kapsar; iç yatışması bu sınıra girmez.","branch_image_ar":"التطامن والانخفاض الحسي","concept_gloss":"fiziksel olarak alçakta bulunma ya da aşağı doğru eğme","contextual_glosses":[{"applicability":"Çevresindeki yüzeye göre aşağıda kalan yer veya arazi bölümünü anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sırtı eğerek aşağı indirme gerçekleşmesini karşılamaz.","preserves":"Araziye ait alçak konumu ve çevreye göre aşağıda kalmayı korur."},"facet_ids":["F001","F002"],"text":"alçak arazi","usage_role":"contextual"},{"applicability":"Bir kişinin sırtını bükerek aşağı indirdiği beden bağlamlarında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Arazinin çevresine göre alçakta bulunması gerçekleşmesini karşılamaz.","preserves":"Sırtın aşağı yönlü bükülmesini ve biçim değişmesini korur."},"facet_ids":["F001","F003"],"text":"sırtını eğdi","usage_role":"contextual"}],"definition":"Bu dal, arazinin çevresine göre alçakta bulunmasını ve sırtın eğilerek aşağı indirilmesini kapsayan fiziksel alçalma alanıdır. Alçak konum ile aşağı yönlü biçim verme, belirli biçim ve yapılarda ayrı gerçekleşmeler olarak korunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ortak fiziksel eksen, bir şeyin çevresine göre aşağıda bulunması veya aşağı yönlü biçim almasıdır."},{"facet_id":"F002","role":"specialization","statement":"Arazi kullanımında, çevresindeki yüzeye göre alçakta kalan yer veya bölüm anlatılır."},{"facet_id":"F003","role":"specialization","statement":"Beden kullanımında, sırt eğilerek aşağı indirilir ve ona alçalmış bir biçim verilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kenarlarla çevrili oyuk veya kazılmış boşluk düşüncesini ekleyebilir.","collision":"Her alçak arazi bölümü belirgin bir oyuk olmak zorunda değildir.","fit":"narrowing","loses":"Sırtı eğme işlemini ve genel aşağı yönlü biçim verme eksenini kaybeder.","preserves":"Çevresine göre aşağıda kalan arazi görünümünü korur."},"text":"çukur"},{"category":"confusable","error_profile":{"adds":"Kendiliğinden düşme, dayanamama veya yapısal bozulma anlamı ekler.","collision":"Durağan alçaklık ve denetimli eğme yerine bir bozulma olayı anlaşılabilir.","fit":"displacement","loses":"Arazinin durağan alçak konumunu ve isteyerek sırt eğmeyi kaybeder.","preserves":"Aşağı yönlü konum değişmesi düşüncesini kısmen korur."},"text":"çökmek"}],"identity_rationale":"Kaynak ifadesi, çevresine göre alçakta kalan araziyi ve sırtın eğilip aşağı indirilmesini aynı fiziksel alçalma alanında açıkça birleştirir. Bu çerçeve, iç durulma dalından ayrıldığı sürece verilen dal kimliğini doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"arazinin çevresine göre alçak bölümü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"çevresine göre alçakta kalan arazi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"sırtını eğip aşağı indirdi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"sırtını eğip aşağı indirdi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sırtını eğip aşağı indirdi"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ses ve anlamca hem durulmaya hem alçalmaya yaklaşan biçim"}],"lexicalization_note":"Tanım, araziyi niteleyen biçimlerle sırtı eğme yapılarını ayrı alt gerçekleşmeler olarak tutar; bunlardan sınırsız bir çıplak kök anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnızca fiziksel alçalma sınırını iç durulma, genel aşağı indirme, beden eğilmesi, yön değiştirme ve düzleşmiş biçim alanlarından ayıran komşular yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal mekanda ya da bedende gözlemlenen aşağı yönlü konum ve biçimi anlatır; komşu dal ise ruhsal veya durumsal yatışmayı anlatır.","focus_only":"Arazi yüzeyinin alçakta kalması veya sırtın gözle görülür biçimde eğilmesi bu dala özgüdür.","gloss":"fiziksel alçalma ile iç durulma","neighbor_only":"Tedirginlikten sonra iç hareketin yatışması ve güven duygusunun doğması öteki dala özgüdür.","neighbor_ref":"root_000948/B001","relation_type":"same_field","shared_zone":"İki dal, hareketin veya yüksekliğin azalması imgesini aynı kök çevresinde taşır."},{"boundary_match":"partial","distinction":"Bu dal belirli arazi ve sırt yapılarıyla sınırlıdır; komşu dal aşağı indirmeyi çok daha geniş nesne, değer ve dilbilgisi alanlarına taşır.","focus_only":"Alçak arazi ile sırtı eğme gerçekleşmelerinin aynı sınırlı dalda birleşmesi bu dala özgüdür.","gloss":"aşağı indirme ve alçaklık","neighbor_only":"Her tür nesneyi yüksekten aşağı indirme, değer düşürme ve dilbilgisel kullanım komşu dalın daha geniş alanıdır.","neighbor_ref":"root_000426/B001","relation_type":"near_synonym","shared_zone":"Her iki dal fiziksel bir yükseklik ekseninde aşağıda bulunmayı veya aşağı indirmeyi kapsar."},{"boundary_match":"partial","distinction":"Bu dal sırtı ve alçak araziyi kapsar; komşu dal baş ile boynun kapanıp aşağı yönelmesini ve benzer batış hareketlerini merkeze alır.","focus_only":"Alçak arazi ve özellikle sırtın eğilmesi bu dalın ayırt edici gerçekleşmeleridir.","gloss":"baş ve boynu aşağı eğme","neighbor_only":"Baş ve boynun öne ya da aşağı sarkması ile gök cisminin batışa yönelmesi komşuya özgüdür.","neighbor_ref":"root_000419/B002","relation_type":"near_neighbor","shared_zone":"Beden bölümünün aşağı yönlü eğilmesi iki dalın kesiştiği fiziksel alandır."},{"boundary_match":"partial","distinction":"Bu dal aşağı yönlü ekseni zorunlu tutar; komşu dalın bükülme ve yön değiştirme çekirdeği aşağı yönle sınırlı değildir.","focus_only":"Çevreye göre alçak arazi konumu ve sırtın aşağı indirilmesi bu dalda belirleyicidir.","gloss":"bükme ve yön değiştirme","neighbor_only":"Bir şeyi yana, geriye veya kıvrımlı bir yöne çevirme ve genel bükme komşu dalda belirleyicidir.","neighbor_ref":"root_001026/B001","relation_type":"near_neighbor","shared_zone":"Sırtın biçimini değiştirerek eğilmesi, iki dalın kesiştiği dar kullanım alanıdır."},{"boundary_match":"partial","distinction":"Bu dal alçak konumla aşağı eğme işlemini birleştirir; komşu dal ise düzleşme, yayvanlık ve biçimsel alçaklığı çeşitli varlıklara yayar.","focus_only":"Sırtı aşağı eğme işlemi ve çevreye göre alçak arazi bu dalın birlikte tuttuğu sınırlardır.","gloss":"alçak ve düz biçim","neighbor_only":"Düzleşmiş yer, yayvan sırt ve alçak ya da düz biçimli hayvan nitelikleri komşu dalın alanıdır.","neighbor_ref":"root_000482/B002","relation_type":"near_neighbor","shared_zone":"Arazi veya sırtın alçak görünümü iki dalın ortak fiziksel betimleme alanıdır."}],"source_phrase_ar":"المطمئن من الأرض أرض منخفضة وهي المتطأمنة (ayn)؛ طمأن ظهره وطامنه بمعنى (sihah)؛ طامن ظهره إذا حناه ومنهم من يقول طأمن (tahdhib)","source_summary":"Kaynakların ortak fiziksel çizgisi iki belirgin gerçekleşme taşır: arazi çevresine göre alçakta kalabilir, sırt ise eğilerek aşağı indirilebilir. Yazım değişiklikleri, sırtı eğme işleminin kavramsal sınırını değiştirmez.","sources":["AY","SI","TA"],"what_is_ar":"انخفاض الأرض وتطامنها، وحني الظهر أو طأمنته وطامنه","what_is_not_ar":"طمأنينة القلب والنفس والسكون بعد الانزعاج إذا لم يرد خفض حسي"},"support_links":["sup_91618802710111938c9a"]},{"boundary":"Anlam, canlı solunumuyla sınırlıdır; can, kan, öz varlık ya da sıkıntı giderme anlamlarını içermez.","branch_kind":"bare","branch_ref":"root_001533/B001","candidate_links":[{"candidate_id":"cand_b7d41e0e669fe7d533a7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"soluk alıp verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Havanın ağız ya da burun yoluyla gövdeye girip yeniden çıkmasıdır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçme sırasında verilen her ara soluk, aynı solunum döngüsünün sayılan bir örneğidir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlının havayı içine alıp dışarı verdiği temel bedensel süreç için kullanılır.","boundary_detail":"Anlam, canlı solunumuyla sınırlıdır; can, kan, öz varlık ya da sıkıntı giderme anlamlarını içermez.","branch_image_ar":"خروج النسيم من الجوف","concept_gloss":"soluk alıp verme","contextual_glosses":[{"applicability":"Solunumun ya da içme sırasında verilen aranın tek bir döngü olarak sayıldığı yerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tek bir giriş-çıkış döngüsünün sayılabilirliğini korur."},"facet_ids":["F002"],"text":"bir soluk","usage_role":"contextual"}],"definition":"Akciğerli bir canlının havayı ağız ya da burun yoluyla gövdesine alıp yeniden dışarı vermesidir. Her bir giriş-çıkış döngüsü ayrı bir soluk olarak sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Havanın ağız ya da burun yoluyla gövdeye girip yeniden çıkmasıdır."},{"facet_id":"F002","role":"example","statement":"İçme sırasında verilen her ara soluk, aynı solunum döngüsünün sayılan bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, akciğerli bir canlının gövdesine havanın girip çıkmasını ve bu döngünün tek tek sayılabilmesini doğrudan anlatır. İçme sırasında sayılan soluklar da bu bedensel sürecin özel bir bağlamıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"soluk alıp verme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"gövdeye girip çıkan hava; soluk"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tek soluk ya da soluklanma arası"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"soluklar"}],"lexicalization_note":"Çıplak dal, soluk alıp verme sürecini bildirir; içme bağlamı yalnızca bu sürecin sayıldığı bir kullanımdır.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; soluk verme odağındaki bu komşu, temel sınırı en açık biçimde gösterdiği için seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hava alma ile vermeyi birlikte içeren genel solunumdur; komşu ise özellikle güçlü dışa verişi ve doğan sesi anlatır.","focus_only":"Odak dal, sessiz ve olağan hava girişini de kapsayan tam solunum döngüsüdür.","gloss":"soluk verme ve ses çıkarma","neighbor_only":"Komşu dal, göğüsten havayı dışarı vermeye, buna eşlik eden sese ve sıkıntı belirtisine ağırlık verir.","neighbor_ref":"root_000634/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da gövdedeki havanın dışarı çıkması bulunur."}],"source_phrase_ar":"التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)","source_summary":"Kaynaklar, temel anlamı havanın canlı gövdesine girip çıkması ve bu hareketin tekil döngüler hâlinde sayılması olarak ortaklaştırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه التنفس والأنفاس وخروج الريح من الجوف أو الفم والمنخر، وما يلحق به من نفس الشرب إذا كان المراد به نفسا في الشرب.","what_is_not_ar":"ليس هو الروح أو الذات أو الدم ولا التفريج عن الكربة إلا من جهة المجاز."},"support_links":["sup_e01ceda026aa2914df65"]},{"boundary":"Dal, önceden var olan bir sıkıntının giderilmesini gerektirir; genel genişlik, süre ya da bedensel solunum değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B002","candidate_links":[{"candidate_id":"cand_b7d41e0e669fe7d533a7","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"sıkıntıyı hafifletip ferahlatma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sıkıntı içindeki kişinin yükünü hafifletip onu rahatlatma eylemidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Esinti veya yardım, sıkıntıdakine ferahlık getiren araç olarak adlandırılabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin içinde bulunduğu darlık ya da ağır durum etkin biçimde azaltıldığında uygundur.","boundary_detail":"Dal, önceden var olan bir sıkıntının giderilmesini gerektirir; genel genişlik, süre ya da bedensel solunum değildir.","branch_image_ar":"توسيع الكربة بالتنفيس","concept_gloss":"sıkıntıyı hafifletip ferahlatma","contextual_glosses":[{"applicability":"Esinti veya yardım, sıkıntıdaki kişiyi rahatlatan araç olarak anıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aracın sıkıntıyı gideren işlevini açıkça korur."},"facet_ids":["F002"],"text":"ferahlık getiren esinti ya da yardım","usage_role":"explanatory"}],"definition":"Sıkıntı içindeki birinin üzerindeki baskıyı azaltıp ona rahatlama sağlamaktır. Esinti ya da yardım, bu rahatlamayı sağladığı ölçüde aynı anlam alanına girer.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sıkıntı içindeki kişinin yükünü hafifletip onu rahatlatma eylemidir."},{"facet_id":"F002","role":"associated_use","statement":"Esinti veya yardım, sıkıntıdakine ferahlık getiren araç olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi, sıkıntı içindeki kişinin yükünü hafifletme ve ona ferahlık sağlama eylemini açıkça kurar. Esinti ya da yardım da ancak bu rahatlatıcı işlev bakımından dala girer.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"Tanrı onun sıkıntısını giderdi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"beni sıkıntıdan kurtarıp rahatlat"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı"}],"lexicalization_note":"Eylem kalıpları sıkıntıyı giderme işini, ayrı bir kullanım ise esinti ya da yardımı bu işin aracı olarak anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sıkıntının giderilmesiyle doğan rahatlama sınırını en iyi açıklayan yakın anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, bir sıkıntıyı giderip kişiye ferahlık verme eylemidir; komşu, bu etkinin sonucu olan çözülme ve kurtulma durumuna daha çok ağırlık verir.","focus_only":"Odak dal, sıkıntıyı etkin biçimde hafifleten kişi, güç ya da aracı öne çıkarır.","gloss":"üzüntü ve sıkıntının çözülmesi","neighbor_only":"Komşu dal, üzüntü ve kaygının çözülüp ortadan kalkması sonucunu daha geniş biçimde kapsar.","neighbor_ref":"root_001139/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da darlık ve üzüntüden rahatlığa geçişi anlatır."}],"source_phrase_ar":"نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)","source_summary":"Kaynaklar, sıkıntının hafifletilmesi ile bunun sağladığı ferahlığı ortak çekirdek sayar; esinti ve yardım bu işlevle ilişkilendirilir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه نفس الله الكربة، والتنفس عن المكروب، والفرج من الشدة، والريح أو الأنصار حين تذكر باعتبار التفريج.","what_is_not_ar":"ليس هو مجرد النفس الهوائي ولا مطلق السعة أو المهلة بلا كربة."},"support_links":["sup_e01ceda026aa2914df65"]},{"boundary":"Buradaki göz, görme organı ya da özdeşlik bildiren göz değil, zarar verdiğine inanılan bakıştır.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"kem gözle zarar verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Zarar verdiğine inanılan bakışın bir kişiye yönelip onu etkilemesidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zararlı bakışı yönelten kişi, bu etkiyi yapan kimse olarak adlandırılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir bakışın kişiye zarar getirdiğine inanılan etkiyi ve gerçekleşmesini anlatır.","boundary_detail":"Buradaki göz, görme organı ya da özdeşlik bildiren göz değil, zarar verdiğine inanılan bakıştır.","branch_image_ar":"إصابة العين بالنفس","concept_gloss":"kem gözle zarar verme","contextual_glosses":[{"applicability":"Zararlı olduğuna inanılan bakışın bir kişiyi etkilediği cümlelerde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakışın hedefe ulaşıp zarar vermesi olayını korur."},"facet_ids":["F001"],"text":"kem göz değmesi","usage_role":"contextual"}],"definition":"Bir kişinin bakışıyla başkasına zarar verdiğine inanılan etki ve bu etkinin birine ulaşmasıdır. Bu bakışı yönelten kişi de dalın adlandırma alanındadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Zarar verdiğine inanılan bakışın bir kişiye yönelip onu etkilemesidir."},{"facet_id":"F002","role":"associated_use","statement":"Zararlı bakışı yönelten kişi, bu etkiyi yapan kimse olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi, bir bakışın kişiye zarar verdiği inancını, bu zararın gerçekleşmesini ve zararlı bakışı yönelten kişiyi aynı dalda açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"zarar verdiğine inanılan bakış"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ona kem göz değdi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kem gözle zarar veren kişi"}],"lexicalization_note":"Çıplak biçimler zararlı bakışı ve bunu yönelten kişiyi, kalıp kullanım ise bakışın birine değmesini anlatır.","neighbor_coverage_note":"Bütün aday kartlar gözden geçirildi; yalnızca sınırları tam örtüşen eş anlamlı dal yayımlanmaya değer bulundu.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, katılımcılar ve kapsam bakımından anlamlı bir ayrım görünmez; iki dal birbirinin yerine geçebilir.","focus_only":null,"gloss":"kem gözle zarar verme","neighbor_only":null,"neighbor_ref":"root_001069/B004","relation_type":"synonym","shared_zone":"İki dal da bakışla zarar verme, bunu yapan kişi ve bundan etkilenen kişi sınırlarını paylaşır."}],"source_phrase_ar":"يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)","source_summary":"Kaynaklar, zarar veren bakış, bu bakışın birine değmesi ve onu yönelten kişi arasında ortak ve tutarlı bir anlam bağı kurar.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه تسمية العين نفسا، وإصابة المنظور بنفس، والنافس بمعنى العائن.","what_is_not_ar":"ليس هو عين الشيء بمعنى ذاته ولا النفس الروح."},"support_links":[]},{"boundary":"Dal kanı anlatır; canın kendisi, doğum sonrası kanama ya da her türlü sıvı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"canlıdaki akışkan kan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı gövdesinde bulunan ve akabilen kanı adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanın yitirilmesi yaşamın yitirilmesine yol açtığı için kan ile can arasında bağ kurulur."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlı gövdesindeki kan ve özellikle akışkan kana sahip olma anlatıldığında uygundur.","boundary_detail":"Dal kanı anlatır; canın kendisi, doğum sonrası kanama ya da her türlü sıvı değildir.","branch_image_ar":"الدم السائل قوام النفس","concept_gloss":"canlıdaki akışkan kan","contextual_glosses":[{"applicability":"Bir hayvanın akışkan kana sahip olduğu kalıp kullanımda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Canlının akışkan kana sahip olması koşulunu korur."},"facet_ids":["F001"],"text":"kanı akan canlı","usage_role":"contextual"}],"definition":"Canlı gövdesinde dolaşan ve akabilen kandır; kaybının yaşamı sona erdirmesi, adlandırmanın gerekçesi olarak görülür. Akışkan kana sahip olma da özel bir kalıpla belirtilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı gövdesinde bulunan ve akabilen kanı adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Kanın yitirilmesi yaşamın yitirilmesine yol açtığı için kan ile can arasında bağ kurulur."}],"identity_rationale":"Kaynak ifadesi, anlamı doğrudan kana bağlar ve kanın kaybı ile yaşamın kaybı arasındaki ilişkiyi adlandırmanın gerekçesi olarak verir. Akışkan kanlı canlılara ilişkin kalıp da aynı sınırı doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kaybıyla yaşamın da yitirildiği kan"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"hayvandaki akışkan kan"}],"lexicalization_note":"Çıplak biçim kanı adlandırır; kalıp kullanım yalnızca hayvandaki akışkan kanı ve ona sahip olmayı belirtir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel kan alanıyla örtüşen bu komşu, odaktaki yaşam ve akışkanlık sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kanı yaşamı taşıyan akışkan madde olarak adlandırır; komşu dal ise kanın kendisine ek olarak yaradan dışarı çıkma olayını da anlatır.","focus_only":"Odak dal, kanı yaşamın sürmesiyle ilişkilendirir ve akışkan kanlı canlı kalıbını kapsar.","gloss":"kan ve kanama","neighbor_only":"Komşu dal, yara ya da kesikten kan çıkması olayını ve kan parçasını da kapsar.","neighbor_ref":"root_000491/B001","relation_type":"near_synonym","shared_zone":"İki dalın ortak alanı canlı gövdesindeki bilinen kandır."}],"source_phrase_ar":"النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)","source_summary":"Kaynaklar anlamı kan olarak ortaklaştırır; akışkan kanlı olma kalıbını ve kan kaybıyla yaşam kaybı arasındaki bağı da birlikte aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه النفس بمعنى الدم، والنفس السائلة، وتسميته نفسا لأن فقد الدم يذهب بالنفس.","what_is_not_ar":"ليس هو الروح نفسها ولا دم النفاس من جهة الولادة إلا إذا كان اللفظ دما."},"support_links":[]},{"boundary":"Doğum ve doğum sonrası durum çekirdektir; adet görme, kaynakça bildirilen bağımlı bir yan kullanımdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"doğum ve doğuma bağlı kadın-çocuk durumu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadının doğurmasını ve doğumdan sonraki kanamalı durumunu kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğan çocuk ve henüz doğmamış olma, doğum olayına göre adlandırılır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı kaynak kullanımlarında kadın için adet görme anlamı da bildirilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğurma olayı, doğum sonrası kadın ve doğan çocuk birlikte kavramsallaştırıldığında uygundur.","boundary_detail":"Doğum ve doğum sonrası durum çekirdektir; adet görme, kaynakça bildirilen bağımlı bir yan kullanımdır.","branch_image_ar":"خروج الولد ودم النفاس","concept_gloss":"doğum ve doğuma bağlı kadın-çocuk durumu","contextual_glosses":[{"applicability":"Yalnızca kaynakça bildirilen yan kullanımda, kadının dönemsel kanaması kastedildiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yan kullanımın kadın ve dönemsel kanama sınırını korur."},"facet_ids":["F003"],"text":"adet görme","usage_role":"contextual"}],"definition":"Kadının doğurması, doğumdan sonraki kanamalı durumu ve dünyaya gelen çocuğun bu olayla ilişkili adlandırılmasıdır. Bazı kullanımlarda aynı söz ailesi adet görmeye de uygulanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadının doğurmasını ve doğumdan sonraki kanamalı durumunu kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Doğan çocuk ve henüz doğmamış olma, doğum olayına göre adlandırılır."},{"facet_id":"F003","role":"source_variant","statement":"Bazı kaynak kullanımlarında kadın için adet görme anlamı da bildirilir."}],"identity_rationale":"Kaynak ifadesinin ana ekseni kadının doğurması, doğumdan sonraki durumu ve doğan çocuktur. Bunun yanında bazı kullanımlarda aynı söz ailesi adet görme için de aktarılır; bu yan kullanım doğum çekirdeğiyle özdeşleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"doğum yapmış ya da doğum sonrası kanaması olan kadın"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"doğum ve doğum sonrası kanama dönemi"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yeni doğan çocuk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"doğmadan önce"}],"lexicalization_note":"Biçimler doğum yapan kadını, doğum sürecini ve yeni doğanı; ayrı kullanım ise doğmadan önceki zamanı belirtir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; adet kanaması komşusu, doğum çekirdeği ile yan kullanım arasındaki sınırı doğrudan aydınlatır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda adet görme yalnızca yan kullanımdır ve ana eksen doğumdur; komşu dalın çekirdeği ise dönemsel rahim kanamasıdır.","focus_only":"Odak dalın çekirdeği doğum, doğum sonrası kadın ve yeni doğan çocuktur.","gloss":"adet kanaması","neighbor_only":"Komşu dal, rahim kanının belirli dönemlerde çıkmasını, bunun zamanını ve yerini kapsar.","neighbor_ref":"root_000379/B001","relation_type":"near_neighbor","shared_zone":"İki dal, kadından kan gelmesi bağlamında sınırlı olarak kesişir."}],"source_phrase_ar":"الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)","source_summary":"Toplu kaynak kaydı doğum, doğum yapan kadın ve yeni doğanı ortak eksende birleştirir; ayrıca adet görme yönünde sınırlı bir kullanım farkı taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفاس ولادة المرأة، والنفساء، والمنفوس بمعنى المولود، واستعماله في الحيض حيث نص المصدر عليه.","what_is_not_ar":"ليس هو كل دم ولا كل خروج نفس، بل باب الولادة والحيض المنصوص عليه."},"support_links":[]},{"boundary":"Dal yalnızca içme bağlamındaki sayılabilir içim bölümleridir; genel solunum ya da her küçük sıvı miktarı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"soluk aralı içim ve bir içimlik yudum","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İçme eylemi soluklanma aralarıyla ayrılan sayılabilir bölümlere ayrılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek bölüm, bir yudum ya da bir solukta alınan içimlik paydır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçeceğin aralarda soluklanılarak bölümler hâlinde içilmesi ve her bölümün sayılması için uygundur.","boundary_detail":"Dal yalnızca içme bağlamındaki sayılabilir içim bölümleridir; genel solunum ya da her küçük sıvı miktarı değildir.","branch_image_ar":"نفس الشرب وجرعته","concept_gloss":"soluk aralı içim ve bir içimlik yudum","contextual_glosses":[{"applicability":"İçme eylemi üç ayrı bölümde ve aralarda soluklanarak yapıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçmenin üç sayılabilir bölüme ayrılmasını korur."},"facet_ids":["F001"],"text":"üç solukta içmek","usage_role":"contextual"}],"definition":"Bir içeceği, aralarda soluklanarak bir veya birkaç ayrı içim bölümünde içmektir. Her bölüm tek bir yudumlama ya da içimlik pay olarak sayılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İçme eylemi soluklanma aralarıyla ayrılan sayılabilir bölümlere ayrılır."},{"facet_id":"F002","role":"specialization","statement":"Tek bölüm, bir yudum ya da bir solukta alınan içimlik paydır."}],"identity_rationale":"Kaynak ifadesi, içmeyi soluk aralarıyla bölünen bir eylem olarak ve bu eylemin tek bir içimlik bölümünü açıkça anlatır. Bir, iki ya da üç olarak sayılan şey içmenin bu bölümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bir solukta alınan yudum ya da içim"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"üç soluk arasıyla içme"}],"lexicalization_note":"Çıplak biçim bir içimlik bölümü, kalıp ise içmenin üç soluk arasıyla yapılmasını anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yudum komşusu, miktar ile soluk aralığına göre bölünmüş içim arasındaki farkı en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odaktaki birim soluk arasıyla belirlenen içim bölümüdür; komşudaki birim ise boğazdan geçirilen sıvı miktarı ve yutma hareketidir.","focus_only":"Odak dal, içmeyi soluklanma aralarıyla bölüp her bölümü sayar.","gloss":"yudum ve yutma","neighbor_only":"Komşu dal, boğazdan geçirilen küçük miktarı, ağız dolusunu ve istemeden art arda yutmayı kapsar.","neighbor_ref":"root_000237/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir içeceğin küçük ve tek seferlik alınışını kapsar."}],"source_phrase_ar":"كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)","source_summary":"Kaynaklar, içme eyleminin bir, iki veya üç soluk aralığına bölünmesini ve her bölümün bir içimlik pay sayılmasını ortaklaştırır.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه الشرب بنفس أو أنفاس، والنفس بمعنى الجرعة أو المستراح في الشرب.","what_is_not_ar":"ليس هو مجرد التنفس خارج الشرب ولا قدر الدباغ وإن وافقه في صغر المقدار."},"support_links":[]},{"boundary":"Dal, deri işleme maddesinin ölçüsüdür; işlenmiş derinin kendisi, belirli bir bitki ya da içecek yudumu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"bir deri işlemeye yetecek sepi maddesi payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir derinin tek seferlik işlenmesine yetecek küçük sepi maddesi miktarıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşleme maddesi bir veya iki küçük pay hâlinde ölçülüp verilebilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deri işlemede kullanılan maddenin tek uygulamalık küçük miktarı için uygundur.","boundary_detail":"Dal, deri işleme maddesinin ölçüsüdür; işlenmiş derinin kendisi, belirli bir bitki ya da içecek yudumu değildir.","branch_image_ar":"قدر دبغة يسيرة","concept_gloss":"bir deri işlemeye yetecek sepi maddesi payı","contextual_glosses":[{"applicability":"Malzeme iki küçük uygulama payı olarak istendiğinde doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Maddenin iki ayrı işleme payı olarak sayılmasını korur."},"facet_ids":["F002"],"text":"iki işlemelik sepi maddesi","usage_role":"contextual"}],"definition":"Bir deriyi bir kez sepelemek için gereken küçük işleme maddesi miktarıdır. Bu miktar bir ya da iki pay olarak sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir derinin tek seferlik işlenmesine yetecek küçük sepi maddesi miktarıdır."},{"facet_id":"F002","role":"specialization","statement":"İşleme maddesi bir veya iki küçük pay hâlinde ölçülüp verilebilir."}],"identity_rationale":"Kaynak ifadesi, bir deriyi bir kez işlemek için gereken küçük sepi maddesi miktarını ve bunun bir ya da iki pay olarak sayılmasını açıkça bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"deriyi bir kez işlemeye yetecek sepi maddesi"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir işlemelik sepi maddesi payı"}],"lexicalization_note":"Çıplak biçim küçük sepi maddesi payını, kalıp kullanım ise bunun bir veya iki pay olarak verilmesini anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; belirli işleme bitkisini anlatan komşu, malzeme türü ile malzeme miktarı ayrımını açıkça gösterir.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak bir ölçü birimidir; komşu ise belirli bir bitkiyi ve ondan türeyen deri işleme kullanımlarını adlandırır.","focus_only":"Odak dal, deri işlemede kullanılan maddenin tek uygulamalık miktarını bildirir.","gloss":"deri işlemede kullanılan ağaç","neighbor_only":"Komşu dal, belirli bir ağacı, onunla işlenmiş deriyi ve ağacın hayvana etkisini kapsar.","neighbor_ref":"root_001079/B003","relation_type":"same_field","shared_zone":"İki dal da deri işleme sürecinde kullanılan maddeler alanındadır."}],"source_phrase_ar":"في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)","source_summary":"Kaynaklar, anlamı derinin bir kez işlenmesine yetecek küçük sepi maddesi payı olarak ortak biçimde verir.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه النفس أو النفسين من الدباغ، أي مقدار يسير يدبغ به الجلد مرة أو مرتين.","what_is_not_ar":"ليس هو جرعة الشراب ولا النفاسة في المال."},"support_links":[]},{"boundary":"Dal, su ve içeceğin yaşamı sürdürme ya da doyurucu olma niteliğidir; sayılan tek yudum veya canın kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"yaşamı sürdüren, bol ve doyurucu su","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su, yaşamın sürmesini sağlayan temel içecek olarak adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçecek, bol ve susuzluğu giderici olduğunda doyurucu bir genişlik taşır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Karşıt kalıp, içecekte doyurucu ve rahat içimli niteliğin bulunmadığını bildirir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su ya da içecek, yaşamı destekleyen ve susuzluğu gideren yeterlilik bakımından anlatıldığında uygundur.","boundary_detail":"Dal, su ve içeceğin yaşamı sürdürme ya da doyurucu olma niteliğidir; sayılan tek yudum veya canın kendisi değildir.","branch_image_ar":"ماء تقام به النفس","concept_gloss":"yaşamı sürdüren, bol ve doyurucu su","contextual_glosses":[{"applicability":"İçeceğin karşıt kalıpla, rahat içim ve doyuruculuktan yoksun olduğu anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Doyurucu ve rahat içimli niteliğin yokluğunu korur."},"facet_ids":["F003"],"text":"içimi güç ve doyurmayan içecek","usage_role":"contextual"}],"definition":"Yaşamı ayakta tutan su ve içene genişlik sağlayıp susuzluğu gideren doyurucu içecektir. Karşıt kullanım, içeceğin bu rahat içimli ve doyurucu niteliği taşımadığını belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su, yaşamın sürmesini sağlayan temel içecek olarak adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"İçecek, bol ve susuzluğu giderici olduğunda doyurucu bir genişlik taşır."},{"facet_id":"F003","role":"source_variant","statement":"Karşıt kalıp, içecekte doyurucu ve rahat içimli niteliğin bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi suyu yaşamı ayakta tutan madde olarak adlandırır ve içeceğin bol, doyurucu ve susuzluğu giderici oluşunu aynı bağıntıyla açıklar. Karşıt kalıp bu niteliğin bulunmadığını bildirir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yaşamı ayakta tutan su"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bol ve susuzluğu gideren içecek"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"tadı kötü, bayat ve içimi güç içecek"}],"lexicalization_note":"Çıplak biçim suyu, iki karşıt kalıp ise içecekte doyurucu genişliğin bulunmasını ya da bulunmamasını anlatır.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; susuzluğu giderme komşusu, içeceğin niteliği ile içenin ulaştığı sonuç arasındaki sınırı belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak, suyun ya da içeceğin yeterli ve doyurucu niteliğidir; komşu ise içenin susuzluktan kurtulması sonucunu ve bunun mecazlı uzantısını anlatır.","focus_only":"Odak dal suyu ve içeceği, doyurucu niteliğin taşıyıcısı olarak adlandırır.","gloss":"susuzluğu giderme","neighbor_only":"Komşu dal susuzluğu giderme eylemini ve haber ya da görüşle iç rahatlığı bulma uzantısını kapsar.","neighbor_ref":"root_001544/B002","relation_type":"near_synonym","shared_zone":"İki dal da su içmenin susuzluğu giderip rahatlık sağlaması alanında örtüşür."}],"source_phrase_ar":"يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)","source_summary":"Kaynaklar suyu yaşamın dayanağı sayar; içecekte bolluk ve susuzluğu giderme niteliğini olumlu ve olumsuz kalıplarla karşılaştırır.","sources":["MQ","TA"],"what_is_ar":"يدخل فيه تسمية الماء نفسا، والشراب ذو النفس إذا كان فيه سعة وري، ونقيضه الشراب غير ذي نفس.","what_is_not_ar":"ليس هو النفس الروح نفسها ولا جرعة الشرب المعدودة فقط."},"support_links":[]},{"boundary":"Dal, yayılma ve açılmayı belirli öznelere bağlayan kalıplardan oluşur; genel bir çıplak anlam ya da canlı solunumu değildir.","branch_kind":"collocation","branch_ref":"root_001533/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"kalıba bağlı yarılıp açılma ve genişleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yay için kullanıldığında yarılma ya da çatlama olayını bildirir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sabah ve gündüz için kullanıldığında aydınlığın açılmasını, sürenin uzayıp genişlemesini bildirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Irmak ya da dalga için kullanıldığında suyun artıp dışarı doğru yayılmasını bildirir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca verilen yay, sabah, gündüz ve su kalıplarının ortak görüntüsünü topluca anlatmak için uygundur.","boundary_detail":"Dal, yayılma ve açılmayı belirli öznelere bağlayan kalıplardan oluşur; genel bir çıplak anlam ya da canlı solunumu değildir.","branch_image_ar":"انفتاح الصبح والشيء كالنفس","concept_gloss":"kalıba bağlı yarılıp açılma ve genişleme","contextual_glosses":[{"applicability":"Karanlığın yarılıp sabah aydınlığının belirmesi kalıbında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sabah aydınlığının yarılıp açılarak belirmesini korur."},"facet_ids":["F002"],"text":"sabahın sökmesi","usage_role":"contextual"},{"applicability":"Irmak suyunun yükselip çevreye doğru yayılması kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Su miktarındaki artışı ve dışa doğru yayılmayı korur."},"facet_ids":["F003"],"text":"suyun artıp yayılması","usage_role":"contextual"}],"definition":"Yalnızca belirli kalıplarda, yayın yarılması; sabahın açılması; gündüzün uzayıp genişlemesi veya ırmak suyunun artıp yayılmasıdır. Ortak görüntü, kapalı ya da dar bir durumdan açılma ve genişlemeye geçiştir.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Yay için kullanıldığında yarılma ya da çatlama olayını bildirir."},{"facet_id":"F002","role":"core","statement":"Sabah ve gündüz için kullanıldığında aydınlığın açılmasını, sürenin uzayıp genişlemesini bildirir."},{"facet_id":"F003","role":"extension","statement":"Irmak ya da dalga için kullanıldığında suyun artıp dışarı doğru yayılmasını bildirir."}],"identity_rationale":"Kaynak ifadesindeki kullanımlar, belirli öznelerin yarılması, açılması, uzayıp genişlemesi veya suyu artarak yayılması ortak görüntüsünde birleşir. Bu anlam yalnızca verilen kalıplarda geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"yay çatladı ya da yarıldı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sabah söktü, aydınlık yayıldı"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"gündüz uzayıp genişledi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ırmağın suyu artıp yayıldı"}],"lexicalization_note":"Anlam yalnızca yay, sabah, gündüz ve ırmakla kurulan kalıplara bağlıdır; çıplak kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sabahın açılması ortaklığını ve kalıpların farklı yönlere uzanmasını en açık gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak sabah görüntüsüne rağmen odak dalın öteki kalıpları yay, gündüz ve suya uzanır; komşu ise bulut açıklığı ve yağış alanındaki boşluk yönünde genişler.","focus_only":"Odak dal, sabah yanında yayın çatlamasını, gündüzün genişlemesini ve suyun artmasını da kapsayan ayrı kalıplar taşır.","gloss":"sabahın ve bulutun yarılıp açılması","neighbor_only":"Komşu dal, güneş ya da ayın bulut aralığından çıkmasını ve çevresi yağmurluyken kuru kalan yeri de kapsar.","neighbor_ref":"root_001126/B003","relation_type":"near_neighbor","shared_zone":"İki dal, sabah aydınlığının karanlığı yararak ortaya çıkması görüntüsünde kesişir."}],"source_phrase_ar":"تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)","source_summary":"Toplu kaynak kaydı, yaydaki çatlama, sabahtaki açılma, gündüzdeki genişleme ve sudaki artışı kalıba bağlı bir açılma-yayılma görüntüsünde birleştirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه تنفس الصبح والنهار إذا تبلج أو امتد، وتنفس القوس إذا انشقت، وزيادة الماء أو الموج حين يخرجان أو ينتشران.","what_is_not_ar":"ليس هو التنفس الحيواني ولا مجرد السعة الزمنية إلا إذا كان اللفظ عن الانفتاح أو الامتداد."},"support_links":[]},{"boundary":"Dal dışarıdaki değerli şeye yönelen istek ve çekişmeyle ilgilidir; kişinin kendi onuru ya da yücelik duygusu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"değerli ve uğrunda yarışılan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yüksek değer ve önem taşıdığı için insanların arzuladığı şeydir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsanlar bu şeyi elde etmek ya da üstünlere benzemek için birbirleriyle yarışabilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Değerli şeyi başkasından esirgeme veya ona sahip olanı kıskanma biçiminde bir sahiplenme doğabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin yüksek değeri insanların onu istemesine ve elde etmek için yarışmasına yol açtığında uygundur.","boundary_detail":"Dal dışarıdaki değerli şeye yönelen istek ve çekişmeyle ilgilidir; kişinin kendi onuru ya da yücelik duygusu değildir.","branch_image_ar":"شيء نفيس تتنافس فيه النفوس","concept_gloss":"değerli ve uğrunda yarışılan şey","contextual_glosses":[{"applicability":"Değerli görülen şeyin başkasına geçmesi istenmediğinde veya sahibi kıskanıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Değerli şeye yönelik kıskanç sahiplenmeyi ve esirgemeyi korur."},"facet_ids":["F003"],"text":"kıskanıp başkasından esirgemek","usage_role":"contextual"}],"definition":"İnsanların değer ve önem yüklediği, elde etmek ya da benzemek için uğrunda yarıştığı şeydir; bu yönelim, şeyin başkasına geçmesini istemeyerek esirgeme veya kıskanma biçimini de alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yüksek değer ve önem taşıdığı için insanların arzuladığı şeydir."},{"facet_id":"F002","role":"extension","statement":"İnsanlar bu şeyi elde etmek ya da üstünlere benzemek için birbirleriyle yarışabilir."},{"facet_id":"F003","role":"associated_use","statement":"Değerli şeyi başkasından esirgeme veya ona sahip olanı kıskanma biçiminde bir sahiplenme doğabilir."}],"identity_rationale":"Kaynak ifadesi değerli şeyi, ona yönelen isteği, uğrunda yarışmayı ve başkasına geçmesini istemeyerek esirgeme ya da kıskanmayı tek bir değer-yönelim zincirinde açıkça birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"değerli, önemli ve arzulanan"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bir şeyi elde etme ya da üstünlere benzeme yarışı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"başkasına vermeye kıyamayıp esirgemek"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"sahip olduğu şey yüzünden onu kıskanmak"}],"lexicalization_note":"Biçimler değerli şeyi ve yarışmayı, kalıplar ise o şeyi başkasından esirgeme veya kıskanmayı anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; değerli nesne ortaklığı yanında yarışma sınırını görünür kılan en yararlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değerden doğan kişiler arası yarışma ve kıskançlığı kurar; komşu dal ise değerli nesne ile sahibinin ona bağlılığı üzerinde durur.","focus_only":"Odak dal, yüksek değerin yanında o şey uğrundaki yarışmayı ve kıskanç esirgemeyi de kapsar.","gloss":"bağlanılan değerli şey","neighbor_only":"Komşu dal, sahibinin bağlandığı ve koruduğu malı ya da başka değerli nesneleri adlandırmaya ağırlık verir.","neighbor_ref":"root_001039/B007","relation_type":"near_synonym","shared_zone":"İki dal da değerli görülen ve sahibinin kolayca vazgeçmediği şeyi kapsar."}],"source_phrase_ar":"شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)","source_summary":"Kaynaklar yüksek değer, ona duyulan istek, yarışma ve değerli şeyi başkasından esirgeme ya da kıskanma ilişkilerini tek bir toplu iddiada birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفيس والنفاسة والمنفس، والرغبة والمنافسة في الشيء، والضن أو الحسد به إذا كان لقيمته ورغبة النفس فيه.","what_is_not_ar":"ليس هو عزة النفس والهمة في صاحبها إلا إذا كان الكلام عن المال أو الشيء المرغوب فيه."},"support_links":[]},{"boundary":"Dal bedensel yaşamı sağlayan can ve canlı bireydir; düşünce, özdeşlik vurgusu, kan ya da soluk değildir.","branch_kind":"bare","branch_ref":"root_001533/B011","candidate_links":[{"candidate_id":"cand_273e88bd4ea4aeac7c40","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"bedene yaşam veren can","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bedene yaşam veren ve bedenden ayrılması ölüm sayılan candır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu canı taşıyan her insan ayrı bir canlı birey olarak adlandırılabilir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Canlılığı sağlayan ve bedenden ayrılması ölüm anlamına gelen yaşam taşıyıcısı için uygundur.","boundary_detail":"Dal bedensel yaşamı sağlayan can ve canlı bireydir; düşünce, özdeşlik vurgusu, kan ya da soluk değildir.","branch_image_ar":"النفس التي بها الحياة","concept_gloss":"bedene yaşam veren can","contextual_glosses":[{"applicability":"İnsanların tek tek canlı varlıklar olarak sayıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her insanın ayrı bir canlı birey olarak sayılmasını korur."},"facet_ids":["F002"],"text":"canlı birey","usage_role":"contextual"}],"definition":"Bedeni canlı tutan ve ayrılmasıyla ölümün gerçekleştiği candır. Bu yaşam taşıyıcısı bakımından her insan ayrı bir canlı birey olarak da sayılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bedene yaşam veren ve bedenden ayrılması ölüm sayılan candır."},{"facet_id":"F002","role":"extension","statement":"Bu canı taşıyan her insan ayrı bir canlı birey olarak adlandırılabilir."}],"identity_rationale":"Kaynak ifadesi bedeni canlı tutan ilkeyi, onun bedenden çıkmasıyla ölümü ve her insanın canlı bir birey olarak bu adla sayılabilmesini doğrudan açıklar.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"bedene yaşam veren can"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"insan ya da canlı birey"}],"lexicalization_note":"Çıplak dal, bedene yaşam veren canı ve bununla canlı sayılan bireyi kapsar; kalıp anlamı içe aktarılmaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; yalnızca yaşam veren can anlamında tam sınır eşleşmesi gösteren eş anlamlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Verilen kartlarda çekirdek, yaşam işlevi ve bedenden ayrılma sınırı bütünüyle örtüşür; anlamlı bir ayrım yoktur.","focus_only":null,"gloss":"bedene yaşam veren can","neighbor_only":null,"neighbor_ref":"root_000609/B001","relation_type":"synonym","shared_zone":"İki dal da bedeni canlı tutan canı ve onun bedenden çıkmasını aynı sınırlarla anlatır."}],"source_phrase_ar":"النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)","source_summary":"Kaynaklar, bedensel yaşamı sağlayan can, bu canın çıkmasıyla ölüm ve insanın canlı birey olarak sayılması üzerinde birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفس بمعنى الروح والحياة، وكل إنسان نفس، وخروج النفس عند الموت، والنفس الحية التي بها حياة الجسد.","what_is_not_ar":"ليس هو ذات الشيء للتوكيد ولا ما في النفس من قصد أو غيب فقط."},"support_links":["sup_b6eaa5b9e6cdd98e303b"]},{"boundary":"Dal yalnızca özdeşlik ve pekiştirme kalıplarındadır; canlılık ilkesi, zararlı bakış ya da iç düşünce değildir.","branch_kind":"collocation","branch_ref":"root_001533/B012","candidate_links":[{"candidate_id":"cand_82b0d0d8b27accd52efc","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"şeyin kendisi ve bütün öz varlığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin bütün gerçeği ve öz varlığıyla kendisini pekiştirerek gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin başkası aracılığıyla değil, bizzat kendisinin bulunmasını belirtir."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir nesne ya da kişinin başkası değil tam olarak kendisi olduğu vurgulandığında uygundur.","boundary_detail":"Dal yalnızca özdeşlik ve pekiştirme kalıplarındadır; canlılık ilkesi, zararlı bakış ya da iç düşünce değildir.","branch_image_ar":"عين الشيء وذاته","concept_gloss":"şeyin kendisi ve bütün öz varlığı","contextual_glosses":[{"applicability":"Bir kişinin aracı kullanmadan doğrudan bulunduğu ya da eylemi yaptığı bağlamda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin doğrudan ve aracısız bulunması vurgusunu korur."},"facet_ids":["F002"],"text":"bizzat kendisi","usage_role":"contextual"}],"definition":"Bir şeyin başkası ya da bir parçası değil, bütün gerçeği ve öz varlığıyla kendisi olduğunu vurgulamaktır. Kişi için kullanıldığında onun aracısız biçimde bizzat bulunmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin bütün gerçeği ve öz varlığıyla kendisini pekiştirerek gösterir."},{"facet_id":"F002","role":"specialization","statement":"Kişinin başkası aracılığıyla değil, bizzat kendisinin bulunmasını belirtir."}],"identity_rationale":"Kaynak ifadesi bir şeyin aynısını, bütün varlığını, gerçeğini ve özünü vurgulayan kullanımı açıkça verir. Kişinin aracısız olarak bizzat bulunması da aynı özdeşlik kalıbına bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"şeyin tam kendisi ve gerçeği"},{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"başkası aracılığıyla değil, bizzat kendisi"}],"lexicalization_note":"Anlam, bir şeyin kendisini ya da bir kişinin bizzat bulunmasını bildiren kalıplarla sınırlıdır; çıplak anlama genellenmez.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; özdeşlik ortaklığını ve pekiştirme-seçip belirleme farkını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıba bağlı özdeşlik pekiştirmesidir; komşu dal özdeşliğe ek olarak bir öğeyi topluluktan ayırıp belirleme işlevi taşır.","focus_only":"Odak dal, bütün öz varlığı ve bizzat bulunmayı pekiştiren kalıpları kapsar.","gloss":"şeyin aynısı ve kendisi","neighbor_only":"Komşu dal, bir öğeyi topluluğun geri kalanından özellikle seçip belirtme kullanımını da kapsar.","neighbor_ref":"root_001069/B013","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyin başka bir şey değil, tam olarak kendisi olduğunu bildirir."}],"source_phrase_ar":"كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)","source_summary":"Kaynaklar, şeyin kendisini bütün gerçeği ve özüyle vurgulama ile kişinin bizzat bulunması kullanımında birleşir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه النفس بمعنى عين الشيء، ذاته، حقيقته، جملته، كنهه وجوهره، واستعمالها للتوكيد.","what_is_not_ar":"ليس هو الروح الحية ولا العين المؤذية ولا المعنى الباطن من القصد إلا بقرينة."},"support_links":["sup_76a7755cb4b4fa21581c"]},{"boundary":"Dal iç düşünce ve ayırt etme gücüyle sınırlıdır; kişinin bütünü, bedensel canı veya yalnızca dışa vurulmuş söz değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"iç düşünce, niyet ve ayırt etme gücü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin içinde tuttuğu düşünce, niyet ya da kendine özgü bilgidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğru ayrımlar yapmayı sağlayan zihinsel yeti de bu içsel idrak alanında adlandırılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin dışa vurmadığı içeriği veya ayrım yapmasını sağlayan zihinsel yetisi anlatıldığında uygundur.","boundary_detail":"Dal iç düşünce ve ayırt etme gücüyle sınırlıdır; kişinin bütünü, bedensel canı veya yalnızca dışa vurulmuş söz değildir.","branch_image_ar":"ما في النفس من عقل وروع","concept_gloss":"iç düşünce, niyet ve ayırt etme gücü","contextual_glosses":[{"applicability":"Kişinin henüz söylemediği bir şeyi düşünmesi ya da yapmaya niyetlenmesi bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Düşüncenin içte bulunmasını ve henüz dışa vurulmamasını korur."},"facet_ids":["F001"],"text":"aklından geçirmek","usage_role":"contextual"}],"definition":"Kişinin içinde bulunan, henüz dışa vurulmamış düşünce, niyet veya bilgidir. Aynı alan, kişinin ayırt etmesini sağlayan zihinsel gücü de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin içinde tuttuğu düşünce, niyet ya da kendine özgü bilgidir."},{"facet_id":"F002","role":"extension","statement":"Doğru ayrımlar yapmayı sağlayan zihinsel yeti de bu içsel idrak alanında adlandırılır."}],"identity_rationale":"Kaynak ifadesi kişinin içinde taşıdığı düşünceyi, niyeti ve bilgiyi; ayrıca ayırt etmeyi sağlayan zihinsel yetiyi açıkça aynı içsel idrak alanında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"onun içinden geçen düşünce ya da niyet"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"ayırt etmeyi sağlayan zihinsel güç"}],"lexicalization_note":"Kalıp kullanım içteki düşünce ve niyeti, ayrı birim ise ayırt etmeyi sağlayan zihinsel gücü anlatır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; söylenmemiş düşünce komşusu, içsel alanın söz tasarısından daha geniş olduğunu en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal içsel idrakin daha geniş alanıdır; komşu dal özellikle dile getirilmeden önce zihinde tasarlanan söze yönelir.","focus_only":"Odak dal, dışa vurulmamış düşüncenin yanında niyet, iç bilgi ve ayırt etme yetisini de kapsar.","gloss":"söylenmemiş iç düşünce","neighbor_only":"Komşu dal, sözle ortaya konmadan önce zihinde tasarlanan söyleyiş içeriğine odaklanır.","neighbor_ref":"root_001272/B012","relation_type":"near_synonym","shared_zone":"İki dal da kişinin zihninde bulunan fakat henüz sözle açıklanmamış içeriği kapsar."}],"source_phrase_ar":"نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)","source_summary":"Kaynaklar, kişinin içindeki düşünce ve bilgiyi ayırt etme yetisiyle birlikte içsel idrak alanında birleştirir.","sources":["TA","MU"],"what_is_ar":"يدخل فيه ما في نفس المرء من روع وقصد، ونفس العقل والتمييز، وما يعبر عنه بالغيب أو العندية في سياق ما في النفس.","what_is_not_ar":"ليس هو الذات المؤكدة ولا الروح التي بها الحياة إلا إذا دل السياق على الإدراك الباطن."},"support_links":[]},{"boundary":"Karakter gücü ile yüksek özdeğer aynı dalda iki bağlı görünüm olarak ayrılır; dışarıdaki değerli mal ve onun için yarışma kapsama girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B014","candidate_links":[{"candidate_id":"cand_c7c66cce6cec5fa0028f","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"sağlam, cömert ve onurlu yaradılış","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin sağlam karakterli, dayanıklı ve cömert oluşunu bildirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin büyüklük duygusu, gururu, onuru, yüksek amacı ve kendine saygısı da ayrı görünüm olarak aktarılır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin dayanıklılığı, cömertliği ve kendine verdiği yüksek değer birlikte anlatıldığında uygundur.","boundary_detail":"Karakter gücü ile yüksek özdeğer aynı dalda iki bağlı görünüm olarak ayrılır; dışarıdaki değerli mal ve onun için yarışma kapsama girmez.","branch_image_ar":"قوة النفس وخلقها","concept_gloss":"sağlam, cömert ve onurlu yaradılış","contextual_glosses":[{"applicability":"Kişinin kendi değerini koruması, yüksek hedef taşıması veya gurur göstermesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Onuru, yüksek amacı ve kendine değer verme yönünü korur."},"facet_ids":["F002"],"text":"yüksek amaç ve kendine saygı","usage_role":"contextual"}],"definition":"Kişide görülen sağlam karakter, dayanıklılık ve cömertliktir; buna bağlı ikinci görünüm, kişinin kendi değerini yüksek tutması, onur, yüksek amaç ve kimi bağlamlarda gurur göstermesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin sağlam karakterli, dayanıklı ve cömert oluşunu bildirir."},{"facet_id":"F002","role":"source_variant","statement":"Kişinin büyüklük duygusu, gururu, onuru, yüksek amacı ve kendine saygısı da ayrı görünüm olarak aktarılır."}],"identity_rationale":"Kaynak ifadesi bir yanda karakter, dayanıklılık ve cömertliği; öte yanda büyüklük duygusu, gurur, onur, yüksek amaç ve kendine saygıyı aktarır. Dal korunabilir, ancak bu iki görünüm tek ve ayrışmaz bir huy gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_038","rendering_kind":"ordinary","target_gloss":"sağlam karakterli, dayanıklı ve cömert adam"},{"lexical_unit_id":"lu_039","rendering_kind":"ordinary","target_gloss":"büyüklük duygusu, onur, yüksek amaç ve kendine saygı"}],"lexicalization_note":"Kişiyle kurulan kalıp karakter, dayanıklılık ve cömertliği; çıplak biçim büyüklük, onur ve yüksek amacı bildirir.","neighbor_coverage_note":"Bütün aday kartlar karşılaştırıldı; cömertlik ortaklığı ile karakter gücü ve eylem hevesi ayrımını gösteren komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak kişinin yerleşik karakter gücü ve özdeğerini anlatır; komşu ise iyilik yapma anındaki gönüllü canlılık ve atılganlığı öne çıkarır.","focus_only":"Odak dal, dayanıklılık ve cömertliğin yanında gurur, onur ve yüksek amacı da kapsar.","gloss":"iyiliğe heves ve eli açıklık","neighbor_only":"Komşu dal, iyilik yapmaya hevesle yönelme, canlılık ve gönül genişliği üzerinde durur.","neighbor_ref":"root_000609/B010","relation_type":"near_synonym","shared_zone":"İki dal, cömert ve iyi davranışa yatkın kişi görünümünde örtüşür."}],"source_phrase_ar":"رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)","source_summary":"Toplu kaynak kaydı, sağlam ve cömert karakter görünümünü kişinin büyüklük, onur, yüksek amaç ve kendine saygı duygularıyla yan yana getirir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه النفس بمعنى الخلق والجلادة والسخاء، وبمعنى العظمة والكبر والعزة والهمة والأنفة.","what_is_not_ar":"ليس هو النفيس من المال ولا المنافسة على شيء خارج النفس."},"support_links":["sup_91618802710111938c9a"]},{"boundary":"Dal ölçülebilir yer, boyut veya süre genişliğidir; belirli bir sıkıntıyı giderme ya da sabahın açılması değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001533/B015","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"uzaklık, genişlik ve zaman payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Mekânda iki sınır arasındaki uzaklık, açıklık veya boyutsal genişliktir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Zamanda ek süre, işte ise rahat davranmaya elveren hareket alanıdır."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Mekânsal aralık, nesne boyutu, ek süre veya bir işteki hareket alanı anlatıldığında uygundur.","boundary_detail":"Dal ölçülebilir yer, boyut veya süre genişliğidir; belirli bir sıkıntıyı giderme ya da sabahın açılması değildir.","branch_image_ar":"سعة ومسافة ومهلة","concept_gloss":"uzaklık, genişlik ve zaman payı","contextual_glosses":[{"applicability":"Bir işi yapmak için yeterli serbestlik ve ek zaman bulunduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşteki serbestliği ve ek süre payını birlikte korur."},"facet_ids":["F002"],"text":"rahat hareket edecek alan ve süre","usage_role":"contextual"}],"definition":"Yer bakımından uzaklık veya aralık, boyut bakımından uzunluk ve genişlik, zaman ya da iş bakımından ise ek süre ve hareket alanıdır. Bütün kullanımlarda sınırlar arasındaki payın büyümesi esastır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Mekânda iki sınır arasındaki uzaklık, açıklık veya boyutsal genişliktir."},{"facet_id":"F002","role":"extension","statement":"Zamanda ek süre, işte ise rahat davranmaya elveren hareket alanıdır."}],"identity_rationale":"Kaynak ifadesi mekânsal uzaklık ve genişliği, işte hareket alanı ve süre payını, ayrıca uzunluk ve zaman uzatımını aynı genişleme ölçüsü altında açıkça toplar.","lexical_glosses":[{"lexical_unit_id":"lu_040","rendering_kind":"ordinary","target_gloss":"işinde rahat hareket edecek genişlikte"},{"lexical_unit_id":"lu_041","rendering_kind":"ordinary","target_gloss":"ek süre ya da hareket alanı"},{"lexical_unit_id":"lu_042","rendering_kind":"ordinary","target_gloss":"daha uzak, daha uzun ya da daha geniş"}],"lexicalization_note":"Kalıp kullanım bir işteki hareket alanını, biçimler ise süre payı ile mekânsal ya da boyutsal genişliği anlatır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; uzunluk ve uzaklık ortaklığının yanında odaktaki süre ve hareket alanı ekini gösteren komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genişleyen payı yer, boyut ve süre arasında geneller; komşu dal belirli varlıkların uzun veya uzak oluşuna ve işin uzamasına yönelir.","focus_only":"Odak dal, uzaklık ve uzunluğun yanında ek süreyi ve bir işteki rahat hareket alanını kapsar.","gloss":"uzunluk ve uzaklığa yayılma","neighbor_only":"Komşu dal, uzun insanı, uçsuz bucaksız yeri ve uzun süren işleri özel kullanımlar olarak kapsar.","neighbor_ref":"root_001402/B009","relation_type":"near_synonym","shared_zone":"İki dal mekânsal uzaklık, uzunluk ve bir işin sürmesi alanında örtüşür."}],"source_phrase_ar":"هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)","source_summary":"Kaynaklar uzaklık, açıklık, uzunluk, ek süre ve işte hareket alanını sınırlar arasındaki payın genişlemesi altında birleştirir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه السعة في الأمر، والفسحة، والمهلة، وطول الأجل أو النهار أو الكتاب، وبعد المنزل واتساع ما بين الفريقين.","what_is_not_ar":"ليس هو تفريج الكربة المخصوص ولا تنفس الصبح من حيث الانفلاق إلا إن كان المراد مطلق الامتداد."},"support_links":[]},{"boundary":"Adlandırma eski bahis oyunundaki belirli oka aittir; temel sıra beşinci, kayıtlı karşı görüş dördüncüdür.","branch_kind":"bare","branch_ref":"root_001533/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","surface_ar":"نَّفْسُ"}],"gloss":"eski bahis oyunundaki beşinci pay oku","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eski bahis oyunundaki beşinci pay oku olarak ve beş payla tanımlanır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı toplu kaynak kaydında okun dördüncü sırada olduğu yönünde karşı bir aktarım bulunur."}}],"root_ar":"ن ف س","root_id":"root_001533","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli oyun okunun baskın aktarımdaki sırası ve pay değeri kastedildiğinde uygundur.","boundary_detail":"Adlandırma eski bahis oyunundaki belirli oka aittir; temel sıra beşinci, kayıtlı karşı görüş dördüncüdür.","branch_image_ar":"النافس سهم الميسر الخامس","concept_gloss":"eski bahis oyunundaki beşinci pay oku","contextual_glosses":[{"applicability":"Sıra konusundaki karşı aktarım özellikle belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli oyun okunu ve dördüncü sıra karşı aktarımını korur."},"facet_ids":["F002"],"text":"dördüncü sayıldığı da aktarılan oyun oku","usage_role":"explanatory"}],"definition":"Eski bir bahis oyununda kullanılan, çoğunluk aktarımına göre beşinci sıradaki ve beş pay taşıyan oktur. Başka bir aktarım onu dördüncü sıraya koyar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eski bahis oyunundaki beşinci pay oku olarak ve beş payla tanımlanır."},{"facet_id":"F002","role":"source_variant","statement":"Aynı toplu kaynak kaydında okun dördüncü sırada olduğu yönünde karşı bir aktarım bulunur."}],"identity_rationale":"Kaynak ifadesinin baskın bildirimi, belirli bahis okunun beşinci sırada olduğu ve beş pay taşıdığı yönündedir. Aynı toplu iddiada dördüncü sıra biçiminde bir aktarım da bulunduğu için sıra tartışmasız gösterilemez.","lexical_glosses":[{"lexical_unit_id":"lu_043","rendering_kind":"ordinary","target_gloss":"eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok"}],"lexicalization_note":"Çıplak biçim yalnızca eski bahis oyunundaki belirli pay okunu adlandırır; kişi ya da değer yarışması anlamı taşımaz.","neighbor_coverage_note":"Bütün aday kartlar değerlendirildi; genel oyun oku komşusu, özel sıra ve pay değerinin dalı nasıl daralttığını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıra ve pay değeriyle belirlenen özel oktur; komşu dal ise herhangi bir oyun okunu veya işlenmemiş ok gövdesini anlatır.","focus_only":"Odak dal, belirli sıraya ve beş pay değerine sahip tek bir oyun okunu adlandırır.","gloss":"oyun oku ve çıplak ok gövdesi","neighbor_only":"Komşu dal, henüz uç ve tüy takılmamış ok gövdesini ve oyun oklarının herhangi birini genel olarak kapsar.","neighbor_ref":"root_001203/B007","relation_type":"near_neighbor","shared_zone":"İki dal da eski bahis oyununda kullanılan ok biçimli araç alanında kesişir."}],"source_phrase_ar":"النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)","source_summary":"Toplu kaynak kaydı belirli oyun okunu çoğunlukla beşinci sıra ve beş payla tanımlar; bunun yanında dördüncü sıra aktarımını da korur.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه النافس اسما لقدح من قداح الميسر، خاصة الخامس على نص أكثر المصادر، مع التنبيه إلى قول الرابع في Sihah.","what_is_not_ar":"ليس هو العائن ولا المتنافس في القيمة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["89:27:1"],"branch_refs":[],"candidate_id":"cand_4a68b99a021fb6ebe2a4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:1:boundary-pivot","source_type":"word_analysis","support_ids":["sup_16fbbfbff44c510401b6","sup_5e0b9a135cdbd8f40268"],"title":"third-person judgment pivots to direct call","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:1","qac_refs":["89:27:1:1"],"status":"accepted"}},{"anchor_refs":["89:27:1"],"branch_refs":[],"candidate_id":"cand_c10cd64563480510cd45","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:1:extended-onset","source_type":"word_analysis","support_ids":["sup_5e0b9a135cdbd8f40268","sup_f339e4471d229072a507"],"title":"drawn-out opening call","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:1","qac_refs":["89:27:1:1"],"status":"accepted"}},{"anchor_refs":["89:27:1"],"branch_refs":[],"candidate_id":"cand_653d4f94fbeec21404bc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:1:recognition-summons","source_type":"word_analysis","support_ids":["sup_5e0b9a135cdbd8f40268","sup_ce3a3d634e21aa504ba2"],"title":"call range narrows to solemn recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:1","qac_refs":["89:27:1:1"],"status":"accepted"}},{"anchor_refs":["89:27:1"],"branch_refs":[],"candidate_id":"cand_0941b1d58fcb59755383","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:1:verbless-launch","source_type":"word_analysis","support_ids":["sup_5e0b9a135cdbd8f40268","sup_fcdc43df3f10dcab80c3"],"title":"summons opens before any predicate","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:1","qac_refs":["89:27:1:1"],"status":"accepted"}},{"anchor_refs":["89:27:1"],"branch_refs":[],"candidate_id":"cand_762b2832c5a63d3a39fe","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:1:vocative-scope","source_type":"word_analysis","support_ids":["sup_5e0b9a135cdbd8f40268","sup_e64d7820109d73d4caed"],"title":"vocative governs the full tranquil-self title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:1","qac_refs":["89:27:1:1"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_66ea6b6e7235188ff8dd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:2:canonical-feminine-form","source_type":"word_analysis","support_ids":["sup_94a1268eb90d1b170c35","sup_d3cfb038e4a344eed100"],"title":"canonical feminine marking is contrastive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:2","qac_refs":["89:27:1:2"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_ce36648db7ef82eb02de","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:2:expanded-entry","source_type":"word_analysis","support_ids":["sup_94a1268eb90d1b170c35","sup_b41cbc7d11682e6de8e5"],"title":"support form slows entry into the noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:2","qac_refs":["89:27:1:2"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_8c4955a4625e00611813","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:2:feminine-agreement","source_type":"word_analysis","support_ids":["sup_94a1268eb90d1b170c35","sup_e7451d77dd517398acee"],"title":"feminine support locks onto the self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:2","qac_refs":["89:27:1:2"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_9a56059fa82879b921fd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:2:placeholder-alert","source_type":"word_analysis","support_ids":["sup_85c2952f7ac07e6b56a0","sup_94a1268eb90d1b170c35"],"title":"placeholder and alert point forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:2","qac_refs":["89:27:1:2"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_2f1a5c8a334336fe011d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:2:positive-addressee-turn","source_type":"word_analysis","support_ids":["sup_94a1268eb90d1b170c35","sup_cf3e2b77210295fb3a79"],"title":"placeholder opens the way to the named addressee","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:2","qac_refs":["89:27:1:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_76d7c1e3f7c1c908a320","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:adjective-bound-title","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_6b382e1ee18027e6efd8"],"title":"definiteness and agreement bind the tranquil title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_e294aa02a6b5dbf30007","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:boundary-inner-identity","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_8ab7a56c4e9c4085ab59"],"title":"external restraint gives way to inner selfhood","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_bd6b495add4b8a943f23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:definite-appositional-addressee","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_a71fc8b080001b28eda3"],"title":"definite noun resolves the support form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_5e8bbc2fe46fa3069286","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:definite-singular-vocative-narrowing","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_983fa07c8c0f103a3df0"],"title":"common self-field becomes one addressed self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_1bba4480abb72da6d22f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:head-before-qualifier","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_f5d9c10c990467afc173"],"title":"selfhood lands before tranquility qualifies it","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_77064e905e1b89a73d80","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:intertextual-recognition","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_4c8ee76b3de2ac8283ed"],"title":"mortality and moral testing resolve into recognition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_c3ffc1f705401fcb2cf2","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:recipient-before-agency","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_804d776300024e2fb288"],"title":"recognized recipient becomes later mover","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_52d8eef89a1b74bfddc3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:value-without-striving","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_a6cc017f2013b3f42330"],"title":"preciousness is subordinated to settled identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_88435e05c2d6b0274fa7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:3:whole-living-self","source_type":"word_analysis","support_ids":["sup_05f2ab5c884307c80f05","sup_a8afcd6e57164c50e307"],"title":"selfhood carries breath and relief pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:3","qac_refs":["89:27:2:1","89:27:2:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_bfdebf54a6b91d7247b5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:adjectival-participle-title","source_type":"word_analysis","support_ids":["sup_95748bfc8731f3642d85","sup_f2043644d34a7d565e7b"],"title":"participial adjective identifies the self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_318b7624bf2ae9581b4a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:boundary-inward-settledness","source_type":"word_analysis","support_ids":["sup_3469699e88fb14555ff6","sup_f2043644d34a7d565e7b"],"title":"external binding becomes inward composure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_968168da3fe335479955","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:bridge-to-following-states","source_type":"word_analysis","support_ids":["sup_6ccdbc0adbb57061054e","sup_f2043644d34a7d565e7b"],"title":"tranquility prepares the states of 89:28","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_6d23d7f6b0141524affc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:distributional-prominence","source_type":"word_analysis","support_ids":["sup_67017ec921f769becc45","sup_f2043644d34a7d565e7b"],"title":"rare settled-state form is prominent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_6ac11faf16383f87f237","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:final-closure","source_type":"word_analysis","support_ids":["sup_91e74a7675305363d795","sup_f2043644d34a7d565e7b"],"title":"final adjective lands the ayah on tranquility","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_b312d08d311cf8c8ce12","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:hamzah-and-heavy-ending","source_type":"word_analysis","support_ids":["sup_36d27465e716988db2c5","sup_f2043644d34a7d565e7b"],"title":"marked sound shape gives settled weight","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_871344641b195fc4466f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:hearts-to-whole-self","source_type":"word_analysis","support_ids":["sup_a439bcd79e4196680edb","sup_f2043644d34a7d565e7b"],"title":"heart-rest echo expands to the whole self","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_061a04c0eb1b1452032a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:opposed-securities","source_type":"word_analysis","support_ids":["sup_6283c7ed70acab92290a","sup_f2043644d34a7d565e7b"],"title":"two kinds of firmness are inverted","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_87b2d0e1f270b9c70dc5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:participial-state-form","source_type":"word_analysis","support_ids":["sup_d6140edbe041dc508cf5","sup_f2043644d34a7d565e7b"],"title":"process is compressed into possessed state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_2e09ee8fb97fb70fb738","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:security-and-stilling-contour","source_type":"word_analysis","support_ids":["sup_809fac8cb0cebce26a88","sup_f2043644d34a7d565e7b"],"title":"security and lowering support settledness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:4"],"branch_refs":[],"candidate_id":"cand_0e72deeb4b1c5b720782","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"89:27:4:settled-reassurance-after-disturbance","source_type":"word_analysis","support_ids":["sup_7857705995572417940f","sup_f2043644d34a7d565e7b"],"title":"calm means achieved settled rest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"89:27:4","qac_refs":["89:27:3:1","89:27:3:2"],"status":"accepted"}},{"anchor_refs":["89:27:2"],"branch_refs":[],"candidate_id":"cand_9e20854314c74c8751f3","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001533"],"scope":"focus_ayah","source_local_id":"89:27:2:2","source_type":"qac_morpheme","support_ids":["sup_1b5f349f110abf416d33"],"title":"QAC root occurrence: ن ف س","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:27:3"],"branch_refs":[],"candidate_id":"cand_9eb9b22fd422d64b79af","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000948"],"scope":"focus_ayah","source_local_id":"89:27:3:2","source_type":"qac_morpheme","support_ids":["sup_5b378c829c123cfadeea"],"title":"QAC root occurrence: ط م ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["89:27"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:27","branch_refs":["root_000948/B001","root_001533/B011"],"candidate_id":"cand_273e88bd4ea4aeac7c40","commentary_obligation":"review","hft_ref":"hft_970dcff5fe5b55c38beb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_living_self_settled","source_type":"hft","support_ids":["sup_b6eaa5b9e6cdd98e303b"],"title":"baseline_living_self_settled","trust":"legacy_unbound"},{"anchor_refs":["89:27"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:27","branch_refs":["root_000948/B001","root_001533/B012"],"candidate_id":"cand_82b0d0d8b27accd52efc","commentary_obligation":"review","hft_ref":"hft_e595f0b17df659417be0","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_essential_self_at_rest","source_type":"hft","support_ids":["sup_76a7755cb4b4fa21581c"],"title":"baseline_essential_self_at_rest","trust":"legacy_unbound"},{"anchor_refs":["89:27"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:27","branch_refs":["root_000948/B001","root_001533/B001","root_001533/B002"],"candidate_id":"cand_b7d41e0e669fe7d533a7","commentary_obligation":"review","hft_ref":"hft_20f5606fd1da5b0e5daa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_breath_released","source_type":"hft","support_ids":["sup_e01ceda026aa2914df65"],"title":"baseline_breath_released","trust":"legacy_unbound"},{"anchor_refs":["89:27"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"89:27","branch_refs":["root_000948/B002","root_001533/B014"],"candidate_id":"cand_c7c66cce6cec5fa0028f","commentary_obligation":"review","hft_ref":"hft_7f95174bb021cb8dae56","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_lowered_mettle","source_type":"hft","support_ids":["sup_91618802710111938c9a"],"title":"baseline_lowered_mettle","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|ya+","morpheme_role":"PREFIX","pos":"VOC","qac_ref":"89:27:1:1","qac_word_ref":"89:27:1","root_ar":"","surface_ar":"يَٰٓ"},{"lemma_ar":"أَيَّتُهَا","morph_features":"STEM|POS:N|LEM:>ay~atuhaA|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:1:2","qac_word_ref":"89:27:1","root_ar":"","surface_ar":"أَيَّتُهَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:27:2:1","qac_word_ref":"89:27:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","root_ar":"ن ف س","surface_ar":"نَّفْسُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:27:3:1","qac_word_ref":"89:27:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُّطْمَئِنَّة","morph_features":"STEM|POS:ADJ|ACT|PCPL|(XII)|LEM:m~uToma}in~ap|ROOT:Tmn|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:27:3:2","qac_word_ref":"89:27:3","root_ar":"ط م ن","surface_ar":"مُطْمَئِنَّةُ"}],"word_analysis_qac_refs":[["89:27:1:1"],["89:27:1:2"],["89:27:2:1","89:27:2:2"],["89:27:3:1","89:27:3:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["89:27:1","89:27:2","89:27:3","89:27:4"]},"focus_surface_evidence":{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|ya+","morpheme_role":"PREFIX","pos":"VOC","qac_ref":"89:27:1:1","qac_word_ref":"89:27:1","root_ar":"","surface_ar":"يَٰٓ"},{"lemma_ar":"أَيَّتُهَا","morph_features":"STEM|POS:N|LEM:>ay~atuhaA|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:1:2","qac_word_ref":"89:27:1","root_ar":"","surface_ar":"أَيَّتُهَا"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:27:2:1","qac_word_ref":"89:27:2","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَفْس","morph_features":"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"89:27:2:2","qac_word_ref":"89:27:2","root_ar":"ن ف س","surface_ar":"نَّفْسُ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"89:27:3:1","qac_word_ref":"89:27:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مُّطْمَئِنَّة","morph_features":"STEM|POS:ADJ|ACT|PCPL|(XII)|LEM:m~uToma}in~ap|ROOT:Tmn|F|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"89:27:3:2","qac_word_ref":"89:27:3","root_ar":"ط م ن","surface_ar":"مُطْمَئِنَّةُ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["89:27:1:1"],["89:27:1:2"],["89:27:2:1","89:27:2:2"],["89:27:3:1","89:27:3:2"]],"word_analysis_refs":["89:27:1","89:27:2","89:27:3","89:27:4"],"word_rows":[{"analysis_record_ref":"89:27:1","analytic_gloss_range_en":"direct vocative opening that turns the line into a solemn summons over the whole tranquil-soul title, not a report or loose exclamation","analytic_root_gloss_range_en":null,"qac_refs":["89:27:1:1"],"root":{},"surface":{"arabic":"يَٰٓ","transliteration":"yā"}},{"analysis_record_ref":"89:27:2","analytic_gloss_range_en":"feminine vocative support form with alerting deixis, delaying and mediating the definite addressee rather than acting as a separate referent or possessive phrase","analytic_root_gloss_range_en":null,"qac_refs":["89:27:1:2"],"root":{},"surface":{"arabic":"أَيَّتُهَا","transliteration":"ayyatuhā"}},{"analysis_record_ref":"89:27:3","analytic_gloss_range_en":"the definite, singular, addressed self or soul as a whole living identity, already inside the vocative frame and qualified by tranquility before it becomes the commanded mover in 89:28","analytic_root_gloss_range_en":"broad root range covering breath, relief, living self or soul, inner identity, preciousness, and the thing itself; here the living self and inner identity branches are selected, while breath, relief, and value remain controlled image-pressure rather than independent local senses","qac_refs":["89:27:2:1","89:27:2:2"],"root":{"arabic":"ن ف س","transliteration":"n-f-s"},"surface":{"arabic":"ٱلنَّفْسُ","transliteration":"an-nafsu"}},{"analysis_record_ref":"89:27:4","analytic_gloss_range_en":"definite feminine active participial adjective naming the addressed self's achieved settled reassurance as an identifying state inside the title","analytic_root_gloss_range_en":"root field of becoming still, settled, reassured, secure, or brought down after disturbance; V4 has no guardrail rows for this root in the bundle, so local grammar and CRITICAL evidence keep the settled-state adjective central while security and phonic pressures remain qualified supports","qac_refs":["89:27:3:1","89:27:3:2"],"root":{"arabic":"ط م أ ن","transliteration":"ṭ-m-ʾ-n"},"surface":{"arabic":"ٱلْمُطْمَئِنَّةُ","transliteration":"al-muṭmaʾinnatu"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["89:27"],"branch_refs":["root_000948/B001","root_001533/B011"],"candidate_id":"cand_273e88bd4ea4aeac7c40","evidence_scope":"focus_ayah","hft_ref":"hft_970dcff5fe5b55c38beb","item_id":"baseline_living_self_settled","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_living_self_settled","support_id":"sup_b6eaa5b9e6cdd98e303b"},{"anchor_refs":["89:27"],"branch_refs":["root_000948/B001","root_001533/B012"],"candidate_id":"cand_82b0d0d8b27accd52efc","evidence_scope":"focus_ayah","hft_ref":"hft_e595f0b17df659417be0","item_id":"baseline_essential_self_at_rest","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_essential_self_at_rest","support_id":"sup_76a7755cb4b4fa21581c"},{"anchor_refs":["89:27"],"branch_refs":["root_000948/B001","root_001533/B001","root_001533/B002"],"candidate_id":"cand_b7d41e0e669fe7d533a7","evidence_scope":"focus_ayah","hft_ref":"hft_20f5606fd1da5b0e5daa","item_id":"baseline_breath_released","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_breath_released","support_id":"sup_e01ceda026aa2914df65"},{"anchor_refs":["89:27"],"branch_refs":["root_000948/B002","root_001533/B014"],"candidate_id":"cand_c7c66cce6cec5fa0028f","evidence_scope":"focus_ayah","hft_ref":"hft_7f95174bb021cb8dae56","item_id":"baseline_lowered_mettle","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_lowered_mettle","support_id":"sup_91618802710111938c9a"}],"diagnostics":[],"lane_counts":{"global":13,"macro":12,"micro":4},"packet_summary":{"ayah_count":30,"focus_ref":"89:27","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س ر ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000702","furuq_root_norm":"س ر ي","furuq_source_root_norm":"س ر ي","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000697","furuq_root_norm":"س ر ر","furuq_source_root_norm":"س ر ر","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ف ع ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001167","furuq_root_norm":"ف ع ل","furuq_source_root_norm":"ف ع ل","is_dominant":true,"target_occurrences":108,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000007","furuq_root_norm":"ء ب و","furuq_source_root_norm":"أ ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ع و د","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001058","furuq_root_norm":"ع و د","furuq_source_root_norm":"ع و د","is_dominant":true,"target_occurrences":35,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000989","furuq_root_norm":"ع د د","furuq_source_root_norm":"ع د د","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ج و ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000273","furuq_root_norm":"ج و ب","furuq_source_root_norm":"ج و ب","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000283","furuq_root_norm":"ج ي ب","furuq_source_root_norm":"ج ي ب","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000220","furuq_root_norm":"ج ب ي","furuq_source_root_norm":"ج ب ي","is_dominant":false,"target_occurrences":2,"target_rank":3},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000214","furuq_root_norm":"ج ب ب","furuq_source_root_norm":"ج ب ب","is_dominant":false,"target_occurrences":1,"target_rank":4}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ب ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000153","furuq_root_norm":"ب ل و","furuq_source_root_norm":"ب ل و","is_dominant":true,"target_occurrences":28,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000154","furuq_root_norm":"ب ل ي","furuq_source_root_norm":"ب ل ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ق و ل","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001272","furuq_root_norm":"ق و ل","furuq_source_root_norm":"ق و ل","is_dominant":true,"target_occurrences":1408,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001251","furuq_root_norm":"ق ل ل","furuq_source_root_norm":"ق ل ل","is_dominant":false,"target_occurrences":163,"target_rank":2}]},{"qac_root":"ه و ن","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001453","furuq_root_norm":"م ه ن","furuq_source_root_norm":"م ه ن","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001608","furuq_root_norm":"ه و ن","furuq_source_root_norm":"ه و ن","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001687","furuq_root_norm":"و ه ن","furuq_source_root_norm":"و ه ن","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ء ك ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000043","furuq_root_norm":"ء ك ل","furuq_source_root_norm":"أ ك ل","is_dominant":true,"target_occurrences":79,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001315","furuq_root_norm":"ك ل ل","furuq_source_root_norm":"ك ل ل","is_dominant":false,"target_occurrences":30,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["89:1","89:2","89:3","89:4","89:5","89:6","89:7","89:8","89:9","89:10","89:11","89:12","89:13","89:14","89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"89:27","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":19,"unstructured_record_count":0},"identity":{"ayah_ref":"89:27","lane":"micro","linguistic_source_ref":"89:27","surface_ref":"89:27","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"89:27","target_tokens":[["Ey",["89:27:1"]],["huzur",["89:27:3"]],["bulmuş",["89:27:3"]],["ruh",["89:27:2"]]],"text":"Ey huzur bulmuş ruh!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":15,"ayah_to":30,"id":"s089-p02-015-030","label":"The wealth test, judgment, and tranquil soul","number":2,"refs":["89:15","89:16","89:17","89:18","89:19","89:20","89:21","89:22","89:23","89:24","89:25","89:26","89:27","89:28","89:29","89:30"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3","source_type":"word_analysis","support_id":"sup_05f2ab5c884307c80f05","text":"{\"gloss_range\":\"the definite, singular, addressed self or soul as a whole living identity, already inside the vocative frame and qualified by tranquility before it becomes the commanded mover in 89:28\",\"prose\":\"{{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}}) resolves the support form and names the addressee as a definite, singular self. Its nominative appositional role keeps it inside the address rather than making it an object or circumstantial state, and its agreement with {{ar:ٱلْمُطْمَئِنَّةُ}} ({{tr:al-muṭmaʾinnatu}}) makes tranquility part of the title. The repeated definiteness binds noun and adjective into a recognized title, while a very common Quranic self-word is narrowed here to one direct addressee. The root range lets the word carry whole living identity: soul, person, inner self, and embodied life-breath. That breath and relief pressure is real but locally narrowed; the ayah calls the living self, not a free-standing breath, and the settled adjective makes release from constriction felt without replacing the selected selfhood sense. A value branch also stays subordinate to the title: the self is not marked by rivalry or striving for what is precious, but by the settled condition that qualifies it. The noun arrives before the qualifier, so selfhood is named first and then disclosed as tranquil. It also prepares 89:28, where the named recipient of recognition becomes the addressee of {{ar:ٱرْجِعِىٓ}} ({{tr:irjiʿī}}). Against the prior binding scene in 89:26, the visual center moves from external restraint to inner identity. The inter-ayah echoes sharpen that recognition: every soul's mortality (3:185) is narrowed here to one addressed self, and the morally fashioned self of 91:7-10 is heard after its polarity has settled.\",\"root_display\":\"{{ar:ن ف س}} ({{tr:n-f-s}})\",\"root_gloss_range\":\"broad root range covering breath, relief, living self or soul, inner identity, preciousness, and the thing itself; here the living self and inner identity branches are selected, while breath, relief, and value remain controlled image-pressure rather than independent local senses\",\"surface_display\":\"{{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1:boundary-pivot","source_type":"word_analysis","support_id":"sup_16fbbfbff44c510401b6","text":"{\"blocking_evidence\":null,\"headline\":\"third-person judgment pivots to direct call\",\"reader_payoff\":\"The reader feels the scene change immediately from observed punishment in 89:26 to a directly heard address in 89:27.\",\"reason\":\"The vocative particle is the first surface marker of the shift from the prior third-person judgment scene into direct address.\",\"representative_source_ids\":[\"QI-6727ea1d\",\"QB-7934d605\",\"QB-c24ca69d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:27:2:2","source_type":"qac_morpheme","support_id":"sup_1b5f349f110abf416d33","text":"{\"lemma_ar\":\"نَفْس\",\"morph_features\":\"STEM|POS:N|LEM:nafos|ROOT:nfs|FS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"89:27:2:2\",\"qac_word_ref\":\"89:27:2\",\"root_ar\":\"ن ف س\",\"surface_ar\":\"نَّفْسُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:boundary-inward-settledness","source_type":"word_analysis","support_id":"sup_3469699e88fb14555ff6","text":"{\"blocking_evidence\":null,\"headline\":\"external binding becomes inward composure\",\"reader_payoff\":\"The reader feels the prior firmness of punishment in 89:26 inverted into blessed inward settledness in 89:27.\",\"reason\":\"Boundary rows contrast the prior outward restraint scene with the new recognition scene completed by the inner-state adjective.\",\"representative_source_ids\":[\"QS-f1191565\",\"QB-32f82d27\",\"QB-5f061ce3\",\"QB-950fa613\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:hamzah-and-heavy-ending","source_type":"word_analysis","support_id":"sup_36d27465e716988db2c5","text":"{\"blocking_evidence\":null,\"headline\":\"marked sound shape gives settled weight\",\"reader_payoff\":\"The reader hears a controlled catch and heavy ending that make the final calm less fleeting.\",\"reason\":\"The written hamzah and doubled ending are visible in the surface form and support the row's sound-form observation.\",\"representative_source_ids\":[\"QF-1d9fe72b\",\"QP-76044864\",\"QP-85782e4b\",\"MP-f6fba206\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:intertextual-recognition","source_type":"word_analysis","support_id":"sup_4c8ee76b3de2ac8283ed","text":"{\"blocking_evidence\":null,\"headline\":\"mortality and moral testing resolve into recognition\",\"reader_payoff\":\"The reader notices that broad Quranic scenes of soul-mortality and moral testing are reframed here as singular tranquil recognition.\",\"reason\":\"The CRITICAL rows provide concrete links to every soul tasting death (3:185) and the fashioned and tested self (91:7-10), and neither is contradicted by local grammar.\",\"representative_source_ids\":[\"QI-26aac8ba\",\"QI-4a7ef03f\",\"MI-16e70583\",\"MI-5d1b56c7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"89:27:3:2","source_type":"qac_morpheme","support_id":"sup_5b378c829c123cfadeea","text":"{\"lemma_ar\":\"مُّطْمَئِنَّة\",\"morph_features\":\"STEM|POS:ADJ|ACT|PCPL|(XII)|LEM:m~uToma}in~ap|ROOT:Tmn|F|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"89:27:3:2\",\"qac_word_ref\":\"89:27:3\",\"root_ar\":\"ط م ن\",\"surface_ar\":\"مُطْمَئِنَّةُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1","source_type":"word_analysis","support_id":"sup_5e0b9a135cdbd8f40268","text":"{\"gloss_range\":\"direct vocative opening that turns the line into a solemn summons over the whole tranquil-soul title, not a report or loose exclamation\",\"prose\":\"{{ar:يَٰٓ}} ({{tr:yā}}) makes the ayah begin as direct address. Its scope reaches through {{ar:أَيَّتُهَا}} ({{tr:ayyatuhā}}) to the full title {{ar:ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ}} ({{tr:an-nafsu al-muṭmaʾinnatu}}), so the tranquil self is summoned, not merely described. The call range is narrowed here to solemn recognition: the following title blocks a grief-cry or request reading. Because the line has no finite predicate, the opening vocative carries the first act of the ayah and pivots the scene from the third-person binding statement in 89:26 into second-person recognition. The extended written and audible onset lets that pivot arrive as a drawn-out summons before the support form and noun appear.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:يَٰٓ}} ({{tr:yā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:opposed-securities","source_type":"word_analysis","support_id":"sup_6283c7ed70acab92290a","text":"{\"blocking_evidence\":null,\"headline\":\"two kinds of firmness are inverted\",\"reader_payoff\":\"The reader notices that security can appear as imposed restraint in 89:26 or inward reassurance in 89:27, with the final adjective carrying the blessed side.\",\"reason\":\"The boundary row distinguishes the opposed modes of firmness across the ayah boundary, and the local adjective names the inward mode.\",\"representative_source_ids\":[\"QB-f6dda377\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:distributional-prominence","source_type":"word_analysis","support_id":"sup_67017ec921f769becc45","text":"{\"blocking_evidence\":null,\"headline\":\"rare settled-state form is prominent\",\"reader_payoff\":\"The reader notices the final qualifier as a marked settled-state label rather than a routine adjective.\",\"reason\":\"Contextual evidence marks the exact root-form as low occurrence, supporting the prominence of this final participial qualifier.\",\"representative_source_ids\":[\"QI-2714bb4d\",\"QI-532d8a4e\",\"QH-ca8570c9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:adjective-bound-title","source_type":"word_analysis","support_id":"sup_6b382e1ee18027e6efd8","text":"{\"blocking_evidence\":null,\"headline\":\"definiteness and agreement bind the tranquil title\",\"reader_payoff\":\"The reader notices tranquility as part of a recognized title, not a detached predicate floating after the noun.\",\"reason\":\"The noun and adjective share definiteness, gender, and local attachment, so the adjective qualifies the addressed self directly.\",\"representative_source_ids\":[\"QG-caf0233a\",\"QF-76dd0ef6\",\"QE-97bef82f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:bridge-to-following-states","source_type":"word_analysis","support_id":"sup_6ccdbc0adbb57061054e","text":"{\"blocking_evidence\":null,\"headline\":\"tranquility prepares the states of 89:28\",\"reader_payoff\":\"The reader notices that the final settled state becomes the threshold for return and reciprocal approval in 89:28.\",\"reason\":\"The CRITICAL rows link the adjective of 89:27 to the feminine states and imperative movement that follow in 89:28.\",\"representative_source_ids\":[\"QB-5be3daf8\",\"QB-feb49b9e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:settled-reassurance-after-disturbance","source_type":"word_analysis","support_id":"sup_7857705995572417940f","text":"{\"blocking_evidence\":null,\"headline\":\"calm means achieved settled rest\",\"reader_payoff\":\"The reader hears tranquility as achieved repose after agitation, not a vague pleasant mood.\",\"reason\":\"The bundle lacks V4 rows for {{ar:ط م أ ن}} ({{tr:ṭ-m-ʾ-n}}), but the CRITICAL lexical evidence coheres with the local participial adjective and is not contradicted by guardrail evidence.\",\"representative_source_ids\":[\"QS-2ae8b26f\",\"QS-2e0df3ad\",\"QS-3372b78a\",\"MS-3d1ec584\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:recipient-before-agency","source_type":"word_analysis","support_id":"sup_804d776300024e2fb288","text":"{\"blocking_evidence\":null,\"headline\":\"recognized recipient becomes later mover\",\"reader_payoff\":\"The reader notices that 89:27 first names the soul as recipient of recognition, then 89:28 can command it to return.\",\"reason\":\"The local ayah contains the named addressee without a finite verb, while the following ayah supplies the feminine imperative to that same addressed self.\",\"representative_source_ids\":[\"QS-60222a42\",\"QF-4599eedc\",\"MI-8ac95efc\",\"QB-86be7197\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:security-and-stilling-contour","source_type":"word_analysis","support_id":"sup_809fac8cb0cebce26a88","text":"{\"blocking_evidence\":null,\"headline\":\"security and lowering support settledness\",\"reader_payoff\":\"The reader senses secure composure and downward stilling inside the canonical settledness, without replacing the canonical adjective.\",\"reason\":\"The non-canonical security reading and partner field are useful as contrastive support, while the local canonical surface remains the settled-rest participle.\",\"representative_source_ids\":[\"QS-658709c1\",\"QS-88833fc0\",\"ME-7d02bda1\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2:placeholder-alert","source_type":"word_analysis","support_id":"sup_85c2952f7ac07e6b56a0","text":"{\"blocking_evidence\":null,\"headline\":\"placeholder and alert point forward\",\"reader_payoff\":\"The reader sees the addressee being formally delayed and revealed rather than introduced by a bare noun call.\",\"reason\":\"The wider range of the support form is narrowed by the preceding vocative and following definite noun; the final alerting element is deictic in this frame, not ordinary possession.\",\"representative_source_ids\":[\"QG-c271f3a0\",\"QG-cf8341d2\",\"QS-a395f76b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:boundary-inner-identity","source_type":"word_analysis","support_id":"sup_8ab7a56c4e9c4085ab59","text":"{\"blocking_evidence\":null,\"headline\":\"external restraint gives way to inner selfhood\",\"reader_payoff\":\"The reader sees the scene's center shift from imposed binding in 89:26 to an included and named inner self in 89:27.\",\"reason\":\"The boundary rows describe the move from negated universal agency and external restraint to positive direct address of a definite self.\",\"representative_source_ids\":[\"QB-0b1a4af5\",\"QB-6cde696b\",\"QB-e4afc728\",\"QB-39272898\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:final-closure","source_type":"word_analysis","support_id":"sup_91e74a7675305363d795","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective lands the ayah on tranquility\",\"reader_payoff\":\"The reader feels the vocative buildup resolve in the final word, making tranquility the line's last conceptual landing.\",\"reason\":\"The adjective follows the head noun and is the final word of 89:27, so it resolves the addressed title before 89:28 begins.\",\"representative_source_ids\":[\"QT-3642f67f\",\"QT-b24ed0bb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2","source_type":"word_analysis","support_id":"sup_94a1268eb90d1b170c35","text":"{\"gloss_range\":\"feminine vocative support form with alerting deixis, delaying and mediating the definite addressee rather than acting as a separate referent or possessive phrase\",\"prose\":\"{{ar:أَيَّتُهَا}} ({{tr:ayyatuhā}}) is not a floating pronoun between the call and the noun. It is the feminine support form that lets the vocative address a definite addressee, and its agreement points forward to {{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}}). The attached alerting element points the hearer into the coming noun phrase rather than creating possession. This makes the address unfold in stages: first the call, then the gendered support, then the named self and its final qualifying state. The feminine frame also begins before the later feminine commands, so the discourse-person shift is already active in the support form. After 89:26 has excluded every rival agent, this placeholder becomes the doorway through which one definite self enters the speech. The canonical feminine marking also matters as a contrastive apparatus point; it keeps the support fitted to the feminine noun, while non-canonical masculine-like support cannot control the local parse.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:أَيَّتُهَا}} ({{tr:ayyatuhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:adjectival-participle-title","source_type":"word_analysis","support_id":"sup_95748bfc8731f3642d85","text":"{\"blocking_evidence\":null,\"headline\":\"participial adjective identifies the self\",\"reader_payoff\":\"The reader notices settledness as an identifying state inside the address, not as a separate report about the soul.\",\"reason\":\"QAC and attachment evidence identify the word as a definite feminine active participle agreeing with and adjectivally modifying {{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}}).\",\"representative_source_ids\":[\"QG-927b382e\",\"QG-e1c5f3ed\",\"QG-ed79aa67\",\"MG-33209c3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:definite-singular-vocative-narrowing","source_type":"word_analysis","support_id":"sup_983fa07c8c0f103a3df0","text":"{\"blocking_evidence\":null,\"headline\":\"common self-field becomes one addressed self\",\"reader_payoff\":\"The reader sees a very common Quranic self-word narrowed into one direct and recognizable addressee.\",\"reason\":\"Contextual profiles show a very common abstract noun form, while the local definite singular vocative frame individualizes it.\",\"representative_source_ids\":[\"QF-78766a07\",\"QI-033f3710\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:hearts-to-whole-self","source_type":"word_analysis","support_id":"sup_a439bcd79e4196680edb","text":"{\"blocking_evidence\":null,\"headline\":\"heart-rest echo expands to the whole self\",\"reader_payoff\":\"The reader sees the rest-field known from hearts finding rest by remembrance (13:28) applied here to the whole addressed self.\",\"reason\":\"The CRITICAL rows give the concrete comparison to hearts finding rest (13:28), and local grammar places the related rest-field on the whole self.\",\"representative_source_ids\":[\"QI-26b76a28\",\"MI-5e98e12c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:value-without-striving","source_type":"word_analysis","support_id":"sup_a6cc017f2013b3f42330","text":"{\"blocking_evidence\":null,\"headline\":\"preciousness is subordinated to settled identity\",\"reader_payoff\":\"The reader notices that any value-pressure around the self is realized through settled qualification, not competition or striving.\",\"reason\":\"The root range includes preciousness and rivalry for valued things, but the local phrase values the self by its tranquil title, not by a competition construction.\",\"representative_source_ids\":[\"QS-80c2c3d0\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:definite-appositional-addressee","source_type":"word_analysis","support_id":"sup_a71fc8b080001b28eda3","text":"{\"blocking_evidence\":null,\"headline\":\"definite noun resolves the support form\",\"reader_payoff\":\"The reader sees the self as the named addressee inside the vocative architecture, not as an anonymous soul or separate clause.\",\"reason\":\"QAC and attachment evidence mark the word as a definite feminine nominative noun in apposition to the support form.\",\"representative_source_ids\":[\"QG-3e253622\",\"QG-6dacea6c\",\"QG-af81fcf6\",\"MG-9d1ff7f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:whole-living-self","source_type":"word_analysis","support_id":"sup_a8afcd6e57164c50e307","text":"{\"blocking_evidence\":null,\"headline\":\"selfhood carries breath and relief pressure\",\"reader_payoff\":\"The reader hears the addressed soul as a whole living identity with embodied breath and release pressure, not as a thin abstraction.\",\"reason\":\"V4 supports living self, inner identity, breath, and relief branches for {{ar:ن ف س}} ({{tr:n-f-s}}), while local grammar selects the addressed self rather than an independent breath or relief construction.\",\"representative_source_ids\":[\"QS-722d6d15\",\"QS-7cca906c\",\"QS-c3b507fd\",\"MS-aca46f40\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2:expanded-entry","source_type":"word_analysis","support_id":"sup_b41cbc7d11682e6de8e5","text":"{\"blocking_evidence\":null,\"headline\":\"support form slows entry into the noun\",\"reader_payoff\":\"The reader feels the addressee's arrival delayed by a ceremonially expanded call rather than rushed into a bare noun.\",\"reason\":\"The sequence places two vocative elements before the noun, creating both structural delay and a longer calling cadence.\",\"representative_source_ids\":[\"QT-e4046cb7\",\"QP-51d3a70a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1:recognition-summons","source_type":"word_analysis","support_id":"sup_ce3a3d634e21aa504ba2","text":"{\"blocking_evidence\":null,\"headline\":\"call range narrows to solemn recognition\",\"reader_payoff\":\"The reader hears the word as a performed recognition of the settled self, not as a grief cry, request, or neutral information marker.\",\"reason\":\"The particle has a broader discourse range, but the following definite tranquil-self title and lack of finite predicate select solemn address in this local frame.\",\"representative_source_ids\":[\"QS-827e83fb\",\"QS-9569d2ae\",\"QI-d3151189\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2:positive-addressee-turn","source_type":"word_analysis","support_id":"sup_cf3e2b77210295fb3a79","text":"{\"blocking_evidence\":null,\"headline\":\"placeholder opens the way to the named addressee\",\"reader_payoff\":\"The reader notices the move from excluded rival agency in 89:26 to one definite self entering the address in 89:27.\",\"reason\":\"The support form is the grammatical bridge through which the definite self is named after the previous ayah's universal exclusion.\",\"representative_source_ids\":[\"QB-5f65e6ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2:canonical-feminine-form","source_type":"word_analysis","support_id":"sup_d3cfb038e4a344eed100","text":"{\"blocking_evidence\":null,\"headline\":\"canonical feminine marking is contrastive\",\"reader_payoff\":\"The reader notices the visible feminine marking around the noun as part of the address's recognition force.\",\"reason\":\"The canonical form preserves feminine agreement with the local noun; the non-canonical contrast is useful as apparatus, but it does not govern the canonical parse.\",\"representative_source_ids\":[\"QF-ae01d896\",\"QF-c41cf17d\",\"QF-cd44f86d\",\"QE-b374f70b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4:participial-state-form","source_type":"word_analysis","support_id":"sup_d6140edbe041dc508cf5","text":"{\"blocking_evidence\":null,\"headline\":\"process is compressed into possessed state\",\"reader_payoff\":\"The reader notices that the soul is addressed under an already possessed state, not narrated as becoming calm in the moment.\",\"reason\":\"The active participial adjective and definite agreement present settledness as part of the title at address-time.\",\"representative_source_ids\":[\"QF-25f525f7\",\"QF-aac1ddb9\",\"QF-c70ce45f\",\"MF-df7e90a7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1:vocative-scope","source_type":"word_analysis","support_id":"sup_e64d7820109d73d4caed","text":"{\"blocking_evidence\":null,\"headline\":\"vocative governs the full tranquil-self title\",\"reader_payoff\":\"The reader notices that the particle summons the whole tranquil-self title rather than loosely introducing an exclamation.\",\"reason\":\"QAC and attachment evidence mark {{ar:يَٰٓ}} ({{tr:yā}}) as the vocative particle governing the support construction that introduces the addressee phrase.\",\"representative_source_ids\":[\"QG-3045901c\",\"QG-52bcebae\",\"MG-6c298487\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:2:feminine-agreement","source_type":"word_analysis","support_id":"sup_e7451d77dd517398acee","text":"{\"blocking_evidence\":null,\"headline\":\"feminine support locks onto the self\",\"reader_payoff\":\"The reader notices that the second-person feminine frame begins before the noun and before the following commands.\",\"reason\":\"The support word agrees with the feminine noun {{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}}), and attachment evidence treats that noun as the addressee supplied by the construction.\",\"representative_source_ids\":[\"QG-8d3a9114\",\"MG-60cd7747\",\"QI-8697cbdb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:4","source_type":"word_analysis","support_id":"sup_f2043644d34a7d565e7b","text":"{\"gloss_range\":\"definite feminine active participial adjective naming the addressed self's achieved settled reassurance as an identifying state inside the title\",\"prose\":\"{{ar:ٱلْمُطْمَئِنَّةُ}} ({{tr:al-muṭmaʾinnatu}}) completes the title by qualifying {{ar:ٱلنَّفْسُ}} ({{tr:an-nafsu}}) from inside the address. As a definite feminine active participle, it presents settled reassurance as a state possessed at the moment of summons, not as a separate predicate and not as a later circumstantial state. The lexical pressure is more than pleasant calm: the root field points to stillness, reassurance, and security after motion or fear, with a concrete sense of agitation brought down into rest. The security-adjacent non-canonical reading and partner field support that confidence, but the canonical word keeps safety joined to settledness rather than replacing it with a separate security adjective. Because the adjective is the final word, the ayah lands on tranquility before 89:28 commands return. The internal hamzah and doubled ending give that landing audible weight, so the sound shape supports the semantic settling. The rare participial form also makes the qualifier prominent, and the echo with hearts finding rest by remembrance (13:28) expands here into the whole addressed self. Across the boundary from 89:26, imposed restraint is inverted into inward settledness, and this final state becomes the threshold for the pleased and approved states that follow in 89:28.\",\"root_display\":\"{{ar:ط م أ ن}} ({{tr:ṭ-m-ʾ-n}})\",\"root_gloss_range\":\"root field of becoming still, settled, reassured, secure, or brought down after disturbance; V4 has no guardrail rows for this root in the bundle, so local grammar and CRITICAL evidence keep the settled-state adjective central while security and phonic pressures remain qualified supports\",\"surface_display\":\"{{ar:ٱلْمُطْمَئِنَّةُ}} ({{tr:al-muṭmaʾinnatu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1:extended-onset","source_type":"word_analysis","support_id":"sup_f339e4471d229072a507","text":"{\"blocking_evidence\":null,\"headline\":\"drawn-out opening call\",\"reader_payoff\":\"The reader notices that the call begins with visible and audible length before the addressee is named.\",\"reason\":\"The split analysis makes the vocative particle visible, and its written surface carries an extended opening before the support form follows.\",\"representative_source_ids\":[\"QF-315f5539\",\"QF-9dc75167\",\"QP-15201fa8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:3:head-before-qualifier","source_type":"word_analysis","support_id":"sup_f5d9c10c990467afc173","text":"{\"blocking_evidence\":null,\"headline\":\"selfhood lands before tranquility qualifies it\",\"reader_payoff\":\"The reader feels the title unfold as self first, then tranquility as the resolving qualification.\",\"reason\":\"The noun precedes the adjective in a verbless recognition scene, so the qualifier resolves the identity rather than replacing the head noun.\",\"representative_source_ids\":[\"QT-de115b1f\",\"MT-779eb6ae\",\"QT-e3172487\",\"QY-45bb8642\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"89:27:1:verbless-launch","source_type":"word_analysis","support_id":"sup_fcdc43df3f10dcab80c3","text":"{\"blocking_evidence\":null,\"headline\":\"summons opens before any predicate\",\"reader_payoff\":\"The reader notices that identity and inner state carry the ayah before any action or command begins.\",\"reason\":\"The ayah opens with the vocative particle and contains no finite predicate in 89:27, so summons and recognition supply the line's structural force.\",\"representative_source_ids\":[\"QT-e4581482\",\"MT-3701d62a\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000948/B001","root_001533/B011"],"payload":{"activation_trace":[{"branch_id":"B011","mapped_root_id":"root_001533","role":"The living soul-self supplies the animate identity directly summoned by the vocative.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000948","role":"Settled calm supplies the addressee's attained condition and implies prior agitation as its contrast.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]}],"changed_reading":{"after":"The living self is personally summoned in the condition of having come to rest after disturbance.","before":"A soul is merely described as calm."},"confidence":"strong","focus_anchor":"The noun النفس is the addressee and المطمئنة is its feminine singular modifier.","mechanism":"The address selects the life-bearing self and names its achieved condition as settled calm after disturbance.","model_id":"baseline_living_self_settled"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_living_self_settled","source_type":"hft","support_id":"sup_b6eaa5b9e6cdd98e303b","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000948/B001","root_001533/B012"],"payload":{"activation_trace":[{"branch_id":"B012","mapped_root_id":"root_001533","role":"The very thing itself supplies an essential rather than merely affective scope for النفس.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000948","role":"Settled calm functions as a stable quality of that whole identity.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]}],"changed_reading":{"after":"The addressee is addressed at the level of its whole, settled identity.","before":"The addressee happens to feel tranquil."},"confidence":"strong","focus_anchor":"النفس can mark the very identity or essence of the addressed one, not only a passing psychic state.","mechanism":"The adjective reaches the whole identity: calm has penetrated to the self's core rather than remaining an emotion laid over it.","model_id":"baseline_essential_self_at_rest"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_essential_self_at_rest","source_type":"hft","support_id":"sup_76a7755cb4b4fa21581c","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000948/B001","root_001533/B001","root_001533/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001533","role":"Breath leaving the body gives النفس a rhythmic, embodied substrate.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001533","role":"Relief by making breathing room turns calm into release from constriction.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000948","role":"Settling after agitation supplies the endpoint of the release.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]}],"changed_reading":{"after":"Calm is also the body's recovered breathing room, an unforced breath after constriction.","before":"Calm is an abstract inward mood."},"confidence":"medium","focus_anchor":"The focus noun carries breath and relief branches while its modifier carries settling after agitation.","mechanism":"A respiratory-material reading coexists with the personal one: constriction has been given room, breath can leave freely, and the self is calm because it is no longer held tight.","model_id":"baseline_breath_released"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_breath_released","source_type":"hft","support_id":"sup_e01ceda026aa2914df65","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ","ayah_ref":"89:27"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000948/B002","root_001533/B014"],"payload":{"activation_trace":[{"branch_id":"B014","mapped_root_id":"root_001533","role":"Inner mettle and self-regard supply what can cease straining upward.","root":"ن ف س","source_ref":"89:27","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000948","role":"Physical lowering supplies an embodied posture of composure rather than an emotion alone.","root":"ط م ن","source_ref":"89:27","source_word_indices":["3"]}],"changed_reading":{"after":"It may also picture a self whose mettle has stopped elevating itself and has settled low without collapse.","before":"المطمئنة means only psychologically untroubled."},"confidence":"exploratory","focus_anchor":"The adjective's inventory includes physical lowering, while النفس can denote self-regard, resolve, and inner mettle.","mechanism":"The phrase can spatialize composure as proud or strained self-regard bending down into a stable low posture without being degraded.","model_id":"baseline_lowered_mettle"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_lowered_mettle","source_type":"hft","support_id":"sup_91618802710111938c9a","trust":"legacy_unbound"}]}
</lane_packet_json>
