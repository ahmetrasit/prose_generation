# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **92:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s092-regular-20260912/s092/92_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "92:2",
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
{"branch_registry":[{"boundary":"Bu dal, parlatma, yurttan ayrılma, gelin gösterimi ve saçın çekilmesi gibi öteki dalların özel anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000256/B001","candidate_links":[{"candidate_id":"cand_144d31dcabf292c3749f","lane":"micro"},{"candidate_id":"cand_f36155fd60af20406c62","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"örtülünün açığa çıkması veya çıkarılması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gizli, örtülü veya belirsiz olan şey görünür ve anlaşılır hale gelir ya da biri onu bu hale getirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin veya durumun ne olduğu açıklık kazanır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaygı, hastalık veya karanlık gibi örten bir durum dağılır ya da giderilir."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görünür ve anlaşılır hale gelme ya da getirme biçimindeki genel çekirdeğini karşılar.","boundary_detail":"Bu dal, parlatma, yurttan ayrılma, gelin gösterimi ve saçın çekilmesi gibi öteki dalların özel anlamlarını kapsamaz.","branch_image_ar":"الكشف والظهور","concept_gloss":"örtülünün açığa çıkması veya çıkarılması","contextual_glosses":[{"applicability":"Bir haberin, durumun veya kişinin halinin anlaşılır olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirsiz bir bilginin anlaşılır hale gelmesini doğal Türkçeyle karşılar."},"facet_ids":["F002"],"text":"açıklığa kavuşmak","usage_role":"contextual"},{"applicability":"Kaygı, hastalık ya da karanlık gibi örten bir durumun ortadan kalktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Örten veya bunaltan durumun ortadan kalkmasını ve alttaki halin açığa çıkmasını korur."},"facet_ids":["F003"],"text":"dağılmak veya giderilmek","usage_role":"contextual"}],"definition":"Örtülü ya da bilinmez olan bir şeyin açığa çıkması veya açığa çıkarılmasıdır. Haber ve durum anlaşılır hale gelebilir; kaygı, hastalık ya da karanlık gibi örten bir etken de giderilerek alttaki durum görünür olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gizli, örtülü veya belirsiz olan şey görünür ve anlaşılır hale gelir ya da biri onu bu hale getirir."},{"facet_id":"F002","role":"specialization","statement":"Bir haberin veya durumun ne olduğu açıklık kazanır."},{"facet_id":"F003","role":"extension","statement":"Kaygı, hastalık veya karanlık gibi örten bir durum dağılır ya da giderilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Fiziksel açığa çıkmayı ve kaygı, hastalık ya da karanlığın dağılması yönünü karşılamaz.","preserves":"Bilgiye ilişkin belirsizliğin giderilmesi yönünü korur."},"text":"açıklama"}],"identity_rationale":"Kaynak ifadesi, örtülü bir şeyin açığa çıkmasını veya çıkarılmasını temel alır; haberin anlaşılır olması ile hastalık, kaygı ve karanlık gibi örten durumların dağılmasını bu temelin farklı gerçekleşmeleri olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"örtülü şeyi açığa çıkarmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"açık, belirgin; açık kanıt"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haber benim için açıklığa kavuştu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"hastalığı gidermek veya kaygıyı dağıtmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"ortaya çıkmak, görünür olmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"örtücü durum dağılıp açılmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birbirimizin hali karşılıklı olarak ortaya çıktı"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"sarığı alından katlayarak kaldırmak"}],"lexicalization_note":"Tanım hem genel açığa çıkma çekirdeğini hem de haber, hastalık, kaygı ve başlıkla kurulan belirli kullanımları birbirine karıştırmadan korur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yalnızca açığa çıkma çekirdeğini bilgi, etkin ortaya çıkarma ve parlatma sınırlarıyla belirginleştiren üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal ortaya çıkma ve belli olma alanını kanıtlarla birlikte genişletirken bu dal, açığa çıkarma işlemini ve örten sıkıntının giderilmesini özellikle içerir.","focus_only":"Örten bir durumun giderilmesiyle kaygı veya hastalığın dağılmasını da kapsar.","gloss":"ortaya çıkma ve belli olma","neighbor_only":"Açıklığı belirten kanıt ve belirti adlarını da kendi alanına alır.","neighbor_ref":"root_000170/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da gizli veya belirsiz bir şeyin görünür ve anlaşılır hale gelmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal hem kendiliğinden açılmayı hem de açıklığa kavuşturmayı kapsar; komşu dal ise gizliyi etkin biçimde ortaya çıkarma işlemine daha sıkı bağlıdır.","focus_only":"Bir şeyin kendiliğinden görünür olması ve sıkıntının dağılması bu dalda belirgindir.","gloss":"gizliliği kaldırıp ortaya çıkarma","neighbor_only":"Saklı şeyi yerinden çıkarma ve başkasının gizliliğini kaldırma yönü daha baskındır.","neighbor_ref":"root_000428/B003","relation_type":"near_synonym","shared_zone":"İki dal da bir şey üzerindeki gizliliğin kaldırılması sonucunda görünürlüğü anlatır."},{"boundary_match":"partial","distinction":"Bu dalın çekirdeği açığa çıkmadır; komşu dal ise belirli nesne ve uygulamalarda yüzeyi ya da görüşü berraklaştıran işleme dayanır.","focus_only":"Gizli veya belirsiz olanın görünür ve anlaşılır hale gelmesini anlatır.","gloss":"parlatıp berraklaştırma","neighbor_only":"Kılıcın yüzeyini parlatma ve göz boyasıyla görüşü berraklaştırma kullanımlarına bağlıdır.","neighbor_ref":"root_000256/B002","relation_type":"near_neighbor","shared_zone":"Her ikisinde de bir engelin azalmasıyla açıklık veya berraklık sonucu doğar."}],"source_phrase_ar":"انكشاف الشيء وبروزه (maqayis)؛ أمر جلي واضح وأجل لنا هذا الأمر أي أوضحه وجلا الله عنك المرض (ayn)؛ الجلي نقيض الخفي وجلا لي الخبر وجلوت أي أوضحت وكشفت وانجلى عنه الهم وتجالينا (sihah)؛ أصل الجلو الكشف الظاهر والتجلي قد يكون بالذات وبالأمر والفعل (mufradat)","source_summary":"Kaynaklar, görünmez veya anlaşılmaz olanın ortaya çıkması ile onu örten şeyin kaldırılmasını ortak çekirdek sayar; haberin açıklığa kavuşmasını ve sıkıntı, hastalık ya da karanlığın dağılmasını bu çekirdeğe bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"ظهور الشيء بعد خفائه وبيان الأمر والخبر وانكشاف الهم والمرض والظلام","what_is_not_ar":"ليس الجلاء عن الوطن ولا جلوة العروس ولا الصقل ولا انحسار الشعر"},"support_links":["sup_2fcd94077e1707e120e8","sup_874c7c38b83d38d30918"]},{"boundary":"Tanım yalnızca kılıç yüzeyinin parlatılması ile göz boyasının görüşü berraklaştırdığı kullanımları kapsar; genel açığa çıkarma anlamına yayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000256/B002","candidate_links":[{"candidate_id":"cand_b60cfc02f90a5d784d58","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"kılıcı parlatma ve göz boyasıyla görüşü berraklaştırma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kılıcın yüzeyi işlenerek parlatılır ve temiz bir görünüm kazanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göze çekilen belirli boya, görüşü daha berrak hale getiren madde veya uygulama olarak adlandırılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın birbirinden ayrılması gereken iki nesneye bağlı kullanımını birlikte temsil eder.","boundary_detail":"Tanım yalnızca kılıç yüzeyinin parlatılması ile göz boyasının görüşü berraklaştırdığı kullanımları kapsar; genel açığa çıkarma anlamına yayılmaz.","branch_image_ar":"الصقل والتجلية","concept_gloss":"kılıcı parlatma ve göz boyasıyla görüşü berraklaştırma","contextual_glosses":[{"applicability":"Kılıç yüzeyinin işlenip temiz ve parlak hale getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Metal yüzeyinin işlenerek parlaklaştırılması işlemini eksiksiz karşılar."},"facet_ids":["F001"],"text":"kılıcı parlatmak","usage_role":"contextual"},{"applicability":"Göz boyasının görmeyi açtığı veya berraklaştırdığı tarihsel kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görüşteki berraklaşmayı ve bunun göz boyası aracılığıyla gerçekleşmesini korur."},"facet_ids":["F002"],"text":"görüşü göz boyasıyla berraklaştırmak","usage_role":"explanatory"}],"definition":"Belirli kullanımlarda kılıcın yüzeyini işleyip parlak ve temiz hale getirmeyi, başka bir kullanımda ise göze çekilen boyayla görüşü berraklaştırmayı anlatır. İki kullanım ortak bir açıklık sonucu taşır, fakat aynı işlem değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kılıcın yüzeyi işlenerek parlatılır ve temiz bir görünüm kazanır."},{"facet_id":"F002","role":"specialization","statement":"Göze çekilen belirli boya, görüşü daha berrak hale getiren madde veya uygulama olarak adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kesici ağzı keskinleştirme işlemini zorunluymuş gibi ekler.","collision":"Keskinleştirme dalıyla karışır.","fit":"displacement","loses":"Parlaklık sonucunu ve göz boyasına bağlı görüş kullanımını kaybeder.","preserves":"Kılıca uygulanan bir yüzey işlemi olmasını kısmen korur."},"text":"bileme"}],"identity_rationale":"Kaynak ifadesi kılıcı parlatma ile görüşü göz boyası aracılığıyla berraklaştırmayı birlikte verir. Dal korunabilir, ancak bunlar tek bir sınırsız parlatma anlamı değil, ayrı nesne ve uygulamalara bağlı iki gerçekleşmedir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kılıcı parlatıp temizlemek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"görüşü berraklaştırdığı kabul edilen göz boyası"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"görüşü göz boyasıyla berraklaştırmak"}],"lexicalization_note":"Kılıçla ve göz boyasıyla kurulan kullanımlar ayrı yüzey ve görüş boyutları olarak belirtilir; bunlardan bağımsız bir yalın anlam çıkarılmaz.","neighbor_coverage_note":"Adayların tümü incelendi; metal işleme çekirdeğini keskinleştirmeden ve mecazlı arınmadan, görüş kullanımını da genel açığa çıkmadan ayıran üç karşılaştırma seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kılıcın parlak ve temiz hale gelmesine odaklanır; komşu dalda kesici kenarın taşla bilenmesi ve keskinleşmesi belirleyicidir.","focus_only":"Göz boyasıyla görüşü berraklaştıran ayrı bir kullanım da taşır.","gloss":"taşla keskinleştirme ve parlatma","neighbor_only":"Bileği taşıyla kesici kenarı keskinleştirme işlemini özellikle kapsar.","neighbor_ref":"root_000750/B003","relation_type":"near_synonym","shared_zone":"İki dal da metal bir aracın yüzeyine uygulanan iyileştirici işlemi kapsar."},{"boundary_match":"partial","distinction":"Kılıç bağlamındaki çekirdek örtüşür; bu dal görüşe, komşu dal ise öğütle arındırılan kalbe doğru farklı bir kapsam genişlemesi gösterir.","focus_only":"Göz boyası yoluyla görüşün berraklaşmasını da içerir.","gloss":"kılıcı veya kalbi parlatma","neighbor_only":"Kalbin öğütlerle arındırılmasına uzanan mecazlı kullanımı vardır.","neighbor_ref":"root_000299/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda kılıcın yüzeyini parlatıp temiz hale getirme kullanımı bulunur."},{"boundary_match":"partial","distinction":"Bu dal belirli bir yüzeyi ya da görüşü işlemle berraklaştırır; komşu dalın çekirdeği örtülü olanın genel olarak görünür hale gelmesidir.","focus_only":"Nesne ve uygulama olarak kılıca ve göz boyasına bağlıdır.","gloss":"açığa çıkma","neighbor_only":"Bilgi, kaygı, hastalık ve karanlık gibi geniş alanlarda açığa çıkmayı kapsar.","neighbor_ref":"root_000256/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal açıklık veya berraklık sonucunu ortak bir anlam bağı olarak taşır."}],"source_phrase_ar":"جلوت السيف جلاء (maqayis;mufradat)؛ جلا الصيقل السيف واجتلاه (ayn;tahdhib)؛ الجلا مقصور الإثمد لأنه يجلو البصر (ayn)؛ جلوت بصري بالكحل والجلا كحل (sihah;tahdhib)","source_summary":"Kaynaklar kılıcın parlatılmasını ortak biçimde aktarır; ayrıca göz boyasının görüşü berraklaştırması ve bu amaçla kullanılan maddenin adı aynı anlam alanında verilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"تجلية السيف وصقله والكحل أو الإثمد الذي يجلو البصر","what_is_not_ar":"ليس مطلق البيان ولا الجلاء عن الأوطان"},"support_links":["sup_fb8ed09773bd4c50b7be"]},{"boundary":"Anlam düğündeki gelin gösterimine bağlıdır; genel gösterme, evlenme veya bu sırada verilen armağan dalıyla özdeş değildir.","branch_kind":"collocation","branch_ref":"root_000256/B003","candidate_links":[{"candidate_id":"cand_a11327c2c8bfde7a82db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"gelini törende gösterme veya gösterilmiş gelini görme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gelin, düğün bağlamında hazırlanıp eşine ve ilgili topluluğa görünür biçimde sunulur."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eş, gelini hazırlanıp sunulmuş olduğu sırada görür."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gelin gösteriminin hem sunan hem de gören katılımcıya göre kurulan iki kullanımını kapsar.","boundary_detail":"Anlam düğündeki gelin gösterimine bağlıdır; genel gösterme, evlenme veya bu sırada verilen armağan dalıyla özdeş değildir.","branch_image_ar":"جلوة العروس","concept_gloss":"gelini törende gösterme veya gösterilmiş gelini görme","contextual_glosses":[{"applicability":"Hazırlanmış gelinin görünür biçimde sunulduğu eylem için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelin, düğün bağlamı ve törensel gösterme eylemini birlikte korur."},"facet_ids":["F001"],"text":"gelini düğünde göstermek","usage_role":"contextual"},{"applicability":"Eşin gelini törensel sunum halindeyken gördüğü eylem için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görme eylemini, eş katılımcısını ve gelinin önceden hazırlanıp sunulmuş olmasını korur."},"facet_ids":["F002"],"text":"gösterilmiş gelini görmek","usage_role":"contextual"}],"definition":"Düğün sırasında gelinin hazırlanarak görünür biçimde sunulması ve eşinin onu bu sunulmuş halde görmesidir. Gösterme ile görme, aynı törensel durumun birbirini izleyen iki katılımcı eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gelin, düğün bağlamında hazırlanıp eşine ve ilgili topluluğa görünür biçimde sunulur."},{"facet_id":"F002","role":"associated_use","statement":"Eş, gelini hazırlanıp sunulmuş olduğu sırada görür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Gelin gösteriminden bağımsız olarak bütün evlilik kurma olayını kapsar.","collision":"Evlilik ve gelin gösterimi ayrı olaylar olduğu için sınırlar çakışır.","fit":"broadening","loses":null,"preserves":"Olayın evlilik çevresinde gerçekleşmesini korur."},"text":"evlenmek"}],"identity_rationale":"Kaynak ifadesi düğün bağlamında gelinin hazırlanıp görünür biçimde sunulmasını ve eşinin onu bu sunum sırasında görmesini açıkça iki bağlı eylem olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gelini düğünde görünür biçimde sunmak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sunulmuş gelini görmek"}],"lexicalization_note":"Tanım yalnızca gelinin düğün sırasında gösterilmesi ve gösterilmiş halde görülmesi yapısına bağlı tutulur; yalın bir gösterme anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dalı genel göstermeden, evlenme olayından ve aynı törendeki armağan verme eyleminden ayıran üç ilişki yeterli bulundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel gösterme değildir; gelinin düğündeki hazırlanmış sunumuna ve eşin onu bu halde görmesine bağlı özel bir yapıdır.","focus_only":"Gelin, düğün ve eşin görmesi biçimindeki törensel katılımcıları zorunlu kılar.","gloss":"bir şeyi gösterme","neighbor_only":"Herhangi bir nesnenin genel olarak ortaya konmasını veya gösterilmesini kapsar.","neighbor_ref":"root_000299/B006","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir şey başkasının görebileceği biçimde görünür hale getirilir."},{"boundary_match":"thematic_only","distinction":"Komşu dal evlilik bağının kurulmasına yöneliktir; bu dal ise o süreçteki belirli bir görünür sunum ve görme anını adlandırır.","focus_only":"Düğün içinde gelinin gösterilmesi ve görülmesi eylemlerini anlatır.","gloss":"evlenme ve ortak yaşama geçme","neighbor_only":"Evlilik kurmayı ve eşle ortak yaşama geçmeyi anlatır.","neighbor_ref":"root_000166/B010","relation_type":"thematic","shared_zone":"İki dal da düğün ve evlilik sürecinde yer alan olayları konu edinir."},{"boundary_match":"thematic_only","distinction":"Bu dal görsel sunum ve görme eylemidir; komşu dal bu sırada gerçekleşen verme eylemi ve verilen şeydir.","focus_only":"Gelinin sunulması ile eşin onu görmesini ifade eder.","gloss":"gelin gösteriminde verilen armağan","neighbor_only":"Aynı törensel anda eşin geline verdiği armağanı ifade eder.","neighbor_ref":"root_000256/B009","relation_type":"thematic","shared_zone":"Her iki dal aynı gelin gösterimi sahnesine ve onun katılımcılarına bağlıdır."}],"source_phrase_ar":"جلوت العروس جلوة وجلاء (maqayis;mufradat)؛ الماشطة تجلو العروس وقد جليت على زوجها واجتلاها زوجها أي نظر إليها (ayn;tahdhib)؛ جلوت العروس جلاء وجلوة واجتليتها إذا نظرت إليها مجلوة (sihah)","source_summary":"Kaynaklar gelinin törensel olarak gösterilmesini ve eşinin onu bu halde görmesini aynı düğün sahnesinin bağlı eylemleri olarak ortak biçimde aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إظهار العروس وتجليتها والنظر إليها في الجلوة","what_is_not_ar":"ليس عطية الجلوة ولا صقل السيف"},"support_links":["sup_f2913b56e6468397184d"]},{"boundary":"Yurttan ayrılma çekirdektir; zorla çıkarma ayrı katılımcı yönüdür, topluluk adı ile çevreden açılma ise bağımlı uzantılardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000256/B004","candidate_links":[{"candidate_id":"cand_bb5639e032b701b4c8c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"yerleşimden ayrılma veya çıkarılma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk yerleştiği evlerden, ülkeden veya yurttan ayrılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi veya yönetim, topluluğu yerleşiminden çıkarır ve ayrılmasına neden olur."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yurdundan ayrılıp başka yere yerleşen veya yönetim koruması altında özel vergi yükümlüsü olan topluluk bu anlam ailesindeki bir adla anılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir şeyin ya da öldürülmüş kişinin çevresinde toplananlar yanından açılıp dağılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın topluluğun kendisinin ayrılması ile bir yetkenin onu çıkarması biçimindeki temel karşıt katılımcı yönlerini kapsar.","boundary_detail":"Yurttan ayrılma çekirdektir; zorla çıkarma ayrı katılımcı yönüdür, topluluk adı ile çevreden açılma ise bağımlı uzantılardır.","branch_image_ar":"الجلاء عن الوطن","concept_gloss":"yerleşimden ayrılma veya çıkarılma","contextual_glosses":[{"applicability":"Bir topluluğun kendi yurdundan veya yerleşiminden çıkması anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun yerleşiminden ayrılan katılımcı olmasını ve yurt bağını korur."},"facet_ids":["F001"],"text":"yurdundan ayrılmak","usage_role":"contextual"},{"applicability":"Bir yetkenin topluluğu yerleşiminden ayrılmaya zorladığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çıkaran kişi ile çıkarılan topluluk arasındaki ettirgen katılımcı ayrımını korur."},"facet_ids":["F002"],"text":"yurdundan çıkarmak","usage_role":"contextual"},{"applicability":"Bir şeyin çevresinde toplanmış kişilerin yanından çekilip aralık verdiği özel kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Önceki kuşatma veya toplanma durumundan sonra çevrenin açılmasını korur."},"facet_ids":["F004"],"text":"çevresinden açılıp dağılmak","usage_role":"explanatory"}],"definition":"Bir topluluğun yerleşiminden veya yurdundan ayrılması ya da bir yetkenin onları oradan çıkarmasıdır. Aynı anlam ailesinde yurdundan ayrılmış topluluk adı ile çevresine toplanılmış bir şeyin yanından açılıp dağılma kullanımı da bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk yerleştiği evlerden, ülkeden veya yurttan ayrılır."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi veya yönetim, topluluğu yerleşiminden çıkarır ve ayrılmasına neden olur."},{"facet_id":"F003","role":"extension","statement":"Yurdundan ayrılıp başka yere yerleşen veya yönetim koruması altında özel vergi yükümlüsü olan topluluk bu anlam ailesindeki bir adla anılır."},{"facet_id":"F004","role":"associated_use","statement":"Bir şeyin ya da öldürülmüş kişinin çevresinde toplananlar yanından açılıp dağılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasını zorla çıkarma ile bir şeyin çevresinden açılıp dağılma kullanımlarını karşılamaz.","preserves":"Bir topluluğun yurdundan ayrılıp başka yere yönelmesini korur."},"text":"göç"}],"identity_rationale":"Kaynak ifadesinin ana bölümü bir topluluğun yurdundan ayrılması veya çıkarılmasıdır; ayrıca yurdundan ayrılmış topluluk adını ve çevresine toplanılmış bir şeyin yanından açılıp dağılmayı da içerir. Bu son kullanım, yalnızca yurt çerçevesine indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yurttan veya yerleşimden ayrılma"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"onları ülkeden çıkarmak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yurdundan ayrılmış topluluk; yönetim korumasında özel vergi ödeyen topluluk"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"çevresinde toplanılan şeyin yanından açılıp dağılmak"}],"lexicalization_note":"Yurttan ayrılma, başkasını çıkarma, ayrılan topluluk ve çevrelenmiş şeyden açılma biçimleri ayrı tutulur; tek bir sınırsız uzaklaşma anlamında eritilmez.","neighbor_coverage_note":"Tüm adaylar gözden geçirildi; yurt ve topluluk sınırını genel uzaklaştırmadan, yük indirmeden ve dışlayıcı kovmadan ayıran üç yakın komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İnsanları ülkeden çıkarma alanında güçlü örtüşme vardır; bu dal ayrıca çıkıp gitme sonucunu ve topluluk adını, komşu dal ise yükü yerinden alma kullanımını taşır.","focus_only":"Topluluğun kendiliğinden ayrılmasını ve ayrılan topluluğun adlandırılmasını da kapsar.","gloss":"yerinden çıkarma","neighbor_only":"Bir yükün hayvanın sırtından indirilmesi gibi nesneye yönelik uzaklaştırmayı da kapsar.","neighbor_ref":"root_000769/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiyi veya topluluğu bulunduğu yerden çıkarıp uzaklaştırmayı anlatır."},{"boundary_match":"partial","distinction":"Bu dal yerleşim ve yurt bağında toplu ayrılma ya da çıkarılmadır; komşu dalın yer ve katılımcı sınırı daha geniştir.","focus_only":"Yurt ve topluluk ölçeğini, ayrıca ayrılan tarafın kendi hareketini öne çıkarır.","gloss":"birini yerinden uzaklaştırma","neighbor_only":"Bir kişiyi herhangi bir yerden kaldırıp başka yere gönderme kapsamı daha geneldir.","neighbor_ref":"root_000551/B007","relation_type":"near_synonym","shared_zone":"Her iki dalda bir insan veya topluluk bulunduğu yerden ayrılmaya sevk edilir."},{"boundary_match":"partial","distinction":"Bu dalda topluluğun yurttan çıkışı ve çıkarılması birlikte kodlanır; komşu dal dışlayıcı kovma ve uzak tutma eylemine daha sıkı bağlıdır.","focus_only":"Ayrılan topluluğun kendi çıkışını ve çevreden açılma uzantısını da içerir.","gloss":"kovup uzaklaştırma","neighbor_only":"Kovma, dışlama ve sürgün edilen kişiyi uzak tutma sonucunu özellikle içerir.","neighbor_ref":"root_000930/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi veya topluluğun bulunduğu yerden zorla çıkarılmasını kapsar."}],"source_phrase_ar":"جلا القوم عن منازلهم جلاء وأجليتهم (maqayis)؛ الجلاء أن يجلو قوم عن بلادهم والجالية أهل الذمة (ayn)؛ الجلاء الخروج من البلد والجالية الذين جلوا عن أوطانهم (sihah)؛ أجليت القوم عن منازلهم فجلوا عنها أي أبرزتهم عنها (mufradat)","source_summary":"Kaynaklar bir topluluğun yurdundan çıkması ile başkası tarafından çıkarılması arasındaki katılımcı ayrımını korur; yurdundan ayrılan topluluk adını ve bir şeyin çevresinden açılmayı da aynı alana bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"خروج القوم من المنازل والأوطان وإخراجهم منها وما يتصل بالجالية","what_is_not_ar":"ليس انكشاف الخبر ولا انجلاء الهم"},"support_links":["sup_d963a133807003af2ab9"]},{"boundary":"Dal doğal veya durum bildiren ön saç açıklığıyla sınırlıdır; saçın kesilmesi, bütün başın saçsızlığı ya da genel görünürlük anlamı değildir.","branch_kind":"bare","branch_ref":"root_000256/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"ön saç çizgisinin gerilemesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Saç başın ön kısmından çekilir ve ön saç çizgisi geriler."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ön başta saçın çekildiği açık bölgeler ve bu görünüşe sahip kişi adlandırılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın başın ön bölümündeki saçın çekilip deriyi açığa çıkarması biçimindeki çekirdeğini karşılar.","boundary_detail":"Dal doğal veya durum bildiren ön saç açıklığıyla sınırlıdır; saçın kesilmesi, bütün başın saçsızlığı ya da genel görünürlük anlamı değildir.","branch_image_ar":"انكشاف مقدّم الرأس","concept_gloss":"ön saç çizgisinin gerilemesi","contextual_glosses":[{"applicability":"Bir kişinin ön saç çizgisinin gerileyerek alnının daha açık görünmesi anlatıldığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişideki ön saç gerilemesini ve bunun görünür sonucunu doğal bir ifadeyle korur."},"facet_ids":["F001","F002"],"text":"alnı açılmak","usage_role":"contextual"}],"definition":"Saçın başın ön kısmından çekilerek ön saç çizgisinin gerilemesi ve bu bölgede baş derisinin açığa çıkmasıdır. Bu görünüşe sahip kişi ve saçsızlaşan ön bölgeler de aynı alan içinde adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Saç başın ön kısmından çekilir ve ön saç çizgisi geriler."},{"facet_id":"F002","role":"extension","statement":"Ön başta saçın çekildiği açık bölgeler ve bu görünüşe sahip kişi adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Saç kaybını başın ön kısmıyla sınırlamayıp bütün başa yayar.","collision":"Genel saçsızlık anlamıyla karışır.","fit":"broadening","loses":null,"preserves":"Saç kaybı ve baş derisinin görünür olması sonucunu korur."},"text":"kel olmak"}],"identity_rationale":"Kaynak ifadesi saçın başın ön bölümünden çekilmesini, ön saç çizgisinin açılmasını ve bu görünüşe sahip kişiyi açıkça aynı çekirdekte birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ön saçları çekilmiş kişi; ön saçların çekilmesi"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"geniş ve güzel alın"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"başın ön kısımları ve saçsız bölgeleri"}],"lexicalization_note":"Tanım yalın dalın ön başta saçın çekilmesi çekirdeğini verir; geniş ve güzel alın gibi ayrı bir sözcük kullanımını çekirdeğe taşımaz.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; ön baş sınırını şakak açılmasından, genel saçsızlıktan ve kesme eyleminden ayıran üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal ön baştaki açılmayı genel olarak kapsar; komşu dal gerilemeyi özellikle alnın iki yanındaki şakak girintilerine bağlar.","focus_only":"Ön saç çizgisinin orta bölümü dahil genel ön kısmındaki gerilemeyi kapsar.","gloss":"şakaklardan saç çekilmesi","neighbor_only":"Saçın özellikle alnın iki yanından çekilmesini ve bu iki girintiyi öne çıkarır.","neighbor_ref":"root_001489/B007","relation_type":"near_synonym","shared_zone":"İki dal da ön saç çizgisinin gerileyip alın çevresini açık bırakmasını anlatır."},{"boundary_match":"partial","distinction":"Bu dal ön saç çizgisindeki gerileme durumudur; komşu dal ise saçın bilinçli bir işlemle kesilmesi veya kazınmasıdır.","focus_only":"Saçın durum veya nitelik olarak ön kısımdan çekilmiş olmasını anlatır.","gloss":"saçı kesip kazıma","neighbor_only":"Saçı bir araçla kesme veya kazıma eylemini ve bunun ürünlerini kapsar.","neighbor_ref":"root_000350/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalın sonucunda başın bir bölümü saçtan arınmış ve açık görünebilir."},{"boundary_match":"partial","distinction":"Bu dalın bölgesel sınırı ön baştır; komşu dal genel saçsızlığa ve saç dışındaki boşluk ya da çıplaklık durumlarına uzanır.","focus_only":"Saç kaybını özellikle başın ön kısmına ve ön saç çizgisine bağlar.","gloss":"saçsızlık ve çıplaklık","neighbor_only":"Bütün başta saçsızlık yanında boş, çıplak veya örtüsüz başka alanlara da genişler.","neighbor_ref":"root_001219/B008","relation_type":"near_synonym","shared_zone":"İki dal da saçın yokluğu nedeniyle baş derisinin açık kalmasını kapsar."}],"source_phrase_ar":"رجل أجلى إذا ذهب شعر مقدم رأسه وهو الجلا (maqayis)؛ الجبهة الجلواء والرجل أجلى (ayn)؛ انحسار مقدم الرأس (jamhara)؛ الجلاء انحسار الشعر عن مقدم الرأس والمجالي مقادم الرأس (sihah)؛ فهو أجلى مع الجلا (tahdhib)؛ رجل أجلى انكشف بعض رأسه عن الشعر (mufradat)","source_summary":"Kaynaklar başın önündeki saçın çekilmesini ve bu nedenle derinin görünür olmasını ortak çekirdek sayar; kişi niteliğini ve ön baştaki saçsız bölgeleri buna bağlar.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"ذهاب الشعر عن مقدمة الرأس أو مواضع الصلع حتى يقال رجل أجلى","what_is_not_ar":"ليس انكشاف الأمر ولا الجلاء عن الوطن"},"support_links":[]},{"boundary":"Anlam kalıplaşmış kişi nitelemesine bağlıdır; genel görünürlük, geçici dikkat çekme veya yalnızca bir ad taşıma anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000256/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"adı ve konumu herkesçe bilinen kişi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi yaygın ünü nedeniyle herkesçe tanınır ve durumu gizli kalmaz."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, kişinin yüksek saygınlığını ve toplum içindeki belirgin yerini de anlatabilir."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıplaşmış nitelemenin ün ve yüksek konumdan doğan tanınmışlık çekirdeğini karşılar.","boundary_detail":"Anlam kalıplaşmış kişi nitelemesine bağlıdır; genel görünürlük, geçici dikkat çekme veya yalnızca bir ad taşıma anlamı değildir.","branch_image_ar":"الشهرة وابن جلا","concept_gloss":"adı ve konumu herkesçe bilinen kişi","contextual_glosses":[{"applicability":"Bir kişinin hem ününün hem de yüksek toplumsal yerinin vurgulandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaygın tanınmışlık ile yüksek saygınlığı tek bir doğal kişi nitelemesinde birleştirir."},"facet_ids":["F001","F002"],"text":"herkesçe tanınan seçkin kişi","usage_role":"contextual"}],"definition":"Sabit bir övgü sözünde, ünü ve yüksek toplumsal konumu herkesçe bilinen, kim olduğu veya değeri gizli kalmayan kişi anlatılır. Açıklık burada kişinin durumunun yaygın biçimde tanınmasına dönüşmüştür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi yaygın ünü nedeniyle herkesçe tanınır ve durumu gizli kalmaz."},{"facet_id":"F002","role":"specialization","statement":"Niteleme, kişinin yüksek saygınlığını ve toplum içindeki belirgin yerini de anlatabilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kalıplaşmış övgü niteliğini ve yüksek toplumsal konum vurgusunu tek başına taşımaz.","preserves":"Kişinin geniş çevrede tanınmasını korur."},"text":"ünlü"}],"identity_rationale":"Kaynak ifadesi sabit bir övgü sözünü, sahibinin ünü, açıkça bilinen durumu ve yüksek toplumsal konumu üzerinden açıklar; bu nedenle dal sıradan bir kişi adı değil, tanınmışlık bildiren kalıplaşmış nitelemedir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"herkesçe tanınan, durumu gizli olmayan kişi"}],"lexicalization_note":"Tanım yalnızca ünü ve yüksek konumu gizli kalmayan kişi için kullanılan sabit nitelemeyi açıklar; bağımsız bir yalın kök anlamı üretmez.","neighbor_coverage_note":"Adayların tamamı incelendi; kalıplaşmış olumlu kişi nitelemesini genel ün sonucundan, iyi anılma alanından ve kamuya yayılmadan ayıran üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal tanınmış ve yüksek konumlu kişiye yönelik kalıplaşmış bir övgüdür; komşu dal ünün oluşmuş bir toplumsal sonuç olmasına odaklanır.","focus_only":"Belirli bir kişiyi yüksek konumuyla birlikte öven sabit nitelemeye bağlıdır.","gloss":"ün salmış olma","neighbor_only":"Bir kişi veya topluluğun sonunda dillere düşen ün haline gelmesini daha genel anlatır.","neighbor_ref":"root_000500/B004","relation_type":"near_synonym","shared_zone":"Her iki dal bir kişi veya topluluğun durumunun geniş çevrede bilinmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal ün sahibi kişiye verilen belirli nitelemedir; komşu dal kişinin iyi ününü ve övülmesini bağımsız kavramlar olarak anlatır.","focus_only":"Durumu gizli kalmayan kişiyi belirli bir sabit sözle niteler.","gloss":"iyi ün ve saygınlık","neighbor_only":"İyi anılma, övgü, ün ve saygınlığın kendisini daha geniş bir ad alanı olarak kapsar.","neighbor_ref":"root_000516/B007","relation_type":"near_synonym","shared_zone":"İki dal da kişinin toplumda tanınması ve yüksek değer görmesi alanında örtüşür."},{"boundary_match":"partial","distinction":"Bu dal olumlu tanınmış kişiyi niteler; komşu dal ünün yayılma sürecine ve olumlu olmayan duyurma biçimlerine kadar genişler.","focus_only":"Yüksek konumu bilinen kişi için olumlu ve kalıplaşmış bir nitelemedir.","gloss":"ün ve kamuya yayılma","neighbor_only":"Ünün yayılması yanında gösteriş yapma ve birini kötü biçimde duyurma kullanımlarını da kapsar.","neighbor_ref":"root_000741/B005","relation_type":"near_neighbor","shared_zone":"Her ikisinde de kişinin adının veya durumunun insanlar arasında yaygın biçimde bilinmesi vardır."}],"source_phrase_ar":"هو ابن جلا إذا كان لا يخفى أمره لشهرته (maqayis)؛ أنا ابن جلا أي أنا ابن الواضح الأمر المشهور (ayn)؛ الجلا الأمر الواضح المكشوف وأنا ابن جلا (jamhara)؛ كأنه يقال له جلا الأمور وكشفها (sihah)؛ هو ابن جلا للرجل إذا كان عالي الشرف لا يخفى مكانه (tahdhib)؛ فلان ابن جلا أي مشهور (mufradat)","source_summary":"Kaynaklar kalıplaşmış nitelemenin ünü nedeniyle durumu gizli olmayan kişiyi anlattığında birleşir; yüksek saygınlık ve toplumdaki belirgin yer bu tanınmışlığın özel bir yönüdür.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الشهرة التي لا يخفى صاحبها والمثل ابن جلا وما يجري مجراه من وضوح الأمر","what_is_not_ar":"ليس اسما مجردا ولا جلاء الوطن"},"support_links":[]},{"boundary":"Dal doğal gök ve gündüz açıklığıyla sınırlıdır; genel bilgi açıklığı, metal parlaklığı veya yalnızca tek bir ışık kaynağının parıltısı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000256/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"açık gök ve aydınlanan gündüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gök bulutsuz, açık ve duru bir görünüm kazanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Gündüz aydınlığı yayılır, güneşi ve çevreyi görünür hale getirir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir gündüzlük beyaz aydınlık veya ertesi günün kuşluk vaktine uzanan süre adlandırılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın gökteki açıklık ile gündüz ışığının görünür kılıcı yayılımını birlikte temsil eder.","boundary_detail":"Dal doğal gök ve gündüz açıklığıyla sınırlıdır; genel bilgi açıklığı, metal parlaklığı veya yalnızca tek bir ışık kaynağının parıltısı değildir.","branch_image_ar":"بياض اليوم وصفاء الجو","concept_gloss":"açık gök ve aydınlanan gündüz","contextual_glosses":[{"applicability":"Göğün bulutlardan arınıp açık ve duru hale geldiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Göğün kapalı durumdan bulutsuz ve açık duruma geçmesini doğal biçimde karşılar."},"facet_ids":["F001"],"text":"gök açıldı","usage_role":"contextual"},{"applicability":"Gündüz ışığının yayılıp güneşi ve çevreyi görünür kıldığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzün yayılan ışıkla görünürlüğü sağlamasını korur."},"facet_ids":["F002"],"text":"gündüz ortalığı aydınlattı","usage_role":"contextual"}],"definition":"Göğün bulutlardan arınmış ve açık olması ile gündüz aydınlığının yayılıp güneşi ve çevreyi görünür kılmasıdır. Bir günlük aydınlık süre de bu doğal açıklık alanında adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gök bulutsuz, açık ve duru bir görünüm kazanır."},{"facet_id":"F002","role":"specialization","statement":"Gündüz aydınlığı yayılır, güneşi ve çevreyi görünür hale getirir."},{"facet_id":"F003","role":"extension","statement":"Bir gündüzlük beyaz aydınlık veya ertesi günün kuşluk vaktine uzanan süre adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Gök ve gündüz sınırı olmadan her türlü ışıklı veya yansıtıcı görünümü kapsar.","collision":"Metal yüzeyi ve tekil ışık kaynaklarıyla karışabilir.","fit":"broadening","loses":null,"preserves":"Işık ve yüksek görünürlük sonucunu korur."},"text":"parlaklık"}],"identity_rationale":"Kaynak ifadesi bulutsuz ve açık göğü, bir gündüzlük aydınlık süreyi ve gündüzün güneşi görünür kılmasını aynı doğal aydınlanma alanında verir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"bulutsuz, açık gök"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"bir gündüzlük aydınlık süre"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"gündüzün güneşi belirginleştirmesi"}],"lexicalization_note":"Açık gök, bir günlük aydınlık süre ve gündüzün güneşi belirginleştirmesi ayrı yapılara bağlı tutulur; bunlardan sınırsız bir yalın parlaklık anlamı çıkarılmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; gündüz ve açık gök sınırını kuşluk aydınlığından, gökteki tekil beyazlıktan ve belirli ışık kaynaklarından ayıran üç ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal açık gök ve gündüzün yayılışına bağlıdır; komşu dal kuşluk ışığına odaklanır ve gece ile renk alanına da uzanır.","focus_only":"Bulutsuz göğü ve gündüzün güneşi görünür kılan yayılımını birlikte kapsar.","gloss":"kuşluk aydınlığı ve duruluk","neighbor_only":"Kuşluk ışığını, aydınlık geceyi ve hayvan donundaki açık rengi de kapsar.","neighbor_ref":"root_000904/B005","relation_type":"near_synonym","shared_zone":"İki dal gündüz ışığının berrak, açık ve görünürlüğü artıran niteliğinde örtüşür."},{"boundary_match":"partial","distinction":"Bu dal göğün genel durumu ve gündüz ışığıdır; komşu dal gök içinde yer alan belirli bir beyazlık unsurudur.","focus_only":"Göğün bütün olarak açık olmasını ve gündüz aydınlığını anlatır.","gloss":"gökteki beyazlık","neighbor_only":"Gökte seçilen belirli bir beyazlık oluşumunu adlandırır.","neighbor_ref":"root_001331/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal gökte görülen beyazlık ve açıklık izlenimiyle ilişkilidir."},{"boundary_match":"field_only","distinction":"Bu dal yayılmış gündüz açıklığıdır; komşu dal tekil gök cisimleri veya şimşekten çıkan ışığın kendisine odaklanır.","focus_only":"Gök durumunu ve gündüzün yayılmış aydınlığını anlatır.","gloss":"şimşek ve ay ışığı","neighbor_only":"Şimşek, ay ve dolunay gibi belirli kaynakların ışığını anlatır.","neighbor_ref":"root_000751/B004","relation_type":"same_field","shared_zone":"İki dal göksel ışık ve karanlığın azalması alanında buluşur."}],"source_phrase_ar":"السماء جلواء أي مصحية (maqayis;sihah;mufradat)؛ جلاء يوم واحد أي بياض يوم (ayn;tahdhib)؛ والنهار إذا جلاها إذا بين الشمس (tahdhib)","source_summary":"Kaynaklar açık göğü ve gündüzün aydınlık görünümünü ortak doğal açıklık alanında toplar; gündüzün güneşi belirginleştirmesi ile bir günlük aydınlık süre bu alanın bağlı kullanımlarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"بياض اليوم وصفاء السماء وانبساط النهار الذي يكشف الظلمة","what_is_not_ar":"ليس البيان الحقوقي ولا الجلاء عن الوطن"},"support_links":[]},{"boundary":"Dal belirli bakış ve baş yöneltme biçimleriyle sınırlıdır; gelini görme, göze boya çekme veya her türlü sıradan bakma anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_000256/B008","candidate_links":[{"candidate_id":"cand_a11327c2c8bfde7a82db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"başı kaldırıp bakışı hedefe yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bakan, hedefi fark edince başını ve gözlerini ona doğru kaldırıp bakışını yöneltir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Av kuşu, gördüğü avı yakından izlemek üzere bakışını ona diker."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir şeye yüksekten gözeterek veya beklentiyle yönelmiş biçimde bakılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bedensel yönelmeyi ve hedefe dikilen bakışı birlikte içeren çekirdeğini karşılar.","boundary_detail":"Dal belirli bakış ve baş yöneltme biçimleriyle sınırlıdır; gelini görme, göze boya çekme veya her türlü sıradan bakma anlamı değildir.","branch_image_ar":"النظر المتطلع","concept_gloss":"başı kaldırıp bakışı hedefe yöneltme","contextual_glosses":[{"applicability":"Bir av kuşunun başını kaldırıp bakışını avına yönelttiği bağlam için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Av hedefini, odaklı izlemeyi ve bakışın ona yönelmesini korur."},"facet_ids":["F002"],"text":"avı gözleriyle süzmek","usage_role":"contextual"},{"applicability":"Bir şeye yukarıdan, gözetleyici veya beklentili biçimde bakıldığı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yüksek konumu ve dikkatle hedefe yönelmiş bakışı korur."},"facet_ids":["F003"],"text":"yüksekten gözeterek bakmak","usage_role":"explanatory"}],"definition":"Bir hedefi, özellikle avı, fark edince başı ve gözleri ona doğru kaldırıp bakışı hedefe yöneltmektir. Kullanım ayrıca yüksek bir konumdan gözeterek veya beklentiyle bir şeye bakmayı kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bakan, hedefi fark edince başını ve gözlerini ona doğru kaldırıp bakışını yöneltir."},{"facet_id":"F002","role":"specialization","statement":"Av kuşu, gördüğü avı yakından izlemek üzere bakışını ona diker."},{"facet_id":"F003","role":"extension","statement":"Bir şeye yüksekten gözeterek veya beklentiyle yönelmiş biçimde bakılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Başın kaldırılması, hedefe dikilme ve gözetleme koşulu olmadan her türlü görsel yönelmeyi kapsar.","collision":"Sıradan görme ve bakma eylemleriyle karışır.","fit":"broadening","loses":null,"preserves":"Gözlerin bir şeye yönelmesi temelini korur."},"text":"bakmak"}],"identity_rationale":"Kaynak ifadesi bir av kuşunun avı sezince başını ve gözünü kaldırıp ona yöneltmesini, bakışı hedefe atar gibi çevirmesini ve yüksekten gözeterek bir şeye bakmayı aynı yönelmiş bakış çekirdeğinde verir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"başı ve gözleri kaldırıp bakışı ava yöneltmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bir şeye gözeterek ve beklentiyle bakmak"}],"lexicalization_note":"Tanım yalnızca başı ve bakışı hedefe kaldırma, avı süzme ve yüksekten gözeterek bakma biçimlerini kapsar; yalın bir görme anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar incelendi; hedefe kaldırılan tek odaklı bakışı uzun bakıştan, korkuyla donan gözden ve ikiye bölünmüş bakıştan ayıran üç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal baş ve bakışın hedefe kaldırılmasıyla özellikle avı gözetmeye bağlıdır; komşu dal bakışın süresini ve kesintisizliğini öne çıkarır.","focus_only":"Başın kaldırılmasını, av hedefini ve yüksekten gözetme biçimini öne çıkarır.","gloss":"gözünü dikip uzun süre bakma","neighbor_only":"Gözleri açık tutarak uzun süre bakmayı ve bakışı aşağı çevirmeyi de kapsar.","neighbor_ref":"root_001594/B001","relation_type":"near_synonym","shared_zone":"İki dal da gözlerin belirli bir hedefe yoğun ve sürekli biçimde yönelmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal hedefe yönelik gözetleyici eylemdir; komşu dal korku veya şaşkınlığın istemsiz sonucu olan donuk bakıştır.","focus_only":"Hedefi izlemek için bilinçli biçimde baş ve göz yöneltmeyi anlatır.","gloss":"şaşkınlıktan donup kalan bakış","neighbor_only":"Şaşkınlık veya korku nedeniyle gözün donması ve kırpılmaması durumunu anlatır.","neighbor_ref":"root_000108/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda bakış güçlü biçimde bir noktaya yönelmiş ve belirgin hale gelmiştir."},{"boundary_match":"partial","distinction":"Bu dal tek hedefe yoğunlaşmadır; komşu dal gözlerin aynı anda iki farklı yöne veya kişiye bakıyor görünmesini anlatır.","focus_only":"Bakışı tek bir av veya hedef üzerinde toplar.","gloss":"iki yöne bölünen bakış","neighbor_only":"Bakışı iki ayrı kişi veya yön arasında bölünmüş gösterir.","neighbor_ref":"root_000794/B004","relation_type":"near_neighbor","shared_zone":"İki dal da bakışın yönü ve hedeflerle kurduğu ilişkiyi özel olarak anlatır."}],"source_phrase_ar":"البازي يجلي إذا آنس الصيد فرفع طرفه ورأسه وتجليت الشيء نظرت إليه (ayn)؛ جلى ببصره تجلية إذا رمى به كما ينظر الصقر إلى الصيد (sihah)؛ التجلي النظر بالأشراف (tahdhib)","source_summary":"Kaynaklar bakışın hedefe güçlü biçimde yönelmesini ortaklaştırır; av kuşunun başını ve gözünü kaldırması, bakışı avına dikmesi ve yüksekten gözeterek bakma bu yönelmenin belirtileridir.","sources":["AY","SI","TA"],"what_is_ar":"النظر إلى الشيء ورفع الطرف والرأس نحوه كما في الصائد أو البازي","what_is_not_ar":"ليس جلوة العروس ولا كحل البصر"},"support_links":["sup_f2913b56e6468397184d"]},{"boundary":"Anlam gelin gösterimi sırasındaki armağana bağlıdır; genel armağan, evlilik bedeli, ücret veya gelini görme eylemi değildir.","branch_kind":"collocation","branch_ref":"root_000256/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","surface_ar":"تَجَلَّىٰ"}],"gloss":"gelin gösteriminde verilen armağan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eş, gelinin törensel gösterimi sırasında ona bir hizmetçi armağan eder."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu törensel anda verilen armağanın kendisi de aynı kullanımla adlandırılır."}}],"root_ar":"ج ل و","root_id":"root_000256","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın düğündeki belirli zaman, veren ve alan katılımcılarıyla sınırlı armağan çekirdeğini karşılar.","boundary_detail":"Anlam gelin gösterimi sırasındaki armağana bağlıdır; genel armağan, evlilik bedeli, ücret veya gelini görme eylemi değildir.","branch_image_ar":"عطية الجلوة","concept_gloss":"gelin gösteriminde verilen armağan","contextual_glosses":[{"applicability":"Eşin gelinin törensel sunumu sırasında ona armağan verdiği eylem için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Veren ile alanı, gelin gösterimi zamanını ve armağan eylemini korur."},"facet_ids":["F001"],"text":"gelin gösteriminde armağan vermek","usage_role":"contextual"}],"definition":"Eşin, gelinin törensel olarak gösterildiği sırada ona bir hizmetçi armağan etmesi ve bu olaya bağlı armağandır. Belirleyici olan, armağanın genel niteliği değil verilme zamanı ve düğündeki katılımcılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eş, gelinin törensel gösterimi sırasında ona bir hizmetçi armağan eder."},{"facet_id":"F002","role":"extension","statement":"Bu törensel anda verilen armağanın kendisi de aynı kullanımla adlandırılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Evlilik öncesi anlaşmaya veya aileye yapılan zorunlu ödemeyi çağrıştırır.","collision":"Evlilik bedeli alanıyla karışır.","fit":"displacement","loses":"Gelin gösterimi anını, geline yönelen armağanı ve hizmetçi örneğini kaybeder.","preserves":"Evlilik çevresinde bir değer aktarılması yönünü korur."},"text":"başlık parası"}],"identity_rationale":"Kaynak ifadesi eşin, gelinin törensel olarak gösterildiği sırada ona bir hizmetçi armağan etmesini ve bu armağanın adını açıkça bildirir; eylem, görme veya gelini gösterme değil verme olayıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"eşinin gelin gösterimi sırasında ona bir hizmetçi armağan etmesi"}],"lexicalization_note":"Tanım eşin gelin gösterimi sırasında belirli bir armağan vermesi yapısına bağlı tutulur; bağımsız ve genel bir verme anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel törensel armağanı genel bağıştan, incelik armağanından, evlilik bedelinden ve aynı sahnedeki gösterim eyleminden ayıran dört ilişki yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın katılımcıları ve törensel zamanı sabittir; komşu dal armağanın incelik ve sevgi değerini öne çıkaran genel bir alandır.","focus_only":"Gelin gösterimi sırasında eşten geline verilen belirli armağanla sınırlıdır.","gloss":"incelikli armağan","neighbor_only":"Sevgi göstergesi olarak sunulan her türlü değerli ve hoş armağanı kapsar.","neighbor_ref":"root_001356/B003","relation_type":"near_synonym","shared_zone":"İki dal da karşılık beklenmeden birine değerli bir şey vermeyi anlatır."},{"boundary_match":"partial","distinction":"Bu dal düğündeki özel armağandır; komşu dalın karşılıksız verme çekirdeği olay, alıcı ve nesne bakımından daha geniştir.","focus_only":"Armağanı gelin gösterimi anına ve eşler arasındaki belirli verme olayına bağlar.","gloss":"karşılıksız bağış","neighbor_only":"Karşılıksız bağışı farklı kişilere ve durumlara genişletir.","neighbor_ref":"root_001481/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda veren, karşılığında eşdeğer bir ödeme beklemeden bir şey aktarır."},{"boundary_match":"field_only","distinction":"Bu dal gösterim anındaki armağandır ve törensel bir ek niteliğindedir; komşu dal evlilik anlaşmasına bağlı temel mali haktır.","focus_only":"Gelin gösterimi sırasında verilen törensel ve ek armağanı anlatır.","gloss":"evlilik bedeli","neighbor_only":"Evlilik kurulurken kadına bağlanan evlilik bedelini anlatır.","neighbor_ref":"root_000852/B007","relation_type":"same_field","shared_zone":"İki dal evlilik bağlamında kadına yönelen maddi değer aktarımıyla ilgilidir."},{"boundary_match":"thematic_only","distinction":"Bu dal o sahnedeki armağan aktarımıdır; komşu dal ise gelinin sunulması ve görülmesi eylemleridir.","focus_only":"Törensel anda geline verilen şeyi ve verme eylemini anlatır.","gloss":"gelinin törensel gösterimi","neighbor_only":"Gelinin görünür biçimde sunulmasını ve eşin onu görmesini anlatır.","neighbor_ref":"root_000256/B003","relation_type":"thematic","shared_zone":"Her iki dal aynı gelin gösterimi olayını, eşi ve gelini ortak sahne olarak taşır."}],"source_phrase_ar":"جلاها زوجها وصيفا أي أعطاها وما جلوتها بالكسر (sihah)؛ جلى فلان امرأته وصيفا حين اجتلاها أي أعطاها وصيفا عند جلوتها وما جلوتها بالكسر (tahdhib)","source_summary":"Kaynaklar eşin gelin gösterimi sırasında geline bir hizmetçi vermesini ortak biçimde aktarır ve aynı biçimi bu özel törensel armağan için de kullanır.","sources":["SI","TA"],"what_is_ar":"ما يعطى عند جلوة العروس ويقال جلاها زوجها وصيفا وما جلوتها","what_is_not_ar":"ليس النظر إلى العروس ولا صقل السيف"},"support_links":[]},{"boundary":"Dal, aydınlık zaman dilimini veya genel açma eylemini değil, su yatağını ve ona bağlı kullanımları kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B001","candidate_links":[{"candidate_id":"cand_f36155fd60af20406c62","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"bol su taşıyan doğal akarsu yatağı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taşkın ya da bol suyu taşıyan ve toprağı yararak belirginleşen doğal bir su yatağıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Suyun arazide akması ve bu akışla kendine bir yatak açması anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Su yatağının kendine sağlam ve yerleşik bir güzergah edinmesi yapı bağlı bir kullanımdır."}},{"facet_id":"F004","role":"specialization","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Suyun kazıp oluşturduğu belirli yatak yeri de bu dal içinde adlandırılır."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kuyu kazısının yer altındaki su düzeyine ulaşması, suya varma sonucunu bildiren bağlı bir kullanımdır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın çekirdeğini, hem akan suyu taşıma hem de toprağı yararak oluşmuş yatak olma yönleriyle karşılar.","boundary_detail":"Dal, aydınlık zaman dilimini veya genel açma eylemini değil, su yatağını ve ona bağlı kullanımları kapsar.","branch_image_ar":"نهر يشق الأرض بماء جار","concept_gloss":"bol su taşıyan doğal akarsu yatağı","contextual_glosses":[{"applicability":"Suyun arazide ilerleyerek kendi akış yolunu oluşturduğu yapı bağlı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Akışı ve akış sonucunda bir su yatağı oluşmasını birlikte korur."},"facet_ids":["F002"],"text":"su akıp kendine yatak açtı","usage_role":"contextual"},{"applicability":"Kuyu kazısının yer altındaki su düzeyine vardığını anlatan özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kazma sürecinin suya ulaşmasıyla tamamlanan sonucu açıkça korur."},"facet_ids":["F005"],"text":"kazı suya ulaştı","usage_role":"contextual"}],"definition":"Yeryüzünü yararak açılmış, taşkın ya da bol suyu taşıyan doğal su yatağıdır. Yapıya bağlı kullanımlarda suyun akıp kendine yatak açması, yatağın sağlam bir güzergah edinmesi ve kazının suya ulaşması anlatılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taşkın ya da bol suyu taşıyan ve toprağı yararak belirginleşen doğal bir su yatağıdır."},{"facet_id":"F002","role":"specialization","statement":"Suyun arazide akması ve bu akışla kendine bir yatak açması anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Su yatağının kendine sağlam ve yerleşik bir güzergah edinmesi yapı bağlı bir kullanımdır."},{"facet_id":"F004","role":"specialization","statement":"Suyun kazıp oluşturduğu belirli yatak yeri de bu dal içinde adlandırılır."},{"facet_id":"F005","role":"extension","statement":"Kuyu kazısının yer altındaki su düzeyine ulaşması, suya varma sonucunu bildiren bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi, taşkın ya da bol suyun aktığı yatağı; bu yatağın toprağı yarmasını ve suyun akarak kendine yol açmasını aynı dalda açıkça birleştirir. Kuyu kazısında suya ulaşma ve yatağın yerleşmesi ise bu çekirdeğe bağlı özel kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"taşkın suyun aktığı doğal akarsu yatağı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"akarsu yatakları"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"akarsular veya akarsu yatakları"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"akarsu yatağı sağlam bir güzergah edindi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"su aktı ve kendine bir yatak açtı"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bol sulu veya geniş akarsu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"suyun kazıp açtığı yatak yeri"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kuyu kazısı suya ulaştı"}],"lexicalization_note":"Tanım, yalın su yatağı anlamını korur; suyun akması, yatağın yerleşmesi ve kazıda suya ulaşılması yalnız kendi yapılarına bağlı tutulur.","neighbor_coverage_note":"Listelenen bütün adaylar su yatağı, akış, vadi, iç dallar ve ilgisiz alanlar bakımından değerlendirildi; sınırı en açık biçimde gösteren dört karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal doğal akarsu yatağını büyüklükçe sınırlamaz ve bol suyu da kapsar; komşu dal ise küçük, uzanan veya ana yataktan ayrılan su yoluna özelleşir.","focus_only":"Taşkın ya da bol su taşıyabilen doğal yatağın genel kapsamı bulunur.","gloss":"küçük su yolu","neighbor_only":"Özellikle küçük ve uzanan bir yan su yolu olma sınırı bulunur.","neighbor_ref":"root_000229/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da akan suyu taşıyan belirgin bir arazi yatağını gösterir."},{"boundary_match":"partial","distinction":"Odak dal akışın geçtiği doğal yatağı adlandırır; komşu dal ise öncelikle yüzeyde hareket eden suyu adlandırdığı için olağan kullanımda birbirinin yerine geçmez.","focus_only":"Suyun aktığı ve toprağı yaran kalıcı yatak öne çıkar.","gloss":"yeryüzünde akan su","neighbor_only":"Yatak yerine yeryüzünde akmakta olan su kütlesi öne çıkar.","neighbor_ref":"root_000768/B002","relation_type":"near_neighbor","shared_zone":"İki dal da yeryüzündeki görünür su akışını aynı sahne içinde ele alır."},{"boundary_match":"partial","distinction":"Odak dal su akışının yatağı olarak tanımlanır; komşu dal ise su bulunmasa da varlığını sürdüren geniş bir yer şekli ve sel geçididir.","focus_only":"Bol ya da taşkın suyu taşıyan doğal su yatağıdır.","gloss":"sel yolu olan vadi","neighbor_only":"Dağlar ve tepeler arasındaki geniş arazi geçidi de kapsama girer.","neighbor_ref":"root_001637/B005","relation_type":"near_neighbor","shared_zone":"Her ikisi de suyun arazide izlediği doğal bir geçiş hattını içerebilir."},{"boundary_match":"partial","distinction":"Odak dal bu sürecin su taşıyan arazi yatağını gösterir; komşu dal ise farklı nesnelerde gerçekleşebilen açma ve genişletme işlemini gösterir.","focus_only":"Ortaya çıkmış doğal su yatağı ve onun içindeki akış bulunur.","gloss":"açıp genişletme","neighbor_only":"Bir şeyi açma, genişletme veya içeriğini akışa bırakma işlemi bulunur.","neighbor_ref":"root_001559/B003","relation_type":"near_neighbor","shared_zone":"Toprağın ya da bir açıklığın yarılması ve akışa yol verilmesi ortak imgedir."}],"source_phrase_ar":"النهر مجرى الماء الفائض (mufradat)؛ النهر واحد الأنهار وجمعه أنهار ونهر (ayn;sihah;tahdhib;maqayis)؛ سمي النهر لأنه ينهر الأرض أي يشقها (maqayis)؛ استنهر النهر أخذ مجراه (ayn;tahdhib;maqayis)؛ نهر الماء أو أنهر الماء جرى (sihah;tahdhib;maqayis)؛ نهر نهر كثير الماء (sihah;tahdhib;maqayis;mufradat)؛ حفرت البئر حتى نهرت أي بلغت الماء (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bol veya taşkın suyu taşıyan doğal yatağın toprağı yarmasıdır. Toplu kanıt ayrıca suyun akıp yatak açmasını, yatağın yerleşmesini, bol ya da geniş oluşunu ve kuyu kazısında suya ulaşmayı kapsar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"مجرى الماء الفائض؛ النهر والأنهار وجمع نهر؛ شق الأرض بالمجرى؛ جريان الماء الكثير؛ أخذ المجرى موضعا؛ بلوغ الماء في الحفر","what_is_not_ar":"لا يدخل فيه النهار الزمني؛ ولا الزجر والانتهار؛ ولا فرخ الطير"},"support_links":["sup_2fcd94077e1707e120e8"]},{"boundary":"Dal, yirmi dört saatlik günün tamamına zorunlu olarak yayılmaz ve su yatağı anlamından bütünüyle ayrıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B002","candidate_links":[{"candidate_id":"cand_144d31dcabf292c3749f","lane":"micro"},{"candidate_id":"cand_b60cfc02f90a5d784d58","lane":"micro"},{"candidate_id":"cand_a11327c2c8bfde7a82db","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"şafaktan gün batımına aydınlık gündüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Şafaktan güneş batımına kadar ışığın yayıldığı ve geceye karşıt olan süredir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı kullanımlarda aydınlık süre, bir günün adı yerine geçer."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu zaman adının belirli bir çoğul biçimi de tanıklanmıştır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Gündüz vaktine sahip olan veya gündüz baskın yapan kişi için yapı bağlı bir niteleme kullanılır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Karanlıktan çıkıp gündüzün aydınlığına girme de yapı bağlı bir kullanımdır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın ışık, süre ve geceye karşıtlık bileşenlerini birlikte taşıyan genel karşılığıdır.","boundary_detail":"Dal, yirmi dört saatlik günün tamamına zorunlu olarak yayılmaz ve su yatağı anlamından bütünüyle ayrıdır.","branch_image_ar":"انفتاح النهار بالضياء","concept_gloss":"şafaktan gün batımına aydınlık gündüz","contextual_glosses":[{"applicability":"Geceye karşıt aydınlık zaman diliminin cümle içinde doğal ve kısa karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Aydınlık zaman dilimini ve geceye karşıt oluşunu doğal biçimde korur."},"facet_ids":["F001"],"text":"gündüz","usage_role":"general"},{"applicability":"Aydınlık sürenin kaynakta bir gün adı yerine kullanıldığı sınırlı bağlamlar içindir.","error_profile":{"adds":"Bağlam dışında yirmi dört saatlik tam günü de düşündürebilir.","collision":"Tam gün ile yalnız aydınlık süre arasındaki sınır belirsizleşebilir.","fit":"broadening","loses":null,"preserves":"Belirli bir zaman birimi ve gündelik süre düşüncesini korur."},"facet_ids":["F002"],"text":"gün","usage_role":"contextual"},{"applicability":"Bir öznenin karanlıktan çıkarak gündüzün aydınlığına girdiği yapı bağlı kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gündüzün aydınlığına girme yönündeki katılımcı değişimini korur."},"facet_ids":["F005"],"text":"gündüz vaktine çıktı","usage_role":"contextual"}],"definition":"Şafağın doğuşundan güneşin batışına kadar ışığın yayıldığı, geceye karşıt zaman dilimidir. Bazı kullanımlarda gün adı, çoğul biçim, gündüz vakti hareket eden kişi veya aydınlığa çıkma anlamı kazanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Şafaktan güneş batımına kadar ışığın yayıldığı ve geceye karşıt olan süredir."},{"facet_id":"F002","role":"extension","statement":"Bazı kullanımlarda aydınlık süre, bir günün adı yerine geçer."},{"facet_id":"F003","role":"source_variant","statement":"Bu zaman adının belirli bir çoğul biçimi de tanıklanmıştır."},{"facet_id":"F004","role":"associated_use","statement":"Gündüz vaktine sahip olan veya gündüz baskın yapan kişi için yapı bağlı bir niteleme kullanılır."},{"facet_id":"F005","role":"associated_use","statement":"Karanlıktan çıkıp gündüzün aydınlığına girme de yapı bağlı bir kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı, şafağın doğuşundan güneşin batışına kadar ışığın yayıldığı ve geceye karşıt olan süre olarak kurar. Gün anlamı, çoğul kullanım, gündüz vakti hareket eden kişi ve aydınlığa çıkma bu zaman çekirdeğine bağlı yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"şafaktan güneş batımına kadar süren aydınlık gündüz"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"aydınlık gündüz süreleri"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gündüz vaktinde baskın yapan kimse"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gündüzün aydınlığına girdik"}],"lexicalization_note":"Yalın aydınlık zaman anlamı tanımın çekirdeğidir; kişi nitelemesi ve aydınlığa girme yalnız tanıklanan yapılara bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar ışık, zaman sınırı, gök cismi, sabah bölümü ve kökün diğer dalları bakımından karşılaştırıldı; en yakın üç zaman ve aydınlık komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal şafaktan başlayan ışıklı süreyi ve gece karşıtlığını vurgular; komşu dal güneş doğumundan batımına ölçülen bilinen gün süresini öne çıkarır.","focus_only":"Işığın yayılması ve geceye karşıtlık tanımın kurucu parçalarıdır.","gloss":"güneş doğumundan batımına gün","neighbor_only":"Güneşin doğuşuyla başlayan ve bir gün birimi olarak sayılan süre öne çıkar.","neighbor_ref":"root_001700/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gün içindeki aydınlık zaman aralığını sınırlarıyla gösterir."},{"boundary_match":"partial","distinction":"Odak dal aydınlık gündüzün tamamıdır; komşu dal yalnız bu sürenin ilk bölümünü ve başlangıç anını adlandırır.","focus_only":"Şafaktan gün batımına kadar uzanan bütün aydınlık süreyi kapsar.","gloss":"sabah ve günün başlangıcı","neighbor_only":"Aydınlık sürenin yalnız başlangıcı ve sabah bölümüyle sınırlıdır.","neighbor_ref":"root_000839/B001","relation_type":"near_neighbor","shared_zone":"İki dal da karanlığın ardından başlayan gündüz zamanına ilişkindir."},{"boundary_match":"partial","distinction":"Odak dal ışıklı zaman aralığını adlandırır; komşu dal ise ışığın veya yüzün aydınlanma durumunu ve belirli sabah vakitlerini kapsar.","focus_only":"Belirli başlangıç ve bitiş sınırları olan bir zaman dilimidir.","gloss":"ışığın belirginleşmesi","neighbor_only":"Yüzün parlaması ve karanlıktan sonra ışığın belirginleşmesi de kapsamdadır.","neighbor_ref":"root_000712/B002","relation_type":"near_neighbor","shared_zone":"Aydınlığın karanlıktan sonra görünür hale gelmesi iki dalın kesişimidir."}],"source_phrase_ar":"النهار ضياء ما بين طلوع الفجر إلى غروب الشمس (ayn;tahdhib;maqayis)؛ النهار ضد الليل (sihah)؛ الوقت الذي ينتشر فيه الضوء (mufradat)؛ النهار اسم لكل يوم (tahdhib)؛ النهار يجمع على نهر (sihah;tahdhib;maqayis)؛ رجل نهر صاحب نهار (ayn;sihah;tahdhib;maqayis;mufradat)","source_summary":"Kaynaklar aydınlık gündüz süresini geceye karşıt, ışığın yayıldığı zaman olarak ortaklaştırır. Toplu kanıt bu sürenin kimi yerde gün adı olmasını, çoğulunu, gündüz hareket eden kişi nitelemesini ve aydınlığa girme kullanımını da taşır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النهار وضوء ما بين طلوع الفجر وغروب الشمس؛ ضد الليل؛ اليوم في بعض الاستعمال؛ جمع النهار على نهر؛ رجل نهر صاحب نهار","what_is_not_ar":"لا يدخل فيه مجرى الماء؛ ولا السعة المجردة؛ ولا فرخ الطير"},"support_links":["sup_874c7c38b83d38d30918","sup_f2913b56e6468397184d","sup_fb8ed09773bd4c50b7be"]},{"boundary":"Akış, kan ve bağırsak kullanımlarında belirgindir; açık alan ve yarık genişletmede ise kurucu öğe açıklık veya genişliktir.","branch_kind":"mixed_non_bare","branch_ref":"root_001559/B003","candidate_links":[{"candidate_id":"cand_f36155fd60af20406c62","lane":"micro"},{"candidate_id":"cand_bb5639e032b701b4c8c0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"bir şeyi açma veya genişletme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin açılması, açılması için yarılması veya mevcut açıklığının genişletilmesi temel ilişkidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanı açılan bir yerden serbest bırakıp akıtma, çekirdeğin akış sonuçlu özel gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir yaranın veya yarığın açıklığını büyütmek, genişletme çekirdeğinin özel gerçekleşmesidir."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Evlerin önleri arasında kalan ve atıkların bırakıldığı açık alan, açıklık sonucunun adlaşmış uzantısıdır."}},{"facet_id":"F005","role":"associated_use","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Bağırsağın çözülüp akarsu gibi boşalması, akış benzetmesine bağlı bedensel bir kullanımdır."}},{"facet_id":"F006","role":"source_variant","source_fields":["distinctive_facets[F006]"],"statements":{"statement":"Genişlik, kimi açıklamalarda su yatağına benzetilir; başka bir anlatımda aydınlıkla birlikte anılır."}},{"facet_id":"F007","role":"associated_use","source_fields":["distinctive_facets[F007]"],"statements":{"statement":"Tehlikeler için kullanılan bir biçim, iki ayrı söz öğesinin kaynaştırılmasıyla açıklanan tartışmalı bir türetmedir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın akış gerektirmeyen açma ve genişletme çekirdeğini temsil eder; akış yalnız uygun bağlamlardaki özel gerçekleşmelere aittir.","boundary_detail":"Akış, kan ve bağırsak kullanımlarında belirgindir; açık alan ve yarık genişletmede ise kurucu öğe açıklık veya genişliktir.","branch_image_ar":"فتح الشيء وتوسيعه حتى يسيل أو ينفسح","concept_gloss":"bir şeyi açma veya genişletme","contextual_glosses":[{"applicability":"Bir açıklık oluşturarak veya açılmış yeri serbest bırakarak kanın akmasını sağlama bağlamındadır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kanı açıp serbest bırakma işlemini ve ortaya çıkan akışı korur."},"facet_ids":["F002"],"text":"kanı akıttı","usage_role":"contextual"},{"applicability":"Yara, delik veya benzeri bir açıklığın daha geniş hale getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mevcut açıklığın genişletilmesi işlemini doğrudan korur."},"facet_ids":["F003"],"text":"yarığı genişletti","usage_role":"contextual"},{"applicability":"Evlerin ön bölümleri arasında kalan ve atık bırakılabilen belirli açık yeri açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerleşim içindeki açık alanı ve evler arasındaki konumunu korur."},"facet_ids":["F004"],"text":"evler arasındaki açık alan","usage_role":"explanatory"}],"definition":"Bir şeyi açmak, yarığını genişletmek veya içindekini akacak biçimde serbest bırakmaktır. Bu çekirdek kan akıtma, yara açıklığını büyütme, açık alan, bağırsak boşalması ve genişlik ya da aydınlık benzetmelerinde özelleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin açılması, açılması için yarılması veya mevcut açıklığının genişletilmesi temel ilişkidir."},{"facet_id":"F002","role":"specialization","statement":"Kanı açılan bir yerden serbest bırakıp akıtma, çekirdeğin akış sonuçlu özel gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"Bir yaranın veya yarığın açıklığını büyütmek, genişletme çekirdeğinin özel gerçekleşmesidir."},{"facet_id":"F004","role":"extension","statement":"Evlerin önleri arasında kalan ve atıkların bırakıldığı açık alan, açıklık sonucunun adlaşmış uzantısıdır."},{"facet_id":"F005","role":"associated_use","statement":"Bağırsağın çözülüp akarsu gibi boşalması, akış benzetmesine bağlı bedensel bir kullanımdır."},{"facet_id":"F006","role":"source_variant","statement":"Genişlik, kimi açıklamalarda su yatağına benzetilir; başka bir anlatımda aydınlıkla birlikte anılır."},{"facet_id":"F007","role":"associated_use","statement":"Tehlikeler için kullanılan bir biçim, iki ayrı söz öğesinin kaynaştırılmasıyla açıklanan tartışmalı bir türetmedir."}],"identity_rationale":"Kaynak ifadesinin çekirdeği bir şeyi açmak, yarığını genişletmek veya içindekini serbestçe akacak hale getirmektir. Geçici dal imgesi kullanılabilir, ancak her örnekte akış sonucu bulunmadığından genişleme ve açıklık yönü akıştan bağımsız olarak da korunmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"genişlik veya aydınlıkla birlikte genişlik"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kanı açıp serbest bırakarak akıttı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yaranın veya yarığın açıklığını genişletti"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"genişledi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"evlerin önleri arasında atık bırakılan açık alan"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bağırsağı çözüldü ve akarsu gibi boşaldı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tehlikeler; birleşik bir türetme olarak açıklanan biçim"}],"lexicalization_note":"Genel açılma ve genişleme çekirdeği korunur; kan, yara, açık alan ve bağırsak kullanımları kendi biçim ve yapılarına bağlanır.","neighbor_coverage_note":"Bütün adaylar açma, yayma, genişletme, tıkanma, daralma, bedensel açıklık ve kökün iç dalları bakımından değerlendirildi; dört yakın sınır seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal açmanın yanında genişlemeyi ve kimi yapılarda akışı kurucu sayar; komşu dal daha genel yarma ve açma eylemine, ayrıca kendine özgü canlı örneklerine uzanır.","focus_only":"Açıklığı büyütme ve içeriği akışa serbest bırakma yönü bulunur.","gloss":"yarıp açma","neighbor_only":"Karın yarma ve yavruyu çıkarmak için hayvanı açma gibi özel kapsamlar bulunur.","neighbor_ref":"root_000139/B002","relation_type":"near_synonym","shared_zone":"Bir nesnenin bütünlüğünü bozarak açıklık oluşturma iki dalın ortak çekirdeğidir."},{"boundary_match":"partial","distinction":"Odak dal açıklık oluşturma, yarığı büyütme ve akışa izin verme işlemlerini içerir; komşu dal ise ferahlık ve mekansal yayılma yönünde özelleşir.","focus_only":"Yarık açma ve içeriği akıtacak biçimde serbest bırakma bulunur.","gloss":"ferahlatıp genişletme","neighbor_only":"Bir yere ferahlık verme veya bir varlığa açılıp uzaklaşmasını söyleme bulunur.","neighbor_ref":"root_000549/B006","relation_type":"near_synonym","shared_zone":"Her iki dal bir şeyin alanını veya açıklığını büyütme düşüncesinde kesişir."},{"boundary_match":"partial","distinction":"Odak dal akış olmasa da açılma ve genişlemeyi kapsar; komşu dal geniş yarılma ile özellikle suyun patlayarak çıkmasını birlikte öne çıkarır.","focus_only":"Kan, yara, açık alan ve bağırsak gibi farklı yapılardaki genişleme kapsamı bulunur.","gloss":"geniş yarılıp fışkırma","neighbor_only":"Geniş yarılmayla suyun güçlü biçimde fışkırması ve bunun açıldığı yerler bulunur.","neighbor_ref":"root_001132/B001","relation_type":"near_synonym","shared_zone":"Geniş bir açıklığın oluşması ve bu açıklıktan akış çıkması ortak bölgedir."},{"boundary_match":"partial","distinction":"Odak dal işlemi ve durum değişimini anlatır; komşu dal ise bu değişimle ilişkilendirilen kalıcı su yatağını adlandırır.","focus_only":"Farklı nesnelerde gerçekleşen açma, genişletme veya serbest bırakma işlemidir.","gloss":"doğal akarsu yatağı","neighbor_only":"Bol suyu taşıyan, toprağı yarmış doğal arazi yatağıdır.","neighbor_ref":"root_001559/B001","relation_type":"near_neighbor","shared_zone":"Bir açıklığın su akışına yol vermesi ve yatağın yarılarak oluşması ortak imgedir."}],"source_phrase_ar":"أصل صحيح يدل على تفتح شيء أو فتحه (maqayis)؛ أنهرت الدم فتحته وأرسلته (maqayis)؛ أنهرت الدم أي أسلته (sihah;mufradat)؛ أنهرت الطعنة وسعتها وأنهر فتقها (sihah;tahdhib)؛ نهر من نهر الفتق (maqayis)؛ استنهر الشيء اتسع (sihah)؛ المنهرة فضاء يكون بين أفنية القوم (maqayis;sihah;mufradat)؛ أنهر بطنه إذا جاء بطنه مثل مجيء النهر (tahdhib)؛ النهر السعة تشبيها بنهر الماء وفي ضياء وسعة (mufradat;sihah;tahdhib)","source_summary":"Toplu kanıt açma ve genişletme çekirdeğini kanın akıtılması, yara açıklığının büyütülmesi ve bir şeyin genişlemesiyle kurar. Açık alan, bağırsak boşalması, genişlik ve aydınlık anlatımları ile birleşik türetme açıklaması bu çekirdeğin farklı uzantılarıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"فتح الشيء وتوسيعه؛ إسالة الدم؛ اتساع الطعنة والفتق؛ الفضاء بين الأفنية؛ مجيء البطن كمجيء النهر؛ تفسير النهر بالسعة أو الضياء والسعة","what_is_not_ar":"لا يدخل فيه النهر المائي بوصفه مجرى قائما؛ ولا النهار الزمني؛ ولا الزجر"},"support_links":["sup_2fcd94077e1707e120e8","sup_d963a133807003af2ab9"]},{"boundary":"Dal genel kabalık, suç sayma veya salt susturma değildir; kişiye yöneltilen sert sözlü engelleme yapısıyla sınırlıdır.","branch_kind":"collocation","branch_ref":"root_001559/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"sert sözle azarlayıp engelleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Muhataba sert ve azarlayıcı söz yönelterek onu kötü bir davranıştan caydırma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, kişiyi doğrudan karşılayıp yüzüne karşı azarlama biçiminde gerçekleşebilir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişiyi sert sözle karşılayıp davranışından caydırmayı amaçlayan yapı bağlı kullanımın tam karşılığıdır.","boundary_detail":"Dal genel kabalık, suç sayma veya salt susturma değildir; kişiye yöneltilen sert sözlü engelleme yapısıyla sınırlıdır.","branch_image_ar":"زجر بكلام مغلظ","concept_gloss":"sert sözle azarlayıp engelleme","contextual_glosses":[{"applicability":"Kişiye yüz yüze sert söz söylendiği, ancak caydırma amacı bağlamdan anlaşıldığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kötü davranışı engelleme yönünü tek başına açıkça söylemez.","preserves":"Muhataba yöneltilen sert ve azarlayıcı konuşmayı korur."},"facet_ids":["F001","F002"],"text":"sertçe azarladı","usage_role":"contextual"}],"definition":"Bir kişiyi sert ve azarlayıcı sözle karşılayarak kötü bir davranıştan alıkoymaya veya caydırmaya çalışmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Muhataba sert ve azarlayıcı söz yönelterek onu kötü bir davranıştan caydırma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, kişiyi doğrudan karşılayıp yüzüne karşı azarlama biçiminde gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi, bir kişiyi sert ve azarlayıcı sözle karşılayarak kötü davranıştan caydırma eylemini tutarlı biçimde verir. Sertlik yalnız konuşma tarzı değil, muhataba yöneltilen engelleyici azarın kurucu parçasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"onu sert sözle azarlayıp engelledi"}],"lexicalization_note":"Anlam yalnız kişiye yöneltilen sert sözlü azarlama yapısında tanıklanır ve yalın bir kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar azarlama, kınama, sözde sertlik, yüzüne karşı konuşma, susturma ve kökün diğer dalları bakımından değerlendirildi; üç işlevsel karşıtlık seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişiye yöneltilen sert sözlü azardır; komşu dal daha geniş biçimde insanı, hayvanı veya başka varlıkları sesle men etme, sürme ve ses çıkarma alanını kapsar.","focus_only":"Bir kişiyi sert ve yüzüne yöneltilen sözle caydırma sınırı bulunur.","gloss":"sesle azarlayıp uzaklaştırma","neighbor_only":"Hayvan, bulut veya başka varlıkları sesle sürme ve sesin kendisini adlandırma kapsamı bulunur.","neighbor_ref":"root_000624/B001","relation_type":"near_synonym","shared_zone":"Muhatabı ses veya söz yoluyla durdurma, caydırma ve geri çevirme ortaktır."},{"boundary_match":"partial","distinction":"Odak dal amaçlı bir azarlama eylemidir; komşu dal ise eylem gerektirmeyen genel bir sertlik ve kabalık niteliğidir.","focus_only":"Belirli bir muhatabı davranıştan caydırmaya yönelik sözlü eylemdir.","gloss":"sözde veya davranışta sertlik","neighbor_only":"Söz, davranış, buyruk veya cezanın genel sertlik niteliğini kapsar.","neighbor_ref":"root_001099/B002","relation_type":"near_neighbor","shared_zone":"Sertlik ve muhatap üzerinde baskı kuran konuşma iki dalda da bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal davranışı engellemeye dönük sert azardır; komşu dal geçmiş bir suç veya kusur üzerinden kınama ve ayıplamayı öne çıkarır.","focus_only":"Sert sözle anlık olarak durdurma veya caydırma amacı bulunur.","gloss":"suçundan dolayı kınama","neighbor_only":"İşlenmiş suçu sayıp dökme, ayıplama ve uzun uzadıya kınama bulunur.","neighbor_ref":"root_000197/B001","relation_type":"near_neighbor","shared_zone":"Muhataba olumsuz değerlendirme içeren ağır söz yöneltme ortak alandır."}],"source_phrase_ar":"نهرت الرجل نهرا وانتهرته انتهارا زجرته بكلام عن شر (ayn)؛ نهره وانتهره أي زبره (sihah)؛ نهرته وانتهرته إذا استقبلته بكلام تزجره (tahdhib)؛ النهر والانتهار الزجر بمغالظة (mufradat)","source_summary":"Kaynaklar, bir kişiye sert sözle yöneltilen azarlama ve engellemeyi ortak çekirdek olarak verir. Doğrudan karşılayarak konuşma, eylemin yüz yüze gerçekleşebilen biçimini belirginleştirir.","sources":["AY","SI","TA","MU"],"what_is_ar":"نهر الرجل وانتهره إذا زجره أو زبره بكلام شديد؛ الانتهار بمعنى الاستقبال بالزجر","what_is_not_ar":"لا يدخل فيه النهر المائي؛ ولا النهار؛ ولا مجرد فتح الشيء أو توسعته"},"support_links":[]},{"boundary":"Bu ad genel olarak bütün yavruları kapsamaz; tanıklanan bazı kuşlarla sınırlıdır ve tür aktarımı kaynaklar arasında değişir.","branch_kind":"bare","branch_ref":"root_001559/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"bazı kuşların yavrusu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz, genel yavru adı değil, bazı kuşların yavrusu için kullanılan sınırlı bir addır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yavrunun ait olduğu kuş, aktarımlarda bağırtlak türleri, kartal veya toy kuşu olarak farklı biçimlerde belirtilir."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Türü kaynak aktarımına göre değişen, ancak kuş yavrusu olma çekirdeği sabit kalan dalın en kısa karşılığıdır.","boundary_detail":"Bu ad genel olarak bütün yavruları kapsamaz; tanıklanan bazı kuşlarla sınırlıdır ve tür aktarımı kaynaklar arasında değişir.","branch_image_ar":"النَّهار فرخ طير","concept_gloss":"bazı kuşların yavrusu","contextual_glosses":[{"applicability":"Kuş türünün metinde ayrıca belirtildiği veya tarihsel adın yalnız yavru oluşunun önemli olduğu bağlamlarda kullanılır.","error_profile":{"adds":"Tanıklanmayan bütün kuş türlerini kapsayabilecek genel bir alan açar.","collision":"Sınırlı tarihsel ad ile genel kuş yavrusu ifadesi karışabilir.","fit":"broadening","loses":null,"preserves":"Canlının bir kuş yavrusu olduğu temel bilgiyi korur."},"facet_ids":["F001"],"text":"kuş yavrusu","usage_role":"contextual"}],"definition":"Bazı kuşların yavrusu için kullanılan bir addır; hangi kuş türünü gösterdiği konusunda aktarımlar bağırtlak türleri, kartal ve toy kuşu arasında değişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz, genel yavru adı değil, bazı kuşların yavrusu için kullanılan sınırlı bir addır."},{"facet_id":"F002","role":"source_variant","statement":"Yavrunun ait olduğu kuş, aktarımlarda bağırtlak türleri, kartal veya toy kuşu olarak farklı biçimlerde belirtilir."}],"identity_rationale":"Kaynak ifadesi sözü bazı kuşların yavrusu olarak doğrular, ancak kuş türünü tekleştirmez. Aktarımlar bağırtlak türleri, kartal ve toy kuşu arasında değiştiği için dal kuş yavrusu çekirdeğinde tutulmalı, belirli bir türe indirgenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"türü aktarıma göre değişen bir kuş yavrusu"}],"lexicalization_note":"Tanım yalın biçimin bazı kuş yavruları için kullanımını verir; komşu dallardaki belirli tür adları buraya taşınmaz.","neighbor_coverage_note":"Bütün adaylar kuş türü, genel yavruluk, başka hayvan adları ve kökün iç dalları bakımından değerlendirildi; tür sınırını açıklayan üç komşu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın tür aktarımı birden çok ve uyuşmaz kuşu kapsar; komşu dal ise keklik ve bağırtlak yavrularını, ayrıca cinsiyete göre biçimleriyle sınırlar.","focus_only":"Aktarıma göre kartal veya toy kuşu yavrusunu da gösterebilen değişken kapsam bulunur.","gloss":"keklik veya bağırtlak yavrusu","neighbor_only":"Erkek ve dişi için ayrı biçimler ile keklik yavrusu kapsamı bulunur.","neighbor_ref":"root_000735/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da bağırtlak türlerinin yavrularını gösterebilir."},{"boundary_match":"field_only","distinction":"Odak dalın tanıklanan türleri arasında keklik kesin biçimde yer almaz ve aktarım değişkendir; komşu dal doğrudan keklik yavrusuna özgüdür.","focus_only":"Birden fazla kuş türüne ilişkin değişken tarihsel aktarım bulunur.","gloss":"keklik yavrusu","neighbor_only":"Yalnız keklik yavrusunu gösteren belirli bir ad bulunur.","neighbor_ref":"root_000728/B007","relation_type":"same_field","shared_zone":"İki dal da belirli kuşların yavruları için kullanılan özel adlardır."},{"boundary_match":"partial","distinction":"Odak dal bazı kuş türleriyle sınırlı özel bir addır; komşu dal ise insan ve hayvan yavrularına yayılabilen genel bir yaş ve küçüklük adıdır.","focus_only":"Yalnız bazı kuş türlerinin yavrularına ait tarihsel bir ad olma sınırı bulunur.","gloss":"küçük yavru","neighbor_only":"İnsan, evcil hayvan ve yabani hayvan yavrularını kapsayan genel küçüklük alanı bulunur.","neighbor_ref":"root_000942/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da henüz yetişkin olmayan bir canlı yavrusunu gösterebilir."}],"source_phrase_ar":"النهار فرخ القطا والغطاط والعقاب ونحوه وثلاثة أنهرة (ayn)؛ النهار فرخ الحبارى (sihah;tahdhib;mufradat)؛ النهار فرخ بعض الطير مما لا يعرج على مثله ولا معنى له (maqayis)","source_summary":"Toplu kanıt sözü bazı kuşların yavrusu olarak ortaklaştırır, fakat tür konusunda ayrışır. Aktarılan türler bağırtlak benzeri kuşlardan kartala ve toy kuşuna kadar değiştiği için tek bir kuş belirlemek mümkün değildir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"النَّهار اسما لفرخ بعض الطير؛ فرخ القطا أو الغطاط أو العقاب أو الحبارى بحسب نقل المصادر","what_is_not_ar":"لا يدخل فيه النهار الزمني؛ ولا النهر المائي؛ ولا الزجر"},"support_links":[]},{"boundary":"Dalın odağı fırsatçı ve ani kapmadır; salt gizlilik, genel hırsızlık veya her türlü kandırma yeterli değildir.","branch_kind":"bare","branch_ref":"root_001559/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"fırsat kollayıp gizlice kapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi karşı taraf hazırlıksızken ani bir atılışla kapma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem, fırsat kollama ve kapmayı fark ettirmeden gerçekleştirme yönü taşır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ani atılış, karşı tarafın hazırlıksızlığı ve fırsatçı kapma bileşenlerini birlikte karşılar.","boundary_detail":"Dalın odağı fırsatçı ve ani kapmadır; salt gizlilik, genel hırsızlık veya her türlü kandırma yeterli değildir.","branch_image_ar":"الدغرة والخلسة","concept_gloss":"fırsat kollayıp gizlice kapma","contextual_glosses":[{"applicability":"Bir şeyin karşı taraf hazırlıksızken ani ve fark ettirilmeden alındığı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kapmanın gizli, ani ve fırsattan yararlanan biçimini korur."},"facet_ids":["F001","F002"],"text":"gizlice kapıverme","usage_role":"contextual"}],"definition":"Bir fırsatı kollayıp ani bir atılışla bir şeyi gizlice veya karşı taraf hazırlıksızken kapma eylemidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi karşı taraf hazırlıksızken ani bir atılışla kapma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem, fırsat kollama ve kapmayı fark ettirmeden gerçekleştirme yönü taşır."}],"identity_rationale":"Tek kaynak ifadesi anlamı ani bir atılışla, fırsattan yararlanarak gizlice kapma olarak verir. Bu çekirdek genel hırsızlıktan, uzun süreli hileden ve öldürücü gizli saldırıdan daha dardır.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"fırsat kollayıp ani biçimde gizlice kapma"}],"lexicalization_note":"Tanım, yalın biçimin ani ve fırsatçı kapma anlamıyla sınırlıdır; komşu hile ve hırsızlık yapıları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar hız, gizlilik, fırsat kollama, hile, hırsızlık, öldürücü sonuç ve kökün iç dalları bakımından değerlendirildi; üç yakın sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal fırsat kollama ve gizli ani atılışla sınırlıdır; komşu dal hızla kapma çekirdeğinden çok daha geniş nesne ve sonuçlara uzanır.","focus_only":"Karşı tarafın hazırlıksızlığından yararlanan fırsatçı atılış öne çıkar.","gloss":"hızla kapıp alma","neighbor_only":"Hızlı koparıp alma yanında işitme, görme, baş alma ve yağmalama uzantıları bulunur.","neighbor_ref":"root_000423/B001","relation_type":"near_synonym","shared_zone":"Bir şeyi hızlı ve beklenmedik biçimde ele geçirme iki dalın ortak alanıdır."},{"boundary_match":"partial","distinction":"Odak dal bu fırsatı ani bir kapma eylemiyle sonuçlandırır; komşu dal ise dalgınlığı kullanma yöntemini anlatır ve belirli bir alma sonucu gerektirmez.","focus_only":"Fırsat sonunda bir şeyi ani biçimde kapma sonucu bulunur.","gloss":"dalgınlıktan yararlanma","neighbor_only":"Karşı tarafın dalgınlığını kullanma, herhangi bir kapma sonucu olmadan da bulunabilir.","neighbor_ref":"root_001097/B005","relation_type":"near_neighbor","shared_zone":"Karşı tarafın hazırlıksız veya dikkatsiz anından yararlanma ortaktır."},{"boundary_match":"partial","distinction":"Odak dal ani kapmayla sınırlı kalır; komşu dal gizli ele geçirmeyi öldürme, yok etme ya da gücü giderme gibi ağır sonuçlarla birleştirir.","focus_only":"Ani ve fırsatçı kapma, öldürme veya yok etme gerektirmez.","gloss":"gizlice ele geçirip yok etme","neighbor_only":"Gizlice öldürme, yok etme veya güç ve bilinci giderme sonuçları bulunur.","neighbor_ref":"root_001115/B001","relation_type":"near_neighbor","shared_zone":"Eylemin hedefçe önceden fark edilmemesi ve gizli gerçekleşmesi ortaktır."}],"source_phrase_ar":"النهر الدغرة وهي الخلسة (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Ani atılışla fırsatçı kapma anlamı bu dalda tek kaynaklı bir tanıklığa dayanır."}],"source_summary":"Bu dal için ortaklaştırılabilecek çok kaynaklı bir anlatım yoktur; kanıt ani ve gizlice kapma anlamını tek başına tanıklar.","sources":["TA"],"what_is_ar":"النهر بمعنى الدغرة؛ الدغرة هي الخلسة","what_is_not_ar":"لا يدخل فيه الزجر؛ ولا جريان الماء؛ ولا فتح الدم أو الطعنة"},"support_links":[]},{"boundary":"Dal yalnız belirtilen özel-ad kullanımlarını kapsar; zaman, su yatağı veya yıldızların genel tür anlamı buraya aktarılmaz.","branch_kind":"non_bare","branch_ref":"root_001559/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"kişi, yer ve yıldızlara ait özel adlar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, ortak bir tür anlamı değil, belirli varlıkları gösteren sınırlı bir özel-ad kümesini temsil eder."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kümedeki kullanımlardan biri belirli bir topluluktan bir şairin adıdır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kümedeki kullanımlardan biri belirli bir yerin adıdır."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Kümedeki kullanımlardan biri sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak addır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın heterojen üyelerini ortak anlam uydurmadan, yalnız belirli varlıkları gösteren adlar olarak temsil eder.","boundary_detail":"Dal yalnız belirtilen özel-ad kullanımlarını kapsar; zaman, su yatağı veya yıldızların genel tür anlamı buraya aktarılmaz.","branch_image_ar":"أعلام وأسماء خاصة","concept_gloss":"kişi, yer ve yıldızlara ait özel adlar","contextual_glosses":[{"applicability":"Kümedeki kişi adının, yazımı ayrıca üretilmeden yalnız işlevinin açıklanması gereken bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın belirli bir şairi gösteren kişi adı olmasını korur."},"facet_ids":["F002"],"text":"bir şairin adı","usage_role":"explanatory"},{"applicability":"Kümedeki yer adının, yüzey biçimi verilmeden yalnız adlandırma işlevinin açıklandığı bağlam içindir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın belirli bir yeri gösteren özel ad olmasını korur."},"facet_ids":["F003"],"text":"bir yer adı","usage_role":"explanatory"},{"applicability":"Sularının bolluğuyla ilişkilendirilen iki yıldız için kullanılan ortak adın işlevini açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki yıldızı birlikte adlandırmayı ve ortak ad ilişkisini korur."},"facet_ids":["F004"],"text":"iki yıldızın ortak adı","usage_role":"explanatory"}],"definition":"Aynı sözlük maddesinde yer alan, bir şairi, bir yeri ve sularının bolluğu gerekçesiyle iki yıldızı gösteren birbirinden ayrı özel ad kullanımlarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, ortak bir tür anlamı değil, belirli varlıkları gösteren sınırlı bir özel-ad kümesini temsil eder."},{"facet_id":"F002","role":"example","statement":"Kümedeki kullanımlardan biri belirli bir topluluktan bir şairin adıdır."},{"facet_id":"F003","role":"example","statement":"Kümedeki kullanımlardan biri belirli bir yerin adıdır."},{"facet_id":"F004","role":"example","statement":"Kümedeki kullanımlardan biri sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak addır."}],"identity_rationale":"Kaynak ifadesi bir şairin adı, bir yer adı ve sularının bolluğu gerekçesiyle iki yıldız için kullanılan ortak adı aynı özel-ad kümesinde toplar. Küme geçerlidir, ancak üyeler ortak bir kavramın örnekleri değil, yalnız aynı sözlük maddesinde bulunan ayrı özel adlardır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"belirli bir topluluktan bir şairin adı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir yer adı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"sularının bolluğu nedeniyle iki yıldız için kullanılan ortak ad"}],"lexicalization_note":"Tanım yalnız kanıtta verilen kişi, yer ve iki yıldızın ortak adıyla sınırlıdır; bunlardan genel bir yalın anlam çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar kişi, yer, topluluk, gök adı ve kökün anlam dalları bakımından değerlendirildi; yalnız özel-ad sınıfını paylaşan üç aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Dallar yalnız özel-ad alanını paylaşır; gösterdikleri kişi, yer ve gök varlıkları bütünüyle farklı olduğundan birbirlerinin yerine kullanılamaz.","focus_only":"Belirli bir şair, belirli bir yer ve iki yıldızın ortak adından oluşan kapalı liste bulunur.","gloss":"başka kişi, yer ve gök adları","neighbor_only":"Başka kişileri, yerleri ve tek bir gök cismini gösteren ayrı bir ad kümesi bulunur.","neighbor_ref":"root_000333/B012","relation_type":"same_field","shared_zone":"Her iki dal da kişi, yer veya gök varlığı gösteren özel adları toplar."},{"boundary_match":"field_only","distinction":"Ortaklık yalnız ad türündedir; her dal farklı varlıkları gösteren kapalı bir ad listesine sahip olduğu için anlamsal ikame yoktur.","focus_only":"Bir şair, bir yer ve iki yıldıza ilişkin üç ayrı ad kullanımı bulunur.","gloss":"başka kişi ve yer adları","neighbor_only":"Başka bir yer ile şiir tanığındaki başka bir kişiye ait adlar bulunur.","neighbor_ref":"root_001694/B010","relation_type":"same_field","shared_zone":"Her iki dal kişi ve yerleri gösteren özel ad kullanımlarını içerir."},{"boundary_match":"field_only","distinction":"Odak dal üç belirli kullanımın kapalı kümesidir; komşu dal başka biçimlerden türemiş ayrı kişi ve yer adlarını kapsar.","focus_only":"İki yıldız için kullanılan ortak ad ve bu dala özgü kişi ile yer adı bulunur.","gloss":"başka türemiş kişi ve yer adları","neighbor_only":"Başka bir söz ailesinden türemiş çok sayıda kişi ve yer adı bulunur.","neighbor_ref":"root_000943/B007","relation_type":"same_field","shared_zone":"Her iki dal sözlükteki biçimlerden doğan kişi ve yer adlarını bir araya getirir."}],"source_phrase_ar":"نهار بن توسعة اسم شاعر من تميم (sihah)؛ نهروان بلد (sihah)؛ العرب تسمي العواء والسماك الأنهرين لكثرة مائهما (tahdhib)","source_summary":"Toplu kanıt üç ayrı özel-ad kullanımını bir araya getirir: bir şair, bir yer ve sularının bolluğuyla ilişkilendirilen iki yıldızın ortak adı. Bu üyeler arasında özel ad olmanın dışında ortak bir sözlük anlamı kurulmaz.","sources":["SI","TA"],"what_is_ar":"الأعلام والأسماء الخاصة الواردة في المادة؛ نهار بن توسعة اسما لشاعر؛ نهروان اسما لبلد؛ الأنهران اسما للعواء والسماك لكثرة مائهما","what_is_not_ar":"لا يدخل فيه النهار الزمن ولا النهر المجرى إلا إذا كان الاسم معللا بهما"},"support_links":[]},{"boundary":"Dal yalnız bulut adıdır; su yatağı, aydınlık gündüz veya belirli bulut türlerinin ek özellikleri tanıma girmez.","branch_kind":"bare","branch_ref":"root_001559/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","surface_ar":"نَّهَارِ"}],"gloss":"bulut","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gökyüzündeki bulutu herhangi bir tür özelliği eklemeden adlandırır."}}],"root_ar":"ن ه ر","root_id":"root_001559","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bir tür, büyüklük, yağış veya oluşma zamanı eklemeden dalın genel gökyüzü varlığını karşılar.","boundary_detail":"Dal yalnız bulut adıdır; su yatağı, aydınlık gündüz veya belirli bulut türlerinin ek özellikleri tanıma girmez.","branch_image_ar":"النَّاهُور سحاب","concept_gloss":"bulut","contextual_glosses":[{"applicability":"Yalın biçimin cümle içinde sayılabilir tek bir gökyüzü bulutunu gösterdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Herhangi bir tür niteliği eklemeden tek bir bulutu gösterir."},"facet_ids":["F001"],"text":"bir bulut","usage_role":"general"}],"definition":"Gökyüzünde görülen bulut için kullanılan yalın bir addır; tanıklık belirli bir bulut türü veya hava olayıyla sınır koymaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gökyüzündeki bulutu herhangi bir tür özelliği eklemeden adlandırır."}],"identity_rationale":"Tek kaynak ifadesi yalın biçimi doğrudan bulut olarak tanımlar. Bulutun inceliği, su taşıması, kalıcılığı veya günün belirli vaktinde oluşması gibi ek bir özellik verilmediğinden dal genel bulut anlamında tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"bulut"}],"lexicalization_note":"Tanım yalın biçimin genel bulut anlamını verir; komşu dallardaki incelik, büyüklük, yağış veya zaman özelliklerini içeri almaz.","neighbor_coverage_note":"Bütün adaylar bulut türü, biçim, yağış, hareket, büyüklük, oluşma zamanı ve kökün iç dalları bakımından değerlendirildi; üç yakın bulut komşusu seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız genel bulut adıdır; komşu dal bulutun parçasına, yağmura, doluya ve bunlarla ilgili türemiş kullanımlara uzanır.","focus_only":"Ek nitelik taşımayan tek ve genel bir bulut adı bulunur.","gloss":"bulut ve yağış bulutu","neighbor_only":"Bulut parçası, yağmur, dolu ve bunlardan türeyen kullanımlar da kapsama girer.","neighbor_ref":"root_001419/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın çekirdeğinde gökyüzündeki bulut bulunur."},{"boundary_match":"partial","distinction":"Odak dal genel buluttur; komşu dal ise görünüşü dağa benzeyen, ince ve çoğu aktarımda su taşımayan belirli bir bulut türüdür.","focus_only":"Bulutun inceliği, biçimi veya su taşıması konusunda bir sınırlama yoktur.","gloss":"ince ve su taşımayan bulut","neighbor_only":"İnce, dağ gibi karşıdan görünen ve çoğu anlatımda su taşımayan bulut olma sınırı vardır.","neighbor_ref":"root_000252/B005","relation_type":"near_synonym","shared_zone":"Her iki dal gökyüzünde görülen bir bulutu adlandırır."},{"boundary_match":"partial","distinction":"Odak dal niteliksiz genel addır; komşu dal bir yerde oyalanan, yavaş hareket eden ve su yüküyle ilişkilendirilen özel bulut türüdür.","focus_only":"Bulutun hareketi, kalış süresi veya su miktarı belirtilmez.","gloss":"yavaş ve kalıcı bulut","neighbor_only":"Bir yerde kalan, ağır ilerleyen ve çok su taşıyabilen bulut olma niteliği bulunur.","neighbor_ref":"root_000902/B007","relation_type":"near_synonym","shared_zone":"Her iki dal tek bir bulut varlığını gösterebilir."}],"source_phrase_ar":"الناهُور السحاب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Genel bulut anlamı bu dalda tek kaynaklı ve ek niteliksiz bir tanıklığa dayanır."}],"source_summary":"Bu dal için ortaklaştırılabilecek çok kaynaklı bir anlatım yoktur; kanıt yalın biçimin genel bulut anlamını tek başına tanıklar.","sources":["TA"],"what_is_ar":"النَّاهُور اسما للسحاب","what_is_not_ar":"لا يدخل فيه النهر المائي؛ ولا النهار؛ ولا الأعلام الخاصة"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["92:2:1"],"branch_refs":[],"candidate_id":"cand_1646d36b0ab6ee69689a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:1:compact-day-oath-unit","source_type":"word_analysis","support_ids":["sup_34de1bde60e6106aa2ac","sup_946819ccd74e669ca195"],"title":"particle and day noun form a compact unit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:1","qac_refs":["92:2:1:1"],"status":"accepted"}},{"anchor_refs":["92:2:1"],"branch_refs":[],"candidate_id":"cand_36bca4dd261aac840c21","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:1:oath-connective-force","source_type":"word_analysis","support_ids":["sup_946819ccd74e669ca195","sup_ef84f40fbba4a19c4219"],"title":"oath force and coordination work together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:1","qac_refs":["92:2:1:1"],"status":"accepted"}},{"anchor_refs":["92:2:1"],"branch_refs":[],"candidate_id":"cand_b6c693ec66d6a2da4276","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:1:serial-oath-continuity","source_type":"word_analysis","support_ids":["sup_946819ccd74e669ca195","sup_b4ff049755e7b551a244"],"title":"second member of an unresolved oath series","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:1","qac_refs":["92:2:1:1"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_6b96d4d64ada84c2b55e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:day-as-unveiling-actor","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_ea69d397861403d126ef"],"title":"sworn object becomes the verb's actor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_88f4c25c0a8b45b1d2a7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:flow-pressure-narrowed","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_1944fa2fa7f285db629b"],"title":"river-flow field becomes daylight outpouring pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_7be9e899d4ddbf626b73","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:night-day-binary","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_32d207bcd8b3169e199f"],"title":"day answers the prior night as opposite pole","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_2e5df47ae21cecb38a6a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:oath-governed-definite-day","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_1397f8fd1ae835bb9dd3"],"title":"definite day is governed as sworn object","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_44f953a67e3ea692c77d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:oath-sequence-forward-motion","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_e7903f2434dc43f8dde6"],"title":"second oath object points beyond itself","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:2"],"branch_refs":[],"candidate_id":"cand_2d24818c872d9b8e6730","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:2:unified-day-field-and-sound","source_type":"word_analysis","support_ids":["sup_0c38edc1f2c07e0af83d","sup_97d17635882f5f0d88ff"],"title":"singular definite form presents one opening field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:2","qac_refs":["92:2:1:2","92:2:1:3"],"status":"accepted"}},{"anchor_refs":["92:2:3"],"branch_refs":[],"candidate_id":"cand_25a6d43745d92846e8ea","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:3:cadence-shift","source_type":"word_analysis","support_ids":["sup_1dc34fc0e74bcb63f073","sup_44dc3311df466d7590b1"],"title":"sharp onset and open cadence mark the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:3","qac_refs":["92:2:2:1"],"status":"accepted"}},{"anchor_refs":["92:2:3"],"branch_refs":[],"candidate_id":"cand_133826fbbcb338d89e3e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:3:habitual-certainty","source_type":"word_analysis","support_ids":["sup_1dc34fc0e74bcb63f073","sup_3f6eb93ffde89bce860b"],"title":"whenever force rather than uncertain if","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:3","qac_refs":["92:2:2:1"],"status":"accepted"}},{"anchor_refs":["92:2:3"],"branch_refs":[],"candidate_id":"cand_c2254007592d0d7e730c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:3:parallel-idhā-frame","source_type":"word_analysis","support_ids":["sup_1dc34fc0e74bcb63f073","sup_ff401a05281abb62a814"],"title":"repeated temporal frame aligns night and day","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:3","qac_refs":["92:2:2:1"],"status":"accepted"}},{"anchor_refs":["92:2:3"],"branch_refs":[],"candidate_id":"cand_687fa5d64ca1cca3fbe5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"92:2:3:temporal-hinge","source_type":"word_analysis","support_ids":["sup_1dc34fc0e74bcb63f073","sup_cb4d1b220b5676fb874c"],"title":"particle binds day to its unveiling clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:3","qac_refs":["92:2:2:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_f38551885aeb9e2031c3","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:covering-reversal","source_type":"word_analysis","support_ids":["sup_98779029cc1b7fb33fcc","sup_a3ab3a24dd48240b0181"],"title":"unveiling reverses the prior covering scene","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_6dac1aa20362f3293620","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:day-subject-agency","source_type":"word_analysis","support_ids":["sup_31fc518f72d614aac93e","sup_a3ab3a24dd48240b0181"],"title":"masculine agreement makes day the self-disclosing actor","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_a973af8ff45a532c5560","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:daylight-manifestation-collocation","source_type":"word_analysis","support_ids":["sup_51f6f302b4fd3d67c6c2","sup_a3ab3a24dd48240b0181"],"title":"day noun and manifestation verb form one field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_d74162df189d57444d84","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:final-clause-closure","source_type":"word_analysis","support_ids":["sup_095aca1aea779e928b0d","sup_a3ab3a24dd48240b0181"],"title":"delayed final verb closes on manifestation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_27c53f50c6d3949d3871","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:form-v-self-unveiling","source_type":"word_analysis","support_ids":["sup_625b60c6a5b5413fff36","sup_a3ab3a24dd48240b0181"],"title":"Form V marks self-unveiling and becoming manifest","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_a32f1b370be35e6ced20","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:perfect-habitual-certainty","source_type":"word_analysis","support_ids":["sup_a3ab3a24dd48240b0181","sup_deb4eda13b324eaa9d6a"],"title":"perfect under the temporal particle gives completed recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_a67ac9f1da105c94d1bd","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:rare-theophanic-register","source_type":"word_analysis","support_ids":["sup_25cb03a4c7bd01d858de","sup_a3ab3a24dd48240b0181"],"title":"rare manifestation verb carries elevated register","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_2ef326d3f5af65eef4ae","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:root-image-clearing-disclosure","source_type":"word_analysis","support_ids":["sup_8cf5b1ec33e9b815234c","sup_a3ab3a24dd48240b0181"],"title":"clearing, polishing, and display enrich manifestation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_8ed1f82e2dd24107bb53","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:sound-and-cadence","source_type":"word_analysis","support_ids":["sup_a3ab3a24dd48240b0181","sup_d30fea19b90b2cb21e2e"],"title":"doubled center releases into final open cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:4"],"branch_refs":[],"candidate_id":"cand_3aa606e8030866f0f292","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:4:variant-contrast","source_type":"word_analysis","support_ids":["sup_1baf5171e2289554bb0b","sup_a3ab3a24dd48240b0181"],"title":"variant readings expose subject and agency alternatives","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"92:2:4","qac_refs":["92:2:3:1"],"status":"accepted"}},{"anchor_refs":["92:2:1"],"branch_refs":[],"candidate_id":"cand_a25e5d2c14ef1bc9d153","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001559"],"scope":"focus_ayah","source_local_id":"92:2:1:3","source_type":"qac_morpheme","support_ids":["sup_34c2c7d796d60f3ff7a9"],"title":"QAC root occurrence: ن ه ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:2:3"],"branch_refs":[],"candidate_id":"cand_916c10fe7317a8e5f96e","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000256"],"scope":"focus_ayah","source_local_id":"92:2:3:1","source_type":"qac_morpheme","support_ids":["sup_c6efc208ba23a0fb84a6"],"title":"QAC root occurrence: ج ل و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["92:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:2","branch_refs":["root_000256/B001","root_001559/B002"],"candidate_id":"cand_144d31dcabf292c3749f","commentary_obligation":"review","hft_ref":"hft_3318a3e0e8de139ccb22","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_opening_disclosure","source_type":"hft","support_ids":["sup_874c7c38b83d38d30918"],"title":"baseline_opening_disclosure","trust":"legacy_unbound"},{"anchor_refs":["92:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:2","branch_refs":["root_000256/B002","root_001559/B002"],"candidate_id":"cand_b60cfc02f90a5d784d58","commentary_obligation":"review","hft_ref":"hft_a52b620517c03601f4ea","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_optical_polish","source_type":"hft","support_ids":["sup_fb8ed09773bd4c50b7be"],"title":"baseline_optical_polish","trust":"legacy_unbound"},{"anchor_refs":["92:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:2","branch_refs":["root_000256/B001","root_001559/B001","root_001559/B003"],"candidate_id":"cand_f36155fd60af20406c62","commentary_obligation":"review","hft_ref":"hft_a6f083db319cd804239c","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_hydraulic_corridor","source_type":"hft","support_ids":["sup_2fcd94077e1707e120e8"],"title":"baseline_hydraulic_corridor","trust":"legacy_unbound"},{"anchor_refs":["92:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:2","branch_refs":["root_000256/B003","root_000256/B008","root_001559/B002"],"candidate_id":"cand_a11327c2c8bfde7a82db","commentary_obligation":"review","hft_ref":"hft_dfe9cb9483510adce243","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_public_display","source_type":"hft","support_ids":["sup_f2913b56e6468397184d"],"title":"baseline_public_display","trust":"legacy_unbound"},{"anchor_refs":["92:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"92:2","branch_refs":["root_000256/B004","root_001559/B003"],"candidate_id":"cand_bb5639e032b701b4c8c0","commentary_obligation":"review","hft_ref":"hft_d5bdb434ac9b7e069398","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_expulsive_clearance","source_type":"hft","support_ids":["sup_d963a133807003af2ab9"],"title":"baseline_expulsive_clearance","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:2:1:1","qac_word_ref":"92:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:2:1:2","qac_word_ref":"92:2:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","root_ar":"ن ه ر","surface_ar":"نَّهَارِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"92:2:2:1","qac_word_ref":"92:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","root_ar":"ج ل و","surface_ar":"تَجَلَّىٰ"}],"word_analysis_qac_refs":[["92:2:1:1"],["92:2:1:2","92:2:1:3"],["92:2:2:1"],["92:2:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["92:2:1","92:2:2","92:2:3","92:2:4"]},"focus_surface_evidence":{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"92:2:1:1","qac_word_ref":"92:2:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"92:2:1:2","qac_word_ref":"92:2:1","root_ar":"","surface_ar":"ٱل"},{"lemma_ar":"نَهَار","morph_features":"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"92:2:1:3","qac_word_ref":"92:2:1","root_ar":"ن ه ر","surface_ar":"نَّهَارِ"},{"lemma_ar":"إِذَا","morph_features":"STEM|POS:T|LEM:<i*aA","morpheme_role":"STEM","pos":"T","qac_ref":"92:2:2:1","qac_word_ref":"92:2:2","root_ar":"","surface_ar":"إِذَا"},{"lemma_ar":"تَجَلَّىٰ","morph_features":"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"92:2:3:1","qac_word_ref":"92:2:3","root_ar":"ج ل و","surface_ar":"تَجَلَّىٰ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["92:2:1:1"],["92:2:1:2","92:2:1:3"],["92:2:2:1"],["92:2:3:1"]],"word_analysis_refs":["92:2:1","92:2:2","92:2:3","92:2:4"],"word_rows":[{"analysis_record_ref":"92:2:1","analytic_gloss_range_en":"oath particle with connective force; locally it opens the second sworn object while continuing the oath chain","analytic_root_gloss_range_en":null,"qac_refs":["92:2:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"92:2:2","analytic_gloss_range_en":"the definite daylight period; locally a sworn-by object that becomes the implied actor of unveiling","analytic_root_gloss_range_en":"root range includes daylight/daytime, river or watercourse flow, opening or widening, harsh rebuke, and other marginal nouns; the local context selects daylight while preserving limited flow and outpouring image pressure","qac_refs":["92:2:1:2","92:2:1:3"],"root":{"arabic":"ن ه ر","transliteration":"n-h-r"},"surface":{"arabic":"ٱلنَّهَارِ","transliteration":"al-nahāri"}},{"analysis_record_ref":"92:2:3","analytic_gloss_range_en":"temporal and conditional adverb; locally when or whenever, binding the perfect verb into the day-oath circumstance","analytic_root_gloss_range_en":null,"qac_refs":["92:2:2:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"إِذَا","transliteration":"idhā"}},{"analysis_record_ref":"92:2:4","analytic_gloss_range_en":"perfect Form V intransitive/reflexive manifestation; locally the day self-discloses or becomes fully visible whenever the temporal clause occurs","analytic_root_gloss_range_en":"root range includes uncovering and manifestation, polishing and clearing, bridal display, departure or clearing away, daylight brightness, gaze, fame, and marginal gift uses; locally the manifestation and daylight-clearing branches are selected, with polishing and display imagery as narrowed pressure","qac_refs":["92:2:3:1"],"root":{"arabic":"ج ل و","transliteration":"j-l-w"},"surface":{"arabic":"تَجَلَّىٰ","transliteration":"tajallā"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":4,"words_total":4,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["92:2"],"branch_refs":["root_000256/B001","root_001559/B002"],"candidate_id":"cand_144d31dcabf292c3749f","evidence_scope":"focus_ayah","hft_ref":"hft_3318a3e0e8de139ccb22","item_id":"baseline_opening_disclosure","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_opening_disclosure","support_id":"sup_874c7c38b83d38d30918"},{"anchor_refs":["92:2"],"branch_refs":["root_000256/B002","root_001559/B002"],"candidate_id":"cand_b60cfc02f90a5d784d58","evidence_scope":"focus_ayah","hft_ref":"hft_a52b620517c03601f4ea","item_id":"baseline_optical_polish","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_optical_polish","support_id":"sup_fb8ed09773bd4c50b7be"},{"anchor_refs":["92:2"],"branch_refs":["root_000256/B001","root_001559/B001","root_001559/B003"],"candidate_id":"cand_f36155fd60af20406c62","evidence_scope":"focus_ayah","hft_ref":"hft_a6f083db319cd804239c","item_id":"baseline_hydraulic_corridor","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_hydraulic_corridor","support_id":"sup_2fcd94077e1707e120e8"},{"anchor_refs":["92:2"],"branch_refs":["root_000256/B003","root_000256/B008","root_001559/B002"],"candidate_id":"cand_a11327c2c8bfde7a82db","evidence_scope":"focus_ayah","hft_ref":"hft_dfe9cb9483510adce243","item_id":"baseline_public_display","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_public_display","support_id":"sup_f2913b56e6468397184d"},{"anchor_refs":["92:2"],"branch_refs":["root_000256/B004","root_001559/B003"],"candidate_id":"cand_bb5639e032b701b4c8c0","evidence_scope":"focus_ayah","hft_ref":"hft_d5bdb434ac9b7e069398","item_id":"baseline_expulsive_clearance","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_expulsive_clearance","support_id":"sup_d963a133807003af2ab9"}],"diagnostics":[],"lane_counts":{"global":20,"macro":6,"micro":5},"packet_summary":{"ayah_count":21,"focus_ref":"92:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء و ل","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000067","furuq_root_norm":"ء و ل","furuq_source_root_norm":"أ و ل","is_dominant":true,"target_occurrences":148,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001684","furuq_root_norm":"و ل ي","furuq_source_root_norm":"و ل ي","is_dominant":false,"target_occurrences":16,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ش ق و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000808","furuq_root_norm":"ش ق و","furuq_source_root_norm":"ش ق و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000809","furuq_root_norm":"ش ق ي","furuq_source_root_norm":"ش ق ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11","92:12","92:13","92:14","92:15","92:16","92:17","92:18","92:19","92:20","92:21"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"92:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"92:2","lane":"micro","linguistic_source_ref":"92:2","surface_ref":"92:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"92:2","target_tokens":[["Açığa",["92:2:3"]],["çıktığı",["92:2:3"]],["zaman",["92:2:2"]],["gündüze",["92:2:1"]]],"text":"Açığa çıktığı zaman gündüze,"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":11,"id":"s092-p01-001-011","label":"Contrasting forms of striving","number":1,"refs":["92:1","92:2","92:3","92:4","92:5","92:6","92:7","92:8","92:9","92:10","92:11"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:final-clause-closure","source_type":"word_analysis","support_id":"sup_095aca1aea779e928b0d","text":"{\"blocking_evidence\":null,\"headline\":\"delayed final verb closes on manifestation\",\"reader_payoff\":\"The reader notices that the ayah waits until the last word to deliver the decisive act of manifestation.\",\"reason\":\"The suppressed oath verb keeps the surface compressed, and the verb arrives after the oath object and temporal particle as the ayah's closure.\",\"representative_source_ids\":[\"QT-3513e765\",\"QT-4b0763c6\",\"QT-9cca5000\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2","source_type":"word_analysis","support_id":"sup_0c38edc1f2c07e0af83d","text":"{\"gloss_range\":\"the definite daylight period; locally a sworn-by object that becomes the implied actor of unveiling\",\"prose\":\"{{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}) is first fixed as the definite sworn-by day under {{ar:وَ}} ({{tr:wa}}), with genitive oath governance preventing it from being a simple nominative subject at the front. Its singular abstract form presents daylight as one continuous diurnal field, and the joined recited onset after {{ar:وَ}} ({{tr:wa}}) makes the particle-noun dependency audible. Yet the same noun is then recovered as the masculine subject inside {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}), so the sworn object becomes the actor of disclosure. The local sense is daylight, not river, but the {{ar:ن ه ر}} ({{tr:n-h-r}}) root field lets daylight feel like an opening out or outpouring of visibility against the prior night scene, while the oath sequence still points beyond this second object toward what follows.\",\"root_display\":\"{{ar:ن ه ر}} ({{tr:n-h-r}})\",\"root_gloss_range\":\"root range includes daylight/daytime, river or watercourse flow, opening or widening, harsh rebuke, and other marginal nouns; the local context selects daylight while preserving limited flow and outpouring image pressure\",\"surface_display\":\"{{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:oath-governed-definite-day","source_type":"word_analysis","support_id":"sup_1397f8fd1ae835bb9dd3","text":"{\"blocking_evidence\":null,\"headline\":\"definite day is governed as sworn object\",\"reader_payoff\":\"The reader notices that the day is elevated into oath evidence before it becomes part of the scene.\",\"reason\":\"The noun is definite and genitive under the oath particle, so the local grammar makes it a sworn-by object rather than an initial nominative subject.\",\"representative_source_ids\":[\"QG-06a34db7\",\"QG-c727d6e7\",\"QI-6fbd2f37\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:flow-pressure-narrowed","source_type":"word_analysis","support_id":"sup_1944fa2fa7f285db629b","text":"{\"blocking_evidence\":null,\"headline\":\"river-flow field becomes daylight outpouring pressure\",\"reader_payoff\":\"The reader notices daylight as an active outflow of visibility, while still reading the word as day rather than river.\",\"reason\":\"V4 separates the daylight branch from river and opening branches; the local oath pair with night and the unveiling verb select daylight, while root-family evidence preserves flow and opening as image pressure.\",\"representative_source_ids\":[\"QS-ac0c41ff\",\"QS-b8af1581\",\"MS-d4f8d33f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:variant-contrast","source_type":"word_analysis","support_id":"sup_1baf5171e2289554bb0b","text":"{\"blocking_evidence\":null,\"headline\":\"variant readings expose subject and agency alternatives\",\"reader_payoff\":\"The reader notices how precise the canonical surface is: masculine perfect day-agreement and self-manifesting agency are preserved against alternative parses.\",\"reason\":\"The supplied variants are useful as contrast, but the canonical local parse remains the 3ms perfect intransitive/reflexive verb agreeing with the day noun.\",\"representative_source_ids\":[\"QG-941e1a69\",\"QF-50e86521\",\"QY-9fcd4d12\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:3","source_type":"word_analysis","support_id":"sup_1dc34fc0e74bcb63f073","text":"{\"gloss_range\":\"temporal and conditional adverb; locally when or whenever, binding the perfect verb into the day-oath circumstance\",\"prose\":\"{{ar:إِذَا}} ({{tr:idhā}}) is the hinge between the sworn day and its action. It makes {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}) the temporal circumstance of {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}), so the oath is not by day in the abstract but by day whenever it unveils. Because the following verb is perfect, the recurring scene is presented with certainty and completion, while the repeated frame parallels 92:1 and makes covering and unveiling comparable at the same grammatical slot. Its initial catch marks the turn from oath object to when-clause, and its open ā ending fuses rhythmically with the unveiling verb.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِذَا}} ({{tr:idhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:rare-theophanic-register","source_type":"word_analysis","support_id":"sup_25cb03a4c7bd01d858de","text":"{\"blocking_evidence\":null,\"headline\":\"rare manifestation verb carries elevated register\",\"reader_payoff\":\"The reader notices that ordinary daylight is described with a rare manifestation verb that also resonates with divine self-disclosure at 7:143.\",\"reason\":\"The root/form profile is low occurrence and includes the Form V use at 7:143, but this resonance is narrowed so it does not replace the local daylight subject.\",\"representative_source_ids\":[\"QS-e5e89d4d\",\"MS-93552799\",\"MI-40c284da\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:day-subject-agency","source_type":"word_analysis","support_id":"sup_31fc518f72d614aac93e","text":"{\"blocking_evidence\":null,\"headline\":\"masculine agreement makes day the self-disclosing actor\",\"reader_payoff\":\"The reader notices the day itself as the grammatical actor of manifestation, not a passive backdrop.\",\"reason\":\"The 3ms agreement and implicit-subject evidence resolve {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}) back to {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}).\",\"representative_source_ids\":[\"QG-50e76c96\",\"QG-e19e4fdc\",\"QS-d034189a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:night-day-binary","source_type":"word_analysis","support_id":"sup_32d207bcd8b3169e199f","text":"{\"blocking_evidence\":null,\"headline\":\"day answers the prior night as opposite pole\",\"reader_payoff\":\"The reader notices that the ayah is not naming another time at random; it answers the night oath of 92:1 with the opposite temporal pole.\",\"reason\":\"The contextual profiles show a strong day-night pairing, and the local oath sequence places this noun immediately after the night-covering scene of 92:1.\",\"representative_source_ids\":[\"QS-a1902552\",\"MT-505ffe41\",\"QB-949ea92b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:2:1:3","source_type":"qac_morpheme","support_id":"sup_34c2c7d796d60f3ff7a9","text":"{\"lemma_ar\":\"نَهَار\",\"morph_features\":\"STEM|POS:N|LEM:nahaAr|ROOT:nhr|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"92:2:1:3\",\"qac_word_ref\":\"92:2:1\",\"root_ar\":\"ن ه ر\",\"surface_ar\":\"نَّهَارِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:1:compact-day-oath-unit","source_type":"word_analysis","support_id":"sup_34de1bde60e6106aa2ac","text":"{\"blocking_evidence\":null,\"headline\":\"particle and day noun form a compact unit\",\"reader_payoff\":\"The reader notices the particle leaning directly into the definite day noun as a compact sworn-object onset.\",\"reason\":\"The surface sequence joins {{ar:وَ}} ({{tr:wa}}) to {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}), making the oath dependency audible and visible at the start of the ayah.\",\"representative_source_ids\":[\"QF-9c5f897e\",\"MT-ae5a114f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:3:habitual-certainty","source_type":"word_analysis","support_id":"sup_3f6eb93ffde89bce860b","text":"{\"blocking_evidence\":null,\"headline\":\"whenever force rather than uncertain if\",\"reader_payoff\":\"The reader notices each dawn-like unveiling as a repeated certainty, not as a doubtful condition.\",\"reason\":\"The cyclical daylight scene and perfect verb after {{ar:إِذَا}} ({{tr:idhā}}) select a temporal-habitual sense, while the profile gives no local uncertainty or negation.\",\"representative_source_ids\":[\"QG-df0442fa\",\"MG-2abda42f\",\"QS-f5b2e862\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:3:cadence-shift","source_type":"word_analysis","support_id":"sup_44dc3311df466d7590b1","text":"{\"blocking_evidence\":null,\"headline\":\"sharp onset and open cadence mark the clause\",\"reader_payoff\":\"The reader hears the temporal clause begin with a distinct catch and then merge rhythmically with the unveiling verb.\",\"reason\":\"The particle's initial hamza marks the shift from oath object to temporal specification, and its open ending pairs with the final verb's open cadence.\",\"representative_source_ids\":[\"QP-1f6fafbe\",\"QP-fa8e78e5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:daylight-manifestation-collocation","source_type":"word_analysis","support_id":"sup_51f6f302b4fd3d67c6c2","text":"{\"blocking_evidence\":null,\"headline\":\"day noun and manifestation verb form one field\",\"reader_payoff\":\"The reader notices that the day noun is matched with a manifestation verb, making daylight and disclosure one local phrase-field.\",\"reason\":\"The contextual co-occurrence signal and local adjacency tie {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}) to {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}) as the day-action pairing.\",\"representative_source_ids\":[\"QI-5f149d4d\",\"QE-7e58bb38\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:form-v-self-unveiling","source_type":"word_analysis","support_id":"sup_625b60c6a5b5413fff36","text":"{\"blocking_evidence\":null,\"headline\":\"Form V marks self-unveiling and becoming manifest\",\"reader_payoff\":\"The reader notices that manifestation is built into the derived form, so the day is grammatically made to unfold into visibility.\",\"reason\":\"QAC and attachment evidence identify the local verb as Form V, intransitive/reflexive, with no object; the ta-prefix and doubled middle consonant visibly support that derived force.\",\"representative_source_ids\":[\"QF-47424b1a\",\"QF-b138a019\",\"MF-cff17414\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:root-image-clearing-disclosure","source_type":"word_analysis","support_id":"sup_8cf5b1ec33e9b815234c","text":"{\"blocking_evidence\":null,\"headline\":\"clearing, polishing, and display enrich manifestation\",\"reader_payoff\":\"The reader notices daylight as radiant disclosure produced by clearing opacity, not as a bare sunrise label.\",\"reason\":\"V4 supports branches of manifestation, polishing, display, clearing away, and daylight brightness; local grammar selects manifestation of daylight while preserving the concrete clearing and radiance pressure.\",\"representative_source_ids\":[\"QS-09386699\",\"QS-34787c69\",\"QS-b29697a3\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:1","source_type":"word_analysis","support_id":"sup_946819ccd74e669ca195","text":"{\"gloss_range\":\"oath particle with connective force; locally it opens the second sworn object while continuing the oath chain\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) is not a loose conjunction. It carries oath force into {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}) while linking this oath back to 92:1, so the day is heard as the second member of one continuing oath series rather than as a fresh detached sentence. That series moves through night, day, and the next sworn object in 92:3 before its answer, so the particle also leaves the oath construction open and makes the reader wait with the sequence instead of resolving the claim inside this ayah.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:unified-day-field-and-sound","source_type":"word_analysis","support_id":"sup_97d17635882f5f0d88ff","text":"{\"blocking_evidence\":null,\"headline\":\"singular definite form presents one opening field\",\"reader_payoff\":\"The reader notices the day as one definite expanse whose recited onset opens outward after the oath particle.\",\"reason\":\"The singular abstract definite noun and the joined recitation after {{ar:وَ}} ({{tr:wa}}) support a unified daylight field rather than a countable object.\",\"representative_source_ids\":[\"QF-4f137527\",\"QP-307f08fe\",\"QP-429e769a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:covering-reversal","source_type":"word_analysis","support_id":"sup_98779029cc1b7fb33fcc","text":"{\"blocking_evidence\":null,\"headline\":\"unveiling reverses the prior covering scene\",\"reader_payoff\":\"The reader notices the verb as the active reversal of the night-covering action in 92:1.\",\"reason\":\"The boundary rows place 92:2 after the night-covering scene of 92:1, and the local verb supplies the opposite motion of uncovering and shining forth.\",\"representative_source_ids\":[\"QS-b96ff912\",\"QE-0d6f332f\",\"QB-80126bd6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4","source_type":"word_analysis","support_id":"sup_a3ab3a24dd48240b0181","text":"{\"gloss_range\":\"perfect Form V intransitive/reflexive manifestation; locally the day self-discloses or becomes fully visible whenever the temporal clause occurs\",\"prose\":\"{{ar:تَجَلَّىٰ}} ({{tr:tajallā}}) carries the ayah's final semantic weight: the day does not merely exist after night; it manifests itself. Its Form V shape and omitted masculine subject route the action back to {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}), while {{ar:إِذَا}} ({{tr:idhā}}) with the perfect makes the manifestation recur as a completed certainty. The root's uncovering, clearing, polishing, and display fields make daylight feel like visibility released from cover, but the local frame keeps the selected sense to daylight self-disclosure rather than importing every branch. Because the same rare manifestation verb resonates with divine self-disclosure at 7:143, the daylight scene carries an elevated register while still keeping day as the local subject. Variant readings sharpen the received surface by contrast: the canonical form preserves masculine day-agreement and self-manifesting agency. Its doubled center and final open ā make the manifestation feel concentrated and released, and that cadence points forward to the oath-answer in 92:4.\",\"root_display\":\"{{ar:ج ل و}} ({{tr:j-l-w}})\",\"root_gloss_range\":\"root range includes uncovering and manifestation, polishing and clearing, bridal display, departure or clearing away, daylight brightness, gaze, fame, and marginal gift uses; locally the manifestation and daylight-clearing branches are selected, with polishing and display imagery as narrowed pressure\",\"surface_display\":\"{{ar:تَجَلَّىٰ}} ({{tr:tajallā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:1:serial-oath-continuity","source_type":"word_analysis","support_id":"sup_b4ff049755e7b551a244","text":"{\"blocking_evidence\":null,\"headline\":\"second member of an unresolved oath series\",\"reader_payoff\":\"The reader notices that the sworn assertion has not arrived yet; the particle keeps the series open across ayah boundaries.\",\"reason\":\"The bundle identifies the oath as part of the 92:1-4 unit, so the repeated particle continues the oath frame until the later response.\",\"representative_source_ids\":[\"MG-fbdb492d\",\"QT-0c200c32\",\"QB-5fd6aeb1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"92:2:3:1","source_type":"qac_morpheme","support_id":"sup_c6efc208ba23a0fb84a6","text":"{\"lemma_ar\":\"تَجَلَّىٰ\",\"morph_features\":\"STEM|POS:V|PERF|LEM:tajal~aY`|ROOT:jlw|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"92:2:3:1\",\"qac_word_ref\":\"92:2:3\",\"root_ar\":\"ج ل و\",\"surface_ar\":\"تَجَلَّىٰ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:3:temporal-hinge","source_type":"word_analysis","support_id":"sup_cb4d1b220b5676fb874c","text":"{\"blocking_evidence\":null,\"headline\":\"particle binds day to its unveiling clause\",\"reader_payoff\":\"The reader notices that the day is sworn by at the moment of unveiling, not left as an unqualified time noun.\",\"reason\":\"Attachment evidence identifies {{ar:إِذَا}} ({{tr:idhā}}) as opening the temporal clause whose predicate is {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}).\",\"representative_source_ids\":[\"QG-6ec83cf7\",\"QG-d7e8b6d0\",\"QT-c4dd5652\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:sound-and-cadence","source_type":"word_analysis","support_id":"sup_d30fea19b90b2cb21e2e","text":"{\"blocking_evidence\":null,\"headline\":\"doubled center releases into final open cadence\",\"reader_payoff\":\"The reader hears the manifestation concentrate at the doubled consonant and then open into the final cadence.\",\"reason\":\"The shaddah, lateral sound, alif maqsurah ending, and shared open cadence with {{ar:إِذَا}} ({{tr:idhā}}) support the sound-shape payoff without changing the lexical parse.\",\"representative_source_ids\":[\"QP-440aa2f6\",\"QP-99ac94ee\",\"MP-69bcb8f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:4:perfect-habitual-certainty","source_type":"word_analysis","support_id":"sup_deb4eda13b324eaa9d6a","text":"{\"blocking_evidence\":null,\"headline\":\"perfect under the temporal particle gives completed recurrence\",\"reader_payoff\":\"The reader notices daylight's unveiling as a recurring event presented with accomplished certainty.\",\"reason\":\"The verb is perfect inside the {{ar:إِذَا}} ({{tr:idhā}}) clause, so the aspect supports habitual certainty rather than an uncertain or merely ongoing process.\",\"representative_source_ids\":[\"QG-69800006\",\"MG-f904ca04\",\"QB-84b4f881\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:oath-sequence-forward-motion","source_type":"word_analysis","support_id":"sup_e7903f2434dc43f8dde6","text":"{\"blocking_evidence\":null,\"headline\":\"second oath object points beyond itself\",\"reader_payoff\":\"The reader notices that the day is foregrounded before its unveiling predicate and still leaves the oath series moving forward.\",\"reason\":\"Word order places the sworn object before the temporal predicate, and the oath-response unit remains open beyond this ayah.\",\"representative_source_ids\":[\"QT-9fd8fce9\",\"QB-21a89770\",\"QB-f0876e8d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:2:day-as-unveiling-actor","source_type":"word_analysis","support_id":"sup_ea69d397861403d126ef","text":"{\"blocking_evidence\":null,\"headline\":\"sworn object becomes the verb's actor\",\"reader_payoff\":\"The reader notices the day move from oath object into the implied subject that performs the unveiling.\",\"reason\":\"Attachment evidence resolves the 3ms subject agreement on {{ar:تَجَلَّىٰ}} ({{tr:tajallā}}) back to {{ar:ٱلنَّهَارِ}} ({{tr:al-nahāri}}).\",\"representative_source_ids\":[\"QG-ad0a91de\",\"QS-5ecdb2ca\",\"QI-84704d5b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:1:oath-connective-force","source_type":"word_analysis","support_id":"sup_ef84f40fbba4a19c4219","text":"{\"blocking_evidence\":null,\"headline\":\"oath force and coordination work together\",\"reader_payoff\":\"The reader notices that one particle both swears by the day and keeps the night-day oath sequence continuous.\",\"reason\":\"QAC marks {{ar:وَ}} ({{tr:wa}}) as conjunction and oath particle, and the attachment evidence licenses compressed oath ellipsis rather than a merely narrative connector.\",\"representative_source_ids\":[\"QG-2474bdef\",\"QS-1c3ce057\",\"QI-358505d5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"92:2:3:parallel-idhā-frame","source_type":"word_analysis","support_id":"sup_ff401a05281abb62a814","text":"{\"blocking_evidence\":null,\"headline\":\"repeated temporal frame aligns night and day\",\"reader_payoff\":\"The reader notices 92:1 and 92:2 as matching temporal frames whose verbs then contrast covering with unveiling.\",\"reason\":\"The repeated temporal particle makes the two oath clauses structurally comparable while leaving the local verb contrast to carry the difference.\",\"representative_source_ids\":[\"MT-2d990c16\",\"QB-d9d6873e\",\"QB-de4cf96a\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_001559/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001559","role":"The daylight-opening branch supplies the expanding lit interval and makes it the temporal substrate of disclosure.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"The uncovering branch supplies emergence after concealment and makes the predicate an event of disclosure.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"The verse presents daybreak as an active threshold in which a field of visibility opens and the day comes forth within its own opening.","before":"The verse names daytime at a moment when it is simply visible."},"confidence":"strong","focus_anchor":"The word-1 day noun and the word-3 reflexive manifestation verb form a temporal event rather than a static description.","mechanism":"A bounded interval opens in light while what was hidden becomes perceptible; the day is both the arriving field of visibility and the participant that comes forth within it.","model_id":"baseline_opening_disclosure"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_opening_disclosure","source_type":"hft","support_id":"sup_874c7c38b83d38d30918","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000256/B002","root_001559/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001559","role":"The lit-day branch supplies illumination as the material in which visual distinctions become available.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B002","mapped_root_id":"root_000256","role":"The polishing-and-sight-clearing branch supplies removal of visual impedance and functions as the mechanism of manifestness.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"Day acts as a clearing operation upon perception, making other things discriminable as it manifests.","before":"Day appears as a luminous object."},"confidence":"medium","focus_anchor":"The manifestation verb at word 3 can describe not only appearance but the clearing of a medium or faculty of sight.","mechanism":"Daylight works like a polishing operation: obscurity is removed from the visual field until forms can be distinguished. Manifestation is thus produced clarity, not merely added brightness.","model_id":"baseline_optical_polish"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_optical_polish","source_type":"hft","support_id":"sup_fb8ed09773bd4c50b7be","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000256/B001","root_001559/B001","root_001559/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001559","role":"The river-course branch supplies directed flow that cuts a traversable channel and models daylight's advance.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001559","role":"The widening-until-flow branch supplies spatial expansion and makes openness an effect of passage.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_000256","role":"The manifestation branch converts the imagined channel's opening into an observable disclosure.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"Daylight makes its own corridor, cutting and widening a course through what had been visually closed.","before":"Daylight fills an already available space."},"confidence":"exploratory","focus_anchor":"The day noun at word 1 carries channel-cutting and widening branches, while the word-3 verb anchors the result in visible emergence.","mechanism":"The advance of day can be pictured as a flowing course that cuts and widens a corridor through obscurity. Visibility is spatially made by passage rather than switched on all at once.","model_id":"baseline_hydraulic_corridor"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_hydraulic_corridor","source_type":"hft","support_id":"sup_2fcd94077e1707e120e8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000256/B003","root_000256/B008","root_001559/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001559","role":"The opening day branch supplies the public interval in which presentation can occur.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000256","role":"The ceremonial-display branch supplies a transition from withheld to presented and gives manifestation a social staging.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000256","role":"The searching-gaze branch supplies an implied witness and makes visibility relational rather than purely physical.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"The day presents itself in a scene of display and regard, making manifestation an encounter between appearance and gaze.","before":"The verse reports an impersonal astronomical transition."},"confidence":"exploratory","focus_anchor":"The reflexive word-3 verb permits the day to be construed as presenting itself to a gaze.","mechanism":"Manifestation has a social-visual structure: something formerly withheld is displayed, and an observer's gaze rises to meet it. Day is staged presence, not only illumination.","model_id":"baseline_public_display"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_public_display","source_type":"hft","support_id":"sup_f2913b56e6468397184d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَٱلنَّهَارِ إِذَا تَجَلَّىٰ","ayah_ref":"92:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000256/B004","root_001559/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001559","role":"The opening-and-widening branch supplies the production of room in which the day can spread.","root":"ن ه ر","source_ref":"92:2","source_word_indices":["1"]},{"branch_id":"B004","mapped_root_id":"root_000256","role":"The departure-and-expulsion branch supplies displacement and makes clearance the underside of manifestation.","root":"ج ل و","source_ref":"92:2","source_word_indices":["3"]}],"changed_reading":{"after":"Manifestation is a replacement event: day spreads by clearing another occupancy from the field.","before":"Manifestation adds a visible presence."},"confidence":"medium","focus_anchor":"The word-3 manifestation root includes departure and expulsion, while the word-1 day root includes opening and enlargement.","mechanism":"The day becomes manifest by making room: its expansion dislodges what occupied the visual field. Disclosure is simultaneously arrival and evacuation.","model_id":"baseline_expulsive_clearance"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_expulsive_clearance","source_type":"hft","support_id":"sup_d963a133807003af2ab9","trust":"legacy_unbound"}]}
</lane_packet_json>
