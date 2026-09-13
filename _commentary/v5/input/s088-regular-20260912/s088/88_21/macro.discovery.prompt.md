# Commentary v5 scope discovery

You are the fresh **macro** scope discoverer for **88:21**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s088-regular-20260912/s088/88_21/macro.discovery.json` and modify nothing
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
  "ayah_ref": "88:21",
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
{"branch_registry":[{"boundary":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"erkek cinsiyet ve erkek yavru doğurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeklik karşıtlığını ve buna bağlı doğurma türetimlerini birlikte göstermek gereken genel açıklamalarda kullanılır.","boundary_detail":"Dalın çekirdeği biyolojik erkeklik karşıtlığıdır; doğum ve benzetme anlatımları ancak kendi sözlüksel yapıları içinde geçerlidir.","branch_image_ar":"الذكر خلاف الأنثى","concept_gloss":"erkek cinsiyet ve erkek yavru doğurma","contextual_glosses":[{"applicability":"Bir insanın ya da hayvanın dişinin karşıtı olan cinsiyeti belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Erkek yavru doğurmaya ilişkin türemiş kullanım alanını dışarıda bırakır.","preserves":"Bireyin erkek cinsiyetinden olması anlamını korur."},"facet_ids":["F001","F002"],"text":"erkek","usage_role":"general"},{"applicability":"Bir dişinin doğurduğu yavrunun erkek olduğunu bildiren çekimli yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel erkek cinsiyet kategorisini ve çoğul adlandırmaları kapsamaz.","preserves":"Doğum sonucunun erkek yavru olması anlamını korur."},"facet_ids":["F003"],"text":"erkek yavru doğurmak","usage_role":"contextual"}],"definition":"Canlıların dişinin karşısında yer alan erkek cinsiyetinden olmasıdır. Bu çekirdeğe bağlı biçimler, erkek yavru dünyaya getirmeyi veya bunu alışkanlıkla yapmayı da anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve hayvanlarda dişinin karşıtı olan erkek cinsiyet kategorisini belirtir."},{"facet_id":"F002","role":"extension","statement":"Erkek bireylerin çoğulunu ve erkek olma durumunu adlandıran biçimleri kapsar."},{"facet_id":"F003","role":"specialization","statement":"Belirli çekimli biçimlerde bir dişinin erkek yavru doğurmasını veya çoğunlukla erkek yavru doğurmasını anlatır."}],"identity_rationale":"Kaynak ifadesi dalın merkezini dişinin karşıtı olan erkek cinsiyet olarak kurar; çoğul adları ve erkek yavru doğurma anlatımları bu merkeze bağlı türetimlerdir. Ayrı sözlüksel birimlerde görülen anatomi ve erkeğe benzetme kullanımları çekirdek tanımı genişletmez.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"erkek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"erkek üreme organı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"erkeğin üreme organı çevresindeki organlar"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"erkekler veya erkeklik"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"erkek yavru doğurdu"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"çoğunlukla erkek yavru doğuran dişi"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"erkek yapılı kadın veya dişi deve"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"gebe için kolay doğum ve erkek çocuk dileği"}],"lexicalization_note":"Tanım erkek cinsiyet çekirdeğini korur; doğurma, anatomi ve benzetme anlamları yalnız ilgili çekimli biçim ya da söz öbeğiyle sınırlandırılır.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; dört belirgin karşıtlık veya sınır ilişkisi seçildi, kalanlar anatomi, gelişim, bellek, söz ve belge alanlarında uzak ya da yinelenen eşleşmelerdi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Aynı cinsiyet ekseninde doğrudan karşıttırlar; biri erkek, öteki dişi tarafını seçer.","focus_only":"Odak dalı erkek cinsiyetini ve ona bağlı erkek yavru doğurma biçimlerini anlatır.","gloss":"erkek ile dişi","neighbor_only":"Komşu dal dişi cinsiyetini ve dişiliğe bağlı biçimleri anlatır.","neighbor_ref":"root_000058/B001","relation_type":"antonym","shared_zone":"İki dal canlıların biyolojik cinsiyet ayrımının karşıt uçlarını adlandırır."},{"boundary_match":"partial","distinction":"Odak biyolojik kategoridir ve hayvanları da kapsar; komşu ise insan kişisini ve toplumsal nitelendirmeleri öne çıkarır.","focus_only":"Odak, insanlarla sınırlı olmayan erkek cinsiyet kategorisini belirtir.","gloss":"erkek cinsiyet ile erkek kişi","neighbor_only":"Komşu, yetişkin erkek kişiyi ve ona yüklenen erkekçe nitelikleri belirtir.","neighbor_ref":"root_000546/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal insan söz konusu olduğunda erkek olma alanında buluşur."},{"boundary_match":"partial","distinction":"Cinsiyet kategorisi bir bütün olarak bireyi sınıflandırır; komşu ifade yalnız belirli bir organı adlandırır.","focus_only":"Odak dalı canlı bireyin erkek cinsiyetinden olmasını temel alır.","gloss":"erkeklik ile erkek anatomisi","neighbor_only":"Komşu dal yalnız erkek üreme organı için kullanılan örtmeceli bir adı verir.","neighbor_ref":"root_000597/B007","relation_type":"near_neighbor","shared_zone":"İki dal erkek cinsiyetle ilişkili bedensel alana temas eder."},{"boundary_match":"field_only","distinction":"Birinci dal cinsiyet sınıflamasıdır; ikinci dal ise cinsiyetten bağımsız varlıklara aktarılabilen güç ve sertlik niteliğidir.","focus_only":"Odak dalı gerçek erkek cinsiyetini ve buna bağlı doğum biçimlerini anlatır.","gloss":"erkeklik ile güçlü sertlik","neighbor_only":"Komşu dal nesne, bitki, insan veya olaylara yüklenen sertlik ve güç niteliğini anlatır.","neighbor_ref":"root_000516/B002","relation_type":"same_field","shared_zone":"Aynı kökten gelen iki dal bazı niteleme biçimlerinde erkeklik çağrışımını paylaşır."}],"source_phrase_ar":"الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)","source_summary":"Kaynaklar erkek ile dişi arasındaki temel karşıtlıkta birleşir; ayrıca erkekler için kullanılan çoğul biçimleri ve erkek yavru doğurmaya ilişkin türetimleri aynı anlam alanına bağlar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكر والذكورة والذكران وولادة الذكور والمذكار وما شبه بالذكر في الخلقة.","what_is_not_ar":"لا يدخل فيه مجرد التذكر أو الذكر باللسان ولا الصيت والشرف."},"support_links":[]},{"boundary":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B002","candidate_links":[{"candidate_id":"cand_84cf4ca370f3d9ffc3b6","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"sert, keskin ve güçlü olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel sertlik ile kişi ve durumlara aktarılan yoğun güç anlamlarını birlikte açıklarken kullanılır.","boundary_detail":"Anlam bir cinsiyet adı değil, yalnız belirli söz öbeklerinde nesneye veya duruma yüklenen sertlik, keskinlik ve güç niteliğidir.","branch_image_ar":"صلابة الذكر وحدته وشدته","concept_gloss":"sert, keskin ve güçlü olma","contextual_glosses":[{"applicability":"Demir, bitki veya benzeri maddi bir varlığın kuru, kalın ve dayanıklı yapısı anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kılıçtaki keskinliği ve kişi ya da olaylara aktarılan güç anlamını dışarıda bırakır.","preserves":"Maddi varlıktaki güçlü sertlik ve dayanıklılık niteliğini korur."},"facet_ids":["F001","F002"],"text":"çok sert ve dayanıklı","usage_role":"contextual"},{"applicability":"Kişi, gün, yol, felaket, yağmur, söz veya şiir yoğunluk ve zorluk bakımından nitelenirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Metal ve bitkideki somut sertlik ile kılıçtaki keskinliği kapsamaz.","preserves":"Aktarmalı güç, şiddet ve zorluk anlamını korur."},"facet_ids":["F001","F003"],"text":"çetin ve güçlü","usage_role":"contextual"}],"definition":"Belirli varlıkların sert, kuru, keskin, güçlü veya çetin oluşunu bildiren bir nitelemedir. Metal ve bitkide fiziksel dayanıklılığı, kişi, olay, hava ve sözde ise yoğun güç ya da zorluğu anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığa güçlü sertlik, keskinlik veya çetinlik niteliği yükler."},{"facet_id":"F002","role":"specialization","statement":"Demirin en sert ve kuru türünü, kılıcın keskinliğini ve bitkinin kalın sert yapısını belirtir."},{"facet_id":"F003","role":"extension","statement":"Kişi, gün, yol, felaket, yağmur, söz ve şiir için güç, şiddet veya zorluk anlatan aktarmalı bir niteleme olur."}],"identity_rationale":"Kaynak ifadesi demir, kılıç ve sert bitkilerdeki somut sertlik ile insan, gün, yol, felaket, yağmur, söz ve şiire aktarılan güç ve şiddeti aynı niteleme dalında toplar. Geçici çerçeve bu yapıyı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"demirin en sert ve kuru türü"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"keskin ve sağlam kılıç"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"kılıcın veya erkeğin keskinliği"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kalın ve sert otlar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"güçlü, yiğit ve onurlu adam"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çetin ve korkutucu gün, yol veya felaket"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"şiddetli yağmur, sağlam söz veya güçlü şiir"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova"}],"lexicalization_note":"Somut ve aktarmalı nitelikler ayrı yüzler olarak korunur; hiçbiri bağlamdan bağımsız genel bir kök anlamı gibi sunulmaz.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; en açıklayıcı beş karşıt veya yakın sınır seçildi, öteki adaylar hava, madde ve kardeş dallar bakımından daha uzak ya da yinelenendi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak güçlü ve keskin ucu, komşu ise yumuşak ve zayıf ucu seçtiği için doğrudan karşıttırlar.","focus_only":"Odak dalı sertlik, keskinlik, güç ve çetinlik niteliğini taşır.","gloss":"sertlik ile yumuşaklık","neighbor_only":"Komşu dal yumuşaklık, kesmeyiş, zayıflık ve edilgenlik niteliğini taşır.","neighbor_ref":"root_000058/B002","relation_type":"antonym","shared_zone":"İki dal nesne ve kişilerin güç ile dayanıklılık eksenindeki karşıt uçlarını niteler."},{"boundary_match":"partial","distinction":"Odak keskinlik ve şiddetli durumlara daha açıktır; komşu sıkılık ve darbeye dayanma yeteneğine daha belirgin biçimde bağlıdır.","focus_only":"Odak, keskinlik ile gün, yol, yağmur, söz ve şiirdeki aktarmalı şiddeti de kapsar.","gloss":"çetin sertlik ile dayanıklılık","neighbor_only":"Komşu, darbeye dayanma ve sıkı dokulu sağlamlık gibi bedensel veya maddi dayanıklılığı öne çıkarır.","neighbor_ref":"root_000253/B002","relation_type":"near_synonym","shared_zone":"Her iki dal güçlü, sağlam ve kolay bozulmayan bir niteliği anlatabilir."},{"boundary_match":"partial","distinction":"Komşu kılıca özgü dar bir nitelemedir; odak ise aynı özelliği daha geniş bir varlık ve durum dizisine taşır.","focus_only":"Odak metal dışındaki varlıkları ve aktarmalı güç nitelemelerini de kapsar.","gloss":"genel sertlik ile keskin kılıç","neighbor_only":"Komşu yalnız bir kılıcın keskin ve kesici olmasını niteler.","neighbor_ref":"root_000258/B009","relation_type":"near_synonym","shared_zone":"Kılıç söz konusu olduğunda iki dal keskinlik ve güçlü kesme niteliğinde buluşur."},{"boundary_match":"partial","distinction":"Odak keskin ve çetin oluşa, komşu ise gücün sürmesi ve maddi sağlamlığa doğru ayrışır.","focus_only":"Odak keskinliği ve belirli söz öbeklerindeki çetinlik nitelemesini içerir.","gloss":"sert güç ile kalıcı sağlamlık","neighbor_only":"Komşu kalıcılık, semizlik ve kumaş dayanıklılığı gibi ek gelişmeleri içerir.","neighbor_ref":"root_000973/B007","relation_type":"near_synonym","shared_zone":"Her iki dal güç, sertlik ve dayanıklılık alanında önemli ölçüde örtüşür."},{"boundary_match":"field_only","distinction":"Sertlik niteliği cinsiyet bildirmez; erkek cinsiyet dalı da tek başına güç veya keskinlik yüklemez.","focus_only":"Odak çeşitli varlıklara yüklenen sertlik, güç ve keskinliği anlatır.","gloss":"güç niteliği ile erkek cinsiyet","neighbor_only":"Komşu erkek ile dişi arasındaki biyolojik cinsiyet karşıtlığını anlatır.","neighbor_ref":"root_000516/B001","relation_type":"same_field","shared_zone":"İki dal aynı kökten gelen ve kimi tarihsel nitelemelerde ilişkilenen anlam alanlarına aittir."}],"source_phrase_ar":"سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)","source_summary":"Kaynaklar sert demir, keskin kılıç ve kalın bitki örneklerini temel alır; aynı niteliği güçlü kişiye ve şiddetli ya da çetin olay, yol, hava ve söz anlatımlarına genişletir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحديد الذكر والسيف المذكر وذكور البقل وما وصف بالشدة والقوة كالرجل الذكر واليوم والطريق والداهية والمطر.","what_is_not_ar":"لا يدخل فيه الذكر بمعنى الحفظ أو الكلام أو الكتاب."},"support_links":["sup_265dad3a27c0e243af97"]},{"boundary":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B003","candidate_links":[{"candidate_id":"cand_b78e12f6673ad80c667a","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"akılda tutma ve yeniden hatırlama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bellekte koruma durumunu hem de unutulanı etkin biçimde geri çağırma sürecini birlikte anlatır.","boundary_detail":"Bu dal zihindeki koruma ve geri çağırmayla sınırlıdır; bir sözü yalnız ağızdan söylemek veya kamuya duyurmak bu çekirdeğe girmez.","branch_image_ar":"استحضار الشيء بعد النسيان أو مع الحفظ","concept_gloss":"akılda tutma ve yeniden hatırlama","contextual_glosses":[{"applicability":"Unutulmuş veya o sırada düşünülmeyen bir şey yeniden bilince geldiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bilgiyi sürekli akılda tutma ve ezber için çalışma yüzlerini dışarıda bırakır.","preserves":"Bilgiyi yeniden bilince getirme eylemini doğal biçimde korur."},"facet_ids":["F002"],"text":"hatırlamak","usage_role":"general"},{"applicability":"Bir bilgi ya da yükümlülüğün unutulmadan bellekte korunması istendiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Unutulanı etkin olarak geri çağırma ve arama sürecini kapsamaz.","preserves":"Bilginin bellekte hazır ve korunmuş bulunması anlamını korur."},"facet_ids":["F001"],"text":"aklında tutmak","usage_role":"contextual"}],"definition":"Bir şeyi unutmayacak biçimde zihinde tutmak veya unutulan bilgiyi yeniden bilince getirmektir. Buna bağlı kullanımlar, kayıp bilgiyi aramayı ve belleği korumak için çalışmayı da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir bilginin zihinde korunması ve unutmanın karşıtı olarak hazır bulunmasıdır."},{"facet_id":"F002","role":"core","statement":"Unutulmuş veya gözden uzaklaşmış bir bilgiyi yeniden bilince getirme eylemidir."},{"facet_id":"F003","role":"specialization","statement":"Kaybolan bilgiyi zihinde arama ve öğrenileni bellekte tutmak için çalışma süreçlerini kapsar."}],"identity_rationale":"Kaynak ifadesi unutmanın karşıtı olarak bir şeyi zihinde tutmayı, unutulanı yeniden bilince getirmeyi ve kaybolan bilgiyi arayıp bulmayı birlikte verir. Geçici çerçeve zihinsel süreç ile korunmuş bellek durumunu doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"hatırladı veya aklında tuttu"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"aklında"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"hatırlama"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"ezberlemek için çalışma"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Zihinsel çekirdek korunur; akılda olma, yeniden hatırlama, ezber çalışması ve iyi bellek nitelemeleri kendi yapılarına bağlı yüzlerdir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; bellek eksenini en iyi açıklayan beş ilişki seçildi, tanıma, düşünme, eski tanışıklık ve diğer kardeş dallar daha uzak veya yinelenen kaldı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak bellekte varlık ve erişimi, komşu ise aynı varlık ve erişimin kaybını bildirir.","focus_only":"Odak bir bilginin bellekte bulunmasını veya yeniden bilince gelmesini anlatır.","gloss":"hatırlama ile unutma","neighbor_only":"Komşu bir bilginin bellekten kaybolmasını ve sahibince erişilememesini anlatır.","neighbor_ref":"root_000913/B004","relation_type":"antonym","shared_zone":"İki dal bilginin bellekte bulunup bulunmaması ekseninde karşı karşıya gelir."},{"boundary_match":"partial","distinction":"Komşu daha çok bilginin yerleşik korunmasına, odak ise hem korumaya hem yeniden geri çağırmaya uzanır.","focus_only":"Odak unutulan bilgiyi etkin biçimde geri çağırma sürecini de içerir.","gloss":"hatırlama ile bellekte saklama","neighbor_only":"Komşu işitilen veya öğrenilen şeyin zihinde sağlam biçimde yerleşmesini öne çıkarır.","neighbor_ref":"root_000342/B002","relation_type":"near_synonym","shared_zone":"Her iki dal bilginin unutulmadan zihinde bulunması alanında örtüşür."},{"boundary_match":"partial","distinction":"Ezbere bilme dış kaynağa ihtiyaç duymayan yerleşik öğrenmeyi gerektirir; odak böyle bir öğrenme koşulu olmadan da hatırlamayı kapsar.","focus_only":"Odak genel olarak akılda tutmayı ve unutulanı hatırlamayı kapsar.","gloss":"hatırlama ile ezbere bilme","neighbor_only":"Komşu bir metne bakmadan ezbere bilme durumuyla sınırlıdır.","neighbor_ref":"root_000970/B019","relation_type":"near_neighbor","shared_zone":"İki dal bilginin zihinde hazır bulunması bakımından buluşur."},{"boundary_match":"partial","distinction":"Komşu bir çalışma yöntemi ve yineleme sürecidir; odak ise yönteme bağlı olmadan bellek durumu ile geri çağırmayı anlatır.","focus_only":"Odak bilginin zihinde bulunması veya geri çağrılması sonucunu içerir.","gloss":"hatırlama ile zihinsel yineleme","neighbor_only":"Komşu bir sözü belleğe yerleştirmek için içten yineleme eylemini öne çıkarır.","neighbor_ref":"root_000562/B006","relation_type":"near_neighbor","shared_zone":"İçten yineleme, bilginin hatırlanmasını ve bellekte tutulmasını destekleyebilir."},{"boundary_match":"partial","distinction":"Odak zihinsel sonuç ve süreçtir; komşu bu sonucu meydana getiren neden veya hatırlatıcıdır.","focus_only":"Odak kişinin zihninde gerçekleşen hatırlama ve akılda tutma durumudur.","gloss":"hatırlama ile hatırlatma","neighbor_only":"Komşu bir başkasında ya da kişinin kendisinde hatırlamayı doğuran uyarı, araç veya eylemdir.","neighbor_ref":"root_000516/B009","relation_type":"near_neighbor","shared_zone":"İki dal unutulan bilginin yeniden zihinde hazır olması sonucunda buluşur."}],"source_phrase_ar":"ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)","source_summary":"Kaynaklar unutmanın karşıtı olan zihinsel korumayı, unutulanı geri çağırmayı ve kaybolan bilgiyi yeniden bulma çabasını tek bir bellek alanında toplar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الحفظ والاستحضار بالقلب والتذكر والاستذكار وما يكون خلاف النسيان.","what_is_not_ar":"لا يدخل فيه مجرد جريان اللفظ على اللسان إذا لم يقصد حضور المعنى في النفس."},"support_links":["sup_d78a84e1907e7bcf5380"]},{"boundary":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_kind":"collocation","branch_ref":"root_000516/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"bir şeyi sözle anma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişi, nesne veya konunun dilde adlandırılması ve söz konusu edilmesi gereken yapılarda kullanılır.","boundary_detail":"Dal yalnız sözle anma yapısı içinde geçerlidir; içten hatırlama, genel konuşma yetisi ve anılmanın doğurduğu ün ayrı dallardır.","branch_image_ar":"جريان الذكر على اللسان","concept_gloss":"bir şeyi sözle anma","contextual_glosses":[{"applicability":"Bir kişi ya da şeyin adı konuşma içinde geçirildiğinde doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Her türlü söz sayılabilen geniş kaynak açıklamasını ve özel çekiştirme kullanımını belirtmez.","preserves":"Bir şeyi söz içinde adlandırma ve söz konusu etme eylemini korur."},"facet_ids":["F001","F002"],"text":"anmak","usage_role":"general"},{"applicability":"Bir insanın eksik ve kusurlarından o yokken söz etme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tarafsız veya olumlu sözle anma çekirdeğini dışarıda bırakır.","preserves":"İnsanları kusurlarıyla anma biçimindeki olumsuz özel kullanımı korur."},"facet_ids":["F003"],"text":"arkasından kusurlarını söylemek","usage_role":"contextual"}],"definition":"Bir şeyi dil aracılığıyla söz konusu etmek, adını söylemek veya sözle görünür kılmaktır. İnsanların kusurlarını arkalarından söyleme, bu eylemin olumsuz bağlama bağlı bir türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, nesne veya konuyu dilde söz olarak geçirmek ve adını söylemektir."},{"facet_id":"F002","role":"extension","statement":"Söz aracılığıyla bir şeyi bildirme veya görünür kılma yönünü taşır."},{"facet_id":"F003","role":"associated_use","statement":"İnsanların kusurlarından arkalarında söz etme bağlamında çekiştirme anlamına gelir."}],"identity_rationale":"Kaynak ifadesi bir şeyin dilde söz olarak geçirilmesini merkeze alır ve kusur söyleyerek çekiştirmeyi bağlama bağlı bir alt kullanım olarak verir. Her sözün bu adla anılabileceği geniş açıklama, dalı bütün konuşma eylemleriyle özdeşleştirmeden yorumlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sözle anma"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"insanların arkasından kusurlarını söyleme"}],"lexicalization_note":"Tanım açıkça sözle anma yapısına bağlı tutulur; çekiştirme anlamı yalnız insanlardan kusurlarıyla söz etme bağlamında verilir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; konuşma, övgü, yerme, hatırlama ve ünle en yararlı beş sınır seçildi, diğerleri özel konuşma türleri veya uzak kardeş anlamlardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Dile getirme genel bir konuşma eylemidir; sözle anma ise belirli bir içeriği adlandırıp konu etmeye bağlıdır.","focus_only":"Odak belirli bir kişi, nesne veya konuyu söz içinde anmayı gerektirir.","gloss":"sözle anma ile dile getirme","neighbor_only":"Komşu, belirli bir içeriği anma koşulu olmadan konuşma seslerini dışa vurmayı anlatır.","neighbor_ref":"root_001364/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal düşüncenin dil ve ses aracılığıyla dışarı çıkarılmasını içerir."},{"boundary_match":"partial","distinction":"Övme zorunlu olarak olumlu değer yükler; odak dalı ise değer yönü taşımadan yalnız söz konusu etmeyi de kapsar.","focus_only":"Odak olumlu, tarafsız veya olumsuz olabilen genel sözle anmayı kapsar.","gloss":"anma ile övme","neighbor_only":"Komşu bir kişiyi en iyi nitelikleriyle överek yüceltme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övme sırasında kişi olumlu özellikleriyle söz içinde anılır."},{"boundary_match":"partial","distinction":"Odaktaki olumsuz kullanım arkadan kusur söylemeyle sınırlıdır; komşu daha geniş yerme ve saldırı davranışlarını içerir.","focus_only":"Odak tarafsız ve olumlu sözle anmayı da kapsayan daha geniş bir eylemdir.","gloss":"kusurla anma ile yerme","neighbor_only":"Komşu kusur arama, küçümseme ve gizli ya da açık saldırı yollarını içerir.","neighbor_ref":"root_001376/B001","relation_type":"near_neighbor","shared_zone":"İki dal bir kişiyi kusurları üzerinden söz konusu etme bağlamında örtüşebilir."},{"boundary_match":"partial","distinction":"Hatırlama zihinsel bir durum veya süreçtir; sözle anma ise dışa vurulan dilsel eylemdir.","focus_only":"Odak içeriğin dil aracılığıyla dışa vurulmasını gerektirir.","gloss":"sözle anma ile hatırlama","neighbor_only":"Komşu içerik söylenmese bile onun zihinde korunması veya geri çağrılmasıdır.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"Bir şeyi hatırlamak, onun daha sonra sözle anılmasına eşlik edebilir."},{"boundary_match":"partial","distinction":"Odak tekil dilsel eylemdir; komşu bu tür anmaların toplumsal sonucu olan kalıcı itibardır.","focus_only":"Odak bir kişi veya şeyden söz etme eylemini anlatır.","gloss":"anma eylemi ile iyi ün","neighbor_only":"Komşu sürekli ve olumlu anılmanın doğurduğu iyi ün, onur ve saygınlığı anlatır.","neighbor_ref":"root_000516/B007","relation_type":"near_neighbor","shared_zone":"Bir kişinin toplum içinde anılması onun ününün oluşmasına katkı sağlayabilir."}],"source_phrase_ar":"ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)","source_summary":"Kaynaklar bir şeyin dilde söz olarak geçirilmesini ortak çekirdek sayar; insanları kusurlarıyla anmayı ise bağlama bağlı olumsuz bir kullanım olarak ekler.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه ذكر الشيء باللسان والقول والإظهار والتسمية، ومنه ذكر الناس بخير أو بسوء إذا دل السياق.","what_is_not_ar":"لا يدخل فيه الحفظ القلبي وحده ولا الشرف والصيت الناتج عن الذكر."},"support_links":[]},{"boundary":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"Tanrı'yı kulluk amacıyla anma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanrı'ya yönelen yakarış, övgü, şükür, itaat ve dinî okuma eylemlerini ortak bir kulluk kavramında toplar.","boundary_detail":"Her sözlü anma bu dala girmez; eylemin Tanrı'ya yönelmiş bir kulluk, övgü, yakarış veya itaat niteliği taşıması gerekir.","branch_image_ar":"ذكر الله عبادة وثناء ودعاء","concept_gloss":"Tanrı'yı kulluk amacıyla anma","contextual_glosses":[{"applicability":"Tanrı'ya bilinçli biçimde yönelen övgü, yakarış veya kulluk eylemi genel olarak belirtilirken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Buyruklara uyma ve dinî metin okuma gibi davranışsal gerçekleşmeleri açıkça belirtmez.","preserves":"Tanrı'ya yönelen bilinçli anma ve kulluk çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"Tanrı'yı anmak","usage_role":"general"},{"applicability":"Kulluğun sözlü yakarış, övgü ve yüceltme yönü bağlamda baskın olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Şükretme, itaat ve dinî okuma gibi öteki gerçekleşmeleri kapsamaz.","preserves":"Yakarış, övgü ve yüceltme biçimindeki kulluk eylemlerini korur."},"facet_ids":["F002"],"text":"yakarışta ve övgüde bulunmak","usage_role":"contextual"}],"definition":"Tanrı'yı kulluk amacıyla anmak; ona yönelen yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma eylemlerini yerine getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı'ya yönelmiş bir kulluk ve bilinçli anma eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Yakarış, övgü, yüceltme ve şükretme bu kulluk yöneliminin sözlü veya içsel biçimleridir."},{"facet_id":"F003","role":"extension","statement":"Buyruklara uyma ve dinî metni bu amaçla okuma da aynı kulluk alanında değerlendirilir."}],"identity_rationale":"Kaynak ifadesi Tanrı'yı anmaya yönelen kulluk eylemlerini; yakarış, övgü, yüceltme, şükretme, buyruklara uyma ve dinî metin okuma örnekleriyle açıklar. Geçici çerçeve bu ibadet odaklı kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı'yı kulluk, övgü ve yakarışla anma"}],"lexicalization_note":"Genel kulluk anlamı ile Tanrı'yı anma söz öbeği ayrılır; dinî metin okuma ancak bu kulluk yönelimi içinde değerlendirilir.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; genel anma, belirli yakarışlar ve ibadet sessizliğiyle ilgili dört ilişki seçildi, kalan adaylar aynı sahnenin daha uzak parçalarıydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Genel sözle anma yalnız dilsel eylemdir; odak dalı ise belirli bir yöneliş ve kulluk amacı gerektirir.","focus_only":"Odak Tanrı'ya yönelmiş kulluk, yakarış, övgü ve itaat koşulunu taşır.","gloss":"kulluk amacıyla anma ile sözle anma","neighbor_only":"Komşu herhangi bir kişi, nesne veya konuyu söz içinde anmayı kapsar.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Tanrı'yı sözle anma, her iki dalın kesişebildiği bir gerçekleşmedir."},{"boundary_match":"thematic_only","distinction":"Belirli kabul dileği kendi kalıplaşmış işlevine sahiptir; odak ise tek bir söz kalıbına bağlı olmayan geniş kulluk alanıdır.","focus_only":"Odak çok sayıda sözlü ve davranışsal kulluk biçimini kapsar.","gloss":"genel kulluk ile kabul dileği","neighbor_only":"Komşu yakarışın kabulü için söylenen belirli bir karşılıkla sınırlıdır.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal yakarış ve dinsel söz eylemi bağlamında aynı sahnede yer alabilir."},{"boundary_match":"thematic_only","distinction":"Komşu isteğin konusunu su ve yağmurla sınırlar; odak ise konu sınırlaması olmayan kulluk yönelimidir.","focus_only":"Odak övgü, şükür, itaat ve farklı yakarış türlerini birlikte kapsar.","gloss":"kulluk ile yağmur dileği","neighbor_only":"Komşu özellikle su ve yağmur istemeye yönelik yakarıştır.","neighbor_ref":"root_000722/B006","relation_type":"thematic","shared_zone":"Yağmur isteme eylemi Tanrı'ya yönelen bir yakarış olarak odak alanında gerçekleşebilir."},{"boundary_match":"thematic_only","distinction":"Sessizlik ibadetin düzenleyici bir koşuludur; odak ise Tanrı'ya yönelen anma ve kulluk eyleminin kendisidir.","focus_only":"Odak anma, yakarış, övgü, okuma ve itaat gibi etkin kulluk biçimleridir.","gloss":"kulluk eylemi ile ibadet sessizliği","neighbor_only":"Komşu ibadet sırasında sıradan konuşmayı bırakıp susma davranışıdır.","neighbor_ref":"root_001260/B004","relation_type":"thematic","shared_zone":"İki dal aynı ibadet ortamında birlikte bulunabilir."}],"source_phrase_ar":"الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)","source_summary":"Kaynaklar Tanrı'yı anmayı ibadet, yakarış ve övgü ekseninde birleştirir; yüceltme, şükretme, itaat ve dinî metin okumayı bu yönelimin farklı gerçekleşmeleri sayar.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الصلاة والدعاء والثناء والتسبيح والشكر والطاعة وقراءة القرآن من حيث هي ذكر لله.","what_is_not_ar":"لا يدخل فيه كل ذكر لساني عام ولا الكتاب المسمى ذكرا إلا من جهة القراءة والعبادة."},"support_links":[]},{"boundary":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_kind":"bare","branch_ref":"root_000516/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"indirildiğine inanılan kutsal kitap","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dinin hükümlerini içeren peygamber kitabı genel bir tür olarak anlatılırken kullanılır.","boundary_detail":"Dal kutsal veya vahyedilmiş sayılan kitabın kendisidir; okuma, çalışma, ibadet ya da zihinsel hatırlama eylemi değildir.","branch_image_ar":"الذكر كتاب منزل أو كتاب دين","concept_gloss":"indirildiğine inanılan kutsal kitap","contextual_glosses":[{"applicability":"Bağlam kitabın dini ve vahyedilmiş niteliğini zaten açıkça gösterdiğinde doğal kısa karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Peygambere indirilme ve önceki kitapları kapsayan üst ad olma ayrıntısını açıkça belirtmez.","preserves":"Dini içerikli ve kutsal kabul edilen kitap olma çekirdeğini korur."},"facet_ids":["F001"],"text":"kutsal kitap","usage_role":"general"}],"definition":"Dinin hükümlerini ve açıklamalarını içeren, bir peygambere indirildiğine inanılan kutsal kitaptır. Kapsam hem Kur'an'ı hem de daha önceki kutsal kitapları içine alabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dinin ayrıntılarını bildiren ve ilahi kaynaklı kabul edilen kitaptır."},{"facet_id":"F002","role":"extension","statement":"Kur'an ile ondan önceki peygamberlere bağlanan kutsal kitapları kapsayan bir üst ad olabilir."}],"identity_rationale":"Kaynak ifadesi dini açıklayan kitabı, peygamberlere indirildiğine inanılan kitapları, Kur'an'ı ve önceki kutsal kitapları aynı dalda toplar. Geçici çerçeve metinsel nesneyi doğru biçimde ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"dinin ayrıntılarını bildiren kutsal kitap"}],"lexicalization_note":"Tanım yalın dalın kutsal kitap anlamını verir; okuma veya ibadetle ilgili söz öbeklerinden yeni bir genel anlam aktarılmaz.","neighbor_coverage_note":"Sunulan on beş adayın tümü değerlendirildi; kitap bölümü, okuma ve çalışmayla ilgili üç sınır seçildi, öteki adaylar ad, görünme, kulluk veya gizli haber alanlarında uzak kaldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak bütün kitap veya kitap türünü, komşu ise onun çevrelenmiş bölümünü adlandırır.","focus_only":"Odak kutsal kitabın bütünü veya kutsal kitap türüdür.","gloss":"kutsal kitap ile kitap bölümü","neighbor_only":"Komşu kutsal metnin sınırları belirlenmiş bir bölümü ve ayrıca yüksek konum anlamıdır.","neighbor_ref":"root_000758/B003","relation_type":"near_neighbor","shared_zone":"Kutsal kitabın belirli bölümleri, bütün metnin yapısal parçalarıdır."},{"boundary_match":"thematic_only","distinction":"Kitap bir nesnedir; okuma ise yalnız kutsal kitaplarla sınırlı olmayan bir eylemdir.","focus_only":"Odak okunan kutsal metinsel nesnenin kendisidir.","gloss":"kutsal kitap ile okuma","neighbor_only":"Komşu metni sesli veya sessiz okuma, başkasına okutma ve birlikte çalışma eylemleridir.","neighbor_ref":"root_001210/B002","relation_type":"thematic","shared_zone":"Kutsal kitap, okuma eyleminin önemli bir nesnesi olabilir."},{"boundary_match":"thematic_only","distinction":"Odak metinsel nesnedir; komşu farklı kitaplara da uygulanabilen öğrenme etkinliğidir.","focus_only":"Odak dini içeriği taşıyan kitabın kendisini adlandırır.","gloss":"kutsal kitap ile metin çalışması","neighbor_only":"Komşu bir kitabı okuyup yineleyerek öğrenme ve belleğe yerleştirme sürecidir.","neighbor_ref":"root_000470/B002","relation_type":"thematic","shared_zone":"Kutsal kitap üzerinde okuma ve öğrenme çalışması yapılabilir."}],"source_phrase_ar":"الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)","source_summary":"Kaynaklar dini açıklayan peygamber kitaplarını ortak çekirdek olarak verir ve kapsamı Kur'an ile önceki kutsal kitaplara kadar genişletir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الكتاب الذي فيه تفصيل الدين وكل كتاب للأنبياء والقرآن والكتب المتقدمة.","what_is_not_ar":"لا يدخل فيه فعل التذكر ولا مطلق الصلاة والدعاء إلا إذا كان اللفظ يدل على الكتاب أو القرآن."},"support_links":[]},{"boundary":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"onur, iyi ün ve saygınlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin olumlu tanınması ile toplumsal yüksekliğini birlikte anlatmak gereken bağlamlarda kullanılır.","boundary_detail":"Dal anma eyleminin kendisi değil, kişinin olumlu biçimde anılmasıyla bağlantılı onur, iyi ün ve saygınlıktır.","branch_image_ar":"ذكر المرء شرف وصيت","concept_gloss":"onur, iyi ün ve saygınlık","contextual_glosses":[{"applicability":"Kişinin insanlar arasında olumlu biçimde tanınıp anılması bağlamda öne çıktığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yüksek konum ve onur bileşenini tek başına açıkça belirtmez.","preserves":"Olumlu tanınma ve insanlar arasında yayılan övgü yönünü korur."},"facet_ids":["F002"],"text":"iyi ün","usage_role":"general"},{"applicability":"Toplumdaki yüksek değer ve itibar, yaygın tanınmadan daha önemli olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Adının yayılması ve övgüyle anılması yönünü açıkça kapsamaz.","preserves":"Kişinin yüksek toplumsal değeri ve saygınlığı anlamını korur."},"facet_ids":["F001"],"text":"onur ve saygınlık","usage_role":"contextual"}],"definition":"Bir kişinin insanlar arasında olumlu biçimde tanınmasından doğan iyi ün, onur, övgü ve yüksek saygınlıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin toplum içinde taşıdığı onur ve yüksek saygınlıktır."},{"facet_id":"F002","role":"core","statement":"Kişinin olumlu biçimde anılmasıyla yayılan iyi ün ve övgüdür."}],"identity_rationale":"Kaynak ifadesi bir kişinin toplum içindeki yüksek konumunu, iyi ününü, övgüyle anılmasını ve saygınlığını ortak bir sonuç alanında toplar. Geçici çerçeve bu toplumsal değer ve yayılmış tanınma bileşimini doğru verir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"onur, iyi ün ve övgü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"belleği güçlü, yiğit veya iyi anılan adam"}],"lexicalization_note":"Yalın iyi ün ve onur anlamı korunur; kişi niteleyen söz öbeği bellek gücü ile iyi anılmayı kendi bağlamında birleştirir.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; iyi ün, güzel anılma, yüce saygınlık, tanınmışlık ve övgüyle ilgili beş sınır seçildi, kalan adaylar daha dar statü türleri veya kardeş dallardı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu yayılan iyi üne daha dardır; odak bu üne onur ve toplumsal yükseklik bileşenini de ekler.","focus_only":"Odak iyi üne ek olarak onur ve yüksek toplumsal konumu da kapsar.","gloss":"onurlu ün ile iyi ün","neighbor_only":"Komşu özellikle insanlar arasında yayılmış güzel ve olumlu ünle sınırlıdır.","neighbor_ref":"root_000890/B002","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin insanlar arasında olumlu biçimde tanınıp anılmasını anlatır."},{"boundary_match":"partial","distinction":"Komşu güzel söz ve övgü sonucuna daha yakındır; odak bunun yanında onur ve yüksek konumu da kurucu sayar.","focus_only":"Odak kişinin yüksek konumunu ve saygınlığını da içerir.","gloss":"saygınlık ile güzel anılma","neighbor_only":"Komşu kişinin insanlar arasında güzel sözle anılması ve övülmesine odaklanır.","neighbor_ref":"root_000804/B004","relation_type":"near_synonym","shared_zone":"İki dal olumlu anılma ve iyi ün alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak iyi anılma ve ünle bağlantılıdır; komşu ün bulunmasa da büyüklük ve otoriteyi ifade edebilir.","focus_only":"Odak yaygın olumlu anılma ve iyi ün bileşenini taşır.","gloss":"iyi ün ile yüce saygınlık","neighbor_only":"Komşu kutsallık, büyüklük, önderlik ve görüş üstünlüğü gibi ek toplumsal boyutlar içerir.","neighbor_ref":"root_001029/B010","relation_type":"near_synonym","shared_zone":"Her iki dal kişinin toplumdaki onur ve yüksek değerini anlatabilir."},{"boundary_match":"partial","distinction":"Tanınmışlık değer bakımından yansız olabilir; odak dalı ise olumlu değerlendirme ve onur taşır.","focus_only":"Odak ünün olumlu, övgüye değer ve onurlu olmasını gerektirir.","gloss":"iyi ün ile tanınmışlık","neighbor_only":"Komşu bir topluluğun veya kişinin olumlu ya da olumsuz değer belirtilmeden tanınır hale gelmesini anlatabilir.","neighbor_ref":"root_000500/B004","relation_type":"near_neighbor","shared_zone":"İki dal bir adın insanlar arasında yayılması ve tanınması alanında buluşur."},{"boundary_match":"partial","distinction":"Komşu bir söz eylemi, odak ise bu ve benzeri değerlendirmelerin toplumsal sonucu olan itibardır.","focus_only":"Odak kişinin kazandığı kalıcı iyi ün ve toplumsal değerdir.","gloss":"iyi ün ile övme","neighbor_only":"Komşu kişiyi iyi özellikleriyle övme eylemidir.","neighbor_ref":"root_000933/B002","relation_type":"near_neighbor","shared_zone":"Övgü eylemi kişinin iyi ününün oluşmasına veya güçlenmesine katkı verebilir."}],"source_phrase_ar":"الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)","source_summary":"Kaynaklar onur ve yüksek konumu, insanlar arasında yayılan iyi ün ve övgüyle birlikte tek bir olumlu toplumsal itibar alanında birleştirir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الشرف والعلاء والصيت والثناء وحسن الذكر.","what_is_not_ar":"لا يدخل فيه مجرد التلفظ باسم الشيء ولا الذكر بمعنى الكتاب إلا إذا صرح بالشرف أو الصيت."},"support_links":[]},{"boundary":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_kind":"collocation","branch_ref":"root_000516/B008","candidate_links":[{"candidate_id":"cand_e87b67e684eeb4305325","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"hakkı gösteren yazılı belge","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir hakkın yazıyla kayda geçirildiği belgeyi veya bu belgelerin çoğulunu açıklarken kullanılır.","boundary_detail":"Anlam bağımsız bir kitap adı değildir; bir hakkı gösteren yazılı belgeyi adlandıran belirli söz öbeğiyle sınırlıdır.","branch_image_ar":"ذكر الحق صك ووثيقة حق","concept_gloss":"hakkı gösteren yazılı belge","contextual_glosses":[{"applicability":"Bağlam belgenin yazılı olduğunu açıkça gösterdiğinde kısa ve doğal karşılık olarak kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yazılı olma niteliğini ve çoğul biçimin tarihsel yapısını açıkça belirtmez.","preserves":"Belgenin belirli bir hakkı gösterme ve kanıtlama işlevini korur."},"facet_ids":["F001"],"text":"hak belgesi","usage_role":"general"},{"applicability":"Birden çok hakkı veya birden çok yazılı kanıtı topluca adlandıran çoğul yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tekil belge kullanımını dışarıda bırakır.","preserves":"Birden çok yazılı hak belgesinin topluca adlandırılmasını korur."},"facet_ids":["F002"],"text":"hak belgeleri","usage_role":"contextual"}],"definition":"Bir hakkın varlığını, sahibini veya koşullarını yazılı olarak gösteren belge ve bu tür belgelerin çoğul adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hakkı yazılı biçimde kayda geçirip kanıtlayan belgedir."},{"facet_id":"F002","role":"extension","statement":"Aynı yapının çoğul biçimi birden çok hak belgesini topluca adlandırır."}],"identity_rationale":"Kaynak ifadesi yalnız belirli hak söz öbeğinde bir hakkı kayda geçiren yazılı belgeyi ve bu belgelerin çoğulunu verir. Geçici çerçeve yapıya bağlı belge anlamını eksiksiz yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakkı gösteren yazılı belge"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yazılı hak belgeleri"}],"lexicalization_note":"Tanım yalnız hak belgesi yapısına ve onun çoğul biçimine bağlanır; yalın köke genel belge anlamı yüklenmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; eş belge, geniş kayıt, genel yazılı kâğıt, hakkın kendisi ve vasiyetle ilgili beş sınır seçildi, kalan adaylar yazma eylemi, pay veya kardeş anlamlarda daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak belgenin belirli bir hakkı göstermesini gerektirir; komşu ise bu koşul olmadan daha genel yazılı belgeleri de kapsar.","focus_only":"Odak yalnız bir hakkı gösteren yazılı belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile yazılı senet","neighbor_only":"Komşu hak bağlantısı zorunlu olmadan yazılı kitap veya senetleri kapsar.","neighbor_ref":"root_000874/B006","relation_type":"near_synonym","shared_zone":"İki dal yazılı senet veya belgeyi adlandırdıklarında örtüşür."},{"boundary_match":"partial","distinction":"Odak hak belgesine daralır; komşu belge türlerini ve resmi kayıt eylemini daha geniş biçimde kapsar.","focus_only":"Odak özellikle bir hakkı gösteren belge yapısıyla sınırlıdır.","gloss":"hak belgesi ile resmi kayıt","neighbor_only":"Komşu kayıt defteri, yükümlülük belgesi, yazılı sayfa ve yargıcın kayda geçirmesi gibi daha geniş kullanımları kapsar.","neighbor_ref":"root_000677/B004","relation_type":"near_synonym","shared_zone":"Her iki dal hakkı veya yükümlülüğü yazılı biçimde güvence altına alan belgeyi anlatabilir."},{"boundary_match":"partial","distinction":"Odak hak ilişkisine bağlıdır; komşu daha genel yazılı nesneyi ve belge dışındaki pay anlamını da içerir.","focus_only":"Odak belgenin belirli bir hakkı kanıtlama işlevini zorunlu kılar.","gloss":"hak belgesi ile yazılı kâğıt","neighbor_only":"Komşu yazılı belge yanında ayrılmış pay ve ödül gibi belge dışı anlamlara da uzanır.","neighbor_ref":"root_001239/B002","relation_type":"near_synonym","shared_zone":"İki dal yazılı bir belge veya kayıt nesnesini adlandırabilir."},{"boundary_match":"field_only","distinction":"Hak hukuki veya toplumsal ilişkidir; belge ise o ilişkinin varlığını gösteren ayrı bir nesnedir.","focus_only":"Odak hakkı kanıtlayan yazılı belgedir.","gloss":"hak belgesi ile hakkın kendisi","neighbor_only":"Komşu kişinin sahip olduğu hakkın veya hak iddiasının kendisidir.","neighbor_ref":"root_000347/B003","relation_type":"same_field","shared_zone":"Belge, kişinin sahip olduğu hakkı kayda geçirir ve kanıtlar."},{"boundary_match":"partial","distinction":"Odak bir hakkı kanıtlar; komşu ise bir kişiye yapılacak işi önceden bildirip emanet eder.","focus_only":"Odak mevcut bir hakkı gösteren yazılı kanıt işlevidir.","gloss":"hak belgesi ile yazılı vasiyet","neighbor_only":"Komşu gelecekte uyulması gereken buyruk veya görevi emanet eden vasiyet ve talimattır.","neighbor_ref":"root_001055/B002","relation_type":"near_neighbor","shared_zone":"İki dal yükümlülük doğurabilen ve korunması gereken yazılı belgeler alanında buluşur."}],"source_phrase_ar":"ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)","source_summary":"Kaynaklar belirli hak söz öbeğini yazılı hak belgesi olarak açıklar ve çoğul biçimin birden çok hak belgesini gösterdiğinde birleşir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه ذكر الحق بمعنى الصك وجمعه ذكور حقوق أو ذكور حق.","what_is_not_ar":"لا يدخل فيه الكتاب الديني المسمى ذكرا ولا التذكرة العامة."},"support_links":["sup_a859b7bac146203ea18e"]},{"boundary":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_kind":"mixed_non_bare","branch_ref":"root_000516/B009","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"},{"candidate_id":"cand_433f025a662154dc3fc1","lane":"macro"},{"candidate_id":"cand_439262cac08c505ea74d","lane":"macro"}],"focus_root_occurrences":[{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","surface_ar":"ذَكِّرْ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","surface_ar":"مُذَكِّرٌ"}],"gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}}],"root_ar":"ذ ك ر","root_id":"root_000516","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hatırlamayı doğuran eylemi, buna yarayan işaret veya nesneyi ve belirli biçime bağlı sık anmayı birlikte açıklamak gereken genel bağlamlarda kullanılır.","boundary_detail":"Dal hatırlamanın kendisi değil, onu doğuran eylem veya araçtır; sık anma anlamı da yalnız kaynakta belirtilen biçime bağlı bir yoğunluk yüzüdür.","branch_image_ar":"الذكرى والتذكرة ما يذكّر","concept_gloss":"hatırlatma, hatırlamayı sağlayan araç ve sıkça anma","contextual_glosses":[{"applicability":"Bir kişide unutulmuş bilginin yeniden zihne gelmesini sağlayan eylem anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatıcı nesne ve sık anma yüzlerini dışarıda bırakır.","preserves":"Hatırlamayı başka bir kişide meydana getiren geçişli eylemi korur."},"facet_ids":["F001"],"text":"hatırlatmak","usage_role":"general"},{"applicability":"Bir ihtiyaç veya bilginin unutulmamasını sağlayan not, işaret ya da nesne anlatılırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Hatırlatma eylemini ve sık anma yoğunluğunu kapsamaz.","preserves":"Hatırlamaya yarayan araç ve işaret işlevini korur."},"facet_ids":["F002"],"text":"hatırlatıcı","usage_role":"contextual"},{"applicability":"Kaynakta yoğunluk bildiren belirli ad biçimi bir şeyi çok kez anmayı anlattığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başkasına hatırlatma ve hatırlatıcı araç anlamlarını dışarıda bırakır.","preserves":"Bir şeyi çok ve yinelenen biçimde anma yoğunluğunu korur."},"facet_ids":["F003"],"text":"sıkça anma","usage_role":"explanatory"}],"definition":"Bir bilginin yeniden zihinde belirmesini sağlamak veya buna yarayan bir işaret ya da araç sunmaktır. Belirli bir biçim ayrıca bir şeyi sıkça anmayı anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir başkasında veya kişinin kendisinde unutulmuş bilginin yeniden hatırlanmasını sağlar."},{"facet_id":"F002","role":"specialization","statement":"Bir ihtiyacı veya bilgiyi hatırlamaya yarayan işaret, not ya da araç olarak gerçekleşir."},{"facet_id":"F003","role":"source_variant","statement":"Belirli bir ad biçiminde bir şeyi sık ve yoğun biçimde anma anlamı taşır."}],"identity_rationale":"Kaynak ifadesi yalnız hatırlatan bir nesneyi değil, başkasında hatırlamayı meydana getirme eylemini, hatırlamaya yarayan aracı ve bazı biçimlerde sık anmayı birlikte verir. Dal korunabilir, ancak geçici nesne merkezli çerçeve bu süreç ve yoğunluk yüzlerini açıkça kapsayacak biçimde genişletilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"hatırlatma, öğüt alma veya sıkça anma"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"hatırlatıcı"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"hatırlatma"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"ona o şeyi hatırlattı"}],"lexicalization_note":"Hatırlatma eylemi, hatırlatıcı araç ve sık anma ayrı yüzler olarak tutulur; bu yapıların hiçbiri yalın zihinsel hatırlamayla özdeşleştirilmez.","neighbor_coverage_note":"Sunulan on dört adayın tümü değerlendirildi; öğüt, uyarı, dikkat çekme, hatırlama ve sözle anmayla ilgili beş sınır seçildi, kalan adaylar öğretme, aktarma, yazı veya yergi alanlarında daha uzaktı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu ahlaki yönlendirme ve duygusal etki taşır; odak bunları gerektirmeyen genel hatırlatma alanıdır.","focus_only":"Odak her tür bilgiyi hatırlatabilir ve bir araç ya da işaret biçiminde gerçekleşebilir.","gloss":"genel hatırlatma ile öğüt","neighbor_only":"Komşu korkutma, sakındırma ve iyi sonuca yöneltme yoluyla kalbi etkileyen öğütle sınırlıdır.","neighbor_ref":"root_001663/B001","relation_type":"near_synonym","shared_zone":"Öğüt, kişiye unuttuğu değer veya sonucu yeniden hatırlatabilir."},{"boundary_match":"partial","distinction":"Uyarma risk ve sakınma yönelimi gerektirir; hatırlatma ise böyle bir değer ve tehlike koşulu taşımaz.","focus_only":"Odak tarafsız, olumlu veya olumsuz herhangi bir bilgiyi yeniden zihne getirebilir.","gloss":"hatırlatma ile uyarma","neighbor_only":"Komşu kişide tehlikeye karşı dikkat ve sakınma meydana getirmeyi amaçlar.","neighbor_ref":"root_000301/B002","relation_type":"near_neighbor","shared_zone":"Bir tehlikeyi hatırlatmak aynı zamanda kişinin dikkatli olmasını sağlayabilir."},{"boundary_match":"partial","distinction":"Komşu soru ve bilgi isteme işlevi taşır; odak ise önceden bilinen içeriğin yeniden hatırlanmasını hedefler.","focus_only":"Odak önceden bilinen bir içeriği yeniden zihne getirmeyi sağlar.","gloss":"hatırlatma ile dikkat çekme","neighbor_only":"Komşu karşıdakinin dikkatini çekip ondan bilgi istemeye yarayan bir söyleyiş kalıbıdır.","neighbor_ref":"root_000531/B013","relation_type":"near_neighbor","shared_zone":"Dikkat çekme, dinleyiciyi belirli bir konuya zihinsel olarak yöneltebilir."},{"boundary_match":"partial","distinction":"Odak sonuç doğuran uyarıcı eylem veya araçtır; komşu ise ortaya çıkan zihinsel durum ve süreçtir.","focus_only":"Odak hatırlamayı meydana getiren dış veya geçişli neden ile aracı anlatır.","gloss":"hatırlatma ile hatırlama","neighbor_only":"Komşu kişinin zihninde bilginin korunması veya yeniden bulunması sürecidir.","neighbor_ref":"root_000516/B003","relation_type":"near_neighbor","shared_zone":"İki dal unutulmuş bilginin yeniden zihinde hazır bulunması sonucunda birleşir."},{"boundary_match":"partial","distinction":"Sözle anma dilsel biçimi gerektirir fakat hatırlatma amacı taşımaz; odak farklı araçlarla gerçekleşebilir ve hatırlama sonucu hedefler.","focus_only":"Odak sözlü olmak zorunda değildir ve temel işlevi bilgiyi yeniden zihne getirmektir.","gloss":"hatırlatma ile sözle anma","neighbor_only":"Komşu belirli bir kişi veya şeyi söz içinde adlandırıp konu etmektir.","neighbor_ref":"root_000516/B004","relation_type":"near_neighbor","shared_zone":"Bir şeyi sözle anmak dinleyene o şeyi hatırlatabilir."}],"source_phrase_ar":"الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)","source_summary":"Kaynaklar hatırlatmayı başkasında hatırlama meydana getiren geçişli eylem ve hatırlamaya yarayan araç olarak verir; ayrıca belirli biçimde sık anma yoğunluğunu kaydeder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الذكرى والتذكير والتذكرة وما يجعل الشيء مذكورا أو يعيد حضوره.","what_is_not_ar":"لا يدخل فيه نفس الحفظ القلبي إلا من حيث النتيجة، ولا الذكر بمعنى الذكران والذكورة."},"support_links":["sup_03e31e82f6f0882615fa","sup_d2df2804962505bc38b9","sup_edc4a8bad16b57ab51d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000065/B001","candidate_links":[{"candidate_id":"cand_b78e12f6673ad80c667a","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0d84b994d39e73733f1a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Return to a destination projects the mnemonic return onto the persons' later trajectory.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000065","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d78a84e1907e7bcf5380"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000318/B001","candidate_links":[{"candidate_id":"cand_b78e12f6673ad80c667a","lane":"macro"},{"candidate_id":"cand_e87b67e684eeb4305325","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_0d84b994d39e73733f1a","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting and account give the later return its evaluative terminus.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]},{"hft_ref":"hft_9b443b710c4d6a40756b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Counting and account provide the later forum in which preserved notice and legible evidence would matter.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000318","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a859b7bac146203ea18e","sup_d78a84e1907e7bcf5380"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000434/B001","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f611b505d15081d6521","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Measuring and proportioning invites inspection of construction rather than bare object recognition.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000434","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_03e31e82f6f0882615fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000582/B001","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f611b505d15081d6521","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Elevation contributes a vertical relation for inquiry.","root":"ر ف ع","source_ref":"88:18","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000582","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_03e31e82f6f0882615fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000703/B001","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f611b505d15081d6521","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"An even extended surface completes the shift from vertical structures to a traversable horizontal field.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000703","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_03e31e82f6f0882615fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000704/B003","candidate_links":[{"candidate_id":"cand_433f025a662154dc3fc1","lane":"macro"},{"candidate_id":"cand_84cf4ca370f3d9ffc3b6","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c8d1daa4eb81b9820469","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The image of a dominating overseer defines the coercive function excluded from reminding.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]},{"hft_ref":"hft_b33efeae5b0ee376292d","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Dominating oversight supplies the excluded extreme that contains sharpness within speech rather than compulsion.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000704","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_265dad3a27c0e243af97","sup_edc4a8bad16b57ab51d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000994/B003","candidate_links":[{"candidate_id":"cand_439262cac08c505ea74d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_76afbd4f7da7196b35e7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Restraint, prevention, and weaning contribute the exploratory idea of interruption before a settled harmful course.","root":"ع ذ ب","source_ref":"88:24","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000994","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d2df2804962505bc38b9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_000994/B005","candidate_links":[{"candidate_id":"cand_439262cac08c505ea74d","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_76afbd4f7da7196b35e7","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Painful punishment preserves the overt endpoint and prevents the weaning image from replacing the source phrase's direct sense.","root":"ع ذ ب","source_ref":"88:24","source_word_indices":["1","3"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_000994","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_d2df2804962505bc38b9"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001390/B001","candidate_links":[{"candidate_id":"cand_433f025a662154dc3fc1","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_c8d1daa4eb81b9820469","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Present-state negation explicitly removes the following supervisory identity from the addressee.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001390","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_edc4a8bad16b57ab51d7"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001507/B001","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f611b505d15081d6521","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Erect and conspicuous setting contributes stability and placement as an observable relation.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001507","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_03e31e82f6f0882615fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001520/B001","candidate_links":[{"candidate_id":"cand_50b4fe7c7366cc8e50fa","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_8f611b505d15081d6521","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"Directing sight or insight supplies the attentional action through which the reminder works.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001520","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_03e31e82f6f0882615fa"]},{"boundary":"No registered branch descriptor is supplied. An exact HFT trace may support an attributed contextual activation, but it does not establish a gloss, facet, or verified lexical identity.","branch_kind":null,"branch_ref":"root_001650/B001","candidate_links":[{"candidate_id":"cand_e87b67e684eeb4305325","lane":"macro"}],"focus_root_occurrences":[],"gloss":null,"hft_citations":[{"hft_ref":"hft_9b443b710c4d6a40756b","qualification":"Exact HFT-attributed role; eligible as attributed contextual evidence, not verified lexicon evidence.","role":"The non-dominant mapped image of a visible identifying mark makes the observed world analogically legible as evidence.","root":"س م و","source_ref":"88:18","source_word_indices":["2"]}],"lexicon_identity_status":"unresolved","registry":"unresolved","review_facets":[],"root_ar":null,"root_id":"root_001650","root_occurrence_qualification":"No registered focus occurrence is supplied. Use only the HFT-cited context coordinate, root, and role for an attributed activation whose contact returns to the focus.","semantic_detail":{},"support_links":["sup_a859b7bac146203ea18e"]}],"candidate_inventory":[{"anchor_refs":["88:17","88:18","88:19","88:20","88:21"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000434/B001","root_000516/B009","root_000582/B001","root_000703/B001","root_001507/B001","root_001520/B001"],"candidate_id":"cand_50b4fe7c7366cc8e50fa","commentary_obligation":"review","hft_ref":"hft_8f611b505d15081d6521","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_observational_how","source_type":"hft","support_ids":["sup_03e31e82f6f0882615fa"],"title":"delta_observational_how","trust":"legacy_unbound"},{"anchor_refs":["88:21","88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B009","root_000704/B003","root_001390/B001"],"candidate_id":"cand_433f025a662154dc3fc1","commentary_obligation":"review","hft_ref":"hft_c8d1daa4eb81b9820469","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_noncoercive_role_boundary","source_type":"hft","support_ids":["sup_edc4a8bad16b57ab51d7"],"title":"delta_noncoercive_role_boundary","trust":"legacy_unbound"},{"anchor_refs":["88:21","88:25","88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000065/B001","root_000318/B001","root_000516/B003"],"candidate_id":"cand_b78e12f6673ad80c667a","commentary_obligation":"review","hft_ref":"hft_0d84b994d39e73733f1a","kind":"context_delta","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:delta_return_before_account","source_type":"hft","support_ids":["sup_d78a84e1907e7bcf5380"],"title":"delta_return_before_account","trust":"legacy_unbound"},{"anchor_refs":["88:21","88:22"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B002","root_000704/B003"],"candidate_id":"cand_84cf4ca370f3d9ffc3b6","commentary_obligation":"review","hft_ref":"hft_b33efeae5b0ee376292d","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_pointed_noncoercive_edge","source_type":"hft","support_ids":["sup_265dad3a27c0e243af97"],"title":"outlier_pointed_noncoercive_edge","trust":"legacy_unbound"},{"anchor_refs":["88:21","88:24"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000516/B009","root_000994/B003","root_000994/B005"],"candidate_id":"cand_439262cac08c505ea74d","commentary_obligation":"review","hft_ref":"hft_76afbd4f7da7196b35e7","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_preventive_weaning","source_type":"hft","support_ids":["sup_d2df2804962505bc38b9"],"title":"outlier_preventive_weaning","trust":"legacy_unbound"},{"anchor_refs":["88:18","88:21","88:26"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"88:21","branch_refs":["root_000318/B001","root_000516/B008","root_001650/B001"],"candidate_id":"cand_e87b67e684eeb4305325","commentary_obligation":"review","hft_ref":"hft_9b443b710c4d6a40756b","kind":"surprising_outlier","lane":"macro","lane_assignment_basis":"all explicit HFT anchors lie in the declared pericope","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"declared_pericope","source_local_id":"reader_hft_a:outlier_visible_record","source_type":"hft","support_ids":["sup_a859b7bac146203ea18e"],"title":"outlier_visible_record","trust":"legacy_unbound"}],"connection_registry":[{"connection_evidence_ref":"conn_ev_0944968f56b57d177fd0","connection_ref":"conn_a71df11d358f47f52baa","note":"Places final accounting with God, clarifying why the messenger's task in 88:21 is limited.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_af08520a14b4106dbd7e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:26","source_note":"Immediate role boundary: the messenger only reminds.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:26","source_target_components":["88:26"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:26","target_evidence":{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"},"target_ref":"88:26"},{"connection_evidence_ref":"conn_ev_e55fae173f2f8b9d9903","connection_ref":"conn_59feecd8a686e6e857f6","note":"The immediate sequel supplies the decisive non-control boundary for the command in 88:21.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_bbbbf5bc630732735548","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:22","source_note":"The immediately preceding command defines the messenger's task as reminding.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:22","source_target_components":["88:22"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:22","target_evidence":{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"},"target_ref":"88:22"},{"connection_evidence_ref":"conn_ev_abead34f464d07cbc9b5","connection_ref":"conn_57f32e1cb4099744c4ae","note":"One of the immediately preceding signs whose contemplation gives concrete content to 88:21.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_394f99f5186b44440566","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"weak","source_focus_ref":"88:19","source_note":"The nearby reminder command offers only a secondary contextual boundary.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:19","source_target_components":["88:19"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:19","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},"target_ref":"88:19"},{"connection_evidence_ref":"conn_ev_6b9ad55546fc90f66795","connection_ref":"conn_40828ac7b9d3c7844366","note":"An immediately preceding sign that concretely supplies the observational content of 88:21.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_97a7559226fa62ca5a2e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:18","source_note":"Immediate sequel makes the observation function as reminder rather than a standalone description.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:18","source_target_components":["88:18"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:18","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},"target_ref":"88:18"},{"connection_evidence_ref":"conn_ev_5d0405d3914c44989c4a","connection_ref":"conn_c45d42700c44710a8169","note":"The final immediate sign completes the observational material to be recalled in 88:21.","origin":"authored_focus_row","prior_label":"medium","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_9ca9175b77c7e43ab5a9","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"medium","source_focus_ref":"88:20","source_note":"The ensuing reminder sets the function of the preceding observations, without redefining earth.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:20","source_target_components":["88:20"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:20","target_evidence":{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},"target_ref":"88:20"},{"connection_evidence_ref":"conn_ev_724a7fca7e025012c2ac","connection_ref":"conn_335dfbae40dcd83ab1af","note":"The first immediate sign provides the clearest concrete material that 88:21 tells the messenger to recall.","origin":"authored_focus_row","prior_label":"strong","qualification":{"boundary":"Use this row to discover and assess the stated relation. The exact target Arabic is supplied, but target morphology and lexical analysis are not. Do not invent those missing details. Opposite-direction nominations and counterevidence remain visible, but neither is a focus-direction verdict.","has_reciprocal_counterevidence":false,"has_reciprocal_missing_ayah_suggestion":false,"has_reciprocal_nomination":true,"prior_label_is_not_a_decision":true,"reciprocal_source_direction_labels_are_not_focus_decisions":true,"self_reference_is_source_emphasis_not_reciprocity":false,"source_note_is_range_level":false,"source_row_role_is_provenance_not_a_decision":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_57002fc1950314378bb4","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:17","source_note":"Names reminder as the proper role, completing the no-control boundary with 88:22.","source_row_role":"ranked_review","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope","source_row_role":"ranked_review","source_target_component_ref":"88:17","source_target_components":["88:17"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:17","target_evidence":{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},"target_ref":"88:17"},{"connection_ref":"conn_b27d963a8232419c4054","note":null,"origin":"derived_reciprocal_seed","prior_label":null,"qualification":{"boundary":"At least one source-direction review meaningfully linked this target back to the focus ayah. Treat its note and label only as a discovery nomination. Reassess the relation from the focus ayah using the supplied exact target Arabic; do not invent missing target morphology or inherit the source label.","derived_reciprocal_counterevidence":false,"derived_reciprocal_seed":true,"has_missing_ayah_suggestion_source_row":true,"has_ranked_review_source_row":false,"has_reciprocal_counterevidence":false,"has_reciprocal_nomination":true,"receiving_direction_requires_fresh_assessment":true,"source_direction_labels_are_not_focus_decisions":true,"source_row_roles_are_provenance_not_decisions":true,"target_ayah_text_supplied":true,"target_morphology_supplied":false},"reciprocal_evidence":[{"connection_evidence_ref":"conn_ev_0470a0e6c8e3a0e7ea9e","projection_record_type":"reciprocal_nomination","receiving_direction_label":null,"record_type":"reciprocal_nomination","relation_scope":"same_surah","source_direction_label":"strong","source_focus_ref":"88:23","source_note":"Missing immediate command to remind; it establishes the function preceding the exception.","source_row_role":"missing_ayah_suggestion","source_target_component_ref":"88:21","source_target_components":["88:21"],"source_target_is_range":false,"source_target_range_boundary":null,"source_target_range_evidence":[],"source_target_ref":"88:21"}],"relation_scope":"declared_pericope_reciprocal_evidence","target_evidence":{"arabic_uthmani":"إِلَّا مَن تَوَلَّىٰ وَكَفَرَ","ayah_ref":"88:23"},"target_ref":"88:23"}],"focus":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:21:1:1","qac_word_ref":"88:21:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","root_ar":"ذ ك ر","surface_ar":"ذَكِّرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:21:2:1","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"88:21:2:2","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"88:21:3:1","qac_word_ref":"88:21:3","root_ar":"","surface_ar":"أَنتَ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","root_ar":"ذ ك ر","surface_ar":"مُذَكِّرٌ"}],"word_analysis_qac_refs":[["88:21:1:1"],["88:21:1:2"],["88:21:2:1","88:21:2:2"],["88:21:3:1"],["88:21:4:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["88:21:1","88:21:2","88:21:3","88:21:4","88:21:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"88:21:1:1","qac_word_ref":"88:21:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذُكِّرَ","morph_features":"STEM|POS:V|IMPV|(II)|LEM:*uk~ira|ROOT:*kr|2MS","morpheme_role":"STEM","pos":"V","qac_ref":"88:21:1:2","qac_word_ref":"88:21:1","root_ar":"ذ ك ر","surface_ar":"ذَكِّرْ"},{"lemma_ar":"إِنّ","morph_features":"STEM|POS:ACC|LEM:<in~|SP:<in~","morpheme_role":"STEM","pos":"ACC","qac_ref":"88:21:2:1","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"إِنَّ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:PREV|LEM:maA","morpheme_role":"STEM","pos":"PREV","qac_ref":"88:21:2:2","qac_word_ref":"88:21:2","root_ar":"","surface_ar":"مَآ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|2MS","morpheme_role":"STEM","pos":"PRON","qac_ref":"88:21:3:1","qac_word_ref":"88:21:3","root_ar":"","surface_ar":"أَنتَ"},{"lemma_ar":"مُذَكِّر","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:mu*ak~ir|ROOT:*kr|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"88:21:4:1","qac_word_ref":"88:21:4","root_ar":"ذ ك ر","surface_ar":"مُذَكِّرٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["88:21:1:1"],["88:21:1:2"],["88:21:2:1","88:21:2:2"],["88:21:3:1"],["88:21:4:1"]],"word_analysis_refs":["88:21:1","88:21:2","88:21:3","88:21:4","88:21:5"],"word_rows":[{"analysis_record_ref":"88:21:1","analytic_gloss_range_en":"consequential or resumptive connector prefixed to the following command","analytic_root_gloss_range_en":null,"qac_refs":["88:21:1:1"],"root":{},"surface":{"arabic":"فَ","transliteration":"fa"}},{"analysis_record_ref":"88:21:2","analytic_gloss_range_en":"Form II imperative to cause reminder, with object and instrument unstated","analytic_root_gloss_range_en":"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; the local Form II command activates the reminder/admonitory speech branch","qac_refs":["88:21:1:2"],"root":{"arabic":"ذ ك ر","transliteration":"dh-k-r"},"surface":{"arabic":"ذَكِّرْ","transliteration":"dhakkir"}},{"analysis_record_ref":"88:21:3","analytic_gloss_range_en":"restrictive particle that places the following nominal clause under limitation","analytic_root_gloss_range_en":null,"qac_refs":["88:21:2:1","88:21:2:2"],"root":{},"surface":{"arabic":"إِنَّمَآ","transliteration":"innamā"}},{"analysis_record_ref":"88:21:4","analytic_gloss_range_en":"independent second-person masculine singular pronoun serving as subject of the restrictive nominal clause","analytic_root_gloss_range_en":null,"qac_refs":["88:21:3:1"],"root":{},"surface":{"arabic":"أَنتَ","transliteration":"anta"}},{"analysis_record_ref":"88:21:5","analytic_gloss_range_en":"Form II active participle: reminder-agent, predicate of the explicit addressee under restriction","analytic_root_gloss_range_en":"broad root range includes remembering, mentioning, worshipful remembrance, scripture, renown, and reminder or admonition; this active participle selects the reminder-agent role and excludes coercive control","qac_refs":["88:21:4:1"],"root":{"arabic":"ذ ك ر","transliteration":"dh-k-r"},"surface":{"arabic":"مُذَكِّرٌۭ","transliteration":"mudhakkirun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":9,"missing_anchor_refs":[],"supplied_unique_anchor_count":9},"assigned_record_count":6,"assigned_records":[{"anchor_refs":["88:17","88:18","88:19","88:20","88:21"],"branch_refs":["root_000434/B001","root_000516/B009","root_000582/B001","root_000703/B001","root_001507/B001","root_001520/B001"],"candidate_id":"cand_50b4fe7c7366cc8e50fa","evidence_scope":"declared_pericope","hft_ref":"hft_8f611b505d15081d6521","item_id":"delta_observational_how","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_observational_how","support_id":"sup_03e31e82f6f0882615fa"},{"anchor_refs":["88:21","88:22"],"branch_refs":["root_000516/B009","root_000704/B003","root_001390/B001"],"candidate_id":"cand_433f025a662154dc3fc1","evidence_scope":"declared_pericope","hft_ref":"hft_c8d1daa4eb81b9820469","item_id":"delta_noncoercive_role_boundary","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_noncoercive_role_boundary","support_id":"sup_edc4a8bad16b57ab51d7"},{"anchor_refs":["88:21","88:25","88:26"],"branch_refs":["root_000065/B001","root_000318/B001","root_000516/B003"],"candidate_id":"cand_b78e12f6673ad80c667a","evidence_scope":"declared_pericope","hft_ref":"hft_0d84b994d39e73733f1a","item_id":"delta_return_before_account","kind":"context_delta","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:delta_return_before_account","support_id":"sup_d78a84e1907e7bcf5380"},{"anchor_refs":["88:21","88:22"],"branch_refs":["root_000516/B002","root_000704/B003"],"candidate_id":"cand_84cf4ca370f3d9ffc3b6","evidence_scope":"declared_pericope","hft_ref":"hft_b33efeae5b0ee376292d","item_id":"outlier_pointed_noncoercive_edge","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_pointed_noncoercive_edge","support_id":"sup_265dad3a27c0e243af97"},{"anchor_refs":["88:21","88:24"],"branch_refs":["root_000516/B009","root_000994/B003","root_000994/B005"],"candidate_id":"cand_439262cac08c505ea74d","evidence_scope":"declared_pericope","hft_ref":"hft_76afbd4f7da7196b35e7","item_id":"outlier_preventive_weaning","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_preventive_weaning","support_id":"sup_d2df2804962505bc38b9"},{"anchor_refs":["88:18","88:21","88:26"],"branch_refs":["root_000318/B001","root_000516/B008","root_001650/B001"],"candidate_id":"cand_e87b67e684eeb4305325","evidence_scope":"declared_pericope","hft_ref":"hft_9b443b710c4d6a40756b","item_id":"outlier_visible_record","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors lie in the declared pericope","owning_lane":"macro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_visible_record","support_id":"sup_a859b7bac146203ea18e"}],"diagnostics":[],"lane_counts":{"global":15,"macro":6,"micro":3},"packet_summary":{"ayah_count":26,"focus_ref":"88:21","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"غ ش و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001088","furuq_root_norm":"غ ش و","furuq_source_root_norm":"غ ش و","is_dominant":true,"target_occurrences":18,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001089","furuq_root_norm":"غ ش ي","furuq_source_root_norm":"غ ش ي","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"ص ل ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":true,"target_occurrences":6,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":false,"target_occurrences":3,"target_rank":2}]},{"qac_root":"س ق ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000722","furuq_root_norm":"س ق ي","furuq_source_root_norm":"س ق ي","is_dominant":true,"target_occurrences":14,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000762","furuq_root_norm":"س و ق","furuq_source_root_norm":"س و ق","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ء ن ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000063","furuq_root_norm":"ء ن ي","furuq_source_root_norm":"أ ن ي","is_dominant":true,"target_occurrences":5,"target_rank":1},{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000068","furuq_root_norm":"ء و ن","furuq_source_root_norm":"أ و ن","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"س ع ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000709","furuq_root_norm":"س ع ي","furuq_source_root_norm":"س ع ي","is_dominant":true,"target_occurrences":26,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000760","furuq_root_norm":"س و ع","furuq_source_root_norm":"س و ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]},{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]}],"window":["88:1","88:2","88:3","88:4","88:5","88:6","88:7","88:8","88:9","88:10","88:11","88:12","88:13","88:14","88:15","88:16","88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"broader_than_declared_pericope","reader_identity":[{"focus_ref":"88:21","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":14,"unstructured_record_count":0},"identity":{"ayah_ref":"88:21","lane":"macro","linguistic_source_ref":"88:21","surface_ref":"88:21","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"88:21","target_tokens":[["O",["88:21:1"]],["halde",["88:21:1"]],["hatırlat",["88:21:1"]],["sen",["88:21:3"]],["yalnızca",["88:21:2"]],["hatırlatansın",["88:21:4"]]],"text":"O halde hatırlat; sen yalnızca hatırlatansın."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":6,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"pericope-anchored channels and exactly matching HFT only","pericope":{"ayah_from":17,"ayah_to":26,"id":"s088-p02-017-026","label":"Creation signs and the duty to remind","number":2,"refs":["88:17","88:18","88:19","88:20","88:21","88:22","88:23","88:24","88:25","88:26"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"blocked","docket_ready":false}},"selected_context_units":[{"automatic_prefatory_basmala_membership":true,"ayah_ref":"88:0","context_kind":"host_prefatory_basmala","evidence":{"context_ayat":[{"ref":"88:0","root_occurrences":[{"lemmas_ar":["ٱسْم"],"occurrence_count":1,"pos_tags":["N"],"root":"س م و","surfaces_ar":["سْمِ"],"word_indices":["1"]},{"lemmas_ar":["ٱللَّه"],"occurrence_count":1,"pos_tags":["PN"],"root":"ء ل ه","surfaces_ar":["ٱللَّهِ"],"word_indices":["2"]},{"lemmas_ar":["رَّحْمَٰن","رَّحِيم"],"occurrence_count":2,"pos_tags":["ADJ","ADJ"],"root":"ر ح م","surfaces_ar":["رَّحْمَٰنِ","رَّحِيمِ"],"word_indices":["3","4"]}],"root_sequence":["س م و","ء ل ه","ر ح م","ر ح م"],"text_ar":"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"}],"context_order":["88:0"],"context_root_cues":[{"root":"س م و","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"العلو والارتفاع"},{"branch_id":"B002","branch_image_ar":"الشخص المرتفع الظاهر"},{"branch_id":"B003","branch_image_ar":"تطاول الفحل على الشول"},{"branch_id":"B004","branch_image_ar":"السماء وما علا فأظل"},{"branch_id":"B005","branch_image_ar":"الاسم تنويه ودلالة"},{"branch_id":"B006","branch_image_ar":"الخروج للصيد"},{"branch_id":"B007","branch_image_ar":"المساماة والمباراة"},{"branch_id":"B008","branch_image_ar":"الصيت الحسن المنتشر"}],"mapped_root_id":"root_000745","mapped_root_norm":"س م و"},{"branches":[{"branch_id":"B001","branch_image_ar":"أثر وسم ظاهر يجعل الشيء معروفا"},{"branch_id":"B002","branch_image_ar":"سمة يرى بها الناظر دلالة الحال"},{"branch_id":"B003","branch_image_ar":"مطر أول يسم الأرض بالنبات"},{"branch_id":"B004","branch_image_ar":"موسم معلم يجتمع إليه الناس"},{"branch_id":"B005","branch_image_ar":"حسن عليه أثر الجمال"},{"branch_id":"B006","branch_image_ar":"وسمة يخضب بورقها"}],"mapped_root_id":"root_001650","mapped_root_norm":"و س م"},{"branches":[{"branch_id":"B001","branch_image_ar":"ثقب ضيق يدخل منه الشيء"},{"branch_id":"B002","branch_image_ar":"سم يدخل البدن"},{"branch_id":"B003","branch_image_ar":"خاصّة داخلة في الباطن"},{"branch_id":"B004","branch_image_ar":"ريح حارة نافذة"},{"branch_id":"B005","branch_image_ar":"إصلاح يدخل بين المتباينين"},{"branch_id":"B006","branch_image_ar":"ودع وخرز مثقوب للزينة"},{"branch_id":"B007","branch_image_ar":"سمامة وطير سريع"},{"branch_id":"B008","branch_image_ar":"أسماء السمسم والخفة"},{"branch_id":"B009","branch_image_ar":"لا سم ولا حم"},{"branch_id":"B010","branch_image_ar":"السامة موت"},{"branch_id":"B011","branch_image_ar":"وجه مقصود وغور مسبور"},{"branch_id":"B012","branch_image_ar":"سد وشد"},{"branch_id":"B013","branch_image_ar":"شخص الشيء وسماوته"}],"mapped_root_id":"root_000743","mapped_root_norm":"س م م"}]},{"root":"ء ل ه","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"التعبد والمعبود"},{"branch_id":"B002","branch_image_ar":"اسم الله في القسم والنداء"}],"mapped_root_id":"root_000047","mapped_root_norm":"ء ل ه"}]},{"root":"ر ح م","targets":[{"branches":[{"branch_id":"B001","branch_image_ar":"الرَّحْمَة والرقة"},{"branch_id":"B002","branch_image_ar":"الرَّحِم والقرابة"},{"branch_id":"B003","branch_image_ar":"رَحِم الأنثى"},{"branch_id":"B004","branch_image_ar":"وجع الرَّحِم بعد الولادة"}],"mapped_root_id":"root_000552","mapped_root_norm":"ر ح م"}]}],"protocol":"commentary-v5-native-context-member-v1"},"focus_eligible":false,"lane":"macro","linguistic_source_ref":"1:1","surface_ref":"88:0"}],"support_registry":[{"anchor_evidence":[{"arabic_uthmani":"أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ","ayah_ref":"88:17"},{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},{"arabic_uthmani":"وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ","ayah_ref":"88:19"},{"arabic_uthmani":"وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ","ayah_ref":"88:20"},{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":5,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":5,"target_morphology_supplied":false},"branch_refs":["root_000434/B001","root_000516/B009","root_000582/B001","root_000703/B001","root_001507/B001","root_001520/B001"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000516","role":"The reminder as a means of renewed presence gives the observational prompts their mnemonic function.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_001520","role":"Directing sight or insight supplies the attentional action through which the reminder works.","root":"ن ظ ر","source_ref":"88:17","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000434","role":"Measuring and proportioning invites inspection of construction rather than bare object recognition.","root":"خ ل ق","source_ref":"88:17","source_word_indices":["6"]},{"branch_id":"B001","mapped_root_id":"root_000582","role":"Elevation contributes a vertical relation for inquiry.","root":"ر ف ع","source_ref":"88:18","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_001507","role":"Erect and conspicuous setting contributes stability and placement as an observable relation.","root":"ن ص ب","source_ref":"88:19","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000703","role":"An even extended surface completes the shift from vertical structures to a traversable horizontal field.","root":"س ط ح","source_ref":"88:20","source_word_indices":["4"]}],"changed_reading":{"after":"Redirect attention and ask how the visible world is configured so recognition can reactivate through observation.","before":"Repeat a settled conclusion to the audience."},"confidence":"strong","mechanism":"The four-object sequence redirects sight and insight toward measured making, elevation, erect placement, and extended surface. The reminder thus prompts an inquiry into relations and construction; it activates recognition by disciplined looking rather than supplying every conclusion.","model_id":"delta_observational_how","reader_inference":"The packet supplies directed looking, repeated how-questions, and a measured vertical-to-horizontal construction sequence; I infer that guided inquiry causes recollection. A live alternative is that the sequence supplies proofs or wonders while reminding remains only the later verbal command.","status":"revised","structural_cues":["The branchless root ك ي ف appears only as a structural interrogative at 88:17 word 5 and at 88:18, 88:19, and 88:20 word 3; no mapped or branch ID is assigned to it.","Repeated وَإِلَى directs attention successively to animal, sky, mountains, and earth.","Four passive predicates foreground how each object came to have its observable configuration."],"trigger_roots":["ن ظ ر","خ ل ق","ر ف ع","ن ص ب","س ط ح"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_observational_how","source_type":"hft","support_id":"sup_03e31e82f6f0882615fa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000516/B009","root_000704/B003","root_001390/B001"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000516","role":"The reminder-agent supplies a positive but limited office centered on making content present.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_001390","role":"Present-state negation explicitly removes the following supervisory identity from the addressee.","root":"ل ي س","source_ref":"88:22","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"The image of a dominating overseer defines the coercive function excluded from reminding.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"Make the matter present with urgency, but do not confuse presentation with control over persons or outcomes.","before":"Remind until the audience's response has been secured."},"confidence":"strong","mechanism":"The restrictive identity in the focus is immediately given a negative boundary: the reminder presents and re-presents, but does not become the overseeing power who arranges people under compulsion.","model_id":"delta_noncoercive_role_boundary","reader_inference":"The packet supplies a restricted reminder identity and an explicit denial of dominating oversight; I infer that response and enforcement lie outside the assigned role. The live alternative is a narrower legal limitation that says nothing about the ordinary persuasive force of speech.","status":"revised","structural_cues":["إِنَّمَا أَنتَ in 88:21 restricts identity, and لَّسْتَ عَلَيْهِم in 88:22 immediately states what that identity is not.","The repeated second-person أنت and تاء of لست hold the same agent across the positive and negative clauses."],"trigger_roots":["ل ي س","س ط ر"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_noncoercive_role_boundary","source_type":"hft","support_id":"sup_edc4a8bad16b57ab51d7","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"إِنَّ إِلَيْنَآ إِيَابَهُمْ","ayah_ref":"88:25"},{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000065/B001","root_000318/B001","root_000516/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000516","role":"Recall supplies a return of content to present mind.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_000065","role":"Return to a destination projects the mnemonic return onto the persons' later trajectory.","root":"ء و ب","source_ref":"88:25","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and account give the later return its evaluative terminus.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"Return to awareness now, before the persons' unavoidable return and account later.","before":"Recall a message whose timing has no larger structure."},"confidence":"strong","mechanism":"Cognitive return in the focus anticipates personal return in 88:25 and reckoning in 88:26. The reminder becomes an early, reversible return to awareness before the later return and account, whose agency is explicitly assigned elsewhere.","model_id":"delta_return_before_account","reader_inference":"The packet supplies recall, eventual return, and subsequent account; I infer that present remembering is an anticipatory return with room for changed action. A live alternative is that the shared return-shape is thematic sequencing rather than a mechanism internal to ذَكِّرْ.","status":"strengthened","structural_cues":["The closing إِلَيْنَا and عَلَيْنَا transfer return and account away from the second-person reminder.","ثُمَّ sequences account after return, whereas the focus reminder occurs before both."],"trigger_roots":["ء و ب","ح س ب"]},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:delta_return_before_account","source_type":"hft","support_id":"sup_d78a84e1907e7bcf5380","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ","ayah_ref":"88:22"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000516/B002","root_000704/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000516","role":"Hardness and sharpness contribute a possible bracing intensity to the act of reminding.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B003","mapped_root_id":"root_000704","role":"Dominating oversight supplies the excluded extreme that contains sharpness within speech rather than compulsion.","root":"س ط ر","source_ref":"88:22","source_word_indices":["3"]}],"changed_reading":{"after":"Deliver a pointed, bracing reminder whose force remains verbal and non-dominating.","before":"Remind in a semantically neutral tone."},"confidence":"exploratory","containment":"The hard, sharp, forceful branch is surprising beside ordinary mnemonic language, but it remains anchored in the twice-repeated focus root and can color the imperative's manner. Render it only as a pointed or bracing verbal edge, not as masculinity, violence, or coercive control, which 88:22 explicitly excludes.","focus_anchor":"The doubled ذ ك ر root joins a direct imperative to the identity مُذَكِّر, allowing a branch-level tonal activation while إنما keeps the office bounded.","outlier_id":"outlier_pointed_noncoercive_edge"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_pointed_noncoercive_edge","source_type":"hft","support_id":"sup_265dad3a27c0e243af97","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ","ayah_ref":"88:24"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":2,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":2,"target_morphology_supplied":false},"branch_refs":["root_000516/B009","root_000994/B003","root_000994/B005"],"payload":{"activation_trace":[{"branch_id":"B009","mapped_root_id":"root_000516","role":"The reminder supplies a present intervention capable of reopening awareness.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B003","mapped_root_id":"root_000994","role":"Restraint, prevention, and weaning contribute the exploratory idea of interruption before a settled harmful course.","root":"ع ذ ب","source_ref":"88:24","source_word_indices":["1","3"]},{"branch_id":"B005","mapped_root_id":"root_000994","role":"Painful punishment preserves the overt endpoint and prevents the weaning image from replacing the source phrase's direct sense.","root":"ع ذ ب","source_ref":"88:24","source_word_indices":["1","3"]}],"changed_reading":{"after":"Exploratorily, the reminder opens a non-coercive interval in which one may be weaned from refusal before punitive consequence.","before":"The reminder merely announces punishment."},"confidence":"exploratory","containment":"The restraint or weaning image is branch-distant from the overt punishment wording in 88:24, so it must not replace punishment as the verse's gloss. It remains useful as a root-internal activation: the non-coercive reminder may be rendered as a preventive interruption that can detach a hearer from refusal before punishment, with the causal arrow marked as exploratory.","focus_anchor":"The imperative asks the reminder-agent to intervene before the post-focus sequence of turning away and punishment.","outlier_id":"outlier_preventive_weaning"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_preventive_weaning","source_type":"hft","support_id":"sup_d2df2804962505bc38b9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ","ayah_ref":"88:18"},{"arabic_uthmani":"فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ","ayah_ref":"88:21"},{"arabic_uthmani":"ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم","ayah_ref":"88:26"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":3,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":3,"target_morphology_supplied":false},"branch_refs":["root_000318/B001","root_000516/B008","root_001650/B001"],"payload":{"activation_trace":[{"branch_id":"B008","mapped_root_id":"root_000516","role":"A document preserving a right turns reminder into exploratory service of notice or durable claim.","root":"ذ ك ر","source_ref":"88:21","source_word_indices":["1","4"]},{"branch_id":"B001","mapped_root_id":"root_001650","role":"The non-dominant mapped image of a visible identifying mark makes the observed world analogically legible as evidence.","root":"س م و","source_ref":"88:18","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000318","role":"Counting and account provide the later forum in which preserved notice and legible evidence would matter.","root":"ح س ب","source_ref":"88:26","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, the reminder serves notice and makes a claim legible against a visible field that culminates in account.","before":"The reminder is a transient spoken prompt."},"confidence":"exploratory","containment":"This reading joins the focus root's rights-document branch to a non-dominant split mapping of the sky root as a visible identifying mark, then to final account. It remains packet-anchored but is form-distant: render it as an abductive analogy of notice, legibility, and record, never as an etymological claim that سَمَاء derives from وَسْم or as the primary gloss of مُذَكِّر.","focus_anchor":"The focus repeats ذ ك ر in command and agent forms, and its branch inventory includes a written instrument that preserves a right or claim.","outlier_id":"outlier_visible_record"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"broader_than_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"macro","source_local_id":"reader_hft_a:outlier_visible_record","source_type":"hft","support_id":"sup_a859b7bac146203ea18e","trust":"legacy_unbound"}]}
</lane_packet_json>
