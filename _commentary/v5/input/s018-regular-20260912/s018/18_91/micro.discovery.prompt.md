# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **18:91**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s018-regular-20260912/s018/18_91/micro.discovery.json` and modify nothing
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
  "ayah_ref": "18:91",
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
{"analysis_context":{"analysis_id":"s018-regular-20260912","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"18:91","host_surah":18,"lane_context_refs":[],"ordered_context_refs":["18:83","18:84","18:85","18:86","18:87","18:88","18:89","18:90","18:92","18:93","18:94","18:95","18:96","18:97","18:98","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal yalnız fiziksel çevreleme ve çevrili yapı alanındadır; koruma, eksiksiz bilme ve yıkıma uğratma anlamlarını içermez.","branch_kind":"mixed_non_bare","branch_ref":"root_000372/B001","candidate_links":[{"candidate_id":"cand_969feb829d06e7af46c2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"fiziksel olarak çevresini sarma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne, kişi ya da yer başka bir şey tarafından fiziksel olarak çevrelenir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir yerin ya da ekili alanın çevresine, içindekileri kuşatan bir duvar yapılabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yiyecek için çevrili bir yer yapılması ve atların bir kişinin çevresini sarması fiziksel çevrelemenin örnekleridir."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın genel fiziksel çekirdeğini ve bu çekirdekten doğan çevrili yapı okumalarını kapsayan en kısa doğal karşılıktır.","boundary_detail":"Bu dal yalnız fiziksel çevreleme ve çevrili yapı alanındadır; koruma, eksiksiz bilme ve yıkıma uğratma anlamlarını içermez.","branch_image_ar":"الإحاطة الحسية والتحويط","concept_gloss":"fiziksel olarak çevresini sarma","contextual_glosses":[{"applicability":"Bir kişi, nesne ya da yerin fiziksel olarak her yandan çevrelendiği genel eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Fiziksel sarma hareketini ve çevreleyen ile çevrelenen arasındaki ilişkiyi korur."},"facet_ids":["F001"],"text":"çevresini sardı","usage_role":"general"},{"applicability":"Bir yerin ya da ekili alanın çevresine onu sınırlayan duvar yapılmasını anlatan yapı bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Duvar yapma işlemini ve duvarın içteki alanı fiziksel olarak çevrelemesini birlikte korur."},"facet_ids":["F002"],"text":"çevresine duvar ördü","usage_role":"contextual"}],"definition":"Bir şeyin başka bir şeyin çevresini fiziksel olarak sarmasıdır; duvar örme, çevrili bir saklama yeri yapma ve atların bir kişinin çevresinde halka oluşturması bu çekirdeğin özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne, kişi ya da yer başka bir şey tarafından fiziksel olarak çevrelenir."},{"facet_id":"F002","role":"specialization","statement":"Bir yerin ya da ekili alanın çevresine, içindekileri kuşatan bir duvar yapılabilir."},{"facet_id":"F003","role":"example","statement":"Yiyecek için çevrili bir yer yapılması ve atların bir kişinin çevresini sarması fiziksel çevrelemenin örnekleridir."}],"identity_rationale":"Kaynak sözü, bir şeyin başka bir şeyi fiziksel olarak çevrelemesini temel alır; duvar yapma, çevrili bir saklama yeri ve atların bir kişinin çevresinde halka oluşturması bu fiziksel çekirdeğin açık gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyin çevresini fiziksel olarak sardı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"çevresine duvar ördü"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir yeri çevreleyen duvar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yiyecek için yapılmış çevrili saklama yeri"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"atlar kişinin çevresini sardı"}],"lexicalization_note":"Yalın eylem fiziksel çevrelemeyi bildirir; duvar örme ve atların birini çevrelemesi ise kendi yapılarıyla sınırlı özel gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; yayımlanan iki komşu, fiziksel çevrelemenin toplu halka oluşturma ve yüksek sur alanlarıyla karışabileceği en belirgin sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği genel fiziksel çevrelemedir ve yapı nesnelerine kadar uzanır; komşu dal ise bakışını hedefe yöneltmiş insan topluluğunun çevredeki duruşunu anlatır, bu yüzden olağan kullanımda birbirinin yerine geçmez.","focus_only":"Odak dal, duvar ve çevrili saklama yeri gibi cansız çevreleyicileri ve atların bir kişiyi sarmasını da kapsar.","gloss":"çevresinde toplanıp bakma","neighbor_only":"Komşu dal, insanların bir şeyin çevresinde durup ona bakması biçimindeki toplu duruşu özellikle belirtir.","neighbor_ref":"root_001308/B012","relation_type":"near_neighbor","shared_zone":"İki dalda da bir hedefin çevresinde fiziksel bir halka ya da kuşak oluşur."},{"boundary_match":"field_only","distinction":"Odak dal duvarı çevreleme işlevi bakımından ele alır; komşu dalın çekirdeği ise yüksek sur ya da duvar nesnesi ve onun yüksekliğine bağlı eylemlerdir.","focus_only":"Odak dal, her tür fiziksel sarma hareketini ve çevrili yer yapmayı kapsar.","gloss":"yüksek sur ve duvar","neighbor_only":"Komşu dal, özellikle yüksek şehir surunu, duvarın yüksekliğini ve duvara çıkmayı kapsar.","neighbor_ref":"root_000758/B002","relation_type":"same_field","shared_zone":"Her iki dalda da bir alanı sınırlayan duvar bulunabilir."}],"source_phrase_ar":"هو الشيء يطيف بالشيء (maqayis)؛ احتاطت الخيل بفلان وأحاطت به أي أحدقت (ayn;sihah;tahdhib)؛ الحائط لأنه يحوط ما فيه وحوطت حائطا (ayn;tahdhib)؛ الحائط الجدار الذي يحوط بالمكان (mufradat)؛ الحواطة حظيرة تتخذ للطعام (maqayis;sihah)","source_summary":"Kaynaklar fiziksel çevreleme çekirdeğinde birleşir; genel sarma hareketini, çevreleyen duvarı, yiyecek için yapılan çevrili yeri ve atların bir kişiyi halka içine almasını birlikte gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الإحاطة الحسية بالشيء أو المكان، والتحويط بالحائط أو الحظيرة، وإحداق الخيل بالإنسان","what_is_not_ar":"ليس العلم المحيط ولا الرعاية والحفظ ولا الهلاك الواقع بالمحاط به"},"support_links":["sup_9efe344c8d839dcee658"]},{"boundary":"Dalın merkezi koruma ve sürekli gözetmedir; önlem alma, engellenme ve şefkat okumaları genel yalın anlama dönüştürülmemelidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000372/B002","candidate_links":[{"candidate_id":"cand_d245abba4eba71397244","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"koruyup gözetme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi ya da şey korunur, gözetilir ve durumuyla sürekli ilgilenilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin kendisi için güvenilir yolu seçmesi, koruma amacını önceden önlem alma davranışına taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir edilgen yapıda, kişilerin ilerlemesinin engellenmesi anlatılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Belirli bir söz öbeğinde, bir kimsenin başkasına karşı şefkat ve yakınlık duyması anlatılır."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yalın biçimlerdeki merkezi anlamını verir; yapı bağımlı önlem, engellenme ve şefkat okumaları bağlama göre ayrıca belirtilmelidir.","boundary_detail":"Dalın merkezi koruma ve sürekli gözetmedir; önlem alma, engellenme ve şefkat okumaları genel yalın anlama dönüştürülmemelidir.","branch_image_ar":"الحفظ والحياطة","concept_gloss":"koruyup gözetme","contextual_glosses":[{"applicability":"Kişinin kendisini korumak amacıyla daha güvenilir yolu seçtiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Zararı önleme amacını ve güvenli olanı seçme davranışını korur."},"facet_ids":["F002"],"text":"önlem aldı","usage_role":"contextual"},{"applicability":"Kişilerin gitmesinin ya da amaçlarına ulaşmasının engellendiği özel edilgen yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dış bir etken tarafından engellenme ve hareket edememe sonucunu korur."},"facet_ids":["F003"],"text":"alıkonuldular","usage_role":"contextual"},{"applicability":"Bir kimsenin başka birine yönelik şefkat ve yakınlığını bildiren özel söz öbeğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yönelen şefkat, yakınlık ve duygusal gözetme tutumunu korur."},"facet_ids":["F004"],"text":"sana karşı şefkat besliyor","usage_role":"explanatory"}],"definition":"Bir kimseyi ya da şeyi koruyup sürekli gözeterek zarar görmesini önlemeye çalışmaktır; güvenli yolu seçme, engellenme ve şefkat gösterme okumaları yalnız tanıklanan özel yapılarda ortaya çıkar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi ya da şey korunur, gözetilir ve durumuyla sürekli ilgilenilir."},{"facet_id":"F002","role":"extension","statement":"Kişinin kendisi için güvenilir yolu seçmesi, koruma amacını önceden önlem alma davranışına taşır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir edilgen yapıda, kişilerin ilerlemesinin engellenmesi anlatılır."},{"facet_id":"F004","role":"associated_use","statement":"Belirli bir söz öbeğinde, bir kimsenin başkasına karşı şefkat ve yakınlık duyması anlatılır."}],"identity_rationale":"Kaynak sözü koruyup gözetmeyi temel anlam olarak doğrular; güvenli yolu seçme, engellenme ve şefkat gösterme ise bu çekirdekle ilişkili fakat yalnız belirli biçimlerde görülen yan kullanımlardır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"onu koruyup gözetti"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"koruma, gözetme ve sürekli ilgilenme"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"güvenli yolu seçerek önlem alma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sana karşı şefkat ve yakınlık besliyor"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"alıkonulmanız dışında"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme"}],"lexicalization_note":"Yalın biçimler koruyup gözetmeyi bildirir; önlem alma, engellenme ve şefkat gösterme okumaları yalnız tanıklanan biçim ve söz öbeklerinde geçerlidir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; koruma alanındaki en yakın karşılık ile aynı kökün fiziksel çevreleme dalı, okuyucunun karıştırabileceği iki temel sınırı yeterince gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Merkezi koruma anlamlarında büyük ölçüde örtüşürler; odak dalın yapı bağımlı önlem ve şefkat uzantıları ile komşu dalın bekçilik ve emanet rolleri tam karşılıklılığı engeller.","focus_only":"Odak dal, güvenli yolu seçme, belirli bir yapıda engellenme ve şefkat gösterme uzantılarını da içerir.","gloss":"koruma ve gözetme","neighbor_only":"Komşu dal, korumanın yanı sıra bekçilik, emanet sorumluluğu ve görevli koruyucu rollerini açıkça kapsar.","neighbor_ref":"root_000342/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kişi ya da şeyi zarar görmesin diye koruma, gözetme ve durumuyla ilgilenme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal işlevsel korumayı ve ilgiyi, komşu dal ise uzamsal çevrelemeyi temel alır; birinin sonucu ötekinin fiziksel düzenini gerektirmez.","focus_only":"Odak dalın sonucu bir kişi ya da şeyin korunması, gözetilmesi veya zararının önlenmesidir.","gloss":"fiziksel çevreleme","neighbor_only":"Komşu dal, koruma amacı gerektirmeden yalnız fiziksel olarak çevreleme ve duvarla kuşatma bildirir.","neighbor_ref":"root_000372/B001","relation_type":"near_neighbor","shared_zone":"Çevresini sarma düşüncesi, koruyup kollama eylemiyle kavramsal bir bağ kurabilir."}],"source_phrase_ar":"حطت الرجل أحوطه حوطا إذا حفظته (jamhara)؛ حاطه حيطة إذا تعاهده (ayn;tahdhib)؛ كلأه ورعاه (sihah)؛ الحياطة الحفظ والاحتياط استعمال ما فيه الحياطة (mufradat)؛ تستعمل في المنع (mufradat)؛ مع فلان حيطة لك أي تحنن وتعطف (sihah)","source_summary":"Kaynaklar koruma, gözetme ve sürekli ilgilenme çekirdeğini paylaşır; ayrıca bu çekirdeğin güvenilir yolu seçme, engellenme ve birine şefkat gösterme yönündeki yapı bağımlı uzantılarını bildirir.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"حفظ الشيء ورعايته وتعاهده، وما يتفرع عنه من الاحتياط والمنع والتعطف","what_is_not_ar":"ليس مجرد الإحداق المكاني ولا بلوغ العلم أقصاه"},"support_links":["sup_aeda0139e0e66cf77048"]},{"boundary":"Anlam, eşeğin sürüsünü toplayıp bir araya sürmesi yapısına bağlıdır; genel toplama ya da fiziksel çevreleme anlamı olarak genişletilemez.","branch_kind":"collocation","branch_ref":"root_000372/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"eşeğin sürüsünü bir araya toplaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eşek, kendi sürüsünün dağılmış üyelerini bir araya toplar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toplama, sürü üyelerini yöneltip aynı yerde buluşturan hayvan güdümü olarak gerçekleşir."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız tanıklanan hayvan ve sürü ilişkisini ifade eder; başka nesne ya da insan topluluklarının genel olarak toplanmasına aktarılmaz.","boundary_detail":"Anlam, eşeğin sürüsünü toplayıp bir araya sürmesi yapısına bağlıdır; genel toplama ya da fiziksel çevreleme anlamı olarak genişletilemez.","branch_image_ar":"جمع العانة وحوطها","concept_gloss":"eşeğin sürüsünü bir araya toplaması","contextual_glosses":[{"applicability":"Eşeğin dağılmış sürü üyelerini yönlendirip tek bir topluluk durumuna getirdiği anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem dağınık sürüyü toplama sonucunu hem de üyeleri yönlendirerek bir araya getirme sürecini korur."},"facet_ids":["F001","F002"],"text":"sürüsünü toparlayıp bir araya sürdü","usage_role":"contextual"}],"definition":"Eşeğin dağılmış sürüsünü yönlendirerek tek yerde bir araya toplamasını bildiren özel yapıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eşek, kendi sürüsünün dağılmış üyelerini bir araya toplar."},{"facet_id":"F002","role":"specialization","statement":"Toplama, sürü üyelerini yöneltip aynı yerde buluşturan hayvan güdümü olarak gerçekleşir."}],"identity_rationale":"Kaynak sözü yalnız eşeğin kendi sürüsünü bir araya toplamasını bildirir; dağınık öğeleri genel olarak toplama fikri bulunsa da dalın kimliği bu hayvan ve sürü yapısıyla açıkça sınırlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"eşek kendi sürüsünü toplayıp bir araya sürdü"}],"lexicalization_note":"Tanıklık yalnız eşeğin kendi sürüsünü toplaması yapısındadır; tanım bu eylemi bağımsız ve genel bir toplama anlamına dönüştürmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel toplama ile hayvan sürme dalları, bu özel yapının hem sonuç hem de katılımcı sınırını en açık biçimde belirler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel toplamanın hayvan güdümüne bağlı özel bir gerçekleşmesidir; komşu dalın katılımcıları ve nesneleri sınırsız olduğundan iki ifade yalnız sürü bağlamında yaklaşır.","focus_only":"Odak dal, eyleyenin eşek ve toplananın onun sürüsü olmasını gerektiren dar bir yapıdır.","gloss":"dağınık şeyleri toplama","neighbor_only":"Komşu dal, mal, insan ve çeşitli yerlerden gelen başka öğeler dahil her tür dağınık şeyi toplamayı kapsar.","neighbor_ref":"root_000259/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın sonucu, dağılmış üyelerin tek bir topluluk durumuna gelmesidir."},{"boundary_match":"partial","distinction":"Odak dal yönlendirmeyi toplama sonucuna bağlar; komşu dalın çekirdeği ise hareket ettirmedir ve sonuç toplama olabileceği gibi gönderme ya da dağıtma da olabilir.","focus_only":"Odak dalda sürme hareketinin zorunlu sonucu sürünün bir araya toplanmasıdır.","gloss":"hayvanları sürme ve yöneltme","neighbor_only":"Komşu dal hayvanı yumuşakça sürmeyi, sesle yöneltmeyi, göndermeyi ve dağıtmayı da kapsar.","neighbor_ref":"root_000115/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da hayvan topluluğunun hareketi bir eyleyen tarafından yönlendirilir."}],"source_phrase_ar":"الحمار يحوط عانته يجمعها (maqayis;ayn;sihah;tahdhib)","source_summary":"Kaynaklar, eşeğin kendi sürüsünü toplayıp bir araya getirdiği yapı üzerinde birleşir ve bu kullanımı genel toplama eyleminden daha dar biçimde tanıklar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"جمع المتفرق وسوق الجماعة حتى تجتمع، كحوط الحمار عانته","what_is_not_ar":"ليس الحائط ولا الحياطة بمعنى الحفظ"},"support_links":[]},{"boundary":"Dal, tanıklanan eksiksiz bilme ve bütünüyle elde etme yapılarıyla sınırlıdır; sıradan bilgi ya da kısmi edinme bu sınıra girmez.","branch_kind":"collocation","branch_ref":"root_000372/B004","candidate_links":[{"candidate_id":"cand_5b49b28e7610e428562b","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"bir şeyi bütünüyle bilme veya elde etme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşlem, konusu olan şeyin yalnız bir bölümüne değil tamamına ulaşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bilgi uygulamasında şeyin varlığı, türü, ölçüsü ve niteliği dahil bütün yönleri bilinir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Elde etme uygulamasında şeyin bir bölümü değil bütünü ele geçirilir ve denetim altına alınır."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iki tanıklanmış uygulamasını ortak tamamlık ölçütüyle birlikte verir ve kısmi bilgi ya da edinmeden ayırır.","boundary_detail":"Dal, tanıklanan eksiksiz bilme ve bütünüyle elde etme yapılarıyla sınırlıdır; sıradan bilgi ya da kısmi edinme bu sınıra girmez.","branch_image_ar":"تمام الإحاطة علما وإحرازا","concept_gloss":"bir şeyi bütünüyle bilme veya elde etme","contextual_glosses":[{"applicability":"Bir şeyin varlığı, türü, ölçüsü ve niteliği dahil bütün yönlerinin bilindiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin konuya kısmen değil bütün belirleyici yönleriyle ulaşması koşulunu korur."},"facet_ids":["F001","F002"],"text":"konuyu bütün yönleriyle biliyor","usage_role":"contextual"},{"applicability":"Bir nesnenin ya da varlığın hiçbir bölümü dışarıda kalmadan bütünüyle elde edildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Elde etmenin şeyin bir parçasıyla sınırlı kalmayıp tamamına ulaşmasını korur."},"facet_ids":["F001","F003"],"text":"şeyin tamamını elde etti","usage_role":"contextual"}],"definition":"Bir şeyi bütünüyle elde edip denetim altına almak ya da onun varlığını, türünü, ölçüsünü ve niteliğini eksiksiz bilmek üzere tamamına ulaşmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşlem, konusu olan şeyin yalnız bir bölümüne değil tamamına ulaşır."},{"facet_id":"F002","role":"specialization","statement":"Bilgi uygulamasında şeyin varlığı, türü, ölçüsü ve niteliği dahil bütün yönleri bilinir."},{"facet_id":"F003","role":"specialization","statement":"Elde etme uygulamasında şeyin bir bölümü değil bütünü ele geçirilir ve denetim altına alınır."}],"identity_rationale":"Kaynak sözü ortak bir eksiksizlik ölçütü altında iki uygulama verir: bir şeyi bütünüyle elde etmek ve onun varlığı, türü, ölçüsü ile niteliğini son sınırına kadar bilmek. Dal korunabilir, ancak bu iki uygulama tek bir belirsiz bilme anlamında eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onu bütün yönleriyle eksiksiz bildi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"şeyin tamamını elde edip denetim altına aldı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"hakkında eksiksiz bilgi edinmediği şey"}],"lexicalization_note":"Anlam yalnız eksiksiz bilgi ve bir şeyin tamamını elde etme yapılarında tanıklıdır; bağımsız yalın kök anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel anlama dalı bilgi bakımından, bütünü alma dalı ise elde etme bakımından bu dalın iki uygulamasına en yakın sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sıradan bilmeden daha güçlüdür ve konunun hiçbir belirleyici yönünün dışarıda kalmamasını gerektirir; komşu dalda böyle bir tamamlık eşiği yoktur.","focus_only":"Odak dal, bilginin varlık, tür, ölçü ve nitelik dahil konunun bütün yönlerine ulaşmasını şart koşar.","gloss":"anlama ve bilme","neighbor_only":"Komşu dal, söz ya da anlamı kavrama ve bir şeyi bilme gibi eksiksizlik şartı taşımayan genel anlayışı kapsar.","neighbor_ref":"root_001171/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir konu hakkında bilgi edinme ve onu zihinsel olarak kavrama alanında buluşur."},{"boundary_match":"partial","distinction":"Bütünü elde etme bağlamında yaklaşırlar; odak dalın eksiksiz bilgi uygulaması ve komşu dalın alma-verme deyimi, kapsamlarını tam eşdeğer olmaktan çıkarır.","focus_only":"Odak dal, bütünüyle elde etmenin yanında bütün yönleriyle bilme uygulamasını da içerir.","gloss":"bir şeyi bütünüyle alma","neighbor_only":"Komşu dal, bir şeyi bütünüyle alma ya da verme eylemini özel bir deyim üzerinden anlatır.","neighbor_ref":"root_000601/B005","relation_type":"near_synonym","shared_zone":"İki dalın elde etme uygulamasında şeyin hiçbir parçası dışarıda bırakılmaz."}],"source_phrase_ar":"كل من أحرز شيئا كله وبلغ علمه أقصاه فقد أحاط به (ayn;tahdhib)؛ أحاط به علما (sihah)؛ الإحاطة بالشيء علما هي أن تعلم وجوده وجنسه وقدره وكيفيته (mufradat)","source_summary":"Kaynaklar, bir konunun tamamına ulaşma ölçütünü paylaşır; bunu hem bütün yönleriyle eksiksiz bilme hem de bir şeyin tamamını elde etme uygulamalarıyla açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"بلوغ العلم بالشيء من جميع جهاته أو إحرازه كله","what_is_not_ar":"ليس الإحداق الحسي ولا الحفظ العملي"},"support_links":["sup_3b9030bdd955aa8e05b0"]},{"boundary":"Bir iş çevresinde dönme ile direnen kişiyi dolaylı biçimde razı etmeye çalışma ayrı tutulmalıdır; her ikisi de fiziksel çevreleme dalından farklıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000372/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"çevresinde dönme veya dolaylı yoldan razı etmeye çalışma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eyleyen, belirli bir işin çevresinde dönüp durur ve ona doğrudan girmek yerine çevresinde hareket eder."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiler arası kullanımda eyleyen, karşı tarafın istemediği bir şeyi ondan elde etmek için dolaylı ve ısrarlı biçimde uğraşır."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın iş çevresinde dönme ve direnen kişiden bir sonuç elde etmeye çalışma kullanımlarını birbirine karıştırmadan birlikte temsil eder.","boundary_detail":"Bir iş çevresinde dönme ile direnen kişiyi dolaylı biçimde razı etmeye çalışma ayrı tutulmalıdır; her ikisi de fiziksel çevreleme dalından farklıdır.","branch_image_ar":"الدوران والمداورة","concept_gloss":"çevresinde dönme veya dolaylı yoldan razı etmeye çalışma","contextual_glosses":[{"applicability":"Eyleyenin belirli bir işe doğrudan girmeyip onun çevresinde dolaştığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bir işin çevresinde süren dönme ve dolanma hareketini korur."},"facet_ids":["F001"],"text":"o işin çevresinde dönüp duruyorum","usage_role":"contextual"},{"applicability":"Bir kişinin karşı çıktığı bir sonucu ondan dolaylı ve ısrarlı yollarla elde etmeye çalışma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eyleyenin isteğini, karşı tarafın direncini ve onu dolaylı biçimde razı etmeye çalışma sürecini korur."},"facet_ids":["F002"],"text":"istemediği şeye onu razı etmeye çalıştı","usage_role":"explanatory"}],"definition":"Bir işin çevresinde dönüp durmak ya da birinden istediği fakat onun karşı çıktığı bir sonucu dolaylı yollarla elde etmeye çalışmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eyleyen, belirli bir işin çevresinde dönüp durur ve ona doğrudan girmek yerine çevresinde hareket eder."},{"facet_id":"F002","role":"extension","statement":"Kişiler arası kullanımda eyleyen, karşı tarafın istemediği bir şeyi ondan elde etmek için dolaylı ve ısrarlı biçimde uğraşır."}],"identity_rationale":"Kaynak sözü, bir işin çevresinde dönüp durma ile istemediği bir konuda bir kişiyi dolaylı yollarla razı etmeye çalışma kullanımlarını birlikte tanıklar. İkinci kullanımda karşı tarafın direnci ve istenen sonuç kurucudur; yalın bir dönme anlamına indirgenemez.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"o işin çevresinde dönüp duruyorum"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"istemediği bir şeyi ondan elde etmek için dolaylı yollardan uğraştı"}],"lexicalization_note":"Bir kullanım belirli bir işin çevresinde dönme söz öbeğine, diğeri ise isteğe karşı çıkan kişiyi dolaylı yoldan razı etmeye çalışma biçimine bağlıdır.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; kaçamak davranma dolaylı kişiler arası tutumu, akbabaların dönmesi ise somut hareket görüntüsünü ayıran en yararlı iki karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hedefe ulaşmak için karşı tarafı razı etmeye yönelir; komşu dal ise yükümlülükten ya da karşılaşmadan kaçınan savunucu bir dolaylılık taşır.","focus_only":"Odak dalın kişiler arası kullanımında eyleyen, direnen kişiden belirli bir sonucu elde etmeye çalışır.","gloss":"kaçamak davranıp oyalama","neighbor_only":"Komşu dalda eyleyen, karşısındakinden bir şey elde etmek yerine kaçamak davranır, oyalar ya da savuşturur.","neighbor_ref":"root_000366/B002","relation_type":"near_neighbor","shared_zone":"İki dal da açık ve doğrudan ilerlemek yerine dolaylı, dönemeçli bir kişiler arası tutumu anlatır."},{"boundary_match":"partial","distinction":"Odak dal iş ve istek alanına taşınmış amaçlı bir dolanmayı, komşu dal ise kuşların somut dairesel uçuşunu anlatır; hareket görüntüsü ortak olsa da kullanım sınırları ayrıdır.","focus_only":"Odak dal, bir iş çevresinde oyalanma veya bir kişiyi razı etmeye çalışma gibi amaçlı insan eylemlerini bildirir.","gloss":"akbabaların çevrede dönmesi","neighbor_only":"Komşu dal, akbabaların ölülerin ya da öldürülmüş bir canlının çevresinde fiziksel olarak daire çizmesini anlatır.","neighbor_ref":"root_000928/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da bir hedefin çevresinde tekrarlanan dönme hareketi görüntüsü bulunur."}],"source_phrase_ar":"أنا أحوط حول ذلك الأمر أي أدور (sihah)؛ حاوطت فلانا محاوطة إذا داورته في أمر تريده منه وهو يأباه (tahdhib)","source_summary":"Toplu kanıt iki kapsamı ayırır: bir işin çevresinde dönme ve bir isteğe direnen kişiyi dolaylı yollarla razı etmeye çalışma. İkinci kapsam, istek ile karşı koyma arasındaki katılımcı ayrımını gerektirir.","sources":["SI","TA"],"what_is_ar":"الدوران حول أمر أو مداورة شخص في طلب يراد منه","what_is_not_ar":"ليس الإحاطة الحسية الخالصة ولا الحفظ"},"support_links":[]},{"boundary":"Dal, üstün bir güç altında çaresiz kalma ile bunun yaklaşan ya da gerçekleşen yıkım sonuçlarını kapsar; sırf fiziksel çevreleme değildir.","branch_kind":"collocation","branch_ref":"root_000372/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"karşı konulmaz bir güçle kuşatılıp yıkıma sürüklenme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Etkilenen taraf, kendisini her yönden bastıran ve karşı koyamadığı üstün bir gücün altında kalır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kişi bakımından bu durum, sonunun ya da yıkımının yaklaşmış olduğunu bildirir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ürün bakımından kuşatıcı zarar, onun yok olup bozulması sonucunda gerçekleşir."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi, topluluk veya şeyin üstün bir gücün altında kalmasını ve bu durumun yaklaşan ya da gerçekleşen yıkıma uzanmasını birlikte ifade eder.","boundary_detail":"Dal, üstün bir güç altında çaresiz kalma ile bunun yaklaşan ya da gerçekleşen yıkım sonuçlarını kapsar; sırf fiziksel çevreleme değildir.","branch_image_ar":"إحاطة الغلبة والهلاك","concept_gloss":"karşı konulmaz bir güçle kuşatılıp yıkıma sürüklenme","contextual_glosses":[{"applicability":"Bir topluluğun kendisini her yönden bastıran üstün bir güç karşısında çıkışsız kaldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstün gücün kuşatıcı etkisini ve etkilenenlerin karşı koyamama durumunu korur."},"facet_ids":["F001"],"text":"karşı koyamayacakları bir gücün altında kaldılar","usage_role":"explanatory"},{"applicability":"Bir kişinin yıkımının yakın olduğu sonuca odaklanan anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kişiyi bu sona götüren kuşatıcı üstün güç açıkça aktarılmaz.","preserves":"Kişinin yıkım ya da ölüm eşiğine yaklaşmış olması sonucunu korur."},"facet_ids":["F002"],"text":"sonu yaklaşmıştı","usage_role":"contextual"},{"applicability":"Ürünün uğradığı zararla bütünüyle yok olduğu ve işe yaramaz hale geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sonucu doğuran kuşatıcı ve karşı konulamaz güç görüntüsü açıkça aktarılmaz.","preserves":"Ürünün yok olması ve bozulması biçimindeki gerçekleşmiş sonucu korur."},"facet_ids":["F003"],"text":"ürünü yok olup bozuldu","usage_role":"contextual"}],"definition":"Bir kişi, topluluk ya da şeyin karşı koyamayacağı kuşatıcı bir gücün altında kalmasıdır; bu durum kişinin sonunun yaklaşmasına veya bir ürünün yok olup bozulmasına varabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Etkilenen taraf, kendisini her yönden bastıran ve karşı koyamadığı üstün bir gücün altında kalır."},{"facet_id":"F002","role":"specialization","statement":"Bir kişi bakımından bu durum, sonunun ya da yıkımının yaklaşmış olduğunu bildirir."},{"facet_id":"F003","role":"example","statement":"Bir ürün bakımından kuşatıcı zarar, onun yok olup bozulması sonucunda gerçekleşir."}],"identity_rationale":"Kaynak sözü bir kişi ya da topluluğun karşı koyamayacağı üstün bir gücün altında kalmasını, kişinin sonunun yaklaşmasını ve ürünün yok olup bozulmasını birlikte verir. Yıkım önemli bir sonuçtur, ancak üstün güçle kuşatılma ifadesinin her örneğinde tamamlanmış yıkım açıkça belirtilmez.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"sonunu getirecek bir gücün altında kaldı"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ürünü yok olup bozuldu"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"karşı koyamayacakları bir güçle kuşatıldılar"}],"lexicalization_note":"Anlam yalnız edilgen kuşatılma yapılarında kişi, topluluk veya ürüne bağlanır; yalın bir çevreleme ya da genel yıkım anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel felaket dalı sonuç yakınlığını, çökme dalı ise yıkım biçimini gösterir ve kuşatıcı üstün güç koşulunu belirginleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı özelliği kuşatıcı üstün güç ve çıkışsızlıktır; komşu dal felaketin gelişini bildirir, fakat çevreleyen güç ilişkisini zorunlu kılmaz.","focus_only":"Odak dal, yıkımı kişinin ya da şeyin her yönden bastıran üstün bir gücün altında kalmasıyla ilişkilendirir ve bazen yalnız sonun yaklaştığını bildirir.","gloss":"felaket veya yıkımın gelmesi","neighbor_only":"Komşu dal, ölüm, ağır hastalık, kırılma, öldürme ve malın yok olması gibi doğrudan felaket türlerini genişçe kapsar.","neighbor_ref":"root_000009/B011","relation_type":"near_synonym","shared_zone":"İki dal da kişi ya da malın ağır zarara, yok oluşa veya ölüm tehlikesine uğraması alanındadır."},{"boundary_match":"partial","distinction":"Odak dal yıkımı kuşatıcı güce yenik düşme süreciyle kurar; komşu dal ise yapının ya da durumun çökmesini, bunu doğuran çevreleme ilişkisi olmadan anlatır.","focus_only":"Odak dalda etkilenen tarafı bastıran dışsal ve kuşatıcı bir üstün güç bulunur.","gloss":"çökme, kırılma ve yıkılma","neighbor_only":"Komşu dal evin yıkılması, şeyin kırılması, yapının düşmesi ve saygınlığın gitmesi gibi iç yapının çöküşünü kapsar.","neighbor_ref":"root_000204/B004","relation_type":"near_neighbor","shared_zone":"Her iki dalın sonucunda bir kişi, nesne ya da düzen varlığını veya ayakta kalma gücünü yitirebilir."}],"source_phrase_ar":"أحيط بفلان إذا دنا هلاكه فهو محاط به (tahdhib)؛ أصابه ما أهلكه وأفسده (tahdhib)؛ أحيط بهم فذلك إحاطة بالقدرة (mufradat)","source_summary":"Toplu kanıt, karşı konulamaz gücün etkisi altında kalmayı ortak zemin yapar; kişi için yaklaşan sonu, ürün için yok olup bozulmayı ve topluluk için üstün güçle her yandan bastırılmayı ayrı gerçekleşmeler olarak sunar.","sources":["TA","MU"],"what_is_ar":"وقوع المرء أو الشيء تحت غلبة محيطة تنتهي إلى الهلاك أو الفساد أو العجز","what_is_not_ar":"ليس العلم المحيط ولا الحائط الحسي"},"support_links":[]},{"boundary":"Dal yalnız belirtilen gümüş süs ve onun ipli çeşidiyle ilgilidir; genel takı, duvar, koruma veya fiziksel çevreleme anlamı değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000372/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"yuvarlak veya hilal biçimli gümüş süs","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, gümüşten yapılmış yuvarlak ya da hilal biçimli bir süsü belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir betimlemede süs, kırmızı ve siyah iki renkli bükülü, boncuklu bir ipte bulunan gümüş hilaldir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Süs kadının alnına asılabilir ya da çocuğa takılabilir."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın nesne çekirdeğini verir; alna asılma, çocuğa takılma ve boncuklu iki renkli ipe bağlanma ayrıntıları bağlama göre eklenir.","boundary_detail":"Dal yalnız belirtilen gümüş süs ve onun ipli çeşidiyle ilgilidir; genel takı, duvar, koruma veya fiziksel çevreleme anlamı değildir.","branch_image_ar":"الحوط حلية مستديرة","concept_gloss":"yuvarlak veya hilal biçimli gümüş süs","contextual_glosses":[{"applicability":"Kadının gümüşten yapılmış yuvarlak süsü alnında taşıdığı betimlemede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gümüş süsün yuvarlaklığını, alında taşınmasını ve asılarak kullanılmasını korur."},"facet_ids":["F001","F003"],"text":"alnına yuvarlak bir gümüş süs astı","usage_role":"contextual"},{"applicability":"Gümüş hilal biçimli parçanın bir çocuğa süs olarak takıldığı anlatımda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süsün gümüş malzemesini, hilal biçimini ve çocuğa takılması eylemini korur."},"facet_ids":["F001","F003"],"text":"çocuğa gümüş hilal biçimli süs taktı","usage_role":"contextual"}],"definition":"Gümüşten yapılmış, alna asılan ya da çocuğa takılan yuvarlak veya hilal biçimli bir süstür; bir anlatımda kırmızı ve siyah bükülü, boncuklu bir ipteki gümüş hilali de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, gümüşten yapılmış yuvarlak ya da hilal biçimli bir süsü belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Bir betimlemede süs, kırmızı ve siyah iki renkli bükülü, boncuklu bir ipte bulunan gümüş hilaldir."},{"facet_id":"F003","role":"associated_use","statement":"Süs kadının alnına asılabilir ya da çocuğa takılabilir."}],"identity_rationale":"Kaynak sözü gümüşten yuvarlak ya da hilal biçimli bir süsü açıkça tanımlar; onu kadının alnına asılan parça, iki renkli boncuklu ipteki gümüş hilal ve çocuğa takılan süs olarak çeşitlendirir.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yuvarlak gümüş süs veya boncuklu iki renkli ipteki gümüş hilal"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"çocuğa gümüş hilal biçimli süs taktı"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"akrabalık bağını gözetme ya da çocuğa gümüş hilal biçimli süs takma buyruğu olarak aktarılan ikileme"}],"lexicalization_note":"Yalın ad süsü belirtir; alna asma, iki renkli boncuklu ipte bulunma ve çocuğa takma okumaları tanıklanan yapılara bağlı gerçekleşmelerdir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kolyeye eklenen takı parçası en yakın nesne karşılığını, bilezik ise yalnız aynı süs alanında kalan belirgin bir karşıtı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın gümüş ve yuvarlak ya da hilal biçimli nesnesi daha belirgindir; komşu dalın kolye içindeki takı türü bu biçim ve kullanım yerleriyle sınırlandırılmaz.","focus_only":"Odak dal gümüş, yuvarlaklık veya hilal biçimi, alna asılma ve bazen iki renkli boncuklu ip ayrıntılarını taşır.","gloss":"kolyede kullanılan takı parçası","neighbor_only":"Komşu dal, kolyelerde kullanılan ve malzemesi ya da biçimi burada belirtilmeyen genel bir takı türünü adlandırır.","neighbor_ref":"root_000291/B008","relation_type":"near_synonym","shared_zone":"İki dal da başka bir takı düzenine eklenebilen ve bedende taşınan süs parçalarını belirtir."},{"boundary_match":"field_only","distinction":"Süs alanı ortaktır; odak dal biçimi, gümüş malzemesi ve alın ya da çocuk üzerindeki kullanımıyla, komşu dal ise bilekteki halka biçimli takıyla ayrılır.","focus_only":"Odak dal, alında ya da çocuk üzerinde taşınan gümüş, yuvarlak veya hilal biçimli süstür.","gloss":"bilekte taşınan bilezik","neighbor_only":"Komşu dal, bilekte taşınan ve fildişi ya da benzeri sert maddelerden yapılabilen bilezik türüdür.","neighbor_ref":"root_001424/B006","relation_type":"same_field","shared_zone":"Her iki dal bedene takılan süs eşyalarını adlandırır."}],"source_phrase_ar":"الحوط شيء مستدير تعلقه المرأة على جبينها من فضة (maqayis)؛ الحوط خيط مفتول من لونين أحمر وأسود وهلال من فضة (tahdhib)؛ أن يحلي صبيه بالحوط وهو هلال من فضة (tahdhib)","source_summary":"Toplu kanıt gümüş, yuvarlaklık ya da hilal biçimi ve takılma işlevini ortaklaştırır; betimlemeler alna asılan tek parçalı süs ile iki renkli boncuklu ipteki gümüş hilal arasında çeşitlenir.","sources":["MQ","TA"],"what_is_ar":"حلية مستديرة أو خيط ذو خرز وهلال من فضة يسمى الحوط","what_is_not_ar":"ليس الحائط ولا الحفظ ولا الإحاطة العلمية"},"support_links":[]},{"boundary":"Anlam yalnız eksik para miktarını tamamlayan ek tutardır; genel ödeme, borç, para birimi veya eksilme anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_000372/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","surface_ar":"أَحَطْ"}],"gloss":"eksik para tutarını tamamlayan ek miktar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eklenen para miktarı, mevcut eksikliği kapatır ve toplamı gereken düzeye tamamlar."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tamamlama miktarı miras paylarının hesabında veya başka para hesaplarında kullanılabilir."}}],"root_ar":"ح و ط","root_id":"root_000372","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Miras payı ya da başka para hesabındaki açığı kapatan tutarı belirtir; açığın kendisi veya kullanılan para birimi için kullanılmaz.","boundary_detail":"Anlam yalnız eksik para miktarını tamamlayan ek tutardır; genel ödeme, borç, para birimi veya eksilme anlamlarını kapsamaz.","branch_image_ar":"حوط الدراهم الناقصة","concept_gloss":"eksik para tutarını tamamlayan ek miktar","contextual_glosses":[{"applicability":"Hesapta gereken toplamın altında kalan miktarı ek ödeme ile tamamlamaktan söz edilen bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eksikliği kapatma işlevini ve eklenen şeyin para miktarı olmasını korur."},"facet_ids":["F001","F002"],"text":"eksiği kapatan para","usage_role":"contextual"}],"definition":"Miras paylarında veya başka bir para hesabında eksik kalan miktarı tamamlayarak toplamı gereken düzeye çıkaran ek para tutarıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eklenen para miktarı, mevcut eksikliği kapatır ve toplamı gereken düzeye tamamlar."},{"facet_id":"F002","role":"example","statement":"Tamamlama miktarı miras paylarının hesabında veya başka para hesaplarında kullanılabilir."}],"identity_rationale":"Kaynak sözü, miras paylarında veya başka hesaplarda eksik kalan para miktarını tamamlayan ek tutarı açıkça adlandırır. Dal, eksikliğin kendisini ya da para birimini değil, eksikliği kapatan miktarı gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"eksik para tutarını tamamlayan ek miktar"}],"lexicalization_note":"Yalın ad, eksik kalan para miktarını tamamlayan ek tutarı belirtir; tanım herhangi bir özel söz öbeğinden genel para anlamı türetmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; eksilmenin kendisi ile payları denkleştirme işlemi, bu dalın yalnız açığı kapatan ek para miktarı olduğunu en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal açığın kendisidir; odak dal ise o açığı gideren ek miktardır. Biri sorun durumunu, diğeri tamamlama aracını gösterir.","focus_only":"Odak dal, belirlenmiş eksikliği kapatmak için sonradan eklenen para miktarını adlandırır.","gloss":"para veya paydaki eksilme","neighbor_only":"Komşu dal, para ağırlığında, mirasta veya başka bir değerde ortaya çıkan eksilmenin kendisini adlandırır.","neighbor_ref":"root_000641/B005","relation_type":"near_neighbor","shared_zone":"İki dal aynı hesapta gereken tutar ile eldeki tutar arasındaki parasal farkla ilgilidir."},{"boundary_match":"partial","distinction":"Odak dal parasal açığı tamamlayan miktarın adıdır; komşu dal ise ortaklar arasındaki payları eşitleyen işlem ve fazla kısmın geri verilmesi düzenidir.","focus_only":"Odak dal yalnız eksik para miktarını kapatan ek tutarı belirtir.","gloss":"payları eşitleyerek denkleştirme","neighbor_only":"Komşu dal, ortaklar arasındaki bölüşümde payları eşitlemek için fazlalığın geri verilmesini de içeren daha geniş bir denkleştirme işlemidir.","neighbor_ref":"root_000744/B008","relation_type":"near_neighbor","shared_zone":"İki dalda da hesaplanan paylar arasındaki dengesizlik ekleme ya da geri verme yoluyla giderilir."}],"source_phrase_ar":"الدراهم إذا نقصت في الفرائض أو غيرها هلم حوطها؛ الحوط ما يتم به دراهمه","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, miras paylarında veya başka hesaplarda eksik kalan para miktarını tamamlayan ek tutarı bildirir."}],"source_summary":"Kanıt bağımsız anlam çeşitleri sunmaz; kullanımı, para hesabındaki eksikliği gereken düzeye çıkaran dar bir tamamlama miktarıyla sınırlar.","sources":["TA"],"what_is_ar":"القدر الذي يتم به نقصان الدراهم في الفرائض أو غيرها","what_is_not_ar":"ليس الحفظ ولا الحائط ولا الحلية"},"support_links":[]},{"boundary":"Çekirdek, bilgi edinme ve iletmenin yanı sıra sınayarak iç yüzü tanımayı kapsar; arazi, tarım ve öteki eş sesli dallar buna girmez.","branch_kind":"bare","branch_ref":"root_000387/B001","candidate_links":[{"candidate_id":"cand_5b49b28e7610e428562b","lane":"micro"},{"candidate_id":"cand_d245abba4eba71397244","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"bilgi edinme, bildirme ve deneyerek iç yüzü tanıma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey veya olay hakkında edinilen ve aktarılabilen bilgiyi belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Edinilen bilgiyi bir başkasına bildirme ve onun bilgilenmesini sağlama eylemini kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Soru sorarak bilgi aramayı ve bir şeyi sınayıp deneyerek tanımayı kapsar."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir işin iç yüzünü bilen kişiyi ve dış görünüşün karşısındaki gerçek iç niteliği belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bilgi, aktarım, araştırma, sınama ve iç niteliği bilme yönlerinin birlikte kastedildiği genel açıklamalarda uygundur.","boundary_detail":"Çekirdek, bilgi edinme ve iletmenin yanı sıra sınayarak iç yüzü tanımayı kapsar; arazi, tarım ve öteki eş sesli dallar buna girmez.","branch_image_ar":"العلم بالخبر وباطن الأمر","concept_gloss":"bilgi edinme, bildirme ve deneyerek iç yüzü tanıma","contextual_glosses":[{"applicability":"Bir kişinin öğrendiği şeyi başkasına iletmesi bağlamında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgi arama, sınama, deneyim ve iç niteliği tanıma yönlerini kapsamaz.","preserves":"Bilginin başkasına aktarılması yönünü açık biçimde korur."},"facet_ids":["F002"],"text":"bilgi vermek","usage_role":"contextual"},{"applicability":"Deneyim veya sınama sonucunda bir konunun görünmeyen gerçekliğine hakim olmayı anlatan bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel bilgi aktarımını ve soru sorarak bilgi edinme eylemini dışarıda bırakır.","preserves":"Deneyimle kazanılan derin bilgi ve iç niteliği tanıma yönünü korur."},"facet_ids":["F003","F004"],"text":"işin iç yüzünü bilmek","usage_role":"contextual"}],"definition":"Bir şey hakkında bilgi edinme veya edinilen bilgiyi başkasına iletme; ayrıca sorarak öğrenme, sınama ve deneyim yoluyla bir işin iç yüzünü tanıma alanıdır. Bir kimsenin ya da şeyin dış görünüşünden ayrılan gerçek niteliği de bu bilgi alanının uzantısı olarak belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey veya olay hakkında edinilen ve aktarılabilen bilgiyi belirtir."},{"facet_id":"F002","role":"core","statement":"Edinilen bilgiyi bir başkasına bildirme ve onun bilgilenmesini sağlama eylemini kapsar."},{"facet_id":"F003","role":"specialization","statement":"Soru sorarak bilgi aramayı ve bir şeyi sınayıp deneyerek tanımayı kapsar."},{"facet_id":"F004","role":"extension","statement":"Bir işin iç yüzünü bilen kişiyi ve dış görünüşün karşısındaki gerçek iç niteliği belirtir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":null,"collision":"Güncel kullanımda çoğunlukla olay bildirimi veya medya içeriğiyle anlaşılır.","fit":"drifted_loanword","loses":"Sınama, deneyim, uzman bilgi ve dış görünüşten ayrılan iç nitelik yönlerini siler.","preserves":"Bir olay hakkında alınan veya iletilen bilgi yönünü korur."},"text":"haber"}],"identity_rationale":"Dalın bilgi ve iç yüz eksenli çerçevesi kaynak ifadesini genel olarak karşılar; ancak anlam yalnızca edinilmiş bilgi değildir. Bilgiyi başkasına iletme, soru sorarak bilgi edinme, sınama ve deneyim yoluyla bir işin iç yüzünü tanıma ile dış görünüşten ayrılan gerçek nitelik de dalın sınırları içinde tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir olay veya durum hakkında edinilen ve aktarılan bilgi"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bilgi vermek; bildirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"bir konuyu sorup bilgi edinmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"sınayıp deneyerek bilgi sahibi olmuş kişi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bilgili; bir işin iç yüzüne hakim"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"dış görünüşün karşısındaki iç yüz ve gerçek nitelik"}],"lexicalization_note":"Dal yalın biçimlere dayanır; tanım herhangi bir kalıba bağlanmadan bilgi edinme, bildirme, sınama ve iç niteliği bilme alanını kapsar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bilme, araştırarak bilgi edinme ve gizli olana ulaşma sınırlarını en iyi açıklayan üç karşıtlık yayımlandı, yalnızca aynı senaryoda bulunan veya öteki eş sesli dallara ait adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, genel bilme ve bildirmeye ek olarak soruşturma, deneyip sınama ve iç yüzü tanıma sınırlarını taşır; bu nedenle tam ikame kurulamaz.","focus_only":"Soruşturma, sınama, deneyimle iç yüzü tanıma ve dış görünüşten ayrılan iç niteliği adlandırma kapsamı vardır.","gloss":"bilmek ve bildirmek","neighbor_only":"Komşu kartı bilgiyi edinme ve başkasına iletme çekirdeğini daha genel bir bilme alanı olarak verir.","neighbor_ref":"root_000473/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme ve edinilen bilgiyi başkasına aktarma alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği bilgi arama sürecidir; odak dal ise aranan bilginin kendisini, aktarımını ve deneyimle oluşan derin bilgiyi de adlandırır.","focus_only":"Edinilmiş bilgiyi, onu bildirmeyi, deneyime dayalı uzmanlığı ve iç niteliği de kapsar.","gloss":"sorup araştırarak bilgi arama","neighbor_only":"Bilgiye ulaşmak için araştırma, yoklama, gizliyi açığa çıkarma ve soruşturma sürecini öne çıkarır.","neighbor_ref":"root_000085/B002","relation_type":"near_neighbor","shared_zone":"İki dal, soru sorarak veya araştırarak bilinmeyen bir konu hakkında bilgi edinmede buluşur."},{"boundary_match":"partial","distinction":"Odak dalda iç yüz bilgisi geniş bilgi ve deneyim alanının bir uzantısıdır; komşu dalda belirleyici özellik gizli olana ulaşmaktır.","focus_only":"Genel bilgi, bildirme, sınama ve deneyimle öğrenme kapsamı bulunur.","gloss":"gizli olana vakıf olma","neighbor_only":"Özellikle gizli bir şeyi keşfetme ve onu başkasına gösterme yönü bulunur.","neighbor_ref":"root_000982/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da görünmeyen veya içte kalan bir gerçeğin bilinmesiyle ilişkilidir."}],"source_phrase_ar":"الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)","source_summary":"Kaynakların birleşen tanıklığı, bilgi edinme ve bildirme çekirdeğini soruşturma, sınama, deneyime dayalı bilme ve iç niteliği tanıma yönleriyle genişletir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الخبر والنبأ والإخبار والاستخبار والخبرة بمعنى الاختبار والمعرفة ببواطن الأمر والخبير العالم والمخبر الباطن لا المنظر","what_is_not_ar":"الأرض اللينة والمخابرة والمزادة والناقة الغزيرة والزبد والوبر والخبرة في الشاة"},"support_links":["sup_3b9030bdd955aa8e05b0","sup_aeda0139e0e66cf77048"]},{"boundary":"Dal, gevşek veya alçak araziyi, bitkili-sulu yeri ve akışla oluşan su birikintisini ayrı fakat bağlantılı yer biçimleri olarak tutar.","branch_kind":"bare","branch_ref":"root_000387/B002","candidate_links":[{"candidate_id":"cand_969feb829d06e7af46c2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"gevşek, alçak ve su tutan arazi veya su birikintisi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gevşek, yumuşak ya da alçak ve yağmur suyunun toplanabildiği araziyi belirtir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sıcak, ağaçlı ve suyu bol bir yer niteliğini belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Akışın oluşturduğu ve insanların içine girip geçebildiği bir su birikintisini belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Arazi niteliğiyle akışta oluşan su birikintisinin birlikte temsil edilmesi gereken dal düzeyi açıklamalarda uygundur.","boundary_detail":"Dal, gevşek veya alçak araziyi, bitkili-sulu yeri ve akışla oluşan su birikintisini ayrı fakat bağlantılı yer biçimleri olarak tutar.","branch_image_ar":"لين الأرض ومائها","concept_gloss":"gevşek, alçak ve su tutan arazi veya su birikintisi","contextual_glosses":[{"applicability":"Toprağın yumuşaklığı, gevşekliği veya alçaklığı nedeniyle su topladığı arazi bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sıcak ve ağaçlı yer ile bağımsız su birikintisi gerçekleşmelerini kapsamaz.","preserves":"Arazinin gevşek, alçak ve su toplayan niteliğini korur."},"facet_ids":["F001"],"text":"gevşek ve su tutan arazi","usage_role":"contextual"},{"applicability":"Suyun bir akış yatağında toplanıp insanların içinden geçebildiği birikinti bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gevşek arazi ile sıcak, ağaçlı ve suyu bol yer niteliklerini dışarıda bırakır.","preserves":"Akışın oluşturduğu geçilebilir su birikintisi yönünü korur."},"facet_ids":["F003"],"text":"akış yatağındaki su birikintisi","usage_role":"contextual"}],"definition":"Gevşek, yumuşak veya alçak olup su toplayabilen araziyi ve sıcak, ağaçlı, suyu bol bir yeri belirtir. Ayrıca akış yatağında oluşup insanların içinden geçebildiği su birikintisini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gevşek, yumuşak ya da alçak ve yağmur suyunun toplanabildiği araziyi belirtir."},{"facet_id":"F002","role":"specialization","statement":"Sıcak, ağaçlı ve suyu bol bir yer niteliğini belirtir."},{"facet_id":"F003","role":"extension","statement":"Akışın oluşturduğu ve insanların içine girip geçebildiği bir su birikintisini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kalıcı çamurluluk ve batma tehlikesi gibi kaynakta bulunmayan özellikler ekler.","collision":"Gevşek araziyi ve geçilebilir su birikintisini tek bir sulak alan türüyle karıştırır.","fit":"broadening","loses":null,"preserves":"Alçak ve su toplayan arazi çağrışımını kısmen korur."},"text":"bataklık"}],"identity_rationale":"Kaynak ifadesi yalnızca yumuşak araziyi ve onun suyunu anlatmaz. Gevşek ya da alçak arazi, sıcak ve ağaçlı-sulu yer ile akışın oluşturduğu su birikintisi ayrı gerçekleşmelerdir; dal korunabilir, fakat su birikintisi arazi niteliğinin içine eritilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"gevşek, yumuşak veya alçak olup su toplayan arazi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sıcak, ağaçlı ve suyu bol yer"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"akış yatağında oluşan geçilebilir su birikintisi"}],"lexicalization_note":"Dal yalın kullanımlara dayanır; tanım belirli bir söz öbeğine bağlanmadan arazi, yer ve su birikintisi gerçekleşmelerini ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; su toplanan çöküntü, alçak-bitkili arazi ve düz-verimli arazi en açıklayıcı sınırları verdi, yağışsızlık veya sulama eylemi gibi karşıt senaryolar ile öteki eş sesli dallar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda su birikintisi daha geniş bir gevşek ve su tutan arazi alanının uzantısıdır; komşu dalın çekirdeği ise belirli çukurlaşmalardaki su toplanmasıdır.","focus_only":"Gevşek veya yumuşak arazi ile sıcak, ağaçlı ve suyu bol yer kapsamı bulunur.","gloss":"çöküntüde toplanan su","neighbor_only":"Suyun özellikle kale çevresi, çöküntü veya büyük çukur gibi yerlerde toplanmasını belirtir.","neighbor_ref":"root_000282/B002","relation_type":"near_neighbor","shared_zone":"İki dal da alçak bir yerde biriken suyu veya böyle bir su birikme alanını kapsar."},{"boundary_match":"partial","distinction":"Odak dalın sınırı gevşeklik ve su tutma çevresinde kurulur; komşu dalda alçaklığın yanında bitki yetiştirme özelliği öne çıkar.","focus_only":"Toprağın gevşekliği, su toplaması ve ayrı bir su birikintisini adlandırma kapsamı vardır.","gloss":"alçak ve bitki bitiren arazi","neighbor_only":"Alçak arazinin bitki yetiştirmesi belirleyici özelliktir.","neighbor_ref":"root_000965/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal da alçalmış ve bitkiyle ilişkili bir arazi biçimini anlatabilir."},{"boundary_match":"field_only","distinction":"Odak dal su ve gevşeklik özellikleriyle, komşu dal ise düzlük ve verimlilik özellikleriyle tanımlanır; olağan bağlamda birbirinin yerine geçmez.","focus_only":"Gevşeklik, alçaklık, su toplama ve akışta oluşan birikinti anlamlarını taşır.","gloss":"düz ve verimli arazi","neighbor_only":"Düzgün ve verimli olup bitkiyi iyi yetiştiren araziyi belirtir.","neighbor_ref":"root_001521/B006","relation_type":"same_field","shared_zone":"İki dal da toprağın yapısını ve bitki yetişmesine elverişli araziyi betimler."}],"source_phrase_ar":"الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)","source_summary":"Birleşik tanıklık, yumuşak veya gevşek arazi çekirdeğine alçak ve su tutan yer, sıcak-ağaçlı-sulu mekan ve akışta oluşan su birikintisi gerçekleşmelerini ekler.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"يدخل فيه الخبراء والخبار والأرض الرخوة أو اللينة أو المنخفضة وما يجتمع فيها من ماء وشجر ومكان خَبِر","what_is_not_ar":"العلم والنبأ والمخابرة والمزادة والناقة الغزيرة والزبد والوبر والخبرة في الشاة"},"support_links":["sup_9efe344c8d839dcee658"]},{"boundary":"Dal, çiftçi rolünü ve üründen belirli pay karşılığı yapılan ortakçılığı kapsar; genel ekim, toprak işleme veya ücretli çalışma bununla özdeş değildir.","branch_kind":"bare","branch_ref":"root_000387/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"üründen pay karşılığı ortakçılık ve bunu yapan çiftçi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Toprağı işleyen ve tarımsal üretimi yürüten çiftçiyi belirtir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toprağın, elde edilen ürünün yarısı, üçte biri veya belirli bir payı karşılığında işlenmesi düzenini belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem tarımsal ortakçılık düzeninin hem de toprağı işleyen katılımcının dal düzeyinde birlikte gösterilmesi gerektiğinde uygundur.","boundary_detail":"Dal, çiftçi rolünü ve üründen belirli pay karşılığı yapılan ortakçılığı kapsar; genel ekim, toprak işleme veya ücretli çalışma bununla özdeş değildir.","branch_image_ar":"إصلاح الأرض بالمخابرة","concept_gloss":"üründen pay karşılığı ortakçılık ve bunu yapan çiftçi","contextual_glosses":[{"applicability":"Toprağın, elde edilecek ürünün önceden belirlenen bölümü karşılığında işletilmesi bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Toprağı işleyen kişinin ayrıca adlandırılması yönünü kapsamaz.","preserves":"Tarımsal üretimi ve ürün payına dayalı karşılık koşulunu korur."},"facet_ids":["F002"],"text":"üründen pay karşılığı ortakçılık","usage_role":"contextual"},{"applicability":"Söz konusu üretim düzeninde araziyi ekip biçen kişinin adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Üründen belirli bir pay karşılığında kurulan ortakçılık düzenini belirtmez.","preserves":"Toprağı işleyen tarımsal üretici rolünü korur."},"facet_ids":["F001"],"text":"toprağı işleyen çiftçi","usage_role":"contextual"}],"definition":"Toprağı işleyip tarımsal üretimi yapan çiftçiyi ve emeğin ya da kullanımın karşılığının topraktan çıkan ürünün yarısı, üçte biri veya önceden belirlenmiş başka bir payı olduğu ortakçılık düzenini belirtir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Toprağı işleyen ve tarımsal üretimi yürüten çiftçiyi belirtir."},{"facet_id":"F002","role":"core","statement":"Toprağın, elde edilen ürünün yarısı, üçte biri veya belirli bir payı karşılığında işlenmesi düzenini belirtir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Karşılığın sabit kira bedeli olduğu farklı bir sözleşme türünü düşündürür.","collision":"Ürün ortakçılığını sıradan arazi kirasıyla karıştırır.","fit":"displacement","loses":"Karşılığın elde edilen üründen belirli bir pay olması koşulunu siler.","preserves":"Arazinin başka bir kişi tarafından işletilmesi ilişkisini kısmen korur."},"text":"tarla kiralama"}],"identity_rationale":"Kaynak ifadesinin çekirdeği genel olarak toprağı iyileştirmek değil, toprağı işleyen çiftçi ile ürünün yarısı, üçte biri veya başka belirli bir payı karşılığında yapılan tarımsal ortakçılıktır. Dal korunabilir, ancak tanım işleme eyleminden çok paya dayalı üretim düzenine bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"toprağı işleyen çiftçi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık"}],"lexicalization_note":"Dal yalın biçimlere dayanır; çiftçi adını ve belirli ürün payına bağlı tarımsal ortakçılığı özel bir kalıba genellemeden birlikte açıklar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel tarımsal ortakçılık, çiftçi adı ve toprağı işleme eylemiyle kurulan üç sınır yayımlandı, ücret, ürün artışı ve genel edinme gibi daha uzak ilişkiler elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, genel ortakçılık alanını ürün payının belirlenmesi ve toprağı işleyen kişiyle sınırlar; komşu kart bu ayrıntıları zorunlu kılmaz.","focus_only":"Toprağı işleyen kişiyi adlandırır ve karşılığın üründen yarım, üçte bir veya belirlenmiş bir pay olmasını açıkça içerir.","gloss":"tarımsal ortakçılık","neighbor_only":"Tarımsal ortakçılığı bilinen genel adıyla verir, fakat kartta belirli pay koşulu veya çiftçi rolü açıklanmaz.","neighbor_ref":"root_000630/B003","relation_type":"near_synonym","shared_zone":"İki dal da tarımsal üretimin paylaşım ilişkisi içinde yürütülmesini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalın ayırıcı yönü ürün paylaşımına dayalı üretim ilişkisidir; komşu dal yalnızca çiftçi grubunu veya üyesini adlandırır.","focus_only":"Ürün payına dayalı ortakçılık düzenini ve bu düzende toprağı işleyen tekil rolü kapsar.","gloss":"çiftçiler","neighbor_only":"Bir çiftçi topluluğunu ve topluluğun bir üyesini adlandıran ayrı bir kişi adıdır.","neighbor_ref":"root_001003/B012","relation_type":"same_field","shared_zone":"Her iki dal tarımsal üretimi yapan çiftçileri adlandırma alanında buluşur."},{"boundary_match":"field_only","distinction":"Komşu dal fiziksel toprak işleme eylemine, odak dal ise bu işi yapan kişi ile ürün paylaşımına dayalı toplumsal düzene odaklanır.","focus_only":"Çiftçi rolünü ve üründen pay karşılığı kurulan üretim düzenini belirtir.","gloss":"toprağı sürüp ekime hazırlama","neighbor_only":"Toprağı sürme, kabartma ve ekime hazırlama eylemini belirtir.","neighbor_ref":"root_000384/B007","relation_type":"same_field","shared_zone":"İki dal toprağın tarımsal üretim amacıyla işlenmesi alanında yer alır."}],"source_phrase_ar":"الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)","source_summary":"Birleşik tanıklık, toprağı işleyen kişi adını ürünün yarısı, üçte biri veya belirlenmiş başka bir payı karşılığında yapılan tarımsal ortakçılıkla ilişkilendirir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الخبير بمعنى الأكار والمخابرة والمؤاكرة والمزارعة بجزء معلوم مما يخرج من الأرض","what_is_not_ar":"الخبر بمعنى العلم والأرض نفسها والمزادة والناقة والزبد والوبر والخبرة في الشاة"},"support_links":[]},{"boundary":"Çekirdek büyük su tulumudur; bol verimli dişi deve, kabın genişlik ve doluluk özelliğine dayanan benzetmeli uzantıdır.","branch_kind":"bare","branch_ref":"root_000387/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"büyük su tulumu ve bolluğuyla ona benzetilen dişi deve","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Büyük ve geniş bir su tulumunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bol sütü veya verimi nedeniyle büyük su tulumuna benzetilen dişi deveyi belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Temel kap anlamı ile benzetmeye dayalı dişi deve uzantısının birlikte gösterildiği dal düzeyi açıklamada uygundur.","boundary_detail":"Çekirdek büyük su tulumudur; bol verimli dişi deve, kabın genişlik ve doluluk özelliğine dayanan benzetmeli uzantıdır.","branch_image_ar":"الغزر في المزادة والناقة","concept_gloss":"büyük su tulumu ve bolluğuyla ona benzetilen dişi deve","contextual_glosses":[{"applicability":"Suyun taşındığı veya saklandığı büyük ve geniş deri kabın doğrudan adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bolluk benzetmesiyle adlandırılan dişi deve uzantısını kapsamaz.","preserves":"Dalın temel büyük kap anlamını eksiksiz korur."},"facet_ids":["F001"],"text":"büyük su tulumu","usage_role":"contextual"},{"applicability":"Dişi devenin verimi ve içindeki bolluk bakımından büyük kaba benzetildiği hayvancılık bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Benzetmenin temelindeki büyük su tulumunu doğrudan adlandırmaz.","preserves":"Benzetmeye dayanan bol verimli dişi deve anlamını korur."},"facet_ids":["F002"],"text":"bol sütlü dişi deve","usage_role":"contextual"}],"definition":"Büyük ve geniş bir su tulumunu belirtir. Çok verimli ve bol sütlü dişi deve, içindeki bolluk ve genişlik bakımından bu kaba benzetilerek aynı adla anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Büyük ve geniş bir su tulumunu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bol sütü veya verimi nedeniyle büyük su tulumuna benzetilen dişi deveyi belirtir."}],"identity_rationale":"Kaynak ifadesi büyük ve geniş bir su tulumunu temel referent olarak verir; bol verimli dişi deve de içindeki bolluk bakımından bu kaba benzetilerek aynı adla anılır. Sağlanan çerçeve hem temel nesneyi hem benzetmeye dayalı uzantıyı doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"büyük ve geniş su tulumu"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve"}],"lexicalization_note":"Dal yalın adlandırmalara dayanır; tanım büyük su tulumunu temel alır ve dişi deve anlamını benzetmeye bağlı bir uzantı olarak sınırlar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; büyük su kabı, bol sütlü dişi deve ve genel dolulukla kurulan üç yakın sınır yayımlandı, yalnızca bitki yoğunluğu veya süt çıkışı gibi daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kabı geniş bir su tulumudur ve deve uzantısı benzetmelidir; komşu dal büyük kova ile su taşıyıcısı çevresinde kurulur.","focus_only":"Büyük deri su tulumunu ve ona benzetilen bol verimli dişi deveyi kapsar.","gloss":"büyük su kovası ve su taşıyıcısı","neighbor_only":"Büyük kova ile su taşıyan hayvan veya taşıma düzeneği anlamlarını kapsar.","neighbor_ref":"root_001077/B002","relation_type":"near_neighbor","shared_zone":"İki dal da su taşımaya yarayan büyük bir kabı adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda bolluk büyük su tulumu benzetmesiyle ifade edilir; komşu dalda belirleyici özellik sütün uzun süre birikmiş olmasıdır.","focus_only":"Dişi deveyi büyük su tulumuna benzetir ve temel olarak bu kabı da adlandırır.","gloss":"uzun süre süt biriktiren dişi deve","neighbor_only":"Sütün uzun süre birikmesiyle memesi dolu kalan dişi deveyi belirtir.","neighbor_ref":"root_000752/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da süt bolluğu veya uzun süreli dolulukla nitelenen dişi deveyi anlatır."},{"boundary_match":"partial","distinction":"Odak dal belirli bir kap türü ile benzetmeli hayvan adıdır; komşu dal ise çeşitli nesnelere uygulanabilen genel doluluk niteliğidir.","focus_only":"Belirli bir büyük su kabını ve bu kaba benzetilen dişi deveyi adlandırır.","gloss":"bütünüyle dolu olma","neighbor_only":"Kabın türünden bağımsız olarak bir yerin veya nesnenin bütünüyle dolu olmasını belirtir.","neighbor_ref":"root_000945/B007","relation_type":"near_neighbor","shared_zone":"İki dal geniş bir kabın doluluğu ve çok miktarda içerik taşıması düşüncesinde kesişir."}],"source_phrase_ar":"الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)","source_summary":"Kaynakların birleşen tanıklığı büyük su tulumunu temel anlam olarak verir ve bol verimli dişi deve adını bu kabın genişliği ile doluluğuna dayanan bir benzetme olarak açıklar.","sources":["MQ","JA","SI","MU"],"what_is_ar":"يدخل فيه الخَبْر للمزادة العظيمة وتشبيه الناقة الغزيرة بها في السعة والغزر","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والزبد والوبر والخبرة في الشاة"},"support_links":[]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_000387/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kesilip yenebilen yumuşak bitkiyi belirtir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yünü veya ince ve yumuşak hayvan kılını belirtir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Devenin ağzında oluşan ya da ağzından attığı köpüğü belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıttaki sınırlı adlandırma kümesinin üç referentini birlikte göstermek gerektiğinde uygundur; tek üretken çekirdek iddiası taşımaz.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"اللِّين في النبات والوبر والزبد","concept_gloss":"yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü","contextual_glosses":[{"applicability":"Sözcüğün yumuşak ve yenebilir bitkiyi adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yün veya ince kıl ile deve ağzı köpüğü referentlerini kapsamaz.","preserves":"Yumuşak bitki referentini ve yenebilme bağlamını korur."},"facet_ids":["F001"],"text":"kesilip yenebilen yumuşak bitki","usage_role":"contextual"},{"applicability":"Sözcüğün hayvan üzerindeki yün ya da ince kılı adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumuşak bitki ile deve ağzı köpüğü referentlerini kapsamaz.","preserves":"Yün veya ince hayvan kılı referentini korur."},"facet_ids":["F002"],"text":"yün veya ince hayvan kılı","usage_role":"contextual"},{"applicability":"Sözcüğün devenin ağzında oluşan veya ağzından atılan köpüğü adlandırdığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yumuşak bitki ile yün veya ince hayvan kılı referentlerini kapsamaz.","preserves":"Deve ağzındaki köpük referentini açık biçimde korur."},"facet_ids":["F003"],"text":"devenin ağzından çıkan köpük","usage_role":"contextual"}],"definition":"Kaynak tanıklığında aynı yalın biçim, yumuşak bitkiyi, yün veya ince hayvan kılını ve devenin ağzından çıkan köpüğü ayrı ayrı adlandırır. Bu referentler için kaynakça desteklenen tek bir ortak kavramsal çekirdek kurulamaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kesilip yenebilen yumuşak bitkiyi belirtir."},{"facet_id":"F002","role":"source_variant","statement":"Yünü veya ince ve yumuşak hayvan kılını belirtir."},{"facet_id":"F003","role":"source_variant","statement":"Devenin ağzında oluşan ya da ağzından attığı köpüğü belirtir."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kesilip yenebilen yumuşak bitki"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yün veya ince hayvan kılı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"devenin ağzında oluşan veya ağzından çıkan köpük"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الخبير للنبات اللين والوبر وزبد أفواه الإبل أو ما يلقيه البعير من فيه","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والمزادة والناقة والخبرة في الشاة"},"support_links":[]},{"boundary":"Dal, ortak alım-kesim-bölüşüm sürecine konu olan koyunu ve bu tür bölüşümden alınan et veya balık payını kapsar.","branch_kind":"bare","branch_ref":"root_000387/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","surface_ar":"خُبْرًا"}],"gloss":"ortak alınıp kesilen koyun veya bölüşülen et-balık payı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluğun ortaklaşa satın alıp kestiği ve etini kendi arasında bölüştüğü koyunu belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir bölüşüm sonucunda kişiye düşen et veya balık payını belirtir."}}],"root_ar":"خ ب ر","root_id":"root_000387","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortak alım, kesim ve bölüşüme konu olan koyunla bundan doğan yiyecek payının birlikte gösterildiği dal düzeyi açıklamada uygundur.","boundary_detail":"Dal, ortak alım-kesim-bölüşüm sürecine konu olan koyunu ve bu tür bölüşümden alınan et veya balık payını kapsar.","branch_image_ar":"القسمة في الشاة واللحم","concept_gloss":"ortak alınıp kesilen koyun veya bölüşülen et-balık payı","contextual_glosses":[{"applicability":"Bir topluluğun koyunu birlikte satın alıp kesmesi ve etini kendi arasında paylaşması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Etten veya balıktan alınan genel pay uzantısını kapsamaz.","preserves":"Ortak alım, kesim ve etin katılımcılar arasında bölüşülmesi sürecini korur."},"facet_ids":["F001"],"text":"ortak alınıp eti bölüşülen koyun","usage_role":"contextual"},{"applicability":"Bir bölüşüm sonunda kişiye düşen et ya da balık bölümünün adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koyunun ortaklaşa satın alınması, kesilmesi ve bütün etinin paylaşılması olayını kapsamaz.","preserves":"Bölüşüm sonucunda alınan yiyecek payını korur."},"facet_ids":["F002"],"text":"et veya balıktan alınan pay","usage_role":"contextual"}],"definition":"Bir topluluğun ortaklaşa satın aldığı, kestiği ve etini aralarında paylaştığı koyunu belirtir. Bununla bağlantılı olarak, bölüşümde bir kişinin etten veya balıktan aldığı payı da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluğun ortaklaşa satın alıp kestiği ve etini kendi arasında bölüştüğü koyunu belirtir."},{"facet_id":"F002","role":"extension","statement":"Bir bölüşüm sonucunda kişiye düşen et veya balık payını belirtir."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Mülkiyet, şirket ortaklığı veya soyut hak payı gibi çok daha geniş kullanım alanları ekler.","collision":"Ortak kesim olayını ve payın et ya da balık olması koşulunu belirsizleştirir.","fit":"broadening","loses":null,"preserves":"Bir bölüşümde kişiye düşen pay yönünü korur."},"text":"hisse"}],"identity_rationale":"Kaynak ifadesi, bir topluluğun ortaklaşa satın alıp kestiği ve etini bölüştüğü koyunu temel olaylı referent olarak verir; etten veya balıktan alınan pay bunun bölüşüm sonucunu genelleştiren bağlantılı anlamıdır. Sağlanan çerçeve süreç, nesne ve sonuç ayrımını korumaya elverişlidir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ortaklaşa alınıp kesilen ve eti bölüşülen koyun"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"et veya balıktan alınan pay"}],"lexicalization_note":"Dal yalın biçimlere dayanır; tanım ortaklaşa alınan koyun ile bölüşümden doğan et veya balık payını aşamalı olarak ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel belirlenmiş pay, kesimde ilk ayrılan et payı ve oranlı bölümle kurulan üç sınır yayımlandı, yalnızca et türü veya miras bölüşümüyle ilgili daha uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yiyecek payını ortak koyun kesimiyle bağlantılı olarak sınırlar; komşu dal nesne türünden ve kesim sürecinden bağımsız genel pay kavramıdır.","focus_only":"Ortak alınan koyun, kesim ve payın özellikle etten veya balıktan alınması koşulları bulunur.","gloss":"kişiye ayrılan belirli pay","neighbor_only":"Herhangi bir şeyden bir kişiye ayrılmış belirli hakkı veya bölümü genel olarak belirtir.","neighbor_ref":"root_001507/B005","relation_type":"near_synonym","shared_zone":"İki dal da bölüşülen bir şeyden belirli bir kişiye düşen bölümü adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda payın ilk olması veya büyük bir parça olması gerekmez ve balığı da kapsar; komşu dal ilk ayrılma ve deve eti özellikleriyle sınırlıdır.","focus_only":"Ortak satın alınan koyunun tamamını ve et ya da balık payını kapsar.","gloss":"bölüşümde ilk ayrılan et payı","neighbor_only":"Bölüşümde ilk ayrılan payı ve özellikle büyük bir deve eti parçasını belirtir.","neighbor_ref":"root_000090/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da kesilmiş hayvan etinin bölüşümünde bir kişiye ayrılan payı anlatır."},{"boundary_match":"field_only","distinction":"Odak dal yiyecek türü ve ortak kesim süreciyle, komşu dal ise payın kesin oranıyla tanımlanır; biri diğerinin yerine geçmez.","focus_only":"Ortak koyun kesimi ile et veya balık olarak alınan payı belirtir.","gloss":"üçte birlik bölüm","neighbor_only":"Herhangi bir şeyin tam üçte birini veya üçte ikisini oran olarak belirtir.","neighbor_ref":"root_000203/B002","relation_type":"same_field","shared_zone":"İki dal da bir bütünün bölünmesi ve bir bölümün ayrılması alanında yer alır."}],"source_phrase_ar":"الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)","source_summary":"Birleşik tanıklık ortaklaşa koyun satın alma, kesme ve eti bölüşme sürecini verir; etten veya balıktan alınan pay da bu bölüşüm çekirdeğinin sonuçsal uzantısıdır.","sources":["MQ","JA","SI"],"what_is_ar":"يدخل فيه الخُبْرة للشاة المشتركة التي يذبحها القوم ويقتسمون لحمها أو للنصيب من اللحم والسمك","what_is_not_ar":"العلم والنبأ والأرض والمخابرة والمزادة والناقة والزبد والوبر"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["18:91:1"],"branch_refs":[],"candidate_id":"cand_45e77bf64d1ad48578bf","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:1:kaf-retrospective-comparison","source_type":"word_analysis","support_ids":["sup_2bb58c6e794009ceea68","sup_ec504f08009472d95272"],"title":"retrospective comparison hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:1","qac_refs":["18:91:1:1"],"status":"accepted"}},{"anchor_refs":["18:91:2"],"branch_refs":[],"candidate_id":"cand_8870d2cdc979cefc9275","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:2:demonstrative-discourse-seal","source_type":"word_analysis","support_ids":["sup_367788b2f972aa95831f","sup_870cb74d6a3864b74614"],"title":"definite distal scene seal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:2","qac_refs":["18:91:1:2"],"status":"accepted"}},{"anchor_refs":["18:91:2"],"branch_refs":[],"candidate_id":"cand_99f3375338a39285e65e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:2:kadhālika-boundary-marker","source_type":"word_analysis","support_ids":["sup_367788b2f972aa95831f","sup_48060590e16281b81058"],"title":"boundary-marker recurrence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:2","qac_refs":["18:91:1:2"],"status":"accepted"}},{"anchor_refs":["18:91:3"],"branch_refs":[],"candidate_id":"cand_40744c91eb808ead9145","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:3:wa-qad-backgrounded-aside","source_type":"word_analysis","support_ids":["sup_428425eb6bce9f27df73","sup_a7f7719d61d7e545b5f2"],"title":"backgrounded divine aside","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:3","qac_refs":["18:91:2:1"],"status":"accepted"}},{"anchor_refs":["18:91:4"],"branch_refs":[],"candidate_id":"cand_2b59198c8be6cf31becd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:4:qad-verified-anterior-completion","source_type":"word_analysis","support_ids":["sup_634b4a7665e4afed4db4","sup_a8b5a1b52c9b8d1e760b"],"title":"verified prior completion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:4","qac_refs":["18:91:2:2"],"status":"accepted"}},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_5e89b2623cee14d7d06a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:completed-divine-active-agency","source_type":"word_analysis","support_ids":["sup_681c5fae08c4c61613a7","sup_c970a0c39b8f513e80e3"],"title":"completed divine active agency","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_7db65e6603ae52868864","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:discourse-pivot-from-journey-to-aside","source_type":"word_analysis","support_ids":["sup_507e2a251892f3bbbd82","sup_681c5fae08c4c61613a7"],"title":"pivot from journey to aside","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_6664bcac43a0529aaaab","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:divine-knowledge-formula-localized","source_type":"word_analysis","support_ids":["sup_681c5fae08c4c61613a7","sup_773dbb8cc981a86f3744"],"title":"formulaic divine knowledge localized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_2b0f31137b12e53ff313","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:governed-domain-and-mode-frame","source_type":"word_analysis","support_ids":["sup_681c5fae08c4c61613a7","sup_eec18507f794dbe2e770"],"title":"domain and mode frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_ca98c0bbe70b6ef80a6a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:spatial-enclosure-as-knowledge","source_type":"word_analysis","support_ids":["sup_2df71bb1de65643a6dec","sup_681c5fae08c4c61613a7"],"title":"spatial enclosure converted into knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91:6"],"branch_refs":[],"candidate_id":"cand_017c8917a6a64c787547","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:6:bi-contact-and-fusion","source_type":"word_analysis","support_ids":["sup_0e8b4e1a0ee358108875","sup_2dc8a10e839eace6a76d"],"title":"contact pressure in fused domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:6","qac_refs":["18:91:4:1"],"status":"accepted"}},{"anchor_refs":["18:91:6"],"branch_refs":[],"candidate_id":"cand_497ec8074f9482d39e96","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:6:bi-governed-domain","source_type":"word_analysis","support_ids":["sup_0e8b4e1a0ee358108875","sup_ce11a83f7a80035fca38"],"title":"governed domain marker","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:6","qac_refs":["18:91:4:1"],"status":"accepted"}},{"anchor_refs":["18:91:7"],"branch_refs":[],"candidate_id":"cand_384c3cd71eec4150e2a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:7:open-relative-governed-domain","source_type":"word_analysis","support_ids":["sup_8d4cb657c5121a9dda5c","sup_a55bab4d3ee45624348c"],"title":"open relative domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:7","qac_refs":["18:91:4:2"],"status":"accepted"}},{"anchor_refs":["18:91:8"],"branch_refs":[],"candidate_id":"cand_c2f3631e8569c5d49510","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:8:proximate-possessor-domain","source_type":"word_analysis","support_ids":["sup_6fde359a556544d6bcb2","sup_c7e9b909f08cfc6a28a1"],"title":"proximate possessor-domain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:8","qac_refs":["18:91:5:1","18:91:5:2"],"status":"accepted"}},{"anchor_refs":["18:91:8"],"branch_refs":[],"candidate_id":"cand_1298f2fe4e28ae11075a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:8:relative-completion-before-tamyiz","source_type":"word_analysis","support_ids":["sup_c7e9b909f08cfc6a28a1","sup_c8cffb31962f09c31af5"],"title":"relative completion before specification","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:8","qac_refs":["18:91:5:1","18:91:5:2"],"status":"accepted"}},{"anchor_refs":["18:91:8"],"branch_refs":[],"candidate_id":"cand_b2cbbe386e75222373e6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"18:91:8:suffix-referent-boundary-recovery","source_type":"word_analysis","support_ids":["sup_0a062c97a70d99fa098d","sup_c7e9b909f08cfc6a28a1"],"title":"suffix recovers Dhū al-Qarnayn","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:8","qac_refs":["18:91:5:1","18:91:5:2"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_f71a02805ea8595f82b5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:closure-sound-and-boundary-cadence","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_80c060f0f9a96973ba99"],"title":"dense closure and boundary cadence","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_543b6e6ec184b0f6ef7d","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:masdar-not-title","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_84f8944bd813d76998e8"],"title":"gerund process rather than title","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_cbc1f73970a726ac0f73","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:qiraat-weight-preserved-role","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_d526382d3ea894e4ac04"],"title":"variant weight without syntactic shift","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_d3a22218766f47ef518e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:same-surah-echo-18-68","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_66ed32597f52b15464be"],"title":"18:68 reversal of human non-encompassment","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_95d319ccf1d34907bb30","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:tamyiz-knowledge-mode","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_f2e04f3db71780bf82cd"],"title":"accusative knowledge-mode","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:9"],"branch_refs":[],"candidate_id":"cand_a2f6633bb58309162748","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:9:tested-reportable-acquaintance","source_type":"word_analysis","support_ids":["sup_07af206f2dd97b0da6ab","sup_455ba871c7171181dc65"],"title":"tested and reportable knowledge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:9","qac_refs":["18:91:6:1"],"status":"accepted"}},{"anchor_refs":["18:91:3"],"branch_refs":[],"candidate_id":"cand_bb0a9aa99970da7e944c","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:3:1","source_type":"qac_morpheme","support_ids":["sup_12d361c0ae8d5bcfed9d"],"title":"QAC root occurrence: ح و ط","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:91:6"],"branch_refs":[],"candidate_id":"cand_c67b89f23b53a6632d34","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000387"],"scope":"focus_ayah","source_local_id":"18:91:6:1","source_type":"qac_morpheme","support_ids":["sup_8c5cf870d0c18a1b597a"],"title":"QAC root occurrence: خ ب ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["18:91:5"],"branch_refs":[],"candidate_id":"cand_2a0acd8e50ba662fa444","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000372"],"scope":"focus_ayah","source_local_id":"18:91:5:phonetic-density","source_type":"word_analysis","support_ids":["sup_681c5fae08c4c61613a7","sup_c0ff0c2397dd07cc5f80"],"title":"phonetic density","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"18:91:5","qac_refs":["18:91:3:1","18:91:3:2"],"status":"accepted"}},{"anchor_refs":["18:91"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:91","branch_refs":["root_000372/B004","root_000387/B001"],"candidate_id":"cand_5b49b28e7610e428562b","commentary_obligation":"review","hft_ref":"hft_fea8dba5b1ee7ddb74fb","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_total_interior_knowledge","source_type":"hft","support_ids":["sup_3b9030bdd955aa8e05b0"],"title":"baseline_total_interior_knowledge","trust":"legacy_unbound"},{"anchor_refs":["18:91"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:91","branch_refs":["root_000372/B002","root_000387/B001"],"candidate_id":"cand_d245abba4eba71397244","commentary_obligation":"review","hft_ref":"hft_43c7ab58e00a1b06aa43","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_informed_custody","source_type":"hft","support_ids":["sup_aeda0139e0e66cf77048"],"title":"baseline_informed_custody","trust":"legacy_unbound"},{"anchor_refs":["18:91"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"18:91","branch_refs":["root_000372/B001","root_000387/B002"],"candidate_id":"cand_969feb829d06e7af46c2","commentary_obligation":"review","hft_ref":"hft_d732a40a82a4ff34f320","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_embodied_station_survey","source_type":"hft","support_ids":["sup_9efe344c8d839dcee658"],"title":"baseline_embodied_station_survey","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|ka+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:91:1:1","qac_word_ref":"18:91:1","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"18:91:1:2","qac_word_ref":"18:91:1","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"18:91:2:1","qac_word_ref":"18:91:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"18:91:2:2","qac_word_ref":"18:91:2","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","root_ar":"ح و ط","surface_ar":"أَحَطْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:91:3:2","qac_word_ref":"18:91:3","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:91:4:1","qac_word_ref":"18:91:4","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"18:91:4:2","qac_word_ref":"18:91:4","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"لَدَي","morph_features":"STEM|POS:LOC|LEM:laday","morpheme_role":"STEM","pos":"LOC","qac_ref":"18:91:5:1","qac_word_ref":"18:91:5","root_ar":"","surface_ar":"لَدَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:91:5:2","qac_word_ref":"18:91:5","root_ar":"","surface_ar":"هِ"},{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","root_ar":"خ ب ر","surface_ar":"خُبْرًا"}],"word_analysis_qac_refs":[["18:91:1:1"],["18:91:1:2"],["18:91:2:1"],["18:91:2:2"],["18:91:3:1","18:91:3:2"],["18:91:4:1"],["18:91:4:2"],["18:91:5:1","18:91:5:2"],["18:91:6:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["18:91:1","18:91:2","18:91:3","18:91:4","18:91:5","18:91:6","18:91:7","18:91:8","18:91:9"]},"focus_surface_evidence":{"arabic_uthmani":"كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|ka+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:91:1:1","qac_word_ref":"18:91:1","root_ar":"","surface_ar":"كَ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"18:91:1:2","qac_word_ref":"18:91:1","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"18:91:2:1","qac_word_ref":"18:91:2","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"قَد","morph_features":"STEM|POS:CERT|LEM:qad","morpheme_role":"STEM","pos":"CERT","qac_ref":"18:91:2:2","qac_word_ref":"18:91:2","root_ar":"","surface_ar":"قَدْ"},{"lemma_ar":"أَحَاطَ","morph_features":"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P","morpheme_role":"STEM","pos":"V","qac_ref":"18:91:3:1","qac_word_ref":"18:91:3","root_ar":"ح و ط","surface_ar":"أَحَطْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:1P","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:91:3:2","qac_word_ref":"18:91:3","root_ar":"","surface_ar":"نَا"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"18:91:4:1","qac_word_ref":"18:91:4","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:REL|LEM:maA","morpheme_role":"STEM","pos":"REL","qac_ref":"18:91:4:2","qac_word_ref":"18:91:4","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"لَدَي","morph_features":"STEM|POS:LOC|LEM:laday","morpheme_role":"STEM","pos":"LOC","qac_ref":"18:91:5:1","qac_word_ref":"18:91:5","root_ar":"","surface_ar":"لَدَيْ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"18:91:5:2","qac_word_ref":"18:91:5","root_ar":"","surface_ar":"هِ"},{"lemma_ar":"خُبْر","morph_features":"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"18:91:6:1","qac_word_ref":"18:91:6","root_ar":"خ ب ر","surface_ar":"خُبْرًا"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["18:91:1:1"],["18:91:1:2"],["18:91:2:1"],["18:91:2:2"],["18:91:3:1","18:91:3:2"],["18:91:4:1"],["18:91:4:2"],["18:91:5:1","18:91:5:2"],["18:91:6:1"]],"word_analysis_refs":["18:91:1","18:91:2","18:91:3","18:91:4","18:91:5","18:91:6","18:91:7","18:91:8","18:91:9"],"word_rows":[{"analysis_record_ref":"18:91:1","analytic_gloss_range_en":"comparison particle governing the following demonstrative and opening a retrospective discourse frame","analytic_root_gloss_range_en":null,"qac_refs":["18:91:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"كَ","transliteration":"ka"}},{"analysis_record_ref":"18:91:2","analytic_gloss_range_en":"distal demonstrative recovering a prior discourse unit inside the comparison phrase","analytic_root_gloss_range_en":null,"qac_refs":["18:91:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"18:91:3","analytic_gloss_range_en":"resumptive connector in a {{ar:وَقَدْ}} ({{tr:wa-qad}}) sequence, with circumstantial background pressure","analytic_root_gloss_range_en":null,"qac_refs":["18:91:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"18:91:4","analytic_gloss_range_en":"certainty particle with a perfect verb, marking verified completed action with anterior/background force","analytic_root_gloss_range_en":null,"qac_refs":["18:91:2:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"قَدْ","transliteration":"qad"}},{"analysis_record_ref":"18:91:5","analytic_gloss_range_en":"completed divine encompassing directed through a bāʾ-marked domain and specified as knowledge","analytic_root_gloss_range_en":"root range includes surrounding, guarding, wall/enclosure imagery, complete grasp, maneuvering, ruin/overtaking, ornament, and completion of deficiency; local Form IV plus {{ar:خُبْرًا}} ({{tr:khubran}}) selects comprehensive epistemic encompassing while preserving enclosure imagery","qac_refs":["18:91:3:1","18:91:3:2"],"root":{"arabic":"ح و ط","transliteration":"ḥ-w-ṭ"},"surface":{"arabic":"أَحَطْنَا","transliteration":"aḥaṭnā"}},{"analysis_record_ref":"18:91:6","analytic_gloss_range_en":"preposition governing the open relative domain after the encompassing verb","analytic_root_gloss_range_en":null,"qac_refs":["18:91:4:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"بِ","transliteration":"bi"}},{"analysis_record_ref":"18:91:7","analytic_gloss_range_en":"relative pronoun that heads an open, governed domain completed by the following locative phrase","analytic_root_gloss_range_en":null,"qac_refs":["18:91:4:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"18:91:8","analytic_gloss_range_en":"locative adverbial with attached masculine singular suffix, completing the relative domain as what is at hand with him","analytic_root_gloss_range_en":null,"qac_refs":["18:91:5:1","18:91:5:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"لَدَيْهِ","transliteration":"ladayhi"}},{"analysis_record_ref":"18:91:9","analytic_gloss_range_en":"indefinite accusative verbal noun specifying the encompassing as verified, comprehensive knowledge","analytic_root_gloss_range_en":"root range includes report/information, tested inner knowledge, inquiry, soft low ground, cultivation/sharecropping, abundance in a waterskin or milk-rich camel, softness, and shared portions; local gerund selects knowledge by report/tested acquaintance, not the non-epistemic branches","qac_refs":["18:91:6:1"],"root":{"arabic":"خ ب ر","transliteration":"kh-b-r"},"surface":{"arabic":"خُبْرًا","transliteration":"khubran"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":9,"words_total":9,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["18:91"],"branch_refs":["root_000372/B004","root_000387/B001"],"candidate_id":"cand_5b49b28e7610e428562b","evidence_scope":"focus_ayah","hft_ref":"hft_fea8dba5b1ee7ddb74fb","item_id":"baseline_total_interior_knowledge","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_total_interior_knowledge","support_id":"sup_3b9030bdd955aa8e05b0"},{"anchor_refs":["18:91"],"branch_refs":["root_000372/B002","root_000387/B001"],"candidate_id":"cand_d245abba4eba71397244","evidence_scope":"focus_ayah","hft_ref":"hft_43c7ab58e00a1b06aa43","item_id":"baseline_informed_custody","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_informed_custody","support_id":"sup_aeda0139e0e66cf77048"},{"anchor_refs":["18:91"],"branch_refs":["root_000372/B001","root_000387/B002"],"candidate_id":"cand_969feb829d06e7af46c2","evidence_scope":"focus_ayah","hft_ref":"hft_d732a40a82a4ff34f320","item_id":"baseline_embodied_station_survey","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_embodied_station_survey","support_id":"sup_9efe344c8d839dcee658"}],"diagnostics":[],"lane_counts":{"global":7,"macro":8,"micro":3},"packet_summary":{"ayah_count":16,"focus_ref":"18:91","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["18:83","18:84","18:85","18:86","18:87","18:88","18:89","18:90","18:91","18:92","18:93","18:94","18:95","18:96","18:97","18:98"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"18:91","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":7,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"18:91","lane":"micro","linguistic_source_ref":"18:91","surface_ref":"18:91","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"18:91","target_tokens":[["İşte",["18:91:1"]],["böyleydi",["18:91:1"]],["Biz",["18:91:2"]],["onun",["18:91:2"]],["sahip",["18:91:3"]],["olduğu",["18:91:4"]],["her",["18:91:4"]],["şeyi",["18:91:5"]],["bilgimizle",["18:91:5"]],["kuşatmıştık",["18:91:6"]]],"text":"İşte böyleydi. Biz onun sahip olduğu her şeyi bilgimizle kuşatmıştık."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":83,"ayah_to":98,"id":"s018-p05-083-098","label":"Dhul-Qarnayn and Gog and Magog","number":5,"refs":["18:83","18:84","18:85","18:86","18:87","18:88","18:89","18:90","18:91","18:92","18:93","18:94","18:95","18:96","18:97","18:98"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9","source_type":"word_analysis","support_id":"sup_07af206f2dd97b0da6ab","text":"{\"gloss_range\":\"indefinite accusative verbal noun specifying the encompassing as verified, comprehensive knowledge\",\"prose\":\"{{ar:خُبْرًا}} ({{tr:khubran}}) is the final accusative specification, so it tells the reader what kind of encompassing {{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}}) is. It is not another thing inside {{ar:مَا لَدَيْهِ}} ({{tr:mā ladayhi}}), and it is not the adjective-title {{ar:خَبِيرٌ}} ({{tr:khabīrun}}); it is a rare gerund that makes knowledge the clause's closing operation. The supported {{ar:خ ب ر}} ({{tr:kh-b-r}}) branch gives reportable, tested acquaintance, and the same-surah pairing with 18:68 reverses human non-encompassment into divine completed knowledge. Variant {{ar:خُبُرًا}} ({{tr:khuburan}}) expands the sound-weight while preserving the same accusative role.\",\"root_display\":\"{{ar:خ ب ر}} ({{tr:kh-b-r}})\",\"root_gloss_range\":\"root range includes report/information, tested inner knowledge, inquiry, soft low ground, cultivation/sharecropping, abundance in a waterskin or milk-rich camel, softness, and shared portions; local gerund selects knowledge by report/tested acquaintance, not the non-epistemic branches\",\"surface_display\":\"{{ar:خُبْرًا}} ({{tr:khubran}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:8:suffix-referent-boundary-recovery","source_type":"word_analysis","support_id":"sup_0a062c97a70d99fa098d","text":"{\"blocking_evidence\":null,\"headline\":\"suffix recovers Dhū al-Qarnayn\",\"reader_payoff\":\"The reader notices that the attached suffix carries the protagonist across the ayah boundary without renaming him.\",\"reason\":\"Attachment evidence resolves the masculine singular suffix to Dhū al-Qarnayn and warns against routing it to a nearer abstract or scene element.\",\"representative_source_ids\":[\"QG-f0798208\",\"QF-b400d020\",\"QB-8e3a7545\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:6","source_type":"word_analysis","support_id":"sup_0e8b4e1a0ee358108875","text":"{\"gloss_range\":\"preposition governing the open relative domain after the encompassing verb\",\"prose\":\"{{ar:بِ}} ({{tr:bi}}) is the small hinge that lets {{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}}) take {{ar:مَا لَدَيْهِ}} ({{tr:mā ladayhi}}) as its domain. It routes the verb toward a field rather than a bare direct object, and its attachment/contact pressure makes that field feel closely surrounded before {{ar:خُبْرًا}} ({{tr:khubran}}) names the knowledge-mode.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:91:3:1","source_type":"qac_morpheme","support_id":"sup_12d361c0ae8d5bcfed9d","text":"{\"lemma_ar\":\"أَحَاطَ\",\"morph_features\":\"STEM|POS:V|PERF|(IV)|LEM:>aHaATa|ROOT:HwT|1P\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"18:91:3:1\",\"qac_word_ref\":\"18:91:3\",\"root_ar\":\"ح و ط\",\"surface_ar\":\"أَحَطْ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:1:kaf-retrospective-comparison","source_type":"word_analysis","support_id":"sup_2bb58c6e794009ceea68","text":"{\"blocking_evidence\":null,\"headline\":\"retrospective comparison hinge\",\"reader_payoff\":\"The reader notices that the ayah first turns backward to the completed scene before it gives the divine knowledge frame.\",\"reason\":\"The QAC grammar identifies {{ar:كَ}} ({{tr:ka}}) as comparison, and attachment evidence ties {{ar:كَذَٰلِكَ}} ({{tr:kadhālika}}) to the preceding episode, so the CRITICAL comparison, fused form, and boundary rows are locally supported.\",\"representative_source_ids\":[\"QG-4f3d0ba6\",\"QS-668170ea\",\"QB-17402fe2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:6:bi-contact-and-fusion","source_type":"word_analysis","support_id":"sup_2dc8a10e839eace6a76d","text":"{\"blocking_evidence\":null,\"headline\":\"contact pressure in fused domain\",\"reader_payoff\":\"The reader notices that the fused {{ar:بِمَا}} ({{tr:bimā}}) makes the broad domain arrive as one compact governed unit.\",\"reason\":\"The contact nuance is useful as particle pressure, but local syntax primarily licenses the bāʾ as a governed domain marker.\",\"representative_source_ids\":[\"QS-89d5be4c\",\"QF-890f654f\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:spatial-enclosure-as-knowledge","source_type":"word_analysis","support_id":"sup_2df71bb1de65643a6dec","text":"{\"blocking_evidence\":null,\"headline\":\"spatial enclosure converted into knowledge\",\"reader_payoff\":\"The reader notices the concrete perimeter image inside the verb, while the local grammar makes that perimeter an image of comprehensive knowing.\",\"reason\":\"V4 supports surrounding, guarding, and wall-field branches for {{ar:ح و ط}} ({{tr:ḥ-w-ṭ}}), but {{ar:خُبْرًا}} ({{tr:khubran}}) narrows local activation to epistemic encompassing rather than architecture, self-precaution, or simple guarding.\",\"representative_source_ids\":[\"QS-d9bbed3e\",\"QS-de3d668a\",\"QY-e380c03c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:2","source_type":"word_analysis","support_id":"sup_367788b2f972aa95831f","text":"{\"gloss_range\":\"distal demonstrative recovering a prior discourse unit inside the comparison phrase\",\"prose\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}}) supplies the content-bearing pointer in {{ar:كَذَٰلِكَ}} ({{tr:kadhālika}}). Its definiteness assumes that the reader can recover the referent from 18:90, while its distal quality holds that scene at discourse distance as a completed object of comment. The result is not another travel event but a seal that lets the verse pivot into divine assessment.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:3:wa-qad-backgrounded-aside","source_type":"word_analysis","support_id":"sup_428425eb6bce9f27df73","text":"{\"blocking_evidence\":null,\"headline\":\"backgrounded divine aside\",\"reader_payoff\":\"The reader notices that the connector changes discourse layer instead of adding another travel action.\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) here as resumptive, and the clause evidence places {{ar:وَقَدْ أَحَطْنَا}} ({{tr:wa-qad aḥaṭnā}}) as the finite predicate of the resumed divine statement.\",\"representative_source_ids\":[\"QG-7f0f4da4\",\"QG-e1d0eaca\",\"MT-c789f34b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:tested-reportable-acquaintance","source_type":"word_analysis","support_id":"sup_455ba871c7171181dc65","text":"{\"blocking_evidence\":null,\"headline\":\"tested and reportable knowledge\",\"reader_payoff\":\"The reader notices that the knowledge is not bare information; it has the pressure of probed, reliable acquaintance that can be stated in the divine aside.\",\"reason\":\"V4 supports the report/tested-knowledge branch for {{ar:خ ب ر}} ({{tr:kh-b-r}}), while local syntax selects the knowledge result rather than a literal testing event or non-epistemic branch.\",\"representative_source_ids\":[\"QS-631d3008\",\"QS-af407a83\",\"QY-a3a4b165\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:2:kadhālika-boundary-marker","source_type":"word_analysis","support_id":"sup_48060590e16281b81058","text":"{\"blocking_evidence\":null,\"headline\":\"boundary-marker recurrence\",\"reader_payoff\":\"The reader notices that the phrase has boundary-marking force here, while the local syntax keeps it tied to this immediate episode.\",\"reason\":\"The recurrence claim is useful as discourse pressure, but without a concrete local cross-reference list it should not control the parse beyond the demonstrative's boundary position.\",\"representative_source_ids\":[\"QE-6bc0e21b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:discourse-pivot-from-journey-to-aside","source_type":"word_analysis","support_id":"sup_507e2a251892f3bbbd82","text":"{\"blocking_evidence\":null,\"headline\":\"pivot from journey to aside\",\"reader_payoff\":\"The reader notices that the verb replaces travel narration with the main assertion of a divine aside.\",\"reason\":\"The clause begins after the deictic seal and contains the finite predicate of the resumed statement, so this verb is the structural pivot.\",\"representative_source_ids\":[\"QT-cef9fdf0\",\"QT-d959371e\",\"QB-4b878637\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:4","source_type":"word_analysis","support_id":"sup_634b4a7665e4afed4db4","text":"{\"gloss_range\":\"certainty particle with a perfect verb, marking verified completed action with anterior/background force\",\"prose\":\"{{ar:قَدْ}} ({{tr:qad}}) verifies the whole knowledge assertion, not just the verb stem. With the perfect {{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}}), it makes divine encompassing an already completed and assured fact, so the audience receives the clause as backgrounded epistemic framing rather than a new inference from the journey scene.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:قَدْ}} ({{tr:qad}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:same-surah-echo-18-68","source_type":"word_analysis","support_id":"sup_66ed32597f52b15464be","text":"{\"blocking_evidence\":null,\"headline\":\"18:68 reversal of human non-encompassment\",\"reader_payoff\":\"The reader notices that the rare gerund answers an earlier same-surah inability frame with divine completed capacity (18:68).\",\"reason\":\"The same-surah echo is concrete and contrastive: 18:68 denies human encompassing knowledge, while 18:91 places {{ar:خُبْرًا}} ({{tr:khubran}}) under divine completed encompassing.\",\"representative_source_ids\":[\"QI-a8e10562\",\"QE-d8a7b28d\",\"QH-5a2b95da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5","source_type":"word_analysis","support_id":"sup_681c5fae08c4c61613a7","text":"{\"gloss_range\":\"completed divine encompassing directed through a bāʾ-marked domain and specified as knowledge\",\"prose\":\"{{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}}) is the clause pivot. Its Form IV perfect and fused {{ar:نَا}} ({{tr:nā}}) subject present a completed divine act, while the following {{ar:بِمَا لَدَيْهِ}} ({{tr:bimā ladayhi}}) gives the domain and {{ar:خُبْرًا}} ({{tr:khubran}}) gives the knowledge-mode. The root's surrounding and wall-field pressure remains visible, but the final accusative narrows the local action from physical encirclement to epistemic enclosure: whatever was with Dhū al-Qarnayn is already held within completed divine knowledge. This also answers same-surah failure or passivity around encompassing at 18:42 and 18:68, and it participates in broader divine-knowledge formulas (2:255; 4:108; 65:12) without becoming generic.\",\"root_display\":\"{{ar:ح و ط}} ({{tr:ḥ-w-ṭ}})\",\"root_gloss_range\":\"root range includes surrounding, guarding, wall/enclosure imagery, complete grasp, maneuvering, ruin/overtaking, ornament, and completion of deficiency; local Form IV plus {{ar:خُبْرًا}} ({{tr:khubran}}) selects comprehensive epistemic encompassing while preserving enclosure imagery\",\"surface_display\":\"{{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:8:proximate-possessor-domain","source_type":"word_analysis","support_id":"sup_6fde359a556544d6bcb2","text":"{\"blocking_evidence\":null,\"headline\":\"proximate possessor-domain\",\"reader_payoff\":\"The reader notices that the broad domain is not vague; it is whatever lies within one protagonist's immediate sphere.\",\"reason\":\"QAC and attachment evidence support {{ar:لَدَيْهِ}} ({{tr:ladayhi}}) as a locative expression with possessive suffix, completing the relative content of {{ar:مَا}} ({{tr:mā}}).\",\"representative_source_ids\":[\"QG-0a4d491a\",\"QS-7ea20321\",\"QY-b0749014\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:divine-knowledge-formula-localized","source_type":"word_analysis","support_id":"sup_773dbb8cc981a86f3744","text":"{\"blocking_evidence\":null,\"headline\":\"formulaic divine knowledge localized\",\"reader_payoff\":\"The reader notices a wider Quranic divine-knowledge construction, but sees it anchored to Dhū al-Qarnayn's immediate domain here.\",\"reason\":\"The {{ar:أَحَاطَ}} ({{tr:aḥāṭa}}) plus {{ar:بِ}} ({{tr:bi}}) pattern is supported as a divine-knowledge frame (2:255; 4:108; 65:12), while the local object remains {{ar:مَا لَدَيْهِ}} ({{tr:mā ladayhi}}).\",\"representative_source_ids\":[\"QI-81fea9c0\",\"MI-a715963f\",\"QE-ccb39109\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:closure-sound-and-boundary-cadence","source_type":"word_analysis","support_id":"sup_80c060f0f9a96973ba99","text":"{\"blocking_evidence\":null,\"headline\":\"dense closure and boundary cadence\",\"reader_payoff\":\"The reader notices the final word's compact sound and its boundary contrast with the prior closure at 18:90, while grammar remains the main interpretive control.\",\"reason\":\"The acoustic and boundary observations are useful only after being limited by the syntactic fact that {{ar:خُبْرًا}} ({{tr:khubran}}) is a tamyīz.\",\"representative_source_ids\":[\"QP-39cf2efb\",\"QP-be119910\",\"QB-518fd5bd\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:masdar-not-title","source_type":"word_analysis","support_id":"sup_84f8944bd813d76998e8","text":"{\"blocking_evidence\":null,\"headline\":\"gerund process rather than title\",\"reader_payoff\":\"The reader notices that the ayah closes on knowledge in operation rather than merely naming the knower with an attribute.\",\"reason\":\"The local form is an indefinite gerund, while the broader root field includes the frequent adjective {{ar:خَبِيرٌ}} ({{tr:khabīrun}}); the contrast is form-level, not a rejection of the divine-knowledge field.\",\"representative_source_ids\":[\"QG-24654f59\",\"QF-66d74dc5\",\"QI-ce131deb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:2:demonstrative-discourse-seal","source_type":"word_analysis","support_id":"sup_870cb74d6a3864b74614","text":"{\"blocking_evidence\":null,\"headline\":\"definite distal scene seal\",\"reader_payoff\":\"The reader notices that a single demonstrative gathers the prior scene into a completed unit before commentary begins.\",\"reason\":\"QAC and attachment evidence support {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) as a demonstrative governed by {{ar:كَ}} ({{tr:ka}}), with referent supplied by the prior episode.\",\"representative_source_ids\":[\"QG-3806dc11\",\"QS-64dcda91\",\"QB-254ec29d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"18:91:6:1","source_type":"qac_morpheme","support_id":"sup_8c5cf870d0c18a1b597a","text":"{\"lemma_ar\":\"خُبْر\",\"morph_features\":\"STEM|POS:N|LEM:xubor|ROOT:xbr|M|INDEF|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"18:91:6:1\",\"qac_word_ref\":\"18:91:6\",\"root_ar\":\"خ ب ر\",\"surface_ar\":\"خُبْرًا\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:7:open-relative-governed-domain","source_type":"word_analysis","support_id":"sup_8d4cb657c5121a9dda5c","text":"{\"blocking_evidence\":null,\"headline\":\"open relative domain\",\"reader_payoff\":\"The reader notices that the domain is both syntactically controlled and semantically expansive.\",\"reason\":\"QAC identifies {{ar:مَا}} ({{tr:mā}}) as a relative pronoun, and attachment evidence confirms that it is governed by {{ar:بِ}} ({{tr:bi}}) and completed by {{ar:لَدَيْهِ}} ({{tr:ladayhi}}).\",\"representative_source_ids\":[\"QG-14e88f08\",\"QG-d096dc67\",\"QY-bf419d20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:7","source_type":"word_analysis","support_id":"sup_a55bab4d3ee45624348c","text":"{\"gloss_range\":\"relative pronoun that heads an open, governed domain completed by the following locative phrase\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) keeps the encompassed content open while keeping it grammatically bounded. It is governed by {{ar:بِ}} ({{tr:bi}}), heads the relative phrase, and waits for {{ar:لَدَيْهِ}} ({{tr:ladayhi}}) to complete it. The reader hears breadth first, then learns that the breadth belongs to Dhū al-Qarnayn's at-hand sphere.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:3","source_type":"word_analysis","support_id":"sup_a7f7719d61d7e545b5f2","text":"{\"gloss_range\":\"resumptive connector in a {{ar:وَقَدْ}} ({{tr:wa-qad}}) sequence, with circumstantial background pressure\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) keeps the opening seal and the verified knowledge clause as distinct beats. In {{ar:وَقَدْ}} ({{tr:wa-qad}}), the connector does not simply continue the travel sequence; it opens a divine aside and can also make that aside the background condition under which the scene unfolded.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:4:qad-verified-anterior-completion","source_type":"word_analysis","support_id":"sup_a8b5a1b52c9b8d1e760b","text":"{\"blocking_evidence\":null,\"headline\":\"verified prior completion\",\"reader_payoff\":\"The reader notices that divine knowledge is presented as already complete before the narrated scene is assessed.\",\"reason\":\"The local verb is perfect, so {{ar:قَدْ}} ({{tr:qad}}) carries taḥqīq and completed-background force rather than possibility.\",\"representative_source_ids\":[\"QG-1c499b8c\",\"QG-9d513479\",\"MT-28889369\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:phonetic-density","source_type":"word_analysis","support_id":"sup_c0ff0c2397dd07cc5f80","text":"{\"blocking_evidence\":null,\"headline\":\"phonetic density\",\"reader_payoff\":null,\"reason\":\"No guardrail contradicts the phonetic observation, but it is decorative at this processing layer and would not materially guide lexical review or translation.\",\"representative_source_ids\":[\"QP-1699f0f4\"],\"status\":\"dropped_filler\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:8","source_type":"word_analysis","support_id":"sup_c7e9b909f08cfc6a28a1","text":"{\"gloss_range\":\"locative adverbial with attached masculine singular suffix, completing the relative domain as what is at hand with him\",\"prose\":\"{{ar:لَدَيْهِ}} ({{tr:ladayhi}}) fixes the open {{ar:مَا}} ({{tr:mā}}) to one possessor-domain. As a locative expression it makes the field what is at hand with him, and the attached masculine {{ar:ـهِ}} ({{tr:-hi}}) routes that field back to Dhū al-Qarnayn rather than to the sun or the exposed people of 18:90. It completes the relative phrase before {{ar:خُبْرًا}} ({{tr:khubran}}) states the mode of divine encompassing.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:لَدَيْهِ}} ({{tr:ladayhi}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:8:relative-completion-before-tamyiz","source_type":"word_analysis","support_id":"sup_c8cffb31962f09c31af5","text":"{\"blocking_evidence\":null,\"headline\":\"relative completion before specification\",\"reader_payoff\":\"The reader notices the order: first the domain is located with him, then the final word names the knowledge-mode covering it.\",\"reason\":\"The local syntax completes {{ar:مَا}} ({{tr:mā}}) with {{ar:لَدَيْهِ}} ({{tr:ladayhi}}) before the separate accusative specification.\",\"representative_source_ids\":[\"QT-0b70ad1f\",\"QT-eaf0a01e\",\"MT-384e769e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:completed-divine-active-agency","source_type":"word_analysis","support_id":"sup_c970a0c39b8f513e80e3","text":"{\"blocking_evidence\":null,\"headline\":\"completed divine active agency\",\"reader_payoff\":\"The reader notices that encompassment is not lacking, passive, attempted, or ongoing here; it is completed by the divine speaker.\",\"reason\":\"The local form is active perfect Form IV with first-person plural agreement, and same-surah contrasts at 18:42 and 18:68 sharpen the active divine completion without overriding the local parse.\",\"representative_source_ids\":[\"QG-b1ac3cd0\",\"QF-b26e9677\",\"QI-6496fd3c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:6:bi-governed-domain","source_type":"word_analysis","support_id":"sup_ce11a83f7a80035fca38","text":"{\"blocking_evidence\":null,\"headline\":\"governed domain marker\",\"reader_payoff\":\"The reader notices that the object of encompassing is a governed domain, not a loose afterthought or the final knowledge noun.\",\"reason\":\"Attachment and valency evidence show {{ar:بِ}} ({{tr:bi}}) marking the complement selected by the encompassing verb.\",\"representative_source_ids\":[\"QG-72c1980c\",\"QG-a86aee38\",\"QT-4086ea46\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:qiraat-weight-preserved-role","source_type":"word_analysis","support_id":"sup_d526382d3ea894e4ac04","text":"{\"blocking_evidence\":null,\"headline\":\"variant weight without syntactic shift\",\"reader_payoff\":\"The reader notices that the recitational variant changes the closing word's internal weight without changing its grammatical job.\",\"reason\":\"The variant {{ar:خُبُرًا}} ({{tr:khuburan}}) is useful for sound and form pressure, but the accusative specification role remains stable.\",\"representative_source_ids\":[\"QF-d5b5c10a\",\"QF-f22b905b\",\"QP-018841c0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:1","source_type":"word_analysis","support_id":"sup_ec504f08009472d95272","text":"{\"gloss_range\":\"comparison particle governing the following demonstrative and opening a retrospective discourse frame\",\"prose\":\"{{ar:كَ}} ({{tr:ka}}) does not open a fresh narrative item by itself. As the comparison side of {{ar:كَذَٰلِكَ}} ({{tr:kadhālika}}), it binds the verse back to the preceding sunrise-side scene (18:90), making the new divine assertion read as a retrospective hinge: the prior scene is the comparison base, and the knowledge clause explains how that scene was already contained.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:كَ}} ({{tr:ka}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:5:governed-domain-and-mode-frame","source_type":"word_analysis","support_id":"sup_eec18507f794dbe2e770","text":"{\"blocking_evidence\":null,\"headline\":\"domain and mode frame\",\"reader_payoff\":\"The reader notices the clause is architected as act, domain, and knowledge-mode rather than a simple object statement.\",\"reason\":\"Attachment and valency evidence confirm that the verb governs a {{ar:بِ}} ({{tr:bi}}) complement and receives {{ar:خُبْرًا}} ({{tr:khubran}}) as accusative specification.\",\"representative_source_ids\":[\"QG-0184a4b2\",\"QG-e337d3a0\",\"QY-f83060b8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"18:91:9:tamyiz-knowledge-mode","source_type":"word_analysis","support_id":"sup_f2e04f3db71780bf82cd","text":"{\"blocking_evidence\":null,\"headline\":\"accusative knowledge-mode\",\"reader_payoff\":\"The reader notices that the final word specifies the mode of encompassing, not a possessed item or loose object.\",\"reason\":\"QAC and attachment evidence identify {{ar:خُبْرًا}} ({{tr:khubran}}) as an accusative tamyīz/specification of {{ar:أَحَطْنَا}} ({{tr:aḥaṭnā}}).\",\"representative_source_ids\":[\"QG-00a48049\",\"QG-bb9683f6\",\"QT-70151a95\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا","ayah_ref":"18:91"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000372/B004","root_000387/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000372","role":"Complete enclosure in knowledge supplies the mechanism's all-sided epistemic scope.","root":"ح و ط","source_ref":"18:91","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000387","role":"Knowledge of news and an affair's interior supplies depth beyond outward report.","root":"خ ب ر","source_ref":"18:91","source_word_indices":["6"]}],"changed_reading":{"after":"God's prior knowledge completely surrounds every side and inward reality of what was present to him.","before":"God knew what was with him."},"confidence":"strong","focus_anchor":"The pairing of word 3 (ahata) with word 6 (khubran).","mechanism":"All-sided enclosure combines with knowledge of an affair's interior, so the clause asserts exhaustive depth rather than receipt of a report.","model_id":"baseline_total_interior_knowledge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_total_interior_knowledge","source_type":"hft","support_id":"sup_3b9030bdd955aa8e05b0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا","ayah_ref":"18:91"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000372/B002","root_000387/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000372","role":"Preservation, care, and precaution turn encompassing into active custody.","root":"ح و ط","source_ref":"18:91","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000387","role":"Interior knowledge makes the proposed custody informed rather than merely defensive.","root":"خ ب ر","source_ref":"18:91","source_word_indices":["6"]}],"changed_reading":{"after":"The clause can also place him and what attended him under informed, preserving oversight.","before":"The clause reports detached awareness of his circumstances."},"confidence":"medium","focus_anchor":"Word 3's preserving branch acts on the open referent 'what was with him,' while word 6 supplies informed inward awareness.","mechanism":"Enclosure can be protective custody as well as perimeter; joined to khubr, it yields watchful care that knows what it preserves.","model_id":"baseline_informed_custody"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_informed_custody","source_type":"hft","support_id":"sup_aeda0139e0e66cf77048","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"كَذَٰلِكَ وَقَدْ أَحَطْنَا بِمَا لَدَيْهِ خُبْرًۭا","ayah_ref":"18:91"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000372/B001","root_000387/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000372","role":"Physical surrounding or fencing supplies a surveyed perimeter.","root":"ح و ط","source_ref":"18:91","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_000387","role":"Soft or low ground with water supplies the exploratory terrain content inside that perimeter.","root":"خ ب ر","source_ref":"18:91","source_word_indices":["6"]}],"changed_reading":{"after":"Exploratorily, the knowledge is embodied as a complete survey of the ground and conditions at his station.","before":"Khubr is treated as purely propositional knowledge."},"confidence":"exploratory","focus_anchor":"The physical branches available at focus words 3 and 6 permit a terrain-level model without leaving the clause.","mechanism":"Sensory enclosure combines with kh-b-r's low, soft, watered ground to picture knowledge as an all-around survey of the material station.","model_id":"baseline_embodied_station_survey"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_embodied_station_survey","source_type":"hft","support_id":"sup_9efe344c8d839dcee658","trust":"legacy_unbound"}]}
</lane_packet_json>
