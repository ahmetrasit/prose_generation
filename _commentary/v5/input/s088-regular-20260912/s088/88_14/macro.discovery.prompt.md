# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:14**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_14/macro.discovery.json` and modify nothing
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

- Macro has no explicitly added external ayat. Assess the declared pericope or host-surah context, including any automatic host basmala, as ordinary non-focus context.

## Response Schema

Return exactly these top-level fields:

```json
{
  "schema_version": "commentary-v5-scope-discovery-v1",
  "ayah_ref": "88:14",
  "lane": "macro",
  "coverage_complete": true,
  "candidate_decisions": [
    {
      "candidate_id": "exact packet candidate ID",
      "decision": "accept | narrow | represented | reject",
      "reason": "specific evidentiary reason",
      "finding_refs": ["macro:stable-key"],
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
      "finding_ref": "macro:stable-key",
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
`macro:`. Accepted/narrowed candidates own dedicated findings. A represented
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
{"branch_registry":[{"boundary":"The vessel, vessels, and containers in which things are placed","branch_kind":null,"branch_ref":"root_000063/B004","candidate_links":[{"candidate_id":"cand_0e07f1c4f266a0d6604c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"vessel or container","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الإناء الوعاء","image_en":"vessel or container"}}],"root_ar":"ء ن ي","root_id":"root_000063","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الإناء الوعاء","image_en":"vessel or container","scope_ar":"الإناء والآنية والأواني وما يوضع فيه الشيء","scope_en":"The vessel, vessels, and containers in which things are placed"},"support_links":["sup_80286e18a4bac3c6cffb"]},{"boundary":"Physical elevation of objects or structures from a lower place to a higher one","branch_kind":null,"branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_e0b5962eda40aa011b0c","lane":"macro"},{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"}],"focus_root_occurrences":[],"gloss":"raising something upward","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"إعلاء الشيء","image_en":"raising something upward"}}],"root_ar":"ر ف ع","root_id":"root_000582","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"إعلاء الشيء","image_en":"raising something upward","scope_ar":"إعلاء الأجسام أو البناء وإزالة الشيء عن موضعه إلى علو","scope_en":"Physical elevation of objects or structures from a lower place to a higher one"},"support_links":["sup_b336ca74d7f3a9612e27","sup_cfa66887abd9775cafcb"]},{"boundary":"The bed, couch, throne-like seat, head base, and settled ease or support.","branch_kind":null,"branch_ref":"root_000697/B011","candidate_links":[{"candidate_id":"cand_e0b5962eda40aa011b0c","lane":"macro"},{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"},{"candidate_id":"cand_223d5984fe02c0e63dca","lane":"macro"}],"focus_root_occurrences":[],"gloss":"place of settled support","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"موضع الاستقرار والاتكاء","image_en":"place of settled support"}}],"root_ar":"س ر ر","root_id":"root_000697","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"موضع الاستقرار والاتكاء","image_en":"place of settled support","scope_ar":"السرير والسرر والأسرة وسرير الرأس وسرير العيش وما يستقر عليه أو عنده","scope_en":"The bed, couch, throne-like seat, head base, and settled ease or support."},"support_links":["sup_80c7c66001a3ef24eccb","sup_b336ca74d7f3a9612e27","sup_cfa66887abd9775cafcb"]},{"boundary":"This branch covers bodily or animal fatness, being fat, making something fat, the fattening medicine, and finding something fat.","branch_kind":null,"branch_ref":"root_000744/B001","candidate_links":[{"candidate_id":"cand_c99e1b0c8e7bc09cf0ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":"fatness as the opposite of leanness","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"السِّمَن ونقيض الهزال","image_en":"fatness as the opposite of leanness"}}],"root_ar":"س م ن","root_id":"root_000744","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"السِّمَن ونقيض الهزال","image_en":"fatness as the opposite of leanness","scope_ar":"يدخل فيه السِّمَن والسَّمين والسِّمان والتسمين بمعنى جعل الشيء سمينا والسُّمْنة الدواء واستسمانه وجدان السمن فيه","scope_en":"This branch covers bodily or animal fatness, being fat, making something fat, the fattening medicine, and finding something fat."},"support_links":["sup_3e0da71c75f0136e8c64"]},{"boundary":"the صفة as an architectural feature and as a saddle or animal fitting","branch_kind":null,"branch_ref":"root_000871/B004","candidate_links":[{"candidate_id":"cand_e0b5962eda40aa011b0c","lane":"macro"}],"focus_root_occurrences":[],"gloss":"bench or pad-like structure","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الصُّفَّة في البناء والسرج","image_en":"bench or pad-like structure"}}],"root_ar":"ص ف ف","root_id":"root_000871","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الصُّفَّة في البناء والسرج","image_en":"bench or pad-like structure","scope_ar":"الصُّفَّة من البنيان، وصُفَّة السرج، وما يعمل للدابة من ذلك","scope_en":"the صفة as an architectural feature and as a saddle or animal fitting"},"support_links":["sup_cfa66887abd9775cafcb"]},{"boundary":"A plant called ṣiliyān, with a large head or spike, grazed by camels and called camel bread.","branch_kind":null,"branch_ref":"root_000880/B010","candidate_links":[{"candidate_id":"cand_c99e1b0c8e7bc09cf0ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":"a grazing plant called siliyan","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"الصِّليان نبت ترعاه الإبل","image_en":"a grazing plant called siliyan"}}],"root_ar":"ص ل ي","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"الصِّليان نبت ترعاه الإبل","image_en":"a grazing plant called siliyan","scope_ar":"الصليان نبت عظيم السنمة أو السنبلة ترعاه الإبل وتسمية العرب خبزة الإبل","scope_en":"A plant called ṣiliyān, with a large head or spike, grazed by camels and called camel bread."},"support_links":["sup_3e0da71c75f0136e8c64"]},{"boundary":"The plant named ضريع, including dry shibrq or the red foul-smelling plant in one report","branch_kind":null,"branch_ref":"root_000908/B005","candidate_links":[{"candidate_id":"cand_c99e1b0c8e7bc09cf0ea","lane":"macro"}],"focus_root_occurrences":[],"gloss":"the plant called dari","lexicon_identity_status":null,"registry":"nominated","review_facets":[{"facet_id":"SOURCE_IMAGE","role":"source_semantic_image","source_fields":["image_ar","image_en"],"statements":{"image_ar":"نبات الضريع","image_en":"the plant called dari"}}],"root_ar":"ض ر ع","root_id":"root_000908","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"image_ar":"نبات الضريع","image_en":"the plant called dari","scope_ar":"النبات المسمى الضريع؛ يبيس الشبرق؛ النبات الأحمر المنتن المذكور في بعض الأقوال","scope_en":"The plant named ضريع, including dry shibrq or the red foul-smelling plant in one report"},"support_links":["sup_3e0da71c75f0136e8c64"]},{"boundary":"Dal yalnızca kulpsuz ya da kulaksız içme kabını kapsar; çalgı, oyun, içme eylemi ve beden özelliği anlamlarını kapsamaz.","branch_kind":"bare","branch_ref":"root_001328/B001","candidate_links":[{"candidate_id":"cand_0e07f1c4f266a0d6604c","lane":"macro"},{"candidate_id":"cand_71ed65cf10ddd214eaab","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"kulpsuz içme kabı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir içeceğin konduğu ve içildiği kap türüdür."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kabın tutma kulpu ya da yan kulağı bulunmaz."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kap, bardak, testi veya dökme kabı türleriyle açıklanabilir; bir anlatım yuvarlak başlı oluşunu da belirtir."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın içme kabı olma işlevini ve kulp ya da kulak taşımama sınırını birlikte veren genel karşılıktır.","boundary_detail":"Dal yalnızca kulpsuz ya da kulaksız içme kabını kapsar; çalgı, oyun, içme eylemi ve beden özelliği anlamlarını kapsamaz.","branch_image_ar":"الكوب بلا عروة","concept_gloss":"kulpsuz içme kabı","contextual_glosses":[{"applicability":"Kabın özellikle bardak türünde düşünüldüğü bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Testi veya dökme kabı olarak açıklanan öteki kap görünümlerini dışarıda bırakır.","preserves":"İçme kabı olmayı ve kulpsuzluk özelliğini korur."},"facet_ids":["F001","F002","F003"],"text":"kulpsuz bardak","usage_role":"contextual"},{"applicability":"Yuvarlak başlı ve yan kulağı bulunmayan kap betiminin öne çıktığı özel bağlamda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yuvarlak başlılık belirtmeyen genel kulpsuz içme kabı kapsamını daraltır.","preserves":"Kulaksız olma sınırını ve kap niteliğini korur."},"facet_ids":["F001","F002","F003"],"text":"kulaksız yuvarlak kap","usage_role":"explanatory"}],"definition":"İçecek koymak ve içmek için kullanılan, kulpu ya da kulağı bulunmayan kaptır. Kaynaklarda kap türü değişik biçimlerde açıklansa da kulpsuzluk ortak sınırdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir içeceğin konduğu ve içildiği kap türüdür."},{"facet_id":"F002","role":"core","statement":"Kabın tutma kulpu ya da yan kulağı bulunmaz."},{"facet_id":"F003","role":"source_variant","statement":"Kap, bardak, testi veya dökme kabı türleriyle açıklanabilir; bir anlatım yuvarlak başlı oluşunu da belirtir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kulplu bardakları da kapsayabildiği için dalın kulpsuzluk sınırını aşar.","collision":null,"fit":"broadening","loses":null,"preserves":"İçecek koymaya ve içmeye yarayan kap olma yönünü korur."},"text":"bardak"}],"identity_rationale":"Kaynak ifadesi, bu dalı kulpu ya da kulağı bulunmayan bir içme kabı olarak açıkça sınırlar. Kap türüne ilişkin bardak, testi ve dökme kabı gibi anlatımlar ile yuvarlak başlı olma ayrıntısı, aynı kulpsuz kap çekirdeğinin değişik kaynak görünümleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"kulpu ya da kulağı olmayan içme kabı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kulpu ya da kulağı olmayan içme kapları"}],"lexicalization_note":"Tanım yalın biçimin kap anlamıyla sınırlıdır ve başka dallardaki eylem ya da özel kullanım anlamlarını bu dala taşımaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; kulpsuzluk, içerikle adlandırma ve ölçme işlevi sınırlarını en açık gösteren üç karşılaştırma seçildi. Öteki adaylar yalnız genel kap alanını paylaştığı veya bu dalın eşsesli diğer anlamları olduğu için ayrıca yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalında kulpsuzluk tanımın kurucu sınırıdır; komşu dalda bu biçim şartı yoktur ve kapsam ölçü işlevi ile o kaptan içme eylemine uzanabilir.","focus_only":"Bu dal, içme kabının kulpu ya da kulağı bulunmamasını zorunlu kılar.","gloss":"bardak ve ölçü kabı","neighbor_only":"Komşu dal, kabı belirli bir topluluğun bardağı veya bir ölçü kabı olarak ele alır ve onunla içme eylemine de uzanır.","neighbor_ref":"root_001130/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da içmek için kullanılan kapları adlandırır."},{"boundary_match":"partial","distinction":"Odak dalı biçimsel olarak kulpsuz bir kabı adlandırır; komşu dalın sınırı ise kap ile içeriğinin birlikte veya birbirinin yerine anılmasına dayanır.","focus_only":"Kulpu ya da kulağı olmayan kabın kendisini gösterir.","gloss":"içeceğiyle birlikte kap","neighbor_only":"Kabın içindeki içecekle birlikte düşünülmesine, yalnız kaba veya yalnız içeceğe aktarılmasına izin verir.","neighbor_ref":"root_001277/B001","relation_type":"near_neighbor","shared_zone":"İki dal da içecek sunmaya yarayan bir kap çevresinde buluşur."},{"boundary_match":"partial","distinction":"Odak dalının ayırıcı yanı kulpsuzluk iken komşu dalın ayırıcı yanı ölçü kabı olarak da iş görmesi ve ölçü değeridir.","focus_only":"İçme amacı ve kulpsuzluk birlikte zorunludur.","gloss":"içme ve ölçme kabı","neighbor_only":"Komşu kap hem içme hem ölçme işlevi görebilir ve belirli bir ölçü değerine bağlanır.","neighbor_ref":"root_000892/B004","relation_type":"near_neighbor","shared_zone":"Her ikisi de içmede kullanılabilen kap türleridir."}],"source_phrase_ar":"الكوب القدح لا عروة له (maqayis;mufradat)؛ الكوب كوز لا عروة له (ayn;sihah)؛ الكوب الإبريق بلا عروة (jamhara)؛ الكوب الكوز المستدير الرأس الذي لا أذن له (tahdhib)","source_summary":"Kaynaklar kulpu ya da kulağı olmayan içme kabı çekirdeğinde birleşir. Kabın bardak, testi veya dökme kabı olarak betimlenmesi ve yuvarlak başlılık ayrıntısı, ortak sınırı değiştirmeyen anlatım çeşitleridir.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"الكوب والقدح والكوز والإبريق إذا كان إناء للشرب بلا عروة أو بلا أذن","what_is_not_ar":"ليس الكوبة الطبل ولا الشطرنجة ولا الشرب بالكوب ولا دقة العنق وعظم الرأس"},"support_links":["sup_80286e18a4bac3c6cffb","sup_bb11170b199d1277b9b3"]},{"boundary":"Dal, birbirine alternatif çalgı türlerini kapsayan bir adlandırmadır; bütün özellikleri aynı araçta birleştirmez.","branch_kind":"bare","branch_ref":"root_001328/B002","candidate_links":[{"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Eğlence amacıyla çalınan bir araçtır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Vurmalı çalgı görünümü davul ya da küçük ve ortası dar bir davuldur."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir görünüm, uzun saplı telli bir çalgıdır."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Üflemeli görünüm, bir deri parçasına birleştirilen ve içine üflenen borulardan oluşur."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alternatif araç türlerini tek bir birleşik yapı gibi göstermeden dalın bütün kaynak kapsamını veren açıklayıcı karşılıktır.","boundary_detail":"Dal, birbirine alternatif çalgı türlerini kapsayan bir adlandırmadır; bütün özellikleri aynı araçta birleştirmez.","branch_image_ar":"الكوبة آلة لهو","concept_gloss":"davul, uzun saplı telli çalgı veya deriye geçirilmiş üfleme borularından oluşan eğlence çalgısı","contextual_glosses":[{"applicability":"Vurmalı çalgı görünümünün söz konusu olduğu bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Uzun saplı telli çalgı ile deriye birleştirilmiş üfleme boruları görünümlerini dışarıda bırakır.","preserves":"Eğlence için çalınan vurmalı araç görünümünü korur."},"facet_ids":["F001","F002"],"text":"davul","usage_role":"contextual"},{"applicability":"Telli araç görünümünün açıkça kastedildiği bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davul ve deriye birleştirilmiş üfleme boruları görünümlerini dışarıda bırakır.","preserves":"Eğlence çalgısı olmayı ve telli araç görünümünü korur."},"facet_ids":["F001","F003"],"text":"uzun saplı telli çalgı","usage_role":"contextual"},{"applicability":"Deri parçasında birleştirilen boruların üflenerek çalındığı araç görünümünü açıklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Davul ve uzun saplı telli çalgı görünümlerini dışarıda bırakır.","preserves":"Üfleme borularını, deri içinde birleşmelerini ve çalınma biçimini korur."},"facet_ids":["F001","F004"],"text":"deriye geçirilmiş üfleme boruları","usage_role":"explanatory"}],"definition":"Eğlence amacıyla çalınan bir çalgıyı adlandırır. Kaynaklara göre bu çalgı bir davul, küçük ve ortası dar bir davul, uzun saplı telli bir çalgı veya deriye birleştirilmiş ve üflenerek çalınan borular olabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Eğlence amacıyla çalınan bir araçtır."},{"facet_id":"F002","role":"source_variant","statement":"Vurmalı çalgı görünümü davul ya da küçük ve ortası dar bir davuldur."},{"facet_id":"F003","role":"source_variant","statement":"Başka bir görünüm, uzun saplı telli bir çalgıdır."},{"facet_id":"F004","role":"source_variant","statement":"Üflemeli görünüm, bir deri parçasına birleştirilen ve içine üflenen borulardan oluşur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Eğlence amacıyla ilişkilendirilmeyen ve kaynakta verilen türlerden olmayan bütün çalgıları da kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Çalınan bir araç olma yönünü korur."},"text":"çalgı"}],"identity_rationale":"Kaynak ifadesi bu adı eğlence için çalınan bir araçla ilişkilendirir; ancak tek bir araç yapısı vermez. Davul ve küçük, ortası dar davul anlatımlarının yanında uzun saplı telli bir çalgı ile deriye birleştirilmiş üfleme boruları da yer alır. Bu nedenle dal korunabilir, fakat bu araçların özellikleri tek bir birleşik çalgının parçaları gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"davul veya küçük, ortası dar davul"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"uzun saplı telli çalgı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"deri parçasına birleştirilip üflenerek çalınan borular"}],"lexicalization_note":"Tanım yalın biçimin çalgı anlamını verir; belirli bir araç türünü bütün dalın tek anlamı saymaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; davul, telli çalgı ve üfleme boruları görünümlerinin sınırlarını keskinleştiren üç aday seçildi. Ses, deri ve şarkı alanındaki öteki adaylar aracın kendisiyle yeterli anlam örtüşmesi taşımadığından yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal tek yüzlü belirli bir davula bağlıdır; odak dalında davul yalnızca alternatiflerden biridir ve tek yüzlülük koşulu bulunmaz.","focus_only":"Davul dışında uzun saplı telli çalgı ve deriye birleştirilmiş üfleme boruları görünümlerini de kapsar.","gloss":"tek yüzlü davul","neighbor_only":"Belirli olarak tek yüzlü bir davul türünü gösterir.","neighbor_ref":"root_001281/B012","relation_type":"near_synonym","shared_zone":"İki dal da bir davul türünü adlandırabildiği ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalındaki üflemeli araç birden çok borunun deride birleşmesiyle tanımlanır; komşu dal tek kamıştan yapılan çoban aracıdır.","focus_only":"Bir deri parçasında birleştirilmiş birden çok üfleme borusu görünümünü içerir ve başka çalgı türlerine de uzanır.","gloss":"çoban borusu","neighbor_only":"Çobanın üflediği tek bir kamış boru türünü gösterir.","neighbor_ref":"root_001586/B010","relation_type":"near_neighbor","shared_zone":"Her iki dalın bir görünümünde üflenerek çalınan boru biçimli araç vardır."},{"boundary_match":"partial","distinction":"Odak dalındaki telli görünüm daha genel bir uzun saplı çalgıdır ve dal başka araç türlerini de kapsar; komşu dal belirli bir telli aracın vurularak çalınmasına bağlıdır.","focus_only":"Vurmalı ve üflemeli araçlara da uzanan birden çok alternatif çalgı görünümü vardır.","gloss":"vurularak çalınan telli çalgı","neighbor_only":"Vurularak çalınan belirli bir telli çalgıyı gösterir.","neighbor_ref":"root_000650/B006","relation_type":"near_neighbor","shared_zone":"İki dal da telli bir çalgıyı gösterebilir."}],"source_phrase_ar":"الكوبة الطبل للعب (maqayis)؛ الكوبة الطبل الذي يلعب به (mufradat)؛ الكوبة الطبل (jamhara)؛ الطبل والطنبور (jamhara)؛ الكوبة الطبل الصغير المخصر (sihah)؛ الكوبة قصبات تجمع في قطعة أديم ويزمر فيها (ayn)","source_summary":"Kanıt, eğlence için çalınan araç çekirdeğini ortaklaştırırken aracın türünü değişik biçimlerde verir: davul ve küçük, ortası dar davul; uzun saplı telli çalgı; deriye birleştirilmiş üfleme boruları. Bunlar tek bir aracın birleşik özellikleri değil, adın alternatif göndergeleridir.","sources":["MQ","AY","JA","SI","MU"],"what_is_ar":"الكوبة للطبل والطبل الصغير المخصر والطبل الذي يلعب به والطنبور والقصبات المجموعة في أديم يزمر فيها","what_is_not_ar":"ليس الكوب إناء الشرب ولا الشطرنجة ولا إلصاق بعض الشيء ببعض"},"support_links":["sup_aad66371219c89c7e1ab"]},{"boundary":"Dal yalnızca satranç oyununu adlandırır; aynı biçimle ilişkilendirilen çalgı anlamı bu dalın dışında kalır.","branch_kind":"bare","branch_ref":"root_001328/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"satranç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bir tahta oyunu olan satrancı adlandırır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakta verilen belirli oyunun Türkçedeki doğal ve eksiksiz adıdır.","boundary_detail":"Dal yalnızca satranç oyununu adlandırır; aynı biçimle ilişkilendirilen çalgı anlamı bu dalın dışında kalır.","branch_image_ar":"الكوبة الشطرنجة","concept_gloss":"satranç","contextual_glosses":[{"applicability":"Oyun niteliğinin açıkça belirtilmesinin yararlı olduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Oyunun kimliğini ve oyun türünde oluşunu açıkça korur."},"facet_ids":["F001"],"text":"satranç oyunu","usage_role":"explanatory"}],"definition":"Karşılıklı oyuncuların taşları kurallı biçimde hareket ettirdiği satranç adlı tahta oyununu adlandıran kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bir tahta oyunu olan satrancı adlandırır."}],"identity_rationale":"Kaynak ifadesi bu biçimi doğrudan satranç oyunuyla özdeşleştirir. Provisional dal çerçevesi bu açık oyun adını doğru yansıtır ve başka bir araç, kap veya eylem anlamını içeri almaz.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"satranç"}],"lexicalization_note":"Tanım yalın biçimin oyun adını verir ve aynı söz biçiminin başka dallardaki anlamlarını buna katmaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi. Adayların hiçbiri satrançla ikame edilebilir bir anlam ya da dal sınırını açıklayan yeterli bir örtüşme sunmadığı için komşu ayrımı yayımlanmadı; aynı söz biçiminin öteki anlamları yalnız eşseslidir.","source_phrase_ar":"الكوبة الشطرنجة (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, bu biçimin satranç oyununu adlandırdığını bildirir."}],"source_summary":"Bu dal için kanıt tek bir açık oyun anlamı verir ve kap, çalgı ya da eylem anlamlarına ilişkin bir genişleme bildirmez.","sources":["AY"],"what_is_ar":"الكوبة إذا أريد بها الشطرنجة","what_is_not_ar":"ليس الكوب إناء الشرب ولا الكوبة الطبل والطنبور والقصبات"},"support_links":[]},{"boundary":"Anlam, parçaları birbirinin üzerine getirip yapıştıran özel söyleyişle sınırlıdır; genel toplama veya bağlama anlamı değildir.","branch_kind":"non_bare","branch_ref":"root_001328/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"üst üste getirip yapıştırmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bazı parçalar başka parçaların üzerine getirilir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst üste getirilen parçalar birbirine yapıştırılır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Parçaların hem konum ilişkisini hem de yapışma sonucunu birlikte veren tam karşılıktır.","boundary_detail":"Anlam, parçaları birbirinin üzerine getirip yapıştıran özel söyleyişle sınırlıdır; genel toplama veya bağlama anlamı değildir.","branch_image_ar":"كُوب بعضه على بعض","concept_gloss":"üst üste getirip yapıştırmak","contextual_glosses":[{"applicability":"Nesne parçalarının karşılıklı konumu bağlamdan belli olduğunda doğal bir eylem karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Parçaların birbirinin üzerinde olmasını ve yapışmasını birlikte korur."},"facet_ids":["F001","F002"],"text":"birbirinin üzerine yapıştırmak","usage_role":"contextual"}],"definition":"Bir şeyin bazı parçalarını öteki parçaların üzerine getirerek birbirine yapıştırmaktır. Üst üste yerleştirme ilişkisi ve parçaların tutunması birlikte kurucudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bazı parçalar başka parçaların üzerine getirilir."},{"facet_id":"F002","role":"core","statement":"Üst üste getirilen parçalar birbirine yapıştırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Üst üste getirme ve yapıştırma bulunmayan her türlü birleştirmeyi de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"Ayrı parçalar arasında bağlantı kurulması yönünü korur."},"text":"birleştirmek"}],"identity_rationale":"Kaynak ifadesi, bazı parçaların birbirinin üzerine getirilerek birbirine yapıştırılmasını bildirir. Dal çerçevesi hem parçalar arasındaki üst üste gelme ilişkisini hem de bunun sonucundaki yapışmayı korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"parçalarını birbirinin üzerine getirip yapıştırmak"}],"lexicalization_note":"Tanım yalnızca parçaların birbirinin üzerine getirilmesini belirten tedarikli söyleyişe bağlıdır ve bunu yalın kökün genel anlamına dönüştürmez.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; genel bağlantı, yana yapıştırma ve toplama anlamlarıyla kurulan üç karşılaştırma dalın konum ve sonuç sınırını yeterince gösterir. Öteki adaylar bu ayrımları tekrar ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı üst üste konmuş parçaların yapıştırılmasına bağlıdır; komşu dal konum ve yapıştırma şartı olmadan çok daha genel bağlantı ve birleşmeyi kapsar.","focus_only":"Parçaların birbirinin üzerine getirilmesi ve yapışması birlikte zorunludur.","gloss":"bağlamak ve birleştirmek","neighbor_only":"Somut ve soyut şeyler arasında genel bağlantı, süreklilik veya birleşme kurulmasına uzanır.","neighbor_ref":"root_001655/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ayrı şeylerin birbirine tutunması veya bağlanması sonucunu içerebilir."},{"boundary_match":"partial","distinction":"Odak dalının konum sınırı parçaların üst üste gelmesidir; komşu dalda yapışma özellikle yan tarafa yönelir.","focus_only":"Bir şeyin parçalarını birbirinin üzerine getirerek yapıştırır.","gloss":"yana yapıştırmak","neighbor_only":"Bir şeyi özellikle yana yapıştırmayı ve bu yana çekip yakın tutmayı anlatır.","neighbor_ref":"root_001356/B005","relation_type":"near_synonym","shared_zone":"İki dal da bir şeyi başka bir yüzeye yapıştırma eyleminde örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği genel toplama ve eklemedir; odak dalı ise bu işlemin üst üste konum ve yapışma yoluyla yapılmasına bağlıdır.","focus_only":"Üst üste getirme ve yapıştırarak tutturma sonucunu şart koşar.","gloss":"toplamak ve eklemek","neighbor_only":"Toplama, bir araya getirme, dikme ve çeşitli kapatma eylemlerine kadar uzanır.","neighbor_ref":"root_001283/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda ayrı parçalar bir araya getirilebilir."}],"source_phrase_ar":"بعضها كُوب على بعض أي ألزق (ayn)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, parçaları birbirinin üzerine getirip yapıştırma eylemini bildirir."}],"source_summary":"Kanıt, parçaların yalnız yan yana toplanmasını değil, birbirinin üzerine getirilip birbirine yapıştırılmasını anlatan sınırlı bir eylem anlamı verir.","sources":["AY"],"what_is_ar":"ما كان بمعنى ألصق بعضه على بعض","what_is_not_ar":"ليس الكوب إناء الشرب ولا الكوبة آلة اللهو"},"support_links":[]},{"boundary":"Dal kabın kendisini değil, o kap kullanılarak gerçekleştirilen içme eylemini gösterir.","branch_kind":"bare","branch_ref":"root_001328/B005","candidate_links":[{"candidate_id":"cand_0e07f1c4f266a0d6604c","lane":"macro"},{"candidate_id":"cand_21ab6f111adc25e1acf7","lane":"macro"},{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"kulpsuz içme kabından içmek","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir içeceği içme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İçme eylemi kulpsuz bir içme kabı kullanılarak yapılır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İçme eylemini ve bu eylemde kullanılan özel kap türünü birlikte veren karşılıktır.","boundary_detail":"Dal kabın kendisini değil, o kap kullanılarak gerçekleştirilen içme eylemini gösterir.","branch_image_ar":"الشرب بالكوب","concept_gloss":"kulpsuz içme kabından içmek","contextual_glosses":[{"applicability":"Söz konusu kabın içme kabı olduğu bağlamdan açıkça anlaşıldığında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İçme eylemini ve kulpsuz kabın kullanımını korur."},"facet_ids":["F001","F002"],"text":"kulpsuz kaptan içmek","usage_role":"contextual"}],"definition":"Bir içeceği kulpu bulunmayan içme kabını kullanarak içmektir. İçme eylemi çekirdek, kullanılan kap ise eylemi sınırlandıran araçtır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir içeceği içme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"İçme eylemi kulpsuz bir içme kabı kullanılarak yapılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Kulpsuz içme kabı dışında başka yollarla gerçekleştirilen bütün içme eylemlerini de kapsar.","collision":null,"fit":"broadening","loses":null,"preserves":"İçeceği alma eylemini korur."},"text":"içmek"}],"identity_rationale":"Kaynak ifadesi eylemi, içeceği belirli türde bir içme kabı kullanarak içmek biçiminde açıklar. Dal çerçevesi kabın kendisiyle içme eylemini birbirine karıştırmadan araç koşulunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kulpsuz içme kabından içmek"}],"lexicalization_note":"Tanım yalın eylem biçiminin kap kullanarak içme anlamını verir; kap adını eylemin yerine geçirmez.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; aşırı içme, sabah içme ve kullanılan kabın kendisiyle yapılan karşılaştırmalar araç koşulunu en açık biçimde ayırır. Yutma, yudum ve başka kap adları aynı sınırı daha az doğrudan gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı miktar veya doyma bildirmez, yalnız aracı belirler; komşu dal kullanılan kaptan bağımsız olarak aşırılık ve doymama bildirir.","focus_only":"İçme eylemini kullanılan kulpsuz kapla sınırlar.","gloss":"çok içip doymamak","neighbor_only":"Çok içme, doymama ve aralıklarla içmeyi sürdürme koşullarını taşır.","neighbor_ref":"root_000717/B005","relation_type":"near_neighbor","shared_zone":"Her iki dalın çekirdeğinde bir içeceği içme eylemi vardır."},{"boundary_match":"partial","distinction":"Odak dalındaki koşul kullanılan kap, komşu daldaki koşul ise günün sabah vaktidir; komşu ayrıca yeme ve sunmaya uzanır.","focus_only":"İçmeyi kulpsuz bir kabın kullanımına bağlar.","gloss":"sabah içmek","neighbor_only":"İçme, yeme veya sunma eylemini sabah vaktine bağlar.","neighbor_ref":"root_000839/B003","relation_type":"near_neighbor","shared_zone":"İki dal da belirli bir koşulla sınırlandırılmış içme eylemini içerebilir."},{"boundary_match":"thematic_only","distinction":"Odak dalı bir içme eylemidir; komşu dal ise o eylemde araç olabilen nesnedir, bu nedenle birbirlerinin yerine kullanılamazlar.","focus_only":"Kulpsuz kabı kullanarak yapılan eylemi gösterir.","gloss":"kulpsuz içme kabı","neighbor_only":"Eylemde kullanılan kulpsuz içme kabının kendisini gösterir.","neighbor_ref":"root_001328/B001","relation_type":"thematic","shared_zone":"Aynı içme olayında biri eylemi, öteki kullanılan aracı adlandırır."}],"source_phrase_ar":"كاب يكوب إذا شرب بالكوب (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, eylemi kulpsuz içme kabını kullanarak içmek biçiminde açıklar."}],"source_summary":"Kanıt, genel içme eylemini kullanılan araç bakımından sınırlar: içecek, kulpsuz bir içme kabı aracılığıyla içilir.","sources":["TA"],"what_is_ar":"الفعل كاب يكوب إذا شرب بالكوب","what_is_not_ar":"ليس الكوب نفس إناء الشرب ولا الكوبة آلة اللهو"},"support_links":["sup_80286e18a4bac3c6cffb","sup_b336ca74d7f3a9612e27","sup_bb4f38c1e59003f7f1e8"]},{"boundary":"Dal, ince boyun ve büyük baş özelliklerinin birleşimidir; boynun yalnız uzun, eğik veya uzatılmış olması yeterli değildir.","branch_kind":"bare","branch_ref":"root_001328/B006","candidate_links":[{"candidate_id":"cand_223d5984fe02c0e63dca","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","surface_ar":"أَكْوَابٌ"}],"gloss":"ince boyunluluk ve iri başlılık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Boyun ince yapıdadır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Baş büyük yapıdadır."}}],"root_ar":"ك و ب","root_id":"root_001328","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Birleşik beden özelliğinin iki zorunlu parçasını da açıkça veren genel karşılıktır.","boundary_detail":"Dal, ince boyun ve büyük baş özelliklerinin birleşimidir; boynun yalnız uzun, eğik veya uzatılmış olması yeterli değildir.","branch_image_ar":"دقة العنق وعظم الرأس","concept_gloss":"ince boyunluluk ve iri başlılık","contextual_glosses":[{"applicability":"Beden görünümünün tam bir söz öbeğiyle açıklanmasının gerektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnce boyun ve iri baş özelliklerini birlikte korur."},"facet_ids":["F001","F002"],"text":"ince boyunlu ve iri başlı olma","usage_role":"explanatory"}],"definition":"Boynun ince, başın ise büyük olmasıyla oluşan birleşik beden yapısıdır. Her iki oransal özellik de tanımın zorunlu parçasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Boyun ince yapıdadır."},{"facet_id":"F002","role":"core","statement":"Baş büyük yapıdadır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başın büyük olması biçimindeki ikinci zorunlu özelliği düşürür.","preserves":"Boynun ince olması özelliğini korur."},"text":"ince boyunluluk"}],"identity_rationale":"Kaynak ifadesi boynun inceliği ile başın büyüklüğünü birlikte veren bir beden özelliğini açıkça bildirir. Dal çerçevesi iki özelliği de korur ve yalnız boyun inceliğine ya da yalnız baş büyüklüğüne indirgemez.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"boynun inceliği ve başın büyüklüğü"}],"lexicalization_note":"Tanım yalın biçimin birleşik beden özelliğini verir ve boyunla ilgili başka hareket ya da biçim anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün komşu adayları değerlendirildi; boyun uzunluğu ve genel beden inceliğiyle ilgili üç aday, odak dalındaki ince boyun ile büyük baş birleşimini en iyi sınırlar. Boyun hareketi, boyun yanı ve kısa boy gibi adaylar daha uzak kaldığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dalı incelik ve büyük baş oranına dayanır; komşu dal uzunluk, uzatma ve yükseltmeye dayanır, dolayısıyla iki betim birbirinin yerine geçmez.","focus_only":"İnce boyunla birlikte büyük baş özelliğini zorunlu kılar.","gloss":"uzun ve uzatılmış boyun","neighbor_only":"Boynun uzunluğu, uzatılması veya başın yukarı kaldırılması özelliklerini içerir.","neighbor_ref":"root_000706/B002","relation_type":"same_field","shared_zone":"Her iki dal da boynun görünüşüne ilişkin bir beden özelliğini anlatır."},{"boundary_match":"field_only","distinction":"Odak dalında uzunluk şartı yoktur ve büyük baş zorunludur; komşu dal uzunluğu öne çıkarır ve baş büyüklüğü bildirmez.","focus_only":"Boynun inceliğini başın büyüklüğüyle birlikte betimler.","gloss":"uzun kişi veya uzun boyun","neighbor_only":"Kişinin veya boynun uzun olmasını betimler.","neighbor_ref":"root_001405/B007","relation_type":"same_field","shared_zone":"İki dal da kişinin boyun ve beden oranlarıyla ilgili görünüşünü betimler."},{"boundary_match":"field_only","distinction":"Odak dalı iki belirli beden bölümünün karşıt oranını tanımlar; komşu dal bütün bedenin ince ve sıkı yapısını anlatır.","focus_only":"İnce boyun ile büyük baş arasındaki özel oranı gösterir.","gloss":"ince ve sıkı yapılı beden","neighbor_only":"Bedenin bütünüyle sıkı, kıvrak veya ip gibi ince görünmesini gösterir.","neighbor_ref":"root_001422/B002","relation_type":"same_field","shared_zone":"Her iki dal insan bedeninin ince veya narin görünümüyle ilişkilidir."}],"source_phrase_ar":"الكَوَب دقة العنق وعظم الرأس (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek kaynak, ince boyun ile büyük başın birlikte bulunduğu beden özelliğini bildirir."}],"source_summary":"Kanıt, boyun inceliği ile baş büyüklüğünü tek bir birleşik beden betimi içinde verir; iki özellikten biri çıkarıldığında dalın anlamı eksik kalır.","sources":["TA"],"what_is_ar":"الكَوَب في وصف دقة العنق وعظم الرأس","what_is_not_ar":"ليس الكوب إناء الشرب ولا الفعل كاب يكوب في الشرب"},"support_links":["sup_80c7c66001a3ef24eccb"]},{"boundary":"Çekirdek, nesneyi yerine indirme ve konduğu yerle sınırlıdır; kalıp kullanımlar ayrı render edilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B001","candidate_links":[{"candidate_id":"cand_0e07f1c4f266a0d6604c","lane":"macro"},{"candidate_id":"cand_e0b5962eda40aa011b0c","lane":"macro"},{"candidate_id":"cand_21ab6f111adc25e1acf7","lane":"macro"},{"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"bir şeyi indirip yerine koyma; konduğu yer","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesne kaldırmanın karşıtı olarak aşağı indirilir ya da elden bırakılıp yerine konur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem alanından nesnenin konduğu yer veya konum adı gelişir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kanıt, kimi yerde indirmeyi öne çıkarır, kimi yerde daha geniş bir yerine koyma işini kapsar."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın dal için nesnenin indirilip belirli yere konmasını ve bundan çıkan yer adını kapsar.","boundary_detail":"Çekirdek, nesneyi yerine indirme ve konduğu yerle sınırlıdır; kalıp kullanımlar ayrı render edilir.","concept_gloss":"bir şeyi indirip yerine koyma; konduğu yer","contextual_glosses":[{"applicability":"Nesnenin elden bırakılıp veya indirilip belirli bir yere konduğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Nesneye yapılan koyma işini korur."},"facet_ids":["F001"],"text":"yerine koymak","usage_role":"contextual"},{"applicability":"Eylemin sonucunda ortaya çıkan yer veya konum adı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yer adını ve konma ilişkisini korur."},"facet_ids":["F002"],"text":"konduğu yer","usage_role":"contextual"}],"definition":"Bir şeyi eldeki ya da yüksek konumdan indirip belirli bir yere koyma; aynı alan, nesnenin konduğu yeri de adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesne kaldırmanın karşıtı olarak aşağı indirilir ya da elden bırakılıp yerine konur."},{"facet_id":"F002","role":"extension","statement":"Eylem alanından nesnenin konduğu yer veya konum adı gelişir."},{"facet_id":"F003","role":"source_variant","statement":"Kanıt, kimi yerde indirmeyi öne çıkarır, kimi yerde daha geniş bir yerine koyma işini kapsar."}],"identity_rationale":"Kaynak ifadesi bu dalın çekirdeğini bir şeyi aşağı indirme, elden bırakma ya da kaldırmanın karşıtı olarak yerine koyma anlamında kurar. Yapı kurma ve kayıt ortaya çıkarma gibi kullanımlar ancak ayrı kalıplar olarak korunmalıdır; yalın dalın genel anlamı bunlara genişletilmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi yerine koymak veya elden bırakmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yer, konum"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yerine konmuş şey"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ev yapmak veya kurmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yazılı kayıtları ortaya çıkarmak"}],"lexicalization_note":"mixed_non_bare olduğu için yalın koyma ve yer anlamı, kalıp bağlı yapı kurma ya da kayıt gösterme kullanımlarından ayrı tutulur.","neighbor_coverage_note":"Listelenen adayların tamamı değerlendirildi; yayımlananlar okuyucunun en kolay karıştırabileceği dikey hareket, sabitlenme ve deve boynu alçaltma sınırlarını gösterir.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalda hareket aşağıya veya belirlenmiş yere doğrudur; komşuda hareket yukarıya ve yükseltmeye doğrudur.","focus_only":"Odak dal nesneyi aşağı indirip yerine koyar.","gloss":"indirme ile yükseltme","neighbor_only":"Komşu dal nesneyi yukarı kaldırma ve yüksek konuma çıkarma yönündedir.","neighbor_ref":"root_000582/B001","relation_type":"antonym","shared_zone":"İkisi de nesnenin dikey konumunu değiştirme alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici olan nesnenin konmasıdır; komşuda belirleyici olan nesnenin orada kalıcı biçimde tutunmasıdır.","focus_only":"Odak dal nesneyi bir yere koyma eylemini de içerir.","gloss":"koyma ile sabit kalma","neighbor_only":"Komşu dal yerinde sabit kalma, yapışma veya sağlamlaştırma sonucunu öne çıkarır.","neighbor_ref":"root_000562/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir yerle bağlantı kuran nesneyi düşünür."},{"boundary_match":"partial","distinction":"Odak dal genel yerleştirme anlamındadır; komşu dal yalnızca binicinin binmesini sağlayan hayvan duruşunu anlatır.","focus_only":"Odak dal her tür nesneyi yerine koyma ve konulan yeri kapsar.","gloss":"genel indirme ile binme için alçaltma","neighbor_only":"Komşu dal devenin başını veya boynunu binme amacıyla alçaltmasına bağlıdır.","neighbor_ref":"root_001657/B013","relation_type":"near_neighbor","shared_zone":"İkisi de aşağı yönlü bir hareketi kullanır."}],"source_summary":"Ortak kanıt, anlamı bir nesneyi aşağı indirme, elden bırakma veya kaldırmanın karşıtı olarak belirli bir yere koyma ekseninde toplar. Aynı kanıt bu eylemden konulan yer adının da çıktığını gösterir."},"support_links":["sup_80286e18a4bac3c6cffb","sup_aad66371219c89c7e1ab","sup_bb4f38c1e59003f7f1e8","sup_cfa66887abd9775cafcb"]},{"boundary":"Doğum çekirdektir; özel gebe kalma zamanı aynı dalda ayrı bir sınırlı facet olarak kalır.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"doğumla yükü bırakma ve özel gebe kalma zamanı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın çocuğunu veya taşıdığı gebelik yükünü doğumla bırakır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı malzeme, gebeliğin adetin hemen öncesindeki temizlik sonunda başlamasını özel olarak adlandırır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Doğum çekirdeğini ve adet döngüsü sınırındaki özel gebelik zamanı kullanımını birlikte temsil eder.","boundary_detail":"Doğum çekirdektir; özel gebe kalma zamanı aynı dalda ayrı bir sınırlı facet olarak kalır.","concept_gloss":"doğumla yükü bırakma ve özel gebe kalma zamanı","contextual_glosses":[{"applicability":"Kadın öznesinin çocuğunu dünyaya getirdiği gerçek doğum bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadın öznesi ve doğumla bırakma anlamını korur."},"facet_ids":["F001"],"text":"çocuğunu doğurmak","usage_role":"contextual"},{"applicability":"Gebeliğin temizlik süresinin sonunda ve adetin hemen öncesinde başladığını anlatan özel ad için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Döngü sınırındaki gebelik zamanı bilgisini korur."},"facet_ids":["F002"],"text":"adet öncesi gebelik başlangıcı","usage_role":"explanatory"}],"definition":"Kadının gebelik yükünü doğumla bırakmasını anlatır; ayrıca adetin hemen öncesindeki temizlik sonunda oluşan gebelik için özel bir ad kullanımını içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın çocuğunu veya taşıdığı gebelik yükünü doğumla bırakır."},{"facet_id":"F002","role":"specialization","statement":"Aynı malzeme, gebeliğin adetin hemen öncesindeki temizlik sonunda başlamasını özel olarak adlandırır."}],"identity_rationale":"Kaynak ifadesi kadının çocuğunu veya gebelik yükünü doğumla bırakmasını açıkça verir, fakat aynı dalda adetin hemen öncesindeki temizlik sonunda oluşan gebelik için özel bir kullanım da yer alır. Bu yüzden dal doğum olarak kullanılabilir, ancak gebelik zamanına ait yan kullanımı gizlenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kadının çocuğunu doğurması"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"adet öncesi temizlik sonunda gebe kalma"}],"lexicalization_note":"mixed_non_bare olduğu için kadınla kurulan doğum kalıbı ile yalın zaman adı birbirine karıştırılmaz.","neighbor_coverage_note":"Tüm adaylar kontrol edildi; yayımlanan ayrımlar doğum, doğum sancısı ve tamamlanmamış düşme sınırlarını özellikle netleştirir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Doğum bağlamında çok yakındırlar, fakat odak dalın özel zaman adı komşuda çekirdek değildir.","focus_only":"Odak dal doğumun yanında adet döngüsüne bağlı özel gebelik zamanı adını da taşır.","gloss":"doğum","neighbor_only":"Komşu dal doğum olayını ve doğum zamanının gelmesini daha genel biçimde kapsar.","neighbor_ref":"root_001683/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de çocuğun dünyaya gelmesi ve gebelikten çıkış alanındadır."},{"boundary_match":"partial","distinction":"Odak dal sonuçlanan doğumu veya gebelik zamanını adlandırır; komşu dal doğuma yaklaşan bedensel süreçleri adlandırır.","focus_only":"Odak dal doğumun gerçekleşmesini veya özel gebe kalma zamanını anlatır.","gloss":"doğum ile doğum sancısı","neighbor_only":"Komşu dal doğum sancısı, yakın doğum ve rahimdeki hareket alanındadır.","neighbor_ref":"root_001406/B002","relation_type":"near_neighbor","shared_zone":"İkisi de gebeliğin son evreleri ve doğum çevresindedir."},{"boundary_match":"partial","distinction":"Odak dal doğumu esas alır; komşu dal tamamlanmamış gebelikten düşme sınırına sahiptir.","focus_only":"Odak dal normal doğurma anlamını taşır.","gloss":"doğum ile düşük","neighbor_only":"Komşu dal tamamlanmadan düşen çocuk veya düşük olayına bağlıdır.","neighbor_ref":"root_000719/B004","relation_type":"near_neighbor","shared_zone":"İkisi de rahimdeki çocuğun anneden ayrılması alanındadır."}],"source_summary":"Ortak kanıt, kadın öznesiyle doğum yapma ve gebelik yükünü bırakma anlamını verir. Aynı toplu kanıt, gebeliğin belirli bir adet döngüsü sınırında başlamasıyla ilgili daha dar bir ad kullanımını da korur."},"support_links":[]},{"boundary":"Kapsam hayvan yürüyüşü ve onu hızlandırma ile sınırlıdır; genel acelecilik değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"hayvanın hızlı ya da özel yürüyüşle ilerlemesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hayvan veya binek yol içinde belirli bir yürüyüşle ilerler."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıtın bir kısmı yürüyüşü hızlı koşu, bir kısmı daha kolay ve alçak bir gidiş olarak sınırlar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Binici hayvanı bu yürüyüşe veya hıza zorlayabilir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan yürüyüşü, hızlandırma ve kaynaklarda görülen kolay gidiş sınırı için uygundur.","boundary_detail":"Kapsam hayvan yürüyüşü ve onu hızlandırma ile sınırlıdır; genel acelecilik değildir.","concept_gloss":"hayvanın hızlı ya da özel yürüyüşle ilerlemesi","contextual_glosses":[{"applicability":"Binek veya hayvanın hızlı yürüdüğü ya da koştuğu bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanın yol içinde hızlanmasını korur."},"facet_ids":["F001","F002"],"text":"hızla gitmek","usage_role":"contextual"},{"applicability":"Sürücü veya binici hayvanı bu gidişe sevk ettiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ettirgen katılımcıyı ve hızlandırma işini korur."},"facet_ids":["F003"],"text":"bineği hızlandırmak","usage_role":"contextual"}],"definition":"Binek ya da hayvanın yolda özel bir yürüyüşle hızlı veya rahat biçimde ilerlemesi; binici de onu bu gidişe sevk edebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hayvan veya binek yol içinde belirli bir yürüyüşle ilerler."},{"facet_id":"F002","role":"source_variant","statement":"Kanıtın bir kısmı yürüyüşü hızlı koşu, bir kısmı daha kolay ve alçak bir gidiş olarak sınırlar."},{"facet_id":"F003","role":"specialization","statement":"Binici hayvanı bu yürüyüşe veya hıza zorlayabilir."}],"identity_rationale":"Kaynak ifadesi hayvanın yolda hızlı gitmesini ve binicinin onu hızlandırmasını güçlü biçimde destekler; ancak bazı kanıtlar bunu sadece koşu değil, daha alçak veya kolay bir yürüyüş türü olarak da verir. Bu nedenle dal hız anlamıyla kullanılabilir, fakat her bağlamda en şiddetli koşu gibi okunmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bineğin hızlı gitmesi veya koşması"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"sürücünün bineği hızlandırması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bu yürüyüşü güzel olan"}],"lexicalization_note":"mixed_non_bare olduğu için hayvanın kendi yürüyüşü, binicinin hızlandırması ve kalıp halindeki yürüyüş niteliği ayrı tutulur.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar hız, koşu derecesi ve binek duruşu arasındaki başlıca sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hız bağlamında çok yakındırlar; odak dalın kaynak aralığı sadece yüksek hız değil, özel yürüyüş biçimini de içerir.","focus_only":"Odak dalda bazı kanıtlar daha kolay veya alçak yürüyüşü de korur.","gloss":"bineğin hızla gitmesi","neighbor_only":"Komşu dal bineklerde hızlı gidiş ve bu hıza sevk etmeyi daha genel biçimde kapsar.","neighbor_ref":"root_001628/B001","relation_type":"near_synonym","shared_zone":"İkisi de binek veya hayvanın yol içinde hızlanması alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal yürüyüş türü ve hızlandırma çevresindedir; komşu dal çok sert koşu derecesini adlandırır.","focus_only":"Odak dal hızla birlikte kolay veya düşük yürüyüş varyantını da taşıyabilir.","gloss":"özel gidiş ile sert koşu","neighbor_only":"Komşu dal devenin en şiddetli koşusu ve ayak vuruşu üzerine kuruludur.","neighbor_ref":"root_000536/B012","relation_type":"same_field","shared_zone":"Her ikisi de deve veya binek koşusu alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal yol içi gidişi anlatır; komşu dal binicinin üzerine çıkmasını sağlayan duruşu anlatır.","focus_only":"Odak dal hayvanın yolda ilerleyişidir.","gloss":"yürüme ile binmeye hazırlanma","neighbor_only":"Komşu dal hayvanın binilsin diye boynunu alçaltmasıdır.","neighbor_ref":"root_001657/B013","relation_type":"same_field","shared_zone":"İkisi de binek hayvanın hareket veya duruşuna bağlıdır."}],"source_summary":"Ortak kanıt, dalı hayvanın yolda belirli bir gidişle ilerlemesi ve kişinin onu bu gidişe sevk etmesi etrafında toplar. Toplu anlatımda hız, koşu ve daha kolay bir yürüyüş niteliği birlikte bulunduğundan tanım bu aralığı açık tutar."},"support_links":[]},{"boundary":"Dal ticaret ve sermaye eksilmesiyle sınırlıdır; sosyal düşüklük veya fiziksel koyma değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001657/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"ticarette zarar ve sermaye indirimi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ticaret yapan kişi zarar eder veya sermayesi beklenen tutarın altına düşer."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eksilen veya indirilen pay sermayeden düşülen tutar olarak adlandırılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinden fiyat veya alacakta indirim isteme kullanımı aynı eksiltme alanına bağlıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ticari zarar, sermayeden düşme ve indirim isteme alanlarını kapsar.","boundary_detail":"Dal ticaret ve sermaye eksilmesiyle sınırlıdır; sosyal düşüklük veya fiziksel koyma değildir.","concept_gloss":"ticarette zarar ve sermaye indirimi","contextual_glosses":[{"applicability":"Kişinin ticaretinde kardan değil kayıptan söz edildiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ticari kayıp sonucunu korur."},"facet_ids":["F001"],"text":"zarar etmek","usage_role":"contextual"},{"applicability":"Kayıp veya indirim tutarının sermaye üzerinden adlandırıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sermayeden eksilen tutarı korur."},"facet_ids":["F002"],"text":"sermayeden düşülen pay","usage_role":"explanatory"}],"definition":"Ticarette zarar etme ya da sermaye tutarından bir kısmın düşmesi; kişi karda değil eksilmede kalır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ticaret yapan kişi zarar eder veya sermayesi beklenen tutarın altına düşer."},{"facet_id":"F002","role":"specialization","statement":"Eksilen veya indirilen pay sermayeden düşülen tutar olarak adlandırılır."},{"facet_id":"F003","role":"associated_use","statement":"Birinden fiyat veya alacakta indirim isteme kullanımı aynı eksiltme alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi ticarette zarar etmeyi ve sermayeden düşülen kısmı aynı ekonomik düşüş alanında açıkça birleştirir. Provisional çerçeve sermaye kaybı, indirim ve zarar sınırlarını doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ticarette zarar etmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sermayeden düşülen indirim veya eksilti"}],"lexicalization_note":"mixed_non_bare olduğu için ticarette zarar etme kalıbı ile sermayeden düşülen pay adı ayrı ama aynı ekonomik alanda tutulur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlanan ayrımlar ticari zarar, genel eksilme ve kar karşıtlığı sınırlarını kapsar.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sınırları örtüşür; ikisi de ticari zarar ve sermaye eksiltisi alanında aynı çekirdeği verir.","focus_only":null,"gloss":"ticarette zarar","neighbor_only":null,"neighbor_ref":"root_000409/B002","relation_type":"synonym","shared_zone":"İkisi de ticarette sermaye veya satış sonucunda kardan değil kayıptan söz eder."},{"boundary_match":"partial","distinction":"Odak dal ticari zarar koşulunu ister; komşu dal bu koşul olmadan genel azalmayı anlatır.","focus_only":"Odak dal eksilmeyi özellikle ticaret ve sermaye bağlamına bağlar.","gloss":"sermaye kaybı ile genel eksilme","neighbor_only":"Komşu dal her tür azalmanın ve eksilmenin genel alanını kapsar.","neighbor_ref":"root_001542/B001","relation_type":"near_synonym","shared_zone":"İkisi de bir miktarın azalması anlamını paylaşır."},{"boundary_match":"opposed","distinction":"Odak dal negatif ekonomik sonuçtur; komşu dal pozitif artış veya kazanç yönünü taşır.","focus_only":"Odak dal ticarette kayıp ve sermaye düşmesini anlatır.","gloss":"zarar ile kar","neighbor_only":"Komşu dal alışverişte artış, ürün veya kar elde etme yönündedir.","neighbor_ref":"root_000533/B001","relation_type":"antonym","shared_zone":"İkisi de ticari sonuç ve sermaye hareketi alanındadır."}],"source_summary":"Ortak kanıt, dalı ticarette zarar etmek ve sermayeden düşülen eksilti olarak verir. Aynı toplu malzeme bu eksiltinin talep edilen indirim biçimine de uzandığını gösterir."},"support_links":[]},{"boundary":"Dal toplumsal ya da davranışsal alçalma alanındadır; para kaybı veya fiziksel yerleştirme değildir.","branch_kind":"bare","branch_ref":"root_001657/B005","candidate_links":[{"candidate_id":"cand_71ed65cf10ddd214eaab","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"düşük konum ve kendini alçaltma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi toplumsal konum veya soy bakımından düşük ve itibarsız görülür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kanıt, bu düşüklüğü yüksek veya soylu olmanın karşıtı olarak belirler."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kendini alçaltarak boyun eğme tavrı aynı anlam alanına bağlıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Toplumsal düşük sayılma ile davranışsal boyun eğme alanlarını birlikte kapsar.","boundary_detail":"Dal toplumsal ya da davranışsal alçalma alanındadır; para kaybı veya fiziksel yerleştirme değildir.","concept_gloss":"düşük konum ve kendini alçaltma","contextual_glosses":[{"applicability":"Kişinin soy, onur veya toplumdaki yeri bakımından aşağı sayıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplumsal düşük konum anlamını korur."},"facet_ids":["F001","F002"],"text":"düşük konumlu","usage_role":"contextual"},{"applicability":"Kişinin tavır olarak kendini aşağı çektiği veya boyun eğdiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Davranışsal alçalmayı ve boyun eğmeyi korur."},"facet_ids":["F003"],"text":"kendini alçaltarak boyun eğmek","usage_role":"explanatory"}],"definition":"Kişinin soy, konum veya davranış bakımından aşağı ve itibarsız sayılması; ayrıca kendini alçaltarak boyun eğme tavrını içerir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi toplumsal konum veya soy bakımından düşük ve itibarsız görülür."},{"facet_id":"F002","role":"source_variant","statement":"Kanıt, bu düşüklüğü yüksek veya soylu olmanın karşıtı olarak belirler."},{"facet_id":"F003","role":"extension","statement":"Kendini alçaltarak boyun eğme tavrı aynı anlam alanına bağlıdır."}],"identity_rationale":"Kaynak ifadesi kişiyi soyluluk veya yüksek konumun karşıtı olarak düşük ve itibarsız sayar; ayrıca kişinin kendini alçaltarak boyun eğmesini aynı düşüklük alanına bağlar. Provisional çerçeve sosyal konum ve alçalma ayrımını doğru taşır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"düşük konumlu kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"aşağı konum, düşüklük"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"kendini alçaltarak boyun eğme"}],"lexicalization_note":"bare olduğu için tanım yalın sosyal düşüklük ve kendini alçaltma alanında kalır; kalıp bağlı anlam içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar sosyal düşüklük, boyun eğme ve kibir karşıtlığındaki başlıca karışma alanlarını kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha çok kişinin konum veya soydaki düşüklüğünü adlandırır; komşu dal aşağı düşürme sürecini daha geniş tutar.","focus_only":"Odak dal kişinin düşük ve itibarsız sayılmasına ad olur.","gloss":"düşük konum","neighbor_only":"Komşu dal yüksek bir halden düşürülme, mal veya iyi durum kaybı gibi daha geniş bir alçalışı kapsar.","neighbor_ref":"root_001575/B002","relation_type":"near_synonym","shared_zone":"İkisi de insanın yüksek durumdan aşağı görülmesi alanındadır."},{"boundary_match":"partial","distinction":"Odak dal kişinin değer veya statüsündeki düşüklüğü korur; komşu dal daha çok huşu ve bedensel uysallıktır.","focus_only":"Odak dal sosyal itibarsızlık ve düşük konumu içerir.","gloss":"düşüklük ile boyun eğme","neighbor_only":"Komşu dal baş eğme, ses kısma ve organların sükuneti gibi boyun eğen beden tavrını öne çıkarır.","neighbor_ref":"root_000412/B001","relation_type":"near_neighbor","shared_zone":"İkisi de kendini aşağı çekme ve alçak durma alanına yaklaşır."},{"boundary_match":"opposed","distinction":"Odak dal aşağılık veya alçak duruşu anlatır; komşu dal üstünlük gösteren yükselişi anlatır.","focus_only":"Odak dal aşağı görülme ve kendini alçaltma yönündedir.","gloss":"alçalma ile kibirlenme","neighbor_only":"Komşu dal burnunu veya başını kaldırarak kibirlenme yönündedir.","neighbor_ref":"root_000817/B002","relation_type":"antonym","shared_zone":"İkisi de kişinin kendini toplum içinde nasıl konumladığıyla ilgilidir."}],"source_summary":"Ortak kanıt, dalı kişide düşük konum, soyluluk karşıtı olma ve itibarsızlık olarak toplar. Aynı kanıt kendini alçaltma ve boyun eğme tavrını da bu düşüklük alanına bağlar."},"support_links":["sup_bb11170b199d1277b9b3"]},{"boundary":"Dal, yerleştirilmiş topluluklar, kayıtlı askerler ve yüklerdir; ticari indirim anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001657/B006","candidate_links":[{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"},{"candidate_id":"cand_223d5984fe02c0e63dca","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"yerleştirilmiş topluluk, kayıtlı asker ya da yük","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir topluluk eski yerinden alınıp başka bir yerde oturtulur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Askerlerden oluşan bir grup belirli bir bölgenin kaydına bağlanabilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı ad alanında topluluğun taşıdığı ağır eşyalar da anılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer değiştirmiş topluluk, bölge kaydına bağlı asker ve topluluk yükü kullanımlarını kapsar.","boundary_detail":"Dal, yerleştirilmiş topluluklar, kayıtlı askerler ve yüklerdir; ticari indirim anlamı dışarıda kalır.","concept_gloss":"yerleştirilmiş topluluk, kayıtlı asker ya da yük","contextual_glosses":[{"applicability":"Bir halk veya grup yerinden alınıp başka bir yerde oturtulduğunda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Topluluğun yer değiştirilip oturtulmasını korur."},"facet_ids":["F001"],"text":"başka yere yerleştirilen topluluk","usage_role":"contextual"},{"applicability":"Asker adlarının belirli bir bölge kaydına yazıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Asker grubunu ve bölge kaydına bağlanmayı korur."},"facet_ids":["F002"],"text":"bölgeye kaydedilmiş askerler","usage_role":"contextual"},{"applicability":"Adın bir topluluğa ait ağır eşya veya yükler için kullanıldığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşınan yük anlamını korur."},"facet_ids":["F003"],"text":"topluluğun yükleri","usage_role":"contextual"}],"definition":"Yerinden alınıp başka yere yerleştirilen toplulukları, bir bölge kaydına bağlanan askerleri ve topluluğun taşınan yüklerini adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir topluluk eski yerinden alınıp başka bir yerde oturtulur."},{"facet_id":"F002","role":"specialization","statement":"Askerlerden oluşan bir grup belirli bir bölgenin kaydına bağlanabilir."},{"facet_id":"F003","role":"source_variant","statement":"Aynı ad alanında topluluğun taşıdığı ağır eşyalar da anılır."}],"identity_rationale":"Kaynak ifadesi başka yere taşınıp yerleştirilen toplulukları, bir bölge kaydına bağlanan askerleri ve topluluğun yüklerini birlikte verir. Bunlar tek bir basit nesne koyma anlamı değildir; ancak yerleştirilmiş veya kayıt altına konmuş kişi ve yükler başlığı altında korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"başka bir yere taşınıp yerleştirilen topluluklar"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bölgeye kaydedilen askerler veya topluluğun yükleri"}],"lexicalization_note":"bare olduğu için tanım bu ad grubunun kendi sınırında kalır; ticaret veya genel koyma kalıplarından anlam taşımaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar yerinden edilme, grup adı ve yük anlamı çevresindeki en yararlı sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal sonuçtaki yerleşmiş grubu adlandırır; komşu dal ayrılma ve sürülme hareketini adlandırır.","focus_only":"Odak dal başka yerde oturtulan topluluk adını verir.","gloss":"yerleştirilen topluluk ile yurttan çıkarma","neighbor_only":"Komşu dal yurtlardan çıkma veya çıkarılma eylemini anlatır.","neighbor_ref":"root_000256/B004","relation_type":"near_neighbor","shared_zone":"İkisi de bir grubun yurdundan ayrılması veya ayrılmaya zorlanması alanındadır."},{"boundary_match":"field_only","distinction":"Odak dalın belirleyici yönü yerleştirilme veya kayıt bağlamıdır; komşuda belirleyici yön karışık ve bölük bölük topluluktur.","focus_only":"Odak dal yer değiştirilmiş veya kayda geçirilmiş gruba bağlıdır.","gloss":"yerleştirilmiş grup ile karışık grup","neighbor_only":"Komşu dal farklı kabilelerden veya kesimlerden oluşan karışık toplulukları anlatır.","neighbor_ref":"root_001667/B002","relation_type":"same_field","shared_zone":"İkisi de insan gruplarını adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda yük anlamı aynı ad grubunun özel bir kullanımıdır; komşu dal yük kavramını çekirdek anlam yapar.","focus_only":"Odak dal yük anlamını topluluk adının bir varyantı olarak taşır.","gloss":"topluluk yükü ile genel yük","neighbor_only":"Komşu dal yük, ağırlık ve taşınan şeyler alanını genel olarak kapsar.","neighbor_ref":"root_000644/B001","relation_type":"near_neighbor","shared_zone":"İkisi de taşınan ağır eşya veya yük kavramına dokunur."}],"source_summary":"Toplu kanıt, dalı başka yere taşınıp yerleştirilen topluluklar ve kayıt altına alınan askerler etrafında kurar. Aynı toplu kanıt, adın topluluğa ait yükler için de kullanıldığını bildirir."},"support_links":["sup_80c7c66001a3ef24eccb","sup_b336ca74d7f3a9612e27"]},{"boundary":"Dal deve otlaması ve belirli otlak bitkisiyle sınırlıdır; hızlı yürüyüş anlamı dışarıda kalır.","branch_kind":"bare","branch_ref":"root_001657/B007","candidate_links":[{"candidate_id":"cand_c99e1b0c8e7bc09cf0ea","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"devenin tuzcul otu otlaması ve orada konaklaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Develer belirli otlak bitkisini yer veya onun üzerinde kalır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, develerin üzerinde kaldığı bitki veya otlak alanına da aktarılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve sürüsü, belirli otlak bitkisi ve bu bitki alanında kalma bağlamlarında uygundur.","boundary_detail":"Dal deve otlaması ve belirli otlak bitkisiyle sınırlıdır; hızlı yürüyüş anlamı dışarıda kalır.","concept_gloss":"devenin tuzcul otu otlaması ve orada konaklaması","contextual_glosses":[{"applicability":"Tek bir devenin bu bitkiyle beslenmesi veya yanında kalması bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Deveyi ve özel otlama nesnesini korur."},"facet_ids":["F001"],"text":"tuzcul otu otlayan deve","usage_role":"contextual"},{"applicability":"Ad bitkinin kendisine veya bu bitkinin bulunduğu otlak alanına geçtiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitki ve otlak alanı anlamını korur."},"facet_ids":["F002"],"text":"tuzcul otlak bitkisi","usage_role":"contextual"}],"definition":"Develerin belirli tuzcul veya sert otlak bitkisini yemesi ya da onun bulunduğu yerde konaklaması; aynı ad bitki veya otlak alanı için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Develer belirli otlak bitkisini yer veya onun üzerinde kalır."},{"facet_id":"F002","role":"extension","statement":"Ad, develerin üzerinde kaldığı bitki veya otlak alanına da aktarılır."}],"identity_rationale":"Kaynak ifadesi develerin belirli meralık bitkiyi yemesi veya o bitki alanında konaklaması ile bitkinin kendisine verilen adı birlikte gösterir. Provisional çerçeve otlama, konaklama ve bitki adı ilişkisini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tuzcul otu otlayan veya yanında konaklayan dişi deve"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tuzcul bitkiyi otlayan develer"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"tuzcul yemlik bitki veya develerin kaldığı otlak"}],"lexicalization_note":"bare olduğu için tanım bu otlama ve bitki alanına bağlı yalın kullanımları verir; başka deve hareketleri içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar genel mera, otlatma eylemi ve alanda kalma anlamlarıyla karışmayı sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal deve ve belirli bitki türüyle sınırlıdır; komşu dal genel ot ve mera adıdır.","focus_only":"Odak dal develeri ve belirli tuzcul otlak bitkisini ister.","gloss":"özel deve otlağı ile genel mera","neighbor_only":"Komşu dal hayvanların yediği ot ve merayı genel biçimde kapsar.","neighbor_ref":"root_000003/B001","relation_type":"near_neighbor","shared_zone":"İkisi de hayvanların yediği bitki ve otlak alanındadır."},{"boundary_match":"field_only","distinction":"Odak dal hayvanın yediği özel bitki ve konaklama yeridir; komşu dal otlatma izni ve serbest bırakma eylemidir.","focus_only":"Odak dal belirli bitkiyi yeme ve yanında kalma durumunu adlandırır.","gloss":"özel otlama ile meraya salma","neighbor_only":"Komşu dal hayvanı meraya salma ve serbest otlatma eylemini anlatır.","neighbor_ref":"root_000764/B003","relation_type":"same_field","shared_zone":"İkisi de sürü hayvanlarının otlaması alanındadır."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı koşulu özel bitki adıdır; komşuda ayırıcı koşul hayvanın bir yanda kalması veya sürü niteliğidir.","focus_only":"Odak dal özel otlak bitkisi ve deve kullanımını korur.","gloss":"deve otlağı ile yana bağlı otlama","neighbor_only":"Komşu dal belirli bir yana bağlı kalarak otlayan veya çok sayıda olan hayvan grubunu anlatır.","neighbor_ref":"root_000902/B006","relation_type":"near_neighbor","shared_zone":"İkisi de hayvanın belli bir otlama alanında kalmasına ilişir."}],"source_summary":"Ortak kanıt, dalı develerin belirli otlak bitkisini yemesi ve onun bulunduğu yerde kalması olarak verir. Aynı kanıt adın bitkiye veya bu bitkinin bulunduğu yere de geçtiğini gösterir."},"support_links":["sup_3e0da71c75f0136e8c64"]},{"boundary":"Dal terzilikte kumaşa pamuk serme ve ardından dikme işlemidir; genel koyma anlamı değildir.","branch_kind":"bare","branch_ref":"root_001657/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"kumaşa pamuk serip dikme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Pamuk kumaşın üzerine düzgünce serilir veya konur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Pamuk yerleştirildikten sonra giysinin dikilmesi bu teknik işin parçasıdır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Pamuk yerleştirme ve sonrasındaki giysi dikme işlemini birlikte anlatır.","boundary_detail":"Dal terzilikte kumaşa pamuk serme ve ardından dikme işlemidir; genel koyma anlamı değildir.","concept_gloss":"kumaşa pamuk serip dikme","contextual_glosses":[{"applicability":"Terzinin pamuğu kumaş üzerine yerleştirdiği aşama için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Pamuk yerleştirme aşamasını korur."},"facet_ids":["F001"],"text":"kumaşa pamuk sermek","usage_role":"contextual"},{"applicability":"Giysinin pamuk yerleştirmesinden sonra dikildiği teknik bağlam için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Süreç sırasını ve dikme aşamasını korur."},"facet_ids":["F002"],"text":"pamuk serildikten sonra dikmek","usage_role":"explanatory"}],"definition":"Terzinin pamuğu kumaş üzerine sermesi ve bu yerleştirmeden sonra pamuklu giysiyi dikmesi.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Pamuk kumaşın üzerine düzgünce serilir veya konur."},{"facet_id":"F002","role":"specialization","statement":"Pamuk yerleştirildikten sonra giysinin dikilmesi bu teknik işin parçasıdır."}],"identity_rationale":"Kaynak ifadesi terzinin pamuğu kumaş üzerine sermesini ve pamuk konduktan sonra giysiyi dikmesini aynı el işi sürecinde verir. Provisional çerçeve bu teknik kullanımın sınırını doğru gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kumaşa pamuk koyma veya sonra giysiyi dikme"}],"lexicalization_note":"bare olduğu için tanım bu teknik el işi adında kalır; genel yerleştirme veya karşılıklı anlaşma anlamı içeri alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar dikiş, astar ve pamuk hazırlama alanlarıyla en yakın karışmaları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal pamuk serme aşamasına bağlıdır; komşu dal bu özel hazırlık olmadan genel dikiştir.","focus_only":"Odak dal dikmeden önce kumaşa pamuk yerleştirme aşamasını ister.","gloss":"pamuklu dikim ile genel dikiş","neighbor_only":"Komşu dal dikiş, dikilmiş şey ve dikme aracı alanını genel biçimde kapsar.","neighbor_ref":"root_000453/B006","relation_type":"near_neighbor","shared_zone":"İkisi de kumaş işleme ve dikme alanındadır."},{"boundary_match":"partial","distinction":"Odak dal teknik işlemdir; komşu dal giysideki iç katman veya astar sonucudur.","focus_only":"Odak dal pamuğun kumaş üzerine serilmesi ve ardından dikilmesidir.","gloss":"pamuk serme ile astar","neighbor_only":"Komşu dal elbisenin iç yüzü veya astarını adlandırır.","neighbor_ref":"root_000128/B003","relation_type":"near_neighbor","shared_zone":"İkisi de giysinin iç yapısı ve katmanlarıyla ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal lifli malzemeyi kumaşa koyar; komşu dal lifli malzemenin hacmini açar ve dağıtır.","focus_only":"Odak dal pamuğu kumaşa yerleştirir.","gloss":"yerleştirme ile kabartma","neighbor_only":"Komşu dal pamuk veya yünün kabartılıp dağıtılmasını anlatır.","neighbor_ref":"root_001534/B001","relation_type":"same_field","shared_zone":"İkisi de pamuk veya yün gibi lifli malzemeyle çalışır."}],"source_summary":"Ortak kanıt, dalı terzilikte pamuğun kumaşa serilmesi ve bundan sonra pamuklu giysinin dikilmesi olarak toplar. Bu kullanım genel koyma değil, belirli bir el işi sürecidir."},"support_links":[]},{"boundary":"Dal yalnızca kadın ve baş örtüsü kalıbına bağlıdır; genel soyunma veya doğum değildir.","branch_kind":"collocation","branch_ref":"root_001657/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"baş örtüsünü çıkarıp baş örtüsüz kalma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın baş örtüsünü çıkarır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sonuçta kadın baş örtüsüz olarak nitelenir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadın öznesi ve baş örtüsü kalıbı bulunduğunda tam uygulanır.","boundary_detail":"Dal yalnızca kadın ve baş örtüsü kalıbına bağlıdır; genel soyunma veya doğum değildir.","concept_gloss":"baş örtüsünü çıkarıp baş örtüsüz kalma","contextual_glosses":[{"applicability":"Kadının baş örtüsünü çıkarmış olmasından doğan durum nitelenirken uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sonuçtaki örtüsüzlük durumunu korur."},"facet_ids":["F002"],"text":"baş örtüsüz kadın","usage_role":"contextual"},{"applicability":"Eylemin kendisi, yani örtünün çıkarılması öne çıktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Baş örtüsünün çıkarılmasını korur."},"facet_ids":["F001"],"text":"baş örtüsünü çıkarmak","usage_role":"contextual"}],"definition":"Kadının baş örtüsünü çıkarıp üzerinde baş örtüsü bulunmaması durumunu anlatan kalıp kullanım.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın baş örtüsünü çıkarır."},{"facet_id":"F002","role":"extension","statement":"Sonuçta kadın baş örtüsüz olarak nitelenir."}],"identity_rationale":"Kaynak ifadesi kadın için baş örtüsünü çıkarmayı ve bu yüzden üzerinde baş örtüsü bulunmamasını doğrudan verir. Provisional çerçeve doğum veya genel koyma anlamına kaymadan bu kalıp sınırını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"baş örtüsünü çıkardığı için baş örtüsüz kadın"}],"lexicalization_note":"collocation olduğu için tanım kadın baş örtüsü kalıbına bağlıdır; yalın köke genel çıkarma anlamı verilmez.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar genel açma, kadın örtüsü ve örtülü-örtüsüz karşıtlığını açıklar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal baş örtüsüz kadın sonucunu ister; komşu dal bu sonucu gerektirmeyen genel örtü kaldırmadır.","focus_only":"Odak dal kadın baş örtüsüne bağlı özel kalıptır.","gloss":"baş örtüsünü çıkarma ile genel açma","neighbor_only":"Komşu dal her türlü örtüyü kaldırma, açma ve temizleme kullanımlarını kapsar.","neighbor_ref":"root_000712/B001","relation_type":"near_synonym","shared_zone":"İkisi de örtü veya kapatan şeyin kaldırılması alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal örtünün kaldırıldığı sonucu anlatır; komşu dal örtünün sağladığı saklanma yönündedir.","focus_only":"Odak dal baş örtüsünün çıkarılması ve baş örtüsüz kalmadır.","gloss":"örtüsüz kalma ile örtünme","neighbor_only":"Komşu dal kadının örtünmesini sağlayan şeyle ilgilidir.","neighbor_ref":"root_000848/B012","relation_type":"polarity_pair","shared_zone":"İkisi de kadının örtüsü ve örtülü olma durumu alanındadır."},{"boundary_match":"opposed","distinction":"Odak dal örtünün yokluğuna gider; komşu dal örtünün kendisini ve kapatma işlevini adlandırır.","focus_only":"Odak dal baş örtüsünün çıkarılmasıyla oluşan örtüsüzlüğü anlatır.","gloss":"örtüyü çıkarma ile örtü","neighbor_only":"Komşu dal bedeni veya baş ve göğsü örten dış örtüyü adlandırır.","neighbor_ref":"root_000252/B004","relation_type":"polarity_pair","shared_zone":"İkisi de kadın örtüsü ve bedenin örtülmesi çevresindedir."}],"source_summary":"Ortak kanıt, dalı kadının baş örtüsünü çıkarması ve bu yüzden baş örtüsüz olması olarak verir. Kullanım kalıp bağlıdır ve genel koyma anlamına genişletilmez."},"support_links":[]},{"boundary":"Dal yalnızca bir şeyi başkasına saklatmak üzere bırakma kalıbıdır.","branch_kind":"collocation","branch_ref":"root_001657/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"saklaması için birine bırakma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahip, bir şeyi saklaması için başka bir kişinin yanına bırakır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bırakılan şey, saklanmak üzere başkasına teslim edilen mal olarak anlaşılır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin korunması için başka kişinin yanına bırakıldığı kalıp bağlamlarda uygundur.","boundary_detail":"Dal yalnızca bir şeyi başkasına saklatmak üzere bırakma kalıbıdır.","concept_gloss":"saklaması için birine bırakma","contextual_glosses":[{"applicability":"Bir kişi malını başka birinin yanında korunsun diye bıraktığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Saklama amacını ve başkasına bırakmayı korur."},"facet_ids":["F001"],"text":"saklatmak üzere bırakmak","usage_role":"contextual"}],"definition":"Bir malı veya şeyi korunup saklanması için başka bir kişinin yanında bırakma.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahip, bir şeyi saklaması için başka bir kişinin yanına bırakır."},{"facet_id":"F002","role":"associated_use","statement":"Bırakılan şey, saklanmak üzere başkasına teslim edilen mal olarak anlaşılır."}],"identity_rationale":"Kaynak ifadesi bir şeyi bir kişinin yanında saklatma anlamındaki kalıbı doğrudan verir. Provisional çerçeve ticari indirim veya genel koyma anlamına kaymadan saklanması için bırakma ilişkisini doğru temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir şeyi saklaması için birinin yanına bırakmak"}],"lexicalization_note":"collocation olduğu için tanım kişinin yanında saklatma kalıbına bağlı kalır; yalın köke genel bırakma anlamı yüklenmez.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar saklatma, koruma ve güvence olarak tutma arasındaki temel sınırları kapsar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıp bağlıdır; komşu dal aynı ilişkiyi daha geniş ad ve fiil ağıyla taşır.","focus_only":"Odak dal belirli bırakma kalıbıyla sınırlıdır.","gloss":"saklatmak için bırakma","neighbor_only":"Komşu dal saklanmak üzere bırakılan şey, bırakma eylemi, kabul etme ve bırakılan yer gibi alanları daha geniş kapsar.","neighbor_ref":"root_001635/B005","relation_type":"near_synonym","shared_zone":"İkisi de bir şeyi korunması için başkasına bırakma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal saklama için teslim etme anını anlatır; komşu dal koruma işinin kendisini anlatır.","focus_only":"Odak dal bir şeyi başkasına bırakma teslimini içerir.","gloss":"bırakma ile koruma","neighbor_only":"Komşu dal koruma, gözetme ve bekçilik işini genel olarak anlatır.","neighbor_ref":"root_000342/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin güvenle tutulması amacına bağlanır."},{"boundary_match":"partial","distinction":"Odak dal saklama ve geri alma güvenine dayanır; komşu dal borç ilişkisine bağlı güvence işlevidir.","focus_only":"Odak dal korunsun diye bırakılan maldır.","gloss":"saklatılan şey ile güvence","neighbor_only":"Komşu dal borca güvence olarak tutulan şeyi anlatır.","neighbor_ref":"root_000607/B001","relation_type":"near_neighbor","shared_zone":"İkisi de bir malın başka elde tutulmasına ilişir."}],"source_summary":"Ortak kanıt, dalı bir şeyi başkasının yanında saklatmak üzere bırakma kalıbı olarak verir. Bırakılan şey, korunması için o kişiye teslim edilen maldır."},"support_links":[]},{"boundary":"Çekirdek karşılıklı anlaşma ve görüşmedir; işlem türleri buna bağlı özel kullanımlardır.","branch_kind":"bare","branch_ref":"root_001657/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"karşılıklı anlaşma ve görüşme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki kişi veya taraf bir iş üzerinde karşılıklı anlaşır ve onu görüşür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Karşılıklı para koymalı sözleşme aynı ad alanında özel bir işlem kullanımıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Satıştan karşılıklı vazgeçme de bu karşılıklı işlem alanına bağlanır."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ana çekirdeği verir; işlem türleri bağlamda gerektiğinde ayrıca açıklanır.","boundary_detail":"Çekirdek karşılıklı anlaşma ve görüşmedir; işlem türleri buna bağlı özel kullanımlardır.","concept_gloss":"karşılıklı anlaşma ve görüşme","contextual_glosses":[{"applicability":"Tarafların bir işi karşılıklı kabul ettiği ve görüştüğü bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı anlaşma çekirdeğini korur."},"facet_ids":["F001"],"text":"bir konuda anlaşmak","usage_role":"contextual"},{"applicability":"İki tarafın satış işlemini bırakması anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Satışı karşılıklı bırakma kullanımını korur."},"facet_ids":["F003"],"text":"satıştan karşılıklı vazgeçme","usage_role":"contextual"},{"applicability":"Tarafların sonuç için karşılıklı para veya değer bağladığı işlem kullanımı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı işlem ve değer bağlama anlamını korur."},"facet_ids":["F002"],"text":"karşılıklı para koymalı sözleşme","usage_role":"explanatory"}],"definition":"İki tarafın bir işi karşılıklı olarak ortaya koyup üzerinde anlaşması veya görüşmesi; buna bağlı olarak para koymalı sözleşme ve satıştan karşılıklı vazgeçme gibi işlem kullanımları da bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki kişi veya taraf bir iş üzerinde karşılıklı anlaşır ve onu görüşür."},{"facet_id":"F002","role":"associated_use","statement":"Karşılıklı para koymalı sözleşme aynı ad alanında özel bir işlem kullanımıdır."},{"facet_id":"F003","role":"associated_use","statement":"Satıştan karşılıklı vazgeçme de bu karşılıklı işlem alanına bağlanır."}],"identity_rationale":"Kaynak ifadesi iki tarafın bir iş üzerinde karşılıklı anlaşmasını ve onu görüşmesini ana çekirdek olarak verir. Aynı toplu kanıt bahisleşme ve satıştan karşılıklı vazgeçme gibi işlem kullanımlarını da içerdiğinden tanım yalnızca genel anlaşma diye düzleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bir işte karşılıklı anlaşmak ve onu görüşmek"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"karşılıklı para koymalı sözleşme veya satışı bırakma"}],"lexicalization_note":"bare olduğu için tanım karşılıklı anlaşma adının kendi yalın alanında kalır; fiziksel koyma anlamı içeri alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar anlaşma, razı olma ve karşılıklı bırakma alanlarındaki başlıca sınırları gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal karşılıklı görüşme ve işlem bağını korur; komşu dal daha genel uyum ve denkliği anlatır.","focus_only":"Odak dal iki tarafın bir işi görüşmesini ve bazı işlem uzantılarını içerir.","gloss":"karşılıklı anlaşma ile uygunluk","neighbor_only":"Komşu dal uygunluk, denk düşme ve söz birliği alanını daha genel biçimde kapsar.","neighbor_ref":"root_000927/B003","relation_type":"near_synonym","shared_zone":"İkisi de uyuşma ve anlaşma alanındadır."},{"boundary_match":"partial","distinction":"Odak dal işin konuşulup karara bağlanmasını öne çıkarır; komşu dal iç kabul ve hoşnutluk yönünü öne çıkarır.","focus_only":"Odak dal görüşme, karşılıklı sözleşme ve satıştan vazgeçme kullanımlarını içerir.","gloss":"anlaşma ile karşılıklı razı olma","neighbor_only":"Komşu dal tarafların birbirinden hoşnut olup razı olması yönündedir.","neighbor_ref":"root_000569/B003","relation_type":"near_neighbor","shared_zone":"İkisi de iki taraflı kabul alanındadır."},{"boundary_match":"partial","distinction":"Satıştan vazgeçme bağlamında yaklaşırlar; odak dalın ana çekirdeği daha geniş karşılıklı görüşme ve anlaşmadır.","focus_only":"Odak dal satıştan vazgeçmenin yanında genel görüşme ve anlaşmayı da taşır.","gloss":"satıştan vazgeçme","neighbor_only":"Komşu dal iki taraf arasında bırakma veya ayrılmayı çekirdek yapar.","neighbor_ref":"root_000180/B005","relation_type":"near_synonym","shared_zone":"İkisi de karşılıklı bırakma kullanımıyla kesişir."}],"source_summary":"Ortak kanıt, dalı bir konuda karşılıklı anlaşma ve görüşme olarak toplar. Aynı toplu kanıt, karşılıklı para koymalı sözleşme ve satıştan vazgeçme gibi işlem uzantılarını da tek branch claim altında verir."},"support_links":[]},{"boundary":"Dal sağlamlık eksikliği, kadınsı sayılan yumuşama ve at kusurunu kapsar; sosyal düşüklükle aynı değildir.","branch_kind":"bare","branch_ref":"root_001657/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"sağlamlık eksikliği ve kusurlu yumuşama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin işi, yapısı veya yaratılışı sağlam ve toparlanmış değildir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Konuşma veya kişide kadın konuşmasına benzetilen yumuşama ve kadınsı sayılan tavır anılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"At için alt bacağın yayılıp üst kısmın ardından gelmesi biçimindeki yürüyüş kusuru örneklenir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişinin sağlam olmaması, kadınsı sayılan yumuşama ve at yürüyüş kusurunu açıklayıcı biçimde kapsar.","boundary_detail":"Dal sağlamlık eksikliği, kadınsı sayılan yumuşama ve at kusurunu kapsar; sosyal düşüklükle aynı değildir.","concept_gloss":"sağlamlık eksikliği ve kusurlu yumuşama","contextual_glosses":[{"applicability":"Kişinin işi, yapısı veya karakteri toparlanmış ve sağlam görülmediğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişideki sağlamlık eksikliğini korur."},"facet_ids":["F001"],"text":"sağlam olmayan kişi","usage_role":"contextual"},{"applicability":"Kaynakların konuşmayı kadın konuşmasına benzeterek nitelediği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmadaki kadınsı sayılan yumuşama bilgisini korur."},"facet_ids":["F002"],"text":"kadınsı sayılan konuşma","usage_role":"contextual"},{"applicability":"Atın bacak hareketindeki kusur özel olarak anlatıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"At öznesini ve yürüyüş kusurunu korur."},"facet_ids":["F003"],"text":"yürüyüş kusurlu at","usage_role":"contextual"}],"definition":"İnsanda işin, yapının veya tavrın sağlam olmaması; konuşma ya da kişide kadınsı sayılan yumuşama ve atta belirli bir yürüyüş kusuru için de kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin işi, yapısı veya yaratılışı sağlam ve toparlanmış değildir."},{"facet_id":"F002","role":"extension","statement":"Konuşma veya kişide kadın konuşmasına benzetilen yumuşama ve kadınsı sayılan tavır anılır."},{"facet_id":"F003","role":"example","statement":"At için alt bacağın yayılıp üst kısmın ardından gelmesi biçimindeki yürüyüş kusuru örneklenir."}],"identity_rationale":"Kaynak ifadesi sağlam olmayan kişi veya yaratılış, kadın konuşmasına benzetilen yumuşama, kişide kadınsı sayılan tavır ve attaki yürüyüş kusurunu aynı dalda verir. Bu malzeme tek bir düz anlamdan çok sağlamlık eksikliği ve kusurlu yumuşama çevresinde tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"işi veya yapısı sağlam olmayan, kadınsı sayılan kişi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"kadın konuşmasına benzetilen yumuşama"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"alt bacağını yayarak yürüyen kusurlu at"}],"lexicalization_note":"bare olduğu için tanım bu yalın nitelik alanında kalır; sosyal düşüklük veya ticari eksilme buraya alınmaz.","neighbor_coverage_note":"Adayların tamamı değerlendirildi; yayımlananlar kişisel sağlamlık, bedensel gevşeklik ve genel bozulma alanlarındaki en yakın sınırları verir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yapısal sağlamlık ve belirli at kusurunu da kapsar; komşu dal akıl ve tavır gevşekliği çevresindedir.","focus_only":"Odak dal sağlam olmayan kişi, kadınsı sayılan tavır ve at kusurunu birlikte taşır.","gloss":"sağlamlık eksikliği ile gevşeklik","neighbor_only":"Komşu dal akıl eksikliği, görüşte gevşeklik ve hafiflik alanına daha çok yönelir.","neighbor_ref":"root_001173/B006","relation_type":"near_neighbor","shared_zone":"İkisi de kişide toparlanmışlık eksikliği ve yumuşaklık alanına yaklaşır."},{"boundary_match":"partial","distinction":"Odak dal sosyal veya tavırsal nitelemeye de açılır; komşu dal daha çok organ ve eklem gevşekliğidir.","focus_only":"Odak dal insan niteliği ve at yürüyüş kusurunu aynı ad altında tutar.","gloss":"sağlam olmayan yapı ile gevşek eklem","neighbor_only":"Komşu dal eklemlerin gevşemesi ve bedenin parçalanmış gibi olması alanındadır.","neighbor_ref":"root_000432/B008","relation_type":"near_neighbor","shared_zone":"İkisi de bedensel veya yapısal gevşeklik alanındadır."},{"boundary_match":"partial","distinction":"Odak dal kişisel yapı ve belirli kusurlara bağlıdır; komşu dal işin veya düzenin bozulmasına bağlıdır.","focus_only":"Odak dal kişide sağlamlık eksikliği ve konuşma yumuşamasını anlatır.","gloss":"sağlamlık eksikliği ile bozulma","neighbor_only":"Komşu dal iş, savaş veya görüşte bozulma ve zayıflamayı anlatır.","neighbor_ref":"root_000435/B010","relation_type":"near_neighbor","shared_zone":"İkisi de bir şeyin güçlü ve düzgün olmamasını paylaşır."}],"source_summary":"Toplu kanıt, dalı insanda sağlamlık ve toparlanmışlık eksikliği çevresinde verir. Aynı kanıt konuşma ve kişide kadınsı sayılan yumuşama ile atta belirli bir yürüyüş kusurunu da bu gevşeklik alanına bağlar."},"support_links":[]},{"boundary":"Dal binme amacıyla deve başı veya boynunun alçaltılmasıdır; yol hızı değildir.","branch_kind":"bare","branch_ref":"root_001657/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","surface_ar":"مَّوْضُوعَةٌ"}],"gloss":"binmek için devenin boynunu alçaltma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Devenin başı veya boynu aşağı indirilir ya da deve bunu yapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Alçaltmanın amacı binicinin ayağını boyna koyarak deveye binmesidir."}}],"root_ar":"و ض ع","root_id":"root_001657","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Deve ayaktayken binicinin ayağını boyna koyup binmesi için yapılan alçaltma bağlamında uygundur.","boundary_detail":"Dal binme amacıyla deve başı veya boynunun alçaltılmasıdır; yol hızı değildir.","concept_gloss":"binmek için devenin boynunu alçaltma","contextual_glosses":[{"applicability":"Binmek için hayvanın boynu veya başı aşağı alındığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyun veya baş indirme eylemini korur."},"facet_ids":["F001"],"text":"devenin boynunu indirmek","usage_role":"contextual"},{"applicability":"Devenin biniciye çıkış kolaylığı sağladığı duruş açıklanırken uygundur.","error_profile":{"adds":"Çöker gibi ifadesi diz çökme çağrışımı ekleyebilir; kaynak çekirdeği baş ve boyun alçaltmadır.","collision":null,"fit":"broadening","loses":null,"preserves":"Binme amacını ve aşağı eğilme yönünü korur."},"facet_ids":["F001","F002"],"text":"binmek için çöker gibi eğilmek","usage_role":"explanatory"}],"definition":"Devenin ayaktayken başını veya boynunu alçaltması ya da alçalttırılması; binici ayağını boyna koyup binebilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Devenin başı veya boynu aşağı indirilir ya da deve bunu yapar."},{"facet_id":"F002","role":"specialization","statement":"Alçaltmanın amacı binicinin ayağını boyna koyarak deveye binmesidir."}],"identity_rationale":"Kaynak ifadesi devenin ayaktayken başını veya boynunu alçaltmasını, binicinin ayağını boyna koyup binebilmesi amacıyla açıkça verir. Provisional çerçeve bu amaçlı hayvan duruşunu doğru temsil eder ve hızlı yürüme anlamına kaymaz.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"binmek için devenin boynunu veya başını alçaltması"}],"lexicalization_note":"bare olduğu için tanım bu deve duruşunun yalın kullanımında kalır; genel koyma veya hızlı yürüyüş anlamı alınmaz.","neighbor_coverage_note":"Tüm adaylar değerlendirildi; yayımlananlar aynı deve duruşu, yorgunluk duruşu ve karşıt baş yönüyle en önemli ayrımları verir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sınırları örtüşür; iki dal da aynı amaçlı deve duruşunu verir.","focus_only":null,"gloss":"binmek için deve başını alçaltma","neighbor_only":null,"neighbor_ref":"root_000426/B005","relation_type":"synonym","shared_zone":"İkisi de devenin başını veya boynunu binici binsin diye aşağı almasını anlatır."},{"boundary_match":"partial","distinction":"Odak dal yardımcı ve amaçlı bir binme duruşudur; komşu dal yorgunluk belirtisidir.","focus_only":"Odak dal alçaltmayı binme amacıyla yapar.","gloss":"binme için alçaltma ile yorgun boyun uzatma","neighbor_only":"Komşu dal devenin yorgunluktan boynunu uzatması ve ses çıkarmasıdır.","neighbor_ref":"root_000814/B007","relation_type":"near_neighbor","shared_zone":"İkisi de devenin boyun duruşuna bağlıdır."},{"boundary_match":"opposed","distinction":"Odak dal aşağı yönlü ve binmeye yardımcıdır; komşu dal yukarı yönlü bir baş hareketidir.","focus_only":"Odak dal binmek için baş veya boynu aşağı alır.","gloss":"baş indirme ile baş kaldırma","neighbor_only":"Komşu dal yüklenirken başın yukarı kaldırılmasını anlatır.","neighbor_ref":"root_001000/B009","relation_type":"polarity_pair","shared_zone":"İkisi de yüklenme veya binme çevresinde hayvan başının yönüyle ilgilidir."}],"source_summary":"Ortak kanıt, dalı devenin başını veya boynunu binme amacıyla alçaltması olarak verir. Eylem, hayvanın yol içi hızı değil, biniciye çıkış kolaylığı sağlayan duruştur."},"support_links":[]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000063/B003","candidate_links":[{"candidate_id":"cand_21ab6f111adc25e1acf7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3c54c8380b468c48597b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Reaching full maturity or limit sharpens the source's extreme condition against the neutral readiness of the placed cups.","root":"ء ن ي","source_ref":"88:5","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000063","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bb4f38c1e59003f7f1e8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000083/B001","candidate_links":[{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e82c542352c138dc0359","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dispersal supplies broad coverage, extending the local cup stations into a complete inhabited surface.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000083","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b336ca74d7f3a9612e27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000240/B006","candidate_links":[{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e82c542352c138dc0359","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Continuing provision or supply gives the upstream flow a sustaining function that the cups can portion.","root":"ج ر ي","source_ref":"88:12","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000240","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b336ca74d7f3a9612e27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000722/B001","candidate_links":[{"candidate_id":"cand_21ab6f111adc25e1acf7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3c54c8380b468c48597b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Giving someone drink supplies the contrasting causative relation in which intake is administered.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000722","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bb4f38c1e59003f7f1e8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000741/B007","candidate_links":[{"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_57217d4514b217da18d9","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Pleasurable hearing and music make the absent sonic channel specific enough to activate the instrument branch.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000741","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_aad66371219c89c7e1ab"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000871/B001","candidate_links":[{"candidate_id":"cand_675e5254e815286595bb","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_e82c542352c138dc0359","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Alignment on an even line supplies ordered horizontal adjacency after the cups.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000871","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_b336ca74d7f3a9612e27"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001042/B002","candidate_links":[{"candidate_id":"cand_71ed65cf10ddd214eaab","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_65221ad918c963102235","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Elevation of rank lets the garden's height operate socially as well as spatially.","root":"ع ل و","source_ref":"88:10","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001042","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bb11170b199d1277b9b3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001069/B006","candidate_links":[{"candidate_id":"cand_21ab6f111adc25e1acf7","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_3c54c8380b468c48597b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The flowing water source supplies an undivided origin from which the earlier recipients are made to drink.","root":"ع ي ن","source_ref":"88:5","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001069","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bb4f38c1e59003f7f1e8"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001361/B003","candidate_links":[{"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_57217d4514b217da18d9","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Mixed noisy sound supplies what the scene excludes, turning set-down sonic objects into an image of tranquility.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001361","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_aad66371219c89c7e1ab"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001525/B001","candidate_links":[{"candidate_id":"cand_71ed65cf10ddd214eaab","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_65221ad918c963102235","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Good condition and beneficence supply the recipients' favorable estate.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001525","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_bb11170b199d1277b9b3"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001630/B004","candidate_links":[{"candidate_id":"cand_71ed65cf10ddd214eaab","lane":"macro"},{"candidate_id":"cand_223d5984fe02c0e63dca","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_65221ad918c963102235","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The face standing for the whole person identifies the beneficiaries whose position is being contrasted with the objects.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"hft_ref":"hft_965d33aa5db61f7461ad","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The face as a stand-in for the person supplies the nearby bodily scale for the visual analogy.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001630","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_80c7c66001a3ef24eccb","sup_bb11170b199d1277b9b3"]}],"candidate_inventory":[{"anchor_refs":["88:14","88:5"],"branch_refs":["root_000063/B004","root_001328/B001","root_001328/B005","root_001657/B001"],"candidate_id":"cand_0e07f1c4f266a0d6604c","commentary_obligation":"review","focus_branch_refs":["root_001328/B001","root_001328/B005","root_001657/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000063/B004"],"root_ids":[],"scope":"pericope","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_ids":["sup_40f4184ec37796a22546","sup_4fe7afca88907115e180","sup_80286e18a4bac3c6cffb","sup_9a471539b0f28af84ca9","sup_d0bf93f968bbf9e4ba83"],"title":"Cup, Vessel, and Placement","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:13","88:14","88:15"],"branch_refs":["root_000582/B001","root_000697/B011","root_000871/B004","root_001657/B001"],"candidate_id":"cand_e0b5962eda40aa011b0c","commentary_obligation":"review","focus_branch_refs":["root_001657/B001"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000582/B001","root_000697/B011","root_000871/B004"],"root_ids":[],"scope":"pericope","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_ids":["sup_3f0e3fde702f98ff06e2","sup_5eab647facb844adf4b6","sup_864db6a36a51e7f5c840","sup_b0038bff32bfbb04660a","sup_cfa66887abd9775cafcb"],"title":"Raised Couch and Seat","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:14","88:4","88:6","88:7"],"branch_refs":["root_000744/B001","root_000880/B010","root_000908/B005","root_001657/B007"],"candidate_id":"cand_c99e1b0c8e7bc09cf0ea","commentary_obligation":"review","focus_branch_refs":["root_001657/B007"],"kind":"resonance_nomination","lane":"macro","nominated_branch_refs":["root_000744/B001","root_000880/B010","root_000908/B005"],"root_ids":[],"scope":"pericope","source_local_id":"E:Noxious Fodder","source_type":"channel","support_ids":["sup_1c70b47141e2fa91a60c","sup_1eb890d50c87f39e9d22","sup_3e0da71c75f0136e8c64","sup_3e62797937df4e40d6be","sup_83ada64159fe803dee25"],"title":"Noxious Fodder","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["88:14","88:5"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_000063/B003","root_000722/B001","root_001069/B006","root_001328/B005","root_001657/B001"],"candidate_id":"cand_21ab6f111adc25e1acf7","commentary_obligation":"review","hft_ref":"hft_3c54c8380b468c48597b","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-administered-versus-offered-drink","source_type":"hft","support_ids":["sup_bb4f38c1e59003f7f1e8"],"title":"delta-administered-versus-offered-drink","trust":"legacy_unbound"},{"anchor_refs":["88:10","88:14","88:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_001042/B002","root_001328/B001","root_001525/B001","root_001630/B004","root_001657/B005"],"candidate_id":"cand_71ed65cf10ddd214eaab","commentary_obligation":"review","hft_ref":"hft_65221ad918c963102235","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-downward-service-in-high-estate","source_type":"hft","support_ids":["sup_bb11170b199d1277b9b3"],"title":"delta-downward-service-in-high-estate","trust":"legacy_unbound"},{"anchor_refs":["88:12","88:13","88:14","88:15","88:16"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_000083/B001","root_000240/B006","root_000582/B001","root_000697/B011","root_000871/B001","root_001328/B005","root_001657/B006"],"candidate_id":"cand_675e5254e815286595bb","commentary_obligation":"review","hft_ref":"hft_e82c542352c138dc0359","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta-hydraulic-furnishing-topology","source_type":"hft","support_ids":["sup_b336ca74d7f3a9612e27"],"title":"delta-hydraulic-furnishing-topology","trust":"legacy_unbound"},{"anchor_refs":["88:11","88:14"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_000741/B007","root_001328/B002","root_001361/B003","root_001657/B001"],"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","commentary_obligation":"review","hft_ref":"hft_57217d4514b217da18d9","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-silenced-instrument-shadow","source_type":"hft","support_ids":["sup_aad66371219c89c7e1ab"],"title":"outlier-silenced-instrument-shadow","trust":"legacy_unbound"},{"anchor_refs":["88:13","88:14","88:8"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:14","branch_refs":["root_000697/B011","root_001328/B006","root_001630/B004","root_001657/B006"],"candidate_id":"cand_223d5984fe02c0e63dca","commentary_obligation":"review","hft_ref":"hft_965d33aa5db61f7461ad","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier-anthropomorphic-cup-stations","source_type":"hft","support_ids":["sup_80c7c66001a3ef24eccb"],"title":"outlier-anthropomorphic-cup-stations","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_4d8a25f4cc2146ab25db","connection_ref":"conn_97be6a3aa2fe1d578f5c","note":"Local contrary scene: drinking from عَيْنٍ ءَانِيَةٍ frames the later prepared cups.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_04509d5d1efe19060a35","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:5","source_note":"Placed cups extend the same-surah setting of prepared drinking service.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:5","source_target_components":["88:5"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:5","target_evidence":{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"},"target_ref":"88:5"},{"connection_evidence_ref":"conn_ev_5e8c483be261c9b619d5","connection_ref":"conn_af98dc0168decbdefa5a","note":"Immediate continuation adds arranged furnishings beside the positioned cups.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_b5da870f5b2a7e49b6cf","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:15","source_note":"The adjacent أكواب موضوعة locates the نمارق within a deliberately prepared sequence of objects.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:15","source_target_components":["88:15"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:15","target_evidence":{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},"target_ref":"88:15"},{"connection_evidence_ref":"conn_ev_843d3abf09604c0213a4","connection_ref":"conn_8c9c9cdd9a0f6a3aa74d","note":"Immediate prior raised couches make the cups part of a prepared elevated setting.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_3de235196bcbd0cee8d3","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:13","source_note":"Immediate placed cups show the couches within a prepared furnishing sequence.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:13","source_target_components":["88:13"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:13","target_evidence":{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},"target_ref":"88:13"},{"connection_evidence_ref":"conn_ev_a75cd37d5e7f41a5b62c","connection_ref":"conn_7aff262a9822c7998ef7","note":"Immediate prior عَيْنٌ جَارِيَةٌ supplies the flowing-drink context for the cups.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2bd1d4d0a1adb6a80443","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:12","source_note":"Immediate continuation adds a further item in the focus's فِيهَا scene.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:12","source_target_components":["88:12"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:12","target_evidence":{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},"target_ref":"88:12"},{"connection_evidence_ref":"conn_ev_040877e32ac320e6aa89","connection_ref":"conn_c1407baf7e05e9cb9413","note":"Immediate continuation adds spread furnishings to the prepared setting.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_39b87c81ba1feb53aace","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:16","source_note":"Placed cups complete the deliberate spatial order around the carpets.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:16","source_target_components":["88:16"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:16","target_evidence":{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"},"target_ref":"88:16"},{"connection_evidence_ref":"conn_ev_52b3c3ac8838529ec0de","connection_ref":"conn_035dd788a83beb819cde","note":"Immediate high-garden frame qualifies the placement as part of the favorable scene.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_2751ed81c3250c61a48c","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:10","source_note":"The placed cups further show a ready, accessible garden interior.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:10","source_target_components":["88:10"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:10","target_evidence":{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},"target_ref":"88:10"},{"connection_evidence_ref":"conn_ev_25c020831bd934ff7ddf","connection_ref":"conn_6f4684eae78932fad047","note":"Pleasure with effort gives only broad favorable-scene context.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_fd81645d33873df3c2d3","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:9","source_note":"Adds a minor immediate-scene furnishing detail.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:9","source_target_components":["88:9"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:9","target_evidence":{"arabic_uthmani":"لِّسَعْيِهَا رَاضِيَةٌۭ","ayah_ref":"88:9"},"target_ref":"88:9"},{"connection_evidence_ref":"conn_ev_da3f9c3da6aee0792ba6","connection_ref":"conn_ef3f7f3d6cddc31a4146","note":"The opening supplies only distant surah framing.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_35fa3403b57ada71c221","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:1","source_note":"Adjacent cup detail adds no interpretive leverage.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:1","source_target_components":["88:1"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:1","target_evidence":{"arabic_uthmani":"هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ","ayah_ref":"88:1"},"target_ref":"88:1"},{"connection_evidence_ref":"conn_ev_0daaca9d73a18f51b5be","connection_ref":"conn_d3b21f3cd0046c263da4","note":"The afflicted-face scene is a broad contrary backdrop only.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d1946fff4b2534f442e2","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:2","source_note":"The placed cups do not clarify 88:2.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:2","source_target_components":["88:2"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:2","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ","ayah_ref":"88:2"},"target_ref":"88:2"},{"connection_evidence_ref":"conn_ev_637de494d5f8c84f76c7","connection_ref":"conn_fd4ef65a20db91ece2ae","note":"Hunger in the contrary scene sharpens the later scene's prepared provision.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_49956dcf17dc9f07bd65","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:7","source_note":"The cups are part of the immediate contrasting provision.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:7","source_target_components":["88:7"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:7","target_evidence":{"arabic_uthmani":"لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ","ayah_ref":"88:7"},"target_ref":"88:7"},{"connection_evidence_ref":"conn_ev_44335bb4bacac10f2f8c","connection_ref":"conn_a076acbe91a484b870ef","note":"The contrary food scene makes the later prepared drink a marked provision contrast.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_7ae1b9b60dc1f538ae74","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:6","source_note":"No material link to the food or plant reading.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:6","source_target_components":["88:6"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:6","target_evidence":{"arabic_uthmani":"لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ","ayah_ref":"88:6"},"target_ref":"88:6"},{"connection_evidence_ref":"conn_ev_5bfadbbade0c3ee94182","connection_ref":"conn_c675911e30a33435bb3a","note":"Local absence of لَٰغِيَةٌ bounds the weak f04 sound-association reading.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_62e47d1542144a9c0ca2","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:11","source_note":"Immediate furnishing detail only weakly continues the Garden scene.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:11","source_target_components":["88:11"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:11","target_evidence":{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"},"target_ref":"88:11"},{"connection_evidence_ref":"conn_ev_149ce6cca010f179a4ec","connection_ref":"conn_9b8d776b5023fd720e59","note":"Pleasant faces add immediate recipient context for the prepared garden provisions.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_d587a350ab938372f285","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:8","source_note":"Immediate placed vessels further materialize the ease-setting.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:8","source_target_components":["88:8"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:8","target_evidence":{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"},"target_ref":"88:8"},{"connection_evidence_ref":"conn_ev_73ae228b10ff10b82af9","connection_ref":"conn_dc1fc41fab55b1f1162b","note":"Toil and exhaustion form a broad contrary backdrop to the favorable provisions.","origin":"authored_focus_row","prior_label":"weak","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":true,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":false,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_872de5f36ba5599a9c14","projection_record_type":"reciprocal_counterevidence","receiving_direction_label":null,"record_type":"reciprocal_counterevidence","relation_scope":"same_surah","source_direction_label":"no value","source_focus_ref":"88:3","source_note":"The placed cups do not clarify the focus.","source_row_role":"ranked_review","source_target_component_ref":"88:14","source_target_components":["88:14"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:14"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:3","source_target_components":["88:3"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:3","target_evidence":{"arabic_uthmani":"عَامِلَةٌۭ نَّاصِبَةٌۭ","ayah_ref":"88:3"},"target_ref":"88:3"}],"focus":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:14:1:1","qac_word_ref":"88:14:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","root_ar":"ك و ب","surface_ar":"أَكْوَابٌ"},{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","root_ar":"و ض ع","surface_ar":"مَّوْضُوعَةٌ"}],"word_analysis_qac_refs":[["88:14:1:1"],["88:14:1:2"],["88:14:2:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:14:1","88:14:2","88:14:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"88:14:1:1","qac_word_ref":"88:14:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"أَكْوَاب","morph_features":"STEM|POS:N|LEM:>akowaAb|ROOT:kwb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:14:1:2","qac_word_ref":"88:14:1","root_ar":"ك و ب","surface_ar":"أَكْوَابٌ"},{"lemma_ar":"مَّوْضُوعَة","morph_features":"STEM|POS:ADJ|PASS|PCPL|LEM:m~awoDuwEap|ROOT:wDE|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"88:14:2:1","qac_word_ref":"88:14:2","root_ar":"و ض ع","surface_ar":"مَّوْضُوعَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:14:1:1"],["88:14:1:2"],["88:14:2:1"]],"word_analysis_refs":["88:14:1","88:14:2","88:14:3"],"word_rows":[{"analysis_record_ref":"88:14:1","analytic_gloss_range_en":"prefixed connector adding the cups to the ongoing garden inventory while preserving the compressed locative frame","analytic_root_gloss_range_en":null,"qac_refs":["88:14:1:1"],"root":{},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"88:14:2","analytic_gloss_range_en":"indefinite plural cups or drinking vessels, foregrounded as ready service equipment rather than beverage or pouring apparatus","analytic_root_gloss_range_en":"cup-vessel language is the locally selected branch; broader lexical branches include instrument, game-object, attachment, drinking-from-a-cup, and body-shape senses that are not activated by this surface","qac_refs":["88:14:1:2"],"root":{"arabic":"ك و ب","transliteration":"k-w-b"},"surface":{"arabic":"أَكْوَابٌۭ","transliteration":"akwābun"}},{"analysis_record_ref":"88:14:3","analytic_gloss_range_en":"passive participial placed-state adjective: the cups are set, positioned, and ready as a collective service arrangement","analytic_root_gloss_range_en":"setting down, putting in place, locating, assigning, lowering, reducing, depositing, and other branch-specific uses; local grammar selects completed placed-state with access and assignment pressure","qac_refs":["88:14:2:1"],"root":{"arabic":"و ض ع","transliteration":"w-ḍ-ʿ"},"surface":{"arabic":"مَّوْضُوعَةٌۭ","transliteration":"mawḍūʿatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":9,"missing_anchor_refs":[],"supplied_unique_anchor_count":9},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["88:14","88:5"],"branch_refs":["root_000063/B003","root_000722/B001","root_001069/B006","root_001328/B005","root_001657/B001"],"candidate_id":"cand_21ab6f111adc25e1acf7","evidence_scope":"declared_pericope","hft_ref":"hft_3c54c8380b468c48597b","item_id":"delta-administered-versus-offered-drink","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-administered-versus-offered-drink","support_id":"sup_bb4f38c1e59003f7f1e8"},{"anchor_refs":["88:10","88:14","88:8"],"branch_refs":["root_001042/B002","root_001328/B001","root_001525/B001","root_001630/B004","root_001657/B005"],"candidate_id":"cand_71ed65cf10ddd214eaab","evidence_scope":"declared_pericope","hft_ref":"hft_65221ad918c963102235","item_id":"delta-downward-service-in-high-estate","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-downward-service-in-high-estate","support_id":"sup_bb11170b199d1277b9b3"},{"anchor_refs":["88:12","88:13","88:14","88:15","88:16"],"branch_refs":["root_000083/B001","root_000240/B006","root_000582/B001","root_000697/B011","root_000871/B001","root_001328/B005","root_001657/B006"],"candidate_id":"cand_675e5254e815286595bb","evidence_scope":"declared_pericope","hft_ref":"hft_e82c542352c138dc0359","item_id":"delta-hydraulic-furnishing-topology","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta-hydraulic-furnishing-topology","support_id":"sup_b336ca74d7f3a9612e27"},{"anchor_refs":["88:11","88:14"],"branch_refs":["root_000741/B007","root_001328/B002","root_001361/B003","root_001657/B001"],"candidate_id":"cand_7b6aa9cfb6d6f93ddab2","evidence_scope":"declared_pericope","hft_ref":"hft_57217d4514b217da18d9","item_id":"outlier-silenced-instrument-shadow","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-silenced-instrument-shadow","support_id":"sup_aad66371219c89c7e1ab"},{"anchor_refs":["88:13","88:14","88:8"],"branch_refs":["root_000697/B011","root_001328/B006","root_001630/B004","root_001657/B006"],"candidate_id":"cand_223d5984fe02c0e63dca","evidence_scope":"declared_pericope","hft_ref":"hft_965d33aa5db61f7461ad","item_id":"outlier-anthropomorphic-cup-stations","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier-anthropomorphic-cup-stations","support_id":"sup_80c7c66001a3ef24eccb"}],"diagnostics":[],"lane_counts":{"global":11,"macro":5,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:14","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:14","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"88:14","lane":"macro","linguistic_source_ref":"88:14","surface_ref":"88:14","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:14","target_tokens":[["Konulmuş",["88:14:2"]],["kadehler",["88:14:1"]],["de",["88:14:1"]],["vardır",["88:14:1"]]],"text":"Konulmuş kadehler de vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":1,"ayah_to":16,"id":"s088-p01-001-016","label":"Faces at the overwhelming event","number":1,"refs":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Noxious Fodder","source_type":"channel","support_id":"sup_1c70b47141e2fa91a60c","text":"Pasture, forage, toxicity, and failed fattening sharpen the surface image of food without nourishment.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"E:Noxious Fodder","source_type":"channel","support_id":"sup_1eb890d50c87f39e9d22","text":"A harmful plant is available as forage but fails to nourish the animal.","trust":"trusted"},{"branch_refs":["root_000744/B001","root_000880/B010","root_000908/B005","root_001657/B007"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"E:Noxious Fodder","source_type":"channel","support_id":"sup_3e0da71c75f0136e8c64","text":"noxious thorny plant `ض ر ع:B005/m01`; camel forage plant `ص ل ي:B010/m01`; camel pasture `و ض ع:B007/m01`; failure to fatten `س م ن:B001/m03`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Noxious Fodder","source_type":"channel","support_id":"sup_3e62797937df4e40d6be","text":"88:6 `ضريع` (`ض ر ع`); 88:4 `تصلى` (`ص ل ي`); 88:14 `موضوعة` (`و ض ع`); 88:7 `يسمن` (`س م ن`)","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_3f0e3fde702f98ff06e2","text":"Resting surface, elevation, support, and placement describe one prepared seat.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_id":"sup_40f4184ec37796a22546","text":"Liquids are held, carried, poured, and accessed through specialized receptacles and fittings.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_id":"sup_4fe7afca88907115e180","text":"A handleless drinking vessel is set in a designated place for use.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_5eab647facb844adf4b6","text":"Soft, ordered supports receive a reclining or seated body.","trust":"trusted"},{"branch_refs":["root_000063/B004","root_001328/B001","root_001328/B005","root_001657/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_id":"sup_80286e18a4bac3c6cffb","text":"handleless cup `ك و ب:B001/m01`; general vessel or container `ء ن ي:B004/m01`; deliberate placement `و ض ع:B001/m01`; drinking from a cup `ك و ب:B005/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"E:Noxious Fodder","source_type":"channel","support_id":"sup_83ada64159fe803dee25","text":"Eating, abstaining, fattening, and livelihood alter whether a body is sustained.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_864db6a36a51e7f5c840","text":"A resting platform is raised, placed, and prepared for reclining.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"macro","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_id":"sup_9a471539b0f28af84ca9","text":"Receptacle, placement, and drinking function form the complete tableware scene stated at the surface.","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_b0038bff32bfbb04660a","text":"88:13 `سرر مرفوعة` (`س ر ر`, `ر ف ع`); 88:15 `مصفوفة` (`ص ف ف`); 88:14 `موضوعة` (`و ض ع`)","trust":"trusted"},{"branch_refs":["root_000582/B001","root_000697/B011","root_000871/B004","root_001657/B001"],"citable":true,"role":"branch_nomination","scope":"macro","source_local_id":"A:Raised Couch and Seat","source_type":"channel","support_id":"sup_cfa66887abd9775cafcb","text":"couch or resting place `س ر ر:B011/m01`; raised placement `ر ف ع:B001/m01`; building or saddle platform `ص ف ف:B004/m01`; settled placement `و ض ع:B001/m01`","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"context_only","scope":"macro","source_local_id":"A:Cup, Vessel, and Placement","source_type":"channel","support_id":"sup_d0bf93f968bbf9e4ba83","text":"88:14 `أكواب موضوعة` (`ك و ب`, `و ض ع`); 88:5 `آنية` (`ء ن ي`)","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ","ayah_ref":"88:5"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000063/B003","root_000722/B001","root_001069/B006","root_001328/B005","root_001657/B001"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001328","role":"Drinking from a cup anchors the revised model in the use latent in the focus object.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Completed placement makes the favorable drink available before any action is demanded of its recipient.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000722","role":"Giving someone drink supplies the contrasting causative relation in which intake is administered.","root":"س ق ي","source_ref":"88:5","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001069","role":"The flowing water source supplies an undivided origin from which the earlier recipients are made to drink.","root":"ع ي ن","source_ref":"88:5","source_word_indices":["3"]},{"branch_id":"B003","mapped_root_id":"root_000063","role":"Reaching full maturity or limit sharpens the source's extreme condition against the neutral readiness of the placed cups.","root":"ء ن ي","source_ref":"88:5","source_word_indices":["4"]}],"changed_reading":{"after":"The cups reverse the earlier drink mechanism: coercive delivery from an extreme source gives way to portioned drink made available without compulsion.","before":"The set cups merely add a pleasant counterpart to an earlier unpleasant drink."},"confidence":"strong","mechanism":"The earlier drink scene couples being made to drink with a spring and a content that has reached an extreme state. Against that apparatus, the focus ayah relocates drinking into vessels already set down. The changed variable is agency: imposed intake from a source becomes unforced access to prepared portions.","model_id":"delta-administered-versus-offered-drink","reader_inference":"The packet supplies administered drinking, a water source, extremity, cup-use, and completed placement; I infer that their opposed grammatical agencies are contrastive. A live alternative is that the scenes contrast only contents and outcomes, with no intended agency contrast.","status":"revised","structural_cues":["88:4-5 forms a fire-to-administered-drink sequence, whereas 88:14 is a verbless display of already prepared objects.","The same ع ي ن source-slot recurs at 88:12 before the cups, allowing the two drink environments to be compared without equating them."],"trigger_roots":["س ق ي","ع ي ن","ء ن ي"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-administered-versus-offered-drink","source_type":"hft","support_id":"sup_bb4f38c1e59003f7f1e8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِى جَنَّةٍ عَالِيَةٍۢ","ayah_ref":"88:10"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_001042/B002","root_001328/B001","root_001525/B001","root_001630/B004","root_001657/B005"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001328","role":"The handleless vessel makes bodily reach especially relevant to where the object is lowered or placed.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B005","mapped_root_id":"root_001657","role":"Lowness of rank and humility supplies a social-vertical shadow to the cups' physical placement.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001630","role":"The face standing for the whole person identifies the beneficiaries whose position is being contrasted with the objects.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001525","role":"Good condition and beneficence supply the recipients' favorable estate.","root":"ن ع م","source_ref":"88:8","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001042","role":"Elevation of rank lets the garden's height operate socially as well as spatially.","root":"ع ل و","source_ref":"88:10","source_word_indices":["3"]}],"changed_reading":{"after":"Within a high estate, the cups' downward placement performs service: status rises for the persons while useful objects are made low and reachable.","before":"Placed means only that the cups occupy a location."},"confidence":"medium","mechanism":"A low-rank or humbling branch of the focus placement word is activated between persons in good condition and a high garden. The apparent contradiction resolves functionally: persons are elevated while service objects descend into reach. Lowness becomes accommodation rather than degradation.","model_id":"delta-downward-service-in-high-estate","reader_inference":"The packet supplies favorable persons, elevation, handleless cups, and a lowness branch of placement; I infer a service relation in which objects are lowered so recipients need not lower themselves. The ordinary alternative is simple location with no social inversion.","status":"new","structural_cues":["88:8 names the persons before 88:10 names the high setting and 88:14 names the placed service objects.","The passive participle leaves the placing agent unexpressed, foregrounding the completed accommodation rather than command."],"trigger_roots":["و ج ه","ن ع م","ع ل و"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-downward-service-in-high-estate","source_type":"hft","support_id":"sup_bb11170b199d1277b9b3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا عَيْنٌۭ جَارِيَةٌۭ","ayah_ref":"88:12"},{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"وَنَمَارِقُ مَصْفُوفَةٌۭ","ayah_ref":"88:15"},{"arabic_uthmani":"وَزَرَابِىُّ مَبْثُوثَةٌ","ayah_ref":"88:16"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000083/B001","root_000240/B006","root_000582/B001","root_000697/B011","root_000871/B001","root_001328/B005","root_001657/B006"],"payload":{"activation_trace":[{"branch_id":"B005","mapped_root_id":"root_001328","role":"Cup-mediated drinking gives the central objects a transfer function rather than a merely decorative one.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001657","role":"Assignment to a determined station makes each cup a node in the surrounding arrangement.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B006","mapped_root_id":"root_000240","role":"Continuing provision or supply gives the upstream flow a sustaining function that the cups can portion.","root":"ج ر ي","source_ref":"88:12","source_word_indices":["3"]},{"branch_id":"B011","mapped_root_id":"root_000697","role":"A place of settled rest identifies the bodies and activity around which the service nodes are arranged.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Physical raising supplies the vertical coordinate immediately before the focus placement.","root":"ر ف ع","source_ref":"88:13","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000871","role":"Alignment on an even line supplies ordered horizontal adjacency after the cups.","root":"ص ف ف","source_ref":"88:15","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000083","role":"Dispersal supplies broad coverage, extending the local cup stations into a complete inhabited surface.","root":"ب ث ث","source_ref":"88:16","source_word_indices":["2"]}],"changed_reading":{"after":"The cups are the middle transfer layer of an engineered hospitality field, connecting continuous supply to elevated rest and distributing access across the furnished surface.","before":"The cups are one furnishing among several."},"confidence":"strong","mechanism":"The sequence around 88:14 moves from continuous flow to resting places raised, cups stationed, cushions aligned, and carpets dispersed. The cups become transfer nodes between a resource and bodies at rest; their placement mediates vertical elevation and horizontal distribution.","model_id":"delta-hydraulic-furnishing-topology","reader_inference":"The packet supplies continuous provision, rest, elevation, stationing, alignment, and dispersal; I infer a functional topology in which cups transfer flow to resting occupants. A live alternative is a noncausal catalogue whose spatial verbs signal abundance only.","status":"strengthened","structural_cues":["88:12-16 is an uninterrupted sequence of source, resting furniture, cups, cushions, and floor coverings.","The four object lines 88:13-16 use parallel indefinite nouns followed by feminine passive participles.","The participles progress through raised, placed, aligned, and dispersed, giving placement a distinct middle operation."],"trigger_roots":["ج ر ي","س ر ر","ر ف ع","ص ف ف","ب ث ث"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta-hydraulic-furnishing-topology","source_type":"hft","support_id":"sup_b336ca74d7f3a9612e27","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ","ayah_ref":"88:11"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000741/B007","root_001328/B002","root_001361/B003","root_001657/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001328","role":"The drum or reed-instrument image supplies a latent sonic object behind the ordinary cup surface.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001657","role":"Setting the object down lets the activated instrument-shadow be physically stilled.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000741","role":"Pleasurable hearing and music make the absent sonic channel specific enough to activate the instrument branch.","root":"س م ع","source_ref":"88:11","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001361","role":"Mixed noisy sound supplies what the scene excludes, turning set-down sonic objects into an image of tranquility.","root":"ل غ و","source_ref":"88:11","source_word_indices":["4"]}],"changed_reading":{"after":"At the level of lexical shadow, even an instrument latent in the cup-root has been laid down: abundance remains, but clamor is disarmed.","before":"The absence of idle sound and the presence of cups are unrelated comforts."},"confidence":"exploratory","containment":"This is surprising because the surface plural ordinarily identifies drinking cups, while the cited ك و ب branch names a music instrument. It remains valid as a root-branch and sonic activation under the nearby negation of heard noise: an instrument-shadow can be imagined as laid down and inactive. Downstream prose must mark this as lexical resonance, never translate أَكْوَابٌ as instruments.","focus_anchor":"The instrument branch belongs to the focus root ك و ب, and the placement participle can materially render sonic potential as set down.","outlier_id":"outlier-silenced-instrument-shadow"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-silenced-instrument-shadow","source_type":"hft","support_id":"sup_aad66371219c89c7e1ab","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ","ayah_ref":"88:13"},{"arabic_uthmani":"وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ","ayah_ref":"88:14"},{"arabic_uthmani":"وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ","ayah_ref":"88:8"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000697/B011","root_001328/B006","root_001630/B004","root_001657/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001328","role":"A thin neck and enlarged head supply an anthropomorphic silhouette latent in the cup-root.","root":"ك و ب","source_ref":"88:14","source_word_indices":["1"]},{"branch_id":"B006","mapped_root_id":"root_001657","role":"Persons assigned to a fixed place let the repeated vessel silhouettes be imagined as stationed bodies.","root":"و ض ع","source_ref":"88:14","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001630","role":"The face as a stand-in for the person supplies the nearby bodily scale for the visual analogy.","root":"و ج ه","source_ref":"88:8","source_word_indices":["1"]},{"branch_id":"B011","mapped_root_id":"root_000697","role":"A resting or reclining place situates bodies near the stationed cup silhouettes.","root":"س ر ر","source_ref":"88:13","source_word_indices":["2"]}],"changed_reading":{"after":"As a visual-material outlier, their necked silhouettes and assigned stations echo the resting occupants, making service objects into quiet proxies for a fully populated scene.","before":"The cups are inert objects beside human occupants."},"confidence":"exploratory","containment":"This is surprising because thin-necked, large-headed morphology is a remote descriptive branch and cups are not persons. It remains materially anchored in the vessel silhouettes and in the focus root's own assigned-person branch, while faces and resting places provide nearby bodily cues. Downstream prose must qualify it as visual anthropomorphism, not lexical personification or doctrine.","focus_anchor":"The cup root contains a thin-necked, large-headed profile, and the placement root contains persons assigned to positions.","outlier_id":"outlier-anthropomorphic-cup-stations"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier-anthropomorphic-cup-stations","source_type":"hft","support_id":"sup_80c7c66001a3ef24eccb","trust":"legacy_unbound"}]}
</lane_packet_json>
